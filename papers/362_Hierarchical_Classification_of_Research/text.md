Hierarchical Classification of Research Fields
in the “Web of Science” Using Deep Learning
Susie Xi Rao1,2*, Peter H. Egger1 and Ce Zhang2
1*Department of Management, Technology, and Economics, ETH
Zurich, Leonhardstrasse 21, Zurich, 8092, Zurich, Switzerland.
2Department of Computer Science, ETH Zurich,
Stampfenbachstrasse 114, Zurich, 8092, Zurich, Switzerland.
*Corresponding author(s). E-mail(s): srao@ethz.ch;
Contributing authors: pegger@ethz.ch; ce.zhang@inf.ethz.ch;
Abstract
This paper presents a hierarchical classification system that automati-
cally categorizes a scholarly publication using its abstract into a three-tier
hierarchical label set (discipline, field, subfield) in a multi-class setting.
This system enables a holistic categorization of research activities in the
mentioned hierarchy in terms of knowledge production through articles
and impact through citations, permitting those activities to fall into mul-
tiple categories. The classification system distinguishes 44 disciplines,
718 fields and 1,485 subfields among 160 million abstract snippets in
Microsoft Academic Graph (version 2018-05-17). We used batch training
in a modularized and distributed fashion to address and allow for inter-
disciplinary and interfield classifications in single-label and multi-label
settings. In total, we have conducted 3,140 experiments in all considered
models (Convolutional Neural Networks, Recurrent Neural Networks,
Transformers). The classification accuracy is >90% in 77.13% and
78.19% of the single-label and multi-label classifications, respectively. We
examine the advantages of our classification by its ability to better align
research texts and output with disciplines, to adequately classify them in
an automated way, and to capture the degree of interdisciplinarity. The
proposed system (a set of pre-trained models) can serve as a backbone
to an interactive system for indexing scientific publications in the future.
Keywords: Hierarchical text classification, neural networks,
Transformers, meta-analysis, interdisciplinarity
JEL Classification: C38
MSC Classification: 68T50
1
arXiv:2302.00390v3  [cs.DL]  25 Jul 2024

2
Hierarchical Research Fields Classification
1 Introduction
For many purposes in academic life and beyond, a hierarchical classifica-
tion (Bransford et al., 1999; Tsien, 2007) of academic output into disciplines,
fields, and subfields appears desirable, if not mandatory. Let us provide three
examples to illustrate the need.
1. A young, talented high-school graduate wanted to choose a discipline and
later a field and subfield of study, as well as the associated top institutions in
terms of faculty for their focus according to the dynamics in the (sub-)field
in terms of output and citations, in order to optimize their career prospect.
2. A scientific funding institution wanted to determine the relative degree of
interdisciplinarity in a field of study to judge applications in this regard.
3. A university-level tenure committee wanted to objectively determine the
top scholars of the same cohort in terms of their output and impact in the
same subfield as a given candidate.
Each of these interests requires a clear delineation between disciplines,
fields, and subfields across an array of academic domains of interest and, hence,
a categorization of academic work and interests in horizontal (across disci-
plines; across fields within a discipline; across subfields within a field of study)
and vertical terms (in discipline, field, and subfield of study).1 A few disci-
plines such as computer science, economics, mathematics, and physics have
established widely agreed vertical systems within their discipline. However, a
system with comparable granularity that encompasses most academic disci-
plines is missing. This void poses problems for a comparison of, for example,
the ’narrowness’ of fields in different disciplines, the degree of interdisciplinar-
ity or impact breadth of work, or the relative performance of scholars with a
similar focus of interest.
This paper contributes to the literature on meta-science – the science of
science – which roots in scientometrics, bibliometrics, and informetrics. Specif-
ically, it relates to efforts which focus on a comparison of scholars or academic
institutions in specific disciplines and fields, on the measurement and out-
puts reated to interdisciplinary endeavors, on the dissimilarity or similarity of
research bases, scholarly inputs and outputs of disciplines and fields, etc.
For the aforementioned lines of interest, we need a unified classification
system across disciplines and a large amount of data with good coverage
of disciplines. Regarding the classification system, we have taken a primar-
ily supervised machine learning (ML) approach. Regarding data, Microsoft
Academic Graph (MAG) represents a particularly useful database for these
approaches as it contains abstracts and other attributes on a large amount
1For clarification, we hereby define our terminology in describing the hierarchy of fields in
this paper. A discipline is defined as an academic discipline, known as a branch of knowledge.
Beneath which, its subfields are called fields in this paper. The subfields under a field are called
subfields here. We have a three-level hierarchy defined in our paper to describe the structure of
academic fields: discipline-field-subfield. The specification of fields helps us to specify the analysis
on different levels as we will see later. The term field is used as a general term to refer to a
discipline or a field or a subfield.

Hierarchical Research Fields Classification
3
of scientific output, and the quality of the data it covers has improved sig-
nificantly over the years (Sinha et al., 2015; Shen et al., 2018; Wang et al.,
2019).
With the supervised approach, the mappings of abstracts and keywords
from MAG to the targeted classification system are informed (i.e., the algo-
rithms are trained) by existing discipline classifications using cross-disciplinary
information such as “List of academic fields” from Wikipedia (2018b) and
discipline-specific classifications, such as JEL (American Economic Associa-
tion, 2018) in economics, ACM (Association for Computing Machinery, 2018)
in computer science and PACS (American Institute of Physics, 2018) in physics
and astronomy.
The main purpose of this paper is to deliver a system which acknowledges
the organization of academic work horizontally between disciplines and verti-
cally into discipline, field, and subfield in order to help answering questions
of the aforementioned type. As indicated above, this approach faces the fol-
lowing challenges. Specifically, we need to delineate the boundaries between
disciplines (e.g., mathematics, economics, engineering, computer science) as
well as of fields and subfields within disciplines. In this regard, we decided
to establish an ontology that has approximately even granularity across dis-
ciplines, fields, and subfields. A key goal of this “global” classification system
is to enable normalized and unnormalized impact analyses within and across
disciplines, while permitting a multi-label (interdisciplinary, interfield, inter-
subfield) classification of academic output based on abstracts and keywords.
Finally, a prerequisite for such a system is that it can be modified and extended
on the basis of new data in a timely manner, while using extremely large
amounts of data (such as abstracts and keywords).
Using data from MAG and supervised algorithms, the paper offers the fol-
lowing key contributions. First, we develop advanced tools to classify large
amounts of text data into clusters. Such an analysis is key when one wishes
to understand important features of the state or its change over time of
a field of interest here in the academic publication space. Specifically, we
permit the clusters to overlap, so that any type of output can principally
be classified as being situated strictly within or between (in multiple) dis-
ciplines, fields, and subfields. Specifically, we conduct a large number of
experiments in various state-of-the-art neural network architectures (Con-
volutional Neural Networks, Recurrent Neural Networks, Transformers) and
evaluate extensively a set of performance metrics (accuracy, precision, recall)
in 44 disciplines, 718 fields, and 1,485 subfields in both single-label and multi-
label settings to proposed the envisaged classification scheme. We make the
codebase of the classification system publicly available and accessible under
https://gitlab.ethz.ch/raox/science-clf.
The remainder of the paper is organized as follows. We introduce the
research methodologies and our goals in designing a hierarchical classification
system in Section 2. In Section 3, we first discuss the utilization of data sources

4
Hierarchical Research Fields Classification
(MAG for academic abstracts and keywords and other sources for existing dis-
cipline label systems). Section 4 describes the challenges and need to generate
high-quality training data by linking the data sources underlying our classifica-
tion system. In Section 5 we propose the design of a modularized hierarchical
classification system in both single-label and multi-label settings. We present
our experimental setups and evaluate their performance in single-label and
multi-label settings in Section 6. Finally, in Section 7, we report on interfield-
ness scores within and across all disciplines with field as the unit of analysis
as an exemplary result derived from the classification system.
2 Hierarchical Multi-Class Classification
In this paper, we present a modularized hierarchical multi-class classi-
fication system, which is capable of handling a large amount of text data
as contained in MAG (see Section 3.1) in multi-level label schemes (see
Section 3.2). In a nutshell, the proposed classification takes an abstract of a
publication as input and outputs three labels which indicate at least one disci-
pline (e.g., computer science), at least one field (e.g., information system), and
at least one subfield (e.g., database) the publication belongs to. The system is
modular, because it can cope with training and inference in a discipline-field-
subfield structure, and it can take any state-of-the-art neural architecture as
classifier.
A hierarchical classification, as opposed to a single classifier, is needed for
the following reasons. First, a single classifier for all categories at the deepest
levels could be used in conjunction with preexisting hierarchy information
for disciplines. However, on the one hand, due to class confusability (Gupta
et al., 2014; Liu et al., 2005; Rubin et al., 2012) and class imbalance (Liu
et al., 2009; Padurariu and Breaban, 2019), ML-based text classifiers usually
perform poorly and become costly to train as the number of classes increases.
This is avoided in the present context when working with disciplines, fields
within disciplines, and subfields within fields, rather than treating all subfields
horizontally and simultaneously. Moreover, even with subfields at hand, one
would not easily be able to associate those with disciplines, as many disciplines
do not have widely acknowledged hierarchical intra-disciplinary categorization
schemes. Second, for the purpose at hand, one will need to re-train the models
from time to time to keep the classifications constantly up to date, because
scholarly publications are streamed in timely, and in the future one might wish
to incorporate a “human-in-the-loop” approach. Hence, it is costly to have a
single model for all labels, which requires re-training the whole system every
time one updates the input. In contrast, having several models in a hierarchy
allows one to selectively train only those models that require an update. For
instance, this means in our case one could re-train the model for a single
discipline only with a new dump of discipline-specific publications delivered.
Now, we discuss two settings in the multi-class classification: (1) single-
label, where we assume that each piece of academic output (and abstract

Hierarchical Research Fields Classification
5
or paper) can only be assigned to one category; (2) multi-label, where we
assume binary relevance (Godbole and Sarawagi, 2004; Nam et al., 2014) of
each category and the categories are independent of each other, with each piece
of academic output being potentially assigned to multiple categories.2
The goal of the hierarchical multi-class system in the present context is two-
fold: first, to provide a system that is modularized by disciplines, fields, and
subfields, which enables efficient re-training of the models; second, to enable
the system to perform both single-label and multi-label classifications in a
multi-class setting.
3 Data Sources
The present work uses the following data sources.
3.1 MAG
The MAG database provides us with abstracts of a large number of scientific
publications (our input in Section 5.3). In this section, we discuss the merits
and disadvantages of MAG as a main data source for the present purpose.
3.1.1 Merits and Disadvantages of MAG
The systems and results we develop in this paper are based on the MAG
snapshot (2018-05-17) obtained from MAS with around 160 million scholarly
publications (i.e., excluding patent publications). The database includes all
scholarly publications with their attributes such as title, authors, affiliations,
venue, field of study (FOS), abstract, citation count, paper reference, etc. The
tables in the database are linked through paper ID, author ID, affiliation ID,
FOS ID, etc. To see the most recent MAG entity data scheme, including the
name and type of each attribute, see Services (2018). The way in which the
database was created and improved over the years and how some attributes
(such as FOS) were generated has been described in detail in Shen et al. (2018);
Sinha et al. (2015); Wang et al. (2019).
MAG offers the following merits to users.
• It provides keywords and even a loose hierarchy in the FOS scheme that are
human-curated (by the author or publisher) or machine-generated.
• It provides a set of normalized tables that can be easily joined via “Paper
ID”. Through these joins, meta-data of publications such as citations,
authors, and their affiliations, venues, etc., are accessible.
• It has been continuously updated until the end of 2021 and its successor
OpenAlex (Priem et al., 2022) has taken over most of its structure.
2In future work, we would like to extend our current multi-label classification system to alow
for a score of the discipline composition of an article. For example, one could then state that
an article 30% belongs to computer science and 70% to economics. For this, one would have to
remove the label independence assumption and construct a label powerset of the classes. In this
regard, one could make use of data-driven modularity metrics, defining the class powersets of the
labels (c.f. Szyma´nski et al. (2016)).

6
Hierarchical Research Fields Classification
A key question to ask and answer is why one would deem it insufficient to
work with the existing FOS tags available in MAG. Essentially, three reasons
come to mind, noting that MAG’s approach had not been developed with the
intent of organizing disciplines in a comparable granular structure.
First, MAG only distinguishes between 19 disciplines (top-level FOS) rather
than the 44 disciplines commonly discerned. E.g., among the many commonly
acknowledged disciplines, MAG does not consider linguistics or archaeology.
We work with 44 disciplines and design our own classification system based on
them (see Section 3.2).
Second, the MAG FOS scheme had not been established with the perspec-
tive of a hierarchical classification scheme as the one targeted here. Rather,
it is inherited from what certain academic publishers have provided, and the
latter is augmented with unsupervised machine learning (ML; c.f. “Field of
Study Entity Discovery” in Sinha et al. (2015)). As a consequence, the avail-
able FOS tags (topics) differ vastly in terms of their granularity, and they
are not systematically comparable or aligned with the classifications in disci-
plines that consider widely acknowledged hierarchical structures for themselves
such as computer science (ACM), economics (JEL), or physics and astronomy
(PACS).3
Third, FOS tags often contradict author-declared classifications in dis-
ciplines where such declaration is customary and typically published with
academic texts (e.g., in ACM, JEL, or PACS).
All of the above calls for the development of a new hierarchical system
of fine granularity, which subsequently would permit an analysis of research
input or output across comparable categories.
3.1.2 Comparison of MAG with Other Databases of
Academic Output
There are several academic databases that cover academic output across disci-
plines and could be used as the main source in our project, the most prominent
being Web of Science by Clarivate Analytics (Web of Science, 2023), Google
Scholar (Scholar, 2023), Scopus by Elsevier (Scopus, 2023), and Microsoft Aca-
demic Graph (MAG) (Sinha et al., 2015; Wang et al., 2019, 2020). Despite the
three shortcomings discussed in Section 3.1.1, we choose MAG as a data source
for two reasons: (1) it provides good coverage of scientific publications in an
3According to Sinha et al. (2015), the FOS tags were generated by seeding using existing key-
words of good quality through name matching and some heuristic rules. This does not assure an
acceptable or comparable level of granularity of FOS tags within and across disciplines. We have
evaluated the topic hierarchy in the horizontal and vertical manner. For instance, consider the
following subfields of computer science (CS) according to MAG: “Natural language processing”,
“Machine translation”, “BLEU” and “Chinese Mandarin”. These are put on the same horizon-
tal level by MAG, which apparently is deficient. Ideally, “BLEU” should be a level lower than
“Machine translation”. Moreover, it is not intuitive to put “Chinese Mandarin” as an FOS tag
of the same hierarchical level as “Machine translation”. Looking at the discipline of economics,
we observe similar problems. We also observe that the number of child levels (equivalent to fields
in disciplines) varies largely for each topic. Therefore, it is impossible to construct a global tax-
onomy based on the FOS topic hierarchy provided by MAG without making use of the external
discipline classifications.

Hierarchical Research Fields Classification
7
open-sourced data dump (see (Mart´ın-Mart´ın et al., 2021) for a small quanti-
tative analysis of the coverage in English citations),4 and (2) it is constantly
updated and has linkages of publications, authors and affiliations.
3.2 Discipline Classifications
In this subsection, we explain the need to create a hierarchical label system
by combining “List of academic fields” from Wikipedia and domain-specific
classifications such as ACM for computer science or JEL for economics.
3.2.1 Merits and Disadvantages of Existing Discipline
Classifications and Label Systems
We have evaluated existing discipline/field classifications published nationally
and internationally. They come mainly from two sources: research funding
institutions and Wikipedia.
We present here a list of classifications from various major research funding
institutions we examined in May 2018:
• German Research Foundation (Deutsche Forschungsgemeinschaft) (2018),
• Japanese Society for the Promotion of Science (2018),
• Australian Standard Research Classification (ASRC) (2018),
• Organisation for Economic Co-operation and Development (OECD) (2018),
• US National Science Foundation (NSF) (2018),
• European Economic Community (EEC) (2018).
However, not a single one of the classification schemes of the above institu-
tions provides a comprehensive global hierarchical structure as targeted here
(discipline-field-subfield), and also the information contained in the various
sources cannot be combined in a straightforward way. We therefore proceed by
defining the hierarchy starting from the level of disciplines and gradually fill
in a two-sublayer hierarchy based on within-discipline classification schemes.
“List of academic fields” from Wikipedia turns out to be the most com-
prehensive classification with good coverage of disciplines and a well-organized
hierarchy. We use the version (Wikipedia, 2018b) published in May 2018, con-
sistent with the timeframe of the MAG data dump used here. In total, the
Wikipedia scheme covers 55 disciplines in the entire hierarchy.
3.2.2 Establishing Our Three-Level Label Hierarchy
In this section, we discuss the steps to create our global classification scheme.
It is done by combining the 44 disciplines in the Wikipedia “List of academic
4In Mart´ın-Mart´ın et al. (2021), they looked at six data sources (Microsoft Academic, Dimen-
sions, the OpenCitations Index of CrossRef Open DOI-to-DOI citations (COCI), Web of Science
Core Collection (WoS), Scopus, or Google Scholar) and investigated 3,073,351 citations found
in 2,515 English-language highly cited documents published in 2006 from 252 subject categories
based on the subject fields listed in Google Classic Papers (2006) (c.f. the list here), expanding
and updating the largest previous comparative study (Birkle et al., 2020). Archived instructions
for data access to MAG can be found in https://learn.microsoft.com/en-us/academic-services/
graph/get-started-receive-data (last accessed: Nov 18, 2022). MAG is succeeded by OpenAlex.

8
Hierarchical Research Fields Classification
fields” and discipline-specific classifications such as JEL and ACM. Our three-
level hierarchy of labels is used in Section 6.1 to generate a high-quality
training set for our own classification system.
Step 1: Pruning the Wikipedia Hierarchy.
We list the discipline hierarchy of the Wikipedia taxonomy in Figure 1. Note
that we only have to classify the leaf nodes, which leaves us with 44 disciplines
(marked with (*) in Figure 1). For instance, knowing the classifications of
“Literature”, “Performing arts” and “Visual arts” gives us the whole hierarchy
of their parent discipline “The arts”, so we do not need to run a classification
for the parent discipline “The arts”.
Step 2: Merging Discipline-Specific Classifications with the Pruned
Wikipedia Hierarchy.
What we need next is a vertical (or hierarchical) classification scheme for
each of the 44 disciplines. Here, we make use of existing discipline classifica-
tions, such as the ACM classification for computer science (Association for
Computing Machinery, 2018), the JEL classification for economics (American
Economic Association, 2018), the PACS classification for physics (American
Institute of Physics, 2018), and the MSC classification for mathematics (Amer-
ican Mathematical Society (AMS) and Zentralblatt MATH, 2018).
Note that for the classification scheme of mathematics, we carefully com-
pare MSC vs. the classification of mathematics in the Wikipedia taxonomy
(where “Mathematics” →“Pure mathematics” + “Applied mathematics”).
Instead of MSC, we decided to use “Pure mathematics” and “Applied mathe-
matics” as two fields for mathematics. This is because of the overrepresentation
of mathematics if we use MSC as a discipline classification.
For those disciplines that do not have a pre-defined classification, Wikipedia
serves as the source. For instance, for the discipline “Linguistics and lan-
guages”, we resort to the corresponding linked page (Wikipedia, 2018c) in the
“List of academic fields”.
Step 3: Create a Discipline-Field-Subfield Label Structure for All
Disciplines.
It is worth noting that not every discipline classification has a three-level
structure in Wikipedia or its own classification system. We decide for each dis-
cipline to feature such a three-level structure, because it is common to have one
for the majority of disciplines (c.f. “List of academic fields” from Wikipedia
(Wikipedia, 2018b)). We take the 44 disciplines as the discipline level, the
first level tags in each discipline classification as the field level and the sec-
ond level tags in each discipline classification as the subfield level. Hence, our
classification scheme is defined as a discipline-field-subfield structure (see the
illustration of JEL classifications in Figure 2).

Hierarchical Research Fields Classification
9
ROOT
Humanities
Anthropology
Archaeology (*)
History (*)
Linguistics and languages (*)
Philosophy (*)
Religion (*)
The arts
Literature (*)
Performing arts (*)
Visual arts (*)
Social sciences
Economics (*)
Geography (*)
Interdisciplinary studies
Area studies (*)
Ethnic and cultural studies (*)
Gender and sexuality studies (*)
Organizational (*)
Political science (*)
Psychology (*)
Sociology (*)
Natural sciences
Biology (*)
Chemistry (*)
Earth sciences (*)
Physics (*)
Space sciences (*)
Formal sciences
Computer (*)
Logic (*)
Mathematics
Pure mathematics (*)
Applied mathematics (*)
Statistics
Systems science (*)
Professions and applied sciences
Agriculture (*)
Architecture and design (*)
Business (*)
Divinity (*)
Education (*)
Engineering and technology (*)
Environmental studies and forestry (*)
Family and consumer science (*)
Human physical performance and recreation (*)
Journalism, media studies and communication (*)
Law (*)
Library and museum studies (*)
Medicine (*)
Military sciences (*)
Public administration
Public policy (*)
Social work (*)
Transportation (*)
Fig. 1 Discipline hierarchy of the Wikipedia taxonomy. Note that we only have to classify
the leaf nodes, which leaves us with 44 disciplines (marked with (*)).

10
Hierarchical Research Fields Classification
4 From Abstracts and Labels to A Classification
The following subsections describe how we connect the data sources, which
include both abstracts (Section 3.1) and labels (Section 3.2), with a classifi-
cation system (Section 5.1). We started by using the existence of FOS tags to
link the labels with the abstracts, but found that only 51.3% of the abstracts
could be assigned to labels (see Section 4.1). To improve on the latter, we
experimented with supervised and unsupervised topic models (Appendix A.1),
as well as simpler supervised models such as SVM (Appendix A.2). But those
approaches did not perform well in disambiguating disciplines. Ultimately, we
created a modularized three-level hierarchical classification system (Section 5)
that supports a subsequent analysis, for which we provide an example related
to research interfieldness and interdisciplinarity (Section 7). The modular
approach enables us to break down the process into manageable parts and bet-
ter understand the connections between the data sources and the classification
system.
4.1 Linking Abstracts and Labels
To create a discipline-publication mapping, we start linking the abstracts and
labels. Here, we describe how we automatically annotate a publication with a
set of discipline-field-subfield labels.
• For the disciplines of “Computer science”, “Economics” and “Physics”,
where a discipline-specific annotation exists (ACM, JEL, and PACS, respec-
tively), we run name-matching based on the existence of FOS tags in the
levels lower than the third level (e.g., levels 4-6 for JEL and ACM). We do
this only for the subfield level.
• For the disciplines without a pre-defined taxonomy, we use the Wikipedia
taxonomy (e.g., “Linguistics and languages” in Wikipedia (2018c)) and find
the matches of the FOS tags in the text description provided by Wikipedia
(e.g., Wikipedia (2018a) for “Linguistics and languages”). Likewise, we do
this only for the subfield level.
Specifically, we first distinguish between singleton and non-singleton FOS tags.
Non-singleton FOS tags are matched based on their presence in the text
describing the subfield in the Wikipedia taxonomy (tag ⟨wikitext⟩here). For
singleton FOS tags, we match based on their appearance in topic nouns (tag
⟨TopicNouns⟩here), where the topic nouns are extracted using LDA topic
modeling (Blei et al., 2003) and setting the topic to 1 for the text in each sub-
field. If there is a match between a subfield and FOS tags in one publication,
we annotate this publication with the corresponding set of discipline-field-
subfield labels. Figure 2 shows how the matching is performed following the
JEL classification scheme in the discipline “Economics”. The matching rate,
which states how many publications could be linked to a set of discipline-field-
subfield labels, was only 51.3% (or 89,746,934 out of 174,910,379 individual
research output identifiers in MAG).

Hierarchical Research Fields Classification
11
MAG Field of study

Neoclassifical model
Trade policy
Economic integration
Database systems
International finance
...
Matching rule: whether bigram
tokens on the levels lower than
the subfield found in the paper’s
fields of study in MAG. 
Field
Field
Subfield
Discipline: Economics
MAG PaperId

1
2
3
4
5
...
MAG
PaperId
MAG Field
of study
Labels
2
Neoclassical
model
Economics-International
economics-Trade
4
Trade policy
Economics-International
economics-Trade
Discipline-publication mapping generated
Fig. 2 Discipline (JEL) publication mapping using FOS tags from MAG.
The outcome mentioned above prompts us to consider methods for assign-
ing labels to all papers that have not yet been matched. The challenges involved
in this task include (1) the need for a rapid and large-scale approach and (2) the
importance of quality, which requires a robust model with high performance.
4.2 Related Work on Abstract-to-Discipline
Classification and Baseline Models
Kowsari et al. (2017) have proposed a two-level hierarchical classification sys-
tem to classify scientific fields in a single-label setting. They have investigated
only seven disciplines (“Biochemistry”, “Civil engineering”, “Computer sci-
ence”, “Electrical engineering”, “Medical sciences”, “Mechanical engineering”,
“Psychology”) with a small web-crawled dataset (WOS-46985) as a proof of
concept. Their codebase is publicly available, but it suffers from scalability
issues in both data loading and embedding computation, and it does not
support parallel training. We adopt the same concept of hierarchical text
classification but propose a new usage of data sources (MAG, Wikipedia clas-
sification, and in-domain classifications such as ACM, JEL, and PACS), and
build a modularized pipeline scalable to the one of the largest body of academic
publications.
We have conducted the case studies illustrated in Appendix A of the
disciplines “Computer science” and “Economics” from MAG and on a bench-
marking dataset WOS-46985 published in Kowsari et al. (2017). As baseline
models, we use topic modeling and hierarchical support vector machines
(SVM). We also evaluated deep learning-based models described in Kowsari
et al. (2017). From this effort, we concluded that the deep learning-based mod-
els developed for hierarchical classification as described in the Appendix A.3
suited our purpose the best. We designed our large-scale three-level classi-
fication system, with an efficient data loader built on top of the Lightning
Memory-Mapped Database (LMDB) (Howard Chu, 2011) and the modularized
model training and inference described in Section 5.1.

12
Hierarchical Research Fields Classification
5 Our Proposed Classification System
We now present our modularized three-level hierarchical classification system
by introducing the system design – modularizable neural architecture as clas-
sifiers (Section 5.1), the single-label and multi-label settings (Section 5.2) in
the classification, and the preprocessing steps of our system input – abstracts
and labels (Section 5.3).
5.1 Three-Level Classification
We design a three-level classification system as depicted in Figure 3. The input
of the whole system is an abstract of an article in the training corpus. And the
output for each publication is a triplet of labels (discipline, field, subfield). The
system can be trained in a distributed way and has the capability to handle
large datasets thanks to the preprocessing in Section 5.3.1.
System Components.
We design the system in a modular fashion; this means that users can easily
adapt the system with newer and fancier deep learning models (e.g., Trans-
formers (Devlin et al., 2019)) and with any hierarchical taxonomy that has a
similar structure to ours. There are three components in our classification sys-
tem. The first component (L1) performs classification in disciplines, the second
component (L2) in
fields, and the third (L3) in subfields. In each compo-
nent, we have implemented four architecture choices, as discussed later in this
section, feedforward deep neural networks (DNN), recurrent neural networks
(RNN) using gated recurrent units (GRU), convolutional neural networks
(CNN), and Transformers.
The hierarchical system can help to determine the assignment of a research
abstract to disciplines, fields, and subfields. We denote p a publication, D a
discipline, Fi a field in D, Fij a subfield in Fi. We obtain the unconditional
probability P(p ∈D) from the first component of the system that classifies the
disciplines and P(p ∈Fi | p ∈D) from the second component that classifies
the fields. Similarly, one can compute the composition to a finer granularity by
getting the P(p ∈Fij | p ∈Fi, p ∈D) from the third component that classifies
the subfields.
The second component (L2) of the classification system consists of a neural
network (say DNN) trained for the domain output in the first component
(L1). The input in a neural network in the second component (e.g., DNN) is
connected to the output of the first level. For example, if the output of the first
component is labeled “Computer science” (D) then the DNN in the subsequent
component to predict fields Fi in D is trained only with all computer science
publications. Therefore, while the DNN in the first component is trained with
all publications of all disciplines, each DNN in the second component is trained
only with the publications for the specified discipline D. This applies to the
third component (L3), e.g., only the abstracts that are classified to belong to

Hierarchical Research Fields Classification
13
“Information system” (Fi) are then fed into the neural network that classifies
the subfields under “Information system” in the third component.
Modularized Neural Classifiers.
One advantage of a modularized hierarchical model is that, at a certain level,
a poorly performing model (like CNN) could be easily replaced by a stronger
model (like Transformers), without needing to change other submodels or data
input. We now list the neural classifiers implemented in our system, DNN,
RNN using GRU, CNN, and Transformers. Additional neural architectures can
be easily integrated into the modularized system.
DNNs are well suited for text classification tasks because they are capable
of learning complex non-linear relationships between input features and output
labels. The input features could be words or word embeddings, and the output
labels could be class labels, such as topic labels. DNNs can handle inputs of
variable length by using padding or truncation techniques. However, they do
not have any memory mechanism to handle sequential data, making them
unsuitable for long sequential text data.
RNNs are designed to handle (long) sequential data and can capture tempo-
ral dependencies in input data. In the context of text classification, RNNs can
take a sequence of words as input and use their memory to capture the context
and meaning of each word in the entire sequence. This makes RNNs ideal for
tasks with strong context dependency. RNNs can be trained using backprop-
agation through time, which updates the weights of the network based on the
error at each time step. We use GRUs (instead of LSTMs) for computational
efficiency or simplicity in our design.
CNNs are primarily designed for image classification, but have also become
widely used for text classification. With the latter, CNNs can be used to extract
local features from text data by treating them as two-dimensional signals.
This is achieved by using two-dimensional convolutions over the sequence of
words, which allow the network to capture patterns and relationships between
adjacent words in the input. This makes CNNs ideal for tasks such as text
categorization, topic classification, and sentiment analysis. In addition, CNNs
are computationally efficient and can be trained on large datasets.
Transformers use self-attention mechanisms to model contextualized rela-
tionships between words, build a stack of encoders (“transformer blocks”),
and learn the word representations in “weights”. These weights then deter-
mine the importance of words/sentences for further processing. Bidirectional
Encoder Representations from Transformers (BERT) are pre-trained5 Trans-
former models on tasks like the masked-sentence task and next-sentence
prediction. BERT outperforms baselines on many other tasks such as Q&A
(Devlin et al., 2019). It is “bi-directional” in the sense that words before and
after the target word-to-predict are considered. For transfer learning where the
5BERT has been trained with English Wikipedia of approximately 2.5 billion words and
BooksCorpus of approximately 800 million words (Zhu et al., 2015).

14
Hierarchical Research Fields Classification
Input Layer
Hidden Layer
Output
Discipline
x0
x1
xf
y0
y1
ym
Economics
Computer science
Mathematics
Trade
Finance
Information
System
Math of
Computing
...
...
...
...
...
...
...
...
...
...
...
...
...
...
...
...
...
...
...
...
...
...
...
...
...
...
...
...
...
...
...
...
...
...
...
...
...
...
...
...
...
...
Combinatorics
Number
Theory
...
...
...
...
...
...
...
...
...
...
...
...
...
...
...
...
...
...
Input
Layer
Hidden
Layer
Output
Field
Trade Policy
Trade and Labor Market
Interactions
...
...
...
...
...
...
...
...
...
...
...
...
...
Input
Layer
Hidden
Layer
Output
Subfield
Foreign Aid 
Foreign Policy
...
...
...
...
...
...
...
...
...
...
...
...
...
Database
Info Storage and Retrieval
...
...
...
...
...
...
...
...
...
...
...
...
Numerical Analysis
Discrete Math
...
...
...
...
...
...
...
...
...
...
...
...
...
...
...
...
...
...
...
...
Graph Theory
Algebraic Combinatorics
...
...
...
...
...
...
...
...
...
...
...
...
Sequences and Sets
Polynomials and Matrices
...
...
...
...
...
...
...
...
...
...
...
...
...
...
...
...
...
...
...
Fig. 3 Three-level hierarchical classification system.

Hierarchical Research Fields Classification
15
embedding representations could be obtained from pre-trained BERT mod-
els, one does not need to retrain the in-domain models from scratch but only
need to freeze most of the layers and fine-tune the few last layers. In fine-
tuning, we jointly train them with newly added layers, such as dense layers,
for downstream specific classification.
BERT models are composed of two parts, the pre-processing and the
encoder fine-tuning parts. The pre-processing encoder generates three repre-
sentative embeddings given an input text into: (1) “token” embeddings based
on the present tokens, (2) “segment” embeddings based on the sentence or
phrase a particular token belongs to, and (3) “positional” embeddings based
on the token position. Similar to the maximum sequence length imposed on
the tokenization for DNN/CNN/RNN, BERT has the limit of 512 tokens of
each input text. The encoder part uses the BERT pre-trained model, trans-
forms an input text into embeddings via the pre-processing steps we discussed
above, then passes the embeddings to the transformer blocks, and finally puts
a dense layer as we discussed in the fine-tuning procedure.
5.2 Single-Label and Multi-Label Settings
In single-label settings, each piece of academic output is assigned to only one
category, while in multi-label settings, each output can be assigned to multiple
categories, with binary relevance and independent categories. These concepts
have been discussed in related work such as Godbole and Sarawagi (2004);
Nam et al. (2014).
Necessity of Multi-Label Classification and Its Assumptions.
In the context of interdisciplinarity (Section 7), if we only look at the single-
label setting in a multi-class classification, where a single input is associated
with exactly one of the many potential classes, it is a strong restriction. When
we consider the multi-label setting, where a single input is allowed to be asso-
ciated with one or more classes. This way, cross-disciplinary inputs such as
“Biochemistry” – which combines “Biology” and “Chemistry” – are considered
to have two labels.
As the simplest approach to start with, multi-label classification can be
viewed as multiple binary classification problems under the assumption of label
independence. That is, given one input, the relevance of one label does not
depend on the relevance of other labels. Another assumption to make for multi-
label classification is the train-/test-split. In the single-label setting, the split
can be done by stratified sampling the label using its original distribution,
since each input belongs to precisely one label. In the multi-label setting,
however, since each input can belong to more than one label, simply performing
“stratified” sampling is no longer trivial. Moreover, using the label powersets
to perform stratified sampling is highly impractical: there are many possible
combinations of labels up to 2n for n classes, so we might end up having very
few samples belonging to some label set, which renders stratified sampling

16
Hierarchical Research Fields Classification
useless. The current implementation uses the same train-/test-split as in the
single-label setting.6
Specifications of Multi-Label Settings.
We conduct the experiments under the binary relevance (BR) assumption
because of its scalability. Also, the hierarchical arrangement of the labels to
some extent incorporates the label independence assumption. BR requires a
minimal change to our technical setup as opposed to the single-label setup.
• The input format does not need to change since the labels are already
inputted as multi-hot encoding.
• The loss function must change from categorical cross entropy to binary cross
entropy7 following the BR approach, which is also found to be an effective
loss function (Nam et al., 2014).
• The activation function of the final dense layer becomes sigmoid instead of
softmax, following the loss of binary cross-entropy.
After changing to sigmoid activation, the output array is thus no longer
a probability array (i.e., its entries do not sum up to one). Each entry, which
corresponds to the relevance of each label, remains between 0 and 1 (inclusive),
which corresponds to the “relevance” of the input given one label. With this
output format, it is also useful to set a threshold to treat the label as relevant:
instead of cutting off at 0.5 as in normal sigmoid, we might lower the cut-off
threshold, since the use case of the system is to explore the class membership.
As discussed above, we decide to perform stratified sampling on the label
sets. This does not require any change to our codebase of the single-label
setting.
Another choice we need to make is the performance metric, which we have
used, namely categorical accuracy, in the single-label experiments. The main
difference between categorical accuracy and binary accuracy in a multi-label
setting is that the latter exaggerates the performance when the ground-truth
multi-hot label is sparse.8 Therefore, we maintain the very conservative metric,
categorical accuracy, along with precision and recall. Lowering the accuracy
threshold from 0.5 to 0.3 may improve the performance; we will consider more
sophisticated and customized metrics in future work.
6We are aware of that this setting can lead to the same sample might be assigned to both the
train and the test sets from different labels it is associated with. One remedy for this problem is to
use iterative stratification, which allows setting up a k-fold cross-validation such that the distribu-
tion of relevant and irrelevant samples of each label is normalized (Sechidis et al., 2011; Szyma´nski
and Kajdanowicz, 2017). Iterative stratification is implemented in the scikit-multilearn library
for Python (Szyma´nski et al., 2014). However, due to the lack of maintenance and documenta-
tion, we do not use this library at this stage and simply adopt stratified sampling as we do in the
single-label setting.
7Each pair of classes gets compared and their binary cross-entropy loss computed; the sum of
losses for all the pairs is optimized.
8For example, consider the case where a classifier always predicts nothing, i.e., the predicted
label is a zero array. When the ground truth label is sparse, for example, having only 2 out of 8
classes relevant, the binary accuracy would be 6/8 = 75%, although this classifier is completely
uninformative. See TensorFlow (2022a) on binary accuracy and TensorFlow (2022b) on categorical
accuracy for more details.

Hierarchical Research Fields Classification
17
5.3 Preprocessing of Input to Our Classification System
Here we present the necessary preprocessing steps for the input (abstracts and
label sets, see Section 3) to our classification system. It should be noted that
the same steps are used in both single-label and multi-label settings.
5.3.1 Abstracts
We are in need of an efficient preprocessing pipeline for a system with a large
number of training instances (984,722,678 abstracts in a multi-label setting).
Each abstract is a text snippet of around 200 words, with variation across
fields.
From Raw Text to LMDB.
Our model inputs – the abstracts of the papers – are provided in
PaperAbstractsInvertedIndex.txt in the inverted index format in the MAG
dataset. A dummy dataset is provided in Table 1 for illustration purposes. We
first decode all inverted abstracts in abstracts of normal reading order (the
column “Original abstract”). We then tokenize each abstract into a sequence
of its token IDs. We use tensorflow.keras.layers.TextVectorization for
this.
We then store text vectors after tokenization in an LMDB instance per
discipline, where batch generator IDs are keys, and the token sequences of their
abstracts are values. This is to facilitate batch processing during training.9
Table 1 Dummy sample of paper abstract inverted index from MAG.
Paper ID
IndexLength
InvertedIndex
Original abstract
12
5
{“I”: [0, 3],
“am”: [1, 4],
“who”: [2]}
I am who I am
1
3
{“All”: [0, 2],
“in”: [1]}
All in all
6
...
...
...
Efficient Data Loader with LMDB.
We first select the top-k frequent words from the “bag of words” in the training
set (say k = 3000) and pre-compute the representations with GloVe (Pen-
nington et al., 2014) or BERT that are static over all the models but fetched
9To ensure that the size of the training corpus does not become the bottleneck of training,
because the existing preprocessing wrappers in e.g.,tensorflow and keras break down when com-
puting the word index of the training corpus and then one hot encoding for each text snippet
for a large training corpus. In our case studies discussed in Appendix A, more than 2 mil-
lion training instances have already crashed the fit on texts(texts) method; see this post under
http://faroit.com/keras-docs/1.2.2/preprocessing/text/ (last accessed: Feb 29, 2020).

18
Hierarchical Research Fields Classification
constantly in a key-value database (DB) that supports multithreading reads.
After benchmarking many existing DB solutions (c.f. Piriyatamwong (2022)),
we select Lightning Memory-Mapped Database (LMDB) (LMDB, 2022) as our
key-value store.
Making use of the word representations, we also pre-compute the repre-
sentation for each abstract and store it in an LMDB instance. Each discipline
of the 44 chosen has its own LMDB instance. This choice is a trade-off of
data loading for different levels of models: typically, in the three-tier labels
(discipline-field-subfield), we most likely will update field-specific models or
subfield specific models. The top level (aka a model to classify all 44 disciplines)
will only be updated in case of a large update of the publication database.
Making data loading more efficient for all models gives our classification
system a computational speedup and a capacity to handle an arbitrarily large
number of training instances, which is expected as the scholarly publication
space is growing rapidly.
5.3.2 Labels
Categorical labels are already provided after the discipline-publication map-
ping described in Section 4, so preprocessing involves only one step: To encode
categorical labels into category IDs readable by the classifiers. To incorporate
the extension to both single-label and multi-label classifiers, we use multi-
hot encoding using sklearn.preprocessing.MultiLabelBinarizer for label
encoding.
6 Experiments and Evaluation
We perform experiments using the four neural network architectures (DNN,
CNN, RNN, Transformer) described in Section 5.1. Note that due to the com-
putational costs of Transformers, we only use them to improve the models that
perform poorly with the basic neural architectures (DNN, CNN, RNN). We
share the results of single-label and multi-label settings.
The models are implemented in Python using the Keras library and are
automatically tracked by the MLFlow library10 We use Keras Functional API,
which builds a directed acyclic graph (DAG) of layers to allow non-linear
topology, such as shared layers and multiple inputs and outputs. We utilize
the Distributed Learning module from the Tensorflow Distributed Learning
API called MirroredStrategy, which supports synchronous training across
multiple GPU workers,11 for fast training.
10MLFlow is an open-source platform for managing the end-to-end machine learning lifecycle
(Chen et al., 2020; Zaharia et al., 2018). Its main functionality is the automatic tracking of dif-
ferent machine learning experiments and runs. In particular, it automatically records the training
parameters and results as well as the trained models.
11One replica is created per GPU device, and each model variable is mirrored across all replicas
and is kept in sync by applying identical updates. All-reduce algorithms are used to communicate
variable updates, in particular to aggregate gradients produced by different workers that work
in different slices of input data in sync, using the NVIDIA Collective Communication Library
(NCCL).

Hierarchical Research Fields Classification
19
Categorical accuracy, precision, and recall are tracked. Other model
settings can be found in the Appendix B.
6.1 Training and Testing Sets
The ultimate goal we want to achieve by linking the MAG abstracts and the
discipline hierarchy (Section 4) is to create high-quality training data for our
classification system. If there are matches between a publication abstract and
a set of discipline-field-subfield labels, we use this match in the training set;
otherwise, a publication is put in the test set. Despite the abstract-label linkage
only covering 51.3% of all the papers in MAG, this approach is effective in
automatically generating high-quality training instances for our classification
system. The 40% of the training set is used as the validation set and all the
results we report below are on the validation set. The results are calculated
using a generic list of the top vocabulary k in the training corpus (k = 3000).12
6.2 Single-Label Experiments
CNN and RNN Results.
In our small-scale ablation study described in Piriyatamwong (2022) using the
dataset described in Appendix A, RNN and CNN significantly outperformed
DNN. Therefore, we evaluate only the RNN and CNN models on the 44-
discipline dataset. We performed in total 1,526 experiments: 2 architectures ×
763 models (1 model for Level 0, 44 models for Level 1, 718 models for Level
2). Due to the sheer number of experiments, the full result table is available in
our code repository.13 Here, we provide an executive summary of the results.
• For most models, all architectures achieve good performance in all perfor-
mance metrics. Specifically, in 77.13%, 81.26%, and 76.02% of the models,
their accuracy, precision, and recall reach 90% or more regardless of the
architecture, respectively.
• In terms of precision, CNN seems to perform best for most models, followed
by RNN. Specifically, 54.95% models get the best precision from CNN, and
45.05% models from RNN. The mean precision scores for CNN and RNN in
all models are 95.96% and 93.70%, respectively. The same conclusions can
be drawn if we use accuracy and recall as performance metrics.
• In the 165 models where the best accuracy of all architectures is less than
90%, CNN also performs significantly better than RNN in all except 19
12We have experimented in Piriyatamwong (2022) that the use of technical jargon from the
abstracts can slightly improve the classification performance. However, it is not feasible to use
technical jargon for all disciplines for the following reasons: (1) Not all papers have good FOS
tags, as we see in the matching process in Section 6.1. (2) It requires an additional step to extract
quality words as discussed in Rao et al. (2022). After careful evaluations of the existing methods
of keyphrase extraction, we are currently using KeyBERT (Grootendorst, 2020) to extract missing
keyphrases for the MAG or OpenAlex data dump, which once completed can serve as the backbone
of an upgraded version of the classification system.
13The results of single-label experiments are accessible under https://gitlab.ethz.ch/raox/
science-clf/-/blob/main/result tables/single label clean modelnotempty export v2 fixed.csv.

20
Hierarchical Research Fields Classification
models. Looking at the best precision scores of all architectures, which are
< 90%, we have 35 RNN models and 70 CNN models.
• For 4.7% of all CNN/RNN models, their precision is extremely poor (less
than 70%) in any architecture. In these models, the mean accuracy is 50.87%,
and the mean recall is also poor with only 30.85%. On average, there are
5.97 classes to predict in these models, with 1.35 million training instances
on average.14 Hence, we need to and should be able to further improve the
performance of these models.
It is clearly beneficial to use CNN as the base model for single-label clas-
sifications. In terms of training time per epoch, we report the average time at
each level of the models. The numbers we report here are computed on a single
unit of GPU (NVIDIA GeForce RTX 3090, 24GB memory), on a machine with
64 units of AMD EPYC 7313 16-core Processor and 504 GB memory. We have
run all the experiments on two such machines, one with 8 units of NVIDIA
GeForce RTX 3090 and the other with 4 units. For the top level, CNN takes
about 6 hours, while RNN takes about 9 hours. For the second level, CNN
takes 1 hour 20 minutes on average, while RNN takes 3 hour 47 minutes. For
the third level, CNN and RNN take 12 and 22 minutes on average, respectively.
The performance report suggests that CNN and RNN perform well in most
cases. Taking into account the efficiency of training, CNN seems to be a clear
winner to serve as a suitable “default” model for the entire hierarchy. For those
models that have extremely poor accuracy, which we pay attention to in our
improved approaches using keywords as a vocabulary list (c.f. Piriyatamwong
(2022)) or Transformers we evaluate in the subsequent section.
Transformers Results.
In the above reported results using CNN/RNN, we have 49 remaining poorly
performing models that have a precision of less than 70% even in the best
performing architectures among CNN and RNN. As in previous sections, we
provide a result summary here and refer readers to the full result table in our
code repository. 15
• Transformers seem to improve performance in terms of precision (26 out of
49), accuracy (30 out of 49), and recall (30 out of 49). Improvement varies
from as little as 0.08% to as much as 33.27% (from 25.19% to 58.46%).
• Due to training efficiency, we use only the batch size of 16 and run for one
epoch.
• The average time per epoch is shorter than with RNN (sometimes only
half), despite the large difference in batch size (RNN: 512 or 1,024
vs. Transformers: 16).
14Other statistics on the number of training instances are minimum 869, median 51,223,
maximum 19,613,670.
15The
results
of
single-label
experiments
using
Transformers
are
accessbile
under
https://gitlab.ethz.ch/raox/science-clf/-/blob/main/result tables/transformer single label
clean modelnotempty export v2.csv.

Hierarchical Research Fields Classification
21
Summary of Single-Label Classifications.
Although CNN/RNN models have achieved good performance, they suffer from
either computational efficiency or performance, such as sequential processing
in RNN. It is suggested that we can use CNN as the base model of the system,
but we are in need of a superior classifier for models that are still performing
poorly. Transformer models are proposed to solve the inefficiency in sequential
processing, by processing the text as a whole rather than word by word sequen-
tially. This allows for parallelization and makes processing computationally
more efficient without sequential processing (Vaswani et al., 2017).
6.3 Multi-Label Experiments
After removing single-label models, we have 1,474 models to train using each
of the CNN and RNN neural network architectures.
CNN and RNN Results.
As in previous sections, we provide a summary of the results here and refer the
reader to the complete result table in the full result table in our code base.16
The result summary is as follows:
• Despite the conservative accuracy determination choice, the models perform
acceptably: 1,123 out of 1,474 models achieve an accuracy of at least 90%
on their best models. In these models, precision and recall are equally good:
1,208 and 1,131 of 1,474 models have achieved > 90%, respectively.
• CNN continues to lead in performance in all performance metrics: It per-
forms best in 56.7% of the models, followed by RNN in 43.3% of the models
according to the precision score.
• The average precision scores for CNN and RNN are 95.69% and 93.18%,
respectively. This shows a small degradation from the single-label case, as
expected.
The computational time for the top level is 105 hours for CNN and 1,688 hours
for RNN, with a batch size of 64 due to RAM constraints. On the second level,
CNN per epoch on average takes 1 hour, while RNN requires 3 hours and
14 minutes. On the third level, CNN and RNN take on average 48 minutes
and 1 hour 20 minutes, respectively. Therefore, we draw conclusions similar to
those of Section 3.2: CNN is a good choice of default model in our hierarchical
classification system on all levels, be it single-label or multi-label.
6.3.1 Transformers for Multi-Label Classification
Similar to the setting described in Section 6.2, we also perform experiments
in the Transformers on multi-label classification, whose precision is less than
16The results of multi-label experiments are accessible under https://gitlab.ethz.ch/raox/
science-clf/-/blob/main/result tables/multi label clean modelnotempty export v2 fixed.csv.

22
Hierarchical Research Fields Classification
70%. There are 51 such models to train.17 Here are the observations that we
make. Transformers seem to improve performance in terms of precision (41
out of 51), accuracy (39 out of 51), and recall (21 out of 51); the improvement
varies from as little as 0.05% to as much as 51.9% (from 21.01% to 72.91%).
The training setup is identical to that in Section 6.2 and the training time per
epoch on average also follows the pattern found in the single-label setting.
7 Interfield Citation Scores Within and Across
Disciplines
Interdisciplinarity is in the limelight of research funding bodies and is believed
to be the key to breakthrough innovations in many fields of academic inter-
est (see Ioannidis (2005); Leydesdorff and Rafols (2009); Van Noorden et al.
(2015)). Measuring it requires a clear delineation of the boundaries of disci-
plines as well as of intra-disciplinary fields on the one hand and metrics that
indicate intra- versus inter-disciplinary activity. Since disciplinary boundaries
are easier to determine than those across fields within disciplines, earlier work
has mainly focused on interdisciplinary rather than interfield interdependence
of research. The usual interdependence metrics are citation input (demand)
and output (supply) between disciplines (see Ioannidis (2005); Leydesdorff and
Rafols (2009); Van Noorden et al. (2015)).
The framework proposed in this paper can help inform and add to this
debate in the following way. First, it can identify the fields within disciplines
that are particularly responsible for the absorption as well as the supply
of ideas among field-to-field cells. To the extent that two fields in a pair
belong to two different disciplines, this allows identification of interdisciplinary
citation input and output scores. Second, the established taxonomy in this
paper can determine to what extent such interdisciplinarity scores are con-
centrated versus dispersed between the supplying (outputting) and receiving
(inputting) disciplines. Third, the same taxonomy can even help, by anchoring
the authors of academic output in (potentially multiple) disciplines and fields,
understanding to which extent such flows of ideas happen and interdepen-
dence is created by and from authors with a cross-disciplinary footing in their
own academic work (within-author interdisciplinarity) or not (between-author
interdisciplinarity). Fourth, by assigning researchers to disciplines and fields,
the approach can help identify to what extent interdisciplinary impact is more
or less likely in the case of interdisciplinary collaborations in academic work or
not. The latter two aspects might be important for the selection of instruments
geared toward promoting interdisciplinary research and its impact.
In this section, we will focus on citation inputs and outputs as metrics of
influence within and across fields, as well as within and across disciplines. We
will do so from a macro-perspective of disciplines (Section 7.2), subsequently
17The
results
of
multi-label
experiments
using
Transformers
are
accessible
under
https://gitlab.ethz.ch/raox/science-clf/-/blob/main/result tables/transformer multi label clean
modelnotempty export v2.csv.

Hierarchical Research Fields Classification
23
0 1 2 3 4 5 6 7 8 9 10111213141516171819202122232425262728293031323334353637383940414243
Discipline
0.0
0.5
1.0
1.5
2.0
2.5
3.0
Number Field
1e7
agri
phil
edu
anthro
jour
(a) Number of total papers.
0 1 2 3 4 5 6 7 8 9 10111213141516171819202122232425262728293031323334353637383940414243
Discipline
0
10
20
30
40
50
60
Number Field
agri
phil
edu
anthro
jour
(b) Number of fields.
0 1 2 3 4 5 6 7 8 9 10111213141516171819202122232425262728293031323334353637383940414243
Discipline
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
4.0
Ratio (Total Papers / Number Field)
1e6
cs
purem
agri
geo
perf
phil
space
sys
logic
edu
jour
anthro
appliedm
(c) Ratio of total papers to number of fields.
Fig. 4 Distributions of total papers, number of fields and their ratio in 44 disciplines.

24
Hierarchical Research Fields Classification
Demand 
 (Range: 0-2e8)
Supply 
 (Range: 0-2e8)
cs
(0)
econ
(1)
purem
(2)
phys
(3)
agri
(4)
anthro
(5)
arch
(6)
area
(7)
div
(8)
earth
(9)
env
(10)
ethnic
(11)
fam
(12)
gender
(13)
geo
(14)
human
(15)
law
(16)
lib
(17)
ling
(18)
lit
(19)
org
(20)
perf
(21)
phil
(22)
pol
(23)
pub
(24)
rel
(25)
socw
(26)
space
(27)
sys
(28)
trans
(29)
vis
(30)
logic
(31)
edu
(32)
bus
(33)
chem
(34)
eng
(35)
hist
(36)
med
(37)
mil
(38)
psy
(39)
soc
(40)
jour
(41)
appliedm
(42)
bio
(43)
Disciplines
Fig. 5 Box plots for demand and supply of 44 disciplines.
consider fields within disciplines (Section 7.3), and finally we will offer a dis-
cussion of the latter two subsections in light of score measurement in Section
7.4.
7.1 General Approach
At the macro level, we will consider interdisciplinary citation matrices across
all 44 considered disciplines on the one hand and all 718 fields in the disciplines
on the other hand. The underlying citation linkages for each pair of outputs
are provided in MAG.
Each research output (e.g., article) in MAG is classified to belong to at
least one discipline of academic work and at least one field (the highest hier-
archical level below the one of disciplines). Altogether, we distinguish between
44 disciplines which cover 718 fields of academic research. Hence, the average
discipline covers 16 fields. Figure 4 shows the distributions of the total aca-
demic articles (a), field numbers (b), and their ratio (c) in all 44 disciplines in
our multi-label training set, which dates from 1800 to 2018.
The ratio represents the average number of articles per field within dis-
ciplines. We see that the distributions of various attributes differ largely
from each other and result in the highest average numbers of articles per
field (c) being “Computer science”, “Pure mathematics”, “Agriculture”,
“Anthropology”, “Philosophy”, “System science”, “Logic”, “Education”, and
“Journalism”. This is due to the fact that a discipline generates many pub-
lications such as “Computer science” or “Agriculture”, and/or it has a small
number of fields such as “Anthropology” or “Journalism”.

Hierarchical Research Fields Classification
25
Figure 5 provides the whisker plots of the distribution of citations outward
(supplied; output) and inward (demanded; input) in the fields for each disci-
pline. We observe that in most of the discplines the citation supply and demand
are almost equal, but their range varies largely across different disciplines.
There are certain disciplines such as “Computer science”, “Earth science”,
“Gender study”, “Public policy”, “Space science”, “Education”, “Business”,
“Chemistry”, “Engineering”, “Medicine”, “Psychology” and “Biology” that
have large outliers in either citation demand or supply.18
Let us organize the data in matrix form, so that rows are sorted first
by discipline and subsequently by field within a discipline (here, we use the
arbitrary numeric encodings for sorting that are fixed in the training stage,
see Appendix C). This matrix is composed of 44 discipline-to-discipline blocks,
where each block consists of the number of fields in the citing discipline in
rows and the number of fields in the cited discipline in columns. Hence, along
the diagonal, we find square blocks of intra-disciplinary citations across fields
within a discipline, and off the diagonal blocks there are inter-disciplinary
citations across fields between disciplines.
Let us denote the just-mentioned 718 × 718 matrix with citation counts
by I = Idf,d′f ′, where {d, d′} is a pair of disciplines, and {f, f ′} are a pair of
fields. In the latter statements, d and d′ might be identical in general, and f
and f ′ might be identical only if d = d′. The matrix I can be though of as to
be made up of discipline-to-discipline blocks that are themselves made up of
field-to-field cells.
Let us use I0 to denote the raw matrix of citation count inputs, demand by
fields in rows, and supply from fields in columns, and let O0 = I′
0 denote its
transpose, the citation count output matrix. It is customary to row normalize
these matrices to focus on the distribution of counts within a row (this is
also called normalization by degree). Let us denote these normalized matrix
counterparts by I and O and note that for each of them, all cell entries are
nonnegative and sum up to unity in a row. Hence, the cells indicate the share of
one input field (absorbing) in the output field’s overall citations and the share
of one output field (supplying) in the input field’s overall citations, respectively.
A matrix of further interest is the net output matrix D0 = O0 −I0 and
its row-normalized counterpart D, where we can use the absolute row sum
normalization for the latter.
With this approach, we can consider the share of within-field citation scores
(which is by definition an intra-disciplinary concept), the share of inter-field
citation weights within a discipline, and the share of inter-field citation weights
across disciplines. The latter is by definition an interdisciplinarity score, which
can be further decomposed into specific components that accrue to individual
fields. Overall, these scores provide a field-anchored description of citation
gross inputs and outputs as well as net outputs.
18For the comparison between citation demand and supply of each discipline, we refer readers to
the box plots in online Appendix via https://gitlab.ethz.ch/raox/science-clf/-/blob/main/result
tables/online appendix.pdf.

26
Hierarchical Research Fields Classification
Table 2 Multi-labeled papers with field assignments (2786288045 cites 2101095530).
Paper ID
Paper title
Field labels
Field
2786288045
Chapter 1 – Definition of Gastroesophageal Reflux
Disease: Past, Present, and Future
43-30
Bio-Pathology
2101095530
Esophageal Adenocarcinoma Incidence:
Are We Reaching the Peak?
3-18
PACS-Biological and medical physics
43-30
Bio-Pathology
43-2
Bio-Endocrinology
7.2 Interfield Citations Between 44 Disciplines
First, we create a dataframe where each row is a tuple of (Paper1, Paper2,
Disc1, Disc2), where Paper1 and Paper2 are the Paper IDs in MAG; Disc1
and Disc2 are the discipline labels of Paper1 and Paper2 in the multi-label
setting. The edge value between these two paper nodes is binary, indicating
a citation relationship. For instance, a tuple (2786288045, 2101095530, 43, 3)
means Paper1 in “Biology” (43) with the Paper ID of 2786288045 cites Paper2
in “Physics” (3) with the Paper ID of 2101095530. We provide an extensive
example in Table 2 on the field level, where we have Paper1 2786288045 citing
Paper2 2101095530. Note that here we provide field labels, with which we gen-
erate discipline labels. In this case, we have discipline-to-discipline mappings
of (43, 3) and (43, 43), as well as field-to-field mappings (43-30, 3-18), (43-30,
43-30), and (43-30, 43-2). Each pair is an element of the Cartesian product of
the label sets of Paper1 and of Paper2.
In total, there are 43,718,407,275 tuples in the training set of our multi-
label settings across 44 disciplines. Then, we aggregate the tuples up into a
discipline-by-discipline matrix. The discipline-to-coding mapping is listed in
Appendix C.
Normalization by row sum of matrix I0 describes the ratio of all disciplines
in terms of demand from a specific discipline d, while normalization by row
sum of matrix O0 (which corresponds to column normalization of I0) describes
the ratio of supply from all disciplines to a specific discipline d′.
Based on the normalized matrices I and O, we generate heatmaps in pan-
els (a) for the input matrix I and (b) the output matrix O in Figure 6. The
heatmaps permit identifying disciplines that face a high relative interdisci-
plinary demand from one discipline (in a row across columns of I) and ones
that generate a high relative output across disciplines from a given discipline
(in a row across columns of O). Interestingly, the right-stochastic matrices
I and O do not show dominating diagonal elements (dominance of intra-
disciplinary impact) throughout the disciplines, but some disciplines are more
strongly represented in interdisciplinary input dependence and output impact
than others.
Disciplines that have a particularly high interdisciplinary demand (red cells
in rows in Figure 6 (a)) are the following:
• “Computer science” (0) highly demands (cites heavily) from “Chemistry”
(34) and “Biology” (43).

Hierarchical Research Fields Classification
27
(a) Input matrix I.
0
1
2
3
4
5
6
7
8
9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43
Out Citations of d′ Fields  (Supply/Output) 
 d′ is cited by d
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
Row Normalized 
 In Citations of d Fields (Demand/Input) 
 d cites d′ 
0.02
0.04
0.06
0.08
0.10
(b) Output matrix O.
0
1
2
3
4
5
6
7
8
9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43
In Citations of d Fields (Demand/Input) 
 d cites d′ 
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
Row Normalized 
 Out Citations of d′ Fields  (Supply/Output) 
 d′ is cited by d
0.02
0.04
0.06
0.08
0.10
Fig. 6 Across-discipline interdisciplinary scores of all 44 disciplines.

28
Hierarchical Research Fields Classification
• “Physics” (3) has a high demand from “Computer sciences” (0), “Earth
sciences” (9), “Chemistry” (34) and “Engineering and technology” (35).
• “Earth sciences” (9) have high demands from “Chemistry” (34).
• “Space sciences” (27) highly demands from “Computer science” (0), “Earth
sciences” (9), “Chemistry” (34), “Engineering and technology” (35) and
“Biology” (43).
• “Chemistry” (34) demands highly from “Engineering and technology” (35)
and “Biology” (43).
• “Engineering and technology” (35) demands highly from “Chemistry” (34)
and “Biology” (43).
Disciplines that have a high interdisciplinary supply (red cells in rows of
Figure 6 (b)) are the following:
• “Computer science” (0) is highly cited by “Chemistry” (34) and “Biology”
(43).
• “Physics” (3) is highly cited by “Computer sciences” (0), “Earth science”
(9), “Chemistry” (34), “Engineering and technology” (35), and “Biology”
(43).
• “Earth sciences” (9) is highly cited by “Computer science” (0) and “Chem-
istry” (34).
• “Gender studies” (13) are highly cited by “Education” (32), “Psychology”
(39) and “Biology” (43).
• “Space sciences” (27) is highly cited by “Computer science” (0), “Chem-
istry” (34), “Engineering and technology” (35) and “Biology” (43).
• “Chemistry” (34) is highly cited by “Computer science” (0), “Earth science”
(9), “Engineering and technology” (35) and “Biology” (43).
• “Engineering and technology” (35) is highly cited by “Computer science”
(0), “Earth sciences” (9), “Chemistry” (34), and “Biology” (43).
• “Medicine” (37) is highly cited by “Education” (32), “Chemistry” (34) and
“Biology” (43).
• “Psychology” (39) is highly cited by “Education” (32) and “Biology” (43).
• “Biology” (43) is highly cited by “Computer science” (0), “Education” (32),
“Chemistry” (34), and “Psychology” (39).
• “Computer science” (0), “Education” (32), “History” (36), “Psychology”
(39), “Sociology” (40), and “Biology” (43) are disciplines that are cited by
almost all disciplines.
In general, the above analysis suggests two interesting findings. First, in
many disciplines, contributions from other disciplines outweigh those within
the discipline. Second, often the relative importance of “foreign” disciplines in
terms of demand and supply of impact is often but not always mutual. These
findings are consistent with the conclusions drawn from previous research
discussed in Ioannidis (2005); Leydesdorff and Rafols (2009); Van Noorden
et al. (2015). However, the present findings are drawn from much more
comprehensive sets of fine-grained data.

Hierarchical Research Fields Classification
29
cs
phys
earth
space
chem
eng
purem
gender
edu
psy
pub
bio
med
Fig. 7 Diagram of high demand (out-degree) and high supply (in-degree) among selected
disciplines. Discipline labels are “eng”: Engineering and technology; “space”: Space sciences; “pub”: Public
policy; “gender”: Gender and sexuality studies; “earth”: Earth sciences; “bio”: Biology; “purem”: Pure mathe-
matics; “cs”: Computer science; “edu”: Education; “phys”: Physics; “chem”: Chemistry; “med”: Medicine; “psy”:
Psychology.
To better visualize the strong demand-supply relationships among some
disciplines, we only look at red cells (with relative row-normalized citation
values greater than 0.06) in Figure 6 and draw them in a diagram. In Figure 7,
we summarize the above-mentioned finding in a bidirectional graph, where the
out-degree indicates demand and the in-degree indicates supply of impact. For
instance, when “Computer science” (d) cites (demands from) “Chemistry” (d′),
we speak of the relative out-degree of “Computer science” (d), here. Conversely,
when “Computer science” (d) is cited by (supplies to) “Chemistry” (d′), we
speak of relative in-degree of “Computer science” (d).
We observe in Figure 7 that “Engineering and Technology”, “Computer
science”, “Chemistry”, and “Biology” have both a high in-degree (supply) and
a high out-degree (demand). Moreover, some disciplines such as “Medicine”,
“Chemistry”, and “Biology” form a relative citation cluster with mutual
interdependencies (by counting the triangular structures). It is essential to
understand these connections and dependencies. For instance, they may reveal
an intrinsic similarity among disciplines in terms of the research methods and
subjects (reflected in mutual impact) apart from interdisciplinary influence in
a more narrow sense.
We now discuss the net output matrix D0 = O0 −I0, where I0 denotes the
raw matrix of citation-count inputs, demand by fields in rows and supply from
fields in columns and O0 = I′
0.19 Its row-normalized variant is D. They are
illustrated in Figure 8. Note that D0 is normalized by the absolute row sum.20
19With matrices and vectors, a superscript prime (′) will generally indicate a transpose.
20Note that one should not simply row-normalize D0, because D contains positive and negative
cell entries.

30
Hierarchical Research Fields Classification
(a) D0
0
1
2
3
4
5
6
7
8
9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43
Raw Citations 
0 =
0
0
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
Net Output
6
4
2
0
2
4
6
1e6
(b) D
0
1
2
3
4
5
6
7
8
9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43
Absolute Row Sum Normalization
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
Net Output
0.15
0.10
0.05
0.00
0.05
0.10
Fig. 8 Net output matrices (raw net citation counts and row-normalized).

Hierarchical Research Fields Classification
31
Out Citations of Fields  (Supply/Output) 
 Row Sum Normalization (truncated at 0.01, same color >= 0.01)
In Citations of Fields (Demand/Input)
cs
cs
econ
econ
purem
purem
phys
phys
agri
agri
anthro
anthro
arch
arch
area
area
div
div
earth
earth
env
env
ethnic
ethnic
fam
fam
gender
gender
geo
geo
human
human
law
law
lib
lib
ling
ling
lit
lit
org
org
perf
perf
phil
phil
pol
pol
pub
pub
rel
rel
socw
socw
space
space
sys
sys
trans
trans
vis
vis
logic
logic
edu
edu
bus
bus
chem
chem
eng
eng
hist
hist
med
med
mil
mil
psy
psy
soc
soc
jour
jour
appliedm
appliedm
bio
bio
0.000
0.002
0.004
0.006
0.008
0.010
Fig. 9 Across-and-within field interdisciplinary row-normalized demand of all fields in I.
An inspection of D0 suggests that certain disciplines have a positive net output,
which is indicated by the red rows in Figrue 8 (a), e.g., “Computer science” (0),
“Economics” (1), “Pure mathematics” (2), “Space science” (27), “Chemistry”
(34) and “Biology” (43). The latter means that a discipline influences other
disciplines more than it absorbs from them.
7.3 Intra- And Interfield Citation Scores For 718 Fields
Within 44 Disciplines
We next move from pairs {d, d′} of disciplines to pairs {f, f ′} of fields.Figure
9 illustrates the distribution of row-normalized inter-field impacts among 718
fields, focusing on relative citation input/demand. For better visibility, we
do not only row normalize the matrices I0 and O0 but additionally use a
truncation threshold value of 0.01 (setting all cell values larger than the
threshold value to 0.01). Moreover, we indicate the disciplinary boundaries so
as to clearly spot intra- and inter-disciplinary demand across fields. We can
summarize the respective results as follows:

32
Hierarchical Research Fields Classification
In Citations of Fields (Demand/Input)  
 Row Sum Normalization (truncated at 0.01, same color >= 0.01)
Out Citations of Fields  (Supply/Output)
cs
cs
econ
econ
purem
purem
phys
phys
agri
agri
anthro
anthro
arch
arch
area
area
div
div
earth
earth
env
env
ethnic
ethnic
fam
fam
gender
gender
geo
geo
human
human
law
law
lib
lib
ling
ling
lit
lit
org
org
perf
perf
phil
phil
pol
pol
pub
pub
rel
rel
socw
socw
space
space
sys
sys
trans
trans
vis
vis
logic
logic
edu
edu
bus
bus
chem
chem
eng
eng
hist
hist
med
med
mil
mil
psy
psy
soc
soc
jour
jour
appliedm
appliedm
bio
bio
0.000
0.002
0.004
0.006
0.008
0.010
Fig. 10 Across-and-within field interdisciplinary row-normalized supply of all fields in O.
• Within each discipline, fields in “Physics”, “Earth science”, “Logic”, “Chem-
istry”, and “Biology” have a strong intra-field citation demand.
• Some disciplines have extremely high intra-disciplinary inter-field impacts
compared to inter-disciplinary inter-field impacts. Examples are “Psychol-
ogy” and “Biology”.
• There is only one discipline, “Physics”, where the strongest inter-field cita-
tion demand is not from within its own discipline, but from outside (namely
“Space science”, “Chemistry” and “Engineering”).
• There are some disciplines such as “Psychology” and “Sociology” that
are highly demanded by clusters of disciplines (those belonging to the
humanities and social sciences).
Figure 10 focuses on the (truncated) relative citation output/suply. For
reasons of better visibility, here we also choose a threshold value of 0.01. The
corresponding findings can be summarized as follows:
• Intra-field supply in most fields is not higher compared to the supply from
other fields within the same discipline.

Hierarchical Research Fields Classification
33
Absolute Row Sum Normalization (truncated at 0.01, same color >= 0.01) 
Net Output Matrix
cs
cs
econ
econ
purem
purem
phys
phys
agri
agri
anthro
anthro
arch
arch
area
area
div
div
earth
earth
env
env
ethnic
ethnic
fam
fam
gender
gender
geo
geo
human
human
law
law
lib
lib
ling
ling
lit
lit
org
org
perf
perf
phil
phil
pol
pol
pub
pub
rel
rel
socw
socw
space
space
sys
sys
trans
trans
vis
vis
logic
logic
edu
edu
bus
bus
chem
chem
eng
eng
hist
hist
med
med
mil
mil
psy
psy
soc
soc
jour
jour
appliedm
appliedm
bio
bio
0.000
0.002
0.004
0.006
0.008
0.010
Fig. 11 Truncated absolute row-normalized net output matrix D across 718 fields.
• All fields in some disciplines supply to many fields in some related disci-
pline. E.g,. fields in “Physics” supply highly to those in “Chemistry”, “Space
science”, and “Engineering”.
• “Psychology” and “Biology” display a high inter-field disciplinarity in supply
within their disciplinary boundaries.
Following the procedure for computing the net output matrix D0 and its
absolute row normalized variant D in Section 7.2, we generate a normalized
net output matrix of fields. To better visualize the matrix D, we again truncate
it, using a threshold value of 0.01 for the cell entries of D in Figure 11.
From this we observe that fields in disciplines such as “Physics”, “Earth
science”, “Chemistry”, and “Biology” form a cluster that generates net citation
output to fields from the same cluster but in other disciplines.
We see that the fields in “Physics” and “Chemistry” have a strong impact
on the fields in “Chemistry” and “Engineering” (red cells). We see that there
are no largely excessive net relative inputs (negative net relative output) rel-
ative to the chosen threshold value. However, if we look at the net output at
the discipline level (Figure 8), the variation is much greater.

34
Hierarchical Research Fields Classification
field
discipline
Fig. 12 Illustration of interfieldness and units of analysis.
7.4 Interfieldness Within and Across Disciplines
(Interdisciplinarity)
We care about various levels of the impact of a research field or a discipline
on others. In what follows, we will focus on “interfieldness” – the citation
connectivity between pairs of fields – within a discipline (Section 7.4.1) and
across disciplines, that is, interdisciplinarity (Section 7.4.2), always keeping
the focus on a granularity at the level of fields of research.
7.4.1 Within-Discipline Interfieldness
Here, we will focus on one concept of measurement of interfieldness: normalized
cross-field citation counts within a discipline. Think of an Nd×NFd assignment
matrix ZFd that has as many rows as there are publications in discipline d
and as many columns as there are fields in d. Let Cdd be the binary-entry,
Nd × Nd citation-input matrix of field d. Then, we obtain an unnormalized
interfieldness matrix of size Fd × Fd:
Idd0 = Z′
FdCddZFd,
(1)
where Idd0 is a submatrix of the earlier citation-input matrix I0 for all pairs
{f, f ′} of fields in discipline d. Note that, as before, the raw output matrix
is defined as Odd0 = I′
dd0. Discipline block matrices Idd0 along the diagonals

Hierarchical Research Fields Classification
35
0.005
0.010
0.015
0.020
0.025
References (Demand) from Outside Fields Within Discipline            
 (
dd
dd
IFd)
Fd
0.005
0.010
0.015
0.020
0.025
Citations (Supply) to Outside Fields Within Discipline            
 (
dd
dd
IFd)
Fd
0-0
0-1
0-2
0-3
0-4
0-5
0-6
0-7
0-8
0-9
0-10
0-11
0-12
Less interdisciplinary
More interdisciplinary
    0-0     Information systems
    0-1     Hardware
    0-2     General and reference
    0-3     Social and professional topics
    0-4     Applied computing
    0-5     Computer systems organization
    0-6     Human-centered computing
    0-7     Mathematics of computing
    0-8     Theory of computation
    0-9     Networks
    0-10    Computing methodologies
    0-11    Security and privacy
    0-12    Software and its engineering
Computer science
0.005
0.010
0.015
0.020
0.025
0.030
References (Demand) from Outside Fields Within Discipline            
 (
dd
dd
IFd)
Fd
0.005
0.010
0.015
0.020
0.025
0.030
Citations (Supply) to Outside Fields Within Discipline            
 (
dd
dd
IFd)
Fd
1-0
1-1
1-2
1-3
1-4
1-5
1-6
1-7
1-8
1-9
1-10
1-11
1-12
1-13
1-14
Less interdisciplinary
More interdisciplinary
    1-0   Microeconomics
    1-1   General Economics and Teaching
    1-2   Other Special Topics
    1-3   Law and Economics
    1-4   Agricultural and Natural Resource Economics 
            & Environmental and Ecological Economics
    1-5   Public Economics
    1-6   Economic Development, Innovation, Technological 
            Change, and Growth
    1-7   History of Economic Thought, Methodology, 
            and Heterodox Approaches
    1-8   International Economics
    1-9   Mathematical and Quantitative Methods
    1-10  Industrial Organization
    1-11  Labor and Demographic Economics
    1-12  Economic Systems
    1-13  Business Administration and Business Economics 
            & Marketing & Accounting & Personnel Economics
    1-14  Macroeconomics and Monetary Economics
Economics
Fig. 13 Interfieldness by demand from and supply to other within-discipline fields in two
exemplary disciplines (“Computer science” and “Economics”).

36
Hierarchical Research Fields Classification
are visualized in Figure 12. Again, we row normalize Idd0 to get Idd and row
normalize I′
dd0 to get Odd.
For any generic matrix V with elements vij, let tr(V ) = P
i vii denote the
trace of V , defined as the sum of diagonal elements. With an identity matrix
INd that has the same number of rows and columns as there are publications
in the discipline d, Nd, we have tr(INd) = Nd. Note that by design, tr(Cdd) =
0, because all citations are between research publications (there are no self-
citations at the publication level). Let ιNd and ιFd denote column vectors of as
many rows as there are publications and fields in the discipline d, respectively.
It will be useful to utilize k for Fd × 1 vectors of (some) degree in rows of
matrices and κ for degree-based scalars.
Armed with those definitions, we can state the following properties for each
field:
• the vector of the total number of in-citations per field within discipline d is
kin
Cdd = Idd0ιFd;
• the vector of the total number of out-citations per field within discipline d
is kout
Cdd = Odd0ιFd;
• the total number of citations within discipline d is κtotal
Cdd = ι′
FdIdd0ιFd, where
κtotal
Cdd = ι′
Fdkin
Cdd = ι′
Fdkout
Cdd;
• the total number of intrafield citations in discipline d is κintra
Cdd
= tr(Idd0) =
tr(Odd0);
• the total number of interfield citations in discipline d is κinter
Cdd
= κtotal
Cdd −
κintra
Cdd .
We first focus on the interfieldness within each discipline, i.e., the intra-
disciplinary but interfield citation scores. By subtracting the diagonal elements
in the normalized matrices Idd and Odd (i.e., the ratio of intrafield citations
κintra
Cdd
in kin
Cdd and kout
Cdd), we plot the demand and supply of fields from and
to other fields within a discipline. An inspection of those plots attests to vary-
ing patterns of interfieldness within the 44 disciplines (see the complete set of
figures in our online Appendix B).21 In Figure 13, we illustrate the said pat-
terns for two disciplines that are sufficiently different, namely computer science
and economics.
In computer science, almost all fields have balanced demand and supply
towards other fields within the discipline. Most of the fields in computer science
have a high degree of interfield citations with one exception, applied computing
(0-4).22 In economics, we see a dispersion of demand and supply in fields, with
fields like microeconomics (1-0), history of economic thought (1-7), economic
systems (1-12) in the right upper corner having more references from outside
fields and a high interfieldness score.
21Online appendix is accessible under https://gitlab.ethz.ch/raox/science-clf/-/blob/main/
result tables/online appendix.pdf.
22We will see subsequently that applied computing has a high interdisciplinarity score to fields
outside of computer science (see Figures 9 and 10), while having a low interfieldness score within
its own discipline.

Hierarchical Research Fields Classification
37
Let us use Idd0 −Odd0 = −Ddd0 to denote the unnormalized net cita-
tion inflow matrix and Idd0 + Odd0 to denote the unnormalized total citation
flow matrix. Finally, let |−Ddd0| denote the absolute net in- or outflows of
citations per field in discipline d. (−Ddd0)ιFd is a vector of (positive or neg-
ative) in-citation flows. Using (Idd0 ◦IFd) as the Fd × Fd diagonal matrix of
unnormalized intra-field citations in d, ktotal
Cdd0 = (Idd0 + Odd0 −(Idd0 ◦IFd))ιFd
is the vector of total in- and out-citations, avoiding intra-field citations to
be counted twice. Then, the following scores can be defined for each field.
The vector of intra-field citation scores within the discipline d is ςintra
d
=
ιFd −diag(ktotal
Cdd0)−1(|−Ddd0|)ιFd. The elements of the latter are bounded
between zero and one, and they are larger for fields with higher intra-field cita-
tion scores relative to all intra-disciplinary citations of all the fields demand
and supply. ςunbal
d
= diag(ktotal
Cdd0)−1(−Ddd0)ιFd is a score that is bounded by
(−1, 1) and indicates the relative degree of in- over out-citations per field. ςintra
d
and ςunbal
d
can be simply or field-citation-weighted averaged for each discipline
d.
We report on these results in Table 3 for a simple average of ςintra
d
in col-
umn (3) and ςunbal
d
in column (4) across all fields within one discipline d.23
A higher score of ςintra
d
indicates higher average intra- rather than inter-field
contributions within a discipline. A more negative (positive) score of ςunbal
d
indicates that the average field in a discipline supplies (demands) more cita-
tions than it demands (supplies) from or to other fields within the respective
discipline.24
The table indicates that disciplines “Pure mathematics”, “Logic”, “Mil-
itary science”, and “Journalism” exhibit particularly high intra-field scores,
whereas “Economics”, “Physics”, “Family Studies”, and “Systems science”
have above average intra-field citation scores. Furthermore, the results sug-
gest that “Physics”, “Area studies”, “Family studies”, and “Systems science”
(most of those apearing with low intra-field scores above) have relatively large
intradisciplinary net donors of citations (the smallest negative ςunbal
d
values in
column (4) of Table 3), whereas “Computer science”, “Architecture”, “Per-
forming arts”, and “Transportation studies”have relatively large net recipients
(the largest positive ςunbal
d
in column (4) of Table 3).
7.4.2 Across-Discipline Interfieldness (Interdisciplinarity)
We next consider the interfieldness of the 718 fields across disciplines.
Therefore, the focus in this section is entirely on interdisciplinarity. Before scru-
tinizing on individual fields, let us consider the scores at the level of aggregate
disciplines.
It will be useful to define the block-diagonal matrix of unnormalized in-
citations B0 = diagD
d=1(Idd0) as well as the matrices I∗
0 = I0 −B0 and O∗
0 =
23The full result table of ςintra
d
(column (3)) and ςunbal
d
(column (4)) on each field is accessi-
ble under https://gitlab.ethz.ch/raox/science-clf/-/blob/main/result tables/interfieldness tables
appendix/output sigma.csv.
24Note that ςunbal
d
does not mechanically sum to zero for a discipline because of the asymmetry
of I.

38
Hierarchical Research Fields Classification
Table 3 Interfieldness scores per discipline d within and across disciplines.
[Within-discipline] column (3): intra-field scores ςintra
d
, column (4): relative in- over out citation scores ςunbal
d
.
[Across-discipline] column (5): in- and out-citation scores overlap in interdisciplinary citation ςinter
d
,
column (6): relative in- over out-citation scores ςunbal
¬d
.
We mark the top 4 highest scores per column in bold and underline the four lowest scores.
Discipline label
Discipline
ςintra
d
ςunbal
d
ςinter
d
ςunbal
¬d
(1)
(2)
(3)
(4)
(5)
(6)
0
Computer science
0.8846
0.0675
0.8558
0.0880
1
Economics
0.8231
0.0054
0.7938
-0.0948
2
Pure mathematics
0.9933
-0.0001
0.9575
-0.0234
3
Physics
0.8357
-0.0581
0.8216
-0.0921
4
Agriculture
0.9315
-0.0299
0.8630
0.0208
5
Anthropology
0.9758
-0.0180
0.9366
0.0089
6
Architecture
0.8390
0.0888
0.8004
0.1167
7
Area studies
0.8729
-0.0682
0.8532
-0.0104
8
Divinity
0.9130
-0.0283
0.8491
-0.0754
9
Earth science
0.9409
-0.0147
0.9114
-0.0064
10
Environmental science
0.9582
0.0001
0.8855
0.0655
11
Ethnic studies
0.9443
-0.0165
0.9083
-0.0541
12
Family studies
0.7338
-0.0969
0.5721
0.2574
13
Gender studies
0.9378
-0.0030
0.9021
0.0438
14
Geography
0.9159
0.0236
0.8745
0.0554
15
Human performances
0.8906
0.0270
0.8712
0.0424
16
Law
0.9313
-0.0302
0.9000
-0.0534
17
Library science
0.9555
0.0283
0.9056
0.0653
18
Linguistics
0.9040
-0.0141
0.8904
-0.0404
19
Literature
0.9253
-0.0215
0.8833
-0.0516
20
Organizational studies
0.9156
-0.0117
0.9003
0.0132
21
Performing arts
0.9227
0.0296
0.8535
0.1051
22
Philosophy
0.9708
0.0010
0.9468
-0.0117
23
Political science
0.9469
0.0002
0.9054
0.0465
24
Public administration
0.9346
0.0055
0.9085
0.0245
25
Religious studies
0.9507
-0.0123
0.9158
-0.0250
26
Social work
0.9617
0.0060
0.9332
0.0253
27
Space science
0.9701
0.0049
0.8942
-0.0760
28
Systems science
0.8328
-0.0487
0.7869
0.0284
29
Transportation studies
0.9453
0.0296
0.9194
0.0416
30
Visual arts
0.9770
-0.0097
0.9064
-0.0238
31
Logic
0.9851
0.0024
0.9623
-0.0060
32
Education
0.9325
0.0158
0.9040
0.0538
33
Business
0.9362
0.0067
0.8959
0.0681
34
Chemistry
0.9083
-0.0033
0.9112
-0.0332
35
Engineering
0.9301
-0.0267
0.8929
0.0597
36
History
0.9473
-0.0183
0.9105
-0.0130
37
Medicine
0.9305
0.0205
0.9050
0.0271
38
Military science
0.9820
-0.0068
0.9789
-0.0152
39
Psychology
0.9460
-0.0059
0.9445
-0.0073
40
Sociology
0.9106
-0.0239
0.9064
-0.0378
41
Journalism
0.9919
0.0032
0.9513
0.0179
42
Applied mathematics
0.9641
-0.0136
0.9578
-0.0303
43
Biology
0.8914
0.0245
0.9149
-0.0380
I∗′
0 . The latter two matrices exclude the intra-disciplinary citation blocks Idd0
visualized in Figure 12. Upon using I and O and B = diagD
d=1(Idd), we can
obtain the normalized I∗and O∗analogously to O∗
0 = I∗′
0 . Note that their

Hierarchical Research Fields Classification
39
0.92
0.94
0.96
0.98
1.00
References (Demand) from Outside Disciplines 
 (
ID)
D
0.92
0.94
0.96
0.98
1.00
Citations (Supply) to Outside Disciplines 
 (
ID)
D
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
Less interdisciplinary
More interdisciplinary
0: Computer science
1: Economics
2: Pure mathematics
3: Physics
4: Agriculture
5: Anthropology
6: Architecture
7: Area studies
8: Divinity
9: Earth science
10: Environmental science
11: Ethnic studies
12: Family studies
13: Gender studies
14: Geography
15: Human performances
16: Law
17: Library science
18: Linguistics
19: Literature
20: Organizational studies
21: Performing arts
22: Philosophy
23: Political science
24: Public policy
25: Religion
26: Social work
27: Space science
28: Systems science
29: Transportation studies
30: Visual arts
31: Logic
32: Education
33: Business
34: Chemistry
35: Engineering
36: History
37: Medicine
38: Military science
39: Psychology
40: Sociology
41: Journalism
42: Applied mathematics
43: Biology
Humanities
Social sciences
Natural sciences
Formal sciences
Professions and applied sciences
Fig. 14 Degrees of interdisciplinarity by demand from and supply to outside disciplines in
44 disciplines.
rows do not sum up to unity, but to less than unity, depending on the relative
weight of intradisciplinary citations.
Similar to the exercise in Figure 13, we plot the demand from and supply
to outside disciplines in terms of citations in Figure 14. The underlying metrics
are based on the D row sums of 44×44 (aggregated) discipline-level counterpart
matrices to I∗and O∗. The aggregated matrices obtain one pair of (in- and out-
citation interdiscipline) values for each of the 44 disciplines. Similar to Figure
3 in Van Noorden et al. (2015), we show the degrees of interdisciplinarity at
the level of discipline in Figure 14.
In the figure, more interdisciplinary disciplines are found in the top-right
area and the less interdisciplinary ones are found in the bottom-left area of
the figure. The position of a discipline is determined by two factors: the extent
to which its research output is cited by disciplines outside its own (on the
abscissa), and the extent to which those outside disciplines are cited by that
discipline (on the ordinate). As with the fields-based matrix, the scores are
lower than unity, because the diagonal (here a scalar, at the level of fields a
matrix) is subtracted. Figure 6 indicates that the disciplines vary significantly

40
Hierarchical Research Fields Classification
in terms of their interdisciplinarity scores. At the low interdisciplinarity end we
find “Biology” and “Chemistry”, while at the high end we find “Area studies”
and “Family studies”.
For better illustration, we group the disciplines by the Wikipedia dis-
cipline classification depicted in Figure 1. There are five broad categories:
“Humanities”, “Social sciences”, “Natural sciences”, “Formal sciences”, and
“Professions and applied sciences”. The visualization suggests that there is a
lower degree of interdisciplinarity in the “Natural sciences” (+). “Professions
and applied sciences” (
▶
) have a large variation in terms of interdisciplinarity.
In that category, “Engineering and technology” (35) shows the least demand
and supply from and to outside disciplines, while “Education” (32) has a high
interdisciplinary demand and supply. Apart from “Computer science” (0), the
other “Formal sciences” (×) have a high interdisciplinarity. Disciplines in the
“Humanities” (
) have a relatively high demand and supply from and to
outside disciplines, and so do disciplines in “Social sciences” (•).
These results only partially corroborate the ones in Figure 3 in Van Noor-
den et al. (2015). There as well as here the “Social sciences” display a high
degree of interdisciplinarity and “Physics” (3) has a low one. Some fields such
as “Anthropology” (4) or “Psychology” (39) have similar positions w.r.t. other
disciplines between Van Noorden et al. (2015) and our study. Yet, some other
fields (“Biology” (43) and “Applied mathematics” (42)) show an opposite posi-
tioning in comparison to Van Noorden et al. (2015).25 Since the sample in
Van Noorden et al. (2015) is based on only 35 million articles in 2001-2010
in the Web of Science of 14 major conventional disciplines and 143 fields, we
cannot draw decisive conclusions based on the differences. However, any dif-
ferences may suggest there being interesting results to emerge from tracking
longitudinal changes of interdisciplinarity in larger disciplinary cross sections.
Next we focus on individual fields in the 44 disciplines, of which there are
F = 718. We perform the same exercise as above for the 718 individual fields
to measure their interdisciplinarity scores in Figure 15, excluding fields within
each discipline. The underlying metrics are now based on the F row sums
of I∗and O∗, obtaining one pair of values for each of the 718 fields. Again,
we augment the analysis with results grouped by the five broad categories of
disciplines used above. The respective analysis suggests distinctive patterns
for the fields in different categories. (1) Ones in the “Natural sciences” (+)
and “Social sciences” (•) have the highest variability of interdisciplinarity.
(2) Fields in “Professions and applied sciences” (
▶
), “Humanities” (
) , and
“Formal sciences” (×) have a relatively high average degree interdisciplinarity.
We mark fields that are in various spectrums of the distribution for a better
comparison between the two visualizations. Clearly, we see some bimodality
for the fields we single out: some are highly dependent on fields within their
25“Biology” in Figure 3 of Van Noorden et al. (2015) has a wide variation in interdisciplinarity,
with “General biology” on the upper right corner and the remaining fields scattered in the middle
spectrum of distribution.

Hierarchical Research Fields Classification
41
0.5
0.6
0.7
0.8
0.9
1.0
References (Demand) from Outside Fields (excl. within-discipline fields) 
 
*
F
0.5
0.6
0.7
0.8
0.9
1.0
Citations (Supply) to Outside Fields (excl. within-discipline fields) 
 
*
F
6-7
1-7
1-9
39-38
43-12
34-31
3-16
3-31
3-49
0-4
28-7
6-7
29-8
Less interdisciplinary
More interdisciplinary
0-4     CS-Applied computing (Formal sciences)
1-7     Econ-History of Economic Thought, Methodology, 
          and Heterodox Approaches (Social sciences)
1-9     Econ-Mathematical and Quantitative Methods
          (Social sciences)
6-7     Arch-Fashion_design (Humanities)
3-16    PACS-Stars (Natural sciences)
3-31    PACS-Specific theories and interaction models;
           particle systematics (Natural sciences)
3-49    PACS-Solid earth physics (Natural sciences)
28-7    Sys-Systems_engineering (Formal sciences)
29-8    Trans-Vehicles (Professions and applied sciences)
34-31   Chem-Physical_organic_chemistry (Natural sciences)
39-38   Psy-Forensic_developmental_psychology (Social sciences)
43-12   Bio-Human_biology (Natural sciences) 
Humanities
Social sciences
Natural sciences
Formal sciences
Professions and applied sciences
Fig. 15 Degrees of interdisciplinarity by demand from and supply to outside fields in 718
fields, excl. within-discipline fields.
home disciplines (39-38, 43-12, 34-31), while others are very interdisciplinary
(6-7, 28-7).
Let us consider ςinter
d
and ςunbal
¬d
, with ¬d denoting the fields that are
outside of a discipline d. These two are Fd × 1 vectors for discipline d, which
are defined as the discipline-d specific Fd × 1 subvectors of:
ςinter
d
= ιF −diag(ktotal
F
)−1(|I∗
0 −O∗
0|)ιF ,
(2)
ςunbal
¬d
= diag(ktotal
F
)−1(I∗
0 −O∗
0)ιF ,
(3)
where ktotal
F
= (I0 + O0 −(O0 ◦IF ))ιF . The term ςinter
d
captures the in- and
out-citation overlap in interdisciplinary citation scores per field in discipline
d relative to all others. ςunbal
¬d
measures the relative degree of in- over out-
citations for the average pair of fields in one discipline relative to all others.
The results are reported in columns (5) and (6) of Table 3 by taking the
simple average of all fields within discipline d.26 In the interdisciplinary setting,
we find that “Pure mathematics”, “Logic”, “Military science”, and “Applied
mathematics” have particularly high in-out-citation overlap scores ςinter
d
, and
“Architecture” (6), “Family studies” (12), “Systems Science” (28) have above
26The full result table of ςinter
d
(column (5)) and ςunbal
¬d
(column (6)) on each field
is accessible at https://gitlab.ethz.ch/raox/science-clf/-/blob/main/result tables/interfieldness
tables appendix/output sigma wo dfields.csv.

42
Hierarchical Research Fields Classification
average in- and out-citation overlapping scores. These disciplines have both a
relatively high ςintra
d
and ςinter
d
compared to other disciplines. These findings
are consistent with the discipline-level analysis in Figure 14. They are situated
in the middle-upper spectrum of the distribution, which indicates a relative
high demand from and supply to the outside disciplines.
The ranking of ςunbal
¬d
of some disciplines has changed a lot compared
to ςunbal
d
within the discipline. In interdisciplinary settings, “Family studies”
has become a large net recipient (the largest ςunbal
¬d
), while “Economics” has
become a net donor (negative ςunbal
¬d
).
Overall, by considering fields as the unit of analysis in studying inter-
disciplinarity, it is possible to attribute metrics to fields and consider the
distribution within and across disciplines in finer granularity. This approach
provides a more comprehensive understanding of research links across disci-
plines, eventually even over time and in geographical space.
8 Conclusion and Future Work
In this paper, we have devised a three-level hierarchical classification system
for scientific publications based on state-of-the-art deep learning methods. This
system supports multi-label classifications in both single-label and multi-label
settings. We have enabled a modularized classification system that copes with
a large and increasing number of publications and supports quick update of
submodels. We have conducted numerous experiments to test the efficiency of
our system. Moreover, we have developed analytics and metrics in measuring
interfieldness within and across disciplines on the level of field. We provide
this platform and data to the research community and invite joint efforts to
enable an efficient ecosystem in the classification of scholarly publications and
the analysis of interdisciplinarity.
As introduced in Section 1, this project is part of a larger research agenda
which aims to tackle multifaceted problems in archiving and organizing expo-
nentially growing scientific publications. As a next step shown in Figure 16,
we would like to involve human-in-the-loop (like human annotations for model
improvement) in crowd-sourcing label quality improvement and, in exchange,
provide an even higher quality database of scholarly publications. Especially,
now that Microsoft Academic Services is no longer available, we are looking
to provide a brand new competitive solution to existing players in the mar-
ket, deploying machine learning models into an interactive web front-end using
Label Studio (Tkachenko et al., 2022), an open-source data labeling tool. To
this end, we have already developed SAINE (Rao et al., 2023), a Scientific
Annotation and Inference Engine of Scientific Research, to better understand
classification results.
In future work, as an extension of the interfieldness analysis, we plan to
use the entire graph (after inference using the models) using OpenAlex to
compute the statistics reported in Section 7. In addition, we are also working
on reproducing the ogbn-MAG benchmark (Hu et al., 2020) using our own
field classifications.

Hierarchical Research Fields Classification
43
Fig. 16 Science hierarchical classification lifecycle.

44
Hierarchical Research Fields Classification
Acknowledgments.
We thank Ms. Piriyakorn Piriyatamwong for her tech-
nical support to our project. The authors also thank the Microsoft Academic
Service and especially Charles Huang for providing instructions to download
the data.
Statements and Declarations
• Funding
Peter Egger and the Chair of Applied Economics acknowledge the sup-
port of the Department of Management, Technology, and Economics at
ETH Zurich. Ce Zhang and the DS3Lab gratefully acknowledge the support
from the Swiss State Secretariat for Education, Research and Innovation
(SERI) under contract number MB22.00036 (for European Research Coun-
cil (ERC) Starting Grant TRIDENT 101042665), the Swiss National Science
Foundation (Project Number 200021 184628, and 197485), Innosuisse/SNF
BRIDGE Discovery (Project Number 40B2-0 187132), European Union
Horizon 2020 Research and Innovation Programme (DAPHNE, 957407),
Botnar Research Centre for Child Health, Swiss Data Science Center,
Alibaba, Cisco, eBay, Google Focused Research Awards, Kuaishou Inc., Ora-
cle Labs, Zurich Insurance, and the Department of Computer Science at
ETH Zurich.
• Conflict of interest/Competing interests
ETH Zurich Domain; University of Zurich, Department of Computational
Linguistics: https://www.cl.uzh.ch/en.html.
• Ethics approval
Not applicable.
• Availability of data and materials
We plan to make the data publicly available (raw data and intermediary
data) upon acceptance of the manuscript. Due to the sheer size of raw and
intermediary data, we will upload the LMDB instances for each discipline
to Zenodo or Mendeley Data.
• Code availability
The code base has been made available under https://gitlab.ethz.ch/raox/
science-clf.
• Authors’ contributions (14 roles in CRediT)
(1) Conceptualization: Peter Egger, Susie Xi Rao, Ce Zhang. (2) Data cura-
tion: Susie Xi Rao. (3) Formal analysis: Peter Egger, Susie Xi Rao. (4)
Funding acquisition: Peter Egger, Ce Zhang, Susie Xi Rao. (5) Investigation:
Susie Xi Rao, Peter Egger. (6) Methodology: Susie Xi Rao, Ce Zhang, Peter
Egger. (7) Project administration: Peter Egger, Ce Zhang, Susie Xi Rao. (8)
Resources: Peter Egger, Ce Zhang, Susie Xi Rao. (9) Software: Susie Xi Rao.
(10) Supervision: Peter Egger, Ce Zhang. (11) Validation: Susie Xi Rao,
Peter Egger. (12) Visualization: Susie Xi Rao, Peter Egger. (13) Writing -
original draft: Susie Xi Rao, Peter Egger. (14) Writing - review & editing:
Peter Egger, Susie Xi Rao, Ce Zhang.

Hierarchical Research Fields Classification
45
Appendix A
Case Study of Economics,
Computer Science and
Mathematics
To obtain the most accurate ground truth labels for every hierarchical level,
we decided to proceed with papers that are archived according to systematic
hierarchical classification code systems. As such, we restrict our attention to
papers from the following three sources as the first case study.
1. Association for Computing Machinery (ACM), a peer-reviewed journal for
computer science.
2. Journal of Economic Literature (JEL), a peer-reviewed journal for eco-
nomics.
3. Mathematics Subject Classification (MSC), a classification system for
mathematical publications.
By restricting ourselves to three disciplines, we show proof of concepts of
how the hierarchical classification performs. We list the class distribution in
the three datasets in Table A1.
Discipline (L1)
Number of documents
Number of
disciplines (L2)
Number of
disciplines (L3)
ACM (Computer Science)
11,637,219
13
13
JEL (Economics)
8,439,655
15
47
MSC (Mathematics)
10,214,588
55
252
Total
30,291,462
83
312
Table A1 Summary of MAG datasets used in our case study.
A.1
Topic modelling
We have tested topic modeling in both supervised (Mcauliffe and Blei, 2007)
and unsupervised fashions (Blei et al., 2003) by first discovering topics of 55
disciplines using their textual descriptions on the Wikipedia page “List of
academic fields”. Unfortunately, the topic words generated via topic modelling
failed to capture the nuance between fields (class confusability). Using these
lists of words to represent a field is too coarse to link a publication in MAG to
a field. We list four subfields (“Biophysics”, “Molecular biology”, “Structural
Biology”, “Biochemistry”) below that share a similar set of topic words / topic
nouns using a supervised topic model. The complete list of topic words for all
fields and their field description could be found here in our project repository.
<topic>Biophysics</topic>
<TopicWords>biophysics, biology, -, molecular, biological,

46
Hierarchical Research Fields Classification
biophysical, study, department, structure, technique,
system, research, quantum, physic, physiology, chemistry,
protein, biochemistry, interaction, field, medicine, physical,
include, feynman, biomolecular, model, science, apply,
biophysicist, journal, mathematics, experimental, effort,
complex, population, cell, structural, see, molecule, use,
example, microscopy, application, neural, dynamics, computer,
cellular, member, medical, neutron</TopicWords>
<TopicNouns>biophysics, biology, department, study, structure,
technique, system, research, physiology, physic, quantum,
field, biochemistry, medicine, chemistry, interaction,
protein, model, science, journal, biophysicist, feynman,
application, effort, population, mathematics, molecule,
example, cell, computer, dynamics, microscopy, brain, variety,
membrane, nanomedicine, event, alignment, list, complex, gene,
tissue, spectroscopy, idea, machine, society, kinetics,
neutron, physicist, network</TopicNouns>
<topic>Molecular_biology</topic>
<TopicWords>isbn, edition, garland, biology, molecular, base,
biochemistry, rd, pound, nd, link, curlie, external, dmoz,
dna, technique, blot, protein, cell, rna, study, gel,
molecule, gene, probe, pcr, one, size, specific, use,
electrophoresis, expression, array, label, sample, membrane,
interest, sequence, spot, clon, separate, allow, southern,
different, field, via, function, fragment, transfection,
enzyme</TopicWords>
<TopicNouns>isbn, edition, garland, biology, biochemistry, rd,
pound, nd, link, curlie, dmoz, dna, technique, protein, cell,
rna, gel, molecule, pcr, study, gene, size, expression,
electrophoresis, interest, sequence, sample, membrane, spot,
array, blot, probe, field, science, target, function, tissue,
enzyme, transfection, fragment, genetics, interaction,
process, organism, site, restriction, base, time, reaction,
basis</TopicNouns>
<topic>Structural_Biology</topic>
<TopicWords>structure, structural, protein, biology,
molecular, molecule, see, method, model, macromolecule,
function, biologist, shape, acid, make, biochemistry,
biological, cell, tertiary, primary, light, use, native,
small, membrane, study, state, prediction, scattering,
resonance, researcher, electron, spectroscopy, aspect,
physical, deduce, hydrophobicity, integral, amino, predict,

Hierarchical Research Fields Classification
47
alteration, accurate, become, diverse, complement, highly,
understanding, base, topology, approach</TopicWords>
<TopicNouns>structure, protein, biology, molecule, model,
method, function, macromolecule, biologist, light, cell,
biochemistry, acid, electron, researcher, use, spectroscopy,
resonance, prediction, scattering, shape, study, state,
membrane, library, link, magazine, nature, subunit, europe,
cooperativity, pattern, example, datum, reference,
understanding, year, silico, amino, topology, biophysics,
hydrophobicity, aspect, analysis, journal, sequence, density,
chaperonin, bank, bioinformatics</TopicNouns>
<topic>Biochemistry</topic>
<TopicWords>acid, molecule, amino, biochemistry, protein,
form, call, one, two, cell, carbon, glucose, structure, group,
energy, study, enzyme, oxygen, process, biology, molecular,
reaction, biological, life, use, chain, example, glycolysis,
nucleic, organism, carbohydrate, make, living, convert, base,
atom, genetic, reduce, animal, monosaccharide, important, atp,
join, bond, chemistry, lipid, human, function, another,
chemical</TopicWords>
<TopicNouns>acid, molecule, amino, biochemistry, protein,
form, cell, carbon, glucose, structure, group, energy, study,
oxygen, enzyme, process, biology, reaction, life, chain,
example, glycolysis, organism, carbohydrate, living, atom,
animal, monosaccharide, atp, bond, chemistry, lipid, function,
chemical, monomer, sugar, base, pathway, component, role,
information, plant, water, nadh, adenine, ring, rna, residue,
cycle, gene</TopicNouns>
Our trials of topic modelling have led us to supervised methods, i.e.,
classification. And our data are organized in a hierarchical fashion, i.e., one
publication (its representation being its abstract) and its labels (discipline-
field-subfield). The objective of developing a hierarchical classification system
is to leverage the hierarchical organization to create models and classify
unlabeled test instances into one or more categories within the hierarchy.
A.2
Hierarchical SVM
Classification methods proven effective in hierarchical settings are multi-class
support vector machine (SVM) (Sun and Lim, 2001) and stacking SVM, i.e.,
ensemble of individual SVM classifiers (Kenji Nakano et al., 2017). We carried
out experiments using hierarchical multi-class SVM on a benchmarking dataset
WOS-46985 published in Kowsari et al. (2017). The classification is a two-level
system with 13 first-level (L1) labels and 76 second-level (L2) labels and has
achieved only 37% of macro-F1 across all the L2 classes.

48
Hierarchical Research Fields Classification
A.3
Two-Level Classification
As we see from the poor performance of traditional machine learning tech-
niques in the trials, we need a better solution. Kowsari et al. (2017) has
suggested a success of a hierarchical two-level classification system. The idea
has been attractive not because the hype of the belief that every application
should have a deep learning component which just magically makes the per-
formance better, but because we can leverage the hierarchy structure in the
data by linking the submodels on each level by the stacking of layers, and we
can capture the probability distributions of multiple classes via the softmax
at the last layer of each classification component. We denote p a publication,
D one discipline, Fi one field in D. We obtain the unconditional probability
P(p ∈D) from the first component in the system that classifies the disci-
plines and the conditional probability P(p ∈Fi | p ∈D) from the second
component that classifies the fields. In Piriyatamwong (2022), a master the-
sis supervised by Susie Xi Rao, we have shown reasonable performances for
a three-discipline classification (ACM, JEL and MSC) in both scalability and
prediction accuracy.
Appendix B
Training Setup of Our Classifier
System
We thank Ms. Piriyakorn Piriyatamwong for her technical support to our
project. Note that an ablation study of hyperparameters was presented in her
master thesis (Piriyatamwong, 2022) supervised by Susie Xi Rao. Hence, we
took over the hyperparameters configured in this study and reported them in
Appendix B.
Text Vectorization has the following set up:
• Maximum length of text vectors: 200, which makes sense since abstracts are
usually capped to 150-250 words.
• Split: by white space.
• Normalization: lower-casing and punctuation removals.
Keras models have the following set up:
• Batch size: 1,024 unless the model dataset is too small, then the largest
power of 2 smaller than the model dataset.
• Number of epochs: 1, as the performance is sufficiently good and not
overfitted.
• Optimizer: Root Mean Square Propagation (RMSProp)27 with learning rate
0.001. RMSProp accelerates the gradient descent process of optimizing the
loss function.
• Train-test split ratio: 60% training, 40% test.
27http://www.cs.toronto.edu/∼hinton/coursera/lecture6/lec6.pdf
(last
accessed:
May
23,
2022).

Hierarchical Research Fields Classification
49
BERT uncased model has the following set up, following the recommendations
from the original paper (Devlin et al., 2019).
• Batch size: 16 or 32.
• Number of epochs: 2, 3, or 4.
• Optimizer: Adam optimizer with learning rate 2e-5, another computationally
efficient, scalable optimizer with low memory requirement (Kingma and Ba,
2015).
• Train-test split ratio: 60% training, 40% test.
Appendix C
Discipline-to-Coding and
Field-to-Coding Mappings
We list here the discipline to coding mapping for readers’ reference.
The
718
field
labels
are
accessible
in
our
project
repository
under
the
link
https://gitlab.ethz.ch/raox/science-clf/-/blob/main/result tables/
interfieldness tables appendix/718 field labels master copy.csv.
"infk": 0,
"econ": 1,
"purem": 2,
"phys": 3,
"agri": 4,
"anthro": 5,
"arch": 6,
"area": 7,
"div": 8,
"earth": 9,
"env": 10,
"ethnic": 11,
"fam": 12,
"gender": 13,
"geo": 14,
"human": 15,
"law": 16,
"lib": 17,
"ling": 18,
"lit": 19,
"org": 20,
"perf": 21,
"phil": 22,
"pol": 23,
"pub": 24,
"rel": 25,
"socw": 26,
"space": 27,
"sys": 28,
"trans": 29,
"vis": 30,
"logic": 31,
"edu": 32,
"bus": 33,
"chem": 34,
"eng": 35,
"hist": 36,
"med": 37,
"mil": 38,
"psy": 39,
"soc": 40,
"jour": 41,
"appliedm": 42,
"bio": 43
References
American Economic Association. 2018. JEL Classification System / EconLit
Subject Descriptors. https://www.aeaweb.org/econlit/jelCodes.php?view=

50
Hierarchical Research Fields Classification
jel. [Online; accessed 2018-05-23].
American Institute of Physics. 2018.
Physics and Astronomy Classi-
fication Scheme (PACS) 2010 Regular Edition.
https://web.archive.
org/web/20180921190936/https://publishing.aip.org/publishing/pacs/
pacs-2010-regular-edition. [Online; accessed 2018-05-23].
American Mathematical Society (AMS) and Zentralblatt MATH. 2018. MSC
Classification Codes.
https://cran.r-project.org/web/classifications/MSC.
html. [Online; accessed 2018-05-23].
Association for Computing Machinery. 2018.
ACM Computing Classifi-
cation System.
ftp://cran.r-project.org/pub/R/web/classifications/ACM.
html. [Online; accessed 2018-05-23].
Australian Standard Research Classification (ASRC). 2018.
1297.0 - Aus-
tralian Standard Research Classification (ASRC), 1998 . http://www.abs.
gov.au/ausstats/abs@.nsf/0/44871FAF47845EE1CA25697E0018FD1E?
opendocument. [Online; accessed 2018-05-23].
Birkle, C., D.A. Pendlebury, J. Schnell, and J. Adams. 2020. Web of science as
a data source for research on scientific and scholarly activity. Quantitative
Science Studies 1(1): 363–376 .
Blei, D.M., A.Y. Ng, and M.I. Jordan. 2003.
Latent dirichlet allocation.
Journal of machine Learning research 3(Jan): 993–1022 .
Bransford, J.D., A.L. Brown, and R.R. Cocking. 1999.
How people learn:
Brain, mind, experience, and school (pp. xiv-xv). Washington, DC: National
Academy Press. ED 436: 276 .
Chen, A., A. Chow, A. Davidson, A. DCunha, A. Ghodsi, S.A. Hong, A. Kon-
winski, C. Mewald, S. Murching, T. Nykodym, P. Ogilvie, M. Parkhe,
A. Singh, F. Xie, M. Zaharia, R. Zang, J. Zheng, and C. Zumar 2020. Devel-
opments in mlflow: A system to accelerate the machine learning lifecycle. In
Proceedings of the Fourth International Workshop on Data Management for
End-to-End Machine Learning, DEEM’20, New York, NY, USA. Association
for Computing Machinery.
Devlin, J., M.W. Chang, K. Lee, and K. Toutanova 2019, June. BERT: Pre-
training of deep bidirectional transformers for language understanding. In
Proceedings of the 2019 Conference of the North American Chapter of the
Association for Computational Linguistics: Human Language Technologies,
Volume 1 (Long and Short Papers), Minneapolis, Minnesota, pp. 4171–4186.
Association for Computational Linguistics.

Hierarchical Research Fields Classification
51
European Economic Community (EEC) . 2018.
European Economic
Community (EEC) Sciences Classification .
https://eur-lex.europa.eu/
LexUriServ/LexUriServ.do?uri=CELEX:31991H0337:EN:HTML.
[Online;
accessed 2018-05-23].
German Research Foundation (Deutsche Forschungsgemeinschaft). 2018.
DFG Classification of Scientific Disciplines, Research Areas, Review
Boards and Subject Areas (2016-2019).
http://www.dfg.de/download/
pdf/dfg im profil/gremien/fachkollegien/amtsperiode 2016 2019/
fachsystematik 2016-2019 en grafik.pdf. [Online; accessed 2018-05-23].
Godbole, S. and S. Sarawagi 2004. Discriminative methods for multi-labeled
classification.
In H. Dai, R. Srikant, and C. Zhang (Eds.), Advances
in Knowledge Discovery and Data Mining, Berlin, Heidelberg, pp. 22–30.
Springer Berlin Heidelberg.
Grootendorst, M. 2020. Keybert: Minimal keyword extraction with bert.
Gupta, M.R., S. Bengio, and J. Weston. 2014, jan. Training highly multiclass
classifiers. J. Mach. Learn. Res. 15(1): 1461–1492 .
Howard Chu, S.C. 2011. Lightning memory-mapped database manager (lmdb).
http://www.lmdb.tech/doc/index.html. [Online; accessed 2022-10-5].
Hu, W., M. Fey, M. Zitnik, Y. Dong, H. Ren, B. Liu, M. Catasta, and
J. Leskovec. 2020. Open graph benchmark: Datasets for machine learning on
graphs. Advances in neural information processing systems 33: 22118–22133
.
Ioannidis, J.P.A. 2005. Why most published research findings are false. PLoS
Medicine 2(8): e124. https://doi.org/10.1371/journal.pmed.0020124 .
Japanese Society for the Promotion of Science . 2018. List of Categories, Areas,
Disciplines and Research Fields. https://www.jica.go.jp/english/countries/
oceania/c8h0vm00009r53xl-att/annex5.pdf. [Online; accessed 2018-05-23].
Kenji Nakano, F., S.M. Mastelini, S. Barbon, and R. Cerri 2017. Stacking
methods for hierarchical classification.
In 2017 16th IEEE international
conference on machine learning and applications (ICMLA), pp. 289–296.
IEEE.
Kingma, D.P. and J. Ba 2015. Adam: A method for stochastic optimization.
In Y. Bengio and Y. LeCun (Eds.), 3rd International Conference on Learn-
ing Representations, ICLR 2015, San Diego, CA, USA, May 7-9, 2015,
Conference Track Proceedings.

52
Hierarchical Research Fields Classification
Kowsari, K., D.E. Brown, M. Heidarysafa, K.J. Meimandi, M.S. Gerber, and
L.E. Barnes 2017.
Hdltex: Hierarchical deep learning for text classifica-
tion. In 2017 16th IEEE international conference on machine learning and
applications (ICMLA), pp. 364–371. IEEE.
Leydesdorff, L. and I. Rafols. 2009. A global map of science based on the isi
subject categories. Journal of the American Society for Information Science
and Technology 60(2): 348–362 .
Liu, T.Y., Y. Yang, H. Wan, H.J. Zeng, Z. Chen, and W.Y. Ma. 2005, jun.
Support vector machines classification with a very large-scale taxonomy.
SIGKDD Explor. Newsl. 7(1): 36–43.
https://doi.org/10.1145/1089815.
1089821 .
Liu, Y., H.T. Loh, and A. Sun. 2009. Imbalanced text classification: A term
weighting approach.
Expert Systems with Applications 36(1): 690–701.
https://doi.org/https://doi.org/10.1016/j.eswa.2007.10.042 .
LMDB. 2022. Lmdb documentation. http://www.lmdb.tech/doc/index.html.
[Online; accessed: 2022-10-05].
Mart´ın-Mart´ın, A., M. Thelwall, E. Orduna-Malea, and E. Delgado L´opez-
C´ozar. 2021. Google scholar, microsoft academic, scopus, dimensions, web of
science, and opencitations’ coci: a multidisciplinary comparison of coverage
via citations. Scientometrics 126(1): 871–906 .
Mcauliffe, J. and D. Blei. 2007. Supervised topic models. Advances in neural
information processing systems 20 .
Nam, J., J. Kim, E. Loza Menc´ıa, I. Gurevych, and J. F¨urnkranz 2014.
Large-scale multi-label text classification — revisiting neural networks. In
T. Calders, F. Esposito, E. H¨ullermeier, and R. Meo (Eds.), Machine Learn-
ing and Knowledge Discovery in Databases, Berlin, Heidelberg, pp. 437–452.
Springer Berlin Heidelberg.
Organisation for Economic Co-operation and Development (OECD). 2018.
Revised Field of Science and Technology (FOS) Classification in the Fras-
cati Manual.
https://www.oecd.org/science/inno/38235147.pdf.
[Online;
accessed 2018-05-23].
Padurariu, C. and M.E. Breaban. 2019. Dealing with data imbalance in text
classification. Procedia Computer Science 159: 736–745. https://doi.org/
https://doi.org/10.1016/j.procs.2019.09.229 .
Pennington, J., R. Socher, and C. Manning 2014, October. GloVe: Global
vectors for word representation. In Proceedings of the 2014 Conference on
Empirical Methods in Natural Language Processing (EMNLP), Doha, Qatar,

Hierarchical Research Fields Classification
53
pp. 1532–1543. Association for Computational Linguistics.
Piriyatamwong, P. 2022, March – September. Large-scale hierarchical classifi-
cation for scholarly publications. Master’s thesis, ETH Zurich.
Priem, J., H. Piwowar, and R. Orr. 2022. Openalex: A fully-open index of
scholarly works, authors, venues, institutions, and concepts. arXiv preprint
arXiv:2205.01833 .
Rao, S.X., P. Piriyatamwong, P. Ghoshal, S. Nasirian, E. de Salis, S. Mitrovi´c,
M. Wechner, V. Brucker, P. Egger, and C. Zhang. 2022. Keyword extraction
in scientific documents.
Rao, S.X., Y. Tu, and P.H. Egger. 2023.
Saine: Scientific annotation and
inference engine of scientific research. arXiv preprint arXiv:2302.14468 .
Rubin, T.N., A. Chambers, P. Smyth, and M. Steyvers. 2012, dec. Statistical
topic models for multi-label document classification. Mach Learn: 157–208.
https://doi.org/10.1007/s10994-011-5272-5 .
Scholar, G. 2023. Google Scholar. https://scholar.google.com/intl/en/scholar/
about.html. [Online; accessed 2023-02-07].
Scopus. 2023. Scopus. https://www.elsevier.com/solutions/scopus. [Online;
accessed 2023-02-07].
Sechidis, K., G. Tsoumakas, and I. Vlahavas. 2011. On the stratification of
multi-label data. Machine Learning and Knowledge Discovery in Databases:
145–158 .
Services, M.A. 2018. Microsoft academic graph data schema. https://docs.
microsoft.com/en-us/academic-services/graph/reference-data-schema.
Shen, Z., H. Ma, and K. Wang. 2018.
A web-scale system for scientific
knowledge exploration. arXiv preprint arXiv:1805.12216 .
Sinha, A., Z. Shen, Y. Song, H. Ma, D. Eide, B.j.P. Hsu, and K. Wang 2015. An
overview of microsoft academic service (MAS) and applications. In Proceed-
ings of the 24th international conference on world wide web, pp. 243–246.
ACM.
Sun, A. and E.P. Lim 2001. Hierarchical text classification and evaluation.
In Proceedings 2001 IEEE International Conference on Data Mining, pp.
521–528. IEEE.
Szyma´nski, P., T. Kajdanowicz, and K. Kersting. 2016. How is a data-driven
approach better than random choice in label space division for multi-label
classification? Entropy 18(8): 282 .

54
Hierarchical Research Fields Classification
Szyma´nski, P. and T. Kajdanowicz 2017. A network perspective on stratifica-
tion of multi-label data. In L. Torgo, B. Krawczyk, P. Branco, and N. Moniz
(Eds.), Proceedings of the First International Workshop on Learning with
Imbalanced Domains: Theory and Applications, Volume 74 of Proceedings of
Machine Learning Research, ECML-PKDD, Skopje, Macedonia, pp. 22–35.
PMLR.
Szyma´nski, P., C. Schulze, L. Miranda, F. Almeida, F. Benitez, W. Stachowski,
G. Ku lakowski, J.P.P. Toledano, E. Chzhen, A. Deshpande, chrysm, E. Li,
and T. Kajdanowicz. 2014.
Multi-label classification in python.
http://
scikit.ml. [Online; accessed 2022-11-22].
TensorFlow. 2022a.
Binary accuracy - tensorflow documentation.
https:
//www.tensorflow.org/api docs/python/tf/keras/metrics/BinaryAccuracy.
[Online; accessed: 2022-11-22].
TensorFlow.
2022b.
Categorical
accuracy
-
tensorflow
documenta-
tion.
https://www.tensorflow.org/api docs/python/tf/keras/metrics/
CategoricalAccuracy. [Online; accessed: 2022-11-22].
Tkachenko, M., M. Malyuk, A. Holmanyuk, and N. Liubimov. 2020-2022.
Label Studio: Data labeling software. Open source software available from
https://github.com/heartexlabs/label-studio.
Tsien, J.Z. 2007. The memory code. Scientific American 297(1): 52–59 .
US National Science Foundation (NSF) . 2018. Classification of fields of study
. https://www.nsf.gov/statistics/nsf13327/pdf/tabb1.pdf. [Online; accessed
2018-05-23].
Van Noorden, R. et al. 2015.
Interdisciplinary research by the numbers.
Nature 525(7569): 306–307 .
Vaswani, A., N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A.N. Gomez, L.u.
Kaiser, and I. Polosukhin 2017. Attention is all you need. In I. Guyon, U. V.
Luxburg, S. Bengio, H. Wallach, R. Fergus, S. Vishwanathan, and R. Gar-
nett (Eds.), Advances in Neural Information Processing Systems, Volume 30.
Curran Associates, Inc.
Wang, K., Z. Shen, C. Huang, C.H. Wu, Y. Dong, and A. Kanakia. 2020.
Microsoft academic graph: When experts are not enough.
Quantitative
Science Studies 1(1): 396–413 .
Wang, K., Z. Shen, C. Huang, C.H. Wu, D. Eide, Y. Dong, J. Qian, A. Kanakia,
A. Chen, and R. Rogahn. 2019. A review of microsoft academic services for
science of science studies. Frontiers in Big Data 2: 45. https://doi.org/10.
3389/fdata.2019.00045 .

Hierarchical Research Fields Classification
55
Web
of
Science,
C.A.P.
2023.
Web
of
Science
by
Clarivate
Ana-
lytics PLC.
http://https://clarivate.com/webofsciencegroup/solutions/
webofscience-platform. [Online; accessed 2023-02-07].
Wikipedia. 2018a.
Linguistics.
https://en.wikipedia.org/wiki/Linguistics.
[Online; accessed 2018-07-17].
Wikipedia. 2018b.
List of academic fields.
https://en.wikipedia.org/wiki/
List of academic fields. [Online; accessed 2018-07-17].
Wikipedia.
2018c.
List
of
academic
fields:
Linguistics
and
lan-
guages. https://en.wikipedia.org/wiki/List of academic fields#Linguistics
and languages. [Online; accessed 2018-07-17].
Zaharia, M., A. Chen, A. Davidson, A. Ghodsi, S.A. Hong, A. Konwinski,
S. Murching, T. Nykodym, P. Ogilvie, M. Parkhe, et al. 2018. Accelerating
the machine learning lifecycle with mlflow. IEEE Data Eng. Bull. 41(4):
39–45 .
Zhu, Y., R. Kiros, R. Zemel, R. Salakhutdinov, R. Urtasun, A. Torralba, and
S. Fidler 2015. Aligning books and movies: Towards story-like visual expla-
nations by watching movies and reading books. In 2015 IEEE International
Conference on Computer Vision (ICCV), pp. 19–27.
