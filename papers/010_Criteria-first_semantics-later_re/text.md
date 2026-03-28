# arXiv:2602.15712v1[cs.CV]17 Feb 2026

## Criteria-first, semantics-later: reproducible structure discovery in image-based sciences

#### Jan Bumberger∗ 1,2,3

- 1Helmholtz Centre for Environmental Research – UFZ, Research Data Management RDM, Permoserstraße 15, Leipzig, 04318, Germany
- 2Helmholtz Centre for Environmental Research – UFZ, Department Monitoring and Exploration Technologies, Permoserstraße 15, Leipzig, 04318, Germany


3German Centre for Integrative Biodiversity Research (iDiv) Halle-Jena-Leipzig, Puschstraße 4, Leipzig, 04103, Germany

Abstract

Across the natural and life sciences, images have become a primary measurement modality, yet the dominant analytic paradigm remains semantics-first. Structure is recovered by predicting or enforcing domain-specific labels. This paradigm fails systematically under the conditions that make image-based science most valuable, including open-ended scientific discovery, cross-sensor and cross-site comparability, and long-term monitoring in which domain ontologies and associated label sets drift culturally, institutionally, and ecologically. A deductive inversion is proposed in the form of criteria-first and semantics-later. A unified framework for criteria-first structure discovery is introduced. It separates criterion-defined, semantics-free structure extraction from downstream semantic mapping into domain ontologies or vocabularies and provides a domain-general scaffold for reproducible analysis across image-based sciences. Reproducible science requires that the first analytic layer perform criteriondriven, semantics-free structure discovery, yielding stable partitions, structural fields, or hierarchies defined by explicit optimality criteria rather than local domain ontologies. Semantics is not discarded; it is relocated downstream as an explicit mapping

∗ORCID: 0000-0003-3780-8663

from the discovered structural product to a domain ontology or vocabulary, enabling plural interpretations and explicit crosswalks without rewriting upstream extraction. Grounded in cybernetics, observation-as-distinction, and information theory’s separation of information from meaning, the argument is supported by cross-domain evidence showing that criteria-first components recur whenever labels do not scale. Finally, consequences are outlined for validation beyond class accuracy and for treating structural products as FAIR, AI-ready digital objects for long-term monitoring and digital twins.

Keywords: image segmentation, self-supervised learning, domain shift, ontology drift, criteria-first, structural products, robustness and stability, FAIR digital objects, digital twins

### 1 Why semantics-first is now the limiting assumption

Images are a primary measurement modality across the natural and life sciences, yet analysis still often defaults to a semantics-first paradigm. In this view, structure in data is characterised by mapping measurements to a predefined domain ontology, with label sets as one common special case such as classes, object types, land-cover categories, or phenotypes. This ontology-centric framing breaks down under the very conditions that make image-based science most powerful, including long-term monitoring, cross-sensor and multi-site variability, and open-ended scientific discovery. In such settings, domain ontologies and their associated label sets drift over time and between scientific communities (Kuhn, 1962; Bowker and Star, 1999). These are precisely the conditions targeted by monitoring agendas and digital-twin approaches, which require stable, comparable digitaltwin state variables over long horizons even as interpretive schemes evolve (Rossmann and Hertweck, 2022; Hazeleger et al., 2024; National Academy of Engineering and National Academies of Sciences, Engineering, and Medicine, 2024).

Nevertheless, across image-based sciences the default framing remains semantic. Measurements are used to predict a predefined domain ontology or label set, typically via supervised or weakly supervised pipelines whose success is evaluated primarily by agreement with that ontology. This orientation is increasingly visible in domain reviews, benchmarks, and segmentation pipelines, for example in remote sensing and medical imaging (Lv et al.,

2023; Xu et al., 2024). It is further reinforced by the rise of foundation models for segmentation and vision (Rodrigues et al., 2024; Zhou et al., 2024). While such models can provide impressive generic mask proposals (e.g., SAM; Kirillov et al., 2023), they are often deployed as label amplifiers. Large-scale pretraining on curated corpora and/or substantial labelled supervision for adaptation and alignment, together with prompt engineering, are used to produce stable, domain-aligned outputs. This practice amplifies ontology-centric evaluation cultures and annotation demand. At the same time, these models can also be read as pre-semantic structural extractors. They can generate mask proposals or dense feature fields (e.g., DINOv2; Oquab et al., 2024), which can instantiate candidate structural products upstream under explicit criteria.

The practical success of semantic labelling can obscure a foundational problem: semantics is not a property of the image; it is a property of a community’s interpretive scheme. Ontologies and labels are negotiated, historically contingent, and purposeoriented (Bowker and Star, 1999). In practice, land-cover ontologies differ by institution and policy regime, phenotypes and cell types are reorganised as assays change, and morphological catalogues are revised with new surveys and processing pipelines. These challenges are consequential and they obstruct three core scientific aims: (i) comparability and monitoring (long-term inference requires stability of the analytic layer even as the domain vocabulary evolves), (ii) domain shift (sensor, illumination, seasonality, or site changes), and (iii) open-ended scientific discovery (new phenomena not represented in the training label space).

Under these conditions, semantics-first pipelines quietly conflate two different operations: (i) recovering a structural product from measurement, and (ii) assigning meaning to that product by mapping it into a domain ontology. When meaning is imposed too early, upstream structure becomes hostage to particular domain ontologies, reducing transferability and undermining reproducibility. What is needed is not less theory, but a better placement for theory. Theory should enter as explicit criteria (optimality, stability, scale coherence), not as implicit labels. The proposed shift is therefore to relocate semantics downstream. A reproducible, criterion-defined structural layer can remain stable under

declared perturbations and scale changes, while multiple semantic mappings (and evolving domain ontologies) can be applied and revised without rewriting the foundational measurement-to-structure step.

Classification systems are not merely descriptive; they function as epistemic infrastructures maintained through standards, documentation, and work practices, and they drift as those practices drift (Bowker and Star, 1999). In Kuhnian terms, categories stabilise during phases of “normal science” and are periodically reorganised when anomalies accumulate (Kuhn, 1962). Semantics-first pipelines bake these contingent ontology choices into the analytic layer, turning evolving interpretive schemes into upstream constraints. A criteria-first approach does not eliminate interpretation; it decouples interpretive drift from measurement-to-structure operations by relying on a criterion-defined structural layer, so that scientific comparison remains possible even when label sets and domain ontologies evolve.

### 2 Approach: criteria-first, semantics-later

A criteria-first approach is proposed, in which analysis proceeds by making explicit criteria first and addresses semantics only in a second step (semantics later). The first analytic layer derives a structural product from raw measurements using explicit optimality criteria, yielding a semantics-free structural product (e.g., partitions, graphs, fields including scalar trait fields, or hierarchies) defined by information in the measurement stream rather than by any domain ontology. Because its construction is fully specified by declared criteria, the resulting structural product is reproducible by design and transferable across domains. This separation treats the criterion-defined structural layer as a durable digital artefact for long-term monitoring, downstream reuse, and open-ended scientific discovery.

Key principle In image-based science, reproducible analysis requires that structure precedes semantics: structure is defined as a property of the measurement stream under explicit criteria, whereas semantics is a community- and purpose-bound mapping applied downstream into a domain ontology. Criterion-driven structure discovery is therefore the

reproducible basis for interpretation, domain transfer, long-term monitoring, and openended scientific discovery.

Nevertheless, semantics-free does not mean theory-free, because every analytic procedure commits to assumptions; the difference is where and how assumptions enter. In the proposed inversion, assumptions enter upstream as explicit, inspectable criteria (e.g., stability and scale coherence; Witkin, 1984; Koenderink, 1984; Lindeberg, 2008; global optimisation objectives; Shi and Malik, 2000; trade-offs between fidelity and regularity in variational formulations; Mumford and Shah, 1989). The aim is not to remove semantics but to separate two layers: upstream, derive a structural product that is stable under declared criteria and perturbations; downstream, map that product into semantic interpretation via a domain ontology, acknowledging that this mapping is purpose- and community-dependent. Multiple semantic mappings may legitimately coexist and evolve; documenting them explicitly makes interpretive commitments auditable rather than implicit (cf. documentation practices such as datasheets; Gebru et al., 2021). Key terms are defined in Box 1, and the proposed inversion from semantics-first pipelines to criteria-first structure extraction (with semantics applied downstream) is summarised in Fig. 1.

|Box — Definitions<br><br>Semantics-first: analytic pipelines where the primary objective is mapping measurements directly to a predefined domain ontology.<br><br>Criteria-first: analytic pipelines where the primary objective is extracting a structural product under explicit optimality and stability criteria, independent of any domain ontology.<br><br>Semantics-free structural product: partitions, graphs, fields, or hierarchies defined from the measurement stream without reference to class labels or ontology terms; intended to be stable and transferable.<br><br>Downstream semantics: semantic mappings from a structural product into a domain ontology (including specific label sets), explicitly documented and purpose-bound.|
|---|


Semantics-First Pipeline

- Label-set A1: L1, L2, L3
- Label-set A2: L1, L2, L3


- Domain A specific

ontology

- Domain B specific


- Domain A image
- Domain B image


training per label-set

- Label-set B1: L1, L2, L3
- Label-set B2: L1, L2, L3


ontology

Criteria-First Pipeline

Criterion-defined reproducible structural layer

- Domain A specific

ontology

- Domain B specific


- Domain A image
- Domain B


Structure extraction under explicit criteria

Semantics-free structural product

semantic mapping

- - Robustness
- - Scale coherence
- - Compression
- - Global consistency


image

ontology

- Figure 1: The inversion. Top: a semantics-first pipeline in which a domain-specific label set determines model training (features → prediction) and yields outputs tied to a domain ontology – typically brittle under domain shift. Bottom: a criteria-first pipeline in which explicit optimality criteria define a reproducible, semantics-free structural product that can be mapped downstream to multiple domain ontologies (and evolving label sets).


### 3 From measurement to meaning

The proposed approach is not merely a pragmatic response to label scarcity. It follows from a deeper epistemic perspective’s central claim. Meaning is not an intrinsic property of an image, but an outcome of coupling between an observing system and the measured world. What can be made reproducible across observers, disciplines, and decades is therefore not the meaning of the image, but the structural product that can be extracted from the measurement stream under explicit, shareable criteria. A classical lesson from early vision aligns with a least-commitment design principle. It recommends postponing irreversible semantic commitments and instead computing stable intermediate descriptions (Marr, 1976; Marr and Hildreth, 1980).

In a cybernetic framing, measurement is communication. A sensor delivers a message about an underlying process through a channel with a transfer function and noise (Wiener, 1948; Ashby, 1956; Yuille, 2010). Image analysis then begins as decoding under constraints – recovering stable distinctions that the channel carries and that support prediction, comparison, and feedback. Crucially, those constraints need not be semantic, because they can be stated as explicit criteria such as stability under perturbations, coherence across scale, bounded complexity, or global consistency. System-theoretic accounts sharpen this boundary: observation is not passive copying but an operation of drawing distinctions; semantics is the interpretive scheme that makes distinctions communicable within a community, and that scheme is contingent and revisable (von Bertalanffy, 1968; Spencer-Brown, 1969; Maturana, 1970; Bateson, 1972; von Foerster, 1981). The methodological consequence is clear: reproducible analysis must begin with distinctions definable under explicit criteria, before any community-specific interpretive scheme is imposed.

In terms of information theory, Shannon’s classical separation of information from meaning treats communication as uncertainty reduction under constraints. This provides a principled motivation for criterion-defined structure (Shannon, 1959). From this viewpoint, many structure-extraction methods are transparent as explicit criteria: thresholding maximises a separation criterion (Otsu, 1979); scale-space formalises structure as what persists across scales (Witkin, 1984; Koenderink, 1984; Lindeberg, 2008); variational formulations trade data fidelity against boundary complexity (Mumford and Shah, 1989); and graph partitions optimise global cut objectives (Shi and Malik, 2000). These are transportable optimality principles (Flores-Fuentes et al., 2024). Across these traditions, the same principle recurs. Semantics-free does not mean theory-free. Theory should enter upstream as explicit, inspectable criteria and declared stability commitments, not as implicit semantic assumptions. This makes structure discovery reproducible and supports domain transfer. A stable, criterion-defined structural layer can be mapped to different domain ontologies across time and across communities.

### 4 Unifying framework for criterion-defined structural dis-covery

Across domains, intermediate entities differ in name and domain ontology, but the analytic pattern is the same. A measurement field is transformed into a transferable structural product under explicit criteria. To keep the argument domain-general, a minimal formal setup is used, consisting of a measurement field X, an explicit criterion C, and a criterionparameterised structure-extraction operator SC whose output is a structural product S. Consider an image-based measurement as a (possibly multi-channel) field

X : Ω → Rk, (1)

where Ω is the carrier set (pixels/voxels, points, a spatio-temporal grid, or any sampled domain) and k denotes the number of channels. In long-term monitoring, one may equivalently view X as a measurement stream indexed over time; the definitions below apply pointwise or over spatio-temporal Ω. Here, C specifies how distinctions are drawn operationally from X. C is treated as a fully specified, inspectable object (including parameters and implementation), encoding requirements such as homogeneity/contrast, boundary evidence/discontinuity, geometric consistency, topological persistence, stability under perturbations, bounded complexity/compressibility, or cross-scale coherence. Formally, C may be represented as a functional, a family of constraints, or an energy EC defined over admissible structural candidates. Given X and C, a criterion-parameterised structure-extraction operator yields the structural product

S = SC(X), (2)

where SC denotes a fully specified and inspectable structure-extraction procedure parameterised by the explicit criterion C. Its specification includes constraints, parameters, implementation details (including software version), and an executable protocol. The resulting structural product S is intended to be reproducible under declared stability commitments. Crucially, C does not prescribe a domain ontology (or label set); it specifies an operational notion of optimal structure under C. Many concrete methods implement SC

by solving a criterion-defined decision problem. Where criteria admit convex relaxations, solutions can become effectively independent of initialization, strengthening determinacy and repeatability claims (Pock et al., 2009). A common form is energy minimisation or constrained optimisation:

S ∈ arg min

EC(X, S), (3)

S ∈ Scand

where EC(X, S) is induced by C (data fidelity + regularisation, graph-cut objectives, description length, persistence/stability penalties, etc.), and Scand denotes the admissible candidate set. The approach deliberately does not fix a single structural type. Depending on modality and criterion, S takes values in different structural spaces. Here P(Ω) denotes the space of admissible partitions of Ω; G, H, and F denote admissible spaces of graphs, hierarchies, and structural fields, respectively. For example:

- • partition Π = {Ai}ni=1 of Ω, with Π ∈ P(Ω);
- • graph G = (V,E), with G ∈ G (e.g., adjacency/contact/pose graphs);
- • hierarchy H ∈ H (merge trees, dendrograms, nested partitions);
- • structural field F ∈ F (e.g., level sets, orientation/coherence fields, scalar trait fields, continuous-valued structure descriptors).


The deductive commonality is that a reproducible structural product is defined as the output of explicit criteria applied to measurement. Many structural products admit a natural ordering by refinement/coarsening. For partitions, write Π(i) ⪯ Π(j) to denote that Π(j) is coarser than Π(i) (each cell of Π(j) is a union of cells of Π(i)). A multiscale representation can then be written as a chain (or, more generally, a partially ordered family)

Π(0) ⪯ Π(1) ⪯ ··· ⪯ Π(m). (4)

Here Π(0) corresponds to the sampling induced by Ω, while subsequent levels are criteriondefined aggregations. Semantic interpretation is introduced after structure discovery as a semantic mapping from the structural product (or a chosen level of description) into a domain ontology/vocabulary:

Mi : S → Oi. (5)

Here Oi denotes a domain ontology (with a label set as a common special case). Operationally, Mi often acts on a selected level Π(j) within a multiscale family, but this choice is task- and community-dependent. Multiple mappings Mi : S → Oi may legitimately coexist for the same structural product (pluralism), reflecting different purposes, communities, or reporting regimes. This makes the key deductive point operational: reproducibility and transfer reside upstream in explicit criteria and stable structure extraction (C,SC), while domain ontologies remain downstream, purpose-bound, and revisable. Fig. 2 illustrates this separation in a minimal example.

###### Semantics-firstCriteria-firstData

###### Orginal Contrast Covariate shift Downsample

###### a1 a2 a3 a1 a2 a3 a1 a2 a1 a1 a3

- Figure 2: One image, two layers: stable structural product S = SC(X) versus brittle semantics-first labelling under shift. Columns show the original synthetic measurement field X and three perturbations: global contrast change, covariate shift in


appearance, and downsampling. Top row: X. Middle row (criteria-first): S = SC(X) under the same fixed criterion C, yielding comparable object instances/boundaries across perturbations (white outlines). Bottom row (semantics-first): labels are predicted directly from X into a fixed label set (three colour-coded labels); assignments can collapse under covariate shift or disappear under downsampling (×). In a semantics-later framing, interpretation is a revisable mapping Mi : S → Oi, so ontology drift changes Mi while S can remain comparable and structurally validated.

For a deductive reading, four postulates define the criterion-defined structural layer as a reproducibility substrate: (i) Explicitness: the criterion C is fully specified (including

parameters, software version, protocol); (ii) Determinacy: for a given (X,C), the operator SC yields a well-defined structural product S; (iii) Stability: salient properties of S are stable under a declared family of perturbations/scale changes; and (iv) Mapping pluralism: multiple semantic mappings Mi : S → Oi may legitimately coexist for the same S. These postulates place implicit “theory” where it can be inspected and transported – in C and in testable stability commitments – rather than in implicit label systems.

### 5 Cross-Domain Evidence

Across image-based sciences, semantics-first framing remains the dominant default and is widely reflected in review and benchmark cultures (Lv et al., 2023; Bom et al., 2023; Xu et al., 2024; Sun et al., 2024; Monteiro et al., 2024; Mu¨ller et al., 2024; Yan et al., 2025). Yet across multiple disciplines, a criteria-first approach reliably emerges whenever semantic labelling is scarce, unstable, contested, or prohibitively expensive. The recurring pattern is a practical separation in which a structural product S is extracted first under explicit criteria, while semantic interpretation is applied later as a purpose- and community-dependent mapping into a domain ontology/vocabulary. Table 1 summarises this correspondence in a domain-general scaffold: carrier sets Ω, typical operator/solver types realising SC, structural-product types, and recurring families of criteria C. Extended domain overviews and respective references are provided in Supplementary Note A.

### 6 Structural products as AI-ready FAIR digital objects fordigital twins

A criteria-first, semantics-later approach reshapes what counts as a result and how results should be validated. If the first analytic layer derives a structural product from measurement under explicit criteria, it yields a domain-agnostic, semantics-free structural product S that is reproducible by design and transferable across tasks and communities. This shift is not an optional add-on. It entails consequences for validation, reproducibility, monitoring under drift, and for research as well as data and data-analytic infrastructure. In particular, criterion-defined structural products can be treated as machine-actionable,

→→pixelgrain segment

→→pixelsegment

→instancecandidate

→→pixelsource/blob

→→pointsegment

→→(super)voxelcell

→→keypointlandmark

producttype TypicalcriteriafamiliesCExamplepractice

→objectcandidatefield

→phaseregiondomain

→submapglobalmap

→zone/patchregion

→→voxelsegment

→organpartorgan

→→sampleevent

→horizonunit

→pixel/voxel

sceneregion

terms

tissue

graph/hierarchy photometricSNR;coherence;

hierarchy textureregularity;grain-

planarity/curvature;robust-

tence;compressibility;robust-

cross-scaleconsistency;stabil-

boundarycoherence;deviation

geneity;scalecoherence;ro-

hierarchy geometricconsistency;local

hierarchy/field contrast;shapepriors;persis-

hierarchy signalcoherence;discontinuity;

graph/field spectralhomogeneity;hetero-

hierarchy datafidelity+smoothness;

boundaryevidence;topology;

graph) reprojectionconsistency;loop

persistence;anomaly/deviation

closure;stabilityunderdrift

fromregularity

bustness

stability

ness

ness

ity

optimisation graph(pose

levelsets partition/field/

field/partition/

partition/field/

solvertype Structural-

partition/

partition/

partition/

partition/

graph/

ing;SSLonge-

volumes coherencefilter-

ing;variational

ment;pose-graph

clustering;graph-

watershed;clus-

tering;SSL

surfaces;graph

regionadjacency;

clustering;topol-

frames bundleadjust-

ing;graphlearn-

3Dsensing pointsgeometricgroup-

SSLorganisation

ogy/persistence;

representation

criteria-driven

segmentation;

thresholding;

grid thresholding;

bioimaging voxels/pixelsmorphology;

morphology;

DomainΩOperator/

aggregation

scale-space;

Medicalimagingvoxels/slicesvariational;

graph-cut;

continuity

learning

ometry

based

Material imagingpixels/EBSD

Roboticskeypoints/

geophysics samples/

temporal

spectral

samples

pixels/

Astronomypixels/

spatio-

spatio-

grid

Earthobserva-

tion(EO)and

Pointclouds/

environmental

Microscopy/

Seismology/

monitoring

ofcriteriaC.Examplepracticetermsillustratedomainusagebutarenottheoryprimitives(EBSD=ElectronBackscatterDiffraction,SSL

Table1:Cross-domaincorrespondencebetweencarriersetsΩ,operatortypesrealisingS,structural-producttypes,andrecurringfamiliesC

=Self-supervisedlearning,SNR=Signal-to-NoiseRatio).

versioned digital objects that support FAIR practices (Wilkinson et al., 2016; Huerta et al., 2023; Soiland-Reyes et al., 2024) and provide stable digital-twin state variables for digitaltwin applications (Rossmann and Hertweck, 2022; National Academy of Engineering and National Academies of Sciences, Engineering, and Medicine, 2024).

Beyond class accuracy towards structural validation criteria If semantics is relocated downstream, validation primarily against semantic “ground truth” labels becomes untenable as a universal measure of success, especially under open-ended scientific discovery and long-term drift. Evaluation must therefore target the stability and adequacy of the structural product rather than agreement with potentially shifting label sets. A criteriafirst approach highlights five evidence classes: (i) Robustness: stability under perturbations (noise, illumination/sensor drift, seasonality, site variation); (ii) Scale coherence: consistency across resolutions and scale spaces (Witkin, 1984; Koenderink, 1984; Lindeberg, 2008); (iii) Complexity control (compressibility): preference for shorter descriptions that preserve salient regularities (Rissanen, 1978); (iv) Global optimality and consistency: solutions induced by a well-defined global criterion rather than ad hoc heuristics (Mumford and Shah, 1989; Shi and Malik, 2000); and (v) Downstream pluralism: capacity to support multiple semantic mappings on the same S without hardwiring a single domain ontology upstream. These evidence classes relocate rigor to reproducible structural adequacy and to explicit, testable stability commitments.

Reproducibility, domain transfer, and open-ended scientific discovery Criteriafirst makes reproducibility operational. Given (X,C) and a specified implementation, independent teams can reproduce the same structural product S. This also turns domain transfer into a methodological default. The same criteria-first approach can be deployed across modalities and disciplines, with semantic mappings introduced only where domain knowledge is required. For long-term monitoring, the implication is equally direct. Change detection and early warning need not require predefining all novelties as classes. A criterion-defined structural layer supports open-ended scientific discovery by characterising deviations from stable structural regimes in the measurement stream rather than by assigning observations to a fixed label set (Zhu et al., 2024; Eyring et al., 2024).

AI-ready, FAIR-by-design, and digital-twin state variables Structural products can be treated as first-class research outputs that meet infrastructural requirements. Criteria, software, and workflows should be citable, versioned, and machine-actionable. FAIR has expanded from data to research software and workflows (Barker et al., 2022; Huerta et al., 2023; Wilkinson et al., 2025), and FAIR Digital Object discussions emphasise persistent identification, consistent metadata, and defined operations for interoperable research outputs (Soiland-Reyes et al., 2024; Peters and Schindler, 2024). A criterion-defined structural product is well suited to this framing. It can be published as a versioned digital object DO = (S,metadata,provenance,version). The DO metadata should make the criterion, stability commitments, and provenance explicit. At a minimum, reporting a criteria-first structural product should include: (i) the declared criterion C (objective/constraints) and parameterisation; (ii) an implementation identifier (software version and hash) and random seed, where applicable; (iii) the declared perturbation family or scale envelope used for stability tests; (iv) structural quality metrics (e.g., boundary/partition stability as in Fig. 2); and (v) an exported stability/uncertainty envelope as part of the DO metadata. Operationally, this requires community-maintained schemas or application profiles for S and its DO metadata. It also requires declared operations and lightweight conformance checks so reuse and benchmarking remain comparable across versions and under drift. As versioned, machine-actionable artefacts, such structural products can also serve as standardised inputs or targets for representation learning and foundation-model pipelines, for example as conditioning signals or benchmark substrates. This supports reuse and monitoring under drift without collapsing S into any single domain ontology. This framing also aligns with AI-readiness approaches, which tie readiness to rigorous documentation, provenance, reliability, and FAIRness (Lawrence, 2017; Clark et al., 2024). Digital twins intensify these needs: they integrate observations, models, and AI for continuous decision support, yet domain ontologies evolve (e.g., clinical endpoints change, land-cover legends are revised, and taxonomies update) while digital-twin state variables must remain comparable over long horizons (Rossmann and Hertweck, 2022; National Academy of Engineering and National Academies of Sciences, Engineering, and Medicine, 2024; Tudor et al., 2025; Bongomin et al., 2025). A criteria-first approach therefore provides a stable, reproducible, presemantic structural product that can function as a digital twin’s durable state-variable

layer. Downstream semantics becomes an interface that can be revised or pluralised without breaking longitudinal comparability (Hazeleger et al., 2024).

### 7 Outlook and research agenda

The proposed approach implies a task-oriented research agenda that is both conceptual and practical:

- • Formalise criteria: identify families of optimality and stability criteria that are scientifically meaningful and computationally tractable across modalities.
- • Build structural benchmarks: evaluate structural products by robustness, scale coherence, compressibility, and global consistency rather than only semantic accuracy.
- • Make mappings explicit: treat interpretation as a documented semantic mapping Mi : S → Oi, enabling transparent pluralism and crosswalks across domain ontologies.
- • Use representation learning carefully: exploit SSL/foundation models as implementation families for criteria-first structure extraction, while keeping criteria explicit and testable (Fotopoulou, 2024; Li et al., 2025).
- • Standardise structural products: define schemas, versioning, uncertainty/stability envelopes, provenance, and conformance checks for semantics-free structural products as shareable scientific artefacts.
- • Separate mapping governance: treat downstream semantics (semantic mappings and their associated domain ontologies) as its own artefact class so competing mappings can coexist without rewriting upstream structure.
- • Build domain-independent tooling: develop modular, FAIR-aligned software and workflow layers for criteria-first structure extraction (Barker et al., 2022; Wilkinson et al., 2025).


Recent advances in self-supervised learning strengthen the contact point with this agenda while also making the conceptual gap visible. Fully self-supervised frameworks

can learn image representations without category labels, directly probing how much structure can be acquired without top-down domain ontologies (Konkle and Alvarez, 2022). Work on aligning machine and human vision likewise suggests that representation quality depends on how distinctions are organised across multiple abstraction levels, implying that questions of structure and level precede downstream naming (Muttenthaler et al., 2025). In label-constrained fields such as medical imaging, reviews document how self-supervised learning is increasingly used to extract transferable structural products from unlabelled data before task-specific semantic mappings are introduced (Huang et al., 2023). The claim here is not that self-supervision automatically delivers semantics-free science, but that it can be interpreted most rigorously when treated as an implementation family for explicit, criteria-first structure extraction.

### Acknowledgements and funding

This work was supported by the Helmholtz Association, Germany, and the Federal Ministry of Research, Technology and Space (BMFTR), Germany, through the Helmholtz DataHub initiative of the Research Field Earth and Environment. Helmholtz DataHub enables overarching research data management in accordance with the FAIR principles for the Earth and Environment Programme Changing Earth – Sustaining our Future.

This work contributes to the activities of NFDI4Earth and NFDI4BIOIMAGE, funded by the Deutsche Forschungsgemeinschaft (DFG; project number 460036893 for NFDI4Earth and project number 501864659 for NFDI4BIOIMAGE). NFDI4Earth and NFDI4BIOIMAGE are consortia within the National Research Data Infrastructure (NFDI) e.V. The NFDI is financed by the Federal Republic of Germany and its 16 federal states.

This research also contributes to the development of the eLTER RI cyberinfrastructure within the Horizon 2020 project eLTER PPP (grant no. 871126), eLTER PLUS (grant no. 871128), and eLTER EnRich (grant no. 101131751), funded by the European Commission.

### A Supplement: Domain overviews

Across image-based sciences, the dominant framing remains semantics-first. Analysis is organised around mapping measurements into a domain ontology or label set (Lv et al., 2023; Bom et al., 2023; Xu et al., 2024; Sun et al., 2024; Monteiro et al., 2024; Mu¨ller et al., 2024). Yet, in multiple disciplines, criteria-first components recur in practice whenever semantic labelling becomes scarce, unstable, contested, or prohibitively expensive. The recurring pattern is typically hybrid: an upstream, criterion-defined structural product S is extracted from the measurement stream under explicit criteria, while semantic interpretation remains downstream as a purpose- and community-dependent semantic mapping into a domain ontology/vocabulary. In many current workflows, reporting and benchmarking remain ontology- and label-centric even when a criteria-first sublayer is present.

How to read the sketches Each sketch highlights (i) the semantics-first default in the domain (mapping measurements to a domain ontology or label set), (ii) why this becomes limiting under long-term monitoring, domain shift, or open-ended scientific discovery, and (iii) the recurrent criteria-first sublayer(s) that produce transferable structural products (often partitions, graphs, hierarchies, or structural fields) before semantic mappings are applied. The goal is not to claim that the criteria-first inversion is already the dominant paradigm, but to make visible a cross-domain design pattern that is already widely used in components, and to motivate why treating S as a citable, versioned research artefact is a logical next step.

##### Earth observation (EO) and environmental monitoring

EO products are commonly delivered as thematic discretisations (land-cover/land-use maps, habitat layers, damage classes) whose adequacy is judged by agreement with a chosen domain ontology. In practice, segmentation is often treated as an explicit criteriondriven step that divides images into homogeneous regions, after which classification/labelling acts downstream on the segmented product (Vitti, 2012). Under long-term monitoring, semantics-first assumptions become fragile: acquisition conditions and processing chains change, and domain ontologies drift across institutions and policy regimes, mak-

ing crosswalk-only translations misleading and complicating change analysis (Yang et al., 2017). Upstream comparability is therefore often enforced by explicit criteria on the measurement stream before thematic interpretation, for example via analysis-ready measurement products and reusable spatiotemporal infrastructures such as EO data cubes (Giuliani et al., 2019). Novelty and regime shifts are then first detectable as structural deviations rather than as “new classes”, and change detection is not reducible to static label agreement (Cheng et al., 2024). Related criteria-first components include object-based image analysis and scale-sensitive landscape structure measures (McGarigal et al., 2009; Cushman et al., 2010; Blaschke et al., 2014), as well as spectral approaches to biodiversity (Rocchini et al., 2021), aligning with a recent hybrid landscape modelling framework (Lausch et al., 2026). Self-supervised and foundation-model efforts likewise learn transferable structure from large unlabelled archives (Man˜as et al., 2021). Semantic mappings remain purpose-bound, while reporting and benchmarks remain largely semantics-first; domain shift is typically handled as an add-on to label-centric pipelines rather than as an explicit validation target of the structural product itself (Tuia et al., 2016).

##### Medical imaging

Medical imaging workflows commonly centre on supervised or weakly supervised segmentation pipelines that map voxels/pixels to predefined anatomical or pathological label sets, reinforced by benchmarks that focus on agreement with expert-annotated ground truth (Ronneberger et al., 2015; Litjens et al., 2017; Xu et al., 2024). Label-centric evaluation presumes a stable medical domain ontology, yet clinical vocabularies evolve and labels are expensive, contested, and context-dependent; in addition, inter-rater variability and protocol differences mean that “ground truth” is often only conditionally well-defined, so comparability and reuse depend less on fixed labels than on reproducible extraction of stable boundaries, regions, and salient structural deviations. Classical segmentation approaches optimise explicit criteria (intensity homogeneity, edge continuity, shape priors) to derive structural products before any semantic mapping is applied (Kass et al., 1988; Pham et al., 2000), and this ordering is mirrored in practice when structural anomalies (e.g., lesion boundaries, organ contours) are identified prior to clinical interpretation. Modern workflows also increasingly use self-/weakly supervised representation learning

and foundation-style pretraining to extract transferable structure from unlabelled scans before fine-tuning to a specific label set (Zhou et al., 2019). Semantic mappings then attach diagnostic labels or ontology terms and may change as medical ontologies evolve, but in most current pipelines evaluation and reporting still privilege label agreement; intermediate structural products (e.g., boundary fields, instance partitions, uncertainty maps) are not consistently exposed, versioned, and reused as first-class research outputs.

##### Microscopy / bioimaging

In bioimaging, especially in modern high-resolution microscopy, the volume and complexity of data make exhaustive manual labelling impractical, yet a common pipeline still attempts semantic segmentation by mapping pixels or voxels to a predefined biological domain ontology (often operationalised as a label set of cell types, subcellular structures, or phenotypes) using supervised learning (Moen et al., 2019; Ragone et al., 2023). As modalities such as light-sheet and electron microscopy produce massive data volumes, semantic curation cannot keep pace with data generation; ontology terms for every cell or organelle in a volume may be undefined or too time-consuming to obtain, highlighting the scaling challenge for semantics-first approaches. Microscopy has therefore repeatedly driven criteria-first components whose primary goal is to identify coherent objects or regions without full semantic annotation: deep learning is often first used for representation learning, noise reduction, or generic feature extraction on unlabelled images (Meijering, 2020), yielding transferable structural products that support downstream interpretation. Unsupervised segmentation can partition 3D volumes into neuronal segments or organelle regions based on imaging criteria such as membrane continuity or texture (Vincent and Soille, 1991), long before each segment is mapped into a biological domain ontology; largescale connectomics underscores the same ordering, where the core bottleneck is reliable extraction of each process from dense imagery (Berning et al., 2015). Only after these structural partitions are obtained do researchers map them to neuronal identities or cell types, and semantic mappings are applied downstream, including via generalist segmentation tools (Carpenter et al., 2006; Stringer et al., 2021). Community practice and benchmarks often remain semantics-first: naming, curation, and evaluation dominate what is counted as “success”, while the structural product is treated as an intermediate step rather

than as a stable, portable research output.

##### Seismology and geophysics

There is a growing trend to apply semantic segmentation approaches to seismic data, for example using deep learning to map regions of a seismic image to a geological domain ontology (e.g., facies or rock types) based on training examples (Bergen et al., 2019; Monteiro et al., 2024). Semantics-first pipelines treat seismic interpretation as an image classification task (e.g., sandstone, shale, salt), but traditional – and in many operational workflows still – practice emphasises a different ordering: first extract key structural features from the volume, then interpret them geologically, deferring semantic mapping until after partitioning by explicit criteria. Classical workflows focus on picking horizons, discontinuities, and coherent events using signal-processing criteria (Allen, 1978); techniques such as semblance analysis, coherence measures, and edge detection identify continuous reflectors and faults based on waveform similarity or discontinuity criteria, and optimisation or threshold criteria guide extraction (e.g., high coherence indicates continuity; low coherence highlights breaks) (Col´eou et al., 2003). Modern neural pickers/detectors can likewise be used as criterion-driven extractors (Zhu and Beroza, 2018; Perol et al., 2018). The result is a structural product (e.g., reflector and fault surfaces) that can be made stable and reproducible across surveys, while only subsequently are these structures mapped into a stratigraphic or facies ontology (e.g., naming a horizon as the top of a reservoir formation) by an interpreter; many evaluation settings still benchmark progress by agreement with labelled facies maps, so the criteria-first backbone often remains implicit rather than being formalised and shared as a reusable structural product.

##### Astronomy

Astronomical surveys routinely produce label-centric catalogues with semantic annotations, mapping objects into a domain ontology (e.g., galaxy morphology) or distinguishing stars from galaxies (Bertin, E. and Arnouts, S., 1996; Lintott et al., 2008; Dieleman et al., 2015; Bom et al., 2023). At survey scale, exhaustive semantic curation cannot keep pace with the data deluge: predefined domain ontologies inevitably fall short when sources do not fit known categories or exhibit novel combinations of attributes, making astron-

omy a canonical open-ended scientific discovery setting. Accordingly, in discovery-oriented analyses astronomers increasingly use unsupervised and self-supervised methods to organise survey data and uncover latent structure without immediate reference to established classes (Cheng et al., 2021; Fotopoulou, 2024). Techniques such as clustering, manifold learning, and representation learning group sources by similarity in a data-driven way, effectively partitioning measurement space into stable regions that initially lack names; self-supervised representations can capture structural features (shapes, brightness profiles, spectral signatures) shared across many objects, and clusters and outliers then become candidates for new phenomena. These data-driven structural products are later mapped to astrophysical interpretations and, where appropriate, to new or revised ontology terms; supervised models can coexist for targeted tasks (e.g., specialised detectors trained on simulated labels) (Hezaveh et al., 2017). Flagship products and evaluation often remain label-centric, so this criteria-first layer—while central in discovery workflows—is rarely exposed as a standardised, versioned structural product.

##### Materials science

In materials imaging and analysis, researchers often begin with a semantics-first framing: segment an image into known phase regions (e.g., crystalline phases, grains) or classify features as particular defect types (Kalinin et al., 2015). Supervised learning often dominates published workflows, mapping microstructural images into a predefined materials domain ontology (often operationalised as a label set of phase labels or defect classes) (DeCost et al., 2017; Cecen et al., 2018; Mu¨ller et al., 2024). Such semantics-first pipelines assume that all relevant microstructural categories are known in advance and remain stable across imaging conditions, even though boundaries between categories can shift with microscope settings or processing pipelines and relevant phenomena may not fit a fixed label set. Materials science has long employed criteria-first methods to characterise microstructure (Bostanabad et al., 2018): microstructure segmentation often relies on explicit clustering, geometric regularisation, and morphological constraints to derive structural products such as grains, phase boundaries, or anomalous regions without immediate recourse to ontology terms (Kim et al., 2020; Mu¨ller et al., 2024; Kho et al., 2025). A common example is defect detection, where rather than assuming a universal dictionary of defect types, algorithms

can first identify discontinuities or anomalous arrangements by explicit criteria (deviation from expected periodic structure), yielding a reproducible structural product that can be analysed further. Only afterwards are regions mapped to more specific ontology terms (e.g., dislocation, void, second-phase inclusion) based on context, but in much current practice these criteria-first components are embedded within semantics-first pipelines whose reported outputs and benchmarks remain label-centric, and intermediate structural products are seldom curated and shared as reusable, versioned artefacts.

##### Point clouds and 3D sensing

In 3D scene understanding (e.g., from LiDAR, depth sensors, or multi-view reconstruction), the predominant discourse has been semantic segmentation of point clouds: points are mapped into a label set (e.g., “ground”, “building”, “vehicle”, “vegetation”), and benchmarks measure success by point-level label accuracy for a fixed ontology (Charles et al., 2017; Guo et al., 2021; Sun et al., 2024). Semantic labels in 3D data are unstable across environments and sensors: ontology terms shift across settings (e.g., “building” may not exist in natural scenes), so fixed label sets do not transfer cleanly and require frequent relabelling or adaptation. An alternative emphasis therefore targets geometric segmentation and representation learning that identify stable structural products prior to semantic mapping (Fei et al., 2023; Zeng et al., 2024). Many approaches first seek structure in the point cloud itself via geometric criteria (e.g., robust fitting and alignment) (Fischler and Bolles, 1981; Besl and McKay, 1992), grouping points into planar surfaces, geometric clusters, or consistent volumes based on proximity, normals, and multi-scale coherence; the result is a structural product, a decomposition of the point cloud into geometrically coherent parts. Semantic mappings can then attach ontology terms as needed (e.g., map a flat horizontal segment to “ground”) and can be revised across contexts without recomputing upstream segmentation, but in most published settings success is still primarily measured by semantic label accuracy, so the criteria-first layer often remains a latent backbone rather than an explicitly validated, shareable structural product.

##### Robotics

In robotics and autonomous systems, a paradigmatic criteria-first approach is simultaneous localisation and mapping (SLAM) (Mur-Artal et al., 2015; Cadena et al., 2016). Classical visual SLAM builds maps (often sparse point maps or pose graphs) by optimising geometric criteria such as reprojection consistency of features (e.g., keypoints/descriptors combined with robust estimation) (Fischler and Bolles, 1981; Lowe, 2004), minimising odometry drift, and enforcing loop-closure agreement; the result is a geometric structural product (trajectory and map) without inherent ontology terms. Semantics-first framings arise when tasks are specified as label prediction (including end-to-end semantic prediction from images to actions; Bojarski et al., 2016), or when semantic annotations are layered onto maps (“semantic SLAM”; Chen et al., 2022); these additions depend on applicationspecific ontologies and can change without altering the geometric backbone. The core SLAM process remains a criteria-first structural backbone: a criterion-defined structural product (map and trajectory) is obtained by enforcing geometric consistency constraints and integrating sensor evidence, and this structural product can be made stable and reproducible across runs and platforms when criteria and implementations are fixed. Semantic mappings can then attach ontology terms to map elements (e.g., labelling clusters as “table” or regions as “room A”) for decision-making and communication and can be revised without rerunning mapping, but in current research practice semantics is often added as a task layer on top of SLAM without turning the structural backbone into a standardised, benchmarked structural product with explicit stability envelopes.

### References

- R. V. Allen. Automatic earthquake recognition and timing from single traces. Bulletin of the Seismological Society of America, 68(5):1521–1532, 10 1978. doi: https://doi.org/ 10.1785/BSSA0680051521.


W. R. Ashby. An Introduction to Cybernetics. Chapman & Hall, London, 1956.

M. Barker, N. P. Chue Hong, D. S. Katz, A.-L. Lamprecht, C. Martinez-Ortiz, F. Psomopoulos, J. Harrow, L. J. Castro, M. Gruenpeter, P. A. Martinez, and T. Honeyman. Introducing the FAIR principles for research software. Scientific Data, 9(1):622, 2022. doi: https://doi.org/10.1038/s41597-022-01710-x.

G. Bateson. Steps to an Ecology of Mind. Chandler Publishing, San Francisco, 1972.

- K. J. Bergen, P. A. Johnson, M. V. de Hoop, and G. C. Beroza. Machine learning for data-driven discovery in solid earth geoscience. Science, 363(6433):eaau0323, 2019. doi: https://doi.org/10.1126/science.aau0323.


M. Berning, K. Boergens, and M. Helmstaedter. Segem: Efficient image analysis for highresolution connectomics. Neuron, 87(6):1193–1206, 2015. doi: https://doi.org/10.1016/ j.neuron.2015.09.003.

Bertin, E. and Arnouts, S. SExtractor: Software for source extraction. Astron. Astrophys. Suppl. Ser., 117(2):393–404, 1996. doi: https://doi.org/10.1051/aas:1996164.

P. Besl and N. D. McKay. A method for registration of 3-d shapes. IEEE Transactions on Pattern Analysis and Machine Intelligence, 14(2):239–256, 1992. doi: https://doi. org/10.1109/34.121791.

T. Blaschke, G. J. Hay, M. Kelly, S. Lang, P. Hofmann, E. Addink, R. Queiroz Feitosa,

- F. van der Meer, H. van der Werff, F. van Coillie, and D. Tiede. Geographic objectbased image analysis – towards a new paradigm. ISPRS Journal of Photogrammetry and Remote Sensing, 87:180–191, 2014. doi: https://doi.org/10.1016/j.isprsjprs.2013.09.014.


M. Bojarski, D. Del Testa, D. Dworakowski, B. Firner, B. Flepp, P. Goyal, L. D. Jackel,

M. Monfort, U. Muller, J. Zhang, X. Zhang, J. Zhao, and K. Zieba. End to end learning for self-driving cars. arXiv, 2016. doi: https://doi.org/10.48550/arXiv.1604.07316.

C. R. Bom, A. Cortesi, U. Ribeiro, L. O. Dias, K. Kelkar, A. V. Smith Castelli, L. SantanaSilva, V. Lopes-Silva, T. S. Gon¸calves, L. R. Abramo, E. V. R. Lima, F. AlmeidaFernandes, L. Espinosa, L. Li, M. L. Buzzo, C. Mendes de Oliveira, J. Sodr´e, L,

- F. Ferrari, A. Alvarez-Candal, M. Grossi, E. Telles, S. Torres-Flores, S. V. Werner, A. Kanaan, T. Ribeiro, and W. Schoenell. An extended catalogue of galaxy morphology using deep learning in southern photometric local universe survey data release

3. Monthly Notices of the Royal Astronomical Society, 528(3):4188–4208, 2023. doi: https://doi.org/10.1093/mnras/stad3956.

O. Bongomin, M. C. Mwape, N. S. Mpofu, B. K. Bahunde, R. Kidega, I. L. Mpungu, G. Tumusiime, C. A. Owino, Y. M. Goussongtogue, A. Yemane, P. Kyokunzire, C. Malanda, J. Komakech, D. Tigalana, O. Gumisiriza, and G. Ngulube. Digital twin technology advancing industry 4.0 and industry 5.0 across sectors. Results in Engineering, 26:105583, 2025. doi: https://doi.org/10.1016/j.rineng.2025.105583.

- R. Bostanabad, Y. Zhang, X. Li, T. Kearney, L. C. Brinson, D. W. Apley, W. K. Liu, and W. Chen. Computational microstructure characterization and reconstruction: Review of the state-of-the-art techniques. Progress in Materials Science, 95:1–41, 2018. doi: https://doi.org/10.1016/j.pmatsci.2018.01.005.


- G. C. Bowker and S. L. Star. Sorting Things Out: Classification and Its Consequences. MIT Press, 1999. doi: https://doi.org/10.7551/mitpress/6352.001.0001.


C. Cadena, L. Carlone, H. Carrillo, Y. Latif, D. Scaramuzza, J. Neira, I. Reid, and J. J. Leonard. Past, present, and future of simultaneous localization and mapping: Toward the robust-perception age. IEEE Transactions on Robotics, 32(6):1309–1332, 2016. doi: https://doi.org/10.1109/TRO.2016.2624754.

A. E. Carpenter, T. R. Jones, M. R. Lamprecht, C. Clarke, I. H. Kang, O. Friman, D. A. Guertin, J. H. Chang, R. A. Lindquist, J. Moffat, P. Golland, and D. M. Sabatini. Cellprofiler: image analysis software for identifying and quantifying cell phenotypes. Genome Biology, 7(10):R100, 2006. doi: https://doi.org/10.1186/gb-2006-7-10-r100.

- A. Cecen, H. Dai, Y. C. Yabansu, S. R. Kalidindi, and L. Song. Material structure-property linkages using three-dimensional convolutional neural networks. Acta Materialia, 146: 76–84, 2018. doi: https://doi.org/10.1016/j.actamat.2017.11.053.


- R. Q. Charles, H. Su, M. Kaichun, and L. J. Guibas. Pointnet: Deep learning on point sets for 3d classification and segmentation. In 2017 IEEE Conference on Computer Vision and Pattern Recognition (CVPR), pages 77–85, 2017. doi: https://doi.org/10. 1109/CVPR.2017.16.

W. Chen, G. Shang, A. Ji, C. Zhou, X. Wang, C. Xu, Z. Li, and K. Hu. An overview on visual slam: From tradition to semantic. Remote Sensing, 14(13), 2022. doi: https: //doi.org/10.3390/rs14133010.

G. Cheng, Y. Huang, X. Li, S. Lyu, Z. Xu, H. Zhao, Q. Zhao, and S. Xiang. Change detection methods for remote sensing in the last decade: A comprehensive review. Remote Sensing, 16(13), 2024. doi: https://doi.org/10.3390/rs16132355.

T.-Y. Cheng, M. Huertas-Company, C. J. Conselice, A. Arag´n-Salamanca, B. E. Robertson, and N. Ramachandra. Beyond the hubble sequence – exploring galaxy morphology with unsupervised machine learning. Monthly Notices of the Royal Astronomical Society, 503(3):4446–4465, 2021. doi: https://doi.org/10.1093/mnras/stab734.

T. Clark, H. Caufield, J. A. Parker, S. Al Manir, E. Amorim, J. Eddy, N. Gim, B. Gow, W. Goar, M. Haendel, J. N. Hansen, N. Harris, H. Hermjakob, M. Joachimiak, G. Jordan, I.-H. Lee, S. K. McWeeney, C. Nebeker, M. Nikolov, J. Shaffer, N. Sheffield,

- G. Sheynkman, J. Stevenson, J. Y. Chen, C. Mungall, A. Wagner, S. W. Kong, S. S. Ghosh, B. Patel, A. Williams, M. C. Munoz-Torres, and the Bridge to Artificial Intelligence (Bridge2AI) Consortium members. Ai-readiness for biomedical data: Bridge2ai recommendations. bioRxiv, 2024. doi: https://doi.org/10.1101/2024.10.23.619844.


T. Col´eou, M. Poupon, and K. Azbel. Unsupervised seismic facies classification: A review and comparison of techniques and implementation. The Leading Edge, 22(10):942–953,

2003. doi: https://doi.org/10.1190/1.1623635.

- S. A. Cushman, K. Gutzweiler, J. S. Evans, and K. McGarigal. The Gradient Paradigm:


- A Conceptual and Analytical Framework for Landscape Ecology, pages 83–108. Springer, Tokyo, 2010. doi: https://doi.org/10.1007/978-4-431-87771-4 5.

- B. L. DeCost, T. Francis, and E. A. Holm. Exploring the microstructure manifold: Image texture representations applied to ultrahigh carbon steel microstructures. Acta Materialia, 133:30–40, 2017. doi: https://doi.org/10.1016/j.actamat.2017.05.014.


- S. Dieleman, K. W. Willett, and J. Dambre. Rotation-invariant convolutional neural networks for galaxy morphology prediction. Monthly Notices of the Royal Astronomical Society, 450(2):1441–1459, 2015. doi: https://doi.org/10.1093/mnras/stv632.


- V. Eyring, P. Gentine, G. Camps-Valls, D. M. Lawrence, and M. Reichstein. Ai-empowered next-generation multiscale climate modelling for mitigation and adaptation. Nature Geoscience, 17(10):963–971, 2024. doi: https://doi.org/10.1038/s41561-024-01527-w.

B. Fei, W. Yang, L. Liu, T. Luo, R. Zhang, Y. Li, and Y. He. Self-supervised learning for pre-training 3d point clouds: A survey. arXiv, 2023. doi: https://doi.org/10.48550/arXiv.2305.04691.

M. A. Fischler and R. C. Bolles. Random sample consensus: a paradigm for model fitting with applications to image analysis and automated cartography. Commun. ACM, 24

(6):381–395, 1981. doi: https://doi.org/10.1145/358669.358692.

- W. Flores-Fuentes, O. Sergiyenko, J. C. Rodrı´guez-Quin˜onez, and J. E. Miranda-Vega. Application of information theory to computer vision and image processing. Entropy, 26(2), 2024. doi: https://doi.org/10.3390/e26020114.


- S. Fotopoulou. A review of unsupervised learning in astronomy. Astronomy and Computing, 48:100851, 2024. doi: https://doi.org/10.1016/j.ascom.2024.100851.
- T. Gebru, J. Morgenstern, B. Vecchione, J. W. Vaughan, H. Wallach, H. D. III, and


- K. Crawford. Datasheets for datasets. Commun. ACM, 64(12):86–92, 2021. doi: https: //doi.org/10.1145/3458723.


- G. Giuliani, J. Mas´, P. Mazzetti, S. Nativi, and A. Zabala. Paving the way to increased interoperability of earth observations data cubes. Data, 4(3), 2019. doi: https://doi. org/10.3390/data4030113.


- Y. Guo, H. Wang, Q. Hu, H. Liu, L. Liu, and M. Bennamoun. Deep learning for 3d point clouds: A survey. IEEE Transactions on Pattern Analysis and Machine Intelligence, 43


(12):4338–4364, 2021. doi: https://doi.org/10.1109/TPAMI.2020.3005434.

W. Hazeleger, J. P. M. Aerts, P. Bauer, M. F. P. Bierkens, G. Camps-Valls, M. M. Dekker,

- F. J. Doblas-Reyes, V. Eyring, C. Finkenauer, A. Grundner, S. Hachinger, D. M. Hall, T. Hartmann, F. Iglesias-Suarez, M. Janssens, E. R. Jones, T. K¨lling, M. Lees, S. Lhermitte, R. V. van Nieuwpoort, A.-K. Pahker, O. J. Pellicer-Valero, F. P. Pijpers, A. Siibak, J. Spitzer, B. Stevens, V. V. Vasconcelos, and F. C. Vossepoel. Digital twins of the earth with and for humans. Communications Earth & Environment, 5(1):463, 2024. doi: https://doi.org/10.1038/s43247-024-01626-x.


- Y. D. Hezaveh, L. P. Levasseur, and P. J. Marshall. Fast automated analysis of strong gravitational lenses with convolutional neural networks. Nature, 548(7669):555–557,


2017. doi: https://doi.org/10.1038/nature23463.

- S.-C. Huang, A. Pareek, M. Jensen, M. P. Lungren, S. Yeung, and A. S. Chaudhari. Self-supervised learning for medical image classification: a systematic review and implementation guidelines. npj Digital Medicine, 6(1):74, 2023. doi: https: //doi.org/10.1038/s41746-023-00811-0.


E. A. Huerta, B. Blaiszik, L. C. Brinson, K. E. Bouchard, D. Diaz, C. Doglioni, J. M. Duarte, M. Emani, I. Foster, G. Fox, P. Harris, L. Heinrich, S. Jha, D. S. Katz, V. Kindratenko, C. R. Kirkpatrick, K. Lassila-Perini, R. K. Madduri, M. S. Neubauer, F. E. Psomopoulos, A. Roy, O. Ru¨bel, Z. Zhao, and R. Zhu. FAIR for AI: An interdisciplinary and international community building perspective. Scientific Data, 10(1):487, 2023. doi: https://doi.org/10.1038/s41597-023-02298-6.

- S. V. Kalinin, B. G. Sumpter, and R. K. Archibald. Big–deep–smart data in imaging for guiding materials design. Nature Materials, 14(10):973–980, 2015. doi: https://doi.org/ 10.1038/nmat4395.


- M. Kass, A. Witkin, and D. Terzopoulos. Snakes: Active contour models. International Journal of Computer Vision, 1(4):321–331, 1988. doi: https://doi.org/10.1007/ BF00133570.


- Z. Kho, A. Bridger, K. Butler, E. C. Duran, M. Danaie, and A. S. Eggeman. On the use of clustering workflows for automated microstructure segmentation of analytical stem datasets. APL Materials, 13(1):010901, 2025. doi: https://doi.org/10.1063/5.0246329.


- H. Kim, J. Inoue, and T. Kasuya. Unsupervised microstructure segmentation by mimicking metallurgists’ approach to pattern recognition. Scientific Reports, 10(1):17835, 2020. doi: https://doi.org/10.1038/s41598-020-74935-8.


A. Kirillov, E. Mintun, N. Ravi, H. Mao, C. Rolland, L. Gustafson, T. Xiao, S. Whitehead, A. C. Berg, W.-Y. Lo, P. Doll´r, and R. Girshick. Segment anything. arXiv, 2023. doi: https://doi.org/10.48550/arXiv.2304.02643.

J. J. Koenderink. The structure of images. Biological Cybernetics, 50(5):363–370, 1984. doi: https://doi.org/10.1007/BF00336961.

- T. Konkle and G. A. Alvarez. A self-supervised domain-general learning framework for human ventral stream representation. Nature Communications, 13(1):491, 2022. doi: https://doi.org/10.1038/s41467-022-28091-4.


- T. S. Kuhn. The Structure of Scientific Revolutions. University of Chicago Press, 1962.


- A. Lausch, P. Selsam, and J. Bumberger. Conceptual framework for hybrid landscape modelling: The pixel–zone–object approach and its theoretical foundations. Ecological Indicators, 183:114679, 2026. doi: https://doi.org/10.1016/j.ecolind.2026.114679.


- N. D. Lawrence. Data readiness levels. arXiv, 2017. doi: https://doi.org/10.48550/arXiv.1705.02245.


- Z. Li, Y. Yan, X. Wang, Y. Ge, and L. Meng. A survey of deep learning for industrial visual anomaly detection. Artificial Intelligence Review, 58(9):279, 2025. doi: https: //doi.org/10.1007/s10462-025-11287-7.


- T. Lindeberg. Scale-Space, pages 2495–2504. John Wiley & Sons, Ltd, 2008. ISBN


9780470050118. doi: https://doi.org/10.1002/9780470050118.ecse609.

- C. J. Lintott, K. Schawinski, A. Slosar, K. Land, S. Bamford, D. Thomas, M. J. Raddick, R. C. Nichol, A. Szalay, D. Andreescu, P. Murray, and J. Vandenberg. Galaxy zoo:


morphologies derived from visual inspection of galaxies from the sloan digital sky survey. Monthly Notices of the Royal Astronomical Society, 389(3):1179–1189, 2008. doi: https: //doi.org/10.1111/j.1365-2966.2008.13689.x.

- G. Litjens, T. Kooi, B. E. Bejnordi, A. A. A. Setio, F. Ciompi, M. Ghafoorian, J. A. van der Laak, B. van Ginneken, and C. I. S´nchez. A survey on deep learning in medical image analysis. Medical Image Analysis, 42:60–88, 2017. doi: https://doi.org/10.1016/ j.media.2017.07.005.

D. G. Lowe. Distinctive image features from scale-invariant keypoints. International Journal of Computer Vision, 60(2):91–110, 2004. doi: https://doi.org/10.1023/B:VISI. 0000029664.99615.94.

- J. Lv, Q. Shen, M. Lv, Y. Li, L. Shi, and P. Zhang. Deep learning-based semantic segmentation of remote sensing images: a review. Frontiers in Ecology and Evolution, 11, 2023. doi: https://doi.org/10.3389/fevo.2023.1201125.

- D. Marr. Early processing of visual information. Philosophical Transactions of the Royal Society of London. Series B, Biological Sciences, 275(942):483–519, 1976. doi: https: //doi.org/10.1098/rstb.1976.0090.


- D. Marr and E. Hildreth. Theory of edge detection. Proceedings of the Royal Society of London. B. Biological Sciences, 207(1167):187–217, 1980. doi: https://doi.org/10.1098/ rspb.1980.0020.


H. R. Maturana. Biology of cognition. Research Report BCL 9.0, Biological Computer Laboratory, University of Illinois at Urbana-Champaign, 1970.

O. Man˜as, A. Lacoste, X. Gir´-i Nieto, D. Vazquez, and P. Rodr´ıguez. Seasonal contrast: Unsupervised pre-training from uncurated remote sensing data. In 2021 IEEE/CVF International Conference on Computer Vision (ICCV), pages 9394–9403, 2021. doi: https://doi.org/10.1109/ICCV48922.2021.00928.

- K. McGarigal, S. Tagil, and S. A. Cushman. Surface metrics: an alternative to patch metrics for the quantification of landscape structure. Landscape Ecology, 24(3):433–450,




2009. doi: https://doi.org/10.1007/s10980-009-9327-y.

- E. Meijering. A bird’s-eye view of deep learning in bioimage analysis. Computational and Structural Biotechnology Journal, 18:2312–2325, 2020. doi: https://doi.org/10.1016/j. csbj.2020.08.003.


- E. Moen, D. Bannon, T. Kudo, W. Graf, M. Covert, and D. Van Valen. Deep learning for cellular image analysis. Nature Methods, 16(12):1233–1246, 2019. doi: https://doi.org/ 10.1038/s41592-019-0403-1.


- B. A. Monteiro, G. L. Cangu¸cu, L. M. Jorge, R. H. Vareto, B. S. Oliveira, T. H. Silva, L. A. Lima, A. M. Machado, W. R. Schwartz, and P. O. V. de Melo. Literature review on deep learning for the segmentation of seismic images. Earth-Science Reviews, 258: 104955, 2024. doi: https://doi.org/10.1016/j.earscirev.2024.104955.


D. Mumford and J. Shah. Optimal approximations by piecewise smooth functions and associated variational problems. Communications on Pure and Applied Mathematics, 42(5):577–685, 1989. doi: https://doi.org/10.1002/cpa.3160420503.

- R. Mur-Artal, J. M. M. Montiel, and J. D. Tard´s. Orb-slam: A versatile and accurate monocular slam system. IEEE Transactions on Robotics, 31(5):1147–1163, 2015. doi: https://doi.org/10.1109/TRO.2015.2463671.


- L. Muttenthaler, K. Greff, F. Born, B. Spitzer, S. Kornblith, M. C. Mozer, K.-R. Mu¨ller, T. Unterthiner, and A. K. Lampinen. Aligning machine and human visual representations across abstraction levels. Nature, 647(8089):349–355, 2025. doi: https://doi.org/10.1038/s41586-025-09631-6.
- M. Mu¨ller, M. Stiefel, B.-I. Bachmann, D. Britz, and F. Mu¨cklich. Overview: Machine learning for segmentation and classification of complex steel microstructures. Metals, 14(5), 2024. doi: https://doi.org/10.3390/met14050553.


National Academy of Engineering and National Academies of Sciences, Engineering, and Medicine. Foundational Research Gaps and Future Directions for Digital Twins. The National Academies Press, Washington, DC, 2024. doi: https://doi.org/10.17226/26894.

- M. Oquab, T. Darcet, T. Moutakanni, H. Vo, M. Szafraniec, V. Khalidov, P. Fernandez, D. Haziza, F. Massa, A. El-Nouby, M. Assran, N. Ballas, W. Galuba,


- R. Howes, P.-Y. Huang, S.-W. Li, I. Misra, M. Rabbat, V. Sharma, G. Synnaeve, H. Xu, H. Jegou, J. Mairal, P. Labatut, A. Joulin, and P. Bojanowski. Dinov2: Learning robust visual features without supervision. arXiv, 2024. doi: https://doi.org/10.48550/arXiv.2304.07193.


- N. Otsu. A threshold selection method from gray-level histograms. IEEE Transactions on Systems, Man, and Cybernetics, 9(1):62–66, 1979. doi: https://doi.org/10.1109/TSMC. 1979.4310076.


- T. Perol, M. Gharbi, and M. Denolle. Convolutional neural network for earthquake detection and location. Science Advances, 4(2):e1700578, 2018. doi: https://doi.org/10. 1126/sciadv.1700578.


D. Peters and S. Schindler. FAIR for digital twins. CEAS Space Journal, 16:367–374,

2024. doi: https://doi.org/10.1007/s12567-023-00506-y.

D. L. Pham, C. Xu, and J. L. Prince. Current methods in medical image segmentation. Annual Review of Biomedical Engineering, 2:315–337, 2000. doi: https://doi.org/10. 1146/annurev.bioeng.2.1.315.

T. Pock, D. Cremers, H. Bischof, and A. Chambolle. An algorithm for minimizing the mumford-shah functional. In 2009 IEEE 12th International Conference on Computer Vision, pages 1133–1140, 2009. doi: https://doi.org/10.1109/ICCV.2009.5459348.

M. Ragone, R. Shahabazian-Yassar, F. Mashayek, and V. Yurkiv. Deep learning modeling in microscopy imaging: A review of materials science applications. Progress in Materials Science, 138:101165, 2023. doi: https://doi.org/10.1016/j.pmatsci.2023.101165.

J. Rissanen. Modeling by shortest data description. Automatica, 14(5):465–471, 1978. doi: https://doi.org/10.1016/0005-1098(78)90005-5.

D. Rocchini, N. Salvatori, C. Beierkuhnlein, A. Chiarucci, F. de Boissieu, M. F¨rster, C. X. Garzon-Lopez, T. W. Gillespie, H. C. Hauffe, K. S. He, B. Kleinschmit, J. Lenoir,

- M. Malavasi, V. Moudry´, H. Nagendra, D. Payne, P. Sı´mov´,ˇ M. Torresani, M. Wegmann, and J.-B. F´eret. From local spectral species to global spectral communities: A


benchmark for ecosystem diversity estimate by remote sensing. Ecological Informatics, 61:101195, 2021. doi: https://doi.org/10.1016/j.ecoinf.2020.101195.

- C. N. Rodrigues, I. M. Nunes, M. B. Pereira, H. Oliveira, and J. A. dos Santos. From superpixels to foundational models: An overview of unsupervised and generalizable image segmentation. Comput. Graph., 123(C), 2024. doi: https://doi.org/10.1016/j. cag.2024.104014.


- O. Ronneberger, P. Fischer, and T. Brox. U-net: Convolutional networks for biomedical image segmentation. In N. Navab, J. Hornegger, W. M. Wells, and A. F. Frangi, editors, Medical Image Computing and Computer-Assisted Intervention – MICCAI 2015, pages 234–241, Cham, 2015. Springer International Publishing. doi: https://doi.org/10.1007/ 978-3-319-24574-4 28.


- A. Rossmann and D. Hertweck. Digital twins: A meta-review on their conceptualization, application, and reference architecture. In Proceedings of the 55th Hawaii International Conference on System Sciences (HICSS-55), pages 4518–4527, 2022. doi: https://doi. org/10.24251/HICSS.2022.550.


- C. E. Shannon. Coding Theorems for a Discrete Source With a Fidelity Criterion, volume 7, pages 325–350. Institute of Radio Engineers, International Convention Record,


1959. doi: https://doi.org/10.1109/9780470544242.ch21.

J. Shi and J. Malik. Normalized cuts and image segmentation. IEEE Transactions on Pattern Analysis and Machine Intelligence, 22(8):888–905, 2000. doi: https://doi.org/ 10.1109/34.868688.

- S. Soiland-Reyes, C. Goble, and P. Groth. Evaluating FAIR digital object and linked data as distributed object systems. PeerJ Computer Science, 10:e1781, 2024. doi: https://doi.org/10.7717/peerj-cs.1781.


- G. Spencer-Brown. Laws of Form. George Allen & Unwin, London, 1969.


C. Stringer, T. Wang, M. Michaelos, and M. Pachitariu. Cellpose: a generalist algorithm for cellular segmentation. Nature Methods, 18(1):100–106, 2021. doi: https://doi.org/ 10.1038/s41592-020-01018-x.

Y. Sun, X. Zhang, and Y. Miao. A review of point cloud segmentation for understanding 3D indoor scenes. Visual Intelligence, 2(1):14, 2024. doi: https://doi.org/10.1007/ s44267-024-00046-x.

- B. H. Tudor, R. Shargo, G. M. Gray, J. L. Fierstein, F. H. Kuo, R. Burton, J. T. Johnson, B. B. Scully, A. Asante-Korang, M. A. Rehman, and L. M. Ahumada. A scoping review of human digital twins in healthcare applications and usage patterns. npj Digital Medicine, 8(1):587, 2025. doi: https://doi.org/10.1038/s41746-025-01910-w.


- D. Tuia, C. Persello, and L. Bruzzone. Domain adaptation for the classification of remote sensing data: An overview of recent advances. IEEE Geoscience and Remote Sensing Magazine, 4(2):41–57, 2016. doi: https://doi.org/10.1109/MGRS.2016.2548504.


- L. Vincent and P. Soille. Watersheds in digital spaces: an efficient algorithm based on immersion simulations. IEEE Transactions on Pattern Analysis and Machine Intelligence, 13(6):583–598, 1991. doi: https://doi.org/10.1109/34.87344.


A. Vitti. The mumford–shah variational model for image segmentation: An overview of the theory, implementation and use. ISPRS Journal of Photogrammetry and Remote Sensing, 69:50–64, 2012. doi: https://doi.org/10.1016/j.isprsjprs.2012.02.005.

- L. von Bertalanffy. General System Theory: Foundations, Development, Applications. George Braziller, New York, 1968.

- H. von Foerster. Observing Systems. Intersystems Publications, 1981.


- N. Wiener. Cybernetics or Control and Communication in the Animal and the Machine. MIT Press, 1948. doi: https://doi.org/10.7551/mitpress/11810.001.0001.


- M. D. Wilkinson, M. Dumontier, I. J. Aalbersberg, G. Appleton, M. Axton, A. Baak,
- N. Blomberg, J.-W. Boiten, L. B. da Silva Santos, P. E. Bourne, J. Bouwman, A. J. Brookes, T. Clark, M. Crosas, I. Dillo, O. Dumon, S. Edmunds, C. T. Evelo, R. Finkers,


- A. Gonzalez-Beltran, A. J. G. Gray, P. Groth, C. Goble, J. S. Grethe, J. Heringa, P. A. C. ’t Hoen, R. Hooft, T. Kuhn, R. Kok, J. Kok, S. J. Lusher, M. E. Martone, A. Mons, A. L. Packer, B. Persson, P. Rocca-Serra, M. Roos, R. van Schaik, S.-A. Sansone, E. Schultes, T. Sengstag, T. Slater, G. Strawn, M. A. Swertz, M. Thompson, J. van der Lei, E. van


- Mulligen, J. Velterop, A. Waagmeester, P. Wittenburg, K. Wolstencroft, J. Zhao, and
- B. Mons. The FAIR guiding principles for scientific data management and stewardship. Scientific Data, 3(1):160018, 2016. doi: https://doi.org/10.1038/sdata.2016.18.

S. R. Wilkinson, M. Aloqalaa, K. Belhajjame, M. R. Crusoe, B. de Paula Kinoshita, L. Gadelha, D. Garijo, O. J. R. Gustafsson, N. Juty, S. Kanwal, F. Z. Khan, J. K¨ster, K. Peters-von Gehlen, L. Pouchard, R. K. Rannow, S. Soiland-Reyes, N. Soranzo, S. Sufi, Z. Sun, B. Vilne, M. A. Wouters, D. Yuen, and C. Goble. Applying the FAIR principles to computational workflows. Scientific Data, 12(1):328, 2025. doi: https://doi.org/10. 1038/s41597-025-04451-9.

A. Witkin. Scale-space filtering: A new approach to multi-scale description. In ICASSP ’84. IEEE International Conference on Acoustics, Speech, and Signal Processing, volume 9, pages 150–153, 1984. doi: https://doi.org/10.1109/ICASSP.1984.1172729.

Y. Xu, R. Quan, W. Xu, Y. Huang, X. Chen, and F. Liu. Advances in medical image segmentation: A comprehensive review of traditional, deep learning and hybrid approaches. Bioengineering, 11(10), 2024. doi: https://doi.org/10.3390/bioengineering11101034.

H. Yan, A. Lau, and H. Fan. Evaluating deep learning advances for point cloud semantic segmentation in urban environments. Journal of Cartography and Geographic Information, 75(1):3–22, Mar. 2025. doi: https://doi.org/10.1007/s42489-025-00185-1.

H. Yang, S. Li, J. Chen, X. Zhang, and S. Xu. The standardization and harmonization of land cover classification systems towards harmonized datasets: A review. ISPRS International Journal of Geo-Information, 6(5), 2017. doi: https://doi.org/10.3390/ ijgi6050154.

A. Yuille. An information theory perspective on computational vision. Frontiers of Electrical and Electronic Engineering in China, 5(3):329–346, 2010. doi: https://doi.org/ 10.1007/s11460-010-0107-x.

- C. Zeng, W. Wang, A. Nguyen, J. Xiao, and Y. Yue. Self-supervised learning for point cloud data: A survey. Expert Systems with Applications, 237:121354, 2024. doi: https: //doi.org/10.1016/j.eswa.2023.121354.


- T. Zhou, W. Xia, F. Zhang, B. Chang, W. Wang, Y. Yuan, E. Konukoglu, and D. Cremers. Image segmentation in foundation model era: A survey. arXiv, 2024. doi: https://doi.org/10.48550/arXiv.2408.12957.


Z. Zhou, V. Sodha, M. M. Rahman Siddiquee, R. Feng, N. Tajbakhsh, M. B. Gotway, and J. Liang. Models genesis: Generic autodidactic models for 3D medical image analysis. In D. Shen, T. Liu, T. M. Peters, L. H. Staib, C. Essert, S. Zhou, P.-T. Yap, and A. Khan, editors, Medical Image Computing and Computer Assisted Intervention – MICCAI 2019, pages 384–393, Cham, 2019. Springer International Publishing. doi: https://doi.org/10.1007/978-3-030-32251-9 42.

- F. Zhu, S. Ma, Z. Cheng, X.-Y. Zhang, Z. Zhang, D. Tao, and C.-L. Liu. Open-world machine learning: A review and new outlooks. arXiv, 2024. doi: https://doi.org/10.48550/arXiv.2403.01759.


W. Zhu and G. C. Beroza. Phasenet: a deep-neural-network-based seismic arrival-time picking method. Geophysical Journal International, 216(1):261–273, 2018. doi: https: //doi.org/10.1093/gji/ggy423.

