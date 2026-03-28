# arXiv:2408.10689v1[cs.AI]20 Aug 2024

## Genesis: Towards the Automation of Systems Biology Research

Ievgeniia A. Tiukova1,2 , Daniel Brunnsa˚ker1 , Erik Y. Bjurstr¨m1 , Alexander H. Gower1 , Filip Kronstr¨m1 , Gabriel K. Reder3 , Ronald S. Reiserer4 , Konstantin

Korovin5 , Larisa B. Soldatova6 , John P. Wikswo4 , and Ross D. King1,3

- 1 Chalmers University of Technology, Gothenburg, Sweden

{tiukova,danbru,erikbju,gower,filipkro,rossk}@chalmers.se

- 2 KTH Royal Institute of Technology, Stockholm, Sweden


3 University of Cambridge, Cambridge, United Kingdom gr513@cam.ac.uk 4 Vanderbilt University, Nashville, TN, USA {ron.reiserer,john.p.wikswo}@vanderbilt.edu 5 The University of Manchester, Manchester, United Kingdom konstantin.korovin@manchester.ac.uk 6 Goldsmiths, University of London, London, United Kingdom l.soldatova@gold.ac.uk

Abstract. The cutting edge of applying AI to science is the closed-loop automation of scientific research: robot scientists. We have previously developed two robot scientists: ‘Adam’ (for yeast functional biology), and ‘Eve’ (for early-stage drug design)). We are now developing a next generation robot scientist Genesis. With Genesis we aim to demonstrate that an area of science can be investigated using robot scientists unambiguously faster, and at lower cost, than with human scientists. Here we report progress on the Genesis project. Genesis is designed to automatically improve system biology models with thousands of interacting causal components. When complete Genesis will be able to initiate and execute in parallel one thousand hypothesis-led closed-loop cycles of experiment per-day. Here we describe the core Genesis hardware: the one thousand computer-controlled µbioreactors. For the integrated Mass Spectrometry platform we have developed AutonoMS, a system to automatically run, process, and analyse high-throughput experiments. We have also developed Genesis-DB, a database system designed to enable software agents access to large quantities of structured domain information. We have developed RIMBO (Revisions for Improvements of Models in Biology Ontology) to describe the planned hundreds of thousands of changes to the models. We have demonstrated the utility of this infrastructure by developed two relational learning bioinformatic projects. Finally, we describe LGEM+ a relational learning system for the automated abductive improvement of genome-scale metabolic models.

Keywords: Robot Scientist · Automating Science · Closed-loop Automation.

#### 1 Background

##### 1.1 Automating Science

The most advanced application of AI for science is the closed-loop automation of scientific research. Such systems are called ‘Robot Scientists’, ‘AI Scientists’, ‘Self-driving Labs’, etc. A Robot Scientist autonomously originates hypotheses to explain observations, devise

experiments to test these hypotheses, physically runs the experiments using laboratory robotics, interprets the results to change the probability of hypotheses, and then repeats the cycle [1, 2]. The automation of science has the potential to revolutionise the efficiency of scientific research [3, 4, 5].

We have previously developed two Robot Scientists, ‘Adam’, and ‘Eve’. Adam was the first machine to autonomously discover novel scientific knowledge [2]. Adam investigated the functional genomics of the yeast S. cerevisiae, and discovered the function of locally orphan enzymes. Our second Robot Scientist, Eve, was designed for early-stage drug development [6]. Using econometric modelling we demonstrated that Eve’s use of AI to select compounds outperformed standard drug screening. Eve’s most significant discovery is that triclosan (an anti-microbial compound commonly used in toothpastes, etc.) is an inhibitor of wild-type and drug-resistant dihydrofolate reductase in the malaria-causing parasites P. falciparum and P. vixax [6, 7, 8]. Eve’s approach for closed-loop optimisation has been widely copied by the pharmaceutical industry and in materials science.

##### 1.2 Eukaryotic System Biology

One of the most challenging tasks in modern science is the development of systems biology models of eukaryotic cells. These models are central to the future of medicine (humans are eukaryotes), to agriculture (plants are also eukaryotes), and to biotechnology. The yeast S. cerevisiae is the ‘model organism’ for eukaryotic cells: despite the last common ancestor of humans and yeast living around one billion years ago, most of what is true about yeast is also true for human cells. The medicine Nobel Laureate Leland Hartwell famously said ‘yeast are like small humans’. The similarities between yeast and humans mean that often the easiest way to understand how a human gene works is to study its homolog in yeast, as yeast is much easier to work with.

Even simple model biological system like yeast are incredibly complicated: thousands of genes, proteins, and small-molecules, all interacting together in complicated spatial temporal ways. In addition, Ockham’s razor is not a reliable guide in biology, as biological systems evolved over long time periods. Therefore, basic information theory makes clear that a vast number of experiments will be required to derive an understanding of biological systems. Current high-throughput methods are insufficient for systems biology. This is because, even though very large numbers of experiments may be executed, each individual experiment cannot be designed to test a hypothesis about a model, i.e. current highthroughput experiments are not ‘hypothesis led’.

Systems biology presents an extreme challenge to the traditional human based scientific method. Systems biology models are so complex that they are beyond human intuitive understanding. This complexity plays to the strength of AI. Complex modelling is also complicated by what is known in the philosophy of science as ‘Duhem Thesis’: ‘an experiment ... can never condemn an isolated hypothesis but only a whole theoretical Group’ [9]. This makes model refinement and the generation of efficient experiments to test models especially challenging [10]. We argue that AI systems are now better than humans at this. Due to these, and other challenges of systems biology, AI tools are required to aid the execution of the many closed-loop experimental cycles essential to build accurate and comprehensive 21st century system biology models.

As a proof-of-principle example of the automation of systems biology, we previously chose the diauxic shift in the yeast S. cerevisiae [11]. We automatically developed a model that outperformed the best previous models, and added 92 genes (+45%), and 1,048 interactions (+147%) [11]. The resulting improved model is relevant to understanding cancer, the immune system, and aging.

#### 2 Results

The overall architecture of Genesis is shown in Fig. 1. With Genesis we aim to demonstrate that an area of science can be investigated unambiguously faster, and at lower cost, using robot scientists than with human scientists. Specifically, we aim to demonstrate a hundredfold cost-benefit for Genesis over a standard human scientist in a standard lab.

Genesis is designed to automatically improve a more complicated scientific model than any previous system has attempted. The model that Genesis works with has thousands of interacting causal (mechanical) components related by tens of thousands of parameters. This contrasts sharply with all other closed-loop automated systems that we are aware of, which focus on simple input/output black-box optimisation.

Genesis is specifically designed to automate systems biology research. Genesis will be designed to be able to initiate and execute in parallel one thousand hypothesis-led closedloop cycles of experiment per-day. Each closed-loop cycle will consist of hypothesis formation, experiment planning, laboratory execution, and results interpretation.

||![image 1](Tiukova et al._2024_Genesis Towards the Automation of Systems Biology Research_images/imageFile1.png)|
|---|
<br><br>![image 2](Tiukova et al._2024_Genesis Towards the Automation of Systems Biology Research_images/imageFile2.png)<br><br>Hardware Software<br><br>|Ontologies: Experiment conditions Experiment results System models|
|---|
<br><br>|1,000 Bioreactors|
|---|
<br><br>RDF Knowledge Base<br><br>10,000 state measurements a day AI - modules<br><br>|Agents: genes, proteins, Metabolites (1000s). Inductive Logic Programming Planning of experiments.<br><br>A virtual Research Agency|
|---|
<br><br>Metabolomics Transcriptomics|
|---|


- Fig. 1. The overall architecture of the Genesis system. The main hardware system will have 1,000 computer-controlled µ-bioreactors. These will be connected to a mass-spectrometer to read-out the metabolomic (small-molecules) state of the yeast population, and to an RNA-SEQ system to read-out the transcriptome (tRNA) state of the yeast population. The software consists of many modules, going from low-level bioreactor control, to high-level AI units. The units in italics are currently incomplete.


##### 2.1 Genesis Hardware

The hardware of Genesis will have at its heart a micro-fluidic system with one thousand computer-controlled µ-bioreactors (developed in Vanderbilt University, USA) (Fig. 2). Achieving this will be a revolution in laboratory automation, as most biological labs have ¡10 chemostats. The µ-bioreactors will be arranged in groups of 48 using the standard footprint of a microtitre plate. Each µ-bioreactors will be able to be configured in real time to run in batch, fed batch, or continuous mode. This flexibility will enable a very wide range of biological conditions to be explored, and experiments to be executed. In each µ-bioreactors the Genesis-AI system will specify experiments of the form:

- • Genetics: (yeast strain - from a large library kept in an automated deepfreeze: ∼20,000 strains deletants, reporters, etc.), growth-rate (when used as a chemostat), OD (when used as a turbidostat).
- • Environment: Growth medium (a cocktail of 10 metabolites and small-molecules added to a minimally defined medium from ∼100), Drugs (a complex cocktail of compounds added to the growth media from ∼10,000).


The observables from these experiments will be growth rate (batch), metabolic analysis of the growth medium (∼10 compounds), metabolic analysis of the internal state of the yeast (∼100 metabolites), and comprehensive gene expression levels (∼6,000 genes). These observables are both automatable and highly informative.

![image 3](Tiukova et al._2024_Genesis Towards the Automation of Systems Biology Research_images/imageFile3.png)

![image 4](Tiukova et al._2024_Genesis Towards the Automation of Systems Biology Research_images/imageFile4.png)

### (a) (b)

- Fig. 2. Genesis Hardware. (a) Is the initial 12 µ-bioreactor system working in Chalmers. (2) The schematics of the fluidics and micro-formulator design.


##### 2.2 Mass Spectrometry

In our proof of concept work on automating systems biology [11] we could only measure yeast population growth - using Optical Density (OD). This greatly limited how much could be learnt about systems biology. With Genesis we will measure (1) the internal state of ∼100 metabolites in the yeast populations in the µ-bioreactors, and (2) the internal state of ∼6,000 tRNA types in the yeast populations in the µ-bioreactors (RNA-SEQ). This will enable far greater information constraints on the modelling.

For the metabolomics experiments we plan a capacity of ∼10,000 measurements a day. This is possible through integrating laboratory automation (Agilent RapidFire) and an Agilent 6560 ion mobility-mass spectrometry (IM-MS) system (Fig. 3). Ion mobility MS does not require a slow chromatography step. To the best of our knowledge this is a higher rate of measurements than any existing MS system. To deal with this planned high rate of measurement we have developed AutonoMS, a platform for automatically running, processing, and analysing high-throughput mass spectrometry experiments [12]. AutonoMS enables automated software agent-controlled end-to-end measurement and analysis runs from experimental specification files that can be produced by human users or upstream software processes. AutonoMS is currently designed for IM-MS, but can be adapted to additional analytical instruments and data processing flows.

We have demonstrated the utility of AutonoMS in a high-throughput flow-injection ion mobility configuration with 5 second sample analysis time, processing robotically-prepared chemical standards and cultured yeast samples in targeted and untargeted metabolomics applications [12].

|![image 5](Tiukova et al._2024_Genesis Towards the Automation of Systems Biology Research_images/imageFile5.png)|
|---|


- Fig. 3. The Gensis Mass Spectrometry platform: an Agilent RapidFire (the robotics) and a 6560 ion mobility-mass spectrometry (IM-MS) system.


##### 2.3 Ontologies

In collaboration with IT company Thoughtworks, we have developed Genesis-DB, a database system designed to support the Genesis project, and Robot Scientists in general, by providing software agents access to large quantities of structured domain (RDF, Datalog) information [13]. We have also developed a new ontology for modelling data and meta-data from autonomously performed yeast µ-bioreactors cultivations. The ontologies for experiments records such experimental conditions as temperature, growth medium, pH, sampling times, etc. The ontology for experimental results records Gene counts, mass

spec readouts, etc. Genesis-DB is designed to support reasoning about past experiments, and the planning of future experiments [13].

We have demonstrated how Genesis-DB enables the research life cycle by modelling yeast gene regulation, guiding future hypotheses generation and design of experiments (Fig. 4) [13]. Genesis-DB supports AI-driven discovery through automated reasoning and its design is portable, generic, and easily extensible to other AI-driven molecular biology laboratory data and beyond.

|YBL093C<br><br>YDR171W<br><br>YDR213W<br><br>YDR216W<br><br>YPL240C<br><br>YDR270W<br><br>YDR451C<br><br>YLR259C<br><br>YER036C<br><br>YNL123W<br><br>YER148W<br><br>YFL021W<br><br>YGL047W<br><br>YHR006W<br><br>YHR124W<br><br>YHR178W<br><br>YKL062W<br><br>YKR099W<br><br>YLR071C<br><br>YLR223C<br><br>YLR242C<br><br>YMR009W<br><br>YMR042W<br><br>YMR112C<br><br>YNL314W<br><br>YOL067C<br><br>YOL089C YOR174W<br><br>YOR363C<br><br>YPL048W<br><br>YPR008W<br><br>YPR168W<br><br>YPR176C<br><br>YER036C<br><br>YNL123W<br><br>YOL089C<br><br>YOR174W<br><br>YDR213W<br><br>YHR124W<br><br>YKL062W<br><br>YNL314W<br><br>YDR171W<br><br>YPL240C<br><br>YLR259C<br><br>![image 6](Tiukova et al._2024_Genesis Towards the Automation of Systems Biology Research_images/imageFile6.png)<br><br>|
|---|


- Fig. 4. Visualisation of database usage from demonstration software agent utilisation of experimental metadata for systems biology model improvement. It represents a cycle of model improvement. (a) First a gene regulatory network is reconstructed from gene counts retrieved from the database with query. (b) Then the experimental conditions are retrieved and the space visualised. (c) A hypothesis along with the experimental procedures to test it are written to the database. (d) Then the regulatory network is recreated including data including the new high temperature experiment. (e) New visualisation with high temperature data.


##### 2.4 Model Revision

In the Genesis project we will automate hundreds of thousands of system biology model revisions. This implies that these model revisions will need to be systematically recorded and available for inference. We have therefore developed RIMBO (Revisions for Improvements of Models in Biology Ontology), which describes the changes made to computational biology models [14] (Fig. 5). RIMBO is intended as the foundation of a database

containing and describing iterative improvements to models. By recording high level information, such as modelled phenomena, and model type, using controlled vocabularies from widely used ontologies, the same database can be used for different model types. The database aims to describe the evolution of models by recording chains of changes to them. To make model revisions clear, emphasise has been put on recording the reasons, and descriptions, of the changes.

We have demonstrated the usefulness of a database based on RIMBO by modelling the update from version 8.4.1 to 8.4.2 of the genome-scale metabolic model Yeast8, a modification proposed by an abduction algorithm, as well as thousands simulated revisions [14]. This results in a database demonstrating that revisions can successfully be modelled in a semantically meaningful and storage efficient way.

4 F. Kronstro¨m et al.

| |
|---|


Fig. 1. Overview of RIMBO showing classes, how they are connected, and where they come from. The text under the boxes shows some of the subclasses used for the demonstration in Section 3.1.

Fig. 5. Overview of RIMBO, showing the classes and their relationships.

##### 2.5 Bioinformatics

being a superclass to di erent modelling types, imported from ontologies such as the Mathematical Modelling Ontology (MAMO) and EDAM. Information about this model is provided through links to other concepts. For example, BiologicalProcess classes from GO or CL can describe which phenomenon is being modelled, and terms from REPRODUCE-ME and PROV-O specify important metainformation, such as when and by whom it was created, as well as links to relevant publications. The model is also linked to the model ﬁle, represented by an instance of its corresponding Format class from EDAM. This connects, either to an external reference to a ﬁlestore or an online resource, or a representation of the ﬁle in the graph. There are advantages and disadvantages to each option. External references require maintenance to ensure they point to correct locations, but are more storage-e cient. Having large ﬁles in the graph may a ect query performance.

To demonstrate the utility of our ontologies and databases we have used them as the foundation of two bioinformatic studies [15, 16]. Even though S. cerevisiae is a very well-studied organism, ∼20% of its proteins remain largely unannotated. Many of these uncharacterized proteins are conserved between eukaryotes, including humans, providing a significant incentive to increase the pace of discovery.

The first bioinformatics investigation made use of untargeted metabolomics as a tool for functional discovery, generating profiles of ten regulatory deletant strains which are investigated to better understand the consequences of their deletion, and their role in the metabolic reconfiguration of the diauxic shift [15]. Using previous semi-autonomously developed gene regulatory models produced by Eve [11], a set of ten regulatory genes were selected due to both their particular relevance to the shift and implications of previously unknown connections in literature. These were then individually and collectively investigated using their untargeted metabolic profiles with the goal of clarifying regulatory roles and biological consequences of gene deletion. This also served as an assessment of the

The other central class in this ontology is Revision, which is also a subclass of Model, and describes a modiﬁed version of a Model. Recording the reason along with descriptions of the changes made to models is important, both when improvements are generated by humans and machines. For a human generated revision it can, e.g, be seen as a way of documenting the research. For a machine this enables the system to reason about the e ect of previous changes, as well as providing a way of communicating and motivating its ﬁndings with human researchers. The Reason class is from COMODI and has subclasses such as MismatchWithPublication, MismatchWithData, and KnowledgeGain. Linking this to terms from ontologies like APO and relevant genes or chemicals gives a description of the cause of a change. As one revision might be made up of several changes, such as the addition of multiple new reactions, it is described by a Change collecting, possibly several, instances of Deletions, Insertions, or Updates, all from the COMODI ontology. The change can be described by linking these classes to subclasses of SystemsBiologyRepresentation from SBO and speciﬁc reactions or genes.

suitability of untargeted metabolomics as a tool for guidance in high-throughput model improvements.

The second bioinformatics investigation focussed on proteomics (the state of the proteins in the yeast population). Proteomic profiles reflect the functional readout of the physiological state of an organism. S. cerevisiae is a well-studied model organism, and there is a large amount of structured knowledge on yeast systems biology in databases such as the Saccharomyces Genome Database, and highly curated genome-scale metabolic models like Yeast8. These data-sets, the result of decades of experiments, are abundant in information, and adhere to semantically meaningful ontologies [16]. By representing this knowledge in an expressive Datalog knowledgebase we generated data descriptors using relational learning that, when combined with supervised machine learning, enables us to predict protein abundances in an explainable manner. We learnt predictive relationships between protein abundances, function and phenotype; such as α-amino acid accumulations and deviations in chronological lifespan. We further demonstrate the power of this methodology on the proteins His4 and Ilv2, connecting qualitative biological concepts to quantified abundances.

3

|| |
|---|
| |
| |
| |
<br><br>![image 7](Tiukova et al._2024_Genesis Towards the Automation of Systems Biology Research_images/imageFile7.png)<br><br>![image 8](Tiukova et al._2024_Genesis Towards the Automation of Systems Biology Research_images/imageFile8.png)<br><br>![image 9](Tiukova et al._2024_Genesis Towards the Automation of Systems Biology Research_images/imageFile9.png)<br><br>![image 10](Tiukova et al._2024_Genesis Towards the Automation of Systems Biology Research_images/imageFile10.png)<br><br>![image 11](Tiukova et al._2024_Genesis Towards the Automation of Systems Biology Research_images/imageFile11.png)|
|---|


a transcription factor (B) whose deletion causes the cell to have 176 an abnormal chronological lifespan. 177

Protein abundance can be predicted directly from relational 178 data descriptors 179 The generated programs (descriptors) were used as predictive 180 features (independent variables) for the prediction of abundances 181 for all of the 2292 proteins present in the data-set generated 182 by Messner et al.[10]. Feature importances were calculated using 183 both a model agnostic method, SHAP, and gain, a model speciﬁc 184 importance metric[25, 27, 28]. To assess the predictive capability of 185 the features across the whole space of predictable proteins, values 186 were normalized and averaged across the span of all the trained 187 models. All of the presented patterns along with translations into 188 English are given in the Supplementary Notes (II-V). 189

![image 12](Tiukova et al._2024_Genesis Towards the Automation of Systems Biology Research_images/imageFile12.png)

Fig. 1: Data-set construction using frequent pattern mining on databases on yeast systems biology, utilizing sample meta-data from a proteomics data-set by Messner et al.[10]. Biological databases are represented in Datalog. WARMR is utilized (using sample meta-data from the selected data-set) to extract frequent patterns from the database. These patterns are propositionalized and used as independent variables (predictive variables) in the prediction of protein abundances.

- Fig. 6. Data-set construction using frequent pattern mining on databases on yeast systems biology (SGD, Yeast8, KEGG, BioGRID) and sample metadata from measured protein abundances. Biological databases are represented in Datalog, patterns are then mined with the WARMR relational learning method (using information on strains as examples) (Dehaspe et al., 1998; Srinivasan, 2024) to extract propositional relational patterns (and simple instantiations) that are then used as independent variables in the prediction of protein abundances.


- 156 brings[25]. SHAP is based on a game-theoretic approach and is
- 157 used to evaluate the outputs of any machine learning model[27].
- 158 It connects optimal credit allocation with local explanations
- 159 by estimating instance-wise Shapley values. More speciﬁcally,
- 160 TreeExplainer, a SHAP-based methodology optimized for tree-
- 161 based machine learning models, was used[28].
- 162 Results
- 163 Frequent pattern mining
- 164 As seen in Figure 1, a database was constructed by establishing
- 165 gene-to-entity relations from SGD, BioGRID and Yeast8[3, 4, 5].
- 166 These relations were then described decalaratively in Datalog[21].
- 167 This relational database was then used as a basis for frequent
- 168 pattern searches using a simpliﬁed version of the WARMR-
- 169 algorithm implemented in Aleph, utilizing sample meta-data
- 170 (deletetant strains) as positive examples[22]. The patterns were
- 171 then represented as logic programs[8, 21, 22]. An example of
- 172 a typical pattern (biological concept), represented as a Prolog
- 173 program is:

Gene(A) := RegulatedBy(A, B, Transcription factor), nullPhenotype(B, Abnormal chronological lifespan), InvolvedIn(A, One   carbon metabolic process)

- 174 This program can be interpreted as: genes (A) which are involved
- 175 in the one-carbon metabolic process, and which are regulated by


Fig. 2: Protein abundance predictability from relational features according to mean R2 across 2292 proteins in the data-set. The plot was truncated at ±0.6 R2 for visualization purposes. Each separate model was evaluated using 5-fold CV. One dot represents the mean score of a protein prediction model. The light blue area represents the standard deviation. The histogram denotes the distribution of mean R2 for the predictive models.

As observed in Figure 2A, protein abundance can be predicted 190 from relational descriptors alone, with the majority of models 191 showing a positive, although weak, coe cient of determination. 192 A smaller subset of proteins show a stronger average predictive 193 performance of above 0.3 R2. This indicating that the coverage 194 of relations present in the generated descriptors are su cient 195 to explain a signiﬁcant fraction of the variation present in 196 the abundances. The predictable fraction of proteins compared 197 favourably to an explicit representation of the database (see 198 Supplementary Notes VII) 199

As seen in Figure 3A and Figure 3B, features important 200 for prediction (across the span of all available proteins) are 201 descriptors with a large number of covered examples. Reasonably 202 enough, abundance predictions were mainly dominated by 203 logic programs (descriptions and English translations of these 204 descriptors/programs can be seen in Supplementary Notes 205 II) containing sub-patterns with large e↵ects on metabolism, 206 including: terms regarding decreased ﬁtness or growth defects and 207 abnormal accumulations of ↵-amino acids (ilp140, ilp662, ilp613, 208 ilp322, ilp1187, ilp656, ilp601, ilp345, ilp632, ilp651); exclusively 209

##### 2.6 Learning Logical Models

The primary systems biology target for Genesis is the automated improvement of genomescale metabolic models (GEMs) in S. cerevisiae. There are many different approaches to the systems biology modelling of metabolism, ranging from ordinary differential equations (ODEs), flux-balance analysis (FBA) simulations, to graph topology models [11]. One approach we favour is to use first-order logic (FOL) [1]. The advantage of using FOL is that there are many available tools to infer new structure; which is much harder to do with say ODEs. We have developed LGEM+, a system for automated abductive improvement of GEMs consisting of: a compartmentalised FOL framework for describing biochemical pathways (using curated GEMs as the expert knowledge source); and a two-stage hypothesis LGEMabduction+: a FOLprocedureframework for[17].automated improvement of MNMs 5

![image 13](Tiukova et al._2024_Genesis Towards the Automation of Systems Biology Research_images/imageFile13.png)

![image 14](Tiukova et al._2024_Genesis Towards the Automation of Systems Biology Research_images/imageFile14.png)

![image 15](Tiukova et al._2024_Genesis Towards the Automation of Systems Biology Research_images/imageFile15.png)

![image 16](Tiukova et al._2024_Genesis Towards the Automation of Systems Biology Research_images/imageFile16.png)

Fig. 1. Conversion of genome-scale metabolic model provided in SBML to logical theory. (A) A reaction is encoded in SBML using identiﬁers to represent the substrates and products, and a logical rule for enzyme availability (GPR=“gene-protein-reaction rule”). (B) The information contained on each reaction is encoded using logical formulae into a set of clauses; predicate deﬁnitions are provided in Table 1. Here equation (1) is the reaction activation clause. “∧” is a conjunction symbol (“AND”), meaning all of the literals in the expression must be true for the RHS of the clause to be true; “∨” is a disjunction symbol (“OR”). So we can read (1) as: “reaction r 0889 is active if all of the metabolites in the set {s 0340, s 1207} are present in the cytoplasm and at least one of the isoenzymes is present”. Similarly equation (2) describes the condition for a relevant enzyme to be present; equations (3a,b) describe the conditions for each of these isoenzymes to be formed; and equations (4a-c) are the reaction product clauses and state that “if reaction r 0889 is active then each of its products are present”.

- Fig. 7. Conversion of genome-scale metabolic model provided in SBML to logical theory. (A) A reaction is encoded in SBML using identifiers to represent the substrates and products, and a logical rule for enzyme presence. (B) The information contained on each reaction is encoded using a logical formulae into a set of clauses. Here equation (1) is the reaction activation clause. it can be read as: “reaction r0889 is active if all of the metabolites in the set {s0340, s1207} are present in the cytoplasm and at least one of the isoenzymes is present”. Similarly, equation (2) describes the condition for a relevant enzyme to be present; equations (3a,b) describe the conditions for each of these isoenzymes to be formed; and equations (4a-d) are the reaction product clauses and state that “if reaction r0889 is then each of its products are present”.


![image 17](Tiukova et al._2024_Genesis Towards the Automation of Systems Biology Research_images/imageFile17.png)

![image 18](Tiukova et al._2024_Genesis Towards the Automation of Systems Biology Research_images/imageFile18.png)

![image 19](Tiukova et al._2024_Genesis Towards the Automation of Systems Biology Research_images/imageFile19.png)

![image 20](Tiukova et al._2024_Genesis Towards the Automation of Systems Biology Research_images/imageFile20.png)

We have demonstrated that deductive inference on logical theories created using LGEM+, using the automated theorem prover iProver [18], can predict growth/no- growth of S. cerevisiae strains in minimal media. LGEM+ proposed 2094 unique candidate hypotheses for model improvement [17]. We assessed the value of the generated hypotheses using two criteria: (a) genome-wide single-gene essentiality prediction, and (b) constraint of fluxbalance analysis (FBA) simulations. For (b) we developed an algorithm to integrate FBA with the logic model. We demonstrated a model-driven experimental design strategy, and demonstrate this with a differential expression study on the gene PFK2 [17].

#### 3 Discussion

##### 3.1 Completing Genesis

The core structure of Genesis is complete, but much remains before the system is working at full capacity (Fig. 1). For the hardware: the µ-bioreactor hardware needs to be scaledup from 12 µ-bioreactor units to 48 µ-bioreactor units, and then 21 such units integrated; the MS system needs to fully integrated with the µ-bioreactors; and we also need to integrate the planned (RNA-SEQ) transcriptomics experiments. For the software: we need more work on ontologies, databases, and knowledgebases; we need to develop the planned agent system (an agent for every known gene, protein, small molecule in yeast); we need to further develop the relational learning/inductive logic programming machine learning systems to enable the formation of more biologically relevant hypotheses about mode structure; we need to develop a robust control system to deal with the order of a thousand hypothesis-led experimental cycles per day; and finally we need to implement a Genesis virtual Research Agency to control overall resources to the agents.

##### 3.2 Large Language Models

The success of Large Language Models (LLMs) is a step-change in AI. LLMs have achieved breakthrough performance on a wide range of tasks that require human intelligence. It is to be expected that LLMs will impact on the Genesis project in multiple ways, but it is not yet clear which will be the most important. One exciting potential use of LLMs in Genesis is in converting scientific knowledge currently encoded in natural language (e.g. in textbooks, papers), into explicit formal knowledge (e.g. in logic) that can be checked for correctness/truth and can be directly reasoned with. LLMs solve the predicate invention problem.

Another exciting use of LLMs is in hypothesis formation. The architecture of LLMs entails that the output string is the most likely one given the input string and the training data. For science these strings may be interpreted as scientific hypotheses. Due to their internal complexity and sophistication LLMs have the potential to go beyond existing text-based scientific hypothesis generation tools. The generation of hypotheses by LLMs is closely related to the phenomena of “hallucinations”. These are LLM outputs that are not valid inferences from the training data. Some hallucinations may be simply factually wrong. For others, their validity is uncertain. Hallucinations are a serious problem in many applications. For example, in science it is not acceptable to hallucinate (make up) false references. However in scientific hypothesis generation hallucinations may be useful: probable novel hypotheses whose validity may be objectively tested by laboratory experiments.

#### Acknowledgments

Funding: This work has been supported by the UK Engineering and Physical Sciences Research Council (EPSRC) [EP/R022925/2, EP/W004801/1 and EP/X032418/1], and by the Wallenberg AI, Autonomous Systems and Software Program (WASP) funded by the Alice Wallenberg Foundation.

#### References

- [1] R. D. King, K. E. Whelan, F. M. Jones, P. G. K. Reiser, C. H. Bryant, S. H. Muggleton, D. B. Kell, and S. G. Oliver, “Functional genomic hypothesis generation and experimentation by a robot scientist,” Nature, vol. 427, no. 6971, pp. 247–252, 2004.
- [2] R. D. King, J. Rowland, S. G. Oliver, M. Young, W. Aubrey, E. Byrne, M. Liakata, M. Markham, P. Pir, L. N. Soldatova, A. Sparkes, K. E. Whelan, and A. Clare, “The automation of science,” Science, vol. 324, no. 5923, pp. 85–89, 2009.
- [3] R. King and H. Zenil, “Artificial intelligence in scientific discovery: Challenges and opportunities,” tech. rep., OECD, 2023.
- [4] R. King and H. Zenil, “A framework for evaluating the AI-driven automation of science,” tech. rep., OECD, 2023.
- [5] R. King, O. Peter, and P. Courtney, “Robot scientists: From Adam to Eve to Genesis,” tech. rep., OECD, 2023.
- [6] K. Williams, E. Bilsland, A. Sparkes, W. Aubrey, M. Young, L. N. Soldatova, K. De Grave, J. Ramon, M. de Clare, W. Sirawaraporn, S. G. Oliver, and R. D. King, “Cheaper faster drug development validated by the repositioning of drugs against neglected tropical diseases,” Journal of The Royal Society Interface, vol. 12, no. 104, p. 20141289, 2015. Publisher: Royal Society.
- [7] E. Bilsland, A. Sparkes, K. Williams, H. J. Moss, M. de Clare, P. Pir, J. Rowland, W. Aubrey, R. Pateman, M. Young, M. Carrington, R. D. King, and S. G. Oliver, “Yeast-based automated high-throughput screens to identify anti-parasitic lead compounds,” Open Biology, vol. 3, no. 2, p. 120158, 2013.
- [8] E. Bilsland, L. van Vliet, K. Williams, J. Feltham, M. P. Carrasco, W. L. Fotoran, E. F. G. Cubillos, G. Wunderlich, M. Grøtli, F. Hollfelder, V. Jackson, R. D. King, and S. G. Oliver, “Plasmodium dihydrofolate reductase is a second enzyme target for the antimalarial action of triclosan,” Scientific Reports, vol. 8, no. 1, p. 1038, 2018.
- [9] P. M. M. Duhem, The Aim and Structure of Physical Theory. Princeton University Press, 1991.
- [10] H. Kitano, “Nobel turing challenge: creating the engine for scientific discovery,” npj Systems Biology and Applications, vol. 7, no. 1, pp. 1–12, 2021.
- [11] A. Coutant, K. Roper, D. Trejo-Banos, D. Bouthinon, M. Carpenter, J. Grzebyta, G. Santini, H. Soldano, M. Elati, J. Ramon, C. Rouveirol, L. N. Soldatova, and R. D. King, “Closed-loop cycles of experiment design, execution, and learning accelerate systems biology model development in yeast,” Proceedings of the National Academy of Sciences, vol. 116, no. 36, pp. 18142–18147, 2019.


- [12] G. K. Reder, E. Y. Bjurstro¨m, D. Brunnsa˚ker, F. Kronstr¨m, P. Lasin, I. Tiukova, O. I. Savolainen, J. N. Dodds, J. C. May, J. P. Wikswo, J. A. McLean, and R. D. King, “AutonoMS: Automated ion mobility metabolomic fingerprinting,” Journal of the American Society for Mass Spectrometry, vol. 35, no. 3, pp. 542–550, 2024.
- [13] G. K. Reder, A. H. Gower, F. Kronstr¨m, R. Halle, V. Mahamuni, A. Patel, H. Hayatnagarkar, L. N. Soldatova, and R. D. King, “Genesis-DB: a database for autonomous laboratory systems,” Bioinformatics Advances, vol. 3, no. 1, p. vbad102, 2023.
- [14] F. Kronstr¨m, A. H. Gower, I. A. Tiukova, and R. D. King, “RIMBO - an ontology for model revision databases,” in Discovery Science, pp. 523–534, Springer Nature Switzerland, 2023.
- [15] D. Brunnsa˚ker, G. K. Reder, N. K. Soni, O. I. Savolainen, A. H. Gower, I. A. Tiukova, and R. D. King, “High-throughput metabolomics for the design and validation of a diauxic shift model,” npj Systems Biology and Applications, vol. 9, no. 1, pp. 1–9, 2023.
- [16] D. Brunnsa˚ker, F. Kronstr¨m, I. A. Tiukova, and R. D. King, “Interpreting protein abundance in Saccharomyces cerevisiae through relational learning,” Bioinformatics, vol. 40, no. 2, p. btae050, 2024.
- [17] A. H. Gower, K. Korovin, D. Brunnsa˚ker, I. A. Tiukova, and R. D. King, “LGEM+: A first-order logic framework for automated improvement of metabolic network models through abduction,” in Discovery Science, pp. 628–643, Springer Nature Switzerland, 2023.
- [18] K. Korovin, “iProver – an instantiation-based theorem prover for first-order logic (system description),” in Automated Reasoning, pp. 292–298, Springer, 2008.


