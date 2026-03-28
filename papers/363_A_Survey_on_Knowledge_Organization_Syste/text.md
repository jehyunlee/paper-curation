## A Survey on Knowledge Graphs: Representation, Acquisition and Applications

Shaoxiong Ji, Shirui Pan, Member, IEEE, Erik Cambria, Senior Member, IEEE, Pekka Marttinen, Philip S. Yu, Life Fellow, IEEE

### arXiv:2002.00388v4[cs.CL]1 Apr 2021

Abstract—Human knowledge provides a formal understanding of the world. Knowledge graphs that represent structural relations between entities have become an increasingly popular research direction towards cognition and human-level intelligence. In this survey, we provide a comprehensive review of knowledge graph covering overall research topics about 1) knowledge graph representation learning, 2) knowledge acquisition and completion, 3) temporal knowledge graph, and 4) knowledge-aware applications, and summarize recent breakthroughs and perspective directions to facilitate future research. We propose a full-view categorization and new taxonomies on these topics. Knowledge graph embedding is organized from four aspects of representation space, scoring function, encoding models, and auxiliary information. For knowledge acquisition, especially knowledge graph completion, embedding methods, path inference, and logical rule reasoning, are reviewed. We further explore several emerging topics, including meta relational learning, commonsense reasoning, and temporal knowledge graphs. To facilitate future research on knowledge graphs, we also provide a curated collection of datasets and open-source libraries on different tasks. In the end, we have a thorough outlook on several promising research directions.

Index Terms—Knowledge graph, representation learning, knowledge graph completion, relation extraction, reasoning, deep learning.

I. INTRODUCTION

# I

NCORPORATING human knowledge is one of the research directions of artiﬁcial intelligence (AI). Knowledge

representation and reasoning, inspired by human problem solving, is to represent knowledge for intelligent systems to gain the ability to solve complex tasks [1], [2]. Recently, knowledge graphs as a form of structured human knowledge have drawn great research attention from both the academia and the industry [3]–[6]. A knowledge graph is a structured representation of facts, consisting of entities, relationships, and semantic descriptions. Entities can be real-world objects and abstract concepts, relationships represent the relation

Manuscript received August 09, 2020; revised November xx, 2020; accepted March 30, 2021. This work is supported in part by NSF under grants III1763325, III-1909323, SaTC-1930941, in part by the Agency for Science, Technology and Research (A*STAR) under its AME Programmatic Funding Scheme (Project #A18A2b0046), and in part by the Academy of Finland (grants 336033, 315896), BusinessFinland (grant 884/31/2018), and EU H2020 (grant 101016775). (Corresponding author: Shirui Pan.)

S. Ji and P. Marttinen are with Aalto University, Finland. E-mail: {shaoxiong.ji; pekka.marttinen}@aalto.ﬁ

S. Pan is with the Department of Data Science and AI, Faculty of IT, Monash University, Australia. E-mail: shirui.pan@monash.edu

E. Cambria is with Nanyang Technological University, Singapore. Email: cambria@ntu.edu.sg

P.S. Yu is with University of Illinois at Chicago, USA. E-mail: psyu@uic.edu

between entities, and semantic descriptions of entities, and their relationships contain types and properties with a well-deﬁned meaning. Property graphs or attributed graphs are widely used, in which nodes and relations have properties or attributes.

The term of knowledge graph is synonymous with knowledge base with a minor difference. A knowledge graph can be viewed as a graph when considering its graph structure [7]. When it involves formal semantics, it can be taken as a knowledge base for interpretation and inference over facts [8]. Examples of knowledge base and knowledge graph are illustrated in Fig. 1. Knowledge can be expressed in a factual triple in the form of (head, relation,tail) or (subject, predicate,object) under the resource description framework (RDF), for example, (Albert Einstein, WinnerOf, Nobel Prize). It can also be represented as a directed graph with nodes as entities and edges as relations. For simplicity and following the trend of the research community, this paper uses the terms knowledge graph and knowledge base interchangeably.

(Albert Einstein, BornIn, German Empire) (Albert Einstein, SonOf, Hermann Einstein) (Albert Einstein, GraduateFrom, University of Zurich) (Albert Einstein, WinnerOf, Nobel Prize in Physics) (Albert Einstein, ExpertIn, Physics) (Nobel Prize in Physics, AwardIn, Physics) (The theory of relativity, TheoryOf, Physics) (Albert Einstein, SupervisedBy, Alfred Kleiner) (Alfred Kleiner, ProfessorOf, University of Zurich) (The theory of relativity, ProposedBy, Albert Einstein) (Hans Albert Einstein, SonOf, Albert Einstein)

The theory of relativity

Hans Albert Einstein

Physics

TheoryOf

SonOf

ProposedBy

ExpertIn

AwardIn

Hermann Einstein

SonOf

Albert Einstein

Nobel Prize in Physics

WinnerOf

BornIn

SupervisedBy

German Empire

GraduateFrom

Alfred Kleiner

University of Zurich

ProfessorOf

(a) Factual triples in knowledge base.

(b) Entities and relations in knowledge graph.

Fig. 1: An example of knowledge base and knowledge graph.

Recent advances in knowledge-graph-based research focus on knowledge representation learning (KRL) or knowledge graph embedding (KGE) by mapping entities and relations into low-dimensional vectors while capturing their semantic meanings [5], [9]. Speciﬁc knowledge acquisition tasks include knowledge graph completion (KGC), triple classiﬁcation, entity recognition, and relation extraction. Knowledge-aware models beneﬁt from the integration of heterogeneous information, rich ontologies and semantics for knowledge representation, and multi-lingual knowledge. Thus, many real-world applications such as recommendation systems and question answering have been brought about prosperity with the ability of commonsense understanding and reasoning. Some real-world products, for example, Microsoft’s Satori and Google’s Knowledge Graph [3], have shown a strong capacity to provide more efﬁcient services.

This paper conducts a comprehensive survey of current literature on knowledge graphs, which enriches graphs with more

context, intelligence, and semantics for knowledge acquisition and knowledge-aware applications. Our main contributions are summarized as follows.

- • Comprehensive review. We conduct a comprehensive review of the origin of knowledge graph and modern techniques for relational learning on knowledge graphs. Major neural architectures of knowledge graph representation learning and reasoning are introduced and compared. Moreover, we provide a complete overview of many applications in different domains.
- • Full-view categorization and new taxonomies. A fullview categorization of research on knowledge graph, together with ﬁne-grained new taxonomies are presented. Speciﬁcally, in the high-level, we review the research on knowledge graphs in four aspects: KRL, knowledge acquisition, temporal knowledge graphs, and knowledgeaware applications. For KRL, we further propose ﬁnegrained taxonomies into four views, including representation space, scoring function, encoding models, and auxiliary information. For knowledge acquisition, KGC is reviewed under embedding-based ranking, relational path reasoning, logical rule reasoning, and meta relational learning; entity acquisition tasks are divided into entity recognition, typing, disambiguation, and alignment; and relation extraction is discussed according to the neural paradigms.
- • Wide coverage on emerging advances. We provide wide coverage on emerging topics, including transformer-based knowledge encoding, graph neural network (GNN) based knowledge propagation, reinforcement learning-based path reasoning, and meta relational learning.
- • Summary and outlook on future directions. This survey provides a summary of each category and highlights promising future research directions.


The remainder of this survey is organized as follows: ﬁrst, an overview of knowledge graphs including history, notations, deﬁnitions, and categorization is given in Section II; then, we discuss KRL in Section III from four scopes; next, our review goes to tasks of knowledge acquisition and temporal knowledge graphs in Section IV and Section V; downstream applications are introduced in Section VI; ﬁnally, we discuss future research directions, together with a conclusion in the end. Other information, including KRL model training and a collection of knowledge graph datasets and open-source implementations, can be found in the appendices.

II. OVERVIEW A. A Brief History of Knowledge Bases

Knowledge representation has experienced a long-period history of development in the ﬁelds of logic and AI. The idea of graphical knowledge representation ﬁrstly dated back to 1956 as the concept of semantic net proposed by Richens [10], while the symbolic logic knowledge can go back to the General Problem Solver [1] in 1959. The knowledge base is ﬁrstly used with knowledge-based systems for reasoning and problemsolving. MYCIN [2] is one of the most famous rule-based expert systems for medical diagnosis with a knowledge base

of about 600 rules. Later, the community of human knowledge representation saw the development of frame-based language, rule-based, and hybrid representations. Approximately at the end of this period, the Cyc project1 began, aiming at assembling human knowledge. Resource description framework (RDF)2 and Web Ontology Language (OWL)3 were released in turn, and became important standards of the Semantic Web4. Then, many open knowledge bases or ontologies were published, such as WordNet, DBpedia, YAGO, and Freebase. Stokman and Vries [7] proposed a modern idea of structure knowledge in a graph in 1988. However, it was in 2012 that the concept of knowledge graph gained great popularity since its ﬁrst launch by Google’s search engine5, where the knowledge fusion framework called Knowledge Vault [3] was proposed to build large-scale knowledge graphs. A brief road map of knowledge base history is illustrated in Fig. 10 in Appendix A. Many general knowledge graph databases and domain-speciﬁc knowledge bases have been released to facilitate research. We introduce more general and domain-speciﬁc knowledge bases in Appendices F-A1 and F-A2.

- B. Deﬁnitions and Notations

Most efforts have been made to give a deﬁnition by describing general semantic representation or essential characteristics. However, there is no such wide-accepted formal deﬁnition. Paulheim [11] deﬁned four criteria for knowledge graphs. Ehrlinger and W¨oß [12] analyzed several existing deﬁnitions and proposed Deﬁnition 1, which emphasizes the reasoning engine of knowledge graphs. Wang et al. [5] proposed a deﬁnition as a multi-relational graph in Deﬁnition 2. Following previous literature, we deﬁne a knowledge graph as G = {E,R,F}, where E, R and F are sets of entities, relations and facts, respectively. A fact is denoted as a triple (h,r,t) ∈ F.

- Deﬁnition 1 (Ehrlinger and W¨oß [12]). A knowledge graph acquires and integrates information into an ontology and applies a reasoner to derive new knowledge.
- Deﬁnition 2 (Wang et al. [5]). A knowledge graph is a multirelational graph composed of entities and relations which are regarded as nodes and different types of edges, respectively.


Speciﬁc notations and their descriptions are listed in Table I. Details of several mathematical operations are explained in Appendix B.

- C. Categorization of Research on Knowledge Graph


This survey provides a comprehensive literature review on the research of knowledge graphs, namely KRL, knowledge acquisition, and a wide range of downstream knowledgeaware applications, where many recent advanced deep learning techniques are integrated. The overall categorization of the research is illustrated in Fig. 2.

1http://cyc.com 2Released as W3C recommendation in 1999 available at http://w3.org/TR/

1999/REC-rdf-syntax-19990222.

- 3http://w3.org/TR/owl-guide
- 4http://w3.org/standards/semanticweb
- 5http://blog.google/products/search/introducing-knowledge-graph-things-not


TABLE I: Notations and descriptions.

Notation Description

G A knowledge graph F A set of facts (h, r, t) A triple of head, relation and tail (h, r, t) Embedding of head, relation and tail r ∈ R, e ∈ E Relation set and entity set v ∈ V Vertex in vertice set ξ ∈ EG Edge in edge set es, eq, et Source/query/current entity rq Query relation < w1, . . . , wn > Text corpus d·(·) Distance metric in speciﬁc space fr(h, t) Scoring function σ(·), g(·) Non-linear activation function

Mr Mapping matrix M Tensor L Loss function

Rd d dimensional real-valued space Cd d dimensional complex space Hd d dimensional hypercomplex space Td d dimensional torus space Bdc d dimensional hyperbolic space with curvature c N(u, σ2I) Gaussian distribution

h, t Hermitian dot product t ⊗ r Hamilton product h ◦ t, h t Hadmard (element-wise) product h t Circular correlation concat(), [h, r] Vectors/matrices concatenation ω Convolutional ﬁlters ∗ Convolution operator

convolutional networks (GCNs), adversarial training, reinforcement learning, deep residual learning, and transfer learning.

Temporal Knowledge Graphs incorporate temporal information for representation learning. This survey categorizes four research ﬁelds, including temporal embedding, entity dynamics, temporal relational dependency, and temporal logical reasoning.

Knowledge-aware Applications include natural language understanding (NLU), question answering, recommendation systems, and miscellaneous real-world tasks, which inject knowledge to improve representation learning.

|Representation Space|
|---|


|Natural Language Understanding|
|---|


|Question Answering|
|---|


|Scoring Function|
|---|


|Dialogue Systems|
|---|


- - Recognition
- - Typing
- - Disambiguation
- - Alignment - Neural Nets

- - Attention
- - GCN
- - GAN
- - RL
- - Others


- - Single-fact QA
- - Multi-hop Reasoning
- - Question Generation
- - Search Engine
- - Medical Applications
- - Mental Healthcare
- - Zero-shot Image Classiﬁcation
- - Text Generation
- - Sentiment Analysis


- - Point-wise - Manifold
- - Complex - Gaussian
- - Discrete


- - Distance
- - Semantic Matching
- - Others

- - Linear/Bilinear
- - Factorization
- - Neural Nets
- - CNN
- - RNN
- - Transformers
- - GCN


Knowledge Representation Learning

KnowledgeAware Applications

|Encoding Models|
|---|


|Recommender Systems|
|---|


|Auxiliary Information|
|---|


|Others Applications|
|---|


Knowledge Graph

- Textual - Type - Visual

Knowledge Acquisition

|Entity Discovery|
|---|


Temporal Knowledge Graph

|Relation Extraction|
|---|


|Temporal Embedding|
|---|


|Knowledge Graph Completion|
|---|


|Entity Dynamics|
|---|


- - Embedding-based Ranking
- - Path-based Reasoning
- - Rule-based Reasoning
- - Meta Relational Learning
- - Triple Classiﬁcation


|Temporal Relational Dependency|
|---|


|Temporal Logical Reasoning|
|---|


Fig. 2: Categorization of research on knowledge graphs.

Knowledge Representation Learning is a critical research issue of knowledge graph which paves the way for many knowledge acquisition tasks and downstream applications. We categorize KRL into four aspects of representation space, scoring function, encoding models and auxiliary information, providing a clear workﬂow for developing a KRL model. Speciﬁc ingredients include:

- 1) representation space in which the relations and entities are represented;
- 2) scoring function for measuring the plausibility of factual triples;
- 3) encoding models for representing and learning relational interactions;
- 4) auxiliary information to be incorporated into the embedding methods.


Representation learning includes point-wise space, manifold, complex vector space, Gaussian distribution, and discrete space. Scoring metrics are generally divided into distance-based and similarity matching based scoring functions. Current research focuses on encoding models, including linear/bilinear models, factorization, and neural networks. Auxiliary information considers textual, visual, and type information.

Knowledge Acquisition tasks are divided into three categories, i.e., KGC, relation extraction, and entity discovery. The ﬁrst one is for expanding existing knowledge graphs, while the other two discover new knowledge (aka relations and entities) from the text. KGC falls into the following categories: embedding-based ranking, relation path reasoning, rule-based reasoning, and meta relational learning. Entity discovery includes recognition, disambiguation, typing, and alignment. Relation extraction models utilize attention mechanism, graph

D. Related Surveys

Previous survey papers on knowledge graphs mainly focus on statistical relational learning [4], knowledge graph reﬁnement [11], Chinese knowledge graph construction [13], knowledge reasoning [14], KGE [5] or KRL [9]. The latter two surveys are more related to our work. Lin et al. [9] presented KRL in a linear manner, with a concentration on quantitative analysis. Wang et al. [5] categorized KRL according to scoring functions and speciﬁcally focused on the type of information utilized in KRL. It provides a general view of current research only from the perspective of scoring metrics. Our survey goes deeper to the ﬂow of KRL and provides a full-scaled view from four-folds, including representation space, scoring function, encoding models, and auxiliary information. Besides, our paper provides a comprehensive review of knowledge acquisition and knowledge-aware applications with several emerging topics such as knowledge-graph-based reasoning and few-shot learning discussed.

III. KNOWLEDGE REPRESENTATION LEARNING

KRL is also known as KGE, multi-relation learning, and statistical relational learning in the literature. This section reviews recent advances on distributed representation learning with rich semantic information of entities and relations form four scopes including representation space (representing entities and relations, Sec. III-A), scoring function (measuring the plausibility of facts, Sec. III-B), encoding models (modeling the semantic interaction of facts, Sec. III-C), and auxiliary information (utilizing external information, Sec. III-D). We further provide a summary in Sec. III-E. The training strategies for KRL models are reviewed in Appendix D.

- A. Representation Space


The key issue of representation learning is to learn lowdimensional distributed embedding of entities and relations. Current literature mainly uses real-valued point-wise space (Fig. 3a) including vector, matrix and tensor space, while other kinds of space such as complex vector space (Fig. 3b), Gaussian space (Fig. 3c), and manifold (Fig. 3d) are utilized as well. The embedding space should follow three conditions, i.e., differentiability, calculation possibility, and deﬁnability of a scoring function [15].

1) Point-Wise Space: Point-wise Euclidean space is widely applied for representing entities and relations, projecting relation embedding in vector or matrix space, or capturing relational interactions. TransE [16] represents entities and relations in d-dimension vector space, i.e., h,t,r ∈ Rd, and makes embeddings follow the translational principle h+r ≈ t. To tackle this problem of insufﬁciency of a single space for both entities and relations, TransR [17] then further introduces separated spaces for entities and relations. The authors projected entities (h,t ∈ Rk) into relation (r ∈ Rd) space by a projection matrix Mr ∈ Rk×d. NTN [18] models entities across multiple dimensions by a bilinear tensor neural layer. The relational interaction between head and tail hTMt is captured as a tensor denoted as M ∈ Rd×d×k. Instead of using the Cartesian coordinate system, HAKE [19] captures semantic hierarchies by mapping entities into the polar coordinate system, i.e., entity embeddings em ∈ Rd and ep ∈ [0,2π)d in the modulus and phase part, respectively.

Many other translational models such as TransH [20] also use similar representation space, while semantic matching models use plain vector space (e.g., HolE [21]) and relational projection matrix (e.g., ANALOGY [22]). Principles of these translational and semantic matching models are introduced in Section III-B1 and III-B2, respectively.

2) Complex Vector Space: Instead of using a real-valued space, entities and relations are represented in a complex space, where h,t,r ∈ Cd. Take head entity as an example, h has a real part Re(h) and an imaginary part Im(h), i.e., h = Re(h)+iIm(h). ComplEx [23] ﬁrstly introduces complex vector space shown in Fig. 3b which can capture both symmetric and antisymmetric relations. Hermitian dot product is used to do composition for relation, head and the conjugate of tail. Inspired by Euler’s identity eiθ = cosθ + isinθ, RotatE [24] proposes a rotational model taking relation as a rotation from head entity to tail entity in complex space as t = h◦r where ◦ denotes the element-wise Hadmard product. QuatE [25] extends the complex-valued space into hypercomplex h,t,r ∈ Hd by a quaternion Q = a + bi + cj + dk with three imaginary components, where the quaternion inner product, i.e., the Hamilton product h ⊗ r, is used as compositional operator for head entity and relation. With the introduction of the rotational Hadmard product in complex space, RotatE [24] can also capture inversion and composition patterns as well as symmetry and antisymmetry. QuatE [25] uses Hamilton product to capture latent inter-dependencies within the four-dimensional space of entities and relations and gains a more expressive rotational capability than RotatE.

- 3) Gaussian Distribution: Inspired by Gaussian word embedding, the density-based embedding model KG2E [26] introduces Gaussian distribution to deal with the (un)certainties of entities and relations. The authors embedded entities and relations into multi-dimensional Gaussian distribution H ∼ N (µh,Σh) and T ∼ N (µt,Σt). The mean vector u indicates entities and relations’ position, and the covariance matrix Σ models their (un)certainties. Following the translational principle, the probability distribution of entity transformation H − T is denoted as Pe ∼ N (µh − µt,Σh + Σt). Similarly, TransG [27] represents entities with Gaussian distributions, while it draws a mixture of Gaussian distribution for relation embedding, where the m-th component translation vector of relation r is denoted as ur,m = t − h ∼ N ut − uh, σh2 + σt2 E .
- 4) Manifold and Group: This section reviews knowledge representation in manifold space, Lie group, and dihedral group. A manifold is a topological space, which could be deﬁned as a set of points with neighborhoods by the set theory. The group is algebraic structures deﬁned in abstract algebra. Previous point-wise modeling is an ill-posed algebraic system where the number of scoring equations is far more than the number of entities and relations. Moreover, embeddings are restricted in an overstrict geometric form even in some methods with subspace projection. To tackle these issues, ManifoldE [28] extends point-wise embedding into manifold-based embedding. The authors introduced two settings of manifold-based embedding, i.e., Sphere and Hyperplane. An example of a sphere is shown in Fig. 3d. For the sphere setting, Reproducing Kernel Hilbert Space is used to represent the manifold function. Another “hyperplane” setting is introduced to enhance the model with intersected embeddings. ManifoldE [28] relaxes the real-valued point-wise space into manifold space with a more expressive representation from the geometric perspective. When the manifold function and relation-speciﬁc manifold parameter are set to zero, the manifold collapses into a point.


Hyperbolic space, a multidimensional Riemannian manifold with a constant negative curvature −c (c > 0) : Bd,c =

x ∈ Rd : x 2 < 1c , is drawing attention for its capacity of capturing hierarchical information. MuRP [29] represents the multi-relational knowledge graph in Poincar´e ball of hyperbolic space Bdc = x ∈ Rd : c x 2 < 1 . While it fails to capture logical patterns and suffers from constant curvature. Chami et al. [30] leverages expressive hyperbolic isometries and learns a relation-speciﬁc absolute curvature cr in the hyperbolic space.

TorusE [15] solves the regularization problem of TransE via embedding in an n-dimensional torus space which is a compact Lie group. With the projection from vector space into torus space deﬁned as π : Rn → Tn,x  → [x], entities and relations are denoted as [h],[r],[t] ∈ Tn. Similar to TransE, it also learns embeddings following the relational translation in torus space, i.e., [h] + [r] ≈ [t]. Recently, DihEdral [31] proposes a dihedral symmetry group preserving a 2-dimensional polygon. It utilizes a ﬁnite non-Abelian group to preserve the relational properties of symmetry/skew-symmetry, inversion, and composition effectively with the rotation and reﬂection properties in the dihedral group.

###### r 2 Rd

| | | | | |
|---|---|---|---|---|


| | | | | |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |
| | | | | |


###### Mr 2 Rd⇥d

Mcr 2 Rd⇥d⇥k

(a) Point-wise space.

d

Im(u)

| |u = a + b<br><br>b 2 R<br><br>a 2 R<br><br>u 2 C|
|---|---|
| |Re(u|


d

d

i

)

(b) Complex vector space.

P(x1) P(x2)

0.4

P

0.2

0

2

−2

1.5

−1.5

P(x1,x2)

1

−1

0.5

−0.5

0.3

0

0

0.2

0.5

−0.5

x1 x2

1

−1

0.1

1.5

−1.5

2−2

0

(c) Gaussian distribution.

Fig. 3: An illustration of knowledge representation in different spaces.

(Clock, HasPart, *) 0

0

Clock Dial

0

(Face, HasInstance, *)

(d) Manifold space.

- B. Scoring Function


The scoring function is used to measure the plausibility of facts, also referred to as the energy function in the energybased learning framework. Energy-based learning aims to learn the energy function Eθ(x) (parameterized by θ taking x as input) and to make sure positive samples have higher scores than negative samples. In this paper, the term of the scoring function is adopted for uniﬁcation. There are two typical types of scoring functions, i.e., distance-based (Fig. 4a) and similaritybased (Fig. 4b) functions, to measure the plausibility of a fact. Distance-based scoring function measures the plausibility of facts by calculating the distance between entities, where addictive translation with relations as h+r ≈ t is widely used. Semantic similarity based scoring measures the plausibility of facts by semantic matching. It usually adopts a multiplicative formulation, i.e., h Mr ≈ t , to transform head entity near the tail in the representation space.

r distance

h

t

(a) Translational distancebased scoring of TransE.

#### fr(h,r)

| | | | |
|---|---|---|---|
| | | | |


r

| | | |
|---|---|---|


| | | |
|---|---|---|


h t

(b) Semantic similarity-based scoring of DistMult.

- Fig. 4: Illustrations of distance-based and similarity matching based scoring functions taking TransE [16] and DistMult [32] as examples.


of h+r should be close to the embedding of t with the scoring function is deﬁned under L1 or L2 constraints as

fr(h, t) = h + r − t L1/L2. (2)

Since that, many variants and extensions of TransE have been proposed. For example, TransH [20] projects entities and relations into a hyperplane, TransR [17] introduces separate projection spaces for entities and relations, and TransD [33] constructs dynamic mapping matrices Mrh = rphp + I and Mrt = rptp +I by the projection vectors hp,tp,rp ∈ Rn. By replacing Euclidean distance, TransA [34] uses Mahalanobis distance to enable more adaptive metric learning. Previous methods used additive score functions, TransF [35] relaxes the strict translation and uses dot product as fr(h,t) = (h + r) t. To balance the constraints on head and tail, a ﬂexible translation scoring function is further proposed.

Recently, ITransF [36] enables hidden concepts discovery and statistical strength transferring by learning associations between relations and concepts via sparse attention vectors, with scoring function deﬁned as

fr(h, t) = αHr · D · h + r − αTr · D · t , (3)

where D ∈ Rn×d×d is stacked concept projection matrices of entities and relations and αHr ,αTr ∈ [0,1]n are attention vectors calculated by sparse softmax, TransAt [37] integrates relation attention mechanism with translational embedding, and TransMS [38] transmits multi-directional semantics with nonlinear functions and linear bias vectors, with the scoring function as

1) Distance-based Scoring Function: An intuitive distancebased approach is to calculate the Euclidean distance between the relational projection of entities. Structural Embedding (SE) [8] uses two projection matrices and L1 distance to learn structural embedding as

fr(h, t) = Mr,1h − Mr,2t L1. (1)

A more intensively used principle is the translation-based scoring function that aims to learn embeddings by representing relations as translations from head to tail entities. Bordes et al. [16] proposed TransE by assuming that the added embedding

fr(h, t) =  −tanh(t◦r)◦h+r−tanh(h◦r)◦t+α·(h◦t) 1/2. (4)

KG2E [26] in Gaussian space and ManifoldE [28] with manifold also use the translational distance-based scoring function. KG2E uses two scoring methods, i.e, asymmetric KL-divergence and symmetric expected likelihood. While the scoring function of ManifoldE is deﬁned as

fr(h, t) = M(h, r, t) − Dr2 2 , (5)

where M is the manifold function, and Dr is a relation-speciﬁc manifold parameter.

2) Semantic Matching: Another direction is to calculate the semantic similarity. SME [39] proposes to semantically match separate combinations of entity-relation pairs of (h,r) and (r,t). Its scoring function is deﬁned with two versions of matching blocks - linear and bilinear block, i.e.,

fr(h, t) = gleft(h, r) gright(r, t). (6)

The linear matching block is deﬁned as gleft(h,t) = Ml,1h + Ml,2r +bl , and the bilinear form is gleft(h,r) = (Ml,1h)◦ (Ml,2r)+bl . By restricting relation matrix Mr to be diagonal for multi-relational representation learning, DistMult [32] proposes a simpliﬁed bilinear formulation deﬁned as

fr(h, t) = h diag(Mr)t. (7)

To capture productive interactions in relational data and compute efﬁciently, HolE [21] introduces a circular correlation of embedding, which can be interpreted as a compressed tensor product, to learn compositional representations. By deﬁning a perturbed holographic compositional operator as p(a,b;c) = (c◦a) b, where c is a ﬁxed vector, the expanded holographic embedding model HolEx [40] interpolates the HolE and full tensor product method. It can be viewed as linear concatenation of perturbed HolE. Focusing on multi-relational inference, ANALOGY [22] models analogical structures of relational data. It’s scoring function is deﬁned as

fr(h, t) = h Mrt, (8)

with relation matrix constrained to be normal matrices in linear mapping, i.e., Mr Mr = MrMr for analogical inference. HolE with Fourier transformed in the frequency domain can be viewed as a special case of ComplEx [41], which connects holographic and complex embeddings. The analogical embedding framework [22] can recover or equivalently obtain several models such as DistMult, ComplEx and HolE by restricting the embedding dimension and scoring function. Crossover interactions are introduced by CrossE [42] with an interaction matrix C ∈ Rn

r×d to simulate the bi-directional interaction between entity and relation. The relation speciﬁc interaction is obtained by looking up interaction matrix as cr = xr C. By combining the interactive representations and matching with tail embedding, the scoring function is deﬁned as

f(h, r, t) = σ tanh (cr ◦ h + cr ◦ h ◦ r + b) t . (9)

The semantic matching principle can be encoded by neural networks further discussed in Sec. III-C.

The two methods mentioned above in Sec. III-A4 with group representation also follow the semantic matching principle. The scoring function of TorusE [15] is deﬁned as:

x − y i. (10)

min

(x,y)∈([h]+[r])×[t]

By modeling 2L relations as group elements, the scoring function of DihEdral [31] is deﬁned as the summation of components:

fr(h, t) = h Rt =

L

h(l) R(l)t(l), (11)

l=1

where the relation matrix R is deﬁned in block diagonal form for R(l) ∈ DK, and entities are embedded in real-valued space for h(l) and t(l) ∈ R2.

C. Encoding Models

This section introduces models that encode the interactions of entities and relations through speciﬁc model architectures, including linear/bilinear models, factorization models, and neural networks. Linear models formulate relations as a linear/bilinear mapping by projecting head entities into a representation space close to tail entities. Factorization aims to decompose relational data into low-rank matrices for representation learning. Neural networks encode relational data with non-linear neural activation and more complex network structures by matching semantic similarity of entities and relations. Several neural models are illustrated in Fig. 5.

1) Linear/Bilinear Models: Linear/bilinear models encode interactions of entities and relations by applying linear operation as:

h t

gr (h, t) = MTr

, (12)

or bilinear transformation operations as Eq. 8. Canonical methods with linear/bilinear encoding include SE [8], SME [39], DistMult [32], ComplEx [23], and ANALOGY [22]. For TransE [16] with L2 regularization, the scoring function can be expanded to the form with only linear transformation with one-dimensional vectors, i.e.,

h + r − t 22 = 2rT (h − t)−2hTt+ r 22 + h 22 + t 22 . (13)

Wang et al. [47] studied various bilinear models and evaluated their expressiveness and connections by introducing the concepts of universality and consistency. The authors further showed that the ensembles of multiple linear models can improve the prediction performance through experiments. Recently, to solve the independence embedding issue of entity vectors in canonical Polyadia decomposition, SimplE [48] introduces the inverse of relations and calculates the average canonical Polyadia score of (h,r,t) and (t,r−1,h) as

- 1

- 2


h ◦ rt + t ◦ r t , (14)

fr(h, t) =

where r is the embedding of inversion relation. Embedding models in the bilinear family such as RESCAL, DistMult, HolE and ComplEx can be transformed from one into another with certain constraints [47]. More bilinear models are proposed from a factorization perspective discussed in the next section.

2) Factorization Models: Factorization methods formulated KRL models as three-way tensor X decomposition. A general principle of tensor factorization can be denoted as Xhrt ≈ h Mrt, with the composition function following the semantic matching pattern. Nickel et al. [49] proposed the three-way rank-r factorization RESCAL over each relational slice of knowledge graph tensor. For k-th relation of m relations, the k-th slice of X is factorized as

Xk ≈ ARkAT. (15)

The authors further extended it to handle attributes of entities efﬁciently [50]. Jenatton et al. [51] then proposed a bilinear

|*<br><br>t r h<br><br>Filters|
|---|


###### *

Convolution

Features maps

Score

(a) CNN.

GCN

| | | | |
|---|---|---|---|
| | | | |


| | | | |
|---|---|---|---|
| | | | |


| | | | |
|---|---|---|---|
| | | | |


| | | | |
|---|---|---|---|
| | | | |


| | | | |
|---|---|---|---|
| | | | |


Entity/Relation Embedding

KG

Activation

combine combine

RNN unit

···

e1 r1 e2 r2 e3

(b) GCN.

(c) RSN.

head

Transformer Encoders TrmTrmTrm

TrmTrmTrm

|h01| |
|---|---|
| | |


|hL1|
|---|


|xpos1|
|---|


|xele1|
|---|


+

relation

|hL2|
|---|


|h02|
|---|


|xele2|
|---|


|xpos2|
|---|


+

[MASK]

|hL3|
|---|


|h03|
|---|


Cls

|xpos3|
|---|


|xele3|
|---|


+

Position Embeddings

Element Embeddings

Input Embeddings

Transformer Encoders

(d) Transformer.

- Fig. 5: Illustrations of neural encoding models. (a) CNN [43] input triples into dense layer and convolution operation to learn semantic representation, (b) GCN [44] acts as encoder of knowledge graphs to produce entity and relation embeddings. (c) RSN [45] encodes entity-relation sequences and skips relations discriminatively. (d) Transformer-based CoKE [46] encodes triples as sequences with an entity replaced by [MASK].


structured latent factor model (LFM), which extends RESCAL by decomposing Rk = di=1 αki uivi . By introducing threeway Tucker tensor decomposition, TuckER [52] learns to embed by outputting a core tensor and embedding vectors of entities and relations. LowFER [53] proposes a multimodal factorized bilinear pooling mechanism to better fuse entities and relations. It generalizes the TuckER model and is computationally efﬁcient with low-rank approximation.

3) Neural Networks: Neural networks for encoding semantic matching have yielded remarkable predictive performance in recent studies. Encoding models with linear/bilinear blocks can also be modeled using neural networks, for example, SME [39]. Representative neural models include multi-layer perceptron (MLP) [3], neural tensor network (NTN) [18], and neural association model (NAM) [54]. They generally feed entities or relations or both into deep neural networks and compute a semantic matching score. MLP [3] encodes entities and relations together into a fully-connected layer, and uses a second layer with sigmoid activation for scoring a triple as

fr(h, t) = σ(w σ(W[h, r, t])), (16)

where W ∈ Rn×3d is the weight matrix and [h,r,t] is a concatenation of three vectors. NTN [18] takes entity embeddings as input associated with a relational tensor and outputs predictive score in as

fr(h, t) = r σ(hTMt + Mr,1h + Mr,2t + br), (17)

where br ∈ Rk is bias for relation r, Mr,1 and Mr,2 are relation-speciﬁc weight matrices. It can be regarded as a combination of MLPs and bilinear models. NAM [54] associates the hidden encoding with the embedding of tail entity, and proposes the relational-modulated neural network (RMNN).

4) Convolutional Neural Networks: CNNs are utilized for learning deep expressive features. ConvE [55] uses 2D convolution over embeddings and multiple layers of nonlinear features to model the interactions between entities and relations by reshaping head entity and relation into 2D matrix, i.e., Mh ∈ Rd

w×dh for d = dw × dh. Its scoring function is deﬁned as

w×dh and Mr ∈ Rd

fr (h, t) = σ (vec (σ ([Mh; Mr] ∗ ω)) W) t, (18)

where ω is the convolutional ﬁlters and vec is the vectorization operation reshaping a tensor into a vector. ConvE can express

semantic information by non-linear feature learning through multiple layers. ConvKB [43] adopts CNNs for encoding the concatenation of entities and relations without reshaping (Fig. 5a). Its scoring function is deﬁned as

fr(h, t) = concat (σ ([h, r, t] ∗ ω)) · w. (19)

The concatenation of a set for feature maps generated by convolution increases the learning ability of latent features. Compared with ConvE, which captures the local relationships, ConvKB keeps the transitional characteristic and shows better experimental performance. HypER [56] utilizes hypernetwork H for 1D relation-speciﬁc convolutional ﬁlter generation to achieve multi-task knowledge sharing, and meanwhile simpliﬁes 2D ConvE. It can also be interpreted as a tensor factorization model when taking hypernetwork and weight matrix as tensors.

5) Recurrent Neural Networks: The MLP- and CNN-based models, as mentioned above, learn triplet-level representations. In comparison, the recurrent networks can capture long-term relational dependencies in knowledge graphs. Gardner et al. [57] and Neelakantan et al. [58] propose RNN-based model over the relation path to learn vector representation without and with entity information, respectively. RSN [45] (Fig. 5c) designs a recurrent skip mechanism to enhance semantic representation learning by distinguishing relations and entities. The relational path as (x1,x2,...,xT) with entities and relations in an alternating order is generated by random walk, and it is further used to calculate recurrent hidden state ht = tanh(Whht−1 + Wxxt + b). The skipping operation is conducted as

ht xt ∈ E S1ht + S2xt−1 xt ∈ R

, (20)

ht =

where S1 and S2 are weight matrices.

6) Transformers: Transformer-based models have boosted contextualized text representation learning. To utilize contextual information in knowledge graphs, CoKE [46] employs transformers to encode edges and path sequences. Similarly, KG-BERT [59] borrows the idea form language model pretraining and takes Bidirectional Encoder Representations from Transformer (BERT) model as an encoder for entities and relations.

7) Graph Neural Networks (GNNs): GNNs are introduced for learning connectivity structure under an encoder-decoder framework. R-GCN [60] proposes relation-speciﬁc transformation to model the directed nature of knowledge graphs. Its forward propagation is deﬁned as

 

  , (21)

1 ci,r

x(il+1) = σ

Wr(l)x(jl) + W0(l)x(il)

r∈R j∈Nir

where x(il) ∈ Rd

(l)

is the hidden state of the i-th entity in l-th layer, Nir is a neighbor set of i-th entity within relation r ∈ R, Wr(l) and W0(l) are the learnable parameter matrices, and ci,r is normalization such as ci,r = |Nir|. Here, the GCN [61] acts as a graph encoder. To enable speciﬁc tasks, an encoder model still needs to be developed and integrated into the RGCN framework. R-GCN takes the neighborhood of each entity equally. SACN [44] introduces weighted GCN (Fig. 5b), which deﬁnes the strength of two adjacent nodes with the same relation type, to capture the structural information in knowledge graphs by utilizing node structure, node attributes, and relation types. The decoder module called Conv-TransE adopts ConvE model as semantic matching metric and preserves the translational property. By aligning the convolutional outputs of entity and relation embeddings with C kernels to be M(h,r) ∈ RC×d, its scoring function is deﬁned as

fr(h, t) = g (vec (M (h, r)) W) t. (22)

Nathani et al. [62] introduced graph attention networks with multi-head attention as encoder to capture multi-hop neighborhood features by inputing the concatenation of entity and relation embeddings. CompGCN [63] proposes entity-relation composition operations over each edge in the neighborhood of a central node and generalizes previous GCN-based models.

D. Embedding with Auxiliary Information

Multi-modal embedding incorporates external information such as text descriptions, type constraints, relational paths, and visual information, with a knowledge graph itself to facilitate more effective knowledge representation.

1) Textual Description: Entities in knowledge graphs have textual descriptions denoted as D =< w1,w2,...,wn >, providing supplementary semantic information. The challenge of KRL with textual description is to embed both structured knowledge and unstructured textual information in the same space. Wang et al. [64] proposed two alignment models for aligning entity space and word space by introducing entity names and Wikipedia anchors. DKRL [65] extends TransE [16] to learn representation directly from entity descriptions by a convolutional encoder. SSP [66] captures the strong correlations between triples and textual descriptions by projecting them in a semantic subspace. The joint loss function is widely applied when incorporating KGE with textual description. Wang et al. [64] used a three-component loss L = LK + LT + LA of knowledge model LK, text model LT and alignment model LA. SSP [66] uses a two-component objective function L = Lembed +µLtopic of embedding-speciﬁc loss Lembed and topic-speciﬁc loss Ltopic within textual description, traded off by a parameter µ.

- 2) Type Information: Entities are represented with hier-

archical classes or types, and consequently, relations with semantic types. SSE [67] incorporates semantic categories of entities to embed entities belonging to the same category smoothly in semantic space. TKRL [68] proposes type encoder model for projection matrix of entities to capture type hierarchy. Noticing that some relations indicate attributes of entities, KREAR [69] categorizes relation types into attributes and relations and modeled the correlations between entity descriptions. Zhang et al. [70] extended existing embedding methods with hierarchical relation structure of relation clusters, relations, and sub-relations.

- 3) Visual Information: Visual information (e.g., entity


images) can be utilized to enrich KRL. Image-embodied IKRL [71], containing cross-modal structure-based and imagebased representation, encodes images to entity space and follows the translation principle. The cross-modal representations make sure that structure-based and image-based representations are in the same representation space.

There remain many kinds of auxiliary information for KRL, such as attributes, relation paths, and logical rules. Wang et al. [5] gave a detailed review of using additional information. This paper discusses relation path and logical rules under the umbrella of KGC in Sec. IV-A2 and IV-A4, respectively.

4) Uncertain Information: Knowledge graphs such as ProBase [72], NELL [73], and ConceptNet [74] contain uncertain information with a conﬁdence score assigned to every relational fact. In contrast to classic deterministic knowledge graph embedding, uncertain embedding models aim to capture uncertainty representing the likelihood of relational facts. Chen et al. [75] proposed an uncertain knowledge graph embedding model to simultaneously preserve structural and uncertainty information, where probabilistic soft logic is applied to infer the conﬁdence score. Probability calibration takes a post-processing process to adjust probability scores, making predictions probabilistic sense. Tabacof and Costabello [76] ﬁrstly studied probability calibration for knowledge graph embedding under the closed-world assumption, revealing that well-calibrated models can lead to improved accuracy. Safavi et al. [77] further explored probability calibration under the more challenging open-world assumption.

E. Summary

Knowledge representation learning is vital in the research community of knowledge graph. This section reviews four folds of KRL with several modern methods summarized in Table II and more in Appendix C. Overall, developing a novel KRL model is to answer the following four questions: 1) which representation space to choose; 2) how to measure the plausibility of triplets in a speciﬁc space; 3) which encoding model to use for modeling relational interactions; 4) whether to utilize auxiliary information. The most popularly used representation space is Euclidean point-based space by embedding entities in vector space and modeling interactions via vector, matrix, or tensor. Other representation spaces, including complex vector space, Gaussian distribution, and manifold space and group, are also studied. Manifold space has an advantage over pointwise Euclidean space by relaxing the point-wise embedding.

Gaussian embeddings can express the uncertainties of entities and relations, and multiple relation semantics. Embedding in complex vector space can effectively model different relational connectivity patterns, especially the symmetry/antisymmetry pattern. The representation space plays an essential role in encoding the semantic information of entities and capturing the relational properties. When developing a representation learning model, appropriate representation space should be selected and designed carefully to match the nature of encoding methods and balance the expressiveness and computational complexity. The scoring function with a distance-based metric utilizes the translation principle, while the semantic matching scoring function employs compositional operators. Encoding models, especially neural networks, play a critical role in modeling interactions of entities and relations. The bilinear models also have drawn much attention, and some tensor factorization can also be regarded as this family. Other methods incorporate auxiliary information of textual description, relation/entity types, entity images, and conﬁdence scores.

TABLE II: A summary of recent KRL models. See more in Appendix C.

Model Ent. & Rel. embed. Scoring Function fr(h, t) RotatE [24] h, t ∈ Cd , r ∈ Cd h ◦ r − t TorusE [15] [h], [t] ∈ Tn , [r] ∈ Tn min(x,y)∈([h]+[r])×[t] x − y i SimplE [48] h, t ∈ Rd , r, r ∈ Rd 12 h ◦ rt + t ◦ r t TuckER [52] h, t ∈ Rde , r ∈ Rdr W ×1 h ×2 r ×3 t ITransF [36] h, t ∈ Rd , r ∈ Rd αHr · D · h + r − αTr · D · t HolEx [40] h, t ∈ Rd , r ∈ Rd lj=0 p (h, r; cj) · t CrossE [42] h, t ∈ Rd , r ∈ Rd σ σ (cr ◦ h + cr ◦ h ◦ r + b) t QuatE [25] h, t ∈ Hd , r ∈ Hd h ⊗ |rr| · t SACN [44] h, t ∈ Rd , r ∈ Rd g (vec (M (h, r)) W) t ConvKB [43] h, t ∈ Rd , r ∈ Rd concat (g ([h, r, t] ∗ ω)) w ConvE [55]

Mh ∈ Rdw×dh, t ∈ Rd

σ (vec (σ ([Mh; Mr] ∗ ω)) W) t Mr ∈ Rdw×dh

h(l), t(l) ∈ R2 L

DihEdral [31]

l=1 h(l) R(l)t(l) R(l) ∈ DK

hm, tm ∈ Rd, rm ∈ Rd+ −  hm ◦ rm − tm 2− hp, rp, tp ∈ [0, 2π)d λ sin ((hp + rp − tp) /2) 1

HAKE [19]

2

MuRP [29] h, t, r ∈ Bdc, bh, bt ∈ R −dB h(r), t(r)

+ bs + bo AttH [30] h, t, r ∈ Bdc, bh, bt ∈ R −dcBr Q(h, r), eHt

2

+ bh + bt LowFER [53] h, t ∈ Rd, r ∈ Rd Sk diag UT h VT r

T

t

IV. KNOWLEDGE ACQUISITION

Knowledge acquisition aims to construct knowledge graphs from unstructured text and other structured or semi-structured sources, complete an existing knowledge graph, and discover and recognize entities and relations. Well-constructed and largescale knowledge graphs can be useful for many downstream applications and empower knowledge-aware models with commonsense reasoning, thereby paving the way for AI. The main tasks of knowledge acquisition include relation extraction, KGC, and other entity-oriented acquisition tasks such as entity recognition and entity alignment. Most methods formulate KGC and relation extraction separately. These two tasks, however, can also be integrated into a uniﬁed framework. Han et al. [78] proposed a joint learning framework with mutual attention

for data fusion between knowledge graphs and text, which solves KGC and relation extraction from text. There are also other tasks related to knowledge acquisition, such as triple classiﬁcation [79], relation classiﬁcation [80], and open knowledge enrichment [81]. In this section, three categories of knowledge acquisition techniques, namely KGC, entity discovery, and relation extraction are reviewed thoroughly.

A. Knowledge Graph Completion

Because of the nature of incompleteness of knowledge graphs, KGC is developed to add new triples to a knowledge graph. Typical subtasks include link prediction, entity prediction, and relation prediction.

Preliminary research on KGC focused on learning lowdimensional embedding for triple prediction. In this survey, we term those methods as embedding-based methods. Most of them, however, failed to capture multi-step relationships. Thus, recent work turns to explore multi-step relation paths and incorporate logical rules, termed as relation path inference and rule-based reasoning, respectively. Triple classiﬁcation as an associated task of KGC, which evaluates the correctness of a factual triple, is additionally reviewed in this section.

1) Embedding-based Models: Taking entity prediction as an example, embedding-based ranking methods, as shown in Fig. 6a, ﬁrstly learn embedding vectors based on existing triples. By replacing the tail entity or head entity with each entity e ∈ E, those methods calculate scores of all the candidate entities and rank the top k entities. Aforementioned KRL methods (e.g., TransE [16], TransH [20], TransR [17], HolE [21], and RGCN [60]) and joint learning methods like DKRL [65] with textual information can been used for KGC.

Unlike representing inputs and candidates in the uniﬁed embedding space, ProjE [82] proposes a combined embedding by space projection of the known parts of input triples, i.e., (h,r,?) or (?,r,t), and the candidate entities with the candidate-entity matrix Wc ∈ Rs×d, where s is the number of candidate entities. The embedding projection function including a neural combination layer and a output projection layer is deﬁned as h(e,r) = g (Wcσ(e ⊕ r) + bp), where e ⊕ r = Dee + Drr + bc is the combination operator of input entity-relation pair. Previous embedding methods do not differentiate entities and relation prediction, and ProjE does not support relation prediction. Based on these observations, SENN [83] distinguishes three KGC subtasks explicitly by introducing a uniﬁed neural shared embedding with adaptively weighted general loss function to learn different latent features. Existing methods rely heavily on existing connections in knowledge graphs and fail to capture the evolution of factual knowledge or entities with a few connections. ConMask [84] proposes relationship-dependent content masking over the entity description to select relevant snippets of given relations, and CNN-based target fusion to complete the knowledge graph with unseen entities. It can only make a prediction when query relations and entities are explicitly expressed in the text description. Previous methods are discriminative models that rely on preprepared entity pairs or text corpus. Focusing on the medical domain, REMEDY [85] proposes a generative

##### model, called conditional relationship variational autoencoder, for entity pair discovery from latent space.

score

| | | | |
|---|---|---|---|


| | | | |
|---|---|---|---|


candidate

composition

| | | | |
|---|---|---|---|


| | | | |
|---|---|---|---|


queries

(a) Embedding-based Ranking.

r˜

composition

composition

e1 r1 e2 r2 e3 r3 e4

(b) Relation paths [58].

- Fig. 6: Illustrations of embedding-based ranking and relation path reasoning.


- 2) Relation Path Reasoning: Embedding learning of entities and relations has gained remarkable performance in some benchmarks, but it fails to model complex relation paths. Relation path reasoning turns to leverage path information over the graph structure. Random walk inference has been widely investigated; for example, the Path-Ranking Algorithm (PRA) [86] chooses a relational path under a combination of path constraints and conducts maximum-likelihood classiﬁcation. To improve path search, Gardner et al. [57] introduced vector space similarity heuristics in random walk by incorporating textual content, which also relieves the feature sparsity issue in PRA. Neural multi-hop relational path modeling is also studied. Neelakantan et al. [58] developed an RNN model to compose the implications of relational paths by applying compositionality recursively (in Fig. 6b). Chainof-Reasoning [87], a neural attention mechanism to enable multiple reasons, represents logical composition across all relations, entities, and text. Recently, DIVA [88] proposes a uniﬁed variational inference framework that takes multi-hop reasoning as two sub-steps of path-ﬁnding (a prior distribution for underlying path inference) and path-reasoning (a likelihood for link classiﬁcation).
- 3) RL-based Path Finding: Deep reinforcement learning (RL) is introduced for multi-hop reasoning by formulating path-ﬁnding between entity pairs as sequential decision making, speciﬁcally a Markov decision process (MDP). The policybased RL agent learns to ﬁnd a step of relation to extending the reasoning paths via the interaction between the knowledge graph environment, where the policy gradient is utilized for training RL agents.


DeepPath [89] ﬁrstly applies RL into relational path learning and develops a novel reward function to improve accuracy, path diversity, and path efﬁciency. It encodes states in the continuous space via a translational embedding method and takes the relation space as its action space. Similarly, MINERVA [90] takes path walking to the correct answer entity as a sequential optimization problem by maximizing the expected reward. It excludes the target answer entity and provides more capable inference. Instead of using a binary reward function, MultiHop [91] proposes a soft reward mechanism. Action dropout is also adopted to mask some outgoing edges during training to enable more effective path exploration. M-Walk [92] applies an RNN controller to capture the historical trajectory and uses the Monte Carlo Tree Search (MCTS) for effective path generation.

By leveraging text corpus with the sentence bag of current entity denoted as be

, CPL [93] proposes collaborative policy learning for pathﬁnding and fact extraction from text.

t

With source, query and current entity denoted as es, eq and et, and query relation denoted as rq, the MDP environment and policy networks of these methods are summarized in Table III, where MINERVA, M-Walk and CPL use binary reward. For the policy networks, DeepPath uses fully-connected network, the extractor of CPL employs CNN, while the rest uses recurrent networks.

4) Rule-based Reasoning: To better make use of the symbolic nature of knowledge, another research direction of KGC is logical rule learning. A rule is deﬁned by the head and body in the form of head ← body. The head is an atom, i.e., a fact with variable subjects and/or objects, while the body can be a set of atoms. For example, given relations sonOf, hasChild and gender, and entities X and Y , there is a rule in the reverse form of logic programming as:

(Y,sonOf,X) ← (X,hasChild,Y) ∧ (Y,gender,Male)

Logical rules can been extracted by rule mining tools like AMIE [94]. The recent RLvLR [95] proposes a scalable rule mining approach with efﬁcient rule searching and pruning, and uses the extracted rules for link prediction.

More research attention focuses on injecting logical rules into embeddings to improve reasoning, with joint learning or iterative training applied to incorporate ﬁrst-order logic rules. For example, KALE [96] proposes a uniﬁed joint model with t-norm fuzzy logical connectives deﬁned for compatible triples and logical rules embedding. Speciﬁcally, three compositions of logical conjunction, disjunction, and negation are deﬁned to compose the truth value of a complex formula. Fig. 7a illustrates a simple ﬁrst-order Horn clause inference. RUGE [97] proposes an iterative model, where soft rules are utilized for soft label prediction from unlabeled triples and labeled triples for embedding rectiﬁcation. IterE [98] proposes an iterative training strategy with three components of embedding learning, axiom induction, and axiom injection.

The logical rule is one kind of auxiliary information; meanwhile, it can incorporate prior knowledge, enabling the ability of interpretable multi-hop reasoning and paving the way for generalization even in few-shot labeled relational triples. However, logic rules alone can only cover a limited number of relational facts in knowledge graphs and suffer colossal search space. The combination of neural and symbolic computation has complementary advantages that utilize efﬁcient data-driven learning and differentiable optimization and exploit prior logical knowledge for precise and interpretable inference. Incorporating rule-based learning for knowledge representation is principally to add regularizations or constraints to representations. Neural Theorem Provers (NTP) [99] learns logical rules for multi-hop reasoning, which utilizes a radial basis function kernel for differentiable computation on vector space. NeuralLP [100] enables gradient-based optimization to be applicable in the inductive logic programming, where a neural controller system is proposed by integrating attention mechanism and auxiliary memory. Neural-Num-LP [101] extends NeuralLP to learn numerical rules with dynamic programming and cumulative

TABLE III: Comparison of RL-based path ﬁnding for knowledge graph reasoning.

Method State st Action at Reward γ Policy Network

###### Global 1 et = eq or −1 et = eq

DeepPath [89]

(et, eq − et) {r} Efﬁciency length(1 p) Fully-connected network (FCN)

Diversity − |F1| |iF=1| cos (p, pi) MINERVA [90] (et, es, rq, eq) {(et, r, v)} I {et = eq} ht = LSTM (ht−1, [at−1; ot]) Multi-Hop [91] (et, (es, rq)) r , e | et, r , e ∈ G γ + (1 − γ) frq (es, eT ) ht = LSTM (ht−1, at−1)

M-Walk [92] st−1 ∪ at−1, vt, EGvt, Vvt t EGvt ∪ {STOP} I {et = eq} GRU-RNN + FCN CPL [93] Reasoner (es, rq, ht) {ξ ∈ EG} I {et = eq} ht = LSTM (ht−1, [rt, et])

CPL [93] Extractor bet, et r , e (et,r ,e ) ∈ bet step-wise delayed from reasoner PCNN-ATT

sum operations. pLogicNet [102] proposes probabilistic logic neural networks (Fig. 7b) to leverage ﬁrst-order logic and learn effective embedding by combining the advantages of Markov logic networks and KRL methods while handling the uncertainty of logic rules. ExpressGNN [103] generalizes pLogicNet by tuning graph networks and embedding and achieves more efﬁcient logical reasoning.

Truth Vaules

Logic

Logic Connectives

| | |
|---|---|
| | |
| | |
| | |
| | |


| | |
|---|---|
| | |
| | |
| | |
| | |


| |
|---|
| |
| |
| |


| |
|---|
| |
| |
| |


| |
|---|
| |
| |
| |


| |
|---|
| |
| |
| |


Knowledge

+

+

(Paris, CaptialOf, France) (Paris, LocatedIn, France)

(a) KALE [96].

(Alan Turing,

(Alan Turing, LiveIn, UK)

p p

BornIn, London)

Nationality

0.2

LiveIn

(

(Alan Turing, Nationality,UK)

BornIn ^ CityOf ) Nationality

?

1.5

( Nationality PoliticianOf

(Alan Turing, PoliticianOf,

(London, CityOf,UK)

2.6

p

UK)

⇥

|p<br><br>⇥<br><br>? 1.5<br><br>Observed Hidden<br><br>True False<br><br>To predict Weight|
|---|


(b) pLogicNet [102].

Fig. 7: Illustrations of logical rule learning.

5) Meta Relational Learning: The long-tail phenomena exist in the relations of knowledge graphs. Meanwhile, the real-world scenario of knowledge is dynamic, where unseen triples are usually acquired. The new scenario, called as meta relational learning or few-shot relational learning, requires models to predict new relational facts with only a very few samples.

Targeting at the previous two observations, GMatching [104] develops a metric based few-shot learning method with entity embeddings and local graph structures. It encodes one-hop neighbors to capture the structural information with R-GCN and then takes the structural entity embedding for multistep matching guided by long short-term memory (LSTM) networks to calculate the similarity scores. Meta-KGR [105], an optimization-based meta-learning approach, adopts model agnostic meta-learning for fast adaption and reinforcement learning for entity searching and path reasoning. Inspired by modelbased and optimization-based meta-learning, MetaR [106] transfers relation-speciﬁc meta information from support set to query set, and archives fast adaption via loss gradient of highorder relational representation. Zhang et al. [107] proposed joint modules of heterogeneous graph encoder, recurrent autoencoder, and matching network to complete new relational facts with few-shot references. Qin et al. [108] utilized GAN to generate reasonable embeddings for unseen relations under the zeroshot learning setting. Baek et al. [109] proposed a transductive meta-learning framework, called Graph Extrapolation Networks

(GEN), for few-shot out-of-graph link prediction in knowledge graphs.

6) Triple Classiﬁcation: Triple classiﬁcation is to determine whether facts are correct in testing data, which is typically regarded as a binary classiﬁcation problem. The decision rule is based on the scoring function with a speciﬁc threshold. Aforementioned embedding methods could be applied for triple classiﬁcation, including translational distance-based methods like TransH [20] and TransR [17] and semantic matching-based methods such as NTN [18], HolE [21] and ANALOGY [22].

Vanilla vector-based embedding methods failed to deal with 1-to-n relations. Recently, Dong et al. [79] extended the embedding space into region-based n-dimensional balls where the tail region is in the head region for 1-to-n relation using ﬁne-grained type chains, i.e., tree-structure conceptual clusterings. This relaxation of embedding to n-balls turns triple classiﬁcation into a geometric containment problem and improves the performance for entities with long type chains. However, it relies on the type chains of entities and suffers from the scalability problem.

B. Entity Discovery

This section distinguishes entity-based knowledge acquisition into several fractionized tasks, i.e., entity recognition, entity disambiguation, entity typing, and entity alignment. We term them as entity discovery as they all explore entity-related knowledge under different settings.

1) Entity Recognition: Entity recognition or named entity recognition (NER), when it focuses on speciﬁcally named entities, is a task that tags entities in text. Hand-crafted features such as capitalization patterns and language-speciﬁc resources like gazetteers are applied in many pieces of literature. Recent work applies sequence-to-sequence neural architectures, for example, LSTM-CNN [110] for learning character-level and word-level features and encoding partial lexicon matches. Lample et al. [111] proposed stacked neural architectures by stacking LSTM layers and CRF layers, i.e., LSTM-CRF (in Fig. 8a) and Stack-LSTM. MGNER [112] proposes an integrated framework with entity position detection in various granularities and attention-based entity classiﬁcation for both nested and non-overlapping named entities. Hu et al. [113] distinguished multi-token and single-token entities with multitask training. Recently, Li et al. [114] formulated ﬂat and nested NER as a uniﬁed machine reading comprehension framework by referring annotation guidelines to construct query questions.

Pretrained language models with knowledge graphs such as ERNIE [115] and K-BERT [116] have been applied into NER and achieved improved performance.

- 2) Entity Typing: Entity typing includes coarse and ﬁne-

grained types, while the latter uses a tree-structured type category and is typically regarded as multi-class and multilabel classiﬁcation. To reduce label noise, PLE [117] focuses on correct type identiﬁcation and proposes a partial-label embedding model with a heterogeneous graph for the representation of entity mentions, text features, and entity types and their relationships. To tackle the increasing growth of typeset and noisy labels, Ma et al. [118] proposed prototypedriven label embedding with hierarchical information for zeroshot ﬁne-grained named entity typing. Recent studies utilize embedding-based approaches. For example, JOIE [119] learns joint embeddings of instance- and ontology-view graphs and formulates entity typing as top-k ranking to predict associated concepts. ConnectE [120] explores local typing and global triple knowledge to enhance joint embedding learning.

- 3) Entity Disambiguation: Entity disambiguation or entity


linking is a uniﬁed task which links entity mentions to the corresponding entities in a knowledge graph. For example, Einstein won the Noble Prize in Physics in 1921. The entity mention of “Einstein” should be linked to the entity of Albert Einstein. The contemporary end-to-end learning approaches have made efforts through representation learning of entities and mentions, for example, DSRM [121] for modeling entity semantic relatedness and EDKate [122] for the joint embedding of entity and text. Ganea and Hofmann [123] proposed an attentive neural model over local context windows for entity embedding learning and differentiable message passing for inferring ambiguous entities. By regarding relations between entities as latent variables, Le and Titov [124] developed an end-to-end neural architecture with relation-wise and mention-wise normalization.

4) Entity Alignment: The tasks, as mentioned earlier, involve entity discovery from text or a single knowledge graph, while entity alignment (EA) aims to fuse knowledge among various knowledge graphs. Given E1 and E2 as two different entity sets of two different knowledge graphs, EA is to ﬁnd an alignment set A = {(e1,e2) ∈ E1 × E2|e1 ≡ e2}, where entity e1 and entity e2 hold an equivalence relation ≡. In practice, a small set of alignment seeds (i.e., synonymous entities appear in different knowledge graphs) is given to start the alignment process, as shown in the left box of Fig. 8b.

Embedding-based alignment calculates the similarity between the embeddings of a pair of entities. MTransE [125] ﬁrstly studies entity alignment in the multilingual scenario. It considers distance-based axis calibration, translation vectors, and linear transformations for cross-lingual entity matching and triple alignment veriﬁcation. Following the translation-based and linear transformation models, IPTransE [126] proposes an iterative alignment model by mapping entities into a uniﬁed representation space under a joint embedding framework (Fig. 8b) through aligned translation as e1 + r(E

1→E2) − e2 , linear transformation as M(E

1→E2)e1 − e2 , and parameter sharing as e1 ≡ e2. To solve error accumulation in iterative alignment, BootEA [127] proposes a bootstrapping approach

in an incremental training manner, together with an editing technique for checking newly-labeled alignment.

Additional information of entities is also incorporated for reﬁnement, for example, JAPE [128] capturing the correlation between cross-lingual attributes, KDCoE [129] embedding multi-lingual entity descriptions via co-training, MultiKE [130] learning multiple views of the entity name, relation, and attributes, and alignment with character attribute embedding [131]. Entity alignment has been intensively studied in recent years. We recommend Sun et al.’s quantitative survey [132] for detailed reading.

CRF B-PER E-PER S-LOC

- KG1
- KG2


⌘

e1

r2

e3

| | | | | |
|---|---|---|---|---|


| | | | | |
|---|---|---|---|---|


| | | | | |
|---|---|---|---|---|


| | | | | |
|---|---|---|---|---|


- e1
- e2


e1

e2

|L<br><br>S<br>T M<br>|
|---|


|L<br><br>S<br>T M<br>|
|---|


|L<br><br>S<br>T M<br>|
|---|


|L<br><br>S<br>T M<br>|
|---|


'

+

Alignment Seeds

Newly Aligned Entity Pairs

R=1

e3

r2

e1

'

+

| | | | | |
|---|---|---|---|---|


| | | | | |
|---|---|---|---|---|


| | | | | |
|---|---|---|---|---|


| | | | | |
|---|---|---|---|---|


R( , )

e2

e2 r2 e3

W1

W2

W3

W4

(a) Entity recognition with LSTM-CRF [111].

(b) Entity alignment with IPTransE [126].

Fig. 8: Illustrations of several entity discovery tasks.

C. Relation Extraction

Relation extraction is a key task to build large-scale knowledge graphs automatically by extracting unknown relational facts from plain text and adding them into knowledge graphs. Due to the lack of labeled relational data, distant supervision [133], also referred to as weak supervision or self-supervision, uses heuristic matching to create training data by assuming that sentences containing the same entity mentions may express the same relation under the supervision of a relational database. Mintz et al. [134] adopted the distant supervision for relation classiﬁcation with textual features, including lexical and syntactic features, named entity tags, and conjunctive features. Traditional methods rely highly on feature engineering [134], with a recent approach exploring the inner correlation between features [135]. Deep neural networks are changing the representation learning of knowledge graphs and texts. This section reviews recent advances of neural relation extraction (NRE), with an overview illustrated in Fig. 9.

Deep Residual RE

Attentive RE

Other Tasks

+ Attention

+ Transfer learning

+ ResNet

Neural Relation Extraction

Few-Shot RE

Auxiliary Information

+FSL

(Eg. CNNs/ RNNs)

+ GAN

+ RL

+ GCN

Adversarial RE

RL-based RE

KGs

Fig. 9: An overview of neural relation extraction.

1) Neural Relation Extraction: Trendy neural networks are widely applied to NRE. CNNs with position features of relative distances to entities [136] are ﬁrstly explored for relation classiﬁcation, and then extended to relation extraction by multiwindow CNN [137] with multiple sized convolutional ﬁlters. Multi-instance learning takes a bag of sentences as input to predict the relationship of the entity pair. PCNN [138] applies the piecewise max pooling over the segments of convolutional representation divided by entity position. Compared with vanilla CNN [136], PCNN can more efﬁciently capture the structural information within the entity pair. MIMLCNN [139] further extends it to multi-label learning with cross-sentence max pooling for feature selection. Side information such as class ties [140] and relation path [141] is also utilized. RNNs are also introduced, for example, SDP-LSTM [142] adopts multichannel LSTM while utilizing the shortest dependency path between entity pair, and Miwa et al. [143] stacks sequential and tree-structure LSTMs based on dependency tree. BRCNN [144] combines RNN for capturing sequential dependency with CNN for representing local semantics using two-channel bidirectional LSTM and CNN.

- 2) Attention Mechanism: Many variants of attention mecha-

nisms are combined with CNNs, including word-level attention to capture semantic information of words [145] and selective attention over multiple instances to alleviate the impact of noisy instances [146]. Other side information is also introduced for enriching semantic representation. APCNN [147] introduces entity description by PCNN and sentence-level attention, while HATT [148] proposes hierarchical selective attention to capture the relation hierarchy by concatenating attentive representation of each hierarchical layer. Rather than CNN-based sentence encoders, Att-BLSTM [80] proposes word-level attention with BiLSTM. Recently, Soares et al. [149] utilized pretrained relation representations from the deep Transformers model.

- 3) Graph Convolutional Networks (GCNs): GCNs are


utilized for encoding a dependency tree over sentences or learning KGEs to leverage relational knowledge for sentence encoding. C-GCN [150] is a contextualized GCN model over the pruned dependency tree of sentences after path-centric pruning. AGGCN [151] also applies GCN over the dependency tree, but utilizes multi-head attention for edge selection in a soft weighting manner. Unlike previous two GCN-based models, Zhang et al., [152] applied GCN for relation embedding in knowledge graph for sentence-based relation extraction. The authors further proposed a coarse-to-ﬁne knowledge-aware attention mechanism for the selection of informative instance.

- 4) Adversarial Training: Adversarial Training (AT) is ap-

plied to add adversarial noise to word embeddings for CNNand RNN-based relation extraction under the MIML learning setting [153]. DSGAN [154] denoises distantly supervised relation extraction by learning a generator of sentence-level true positive samples and a discriminator that minimizes the probability of being true positive of the generator.

- 5) Reinforcement Learning: RL has been integrated into


neural relation extraction recently by training instance selector with policy networks. Qin et al. [155] proposed to train policybased RL agent of sentential relation classiﬁer to redistribute false positive instances into negative samples to mitigate the

effect of noisy data. The authors took the F1 score as an evaluation metric and used F1 score based performance change as the reward for policy networks. Similarly, Zeng et al. [156] and Feng et al. [157] proposed different reward strategies. The advantage of RL-based NRE is that the relation extractor is model-agnostic. Thus, it could be easily adapted to any neural architectures for effective relation extraction. Recently, HRL [158] proposed a hierarchical policy learning framework of high-level relation detection and low-level entity extraction.

6) Other Advances: Other advances of deep learning are also applied for neural relation extraction. Noticing that current NRE methods do not use very deep networks, Huang and Wang [159] applied deep residual learning to noisy relation extraction and found that 9-layer CNNs have improved performance. Liu et al. [160] proposed to initialize the neural model by transfer learning from entity classiﬁcation. The cooperative CORD [161] ensembles text corpus and knowledge graph with external logical rules by bidirectional knowledge distillation and adaptive imitation. TK-MF [162] enriches sentence representation learning by matching sentences and topic words. Recently, Shahbazi et al. [163] studied trustworthy relation extraction by benchmarking several explanation mechanisms, including saliency, gradient × input, and leave one out.

The existence of low-frequency relations in knowledge graphs requires few-shot relation classiﬁcation with unseen classes or only a few instances. Gao et al. [164] proposed hybrid attention-based prototypical networks to compute prototypical relation embedding and compare its distance between the query embedding. Qin et al. [165] explored the relationships between relations with a global relation graph and formulated few-shot relation extraction as a Bayesian meta-learning problem to learn the posterior distribution of relations’ prototype vectors.

7) Joint Entity and Relation Extraction: Traditional relation extraction models utilize pipeline approaches by ﬁrst extracting entity mentions and then classifying relations. However, pipeline methods may cause error accumulation. Several studies show better performance by joint learning [143], [166] than by conventional pipeline methods. Katiyar and Cardie [167] proposed a joint extraction framework with an attentionbased LSTM network. Some convert joint extraction into different problems such as sequence labeling via a novel tagging scheme [168] and multi-turn question answering [169]. Challenges remain in dealing with entity pair and relation overlapping [170]. Wei et al. [171] proposed a cascade binary tagging framework that models relations as subject-object mapping functions to solve the overlapping problem.

There is a distribution discrepancy between training and inference in the joint learning framework, leading to exposure bias. Recently, Wang et al. [172] proposed a one-stage joint extraction framework by transforming joint entity and relation extraction into a token pair linking task to mitigate error propagation and exposure bias. In contrast to the common view that joint models can ease error accumulation by capturing mutual interaction of entities and relations, Zhong and Chen [173] proposed a simple pipeline-based yet effective approach to learning two independent encoders for entities and relations, revealing that strong contextual representation can preserve distinct features of entities and relations. Future research needs

to rethink the relation between the pipeline and joint learning methods.

D. Summary

This section reviews knowledge completion for incomplete knowledge graph and acquisition from plain text.

Knowledge graph completion completes missing links between existing entities or infers entities given entity and relation queries. Embedding-based KGC methods generally rely on triple representation learning to capture semantics and do candidate ranking for completion. Embedding-based reasoning remains in individual relation level, and is poor at complex reasoning because it ignores the symbolical nature of knowledge graph, and lack of interpretability. Hybrid methods with symbolics and embedding incorporate rulebased reasoning, overcome the sparsity of knowledge graph to improve the quality of embedding, facilitate efﬁcient rule injection, and induce interpretable rules. With the observation of the graphical nature of knowledge graphs, path search and neural path representation learning are studied. However, they suffer from connectivity deﬁciency when traverses over largescale graphs. The emerging direction of meta relational learning aims to learn fast adaptation over unseen relations in lowresource settings.

Entity discovery acquires entity-oriented knowledge from text and fuses knowledge between knowledge graphs. There are several categories according to speciﬁc settings. Entity recognition is explored in a sequence-to-sequence manner, entity typing discusses noisy type labels and zero-shot typing, and entity disambiguation and alignment learn uniﬁed embeddings with iterative alignment model proposed to tackle the issue of a limited number of alignment seeds. However, it may face error accumulation problems if newly-aligned entities suffer from poor performance. Language-speciﬁc knowledge has increased in recent years and consequentially motivates the research on cross-lingual knowledge alignment.

Relation extraction suffers from noisy patterns under the assumption of distant supervision, especially in text corpus of different domains. Thus, weakly supervised relation extraction must mitigate the impact of noisy labeling. For example, multi-instance learning takes bags of sentences as inputs and attention mechanism [146] reduce noisy patterns by soft selection over instances, and RL-based methods formulate instance selection as a hard decision. Another principle is to learn richer representation as possible. As deep neural networks can solve error propagation in traditional feature extraction methods, this ﬁeld is dominated by DNN-based models, as summarized in Table IV.

V. TEMPORAL KNOWLEDGE GRAPH

Current knowledge graph research mostly focuses on static knowledge graphs where facts are not changed with time, while the temporal dynamics of a knowledge graph is less explored. However, the temporal information is of great importance because the structured knowledge only holds within a speciﬁc period, and the evolution of facts follows a time sequence. Recent research begins to take temporal information into KRL

and KGC, which is termed as temporal knowledge graph in contrast to the previous static knowledge graph. Research efforts have been made for learning temporal and relational embedding simultaneously. Relevant models for dynamic network embedding also inspire temporal knowledge graph embedding. For example, the temporal graph attention (TGAT) network [174] that captures temporal-topological structure and learn time-feature interactions simultaneously may be useful to preserve temporal-aware relation for knowledge graphs.

- A. Temporal Information Embedding

Temporal information is considered in temporal-aware embedding by extending triples into temporal quadruple as (h,r,t,τ), where τ provides additional temporal information about when the fact held. Leblay and Chekol [175] investigated temporal scope prediction over time-annotated triple, and simply extended existing embedding methods, for example, TransE with the vector-based TTransE deﬁned as

fτ(h, r, t) = − h + r + τ − t L1/2. (23)

Ma et al. [176] also generalized existing static embedding methods and proposed ConT by replacing the shared weight vector of Tucker with a timestamp embedding. Temporally scoped quadruple extends triples by adding a time scope [τs,τe], where τs and τe stand for the beginning and ending of the valid period of a triple, and then a static subgraph Gτ can be derived from the dynamic knowledge graph when given a speciﬁc timestamp τ. HyTE [177] takes a time stamp as a hyperplane wτ and projects entity and relation representation as Pτ (h) = h − wτ h wτ, Pτ (t) = t − wτ t wτ, and Pτ (r) = r − wτ r wτ. The temporally projected scoring function is calculated as

fτ(h, r, t) = Pτ (h) + Pτ (r) − Pτ (t) L

1/L2 (24)

within the projected translation of Pτ (h) + Pτ (r) ≈ Pτ (t). Garc´ıa-Dur´an et al. [178] concatenated predicate token sequence and temporal token sequence, and used LSTM to encode the concatenated time-aware predicate sequences. The last hidden state of LSTM is taken as temporal-aware relational embedding rtemp. The scoring function of extended TransE and DistMult are calculated as h + rtemp − t 2 and (h ◦ t)rTtemp, respectively. By deﬁning the context of an entity e as an aggregate set of facts containing e, Liu et al. [179] proposed context selection to capture useful contexts, and measured temporal consistency with selected context. By formulating temporal KGC as 4-order tensor completion, Lacroix et al. [180] proposed TComplEx, which extends ComplEx decomposition, and introduced weighted regularizers.

- B. Entity Dynamics


Real-world events change entities’ state, and consequently, affect the corresponding relations. To improve temporal scope inference, the contextual temporal proﬁle model [181] formulates the temporal scoping problem as state change detection and utilizes the context to learn state and state change vectors. Inspired by the diachronic word embedding, Goel et al. [182]

TABLE IV: A summary of neural relation extraction and recent advances.

Category Method Mechanism Auxiliary Information

O-CNN [136] CNN + max pooling position embedding Multi CNN [137] Multi-window convolution + max pooling position embedding PCNN [138] CNN + piecewise max pooling position embedding MIMLCNN [139] CNN + piecewise and cross-sentence max pooling position embedding Ye et al. [140] CNN/PCNN + pairwise ranking position embedding, class ties Zeng et al. [141] CNN + max pooling position embedding, relation path

CNNs

SDP-LSTM [142] Multichannel LSTM + dropout dependency tree, POS, GR, hypernyms LSTM-RNN [143] Bi-LSTM + Bi-TreeLSTM POS, dependency tree BRCNN [144] Two-channel LSTM + CNN + max pooling dependency tree, POS, NER

RNNs

Attention-CNN [145] CNN + word-level attention + max pooling POS, position embedding Lin et al. [146] CNN/PCNN + selective attention + max pooling position embedding Att-BLSTM [80] Bi-LSTM + word-level attention position indicator APCNN [147] PCNN + sentence-level attention entity descriptions HATT [148] CNN/PCNN + hierarchical attention position embedding, relation hierarchy

Attention

C-GCN [150] LSTM + GCN + path-centric pruning dependency tree KATT [152] Pre-training + GCN + CNN + attention position embedding, relation hierarchy AGGCN [151] GCN + multi-head attention + dense layers dependency tree

GCNs

Wu et al. [153] AT + PCNN/RNN + selective attention indicator encoding DSGAN [154] GAN + PCNN/CNN + attention position embedding

Adversarial

Qin et al. [155] Policy gradient + CNN + performance change reward position embedding Zeng et al. [156] Policy gradient + CNN + +1/-1 bag-result reward position embedding Feng et al. [157] Policy gradient + CNN + predictive probability reward position embedding HRL [158] Hierarchical policy learning + Bi-LSTM + MLP relation indicator

RL

took an entity and timestamp as the input of entity embedding function to preserve the temporal-aware characteristics of entities at any time point. Know-evolve [183], a deep evolutionary knowledge network, investigates the knowledge evolution phenomenon of entities and their evolved relations.

- A multivariate temporal point process is used to model the occurrence of facts, and a novel recurrent network is developed to learn the representation of non-linear temporal evolution. To capture the interaction between nodes, RE-NET [184] models event sequences via RNN-based event encoder, and neighborhood aggregator. Speciﬁcally, RNN is used to capture the temporal entity interaction, and the neighborhood aggregator aggregates the concurrent interactions.


- C. Temporal Relational Dependency

There exists temporal dependencies in relational chains following the timeline, for example, wasBornIn → graduateFrom → workAt → diedIn. Jiang et al. [185], [186] proposed time-aware embedding, a joint learning framework with temporal regularization, to incorporate temporal order and consistency information. The authors deﬁned a temporal scoring function as

f ( rk, rl ) = rkT − rl L

1/2

, (25)

where T ∈ Rd×d is an asymmetric matrix that encodes the temporal order of relation, for a temporal ordering relation pair

rk,rl . Three temporal consistency constraints of disjointness, ordering, and spans are further applied by integer linear programming formulation.

- D. Temporal Logical Reasoning


Logical rules are also studied for temporal reasoning. Chekol et al. [187] explored Markov logic network and probabilistic soft logic for reasoning over uncertain temporal knowledge graphs. RLvLR-Stream [95] considers temporal close-path rules and learns the structure of rules from the knowledge graph stream for reasoning.

VI. KNOWLEDGE-AWARE APPLICATIONS

Rich structured knowledge can be useful for AI applications. However, how to integrate such symbolic knowledge into the computational framework of real-world applications remains a challenge. The application of knowledge graphs includes two folds: 1) in-KG applications such as link prediction and named entity recognition; and 2) out-of-KG applications, including relation extraction and more downstream knowledge-aware applications such as question answering and recommendation systems. This section introduces several recent DNN-based knowledge-driven approaches with the applications on natural language processing and recommendation. More miscellaneous applications such as digital health and search engine are introduced in Appendix E.

A. Language Representation Learning

Language representation learning via self-supervised language model pretraining has become an integral component of many NLP systems. Traditional language modeling does not exploit factual knowledge with entities frequently observed in the text corpus. How to integrate knowledge into language representation has drawn increasing attention. Knowledge graph language model (KGLM) [188] learns to render knowledge by selecting and copying entities. ERNIE-Tsinghua [189] fuses informative entities via aggregated pre-training and random masking. K-BERT [116] infuses domain knowledge into BERT contextual encoder. ERNIE-Baidu [190] introduces named entity masking and phrase masking to integrate knowledge into the language model and is further improved by ERNIE 2.0 [115] via continual multi-task learning. To capture factual knowledge from text, KEPLER [191] combines knowledge embedding and masked language modeling losses via joint optimization. GLM [192] proposes a graph-guided entity masking scheme to utilize knowledge graph implicitly. CoLAKE [193] further exploits the knowledge context of an entity through a uniﬁed word-knowledge graph and a modiﬁed Transformer encoder.

Similar to the K-BERT model and focusing on the medical corpus, BERT-MK [194] integrates medical knowledge into the pretraining language model via knowledge subgraph extraction. Rethinking about large-scale training on language model and querying over knowledge graphs, Petroni et al. [195] analyzed the language model and knowledge base. They found that certain factual knowledge can be acquired via pre-training language model.

- B. Question Answering

Knowledge-graph-based question answering (KG-QA) answers natural language questions with facts from knowledge graphs. Neural network-based approaches represent questions and answers in distributed semantic space, and some also conduct symbolic knowledge injection for commonsense reasoning.

- 1) Single-fact QA: Taking a knowledge graph as an external intellectual source, simple factoid QA or single-fact QA is to answer a simple question involving a single knowledge graph fact. Dai et al. [196] proposed a conditional focused neural network equipped with focused pruning to reduce the search space. BAMnet [197] models the two-way interaction between questions and knowledge graph with a bidirectional attention mechanism. Although deep learning techniques are intensively applied in KG-QA, they inevitably increase the model complexity. Through the evaluation of simple KG-QA with and without neural networks, Mohammed et al. [198] found that sophisticated deep models such as LSTM and GRU with heuristics achieve state of the art, and non-neural models also gain reasonably well performance.
- 2) Multi-hop Reasoning: To deal with complex multi-hop relation requires a more dedicated design to be capable of multihop commonsense reasoning. Structured knowledge provides informative commonsense observations and acts as relational inductive biases, which boosts recent studies on commonsense knowledge fusion between symbolic and semantic space for multi-hop reasoning. Bauer et al. [199] proposed multihop bidirectional attention and pointer-generator decoder for effective multi-hop reasoning and coherent answer generation, utilizing external commonsense knowledge by relational path selection from ConceptNet and injection with selectivelygated attention. Variational Reasoning Network (VRN) [200] conducts multi-hop logic reasoning with reasoning-graph embedding, while handles the uncertainty in topic entity recognition. KagNet [201] performs concept recognition to build a schema graph from ConceptNet and learns path-based relational representation via GCN, LSTM, and hierarchical pathbased attention. CogQA [202] combines implicit extraction and explicit reasoning and proposes a cognitive graph model based on BERT and GNN for multi-hop QA.


- C. Recommender Systems


Integrating knowledge graphs as external information enables recommendation systems to have the ability of commonsense reasoning, with the potential to solve the sparsity issue and the cold start problem. By injecting knowledge-graph-based side information such as entities, relations, and attributes, many efforts work on embedding-based regularization to improve

recommendation. The collaborative CKE [203] jointly trains KGEs, item’s textual information, and visual content via translational KGE model and stacked auto-encoders. Noticing that time-sensitive and topic-sensitive news articles consist of condensed entities and common knowledge, DKN [204] incorporates knowledge graph by a knowledge-aware CNN model with multi-channel word-entity-aligned textual inputs. However, DKN cannot be trained in an end-to-end manner as it needs to learn entity embedding in advance. To enable end-toend training, MKR [205] associates multi-task knowledge graph representation and recommendation by sharing latent features and modeling high-order item-entity interaction. While other works consider the relational path and structure of knowledge graphs, KPRN [206] regards the interaction between users and items as an entity-relation path in the knowledge graph and conducts preference inference over the path with LSTM to capture the sequential dependency. PGPR [207] performs reinforcement policy-guided path reasoning over knowledgegraph-based user-item interaction. KGAT [208] applies graph attention network over the collaborative knowledge graph of entity-relation and user-item graphs to encode high-order connectivities via embedding propagation and attention-based aggregation. Knowledge graph-based recommendation inherently processes interpretability from embedding propagation with multi-hop neighbors in the knowledge graph.

VII. FUTURE DIRECTIONS

Many efforts have been conducted to tackle the challenges of knowledge representation and its related applications. However, there remains several formidable open problems and promising future directions.

- A. Complex Reasoning

Numerical computing for knowledge representation and reasoning requires a continuous vector space to capture the semantic of entities and relations. While embedding-based methods have a limitation on complex logical reasoning, two directions on the relational path and symbolic logic are worthy of being further explored. Some promising methods such as recurrent relational path encoding, GNN-based message passing over knowledge graph, and reinforcement learningbased pathﬁnding and reasoning are up-and-coming for handling complex reasoning. For the combination of logic rules and embeddings, recent works [102], [103] combine Markov logic networks with KGE, aiming to leverage logic rules and handling their uncertainty. Enabling probabilistic inference for capturing the uncertainty and domain knowledge with efﬁciently embedding will be a noteworthy research direction.

- B. Uniﬁed Framework


Several representation learning models on knowledge graphs have been veriﬁed as equivalence, for example, Hayshi and Shimbo [41] proved that HolE and ComplEx are mathematically equivalent for link prediction with a particular constraint. ANALOGY [22] provides a uniﬁed view of several representative models, including DistMult, ComplEx, and

HolE. Wang et al. [47] explored connections among several bilinear models. Chandrahas et al. [209] explored the geometric understanding of additive and multiplicative KRL models. Most works formulated knowledge acquisition KGC and relation extraction separately with different models. Han et al. [78] put them under the same roof and proposed a joint learning framework with mutual attention for information sharing between knowledge graph and text. A uniﬁed understanding of knowledge representation and reasoning is less explored. An investigation towards uniﬁcation in a way similar to the uniﬁed framework of graph networks [210], however, will be worthy of bridging the research gap.

C. Interpretability

Interpretability of knowledge representation and injection is a vital issue for knowledge acquisition and real-world applications. Preliminary efforts have been made for interpretability. ITransF [36] uses sparse vectors for knowledge transferring and interprets with attention visualization. CrossE [42] explores the explanation scheme of knowledge graphs by using embedding-based path searching to generate explanations for link prediction. However, recent neural models have limitations on transparency and interpretability, although they have gained impressive performance. Some methods combine black-box neural models and symbolic reasoning by incorporating logical rules to increase the interoperability. Interpretability can convince people to trust predictions. Thus, further work should go into interpretability and improve the reliability of predicted knowledge.

- D. Scalability

Scalability is crucial in large-scale knowledge graphs. There is a trade-off between computational efﬁciency and model expressiveness, with a limited number of works applied to more than 1 million entities. Several embedding methods use simpliﬁcation to reduce the computation cost, such as simplifying tensor products with circular correlation operation [21]. However, these methods still struggle with scaling to millions of entities and relations.

Probabilistic logic inference using Markov logic networks is computationally intensive, making it hard to scalable to large-scale knowledge graphs. Rules in a recent neural logical model [102] are generated by simple brute-force search, making it insufﬁcient on large-scale knowledge graphs. ExpressGNN [103] attempts to use NeuralLP [100] for efﬁcient rule induction. Nevertheless, there still has a long way to go to deal with cumbersome deep architectures and the increasingly growing knowledge graphs.

- E. Knowledge Aggregation


The aggregation of global knowledge is the core of knowledge-aware applications. For example, recommendation systems use a knowledge graph to model user-item interaction and text classiﬁcation jointly to encode text and knowledge graph into a semantic space. Most current knowledge aggregation methods design neural architectures such as attention

mechanisms and GNNs. The natural language processing community has been boosted from large-scale pre-training via transformers and variants like BERT models. At the same time, a recent ﬁnding [195] reveals that the pre-training language model on the unstructured text can acquire certain factual knowledge. Large-scale pre-training can be a straightforward way to injecting knowledge. However, rethinking the way of knowledge aggregation in an efﬁcient and interpretable manner is also of signiﬁcance.

F. Automatic Construction and Dynamics

Current knowledge graphs rely highly on manual construction, which is labor-intensive and expensive. The widespread applications of knowledge graphs on different cognitive intelligence ﬁelds require automatic knowledge graph construction from large-scale unstructured content. Recent research mainly works on semi-automatic construction under the supervision of existing knowledge graphs. Facing the multimodality, heterogeneity, and large-scale application, automatic construction is still of great challenge.

The mainstream research focuses on static knowledge graphs, with several works on predicting temporal scope validity and learning temporal information and entity dynamics. Many facts only hold within a speciﬁc period. A dynamic knowledge graph, together with learning algorithms capturing dynamics, can address the limitation of traditional knowledge representation and reasoning by considering the temporal nature.

VIII. CONCLUSION

Knowledge graphs as the ensemble of human knowledge have attracted increasing research attention, with the recent emergence of knowledge representation learning, knowledge acquisition methods, and a wide variety of knowledge-aware applications. The paper conducts a comprehensive survey on the following four scopes: 1) knowledge graph embedding, with a full-scale systematic review from embedding space, scoring metrics, encoding models, embedding with external information, and training strategies; 2) knowledge acquisition of entity discovery, relation extraction, and graph completion from three perspectives of embedding learning, relational path inference and logical rule reasoning; 3) temporal knowledge graph representation learning and completion; 4) real-world knowledge-aware applications on natural language understanding, recommendation systems, question answering and other miscellaneous applications. Besides, some useful resources of datasets and open-source libraries, and future research directions are introduced and discussed. Knowledge graph hosts a large research community and has a wide range of methodologies and applications. We conduct this survey to have a summary of current representative research efforts and trends and expect it can facilitate future research.

APPENDIX A A BRIEF HISTORY OF KNOWLEDGE BASES

Figure 10 illustrates a brief history of knolwedge bases.

Fig. 10: A brief history of knowledge bases

|mid 1980s|
|---|
|KL-ONE Frame Language|


|1985|
|---|
|Knowledge Representation Hypothesis|


|2009|
|---|
|OWL 2 Web Ontology Language|


|1983|
|---|
|Knowledge Engineering Environment (KEE)|


|2001|
|---|
|Semantic Web|


|1959|
|---|
|General Problem Solver|


| | | | | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | | |


|1956|
|---|
|Semantic Net|


|1970s|
|---|
|Expert Systems|


|mid 1980s|
|---|
|Frame-based Languages|


|1984|
|---|
|Cyc Project|


|1999|
|---|
|Resource Description Framework (RDF)|


|2004|
|---|
|OWL Web Ontology Language|


|2012|
|---|
|Google’s Knowledge Graph|


APPENDIX B MATHEMATICAL OPERATIONS

Hermitian dot product (Eq. 26) and Hamilton product (Eq. 27) are used in complex vector space (Sec. III-A2). Given h and t represented in complex space Cd, the Hermitian dot product , : Cd × Cd −→ C is calculated as the sesquilinear form of

h, t = hTt, (26)

where h = Re(h) − iIm(h) is the conjugate operation over h ∈ Cd. The quaternion extends complex numbers into fourdimensional hypercomplex space. With two d-dimensional quaternions deﬁned as Q1 = a1 +b1i+c1j+d1k and Q2 = a2+b2i+c2j+d2k, the Hamilton product ⊗ : Hd×Hd → Hd is deﬁned as

Q1 ⊗ Q2 = (a1 ◦ a2 − b1 ◦ b2 − c1 ◦ c2 − d1 ◦ d2)

- + (a1 ◦ b2 + b1 ◦ a2 + c1 ◦ d2 − d1 ◦ c2) i
- + (a1 ◦ c2 − b1 ◦ d2 + c1 ◦ a2 + d1b2) j
- + (a1 ◦ d2 + b1 ◦ c2 − c1 ◦ b2 + d1 ◦ a2) k.


(27)

The Hadmard product (Eq. 28) and circular correlation (Eq. 29) are utilized in semantic matching based methods (Sec. III-B2). Hadmard product, denoted as ◦ or : Rd × Rd → Rd, is also known as element-wise product or Schur product.

(h ◦ t)i = (h t)i = (h)i(t)i (28)

Circular correlation : Rd × Rd → Rd is an efﬁcient computation calculated as:

[a b]k =

d−1

aib(k+i) mod d. (29)

i=0

APPENDIX C A SUMMARY OF KRL MODELS

We conduct a comprehensive summary of KRL models in Table V. The representation space has an impact on the expressiveness of KRL methods to some extent. By expanding point-wise Euclidean space [16], [18], [21], manifold space [28], complex space [23]–[25] and Gaussian distribution [26], [27] are introduced.

Distance-based and semantic matching scoring functions consist of the foundation stones of plausibility measure in KRL. Translational distance-based methods, especially the groundbreaking TransE [16], borrowed the idea of distributed word representation learning and inspired many following approaches, such as TransH [20] and TransR [17] which specify complex relations (1-to-N, N-to-1, and N-to-N) and the

recent TransMS [38] which models multi-directional semantics. As for the semantic matching side, many methods utilizes mathematical operations or compositional operators including linear matching in SME [39], bilinear mapping in DistMult [32], tensor product in NTN [18], circular correlation in HolE [21] and ANALOGY [22], Hadamard product in CrossE [42], and quaternion inner product in QuatE [25].

Recent encoding models for knowledge representation have developed rapidly and generally fall into two families of bilinear and neural networks. Linear and bilinear models use productbased functions over entities and relations, while factorization models regard knowledge graphs as three-way tensors. With the multiplicative operations, RESCAL [49], ComplEx [23], and SimplE [48] also belong to the bilinear models. DistMult [32] can only model symmetric relations, while its extension of ComplEx [23] managed to preserve antisymmetric relations, but involves redundant computations [48]. ComplEx [23], SimplE [48], and TuckER [52] can guarantee full expressiveness under speciﬁc embedding dimensionality bounds. Neural network-based encoding models start from distributed representation of entities and relations, and some utilizes complex neural structures such as tensor networks [18], graph convolution networks [44], [60], [62], recurrent networks [45] and transformers [46], [59] to learn richer representation. These deep models have achieved very competitive results, but they are not transparent, and lack of interpretability. As deep learning techniques are growing prosperity and gaining extensive superiority in many tasks, the recent trend is still likely to focus on more powerful neural architectures or largescale pre-training, while deep interpretable models remains a challenge.

APPENDIX D KRL MODEL TRAINING

Open world assumption (OWA) and closed world assumption (CWA) [214] are considered when training knowledge representation learning models. During training, a negative sample set F is randomly generated by corrupting a golden triple set F under the OWA. Mini-batch optimization and Stochastic Gradient Descent (SGD) are carried out to minimize a certain loss function. Under the OWA, negative samples are generated with speciﬁc sampling strategies designed to reduce the number of false negatives.

TABLE V: A comprehensive summary of knowledge representation learning models

Category Model Ent. embed. Rel. embed. Scoring Function fr(h, t) Polar coordinate

hm, tm ∈ Rk rm ∈ Rk+ −  hm ◦ rm − tm 2 − hp, tp ∈ [0, 2π)k rp, ∈ [0, 2π)k λ sin ((hp + rp − tp) /2) 1

HAKE [19]

ComplEx [23] h, t ∈ Cd r ∈ Cd Re < r, h, t > = Re Kk=1 rkhktk RotatE [24] h, t ∈ Cd r ∈ Cd h ◦ r − t QuatE [25] h, t ∈ Hd r ∈ Hd h ⊗ |rr| · t

Complex vector

ManifoldE [28] h, t ∈ Rd r ∈ Rd M(h, r, t) − Dr2 2 TorusE [15] [h], [t] ∈ Tn [r] ∈ Tn min(x,y)∈([h]+[r])×[t] x − y i DihEdral [31] h(l), t(l) ∈ R2 R(l) ∈ DK Ll=1 h(l) R(l)t(l) MuRP [29] h, t ∈ Bdc, bh, bt ∈ R r ∈ Bdc −dB (expc0 (R logc0 (h)) , t ⊕c r)2 + bh + bt AttH [30] h, t ∈ Bdc, bh, bt ∈ R r ∈ Bdc −dcBr Att qHRot, qHRef; ar ⊕cr rHr , eHt

Manifold & Group

2

+ bh + bt

h ∼ N (µh, Σh)

r ∼ N (µr, Σr) x∈Rke N (x; µr, Σr) log NN((xx;;µµe,Σe)

r,Σr) dx

t ∼ N (µt, Σt) µh, µt ∈ Rd

KG2E [26]

µr ∈ Rd, Σr ∈ Rd×d log x∈Rke N (x; µe, Σe) N (x; µr, Σr) dx Σh, Σt ∈ Rd×d

Gaussian

h ∼ N µh, σ2hI µir ∼ N µt − µh, σh2 + σt2 I

2 2

µh+µi

r−µt

i πri exp −

TransG [27]

t ∼ N (µt, Σt)

r = i πriµir ∈ Rd µh, µt ∈ Rd

σ2 h

+σ2 t

- TransE [16] h, t ∈ Rd r ∈ Rd − h + r − t 1/2 TransR [17] h, t ∈ Rd r ∈ Rk, Mr ∈ Rk×d −  Mrh + r − Mrt 22

TransH [20] h, t ∈ Rd r, wr ∈ Rd − h − wr hwr + r − t − wr twr

2 2

TransA [34] h, t ∈ Rd r ∈ Rd, Mr ∈ Rd×d (|h + r − t|) Wr(|h + r − t|)

- TransF [35] h, t ∈ Rd r ∈ Rd (h + r) t + (t − r) h ITransF [36] h, t ∈ Rd r ∈ Rd αHr · D · h + r − αTr · D · t TransAt [37] h, t ∈ Rd r ∈ Rd Pr (σ (rh) h) + r − Pr (σ (rt) t)


Translational Distance

2 2

TransD [33] h, t, whwt ∈ Rd r, wr ∈ Rk − wrwh + I h + r − wrwt + I t

TransM [211] h, t ∈ Rd r ∈ Rd −θr h + r − t 1/2 TranSparse [212] h, t ∈ Rd

r ∈ Rk, Mr (θr) ∈ Rk×d −  Mr (θr) h + r − Mr (θr) t 21/2 M1r θr1 , M2r θr2 ∈ Rk×d − M1r θr1 h + r − M2r θr2 t 21/2

TATEC [213] h, t ∈ Rd r ∈ Rd, Mr ∈ Rd×d h Mrt + h r + t r + h Dt ANALOGY [22] h, t ∈ Rd Mr ∈ Rd×d h Mrt CrossE [42] h, t ∈ Rd r ∈ Rd σ tanh (cr ◦ h + cr ◦ h ◦ r + b) t SME [39] h, t ∈ Rd r ∈ Rd gleft(h, r) gright(r, t) DistMult [32] h, t ∈ Rd r ∈ Rd h diag(Mr)t HolE [21] h, t ∈ Rd r ∈ Rd r (h   t) HolEx [40] h, t ∈ Rd r ∈ Rd lj=0 p (h, r; cj) · t SE [8] h, t ∈ Rd M1r, M2r ∈ Rd×d − M1rh − M2rt 1 SimplE [48] h, t ∈ Rd r, r ∈ Rd 12 h ◦ rt + t ◦ r t RESCAL [49] h, t ∈ Rd Mr ∈ Rd×d h Mrt LFM [51] h, t ∈ Rd ur, vr ∈ Rp h di=1 αri uivi t TuckER [52] h, t ∈ Rde r ∈ Rdr W ×1 h ×2 r ×3 t LowFER [53] h, t ∈ Rd r ∈ Rd Sk diag UT h VT r

Semantic Matching

T

###### t

MLP [3] h, t ∈ Rd r ∈ Rd σ(w σ(W[h, r, t])) NAM [54] h, t ∈ Rd r ∈ Rd σ z(L) · t + B(L+1)r ConvE [55] Mh ∈ Rdw×dh, t ∈ Rd Mr ∈ Rdw×dh σ (vec (σ ([Mh; Mr] ∗ ω)) W) t ConvKB [43] h, t ∈ Rd r ∈ Rd concat (σ ([h, r, t] ∗ ω)) · w HypER [56] h, t ∈ Rd wr ∈ Rdr σ vec h ∗ vec−1 (wrH) W t SACN [44] h, t ∈ Rd r ∈ Rd g (vec (M (h, r)) W) t NTN [18] h, t ∈ Rd

Neural Networks

r, br ∈ Rk, M ∈ Rd×d×k

r σ hT Mt + Mr,1h + Mr,2t + br Mr,1, Mr,2 ∈ Rk×d

A. Open and Closed World Assumption

The CWA assumes that unobserved facts are false. By contrast, the OWA has a relaxed assumption that unobserved ones can be either missing or false. Generally, OWA has an advantage over CWA because of the incompleteness nature of knowledge graphs. RESCAL [49] is a typical model trained under the CWA, while more models are formulated under the OWA.

B. Loss Function

Several families of loss function are introduced for KRL model optimization. First, a margin-based loss is optimized to learn representations that positive samples have higher scores than negative ones. Some literature also called it as pairwise ranking loss. As shown in Eq. 30 , the rank-based hinge loss maximizes the discriminative margin between a golden triple

(h,r,t) and an invalid triple (h ,r,t ).

max 0, fr(h, t) + γ − fr h , t (30)

min

Θ

(h,r,t)∈F (h ,r,t )∈F

here γ is a margin. The invalid triple (h ,r,t ) is constructed by randomly changing a head or tail entity or both entities in the knowledge graph. Most translation-based embedding methods use margin-based loss [215]. The second kind of loss function is logistic-based loss in Eq. 31, which is to minimize negative log-likelihood of logistic models.

log (1 + exp (−yhrt · fr(h, t))) (31)

min

Θ

(h,r,t)∈F∪F

here yhrt is the label of triple instance. Some methods also use other kinds of loss functions. For example, ConvE and TuckER use binary cross-entropy or the so-called Bernoulli negative log-likelihood loss function deﬁned as:

Ne

1 Ne

(yi · log (pi) + (1 − yi) · log (1 − pi)) , (32)

−

i

where p is the prediction and y is the ground label. And RotatE uses the form of loss function in Eq. 33.

n

1 k

log σ fr hi, ti − γ (33)

− log σ (γ − fr(h, t)) −

i=1

For all those kinds of loss functions, speciﬁc regularization like L2 on parameters or constraints can also be applied, as well as combined with the joint learning paradigm.

C. Negative Sampling

Several heuristics of sampling distribution are proposed to corrupt the head or tail entities. The widest applied one is uniform sampling [16], [17], [39] that uniformly replaces entities. But it leads to the sampling of false-negative labels. More effective negative sampling strategies are required to learn semantic representation and improve predictive performance.

Considering the mapping property of relations, Bernoulli sampling [20] introduces a heuristic of a sampling distribution as tphtph+hpt, where tph and hpt denote the average number of tail entities per head entity and the average number of head entities per tail entity respectively. Domain sampling [36] chooses corrupted samples from entities in the same domain or from the whole entity set with a relation-dependent probability pr or 1 − pr respectively, with the head and tail domain of relation r denoted as MHr = {h | ∃ t(h,r,t) ∈ P} and MTr = {t | ∃ h(h,r,t) ∈ P}, and induced relational set denoted as Nr = {(h,r,t) ∈ P}.

Recently, two adversarial sampling methods are further proposed. KBGAN [215] introduces adversarial learning for negative sampling, where the generator uses probability-based log-loss embedding models. The probability of generating negative samples p hj,r,tj|{(hi,ri,ti)} is deﬁned as

exp fG (hi, r, ti) j=1 exp fG hj, r, tj

, (34)

where fG(h,r,t) is the scoring function of generator. Similarly, Sun et al. [24] proposed self-adversarial negative sampling

based on self scoring function by sampling negative triples from the distribution in Eq. 35, where α is the temperature of sampling.

exp αf hj, r, tj i exp αf (hi, r, ti)

(35)

p hj, r, tj| {(hi, ri, ti)} =

Negative sampling strategies are summarized in Table VI. Trouillon et al. [23] studied the number of negative samples generated per positive training sample and found a trade-off between accuracy and training time.

TABLE VI: A summary of negative sampling

Sampling Mechanism Sampling probability Uniform [39] uniform distribution n1 Bernoulli [20] mapping property tphtph+hpt Domain [36] relation-depend domain min λ M

T r MH

r

|Nr| , 0.5 Adversarial [215] generator embedding exp fG

(hi,r,ti) j=1 exp fG h

,r,t

j Self-adversarial [24] current embedding exp αf hj,r,tj

j

i exp αf(h

i)

,r,t

i

APPENDIX E MORE KNOWLEDGE-AWARE APPLICATIONS

- A. Text Classiﬁcation and Task-Speciﬁc Applications

Knowledge-aware NLU enhances language representation with structured knowledge injected into a uniﬁed semantic space. Recent knowledge-driven advances utilize explicit factual knowledge and implicit language representation. Wang et al. [216] augmented short text representation learning with knowledge-based conceptualization by a weighted wordconcept embedding. Peng et al. [217] integrated an external knowledge base to build a heterogeneous information graph for event categorization in short social text. In the mental healthcare domain, models with knowledge graph facilitate a good understanding of mental conditions and risk factors of mental disorders and are applied to effective prevention of mental health leaded suicide. Gaurs et al. [218] developed a rulebased classiﬁer for knowledge-aware suicide risk assessment with a suicide risk severity lexicon incorporating medical knowledge bases and suicide ontology.

Sentiment analysis integrated with sentiment-related concepts can better understand people’s opinions and sentiments. SenticNet [219] learns conceptual primitives for sentiment analysis, which can also be used as a commonsense knowledge source. To enable sentiment-related information ﬁltering, Sentic LSTM [220] injects knowledge concepts to the vanilla LSTM and designs a knowledge output gate for concept-level output as a complement to the token level.

- B. Dialogue Systems


QA can also be viewed as a single-turn dialogue system by generating the correct answer as a response, while dialogue systems consider conversational sequences and aim to generate ﬂuent responses to enable multi-round conversations via semantic augmentation and knowledge graph walk. Liu et al. [221]

encoded knowledge to augment semantic representation and generated knowledge aware response by knowledge graph retrieval and graph attention mechanism under an encoderdecoder framework. DialKG Walker [222] traverses a symbolic knowledge graph to learn contextual transition in dialogue and predicts entity responses with attentive graph path decoder.

Semantic parsing via formal logical representation is another direction for dialog systems. By predeﬁning a set of base actions, Dialog-to-Action [223] is an encoder-decoder approach that maps executable logical forms from the utterance in conversation, to generate action sequence under the control of a grammar-guided decoder.

C. Medicine and Biology

Knowledge-aware models and their applications pave the way to incorporate domain knowledge for precise prediction in medicine and biology domains. Medical applications involve a domain-speciﬁc knowledge graph of medical concepts. Sousa et

- al. [224] adopted knowledge graph similarity for protein-protein interaction prediction using the Gene Ontology. Mohamed et
- al. [225] formulated drug-target interaction prediction as a link prediction in biomedical knowledge graphs with drugs and their potential targets. Lin et al. [226] developed a knowledge graph network to learn structural information and semantic relation for drug-drug interaction prediction. In the clinical domain, biomedical knowledge from the Uniﬁed Medical Language Systems (UMLS) ontology is integrated into language model pretraining for downstream clinical applications such as clinical entity recognition and medical language inference [227]. Li et al. [228] formulated the task of medical image report generation with three steps of encoding, retrieval, and paraphrasing, where the medical image is encoded by the abnormality graph.


D. Other Applications

There are also many other applications that utilize knowledgedriven methods. 1) Academic search engine helps research to ﬁnd relevant academic papers. Xiong et al. [229] proposed explicit semantic ranking with knowledge graph embedding to help academic search better understand the meaning of query concepts. 2) Zero-shot image classiﬁcation gets beneﬁts from knowledge graph propagation with semantic descriptions of classes. Wang et al. [230] proposed a multi-layer GCN to learn zero-shot classiﬁers using semantic embeddings of categories and categorical relationships. APNet [231] propagates attribute representations with a category graph. 3) Text generation synthesizes and composes coherent multi-sentence texts. Koncel-Kedziorski et al. [232] studied text generation for information extraction systems and proposed a graph transforming encoder for graph-to-text generation from the knowledge graph. Question generation focuses on generating natural language questions. Seyler et al. [233] studied quizstyle knowledge question generation by generating a structured triple-pattern query over the knowledge graph while estimating how difﬁcult the questions are. However, for verbalizing the question, the authors used a template-based method, which may have a limitation on generating more natural expressions.

APPENDIX F DATASETS AND LIBRARIES

In this section, we introduce and list useful resources of knowledge graph datasets and open-source libraries.

A. Datasets

Many public datasets have been released. We conduct an introduction and a summary of general, domain-speciﬁc, taskspeciﬁc, and temporal datasets.

1) General Datasets: Datasets with general ontological knowledge include WordNet [234], Cyc [235], DBpedia [236], YAGO [237], Freebase [238], NELL [73] and Wikidata [239]. It is hard to compare them within a table as their ontologies are different. Thus, only an informal comparison is illustrated in Table VII, where their volumes kept going after their release.

WordNet, ﬁrstly released in 1995, is a lexical database that contains about 117,000 synsets. DBpedia is a communitydriven dataset extracted from Wikipedia. It contains 103 million triples and can be enlarged when interlinked with other open datasets. To solve the problems of low coverage and low quality of single-source ontological knowledge, YAGO utilized the concept information in the category page of Wikipedia and the hierarchy information of concepts in WordNet to build a multi-source dataset with high coverage and quality. Moreover, it is extendable by other knowledge sources. It is available online with more than 10 million entities and 120 million facts currently. Freebase, a scalable knowledge base, came up for the storage of the world’s knowledge in 2008. Its current number of triples is 1.9 billion. NELL is built from the Web via an intelligent agent called Never-Ending Language Learner. It has 2,810,379 beliefs with high conﬁdence by far. Wikidata is a free structured knowledge base, which is created and maintained by human editors to facilitate the management of Wikipedia data. It is multi-lingual with 358 different languages.

The aforementioned datasets are openly published and maintained by communities or research institutions. There are also some commercial datasets. The Cyc knowledge base from Cycorp contains about 1.5 million general concepts and more than 20 million general rules, with an accessible version called OpenCyc deprecated sine 2017. Google knowledge graph hosts more than 500 million entities and 3.5 billion facts and relations. Microsoft builds a probabilistic taxonomy called Probase [72] with 2.7 million concepts.

2) Domain-Speciﬁc Datasets: Some knowledge bases on speciﬁc domains are designed and collected to evaluate domainspeciﬁc tasks. Some notable domains include life science, health care, and scientiﬁc research, covering complex domains and relations such as compounds, diseases, and tissues. Examples of domain-speciﬁc knowledge graphs are ResearchSpace6, a cultural heritage knowledge graph; UMLS [240], a uniﬁed medical language system; SNOMED CT7, a commercial clinical terminology; and a medical knowledge graph from Yidu Research8. More biological databases with domain-speciﬁc

- 6https://www.researchspace.org/index.html
- 7http://www.snomed.org/snomed-ct/ﬁve-step-brieﬁng
- 8https://www.yiducloud.com.cn/en/academy.html


TABLE VII: Statistics of datasets with general knowledge when originally released

Dataset # entities # facts Website WordNet [234] 117,597 207,016 https://wordnet.princeton.edu OpenCyc [235] 47,000 306,000 https://www.cyc.com/opencyc/ Cyc [235] ∼250,000 ∼2,200,000 https://www.cyc.com YAGO [237] 1,056,638 ∼5,000,000 http://www.mpii.mpg.de/∼suchanek/yago DBpedia [236] ∼1,950,000 ∼103,000,000 https://wiki.dbpedia.org/develop/datasets Freebase [238] - ∼125,000,000 https://developers.google.com/freebase/ NELL [73] - 242,453 http://rtw.ml.cmu.edu/rtw/ Wikidata [239] 14,449,300 30,263,656 https://www.wikidata.org/wiki Probase IsA 12,501,527 85,101,174 https://concept.research.microsoft.com/Home/Download Google KG > 500 million > 3.5 billion https://developers.google.com/knowledge-graph

knowledge include STRING, protein-protein interaction networks 9; SKEMPI, a Structural Kinetic and Energetic database of Mutant Protein Interactions [241]; Protein Data Bank (PDB) database10, containing biological molecular data [242]; GeneOntology11, a gene ontology resource that describes protein function; and DrugBank12, a pharmaceutical knowledge base [243], [244].

3) Task-Speciﬁc Datasets: A popular way of generating task-speciﬁc datasets is to sample subsets from large general datasets. Statistics of several datasets for tasks on the knowledge graph itself are listed in Table VIII. Notice that WN18 and FB15k suffer from test set leakage [55]. For KRL with auxiliary information and other downstream knowledge-aware applications, texts and images are also collected, for example, WN18-IMG [71] with sampled images and textual relation extraction dataset including SemEval 2010 dataset, NYT [245] and Google-RE13. IsaCore [246], an analogical closure of Probase for opinion mining and sentiment analysis, is built by common knowledge base blending and multi-dimensional scaling. Recently, the FewRel dataset [247] was built to evaluate the emerging few-shot relation classiﬁcation task. There are also more datasets for speciﬁc tasks such as cross-lingual DBP15K [128] and DWY100K [127] for entity alignment, multi-view knowledge graphs of YAGO26K-906 and DB111K174 [119] with instances and ontologies.

TABLE VIII: A summary of datasets for tasks on knowledge graph itself

QuAD [251] for question answering; and Freebase Semantic Scholar [229] for academic search.

B. Open-Source Libraries

Recent research has boosted the open-source campaign, with several libraries listed in Table IX. They are AmpliGraph [252] for knowledge representation learning, Grakn for integration knowledge graph with machine learning techniques, and Akutan for knowledge graph store and query. The research community has also released codes to facilitate further research. Notably, there are three useful toolkits, namely scikit-kge and OpenKE [253] for knowledge graph embedding, and OpenNRE [254] for relation extraction. We provide an online collection of knowledge graph publications, together with links to some open-source implementations of them, hosted at https://shaoxiongji.github.io/knowledge-graphs/.

TABLE IX: A summary of open-source libraries

Task Library Language URL General Grakn Python github.com/graknlabs/kglib General AmpliGraph TensorFlow github.com/Accenture/AmpliGraph General GraphVite Python graphvite.io Database Akutan Go github.com/eBay/akutan KRL OpenKE PyTorch github.com/thunlp/OpenKE KRL Fast-TransX C++ github.com/thunlp/Fast-TransX KRL scikit-kge Python github.com/mnick/scikit-kge KRL LibKGE PyTorch github.com/uma-pi1/kge KRL PyKEEN Python github.com/SmartDataAnalytics/PyKEEN RE OpenNRE PyTorch github.com/thunlp/OpenNRE

Dataset # Rel. #Ent. # Train # Valid. # Test WN18 [16] 18 40,943 141,442 5,000 5,000 FB15K [16] 1,345 14,951 483,142 50,000 59,071 WN11 [18] 11 38,696 112,581 2,609 10,544 FB13 [18] 13 75,043 316,232 5,908 23,733 WN18RR [55] 11 40,943 86,835 3,034 3,134 FB15k-237 [248] 237 14,541 272,115 17,535 20,466 FB5M [20] 1,192 5,385,322 19,193,556 50,000 59,071 FB40K [17] 1,336 39,528 370,648 67,946 96,678

Numerous downstream knowledge-aware applications also come up with many datasets, for example, WikiFacts [249] for language modeling; SimpleQuestions [250] and LC-

9https://string-db.org 10E.g., RCSB PDB (https://www.rcsb.org), a member of the worldwide PDB

- 11http://geneontology.org
- 12https://go.drugbank.com
- 13https://code.google.com/archive/p/relation-extraction-corpus/


REFERENCES

- [1] A. Newell, J. C. Shaw, and H. A. Simon, “Report on a general problem solving program,” in IFIP congress, vol. 256, 1959, p. 64.
- [2] E. Shortliffe, Computer-based medical consultations: MYCIN. Elsevier, 2012, vol. 2.
- [3] X. Dong, E. Gabrilovich, G. Heitz, W. Horn, N. Lao, K. Murphy, T. Strohmann, S. Sun, and W. Zhang, “Knowledge vault: A web-scale approach to probabilistic knowledge fusion,” in SIGKDD. ACM, 2014, pp. 601–610.
- [4] M. Nickel, K. Murphy, V. Tresp, and E. Gabrilovich, “A review of relational machine learning for knowledge graphs,” Proceedings of the IEEE, vol. 104, no. 1, pp. 11–33, 2016.
- [5] Q. Wang, Z. Mao, B. Wang, and L. Guo, “Knowledge graph embedding: A survey of approaches and applications,” IEEE TKDE, vol. 29, no. 12, pp. 2724–2743, 2017.
- [6] A. Hogan, E. Blomqvist, M. Cochez, C. d’Amato, G. de Melo, C. Gutierrez, J. E. L. Gayo, S. Kirrane, S. Neumaier, A. Polleres et al., “Knowledge graphs,” arXiv preprint arXiv:2003.02320, 2020.
- [7] F. N. Stokman and P. H. de Vries, “Structuring knowledge in a graph,” in Human-Computer Interaction, 1988, pp. 186–206.


- [8] A. Bordes, J. Weston, R. Collobert, and Y. Bengio, “Learning structured embeddings of knowledge bases,” in AAAI, 2011, pp. 301–306.
- [9] Y. Lin, X. Han, R. Xie, Z. Liu, and M. Sun, “Knowledge representation learning: A quantitative review,” arXiv preprint arXiv:1812.10901, 2018.
- [10] R. H. Richens, “Preprogramming for mechanical translation.” Mechanical Translation, vol. 3, no. 1, pp. 20–25, 1956.
- [11] H. Paulheim, “Knowledge graph reﬁnement: A survey of approaches and evaluation methods,” Semantic web, vol. 8, no. 3, pp. 489–508, 2017.
- [12] L. Ehrlinger and W. W¨oß, “Towards a deﬁnition of knowledge graphs,” SEMANTiCS (Posters, Demos, SuCCESS), vol. 48, pp. 1–4, 2016.
- [13] T. Wu, G. Qi, C. Li, and M. Wang, “A survey of techniques for constructing chinese knowledge graphs and their applications,” Sustainability, vol. 10, no. 9, p. 3245, 2018.
- [14] X. Chen, S. Jia, and Y. Xiang, “A review: Knowledge reasoning over knowledge graph,” Expert Systems with Applications, vol. 141, p. 112948, 2020.
- [15] T. Ebisu and R. Ichise, “TorusE: Knowledge graph embedding on a lie group,” in AAAI, 2018, pp. 1819–1826.
- [16] A. Bordes, N. Usunier, A. Garcia-Duran, J. Weston, and O. Yakhnenko, “Translating embeddings for modeling multi-relational data,” in NIPS, 2013, pp. 2787–2795.
- [17] Y. Lin, Z. Liu, M. Sun, Y. Liu, and X. Zhu, “Learning entity and relation embeddings for knowledge graph completion,” in AAAI, 2015, pp. 2181–2187.
- [18] R. Socher, D. Chen, C. D. Manning, and A. Ng, “Reasoning with neural tensor networks for knowledge base completion,” in NIPS, 2013, pp. 926–934.
- [19] Z. Zhang, J. Cai, Y. Zhang, and J. Wang, “Learning hierarchy-aware knowledge graph embeddings for link prediction.” in AAAI, 2020, pp. 3065–3072.
- [20] Z. Wang, J. Zhang, J. Feng, and Z. Chen, “Knowledge graph embedding by translating on hyperplanes,” in AAAI, 2014, pp. 1112–1119.
- [21] M. Nickel, L. Rosasco, and T. Poggio, “Holographic embeddings of knowledge graphs,” in AAAI, 2016, pp. 1955–1961.
- [22] H. Liu, Y. Wu, and Y. Yang, “Analogical inference for multi-relational embeddings,” in ICML, 2017, pp. 2168–2178.
- [23] T. Trouillon, J. Welbl, S. Riedel, E.´ Gaussier, and G. Bouchard, “Complex embeddings for simple link prediction,” in ICML, 2016, pp. 2071–2080.
- [24] Z. Sun, Z.-H. Deng, J.-Y. Nie, and J. Tang, “RotatE: Knowledge graph embedding by relational rotation in complex space,” in ICLR, 2019, pp. 1–18.
- [25] S. Zhang, Y. Tay, L. Yao, and Q. Liu, “Quaternion knowledge graph embedding,” in NeurIPS, 2019, pp. 2731–2741.
- [26] S. He, K. Liu, G. Ji, and J. Zhao, “Learning to represent knowledge graphs with gaussian embedding,” in CIKM, 2015, pp. 623–632.
- [27] H. Xiao, M. Huang, and X. Zhu, “TransG: A generative model for knowledge graph embedding,” in ACL, vol. 1, 2016, pp. 2316–2325.
- [28] ——, “From one point to a manifold: Orbit models for knowledge graph embedding,” in IJCAI, 2016, pp. 1315–1321.
- [29] I. Balazevic, C. Allen, and T. Hospedales, “Multi-relational poincar´e graph embeddings,” in NeurIPS, 2019, pp. 4463–4473.
- [30] I. Chami, A. Wolf, D.-C. Juan, F. Sala, S. Ravi, and C. R´e, “Lowdimensional hyperbolic knowledge graph embeddings,” in ACL, 2020.
- [31] C. Xu and R. Li, “Relation embedding with dihedral group in knowledge graph,” in ACL, 2019, pp. 263–272.
- [32] B. Yang, W.-t. Yih, X. He, J. Gao, and L. Deng, “Embedding entities and relations for learning and inference in knowledge bases,” in ICLR, 2015, pp. 1–13.
- [33] G. Ji, S. He, L. Xu, K. Liu, and J. Zhao, “Knowledge graph embedding via dynamic mapping matrix,” in ACL-IJCNLP, vol. 1, 2015, pp. 687– 696.
- [34] H. Xiao, M. Huang, Y. Hao, and X. Zhu, “TransA: An adaptive approach for knowledge graph embedding,” in AAAI, 2015, pp. 1–7.
- [35] J. Feng, M. Huang, M. Wang, M. Zhou, Y. Hao, and X. Zhu, “Knowledge graph embedding by ﬂexible translation,” in KR, 2016, pp. 557–560.
- [36] Q. Xie, X. Ma, Z. Dai, and E. Hovy, “An interpretable knowledge transfer model for knowledge base completion,” in ACL, 2017, pp. 950–962.
- [37] W. Qian, C. Fu, Y. Zhu, D. Cai, and X. He, “Translating embeddings for knowledge graph completion with relation attention mechanism.” in IJCAI, 2018, pp. 4286–4292.
- [38] S. Yang, J. Tian, H. Zhang, J. Yan, H. He, and Y. Jin, “TransMS: knowledge graph embedding for complex relations by multidirectional semantics,” in IJCAI, 2019, pp. 1935–1942.


- [39] A. Bordes, X. Glorot, J. Weston, and Y. Bengio, “A semantic matching energy function for learning with multi-relational data,” Machine Learning, vol. 94, no. 2, pp. 233–259, 2014.
- [40] Y. Xue, Y. Yuan, Z. Xu, and A. Sabharwal, “Expanding holographic embeddings for knowledge completion,” in NeurIPS, 2018, pp. 4491– 4501.
- [41] K. Hayashi and M. Shimbo, “On the equivalence of holographic and complex embeddings for link prediction,” in ACL, 2017, pp. 554–559.
- [42] W. Zhang, B. Paudel, W. Zhang, A. Bernstein, and H. Chen, “Interaction embeddings for prediction and explanation in knowledge graphs,” in WSDM, 2019, pp. 96–104.
- [43] D. Q. Nguyen, T. D. Nguyen, D. Q. Nguyen, and D. Phung, “A novel embedding model for knowledge base completion based on convolutional neural network,” in NAACL, 2018, pp. 327–333.
- [44] C. Shang, Y. Tang, J. Huang, J. Bi, X. He, and B. Zhou, “End-to-end structure-aware convolutional networks for knowledge base completion,” in AAAI, vol. 33, 2019, pp. 3060–3067.
- [45] L. Guo, Z. Sun, and W. Hu, “Learning to exploit long-term relational dependencies in knowledge graphs,” in ICML, 2019, pp. 2505–2514.
- [46] Q. Wang, P. Huang, H. Wang, S. Dai, W. Jiang, J. Liu, Y. Lyu, Y. Zhu, and H. Wu, “CoKE: Contextualized knowledge graph embedding,” arXiv preprint arXiv:1911.02168, 2019.
- [47] Y. Wang, R. Gemulla, and H. Li, “On multi-relational link prediction with bilinear models,” in AAAI, 2018, pp. 4227–4234.
- [48] S. M. Kazemi and D. Poole, “SimplE embedding for link prediction in knowledge graphs,” in NeurIPS, 2018, pp. 4284–4295.
- [49] M. Nickel, V. Tresp, and H.-P. Kriegel, “A three-way model for collective learning on multi-relational data,” in ICML, vol. 11, 2011, pp. 809–816.
- [50] ——, “Factorizing YAGO: scalable machine learning for linked data,” in WWW, 2012, pp. 271–280.
- [51] R. Jenatton, N. L. Roux, A. Bordes, and G. R. Obozinski, “A latent factor model for highly multi-relational data,” in NIPS, 2012, pp. 3167–3175.
- [52] I. Balaˇzevi´c, C. Allen, and T. M. Hospedales, “TuckER: Tensor factorization for knowledge graph completion,” in EMNLP-IJCNLP, 2019, pp. 5185–5194.
- [53] S. Amin, S. Varanasi, K. A. Dunﬁeld, and G. Neumann, “LowFER: Low-rank bilinear pooling for link prediction,” in ICML, 2020, pp. 1–11.
- [54] Q. Liu, H. Jiang, A. Evdokimov, Z.-H. Ling, X. Zhu, S. Wei, and Y. Hu, “Probabilistic reasoning via deep learning: Neural association models,” arXiv preprint arXiv:1603.07704, 2016.
- [55] T. Dettmers, P. Minervini, P. Stenetorp, and S. Riedel, “Convolutional 2d knowledge graph embeddings,” in AAAI, vol. 32, 2018, pp. 1811–1818.
- [56] I. Balaˇzevi´c, C. Allen, and T. M. Hospedales, “Hypernetwork knowledge graph embeddings,” in ICANN, 2019, pp. 553–565.
- [57] M. Gardner, P. Talukdar, J. Krishnamurthy, and T. Mitchell, “Incorporating vector space similarity in random walk inference over knowledge bases,” in EMNLP, 2014, pp. 397–406.
- [58] A. Neelakantan, B. Roth, and A. McCallum, “Compositional vector space models for knowledge base completion,” in ACL-IJCNLP, vol. 1, 2015, pp. 156–166.
- [59] L. Yao, C. Mao, and Y. Luo, “KG-BERT: BERT for knowledge graph completion,” arXiv preprent arXiv:1909.03193, 2019.
- [60] M. Schlichtkrull, T. N. Kipf, P. Bloem, R. Van Den Berg, I. Titov, and M. Welling, “Modeling relational data with graph convolutional networks,” in ESWC, 2018, pp. 593–607.
- [61] T. N. Kipf and M. Welling, “Semi-supervised classiﬁcation with graph convolutional networks,” in ICLR, 2017, pp. 1–14.
- [62] D. Nathani, J. Chauhan, C. Sharma, and M. Kaul, “Learning attentionbased embeddings for relation prediction in knowledge graphs,” in ACL, 2019, pp. 4710–4723.
- [63] S. Vashishth, S. Sanyal, V. Nitin, and P. Talukdar, “Composition-based multi-relational graph convolutional networks,” in ICLR, 2020, pp. 1–15.
- [64] Z. Wang, J. Zhang, J. Feng, and Z. Chen, “Knowledge graph and text jointly embedding,” in EMNLP, 2014, pp. 1591–1601.
- [65] R. Xie, Z. Liu, J. Jia, H. Luan, and M. Sun, “Representation learning of knowledge graphs with entity descriptions,” in AAAI, 2016, pp. 2659–2665.
- [66] H. Xiao, M. Huang, L. Meng, and X. Zhu, “SSP: semantic space projection for knowledge graph embedding with text descriptions,” in AAAI, 2017, pp. 3104–3110.
- [67] S. Guo, Q. Wang, B. Wang, L. Wang, and L. Guo, “Semantically smooth knowledge graph embedding,” in ACL-IJCNLP, vol. 1, 2015, pp. 84–94.
- [68] R. Xie, Z. Liu, and M. Sun, “Representation learning of knowledge graphs with hierarchical types,” in IJCAI, 2016, pp. 2965–2971.
- [69] Y. Lin, Z. Liu, and M. Sun, “Knowledge representation learning with entities, attributes and relations,” in IJCAI, 2016, pp. 2866–2872.


- [70] Z. Zhang, F. Zhuang, M. Qu, F. Lin, and Q. He, “Knowledge graph embedding with hierarchical relation structure,” in EMNLP, 2018, pp. 3198–3207.
- [71] R. Xie, Z. Liu, H. Luan, and M. Sun, “Image-embodied knowledge representation learning,” in IJCAI, 2017, pp. 3140–3146.
- [72] W. Wu, H. Li, H. Wang, and K. Q. Zhu, “Probase: A probabilistic taxonomy for text understanding,” in SIGMOD, 2012, pp. 481–492.
- [73] A. Carlson, J. Betteridge, B. Kisiel, B. Settles, E. R. Hruschka, and T. M. Mitchell, “Toward an architecture for never-ending language learning,” in AAAI, 2010, pp. 1306–1313.
- [74] R. Speer, J. Chin, and C. Havasi, “ConceptNet 5.5: an open multilingual graph of general knowledge,” in Proceedings of AAAI, 2017, pp. 4444– 4451.
- [75] X. Chen, M. Chen, W. Shi, Y. Sun, and C. Zaniolo, “Embedding uncertain knowledge graphs,” in AAAI, vol. 33, 2019, pp. 3363–3370.
- [76] P. Tabacof and L. Costabello, “Probability calibration for knowledge graph embedding models,” in ICLR, 2019.
- [77] T. Safavi, D. Koutra, and E. Meij, “Evaluating the Calibration of Knowledge Graph Embeddings for Trustworthy Link Prediction,” in Proceedings of EMNLP, 2020, pp. 8308–8321.
- [78] X. Han, Z. Liu, and M. Sun, “Neural knowledge acquisition via mutual attention between knowledge graph and text,” in AAAI, 2018, pp. 4832– 4839.
- [79] T. Dong, Z. Wang, J. Li, C. Bauckhage, and A. B. Cremers, “Triple classiﬁcation using regions and ﬁne-grained entity typing,” in AAAI, vol. 33, 2019, pp. 77–85.
- [80] P. Zhou, W. Shi, J. Tian, Z. Qi, B. Li, H. Hao, and B. Xu, “Attentionbased bidirectional long short-term memory networks for relation classiﬁcation,” in ACL, vol. 2, 2016, pp. 207–212.
- [81] E. Cao, D. Wang, J. Huang, and W. Hu, “Open knowledge enrichment for long-tail entities,” in The Web Conference, 2020, pp. 384–394.
- [82] B. Shi and T. Weninger, “ProjE: Embedding projection for knowledge graph completion,” in AAAI, 2017, pp. 1236–1242.
- [83] S. Guan, X. Jin, Y. Wang, and X. Cheng, “Shared embedding based neural networks for knowledge graph completion,” in CIKM, 2018, pp. 247–256.
- [84] B. Shi and T. Weninger, “Open-world knowledge graph completion,” in AAAI, 2018, pp. 1957–1964.
- [85] C. Zhang, Y. Li, N. Du, W. Fan, and P. S. Yu, “On the generative discovery of structured medical knowledge,” in SIGKDD, 2018, pp. 2720–2728.
- [86] N. Lao and W. W. Cohen, “Relational retrieval using a combination of path-constrained random walks,” Machine learning, vol. 81, no. 1, pp. 53–67, 2010.
- [87] R. Das, A. Neelakantan, D. Belanger, and A. McCallum, “Chains of reasoning over entities, relations, and text using recurrent neural networks,” in EACL, vol. 1, 2017, pp. 132–141.
- [88] W. Chen, W. Xiong, X. Yan, and W. Y. Wang, “Variational knowledge graph reasoning,” in NAACL, 2018, pp. 1823–1832.
- [89] W. Xiong, T. Hoang, and W. Y. Wang, “DeepPath: A reinforcement learning method for knowledge graph reasoning,” in EMNLP, 2017, pp. 564–573.
- [90] R. Das, S. Dhuliawala, M. Zaheer, L. Vilnis, I. Durugkar, A. Krishnamurthy, A. Smola, and A. McCallum, “Go for a walk and arrive at the answer: Reasoning over paths in knowledge bases using reinforcement learning,” in ICLR, 2018, pp. 1–18.
- [91] X. V. Lin, R. Socher, and C. Xiong, “Multi-hop knowledge graph reasoning with reward shaping,” in EMNLP, 2018, pp. 3243–3253.
- [92] Y. Shen, J. Chen, P.-S. Huang, Y. Guo, and J. Gao, “M-Walk: Learning to walk over graphs using monte carlo tree search,” in NeurIPS, 2018, pp. 6786–6797.
- [93] C. Fu, T. Chen, M. Qu, W. Jin, and X. Ren, “Collaborative policy learning for open knowledge graph reasoning,” in EMNLP, 2019, pp. 2672–2681.
- [94] L. A. Gal´arraga, C. Teﬂioudi, K. Hose, and F. Suchanek, “AMIE: association rule mining under incomplete evidence in ontological knowledge bases,” in WWW, 2013, pp. 413–422.
- [95] P. G. Omran, K. Wang, and Z. Wang, “An embedding-based approach to rule learning in knowledge graphs,” IEEE TKDE, pp. 1–12, 2019.
- [96] S. Guo, Q. Wang, L. Wang, B. Wang, and L. Guo, “Jointly embedding knowledge graphs and logical rules,” in EMNLP, 2016, pp. 192–202.
- [97] ——, “Knowledge graph embedding with iterative guidance from soft rules,” in AAAI, 2018, pp. 4816–4823.
- [98] W. Zhang, B. Paudel, L. Wang, J. Chen, H. Zhu, W. Zhang, A. Bernstein, and H. Chen, “Iteratively learning embeddings and rules for knowledge graph reasoning,” in WWW, 2019, pp. 2366–2377.


- [99] T. Rockt¨aschel and S. Riedel, “End-to-end differentiable proving,” in NIPS, 2017, pp. 3788–3800.
- [100] F. Yang, Z. Yang, and W. W. Cohen, “Differentiable learning of logical rules for knowledge base reasoning,” in NIPS, 2017, pp. 2319–2328.
- [101] P.-W. Wang, D. Stepanova, C. Domokos, and J. Z. Kolter, “Differentiable learning of numerical rules in knowledge graphs,” in ICLR, 2020, pp. 1–12.
- [102] M. Qu and J. Tang, “Probabilistic logic neural networks for reasoning,” in NeurIPS, 2019, pp. 7710–7720.
- [103] Y. Zhang, X. Chen, Y. Yang, A. Ramamurthy, B. Li, Y. Qi, and L. Song, “Efﬁcient probabilistic logic reasoning with graph neural networks,” in ICLR, 2020, pp. 1–20.
- [104] W. Xiong, M. Yu, S. Chang, X. Guo, and W. Y. Wang, “One-shot relational learning for knowledge graphs,” in EMNLP, 2018, pp. 1980– 1990.
- [105] X. Lv, Y. Gu, X. Han, L. Hou, J. Li, and Z. Liu, “Adapting meta knowledge graph information for multi-hop reasoning over few-shot relations,” in EMNLP-IJCNLP, 2019, pp. 3374–3379.
- [106] M. Chen, W. Zhang, W. Zhang, Q. Chen, and H. Chen, “Meta relational learning for few-shot link prediction in knowledge graphs,” in EMNLPIJCNLP, 2019, pp. 4217–4226.
- [107] C. Zhang, H. Yao, C. Huang, M. Jiang, Z. Li, and N. V. Chawla, “Few-shot knowledge graph completion,” in AAAI, 2020, pp. 1–8.
- [108] P. Qin, X. Wang, W. Chen, C. Zhang, W. Xu, and W. Y. Wang, “Generative adversarial zero-shot relational learning for knowledge graphs,” in AAAI, 2020, pp. 1–8.
- [109] J. Baek, D. B. Lee, and S. J. Hwang, “Learning to Extrapolate Knowledge: Transductive Few-shot Out-of-Graph Link Prediction,” in NeurIPS, 2020.
- [110] J. P. Chiu and E. Nichols, “Named entity recognition with bidirectional LSTM-CNNs,” Transactions of ACL, vol. 4, pp. 357–370, 2016.
- [111] G. Lample, M. Ballesteros, S. Subramanian, K. Kawakami, and C. Dyer, “Neural architectures for named entity recognition,” in NAACL, 2016, pp. 260–270.
- [112] C. Xia, C. Zhang, T. Yang, Y. Li, N. Du, X. Wu, W. Fan, F. Ma, and P. Yu, “Multi-grained named entity recognition,” in ACL, 2019, pp. 1430–1440.
- [113] A. Hu, Z. Dou, J.-Y. Nie, and J.-R. Wen, “Leveraging multi-token entities in document-level named entity recognition.” in AAAI, 2020, pp. 7961–7968.
- [114] X. Li, J. Feng, Y. Meng, Q. Han, F. Wu, and J. Li, “A uniﬁed MRC framework for named entity recognition,” in ACL, 2020, pp. 5849–5859.
- [115] Y. Sun, S. Wang, Y. Li, S. Feng, H. Tian, H. Wu, and H. Wang, “ERNIE 2.0: A continual pre-training framework for language understanding,” in AAAI, 2020, pp. 8968–8975.
- [116] W. Liu, P. Zhou, Z. Zhao, Z. Wang, Q. Ju, H. Deng, and P. Wang, “K-BERT: Enabling language representation with knowledge graph,” in AAAI, 2020, pp. 1–8.
- [117] X. Ren, W. He, M. Qu, C. R. Voss, H. Ji, and J. Han, “Label noise reduction in entity typing by heterogeneous partial-label embedding,” in SIGKDD, 2016, pp. 1825–1834.
- [118] Y. Ma, E. Cambria, and S. Gao, “Label embedding for zero-shot ﬁnegrained named entity typing,” in COLING, 2016, pp. 171–180.
- [119] J. Hao, M. Chen, W. Yu, Y. Sun, and W. Wang, “Universal representation learning of knowledge bases by jointly embedding instances and ontological concepts,” in KDD, 2019, pp. 1709–1719.
- [120] Y. Zhao, R. Xie, K. Liu, W. Xiaojie et al., “Connecting embeddings for knowledge graph entity typing,” in ACL, 2020, pp. 6419–6428.
- [121] H. Huang, L. Heck, and H. Ji, “Leveraging deep neural networks and knowledge graphs for entity disambiguation,” arXiv preprint arXiv:1504.07678, 2015.
- [122] W. Fang, J. Zhang, D. Wang, Z. Chen, and M. Li, “Entity disambiguation by knowledge and text jointly embedding,” in SIGNLL, 2016, pp. 260– 269.
- [123] O.-E. Ganea and T. Hofmann, “Deep joint entity disambiguation with local neural attention,” in EMNLP, 2017, pp. 2619–2629.
- [124] P. Le and I. Titov, “Improving entity linking by modeling latent relations between mentions,” in ACL, vol. 1, 2018, pp. 1595–1604.
- [125] M. Chen, Y. Tian, M. Yang, and C. Zaniolo, “Multilingual knowledge graph embeddings for cross-lingual knowledge alignment,” in IJCAI, 2017, pp. 1511–1517.
- [126] H. Zhu, R. Xie, Z. Liu, and M. Sun, “Iterative entity alignment via joint knowledge embeddings,” in IJCAI, 2017, pp. 4258–4264.
- [127] Z. Sun, W. Hu, Q. Zhang, and Y. Qu, “Bootstrapping entity alignment with knowledge graph embedding.” in IJCAI, 2018, pp. 4396–4402.
- [128] Z. Sun, W. Hu, and C. Li, “Cross-lingual entity alignment via joint attribute-preserving embedding,” in ISWC, 2017, pp. 628–644.


- [129] M. Chen, Y. Tian, K.-W. Chang, S. Skiena, and C. Zaniolo, “Cotraining embeddings of knowledge graphs and entity descriptions for cross-lingual entity alignment,” in IJCAI, 2018, pp. 3998–4004.
- [130] Q. Zhang, Z. Sun, W. Hu, M. Chen, L. Guo, and Y. Qu, “Multi-view knowledge graph embedding for entity alignment,” in IJCAI, 2019, pp. 5429–5435.
- [131] B. D. Trsedya, J. Qi, and R. Zhang, “Entity alignment between knowledge graphs using attribute embeddings,” in AAAI, vol. 33, 2019, pp. 297–304.
- [132] Z. Sun, Q. Zhang, W. Hu, C. Wang, M. Chen, F. Akrami, and C. Li, “A benchmarking study of embedding-based entity alignment for knowledge graphs,” in VLDB, 2020.
- [133] M. Craven, J. Kumlien et al., “Constructing biological knowledge bases by extracting information from text sources,” in ISMB, vol. 1999, 1999, pp. 77–86.
- [134] M. Mintz, S. Bills, R. Snow, and D. Jurafsky, “Distant supervision for relation extraction without labeled data,” in ACL and IJCNLP of the AFNLP, 2009, pp. 1003–1011.
- [135] J. Qu, D. Ouyang, W. Hua, Y. Ye, and X. Zhou, “Discovering correlations between sparse features in distant supervision for relation extraction,” in WSDM, 2019, pp. 726–734.
- [136] D. Zeng, K. Liu, S. Lai, G. Zhou, and J. Zhao, “Relation classiﬁcation via convolutional deep neural network,” in COLING, 2014, pp. 2335– 2344.
- [137] T. H. Nguyen and R. Grishman, “Relation extraction: Perspective from convolutional neural networks,” in ACL Workshop on Vector Space Modeling for Natural Language Processing, 2015, pp. 39–48.
- [138] D. Zeng, K. Liu, Y. Chen, and J. Zhao, “Distant supervision for relation extraction via piecewise convolutional neural networks,” in EMNLP,

- 2015, pp. 1753–1762.

[139] X. Jiang, Q. Wang, P. Li, and B. Wang, “Relation extraction with multi-instance multi-label convolutional neural networks,” in COLING,

- 2016, pp. 1471–1480.


- [140] H. Ye, W. Chao, Z. Luo, and Z. Li, “Jointly extracting relations with class ties via effective deep ranking,” in ACL, vol. 1, 2017, pp. 1810– 1820.
- [141] W. Zeng, Y. Lin, Z. Liu, and M. Sun, “Incorporating relation paths in neural relation extraction,” in EMNLP, 2017, pp. 1768–1777.
- [142] Y. Xu, L. Mou, G. Li, Y. Chen, H. Peng, and Z. Jin, “Classifying relations via long short term memory networks along shortest dependency paths,” in EMNLP, 2015, pp. 1785–1794.
- [143] M. Miwa and M. Bansal, “End-to-end relation extraction using lstms on sequences and tree structures,” in ACL, vol. 1, 2016, pp. 1105–1116.
- [144] R. Cai, X. Zhang, and H. Wang, “Bidirectional recurrent convolutional neural network for relation classiﬁcation,” in ACL, vol. 1, 2016, pp. 756–765.
- [145] Y. Shen and X. Huang, “Attention-based convolutional neural network for semantic relation extraction,” in COLING, 2016, pp. 2526–2536.
- [146] Y. Lin, S. Shen, Z. Liu, H. Luan, and M. Sun, “Neural relation extraction with selective attention over instances,” in ACL, vol. 1, 2016, pp. 2124– 2133.
- [147] G. Ji, K. Liu, S. He, and J. Zhao, “Distant supervision for relation extraction with sentence-level attention and entity descriptions,” in AAAI, 2017, pp. 3060–3066.
- [148] X. Han, P. Yu, Z. Liu, M. Sun, and P. Li, “Hierarchical relation extraction with coarse-to-ﬁne grained attention,” in EMNLP, 2018, pp. 2236–2245.
- [149] L. B. Soares, N. FitzGerald, J. Ling, and T. Kwiatkowski, “Matching the blanks: Distributional similarity for relation learning,” in ACL, 2019, pp. 2895–2905.
- [150] Y. Zhang, P. Qi, and C. D. Manning, “Graph convolution over pruned dependency trees improves relation extraction,” in EMNLP, 2018, pp. 2205–2215.
- [151] Z. Guo, Y. Zhang, and W. Lu, “Attention guided graph convolutional networks for relation extraction,” in ACL, 2019, pp. 241–251.
- [152] N. Zhang, S. Deng, Z. Sun, G. Wang, X. Chen, W. Zhang, and H. Chen, “Long-tail relation extraction via knowledge graph embeddings and graph convolution networks,” in NAACL, 2019, pp. 3016–3025.
- [153] Y. Wu, D. Bamman, and S. Russell, “Adversarial training for relation extraction,” in EMNLP, 2017, pp. 1778–1783.
- [154] P. Qin, X. Weiran, and W. Y. Wang, “DSGAN: Generative adversarial training for distant supervision relation extraction,” in ACL, vol. 1, 2018, pp. 496–505.
- [155] P. Qin, W. Xu, and W. Y. Wang, “Robust distant supervision relation extraction via deep reinforcement learning,” in ACL, vol. 1, 2018, pp. 2137–2147.


- [156] X. Zeng, S. He, K. Liu, and J. Zhao, “Large scaled relation extraction with reinforcement learning,” in AAAI, 2018, pp. 5658–5665.
- [157] J. Feng, M. Huang, L. Zhao, Y. Yang, and X. Zhu, “Reinforcement learning for relation classiﬁcation from noisy data,” in AAAI, 2018, pp. 5779–5786.
- [158] R. Takanobu, T. Zhang, J. Liu, and M. Huang, “A hierarchical framework for relation extraction with reinforcement learning,” in AAAI, vol. 33, 2019, pp. 7072–7079.
- [159] Y. Huang and W. Y. Wang, “Deep residual learning for weaklysupervised relation extraction,” in EMNLP, 2017, pp. 1803–1807.
- [160] T. Liu, X. Zhang, W. Zhou, and W. Jia, “Neural relation extraction via inner-sentence noise reduction and transfer learning,” in EMNLP, 2018, pp. 2195–2204.
- [161] K. Lei, D. Chen, Y. Li, N. Du, M. Yang, W. Fan, and Y. Shen, “Cooperative denoising for distantly supervised relation extraction,” in COLING, 2018, pp. 426–436.
- [162] H. Jiang, L. Cui, Z. Xu, D. Yang, J. Chen, C. Li, J. Liu, J. Liang, C. Wang, Y. Xiao, and W. Wang, “Relation extraction using supervision from topic knowledge of relation labels,” in IJCAI, 2019, pp. 5024–5030.
- [163] H. Shahbazi, X. Z. Fern, R. Ghaeini, and P. Tadepalli, “Relation extraction with explanation,” in ACL, 2020, pp. 6488–6494.
- [164] T. Gao, X. Han, Z. Liu, and M. Sun, “Hybrid attention-based prototypical networks for noisy few-shot relation classiﬁcation,” in AAAI, vol. 33,

- 2019, pp. 6407–6414.

[165] M. Qu, T. Gao, L.-P. A. Xhonneux, and J. Tang, “Few-shot relation extraction via bayesian meta-learning on relation graphs,” in ICML,

- 2020, pp. 1–10.


- [166] M. Miwa and Y. Sasaki, “Modeling joint entity and relation extraction with table representation,” in EMNLP, 2014, pp. 1858–1869.
- [167] A. Katiyar and C. Cardie, “Going out on a limb: Joint extraction of entity mentions and relations without dependency trees,” in ACL, 2017, pp. 917–928.
- [168] S. Zheng, F. Wang, H. Bao, Y. Hao, P. Zhou, and B. Xu, “Joint extraction of entities and relations based on a novel tagging scheme,” in ACL, 2017, pp. 1227–1236.
- [169] X. Li, F. Yin, Z. Sun, X. Li, A. Yuan, D. Chai, M. Zhou, and J. Li, “Entity-relation extraction as multi-turn question answering,” in ACL, 2019, pp. 1340–1350.
- [170] D. Dai, X. Xiao, Y. Lyu, S. Dou, Q. She, and H. Wang, “Joint extraction of entities and overlapping relations using position-attentive sequence labeling,” in AAAI, vol. 33, 2019, pp. 6300–6308.
- [171] Z. Wei, J. Su, Y. Wang, Y. Tian, and Y. Chang, “A novel cascade binary tagging framework for relational triple extraction,” in ACL, 2020, pp. 1476–1488.
- [172] Y. Wang, B. Yu, Y. Zhang, T. Liu, H. Zhu, and L. Sun, “Tplinker: Single-stage joint extraction of entities and relations through token pair linking,” in COLING, 2020, pp. 1572–1582.
- [173] Z. Zhong and D. Chen, “A frustratingly easy approach for joint entity and relation extraction,” arXiv preprint arXiv:2010.12812, 2020.
- [174] D. Xu, C. Ruan, E. Korpeoglu, S. Kumar, and K. Achan, “Inductive representation learning on temporal graphs,” in ICLR, 2020, pp. 1–19.
- [175] J. Leblay and M. W. Chekol, “Deriving validity time in knowledge graph,” in WWW, 2018, pp. 1771–1776.
- [176] Y. Ma, V. Tresp, and E. A. Daxberger, “Embedding models for episodic knowledge graphs,” Journal of Web Semantics, vol. 59, p. 100490, 2019.
- [177] S. S. Dasgupta, S. N. Ray, and P. Talukdar, “Hyte: Hyperplane-based temporally aware knowledge graph embedding,” in EMNLP, 2018, pp. 2001–2011.
- [178] A. Garc´ıa-Dur´an, S. Dumanˇci´c, and M. Niepert, “Learning sequence encoders for temporal knowledge graph completion,” in EMNLP, 2018, pp. 4816–4821.
- [179] Y. Liu, W. Hua, K. Xin, and X. Zhou, “Context-aware temporal knowledge graph embedding,” in WISE, 2019, pp. 583–598.
- [180] T. Lacroix, G. Obozinski, and N. Usunier, “Tensor decompositions for temporal knowledge base completion,” in ICLR, 2020, pp. 1–12.
- [181] D. T. Wijaya, N. Nakashole, and T. M. Mitchell, “CTPs: Contextual temporal proﬁles for time scoping facts using state change detection,” in EMNLP, 2014, pp. 1930–1936.
- [182] R. Goel, S. M. Kazemi, M. Brubaker, and P. Poupart, “Diachronic embedding for temporal knowledge graph completion,” in AAAI, 2020, pp. 3988–3995.
- [183] R. Trivedi, H. Dai, Y. Wang, and L. Song, “Know-evolve: Deep temporal reasoning for dynamic knowledge graphs,” in ICML, 2017, pp. 3462– 3471.
- [184] W. Jin, C. Zhang, P. Szekely, and X. Ren, “Recurrent event network for reasoning over temporal knowledge graphs,” in ICLR RLGM Workshop, 2019.


- [185] T. Jiang, T. Liu, T. Ge, L. Sha, B. Chang, S. Li, and Z. Sui, “Towards time-aware knowledge graph completion,” in COLING, 2016, pp. 1715– 1724.
- [186] T. Jiang, T. Liu, T. Ge, L. Sha, S. Li, B. Chang, and Z. Sui, “Encoding temporal information for time-aware link prediction,” in EMNLP, 2016, pp. 2350–2354.
- [187] M. W. Chekol, G. Pirr`o, J. Schoenﬁsch, and H. Stuckenschmidt, “Marrying uncertainty and time in knowledge graphs,” in AAAI, 2017, pp. 88–94.
- [188] R. Logan, N. F. Liu, M. E. Peters, M. Gardner, and S. Singh, “Barack’s wife hillary: Using knowledge graphs for fact-aware language modeling,” in ACL, 2019, pp. 5962–5971.
- [189] Z. Zhang, X. Han, Z. Liu, X. Jiang, M. Sun, and Q. Liu, “ERNIE: Enhanced language representation with informative entities,” in ACL, 2019, pp. 1441–1451.
- [190] Y. Sun, S. Wang, Y. Li, S. Feng, X. Chen, H. Zhang, X. Tian, D. Zhu, H. Tian, and H. Wu, “ERNIE: Enhanced representation through knowledge integration,” arXiv preprint arXiv:1904.09223, 2019.
- [191] X. Wang, T. Gao, Z. Zhu, Z. Liu, J. Li, and J. Tang, “KEPLER: A uniﬁed model for knowledge embedding and pre-trained language representation,” TACL, 2020.
- [192] T. Shen, Y. Mao, P. He, G. Long, A. Trischler, and W. Chen, “Exploiting structured knowledge in text via graph-guided representation learning,” in EMNLP, 2020.
- [193] T. Sun, Y. Shao, X. Qiu, Q. Guo, Y. Hu, X.-J. Huang, and Z. Zhang, “CoLAKE: Contextualized Language and Knowledge Embedding,” in COLING, 2020, pp. 3660–3670.
- [194] B. He, D. Zhou, J. Xiao, Q. Liu, N. J. Yuan, T. Xu et al., “BERT-MK: Integrating Graph Contextualized Knowledge into Pre-trained Language Models,” in Findings of EMNLP, 2020, p. 2281–2290.
- [195] F. Petroni, T. Rockt¨aschel, S. Riedel, P. Lewis, A. Bakhtin, Y. Wu, and A. Miller, “Language models as knowledge bases?” in EMNLP-IJCNLP, 2019, pp. 2463–2473.
- [196] Z. Dai, L. Li, and W. Xu, “CFO: Conditional focused neural question answering with large-scale knowledge bases,” in ACL, vol. 1, 2016, pp. 800–810.
- [197] Y. Chen, L. Wu, and M. J. Zaki, “Bidirectional attentive memory networks for question answering over knowledge bases,” in NAACL, 2019, pp. 2913–2923.
- [198] S. Mohammed, P. Shi, and J. Lin, “Strong baselines for simple question answering over knowledge graphs with and without neural networks,” in NAACL, 2018, pp. 291–296.
- [199] L. Bauer, Y. Wang, and M. Bansal, “Commonsense for generative multi-hop question answering tasks,” in EMNLP, 2018, pp. 4220–4230.
- [200] Y. Zhang, H. Dai, Z. Kozareva, A. J. Smola, and L. Song, “Variational reasoning for question answering with knowledge graph,” in AAAI, 2018, pp. 6069–6076.
- [201] B. Y. Lin, X. Chen, J. Chen, and X. Ren, “KagNet: Knowledge-aware graph networks for commonsense reasoning,” in EMNLP-IJCNLP, 2019, pp. 2829–2839.
- [202] M. Ding, C. Zhou, Q. Chen, H. Yang, and J. Tang, “Cognitive graph for multi-hop reading comprehension at scale,” in ACL, 2019, pp. 2694– 2703.
- [203] F. Zhang, N. J. Yuan, D. Lian, X. Xie, and W.-Y. Ma, “Collaborative knowledge base embedding for recommender systems,” in SIGKDD, 2016, pp. 353–362.
- [204] H. Wang, F. Zhang, X. Xie, and M. Guo, “DKN: Deep knowledge-aware network for news recommendation,” in WWW, 2018, pp. 1835–1844.
- [205] H. Wang, F. Zhang, M. Zhao, W. Li, X. Xie, and M. Guo, “Multi-task feature learning for knowledge graph enhanced recommendation,” in WWW, 2019, pp. 2000–2010.
- [206] X. Wang, D. Wang, C. Xu, X. He, Y. Cao, and T.-S. Chua, “Explainable reasoning over knowledge graphs for recommendation,” in AAAI, vol. 33, 2019, pp. 5329–5336.
- [207] Y. Xian, Z. Fu, S. Muthukrishnan, G. de Melo, and Y. Zhang, “Reinforcement knowledge graph reasoning for explainable recommendation,” in SIGIR, 2019.
- [208] X. Wang, X. He, Y. Cao, M. Liu, and T.-S. Chua, “KGAT: Knowledge graph attention network for recommendation,” in SIGKDD, 2019, pp. 950–958.
- [209] A. Sharma, P. Talukdar et al., “Towards understanding the geometry of knowledge graph embeddings,” in ACL, 2018, pp. 122–131.
- [210] P. W. Battaglia, J. B. Hamrick, V. Bapst, A. Sanchez-Gonzalez, V. Zambaldi, M. Malinowski, A. Tacchetti, D. Raposo, A. Santoro, R. Faulkner et al., “Relational inductive biases, deep learning, and graph networks,” arXiv preprint arXiv:1806.01261, 2018.


- [211] M. Fan, Q. Zhou, E. Chang, and T. F. Zheng, “Transition-based knowledge graph embedding with relational mapping properties,” in PACLIC, 2014, pp. 328–337.
- [212] G. Ji, K. Liu, S. He, and J. Zhao, “Knowledge graph completion with adaptive sparse transfer matrix,” in AAAI, 2016, pp. 985–991.
- [213] A. Garc´ıa-Dur´an, A. Bordes, and N. Usunier, “Effective blending of two and three-way interactions for modeling multi-relational data,” in ECML. Springer, 2014, pp. 434–449.
- [214] R. Reiter, “Deductive question-answering on relational data bases,” in Logic and data bases. Springer, 1978, pp. 149–177.
- [215] L. Cai and W. Y. Wang, “KBGAN: Adversarial learning for knowledge graph embeddings,” in NAACL, 2018, pp. 1470–1480.
- [216] J. Wang, Z. Wang, D. Zhang, and J. Yan, “Combining knowledge with deep convolutional neural networks for short text classiﬁcation.” in IJCAI, 2017, pp. 2915–2921.
- [217] H. Peng, J. Li, Q. Gong, Y. Song, Y. Ning, K. Lai, and P. S. Yu, “Finegrained event categorization with heterogeneous graph convolutional networks,” in IJCAI, 2019, pp. 3238–3245.
- [218] M. Gaur, A. Alambo, J. P. Sain, U. Kursuncu, K. Thirunarayan, R. Kavuluru, A. Sheth, R. S. Welton, and J. Pathak, “Knowledgeaware assessment of severity of suicide risk for early intervention,” in WWW, 2019, pp. 514–525.
- [219] E. Cambria, S. Poria, D. Hazarika, and K. Kwok, “SenticNet 5: Discovering conceptual primitives for sentiment analysis by means of context embeddings,” in AAAI, 2018, pp. 1795–1802.
- [220] Y. Ma, H. Peng, and E. Cambria, “Targeted aspect-based sentiment analysis via embedding commonsense knowledge into an attentive lstm,” in AAAI, 2018, pp. 5876–5883.
- [221] Z. Liu, Z.-Y. Niu, H. Wu, and H. Wang, “Knowledge aware conversation generation with explainable reasoning over augmented graphs,” in EMNLP, 2019, pp. 1782–1792.
- [222] S. Moon, P. Shah, A. Kumar, and R. Subba, “OpenDialKG: Explainable conversational reasoning with attention-based walks over knowledge graphs,” in ACL, 2019, pp. 845–854.
- [223] D. Guo, D. Tang, N. Duan, M. Zhou, and J. Yin, “Dialog-to-Action: Conversational question answering over a large-scale knowledge base,” in NeurIPS, 2018, pp. 2942–2951.
- [224] R. T. Sousa, S. Silva, and C. Pesquita, “Evolving knowledge graph similarity for supervised learning in complex biomedical domains,” BMC Bioinformatics, vol. 21, no. 1, p. 6, 2020.
- [225] S. K. Mohamed, V. Nov´aˇcek, and A. Nounu, “Discovering protein drug targets using knowledge graph embeddings,” Bioinformatics, vol. 36, no. 2, pp. 603–610, 2020.
- [226] X. Lin, Z. Quan, Z.-J. Wang, T. Ma, and X. Zeng, “KGNN: Knowledge graph neural network for drug-drug interaction prediction.” IJCAI, 2020.
- [227] B. Hao, H. Zhu, and I. Paschalidis, “Enhancing Clinical BERT Embedding using a Biomedical Knowledge Base,” in Proceedings of COLING, 2020, pp. 657–661.
- [228] C. Y. Li, X. Liang, Z. Hu, and E. P. Xing, “Knowledge-driven encode, retrieve, paraphrase for medical image report generation,” arXiv preprint arXiv:1903.10122, 2019.
- [229] C. Xiong, R. Power, and J. Callan, “Explicit semantic ranking for academic search via knowledge graph embedding,” in WWW, 2017, pp. 1271–1279.
- [230] X. Wang, Y. Ye, and A. Gupta, “Zero-shot recognition via semantic embeddings and knowledge graphs,” in CVPR, 2018, pp. 6857–6866.
- [231] L. Liu, T. Zhou, G. Long, J. Jiang, and C. Zhang, “Attribute propagation network for graph zero-shot learning,” in AAAI, 2020, pp. 4868–4875.
- [232] R. Koncel-Kedziorski, D. Bekal, Y. Luan, M. Lapata, and H. Hajishirzi, “Text generation from knowledge graphs with graph transformers,” in NAACL, 2019, pp. 2284–2293.
- [233] D. Seyler, M. Yahya, and K. Berberich, “Knowledge questions from knowledge graphs,” in SIGIR, 2017, pp. 11–18.
- [234] G. A. Miller, “WordNet: a lexical database for english,” Communications of the ACM, vol. 38, no. 11, pp. 39–41, 1995.
- [235] C. Matuszek, M. Witbrock, J. Cabral, and J. DeOliveira, “An introduction to the syntax and content of cyc,” in AAAI Spring Symposium on Formalizing and Compiling Background Knowledge and Its Applications to Knowledge Representation and Question Answering, 2006, pp. 1–6.
- [236] S. Auer, C. Bizer, G. Kobilarov, J. Lehmann, R. Cyganiak, and Z. Ives, “Dbpedia: A nucleus for a web of open data,” in The semantic web, 2007, pp. 722–735.
- [237] F. M. Suchanek, G. Kasneci, and G. Weikum, “Yago: a core of semantic knowledge,” in WWW, 2007, pp. 697–706.
- [238] K. Bollacker, C. Evans, P. Paritosh, T. Sturge, and J. Taylor, “Freebase: a collaboratively created graph database for structuring human knowledge,” in SIGMOD, 2008, pp. 1247–1250.


- [239] D. Vrandeˇci´c and M. Kr¨otzsch, “Wikidata: a free collaborative knowledge base,” Communications of the ACM, vol. 57, no. 10, pp. 78–85, 2014.
- [240] A. T. McCray, “An upper-level ontology for the biomedical domain,” International Journal of Genomics, vol. 4, no. 1, pp. 80–84, 2003.
- [241] I. H. Moal and J. Fern´andez-Recio, “SKEMPI: a Structural Kinetic and Energetic database of Mutant Protein Interactions and its use in empirical models,” Bioinformatics, vol. 28, no. 20, pp. 2600–2607, 2012.
- [242] H. M. Berman, J. Westbrook, Z. Feng, G. Gilliland, T. N. Bhat, H. Weissig, I. N. Shindyalov, and P. E. Bourne, “The protein data bank,” Nucleic acids research, vol. 28, no. 1, pp. 235–242, 2000.
- [243] D. S. Wishart, C. Knox, A. C. Guo, S. Shrivastava, M. Hassanali, P. Stothard, Z. Chang, and J. Woolsey, “DrugBank: a comprehensive resource for in silico drug discovery and exploration,” Nucleic acids research, vol. 34, no. suppl 1, pp. D668–D672, 2006.

- [244] D. S. Wishart, C. Knox, A. C. Guo, D. Cheng, S. Shrivastava, D. Tzur, B. Gautam, and M. Hassanali, “DrugBank: a knowledgebase for drugs, drug actions and drug targets,” Nucleic acids research, vol. 36, no. suppl 1, pp. D901–D906, 2008.

- [245] S. Riedel, L. Yao, and A. McCallum, “Modeling relations and their mentions without labeled text,” in ECML, 2010, pp. 148–163.
- [246] E. Cambria, Y. Song, H. Wang, and N. Howard, “Semantic multidimensional scaling for open-domain sentiment analysis,” IEEE Intelligent


- Systems, vol. 29, no. 2, pp. 44–51, 2012.
- [247] X. Han, H. Zhu, P. Yu, Z. Wang, Y. Yao, Z. Liu, and M. Sun, “Fewrel: A large-scale supervised few-shot relation classiﬁcation dataset with state-of-the-art evaluation,” in EMNLP, 2018, pp. 4803–4809.
- [248] K. Toutanova and D. Chen, “Observed versus latent features for knowledge base and text inference,” in ACL Workshop on CVSC, 2015, pp. 57–66.
- [249] S. Ahn, H. Choi, T. P¨arnamaa, and Y. Bengio, “A neural knowledge language model,” arXiv preprint arXiv:1608.00318, 2016.
- [250] A. Bordes, N. Usunier, S. Chopra, and J. Weston, “Large-scale simple question answering with memory networks,” arXiv preprint arXiv:1506.02075, 2015.
- [251] P. Trivedi, G. Maheshwari, M. Dubey, and J. Lehmann, “LC-QuAD: A corpus for complex question answering over knowledge graphs,” in ISWC, 2017, pp. 210–218.
- [252] L. Costabello, S. Pai, C. L. Van, R. McGrath, and N. McCarthy, “AmpliGraph: a Library for Representation Learning on Knowledge Graphs,” 2019.
- [253] X. Han, S. Cao, L. Xin, Y. Lin, Z. Liu, M. Sun, and J. Li, “OpenKE: An open toolkit for knowledge embedding,” in EMNLP, 2018, pp. 139–144.
- [254] X. Han, T. Gao, Y. Yao, D. Ye, Z. Liu, and M. Sun, “OpenNRE: An open and extensible toolkit for neural relation extraction,” in EMNLPIJCNLP, 2019, pp. 169–174.


