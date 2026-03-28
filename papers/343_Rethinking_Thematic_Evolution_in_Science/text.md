# arXiv:2603.06436v1[cs.SI]6 Mar 2026

## RETHINKING THEMATIC EVOLUTION IN SCIENCE MAPPING: AN INTEGRATED FRAMEWORK FOR LONGITUDINAL ANALYSIS*

A PREPRINT

#### Massimo Aria †1, Luca D’aniello 1, Michelangelo Misuraca 2, and Maria Spano 1

- 1Department of Economics and Statistics, University of Naples Federico II, 81026 – Naples, Italy
- 2Department of Management & Innovation Systems, University of Salerno, 84084 – Fisciano, Italy


March 9, 2026

### ABSTRACT

Strategic diagrams and co-word analysis are widely employed to examine the conceptual structure of scientiﬁc domains and their development over time. Yet a structural inconsistency characterises dominant longitudinal implementations: themes are detected through relational clustering in weighted networks, whereas their inter-temporal connections are commonly inferred from set-theoretic overlap among keywords or core documents. This study introduces a structurally integrated framework in which lineage reconstruction is embedded within the same weighted relational architecture that underpins cross-sectional detection. The approach models thematic continuity through graded document afﬁliation and a lineage-strength measure that combines directional coverage with centralityweighted structural relevance, thereby conceptualising evolution as the reconﬁguration of relational structures rather than simple lexical persistence. By aligning thematic detection and temporal modelling within a uniﬁed relational paradigm, the framework enhances the methodological coherence and interpretive robustness of longitudinal science mapping.

Keywords Co-word analysis · Fuzzy afﬁliation · Longitudinal network modelling

### 1 Introduction

The quantitative study of scientiﬁc knowledge has increasingly relied on formal models that represent its structural organisation and temporal dynamics. Within this broader landscape, science mapping has emerged as a central methodological paradigm, complementing performance analysis by focusing on the relational architecture of research domains [14, 5, 18]. By leveraging bibliographic data, science mapping seeks to depict in a systematic and reproducible manner the intellectual and conceptual conﬁguration of scientiﬁc ﬁelds. Among the available approaches, co-word analysis has played a pivotal role in operationalising conceptual structure. Since the seminal contributions of Callon et al. [8] and the subsequent formalisation of the strategic diagram [7], networks of term co-occurrence have been used to identify thematic areas and to characterise their structural role within a domain. The combination of community detection and the centrality-density framework has provided an interpretable representation in which themes are classiﬁed according to their strategic importance and internal development. Over time, this paradigm has been consolidated through methodological reﬁnements and dedicated software tools [11, 1], becoming a standard instrument in both cross-sectional and longitudinal bibliometric investigations.

The progressive growth of scientiﬁc production and the increasing interdisciplinarity of research have heightened interest in modelling the dynamic evolution of themes, moving beyond purely static conﬁgurations. Existing longitudinal extensions typically identify thematic clusters independently across successive time periods and subsequently establish intertemporal connections using measures of keyword overlap. This procedure has enabled the systematic detection

∗The algorithm underlying the proposed methodology has been implemented in the development version of the R package bibliometrix. The package is available through the project’s GitHub repository: https://github.com/massimoaria/bibliometrix.

†Corresponding author: aria@unina.it

of continuities, splits, and mergers, thereby offering valuable empirical insights into knowledge dynamics. In parallel, several alternative traditions have addressed longitudinal conceptual change through probabilistic topic models, embedding-based semantic drift measures, or dynamic community detection [3, 12, 16]. These approaches have expanded the methodological repertoire available for studying knowledge dynamics, yet they often involve trade-offs between interpretability, parameterisation, and the transparency of the linkage mechanism. In this setting, strategic mapping remains attractive because it provides an explicit structural representation of themes grounded in observable co-occurrence relations. The present work builds on this strength and targets a speciﬁc methodological discontinuity in dominant longitudinal implementations, namely the divergence between relational theme detection and predominantly lexical lineage construction. Yet the prevailing approach implicitly conceptualises thematic evolution as a problem of alignment between independently derived partitions. Continuity is generally inferred from lexical similarity, while the relational structure that deﬁnes themes cross-sectionally plays only a limited role in modelling their transformation. Moreover, document-level afﬁliation is not explicitly incorporated into lineage mechanisms, and thematic assignment remains predominantly crisp, notwithstanding the increasingly hybrid character of contemporary research. As a result, the representation of evolution may privilege the persistence of vocabulary over the preservation and reconﬁguration of structural relations.

This paper proposes a re-speciﬁcation of longitudinal thematic analysis grounded in a structurally integrated framework. Building upon the co-word tradition, the proposed approach reconceptualises thematic evolution as a networkbased process in which cross-sectional conﬁguration, graded document afﬁliation, and inter-temporal linkage are jointly modelled within a coherent analytical architecture. The objective is not to replace the strategic diagram paradigm, but to extend its explanatory scope by embedding thematic continuity in a formally deﬁned relational representation that enhances methodological coherence and interpretability.

### 2 Conceptual and Methodological Background

Co-word analysis is a foundational methodology for exploring the conceptual organisation of scientiﬁc domains. Introduced by Callon et al. [8, 9], the approach rests on the premise that recurrent co-occurrence patterns among keywords reveal latent thematic structures. Terms are represented as nodes in a network, and their joint appearances deﬁne weighted edges; cohesive subgraphs extracted from this network are interpreted as themes. In this perspective, thematic areas emerge from relational conﬁgurations grounded in observed associations, without relying on predeﬁned classiﬁcations. A decisive theoretical reﬁnement was the evaluation of thematic clusters along two structural dimensions: centrality and density. Centrality reﬂects the extent to which a cluster’s connections with the remainder of the network, and therefore its strategic positioning within the broader domain. Density measures internal cohesion and indicates the degree of conceptual development a theme has achieved. These dimensions were operationalised in the strategic diagram [7], which maps themes onto a two-dimensional space and enables a functional interpretation of their roles within the ﬁeld. The enduring relevance of this representation lies in its capacity to translate network-theoretic properties into an analytically meaningful typology [13].

Subsequent methodological developments have concentrated on improving the robustness of cross-sectional mapping. The adoption of association strength normalisation has been shown to attenuate frequency bias and preserve relational information in co-occurrence networks [19]. Other studies have demonstrated the sensitivity of thematic conﬁgurations to preprocessing choices, term selection, and thresholding decisions, highlighting the importance of methodological consistency. These reﬁnements have strengthened the reliability of thematic detection within individual time slices. The extension of this paradigm to longitudinal analysis has generally proceeded by applying thematic detection independently to successive periods and then establishing connections among clusters across time. The framework proposed by Cobo et al. [10] systematised this procedure by introducing overlap-based similarity measures to identify continuities, splits, and mergers between themes. Inter-temporal relations are thus inferred from the degree of shared vocabulary between clusters identiﬁed in adjacent periods.

A structural asymmetry, however, exists in this dominant paradigm. Whereas cross-sectional detection is explicitly relational, lineage construction is typically reduced to set-theoretic comparisons among term lists, with the consequence that the weighted association structure deﬁning a clusters semantic core does not enter the linkage mechanism. Continuity is thus inferred solely from lexical overlap, leaving aside the preservation or reconﬁguration of underlying structural relations. Likewise, document-level dynamics are not incorporated into the deﬁnition of thematic evolution. Publications are indirectly associated with clusters via their constituent terms, yet their distribution across themes does not explicitly inform modelling of inter-temporal transitions. The reallocation of scientiﬁc production across evolving thematic conﬁgurations thus remains analytically external to the linkage procedure. The asymmetry is reinforced by the widespread reliance on crisp community detection, which executes mutually exclusive term assignment and only indirectly associates publications with themes through their vocabularies. Such partitions offer a clear decomposition

of the term network, but they are not designed to represent graded thematic participation, which is increasingly salient in interdisciplinary environments in which both terms and publications span multiple domains.

These characteristics collectively indicate that existing longitudinal frameworks treat thematic evolution as a correspondence problem between independently derived partitions, generating a conceptual discontinuity between crosssectional representation and temporal transformation. Addressing this discontinuity requires aligning thematic detection, document afﬁliation, and inter-temporal linkage within a uniﬁed relational architecture.

### 3 An Integrated Framework for Longitudinal Thematic Analysis

Let D = {d1,...,dn} denote a set of publications and T = {t1,...,tp} the ordered set of time periods, with ti < ti+1. Each publication belongs to exactly one period on the basis of publication date, so that D(t) ∩ D(t

′) = ∅ for t ̸= t′

and t∈T D(t) = D. For each period t ∈ T, let K(t) denote the set of terms observed in D(t). The analytical goal is twofold. First, we aim to identify for each period t a set of thematic clusters representing coherent research topics:

C(t) = {C1(t),...,Ch(t),...,Cn(t)

} (1) Second, we aim to track the evolutionary relations between clusters in consecutive periods through a lineage function: L(Ch(t),Ch(t′+1)) (2)

t

The resulting structure is a temporally ordered directed graph G = (V,E), where vertices are V = t∈T C(t) and edges represent statistically and substantively meaningful evolutionary connections. The strategy yields a formally

coherent and interpretable account of thematic evolution based on weighted network structure and fuzzy publication afﬁliation, overcoming the limits of binary overlap heuristics.

#### 3.1 Cross-Sectional Thematic Representation

The procedure begins by structuring and organising publications’ content and performing thematic detection. For each period t, terms are extracted from D(t) and a co-occurrence matrix W(t) = [wij(t)] is constructed. Terms can be listed in author keywords, index keywords, or n-grams extracted from titles or abstracts. The generic element of W(t) is expressed as association (or equivalence) index [15, 17] between terms ki and kj, deﬁned as

c(ijt) c(iit)c(jjt)

wij(t) =

(3)

where cij(t) denotes the co-occurrence frequency of the terms, whereas c(iit) and c(jjt) are their occurrences. The matrix W(t) induces a weighted network on K(t), capturing the semantic structure of the collection in period t. To obtain the cluster partition C(t) from the collection, a community detection algorithm is applied to W(t) [2]. For each cluster

Ch(t), the set of related terms is denoted by K(Ch(t)) ⊆ K(t). Structural properties are computed to depict and map clusters, such as centrality and density measures derived from the internal and external link conﬁguration of W(t) [10]. Clusters with negligible cumulative term frequency are ﬁltered out using a predeﬁned threshold to ensure analytical stability.

#### 3.2 Fuzzy Publication-to-Cluster Assignment

Hard partitioning at the publication level is replaced by a fuzzy membership scheme over the clusters C(t), considering that publications may exhibit varying degrees of afﬁliation with multiple themes. For each publication di ∈ D(t) and cluster Ch(t), we compute a similarity score based on the overlap between the publication’s terms and the cluster’s characteristic terms, weighted by term centrality within the cluster, deﬁned as

PR(kt)(Ch) freq(kt)

s(iht) =

(4)

k∈K(di)∩K(Ch(t))

where PR(kt)(Ch) is the PageRank centrality [6, 21] of term k within cluster Ch(t) and freq(kt) its period-speciﬁc frequency in t.

According to Eq. 4, publications’ afﬁliation with a cluster is stronger when publications encompass more terms from the cluster itself, and these shared terms are central (high PageRank) within the cluster’s semantic structure and distinctive (low frequency) rather than ubiquitous across the collection. The membership degree is then normalised to obtain a distribution over clusters

nt

s(iht)

u(iht) =

u(iht) = 1 (5)

, with

nt j=1 s(ijt)

h=1

The resulting fuzzy membership matrix U(t) = [u(iht)] encodes the multithematic nature of publications. In the rare case where a publication has zero similarity with all clusters (i.e., none of its terms appears in any cluster) due to a

very restrictive term ﬁltering, a uniform membership probability u(iht) = 1/nt is assigned for all h topics to ensure numerical stability. The effective size of each cluster, accounting for partial memberships, is computed as:

|D(t)|

u(iht) (6) which captures cumulative and graded afﬁliations, avoiding the constraints of exclusive assignments.

|Ch(t)| =

i=1

#### 3.3 Inter-Temporal Assignment and Lineage Strength

To formalise lineage, we distinguish between coverage and structural relevance. Coverage captures how much of a source theme’s semantic mass is carried forward into a candidate successor, while structural relevance evaluates whether the shared content corresponds to conceptually central elements in both themes. These two dimensions are complementary: the former is directional and sensitive to what is retained from the source, whereas the latter reﬂects mutual thematic coherence. After performing period-speciﬁc analyses for all periods t ∈ T, we quantify the evolutionary connections between clusters in consecutive periods through a lineage strength measure. This measure integrates two complementary dimensions: the weighted inclusion of terms and the importance of shared terms, measured by

their centrality. Let S(Ch(t),Cj(t+1)) = K(Ch(t)) ∩ K(Cj(t+1)) denote the shared terms between two periods. The weighted inclusion index is deﬁned as

PR(kt)(Ch) PRtot(Ch(t))

Iw(Ch(t),Cj(t+1)) = k∈S

(7)

where PRtot(Ch(t)) is the total PageRank of cluster Ch(t). The index assumes values in [0,1] and measures the proportion of cluster Ch(t)’s total PageRank that is carried by terms also appearing in cluster Cj(t+1). It is important to highlight that the weighted inclusion index is asymmetric, so that Iw(Ch(t),Cj(t+1)) ̸= Iw(Cj(t+1),Ch(t)). This asymmetry is meaningful because it reﬂects the extent to which the semantic content of the ﬁrst cluster is retained in the second, while accounting for the relative importance of the shared terms.

The importance index quantiﬁes the aggregate relevance of shared terms by incorporating their centrality in both clusters through a normalised similarity measure, analogous to the association index in Eq. 3, but computed on PageRank values instead of co-occurrence frequencies. The index is deﬁned as

h ,Cj(t+1)) PR(kt)(Ch) · PR(kt+1)(Cj) PRtot(Ch(t)) · PRtot(Cj(t+1))

(t)

Ω(Ch(t),Cj(t+1)) = k∈S(C

(8)

The index takes values in [0,1] and captures the semantic coherence of the evolutionary connection by evaluating the centrality-weighted overlap between clusters. High values indicate that shared terms are not incidental lexical intersections but correspond to structurally central concepts within both thematic conﬁgurations. Conversely, low values suggest that the common vocabulary is peripheral to one or both clusters, signalling limited structural continuity. In contrast to the weighted inclusion index Iw, which is inherently asymmetric and measures the proportion of the source clusters semantic mass retained in the target cluster, the importance index is algebraically symmetric in its two arguments, being deﬁned through a bilinear combination of PageRank centralities normalised by the product of their total masses. Nevertheless, because PageRank scores are computed within period-speciﬁc cluster subgraphs and may exhibit heterogeneous dispersion across periods, the empirical interpretation of this measure can display mild asymmetries. These do not stem from the index’s functional form, but from differences in the underlying centrality

distributions that condition the relative salience of shared terms in each temporal context. Joint consideration of Iw and the importance index distinguishes alternative forms of intertemporal relatedness. When both directional coverage and mutual structural importance are high, the linkage reﬂects strong continuity: a substantial fraction of the source theme is transmitted, and the shared terms remain central in both conﬁgurations. High coverage combined with low importance indicates broad lexical retention without preservation of the semantic core. Conversely, low coverage paired with high importance captures selective transmission, whereby a limited set of shared terms – yet highly central in both clusters – anchors a focused but potentially substantive thematic connection. When both dimensions are low, the relation corresponds to weak continuity, characterised by marginal overlap and peripheral shared content. The integration of both measures in the lineage strength provides a comprehensive assessment of evolutionary connections that accounts for both the extent of overlap and the centrality of shared content

L(Ch(t),Cj(t+1)) = αIw(Ch(t),Cj(t+1)) + (1 − α)Ω(Ch(t),Cj(t+1)) (9)

The parameter α ∈ [0,1] regulates the emphasis placed on directional retention versus mutual structural relevance: values closer to one prioritise coverage of the source theme, values closer to zero prioritise the centrality-weighted coherence of the shared content in both themes, and α = 0.5 provides a balanced compromise. The parameter can be adjusted based on domain characteristics and analytical objectives. For each pair of consecutive periods (t,t + 1), a

lineage strength matrix L(t,t+1) = [Lhj] is built, with a generic element equal to L(Ch(t),Cj(t+1)). The matrix provides a wide overview of all potential evolutionary connections among periods.

#### 3.4 Automatic Lineage Detection and Evolutionary Graph

The ﬁnal component of the approach automatically identiﬁes signiﬁcant evolutionary pathways and produces a thematic evolution graph for visualisation and interpretation. Since not all non-zero lineage strengths represent meaningful evolutionary connections, we apply a dual-thresholding approach that combines absolute and relative criteria to

identify signiﬁcant lineages. For each source cluster Ch(t), we identify target clusters in period t + 1 that satisfy either of the following conditions

L(Ch(t),Cj(t+1)) ≥ θabs (10) where θabs is a minimum lineage strength threshold, and

rankh(Cj(t+1)) ≤ k (11)

where rankh(Cj(t+1)) denotes the rank of Cj(t+1) among all target clusters ordered by lineage strength from Ch(t). The dual criterion ensures that we capture both strongly connected components (exceeding the threshold) and relatively

strong connections (top-k per source), respectively, preventing the loss of important evolutionary paths that may be weaker in absolute terms but represent the primary continuations of source clusters. The evolutionary graph G =

(V,E,w) is directed and acyclic, where V = t∈T C(t) denotes the set of all thematic clusters identiﬁed across the entire temporal horizon, E ⊆ V × V is the set of directed edges (Ch(t),Cj(t+1)) capturing signiﬁcant evolutionary links between clusters in consecutive periods – as determined by the adopted thresholding criteria – and w : E → [0,1] is a weight function assigning to each edge its corresponding lineage strength, such that w (Ch(t),Cj(t+1)) = L(Ch(t),Cj(t+1)).

The graph is temporally stratiﬁed: clusters from period t form a layer t, and edges connect only consecutive layers. Evolutionary patterns are classiﬁed by the in-degree and out-degree of clusters in the resulting graph. A continuation

corresponds to a one-to-one link, with |in(Cj(t+1))| = 1 and |out(Ch(t))| = 1, indicating a stable trajectory across consecutive periods. A split occurs when |out(Ch(t))| > 1, suggesting differentiation or thematic specialisation, while a merge occurs when |in(Cj(t+1))| > 1, indicating thematic consolidation. A cluster is classiﬁed as emergent when |in(Cj(t+1))| = 0, and as disappearing when |out(Ch(t))| = 0, capturing, respectively, the appearance of a conﬁguration without a signiﬁcant predecessor and the absence of a signiﬁcant successor. An evolutionary pathway is deﬁned as a maximal directed sequence through the evolution graph using depth-ﬁrst traversal

,...,Ch(tq)

Pr = ⟨Ch(t1)

⟩ (12) representing a coherent thematic trajectory spanning multiple periods. For each evolutionary pathway Pr = ⟨Ch(t1)

1

q

,...,Ch(tq)

⟩, we compute a set of aggregate indicators summarising its structural and temporal properties. Pathway strength is deﬁned as the product of lineage strengths along consecutive transitions

1

q

q−1

,Ch(ti+1)

L Ch(ti)

Strength(Pr) =

(13)

i

i+1

i=1

capturing the overall continuity of the trajectory. Pathway length corresponds to the number of periods spanned by the sequence, providing a measure of temporal persistence. Finally, cumulative size is deﬁned as

q

|Ch(ti)

| (14)

i

i=1

which aggregates the fuzzy cardinalities of the clusters that compose the pathway and reﬂects its overall substantive weight over time.

The evolutionary graph can be visualised through a thematic evolution plot structured along the temporal dimension. Time periods are arranged on the horizontal axis, while nodes represent thematic clusters identiﬁed in each period. The

size of each node is proportional to the fuzzy cardinality |Ch(t)|, thereby reﬂecting the substantive weight of the cluster. Directed edges connect clusters across consecutive periods, with edge thickness scaled according to the corresponding

lineage strength L, providing an immediate visual indication of the intensity of evolutionary connections. Distinct colours are used to differentiate evolutionary pathways, facilitating the identiﬁcation of coherent thematic trajectories. The vertical positioning of nodes may encode additional structural information, such as centrality, density, or quadrant location in the strategic diagram, thereby integrating longitudinal and cross-sectional perspectives within a uniﬁed visual representation.

The framework is modular, allowing sensitivity analyses with respect to α, threshold parameters, and clustering resolution. From a computational perspective, the dominant costs arise from community detection within each periodspeciﬁc co-occurrence network and from the construction of inter-temporal lineage matrices. Let pt = |K(t)| denote the number of retained terms and mt the number of non-zero edges in the weighted co-occurrence network W(t) for period t. Under standard sparsity conditions (mt ≪ p2t), modularity-based community detection via the Louvain algorithm operates in approximately O(mt) time per iteration, yielding near-linear empirical scaling in the number of edges. PageRank centrality, computed within cluster-induced subgraphs, has complexity O(mthI) for cluster h, where mth denotes its internal edges and I the number of power iterations required for convergence, typically small in practice. Inter-temporal lineage construction requires pairwise comparison of clusters across adjacent periods. If ct = |C(t)| denotes the number of clusters in period t, the lineage matrix between t and t + 1 involves at most O(ctct+1s¯) operations, where s¯ represents the average number of shared terms per cluster pair. Since ct ≪ pt in typical applications, this component remains modest relative to network construction. Overall complexity can therefore be expressed as

ctct+1s¯ (15)

##### O

mt +

t

t

with the edge-based term t mt dominating under realistic sparsity. Importantly, scaling is governed by the number of retained terms and their relational density rather than by the total number of publications, ensuring feasibility for

medium- and large-scale bibliometric collections.

### 4 Empirical Application

To illustrate the analytical potential of the proposed framework, the empirical application considers the complete publication record of the Journal of Informetrics (JOI), one of the principal international outlets in scientometrics and bibliometrics. The journal constitutes an appropriate testbed given its thematic centrality and sustained development over nearly two decades. The dataset was retrieved from the Web of Science Core Collection and covers 2007–2025. After ﬁltering for citable items, the ﬁnal corpus comprises 1,400 articles authored by 2,151 distinct scholars, with a mean of 2.87 co-authors per document and an international co-authorship rate of 30.07%. Average citations per document equal 40.72 over the full window, and reference lists contain 32,929 cited items, indicating a dense intertextual structure. Author-assigned keywords number 3,887 unique terms (1,594 Keywords Plus), reﬂecting substantial semantic heterogeneity and conceptual evolution.

Figure 1 reports annual production into three sub-periods – 2007–2012, 2013–2018, and 2019–2025 – comprising 288, 417, and 695 articles, respectively.

Output increases from 31 articles in 2007 to 110 in 2025, corresponding to an average annual growth rate of 7.29%. Period 2 exceeds Period 1 by 44.8%, and Period 3 is 66.7% larger than Period 2, indicating sustained acceleration. The ﬁrst cutting point (end of 2012) is substantively motivated by the publication of the San Francisco Declaration on Research Assessment, which intensiﬁed debate on responsible evaluation and coincides with a visible rise in publication volume (70 articles in 2012; 93 in 2013). The second cutting point (end of 2018) reﬂects both the consolidation of altmetrics as a distinct research stream and the diffusion of the Leiden Manifesto principles, whose inﬂuence becomes

![image 1](Aria et al_2026_Rethinking Thematic Evolution in Science Mapping A_images/imageFile1.png)

Figure 1: Annual scientiﬁc production of the Journal of Informetrics (2007–2025). Bars are coloured by analytical period; vertical grey lines indicate the two cutting points (end of 2012 and 2018), with period-level document counts shown within each shaded segment.

structurally evident by the close of the decade. The 2019–2025 period thus captures a phase of thematic consolidation and diversiﬁcation.

Co-word analysis was conducted on author-assigned keywords as proxies for conceptual structure. For each period, a co-occurrence matrix was constructed and normalised using the association strength measure deﬁned in Eq. (3), thereby attenuating frequency effects and enabling cross-period comparisons. A minimum threshold of ﬁve occurrences was imposed, retaining up to 250 terms per period. Prior to network construction, 280 pairs of semantically equivalent terms were harmonised (e.g., citation/citations, bibliometrics/bibliometric) to reduce artiﬁcial fragmentation. Community detection was performed using the Louvain algorithm [4], which was selected for its efﬁciency and performance in weighted networks [20]. The resulting partitions provide the basis for fuzzy membership estimation and lineage reconstruction. Inter-period lineage strengths were computed as speciﬁed above, with α = 0.5 to balance directional coverage and reciprocal structural relevance.

#### 4.1 Cross-Sectional Thematic Structure

The cross-sectional analysis identiﬁes 18 thematic clusters in Period 1, 12 in Period 2, and 9 in Period 3. This progressive reduction in the number of clusters is not indicative of thematic contraction; rather, it reﬂects increasing structural consolidation and higher internal density within the co-word networks over time. As the ﬁeld matures, previously fragmented or weakly connected thematic areas tend to coalesce into more cohesive and internally articulated research streams, leading to fewer but structurally stronger communities. The strategic diagrams corresponding to each period are presented in Figures 2–4. These visualisations provide a comparative representation of cluster centrality and density, enabling the identiﬁcation of motor themes, basic and transversal themes, emerging or declining areas, and highly developed but isolated domains within each temporal conﬁguration.

- Period 1 (2007–2012) The thematic conﬁguration of JOI in its founding phase is structured around a diversiﬁed yet methodologically cohesive core centred on bibliometric indicators. The most frequent themes include h-index (112 occurrences), citation analysis (96), citation (93), and bibliometrics (84). In the strategic diagram, h-index is located in the upper-right quadrant (motor themes), combining high centrality and high density, indicating a well-developed, structurally integrated research stream. Citation is located in the lower-right quadrant, where its very high centrality, combined with more moderate density, characterises it as a basic and transversal theme that integrates diverse areas of the domain, not as a self-contained subﬁeld. Related constructs such as scientiﬁc collaboration and peer review also appear among the motor themes, reﬂecting the consolidation of evaluation practices and collaborative dynamics as core components of the journal’s early intellectual proﬁle. Themes including impact factor, journals, and journal evaluation cluster within the right-hand side of the diagram, reinforcing the centrality of research assessment debates in this period. In contrast, clustering and mapping are located in the upper-left quadrant (niche themes), characterised by relatively high internal density but limited centrality, suggesting specialised methodological developments with restricted integrative inﬂuence. Finally, machine learning, digital libraries, and citation counts appear in the lower-left quadrant, combining low density and low centrality, consistent with emerging or weakly institutionalised trajectories that had not yet attained structural prominence within the ﬁeld.


![image 2](Aria et al_2026_Rethinking Thematic Evolution in Science Mapping A_images/imageFile2.png)

Figure 2: Strategic Diagram: Period 1 (2007–2012).

- Period 2 (2013–2018) The intermediate period is characterised by a marked expansion in publication volume (+44.8% relative to Period 1) and a visible reorganisation of the thematic structure. The clusters decrease to 12, while the dominant themes increase substantially in size: bibliometrics (210 occurrences), citation analysis (171), h-index (164), collaboration (113), web of science (101), and impact factor (93). In the strategic diagram, web of science, impact factor, and closely related evaluation constructs are positioned in the upper-right quadrant, indicating well-developed motor themes. By contrast, collaboration, together with bibliometrics and research evaluation, occupies the lower-right quadrant, functioning as highly central but comparatively less dense basic themes that structure the intellectual core of the period. The h-index and citation cluster remains strongly central, consolidating its role as a transversal evaluative framework. A salient development is the emergence of altmetrics (61 occurrences) as a distinct cluster located in the lower-left quadrant, signalling a trajectory that, while thematically innovative and increasingly visible in the literature, had not yet attained structural maturity. The cluster highly cited papers (47) appears in the upper-left quadrant, suggesting a specialised and internally cohesive niche. At the same time, text mining (65) and citation network (46), together with topic modelling and science mapping, indicate a growing methodological diversiﬁcation, though these remain positioned outside the motor core. Finally, academic genealogy and related descriptors form a niche theme characterised by high density but limited centrality, reﬂecting a specialised line of inquiry with restricted integrative inﬂuence.
- Period 3 (2019–2025) The most recent period is characterised by further output expansion (+66.7% relative to Period 2) and a pronounced structural consolidation, with nine clusters that are substantially larger and more internally articulated than in earlier phases. The thematic conﬁguration reﬂects the combined inﬂuence of computational advances and a growing emphasis on systemic and societal dimensions of science. In the strategic diagram, bibliometrics (222 occurrences) and science of science (188) occupy the lower-right quadrant, functioning as highly central but comparatively less dense basic themes. Their position indicates a broad reorientation of the journal’s intellectual core towards macro-level analyses of scientiﬁc systems, while maintaining strong integrative capacity across subdomains. A second major cluster in the basic quadrant is represented by machine learning and artiﬁcial intelligence, signalling the normalisation of computational approaches within the ﬁeld. The upper-right quadrant (motor themes) is dominated by citation impact, scientiﬁc collaboration, and research performance, which exhibit high centrality and density, indicating mature, structurally cohesive research streams. By contrast, altmetrics, citation, and peer review are located near the vertical axis with relatively high density but more moderate centrality, suggesting well-developed yet not fully transversal clusters. Methodological specialisation persists in the upper-left quadrant, where clustering, topic evolution, and bipartite network form niche themes characterised by strong internal cohesion but limited integrative reach. Emerging or context-speciﬁc topics such as research productivity, research funding, and covid-19 appear in the lower-left quadrant, reﬂecting trajectories that are either newly consolidated or episodically driven. Finally, the h-index cluster, though still present (49 occurrences), is positioned closer to the central boundary and shows re-


![image 3](Aria et al_2026_Rethinking Thematic Evolution in Science Mapping A_images/imageFile3.png)

- Figure 3: Strategic Diagram: Period 2 (2013–2018).

duced prominence compared with earlier periods, indicating a gradual rebalancing of attention away from classical indicator-centred research.

![image 4](Aria et al_2026_Rethinking Thematic Evolution in Science Mapping A_images/imageFile4.png)

- Figure 4: Strategic Diagram: Period 3 (2019–2025).


#### 4.2 Thematic Evolution

The evolutionary graph produced by the proposed framework, shown in Figure 5, maps the lineage relations among clusters across the three periods. Lineage strengths are computed using the integrated measure deﬁned in Eq. (9) with α = 0.5, thereby balancing directional coverage and reciprocal structural relevance.

![image 5](Aria et al_2026_Rethinking Thematic Evolution in Science Mapping A_images/imageFile5.png)

Figure 5: Evolutionary graph.

The most robust longitudinal trajectory concerns the bibliometrics cluster, which exhibits the strongest continuation across both transitions. The ﬂow from Period 1 to Period 2 is substantial, and the subsequent transition to Period 3 remains one of the dominant streams in the diagram. This continuity reﬂects the persistent integrative role of bibliometric methodology within the journal’s intellectual structure. A similarly stable pathway characterises citation analysis, which maintains visible connections across periods, preserving its semantic focus on indicator construction and scientometric modelling. The h-index cluster also follows a continuous trajectory, although with progressively reduced magnitude in the ﬁnal period, indicating relative contraction without complete disappearance. Between Period 1 and Period 2, the Sankey structure reveals a marked diversiﬁcation of the highly central citation theme. This latter evolves from a single dominant cluster into multiple successor themes, distributing its weight across h-index, citation analysis, and, to a lesser extent, altmetrics, thereby reﬂecting the specialisation of citation-based inquiry into distinct evaluative and metric-oriented strands. Concurrently, science mapping and scientiﬁc collaboration feed into citation network and collaboration, illustrating a reorganisation of network-analytic approaches. The transition from Period 2 to Period 3 is characterised more by convergence than fragmentation. Notably, collaboration, citation network, and parts of h-index and citation analysis contribute to the emergence of the science of science cluster, which appears in the ﬁnal period as a major basic theme. This pattern indicates an integrative shift towards macro-level analyses of knowledge systems. In parallel, computational strands consolidate: early machine learning and text mining components feed into deep learning, which emerges in Period 3 as a distinct cluster linked to citation-network methodologies. The trajectory of altmetrics is particularly illustrative. Absent as a named cluster in Period 1, it appears in Period 2 and then splits in the subsequent transition, contributing both to a continued altmetrics cluster and to citation impact in Period 3. This dual continuation reﬂects partial institutionalisation alongside integration into broader impact-oriented frameworks.

To assess the robustness of lineage reconstruction to the weighting parameter, the analysis was repeated with moderate perturbations of α (0.3 and 0.7). Observed differences are conﬁned to weaker and peripheral connections. Lower values of α slightly emphasise structurally concentrated transmissions based on highly central shared terms, whereas higher values marginally strengthen broader directional carryover from larger source clusters. These adjustments affect the relative intensity of secondary links but do not modify the principal continuations, splits, or mergers, nor the overall macro-structure of the evolutionary graph. Although only the α = 0.5 conﬁguration is reported for parsimony, the alternative speciﬁcations yield an evolutionary topology that is substantively unchanged. In particular, the dominant longitudinal backbone is preserved across settings: bibliometrics remains the strongest and most stable trajectory over both transitions; h-index exhibits continuity with gradual attenuation; and the convergence of collaboration, citation network, and adjacent evaluative strands into science of science in the ﬁnal period is consistently reconstructed. The consolidation of altmetrics between Period 2 and Period 3 likewise persists under both alternative values. The results, therefore, indicate that the main evolutionary patterns are not artefacts of a speciﬁc parameter choice, while conﬁrming that α meaningfully regulates the balance between directional coverage and structural relevance in marginal transmissions.

#### 4.3 Comparative Assessment with Classical Thematic Evolution

To contextualise the analytical contribution of the proposed framework, its outputs are compared with those generated by SciMAT [11], the most widely adopted implementation of the classical longitudinal approach to thematic evolution. As before, the analysis was performed on the complete publication record of the Journal of Informetrics (2007–2025), partitioned into three identical sub-periods: 2007–2012, 2013–2018, and 2019–2025. SciMAT was conﬁgured using

words (author keywords only) as the unit of analysis. Co-occurrence networks were normalised by association strength; clusters were extracted using single-pass centroid clustering (maximum cluster size set to 100); and the inclusion index was used as both an evolution and an overlap measure. This conﬁguration mirrors the standard operationalisation of the Cobo framework and ensures procedural comparability. The comparison is structured along three dimensions: thematic granularity, cross-sectional cluster composition, and structure of inter-temporal lineage.

Table 1: Number of thematic clusters by period and approach. Period N. of doc. Proposed framework SciMAT

2007–2012 288 18 7 2013–2018 417 12 14 2019–2025 695 9 14

The two approaches yield markedly different cluster counts across all periods. The proposed framework identiﬁes 18, 12, and 9 clusters in Periods 1, 2, and 3, respectively, whereas SciMAT produces 7, 14, and 14 clusters over the same intervals (Table 1). This divergence reﬂects differences in community detection procedures – the proposed framework relies on the Louvain algorithm applied to association-strength-normalised networks, while SciMAT implements single-pass centroid clustering – as well as distinct thresholding strategies. Within the proposed framework, a minimum term frequency of ﬁve occurrences per period and an upper bound of 250 retained terms are imposed to limit sparsity while maintaining semantic coverage. The progressive reduction in cluster count is therefore consistent with increasing network cohesion and consolidation of thematic structure. In contrast, the expansion observed in SciMAT from 7 to 14 clusters appears closely associated with vocabulary growth across periods, leading to ﬁner partitioning of the thematic space. The two approaches thus capture different aspects of structural evolution: consolidation under modularity-based community detection and fragmentation under centroid-based clustering. Figures 6–8 present the three SciMAT strategic diagrams, as exported from the corresponding HTML reports. In each diagram, nodes are positioned according to their centrality (horizontal axis) and density (vertical axis), computed relative to period-speciﬁc means that deﬁne the quadrant boundaries. Node size is proportional to the number of core documents associated with each theme.

|centrality<br><br>density<br><br>CITATION 25<br><br>CITATION-NETWORK 4<br><br>PATENTS 2<br><br>INFORMETRICS 2<br><br>POWER-LAW-MODELS 1<br><br>STOCHASTIC-MODEL 1<br><br>UNIVERSITIES 1|
|---|


- Figure 6: SciMAT strategic diagram:: Period 1 (2007–2012).


- Period 1 (2007–2012) SciMAT identiﬁes a single dominant citation cluster (centrality = 7.47, density = 4.15; 25 core documents) positioned in the basic-themes quadrant, alongside six smaller and comparatively isolated clusters: patents, citation-network, informetrics, power-law-models, stochastic-model, and universities (Figure 6). Three of these (informetrics, power-law-models, stochastic-model) display centrality values approaching zero and occupy peripheral or


niche positions. In the same period, the proposed framework identiﬁes 18 clusters, differentiating among h-index, citation analysis, citation, bibliometrics, and scientiﬁc collaboration as distinct yet structurally interconnected thematic nodes. The allocation of h-index to the motor-themes quadrant and citation to the basic-themes quadrant introduces a clearer articulation between internally cohesive indicator research and transversal citation-based constructs. By comparison, SciMAT’s single citation cluster aggregates several of these components within a uniﬁed theme, resulting in a more compact but less differentiated representation of the period’s evaluative core.

|centrality<br><br>density<br><br>BIBLIOMETRICS 52<br><br>CITATION-DISTRIBUTIONS 7<br><br>IMPACT-FACTOR 5<br><br>COLLABORATION 5<br><br>JOURNAL-IMPACT-FACTOR 4<br><br>DATABASE-ERRORS 3<br><br>IMPACT 2<br><br>SCIENTIFIC-IMPACT 2<br><br>CITATION-COUNTS 2<br><br>PATENT-CITATIONS 1<br><br>SCIENTISTS 1<br><br>CITATION-CONTEXTS 1<br><br>COLLABORATION-NETWORKS 1<br><br>CITATION-PRACTICES 1|
|---|


- Figure 7: SciMAT strategic diagram: Period 2 (2013–2018).


- Period 2 (2013–2018) SciMAT produces 14 clusters, with bibliometrics emerging as the dominant node (centrality = 19.66, density = 4.45; 52 core documents). One structural feature of the partition concerns the placement of impact (centrality = 5.37, density = 25.0) in the motor-themes quadrant despite containing only 2 core documents (Figure 7). This conﬁguration is consistent with the well-known sensitivity of density measures to very small clusters, where limited internal links can produce disproportionately high density values. Several additional clusters – databaseerrors, patent-citations, scientists, citation-contexts, collaboration-networks, and citation-practices – exhibit centrality values below 1.5 and are based on a single core document, suggesting highly localised thematic segments with limited integrative capacity. Notably, SciMAT does not extract altmetrics as a distinct named cluster in this period. In contrast, the proposed framework identiﬁes altmetrics in the lower-left quadrant (61 occurrences), capturing its emergence as a recognisable thematic trajectory prior to full structural consolidation.
- Period 3 (2019–2025) SciMAT again generates 14 clusters, dominated by bibliometrics (centrality = 27.66; 53 core documents) and scientiﬁc-impact (centrality = 11.66; 8 core documents)(Figure 8). The remaining clusters are primarily peripheral, with 10 of the 12 additional themes exhibiting centrality values below 4 and single-document cores, indicating limited structural integration within the network. Two conﬁgurations identiﬁed by the proposed framework in this period – machine learning and artiﬁcial intelligence and science of science – do not emerge as consolidated structures in the SciMAT partition. Their absence as distinct clusters is plausibly related to the dispersion of their constituent vocabulary across multiple SciMAT themes, without sufﬁcient centroid proximity to produce a uniﬁed cluster under single-pass centroid clustering.


Inter-temporal lineage The overlapping map (Figure 9) and the evolution map (Figure 10) summarise SciMAT’s reconstruction of longitudinal dynamics. The overlapping map reports the number of shared terms between adjacent periods: 73 terms overlap between Periods 1 and 2 (Jaccard-type index = 0.70), and 98 terms between Periods 2 and 3 (index = 0.66), suggesting substantial vocabulary continuity over time. The evolution map, based on core documents’ inclusion indices, displays a pronounced hub-and-spoke conﬁguration centred on bibliometrics.

From Period 1 to 2, the dominant citation cluster distributes lineage across bibliometrics (3.57), citationdistributions (4.29), impact-factor (2.86), collaboration (3.33), impact (2.50), and journal-impact-factor (2.50). To-

|centrality<br><br>density<br><br>BIBLIOMETRICS 53<br><br>SCIENTIFIC-IMPACT 8<br><br>COLLABORATION 3<br><br>JOURNAL-RANKING 2<br><br>MANUSCRIPTS 2<br><br>INEQUALITY 2<br><br>ACADEMIC-CAREERS 1<br><br>SIMILARITY-MEASURES 1<br><br>SCIENTIFIC-JOURNALS 1<br><br>DATA-CITATION 1<br><br>SCIENTIFIC-CAREERS 1<br><br>INSTITUTIONS 1<br><br>PATENTS 1<br><br>COMPLEX-NETWORKS 1|
|---|


Figure 8: SciMAT strategic diagram: Period 3 (2019–2025).

gether, informetrics and universities connect to bibliometrics with inclusion weights of 6.67 and 10.00, respectively. These values primarily reﬂect lexical inclusion within core-document sets, as universities contributes exclusively to bibliometrics despite constituting a peripheral, single-document cluster. From Period 2 to 3, bibliometrics absorbs most of the lineage mass: impact → bibliometrics (5.00), impact-factor → bibliometrics (2.86), collaboration → bibliometrics (3.33), and scientiﬁc-impact → bibliometrics (3.33). Only three connections extend to Period 2 clusters beyond bibliometrics: impact-factor → journal-ranking (3.33), collaboration → collaboration (2.50), and scientiﬁcimpact → scientiﬁc-impact (3.33). The resulting structure is strongly centralised around a single dominant hub.

81

51

31

56

73 (0.7)

98 (0.66)

104

154

149

- Figure 9: SciMAT overlapping map. Circles represent the three sub-periods (2007–2012: 104 terms; 2013–2018: 154 terms; 2019–2025: 149 terms). Numbers on arrows denote shared terms between adjacent periods; values in parentheses indicate the corresponding normalised overlap index.


By comparison, the proposed framework reconstructs a more articulated evolutionary conﬁguration. The lineage strength measure, integrating PageRank-weighted term inclusion and mutual structural relevance, captures both strong continuations and selective transmissions across periods. The differentiation of the citation cluster from Period 1 into h-index, citation analysis, and altmetrics in Period 2 emerges through distinct lineage strengths reﬂecting differential coverage and structural salience. Similarly, the convergence of collaboration, citation network, and h-index in Period 2 towards the science of science cluster in Period 3 is reconstructed as the merger of structurally related streams. This pattern does not appear in the SciMAT evolution map, which is driven by inclusion relations over core-document sets and therefore tends to privilege dominant lexical intersections. The gradual contraction of h-index across periods, observable through declining fuzzy cardinality in the proposed framework, is likewise not separately visible in SciMAT’s output, where it is absorbed within the bibliometrics trajectory at successive transitions.

The results shown here indicate that the differences between the two strategies are not merely quantitative variations in cluster counts or lineage weights, but stem from distinct modelling assumptions about what constitutes thematic continuity. Whereas inclusion-based methods reconstruct evolution through lexical intersection among core-document sets,

CITATION

BIBLIOMETRICS

BIBLIOMETRICS

CITATION-DISTRIBUTIONS

SCIENTIFIC-IMPACT

PATENTS

IMPACT-FACTOR

COLLABORATION

COLLABORATION

JOURNAL-RANKING

CITATION-NETWORK

IMPACT

MANUSCRIPTS

JOURNAL-IMPACT-FACTOR

INEQUALITY

INFORMETRICS

SCIENTIFIC-IMPACT

ACADEMIC-CAREERS

CITATION-COUNTS

SIMILARITY-MEASURES

POWER-LAW-MODELS

DATABASE-ERRORS

SCIENTIFIC-JOURNALS

PATENT-CITATIONS

DATA-CITATION

STOCHASTIC-MODEL

SCIENTISTS

SCIENTIFIC-CAREERS

CITATION-CONTEXTS

INSTITUTIONS

UNIVERSITIES

COLLABORATION-NETWORKS

PATENTS

CITATION-PRACTICES

COMPLEX-NETWORKS

- Figure 10: SciMAT evolution map based on the inclusion index (core-documents count). Node area is proportional to the number of core documents; edge thickness reﬂects inclusion weight. Strong links (solid) correspond to abovethreshold inclusion; weak links (dashed) are below-threshold connections retained by the algorithm.


the proposed framework embeds lineage within the weighted relational structure of clusters and incorporates graded document afﬁliation into the linkage mechanism. The consequent divergence in evolutionary topology – centralised hub formation vs articulated split-and-merge patterns – reveals how alternative operationalisations of continuity yield substantively different representations of knowledge dynamics. These ﬁndings encourage broader reﬂection on the conceptual foundations of longitudinal science mapping and the implications of structurally integrated modelling for the interpretation of thematic change.

### 5 Discussion

The present study advances a structural reformulation of thematic evolution within science mapping by resolving a methodological inconsistency embedded in classical longitudinal implementations. In established approaches, themes are detected through relational clustering within co-occurrence networks, yet their evolution is reconstructed through set-theoretic overlap among core documents or keyword lists. This dual logic implicitly shifts the ontological status of themes from network-embedded relational conﬁgurations to bounded lexical sets when moving from cross-sectional to

longitudinal analysis. The framework proposed here restores coherence by embedding lineage reconstruction within the same weighted relational architecture that underpins cross-sectional detection.

Conceptually, this integration reframes thematic continuity as a structurally mediated process. Continuity is no longer inferred solely from shared vocabulary, but from the transformation of weighted conﬁgurations in which term salience and document afﬁliation are jointly considered. By incorporating PageRank-weighted term importance and fuzzy document membership, the model captures graded and directional continuity, distinguishing between broad lexical coverage and mutual structural relevance. This distinction enables the analysis of thematic change by examining how intellectual structures are differentially retained, reweighted, or reconﬁgured across periods. The resulting representation treats thematic change as a dynamic reconﬁguration of relational structures rather than as persistence of surface lexical overlap. Methodologically, three elements constitute the framework’s core innovation. First, fuzzy thematic afﬁliation replaces exclusive publication assignment with graded membership. Scientiﬁc contributions often span multiple thematic strands, and binary partitioning may obscure this multiplicity. The adoption of fuzzy membership provides a more faithful representation of thematic embeddedness and permits the estimation of cluster size via fuzzy cardinality, capturing both the intensity and the dispersion of participation. Second, lineage strength is decomposed into complementary components – weighted inclusion and structural importance – thereby separating directional coverage from reciprocal salience. This decomposition enhances interpretability and renders explicit the modelling assumptions underlying continuity measurement. Third, the parameterisation of lineage weighting through α introduces analytical transparency. Rather than embedding weighting choices implicitly within an index, the framework exposes them as tunable components, facilitating methodological scrutiny and replication.

The comparative assessment illustrates that alternative operationalisations of continuity yield substantively different evolutionary topologies. Inclusion-based methods privilege dominant lexical intersections and tend to generate centralised hub conﬁgurations, in which major themes absorb lineage mass across transitions. By contrast, a structurally integrated speciﬁcation reveals articulated split-and-merge patterns, as well as gradual differentiation or attenuation of thematic strands. These differences are not merely quantitative, reﬂecting distinct epistemic commitments about what constitutes thematic persistence. Beyond its technical modiﬁcations, the proposed framework offers a more explicit articulation of the conceptual premises that inform longitudinal science mapping. At the same time, the scope of the contribution is shaped by several methodological contingencies. The resulting conﬁgurations remain dependent on clustering decisions, as partition boundaries are inherently resolution-sensitive and alternative community detection algorithms may yield different yet equally defensible structures. The importance index, in turn, relies on PageRank as a proxy for semantic salience within clusters; although this measure captures recursive centrality and attenuates degree bias, other centrality speciﬁcations could foreground different structural properties. Network topology is also inﬂuenced by preprocessing choices, such as frequency thresholds and lexical harmonisation, which, despite being explicitly documented, introduce degrees of analytical discretion that warrant transparent reporting and, where possible, sensitivity assessment. Finally, the reliance on discrete temporal segmentation – while consistent with established strategic mapping practice – necessarily imposes boundaries on processes of thematic change that unfold more continuously in practice. These considerations do not undermine the framework’s contribution but clarify its domain of validity. The proposed integration enhances structural coherence between cross-sectional and longitudinal modelling, increases interpretive transparency, and reduces artefacts arising from purely lexical lineage reconstruction. At the same time, it remains embedded within the broader assumptions of network-based science mapping and shares their interpretative and methodological constraints, intrinsic to clustering and keyword-based analysis.

### 6 Conclusions and Final Remarks

This study advances a structurally integrated framework for modelling thematic evolution in science mapping. The point of departure is a methodological asymmetry in classical longitudinal approaches, which combine relational clustering for cross-sectional detection with set-theoretic criteria for inter-temporal linkage. By situating both detection and lineage reconstruction within a uniﬁed weighted network architecture and by introducing graded document afﬁliation, the framework restores coherence between theme identiﬁcation and the modelling of temporal transformation. The central contribution is to redeﬁne thematic continuity as a structurally grounded process: evolution is reconstructed through weighted relational conﬁgurations that jointly incorporate term salience and document-level participation. In this way, the framework preserves the interpretability of strategic diagrams – valued for their capacity to position themes along centrality and density dimensions – while extending their analytical reach to longitudinal dynamics. Rather than tracking vocabulary alone, the model captures how intellectual structures are progressively reconﬁgured, consolidated, or redistributed across periods.

Beyond the empirical application presented here, the framework reinforces the methodological foundations of longitudinal science mapping by making explicit the assumptions underlying lineage construction and by formalising the balance between directional coverage and structural relevance. Such explicit parameterisation enhances analytical

transparency, facilitates replication, and enables systematic comparison across studies without sacriﬁcing interpretability. In doing so, the study situates science mapping within a broader network-analytic perspective, where consistency between structural detection and dynamic modelling is regarded as essential for coherent temporal analysis.

More generally, the framework prompts reconsideration of the epistemic status of themes in bibliometric research. When themes are understood as evolving relational conﬁgurations rather than as bounded lexical aggregates, longitudinal analysis shifts from tracking stable labels to modelling structural transformation. This reorientation contributes to the conceptual consolidation of thematic analysis and positions science mapping as a dynamically consistent approach within the broader ﬁeld of knowledge evolution studies. Further progress in modelling thematic change is likely to depend less on incremental reﬁnements of similarity indices and more on the development of structurally coherent dynamic models capable of accommodating the complexity of intellectual transformation. In this perspective, the present framework offers a principled basis for subsequent theoretical reﬁnement and empirical deployment. Promising directions include the integration of thematic networks with additional relational layers – such as citation, authorship, or institutional ties – so as to capture multidimensional evolutionary processes within multiplex structures; the development of adaptive weighting strategies for lineage strength, in which the balance between inclusion and structural relevance is empirically calibrated; and the exploration of overlapping or rolling temporal windows to approximate continuous thematic drift while preserving the interpretability of strategic mapping.

### References

- [1] M. Aria and C. Cuccurullo. bibliometrix: An R-tool for comprehensive science mapping analysis. J. Informetr., 11(4):959–975, 2017. doi:10.1016/j.joi.2017.08.007.
- [2] M. Aria, C. Cuccurullo, L. D’Aniello, M. Misuraca, and M. Spano. Comparative science mapping: A novel conceptual structure analysis with metadata. Scientometrics, 129:7055–7081, 2024. doi:10.1007/s11192-02405161-6.
- [3] D. M. Blei and J. D. Lafferty. Dynamic topic models. In ICML ’06: Proceedings of the 23rd international conference on Machine learning, pages 113–120. ACM, 2006. doi:10.1145/1143844.1143859.
- [4] V. D. Blondel, J.-L. Guillaume, R. Lambiotte, and E. Lefebvre. Fast unfolding of communities in large networks. J. Stat. Mech.: Theory Exp., 2008(10):P10008, 2008.
- [5] K. Börner. Atlas of Science: Visualizing What We Know. MIT Press, Cambridge, MA, 2010.
- [6] S. Brin and L. Page. The anatomy of a large-scale hypertextual web search engine. Comput. Netw. ISDN Syst., 30(1):107–117, 1998. doi:10.1016/S0169-7552(98)00110-X.
- [7] M. Callon. Techno-economic networks and irreversibility. Sociol. Rev., 38(1_suppl):132–161, 1990. doi:10.1111/j.1467-954X.1990.tb03351.x.
- [8] M. Callon, J.-P. Courtial, W. A. Turner, and S. Bauin. From translations to problematic networks: An introduction to co-word analysis. Soc. Sci. Inf., 22(2):191–235, 1983. doi:10.1177/053901883022002003.
- [9] M. Callon, J. Law, and A. Rip. Mapping the dynamics of science and technology: Sociology of science in the real world. Macmillan, London, 1986.
- [10] M. J. Cobo, A. G. López-Herrera, E. Herrera-Viedma, and F. Herrera. An approach for detecting, quantifying, and visualizing the evolution of a research ﬁeld: A practical application to the fuzzy sets theory ﬁeld. J. Informetr., 5(1):146–166, 2011. doi:10.1016/j.joi.2010.10.002.
- [11] M. J. Cobo, A. G. López-Herrera, E. Herrera-Viedma, and F. Herrera. SciMAT: A new science mapping analysis software tool. J. Am. Soc. Inf. Sci. Technol., 63(8):1609–1630, 2012. doi:10.1002/asi.22688.
- [12] W. L. Hamilton, J. Leskovec, and D. Jurafsky. Diachronic word embeddings reveal statistical laws of semantic change. In Proceedings of the 54th Annual Meeting of the Association for Computational Linguistics (ACL), pages 1489–1501. ACL, 2016. doi:10.18653/v1/P16-1141.
- [13] J. Law and J. Whittaker. Mapping acidiﬁcation research: A test of the co-word method. Scientometrics, 23(3): 417–461, 1992. doi:10.1007/BF02029807.
- [14] E. C. M. Noyons, H. F. Moed, and A. F. J. van Raan. Integrating research performance analysis and science mapping. Scientometrics, 46(3):591–604, 1999. doi:10.1007/BF02459614.
- [15] H. P. F. Peters and A. F. J. van Raan. Co-word-based science maps of chemical engineering. Part II: Representations by combined clustering and multidimensional scaling. Res. Policy, 22(1):47–71, 1993. doi:10.1016/00487333(93)90032-D.
- [16] G. Rossetti and R. Cazabet. Community discovery in dynamic networks: A survey. ACM Comput. Surv., 51(2): 35, 2018. doi:10.1145/3172867.


- [17] N. J. van Eck and L. Waltman. How to normalize cooccurrence data? An analysis of some well-known similarity measures. J. Am. Soc. Inf. Sci. Technol., 60(8):1635–1651, 2009. doi:10.1002/asi.21075.
- [18] A. F. J. van Raan. Measuring science: Basic principles and application of advanced bibliometrics. In W. Glänzel, H. F. Moed, U. Schmoch, and M. Thelwall, editors, Springer Handbook of Science and Technology Indicators, pages 237–280. Springer, Cham, 2019. doi:10.1007/978-3-030-02511-3_9.
- [19] L. Waltman and N. J. van Eck. A systematic empirical comparison of different approaches for normalizing citation impact indicators. J. Informetr., 7(4):833–849, 2013. doi:10.1016/j.joi.2013.08.002.
- [20] Z. Yang, R. Algesheimer, and C. J. Tessone. A comparative analysis of community detection algorithms on artiﬁcial networks. Sci. Rep., 6(1):30750, 2016. doi:10.1038/srep30750.
- [21] P. Zhang, T. Wang, and J. Yan. Pagerank centrality and algorithms for weighted, directed networks. Physica A Stat. Mech. Appl., 586:126438, 2022. doi:10.1016/j.physa.2021.126438.


