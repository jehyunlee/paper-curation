Scientometrics (2024) 129:7055–7081 https://doi.org/10.1007/s11192-024-05161-6

Comparative science mapping: a novel conceptual structure analysis with metadata

Massimo Aria1,5 · Corrado Cuccurullo2,5 · Luca D’Aniello3,5 · Michelangelo Misuraca4,5 · Maria Spano1,5

Received: 10 May 2024 / Accepted: 16 September 2024 / Published online: 28 September 2024 © The Author(s) 2024

### Abstract

Textual analyses on scientific publications are increasingly employed in Bibliometrics to explore the conceptual structure of a research domain, often overlooking other rich metadata that can provide deeper insights into the scientific landscape of reference. This paper introduces an innovative technique to explore the conceptual structure of different observation units in a joint representation. The proposed strategy segments bibliographic datasets based on several metadata dimensions, such as the authors (and their characteristics), the corresponding institutions, or their geographical localisation. It provides detailed maps that depict multiple conceptual frameworks, allowing for detailed comparisons and insights in a joint visualisation. We employed these strategic diagrams to visualise and analyse the oncological research of Italian Academic Medical Centres (AMCs), particularly focusing on public institutions. The analysis focuses on how different AMCs specialise and interact, providing a comparative framework that aids AMCs themselves in directing their research strategies toward innovative fronts. Furthermore, these visualisations can assist policymakers and healthcare stakeholders in understanding the broader research environment, which is crucial for informed decision-making regarding funding and policy development related to the AMCs’ triple mission.

* Maria Spano maria.spano@unina.it Massimo Aria aria@unina.it Corrado Cuccurullo corrado.cuccurullo@unicampania.it Luca D’Aniello luca.daniello@unina.it Michelangelo Misuraca michelangelo.misuraca@unical.it

- 1 University of Naples Federico II, Naples 80126, Italy
- 2 University of Campania L. Vanvitelli, Capua 81043, Italy
- 3 University of Naples Federico II, Naples 80138, Italy
- 4 University of Calabria, Rende 87036, Italy
- 5 K-Synth, Naples 80126, Italy


Vol.:(0123456789)

Keywords Science mapping · Conceptual structure analysis · Visualisation · Open science

# Introduction

Many researchers use quantitative methods to explore the findings of the fields they work in, the influence of the different schools of thought or the competition of conflicting positions, the journals (or the conferences) considered as majorly relevant by the research community of reference, the gaps, trends, and future opportunities (Zhao, 2010). In this framework, the development of bibliometrics introduced the possibility of a systematic, transparent, and reproducible review process based on the statistical measure of science, scientists, and scientific activity. Performance analyses and science mapping (Noyons et al., 1999) are the two main approaches for investigating a scientific field. Typically, performance analyses focus on the authors of scientific contributions, their affiliation and geographical localisation, and leverage the information concerning the contributions themselves, like their source (i.e., where a contribution has been published), the number of citations, the year of publications, and so on, to quantitatively measure the impact and the productivity of the actors involved. Science mapping approaches, instead, employ graphical representations of the patterns and dynamics of knowledge in a given domain, trying to depict its social, intellectual and conceptual structures (Börner, 2010; van Raan, 2019).

The latter emerges in particular from scientific publications’ textual content. Generally, the title, abstract and keywords (more rarely, the full body) of publications are stored in indexing databases, allowing researchers to explore the main topics, concepts, and results of the scientific field of interest, having an overview of the issues addressed in the investigated field with a synchronic perspective (Callon et al., 1983) to portray its state of the art or with a diachronic perspective (Cobo et al., 2011a) to track its evolution. The analyses on textual content, in a bibliometric framework, are mainly carried out through network analysis approaches (Cobo et al., 2011b), highlighting the links between the terms used in the publications but losing a rich range of other information held by bibliographic records that can help researchers understand the landscape of the investigated scientific field.

To leverage such ‘metadata’ from a science mapping perspective, we propose a new analytical strategy that maps the conceptual structure of a domain at a higher level of detail. The bibliographic dataset used in the analysis is segmented according to a characteristic of interest (e.g., the author name or the author type, the institution, the country), allowing the depiction of the distinct conceptual structures. In addition, the separate frameworks are jointly plotted, producing an overall strategic diagram that tracks the different concepts/ topics developed in the scientific field by the various players. Through this novel science mapping technique, we visualise the conceptual structure of the different Italian Academic Medical Centres (AMCs) involved in oncological research, with particular attention to public institutions. AMCs are bodies that combine medical education, research, and clinical care and are typically affiliated with a university’s medical school. They serve as training grounds for medical students, residents, and fellows, encompassing a broad range of in-training healthcare professionals. In addition to providing education, AMCs are often involved in cutting-edge research that shapes the future of healthcare and medical practices, and deliver a broad spectrum of patient care, including specialised treatments and complex procedures that may not be available in other settings. In particular, here we analysed

the research fronts of the different AMCs in oncological research, visualising them in an innovative joint representation that helped compare the main research areas and themes as well as the various specialisations of multiple players operating in the same field.

Oncological research is a multifaceted domain that focuses on understanding cancer biology, identifying risk factors, developing treatments, and improving patient outcomes. Current fronts in oncological research may be summarised in five categories:

- • precision medicine: tailoring treatments based on a patient’s genetic makeup and the genetic profile of their tumour. This personalised approach facilitates the development of targeted therapies aimed at specific molecular pathways;
- • immunotherapy: leveraging patients’ immune system to fight cancer, with treatments such as checkpoint inhibitors and CAR-T cell therapies for certain types of cancer (Waldmann, 2003; Esfahani et al., 2003);
- • real-world evidence: using data collected outside of traditional clinical trials, such as electronic health records and patient registries, to inform treatment decisions, understand disease patterns, and develop new therapies (Di Maio et al., 2019; Khozin et al., 2017).
- • early detection and prevention: identifying biomarkers and developing screening tools that can detect cancer at its earliest and most treatable stages;
- • cancer survivorship: addressing long-term physical, psychological, and social effects faced by cancer survivors and improving their quality of life (Halpern et al., 2015).


Mapping the dynamic positioning of Italian oncological medical research at various levels (i.e., national versus regional, AMCs as a whole versus single AMCs) provides a conceptual framework for the research institutions themselves to direct their efforts towards increasingly innovative fronts, taking into account the general landscape and, at the same time, exploiting this information to establish collaborations with other institutions dealing with the same research areas or topics. Moreover, the possibility of overviewing research in a given field is also helpful for policymakers and other stakeholders involved in healthcare and interested in understanding and administering the different concerns of AMCs, such as appropriate funding mechanisms for financing their crucial ‘triple-mission’ (Leydesdorff & Etzkowitz, 1998).

The paper is structured as follows. In “Mapping scientific fields’ conceptual structure” Sect., the common science mapping strategy based on co-word analysis and its evolution obtained by introducing metadata are formally described. In “Thematic atlas of the Italian oncological research” Sect., a study of Italian oncological research carried out in AMCs during 2000–2019 is presented, aiming at obtaining a thematic atlas through implementing the proposed novel strategy. In “Discussion and final remarks” Sect., some conclusive remarks and possible future developments are reported, discussing the theoretical and practical contributions of the results presented here.

# Mapping scientific fields’ conceptual structure

The scope and volume of research have dramatically increased in the most diverse scientific fields of knowledge over the past years, with a subsequent exponential growth of literature. For this reason, systematically reviewing publications related to a specific domain has become increasingly complex, requiring the intensive use of automatic

quantitative approaches. Alongside the evolution of information and communication technologies, the availability of online resources from indexing databases (e.g., Web of Science, Scopus, Google Scholar) allowed scholars to explore a significant amount of publications, providing valuable insight into existing studies, identifying shared positions and gaps, suggesting open questions and areas of future development. Starting from the textual content encompassed in bibliographic databases (typically, titles, abstracts and keywords of publications), in particular, it is possible to detect and map the concepts/ topics related to the research areas or theme of a scientific field (or subfield) as well as their relations (Leydesdorff, 1989; Noyons & van Raan, 1998; Börner et al., 2003). The resulting conceptual framework becomes a fundamental knowledge base for scholars as well as for institutions evaluating and funding research, which need to track the dynamics of science for planning purposes (Healey et al., 1986; Healey, 1991).

One of the primary approaches in bibliometrics for bringing out the conceptual structure of a scientific field—falling within the most popular science mapping methods—is the so-called co-word analysis. Firstly introduced by Callon et al. (1983), co-word analysis allows identifying association patterns between terms belonging to a set of publications, bringing out the conceptual structure of a scientific field (in the following, the field is intended as a whole research domain or one of its subfields). The rationale of the approach relies on the following premises: (1) authors of scientific publications properly select the terms necessary to describe the different aspects of their research; (2) the use of different terms within the same publication implies potential relationships within one or more concepts/topics; (3) if several authors prove to acknowledge the same set of relationships, it means that the latter holds special significance in the given field of interest. From a methodological viewpoint, the approach involves the terms’ co-occurrence counting. The idea behind the co-word analysis is that the more couples of terms appear together, the stronger their relationship and, hence, their conceptual nexus. Considering all the term couples in the publications, the resulting data structure may be mapped into diagrammatic representations such as trees or graph networks, employing statistical measures to assess the relational significance. Since the co-word analysis was proposed, it has been successfully applied to explore the conceptual structure of different domains (e.g., Coulter et al., 1998; Ding et al., 2001; Wang et al., 2012).

## Problem definition and analytical strategy

Consider a set of n publication records retrieved from a bibliographic database. For each record, a set of metadata concerning the publication itself, the author(s) and the corresponding affiliation, as well as the references, are available. As stated above, the conceptual structure of a scientific field can be highlighted by analysing the textual content of the given set (e.g., authors’ keywords, titles and/or abstracts of the publications). Once selected which part of bibliographic records’ text has to be analysed, it is necessary to prepare the resulting textual body by employing a pre-processing pipeline to avoid potential sources of noise and reduce linguistic heterogeneity at a morphological, lexical and semantic level (see Misuraca & Spano, 2020).

At the end of pre-processing, by using the vector space model (Salton et al., 1975) to derive a set of structured data from text, a documents × terms matrix F with n rows and p columns is built, where p is the number of unique terms listed in the vocabulary of the textual body containing all the publication elements of interest. The generic element fij of the matrix (with i = 1,…,n;j = 1,…,p) represents the importance of a term tj in a

publication di according to the selected weighting scheme (Misuraca et al., 2023). In its simplest form, F is a binary matrix where the generic element fij equals 1 if the term tj occurs at least once in the document di, 0 otherwise. From the documents × terms matrix, it is also possible to derive a p-dimensional terms × terms matrix A = F F. The generic element ajj (j ≠ j ) is the number of documents in which terms tj and tj co-occur (i.e., they are jointly used in the documents). The ajj elements on the principal diagonal of A count the total number of documents containing the specific term tj.

Several alternatives have been proposed and employed in text mining and science mapping literature to count for term co-occurrences in text analyses. The most common indices used in the context of term-based science mapping to quantitatively express the link between two different terms appearing in a collection of publications are the cosine (Salton & McGill, 1983), the Jaccard index (Rip & Courtial, 1984), the inclusion index (Callon et al., 1986) and the association strength (van Eck & Waltman, 2007). Several studies analysed the characteristics of the different proposals, showing their behaviour and the possible shortcomings (e.g. Hamers et al., 1989; Mainali et al., 2009; Sternitzke & Bergmann,2022). In a bibliometric context, van Eck and Waltman (2009) showed that the co-occurrence of two terms belonging to a scientific publication can be more conveniently expressed—among the different mentioned choices—through the association strength due to its probabilistic interpretation. According to the notation above used to define the matrix A, the index can be formally written as:

ajj ajjaj j

ASjj = (1)

where ajj is the observed number of co-occurrence of terms tj and tj , whereas ajj and aj j are the expected numbers of occurrences of tj and tj under the assumption they are statistically independent. The association strength proposed in Eq. 1 is a normalised measure, assuming values in an interval [0,1]. At a value of 0, the observed couple of terms does not co-occur in any analysed publications, while at a value of 1, the observed couple of terms co-occurs in all the analysed publications.

According to network theory, A can be seen as an adjacency matrix, depictable as an undirected weighted graph G(V,E, ) in which each term acts as one of its V nodes, the joint terms’ appearances acts as one of the E links, and ∶ E → R+ is a function assigning weights to the links. Typically, the elements on the principal diagonal are not considered in the graph since they represent buckles and are not informative. This representation allows for visualising both terms at a single level as well as subsets of terms frequently co-occurring together. The underlying assumption is that knowledge can be effectively cast into this format (Sowa, 1984; James, 1992; Carley, 1997). To uncover the set of K different concepts/topics forming the conceptual structure of the surveyed field, it is possible to refer to the so-called community detection (Fortunato, 2010). Community detection allows finding a partition of subgraphs with strongly linked nodes. In the case of science mapping, each subgraph corresponds to a subset of strongly connected terms and, hence, to a concept or topic discussed in the collection of publications under investigation.

Several algorithms can be considered to cope with the described task. Starting from the proposal of Girvan and Newman (2002) based on edge centrality, some authors suggested detecting the community structure of a graph through modularity optimisation (e.g. the fast greedy algorithm of Clauset et al., 2004), through dynamic distances (e.g. the walktrap algorithm of Pons & Latapy, 2005), or through information compression (e.g. the infomap algorithm of Pons & Latapy, 2008). Many other available

variants and alternatives have been used in several applications (). Among the others, the Louvain algorithm proposed by Blondel et al. (2008) showed high effectiveness in comparison with other proposals, both for small and large networks (Yang et al., 2016). An improvement of the Louvain algorithm, known as Leiden algorithm, has been more recently proposed by Traag et al. (2019), overcoming some known limitations concerning the quality of detected communities and the robustness of results but, on the other hand, introducing additional complexity and computational overhead.

The subgraphs obtained by applying the community detection procedure can be better visualised in a bi-dimensional plot known as strategic diagram (Callon et al., 1991; Cobo et al., 2011a), whose axes are a reverse rank transformation of Callon centrality and Callon density:

CCk = 10 × (2)

ASjh

j∈k,h∈k

ASjj t(k)

CDk = 102 × (3)

j,j ∈k

where ASjh is the association strength between terms tj and th belonging to two distinct concept/topic k and k (with k,k ∈ K), ASjj is the association strength between a couple of terms tj and tj belonging to a given topic k, and t(k) is the total number of terms belonging to k. Callon centrality (Eq. 2) can be read as the importance of a concept/topic in the analysed research domain or theme. In contrast, Callon density (Eq. 3) can be read as a concept/ topic development measure. The origin of the coordinate system is set on the centrality and density median rank position. The plot allows defining four typologies of concepts/topics (Cahlik, 2000) according to the quadrant in which they are projected:

- • higher rank values of centrality and density define motor issues that are both relevant and well-developed for the research areas or themes of the scientific field. These concepts/topics are critical for the definition of the related conceptual structure;
- • higher rank values of centrality and lower rank values of density define basic and transversal issues. These concepts/topics are common for the scientific field and pertain to general issues transversal to its different research areas or themes;
- • lower rank values of centrality and density define peripheral issues. They have both low relevance and development. Peripheral issues are weakly developed and marginally relevant within the scientific field (declining issues), or in the initial stages of development and still achieving full awareness (emerging issues);
- • lower rank values of centrality and higher rank values of density define niche issues. These concepts/topics have well-established internal links but unimportant external links, thus they are well developed but of limited relevance within the scientific field.


The steps necessary to bring out a scientific field’s conceptual structure are synthetically depicted in the subsequent Fig. 1.

The strategy has been employed in several studies concerning the most diverse scientific fields (e.g., De Nito et al., 2015; Furstenau et al., 2022; Cobo et al., 2023; VelezEstevez et al., 2023), single journals (e.g., Aria et al., 2020; López-Robles et al., 2021 and even adapted for social media analysis (Aria et al., 2022).

![image 1](Aria et al._2024_Comparative science mapping a novel conceptual structure analysis with metadata_images/imageFile1.png)

- Fig. 1 Analytical strategy for detecting and mapping the conceptual structure


## Conceptual structure analysis with metadata

As claimed above, each bibliographic record usually contains the textual content of the indexed publication and metadata concerning the publication itself (e.g., year, type, source, number of citations, references) as well as the author(s) (e.g., name, affiliation, country). Depending on the indexing database, some of these metadata may be missed or not indexed at all. Typically, the metadata are used in performance analyses to measure the impact and productivity of actors and in science mapping to highlight the intellectual and social structure of a scientific field or related to a particular research issue (Noyons et al., 1991; Peters & van Raan, 1999).

Considering a different standpoint, metadata can be used as external or additional information in the conceptual structure analysis carried out on the available textual content of publications. Baccini et al. (2024), for example, tried combining textual information and metadata to better cluster scientific publications, following the logic of hybrid clustering proposed in scientometrics by Janssens et al. (2009). They performed an LDA topic modelling (Blei, Ng, and Jordan, 2003) to detect the main concepts/topics and the related keywords and connect publications by the similarity of their conceptual frame. Subsequently, they performed a bibliographic coupling (Small, 1997) to connect publications by the conceptual frame similarities depicted in a different perspective. The two networks are jointly viewed as a two-layer multiplex that can be reduced to a single-layer network by employing the similarity network fusion (Wang et al., 2012) and then analysed through community detection to highlight groups of publications sharing a common conceptual base. This process could be easily extended from single publications to authors’, institutions’ or countries’ publications. The caveat to this approach is that the conceptual structure is encompassed in the publications × publications network, making it impossible to overview the different topics/concepts developed by scholars in the given scientific domain. Moreover, the metadata (the cited references, in this case) are used to enrich the clustering procedure on the collection, limiting the possibility of comparing the conceptual structures of different actors. Rafols et al. (2010) have explored the latter task, proposing to create an overall conceptual map (based on subjects’ bibliographic coupling) and compare the conceptual maps of single institutions or other actors/entities to this structure. This strategy also has a primary caveat, related to the non-use of the textual content to define the conceptual structure. Furthermore, all the mentioned techniques produce maps that can be very hard to read and interpret with increasingly complex conceptual structures, requiring additional algebraic and graphical tools to highlight the issues discussed in the reference domain.

Starting from the existing literature, we aim to propose a novel strategy for comparing the conceptual structures of different actors/entities, segmented by one or more characteristics held by metadata, leveraging the textual information encompassed in related scientific publications. Following the approaches commonly used in a scientometric framework, we referred to the thematic analysis approach described in “Problem definition and analytical strategy” Sect., updating the typical strategic diagram representation. The proposed approach aims to provide a joint representation of the different conceptual structures related to the actors/entities of interest rather than a global representation depicting the overall conceptual structure. In this way, it is possible to appreciate how the different actors/entities discussed the research themes and which are their research frontiers, evaluating similarities and differences that can help in assessing the scientific development in a given field or issue. The metadata attached to each indexed publication can be used to segment the analysed dataset into different subsets. The strata can be increasingly complex by adding more metadata (i.e., encompassing more information ), providing insights with varying levels of granularity following the research questions or objectives of investigators.

Given a certain qualitative characteristic X with M modalities that can be observed on the n analysed publications, it is possible to build a n-dimensional vector x whose generic element xi = m indicates that a modality m (with m = 1,…,M) has been observed for a document di. The vector x can also be represented as a complete disjunctive matrix X with n rows and M columns. In this case, each column can be seen as a dummy variable cm containing 1 for publications belonging to the m-th category and 0 for the other ones. The matrix product X F allows obtaining a M × p matrix F̃ whose generic element f̃mj represents the importance of term tj in the group of publications belonging to the m-th category (Fig. 2). It is possible to perform on F̃ the strategy previously described, looking at the concepts/topics emerging from groups of publications.

Alternatively, it is possible to use the vector x as an index for splitting F in M submatrices on which performing the co-word analysis separately. Each submatrix has the same number of columns, considering a common vocabulary of p terms, and a number of rows

![image 2](Aria et al._2024_Comparative science mapping a novel conceptual structure analysis with metadata_images/imageFile2.png)

- Fig. 2 Documents × terms matrices incorporating metadata on documents


nm equal to the number of publications belonging to the m-th category (Fig. 2). The result can also be obtained by the matrix product F, where has n rows and nm columns and each column consisting of a 1 in the row corresponding to the column to pick out and

- 0 everywhere else. The vocabulary can be seen as the union of the single vocabularies related to the different groups of publications. The idea is that the conceptual structure of each category is analysed separately, focusing on the related scientific production. For example, it is possible to examine the conceptual structure of different authors, institutions or countries, starting from the corresponding documents × terms matrices. The approach mentioned above has been used, for example, to compare the conceptual structure emerging from the scientific production of Italian university hospitals (Cuccurullo et al., 2022) or to highlight similarities and differences in Business Administration’s research areas and themes among Italian universities based on their geographical localisation (Cuccurullo et al., 2022b).


Let us consider M binary submatrices containing the presence/absence of p terms

in a group of publications nm referred to a category m (e.g., an author, an institution, a country). From each , it is possible to build a co-occurrence matrix =

containing the counts of how many categories jointly use couples of terms. As above, the co-occurrence of two terms tj and tj into the nm publications may also be expressed as the association strength ASm,jj . Each can be seen as an undirected weighted adjacency matrix depicted by a graph Gm. The isolated nodes of these graphs (i.e., nodes with a degree equal to 0) represent the terms not present in the specific vocabulary of the m-th category and can be removed. On each Gm, a community detection procedure can be employed to uncover the Km concepts/topics forming the conceptual structure of the m-th category.

The concepts/topics obtained through community detection can be visualised in the M strategic diagrams, which separately describe the conceptual structures of the different categories. On the other hand, for comparative purposes, it is possible to plot the M conceptual structures in a unified representation jointly considering the Km concepts/topics related to each category m. To obtain this peculiar plot, the Km values of centrality and density related to the subgraphs composing the conceptual structures of the m-th category are standardised, then a reverse rank transformation is applied to the K = ⋃

m Km values of centrality and density related to all the subgraphs together. If the interest is in the evolution of conceptual structures across years, the analysis and the subsequent joint plot can be repeated for different time slices. A detailed toy example is provided in the supplementary materials to allow a better understanding of how the proposed strategy works.

In the following, our strategy based on the conceptual structure analysis with metadata is applied to oncological research in Italy, focusing on the scientific publications produced by the so-called Institutes for Research, Hospitalisation and Healthcare (IRCCS), qualified institutions of national relevance that pursue scientific research closely connected with hospitals and care services.

# Thematic atlas of the Italian oncological research

Health research is considered one of the key elements and an integral part of the complex activities carried out by the National Health Service. Health research aims to continuously improve assistance, care, and services to significantly increase citizens’ quality of life and meet their well-being expectations. In addition to increasing scientific knowledge, a good research activity significantly impacts researchers’ cultural and professional growth.

It facilitates indeed entering international networks and enhancing the prestige of the involved institutions. For these reasons, analysing scientific production and its impact becomes indispensable. In Italy, public institutions dealing with health research are known as Academic Medical Centres (AMCs), distinguished into three categories: University Hospitals (AOU), former University Hospitals operated by the National Health Service (AOU-SSN), and Institutes for Research, Hospitalisation and Healthcare (IRCCS).

To explore the effectiveness of the proposed strategy, here we focus on a specific type of Italian AMCs, the IRCCS. The institutions are qualified as of national relevance, endowed with financial autonomy and legal personality. The Italian Ministry of Health grants the ‘IRCCS’ denomination to a few institutions, and their activities are regulated by a Legislative Decree (D.Lgs. 288/2003). They are a benchmark for the whole public health system, both for the quality of patient care and the innovation in the field of healthcare management. Moreover, IRCCS drive high-quality clinical assistance in close connection with research activities in the biomedical field, mainly clinical and translational. The activity of IRCCS relates to well-defined research areas, receiving recognition for a single specialised area (monothematic IRCCS) or for multiple integrated areas (polythematic IRCCS).

Among the different IRCCS, we considered the nine public institutions specialising in oncology (Table 1) and their related scientific production. Of those, 6 are monothematic research institutions, whereas the other 3 are polythematic research institutions. The goal is to produce a thematic atlas, explicitly considering the Italian public institutions concerned by this crucial biomedical field.

In the proposed case study, the metadata used in the analysis refers only to the authors’ affiliation, allowing a comparison of the research frontiers of the different public institutions involved in oncological research. Alternatively, it could be interesting to compare public and private institutions’ research or take into account their geographical localisation, or combine the two aspects to evaluate how the different issues have been developed by public/private institutions located in different parts of the country.

## Data retrieval and preparation

We retrieved documents from Web of Science (WoS). To identify the publications related to each IRCCS, we searched the institutions by full name, part of the organization’s name,

- Table 1 List of public IRCCS involved in oncological research


ID Institution Abbreviation Type*

- 1 Centro Riferimento Oncologico CRO AV M
- 2 Centro Riferimento oncologico Basilicata CROB RI M
- 3 Fondazione Ca’Granda - Ospedale Maggiore Policlinico CA GRANDA MI P
- 4 Fondazione IRCCS Istituto Nazionale Tumori FND MI M
- 5 Istituti fisioterapici ospitalieri - Istituto Regina Elena IRE RO P
- 6 Istituto Nazionale Tumori Fondazione Pascale PASCALE NA M
- 7 Istituto Oncologico Veneto IOV VE M
- 8 Istituto Tumori Giovanni Paolo II PAOLOII BA M
- 9 Ospedale Policlinico San Martino MARTINO GE P


M = monothematic, P = polythematic

or its commonly known abbreviation from the Organisations-Enhanced List available on WoS (e.g., ‘IRCCS FND MILANO’ for the Fondazione IRCCS Istituto Nazionale Tumori Milano).

The identification of records included in the collection, along with all inclusion/ exclusion criteria used to refine it, are summarized in Fig. 3 by the PRISMA diagram (Moher et al., 2009).

We selected all documents published from 2000 to 2019, including only articles, proceedings papers, review articles, and book chapters written in English. A total of 45,320 records were initially identified. We then imported the whole collection and converted it into a data frame using the R library bibliometrix, an open-source tool for quantitative research in scientometrics and bibliometrics that includes all the primary methods for performance analysis and science mapping (Aria & Cuccurullo, 2017). For the polythematic IRCCS, we identified only the publications dealing with oncological topics, filtering the records by the Research Areas metadata (SC field).

To consider the publications that have a significant impact in the field of oncological research, we calculated the normalised citation score (NCS) (Waltman et al., 2011):

cti⋆ ∑

⋆

NCS(ct (4)

i ) =

i t=t⋆ cti∕n

where cti⋆ is the citation count of paper i at time t⋆, n is the total number of papers published at time t⋆. Basically, it is calculated as the ratio of the total citation count of each

publication appearing in a given time and the average citation count of all the publications appearing in the same period. When NCS is equal to 1, the output performs just as the global citation average of all the analysed publications, whereas for values greater than 1, the output is more cited than the other publications (Colledge, 2017). We analysed only the publications with an NCS greater than the third quartile (75%) of the corresponding distribution at t⋆ = 2019, obtaining a collection of 5,686 publications for the conceptual structure analysis. Figure 4 shows the distribution of the top 25% NCS publications per institution.

To highlight the main research areas and topics of IRCCS’ oncological research and evaluate their evolution across time, we divided our time span (2000–2019) into three

![image 3](Aria et al._2024_Comparative science mapping a novel conceptual structure analysis with metadata_images/imageFile3.png)

- Fig. 3 PRISMA flow diagram


![image 4](Aria et al._2024_Comparative science mapping a novel conceptual structure analysis with metadata_images/imageFile4.png)

- Fig. 4 Top 25% NCS publications per institutions (2000–2019)


slices, 2000–2006, 2007–2013 and 2014–2019. The results presented in the following take into account this temporal breakdown. A more extensive insight into the oncological research carried out by public IRCCS can be found in Cuccurullo et al. (2023).

## Main results

- Table 2 shows the distribution of the selected publications per IRCCS in the three different periods. The total number of publications of each IRCCS, as explained in “Data retrieval and preparation” Sect., counts only articles, reviews, proceedings papers, and book chapters. The percentage change of produced publications (Δ%) was measured considering the number of publications of the reference sub-period compared to the previous one.


Table 2 Publication distributions per IRCCS in the three time slices ID IRCCS 2000–2006 2007–2013 2014–2019

n % n % Δ% n % Δ%

- 1 CRO AV 175 28.8 186 30.7 6.3 246 40.5 32.3
- 2 CROB RI 11 6.5 65 38.5 491 93 55.0 43.1
- 3 CA GRANDA MI 48 18.6 73 28.3 52.1 137 53.1 87.7
- 4 FND MI 466 22.4 753 36.2 61.6 861 41.4 14.3
- 5 IRE RO 121 31.3 140 36.3 15.7 125 32.4 − 10.7
- 6 PASCALE NA 147 18.8 265 34.0 80.3 368 47.2 38.9
- 7 IOV VE 97 13.1 338 45.4 248.5 309 41.5 − 8.6
- 8 PAOLOII BA 16 6.5 59 24.1 268.8 170 69.4 188.2
- 9 MARTINO GE 147 35.2 135 32.4 − 8.2 135 32.4 0.0


Most of the IRCCS increased their research activity over time. In particular, from 2000–2006 to 2007–2014, the productivity of IOV VE and PAOLOII BA more than tripled, while the productivity of CROB RI almost quintupled. During the same period, the productivity of MARTINO GE fell by 8.2% with respect to the previous subperiod, remaining constant at the same level in 2014–2019. In this latter subperiod, the productivity of PAOLOII BA continued to increase, even if at a lower rate than in the previous subperiod. Conversely, the productivity of IRE RO and IOV VE decreased in the same years by 10.7% and 8.6%, respectively.

Figures 5, 6, and 7 show the overall strategic diagrams of IRCCS’ oncological research for each evaluated time slice, considering the classical approach of thematic analysis described in “Problem definition and analytical strategy” Sect. Research focused on foundational themes in cancer biology and treatment in the first subperiod (Fig. 5). In the early 2000s, the high density and centrality of carcinoma and breast cancer show that oncology was heavily oriented towards understanding tumour biology and improving treatment strategies, particularly for prevalent cancers like breast cancer. Topics like expression and in vitro in the lower-right quadrant indicate their relevance but lesser maturity, suggesting that these were emerging areas of interest during the period. The topic expression, referring to gene expression studies, was central, highlighting the early stages of molecular biology’s growing influence in cancer research. The lower-left quadrant contains emerging topics such as reconstruction, anesthesia, and polymorphisms, which had limited centrality and development at this stage. The thematic focus shifts towards more translational and patientcentred research in the next time slice (Fig. 6). Stem-cell transplantation and colon cancer move into the motor themes quadrant, highlighting advancements in treatments based on cellular therapies and a focus on specific cancer types. The increasing emphasis on personalised and stem-cell-based therapies aligns with broader trends in oncology at the time. Survival and risk are key themes, indicating an increasing interest in patient outcomes and survivorship. Expression remains highly relevant but moves towards being a basic issue, showing that expression, while still central, became a mature area of research. Overall, this period reflects a growing emphasis on personalised medicine and the long-term impacts of treatment. In the last subperiod (Fig. 7), the focus further shifts toward survivorship, patient outcomes, and the application of innovative therapies. Topics like survival, qualityof-life, and risk become central and transversal, reflecting the maturation of patient-centred research. Oncological research is increasingly concerned with treating cancer and its broader implications for patients’ well-being after treatment. Meanwhile, topics such as b-cell lymphoma, lung cancer, and diagnosis show that research into specific cancer types and their early detection continues to be relevant. Niche research on genetic susceptibility and chronic myelogenous leukemia appears well-developed but not central to the broader oncology research, suggesting increasing focus on genetic markers and specialised cancer subtypes.

As explained above, the classic thematic analysis offers an interesting overview of the oncological research but is unable to highlight the contributions and the pecularities of the single institutions. Figures 8, 9, and 10 show the joint strategic diagrams of IRCCS’ oncological research for each time slice, allowing a comparison of the different research strands. To make the plots’ reading more precise, it is worth noting that each represented concept/ topic is labelled with its most frequent term (among the terms belonging to the corresponding subgraph). The dimension of each concept/topic dot is proportional to the occurrence of the characterising keywords, and it is logarithmically rescaled to compare the conceptual structures of the institutes better. In the presented time slices, IRCCS scientific production is rich and varied, sharing, however, three main concepts/topics: expression, survival,

![image 5](Aria et al._2024_Comparative science mapping a novel conceptual structure analysis with metadata_images/imageFile5.png)

#### Thematic Atlas of oncological research in 2000–2006Fig. 5

![image 6](Aria et al._2024_Comparative science mapping a novel conceptual structure analysis with metadata_images/imageFile6.png)

#### Thematic Atlas of oncological research in 2007–2013Fig. 6

![image 7](Aria et al._2024_Comparative science mapping a novel conceptual structure analysis with metadata_images/imageFile7.png)

#### Thematic Atlas of oncological research in 2014–2019Fig. 7

![image 8](Aria et al._2024_Comparative science mapping a novel conceptual structure analysis with metadata_images/imageFile8.png)

#### Thematic Atlas of IRCCS research in 2000–2006Fig. 8

![image 9](Aria et al._2024_Comparative science mapping a novel conceptual structure analysis with metadata_images/imageFile9.png)

#### Thematic Atlas of IRCCS research in 2007–2013Fig. 9

![image 10](Aria et al._2024_Comparative science mapping a novel conceptual structure analysis with metadata_images/imageFile10.png)

#### Thematic Atlas of IRCCS research in 2014–2019Fig. 10

and chemiotherapy. In the first subperiod (Fig. 8), expression was a basic issue for many IRCCS but was a motor issue for IRE RO. In addition, the position of this concept/topic has changed over the years. In the second subperiod (Fig. 9), expression became a motor theme for many IRCCS and started shifting from the upper-right quadrant to the lowerright quadrant in the subsequent subperiod (Fig. 10), consolidating its role as a traditional issue.

Since 2007, studies have started focusing on the survival concept/topic, appearing as an emerging issue in the lower-left quadrant. In the third subperiod, survival became a traditional issue for many IRCCS, denoting greater attention to patients’ healthcare.

Concerning chemiotherapy, it is another issue treated by many IRCCS across time, always positioned on the right side of the map—higher rank centrality—in the different time slices. From the second to the third subperiod, the issue shifted from the upper-right quadrant to the lower-right quadrant, becoming a basic issue.

We observed that niche issues (in the upper-left quadrant) increased over time, meaning that from 2000 to 2019 IRCCS’s oncological research was oriented towards more specialised studies.

# Discussion and final remarks

In this paper, we analysed the research positioning of the different Italian public IRCCS specialising in oncological research. IRCCS often serve as a hub for innovation in healthcare, pioneering new treatments and approaches to patient care. They are involved in clinical trials and may offer patients access to experimental therapies as part of research studies. Because of their close connection to medical schools and educational programs, students and trainees often work alongside experienced healthcare providers, engaging in what is known as a cognitive apprenticeship where they observe, practice, and master clinical skills in a real-world environment. To carry out this bibliometric study, trying to depict the cancer research landscape in Italy, we proposed a new analytical strategybased on co-word analysis—that takes into account the metadata available in the indexing database of scientific publications together with their textual content. Bibliometrics can help track the performance of research investments across time, ensuring accountability and enabling adjustments to strategies as needed based on measurable outcomes, and reveal equipment and facilities heavily used across various research issues, informing decisions on infrastructure investments that would benefit multiple research groups or fields. Employing this novel approach, we identified the different research fronts of IRCCS and visualised them in a joint representation, able to show the significant research issues and specialisations from a comparative perspective.

## Theoretical contributions

Co-word analysis has a long history in bibliometrics, starting from the works of Callon’s research group. It leverages the possibility of representing textual data as relational data, diagrammatically depicted as graphs and analysed with network-based approaches, with the goal of bringing out the conceptual structure of a scientific field. Nevertheless, focusing on the text encompassed in bibliographic records, science mapping techniques typically leave aside helpful information about who produced the publications (at a micro, meso and macro level, considering the authors, the involved institutions and countries, respectively),

when publications have been issued and other valuable aspects such as the cited references, essential to define the social and intellectual structure. Incorporating these metadata can help better understand the conceptual framework, helping discriminate the areas and topics covered by different sources or, in this case, by various institutions.

As in other unsupervised approaches proposed in bibliometrics, the proposed strategy is data-driven, relying only on the data listed in the bibliographic set retrieved from an indexing database. In dealing with textual data, employing other techniques to detect the concepts/topics expressed in the analysed textual body is possible. Factorial-based techniques such as Correspondence Analysis (Cuccurullo et al., 2016) or probabilistic approaches such as Latent Dirichlet Allocation (Suominen & Toivanen, 2016; Cheng et al., 2022) can be considered as an alternative. On one side, these solutions allow to consider covariates (e.g., Chen et al., 2020), but at the same time, they share a known shortcoming caused by the bag-of-words encoding that underlies the algebraic representation of publications as vectors. The use of term co-occurrences and terms × terms adjacency matrices can be seen as a trivial form of embedding able to incorporate the semantic structure of text and the contextual information of terms’ use. The new frontier offered by more complex embedding techniques taking into account the context (e.g., Hu et al., 2019; Shibayama et al., 2021) and the possibility of using supervised (or semi-supervised) approaches leveraging large language models (e.g., Gupta et al., 2024; Karabacak & Margetis, 2024), could represent in the future a standard also for bibliometric analyses, but carrying with him the problems concerning explainability and interpretability typical of deep learning approaches.

The strategy based on co-word analysis and enriched with the visualisation offered by the strategic diagram was firstly proposed for synchronic analyses and then extended for longitudinal studies with a diachronic perspective able to consider the evolution across years of research issues. The possibility of performing cross-sectional studies—introducing the related metadata in the textual data analysis of publications—allows for enhancing the informative power of strategic diagrams, which have an overview of multiple conceptual frameworks at the same time. Thanks to the possibility of joining the single plots in one representation, it is possible to gain insight into the conceptual structure of a specific player whilst also comparing the different conceptual structures.

## Practical implications

Science mapping (and bibliometrics) tools are more and more strategic both for academic institutions and policymakers, as well as for the other stakeholders interested in science advancement because they set an automatic quantitative approach that is able to analyse and visualise the landscape of scientific research systematically. The analytical strategy presented here, in particular, may be seen as a useful decision-support tool for the different players involved in the healthcare system. Comparing conceptual structures across institutions and countries aids policymakers in determining developing positions and identifying areas where additional support is needed.

From a managerial viewpoint, identifying and visualising the key areas and topics may support better budgeting and allocation of resources, including funds, personnel, and infrastructure. Policymakers can use science mapping and bibliometrics to inform decisions regarding research funding investments and strategic planning for scientific advancement, shaping science and technology policies that support promising research fields, and allocating resources to areas with higher potential of impact or where there is

a national strategic interest (Morciano et al., 2020). The joint visualisation of conceptual structures offers a means to demonstrate the effectiveness of these investments and solid evidence to formulate and justify public policies. By using this strategy, policymakers can develop more thoughtful, data-driven strategies for shaping the direction of scientific research, enhancing the nation’s competitiveness, innovation, and scientific leadership (Celis & Gago, 2014).

From a ‘more scientific’ viewpoint, the joint visualisation can reveal critical players, institutions, and countries (depending on the metadata used to produce the segmentation of the knowledge base) that are leading in specific research areas or topics. By understanding research fronts and trends, academic institutions can develop strategic plans that align with emerging areas of interest or strength. This information is also vital for finding potential collaborators, establishing partnerships, and creating networks of centres involved in research on specific issues. On the other hand, policymakers can leverage this information to encourage interdisciplinary and inter-institutional research, improving the effectiveness of outcomes.

The two perspectives above are also of interest to the industry, the third actor with the University and the Government of the ‘triple-helix’ model (Cesaroni & Piccaluga, 2016). An overview of research fronts can point out the key sectors and determine the direction of private investments in research, clearly with a standpoint more oriented to business development rather than the public interest, but valuable to enhance the progress of diagnostic devices and drugs that can both improve prevention as well as care actions (Abramo & D’Angelo, 2009; Robbiano, 2022).

## Limitations and future developments

The analytical strategy presented here may allow different levels of detail, depending on stakeholders’ information needs. The application to Italian oncological research made by public IRCCS, showed the potential of our approach. Nevertheless, the study has some limitations, both methodologically and empirically.

The proposed strategy relies on the vector space model and implicitly on the bag-ofwords encoding. Even if it is possible to perform the co-word analysis on each textual field available for the bibliographic dataset, the results may substantially differ using keywords or the publications’ abstract. In the latter case, many terms are part of the common language used to summarise a study and are low informative (e.g., data, method, analysis), but in a general perspective the longest content allow to discriminate the meaning of terms semantically. To leverage the context, it is necessary to algebraically represent terms (and publications) in an embedded form. As stated above, adjacency matrices could be a simple version of embedding that is useful in keyword analysis, but other more complex algebraic models could be necessary for abstract analysis. A second drawback concerns the community detection step, relying on the Louvain algorithm. As reported, some authors showed its significance in analysing large networks. On the other hand, according to some other authors, the greedy optimisation performed by this approach can create problems with respect to the quality of individual communities (Barroso et al., 2022). The Louvain algorithm can fail to detect small communities due to its resolution limit, which can unjustifiably merge smaller subgraphs into larger ones. Moreover, the method tends to find locally optimal partitions but does not guarantee a global optimum in community detection. In some cases, other community detection methods might be more appropriate depending on the goals of the analysis and the resolution required. At the same time, the temporal

dimension can be considered in the algorithm (Seifikar et al., 2020) instead of performing repeated community detection for each different time slice and linking the concepts/topics afterwards to track their evolution.

Concerning the case study of Italian oncological research, we limited our dataset both temporally (only 2000–2019 publications have been considered) and extensively (only the publications with a top 25% NCS value have been considered). Cancer research is in continuous evolution, both in investigating causes (e.g., discovery of new carcinogens) and development mechanisms and treating different kinds of tumours. Clearly, the analysis performed can track only the major areas and does not allow acknowledgement of pioneering studies on particular issues investigated by some researchers or centres. Another aspect to consider is that the strategy offers a comparative overview of the conceptual structures emerging from the different research activities carried out by the IRCCS, but is not able to assess, for example, the clinical success of the various proposals and experimentations. The question of how to measure and optimise the returns from investment in health and medical research is a highly policy-relevant issue. Our approach may be useful in identifying the different research strands, but other kinds of analyses must be performed to measure the research impact of academic medical institutions, stated that bibliometric analyses have to carefully considered in this context (Akcan et al., 2013).

Future developments will be devoted to developing the strategy by considering several aspects. Concerning data representation, other measures for terms’ co-occurrence will be tested to incorporate as much contextual information as possible. Simultaneously, we will improve the community detection step, considering static as well as dynamic approaches to deal with the temporal dimension in a diverse manner. Finally, we will focus on the graphical representation, operating on the labelling side (to enhance the readability of concepts/topics and link them, for example, with the leading keywords used in the domain) and on the graphical side, trying to make more straightforward the comparison of conceptual structures.

Supplementary Information The online version contains supplementary material available at https://doi. org/10.1007/s11192-024-05161-6.

Author contributions Conceptualisation of the work: M. Aria, C. Cuccurullo. Data collection: L. D’Aniello. Data analysis and interpretation: M. Aria, L. D’Aniello, M. Spano. Original draft preparation: M. Misuraca, M. Spano. Review and editing: M. Misuraca, M. Spano. All authors have read and agreed to the published version of the manuscript.

Funding Open access funding provided by Università degli Studi di Napoli Federico II within the CRUICARE Agreement. This study was supported by the research projects: PRIN-2022 ‘SCIK-HEALTH’ (Project Code: 2022825Y5E; CUP: E53D2300611006); PRIN-2022 PNRR ‘The value of scientific production for patient care in Academic Health Science Centres’ (Project Code: P2022RF38Y; CUP: E53D23016650001).

Data availibility The dataset used and analysed in the present study is available from the corresponding author upon reasonable request.

# Declarations

Conflict of interest The authors have no Conflict of interest to declare that are relevant to this article’s content. Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the

material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.

# References

Abramo, G., & D’Angelo, A. (2009). The alignment of public research supply and industry demand for effective technology transfer: the case of Italy. Science and Public Policy, 36(1), 2–14. Akcan, D., Axelsson, S., Bergh, C., Davidson, T., & Rosén, M. (2013). Methodological quality in clinical trials and bibliometric indicators: No evidence of correlations. Scientometrics, 96(1), 297–303. Aria, M., Misuraca, M., & Spano, M. (2020). Mapping the evolution of social research and data science on 30 years of social indicators research. Social Indicators Research, 149(3), 803–831. Aria, M., & Cuccurullo, C. (2017). bibliometrix: An R-tool for comprehensive science mapping analysis. Journal of Informetrics, 11(4), 959–975.

Aria, M., Cuccurullo, C., D’Aniello, L., Misuraca, M., & Spano, M. (2022). Thematic analysis as a new culturomic tool: The social media coverage on Covid-19 pandemic in Italy. Sustainability, 14(6), 3653.

Baccini, A., Baccini, F., Barabesi, L., Cioni, M., Petrovich, E., & Pignalosa, D. (2024). Fine-grained classification of journal articles based on multiple layers of information through similarity network fusion: The case of the Cambridge journal of economics. Scientometrics, 129(1), 373–400.

Barroso, M., Gómez, D., Gutiérrez, I. (2022). A supervised approach to community detection problem: How to improve louvain algorithm by considering fuzzy measures. C. Kahraman, A.C. Tolga, S.C. Onar, S. Cebi, B. Oztaysi, and I.U. Sari (Eds.), Intelligent and fuzzy systems: Digital acceleration and the new normal—proceedings of the infus 2022 conference (pp. 219–227). Springer.

Blei, D. M., Ng, A. Y., & Jordan, M. I. (2003). Latent Dirichlet allocation. Journal of Machine Learning Research, 3, 993–1022. Blondel, V. D., Guillaume, J.-L., Lambiotte, R., & Lefebvre, E. (2008). Fast unfolding of communities in

large networks. Journal of Statistical Mechanics: Theory and Experiment, 2008(10), P10008. Börner, K. (2010). Atlas of science: Visualizing what we know. MIT Press. Börner, K., Chen, C., & Boyack, K. (2003). Visualizing knowledge domains. Annual Review of Information

Science and Technology, 37, 179–255. Cahlik, T. (2000). Search for fundamental articles in economics. Scientometrics, 49(3), 389–402. Callon, M., Law, J., & Rip, A. (1986). Qualitative scientometrics. In M. Callon, J. Law, & A. Rip (Eds.),

Mapping the dynamics of science and technology: Sociology of science in the real world (pp. 103– 123). Palgrave Macmillan.

Callon, M., Courtial, J. P., & Laville, F. (1991). Co-word analysis as a tool for describing the network of interactions between basic and technological research—The case of polymer chemistry. Scientometrics, 22(1), 155–205.

Callon, M., Courtial, J. P., Turner, W. A., & Bauin, S. (1983). From translations to problematic networks: An introduction to co-word analysis. Social Science Information, 22(2), 191–235. Carley, K. M. (1997). Network text analysis: The network position of concepts. In C. W. Roberts (Ed.), Text

analysis for the social sciences (pp. 79–102). Lawrence Erlbaum Associates. Celis, J. E., & Gago, J. M. (2014). Shaping science policy in Europe. Molecular Oncology, 8(3), 447–457. Cesaroni, F., & Piccaluga, A. (2016). The activities of university knowledge transfer offices: Towards the

third mission in Italy. The Journal of Technology Transfer, 41(4), 753–777. Cheng, X., Cao, Q., & Liao, S. S. (2022). An overview of literature on COVID-19, MERS and SARS: Using text mining and latent Dirichlet allocation. Journal of Information Science, 48(3), 304–320.

Chen, X., Zou, D., Cheng, G., & Xie, H. (2020). Detecting latent topics and trends in educational technologies over four decades using structural topic modeling: A retrospective of all volumes of computers & education. Computers & Education, 151, 103855.

Clauset, A., Newman, M. E. J., & Moore, C. (2004). Finding community structure in very large networks. Physical Review E, 70(6), 066111.

Cobo, M. J., López-Herrera, A. G., Herrera-Viedma, E., & Herrera, F. (2011). An approach for detecting, quantifying, and visualizing the evolution of a research field: A practical application to the fuzzy sets theory field. Journal of Infometrics, 5(1), 146–166.

Cobo, M. J., López-Herrera, A. G., Herrera-Viedma, E., & Herrera, F. (2011). Science mapping software tools: Review, analysis, and cooperative study among tools. Journal of the American Society for Information Science and Technology, 62(7), 1382–1402.

Colledge, L. (2017). Snowball metrics recipe book(Tech. Rep.). Snowball Metrics Project.

Coulter, N., Monarch, I., & Konda, S. (1998). Software engineering as seen through its research literature: A study in co-word analysis. Journal of the American Society for Information Science, 49(13), 1206–1223.

Cuccurullo, C., Aria, M., & Sarto, F. (2016). Foundations and trends in performance management: A twenty-five years bibliometric analysis in business and public administration domains. Scientometrics, 108(2), 595–611.

Cuccurullo, C., Aria, M., Spano, M., & D’Aniello, L. (2023). Leading change in academic health science centers. Zaccaria.

Cuccurullo, C., D’Aniello, L., Aria, M., & Spano, M. (2022). Thematic evolution of academic medical centers’ research: A focus on Italian public-owned Aous in metropolitan areas. In R. Lombardo, I. Camminatiello, & V. Simonacci (Eds.), Innovation and society 50: Statistical and economic methodologies for quality assessment, book of short papers ies2022 (pp. 67–72). PKE.

Cuccurullo, C., D’Aniello, L., & Pizzo, M. (2022). Mapping evolutionary paths of a society: The longitudinal analysis of the Italian Economia Aziendale. In A. Balzanella, M. Bini, C. Cavicchia, & R. Verde (Eds.), Book of short papers: 51st scientific meeting of the Italian statistical society (sis2022) (pp. 786–792). Pearson.

De Nito, E., Gentile, T. A. R., Köhler, T., Misuraca, M., & Reina, R. (2023). E-learning experiences in tertiary education: Patterns and trends in research over the last 20 years. Studies in Higher Education, 48(4), 595–615.

Di Maio, M., Perrone, F., & Conte, P. (2019). Real-world evidence in oncology: Opportunities and limitations. The Oncologist, 25(5), 746–752. Ding, Y., Chowdhury, G. G., & Foo, S. (2001). Bibliometric cartography of information retrieval research by using co-word analysis. Information Processing & Management, 37(6), 817–842.

Esfahani, K., Roudaia, L., Buhlaiga, N., Del Rincon, S. V., Papneja, N., & Miller, W. H. (2003). A review of cancer immunotherapy: From the past, to the present, to the future. Current Oncology, 27(s2), 87–97.

Fortunato, S. (2010). Community detection in graphs. Physics Reports, 486(3–5), 75–174. Furstenau, L. B., Rodrigues, Y. P. R., Sott, M. K., Leivas, P., Dohan, M. S., López-Robles, J. R., &

Choo, K.-K.R. (2023). Internet of things: Conceptual network structure, main challenges and future directions. Digital Communications and Networks, 9(3), 677–687.

Girvan, M., & Newman, M. E. J. (2002). Community structure in social and biological networks. Proceedings of the National Academy of Sciences, 99(12), 7821–7826. Gupta, P., Ding, B., Guan, C., & Ding, D. (2024). Generative AI: A systematic review using topic modelling techniques. Data and Information Management, 100066.

Halpern, M. T., Viswanathan, M., Evans, T. S., Birken, S. A., Basch, E., & Mayer, D. K. (2015). Models of cancer survivorship care: Overview and summary of current evidence. Journal of Oncology Practice, 11(1), 19–27.

Hamers, L., Hemeryck, Y., Herweyers, G., Janssen, M., Keters, H., Rousseau, R., & Vanhoutte, A.

(1989). Similarity measures in scientometric research: The Jaccard index versus Salton’s cosine formula. Information Processing & Management, 25(3), 315–318.

Healey, P. (1991). Researching planning practice. The Town Planning Review, 62(4), 447–459. Healey, P., Rothman, H., & Hoch, P. K. (1986). An experiment in science mapping for research planning.

Research Policy, 15(5), 233–251.

Hu, K., Luo, Q., Qi, K., Yang, S., Mao, J., Fu, X., & Zhu, Q. (2019). Understanding the topic evolution of scientific literatures like an evolving city: Using google word2vec model and spatial autocorrelation analysis. Information Processing & Management, 56(4), 1185–1203.

James, P. (1992). Knowledge graphs. In R. van der Riet & R. Meersman (Eds.), Linguistic instruments in knowledge engineering (pp. 97–117). Elsevier.

Janssens, F., Zhang, L., Moor, B. D., & Glä"nzel, W. (2009). Hybrid clustering for validation and improvement of subject-classification schemes. Information Processing & Management, 45(6), 683–702.

Karabacak, M., & Margetis, K. (2024). Natural language processing reveals research trends and topics in the spine journal over two decades: A topic modeling study. The Spine Journal, 24(3), 397–405. Khozin, S., Blumenthal, G. M., & Pazdur, R. (2017). Real-world data for clinical evidence generation in oncology. JNCI: Journal of the National Cancer Institute, 109(11), djx187. Leydesdorff, L. (1989). Words and co-words as indicators of intellectual organization. Research Policy, 18(4), 209–223. Leydesdorff, L., & Etzkowitz, H. (1998). The triple helix as a model for innovation studies. Science and Public Policy, 25(3), 195–203.

López-Robles, J. R., Cobo, M. J., Gutiérrez-Salcedo, M., Martínez-Sánchez, M. A., Gamboa-Rosales, N. K., & Herrera-Viedma, E. (2021). 30th anniversary of applied intelligence: A combination of bibliometrics and thematic analysis using SCIMAT. Applied Intelligence, 51(9), 6547–6568.

Mainali, K. P., Slud, E., Singer, M. C., & Fagan, W. F. (2022). A better index for analysis of co-occurrence and similarity. Science Advances, 8(4), eabj9204.

Martínez, M. A., Cobo, M. J., Herrera, M., & Herrera-Viedma, E. (2015). Analyzing the scientific evolution of social work using science mapping. Research on Social Work Practice, 25(2), 257–277. Misuraca, M., & Spano, M. (2020). Unsupervised analytic strategies to explore large document collections. In D. Iezzi, D. Mayaffre, & M. Misuraca (Eds.), Text analytics, advances and challenges (pp. 17–28). Springer Nature.

Misuraca, M., Scepi, G., & Spano, M. (2023). Network-based dimensionality reduction for textual datasets. In E. Brentari, M. Chiodi, & E.-J.C. Wit (Eds.), Models for data analysis (pp. 175–190). Springer Nature.

Moher, D., Liberati, A., Tetzlaff, J., & Altman, D. G. (2009). The PRISMA group–Preferred reporting items for systematic reviews and meta-analyses: The PRISMA statement. PLoS Medicine, 6(7), e1000097.

Morciano, C., Errico, M. C., Faralli, C., & Minghetti, L. (2020). An analysis of the strategic plan development processes of major public organisations funding health research in nine high-income countries worldwide. Health Research Policy and Systems, 18(1), 106.

Noyons, E. C. M., & van Raan, A. F. J. (1998). Advanced mapping of science and technology. Scientometrics, 41(1–2), 61–67. Noyons, E. C. M., Moed, H. F., & van Raan, A. F. J. (1999). Integrating research performance analysis and science mapping. Scientometrics, 46(3), 591–604. Peters, H. P. F., & van Raan, A. F. J. (1991). Structuring scientific activities by co-author analysis. Scientometrics, 20(1), 235–255.

Pons, P., & Latapy, M. (2005). Computing communities in large networks using random walks. In P. Yolum, T. Güngör, F. Gürgen, & C. Özturan (Eds.), Computer and information sciences—ISCIS 2005 (pp. 284–293). Springer.

Rafols, I., Porter, A. L., & Leydesdorff, L. (2010). Science overlay maps: A new tool for research policy and library management. Journal of the American Society for Information Science and Technology, 61(9), 1871–1887.

Rip, A., & Courtial, J.-P. (1984). Co-word maps of biotechnology: An example of cognitive scientometrics. Scientometrics, 6(6), 381–400. Robbiano, S. (2022). The innovative impact of public research institutes: Evidence from Italy. Research Policy, 51(10), 104567. Rosvall, M., & Bergstrom, C. T. (2008). Maps of random walks on complex networks reveal community

structure. Proceedings of the National Academy of Sciences, 105(4), 1118–1123. Salton, G., & McGill, M. (1983). Introduction to modern information retrieval. McGraw-Hill. Salton, G., Wong, A., & Yang, C. S. (1975). A vector space model for automatic indexing. Communica-

tions of the ACM, 18(11), 613–620. Seifikar, M., Farzi, S., & Barati, M. (2020). C-Blondel: An efficient Louvain-based dynamic community detection algorithm. IEEE Transactions on Computational Social Systems, 7(2), 308–318. Shibayama, S., Yin, D., & Matsumoto, K. (2021). Measuring novelty in science with word embedding. PLoS ONE, 16(7), e0254034. Small, H. (1997). Update on science mapping: Creating large document spaces. Scientometrics, 38(2),

275–293. Sowa, J. (1984). Conceptual structures: Information processing in mind and machine. Addison-Wesley. Sternitzke, C., & Bergmann, I. (2009). Similarity measures for document mapping: A comparative study

on the level of an individual scientist. Scientometrics, 78(1), 113–130.

Suominen, A., & Toivanen, H. (2016). Map of science with topic modeling: Comparison of unsupervised learning and human-assigned subject classification. Journal of the Association for Information Science and Technology, 67(10), 2464–2476.

Traag, V. A., Waltman, L., & Van Eck, N. J. (2019). From Louvain to Leiden: Guaranteeing well-connected communities. Scientific reports, 9, 5233. van Eck, N. J., & Waltman, L. (2007). Bibliometric mapping of the computational intelligence field. International Journal of Uncertainty, Fuzziness and Knowledge-Based Systems, 15(5), 625–645.

van Eck, N. J., & Waltman, L. (2009). How to normalize cooccurrence data? An analysis of some wellknown similarity measures. Journal of the American Society for Information Science and Technology, 60(8), 1635–1651.

van Raan, A. F. J. (2019). Measuring science: Basic principles and application of advanced bibliometrics. In W. Glänzel, H. F. Moed, U. Schmoch, & M. Thelwall (Eds.), Springer handbook of science and technology indicators (pp. 237–280). Springer.

Velez-Estevez, A., García-Sánchez, P., Moral-Munoz, J. A., & Cobo, M. J. (2022). Why do papers from international collaborations get more citations? A bibliometric analysis of library and information science papers. Scientometrics, 127(12), 7517–7555.

Waldmann, T. A. (2003). Immunotherapy: Past, present and future. Nature Medicine, 9(3), 269–277. Waltman, L., van Eck, N. J., van Leeuwen, T. N., Visser, M. S., & van Raan, A. F. J. (2011). Towards a

new crown indicator: Some theoretical considerations. Journal of Informetrics, 5(1), 37–47. Wang, B., Jiang, J., Wang, W., Zhou, Z.-H., & Tu, Z. (2012). Unsupervised metric fusion by cross diffusion. 2012 IEEE conference on computer vision and pattern recognition (pp. 2997–3004). IEEE. Wang, Z.-Y., Li, G., Li, C.-Y., & Li, A. (2012). Research on the semantic-based co-word analysis. Scientometrics, 90(3), 855–875. Yang, Z., Algesheimer, R., & Tessone, C. J. (2016). A comparative analysis of community detection algorithms on artificial networks. Scientific Reports, 6(1), 30750. Zhao, D. (2010). Characteristics and impact of grant-funded research: A case study of the library and information science field. Scientometrics, 84(2), 293–306.

Publisher’s Note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

