# arXiv:2603.25640v1[cs.DL]26 Mar 2026

## RENOBENCH: A CITATION PARSING BENCHMARK

parth sarin Graduate School of Education Stanford University Stanford, California, USA psarin@stanford.edu

Juan Pablo Alperin Public Knowledge Project Simon Fraser University Vancouver, British Columbia, Canada juan@alperin.ca

Dione Mentis DataCite Hannover, Germany dione.mentis@datacite.org

Adam Buttrick California Digital Library University of California Office of the President Oakland, California, USA Adam.Buttrick@ucop.edu

![image 1](RenoBench A Citation Parsing Benchmark_images/imageFile1.png)

Figure 1: An annotated citation from RenoBench

- 1 INTRODUCTION

Despite sustained interest in machine readable citations (Di Giambattista & Heibi, 2025; Weimer et al., 2025; CiteX, 2026; OpenCitations, 2025), there is currently no community-accepted dataset to evaluate citation parsing. To assist the community working on this task, we introduce the Reference Annotation Benchmark (RenoBench):1 a standardized evaluation benchmark for citation parsing, which we define as the task of annotating a plain-text reference with structured components following the JATS standard (National Information Standards Organization, 2024).

Existing benchmarks typically follow one of three patterns: First, many evaluations rely on small, hand-annotated datasets derived from a single discipline or venue (often computer science or biomedicine) such as those used to evaluate tools like GROBID and CERMINE (Lopez, 2009; Tkaczyk et al., 2018). Second, recently, synthetic citation datasets like GIANT have emerged which are designed to maximize coverage of citation styles (Grennan et al., 2019). These datasets have been shown to be useful in training contexts (Atanassova et al., 2020), but synthetic references do not capture noise introduced by PDF extraction, multilingual syntax conventions, and publisherspecific production workflows encountered in practice (Lipinski et al., 2013). Third, many citation parsers are evaluated on private datasets, limiting reproducibility (Tkaczyk et al., 2018).

In contrast, RenoBench was assembled by extracting plain-text references from public domain PDFs from multiple journals. To our knowledge, RenoBench is the first public domain citation parsing benchmark sourced from real-world, multi-ecosystem conditions. With its release, we hope to complement existing datasets and enable reproducible comparison of citation parsing systems under realistic operating conditions (Atanassova & Bertin, 2024).

- 2 METHODOLOGY 2.1 DATA SOURCES


Article PDFs and their JATS XML annotations were derived from four publication platforms: SciELO, Redalyc, PKP, and Open Research Europe (ORE). The latter two, PKP and ORE, are publicly

1https://huggingface.co/datasets/public-knowledge-project/ ref-annotation-benchmark

available (Garnett, 2016; European Commission, 2025). JATS XML files from Redalyc and SciELO were obtained through communication with these platforms in February and April 2025, respectively.

We obtained the PDF files associated with the JATS XML for each corpus. ORE maintains a public index of XML and PDF URLs;2 the PKP corpus contains PDF versions of each article; and Redalyc and SciELO have publicly available PDFs at predictable URLs associated with each DOI. We then converted PDFs to markdown using markitdown (Microsoft Corporation, 2025), a lightweight conversion utility widely used to generate unstructured inputs to language models.

- 2.2 PARSING AND MATCHING

Plain-text citations were extracted from the markdown using Llama-3.1-8B-Instruct, programmatically verifying that the extracted citations appeared in the input text to prevent hallucinations. These plain-text citations were then matched to the annotated citations in the corresponding JATS XML files. Plain-text citations p were matched to text-only (stripped) XML citations c in order of decreasing similarity, where similarity is defined as

s(p,c) = 1 −

d(p,c) max(|p|,|c|)

,

d(p,c) is the edit distance between p and c, and |s| denotes the number of characters in a string s. All matches with similarity less than 0.75 were excluded. This extraction and reconciliation procedure is described in more detail by sarin & Alperin (2025). This matching resulted in a total of 161,625 data points.

- 2.3 FILTERING

We applied a suite of automated quality checks to remove citations with structural or content errors that would introduce noise into the benchmark. These checks fall into three categories:

- 1. Structural validation checks ensured well-formed XML (e.g., parseable markup, no namespace pollution) and sufficient annotation depth (citations with ≤ 2 meaningful elements were excluded).
- 2. Field-level validation checks asserted regex-style heuristics against fields, detecting invalid dates (e.g., years with letter suffixes like “2020a”, months > 12); problematic page numbers (e.g., reversed ranges where lpage < fpage, extreme values > 10,000 suggesting DOI fragments, or identical start and end pages); field confusion (e.g., years appearing in author fields, URLs in title fields); and author anomalies (e.g., initials stored as surnames, “et al.” parsed as an author name).
- 3. Content consistency checks aligned the structured annotation and the plain-text citation by fuzzy matching extracted surnames, sources, and article titles against the plain-text.


Of the 161,625 matched citation pairs, 115,193 (71.3%) passed all quality checks. The most common failure reasons were missing page numbers for journal articles (27.7% of errors) and reversed page number ranges (14.4%). We excluded citation pairs that failed these checks.

- 2.4 SAMPLING


To construct a dataset capturing a range of contexts, we sought to balance the mix of cited languages, citing and cited publication types, presence of persistent identifiers (PIDs), and publication platform. To impute the cited article language, Llama-3.1-8B-Instruct was used to return the twoletter ISO 639 language code based on the article title. The same model and input were also used to identify whether the citation contained a PID. Each citation was then represented as a binary feature vector encoding PID presence, preprint status, title language (one-hot), publication type (one-hot), and citation source (one-hot).

2https://open-research-europe.ec.europa.eu/published-xml-urls, https: //open-research-europe.ec.europa.eu/about/developers

Rather than sample uniformly, we optimized sampling weights to balance across these features using the following procedure: Let N be the number of total citations and let fi ∈ Rd be the feature vector for the ith data point, xi. Take λ ∈ Rd to be a learnable collection of parameters. Assign a softmax sampling weight to each data point wi ← exp(λ⊺fi), so that the probability that xi is sampled in the first round is

exp(λ⊺fi)

pi(λ) =

.

N j=1 exp(λ⊺fj)

Then, define the aggregate feature vector to be µ(λ) = Ei∼p[fi] = Ni=1 pi(λ)fi, intended to represent a “soft” sample, differentiable with respect to λ. A loss function L(µ) was then designed

to encourage adequate representation/balance. After 1,963 steps at learning rate 10−3, convergence was reached and the final dataset, which contains 10,000 citations, was sampled.

- 2.5 DATASET COMPOSITION The resulting benchmark dataset has the following composition:


- • 59% of citations include a persistent identifier (PID)
- • 14% of the citing articles are preprints
- • Citations span eight languages, with English (32%), Portuguese (30%), and Spanish (23%) most common, followed by French (7%), German (3%), Italian (2%), Russian (2%), and Chinese (1%)
- • Publication types include journal articles (53%), books (30%), website pages (8%), theses (5%), and conference proceedings (4%)
- • Documents are sourced from four platforms: SciELO (47%), Redalyc (24%), ORE (14%), and PKP (14%)


3 EVALUATION

Several models were evaluated on RenoBench, including GROBID (Lopez, 2009), Qwen2.5 (Yang et al., 2025b), Qwen3 (Yang et al., 2025a), Mistral (Jiang et al., 2023), Gemma (Gemma et al., 2025), Llama (Grattafiori et al., 2024), and GPT-OSS (OpenAI et al., 2025). The largest model tested was Qwen3-32B and the smallest was GROBID. We evaluated each of the language models by running inference on the Stanford Marlowe compute cluster (Kapfer et al., 2025) with a prompt that provided two annotated examples of citations that were not included in the benchmark. GROBID was evaluated by querying its web API hosted on Hugging Face Spaces. We also evaluated a finetuned version of Qwen3-0.6B produced by COMET (2025) following the procedure described in sarin & Alperin (2025). Table 1 shows the recall accuracy of different models for different markup fields.

We believe that precision is an unreliable metric on this dataset because the JATS XML often omits valid markup elements that models correctly produce. We evaluated all of the models for precision and manually reviewed 330 randomly sampled errors. We found that correct annotations were being marked as incorrect due to incomplete ground truth 92% of the time for the year field, 85% for the source field, and 72% for the article-title field. For completeness, we still report precision in Table 2.

Tables 1 and 2 report accuracy where, even if the model produced malformed XML, we still considered assertions for fields if they appeared between valid XML tags (e.g., <year>2026</year> may be asserted even if the <mixed-citation> tag is not closed). Tables 3 and 4 report stricter recall and precision metrics, which do not consider those assertions, such that field-level accuracy is bounded above by the valid XML percentage.

Finally, we attempted to optimize the prompt using GEPA (Agrawal et al., 2025), using recall on a held-out training subset as the optimization objective. Prompt optimization did not yield consistent or meaningful improvements over the baseline prompts for any of the evaluated models so we do not report these results.

Table 1: Recall Across Models and Fields

Model Valid XML Surname Given Title Source Volume Issue Year GROBID 100.0 71.6 18.8 65.2 51.8 90.0 86.8 97.9 Qwen/Qwen2.5-3B-Instruct 83.5 93.0 64.1 93.9 54.3 95.5 83.8 93.8 Qwen/Qwen2.5-7B-Instruct 87.6 95.8 74.5 94.0 53.3 96.0 86.9 90.6 Qwen/Qwen3-0.6B 81.4 87.3 62.7 84.7 50.6 92.4 92.7 91.7 Qwen/Qwen3-0.6B

95.0 92.6 77.9 93.4 73.3 98.6 95.3 97.2

+ cometadata/citation-parsing-lora

Qwen/Qwen3-8B 78.2 86.6 70.9 82.0 51.2 90.6 89.8 80.7 Qwen/Qwen3-32B 78.4 86.8 69.2 84.7 55.6 92.3 90.5 86.2 google/gemma-3-1b-it 27.7 84.9 52.5 44.5 37.4 70.9 64.0 69.8 meta-llama/Llama-3.1-8B-Instruct 80.3 82.4 58.6 92.7 57.3 98.1 96.0 94.5 mistralai/Mistral-7B-Instruct-v0.2 86.0 85.4 69.0 91.9 52.8 95.8 94.3 91.6 openai/gpt-oss-20b 88.3 89.1 67.0 93.1 57.4 98.1 96.5 96.7

All values represent recall (%) on field extraction from bibliographic citations. Bold indicates best performance in each column. Valid XML shows the percentage of examples producing well-formed, parseable XML. Field extraction uses a parser with regex fallback to recover fields from malformed XML. Edit distance thresholds: surname/year/volume/issue = 0 (exact), source = 5, title = 10.

4 CONCLUSION

RenoBench provides the first public domain benchmark for evaluating citation parsing under realworld scholarly publishing conditions. Our hope is that it will enable more meaningful and transparent comparisons of reference markup systems that are grounded in references that are noisy, heterogeneous, and multilingual. In presenting our RenoBench, our own evaluations highlight how language models perform on this task relative to established tools and demonstrate the promise of small, domain-specific language models for citation parsing. We see RenoBench as a foundation for future work on improved models and downstream citation indexing applications. If the benchmark proves useful, we propose that it be expanded with higher-fidelity ground truth (i.e., with more detailed JATS tagging) to support more reliable precision evaluation.

REFERENCES

Lakshya A Agrawal, Shangyin Tan, Dilara Soylu, Noah Ziems, Rishi Khare, Krista Opsahl-Ong, Arnav Singhvi, Herumb Shandilya, Michael J Ryan, Meng Jiang, Christopher Potts, Koushik Sen, Alexandros G. Dimakis, Ion Stoica, Dan Klein, Matei Zaharia, and Omar Khattab. GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning, 2025. URL https: //arxiv.org/abs/2507.19457.

Iana Atanassova and Marc Bertin. Breaking Boundaries in Citation Parsing: A Comparative Study of Generative LLMs and Traditional Out-of-the-box Citation Parsers. In Proceedings of the 14th Workshop on Bibliometric-enhanced Information Retrieval (BIR). CEUR-WS, 2024.

Iana Atanassova, Marc Bertin, and Philipp Mayr. Synthetic versus Real Reference Strings for Citation Parsing. In Proceedings of the 16th International Conference on Semantic Systems, pp. 165–172. ACM, 2020.

CiteX. CiteX: Workshop on Citation Extraction and Parsing. https://sites.google.com/ view/workshop-on-citation-extractio/startseite, 2026. Workshop website (accessed 2026-01-13).

COMET. cometadata/citation-parsing-lora-qwen3-0.6b. https://huggingface.co/ cometadata/citation-parsing-lora-qwen3-0.6b, 2025. Hugging Face Model.

Chiara Di Giambattista and Ivan Heibi. OpenCitations: an open infrastructure enabling Open Research Information. Zenodo, October 2025. doi: 10.5281/zenodo.17199853. URL https: //doi.org/10.5281/zenodo.17199853.

European Commission. Open Research Europe: Full article corpus. https:// open-research-europe.ec.europa.eu, 2025. Complete collection of all articles published on Open Research Europe; accessed 19 March 2025.

Alex Garnett. The XML Markup Evaluation Corpus, April 2016. URL https://pkp.sfu.ca/ 2016/04/18/the-xml-markup-evaluation-corpus/.

Gemma, Aishwarya Kamath, Johan Ferret, Shreya Pathak, Nino Vieillard, Ramona Merhej, Sarah Perrin, Tatiana Matejovicova, Alexandre Ram´e, Morgane Rivi`ere, Louis Rouillard, Thomas Mesnard, Geoffrey Cideron, Jean bastien Grill, Sabela Ramos, Edouard Yvinec, Michelle Casbon, Etienne Pot, Ivo Penchev, Ga¨el Liu, Francesco Visin, Kathleen Kenealy, Lucas Beyer, Xiaohai Zhai, Anton Tsitsulin, Robert Busa-Fekete, Alex Feng, Noveen Sachdeva, Benjamin Coleman, Yi Gao, Basil Mustafa, Iain Barr, Emilio Parisotto, David Tian, Matan Eyal, Colin Cherry, JanThorsten Peter, Danila Sinopalnikov, Surya Bhupatiraju, Rishabh Agarwal, Mehran Kazemi, Dan Malkin, Ravin Kumar, David Vilar, Idan Brusilovsky, Jiaming Luo, Andreas Steiner, Abe Friesen, Abhanshu Sharma, Abheesht Sharma, Adi Mayrav Gilady, Adrian Goedeckemeyer, Alaa Saade, Alex Feng, Alexander Kolesnikov, Alexei Bendebury, Alvin Abdagic, Amit Vadi, Andr´as Gy¨orgy, Andr´e Susano Pinto, Anil Das, Ankur Bapna, Antoine Miech, Antoine Yang, Antonia Paterson, Ashish Shenoy, Ayan Chakrabarti, Bilal Piot, Bo Wu, Bobak Shahriari, Bryce Petrini, Charlie Chen, Charline Le Lan, Christopher A. Choquette-Choo, CJ Carey, Cormac Brick, Daniel Deutsch, Danielle Eisenbud, Dee Cattle, Derek Cheng, Dimitris Paparas, Divyashree Shivakumar Sreepathihalli, Doug Reid, Dustin Tran, Dustin Zelle, Eric Noland, Erwin Huizenga, Eugene Kharitonov, Frederick Liu, Gagik Amirkhanyan, Glenn Cameron, Hadi Hashemi, Hanna Klimczak-Pluci´nska, Harman Singh, Harsh Mehta, Harshal Tushar Lehri, Hussein Hazimeh, Ian Ballantyne, Idan Szpektor, Ivan Nardini, Jean Pouget-Abadie, Jetha Chan, Joe Stanton, John Wieting, Jonathan Lai, Jordi Orbay, Joseph Fernandez, Josh Newlan, Ju yeong Ji, Jyotinder Singh, Kat Black, Kathy Yu, Kevin Hui, Kiran Vodrahalli, Klaus Greff, Linhai Qiu, Marcella Valentine, Marina Coelho, Marvin Ritter, Matt Hoffman, Matthew Watson, Mayank Chaturvedi, Michael Moynihan, Min Ma, Nabila Babar, Natasha Noy, Nathan Byrd, Nick Roy, Nikola Momchev, Nilay Chauhan, Noveen Sachdeva, Oskar Bunyan, Pankil Botarda, Paul Caron, Paul Kishan Rubenstein, Phil Culliton, Philipp Schmid, Pier Giuseppe Sessa, Pingmei Xu, Piotr Stanczyk, Pouya Tafti, Rakesh Shivanna, Renjie Wu, Renke Pan, Reza Rokni, Rob Willoughby, Rohith Vallu, Ryan Mullins, Sammy Jerome, Sara Smoot, Sertan Girgin, Shariq Iqbal, Shashir Reddy, Shruti Sheth, Siim P˜oder, Sijal Bhatnagar, Sindhu Raghuram Panyam, Sivan Eiger, Susan Zhang, Tianqi Liu, Trevor Yacovone, Tyler Liechty, Uday Kalra, Utku Evci, Vedant Misra, Vincent Roseberry,

Vlad Feinberg, Vlad Kolesnikov, Woohyun Han, Woosuk Kwon, Xi Chen, Yinlam Chow, Yuvein Zhu, Zichuan Wei, Zoltan Egyed, Victor Cotruta, Minh Giang, Phoebe Kirk, Anand Rao, Kat Black, Nabila Babar, Jessica Lo, Erica Moreira, Luiz Gustavo Martins, Omar Sanseviero, Lucas Gonzalez, Zach Gleicher, Tris Warkentin, Vahab Mirrokni, Evan Senter, Eli Collins, Joelle Barral, Zoubin Ghahramani, Raia Hadsell, Yossi Matias, D. Sculley, Slav Petrov, Noah Fiedel, Noam Shazeer, Oriol Vinyals, Jeff Dean, Demis Hassabis, Koray Kavukcuoglu, Clement Farabet, Elena Buchatskaya, Jean-Baptiste Alayrac, Rohan Anil, Dmitry, Lepikhin, Sebastian Borgeaud, Olivier Bachem, Armand Joulin, Alek Andreev, Cassidy Hardin, Robert Dadashi, and L´eonard Hussenot. Gemma 3 Technical Report, 2025. URL https://arxiv.org/abs/2503.19786.

Aaron Grattafiori, Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian, Ahmad Al-Dahle, Aiesha Letman, Akhil Mathur, Alan Schelten, Alex Vaughan, Amy Yang, Angela Fan, Anirudh Goyal, Anthony Hartshorn, Aobo Yang, Archi Mitra, Archie Sravankumar, Artem Korenev, Arthur Hinsvark, Arun Rao, Aston Zhang, Aurelien Rodriguez, Austen Gregerson, Ava Spataru, Baptiste Roziere, Bethany Biron, Binh Tang, Bobbie Chern, Charlotte Caucheteux, Chaya Nayak, Chloe Bi, Chris Marra, Chris McConnell, Christian Keller, Christophe Touret, Chunyang Wu, Corinne Wong, Cristian Canton Ferrer, Cyrus Nikolaidis, Damien Allonsius, Daniel Song, Danielle Pintz, Danny Livshits, Danny Wyatt, David Esiobu, Dhruv Choudhary, Dhruv Mahajan, Diego Garcia-Olano, Diego Perino, Dieuwke Hupkes, Egor Lakomkin, Ehab AlBadawy, Elina Lobanova, Emily Dinan, Eric Michael Smith, Filip Radenovic, Francisco Guzm´an, Frank Zhang, Gabriel Synnaeve, Gabrielle Lee, Georgia Lewis Anderson, Govind Thattai, Graeme Nail, Gregoire Mialon, Guan Pang, Guillem Cucurell, Hailey Nguyen, Hannah Korevaar, Hu Xu, Hugo Touvron, Iliyan Zarov, Imanol Arrieta Ibarra, Isabel Kloumann, Ishan Misra, Ivan Evtimov, Jack Zhang, Jade Copet, Jaewon Lee, Jan Geffert, Jana Vranes, Jason Park, Jay Mahadeokar, Jeet Shah, Jelmer van der Linde, Jennifer Billock, Jenny Hong, Jenya Lee, Jeremy Fu, Jianfeng Chi, Jianyu Huang, Jiawen Liu, Jie Wang, Jiecao Yu, Joanna Bitton, Joe Spisak, Jongsoo Park, Joseph Rocca, Joshua Johnstun, Joshua Saxe, Junteng Jia, Kalyan Vasuden Alwala, Karthik Prasad, Kartikeya Upasani, Kate Plawiak, Ke Li, Kenneth Heafield, Kevin Stone, Khalid El-Arini, Krithika Iyer, Kshitiz Malik, Kuenley Chiu, Kunal Bhalla, Kushal Lakhotia, Lauren Rantala-Yeary, Laurens van der Maaten, Lawrence Chen, Liang Tan, Liz Jenkins, Louis Martin, Lovish Madaan, Lubo Malo, Lukas Blecher, Lukas Landzaat, Luke de Oliveira, Madeline Muzzi, Mahesh Pasupuleti, Mannat Singh, Manohar Paluri, Marcin Kardas, Maria Tsimpoukelli, Mathew Oldham, Mathieu Rita, Maya Pavlova, Melanie Kambadur, Mike Lewis, Min Si, Mitesh Kumar Singh, Mona Hassan, Naman Goyal, Narjes Torabi, Nikolay Bashlykov, Nikolay Bogoychev, Niladri Chatterji, Ning Zhang, Olivier Duchenne, Onur ¸Celebi, Patrick Alrassy, Pengchuan Zhang, Pengwei Li, Petar Vasic, Peter Weng, Prajjwal Bhargava, Pratik Dubal, Praveen Krishnan, Punit Singh Koura, Puxin Xu, Qing He, Qingxiao Dong, Ragavan Srinivasan, Raj Ganapathy, Ramon Calderer, Ricardo Silveira Cabral, Robert Stojnic, Roberta Raileanu, Rohan Maheswari, Rohit Girdhar, Rohit Patel, Romain Sauvestre, Ronnie Polidoro, Roshan Sumbaly, Ross Taylor, Ruan Silva, Rui Hou, Rui Wang, Saghar Hosseini, Sahana Chennabasappa, Sanjay Singh, Sean Bell, Seohyun Sonia Kim, Sergey Edunov, Shaoliang Nie, Sharan Narang, Sharath Raparthy, Sheng Shen, Shengye Wan, Shruti Bhosale, Shun Zhang, Simon Vandenhende, Soumya Batra, Spencer Whitman, Sten Sootla, Stephane Collot, Suchin Gururangan, Sydney Borodinsky, Tamar Herman, Tara Fowler, Tarek Sheasha, Thomas Georgiou, Thomas Scialom, Tobias Speckbacher, Todor Mihaylov, Tong Xiao, Ujjwal Karn, Vedanuj Goswami, Vibhor Gupta, Vignesh Ramanathan, Viktor Kerkez, Vincent Gonguet, Virginie Do, Vish Vogeti, V´ıtor Albiero, Vladan Petrovic, Weiwei Chu, Wenhan Xiong, Wenyin Fu, Whitney Meers, Xavier Martinet, Xiaodong Wang, Xiaofang Wang, Xiaoqing Ellen Tan, Xide Xia, Xinfeng Xie, Xuchao Jia, Xuewei Wang, Yaelle Goldschlag, Yashesh Gaur, Yasmine Babaei, Yi Wen, Yiwen Song, Yuchen Zhang, Yue Li, Yuning Mao, Zacharie Delpierre Coudert, Zheng Yan, Zhengxing Chen, Zoe Papakipos, Aaditya Singh, Aayushi Srivastava, Abha Jain, Adam Kelsey, Adam Shajnfeld, Adithya Gangidi, Adolfo Victoria, Ahuva Goldstand, Ajay Menon, Ajay Sharma, Alex Boesenberg, Alexei Baevski, Allie Feinstein, Amanda Kallet, Amit Sangani, Amos Teo, Anam Yunus, Andrei Lupu, Andres Alvarado, Andrew Caples, Andrew Gu, Andrew Ho, Andrew Poulton, Andrew Ryan, Ankit Ramchandani, Annie Dong, Annie Franco, Anuj Goyal, Aparajita Saraf, Arkabandhu Chowdhury, Ashley Gabriel, Ashwin Bharambe, Assaf Eisenman, Azadeh Yazdan, Beau James, Ben Maurer, Benjamin Leonhardi, Bernie Huang, Beth Loyd, Beto De Paola, Bhargavi Paranjape, Bing Liu, Bo Wu, Boyu Ni, Braden Hancock, Bram Wasti, Brandon Spence, Brani Stojkovic, Brian Gamido, Britt Montalvo, Carl Parker, Carly Burton, Catalina Mejia, Ce Liu, Changhan Wang, Changkyu Kim, Chao

Zhou, Chester Hu, Ching-Hsiang Chu, Chris Cai, Chris Tindal, Christoph Feichtenhofer, Cynthia Gao, Damon Civin, Dana Beaty, Daniel Kreymer, Daniel Li, David Adkins, David Xu, Davide Testuggine, Delia David, Devi Parikh, Diana Liskovich, Didem Foss, Dingkang Wang, Duc Le, Dustin Holland, Edward Dowling, Eissa Jamil, Elaine Montgomery, Eleonora Presani, Emily Hahn, Emily Wood, Eric-Tuan Le, Erik Brinkman, Esteban Arcaute, Evan Dunbar, Evan Smothers, Fei Sun, Felix Kreuk, Feng Tian, Filippos Kokkinos, Firat Ozgenel, Francesco Caggioni, Frank Kanayet, Frank Seide, Gabriela Medina Florez, Gabriella Schwarz, Gada Badeer, Georgia Swee, Gil Halpern, Grant Herman, Grigory Sizov, Guangyi, Zhang, Guna Lakshminarayanan, Hakan Inan, Hamid Shojanazeri, Han Zou, Hannah Wang, Hanwen Zha, Haroun Habeeb, Harrison Rudolph, Helen Suk, Henry Aspegren, Hunter Goldman, Hongyuan Zhan, Ibrahim Damlaj, Igor Molybog, Igor Tufanov, Ilias Leontiadis, Irina-Elena Veliche, Itai Gat, Jake Weissman, James Geboski, James Kohli, Janice Lam, Japhet Asher, Jean-Baptiste Gaya, Jeff Marcus, Jeff Tang, Jennifer Chan, Jenny Zhen, Jeremy Reizenstein, Jeremy Teboul, Jessica Zhong, Jian Jin, Jingyi Yang, Joe Cummings, Jon Carvill, Jon Shepard, Jonathan McPhie, Jonathan Torres, Josh Ginsburg, Junjie Wang, Kai Wu, Kam Hou U, Karan Saxena, Kartikay Khandelwal, Katayoun Zand, Kathy Matosich, Kaushik Veeraraghavan, Kelly Michelena, Keqian Li, Kiran Jagadeesh, Kun Huang, Kunal Chawla, Kyle Huang, Lailin Chen, Lakshya Garg, Lavender A, Leandro Silva, Lee Bell, Lei Zhang, Liangpeng Guo, Licheng Yu, Liron Moshkovich, Luca Wehrstedt, Madian Khabsa, Manav Avalani, Manish Bhatt, Martynas Mankus, Matan Hasson, Matthew Lennie, Matthias Reso, Maxim Groshev, Maxim Naumov, Maya Lathi, Meghan Keneally, Miao Liu, Michael L. Seltzer, Michal Valko, Michelle Restrepo, Mihir Patel, Mik Vyatskov, Mikayel Samvelyan, Mike Clark, Mike Macey, Mike Wang, Miquel Jubert Hermoso, Mo Metanat, Mohammad Rastegari, Munish Bansal, Nandhini Santhanam, Natascha Parks, Natasha White, Navyata Bawa, Nayan Singhal, Nick Egebo, Nicolas Usunier, Nikhil Mehta, Nikolay Pavlovich Laptev, Ning Dong, Norman Cheng, Oleg Chernoguz, Olivia Hart, Omkar Salpekar, Ozlem Kalinli, Parkin Kent, Parth Parekh, Paul Saab, Pavan Balaji, Pedro Rittner, Philip Bontrager, Pierre Roux, Piotr Dollar, Polina Zvyagina, Prashant Ratanchandani, Pritish Yuvraj, Qian Liang, Rachad Alao, Rachel Rodriguez, Rafi Ayub, Raghotham Murthy, Raghu Nayani, Rahul Mitra, Rangaprabhu Parthasarathy, Raymond Li, Rebekkah Hogan, Robin Battey, Rocky Wang, Russ Howes, Ruty Rinott, Sachin Mehta, Sachin Siby, Sai Jayesh Bondu, Samyak Datta, Sara Chugh, Sara Hunt, Sargun Dhillon, Sasha Sidorov, Satadru Pan, Saurabh Mahajan, Saurabh Verma, Seiji Yamamoto, Sharadh Ramaswamy, Shaun Lindsay, Shaun Lindsay, Sheng Feng, Shenghao Lin, Shengxin Cindy Zha, Shishir Patil, Shiva Shankar, Shuqiang Zhang, Shuqiang Zhang, Sinong Wang, Sneha Agarwal, Soji Sajuyigbe, Soumith Chintala, Stephanie Max, Stephen Chen, Steve Kehoe, Steve Satterfield, Sudarshan Govindaprasad, Sumit Gupta, Summer Deng, Sungmin Cho, Sunny Virk, Suraj Subramanian, Sy Choudhury, Sydney Goldman, Tal Remez, Tamar Glaser, Tamara Best, Thilo Koehler, Thomas Robinson, Tianhe Li, Tianjun Zhang, Tim Matthews, Timothy Chou, Tzook Shaked, Varun Vontimitta, Victoria Ajayi, Victoria Montanez, Vijai Mohan, Vinay Satish Kumar, Vishal Mangla, Vlad Ionescu, Vlad Poenaru, Vlad Tiberiu Mihailescu, Vladimir Ivanov, Wei Li, Wenchen Wang, Wenwen Jiang, Wes Bouaziz, Will Constable, Xiaocheng Tang, Xiaojian Wu, Xiaolan Wang, Xilun Wu, Xinbo Gao, Yaniv Kleinman, Yanjun Chen, Ye Hu, Ye Jia, Ye Qi, Yenda Li, Yilin Zhang, Ying Zhang, Yossi Adi, Youngjin Nam, Yu, Wang, Yu Zhao, Yuchen Hao, Yundi Qian, Yunlu Li, Yuzi He, Zach Rait, Zachary DeVito, Zef Rosnbrick, Zhaoduo Wen, Zhenyu Yang, Zhiwei Zhao, and Zhiyu Ma. The Llama 3 Herd of Models, 2024. URL https://arxiv.org/abs/2407.21783.

Mark Grennan, Martin Schibel, Andrew Collins, and Joeran Beel. GIANT: The 1-Billion Annotated Synthetic Bibliographic-Reference-String Dataset for Deep Citation Parsing. In Edward Curry, Mark T. Keane, Adegboyega Ojo, and Dhaval Salwala (eds.), Proceedings for the 27th AIAI Irish Conference on Artificial Intelligence and Cognitive Science, Galway, Ireland, December 5-6, 2019, volume 2563 of CEUR Workshop Proceedings, pp. 260–271. CEUR-WS.org, 2019. URL https://ceur-ws.org/Vol-2563/aics_25.pdf.

AQ Jiang, A Sablayrolles, et al. Mistral 7B. arXiv preprint arXiv:2310.06825, 2023. URL https: //arxiv.org/abs/2310.06825.

Craig Kapfer, Kurt Stine, Balasubramanian Narasimhan, Christopher Mentzel, and Emmanuel Candes. Marlowe: Stanford’s GPU-based Computational Instrument, January 2025. URL https://doi.org/10.5281/zenodo.14751899.

Matthias Lipinski, Kai Yao, Corinna Breitinger, Joeran Beel, and Bela Gipp. Evaluation of Header Metadata Extraction Approaches and Tools for Scientific PDF Documents. In Proceedings of the 13th ACM/IEEE-CS Joint Conference on Digital Libraries, pp. 385–386. ACM, 2013.

Patrice Lopez. GROBID: Combining Automatic Bibliographic Data Recognition and Term Extraction for Scholarship Publications. International Journal on Document Analysis and Recognition, 13(1):1–23, 2009.

Microsoft Corporation. MarkItDown: A Python Tool for Converting Files to Markdown, 2025. URL https://github.com/microsoft/markitdown. Version 0.1.1.

National Information Standards Organization. ANSI/NISO Z39.96-2024: JATS: Journal Article Tag Suite, 2024. URL https://www.niso.org/publications/z3996-2024-jats. Approved as the standard for XML tagging of journal article content.

OpenAI, Sandhini Agarwal, Lama Ahmad, Jason Ai, Sam Altman, Andy Applebaum, Edwin Arbus, Rahul K. Arora, Yu Bai, Bowen Baker, Haiming Bao, Boaz Barak, Ally Bennett, Tyler Bertao, Nivedita Brett, Eugene Brevdo, Greg Brockman, Sebastien Bubeck, Che Chang, Kai Chen, Mark Chen, Enoch Cheung, Aidan Clark, Dan Cook, Marat Dukhan, Casey Dvorak, Kevin Fives, Vlad Fomenko, Timur Garipov, Kristian Georgiev, Mia Glaese, Tarun Gogineni, Adam Goucher, Lukas Gross, Katia Gil Guzman, John Hallman, Jackie Hehir, Johannes Heidecke, Alec Helyar, Haitang Hu, Romain Huet, Jacob Huh, Saachi Jain, Zach Johnson, Chris Koch, Irina Kofman, Dominik Kundel, Jason Kwon, Volodymyr Kyrylov, Elaine Ya Le, Guillaume Leclerc, James Park Lennon, Scott Lessans, Mario Lezcano-Casado, Yuanzhi Li, Zhuohan Li, Ji Lin, Jordan Liss, Lily, Liu, Jiancheng Liu, Kevin Lu, Chris Lu, Zoran Martinovic, Lindsay McCallum, Josh McGrath, Scott McKinney, Aidan McLaughlin, Song Mei, Steve Mostovoy, Tong Mu, Gideon Myles, Alexander Neitz, Alex Nichol, Jakub Pachocki, Alex Paino, Dana Palmie, Ashley Pantuliano, Giambattista Parascandolo, Jongsoo Park, Leher Pathak, Carolina Paz, Ludovic Peran, Dmitry Pimenov, Michelle Pokrass, Elizabeth Proehl, Huida Qiu, Gaby Raila, Filippo Raso, Hongyu Ren, Kimmy Richardson, David Robinson, Bob Rotsted, Hadi Salman, Suvansh Sanjeev, Max Schwarzer, D. Sculley, Harshit Sikchi, Kendal Simon, Karan Singhal, Yang Song, Dane Stuckey, Zhiqing Sun, Philippe Tillet, Sam Toizer, Foivos Tsimpourlas, Nikhil Vyas, Eric Wallace, Xin Wang, Miles Wang, Olivia Watkins, Kevin Weil, Amy Wendling, Kevin Whinnery, Cedric Whitney, Hannah Wong, Lin Yang, Yu Yang, Michihiro Yasunaga, Kristen Ying, Wojciech Zaremba, Wenting Zhan, Cyril Zhang, Brian Zhang, Eddie Zhang, and Shengjia Zhao. gpt-oss120b & gpt-oss-20b Model Card, 2025. URL https://arxiv.org/abs/2508.10925.

OpenCitations. Workshop on Open Citations and Open Scholarly Metadata. https:// workshop-oc.github.io/, 2025. Workshop website (accessed 2026-01-13).

parth sarin and Juan Pablo Alperin. Citation Parsing and Analysis with Language Models. arXiv preprint arXiv:2505.15948, 2025.

Dominika Tkaczyk, Mateusz Fedoryszak, Piotr Dendek, and Łukasz Bolikowski. Evaluation and Comparison of Open Source Bibliographic Reference Parsers. Scientometrics, 117(1):1–29, 2018.

Verena Weimer, Muhammad Ahsan Shahid, Tamara Heck, Thomas Oerder, Philipp Mayr, and Christoph Schindler. Open Citation Data for Educational Research. Zenodo, October 2025. doi: 10.5281/zenodo.16325125. URL https://doi.org/10.5281/zenodo.16325125.

An Yang, Anfeng Li, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu, Chang Gao, Chengen Huang, Chenxu Lv, Chujie Zheng, Dayiheng Liu, Fan Zhou, Fei Huang, Feng Hu, Hao Ge, Haoran Wei, Huan Lin, Jialong Tang, Jian Yang, Jianhong Tu, Jianwei Zhang, Jianxin Yang, Jiaxi Yang, Jing Zhou, Jingren Zhou, Junyang Lin, Kai Dang, Keqin Bao, Kexin Yang, Le Yu, Lianghao Deng, Mei Li, Mingfeng Xue, Mingze Li, Pei Zhang, Peng Wang, Qin Zhu, Rui Men, Ruize Gao, Shixuan Liu, Shuang Luo, Tianhao Li, Tianyi Tang, Wenbiao Yin, Xingzhang Ren, Xinyu Wang, Xinyu Zhang, Xuancheng Ren, Yang Fan, Yang Su, Yichang Zhang, Yinger Zhang, Yu Wan, Yuqiong Liu, Zekun Wang, Zeyu Cui, Zhenru Zhang, Zhipeng Zhou, and Zihan Qiu. Qwen3 Technical Report, 2025a. URL https://arxiv.org/abs/2505.09388.

An Yang, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu, Chengyuan Li, Dayiheng Liu, Fei Huang, Haoran Wei, Huan Lin, and et al. Qwen2.5 Technical Report. arXiv preprint arXiv:2412.15115, 2025b. URL http://arxiv.org/abs/2412.15115.

A APPENDIX

Table 2: Precision Across Models and Fields

Model Valid XML Surname Given Title Source Volume Issue Year

- GROBID 100.0 70.2 18.7 58.4 48.0 69.8 49.1 96.9 Qwen/Qwen2.5-3B-Instruct 83.5 86.5 62.5 56.0 53.4 86.7 88.0 97.7 Qwen/Qwen2.5-7B-Instruct 87.6 89.0 72.3 59.2 53.0 87.1 78.3 98.2 Qwen/Qwen3-0.6B 81.4 79.5 59.0 51.1 47.4 42.9 25.7 95.1 Qwen/Qwen3-0.6B

+ cometadata/citation-parsing-lora

95.0 83.6 73.5 55.7 66.9 43.5 25.2 96.4

Qwen/Qwen3-8B 78.2 91.8 76.1 60.2 59.1 82.3 74.5 91.4 Qwen/Qwen3-32B 78.4 89.5 71.8 60.9 59.7 86.4 78.2 92.4 google/gemma-3-1b-it 27.7 81.3 49.8 41.1 48.2 57.6 34.1 94.5 meta-llama/Llama-3.1-8B-Instruct 80.3 79.2 58.3 60.7 59.1 85.4 74.3 98.4 mistralai/Mistral-7B-Instruct-v0.2 86.0 85.2 69.3 61.0 65.2 88.7 71.7 97.8 openai/gpt-oss-20b 88.3 85.1 65.8 60.1 57.7 88.4 84.8 98.2

All values represent precision (%) on field extraction from bibliographic citations. Bold indicates best performance in each column. Valid XML shows the percentage of examples producing well-formed, parseable XML. Precision measures the fraction of generated fields that are correct (avoiding hallucinations). Edit distance thresholds: surname/year/volume/issue = 0 (exact), source = 5, title = 10.

Table 3: Recall (Strict) Across Models and Fields

Model Valid XML Surname Given Title Source Volume Issue Year

- GROBID 100.0 71.6 18.8 65.2 51.8 90.0 86.8 97.9 Qwen/Qwen2.5-3B-Instruct 83.5 79.0 54.9 81.6 47.0 84.1 73.5 79.2 Qwen/Qwen2.5-7B-Instruct 87.6 83.7 65.2 83.4 47.1 85.0 76.7 79.8 Qwen/Qwen3-0.6B 81.4 72.5 52.9 72.7 44.2 80.8 81.8 75.8 Qwen/Qwen3-0.6B


#### 95.0 88.5 74.6 89.3 70.1 94.3 91.0 92.8

+ cometadata/citation-parsing-lora

Qwen/Qwen3-8B 78.2 72.5 60.3 73.0 45.6 78.0 77.6 70.5 Qwen/Qwen3-32B 78.4 74.0 59.5 75.9 50.0 81.0 78.0 74.2 google/gemma-3-1b-it 27.7 21.8 13.5 7.6 6.1 11.9 11.0 13.8 meta-llama/Llama-3.1-8B-Instruct 80.3 65.7 45.6 69.6 43.8 73.7 72.5 76.0 mistralai/Mistral-7B-Instruct-v0.2 86.0 74.6 60.6 80.9 46.8 85.3 82.5 79.4 openai/gpt-oss-20b 88.3 78.7 59.1 80.8 49.2 83.0 82.1 85.9

All values represent recall (%) on field extraction from bibliographic citations. Bold indicates best performance in each column. Valid XML shows the percentage of examples producing well-formed, parseable XML. The strict parser rejects malformed XML (mismatched tags, unclosed elements), returning empty results. Edit distance thresholds: surname/year/volume/issue = 0 (exact), source = 5, title = 10.

Table 4: Precision (Strict) Across Models and Fields

Model Valid XML Surname Given Title Source Volume Issue Year GROBID 100.0 70.2 18.7 58.4 48.0 69.8 49.1 96.9 Qwen/Qwen2.5-3B-Instruct 83.5 73.4 53.5 48.7 46.2 76.4 77.1 82.5 Qwen/Qwen2.5-7B-Instruct 87.6 77.8 63.2 52.5 46.8 77.1 69.1 86.5 Qwen/Qwen3-0.6B 81.4 66.1 49.8 43.9 41.4 37.5 22.6 78.6 Qwen/Qwen3-0.6B

95.0 79.9 70.4 53.3 64.1 41.6 24.0 92.0

+ cometadata/citation-parsing-lora

Qwen/Qwen3-8B 78.2 76.8 64.7 53.6 52.6 70.8 64.4 79.8 Qwen/Qwen3-32B 78.4 76.3 61.7 54.6 53.7 75.8 67.4 79.6 google/gemma-3-1b-it 27.7 20.8 12.8 7.0 7.9 9.6 5.8 18.6 meta-llama/Llama-3.1-8B-Instruct 80.3 63.1 45.4 45.6 45.2 64.2 56.2 79.1 mistralai/Mistral-7B-Instruct-v0.2 86.0 74.5 60.9 53.7 57.7 79.0 62.7 84.8 openai/gpt-oss-20b 88.3 75.1 58.0 52.2 49.4 74.8 72.2 87.2

All values represent precision (%) on field extraction from bibliographic citations. Bold indicates best performance in each column. Valid XML shows the percentage of examples producing well-formed, parseable XML. The strict parser rejects malformed XML (mismatched tags, unclosed elements), returning empty results. Edit distance thresholds: surname/year/volume/issue = 0 (exact), source = 5, title = 10.

