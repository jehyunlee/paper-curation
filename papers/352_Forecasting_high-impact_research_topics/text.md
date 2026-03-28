arXiv:2402.08640v4[cs.DL]11 Jun 2025

# Forecasting high-impact research topics via machine learning on evolving knowledge graphs

Xuemei Gu1, ∗ and Mario Krenn1, †

1Max Planck Institute for the Science of Light, Staudtstrasse 2, 91058 Erlangen, Germany

The exponential growth in scientific publications poses a severe challenge for human researchers. It forces attention to more narrow sub-fields, which makes it challenging to discover new impactful research ideas and collaborations outside one’s own field. While there are ways to predict a scientific paper’s future citation counts, they need the research to be finished and the paper written, usually assessing impact long after the idea was conceived. Here we show how to predict the impact of onsets of ideas that have never been published by researchers. For that, we developed a large evolving knowledge graph built from more than 21 million scientific papers. It combines a semantic network created from the content of the papers and an impact network created from the historic citations of papers. Using machine learning, we can predict the dynamic of the evolving network into the future with high accuracy (AUC values beyond 0.9 for most experiments), and thereby the impact of new research directions. We envision that the ability to predict the impact of new ideas will be a crucial component of future artificial muses that can inspire new impactful and interesting scientific ideas.

### INTRODUCTION

As we see an explosion in the number of scientific articles [1–4], it becomes increasingly challenging for researchers to find new impactful research directions beyond their own expertise. Consequently, researchers might have to focus on narrow subdisciplines. A tool that can read and intelligently act upon scientific literature could be an enormous aid to individual scientists in choosing their next new and high-impact research project, which – on a global scale – could significantly accelerate science itself.

These days, a natural first choice for an AI-assistant would be powerful large-language-models (LLMs) such as GPT-4 [5], Gemini [6], LLaMA-2 [7] or custom-made models [8]. However, these models often struggle in scientific reasoning, and it remains unclear how they can suggest new scientific ideas or evaluate their impact in a reliable way in the near term.

An alternative and complementary approach is to build scientific semantic knowledge graphs. Here, the nodes represent scientific concepts and the edges are formed when two concepts are researched together in a scientific paper [2]. While this approach extracts only small amounts of information from each paper, surprisingly non-trivial conclusions can be drawn if the underlying dataset of papers is large. An early example of this is a work in biochemistry [9]. The authors use their semantic network, where nodes represent biomolecules, to find new potentially more efficient exploration strategies for the bio-chemistry community on a global scale. In these semantic networks, an edge between two concepts indicates that researchers have jointly investigated these research concepts. The edges are drawn from papers, thus they are created at a specific time when the paper was published. In this way, one creates an evolving semantic

∗ xuemei.gu@mpl.mpg.de † mario.krenn@mpl.mpg.de

network that captures what researchers have investigated in the past. With such an evolving network, one can ask how the network might evolve in the future. In the scientific context, this question can be reformulated into what scientists will research in the future. For example, if two nodes do not share an edge, one can ask whether they will share an edge in the next three years – or, alternatively, whether scientists will investigate these two concepts jointly within three years. This question, denoted as a link-prediction problem in network theory [10], has been successfully demonstrated with high prediction quality for semantic networks in the field of quantum physics [11] and artificial intelligence [4]. These works focus on the question what scientists will work on, completely leaving out which of these topics will be impactful.

Impact in the scientific community is often approximated (for lack of better metrics [12, 13]) by citations [1, 2, 14, 15], including exciting results that find interpretable mathematical models to describe citation evolution [16–19]. Beside concrete mathematical modelling, impact of scientific papers has also been predicted using advanced statistical and machine-learning methods that use meta-data such as including authors and affiliations [20], the content and the references of the paper [21, 22]. Techniques employed for the predictions of individual paper impact using a combination of characteristics include support-vector machines [23], regression [24–26], dense [27] or graph neural networks [28].

The prediction of a paper’s impact however is only possible after the research is completed, and long after its underlying idea is created. A true scientific assistant or muse however should contribute at the earliest stage of the scientific cycle, when the idea for the next impactful research project is born. One solution is the prediction at the concept level. Specifically, we can ask the question Which scientific concepts, that have never been investigated jointly, will lead to the most impactful research?.

In this work, we answer this question by combining semantic networks and citation networks that are purely

|37,960 concepts|
|---|
|Domain-Specific Concepts<br><br>Optics, Quantum Physics<br><br>![image 1](Gu and Krenn_2025_Forecasting high-impact research topics via machine learning on evolving knowledge graphs_images/imageFile1.png)|


||Proc. Natl Acad. Sci. USA 117, 60–67 (2020)<br><br>Accurate and rapid background estimation in single-molecule localization microscopy using the deep neural network […] even when pointspread function (PSF) engineering is in use to create complex PSF shapes. We trained BGnet to extract the background from images […].<br><br>p1|
|---|
<br><br>|Phys. Rev. D 97, 102002 (2018)<br><br>[…] Cosmic strings are topological defects which can be formed in grand unified theory scale phase transitions in the […] loops and the subsequent emission of gravitational waves, thus offering an experimental signature for the existence of cosmic strings […]<br><br>p3|
|---|
<br><br>|Phys. Rev. B 98, 060301 (2018)<br><br>Learning phase transitions from dynamics […] use of recurrent neural networks for classifying phases […] featuring an inherently dynamical time-crystalline phase, the phase diagram that our network […]<br><br>p4|
|---|
<br><br>|Nat Commun 11, 1493 (2020)<br><br>[…] we develop a supervised machine-learning approach to cluster analysis which is fast and accurate. Trained on a variety of simulated clustered data, the neural network can classify millions of points from a typical single-molecule localization microscopy data set, with […].<br><br>p2|
|---|
<br><br>|![image 2](Gu and Krenn_2025_Forecasting high-impact research topics via machine learning on evolving knowledge graphs_images/imageFile2.png)|
|---|
<br><br>|21,165,421 papers|
|---|
|
|---|


|2,444,442 papers|
|---|
|![image 3](Gu and Krenn_2025_Forecasting high-impact research topics via machine learning on evolving knowledge graphs_images/imageFile3.png)<br><br>![image 4](Gu and Krenn_2025_Forecasting high-impact research topics via machine learning on evolving knowledge graphs_images/imageFile4.png)<br><br>![image 5](Gu and Krenn_2025_Forecasting high-impact research topics via machine learning on evolving knowledge graphs_images/imageFile5.png)<br><br>![image 6](Gu and Krenn_2025_Forecasting high-impact research topics via machine learning on evolving knowledge graphs_images/imageFile6.png)|


|368,825 concepts|
|---|
|Complete Concept Corpus<br><br>![image 7](Gu and Krenn_2025_Forecasting high-impact research topics via machine learning on evolving knowledge graphs_images/imageFile7.png)<br><br>----<br><br>----<br><br>----|


|Nodes: Scientific Concepts|
|---|


mini-knowledge graph

time crystalline phase

neural network

𝑐 𝑦2018:{4,,8𝑐,11:,1144,,10}

phase transition

supervised machine learning

2020,𝑐 ,𝑐 𝑦

2020,𝑐 ,𝑐 𝑦

𝑐,2018 𝑐,

cosmic string

)𝑦(

point spread function

gravitational wave

single molecule localization microscopy

|Edges: co-apperance & citation of concept pairs|
|---|


- FIG. 1. Generation of the knowledge graph with time and citation information. Vertices are formed by scientific concepts, which are extracted from scientific papers (titles and abstracts) from prominent academic preprint servers. Edges are formed when concepts are investigated jointly in a scientific publication. There are 21,165,421 out of 92,764,635 papers from OpenAlex which form at least one edge. The edges are augmented with citation information, which acts as a proxy for impact in our work. A mini-knowledge graph (blue edges) is constructed from four randomly selected papers (p1-p4) [29–32] from OpenAlex as an example. Here, cp4 represents the total citations of paper p4 since its publication, and cp4(y) is its annual citations from 2018 to 2022 (e.g., cp4(2018) = 4). The citation value of the edge is the sum of the all papers creating the edge.


based on the level of scientific concepts1. Specifically, we develop a large evolving knowledge graph using more than 21 million scientific papers, from 1709 (starting with a letter by Antoni van Leeuwenhoek [38]) to April 2023. The vertices of the knowledge graph are scientific concepts and the edges between two concepts contain information about when these topics have been investigated and how often they have been cited subsequently. We then train a machine learning model on the historic evolution of the knowledge graph. We find that the neural network can predict with high accuracy which concept pairs, that have never been jointly investigated before in any scientific paper, will be highly cited in the future. Being able to predict the potential impact of new research ideas – before the paper is written or the research is done or even started – could be a cornerstone in future scientific AI-assistants that help humans broadening their horizon of possible new research endeavours [39].

### RESULTS

Creating a list of scientific concepts – At the heart of our knowledge graph are scientific concepts, as depicted in Fig. 1. We chose not to rely on existing concept lists, such as the APS or computer science ontology [40], for several reasons. Firstly, our goal is to ultimately cover all natural sciences comprehensively, and a universal list encompassing this breadth doesn’t currently exist. Secondly, we want to capture the most recent concepts that might be absent from existing lists. Lastly, generating our list ensures that we have a granular understanding and control over the concepts.

To build our concept list, we started with 2,444,442 papers from four publicly available preprint servers: arXiv, bioRxiv, medRxiv, and chemRxiv. We use papers from preprint servers for two reasons: (1) It contains papers that are not published yet in journals, thus our dataset also contains state-of-the-art concepts; (2) they associate

1 GitHub: Impact4Cast

- (a)
- (b)


Emerging Citation for Concepts

- 101
- 102
- 103
- 104


citationcitation

year

0

2012 2014 2016 2018 2020 2022

Emerging Citation for Concept Pairs

- 101
- 102
- 103
- 104


year

0

2012 2014 2016 2018 2020 2022

|perovskite solar cell vdw heterostrucrure sachdev ye kitaev<br><br>discrete time crystal<br><br>non hermitian skin effect<br><br>high order topological insulator<br><br>quasi bic resonance<br><br>generative adversarial network<br><br>|
|---|


|transition metal & weyl semimetal<br><br>black phosphorus & field effect transistor<br><br>perovskite solar cell & halide perovskite<br><br>perovskite quantum dot & light emitting diode encoder network & convolutional neural net<br><br>minimization algorithm & gravitational wave<br><br>deep convolutional net & image segmentation<br><br>sars cov & regression method|
|---|


- FIG. 2. Fastest growing citations of concepts and concept pairs: Evolution of citations over three years for the topfastest growing, previously uncited concepts (a) and concept pairs (b). We find many revolutionary topics in the realm of quantum physics and optics research in the last decade, including Perovskite devices [33], the emergence of complex and nonhermitian topology [34], the introduction of advanced concepts of machine learning in physics [35–37] and quasi-BIC (bound state in continuum) resonances.


papers to research categories, which can be used to focus on specific scientific domains (as we do, with the field of quantum physics and optics). The data cutoff is February 2023. From these, we extracted titles and abstracts of the papers. To single out concept candidates from this extensive collection, we applied the Rapid Automatic Keyword Extraction (RAKE) algorithm based on statistical text analysis to automatically detect important keywords [41] (see details in the Appendix B). Each of these candidates are ranked Concepts with two words, like phase transition, were retained if they appear in at least 9 papers, while longer concepts, such as single molecule localization microscopy, needed to appear in at least 6 papers. In this way, we can increase the fraction of high-quality concepts. We further developed a suite of natural language processing tools to refine the concepts, followed by manual inspection to remove any incorrectly identified ones. Finally, we got a list which contains over 368,000 concepts. We focus here on concepts specific to the sub-field of optics and quantum physics (representing roughly 10% of the entire concepts), but our method can immediately be translated to any other domain. This refined domain-specific concept list serves as the vertices of our knowledge graph.

Creating an evolving, citation-augmented knowledge graph – Now that we have the vertices, we can create edges that contain information from the

scientific literature. We get the citation information from papers in OpenAlex [42], an open-source database containing detailed information on more than 92 million publications. Edges are drawn when two concepts co-occur in the title or abstract of a scientific paper. If a paper connects two vertices, the weight of the newly formed edge is the paper’s annual citation numbers from 2012 to 2023 together with the total citation number since its publication. If more than one paper creates an edge, then the edge contains the sum of the annual citations (as well as the sum of the total citations) gained by all papers. As research papers appear over time, and their citations are created in time, we effectively build an evolving, citation-augmented knowledge graph that evolves in time (see Fig. 1). From these 92 million papers, 21 million contain at least two concepts of our concept list and can therefore for an edge in the knowledge graph.

The final constructed knowledge graph has 37,960 vertices with more than 26 million edges (built from 190 million concept pairs, containing multi-edges when multiple papers create the same edge) from the OpenAlex dataset, with a data cutoff at April 2023.

In Fig. 2, we show the fastest growing (in terms of citation) concepts and concept pairs since 2012, where we can recognize many highly influential topics in quantum physics and optics research.

features

Jaccard Impactful?

...

Cosine similarity

node degree

2016 2019

train dataset: 2016 -- 2019; test dataset: holdout data 2016 -- 2019; eval dataset: 2019 --2022

- FIG. 3. Forecasting the impact of new research connections. Network and citation features from unconnected vertex pairs from 2016 are used as input to a neural network. The citation information from 2019 is used as a supervision signal to train the neural network. After training, we evaluate the neural network’s abilities by applying it to unconnected vertex pairs from 2019, aiming to predict the developments in 2022 – a task involving data the network has never encountered before.


Forecasting impact of newly created concept connections – With an evolving knowledge graph from the past, we can formulate the prediction of impact for new concept pairs as a supervised learning task, as illustrated in Fig. 3. For a vertex pair that has not had any connection in the year 2016, we predict whether three years later this pair accumulated more than a certain number of citations. Using the historical knowledge graph, we possess an ideal supervision signal for our binary classification task. During the training phase, we selected pairs of vertices that were not connected and calculated 141 features for each pair. These features include 41 network features, divided into 20 node features (such as the number of neighbors and PageRank [43] over the past three years) and 21 edge features (including cosine, geometric, and Simpson similarities [44]). Additionally, we incorporated 100 impact features: 58 of these are node citation features, covering total citations and yearly citations within the last three years. The other 42 features are about vertex pairs and include measures such as the citation ratio between them. Detailed feature description are available in GitHub: Impact4Cast and Tables. I and II in Appendix D. The network features are inspired by the winner of the Science4Cast competition [11, 45], and the citation features are developed empirically and could potentially be improved by careful feature importance analysis. Our neural network is a fully connected feed-forward network with four hidden layers of 600 neurons each. The exploration of more advanced architectures might improve the prediction qualities further. The neural network has to predict whether the unconnected vertex pair in 2019 will have at least IR citations (IR stands for the impact range).

The impact range (IR) is a threshold representing the minimum number of citations a concept pair must accumulate within a specified time frame (e.g., three years) to be classified as “high-impact”. For instance, an IR = 100 means that only concept pairs with at least 100 citations during the defined period are considered impactful. This binary threshold simplifies the problem into a classification task, making it computationally tractable while providing a clear measure of success. Predicting

individual citation counts is inherently noisy due to the stochastic nature of citation dynamics. By using IR, we focus on identifying high-impact trends, avoiding fluctuations of precise citation counts. IR provides a clear and measurable target for classification. This allows us to use metrics like the Area Under the Curve (AUC) of Receiver Operating Characteristics (ROC) curves to evaluate the prediction quality [46].

We perform the training for different values of the impact range IR from IR = 1 to IR = 200, and then quantify the quality with AUC of the ROC curves [46]. The AUC gives a measure of classification quality and stands for the probability that a randomly chosen true example is ranked higher than a randomly chosen false example. A random classifier has AUC = 0.5. We measure the AUC for a test set (which contains unconnected pairs not in the training set) for a prediction from 2016 to 2019, and for an evaluation dataset, with 10 million random data from 2019 to 2022 (while keeping the training data of the neural network from 2016 to 2019). The evaluation dataset shows how well the neural network performs on future, never-seen datasets. This is motivated by our goal that ultimately we want to train a neural network with all available data (let’s say, until January 2023) and predict what happens until the future in 2026. In Fig. 4(a), we find that the AUC scores for both the test set and the evaluation set are beyond 0.8, in most of the cases beyond 0.9, for different IR. We can conclude that the neural network can forecast a high impact of previously never-investigated concept connections to a high degree. In Fig. 4(b), we sort the concept pairs of the evaluation dataset with the neural network (IR = 100), and plot their true citation counts. We further divide the 10 million evaluation dataset into 20 equal parts and plot their average citation count (represented by green bars) for each 5% segment. This clearly demonstrates good predictions at the individual concept pair level. As seen in Fig. 4(c), the highest predicted concept pairs indeed get more than 3 orders of magnitude more citations than the average citation of all 10 million pairs.

Forecasting genuine impact beyond link prediction – Next, we perform an even more challenging, gen-

(a)

(b)

![image 8](Gu and Krenn_2025_Forecasting high-impact research topics via machine learning on evolving knowledge graphs_images/imageFile8.png)

|eval 2019 to 2022<br><br>test 2016 to 2019<br><br>TPR<br><br>0.0<br><br>0.2<br><br>0.4<br><br>0.6<br><br>0.8<br><br>1.0<br><br>0.0 0.2 0.4 0.6 0.8 1.0 FPR<br><br>random<br><br>NN<br><br>ROC Curve|
|---|


800

1.0

- 100
- 101
- 102
- 103


Log-Scale

10-1

0.3

0.9

600

Average Citation

10-2

AUC Score

0.8

Citation

0.2

400

10-3

TPR

0.7

0.0 0.2 0.4 0.6 0.8 1.0

0.1

200

0.6

0

0

0.5

in 1e7

1 50 100 150 200 Impact Range (IR)

0.0 0.2 0.4 0.6 0.8 1.0

NN-sorted Concept Pairs (ranked from high to low)

![image 9](Gu and Krenn_2025_Forecasting high-impact research topics via machine learning on evolving knowledge graphs_images/imageFile9.png)

(c) (d)

| |
|---|


1.0

train 2016 to 2019

- 101
- 102


100

Average Citation of the first N pairs

Log-Scale

IR: {0-5, >=100}

0.8

75

100

0.6

TPR

50

10-1

0.4

0.0 0.2 0.4 0.6 0.8 1.0

25

0.2

test: auc=0.747 eval: auc=0.694 random: auc=0.5

0

0.0

0.0 0.2 0.4 0.6 0.8 1.0 FPR

in 1e7

0.0 0.2 0.4 0.6 0.8 1.0 NN-sorted Concept Pairs (ranked from high to low)

- FIG. 4. Evaluating the machine-learning-based impact forecast. (a): Classification of unconnected pairs, whether they will exceed a certain threshold three years later. Training data contains unconnected vertex pairs from 2016 and the supervision signal according to their impact range IR 3 years later. The test dataset also includes pairs from 2016, but excludes those in the training set. A more challenging evaluation set contains unconnected pairs from 2019, with outcomes verified in 2022, importantly noting that the neural network was only trained on data from 2016 to 2019, not 2019 to 2022. We quantify the quality using the AUC of the ROC curve. For example, IR = 100, i.e, (< 100, >= 100), refers to whether the 3-year citation counts after 2016 (test) or after 2019 (eval) is at least 100. TPR (true positive rate) measures how often a test correctly identifies a true positive, while FPR (false positive rate) measures how often it correctly identifies a true negative. (b): Sorted predictions of the neural network on the evaluation set (blue curve in (a)) shows the very high quality prediction at the level of individual concept pairs. The y-axis stands for the respective fraction of the evaluation dataset (107 data points). The histogram is separated into 20 equal bins. No fitting is involved. In (c), we show the average citation of the first N highest predicted concept pairs. This plot shows impressively that the highest predicted concept pairs indeed have very high citation, more than 3 orders of magnitude higher than the average citation of all 107 pairs (0.029 citations). (d): This more challenging step shows that citation prediction goes beyond link predictions. Here we take unconnected vertex pairs, conditioned on a connection 3 years later. The neural network is tasked to classify these concept pairs in low or high citations, revealing that it is not just predicting new links, but is learning intrinsic citation features. Here IR = [5, 100], i.e, (0 − 5, >= 100), means whether the 3-year citation count after 2016 (test) or after 2019 (eval) is at most 5 or at least 100.


uine impact prediction task that goes beyond link prediction (i.e., predicting which concept pairs will be investigated in the future by a scientific paper). Concretely, in this task training data is conditioned on unconnected vertex pairs in 2016 which are actually connected in 2019. The neural network only gets citation information from 2016 and has to predict whether the newly generated concept pair will be highly impactful or not in the future. For that, our classification task asks whether the newly generated edge will receive citations within 0-5 or

above 100 (Fig. 4(d)) in 2019. We see that the AUC score is beyond 0.7 (for the test set) and beyond 0.67 for the evaluation set, clearly indicating that the neural network can predict impact properties that go beyond the simple link-prediction task.

Highly predicted impact pair and potential applications – We can now investigate the largest predicted pairs of concepts, by taking all unconnected vertex pairs (∼694 million pairs) until January 2023, and let the neural network (trained with all unconnected pairs in

![image 10](Gu and Krenn_2025_Forecasting high-impact research topics via machine learning on evolving knowledge graphs_images/imageFile10.png)

- FIG. 5. Network features vs. predicted impact. A randomly selected set of 100,000 unconnected pairs until January 2023 is used. The color represents the neural network’s prediction of each concept pair’s impact. (a): The y-axis shows cosine similarity, indicating the semantic similarity between concepts; lower values represent concept pairs that are semantically distinct. For each concept pair (u, v), cosine similarity is calculated as the number of shared neighbors divided by the square root of the product of the number of neighbors of u and v. The x-axis is the average vertex degree of the two concepts in the knowledge graph, reflecting their overall prominence. Concepts with low similarity and low degree yet predicted to have high impact could be surprising and offer interesting suggestions. (b): The x-axis represents the average number of new neighbors each concept gained over the last three years. Concept pairs with low similarity and few new neighbors but high impact predictions might highlight potentially overlooked but intriguing ideas. (c): The x-axis denotes citation density (average citations per paper mentioning the concepts). Pairs with low similarity and citation density but high predicted impact could again indicate overlooked potential ideas. (d): Citation counts for concept 1 (x-axis) and concept 2 (y-axis) over last three years are plotted on a logarithmic scale. We can easily identify concept pairs predicted to have high impact in the future, even though they have individually received few citations in the past.


2019 with supervision signal in 2022) sort them by impact predictions. We find that the highest predicted pair is renewable energy and cancer cell. This prediction is a very high-risk bet. For more practical, personalized suggestions, one can restrict the unconnected concept pairs to those related to specific scientists or research groups, aiming for high-impact collaboration suggestions. By examining the published works of scientists to identify their research interests, it becomes possible to identify concept pairs where one aligns with one scientist’s specialty and the other with another scientist’s. Thereby, one can suggest potential collaborations of high impact. As an example, by constraining the personalized research interests of scientists in experimental quantum optics and one researcher in biophysics, the highest predicted impact concepts pairs are ‘microfluidic channel’ with ‘Kerr

resonator’, ‘SARS CoV’ with ‘quantum enhanced sensitivity’ or ‘electron microscopy’ with ‘quantum vacuum field’. These suggestions can be further refined based on their similarity (e.g., represented by the cosine similarity) or the prominence of the concepts (indicated by the node degree), as we show in Fig. 5. Here, we plot 100,000 concept pairs that have not been studied together until January 2023 and use the neural network trained on 2019 dataset to predict their impact. The points are plotted based on various properties, such as the similarity between concepts, their prominence within the network, their growth rate in the network (reflected in newly acquired neighbors), and how often the concepts have been cited previously. Plotting in this way allows us to identify rare outliers – concept pairs with high predicted impact that have unique properties, such

Train: 2019-2021, Eval: 2021-2022

Train: 2018-2020, Eval: 2020-2022

Train: 2017-2019, Eval: 2019-2022

Train: 2016-2018, Eval: 2018-2022

Train: 2015-2017, Eval: 2017-2022

1.0

1.0

1.0

1.0

1.0

0.8

0.8

0.8

0.8

0.8

0.6

0.6

0.6

0.6

0.6

TPR

TPR

TPR

TPR

TPR

0.4

0.4

0.4

0.4

0.4

fcNN AUC=0.9631

fcNN AUC=0.9544

fcNN AUC=0.9474

fcNN AUC=0.9380

fcNN AUC=0.9339

Transformer AUC=0.9571

Transformer AUC=0.9565

Transformer AUC=0.9411

Transformer AUC=0.9377

Transformer AUC=0.9299

0.2

0.2

0.2

0.2

0.2

Forest AUC=0.9532

Forest AUC=0.9560

Forest AUC=0.9445

Forest AUC=0.9361

Forest AUC=0.9314

XGBoost AUC=0.9599

XGBoost AUC=0.9552

XGBoost AUC=0.9433

XGBoost AUC=0.9368

XGBoost AUC=0.9344

Random AUC=0.5

Random AUC=0.5

Random AUC=0.5

Random AUC=0.5

Random AUC=0.5

0.0

0.0

0.0

0.0

0.0

0.0 0.2 0.4 0.6 0.8 1.0 FPR

0.0 0.2 0.4 0.6 0.8 1.0 FPR

0.0 0.2 0.4 0.6 0.8 1.0 FPR

0.0 0.2 0.4 0.6 0.8 1.0 FPR

0.0 0.2 0.4 0.6 0.8 1.0 FPR

Train: 2018-2021, Eval: 2021-2022

Train: 2017-2020, Eval: 2020-2022

Train: 2016-2019, Eval: 2019-2022

Train: 2015-2018, Eval: 2018-2022

Train: 2014-2017, Eval: 2017-2022

1.0

1.0

1.0

1.0

1.0

0.8

0.8

0.8

0.8

0.8

0.6

0.6

0.6

0.6

0.6

TPR

TPR

TPR

TPR

TPR

0.4

0.4

0.4

0.4

0.4

fcNN AUC=0.9635

fcNN AUC=0.9543

fcNN AUC=0.9455

fcNN AUC=0.9358

fcNN AUC=0.9333

Transformer AUC=0.9540

Transformer AUC=0.9582

Transformer AUC=0.9454

Transformer AUC=0.9345

Transformer AUC=0.9301

0.2

0.2

0.2

0.2

0.2

Forest AUC=0.9498

Forest AUC=0.9557

Forest AUC=0.9431

Forest AUC=0.9341

Forest AUC=0.9291

XGBoost AUC=0.9557

XGBoost AUC=0.9566

XGBoost AUC=0.9442

XGBoost AUC=0.9359

XGBoost AUC=0.9331

Random AUC=0.5

Random AUC=0.5

Random AUC=0.5

Random AUC=0.5

Random AUC=0.5

0.0

0.0

0.0

0.0

0.0

0.0 0.2 0.4 0.6 0.8 1.0 FPR

0.0 0.2 0.4 0.6 0.8 1.0 FPR

0.0 0.2 0.4 0.6 0.8 1.0 FPR

0.0 0.2 0.4 0.6 0.8 1.0 FPR

0.0 0.2 0.4 0.6 0.8 1.0 FPR

Train: 2017-2021, Eval: 2021-2022

Train: 2016-2020, Eval: 2020-2022

Train: 2015-2019, Eval: 2019-2022

Train: 2014-2018, Eval: 2018-2022

Train: 2013-2017, Eval: 2017-2022

1.0

1.0

1.0

1.0

1.0

0.8

0.8

0.8

0.8

0.8

0.6

0.6

0.6

0.6

0.6

TPR

TPR

TPR

TPR

TPR

0.4

0.4

0.4

0.4

0.4

fcNN AUC=0.9638

fcNN AUC=0.9537

fcNN AUC=0.9444

fcNN AUC=0.9353

fcNN AUC=0.9296

Transformer AUC=0.9491

Transformer AUC=0.9557

Transformer AUC=0.9432

Transformer AUC=0.9356

Transformer AUC=0.9326

0.2

0.2

0.2

0.2

0.2

Forest AUC=0.9478

Forest AUC=0.9535

Forest AUC=0.9419

Forest AUC=0.9330

Forest AUC=0.9277

XGBoost AUC=0.9581

XGBoost AUC=0.9524

XGBoost AUC=0.9423

XGBoost AUC=0.9340

XGBoost AUC=0.9281

Random AUC=0.5

Random AUC=0.5

Random AUC=0.5

Random AUC=0.5

Random AUC=0.5

0.0

0.0

0.0

0.0

0.0

0.0 0.2 0.4 0.6 0.8 1.0 FPR

0.0 0.2 0.4 0.6 0.8 1.0 FPR

0.0 0.2 0.4 0.6 0.8 1.0 FPR

0.0 0.2 0.4 0.6 0.8 1.0 FPR

0.0 0.2 0.4 0.6 0.8 1.0 FPR

#### (a). Impact Range IR=10.

Train: 2019-2021, Eval: 2021-2022

Train: 2018-2020, Eval: 2020-2022

Train: 2017-2019, Eval: 2019-2022

Train: 2016-2018, Eval: 2018-2022

Train: 2015-2017, Eval: 2017-2022

1.0

| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| |not|enough|data for|evalua|tion|
| | | | | | |
| | | | | | |
| | | | | | |


1.0

1.0

1.0

1.0

0.8

0.8

0.8

0.8

0.8

0.6

0.6

0.6

0.6

0.6

TPR

TPR

TPR

TPR

TPR

0.4

0.4

0.4

0.4

0.4

fcNN AUC=0.9233

fcNN AUC=0.9384

fcNN AUC=0.9355

fcNN AUC=0.9375

Transformer AUC=0.9097

Transformer AUC=0.9330

Transformer AUC=0.9494

Transformer AUC=0.9152

0.2

0.2

0.2

0.2

Forest AUC=0.9264

Forest AUC=0.9559

Forest AUC=0.9458

Forest AUC=0.9342

0.2

XGBoost AUC=0.9160

XGBoost AUC=0.9519

XGBoost AUC=0.9444

XGBoost AUC=0.9368

Random AUC=0.5

Random AUC=0.5

Random AUC=0.5

Random AUC=0.5

0.0

0.0

0.0

0.0

0.0

0.0 0.2 0.4 0.6 0.8 1.0 FPR

0.0 0.2 0.4 0.6 0.8 1.0 FPR

0.0 0.2 0.4 0.6 0.8 1.0 FPR

0.0 0.2 0.4 0.6 0.8 1.0 FPR

0.0 0.2 0.4 0.6 0.8 1.0 FPR

Train: 2018-2021, Eval: 2021-2022

Train: 2017-2020, Eval: 2020-2022

Train: 2016-2019, Eval: 2019-2022

Train: 2015-2018, Eval: 2018-2022

Train: 2014-2017, Eval: 2017-2022

1.0

| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| |not|enough|data for|evalua|tion|
| | | | | | |
| | | | | | |
| | | | | | |


1.0

1.0

1.0

1.0

0.8

0.8

0.8

0.8

0.8

0.6

0.6

0.6

0.6

0.6

TPR

TPR

TPR

TPR

TPR

0.4

0.4

0.4

0.4

0.4

fcNN AUC=0.9178

fcNN AUC=0.9588

fcNN AUC=0.9437

fcNN AUC=0.9400

Transformer AUC=0.9049

Transformer AUC=0.9532

Transformer AUC=0.9495

Transformer AUC=0.9367

0.2

0.2

0.2

0.2

Forest AUC=0.9193

Forest AUC=0.9602

Forest AUC=0.9482

Forest AUC=0.9365

0.2

XGBoost AUC=0.9279

XGBoost AUC=0.9561

XGBoost AUC=0.9472

XGBoost AUC=0.9386

Random AUC=0.5

Random AUC=0.5

Random AUC=0.5

Random AUC=0.5

0.0

0.0

0.0

0.0

0.0

0.0 0.2 0.4 0.6 0.8 1.0 FPR

0.0 0.2 0.4 0.6 0.8 1.0 FPR

0.0 0.2 0.4 0.6 0.8 1.0 FPR

0.0 0.2 0.4 0.6 0.8 1.0 FPR

0.0 0.2 0.4 0.6 0.8 1.0 FPR

Train: 2017-2021, Eval: 2021-2022

Train: 2016-2020, Eval: 2020-2022

Train: 2015-2019, Eval: 2019-2022

Train: 2014-2018, Eval: 2018-2022

Train: 2013-2017, Eval: 2017-2022

1.0

| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| |not|enough|data for|evalua|tion|
| | | | | | |
| | | | | | |
| | | | | | |


1.0

1.0

1.0

1.0

0.8

0.8

0.8

0.8

0.8

0.6

0.6

0.6

0.6

0.6

TPR

TPR

TPR

TPR

TPR

0.4

0.4

0.4

0.4

0.4

fcNN AUC=0.9161

fcNN AUC=0.9497

fcNN AUC=0.9443

fcNN AUC=0.9391

Transformer AUC=0.9329

Transformer AUC=0.9526

Transformer AUC=0.9470

Transformer AUC=0.9414

0.2

0.2

0.2

0.2

Forest AUC=0.9184

Forest AUC=0.9593

Forest AUC=0.9473

Forest AUC=0.9374

0.2

XGBoost AUC=0.9207

XGBoost AUC=0.9489

XGBoost AUC=0.9469

XGBoost AUC=0.9442

Random AUC=0.5

Random AUC=0.5

Random AUC=0.5

Random AUC=0.5

0.0

0.0

0.0

0.0

0.0

0.0 0.2 0.4 0.6 0.8 1.0 FPR

0.0 0.2 0.4 0.6 0.8 1.0 FPR

0.0 0.2 0.4 0.6 0.8 1.0 FPR

0.0 0.2 0.4 0.6 0.8 1.0 FPR

0.0 0.2 0.4 0.6 0.8 1.0 FPR

(b). Impact Range IR=50.

- FIG. 6. Benchmarking fully connected NNs, Transformers, Random Forest, and XGBoost on 27 variations of the prediction task, with 2-4 year training and 1-5 year evaluation intervals, across two different impact ranges (IR).


## as the bright yellow spots highlighted in the insets of Fig. 5. These methods help us narrow down the enor-

Training from 2014 -> 2017

Evaluation: 2017-2018, IR=10

Evaluation: 2017-2019, IR=10

Evaluation: 2017-2020, IR=10

Evaluation: 2017-2021, IR=10

Evaluation: 2017-2022, IR=10

1.0

1.0

1.0

1.0

1.0

0.8

0.8

0.8

0.8

0.8

0.6

0.6

0.6

0.6

0.6

TPR

TPR

TPR

TPR

TPR

0.4

0.4

0.4

0.4

0.4

fcNN AUC=0.9463

fcNN AUC=0.9416

fcNN AUC=0.9373

fcNN AUC=0.9332

fcNN AUC=0.9311

Transformer AUC=0.9572

Transformer AUC=0.9371

Transformer AUC=0.9349

Transformer AUC=0.9304

Transformer AUC=0.9292

0.2

0.2

0.2

0.2

0.2

Forest AUC=0.9446

Forest AUC=0.9317

Forest AUC=0.9314

Forest AUC=0.9294

Forest AUC=0.9289

XGBoost AUC=0.9445

XGBoost AUC=0.9373

XGBoost AUC=0.9365

XGBoost AUC=0.9340

XGBoost AUC=0.9337

Random AUC=0.5

Random AUC=0.5

Random AUC=0.5

Random AUC=0.5

Random AUC=0.5

0.0

0.0

0.0

0.0

0.0

0.0 0.2 0.4 0.6 0.8 1.0 FPR

0.0 0.2 0.4 0.6 0.8 1.0 FPR

0.0 0.2 0.4 0.6 0.8 1.0 FPR

0.0 0.2 0.4 0.6 0.8 1.0 FPR

0.0 0.2 0.4 0.6 0.8 1.0 FPR

Evaluation: 2017-2018, IR=50

Evaluation: 2017-2019, IR=50

Evaluation: 2017-2020, IR=50

Evaluation: 2017-2021, IR=50

Evaluation: 2017-2022, IR=50

1.0

| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| |not|enough|data for|evalua|tion|
| | | | | | |
| | | | | | |
| | | | | | |


1.0

1.0

1.0

1.0

0.8

0.8

0.8

0.8

0.8

0.6

0.6

0.6

0.6

0.6

TPR

TPR

TPR

TPR

TPR

0.4

0.4

0.4

0.4

0.4

fcNN AUC=0.9798

fcNN AUC=0.9493

fcNN AUC=0.9404

fcNN AUC=0.9365

Transformer AUC=0.9744

Transformer AUC=0.9519

Transformer AUC=0.9384

Transformer AUC=0.9307

0.2

0.2

0.2

0.2

Forest AUC=0.9770

Forest AUC=0.9501

Forest AUC=0.9402

Forest AUC=0.9373

0.2

XGBoost AUC=0.9849

XGBoost AUC=0.9531

XGBoost AUC=0.9432

XGBoost AUC=0.9396

Random AUC=0.5

Random AUC=0.5

Random AUC=0.5

Random AUC=0.5

0.0

0.0

0.0

0.0

0.0

0.0 0.2 0.4 0.6 0.8 1.0 FPR

0.0 0.2 0.4 0.6 0.8 1.0 FPR

0.0 0.2 0.4 0.6 0.8 1.0 FPR

0.0 0.2 0.4 0.6 0.8 1.0 FPR

0.0 0.2 0.4 0.6 0.8 1.0 FPR

- FIG. 7. Predictions for varying intervals without retraining. The four ML models were trained using data from 2014 to 2017 and then used to predict outcomes 1 to 5 years into the future without retraining. For one task, the number of positive cases was insufficient for meaningful classification (we set a threshold of at least 10 positive cases out of 1 million total cases).

| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | |no da|ta avail|able| |
| | | | | | |
| | | | | | |
| | | | | | |


0.0 0.2 0.4 0.6 0.8 1.0 FPR

0.0

0.2

0.4

0.6

0.8

1.0

TPR

Evaluation: 2017-2018, IR=50

0.0 0.2 0.4 0.6 0.8 1.0 FPR

0.0

0.2

0.4

0.6

0.8

1.0

TPR

Evaluation: 2017-2019, IR=50

fcNN (IR=50) AUC=0.9798 fcNN (IR=10) AUC=0.9827 Random AUC=0.5

0.0 0.2 0.4 0.6 0.8 1.0 FPR

0.0

0.2

0.4

0.6

0.8

1.0

TPR

Evaluation: 2017-2020, IR=50

fcNN (IR=50) AUC=0.9493 fcNN (IR=10) AUC=0.9553 Random AUC=0.5

0.0 0.2 0.4 0.6 0.8 1.0 FPR

0.0

0.2

0.4

0.6

0.8

1.0

TPR

Evaluation: 2017-2021, IR=50

fcNN (IR=50) AUC=0.9404 fcNN (IR=10) AUC=0.9466 Random AUC=0.5

0.0 0.2 0.4 0.6 0.8 1.0 FPR

0.0

0.2

0.4

0.6

0.8

1.0

TPR

Evaluation: 2017-2022, IR=50

fcNN (IR=50) AUC=0.9365 fcNN (IR=10) AUC=0.9416 Random AUC=0.5

- FIG. 8. Prediction of higher IR. The models are tasked with predicting whether concept pairs will receive at least 50 citations. Training is performed on data from 2014 to 2017, with evaluation conducted over intervals of 2, 3, 4, or 5 years (a 1-year interval lacks sufficient data). The blue line represents the performance of a fully connected neural network trained specifically for this task. In contrast, the red line represents a fully connected neural network (with identical architecture and training parameters) trained to solve the task for IR = 10 instead. Interestingly, the red model achieves slightly higher AUC values, indicating that predictions for higher impact ranges (IR = 50) benefit from training on more diverse data, including those from lower impact ranges.


mously large number of possibilities into a small number of personalized and targeted suggestions, which could inspire new ideas. In practical application, it will be useful to update the knowledge graph regularly, and train the machine learning models on the latest knowledge graph data, so it can better incorporate the latest trends and discoveries for its predictions.

Benchmarking different models and different time intervals – So far, we have only focused on a specific case: a training interval from 2016 to 2019 (3 years) and an evaluation interval from 2019 to 2022 (3 years). Additionally, we have primarily investigated the performance of feed-forward neural networks. Exploring other models and examining their predictive capabilities across various training and evaluation intervals could provide deeper insights into model performance. To do so, we expanded our study to include benchmarking on a small

dataset of 1 million pairs. This benchmarking incorporates the previously used fully connected neural network alongside additional models, including a transformer architecture [47, 48], random forest [49], and XGBoost [50].

The feed-forward neural network, implemented using PyTorch [51], consisted of three hidden layers, each with 600 neurons and ReLU activations [52], resulting in approximately 800,000 trainable parameters. Similarly, the transformer architecture [47, 48] also implemented via PyTorch, was designed with 4 layers, a hidden size of 128, 4 attention heads, and a feedforward dimension of 512, resulting in approximately 800,000 trainable parameters. Positional encodings were added to the input features. Both neural network models were trained using Adam optimizer [53] with a batch size of 2048 and a learning rate of 0.0001. The random forest classifier, implemented with scikit-learn [54], was trained with 300 trees, a mini-

mum of 25 samples required to split a node, and 10 samples per leaf. The XGBoost model was trained using up to 2000 boosting rounds, a learning rate of 0.01, and a maximum tree depth of 10. Hyperparameters for all models were selected via a hyperparameter search for a single benchmark task (training: 2016–2019, evaluation: 2019–2022, with IR = 10) and kept constant for all tasks.

In all tasks, the models are provided with 141 input features of a specific concept pair and have to predict whether this pair will receive more or fewer IR citations (IR = 10 or IR = 50) in certain future years. To achieve this, the four models are trained on 2-, 3-, and 4-year intervals and evaluated on intervals ranging from 1 to 5 years. For example, if the training interval spans 2 years and the evaluation interval spans 5 years, the models are trained using data from 2015 to 2017 to predict whether unconnected concept pairs will receive IR citations. They are then evaluated using 2017 data to make predictions for 2022. After training, the models are evaluated on 1 million concept pairs, predicting the likelihood of each pair receiving more than IR citations. These predictions are ranked (from high to low likelihood) and compared against the ground truth to compute the ROC curve and the AUC score, which measures prediction quality. As shown in Fig.6, the models achieve AUC values exceeding 90% in these tasks. In a slightly modified task, we train the models on the data from 2014 to 2017 and evaluate them from 2017 to 1-5 years into the future (2018 to 2022). This test analyzes how well the prediction perform for intervals on which the models have not been trained and how difficult it is to predict further into the future. As shown in Fig.7, the quality of the predictions indeed decreases for larger intervals.

In Fig.8, we show that models trained on smaller impact ranges can predict higher impact ranges even slightly better than those trained exclusively on higher impact ranges. This might be due to more diverse training data (there are many more examples of IR = 10 than of IR = 50, because many more concept pairs achieve at least 10 citations rather than 50). It might also be explained by a systematic drift in citation patterns between the years the models were trained and the years they are applied, potentially due to the growing number of overall citations. It will be very interesting in the future to explore and understand this effect further and to develop new ML methods that could leverage this dynamic.

All of our models use the same set of input features and do not directly access the full knowledge graph. Developing techniques that can leverage more general graph properties – such as automatically learning features or generating embeddings – would be an interesting avenue to explore. A related approach was demonstrated in a previous competition [4], where the task was to predict the future state of a knowledge graph. There, the graph’s edges represented co-occurrences of concepts in scientific papers. In contrast, the knowledge graph used in our study is more complex, with edges also weighted by the number of citations received by concept pairs. Explor-

ing more end-to-end approaches that integrate more information from the entire knowledge graph could reveal whether such methods can outperform the models and hand-crafted features demonstrated in this work.

### DISCUSSION

We show how to forecast the impact of future research topics. Although we view this as a significant step towards developing truly useful AI-driven assistants, achieving this goal requires numerous further advancements. Firstly, developing methods to extract more complex information from each paper will be crucial, for instance by employing hyper-graph structures that carry more information from each paper [55, 56], which has already been demonstrated to lead to exciting results in other domains [2, 57, 58]. The forecast itself could benefit from more genuine dynamical features that go beyond network snapshots from different years [59], or the application of dynamic word embedding [60]. This might also allow for the forecast of new concepts [61, 62] and their impact. Incorporating the recent dataset [63, 64] into our research could also allow us to explore more complex data structures than those used in our paper. Secondly, it will be interesting to approximate impact with metrics that go beyond citations – which is a crucial topic in computational sociology and the study of the science of science [1, 2]. Additionally, introducing metrics of surprise, as discussed in [65, 66], could serve as a complementary metric to citation prediction for ranking suggestions. Finally, while the suggestion of impactful new ideas might be a key component of future AI assistants, it will be crucial to study its relation to the scientific interest of working researchers [67].

### ACKNOWLEDGEMENTS

The authors thank Burak Gurlek for interesting discussions at the start of this project, and the organizers of OpenAlex, arXiv, bioRxiv, chemRxiv, and medRxiv for making scientific resources freely and readily accessible. X.G acknowledges the support from the Alexander von Humboldt Foundation.

Author Contributions X.G. and M.K. designed research; X.G. performed research and analyzed data; and X.G. and M.K. wrote the manuscript. Competing Interests The authors declare that they have no competing financial interests.

Data availability statement Data is accessible on Zenodo at https://doi.org/10.5281/zenodo.10692137

- [68]. Benchmark data used in our work is also available on Zenodo at https://doi.org/10.5281/zenodo.14527306
- [69]. Codes for this work are available on GitHub at https://github.com/artificial-scientist-lab/Impact4Cast.


Appendix A: Datasets for the knowledge graph

To compile a list of scientific concepts in natural science, we used metadata from four major preprint servers: arXiv, bioRxiv, medRxiv, and chemRxiv. The arXiv dataset can be directly downloaded from Kaggle, while metadata from bioRxiv, medRxiv, and chemRxiv are accessible through their APIs. The full methodology and codes are available on the GitHub: Impact4Cast. Our comprehensive dataset encompasses approximately 2.44 million papers, including 78,084 from arXiv’s physics.optics and quant-ph categories, which were specifically utilized for identifying domain concepts.

For edge generation, we used the OpenAlex database snapshot, available for download in OpenAlex bucket. More details can be found at the OpenAlex documentation site. The complete dataset occupies around 330 GB, expanding to approximately 1.6 TB when decompressed. Our interest was specifically in scientific journal papers that include publication time, title, abstract, and citation information. By focusing on these criteria, we managed to reduce the dataset to a more manageable gzip-compressed size of 68 GB, comprising around 92 million scientific papers. From these 92 million papers, 21 million contain at least two concepts of our final concept list and can therefore for an edge in the knowledge graph.

Appendix B: Details on concept and edge generation

From the preprint dataset of ∼2.44 million papers, we analyzed each article’s title and abstract using the RAKE algorithm.

RAKE works by proposing candidate key phrases from each sentence by splitting the sentence at punctuation marks and stop words. Let’s take the sentence: Recurrent neural networks have significantly improved the accuracy of image recognition in large-scale scientific collaboration networks. RAKE splits this into the candidate phrases Recurrent neural networks, improved, accuracy, image recognition, and large-scale scientific collaboration networks. Each individual word within these candidate phrases receives a score based on two metrics: its frequency (how often it occurs in candidate phrases; here only networks occurs twice, all others once) and its degree (the number of co-occurrences with other words in candidate phrases). For example, the word networks has a higher degree because it appears in multiple longer phrases, thus increasing its importance. The final keyword phrases are ranked based on the summed scores of their individual words, naturally favoring longer, meaningful phrases such as large-scale scientific collaboration networks or recurrent neural networks.

RAKE’s candidates are then used for subsequent analysis. We filtered out concepts to retain only those with two words that appeared in nine or more articles, and those with three or more words that appeared in six or more articles. This step significantly reduced the noise

from the RAKE-generated concepts, yielding a refined list of 726,439 relevant concepts. To further enhance the quality of the identified concepts, we developed a suite of automatic tools designed to identify and eliminate common, domain-independent errors often associated with RAKE. In addition, we conduct a manual review to identify and eliminate any inaccuracies in the concepts. The entire process, which included eliminating non-conceptual phrases, verbs, ordinal numbers, conjunctions, and adverbials, resulted in a full list of 368,825 concepts.

We note that our approach might result in similar or synonymous concepts appearing as separate key phrases due to slight variations or phrasing differences. Although multiple entries in the extracted concept list may represent essentially the same idea, synonymity can effectively be identified by leveraging structural information within the knowledge graph. Specifically, network cosine similarity between nodes (concepts) reveals the degree of similarity in their network neighborhoods, indicating semantic closeness. Practically, this can be utilized to enhance impact forecasting: when recommending new high-impact concept pairs, applying a cosine similarity threshold ensures that suggested pairs have sufficiently distinct meanings, thus avoiding redundancy from synonymous phrases.

We then specifically focused on articles within the physics.optics and quant-ph categories from arXiv to extract domain-specific concepts. Iterating this entire list of concepts to these domain-specific articles, we identified 87,741 relevant concepts. Employing our specially designed automated filtering tool for initial refinement and then conducting a thorough manual review to remove inaccuracies, we narrowed the list down to 37,960 high-quality, domain-specific concepts.

As an example, we show the extraction of concepts for the four papers used in Fig. 1:

- 1. Accurate and rapid background estimation in single-molecule localization microscopy using the deep neural network BGnet [29]: ‘super resolution reconstruction’, ‘neural network’, ‘single molecule tracking’, ‘deep neural net’, ‘deep neural network’, ‘localization microscopy’, ‘biological structure’, ‘point source’, ‘point spread function’, ‘single molecule localization microscopy’, ‘optical microscopy’, and ‘neural net’.
- 2. Machine learning for cluster analysis of localization microscopy data [30]: ‘neural network’, ‘supervised machine learning’, ‘spatial relation’, ‘localization microscopy’, ‘single molecule localization microscopy’, ‘neural net’, and ‘machine learning’.
- 3. Constraints on cosmic strings using data from the first Advanced LIGO observing run [31]: ‘phase transition’, ‘cosmic string’, ‘gravitational wave’, ‘cosmic microwave’, ‘cosmic microwave background’, ‘topological defect’, ‘string theory’, and ‘ring theory’.


4. Learning phase transitions from dynamics [32]: ‘neural network’, ‘recurrent network’, ‘time crystalline phase’, ‘phase transition’, ‘localization transition’, ‘spin chain’, ‘recurrent neural net’, ‘ct model’, ‘recurrent neural network’, ‘phase diagram’, ‘crystalline phase’, ‘neural net’, and ‘recurrent net’.

We created concept pairs, or edges, from the OpenAlex dataset, by detecting when domain-specific concepts co-occurred in paper titles or abstracts. This yielded 193,977,096 concept pairs (including multi-edges) across about 21 million papers. Each edge receives a time-stamp based on its paper’s publication date, converted to the number of days since January 1, 1990. The final full knowledge graph comprises 26,010,946 unique edges after merging multiple edges between the same concept pairs. The citation information for an edge includes the paper’s yearly citations from 2012 to 2023, alongside its total citation since publication. The OpenAlex dataset excludes yearly citations older than ten years, hence the focus on this specific ten-year time frame due to the absence of data prior to 2012. For edges formed by multiple papers, the edge weight combines the annual and total citations from all contributing papers.

Consider the edge formed by the concepts ‘single molecule localization microscopy’ and ‘neural net’, generated from paper p1 [29] published on January 7, 2020. The time-stamp for this edge is derived from the days elapsed since January 1, 1990. The citation metrics for this edge includes the total and yearly citations from each contributing paper. Paper p1 with 38 citations (cp1=38), contributes yearly citations represented as cp1(yi) for i=2023,2022,..., 2012, with actual values {5,8,16,9} for 2023 to 2020, and zeros for previous years, culminating in a citation sequence {5,8,16,9,0,0,0,0,0,0,0,0}. Similarly, paper p2 [30], published on March 20, 2020, with 43 citations (cp2=43), adds its yearly citations {6,16,14,7} for the same period (2023 to 2020). The aggregated citation data for this edge, combining cp1 and cp2, yields a total of 81 citations, with an annual citation sequence of {11,24,30,16,0,0,0,0,0,0,0,0}.

Appendix C: Details on training

Our neural network consists of six fully connected layers, which include four hidden layers with 600 neurons each. The network inputs are 141 features for each unconnected concept pair (vi,vj), denoted as pi,j = (p1i,j,p2i,j,...,p141i,j ), where each pi,j ∈ R. For instance, p1i,j and p2i,j represent the vertex degree of concepts vi and vj for the current year, y. Detailed feature description and feature generation code are available in GitHub: Impact4Cast.

In our training process for the year 2016 to predict impact in 2019, we prepared a dataset comprising approximately 689 million unconnected concept pairs. The

![image 11](Gu and Krenn_2025_Forecasting high-impact research topics via machine learning on evolving knowledge graphs_images/imageFile11.png)

- FIG. 9. Loss curves for one typical example. The training and test loss curves correspond to a fully connected neural network trained on data from 2017 to 2020, with an impact range (IR) of 10.

1 50 100 150 200

IR

- 102

- 103

- 104

- 105

- 106

- 107


Number(logscale)

0.0000

0.0005

0.0010

0.0015

0.0020

0.0025

0.0030

Ratio(Positive/Negative)

Evaluation 2019 --> 2022: Positive, Negative, and Ratio

Positive Number (>=IR)

Negative Number (<IR) Positive/Negative Ratio

- FIG. 10. Positive, negative samples, and their ratio in the 10M evaluation dataset (2019-2022) versus IR.


goal was to evaluate these pairs to determine whether their 3-year citation counts would have at least IR citations (IR is impact range) or not. From this extensive collection, we selected all positive samples (the 3-year citation counts are at least IR). An equivalent number of negative samples were then randomly chosen to match the size of the positive set. The refined dataset was subsequently divided, allocating 85% for training and 15% for testing purposes. For the evaluation dataset in 2019, which aims to predict the impact in 2022, we randomly selected 10 million unconnected pairs. Our neural network was trained using the Adam optimizer with a learning rate of 3×10−5 and a mini-batch size of 1000. In every training batch, we randomly chose an equal number of positive and negative samples from the training set. This approach was also applied to our 2019 training process for predictions into 2022, where the trained neural network is used for future forecasting. An example loss curve is shown in Fig.9. An example for the number of positive and negative cases of the evaluation dataset (for

ROC Curve with Thresholds (IR=10)

ROC Curve for IR=10, 50, 100

1.0

1.0

(FPR=0.3, TPR=0.96)

0.8

0.8

(FPR=0.1, TPR=0.83)

TruePositiveRate

TruePositiveRate

0.6

0.6

0.4

0.4

IR=10 (AUC = 0.94) IR=50 (AUC = 0.96) IR=100 (AUC = 0.95)

0.2

0.2

IR=10 (AUC = 0.94)

Random

0.0

0.0

0.0 0.2 0.4 0.6 0.8 1.0

0.0 0.2 0.4 0.6 0.8 1.0

False Positive Rate

False Positive Rate

- FIG. 11. ROC curve explanation. The ROC curve are plotted for the evaluation data in Fig.4, which illustrates the performance of binary classifiers discussed in our paper. On the left, for IR = 10, the area under the curve (AUC) is 0.94. The x-axis represents the False Positive Rate (FPR), while the y-axis represents the True Positive Rate (TPR). The curve demonstrates how the classifier’s performance changes with variations in the classification threshold, which determines whether a case is classified as Class 0 or Class 1. For instance, at a threshold that gives a classifier with FPR=0.1, the TPR is 0.83, and at FPR=0.3, the TPR is 0.96. Therefore, the ROC curve is more informative than just a single pair of FPR and TPR. On the right, the ROC curves for IR=10, 50, and 100 are shown.


the experiments in Fig.4) is shown in Fig.10. In Fig.11 we explain more details of the ROC curve, specifically its relation to false positive rate (FPR) and true positive rate (TPR).

The full dynamic knowledge graph, along with the data required for feature preparation and evaluation, was processed on an Intel Xeon Gold 6130 CPU with 1 TiB of RAM. However, it is not strictly necessary to have 1 TiB of RAM for this process with the relatively small concept list of 37,960; the high memory capacity was utilized for efficiency and to handle additional operations concurrently. The final domain knowledge graph in this work occupies approximately 23.12 GB of storage. It is worth noting that knowledge graphs built from larger concept lists will require more memory, as the data size and complexity increase.

The neural network training was conducted on a standard single GPU (Nvidia Quadro RTX 6000), with each training run for different impact ranges taking approximately 1.5 hours. For benchmarking, all models – except the transformer model – were run on a standard CPU (Intel Xeon Gold 6130) with memory usage below 15 GB. Each benchmarking task took roughly one hour to complete. The transformer model, however, was run on a single GPU (Nvidia Quadro RTX 6000), taking approximately 3 hours per task.

uses all 141 features, trained on 2016 dataset and impact range IR = 100. To explore the predictive ability of individual features, we trained separate neural networks on each feature using the same 2016 dataset, and then applied the 2019 evaluation dataset to these models. This resulted in 141 individual predictions, each from a network trained on a single feature. The features were ranked by their impact predictions, shown in the Fig. 12. Details of the features are shown in Tables I and I, and the corresponding documentation and source code are available at GitHub: Impact4Cast.

Appendix D: Individual feature’s predictive ability

In Fig. 4 (a), we observe an AUC score of 0.948 for the 2019 evaluation dataset with the neural network that

1.0

AUC=0.948

0.9

0.8

AUC Score

0.7

0.6

0.5

0 20 40 60 80 100 120 140 Sorted Feature

- FIG. 12. Neural network performance across individual features. The highest-performing four features are the Simpson similarity coefficient for the unconnected pair (u, v) across the years y, y−1, and y−2, and the cosine similarity coefficient for unconnected pairs (u, v) in year y (i.e., y=2016), with AUC scores of 0.8880, 0.8795, 0.8720, and 0.8683, respectively. In contrast, the lowest predictive three features are the average total citation count up to year y for vertex v, and the total citation count for the pair (u, v) up to years y − 1 and y − 2, with AUC scores of 0.5219, 0.5234, and 0.5285. Using all 141 features together leads to a significant improvement in the AUC score to 0.948, showing that the combination of all features works better.


#### TABLE I. Detailed description of all customized features for an unconnected concept pair (u, v) for the year y Type Feature Index Description

|node feature|0-5<br><br>|Number of neighbors for each node (u or v) until the year y, y−1, y−2 denoted as Nu,y, Nv,y, Nu,y−1, Nv,y−1, Nu,y−2, and Nv,y−2, ordered as indices 0–5.|
|---|---|---|
| |6-7|Number of new neighbors for each node (u or v) between year y−1 and y i.e., Nu,y−Nu,y−1 and Nv,y−Nv,y−1.|
| |8-9|Number of new neighbors for each node (u or v) between year y−2 and y i.e., Nu,y−Nu,y−2 and Nv,y−Nv,y−2.|
| |10-11|Rank of the number of new neighbors for each node (u or v) between year y−1 and y i.e., rank(Nu,y−Nu,y−1) and rank(Nv,y−Nv,y−1).|
| |12-13|Rank of the number of new neighbors for each node (u or v) between year y−2 and y i.e., rank(Nu,y−Nu,y−1) and rank(Nv,y−Nv,y−2).|
| |14-19<br><br>|PageRank scores of each node (u or v) until the year y, y−1, y−2 denoted and ordered as PRu,y, PRv,y, PRu,y−1, PRv,y−1, PRu,y−2 and PRv,y−2.|
|node citation feature|20-25<br><br>|Yearly citation for each node (u or v) in year y, y−1, y−2 denoted and ordered as Cu,y, Cv,y, Cu,y−1, Cv,y−1, Cu,y−2 and Cv,y−2.|
| |26-31<br><br>|Total citation for each node (u or v) since the first publication to the year y, y−1, and y−2 denoted and ordered as Ctu,y, Ctv,y, Ctu,y−1, Ctv,y−1, Ctu,y−2 and Ctv,y−2.|
| |32-37|Total citations for each node (u or v) in the last 3 years ending in the year y, y−1, and y−2 denoted and ordered as Ct∆3u,y, Ct∆3v,y, Ct∆3u,y−1, Ct∆3v,y−1, Ct∆3u,y−2, and Ct∆3v,y−2.|
| |38-43|Number of papers mentioning node u from the first publication to the year y, y−1, and y−2, similar for node v; denoted and ordered as Pnu,y, Pnv,y, Pnu,y−1, Pnv,y−1, Pnu,y−2, and Pnv,y−2|
| |44-49|Average yearly citations for each node (u or v) in the year y, y−1, y−2 denoted and ordered as Cmu,y, Cmv,y, Cmu,y−1, Cmv,y−1, Cmu,y−2 and Cmv,y−2 e.g., Cmu,y = Cu,y/Pnu,y|
| |50-55|Average total citations for each node (u or v) since the first publications to the years y, y−1, y−2; denoted and ordered as Ctmu,y, Ctmv,y, Ctmu,y−1, Ctmv,y−1, Ctmu,y−2 and Ctmv,y−2; e.g., Ctmu,y = Ctu,y/Pnu,y|
| |56-61<br><br>|Average total citations for each node (u or v) in the last 3 years ending in the year y, y−1, and y−2; denoted and ordered as Ctm∆3u,y, Ctm∆3v,y, Ctm∆3u,y−1, Ctm∆3v,y−1, Ctm∆3u,y−2 and Ctm∆3v,y−2; e.g., Ctm∆3u,y = Ct∆3u,y/Pnu,y|
| |62-63<br><br>|New citations for each node (u or v) between years y−1 and y i.e., Ctu,y−Ctu,y−1 and Ctv,y−Ctv,y−1.|
| |64-65<br><br>|New citations for each node (u or v) between years y−2 and y i.e., Ctu,y−Ctu,y−2 and Ctv,y−Ctv,y−2.|
| |66-67|Rank of the new citations for each node (u or v) between years y−1 and y i.e., rank(Cu,y−Cu,y−1) and rank(Cv,y−Cv,y−1).|
| |68-69<br><br>|Rank of the new citations for each node (u or v) between years y−2 and y i.e., rank(Cu,y−Cu,y−2) and rank(Cv,y−Cv,y−2).|
| |70-71<br><br>|Number of papers mentioning nodes u between years y−1 and y, similar for node v i.e., PRu,y − PRu,y−1 and PRv,y − PRv,y−1|
| |72-73|Number of papers mentioning nodes u between years y−2 and y, similar for node v i.e., PRu,y − PRu,y−2 and PRv,y − PRv,y−2|
| |74-75<br><br>|Rank of the number of papers mentioning nodes u between years y−1 and y, similar for node v; i.e., rank(PRu,y − PRu,y−1) and rank(PRv,y − PRv,y−1)|
| |76-77<br><br>|Number of papers mentioning nodes u between years y−2 and y, similar for node v i.e., rank(PRu,y − PRu,y−2) and rank(PRv,y − PRv,y−2)|


#### TABLE II. continued from previous page for Table. I Type Feature Index Description

|pair feature<br><br>|78-80|Number of shared neighbors between nodes u and v until the year y, y−1, y−2, denoted and ordered as Nsy, Nsy−1 and Nsy−2; e.g., Nsy = Nu,y ∩ Nv,y|
|---|---|---|
| |81-83|Geometric similarity coefficient for the pair (u, v) for the year y, y−1, and y−2 denoted and ordered as Geoy, Geoy−1, and Geoy−2; e.g., Geoy = Ns2y/(Nu,y × Nv,y).|
| |84-86|Cosine similarity coefficient for the pair (u, v) for the year y, y−1, y−2 denoted and ordered as Cosy, Cosy−1, and Cosy−2; e.g., Cosy = Geoy.<br><br>|
| |87-89<br><br>|Simpson coefficient for the pair (u, v) for the year y, y−1, y−2 denoted and ordered as Simy, Simy−1, and Simy−2; e.g., Simy = Nsy/ min(Nu,y, Nv,y).|
| |90-92<br><br>|Preferential attachment coefficient for the pair (u, v) for the year y, y−1, y−2 denoted and ordered as Prey, Prey−1, and Prey−2; e.g., Prey = Nu,y × Nv,y.|
| |93-95<br><br>|Sørensen–Dice coefficient for the pair (u, v) for the year y, y−1, y−2 denoted and ordered as Sory, Sory−1, and Sory−2; e.g., Sory = 2Nsy/(Nu,y + Nv,y).|
| |96-98<br><br>|Jaccard coefficient for the pair (u, v) for the year y, y−1, y−2 denoted and ordered as Jacy, Jacy−1, and Jacy−2; e.g., Jacy = Nsy/(Nu,y + Nv,y − Nsy).|
|pair citation feature|99-101|Ratio of the sum of citations received by nodes u and v until the year y to the total number of papers mentioning either concept; denoted and ordered as r1y, r1y−1, and r1y−2; e.g., r1y = (Ctu,y + Ctv,y)/(Pnu,y + Pnv,y).|
| |102-104|Ratio of the product of citations received by nodes u and v until the year y to the total number of papers mentioning either concept; denoted and ordered as r2y, r2y−1, and r2y−2; e.g., r2y = (Ctu,y × Ctv,y)/(Pnu,y + Pnv,y).|
| |105-107<br><br>|Sum of average citations received by nodes u and v in the year y, y−1, and y−2 denoted and ordered as sy, sy−1, and sy−2; e.g., sy = Cmu,y + Cmv,y.|
| |108-110|Sum of average total citations received by nodes u and v from the first publication to the year y, y−1, and y−2; denoted and ordered as sty, sty−1, and sty−2; e.g., sty = Ctmu,y +Ctmv,y.|
| |111-113<br><br>|Sum of the total citations received by nodes u and v in the last 3 years ending in the year y, y−1, and y−2; denoted and ordered as st∆3y , st∆3y−1, and st∆3y−2; e.g., st∆3y = Ct∆3u,y + Ct∆3v,y.|
| |114-116<br><br>|Sum of average total citations received by nodes u and v in the last 3 years ending in the year y, y−1, and y−2; denoted and ordered as stm∆3y , stm∆3y−1, and stm∆3y−2 e.g., stm∆3y = Ctm∆3u,y + Ctm∆3v,y.|
| |117-119|Minimum number of citations received by either node u or v in years y, y−1, and y−2; denoted and ordered as minCy, minCy−1, and minCy−2; e.g., minCy = min(Cu,y, Cv,y).|
| |120-122<br><br>|Maximum number of citations received by either node u or v in years y, y−1, and y−2; denoted and ordered as maxCy, maxCy−1, and maxCy−2; e.g., maxCy = max(Cu,y, Cv,y).|
| |123-125<br><br>|Minimum number of total citations received by nodes u and v from the first publication to the year y, y−1, and y−2; denoted and ordered as minCty, minCty−1, and minCty−2; e.g., minCty = min(Ctu,y, Ctv,y).|
| |126-128|Maximum number of total citations received by nodes u and v from the first publication to the year y, y−1, and y−2; denoted and ordered as maxCty, maxCty−1, and maxCty−2; e.g., maxCty = max(Ctu,y, Ctv,y).|
| |129-131|Minimum number of total citations received by nodes u and v in the last 3 years ending in the year y, y−1, and y−2; denoted and ordered as minCt∆3y , minCt∆3y−1, and minCt∆3y−2; e.g., minCt∆3y = min(Ct∆3u,y, Ct∆3v,y).|
| |132-134|Maximum number of total citations received by nodes u and v in the last 3 years ending in the year y, y−1, and y−2; denoted and ordered as maxCt∆3y , maxCt∆3y−1, and maxCt∆3y−2; e.g., maxCt∆3y = max(Ct∆3u,y, Ct∆3v,y).|
| |135-137|Minimum number of papers mentioning the node u or node v from the first publication to the year y, y−1, and y−2; denoted and ordered as minPny, minPny−1 and minPny−2; e.g., minPny = min(Pnu,y, Pnv,y).|
| |138-140|Maximum number of papers mentioning the node u or node v from the first publication to the year y, y−1, and y−2; denoted and ordered as maxPny, maxPny−1 and maxPny−2; e.g., maxPny = max(Pnu,y, Pnv,y).|


- [1] S. Fortunato, C. T. Bergstrom, K. Bo¨rner, J. A. Evans, D. Helbing, S. Milojevic´, A. M. Petersen, F. Radicchi, R. Sinatra, B. Uzzi, et al., Science of science, Science 359, eaao0185 (2018).
- [2] D. Wang and A.-L. Baraba´si, The science of science (Cambridge University Press, 2021).
- [3] L. Bornmann, R. Haunschild, and R. Mutz, Growth rates of modern science: a latent piecewise growth curve approach to model publication numbers from established and new literature databases, Humanities and Social Sciences Communications 8, 1 (2021).
- [4] M. Krenn, L. Buffoni, B. Coutinho, S. Eppel, J. G. Foster, A. Gritsevskiy, H. Lee, Y. Lu, J. P. Moutinho, N. Sanjabi, et al., Forecasting the future of artificial intelligence with machine learning-based link prediction in an exponentially growing knowledge network, Nature Machine Intelligence 5, 1326 (2023).
- [5] OpenAI, Gpt-4 technical report, arXiv:2303.08774

(2023).

- [6] Google, Gemini: a family of highly capable multimodal models, arXiv:2312.11805 (2023).
- [7] H. Touvron, L. Martin, K. Stone, P. Albert, A. Almahairi, Y. Babaei, N. Bashlykov, S. Batra, P. Bhargava, S. Bhosale, et al., Llama 2: Open foundation and finetuned chat models, arXiv:2307.09288 (2023).
- [8] Q. Wang, D. Downey, H. Ji, and T. Hope, Learning to generate novel scientific directions with contextualized literature-based discovery, arXiv:2305.14259 (2023).
- [9] A. Rzhetsky, J. G. Foster, I. T. Foster, and J. A. Evans, Choosing experiments to accelerate collective discovery, Proc. Natl. Acad. Sci. USA 112, 14569 (2015).
- [10] V. Martı´nez, F. Berzal, and J.-C. Cubero, A survey of link prediction in complex networks, ACM computing surveys (CSUR) 49, 1 (2016).
- [11] M. Krenn and A. Zeilinger, Predicting research trends with semantic and neural networks with an application in quantum physics, Proc. Natl. Acad. Sci. USA 117, 1910 (2020).
- [12] Challenge the impact factor, Nature Biomedical Engineering 1, 0103 (2017).
- [13] The many facets of impact, Nature Reviews Physics 6, 71 (2024).
- [14] A.-L. Baraba´si, The formula: The universal laws of success (Hachette UK, 2018).
- [15] M. R. Frank, D. Wang, M. Cebrian, and I. Rahwan, The evolution of citation graphs in artificial intelligence research, Nature Machine Intelligence 1, 79 (2019).
- [16] D. Wang, C. Song, and A.-L. Baraba´si, Quantifying longterm scientific impact, Science 342, 127 (2013).
- [17] Q. Ke, E. Ferrara, F. Radicchi, and A. Flammini, Defining and identifying sleeping beauties in science, Proc. Natl. Acad. Sci. USA 112, 7426 (2015).
- [18] R. Sinatra, D. Wang, P. Deville, C. Song, and A.-L. Baraba´si, Quantifying the evolution of individual scientific impact, Science 354, aaf5239 (2016).
- [19] L. Wu, D. Wang, and J. A. Evans, Large teams develop and small teams disrupt science and technology, Nature 566, 378 (2019).
- [20] J. W. Weis and J. M. Jacobson, Learning on knowledge graph dynamics provides an early warning of impactful research, Nature Biotechnology 39, 1300 (2021).


- [21] X. Bai, H. Liu, F. Zhang, Z. Ning, X. Kong, I. Lee, and F. Xia, An overview on evaluating and predicting scholarly article impact, Information 8, 73 (2017).
- [22] W. Xia, T. Li, and C. Li, A review of scientific impact prediction: tasks, features and methods, Scientometrics 128, 543 (2023).
- [23] L. Fu and C. Aliferis, Using content-based and bibliometric features for machine learning models to predict citation counts in the biomedical literature, Scientometrics 85, 257 (2010).
- [24] T. Yu, G. Yu, P.-Y. Li, and L. Wang, Citation impact prediction for scientific papers using stepwise regression analysis, Scientometrics 101, 1233 (2014).
- [25] C. Stegehuis, N. Litvak, and L. Waltman, Predicting the long-term citation impact of recent publications, Journal of informetrics 9, 642 (2015).
- [26] L. Weihs and O. Etzioni, Learning to predict citationbased impact measures, in 2017 ACM/IEEE joint conference on digital libraries (JCDL) (IEEE, 2017) pp. 1– 10.
- [27] X. Ruan, Y. Zhu, J. Li, and Y. Cheng, Predicting the citation counts of individual papers via a bp neural network, Journal of Informetrics 14, 101039 (2020).
- [28] G. He, Z. Xue, Z. Jiang, Y. Kang, S. Zhao, and W. Lu, H2cgl: Modeling dynamics of citation network for impact prediction, arXiv:2305.01572 (2023).
- [29] L. M¨ockl, A. R. Roy, P. N. Petrov, and W. Moerner, Accurate and rapid background estimation in singlemolecule localization microscopy using the deep neural network bgnet, Proc. Natl. Acad. Sci. USA 117, 60

(2020).

- [30] D. J. Williamson, G. L. Burn, S. Simoncelli, J. Griffi´e, R. Peters, D. M. Davis, and D. M. Owen, Machine learning for cluster analysis of localization microscopy data, Nature communications 11, 1493 (2020).
- [31] B. P. Abbott, R. Abbott, T. D. Abbott, F. Acernese, K. Ackley, C. Adams, T. Adams, P. Addesso, R. X. Adhikari, V. B. Adya, et al. (LIGO Scientific Collaboration and Virgo Collaboration), Constraints on cosmic strings using data from the first advanced ligo observing run, Phys. Rev. D 97, 102002 (2018).
- [32] E. van Nieuwenburg, E. Bairey, and G. Refael, Learning phase transitions from dynamics, Phys. Rev. B 98, 060301 (2018).
- [33] Y. Rong, Y. Hu, A. Mei, H. Tan, M. I. Saidaminov, S. I. Seok, M. D. McGehee, E. H. Sargent, and H. Han, Challenges for commercializing perovskite solar cells, Science 361, eaat8235 (2018).
- [34] E. J. Bergholtz, J. C. Budich, and F. K. Kunst, Exceptional topology of non-hermitian systems, Rev. Mod. Phys. 93, 015005 (2021).
- [35] G. Carleo, I. Cirac, K. Cranmer, L. Daudet, M. Schuld, N. Tishby, L. Vogt-Maranto, and L. Zdeborova´, Machine learning and the physical sciences, Rev. Mod. Phys. 91, 045002 (2019).
- [36] M. Krenn, J. Landgraf, T. Foesel, and F. Marquardt, Artificial intelligence and machine learning for quantum technologies, Phys. Rev. A 107, 010101 (2023).
- [37] H. Wang, T. Fu, Y. Du, W. Gao, K. Huang, Z. Liu, P. Chandak, S. Liu, P. Van Katwyk, A. Deac, et al., Scientific discovery in the age of artificial intelligence,


- Nature 620, 47 (2023).
- [38] A. V. Leeuwenhoek, Ii. microscopical observations on the blood vessels and membranes of the intestines. in a letter to the royal society from mr. anthony van leeuwenhoek, frs, Philosophical Transactions of the Royal Society of London 26, 53 (1709).
- [39] M. Krenn, R. Pollice, S. Y. Guo, M. Aldeghi, A. CerveraLierta, P. Friederich, G. dos Passos Gomes, F. Ha¨se, A. Jinich, A. Nigam, et al., On scientific understanding with artificial intelligence, Nature Reviews Physics 4, 761

(2022).

- [40] A. A. Salatino, F. Osborne, T. Thanapalasingam, and E. Motta, The cso classifier: Ontology-driven detection of research topics in scholarly articles, in Digital Libraries for Open Knowledge: 23rd International Conference on Theory and Practice of Digital Libraries, TPDL 2019, Oslo, Norway, September 9-12, 2019, Proceedings 23 (Springer, 2019) pp. 296–311.
- [41] S. Rose, D. Engel, N. Cramer, and W. Cowley, Automatic keyword extraction from individual documents, Text mining: applications and theory , 1 (2010).
- [42] J. Priem, H. Piwowar, and R. Orr, Openalex: A fullyopen index of scholarly works, authors, venues, institutions, and concepts, arXiv:2205.01833 (2022).
- [43] L. Page, S. Brin, R. Motwani, and T. Winograd, The pagerank citation ranking : Bringing order to the web, Stanford InfoLab (1999).
- [44] A.-L. Baraba´si, Network Science (Cambridge University Press, 2016).
- [45] Y. Lu, Predicting research trends in artificial intelligence with gradient boosting decision trees and time-aware graph neural networks, in 2021 IEEE International Conference on Big Data (Big Data) (IEEE, 2021) pp. 5809– 5814.
- [46] T. Fawcett, Roc graphs: Notes and practical considerations for researchers, Machine learning 31, 1 (2004).
- [47] D. Bahdanau, K. Cho, and Y. Bengio, Neural machine translation by jointly learning to align and translate, in International Conference on Learning Representations (ICLR) (2015).
- [48] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, L. u. Kaiser, and I. Polosukhin, Attention is all you need, in Advances in Neural Information Processing Systems, Vol. 30, edited by I. Guyon, U. V. Luxburg, S. Bengio, H. Wallach, R. Fergus, S. Vishwanathan, and R. Garnett (Curran Associates, Inc., 2017).
- [49] J. R. Quinlan, Induction of decision trees, Machine Learning 1, 81 (1986).
- [50] T. Chen and C. Guestrin, Xgboost: A scalable tree boosting system, in Proceedings of the 22nd acm sigkdd international conference on knowledge discovery and data mining (2016) pp. 785–794.
- [51] A. Paszke, S. Gross, F. Massa, A. Lerer, J. Bradbury,


- G. Chanan, T. Killeen, Z. Lin, N. Gimelshein, L. Antiga, A. Desmaison, A. Kopf, E. Yang, Z. DeVito, M. Raison, A. Tejani, S. Chilamkurthy, B. Steiner, L. Fang, J. Bai, and S. Chintala, Pytorch: An imperative style, highperformance deep learning library, in Advances in Neural Information Processing Systems 32 (NeurIPS), edited by
- H. Wallach, H. Larochelle, A. Beygelzimer, F. d'Alche´Buc, E. Fox, and R. Garnett (Curran Associates, Inc., 2019).


- [52] V. Nair and G. E. Hinton, Rectified linear units improve restricted boltzmann machines, in International conference on machine learning (ICML) (2010).
- [53] D. P. Kingma, Adam: A method for stochastic optimization, in International Conference on Learning Representations (ICLR) (2015).
- [54] F. Pedregosa, G. Varoquaux, A. Gramfort, V. Michel, B. Thirion, O. Grisel, M. Blondel, P. Prettenhofer, R. Weiss, V. Dubourg, et al., Scikit-learn: Machine learning in python, Journal of machine learning research 12, 2825 (2011).
- [55] F. Battiston, E. Amico, A. Barrat, G. Bianconi, G. Ferraz de Arruda, B. Franceschiello, I. Iacopini, S. K´efi, V. Latora, Y. Moreno, et al., The physics of higher-order interactions in complex systems, Nature Physics 17, 1093

(2021).

- [56] A. V. Belikov, A. Rzhetsky, and J. Evans, Prediction of robust scientific facts from literature, Nature Machine Intelligence 4, 445 (2022).
- [57] J. G. Foster, A. Rzhetsky, and J. A. Evans, Tradition and innovation in scientists’ research strategies, American Sociological Review 80, 875 (2015).
- [58] J. Sourati and J. A. Evans, Accelerating science with human-aware artificial intelligence, Nature Human Behaviour 7, 1682 (2023).
- [59] G. H. Nguyen, J. B. Lee, R. A. Rossi, N. K. Ahmed, E. Koh, and S. Kim, Continuous-time dynamic network embeddings, in Companion proceedings of the the web conference 2018 (2018) pp. 969–976.
- [60] F. Frohnert, X. Gu, M. Krenn, and E. van Nieuwenburg, Discovering emergent connections in quantum physics research via dynamic word embeddings, Machine Learning: Science and Technology 10.1088/2632-2153/adb00a

(2025).

- [61] A. A. Salatino, F. Osborne, and E. Motta, How are topics born? understanding the research dynamics preceding the emergence of new areas, PeerJ Computer Science 3, e119 (2017).
- [62] A. A. Salatino, F. Osborne, and E. Motta, Augur: forecasting the emergence of new research topics, in Proceedings of the 18th ACM/IEEE on joint conference on digital libraries (2018) pp. 303–312.
- [63] Z. Lin, Y. Yin, L. Liu, and D. Wang, Sciscinet: A largescale open data lake for the science of science research, Scientific Data 10, 315 (2023).
- [64] J. Li, Y. Yin, S. Fortunato, and D. Wang, A dataset of publication records for nobel laureates, Scientific Data 6, 33 (2019).
- [65] J. G. Foster, F. Shi, and J. Evans, Surprise! measuring novelty as expectation violation, SocArXiv 2t46f (2021).
- [66] F. Shi and J. Evans, Surprising combinations of research contents and contexts are related to impact and emerge with scientific outsiders from distant disciplines, Nature Communications 14, 1641 (2023).
- [67] X. Gu and M. Krenn, Interesting scientific idea generation using knowledge graphs and llms: Evaluations with 100 research group leaders, arXiv:2405.17044 (2024).
- [68] X. Gu, Impact4cast: Forecasting high-impact research topics via machine learning on evolving knowledge graphs [data set], zenodo, https://doi.org/10.5281/zenodo.10692137 (2024).
- [69] X. Gu, Benchmark dataset for impact4cast: Forecasting high-impact research topics via machine learning on evolving knowledge graphs [data set]. zenodo.,


#### https://doi.org/10.5281/zenodo.14527306 (2024).

