# SCICAP: Generating Captions for Scientiﬁc Figures

Ting-Yao (Edward) Hsu, C. Lee Giles, Ting-Hao ‘Kenneth’ Huang Pennsylvania State University University Park, PA, USA {txh357, clg20, txh710}@psu.edu

## Abstract

Researchers use ﬁgures to communicate rich, complex information in scientiﬁc papers. The captions of these ﬁgures are critical to conveying effective messages. However, low-quality ﬁgure captions commonly occur in scientiﬁc articles and may decrease understanding. In this paper, we propose an end-to-end neural framework to automatically generate informative, high-quality captions for scientiﬁc ﬁgures. To this end, we introduce SCICAP,1 a largescale ﬁgure-caption dataset based on computer science arXiv papers published between 2010 and 2020. After pre-processing – including ﬁgure-type classiﬁcation, sub-ﬁgure identiﬁcation, text normalization, and caption text selection – SCICAP contained more than two million ﬁgures extracted from over 290,000 papers. We then established baseline models that caption graph plots, the dominant (19.2%) ﬁgure type. The experimental results showed both opportunities and steep challenges of generating captions for scientiﬁc ﬁgures.

## 1 Introduction

Researchers use ﬁgures to explain complex concepts or show critical results. In scholarly articles, ﬁgure captions are critical to get the message across effectively. Ones that are too generic (e.g., “Results of Experiment A.”) or poorly written (e.g., “Relations between X and Y.”) represent missed opportunities to explain scientiﬁc narratives to readers. Unfortunately, such low-quality captions still occur in published scientiﬁc articles. This paper aims to develop automatic ﬁgure-captioning models that generate high-quality captions for ﬁgures and charts in scientiﬁc papers (Figure 1).

Our motivation is two-fold. First, we aim to help researchers write better captions for the ﬁgures and charts in their papers. Automatic caption models trained on informative, high-quality captions can

1SCICAP is available at: https://github.com/ tingyaohsu/SciCap

![image 1](Hsu et al._2021_SciCap Generating Captions for Scientific Figures_images/imageFile1.png)

Figure 1: The ﬁgure captioning model takes a scientiﬁc ﬁgure (e.g., a graph plot) as input and generate captions that describes the ﬁgure.

suggest better captions. Second, the proposed technology can make scientiﬁc charts and ﬁgures more accessible to blind or visually impaired readers. Researchers have developed technologies to assist the blind to navigate graphical content, such as data visualization charts (Swaminathan et al., 2014), printed physical maps (Swaminathan et al., 2016), 3D chemical diagrams (Bernareggi et al., 2019), and images on social media (Wu et al., 2017; Salisbury et al., 2017). However, only a few prior works focused on scientiﬁc ﬁgures. An image-captioning model specialized for scientiﬁc ﬁgures can improve the narration of scientiﬁc articles for the blind even when the original caption is unhelpful.

To this end, we introduce SCICAP, a large-scale image-captioning dataset that contains real-world scientiﬁc ﬁgures and captions. SCICAP was constructed using computer science papers collected and released by arXiv. With pre-processing complete – including ﬁgure-type classiﬁcation, subﬁgure identiﬁcation, text normalization, and caption text selection – SCICAP contained more than two million ﬁgures extracted from over 290,000 papers. We then established baseline models that caption graph plots, the dominant (19.2%) ﬁgure type. The experimental results showed both exciting opportunities and steep challenges of generating captions for scientiﬁc ﬁgures.

## 2 Related Work

One of the few prior works attempting to caption scientiﬁc ﬁgures was by Chen et al. (2019a; 2019b;

3258

Findings of the Association for Computational Linguistics: EMNLP 2021, pages 3258–3264 November 7–11, 2021. ©2021 Association for Computational Linguistics

2020). They created FigCAP, a caption-ﬁgure pair corpus where the ﬁgures are synthesized, and used an LSTM model with an attention mechanism to produce captions. FigCAP was built on research that aimed to analyze ﬁgure content automatically, including Figure-Seer (Siegel et al., 2016), FigureQA (Kahou et al., 2017), and DVQA (Kaﬂe et al., 2018). DVQA and FigureQA were both made using synthetic ﬁgures; FigureSeer contained over 60,000 ﬁgures across seven ﬁgure types extracted from research papers. Meanwhile, Qian et al. (2020) proposed a set of “caption units” (such as Title, Label Name, Min/Max, etc.) that are important to include in a caption of scientiﬁc ﬁgures; they created a model, FigJAM, to produce such units (Qian et al., 2021). Also relevant is the “data-to-caption” work, which takes a chart’s source data table and metadata as input to generate a caption (Obeid and Hoque, 2020; Spreaﬁco and Carenini, 2020). These models generate captions based on data tables, not the ﬁgures.

Differences Between Synthetic and Real-World Captions. Most prior work has tried to generate captions for scientiﬁc ﬁgures using synthetic images and texts (Chen et al., 2019a,b, 2020; Kahou et al., 2017). However, synthetic captions tend to be generic and describe features without conveying higher-level insights, for example, “This is a line plot. It contains 6 categories. Dark Magenta has the lowest value. Lawn Green has the highest value.” (example from FigCAP.) Human-written captions, on the other hand, tend to highlight the meaningful parts of the ﬁgure and bring more context, for example: “Train loss curve with respect to optimization steps. With prior coarse-tuning on NLI data, convergence becomes much faster and easier.” [example from (Jin et al., 2020)].

## 3 Constructing SCICAP Dataset

This section describes the process that massages real-world ﬁgure-caption data into an appropriate easy-to-use format for the NLP community. This data-processing procedure was developed iteratively and empirically.

Step 1: Data Acquisition and Pre-processing. Data acquisition is a fundamental challenge for constructing a public scientiﬁc ﬁgure-caption dataset. Although there is a vast number of scientiﬁc papers, they are not all easy to access. SCICAP is based

on the arXiv dataset (Clement et al., 2019).2 The arXiv dataset is licensed under CC-0, which grants remake and republish rights. It contains a repository of 1.7 million articles with relevant features, such as article titles, authors, categories, abstracts, full-text PDFs, and more.

We ﬁrst downloaded all the scholarly articles from the arXiv dataset and froze the date on Dec 22, 2020 (a total of 1,921,287 papers). SCICAP does not include any papers published after this date. We further narrowed our dataset to papers published between 2010 and 2020 in computer science (cs.) and machine learning (stat.ML) topics, which numbered 295,028 papers. We did not use these papers’ “source ﬁles,” which might contain the original LaTeX and ﬁgure ﬁles. Not all papers come with source ﬁles; some source ﬁles have complex dependencies that are hard to parse.

- Step 2: Figure-Caption Pair Extraction. We then used PDFFigures 2.0 (Clark and Divvala,

2016) to extract the ﬁgures from papers in our paper collection. PDFFigures 2.0 is a Scala-based tool created to extract ﬁgures, captions, tables, and section titles from scholarly documents, with a focus on the computer science domain. In addition to the ﬁgures’ images and captions, the tool also extracted all the text snippets inside the ﬁgures, such as legends, X-Y labels, and titles. The extracted information can be used to boost the performance of image-captioning models. This step resulted in 295,028 papers and 2,170,719 ﬁgures.

- Step 3: Figure Type Classiﬁcation. Given the high diversity in the ﬁgure types included in scientiﬁc articles, we did not aim to create a single captioning model for all types of ﬁgures. Instead, we aimed to create captioning models specialized for one particular ﬁgure type. We used an automatic ﬁgure type classiﬁer (Siegel et al., 2016) to classify ﬁgure type in SCICAP. This pre-trained classiﬁer can identify seven types of ﬁgures: graph plots, ﬂowcharts (also called node diagrams), equations (also called algorithms), bar plots, scatter plots, tables, and “other.” Its reported accuracy is 86% over 60,000 samples (Siegel et al., 2016).


According to the classiﬁer’s prediction, out of 2,170,719 ﬁgures, 19.2% (416,804) are graph plots, 23.6% (511,984) are tables,3 5.9% (127,197) are

- 2arXiv Dataset on Kaggle: https://www.kaggle. com/Cornell-University/arxiv
- 3In this work, tables are not considered to be ﬁgures due to drastically different visual features and contents.


equations (including algorithms and pseudo codes), 8.5% (185,398) are ﬂowcharts, 2.0% (44,052) are scatter plots, 4.7% (101,146) are bar charts, and 36.1% (784,138) are “other.” In SCICAP, we only focus on graph plots, which have the highest classiﬁcation performance (Siegel et al., 2016) and are also the most common ﬁgure type.

- Step 4: Removing Figures with Subﬁgures. Many scientiﬁc ﬁgures contain subﬁgures. For example, in our pilot study (Section 3.1), 35.72% of overall scientiﬁc ﬁgures had subﬁgures. SCICAP focuses on generating captions for single ﬁgures, so we removed ﬁgures with subﬁgures from the dataset. We ﬁrst used handcrafted rules to identify captions that explicitly mention or refer to subﬁgures [for example, (a), a), (b), b), (1), 1),

(2), 2) ... etc.]. Furthermore, we also used FigureSeparator (Tsutsui and Crandall, 2017) to ﬁlter ﬁgures with subﬁgures out of our collection. FigureSeparator is a CNN-based model that separates compound ﬁgures in the ImageCLEF Medical dataset with 85.9% accuracy.

Of 416,804 graph plots identiﬁed in Step 3, the rule-based approach yielded 352,719 graph plots, and the FigureSeparator further narrowed the collection down to 133,543 ﬁgures. An estimated

- 32.04% of the graph plots did not have subﬁgures.


- Step 5: Text Normalization. We used NLTK (Loper and Bird, 2002) for tokenization and converted all the text to lowercase. We also removed the ﬁgure numbers, such as “Figure 1:” or “Fig. 1:”, and only kept the main caption text. The following two text normalization strategies were then applied:

- • Basic Normalization: We replaced all the numbers (e.g., 0, -0.2, 3.44%, 1,000,000) with [NUM].
- • Advanced Normalization: We created regular expressions to identify equations in captions and replaced them with [EQUATION]. We also replaced all the text spans enclosed by any types of bracket pairs, including {}, [], and (), with [BRACKET].


- Step 6: Target Caption Text Selection. SCICAP provides three different data collections, each sampled using different strategies:


• First Sentence (133,543 Figures): This collection includes all the ﬁgures. For each ﬁgure

Figure Type Classiﬁcation (Class = Graph Plot) Approach P R F Acc (Siegel et al., 2016) .90 .83 .87 .95 Non-Subﬁgure Figure Classiﬁcation (For ﬁgures labeled as graph plots in Step 3.) Approach P R F Acc Rule-Based .54 .95 .69 .59 FigureSeparator .98 .66 .79 .83 Rule-Based+FigureSeparator .98 .62 .76 .81

Table 1: The tools used to construct SCICAP evaluated on 1,926 labeled images. For ﬁgure type classiﬁcation, the overall performance over graph plots was reliable. Regarding identifying the graph plots (as labeled automatically in Step 3) that do not contain subﬁgures, FigureSeparator achieved an exceptionally high precision.

included, this collection only includes the ﬁrst sentence of the caption.

- • Single-Sentence Caption (94,110 Figures): This collection includes the complete caption of only the ﬁgures with a one-sentence caption. Of the graph plots, 70.47% had a one-sentence caption.
- • Caption with No More than 100 Words (131,319 Figures): This collection includes the complete caption of only the ﬁgures whose captions contained no more than one hundred tokens (punctuation marks included). In this collection, a caption contains 1.66 sentences on average (SD=1.07).


On average, with advanced normalization (Step 4), a sentence in the “First Sentence” collection contains 23.19 tokens (SD=20.86); a sentence in the “Single-Sentence Caption” collection contains 14.05 tokens (SD=8.15); and a sentence in the “Caption with No More Than 100 Words” collection contains 22.04 tokens (SD=17.44).

Note that we ﬁrst created the 80/10/10 train/val/test data split for the entire corpus and then proceeded with the caption selection step. This procedure ensured that we used the identical set of ﬁgures to construct each collection’s test set; the same applied to their training and validation sets. 3.1 Data Analysis and Quality Measurement

To evaluate the quality of our data cleaning and processing pipeline, we randomly sampled 2,000 ﬁgures from the original arXiv dataset, and one

author manually labelled each ﬁgure’s ﬁgure type and whether it contained subﬁgures (Yes/No).4 Of these 2,000 ﬁgures, 1,926 ﬁgures had no extraction errors, and were included in our follow-up calculation. As for types, 20.35% of the ﬁgures were graph plots, 4.1% were bar charts, and 3.11% were scatter plots.5 In terms of subﬁgures, 237 out of 1,926 ﬁgures (35.72%) contained subﬁgures:

- 33.14% of these ﬁgures contained graph plots as subﬁgures, 5.81% contained bar charts, and 6.83% contained scatter plots.


We used these 1,926 labeled images to evaluate the tools we employed in constructing SCICAP. Table 1 shows the results. For the ﬁgure type classiﬁcation, the overall performance over graph plots were reliable. Regarding identifying the graph plots (as labeled automatically in Step 3) that do not contain subﬁgures, FigureSeparator had an exceptionally high precision.

## 4 Experimental Results

To examine the feasibility and challenges of creating an image-captioning model for scientiﬁc ﬁgures, we established several baselines and tested them using SCICAP. The caption quality was measured by BLEU-4 (Papineni et al., 2002), using the test set of the corresponding data collection as a reference. Figure 2 shows some example outputs.

Baseline Model. We used a classical imagecaptioning model, CNN+LSTM architecture, as our baseline (Xu et al., 2015). The pre-trained ResNet-101 (He et al., 2016) was used as the image encoder to represent a ﬁgure as a 2048-dimension vector. This image vector was then fed into a dense layer to ﬁt the dimension of the word-embedding and the LSTM decoder where the word-embedding and LSTM hidden layer size were all 512. A global attention mechanism was added to the LSTM decoder to better model the context (Luong et al., 2015). The LSTM decoder took the image vector as the initial state and generate captions.

We designed three variations of the baseline models, Vision-only, Vision+Text, and Text-only.

- 4To validate the label quality, we had three graduate students label 100 ﬁgures, respectively. On average, they agreed with 97% of our subﬁgure labels. For the ﬁgures without subﬁgures, they agreed with our ﬁgure type labels 82.17% of the time. For the ﬁgures with subﬁgures, they agreed with at least one of our type labels 86.56% of the time.
- 5A ﬁgure might contain subﬁgures of different types (e.g., a bar chart accompanied by a graph plot.) For each ﬁgure, we took a multi-class labeling strategy that exhaustively labels all distinct types of its subﬁgures.


First Sentence Subﬁg Filter Norm.

Vocab Size

#Fig.

BLEU-4

Rule FigSep B. A.

416,804 30,776 .0259 352,719 24,355 .0236

12,666 .0224 133,543

11,946 .0219 Single-Sentence Caption Only

Subﬁg Filter Norm. Rule FigSep B. A.

Vocab Size

#Fig.

BLEU-4

247,649 21,765 .0291 218,655 17,685 .0228

9,760 .0234 92,021

9,232 .0207 Caption with <= 100 Words

Subﬁg Filter Norm. Rule FigSep B. A.

Vocab Size

#Fig.

BLEU-4

395,024 37,885 .0231 341,350 30,316 .0098

15,642 .0173 132,120

14,974 .0172

Table 2: The baseline model’s performance on SCICAP, using Vision-Only features. Models trained on the Single-Sentence Caption collection performed the best. The low BLEU-4 scores indicate that more research is needed to reliably generate captions for scientiﬁc ﬁgures. (The vocabulary sizes were calculated after dropping words with a frequency below 5.)

The text information was the titles, legends, and X-Y labels extracted from the ﬁgures (Step 2 in Section 3). Another LSTM was used as a text encoder to encode text information into a vector. For the Vision+Text variation, we concatenated the image vector and the text vector together and fed it into the LSTM decoder for caption generation. The Text-only variation only took the text vector as the feature for the LSTM decoder.

Experimental Setups. We trained the baseline models using an 80/10/10 train/val/test data split. The models were trained by minimizing a crossentropy loss with a doubly stochastic regularization (Xu et al., 2015) using Adam (Kingma and Ba, 2014). The weights of the pretrained ResNet-101 image encoder were partially frozen so that only convolutional blocks 2 through 4 were ﬁne-tuned throughout the training process (Yosinski et al.,

![image 2](Hsu et al._2021_SciCap Generating Captions for Scientific Figures_images/imageFile2.png)

Figure 2: Example outputs of the baseline models trained and tested on the Single-Sentence Caption Only collection. Intensive research will be needed to create models that can caption scientiﬁc ﬁgures reliably. [Figure sources: (1) (Zhang et al., 2020), (2) (Baswana et al., 2017), and (3) (Brubaker et al., 2015).]

Data Collection Feature BLEU-4

Vision Only .0219 Vision+Text .0205 Text Only .0213

First Sentence

Vision Only .0207 Vision+Text .0202 Text Only .0212

Single-Sent Caption

Vision Only .0172 Vision+Text .0168 Text Only .0165

Caption w/ <=100 words

Table 3: The experimental results of models using Vision-Only, Text-Only, and Vision+Text features. Vision-Only and Text-Only features yielded similar performance. (All the subﬁgure-ﬁltering and textnormalization steps were applied.)

2014). We empirically set the hyper-parameters by observing the performance gain on the validation set. Hyper-parameters ended up being used were a dropout rate of 0.5; a batch size of 16/32; a learning rate of 4e-4 with a decay factor of 0.8 when there was no improvement for 8 epochs. The models were trained until there was no improvement for 20 epochs. We kept the model with the highest BLEU-4 score on the validation set for testing.

Results. We trained the models on each data collection with varying levels of data ﬁltering and text normalization. Table 2 shows the results. Among the three data collections, the models trained on the

single-sentence captions performed the best. This might be because the Single-Sentence Caption collection, which is a subset of the First Sentence collection, had the smallest vocabulary size.

Effects of Text Normalization. Our experiments did not show the clear beneﬁts of normalizing text to the resulting BLEU-4 scores. We will explore other methods to normalize text, for example, using advanced techniques to identify equations in text (Mali et al., 2020; Mansouri et al., 2020).

Effects of Text and Vision Features. We also used Vision-Only, Text-Only, and Text+Vision features to develop models (Table 3). Vision-Only and Text-Only features yielded similar performance. Furthermore, the models performed slightly worse when training on combined features.

## 5 Conclusion and Future Work

This paper introduces SCICAP, a large-scale imagecaptioning dataset that contains real-world scientiﬁc ﬁgures and captions. SCICAP was constructed using more than two million images from over 290,000 papers collected and released by arXiv. We also established several image-captioning baselines, showing the feasibility and challenges of generating captions for scientiﬁc ﬁgures. In the future, we will explore approaches to improve caption quality, such as taking advantage of large pre-trained language models (Beltagy et al., 2019), or using information in paper’s full text to boost performance.

## Ethical Considerations

Data Licensing. The arXiv dataset uses the CC0 1.0 Universal (CC0 1.0) Public Domain Dedication license,6 which grants permission to remix, remake, annotate, and publish the data.

Potential Biases of Language Technologies. We are aware that language technologies trained on a “standard” or mainstream variety of a language (in our case, English) favor the popular variety and harms people using varieties with fewer speakers. For example, standard automatic speech recognition trained on Dutch speeches results in 10-15% higher error rates on Flemish Dutch than on “standard” Dutch (Feng et al., 2021).

## Acknowledgments

We thank Chieh-Yang Huang, Hua Shen, and Chacha Chen for helping with the data annotation. We thank Chieh-Yang Huang for the feedback and strong technical support. We also thank the anonymous reviewers for their constructive feedback. This research was partially supported by the Seed Grant (2020) from the College of Information Sciences and Technology (IST), Pennsylvania State University.

## References

Surender Baswana, Ayush Goel, and Shahbaz Khan. 2017. Incremental dfs algorithms: a theoretical and experimental study. arXiv preprint arXiv:1705.02613.

Iz Beltagy, Kyle Lo, and Arman Cohan. 2019. Scibert: Pretrained language model for scientiﬁc text. In EMNLP.

Cristian Bernareggi, Dragan Ahmetovic, and Sergio Mascetti. 2019. µgraph: Haptic exploration and editing of 3d chemical diagrams. In The 21st International ACM SIGACCESS Conference on Computers and Accessibility, pages 312–317. ACM.

Marcus A Brubaker, Ali Punjani, and David J Fleet. 2015. Building proteins in a day: Efﬁcient 3d molecular reconstruction. arXiv preprint arXiv:1504.03573.

Charles Chen, Ruiyi Zhang, Sungchul Kim, Scott Cohen, Tong Yu, Ryan Rossi, and Razvan Bunescu. 2019a. Neural caption generation over ﬁgures. In Adjunct Proceedings of the 2019 ACM International

6CC 1.0: https://creativecommons.org/ publicdomain/zero/1.0/

Joint Conference on Pervasive and Ubiquitous Computing and Proceedings of the 2019 ACM International Symposium on Wearable Computers, UbiComp/ISWC ’19 Adjunct, pages 482–485, New York, NY, USA. ACM.

Charles Chen, Ruiyi Zhang, Eunyee Koh, Sungchul Kim, Scott Cohen, and Ryan Rossi. 2020. Figure captioning with relation maps for reasoning. In Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision, pages 1537–1545.

Charles Chen, Ruiyi Zhang, Eunyee Koh, Sungchul Kim, Scott Cohen, Tong Yu, Ryan Rossi, and Razvan Bunescu. 2019b. Figure captioning with reasoning and sequence-level training. arXiv preprint arXiv:1906.02850.

Christopher Clark and Santosh Divvala. 2016. Pdfﬁgures 2.0: Mining ﬁgures from research papers. In 2016 IEEE/ACM Joint Conference on Digital Libraries (JCDL), pages 143–152. IEEE.

Colin B. Clement, Matthew Bierbaum, Kevin P. O’Keeffe, and Alexander A. Alemi. 2019. On the use of arxiv as a dataset.

Siyuan Feng, Olya Kudina, Bence Mark Halpern, and Odette Scharenborg. 2021. Quantifying bias in automatic speech recognition. arXiv preprint arXiv:2103.15122.

Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun. 2016. Deep residual learning for image recognition. In Proceedings of the IEEE conference on computer vision and pattern recognition, pages 770– 778.

Di Jin, Shuyang Gao, Jiun-Yu Kao, Tagyoung Chung, and Dilek Hakkani-tur. 2020. Mmm: Multi-stage multi-task learning for multi-choice reading comprehension. In Proceedings of the AAAI Conference on Artiﬁcial Intelligence, volume 34, pages 8010–8017.

Kushal Kaﬂe, Brian Price, Scott Cohen, and Christopher Kanan. 2018. Dvqa: Understanding data visualizations via question answering. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition, pages 5648–5656.

Samira Ebrahimi Kahou, Vincent Michalski, Adam Atkinson, Ákos Kádár, Adam Trischler, and Yoshua Bengio. 2017. Figureqa: An annotated ﬁgure dataset for visual reasoning. arXiv preprint arXiv:1710.07300.

Diederik P Kingma and Jimmy Ba. 2014. Adam: A method for stochastic optimization. arXiv preprint arXiv:1412.6980.

Edward Loper and Steven Bird. 2002. Nltk: The natural language toolkit. In In Proceedings of the ACL Workshop on Effective Tools and Methodologies for Teaching Natural Language Processing and Computational Linguistics. Philadelphia: Association for Computational Linguistics.

Minh-Thang Luong, Hieu Pham, and Christopher D Manning. 2015. Effective approaches to attentionbased neural machine translation. arXiv preprint arXiv:1508.04025.

Parag Mali, Puneeth Kukkadapu, Mahshad Mahdavi, and Richard Zanibbi. 2020. Scanssd: Scanning single shot detector for mathematical formulas in pdf document images. arXiv preprint arXiv:2003.08005.

Behrooz Mansouri, Anurag Agarwal, Douglas Oard, and Richard Zanibbi. 2020. Finding old answers to new math questions: the arqmath lab at clef 2020. In European Conference on Information Retrieval, pages 564–571. Springer.

Jason Obeid and Enamul Hoque. 2020. Chart-to-text: Generating natural language descriptions for charts by adapting the transformer model. In Proceedings of the 13th International Conference on Natural Language Generation, pages 138–147.

Kishore Papineni, Salim Roukos, Todd Ward, and WeiJing Zhu. 2002. Bleu: a method for automatic evaluation of machine translation. In Proceedings of the 40th annual meeting of the Association for Computational Linguistics, pages 311–318.

Xin Qian, Eunyee Koh, Fan Du, Sungchul Kim, and Joel Chan. 2020. A formative study on designing accurate and natural ﬁgure captioning systems. In Extended Abstracts of the 2020 CHI Conference on Human Factors in Computing Systems, pages 1–8.

Xin Qian, Eunyee Koh, Fan Du, Sungchul Kim, Joel Chan, Ryan A Rossi, Sana Malik, and Tak Yeon Lee. 2021. Generating accurate caption units for ﬁgure captioning. In Proceedings of the Web Conference 2021, pages 2792–2804.

Elliot Salisbury, Ece Kamar, and Meredith Ringel Morris. 2017. Toward scalable social alt text: Conversational crowdsourcing as a tool for reﬁning vision-tolanguage technology for the blind. In Fifth AAAI Conference on Human Computation and Crowdsourcing.

Noah Siegel, Zachary Horvitz, Roie Levin, Santosh Divvala, and Ali Farhadi. 2016. Figureseer: Parsing result-ﬁgures in research papers. In European Conference on Computer Vision, pages 664–680. Springer.

Andrea Spreaﬁco and Giuseppe Carenini. 2020. Neural data-driven captioning of time-series line charts. In Proceedings of the International Conference on Advanced Visual Interfaces, pages 1–5.

Saiganesh Swaminathan, Thijs Roumen, Robert Kovacs, David Stangl, Stefanie Mueller, and Patrick Baudisch. 2016. Linespace: A sensemaking platform for the blind. In Proceedings of the 2016 CHI Conference on Human Factors in Computing Systems, pages 2175–2185. ACM.

Saiganesh Swaminathan, Conglei Shi, Yvonne Jansen, Pierre Dragicevic, Lora A Oehlberg, and JeanDaniel Fekete. 2014. Supporting the design and fabrication of physical visualizations. In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, pages 3845–3854. ACM.

Satoshi Tsutsui and David J Crandall. 2017. A data driven approach for compound ﬁgure separation using convolutional neural networks. In 2017 14th IAPR International Conference on Document Analysis and Recognition (ICDAR), volume 1, pages 533– 540. IEEE.

Shaomei Wu, Jeffrey Wieland, Omid Farivar, and Julie Schiller. 2017. Automatic alt-text: Computergenerated image descriptions for blind users on a social network service. In Proceedings of the 2017 ACM Conference on Computer Supported Cooperative Work and Social Computing, pages 1180–1192. ACM.

Kelvin Xu, Jimmy Ba, Ryan Kiros, Kyunghyun Cho, Aaron Courville, Ruslan Salakhudinov, Rich Zemel, and Yoshua Bengio. 2015. Show, attend and tell: Neural image caption generation with visual attention. In International conference on machine learning, pages 2048–2057. PMLR.

Jason Yosinski, Jeff Clune, Yoshua Bengio, and Hod Lipson. 2014. How transferable are features in deep neural networks? arXiv preprint arXiv:1411.1792.

Peng W Zhang, Francis Lau, and Chiu-W Sham.

2020. Protograph-based low-density parity-check hadamard codes. arXiv preprint arXiv:2010.08285.

