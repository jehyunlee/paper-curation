# arXiv:2503.23285v1[cs.DL]30 Mar 2025

### Mapping the changing structure of science through diachronic periodical embeddings

Zhuoqi Lyu 1 and Qing Ke 1, ∗ 1Department of Data Science, College of Computing, City University of Hong Kong, Hong Kong, China

(Dated: April 1, 2025)

#### Abstract

Understanding the changing structure of science over time is essential to elucidating how science evolves. We develop diachronic embeddings of scholarly periodicals to quantify “semantic changes” of periodicals across decades, allowing us to track the evolution of research topics and identify rapidly developing fields. By mapping periodicals within a physical-life-health triangle, we reveal an evolving interdisciplinary science landscape, finding an overall trend toward specialization for most periodicals but increasing interdisciplinarity for bioscience periodicals. Analyzing a periodical’s trajectory within this triangle over time allows us to visualize how its research focus shifts. Furthermore, by monitoring the formation of local clusters of periodicals, we can identify emerging research topics such as AIDS research and nanotechnology in the 1980s. Our work offers novel quantification in the science of science and provides a quantitative lens to examine the evolution of science, which may facilitate future investigations into the emergence and development of research fields.

Keywords: science of science | evolution of science | map of science | word2vec

∗ Correspondence to q.ke@cityu.edu.hk

###### I. INTRODUCTION

Since the establishment of the first scholarly journal, Philosophical Transactions of the Royal Society, in 1665 [1], journals and conference proceedings have served as the primary outlet for science publishing, crucial for the dissemination of research findings within the scientific community [2, 3]. These periodicals are also instrumental in shaping scientific norms; publishing in them signals affiliations with and establishes standings within a particular scientific community. Additionally, they play a major role in announcing the priority of scientific discoveries, which may influence eligibility for awards and recognition.

As scholarly periodicals tend to publish thematically coherent sets of papers, they are widely considered as a viable representation of knowledge components and consequently used in numerous inquiries into the scientific enterprise. These include identifying recombinant innovation in science [4, 5], categorizing biomedical research [6], and assessing the interdisciplinary integration of emerging fields [7], among others [8, 9]. Notably, periodicals have long been used as instruments to probe the structure of science [10–12], by representing them as crisp discipline vectors, sparse vectors that capture (co-)citation relationships [6, 13–15] or online activities [16], as well as dense vectors based on representation learning methods [17]. These extensive efforts have yielded several global maps of science that are useful for understanding knowledge flow between fields and supporting decision-making processes such as portfolio analysis and resource allocation.

However, these maps are static and fail to capture the dynamic nature of both the evolution of science and the development of scholarly communication. Specifically, science is continually evolving, with new fields and research topics emerging sporadically, which can reshape the landscape of science publishing. For example, the recognition of AIDS as a new disease in the 1980s led to the creation of several journals to accommodate the unmet need for platforms for publishing AIDS-related research. In addition, the rise of interdisciplinary science in recent decades has likely brought certain fields closer to each other [18]. In terms of scholarly communication, technological advancements have drastically transformed science publishing: It is now common for researchers to read and search scientific literature online; many periodicals have transitioned from the printed to

the online medium, which largely eliminates space constraints and allows for more extensive referencing and publishing. All these developments cannot be captured by static, retrospective vectors of periodicals, highlighting the need for dynamic, time-varying representations.

Here, we develop diachronic embeddings of periodicals to examine how these embeddings evolve over time, building on our previous methodology [17]. Previous studies related to ours have studied relationships between disciplines over time using vector representations of disciplines [19], without focusing on the more fine-grained level of periodicals. We demonstrate that, by using diachronic embeddings, we can quantify the magnitude of “semantic change” for each periodical based on its nearest neighbors at different times, chart the direction of semantic changes, and track the evolving frontier of interdisciplinary periodicals. Moreover, by tracking the formation of local clusters of periodicals, we identify numerous emerging themes, such as AIDS research and biomaterials. Overall, our work sheds light on the changing structure of science at the periodical level and provides insights into the evolution of science.

- II. RESULTS


A. Constructing diachronic periodical embeddings

To build diachronic embeddings of periodicals (see Fig. S2 for a schematic illustration), we begin by constructing a citation network for each decade t starting from the 1950s. In the network, nodes represent papers published during that decade and directed links point from citing papers to cited ones. For each network, we perform random walks on it to generate paper citation trails and then map each paper in a citation trail to the periodical in which it was published, resulting in periodical level trails (see Methods). By generating a large number of citation trails, we create an effective exploration of the citation network. Treating each trail as a “sentence” and each periodical as a “word”, we apply word2vec [20] to the periodical trail corpus to learn vector representations of periodicals, denoted as vit for periodical i. Similar to word embeddings, periodicals with similar “contextual” periodicals in citation trails are closer in the vector space, reflecting their semantic similarity. For example, in the 2010s, the periodicals most similar to

Nature are Science, Nature Communication, and Science Advances, highlighting their multidisciplinarity feature. However, back in the 1950s, Nature was largely a biology journal and was most similar to Journal of Molecular Biology, Biochimica et Biophysica Acta, and Naturwissenschaften (see Table S5 for the top neighbors of Nature over time).

We validate our diachronic periodical embeddings using case periodicals. First, we focus on multidisciplinary journals, as they publish papers in multiple disciplines and disciplinary compositions of published papers over time should correlate with their similarities to disciplines, given that citation exchanges tend to occur within disciplines. For example, by re-assigning each Nature paper to the field corresponding to the majority of its references’ fields, we observe a rapid increase in the publication volume of papers in Earth and Planetary Sciences (a Scopus field label) during the 1970s–1990s (Fig. 1A). This makes Nature more likely to occupy similar positions in citation trails as geoscience periodicals and thus more similar to the field. Indeed, when we measure the closeness between Nature and the geoscience field by calculating the average cosine similarity to all periodicals in the field relative to the average across all periodicals, we find that Nature becomes closer to geoscience during the same period (Fig. 1B). In general, there is a positive correlation between publication volume in a field and relative cosine similarity (coefficient of determination R2 = 0.526; Fig. 1C), suggesting that our diachronic embeddings can be used to quantify how the “semantics” of Nature change over time. Repeating this analysis for two other multidisciplinary journals, Science and PNAS, we find a similar correspondence (Figs. S10–S11), further supporting the validity of our diachronic periodical embeddings.

Second, in a similar vein, we examine Cognitive Science, a flagship journal of the field of cognitive science. This field was established in the 1950s with the vision that fruitful cross-fertilization among six diverse disciplines—psychology, linguistics, artificial intelligence, anthropology, philosophy, and neuroscience—would advance the science of mind [7]. However, both commentaries and empirical analyses have noted that over the course of its development, cognitive science has lost its intended diversity and instead been characterized by an overrepresentation of psychology. Our analysis using diachronic embeddings supports this observation; the proportion of psychology papers published in Cognitive Science has increased significantly, and the journal’s closeness to psychology has also increased (Fig. S12).

A Earth

###### C

2.0

R2 = 0.526

Percentageofpapers

20

Phys

Relativesimilarity

1.5

15

1.0

10

0.5

5

0.0

0 1 2 3 Number of papers (log)

B Earth

2.0

Phys

Relativesimilarity

1.8

Life Science

1950s 1960s 1970s 1980s

1990s 2000s 2010s

1.6

Health Science

Physical Science

1.4

Social Science

1.2

1950s 1960s 1970s 1980s 1990s 2000s 2010s Decade

- FIG. 1. Validating diachronic embeddings using Nature. (A) Percentage of papers in Earth and Planetary Sciences and Physics published in Nature by decade. Papers in the 2010s refer to those published in 2010–2021 for simplicity. (B) Relative similarity between Nature and the two focused disciplines. Relative similarity is defined as the average cosine similarity between Nature and all periodicals belonging to that discipline, divided by the average cosine similarity between Nature and all periodicals. (C) The correspondence between publication volume and relative similarity. Color represents discipline and shape marks decade.


B. Quantifying semantic change of periodicals

Our validation exercises above indicate that there are semantic changes for certain periodicals, raising the questions of how to quantify the magnitude of these changes and which periodicals have undergone the most significant transformations. Inspired by computational linguistics studies on semantic changes of words [21], we quantify a periodical’s semantic changes over time by looking at its k nearest neighbors based on its diachronic embeddings (Fig. 2A). Specifically, let Nit1,t2 = Nit1 ∪ Nit2 represent the union of periodical i’s k-nn at t1 and t2 (with k set to 10). We create a vector st1 for t1, where each entry is the cosine similarity between vit1 and vtn1 (n ∈ Nit1,t2), and similarly create another vector st2 for t2. We then measure the semantic change of i from t1 to t2, denoted as dit1,t2, as the cosine distance between st1 and st2, i.e., dit1,t2 = 1 − ||sts1t||·||1·sts2t2||. A periodical tends to have a large d if there is a low overlap between Nit1 and Nit2.

By calculating d between two consecutive decades, we find that across time, periodicals tend to experience limited semantic changes, with the median and the 95th per-

centile of d around 0.01 and 0.04, respectively (Fig. S13). For example, the semantics of Quarterly Journal of Economics, Annals of Mathematics, and American Sociological Review have remained almost unchanged over the past seven decades (Figs. 2H–J). On the other hand, a few periodicals have undergone drastic semantic shifts. Notably, the Proceedings of the Royal Society B: Biological Science (PRSB) experienced a semantic drift in the 1980s, during which it moved closer to computer vision journals like International Journal of Computer Vision and Journal of Machine Vision and Applications (Fig. 2A). This was due to the publication of a few highly influential computer vision papers [22–27], which attracted volumes of citations from this field. Subsequently, PRSB returned to a focus on biology, and its semantic changes decreased over the following decades (Fig. 2B). Similarly, its sister journal, Philosophical Transactions of the Royal Society B, experienced a comparable semantic journey (Fig. 2C), largely due to studies published in the 1980s at the intersection of neural systems and computations [28–30], which generated numerous citations from topics outside biology, particularly in computer vision, neural networks, and cognitive science. Likewise, Yale Journal of Biology and Medicine exhibited significant semantic changes during the 1980s–2000s (Fig. 2D). Upon examining its neighbors over time, we find that it had a rapid shift in research interests from general medicine to digestive diseases in the 1990s, which was later restored in the 2000s. Finally, Figs. 2E–G highlight three periodicals—Bulletin of Mathematical Biology, Annual Meeting of the Association for Computational Linguistics, and Journal of the Acoustical Society of America—whose semantic trajectories have steadily decreased, indicating a stabilization of their neighbors over time.

We further identify periodicals that have undergone the largest topical shifts by summing their semantic changes dt1,t2 over time. Fig. S16 presents the distributions of this total change for periodicals grouped by the decade of their establishment, with several periodicals highlighted within these distributions. We observe that for periodicals established before the 1960s, the distribution of total semantic changes is much flatter compared to those established in later decades. Moreover, there is a graduate emergence of a mode value for total semantic changes, suggesting a potential ubiquity of semantic change over time.

Examining semantic changes at the field level, Fig. S17 shows the distributions of total semantic changes for periodicals across 27 fields. The top three fields experiencing

|A|
|---|


- FIG. 2. Quantifying semantic change, dt1,t2, of a periodical. (A) Two-dimensional visualization of PRSB’s semantic change based on its diachronic embeddings. During the 1970s–1990s, it shifted from a cluster of biology periodicals to computer vision to ecology. (B–J) dt1,t2 for individual periodicals over time. Numbers in parentheses in the titles are total dt1,t2 over time. Figs. S14–S15 provide more examples.


the most shifts are Multidisciplinary, Chemistry, and Biochemistry. Multidisciplinary periodicals are designed to publish contributions spanning various disciplines. Chemistry, often referred to as “the central science”, plays a pivotal role in linking upstream physical sciences with downstream fields like life sciences and medicine [17, 31, 32]. This unique position at the intersection of multiple scientific domains underscores its greater potential for semantic displacement. Biochemistry is also recognized as a highly interdisciplinary field [13]. In contrast, specialized fields such as management, accounting, dentistry, and health professions tend to be more stable.

C. Identifying direction of semantic change

Beyond quantifying the magnitude of semantic changes, we are also interested in understanding the direction of semantic displacement. In doing this, we define several disciplinary poles in the vector space and measure a periodical’s closeness to each pole. Specifically, we focus on the three broad research areas designated by Scopus: physical science, life science, and health science, and identify the pole for each area by averaging the vectors of all periodicals in that area. Formally, let Pt represent the set of vectors for physical science periodicals in decade t. The physical science pole is the centroid of this set: vtP = |P1t| ∑vt∈Pt vt. We measure the closeness between a periodical i and the pole as the cosine similarity between vit and vtP, denoted as lit,P. Similarly, we identify the life and health science poles, vtL and vtH, and calculate periodical i’s closeness to the two areas, lit,L and lit,H. We then normalize the proximity to the three areas, (lit,P, lit,L, lit,H), to form a probability distribution, allowing us to place all periodicals within the physicallife-health triangle.

Fig. 3A presents the positions of all periodicals within the triangle for the 2010s, with colors representing their Scopus labels, to facilitate comparisons with this traditional journal classification system (see Fig. S22 for other decades). In this ternary plot, a point’s position indicates its relative proximity to the three research areas. For example, a periodical closer to the health science (left) corner can be characterized as a health science journal. By construction, periodicals belonging to one area are located nearer to the corresponding corner. Although social science periodicals are not used in forming the triangle, they can still be positioned within it, and they tend to be closer to the physical and health sciences than to the life science.

Fig. 3A reveals blurred and indistinct regions within the triangle where periodicals with different area labels intermingle, and for some periodicals, there is a discrepancy between the manually curated Scopus discipline labels and our data-driven discipline labels based on embeddings. This exposes the nuanced structure in the disciplinary organization and underscores the limitations of categorical classification approaches, emphasizing the need to uncover interdisciplinary periodicals. To address this, we apply k-means clustering to group periodicals into four clusters based on their ternary coordinates (Fig. 3B) and compare these clusters with the four broad areas in the Scopus classification system

![image 1](Lyu and Ke_2025_Mapping the changing structure of science through diachronic periodical embeddings_images/imageFile1.png)

- FIG. 3. Mapping periodicals within the physical-life-health triangle. (A) A ternary plot showing the distribution of all periodicals with respect to three conceptional axes: physical science, life Science, and health science, in the 2010s. Color denotes research area assigned by Scopus.


- (B) The same ternary plot but with periodicals colored by cluster labels generated by k-means based on periodicals’ ternary coordinates. The label of a cluster is the most common Scopus area label. (C) The same ternary plot but with periodicals colored by the level of disagreement between k-means clustering and Scopus labels. Periodicals with larger disagreement are colored darker. Highlighted are 8 misclassified periodicals, whose central colors indicate their clustering labels and edge colors represent research areas assigned by Scopus. (D-J) Interpolated heatmaps of disagreement between k-means clustering results and Scopus labels for each decade. The interpolation is based on inverse distance weighting (IDW). Numbers in titles are average similarity of all periodicals.


using an element-centric measurement, which quantifies similarity between two clusterings at the individual element level [33]. Fig. 3C displays the same map with periodicals colored by similarity, where periodicals with lower similarity are shown in darker shades to highlight disagreements between the two clusterings. We observe that disagreements are indeed located at the intersections of disciplines. Through manual inspection, we find that misclassified journals often exhibit a higher level of interdisciplinarity, including International Journal of Immunogenetics, Journal of Molecular Modeling, and Journal of Mathematics and Music. To pinpoint regions with the highest interdisciplinarity, we use an inverse distance weighting approach [34] to generate an interpolated heatmap of similarity, shown in Fig. 3J. This heatmap reveals that the region closer to the life science corner exhibits a much higher level of interdisciplinarity than those closer to the physical and health science corners.

To further characterize the shift in interdisciplinarity over time, we generate heatmaps

for other decades (Figs. 3D–I). We observe that overall the level of disagreement has decreased over time, indicating a trend towards disciplinary cohesion. For the physical, health, and social science fields, disciplinary organization has become more pronounced, whereas life science periodicals are increasingly blending with those from other disciplines, calling for the need for adopting data-driven discipline classification systems. Correspondingly, interdisciplinary hotspots have shifted from the center of the triangle to the intersections between life science and both physical and health sciences.

Furthermore, by tracking the positions of a periodical within the triangle over time, we can obtain a trajectory that reflects how its research topics evolve temporally. Fig. 4 presents the trajectories of 15 periodicals. Notably, Science exhibits significant semantic displacement toward physical science particularly during the 1990s and 2000s (Fig. 4A), which is consistent with a substantial increase in the number of papers published in Physics and Astronomy. In contrast, Nature has largely maintained its position over the past 70 years, although it has gradually moved toward the center of the triangle (Fig. 4B). This aligns with previous research indicating that Nature has garnered citations from an increasingly diverse range of disciplines [18]. Meanwhile, PNAS experienced a rapid shift away from physical science, gravitating toward life science in the 1950s–1980s (Fig. 4C).

Life science periodicals exhibit a variety of evolutionary trajectories. Over the past 40 years, Cell has shifted away from physical science and gradually moved closer to health science (Fig. 4E). Meanwhile, Biophysical Journal has experienced fluctuations along the physical science axis, ultimately drawing nearer to physical science (Fig. 4F), which reflects the increasing reliance of biology and medicine on physical science [35]. The Journal of Molecular Biology showed a great shift toward life science until the 2000s (Fig. 4G), which seems to be in accordance with the view that the molecular paradigm ceased to be a reliable guide for biology as it was throughout the 20th century [36].

Turning to health science, Lancet, New England Journal of Medicine, and JAMA share a similar path of gradually becoming less health science but more life science (Figs. 4I– K). This trend diverges from the overall trajectory of health science periodicals and may suggest a transformative role played by these prestige periodicals in the convergence of biology and medicine, driven by an increasing dependence of medicine on upstream scientific discoveries from life science, as well as advancements in technologies and instruments for diagnosis and therapeutics [37].

A Science

B Nature

###### C PNAS

D Multi. AVG

0.20

0.18

0.16

0.20

0.50

0.24

0.25

0.60

0.24

0.64

0.55

0.25

0.32

0.45

0.56

0.30

0.54

0.30

0.50

0.30

0.40

0.48

0.40

0.35

0.48

0.36

0.45

0.35 0.25 0.30 0.35 0.40

0.40

0.35

0.24 0.30 0.36

0.16 0.24 0.32 0.40

0.30 0.35 0.40 0.45

E Cell

F Biophys. J.

G J. Mol. Biol.

H Life AVG

0.20

0.56 0.32

0.25

0.48 0.28

0.55

0.25

0.50

0.30

0.52

0.30

0.50

0.46

0.36

0.30

0.45

0.35

0.48

0.32

0.44

0.45

0.40

0.35

0.40

0.40

0.42

0.40

0.44

0.16 0.20 0.24

0.30 0.35 0.40

0.25 0.30 0.35 0.40

0.26 0.28 0.30 0.32

I The Lancet

###### J NEJM

###### K JAMA

L Health AVG

0.55

0.60

0.45

0.56

0.36

0.36

0.35

0.60

0.30

0.65

0.48

0.60

0.33

0.32

0.30

0.25

0.65

0.70

0.64

0.51

0.30

0.28

0.25

0.20

0.70

0.75 0.10 0.15 0.20 0.25

0.68

0.24

0.12 0.16 0.20

0.10 0.15 0.20 0.25

0.21 0.24 0.27

###### M PRL

N Astrophys. J.

###### O PRD

P Physical AVG

0.15

0.10

0.350 0.225

0.20

0.35

0.35

0.20

0.35

0.15

0.250

0.25

0.325

0.30

0.25

0.30

0.30

0.20

0.275

0.30

0.25

0.300

0.30

0.25

0.25

0.25

0.20

0.275

0.20

0.60 0.65 0.70

0.50 0.55 0.60 0.65

0.50 0.55 0.60

0.450 0.475 0.500

###### Q QJE

###### R ASR

S Comput. Linguist.

T Social AVG

0.25

0.30

0.40

0.36 0.24

0.40

0.30

0.33

0.45

0.28

0.33

0.35

0.30

0.32

0.35

0.36

0.50

0.32

0.30

0.28

0.25

0.30

0.40

0.36

0.39

0.55

0.25

0.24

0.20

0.27

0.40 0.45 0.50

0.30 0.35 0.40

0.44 0.48 0.52 0.56

0.36 0.39 0.42

- FIG. 4. Charting evolution traces of periodicals within the physical-life-health triangle. We show trajectories of closeness to the three research areas for 15 periodicals and the averaged trajectories over all periodicals in each category (the last column). Each trajectory is formed by sequentially connecting the positions in the triangle with arrows, from the 1950s (or the decade of establishment) to the 2010s.


##### Looking at physical science periodicals, The Astrophysical Journal, Physical Review D, and PRL underwent significant changes in the 1980s–1990s. The first two shifted away

from physical science, whereas PRL moved in the opposite direction (Fig. 4M–O). Still, they all gravitated towards life science, likely reflecting the thriving of biophysics as a distinct discipline. Finally, a noticeable trend towards life sciences was observed for the three social science periodicals (Figs. 4Q–S). However, QJE and Computational Linguistics reverted to their original levels as when they were established, while ASR ended up closer to life science. The relatively stable trajectory of Computational Linguistics over time may suggest its ongoing commitment to bridge computer science and linguistics.

D. Detecting emerging research topics

As periodicals typically publish topically coherent papers, the birth of new periodicals may signal the emergence of new fields or research directions. For instance, the identification of AIDS as a novel disease in the 1980s led to the establishment of a number of new journals, including AIDS and The Lancet HIV. Similarly, the invention of the scanning tunneling microscope and the discovery of fullerenes during the 1980s—both of which earned Nobel Prizes in 1986 and 1996, respectively—catalyzed the growth of nanotechnology research. This resulted in the creation of numerous journals, such as Nanotechnology, Nano Letters, and Advanced Materials, dedicated to this exciting new area. These observations prompt us to ask: Can we identify emerging research topics in the evolution of science through the lens of newly established periodicals?

Let us begin by examining individual periodicals. We hypothesize that as an emerging research topic matures, a tight cluster forms in which periodicals are highly similar to each other. For example, focusing on the journal AIDS, Fig. 5A illustrates this process. It shows that the nearest neighbors of AIDS became stable starting in the 2000s, with distances between them decreasing over time. This indicates a densification of its most similar neighbors and the formation of a locally cohesive cluster related to AIDS/HIV research, as shown by the periodical names (Table S7). We quantify this process by calculating the change in distance to its k-th nearest neighbor from the decade of establishment to the last decade: ∆d = dt1 − d2010s. For AIDS, ∆d = 0.27. A large ∆d signifies a substantial reduction in the minimum distance to cover its k nearest neighbors, thereby pointing to the formation of a local cluster.

We calculate ∆d for each new periodical across decades, allowing us to identify other

![image 2](Lyu and Ke_2025_Mapping the changing structure of science through diachronic periodical embeddings_images/imageFile2.png)

- A
- B C D


![image 3](Lyu and Ke_2025_Mapping the changing structure of science through diachronic periodical embeddings_images/imageFile3.png)

![image 4](Lyu and Ke_2025_Mapping the changing structure of science through diachronic periodical embeddings_images/imageFile4.png)

![image 5](Lyu and Ke_2025_Mapping the changing structure of science through diachronic periodical embeddings_images/imageFile5.png)

- FIG. 5. Detecting emerging research topics. (A) 2-d visualizations of AIDS (marked as stars) and its 10-nearest neighbors (marked as circles) in each decade. The red line marks d, the cosine distance from AIDS to its 10th nearest neighbor. (B–D) The most representative words appeared in the titles of top 10% periodicals based on ∆d for periodicals established in the (B) 1970s, (C) 1980s, and (D) 1990s.


periodicals that have undergone a similar process of forming a tight cluster since their inception. In the 1980s, notable examples include Sleep (∆d = 0.31), Biomaterials (∆d = 0.29), Journal of Controlled Release (∆d = 0.26), and Applied Organometallic Chemistry (∆d = 0.26) (Table S9). Overall, the distribution of ∆d is symmetrically centered around zero, indicating that only a minority of periodicals have wither merged into clusters or dissociated themselves from their neighborhood over time (Fig. S24). To identify potential emerging research topics, we calculate the representativeness of words in periodical titles by comparing periodicals with ∆d in the top 10% with non-top ones [38], hypothesizing that important topics may appear in multiple periodicals with large ∆d. Figs. 5B–D showcase the most representative words for periodicals established from the 1970s to the 1990s. In the 1970s, systems research and food science emerged as notable topics; the 1980s saw a rising interest in nephrology, hepatology, biomaterials, and AIDS research; while in the 1990s, hematology, sleep, and fractals were a focus of coherent topics.

###### III. DISCUSSION

In this work, we have presented a framework for generating diachronic embeddings of scholarly periodicals, enabling a systematic analysis of the evolving topics in published

research over time. It allows us to identify the directions of semantic shifts by mapping periodicals onto conceptual axes and to detect emerging research topics through tracking the formation of tight clusters. Our diachronic embeddings provide new measurements that address both conceptual and computational challenges. For instance, they enable us to quantify the proximity of periodicals to various disciplines and track the changing landscape of interdisciplinary periodicals. Through comprehensive demonstrations of the utility of our diachronic embeddings, our work represents one of the first efforts to extend embedding-based approaches in the science of science in a diachronic context.

When quantifying the extent of semantic changes, we are aware of another popular method that is based on the alignment between two vector spaces [39]. However, we have found that semantic changes based on this approach are highly influenced by the number of periodicals in different fields: Periodicals in larger fields on average have smaller changes, which arises from the inherent setup of aligning two vector spaces (see SI).

We acknowledge limitations in our study. First, our embeddings may be influenced by errors present in the dataset. Throughout our research, we have noticed instances of periodical entities that were incorrectly disambiguated, such as journals with the same acronym being misidentified as a single entity, or difficulties in accurately representing journals with name changes (see Table S3). Second, we split the dataset by publication decade and trained models using citations from within the same decade, thereby excluding cross-decade citations. Alternative techniques, such as temporal network embedding, may offer a way to incorporate these citations. Third, while our diachronic embeddings assign decade-specific vectors to each periodical, a single vector may not adequately represent multiple contexts, particularly for multidisciplinary periodicals. Future research could explore the effectiveness of contextualized embeddings, such as those derived from the Transformers, in downstream tasks related to scientific evolution. However, previous research suggests that Transformers-based embedding methods do not necessarily outperform word2vec in detecting semantic changes [40].

Despite these limitations, we demonstrate that diachronic embeddings can serve as a valuable tool for the science of science research. Future studies could explore additional dimensions, such as scientific discourse in texts, to create new embedding methods and address questions informed by the insights gained from these embeddings.

- IV. METHODS


A. Dataset

We use a version of the Microsoft Academic Graph (MAG) dataset retrieved in December 2021 [41]. MAG is a large-scale heterogeneous network that contains papers, citations, authors, journals, and more. For our analysis, we focus on journal and conference papers published from 1950 and onward, as earlier papers have scarce references. Our dataset contains 93,311,527 papers published in 53,412 periodicals, with a total of 554,338,274 citations between these papers.

Since discipline category information was not provided in MAG, we use Scopus subject area categories to label periodicals. Scopus employs the ASJC (All Science Journal Classification) scheme to categorize journals into 27 subject areas, which are further organized into four top-level subject fields: physical, life, health, and social science. For journals that belong to multiple subject areas, we select the one most commonly shared by the journal’s 50 closest journals, determined by cosine similarity between their embeddings. We match 22,364 journals between MAG and Scopus based on their names, of which 21,895 are covered in our embeddings.

B. Model

For each citation network between papers, we generate N citation trails, {T1, T2, · · · , TN},

by performing random walks on the network. Each node serves as the starting point of a random walk for five times, to ensure that every paper is visited, and each walk randomly follows outgoing links until reaching a dead end (a paper without outgoing links). For each trail T, represented as a sequence of papers (P1T, P2T, · · · , P|TT|), we create a corresponding periodical trail γT = (V1T,V2T, · · · ,V|TT|), where ViT indicates the publication venue (periodical) of PiT. We then filter out periodical trails of length 1 (i.e., |T| = 1),

- as they do not capture citation relationships between papers, as well as periodical trails composed solely of identical periodicals. We set a minimum frequency threshold of 50 for periodicals, meaning that those with fewer than 50 occurrences are excluded from the embedding model due to data sparsity. Table S1 provides summary statistics for each decade.


For each decade, we use the corpus of periodical trails to train a word2vec model with the skip-gram with negative sampling (SGNS) method [42]. Based on our previous research [17], we set the following hyperparameters: context window size w = 10, embedding dimensions D = 100, and number of sampled negative pairs for each positive input pair k = 5. We also conduct validation experiments with different hyperparameter configurations (see Table S4). After training, the “input” vectors from the word2vec model are used as the periodical embeddings. We utilize the Gensim package for embedding training [43] and obtain embeddings for 43,476 periodicals, after dropping 9,936 periodicals because of data filtering.

C. Data and code availability

##### MAG is publicly available at https://zenodo.org/records/6511057. The code used for data analysis and generating all the results presented in this work is available at https://github.com/netknowledge/diachronic-p2v [44].

###### ACKNOWLEDGMENTS

##### This work is supported by the National Natural Science Foundation of China (72204206), City University of Hong Kong (Project No. 9610552, 7005968), and the Hong Kong Institute for Data Science.

- [1] O. Henry, Epistle dedicatory, Philosophical Transactions of the Royal Society 1, i (1665).
- [2] M. Baldwin, Making “Nature”: The History of a Scientific Journal (University of Chicago Press, 2015).
- [3] A. Csiszar, The Scientific Journal: Authorship and the Politics of Knowledge in the Nineteenth Century (University of Chicago Press, 2018).
- [4] B. Uzzi, S. Mukherjee, M. Stringer, and B. Jones, Atypical combinations and scientific impact, Science 342, 468 (2013).
- [5] J. Wang, R. Veugelers, and P. Stephan, Bias against novelty in science: A cautionary tale for users of bibliometric indicators, Research Policy 46, 1416 (2017).


- [6] F. Narin, G. Pinski, and H. H. Gee, Structure of the biomedical literature, Journal of the American Society for Information Science 27, 25 (1976).
- [7] R. Nu´nez,˜ M. Allen, R. Gao, C. Miller Rigoli, J. Relaford-Doyle, and A. Semenuks, What happened to cognitive science?, Nature Human Behaviour 3, 782 (2019).
- [8] M. B. Line, The ‘half-life’ of periodical literature: Apparent and real obsolescence, Journal of Documentation 26, 46 (1970).
- [9] V. Calcagno, E. Demoinet, K. Gollner, L. Guidi, D. Ruths, and C. de Mazancourt, Flows of research manuscripts among scientific journals reveal hidden submission patterns, Science 338, 1065 (2012).
- [10] L. Leydesdorff, Various methods for the mapping of science, Scientometrics 11, 295 (1987).
- [11] H. Small, Visualizing science by citation mapping, Journal of the American Society for Information Science 50, 799 (1999).
- [12] R. M. Shiffrin and K. B¨orner, Mapping knowledge domains, Proceedings of the National Academy of Sciences 101, 5183 (2004).
- [13] K. W. Boyack, R. Klavans, and K. B¨orner, Mapping the backbone of science, Scientometrics 64, 351 (2005).
- [14] M. Rosvall and C. T. Bergstrom, Maps of random walks on complex networks reveal community structure, Proceedings of the National Academy of Sciences 105, 1118 (2008).
- [15] K. B¨orner, R. Klavans, M. Patek, A. M. Zoss, J. R. Biberstine, R. P. Light, V. Larivi`ere, and K. W. Boyack, Design and update of a classification system: The UCSD map of science, PLOS ONE 7, e39464 (2012).
- [16] J. Bollen, H. V. de Sompel, A. Hagberg, L. Bettencourt, R. Chute, M. A. Rodriguez, and L. Balakireva, Clickstream data yields high-resolution maps of science, PLOS ONE 4, e4803 (2009).
- [17] H. Peng, Q. Ke, C. Budak, D. M. Romero, and Y.-Y. Ahn, Neural embeddings of scholarly periodicals reveal complex disciplinary organizations, Science Advances 7, eabb9004 (2021).
- [18] A. J. Gates, Q. Ke, O. Varol, and A.-L. Barab´asi, Nature’s reach: narrow work has broad impact, Nature 575, 32 (2019).
- [19] B. McGillivray, G. B. Jenset, K. Salama, and D. Schut, Investigating patterns of change, stability, and interaction among scientific disciplines using embeddings, Humanities and Social Sciences Communications 9, 285 (2022).


- [20] T. Mikolov, K. Chen, G. Corrado, and J. Dean, Efficient estimation of word representations in vector space, arXiv:1301.3781 (2013).
- [21] P. Shoemark, F. F. Liza, D. Nguyen, S. Hale, and B. McGillivray, Room to Glo: A systematic comparison of semantic change detection approaches with word embeddings, in Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP) (2019) pp. 66–76.
- [22] D. Marr and E. Hildreth, Theory of edge detection, Proceedings of the Royal Society of London. Series B, Containing papers of a Biological character. Royal Society (Great Britain) 207, 187 (1980).
- [23] H. C. Longuet-Higgins and K. Prazdny, The interpretation of a moving retinal image, Proceedings of the Royal Society of London. Series B. Biological Sciences 208, 385 (1980).
- [24] M. V. Srinivasan, S. B. Laughlin, and A. Dubs, Predictive coding: a fresh view of inhibition in the retina, Proceedings of the Royal Society of London. Series B. Biological Sciences 216, 427 (1982).
- [25] D. I. Perrett, P. A. J. Smith, D. D. Potter, A. J. Mistlin, A. S. Head, A. D. Milner, and M. A. Jeeves, Visual cells in the temporal cortex sensitive to face view and gaze direction, Proceedings of the Royal Society of London. Series B. Biological Sciences 223, 293 (1985).
- [26] M. C. Morrone and D. C. Burr, Feature detection in human vision: a phase-dependent energy model, Proceedings of the Royal Society of London. Series B. Biological Sciences 235, 221

(1988).

- [27] D. C. Marr and S. Ullman, Directional selectivity and its use in early visual processing, Proceedings of the Royal Society of London. Series B. Biological Sciences 211, 151 (1981).
- [28] R. L. Gregory, Perceptions as hypotheses, Philosophical Transactions of the Royal Society of London. B, Biological Sciences 290, 181 (1980).
- [29] M. I. Posner, Y. Cohen, and R. D. Rafal, Neural systems control of spatial orienting, Philosophical Transactions of the Royal Society of London. B, Biological Sciences 298, 187 (1982).
- [30] D. N. Lee, The optic flow field: The foundation of vision, Philosophical Transactions of the Royal Society of London. B, Biological Sciences 290, 169 (1980).
- [31] A. T. Balaban and D. J. Klein, Is chemistry ‘the central science’? how are different sciences related? co-citations, reductionism, emergence, and posets, Scientometrics 69, 615 (2006).


- [32] M. Szell, Y. Ma, and R. Sinatra, A nobel opportunity for interdisciplinarity, Nature Physics 14, 1075 (2018).
- [33] A. J. Gates, I. B. Wood, W. P. Hetrick, and Y.-Y. Ahn, Element-centric clustering comparison unifies overlaps and hierarchy, Sci. Rep. 9, 8574 (2019).
- [34] D. Shepard, A two-dimensional interpolation function for irregularly-spaced data, in Proceedings of the 1968 23rd ACM National Conference (1968) pp. 517–524.
- [35] A. V. Hill, Why biophysics?, Science 124, 1233 (1956).
- [36] C. R. Woese, A new biology for a new century, Microbiology and Molecular Biology Reviews 68, 173 (2004).
- [37] I. L¨owy, Historiography of biomedicine: “bio,” “medicine,” and in between, Isis 102, 116

(2011).

- [38] B. L. Monroe, M. P. Colaresi, and K. M. Quinn, Fightin’ words: Lexical feature selection and evaluation for identifying the content of political conflict, Political Analysis 16, 372–403

(2017).

- [39] W. L. Hamilton, J. Leskovec, and D. Jurafsky, Diachronic word embeddings reveal statistical laws of semantic change, in Proceedings of the 54th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) (2016) pp. 1489–1501.
- [40] D. Schlechtweg, B. McGillivray, S. Hengchen, H. Dubossarsky, and N. Tahmasebi, SemEval2020 task 1: Unsupervised lexical semantic change detection, in Proceedings of the Fourteenth Workshop on Semantic Evaluation (International Committee for Computational Linguistics, Barcelona (online), 2020) pp. 1–23.
- [41] A. Sinha, Z. Shen, Y. Song, H. Ma, D. Eide, B.-j. P. Hsu, and K. Wang, An overview of microsoft academic service (mas) and applications, in Proceedings of the 24th International Conference on World Wide Web (2015) p. 243–246.
- [42] T. Mikolov, I. Sutskever, K. Chen, G. S. Corrado, and J. Dean, Distributed representations of words and phrases and their compositionality, in NIPS (2013).
- [43] R. Rehˇ uˇ˚rek and P. Sojka, Software framework for topic modelling with large corpora, in Proceedings of the LREC 2010 Workshop on New Challenges for NLP Frameworks (2010) pp. 45– 50.
- [44] Z. Lyu and Q. Ke, Diachronic periodical embeddings reveal the evolution of science. GitHub. https://github.com/netknowledge/diachronic-p2v (2025), deposited 28 April 2025.


- [45] P. H. Sch¨onemann, A generalized solution of the orthogonal procrustes problem, Psychometrika 31, 1 (1966).
- [46] L. v. d. Maaten and G. Hinton, Visualizing data using t-sne, Journal of Machine Learning Research 9, 2579 (2008).


## Supporting Information

- S1. SUPPORTING INFORMATION TEXT


A. Quantifying semantic change of periodicals

1. Local neighbor perspective

In the main text, we have quantified the semantic changes of periodical i between t1 and t2 from its local neighbor perspective, which is the cosine distance between the two vectors representing the cosine similarities between i and its nearest neighbors at t1 and t2. Fig. S13 presents the distributions of semantic changes between two consecutive decades, indicating limited changes across decades. Figs. S14–S15 show semantic changes of selected periodicals. Fig. S17 shows the distributions of semantic changes by field, suggesting that periodicals belonging to natural science disciplines, including Chemistry, Biochemistry, and Energy, as well as Multidisciplinary periodicals, tend to have greater semantic changes, compared to those peers that belong to Humanities, Social Sciences, and Business.

2. Global alignment perspective

We also explore another quantification of semantic change, which is based on global alignment between two vector spaces at t1 and t2, given that they may correspond to different coordinate systems. Specifically, let Vt ∈ Rd×|v| denote the matrix of embedding vectors learned at time t and d is the embedding dimension. The alignment is to find the best rotational operation that most closely maps Vt1 to Vt2 for the shared set of periodicals

- at t1 and t2. Formally, the alignment is solved through orthogonal Procrustes analysis:


R(t1→t2) = argmin

Q⊤Q=I

QVt1 − Vt2 F , (1)

where ∥·∥F is the Frobenius norm of a matrix and R(t1→t2) ∈ Rd×d is the identified rotational operation. Eq. 1 can be solved using the application of SVD [45]. Then, the seman-

tic change of periodical i is the cosine distance between vit2 and R(t1→t2)vit1, the aligned

vector of vit1 in the vector space at t2. Here we set t1 and t2 to be two consecutive decades.

However, we stress that although this method has been used in previous studies to detect semantic changes of words [39], it has unequal effects for periodicals from different disciplines. Specifically, the goal of Eq. 1 is to find the best rotation such that the sum of the vector differences across periodicals achieves minimum. Therefore, disciplines with more periodicals, such as Medicine, may play a larger role in determining the alignment matrix, and consequently those periodicals may have smaller semantic changes. Fig. S18 empirically demonstrates this discipline size effect, showing that disciplines with more periodicals tend to experience less semantic changes.

Bearing this caveat in mind, we nevertheless proceed to present the results about semantic changes of periodicals from the global alignment perspective. Fig. S19 indicates that across time, periodicals have limited semantic changes. Fig. S20 plots semantic changes of a set of selected periodicals, suggesting that Annals of Mathematics and American Sociological Review have larger changes than Nature, whereas the opposite is observed when semantic changes are measured using local neighbors. Finally, Fig. S21, which shows the distributions of total semantic changes by field, indicates that Physics and Astronomy, Chemistry, and Psychology periodicals are more vibrant than those from biomedical and health fields, reinforcing partially that semantic changes are dependent on field size.

###### S2. SUPPORTING INFORMATION FIGURES

Num of papers

Num of citations

Num of Periodicals

Num of papers citing peers

111290777

Num of trails

- 101

- 102

- 103

- 104

- 105

- 106

- 107

- 108


48229270

23237879

23120887

| |
|---|


13016157

10066798

7512046

4815134

| |
|---|


3540322

2697061

| |
|---|


1555945

1357085

| |
|---|


726052

| |
|---|


440737458818

276652

| |
|---|


203279

88908 93106

| |
|---|


67625

counts

53297

40872

| |
|---|


30375

13820

13555

10779

| |
|---|


6109

| |
|---|


4775

2778

| |
|---|


957

855

230

185

171

| |
|---|


46

40

40

37

| |
|---|


30

30

8

8

| |
|---|


6

6

1800-18091810-18191820-18291830-18391840-18491850-18591860-18691870-18791880-18891890-18991900-19091910-19191920-19291930-19391940-19491950-19591960-19691970-19791980-19891990-19992000-20092010-2021

decades

- FIG. S1. Summary statistics by decade. Most of these statistics grow exponentially, and the number of citations among papers in the same decade shows the most significant increment rate after the 1950s. The number of generated trails has been maintained at about five times the number of papers citing their peers.


![image 6](Lyu and Ke_2025_Mapping the changing structure of science through diachronic periodical embeddings_images/imageFile6.png)

- FIG. S2. A schematic illustration of obtaining diachronic periodical embeddings. (A) For each decade, we build a paper citation network from the MAG dataset representing citation relationships between papers published in the decade. (B) For each citation network, we perform random walks, by recursively setting every paper as the starting point of the random walk, and randomly choose the next point following the citation flow until we reach a dead end. We then map the sequences of visited papers to the sequences of periodicals, which are our corpora of “sentences”.


- (C) For each corpus, we use word2vec to generate embedding for periodicals that occurred in trails using the skip-gram with negative sampling (SGNS) method, with D = 100,W = 10. A 2-D projection (obtained by applying t-SNE[46]) of overall journal vectors is presented, where each dot represents a journal, and its color denotes its discipline designated in the Scopus ASJC (All Science Journal Classification) scheme (multidisciplinary journals are colored in black). This example is generated using data from the 2010s. By repeating A-C for corpora obtained over 7 decades, from the 1950s to the 2010s, diachronic periodical embeddings could be generated. It can be observed that the embedding space is being overpopulated (Figs. S3–S9 show the 2-d projections of periodical embeddings in the other decades), as a result of increasing number of periodicals (see Table S1).


![image 7](Lyu and Ke_2025_Mapping the changing structure of science through diachronic periodical embeddings_images/imageFile7.png)

###### FIG. S3. 2-D projection of journal embeddings using data from the 1950s.

![image 8](Lyu and Ke_2025_Mapping the changing structure of science through diachronic periodical embeddings_images/imageFile8.png)

###### FIG. S4. 2-D projection of journal embeddings using data from the 1960s.

![image 9](Lyu and Ke_2025_Mapping the changing structure of science through diachronic periodical embeddings_images/imageFile9.png)

###### FIG. S5. 2-D projection of journal embeddings using data from the 1970s.

![image 10](Lyu and Ke_2025_Mapping the changing structure of science through diachronic periodical embeddings_images/imageFile10.png)

###### FIG. S6. 2-D projection of journal embeddings using date from the 1980s.

![image 11](Lyu and Ke_2025_Mapping the changing structure of science through diachronic periodical embeddings_images/imageFile11.png)

###### FIG. S7. 2-D projection of journal embeddings using date from the 1990s.

![image 12](Lyu and Ke_2025_Mapping the changing structure of science through diachronic periodical embeddings_images/imageFile12.png)

###### FIG. S8. 2-D projection of journal embeddings using data from the 2000s.

![image 13](Lyu and Ke_2025_Mapping the changing structure of science through diachronic periodical embeddings_images/imageFile13.png)

###### FIG. S9. 2-D projection of journal embeddings using data from the 2010s.

2.0

###### R2 = 0.417

Relativesimilarity

1.5

1.0

0.5

0.0 0.5 1.0 1.5 2.0 2.5 3.0 3.5 Number of papers (log)

- FIG. S10. Validating diachronic periodical embeddings using Science.


| |R2 = 0.415| | | | | |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |


2.5

Relativesimilarity

2.0

1.5

1.0

0.5

0.0

0 1 2 3 4 Number of papers (log)

###### FIG. S11. Validating diachronic periodical embeddings using PNAS.

###### C

100

| |A| | | | | |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |


R2 = 0.393

Percentageofpapers

80

Relativesimilarity

- 0

- 1

- 2


60

40

20

0

0.0 0.5 1.0 1.5 2.0 2.5 3.0 3.5 Number of papers (log)

###### B

3.0

Relativesimilarity

2.5

Psychology

1970s 1980s 1990s 2000s 2010s

Linguistics

2.0

Artificial Intelligence

1.5

Anthropology

Exp. & Cog. Psych.

Philosophy

AI

1.0

Neuroscience

1970s 1980s 1990s 2000s 2010s Decade

- FIG. S12. Validating our diachronic periodical embeddings using Cognitive Science. (A) Percentage of papers in 6 founding disciplines (defined in [7]) by decade. Papers in the 2010s refer to those published in 2010–2021 for simplicity. (B) Relative similarity between Cognitive Science and periodicals from the 2 focused ASJC categories. Relative similarity is defined as the average cosine similarity between Cognitive Science and all periodicals belonging to that ASJC category, divided by the average cosine similarity between Cognitive Science and all periodicals. (C) The correspondence between publication volume and similarity. Color represents founding disciplines and the shape of point marks decade.


| | |
|---|---|
| | |
| | |
| | |


| | |
|---|---|
| | |
| | |
| | |


| | |
|---|---|
| | |
| | |
| | |


0.04

| | |
|---|---|
| | |
| | |
| | |


| | |
|---|---|
| | |
| | |
| | |


Semanticchange

| | |
|---|---|
| | |
| | |
| | |


0.03

0.02

0.01

1950s 1960s 1960s 1970s 1970s 1980s 1980s 1990s 1990s 2000s 2000s 2010s

- FIG. S13. Distributions of semantic changes based on local neighbors. Lower and upper whiskers correspond to 5th and 95th percentiles, and fliers are not shown for clarity.


Ann N Y Acad Sci (0.47)

Philos Trans R Soc (0.43)

Adv Pharmacol (0.41)

Yale J Biol Med (0.37)

Am Rev Respir Dis (0.34)

| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


0.20

0.15

0.10

0.05

0.00

Science (0.29)

Bull Math Biol (0.29)

Mt Sinai J Med (0.28)

Adv Int Med (0.27)

Adv Cardiology (0.27)

| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


0.20

0.15

0.10

0.05

0.00

Imaging Sci J (0.27)

Protein Sci (0.26)

Am J Phys (0.26)

Philos Trans R Soc A (0.26)

Philos Trans R Soc B (0.25)

| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


0.20

Semanticchange

0.15

0.10

0.05

0.00

Trans Am Philos Soc (0.24)

Nature (0.24)

Proc R Soc B (0.21)

J Antibiot (0.21)

J Biol Phys (0.19)

| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


0.20

0.15

0.10

0.05

0.00

Chemotherapy (0.19)

Adv Genet (0.18)

Eur J Haematol (0.17)

J Acoust Soc Am (0.15)

PNAS (0.12)

| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


0.20

0.15

0.10

0.05

Lancet (0.08)

BMJ (0.08)

IEEE Trans Inf Theory (0.08)

Cogn Sci (0.08)

Br J Radiol (0.07)

0.06

| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


0.05

0.04

0.03

0.02

0.01

0.00

Manag Sci (0.07)

JAMA (0.07)

J R Stat Soc C (0.07)

J Infect Dis (0.07)

NEJM (0.06)

0.06

| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


0.05

0.04

0.03

0.02

0.01

0.00

ACL (0.06)

Angewandte Chemie (0.06)

J Am Chem Soc (0.06)

Phys Rev Lett (0.05)

Bioinformatics (0.05)

0.06

| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


0.05

Semanticchange

0.04

0.03

0.02

0.01

0.00

Phys Rev D (0.05)

Am J Public Health (0.05)

Am Sociol Rev (0.04)

Econometrica (0.04)

Sci Total Environ (0.04)

0.06

| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


0.05

0.04

0.03

0.02

0.01

0.00

Q J Econ (0.03)

J Biol Chem (0.03)

Ann Math (0.03)

Astrophys J (0.02)

0.06

| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


0.05

0.04

0.03

0.02

0.01

800 1950s, N = 1121

A

Psychol. Bull.

Chem. Rev.

600

ASR

JAMA

Econometrica CA: Cancer J. Clin. Lancet

NEJM

BMJ

Proc. R. Soc. B

400

Ann. Math. QJE PRL

PNAS

Nature

Science

200

0

800 1960s, N = 1073

###### B

Mater. Res. Bull.

IEEE. Trans. Biomed. Eng. Ultrasonics

600

Automatica

IEEE Trans Nucl Sci

Lang. Learn. Pattern Recognit.

J. Appl. Crystallogr. JFQA

400

PLB Carbon SLR

Computing

200

0

800 1970s, N = 1916

###### C

Clin. Infect. Dis.

Account. Organ. Soc.

600

EJPR

Pain

Stud. Second Lang. Acquis.

Econ Anal Policy Linguist. Inq.

Cell

Res. Policy

Comput Biol Chem Gene Soc. Netw.

400

J. Biosci.

C.E.J

200

Numberofperidicals

0

800 1980s, N = 2959

###### D

Int. J. Remote Sens.

J. Phys. Condens. Matter JAPP EMJ Stem Cells

600

Transp. Rev.

Appl. Linguist.

NeurIPS

400

J. Account. Econ.

IEEE TMI J. Chemom. Bioelectromagnetics

200

0

800 1990s, N = 4924

E

KDD EMNLP

IEEE TAS

600

Cancer Cell Hum. Resour. Manag. J.

TheWebConf

400

Account. Rev. Cell Res. Materials Sensor

Complexity

200

0

800 2000s, N = 12151

| |Nat. Rev. Immunol.<br><br>Nat. Photonics Nat. Mater<br><br>Lancet Oncol.<br><br>F| | |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |


Obesity Nat. Chem. Biol.

600

PLOS ONE

400

IEEE TII

BMC Res. Notes

200

0

0.055 0.030 0.005 0.020 0.045 0.070 0.095 0.120 0.145 0.170 0.195 0.220 0.245 0.270 0.295

Total semantic change until the 2010s

- FIG. S16. Distributions of total semantic changes of periodicals. We group periodicals based on the decades when they were established and show the distributions for each group. Dashed vertical lines mark the medians. The number of periodicals N are marked on the top right on each panel. Table S8 lists periodical name abbreviations.


0.40

| | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | |


0.35

0.30

0.25

SCtotal

0.20

0.15

0.10

0.05

0.00

Neuro

Eng

Mat

Earth

Med

Math

CS

Env

Soc

Econ

Multi

Bio

Dec

Bus

Arts

ChemEng

Dent

Phys

Nurs

Chem

HealthPro

Biochem

Vet

Immuno

Energy

Pharm

Psy

- FIG. S17. Distributions of periodicals’ total semantic changes untill the 2010s by field (using local neighbor measurement), as designated in the Scopus database. Fields are arranged from left to right based on the median.

1 2 3 4 5 6

0.15

0.20

0.25

0.30

1950s 1960s (-0.20)

2 3 4 5 6

0.20

0.25

0.30

0.35

1960s 1970s (-0.37)

3 4 5 6

0.20

0.25

0.30

0.35

1970s 1980s (-0.42)

3 4 5 6 7

0.20

0.25

0.30

0.35

0.40

1980s 1990s (-0.42)

| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


3 4 5 6 7

0.25

0.30

0.35

0.40

1990s 2000s (-0.36)

4 5 6 7 8

0.20

0.25

0.30

0.35

0.40

2000s 2010s (-0.30)

Number of periodicals (log)

Mediansemanticchange

- FIG. S18. Disciplines with more periodicals tend to experience less semantic changes, which are calculated based on global alignment. Numbers in the parentheses in the titles are correlation coefficients.


1950s 1960s

200

150

100

50

Numberofperiodicals

0

1980s 1990s

1500

1250

1000

750

500

250

0

0.00 0.25 0.50 0.75 1.00

1960s 1970s

500

400

300

200

100

0

1990s 2000s

2500

2000

1500

1000

500

0

0.00 0.25 0.50 0.75 1.00

1970s 1980s

1000

800

600

400

200

0

2000s 2010s

5000

4000

3000

2000

1000

0

0.00 0.25 0.50 0.75 1.00

Semantic change

FIG. S19. Histograms of global alignment based semantic changes.

Ann N Y Acad Sci (2.82)

J R Stat Soc C (2.81)

Philos Trans R Soc A (2.80)

Proc R Soc B (2.18)

0.6

| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


0.5

0.4

0.3

0.2

0.1

0.0

IEEE Trans Inf Theory (1.84)

Phys Rev D (1.76)

Manag Sci (1.68)

Ann Math (1.64)

0.6

| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


0.5

0.4

0.3

0.2

0.1

0.0

Am Sociol Rev (1.62)

Br J Radiol (1.59)

Astrophys J (1.57)

Am J Public Health (1.50)

0.6

| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


0.5

0.4

0.3

0.2

0.1

Semanticchange

0.0

PNAS (1.32)

Angewandte Chemie (1.27)

JAMA (1.26)

J Infect Dis (1.25)

0.6

| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


0.5

0.4

0.3

0.2

0.1

0.0

BMJ (1.22)

Science (1.21)

J Am Chem Soc (1.07)

Nature (1.02)

0.6

| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


0.5

0.4

0.3

0.2

0.1

0.0

Lancet (0.99)

###### ACL (0.99)

Sci Total Environ (0.86)

Bioinformatics (0.84)

0.6

| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


0.5

0.4

0.3

0.2

0.1

0.0

1950s 1960s

1970s 1980s

1990s 2000s

1950s 1960s

1970s 1980s

1990s 2000s

1950s 1960s

1970s 1980s

1990s 2000s

1950s 1960s

1970s 1980s

1990s 2000s

Am Rev Respir Dis (2.09)

| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


Econometrica (1.63)

| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


Q J Econ (1.49)

| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


Phys Rev Lett (1.23)

| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


NEJM (1.02)

| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


J Biol Chem (0.65)

| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


1950s 1960s

1970s 1980s

1990s 2000s

###### FIG. S20. Semantic changes of selected periodicals. Numbers in the parentheses in the titles aretotal changes. Semantic changes are calculated based on global alignment.

3.5

3.0

2.5

| | |
|---|---|
| | |
| | |
| | |


| | |
|---|---|
| | |
| | |
| | |


Totalsemanticchange

| | |
|---|---|
| | |
| | |
| | |


| | |
|---|---|
| | |
| | |
| | |


| | |
|---|---|
| | |
| | |
| | |


| | |
|---|---|
| | |
| | |
| | |


| | |
|---|---|
| | |
| | |
| | |


| | |
|---|---|
| | |
| | |
| | |


2.0

| | |
|---|---|
| | |
| | |
| | |


| | |
|---|---|
| | |
| | |
| | |


| | |
|---|---|
| | |
| | |
| | |


| | |
|---|---|
| | |
| | |
| | |


| | |
|---|---|
| | |
| | |
| | |


| | |
|---|---|
| | |
| | |
| | |


| | |
|---|---|
| | |
| | |
| | |


| | |
|---|---|
| | |
| | |
| | |


| | |
|---|---|
| | |
| | |
| | |


| | |
|---|---|
| | |
| | |
| | |


| | |
|---|---|
| | |
| | |
| | |


| | |
|---|---|
| | |
| | |
| | |


1.5

| | |
|---|---|
| | |
| | |
| | |


| | |
|---|---|
| | |
| | |
| | |


| | |
|---|---|
| | |
| | |
| | |


| | |
|---|---|
| | |
| | |
| | |


| | |
|---|---|
| | |
| | |
| | |


| | |
|---|---|
| | |
| | |
| | |


| | |
|---|---|
| | |
| | |
| | |


1.0

0.5

0.0

Physics and AstronomyEarth and Planetary SciencesChemistryPsychologyMathematicsMultidisciplinaryChemical EngineeringAgricultural and Biological SciencesBiochemistry, Genetics and Molecular BiologyMaterials ScienceImmunology and MicrobiologyEconomics, Econometrics and FinanceEngineeringVeterinarySocial SciencesPharmacology, Toxicology and PharmaceuticsMedicineNeuroscienceComputer ScienceArts and HumanitiesDentistry Health ProfessionsNursingBusiness, Management and AccountingEnvironmental ScienceEnergyDecision Sciences

###### FIG. S21. Distributions of total semantic changes of periodicals by field. Fields are arranged fromleft to right based on the decreasing order of the median.

![image 14](Lyu and Ke_2025_Mapping the changing structure of science through diachronic periodical embeddings_images/imageFile14.png)

FIG.S22.Overalldistributionsofperiodicals’embeddingexhibitedinternaryplotsover7decades.Eachdotrepresentsajournalandis

colored by the research area it belongs to.

1950s (0.52)

1960s (0.59)

1970s (0.62)

1980s (0.67)

2000

4000

1750

500

1500

1500

400

3000

1250

300

1000

1000

2000

750

200

500

500

1000

100

250

0

0

0

0

Frequency

1990s (0.66)

2000s (0.66)

2010s (0.64)

12000

5000

8000

10000

4000

8000

6000

3000

6000

4000

2000

4000

2000

1000

2000

0

0

0

0.0 0.2 0.4 0.6 0.8

0.0 0.2 0.4 0.6 0.8

0.0 0.2 0.4 0.6 0.8

Similarity between Scopus label and k-means clustering results

- FIG. S23. Distributions of periodicals’ similarity between their Scopus label and k-means results.


Numberofperiodicals

1960s

| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


350

300

250

200

150

100

50

0

1980s

| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


1000

800

600

400

200

0

0.4 0.2 0.0 0.2

d

1970s

| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


800

600

400

200

0

1990s

1750

| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


1500

1250

1000

750

500

250

0

0.4 0.2 0.0 0.2

d

###### FIG. S24. Distribution of ∆d for periodicals established in each decade. Only a limited number ofperiodicals exhibit noticeable changes in distance to their 10th nearest neighbor, compared to the2010s.

###### S3. SUPPORTING INFORMATION TABLES

TABLE S1. Summary statistics by decade.

Period Papers Citations Papers citing peers Walks Periodicals

1950–1959 1764551 1438364 276652 1357085 4632 1960–1969 3127165 4356908 726052 3540322 7907 1970–1979 5081708 10729574 1555945 7512046 12430 1980–1989 7541503 21121496 2697061 13016157 18023 1990–1999 11724313 45487363 4815134 23237879 26957 2000–2009 22251359 111762233 10066798 48229270 40738 2010–2021 41820928 359442336 23120887 111290777 46074

TABLE S2. Number of journals in the 27 categories defined in Scopus.

|1950-1959<br><br>|1960-1969|1970-1979<br><br>|1980-1989<br><br>|1990-1999<br><br>|2000-2009<br><br>|2010-2021|
|---|---|---|---|---|---|---|
|count %|count %<br><br>|count %|count %<br><br>|count %|count %<br><br>|count %|


Multidisplinary 8 0.63 9 0.37 14 0.32 16 0.23 26 0.24 46 0.27 58 0.29 Biochemistry, Genetics and Molecular Biology 67 5.23 112 4.61 184 4.25 306 4.40 457 4.28 662 3.87 724 3.61 Physics and Astronomy 48 3.75 94 3.87 151 3.49 224 3.22 330 3.09 442 2.59 459 2.29 Chemistry 38 2.97 91 3.74 126 2.91 167 2.40 253 2.37 329 1.93 366 1.83 Medicine 351 27.42 526 21.65 901 20.82 1445 20.79 2311 21.66 3921 22.95 4635 23.13 Immunology and Microbiology 18 1.41 26 1.07 70 1.62 135 1.94 190 1.78 261 1.53 279 1.39 Engineering 62 4.84 187 7.70 287 6.63 462 6.65 644 6.04 945 5.53 1146 5.72 Arts and Humanities 111 8.67 196 8.07 359 8.29 547 7.87 797 7.47 1203 7.04 1571 7.84 Agricultural and Biological Sciences 161 12.58 274 11.28 402 9.29 608 8.75 804 7.54 1215 7.11 1373 6.85 Dentistry 10 0.78 18 0.74 26 0.60 43 0.62 69 0.65 111 0.65 139 0.69 Materials Science 11 0.86 50 2.06 77 1.78 120 1.73 181 1.70 353 2.07 443 2.21 Nursing 5 0.39 13 0.53 30 0.69 74 1.06 142 1.33 234 1.37 263 1.31 Psychology 33 2.58 62 2.55 137 3.17 227 3.27 360 3.37 485 2.84 520 2.59 Earth and Planetary Sciences 80 6.25 139 5.72 211 4.88 279 4.01 366 3.43 514 3.01 570 2.84 Decision Sciences 4 0.31 2 0.08 11 0.25 19 0.27 37 0.35 78 0.46 86 0.43 Mathematics 73 5.70 137 5.64 200 4.62 280 4.03 437 4.10 679 3.97 744 3.71 Pharmacology, Toxicology and Pharmaceutics 13 1.02 35 1.44 67 1.55 118 1.70 155 1.45 308 1.80 327 1.63 Environmental Science 4 0.31 21 0.86 68 1.57 122 1.76 195 1.83 347 2.03 424 2.12 Social Sciences 132 10.31 303 12.47 651 15.04 1071 15.41 1681 15.76 2747 16.08 3250 16.22 Neuroscience 2 0.16 8 0.33 35 0.81 55 0.79 91 0.85 139 0.81 158 0.79 Chemical Engineering 8 0.63 16 0.66 28 0.65 60 0.86 72 0.67 124 0.73 128 0.64 Veterinary 4 0.31 15 0.62 31 0.72 39 0.56 66 0.62 102 0.60 116 0.58 Economics, Econometrics and Finance 21 1.64 48 1.98 112 2.59 184 2.65 284 2.66 450 2.63 541 2.70 Energy 3 0.23 9 0.37 19 0.44 26 0.37 42 0.39 110 0.64 176 0.88 Computer Science 7 0.55 14 0.58 58 1.34 137 1.97 263 2.47 518 3.03 656 3.27 Business, Management and Accounting 3 0.23 17 0.70 53 1.22 148 2.13 324 3.04 604 3.53 708 3.53 Health Professions 3 0.23 8 0.33 20 0.46 38 0.55 91 0.85 160 0.94 180 0.90

in total 1280 2430 4328 6950 10668 17087 20040

- TABLE S3. Incorrectly disambiguated periodicals found in MAG. The third column indicates when the data corruption occurred. E.g. “1990-” means that the error lasted from the 1950s to the 1980s, and “2000+” means it started from the 2000s and last untill the 2010s.

Periodical Name in MAG Established Corrupted Mixed up with Japanese Journal of Pharmacology 1950s 2010s+ Journal of Japanese Philosophy Journal of Computers 1950s 2000s- Journal de Chimie Physique Journal of Algorithms 1980s 2010s+ Jurnal Ilmu Alam dan Lingkungan Journal of Agricultural Engineering Research 1960s 2010s+ Journal of Advances in Education Research Sozial-und Praventivmedizin 1970s 2010s+ Phytoth´erapie Scientia Forestalis 1950s 2000s- Book reviews puslished on Science Interpretation 1970s 2010s+ Interpretation Genes 1990s 2000s- Genes Protein Science 1950s 1990s- Fortschritte der Physik (Progress of Physics) Hospital Medicine 1990s 2010s+ Hospitality Society Immunotechnology 1990s 2000s+ Informacijos mokslai Journal of Ayurveda and Integrative Medicine 1990s 2010s- The Bulltin of Legal Medicine Versus 1990s 2010s- IEEE Workshop on Visual Surveillance Tradition 1950s 1980s+ Infant Mental Health Journal ACM Transactions on Cyber-Physical Systems 2000s 2010s- Thermal Conductivity Journal of Biomedical Engineering 1970s 2000s- Sheng Wu Yi Xue Gong Cheng Xue Za Zhi Antibiotics and Chemotherapy 1950s 2010s- Chemotherapy Social Work 1960s 2010s+ Semantic Web Production Journal 1980s 1990s- Child Phonology Insight 1990s 1990s+ Insight Sats 2000s 2010s+ SPE Saudi Arabia Section Technical Symposium and Exhibition Leonardo 1960s 2010s+ Innovation and Its Discontents (a book) The Forum 1990s 2010s- Forum Chemical Industry 2000s 2010s- Petroleum and Chemical Industry Conference Europe The American review of respiratory disease 1950s 2000s+ papers missing - only 1 paper in the whole 2000s Chemistry Industry 1950s 2010s+ KEMIJA U INDUSTRIJI (KUI, ”Chemistry in Industry”), Chemistry—An Asian Journal Biosilico 1990s 2010+ BIO, and Biodik : Jurnal Ilmiah Pendidikan Biologi Computer Science and Its Applications 1990s 1990s+ Current Swedish Archaeology Journal of Programming Languages 1990s 2000s+ Journal of Politics and Law

- TABLE S4. Hyperparameter tuning in the model training. Each model was trained using the same citation trails. The minimum frequency is set to 50 in all settings. W is the context window size, D is the number of embedding dimensions. τ is the the Kendall rank correlation coefficient between the proportion of papers and Mean(discipline)/Mean(general).


Nature Science PNAS D W τ p-value τ p-value τ p-value

50 2 0.5270 4.85 × 10−26 0.5183 3.20 × 10−25 0.4114 4.93 × 10−16 50 5 0.5489 4.21 × 10−28 0.5251 7.24 × 10−26 0.4261 4.88 × 10−17 50 10 0.5299 2.60 × 10−26 0.5012 1.05 × 10−23 0.4017 2.56 × 10−15

100 2 0.5475 5.59 × 10−28 0.5204 2.00 × 10−25 0.4017 2.47 × 10−15 100 5 0.5351 8.54 × 10−27 0.5098 1.81 × 10−24 0.3959 6.05 × 10−15 100 10 0.5283 3.84 × 10−26 0.4885 1.36 × 10−22 0.3939 8.73 × 10−15 200 2 0.5408 2.43 × 10−27 0.5245 8.24 × 10−26 0.3930 9.15 × 10−15 200 5 0.5431 1.49 × 10−27 0.5059 4.03 × 10−24 0.3893 1.67 × 10−14 200 10 0.5192 2.58 × 10−25 0.4896 1.10 × 10−22 0.3831 4.13 × 10−14 300 2 0.5426 1.70 × 10−27 0.5178 3.42 × 10−25 0.3932 8.61 × 10−15 300 5 0.5360 7.01 × 10−27 0.5002 1.32 × 10−23 0.3869 2.35 × 10−14 300 10 0.5386 3.98 × 10−27 0.4966 2.72 × 10−23 0.3695 2.96 × 10−13

TABLE S5. Top 10 neighbors of Nature in different decades.

1950s 1960s 1970s 1980s Journal of Molecular Biology Science Science Science Biochimica et Biophysica Acta International Geophysics Advances in Cell Biology PNAS Naturwissenschaften Naturwissenschaften PNAS Oncogene Research Current Science Proc. Royal Soc. B Leukocyte Culture Conference Oncogene Research Biochimica et Biophysica Acta Current Genetics Progress in Growth Factor Research Bull. Soc. chim. biol. Journal of Cell Science Immunological Investigations The EMBO Journal Methods in Enzymology Philos. Trans. R. Soc. A Results and problems in cell differentiation Cold Spring Harb. Symp. Quant. Biol. New Phytologist Biochemical Journal Cell Current Protocols in Molecular Biology Trans. R. Soc. South Africa Indian Journal of Biochemistry Scottish Journal of Geology J. Mol. Cell. Immunol. Biochemical Journal Comprehensive Biochemistry Cell Biology and Immunology of Leukocyte Function Cell

1990s 2000s 2010s Science Science Science PNAS PNAS Nature Communication Current Biology PLOS Biology Science Advances Cell Reflets De La Physique PNAS Evol. Dev. Harvey Lectures iScience J. Mol. Cell. Immunol. Epigenetics Chromatin National Science Review The EMBO Journal Cold Spring Harb. Perspect. Biol. Cell Curr. Opin. Genet. Dev. Embo Molecular Medicine Scientific Reports In Silico Biol. PLOS ONE Clinical OMICs Expert Rev. Mol. Med. Math. Biol. Bioinform. Journal of Genomes and Exomes

TABLE S6. Top 10 neighbors of Bulletin of Mathematical Biology in different decades.

1950s 1960s 1970s 1980s Synthese J. Theor. Biol. J. Math. Biol. Bellman Prize Math. Biosci. Adv. Biol. Med. Phys. IEEE Trans. Biomed. Eng. Bellman Prize Math. Biosci. J. Math. Biol. Trabajos De Estadistica Bellman Prize Math. Biosci. J. Theor. Biol. J. Theor. Biol. Hereditas Int. Jt. Conf. Artif. Intell. Biophys. J. Math. Model. Ire Trans. Med. Electron. R. I. Med. J. Siam J. Appl. Math. Appl. Math. Lett. Tijdschrift Voor Filosofie Kybernetika Biol. Cybern. Math. Comput. Simul. Psychometrika BioSystems Adv. Biol. Med. Phys. Probab. Eng. Inf. Sci. Arkiv f¨or Matematik J. Membr. Biol. Ann. Biomed. Eng. Math. Med. Biol. Sch. Sci. Math. J. Biomech. Ecol. Model. Phys. D: Nonlinear Phenom. Jpn. J. Physiol. Inf. Comput. J. Biol. Phys. Kybernetes

1990s 2000s 2010s J. Theor. Biol. J. Math. Biol. Bellman Prize Math. Biosci. IEEE IJCNN J. Theor. Biol. J. Math. Biol. J. Biol. Syst. Math. Med. Biol. J. Theor. Biol. Math. Med. Biol. Math. Biosci. Eng. Math. Med. Biol. Artificial Life Bellman Prize Math. Biosci. Int. J. Biomath. Bellman Prize Math. Biosci. Math. Model. Nat. Phenom. BioSystems IEEE Trans. Neural Netw. Acta Biotheor. J. Biol. Dyn. Simulated Evol. Learn. BioSystems Math. Biosci. Eng. J. Math. Biol. J. Biol. Syst. Theor. Popul. Biol. N. Z. Int. Two-Stream Conf. Artif. Neural Netw. Expert Syst. Theor. Biol. Med. Model. Eur. Conf. Math. Theor. Biol.

TABLE S7. Top 10 neighbors of AIDS in different decades.

1980s 1990s 2000s 2010s

J. Acquir. Immune Defic. Syndr. J. Acquir. Immune Defic. Syndr. J. Acquir. Immune Defic. Syndr. J. Acquir. Immune Defic. Syndr. AIDS Care AIDS Res. Hum. Retrovir. HIV Med. Lancet HIV Morb. Mortal. Wkly. Rep. Antivir. Ther. Antivir. Ther. Curr. HIV/AIDS Rep. Fam. Pract. P. R. Health Sci. J. HIV Clin. Trials J. Int. AIDS Soc. J. Public Health AIDS Patient Care STDs Curr. Opin. HIV AIDS AIDS Res. Hum. Retrovir. NIPH Ann. Curr. Opin. Infect. Dis. AIDS Rev. HIV Med. Prog. Hematol. Int. J. STD AIDS AIDS Res. Hum. Retrovir. Aids Res. Ther. Del. Med. J. J. Infect. Dis. AIDS Care Curr. Opin. HIV AIDS Boll. Ist. sieroter. milan. J. Assoc. Nurses AIDS Care AIDS Patient Care STDs AIDS Patient Care STDs Pediatr. Infect. Dis. AIDS Clin. Care HIV AIDS Rev. AIDS Rev.

TABLE S8. Periodicals’ abbrevations used in Fig. S16.

Periodical Name Abbreviation Periodical Name Abbreviation

CA: A Cancer Journal for Clinicians CA: Cancer J. Clin. Social Networks Soc. Netw. Quarterly Journal of Economics QJE Life sciences in space research Life Sci Space Res Econometrica Econometrica Computational Biology and Chemistry Comput Biol Chem Psychological Bulletin Psychol. Bull. Civil Engineering C.E.J Chemical Reviews Chem. Rev. Journal of Biosciences J. Biosci. JAMA JAMA Cell Cell Science Science Applied Linguistics Appl. Linguist. Nature Nature Journal of Accounting and Economics J. Account. Econ Proceedings of the National Academy of Sciences of the USA PNAS Journal of Accounting and Public Policy JAPP Physical Review Letters PRL Journal of Physics: Condensed Matter J. Phys. Condens. Matter The New England Journal of Medicine NEJM Transport Reviews Transp. Rev. American Sociological Review ASR European Management Journal EMJ Annals of Mathematics Ann. Math. International Journal of Remote Sensing Int. J. Remote Sens. The Lancet Lancet Stem Cells Stem Cells BMJ BMJ Journal of Chemometrics J. Chemom. Proceedings of The Royal Society B: Biological Sciences Proc. R. Soc. B Bioelectromagnetics Bioelectromagnetics Atmosphere Atmosphere neural information processing systems NeurIPS Language Learning Lang. Learn. IEEE Transactions on Medical Imaging IEEE TMI Automatica Automatica The Accounting Review Account. Rev. Materials Research Bulletin Mater. Res. Bull. Human Resource Management Journal Hum. Resour. Manag. J. Carbon Carbon Cancer Cell Cancer Cell Stanford Law Review SLR IEEE Transactions on Applied Superconductivity IEEE TAS Computing Computing Cell Research Cell Res. Journal of Applied Crystallography J. Appl. Crystallogr. the web conference TheWebConf Ultrasonics Ultrasonics knowledge discovery and data mining KDD IEEE Transactions on Nuclear Science IEEE Trans Nucl Sci empirical methods in natural language processing EMNLP IEEE Transactions on Biomedical Engineering IEEE. Trans. Biomed. Eng. Materials Materials Pattern Recognition Pattern Recognit. Sensors Sensors Physics Letters B PLB Complexity Complexity Journal of Financial and Quantitative Analysis JFQA PLOS ONE PLOS ONE Studies in Second Language Acquisition Stud. Second Lang. Acquis. Nature Reviews Immunology Nat. Rev. Immunol. Linguistic Inquiry Linguist. Inq. Nature Materials Nat. Mater European Journal of Political Research EJPR Lancet Oncology Lancet Oncol. Accounting Organizations and Society Account. Organ. Soc. Nature Photonics Nat. Photonics Clinical Infectious Diseases Clin. Infect. Dis. Obesity Obesity Economic Analysis and Policy Econ Anal Policy Nature Chemical Biology Nat. Chem. Biol. Research Policy Res. Policy IEEE Transactions on Industrial Informatics IEEE TII Gene Gene BMC Research Notes BMC Res. Notes Pain Pain

TABLE S9. List of the top periodicals with the largest ∆d in each decade.

Periodical ∆d 1960s Bulletin of Environmental Contamination and Toxicology 0.323 Physical Therapy 0.320 The Journal of Nuclear Medicine 0.319 Medical & Biological Engineering & Computing 0.315 Calcified Tissue International 0.314 Reproduction 0.302 Clinical Obstetrics and Gynecology 0.290 European Journal of Nutrition 0.290 Diabetologia 0.285 Journal of Catalysis 0.284 1970s Synthesis 0.303 Drug Development and Industrial Pharmacy 0.296 Pain 0.293 Journal of Food Science and Technology-mysore 0.286 Scandinavian Journal of Rheumatology 0.284 Kidney International 0.274 Journal of Optics 0.274 Clinical & Experimental Allergy 0.274 International Journal of Pharmaceutics 0.273 The Journal of Allergy and Clinical Immunology 0.269 1980s Sleep 0.308 Biomaterials 0.288 AIDS 0.266 Journal of Controlled Release 0.265 Applied Organometallic Chemistry 0.262 Archives of Gerontology and Geriatrics 0.261 Journal of Automated Methods & Management in Chemistry 0.261 Particle & Particle Systems Characterization 0.256 Fitoterapia 0.247 Biomedicine & Pharmacotherapy 0.243 1990s Cell Transplantation 0.285 Europace 0.253 Enfermedades Infecciosas Y Microbiologia Clinica 0.248 Journal of Sleep Research 0.247 Indicator South Africa 0.240 International Conference on Telecommunications 0.237 Nanotechnology 0.234 Materials Science and Engineering: C 0.229 Biological Research 0.224 Experimental and Molecular Medicine 0.221

