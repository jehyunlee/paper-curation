SCIBERT: A Pretrained Language Model for Scientiﬁc Text

Iz Beltagy Kyle Lo Arman Cohan Allen Institute for Artiﬁcial Intelligence, Seattle, WA, USA {beltagy,kylel,armanc}@allenai.org

arXiv:1903.10676v3[cs.CL]10 Sep 2019

Abstract

Obtaining large-scale annotated data for NLP tasks in the scientiﬁc domain is challenging and expensive. We release SCIBERT, a pretrained language model based on BERT (Devlin et al., 2019) to address the lack of high-quality, large-scale labeled scientiﬁc data. SCIBERT leverages unsupervised pretraining on a large multi-domain corpus of scientiﬁc publications to improve performance on downstream scientiﬁc NLP tasks. We evaluate on a suite of tasks including sequence tagging, sentence classiﬁcation and dependency parsing, with datasets from a variety of scientiﬁc domains. We demonstrate statistically signiﬁcant improvements over BERT and achieve new state-of-theart results on several of these tasks. The code and pretrained models are available at https://github.com/allenai/scibert/.

# 1 Introduction

The exponential increase in the volume of scientiﬁc publications in the past decades has made NLP an essential tool for large-scale knowledge extraction and machine reading of these documents. Recent progress in NLP has been driven by the adoption of deep neural models, but training such models often requires large amounts of labeled data. In general domains, large-scale training data is often possible to obtain through crowdsourcing, but in scientiﬁc domains, annotated data is difﬁcult and expensive to collect due to the expertise required for quality annotation.

As shown through ELMo (Peters et al., 2018), GPT (Radford et al., 2018) and BERT (Devlin et al., 2019), unsupervised pretraining of language models on large corpora signiﬁcantly improves performance on many NLP tasks. These models return contextualized embeddings for each token which can be passed

into minimal task-speciﬁc neural architectures. Leveraging the success of unsupervised pretraining has become especially important especially when task-speciﬁc annotations are difﬁcult to obtain, like in scientiﬁc NLP. Yet while both BERT and ELMo have released pretrained models, they are still trained on general domain corpora such as news articles and Wikipedia.

In this work, we make the following contributions:

(i) We release SCIBERT, a new resource demonstrated to improve performance on a range of NLP tasks in the scientiﬁc domain. SCIBERT is a pretrained language model based on BERT but trained on a large corpus of scientiﬁc text.

- (ii) We perform extensive experimentation to

investigate the performance of ﬁnetuning versus task-speciﬁc architectures atop frozen embeddings, and the effect of having an in-domain vocabulary.

- (iii) We evaluate SCIBERT on a suite of tasks


in the scientiﬁc domain, and achieve new state-ofthe-art (SOTA) results on many of these tasks.

# 2 Methods

Background The BERT model architecture (Devlin et al., 2019) is based on a multilayer bidirectional Transformer (Vaswani et al., 2017). Instead of the traditional left-to-right language modeling objective, BERT is trained on two tasks: predicting randomly masked tokens and predicting whether two sentences follow each other. SCIBERT follows the same architecture as BERT but is instead pretrained on scientiﬁc text.

Vocabulary BERT uses WordPiece (Wu et al., 2016) for unsupervised tokenization of the input text. The vocabulary is built such that it contains the most frequently used words or subword units. We refer to the original vocabulary released with

BERT as BASEVOCAB.

We construct SCIVOCAB, a new WordPiece vocabulary on our scientiﬁc corpus using the SentencePiece1 library. We produce both cased and uncased vocabularies and set the vocabulary size to 30K to match the size of BASEVOCAB. The resulting token overlap between BASEVOCAB and SCIVOCAB is 42%, illustrating a substantial difference in frequently used words between scientiﬁc and general domain texts.

stracts. ACL-ARC (Jurgens et al., 2018) and SciCite (Cohan et al., 2019) assign intent labels (e.g. Comparison, Extension, etc.) to sentences from scientiﬁc papers that cite other papers. The Paper Field dataset is built from the Microsoft Academic Graph (Sinha et al., 2015)3 and maps paper titles to one of 7 ﬁelds of study. Each ﬁeld of study (i.e. geography, politics, economics, business, sociology, medicine, and psychology) has approximately 12K training examples.

Corpus We train SCIBERT on a random sample of 1.14M papers from Semantic Scholar (Ammar et al., 2018). This corpus consists of 18% papers from the computer science domain and 82% from the broad biomedical domain. We use the full text of the papers, not just the abstracts. The average paper length is 154 sentences (2,769 tokens) resulting in a corpus size of 3.17B tokens, similar to the 3.3B tokens on which BERT was trained. We split sentences using ScispaCy (Neumann et al., 2019),2 which is optimized for scientiﬁc text.

# 3 Experimental Setup

- 3.1 Tasks We experiment on the following core NLP tasks:

- 1. Named Entity Recognition (NER)
- 2. PICO Extraction (PICO)
- 3. Text Classiﬁcation (CLS)
- 4. Relation Classiﬁcation (REL)
- 5. Dependency Parsing (DEP)


PICO, like NER, is a sequence labeling task where the model extracts spans describing the Participants, Interventions, Comparisons, and Outcomes in a clinical trial paper (Kim et al., 2011). REL is a special case of text classiﬁcation where the model predicts the type of relation expressed between two entities, which are encapsulated in the sentence by inserted special tokens.

- 3.2 Datasets


For brevity, we only describe the newer datasets here, and refer the reader to the references in Table 1 for the older datasets. EBM-NLP (Nye et al.,

- 2018) annotates PICO spans in clinical trial abstracts. SciERC (Luan et al., 2018) annotates entities and relations from computer science ab-


![image 1](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1.png)

- 1https://github.com/google/sentencepiece
- 2https://github.com/allenai/SciSpaCy


3.3 Pretrained BERT Variants

BERT-Base We use the pretrained weights for BERT-Base (Devlin et al., 2019) released with the original BERT code.4 The vocabulary is BASEVOCAB. We evaluate both cased and uncased versions of this model.

SCIBERT We use the original BERT code to train SCIBERT on our corpus with the same conﬁguration and size as BERT-Base. We train 4 different versions of SCIBERT: (i) cased or uncased and (ii) BASEVOCAB or SCIVOCAB. The two models that use BASEVOCAB are ﬁnetuned from the corresponding BERT-Base models. The other two models that use the new SCIVOCAB are trained from scratch.

Pretraining BERT for long sentences can be slow. Following the original BERT code, we set a maximum sentence length of 128 tokens, and train the model until the training loss stops decreasing. We then continue training the model allowing sentence lengths up to 512 tokens.

We use a single TPU v3 with 8 cores. Training the SCIVOCAB models from scratch on our corpus takes 1 week5 (5 days with max length 128, then 2 days with max length 512). The BASEVOCAB models take 2 fewer days of training because they aren’t trained from scratch.

All pretrained BERT models are converted to be compatible with PyTorch using the pytorchtransformers library.6 All our models (Sections 3.4 and 3.5) are implemented in PyTorch using AllenNLP (Gardner et al., 2017).

Casing We follow Devlin et al. (2019) in using the cased models for NER and the uncased models

![image 2](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile2.png)

- 3https://academic.microsoft.com/
- 4https://github.com/google-research/bert 5BERT’s largest model was trained on 16 Cloud TPUs for


4 days. Expected 40-70 days (Dettmers, 2019) on an 8-GPU machine.

6https://github.com/huggingface/pytorch-transformers

for all other tasks. We also use the cased models for parsing. Some light experimentation showed that the uncased models perform slightly better (even sometimes on NER) than cased models.

- 3.4 Finetuning BERT

We mostly follow the same architecture, optimization, and hyperparameter choices used in Devlin et al. (2019). For text classiﬁcation (i.e. CLS and REL), we feed the ﬁnal BERT vector for the [CLS] token into a linear classiﬁcation layer. For sequence labeling (i.e. NER and PICO), we feed the ﬁnal BERT vector for each token into a linear classiﬁcation layer with softmax output. We differ slightly in using an additional conditional random ﬁeld, which made evaluation easier by guaranteeing well-formed entities. For DEP, we use the model from Dozat and Manning (2017) with dependency tag and arc embeddings of size 100 and biafﬁne matrix attention over BERT vectors instead of stacked BiLSTMs.

In all settings, we apply a dropout of 0.1 and optimize cross entropy loss using Adam (Kingma and Ba, 2015). We ﬁnetune for 2 to 5 epochs using a batch size of 32 and a learning rate of 5e-6, 1e-5, 2e-5, or 5e-5 with a slanted triangular schedule (Howard and Ruder, 2018) which is equivalent to the linear warmup followed by linear decay (Devlin et al., 2019). For each dataset and BERT variant, we pick the best learning rate and number of epochs on the development set and report the corresponding test results.

We found the setting that works best across most datasets and models is 2 or 4 epochs and a learning rate of 2e-5. While task-dependent, optimal hyperparameters for each task are often the same across BERT variants.

- 3.5 Frozen BERT Embeddings


We also explore the usage of BERT as pretrained contextualized word embeddings, like ELMo (Peters et al., 2018), by training simple task-speciﬁc models atop frozen BERT embeddings.

For text classiﬁcation, we feed each sentence of BERT vectors into a 2-layer BiLSTM of size 200 and apply a multilayer perceptron (with hidden size 200) on the concatenated ﬁrst and last BiLSTM vectors. For sequence labeling, we use the same BiLSTM layers and use a conditional random ﬁeld to guarantee well-formed predictions. For DEP, we use the full model from

Dozat and Manning (2017) with dependency tag and arc embeddings of size 100 and the same BiLSTM setup as other tasks. We did not ﬁnd changing the depth or size of the BiLSTMs to signiﬁcantly impact results (Reimers and Gurevych,

- 2017). We optimize cross entropy loss using Adam,

but holding BERT weights frozen and applying a dropout of 0.5. We train with early stopping on the development set (patience of 10) using a batch size of 32 and a learning rate of 0.001.

We did not perform extensive hyperparameter search, but while optimal hyperparameters are going to be task-dependent, some light experimentation showed these settings work fairly well across most tasks and BERT variants.

4 Results

Table 1 summarizes the experimental results. We observe that SCIBERT outperforms BERT-Base on scientiﬁc tasks (+2.11 F1 with ﬁnetuning and +2.43 F1 without)8. We also achieve new SOTA results on many of these tasks using SCIBERT.

4.1 Biomedical Domain

We observe that SCIBERT outperforms BERTBase on biomedical tasks (+1.92 F1 with ﬁnetuning and +3.59 F1 without). In addition, SCIBERT achieves new SOTA results on BC5CDR and ChemProt (Lee et al., 2019), and EBMNLP (Nye et al., 2018).

SCIBERT performs slightly worse than SOTA on 3 datasets. The SOTA model for JNLPBA is a BiLSTM-CRF ensemble trained on multiple NER datasets not just JNLPBA (Yoon et al.,

- 2018). The SOTA model for NCBI-disease is BIOBERT (Lee et al., 2019), which is BERTBase ﬁnetuned on 18B tokens from biomedical papers. The SOTA result for GENIA is in Nguyen and Verspoor (2019) which uses the model from Dozat and Manning (2017) with partof-speech (POS) features, which we do not use.


In Table 2, we compare SCIBERT results with reported BIOBERT results on the subset of datasets included in (Lee et al., 2019). Interesting, SCIBERT outperforms BIOBERT results on

![image 3](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile3.png)

- 7The SOTA paper did not report a single score. We compute the average of the reported results for each class weighted by number of examples in each class.
- 8For rest of this paper, all results reported in this manner are averaged over datasets excluding UAS for DEP since we already include LAS.


![image 4](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile4.png)

Field Task Dataset SOTA BERT-Base SCIBERT Frozen Finetune Frozen Finetune

![image 5](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile5.png)

![image 6](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile6.png)

![image 7](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile7.png)

![image 8](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile8.png)

![image 9](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile9.png)

![image 10](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile10.png)

![image 11](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile11.png)

![image 12](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile12.png)

![image 13](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile13.png)

![image 14](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile14.png)

![image 15](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile15.png)

![image 16](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile16.png)

![image 17](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile17.png)

![image 18](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile18.png)

![image 19](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile19.png)

![image 20](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile20.png)

![image 21](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile21.png)

![image 22](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile22.png)

![image 23](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile23.png)

![image 24](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile24.png)

![image 25](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile25.png)

![image 26](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile26.png)

![image 27](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile27.png)

![image 28](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile28.png)

![image 29](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile29.png)

![image 30](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile30.png)

![image 31](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile31.png)

![image 32](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile32.png)

![image 33](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile33.png)

![image 34](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile34.png)

![image 35](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile35.png)

![image 36](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile36.png)

![image 37](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile37.png)

![image 38](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile38.png)

![image 39](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile39.png)

![image 40](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile40.png)

![image 41](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile41.png)

![image 42](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile42.png)

![image 43](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile43.png)

![image 44](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile44.png)

![image 45](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile45.png)

![image 46](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile46.png)

![image 47](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile47.png)

![image 48](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile48.png)

![image 49](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile49.png)

![image 50](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile50.png)

![image 51](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile51.png)

![image 52](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile52.png)

![image 53](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile53.png)

![image 54](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile54.png)

![image 55](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile55.png)

![image 56](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile56.png)

![image 57](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile57.png)

![image 58](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile58.png)

![image 59](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile59.png)

![image 60](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile60.png)

![image 61](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile61.png)

![image 62](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile62.png)

![image 63](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile63.png)

![image 64](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile64.png)

![image 65](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile65.png)

![image 66](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile66.png)

![image 67](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile67.png)

![image 68](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile68.png)

![image 69](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile69.png)

![image 70](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile70.png)

![image 71](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile71.png)

![image 72](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile72.png)

![image 73](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile73.png)

![image 74](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile74.png)

![image 75](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile75.png)

![image 76](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile76.png)

![image 77](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile77.png)

![image 78](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile78.png)

![image 79](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile79.png)

![image 80](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile80.png)

![image 81](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile81.png)

![image 82](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile82.png)

![image 83](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile83.png)

![image 84](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile84.png)

![image 85](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile85.png)

![image 86](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile86.png)

![image 87](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile87.png)

![image 88](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile88.png)

![image 89](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile89.png)

![image 90](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile90.png)

![image 91](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile91.png)

![image 92](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile92.png)

![image 93](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile93.png)

![image 94](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile94.png)

![image 95](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile95.png)

![image 96](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile96.png)

![image 97](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile97.png)

![image 98](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile98.png)

![image 99](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile99.png)

![image 100](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile100.png)

![image 101](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile101.png)

![image 102](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile102.png)

![image 103](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile103.png)

![image 104](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile104.png)

![image 105](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile105.png)

BC5CDR (Li et al., 2016) 88.857 85.08 86.72 88.73 90.01 JNLPBA (Collier and Kim, 2004) 78.58 74.05 76.09 75.77 77.28 NCBI-disease (Dogan et al., 2014) 89.36 84.06 86.88 86.39 88.57

NER

Bio

![image 106](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile106.png)

![image 107](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile107.png)

![image 108](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile108.png)

![image 109](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile109.png)

![image 110](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile110.png)

![image 111](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile111.png)

![image 112](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile112.png)

![image 113](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile113.png)

![image 114](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile114.png)

![image 115](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile115.png)

![image 116](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile116.png)

![image 117](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile117.png)

![image 118](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile118.png)

![image 119](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile119.png)

![image 120](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile120.png)

![image 121](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile121.png)

![image 122](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile122.png)

![image 123](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile123.png)

![image 124](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile124.png)

![image 125](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile125.png)

![image 126](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile126.png)

![image 127](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile127.png)

![image 128](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile128.png)

![image 129](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile129.png)

![image 130](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile130.png)

![image 131](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile131.png)

![image 132](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile132.png)

![image 133](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile133.png)

![image 134](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile134.png)

![image 135](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile135.png)

![image 136](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile136.png)

![image 137](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile137.png)

![image 138](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile138.png)

![image 139](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile139.png)

![image 140](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile140.png)

![image 141](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile141.png)

![image 142](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile142.png)

![image 143](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile143.png)

![image 144](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile144.png)

![image 145](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile145.png)

![image 146](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile146.png)

![image 147](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile147.png)

![image 148](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile148.png)

![image 149](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile149.png)

![image 150](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile150.png)

![image 151](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile151.png)

![image 152](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile152.png)

![image 153](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile153.png)

![image 154](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile154.png)

![image 155](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile155.png)

![image 156](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile156.png)

![image 157](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile157.png)

![image 158](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile158.png)

![image 159](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile159.png)

![image 160](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile160.png)

![image 161](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile161.png)

![image 162](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile162.png)

![image 163](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile163.png)

![image 164](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile164.png)

![image 165](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile165.png)

![image 166](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile166.png)

![image 167](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile167.png)

![image 168](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile168.png)

![image 169](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile169.png)

![image 170](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile170.png)

![image 171](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile171.png)

![image 172](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile172.png)

![image 173](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile173.png)

![image 174](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile174.png)

![image 175](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile175.png)

![image 176](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile176.png)

![image 177](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile177.png)

![image 178](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile178.png)

![image 179](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile179.png)

![image 180](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile180.png)

![image 181](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile181.png)

![image 182](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile182.png)

![image 183](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile183.png)

![image 184](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile184.png)

![image 185](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile185.png)

![image 186](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile186.png)

![image 187](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile187.png)

![image 188](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile188.png)

![image 189](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile189.png)

![image 190](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile190.png)

![image 191](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile191.png)

![image 192](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile192.png)

![image 193](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile193.png)

![image 194](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile194.png)

![image 195](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile195.png)

![image 196](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile196.png)

![image 197](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile197.png)

![image 198](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile198.png)

![image 199](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile199.png)

![image 200](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile200.png)

![image 201](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile201.png)

![image 202](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile202.png)

![image 203](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile203.png)

![image 204](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile204.png)

![image 205](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile205.png)

![image 206](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile206.png)

![image 207](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile207.png)

![image 208](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile208.png)

![image 209](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile209.png)

![image 210](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile210.png)

![image 211](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile211.png)

![image 212](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile212.png)

![image 213](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile213.png)

![image 214](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile214.png)

![image 215](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile215.png)

![image 216](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile216.png)

![image 217](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile217.png)

![image 218](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile218.png)

![image 219](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile219.png)

![image 220](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile220.png)

![image 221](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile221.png)

![image 222](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile222.png)

![image 223](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile223.png)

![image 224](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile224.png)

![image 225](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile225.png)

![image 226](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile226.png)

![image 227](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile227.png)

![image 228](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile228.png)

![image 229](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile229.png)

![image 230](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile230.png)

![image 231](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile231.png)

![image 232](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile232.png)

![image 233](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile233.png)

![image 234](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile234.png)

![image 235](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile235.png)

![image 236](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile236.png)

![image 237](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile237.png)

![image 238](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile238.png)

![image 239](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile239.png)

![image 240](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile240.png)

![image 241](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile241.png)

![image 242](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile242.png)

![image 243](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile243.png)

![image 244](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile244.png)

![image 245](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile245.png)

![image 246](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile246.png)

![image 247](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile247.png)

![image 248](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile248.png)

![image 249](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile249.png)

![image 250](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile250.png)

![image 251](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile251.png)

![image 252](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile252.png)

![image 253](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile253.png)

![image 254](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile254.png)

![image 255](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile255.png)

![image 256](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile256.png)

![image 257](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile257.png)

![image 258](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile258.png)

![image 259](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile259.png)

![image 260](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile260.png)

![image 261](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile261.png)

![image 262](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile262.png)

![image 263](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile263.png)

![image 264](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile264.png)

![image 265](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile265.png)

![image 266](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile266.png)

![image 267](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile267.png)

![image 268](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile268.png)

![image 269](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile269.png)

![image 270](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile270.png)

![image 271](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile271.png)

![image 272](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile272.png)

![image 273](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile273.png)

![image 274](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile274.png)

![image 275](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile275.png)

![image 276](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile276.png)

![image 277](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile277.png)

![image 278](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile278.png)

![image 279](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile279.png)

![image 280](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile280.png)

![image 281](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile281.png)

![image 282](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile282.png)

![image 283](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile283.png)

![image 284](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile284.png)

![image 285](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile285.png)

![image 286](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile286.png)

![image 287](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile287.png)

![image 288](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile288.png)

![image 289](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile289.png)

![image 290](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile290.png)

![image 291](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile291.png)

![image 292](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile292.png)

![image 293](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile293.png)

![image 294](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile294.png)

![image 295](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile295.png)

![image 296](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile296.png)

![image 297](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile297.png)

![image 298](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile298.png)

![image 299](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile299.png)

![image 300](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile300.png)

![image 301](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile301.png)

![image 302](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile302.png)

![image 303](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile303.png)

![image 304](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile304.png)

![image 305](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile305.png)

![image 306](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile306.png)

![image 307](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile307.png)

![image 308](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile308.png)

![image 309](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile309.png)

![image 310](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile310.png)

![image 311](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile311.png)

![image 312](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile312.png)

![image 313](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile313.png)

![image 314](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile314.png)

![image 315](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile315.png)

![image 316](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile316.png)

![image 317](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile317.png)

![image 318](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile318.png)

![image 319](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile319.png)

![image 320](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile320.png)

![image 321](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile321.png)

![image 322](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile322.png)

![image 323](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile323.png)

![image 324](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile324.png)

![image 325](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile325.png)

![image 326](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile326.png)

![image 327](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile327.png)

![image 328](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile328.png)

![image 329](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile329.png)

![image 330](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile330.png)

![image 331](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile331.png)

![image 332](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile332.png)

![image 333](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile333.png)

![image 334](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile334.png)

PICO EBM-NLP (Nye et al., 2018) 66.30 61.44 71.53 68.30 72.28 DEP

![image 335](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile335.png)

![image 336](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile336.png)

![image 337](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile337.png)

![image 338](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile338.png)

![image 339](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile339.png)

![image 340](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile340.png)

![image 341](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile341.png)

![image 342](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile342.png)

![image 343](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile343.png)

![image 344](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile344.png)

![image 345](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile345.png)

![image 346](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile346.png)

![image 347](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile347.png)

![image 348](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile348.png)

![image 349](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile349.png)

![image 350](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile350.png)

![image 351](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile351.png)

![image 352](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile352.png)

![image 353](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile353.png)

![image 354](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile354.png)

![image 355](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile355.png)

![image 356](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile356.png)

![image 357](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile357.png)

![image 358](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile358.png)

![image 359](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile359.png)

![image 360](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile360.png)

![image 361](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile361.png)

![image 362](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile362.png)

![image 363](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile363.png)

![image 364](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile364.png)

![image 365](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile365.png)

![image 366](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile366.png)

![image 367](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile367.png)

![image 368](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile368.png)

![image 369](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile369.png)

![image 370](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile370.png)

![image 371](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile371.png)

![image 372](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile372.png)

![image 373](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile373.png)

![image 374](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile374.png)

![image 375](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile375.png)

![image 376](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile376.png)

![image 377](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile377.png)

![image 378](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile378.png)

![image 379](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile379.png)

![image 380](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile380.png)

![image 381](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile381.png)

![image 382](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile382.png)

![image 383](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile383.png)

![image 384](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile384.png)

![image 385](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile385.png)

![image 386](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile386.png)

![image 387](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile387.png)

![image 388](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile388.png)

![image 389](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile389.png)

![image 390](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile390.png)

![image 391](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile391.png)

![image 392](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile392.png)

![image 393](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile393.png)

![image 394](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile394.png)

![image 395](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile395.png)

![image 396](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile396.png)

![image 397](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile397.png)

![image 398](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile398.png)

![image 399](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile399.png)

![image 400](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile400.png)

![image 401](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile401.png)

![image 402](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile402.png)

![image 403](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile403.png)

![image 404](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile404.png)

![image 405](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile405.png)

![image 406](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile406.png)

![image 407](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile407.png)

![image 408](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile408.png)

![image 409](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile409.png)

![image 410](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile410.png)

![image 411](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile411.png)

![image 412](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile412.png)

![image 413](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile413.png)

![image 414](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile414.png)

![image 415](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile415.png)

![image 416](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile416.png)

![image 417](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile417.png)

![image 418](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile418.png)

![image 419](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile419.png)

![image 420](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile420.png)

![image 421](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile421.png)

![image 422](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile422.png)

![image 423](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile423.png)

![image 424](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile424.png)

![image 425](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile425.png)

![image 426](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile426.png)

![image 427](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile427.png)

![image 428](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile428.png)

![image 429](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile429.png)

![image 430](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile430.png)

![image 431](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile431.png)

![image 432](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile432.png)

![image 433](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile433.png)

![image 434](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile434.png)

![image 435](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile435.png)

![image 436](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile436.png)

![image 437](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile437.png)

![image 438](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile438.png)

![image 439](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile439.png)

![image 440](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile440.png)

![image 441](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile441.png)

![image 442](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile442.png)

![image 443](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile443.png)

![image 444](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile444.png)

![image 445](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile445.png)

![image 446](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile446.png)

![image 447](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile447.png)

![image 448](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile448.png)

![image 449](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile449.png)

![image 450](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile450.png)

![image 451](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile451.png)

![image 452](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile452.png)

![image 453](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile453.png)

![image 454](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile454.png)

![image 455](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile455.png)

![image 456](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile456.png)

![image 457](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile457.png)

![image 458](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile458.png)

![image 459](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile459.png)

![image 460](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile460.png)

![image 461](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile461.png)

![image 462](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile462.png)

![image 463](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile463.png)

![image 464](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile464.png)

![image 465](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile465.png)

![image 466](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile466.png)

![image 467](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile467.png)

![image 468](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile468.png)

![image 469](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile469.png)

![image 470](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile470.png)

![image 471](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile471.png)

![image 472](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile472.png)

![image 473](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile473.png)

![image 474](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile474.png)

![image 475](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile475.png)

![image 476](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile476.png)

![image 477](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile477.png)

![image 478](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile478.png)

![image 479](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile479.png)

![image 480](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile480.png)

![image 481](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile481.png)

![image 482](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile482.png)

![image 483](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile483.png)

![image 484](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile484.png)

![image 485](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile485.png)

![image 486](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile486.png)

![image 487](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile487.png)

![image 488](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile488.png)

![image 489](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile489.png)

![image 490](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile490.png)

![image 491](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile491.png)

![image 492](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile492.png)

![image 493](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile493.png)

![image 494](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile494.png)

![image 495](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile495.png)

![image 496](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile496.png)

![image 497](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile497.png)

![image 498](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile498.png)

![image 499](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile499.png)

![image 500](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile500.png)

![image 501](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile501.png)

![image 502](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile502.png)

![image 503](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile503.png)

![image 504](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile504.png)

![image 505](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile505.png)

![image 506](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile506.png)

![image 507](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile507.png)

![image 508](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile508.png)

![image 509](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile509.png)

![image 510](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile510.png)

![image 511](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile511.png)

![image 512](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile512.png)

![image 513](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile513.png)

![image 514](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile514.png)

![image 515](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile515.png)

![image 516](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile516.png)

![image 517](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile517.png)

![image 518](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile518.png)

![image 519](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile519.png)

![image 520](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile520.png)

![image 521](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile521.png)

![image 522](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile522.png)

![image 523](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile523.png)

![image 524](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile524.png)

![image 525](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile525.png)

![image 526](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile526.png)

![image 527](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile527.png)

![image 528](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile528.png)

![image 529](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile529.png)

![image 530](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile530.png)

![image 531](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile531.png)

![image 532](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile532.png)

![image 533](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile533.png)

![image 534](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile534.png)

![image 535](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile535.png)

![image 536](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile536.png)

![image 537](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile537.png)

![image 538](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile538.png)

![image 539](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile539.png)

![image 540](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile540.png)

![image 541](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile541.png)

![image 542](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile542.png)

![image 543](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile543.png)

![image 544](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile544.png)

![image 545](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile545.png)

![image 546](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile546.png)

![image 547](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile547.png)

![image 548](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile548.png)

![image 549](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile549.png)

![image 550](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile550.png)

![image 551](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile551.png)

![image 552](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile552.png)

![image 553](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile553.png)

![image 554](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile554.png)

![image 555](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile555.png)

![image 556](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile556.png)

![image 557](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile557.png)

![image 558](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile558.png)

![image 559](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile559.png)

![image 560](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile560.png)

![image 561](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile561.png)

![image 562](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile562.png)

![image 563](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile563.png)

GENIA (Kim et al., 2003) - LAS 91.92 90.22 90.33 90.36 90.43 GENIA (Kim et al., 2003) - UAS 92.84 91.84 91.89 92.00 91.99

![image 564](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile564.png)

![image 565](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile565.png)

![image 566](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile566.png)

![image 567](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile567.png)

![image 568](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile568.png)

![image 569](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile569.png)

![image 570](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile570.png)

![image 571](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile571.png)

![image 572](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile572.png)

![image 573](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile573.png)

![image 574](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile574.png)

![image 575](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile575.png)

![image 576](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile576.png)

![image 577](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile577.png)

![image 578](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile578.png)

![image 579](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile579.png)

![image 580](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile580.png)

![image 581](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile581.png)

![image 582](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile582.png)

![image 583](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile583.png)

![image 584](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile584.png)

![image 585](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile585.png)

![image 586](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile586.png)

![image 587](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile587.png)

![image 588](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile588.png)

![image 589](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile589.png)

![image 590](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile590.png)

![image 591](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile591.png)

![image 592](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile592.png)

![image 593](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile593.png)

![image 594](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile594.png)

![image 595](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile595.png)

![image 596](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile596.png)

![image 597](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile597.png)

![image 598](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile598.png)

![image 599](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile599.png)

![image 600](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile600.png)

![image 601](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile601.png)

![image 602](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile602.png)

![image 603](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile603.png)

![image 604](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile604.png)

![image 605](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile605.png)

![image 606](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile606.png)

![image 607](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile607.png)

![image 608](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile608.png)

![image 609](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile609.png)

![image 610](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile610.png)

![image 611](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile611.png)

![image 612](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile612.png)

![image 613](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile613.png)

![image 614](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile614.png)

![image 615](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile615.png)

![image 616](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile616.png)

![image 617](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile617.png)

![image 618](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile618.png)

![image 619](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile619.png)

![image 620](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile620.png)

![image 621](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile621.png)

![image 622](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile622.png)

![image 623](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile623.png)

![image 624](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile624.png)

![image 625](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile625.png)

![image 626](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile626.png)

![image 627](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile627.png)

![image 628](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile628.png)

![image 629](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile629.png)

![image 630](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile630.png)

![image 631](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile631.png)

![image 632](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile632.png)

![image 633](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile633.png)

![image 634](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile634.png)

![image 635](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile635.png)

![image 636](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile636.png)

![image 637](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile637.png)

![image 638](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile638.png)

![image 639](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile639.png)

![image 640](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile640.png)

![image 641](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile641.png)

![image 642](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile642.png)

![image 643](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile643.png)

![image 644](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile644.png)

![image 645](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile645.png)

![image 646](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile646.png)

![image 647](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile647.png)

![image 648](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile648.png)

![image 649](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile649.png)

![image 650](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile650.png)

![image 651](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile651.png)

![image 652](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile652.png)

![image 653](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile653.png)

![image 654](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile654.png)

![image 655](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile655.png)

![image 656](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile656.png)

![image 657](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile657.png)

![image 658](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile658.png)

![image 659](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile659.png)

![image 660](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile660.png)

![image 661](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile661.png)

![image 662](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile662.png)

![image 663](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile663.png)

![image 664](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile664.png)

![image 665](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile665.png)

![image 666](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile666.png)

![image 667](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile667.png)

![image 668](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile668.png)

![image 669](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile669.png)

![image 670](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile670.png)

![image 671](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile671.png)

![image 672](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile672.png)

![image 673](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile673.png)

![image 674](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile674.png)

![image 675](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile675.png)

![image 676](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile676.png)

![image 677](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile677.png)

![image 678](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile678.png)

![image 679](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile679.png)

![image 680](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile680.png)

![image 681](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile681.png)

![image 682](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile682.png)

![image 683](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile683.png)

![image 684](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile684.png)

![image 685](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile685.png)

![image 686](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile686.png)

![image 687](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile687.png)

![image 688](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile688.png)

![image 689](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile689.png)

![image 690](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile690.png)

![image 691](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile691.png)

![image 692](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile692.png)

![image 693](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile693.png)

![image 694](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile694.png)

![image 695](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile695.png)

![image 696](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile696.png)

![image 697](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile697.png)

![image 698](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile698.png)

![image 699](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile699.png)

![image 700](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile700.png)

![image 701](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile701.png)

![image 702](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile702.png)

![image 703](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile703.png)

![image 704](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile704.png)

![image 705](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile705.png)

![image 706](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile706.png)

![image 707](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile707.png)

![image 708](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile708.png)

![image 709](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile709.png)

![image 710](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile710.png)

![image 711](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile711.png)

![image 712](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile712.png)

![image 713](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile713.png)

![image 714](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile714.png)

![image 715](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile715.png)

![image 716](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile716.png)

![image 717](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile717.png)

![image 718](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile718.png)

![image 719](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile719.png)

![image 720](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile720.png)

![image 721](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile721.png)

![image 722](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile722.png)

![image 723](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile723.png)

![image 724](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile724.png)

![image 725](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile725.png)

![image 726](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile726.png)

![image 727](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile727.png)

![image 728](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile728.png)

![image 729](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile729.png)

![image 730](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile730.png)

![image 731](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile731.png)

![image 732](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile732.png)

![image 733](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile733.png)

![image 734](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile734.png)

![image 735](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile735.png)

![image 736](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile736.png)

![image 737](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile737.png)

![image 738](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile738.png)

![image 739](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile739.png)

![image 740](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile740.png)

![image 741](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile741.png)

![image 742](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile742.png)

![image 743](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile743.png)

![image 744](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile744.png)

![image 745](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile745.png)

![image 746](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile746.png)

![image 747](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile747.png)

![image 748](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile748.png)

![image 749](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile749.png)

![image 750](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile750.png)

![image 751](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile751.png)

![image 752](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile752.png)

![image 753](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile753.png)

![image 754](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile754.png)

![image 755](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile755.png)

![image 756](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile756.png)

![image 757](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile757.png)

![image 758](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile758.png)

![image 759](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile759.png)

![image 760](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile760.png)

![image 761](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile761.png)

![image 762](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile762.png)

![image 763](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile763.png)

![image 764](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile764.png)

![image 765](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile765.png)

![image 766](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile766.png)

![image 767](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile767.png)

![image 768](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile768.png)

![image 769](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile769.png)

![image 770](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile770.png)

![image 771](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile771.png)

![image 772](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile772.png)

![image 773](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile773.png)

![image 774](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile774.png)

![image 775](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile775.png)

![image 776](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile776.png)

![image 777](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile777.png)

![image 778](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile778.png)

![image 779](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile779.png)

![image 780](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile780.png)

![image 781](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile781.png)

![image 782](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile782.png)

![image 783](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile783.png)

![image 784](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile784.png)

![image 785](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile785.png)

![image 786](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile786.png)

![image 787](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile787.png)

![image 788](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile788.png)

![image 789](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile789.png)

![image 790](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile790.png)

![image 791](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile791.png)

![image 792](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile792.png)

REL ChemProt (Kringelum et al., 2016) 76.68 68.21 79.14 75.03 83.64

![image 793](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile793.png)

NER SciERC (Luan et al., 2018) 64.20 63.58 65.24 65.77 67.57 REL SciERC (Luan et al., 2018) n/a 72.74 78.71 75.25 79.97 CLS ACL-ARC (Jurgens et al., 2018) 67.9 62.04 63.91 60.74 70.98

![image 794](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile794.png)

![image 795](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile795.png)

![image 796](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile796.png)

![image 797](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile797.png)

![image 798](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile798.png)

![image 799](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile799.png)

![image 800](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile800.png)

![image 801](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile801.png)

![image 802](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile802.png)

![image 803](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile803.png)

![image 804](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile804.png)

![image 805](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile805.png)

![image 806](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile806.png)

![image 807](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile807.png)

![image 808](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile808.png)

![image 809](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile809.png)

![image 810](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile810.png)

![image 811](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile811.png)

![image 812](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile812.png)

![image 813](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile813.png)

![image 814](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile814.png)

![image 815](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile815.png)

![image 816](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile816.png)

![image 817](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile817.png)

![image 818](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile818.png)

![image 819](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile819.png)

![image 820](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile820.png)

![image 821](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile821.png)

![image 822](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile822.png)

![image 823](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile823.png)

![image 824](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile824.png)

![image 825](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile825.png)

![image 826](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile826.png)

![image 827](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile827.png)

![image 828](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile828.png)

![image 829](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile829.png)

![image 830](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile830.png)

![image 831](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile831.png)

![image 832](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile832.png)

![image 833](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile833.png)

![image 834](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile834.png)

![image 835](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile835.png)

![image 836](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile836.png)

![image 837](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile837.png)

![image 838](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile838.png)

![image 839](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile839.png)

![image 840](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile840.png)

![image 841](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile841.png)

![image 842](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile842.png)

![image 843](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile843.png)

![image 844](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile844.png)

![image 845](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile845.png)

![image 846](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile846.png)

![image 847](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile847.png)

![image 848](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile848.png)

![image 849](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile849.png)

![image 850](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile850.png)

![image 851](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile851.png)

![image 852](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile852.png)

![image 853](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile853.png)

![image 854](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile854.png)

![image 855](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile855.png)

![image 856](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile856.png)

![image 857](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile857.png)

![image 858](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile858.png)

![image 859](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile859.png)

![image 860](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile860.png)

![image 861](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile861.png)

![image 862](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile862.png)

![image 863](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile863.png)

![image 864](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile864.png)

![image 865](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile865.png)

![image 866](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile866.png)

![image 867](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile867.png)

![image 868](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile868.png)

![image 869](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile869.png)

![image 870](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile870.png)

![image 871](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile871.png)

![image 872](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile872.png)

![image 873](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile873.png)

![image 874](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile874.png)

![image 875](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile875.png)

![image 876](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile876.png)

![image 877](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile877.png)

![image 878](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile878.png)

![image 879](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile879.png)

![image 880](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile880.png)

![image 881](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile881.png)

![image 882](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile882.png)

![image 883](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile883.png)

![image 884](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile884.png)

![image 885](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile885.png)

![image 886](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile886.png)

![image 887](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile887.png)

![image 888](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile888.png)

![image 889](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile889.png)

![image 890](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile890.png)

![image 891](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile891.png)

![image 892](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile892.png)

![image 893](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile893.png)

![image 894](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile894.png)

![image 895](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile895.png)

![image 896](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile896.png)

![image 897](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile897.png)

![image 898](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile898.png)

![image 899](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile899.png)

![image 900](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile900.png)

![image 901](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile901.png)

![image 902](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile902.png)

![image 903](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile903.png)

![image 904](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile904.png)

![image 905](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile905.png)

![image 906](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile906.png)

![image 907](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile907.png)

![image 908](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile908.png)

![image 909](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile909.png)

![image 910](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile910.png)

![image 911](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile911.png)

![image 912](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile912.png)

![image 913](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile913.png)

![image 914](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile914.png)

![image 915](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile915.png)

![image 916](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile916.png)

![image 917](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile917.png)

![image 918](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile918.png)

![image 919](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile919.png)

![image 920](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile920.png)

![image 921](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile921.png)

![image 922](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile922.png)

![image 923](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile923.png)

![image 924](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile924.png)

![image 925](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile925.png)

![image 926](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile926.png)

![image 927](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile927.png)

![image 928](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile928.png)

![image 929](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile929.png)

![image 930](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile930.png)

![image 931](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile931.png)

![image 932](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile932.png)

![image 933](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile933.png)

![image 934](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile934.png)

![image 935](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile935.png)

![image 936](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile936.png)

![image 937](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile937.png)

![image 938](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile938.png)

![image 939](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile939.png)

![image 940](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile940.png)

![image 941](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile941.png)

![image 942](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile942.png)

![image 943](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile943.png)

![image 944](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile944.png)

![image 945](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile945.png)

![image 946](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile946.png)

![image 947](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile947.png)

![image 948](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile948.png)

![image 949](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile949.png)

![image 950](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile950.png)

![image 951](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile951.png)

![image 952](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile952.png)

![image 953](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile953.png)

![image 954](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile954.png)

![image 955](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile955.png)

![image 956](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile956.png)

![image 957](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile957.png)

![image 958](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile958.png)

![image 959](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile959.png)

![image 960](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile960.png)

![image 961](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile961.png)

![image 962](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile962.png)

![image 963](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile963.png)

![image 964](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile964.png)

![image 965](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile965.png)

![image 966](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile966.png)

![image 967](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile967.png)

![image 968](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile968.png)

![image 969](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile969.png)

![image 970](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile970.png)

![image 971](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile971.png)

![image 972](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile972.png)

![image 973](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile973.png)

![image 974](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile974.png)

![image 975](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile975.png)

![image 976](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile976.png)

![image 977](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile977.png)

![image 978](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile978.png)

![image 979](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile979.png)

![image 980](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile980.png)

![image 981](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile981.png)

![image 982](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile982.png)

![image 983](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile983.png)

![image 984](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile984.png)

![image 985](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile985.png)

![image 986](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile986.png)

![image 987](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile987.png)

![image 988](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile988.png)

![image 989](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile989.png)

![image 990](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile990.png)

![image 991](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile991.png)

![image 992](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile992.png)

![image 993](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile993.png)

![image 994](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile994.png)

![image 995](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile995.png)

![image 996](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile996.png)

![image 997](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile997.png)

![image 998](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile998.png)

![image 999](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile999.png)

![image 1000](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1000.png)

![image 1001](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1001.png)

![image 1002](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1002.png)

![image 1003](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1003.png)

![image 1004](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1004.png)

![image 1005](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1005.png)

![image 1006](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1006.png)

![image 1007](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1007.png)

![image 1008](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1008.png)

![image 1009](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1009.png)

![image 1010](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1010.png)

![image 1011](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1011.png)

![image 1012](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1012.png)

![image 1013](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1013.png)

![image 1014](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1014.png)

![image 1015](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1015.png)

![image 1016](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1016.png)

![image 1017](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1017.png)

![image 1018](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1018.png)

![image 1019](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1019.png)

![image 1020](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1020.png)

![image 1021](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1021.png)

![image 1022](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1022.png)

CS

![image 1023](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1023.png)

![image 1024](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1024.png)

![image 1025](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1025.png)

![image 1026](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1026.png)

![image 1027](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1027.png)

![image 1028](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1028.png)

![image 1029](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1029.png)

![image 1030](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1030.png)

![image 1031](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1031.png)

![image 1032](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1032.png)

![image 1033](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1033.png)

![image 1034](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1034.png)

![image 1035](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1035.png)

![image 1036](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1036.png)

![image 1037](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1037.png)

![image 1038](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1038.png)

![image 1039](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1039.png)

![image 1040](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1040.png)

![image 1041](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1041.png)

![image 1042](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1042.png)

![image 1043](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1043.png)

![image 1044](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1044.png)

![image 1045](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1045.png)

![image 1046](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1046.png)

![image 1047](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1047.png)

![image 1048](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1048.png)

![image 1049](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1049.png)

![image 1050](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1050.png)

![image 1051](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1051.png)

![image 1052](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1052.png)

![image 1053](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1053.png)

![image 1054](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1054.png)

![image 1055](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1055.png)

![image 1056](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1056.png)

![image 1057](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1057.png)

![image 1058](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1058.png)

![image 1059](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1059.png)

![image 1060](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1060.png)

![image 1061](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1061.png)

![image 1062](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1062.png)

![image 1063](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1063.png)

![image 1064](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1064.png)

![image 1065](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1065.png)

![image 1066](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1066.png)

![image 1067](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1067.png)

![image 1068](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1068.png)

![image 1069](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1069.png)

![image 1070](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1070.png)

![image 1071](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1071.png)

![image 1072](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1072.png)

![image 1073](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1073.png)

![image 1074](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1074.png)

![image 1075](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1075.png)

![image 1076](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1076.png)

![image 1077](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1077.png)

![image 1078](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1078.png)

![image 1079](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1079.png)

![image 1080](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1080.png)

![image 1081](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1081.png)

![image 1082](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1082.png)

![image 1083](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1083.png)

![image 1084](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1084.png)

![image 1085](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1085.png)

![image 1086](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1086.png)

![image 1087](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1087.png)

![image 1088](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1088.png)

![image 1089](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1089.png)

![image 1090](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1090.png)

![image 1091](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1091.png)

![image 1092](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1092.png)

![image 1093](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1093.png)

![image 1094](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1094.png)

![image 1095](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1095.png)

![image 1096](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1096.png)

![image 1097](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1097.png)

![image 1098](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1098.png)

![image 1099](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1099.png)

![image 1100](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1100.png)

![image 1101](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1101.png)

![image 1102](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1102.png)

![image 1103](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1103.png)

![image 1104](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1104.png)

![image 1105](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1105.png)

![image 1106](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1106.png)

![image 1107](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1107.png)

![image 1108](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1108.png)

![image 1109](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1109.png)

![image 1110](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1110.png)

![image 1111](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1111.png)

![image 1112](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1112.png)

![image 1113](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1113.png)

![image 1114](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1114.png)

![image 1115](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1115.png)

![image 1116](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1116.png)

![image 1117](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1117.png)

![image 1118](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1118.png)

![image 1119](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1119.png)

![image 1120](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1120.png)

![image 1121](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1121.png)

![image 1122](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1122.png)

![image 1123](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1123.png)

![image 1124](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1124.png)

![image 1125](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1125.png)

![image 1126](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1126.png)

![image 1127](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1127.png)

![image 1128](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1128.png)

![image 1129](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1129.png)

![image 1130](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1130.png)

![image 1131](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1131.png)

![image 1132](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1132.png)

![image 1133](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1133.png)

![image 1134](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1134.png)

![image 1135](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1135.png)

![image 1136](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1136.png)

![image 1137](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1137.png)

![image 1138](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1138.png)

![image 1139](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1139.png)

![image 1140](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1140.png)

![image 1141](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1141.png)

![image 1142](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1142.png)

![image 1143](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1143.png)

![image 1144](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1144.png)

![image 1145](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1145.png)

![image 1146](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1146.png)

![image 1147](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1147.png)

![image 1148](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1148.png)

![image 1149](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1149.png)

![image 1150](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1150.png)

![image 1151](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1151.png)

![image 1152](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1152.png)

![image 1153](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1153.png)

![image 1154](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1154.png)

![image 1155](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1155.png)

![image 1156](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1156.png)

![image 1157](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1157.png)

![image 1158](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1158.png)

![image 1159](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1159.png)

![image 1160](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1160.png)

![image 1161](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1161.png)

![image 1162](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1162.png)

![image 1163](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1163.png)

![image 1164](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1164.png)

![image 1165](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1165.png)

![image 1166](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1166.png)

![image 1167](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1167.png)

![image 1168](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1168.png)

![image 1169](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1169.png)

![image 1170](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1170.png)

![image 1171](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1171.png)

![image 1172](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1172.png)

![image 1173](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1173.png)

![image 1174](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1174.png)

![image 1175](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1175.png)

![image 1176](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1176.png)

![image 1177](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1177.png)

![image 1178](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1178.png)

![image 1179](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1179.png)

![image 1180](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1180.png)

![image 1181](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1181.png)

![image 1182](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1182.png)

![image 1183](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1183.png)

![image 1184](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1184.png)

![image 1185](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1185.png)

![image 1186](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1186.png)

![image 1187](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1187.png)

![image 1188](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1188.png)

![image 1189](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1189.png)

![image 1190](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1190.png)

![image 1191](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1191.png)

![image 1192](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1192.png)

![image 1193](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1193.png)

![image 1194](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1194.png)

![image 1195](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1195.png)

![image 1196](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1196.png)

![image 1197](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1197.png)

![image 1198](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1198.png)

![image 1199](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1199.png)

![image 1200](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1200.png)

![image 1201](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1201.png)

![image 1202](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1202.png)

![image 1203](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1203.png)

![image 1204](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1204.png)

![image 1205](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1205.png)

![image 1206](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1206.png)

![image 1207](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1207.png)

![image 1208](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1208.png)

![image 1209](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1209.png)

![image 1210](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1210.png)

![image 1211](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1211.png)

![image 1212](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1212.png)

![image 1213](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1213.png)

![image 1214](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1214.png)

![image 1215](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1215.png)

![image 1216](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1216.png)

![image 1217](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1217.png)

![image 1218](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1218.png)

![image 1219](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1219.png)

![image 1220](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1220.png)

![image 1221](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1221.png)

![image 1222](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1222.png)

![image 1223](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1223.png)

![image 1224](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1224.png)

![image 1225](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1225.png)

![image 1226](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1226.png)

![image 1227](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1227.png)

![image 1228](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1228.png)

![image 1229](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1229.png)

![image 1230](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1230.png)

![image 1231](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1231.png)

![image 1232](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1232.png)

![image 1233](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1233.png)

![image 1234](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1234.png)

![image 1235](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1235.png)

![image 1236](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1236.png)

![image 1237](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1237.png)

![image 1238](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1238.png)

![image 1239](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1239.png)

![image 1240](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1240.png)

![image 1241](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1241.png)

![image 1242](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1242.png)

![image 1243](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1243.png)

![image 1244](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1244.png)

![image 1245](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1245.png)

![image 1246](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1246.png)

![image 1247](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1247.png)

![image 1248](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1248.png)

![image 1249](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1249.png)

![image 1250](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1250.png)

![image 1251](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1251.png)

![image 1252](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1252.png)

Paper Field n/a 63.64 65.37 64.38 65.71 SciCite (Cohan et al., 2019) 84.0 84.31 84.85 85.42 85.49

Multi CLS

![image 1253](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1253.png)

Average 73.58 77.16 76.01 79.27

![image 1254](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1254.png)

- Table 1: Test performances of all BERT variants on all tasks and datasets. Bold indicates the SOTA result (multiple results bolded if difference within 95% bootstrap conﬁdence interval). Keeping with past work, we report macro F1 scores for NER (span-level), macro F1 scores for REL and CLS (sentence-level), and macro F1 for PICO (token-level), and micro F1 for ChemProt speciﬁcally. For DEP, we report labeled (LAS) and unlabeled (UAS) attachment scores (excluding punctuation) for the same model with hyperparameters tuned for LAS. All results are the average of multiple runs with different random seeds.

![image 1255](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1255.png)

Task Dataset BIOBERT SCIBERT

![image 1256](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1256.png)

NER

BC5CDR 88.85 90.01 JNLPBA 77.59 77.28 NCBI-disease 89.36 88.57

![image 1257](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1257.png)

![image 1258](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1258.png)

![image 1259](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1259.png)

![image 1260](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1260.png)

![image 1261](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1261.png)

![image 1262](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1262.png)

![image 1263](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1263.png)

![image 1264](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1264.png)

![image 1265](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1265.png)

![image 1266](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1266.png)

![image 1267](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1267.png)

![image 1268](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1268.png)

![image 1269](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1269.png)

![image 1270](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1270.png)

![image 1271](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1271.png)

![image 1272](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1272.png)

![image 1273](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1273.png)

![image 1274](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1274.png)

![image 1275](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1275.png)

![image 1276](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1276.png)

![image 1277](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1277.png)

![image 1278](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1278.png)

![image 1279](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1279.png)

![image 1280](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1280.png)

![image 1281](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1281.png)

![image 1282](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1282.png)

![image 1283](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1283.png)

![image 1284](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1284.png)

![image 1285](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1285.png)

![image 1286](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1286.png)

![image 1287](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1287.png)

![image 1288](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1288.png)

![image 1289](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1289.png)

![image 1290](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1290.png)

![image 1291](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1291.png)

![image 1292](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1292.png)

![image 1293](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1293.png)

![image 1294](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1294.png)

![image 1295](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1295.png)

![image 1296](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1296.png)

![image 1297](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1297.png)

![image 1298](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1298.png)

![image 1299](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1299.png)

![image 1300](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1300.png)

![image 1301](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1301.png)

![image 1302](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1302.png)

![image 1303](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1303.png)

![image 1304](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1304.png)

![image 1305](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1305.png)

![image 1306](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1306.png)

![image 1307](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1307.png)

![image 1308](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1308.png)

![image 1309](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1309.png)

![image 1310](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1310.png)

![image 1311](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1311.png)

![image 1312](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1312.png)

![image 1313](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1313.png)

![image 1314](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1314.png)

![image 1315](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1315.png)

![image 1316](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1316.png)

![image 1317](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1317.png)

![image 1318](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1318.png)

![image 1319](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1319.png)

![image 1320](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1320.png)

![image 1321](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1321.png)

![image 1322](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1322.png)

![image 1323](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1323.png)

![image 1324](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1324.png)

![image 1325](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1325.png)

![image 1326](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1326.png)

![image 1327](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1327.png)

![image 1328](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1328.png)

![image 1329](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1329.png)

![image 1330](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1330.png)

![image 1331](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1331.png)

![image 1332](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1332.png)

![image 1333](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1333.png)

![image 1334](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1334.png)

![image 1335](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1335.png)

![image 1336](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1336.png)

![image 1337](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1337.png)

![image 1338](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1338.png)

![image 1339](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1339.png)

![image 1340](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1340.png)

![image 1341](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1341.png)

![image 1342](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1342.png)

![image 1343](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1343.png)

![image 1344](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1344.png)

![image 1345](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1345.png)

![image 1346](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1346.png)

![image 1347](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1347.png)

![image 1348](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1348.png)

![image 1349](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1349.png)

![image 1350](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1350.png)

![image 1351](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1351.png)

REL ChemProt 76.68 83.64

![image 1352](Beltagy et al._2019_SciBERT A Pretrained Language Model for Scientific Text_images/imageFile1352.png)

- Table 2: Comparing SCIBERT with the reported BIOBERT results on biomedical datasets.


Cite (Cohan et al., 2019). No prior published SOTA results exist for the Paper Field dataset.

# 5 Discussion

- 5.1 Effect of Finetuning

We observe improved results via BERT ﬁnetuning rather than task-speciﬁc architectures atop frozen embeddings (+3.25 F1 with SCIBERT and +3.58 with BERT-Base, on average). For each scientiﬁc domain, we observe the largest effects of ﬁnetuning on the computer science (+5.59 F1 with SCIBERT and +3.17 F1 with BERT-Base) and biomedical tasks (+2.94 F1 with SCIBERT and +4.61 F1 with BERT-Base), and the smallest effect on multidomain tasks (+0.7 F1 with SCIBERT and +1.14 F1 with BERT-Base). On every dataset except BC5CDR and SciCite, BERT-Base with ﬁnetuning outperforms (or performs similarly to) a model using frozen SCIBERT embeddings.

- 5.2 Effect of SCIVOCAB


BC5CDR and ChemProt, and performs similarly on JNLPBA despite being trained on a substantially smaller biomedical corpus.

- 4.2 Computer Science Domain

We observe that SCIBERT outperforms BERTBase on computer science tasks (+3.55 F1 with ﬁnetuning and +1.13 F1 without). In addition, SCIBERT achieves new SOTA results on ACLARC (Cohan et al., 2019), and the NER part of SciERC (Luan et al., 2018). For relations in SciERC, our results are not comparable with those in Luan et al. (2018) because we are performing relation classiﬁcation given gold entities, while they perform joint entity and relation extraction.

- 4.3 Multiple Domains


We assess the importance of an in-domain scientiﬁc vocabulary by repeating the ﬁnetuning experiments for SCIBERT with BASEVOCAB. We ﬁnd the optimal hyperparameters for SCIBERTBASEVOCAB often coincide with those of SCIBERT-SCIVOCAB.

We observe that SCIBERT outperforms BERTBase on the multidomain tasks (+0.49 F1 with ﬁnetuning and +0.93 F1 without). In addition, SCIBERT outperforms the SOTA on Sci-

Averaged across datasets, we observe +0.60 F1 when using SCIVOCAB. For each scientiﬁc do-

main, we observe +0.76 F1 for biomedical tasks, +0.61 F1 for computer science tasks, and +0.11 F1 for multidomain tasks.

Given the disjoint vocabularies (Section 2) and the magnitude of improvement over BERT-Base (Section 4), we suspect that while an in-domain vocabulary is helpful, SCIBERT beneﬁts most from the scientiﬁc corpus pretraining.

# 6 Related Work

Recent work on domain adaptation of BERT includes BIOBERT (Lee et al., 2019) and CLINICALBERT (Alsentzer et al., 2019; Huang et al., 2019). BIOBERT is trained on PubMed abstracts and PMC full text articles, and CLINICALBERT is trained on clinical text from the MIMIC-III database (Johnson et al., 2016). In contrast, SCIBERT is trained on the full text of 1.14M biomedical and computer science papers from the Semantic Scholar corpus (Ammar et al., 2018). Furthermore, SCIBERT uses an in-domain vocabulary (SCIVOCAB) while the other abovementioned models use the original BERT vocabulary (BASEVOCAB).

# 7 Conclusion and Future Work

We released SCIBERT, a pretrained language model for scientiﬁc text based on BERT. We evaluated SCIBERT on a suite of tasks and datasets from scientiﬁc domains. SCIBERT signiﬁcantly outperformed BERT-Base and achieves new SOTA results on several of these tasks, even compared to some reported BIOBERT (Lee et al., 2019) results on biomedical tasks.

For future work, we will release a version of SCIBERT analogous to BERT-Large, as well as experiment with different proportions of papers from each domain. Because these language models are costly to train, we aim to build a single resource that’s useful across multiple domains.

# Acknowledgment

We thank the anonymous reviewers for their comments and suggestions. We also thank Waleed Ammar, Noah Smith, Yoav Goldberg, Daniel King, Doug Downey, and Dan Weld for their helpful discussions and feedback. All experiments were performed on beaker.org and supported in part by credits from Google Cloud.

# References

Emily Alsentzer, John R. Murphy, Willie Boag, WeiHung Weng, Di Jin, Tristan Naumann, and Matthew B. A. McDermott. 2019. Publicly available clinical bert embeddings. In ClinicalNLP workshop at NAACL.

Waleed Ammar, Dirk Groeneveld, Chandra Bhagavatula, Iz Beltagy, Miles Crawford, Doug Downey, Jason Dunkelberger, Ahmed Elgohary, Sergey Feldman, Vu Ha, Rodney Kinney, Sebastian Kohlmeier, Kyle Lo, Tyler Murray, Hsu-Han Ooi, Matthew Peters, Joanna Power, Sam Skjonsberg, Lucy Lu Wang, Chris Wilhelm, Zheng Yuan, Madeleine van Zuylen, and Oren Etzioni. 2018. Construction of the literature graph in semantic scholar. In NAACL.

Arman Cohan, Waleed Ammar, Madeleine van Zuylen, and Field Cady. 2019. Structural scaffolds for citation intent classiﬁcation in scientiﬁc publications.

In NAACL-HLT, pages 3586–3596, Minneapolis, Minnesota. Association for Computational Linguistics.

Nigel Collier and Jin-Dong Kim. 2004. Introduction to the bio-entity recognition task at jnlpba. In NLPBA/BioNLP.

Tim Dettmers. 2019. TPUs vs GPUs for Transformers (BERT). http://timdettmers.com/2018/10/17/tpus-vs-gpus-for-transformers-bert/. Accessed: 2019-02-22.

Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. 2019. BERT: Pre-training of deep bidirectional transformers for language understanding. In NAACL-HLT.

Rezarta Islamaj Dogan, Robert Leaman, and Zhiyong Lu. 2014. NCBI disease corpus: A resource for disease name recognition and concept normalization. Journal of biomedical informatics, 47:1–10.

Timothy Dozat and Christopher D. Manning. 2017. Deep biafﬁne attention for neural dependency parsing. ICLR.

Matt Gardner, Joel Grus, Mark Neumann, Oyvind Tafjord, Pradeep Dasigi, Nelson F. Liu, Matthew Peters, Michael Schmitz, and Luke S. Zettlemoyer. 2017. Allennlp: A deep semantic natural language processing platform. In arXiv:1803.07640.

Jeremy Howard and Sebastian Ruder. 2018. Universal language model ﬁne-tuning for text classiﬁcation. In ACL.

Kexin Huang, Jaan Altosaar, and Rajesh Ranganath.

2019. Clinicalbert: Modeling clinical notes and predicting hospital readmission. arXiv:1904.05342.

Alistair E. W. Johnson, Tom J. Pollard aand Lu Shen, Liwei H. Lehman, Mengling Feng, Mohammad Ghassemi, Benjamin Moody, Peter Szolovits, Leo Anthony Celi, , and Roger G. Mark. 2016.

Mimic-iii, a freely accessible critical care database. In Scientiﬁc Data, 3:160035.

David Jurgens, Srijan Kumar, Raine Hoover, Daniel A. McFarland, and Daniel Jurafsky. 2018. Measuring the evolution of a scientiﬁc ﬁeld through citation frames. TACL, 06:391–406.

Jin-Dong Kim, Tomoko Ohta, Yuka Tateisi, and Jun’ichi Tsujii. 2003. GENIA corpus - a semantically annotated corpus for bio-textmining. Bioinformatics, 19:i180i182.

Su Kim, David Martı´nez, Lawrence Cavedon, and Lars Yencken. 2011. Automatic classiﬁcation of sentences to support evidence based medicine. In BMC Bioinformatics.

Diederik P. Kingma and Jimmy Ba. 2015. Adam: A method for stochastic optimization. ICLR.

Jens Kringelum, Sonny Kim Kjærulff, Søren Brunak, Ole Lund, Tudor I. Oprea, and Olivier Taboureau. 2016. ChemProt-3.0: a global chemical biology diseases mapping. In Database.

Jinhyuk Lee, Wonjin Yoon, Sungdong Kim, Donghyeon Kim, Sunkyu Kim, Chan Ho So, and Jaewoo Kang. 2019. BioBERT: a pre-trained biomedical language representation model for biomedical text mining. In arXiv:1901.08746.

Jiao Li, Yueping Sun, Robin J. Johnson, Daniela Sciaky, Chih-Hsuan Wei, Robert Leaman, Allan Peter Davis, Carolyn J. Mattingly, Thomas C. Wiegers, and Zhiyong Lu. 2016. BioCreative V CDR task corpus: a resource for chemical disease relation extraction. Database : the journal of biological databases and curation.

Yi Luan, Luheng He, Mari Ostendorf, and Hannaneh Hajishirzi. 2018. Multi-task identiﬁcation of entities, relations, and coreference for scientiﬁc knowledge graph construction. In EMNLP.

Mark Neumann, Daniel King, Iz Beltagy, and Waleed Ammar. 2019. ScispaCy: Fast and robust models for biomedical natural language processing. In arXiv:1902.07669.

Dat Quoc Nguyen and Karin M. Verspoor. 2019. From pos tagging to dependency parsing for biomedical event extraction. BMC Bioinformatics, 20:1–13.

Benjamin Nye, Junyi Jessy Li, Roma Patel, Yinfei Yang, Iain James Marshall, Ani Nenkova, and Byron C. Wallace. 2018. A corpus with multi-level annotations of patients, interventions and outcomes to support language processing for medical literature. In ACL.

Matthew E. Peters, Mark Neumann, Mohit Iyyer, Matt Gardner, Christopher Clark, Kenton Lee, and Luke S. Zettlemoyer. 2018. Deep contextualized word representations. In NAACL-HLT.

Alec Radford, Karthik Narasimhan, Tim Salimans, and Ilya Sutskever. 2018. Improving language understanding by generative pre-training.

Nils Reimers and Iryna Gurevych. 2017. Optimal hyperparameters for deep lstm-networks for sequence labeling tasks. In EMNLP.

Arnab Sinha, Zhihong Shen, Yang Song, Hao Ma, Darrin Eide, Bo-June Paul Hsu, and Kuansan Wang. 2015. An overview of microsoft academic service (MAS) and applications. In WWW.

Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, and Illia Polosukhin. 2017. Attention is all you need. In NIPS.

Yonghui Wu, Mike Schuster, Zhifeng Chen, Quoc V. Le, Mohammad Norouzi, Wolfgang Macherey, Maxim Krikun, Yuan Cao, Qin Gao, Jeff Klingner, Apurva Shah, Melvin Johnson, Xiaobing Liu, Lukasz Kaiser, Stephan Gouws, Yoshikiyo Kato, Taku Kudo, Hideto Kazawa, Keith Stevens, George Kurian, Nishant Patil, Wei Wang, Cliff Young, Jason Smith, Jason Riesa, Alex Rudnick, Oriol Vinyals, Gregory S. Corrado, Macduff Hughes, and Jeffrey Dean. 2016. Google’s neural machine translation system: Bridging the gap between human and machine translation. abs/1609.08144.

Wonjin Yoon, Chan Ho So, Jinhyuk Lee, and Jaewoo Kang. 2018. CollaboNet: collaboration of deep neural networks for biomedical named entity recognition. In DTMBio workshop at CIKM.

