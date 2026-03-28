Knowl. Org. 48(2021)No.7/8 
E. Petrovich. 2021. Science Mapping and Science Maps 
535 
Science Mapping and Science Maps † 
Eugenio Petrovich 
Department of Economics and Statistics,  
Piazza San Francesco 7-8, 53100 Siena (Italy),  
<eugenio.petrovich@unisi.it>  
 
Eugenio Petrovich is post-doctoral researcher at the Department of Economics and Statistics of the University of 
Siena. He holds a Master’s degree in Philosophy and a Ph.D. in Philosophy and human sciences, both from the 
University of Milan. His main research interests include quantitative studies of science, research evaluation, philos-
ophy of science, and quantitative history of philosophy. He is member of the Distant Reading and Data-driven 
Research in the History of Philosophy (DR2) network. He has been visiting researcher at the Centre for Science 
and Technology Studies in Leiden and at the Vossius Center for the History of Humanities and Sciences in Am-
sterdam.  
 
Petrovich, Eugenio. 2021. “Science Mapping and Science Maps.” Knowledge Organization 48(7/8): 535-562. 156 
references. DOI:10.5771/0943-7444-7-8-535. 
 
Abstract: Science maps are visual representations of the structure and dynamics of scholarly knowledge. They aim to show how fields, disci-
plines, journals, scientists, publications, and scientific terms relate to each other. Science mapping is the body of methods and techniques that 
have been developed for generating science maps. This entry is an introduction to science maps and science mapping. It focuses on the concep-
tual, theoretical, and methodological issues of science mapping, rather than on the mathematical formulation of science mapping techniques. 
After a brief history of science mapping, we describe the general procedure for building a science map, presenting the data sources and the 
methods to select, clean, and pre-process the data. Next, we examine in detail how the most common types of science maps, namely the citation-
based and the term-based, are generated. Both are based on networks: the former on the network of publications connected by citations, the 
latter on the network of terms co-occurring in publications. We review the rationale behind these mapping approaches, as well as the techniques 
and methods to build the maps (from the extraction of the network to the visualization and enrichment of the map). We also present less-
common types of science maps, including co-authorship networks, interlocking editorship networks, maps based on patents’ data, and geo-
graphic maps of science. Moreover, we consider how time can be represented in science maps to investigate the dynamics of science. We also 
discuss some epistemological and sociological topics that can help in the interpretation, contextualization, and assessment of science maps. 
Then, we present some possible applications of science maps in science policy. In the conclusion, we point out why science mapping may be 
interesting for all the branches of meta-science, from knowledge organization to epistemology. 
 
Received: 15 June 2020; Revised 1 July 2020; Accepted: 26 April 2021 
 
Keywords: science mapping, science maps, visualization, visualization methods 
 
† Derived from the article titled “Science mapping” in the ISKO Encyclopedia of Knowledge Organization, Version 1.1 published 2021-04-
26. Article category: KO in different contexts and applications. 
 
1.0 Introduction 
 
Science maps, also known as scientographs, bibliometric net-
work visualizations, and knowledge domain maps, are visual 
representations of the structure and dynamics of scholarly 
knowledge. They aim to show how disciplines, fields, spe-
cialties, authors, keywords, or publications relate to each 
other (Börner, Chen, and Boyack 2005; Chen 2013; Rafols, 
Porter, and Leydesdorff 2010; Small 1999; Van Raan 2019). 
Science maps are usually generated based on the analysis of 
large collections of scientific documents (Börner 2010; 
Cobo et al. 2011b). 
Science mapping is the body of methods and techniques 
that have been developed to generate science maps. Science 
mapping has a long tradition in bibliometrics and scien-
tometrics, i.e., the quantitative studies of science (Chen 
2017; Van Raan 2019). In the last decades, it has increasingly 
become an interdisciplinary area, witnessing important con-
tributions from data science, where science mapping belongs 
to the larger and increasingly important area of information 
visualization (Börner, Chen, and Boyack 2005).  
Science maps have several applications. They help to an-
swer questions such as: What are the main topics within a cer-
tain scientific domain? How do these topics relate to each 

Knowl. Org. 48(2021)No.7/8 
E. Petrovich. 2021. Science Mapping and Science Maps 
536 
other? How has a certain scientific domain developed over 
time? Who are the key actors (researchers, institutions, jour-
nals) of a scientific field? Science maps help to investigate 
how the structural units of science relate one another at the 
micro and macro level (Leydesdorff 1987), what factors de-
termine the emergence of new scientific fields and the devel-
opment of interdisciplinary areas (Leydesdorff and Gold-
stone 2014), and, more generally, how scientific change func-
tions (Leydesdorff 2001; Lucio-Arias and Leydesdorff 2009). 
At the same time, the information made accessible by science 
maps can be highly relevant for science policy purposes.  
Science maps, and especially the global maps, also known 
as “atlases of science” (see Section 3.2: Field delineation), 
can help to classify the sciences by showing their mutual re-
lationships (e.g., by showing the citation flows between 
fields). In this sense, science maps are useful tools in Knowl-
edge Organization and have been used to build classifica-
tion systems with a bottom-up approach (see e.g., Waltman 
and van Eck 2012). However, standard methods of science 
mapping are not based on and do not result in semantic re-
lationships between categories (e.g., genus-species relation) 
but association measures between units of analysis (e.g., co-
citation strength between publications, or co-authorship as-
sociation between authors). The closest to semantic rela-
tions that can be produced by standard science mapping ap-
proaches is the relation of inclusion obtained by clustering 
techniques, in which higher-order clusters include lower-or-
der clusters (see Section 4.1.5: Enriching the map). Science 
maps, hence, are not meant to replace taxonomies, classifi-
catory schemes, ontologies, and other classic knowledge or-
ganization systems (KOS) (Hjørland 2013; Mazzocchi 
2018). Rather, they can integrate them by providing extra 
information on the structure of science based on the analy-
sis of citation networks and other kinds of scientific net-
works. At the same time, the application of science maps is 
not restricted to Knowledge Organization but extends to 
the sociology of science and science policy. 
 
1.1 Structure of the paper 
 
This article is an introduction to science maps and science 
mapping methodology. It is structured as follows. Section 2 
offers a brief overview of the history of science mapping. 
Section 3 presents the standard workflow behind a science 
map and the preliminary steps of science mapping: data col-
lection, field delineation, data pre-processing, and network 
extraction. Section 4 examines the different types of science 
maps that can be generated from network data. Section 4.1 
is devoted to citation-based maps, i.e., those maps that are 
based on publications (or aggregates of publications) and ci-
tations (or citation-based relations) between publications. 
This section describes in detail some procedures that are 
common also to other science maps, such as the normaliza-
tion of the raw relatedness scores, and the two most diffused 
visualization approaches, the graph-based and the distance-
based. It also presents some techniques that can be used to 
complement the results of mapping and ease the interpreta-
tion of science maps, such as clustering. Section 4.2 dis-
cusses term-based maps, i.e., those maps that are based on 
the analysis of the titles, abstracts, keywords, or biblio-
graphic descriptors of scientific publications. We will first 
present the classic co-word analysis as developed in the soci-
ology of science and then focus on maps based on terms ex-
tracted automatically with Natural Language Processing 
techniques. Section 4.3 briefly overviews science maps 
based on co-authorship and interlocking editorship net-
works, whereas Section 4.4 reviews science maps based on 
patents and geographic maps of science. Section 5 discusses 
different strategies to include the dimension of time into 
science maps. Section 6 is devoted to the last step in the sci-
ence mapping workflow, namely interpretation, and to dis-
cuss some general issues of science mapping, such as the im-
portance of the level of analysis and the applicability of sci-
ence mapping to the humanities. In section 7, some episte-
mological topics, which bridge across science mapping, so-
ciology of science, and philosophy of science are discussed: 
the objectivity of science maps, the relationship between the 
published side of science and the scientific practice, and the 
meaning of citations. Section 8 overviews the potential ap-
plications of science maps in science policy. Lastly, the Con-
clusion will sketch how science mapping may be of interest 
for all the disciplines that compose meta-science. In the Ap-
pendix, two tools currently available for producing science 
maps, CiteSpace and VOSviewer, are briefly reviewed.  
 
1.2 Three caveats about this paper 
 
This entry focuses on conceptual, theoretical, and method-
ological issues of science mapping rather than on the rigor-
ous mathematical formulation of science mapping tech-
niques, as the basic ideas behind the techniques can often be 
understood without reference to the formal machinery. Rel-
evant technical literature will be pointed out in the refer-
ences. 
Secondly, we will focus on the methodology of science 
mapping, rather than on specific exemplars of science maps. 
We aim to provide the readers with the tools to understand 
and independently assess the science maps they will encoun-
ter (or produce!), rather than offer our opinion on existing 
maps. A wonderful collection of science maps can be found 
in the Atlas of Science by Katy Börner (Börner 2010) and in 
the exhibit Places and Spaces: Mapping Science, which pop-
ularizes the topic of science mapping to the large public all 
over the world since 2005.1 
Lastly, science mapping is not a static research field, but 
it is constantly moving forward. New mapping methods are 

Knowl. Org. 48(2021)No.7/8 
E. Petrovich. 2021. Science Mapping and Science Maps 
537 
developed, old algorithms are dismissed, science mapping 
tools are refined, larger maps are built as higher computing 
capacity becomes available. Therefore, it is not uncommon 
to find disagreement in the current science maps literature 
(e.g., Boyack and Klavans 2010). In this article, we will try 
as far as possible to remain neutral concerning these discus-
sions, presenting to the reader the different options without 
taking a position. 
 
2.0 A brief history of science mapping 
 
Modern science mapping relies on the data provided by 
large, multidisciplinary databases that index vast portions of 
the scientific literature (see Section 3.1: Data sources for sci-
ence mapping). Before the creation of these databases in the 
1960s, it was virtually impossible to generate science maps 
in the modern sense. The idea of representing the structure 
of human knowledge by visual aids, however, dates far back 
in history.  
 
2.1 Ancestors of science maps 
 
Already in the Middle Age, the relationships between the 
seven liberal arts, comprising the trivium and quadrivium, 
were visually represented by allegories.2 However, the most 
popular visual metaphor in history for visualizing knowl-
edge has been the tree (Lima 2014). Its origins can be traced 
back to Aristotle, and to the Isagoge, an introduction to Ar-
istotle’s logic written by Porphyry in the III century. In the 
13th century, Ramon Lull depicted a tree of the sciences in 
his Arbor Scientiae (1295). Descartes, in the Principia 
Philosophiae (1644), used the same image to explain the re-
lationship between metaphysics, physics, and the applied 
sciences. During the Enlightenment, the famous Ency-
clopédie of Diderot and D’Alambert contained a tree-like 
taxonomy of human knowledge (Système Figuré des Con-
naissances Humaines). Similar structures can be found also 
in the XIX century, in philosophical treaties on the classifi-
cation and organization of the sciences.3  
 
2.2 Modern science mapping 
 
The tree-like representations of the sciences in the past usu-
ally had a philosophical aim. They served to reflect on the 
most general principles that underlie human knowledge. At 
the same time, they aimed at organizing scientific and schol-
arly disciplines, by creating hierarchies between them. Of-
ten, they were proposed with a normative spirit: more than 
describing the actual organization of knowledge, they 
wanted to reform and improve it. What they all shared was 
a “top-down” approach. Starting from a certain idea of hu-
man knowledge and a certain set of classificatory categories, 
a taxonomy was devised, which was then used to categorize 
the individual items of knowledge, such as books or scien-
tific papers. The Dewey Decimal Classification, a library 
classification system developed in 1876, epitomizes such a 
top-down approach. 
The creation of the Science Citation Index (SCI) in the 
1960s by Eugene Garfield at the Institute for Scientific In-
formation, allowed for a first time a bottom-up approach. 
As we will see better in the next sections (see Section 3.4: 
Network extraction), the SCI indexed the citation-links be-
tween the articles published in scientific journals. In this 
way, it allowed to reconstruct the network in which each sci-
entific article is embedded, and, by connecting all these net-
works, to reconstruct the structure of entire scientific areas. 
In this way, a new method to map human knowledge be-
came possible. The historian of science Derek De Solla Price 
was the first to suggest such an idea in 1965 (Price 1965). 
Garfield himself proposed the method of historiographs to 
reconstruct the temporal development of scientific ideas by 
analyzing the citation links between publications (Garfield 
1973) (see Section 5: The representation of time in science 
mapping).  
In the 1960s and 1970s, two new techniques, both based 
on citations, were developed to measure the association of 
scientific papers: bibliographic coupling (Kessler 1963) and 
co-citation (Small 1973; Marshakova 1973). They soon be-
came standard techniques for science mapping (see Section 
4.1.2: The links in citation-based maps). Henry Small 
started to use co-citation analysis to map scientific areas and 
study their evolution over time. He generated the first sci-
ence maps based on co-citation analysis in 1977 to study the 
field of collagen research (Small 1977).  
In the 1980s, new methods of analysis were developed, 
such as author co-citation analysis (White and Griffith 
1981) and co-word analysis (Callon et al. 1983). At the same 
time, the technical aspects of science mapping were dis-
cussed and sometimes disputed (Leydesdorff 1987). The 
1990s saw important advancements in computer visualiza-
tion techniques and, in 1991, the first science mapping pro-
gram for the personal computer, SCI-map, was made avail-
able. In the 2000s, the improvement of computer capacity 
allowed to produce the first global maps of science, based 
on the analysis of thousands of journals and millions of 
publications. New user-friendly science mapping tools, 
such as CiteSpace and VOSviewer, were launched in the 
2010s, so that nowadays also the non-experts can generate 
their own science maps. In the last twenty years, science 
mapping has become an increasingly interdisciplinary area, 
with important contributions from computer scientists and 
experts in information visualization, and the last ten years 
have seen what has been called a “Cambrian explosion of sci-
ence maps” (Börner, Theriault, and Boyack 2015).4  
 

Knowl. Org. 48(2021)No.7/8 
E. Petrovich. 2021. Science Mapping and Science Maps 
538 
3.0 Building a science map: the general workflow 
 
The construction of a science map follows a general work-
flow that comprises the following steps (Börner, Chen, and 
Boyack 2005; Cobo et al. 2011b):  
 
1) Data collection. Based on the research question of the 
analyst, the data for the mapping are collected. In princi-
ple, any relational feature of the scientific activity can be 
collected by different methods. In practice, however, 
most science mapping studies are based on data stored in 
bibliographic data sources. Hence, the data collection 
consists in individuate appropriate queries to extract bib-
liographic data from those sources. 
2) Pre-processing. The raw data are cleaned and, if needed, 
further selected (for instance, only publications cited 
over a certain threshold are retained). This step is crucial 
since the goodness of the mapping depends on the qual-
ity of the underlying data. 
3) Network extraction. Depending on the chosen unit of 
analysis (publication, term, author, journal, institution, 
etc.) and the kind of analysis (direct linkage, co-citation, 
bibliographic coupling, co-word analysis, etc.) the corre-
sponding network is extracted from the data.  
4) Normalization. Usually, the relatedness scores (e.g., the 
raw number of co-citations between publications) are 
not directly used to generate the science maps because ex-
perience and experimentation have shown that they can 
create distortions due to the different sizes of the items 
(Boyack and Klavans 2019). It is thus a common practice 
to perform normalization on the raw values using simi-
larity measures. 
5) Visualization. There are different options to visualize the 
network. In graph-based visualizations, graph drawing al-
gorithms are used. In distance-based visualizations, dimen-
sionality reduction techniques are used to plot the data 
into a two-dimensional (or, more rarely, three-dimen-
sional) layout, so that the distances between the points on 
the map reflect the similarity of the units of analysis.  
6) Enrichment. The elements of the map can be enriched 
to provide more information. Frequently, clustering 
techniques are used to find groups of similar nodes and 
colors are used to distinguish nodes belonging to differ-
ent clusters.  
7) Interpretation. The science map is interpreted, usually 
with the help of experts in the mapped domain. The vis-
ual nature of the map enables the recognition of patterns 
and structures, which can provide an answer to research 
questions or help in addressing science policy issues.  
 
In the next sections, we focus on the first three steps of sci-
ence mapping: data collection, data pre-processing, and net-
work extraction. Based on the type of network extracted, 
different types of science maps can be generated. In section 
4, each type is examined in detail. Note that citation-based 
maps will allow us to describe the steps of normalization, 
visualization, and enrichment that recur also in the genera-
tion of other types of science maps. Section 5 is an excursus 
on how time can be represented in science maps, whereas 
section 6 discusses the last phase of science mapping, i.e., the 
interpretation. 
 
3.1 Data sources for science mapping 
 
Science mapping is a methodology that can in principle be 
applied to a variety of data regarding the scientific enter-
prise. In practice, however, the main data sources for science 
mapping are bibliographic databases. Other types of data 
must be collected by the analysts. 
Bibliographic databases are large multi-disciplinary data-
bases that collect the metadata of academic publications 
(authors, title, abstract, keywords, affiliation of the authors, 
publication year, etc.), along with their citations (hence 
their name of “citation indexes”). The main citation indexes 
are Clarivate’s Web of Science (WoS), Elseviers’ Scopus, and 
Google Scholar.  
Recently, two open bibliographic databases have joined 
Google Scholar: Microsoft Academic (launched in 2006, it 
stopped being updated in 2012 and was relaunched in 
2016)5 and Dimensions (launched in 2019)6. Moreover, in 
2017 Crossref, a not-for-profit organization of publishers, 
has made its citation data openly available. Comparisons be-
tween the coverage of these new databases and the coverage 
of traditional databases are currently being undertaken by 
the bibliometric community (Visser, van Eck, and Waltman 
2020; Harzing 2019).  
In addition to multi-disciplinary databases, there are also 
specialized databases, focusing on specific disciplines (e.g., 
PubMed for medicine, and PsycInfo for psychology). Patent 
data can be retrieved from specific data sources such as the 
United States Patent and Trademark Office7, Google pa-
tents8, and the database of the European Patent Office.9  
More detailed information about these databases can be 
found in the dedicated entry of ISKO encyclopedia 
(https://www.isko.org/cyclo/citation). 
 
3.2 Field delineation 
 
To produce a science map, we first need to individuate a set 
of publications that reasonably represent the target of the 
mapping. In bibliometric, this step is often called “field de-
lineation”. Field delineation is the collection of documents 
that are both relevant and specific for the purpose of the 
mapping (Zhao 2009).  
At this point, an important difference can be made be-
tween global and local maps of science. Global maps of sci-

Knowl. Org. 48(2021)No.7/8 
E. Petrovich. 2021. Science Mapping and Science Maps 
539 
ence (also known as atlases of science) aim to map the whole 
science (Börner et al. 2012; Boyack, Klavans, and Börner 
2005; Boyack and Klavans 2019). To produce such maps, 
the main criteria is to maximize coverage. Local maps of sci-
ence, on the other hand, focus on a limited portion of the 
scientific literature (Rafols, Porter, and Leydesdorff 2010). 
Such a portion can be a scientific field, a specialty, a research 
topic, or the publication output of a university. In all these 
cases, the accurate selection of the target publications is a 
crucial step since an unrepresentative or wrong set of publi-
cations will produce a misrepresentation of the target.  
Following Zitt and colleagues, we distinguish three gen-
eral strategies for field delineation: A) rely on external for-
malized resources, such as ready-made science classifica-
tions; B) create ad hoc information retrieval search; C) use 
network exploration resources (i.e., science mapping itself) 
(Laurens, Zitt, and Bassecoulard 2010; Zitt et al. 2019; Zitt 
and Bassecoulard 2006). 
The first strategy is based on ready-made classifications, 
such as the ones used by Web of Science or Scopus to classify 
their records. Other classificatory schemes are produced in 
institutional settings (e.g., by research evaluation agencies 
or by research councils) and, clearly, by libraries. Note that 
sometimes the journal, rather than the individual article, is 
the unit of classification, with the articles inheriting the cat-
egory of the journals where they are published. Following 
this first strategy, representative literature is retrieved by us-
ing these ready-made classifications at different levels of 
granularity (scientific field, specialty, sub-area, etc.). An ev-
ident shortcoming of this strategy is that it heavily relies on 
the goodness of the chosen classifications. 
The second strategy is based on creating, usually in close 
interaction with domain experts, ad hoc searches to query 
the databases. These queries can potentially include any 
searchable part of the bibliographic records: words in titles 
and abstracts, keywords, authors, affiliations, journals, 
dates, references, and so on. A typical query combines a 
search for specialized journals and a lexical search in comple-
ment. Note that the starting queries can be refined, for in-
stance by citation analysis. Once a core set of publications, 
journals or even key authors is determined, new records are 
added by following the citations (articles citing the core set) 
or the references (articles cited by the core set), in an iterative 
process. 
The third strategy relies on science mapping methods 
and, in particular, on clustering. The basic idea is to use bot-
tom-up clustering techniques that group publications based 
not on a classificatory scheme, but on their reciprocal rela-
tions (for instance, their co-citation strength, see Section 
4.1.2: The links in citation-based maps). Techniques of net-
work analysis, as well as experts’ knowledge, are then used to 
select the relevant clusters. By iterating this procedure, an 
increasingly precise field delineation is obtained.  
All these approaches involve the double risk of losing rel-
evant publications and introducing noise (not relevant pub-
lications) in the dataset (Zitt et al. 2019). In fact, there is no 
fit-to-all solution to field delineation. From an operative 
point of view, a good strategy is to combine recursively the 
different approaches, checking each time the set of retrieved 
publications and refining accordingly the queries (an exam-
ple of this approach can be found in Chen 2017).  
However, it is important to remember that, from a theo-
retical point of view, there is no ground truth basis for de-
fining research domains in a purely objective way. As the 
ongoing discussion about research areas definition and clas-
sification shows, research classification should be conceived 
as a social process involving multiple actors, from researchers 
to journals to research evaluation agencies, rather than as a 
static photograph of the structure of science. Classificatory 
schemes as well as the boundaries between areas are con-
stantly negotiated and reshaped under the pressure of dif-
ferent social systems and infrastructures (Sugimoto and 
Weingart 2015). As these systems serve different purposes 
and are governed by different logics, frictions and inconsist-
ences between the classificatory schemes they produce are 
to be expected (Åström, Hammarfelt, and Hansson 2017). 
For instance, an article can be classified as belonging to re-
search area X based on the institutional affiliation of its au-
thors and to research area Y based on the topic of the journal 
where it is published. Even if field delineation is the first 
step in many bibliometric analyses, including science map-
ping, its theoretical stakes should not be underestimated. 
 
3.3 Data cleaning and pre-processing 
 
When the field delineation is completed and the datasets are 
retrieved from bibliographic databases, the data consist basi-
cally of large tables, in which each row corresponds to a pub-
lication and the columns represent the available metadata of 
that publication (e.g., title, authors, abstract, publication 
year, journal, cited references, etc.).Retrieved data usually 
contain errors, for instance, misspelling of author names, er-
rors in the cited references, journal titles, and so on. Cleaning 
the data is a pivotal step in the science mapping workflow be-
cause the quality of the results depends on the quality of the 
data. This task, however, can be highly time-consuming and 
can present difficult issues, such as the disambiguation of au-
thors with homonym names and the merging of authors with 
multiple names (Strotmann and Zhao 2012). 
After the cleaning, the data can be pre-processed. They 
can be divided into different time sub-periods to carry out 
longitudinal studies (see Section 5: The representation of 
time in science mapping), or a portion of the retrieved data 
can be furtherly selected based on some measure, such as the 
most cited articles, the most productive authors, or the jour-
nals with the highest performance metrics. 

Knowl. Org. 48(2021)No.7/8 
E. Petrovich. 2021. Science Mapping and Science Maps 
540 
3.4 Network extraction 
 
In general, a network is a structure made of nodes (also called 
vertices) and links (also called edges). It can be represented as 
a graph or as a matrix. Networks are valuable tools to repre-
sent and study a great variety of natural and social phenom-
ena, from the lineage of a family to patterns of contracts 
among firms, to the spreading of a virus (Barabási 2014).  
In science mapping, we are interested in those networks 
that can capture the structure of science at different levels 
and from different points of view. In fact, these networks 
are the basic structure on which science maps are built. 
From the same set of bibliographic records, it is possible 
to generate different networks, depending on the type of 
nodes and links we decide to focus on. The nodes will rep-
resent the unit of analysis of the final map, whereas the links 
the type of relationship displayed.  
 
4.0 Types of science maps 
 
Science maps can be classified into different types depend-
ing on the kind of data, and hence the kind of network, they 
are based on. In principle, any feature of the scientific enter-
prise that can be represented in relational terms, i.e., as a net-
work of nodes and links, can be used to generate a science 
map. In citation-based maps, the units of analysis (the 
nodes) are publications or aggregates of publications (e.g., 
journals or authors), and the relationships between them 
(the links) are citations or association measures based on ci-
tations (bibliographic coupling and co-citation). In term-
based maps, the units of analysis are textual items (themes, 
keywords or terms) and the relationships are co-occurrence 
frequencies (e.g., the number of times two keywords are 
used together in a set of publications). In co-authorship 
maps, the units are the authors and the links are the number 
of co-authored publications. In interlocking editorship 
maps, the units are the journals and the links are the number 
of persons who are shared between the editorial boards of 
two journals). In addition to these, there are also science 
maps based on patents data and geographic maps of science, 
which will be the topic of Section 4.4.  
 
4.1 Citation-based maps 
 
4.1.1 The nodes in citation-based maps: publications 
and aggregates of publications 
 
In the most basic citation-based map, the nodes represent 
individual publications and the links the citations (refer-
ence-links) among them. An example of citation network is 
provided in Figure 1, where it is visualized as a directed net-
work in which nodes represent publications and arrows the 
reference-links (citations) between them. Some publica-
tions are both citing and cited (e.g., publication a), some 
publications are only cited (e.g., publication f), and some 
publications cite without being cited (e.g., publication e). 
 
Figure 1. Example of citation network. Nodes represent document and ar-
rows the citations between them. 

Knowl. Org. 48(2021)No.7/8 
E. Petrovich. 2021. Science Mapping and Science Maps 
541 
The same information can be represented as an adja-
cency matrix, whose elements indicate whether pairs of 
nodes are connected (“adjacent”) in the network or not. 
When the publication in the row cites a publication in the 
column, the corresponding element in the matrix is 1, 0 oth-
erwise.10 
  
a 
b 
c 
d 
e 
f 
g 
h 
a 
0 
1 
1 
1 
0 
0 
0 
0 
b 
0 
0 
1 
0 
0 
0 
0 
1 
c 
0 
0 
0 
0 
0 
1 
1 
0 
d 
0 
0 
0 
1 
0 
0 
0 
0 
e 
1 
0 
1 
0 
0 
0 
1 
0 
f 
0 
0 
0 
0 
0 
0 
0 
0 
g 
0 
0 
0 
0 
0 
0 
0 
0 
h 
0 
0 
0 
0 
0 
0 
0 
0 
 
Since publications are provided with metadata, such as their 
authors or the journals in which they are published, it is pos-
sible to build aggregates of publications sharing the same 
metadata (Radicchi, Fortunato, and Vespignani 2012). By 
aggregating publications at a higher and higher level, we can 
reach higher units of the analysis and networks based on 
new types of nodes.  
To understand this mechanism, we show how to build a 
journal citation network (Leydesdorff 2004; McCain 1991) 
starting from the document citation network of Figure 1. 
We start by coloring the nodes according to the journals 
where they are published, and the citation links according 
to the journal to which they point (Figure 2).  
The journal citation network is obtained by substituting 
each article with its journal of publication and then using 
the journals as nodes of the network. A link between two 
journals is drawn when they exchange at least one citation. 
Note that in this new network, it is possible to provide links 
with weight, that is the number of citations that each jour-
nal receives from other journals (or from itself). In the pre-
vious network, there was not a proper weight but only an 
on/off relationship (presence of a reference-link or not). 
There are also some loops, produced by articles citing arti-
cles published in the same journal (these loops correspond 
to journal self-citations). The resulting journal citation net-
work is shown in Figure 3. 
By the same aggregation process, we can construct au-
thor citation networks (e.g., McCain 1990; Radicchi et al. 
2009), or reach higher units of analysis, such as institutions 
and even countries (e.g., Glänzel 2001). 
 
 
 
 
Figure 2. Citation network with document-nodes colored based on the jour-
nal they were published in. The color of the arrows corresponds to the color 
of the citing journal. 

Knowl. Org. 48(2021)No.7/8 
E. Petrovich. 2021. Science Mapping and Science Maps 
542 
4.1.2 The links in citation-based maps: direct  
citations, bibliographic coupling, and  
co-citations 
 
Until now, we considered only citations as links in the cita-
tion network. The presence of a reference-link between two 
publications usually attests that they are somehow associ-
ated, for instance, that they share the same topic or research 
method (see Section 7.3: The meaning of citations). Maps 
in which the links are direct citations are called “direct-link-
age” or “cross-citations” or “inter-citation” maps (Waltman 
and van Eck 2012). In science mapping, however, there are 
two other common techniques used to measure the related-
ness or strength of association of publications (or their ag-
gregates): bibliographic coupling (Kessler 1963) and co-ci-
tation (Small 1973; Marshakova 1973). 
In bibliographic coupling, a link between two publica-
tions is established when they share at least one publication 
in their respective bibliographies, i.e. when they have at least 
one reference in common. The weight of the link is propor-
tional to the number of shared references. Co-citation is, in 
a certain sense, the reverse of bibliographic coupling. In a 
co-citation network, a link is drawn between two publica-
tions if they are cited together at least by a third publication, 
and the weight of the link (the so-called co-citation 
strength) is proportional to the number of common cita-
tions they gather (i.e., the number of co-citations).  
Figure 4 shows the bibliographic coupling network gen-
erated from the citation network of Figure 1. Note that 
publication f has no link with other publications because, in 
our example, it did not have any cited reference (i.e., no out-
going link). 
Figure 5 shows the co-citation network. Analogously, 
publication e has no link with other publications because it 
had no citations (i.e., no incoming link). 
Note that citations are directed links because we can dis-
tinguish between a sender and a receiver of the citation. In 
network theory terminology, they are called “arcs” (Wasser-
man and Faust 1994). In contrast, bibliographic coupling 
and co-citation links are un-directed links because biblio-
graphic couplings and co-citations are symmetrical. In net-
work theory terminology, they are called “edges” (Wasser-
man and Faust 1994). 
Starting from a matrix whose rows are the citing publica-
tions and columns are the cited publications, it is possible to 
derive by matrix algebra operations the two co-occurrence 
matrices representing the bibliographic coupling network 
or the co-citation network (Van Raan 2019). 
Note that direct citations, bibliographic coupling, and 
co-citation analysis can be applied not only to single publi-
cations, but also to aggregates of publications. For instance, 
if authors are used as units in co-citation analysis, we have 
Author Co-Citation Analysis (e.g., White and McCain 
1998; Kreuzman 2001), if journals are used as units, we have  
 
Figure 3. Example of journal citation network. Out-citations, in-citations, and 
self-citations between journals are colored, respectively, in green, orange, and 
violet. 

Knowl. Org. 48(2021)No.7/8 
E. Petrovich. 2021. Science Mapping and Science Maps 
543 
 
 
Figure 4. Bibliographic coupling network generated based on the citation net-
work in Figure 1. Nodes are publications, links show bibliographic coupling 
between publications. Note that publication f has no bibliographic coupling 
links with other publications in the network. 
 
Figure 5. Co-citation network generated based on the citation network in Fig-
ure 1. Nodes are publications, links show co-citation between publications. 
Note that publication e has no co-citation links with other publications in the 
network. 

Knowl. Org. 48(2021)No.7/8 
E. Petrovich. 2021. Science Mapping and Science Maps 
544 
Journal Co-Citation Analysis (e.g., McCain 1991). By com-
bining in this way methods and units of analysis, several 
types of bibliometric networks can be generated (Waltman 
and van Eck 2014). Figure 6 shows an example of co-citation 
map using individual publications as units of analysis. 
 
4.1.3 Normalization 
 
Usually, the raw frequencies of citations, bibliographic cou-
plings or co-citations are not directly used as input of the 
visualization process that leads to the final form of the sci-
ence map. This is because the raw frequencies do not 
properly reflect the similarity between the items (van Eck 
and Waltman 2009). To understand why, suppose that de-
partment AA and department BB publish comparable arti-
cles, but department AA, having more researchers than de-
partment BB, publishes 10 times more articles. Other things 
being equal, one would expect that the articles from depart-
ment AA will receive in total about ten times as many cita-
tions as the articles from department BB and thus to have 
about ten times as many co-citations with other depart-
ments in the same discipline as department BB. However, 
the fact that department AA has more co-citations with 
other departments than department BB does not indicate 
that it is more like other departments than department BB. 
It only shows that department AA publishes more articles 
than journal BB because it is bigger. To correct such a dis-
tortion due to the different size of the units of analysis, we 
need to transform the raw co-citation scores, adjusting them 
by some stable quantity, an operation called “normaliza-
tion” (van Eck et al. 2010).  
In science mapping, similarity measures are used to per-
form such a normalization. Following Ahlgren and col-
leagues, we distinguish two main approaches to calculating 
these similarities: the local or direct and the global or indi-
rect (Ahlgren, Jarneving, and Rousseau 2003). In the for-
mer approach, the focus is on the co-occurrence frequencies 
of the items, that are then adjusted for different quantities. 
Examples include the cosine (the most popular one), the as-
sociation strength (used in VOSviewer, see the Appendix), 
the inclusion index, and the Jaccard index (van Eck and 
Waltman 2009). In the latter approach, the focus is on the 
way two items are related to all the other items in the dataset 
under study. This means that what is compared to obtain 
 
Figure 6. Example of co-citation map. The field mapped is analytic philosophy. The nodes represent documents. A link is drawn between 
two nodes when they are co-cited. Size of the nodes is proportional to the number of citations gathered by the document; thickness of the 
links is proportional to the co-citation strength; nodes’ colors indicate the cluster to which they are attributed by the clustering algorithm. 
Nodes are positioned according to their co-citation strength, so that the more frequently they are cited together, the closer they appear on 
the map. The visualization was produced with VOSviewer. 

Knowl. Org. 48(2021)No.7/8 
E. Petrovich. 2021. Science Mapping and Science Maps 
545 
the similarity between two items are their entire profiles, 
i.e., the entire rows (or columns) of the co-occurrence ma-
trix, and not their simple co-occurrence frequency. Pear-
son’s correlation coefficient (r), the cosine11, and the Chi-
Squared distance are examples of indirect similarity measure 
based on the global approach (McCain 1990; White and 
Griffith 1981). However, the reliability of Pearson’s r as a 
similarity measure has been contested (Ahlgren, Jarneving, 
and Rousseau 2003; van Eck and Waltman 2008).  
In general, there is no agreement on what the best nor-
malization procedure is and on what similarity measures 
should be used in science mapping (Boyack and Klavans 
2019; Leydesdorff 2008; Van Raan 2019). In the scien-
tometric community, the discussion still goes on after 35 
years (e.g., Zhou and Leydesdorff 2016). However, it is im-
portant to remember that, depending on the chosen proce-
dure, the resulting science maps can be rather different (Bo-
yack, Klavans, and Börner 2005). 
 
4.1.4 Visualization 
 
Visualization is the step in the science mapping process in 
which the information contained in the network is dis-
played in a visual layout comprehensible to human under-
standing. Following Waltman and Van Eck (2014), we dis-
tinguish two basic types of visualizations: graph-based and 
distance-based. They are not the only approaches available 
but are probably the most common in science mapping.12 
In graph-based visualization, the network is visualized as 
a graph made of nodes and edges (Figures 1, 2, 3, 4, and 5 
are examples of graph-based visualizations). The edges (links 
between nodes) are displayed to indicate the relatedness of 
nodes. The most common technique for creating such 
graphs are force-directed graph drawing algorithms, such as 
the Kamada and Kawai and the Fruchterman and Reingold 
(Chen 2013).  
To understand the underlying mechanism of these algo-
rithms, imagine the network as a physical system, in which 
the nodes are little balls electrically charged and the links are 
springs that connect them. The electric charge creates a re-
pulsive force between the balls, counterbalanced by the at-
tractive force generated by the springs. The algorithms basi-
cally simulate the network as such a physical system made of 
balls and springs and apply two opposite forces to the nodes, 
one attractive (proportional to the weight of the link be-
tween two nodes) and the other repulsive, until the system 
comes to a state of mechanical equilibrium. The final layout 
is the one corresponding to such an equilibrium state. Note 
that several configurations are possible since usually there is 
no unique equilibrium state. 
Force-directed graph drawing algorithms are imple-
mented in software for network analysis and visualization, 
such as Gephi13 and Pajek.14 An example of a graph-based 
science map created with Pajek and visualized with the 
Kamada and Kawai algorithm can be found in (Leydesdorff 
and Rafols 2009, Figure 4). An example of a graph-based sci-
ence map created with Gephi can be found in (Weingart 
2015, Figure 4) 
The other visualization approach is distance-based. In 
distance-based visualizations, the distance of nodes on the 
map reflects their similarity, so that similar nodes are placed 
closer and dissimilar nodes far away. Note that in graph-
based visualization, on the other hand, the position of the 
nodes is not directly related to their similarities, but it is a 
product of the “pull and push” mechanism of the drawing 
algorithm. In distance-based visualizations, links can be 
shown or not. 
Distance-based visualizations are conceptually closer to 
geographic maps than graph-based visualizations. Geo-
graphic maps represent relationships in space by placing ob-
jects that are close in the physical space near on the maps and 
objects that are distant in the physical space further apart on 
the map. Distance-based maps have the same goals, but in-
stead of being based on physical distances, they are based on 
similarities between objects.  
To produce a distance-based visualization, therefore, the 
similarities between the nodes must be transformed into dis-
tances.15 The distance matrix that is thus obtained is concep-
tually analogous to the table reporting the distances be-
tween pairs of cities in a geographic atlas. The task consists 
of reconstructing from the relative distances the positions 
of the items on the map, i.e., in finding the coordinates of 
the items in a two-dimensional space starting from their re-
ciprocal distances. 
To fulfill this task several statistical techniques have been 
developed. The most important belong to the family of 
multi-dimensional scaling (MDS) methods (Borg and 
Groenen 2010). They aim to find the coordinates of the 
points in a lower-dimensional space (usually, a plane) such 
that the distances of the points on the lower-dimensional 
space reflect as accurately as possible the original distances 
of the points. The average difference between the distances 
on the map and the original distances tells us how much the 
map distorts the original configuration. The amount of dis-
tortion is used to calculate the stress of the map. The various 
algorithms for MDS essentially adjust the positions of the 
points until a minimum value of stress is reached.16 
It is important to underlie that distance-based visualiza-
tions can be rotated, flipped, and mirrored. Since the out-
put of MDS is not a set of fixed coordinates but a set of rel-
ative distances between the points, any geometrical transfor-
mations that leave them unaltered can be applied. An exam-
ple of distance-based visualization can be found in (White 
and McCain 1998, Figure 2). 
When interpreting the output of MDS, that is usually a 
two-dimensional map, is it very important to be aware that 

Knowl. Org. 48(2021)No.7/8 
E. Petrovich. 2021. Science Mapping and Science Maps 
546 
the algorithms can generate visual artifacts, i.e., structures or 
patterns that are visible on the map but that are not present 
in the original data. For instance, Van Eck and co-authors 
(2010) note that variants of MDS tend to produce quasi-
circular layout when used on big matrices and that they tend 
to locate items with a high number of co-occurrences to-
ward the center of the map.  
However, the trickiest artifacts have to do with the issue 
of dimensionality reduction, i.e. with the very core of MDS. 
Imagine that we have four points in a three-dimensional 
space, each one located at the same distance from the others, 
like the vertices of a three-sided pyramid, all sides of equal 
length (Borg and Groenen 2010, chap. 13.3). When we try 
to place the four points in a two-dimensional plane, we can 
respect the equal distance only for three points out of four. 
The fourth point will lie almost at the center of a bi-dimen-
sional triangle (as if we were looking at the pyramid from 
the above) so that its distance from the other points will al-
ways be shorter than the distances between the three points 
themselves.17 Without knowing the original three-dimen-
sional structure and by looking only at the two-dimensional 
map, we would wrongly conclude that the fourth point is 
closer to the other three. The wrong conclusion raises from 
the fact that the two-dimensional map necessarily distorts 
the three-dimensional structure because it suppresses the 
third dimension, which however carries essential infor-
mation (the equal distance between the fourth point and 
the other three points). By losing such information, it intro-
duces an artifact. Interestingly, MDS can generate also the 
opposite artifact: points that are placed far away in the map 
can be however connected by “tunnels” in hidden dimen-
sions (Leydesdorff and Rafols 2009). Imagine a paper sheet 
with two distant points on it: if we bend the sheet, we can 
make the two points very close in the third dimension, real-
izing a “tunnel” between them. If we consider only their dis-
tance on the two dimensions of the sheet, however, they will 
appear to be distant. 
In sum, dimensionality reduction techniques do allow us 
to obtain significant insights into the structure of biblio-
metric networks because they reveal the main features of 
such a structure. At the same time, since those features may 
lie in more than two dimensions, one must be aware of the 
inevitable distortions introduced by the dimensionality re-
duction itself. 
 
4.1.5 Enriching the map 
 
With the visualization of the network, we reach the basic 
form of the science map. At this point, the interpretation of 
the map can already begin. However, it is common to enrich 
the basic form by displaying further information on it. 
A first option is to use the size of the nodes and the width 
of the links to convey their properties. In a co-citation map, 
for instance, the size of the nodes can be used to represent 
the number of citations collected by the units of analysis 
(publication, journal, author, etc.) and the links can be 
drawn thicker or darker to express the strength of the con-
nections (e.g., number of co-citations between two nodes). 
Alternatively, the size of the nodes can be used to represent 
the centrality of the nodes, using one of the different no-
tions of centrality defined in network theory. The most 
common include degree centrality, betweenness centrality, 
closeness centrality, and eigenvector centrality (Wasserman 
and Faust 1994). The degree centrality of a node is propor-
tional to the number of its links so that it is higher for highly 
connected nodes. Betweenness is a measure of brokerage of 
gatekeeping, that is of how much a node is an “obligatory 
passage” in the network. In science mapping, it is sometimes 
used to measure interdisciplinarity (Leydesdorff 2007). 
Closeness measures how close a node is to the other nodes 
in the network. Nodes with high closeness are the ones that 
can be reached with few steps18 from any other node in the 
network. Lastly, eigenvector centrality is a measure of the in-
fluence of a node in the network. The underlying idea of 
eigenvector centrality is that the influence of a node de-
pends on the influence of the nodes to which it is con-
nected, so that a node connected with other central nodes 
increases its centrality.  
A further option to enrich the map is to use colors to dis-
tinguish visually different clusters of nodes. Networks typi-
cally display an internal organization in clusters or commu-
nities, that is groups of highly interconnected nodes (Radic-
chi, Fortunato, and Vespignani 2012). In distance-based vis-
ualizations, clusters result as sets of close points, separated 
from other clusters by blank space. The techniques of clus-
ter analysis can be used to detect such communities. One 
common method is hierarchical agglomerative clustering 
(Chen 2013). All the units of the map (the nodes) begin 
alone in groups of size one, then, at each iteration of the 
clustering algorithm, similar groups are merged, until all the 
nodes belong to one super-cluster. A resolution parameter 
controls the granularity of the clustering, i.e., the size of the 
communities. Different agglomerative methods are charac-
terized by the definition of distance between clusters they 
use and by the metric employed to calculate the distances 
(there are lots of options besides the familiar Euclidian dis-
tance). In single-linkage clustering, the distance between 
two clusters is set equal to the distance between their closest 
nodes. In complete-linkage clustering, on the other hand, it 
is equal to the distance between the most distant nodes in 
the two clusters. Lastly, in centroid linkage clustering, it is 
equal to the distance between the “centers” or average points 
(centroids) of the clusters. These clustering procedures, 
however, are only a small fraction of the available tech-
niques and algorithms for clustering and community detec-
tion. In the last years, the techniques based on modularity, 

Knowl. Org. 48(2021)No.7/8 
E. Petrovich. 2021. Science Mapping and Science Maps 
547 
originally developed in physics, are becoming increasingly 
popular (Thijs 2019).19  
Clusters can be labelled automatically by extracting 
terms from the titles, abstracts, and keywords of the publi-
cations in the clusters (Chen 2006) (see Section 4.2.2: Co-
word analysis based on automatically extracted terms). Each 
cluster is thus provided with a word-profile and its most rel-
evant words can be superimposed on the map to facilitate 
the interpretation of the clusters (Chen, Ibekwe-SanJuan, 
and Hou 2010). 
A last method for enriching the science map is to use the 
overlay (Rafols, Porter, and Leydesdorff 2010). In science 
overlay maps, the results of the mapping are laid over a back-
ground, that can be, for instance, a global map of science. 
The background serves as a reference system that facilitates 
the interpretation of the results. For instance, the scientific 
output of a university can be overlaid on a global map of 
science to get an insight into the scientific coverage of the 
university or its impact (see Section 8: Science maps and sci-
ence policy).  
 
4.2 Term-based maps 
 
Term-based science maps are used to extract and visualize 
the intellectual content of a corpus of publications based on 
the analysis of the terms associated with those publications 
(Börner, Chen, and Boyack 2005). These terms can be the 
keywords or descriptors of the publications, or they can be 
extracted automatically from titles and abstracts or even the 
full texts of articles. Term-based science maps allow to ex-
plore at a fine-grained level the intellectual content of pub-
lications since titles, abstracts, and keywords are meant to 
report the main topics, concepts, and results of scientific ar-
ticles (He 1999; Van Raan and Tijssen 1993). 
An important advantage of term-based mapping com-
pared to citation-based mapping is that it applies to fields 
characterized by the scarce presence of citations, such as ap-
plied research and technology (Callon et al. 1983).  
Depending on the method by which the terms character-
izing a publication are extracted, we can distinguish two 
types of term-based maps. Classic co-word analysis, devel-
oped by Callon and colleagues, is based on human-assigned 
keywords. Natural Language Processing (NLP)-based co-
word analysis, on the other hand, is based on terms that are 
automatically extracted from the texts by natural language 
processing techniques.  
Independently of the method, however, co-word analysis 
rests on some assumptions that have been contested. The 
main one is that words and terms have a stable meaning 
across fields and over time so that they can be used as reliable 
proxies of scientific concepts and ideas (Leydesdorff 1997). 
However, this assumption may be false, and historians of 
science have indeed shown that the phenomenon of mean-
ing-shift occurs in science (Kuhn 2000). A possible reply to 
this criticism is that words in co-word analysis are not used 
as carriers of meaning but as simple links between texts 
(Courtial 1998). From an operative point of view, meaning 
shift can be avoided by restricting the time scope of the anal-
ysis to a relatively short period and semantically homogene-
ous areas (Mutschke and Quan-Haase 2001). 
 
4.2.1  Classic co-word analysis and the strategic  
diagrams 
 
The first term-based maps were developed in the 1980s by a 
team of sociologists of science based at the Centre de Soci-
ologie de l’Innovation at the École des Mines in Paris. They 
were designed to study the interaction between scientific 
knowledge and technological innovation, and, more gener-
ally, the relations between science and society (Callon et al. 
1983). It is important to point out that the theoretical foun-
dation of co-word analysis developed by Callon and others 
lies in the tradition of the Science and Technology Studies, 
and in particular in the Actor-Network Theory developed 
by Bruno Latour and others (Callon, Law and Rip 1998; 
Latour 2003). However, as a mapping method, co-word 
analysis can be employed without endorsing such a theoret-
ical framework.  
Callon and colleagues focused in particular on the de-
scriptors employed by documentation services to index the 
content of scientific and technological publications (Cal-
lon, Courtial and Laville 1991). The method of co-word 
analysis, then, consists first in collecting all the descriptors 
of the target documents. After a process of cleaning, in 
which variants and synonyms are merged and not relevant 
descriptors removed (see Section 3.3: Data cleaning and pre-
processing), the co-occurrence frequency of each pair of de-
scriptors is calculated. Two descriptors co-occur if they are 
used together in the description of a single document. A co-
occurrence matrix reporting the co-occurrence frequencies 
of each pair of descriptors is thus produced, and the raw val-
ues are then normalized (see Section 4.1.3: Normalization).  
In the classic co-word methodology, as described by Cal-
lon and colleagues, the visualizations produced by co-word 
analysis are “strategic diagrams” (sometimes called “cogni-
tive maps”), which are a special kind of science map that 
should not be confused with distance-based visualizations. 
To create a strategic diagram, clusters of frequently co-oc-
curring descriptors or keywords are created by some cluster-
ing technique. Such clusters are called “themes” and are de-
scribed by two characteristics: centrality and density. The 
centrality of a cluster is given by its external link, i.e., the 
number of links it has with other clusters. The density of a 
cluster is defined as the proportion between the links that 
are present in the keywords cluster and the number of pos-
sible links. Each theme is thus defined by two variables, cen-

Knowl. Org. 48(2021)No.7/8 
E. Petrovich. 2021. Science Mapping and Science Maps 
548 
trality and density, that constitute its coordinates in the stra-
tegic diagram (He 1999). Then, the strategic diagram is di-
vided into four quadrants (Mutschke and Quan-Haase 
2001). The themes in the first quadrant are characterized by 
high density and high centrality and constitute the main-
stream of the scientific field. The themes in the second 
quadrant, characterized by high centrality and low density, 
are unstructured themes that may be described as “band-
wagon” themes. The themes in the third quadrant are char-
acterized by high density and low centrality: they have a 
well-developed maturity but lacks ties to other themes in the 
field. They are the “ivory tower” themes. Lastly, the themes 
in the fourth quadrant, characterized by low centrality and 
low density, comprise both topics that are fading away and 
new topics that are emerging. In longitudinal analysis, the 
trajectory of a theme can be followed through the quadrants 
of the strategic diagram. An example of a strategic diagram 
can be found in (Cobo et al. 2011a, Figure 6). 
The method of co-word analysis based on descriptors or 
other kinds of keywords may suffer from the so-called “in-
dexer effect” (Law and Whittaker 1992). Indexing may re-
flect the prejudices or points of view of the human indexers 
and may be inconsistent between different indexers or 
change over time. The indexer effect is a problem common 
to all human-based classifications. The study of research 
classification systems reveals that they cannot be taken at 
face value as they are the result of complex disciplinary ne-
gotiations in which both intellectual and academic interests 
are involved.20  
 
4.2.2 Co-word analysis based on automatically  
extracted terms 
 
The indexer effect can be partially avoided by recurring to 
the automatic extraction of terms from titles, abstracts, or 
even the full texts of articles. However, even if this method 
does not rely on the choices of an indexer, it is not free of 
human intervention. In fact, it shifts from the choices of the 
indexer to the choices of the authors of scientific publica-
tions, who decide what words should be included in the ti-
tles and abstracts. The issue of meaning shift, therefore, is 
not solved. 
Natural Language Processing (NLP) techniques are used 
to extract terms from the textual data (Taheo 2018). In gen-
eral, terms are “n-grams”, i.e., sequences of n items (usually 
words). A special category of n-grams are noun-phrases, i.e., 
sequences that consist exclusively of nouns and adjectives 
and that end with a noun (e.g., “text mining”, “network 
analysis”). Algorithms for term detection usually comprise 
several steps: first, the text is split up into sentences and sen-
tences split up into single words (tokenization), then so-
called stop-words are removed (words such as “and”, “or”, 
etc.), and the remaining words are assigned to a part of 
speech, such as verb, noun, adjective, etc. (part-of-speech 
tagging). Noun-phrases are then identified, and, lastly, vari-
ants (e.g., plurals) are merged into one form. Once the list 
of noun-phrases is obtained, a fraction of them is retained. 
A common strategy is to select only the most relevant noun-
phrases. It is important not to confuse relevance with fre-
quency: frequency is a brute measure of the occurrences of 
a term, whereas relevance can be conceived as a measure of 
how specific a term is (Sparck Jones 1972). To understand 
the difference between the two, take a term such as 
“method”. In the scientific literature, it is denoted by a high 
frequency; however, it is scarcely relevant to characterize a 
scientific article, since is occurs probably in most scientific 
articles. Knowing that an article contains the term 
“method” is a very thin indication of its content. Because of 
its being too generic, “methods” therefore has a low rele-
vance. A term such as “cardiovascular”, on the other hand, 
is less frequent than “method” but conveys more infor-
mation about the specific topic of an article. Therefore, it 
has a high relevance. Relevance scores serve to discriminate 
generic from specific terms. A common metric used in text 
mining to calculate relevance scores is TF-IDF, short for 
“term frequency-inverse document frequency” (Salton and 
McGill 1983). The underlying idea is that the relevance of a 
term is proportional to its occurrences and inversely propor-
tional to the number of documents in which it occurs. 
Terms that occur very frequently in a few documents will 
score higher on TF-IDF than terms that occur very fre-
quently in most of the documents. From this basic idea, 
more refined metrics to calculate the TF-IDF have been de-
veloped (Thijs 2019).  
After the selection step, the number of documents in 
which each pair of terms appear is calculated and the corre-
sponding co-occurrence matrix generated. The process is 
then the same as citation-based maps. Usually, the raw co-
occurrence frequencies are normalized (see Section 4.1.3: 
Normalization), and then the term map is obtained in the 
form of a distance- or graph-based visualization (see Section 
4.1.4: Visualization). Further techniques, such as clustering, 
can be applied to enrich the map (see Section 4.1.5: Enrich-
ing the map). Note that term-based maps thus obtained are 
different from the strategic diagrams produced by classic co-
word methodology. They represent the topics recurring in 
the set of publications analyzed, rather than the properties 
of their themes. An example of term-based map is shown in 
Figure 7. 
 
4.3 Other network-based maps 
 
Besides citation networks and term networks, several other 
networks can be used to generate science maps. In this sec-
tion, we briefly present co-authorship networks and inter-
locking editorship networks. 

Knowl. Org. 48(2021)No.7/8 
E. Petrovich. 2021. Science Mapping and Science Maps 
549 
4.3.1 Co-authorship networks 
 
Co-authorship networks are science maps in which the 
nodes represent authors and the links the relation of co-au-
thorship, i.e., the number of articles authored together by 
each pair of authors (Newman 2001). Since co-authorship 
usually implies a strong relationship of collaboration (Katz 
and Martin 1997; Liu et al. 2005), co-authorship networks 
are used to reconstruct and investigate the social networks 
of researchers, the so-called “invisible colleges” (Crane 
1972). It must be remembered, however, that co-authorship 
is only a proxy of scientific collaboration and that some type 
of collaborative work occurring in research (e.g., the work 
of laboratory technicians) do not lead automatically to the 
authorship (Laudel 2002). More generally, the practice of 
authorship and the requirements for being awarded author-
ship varies in different areas (Larivière et al. 2016). Further 
issues that complicate the interpretation of co-authorship 
data are “ghost” and “honorary” authorship, as well as the 
phenomenon of “hyper-authorship” (Cronin 2001). Espe-
cially in bio-medical fields, there is evidence that sometimes 
scientists are included as co-authors of articles even if they 
did not contribute to the research process (“gift” or “hon-
orary” authorship), while others are denied legitimately 
earned authorship (“ghost” authorship) (Wislar et al. 2011). 
Honorary authorship can artificially inflate the relevance of 
some researchers in the co-authorship network, whereas the 
ghost authors remain simply invisible to standard co-au-
thorship analysis. Furthermore, in some areas such as high-
energy physics and again biomedicine, the last years have 
witnessed massive levels of co-authorship. Cronin has 
coined the term “hyper-authorship” to describe such a 
growing phenomenon of publications with hundreds, if 
not thousands of co-authors. For instance, in 2015, a publi-
cation in high-energy physics counted 5000 co-authors. Hy-
per-authorship does not only challenge the standard con-
ception of authorship but also raises several issues about re-
sponsibility and accountability, which have been widely dis-
cussed by editors of biomedical journals (see e.g., ICMJE 
2019). The presence of hyper-authorship is an important 
factor that must be considered when a field is investigated 
by of co-authorship networks.  
In sum, co-authorship networks are useful tools to inves-
tigate scientific collaboration, but, since they are based on 
formal authorship, they should be interpreted in the light of 
detailed knowledge of the authorship practices of the area 
 
Figure 7. Example of term-based map. The field mapped is human geography. The nodes represent the most occurring terms in the field. 
Size of the nodes is proportional to the term’s occurrence. A link is drawn between two terms if they co-occur in the same title or abstract. 
The thickness of the link between two nodes is proportional to the number of co-occurrences of the terms. The color of the nodes corre-
sponds to the cluster they are attributed to by the clustering algorithm. Nodes are positioned in the map based on their co-occurrences, so 
that terms frequently occurring together are closer on the map. The visualization was produced with VOSviewer. 

Knowl. Org. 48(2021)No.7/8 
E. Petrovich. 2021. Science Mapping and Science Maps 
550 
under investigation, taking into consideration also possible 
distortions due to ghost, honorary and hyper-authorship. 
 
4.3.2 Interlocking editorship networks 
 
Interlocking editorship is a method to map relationships be-
tween journals. Two journals are connected in the interlock-
ing editorship network when they have at least one member 
of the editorial board in common (Baccini and Barabesi 
2010). The editors of a scientific journal play a relevant role 
as “gatekeepers” of scientific disciplines since they manage 
the peer review process and make the final decision on the 
publication of articles (Crane 1967). Therefore, interlock-
ing editorship networks can be used to reveal groups of jour-
nals whose editors endorse similar policies. Interlocking ed-
itorship networks seem to be highly correlated with journal 
co-citation networks, showing that similar editorial policies 
may reflect similar intellectual approaches to the discipline 
(Baccini et al. 2019). 
 
4.4 Other types of science maps 
 
In a broader sense of the term, we can include into the cate-
gory of science maps also other visual representations of sci-
ence that are not directly based on networks of scientific 
publications or that integrate network data with other types 
of data. Maps based on the analysis of patents belong to the 
first category and geographic maps of science to the second. 
 
4.4.1 Maps based on patents data 
 
Several maps can be generated from the analysis of patents, 
which are especially interesting for studying the dynamics 
of technology systems and the interaction between science 
and technology (Jaffe and Trajtenberg 2002). A first kind of 
patent map is based on the patents’ metadata stored in pa-
tent databases. Patents, like publications, have several 
metadata, such as the applications, the region where a pa-
tent is in force, the classification category, the application 
year, etc. Moreover, patents frequently include references to 
the scientific literature and other patents as well. All these 
metadata can be used to generate networks of patents or net-
works of patent features (Federico et al. 2017). For instance, 
Boyack and Klavans created a map of patents based on the 
IPC (International Patent Classification). The map shows 
the relations between patents based on their co-classifica-
tion: patents that are classified in the same category form 
clusters (Boyack and Klavans 2008). Other patent maps can 
be generated based on the citation network of patents, ap-
plying the equivalents of the direct linkage, bibliographic 
coupling, and co-citation methods to patents (von Wart-
burg, Teichert, and Rost 2005). Analyzing the references to 
scientific publications contained in patents allows tracing 
the links between scientific knowledge and technological 
applications (Meyer 2000), whereas, by studying the scien-
tists that are both authors of scientific publications and in-
ventors of patents, it is possible to map the overlap between 
scientific and technological literature (Murray 2002). In the 
last years, text-mining techniques see Section 4.2.2: Co-
word analysis based on automatically extracted terms) have 
increasingly been applied to patent mapping (Ranaei et al. 
2019). These methods allow us to automatically extract key-
words from patent documents and then built patent maps 
or term-maps of patents (Lee, Yoon, and Park 2009; Tseng, 
Lin, and Lin 2007). 
 
4.4.2 Geographic maps of science 
 
The science maps we presented so far focused on the ab-
stract spaces of science, such as citation, term, and collabo-
ration spaces. Classic science maps aim at visualizing pat-
terns and trajectories occurring in these abstract dimen-
sions. Science, however, is also a concrete activity occurring 
in specific places on our planet (Finnegan 2015). In fact, sci-
ence is produced in geographic sites that are not equally dis-
tributed on the Earth but are concentrated in few, highly de-
veloped areas. From those sites, scientific knowledge travels, 
as publications and researchers move around the globe. Ge-
ographic maps of science aim at describing the spatial diffu-
sion of scientific activities and the circulation of scientific 
knowledge in the geographic space. They are a key research 
topic in spatial scientometrics (Frenken, Hardeman, and 
Hoekman 2009) and an important tool in the geography of 
science (Livingstone 2003). By showing the unequal spatial 
distribution of science and research in different countries, 
they offer interesting insights into the structure of the 
global research system (Wichmann Matthiessen, Winkel 
Schwarz, and Find 2002). 
Geographic maps of science are created by locating on a 
geographic map, e.g., a map of the Earth, the nodes of the 
network we focus on. For instance, the authors of a co-au-
thorship network can be placed on the map based on the co-
ordinates of their research institutions. Or a network of cit-
ies collaborating in the production of scientific papers can 
be constructed and plotted on a map (Leydesdorff and 
Persson 2010). Or citation flows between universities can be 
geographically visualized (Börner et al. 2006). The tool 
CiteSpace (see the Appendix) provides a specific utility to 
generate geographic maps of science. 
 
5.0 The representation of time in science mapping 
 
There are different options to include the dimension of time 
into science maps. A first option consists in longitudinal 
mapping (Cobo et al. 2011a; Petrovich and Buonomo 2018; 
Petrovich and Tolusso 2019): based on the publication year 

Knowl. Org. 48(2021)No.7/8 
E. Petrovich. 2021. Science Mapping and Science Maps 
551 
of the bibliographic records, subsets of publications belong-
ing to different timespans are created and each of them is 
mapped separately. Note that any mapping technique can be 
used, from co-citation analysis to co-word analysis. Each map 
will represent a sort of “photograph” of the field under inves-
tigation in a certain timespan. The sequence of maps allows 
visualizing the temporal dynamics of the field. A second op-
tion consists in representing on the same map the trajectories 
of the units that change their relative position is subsequent 
maps (White and McCain 1998). A third option is animating 
the map: instead of a static visualization, a short movie is cre-
ated interpolating the layouts of the network in different mo-
ments (Leydesdorff and Schank 2008). 
The first maps including the temporal dimension, how-
ever, used a timeline to represent time. Garfield called them 
“historiographs” (Garfield 2004). In the timeline-based ap-
proach, each node of the network (classically, a publication 
in a citation network) is linked to a specific point in time 
(e.g., the publication year). The visualization, then, uses two 
dimensions: the vertical one is the timeline, whereas the hor-
izontal one is used to represent the relatedness of the items 
(Waltman and van Eck 2014). The result is a citation net-
work spread over a timeline. Garfield tested the validity of 
the historiographs as tools for reconstructing the history of 
science by comparing the narration of the discovery of the 
DNA written by Asimov with the historiograph based on 
the bibliographies of the corresponding publications (Gar-
field 1973). He found a good overlap between the two: the 
key events in the discovery according to Asimov appeared 
also in the historiograph. 
Alluvial maps are another form of timeline-based visuali-
zation. Starting from different phases in the evolution of a 
network, the networks relative to each phase are divided into 
different clusters, and then the trajectories of corresponding 
clusters in subsequent networks are visualized as a stream. 
The fusions and fissions of clusters over time is visualized as 
multiple streams flow over time (Rosvall and Bergstrom 
2010).21 
By combining co-citation mapping and temporal visual-
ization, an amazing visualization of the temporal develop-
ment of the journal Nature in the last 150 years was recently 
produced (Gates et al. 2019).22 
 
6.0 Interpreting a science map 
 
Interpreting a science map means linking the visual and ge-
ometrical properties of the map to substantive features of 
the mapped area or field. For instance, clusters of co-cited 
publications can be mapped to scientific sub-specialties or 
research topics, bibliographic coupling networks can be in-
terpreted as the research fronts of scientific specialties, co-
authorship networks as invisible colleges of scientists, and 
clusters of journals sharing many editors as structures of ac-
ademic power. The interpretation of science maps typically 
involves close interaction with experts of the mapped do-
main, i.e., experienced researchers that have a deep, albeit 
qualitative, knowledge of the structure of the target field 
(Tijssen 1993). Good science maps, however, should not be 
mere quantitative counterimages of the qualitative knowl-
edge of the domain experts. They should provide also new 
insights and useful knowledge for science policy purposes.  
An important aspect to consider in the interpretation is 
the level of analysis of the science map, i.e., the units of anal-
ysis and the type of relationship displayed by the map. Units 
and relations do not only affect the scale of the map, but also 
the dimension of the scientific enterprise that is captured. 
Term-based maps and citation-based maps using the docu-
ment as unit of analysis highlight the epistemic or cognitive 
dimension of science, what philosophers of science call the 
“context of justification” (Lucio-Arias and Leydesdorff 
2009). They show the shared epistemic base of a field 
(Persson 1994). However, they can overemphasize the sta-
bility of scientific knowledge, overshadowing the continu-
ous social negotiation of scientific claims (Knorr-Cetina 
2003). Co-authorship maps. author co-citation analysis, 
and interlocking editorship maps, on the other hand, shed 
light on the social network underlying science, i.e., the “con-
text of discovery” in philosophical terms. When the journal 
is selected as unit of analysis, the communication system is 
highlighted (Cozzens 1989). Hence, the different method-
ologies of science mapping offer a partial representation of 
the multi-dimensional nature of science and scholarship, 
that should be considered during the interpretative phase. 
General theories and models of the structure and dynam-
ics of science can also help in the interpretation of science 
maps, providing general interpretative insights (Boyack and 
Klavans 2019; Chen 2017; Scharnhorst, Börner, and Bes-
selaar 2012). At the same time, however, it is pivotal to con-
sider the specific academic and epistemic cultures of the 
field under study. The interpretation of a science map of a 
social scientific area, for instance, cannot be based on ex-
actly the same concepts than the interpretation of a science 
map of a biomedical area, as the social sciences and biomed-
icine differ in terms of research methods, epistemic culture, 
specialized terminology, use of the references, centrality of 
the journal system, and so on.  
The humanities are a good case in point to highlight the 
importance of the specificity of research areas. Science map-
ping and, more generally, scientometrics and bibliometrics, 
have mainly focused on the sciences since the times of Price 
and Garfield (Franssen and Wouters 2019). Bibliometric 
methods such as citation analysis were tailored to the cita-
tion norms and practices of the sciences. In the humanities, 
however, citations are frequently used not only to refer to 
other scholars’ work but also to point out sources and pri-
mary materials, the equivalent of experimental data for the 

Knowl. Org. 48(2021)No.7/8 
E. Petrovich. 2021. Science Mapping and Science Maps 
552 
sciences (Hellqvist 2009). Negative or contradictory cita-
tions of the works of other scholars are relatively more com-
mon than in the sciences. In fields such as philosophy, 
where argumentation is the key epistemic practice, critical 
citations play a central role (Petrovich 2018). These field-
specific citation practices must be considered in the inter-
pretation of citation-based science maps of humanistic areas 
(Hammarfelt 2016). Moreover, publications in the human-
ities frequently do not target (only) fellow scholars, but also 
the wider public audience (Nederhof 2006). This changes 
the level of specialized and standardized terminology used 
and, consequently, affect the capacity of term-based science 
maps to capture themes and topics.23 To these interpretative 
caveats, one should add the limitations of the existing data-
bases to adequately capture publications in the humanities, 
as they are often published as monographs and in national 
languages (Hammarfelt 2017). 
 
7.0 Science maps and the philosophy of science 
 
In this section, we deal with some epistemological and soci-
ological topics related to science mapping. We start by ask-
ing in what sense science maps offer objective representa-
tions of science, then, we discuss the difference between the 
published side of science and science in the making, and, 
lastly, we examine in more detail the meaning of citations. 
 
7.1 On the objectivity of science maps 
 
Are science maps an objective representation of the struc-
ture and dynamics of science? Clearly, the answer greatly de-
pends on the definition of objectivity we endorse (Daston 
and Galison 2007; Reiss and Sprenger 2017).  
In the previous sections, we saw how the creation of a sci-
ence map involves several methodological and technical deci-
sions from the science cartographer, such as the unit of anal-
ysis, the mapping technique, the normalization method, the 
visualization approach, the clustering algorithm, and so on 
(see Section 3.0: Building a science map). Each decision af-
fects the results and lead to different science maps. There-
fore, science maps, even when they are generated by com-
puter software, should not be conceived as free of human in-
tervention. Human choices occur frequently in the science 
map workflow and should be made transparent in order to 
warrant the reproducibility of science maps (Rafols, Porter 
and Leydesdorff 2010). Therefore, if we equate objectivity 
with the “lack of human intervention” (the so-called me-
chanical objectivity), then science maps, like any other map, 
are not “objective”. Rather, they result from a combination 
of the features of the mapped field, on the one hand, and the 
methodological decisions of the science cartographer on the 
other hand. However, we should acknowledge that no map 
(including geographic maps) is “objective” in this sense. On 
the other hand, if objectivity is intended as inter-subjective 
agreement, then science maps are objective in so far as they 
can be reproduced by different researchers, as long as that 
they follow the same methodology.  
A further sense of objectivity has not to do with a lack of 
human interventions but a lack of human biases. According 
to some authors, science maps are more objective than clas-
sic literature reviews precisely in the sense that science maps 
would avoid the potential biases of human experts (e.g., 
Catherine and Doehne 2018; Kreuzman 2001; Small and 
Griffith 1974; Weingart 2015). The idea is that the expert’s 
knowledge of a research field is inevitably constrained by his 
or her reading capacity: for how many papers one can read, 
they will always represent no more than a tiny portion of the 
literature available in most of the scientific fields. Even if 
such limitations can be mitigated by recurring to teamwork 
and by integrating the knowledge of many experts, the view 
of scientific fields that can be achieved in this way will al-
ways be partial. Thus, there is the potential risk that the rep-
resentations of the scientific fields are distorted by the ex-
perts’ viewpoint (if not prejudices). By contrast, the net-
works on which science maps are based are the result of mil-
lions of micro-actions performed by the scientific commu-
nity itself, such as the choice of certain references or words. 
Science maps allow keeping track of this myriad of micro-
actions. Consider for instance the bibliography of a research 
article. Since the authors cite other publications that are rel-
evant to their work, the bibliography can be conceived as a 
(very partial) representation of the field to which the paper 
belongs. In so far as each new contribution must be related, 
by references, to the existing body of knowledge (the field), 
each paper can be compared to a mirror that reflects, albeit 
partially, the entire field (Amsterdamska and Leydesdorff 
1989). It is a sort of “photograph” taken from a certain 
viewpoint. Hence, the aggregation of the bibliographies of 
thousands of articles that is performed to produce a cita-
tion-based map can be compared to the merging of thou-
sands of partial photographs to make up a single, overall pic-
ture. In this aggregation process, different publications are 
related to one another “unwittingly” by the scientific com-
munity itself. According to some authors, when enough 
large aggregates of publications are considered, the biases 
occurring in the individual bibliographies cancel out and a 
balanced picture is obtained (Van Raan 1998). The under-
lying assumption is that, at least on average, the citation be-
havior of scientists follows a normative model, i.e., that cita-
tions are given because of the scientific content of the cited 
reference and not because of non-scientific motives (see Sec-
tion 7.3: The meaning of citations). 
By the same token, the networks of words visualized in 
term-based maps allow reconstructing the terminology of a 
scientific field because they reflect thousands of terminolog-
ical micro-choices made by the researchers when drafting the 

Knowl. Org. 48(2021)No.7/8 
E. Petrovich. 2021. Science Mapping and Science Maps 
553 
titles and abstracts of their papers. The relations between the 
different terms are the results of these choices. Idiosyncratic 
and non-standard terminological would again choices cancel 
out when enough publications are considered. 
In sum, science maps would be more objective than clas-
sic reviews because they are the result of a bottom-up ap-
proach (Petrovich 2019b). Instead of the traditional top-
down approach that can potentially introduce biases in the 
field representation, science maps allow to represent “the 
point of view of the scientific community on itself” (Small 
1973; Small and Griffith 1974). Once again, science maps 
are not objective because free of human choices. Rather, 
they are objective because they are based on thousands of 
human (micro)choices. The key difference between these 
micro-choices and the decisions taken by the experts in the 
top-down approach lies in the large number of the former. 
It is such a large amount that potentially guarantees the can-
celling out of the biases and, thus, a more balanced repre-
sentation of scientific fields. Far from being the “view from 
nowhere” on science, science maps are the collection of 
multiple, situated viewpoints on science.  
A last point about the objectivity of science maps is 
worth stressing: even if science maps provide bottom-up 
representations of science, nonetheless they remain partial 
from some points of view. First, a science map cannot rep-
resent more than what is contained in the data on which it 
is based. Since the scope of data depends on the scope of the 
bibliographic databases, science mapping techniques will 
deliver very partial representations for those scholarly fields 
that are scarcely covered by current databases, such as some 
areas in the social sciences and humanities or scholarly pro-
duction in national languages (Franssen and Wouters 2019; 
Nederhof 2006). This does not mean that science maps pro-
vide false or distorted representations: rather that they ulti-
mately depend on the scope and limits of the data on which 
they are generated. The second reason why science maps are 
partial is subtler, and it has to do with the nature of the bib-
liographic data and how they represent the scientific activ-
ity. We discuss this topic in the next paragraph.  
 
7.2 Published science vs. science in the making 
 
A defining trait of standard science maps is that they are gen-
erated based on the metadata of scientific publications, as 
they are stored in bibliographic databases. However, publica-
tions (research articles, reviews, conference proceedings, pa-
tents, etc.) are only the final stage of a long and often rough 
research process. They are not meant and should not be con-
sidered as simple mirrors of the research practices themselves 
(Hyland and Salager-Meyer 2009; Wouters 1999a). The writ-
ing of a scientific paper involves the construction of a justifi-
catory structure in which each experiment and analysis con-
tribute to the justification of the paper’s claims (Gross et al. 
2002). As sociological and anthropological studies have re-
vealed, real research practices can be a lot less smooth than the 
accounts we find in the scientific papers (Knorr-Cetina 2003; 
Latour and Woolgar 1986; Townsend and Burgess 2009). 
Real research is full of false starts, blind alleys, and mistakes. 
Discoveries may occur because of serendipity or intuition, the 
order of the experiments can be different both from the re-
search plan and from the methodology described in the final 
paper, research targets may be affected by changes in funding, 
availability of materials and expertise, even academic circum-
stances. Moreover, scientific writing is a literary genre that fol-
lows precise rules, ranging from the format (e.g., the division 
of a research article into standard sections, such as Introduc-
tion, Methods, Results, and Discussion), to the writing style 
(in some fields, an impersonal style is recommended to in-
crease the “objectivity” of the results) (Bazerman 1988; Hy-
land and Salager-Meyer 2009; Swales 2004). Journals’ guide-
lines and peer-review reports can further affect the final form 
of a paper. 
Since standard science maps are based on the published 
side of science, they cannot be used to investigate any re-
search practice that is not recorded in publications. Most of 
what Bruno Latour has called the “science-in-action”, thus, 
remains out of the reach of standard science mapping based 
on bibliographic databases. Note, however, that science 
mapping as a method can be potentially applied to any rela-
tional feature of the scientific enterprise. Other relational 
features, describing the science-in-action, could be mapped 
by new science mapping techniques (for instance, informal 
exchanges between scientists at scientific congresses, e-mail 
flows between laboratories, informal collaboration networks 
not resulting in co-authorship, etc.). However, new ad hoc 
databases must be built to map these features, a costly and 
time-consuming enterprise (Boyack and Klavans 2019). 
 
7.3 The meaning of citations 
 
Citations are pivotal in science mapping: without the refer-
ence links connecting scientific publications, citation-based 
maps would be simply impossible. However, citations are a 
human product: they are the result of the choices made by 
the authors during the writing of their scientific papers. 
Why do scientists choose some references instead of others? 
Do they cite only because of the scientific merit of the cited 
works? How does the citation behavior of scientists change 
in different scientific fields? In traditional citation analysis 
and in standard science mapping, citations are treated 
equally, i.e., all have the same value. However, some cited pa-
pers are widely discussed, while others are perfunctorily 
cited. Some papers are even negatively cited. How can we 
capture the different functions and values of citations?  
Questions like these are discussed in scientometrics and 
sociology of science under the label of citation theory (Born-

Knowl. Org. 48(2021)No.7/8 
E. Petrovich. 2021. Science Mapping and Science Maps 
554 
mann and Daniel 2008; Cronin 1984; Wouters 1999b). Most 
of them are discussed since the dawn of citation analysis and 
still do not have received definite answers. A complete over-
view of citation theories is out of the scope of the present ar-
ticles.24 In this section, we will limit to present the two main 
approaches, in so far as they can help to interpret and contex-
tualize the results of science mapping: the normative theory 
and the socio-constructivist theory. 
The normative theory was proposed within the frame-
work of the normative sociology of science developed by 
Robert K. Merton and his school from the 1960s (Elkana et 
al. 1978; Kaplan 1965; Merton 1974). According to this the-
ory, scientists cite to pay their intellectual debts: when they 
use the results obtained by other scientists in their research, 
the norms of science demand them to acknowledge the debt 
by explicitly citing the relevant papers. Citations count as 
“pellets of peer recognition” and play a fundamental role in 
the reward system of science: they serve to distribute prestige 
among scientists. An important consequence of the norma-
tive theory is that citations can be considered as reliable prox-
ies of scientific quality or impact. Thus, the normative theory 
provides a theoretical justification for the use of citations in 
evaluative contexts. However, the main claim of the norma-
tive theory (i.e., that the citation reflects the scientific merit 
of the cited document, author, or journal) rests upon several 
assumptions, e.g., that citations are made to the best possible 
works, that all citations have equal weight, and that the cita-
tion of a document implies the use of the document by the 
citing author (Nicolaisen 2007). Both the main claim and the 
underlying assumptions have been criticized. 
The socio-constructivist approach to citations is 
grounded in the socio-constructivist sociology of science, a 
sociological paradigm that raised in different forms in the 
1970s partly as a reaction to the normative school (Bloor 
1991; Knorr-Cetina 2003; Latour 2003). According to socio-
constructivists, scientific facts are the result of an intricate 
process of social negotiation among different actors. In the 
social arena of science, scientists use any means necessary to 
advance their claims and achieve a high status in the scientific 
community. No normative system, such as the one described 
by Merton, governs their actions. Socio-constructivists main-
tain that citations play a key role in the social negotiation of 
scientific facts. In particular, they are used as means of per-
suasion: scientists trade on the authority of the cited authors 
to strengthen their claims. Citations are rhetorical devices 
that can be compared to “defense lines” prepared by the sci-
entists to defend their results from criticisms of adversary sci-
entists. Socio-constructivists note also that scientists often 
distort the content of the documents they cite, in order to 
show agreement with authoritative sources even when no 
such an agreement exists. The reason is that scientists would 
be more interested in who they cite, rather than in what the 
cited documents say. Citations, therefore, would reflect the 
social dynamics of the scientific community, rather than the 
accumulation of scientific knowledge. An important conse-
quence is that they cannot be used as proxies of scientific 
quality (MacRoberts and MacRoberts 2018). 
Empirical research has shown that neither the normative 
nor the socio-constructivist theory offer, alone, complete 
explanations of the citation behavior of scientists. The mo-
tivations for citing are complex and multi-dimensional: 
sometimes they reflect purely scientific reasons, as the nor-
mative theory holds, and sometimes obey to social-network-
ing purposes, as the socio-constructivist theory holds 
(Tahamtan and Bornmann 2018). Besides the motivations 
of scientists, also the characteristics of the communication 
system of science (journals, publishers, and so on) affect the 
probability of receiving citations (Cozzens 1989). For in-
stance, publications in languages different from English 
tend to receive, on average, fewer citations, whereas review 
articles tend to attract more citations than research articles 
(Bornmann and Daniel 2008). The citation links between 
documents and authors, therefore, are affected by many dif-
ferent factors, of which scientific merit is only one.  
When interpreting the results of citation-based science 
mapping, we should not overlook the complexity of the ci-
tation practices that determine the links in the citation net-
work. An understanding of the “citation culture” (Wouters 
1999a) of the mapped field helps to interpret correctly a sci-
ence map. 
 
8.0 Science maps and science policy 
 
Since the first experiments in science mapping in the 1970s, 
science maps have been presented recurrently as helpful de-
vices for science policy and research management. The idea 
is that, since science maps offer a panoramic viewpoint of 
the research landscape, they can also help to navigate it. Sci-
ence maps would offer for the abstract space of science the 
same service of orientation that geographic maps provide 
for the physical space (Small 1999).  
Possible science policy topics that can be addressed with 
the help of science maps include (Boyack, Klavans, and 
Börner 2005; Rafols, Porter, and Leydesdorff 2010):  
 
a) Benchmarking: How is an organization perform-
ing compared to competitors? 
b) Collaboration strategy: Who are the potential col-
laborators that can complement the research mis-
sion of the organization? 
c) Development analysis: How do the research themes 
of an organization develop over time? 
d) “Hot areas” detection: What are the scientific areas 
that are growing faster? What is their potential for 
technological transfer? 
 

Knowl. Org. 48(2021)No.7/8 
E. Petrovich. 2021. Science Mapping and Science Maps 
555 
One important advantage of science maps compared to clas-
sic reviews is that they allow also the non-experts to grasp 
easily and quickly the main features of a scientific field be-
cause they rely on the recognition of visual patterns rather 
than on deep scientific expertise. Therefore, they can be 
used as a common base between researchers, science manag-
ers, analysts, and policymakers to discuss strategic decisions, 
such as the allocation of resources (Börner et al. 2012; Noy-
ons and Calero-Medina 2009). 
Nonetheless, science maps should be used in science pol-
icy contexts with a clear understanding of their limits: sci-
ence maps can help the decision-making, but they do not 
provide automatic answers. From this point of view, science 
maps are not different from any scientometric indicator: 
they provide partial representations of science whose cor-
rect interpretation should take into account many different 
factors (see Section 7.1: On the objectivity of science 
maps).[25] Not only science maps are error-prone (e.g., if 
they are generated based on an incorrect field delineation 
procedure, see Section 3.2: Field delineation), but, as we saw 
above, their production involves several technical decisions 
that can deeply influence the final maps (see Section 4.1.3: 
Normalization and Section 4.1.4: Visualization). It is piv-
otal that such decisions should be made transparent, and 
their consequences clear to the analysts and the policymak-
ers, so that science maps do not turn into “black boxes” (Ra-
fols, Porter and Leydesdorff 2010). 
Fortunately, science maps are usually perceived as more 
complex objects, compared to mono-dimensional scien-
tometric indicators such as citation counts or the Journal Im-
pact Factor. Thus, they tend to stimulate a higher level of re-
flexivity in their users compared to sheer numbers. Such re-
flexivity should always be preserved in science policy contexts, 
where science maps must not be treated as “oracles”, even 
when science politicians and research managers desire simple 
and straightforward answers. When using science maps, it 
must be remembered that science is a complex system, where 
simple, ready-made answers can be given very rarely.  
 
9.0 Conclusion 
 
In this paper we have seen how the visual representation of 
science by science maps takes different forms, depending on 
the kind of data, the unit of analysis, the type of relation ex-
amined, and the overall mapping approach used. A science 
map can take both the form of a bibliometric network and 
that of a geographic map or of a patent map. Even artistic 
representations of the sciences have been called, in a derivate 
way, “science maps” (Börner 2010). Science maps find ap-
plication is different domains, from sociology of science to 
science policy, from scientometrics to information visuali-
zation. As we have seen, science mapping, as a body of tech-
niques, stands at the crossroad of numerous disciplines: sci-
entometrics, library and information science, citation anal-
ysis, text analysis, statistics, network analysis, among others.  
Given this manifold of methods, disciplines, and uses, it 
is difficult to find a common trait that identifies the 
uniqueness of science mapping. Perhaps, what most if not 
all science maps share is a bottom-up approach to the inves-
tigation of the structure and dynamics of science (Petrovich 
2019b). Compared with top-down knowledge organization 
systems (KOSs), science maps aim at representing science 
starting from the scientific products themselves rather than 
from more or less a priori conceptual schemes. In this sense, 
they may capture those structuration forces that shape the 
overall configuration of the scientific system and that may 
remain invisible to top-down KOSs. Science mapping may 
be valuable to shed light on the self-organizing properties of 
the scientific enterprise (Lucio-Arias and Leydesdorff 
2009). Hence, we think that science maps can be of interest 
for all the branches of meta-science, from library and infor-
mation science to sociology of science, from knowledge or-
ganization to epistemology.  
 
Acknowledgments 
 
I am grateful to Alberto Baccini, Emiliano Tolusso, two 
anonymous reviewers, and the Editor Birger Hjørland for 
helpful comments and suggestions on a previous version of 
this paper. I gratefully acknowledge financial support from 
the Institute for New Economic Thinking (INET) under 
grant n° INO19-00023. 
 
Notes 
 
1.  http://scimaps.org/home.html 
2.  https://en.wikipedia.org/wiki/Liberal_arts_education 
#/media/File:Hortus_Deliciarum,_Die_Philosophie_ 
mit_den_sieben_freien_K%C3%BCnsten.JPG 
3.  Numerous examples of classifications and visual repre-
sentations of the sciences over the centuries can be 
found and explored in the Interactive Atlas of the Disci-
plines (http://atlas-disciplines.unige.ch/). 
4.  A detailed timeline with key milestones in science map-
ping history can be found in the Part 2 of Börner (2010). 
5.  https://academic.microsoft.com/ 
6.  https://www.dimensions.ai/ 
7.  https://www.uspto.gov/  
8.  http://www.google.com/patents.  
9.  http://www.epo.org/patents/patent-information.html.  
10.  This is the adjacency matrix we obtain when we consider 
the network as directed, i.e., when we distinguish between 
the sender and the receiver of the citation. It is also possi-
ble to consider the citation network as undirected. In this 
case, the elements of the matrix will be set to 1 when there 
is a link between the publications, independently whether 

Knowl. Org. 48(2021)No.7/8 
E. Petrovich. 2021. Science Mapping and Science Maps 
556 
it is a citation (in-coming link) or a reference (out-going 
link), obtaining a symmetrical matrix:  
 
 
a 
b 
c 
d 
e 
f 
g 
h 
a 
0 
1 
1 
1 
1 
0 
0 
0 
b 
1 
0 
1 
0 
0 
0 
0 
1 
c 
1 
1 
0 
0 
1 
1 
1 
0 
d 
1 
0 
0 
0 
0 
0 
1 
0 
e 
1 
0 
1 
0 
0 
0 
1 
0 
f 
0 
0 
1 
0 
0 
0 
1 
0 
g 
0 
0 
1 
1 
1 
1 
0 
0 
h 
0 
1 
0 
0 
0 
0 
0 
0 
 
11.  Note that there are two different similarity measures, a 
direct and an indirect, both called “cosine”. The indi-
rect cosine (that corresponds to the original cosine in-
troduce by Salton and McGill (Salton and McGill 
1983)) is based on the angular distance between two 
vectors and it is calculated from the inner product of 
the vectors (Jones and Furnas 1987). The direct cosine 
is a simplified version of the indirect cosine and it cor-
responds to a variant of the Ochiai coefficient (Zhou 
and Leydesdorff 2016). 
12.  An interesting alternative visualization, closely mod-
elled on geographic maps, is based on the so-called self-
organizing maps (SOM). We refer to (Skupin, Bib-
erstine, and Börner 2013) for a detailed explanation of 
this technically advanced visualization method. 
13.  https://gephi.org/ 
14.  http://mrvar.fdv.uni-lj.si/pajek/ 
15.  Note that not all the similarity measures fulfill the re-
quirements of a distance metric. For instance, negative 
similarity measures (such as the ones produced by Pear-
son’s r) cannot be used as distances because a negative 
distance is meaningless. The other conditions to be sat-
isfied are that the distance of an object from itself should 
be zero, that the distance between A and B should be 
equal to the distance between B and A (symmetry), and 
that the distance from A to B is at most as large as the 
sum of the distance from A to C and the distance 
from C to B (triangle inequality). 
16.  A technical but very clear explanation of MDS can be 
found in (Borg and Groenen 2010, chaps 1–3) and in 
(van Eck et al. 2010). 
17.  It is easy to see that it is a consequence of the triangle 
inequality mentioned in the note above. 
18.  More precisely, shortest paths. 
19.  Hennig et al. (2016) offers an overview and technical 
discussion of clustering techniques. 
20.  From this point of view, the history of the JEL codes 
used in economics is very instructive (Cherrier 2017). 
21.  A tool for generating alluvial maps starting from net-
work data is available at https://www.mapequa-
tion.org/alluvial/  
22.  The map can be explored at https://www.nature.com/ 
immersive/d41586-019-03165-4/index.html A video 
explaining the structure of the map is available at 
https://www.youtube.com/watch?v=GW4s58u8PZo 
&feature=youtu.be 
23.  I am grateful to an anonymous reviewer for pointing me 
out this difference in the use of specific terminology be-
tween the sciences and humanities. 
24.  See Tahamtan and Bornmann (2018; 2019) for an up-
dated overview and Petrovich (2019a) for a systematiza-
tion of the different theories. 
25.  As it is well known, the use of scientometrics for evalu-
ative purpose is a controversial topic that continue to 
raise heated discussions among researchers and policy 
makers. The presentation of this topic, however, falls 
beyond the scope of this article. See Aksnes, Langfeldt, 
and Wouters (2019) for an introduction. 
 
References 
 
Ahlgren, Per, Bo Jarneving and Ronald Rousseau. 2003. 
“Requirements for a Cocitation Similarity Measure, 
with Special Reference to Pearson’s Correlation Coeffi-
cient.” Journal of the American Society for Information 
Science and Technology 54: 550–60. https://doi.org/10. 
1002/asi.10242 
Aksnes, Dag W., Liv Langfeldt and Paul Wouters. 2019. 
“Citations, Citation Indicators, and Research Quality: 
An Overview of Basic Concepts and Theories.” SAGE 
Open 9, no. 1: 215824401982957. https://doi.org/10. 
1177/2158244019829575 
Amsterdamska, Olga and L. Leydesdorff. 1989. “Citations: 
Indicators of Significance?” Scientometrics 15: 449–71. 
https://doi.org/10.1007/BF02017065 
Åström, Fredrik, Björn Hammarfelt and Joachim Hansson. 
2017. “Scientific Publications as Boundary Objects: 
Theorising the Intersection of Classification and Re-
search Evaluation.” Information Research 22, no. 1: 
colis1623. 
Baccini, Alberto and Lucio Barabesi. 2010. “Interlocking 
Editorship. A Network Analysis of the Links between 
Economic Journals.” Scientometrics 82: 365–89. https:// 
doi.org/10.1007/s11192-009-0053-7 
Baccini, Alberto, Lucio Barabesi, Yves Gingras and Mahdi 
Kalfaoui. 2020. “Intellectual and Social Similarity 
among Scholarly Journals. An Exploratory Comparison 
of the Networks of Editors, Authors and Co-Citations.” 
Quantitative Science Studies 1: 277–89. doi: https:// 
doi.org/10.1162/qss_a_00006 

Knowl. Org. 48(2021)No.7/8 
E. Petrovich. 2021. Science Mapping and Science Maps 
557 
Barabási, Albert-László. 2014. Linked: How Everything Is 
Connected to Everything Else and What It Means for 
Business, Science, and Everyday Life. New York: Basic 
Books. 
Bazerman, Charles. 1988. Shaping Written Knowledge: The 
Genre and Activity of the Experimental Article in Science. 
Rhetoric of the Human Sciences. Madison, WI: Univer-
sity of Wisconsin Press. 
Bloor, David. 1991. Knowledge and Social Imagery. 2nd ed. 
Chicago: University of Chicago Press. 
Borg, Ingwer and Patrick J. F Groenen. 2010. Modern Mul-
tidimensional Scaling: Theory and Applications. New 
York; London: Springer. 
Börner, Katy. 2010. Atlas of Science: Visualizing What We 
Know. Cambridge, MA: MIT Press. 
Börner, Katy, Chaomei Chen and Kevin W. Boyack. 2005. 
“Visualizing Knowledge Domains.” Annual Review of In-
formation Science and Technology 37: 179–255. https:// 
doi.org/10.1002/aris.1440370106 
Börner, Katy, Richard Klavans, Michael Patek, Angela M. 
Zoss, Joseph R. Biberstine, Robert P. Light, Vincent 
Larivière and Kevin W. Boyack. 2012. “Design and Up-
date of a Classification System: The UCSD Map of Sci-
ence.” PLoS ONE 7, no. 7: e39464. https://doi.org/10. 
1371/journal.pone.0039464 
Börner, Katy, Shashikant Penumarthy, Mark Meiss and Wei-
mao Ke. 2006. “Mapping the Diffusion of Scholarly 
Knowledge among Major U.S. Research Institutions.” 
Scientometrics 68: 415–26. https://doi.org/10.1007/s11 
192-006-0120-2 
Börner, Katy, Todd N. Theriault and Kevin W. Boyack. 
2015. “Mapping Science Introduction: Past, Present and 
Future: Mapping Science Introduction: Past, Present 
and Future.” Bulletin of the Association for Information 
Science and Technology 41, no. 2: 12–16. https://doi. 
org/10.1002/bult.2015.1720410205 
Bornmann, Lutz and Hans‐Dieter Daniel. 2008. “What Do 
Citation Counts Measure? A Review of Studies on Cit-
ing Behavior.”. Journal of Documentation 64: 45–80. 
https://doi.org/10.1108/00220410810844150 
Boyack, Kevin W. and Richard Klavans. 2008. “Measuring 
Science–Technology Interaction Using Rare Inventor–
Author Names.” Journal of Informetrics 2: 173–82. 
https://doi.org/10.1016/j.joi.2008.03.001 
Boyack, Kevin W. and Richard Klavans. 2010. “Co-Cita-
tion Analysis, Bibliographic Coupling, and Direct Cita-
tion: Which Citation Approach Represents the Re-
search Front Most Accurately?” Journal of the American 
Society for Information Science and Technology 61: 2389–
2404. https://doi.org/10.1002/asi.21419 
Boyack, Kevin W. and Richard Klavans. 2019. “Creation 
and Analysis of Large-Scale Bibliometric Networks.” In 
Springer Handbook of Science and Technology Indicators, 
edited by Wolfgang Glänzel, Henk F. Moed, Ulrich 
Schmoch and Mike Thelwall. Springer Handbooks. 
Cham: Springer International Publishing, 187–212. 
https://doi.org/10.1007/978-3-030-02511-3_8 
Boyack, Kevin W., Richard Klavans and Katy Börner. 2005. 
“Mapping the Backbone of Science.” Scientometrics 64: 
351–74. https://doi.org/10.1007/s11192-005-0255-6 
Callon, Michel, J. P. Courtial and F. Laville. 1991. “Co-
Word Analysis as a Tool for Describing the Network of 
Interactions between Basic and Technological Research: 
The Case of Polymer Chemsitry.” Scientometrics 22: 
155–205. https://doi.org/10.1007/BF02019280 
Callon, Michel, J.-P. Courtial, W. A. Turner and S. Bauin. 
1983. “From Translations to Problematic Networks: An 
Introduction to Co-Word Analysis.” Social Science Infor-
mation 22: 191–235. https://doi.org/10.1177/0539018 
83022002003 
Callon, Michel, John Law and Arie Rip (Eds.). 1998. Map-
ping the Dynamics of Science and Technology: Sociology of 
Science in the Real World. Transferred to digital printing. 
Houndmills: Macmillan. 
Catherine, Herfeld and Malte Doehne. 2018. “Five Reasons 
for the Use of Network Analysis in the History of Eco-
nomics.” Journal of Economic Methodology 25: 311–28. 
https://doi.org/10.1080/1350178X.2018.1529172 
Chen, Chaomei. 2006. “CiteSpace II: Detecting and Visu-
alizing Emerging Trends and Transient Patterns in Scien-
tific Literature.” Journal of the American Society for In-
formation Science and Technology 57: 359–77. https:// 
doi.org/10.1002/asi.20317 
Chen, Chaomei. 2013. Mapping Scientific Frontiers: The 
Quest for Knowledge Visualization. Second Edition. 
London: Springer. 
Chen, Chaomei. 2017. “Science Mapping: A Systematic 
Review of the Literature.” Journal of Data and Infor-
mation Science 2, no. 2: 1–40. https://doi.org/10.1515/ 
jdis-2017-0006 
Chen, Chaomei, Fidelia Ibekwe-SanJuan and Jianhua Hou. 
2010. “The Structure and Dynamics of Cocitation Clus-
ters: A Multiple-Perspective Cocitation Analysis.” Jour-
nal of the American Society for Information Science and 
Technology 61: 1386–409. https://doi.org/10.1002/asi. 
21309 
Cherrier, Beatrice. 2017. “Classifying Economics: A His-
tory of the JEL Codes.” Journal of Economic Literature 
55: 545–79. https://doi.org/10.1257/jel.20151296 
Cobo, M.J., A.G. López-Herrera, E. Herrera-Viedma and F. 
Herrera. 2011a. “An Approach for Detecting, Quantify-
ing, and Visualizing the Evolution of a Research Field: A 
Practical Application to the Fuzzy Sets Theory Field.” 
Journal of Informetrics 5: 146–66. https://doi.org/ 
10.1016/j.joi.2010.10.002 

Knowl. Org. 48(2021)No.7/8 
E. Petrovich. 2021. Science Mapping and Science Maps 
558 
Cobo, M.J., A.G. López-Herrera, E. Herrera-Viedma and F. 
Herrera. 2011b. “Science Mapping Software Tools: Re-
view, Analysis, and Cooperative Study among Tools.” 
Journal of the American Society for Information Science 
and Technology 62: 1382–402. https://doi.org/10.1002/ 
asi.21525 
Courtial, J. P. 1998. “Comments on Leydesdorff’s Article.” 
Journal of the American Society for Information Science 
49: 98. 
Cozzens, Susan E. 1989. “What Do Citations Count? The 
Rhetoric-First Model.” Scientometrics 15: 437–47. 
https://doi.org/10.1007/BF02017064 
Crane, Diana. 1967. “The Gatekeepers of Science: Some 
Factors Affecting the Selection of Articles for Scientific 
Journals.” The American Sociologist 2: 195–201. 
Crane, Diana. 1972. Invisible Colleges; Diffusion of Knowl-
edge in Scientific Communities. Chicago: University of 
Chicago Press. 
Cronin, Blaise. 1984. The Citation Process: The Role and 
Significance of Citations in Scientific Communication. 
London: T. Graham. 
Cronin, Blaise. 2001. “Hyperauthorship: A Postmodern 
Perversion or Evidence of a Structural Shift in Scholarly 
Communication Practices?” Journal of the American So-
ciety for Information Science and Technology 52: 558–69. 
https://doi.org/10.1002/asi.1097 
Daston, Lorraine and Peter Galison. 2007. Objectivity. New 
York; Cambridge, MA: Zone Books.  
Eck, Nees Jan van and Ludo Waltman. 2008. “Appropriate 
Similarity Measures for Author Co‐citation Analysis.” 
Journal of the American Society for Information Science 
and Technology 59: 1653–61. https://doi.org/10.1002/ 
asi.20872 
Eck, Nees Jan van and Ludo Waltman. 2009. “How to Nor-
malize Cooccurrence Data? An Analysis of Some Well-
Known Similarity Measures.” Journal of the American 
Society for Information Science and Technology 60: 1635–
51. https://doi.org/10.1002/asi.21075 
Eck, Nees Jan van and Ludo Waltman. 2010. “Software Sur-
vey: VOSviewer, a Computer Program for Bibliometric 
Mapping.” Scientometrics 84: 523–38. https://doi.org/ 
10.1007/s11192-009-0146-3 
Eck, Nees Jan van, Ludo Waltman, Rommert Dekker and 
Jan van den Berg. 2010. “A Comparison of Two Tech-
niques for Bibliometric Mapping: Multidimensional 
Scaling and VOS.” Journal of the American Society for In-
formation Science and Technology 61: 2405–16. https:// 
doi.org/10.1002/asi.21421 
Elkana, Yehuda, Joshua Laderberg, Robert K. Merton, Ar-
nold Thackray and Harriet Zuckerman (Eds.). 1978. To-
ward a Metric of Science: The Advent of Science Indica-
tors. (Science, Culture & Society). New York: Wiley. 
Federico, Paolo, Florian Heimerl, Steffen Koch and Silvia 
Miksch. 2017. “A Survey on Visual Approaches for Ana-
lyzing Scientific Literature and Patents.”. IEEE Transac-
tions on Visualization and Computer Graphics 23: 2179–
98. https://doi.org/10.1109/TVCG.2016.2610422 
Finnegan, Diarmid. 2015. “Science, Geography Of”. In In-
ternational Encyclopedia of the Social & Behavioral Sci-
ences. Vol. 21. Amsterdam: Elsevier, 236–40. 
Franssen, Thomas and Paul Wouters. 2019. “Science and Its 
Significant Other: Representing the Humanities in Bib-
liometric Scholarship.” Journal of the Association for In-
formation Science and Technology 70: 1124-37. https:// 
doi.org/10.1002/asi.24206 
Frenken, Koen, Sjoerd Hardeman and Jarno Hoekman. 
2009. “Spatial Scientometrics: Towards a Cumulative 
Research Program.” Journal of Informetrics 3: 222–32. 
https://doi.org/10.1016/j.joi.2009.03.005 
Garfield, Eugene. 1973. “Historiographs, Librarianship, 
and the History of Science.” In Toward a Theory of Li-
brarianship, edited by Conrad H. Rawski. Metuchen, 
NJ: Scarecrow Press, 380–402. 
Garfield, Eugene. 2004. “Historiographic Mapping of 
Knowledge Domains Literature.” Journal of Infor-
mation Science 30: 119–45. https://doi.org/10.1177/ 
0165551504042802 
Gates, Alexander J., Qing Ke, Onur Varol and Albert-László 
Barabási. 2019. “Nature’s Reach: Narrow Work Has 
Broad Impact.” Nature 575, no. 7781: 32–34. https:// 
doi.org/10.1038/d41586-019-03308-7 
Glänzel, Wolfgang. 2001. “National Characteristics in In-
ternational Scientific Co-Authorship Relations.” Scien-
tometrics 51: 69–115. https://doi.org/10.1023/A:1010 
512628145 
Gross, Alan G., Alan G. Gross, Joseph E. Harmon and Mi-
chael S. Reidy. 2002. Communicating Science: The Scien-
tific Article from the 17th Century to the Present. Oxford; 
New York: Oxford University Press. 
Hammarfelt, Björn. 2016. “Beyond Coverage: Toward a 
Bibliometrics for the Humanities.” In Research Assess-
ment in the Humanities, edited by Michael Ochsner, 
Sven E Hug and Hans-Dieter Daniel. Springer, 115–31. 
Hammarfelt, Björn. 2017. “Four Claims on Research As-
sessment and Metric Use in the Humanities.” Bulletin of 
the Association for Information Science and Technology 
43, no. 5: 33–8. 
Harzing, Anne-Wil. 2019. “Two New Kids on the Block: 
How Do Crossref and Dimensions Compare with 
Google Scholar, Microsoft Academic, Scopus and the 
Web of Science?” Scientometrics 120: 341–49. https:// 
doi.org/10.1007/s11192-019-03114-y 
He, Qin. 1999. “Knowledge Discovery through Co-Word 
Analysis.” Library Trends 48: 133. 

Knowl. Org. 48(2021)No.7/8 
E. Petrovich. 2021. Science Mapping and Science Maps 
559 
Hellqvist, Björn. 2009. “Referencing in the Humanities 
and Its Implications for Citation Analysis.” Journal of the 
American Society for Information Science and Technology 
61: 310-18. https://doi.org/10.1002/asi.21256 
Hennig, Christian M., Marina Meilă, Fionn Murtagh and 
Roberto Rocci (Eds.). 2016. Handbook of Cluster Anal-
ysis. Chapman & Hall/CRC Handbooks of Modern 
Statistical Methods 9. Boca Raton: CRC Press. 
Hjørland, Birger. 2013. “Citation Analysis: A Social and Dy-
namic Approach to Knowledge Organization.” Infor-
mation Processing & Management 49: 1313–25. https:// 
doi.org/10.1016/j.ipm.2013.07.001 
Hyland, Ken and Françoise Salager-Meyer. 2009. “Scien-
tific Writing.” Annual Review of Information Science 
and Technology 42: 297–338. https://doi.org/10.1002/ 
aris.2008.1440420114 
ICMJE, International Committee of Medical Journal Edi-
tors. 2019. Recommendations for the Conduct, Reporting, 
Editing, and Publication of Scholarly Work in Medical 
Journals. http://www.icmje.org/icmje-recommendations. 
pdf 
Jaffe, Adam B. and Manuel Trajtenberg. 2002. Patents, Ci-
tations, and Innovations: A Window on the Knowledge 
Economy. Cambridge, MA: MIT Press. 
Jones, William P. and George W Furnas. 1987. “Pictures of 
Relevance: A Geometric Analysis of Similarity 
Measures.” Journal of the American Society for Infor-
mation Science 38: 420–42. 
Kaplan, N. 1965. “The Norms of Citation Behavior. Prole-
gomena to the Footnote.” American Documentation 16, 
no. 3: 179–87. 
Katz, J.Sylvan and Ben R. Martin. 1997. “What Is Research 
Collaboration?” Research Policy 26: 1–18. https:// 
doi.org/10.1016/S0048-7333(96)00917-1 
Kessler, M.M. 1963. “Bibliographic Coupling Extended in 
Time: Ten Case Histories.” Information Storage and Re-
trieval 1: 169–87. https://doi.org/10.1016/0020-0271 
(63)90016-0 
Knorr-Cetina, K. 2003. Epistemic Cultures: How the Sciences 
Make Knowledge. Cambridge MA: Harvard University 
Press. 
Kreuzman, Henry. 2001. “A Co-Citation Analysis of Rep-
resentative Authors in Philosophy: Examining the Rela-
tionship between Epistemologists and Philosophers of 
Science.” Scientometrics 51: 525–39. 
Kuhn, Thomas S. 2000. The Road since Structure: Philo-
sophical Essays, 1970-1993, with an Autobiographical In-
terview, edited by James Conant and John Haugeland. 
Chicago: University of Chicago Press. 
Larivière, Vincent, Nadine Desrochers, Benoît Macaluso, 
Philippe Mongeon, Adèle Paul-Hus and Cassidy R 
Sugimoto. 2016. “Contributorship and Division of La-
bor in Knowledge Production.” Social Studies of Science 
46: 417–35. https://doi.org/10.1177/03063127166500 
46 
Latour, Bruno. 2003. Science in Action: How to Follow Scien-
tists and Engineers through Society. Cambridge, MA: 
Harvard University Press. 
Latour, Bruno and Steve Woolgar. 1986. Laboratory Life: 
The Construction of Scientific Facts. Princeton, NJ: 
Princeton University Press. 
Laudel, Grit. 2002. “What Do We Measure by Co-Author-
ships?” Research Evaluation 11, no. 1: 3–15. https:// 
doi.org/10.3152/147154402781776961 
Laurens, Patricia, Michel Zitt and Elise Bassecoulard. 2010. 
“Delineation of the Genomics Field by Hybrid Citation-
Lexical Methods: Interaction with Experts and Valida-
tion Process.” Scientometrics 82: 647–62. https://doi. 
org/10.1007/s11192-010-0177-9 
Law, J. and J. Whittaker. 1992. “Mapping Acidification Re-
search: A Test of the Co-Word Method.” Scientometrics 
23: 417–61. https://doi.org/10.1007/BF02029807 
Lee, Sungjoo, Byungun Yoon and Yongtae Park. 2009. “An 
Approach to Discovering New Technology Opportuni-
ties: Keyword-Based Patent Map Approach.” Technova-
tion 29: 481–97. https://doi.org/10.1016/j.technovation. 
2008.10.006 
Leydesdorff, Loet. 1987. “Various Methods for the Map-
ping of Science.” Scientometrics 11: 295–324. https:// 
doi.org/10.1007/BF02279351 
Leydesdorff, Loet. 1997. “Why Words and Co‐words Can-
not Map the Development of the Sciences.” Journal of 
the American Society for Information Science 48: 418. 
Leydesdorff, Loet. 2001. The Challenge of Scientometrics: 
The Development, Measurement, and Self-Organization 
of Scientific Communications. 2nd edition. Parkland, IL: 
Universal. 
Leydesdorff, Loet. 2004. “Clusters and Maps of Science 
Journals Based on Bi‐connected Graphs in Journal Cita-
tion Reports.” Journal of Documentation 60: 371–427. 
https://doi.org/10.1108/00220410410548144 
Leydesdorff, Loet. 2007. “Betweenness Centrality as an In-
dicator of the Interdisciplinarity of Scientific Journals.” 
Journal of the American Society for Information Science 
and Technology 58: 1303–19. https://doi.org/10.1002/ 
asi.20614 
Leydesdorff, Loet. 2008. “On the Normalization and Visu-
alization of Author Co-Citation Data: Salton’s Cosine 
versus the Jaccard Index.” Journal of the American Society 
for Information Science and Technology 59: 77–85. 
https://doi.org/10.1002/asi.20732 
Leydesdorff, Loet and Robert L. Goldstone. 2014. “Interdis-
ciplinarity at the Journal and Specialty Level: The Chang-
ing Knowledge Bases of the Journal Cognitive Science.” 
Journal of the Association for Information Science and Tech-
nology 65: 164–77. https://doi.org/10.1002/asi.22953 

Knowl. Org. 48(2021)No.7/8 
E. Petrovich. 2021. Science Mapping and Science Maps 
560 
Leydesdorff, Loet and Olle Persson. 2010. “Mapping the 
Geography of Science: Distribution Patterns and Net-
works of Relations among Cities and Institutes.” Journal 
of the American Society for Information Science and Tech-
nology, 61: 1622-34. https://doi.org/10.1002/asi.21347 
Leydesdorff, Loet and Ismael Rafols. 2009. “A Global Map 
of Science Based on the ISI Subject Categories.” Journal 
of the American Society for Information Science and Tech-
nology 60: 348–62. https://doi.org/10.1002/asi.20967 
Leydesdorff, Loet and Thomas Schank. 2008. “Dynamic 
Animations of Journal Maps: Indicators of Structural 
Changes and Interdisciplinary Developments.” Journal 
of the American Society for Information Science and Tech-
nology 59: 1810–18. https://doi.org/10.1002/asi.20891 
Lima, Manuel. 2014. The Book of Trees: Visualizing Branches 
of Knowledge. New York: Princeton Architectural Press. 
Liu, Xiaoming, Johan Bollen, Michael L. Nelson and Her-
bert Van de Sompel. 2005. “Co-Authorship Networks in 
the Digital Library Research Community.” Information 
Processing & Management 41: 1462–80. https://doi. 
org/10.1016/j.ipm.2005.03.012 
Livingstone, David N. 2003. Putting Science in Its Place: Ge-
ographies of Scientific Knowledge. Chicago: University of 
Chicago Press. 
Lucio-Arias, Diana and Loet Leydesdorff. 2009. “The Dy-
namics of Exchanges and References among Scientific 
Texts, and the Autopoiesis of Discursive Knowledge.” 
Journal of Informetrics 3: 261–71. https://doi.org/10. 
1016/j.joi.2009.03.003 
MacRoberts, Michael H. and Barbara R. MacRoberts. 
2018. “The Mismeasure of Science: Citation Analysis.” 
Journal of the Association for Information Science and 
Technology 69: 474–82. https://doi.org/10.1002/asi.23 
970 
Marshakova, Irena. 1973. “System of Document Connec-
tions Based on References.” Nauchno-Tekhnicheskaya 
Informatsiya Seriya 2-Informatsionnye Protsessy I Sis-
temy 2, no. 6: 3–8. 
Mazzocchi, Fulvio. 2018. “Knowledge Organization System 
(KOS).” Knowledge Organization 45: 54–78. 
McCain, Katherine W. 1990. “Mapping Authors in Intel-
lectual Space: A Technical Overview.” Journal of the 
American Society for Information Science 41: 433–43. 
McCain, Katherine W. 1991. “Mapping Economics 
through the Journal Literature: An Experiment in Jour-
nal Cocitation Analysis.” Journal of the American Society 
for Information Science 42: 290–96. https://doi.org/ 
10.1002/(SICI)1097-4571(199105)42:4<290::AID-AS 
I5>3.0.CO;2-9 
Merton, Robert K. 1974. The Sociology of Science: Theoreti-
cal and Empirical Investigations. Chicago: Univ. of Chi-
cago Press. 
Meyer, Martin. 2000. “Does Science Push Technology? Patents 
Citing Scientific Literature.” Research Policy 29: 409–34. 
https://doi.org/10.1016/S0048-7333(99)00040-2 
Moral-Munoz, Jose A., Antonio G. López-Herrera, Enrique 
Herrera-Viedma and Manuel J. Cobo. 2019. “Science 
Mapping Analysis Software Tools: A Review.” In Springer 
Handbook of Science and Technology Indicators, edited by 
Wolfgang Glänzel, Henk F. Moed, Ulrich Schmoch and 
Mike Thelwall. Springer Handbooks. Cham: Springer In-
ternational Publishing, 159–85. https://doi.org/10.1007/ 
978-3-030-02511-3_7 
Murray, Fiona. 2002. “Innovation as Co-Evolution of Sci-
entific and Technological Networks: Exploring Tissue 
Engineering.” Research Policy 31: 1389–1403. https:// 
doi.org/10.1016/S0048-7333(02)00070-7 
Mutschke, Peter and Anabel Quan-Haase. 2001. “Collabo-
ration and Cognitive Structures in Social Science Re-
search Fields. Towards Socio-Cognitive Analysis in In-
formation Systems.” Scientometrics 52: 487–502. 
Nederhof, Anton J. 2006. “Bibliometric Monitoring of Re-
search Performance in the Social Sciences and the Hu-
manities: A Review.” Scientometrics 66: 81–100. https:// 
doi.org/10.1007/s11192-006-0007-2 
Newman, M. E. 2001. “Scientific Collaboration Networks. 
I. Network Construction and Fundamental Results.” 
Physical Review E. 64: 16131. https://doi.org/10.1103/ 
PhysRevE.64.016131 
Nicolaisen, Jeppe. 2007. “Citation Analysis.” Annual Re-
view of Information Science and Technology 41: 609–41. 
https://doi.org/10.1002/aris.2007.1440410120 
Noyons, Ed C. M. and Clara Calero-Medina. 2009. “Apply-
ing Bibliometric Mapping in a High Level Science Policy 
Context: Mapping the Research Areas of Three Dutch 
Universities of Technology.” Scientometrics 79: 261–75. 
https://doi.org/10.1007/s11192-009-0417-z 
Pan, Xuelian, Erjia Yan, Ming Cui and Weina Hua. 2018. 
“Examining the Usage, Citation, and Diffusion Patterns 
of Bibliometric Mapping Software: A Comparative 
Study of Three Tools.” Journal of Informetrics 12: 481–
93. https://doi.org/10.1016/j.joi.2018.03.005 
Persson, Olle. 1994. “The Intellectual Base and Research 
Fronts of JASIS 1986–1990.” Journal of the American 
Society for Information Science 45: 31–8. 
Petrovich, Eugenio. 2018. “Accumulation of Knowledge in 
Para-Scientific Areas: The Case of Analytic Philosophy.” 
Scientometrics 116: 1123–51. https://doi.org/10.1007/ 
s11192-018-2796-5 
Petrovich, Eugenio. 2019a. “The Fabric of Knowledge. To-
wards a Documental History of Late Analytic Philoso-
phy.” Ph.D. Dissertation, Milan: University of Milan. 
https://air.unimi.it/handle/2434/613334 
Petrovich, Eugenio. 2019b. “The Structure of Scientific Dis-
ciplines. Some Notes on the Epistemology of Algorithmic 

Knowl. Org. 48(2021)No.7/8 
E. Petrovich. 2021. Science Mapping and Science Maps 
561 
Representations of Disciplines.” In STOREP 2019. Uni-
versity of Siena. http://conference.storep.org/index.php? 
conference=storep-annual-conference&schedConf=20 
19&page=paper&op=view&path%5B%5D=635 
Petrovich, Eugenio and Valerio Buonomo. 2018. “Recon-
structing Late Analytic Philosophy. A Quantitative Ap-
proach.” Philosophical Inquiries 6: 151-81. https://doi. 
org/10.4454/philinq.v6i1.184 
Petrovich, Eugenio and Emiliano Tolusso. 2019. “Exploring 
Knowledge Dynamics in the Humanities. Two Science 
Mapping Experiments.” Journal of Interdisciplinary His-
tory of Ideas 8, no. 16: 1–30. http://dx.doi.org/10.13 
135/2280-8574/4304 
Price, Derek J. de Solla. 1965. “Networks of Scientific Pa-
pers.” Science 149, no. 3683: 510–15. https://doi.org/ 
10.1126/science.149.3683.510 
Radicchi, F., S. Fortunato and A Vespignani. 2012. “Cita-
tion Networks.” In Models of Science Dynamics: Encoun-
ters between Complexity Theory and Information Sci-
ences, edited by Andrea Scharnhorst, Katy Börner and 
Peter van den Besselaar. Heidelberg; New York: Springer. 
Radicchi, F., Santo Fortunato, Benjamin Markines and 
Alessandro Vespignani. 2009. “Diffusion of Scientific 
Credits and the Ranking of Scientists.” Physical Review 
E 80, no. 5: 056103. https://doi.org/10.1103/PhysRev 
E.80.056103 
Rafols, Ismael, Alan L. Porter and Loet Leydesdorff. 2010. 
“Science Overlay Maps: A New Tool for Research Policy 
and Library Management.” Journal of the American So-
ciety for Information Science and Technology 61: 1871–
87. https://doi.org/10.1002/asi.21368 
Ranaei, Samira, Arho Suominen, Alan Porter and Tuomo 
Kässi. 2019. “Application of Text-Analytics in Quantita-
tive Study of Science and Technology.” In Springer 
Handbook of Science and Technology Indicators, edited by 
Wolfgang Glänzel, Henk F. Moed, Ulrich Schmoch and 
Mike Thelwall. Cham: Springer International Publish-
ing, 957–82. https://doi.org/10.1007/978-3-030-02511- 
3_39 
Reiss, Julian and Jan Sprenger. 2017. “Scientific Objectiv-
ity.” In The Stanford Encyclopedia of Philosophy, edited 
by Edward N. Zalta. Stanford, CA: Metaphysics Re-
search Lab, Center for the Study of Language and Infor-
mation, https://plato.stanford.edu/archives/win2017/ 
entries/scientific-objectivity/. 
Rosvall, Martin and Carl T. Bergstrom. 2010. “Mapping 
Change in Large Networks.” PLoS ONE 5, no. 1: e8694. 
https://doi.org/10.1371/journal.pone.0008694 
Salton, Gerard and Michael J. McGill. 1983. Introduction to 
Modern Information Retrieval. New York: McGraw-
Hill. 
Scharnhorst, Andrea, Katy Börner and Peter van den Bes-
selaar (Eds.). 2012. Models of Science Dynamics: Encoun-
ters between Complexity Theory and Information Sci-
ences. Heidelberg; New York: Springer. 
Skupin, André, Joseph R. Biberstine and Katy Börner. 
2013. “Visualizing the Topical Structure of the Medical 
Sciences: A Self-Organizing Map Approach.” PLoS 
ONE 8, no. 3: e58779. https://doi.org/10.1371/journal. 
pone.0058779 
Small, Henry. 1973. “Co-Citation in the Scientific Litera-
ture: A New Measure of the Relationship between Two 
Documents.” Journal of the American Society for Infor-
mation Science 24: 265–69. https://doi.org/10.1002/asi. 
4630240406 
Small, Henry. 1977. “A Co-Citation Model of a Scientific 
Specialty: A Longitudinal Study of Collagen Research.” 
Social Studies of Science 7: 139–66. https://doi.org/10. 
1177/030631277700700202 
Small, Henry. 1999. “Visualizing Science by Citation Map-
ping.” Journal of the American Society for Information 
Science 50: 799–813. https://doi.org/10.1002/(SICI) 
1097-4571(1999)50:9<799::AID-ASI9>3.0.CO;2-G 
Small, Henry and Belver C. Griffith. 1974. “The Structure 
of Scientific Literatures I: Identifying and Graphing 
Specialties.” Science Studies 4, no. 1: 17–40. https:// 
doi.org/10.1177/030631277400400102 
Sparck Jones, Karen. 1972. “A Statistical Interpretation of 
Term Specificity and its Application to Retrieval.” Jour-
nal of Documentation 28: 11–21. https://doi.org/10. 
1108/eb026526 
Strotmann, Andreas and Dangzhi Zhao. 2012. “Author 
Name Disambiguation: What Difference Does It Make 
in Author-Based Citation Analysis?” Journal of the 
American Society for Information Science and Technology 
63: 1820–33. https://doi.org/10.1002/asi.22695 
Sugimoto, Cassidy R. and Scott Weingart. 2015. “The Ka-
leidoscope of Disciplinarity.” Journal of Documentation 
71: 775–94. https://doi.org/10.1108/JD-06-2014-0082 
Swales, John M. 2004. Research Genres: Explorations and 
Applications. Cambridge, UK; New York: Cambridge 
University Press. 
Tahamtan, Iman and Lutz Bornmann. 2018. “Core Ele-
ments in the Process of Citing Publications: Conceptual 
Overview of the Literature.” Journal of Informetrics 12: 
203–16. https://doi.org/10.1016/j.joi.2018.01.002 
Tahamtan, Iman and Lutz Bornmann. 2019. “What Do Ci-
tation Counts Measure? An Updated Review of Studies 
on Citations in Scientific Documents Published be-
tween 2006 and 2018.” Scientometrics 121: 1635–84. 
https://doi.org/10.1007/s11192-019-03243-4 
Taheo, Jo. 2018. Text Mining: Concepts, Implementation, 
and Big Data Challenge (Studies in Big Data Vol. 45). 
New York, NY: Springer Science+Business Media. 
Thijs, Bart. 2019. “Science Mapping and the Identification 
of Topics: Theoretical and Methodological Considera-

Knowl. Org. 48(2021)No.7/8 
E. Petrovich. 2021. Science Mapping and Science Maps 
562 
tions.” In Springer Handbook of Science and Technology 
Indicators, edited by Wolfgang Glänzel, Henk F. Moed, 
Ulrich Schmoch and Mike Thelwall. Cham: Springer In-
ternational Publishing, 213–33. https://doi.org/10. 
1007/978-3-030-02511-3_9. 
Tijssen, R. J. W. 1993. “A Scientometric Cognitive Study of 
Neural Network Research: Expert Mental Maps versus 
Bibliometric Maps.” Scientometrics 28: 111–36. https:// 
doi.org/10.1007/BF02016288 
Townsend, Keith and John Burgess (Eds.). 2009. Method in 
the Madness? Research Stories You Won’t Find in a Text-
book. Oxford: Chandos. 
Tseng, Yuen-Hsien, Chi-Jen Lin and Yu-I Lin. 2007. “Text 
Mining Techniques for Patent Analysis.” Information 
Processing & Management 43: 1216–47. https://doi. 
org/10.1016/j.ipm.2006.11.011 
Van Raan, Anthony F. J. 1998. “In Matters of Quantitative 
Studies of Science the Fault of Theorists Is Offering Too 
Little and Asking Too Much.” Scientometrics 43: 129–
39. https://doi.org/10.1007/BF02458401 
Van Raan, Anthony F. J. 2019. “Measuring Science: Basic 
Principles and Application of Advanced Bibliometrics.” 
In Springer Handbook of Science and Technology Indica-
tors, edited by Wolfgang Glänzel, Henk F. Moed, Ulrich 
Schmoch and Mike Thelwall. Cham: Springer Interna-
tional Publishing, 237–80. https://doi.org/10.1007/ 
978-3-030-02511-3_10 
Van Raan, Anthony F. J. and R. J. W. Tijssen. 1993. “The 
Neural Net of Neural Network Research: An Exercise in 
Bibliometric Mapping.” Scientometrics 26: 169–92. 
https://doi.org/10.1007/BF02016799 
Visser, Martijn, Nees Jan van Eck and Ludo Waltman. 2020. 
“Large-Scale Comparison of Bibliographic Data Sources: 
Scopus, Web of Science, Dimensions, Crossref, and Mi-
crosoft Academic.” ArXiv:2005.10732 [Cs], May. http:// 
arxiv.org/abs/2005.10732 
Waltman, Ludo and Nees Jan van Eck. 2012. “A New Meth-
odology for Constructing a Publication-Level Classifica-
tion System of Science.” Journal of the American Society 
for Information Science and Technology 63: 2378–92. 
https://doi.org/10.1002/asi.22748 
Waltman, Ludo and Nees Jan van Eck. 2014. “Visualizing 
Bibliometric Networks.” In Measuring Scholarly Im-
pact: Methods and Practice. Springer, 285–320. 
Waltman, Ludo, Nees Jan van Eck and Ed C.M. Noyons. 
2010. “A Unified Approach to Mapping and Clustering 
of Bibliometric Networks.” Journal of Informetrics 4: 
629–35. https://doi.org/10.1016/j.joi.2010.07.002 
Wartburg, Iwan von, Thorsten Teichert and Katja Rost. 
2005. “Inventive Progress Measured by Multi-Stage Pa-
tent Citation Analysis.” Research Policy 34: 1591–607. 
https://doi.org/10.1016/j.respol.2005.08.001 
Wasserman, Stanley and Katherine Faust. 1994. Social Net-
work Analysis: Methods and Applications. Cambridge; 
New York: Cambridge University Press. 
Weingart, Scott B. 2015. “Finding the History and Philoso-
phy of Science.” Erkenntnis 80: 201–13. https://doi. 
org/10.1007/s10670-014-9621-1 
White, Howard D. and Belver C. Griffith. 1981. “Author 
Cocitation: A Literature Measure of Intellectual Struc-
ture.” Journal of the American Society for Information Sci-
ence 32: 163–71. https://doi.org/10.1002/asi.4630320302 
White, Howard D. and Katherine W. McCain. 1998. “Vis-
ualizing a Discipline: An Author Co-Citation Analysis 
of Information Science, 1972 – 1995.” Journal of the 
American Society for Information Science 49: 327-55. 
Wichmann Matthiessen, Christian, Annette Winkel 
Schwarz and Søren Find. 2002. “The Top-Level Global 
Research System, 1997-99: Centres, Networks and No-
dality. An Analysis Based on Bibliometric Indicators.” 
Urban Studies 39: 903–27. https://doi.org/10.1080/ 
00420980220128372 
Wislar, J. S., A. Flanagin, P. B. Fontanarosa and C. D. 
DeAngelis. 2011. “Honorary and Ghost Authorship in 
High Impact Biomedical Journals: A Cross Sectional 
Survey.” BMJ 343: d6128–d6128. https://doi.org/10. 
1136/bmj.d6128 
Wouters, Paul. 1999a. The Citation Culture. Unpublished 
PhD thesis. 
Wouters, Paul. 1999b. “Beyond the Holy Grail: From Cita-
tion Theory to Indicator Theories.” Scientometrics 44: 
561–80. https://doi.org/10.1007/BF02458496 
Zhao, Dangzhi. 2009. “Mapping Library and Information 
Science: Does Field Delineation Matter?” Proceedings of 
the American Society for Information Science and Tech-
nology 46: 1–11. https://doi.org/10.1002/meet.2009. 
1450460279 
Zhou, Qiuju and Loet Leydesdorff. 2016. “The Normaliza-
tion of Occurrence and Co-Occurrence Matrices in Bib-
liometrics Using Cosine Similarities and Ochiai Coeffi-
cients.” Journal of the Association for Information Science 
and Technology 67: 2805–14. https://doi.org/10.1002/ 
asi.23603 
Zitt, Michel and Elise Bassecoulard. 2006. “Delineating 
Complex Scientific Fields by an Hybrid Lexical-Citation 
Method: An Application to Nanosciences.” Information 
Processing & Management 42: 1513–31. https://doi.org/ 
10.1016/j.ipm.2006.03.016 
Zitt, Michel, Alain Lelu, Martine Cadot and Guillaume Ca-
banac. 2019. “Bibliometric Delineation of Scientific 
Fields.” In Springer Handbook of Science and Technology 
Indicators, edited by Wolfgang Glänzel, Henk F. Moed, 
Ulrich Schmoch and Mike Thelwall. Cham: Springer In-
ternational Publishing, 25–68. https://doi.org/10.1007/ 
978-3-030-02511-3_2
