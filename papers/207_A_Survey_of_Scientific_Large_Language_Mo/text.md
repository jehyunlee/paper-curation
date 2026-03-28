A Survey of Scientific Large Language Models:
From Data Foundations to Agent Frontiers
Ming Hu1,2
Chenglong Ma1,3
Wei Li1,4
Wanghan Xu1,4
Jiamin Wu1,5
Jucheng Hu1,6
Tianbin Li1
Guohang Zhuang1
Jiaqi Liu1,7
Yingzhou Lu8
Ying Chen1
Chaoyang Zhang1
Cheng Tan1
Jie Ying1
Guocheng Wu1
Shujian Gao1
Pengcheng Chen1
Jiashi Lin1
Haitao Wu1
Lulu Chen9
Fengxiang Wang1
Yuanyuan Zhang10
Xiangyu Zhao1
Feilong Tang1,2
Encheng Su1
Junzhi Ning1
Xinyao Liu1
Ye Du1
Changkai Ji1
Pengfei Jiang1
Cheng Tang1
Ziyan Huang1
Jiyao Liu1,3
Jiaqi Wei1
Yuejin Yang1
Xiang
Zhang1
Guangshuai Wang1
Yue Yang1
Huihui Xu1
Ziyang Chen1
Yizhou Wang1
Chen Tang1
Jianyu
Wu1
Yuchen Ren1
Siyuan Yan2
Zhonghua Wang2
Zhongxing Xu2
Shiyan Su2
Shangquan Sun1
Runkai
Zhao1
Zhisheng Zhang11
Dingkang Yang3
Jinjie Wei3
Jiaqi Wang1
Jiahao Xu1
Jiangtao Yan1
Wenhao
Tang1
Hongze Zhu1
Yu Liu12
Fudi Wang13
Yiqing Shen14
Yuanfeng Ji8
Yanzhou Su15
Tong Xie16
Hongming Shan3
Chun-Mei Feng17
Zhi Hou1
Diping Song1
Lihao Liu1
Yanyan Huang18
Lequan Yu18
Bin Fu1
Shujun Wang19
Xiaomeng Li20
Xiaowei Hu21
Yun Gu4
Ben Fei5
Benyou Wang22
Yuewen
Cao1
Minjie Shen9
Jie Xu1
Haodong Duan1
Fang Yan1
Hongxia Hao1
Jielan Li1
Jiajun Du23
Yanbo
Wang24
Imran Razzak25
Zhongying Deng26
Chi Zhang1
Lijun Wu1
Conghui He1
Zhaohui Lu4
Jinhai
Huang3
Wenqi Shao1
Yihao Liu1
Siqi Luo1
Yi Xin1
Xiaohong Liu4
Fenghua Ling1
Yuqiang Li1
Aoran Wang1
Siqi Sun1
Qihao Zheng1
Nanqing Dong1
Tianfan Fu27,1
Dongzhan Zhou1
Yan Lu1
Wenlong Zhang1
Jin Ye1,2
Jianfei Cai2
Yirong Chen1
Wanli Ouyang1,5
Yu Qiao1
Zongyuan Ge2†
Shixiang Tang1,5†‡
Junjun He1†‡
Chunfeng Song1†‡
Lei Bai1†§
Bowen Zhou1†§
1Shanghai Artificial Intelligence Laboratory 2Monash University 3Fudan University
4Shanghai Jiao Tong University 5The Chinese University of Hong Kong
6University College London 7UNC-Chapel Hill 8Stanford University 9Virginia Tech
10Purdue University 11China Pharmaceutical University
12Beijing Institute of Heart, Lung and Blood Vessel Diseases 13Chinese Academy of Sciences
14Johns Hopkins University 15Fuzhou University 16University of New South Wales 17University College Dublin
18The University of Hong Kong 19The Hong Kong Polytechnic University
20The Hong Kong University of Science and Technology
21South China University of Technology 22The Chinese University of Hong Kong, Shenzhen
23Caltech 24North University of China 25MBZUAI 26University of Cambridge 27Nanjing University
§ Github Repository: https://github.com/open-sciencelab/Awesome-Scientific-Datasets-and-LLMs
†Corresponding Author, ‡Project Leader, §Scientific Director
1
arXiv:2508.21148v2  [cs.CL]  18 Oct 2025

Abstract
Scientific Large Language Models (Sci-LLMs) are transforming how knowledge is represented, integrated, and applied in
scientific research, yet their progress is shaped by the complex nature of scientific data. This survey presents a comprehensive,
data-centric synthesis that reframes the development of Sci-LLMs as a co-evolution between models and their underlying data
substrate. We formulate a unified taxonomy of scientific data and a hierarchical model of scientific knowledge, emphasizing
the multimodal, cross-scale, and domain-specific challenges that differentiate scientific corpora from general natural language
processing datasets. We systematically review recent Sci-LLMs, from general-purpose foundations to specialized models across
diverse scientific disciplines, alongside an extensive analysis of over 270 pre-/post-training datasets, showing why Sci-LLMs pose
distinct demands—heterogeneous, multi-scale, uncertainty-laden corpora that require representations preserving domain invariance
and enabling cross-modal reasoning. On evaluation, we examine over 190 benchmark datasets and trace a shift from static exams
toward process- and discovery-oriented assessments with advanced evaluation protocols. These data-centric analyses highlight
persistent issues in scientific data development and discuss emerging solutions involving semi-automated annotation pipelines and
expert validation. Finally, we outline a paradigm shift toward closed-loop systems where autonomous agents based on Sci-LLMs
actively experiment, validate, and contribute to a living, evolving knowledge base. Collectively, this work provides a roadmap
for building trustworthy, continually evolving artificial intelligence (AI) systems that function as a true partner in accelerating
scientific discovery.
Keywords: Large Language Model; AI for Science; Scientific Data; Data4LLM
Fig. 1: The song of humanity is a song of courage. The diagram depicts the continuum of scientific inquiry spanning from
subatomic particles through atomic and molecular structures, cellular and organismal biology, ecological systems, planetary
sciences, to cosmological phenomena. Each tier represents distinct yet interconnected domains of investigation, illustrating
the nested hierarchy of natural phenomena and the corresponding disciplinary frameworks employed in their study. This
visualization encapsulates the expansion of scientific understanding from micro to macro dimensions, symbolizing humanity’s
persistent pursuit of knowledge across all scales of nature.
2

CONTENTS
I
Introduction
6
II
Background
9
II-A
Taxonomy of Scientific Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
9
II-A1
Textual Formats . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
9
II-A2
Visual Data
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
10
II-A3
Symbolic Representations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
12
II-A4
Structured Data
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
13
II-A5
Time-Series Data
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
14
II-A6
Multi-omics Integration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
14
II-B
Hierarchical Structure of Scientific Knowledge . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
16
II-B1
Factual Level
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
16
II-B2
Theoretical Level
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
17
II-B3
Methodological and Technological Level . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
17
II-B4
Modeling and Simulation Level
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
18
II-B5
Insight Level . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
18
II-B6
Dynamic Interactions and Evolution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
18
II-B7
Implications for Sci-LLMs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
19
II-C
Key Challenges in Scientific AI
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
19
II-C1
Interpretability in Scientific AI . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
19
II-C2
Cross-scale and Multimodal Integration
. . . . . . . . . . . . . . . . . . . . . . . . . . . . .
19
II-C3
Dynamic Knowledge Evolvement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
20
II-D
Quality Standards for Scientific Datasets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
20
II-D1
Accuracy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
20
II-D2
Completeness
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
20
II-D3
Timeliness . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
20
II-D4
Traceability
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
21
II-E
Dimensions for Evaluating Scientific AI . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
21
II-E1
Expert-Level Scientific Knowledge Comprehension and Retrieval . . . . . . . . . . . . . . .
21
II-E2
Scientific Reasoning and Problem Solving . . . . . . . . . . . . . . . . . . . . . . . . . . . .
21
II-E3
Multimodal Scientific Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
21
III
Scientific Large Language Models
21
III-A
Introduction of Large Language Models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
22
III-B
General-purpose Sci-LLMs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
22
III-C
Domain-specific Sci-LLMs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
24
III-C1
Physics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
24
III-C2
Chemistry
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
25
III-C3
Materials Science . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
25
III-C4
Life Sciences
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
26
III-C5
Astronomy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
29
III-C6
Earth Science
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
29
III-D
Sci-LLMs Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
30
IV
Scientific Data for Pre-training
31
IV-A
Physics, Chemistry and Material Sciences: the Foundation for Understanding the Material World . . . .
32
IV-A1
Physics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
32
IV-A2
Chemistry
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
33
IV-A3
Materials Science . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
33
IV-B
Life Sciences: Complexity from Molecules to Systems
. . . . . . . . . . . . . . . . . . . . . . . . . .
33
IV-B1
Molecular and Cell Biology . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
33
IV-B2
Multi-Omics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
34
IV-B3
Neuroscience . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
34
IV-B4
Healthcare and Medical Science . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
34
IV-B5
Agriculture . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
35
IV-C
Astronomy and Earth Science: Understanding Our Planet
. . . . . . . . . . . . . . . . . . . . . . . . .
35
IV-C1
Astronomy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
35
3

IV-C2
Earth Science
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
35
IV-D
Pre-training Data Analysis
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
36
V
Scientific Data for Post-training
36
V-A
Current Landscape Across Scientific Domains . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
37
V-A1
Physics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
37
V-A2
Chemistry
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
37
V-A3
Materials Science . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
37
V-A4
Life Sciences
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
37
V-A5
Astronomy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
38
V-A6
Earth Science
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
38
V-B
Post-training Data Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
39
VI
Evaluation of Sci-LLMs
40
VI-A
Current Landscape Across Scientific Domains . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
40
VI-A1
Physics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
40
VI-A2
Chemistry
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
40
VI-A3
Materials Science . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
41
VI-A4
Life Sciences
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
41
VI-A5
Astronomy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
41
VI-A6
Earth Science
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
41
VI-A7
General Science . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
42
VI-B
Evaluation Data Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
42
VI-B1
Tiered Regime in Data Generation and Annotation . . . . . . . . . . . . . . . . . . . . . . .
43
VI-B2
Skewed Knowledge Level with Increasing Difficulty . . . . . . . . . . . . . . . . . . . . . .
43
VI-B3
Shift towards Domain-Specific Metrics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
44
VI-C
LLM / Agent as a Judge
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
44
VI-D
Inspiration from Test-Time Learning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
45
VII
Scientific Data Development
45
VII-A
Data Collection and Labeling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
45
VII-A1
Data Source Heterogeneity and Acquisition Strategies
. . . . . . . . . . . . . . . . . . . . .
46
VII-A2
Annotation Methodologies and Quality Control . . . . . . . . . . . . . . . . . . . . . . . . .
46
VII-A3
Cross-Domain Patterns and Domain-Specific Considerations . . . . . . . . . . . . . . . . . .
47
VII-B
Limitations of Current Scientific Datasets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
47
VII-B1
Scarcity of Experimental Data
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
47
VII-B2
Over-reliance on Text Modality Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
48
VII-B3
Representation Gap between Static Knowledge and Dynamic Processes . . . . . . . . . . . .
48
VII-B4
Multi-level Biases in Scientific Datasets . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
48
VII-C
Systematic Issues in Data Quality
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
48
VII-C1
Data Traceability Crisis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
49
VII-C2
Scientific Data Latency . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
49
VII-C3
The Lack of AI-readiness . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
49
VIII
New Paradigms for Data-Driven Sci-LLMs
49
VIII-A
Scientific Agent . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
49
VIII-A1
LLMs as Scientific Agents . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
49
VIII-A2
Multi-Agent Collaboration
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
50
VIII-A3
Tool Use . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
50
VIII-A4
Self-evolving Agents
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
50
VIII-A5
Evaluation Frameworks and Benchmarking
. . . . . . . . . . . . . . . . . . . . . . . . . . .
51
VIII-A6
Autonomous Scientific Discovery . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
51
VIII-B
Data Ecosystems for Sci-LLMs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
51
VIII-B1
The Data Bottleneck Behind the Rise of Scientific Agents . . . . . . . . . . . . . . . . . . .
52
VIII-B2
Building an Operating System-level Interaction Protocol . . . . . . . . . . . . . . . . . . . .
52
VIII-B3
Design Principles for Next-Generation Scientific Data Architecture . . . . . . . . . . . . . .
53
VIII-B4
Sustainable Data Sharing Mechanism
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
53
VIII-B5
Data Safety and Privacy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
53
4

IX
Challenges and Outlook
54
IX-A
Challenges . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
54
IX-A1
Scientific Data Selection for Efficient Pretraining . . . . . . . . . . . . . . . . . . . . . . . .
54
IX-A2
Optimizing Data Processing Pipelines . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
54
IX-A3
Representing Non-Sequential and Non-Textual Data
. . . . . . . . . . . . . . . . . . . . . .
54
IX-A4
LLM Knowledge Update and Version Control . . . . . . . . . . . . . . . . . . . . . . . . . .
54
IX-B
Future Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
55
IX-B1
Integrated Scientific Data Ecosystems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
55
IX-B2
Automated Scientific Data Standardization Pipeline . . . . . . . . . . . . . . . . . . . . . . .
55
IX-B3
Comprehensive Evaluation System . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
55
IX-B4
Advanced Scientific Reasoning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
55
IX-B5
Autonomous Scientific Agents . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
55
IX-B6
From Sci-LLMs to Scientific Discovery . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
55
IX-B7
Ethical Governance for Responsible Scientific AI Innovation . . . . . . . . . . . . . . . . . .
55
X
Conclusion
55
References
69
5

I. INTRODUCTION
“Science is built up with facts, as a house is with stones. But a
collection of facts is no more a science than a heap of stones
is a house.”
— Henri Poincar´e
The rapid advancement of large language models (LLMs)
has sparked a paradigm shift across numerous domains,
demonstrating unprecedented transformative potential through
task automation, productivity enhancement, and breakthrough
innovations [1]–[5] (Fig. 2). These models have fundamentally
transformed scientific research by introducing a unified ap-
proach that replaces traditional task-specific methods, extend-
ing beyond natural language processing to encompass diverse
scientific data types, including molecules [6], proteins [7],
tables [8], and complex metadata. LLMs have already rev-
olutionized fields such as software engineering [2], [9], [10],
law [11], [12], materials science [13], [14], healthcare [15]–
[17], and biomedical research [18], and have been applied
across disciplines from mathematics [19] and physics to chem-
istry [20], biology [21], and geoscience [22].
The evolution of scientific LLMs (Sci-LLMs) has undergone
a paradigm shift through four distinct data-driven phases
from 2018 to 2025 (Fig. 3). The initial transfer learning
phase (2018–2020) witnessed domain-specific adaptations of
BERT [23] architecture, with models like SciBERT [24],
BioBERT [25], and PubMedBERT [26] trained on large-
scale scientific corpora, showing that continued pre-training
on domain literature yields sizable gains in downstream
tasks that require scientific text understanding. These models
provided reliable, static concept representations for specific
downstream uses, but struggled to synthesize or generate
novel scientific content at scale. The subsequent scaling phase
(2020–2022) embraced parameter and token-count expansion,
marking a critical transition. Models like GPT-3 [27] with
175 billion parameters, along with later data/compute-optimal
training rules [28], [29] demonstrated that massive parameter
scaling with diverse training data could achieve emergent
knowledge integration capabilities, fundamentally altering the
landscape of scientific AI. Galactica [30] extended this lesson
to science, with 120 billion parameters trained on more than
48 million scientific papers, textbooks, and encyclopedias,
designing specialized tokenization schemes for mathematical
formulas, chemical structures, and citations. MedPaLM-2 [31],
further instruction-tuned on multiple medical-domain datasets
and achieved over 85% accuracy on USMLE-style questions,
becoming the first AI system to exhibit expert-level medical
reasoning capabilities comparable to those of licensed physi-
cians. However, scaling ran into a data wall for Sci-LLMs:
unlike general-domain crawls with hundreds of billions to
trillions of tokens, high-quality scientific text corpora were
orders of magnitude smaller, with abundant scientific raw data
underutilized in early large-scale attempts.
The instruction-following phase (2022–2024) shifted focus
from capacity to alignment, introducing task adaptation via
reinforcement learning from human feedback (RLHF). Exam-
ples include InstructGPT [32] and ChatGPT [33], enabling
more precise scientific task execution. Subsequently, founda-
tional architectures represented by open-source LLMs (e.g.,
LLaMA [34], Qwen [35], ChatGLM [36], and Mistral [37])
have enabled unprecedented diversity in scientific applica-
tions. Concurrently, the unprecedented expansion of instruc-
tion datasets has given rise to a series of milestone Sci-LLMs.
Specifically, in the biomedical field, Meditron [38], pre-trained
on 48.1 billion tokens from medical literature, demonstrates
the potential of open-source models in professional medical
reasoning. ProteinChat [39], trained on 1.5 million protein-
prompt-answer triplets, facilitates protein research; LLaMA-
Gene [40] integrates gigabytes of DNA, protein, and text
data and 500 millions of instruction examples in DNA/protein
tasks for training, achieving cross-modal biological sequence
understanding. The multidisciplinary model SciGLM [41]
leverages the efficient architecture of ChatGLM, fine-tuned on
254,000 carefully constructed instruction examples, achieving
cross-disciplinary knowledge integration capabilities. Notably,
several works demonstrate a strong correlation between data
scale and model performance: HuatuoGPT-II [42] utilizes an
11 TB medical corpus with million-scale documents for pre-
training, while NatureLM [43] is pre-trained on 143 billion
tokens and fine-tuned using 45.1 million instruction-response
pairs. This dual-drive paradigm of “architectural diversity +
data scaling” has become the core framework for current
scientific large language model development.
Beyond excelling at analyzing existing scientific data, these
models demonstrate remarkable potential in accelerating sci-
entific discovery via hypothesis generation, theorem proving,
experiment design, drug discovery, and weather forecasting,
fundamentally reshaping how complex challenges are ap-
proached and solved in the era of AI-driven research [44]–
[46]. As a prominent example of this trend, Intern-S1 [47]
is a scientific multimodal Mixture-of-Experts (MoE) [48]
foundation model with general understanding and reasoning
capabilities alongside specialized expertise in scientific data
analysis. Continually pre-trained on massive scientific data
with 2.5 trillion tokens and enhanced with a Mixture-of-
Rewards reinforcement learning, it surpasses existing closed-
source state-of-the-art models in professional tasks such as
molecular synthesis, reaction condition prediction, and crys-
talline thermodynamic stability prediction, while maintaining
leading performance on general reasoning tasks.
The latest paradigm of agentic science (2023–now) is en-
abling AI systems with scientific agency, able to plan, act, and
iterate across stages of discovery. Many works demonstrate
end-to-end scientific workflows [44], [49], with increasing
focus on multi-agent [50], [51] and tool ecosystems [18], [52].
Multi-agent designs emulate laboratory hierarchies from prin-
cipal investigators to domain specialists, coordinating through
formalized meeting protocols and critique–iteration loops [53],
[54]. Such systems generate scientific ideas with improved
novelty and feasibility by explicitly modeling research team-
work [55] and scientific law constraints [56]. At scale, coop-
erative frameworks manage entire research lifecycles (prob-
lem scoping, manuscript drafting, etc.), preserving persistent
artifacts and audit trails [57], while embodied variants inte-
grate robotic execution with adaptive planning [58]. Parallel
6

Fig. 2: Cumulative trend of publications on major preprint platforms whose titles or abstracts mention the keyword “language
model” or the combination “language model + scientific domain” (e.g., chemistry, physics, multi-omics, medicine, etc.). Left:
Results from January 2018 to August 2025, from arXiv and PubMed. For arXiv, the matching includes “language model” in
combination with additional science-related keywords; PubMed results are limited to occurrences in titles and abstracts. Both
platforms show rapid growth. Right: Results from 2020 to August 2025, from bioRxiv, medRxiv, and ChemRxiv, all based
on direct matches of “language model” in titles and abstracts. While the overall volumes are smaller than arXiv and PubMed,
all three platforms, especially bioRxiv, show rapid acceleration, reflecting growing interdisciplinary interest in large language
models across biomedical, chemical, and computational sciences.
2019
2020
2022
2023
Transfer Learning
Scaling
Instruction Following
Agentic Science
2024
2025
BERT
BioGPT
Calactica
LangChain
GPT-4
Claude 3
GPT-5
Text Understanding
Knowledge Integration
Task Adaptation
Scientific Research 
Scientific Capability
GPT-3
GPT-2
AI co-scientist
(Gemini 2.0)
o1
ChatGPT
Biomedical
Other disciplines
General Science
API / < 1B
1B-100B
> 100B
2022.10
Coscientist
(GPT-4)
2024.3
2024.9
2025.8
2023.3
2020.6
2019.2
2018.10
InternAgent
PubMedBERT
AlphaFold 2
ChemCrow
(GPT-4)
SciBERT
ClinicalBERT
BioBERT
Chinchilla
BiomedGPT
Biomni
Intern-S1
MedPaLM 2
Fig. 3: Evolution of Sci-LLMs reveals four paradigm shifts from 2018 to 2025, including (1) the progression from transfer
learning approaches, (2) through the scaling era marked by knowledge integration in larger models, (3) instruction-following
capabilities enabling flexible task adaptation, to (4) the latest paradigm introduces scientific agents—AI systems capable of
autonomously conducting scientific research, from hypothesis generation and experimental design to data analysis and discovery.
Note: Model positions reflect their release dates (x-axis) rather than strict paradigm classification. The four paradigms represent
evolving trends in Sci-LLM development with overlaps and continuities, not mutually exclusive categories.
advances in tool integration center on knowledge-graph–driven
orchestration [59] and domain-scale agents interfacing with
hundreds of software tools, databases, and instruments with
provenance tracking [18].
Despite these promising results, Sci-LLMs encounter fun-
damental challenges stemming from the unique characteris-
tics of scientific data and knowledge representation. Unlike
the relatively homogeneous text corpora for general-purpose
LLM development, scientific datasets exhibit extreme het-
erogeneity across modalities and formats. For instance, in
7

chemistry alone, models must reconcile molecular strings,
3D molecular coordinates, spectroscopic data, and reaction
mechanisms, each requiring distinct processing strategies [60].
This heterogeneity extends beyond chemistry to encompass
the full spectrum of scientific disciplines. In life sciences,
models must simultaneously process genomic sequences, pro-
tein structures, multi-omics data, and clinical imaging [61]–
[63], while astronomical applications demand integration of
time-series photometry, spectroscopic observations, and multi-
wavelength imaging across vastly different spatial and tempo-
ral scales [64], [65].
The challenge is further compounded by the hierarchical
nature of scientific knowledge itself, which spans from raw ob-
servational data to abstract theoretical frameworks, each with
its own representational requirements [66], [67]. Moreover,
scientific data often embodies domain-specific semantics that
resist straightforward tokenization or embedding. Mathemati-
cal equations carry precise symbolic relationships that must be
preserved during processing [68], [69], while crystallographic
information files encode 3D structural constraints essential
for materials science applications [70], [71]. Time-series data
from instruments like Laser Interferometer Gravitational-Wave
Observatory (LIGO) contain subtle signals buried in noise,
requiring specialized preprocessing for physical interpretabil-
ity [65], [72]. These diverse data types cannot be adequately
represented through conventional text-based approaches, ne-
cessitating novel architectures that preserve domain-specific
invariance while enabling cross-modal reasoning [73]–[75].
The integration of such heterogeneous data sources poses ad-
ditional computational and methodological challenges. Cross-
scale modeling, from quantum mechanical calculations to
macroscopic phenomena, demands architectures capable of
capturing multi-resolution dependencies [76]. Furthermore,
the uncertainty in experimental measurements require mod-
els to propagate error bounds and maintain scientific rigor
throughout the reasoning process [77]–[79]. These constraints
fundamentally distinguish scientific AI from general-purpose
language modeling, requiring specialized solutions that respect
the unique epistemological foundations of scientific inquiry.
The inherent complexity of scientific data and reasoning
naturally extends to the evaluation of Sci-LLMs, where con-
ventional natural language processing benchmarks prove in-
sufficient for capturing domain-specific competencies. Recent
efforts have produced comprehensive evaluation suites such as
ScienceQA [80], which tests multimodal scientific understand-
ing across elementary to graduate levels, and MMLU-Pro [81],
which includes rigorous assessments in specialized fields
like quantum physics and molecular biology. However, these
benchmarks often fail to capture the nuanced requirements of
scientific discovery, e.g., the ability to generate novel hypothe-
ses, identify non-obvious connections between disparate find-
ings, or design experiments that test theoretical predictions.
To address this gap, Liu et al. propose ResearchBench [82], a
large-scale scientific discovery benchmark spanning 12 disci-
plines to systemically evaluate the hypothesis generation capa-
bilities of LLMs. Furthermore, researchers have also begun de-
veloping process-oriented evaluations that assess intermediate
reasoning steps rather than just final answers, exemplified by
Science 
Domain
Life
Sciences
Physics
Chemistry
Materials
Science
Astronomy
Earth
Science
l
Biology
l
Drug
l
Neuroscience
l
Healthcare
l
Multi-omics
l
Agronomy
l
…
l
Astrophysics
l
Celestial Mechanics
l
Astrometry
l
Cosmology
l
…
l
Hydrosphere
l
Biosphere
l
Lithosphere
l
Atmosphere
l
Cryosphere
l
…
l
Mechanics
l
Electromagnetism
l
Thermodynamics
l
Relativity
l
Quantum Mechanics
l
…
l
Organic Polymer 
Materials
l
Metallic Materials
l
Inorganic Non-Metallic 
Materials
l
Composite Materials
l
Synthesis and 
Processing
l
Microstructure, 
structure, Defects, and 
Properties of Materials
l
Material Failure and 
Protection
l
…
l
Analytical Chemistry
l
Organic Chemistry
l
Inorganic Chemistry
l
Polymer Chemistry
l
Quantum Chemistry
l
…
Fig. 4: Six main scientific domains covered in this survey.
The figure illustrates the primary disciplines investigated in
our study on science-oriented large language models, encom-
passing Chemistry, Materials Science, Physics, Life Sciences,
Astronomy, and Earth Science, along with representative sub-
fields within each domain.
frameworks like ScienceAgentBench [83] that evaluate models
on complex scientific workflows, including literature review,
experimental design, and result interpretation. Benchmarks
such as MultiAgentBench [84] and WorkflowBench [85] now
quantify collaboration, coordination, and workflow synthesis
skills, marking a shift toward measurable, safety-aware, and
reproducible science automation. The community has also
recognized that scientific validity requires more than lin-
guistic fluency; models must respect fundamental constraints
such as physical laws, chemical valence rules, and biological
feasibility [21], [86], [87]. This has led to the integration
of symbolic reasoning modules and constraint satisfaction
systems that act as guardrails during generation, ensuring that
model outputs remain within scientifically plausible bounds
while still allowing for creative exploration at the frontiers of
knowledge.
To address these gaps, several survey papers look into
adjacent facets of the problem. A few works [88], [89]
focused on models and tasks for biomedical data; Zhang et
al. [21] examined Sci-LLMs under a broader perspective
that involves both biological and chemical domains. Other
works [60] explored the application of Sci-LLMs in scientific
discovery. Wei et al. [90] and Wang et al. [91] reviewed
scientific agent paradigms and system designs for autonomous
research and scientific discovery. Ni et al. [92] conducted a
survey on existing benchmarks for LLMs involving several
science fields. Chen et al. [93] provided a comprehensive
survey on AI for autonomous scientific research, offering a
systematic taxonomy and compiling resources across multiple
disciplines. However, these reviews are theme-specific and
8

limited to models with only a cursory touch on the underlying
substrate—scientific datasets, throughout pre-training, post-
training and evaluation. Complementing these perspectives,
our survey contributes a unified, cross-disciplinary synthesis
that explicitly links data foundations to agent frontiers. We
summarize the contributions as follows:
• By introducing a unified taxonomy of scientific data
and a hierarchical model of scientific knowledge, we
provide a novel epistemological framework for analyzing
the challenges in representing scientific information, from
raw observational data and symbolic notations to abstract
theoretical insights.
• We deliver a comprehensive and structured account of
the rapidly evolving landscape of scientific large language
models across six main scientific domains (i.e., physics,
chemistry, life sciences, Earth Science, astronomy, and
materials science; as in Fig. 4).
• By systematically analyzing over 270 pre- and post-
training datasets, we provide a comprehensive panorama
of current scientific datasets for Sci-LLM develop-
ment, distilling the multimodal, cross-scale, and domain-
specific challenges that distinguish Sci-LLMs from their
general-purpose counterpart.
• We conduct a comprehensive review of over 190 eval-
uation datasets for Sci-LLMs, discussing the shift of
evaluation from static exams to research-level scientific
discovery, the increasing employment and combination of
domain-specific metrics, and the emergence of advanced
evaluation methodologies.
• We identify structural failures in scientific data curation
and translate them into a forward-looking data devel-
opment agenda that supports advanced scientific intel-
ligence, advocating for a closed-loop feedback between
autonomous scientific discovery and scientific data infras-
tructure.
Collectively, these contributions establish a consolidated refer-
ence and a clear roadmap for building trustworthy, continually
evolving Sci-LLMs capable of accelerating data-driven scien-
tific discovery.
The paper is organized as follows: Sec. II formulates a
unified taxonomy of scientific data grounded in a hierarchical
model of scientific knowledge. Sec. III shows the landscape
of Sci-LLMs across six main scientific domains. Secs IV, V,
and VI provide an extensive catalog and analysis of existing
pre-training, post-training, and evaluation datasets for Sci-
LLMs. Sec. VII analyzes how scientific data shapes LLM
development and identify systemic issues that impede AI-
readable corpora. Sec. VIII outlines forward directions for
scientific discovery empowered by advanced scientific agents
and data ecosystems. Secs. IX and X summarize challenges,
outlook, and conclusion distilled from the paper.
II. BACKGROUND
This section provides the foundations for understanding
scientific AI systems. We first examine the diverse taxonomy
of scientific data across disciplines (Sec. II-A), followed by an
analysis of the hierarchical structure of scientific knowledge
(Sec. II-B), which reveals that scientific understanding forms
a sophisticated multilevel system rather than a simple infor-
mation repository. Then, we identify critical challenges unique
to scientific AI (Sec. II-C), including knowledge consistency,
interpretability, and the integration of cross-scale multimodal
data. We conclude by establishing frameworks for evaluating
both data quality standards (Sec. II-D) and AI system capabil-
ities specific to scientific domains (Sec. II-E). These elements
collectively define the requirements for AI systems designed
to support rigorous scientific discovery and reasoning.
A. Taxonomy of Scientific Data
Scientific data manifests in striking diversity across disci-
plines, shaped by the fundamental questions and methodolog-
ical paradigms unique to each field. In this subsection, we
review and summarize the primary data types and modalities
across scientific domains, examining how they appear and
function within different scientific contexts, including: textual
formats (papers, experimental reports) in Sec. II-A1, visual
data (medical scans, astronomical observations) in Sec. II-A2,
symbolic representations (formulas, chemical structures) in
Sec. II-A3, structured data (databases, knowledge graphs) in
Sec. II-A4, and time-series data (neurophysiological record-
ings, astronomical light curves) in Sec. II-A5. In addition to
these general types, we also discuss multi-omics integration
in Sec. II-A6 as a special case, as it represents an emerging
paradigm that requires combining heterogeneous data across
multiple biological layers (e.g., genomics, transcriptomics,
proteomics). This taxonomy sets the stage for understanding
how scientific data collectively support AI-driven scientific
discovery across domains, and also establishes the foundation
for developing multimodal large language models (MLLMs)
which aim to process and integrate heterogeneous scientific
data within a unified framework.
1) Textual Formats: Scientific textual data forms the foun-
dational substrate for knowledge representation across disci-
plines, encompassing a rich hierarchy from primary experi-
mental documentation to synthesized knowledge repositories.
At the most granular level, laboratory notebooks, experimental
protocols, and field observations capture the raw process of
scientific discovery, documenting not only successful experi-
ments but also failed attempts and methodological refinements
that prove invaluable for reproducibility and knowledge trans-
fer [94]. This primary documentation feeds into specialized
databases and repositories that have become central to mod-
ern scientific practice: genomic sequences in GenBank [95],
protein structures in RCSB [96], chemical compounds in
PubChem [97], [98], and astronomical observations in NASA’s
Astrophysics Data System (ADS) [99], collectively housing
petabytes of structured information linked to their textual
descriptions and metadata.
The scholarly communication layer builds upon this founda-
tion through peer-reviewed journals, comprehensive textbooks,
and increasingly, preprint repositories that accelerate knowl-
edge dissemination. Traditional venues like Physical Review
Letters, The Astrophysical Journal, and Monthly Notices of the
Royal Astronomical Society maintain rigorous standards while
9

Fig. 5: Examples of visual data across typical medical imaging modalities, involving radiology (PET, CT, mammography,
X-ray, MRI, and ultrasound), dermatology, ophthalmology (CFP, FFA, UWF-SLO, and OCT), endoscopy, histopathology, and
cellular microscopy. The figure is sourced from open-source medical datasets.
platforms such as arXiv [100] and ChemRxiv [101] enable
rapid sharing of emerging findings across physics, astronomy,
chemistry, and interdisciplinary domains. This academic cor-
pus is complemented by educational resources ranging from
open-access textbooks like OpenStax series [102], [103] and
The Feynman Lectures [104] to specialized training materi-
als including agricultural extension question-answering (QA)
records [105], examination questions, and curated datasets
for AI model evaluation such as ScholarChemQA [106],
ScienceQA [107], and materials science benchmarks [108]–
[110].
Beyond traditional academic outputs, scientific textual data
increasingly encompasses regulatory documentation, real-time
observational streams, and computational artifacts that reflect
the evolving nature of modern research. Clinical trial reg-
istries [111], institutional review protocols [112], and biosafety
guidelines [113] ensure responsible research conduct, while
electronic health records [114], [115], citizen science an-
notations from projects like Galaxy Zoo [116], and real-
time environmental monitoring data [117] bridge laboratory
findings with societal applications. The integration of com-
putational approaches has spawned new textual categories,
including bioinformatics pipelines [118], systems biology
models [119], synthesis planning frameworks [120], and code
generation benchmarks [121], [122], all requiring extensive
documentation for reproducibility. This diverse textual ecosys-
tem not only archives scientific progress but enables meta-
analyses [123], knowledge synthesis efforts, and increasingly
sophisticated AI-driven discovery across the full spectrum of
scientific inquiry.
2) Visual Data: Visual data in scientific domains broadly
fall into two categories: instrumental imaging that directly cap-
tures physical subjects through various sensing technologies,
and diagrammatic representations that abstract and visualize
concepts, relationships, and analytical results. These visual
data span an extraordinary range of scales and modalities, from
sub-atomic particle interactions to cosmic structures, providing
essential foundations for multimodal AI systems to understand
scientific phenomena.
At the smallest scales, as shown in Fig. 6, advanced
microscopy techniques, including scanning and transmission
Fig. 6: Examples of visual data in physics. SEM of
epoxy with/without AlN [124]; TEM of W-doped Cu–Pt
nanoalloys [125]; AFM topography of hyper-stoichiometric
UO2
[126]; STM of Si (111)-(7×7) at multiple scan
sizes [127]; UV/Vis contour map (500–680 nm) [128]; In-
frared thermographs of a directional emitter [129]; Raman
helicity-resolved maps of 1T-TaS2 [130]; NMR of yttrium
hydrides [131]. All panels are reused or adapted under the
stated licenses (CC-BY-4.0 or CC-BY), with minor cropping
only.
electron microscopy (SEM/TEM) [132], [133], atomic force
microscopy (AFM) [134], and scanning tunneling microscopy
(STM) [135], reveal atomic structures and molecular arrange-
ments critical for physics, materials science and chemistry.
Visual spectrum data, including ultraviolet-visible spectropho-
tometry (UV/Vis) [136], infrared [137], Raman [138], and
nuclear magnetic resonance (NMR) [139] spectroscopy, serve
as molecular “fingerprints” across chemistry, materials science,
and physics, with visual representations proven effective for
spectrum learning [140], [141].
In life sciences, light microscopy (brightfield, confocal) and
fluorescence microscopy capture cellular structures and protein
localizations, with datasets like the Human Protein Atlas [142]
and Broad Bioimage Benchmark Collection [143] supporting
cell segmentation and phenotype classification tasks. These
microscopy images, typically stored in formats like TIFF [144]
or ND2 [145], have been increasingly leveraged for training
visual-language models [146], [147]. Moving up in scale,
whole-slide digital pathology produces gigapixel images stored
10

Lithosphere
Biosphere
Cryosphere
Hydrosphere
Atmosphere
Anthroposphere
Fig. 7: Data from Earth science’s six major domains, including the lithosphere, anthroposphere, biosphere, cryosphere,
hydrosphere, and atmosphere. Each panel consists of geospatial data, maps, satellite imagery, charts, etc. These data sources
are highly diverse, encompassing a wide range of spatial and temporal resolutions, as detailed in Sec. II-B1. The figure is
sourced from MSEarth [153], and authorization for its use has been obtained from the original author.
The W50 “Manatee” Nebula shown 
in visible radio light. (VLA)
Radio visual
Optical visual
This Hubble image shows galaxy 
cluster ACO S 295.  (HST)
NGC 4535 spiral galaxy as imaged 
by HST. (HST)
Infrared visual 
 Image Credit: NASA/VLA/HST/JWST.
VLA image of radio emissions from 
neutron star collision and gravitational 
waves. (VLA)
Alpha Centauri 3 Panel. (JWST)
Astronomical visual 
data
Fig. 8: Examples of astronomical data, demonstrating the
application of radio signals, optical signals, and infrared
signals in imaging different astronomical objects. The image
is sourced from NASA.
in SVS format, essential for cancer diagnosis, with large co-
horts like TCGA [148] and CPTAC [149] providing thousands
of images paired with diagnostic reports [150]–[152].
At tissue and organ scales, radiological imaging en-
compasses
multiple
modalities
including
X-rays
[154],
[155], computed tomography (CT) [156]–[158], histopathol-
ogy
[159],
magnetic
resonance
imaging
(MRI)
[160],
[161], ultrasound [162], [163], positron emission tomography
(PET) [164], [165], and mammography [166], each revealing
different aspects of internal anatomy and function. These
images, commonly stored in DICOM [167] or NIfTI [168]
formats with rich metadata, can be processed using specialized
viewers like RadiAnt [169] and MRIcroGL [170] or program-
matic libraries such as pydicom [171] and SimpleITK [172].
Clinical imaging extends to specialized domains like oph-
thalmology with color fundus photography (CFP) [173]–
[175], fundus fluorescein angiography (FFA) [176], ophthal-
mology [177] and optical coherence tomography (OCT) [178],
[179], dermatology for skin lesion analysis [180], [181] oph-
thalmic surgical microscopy for high-resolution intraopera-
tive visualization in ophthalmic procedures [182]–[185], and
endoscopy for surgical guidance [186]–[188]. These visual
data, once paired with their descriptions and reports, hold
great potential in developing healthcare MLLMs; visualization
examples are shown in Fig. 5.
At macroscopic scales, natural photographs capture biodi-
versity through datasets like iNaturalist [189], while agricul-
tural visual data span from micro-level plant imaging to macro-
level UAV and satellite imagery for crop monitoring [190]–
[192]. Earth science leverages satellite remote sensing [193],
[194] and atmospheric datasets [195], [196] for climate mod-
eling and environmental monitoring. As shown in Fig. 7, due
to the diversity of their collection sources, earth observation
data exhibit significant variability. For instance, some data
are obtained from ground-based observation stations, offering
long-term and continuous records at specific locations. Other
datasets are derived from multispectral remote sensing tech-
nologies, which provide comprehensive information on surface
and atmospheric characteristics across larger spatial scales.
Additionally, reanalysis data [195] integrate observational
records with numerical models, resulting in meteorological
and environmental parameters with enhanced temporal and
spatial consistency. These various types of data each possess
11

unique features in terms of spatial coverage, temporal resolu-
tion, and observational content, offering a multi-dimensional
information foundation for research in earth system science.
Beyond Earth, astronomical observations across the radio
interferometry [197] to optical [64], [198] and infrared [199],
capture celestial phenomena, complemented by spectroscopic
data from instruments like Large sky Area Multi-Object fiber
Spectroscopic Telescope (LAMOST) [200] that reveal chemi-
cal compositions and stellar dynamics, as illustrated in Fig. 8.
Complementing direct imaging, diagrammatic figures and
spectroscopic visualizations provide crucial abstractions of
scientific knowledge that cannot be captured through pho-
tography alone. Molecular structure diagrams, increasingly
recognized as natural interfaces for chemical AI systems [201],
have been curated into large-scale datasets for tasks ranging
from image captioning to property prediction [97], [202],
[203]. Schematic diagrams and conceptual illustrations from
scientific literature [204]–[207] distill complex processes and
experimental setups into accessible forms, essential for both
human understanding and AI interpretation. These diverse
visual modalities from atomic-resolution microscopy to cos-
mic surveys, and from molecular diagrams to climate visu-
alizations, collectively form a rich multimodal foundation for
scientific AI systems. The integration of these varied visual el-
ements into comprehensive datasets like MaCBench [208] and
MMSci [75] enables models to synthesize knowledge across
disciplines, though challenges remain in aligning dense visual
information with semantic textual descriptions, particularly for
complex phenomena in molecular biology, materials science,
and mathematical physics that require advanced multimodal
learning techniques.
3) Symbolic Representations:
Symbolic representations
constitute a fundamental data modality in scientific com-
puting, providing abstract, non-numeric encodings of scien-
tific entities, relationships, and laws that are both human-
interpretable
and
machine-processable.
These
representa-
tions include molecular structures encoded as string nota-
tions, such as Simplified Molecular-Input Line-Entry Sys-
tem (SMILES) strings [209], International Chemical Identi-
fier (InChI) codes [210], Self-Referencing Embedded Strings
(SELFIES) [211]), Crystallographic Information Files (CIF)
for material structures, and parameterized equations for
physics and Earth system modeling. The significance of sym-
bolic data lies in its ability to encode complex scientific knowl-
edge in compact, manipulable forms that preserve semantic
meaning while enabling automated reasoning, transformation,
and discovery operations critical for modern scientific com-
puting.
The most prevalent symbolic representations in chemistry
and materials science are string-based molecular encodings,
with SMILES [209] being the de facto standard since the
1980s. SMILES is a specification in the form of a line
notation for describing the structure of chemical species us-
ing short ASCII strings, encoding molecular structures using
ASCII strings with specific rules: atoms are represented by
their chemical element symbols (often with brackets omitted),
bonds by symbols including “-” (single), “=” (double), “#”
(triple), “:” (aromatic), rings by breaking cycles and adding
matching numbers (e.g., “O1CCOCC1” for 1,4-Dioxane), aro-
matic rings using lowercase letters or alternating bonds (e.g.,
“c1ccccc1” for benzene), and branches using parentheses (e.g.,
“CCC(=O)O” for propionic acid). An extension of SMILES
for polymers is BigSMILES [212], which represents poly-
mers as stochastic objects with monomers enclosed in curly
brackets, as illustrated in Fig. 9. However, SMILES suffers
from syntactic fragility—small perturbations can render strings
invalid. To address this, SELFIES (SELF-referencing Em-
bedded Strings) [213] was introduced in 2020, guaranteeing
100% validity through formal grammar rules. SELFIES uses a
vocabulary of tokens like “[C]”, “[=O]”, “[Branch]”, “[Ring]”
with localized markers for branches and rings, enabling robust
left-to-right parsing that gracefully handles errors. Fig. 10
shows examples of Formaldehyde and Phenol’s molecular
graphs and corresponding SMILES and SELFIES strings. The
difference between SMILES, BigSMILES, and SELFIES is
demonstrated in Table I. Beyond strings, molecular graphs
provide more intuitive representations where nodes correspond
to atoms and edges to bonds, with adjacency matrices encoding
connectivity and bond types [214]. Recent benchmark [215]
reveals that SMILES remains most expressive for molecular
optimization tasks, while SELFIES often underperforms due
to redundancy.
For crystalline materials, the CIF format serves as the stan-
dard, encoding unit cell parameters (lattice constants a, b, c,
angles α, β, γ), atomic positions in fractional coordinates,
space group symmetries, and experimental metadata in a
structured key-value format readable by tools like pymatgen
and VESTA. These representations underpin major databases
including ZINC [216], ChEMBL [217], USPTO [218], ICSD,
and the Materials Project [70], as well as benchmarks like
MoleculeNet [219] and MatBench [71].
In physics and astronomy, symbolic representations extend
beyond structural encodings to encompass mathematical ex-
pressions, differential equations, and theoretical frameworks
that enable automated scientific discovery. At the core are
algebraic equations, differential/integral forms, and probability
distributions, with recent work demonstrating that LLMs per-
forming symbolic derivation, i.e., keeping variables symbolic
before late-stage numerical substitution, tend to achieve higher
accuracy on physics problem solving compared with numeric-
first approaches [68]. Equation graphs represent variables
and operators as nodes, enabling graph-based symbolic re-
gression; for instance, graph networks trained on force-law
data successfully recover Newton’s law through message-
passing outputs [220]. Building on this foundation, LLM-
powered methods like Dual Reasoning Symbolic Regression
integrate language model reasoning with reflective optimiza-
tion for equation extraction [69]. In astronomy, systems like
PhyE2E [221] demonstrate end-to-end neural symbolic regres-
sion, generating dimensionally consistent formulas from di-
verse sources including NASA’s THEMIS mission data [222],
AI Feynman datasets [223], [224], and solar observation data
(SILSO) [225]. Similarly, Earth science employ symbolic rep-
resentations through mathematical formula fitting and regres-
sion for modeling complex phenomena governed by partially
understood physics, such as the Navier-Stokes equations [226]
12

TABLE I: Comparison of SMILES, BigSMILES, and SELFIES representations.
Feature
SMILES [209]
BigSMILES [212]
SELFIES [213]
Primary domain
Small molecules
Polymers and macromolecules
Small molecules
Syntax basis
ASCII strings with chemical rules
SMILES syntax + curly bracket extensions
Tokenized grammar rules
Connectivity encoding
Explicit bonds, rings, branches
Bonds, rings, branches + bonding descriptors ([*]) Encoded via grammar tokens
Stochastic representation
Not supported
Supported via curly brackets
Not supported
Polymer architecture
Not supported
Supports block, random, graft, branched
Not supported
Error tolerance
Fragile—small changes can break validity
Same as SMILES for monomers
Guaranteed 100% valid
Typical example
CCO (ethanol)
{[*]CC[*]} (polyethylene)
[C][C][O] (ethanol)
Advantages
Compact, widely supported
Encodes polymer connectivity
Robust to syntax errors
Limitations
Syntactic fragility
Still fragile at monomer level
Redundancy, longer strings
Fig. 9: Schematic of BigSMILES representations from Lin et
al. [212]. Polymers are represented as monomers (repeating
units) enclosed within curly brackets; the curly brackets indi-
cate that the molecule is a stochastic object. The monomers are
represented as SMILES strings, with additional information
expressing the connectivity between monomeric units.
in atmospheric motion, wave equations in seismology [227],
and shallow-water equations in oceanography [228]. These
models utilize parameterization schemes and regression anal-
ysis (least squares, Bayesian inference) to align theoretical
predictions with observational data, demonstrating how sym-
bolic representations serve as a bridge between empirical
observations and theoretical understanding across scientific
disciplines.
4) Structured Data: Structured data in scientific domains
refers to information systematically organized through ex-
plicit, formal models that enable efficient querying, stor-
age, and computational reasoning. Across disciplines, struc-
tured data follows a progression from simple tabular formats
to complex knowledge representations. At the foundational
level, data tables T consisting of columns {ci}C
i=1 and rows
{lj}R
j=1 serve as the basic organizational unit, with each cell
vij representing measurements or annotations. These tables,
prevalent in resources like GEO [229], dbSNP [230], and
weather station datasets such as WEATHER-5K [231], provide
straightforward data organization but lack explicit semantics
or inter-attribute relationships. Building upon this foundation,
relational databases D = {T1, T2, . . . , TN} extend tables
with schema-level constraints and referential integrity, where
foreign key pairs (c(k)
i
, c(h)
j
) connect columns across tables,
enabling complex queries over diverse entities as seen in
Ensembl [232] and UniProtKB [233].
The evolution toward more expressive representations in-
cludes ontologies and knowledge graphs that capture domain-
specific semantics and relationships. Ontologies formally
Fig. 10: Exemplified symbolic representations (cheminformat-
ics) of formaldehyde and phenol: molecular graph, SMILES
and SELFIES string, node identity, and adjacency matrix.
Hydrogens are typically omitted in SMILES and SELFIES
strings. In the adjacency matrix, edge weights reflect bond
types: 1 for single bonds, 2 for double bonds, and 3 for bonds
in the aromatic ring.
represent concepts and their relationships using languages
like Web Ontology Language [234] or Open Biological and
Biomedical Ontologies [235], defining classes, properties, and
hierarchies for semantic interoperability and logical inference,
exemplified by the Gene Ontology [236] and Human Pheno-
type Ontology [237]. A knowledge graph is a collection of re-
lational facts G ⊆E×R×E, where E denotes the set of entities
and R the set of semantic relations. By integrating heteroge-
neous data into a unified semantic representation, knowledge
graphs facilitate knowledge reasoning and discovery [238],
[239], as exemplified by UMLS [240] and PrimeKG [241];
similarly, CLLMate [242] aligns meteorological records with
climate events. Taken together, these developments form
a structured data ecosystem supported by standardized ex-
change formats—including CSV, XML, JSON, YAML, HDF5,
ROOT, FITS, and NetCDF—that ensure traceability and in-
teroperability across disciplines. Large-scale repositories have
emerged as critical infrastructure, from molecular libraries
like ZINC [216] and ChEMBL [217] storing compounds
in SMILES format [243], [244], to physics archives like
CODATA [245] and particle physics databases [246], astro-
nomical catalogs including SIMBAD [247] and VizieR [248],
materials databases such as the Materials Project [70] and
13

T
S
Fig. 11: Five-channel EEG recording setup and corresponding
time series data. Horizontal axis: time (T); Vertical axis:
individual EEG channels showing brain electrical activity
patterns recorded from scalp electrodes. Figure is adapted from
CSBrain [272].
MatBench [71].
The sophistication of structured data extends to specialized
property datasets that enable targeted scientific investigations.
In chemistry, ADMET (Absorption, Distribution, Metabolism,
Excretion, and Toxicity) databases [244], [249] provide com-
prehensive pharmacokinetic properties including absorption
(Bioavailability [250], HIA [251]), distribution (BBB [252],
FreeSolv [253]), metabolism (Clearance-AstraZeneca [254]),
excretion (VDss [62], [255]), and toxicity (ClinTox [219], Tox-
Cast [256], Tox21 [257]) measurements crucial for drug dis-
covery. Similarly, gravitational-wave catalogs like GWTC [65]
document events with detailed source parameters in machine-
readable formats, while materials databases provide multi-
property coverage including electronic, thermodynamic, and
mechanical behaviors computed under standardized protocols.
These structured resources leverage persistent identifiers and
metadata standards, facilitating rich scholarly analyses through
bibliographic knowledge graphs like INSPIRE-HEP [258]
and NASA ADS [99], ultimately enabling robust predictive
modeling and efficient exploration of vast scientific spaces
across all disciplines.
5) Time-Series Data: Time series data, characterized by
sequences of temporal data points collected at certain in-
tervals [259]–[261], constitutes a fundamental data modality
across scientific disciplines, capturing dynamic phenomena
from nanoseconds to decades. These data enable the analysis
of temporal patterns, periodicity, and system evolution across
vastly different scales—from molecular dynamics tracking
atomic positions {X(t) ∈RN×3}T
t=0, velocities {V(t) ∈
RN×3}T
t=0, and forces {F(t) ∈RN×3}T
t=0 in datasets like
MD17 [262] and ISO17 [263], [264], to astronomical ob-
servations monitoring stellar brightness variations for exo-
planet detection in missions like Kepler [265] and Five-
hundred-meter Aperture Spherical Telescope (FAST) [266].
The temporal resolution spans milliseconds in neurophysio-
logical recordings such as electroencephalogram (EEG) [267]
capturing brain oscillations [268] and event-related poten-
tials [269] (Fig. 11), to hourly meteorological variables in
the ERA5 dataset [195] with 0.25-degree spatial resolution,
and continuous seismic waveforms from Incorporate Research
Institutions for Seismology [270] and United States Geological
Survey networks [271] for earthquake monitoring.
The diversity of time-series modalities reflects the mul-
Epigenomics
Proteomics
Genomics
Transcriptomics
Metabolomics
Transcription
Expression
Translation
Function
Microbiome
e
l
y
t
S
 
e
f
i
L
l
a
i
c
o
S
l
a
c
i
m
e
h
C
-
l
a
c
i
s
y
h
P
s
m
e
t
s
y
s
o
c
E
Exposome
Micribial 
Reactions
Environmental 
Effects
Fig. 12: Multi-omics data landscape.
tiscale nature of scientific phenomena. In biological sys-
tems, time-series data capture dynamics from molecular-level
gene expression patterns revealing temporal responses [273]–
[275]
to
clinical
monitoring
through
electrocardiogram
(ECG) [276] for cardiac rhythm analysis [277], electromyo-
gram (EMG) [278] for muscle activity [279], and continuous
glucose monitoring [280], [281]. Neuroimaging modalities
provide complementary temporal and spatial resolutions: func-
tional magnetic resonance imaging (fMRI) detects blood-
oxygen-level-dependent (BOLD) signals [282] for mapping
brain networks [283], while magnetoencephalography (MEG)
measures magnetic fields from neuronal activity [284], [285].
In chemistry, molecular spectrum data mainly include Ra-
man, infrared (IR), ultraviolet (UV), 1H nuclear magnetic
resonance (NMR), and
13C NMR spectroscopy [286], re-
vealing structural and compositional information enabling AI-
driven representation learning [140]. Physics leverages high-
frequency strain data from LIGO/Virgo at 16,384 Hz for
gravitational wave detection [65], while SDO [287] provides
Atmospheric Imaging Assembly Extreme Ultraviolet images
every 12 seconds and Helioseismic and Magnetic Imager
(HMI) vector-magnetogram-derived Space-weather HMI Ac-
tive Region Patches features at 12-minute cadence to forecast
space weather [288].
These temporal datasets serve critical roles in understanding
system dynamics, enabling predictive modeling, and monitor-
ing critical events. Longitudinal clinical studies utilize serial
MRI, CT, and clinical report data [289] to model disease
trajectories [290], [291], while synoptic astronomical surveys
like The Zwicky Transient Facility [292] and Legacy Survey of
Space and Time [293] generate calibrated image sequences for
transient detection. Earth science integrates atmospheric data
from WeatherBench [196] and WEATHER-5K [231], oceanic
measurements from the Hybrid Coordinate Ocean Model
(HYCOM) [294] and NOAA Tides [295], and geophysical
recordings for comprehensive Earth system monitoring. The
standardization of these diverse time-series formats facilitates
cross-disciplinary AI applications [296]–[298], establishing
time-series analysis as a cornerstone methodology for extract-
ing insights from dynamic scientific phenomena across all
scales.
6) Multi-omics Integration: Driven by rapid advances in
high-throughput technologies, multi-omics has emerged as a
powerful approach for capturing the complexity of living
14

<DNA> A T C A A T A T C C A C C T … T G A T</DNA>
<RNA> G A G UA G AA G C G U U C … C U C C </RNA>
<Protein> G S G F R K M A F P S G K … V T F Q </Protein>
Fig. 13: Symbolic representations and 3D structure visual-
izations across different scientific domains: DNA, RNA and
Protein. The DNA structure is split into chain I and chain
J from PDB 1KX5 [299] and visualized by UCSF Chimera
[300]. The RNA structure is from the RNAsolo with ID
7ELQ [301], [302]. The protein snapshot is from the PDB
bank with ID 7CAM [303]. The DNA and protein are adapted
from NatureLM [43].
systems through the integrated analysis of multiple layers
of biological data [61]. As illustrated in Fig. 12, the multi-
omics landscape encompasses seven major data modalities:
genomics (capturing genetic sequences and variations), epige-
nomics (mapping regulatory modifications), transcriptomics
(profiling gene expression), proteomics (analyzing protein
abundance and function), metabolomics (measuring small
molecule metabolites), microbiome (characterizing microbial
communities and their functions/interactions), and exposome
(tracking environmental effects). These omics layers are inter-
connected through biological processes, from transcription and
translation at the molecular level to environmental interactions
at the systems level, offering complementary insights that
together enable a more comprehensive understanding of bi-
ological processes than any single layer alone [304], [305]. At
the molecular core of this framework, biological information
flows from DNA to RNA to proteins, with each biomolecule
existing in both symbolic sequence representations and three-
dimensional structural forms (Fig. 13).
Multi-omics technologies have continued to advance, of-
fering improved resolution, accuracy, and scalability, along
with enhanced methods for integrating data across different
biological domains [62], [306]–[308]. As a result, multi-omics
has emerged as a cornerstone of modern scientific research,
providing deeper insights into the molecular mechanisms
underlying health and disease, unraveling complex regulatory
networks, and driving data-informed discoveries across diverse
biological domains [309].
Genomics encompasses a vast and evolving ecosystem of
structured, symbolic and sequence-based representations. (i)
Reference genomes, such as those hosted by Ensembl [310]
and UCSC Genome Browser [311], provide curated nucleotide
sequences and annotated genomic elements across thousands
of species. (ii) Genetic variation, arising from differences
in DNA sequences across individuals or populations, is a
central focus of genomics. Population-scale resources such
as GWAS Catalog [312], dbSNP [230] and gnomAD [313]
catalog common and rare variants, providing estimates of
allele frequencies across diverse cohorts, while ClinVar con-
nects specific variants to clinical phenotypes and pathogenicity
interpretations [314]. (iii) Functional genomics maps, such as
those from ENCODE and Roadmap Epigenomics [315], layer
chromatin accessibility, histone marks, DNA methylation, and
transcription factor binding profiles onto the genome to reveal
regulatory landscapes. (iv) Spatial genome resources [316],
[317], including Hi-C datasets and 3D genome browsers,
reconstruct chromatin topology to explore long-range reg-
ulatory interactions. Genomic data are inherently symbolic
and sequential, with rich metadata and controlled vocabular-
ies [237]—features that make them well-suited for conversion
into prompt-based representations for language models [318],
[319]. Emerging methods already leverage large-scale variant
catalogs [313] and knowledge graphs [241] to train founda-
tion models for genotype-phenotype reasoning, while multi-
resolution integration with imaging or epigenetics supports
causal inference at cellular and organismal scales.
Transcriptomics captures the dynamic and context-specific
landscape of gene expression, linking genome to phenotype
in time and space. Its data ecosystem spans multiple layers
that together provide a comprehensive view of transcriptional
activity. (i) Transcript annotations from sources like GEN-
CODE [320] and RefSeq [321] define exon–intron struc-
tures, splice variants, and isoform-level expression. (ii) At
the foundational level, bulk RNA-seq and single-cell RNA-seq
repositories such as GEO [229], and ArrayExpress [322] house
millions of transcriptomic profiles across tissues, conditions,
and perturbations. (iii) Expression atlases, such as the Human
Cell Atlas or GTEx [323], enable comparative and tissue-
specific analyses of transcriptional activity. (iv) Spatial tran-
scriptomics platforms, including 10x Genomics Visium [324],
Slide-seq [325], and Stereo-seq [326], link gene expression
profiles to precise tissue coordinates, enabling spatially re-
solved analyses of cell-cell interactions, microenvironmental
heterogeneity, and histopathological context. Public reposito-
ries like SpatialDB [327] aggregate thousands of such datasets
across diverse species and conditions, facilitating cross-study
comparisons and integration with histology images. (v) Gene
co-expression networks, such as STRING [328] co-expression
edges, provide functional grouping of genes based on cor-
related activity. These transcriptomic resources form a rich,
structured, and temporally resolved representation of cellular
states, readily convertible into graph-, token-, or prompt-based
formats for integration with other omics layers in large-scale
modeling.
Proteomics is often described as multimodal, but, strictly
speaking, the field rarely couples images with free text in the
way vision-language benchmarks do. Instead, it juggles molec-
ular representations drawn from distinct information channels:
(i) structured knowledge bases such as UniProtKB deliver
expertly curated sequences, domains and post-translational
modifications for more than 250 million proteins [233], among
them, the reviewed subset UniProtKB/Swiss-Prot (0.57 mil-
lion entries, as of August 2025) is the most widely used;
while the Protein Data Bank (PDB) stores atomic coordinates
15

for experimentally determined folds [329] ; (ii) interaction
networks fuse biochemical and genetic evidence—STRING
merges literature, co-expression and synteny to build genome-
wide association graphs [330], whereas BioGRID [331] and
IntAct [332] record bench-validated contacts; (iii) symbolic
ontologies provide a shared semantic layer, with the Gene
Ontology defining controlled terms for function, process and
localization [333]; (iv) image resources such as the Human
Protein Atlas place thousands of proteins into tissue and
cellular context by immunohistochemistry and fluorescence
microscopy [334]; (v) computational structure repositories,
notably the AlphaFold Protein Structure Database, extend
empirical coverage with high-confidence models for millions
of previously unsolved proteins [335]; and (vi) time-resolved
quantitative datasets from mass-spectrometry pipelines are
shared through the ProteomeXchange consortium [336], with
PRIDE as its flagship archive [337]. Seamlessly combining
these heterogeneous modalities yields synergistic insight, e.g.,
PDB experimental structures and AlphaFold DB predicted
models (surfaced via PDBe-KB) jointly constrain interaction
graphs from STRING, BioGRID, and IntAct; ontology-aware
statistics translate large-scale microscopy screens into testable
biological hypotheses; and longitudinal mass spectrometry
experiments connect dynamic post-translational regulation to
spatial relocalization inferred from imaging. Although cor-
pora already formatted as dialogue for LLM training remain
scarce, the underlying repositories constitute machine-readable
graphs, tables and sequences that can be converted into textual
prompts or retrieval-augmented contexts with minimal tem-
plating. Emerging pipelines therefore marry graph databases
with transformer representation learning, reconcile identifiers
across formats, and propagate uncertainty, all under FAIR stan-
dards [338] (Findable, Accessible, Interoperable, Reusable)
such as MIAPE [339] and ProteomeXchange-XML [336].
As these resources expand and model architectures mature,
a genuinely integrative, causally grounded “digital proteome”
becomes feasible, where each protein is simultaneously en-
coded as sequence, structure, dynamic profile, network node
and spatial image, ready for LLM-driven reasoning across the
molecular landscape.
Beyond the molecular central dogma, additional omics
layers provide complementary biochemical and environmental
perspectives. Metabolomics profiles small-molecule metabo-
lites to capture biochemical activity and phenotypic state, with
repositories such as the Human Metabolome Database [340]
and MetaboLights [341] supporting pathway-level integra-
tion with other omics. Microbiome studies characterize the
composition and functional potential of microbial communi-
ties through metagenomic and metatranscriptomic sequencing,
with resources like the Human Microbiome Project [342]
and MGnify [343] enabling host–microbe interaction analyses.
Exposome research examines the totality of environmental
exposures, including diet, pollutants, and lifestyle factors, us-
ing chemical assays, wearable sensors, and curated biomarker
databases such as Exposome-Explorer [344]. These layers ex-
tend multi-omics frameworks by linking molecular phenotypes
to ecological and environmental contexts.
From precision medicine and cancer research to environ-
mental science and agriculture, multi-omics data now empower
researchers to tackle complex, interdisciplinary problems and
generate holistic models of biological and ecological sys-
tems [345]–[347].
B. Hierarchical Structure of Scientific Knowledge
Scientific knowledge fundamentally differs from a flat col-
lection of information. Instead, it manifests as a sophisti-
cated hierarchical system that mirrors the progressive nature
of human cognition and the evolutionary path of scientific
discovery from phenomena to essence, from the concrete to the
abstract. This inherent stratification resonates with established
knowledge hierarchy models, most notably the DIKW (Data-
Information-Knowledge-Wisdom) pyramid articulated by Ack-
off [348] and systematically analyzed by Rowley [349], which
posits that knowledge emerges through qualitative transfor-
mations rather than mere accumulation. However, as Ze-
leny [350] observed in mapping knowledge forms from “know-
nothing” through “know-what” and “know-how” to “know-
why,” scientific inquiry demands a more nuanced taxonomy
that captures both procedural and explanatory dimensions.
Building upon these theoretical foundations while addressing
the unique epistemological requirements of scientific practice,
we propose a five-tiered framework encompassing factual, the-
oretical, methodological-technological, modeling-simulation,
and insight levels. This stratification reflects what Baskarada
and Koronios [351] characterize as the need to contextualize
knowledge hierarchies within specific domains, incorporating
the computational and instrumental dimensions essential to
contemporary science. Each level represents not merely a
repository of information but a distinct mode of understanding,
exhibiting emergent properties that reflect the transformative
nature of scientific knowledge construction. The following sec-
tions will systematically examine each stratum, revealing how
this hierarchical architecture facilitates both the organization
of existing knowledge and the generation of novel scientific
insights.
To this end, we organize this subsection into five intercon-
nected components, each representing a distinct level of scien-
tific knowledge, as shown in Fig. 14. These levels include: the
Factual Level (Sec. II-B1), the Theoretical Level (Sec. II-B2),
the Methodological and Technological Level (Sec. II-B3),
the Modeling and Simulation Level (Sec. II-B4), and the
Insight Level (Sec. II-B5). In addition, we discuss Dynamic
Interactions and Evolution (Sec. II-B6) which highlights the
iterative feedback loops across levels that collectively drive
scientific progress. Finally, we conclude this subsection with
the implication of such hierarchy (Sec. II-B7), which not only
underscores the progressive deepening from data to discovery
but also provides a structured foundation for developing Sci-
LLMs that can effectively capture and utilize the multifaceted
nature of scientific data.
1) Factual Level: At the foundation of scientific knowledge
lies the factual level—direct observational data, experimental
measurements, and empirical evidence that constitute our pri-
mary interface with the physical world. This raw, unprocessed
information serves as the bedrock for all subsequent scientific
understanding.
16

Factual Level
Raw Observational and Experimental Data
measurement data, observation records,  experimental results
Theoretical Level
Scientific Laws and Principles Framework
mathematical equations, causal models, hypothesis validation
Methodological & Technological Level
R&D Methodologies and Technical Tools
experimental protocols, algorithms and instrumentation
Modeling & Simulation Level
Computational Models and Predictive Systems
numerical simulation, digital twins
Insight Level
Scientific Discoveries and Innovative 
Breakthroughs
new theories, paradigm shifts
Data 
Collection
Pattern 
Discovery
Hypothesis 
Validation
Theoretical 
Innovation ↻
→
→
→
1
2
3
4
5
Dynamic
Interactions
Fig. 14: Hierarchical structure of scientific knowledge. The
framework comprises five levels: factual (raw data), theoretical
(laws and principles), methodological/technological (methods
and tools), modeling/simulation (computational models), and
insight (discoveries). The bottom panel illustrates the iterative
cycle linking these levels through data collection, pattern
recognition, hypothesis testing, and theory development.
Factual data is characterized by its objectivity and minimal
human intervention. When astronomers collect astronomical
imaging data, such as multi-band images [352], and addi-
tional light curves and spectra from distant galaxies, parti-
cle physicists capture collision events at the Large Hadron
Collider [72], gravitational-wave detectors measure strain sig-
nals [353], or biologists sequence genetic material [354], they
obtain direct representations of nature’s state. Despite instru-
mental limitations, these data fundamentally reflect objective
reality independent of theoretical frameworks.
Modern experiments generate data of unprecedented di-
mensionality and structural complexity. High-energy physics
experiments like A Toroidal LHC Apparatus (ATLAS) and
Compact Muon Solenoid (CMS) produce order-of-tens of
terabytes of collision data per second [72], while LIGO and
Virgo release strain data sampled at 16,384 Hz [65]. This
heterogeneity spans all domains: multi-channel neural record-
ings capture brain dynamics at millisecond resolution [355],
single-cell RNA sequencing reveals cellular heterogeneity with
millions of transcripts [356], multi-omics platforms integrate
genomic, proteomic, and metabolomic data [61], agricultural
sensors monitor crop phenotypes across spatial and temporal
scales [357], and Earth observation satellites generate multi-
spectral imagery for climate monitoring [358].
Critical to scientific data is its spatiotemporal context.
Astronomical observations acquire meaning only when an-
chored by precise coordinates and timestamps, enabling cross-
instrument calibration and transient detection. Self-supervised
models that jointly encode images, spectra, and light curves
demonstrate that meaningful representations emerge through
multimodal fusion [359]. Similarly, seismic wave arrivals at
distributed stations enable earthquake triangulation and Earth
structure probing [360], [361], while drug discovery relies on
temporal pharmacokinetic profiles [362] and agricultural yield
predictions depend on phenological timing [363]. In the field
of Earth science, the spatiotemporal characteristics of data
are particularly prominent. This is primarily reflected in the
fact that spatial scales of Earth science data often need to
be mapped to specific geographic resolutions. For example,
in [364], global meteorological variables are represented using
a 128 × 256 tensor, providing a spatial discretization suitable
for modeling over the entire globe. Regarding temporal res-
olution, different tasks require data at distinct time intervals.
For some short-term nowcasting tasks [365], [366], data are
typically recorded at 10-minute intervals, enabling the capture
of rapidly evolving atmospheric phenomena. In contrast, for
medium-range forecasting tasks [367], [368], data are usually
sampled every 6 hours to balance data volume with the relevant
timescales for prediction.
Inherent uncertainties and noise are integral to factual
data. Quantum experiments face fundamental measurement
limits [77], biological studies contend with individual vari-
ation and technical noise [78], astronomical observations
are severely degraded by atmospheric turbulence [369], and
clinical trials must account for patient heterogeneity [370].
These uncertainties inform confidence bounds and guide robust
analytical methods across all scientific disciplines.
2) Theoretical Level: The theoretical level transcends em-
pirical observations through diverse forms of abstraction and
formalization. Beyond mathematical equations such as New-
ton’s mechanics [371], Maxwell’s electromagnetism [372],
Schr¨odinger’s quantum mechanics [373], and Hodgkin-Huxley
neural dynamics [374], scientific theories employ multiple
representational frameworks.
Conceptual models capture fundamental principles: the
central dogma in molecular biology [375], plate tectonics
in geoscience [376], and the Standard Model in particle
physics [377]. Classification systems organize knowledge hier-
archically: Linnaean taxonomy [378], the periodic table [379],
Gene Ontology [236], and astronomical object catalogs [248].
Network representations reveal systemic relationships: protein
interaction networks [380], metabolic pathways [381], ecolog-
ical food webs [382], and brain connectomes [383]. Computa-
tional models bridge theory and prediction: climate circulation
models [384], molecular dynamics simulations [385], popu-
lation genetics algorithms [386], and pharmacokinetic com-
partmental models [387]. Statistical frameworks quantify un-
certainty: Bayesian inference in phylogenetics [388], machine
learning in multi-omics integration [61], and cosmological
parameter estimation [389].
These diverse theoretical representations exhibit hierarchical
organization and domain-specific validity. Mathematical for-
malisms enable precise predictions; conceptual models provide
intuitive understanding; classification systems facilitate knowl-
edge organization; network models reveal emergent properties;
computational approaches handle complexity. Together, they
transform raw data into actionable scientific knowledge, cre-
ating a multi-layered theoretical infrastructure that supports
discovery, prediction, and technological innovation across dis-
ciplines [67].
3) Methodological and Technological Level: Between raw
facts and abstract theories lies a crucial intermediate layer of
methods and tools that transform theoretical predictions into
17

testable hypotheses and raw data into theoretical insights.
Scientific methodology has evolved from simple compara-
tive studies to sophisticated experimental designs across disci-
plines. Revolutionary techniques open new frontiers: CRISPR-
Cas9 enables precise genomic editing [390], ultracold atom
Bose-Einstein condensation paved the way for quantum sim-
ulation [391], and high-throughput sequencing enables multi-
omics profiling [61].
Computational methods bridge theory and experiment.
Monte Carlo algorithms [392] underpin simulations from
protein folding to climate modeling. Machine learning ex-
tracts patterns from massive datasets, e.g., AlphaFold [393]
predicts protein structures, while algorithms identify astronom-
ical objects and reconstruct neural circuits [394]. Statistical
frameworks ensure rigorous inference: particle physics com-
monly adopts a five-sigma threshold for discovery [395], while
Bayesian approaches provide principled uncertainty quantifi-
cation across fields [79].
Instrumental technologies extend observation into new
realms. From Ruska’s electron microscope [396] to modern
cryo-electron microscopes (cryo-EM), from LIGO’s detection
of 10−21-level spacetime strains [65] to single-cell sequenc-
ing [397], these tools fundamentally alter what questions we
can ask. This creates feedback loops where better instruments
enable deeper theories, which guide development of more
sophisticated technologies.
4) Modeling and Simulation Level: This level involves
utilizing numerical simulations to replicate complex systems.
Virtual experiments enable researchers to test hypotheses and
predict phenomena otherwise difficult or costly to study.
Contemporary modeling emphasizes multi-scale integration.
Materials science connects quantum calculations at atomic
scales to macro-level material behaviors [76]. Climate mod-
eling integrates short-term atmospheric processes with long-
term ocean dynamics, bridging local weather and global
climate change [398]. Astronomy links transient events like
supernovae to long-term galaxy evolution spanning billions
of years [399]. Physics-informed neural networks merge
physical laws and data-driven approaches, enabling effective
data-physics fusion for fluid dynamics simulations with no-
table demonstrations from aerospace to biomedical applica-
tions [400], [401]. Life sciences employ multi-scale models to
explore molecular interactions and biological systems [402].
Computational simulations accelerate drug discovery by pre-
dicting molecular interactions [403]. Multi-omics approaches
integrate genomic, proteomic, and metabolomic data to de-
cipher disease mechanisms and guide personalized treat-
ment [61]. Neuroscience simulations range from synaptic pro-
cesses to brain-wide activity [404], while agronomic models
forecast crop performance under varying environmental con-
ditions [405]. Rigorous verification and validation processes
ensure model reliability, confirming computational accuracy
and predictive validity against experimental data, which is
critical in nuclear engineering, aerospace, and medical cer-
tifications [406].
Thus, the modeling and simulation level serves as a foun-
dational tool, supporting modern scientific exploration and
informed decision-making.
5) Insight Level: At the apex of the scientific hierarchy,
the insight level represents transformative moments when dis-
parate knowledge coalesces into revolutionary understanding.
Cross-disciplinary fusion has repeatedly catalyzed such break-
throughs: Shannon’s information theory meeting molecular
biology birthed bioinformatics, revealing life as an information
processing system [407], [408]; neuroscience converging with
physics produced brain imaging technologies that decode
neural activity patterns [409]; astronomical spectroscopy com-
bined with quantum mechanics unveiled stellar nucleosynthe-
sis, explaining element formation across the cosmos [410].
These interdisciplinary insights demand intellectual flexibility
to recognize patterns across traditional boundaries, from pro-
tein folding dynamics mirroring energy landscape theory in
physics [411], to agricultural genomics borrowing population
genetics models to enhance crop resilience [412].
Scientific revolutions often emerge from careful attention
to anomalies that challenge existing frameworks. Classical
physics predicted unbounded ultraviolet radiance at short
wavelengths under the Rayleigh-Jeans law; Planck’s quan-
tization of energy in 1900 resolved this “ultraviolet catas-
trophe” and birthed quantum theory [413]. Similarly, the
discovery of reverse transcriptase shattered the central dogma
of molecular biology [414], while anomalous galactic rotation
curves revealed dark matter’s existence [415]. In pharma-
cology, unexpected drug side effects have led to therapeutic
breakthroughs: sildenafil’s transition from angina treatment
to erectile dysfunction exemplifies serendipitous discovery
through anomaly recognition [416]. True conceptual inno-
vation transcends problem-solving to introduce novel frame-
works: Darwin’s natural selection fundamentally altered our
view of life’s relationship to time [417]; plate tectonics uni-
fied previously disparate geological phenomena [418]; sys-
tems biology’s emergence revealed that biological function
arises from network interactions rather than isolated compo-
nents [402].
In the era of multi-omics and big data, extracting genuine in-
sight requires navigating information overload through human-
AI collaboration. Machine learning excels at pattern recog-
nition across genomic, proteomic, and metabolomic datasets,
uncovering disease signatures invisible to traditional analy-
sis [61]. Yet human judgment remains essential for distinguish-
ing correlation from causation, contextualizing discoveries
within theoretical frameworks, and recognizing which patterns
reflect fundamental principles. The future of scientific insight
lies in this synergy, where computational power amplifies
human creativity to reveal nature’s hidden connections across
scales from quantum to cosmic, from molecular to ecological.
6) Dynamic
Interactions
and
Evolution:
Scientific
progress emerges from dynamic interactions between hierar-
chical levels of knowledge, creating intricate feedback loops
that drive discovery forward. This process manifests through
three primary mechanisms: bottom-up induction, top-down
deduction, and horizontal method transfer.
Inductive processes transform observations into theoreti-
cal understanding across disciplines. In astronomy, Kepler’s
analysis of Brahe’s observations yielded planetary motion
laws, later unified by Newton’s gravitational theory. Modern
18

life sciences follow similar trajectories: genomic sequencing
reveals patterns explained through molecular and evolutionary
models; neuroimaging data drives theories of brain function;
agricultural field trials inform crop optimization strategies;
and multi-omics integration uncovers systems-level biological
principles. In physics, deduction channels theoretical insights
into experimental design. Einstein’s 1916 prediction of grav-
itational waves guided decades of detector development, cul-
minating in LIGO and Virgo’s detection of spacetime strains
(∼10−21 m) from binary black-hole mergers in 2015, con-
firming century-old predictions and inaugurating gravitational-
wave astronomy [419].
Horizontal method transfer catalyzes unexpected advances.
X-ray crystallography transitioned from mineralogy to re-
vealing biomolecular structures; machine learning algorithms
developed for image recognition now predict protein folding
and drug-target interactions; network analysis from sociology
illuminates ecological interactions and neural connectivity;
spectroscopic techniques from physics enable remote sensing
in Earth science and metabolomics profiling. This evolution
follows a spiral pattern where theories transcend and include
predecessors, i.e., classical mechanics subsumed within rela-
tivity and quantum mechanics, Mendelian genetics integrated
with molecular biology, revealing why earlier frameworks
succeeded within their domains while pointing toward a more
comprehensive understanding. Such dynamic interactions are
essential for developing AI systems that capture science’s
creative essence beyond pattern matching.
7) Implications for Sci-LLMs: This hierarchical frame-
work carries profound implications for the development and
deployment of Sci-LLMs. Each level offers distinct computa-
tional challenges and opportunities for language model inte-
gration. At the factual level, LLMs must learn to parse hetero-
geneous data formats, extract patterns from high-dimensional
observations, and maintain spatiotemporal context, which is
essential for tasks like automated literature mining and ex-
perimental data interpretation. The theoretical level demands
that models internalize mathematical formalisms, causal rela-
tionships, and domain-specific ontologies, enabling them to
reason about scientific laws and generate testable hypothe-
ses. The methodological level requires LLMs to understand
experimental protocols, computational workflows, and instru-
mental constraints, facilitating automated experiment design
and method recommendation. At the modeling and simula-
tion level, language models can serve as interfaces between
natural language queries and complex computational engines,
translating scientific questions into simulation parameters and
interpreting results. Finally, the insight level challenges LLMs
to perform cross-domain synthesis and creative hypothesis
generation, capabilities that emerge from training on the full
spectrum of scientific knowledge rather than isolated datasets.
By incorporating data from all five levels, Sci-LLMs can
transcend simple information retrieval to become active par-
ticipants in the scientific discovery process, bridging human
intuition with computational power.
C. Key Challenges in Scientific AI
In the field of scientific AI, especially within LLMs and
MLLMs, several key challenges must be addressed to en-
able meaningful scientific understanding and reasoning. These
challenges include interpretability (Sec. II-C1), cross-scale
and multimodal integration (Sec. II-C2), as well as dynamic
knowledge evolvement (Sec. II-C3), all of which are essential
for enhancing the effectiveness of these models in scientific
applications.
1) Interpretability in Scientific AI: Interpretability remains
a major bottleneck. Scientific reasoning is inherently logical,
based on clear explanations and justifications. However, LLMs
and MLLMs are typically perceived as “black-box” models,
making it difficult to understand the rationale behind a model’s
reasoning or output. This challenge is particularly acute in
scientific domains, where understanding the “why” and “how”
behind an answer is just as important as the answer itself.
Interpretability is crucial for building trust in Sci-LLMs,
especially in high-stakes fields such as drug discovery and
climate modeling. In LLM/MLLM area, prompting or training
the model with chain-of-thought (CoT) [420], [421] emerges
as an effective technique to elicit explicit, natural-language
reasoning capability of LLMs. CoT enables the model to
write a step-by-step reasoning trace, breaking down complex
tasks before giving the final answer. This makes the reasoning
path more transparent and provides clearer insights into its
decision-making. The recent work, BioReason [422], intro-
duces this multi-step reasoning strategy into DNA foundation
models, enabling deep, interpretable biological reasoning from
complex genomic data. By integrating a DNA foundation
model with an LLM and constructing a biological CoT,
BioReason empowers the LLM to directly process and reason
with genomic information, fostering multimodal biological
understanding. Through reinforcement learning, the model
refines its multi-step reasoning capabilities, leading to biologi-
cally coherent deductions and outperforming traditional single-
modality models on biological reasoning benchmarks. Overall,
conducting CoT reasoning in scientific AI models is particu-
larly challenging due to the complexity and domain-specific
nature of scientific knowledge. Unlike generalist models, sci-
entific reasoning involves hypothesis-driven logic grounded in
empirical evidence, requiring a precise understanding across
disciplines such as biology, chemistry, and physics. Therefore,
more work is needed to develop transparent models that can
offer both scientific accuracy and explainable reasoning.
2) Cross-scale and Multimodal Integration: Another ma-
jor hurdle in the application of LLMs and MLLMs to scientific
reasoning is their ability to handle cross-scale and multimodal
integration. Scientific data is often characterized by hierar-
chical structures that span multiple scales, from microscopic
phenomena (e.g., molecular dynamics in chemistry) to macro-
scopic phenomena (e.g., weather patterns or ecosystem behav-
ior). For example, in computational biology, understanding the
behavior of a cell involves integrating data from individual
molecules to entire tissues, which can require models to si-
multaneously process both fine-grained details and large-scale
systems. Traditional LLMs excel at processing textual data but
19

struggle to model spatiotemporal dependencies across scales.
Moreover, scientific reasoning frequently involves multimodal
data, typically combining text, images, numerical data, and
experimental results. This requires models to seamlessly inte-
grate heterogeneous data sources [73], [74]. The challenge is
further exacerbated when the information comes from different
experimental setups or different measurement modalities, each
requiring tailored processing pipelines that preserve important
domain-specific features. For instance, bioinformatics deals
with an extensive variety of data, including DNA, RNA,
protein sequences, and drug molecules [63]. MLLMs have
the potential to address this complexity by integrating text,
images, audio, and other modalities. They offer promising op-
portunities to enhance scientific understanding by connecting
disparate data points and inferring relationships across these
varied modalities. Initiatives such as the National Institutes
of Health’s “Advancing Health Research through Multimodal
AI” [423] exemplify this trend, aiming to develop data-driven
multimodal AI approaches to model, interpret, and predict
complex biological, behavioral, and health systems. However,
significant challenges persist in achieving seamless multimodal
integration. MLLMs frequently struggle with complex multi-
modal and multi-step reasoning tasks, often relying on shallow
multimodal cues or defaulting to text-dominant reasoning
rather than truly integrated understanding. A major bottleneck
in their development is the scarcity of appropriate, high-quality
multimodal scientific datasets.
To address these challenges, models need to move beyond
isolated data streams and embrace a holistic integration of
cross-scale and multimodal information to create truly unified
frameworks that can seamlessly integrate complex scientific
data and perform rigor scientific reasoning.
3) Dynamic Knowledge Evolvement:
One of the most
prominent challenges in applying LLMs and MLLMs to scien-
tific domains is ensuring knowledge update and evolvement.
In scientific research, knowledge evolves dynamically, with
new discoveries constantly challenging existing theories. This
makes it difficult for models trained on static datasets to
maintain consistency with the most current body of sci-
entific knowledge. Models that fail to continuously update
their knowledge bases risk generating outdated or conflicting
information, which can undermine their utility in domains
like medical research, physics, or environmental science. To
fix this, we need to explore new methods like automated
knowledge injection and model adaptation. These approaches
would allow models to continuously integrate new research
findings, ensuring they remain coherent and aligned with the
rapidly changing world of scientific discovery.
D. Quality Standards for Scientific Datasets
Assessing the quality of scientific data is essential for
developing robust scientific AI models. In this subsection, we
outline four complementary dimensions that together char-
acterize data quality in scientific contexts. First, accuracy
(Sec. II-D1) assesses how faithfully data represent the under-
lying phenomena. Second, completeness (Sec. II-D2) concerns
the extent to which datasets capture all relevant elements
across content, structure, and temporal coverage. Third, time-
liness (Sec. II-D3) measures the update frequency and re-
sponsiveness of datasets to real-world changes. Finally, trace-
ability (Sec. II-D4) ensures transparency and reproducibility
by documenting provenance, metadata, and version histories.
Together, these aspects provide a systematic framework for
evaluating the reliability, usability, and long-term value of
scientific datasets, standardizing data management practices
and guiding optimal AI deployment.
1) Accuracy: Accuracy is one of the fundamental dimen-
sions of scientific data quality, reflecting how closely data rep-
resent the real world in terms of spatial positioning, temporal
annotation, and signal fidelity. High-accuracy data not only
enhances the training efficiency and inference precision of AI
models, but also directly impact the credibility of scientific
conclusions. For example, in geospatial datasets, Landsat
8 satellite imagery, after ground control point correction,
achieves a geolocation error of 15 to 30 meters, indicating
high spatial precision [424]. In contrast, location information
from some social media platforms is often only annotated
at the city level, offering coarse granularity that hinders
fine-grained modeling [425]. In the physical sciences, the
Materials Project provides data generated via first-principles
calculations, controlling model errors, and ensuring reliable
accuracy in band structure and lattice constants [70]. Common
methods for assessing accuracy include mean squared error
(MSE), root mean square error (RMSE), temporal alignment
deviation, and signal-to-noise ratio (SNR), typically quantified
by comparing with ground truth or high-quality benchmark
datasets [426], [427].
2) Completeness:
Completeness refers to the extent to
which a scientific data set adequately covers content, structural
fields, and temporal span, whether it contains all the data
elements that should have been collected. It serves as a foun-
dation for systematic and logical data analysis. In genomics,
completeness is often evaluated by sequencing depth; cover-
age below 10× is generally insufficient to accurately detect
mutations, and modern whole genome sequencing standards
typically require an average coverage of 30× or more [428],
[429]. In the field of materials science, data integrity directly
determines the success or failure of data-driven discovery
of new materials [430]. Methods for assessing complete-
ness include missing value statistics, field coverage analysis,
breakpoint detection, and time series gap identification. For
example, in Earth science, SCDNA [431] filled in missing
data for precipitation, minimum temperature, and maximum
temperature to ensure the data integrity across all weather
stations, which improved the accuracy of spatial interpolation.
Tools such as OpenRefine [432] and DataCleaner [433] can
automatically detect missing entries, structural anomalies, and
null fields, thus improving the overall quality of datasets.
3) Timeliness: Timeliness measures data update frequency,
the latency between data collection and release, and the
speed at which data respond to real-world changes. This
is crucial for applications like emergency response, trend
forecasting, and dynamic modeling. For instance, during the
COVID-19 pandemic, the Johns Hopkins University dataset
was released at daily intervals, enabling rapid epidemic mod-
20

eling and policy decision-making on a global scale [434].
In remote sensing, NASA’s MODIS satellite products are
updated daily, supporting timely environmental monitoring
and disaster assessment [435]. In contrast, traditional datasets
like ImageNet [436] and MNIST have not been updated for
years, making them suitable for algorithm benchmarking but
less relevant for contemporary applications. Meanwhile, open
knowledge bases like Wikidata allow real-time user editing
and provide API-based updates, representing a higher level of
“interactive timeliness” [437]. Timeliness can be systemati-
cally quantified using indicators such as collection-to-release
time lag, average update interval, event response delay, and
timestamp consistency [426], [438].
4) Traceability: Data traceability refers to the ability to
track the complete journey of data from its origin and transfor-
mations to its final use. Traceability has increasingly become
a critical supplementary metric for evaluating scientific data
security and trustworthiness, especially in the context of open
science and data reuse. Highly traceable data should include
complete metadata, change logs, version control records,
and accountability information, meeting the “Findability” and
“Reusability” criteria of the FAIR principles [338]. For ex-
ample, each record on the OpenAIRE platform [439] includes
a unique DOI, data acquisition description, and license de-
tails, significantly enhancing verifiability and reuse credibility.
Moderately traceable data may provide basic metadata but
often lack processing chains, revision histories, or algorithmic
documentation, limiting users’ ability to assess reliability.
Low-traceability data typically lack source documentation
and coherent annotation, rendering them difficult to verify.
For instance, web-scraped research images or code snippets
without provenance or revision records pose considerable
risks in academic usage [440]. Recently, technologies such
as blockchain and cryptographic hash signatures are being
explored to build traceability chains and verifiable records for
scientific data [441].
E. Dimensions for Evaluating Scientific AI
General-purpose LLM benchmarks primarily assess core
natural language processing and general reasoning abilities.
Key evaluation dimensions typically include language un-
derstanding, fluency, factual knowledge recall, reasoning and
problem-solving. These benchmarks are designed to evaluate
broad linguistic competence and general cognitive skills across
everyday or non-specialized domains. Even when covering
technical subjects (e.g., STEM topics in MMLU), they often
assume only basic computational skills and high school–level
science knowledge. Evaluations of factuality and alignment
are typically grounded in general content. In contrast, science-
focused LLM benchmarks require mastery of the depth, pre-
cision, and rigor characteristic of academic research. Beyond
the general dimensions listed above, scientific LLMs must be
evaluated on their ability to engage with domain-specific sci-
entific knowledge, reason with formal systems (e.g., equations,
symbolic logic), retrieve and synthesize scholarly information,
and support hypothesis generation or experimental design.
1) Expert-Level Scientific Knowledge Comprehension and
Retrieval: Unlike general-purpose language models, scientific
AI models must retrieve, comprehend, and apply cutting-edge
research knowledge across diverse scientific disciplines with
domain-level expertise. This knowledge extends beyond gen-
eral encyclopedic facts to include domain-specific equations,
physical constants, technical terminology, and theoretical con-
structs. A model’s ability to access, interpret, and reason
over external academic knowledge is a critical dimension of
evaluation, serving as a cornerstone for enabling automated
scientific discovery. Key evaluation aspects include informa-
tion retrieval, literature-based fact verification, and the inte-
gration of heterogeneous scientific knowledge. For example,
SciBench [442] introduces benchmark tasks requiring the re-
trieval of mathematical equations, chemical laws, and physical
theorems; SciKnowEval [443] spans domains from biology to
materials science, assessing tasks such as molecule identifica-
tion and reaction prediction; and SciQA [108] leverages the
Open Research Knowledge Graph to support complex cross-
domain scientific questions. This dimension challenges models
on both the breadth and depth of scientific understanding,
emphasizing accuracy, completeness, and the ability to engage
with knowledge beyond surface-level facts.
2) Scientific Reasoning and Problem Solving: Scientific
problems often require multi-step reasoning rooted in the
principles of the scientific method. Effective models must be
capable of formulating and decomposing complex problems,
applying relevant scientific laws and theories, and performing
precise numerical computations. SFE [444], for example,
emphasizes advanced reasoning skills of Sci-LLMs, including
the evaluation of scientific attribute understanding and com-
parative analysis. Error analyses of science-focused bench-
marks reveal that key reasoning capabilities include logical
decomposition, causal inference, deductive problem solving,
and abstract reasoning. These tasks extend beyond the scope of
general mathematical puzzles found in standard LLM bench-
marks, demanding the ability to reason about experimental
procedures, derive theoretical formulas, and interpret results
within a scientific framework.
3) Multimodal Scientific Data: Science AI models should
incorporate various modalities other than language. The ability
to understand data diagrams, including figures and tables,
and to conduct quantitative and statistical analysis to identify
scientific trends, is crucial. Furthermore, expert AI models
need to comprehend specialized scientific data that requires
domain-specific knowledge, such as chemical structures and
laboratory images, for high-level reasoning. SciBench [442]
notably includes a multimodal subset with figures and graphs,
highlighting that assessing the ability to interpret visual sci-
entific information is a dimension beyond typical LLMs and
even MLLMs. On the other hand, it remains to be seen whether
current science AI models can fully incorporate and leverage
all these diverse data types effectively for truly advanced
scientific discovery.
III. SCIENTIFIC LARGE LANGUAGE MODELS
Sci-LLMs are emerging as powerful tools for modeling, un-
derstanding, and reasoning across diverse scientific domains.
21

Could you provide the 
SMILES code for this 
chemical?   
Sci-LLMs
Based on the biopsy findings 
shown, what is the cause of 
the patient’s condition?
Physics
 Materials 
Science
Chemistry
Life 
Sciences
Earth 
Science
Astronomy
Floatation beneficiation is based on the 
principle of?  Mineral surface hydrophobicity. 
What's the main color of the 
spiral arms in the image?
What does the image show?
The image shows a large 
international airport …
MedGemma
SeedLLM
ProLLaMA
MechGPT
Xiwu
Poseidon
ChemLM
Chemma
LLM-RDF
ChemLLM
ChatMOF
CrystaLLM
LLM-Prop
K2
OceanGPT
GeoChat
SkyEyeGPT
A 2 kg bracelet, ... . What 
is the speed at which the 
bracelet hits the spring? 
AstroLLaMA
AstroLLaVA
AstroSage
UniMind
Fig. 15: Research scopes of Sci-LLMs across six scientific subjects: physics, chemistry, materials science, life sciences, Earth
science, and astronomy. For each subject, we present representative domain-specific Sci-LLMs and example questions that the
Sci-LLMs are able to solve.
This section begins with a brief touch on the architecture
and training of general LLMs, establishing the groundwork
for their scientific extensions (Sec. III-A), followed by a
survey of general-purpose Sci-LLMs (Sec. III-B). We then
introduce major scientific LLMs across six natural science
domains (Sec. III-C), including physics (Sec. III-C1), chem-
istry (Sec. III-C2), materials science (Sec. III-C3), life sciences
(Sec. III-C4), astronomy (Sec. III-C5), and Earth science
(Sec. III-C6), each with unique data modalities, modeling
challenges, and scientific applications. Fig. 15 illustrates the
research scope of Sci-LLMs covered in this survey.
A. Introduction of Large Language Models
LLMs [35], [445], [446] exhibit strong capabilities in un-
derstanding, generating, and interacting with human language.
LLMs can comprehend the intricate relationships among mas-
sive amounts of text, sequential, and visual data in queries,
and generate corresponding answers following user instruc-
tions. Existing LLMs are mainly based on a decoder-only
transformer architecture [447], which converts human natural
language into a sequence of textual tokens. When equipped
with specific modality encoders, data from other modalities,
such as images or videos, can also be converted into tokens
and processed by LLMs. Then, LLMs generate or expand
information when given an input or condition by extracting
relationships between tokens. The generated tokens are then
decoded into text or other modalities that humans can under-
stand. To enable such capability, LLMs are usually pre-trained
on vast and diverse data using the next-token prediction ob-
jective [445]. This process encodes world knowledge into the
LLMs and serves as the foundation for their capabilities. The
post-training process is crucial for activating and enhancing
the task-specific knowledge that LLMs acquire from the large-
scale data, allowing them to understand user instructions and
solve complex tasks in practical applications.
B. General-purpose Sci-LLMs
Current scientific LLMs are mainly developed from exist-
ing general-purpose LLMs through post pre-training or fine-
tuning on data from specific scientific tasks [448]. They do
not alter the model architecture of existing LLMs. Instead,
domain-specific encoders are used to convert scientific data,
such as medical images and protein sequences, into tokens
compatible with the LLM backbones. Fig. 16 demonstrates
the architecture of LLMs in the scientific domain. They
can achieve significant performance improvement on certain
scientific tasks, but they cannot push the capability boundary
of existing LLMs due to the limited data scale and task
diversity. For example, DARWIN models [449] are fine-tuned
on the open-source LLaMA-7B [34] using about 60 K science-
focused instruction examples covering physics, chemistry, and
materials science. These instructions are carefully collected
from science exams and scholarly papers. SciGLM [41] is
further fine-tuned from a general-purpose LLM with the pro-
posed SciInstruct dataset, which enhances the model’s ability
to understand intricate scientific concepts, derive symbolic
equations, and solve numerical problems. SciInstruct is built
through self-reflective annotation to alleviate data scarcity in
science domains such as Physics and Chemistry.
However, directly fine-tuning open-source LLMs does not
significantly enhance their scientific capabilities because of
a limited training corpus. Therefore, to improve performance
on scientific tasks, a model should be pre-trained on large-
scale scientific data, thereby strengthening its capabilities for
scientific tasks. For example, Galactica [30] is a 120 B param-
eter decoder-only model trained on 106 B tokens drawn from
papers, reference materials, encyclopedias, and other scientific
sources. Its corpus mixes text with scientific sequence repre-
sentations such as protein sequences and chemical formulae,
as well as LaTeX and code. At release, Galactica reported
state-of-the-art results on PubMedQA [450] and MedMCQA-
22

Language Model
...
...
Text Tokenizer
User Query
Response
Scientific Text: Glaucoma is a group of progressive 
optic neuropathies characterized by …
Protein:    <protein>GSGFRKMAF…VTFQ</protein>
Molecule: <SMILES>CC1=CC2C(CO)C2C1</SMILES>
...
Language Model
...
...
Text Tokenizer
User Query
Response
Domain-specific 
Encoder
(a) Text-only scientific language model architecture.
(b) Multimodal scientific language model architecture.
DNA/RNA: <DNA>ATCAATATC…TGAT</DNA>
Fig. 16: Illustration of common model architectures for existing scientific large language models. (a) Left: Text-only language
model architecture showing the processing pipeline where user queries are processed through a text tokenizer, with scientific
text inputs (including disease descriptions, DNA/RNA sequences, protein sequences, and SMILES molecular representations)
as part of the query, to generate responses. (b) Right: Multimodal model architecture featuring a domain-specific encoder that
processes diverse scientific data types (molecular structures, DNA structures, microscopic images, etc.) alongside text inputs,
enabling comprehensive scientific question-answering capabilities through the integration of textual and non-textual scientific
information.
dev [451] and strong performance on mathematical reasoning
and technical knowledge probes, as well as chemistry, biology
and physics capabilities
SciDFM [452] adopts a MoE [48] architecture with 5.6
B active parameters routed across eight experts. It is pre-
trained from scratch on 300 B science-domain tokens covering
mathematics, chemistry, biology, geography, and general sci-
ence, together with 270 B general-domain tokens. This broad
training corpus strengthens the model’s scientific capabili-
ties. SciDFM is then fine-tuned on customized instruction-
tuning data derived from open-source datasets to improve
its performance on downstream scientific benchmarks. Om-
niScience [453] is built on the LLaMA-3.1-70B model and
undergoes domain-adaptive pre-training on a carefully curated
corpus of papers, journals, and textbooks that span general
science and electrochemistry. The model is then instruction-
tuned to improve its understanding of science-specific task
prompts. Finally, OmniScience distills knowledge from the
advanced reasoning model DeepSeek-R1 by fine-tuning on the
s1K-1.1 dataset [454], thereby gaining multi-step reasoning
capability for complex scientific problems. Intern-S1 [47] is a
recently released open-source scientific multimodal foundation
model developed by Shanghai AI Laboratory. It adopts a MoE
architecture with 241B total parameters and 28B activated per
inference step. The language backbone is based on Qwen3-
235B MoE and is extended with specialized encoders, includ-
ing InternViT-6B for vision and a time-series signal encoder,
together with a dynamic tokenizer designed for scientific
formats such as SMILES and FASTA. Trained on over 5 tril-
lion tokens, including 2.5T from scientific domains, Intern-S1
delivers competitive performance on general reasoning tasks
while surpassing both open- and closed-source systems across
multiple scientific benchmarks, such as molecular synthesis
planning, materials property prediction, and crystal stability.
Recently, beyond large-scale pre-training, existing general-
purpose LLMs [455] propose test-time scaling by intro-
ducing Chain-of-Thought reasoning process [420]. Such a
paradigm demonstrates potential in solving complex scientific
tasks, which require reasoning from multiple perspectives
and drawing accurate and interpretable conclusions [456].
To achieve this, recent work tries different approaches. For
example, DeepSeek-R1 [457], built upon DeepSeek-V3-Base
through cold-start training and reasoning-oriented Reinforce-
ment Learning (RL) processes, achieves results comparable
to OpenAI-o1 model [455] on scientific benchmarks such as
MMLU-Pro [81], and GPQA-Diamond [458]. Qwen3 [459]
draws inspiration from DeepSeek-R1 and is designed with
a MoE architecture. It integrates both thinking and non-
thinking modes into a unified framework, allowing the model
to respond adaptively based on task difficulty to avoid unneces-
sary computational overhead compared to DeepSeek-R1. Kimi
K2 [460] scales the MoE architecture to 1 trillion parameters
with 32 billion activated parameters. K2 undergoes a multi-
stage post-training process which is powered by the proposed
large-scale agentic data. Therefore, K2 can interact with real
and synthetic environments using diverse tools, demonstrating
its potential for addressing complex scientific tasks. Gemini
2.5 Pro [461] is a reasoning model that can process multimodal
and long-contextual data. It can handle text, image, video, and
audio inputs with a total context length of 1 million tokens.
This capability makes it well-suited for complex scientific
tasks that involve processing sensor or sequence data from
different devices or databases. Grok 4 [462] is trained with
large-scale RL at pre-training scale, achieving 50.7% accuracy
23

BioBERT
2019
2020
2021
2022
2023
2025
2024
1-4
Life Sciences
Chemistry
Physics
Astronomy
Earth Sciences
Materials Science
Open Source
Close Source
5-8
BioMegatron
Med-PaLM
SciFive
ESM
BioBART
ProGen
ProtGPT2
BioGPT
PubMedGPT
MLF
DoctorGPT
Qilin-Med-VL
MedAlpaca
DoctorGLM
BenTsao
HuatuoGPT
LLava-Med
Med-ChatGLM
K2
9-12
PMC-LLaMA
QiZhenGPT
DrugGPT
DNAGPT
Med-Flamingo
Sunsimiao
GeoChat
AstroLLaMA
BianQue
MechGPT
BioMedGPT
MindGPT
Biomedicine-LLM
polyBERT
OceanGPT
Coscientist
ShenNong-TCM-LLM
AlpaCare
CXR-LLaVA
ChiMed-GPT
ProGen2
MediTron
1-6
7-12
Lingo3DMol
SkyEyeGPT
ChatMOF
Xiwu
Poseidon
PathChat
Taiyi-LLM
Me-LLaMA
Evo
AstroLLaMA-3-8B
TeoChat
EarthDial
Prompt-MolOpt
EarthMarker
AgroGPT
JiuZhou
BioMistral
GMAI-VL
BiomedGPT
TamGen
LLM-RDF
MolBART
1-6
AstroLLaVA
Qwen2-KG
GeoPixel
MATE
ClimateChat
GeoGPT
LLM4SD
Chemma
AstroSage-LLaMA-3.1-8B
ReactSeq
L3M
LLM-Prop
7-12
AlphaGenome
WENTS
WildfireGPT
Woollie
HybriDNA
HealthGPT
EagleVision
MindLLM
GENERator
GENA-LM
Token-Mol
Medgemma
Lingshu
Med-R1
SMILES-BERT
MOFormer
MolXPT
Med-Gemini
SeedLLM
CrystaLLM
CSLLM
Baichuan-Omni-1.5
ClinicalCamel
HuatuoGPT
LLava-Med
Sunsimiao
MindGPT
Biomedicine-LLM
ShenNong-TCM-LLM
Med-R1
ChemLLM
ChemVLM
Baichuan-M1
Baichuan-M2
HyperSIGMA
BrainGPT
GeoLLaVA-8K
Intern-S1
General Science
ESM-2
ESM3
Evo2
hybrid CLM
ChemLM
Fig. 17: Chronological overview of notable Sci-LLMs categorized by six scientific domains, spanning from 2019 through early
2025. Due to the rapid expansion of the field, this figure presents a selective overview. For detailed information, please refer
to Tab. VII.
on the Humanity’s Last Exam (HLE) [463] and demonstrating
strong scientific reasoning capabilities.
The test-time scaling strategy demonstrates strong potential
for enhancing generalization in scientific tasks by understand-
ing multimodal scientific data and reasoning with scientific
tools. In the future, further scaling up the RL process could
lead to frontier intelligence surpassing human capabilities,
enabling novel scientific discoveries and allowing models to
design and conduct experiments using real-world tools in
support of the proposed hypotheses. Moreover, developing a
virtual laboratory environment [54] where LLMs can conduct
experiments and collect experimental feedback would acceler-
ate the training process toward more powerful general-purpose
scientific intelligence.
C. Domain-specific Sci-LLMs
In some cases, domain-specific scientific LLMs can be more
helpful for particular scientific tasks. Such models can be
constructed with well-curated, domain-specific datasets and
training schemes tailored to the target subject. Below, we intro-
duce recent domain-specific scientific LLMs that cover eight
subjects. Fig. 17 demonstrates the development of scientific
LLMs across six subjects.
1) Physics: In the field of physics, scientific LLMs have
begun to take a significantly different path compared to tradi-
tional symbolic modeling and numerical simulation. By inte-
grating LLMs with physics engines and visual modules, these
models are not only capable of processing natural language
descriptions of physical systems but also able to explicitly
estimate physical parameters, simulate dynamic evolution,
and represent physical laws symbolically. They are evolving
from language understanding systems into intelligent tools that
interact directly with scientific workflows.
LLMPhy [464] is a representative model that combines
program synthesis with physics simulation feedback. Its core
idea is to use an LLM to generate symbolic code that can be
executed by a non-differentiable physics engine, enabling iter-
ative refinement of physical parameters like friction, stiffness,
damping, and rotational inertia. In Phase 1, the system uses
trajectories extracted from auxiliary videos, while in Phase 2,
it processes multi-view images with a vision-language model
to reconstruct the scene layout. The TraySim dataset, which
provides paired multi-view images and video trajectories,
supports a closed-loop “analysis-by-synthesis” framework that
allows the model to align simulation results with physical
reasoning. POSEIDON [465] is a model designed for learning
solution operators of partial differential equations (PDEs).
While it does not use natural language as input, its core is a
scalable Operator Transformer with strong temporal modeling
capabilities enabled by time-conditioned layer normalization.
The architecture uses a multi-scale Vision Transformer [466]
to encode spatial fields, and a U-Net-style module to encode
input into latent space. The transformer backbone, along with
time-conditioned layer normalization, enables continuous-in-
time evaluations, with optional autoregressive rollouts during
inference. It is trained in two stages: large-scale pretraining
using an “all-to-all” strategy on PDE trajectories (e.g., Euler,
Navier-Stokes), and small-sample fine-tuning on specific PDE
tasks. POSEIDON achieves high sample efficiency, requiring
only 20 samples to match the performance of the widely-used
FNO that needs 1024 samples. Xiwu [467] is a domain-specific
model for high energy physics (HEP), built on Vicuna-13B-
v1.5. Its system includes a data engine, LLM core, vector
memory, and user-facing interfaces. It is trained in three stages:
continued pretraining on 750M HEP-specific textual tokens,
24

supervised fine-tuning on 26k human-verified QA pairs, and
real-time learning via a just-in-time system where expert users
can inject, correct, or update knowledge in a vector storage for
retrieval. Xiwu outperforms Vicuna-13B in 95% of win-or-
draw rate and surpasses GPT-4 in most tasks involving HEP
software code generation for BESIII Offline Software Sys-
tem(BOSS) [468], demonstrating its domain specialization.
In summary, these models reflect the diverse design and
training strategies adapted for physics tasks. They range from
symbol-to-simulation systems and PDE operator learners, to
physics QA transformers and high-energy physics retrievers.
As they evolve, further integration of multimodal capabilities,
improved spatiotemporal reasoning, and unified knowledge
representation frameworks will be essential for expanding their
scientific utility.
2) Chemistry: In this section, we review the latest advances
in LLMs in the field of chemistry. We begin by examining
their model architectures, training strategies, and the core data
modalities employed, such as molecular structures, reaction
data, spectroscopic information, and scientific literature. Next,
we provide a comprehensive, domain-specific overview of
their applications across key areas in chemistry, including
molecular design, reaction prediction, retrosynthetic analysis,
catalyst discovery, quantum chemistry, and materials science.
Finally, we critically discuss the major challenges and ethical
considerations in the field, and offer a perspective on future
research directions and opportunities for AI-driven chemical
innovation.
ChemLLM [20] is one of the earliest LLMs that is specif-
ically designed for chemistry. It also curates ChemData,
a specialized instruction-tuning dataset, and ChemBench, a
comprehensive benchmark covering nine core chemistry tasks.
InstructMol [469] aligned molecular structure and text via
using a light-weighted projector, following LLaVA’s align-
ment strategy. It leverages a two-stage training scheme which
starts with the multimodal alignment object followed task-
specific instruction tuning. InstructMol supports several tasks,
including molecule property prediction, molecule description
generation, retrosynthesis prediction, etc. ChemDFM [470]
is pre-trained on 34 billion tokens from chemical literature
and textbooks, and fine-tuned with 2.7 million instruction
pairs. As a result, ChemDFM is capable of understanding and
reasoning over chemical knowledge through natural, free-form
dialogue. ChemMLLM [201] is proposed to mitigate the gap in
generating molecular images, establishing a unified MLLM for
chemical understanding and generation across text, molecular
SMILES string, and molecular images. Chem3DLLM [471]
addresses the inability of traditional large language mod-
els to generate accurate 3D molecular conformations due
to incompatible formats, lack of multimodal alignment, and
absence of chemical priors. It introduces a reversible text
encoding of 3D structures, enabling lossless compression
and integration within a language-model token space. A
protein-embedding projector aligns protein pocket represen-
tations, while reinforcement learning with chemical validity
rewards enforces physical plausibility, yielding state-of-the-art
results in structure-based drug design.
3) Materials Science: LLMs have also been widely ex-
plored in diverse tasks in materials science. Recent studies
have applied a transformer-based encoder to learn material
representations. For example, SMILES-BERT [472] is pre-
trained on a vast collection of SMILES corpora to learn molec-
ular representations for property prediction. Similarly, poly-
BERT [473] employs a DeBERTa-based encoder [474] trained
on about 100 million hypothetical polymer SMILES, enabling
end-to-end polymer fingerprinting. MatBERT-bandgap [475]
was pre-trained on about 2 million materials science ab-
stracts, learning latent compositional features. Regression
Transformer [476] adopts a novel multi-task scheme, trans-
lating property regression into sequence outputs by tokeniz-
ing continuous values and alternating masked-language and
regression training phases. Regression Transformer can simul-
taneously predict numeric properties and generate molecular
strings, effectively merging regression and generation tasks.
Some work applies general-purpose LLMs by utilizing
Retrieval-Augmented Generation (RAG) equipped with pro-
fessional databases to solve related tasks. Knowledge integra-
tion is another strength. Qwen2-KG [477] uses Qwen2-72B
together with a retrieved materials knowledge graph to answer
questions about framework materials. By combining chain-of-
thought retrieval with graph facts, it achieves about 91.7%
accuracy on a held-out QA benchmark, outperforming LLM-
only baselines and providing cited sources.
Recent work has investigated fine-tuning a ChatGPT-style
model (i.e., decoder-only transformer) to materials science. For
example, MolXPT [478] is built on GPT-2 [479] and learns
from combined PubMed abstracts and molecular SMILES
data, while GPT-MolBERTa [480] is fine-tuned from a BERT-
like encoder on about 326K molecular descriptions synthe-
sized by ChatGPT. In the molecular domain, MolGPT [481]
uses a GPT-style causal LM objective: it is pre-trained on
millions of SMILES strings and then fine-tuned for condi-
tional generation (scaffold or property guidance). XYZTrans-
former [482] is designed to process molecular structural data
and is a decoder-only transformer trained directly on the raw
3D coordinates of molecules. CrystaLLM [483] is fine-tuned
from the LLaMA-2 model using text-formatted crystal struc-
tures, harnessing billions of parameters to capture atomistic
symmetries. CrystaLLM can generate metastable materials
with a frequency of about 49% when given desired features,
and significantly outperforms diffusion-based models. In syn-
thesis planning, Okabe et al. develop three LLMs (LHS2RHS,
RHS2LHS, TGT2CEQ) [484] to predict chemical equations:
given reactants they predict products (LHS→RHS) or vice
versa, and they can generate balanced chemical equations
for target compounds. Fine-tuning on text-mined inorganic
syntheses raised reaction-prediction accuracy to about 90%,
enabling rapid synthesis route inference. CSLLM [485] is
fine-tuned from LLaMA-3-8B to predict the synthesizability
and precursors of crystal structures. CSLLM reaches approx-
imately 98.6% accuracy on the synthesizability prediction
task, which is vastly higher than that of Density Functional
Theory (DFT)-based filters, for identifying experimentally
realized crystals. CSLLM can also predict the likely pre-
cursors and synthesis methods (solid vs solution), illustrat-
25

ing how LLMs can capture complex experimental domain
knowledge. MechGPT [486] is tailored for material mechanics
and multiscale modeling. It is built on the LLaMA2 model
and fine-tuned using LoRA techniques with domain-specific
question-answering (QA) data. Although its current inputs are
text-based, the model is designed to eventually incorporate
image and structural modalities. Its demonstrated capabilities
include knowledge retrieval, hypothesis generation, and the
construction of interpretable ontological knowledge graphs
for structural insight. While MechGPT’s input is currently
text-only, its architecture is designed to accommodate future
multimodal extensions.
4) Life Sciences: LLMs, pre-trained on large-scale sci-
entific data in the field of life sciences, can adapt to a
wide spectrum of downstream tasks, ranging from generating
accurate diagnostic reports to designing previously unknown
protein structures or novel drugs [21]. These tasks are closely
related to human health. In this part, we review the develop-
ment of LLMs in the field of life sciences, including model
architectures, training schemes, and applications.
Multi-Omics. DNA, RNA, and protein sequences have been
seen as the “language of life” in computational biology in re-
cent years [487].Recent advances in multi-omics research have
developed two complementary families of domain-specific
language models: (i) encoder-centric genomics/protein lan-
guage models (GLMs/PLMs) that are trained from scratch on
biological sequences to learn molecular representations and bi-
ological constraints like the EVO series [488], [489] and ESM
series [490]–[492]; and (ii) LLM-augmented systems that
integrate omics data into instruction-following text LLMs to
generate natural-language outputs, typically leveraging models
from category (i) as omics encoders.
For category (i), EVO [488] represents a groundbreaking
advancement in genomic foundation modeling, being trained
on an extensive dataset comprising over 80,000 bacterial and
archaeal genomes, as well as millions of predicted phage
and plasmid sequences, totaling 300 billion nucleotide tokens.
This model establishes scaling laws for DNA that complement
those discovered in language and vision domains. Additionally,
EVO seamlessly integrates across DNA, RNA, and proteins,
achieving zero-shot function prediction that rivals specialized
language models. EVO2 [489] scales training to 9.3 trillion
DNA bases spanning all domains of life and extends context
to genome scale (up to 1M tokens), accurately predicting func-
tional impacts of genetic variation and supporting genome-
level design. Focusing on proteomics foundation models,
the methodological landscape is evolving from unconditional
sequence modeling toward a closed loop of controllable
generation—cross-modal semantic alignment—interactive rea-
soning: at the outset, ESM-1b [490] demonstrates that large-
scale unsupervised modeling of 250M protein sequences learns
representations with emergent structure/function information
enabling accurate long-range contact prediction and remote-
homology organization. MSA Transformer [493] applies axial
attention directly to multiple-sequence alignments to cap-
ture coevolutionary dependencies, yielding unsupervised struc-
tural features and strong contact-prediction signals. ESM-
1v [494] introduces a protein LM whose zero-shot likeli-
hoods match state-of-the-art supervised predictors on deep
mutational scanning benchmarks for functional effect pre-
diction. ESM-IF1 [495] performs inverse folding by training
on millions of predicted backbones, achieving 51% native
sequence recovery (72% for buried residues) on held-out
structures and generalizing to complex design settings. ESM-
2/ESMFold [496] enables direct single-sequence, atomic-level
3D structure prediction without MSAs, delivering strong ac-
curacy at substantially higher speed than traditional MSA-
based pipelines. ESM3 [492] unifies sequence, structure, and
function in a single multimodal generative model that reasons
across modalities and designs novel, functional proteins far
from known families. ProtGPT2 [497] learns the “grammar”
of proteins via large-scale unsupervised training, enabling
de novo generation close to natural sequence statistics; on
controllability and scale, ProGen [498] injects functional
and localization conditions into autoregressive modeling, and
ProGen2 [499] further expands parameters and corpora to
improve generalization and fitness prediction; along the path
from general LLMs to domain adaptation. Ankh [500] attains
strong baselines under lower compute through protein-oriented
training and architectural optimizations; centering on text-
driven design,
As instances of (ii), LLaMA-Gene [40] adapts LLaMA2-7B
via domain-adaptive continued pretraining on a 39.5B-token
DNA corpus from reference genomes, followed by instruction
tuning with 800K synthetic multi-omics QA pairs (variant
interpretation, promoter prediction, transcript identification).
ProLLaMA [501] migrates general models to protein multi-
tasking via vocabulary pruning and instruction alignment.
ProteinDT [502], PAAG [503], and Pinal [504] map natural-
language intent to controllable sequences—respectively via
text-protein alignment, annotation-sequence multi-level do-
main alignment, and a two-stage pipeline—and support se-
quence editing; for interactive analysis, ProteinGPT [505] and
ProteinChat [39]/ProtChatGPT [506] align sequence/structure
representations with LLMs to enable multi-turn QA around
function and structure; in cross-modal translation, ProTrans-
lator [507] and BioTranslator [508] achieve zero-shot transfer
between text and protein/biological data (text ↔protein/data);
to enhance interpretability, Prot2Text [509] directly generates
free-text functional descriptions from sequences. Evolla [510]
is a protein-language generative model with 80 billion param-
eters, designed to decode the molecular language of proteins
by integrating sequence and structural information on proteins,
together with user-query information. This capability is en-
abled by the proposed 546 million protein-centric question-
answer pairs. Taken together, this line of work progresses
from “learning the protein grammar” to “conditional control-
lable generation” and onward to “cross-modal alignment and
dialogue-centric agents,” converging toward a design-analysis-
feedback loop for proteomics foundation models.
Recent work proposes to understand DNA, RNA, and
protein sequences simultaneously. NatureLM [43] presents
a general Sci-LLM instruction-tuned across genomics, pro-
teomics, biochemistry, and materials science. Its post-training
data comprises over 1.1M instruction pairs generated from
curated databases such as UniProt, Ensembl, and GenBank,
26

spanning protein functions, gene regulatory elements, and
variant effects, formatted in English QA and reasoning chains.
ChatNT [511] further establishes a multi-task conversational
agent trained on curated instruction datasets across DNA,
RNA, and protein domains. It integrates 361M English and
DNA tokens from 18 task categories (e.g., methylation, splic-
ing, polyadenylation, protein melting), and uses a unified text-
to-text objective with an English-aware Perceiver projection
to align genomic sequences with natural language prompts.
Collectively, these models highlight the shift toward cross-
omics instruction tuning that enables unified biological rea-
soning across diverse molecular inputs.
Molecular and Cellular Biology.
Some studies propose
applying LLMs in the field of molecular and cellular biology.
These LLMs focus on understanding the morphology and
function of cells in living organisms.
For example, MolecularGPT [512] is an instruction-tuned
large language model (LLaMA-2-7B–based) for molecular
property prediction that operates on SMILES strings, enabling
zero or few-shot inference across diverse biological molecules.
It is obtained by QLoRA fine-tuning on a hybrid instruction
set spanning over 1,000 property tasks compiled from sources
such as ChEMBL bioassays, CHEMBL physico-chemical
properties, and QM9 (HOMO/LUMO), with about 3.5 GB
of training tokens. scGPT [513] is transformer-based single-
cell foundation model with a specialized masked-attention
scheme that jointly learns gene and cell embeddings to support
cell-type annotation, batch correction, perturbation-response
prediction, and gene network inference. It is pretrained in
a self-supervised manner on over 33 million normal human
cells from the CELLxGENE atlas and then adapted via task-
specific fine-tuning pipelines for diverse downstream single-
cell applications.
LLMs have also emerged as powerful tools for de novo
molecular design. By treating chemical structures as “lan-
guages” (e.g., using SMILES notation), models like Chem-
BERTa [514] and MolBERT [515] generate novel molecules
with desired properties. For instance, Edwards et al. [202]
fine-tuned GPT-3 on chemical datasets to produce drug-like
molecules, achieving hit rates comparable to high-throughput
screening. In drug discovery, LLMs accelerate lead optimiza-
tion. They predict bioactivity by analyzing sequence data
from proteins and ligands. A notable example is the inte-
gration of LLMs with reinforcement learning in models like
Chemformer, which designs molecules for specific targets,
such as COVID-19 inhibitors [516]. These approaches reduce
synthesis trials by 50-70%, as validated in virtual screening
benchmarks.
Healthcare and Medical Science.
Recent LLMs in the
field of healthcare and medical science are primarily adapted
from existing general-purpose LLMs [517]. These models are
typically further pre-trained on domain-specific corpora, such
as clinical reports, medical literature, and imaging data. They
are then fine-tuned with medical instruction-response pairs to
serve diverse user groups, including doctors, students, and
patients.
Due to computational costs, recent medical LLMs only
perform supervised fine-tuning (SFT) on general LLMs using
medical-related instruction data. This process introduces the
capability to solve medical tasks to general LLMs. For exam-
ple, BioMistral [518], BioMedLM [519], ClinicalCamel [520],
and MedAlpaca [521] collect medical question-answering
pairs and doctor-patient dialogue data, and perform SFT on
open-source LLMs such as LLaMA, achieving performance
improvements on several medical benchmarks, such as MedM-
CQA [451], PubMedQA [450] and MedQA [522]. Med-PaLM
series [31] are developed from a 540B parameter LLM,
PaLM, are directly instruction-tuned on PaLM, and using
a combination of prompt engineering technologies [523] to
adpat to medical quesiton-answering tasks. Apollo [524] is a
lightweight multilingual medical LLM, which collects medical
data covering the six most widely spoken languages. Such a
lightweight model can be deployed in hospitals to help protect
the privacy of medical data. HuatuoGPT [525] is fine-tuned
from general LLMs using medical instruction and conversation
data from both real-world sources and ChatGPT, in order to
introduce medical-specific skills and to distill capabilities from
powerful general LLMs.
Only performing SFT on existing general LLMs cannot
further improve model performance in the healthcare field.
Further scaling up the pre-training scale is beneficial to model
performance. For example, PMC-LLaMA [526] is based on
LLaMA and was pre-trained on data containing 4.8 million
biomedical academic papers and 30,000 medical textbooks.
HuatuoGPT-II [42] combines pre-training and instruction tun-
ing, using over 5.2 million medical documents from encyclo-
pedias, books, and web corpora, as well as 142,000 medi-
cal instructions. It is based on the Baichuan2-Base models.
CHIMED-GPT [527] collects over 214 million multilingual
tokens in Chinese and English from medical textbooks and
encyclopedia data, and is pre-trained on Ziya-13-v2 [528].
This work also conducts RLHF [529] to further enhance the
safety of the model’s responses. Zhongjing [530] also conducts
complete training process including pre-training, instruction-
tuning and RLHF. Besides, Zhongjing supports multi-turn
dialogues to meet real-world diagnosis requirements. Me-
LLaMA [531] is continually pre-trained on LLaMA2 with 129
billion tokens from biomedical datasets, research papers, and
clinical notes, and is then fine-tuned on 214,000 instruction
tuning samples from clinical domains. Baichuan-M1 [532] is
trained from scratch and further scales up the pre-training pro-
cess, using over 20 trillion tokens, which include both general
data and medical-related data such as clinical information and
patient records. Baichuan-M1 achieves significant performance
across more than 17 medical-related benchmarks.
Clinical practice is inherently multimodal. The diagnostic
process requires physicians to synthesize information from
diverse sources, including the patient’s verbal descriptions
(text/audio), physical signs (visual), medical imaging (vi-
sual), and laboratory findings (structured data). Accordingly,
MLLMs capable of processing multiple data modalities are
considered a critical path forward in the evolution of medical
AI [533]. Recent work investigates the use of MLLMs in
the medical field, mainly focusing on two primary tasks:
medical reports generation [534] and medical Visual Ques-
tion Answering (VQA) [535], [536]. LLaVA-Med [537], as a
27

pioneering work in this domain, successfully transferred the
capabilities of a general-purpose MLLM, i.e., LLaVA, to the
biomedical field. It is fine-tuned on the visual instruction-
tuning data from PubMed papers and can understand medical
images. CXR-LLaVA [538] and Radiology-LLaMA2 [539] are
specifically developed for chest X-ray (CXR) imaging. They
utilize GPT-4 to extract impressions and findings from ra-
diology reports in order to enhance their ability to interpret
X-ray images, and they can generate reports in a clinical
style. Med-Flamingo [540] is continually pre-trained on paired
and interleaved medical image-text data from publications and
textbooks, and can solve medical VQA tasks through few-shot
learning without further fine-tuning on the VQA datasets.
Moreover, several works aim to extend the medical MLLMs
capability to diverse medical tasks requiring more modality in-
formation and reasoning capabilities. HuatuoGPT-Vision [541]
and GMAI-VL [542] collect large-scale medical multimodal
data from PubMed papers and open-source medical image
datasets. They are pre-trained on extensive medical image-
caption pairs and further fine-tuned on data containing di-
verse instructions in the medical field. Therefore, they can
solve a wide range of tasks from different departments.
MedGemma [543] further extends the in-context length of
MLLMs and can process long-context data such as medi-
cal videos or patient electronic health records. HuatuoGPT-
o1 [544] aims to introduce complex medical reasoning ca-
pability by fine-tuning the model on question-answer pairs
with complex reasoning trajectories and conducting RL
with verifier-based rewards to enhance complex reasoning.
Medground-r1 [545] leverages GRPO with spatial-semantic
rewards to enhance medical image grounding without CoT
annotations. GMAI-VL-R1 [546] introduces multimodal medi-
cal reasoning capability by directly applying RL to verifiable
multiple-choice VQA data, thereby enhancing performance on
medical image diagnosis and VQA tasks without collecting
complex reasoning data.
Agriculture. In this section, we examine the emerging
family of agricultural LLMs, covering their architectural
choices, training strategies, and domain-specific capabilities.
SeedLLM [547] is a domain-specific large language model
for seed science, built on Qwen2.5-7B. It is pre-trained on
RiceCorpus (a bilingual corpus of 1.38 million agronomy
papers) and GeneralCorpus [548], [549], targeting terminology
and knowledge from modern breeding research. The fine-
tuning stage uses QAs from both general and agricultural
domains, synthesized using GraphGen [550], a knowledge-
graph-based generation framework. SeedLLM is evaluated on
SeedBench, a multi-task benchmark co-designed with domain
experts for seed breeding applications. The model remains
closed-source. PLLaMA [551] is an open-source language
model tailored for plant science. It extends LLaMA-2 with 7B
and 13B parameter variants, and is continuously pre-trained
on 1.5 million plant-related scholarly articles curated from
the S2ORC corpus. Fine-tuning employs 1,030 instruction
samples adapted from LIMA. The model is evaluated on a
held-out plant science quiz set, showing strong comprehen-
sion of plant genetics, physiology, and breeding concepts.
AgroGPT [552] is an open-source multimodal assistant for
agronomic consultation, with 3B and 7B vision-language
variants based on LLaVA. While no raw pretraining corpus
is used, AgroGPT is fine-tuned on AgroInstruct—a dataset of
70k synthetic QA pairs created from agricultural images using
LLM-generated captions and instructions. It is evaluated on
AgroEvals, a domain-specific benchmark for fine-grained crop
disease and pest identification. AgroGPT demonstrates supe-
rior performance over generalist models and human baselines
in image-based agronomic reasoning.
Neuroscience. Recent advances in LLMs for neuroscience
have integrated both neuroscience literature and neural data
from multiple modalities such as EEG and fMRI to im-
prove interpretability and performance on brain related tasks.
BrainGPT [553] is a domain specialized language model for
neuroscience, fine tuned from Mistral 7B using low rank
adaptation on 1.3 billion tokens from neuroscience literature.
Evaluated on BrainBench, a benchmark for neuroscience-
related question answering, BrainGPT outperformed both gen-
eral models and human experts. EEG-GPT [554] is a domain-
specific LLM based on OpenAI’s GPT-3 (da Vinci), designed
for EEG classification and interpretation. It achieves strong
few-shot performance using only 2% of training data and em-
ploys tree-of-thought reasoning with specialist EEG tools for
interpretable, step-wise decision-making. NeuroLM [555] is a
multi-task foundation model that integrates EEG signals into
a language modeling framework. It trains a vector-quantized
tokenizer to convert EEG data into discrete neural tokens,
and fine-tunes a GPT-2
[479] language model with multi-
channel autoregression and instruction tuning. The model
is evaluated on neural decoding tasks including sleep stage
classification, epilepsy detection, motor imagery decoding, and
emotion recognition, demonstrating that incorporating neural
representations significantly enhances brain signal analysis.
UMBRAE [556] unifies multimodal brain decoding by aligning
fMRI signals with pretrained CLIP
[557] visual features
via a universal brain encoder. Cross-subject training promotes
subject-agnostic representations, which are connected through
adapter modules to a Vicuna-7B/13B-based multimodal lan-
guage model for semantic captioning and spatial grounding.
MindGPT [558] is a GPT-2–based model that decodes vi-
sual stimuli from non-invasive brain recordings into natural
language. It integrates a CLIP-guided encoder with cross-
attention mechanisms to align brain, visual, and linguistic rep-
resentations, enabling accurate semantic interpretation of vi-
sual experiences. MindLLM [559] is a subject-agnostic model
for fMRI-to-text decoding that combines a neuroscience-
informed encoder with Vicuna-7B. Trained via brain instruc-
tion tuning, it supports a wide range of tasks—including
perception, memory retrieval, symbolic language processing,
and reasoning—achieving flexible and accurate semantic in-
terpretation of brain activity. UniMind [560] is a general-
purpose EEG foundation model that leverages InternLM2.5 to
unify multi-task brain decoding by bridging the modality gap
between neural signals and language representations. It intro-
duces a Neuro-Language Connector to distill spatiotemporal
EEG patterns into LLM-interpretable embeddings and employs
a Task-aware Query Selection mechanism for adaptive task-
specific decoding, achieving robust performance across diverse
28

EEG tasks without task-specific fine-tuning. Neuro-GPT [561]
is built on the open-source GPT-2 model, combined with
a convolutional-transformer EEG encoder trained using self-
supervised learning. It reconstructs masked EEG segments
from large-scale clinical data and demonstrates strong gener-
alizability in downstream motor imagery classification tasks.
5) Astronomy: In this section, we review recent advances
in astronomy-specific LLMs, highlighting representative mod-
els such as AstroLLaMA [562], AstroLLaVA [563], and As-
troSage [564]. These models are generally built upon LLaMA-
2 or LLaMA-3 architectures, with LLMs focusing on text
understanding and generation, and MLLMs incorporating vi-
sual encoders (e.g., CLIP ViT-L/14) and projection layers to
integrate astronomical images with text. Most models follow
a two-stage training strategy: continual pre-training (CPT)
using large-scale astronomy literature (e.g., arXiv abstracts,
Wikipedia, textbooks) to enhance general domain understand-
ing, and SFT using domain-specific tasks, such as question
answering, multiple-choice reasoning, and synthetic dialogue
generation. Low-Rank Adaptation (LoRA) [565] and other
parameter-efficient tuning methods are commonly used for
resource-effective adaptation. These developments lay the
foundation for a new generation of astronomy-focused models,
which we detail below in terms of their architectures, training
pipelines, and domain-specific capabilities.
AstroLLaMA [562] is an astronomy-specific language model
fine-tuned from LLaMA-2. It focuses on traditional language
modeling tasks, with text as the modality. The model was fine-
tuned using over 300,000 astronomy abstracts (approximately
95 million tokens) from the arXiv database and employs LoRA
to improve resource efficiency. In a text generation task, the
model was tested by having it produce astronomy-related
abstracts. The results showed that AstroLLaMA achieved a
32.5% reduction in perplexity compared to LLaMA-2, gen-
erating text that was more specific to the astronomy field
and possessed deeper insights. Furthermore, AstroLLaMA’s
embedding space better reflects the semantic differences within
astronomical text. Despite issues such as knowledge gaps and
the generation of fictitious data, AstroLLaMA outperformed
general-purpose models overall. AstroLLaVa [563] is a mul-
timodal visual-language model for astronomy that combines
images and text. Built on the LLaVA 1.5 architecture, its
visual encoder uses the CLIP ViT-L/14 model, and its language
model is based on LLaMA 7B. Fine-tuning data is sourced
from publicly available images and captions from NASA’s
“Astronomy Picture of the Day” (approximately 9,962 image-
text pairs), the European Southern Observatory (approximately
14,617 image-text pairs), and the NASA/ESA Hubble Space
Telescope (approximately 5,204 image-text pairs). GPT-4 is
used to generate a synthetic dialogue dataset from the image
captions. Training utilizes a two-stage fine-tuning strategy:
in the first stage, only the visual-language projection layer
is trained using astronomical image-text pairs, with the pre-
trained visual encoder and language model fixed. In the
second stage, synthetic astronomy question-answer pairs are
used for instruction tuning, resulting in end-to-end fine-tuning
of the entire model. The evaluation used the Galaxy 10
DECaLS dataset [566]. The model was tasked with describing
galaxy images from the G10 test set. The results show that
AstroLLaVA performs slightly better than the LLaVA 1.5
model in the task of describing galaxy images. AstroSage-
LLaMA-3.1 [567] is based on Meta’s LLaMA-3.1 model. Like
AstroSage-LLaMA-3.1-8B, this model is trained in two main
phases: CPT and SFT. It also employs a model merging
strategy to combine the strengths of multiple models. However,
during the SFT phase, it is fine-tuned using a diverse dataset,
including the LLaMA-Nemotron-Post-Training Dataset, the
OpenHermes 2.5 dataset, and domain-specific QA datasets.
Evaluation was performed using the AstroMLab-1 benchmark,
which consists of 4,425 high-quality, human-verified multiple-
choice questions from the Annual Review of Astronomy and
Astrophysics paper, which were not included in the training
set. The results show that AstroSage-LLaMA-3.1 achieved
an accuracy of 86.2% without enabling inference mode, sur-
passing all other open weights and proprietary models tested,
proving that domain specialization can significantly improve
the performance of the model in a specific domain.
These astronomy-specific models reflect the increasing ma-
turity and specialization of LLMs and MLLMs in science.
With better perplexity, semantic understanding, and strong
performance on domain benchmarks, they show the value of
targeted pretraining and fine-tuning.
6) Earth Science:
The application of LLMs in Earth
science is undergoing a significant transformation, moving
from general-purpose models to highly specialized, domain-
adapted solutions. This shift is driven by the necessity to
handle unique data characteristics, such as immense volume,
high granularity, and diverse modalities. The advancements
discussed here are rooted in the development of sophisticated,
domain-specific datasets and innovative architectural designs
tailored for scientific inquiry.
A foundational challenge in adapting LLMs for scientific
domains is the scarcity of high-quality, expert-level instruc-
tion data. To bridge this gap, several works have focused
on creating specialized text-based datasets. In the field of
geoscience, K2 [568] was trained on GeoSignal, the first
supervised instruction dataset enabling models to understand
and respond to complex queries from geoscientists. Similarly,
ClimateChat [569] was built upon the ClimateChat-Corpus, a
large-scale, high-precision dataset constructed through a semi-
automated pipeline combining self-QA, web scraping, and
self-instruct methods to enhance expertise in climate change
topics. For ocean science, OceanGPT [570] leveraged the
DoInstruct Framework, which uses a multi-agent approach to
automatically generate expert-level instructions, overcoming
the prohibitive cost of manual annotation.
In the multimodal domain, the unique characteristics of
remote sensing (RS) imagery have necessitated the creation
of equally specialized datasets. EagleVision [571] was trained
on the proposed EVAttrs-95K, the first large-scale dataset
designed for fine-grained object-level understanding, enabling
comprehension and description of intricate object attributes in
RS imagery beyond simple classification. EarthMarker [572]
was supported by the RSVP dataset, containing approximately
3.65 million multimodal pairs of image-point-text and image-
region-text, enabling nuanced interpretations guided by vi-
29

LLM
MLLM
0
20
40
60
80
100
Count
96 (74.4%)
33 (25.6%)
LLM vs MLLM
(a) LLM vs MLLM ratio.
0
10
20
30
40
Count
InternLM
Baichuan
ChatGLM
BERT
Vicuna
GPT
Qwen
LLaMA
3 (2.6%)
4 (3.4%)
5 (4.3%)
6 (5.1%)
9 (7.7%)
11 (9.4%)
15 (12.8%)
45 (38.5%)
Base Model Family (Top-K)
(b) Base model family distribution (Top-K).
0
10
20
30
40
50
Count
32B
3B
2B
6B
8B
70B
13B
7B
3 (2.0%)
3 (2.0%)
3 (2.0%)
5 (3.3%)
7 (4.6%)
8 (5.2%)
14 (9.2%)
49 (32.0%)
Parameter Size (Top-K)
(c) Parameter size distribution (Top-K).
Fig. 18: Statistical overview derived from Table VII. (a) Sci-LLM vs Sci-MLLM counts. (b) Base model family distribution;
only top-K are shown. (c) Parameter size distribution (all variants of multi-scale models are counted individually); only top-K
are shown.
sual prompts. For pixel-level grounding, GeoPixel [573] was
trained on GeoPixelD, which provides over 50,000 grounded
phrases and 600,000 object masks, achieving end-to-end seg-
mentation in high-resolution images. To address ultra-high-
resolution imagery, GeoLLaVA-8K [574] utilized the Back-
ground Token Pruning and Anchored Token Selection meth-
ods, enabling complex dialogue and reasoning on images up
to 8K resolution.
The scope of these models extends beyond static im-
age analysis to encompass dynamic and multi-source data.
EarthDial [575] was trained on EarthDial-Instruct, the largest
remote sensing instruction-tuning dataset, comprising over 11
million instruction pairs across modalities like RGB, Synthetic
Aperture Radar, and multispectral data, enabling reasoning
over diverse Earth observation data. HyperSIGMA [576] uni-
fies HSI interpretation across tasks and scenes, scalable to
over one billion parameters. SelectiveMAE [577] dynami-
cally encodes and reconstructs semantically rich patch tokens,
thereby reducing the inefficiencies of traditional MIM mod-
els caused by redundant background pixels in RS images.
RoMA [578] enhances scalability for high-resolution images
through a tailored auto-regressive learning strategy. Further-
more, TEOChat [579] was powered by the proposed TEOChat-
las, the first instruction-following dataset for temporal Earth
observation data, making it the first vision-language assistant
capable of engaging in dialogues about change detection
and time-series analysis. These innovative models, and the
specialized datasets that train them, represent a significant step
toward enabling more dynamic and comprehensive analysis
for applications like environmental monitoring and disaster
response.
D. Sci-LLMs Analysis
Our survey highlights key trends in the development of
Sci-LLMs. Roughly three quarters of current models are text-
only LLMs, while MLLMs comprise only about one quarter
(Fig. 18a). This imbalance reflects the dominance of text-
based scientific sources (e.g., papers, patents, manuals) and
the scarcity and cost of fine-grained multimodal supervision.
Where MLLMs emerge—such as in medical imaging, life
sciences, or remote sensing—they typically rely on smaller
but higher-quality paired datasets that enable stronger cross-
modal alignment. Looking forward, as scientific discovery in-
creasingly depends on integrating heterogeneous signals (e.g.,
astronomy that requires optical, radio, and X-ray observations
to confirm cosmic events [580], or climate science that unites
satellite images, numerical models, and field reports [581]),
the demand for Sci-MLLMs capable of synthesizing diverse
modalities will grow. Thus, the current text-centric dominance
may gradually give way to balanced multimodal ecosystems,
powered by improved dataset curation and efficient alignment
techniques.
The base-model landscape is now characterized by the
primacy
of
open-source,
general-purpose
families,
with
LLaMA [34], [446], [582] constituting the largest share
and Qwen [35], [459], [583] close behind, complemented
by instruction-tuned derivatives (e.g., Vicuna [584]) and a
thinner tail of encoder-style models (e.g., BioBERT [25],
ESM-2 [491]) that persist primarily in legacy or narrow-
domain pipelines (Fig. 18b). Their dominance is explained
by mature tooling, stable alignment recipes, scalable pa-
rameter ranges, and ultra-large pretraining corpora, which
jointly enable low-cost adaptation and strong zero-/few-shot
performance. In practice, open-source base models further
facilitate rapid adaptation to emerging application scenarios
by leveraging newly collected data via supervised fine-tuning
(SFT), lightweight parameter-efficient methods, or modest
instruction refinement. More broadly, progress is shaped by
advances in training data curation and systems integrations,
including retrieval-augmented workflows for maintaining up-
to-date knowledge, high-quality expert QA and protocol-style
instruction sets (e.g., DoctorGLM [585], MedAlpaca [521]),
targeted generation of challenging examples to improve cov-
erage of rare cases, and the use of structured, tool-supported
reasoning with simulators, analysis libraries, or code execution
to support verifiable complex reasoning.
Across recent public tallies and our own tabulated statis-
tics of released scientific models, parameter sizes in prac-
tice skew strongly toward smaller scales: 7B models consti-
tute the largest share, 13B models are also frequent, while
30

70B-and-above models remain comparatively rare (Fig. 18c).
This distribution reflects multiple deployment constraints, in-
cluding privacy and compliance requirements (e.g., HIPAA,
GDPR) [586], inference latency and operational cost, the need
for determinism and reproducibility, as well as on-premise,
air-gapped, or data-sovereign environments. Many scientific
tasks, such as protein folding, gene expression modeling, and
materials discovery, are knowledge-dense yet narrow in scope,
where small-to-mid sized models (7B–13B), when paired with
retrieval augmentation or fine-tuning on scientific corpora,
often achieve competitive performance relative to much larger
counterparts [24]. Preferences for such models also mirror
practical considerations: limited compute and memory in
academic/lab settings, energy constraints, restricted access
to sensitive datasets, and the complexity of deploying very
large systems in regulated domains [587]. Looking ahead, as
hardware efficiency (e.g., distributed training, mixed preci-
sion, memory optimization) and privacy/governance tooling
advance, very large models are expected to play a greater
role on the centralized training side, serving as knowledge
sources, data generators, and evaluators. Nevertheless, distilled
or quantized 7B–13B models are likely to remain the backbone
for local and resource-constrained deployments, including in
hospitals, laboratories, and field-deployed systems (e.g., satel-
lites or environmental sensors) [588]. These trends and drivers
may vary across disciplines and institutions, and shares should
always be interpreted with respect to the specific datasets and
benchmarks at hand.
From a data–task interface perspective, several emerging
themes are shaping the design and application of Sci-LLMs.
One promising direction is evidence-grounded generation with
traceable provenance, which is essential for credible scientific
outputs. Unlike general-purpose LLMs prone to hallucinations,
Sci-LLMs are expected to produce verifiable claims with
transparent source attribution, with data cards, citations, spatial
or experimental coordinates, and retrieval logs serving as key
scaffolds for trust and reproducibility [24], [585]. Another
challenge and opportunity lies in cross-modal alignment. High-
quality supervision (e.g., region-level grounding in remote
sensing) consistently yields better results than weakly aligned
approaches where images are abstracted into generic embed-
dings [574], [589]. A notable trend is the move toward agentic
Sci-LLMs that integrate with scientific tools and workflows.
Instead of static question-answering, these models are in-
creasingly capable of retrieving literature, querying databases,
running molecular or geospatial simulations, executing code
for statistical analyses, and orchestrating lab or field data
pipelines. This agentic behavior enables more reproducible
and actionable scientific discoveries [521], [585]. Finally,
temporal awareness and continual adaptation are becoming
increasingly important, since scientific knowledge evolves
rapidly. Versioned corpora [590], adaptive retrieval windows,
and uncertainty calibration [86] help models remain aligned
with the current state of knowledge [587]. These patterns
should be viewed not as fixed principles but as recurring
observations that point to current bottlenecks and promising
frontiers for Sci-LLM research.
Overall, the current landscape of Sci-LLMs is character-
ized less by architectural innovation and more by strategic
adaptations of general-purpose foundations to domain-specific
needs. The field remains heavily influenced by open-source
base models, notably the LLaMA and Qwen families, which
dominate due to their scalability, robust tooling, and strong
zero-shot generalization. Model size skews toward the 6B–13B
parameter range, reflecting pragmatic constraints around de-
ployment costs, privacy-compliant inference, and operational
efficiency in resource-limited environments such as clinics,
labs, and edge devices. Performance gains are increasingly
driven by sophisticated data pipelines and workflow integra-
tions rather than pure scaling: knowledge-grounded generation
provides verifiable outputs and supports hallucination mitiga-
tion [591], [592], tool-assisted reasoning enables executable
simulations and code, and high-quality cross-modal alignment
supports meaningfully integrated understanding of text, im-
ages, structures, and geospatial data. Looking ahead, progress
will hinge on improving verifiability and temporal adaptabil-
ity—embedding provenance tracking, supporting continuous
knowledge updates [591], and refining agentic capabilities
for real-world scientific tasks. As multimodal and tool-using
paradigms mature, Sci-LLMs are poised to evolve from pas-
sive question-answering systems into active participants in
the scientific process, facilitating discovery across biomedical,
chemical, material, and environmental sciences [593].
IV. SCIENTIFIC DATA FOR PRE-TRAINING
Pre-training forms the foundation of LLMs and MLLMs
by equipping them with broad, domain-relevant knowledge
before task-specific fine-tuning. These models are typically
pre-trained on massive and diverse datasets - for example,
Yi [594] utilizes data from multiple sources including web-
pages, code, papers, and Q&A content, while LLaMA [34]’s
pre-training corpus spans approximately 1.4 TB across various
domains such as CommonCrawl [595], GitHub, Wikipedia,
and academic sources (Fig. 19a). This extensive scale and
broad coverage ensure models acquire comprehensive knowl-
edge across different domains and languages. In the scientific
domain, pre-training datasets must capture both the scale and
diversity of knowledge, from symbolic laws of physics to com-
plex biological systems and planetary processes. Unlike gen-
eral web corpora, scientific datasets often combine structured
experimental results, simulation outputs, specialized notations,
and multimodal formats. The breadth and fidelity of these
datasets directly influence a model’s ability to understand, rea-
son, and generate within a specific scientific context. Looking
at the scientific pre-training landscape, Intern-S1 exemplifies
this specialized approach by dedicating 2.5T tokens (45.8%
of its total corpus) specifically to scientific content across six
domains (Fig. 19b), providing the deep domain knowledge
essential for superior performance on complex scientific tasks.
In the following subsections, we move from the smallest build-
ing blocks of matter (molecules and atoms) through complex
biological systems and planetary-scale phenomena, concluding
with interdisciplinary datasets that bridge multiple domains.
The details of the pre-training datasets are summarized in
Tab. IV.
31

(a) Pre-training dataset mixture of LLaMA [34], Yi [594] and GPT-3 [445].
Data Distribution
Science Breakdown
2.5T
(45.8%)
0.7T
(12.1%)
2.3T
(42.1%)
13.0%
7.3%
6.4%
19.4%
10.5%
14.7%
28.8%
Science
Code
General
Physics
Materials Science
Chemistry
Life Sciences
Mathematics
Earth Science
Other Sciences
(b) Distribution of continual pre-training data for Intern-S1 [47], involving 5.5T high-quality textual tokens with 2.5T scientific tokens across
over six domains. Adapted from [47].
Fig. 19: Pre-training dataset distributions for different language models. (a) Dataset mixture comparison across GPT-3, LLaMA,
and Yi models. (b) Detailed distribution of Intern-S1’s continual pre-training data with emphasis on scientific domains.
A. Physics, Chemistry and Material Sciences: the Founda-
tion for Understanding the Material World
Pre-training in physics, chemistry, and materials science
focuses on representing the structure, dynamics, and properties
of matter. These domains benefit from a combination of high-
fidelity simulations, experimental measurements, and textual
corpora that encode formal theories and experimental proce-
dures. The challenge is balancing the precision of synthetic
data with the complexity of real-world measurements, while
integrating symbolic, numerical, and visual modalities.
1) Physics:
In physics, the pre-training landscape is
dominated by large-scale synthetic datasets derived from
computational
frameworks
such
as
molecular
dynamics
(LAMMPS [596]), finite-element methods, and cosmological
simulations (Illustris [597], Bolshoi [598], as well as grid-
based hydrodynamics with Enzo [599]). These provide high-
resolution spatiotemporal fields, wavefunctions, potentials,
and other symbolic outputs that are invaluable for surrogate
modeling and embedding physics-informed inductive biases.
However, their controlled and often idealized nature makes it
challenging for models to generalize to noisy or chaotic real-
world conditions.
Experimental and observational datasets in physics, such as
those from particle physics experiments including the Euro-
pean Organization for Nuclear Research (CERN) [600] and
the Large Hadron Collider beauty (LHCb) [601], condensed
matter platforms including STM [135] and angle-resolved
photoemission spectroscopy [602], or large astronomical ob-
servatories including Hubble Space Telescope (HST) [198]
and Atacama Large Millimeter/submillimeter Array [603],
are comparatively scarce in formats readily consumable by
machine learning pipelines. The data are often fragmented
across specialized repositories, use inconsistent formats, and
may be restricted by access policies. Structured, standardized
collections remain rare, limiting their use for large-scale pre-
training.
Efforts such as the Galactica simulation database [604]
llustrate a move toward open, FAIR-compliant dissemination
of astrophysics data. By centralizing metadata and reducing
datasets from diverse simulation projects, Galactica covers
cosmology, galaxy formation, and the interstellar medium, and
supports generation of standardized, API-accessible high-level
products (e.g., 1D profiles, 2D maps, 3D cubes). Although not
yet matching the sheer scale of Illustris or Bolshoi, it con-
tributes critical data diversity for building more generalizable
physical science foundation models.
On the textual side, corpora such as SciBERT [24], pre-
trained on 1.14M full-text scientific papers (including physics
literature), underscore the importance of domain-relevant
language pre-training. Multimodal datasets like Multimodal
ArXiv [605] which comprises 6.4M figure-caption pairs and
100K figure-based QA pairs, bridge visual and symbolic scien-
tific reasoning. These complement simulation-heavy datasets
by incorporating authentic visuals, diagrams, and plots, thus
32

enriching models’ capacity for both symbolic reasoning and
real-world data interpretation.
2) Chemistry: Chemistry builds directly on physical princi-
ples to describe the structures, transformations, and properties
of molecules and compounds. Pre-training datasets in chem-
istry reflect the field’s diversity of representations, including
SMILES [20], [201] and SELFIES strings for linear encodings,
molecular graphs [469] for connectivity patterns, and 3D
coordinate formats (SDF, PDB) for spatial conformation [471].
These enable models to learn relationships between topology,
stereochemistry, and molecular function.
Large, curated molecular libraries form the backbone of
chemical pre-training. ZINC [606] offers millions of com-
mercially available drug-like compounds, ChEMBL [217]
aggregates bioactive molecules with activity annotations, and
MOSES [607] provides a standardized benchmark set for gen-
erative modeling. Early pre-trained models such as SMILES-
BERT [472] and more recent architectures like SMILES-
Mamba [608] demonstrate how sequence-based learning can
support tasks ranging from de novo molecular genera-
tion [609], [610] to property prediction [611] and structure-
based drug design [612].
Chemical reaction datasets expand the scope of pre-training
to transformation pathways. The USPTO dataset [613], con-
taining million-scale reactions annotated with reactants, prod-
ucts, catalysts, temperatures, and other conditions, supports
retrosynthesis planning, reaction outcome prediction, yield
estimation, and catalyst selection [244], [614]. Together, these
datasets enable LLMs/MLLMs to model both static chemical
structures and dynamic processes.
3) Materials Science: Materials science extends chemistry
into the design, synthesis, and characterization of substances
with tailored properties. Pre-training datasets in this field span
multiple modalities: crystallographic structure files, chemical
notation datasets, property-specific compilations, and large
textual corpora.
Crystallographic datasets, encoded in CIF formats, are cen-
tral for learning structural-property relationships. The Ma-
terials Project [70] offers over half a million entries cov-
ering known and predicted materials, while OQMD [615]
contains more than a million calculated electronic property
records. ICSD [616] curates inorganic crystal structures, and
specialized datasets such as CoRE MOF [617], QMOF [618]
and DigiMOF [619] target metal-organic frameworks. NO-
MAD [620] and Materials Project Trajectory [621] scale up
to millions of entries, incorporating dynamic simulation data.
Sequence representation datasets like USPTO [218] and
JARVIS-DFT [622] provide alternative chemical encodings
(InChI, IUPAC, SELFIES), while large chemical libraries such
as ZINC [623] overlap with both chemistry and materials
applications. Property-specific datasets [624] focus on tar-
geted physical or mechanical attributes, enabling specialized
pre-training for predictive modeling. Textual datasets like
MatScholar [625], with millions of publications, comple-
ment structured data by providing unstructured knowledge on
material-property relationships.
Across physics, chemistry, and material sciences, pre-
training datasets evolve from highly idealized simulations to
richly annotated experimental corpora, and from symbolic
equations to multimodal figure-caption pairs. The scale and
diversity of these resources are critical: physics simulations
anchor models in governing laws, chemical libraries teach
molecular diversity and reactivity, and material databases
bridge microscopic structures with macroscopic properties.
Future progress will hinge on integrating these modalities
by combining simulation outputs, experimental measurements,
and literature-derived knowledge, to build foundation models
capable of reasoning seamlessly from atomic-scale phenomena
to engineered material systems.
B. Life Sciences: Complexity from Molecules to Systems
1) Molecular and Cell Biology: At the molecular scale, the
central dogma, i.e., DNA-to-RNA-to-protein, shapes the data
landscape for pre-training. Sequence-based datasets dominate,
with different corpora focusing on small molecules, nucleic
acids, or proteins.
Pre-training in the life sciences aims to equip LLMs and
MLLMs with the ability to represent, reason about, and
generate knowledge across the intricate hierarchy of living
systems. This hierarchy begins at the smallest biological units
(e.g., genes, proteins, and metabolites), progresses through cel-
lular and tissue-scale processes, and culminates in organismal,
clinical, and ecological contexts. Biological data is inherently
heterogeneous: sequence strings, structural models, expression
matrices, microscopy images, clinical narratives, and more.
Effective pre-training datasets must therefore capture both the
fine-grained molecular details and the higher-order interactions
that emerge across scales, while aligning multimodal inputs
into unified representations.
Current biology pre-training datasets for LLMs span mul-
tiple molecular modalities, with molecular, protein, and nu-
cleic acid sequences constituting the primary data types.
For molecular representations, several notable datasets have
emerged: SPICE [626], PCdes [627], PubChemSTM [628],
and MoMu [629] utilize SMILES strings or molecular graphs
for pre-training, while TCPA [630] focuses on protein se-
quences. In the protein domain, UniRef [631] databases serve
as the foundational resource, with UniRef50 and UniRef90
containing approximately 49 million protein sequences after
clustering at 50% and 90% sequence identity, respectively.
For nucleic acid sequences, DNABERT [632] utilized the
human reference genome (Hg38.p13) for pre-training, while
DNABERT-2 [318] expanded to multi-species genomes from
135 species, creating a dataset 12 times larger than its pre-
decessor. RNA pre-training has leveraged RNAcentral [633]
database with million-scale non-coding RNA sequences.
The evolution of these datasets reflects a clear trend toward
multi-species, multimodal approaches and increased scale.
Recent advances include sophisticated tokenization strategies,
such as DNABERT-2’s [318] Byte Pair Encoding (BPE) re-
placing traditional k-mer tokenization, and the incorporation
of structural and functional annotations beyond raw sequences.
Cross-modal pre-training has gained traction, with an increas-
ing number of datasets [628], [629] bridging molecular struc-
tures with natural language descriptions, enabling more com-
prehensive molecular understanding. Future directions point
33

toward larger-scale datasets that incorporate 3D structures,
epigenetic modifications, and cross-species evolutionary rela-
tionships, as evidenced by emerging comprehensive bench-
marks [318] for systematic model evaluation across diverse
genomic tasks.
2) Multi-Omics: Multi-omics pre-training aims to unify
genomics, transcriptomics, proteomics, and beyond into in-
tegrated representations.
At the genomic level, pre-training corpora often start
with the complete human reference genome (GRCh37 [634])
and population-scale sequences from projects like the 1000
Genomes Project [635]. To enhance generalization and cross-
species utilization, pretraining corpora are often further ex-
panded to encompass genomic sequences from multiple
species, such as archaea, fungi, and vertebrate mammalian,
collected from scientific repositories such as NCBI Gen-
Bank [95]. Omni-DNA [636] constructs a 30B-token corpus by
sampling and deduplicating genomic fragments from NCBI’s
multi-species genome database, covering bacteria, archaea,
fungi, plants, and vertebrates. GeneChat [637] focuses on
encoding human genomic syntax and semantics by extracting
1024 bp fragments from the GRCh38 reference genome.
DNAHLM [638] adopts a hybrid corpus of equal-size genomic
and textual data, drawing DNA sequences from the GRCh38
human genome and papers from Wikipedia. More recently,
BioReason [422] extends beyond sequence modeling by in-
corporating a dual-channel corpus consisting of PubMed and
Wikipedia texts alongside a large-scale gene-gene interaction
graph built from sources like STRING, Reactome, and Gene
Ontology, enabling joint pretraining across natural language
and biological relational structures.
In transcriptomics, early large-scale pretraining efforts have
focused on gene expression matrices derived from single-cell
RNA sequencing (scRNA-seq) data. Foundation models [513],
[639] are typically trained on datasets including HCA and Tab-
ula Muris, where expression profiles are represented as gene
tokens or gene-expression pairs. Moving beyond unimodal ex-
pression, scMMGPT [640] demonstrates a large-scale dataset
with natural language data, involving over six million single
cells across three modalities: scRNA-seq, scATAC-seq, and
RNA-protein measurements from CITE-seq. RNA-GPT [641]
develops a training corpus with 130,102 full-length transcripts
from the GENCODE v38 reference, boosting the unification
of transcript-level RNA understanding and generation with
language-level reasoning.
In proteomics, UniProtKB (Swiss-Prot and TrEMBL) serves
as the foundational pretraining resource [642]. For example,
ProteinLMDataset [643] is built by SIFTS-mediated mapping
of protein data bank [329] entries to UniProt, integrating bil-
lions of tokens from PubMed abstracts, Swiss-Prot and PMC
full texts; Evolla [510] extracts 14 M expert-curated Informa-
tion Points from Swiss-Prot and clustered TrEMBL entries,
which are then transformed into high-confidence question-
answer pairs via an LLM-driven augmentation pipeline.
Emerging multi-omics corpora begin to unify diverse
biological modalities, integrating sequence-level data with
biomedical text. NatureLM [43] assembles over 3.27 trillion
tokens from 35 biomedical corpora encompassing molecular
sequences, clinical narratives, literature, and imaging-derived
captions. This massive collection incorporates structured omics
repositories such as UniProt, GENCODE, and the Human
Protein Atlas alongside unstructured text from medical corpora
like PubMed, enabling alignment between textual semantics
and molecular features across scales. LLaMA-Gene [40] cu-
rates a multimodal biomedical instruction corpus by align-
ing 6.2 million natural language queries with structured
molecular knowledge graphs derived from GeneCards [644],
OMIM [645], and Ensembl [646]. This results in paired rep-
resentations of gene-level annotations, phenotypes, diseases,
and variant consequences, supporting instruction-tuned pre-
training for gene-centric biomedical reasoning. ChatNT [511]
constructs a fully multimodal instruction dataset comprising
605 million DNA tokens and 273 million English tokens,
covering 27 downstream tasks involving DNA, RNA, and
protein processes. Together, these works exemplify a paradigm
shift toward integrative instruction datasets that fuse omics,
clinical, and textual domains into unified token spaces for
large-scale pretraining.
3) Neuroscience: In the field of neuroscience, pretraining
primarily entails two components: extensive text corpora of
neuroscience literature and modality-specific encoders pre-
trained on brain signals such as EEG, fMRI, and MEG. The lit-
erature corpus, exemplified by the BrainGPT [553] comprises
approximately 1.3 billion words drawn from 332,807 abstracts
and 123,085 full-text articles in the PubMed Central Open
Access Subset, covering 100 high-impact journals (e.g., Na-
ture, Cell, Neuron, PNAS) published between 2002 and 2022.
The LaBraM [647] framework integrates over 2534.78 hours
of EEG data from about 20 public and proprietary datasets,
encompassing motor imagery, emotion recognition, grasp-and-
lift tasks, P300 spelling paradigms, epilepsy detection, and
resting-state recordings, with channel counts of 19-64 and
sampling rates of 160-2048 Hz.
4) Healthcare and Medical Science: Depending on the
model type, pre-training strategies for medical models vary:
LLMs are primarily trained on large-scale clinical and biomed-
ical texts to acquire medical language understanding. However,
when translated to MLLMs, they require another multimodal
pre-training stage that aligns visual and textual modalities to
develop image-grounded understanding. Accordingly, the pre-
training datasets can be broadly categorized into text-only
corpora for LLMs and image-text pairs for MLLMs.
Medical textual data contains essential domain knowledge.
The textual corpora are dominated by conversational clinical
dialogues [42], [521], [648]–[650]. Clinical dialogues cover a
wide range of outpatient scenarios, but their level of expertise
and reliability is difficult to guarantee due to the absence
of follow-up examinations for verification. Medical textbooks
and research papers [204], [521], [590], [651], [652] help
address this issue, serving as critical sources of knowledge in
the medical domain. Electronic Health Records (EHR) [653]–
[656] include basic demographic data, summaries of major
diseases and health issues, and key healthcare service records,
providing longitudinal health information of patients over
time. However, EHR datasets suitable for reasoning over tem-
poral patient trajectories are still scarce. Clinical reports [154],
34

[657]–[660] document the entire patient journey, ranging
from admission and examination to diagnosis, treatment, and
follow-up. However, access to such reports typically requires
strict ethical review and entails potential privacy risks, which
limit their overall availability and scale.
For MLLMs, image-text pre-training datasets play a cen-
tral role. Large-scale corpora such as PMC-OA [205], RO-
COv2 [661], MedICaT [662], and Open-PMC-18M contain
millions of biomedical figures and their associated cap-
tions, largely sourced from academic literature. Datasets
like MIMIC-CXR [154], CheXpertPlus [657], and PMC-
CaseReport [658], on the other hand, provide detailed diagnos-
tic reports with finer-grained information derived from the cor-
responding medical images. These datasets cover a wide range
of modalities, including CT, MRI, X-ray, ultrasound, PET,
endoscopy, and histopathology, offering diverse supervision
signals for learning visual-semantic correspondence. Domain-
specialized image-text corpora also exist to target specific
medical subfields. For example, MM-Retinal [663] focuses
on ophthalmology, while Quilt-1M [151] concentrates on
histopathological imagery with expert-vetted captions. These
datasets serve to refine model understanding in narrowly
scoped visual domains where general medical datasets may
lack coverage.
Beyond static medical images, medical videos also encap-
sulate essential domain knowledge, including educational con-
tent for clinical training, patient simulation [664], surgical pro-
cedures [665], and other clinically relevant scenarios. Models
can learn comprehensive diagnostic and therapeutic knowledge
from such videos. However, there remains a significant gap in
scale between medical videos and medical images.
Despite their scale and variety, existing datasets in the
healthcare and medical sciences domain show a striking
modality imbalance, where medical image data occupies a sig-
nificant position among all datasets, with the majority centered
around radiological imaging. Further, for multimodal pre-
training data, the annotation quality remains variable, ranging
from noisy figure caption to partially validated annotations,
which can affect model reliability.
5) Agriculture: In the agricultural domain, LLMs are gen-
erally pre-trained using corpora compiled from millions of
multilingual agronomy journal articles, tens of thousands of
professional textbooks, and genomic sequence databases. The
construction of such pre-training datasets typically involves a
labor-intensive pipeline including OCR processing, dedupli-
cation, and filtering of low-quality content. Although several
agricultural LLMs have been introduced [547], [551], none of
their domain-specific pre-training datasets have been publicly
released, hindering reproducibility and further research.
C. Astronomy and
Earth Science:
Understanding
Our
Planet
Astronomy and Earth science datasets expand scientific
LLM/MLLM pre-training into domains where spatial, tempo-
ral, and spectral diversity is immense. They provide obser-
vational records, simulation outputs, and literature that span
cosmic scales and Earth’s interconnected physical systems. For
LLMs, pre-training relies heavily on textual resources derived
from research publications, mission archives, and observa-
tional metadata. For MLLMs, multimodal corpora integrate
high-resolution imagery, time-series data, maps, and spectra
with descriptive text, enabling models to connect visual and
quantitative patterns with domain-specific narratives.
1) Astronomy:
Astronomy is among the most data-
intensive scientific fields, yet large-scale, open, and multi-
modal pre-training datasets remain rare. Existing resources
are fragmented across text, image, and spectral modalities,
each with distinct acquisition challenges. While simulation-
heavy domains like physics can generate abundant synthetic
corpora, astronomical data acquisition depends on long-term
sky surveys with large telescopes, such as LAMOST [200]
and Gaia [666], making large-scale datasets costly and slow
to compile. Moreover, observational modalities like images,
spectra, and time-series differ in wavelength coverage, res-
olution, and signal-to-noise ratios, and are stored in hetero-
geneous formats with inconsistent calibration standards. Core
physical parameters (e.g., stellar mass, metallicity) are often
inferred indirectly via modeling rather than directly observed,
limiting the availability of high-quality, labeled examples for
supervised pre-training.
Among existing text-based datasets, resources like NASA
ADS [667] provide extensive corpora of astronomical re-
search papers, abstracts, and technical documents. These
have supported the construction of domain language models
such as AstroBERT [668], trained for semantic understanding
and entity recognition in astronomical contexts. SpecCLIP
model [669] using LAMOST [200] and Gaia XP spectral
data [666], aligns and reconstructs different spectral modalities
through comparative learning. AstroPT [670], an image model
built based on Dark Energy Spectroscopic Instrument Legacy
Survey images, uses an autoregressive generative model to
learn the potential distribution structure of galaxy images.
However, such datasets typically focus on single modalities
with narrow coverage, preventing the formation of a general-
purpose astronomical foundation dataset. At present, text data
remains the most tractable and widely used modality for
pre-training in astronomy, while comprehensive multimodal
datasets that integrate images, spectra, and time series are still
largely absent.
2) Earth Science: Earth science remain less explored in
pretraining dataset construction; most existing corpora in this
field are derived from academic papers, textbooks, and similar
sources. The scarcity is due in part to the dispersed and het-
erogeneous nature of Earth science data. Textual information
is often embedded in PDFs of academic papers and textbooks,
requiring complex parsing, while visual data (e.g., atmospheric
variable fields, remote sensing imagery, and geological cross-
sections) lacks the readily captionable semantic features found
in natural images, making text–image alignment particularly
challenging.
Despite the scarcity of public pretraining datasets, several
approaches to data construction offer valuable insights. For in-
stance, EarthSE [671] leverages approximately 100,000 Earth
science-related academic papers as its corpus. By employing
advanced PDF parsing tools, these papers are converted into
35

text, followed by automated annotation and data cleaning pro-
cesses to produce high-quality datasets. Similarly, studies like
ClimaQA [672] extract structured corpora from Earth science
textbooks. K2 [568], on the other hand, gathers substantial
textual data from internet sources, such as Wikipedia, relevant
to Earth sciences.
Although limited in scale and diversity for pretraining
LLMs, these resources show that scholarly literature and
curated web content remain the primary sources for Earth
science textual data. Moving forward, integrating multi-source
data, improving parsing techniques, and developing algorithms
tailored for aligning Earth science images with text will
advance pretraining dataset development in this field.
D. Pre-training Data Analysis
Across domains, current scientific pre-training corpora show
clear strengths and equally clear gaps.
Throughout the scientific landscape, the dataset ecosystem
is both broad and heterogeneous, spanning text (papers, guide-
lines, EHR), symbolic structures (SMILES strings, CIF, gene
and protein sequences), and multimodal pairings (figures, radi-
ology, microscopy, spectra, videos). This diversity is illustrated
in Fig. 20, which visualizes the relative distributions of pre-
training data modalities (left) and task types (right). As shown,
certain modalities such as academic papers, SMILES strings,
and radiology images dominate, while others remain under-
represented; similarly, task types are heavily skewed toward
raw text and classification. Such uneven coverage underscores
both the breadth and imbalance of current scientific corpora,
leading to several problems:
First, modality imbalance persists: physics remains dom-
inated by idealized simulations [597], [598], which transfer
poorly to noisy, instrument-specific observations, underscor-
ing the simulation-to-observation gap. Second, many MLLM
datasets rely on captions or rule-based labelers, yielding
weakly grounded semantics [205], [661], while even higher-
quality radiology resources still depend on automatic pipelines
that propagate labeling bias [657]. Third, heterogeneity and
poor standardization impede cross-source fusion. For example,
materials repositories (Materials Project [70], NOMAD [620],
OQMD [615]) expose inconsistent metadata and calculation
settings, complicating integrated pre-training and evaluation.
Similar issues appear in astronomy, where multi-instrument
spectra [200], [666], [669] differ in bandpass, resolution, and
calibration, challenging multimodal alignment. Fourth, some
fields lack truly open, large-scale pre-training corpora: Earth
science efforts [568], [671] remain text-centric and modest
in scale, limiting broad generalization. Fifth, data governance
constrains clinical/EHR corpora [673], [674], yielding smaller
or temporally stale distributions relative to real-world care.
Finally, scale–quality trade-offs are unresolved: massive chem-
ical/molecular pools [623], [624] offer breadth but limited
property curation, whereas targeted materials sets emphasize
fidelity at the expense of coverage.
Such uneven landscape gives rise to a fundamental tension:
scientific LLMs/MLLMs require rich, multimodal pretrain-
ing to support domain-aware reasoning, but collecting such
Fig. 20: Word clouds of the pre-training dataset. The plots
show the relative distributions of modalities (left) and types
(right), with word size proportional to frequency.
OCR
27.6%
Language
23.8%
General
33.3%
Counting
8.5%
Code
0.8%
Math
3.2%
Science
2.9%
Cambrian-7M
Fig. 21: Composition of the Cambrian-7M [680] instruction
tuning dataset.
corpora is often expensive and sparse. Therefore, classical
large-scale scaling for training general-domain models, which
throws ever-more tokens and parameters at the problem, is
much less feasible for the development of scientific models.
Efficient pretraining thus emerges as a critical design princi-
ple. Leveraging compute-optimal scaling laws [28], [675] (e.g.,
models should balance parameters and tokens for optimal com-
pute efficiency) offers a roadmap for budget-aware model de-
sign. Techniques such as carefully curated data mixtures [676],
high-quality subset selection [677], and continual pretrain-
ing [678], [679] further promise to stretch domain-limited
scientific resources effectively.
V. SCIENTIFIC DATA FOR POST-TRAINING
Post-training in scientific LLMs/MLLMs aims to align a
pre-trained backbone, which is already equipped with broad
factual knowledge, with the specific problem-solving styles
and interactive workflows of scientific practice. Unlike pre-
training which focuses on coverage and scale, post-training cu-
rates domain-specific, high-quality, and task-oriented datasets
that teach models to solve problems, follow instructions, and
explain their reasoning in ways aligned with disciplinary
norms, moving beyond simple factual memory.
Across the sciences, post-training datasets have evolved
from small, text-only instruction corpora toward large, multi-
modal, and reasoning-rich collections. However, these datasets
vary greatly in sources, size, supervision type, and modality,
reflecting differences in data availability, curation cost, and the
maturity of AI adoption in each domain.
36

Small proportion of scientific data in current multimodal
instruction tuning is exemplified by the Cambrian-7M dataset
[680] (Fig. 21), where science-specific content comprises only
2.9% of the total training corpus, with the majority dominated
by OCR (27.6%), general knowledge, and language tasks.
A. Current Landscape Across Scientific Domains
The details of the post-training datasets are summarized in
Tab. IV.
1) Physics: Physics post-training datasets aim to move be-
yond fact recall toward the procedural and conceptual mastery
that physicists use in practice. The scope spans multi-step
derivation, formula reconstruction, unit consistency checks,
experimental interpretation, and numerical estimation. These
tasks demand both symbolic fluency and the ability to reason
under physical constraints, which are often absent from generic
LLM training corpora.
Existing open resources remain dominated by text-based
QA formats, often adapted from educational or competition
contexts. PIQA [681] captures physical commonsense, includ-
ing tool use and intuitive actions, though it stops short of
formal derivations. SciBench [442] and the physics problems
within the PhysicsArena [682] benchamrk introduce com-
putational questions with numeric computation and formula
application, making them suitable for fine-tuning unit handling
and basic symbolic manipulation. MATH500 [683] is a curated
500-problem subset of the MATH [684] benchmark spanning
seven competition-style mathematics subjects; while it does
not include a physics category, its algebraic and symbolic
problems can help evaluate skills that are often prerequisite
for physics problem solving.
Beyond direct extraction from exams and textbooks, syn-
thetic or semi-synthetic resources increasingly scale coverage.
Nemotron-Science [685] subset contains teacher-generated
reasoning traces across scientific domains including physics;
NaturalReasoning [686] contributes 2.8M challenging ques-
tions with reference answers and is widely used to distill
long CoT from stronger models; and SCP-116K [687] offers
116k automatically extracted problem–solution pairs in higher-
education science (including physics), providing step-wise
solutions without relying on LLM-generated CoT.
Overall, physics post-training datasets today provide a
strong base for short-form problem-solving, with growing
use of synthetic CoT corpora [685], [686] to extend rea-
soning depth. However, most of them are text-only without
figures or symbolic markup, failing to represent the dual
textual-symbolic nature of physics reasoning. Further, post-
training datasets still rarely capture the multimodal richness of
real-world tasks, such as interpreting force diagrams, circuit
schematics, or motion graphs, despite such modalities being
central to the discipline.
2) Chemistry:
Chemistry post-training relies on high-
quality, task-specific datasets to fine-tune models for molecular
property prediction, structure-based reasoning, and genera-
tive chemistry. Unlike pre-training corpora that may contain
millions of weakly labeled compounds, post-training data is
limited in scale due to the high cost of wet-lab experiments
and structural determinations.
For example, drug-discovery ADMET datasets [244] are
often limited to hundreds to thousands of entries because mea-
suring absorption, distribution, metabolism, excretion, and tox-
icity requires time-intensive experiments. The Cross-Docked
dataset [688] contains 22.5M estimated 3D protein-ligand
binding poses generated by molecular docking into multiple
protein binding pockets, providing a large-scale resource for
training and benchmarking structure-based drug discovery
models. PDBBind [689] database stands out as a high-quality,
manually curated resource that extracts experimentally vali-
dated protein-ligand complexes from the Protein Data Bank,
each annotated with quantitatively measured binding affinity
data, supporting both structural analysis and predictive mod-
eling of binding strength.
Chemistry datasets increasingly combine molecular for-
mats (SMILES, InChI, 3D coordinates) with textual anno-
tations [690], allowing LLMs to align symbolic chemistry
representations with natural language descriptions. This multi-
modal pairing is key to enabling cross-format translation, e.g.,
predicting a compound’s IUPAC name from structure or vice
versa.
3) Materials
Science:
Materials
science
post-training
datasets are scarce and often repurposed from pretraining
corpora. Molecular generation benchmarks like MOSES [691]
and ChEBI-20 [692] pair SMILES with text descriptions,
supporting tasks from generation to captioning. ChEBI-20-
MM [693] extends these with richer metadata (InChI, IUPAC,
polar area), enabling cross-format translation. Apart from text
and SMILE modalities, there are visual datasets from high-
resolution characterization resources such as the Warwick
Electron Microscopy Datasets [694], containing tens of thou-
sands of STEM/TEM images and simulated wavefunctions.
These enable image captioning, defect identification, and prop-
erty inference when paired with textual descriptions. How-
ever, such visual data are limited. Most datasets lack multi-
step reasoning traces, multimodal integration, or workflows
that combine molecular design with property calculation and
analysis.
4) Life Sciences: Life sciences post-training data spans
diverse subdomains, each with distinct data modalities, su-
pervision formats, and reasoning demands.
Molecular
and
cell
biology
datasets
include
three
main groups. First, sequence-to-function datasets such as
PEER [695] and BEACON [696] focus on protein and
RNA property prediction. Second, large-scale instruction cor-
pora like Mol-Instructions [697], OPI [698], and PubChem-
STM [628] translate biochemical facts into conversational
form, covering protein, nucleic acid, and small molecule
entities, moving supervised fine-tuning beyond factual recall
toward interactive QA. The third stream, still emerging, in-
volves reasoning-focused datasets that pair each biology QA
with an explicit chain-of-thought, such as ProCoT [699] for
pathway reasoning and ToT-Biology [700] for mechanistic
explanations.
For multi-omics post-training, DNA-focused datasets like
Omni-DNA [636], GeneChat [637], and DNAHLM [638]
frame genomics tasks (e.g., promoter detection, variant in-
terpretation) as instruction-response pairs. RNA post-training
37

includes single-cell and bulk expression modeling, as in
scMM-GPT [640], which aligns scRNA-seq, scATAC-seq,
and CITE-seq modalities with prompts describing biological
contexts. Proteomics leverages UniProt-derived resources such
as ProteinLMDataset [643] and Evolla [510], creating hun-
dreds of thousands to millions of protein-centric QA pairs.
Multi-omics instruction sets like Biology-Instructions [701]
extend post-training to integrated DNA, RNA, and proteins,
typically by synthesizing instruction-response pairs from ref-
erence databases and combining them with curated variant
interpretation and functional annotation tasks.
In healthcare and medicine, post-training data support
a wide range of tasks with the most mature ecosys-
tems: clinical dialogues (MedDialog [702], ChatDoctor [648],
NoteChat [703]) for medical chatbots, medical image re-
port generation (PMC-CaseReport [658], MIMIC-CXR [154],
CheXpertPlus [657]) for structured documentation, mul-
timodal question-answering (EHRXQA [704], PubMedVi-
sion [541], VQA-RAD [705], GMAI-VL-5.5M [542]) for
textual or visual comprehension, with chain-of-thought data
(GMAI-Reasoning-10K [546]) for step-by-step diagnostic rea-
soning on medical images.
Post-training in neuroscience refers to the alignment of
measured neural signals, EEG, MEG, and fMRI, with the
text embedding space of large language models to enable
decoding of related semantics. The experimental tasks fall
into several broad categories, including visual decoding, text
decoding, sleep classification, clinical abnormality detection,
motor imagery, emotion recognition, and workload assess-
ment. In visual decoding, several rich benchmark datasets
have been collected. Things-EEG1 [706] comprises EEG
recordings from 50 participants responding to rapid serial
visual presentation of 22,248 images covering 1,854 object
concepts. Things-EEG2 [707] provides high temporal reso-
lution EEG from 10 subjects over 82,160 image presenta-
tion trials drawn from 16,740 conditions selected from the
THINGS database. The Natural Scenes Dataset (NSD) [708]
contains roughly 213,000 trials from eight subjects viewing
70,566 natural images, with blood oxygen level dependent
responses captured using 7 Tesla fMRI at 1.8 millimeter
resolution. Things-fMRI [709] includes denoised responses
from three participants to 8,740 images representing 720
objects, collected across 12 independent scanning sessions. To
extend visual decoding into the realm of imagined content,
NSD-Imagery [710] offers a benchmark with 2,304 mental
imagery trials collected from NSD, with stimuli spanning
simple shapes, complex natural scenes, and conceptual words.
Complementing the fMRI-based work, Things-MEG [709]
records neural responses from four participants to the same
22,448 images (1,854 objects) with millisecond-level temporal
precision. Neuro-3D [711] constructed the EEG-3D dataset,
which contains EEG signals collected from 12 participants
while they viewed 72 categories of 3D objects (both images
and rotating videos). For text decoding, the ZuCo collections
capture EEG and eye-tracking data during natural reading
and semantic annotation. ZuCo1 [712] recorded data from
12 native English adults reading over 21,000 words in 1,107
sentences across tasks such as sentiment judgment, entity
relation recognition, and extraction of targeted relations like
nationality, occupation, or employer. ZuCo2 [713] refines the
experimental design by gathering EEG and eye movement data
from 18 participants during both free reading and annotation
specific to semantic relations, using 739 English sentences
to better isolate cognitive differences between conditions.
Beyond decoding of visual and linguistic content, other neu-
ral domains contribute complementary signals. Sleep stage
classification is supported by datasets such as HMC [714],
SleepEDF [715], and SHHS [716]. Clinical abnormality de-
tection focuses on disorders such as epilepsy, with datasets
including TUEV [717], TUAB [717], and TUSL [718]. Motor
imagery is studied using the SHU [719] dataset. Emotion
recognition draws on SEED [720] and SEED-IV [721] to
characterize affective states from neural activity. Cognitive
Workload [722] has been probed by collecting EEG from
36 healthy university students engaged in continuous mental
arithmetic through serial subtraction, contrasting resting state
with task periods to reveal neural correlates of load. Together,
these datasets form a diverse and multi-task foundation for
grounding brain activity in language model spaces and de-
coding semantics relevant to perception, cognition, clinical
assessment, and internal mental states.
Agriculture uses domain-specific instruction corpora (e.g.,
CROP [723]) and multimodal VQA datasets (e.g., AgroIn-
struct [552], MIRAGE [191]) to adapt LLMs/MLLMs to crop
health assessment, pest identification, and farm management.
Together, life sciences post-training data covers a broad
modality spectrum from sequences and molecular graphs to
clinical images and neural recordings, requiring models to
unify understanding across vastly different biological scales.
5) Astronomy: Astronomy post-training data has evolved
from pure-text corpora to rich multimodal resources. Early
efforts collected hundreds of thousands of arXiv astronomy
paper abstracts [562], embedding field-specific terminology
and style. Later expansions included texts from introductions
and conclusions [724], as well as LLM-generated QA pairs
from arXiv content, shifting toward interactive tasks.
To support more complex joint vision-language under-
standing tasks, post-training data construction incorporated
multimodality. For instance, AstroLLaVA [563] integrates
NASA’s “Astronomy Picture of the Day” and HST obser-
vation data [352], generating tens of thousands of image-
caption pairs. Additionally, large-scale synthetic pipelines now
leverage arXiv, astronomy Wikipedia, and textbooks to pro-
duce millions of domain-specific question-answer pairs [564],
[567], [725]. For fine-grained tasks, such as named entity
recognition in astronomy literature, manual curation remains
essential, as seen in Astro-NER [726].
These datasets collectively enable models to handle domain
knowledge understanding and multimodal image-text ground-
ing for astronomical observation.
6) Earth Science: Earth science post-training datasets now
span atmospheric, oceanic, terrestrial, and ecological domains.
Early examples like FloodNet [727] paired remote-sensing
images with templated questions. Automated pipelines such
as EarthVQA [728] and TEOChatlas [579] expanded to hun-
dreds of thousands of GIS-derived visual QA pairs. Weath-
38

erQA [729] introduced reasoning over weather composites,
and SeafloorAI [730] scaled to millions of sonar-QA pairs.
Cross-sphere datasets also appeared, like GeoLLaVA-
8K [574], the highest-resolution vision-language datasets in
remote sensing field to date, covering 22 real-world di-
alogue tasks. Supporting corpora like RS5M [731] and
SkyScript [732] offer millions of image-caption pairs across
optical, Synthetic-Aperture Radar, and Infrared (IR) modali-
ties.
With increasingly automated annotation via advanced
MLLMs like GPT-4 or Gemini-Vision, Earth science post-
training data now enables not only scene captioning but also
multi-step reasoning over complex Earth-system interactions.
B. Post-training Data Analysis
Existing post-training datasets share the following patterns
and trends across domains.
First, instruction-based corpora dominate, converting struc-
tured domain knowledge (e.g., databases, ontologies, bench-
mark tasks) into prompt-response pairs. These range from
molecular biology and chemistry’s SMILES-language in-
struction sets [690], [697] to astronomy’s literature-derived
QA [725], and from clinical dialogue datasets [703] to Geo-
graphic Information System (GIS)-to-question pipelines [579]
in Earth science.
Another trend to be noted is the increasing importance
of multimodal and multi-domain corpora. Domains with rich
data modalities (e.g., images), such as healthcare [150], [152],
[154], astronomy [563], and Earth science [574], now build
VQA datasets or image-caption pairs to bridge visual and
textual reasoning. Further, the multi-omics domain in life
sciences typically require analysis across genomics, pro-
teomics, and transcriptomics [40], [43]. In chemistry and
materials science, SMILES strings, 3D molecular coordinates,
microscopy images, and textual descriptions are increasingly
co-annotated. This multimodal shift is crucial for teaching
models to interpret data in heterogeneous forms and perform
fluidly across related scientific subfields. As shown in Fig. 22,
the source distribution of existing post-training corpora for
scientific LLMs/MLLMs reveals significant domain-specific
biases and cross-domain imbalances across different scientific
fields. These skews highlight opportunities for future corpus
building to diversify inputs, reduce training bias, and improve
model generalization across disciplines.
Further, across domains, there is a clear trend toward explicit
reasoning supervision beyond simple QA, driven by the need
for models to handle complex, multi-step decision-making.
However, these reasoning-oriented datasets are unevenly dis-
tributed. Biomedical sciences have begun producing chain-of-
thought datasets for molecular pathways [699], [700] or multi-
step diagnosis [733], [734], even for multimodal tasks [546];
but large-scale, publicly available CoT corpora are relatively
scarce in other domains.
Finally, scalable data synthesis has emerged as a prac-
tical solution to annotation bottlenecks. High-quality litera-
ture corpora, simulation outputs, and curated databases are
now mined by LLMs to produce domain-specific instruction-
response pairs [152], [690], [725] and reasoning traces [544],
C
h
e
m
is
tr
y
A
s
t
r
o
n
o
m
y
P
h
y
s
i
c
s
M
a
t
e
ri
a
l
s
S
ci
e
n
c
e
L
i
f
e
S
c
i
e
n
c
e
s
E
a
rt
h
S
c
i
e
n
c
e
G
e
n
e
r
a
l
S
c
i
e
n
c
e
Academic and research resources
Comprehensive multi-source integration
Encyclopedias and knowledge bases
Integration of existing datasets
Scientific databases
Web and Internet content
Other sources
Books and literary works
Social media and forums
Fig. 22: Source distribution of existing post-training corpora
for scientific LLMs/MLLMs, normalized within each domain,
showing significant domain-specific biases and cross-domain
imbalance. These skews highlight where future corpus building
could diversify inputs to reduce training bias and improve
model generalization across disciplines.
Fig. 23: Word clouds of the post-training dataset. The plots
show the relative distributions of modalities (left) and types
(right), with word size proportional to frequency.
[685] at scale, employing advanced techniques like multi-agent
validation [734] to maintain fidelity, enabling the production of
millions of domain-relevant samples that would be infeasible
to curate manually. As illustrated in the word clouds of Fig.
23, post-training datasets encompass diverse modalities (left)
and types (right), ranging from scientific representations like
SMILES and nucleotide sequences to text-QA, image-text, and
VQA content, reflecting the field’s shift toward multimodal
and integrated approaches.
In combination, these trends mark a shift from narrow, text-
bound, single-domain resources toward broad, richly anno-
tated, and operationally relevant datasets. This evolution posi-
tions post-training not merely as a final polishing step, but as
a critical stage where scientific LLMs acquire the multimodal
fluency, interdisciplinary reasoning, and tool integration skills
necessary for real-world research environments.
39

Despite these advances, significant gaps remain. Datasets
with multi-step reasoning traces tied to real experimental or
computational workflows are still scarce in most domains.
Some of existing CoT datasets [544], [685], [734] are distilled
from existing reasoning models [455], [457] without extensive
expert validation. Moreover, multimodal coverage is uneven:
while medicine, Earth science, and astronomy have rich image-
text corpora, physics still lacks large-scale datasets that pair
problems with diagrams or simulations. Licensing, privacy,
and standardization also hinder dataset reuse, especially in
healthcare and proprietary industrial research.
Future efforts should prioritize integrated multimodal cor-
pora; process-aware datasets with explicit reasoning traces,
experiment design steps, and intermediate analyses; and tool-
grounded examples showing models how to invoke simula-
tions, parse outputs, and iterate on hypotheses. Continuous
post-training pipelines will be needed to keep pace with fast-
evolving scientific data, blending automated ingestion with ex-
pert oversight. Synthetic data generation will remain essential,
but should follow hybrid pipelines that combine automated
scaling with human validation to maintain fidelity.
Ultimately, the goal is to move from LLMs that recall
scientific facts to models that can operate as collaborative
research assistants: reasoning across disciplines, working with
tools, and adapting to new knowledge in real time.
VI. EVALUATION OF SCI-LLMS
The evaluation of Sci-LLMs has increasingly gained atten-
tion as AI-for-Science (AI4Science) becomes integral to con-
temporary research. Recent developments in this area highlight
the critical need for comprehensive assessment frameworks
that evaluate model performance across diverse scientific dis-
ciplines, addressing multiple dimensions such as knowledge
retention, understanding, reasoning, multimodality, and adher-
ence to scientific values. Platforms such as SciHorizon [735]
exemplify this trend, offering holistic benchmarking solutions
that assess both AI-readiness of scientific datasets and fine-
grained capabilities of LLMs across domains. In the following,
we will explore the evolution and current status of scientific
benchmark datasets, outlining their role in driving further
advancements in AI4Science evaluation methodologies.
A. Current Landscape Across Scientific Domains
The evaluation of scientific foundation models across di-
verse disciplines has led to the development of specialized
benchmarks that assess both domain-specific knowledge and
reasoning capabilities. These benchmarks span from funda-
mental physics problems to complex biological systems, each
differing in sources and targeted problems, designed to capture
the unique challenges within their respective fields. The details
of the evaluation datasets are summarized in Tab. V.
1) Physics:
In
physics,
evaluation
benchmarks
have
evolved to test models across educational, competitive, and
research-oriented tasks. At the foundational level, MM-
PhyQA [736] targets high-school physics via multimodal ques-
tions with explicit multi-image chain-of-thought prompting,
while OlympiadBench [737] stresses bilingual, Olympiad-
grade mathematics-and-physics problems with expert step an-
notations. PIQA [681] and PROST [738] earlier emphasized
physical commonsense through multiple-choice plausibility
tasks, establishing a bridge from general commonsense QA
into domain-specific physics.
The progression continues through undergraduate-level
challenges with PhysUniBench [739], PhysReason [740],
and PhysicsArena [682], which systematically probe deeper
physics reasoning through variable identification, process for-
mulation, and solution derivation. UGPhysics [741] expands
this scope by compiling bilingual undergraduate physics re-
sources across mechanics, thermodynamics, and electromag-
netism, while PhyX [742], PHYSICS [743], and SeePhys [744]
integrate text with diagrams and experimental setups to test
multimodal reasoning in diverse physics domains. Comple-
menting these, TPBench [745] introduces advanced theoretical
physics tasks spanning cosmology, relativity, and quantum
mechanics, while PHYBench [746] targets physical percep-
tion more broadly, introducing metrics like Expression Edit
Distance to distinguish genuine reasoning from shortcuts.
Beyond problem-solving, physics benchmarks extend to
equation discovery and symbolic regression. FSReD / AI
Feynman [223] supplies physics-grounded targets for sym-
bolic regression, while SRBench [747] establishes a living
benchmark suite for comparing symbolic regression methods.
LLM-SRBench [748] specifically targets scientific equation
discovery with large language models, carefully designing
problem splits to avoid trivial memorization.
Physical intuition in video is covered by IntPhys 2 [749],
which presents synthetic scenarios requiring models to dis-
tinguish possible from impossible events, MVP-Bench [750]
which constructs minimal video pairs to force true physical
understanding, and MVBench [751] which offers broad tem-
poral multimodal video understanding tasks.
2) Chemistry:
Chemistry
benchmarks
have
similarly
evolved to encompass both knowledge assessment and prac-
tical applications. ChemBench [20] and ChemEval [752] pro-
vide comprehensive coverage of nine and 42 core chemistry
tasks, respectively, while ChemMLLM [201] extends eval-
uation to multimodal chemistry research, including image-
to-image translation for molecule optimization and text-to-
image translation for molecular design. Specialized bench-
marks target specific aspects: ChemSafetyBench [753] focuses
on safety issues of LLM responses in chemical experiments;
TrialBench [754] focuses on clinical trial problems relevant
to drug development, QCBench [755] evaluates quantitative
chemistry problem-solving across seven subfields from ana-
lytical to quantum chemistry, and PMO (practical molecule
optimization) [215] addresses molecular optimization with
23 objectives covering diversity, synthetic accessibility, and
optimization ability. The critical role of spectroscopic data is
captured by SpectrumWorld [756], which introduces 14 multi-
modal tasks spanning over 10 major spectroscopic techniques
and 1.2 million distinct chemical compounds, evaluating mod-
els on spectrum-to-structure reasoning and spectral prediction
from SMILES.
40

3) Materials Science: The intersection of chemistry and
materials leads naturally to materials science benchmarks,
which have evolved from traditional machine learning eval-
uations to LLM-specific assessments. MoleculeNet [219] es-
tablished early standards with over 700,000 compounds for
molecular property prediction, while MatBench [71] intro-
duced specialized tasks for inorganic materials focusing on
electronic structure and mechanical characteristics. Modern
benchmarks like LLM4Mat-Bench [757] advance the field
with 1.9 million crystal structures supporting multiple in-
put modalities, revealing important limitations of general-
purpose LLMs in handling specialized representations like
CIF files. Question answering capabilities are assessed through
MaScQA [109] and MatBookQA [758], which evaluate con-
ceptual understanding and numerical reasoning in materials
science. Generative capabilities are tested by GuacaMol [759]
and MOSES [691] for molecular design tasks, while mul-
timodal understanding is challenged by MMSci [75] and
MaCBench [208], mirroring real-world materials characteri-
zation workflows.
4) Life Sciences: Life sciences present particularly diverse
evaluation challenges spanning molecular biology, healthcare,
agriculture, and neuroscience. At the molecular level, bench-
marks progress from DNA sequence understanding through
DeepSEA [760], Ensembl collections [761], and Genomics-
Long-Range [762] to small-molecule tasks with TOMG-
Bench [763] and MoleculeQA [764]. Higher-level biological
reasoning is assessed by LAB-Bench [765] for wet-lab com-
petence, GeneTuring [766] for genomic knowledge retrieval,
and Genome-Bench [767] for multi-step CRISPR reasoning.
MicroVQA [147] bridges microscopy and molecular function
through expert-verified visual question answering. In video do-
main, SCIVID [768] is a cross-domain scientific video bench-
mark comprising five tasks across animal behavior, medical
imaging, and weather forecasting. It includes diverse modal-
ities (grayscale, RGB, multi-channel meteorological data),
varying temporal scales, and tasks such as classification, point
tracking, and spatiotemporal forecasting.
Healthcare
evaluation
emphasizes
clinical
knowledge
through both text and visual modalities. Text-based bench-
marks include BioASQ [769], PubMedQA [450], and re-
cent comprehensive efforts like MedBench [770], MedX-
pertQA [771], and HealthBench [772] that approach board-
exam rigor. Visual question answering progresses from fo-
cused datasets like VQA-RAD [705], PathVQA [150], and
SLAKE [773] to more comprehensive multimodal assess-
ments in AMOS-MM [156] and RP3D-DiagDS [774]. More
recently, with the rapid progress in Sci-LLMs and scien-
tific agents, some challenging benchmarks have emerged
for evaluating these advanced models. RareBench [775] tar-
gets rare-disease diagnosis, compiling the largest open-source
rare-patient dataset and assessing LLMs across tasks such
as phenotype extraction and differential/disease screening.
MedAgentBench [776] provides a virtual EHR environment
with 100 realistic patients and 300 clinician-authored tasks
across 10 categories to benchmark medical LLM agents.
AgentClinic [777] evaluates multimodal agents by simulating
clinical environments that require history taking, clinical in-
terviewing, and sequential decision making. Agents will need
to use tools and actively gather useful information through
doctor–patient interactions for accurate diagnosis. These suites
push evaluation beyond static QA toward interactive, end-to-
end decision making aligned with real-world practice.
Agricultural
applications
are
evaluated
through
Seed-
Bench [778] for seed breeding capabilities, AgXQA [105]
for extension services, and AgEval [190] for plant stress
phenotyping. Neuroscience assessment combines knowledge-
based evaluation through BrainBench [553] with semantic
decoding tasks spanning visual decoding [706], [707], text
decoding [712], and clinical applications including sleep clas-
sification [714] and emotion recognition [720].
Multi-omics modeling has driven unified benchmark de-
velopment across biological scales. RNA-specific evaluations
have evolved from expression matrix tasks in scBERT [639]
and
scGPT
[513]
to
multimodal
assessments
in
scM-
MGPT [640] and comprehensive QA in RNA-GPT [641]’s
RNA-QA dataset
with
over
400K entries. Cross-modal
integration is exemplified by LLaMA-Gene [40]’s gene-
centric instruction-following, NatureLM [43]’s 50+ biomedical
dataset evaluation, and ChatNT’s 18-task genomics instruction
suite covering processes from RNA degradation to protein
stability.
5) Astronomy: Astronomy benchmarks utilize diverse data
sources, ranging from scientific literature to observational
data. AstroLLaMA [562] and AstroMLab [564], [567], [779]
utilize arXiv’s astro-ph category for training and evaluation,
while specialized tasks include Astro-NER [726] for entity
recognition and Astro-QA [780] for question answering. Ob-
servational data processing is addressed through Starwhisper-
pulsar [781] for pulsar classification, AstroPT [670] for phys-
ical simulation acceleration, and visualization tools like AS-
TROVISBENCH. PAPERCLIP [782] combines text and image
data for literature analysis, while Pathfinder [783] provides
efficient navigation of large-scale astronomical observations.
6) Earth Science:
Earth science benchmarks focus on
atmospheric studies and remote sensing applications. Atmo-
spheric evaluation includes text-based ClimaQA [672] and
ClimateBERT [784], alongside multimodal WeatherQA [729].
Remote sensing benchmarks such as OceanBench [570],
RSIEval [785], and XLRS-Bench [786] emphasize satellite
imagery interpretation through tasks including image caption-
ing, visual question answer and visual grounding in ultra-
high-resolution RS scenarios.. Interdisciplinary efforts like
OmniEarth-Bench [787], EarthSE [671], and MSEarth [153]
integrate data across hydrosphere, biosphere, lithosphere, and
cryosphere, challenging models with complex cross-domain
reasoning.
Across all these scientific domains, evaluation metrics have
evolved beyond simple accuracy to include domain-specific
measures: AUROC (Area Under the Receiver Operating Char-
acteristic curve) and MCC for imbalanced biological data,
exact match and MSE for symbolic regression, Expression
Edit Distance for physical reasoning, validity and synthetic
accessibility for molecular generation, and multimodal metrics
like IoU (Intersection over Union) for visual grounding tasks.
These benchmarks collectively reveal that while foundation
41

Accuracy (%)
Math
Bio/Med
Chemistry
Physics
LLM-as-a-Judge score
Astronomy
Life
Chemistry
Earth
Material
Accuracy (%)
Chemistry
Biology
Health
Physics
Math
Fig. 24: Performance of leading closed-source models drops
significantly on challenging scientific benchmarks (HLE [463],
SFE [444]) compared to MMLU-Pro [81] across multiple
domains. Top to bottom: HLE, SFE (en), MMLU-Pro.
models show promise in scientific applications, significant
gaps remain in handling specialized representations, cross-
modal reasoning, and the integration of domain expertise with
general language understanding.
7) General Science: General-purpose science benchmarks
have coalesced into three major strands: exam-style text QA
that samples broadly across disciplines [81], [788], [789],
multimodal figure/image QA that reflects the visual nature of
scientific communication [80], [605], [790], [791], and special-
ized formats that probe symbolic or programmatic reasoning
beyond free-form answers [748].
Exam-style suites such as MMLU [81], C-Eval [788], and
AGIEval [789] provide wide coverage from secondary to
undergraduate levels in both English and Chinese, enabling
coarse-grained cross-lingual comparisons but often empha-
sizing short multiple-choice formats. Yet, as models satu-
rated these leaderboards, newer variants emphasized robust-
ness, harder distractors, and reasoning-heavy prompts (e.g.,
MMLU-Pro [81]). In parallel, multimodal suites such as
ScienceQA [80] and MMMU [605] advanced beyond text
by combining images, diagrams, tables, and interleaved text;
MMMU-Pro [790] further filters out items answerable by text-
only models and embeds questions in images to enforce gen-
uine visual-linguistic integration, yielding substantially lower
accuracies than on the original set. Graduate-level sets like
GPQA [458] and SuperGPQA [792] target expert-authored,
“Google-proof” scientific reasoning across biology, physics,
and chemistry (and hundreds of graduate disciplines in Su-
perGPQA), helping to expose reasoning gaps that remain
hidden on easier general-purpose tests.
These methodological choices clarify what is being mea-
sured—fact recall, modality integration, or multi-step reason-
ing; they help explain why success on broad academic exams
does not automatically translate to scientific cognition under
stricter evidence conditions. Notably, there is a significant
performance gap between general academic benchmarks and
domain-specific scientific challenges. As shown in Fig. 24,
while leading closed-source models achieve 80-95% accuracy
on MMLU-Pro [81], their performance drops dramatically on
frontier scientific “stress tests” like Humanity’s Last Exam
(HLE) [463] and Scientists’ First Exam (SFE) [444]. Specifi-
cally, most models score only 2-10% on HLE across various
domains, with chemistry showing the best but still poor results.
On SFE, despite relatively better performance in materials
science, accuracy remains low at 20-40% in other scientific
domains. This stark contrast reveals that current LLMs, despite
excelling at general knowledge tasks, struggle significantly
with tasks requiring deep scientific reasoning and domain
expertise.
Consequently, evaluation methodology in general science
is pivoting toward designs that make reasoning requirements
explicit and verifiable. Fixed-choice protocols report accuracy
but implicitly test calibration via distractor design, mak-
ing them sensitive to ambiguity and annotation artifacts;
MMLU-Pro’s ten-option format and curated hard negatives
reduce chance performance and inflate the penalty for shallow
heuristic. MMMU-Pro’s vision-only setting removes textual
crutches, isolating visual understanding from language priors
and better reflecting figure-centric scientific communication.
SFE formalizes multimodal scoring with IoU, BERTScore,
and LLM-as-a-Judge for structured visual tasks, while HLE
introduces calibration error alongside accuracy to quantify
overconfidence on hard scientific questions. Programmatic
tasks like LLM-SRBench [748] enable exact-match and MSE
for equations, and broad suites such as SciEval [793] and
SciKnowEval [443] aggregate multiple task families with
diverse metrics to reflect the varied outputs typical in science.
Together, these evaluations complement broad academic tests
by injecting domain-shaped modalities, harder question de-
sign, and metric pluralism, thereby offering a more faithful
picture of scientific reasoning than can be obtained from
general benchmarks alone.
B. Evaluation Data Analysis
To understand the landscape of scientific evaluation bench-
marks, we first examine the distribution of data sources and
42

C
h
e
m
is
tr
y
A
s
t
r
o
n
o
m
y
P
h
y
s
i
c
s
M
a
t
e
ri
a
l
s
S
ci
e
n
c
e
L
i
f
e
S
c
i
e
n
c
e
s
E
a
rt
h
S
c
i
e
n
c
e
Academic and research resources
Comprehensive multi-source integration
Encyclopedias and knowledge bases
Integration of existing datasets
Scientific databases
Web and Internet content
Other sources
Books and literary works
Social media and forums
Patent databases
Fig. 25: Source distribution of existing evaluation corpora
for scientific LLMs/MLLMs, normalized within each domain.
Most domains rely on a single dominant source type, showing
today’s headline scores often reflect proficiency with one
writing style or data type rather than robust, cross-domain
scientific reasoning, highlighting the need for broader, more
heterogeneous evaluation suites.
benchmark characteristics across domains. Fig. 25 reveals a
striking pattern: most scientific domains rely heavily on a
single dominant source type, with academic and research
resources dominating in Physics and Chemistry, while Life
Sciences shows slightly more diversity. This homogeneity in
source materials raises concerns about the robustness and
generalizability of current evaluation suites, as models may
overfit to specific data types rather than developing broad
scientific reasoning capabilities. Fig. 26 further illustrates
the composition of these benchmarks through word clouds,
where the prevalence of text-based QA formats and specific
modalities like “VQA” and “Text-QA” highlights the current
emphasis on question-answering paradigms, while revealing
gaps in coverage of other important scientific tasks such as
hypothesis generation, experimental design, or cross-domain
reasoning.
These visualization patterns motivate a deeper analysis of
how scientific benchmarks are constructed and what they
actually measure. Across recent benchmarks for evaluating
Sci-LLMs/MLLMs, we observe several patterns.
1) Tiered Regime in Data Generation and Annotation:
Annotation in scientific benchmarks shows a tiered, hybrid
regime: manual expert curation anchors quality in hard do-
mains, semi-automated human-in-the-loop pipelines deliver
scale with control, and fully automated systems enable extreme
throughput where labels can be programmatically derived.
Fig. 26: Word clouds of the scientific benchmarks. The plots
show the relative distributions of modalities (left) and types
(right), with word size proportional to frequency.
Each of them trades off quality, scalability, and resource
requirements.
Manual annotation remains prevalent in specialized sci-
entific domains where expert knowledge is crucial [737],
[769]. For instance, MicroVQA [147] employs 12 human
annotators for microscopy image question-answering, while
OmniEarth-Bench [787] utilizes over 40 annotators to ensure
comprehensive coverage of Earth science domains.
Semi-automated pipelines balance speed and fidelity by
pairing LLM/tooling with expert review: Genome-Bench drafts
with GPT-4 models before human checks [767]; MM-PhyQA
blends ChatGPT and scripts with over eight reviewers [794];
RP3D-DiagDS couples custom crawlers and GPT-4 with spe-
cialist adjudication
[774]. However, recommended practices
(e.g., annotator training, pilot studies, iterative refinement) are
still too rarely documented.
Fully automated pipelines achieves efficient annotation
using established computational frameworks: the Genomics
Long Range benchmark synthesize targets from experimen-
tal/computational protocols [760], [762]; USPTO mines 1.9M
patents programmatically [613]; RSVQA-LRBEN generates
million-scale remote-sensing QAs by rule-based analysis of
satellite imagery
[795]. This maximizes coverage and ef-
ficiency. However, benchmarks that involve LLMs as auto-
annotation tools raise risks of (i) circularity and contamination
when the same or closely related LLMs are later evaluated on
LLM-labeled data, and (ii) propagation of potential inaccura-
cies and biases in LLM-based annotation. Such problems are
even harder to review, because LLMs can produce nuanced,
plausible, yet erroneous answers at scale, which are often diffi-
cult to validate without high-level expertise. This highlights the
need for careful validation even in automated pipelines [746],
[796].
2) Skewed
Knowledge
Level
with
Increasing
Diffi-
culty:
The knowledge level required by the evaluation
datasets, i.e., difficulty, is under-specified and skewed. A
large fraction of recent datasets do not provide informa-
tion about their difficulty entirely, typical in integrated
or web-mined corpora where provenance is diffuse (e.g.,
OmniMedVQA [797], VRSBench [798], SRBench [747]).
Among those that do specify, there is a polarization: high-
stakes or research-level resources tag themselves “Expert”
(e.g., PhysicsArena [682], LLM4MatBench [757], RP3D-
DiagDS [774], MedXpertQA [771]) while exam/education-
style benchmarks cluster at “Undergraduate” (e.g., UG-
Physics [741]; PHYSICS [743], MEDIQA-AnS [799]) with
43

very few “Intermediate” slices to chart capability boundaries
across a continuum [107]. Cross-sectioning by release date
suggests the skew is increasing: 2024–2025 saw a wave
of expert-labeled clinical and science sets (MedXpertQA
2025.01; PhysicsArena 2025.05) alongside new Undergraduate
exam corpora (UGPhysics 2025.01; PHYSICS 2025.03).
These expert-level benchmarks demand not only deep do-
main knowledge but also the ability to synthesize information
from and reason on multimodal and cross-domain cues. Med-
ical benchmarks particularly exemplify this with requirements
of complex reasoning on rare diseases [775] and dubious
cases [772]. Questions in these benchmarks are typically
designed to be “Google-proof” [458] and entangled, requiring
genuine understanding and multi-step thinking [740] rather
than simple memorization, setting a particularly high bar for
model evaluation. The emergence of expert-level benchmarks
could be attributed to the need for testing the limits of capabil-
ity of frontier LLMs, and also reflects growing recognition that
scientific reasoning requires not just factual knowledge but the
ability to apply, analyze, and create new understanding [800].
3) Shift towards Domain-Specific Metrics: In terms of
evaluation methods and metrics, question-answering form is
the prevailing evaluation, but the metrics are evolving from
simple accuracy measurements to sophisticated multi-faceted,
domain-specific assessment frameworks, reflecting the hetero-
geneity of scientific problems.
Scientific benchmark datasets designed for modern Sci-
LLMs
typically
focus
on
closed-ended
questions
(e.g.,
multiple-choice questions, “True/False” problems), where the
exact answers can be easily extracted from the outputs of Sci-
LLMs using regular expressions; the dominant evaluation met-
rics are simple and objective: exact match and accuracy. Such
a single universal score, however, provides limited insights on
the capability of Sci-LLMs, and is difficult to employ in open-
ended questions. Benchmarks that require natural language
generation frequently adopt n-gram overlap (BLEU/ROUGE)
to compare free-form outputs against references [150], [799].
However, these surface-form metrics do not consider semantic
correctness. BERTscore [801], as employed in some bench-
marks [153], [802], mitigates this problem by comparing the
embedding similarity between Sci-LLM’s responses and gold
answers, yet the semantic similarity still does not guarantee
factual correctness and underweights negation and nuanced
meanings.
Domain-anchored measures are strongest where the sci-
ence supplies mature targets: in genomics and multi-omics,
AUROC/AUPRC are standard for association and retrieval
(e.g., DISEASES [803], repoDB [804]), while regression
tasks [805] adopt R2, RMSE, or Pearson’s correlation coef-
ficients (PCC) to quantify effect-size prediction rather than
linguistic plausibility. Chemistry emphasizes chemical validity
and drug-likeness for molecular generation, rightly scoring
whether molecules are synthesizable and pharmacologically
plausible [216], [217]. Physics benchmarks illustrate metric
specialization along two axes: exact string/structure match for
symbolic regression [223], [747], which verifies whether a
discovered closed-form is the same function, and step-wise
or explanation-sensitive grading [746] that penalizes reasoning
drift even when final answers coincide.
The merit of this trend is clear: metrics are increasingly
aligned with the scientific target, enabling faithful model
selection and revealing failure modes that generic QA accuracy
would hide. But there are risks. First, narrow metrics can be
gamed (e.g., maximizing BLEU without factual grounding,
or optimizing AUROC under pathological class priors). Also,
portfolios are inconsistent across datasets, impeding cross-
domain comparison. Furthermore, many QA/VQA sets still
rely on overlap-based or single-number accuracy for open-
ended tasks, under-measuring calibration, citation faithfulness,
and harm [772]. Looking forward, future scientific benchmark-
ing should (i) pair task-native objectives with calibration and
uncertainty reporting (e.g., ECE/Brier alongside AUROC for
DISEASES [803]); (ii) add process-aware scoring that evalu-
ates intermediate steps and evidence use [746]; (iii) incorporate
reference-grounded factuality/citation checks for text outputs
so a model must justify answers beyond n-grams [150], [799];
and (iv) standardize multi-metric dashboards per domain to
avoid metric gaming and improve comparability across re-
leases [786], [798], [806].
C. LLM / Agent as a Judge
With the rapid advancements in LLMs and multimodal
generative models, traditional evaluation methods, which often
rely on a single numerical score (e.g., accuracy) or require
extensive manual labor, have become inadequate. To address
this challenge, an emerging trend is to use agentic systems
to evaluate other agents or models. This “Agent-as-a-Judge”
paradigm is a natural extension of “LLM-as-a-Judge” [807]
and provides richer, more reliable evaluations by incorporat-
ing agentic features like dynamic planning and intermediate
feedback (Fig. 27).
The primary advantages of the “Agent-as-a-Judge” frame-
work are its flexibility, efficiency, and explainability. It typ-
ically employs a multi-round, dynamically adjusting evalu-
ation process that mimics the strategies of human experts.
During this process, the agent judge can dynamically adapt
its evaluation direction and test cases based on intermediate
results and observed feedback. This approach moves away
from a reliance on fixed benchmarks and large sample sizes,
significantly reducing the time and computational cost required
for evaluation.
For instance, in code generation [808], the agent judge
can evaluate a developer agent’s performance on multi-step
tasks, not just the final outcome. In the domain of visual
generation [809], an evaluation agent can conduct multi-round
assessments based on an open-ended user query, ultimately
providing a detailed natural language analysis and summary
rather than just a simple numerical score. This provides
deeper insights into a model’s strengths and weaknesses. In
the hypothesis generation task [810], [811], a judge agent
evaluates the novelty, validity, and coverage of key points
in the proposed hypotheses, which is well-suited to their
inherently flexible and open-ended nature.
This trend has profound implications for future evaluation
in the scientific domain, particularly for automated scientific
44

Exact match
Semantic similarity
LLM-as-a-judge
Agent-as-a-judge
Question
Question
Question
Question
Options
A. ...
B. ...
Sci-LLM
Output
answer
Ref.
answer
“Right” / “Wrong”
Sci-LLM
Output
answer
Ref.
answer
Similarity
Sci-LLM
Tools
Search
Output report
Judge LLM
Assessment
Exp. environment
Code
Scientific
data
File
...
Sci-agent
Sci-agent
Evolving Evaluation
Evolving Output
Closed-ended answer
Open-ended answer
Reasoning report
Scientific discovery
Assessment
Exp. environment
Judge agent
Language encoder
(e.g., BERT)
Fig. 27: The evolution of evaluation methods for LLMs, starting from simple “Right or wrong” exact matches and progressing
to semantic similarity comparisons for open-ended answers with metrics like BERT-Score [801]. More advanced methods
include using an LLM as a judge to generate reasoning reports, culminating in the use of multiple agents and tools within an
experimental environment for scientific discovery to provide a comprehensive model assessment.
discovery. Automated scientific discovery often involves com-
plex, multi-step tasks where the outcome cannot be easily
quantified with a single metric. Traditional evaluation methods
are ineffective at capturing the intermediate processes and pin-
pointing failures within these tasks. The ”Agent-as-a-Judge”
framework addresses this by providing rich intermediate feed-
back and a comprehensive analysis of the entire process.
D. Inspiration from Test-Time Learning
Test-Time Learning (TTL) is gaining significant traction in
the natural sciences due to its unique value proposition. First,
scientific benchmark evaluation inherently involves working
with test sets that lack ground-truth answers, which perfectly
fits TTL’s paradigm of adaptation at inference time without
requiring labeled data [812]. On the other hand, datasets in the
natural sciences exhibit strong heterogeneity and distribution
shift. For example, Earth sciences encompass atmospheric,
oceanic, remote sensing imagery, and textbook text, with
large differences in data structure and semantics within each
subdomain. Conventional, statically pretrained LLMs often un-
derperform when confronted with data distributions markedly
different from their training corpus, whereas TTL enables
immediate adaptation by dynamically updating parameters or
reasoning strategies using currently observed, unlabeled test
samples.
TTL’s practical application in the natural sciences manifests
in several technical pathways. MedAdapter [813] employs
post-hoc adapters for TTL in biomedical applications. Across
four biomedical reasoning tasks and eight datasets, the per-
formance of white-box LLMs improved by 18.24%, while the
performance of black-box LLMs improved by 10.96%. In the
field of chemistry, [814] proposes scaling test-time training
with reinforcement learning for chemical language models to
improve chemical space exploration on their proposed bench-
mark, MolExp, which focuses on discovering structurally
diverse molecules with similar bioactivity. Evaluation results
on MolExp reveal that extending increasing the TTL will
improve model performance, but the performance gains will
diminish if the TTL time is too long. In theoretical physics,
Gao et al. [815] proposed a symbolic weak-verifier framework
in TTL to enhance performance on the TPBench [745] physics
dataset.
VII. SCIENTIFIC DATA DEVELOPMENT
This section examines how scientific data influences model
development across various stages including data collection,
training, and evaluation, highlighting systemic limitations and
emerging opportunities. We begin by analyzing the methodolo-
gies in scientific data construction (Sec. VII-A), and then point
out critical limitations of current datasets (Sec. VII-B). Finally,
we identify deeper structural issues that hinder the usability
of scientific data for LLM development (Sec. VII-C).
A. Data Collection and Labeling
The development of Sci-LLMs fundamentally depends on
the quality of their training data; our analysis of existing
datasets reveals a complex landscape of acquisition and an-
notation practices that vary across domains, reflecting both
the heterogeneous nature of scientific knowledge and the
practical constraints of dataset construction. This subsection
discusses three aspects that outline the key factors shaping how
scientific datasets are constructed and curated for LLM devel-
opment, including: (i) data source heterogeneity and acquisi-
tion strategies (Sec. VII-A1), which describe the diversity of
45

1. Data Acquisition
Web & Internet
Literary Works 
& Book
Academic
Resources
Social Media
Scientific 
Databases
Patent
Open-source 
Datasets
Multi-source 
/ Others
3. Data Review
Domain-specific  
instruction data synthesis
QA, CoT, 
alignment, ...
Scientific text 
synthesis
Closed-ended QA, open-
ended QA, multi-hop, ...
Data 
deduplication
Data 
filtering
Data 
selection
Data 
mixing
Domain
filtering
Quality
filtering
Domain-specific
augmentation
Structural
templating
Task 
design
Question
definition
Answer 
curation
Quality 
control
Fidelity 
Diversity 
Accuracy 
Safety 
Privacy
Post-
training
Evalua-
tion
2. Data Synthesis Pipelines
Text, sequence, 
symbol, code, ...
Pre-
training
Verified & validated 
QA synthesis
Intrinsic Evaluation
Extrinsic Validation
Human-in-the-Loop
Fig. 28: Scientific data construction pipeline: multi-source data acquisition, data synthesis pipelines for pre-training, post-
training and evaluation stages, and comprehensive review framework incorporating intrinsic evaluation, extrinsic validation and
human-in-the-loop feedback with five quality criteria (safety, fidelity, accuracy, diversity, privacy).
infrastructures and repositories that supply scientific data; (ii)
annotation methodologies and quality control (Sec. VII-A2),
which address the pipelines and validation processes used to
ensure data reliability; and (iii) cross-domain patterns and
domain-specific considerations (Sec. VII-A3), which highlight
recurring challenges such as bias, ethical constraints, and
disciplinary practices.
1) Data Source Heterogeneity and Acquisition Strategies:
The scientific data ecosystem exhibits remarkable diversity in
its sources, with each domain developing distinct acquisition
strategies tailored to its knowledge infrastructure. Academic
and research resources constitute the primary foundation
(Figs. 22 and 25), accounting for the majority of datasets
across all disciplines. In life sciences, repositories like PubMed
Central and specialized databases such as MIMIC-CXR [154]
provide structured access to millions of medical images and
clinical reports. The astronomy domain leverages arXiv ex-
tensively, with datasets like AstroLLaMA [562] utilizing over
300,000 abstracts, while materials science relies heavily on
computational databases like the Materials Project and exper-
imental repositories such as USPTO [613] patents.
This reliance on established scientific infrastructure presents
both advantages and limitations. While peer-reviewed sources
ensure data quality and scientific validity, they introduce
significant temporal delays—publications typically lag behind
actual discoveries by months or years, creating what the paper
identifies as a ”data latency” problem. Moreover, the domi-
nance of English-language sources creates linguistic bias, with
Chinese-language datasets primarily confined to healthcare
applications like CMB-Exam [816] and agricultural resources
like CROP, despite substantial scientific contributions from
non-English speaking regions.
Web-scraped content emerges as a secondary but increas-
ingly important source, particularly for multimodal data. Re-
mote sensing datasets like RS5M [731] aggregate millions of
satellite images from online repositories, while medical edu-
cation platforms contribute to datasets like MedDialog [702].
However, the quality and reliability of web-sourced data vary
considerably, necessitating sophisticated filtering mechanisms.
Patent databases represent a unique intersection of scientific
and commercial knowledge, particularly valuable in chemistry
and materials science, where USPTO provides access to nearly
2 million chemical reactions with detailed experimental pro-
cedures often absent from academic publications.
2) Annotation Methodologies and Quality Control: The
scientific data synthesis employs a sophisticated multi-track
pipeline architecture designed to address the distinct require-
ments of pre-training, post-training, and evaluation phases
(Fig. 28). The pre-training synthesis pipeline begins with data
deduplication to eliminate redundancy across heterogeneous
sources, followed by quality-based filtering that removes low-
value content. Selected data undergoes strategic mixing to
ensure balanced representation across scientific domains, cre-
ating a diverse foundation for initial model training. This rel-
atively straightforward process prioritizes scale and coverage
over precision, establishing broad scientific knowledge bases.
In contrast, the post-training synthesis pipeline imple-
ments more stringent quality controls tailored for instruction-
following capabilities. Domain-specific filters first categorize
content by scientific subdisciplines, after which quality filters
apply elevated standards including factual verification and ci-
tation validation. The pipeline then enhances underrepresented
domains through targeted synthesis and implements structural
templates to standardize instruction-response formats. This
refined approach ensures that post-training data not only main-
tains scientific accuracy but also follows consistent patterns
that facilitate effective fine-tuning.
The evaluation data synthesis pipeline represents the most
rigorous track, beginning with careful task design that spans
multiple cognitive levels from basic factual recall to com-
plex multi-step reasoning. Question creation generates di-
verse query types including multiple-choice questions with
scientifically plausible distractors, open-ended problems re-
quiring detailed explanations, and multi-hop challenges that
46

test reasoning capabilities. Each answer undergoes meticulous
construction with step-by-step derivations and comprehensive
explanations, followed by multi-round quality assurance to
validate both scientific accuracy and logical coherence.
These pipelines produce three distinct categories of syn-
thesized data. Instruction-response pairs encompass sequence-
based formats for procedural knowledge, symbol-based repre-
sentations for mathematical and chemical notations, and code
implementations for computational tasks. Knowledge and QA
pairs include both alignment data for factual grounding and
chain-of-thought examples that demonstrate explicit reasoning
processes. Open-ended QA pairs, primarily used for eval-
uation, feature both multiple-choice questions and complex
problems requiring detailed explanations.
The synthesized evaluation data undergoes comprehen-
sive human-in-the-loop review across six critical dimensions.
Safety checks ensure no harmful scientific misinformation,
while accuracy validation verifies factual correctness against
authoritative sources. Diversity assessment confirms broad
coverage across subdomains and question types, and fidelity
review maintains consistency with established scientific prin-
ciples. Privacy screening removes any personally identifiable
information, and throughout this process, domain experts
provide iterative feedback to refine data quality. This rigorous
validation framework proves essential for evaluation datasets,
as they serve as definitive benchmarks for assessing model
capabilities in scientific reasoning and knowledge application.
3) Cross-Domain Patterns and Domain-Specific Consid-
erations: Despite domain-specific variations, several patterns
emerge across scientific data collection efforts. The transition
from individual datasets to integrated ecosystems characterizes
modern approaches, with initiatives like GMAI-VL [542]
in healthcare aggregating 5.5 million multimodal examples
across institutions. This consolidation addresses fragmentation
but introduces new challenges in maintaining provenance and
ensuring consistent quality standards across heterogeneous
sources.
Domain expertise requirements create natural barriers to
cross-disciplinary data sharing. Medical datasets require un-
derstanding of clinical workflows and regulatory constraints,
while astronomical data demands familiarity with coordinate
systems and instrumental calibrations. Agriculture occupies a
unique position, requiring integration of biological knowledge
with environmental monitoring, resulting in datasets like MI-
RAGE [191] that combine expert agricultural consultations
with field imagery.
There is a concerning trend toward annotation convenience
rather than scientific completeness. Datasets often reflect what
is easily accessible rather than what is scientifically impor-
tant—published positive results dominate while negative find-
ings remain largely absent. This bias extends to experimental
conditions, with datasets capturing idealized scenarios rather
than the messy reality of scientific practice. Materials science
datasets focus on computationally generated structures while
experimental synthesis failures go unrecorded, creating an
incomplete picture of the scientific process.
Privacy and ethical considerations impose additional con-
straints, particularly in life sciences. While physics and as-
tronomy data are generally open, medical datasets require
extensive de-identification and access controls. This creates
a fundamental tension between data availability and patient
protection, resulting in geographic and demographic biases
as datasets predominantly originate from well-resourced in-
stitutions in developed countries. Agricultural datasets face
similar challenges with proprietary farming data, limiting the
diversity of crop varieties and growing conditions represented
in publicly available resources.
B. Limitations of Current Scientific Datasets
Despite rapid growth in scientific corpora, current datasets
exhibit significant limitations in scope, granularity, and modal-
ity coverage. This subsection characterizes fundamental chal-
lenges that constrain the training and evaluation of Sci-LLMs,
including: (i) the scarcity of experimental data (Sec. VII-B1),
which arises from the high cost of data acquisition and
the rarity of scientific phenomena; (ii) the over-reliance on
text modality data (Sec. VII-B2), which limits multimodal
reasoning and reduces empirical grounding; (iii) the represen-
tation gap between static knowledge and dynamic processes
(Sec. VII-B3), showing how current datasets fail to capture the
evolving nature of scientific inquiry; and finally, (iv) the multi-
level biases (Sec. VII-B4) that stem from publication practices,
language dominance, and domain skew, all of which impact
the fairness and generalizability of Sci-LLMs.
1) Scarcity of Experimental Data: The scarcity of experi-
mental data in scientific domains stems from several inherent
characteristics of scientific data. These factors collectively
hinder the development of data-intensive scientific LLMs and
MLLMs. The first characteristic is the high acquisition cost in
experimental data generation. Scientific experimentation is of-
ten extraordinarily expensive and time-consuming. Experimen-
tal research frequently faces significant financial constraints
that cause sufficient experiments to yield statistically reliable
results. For instance, in drug discovery, obtaining accurate
protein structures is essential for understanding molecular
interactions, but it requires costly wet-lab experiments and
specialized equipment like cryo-electron microscopes, X-ray
crystallography. Similarly, generating high-fidelity simulation
data [385], [403], [597], which can serve as a proxy for exper-
imental data in scientific machine learning, typically demands
substantial computational resources and long processing time
to generate datasets of adequate size. This inherent financial
and temporal burden directly restricts the scale and diversity
of experimental datasets. The traditional pace of scientific
investigation, constrained by these resource limitations, often
struggles to match the data demands of modern AI models,
creating a fundamental bottleneck. In healthcare, access to
clinical data usually requires rigorous ethical review and
carries privacy risks, constraining their widespread availability
and scalability. Another inherent unique challenge causing the
data scarcity is the rarity of specific scientific phenomena.
Unlike other forms of scarcity that might be mitigated through
increased resources or improved collection methods, this type
of scarcity is intrinsic to the natural world or specific ex-
perimental conditions. For example, in healthcare, research
47

into rare diseases is perpetually hampered by the limited
availability of patient data, directly impeding the development
of effective treatments and diagnostic tools. This means that AI
models designed for these domains must be capable of learning
effectively from extremely limited examples, as the underlying
phenomena themselves are inherently infrequent. The lack
of AI-ready experimental data is another key challenge in
building effective scientific LLM models. Experimental data in
the natural sciences suffer from heterogeneity and the lack of
standardization [817], as they come from diverse instruments,
protocols, and domains, each with its own formats, units, and
conventions. Without community-adopted standards for data
schemas and metadata fields, integrating datasets across labs
or domains becomes a labor-intensive and error-prone task.
As a result, crucial contextual information (e.g., experimental
conditions, calibration details) are often omitted or encoded in-
consistently, forcing AI practitioners to spend disproportionate
effort on data preprocessing rather than model development.
2) Over-reliance on Text Modality Data: Current scientific
corpora for LLMs and MLLMs rely heavily on published
articles, patents, and reviews, which are rich in descriptive
content but poor in raw experimental detail [30], [41], [453],
[454]. This over-reliance on the text modality introduces
several issues. First, scientific datasets tend to prioritize aggre-
gated summaries over raw measurements, leading to limited
quantitative depth. Textual reports often present averaged
results without revealing underlying data distributions. Con-
sequently, models are never exposed to the full variability
of experimental outcomes, limiting their capacity to reason
about uncertainty or discern fine-grained trends. Second, text-
based scientific literature often exhibits selection and reporting
bias. Authors typically highlight statistically significant or
positive findings, while omitting negative results or method-
ological failures. This causes a skewed perception of science
as a linear and uniformly successful process. Beyond textual
limitations, current scientific datasets suffer from a scarcity
of structured experimental data, as detailed in Sec. VII-B1.
Machine-readable protocols, equipment settings, and raw time-
series measurements are rarely shared in standardized for-
mats [338], [818]. Without detailed reagent tables, step-by-
step procedures, or high-resolution simulation outputs, models
cannot infer the precise cause-effect relationships that drive
scientific discovery. Moreover, many key scientific modalities
are either excluded or available only as low-resolution figures
embedded in PDFs. These include spectra, microscopy im-
ages, chromatography traces, and raw sensor streams. Without
high-quality multimodal signals, MLLMs lack the empirical
grounding to connect textual hypotheses with experimental
evidence. Overall, the imbalance between descriptive text and
scientific modality data severely limits a model’s ability to
generalize from narrative summaries to the rigorous, data-
driven reasoning required in cutting-edge research. Bridging
this gap will require more complete, structured, and multi-
modal experimental datasets.
3) Representation Gap between Static Knowledge and
Dynamic Processes: Scientific datasets usually provide static
snapshots of knowledge at the time of collection, which
fails to reflect the continuously evolving nature of scientific
discovery. In contrast, scientific progress is a iterative cycle of
formulating hypotheses, testing them against emerging data,
and refining through continuous experimentation and analysis.
This mismatch between static data and the dynamic research
process creates a significant representation gap: models trained
on these one-off datasets struggle to make reliable predictions
or conduct meaningful reasoning about evolving phenomena.
The gap is particularly pronounced in observational records,
experimental results, and scientific QA benchmarks that often
rely on predetermined question–answer pairs from published
sources. The static nature of these collections leads to “knowl-
edge expiration” as new findings emerge, thereby undermining
their relevance and validity. As facts change, models trained
on these snapshots may yield outdated or even contradictory
conclusions, which impedes their utility for real-time reason-
ing and hypothesis generation that requires up-to-date evidence
and iterative feedback.
4) Multi-level Biases in Scientific Datasets:
Scientific
datasets contain systematic biases that embed skewed per-
spectives into the training of LLMs. These biases arise when
data deviates from a comprehensive scientific reality, includ-
ing publication bias, domain bias, author and institutional
biases. Understanding these biases is the crucial step toward
building fairer and more accurate AI models. Publication bias
leads to an overabundance of positive results, as studies with
statistically significant findings are up to three times more
likely to be published than those with null results
[819].
This dismissal of negative or inconclusive data distorts the
available evidence. Language bias reinforces the dominance
of English, as English-language publications make up the
vast majority of accessible scientific literature [820]. This
causes models to misrepresent or underperform on scientific
work from other languages and cultural contexts. Pervasive
domain bias exists in repositories such as PubMed, which
disproportionately focus on the life sciences and biomedicine,
while underrepresenting disciplines like physics, chemistry,
and social sciences. This impairs the ability of LLMs to
generalize across scientific domains. Finally, author and in-
stitutional biases emerge when a small number of prolific
researchers or elite institutions contribute disproportionately.
This phenomenon imprints specific writing styles and thematic
focuses, causing models to mirror dominant voices rather than
reflect the full diversity of scientific discourse. Addressing
these systematic biases through corpus diversification, targeted
augmentation of underrepresented domains, and bias-aware
sampling is essential for building fairer and more reliable
scientific LLMs.
C. Systematic Issues in Data Quality
Beyond surface-level limitations, the scientific data ecosys-
tem suffers from systemic issues that undermine the data-
driven scientific AI. This subsection highlights three critical
areas that must be addressed to support robust Sci-LLM
development. First, we describe the data traceability crisis
(Sec. VII-C1), where missing provenance and undocumented
preprocessing hinder reproducibility and trust. Next, we ex-
plore scientific data latency (Sec. VII-C2), which delays the in-
corporation of recent discoveries into model training and limits
48

real-time scientific reasoning. Finally, we focus on the lack of
AI-readiness (Sec. VII-C3), emphasizing how poor formatting,
missing metadata, and domain-specific heterogeneity prevent
many datasets from being directly used in LLM pipelines.
These structural deficiencies highlight the need for end-to-
end redesign of scientific data practices, enabling continuous,
traceable, and AI-compatible knowledge integration.
1) Data Traceability Crisis: The scientific data traceability
crisis in building LLMs and MLLMs for various science do-
mains poses a significant challenge to the integrity and utility
of AI-driven scientific discovery. The data traceability crisis
stems from inconsistent, incomplete, and often undocumented
management of the diverse scientific datasets used to train
these complex models. The metadata of scientific datasets de-
scribing sample provenance, processing details and versioning
information are often sparse or missing. Fundamentally, this
deficiency in transparency and auditability may undermine
scientific rigor and reproducibility. Subsequent researchers
struggle to reconstruct how scientific data are generated
and transformed. It exacerbates existing problems such as
bias propagation, introduces considerable legal and ethical
liabilities, and complicates the crucial process of validating
AI-generated scientific hypotheses. Also, there is increasing
difficulty in distinguishing synthetic from real experimental
data. Recent analyses show systematic under-utilization of
roughly three-quarters of online data repositories, largely due
to insufficient data traceability [821]. The cumulative effect
could diminish the trust in AI systems, particularly within
high-stakes scientific applications ranging from novel drug
discovery to precise medical diagnostics. Addressing this
issue necessitates a comprehensive strategy that integrates
advanced technological solutions with robust data governance
frameworks, clear regulatory guidelines, and a sustained com-
mitment to fostering greater transparency and accountability
throughout the AI development lifecycle.
2) Scientific Data Latency: Scientific data latency refers
to the delay between when new experimental results, publica-
tions, or datasets are generated and when they become avail-
able for a scientific LLM to ingest. This latency issue under-
mines model accuracy, reliability, and relevance, particularly in
fast-evolving fields such as biomedicine, climate science, and
materials science, where new discoveries can quickly render
older information obsolete. The data latency issue arises from
several aspects. First, many scientific findings appear only after
lengthy peer-review and publication processes with datasets
remain inaccessible, delaying their inclusion in model training.
Second, even publicly released data often lack standardized
metadata or real-time update mechanisms, causing models
to train on out-of-date versions of datasets. Third, high-
throughput instruments and simulation platforms can produce
terabytes of data daily, but bandwidth constraints, quality-
control pipelines, and manual curation introduce additional
lags before data are transformed into machine-readable for-
mats. As a result, scientific AI models may perpetuate outdated
knowledge, overlook the latest experimental protocols or dis-
coveries, leading to increased risk of hallucination when faced
with unfamiliar recent developments. Addressing data latency
requires the adoption of open-access policies and development
metadata standards to enable automatic updates to training
corpora.
3) The Lack of AI-readiness:
In the era of scientific
AI, scientific data needs to be readily consumable by AI
models, seamlessly integrating into their training and infer-
ence processes to support automated and scalable scientific
discovery. Despite their immense potential, many scientific
datasets are underutilized due to their lack of AI-readiness,
posing significant challenges for scientific LLM development.
This incompatibility issue stems from incomplete essential
metadata, insufficient preprocessing, mismatched structures,
and the inherent complexities of diverse scientific information,
making direct utilization for model training difficult. Such
limitations impede immediate usability, forcing researchers to
invest substantial effort in data adaptation rather than accelerat-
ing LLM-driven scientific discovery. The majority of published
scientific data require extensive preprocessing, curation and
enrichment before they become AI-ready, significantly slowing
down progress in building domain-specialized LLMs and other
data-driven scientific tools. To bridge this gap, the scientific
community must shift from simply making data available to
ensuring it is truly actionable.
VIII. NEW PARADIGMS FOR DATA-DRIVEN SCI-LLMS
New paradigms are emerging that reimagines Sci-LLMs not
just as passive predictors but as active, goal-directed systems,
i.e., agents, capable of autonomy, interactivity, and orches-
tration across tools and tasks [822]. This section explores
two major shifts shaping the future of Sci-LLMs. First, we
examine the emergence of scientific agents (Sec. VIII-A),
which transform Sci-LLMs into autonomous entities that em-
phasize planning, experimenting, and self-improving. Then,
we analyze how data ecosystems for Sci-LLMs must be
redesigned to support these agents (Sec. VIII-B).
A. Scientific Agent
A key paradigm shift is treating LLMs as scientific
agents that can plan and execute research tasks with a
degree of autonomy. This subsection introduces key devel-
opments in this direction, beginning with a brief introduc-
tion on the transition from Sci-LLMs to scientific agents
(Sec. VIII-A1), followed by the concept of multi-agent col-
laboration (Sec.VIII-A2). Next, we explore the integration
of external tools (Sec. VIII-A3), which enable agents to
interact with databases, software, and real-world systems. We
also discuss self-evolving agents (Sec. VIII-A4) that refine
their skills, prompts, and tool usage through iterative feed-
back. Then, we highlight emerging evaluation frameworks and
benchmarks (Sec. VIII-A5) that rigorously assess agents on
end-to-end workflows, collaboration, and safety in scientific
tasks. Finally, we introduce the application of scientific agents
on autonomous scientific discovery (Sec. VIII-A5).
1) LLMs
as
Scientific
Agents:
Rather
than
simple
question-answering, a scientific LLM agent is given high-level
goals (e.g., “discover potential drug candidates for disease X”)
and autonomously decomposes the task, gathers information,
performs experiments (virtually), and synthesizes results [823].
49

These agents maintain structured, hypothesis-driven work-
flows that echo the scientific method: defining hypotheses,
selecting experimental methods, and validating results before
drawing conclusions. Crucially, they emphasize reproducibility
and scientific rigor, incorporating domain-specific constraints
and verification steps that generic AI assistants often lack.
Studies have highlighted that accelerating discovery requires
capabilities beyond generic chatbots – for instance, generating
novel hypotheses, designing and running experiments, and
interpreting complex data in context [18], [44]. By building
these capabilities, LLM-based scientific agents aim to serve as
AI co-researchers that can handle tedious or complex aspects
of research, allowing human scientists to focus on creativity
and high-level decisions.
2) Multi-Agent Collaboration:
Recent scientific agents
have shifted from single monolithic planners to structured
teams that reflect real laboratory roles and social dy-
namics [53]. The Virtual Lab [54] organizes a principal-
investigator agent and specialist scientist agents into recur-
ring “research meetings,” demonstrating end-to-end design of
SARS-CoV-2 nanobodies and validating wet-lab outcomes; the
setting formalizes division of labor, critique, and iteration, and
reports meaningful human-in-the-loop oversight while preserv-
ing agent autonomy. VIRSCI [55] models team formation ex-
plicitly for idea generation, showing that diversified agent roles
and controlled disagreement increase novelty without sacrific-
ing feasibility. PiFlow [56] adds principle-aware collaboration
for hypothesis refinement by constraining agent proposals
with physical/biological priors to reduce aimless exploration,
a common failure mode in free-form multi-agent pipelines.
At the system level, Agent Laboratory [57] frames an entire
“paper-production” pipeline—problem scoping, method selec-
tion, execution, analysis, and writing—via cooperating agents
with persistent artifacts and audit trails. For embodied science,
ChemAgents [58] deploy a hierarchical multi-agent controller
onboard a robotic chemist to coordinate experiment planning,
execution, and self-correction across hardware and simulation.
Beyond homogeneous LLM teams, hybrid collectives of agents
and humans (e.g., steering committees) have become standard,
with explicit critique-and-revision loops and role-switching
when agents detect stale priors or tool failures [824].
Empirically, multi-agent settings yield the largest gains
when: (1) roles are capability-aligned (planner, critic, execu-
tor); (2) communication channels are structured (RFA tem-
plates, meeting minutes, explicit “claim–evidence” schemas);
and (3) conflict resolution is formalized (voting, debate,
or auctioning). Science-centric multi-agent benchmarks, e.g.,
MultiAgentBench [84] for coordination/competition and com-
municative multimodal tasks, now make such interaction skills
measurable.
3) Tool Use: A defining feature of scientific LLM agents
is their heavy integration with external tools and data re-
sources [823]. SciToolAgent [59] organizes hundreds of
domain tools via a knowledge-graph of capabilities, pre-
conditions, and I/O signatures; the graph enables retrieval-
augmented tool selection, multi-hop sequencing, and fault-
aware backoff across several domains. It reports consistent
gains over vanilla tool-calling baselines on curated scien-
tific workflows and adds policy checks for responsible use.
Biomni [18] exemplifies a domain-scale agent that interfaces
with 150 tools, 59 databases, and 105 software packages to
automate biomedical analyses end-to-end, emphasizing repro-
ducibility and provenance. Under the hood, modern stacks
increasingly adopt the Model Context Protocol (MCP) [825]
to standardize tool discovery, authorization, and invocation,
reducing “glue code” and enabling safer cross-vendor or-
chestration; MCP also clarifies user consent and credentials
for tools that execute code or reach sensitive data. For
web-facing evidence gathering, computer-using and browser-
control agents [826] have matured from ad hoc headless
scripts to trained GUI/web agents that read, click, and upload
files, with reinforcement learning on screen traces; these
unlock literature mining, data extraction, and online lab lo-
gistics but raise security issues (e.g., prompt-injection, DOM-
mismatch), motivating sandboxes and allowlists [827]. For
workflow synthesis, WorkflowLLM and WorkflowBench [85]
explicitly evaluate whether an agent can translate natural-
language protocols into executable API graphs and recover
from tool failures; results indicate that specialized workflow-
tuned models can outperform general LLMs even with in-
context learning. Overall, the state of the art combines: sym-
bolic resource models (capability graphs, ontologies), stan-
dardized tool transport, execution sandboxes (containers, rate
caps), and reflective monitors that detect hallucinated tools or
unsafe parameterizations before launch.
4) Self-evolving Agents: Self-evolving agents extend sci-
entific LLM agents by adding continual adaptation loops to
the standard plan–experiment–verify workflow, so the agent
improves itself over time, not just the artifact. Intra-test-time,
agents externalize feedback and update episodic memory or
prompts to correct future trials, boosting sequential decision
making and coding without weight updates [828], [829].
Agents also accumulate executable skills and even create tools:
Voyager [830] builds a growing library of programs plus an
automatic curriculum that transfers to new worlds. Inter-test-
time, agents update their models via self-generated supervi-
sion [831], [832]. Further, prompts and tool-use policies can be
evolved automatically [833]. For example, Toolformer [834]
demonstrates self-supervised acquisition of API-calling skills
that persist across tasks. Together, these mechanisms instanti-
ate agents that learn from experience, expand capabilities, and
reduce brittleness over long horizons.
In scientific fields, self-evolving agents hold the great po-
tential to continually refine hypotheses, protocols, and tool-use
policies from experimental and literature feedback, rather than
remaining fixed. In biomedicine, STELLA [835] couples an
evolving “Template Library” with a dynamic “Tool Ocean,”
where a Tool-Creation agent autonomously discovers and
integrates new bioinformatics tools; the system’s accuracy
on biomedical benchmarks rises as it accumulates trials, evi-
dencing intra- and inter-task self-improvement. OriGene [836]
instantiates a self-evolving virtual disease biologist: special-
ized agents refine thinking templates, tool composition, and
analytic protocols using human and wet-lab feedback, and the
framework generated targets (e.g., GPR160 for liver cancer)
that were experimentally validated in patient-derived models.
50

In chemistry, ChemAgent [837] maintains a self-updating
library that decomposes problems and reuses refined solutions,
yielding large gains on SciBench [442] and pointing to drug-
and materials-discovery use cases. However, scientific agents
that reliably self-evolve across long horizons with closed-loop
laboratory validation remain rare today and an important next
step in AI-driven scientific discovery [46].
5) Evaluation Frameworks and Benchmarking: Evalua-
tion has shifted from single-turn QA to long-horizon scientific
workflows with verifiable endpoints. ScienceAgentBench [83]
decomposes 102 real tasks from peer-reviewed papers across
four disciplines into executable subtasks with gold pipelines,
expert validation, and containerized harnesses; despite mul-
tiple attempts, the best agents solved only about a third of
tasks, highlighting large headroom and the need for tool
mastery and code debugging. CURIE [110] stresses long-
context scientific reasoning and information extraction across
six domains with expert-curated problems, pushing agents to
manage citations, units, experimental conditions, and cross-
figure synthesis. DiscoveryWorld [838] provides a simulated
environment that supports end-to-end discovery, including
hypothesis formation, experiment design, measurement, and
model revision, while automatically scoring task comple-
tion, action relevance, and discovered knowledge to enable
repeatable testing without wet-lab costs. Auto-Bench [839]
targets causal discovery and hypothesis testing, rewarding
agents for uncovering latent structure and justifying inter-
ventions. WorkflowBench [85] measures orchestration quality
using code-level metrics (e.g., CodeBLEU, pass rates) for
converting natural instructions into robust API workflows.
For collaboration, MultiAgentBench [84] and communicative
multimodal suites [840] quantify coordination, negotiation,
and information-sharing when agents have asymmetric views.
Cross-cutting surveys [841] now standardize taxonomies of
what-to-evaluate (capability, reliability, safety) and how-to-
evaluate (interaction modes, datasets, metrics, tooling), and
call for third-party harnesses, leakage controls, and safety red-
teaming specific to agents with execution privileges. Emerging
best practices include: containerized runners; seeded random-
ness and pass@k for robustness; provenance logging; leakage
audits for data-contaminated facts; and safety checks for tool
scopes, credentials, and network access.
6) Autonomous Scientific Discovery: Autonomous scien-
tific discovery represents a transformative paradigm using
LLMs [457], [842]–[845] and robotics to conduct scientific
research independently without direct human intervention [46],
[49], [846], [847]. By automating critical research tasks includ-
ing data analysis, hypothesis generation, experiment design,
and result interpretation, these automated systems efficiently
process vast amounts of information and uncover patterns that
elude human researchers [846], [848].
Chemistry has seen rapid progress with LLM-tool hybrids
that couple symbolic planners with domain utilities. A repre-
sentative milestone is Coscientist [44], which combined GPT-
4 planning with code execution and instrument control in a
cloud laboratory to autonomously design, run, and analyze
multistep chemistry experiments, including protocol synthesis,
hardware documentation navigation, liquid-handling control,
and data-driven optimization. ChemCrow [52] integrated GPT-
4 with expert-designed chemistry tools, demonstrating end-
to-end tasking from retrosynthesis and catalyst design to
guiding discovery of new chromophores, with expert evalu-
ation showing substantial gains over base models. In the life
sciences, agentic LLMs are beginning to automate experimen-
tal design logic. CRISPR-GPT [849] illustrates how domain
knowledge and tool use can turn free-form language reasoning
into executable gene-editing workflows, chaining literature-
grounded analysis with constraint-aware proposal, delivery
recommendations, and validation planning.
Materials discovery provides a complementary proving
ground where scientific agents orchestrate in silico design
loops and prepare hand-offs to self-driving labs. LLMatDe-
sign [850] shows that reflective agentic loops can translate
high-level targets into candidate materials, invoke calculators
for property estimation, and iteratively refine compositions
in low-data regimes. At the systems level, emerging frame-
works [851] aim to standardize the interface between agentic
planning and autonomous experimentation platforms, high-
lighting patterns for task specification, data management, and
safety interlocks that generalize across domains.
Despite these promising results, autonomous scientific dis-
covery faces significant challenges in two aspects. (i) Gener-
ating proposals that balance scientific validity with genuine
novelty requires systems to identify research gaps and formu-
late innovative hypotheses while maintaining scientific rigor, a
task complicated by AI models’ reliance on existing data pat-
terns. (ii) Implementing closed-loop feedback for end-to-end
experimental validation demands seamless integration across
multiple domains, from robotics for experiment execution to
advanced analytics for result interpretation, while adapting to
real-world experimental uncertainties. Recent developments
such as InternAgent [852] demonstrate progress in address-
ing these challenges through integrated pipelines that span
from idea generation to experimental validation, achieving
notable improvements in tasks like reaction yield prediction
and enhancer activity prediction within significantly reduced
timeframes compared to traditional human-led research.
B. Data Ecosystems for Sci-LLMs
While scientific agents, exemplified by systems like Chem-
Crow [853] and Biomni [18], independently perform complex
scientific tasks, they require an equally advanced data ecosys-
tem to truly thrive. This subsection outlines how data ecosys-
tems must evolve to support autonomous, tool-using Sci-
LLMs. Fig. 29 depicts this evolution: current data foundations
have enabled the emergence of scientific knowledge capabili-
ties in LLMs (Stages I-II), while the transition to agent-driven
discovery (Stage III) necessitates reciprocal development of
data ecosystems to establish closed-loop feedback between
autonomous experimentation and data infrastructure. We first
provide an analysis of the bottlenecks behind the rise of scien-
tific agents (Sec. VIII-B1), and then introduce the concept of
an operating system-level interaction protocol (Sec. VIII-B2).
We propose design principles for next-generation scientific
data architecture (Sec. VIII-B3), laying the foundation for
51

Autonomous 
Experimentation
Data 
Ecosystem
Physics
Chemistry
Materials
Science
Life
Sciences
Astronomy
Earth
Sciences
Engineering
Math
Social 
Sciences…
Data 
Efficiency
Multimodal 
Representation
Knowledge 
Update
Evaluation 
System
Cross-domain 
generalization
Scientific 
reasoning
Interpretability & 
Transparency
Ethical &
Responsible
Data Foundation
Scientific Knowledge Emergence 
Agent-driven Scientific Discovery
Fig. 29: From data infrastructure to agent-assisted discovery: A three-stage evolution of AI in scientific research. This figure
delineates the incremental evolution of data-driven Sci-LLMs: (i) Stage I establishes foundational data infrastructure with
capabilities in efficiency, multimodal representation, and knowledge updating; (ii) Stage II demonstrates the emergence of
scientific capabilities in LLMs driven by mature data ecosystems, enabling cross-domain generalization and scientific reasoning;
(iii) Stage III envisions autonomous AI agents that assist scientific discovery while creating closed-loop feedback with data
ecosystems, a prospective paradigm for self-evolving discovery systems. This evolution, currently manifesting across physics,
chemistry, life sciences, and other domains, illustrates both realized achievements and the expanding potential for AI-driven
research as these technologies proliferate into broader scientific disciplines.
a closed-loop system of machine-led scientific inquiry. Fi-
nally, we discuss a sustainable data sharing protocols that
may benefit the AI4Science community (Sec. VIII-B4). The
ultimate vision is to develop comprehensive platforms like
Intern-Discovery [854] and ScienceOne [855], which aim to
support the entire research workflow through human-machine
collaboration and the integration of “dry” computational anal-
ysis with “wet” lab experimentation, turning Sci-LLMs from
“knowledge processors” to genuine “reasoning engines” for
scientific discovery.
1) The Data Bottleneck Behind the Rise of Scientific
Agents: A primary bottleneck is the severe imbalance in data
modalities available for training. The corpora for today’s Sci-
LLMs are overwhelmingly dominated by textual data, such
as scientific papers and textbooks [24], [30]. While valuable,
this creates a critical gap: there is a severe scarcity of high-
quality, AI-ready experimental and observational data. This
imbalance forces models to learn a description of science
rather than the underlying principles from primary evidence.
Consequently, their reasoning is often shallow, excelling at
textual pattern matching but struggling with novel problems
that require a deep, causal understanding of experimental
phenomena. Efforts to bridge this gap, such as Biomni [18]
which integrates heterogeneous biological data from genomics
to proteomics, underscore both the necessity and the immense
difficulty of creating such multimodal datasets at scale.
Compounding this issue is the disconnected nature of
the scientific knowledge hierarchy within current datasets.
Scientific knowledge is not a flat collection of facts but a
structured hierarchy, and existing data fails to capture the rich
connections between its layers (Sec. II-B). For instance, raw
experimental data is often decoupled from its rich context,
such as the specific instrumental settings and protocols used
to generate it, making it nearly impossible for an agent to
critically evaluate data quality. Furthermore, while scientific
formulas are abundant in texts, the logical derivation processes
and underlying assumptions are rarely encoded, limiting an
agent’s ability to perform rigorous, step-by-step symbolic
reasoning. Most critically, the creative aspects of science,
including failed experiments, serendipitous discoveries, and
novel hypotheses, are almost entirely absent from training
data, starving agents of the examples needed to learn genuine
innovative thinking.
2) Building an Operating System-level Interaction Pro-
tocol: To transcend these limitations, the solution lies not
merely in better datasets but in a fundamentally new archi-
tecture for how agents interact with the scientific world. This
necessitates a shift from monolithic, self-contained models to
dynamic, agent-based systems capable of wielding external
tools for experimentation, simulation, and analysis [856].
Such complex interaction demands an operating system-level
interaction protocol, which would serve as the standardized
interface between the agent’s core reasoning engine and the
vast ecosystem of specialized scientific resources, including
databases, computational simulators, data analysis packages,
and even robotic wet-lab platforms.
This “operating system” would empower the scientific agent
to autonomously manage a full research cycle. Upon receiving
a high-level objective, the agent would first decompose the
problem into a sequence of actionable steps. For each step,
it would select and invoke the appropriate tool through the
standardized protocol—be it querying the Materials Project
database for candidate compounds, running a simulation in
LAMMPS [596] to test physical properties, or analyzing
spectral data with a dedicated library. The protocol must also
enable the agent to parse the diverse outputs from these tools,
52

including numerical results, error codes, structured data files,
while integrating this new information back into its reasoning
context to inform its next action. By establishing this robust
interaction framework, we can begin to address the core data
bottlenecks directly. An agent equipped with such a protocol
is no longer solely dependent on static, pre-existing datasets.
Instead, it can actively generate and consume AI-ready data
on the fly, bridging the chasm between textual knowledge and
empirical evidence. This creates a closed-loop system where
hypotheses are not just formulated based on past literature but
are immediately tested through simulation or data retrieval,
and the results iteratively refine the agent’s understanding.
3) Design Principles for Next-Generation Scientific Data
Architecture: Realizing the vision of autonomous scientific
agents necessitates a fundamental rethinking of how scientific
data is created, managed, and shared. Merely accumulating
more data is insufficient; the next generation of scientific
data infrastructure must be architected from the ground up to
support agent-driven discovery. This requires a paradigm shift
guided by a new set of design principles that prioritize the
needs of intelligent systems, transforming data from a passive
archive into an active, operational resource. These principles
aim to resolve the systemic bottlenecks of traceability, latency,
and AI-readiness that currently hinder progress.
The foremost principle is to ensure that all scientific data
is actionable and AI-ready by design. This moves beyond
the FAIR principles of Findability, Accessibility, Interoper-
ability, and Reusability by demanding that data be immedi-
ately consumable by machine learning models with minimal
preprocessing [338]. In practice, this means establishing and
enforcing community-wide standards for rich, structured meta-
data that captures the full experimental context, from sample
provenance and instrument calibration to software versions
and processing parameters. Data should be published not as
static, isolated files but as integrated packages that link raw
outputs to their corresponding protocols and analyses, enabling
an agent to understand not just what the data is, but how it
was generated and why it is significant.
A second critical principle is the development of infrastruc-
ture for continuous integration and low-latency updates. The
current lag between a scientific discovery and its incorporation
into training corpora renders models perpetually out-of-date, a
fatal flaw in fast-moving fields. Next-generation data architec-
tures must implement automated pipelines that continuously
ingest, validate, and structure new data from publications,
preprints, and experimental platforms. Adopting open-access
policies and version-controlled repositories with real-time API
access will be crucial. This ensures that scientific agents
can learn from the most current knowledge and experimental
findings, reducing the risk of hallucination and enabling them
to reason at the cutting edge of research.
Finally, the new architecture must be built upon a foundation
of unambiguous traceability and comprehensive knowledge
integration. To build trustworthy AI systems, every piece of
data must be accompanied by an immutable record of its origin
and transformation history, a “chain of custody” that allows
for complete reproducibility and auditing [441]. This requires
more than just metadata; it calls for the integration of data
across different modalities and levels of the scientific knowl-
edge hierarchy. The ideal data ecosystem would seamlessly
link a theoretical concept in a textbook to the specific formulas
that formalize it, which in turn connect to the experimental
datasets that validate it, and the computational code used to
analyze it. By architecting this deeply interconnected web of
knowledge, we provide scientific agents with the rich, multi-
faceted context they need to perform complex, verifiable, and
truly insightful reasoning.
4) Sustainable Data Sharing Mechanism:
Traditional
models of data exchange, such as centralized repositories,
or closed-access publications, are proving insufficient for
the scale, diversity, and adaptability required to support the
development of cutting-edge scientific LLMs. As LLMs in-
creasingly depend on vast, heterogeneous, and continuously
evolving datasets, data sharing is being reconceptualized as a
dynamic ecosystem rather than a static resource.
Emerging paradigms of sustainable data sharing center
on principles of openness, fairness, and long-term viability.
Decentralized architectures, often enabled by blockchain, cre-
ate transparent systems for tracing provenance, attributing
value, and rewarding contributions through automated con-
tracts, which can foster trust and incentivize participation. Data
ecosystems are shifting from static collections to automated
curation pipelines that continuously integrate peer-reviewed
publications, experimental outputs, and domain-specific repos-
itories. This ensures that scientific LLMs are not only com-
prehensive but also current and reliable. The establishment
of community-governed data commons is also important, in
which stakeholders across academia, industry, and public in-
stitutions collaborate to set standards for licensing and ethical
use. At the same time, recognizing data-sharing contributions
within academic evaluation systems, similar to citation credit,
could provide strong incentives for participation. The main
challenge is to create fair and transparent rules for governance
and benefit-sharing that balance the interests of institutions,
companies, and individual researchers while ensuring legal,
ethical, and reproducible practices. Ultimately, sustainable data
sharing mechanisms represent not just a technical necessity but
also a cultural and institutional shift, laying the foundation for
scientific LLMs that can accelerate discovery while upholding
the values of equity, transparency, and reproducibility.
5) Data Safety and Privacy: The transition to data-driven
science is gated by a critical threshold of trust: to confidently
leverage high-value datasets, researchers must be assured of
their safety, ethical standing, and legal compliance. Creating
this trust requires a comprehensive governance framework
built on two core pillars: robust privacy protection and ad-
herence to national data controls.
The first pillar is rigorous privacy protection, particularly
for sensitive information in fields like medicine and social
sciences. Data can be stratified by risk, from low-risk ag-
gregated statistics to high-risk genomic or personal health
records [857]. A primary challenge with high-risk data is
preventing re-identification, where even anonymized datasets
can be cross-referenced with public information to uncover
individual identities [858]–[860]. This risk necessitates ad-
vanced de-identification techniques and strict access protocols
53

to protect research participants.
The second pillar addresses data sovereignty and national
controls. Scientific data is increasingly viewed as a strategic
national asset, leading nations to implement regulations that
govern its cross-border flow and use. Prominent examples
include the European Union’s General Data Protection Reg-
ulation (GDPR) [861], which imposes strict conditions on
transferring personal data of EU citizens internationally [862],
and U.S. Export Administration Regulations (EAR) [863],
which control the export of sensitive dual-use technologies.
These legal frameworks require that international scientific
collaborations could build compliance into their data manage-
ment plans from the outset to avoid project-threatening legal
and ethical conflicts.
IX. CHALLENGES AND OUTLOOK
A. Challenges
1) Scientific Data Selection for Efficient Pretraining:
The sheer volume of scientific literature and data necessitates
a strategic approach to data selection for pretraining Sci-
LLMs. Naively ingesting all available information is not
only computationally expensive but can also be detrimental
to model performance due to the varying quality of data
[864]. The challenge, therefore, is to curate a high-quality,
diverse, and representative dataset that enables the model to
learn the fundamental principles of a scientific domain. A
significant hurdle is the inherent noise and bias present in
scientific datasets. Training data can contain everything from
experimental artifacts and outdated information to systemic
biases present in the research literature. Filtering out such
low-quality or irrelevant data is crucial for improving training
efficiency and the downstream performance of the model.
Furthermore, ensuring broad coverage across different sub-
domains, languages, and contexts is essential to prevent the
model from becoming overly specialized and to foster in-
terdisciplinary insights. Recent approaches to data selection
are moving beyond simple heuristics. Model-based filtering
techniques, which use a trained model to identify high-quality
and diverse data samples, have shown promise in improving
pretraining for multilingual datasets [865]. Some methods
even employ online batch selection, dynamically choosing the
most informative data during the training process itself to
adapt to the model’s evolving understanding [866], and thus
create an efficient pretraining process by focusing on data that
maximizes learning and generalization [867], [868].
2) Optimizing Data Processing Pipelines: Once a dataset
has been selected, it must be transformed into a format that
a large language model can understand. This involves devel-
oping robust and scalable data processing pipelines tailored to
the unique characteristics of scientific information. Traditional
data pipelines often struggle with the heterogeneity of scien-
tific data, which can range from unstructured text and images
to highly structured formats like tables and code. The tokeniza-
tion process, which breaks down text into manageable units
for the model, presents a significant challenge in scientific
domains. General-purpose tokenizers, such as BPE (Byte Pair
Encoding), frequently fail to capture the semantic meaning of
specialized scientific terms, chemical formulas, or biological
sequences, leading to fragmented representations. For instance,
a complex molecule name might be broken into generic tokens
that lose its specific chemical meaning. Consequently, spe-
cialized vocabularies and tokenization strategies are required
to maintain domain fidelity. Additionally, data cleaning and
normalization are crucial steps, particularly for unstructured
formats like PDFs, which often contain formatting errors,
figures, and tables that must be accurately extracted and
converted to a uniform input format for efficient processing
by the model [30], [41].
3) Representing Non-Sequential and Non-Textual Data:
Large language models are fundamentally designed to process
sequential data, typically text. However, a significant portion
of scientific knowledge is expressed in non-sequential and
non-textual formats, presenting a profound challenge for Sci-
LLMs. In chemistry, models must interpret 3D molecular
structures, which are inherently graphical and non-sequential,
alongside text-based representations like SMILES strings.
Similarly, in biology, protein structures, gene regulatory net-
works, and genomic data are challenging to represent within
a standard linear transformer architecture. Addressing this
requires innovative approaches that bridge the gap between
sequential language processing and complex data structures.
This often involves multimodal or hybrid architectures. For
example, some approaches utilize graph to encode structural
information like molecular graphs and then project these
embeddings into the Transformer’s input space. Other methods
rely on specialized encoding schemas, such as representing
complex mathematical equations or tables as structured text
sequences, while still preserving their logical and spatial
relationships. The challenge lies in ensuring that these rep-
resentations maintain semantic fidelity and allow the model
to reason across different modalities, moving beyond simple
text understanding to truly grasp the complex relationships
embedded in scientific data.
4) LLM Knowledge Update and Version Control: Scien-
tific research evolves rapidly, with constant influxes of new
discoveries, datasets, and revised theories across disciplines.
Yet, most LLMs are trained on static snapshots of the lit-
erature, rendering them quickly outdated, especially in fast-
moving domains like biomedicine, healthcare, and atmospheric
science, where recent findings can directly influence critical
decisions. Retrieval-augmented approaches offer partial relief
by accessing external sources at inference time, but often fall
short in relevance filtering, source attribution, and resolving
conflicting information. To develop truly current scientific
LLMs, continuous and automated updating pipelines are essen-
tial, capable of regularly ingesting peer-reviewed publications,
preprints, and curated datasets with built-in version control
and traceability. Although tools like ChatGPT and DeepSeek
integrate web search, they lack guarantees of relevance or
reliability. A promising direction is to create collaborative
platforms for dataset generation and distribution, leveraging
adaptive strategies to ensure sustained LLM performance over
time.
54

B. Future Work
1) Integrated Scientific Data Ecosystems: The path for-
ward requires fundamental reconceptualization of how we
approach scientific AI, moving beyond incremental improve-
ments to existing paradigms. Central to this transformation
is the development of integrated scientific data ecosystems
that transcend traditional repository models. These ecosys-
tems must seamlessly connect experimental apparatus, com-
putational simulations, theoretical frameworks, and published
knowledge into living, evolving networks. Rather than static
datasets, we envision active data streams where new exper-
imental results automatically propagate through the system,
updating model understanding while maintaining rigorous
provenance tracking. This requires not only technical infras-
tructure but also new incentive structures within the scientific
community that reward data curation and sharing as first-class
research contributions.
2) Automated Scientific Data Standardization Pipeline:
In the era of data-centric scientific AI, future work must
prioritize the development of automated data standardization
pipelines. These pipelines will serve as the foundational infras-
tructure for training robust and reproducible Sci-LLMs, with
emphasis shifting from model architecture to data curation.
More research work should focus on developing systems that
can automatically clean, validate, and enrich raw scientific
data in heterogeneous forms and modalities, ensuring high-
fidelity inputs for AI models. The development of robust data
versioning and reproducible preparation workflows will also
be essential to make Sci-LLM development not just scalable
but also transparent and reproducible. The ultimate goal is
to move from manual, ad hoc data curation to a scalable,
automated system that provides the scientific community with
readily accessible, high-quality, and standardized data.
3) Comprehensive Evaluation System: Future directions
for comprehensive evaluation should address challenges at
both the model and data levels. From the perspective of Sci-
LLMs, there is a growing need for standardized, domain-
specific benchmarks that go beyond surface-level metrics to as-
sess reasoning depth, factual accuracy, and scientific creativity
across disciplines. Evaluations should incorporate multimodal
and multistep scientific tasks to better reflect real-world re-
search scenarios. On the data side, defining and measuring
dataset quality remains a fundamental challenge, as current
approaches often fail to capture how data supports model capa-
bilities. Key criteria, such as AI-readiness, completeness, sci-
entific relevance, timeliness, usability, and accessibility, must
be integrated into data evaluation frameworks. A key direction
for future research is to develop a systematic framework for
data assessment, enabling more informed dataset selection
and ultimately advancing model reliability and performance.
Integrating these two perspectives will enable more robust,
nuanced, and trustworthy evaluation frameworks that drive the
development of truly capable scientific AI systems.
4) Advanced Scientific Reasoning: The evolution from
current language models to genuine scientific reasoning sys-
tems demands architectural innovations that embed physi-
cal laws, causal structures, and domain-specific constraints
directly into model design. Future architectures must move
beyond pattern matching to incorporate symbolic reasoning
capabilities, enabling manipulation of mathematical equations
and chemical structures with the same fluency as natural lan-
guage. These systems should exhibit compositional generaliza-
tion—applying learned principles to novel combinations never
seen during training—and maintain explicit representations of
uncertainty that propagate through reasoning chains. The inte-
gration of neural and symbolic approaches, long pursued but
never fully realized, becomes essential for scientific domains
where interpretability and correctness are paramount.
5) Autonomous Scientific Agents: A paradigm shift from
passive models to active scientific agents represents per-
haps the most transformative direction for future research.
These agents must possess capabilities beyond current sys-
tems: proposing testable hypotheses, designing experiments
to resolve uncertainties, and iterating based on empirical re-
sults. This requires developing safe interaction protocols with
laboratory equipment and simulation environments, creating
standardized interfaces for scientific tools and databases, and
establishing frameworks for multi-agent collaboration where
specialized models contribute complementary expertise. The
vision extends to AI systems that not only assist human
scientists but also autonomously explore hypothesis spaces too
vast for human investigation.
6) From Sci-LLMs to Scientific Discovery: The ultimate
objective of Sci-LLMs extends beyond the automation of
routine tasks to the acceleration of pivotal scientific break-
throughs. Sci-LLMs present unique potentials to identify sub-
tle, non-obvious correlations and patterns within vast, multi-
modal datasets that would be impossible for human researchers
to process in a short time. We are moving from a phase
where Sci-LLMs are primarily used for literature review and
synthesis to an advanced stage where these models can serve
as powerful instruments for accelerated hypothesis generation,
potentially contributing to Nobel Prize-worthy discoveries.
While human creativity and ethical oversight remain impor-
tant, Sci-LLMs will act as collaborators to help significantly
reduce the discovery cycle, allowing researchers to pursue
more ambitious research. This integration has the potential
to redefine the very nature of scientific method, pushing the
boundaries of human knowledge in unprecedented ways.
7) Ethical Governance for Responsible Scientific AI Inno-
vation: The responsible development of increasingly capable
scientific AI systems necessitates robust ethical frameworks
and governance structures [869]. As these systems begin to
influence research directions and resource allocation, ensuring
equitable access becomes critical to prevent further con-
centration of scientific capabilities. Questions of attribution,
accountability, and validation for AI-generated discoveries
require careful consideration and community consensus. The
environmental impact of training large-scale models shall be
balanced against their potential contributions to sustainability
science, demanding innovations in efficient training and model
architectures.
X. CONCLUSION
This survey systematically reviews the emerging field of
scientific large language models from the perspectives of data,
55

model architectures, and agent-based systems. By introducing
a unified taxonomy of scientific data and analyzing more
than 270 pre-training and post-training datasets as well as
over 190 evaluation datasets, we highlight the distinctive
multimodal, cross-scale, and domain-specific challenges that
differentiate scientific AI from general-purpose LLMs. We
summarize the evolution from transfer learning and large-
scale foundation models to instruction-following and tool-
augmented scientific agents, and examine current evaluation
practices spanning static benchmarks, process-oriented assess-
ments, and autonomous scientific discovery frameworks. We
further discuss persistent issues in data quality, representation
gaps, and knowledge updating, and outline future directions
including operating-system–level data ecosystems and hybrid
neural–symbolic architectures. Together, these insights provide
a consolidated reference and a forward-looking roadmap for
building trustworthy, continually evolving Sci-LLMs capable
of advancing data-driven scientific discovery.
56

TABLE II: Data source description.
Source
Description
Web and Internet content
High-quality web crawl datasets containing billions of pages from diverse internet sources, including news
articles, blogs, and general web content. These datasets undergo extensive cleaning and deduplication
processes to ensure text quality for language model training.
Books and literary works
Digitized collections of books spanning various genres, languages, and time periods. Sources include
public domain texts, open-access libraries, and e-book platforms, providing rich narrative content and
diverse writing styles.
Encyclopedias
and
knowledge
bases
Structured knowledge repositories like Wikipedia and other encyclopedic sources across multiple
languages. These provide factual, well-organized information on diverse topics with consistent formatting
and citation standards.
Academic and research resources
Peer-reviewed papers, preprints, theses, and scholarly publications from repositories like arXiv and
academic databases. These sources offer technical, specialized content with rigorous methodology and
domain expertise.
Social media and forums
User-generated content from platforms like Reddit and Stack Exchange, capturing conversational
language, community discussions, and Q&A formats that reflect natural human communication patterns.
Integration of existing datasets
Curated collections that combine and refine multiple existing open-source datasets, leveraging previous
data curation efforts to create comprehensive training corpora.
Scientific databases
Specialized repositories containing structured scientific data including biomedical literature, protein
sequences, chemical compounds, clinical trials, astronomical observations, and materials science data
from authoritative institutions.
Patent databases
Technical documentation from global patent offices including USPTO, EPO, and WIPO, containing
detailed descriptions of innovations, technical specifications, and claims across various technological
domains.
Comprehensive multi-source in-
tegration
Large-scale datasets that aggregate content from multiple source types (web, books, code, academic
papers) to create diverse, balanced training corpora.
Other sources
Additional specialized or proprietary content sources that don’t fit into the above categories, potentially
including domain-specific databases, institutional archives, or unique text collections.
TABLE III: Data type description.
Type
Description
Raw text
A broad umbrella for any string-serializable content, e.g., natural language plus tables, sequences, code,
logs, etc. Used for language modeling or domain pretraining without explicit prompts/answers or paired
media.
Text QA
Text-only question-answer pairs, optionally with supporting passages, supervising reading comprehension
or factual reasoning.
Text QA with CoT
Text QA augmented with explicit multi-step explanations or derivations alongside the final answer.
VQA
Visual question-answering pairs, where each image is with a question and the corresponding answer.
VQA (multi-image)
A question grounded on two or more related images, requiring cross-image comparison, temporal
alignment, or aggregation.
VQA with CoT
VQA data augmented with step-by-step rationales or intermediate reasoning traces in addition to the final
answer.
Image-text
Image-text pairs, where the text contains description (e.g., captions, reports) for alignment, captioning,
retrieval, or representation learning.
Video-text
Video-text pairs, where the text contains description (e.g., subtitles, transcripts, narrations) for alignment,
captioning, retrieval, or representation learning.
Classification, regression, gener-
ation, etc.
For numeric/matrix/graph records lacking natural-language pairing, annotate by supervised objective.
57

TABLE IV: Summary of pre-training and post-training datasets for scientific LLMs/MLLMs. [link] directs to dataset websites.
Scientific Domain
Dataset
Subdomain
Modality
Purpose
Type
Release Language Source
Annotation
Pipeline
Human
Annotators Human Tasks
Auto-annotation
Tools
Size
Life Sciences
MIRAGE [191] [link]
Agriculture
Biological entity photos
SFT
VQA (multi-image)
2025.06 EN
Scientific databases
Semi-automated
N/A
Data generation
GPT-4.1
37,512
CROP [723] [link]
Agriculture
Academic papers
SFT
Text QA
2024.09 EN, ZH
Academic and research resources
Semi-automated
N/A
Data generation
GPT-4
211,909
ToT-Biology [link]
General Biology
Biomedical QA
SFT, CoT
Text QA with CoT
2025.01 EN
Academic and research resources
N/A
N/A
N/A
N/A
23,000
BioASQ10b-factoid [769] [link]
General Biology
Clinical dialogue
SFT
Text QA
2023.07 EN
Academic and research resources
Manual
N/A
Data generation and review
N/A
1.25K
ReasonMed [734] [link]
Healthcare and Medical Sciences
Clinical dialogue
SFT, CoT
Text QA with CoT
2025.06 EN
Comprehensive multi-source inte-
gration
Automated
N/A
N/A
Qwen-2.5-72B,
DeepSeek-R1-
Distill-Llama-70B,
HuatuoGPT-o1-70B
194,925
Open-PMC-18M [870] [link]
Healthcare and Medical Sciences
CT, CFP
Pre-training
Image-text
2025.06 EN
Academic and research resources
Automated
N/A
N/A
N/A
25,000,000
ReXVQA [871] [link]
Healthcare and Medical Sciences
X-ray
SFT
VQA
2025.06 EN
Integration of existing datasets
Semi-automated
3
Data review
GPT-4o,
ClinicalBERT,
MedEmbed
613,277
RexGradient-160K [872] [link]
Healthcare and Medical Sciences
X-ray
Pre-training, SFT
Image-text
2025.05 EN
Scientific databases
Manual
N/A
N/A
N/A
160K
AlphaMed19K [873] [link]
Healthcare and Medical Sciences
Biomedical QA
SFT, CoT
Text QA
2025.05 EN
Integration of existing datasets
Automated
N/A
Data generation and review
N/A
19,178
Derm1M [874] [link]
Healthcare and Medical Sciences
Dermatological images
Pre-training
Image-text
2025.3
EN
Social media and forums, Aca-
demic and research resources
Automated
N/A
N/A
DenseNet,
DINO,
GPT-4o, Whisper
1,029,761
MedVideoCap-55K [664] [link]
Healthcare and Medical Sciences
Medical videos
Pre-training, SFT
Video-text
2025.04 EN
Web and Internet content
Automated
N/A
Data review
GPT-4o
55,803
medical-o1-reasoning-SFT [544] [link]
Healthcare and Medical Sciences
Clinical dialogue
SFT, CoT
Text QA with CoT
2025.04 EN, ZH
Comprehensive multi-source inte-
gration
Automated
N/A
N/A
DeepSeek-R1
90,200
GMAI-Reasoning10K [546] [link]
Healthcare and Medical Sciences
CT,
Dermatology,
Endoscopy,
CFP,
Histopathology, MRI, Microscopy, OCT,
PET, US, X-ray, etc.
SFT
VQA
2025.04 EN
Comprehensive multi-source inte-
gration
Semi-automated
N/A
Data review
GPT-4o
17,004
MedReason [733] [link]
Healthcare and Medical Sciences
Clinical dialogue
SFT, CoT
Text QA with CoT
2025.03 EN
Comprehensive multi-source inte-
gration
Automated
N/A
N/A
N/A
32,682
GEMeX-VQA [875] [link]
Healthcare and Medical Sciences
X-ray
Pre-training, SFT
VQA
2025.03 EN
Integration of existing datasets
Semi-automated
N/A
Data review
OpenBioLLM-70B,
GPT-4o
1,601,615
MIMIC-Diff-VQA [796] [link]
Healthcare and Medical Sciences
X-ray
SFT
VQA (multi-image)
2025.02 EN
Scientific databases
Semi-automated
3
Data generation and review
ScispaCy
630,633
ICG-CXR [876] [link]
Healthcare and Medical Sciences
X-ray
SFT
VQA (multi-image)
2025.03 EN
Scientific databases
Automated
N/A
Data generation and review
GPT-4
11,439
VL-Health [877] [link]
Healthcare and Medical Sciences
CT, CFP, MRI, Microscopy, OCT, US, X-ray Pre-training, SFT
Image-text, VQA
2025.02 EN, ZH
Comprehensive multi-source inte-
gration
Semi-automated
N/A
Data review
GPT-4o
1,548,847
BIOMEDICA [204] [link]
Healthcare and Medical Sciences
Academic papers
Pre-training
Raw text
2025.01 EN
Academic and research resources
Semi-automated
7
Data review
N/A
2,400,000
AfriMed-QA v2 [878] [link]
Healthcare and Medical Sciences
Clinical dialogue
SFT
Text QA
2024.11 EN
Comprehensive multi-source inte-
gration
Semi-automated
N/A
N/A
N/A
15,275
GMAI-VL-5.5M [542] [link]
Healthcare and Medical Sciences
CT,
Dermatology,
Endoscopy,
CFP,
Histopathology, MRI, Microscopy, OCT,
PET, US, X-ray, etc.
SFT
VQA, Text QA
2024.11 EN, ZH
Comprehensive multi-source inte-
gration
Semi-automated
5
Data review
GPT-4o
5.5M
OphVL [665] [link]
Healthcare and Medical Sciences
Ophthalmic Surgical Video
Pre-training
Video-text
2024.11 EN
Web and Internet content
Automated
N/A
Data generation and review
SurgicBERTa, GPT-
4o
375,198
Bora-v1 [879] [link]
Healthcare and Medical Sciences
Endoscopy, MRI, Microscopy, US
SFT
Video-text
2024.10 EN
Integration of existing datasets
Automated
N/A
Data review
N/A
4,897
MedSyn [880] [link]
Healthcare and Medical Sciences
Clinical documentation
Pre-training
Raw text
2024.08 RU
Academic and research resources
Automated
N/A
N/A
GPT-4,
Medical
Knowledge Graph
41,200
RealMedQA [881] [link]
Healthcare and Medical Sciences
Biomedical QA
SFT
Text QA
2024.08 EN
Encyclopedias
and
knowledge
bases
Semi-automated
6
Data generation and review
GPT-3.5-turbo
1,200
MedTrinity-25M [882] [link]
Healthcare and Medical Sciences
CT, MRI, X-ray, Histopathology, etc.
Pre-training
Image-text, VQA
2024.08 EN
Integration of existing datasets, Sci-
entific databases
Automated
N/A
N/A
N/A
25,000,000
MedPix-single [883] [link]
Healthcare and Medical Sciences
CT, MRI, US, X-ray
Pre-training
Image-text
2024.07 EN
Scientific databases
Manual
N/A
Data generation
N/A
59,000
BIMCV-R [884] [link]
Healthcare and Medical Sciences
CT
Pre-training
Image-text
2024.07 EN
Scientific databases
Semi-automated
20+
Data review
GPT-4
8,069
MIMIC-Ext-MIMIC-CXR-VQA [885] [link]
Healthcare and Medical Sciences
X-ray
Pre-training, SFT
VQA
2024.07 EN
Integration of existing datasets
Semi-automated
4
Data review
GPT-4
377,391
EHRXQA [704] [link]
Healthcare and Medical Sciences
X-ray
Pre-training, SFT
VQA
2024.07 EN
Integration of existing datasets
Semi-automated
4
Data review
GPT-4
46,152
CheXpertPlus [657] [link]
Healthcare and Medical Sciences
X-ray
Pre-training
Image-text
2024.06 EN
Scientific databases
Semi-automated
10
Data generation and review
CheXbert, Radgraph
223,228
PubMedVision [541] [link]
Healthcare and Medical Sciences
CT, Endoscopy, CFP, Infrared Reflectance,
MRI, Microscopy, OCT, US, X-ray
SFT
VQA
2024.06 EN
Academic and research resources
Automated
N/A
N/A
GPT-4,
GPT-4V,
SentenceBERT
1,294,092
MediQ [654] [link]
Healthcare and Medical Sciences
EHR
SFT
Text QA
2024.06 EN
Academic and research resources
Automated
N/A
N/A
GPT-3.5, LLaMA-3
2,545
HuatuoGPT2-SFT-GPT4-140K [42] [link]
Healthcare and Medical Sciences
Clinical dialogue
SFT
Text QA
2024.06 ZH
Other sources
Automated
N/A
Data generation and review
GPT-4
140,000
Asclepius-Synthetic-Clinical-Notes [link]
Healthcare and Medical Sciences
EHR
SFT
Text QA
2024.06 EN
Academic and research resources
Semi-automated
N/A
Data generation
GPT-3.5
158,114
Know Medical Dialogues [link]
Healthcare and Medical Sciences
Clinical dialogue
SFT
Text QA
2024.06 EN
Web and Internet content
Automated
N/A
N/A
N/A
480
Duvel [link]
Healthcare and Medical Sciences
Academic papers
SFT
Classification
2024.05 EN
Scientific databases
Semi-automated
N/A
Data generation
ALAMBIC
6,553
SkinCAP [886] [link]
Healthcare and Medical Sciences
Dermatology
Pre-training
Image-text
2024.05 EN
Academic and research resources
Semi-automated
N/A
N/A
N/A
4,000
MM-Retinal [887] [link]
Healthcare and Medical Sciences
CFP, FFA, OCT
Pre-training, SFT
Image-text
2024.05 EN, ZH
Academic and research resources
Semi-automated
6
Data review
N/A
4,349
M3D-Data (caption) [660] [link]
Healthcare and Medical Sciences
CT, Clinical reports
Pre-training, SFT
Image-text, Text QA, VQA
2024.04 EN
Scientific databases, Integration of
existing datasets
Semi-automated
N/A
Data generation and review
GPT-4V
120,092
M3D-Data (instruction) [660] [link]
Healthcare and Medical Sciences
CT, Clinical reports
SFT
Image-text, Text QA, VQA
2024.04 EN
Scientific databases, Integration of
existing datasets
Semi-automated
N/A
Data generation and review
GPT-4V
58,180
RadGenome-Chest CT [888] [link]
Healthcare and Medical Sciences
CT
Pre-training, SFT
VQA, Image-text
2024.04 EN
Academic and research resources
Semi-automated
N/A
Data review
SAT, GPT-4, GPT-2
1,965,000
CXR-LLM [link]
Healthcare and Medical Sciences
X-ray
SFT
VQA
2024.03 EN
Integration of existing datasets
Semi-automated
N/A
Data generation
GPT-4
104,892
MedChatZH [889] [link]
Healthcare and Medical Sciences
Clinical dialogue
Pre-training, SFT
Text QA
2024.03 ZH
Comprehensive multi-source inte-
gration
Semi-automated
N/A
Data generation
N/A
2,068,823
Mental health chatbot dataset [link]
Healthcare and Medical Sciences
Clinical dialogue
SFT
Text QA
2024.02 EN
Web and Internet content
Automated
N/A
N/A
N/A
172
StatPearls [890] [link]
Healthcare and Medical Sciences
Academic papers
Pre-training
Raw text
2024.02 EN
Scientific databases
Automated
N/A
N/A
N/A
301,202
Quilt-Instruct [891] [link]
Healthcare and Medical Sciences
Histopathology
SFT
VQA
2024.02 EN
Web and Internet content
Semi-automated
N/A
Data review
GPT-4-turbo
107,131
SHADR [674] [link]
Healthcare and Medical Sciences
EHR
SFT
Classification
2024.01 EN
Scientific databases
Semi-automated
N/A
Data review
GPT-3.5
446
RJUA-QA [892] [link]
Healthcare and Medical Sciences
Dianosis report, Clinical dialogue
SFT
Text QA
2023.12 ZH
Other sources
Manual
N/A
Data generation and review
N/A
1,705
RP3D-DiagDS [774] [link]
Healthcare and Medical Sciences
CT, MRI, X-ray US, Fluoroscopy, etc.
Pre-training
Classification
2023.12 EN
Scientific databases
Semi-automated
N/A
Data generation and review
Custom
crawlers,
GPT-4
40,936
PMC-Inline [658] [link]
Healthcare and Medical Sciences
CT, MRI, PET, US, X-ray
Pre-training
Image-text
2023.11 EN
Academic and research resources
Automated
N/A
N/A
N/A
11,000,000
ROCOv2 [661] [link]
Healthcare and Medical Sciences
CT, MRI, PET, US, X-ray
Pre-training, SFT
Image-text
2023.11 EN
Academic and research resources
Semi-automated
N/A
N/A
fastText, MedCAT
80,080
PMC-CaseReport [658] [link]
Healthcare and Medical Sciences
X-ray
SFT
Image-text, VQA
2023.11 EN
Academic and research resources
Automated
N/A
N/A
N/A
1,100,000
MedMD [658] [link]
Healthcare and Medical Sciences
CT, MRI, PET, US, X-ray
Pre-training, SFT
Image-text, VQA
2023.11 EN
Academic and research resources
Semi-automated
8
Data review
ChatGPT
16,000,000
Taiyi-Instruction-Data-001 [893] [link]
Healthcare and Medical Sciences
Dianosis report, Clinical dialogue, EMR,
Academic papers, etc.
Pre-training, SFT
Text QA
2023.11 EN, ZH
Integration of existing datasets
Automated
N/A
Data review
N/A
1,114,315
MTS-DIALOG [894] [link]
Healthcare and Medical Sciences
Clinical dialogue
Pre-training
Text QA
2023.11 EN
Academic and research resources
Semi-automated
12
Data generation and review
GPT-4o
23,977
MTS-Dialog [894] [link]
Healthcare and Medical Sciences
Clinical dialogue
Pre-training
Raw text
2023.11 EN
Patent databases
Semi-automated
9
Data generation and review
OPUS-MT, BART
1,701
Clinical Guidelines [38] [link]
Healthcare and Medical Sciences
Clinical guidelines
Pre-training
Text QA with CoT
2023.11 EN
Scientific databases
Semi-automated
N/A
Data review
S2ORC, GROBID
38,000
INSPECT [895] [link]
Healthcare and Medical Sciences
CT
Pre-training
Image-text
2023.11 EN
Scientific databases
Semi-automated
N/A
Data review, Data generation
Clinical Longformer
23,248
AeroPath [896] [link]
Healthcare and Medical Sciences
CT
Agent
Segmentation
2023.11 EN
Scientific databases
Semi-automated
2
Data review
3D Slicer
27 (CT scans)
MORFITT [897] [link]
Healthcare and Medical Sciences
Clinical papers
Pre-training
Classification
2023.11 FR
Academic and research resources
Manual
N/A
Data review
N/A
3,556
NoteChat [703] [link]
Healthcare and Medical Sciences
Clinical dialogue
SFT
Text QA
2023.10 EN
Integration of existing datasets
Automated
N/A
N/A
N/A
207,000
ChiMed-VL [898] [link]
Healthcare and Medical Sciences
X-ray, CT, MRI, etc.
Pre-training, SFT
Image-text, Text QA
2023.10 ZH, EN
Integration of existing datasets
Automated
N/A
N/A
GPT-3.5
1,049,455
OncQA [899] [link]
Healthcare and Medical Sciences
Dianosis report
SFT
Text QA
2023.10 EN
Other sources
Manual
6
Data generation and review
GPT-4
156
SDOH-NLI [900] [link]
Healthcare and Medical Sciences
Clinical notes
Pre-training
Classification
2023.10 EN
Integration of existing datasets
Manual
N/A
Data generation
N/A
21.1K
CMtMedQA [901] [link]
Healthcare and Medical Sciences
Clinical dialogue
SFT
Text QA
2023.08 ZH
Other sources
Automated
N/A
Data review
N/A
68,000
DISC-Med-SFT [902] [link]
Healthcare and Medical Sciences
Clinical dialogue
SFT
Text QA
2023.08 ZH
Integration of existing datasets
Semi-automated
N/A
Data review
GPT-3.5, GPT-4
470,000
Healix-V1 [link]
Healthcare and Medical Sciences
Clinical dialogue
SFT
Text QA
2023.07 EN
Comprehensive multi-source inte-
gration
N/A
N/A
N/A
N/A
796,239
Medical Cord19 [590] [link]
Healthcare and Medical Sciences
Academic papers
Pre-training
Raw text
2023.07 EN
Academic and research resources
Automated
N/A
N/A
N/A
250,000
Pile-PubMed Central [652] [link]
Healthcare and Medical Sciences
Academic papers
Pre-training
Raw text
2023.07 EN
Academic and research resources
Automated
N/A
Data generation
N/A
N/A
AGCT [903] [link]
Healthcare and Medical Sciences
Biomedical knowledge base
Pre-training
Raw text
2023.07 EN, FR
Scientific databases
Automated
N/A
N/A
Custom generation
421,216
Synthetic CSAW 100k Mammograms [904] [link]
Healthcare and Medical Sciences
Mammography
SFT
Image-text
2023.07 EN
Scientific databases
Automated
N/A
N/A
Diffusion Model
100K
Quilt-1M [151] [link]
Healthcare and Medical Sciences
Histopathology
Pre-training, SFT
Image-text
2023.06 EN
Academic and research resources,
Web and Internet content, Other
sources
Automated
N/A
N/A
N/A
1,000,000
LLaVA-Med [905] [link]
Healthcare and Medical Sciences
CT, Histopathology, MRI, Microscopy, PET,
US, X-ray
Pre-training, SFT
VQA, Image-text
2023.06 EN
Comprehensive multi-source inte-
gration
Automated
N/A
N/A
GPT-4
630,000
ShenNong-TCM-Dataset [906] [link]
Healthcare and Medical Sciences
Clinical dialogue
SFT, CoT
Text QA
2023.06 ZH
Comprehensive multi-source inte-
gration
Automated
N/A
Data generation
ChatGPT
113,000
PMC-VQA [907] [link]
Healthcare and Medical Sciences
CT, CFP, Histopathology, MRI, Microscopy,
US, X-ray
SFT
VQA
2023.05 EN
Academic and research resources
Automated
N/A
N/A
N/A
226,946
ChatMed-Consult-Dataset [908] [link]
Healthcare and Medical Sciences
Clinical dialogue
SFT
Text QA
2023.05 ZH
Web and Internet content
Automated
N/A
Data generation
GPT-3.5-Turbo
549,000
QiZhenGPT-20k [909] [link]
Healthcare and Medical Sciences
Clinical dialogue
SFT
Text QA
2023.05 ZH
Other sources
Automated
N/A
Data generation
N/A
20,000
Huatuo-26M [910] [link]
Healthcare and Medical Sciences
Biomedical QA
Pre-training, SFT
Text QA
2023.05 EN
Encyclopedias
and
knowledge
bases
Semi-automated
N/A
Data review
Bert, T5
26,000,000
Huatuo26M-Lite [910] [link]
Healthcare and Medical Sciences
Clinical dialogue, Dianosis report
Pre-training, SFT
Text QA
2023.05 ZH
Web and Internet content
Semi-automated
N/A
Data review
ChatGPT
177,703
Visual Med-Alpaca [link]
Healthcare and Medical Sciences
CT, CFP, Histopathology, MRI, Microscopy,
US, X-ray
SFT
VQA
2023.04 EN
Scientific databases
Automated
N/A
N/A
GPT-3.5
54,000
MedAlpaca [521] [link]
Healthcare and Medical Sciences
Clinical dialogue, Academic papers
Pre-training, SFT
Raw text, Text QA
2023.04 EN
Comprehensive multi-source inte-
gration
Automated
N/A
Data generation and review
N/A
860,076
Med-ChatGLM [911] [link]
Healthcare and Medical Sciences
Biomedical knowledge base
SFT
Text QA
2023.04 ZH
Integration of existing datasets
Automated
N/A
Data generation
GPT-3.5
7,622
PMC-OA [205] [link]
Healthcare and Medical Sciences
CT, Dermatology, Endoscopy, Histopathol-
ogy, Microscopy, MRI, OCT, PET, X-ray
Pre-training
Image-text
2023.03 EN
Academic and research resources
Automated
N/A
Data generation and review
ResNet101
(DocFigure),
ResNet34
(DETR
MedICaT),
PMC-
CLIP
1,646,592
ChatDoctor [648] [link]
Healthcare and Medical Sciences
Clinical dialogue
SFT
Text QA
2023.03 EN
Other sources
Semi-automated
N/A
Data generation and review
N/A
115,000
WikiMedQA [912] [link]
Healthcare and Medical Sciences
Clinical Reports
SFT
Text QA
2023.03 EN
Web and Internet content
Semi-automated
N/A
N/A
SentenceBERT,
BioLinkBERT
111,895
MIMIC-IV [673] [link]
Healthcare and Medical Sciences
EHR
Pre-training, SFT
Raw text
2023.01 EN
Scientific databases
Semi-automated
N/A
N/A
Transformer-DeID
364,627
BioRED [651] [link]
Healthcare and Medical Sciences
Academic papers
Pre-training
Classification
2022.09 EN
Scientific databases
Semi-automated
6
Data generation and review
PubTator
500
ViHealthQA [913] [link]
Healthcare and Medical Sciences
Biomedical QA
SFT
Text QA
2022.06 VI
Social media and forums
Manual
N/A
Data generation
N/A
10,015
Continued on next page
58

TABLE IV – continued from previous page
Scientific Domain
Dataset
Domain
Modality
Purpose
Type
Release Language Source
Annotation
Pipeline
Human
Annotators Human Tasks
Auto-annotation
Tools
Size
MedMCQA [451] [link]
Healthcare and Medical Sciences
Medical exams
SFT
Text QA
2022.03 EN
Books and literary works
Automated
N/A
Data generation
N/A
193,155
PMC-Patients-ReCDS [914] [link]
Healthcare and Medical Sciences
Clinical dialogue
SFT
Text QA
2022.02 EN
Academic and research resources
Automated
N/A
N/A
N/A
293,000
PMC-Patients [915] [link]
Healthcare and Medical Sciences
Clinical report
Pre-training
Raw text
2022.02 EN
Scientific databases
Semi-automated
N/A
Data review
PubMedBERT,
BioLinkBERT
167,000
CMCQA [916] [link]
Healthcare and Medical Sciences
Clinical dialogue
SFT
Text QA
2022.01 ZH
Web and Internet content
Automated
N/A
Data review
N/A
1,294,753
IMCS-V2 [917] [link]
Healthcare and Medical Sciences
Clinical dialogue
SFT
Text QA
2022.01 ZH
Other sources
Manual
N/A
Data generation and review
N/A
4,116
MLEC-QA [918] [link]
Healthcare and Medical Sciences
Biomedical QA
SFT
Raw text
2021.11 ZH
Academic and research resources
Semi-automated
N/A
Data generation and review
N/A
136,236
ImageClef-VQA Med 2021 [919] [link]
Healthcare and Medical Sciences
CT, MRI, US, X-ray
SFT
VQA
2021.09 EN
Academic and research resources
Automated
N/A
N/A
N/A
4,500
BioLeaflets [920] [link]
Healthcare and Medical Sciences
Package leaflets
Pre-training
Raw text
2021.09 EN
Web and Internet content
Semi-automated
N/A
Data generation
Stanza,
Amazon
Comprehend
Medical
1,067
MedGPT-5k-ko [656] [link]
Healthcare and Medical Sciences
Clinical trials, EHR, Medical forum, Medi-
cal textbooks
SFT
Classification, Text QA
2021.06 ZH
Scientific databases, Books and lit-
erary works, Web and Internet con-
tent, Comprehensive multi-source
integration
Manual
3
Data generation and review
N/A
149,141
CBLUE [921] [link]
Healthcare and Medical Sciences
Clinical trials, EHR, Medical forum, Medi-
cal textbooks
SFT
Classification, Text QA
2021.06 ZH
Scientific databases, Books and lit-
erary works, Web and Internet con-
tent, Comprehensive multi-source
integration
Manual
3
Data generation and review
N/A
149,141
MedDG [922] [link]
Healthcare and Medical Sciences
Clinical dialogue
SFT
Text QA
2021.05 ZH
Web and Internet content
Automated
N/A
Data generation and review
N/A
100,000
SLAKE [773] [link]
Healthcare and Medical Sciences
CT, MRI, X-ray
SFT
VQA
2021.02 EN, ZH
Academic and research resources
Automated
N/A
N/A
N/A
11,958
Chinese-medical-dialogue-data [923] [link]
Healthcare and Medical Sciences
Clinical dialogue
SFT
Text QA
2021.02 ZH
Other sources
N/A
N/A
N/A
N/A
792,099
DeepEyeNet [659] [link]
Healthcare and Medical Sciences
CFP, FFA
Pre-training
Image-text
2021.01 EN
Scientific databases
Manual
N/A
Data generation
N/A
15,709
AIforCOVID [924] [link]
Healthcare and Medical Sciences
X-ray
Pre-training, SFT
Image-text
2020.12 EN
Scientific databases
Manual
N/A
Data generation
N/A
820
MedICaT [662] [link]
Healthcare and Medical Sciences
CT, Endoscopy, Histopathology, MRI, Mi-
croscopy, PET, US, X-ray
Pre-training, SFT
Image-text
2020.10 EN
Academic and research resources
Semi-automated
7
Data generation
ResNet101-
DocFigure, ScispaCy 217,060
ImageClef-VQA Med 2020 [925] [link]
Healthcare and Medical Sciences
CT, MRI, US, X-ray
SFT
VQA
2020.09 EN
Academic and research resources
Automated
N/A
N/A
N/A
4,000
MedQA [522] [link]
Healthcare and Medical Sciences
Medical exams
SFT
Text QA
2020.09 EN, ZH
Scientific databases
Manual
N/A
Data generation and review
N/A
61,097
MedDialog-CN [702] [link]
Healthcare and Medical Sciences
Clinical dialogue
SFT
Text QA
2020.07 ZH
Web and Internet content
Automated
N/A
Data review
N/A
1,100,000
MEDIQA-AnS [799] [link]
Healthcare and Medical Sciences
Consumer health QA
SFT
Text QA
2020.05 EN, ZH
Web and Internet content
Semi-automated
2
Data generation
Custom crawlers
156
MedDialog [650] [link]
Healthcare and Medical Sciences
Clinical dialogue
SFT
Text QA
2020.04 EN, ZH
Web and Internet content
Automated
N/A
N/A
Custom crawlers
14,668,058
PathVQA [150] [link]
Healthcare and Medical Sciences
Histopathology
SFT
VQA
2020.03 EN
Academic and research resources
Automated
N/A
N/A
N/A
19,654
RetinaRocks [link]
Healthcare and Medical Sciences
CFP
Pre-training, SFT
Image-text
2019.12 EN
Other sources
Manual
N/A
Data generation
N/A
4,000
MedQuAD [926] [link]
Healthcare and Medical Sciences
Clinical dialogue
SFT
Text QA
2019.10 EN
Web and Internet content
Automated
N/A
N/A
Custom crawlers
47,441
ImageClef-VQA Med 2019 [927] [link]
Healthcare and Medical Sciences
CT, MRI, US, X-ray
SFT
VQA
2019.09 EN
Academic and research resources
Automated
N/A
N/A
N/A
15,292
PubMedQA [450] [link]
Healthcare and Medical Sciences
Academic papers
SFT
Text QA
2019.09 EN
Web and Internet content
Semi-automated
N/A
Data generation and review
N/A
212,300
PubMedQA instruction [450] [link]
Healthcare and Medical Sciences
Academic papers
SFT
Text QA
2019.09 EN
Academic and research resources
Manual
N/A
Data generation
N/A
1K
MIMIC-CXR [154] [link]
Healthcare and Medical Sciences
X-ray
Pre-training
Image-text
2019.08 EN
Scientific databases
Manual
N/A
Data generation
N/A
227,835
MIMIC-Extract [653]
Healthcare and Medical Sciences
EHR
Pre-training
Text QA
2019.07 EN
Scientific databases
Automated
N/A
N/A
N/A
2,000,000
webMedQA [928] [link]
Healthcare and Medical Sciences
Clinical dialogue
SFT
Text QA
2019.03 ZH
Web and Internet content
Automated
N/A
Data review
N/A
63,284
VQA-RAD [705] [link]
Healthcare and Medical Sciences
CT, MRI, PET, US, X-ray
SFT
VQA
2018.11 EN
Academic and research resources
Manual
N/A
Data generation
N/A
1,793
cMedQA2 [929] [link]
Healthcare and Medical Sciences
Clinical dialogue
SFT
Text QA
2018.11 ZH
Web and Internet content
Automated
N/A
Data review
N/A
108,000
ROCO [930] [link]
Healthcare and Medical Sciences
CT, MRI, PET, US, X-ray
Pre-training, SFT
Image-text
2018.09 EN
Academic and research resources
Automated
N/A
N/A
N/A
81,000
emrQA [931] [link]
Healthcare and Medical Sciences
Clinical dialogue
SFT
Text QA
2018.09 EN
Integration of existing datasets
Semi-automated
N/A
N/A
N/A
455,000
ImageClef-VQA Med 2018 [932] [link]
Healthcare and Medical Sciences
CT, MRI, US, Unknown, X-ray
SFT
VQA
2018.06 EN
Academic and research resources
Automated
N/A
N/A
N/A
6,413
LiveQA [933] [link]
Healthcare and Medical Sciences
Consumer health QA
SFT
Text QA
2018.02 EN
Scientific databases
Automated
N/A
Data review
N/A
634
LiveQA trec2017 [649] [link]
Healthcare and Medical Sciences
Clinical dialogue
SFT
Text QA
2017.08 EN
Academic and research resources
Semi-automated
N/A
Data review
N/A
634
OpenI [155] [link]
Healthcare and Medical Sciences
X-ray
Pre-training
Image-text
2016.03 EN
Scientific databases
Manual
N/A
Data generation
N/A
3,955
Retina Image Bank [link]
Healthcare and Medical Sciences
CFP, FFA
Pre-training, SFT
Image-text
2012.08 EN
Other sources
Manual
N/A
Data generation
N/A
30,452
William Hoyt ImageText [link]
Healthcare and Medical Sciences
CFP
Pre-training
Image-text
2004.03 EN
Scientific databases
Manual
N/A
Data generation
N/A
856
Pima [655] [link]
Healthcare and Medical Sciences
EHR
SFT
Classification
1988.11 EN
Scientific databases
Manual
N/A
N/A
N/A
691
COVID-19-Data-Hub [934] [link]
Healthcare and Medical Sciences
Global pandemic data (cases, vaccines, poli-
cies, etc.)
Pre-training, RAG
Classification, Regression
2020.07 EN
Comprehensive multi-source inte-
gration
Automated
N/A
N/A
R package
N/A
BEACON [696] [link]
Molecular and Cellular Biology
RNA sequence
SFT
Raw text
2024.06 EN
Comprehensive multi-source inte-
gration
Semi-automated
N/A
Data generation and review
N/A
870,883
SPICE [626] [link]
Molecular and Cellular Biology
SMILES
Pre-training, RAG
Classification, Regression
2024.03 EN
Scientific databases
Semi-automated
N/A
Data generation and review
N/A
113,999
PubChemSTM [628] [link]
Molecular and Cellular Biology
SMILES
Pre-training, SFT
Raw text
2024.01 EN
Academic and research resources
Semi-automated
N/A
Data generation
SciBERT, spaCy
281,000
SourceData [935] [link]
Molecular and Cellular Biology
Academic papers
Pre-training
VQA
2023.10 EN
Academic and research resources
Semi-automated
N/A
Data review
PubMedBERT,
BioLinkBERT,
GPT-4o
62,543
Mol-Instructions [697] [link]
Molecular and Cellular Biology
Biomolecular instructions
SFT
Text QA
2023.06 EN
Comprehensive multi-source inte-
gration
Automated
N/A
Data review
GPT-3.5
2,043,000
PCdes [627] [link]
Molecular and Cellular Biology
SMILES
Pre-training, SFT
Raw text
2022.12 EN
Academic and research resources
Automated
N/A
N/A
Custom crawlers
12,000
MoMu [629] [link]
Molecular and Cellular Biology
Graph
Pre-training, SFT
Raw text
2022.12 EN
Academic and research resources
Automated
N/A
N/A
OGB
15,613
PEER [695] [link]
Molecular and Cellular Biology
Protein sequence
SFT
Classification, Regression
2022.10 EN
Comprehensive multi-source inte-
gration
Semi-automated
N/A
Data generation and review
N/A
329,922
BioGPT [936] [link]
Molecular and Cellular Biology,
Healthcare and Medical Sciences
Biomedical domain pretraining corpus
Pre-training, SFT
Raw text
2022.08 EN
Scientific databases, Academic and
research resources
Automated
N/A
N/A
Moses
tokenizer,
fastBPE
15M
DISEASES [803] [link]
Molecular and Cellular Biology,
Healthcare and Medical Sciences,
Multi-omics
Disease-gene associations
SFT, RAG
Classification
2015.01 EN
Academic and research resources,
Integration of existing datasets, Sci-
entific databases
Semi-automated
N/A
Data generation and review
NER tagger
8,336,442
BioReason [422] [link]
Molecular and Cellular Biology,
Multi-omics
DNA sequence, KEGG pathways, Gene vari-
ants
SFT, CoT
Text QA with CoT
2025.05 EN
Scientific databases, Academic and
research resources
Semi-automated
N/A
N/A
Custom scripts
87,620
GeneChat [637] [link]
Multi-omics
Nucleotide sequence
Pre-training
Text QA
2025.06 EN
Scientific databases
N/A
N/A
Data generation
N/A
47,275
Genomics instructions [511] [link]
Multi-omics
Nucleotide sequence
SFT
Text QA
2025.04 EN
Academic and research resources
N/A
N/A
Data generation
N/A
4,954,234
scMMGPT data [640] [link]
Multi-omics
scRNA-seq
Pre-training, SFT
scRNA-seq-text
2025.03 EN
Academic and research resources
Automated
N/A
N/A
N/A
467K
OPI [698] [link]
Multi-omics
Protein
SFT
Text QA
2025.03 EN
Scientific databases
Semi-automated
N/A
Data generation
GPT-3.5
1,640,000
OpenGenome2 [489] [link]
Multi-omics
Nucleotide sequence
Pre-training
Raw text
2025.02 EN
Integration of existing datasets
N/A
N/A
N/A
N/A
8,800B
(nucleotides)
Seq2Func [636] [link]
Multi-omics
Nucleotide sequence
SFT
Text QA
2025.02 EN
Scientific databases
Automated
N/A
Data generation
N/A
297,000
DNA2Image [636] [link]
Multi-omics
Nucleotide sequence
SFT
Generation
2025.02 EN
Scientific databases
Automated
N/A
Data generation
N/A
43,200
LLaMA-Gene (protein) [40] [link]
Multi-omics
Protein sequence
Pre-training, SFT
Text QA
2024.12 EN
Scientific databases
N/A
N/A
Data generation
N/A
62,918
LLaMA-Gene (DNA) [40] [link]
Multi-omics
DNA sequence
Pre-training, SFT
Text QA
2024.12 EN
Scientific databases
N/A
N/A
Data generation
N/A
178,551
OpenGenome [488] [link]
Multi-omics
Nucleotide sequence
Pre-training
Raw text
2024.11 EN
Integration of existing datasets
N/A
N/A
N/A
N/A
300B
(nucleotides)
The 1000G [319] [link]
Multi-omics
Nucleotide sequence
Pre-training
Raw text
2024.10 EN
Scientific databases
N/A
N/A
N/A
N/A
20,500B
(nucleotides)
Multispecies dataset [319] [link]
Multi-omics
Nucleotide sequence
Pre-training
Raw text
2024.10 EN
Scientific databases
N/A
N/A
N/A
N/A
174B
(nucleotides)
NT Benchmark [319] [link]
Multi-omics
Nucleotide sequence
SFT
Classification
2024.10 EN
Academic and research resources
N/A
N/A
N/A
N/A
493,242
ProteinLMDataset [643] [link]
Multi-omics
Protein sequence
Pre-training
Raw text
2024.06 EN
Academic and research resources
Automated
N/A
N/A
N/A
893,000
RNAcentral [641], [937] [link]
Multi-omics
RNA sequence
Pre-training
Raw text
2024.05 EN
Scientific databases
N/A
N/A
N/A
N/A
23M
RNA-QA [641] [link]
Multi-omics
RNA sequence
SFT
Text QA
2024.05 EN
Academic and research resources
Automated
N/A
N/A
GPT-4o
407,616
ProCoT [699] [link]
Multi-omics
Biomedical QA
SFT, CoT
Text QA with CoT
2024.05 EN
Scientific databases, Academic and
research resources
Semi-automated
N/A
Data generation and review
embedding-based fil-
tering
4,967,723
UniProtKB/Swiss-Prot [938]
Multi-omics
Protein sequence
Pre-training
Raw text
2023.11 EN
Scientific databases
N/A
N/A
N/A
N/A
570K
Multi-species genome [318] [link]
Multi-omics
Nucleotide sequence
Pre-training
Raw text
2023.06 EN
Integration of existing datasets
N/A
N/A
N/A
N/A
32.49B
(nucleotides)
Genomic Benchmark [939] [link]
Multi-omics
Nucleotide sequence
SFT
Classification
2023.05 EN
Academic and research resources
N/A
N/A
N/A
N/A
699,116
CELLxGENE scRNA-seq Collection [513] [link]
Multi-omics
scRNA-seq
Pre-training
Gene Expression-pretrain
2023.05 EN
Scientific databases
N/A
N/A
N/A
N/A
33 M
Human Pancreas [940] [link]
Multi-omics
scRNA-seq
SFT
Classification
2023.01 EN
Academic and research resources
N/A
N/A
N/A
N/A
10,600
scFoundation Dataset [941] [link]
Multi-omics
scRNA-seq
Pre-training
Gene Expression-pretrain
2022.10 EN
Scientific databases
N/A
N/A
N/A
N/A
50M
Human genome [632] [link]
Multi-omics
Nucleotide sequence
Pre-training
Raw text
2021.02 EN
Scientific databases
N/A
N/A
N/A
N/A
2.75B
(nucleotides)
GPD [942] [link]
Multi-omics
Nucleotide sequence
Pre-training
Raw text
2021.02 EN
Scientific databases
N/A
N/A
N/A
N/A
142,809
Myeloid [943] [link]
Multi-omics
scRNA-seq
SFT
Classification
2021.02 EN
Academic and research resources
N/A
N/A
N/A
N/A
9,748
Human Cell Atlas Dataset [944] [link]
Multi-omics
scRNA-seq
SFT
Classification
2021.02 EN
Academic and research resources
N/A
N/A
N/A
N/A
84,363
GVD [945] [link]
Multi-omics
Nucleotide sequence
Pre-training
Raw text
2019.07 EN
Scientific databases
N/A
N/A
N/A
N/A
13,203B
Multiple Sclerosis [946] [link]
Multi-omics
scRNA-seq
SFT
Classification
2019.07 EN
Academic and research resources
N/A
N/A
N/A
N/A
7,844
PanglaoDB [947] [link]
Multi-omics
scRNA-seq
Pre-training
Gene Expression-pretrain
2018.11 EN
Scientific databases
N/A
N/A
N/A
N/A
1,126,580
Zheng68k [948] [link]
Multi-omics
scRNA-seq
SFT
Classification
2016.07 EN
Academic and research resources
N/A
N/A
N/A
N/A
68,450
GRCh38/hg38 [634] [link]
Multi-omics
Nucleotide sequence
Pre-training
Raw text
2013.12 EN
Scientific databases
N/A
N/A
N/A
N/A
3.1B
(nucleotides)
Biology-Instructions [701] [link]
Multi-omics
DNA, RNA, Protein sequence
SFT
Text QA
2024.12 EN
Academic and research resources
Semi-automated
N/A
Data generation
GPT-4o, Claude-3.5-
sunnet
3.3 M
TCPA [630] [link]
Multi-omics
Protein sequence
Pre-training
Raw text
2013.09 EN
Academic and research resources
N/A
N/A
N/A
N/A
4,379
NCBI-GenBank [95] [link]
Multi-omics
Nucleotide sequence
Pre-training
Raw text
2012.11 EN
Scientific databases
N/A
N/A
N/A
N/A
5,000B
(nucleotides)
GRCh37/hg19 [634] [link]
Multi-omics
Nucleotide sequence
Pre-training
Raw text
2009.02 EN
Scientific databases
N/A
N/A
N/A
N/A
3.1B
(nucleotides)
Neuro-3D [711] [link]
Neuroscience
EEG
Pre-training, SFT
Classification
2025.03 EN
Academic and research resources
Semi-automated
N/A
N/A
N/A
720
Things-MEG [709] [link]
Neuroscience
MEG
Pre-training, SFT
Classification
2023.04 EN
Academic and research resources
Semi-automated
N/A
N/A
N/A
22,248
Things-EEG2 [707] [link]
Neuroscience
EEG
Pre-training, SFT
Classification
2022.11 EN
Academic and research resources
Semi-automated
N/A
N/A
N/A
16,740
SHU [719] [link]
Neuroscience
EEG
Pre-training, SFT
Classification
2022.08 EN
Academic and research resources
Semi-automated
N/A
N/A
N/A
11,988
Things-fMRI [709] [link]
Neuroscience
fMRI
Pre-training, SFT
Classification
2022.07 EN
Academic and research resources
Semi-automated
N/A
N/A
N/A
8,740
NSD-Imagery [710] [link]
Neuroscience
fMRI
Pre-training, SFT
Classification
2022.07 EN
Academic and research resources
Semi-automated
N/A
N/A
N/A
2,304
HMC [714] [link]
Neuroscience
EEG
Pre-training, SFT
Classification
2022.03 EN
Academic and research resources
Semi-automated
N/A
N/A
N/A
154
Things-EEG1 [706] [link]
Neuroscience
EEG
Pre-training, SFT
Classification
2022.01 EN
Academic and research resources
Semi-automated
N/A
N/A
N/A
22,248
NSD [708] [link]
Neuroscience
fMRI
Pre-training, SFT
Classification
2021.09 EN
Academic and research resources
Semi-automated
N/A
N/A
N/A
70,566
ZuCo2 [713] [link]
Neuroscience
EEG
Pre-training, SFT
Text QA
2019.11 EN
Academic and research resources
Semi-automated
N/A
N/A
N/A
739
Continued on next page
59

TABLE IV – continued from previous page
Scientific Domain
Dataset
Domain
Modality
Purpose
Type
Release Language Source
Annotation
Pipeline
Human
Annotators Human Tasks
Auto-annotation
Tools
Size
DIR [949] [link]
Neuroscience
fMRI
Pre-training, SFT
Classification
2019.01 EN
Academic and research resources
Semi-automated
N/A
N/A
N/A
6,000
Workload [722] [link]
Neuroscience
EEG
Pre-training, SFT
Classification
2018.12 EN
Academic and research resources
Semi-automated
N/A
N/A
N/A
1080
ZuCo1 [712] [link]
Neuroscience
EEG
Pre-training, SFT
Text QA
2018.11 EN
Academic and research resources
Semi-automated
N/A
N/A
N/A
1,107
SEED-IV [721] [link]
Neuroscience
EEG
Pre-training, SFT
Classification
2018.02 EN
Academic and research resources
Semi-automated
N/A
N/A
N/A
143,610
TUSL [718] [link]
Neuroscience
EEG
Pre-training, SFT
Classification
2018.01 EN
Academic and research resources
Semi-automated
N/A
N/A
N/A
245
TUEV [717] [link]
Neuroscience
EEG
Pre-training, SFT
Classification
2015.12 EN
Academic and research resources
Semi-automated
N/A
N/A
N/A
112,237
TUAB [717] [link]
Neuroscience
EEG
Pre-training, SFT
Classification
2015.12 EN
Academic and research resources
Semi-automated
N/A
N/A
N/A
409,083
SEED [720] [link]
Neuroscience
EEG
Pre-training, SFT
Classification
2015.05 EN
Academic and research resources
Semi-automated
N/A
N/A
N/A
144,851
Sleep-EDF [715] [link]
Neuroscience
EEG
Pre-training, SFT
Classification
2013.10 EN
Academic and research resources
Semi-automated
N/A
N/A
N/A
197
SHHS [716] [link]
Neuroscience
EEG
Pre-training, SFT
Classification
1998.01 EN
Academic and research resources
Semi-automated
N/A
N/A
N/A
6,441
repoDB [804] [link]
Pharmacy, Healthcare and Medical
Sciences
Drug-disease relationships, Clinical trials
RAG
Classification, Text QA
2017.03 EN
Scientific databases
Automated
N/A
N/A
scripts
15,648
Chemistry
MOSES [607] [link]
Biochemistry
SMILES
Pre-training
Raw text
2020.07 EN
Academic and research resources
Automated
N/A
Data generation and review
N/A
1,936,962
ChemBL [217] [link]
Biochemistry
SMILES
Pre-training
Raw text
2012.01 EN
Academic and research resources
Automated
N/A
Data generation and review
N/A
1,961,462
ChemRxivQuest [950] [link]
General Chemistry
Academic papers
Pre-training, SFT
Text QA
2025.05 EN
Academic and research resources
Manual
N/A
Data generation and review
N/A
970
ScholarChemQA [106] [link]
General Chemistry
Academic papers
Pre-training, SFT
Text QA
2025.02 EN
Academic and research resources
Manual
N/A
Data generation and review
N/A
40K
SMolInstruct [690] [link]
General Chemistry
SMILES
SFT
Text QA
2024.08 EN
Scientific databases
Semi-automated
N/A
Data generation and review
GPT-4
3.3M
ChemNLP [951] [link]
General Chemistry
Text
Pre-training, SFT
Classification
2023.01 EN
Academic and research resources
Manual
N/A
Data generation and review
N/A
110,342
PMO [215] [link]
General Chemistry
SMILES
Pre-training, SFT
Raw text
2022.05 EN
Academic and research resources
Automated
N/A
Data generation and review
N/A
10K
ZINC [216] [link]
General Chemistry
SMILES
Pre-training
Raw text
2012.10 EN
Academic and research resources
Automated
N/A
Data generation and review
N/A
250K
DeepProtein [952] [link]
Pharmacy
Protein sequence, SMILES
Pre-training, SFT
Raw text
2025.05 EN
Academic and research resources
Automated
N/A
Data generation and review
N/A
78K
TrialBench [754] [link]
Pharmacy
SMILES, Disease code
Pre-training, SFT
Raw text
2024.09 EN
Academic and research resources
Automated
N/A
Data generation and review
N/A
470K
TDC2 [953] [link]
Pharmacy
SMILES, Protein sequence, Genome se-
quence
Pre-training, SFT
Classification, Regression, Genera-
tion
2024.09 EN
Academic and research resources
Manual
N/A
Data generation and review
N/A
3.4B (tokens)
SBDDBench [954] [link]
Pharmacy
Text, Protein sequence, SMILES
Pre-training, SFT
Protein-ligand
2022.06 EN
Academic and research resources
Automated
N/A
Data generation and review
N/A
5K
TOP [955] [link]
Pharmacy
SMILES
Pre-training, SFT
Raw text
2022.02 EN
Academic and research resources
Automated
N/A
Data generation and review
N/A
12K
TDC [244] [link]
Pharmacy
SMILES, Protein sequence, Genome se-
quence
Pre-training, SFT
Classification, Regression, Genera-
tion
2021.06 EN
Academic and research resources
Manual
N/A
Data generation and review
N/A
0.2B (tokens)
DeepPurpose [611] [link]
Pharmacy
Protein sequence, SMILES
Pre-training, SFT
Raw text
2020.12 EN
Academic and research resources
Automated
N/A
Data generation and review
N/A
5,074
DrugBank [956] [link]
Pharmacy
SMILES
Pre-training, SFT
Raw text
2018.01 EN
Academic and research resources
Manual
N/A
Data generation and review
N/A
18K
DrugCentral [957] [link]
Pharmacy
SMILES
Pre-training, SFT
Raw text
2017.01 EN
Academic and research resources
Automated
N/A
Data generation and review
N/A
4,995
USPTO [613]
Synthetic Chemistry
SMILES
Pre-training, SFT
Generation
2015.07 EN
Patent databases
Manual
N/A
Data generation and review
N/A
1,939,253
Physics
MM-PhyQA [736] [link]
General Physics
High-school exams
SFT, CoT
VQA with CoT
2024.04 EN
Web and Internet content
Manual
N/A
Data generation and review
AFL 3.0
3,825
PIQA [681] [link]
General Physics
Text
SFT
Text QA
2020.01 EN
Other sources
Semi-automated
AFLite
Data generation and review
N/A
19,838
Astronomy
AstroLLaVA [563] [Link]
Astronomy
General dialog, Astronomical images
SFT
VQA
2025.04 EN
Comprehensive multi-source inte-
gration
Semi-automated
N/A
Data review
GPT-4
29,783
AstroPT [670] [Link]
Astronomy
Astronomical images
Pre-training
Regression
2024.05 EN
Web and Internet content, Scientific
databases
Automated
N/A
Data review
DESI Legacy Survey
API
8.6M (tokens)
Astro-NER [726] Link
Astronomy
Academic papers
SFT
Text QA
2024.05 EN
Academic and research resources
Semi-automated
4
Data generation and review
GPT-3.5
5000
AstroLLaMA-chat [724] [Link]
Astronomy
Academic papers
SFT
Text QA
2024.01 EN
Academic and research resources
Manual
N/A
Data review
N/A
10,356
AstroLLaMA [562] [Link]
Astronomy
Academic papers
SFT
Text QA
2023.09 EN
Academic and research resources,
Web and Internet content
Manual
N/A
Data review
N/A
9.5M
ATel [958] Link
Astronomy
Academic papers
SFT
Text QA
2023.05 EN
Academic and research resources
Manual
N/A
Data review
N/A
234
AstroBERT [668][Link]
Astronomy
Academic papers
Pre-training
Raw text
2022.11 EN
Academic and research resources
Automated
12
Data generation and review
N/A
3.8B (tokens)
AstroMLab 4 [567] [Link]
Astronomy
Academic papers
SFT
Text QA
2025.05 EN
Integration of existing datasets
Automated
N/A
Data generation and review
Gemini-1.5-Pro
250,000
arXiv
preprints
AstroMLab 3 [564] [Link]
Astronomy
Academic papers
SFT
Text QA
2025.04 EN
Academic and research resources
Automated
N/A
Data generation and review
Gemini-1.5-Pro
3.3B (tokens)
AstroMLab 2 [725] [Link]
Astronomy
Academic papers
SFT
Text QA
2024.09 EN
Academic and research resources
Automated
N/A
Data generation and review
Gemini-1.5-Pro
10,356
Starwhisper-pilsar [781] Link
Astrophysics
Text, pulsar diagnostic plots, pulsars signals SFT
Classification
2024.04 EN
Integration of existing datasets
Manual
N/A
Data generation and review
DeepSeek-VL-7B,
InternVL2-40B
106,674
PAPERCLIP [782] [Link]
Astrophysics
synthetic conversation text, Astronomical
images
SFT
Image-text
2024.03 EN
Academic and research resources
Automated
N/A
Data review
Mixtral-8x7B-
Instruct
31,859
Materials Science
ChEBI-20-MM [693] [link]
Materials Science
InChI, IUPAC, SELFIES, Molecular image
SFT
Text QA
2025.01 EN
Integration of existing datasets
Manual
N/A
Data generation and review
N/A
29,706
Materials Project Trajectory [621] [link]
Materials Science
CIF
Pre-training
Raw text
2023.07 EN
Scientific databases
Manual
N/A
Data generation and review
N/A
1,580,395
DigiMOF [619] [link]
Materials Science
CIF
Pre-training
Raw text
2023.05 EN
Academic and research resources
Manual
N/A
Data generation and review
N/A
15,501
Novel Materials Discovery (NOMAD) [620] [link]
Materials Science
CIF
Pre-training
Raw text
2023.03 EN
Scientific databases
Manual
N/A
Data generation and review
N/A
4,341,443
MOFX-DB (hMOF) [959] [link]
Materials Science
CIF
Pre-training
Raw text
2023.02 EN
Integration of existing datasets
Manual
N/A
Data generation and review
N/A
160,000
MatScholar [625] [link]
Materials Science
Academic papers
Pre-training
Raw text
2022.07 EN
Academic and research resources
Manual
N/A
Data generation and review
N/A
5M
Pfeiffer et al. Chemical composition [624] [link]
Materials Science
Chemical Composition
Pre-training
Raw text
2022.03 EN
Comprehensive multi-source inte-
gration
Manual
N/A
Data generation and review
N/A
14,884
Pfeiffer et al. Mechanical Properties [624] [link]
Materials Science
Numerical property
Pre-training
Raw text
2022.03 EN
Comprehensive multi-source inte-
gration
Manual
N/A
Data generation and review
N/A
1,278
ChEBI-20 [692] [link]
Materials Science
Scientific instruction
SFT
Text QA
2021.11 EN
Integration of existing datasets
Manual
N/A
Data generation and review
N/A
29709
ZINC [623] [link]
Materials Science
SMILES
Pre-training
Raw text
2020.12 EN
Scientific databases
Manual
N/A
Data generation and review
N/A
230M
JARVIS-DFT [622] [link]
Materials Science
InChI, IUPAC, SELFIES
Pre-training
Raw text
2020.11 EN
Integration of existing datasets
Manual
N/A
Data generation and review
N/A
41,000
MOSES [691] [link]
Materials Science
SMILES
SFT
Text QA
2020.11 EN
Integration of existing datasets
Manual
N/A
Data generation and review
N/A
1.6M
QMOF [618] [link]
Materials Science
CIF
Pre-training
Raw text
2020.05 EN
Academic and research resources
Manual
N/A
Data generation and review
N/A
20,000
Warwick Electron Microscopy Datasets [694] [link]
Materials Science
STEM image, TEM image, TEM exit wave-
function
SFT
VQA
2020.05 EN
Academic and research resources
Manual
N/A
Data generation and review
N/A
135395
CoRE MOF 2019 [617] [link]
Materials Science
CIF
Pre-training
Raw text
2019.12 EN
Integration of existing datasets
Manual
N/A
Data generation and review
N/A
14,000
Inorganic Crystal Structure Database (ICSD) [616]
[link]
Materials Science
CIF
Pre-training
Raw text
2019.10 EN
Scientific databases
Manual
N/A
Data generation and review
N/A
318,901
US Patent Office (USPTO) [218] [link]
Materials Science
SMILES
Pre-training
Raw text
2017.06 EN
Patent databases
Manual
N/A
Data generation and review
N/A
2,830,616
Open Quantum Materials Database (OQMD) [615]
[link]
Materials Science
CIF
Pre-training
Raw text
2014.11 EN
Scientific databases
Manual
N/A
Data generation and review
N/A
1,317,811
Materials Project [70] [link]
Materials Science
CIF
Pre-training
Raw text
2013.07 EN
Scientific databases
Manual
N/A
Data generation and review
N/A
577,813
Earth Science
WeatherQA [729] [link]
Atmosphere
Remote sensing, Science QA
SFT
VQA
2024.06 EN
Scientific databases
Semi-automated
4
Data review
GPT-4
8,511
SeafloorAI [730] [link]
Hydrosphere
Sonar images, Text
SFT
VQA
2024.11 EN
Scientific databases
Semi-automated
4
Data review
GPT-4
7M
TEOChatlas [579] [link]
Lithosphere
Remote sensing
SFT
VQA
2025.01 EN
Scientific databases
Automated
N/A
Data generation
N/A
554K
EarthVQA [728] [link]
Lithosphere
Remote sensing, Science QA
SFT
VQA
2023.12 EN
Scientific databases
Automated
N/A
Data generation
ArcGIS toolbox
208K
Geochat [589] [link]
Lithosphere
Remote sensing, Science QA
SFT
VQA
2023.11 EN
Scientific databases
Automated
N/A
Data generation
Vicuna-v1.5
306K
FloodNet [727] [link]
Lithosphere
Remote sensing, Science QA
SFT
VQA
2021.05 EN
Scientific databases
Manual
N/A
Data generation and review
N/A
11K
GeoSignal [568] [link]
Lithosphere, Hydrosphere, Atmo-
sphere
Remote sensing, Science QA
SFT
Text QA
2023.06 EN
Encyclopedias
and
knowledge
bases,
Academic
and
research
resources,
Scientific
databases,
Comprehensive
multi-source
integration
Semi-automated
10
Data review
GPT-4
39,749
GeoLLaVA-8k [574] [link]
Remote Sensing
Remote sensing
SFT
Image-text, VQA
2025.05 EN
Academic and research resources
Semi-automated
35
Data generation and review
GPT-4o
81,367
EVAttrs-95k [571] [link]
Remote Sensing
Remote sensing, Object property
SFT
Image-text, VQA
2025.03 EN
Academic and research resources
Semi-automated
N/A
Data generation and review
Qwen2-VL-72B,
GPT-4o
95.1K
VersaD [960] [link]
Remote Sensing
Remote sensing
Pre-training
Image-text
2024.11 EN
Academic and research resources
Automated
N/A
N/A
Gemini-Vision
1.4M
RSVP [572] [link]
Remote Sensing
Remote sensing
SFT
Image-text, VQA
2024.10 EN
Integration
of
existing
datasets,
Academic and research resources
Automated
N/A
N/A
GPT-4V,
DINOv2-
ViT
L/14,
CLIP-
ConvNeXt
3.65M
FIT-RS [961] [link]
Remote Sensing
Remote sensing, Relation graph, etc.
SFT
Image-text, VQA
2024.07 EN
Integration
of
existing
datasets,
Academic and research resources
Semi-automated
N/A
Data generation
TinyLLaVA-3.1B,
GPT-4,
GPT-3.5,
CLIP-ViT-L14
1,415K
VRSBench [798] [link]
Remote Sensing
Remote sensing
SFT
Image-text, VQA
2024.06 EN
Academic and research resources
Semi-automated
N/A
Data review
GPT-4V
142,390
MMRS-1M [962] [link]
Remote Sensing
Remote sensing, Optical, SAR, Infrared, etc. SFT
Image-text, VQA
2024.03 EN
Integration of existing datasets
Automated
N/A
N/A
N/A
1.06M
ChatEarthNet [963] [link]
Remote Sensing
Remote sensing, Optical, Multi-band
SFT
Image-text
2024.02 EN
Scientific databases
Semi-automated
N/A
Data review
GPT-3.5, GPT-4V
173,488
LHRS-Align [964] [link]
Remote Sensing
Remote sensing
Pre-training
Image-text
2024.02 EN
Scientific databases
Automated
N/A
N/A
Vicuna-v1.5-13B
1.15M
LHRS-Instruct [964] [link]
Remote Sensing
Remote sensing
SFT
Image-text, VQA
2024.02 EN
Integration
of
existing
datasets,
Academic and research resources
Semi-automated
N/A
Data review
Vicuna-v1.5-13B,
GPT-4
12K
RS5M [731] [link]
Remote Sensing
Remote sensing
Pre-training
Image-text
2024.01 EN
Scientific databases
Automated
N/A
N/A
CLIP
5.07M
SkyEye-968k [965] [link]
Remote Sensing
Remote sensing
SFT
Image-text, Video-text, VQA
2024.01 EN
Integration of existing datasets
Semi-automated
N/A
Data review
N/A
968K
SkyScript [732] [link]
Remote Sensing
Remote sensing
Pre-training
Image-text
2023.12 EN
Academic and research resources,
Scientific databases
Automated
N/A
N/A
CLIP, Logistic Re-
gression model
2.6M
RSICap [785] [link]
Remote Sensing
Remote sensing
SFT
Image-text
2023.07 EN
Academic and research resources
Manual
5
Data generation, Data review
N/A
2.5K
General Science
NaturalReasoning [686] [link]
Multidisciplinary (incl. Physics)
Text
SFT
Text QA with CoT
2025.02 EN
Web and Internet content, Books
and literary works, Academic and
research resources
Semi-automated
N/A
Data review
LLaMA-70B
2.8M
Nemotron-Science [685] [link]
Multidisciplinary (incl. Physics)
Text with formulae and code
SFT, RLHF
Text QA with CoT
2025.05 EN
Social
media
and
forums,
Academic and research resources,
Books and literary works
Semi-automated
N/A
Data review
DeepSeek-R1
2.7M
Galactica [30] [link]
Multidisciplinary (incl. Chemistry) Text (incl. formulas, code)
Pre-training
Raw text
2022.11 EN
Webpages
Fully-automated
N/A
Data generation and review
Custom
crawlers,
PDF parsers
106B tokens
SciBERT [24] [link]
Multidisciplinary (incl. Physics)
Academic papers
Pre-training
Raw text
2019.09 EN
Academic and research resources
Automated
N/A
Data generation
Crawlers, text pro-
cessing tools
3.3B (tokens)
ArXivCap [605] [link]
Physics, Biology, etc.
Paper figures
Pre-training
Image-text
2024.05 EN
Academic and research resources
Semi-automated
7
Data review
PDF parsers
6.4M
SCP-116K [687] [link]
Physics, Chemistry, Biology, etc.
Text with formulae
SFT
Text QA with CoT
2025.01 EN
Academic and research resources,
Books and literary works
Semi-automated
N/A
Data review
PDF parsers, OCR,
LaTeX rendering
116.8K
Continued on next page
60

TABLE IV – continued from previous page
Scientific Domain
Dataset
Domain
Modality
Purpose
Type
Release Language Source
Annotation
Pipeline
Human
Annotators Human Tasks
Auto-annotation
Tools
Size
MegaScience [966] [link]
Medicine, Physics, Chemistry, Bi-
ology
Science textbooks
SFT
Text QA with CoT
2024.08 EN
Web and Internet content, Books
and literary works, Integration of
existing datasets
Semi-automated
N/A
Data review
Llama3.3-70B-
Instruct,
DeepSeek-
V3,
BGE-large-en-
v1.5
651,840
61

TABLE V: Summary of evaluation datasets for scientific LLMs/MLLMs. [link] directs to dataset websites.
Scientific
Domain
Dataset
Subdomain
Modality
Level
Type
Release Language Source
Annotation
Pipeline
Human
Annotators
Human Tasks
Auto-annotation
Tools
Size
Evaluation
Type
Metrics
Life Science
SeedBench [778] [link]
Agriculture
Breeding literature
Expert
Text QA
2025.05 EN, ZH
Academic and research resources
Semi-automated
N/A
Data generation and review
GPT-4
2,264
MCQ,
Open-
ended
Acc, F1, ROUGE
AgEval [190] [link]
Agriculture
Plant stress phenotyping photos and
annotations
Expert
VQA
2025.01 EN
Scientific databases
N/A
N/A
N/A
N/A
1,200
Classification,
Regression
F1, NMAE
AgXQA [105] [link]
Agriculture
Agricultural extension records
Expert
Text QA
2024.10 EN
Academic and research resources
Semi-automated
N/A
N/A
N/A
2,186
Open-ended
EM, F1
Fundus-MMBench [967] [link]
Healthcare and Medical Sciences
CFP
Expert
VQA
2025.07 EN
Integration of existing datasets
Manual
N/A
Data review
N/A
620
MCQ
Acc
ReXVQA [871] [link]
Healthcare and Medical Sciences
X-ray
N/A
VQA
2025.06 EN
Integration of existing datasets
Semi-automated
3
Data review
GPT-4o,
ClinicalBERT,
MedEmbed
40,557
MCQ
Acc
HealthBench [772] [link]
Healthcare and Medical Sciences
Clinical dialogue, Medical task re-
quests, Medical record summariza-
tion, etc.
Expert
Text QA
2025.05 EN
Comprehensive multi-source inte-
gration
Semi-automated
262
Data generation and review
GPT-o1, GPT-4.1
5,000
Open-ended
Customized rubric crite-
rion
MedAlpaca [521] [link]
Healthcare and Medical Sciences
Biomedical knowledge base
Expert
Text QA
2025.03 EN
Web and Internet content
Semi-automated
N/A
Data review
GPT-3.5-Turbo
374
MCQ
Acc
GEMeX-VQA [875] [link]
Healthcare and Medical Sciences
X-ray
N/A
VQA
2025.03 EN
Integration of existing datasets
Semi-automated
N/A
Data review
OpenBioLLM-70B,
GPT-4o
3,960
MCQ,
True/False,
Open-ended
Acc
MIMIC-Diff-VQA [796] [link]
Healthcare and Medical Sciences
X-ray
Expert
VQA (multi-image)
2025.02 EN
Scientific databases
Semi-automated
3
Data generation and review
ScispaCy
70,070
MCQ,
Open-
ended
BLEU,
METEOR,
ROUGE-L, CIDEr
MedAgentBench [776] [link]
Healthcare and Medical Sciences
EHR, Lab results, Diagnosis codes,
Medication orders
Expert
Text QA
2025.01 EN
Academic and research resources
Manual
2
Data generation and review
N/A
300
Open-ended
Success rate
MedXpertQA [771] [link]
Healthcare and Medical Sciences
CT, ECG, Histopathology, MRI,
US, X-ray, etc.
Expert
VQA, Text QA
2025.01 EN
Academic and research resources
Semi-automated
N/A
Data generation and review
GPT-4o, Claude
4,460
MCQ
Acc
OpenMM-Medical [968] [link]
Healthcare and Medical Sciences
CT, Dermatology, Endoscopy, CFP,
MRI, Microscopy, X-ray, etc.
N/A
VQA
2025.01 EN, ZH
Comprehensive multi-source inte-
gration
Semi-automated
N/A
Data review
GPT-4o
88,996
MCQ
Acc
Asclepius [969] [link]
Healthcare and Medical Sciences
CT,
Dermatology,
CFP,
Histopathology, MRI, Microscopy,
OCT, X-ray, etc.
N/A
VQA, Image-text
2024.11 EN
Comprehensive multi-source inte-
gration
Semi-automated
34
Data generation and review
ChatGPT,
GPT-4V,
GPT-4o
3,232
MCQ
Acc
ClinicalBench [970] [link]
Healthcare and Medical Sciences
EHR
N/A
Text QA
2024.11 EN
Integration of existing datasets
N/A
N/A
N/A
N/A
N/A
MCQ
F1, AUROC
WorldMedQA-V [971] [link]
Healthcare and Medical Sciences
Dermatology, Microscopy, X-ray,
etc.
N/A
VQA
2024.10 EN,
JA,
ES,
HE,
PT
Academic and research resources
Semi-automated
N/A
Data review
GPT-4o,
Gemini
Flash1-5,
Yi-VL-
34B
568
MCQ
Acc
CRAFT-BioQA [972] [link]
Healthcare and Medical Sciences
Biomedical QA
N/A
Text QA
2024.09 EN
Academic and research resources
Automated
N/A
N/A
N/A
N/A
MCQ
Acc
MedTrinity-25M [882] [link]
Healthcare and Medical Sciences
CT, MRI, X-ray, Histopathology,
etc.
Expert
Image-text, VQA
2024.08 EN
Integration of existing datasets, Sci-
entific databases
Automated
N/A
N/A
N/A
100,000
Open-ended
Acc
GMAI-MMBench [973] [link]
Healthcare and Medical Sciences
CT, Dermatology, Endoscopy, CFP,
Histopathology, MRI, Microscopy,
OCT, PET, US, X-ray, etc.
N/A
VQA
2024.08 EN
Comprehensive multi-source inte-
gration
Semi-automated
N/A
Data review
GPT-4o
26k
MCQ
Acc
SlideBench [152] [link]
Healthcare and Medical Sciences
Histopathology
N/A
VQA
2024.11 EN
Scientific databases
Semi-automated
N/A
Data generation and review
GPT-4o
16k
MCQ,
Open-
ended
Acc, BLEU
Bio-ML [974] [link]
Healthcare and Medical Sciences
Ontology data
Expert
Text QA
2024.07 EN
Encyclopedias
and
knowledge
bases
Semi-automated
N/A
Data generation and review
N/A
25,270
Retrieval
F1
MedBench [770] [link]
Healthcare and Medical Sciences
Dianosis report, Clinical dialogue,
EHR
Expert
Text QA
2024.06 ZH
Integration of existing datasets
Manual
N/A
Data generation
N/A
300,901
MCQ,
Open-
ended
BLEU,
ROUGE-L,
F1,
Acc
ClinicalLab [802] [link]
Healthcare and Medical Sciences
Clinical notes
Expert
Text QA
2024.06 EN, ZH
Other sources
Manual
N/A
Data generation and review
GPT-4
1,500
Open-ended
DWR, DIFR, CDR, Ac-
ceptability, Acc, BLEU,
ROUGE, BERTScore
AgentClinic-NEJM [777] [link]
Healthcare and Medical Sciences
Clinical dialog, Diagnosis report,
CT, Dermatology, Histopathology,
etc.
Expert
VQA
2024.05 EN
Academic and research resources,
Comprehensive multi-source inte-
gration
Automated
N/A
N/A
N/A
120
Open-ended
Acc, Patient compliance,
Consultation ratings
AgentClinic-Lang [777] [link]
Healthcare and Medical Sciences
Medical exams
Expert
Text QA
2024.05
EN,
ES,
FA,
FR,
HI,
KO,
ZH
Academic and research resources,
Comprehensive multi-source inte-
gration
Semi-automated
N/A
Data review
GPT-4
749
Open-ended
Acc, Patient compliance,
Consultation ratings
AgentClinic-MedQA [777] [link]
Healthcare and Medical Sciences
Medical exams
Expert
Text QA
2024.05 EN
Academic and research resources,
Comprehensive multi-source inte-
gration
Semi-automated
N/A
Data review
GPT-4
215
Open-ended
Acc, Patient compliance,
Consultation ratings
AgentClinic-MIMIC-IV [777] [link]
Healthcare and Medical Sciences
EHR
Expert
Text QA
2024.05 EN
Scientific databases
Semi-automated
N/A
Data review
GPT-4
200
Open-ended
Acc, Patient compliance,
Consultation ratings
AgentClinic-Spec [777] [link]
Healthcare and Medical Sciences
Medical exams
Expert
Text QA
2024.05 EN
Integration of existing datasets
Semi-automated
N/A
N/A
GPT-4
260
Open-ended
Acc, Patient compliance,
Consultation ratings
M3D-Bench [660] [link]
Healthcare and Medical Sciences
CT, Clinical reports
Expert
Image-text, Text QA,
VQA
2024.04 EN
Scientific databases, Integration of
existing datasets
Semi-automated
N/A
Data generation and review
GPT-4V
1,235
MCQ,
Open-
ended, Retrieval
Acc, BLEU, ROUGE
AMOS-MM [156] [link]
Healthcare and Medical Sciences
CT
Expert
Image-text, VQA
2024.04 EN, ZH
Integration of existing datasets, Sci-
entific databases
N/A
N/A
N/A
N/A
2300
Open-ended,
MCQ
Acc
CMtMedQA [530] [link]
Healthcare and Medical Sciences
Clinical dialogue
Expert
Text QA
2024.03 ZH
Books and literary works
Semi-automated
6
Data review
GPT-3.5,
CMeKG,
RLHF-Label-Tool
70k
Open-ended
GPT-4 score
Medbullets [975] [link]
Healthcare and Medical Sciences
Medical exams
N/A
Text QA
2024.02 EN
Social media and forums
Automated
N/A
Data review
N/A
618
MCQ
ROUGE-L,
BERTScore,
CTC,
G-Eval,
BARTScore+
RareBench [775] [link]
Healthcare and Medical Sciences
EHR, Medical history, Lab tests
Expert
Text QA
2024.02 EN, ZH
Scientific databases, Academic and
research resources, Other sources
Manual
N/A
Data generation and review
N/A
2,185
Open-ended
Precision, Recall, F1, Me-
dian Rank, etc.
OmniMedVQA [797] [link]
Healthcare and Medical Sciences
CT, Dermatology, Endoscopy, CFP,
Histopathology, MRI, Microscopy,
OCT, PET, US, X-ray, etc.
N/A
VQA
2024.02 EN
Comprehensive multi-source inte-
gration
Semi-automated
N/A
Data review
GPT-4
127,995
MCQ
Acc
MultiMedEval [976] [link]
Healthcare and Medical Sciences
CT,
Dermatology,
CFP,
Histopathology, MRI, Microscopy,
OCT, US, X-ray, etc.
N/A
VQA
2024.02 EN
Integration of existing datasets
Semi-automated
N/A
Data review
CheXbert, GPT, Rad-
Graph
60k
MCQ
Acc
Fhirfly Medical Questions [link]
Healthcare and Medical Sciences
Biomedical QA
N/A
Text QA
2024.01 EN
Academic and research resources
Semi-automated
N/A
Data review
N/A
25,102
True/False
Acc
RP3D-DiagDS [774] [link]
Healthcare and Medical Sciences
CT, MRI, X-ray, US, Fluoroscopy,
etc.
Expert
Classification
2023.12 EN
Scientific databases
Semi-automated
N/A
Data generation and review
Custom
crawlers,
GPT-4
40,936
True/False
AUROC, AP
NEJM-AI Benchmarking [977] [link]
Healthcare and Medical Sciences
Medical exams
Expert
Text QA
2023.11 EN
Academic and research resources
Automated
N/A
N/A
NLTK, Regex
858
MCQ
Acc, BLEU, WER, Cosine
MORFITT [897] [link]
Healthcare and Medical Sciences
Clinical papers
Expert
Classification
2023.11 FR
Academic and research resources
Manual
N/A
Data review
N/A
1,560
Classification
Precision, Rappel, F1
SourceData [935] [link]
Healthcare and Medical Sciences
Gene/protein entities
Expert
Raw text
2023.10 EN
Academic and research resources
Manual
N/A
Data generation and review
N/A
620,000
NER
Precision, Recall, F1
SDOH-NLI [900] [link]
Healthcare and Medical Sciences
Clinical notes
Expert
Classification
2023.10 EN
Integration of existing datasets
Manual
N/A
Data generation
N/A
4.21k
Classification
Precision, Recall, F1
HealthsearchQA [15] [link]
Healthcare and Medical Sciences
Consumer health QA
Expert
Text QA
2023.08 EN
Web and Internet content
Semi-automated
N/A
Data review
N/A
3,173
Open-ended
Factuality,
Comprehen-
sion, Reasoning, Possible
harm and bias
CMB-Exam [816] [link]
Healthcare and Medical Sciences
Medical exams
Expert
Text QA
2023.08 ZH
Web and Internet content
Semi-automated
N/A
Data review
N/A
280,839
MCQ
Acc
CMB-Clin [816] [link]
Healthcare and Medical Sciences
Medical exams
Expert
Text QA
2023.08 ZH
Books and literary works
Semi-automated
N/A
Data review
N/A
208
Open-ended
Fluency, Relevance, Com-
pleteness, Proficiency
MultiMedBench [978] [link]
Healthcare and Medical Sciences
CT, Dermatology, Histopathology,
Microscopy, MRI, X-ray, etc.
N/A
Text QA, VQA
2023.07 Mixed
Integration of existing datasets
N/A
N/A
N/A
N/A
1M
N/A
Acc, ROUGE-L, BLEU,
F1-RadGraph, F1
GPT-4 BiasBenchmark [979] [link]
Healthcare and Medical Sciences
Clinical trials
Expert
Text QA
2023.07 EN
Academic and research resources
Semi-automated
N/A
Data generation and review
GPT-4
213
Open-ended
Acc
Lavita Medical QA [980] [link]
Healthcare and Medical Sciences
Clinical guidelines
N/A
Text QA
2023.07 EN
Academic and research resources
Automated
N/A
N/A
N/A
11,500
MCQ
Acc
BioASQ10b-factoid [769] [link]
Healthcare and Medical Sciences
Clinical dialogue, PubMed snippets Expert
Text QA
2023.07 EN
Scientific databases, Academic and
research resources
Manual
N/A
Data generation and review
N/A
166
Open-ended
Acc, MRR
MedNERF [981] [link]
Healthcare and Medical Sciences
Drug Prescription
Expert
Classification
2023.06 FR
Other sources
Manual
N/A
Data generation and review
N/A
100
NER
F1
WikiMedQA [912] [link]
Healthcare and Medical Sciences
Clinical reports
Expert
Text QA
2023.03 EN
Web and Internet content
Semi-automated
N/A
N/A
SentenceBERT,
BioLinkBERT
5,893
MCQ
Acc
BioASQ [769] [link]
Healthcare and Medical Sciences
Biomedical Documents
Expert
Text QA
2022.12 EN
Academic and research resources
Manual
21
Data generation and review
N/A
4,721
Open-ended
Acc
BioRED [651] [link]
Healthcare and Medical Sciences
Biomedical papers
N/A
Classification
2022.09 EN
Scientific databases
Semi-automated
6
Data generation and review
PubTator
100
NER
Precision, Recall, F1
BioLeaflets [920] [link]
Healthcare and Medical Sciences
Package leaflets
Expert
Raw text
2021.09 EN
Web and Internet content
Semi-automated
N/A
Data generation
Stanza,
Amazon
Comprehend
Medical
134
Generation
SacreBLEU,
ROUGE-L,
BERTScore,
BLEURT,
MoverScore-21
CBLUE [921] [link]
Healthcare and Medical Sciences
Clinical trials, EHR, Medical fo-
rum, Medical textbooks
N/A
Classification,
Text
QA
2021.06 ZH
Comprehensive multi-source inte-
gration
Manual
3
Data generation and review
N/A
46,729
NER,
Open-
ended, Retrieval
Acc, F1
SLAKE [773] [link]
Healthcare and Medical Sciences
CT, MRI, X-ray
N/A
VQA
2021.02 EN, ZH
Academic and research resources
Automated
N/A
N/A
N/A
2,070
MCQ,
Open-
ended
Acc
MEDIQA-AnS [799] [link]
Healthcare and Medical Sciences
Consumer health QA
Undergraduate Text QA
2020.09 EN
Web and Internet content
Manual
2
Data generation
N/A
708
Open-ended
ROUGE, BLEU
RadVisDial (G) [982] [link]
Healthcare and Medical Sciences
X-ray
N/A
VQA
2020.07 EN
Integration of existing datasets
Semi-automated
2
Data generation
NegBio, CheXpert
91k
MCQ
Acc
CORD-19 [590] [link]
Healthcare and Medical Sciences
Academic papers
N/A
Text QA
2020.03 EN
Academic and research resources
N/A
N/A
N/A
N/A
280K
Retrieval, QA
MRR, Acc
PathVQA [150] [link]
Healthcare and Medical Sciences
Histopathology
Expert
VQA
2020.03 EN
Academic and research resources
Automated
N/A
N/A
CoreNLP
6,012
MCQ,
Open-
ended
BLEU, Exact-match, F1
MedQuAD [926] [link]
Healthcare and Medical Sciences
Patient educational materials
Undergraduate Text QA
2019.11 EN
Web and Internet content
Semi-automated
2
Data generation
MetaMap
Lite,
UMLS lookup
47,457
Open-ended
Acc, F1, MRR
Pubmed Causal [983] [link]
Healthcare and Medical Sciences
Biomedical papers
N/A
Classification
2019.11 EN
Scientific databases
Manual
N/A
Data generation
N/A
2,446
Classification
Acc, F1
PubMedQA instruction [450] [link]
Healthcare and Medical Sciences
Clinical dialogue
Expert
Text QA
2019.09 EN
Academic and research resources
Manual
N/A
Data generation
N/A
273k
Classification
Acc
VQA-RAD [705] [link]
Healthcare and Medical Sciences
CT, MRI, PET, US, X-ray
N/A
VQA
2018.11 EN
Academic and research resources
Manual
N/A
Data generation
N/A
451
MCQ,
Open-
ended
Acc, BLEU
Pima [655] [link]
Healthcare and Medical Sciences
EHR
Expert
Classification
1988.11 EN
Scientific databases
Manual
N/A
N/A
N/A
77
Classification
AUROC
TOMG-Bench [763] [link]
Molecular and Cellular Biology
Molecule
Expert
Text QA
2024.12 EN
Scientific databases
Automated
N/A
N/A
N/A
45,000
Open-ended
Success Rate, Similarity,
Novelty, Validity
MoleculeQA [764] [link]
Molecular and Cellular Biology
Molecule
Expert
Text QA
2024.11 EN
Scientific databases
Manual
2
Data generation and review
N/A
62,000
MCQ
Acc
BEACON [696] [link]
Molecular and Cellular Biology
RNA sequence
N/A
Raw text
2024.06 EN
Comprehensive multi-source inte-
gration
Semi-automated
N/A
Data generation and review
N/A
96,283
Classification,
Regression
F1,
AUROC,
Precision,
R2, MSE, PCC
GeneHop [984] [link]
Molecular and Cellular Biology
Multi-hop genomic QA
N/A
Text QA
2023.04 EN
Academic and research resources
Manual
N/A
Data generation and review
N/A
150
Open-ended
Acc
PCdes [627] [link]
Molecular and Cellular Biology
SMILES
N/A
Text QA
2022.12 EN
Academic and research resources
Automated
N/A
N/A
Custom crawlers
3,000
Retrieval
Acc, Recall
PEER [695] [link]
Molecular and Cellular Biology
Protein sequence
Expert
Classification,
Regression
2022.10 EN
Comprehensive multi-source inte-
gration
Semi-automated
N/A
Data generation and review
N/A
115,281
Classification,
Regression
Acc,
RMSE,
Precision,
PCC
BioPreDyn-bench [985] [link]
Molecular and Cellular Biology
Time-series (simulation data)
Expert
Regression
2015.02 EN
Academic and research resources
N/A
N/A
N/A
6
6
Open-ended
NRMSE
Continued on next page
62

TABLE V continued from previous page
Scientific
Domain
Dataset
Domain
Modality
Level
Type
Release Language Source
Annotation
Pipeline
Human
Annotators
Human Tasks
Auto-annotation
Tools
Size
Evaluation
Type
Metrics
MicroVQA [147] [link]
Molecular
and
Cellular
Biology,
Healthcare and Medical Sciences
Microscopy
Expert
VQA
2025.03 EN
Academic and research resources
Semi-automated
12
Data generation and review
GPT-4o
1042
MCQ
Acc
DISEASES [803] [link]
Molecular
and
Cellular
Biology,
Healthcare
and
Medical
Sciences,
Multi-omics
Disease-gene associations
Expert
Classification
2015.01 EN
Academic and research resources,
Integration of existing datasets, Sci-
entific databases
Semi-automated
N/A
Data generation and review
NER tagger
8,336,442
Open-ended,
True/False,
Retrieval
Precision, Recall, F1, AU-
ROC, AUPRC
LAB-Bench [765] [link]
Molecular and Cellular Biology, Multi-
omics, Neuroscience
Research problems
N/A
Text QA
2024.07 EN
Academic and research resources
N/A
N/A
N/A
N/A
2,457
MCQ
Acc
BioProBench [986] [link]
Molecular and Cellular Biology, Multi-
omics, Pharmacy, Neuroscience, etc.
Protocol
N/A
Text QA
2025.05 EN
Academic and research resources
Semi-automated
N/A
Data review
N/A
556,171
Open-ended
Acc, F1, EM, BLEU
Genome-Bench [767] [link]
Multi-omics
Research problems
N/A
Text QA
2025.06 EN
Academic and research resources
N/A
N/A
Data generation and review
GPT-4 Turbo, GPT-
4o
3,332
MCQ
Acc
GeneChat-test [637] [link]
Multi-omics
Nucleotide sequence
N/A
Text QA
2025.06 EN
Scientific databases
N/A
N/A
Data generation
N/A
N/A
Open-ended
BLUE, METEOR
GeneChat [637] [link]
Multi-omics
Nucleotide sequence
N/A
Text QA
2025.06 EN
Scientific databases
N/A
N/A
Data generation
N/A
2,973
Open-ended
BLEU, METEOR
Genomics instructions [511] [link]
Multi-omics
Nucleotide sequence
N/A
Text QA
2025.04 EN
Academic and research resources
N/A
N/A
Data generation
N/A
403,814
Classification,
Regression
F1, MCC, AUROC, PCC
BixBench [987] [link]
Multi-omics
Genomics transcriptomics text
Expert
Text QA
2025.03 EN
Academic and research resources
Semi-automated
Data
generation
and review
53
Claude 3.5 Sonnet
296
Open-ended,
MCQ
Acc
Seq2Func [939] [link]
Multi-omics
Nucleotide sequence
N/A
Text QA
2025.02 EN
Scientific databases
Automated
N/A
Data generation
N/A
33,000
MCQ
MCC, F1
DNA2Image [939] [link]
Multi-omics
Nucleotide sequence
N/A
Generation
2025.02 EN
Scientific databases
Automated
N/A
Data generation
N/A
4,800
Generation
Invalid percentage, F1
DNA Long Bench [988] [link]
Multi-omics
DNA sequence
N/A
Classification,
Regression
2025.01 EN
Scientific databases; Academic and
research resources
Automated
N/A
N/A
N/A
213,416
Classification,
Regression
SCC, PCC, AUROC
LLaMA-Gene (protein) [40] [link]
Multi-omics
Protein sequence
N/A
Text QA
2024.12 EN
Scientific databases
N/A
N/A
Data generation
N/A
6,991
Open-ended
Acc
LLaMA-Gene (DNA) [40] [link]
Multi-omics
DNA sequence
N/A
Text QA
2024.12 EN
Scientific databases
N/A
N/A
Data generation
N/A
19,839
Open-ended
Acc
NT Benchmark [319] [link]
Multi-omics
Nucleotide sequence
N/A
Classification
2024.10 EN
Academic and research resources
N/A
N/A
N/A
N/A
38,822
MCQ
MCC
BioinformaticsBench [989] [link]
Multi-omics
Textbook
Undergraduate Text QA
2024.06 EN
Books and literary works, Aca-
demic and research resources
Semi-automated
4
N/A
GPT-3.5,
GPT-4,
GPT-4 Turbo
602
MCQ,
True/False,
Open-ended
Acc
genomics-long-range-
benchmark [762] [link]
Multi-omics
Nucleotide sequence
N/A
Classification,
Regression
2024.05 EN
Academic and research resources
N/A
N/A
N/A
N/A
N/A
Classification,
Regression
MCC
RNA-QA [641] [link]
Multi-omics
RNA sequence
N/A
Text QA
2024.05 EN
Academic and research resources
Automated
N/A
N/A
N/A
121 K
Open-ended
Precision,
Recall,
F1,
ROUGE
BioinfoBench [990] [link]
Multi-omics
RNA sequence
Undergraduate Text QA
2023.10 EN
Other sources
Semi-automated
N/A
Data review
ChatGPT
200
MCQ
Acc,
Perplexity,
Next-
token likelihood
BioCoder [121] [link]
Multi-omics
Codes
Undergraduate Text QA
2023.08 EN
Integration
of
existing
datasets,
Academic and research resources
Automated
N/A
N/A
N/A
2522
Open-ended
Acc
SpeciesClassification [991] [link]
Multi-omics
Nucleotide sequence
N/A
Classification
2023.06 EN
Academic and research resources
N/A
N/A
N/A
N/A
5
species
genomes
MCQ
Acc
GUE Benchmark [318] [link]
Multi-omics
Nucleotide sequence
N/A
Classification
2023.06 EN
Academic and research resources
N/A
N/A
N/A
N/A
80,648
MCQ
MCC, F1
Genomic Benchmark [939] [link]
Multi-omics
Nucleotide sequence
N/A
Classification
2023.05 EN
Academic and research resources
N/A
N/A
N/A
N/A
191,589
MCQ
Acc, F1
GeneTuring [766] [link]
Multi-omics
Biomedical knowledge base
N/A
Text QA
2023.03 EN
Academic and research resources
N/A
N/A
Data generation
GPT-2,
BioGPT,
BioMedLM, GPT-3,
ChatGPT, New Bing
600
MCQ
Acc
Human Pancreas [940] [link]
Multi-omics
scRNA-seq
N/A
Classification
2023.01 EN
Academic and research resources
N/A
N/A
N/A
N/A
4,218
Classification
Acc, Precision, Recall, F1
Myeloid [943] [link]
Multi-omics
scRNA-seq
N/A
Classification
2021.02 EN
Academic and research resources
N/A
N/A
N/A
N/A
3,430
Classification
Acc, Precision, Recall, F1
Human Cell Atlas Dataset [944] [link]
Multi-omics
scRNA-seq
N/A
Classification
2021.02 EN
Academic and research resources
N/A
N/A
N/A
N/A
84,363
Classification
Acc, F1
Human enhancers Ensembl [761] [link] Multi-omics
Nucleotide sequence
N/A
Classification
2021.01 EN
Academic and research resources
N/A
N/A
N/A
N/A
154,842
MCQ
MCC
Human
regulatory
En-
sembl [761] [link]
Multi-omics
Nucleotide sequence
N/A
Classification
2021.01 EN
Academic and research resources
N/A
N/A
N/A
N/A
289,061
MCQ
MCC
Human ocr Ensembl [761] [link]
Multi-omics
Nucleotide sequence
N/A
Classification
2021.01 EN
Academic and research resources
N/A
N/A
N/A
N/A
174,756
MCQ
MCC
Multiple Sclerosis [946] [link]
Multi-omics
scRNA-seq
N/A
Classification
2019.07 EN
Academic and research resources
N/A
N/A
N/A
N/A
13,468
Classification
Acc, Precision, Recall, F1
APARENT [805] [link]
Multi-omics
Nucleotide sequence
N/A
Regression
2019.06 EN
Academic and research resources
N/A
N/A
N/A
N/A
8,000
Regression
R2
Human enhancers Cohn [939] [link]
Multi-omics
Nucleotide sequence
N/A
Classification
2018.02 EN
Academic and research resources
N/A
N/A
N/A
N/A
27,791
MCQ
MCC
Human
non-TATA
promot-
ers [992] [link]
Multi-omics
Nucleotide sequence
N/A
Classification
2017.02 EN
Academic and research resources
N/A
N/A
N/A
N/A
36,131
MCQ
MCC
Zheng68k [948] [link]
Multi-omics
scRNA-seq
N/A
Classification
2016.07 EN
Academic and research resources
N/A
N/A
N/A
N/A
68,450
Classification
Acc, F1
Drosophila
enhancers
Stark [993] [link]
Multi-omics
Nucleotide sequence
N/A
Classification
2014.06 EN
Academic and research resources
N/A
N/A
N/A
N/A
6,914
MCQ
MCC
COMET [308] [link]
Multi-omics
DNA,
RBA,
Protein
Sequence/Residue
N/A
Classification,
Regression
2024.12 EN
Academic and research resources
N/A
N/A
N/A
N/A
1.22M
Classification,
Regression
R2, PCC, F1, SCC
AdaBrain-Bench [994] [link]
Neuroscience
EEG
N/A
Classification
2025.07 EN
Integration of existing datasets
N/A
N/A
N/A
N/A
N/A
Open-ended
Acc,
AUROC,
AUPRC,
F1, PCC, R2
FDA Pharmaceuticals FAQ [995] [link] Pharmacy
FAQ-style text
Expert
Text QA
2023.03 EN
Web and Internet content
Automated
N/A
N/A
N/A
1,681
MCQ
Acc
repoDB [804] [link]
Pharmacy, Healthcare and Medical Sci-
ences
Drug-disease relationships, Clinical
trial outcomes
Expert
Classification,
Text
QA
2017.03 EN
Scientific databases
Automated
N/A
N/A
scripts
15,648
MCQ, Retrieval
AUROC, AUPRC, Acc
Chemistry
OmniGenBench [996] [link]
Biochemistry, Multi-omics
DNA sequence, RNA sequence, TF
binding, etc.
N/A
Classification
2025.05 N/A
Integration
of
existing
datasets,
Academic and research resources
N/A
N/A
N/A
N/A
N/A
N/A
AUROC, F1, RMSE, R2
MOSES [607] [link]
Biochemistry
SMILES
Expert
Raw text
2020.07 EN
Academic and research resources
Manual
N/A
Data review
N/A
1,936,962
Generation
Chemical validity, Drug-
likeness
ChEMBL [217] [link]
Biochemistry
SMILES
Expert
Raw text
2012.01 EN
Academic and research resources
Manual
N/A
Data generation and review
N/A
1.96M
Generation
Chemical validity, Drug-
likeness
ChemRxivQuest [950] [link]
General Chemistry
Academic papers
Expert
Text QA
2025.05 EN
Academic and research resources
Manual
N/A
Data generation and review
NA
970
Open-ended
Acc
ScholarChemQA [106] [link]
General Chemistry
Academic papers
Expert
Text QA
2025.02 EN
Academic and research resources
Manual
N/A
Data generation and review
N/A
40K
MCQ
Acc
ChemSafetyBench [753]
General Chemistry
Text
Expert
Raw text
2024.11 EN
Academic and research resources
Automated
N/A
Data generation and review
NA
30K+
Open-ended
Acc, Recall, Precision, F1,
safety/quality score, etc.
ChemEval [752]
General Chemistry
Text
Expert
Raw text
2024.09 EN
Academic and research resources
Automated
N/A
Data generation and review
NA
unknown (42
tasks)
Open-ended
Acc, BLEU-2, F1, etc.
ChemNLP [951] [link]
General Chemistry
Text
Secondary
school
Text QA
2023.01 EN
Academic and research resources
Manual
N/A
Data generation and review
N/A
27.6K
Classification,
NER, Generation Acc, ROUGE
ZINC [216] [link]
General Chemistry
SMILES
Expert
Raw text
2012.10 EN
Academic and research resources
Manual
N/A
Data review
N/A
250K
Generation
Chemical validity, Drug-
likeness
PMO [215] [link]
General Chemistry
SMILES
Expert
Raw text
2022.05 EN
Academic and research resources
Automated
N/A
Data generation and review
N/A
10K
Open-ended
target property, Chemical
validity, Drug-likeness
DeepProtein [952] [link]
Pharmacy
Protein sequence, SMILES
Expert
Raw text
2025.05 EN
Academic and research resources
Automated
N/A
Data generation and review
N/A
78K
Classification,
Regression
Acc, MAE, F1, AUPRC,
AUROC, R2, etc.
TrialBench [754] [link]
Pharmacy
SMILES, Disease code
Expert
Raw text
2024.09 EN
Academic and research resources
Automated
N/A
Data generation and review
N/A
470K
Open-ended
F1,
Recall,
Precision,
MSE, etc.
TDC2 [953] [link]
Pharmacy
SMILES,
Protein
sequence,
Genome sequence
Expert
Raw text
2024.09 EN
Academic and research resources
Manual
N/A
Data generation and review
NA
3.4B tokens
Open-ended
F1,
Recall,
Precision,
MSE, etc.
PCQM4Mv2 [997] [link]
Pharmacy
Molecular graph
N/A
Regression
2022.11 EN
Academic and research resources
Automated
N/A
N/A
N/A
3,746,619
Regression
MAE
SBDDBench [954] [link]
Pharmacy
Protein sequence, SMILES
Expert
Protein-ligand
2022.06 EN
Academic and research resources
Automated
N/A
Data generation and review
N/A
5K
Open-ended
binding affinity, Chemical
validity, Drug-likeness
GEOM [998] [link]
Pharmacy
3D conformation
N/A
Regression
2022.04 EN
Academic and research resources
Automated
N/A
N/A
CREST
(GFN2-
xTB)
37M
confor-
mations
Regression
MAE, RMSD
TOP [955] [link]
Pharmacy
SMILES
Expert
Raw text
2022.02 EN
Academic and research resources
Automated
N/A
Data generation and review
N/A
12K
Open-ended
F1, Recall, AUPRC, etc.
TDC [244] [link]
Pharmacy
SMILES,
Protein
sequence,
Genome sequence
Expert
Raw text
2021.06 EN
Academic and research resources
Manual
N/A
Data generation and review
NA
0.2B tokens
Open-ended
F1,
Recall,
Precision,
MSE, etc.
DeepPurpose [611] [link]
Pharmacy
Protein sequence, SMILES
Expert
Raw text
2020.12 EN
Academic and research resources
Automated
N/A
Data generation and review
N/A
5,074
Classification,
Regression
MSE, PCC, F1, AUROC,
AUPRC, etc.
DrugBank [956] [link]
Pharmacy
SMILES
Expert
Raw text
2018.01 EN
Academic and research resources
Manual
N/A
Data generation and review
N/A
17.47K
Open-ended
Acc
USPTO [613]
Synthetic Chemistry
SMILES
Expert
Raw text
2015.07 EN
Patent databases
Manual
N/A
Data generation and review
NA
1,939,253
Open-ended
Acc, F1, MSE, etc.
Physics
FSReD [223] [link]
General Physics
Text
Expert
Text QA
2019.05 EN
Comprehensive multi-source inte-
gration
Automated
N/A
Data review
N/A
120
Regression
MSE, Exact Match
PIQA [681] [link]
General Physics
Text
Primary
school
Text QA
2020.01 EN
Other sources
Semi-automated
N/A
Data generation and review
N/A
2,000
MCQ
Acc
SRBench [747] [link]
General Physics
Text
N/A
Text QA
2021.07 EN
Comprehensive multi-source inte-
gration
Semi-automated
N/A
Data generation and review
N/A
252
Open-ended
Acc,
Simplicity,
Exact
Match
PROST [738] [link]
General Physics
Text
N/A
Text QA
2021.08 EN
Other sources
Semi-automated
4
Data generation
N/A
18,736
MCQ
Acc
MM-PhyQA [736] [link]
Kinematics, Mechanics, Electrostatics
and Current Electricity, Thermodynam-
ics, Optics, Magnetism, etc.
Text
High school
VQA with CoT
2024.04 EN
Comprehensive multi-source inte-
gration
Semi-automated
8+
Data generation and review
ChatGPT
675
MCQ
Acc, ROUGE
MVBench [751] [link]
General Physics
Video
N/A
Video QA
2024.05 EN
Comprehensive multi-source inte-
gration
Automated
0
Data review
N/A
4,000
MCQ
Acc
UGPhysics [741] [link]
Mechanics, Thermodynamics, Electro-
magnetism, Modern Physics
Text (problem statements, equa-
tions, reasoning)
Undergraduate Text QA
2025.01 EN, ZH
Academic and research resources
Semi-automated
N/A
Data generation and review
GPT-4o
11,040
MCQ,
Open-
ended,
True/False,
Retrieval
Acc
PhysReason [740] [link]
Mechanics, Electromagnetism, Ther-
modynamics, etc.
Text (problem statements, equa-
tions), Diagrams (physics illustra-
tions)
Undergraduate,
Graduate,
Expert
Text QA, VQA
2025.02 EN
Comprehensive multi-source inte-
gration
Semi-automated
4
Data generation and review
GPT-4
1,200
MCQ
Acc
TPBench [745] [link]
Cosmology, High Energy Theory, Gen-
eral Relativity, Astrophysics, Electro-
magnetism, Quantum Mechanics, Me-
chanics, etc.
Text
N/A
Text QA
2025.02 N/A
Other sources
Manual
N/A
Data generation and review
N/A
57
Open-ended
Acc,
AI-based
Holistic
Grading
PHYSICS [743] [link]
Mechanics, Electromagnetism, Ther-
modynamics, Optics, etc.
Text (problem statements, equa-
tions, reasoning), Diagrams (illus-
trations, charts, experimental se-
tups)
Undergraduate Text QA, VQA
2025.03 EN
Comprehensive multi-source inte-
gration
Manual
N/A
Data generation and review
N/A
1,297
Open-ended
Acc
PhysicsArena [682] [link]
Mechanics, Electromagnetism, Ther-
modynamics, etc.
Text (problem statements, equa-
tions, reasoning), Diagrams (illus-
trations, charts, experimental se-
tups)
Expert
Text QA, VQA
2025.05 EN
Comprehensive multi-source inte-
gration
Semi-automated
N/A
Data generation and review
N/A
5,100
Open-ended
Acc
Continued on next page
63

TABLE V continued from previous page
Scientific
Domain
Dataset
Domain
Modality
Level
Type
Release Language Source
Annotation
Pipeline
Human
Annotators
Human Tasks
Auto-annotation
Tools
Size
Evaluation
Type
Metrics
PHYBench [746] [link]
Mechanics, Electricity, Thermodynam-
ics, Optics, Modern Physics, etc.
Research problems
Undergraduate Text QA
2025.05 EN
Comprehensive multi-source inte-
gration
Semi-automated
178
Data generation and review
o1, DeepSeek-R1
500
Open-ended
EED
PhyX [742] [link]
Mechanics,
Quantum
Mechanics,
Thermodynamics,
Electromagnetism,
Atomic Physics, etc.
Text (problem statements, equa-
tions, reasoning), Diagrams (illus-
trations, charts, experimental se-
tups)
Undergraduate Text QA, VQA
2025.05 EN
Comprehensive multi-source inte-
gration
Semi-automated
N/A
Data generation and review
GPT-4o
3,000
MCQ,
Open-
ended
Acc
PhysUniBench [739] [link]
Mechanics, Electromagnetism, Optics,
Atomic Physics, etc.
Text (problem statements, equa-
tions), Diagrams (physics illustra-
tions)
Undergraduate VQA
2025.06 EN, ZH
Comprehensive multi-source inte-
gration
Manual
N/A
Data generation and review
N/A
3,304
Open-ended,
MCQ
Acc
IntPhys 2 [749] [link]
General Physics
Video, Text (scene parameters, ob-
ject categories, trajectories, physi-
cal attributes)
N/A
Video QA
2025.06 N/A
Other sources
Semi-automated
N/A
Data generation and review
N/A
1,400
Open-ended
Acc
MVP-Bench [750] [link]
General Physics
Video
N/A
Video QA
2025.06 EN
Encyclopedias
and
knowledge
bases
Semi-automated
N/A
Data generation and review
OpenAI CLIP (ViT-
L/14)
55,000
Open-ended
Acc
SeePhys [744] [link]
Mechanics, Electromagnetism, Parti-
cle Physics, Optics=, Astrophysics,
Thermodynamics, Quantum Mechan-
ics, etc.
Text (problem statements, equa-
tions), Diagrams (physics illustra-
tions)
Secondary
school,
Un-
dergraduate,
Graduate
VQA
2025.07 EN,ZH
Comprehensive multi-source inte-
gration
Semi-automated
N/A
Data generation and review
GPT-4o
2,000
Open-ended
Acc
Astronomy
Astro-QA [780] [link]
Astronomy
Astronomy
Olympiad
competitions, Astronomy exams,
Online encyclopedias
Undergraduate Text QA
2025.06 Mixed
Comprehensive multi-source inte-
gration
Manual
30+
Data generation and review
N/A
3,082
Open-ended
DGscore,
BLEU,
ROUGE, chrF
Astrovisbench [999] [link]
Astronomy
Galaxy images
Expert
VQA
2025.06 EN
Comprehensive multi-source inte-
gration
Semi-automated
6
Data review
GPT-4o, Claude 3.5
Sonnet
432
Open-ended
VIscore, Image error level,
Expert evaluation
AstroMLab 1 [779] [link]
Astronomy
Academic papers
Expert
Text QA
2024.11 EN
Academic and research resources
Automated
N/A
Data review
Gemini-1.5-Pro
4,425
MCQ
Acc
AstroPT [670] [link]
Astronomy
Astronomical images
Expert
Image-text
2024.05 EN
Web and Internet content, Scientific
databases
Automated
N/A
Data review
DESI Legacy Survey
API
8.6 M
Classification
PCC, Acc
Astro-NER [726] [link]
Astronomy
Academic papers
Expert
Text QA
2024.05 EN
Academic and research resources
Semi-automated
4
Data generation and review
GPT-3.5
5,000
Open-ended
Precision, Recall, F1
AstroLLaMA [562] [link]
Astronomy
Academic papers
Expert
Text QA
2023.09 EN
Academic
and
research
resources,Web and Internet content Manual
N/A
Data review
N/A
9.5 M
Open-ended
Perplexity, Cosine similar-
ity
ATel [958] [link]
Astronomy
Academic papers
Expert
Text QA
2023.05 EN
Academic and research resources
Manual
N/A
Data review
N/A
234
Open-ended
Acc
PhyE2Es [221] [link]
Astrophysics
Text with formulae
Expert
Raw text
2025.03 EN
Scientific databases
Automated
N/A
Data generation and review
OpenLLAMA-2-3B
8,000
Regression
Acc, Numerical precision,
Formula complexity, For-
mula depth
Pathfinder Dataset [783] [link]
Astrophysics
Academic papers, ADS
Expert
Text QA with CoT
2024.11 EN
Web and Internet content, Aca-
demic and research resources
Automated
36+
Data generation and review
text-embedding-3-
small
385,166
Open-ended
Acc,
MRR,
Recall,
NDCG, relevance score
Starwhisper-pilsar [781] [link]
Astrophysics
Pulsar diagnostic plots, Pulsars sig-
nals
Expert
VQA
2024.04 EN
Integration of existing datasets
Manual
N/A
Data generation and review
DeepSeek-VL-7B,
InternVL2-40B
106,674
Open-ended
Acc, Recall, Precision, F1,
etc.
PAPERCLIP [782] [link]
Astrophysics
Synthetic conversation, Astronomi-
cal images
Expert
Text QA
2024.03 EN
Academic
and
research
resources,Scientific databases
Automated
N/A
Data generation and review
Mixtral-8x7B-
Instruct
31,859
Open-ended
Acc
Materials Science CheMatAgent [120] [link]
Materials Science
Scientific instruction
Expert
Text QA
2025.06 EN
Other sources
Manual
N/A
Data generation and review
N/A
137
Open-ended
Acc
ChEBI-20-MM [693] [link]
Materials Science
InChI, IUPAC, SELFIES, Science
QA, Molecular Image
Expert
Text QA
2025.01 EN
Integration of existing datasets
Manual
N/A
Data generation and review
N/A
3,300
Open-ended
BLEU,
ROUGE,
METEOR, CIDEr
LLM4MatBench [757] [link]
Materials Science
CIF, Chemical composition, Nu-
merical property
Expert
Text QA
2024.10 EN
Scientific databases
Manual
N/A
Data generation and review
N/A
1.9M
Open-ended
Acc
MatText [1000] [link]
Materials Science
Chemical composition, Numerical
property
Expert
Text QA
2024.08 EN
Scientific databases
Manual
N/A
Data generation and review
N/A
2,000,000
Open-ended
MAE, AUROC
MatBookQA [758] [link]
Materials Science
Science QA
Expert
Text QA
2024.05 EN
Academic and research resources
Manual
N/A
Data generation and review
N/A
650
Open-ended
Acc
MaSCQA [109] [link]
Materials Science
Science QA
Expert
Text QA
2023.08 EN
Academic and research resources
Manual
N/A
Data generation and review
N/A
650
Open-ended
Acc
MatSci-NLP [1001] [link]
Materials Science
Chemical composition, Numerical
property
Expert
Text QA
2023.05 EN
Academic and research resources
Manual
N/A
Data generation and review
N/A
169,197
Open-ended
Acc, F1
ChEBI-20 [692] [link]
Materials Science
Scientific instruction
Expert
Text QA
2021.11 EN
Integration of existing datasets
Manual
N/A
Data generation and review
N/A
3,301
Open-ended
BLEU,
ROUGE,
METEOR, CIDEr
MOSES [691] [link]
Materials Science
SMILES
Expert
Text QA
2020.11 EN
Integration of existing datasets
Manual
N/A
Data generation and review
N/A
176,000
Open-ended
Uniqueness,
Validity,
Frag, Scaff, SNN
MatBench [71] [link]
Materials Science
CIF, Numerical property, Chemical
composition
Expert
Text QA
2020.09 EN
Scientific databases
Manual
N/A
Data generation and review
N/A
408,062
Open-ended
MAE, AUROC
GuacaMol [759] [link]
Materials Science
SMILES
Expert
Text QA
2019.03 EN
Integration of existing datasets
Manual
N/A
Data generation and review
N/A
2M
Open-ended
Validity,
Uniqueness,
Novelty
MoleculeNet [219] [link]
Materials Science
SMILES
Expert
Text QA
2017.03 EN
Integration of existing datasets
Manual
N/A
Data generation and review
N/A
700,000
Open-ended
AUROC, AUPRC, RMSE,
MAE
MaCBench [208] [link]
Materials Science, Chemistry
Science QA, AFM Image
Expert
VQA
2024.11 EN
Academic and research resources
Manual
N/A
Data generation and review
N/A
628
Open-ended
Acc
MMSci [75] [link]
Materials Science, Chemistry
Science QA
Graduate
VQA
2024.05 EN
Academic and research resources
Manual
N/A
Data generation and review
N/A
742,273
Open-ended
Acc
Earth Science
ClimaQA [672] [link]
Atmosphere
Textbooks
Expert
Text QA
2025.03 EN
Books and literary works
Semi-automated
Data review
GPT-4o
3,633
MCQ,
Open-
ended
Acc, BLEU, etc.
WeatherQA [729] [link]
Atmosphere
Remote sensing, Science QA
Expert
VQA (multi-image)
2024.06 EN
Scientific databases
Semi-automated
4
Data review
600
MCQ,
Open-
ended
Acc, F1, BLEU, etc.
ClimateBERT [784] [link]
Atmosphere
Corporate annual reports, Sustain-
ability reports
Secondary
school
Text QA
2022.12 EN
Web and Internet content
Manual
4+
Data review
Prodigy
320
MCQ
Acc
OceanBench [570] [link]
Hydrosphere
Academic papers
Expert
Text QA
2024.09 EN
Academic and research resources
Automated
10+
Data review
GPT-4, GPT-3.5
13,000
Open-ended
Win Rate
OmniEarth-Bench [787] [link]
Hydrosphere, Biosphere, Lithosphere,
Atmosphere, Cryosphere
Remote sensing, Science QA
Expert
VQA
with
CoT
(multi-image)
2025.05 EN
Integration of existing datasets
Manual
40+
Data generation and review
29,779
MCQ
Acc, Precision, Recall, F1
MSEarth [153] [link]
Hydrosphere, Biosphere, Lithosphere,
Atmosphere, Cryosphere
Academic papers
Expert
VQA with CoT
2025.05 EN
Academic and research resources
Semi-automated
20+
Data review
GPT-4o
11,500
MCQ,
Open-
ended
BLEU, BERTScore, Acc
EarthSE [671] [link]
Hydrosphere, Biosphere, Lithosphere,
Atmosphere, Cryosphere
Academic papers
Expert
Text QA with CoT
2025.05 EN
Academic and research resources
Semi-automated
20+
Data review
GPT-4o
10,000
Open-ended
Acc
GeoBench [568] [link]
Lithosphere
Science QA
Expert
Text QA
2023.06 EN
Web and Internet content, Aca-
demic and research resources
Semi-automated
10+
Data review
2,516
MCQ,
Open-
ended
Acc, GPTScore
XLRS-Bench [786] [link]
Remote Sensing
Remote sensing
N/A
Image-text, VQA
2025.03 EN, ZH
Academic and research resources
Semi-automated
55
Data generation and review
GPT-4o
32,389
MCQ,
Open-
ended
Acc, IoU, BLEU, etc.
LRS-VQA [553] [link]
Remote Sensing
Remote sensing
N/A
Image-text, VQA
2025.03 EN
Academic and research resources
Automated
N/A
N/A
Qwen2-VL, GPT-4V 7,333
Open-ended
Acc
MME-RealWorld-RS [1002] [link]
Remote Sensing
Remote sensing
N/A
Image-text, VQA
2024.08 EN, ZH
Academic and research resources
Manual
N/A
Data generation and review
N/A
3,738
MCQ
Acc
VRSBench [798] [link]
Remote Sensing
Remote sensing
N/A
Image-text, VQA
2024.06 EN
Academic and research resources
Semi-automated
N/A
Data review
GPT-4V
62,917
Open-ended
Acc, IoU, BLEU, etc.
GeoChat [589] [link]
Remote Sensing
Remote sensing
N/A
Image-text, VQA
2023.11 EN
Academic and research resources,
Integration of existing datasets
Automated
N/A
N/A
Vicuna
10K
Open-ended
Acc, IoU, METEOR
RSIEval [785] [link]
Remote Sensing
Remote sensing
N/A
Image-text, VQA
2023.07 EN
Academic and research resources
Manual
5
Data generation and review
N/A
1,036
Open-ended
Acc, BLEU, ROUGE, etc.
DIOR-RSVG [806] [link]
Remote Sensing
Remote sensing
N/A
Image-text
2022.10 EN
Academic and research resources
Semi-automated
N/A
Data review
N/A
17,402
Open-ended
IoU
NWPU-Captions [1003] [link]
Remote Sensing
Remote sensing
N/A
Image-text
2022.08 EN
Academic and research resources
Manual
N/A
Data generation
N/A
31,500
Open-ended
BLEU, METEOR, etc.
RSVQA-HRBEN [795] [link]
Remote Sensing
Remote sensing
N/A
Image-text, VQA
2020.05 EN
Scientific databases
Automated
N/A
N/A
N/A
77,232
Open-ended
Acc
RSVQA-LRBEN [795] [link]
Remote Sensing
Remote sensing
N/A
Image-text, VQA
2020.05 EN
Scientific databases
Automated
N/A
N/A
N/A
1,066,316
Open-ended
Acc
RSICD [1004] [link]
Remote Sensing
Remote sensing
N/A
Image-text
2017.12 EN
Academic and research resources
Manual
N/A
Data generation
N/A
10,921
Open-ended
BLEU, METEOR, CIDEr
UCM-Captions [1004] [link]
Remote Sensing
Remote sensing
N/A
Image-text
2016.07 EN
Academic and research resources
Manual
N/A
Data generation
N/A
2,100
Open-ended
BLEU, METEOR, CIDEr
Sydney-Captions [1004] [link]
Remote Sensing
Remote sensing
N/A
Image-text
2016.07 EN
Academic and research resources
Manual
N/A
Data generation
N/A
613
Open-ended
BLEU, METEOR, CIDEr
64

TABLE VI: Summary of general science evaluation datasets for scientific LLMs/MLLMs. [link] directs to dataset websites.
Dataset
Scientific Domain
Modality
Type
Release Language Source
Annotation
Pipeline
Human
Annotators
Human Tasks
Auto-annotation
Tools
Size
Level
Evaluation
Type
Metrics
MMMU [790] [link]
Science
(Biology,
Chemistry,
Geography, Math, Physics), Health
& Medicine (Basic Medical Science,
Clinical
Medicine,
Diagnostics,
Pharmacy, Public Health), Tech &
Engineering (Materials, etc.)
Scientific VQA, MRI, CT, X-ray,
etc.
VQA
2023.11 EN
Comprehensive multi-source inte-
gration
Semi-automatic
50
Data review
Claude, GPT-4, GPT-4V 11,550
Expert
MCQ
Acc
MMMU Pro [791] [link]
Science
(Biology,
Chemistry,
Geography, Math, Physics), Health
& Medicine (Basic Medical Science,
Clinical
Medicine,
Diagnostics,
Pharmacy, Public Health), Tech &
Engineering (Materials, etc.)
Scientific VQA, MRI, CT, X-ray,
etc.
VQA
2023.11 EN
Comprehensive multi-source inte-
gration
Semi-automatic
N/A
Data review
Claude, GPT-4, GPT-4V 5,190
Expert
MCQ
Acc
ScienceQA [107] [link]
Biology,
Earth
Science,
Physics,
Chemistry, Geography
Scientific query, Scientific instruc-
tion, Science textbooks and litera-
ture
VQA
2022.01 EN
Books and literary works
Manual
9+
Data generation and
review
ViT, GPT-2
21.2k
Primary
school,
Secondary school MCQ
Acc
SciQA [108] [link]
Material Science, Chemistry, Life sci-
ences
Scientific query
Text QA
2023.05 EN
Academic and research resources
Manual
N/A
Data generation and
review
N/A
2,565
Expert
Open-ended
Acc
Scicode [122] [link]
Material Science, Biology, Chemistry,
Physics, Mathematics
Scientific Instruction
Text QA
2024.08 EN
Academic and research resources
Manual
N/A
Data generation and
review
N/A
338
Expert
Open-ended
pass@1
CURIE [110] [link]
Materials
Science,
Life
Sciences,
Physics, Earth Science
Scientific query
VQA
2025.04 EN
Integration of existing datasets
Manual
N/A
Data generation and
review
N/A
580
Expert
Open-ended
Acc
TheoremQA [1005] [link]
Physics, Mathematics
Theorems
Text QA
2023.12 EN
Books and literary works, Encyclo-
pedias and knowledge bases
Manual
N/A
Data generation and
review
N/A
800
Undergraduate,
Expert
Open-ended
Acc
SciBench [442] [link]
Physics, Chemistry
Science QA
Text QA
2023.09 EN
Books and literary works
Manual
7
Data review
N/A
695
Undergraduate
Open-ended
Acc
JEEBench [1006] [link]
Physics, Chemistry
Science Exams
Text QA
2023.12 EN
Other sources
Semi-automated
N/A
Data generation and
review
N/A
515
Expert
MCQ
Acc
MMLU [1007] [link]
Physics (College Physics, Conceptual
Physics, High School Physics), Chem-
istry (College Chemistry, High School
Chemistry), Biology (College Biology,
High School Biology)
Science QA
Text QA
2020.09 EN
Books and literary works
Manual
7
Data generation and
review
N/A
15.9k
Secondary
School,
Undergraduate,
Expert
MCQ
Acc
C-Eval [788] [link]
Chemistry (College Chemistry, High
School
Chemistry,
Middle
School
Chemistry), Physics (College Physics,
High School Physics, Middle School
Physics),
Biology
(High
School
Biology,
Middle
School
Biology),
Medicine
(Veterinary
Medicine,
Basic Medicine, Clinical Medicine,
Physician),
Earth
Science
(High
School
Geography,
Middle
School
Geography)
Exam questions, Chinese educa-
tional assessments
Text QA
2023.05 ZH
Books and literary works
Manual
12
Data generation and
review
N/A
13.9k
Primary
school,
Secondary
school,
Undergraduate
MCQ
Acc
GPQA [458] [link]
Chemistry, Biology, Physics
Graduate-level scientific questions
Text QA
2023.11 EN
Other sources
Manual
8
Data generation and
review
N/A
448
Expert
MCQ
Acc
ArXivQA [605] [link]
Physics (Accelerator Physics, High En-
ergy Physics - Lattice, Mathematical
Physics, etc.), Chemistry (Chemical
Physics), Biology (Quantitative Biol-
ogy), Material (Materials Theory)
scientific figure question-answer
Text QA
2024.05 EN, ZH
Other sources
Semi-automated
N/A
Data generation and
review
GPT-4V
249,587
Expert
MCQ
Acc
Xiezhi [1008] [link]
Agronomy (Crop Science, Veterinary
Medicine),
Science
(Chemistry,
Physics),
Medicine
(Traditional
Chinese Medicine)
Professional exams
Text QA
2024.05 EN
Comprehensive multi-source inte-
gration
Semi-automated
N/A
Data review
ChatGPT, Llama-7B
250k
Expert
MCQ
Acc
SuperGPQA [792] [link]
Medicine, Science, Agriculture
Graduate Disciplines QA
Text QA
2025.02 EN
Other sources
Semi-automatic
80+
Data generation and
review
N/A
26.5k
Expert
MCQ
Acc
BMMR [1009] [link]
Health
(Medicine,
Pharmacy,
etc.),
Natural Sciences (Physics, Biology,
etc.), Agriculture
Image, College-level visual ques-
tion answering, OCR-based QA
VQA
2025.07 EN, ZH
Web and Internet content, Books
and literary works, Integration of
existing datasets
Semi-automated
N/A
Data generation and
review
N/A
109,449
Primary
school,
Undergraduate,
Secondary school
MCQ
Acc
OlympiadBench [737] [link]
Physics, Mathematics
QA from math and physics compe-
titions, Image
Text QA, VQA
2024.02 ZH, EN
Other sources
Semi-automated
14
Data generation and
review
N/A
8.5k
Expert
Open-ended
Acc
LLM-SRBench [748] [link]
LSR-Synth
(Chemistry,
Biology,
Physics,
Material
Science),
LSR-
Transform
Structured Data
text
2025.04 EN
Comprehensive multi-source inte-
gration
Fully-automated
0
Data generation and
review
N/A
239
Expert
Open-ended
Exact Match, MSE
HLE [463] [link]
Biology (Marine Biology, Molecular
Biology, Computational Biology, Ecol-
ogy, etc.), Chemistry (Chemical En-
gineering, Biochemistry, etc.), Physics
(Biophysics), Materials Science
Organic reaction analysis, Molecu-
lar text, Chemical equations, Med-
ical question answering, Textbook
QA, etc.
Text QA
2025.01 EN
Academic and research resources
Manual
nearly 1000
Data generation and
review
GPT-4o
2,500
Expert
MCQ,
Open-
ended
Acc, Calibration Error
SFE [444] [link]
Astronomy, Chemistry, Life Science,
Materials Science, Earth Science
Protein structure, RNA structure,
Molecular structure, etc.
VQA
2025.06 EN, ZH
Scientific databases, Academic and
research resources
Manual
N/A
Data generation and
review
GPT-4o
1,660
Expert
MCQ,
Open-
ended
Exact Match, LLM-as-a-
Judge score, BERTScore,
IoU
SciEval [793] [link]
Chemistry, Physics, Biology
Text (equations, molecules, chemi-
cal reactions, scientific QA, etc.)
Text QA
2023.08 EN
Comprehensive multi-source inte-
gration
Semi-automated
N/A
Data review
GPT-4
18,000
Undergraduate,
Graduate
MCQ,
Open-
ended, True/False Acc, BLEU, MSE
Continued on next page
65

TABLE VI – continued from previous page
Dataset
Scientific Domain
Modality
Type
Release Language Source
Annotation
Pipeline
Human
Annotators
Human Tasks
Auto-annotation
Tools
Size
Level
Evaluation
Type
Metrics
SciKnowEval [443] [link]
Chemistry, Physics, Biology, Materials
Science
Textbook
QA,
Literature
QA,
SMILES, IUPAC, Equations, etc.
Text QA, Classifica-
tion, Regression
2024.06 EN
Comprehensive multi-source inte-
gration, Academic and research re-
sources, Scientific databases, Inte-
gration of existing datasets
Semi-automated
N/A
Data review
GPT-4o,
GPT-3.5,
Claude3, LLaMA, Qwen 70,203
Undergraduate,
Graduate, Expert
MCQ,
True/False,
Open-ended
Acc, F1, BLEU, ROUGE,
Smith-Waterman,
Tanimoto
AGIEval [789] [link]
Chemistry
(GK-chemistry),
Physics
(GK-physics), Biology (GK-biology),
Geography (GK-geography)
Textbook, Literature, SMILES, IU-
PAC, Equations, etc.
Text QA
2023.09 EN, ZH
Academic and research resources,
Integration of existing datasets
Semi-automated
N/A
Data review
ChatGPT, GPT-4
8,062
Secondary
school,
Undergraduate
MCQ,
Open-
ended
Acc, EM
ScienceAgentBench [83] [link]
Bioinformatics, Computational chem-
istry, Geographical information sci-
ence, Psychology & cognitive neuro-
science
Microscopy
images,
SMILES
strings,
Geospatial
data,
EEG,
ECG, IMU, etc.
VQA
2024.10 EN
Academic and research resources,
Integration of existing datasets
Manual
9
Data generation and
review
N/A
102 tasks
Expert
Open-ended
VER,
SR,
Code-
BERTScore,
GPT-4o
Judge
66

TABLE VII: Summary of scientific large language models. [link] directs to model websites.
Scientific Domain
Model
Subdomain
Parameters
Base Model
Modality Encoder
Release
Open-source
General-purpose
Galactica [30] [link]
General Science
120B
N/A
N/A
2022.11
✓
DARWIN [449] [link]
General Science
7B
LLaMA-7B, Vicuna-7B
N/A
2023.08
✓
FORGE [1010] [link]
General Science
26B
GPT-NeoX
N/A
2023.11
✓
SciGLM [41] [link]
General Science
6B / 32B
ChatGLM3
N/A
2024.01
✓
SciDFM [452] [link]
General Science
18.2B-A5.6B
N/A
N/A
2024.09
✓
OmniScience [453] [link]
General Science
70B
LLaMA-3.1
N/A
2025.03
✗
Intern-S1 [47] [link]
General Science
241B-A28B/8B
Qwen3-235B-A22B, Qwen3-8B
InternViT-6B, InternViT-300M
2025.08
✓
Physics
MechGPT [486] [link]
Mechanics
13B / 70B
LLaMA-2
N/A
2023.10
✓
Xiwu [467] [link]
High Energy Physics
7B / 13B
LLaMA, Vicuna, ChatGLM, Grok-
1
N/A
2024.04
✓
Poseidon [465] [link]
Partial Differential Equations
0.02B / 0.2B / 0.6B
scOT
N/A
2024.05
✓
L3M [1011] [link]
Astrophysics
0.5B
Qwen2.5-0.5B-Instruct
N/A
2025.06
✗
Chemistry
ChemLLM [20] [link]
Chemistry, Pharmacy
7B
InternLM2
N/A
2024.06
✓
LLM-RDF [1012]
Chemistry, chemical synthesis
N/A
GPT-4
N/A
2024.11
✓
InstructMol [469] [link]
Biochemistry, Chemistry, Pharmacy
7B
LLaMA
molecular graph encoder
2024.12
✓
ChemDFM [470] [link]
Chemistry (molecular design), Chemistry
13B
LLaMA-2
N/A
2025.07
✓
ChemMLLM [201] [link]
Chemistry (molecular design), Pharmacy
34B
Lumina-mGPT-34B-512
VQGAN
2025.08
✓
Chemma [1013]
Chemistry, Organic Chemistry
7B
LLaMA-2
N/A
2025.07
✓
Chem3DLLM [471]
Chemistry (Molecular Design), Pharmacy
7B
Qwen2-7B
ESM-Encoder
2025.08
✓
Materials Science
SMILES-BERT [472] [link]
Materials Science
30M
BERT-small
N/A
2019.09
✓
MolGPT [481] [link]
Materials Science
N/A
N/A
N/A
2022.05
✓
MOFormer [1014]
Materials Science
N/A
N/A
N/A
2022.10
✗
MatBert-bandgap [475] [link]
Materials Science
110M
MatBERT
N/A
2023.03
✓
Regression Transformer [476] [link]
Materials Science
N/A
N/A
N/A
2023.04
✓
MolXPT [478] [link]
Materials Science
N/A
GPT-2
N/A
2023.05
✓
xyztransformer [482] [link]
Materials Science
N/A
N/A
N/A
2023.05
✓
polyBERT [473] [link]
Materials Science
N/A
DeBERTa
N/A
2023.07
✓
GPT-MolBERTa [480]
Materials Science
N/A
RoBERTa
N/A
2023.10
✗
ChemRLformer [1015]
Materials Science
N/A
N/A
N/A
2023.10
✗
CrystaLLM [1016] [link]
Materials Science
70B
LLaMA-2 70B
N/A
2024.02
✓
MatText [1017] [link]
Materials Science
N/A
BERT
N/A
2024.06
✓
ChatMOF [1018] [link]
Materials Science
N/A
GPT-4, GPT-3.5-turbo, and GPT-
3.5-turbo-16k
N/A
2024.06
✓
LHS2RHS [484]
Materials Science
N/A
N/A
N/A
2024.10
✗
RHS2LHS [484]
Materials Science
N/A
N/A
N/A
2024.10
✗
TGT2CEQ [484]
Materials Science
N/A
N/A
N/A
2024.10
✗
CrystaLLM [483] [link]
Materials Science
200M
GPT-2
N/A
2024.12
✓
molT5-large [1019] [link]
Materials Science
770M
T5-large
N/A
2024.12
✓
Qwen2-KG [477] [link]
Materials Science
72B
Qwen2-72B
N/A
2025.02
✓
LLM-Prop [1020] [link]
Materials Science
37M
T5-small
N/A
2025.06
✓
Crystal Synthesis LLM [485] [link]
Materials Science
8B
LLaMA-3-8B
N/A
2025.07
✓
Life Sciences
ShizhenGPT [1021] [link]
Healthcare and Medical Sciences
7B / 32B
Qwen2.5
Qwen2.5-VL
vision
encoder,
Whisper-large-v3
2025.08
✓
ProGen2 [499] [link]
Proteomics
6.4B / 2.7B / 764M / 151M
N/A
N/A
2022.06
✓
BioGPT [936] [link]
Healthcare and Medical Sciences, General Biology
347M
GPT-2
N/A
2022.10
✓
ESM-2 [491] [link]
Proteomics
15B / 3B / 650M /150M/ 35M / 8M N/A
N/A
2023.03
✓
OphGLM [1022] [link]
Healthcare and Medical Sciences
6B
ChatGLM-6B
ConvNext
2023.03
✓
MedAlpaca [521] [link]
Healthcare and Medical Sciences
7B / 13B
LLaMA
N/A
2023.04
✓
DoctorGLM [585] [link]
Healthcare and Medical Sciences
6B
ChatGLM-6B
N/A
2023.04
✓
PMC-LLaMA [1023] [link]
Healthcare and Medical Sciences
13B
LLaMA
N/A
2023.04
✓
scGPT [513] [link]
Multi-omics
30k / 300k / 3M / 33M
N/A
N/A
2023.04
✓
Med-PaLM [31] [link]
Healthcare and Medical Sciences
N/A
PaLM
N/A
2023.05
✗
Med-PaLM 2 [1024] [link]
Healthcare and Medical Sciences
N/A
PaLM 2
N/A
2023.05
✗
GatorTronS [16] [link]
Healthcare and Medical Sciences
345M / 3.9B / 8.9B
GPT-3
N/A
2023.05
✓
GatorTronGPT [1025] [link]
Healthcare and Medical Sciences
5B / 20B
GPT-3
N/A
2023.05
✓
HuatuoGPT [525] [link]
Healthcare and Medical Sciences
7B / 13B
Baichuan-7B,
Ziya-LLaMA-13B-
Pretrain-v1
N/A
2023.05
✓
BiomedGPT [1026] [link]
Healthcare and Medical Sciences
33M / 93M / 182M
OFA
VQ-GAN
2023.05
✓
ClinicalGPT [1027] [link]
Healthcare and Medical Sciences
7B
BLOOM-7B
N/A
2023.06
✓
GENA-LM [1028] [link]
Molecular and Cell Biology, Multi-omics
110M / 336M
BERT
N/A
2023.06
✓
NYUTron [1029] [link]
Healthcare and Medical Sciences, Neuroscience,
Pharmacy
190M
BERT
N/A
2023.06
✓
ChatDoctor [1030] [link]
Healthcare and Medical Sciences
7B
LLaMA
N/A
2023.06
✓
SoulChat [1031] [link]
Neuroscience, Healthcare and Medical Sciences
6B
ChatGLM-6B
N/A
2023.07
✓
DNAGPT [1032] [link]
Molecular and Cell Biology, Multi-omics
3B
GPT
N/A
2023.07
✓
Med-Flamingo [540] [link]
Healthcare and Medical Sciences
9B
Openflamingo
Openflamingo
2023.07
✓
DISC-MedLLM [902] [link]
Healthcare and Medical Sciences
13B
Baichuan-13B
N/A
2023.08
✓
IvyGPT [1033] [link]
Healthcare and Medical Sciences
33B
LLaMA-33B
N/A
2023.08
✗
Zhongjing [530] [link]
Healthcare and Medical Sciences
13B
Ziya-LLaMA-13B-V1
N/A
2023.08
✓
Radiology-Llama2 [539] [link]
Healthcare and Medical Sciences
7B
LLaMA-2
N/A
2023.08
✓
RadFM [1034] [link]
Healthcare and Medical Sciences
9B
MedLLaMA-13B
3D ViT
2023.08
✓
CPLLM [1035] [link]
Healthcare and Medical Sciences
13B
Llama2-13B
N/A
2023.09
✓
DRG-LLaMA [1036] [link]
Healthcare and Medical Sciences
7B
LLaMA-7B
N/A
2023.09
✓
MindGPT [558] [link]
Neuroscience, Healthcare and Medical Sciences
124M
GPT-2
CLIP-ViT-B/32
2023.09
✗
BioinspiredLLM [1037] [link]
General Biology, Molecular and Cell Biology, Pro-
teomics
13B
LLaMA-2
N/A
2023.09
✓
Qilin-Med [1038] [link]
Healthcare and Medical Sciences
7B
Baichuan-7B
N/A
2023.10
✗
CXR-LLAVA [538] [link]
Healthcare and Medical Sciences
7B
LLaMA-2
CLIP ViT-L/16
2023.10
✓
InstructProtein [1039]
Proteomics
1.3B
OPT-1.3B
N/A
2023.10
✗
ChiMed-GPT [527] [link]
Healthcare and Medical Sciences
13B
Ziya-13B-v2
N/A
2023.11
✓
HuatuoGPT-II [42] [link]
Healthcare and Medical Sciences
7B/13B
Baichuan2-7B-Base,
Baichuan2-
13B-Base
N/A
2023.11
✓
Taiyi-LLM [1040] [link]
Healthcare and Medical Sciences
7B
Qwen-7B-base
N/A
2023.11
✓
Meditron [38] [link]
Healthcare and Medical Sciences
7B / 70B
LLaMA-2
N/A
2023.11
✓
MAIRA-1 [1041] [link]
Healthcare and Medical Sciences
7B
Vicuna-7B
RAD-DINO
2023.11
✓
MAIRA-2 [1042] [link]
Healthcare and Medical Sciences
7B
Vicuna-7B-v1.5
RAD-DINO
2023.11
✓
Neuro-GPT [561] [link]
Neuroscience, Healthcare and Medical Sciences
124M
GPT-2
EEG Encoder
2023.11
✓
PLLaMa [551] [link]
Molecular and Cell Biology, General Biology
7B / 13B
LLaMA-2
N/A
2024.01
✓
EEG-GPT [554] [link]
Neuroscience
N/A
GPT-3
EEG Encoder
2024.01
✗
BioMistral [518] [link]
Healthcare and Medical Sciences, Molecular and Cell
Biology
7B
Mistral-7B-Instruct-v0.1
N/A
2024.02
✓
MMed-LLaMA 3 [1043] [link]
Healthcare and Medical Sciences
8B
LLaMA 3
N/A
2024.02
✓
ProLLaMA [1044] [link]
Proteomics
7B
LLaMA-2
N/A
2024.02
✓
ProtLLM [1045] [link]
Proteomics
7B
LLaMA-7B
ProtST (protein)
2024.03
✓
BrainGPT [553] [link]
Neuroscience
7B
Mistral-7B
N/A
2024.03
✓
Apallo [524] [link]
Healthcare and Medical Sciences
0.5B / 1.8B / 2B / 6B / 7B
Qwen
N/A
2024.03
✓
Med-Gemini [1046] [link]
Healthcare and Medical Sciences
N/A
Gemini 1.5 Pro
Custom encoders (multimodal)
2024.04
✗
UMBRAE [556] [link]
Neuroscience
7B
Vicuna-7B
CLIP-ViT/L-14 (vision), Encoder
(fMRI)
2024.04
✓
SeedLLM [547] [link]
Agronomy
7B
Qwen2.5
N/A
2024.04
✗
Alphafold3 [1047] [link]
Molecular and Cell Biology, Proteomics, Pharmacy,
Neuroscience
N/A
N/A
Input Feature Embedder
2024.05
✗
DrugLLM [6] [link]
Pharmacy
7B
LLaMA 7B
N/A
2024.05
✗
LLaVA-Med [537] [link]
Healthcare and Medical Sciences
N/A
Vicuna-7B
Clip ViT-L/14
2024.05
✓
CareGPT [1048] [link]
Healthcare and Medical Sciences
7B
LLaMA-2
N/A
2024.05
✓
ProtT3 [1049] [link]
Proteomics
N/A
Galactica 1.3B
ESM-2 (protein)
2024.05
✓
MolecularGPT [512] [link]
Molecular and Cell Biology
N/A
LLaMA
N/A
2024.06
✓
HuatuoGPT-Vision [541] [link]
Healthcare and Medical Sciences
7B / 34B
Qwen2-7B
Qwen Image Encoder (vision)
2024.06
✓
NeuroLM [555] [link]
Neuroscience
254M/500M/1.7B
GPT-2
Encoder (EEG)
2024.08
✓
RNAGPT [641] [link]
Molecular and Cell Biology, Multi-omics
8B
LLaMA-3
RNA-FM sequence encoder (RNA) 2024.10
✗
AgroGPT [552] [link]
Agronomy
3B / 7B
LLaVA-1.5, Mipha
CLIP-ViT-L/14 (vision), SigLIP
2024.10
✓
LLaMA-Gene [40] [link]
Molecular and Cell Biology, Proteomics
7B
LLaMA-7B
N/A
2024.11
✓
GMAI-VL [542] [link]
Healthcare and Medical Sciences
7B
InternLM
Image Encoder (vision)
2024.11
✓
HuatuoGPT-o1 [544] [link]
Healthcare and Medical Sciences
7B / 8B / 70B / 72B
LLaMA-3.1, Qwen2.5
N/A
2024.12
✓
Evolla [510] [link]
Proteomics
10B / 80B
LLaMA-3 8B
Saprot (protein)
2025.01
✓
UniMind [560]
Neuroscience
7B
InternLM2.5
Encoder (EEG)
2025.01
✗
NatureLM [43] [link]
Pharmacy, Molecular and Cell Biology, Proteomics,
Material
46.7B
Mixtral 8x7B
N/A
2025.02
✗
MindLLM [559] [link]
Neuroscience, Healthcare and Medical Sciences
7B
Vicuna-7B
Encoder (fMRI)
2025.02
✓
MedVLM-R1 [1050] [link]
Healthcare and Medical Sciences
2B
Qwen2-VL
Qwen Image Encoder (vision)
2025.02
✓
AlphaGenome [1051] [link]
Molecular and Cell Biology, Multi-omics
N/A
N/A
N/A
2025.05
✓
ChatNT [511] [link]
Molecular and Cell Biology, Proteomics, Multi-omics 7B
Vicuna-7B
Nucleotide Transformer v2 (DNA)
2025.06
✓
Lingshu [1052] [link]
Healthcare and Medical Sciences
7B / 32B
Qwen
N/A
2025.06
✓
PodGPT [1053] [link]
Healthcare and Medical Sciences
N/A
Gemma, Mixtral, LLaMA
N/A
2025.07
✓
MedGemma [543] [link]
Healthcare and Medical Sciences
4B / 27B
Gemma 3
SigLip Image Encoder (vision)
2025.07
✓
Continued on next page
67

TABLE VII – continued from previous page
Scientific Domain
Models
Domain
Parameters
Base LLM
Modality encoder
Release
Open-source
Astronomy
AstroLLaMA-2-7B [562] [link]
Astronomy
7B
Llama-2 LLM
N/A
2023.09
✓
AstroLLaMA-3-8B [725] [link]
Astronomy
8B
LLaMA-2-7B LLM
N/A
2024.09
✓
AstroLLaMA-2-70B [725] [link]
Astronomy
70B
LLaMA-2-7B LLM
N/A
2024.09
✓
AstroSage-LLaMA-3.1-8B [564] [link]
Astronomy
8B
Llama-3.1-8B LLM
N/A
2025.04
✓
AstroLLaVa-7B [563] [link]
Astronomy
7B
LLaVA 1.5 LLM
CLIP-ViT/L-14 (vision)
2025.04
✓
AstroSage-LLaMA-3.1-70B [567] [link]
Astronomy
70B
Llama-3.1-70B LLM
N/A
2025.05
✓
Earth Science
OceanGPT [570] [link]
Hydrosphere, Biosphere, Lithosphere, Remote Sens-
ing
7B
LLama, Qwen
N/A
2023.03
✓
K2 [568] [link]
Lithosphere, Remote Sensing
7B
LLama
N/A
2023.08
✓
GeoChat [589] [link]
Remote Sensing, Lithosphere
7B
Vicuna-v1.5
N/A
2023.11
✓
SkyEyeGPT [965] [link]
Remote Sensing
7B
N/A
N/A
2024.01
✓
TeoChat [579] [link]
Remote Sensing, Lithosphere
7B
Vdieo-LLaVA
N/A
2024.10
✓
EarthMarker [572] [link]
Remote Sensing
13B
LLaMA-2
N/A
2024.11
✓
EarthDial [575] [link]
Remote Sensing
4B
Phi-3-mini
N/A
2024.12
✓
GeoPixel [573] [link]
Remote Sensing, Lithosphere
7B
IXC-2.5
N/A
2025.01
✓
EagleVision [571] [link]
Remote Sensing
1B/2B/4B/7B
Qwen2-VL-72B, GPT-4o
N/A
2025.03
✓
ClimateChat [569] [link]
Lithosphere, Climate
7B
jiuZhou
N/A
2025.03
✓
GeoGPT [1054] [link]
Lithosphere, Remote Sensing
70B
Llama3.1-70B, Qwen2.5-72B
N/A
2025.04
✓
GeoLLaVA-8K [574] [link]
Remote Sensing, Lithosphere
7B
LongVA
N/A
2025.05
✓
68

REFERENCES
[1] H. Wang, T. Fu, Y. Du, W. Gao, K. Huang, Z. Liu, P. Chandak,
S. Liu, P. Van Katwyk, A. Deac et al., “Scientific discovery in the
age of artificial intelligence,” Nature, vol. 620, no. 7972, pp. 47–60,
2023.
[2] J. Jiang, F. Wang, J. Shen, S. Kim, and S. Kim, “A survey on large lan-
guage models for code generation,” arXiv preprint arXiv:2406.00515,
2024.
[3] X. Zhang, L. Wang, J. Helwig, Y. Luo, C. Fu, Y. Xie, M. Liu,
Y. Lin, Z. Xu, K. Yan et al., “Artificial intelligence for science
in quantum, atomistic, and continuum systems,” Foundations and
Trends® in Machine Learning, vol. 18, no. 4, pp. 385–912, 2025.
[4] X. Zhou, J. He, W. Zhou, H. Chen, Z. Tang, H. Zhao, X. Tong, G. Li,
Y. Chen, J. Zhou et al., “A survey of LLM × data,” arXiv preprint
arXiv:2505.18458, 2025.
[5] Y. Liu, J. Cao, C. Liu, K. Ding, and L. Jin, “Datasets for
large language models: A comprehensive survey,” arXiv preprint
arXiv:2402.18041, 2024.
[6] X. Liu, Y. Guo, H. Li, J. Liu, S. Huang, B. Ke, and J. Lv, “Drugllm:
Open large language model for few-shot molecule generation,” arXiv
preprint arXiv:2405.06690, 2024.
[7] Y. Xiao, W. Zhao, J. Zhang, Y. Jin, H. Zhang, Z. Ren, R. Sun,
H. Wang, G. Wan, P. Lu et al., “Protein large language models: A
comprehensive survey,” arXiv preprint arXiv:2502.17504, 2025.
[8] X. Fang, W. Xu, F. A. Tan, J. Zhang, Z. Hu, Y. Qi, S. Nick-
leach, D. Socolinsky, S. Sengamedu, and C. Faloutsos, “Large lan-
guage models (llms) on tabular data: Prediction, generation, and
understanding–a survey,” arXiv preprint arXiv:2402.17944, 2024.
[9] T. Ridnik, D. Kredo, and I. Friedman, “Code generation with al-
phacodium: From prompt engineering to flow engineering,” arXiv
preprint arXiv:2401.08500, 2024.
[10] X. Hou, Y. Zhao, Y. Liu, Z. Yang, K. Wang, L. Li, X. Luo, D. Lo,
J. Grundy, and H. Wang, “Large language models for software
engineering: A systematic literature review,” ACM Transactions on
Software Engineering and Methodology, vol. 33, no. 8, pp. 1–79,
2024.
[11] J. Cui, Z. Li, Y. Yan, B. Chen, and L. Yuan, “Chatlaw: Open-source
legal large language model with integrated external knowledge bases,”
CoRR, 2023.
[12] P. Colombo, T. P. Pires, M. Boudiaf, D. Culver, R. Melo, C. Corro,
A. F. Martins, F. Esposito, V. L. Raposo, S. Morgado et al., “Saullm-
7b: A pioneering large language model for law,” arXiv preprint
arXiv:2403.03883, 2024.
[13] G. Tom, S. P. Schmid, S. G. Baird, Y. Cao, K. Darvish, H. Hao,
S. Lo, S. Pablo-Garc´ıa, E. M. Rajaonson, M. Skreta et al., “Self-
driving laboratories for chemistry and materials science,” Chemical
Reviews, vol. 124, no. 16, pp. 9633–9732, 2024.
[14] Y. Zimmermann, A. Bazgir, A. Al-Feghali, M. Ansari, J. Bocarsly,
L. C. Brinson, Y. Chiang, D. Circi, M.-H. Chiu, N. Daelman et al.,
“34 examples of llm applications in materials science and chemistry:
Towards automation, assistants, agents, and accelerated scientific
discovery,” Machine Learning: Science and Technology, vol. 6, no. 3,
2025.
[15] K. Singhal, S. Azizi, T. Tu, S. S. Mahdavi, J. Wei, H. W. Chung,
N. Scales, A. Tanwani, H. Cole-Lewis, S. Pfohl et al., “Large language
models encode clinical knowledge,” Nature, vol. 620, no. 7972, pp.
172–180, 2023.
[16] C. Peng, X. Yang, A. Chen, K. E. Smith, N. PourNejatian, A. B.
Costa, C. Martin, M. G. Flores, Y. Zhang, T. Magoc et al., “A study of
generative large language model for medical research and healthcare,”
NPJ digital medicine, vol. 6, no. 1, p. 210, 2023.
[17] M. Y. Lu, B. Chen, D. F. Williamson, R. J. Chen, M. Zhao, A. K.
Chow, K. Ikemura, A. Kim, D. Pouli, A. Patel et al., “A multimodal
generative ai copilot for human pathology,” Nature, vol. 634, no. 8033,
pp. 466–473, 2024.
[18] K. Huang, S. Zhang, H. Wang, Y. Qu, Y. Lu, Y. Roohani, R. Li,
L. Qiu, G. Li, J. Zhang et al., “Biomni: A general-purpose biomedical
ai agent,” biorxiv, pp. 2025–05, 2025.
[19] J. Ahn, R. Verma, R. Lou, D. Liu, R. Zhang, and W. Yin, “Large
language models for mathematical reasoning: Progresses and chal-
lenges,” arXiv preprint arXiv:2402.00157, 2024.
[20] D. Zhang, W. Liu, Q. Tan, J. Chen, X. Yue, W. Ouyang, D. Zhou,
S. Zhang, M. Su, H. Zhong, and Y. Li, “Chemllm: A chemical large
language model,” arXiv preprint, 2024.
[21] Q. Zhang, K. Ding, T. Lv, X. Wang, Q. Yin, Y. Zhang, J. Yu, Y. Wang,
X. Li, Z. Xiang et al., “Scientific large language models: A survey on
biological & chemical domains,” ACM Computing Surveys, vol. 57,
no. 6, pp. 1–38, 2025.
[22] Z. Lin, C. Deng, L. Zhou, T. Zhang, Y. Xu, Y. Xu, Z. He, Y. Shi,
B. Dai, Y. Song et al., “Geogalactica: A scientific large language
model in geoscience,” arXiv preprint arXiv:2401.00434, 2023.
[23] J. Devlin, M.-W. Chang, K. Lee, and K. Toutanova, “Bert: Pre-training
of deep bidirectional transformers for language understanding,” in
Proceedings of the 2019 conference of the North American chapter
of the association for computational linguistics: human language
technologies, volume 1 (long and short papers), 2019, pp. 4171–4186.
[24] I. Beltagy, K. Lo, and A. Cohan, “SciBERT: A pretrained language
model for scientific text,” Sep. 2019.
[25] J. Lee, W. Yoon, S. Kim, D. Kim, S. Kim, C. H. So, and
J. Kang, “Biobert: a pre-trained biomedical language representation
model
for
biomedical
text
mining,”
Bioinformatics,
vol.
36,
no.
4,
p.
1234–1240,
Sep.
2019.
[Online].
Available:
http:
//dx.doi.org/10.1093/bioinformatics/btz682
[26] Y. Gu, R. Tinn, H. Cheng, M. Lucas, N. Usuyama, X. Liu, T. Nau-
mann, J. Gao, and H. Poon, “Domain-specific language model pre-
training for biomedical natural language processing,” ACM Transac-
tions on Computing for Healthcare (HEALTH), vol. 3, no. 1, pp. 1–23,
2021.
[27] L. Floridi and M. Chiriatti, “Gpt-3: Its nature, scope, limits, and
consequences,” Minds and machines, vol. 30, no. 4, pp. 681–694,
2020.
[28] J. Hoffmann, S. Borgeaud, A. Mensch, E. Buchatskaya, T. Cai,
E. Rutherford, D. de Las Casas, L. A. Hendricks, J. Welbl, A. Clark,
T. Hennigan, E. Noland, K. Millican, G. van den Driessche, B. Damoc,
A. Guy, S. Osindero, K. Simonyan, E. Elsen, O. Vinyals, J. W. Rae,
and L. Sifre, “Training compute-optimal large language models,” in
Proceedings of the 36th International Conference on Neural Informa-
tion Processing Systems, 2022.
[29] J. Kaplan, S. McCandlish, T. Henighan, T. B. Brown, B. Chess,
R. Child, S. Gray, A. Radford, J. Wu, and D. Amodei, “Scaling laws
for neural language models,” arXiv preprint arXiv:2001.08361, 2020.
[30] R. Taylor, M. Kardas, G. Cucurull, T. Scialom, A. Hartshorn, E. Sar-
avia, A. Poulton, V. Kerkez, and R. Stojnic, “Galactica: A large
language model for science,” arXiv preprint arXiv:2211.09085, 2022.
[31] K. Singhal, T. Tu, J. Gottweis, R. Sayres, E. Wulczyn, L. Hou,
K. Clark, S. Pfohl, H. Cole-Lewis, D. Neal, M. Schaekermann,
A. Wang, M. Amin, S. Lachgar, P. Mansfield, S. Prakash, B. Green,
E. Dominowska, B. A. y Arcas, N. Tomasev, Y. Liu, R. Wong,
C. Semturs, S. S. Mahdavi, J. Barral, D. Webster, G. S. Corrado,
Y. Matias, S. Azizi, A. Karthikesalingam, and V. Natarajan, “Towards
expert-level medical question answering with large language models,”
2023. [Online]. Available: https://arxiv.org/abs/2305.09617
[32] L. Ouyang, J. Wu, X. Jiang, D. Almeida, C. Wainwright, P. Mishkin,
C. Zhang, S. Agarwal, K. Slama, A. Ray et al., “Training language
models to follow instructions with human feedback,” Advances in
neural information processing systems, vol. 35, pp. 27 730–27 744,
2022.
[33] OpenAI,
“Introducing
chatgpt,”
https://openai.com/blog/chatgpt,
2022, accessed: 2025-08-11.
[34] H. Touvron, T. Lavril, G. Izacard, X. Martinet, M.-A. Lachaux,
T. Lacroix, B. Rozi`ere, N. Goyal, E. Hambro, F. Azhar et al., “Llama:
Open and efficient foundation language models,” arXiv preprint
arXiv:2302.13971, 2023.
[35] J. Bai, S. Bai, Y. Chu, Z. Cui, K. Dang, X. Deng, Y. Fan, W. Ge,
Y. Han, F. Huang et al., “Qwen technical report,” arXiv preprint
arXiv:2309.16609, 2023.
[36] T. GLM, A. Zeng, B. Xu, B. Wang, C. Zhang, D. Yin, D. Zhang,
D. Rojas, G. Feng, H. Zhao et al., “Chatglm: A family of large
language models from glm-130b to glm-4 all tools,” arXiv preprint
arXiv:2406.12793, 2024.
[37] A. Q. Jiang, A. Sablayrolles, A. Mensch, C. Bamford, D. S. Chaplot,
D. de las Casas, F. Bressand, G. Lengyel, G. Lample, L. Saulnier,
L. R. Lavaud, M.-A. Lachaux, P. Stock, T. L. Scao, T. Lavril, T. Wang,
T. Lacroix, and W. E. Sayed, “Mistral 7b,” https://arxiv.org/abs/2310.
06825, 2023.
[38] Z. Chen, A. H. Cano, A. Romanou, A. Bonnet, K. Matoba, F. Salvi,
M. Pagliardini, S. Fan, A. K¨opf, A. Mohtashami et al., “Meditron-
70b: Scaling medical pretraining for large language models,” arXiv
preprint arXiv:2311.16079, 2023.
[39] M. Huo, H. Guo, X. Cheng, D. Singh, H. Rahmani, S. Li, P. Gerlof,
T. Ideker, D. A. Grotjahn, E. Villa et al., “Multi-modal large language
69

model enables protein function prediction,” bioRxiv, pp. 2024–08,
2024.
[40] W. Liang, “LLaMA-Gene: A general-purpose gene task large lan-
guage model based on instruction fine-tuning,” arXiv preprint
arXiv:2412.00471, 2024.
[41] D. Zhang, Z. Hu, S. Zhoubian, Z. Du, K. Yang, Z. Wang, Y. Yue,
Y. Dong, and J. Tang, “Sciglm: Training scientific language models
with self-reflective instruction annotation and tuning,” arXiv preprint
arXiv:2401.07950, 2024.
[42] J. Chen, X. Wang, K. Ji, A. Gao, F. Jiang, S. Chen, H. Zhang,
D.
Song,
W.
Xie,
C.
Kong,
J.
Li,
X.
Wan,
H.
Li,
and
B. Wang, “Huatuogpt-ii, one-stage training for medical adaption of
llms,” Proceedings of COLM (arXiv:2311.09774v2), 2024. [Online].
Available: https://arxiv.org/abs/2311.09774
[43] Y. Xia, P. Jin, S. Xie, L. He, C. Cao, R. Luo, G. Liu, Y. Wang, Z. Liu,
Y.-J. Chen et al., “Nature language model: Deciphering the language
of nature for scientific discovery,” arXiv preprint arXiv:2502.07527,
2025.
[44] D. A. Boiko, R. MacKnight, B. Kline, and G. Gomes, “Autonomous
chemical research with large language models,” Nature, vol. 624, no.
7992, pp. 570–578, 2023.
[45] S. Hong, M. Zhuge, J. Chen, X. Zheng, Y. Cheng, J. Wang, C. Zhang,
Z. Wang, S. K. S. Yau, Z. Lin et al., “Metagpt: Meta programming for
a multi-agent collaborative framework,” in The Twelfth International
Conference on Learning Representations, 2023.
[46] J. Gottweis, W.-H. Weng, A. Daryin, T. Tu, A. Palepu, P. Sirkovic,
A. Myaskovsky, F. Weissenberger, K. Rong, R. Tanno et al., “Towards
an ai co-scientist,” arXiv preprint arXiv:2502.18864, 2025.
[47] L. Bai, Z. Cai, M. Cao, W. Cao, C. Chen, H. Chen, K. Chen, P. Chen,
Y. Chen, Y. Chen, Y. Cheng, Y. Cheng, P. Chu, T. Chu, E. Cui, G. Cui,
L. Cui, Z. Cui, N. Deng, N. Ding, N. Dong, P. Dong, S. Dou, S. Du,
H. Duan, C. Fan, B. Gao, C. Gao, J. Gao, S. Gao, Y. Gao, Z. Gao,
J. Ge, Q. Ge, L. Gu, Y. Gu, A. Guo, Q. Guo, X. Guo, C. He, J. He,
Y. Hong, S. Hou, C. Hu, H. Hu, J. Hu, M. Hu, Z. Hua, H. Huang,
J. Huang, X. Huang, Z. Huang, Z. Jiang, L. Kong, L. Li, P. Li, P. Li,
S. Li, T. Li, W. Li, Y. Li, D. Lin, J. Lin, T. Lin, Z. Lin, H. Liu,
J. Liu, J. Liu, J. Liu, K. Liu, K. Liu, K. Liu, S. Liu, S. Liu, W. Liu,
X. Liu, Y. Liu, Z. Liu, Y. Lu, H. Lv, H. Lv, H. Lv, Q. Lv, Y. Lv,
C. Lyu, C. Ma, J. Ma, R. Ma, R. Ma, R. Ma, X. Ma, Y. Ma, Z. Ma,
S. Mi, J. Ning, W. Ning, X. Pang, J. Peng, R. Peng, Y. Qiao, J. Qiu,
X. Qu, Y. Qu, Y. Ren, F. Shang, W. Shao, J. Shen, S. Shen, C. Song,
D. Song, D. Song, C. Su, W. Su, W. Sun, Y. Sun, Q. Tan, C. Tang,
H. Tang, K. Tang, S. Tang, J. Tong, A. Wang, B. Wang, D. Wang,
L. Wang, R. Wang, W. Wang, W. Wang, Y. Wang, Z. Wang, L.-I.
Wu, W. Wu, Y. Wu, Z. Wu, L. Xiao, S. Xing, C. Xu, H. Xu, J. Xu,
R. Xu, W. Xu, G. Yang, Y. Yang, H. Ye, J. Ye, S. Ye, J. Yu, J. Yu,
J. Yu, F. Yuan, B. Zhang, C. Zhang, C. Zhang, H. Zhang, J. Zhang,
Q. Zhang, Q. Zhang, S. Zhang, T. Zhang, W. Zhang, W. Zhang,
Y. Zhang, Z. Zhang, H. Zhao, Q. Zhao, X. Zhao, X. Zhao, B. Zhou,
D. Zhou, P. Zhou, Y. Zhou, Y. Zhou, D. Zhu, L. Zhu, and Y. Zou,
“Intern-s1: A scientific multimodal foundation model,” arXiv preprint
arXiv:2508.15763, 2025.
[48] N.
Shazeer,
A.
Mirhoseini,
K.
Maziarz,
A.
Davis,
Q.
Le,
G. Hinton, and J. Dean, “Outrageously large neural networks: The
sparsely-gated mixture-of-experts layer,” in International Conference
on Learning Representations, 2017. [Online]. Available: https:
//openreview.net/forum?id=B1ckMDqlg
[49] Y. Yamada, R. T. Lange, C. Lu, S. Hu, C. Lu, J. Foerster, J. Clune,
and D. Ha, “The ai scientist-v2: Workshop-level automated scientific
discovery via agentic tree search,” arXiv preprint arXiv:2504.08066,
2025.
[50] A. Ghafarollahi and M. J. Buehler, “Sciagents: automating scientific
discovery through bioinspired multi-agent intelligent graph reason-
ing,” Advanced Materials, vol. 37, no. 22, p. 2413523, 2025.
[51] A. E. Ghareeb, B. Chang, L. Mitchener, A. Yiu, C. J. Szostkiewicz,
J. M. Laurent, M. T. Razzak, A. D. White, M. M. Hinks, and S. G.
Rodriques, “Robin: A multi-agent system for automating scientific
discovery,” arXiv preprint arXiv:2505.13400, 2025.
[52] A. M. Bran, S. Cox, O. Schilter, C. Baldassari, A. D. White, and
P. Schwaller, “Chemcrow: Augmenting large-language models with
chemistry tools,” arXiv preprint arXiv:2304.05376, 2023.
[53] J. Luo, W. Zhang, Y. Yuan, Y. Zhao, J. Yang, Y. Gu, B. Wu,
B. Chen, Z. Qiao, Q. Long et al., “Large language model agent: A
survey on methodology, applications and challenges,” arXiv preprint
arXiv:2503.21460, 2025.
[54] K. Swanson, W. Wu, N. L. Bulaong, J. E. Pak, and J. Zou, “The
virtual lab of ai agents designs new sars-cov-2 nanobodies,” Nature,
pp. 1–3, 2025.
[55] H. Su, R. Chen, S. Tang, Z. Yin, X. Zheng, J. Li, B. Qi, Q. Wu,
H. Li, W. Ouyang et al., “Many heads are better than one: Improved
scientific idea generation by a llm-based multi-agent system,” arXiv
preprint arXiv:2410.09403, 2024.
[56] Y. Pu, T. Lin, and H. Chen, “Piflow: Principle-aware scientific discov-
ery with multi-agent collaboration,” arXiv preprint arXiv:2505.15047,
2025.
[57] S. Schmidgall, Y. Su, Z. Wang, X. Sun, J. Wu, X. Yu, J. Liu, M. Moor,
Z. Liu, and E. Barsoum, “Agent laboratory: Using llm agents as
research assistants,” arXiv preprint arXiv:2501.04227, 2025.
[58] T. Song, M. Luo, X. Zhang, L. Chen, Y. Huang, J. Cao, Q. Zhu,
D. Liu, B. Zhang, G. Zou et al., “A multiagent-driven robotic ai
chemist enabling autonomous chemical research on demand,” Journal
of the American Chemical Society, vol. 147, no. 15, pp. 12 534–
12 545, 2025.
[59] K. Ding, J. Yu, J. Huang, Y. Yang, Q. Zhang, and H. Chen,
“Scitoolagent: A knowledge graph-driven scientific agent for multi-
tool integration,” 2025. [Online]. Available: https://arxiv.org/abs/
2507.20280
[60] Y. Zhang, X. Chen, B. Jin, S. Wang, S. Ji, W. Wang, and
J. Han, “A comprehensive survey of scientific large language models
and their applications in scientific discovery,” in Proceedings of
the 2024 Conference on Empirical Methods in Natural Language
Processing.
Association for Computational Linguistics, Nov. 2024,
pp. 8783–8817. [Online]. Available: https://aclanthology.org/2024.
emnlp-main.498/
[61] Y. Hasin, M. Seldin, and A. Lusis, “Multi-omics approaches to
disease,” Genome biology, vol. 18, no. 1, p. 83, 2017.
[62] L. Chen, Y. Lu, C.-T. Wu, R. Clarke, G. Yu, J. E. Van Eyk, D. M.
Herrington, and Y. Wang, “Data-driven detection of subtype-specific
differentially expressed genes,” Scientific reports, vol. 11, no. 1, p.
332, 2021.
[63] W. Ruan, Y. Lyu, J. Zhang, J. Cai, P. Shu, Y. Ge, Y. Lu, S. Gao,
Y. Wang, P. Wang et al., “Large language models for bioinformatics,”
arXiv preprint arXiv:2501.06271, 2025.
[64] D. G. York, J. Adelman, J. E. Anderson, S. F. Anderson, J. Annis,
N. A. Bahcall, ..., and D. G. York, “The sloan digital sky survey:
Technical summary,” The Astronomical Journal, vol. 120, no. 3, pp.
1579–1587, 2000.
[65] R. Abbott, T. Abbott, F. Acernese, K. Ackley, C. Adams, N. Adhikari,
R. Adhikari, V. Adya, C. Affeldt, D. Agarwal et al., “Gwtc-3:
Compact binary coalescences observed by ligo and virgo during the
second part of the third observing run,” Physical Review X, vol. 13,
no. 4, p. 041039, 2023.
[66] R. Rozzi, S. Pickett, C. Palmer, J. J. Armesto, and J. B. Callicott,
Linking ecology and ethics for a changing world.
Springer, 2013.
[67] H. A. Simon, “The architecture of complexity,” in The Roots of
Logistics.
Springer, 2012, pp. 335–361.
[68] N. Dan, Y. Cai, and Y. Wang, “Symbolic or numerical? under-
standing physics problem solving in reasoning llms,” arXiv preprint
arXiv:2507.01334, 2025, version 2, July 3, 2025.
[69] R. Wang, B. Wang, K. Li, Y. Zhang, and J. Cheng, “Drsr: Llm
based scientific equation discovery with dual reasoning from data and
experience,” arXiv preprint arXiv:2506.04282, 2025, version 1, June
4, 2025.
[70] A. Jain, S. P. Ong, G. Hautier, W. Chen, W. D. Richards,
S. Dacek, S. Cholia, D. Gunter, D. Skinner, G. Ceder, and
K. A. Persson, “Commentary: The materials project: A materials
genome
approach
to
accelerating
materials
innovation,”
APL
Materials, vol. 1, no. 1, p. 011002, 07 2013. [Online]. Available:
https://doi.org/10.1063/1.4812323
[71] A.
Dunn,
Q.
Wang,
A.
Ganose,
D.
Dopp,
and
A.
Jain,
“Benchmarking materials property prediction methods: the matbench
test set and automatminer reference algorithm,” npj Computational
Materials,
vol.
6,
no.
1,
p.
138,
2020.
[Online].
Available:
https://doi.org/10.1038/s41524-020-00406-3
[72] L. Evans and P. Bryant, “LHC machine,” Journal of Instrumentation,
vol. 3, no. 08, p. S08001, 2008.
[73] S. Steyaert, M. Pizurica, D. Nagaraj, P. Khandelwal, T. Hernandez-
Boussard, A. J. Gentles, and O. Gevaert, “Multimodal data fusion
for cancer biomarker discovery with deep learning,” Nature machine
intelligence, vol. 5, no. 4, pp. 351–362, 2023.
[74] K. M. Boehm, P. Khosravi, R. Vanguri, J. Gao, and S. P. Shah, “Har-
nessing multimodal data integration to advance precision oncology,”
Nature Reviews Cancer, vol. 22, no. 2, pp. 114–126, 2022.
70

[75] Z. Li, X. Yang, K. Choi, W. Zhu, R. Hsieh, H. Kim, J. H. Lim,
S. Ji, B. Lee, X. Yan, L. R. Petzold, S. D. Wilson, W. Lim, and
W. Y. Wang, “Mmsci: A dataset for graduate-level multi-discipline
multimodal scientific understanding,” 2025. [Online]. Available:
https://arxiv.org/abs/2407.04903
[76] M. F. Horstemeyer, “Multiscale modeling: a review,” Practical aspects
of computational chemistry: methods, concepts and applications, pp.
87–135, 2009.
[77] W. Heisenberg, “ ¨Uber den anschaulichen inhalt der quantentheoretis-
chen kinematik und mechanik,” Zeitschrift f¨ur Physik, vol. 43, pp.
172–198, 1927.
[78] P. Brennecke, S. Anders, J. K. Kim, A. A. Kołodziejczyk, X. Zhang,
V. Proserpio, B. Baying, V. Benes, S. A. Teichmann, J. C. Marioni
et al., “Accounting for technical noise in single-cell rna-seq experi-
ments,” Nature methods, vol. 10, no. 11, pp. 1093–1095, 2013.
[79] D. Sivia and J. Skilling, Data analysis: a Bayesian tutorial.
OUP
Oxford, 2006.
[80] P. Lu, S. Mishra, T. Xia, L. Qiu, K.-W. Chang, S.-C. Zhu, O. Tafjord,
P. Clark, and A. Kalyan, “Learn to explain: Multimodal reasoning via
thought chains for science question answering,” Advances in Neural
Information Processing Systems, vol. 35, pp. 2507–2521, 2022.
[81] Y. Wang, X. Ma, G. Zhang, Y. Ni, A. Chandra, S. Guo, W. Ren,
A. Arulraj, X. He, Z. Jiang et al., “Mmlu-pro: A more robust and
challenging multi-task language understanding benchmark,” Advances
in Neural Information Processing Systems, vol. 37, pp. 95 266–95 290,
2024.
[82] Y. Liu, Z. Yang, T. Xie, J. Ni, B. Gao, Y. Li, S. Tang, W. Ouyang,
E. Cambria, and D. Zhou, “Researchbench: Benchmarking llms in
scientific discovery via inspiration-based task decomposition,” arXiv
preprint arXiv:2503.21248, 2025.
[83] Z. Chen, S. Chen, Y. Ning, Q. Zhang, B. Wang, B. Yu, Y. Li,
Z. Liao, C. Wei, Z. Lu, V. Dey, M. Xue, F. N. Baker, B. Burns,
D. Adu-Ampratwum, X. Huang, X. Ning, S. Gao, Y. Su, and H. Sun,
“ScienceAgentBench: Toward rigorous assessment of language agents
for data-driven scientific discovery,” in The Thirteenth International
Conference on Learning Representations, 2025. [Online]. Available:
https://openreview.net/forum?id=6z4YKr0GK6
[84] K. Zhu, H. Du, Z. Hong, X. Yang, S. Guo, Z. Wang, Z. Wang, C. Qian,
X. Tang, H. Ji et al., “Multiagentbench: Evaluating the collaboration
and competition of llm agents,” arXiv preprint arXiv:2503.01935,
2025.
[85] S. Fan, X. Cong, Y. Fu, Z. Zhang, S. Zhang, Y. Liu, Y. Wu,
Y. Lin, Z. Liu, and M. Sun, “Workflowllm: Enhancing workflow
orchestration capability of large language models,” arXiv preprint
arXiv:2411.05451, 2024.
[86] X. Liu, L. Ma, Y. Li, W. Yang, Q. Zhou, J. Song, S. Li, and B. Fei,
“Chemau: Harness the reasoning of llms in chemical research with
adaptive uncertainty estimation,” arXiv preprint arXiv:2506.01116,
2025.
[87] P. Kesseli, P. O’Hearn, and R. S. Cabral, “Logic.py: Bridging the
gap between llms and constraint solvers,” 2025. [Online]. Available:
https://arxiv.org/abs/2502.15776
[88] K. He, R. Mao, Q. Lin, Y. Ruan, X. Lan, M. Feng, and E. Cambria, “A
survey of large language models for healthcare: from data, technology,
and applications to accountability and ethics,” Information Fusion,
vol. 118, p. 102963, 2025.
[89] R. Mousa, A. Sarabadani, T. Taami, A. A. Bengari, O. Eslamifar,
M. A. Shalmani, and E. K. Shahmarvandi, “A comparative survey on
large language models for biological data,” Preprints, 2025. [Online].
Available: https://doi.org/10.20944/preprints202504.2464.v1
[90] J. Wei, Y. Yang, X. Zhang, Y. Chen, X. Zhuang, Z. Gao, D. Zhou,
G. Wang, Z. Gao, J. Cao, Z. Qiu, X. He, Q. Zhang, C. You, S. Zheng,
N. Ding, W. Ouyang, N. Dong, Y. Cheng, S. Sun, L. Bai, and B. Zhou,
“From ai for science to agentic science: A survey on autonomous
scientific discovery,” arXiv preprint arXiv:2508.14111, 2025.
[91] X. Wang, J. Xu, A. H. Feng, Y. Chen, H. Guo, F. Zhu, Y. Shao,
M. Ren, H. Yi, S. Lian, H. Yang, T. Wu, H. Hu, S. Xiang, X.-Y. Zhang,
and C.-L. Liu, “The hitchhiker’s guide to autonomous research: A
survey of scientific agents,” TechRxiv, 2025. [Online]. Available:
http://dx.doi.org/10.36227/techrxiv.175459840.02185500/v1
[92] S. Ni, G. Chen, S. Li, X. Chen, S. Li, B. Wang, Q. Wang, X. Wang,
Y. Zhang, L. Fan, C. Li, R. Xu, L. Sun, and M. Yang, “A survey on
large language model benchmarks,” arXiv preprint arXiv:2508.15361,
2025.
[93] Q. Chen, M. Yang, L. Qin, J. Liu, Z. Yan, J. Guan, D. Peng, Y. Ji,
H. Li, M. Hu et al., “Ai4research: A survey of artificial intelligence
for scientific research,” arXiv preprint arXiv:2507.01903, 2025.
[94] S. Schnell, “Ten simple rules for a computational biologist’s labora-
tory notebook,” p. e1004385, 2015.
[95] D. A. Benson, M. Cavanaugh, K. Clark, I. Karsch-Mizrachi, D. J.
Lipman, J. Ostell, and E. W. Sayers, “Genbank,” Nucleic acids
research, vol. 41, no. D1, pp. D36–D42, 2012.
[96] S. K. Burley, C. Bhikadiya, C. Bi, S. Bittrich, L. Chen, G. V.
Crichlow, C. H. Christie, K. Dalenberg, L. Di Costanzo, J. M. Duarte
et al., “Rcsb protein data bank: powerful new tools for exploring 3d
structures of biological macromolecules for basic and applied research
and education in fundamental biology, biomedicine, biotechnology,
bioengineering and energy sciences,” Nucleic acids research, vol. 49,
no. D1, pp. D437–D451, 2021.
[97] Y. Wang, S. H. Bryant, T. Cheng, J. Wang, A. Gindulyte, B. A.
Shoemaker, P. A. Thiessen, S. He, and J. Zhang, “Pubchem bioassay:
2017 update,” Nucleic acids research, vol. 45, no. D1, pp. D955–
D963, 2017.
[98] S. Kim, J. Chen, T. Cheng, A. Gindulyte, J. He, S. He, Q. Li, B. A.
Shoemaker, P. A. Thiessen, B. Yu et al., “Pubchem 2023 update,”
Nucleic acids research, vol. 51, no. D1, pp. D1373–D1380, 2023.
[99] M. J. Kurtz, G. Eichhorn, A. Accomazzi, C. S. Grant, S. S. Murray,
and J. M. Watson, “The nasa astrophysics data system: Overview,”
Astronomy and astrophysics supplement series, vol. 143, no. 1, pp.
41–59, 2000.
[100] Cornell University. (2025) arxiv. Accessed 7 July 2025. [Online].
Available: https://arxiv.org/
[101] L. L. Kiessling, L. E. Fernandez, A. P. Alivisatos, and P. S. Weiss,
“Chemrxiv: A chemistry preprint server,” pp. 9053–9054, 2016.
[102] P.
P.
Urone
and
R.
Hinrichs,
College
Physics,
2nd
edition,
2nd ed.
Houston, TX: OpenStax, 2022, web version last updated
July 9, 2025; Licensed under Creative Commons Attribution 4.0
International (CC BY 4.0). Accessed 2025-08-26. [Online]. Available:
https://openstax.org/details/books/college-physics-2e
[103] OpenStax, Physics.
Rice University, 2016. [Online]. Available:
https://openstax.org/details/books/physics
[104] R. P. Feynman, R. B. Leighton, and M. Sands, “The feynman
lectures on physics—online edition,” https://www.feynmanlectures.
caltech.edu, 2014, authorised web release of the three-volume classic.
[105] J. Kpodo, P. Kordjamshidi, and A. P. Nejadhashemi, “Agxqa: A
benchmark for advanced agricultural extension question answering,”
Computers and Electronics in Agriculture, vol. 225, p. 109349, 2024.
[106] X. Chen, T. Wang, T. Guo, K. Guo, J. Zhou, H. Li, Z. Song, X. Gao,
and X. Zhang, “Unveiling the power of language models in chemical
research question answering,” Communications Chemistry, vol. 8,
no. 1, p. 4, 2025.
[107] T. Saikh, T. Ghosal, A. Mittal, A. Ekbal, and P. Bhattacharyya,
“Scienceqa: A novel resource for question answering on scholarly
articles,” International Journal on Digital Libraries, vol. 23, no. 3,
pp. 289–301, 2022.
[108] S. Auer, D. A. C. Barone, C. Bartz, E. G. Cortes, M. Y. Jaradeh,
O. Karras, M. Koubarakis, D. Mouromtsev, D. Pliukhin, D. Radyush,
I. Shilin, M. Stocker, and E. Tsalapati, “The sciqa scientific
question answering benchmark for scholarly knowledge,” Scientific
Reports, vol. 13, no. 1, p. 7240, May 2023. [Online]. Available:
https://doi.org/10.1038/s41598-023-33607-z
[109] M. Zaki, Jayadeva, Mausam, and N. M. A. Krishnan, “Mascqa:
A question answering dataset for investigating materials science
knowledge of large language models,” 2023. [Online]. Available:
https://arxiv.org/abs/2308.09115
[110] H. Cui, Z. Shamsi, G. Cheon, X. Ma, S. Li, M. Tikhanovskaya, P. C.
Norgaard, N. Mudur, M. B. Plomecka, P. Raccuglia et al., “Curie:
Evaluating llms on multitask scientific long-context understanding and
reasoning,” in The Thirteenth International Conference on Learning
Representations, 2025.
[111] D. A. Zarin, T. Tse, R. J. Williams, R. M. Califf, and N. C. Ide,
“The clinicaltrials. gov results database—update and key issues,” New
England Journal of Medicine, vol. 364, no. 9, pp. 852–860, 2011.
[112] D. B. Resnik, The ethics of research with human subjects: Protecting
people, advancing science, promoting trust.
Springer, 2018, vol. 74.
[113] D. Baltimore, P. Berg, M. Botchan, D. Carroll, R. A. Charo,
G. Church, J. E. Corn, G. Q. Daley, J. A. Doudna, M. Fenner et al.,
“A prudent path forward for genomic engineering and germline gene
modification,” Science, vol. 348, no. 6230, pp. 36–38, 2015.
[114] P. B. Jensen, L. J. Jensen, and S. Brunak, “Mining electronic health
records: towards better research applications and clinical care,” Nature
Reviews Genetics, vol. 13, no. 6, pp. 395–405, 2012.
[115] B. Shickel, P. J. Tighe, A. Bihorac, and P. Rashidi, “Deep ehr: a
survey of recent advances in deep learning techniques for electronic
71

health record (ehr) analysis,” IEEE journal of biomedical and health
informatics, vol. 22, no. 5, pp. 1589–1604, 2017.
[116] Zooniverse Team. (2007) Galaxy zoo. Citizen science project
for galaxy classification, part of the Zooniverse platform. [Online].
Available: https://www.zooniverse.org/projects/zookeeper/galaxy-zoo/
[117] S. Kelling, W. M. Hochachka, D. Fink, M. Riedewald, R. Caruana,
G. Ballard, and G. Hooker, “Data-intensive science: a new paradigm
for biodiversity studies,” BioScience, vol. 59, no. 7, pp. 613–620,
2009.
[118] I. Thiele and B. Ø. Palsson, “A protocol for generating a high-quality
genome-scale metabolic reconstruction,” Nature protocols, vol. 5,
no. 1, pp. 93–121, 2010.
[119] B. Palsson, Systems biology.
Cambridge university press, 2015.
[120] M. Wu, Y. Wang, Y. Ming, Y. An, Y. Wan, W. Chen, B. Lin, Y. Li,
T. Xie, and D. Zhou, “Chematagent: Enhancing llms for chemistry
and materials science through tree-search based tool learning,” 2025.
[Online]. Available: https://arxiv.org/abs/2506.07551
[121] X. Tang, B. Qian, R. Gao, J. Chen, X. Chen, and M. B. Gerstein,
“Biocoder: a benchmark for bioinformatics code generation with large
language models,” Bioinformatics, vol. 40, no. Supplement 1, pp.
i266–i276, 2024.
[122] M. Tian, L. Gao, S. D. Zhang, X. Chen, C. Fan, X. Guo, R. Haas,
P. Ji, K. Krongchon, Y. Li, S. Liu, D. Luo, Y. Ma, H. Tong, K. Trinh,
C. Tian, Z. Wang, B. Wu, Y. Xiong, S. Yin, M. Zhu, K. Lieret, Y. Lu,
G. Liu, Y. Du, T. Tao, O. Press, J. Callan, E. Huerta, and H. Peng,
“Scicode: A research coding benchmark curated by scientists,” 2024.
[123] J. Gurevitch, J. Koricheva, S. Nakagawa, and G. Stewart, “Meta-
analysis and the science of research synthesis,” Nature, vol. 555, no.
7695, pp. 175–182, 2018.
[124] A. Ali, N. Zhang, and R. M. Santos, “Mineral characterization using
scanning electron microscopy (sem): a review of the fundamentals,
advancements, and research directions,” Applied Sciences, vol. 13,
no. 23, p. 12600, 2023.
[125] D. Liu, Q. Zeng, C. Hu, D. Chen, H. Liu, Y. Han, L. Xu, Q. Zhang,
and J. Yang, “Light doping of tungsten into copper-platinum nanoal-
loys for boosting their electrocatalytic performance in methanol
oxidation,” Nano Res. Energy, vol. 1, no. 2, p. e9120017, 2022.
[126] C. T´obi, N. Q. Kh´anh, Z. Homonnay, and ´E. Sz´eles, “Applicability of
atomic force microscopy for nuclear forensic examination,” Journal of
Radioanalytical and Nuclear Chemistry, vol. 334, no. 1, pp. 753–761,
2025.
[127] V. Mansurov, T. Malin, S. Teys, V. Atuchin, D. Milakhin, and
K. Zhuravlev, “Stm/sts study of the density of states and contrast
behavior at the boundary between (7× 7) n and (8× 8) structures in
the sin/si (111) system,” Crystals, vol. 12, no. 12, p. 1707, 2022.
[128] S. Woo, H. Jung, and Y. Yoon, “Real-time uv/vis spectroscopy to
observe photocatalytic degradation,” Catalysts, vol. 13, no. 4, p. 683,
2023.
[129] Z. Fan, T. Hwang, S. Lin, Y. Chen, and Z. J. Wong, “Directional
thermal emission and display using pixelated non-imaging micro-
optics,” Nature Communications, vol. 15, no. 1, p. 4544, 2024.
[130] Y. Zhao, Z. Nie, H. Hong, X. Qiu, S. Han, Y. Yu, M. Liu, X. Qiu,
K. Liu, S. Meng et al., “Spectroscopic visualization and phase
manipulation of chiral charge density waves in 1t-tas2,” Nature
Communications, vol. 14, no. 1, p. 2223, 2023.
[131] T. Meier, A. Aslandukova, F. Trybel, D. Laniel, T. Ishii, S. Khan-
darkhaeva, N. Dubrovinskaia, and L. Dubrovinsky, “In situ high-
pressure nuclear magnetic resonance crystallography in one and two
dimensions,” Matter and Radiation at Extremes, vol. 6, no. 6, 2021.
[132] J. I. Goldstein, D. E. Newbury, D. C. Joy, C. E. Lyman, P. Echlin,
E. Lifshin, L. Sawyer, and J. R. Michael, Scanning Electron Mi-
croscopy and X-ray Microanalysis, 4th ed.
Springer, 2018.
[133] D. B. Williams and C. B. Carter, Transmission Electron Microscopy:
A Textbook for Materials Science, 2nd ed.
Springer, 2009.
[134] G. Binnig, C. F. Quate, and C. Gerber, “Atomic force microscope,”
Physical Review Letters, vol. 56, no. 9, pp. 930–933, 1986.
[135] G. Binnig and H. Rohrer, “Scanning tunneling microscope,” Re-
vista de F´ısica: Estudios en F´ısica, vol. 0, pp. 3–5, 1982, nobel
Prize–winning invention; original publication in 1981.
[136] D. A. Skoog, F. J. Holler, and S. R. Crouch, Principles of Instrumental
Analysis, 7th ed.
Cengage Learning, 2017.
[137] B. Stuart, Infrared Spectroscopy: Fundamentals and Applications.
John Wiley & Sons, 2004.
[138] J. R. Ferraro, K. Nakamoto, and C. W. Brown, Introductory Raman
Spectroscopy, 2nd ed.
Academic Press, 2003.
[139] T. D. W. Claridge, High-Resolution NMR Techniques in Organic
Chemistry, 3rd ed.
Elsevier, 2016.
[140] X.-Y. Lu, H.-P. Wu, H. Ma, H. Li, J. Li, Y.-T. Liu, Z.-Y. Pan, Y. Xie,
L. Wang, B. Ren et al., “Deep learning-assisted spectrum–structure
correlation: state-of-the-art and perspectives,” Analytical Chemistry,
vol. 96, no. 20, pp. 7959–7975, 2024.
[141] X. Liu, H. An, W. Cai, and X. Shao, “Deep learning in spectral anal-
ysis: Modeling and imaging,” TrAC Trends in Analytical Chemistry,
vol. 172, p. 117612, 2024.
[142] F. Pont´en, K. Jirstr¨om, and M. Uhlen, “The human protein atlas—a
tool for pathology,” The Journal of Pathology: A Journal of the
Pathological Society of Great Britain and Ireland, vol. 216, no. 4,
pp. 387–393, 2008.
[143] V. Ljosa, K. L. Sokolnicki, and A. E. Carpenter, “Annotated high-
throughput microscopy image sets for validation,” Nature Methods,
vol. 9, no. 7, p. 637, 2012.
[144] C.
Gohlke,
“cgohlke/tifffile:
v2022.5.4,”
https://doi.org/10.5281/
zenodo.6795861, Jul. 2022, version v2022.5.4.
[145] Nikon
Instruments
Inc.,
“NIS-Elements
Viewer:
Free
nd2
image-viewer,”
https://www.microscope.healthcare.nikon.com/
products/software/nis-elements/software-resources,
2020,
version
5.21.00.
[146] A. Lozano, J. Nirschl, J. Burgess, S. R. Gupte, Y. Zhang, A. Unell,
and S. Yeung, “Micro-bench: A microscopy benchmark for vision-
language understanding,” Advances in Neural Information Processing
Systems, vol. 37, pp. 30 670–30 685, 2024.
[147] J. Burgess, J. J. Nirschl, L. Bravo-S´anchez, A. Lozano, S. R. Gupte,
J. G. Galaz-Montoya, Y. Zhang, Y. Su, D. Bhowmik, Z. Coman et al.,
“Microvqa: A multimodal reasoning benchmark for microscopy-based
scientific research,” in Proceedings of the Computer Vision and
Pattern Recognition Conference, 2025, pp. 19 552–19 564.
[148] C. Hutter and J. C. Zenklusen, “The cancer genome atlas: creating
lasting value beyond its data,” Cell, vol. 173, no. 2, pp. 283–285,
2018.
[149] N. J. Edwards, M. Oberti, R. R. Thangudu, S. Cai, P. B. McGarvey,
S. Jacob, S. Madhavan, and K. A. Ketchum, “The CPTAC data portal:
a resource for cancer proteomics research,” Journal of proteome
research, vol. 14, no. 6, pp. 2707–2713, 2015.
[150] X. He, Y. Zhang, L. Mou, E. Xing, and P. Xie, “Pathvqa: 30000+
questions for medical visual question answering,” arXiv preprint
arXiv:2003.10286, 2020.
[151] W. Ikezogwo, S. Seyfioglu, F. Ghezloo, D. Geva, F. Sheikh Mo-
hammed, P. K. Anand, R. Krishna, and L. Shapiro, “Quilt-1M: One
million image-text pairs for histopathology,” Advances in Neural
Information Processing Systems, vol. 36, pp. 37 995–38 017, 2023.
[152] Y. Chen, G. Wang, Y. Ji, Y. Li, J. Ye, T. Li, M. Hu, R. Yu, Y. Qiao,
and J. He, “Slidechat: A large vision-language assistant for whole-
slide pathology image understanding,” in Proceedings of the Computer
Vision and Pattern Recognition Conference, 2025, pp. 5134–5143.
[153] X. Zhao, W. Xu, B. Liu, Y. Zhou, F. Ling, B. Fei, X. Yue,
L. Bai, W. Zhang, and X.-M. Wu, “Msearth: A benchmark for
multimodal scientific comprehension of earth science,” arXiv preprint
arXiv:2505.20740, 2025.
[154] A. E. Johnson, T. J. Pollard, S. J. Berkowitz, N. R. Greenbaum, M. P.
Lungren, C.-y. Deng, R. G. Mark, and S. Horng, “MIMIC-CXR, a
de-identified publicly available database of chest radiographs with
free-text reports,” Scientific data, vol. 6, no. 1, p. 317, 2019.
[155] D. Demner-Fushman, M. D. Kohli, M. B. Rosenman, S. E. Shooshan,
L. Rodriguez, S. Antani, G. R. Thoma, and C. J. McDonald,
“Preparing a collection of radiology examinations for distribution and
retrieval,” Journal of the American Medical Informatics Association,
vol. 23, no. 2, pp. 304–310, 2015.
[156] Y. Ji, H. Bai, C. Ge, J. Yang, Y. Zhu, R. Zhang, Z. Li, L. Zhanng,
W. Ma, X. Wan et al., “Amos: A large-scale abdominal multi-organ
benchmark for versatile medical image segmentation,” Advances in
Neural Information Processing Systems, vol. 35, pp. 36 722–36 732,
2022.
[157] I. E. Hamamci, S. Er, C. Wang, F. Almas, A. G. Simsek, S. N. Esirgun,
I. Doga, O. F. Durugol, W. Dai, M. Xu et al., “Developing generalist
foundation models from a multimodal dataset for 3d computed
tomography,” arXiv preprint arXiv:2403.17834, 2024.
[158] National Lung Screening Trial Research Team, “Data from the
national lung screening trial (nlst),” 2013. [Online]. Available:
https://www.cancerimagingarchive.net/collection/nlst/
[159] N. Kumar, R. Verma, S. Sharma, S. Bhargava, A. Vahadane, and
A. Sethi, “A dataset and a technique for generalized nuclear segmen-
tation for computational pathology,” IEEE transactions on medical
imaging, vol. 36, no. 7, pp. 1550–1560, 2017.
72

[160] T. Wald, C. Ulrich, J. Suprijadi, S. Ziegler, M. Nohel, R. Peretzke,
G. K¨ohler, and K. H. Maier-Hein, “An openmind for 3d medical vision
self-supervised learning,” arXiv preprint arXiv:2412.17041, 2024.
[161] T. A. D’Antonoli, L. K. Berger, A. K. Indrakanti, N. Vishwanathan,
J. Weiß, M. Jung, Z. Berkarda, A. Rau, M. Reisert, T. K¨ustner
et al., “Totalsegmentator mri: Robust sequence-independent seg-
mentation of multiple anatomic structures in mri,” arXiv preprint
arXiv:2405.19492, 2024.
[162] W. Al-Dhabyani, M. Gomaa, H. Khaled, and A. Fahmy, “Dataset of
breast ultrasound images,” Data in Brief, vol. 28, p. 104863, 2020.
[Online]. Available: https://www.sciencedirect.com/science/article/pii/
S2352340919312181
[163] Y. Yang, Y. Chen, X. Dong, J. Zhang, C. Long, Z. Jin, and Y. Dai,
“An annotated heterogeneous ultrasound database,” Scientific Data,
vol. 12, no. 1, p. 148, 2025.
[164] S. Gatidis, T. Hepp, M. Fr¨uh, C. La Foug`ere, K. Nikolaou, C. Pfan-
nenberg, B. Sch¨olkopf, T. K¨ustner, C. Cyran, and D. Rubin, “A whole-
body FDG-PET/CT dataset with manually annotated tumor lesions,”
Scientific Data, vol. 9, no. 1, p. 601, 2022.
[165] S. Gatidis, M. Fr¨uh, M. Fabritius, S. Gu, K. Nikolaou, C. La Foug`ere,
J. Ye, J. He, Y. Peng, L. Bi et al., “Results from the autoPET chal-
lenge on fully automated lesion segmentation in oncologic PET/CT
imaging,” Nature Machine Intelligence, vol. 6, no. 11, pp. 1396–1405,
2024.
[166] J. Suckling, “The mammographic images analysis society digital
mammogram database,” in Exerpta Medica. International Congress
Series, 1994, vol. 1069, 1994, pp. 375–378.
[167] N. E. M. Association et al., “Digital imaging and communication
in medicine (DICOM),” NEMA PS 3 Supplement 23 Structured
Reporting, 1997.
[168] R. Cox, J. Ashburner, H. Breman, K. Fissell, C. Haselgrove,
C. Holmes, J. Lancaster, D. Rex, S. Smith, J. Woodward, and
S. Strother, “A (sort of) new image data format standard: NiFTI-1,” in
10th Annual Meeting of the Organization for Human Brain Mapping,
vol. 22, 01 2004.
[169] Medixant, “RadiAnt DICOM viewer,” https://www.radiantviewer.
com, version 2021.1.
[170] C. Rorden, “MRIcroGL: Open-source 2d/3d neuroimaging viewer,”
https://github.com/rordenlab/MRIcroGL, 2025, version v1.2.
[171] D. Mason, scaramallion, mrbean bremen, rhaxton, J. Suever, D. P.
Orfanos, Vanessasaurus, G. Lemaitre, A. Panchal, A. Rothberg,
M. D. Herrmann, J. Massich, J. Kerns, K. van Golen, C. Bridge,
S. Biggs, T. Robitaille, moloney, M. Shun-Shin, B. Conrad, pawelza-
jdel, M. Mattes, Y. Lyu, T. Cogan, Z. Baratz, F. C. Morency, Taylor,
and T. Sentner, “pydicom/pydicom: pydicom 3.0.1,” https://doi.org/
10.5281/zenodo.13824606, Sep. 2024, version v3.0.1.
[172] B. C. Lowekamp, D. T. Chen, L. Ib´a˜nez, and D. Blezek, “The design
of SimpleITK,” Frontiers in Neuroinformatics, vol. 7, p. 45, 2013.
[173] J. Staal, M. D. Abr`amoff, M. Niemeijer, M. A. Viergever, and
B. Van Ginneken, “Ridge-based vessel segmentation in color images
of the retina,” IEEE Transactions on Medical Imaging, vol. 23, no. 4,
pp. 501–509, 2004.
[174] A. Hoover, V. Kouznetsova, and M. Goldbaum, “Locating blood
vessels in retinal images by piecewise threshold probing of a matched
filter response,” IEEE Transactions on Medical Imaging, vol. 19,
no. 3, pp. 203–210, 2000.
[175] C. De Vente, K. A. Vermeer, N. Jaccard, H. Wang, H. Sun, F. Khader,
D. Truhn, T. Aimyshev, Y. Zhanibekuly, T.-D. Le et al., “AIROGS:
Artificial intelligence for robust glaucoma screening challenge,” IEEE
Transactions on Medical Imaging, vol. 43, no. 1, pp. 542–557, 2023.
[176] R. Wu, C. Zhang, J. Zhang, Y. Zhou, T. Zhou, and H. Fu, “Mm-retinal:
Knowledge-enhanced foundational pretraining with fundus image-text
expertise,” in International Conference on Medical Image Computing
and Computer-Assisted Intervention.
Springer, 2024, pp. 722–732.
[177] L. Ding, A. E. Kuriyan, R. S. Ramchandran, C. C. Wykoff, and
G. Sharma, “PRIME-FP20: Ultra-widefield fundus photography vessel
segmentation dataset,” IEEE Dataport, 2020, [Online]. Available:
http://dx.doi.org/10.21227/ctgj-1367.
[178] X. Liang, M. Bian, M. Chen, L. Liu, J. He, J. Xu, and L. Li,
“A novel ophthalmic benchmark for evaluating multimodal large
language models with fundus photographs and oct images,” arXiv
preprint arXiv:2503.07094, 2025.
[179] D. S. Kermany, M. Goldbaum, W. Cai, C. C. Valentim, H. Liang,
S. L. Baxter, A. McKeown, G. Yang, X. Wu, F. Yan et al., “Identi-
fying medical diagnoses and treatable diseases by image-based deep
learning,” Cell, vol. 172, no. 5, pp. 1122–1131, 2018.
[180] P. Tschandl, C. Rosendahl, and H. Kittler, “The HAM10000 dataset,
a large collection of multi-source dermatoscopic images of common
pigmented skin lesions,” Scientific data, vol. 5, no. 1, pp. 1–9, 2018.
[181] N. Codella, V. Rotemberg, P. Tschandl, M. E. Celebi, S. Dusza,
D. Gutman, B. Helba, A. Kalloo, K. Liopyris, M. Marchetti et al.,
“Skin lesion analysis toward melanoma detection 2018: A challenge
hosted by the international skin imaging collaboration (isic),” arXiv
preprint arXiv:1902.03368, 2019.
[182] M. Hu, P. Xia, L. Wang, S. Yan, F. Tang, Z. Xu, Y. Luo, K. Song,
J. Leitner, X. Cheng et al., “Ophnet: A large-scale video benchmark
for ophthalmic surgical workflow understanding,” in European Con-
ference on Computer Vision.
Springer, 2024, pp. 481–500.
[183] M. Hu, L. Wang, S. Yan, D. Ma, Q. Ren, P. Xia, W. Feng, P. Duan,
L. Ju, and Z. Ge, “Nurvid: A large expert-level video database
for nursing procedure activity understanding,” Advances in Neural
Information Processing Systems, vol. 36, pp. 18 146–18 164, 2023.
[184] M. Hu, Z. Yu, F. Tang, K. Chen, Y. Li, I. Razzak, J. He, T. Birdal,
K. Zhou, and Z. Ge, “Towards dynamic 3d reconstruction of
hand-instrument interaction in ophthalmic surgery,” arXiv preprint
arXiv:2505.17677, 2025.
[185] W. Li, M. Hu, G. Wang, L. Liu, K. Zhou, J. Ning, X. Guo,
Z. Ge, L. Gu, and J. He, “Ophora: A large-scale data-driven text-
guided ophthalmic surgical video generation model,” arXiv preprint
arXiv:2505.07449, 2025.
[186] D. Jha, P. H. Smedsrud, M. A. Riegler, P. Halvorsen, T. De Lange,
D. Johansen, and H. D. Johansen, “Kvasir-seg: A segmented
polyp dataset,” in International conference on multimedia modeling.
Springer, 2019, pp. 451–462.
[187] A. P. Twinanda, S. Shehata, D. Mutter, J. Marescaux, M. De Mathelin,
and N. Padoy, “Endonet: a deep architecture for recognition tasks on
laparoscopic videos,” IEEE Transactions on Medical Imaging, vol. 36,
no. 1, pp. 86–97, 2016.
[188] Endoscopic Vision Challenge Organizers, “Endoscopic Vision Chal-
lenge 2025,” https://opencas.dkfz.de/endovis/challenges/2025/, 2025,
accessed: 2025-07-12.
[189] G. Van Horn, O. Mac Aodha, Y. Song, Y. Cui, C. Sun, A. Shepard,
H. Adam, P. Perona, and S. Belongie, “The inaturalist species classi-
fication and detection dataset,” in Proceedings of the IEEE conference
on computer vision and pattern recognition, 2018, pp. 8769–8778.
[190] M. Arbab Arshad, T. Zaki Jubery, T. Roy, R. Nassiri, A. K. Singh,
A. Singh, C. Hegde, B. Ganapathysubramanian, A. Balu, A. Kr-
ishnamurthy et al., “Ageval: A benchmark for zero-shot and few-
shot plant stress phenotyping with multimodal llms,” arXiv preprint
arXiv:2407.19617, 2024.
[191] V. Dongre, C. Gui, S. Garg, H. Nayyeri, G. Tur, D. Hakkani-T¨ur,
and V. S. Adve, “Mirage: A benchmark for multimodal information-
seeking and reasoning in agricultural expert-guided conversations,”
arXiv preprint arXiv:2506.20100, 2025.
[192] M. T. Chiu, X. Xu, Y. Wei, Z. Huang, A. G. Schwing, R. Brunner,
H. Khachatrian, H. Karapetyan, I. Dozier, G. Rose et al., “Agriculture-
vision: A large aerial image database for agricultural pattern analysis,”
in Proceedings of the IEEE/CVF Conference on Computer Vision and
Pattern Recognition, 2020, pp. 2828–2838.
[193] C. Justice, J. Townshend, E. Vermote, E. Masuoka, R. Wolfe,
N. Saleous, D. Roy, and J. Morisette, “An overview of modis land
data processing and product status,” Remote sensing of Environment,
vol. 83, no. 1-2, pp. 3–15, 2002.
[194] A. Moreira, P. Prats-Iraola, M. Younis, G. Krieger, I. Hajnsek, and
K. P. Papathanassiou, “A tutorial on synthetic aperture radar,” IEEE
Geoscience and remote sensing magazine, vol. 1, no. 1, pp. 6–43,
2013.
[195] H. Hersbach, B. Bell, P. Berrisford, S. Hirahara, A. Hor´anyi,
J. Mu˜noz-Sabater, J. Nicolas, C. Peubey, R. Radu, D. Schepers
et al., “The era5 global reanalysis,” Quarterly journal of the royal
meteorological society, vol. 146, no. 730, pp. 1999–2049, 2020.
[196] S. Rasp, P. D. Dueben, S. Scher, J. A. Weyn, S. Mouatadid, and
N. Thuerey, “Weatherbench: a benchmark data set for data-driven
weather forecasting,” Journal of Advances in Modeling Earth Systems,
vol. 12, no. 11, p. e2020MS002203, 2020.
[197] A. R. Thompson, J. M. Moran, and G. W. Swenson, Interferometry
and Synthesis in Radio Astronomy, 3rd ed.
Springer, 2017.
[198] “Hubble space telescope,” https://www.stsci.edu/hst, 2025, operated
by NASA and ESA; high-resolution optical and UV imaging.
[199] J. P. Gardner, J. C. Mather, M. Clampin, R. Doyon, M. A. Greenhouse,
H. B. Hammel, J. B. Hutchings, P. Jakobsen, S. J. Lilly, K. S. Long
et al., “The james webb space telescope,” Space Science Reviews, vol.
123, no. 4, pp. 485–606, 2006.
73

[200] G. Zhao, Y.-H. Zhao, Y.-Q. Chu, Y.-P. Jing, and L.-C. Deng, “Lamost
spectral survey—an overview,” Research in Astronomy and Astro-
physics, vol. 12, no. 7, p. 723, 2012.
[201] Q. Tan, D. Zhou, P. Xia, W. Liu, W. Ouyang, L. Bai, Y. Li, and
T. Fu, “Chemmllm: Chemical multimodal large language model,”
arXiv preprint arXiv:2505.16326, 2025.
[202] C. Edwards, T. Lai, K. Ros, G. Honke, K. Cho, and H. Ji, “Translation
between molecules and natural language,” in 2022 Conference on
Empirical Methods in Natural Language Processing, EMNLP 2022.
Association for Computational Linguistics (ACL), 2022, pp. 375–413.
[203] T. Fu, C. Xiao, L. M. Glass, and J. Sun, “Moler: Incorporate
molecule-level reward to enhance deep generative model for molecule
optimization,” IEEE transactions on knowledge and data engineering,
vol. 34, no. 11, pp. 5459–5471, 2021.
[204] A. Lozano, M. W. Sun, J. Burgess, L. Chen, J. J. Nirschl, J. Gu,
I. Lopez, J. Aklilu, A. Rau, A. W. Katzer et al., “Biomedica: An
open biomedical image-caption archive, dataset, and vision-language
models derived from scientific literature,” in Proceedings of the
Computer Vision and Pattern Recognition Conference, 2025, pp.
19 724–19 735.
[205] W. Lin, Z. Zhao, X. Zhang, C. Wu, Y. Zhang, Y. Wang, and
W. Xie, “PMC-CLIP: Contrastive language-image pre-training using
biomedical documents,” in International Conference on Medical Im-
age Computing and Computer-Assisted Intervention. Springer, 2023,
pp. 525–536.
[206] A. Kembhavi, M. Salvato, E. Kolve, M. Seo, H. Hajishirzi, and
A. Farhadi, “A diagram is worth a dozen images,” in European
Conference on Computer Vision.
Springer International Publishing,
2016, pp. 235–251.
[207] K. V. Jobin, A. Mondal, and C. V. Jawahar, “DocFigure: A dataset
for scientific document figure classification,” in 2019 International
Conference on Document Analysis and Recognition Workshops (IC-
DARW), vol. 1, 2019, pp. 74–79.
[208] N. Alampara, I. Mandal, P. Khetarpal, H. S. Grover, M. Schilling-
Wilhelmi, N. M. A. Krishnan, and K. M. Jablonka, “MaCBench:
A multimodal chemistry and materials science benchmark,” in AI
for Accelerated Materials Design - NeurIPS 2024, 2024. [Online].
Available: https://openreview.net/forum?id=Q2PNocDcp6
[209] D. Weininger, “Smiles, a chemical language and information system.
1. introduction to methodology and encoding rules,” Journal of
chemical information and computer sciences, vol. 28, no. 1, pp. 31–
36, 1988.
[210] S. R. Heller and A. D. McNaught, “The iupac international chemical
identifier (inchi),” Chemistry International, vol. 31, no. 1, p. 7, 2009.
[211] M. Krenn, Q. Ai, S. Barthel, N. Carson, A. Frei et al., “SELFIES
and the future of molecular string representations,” arXiv:2204.00056,
2022.
[212] T.-S. Lin, C. W. Coley, H. Mochigase, H. K. Beech, W. Wang,
Z. Wang, E. Woods, S. L. Craig, J. A. Johnson, J. A. Kalow
et al., “BigSMILES: a structurally-based line notation for describing
macromolecules,” ACS Central Science, vol. 5, no. 9, pp. 1523–1531,
2019.
[213] M. Krenn, F. H¨ase, A. Nigam, P. Friederich, and A. Aspuru-
Guzik, “Self-referencing embedded strings (SELFIES): A 100% ro-
bust molecular string representation,” Machine Learning: Science and
Technology, vol. 1, no. 4, p. 045024, 2020.
[214] C. W. Coley, R. Barzilay, W. H. Green, T. S. Jaakkola, and K. F.
Jensen, “Convolutional embedding of attributed molecular graphs for
physical property prediction,” Journal of chemical information and
modeling, vol. 57, no. 8, pp. 1757–1772, 2017.
[215] W. Gao, T. Fu, J. Sun, and C. W. Coley, “Sample efficiency matters:
benchmarking molecular optimization,” Neural Information Process-
ing Systems (NeurIPS) Track on Datasets and Benchmarks, 2022.
[216] J. J. Irwin, T. Sterling, M. M. Mysinger, E. S. Bolstad, and R. G.
Coleman, “ZINC: a free tool to discover chemistry for biology,”
Journal of chemical information and modeling, vol. 52, no. 7, pp.
1757–1768, 2012.
[217] A. Gaulton, L. J. Bellis, A. P. Bento, J. Chambers, M. Davies,
A. Hersey, Y. Light, S. McGlinchey, D. Michalovich, B. Al-Lazikani
et al., “ChEMBL: a large-scale bioactivity database for drug discov-
ery,” Nucleic acids research, vol. 40, no. D1, pp. D1100–D1107, 2012.
[218] D. Lowe, “Chemical reactions from US patents (1976-Sep2016),”
6
2017.
[Online].
Available:
https://figshare.com/articles/dataset/
Chemical reactions from US patents 1976-Sep2016 /5104873
[219] Z. Wu, B. Ramsundar, E. N. Feinberg, J. Gomes, C. Geniesse,
A.
S.
Pappu,
K.
Leswing,
and
V.
Pande,
“Moleculenet:
A
benchmark
for
molecular
machine
learning,”
2018.
[Online].
Available: https://arxiv.org/abs/1703.00564
[220] M. D. Cranmer, R. Xu, P. Battaglia, and S. Ho, “Learning sym-
bolic physics with graph networks,” in Proc. NeurIPS Workshop on
Machine Learning and the Physical Sciences, 2019, arXiv preprint
arXiv:1909.05862.
[221] J. Ying, H. Lin, C. Yue, Y. Chen, C. Xiao, Q. Shi, Y. Liang, S.-T. Yau,
Y. Zhou, and J. Ma, “A neural symbolic model for space physics,”
arXiv preprint arXiv:2503.07994, 2025.
[222] V. Angelopoulos, “The themis mission,” Space Science Reviews, vol.
141, no. 1, pp. 5–34, 2008.
[223] S.-M. Udrescu and M. Tegmark, “Ai feynman: A physics-inspired
method for symbolic regression,” Science advances, vol. 6, no. 16, p.
eaay2631, 2020.
[224] S.-M. Udrescu, A. Tan, J. Feng, O. Neto, T. Wu, and M. Tegmark,
“Ai feynman 2.0: Pareto-optimal symbolic regression exploiting graph
modularity,” Advances in Neural Information Processing Systems,
vol. 33, pp. 4860–4871, 2020.
[225] A. Mu˜noz-Jaramillo and J. M. Vaquero, “Visualization of the chal-
lenges and limitations of the long-term sunspot number record,”
Nature Astronomy, vol. 3, no. 3, pp. 205–211, 2019.
[226] P. Constantin and C. Foias¸, Navier-stokes equations.
University of
Chicago press, 1988.
[227] P. Bormann, B. Engdahl, and R. Kind, “Seismic wave propagation and
earth models,” in New manual of seismological observatory practice
2 (NMSOP2).
Deutsches GeoForschungsZentrum GFZ, 2012, pp.
1–105.
[228] D. Y. Le Roux, A. Staniforth, and C. A. Lin, “Finite elements for
shallow-water equation ocean models,” Monthly Weather Review, vol.
126, no. 7, pp. 1931–1951, 1998.
[229] R. Edgar, M. Domrachev, and A. E. Lash, “Gene expression omnibus:
Ncbi gene expression and hybridization array data repository,” Nucleic
Acids Research, vol. 30, no. 1, pp. 207–210, 2002.
[230] S. T. Sherry et al., “dbsnp: the ncbi database of genetic variation,”
Nucleic Acids Research, vol. 29, no. 1, pp. 308–311, 2001.
[231] T. Han, S. Guo, Z. Chen, W. Xu, and L. Bai, “Weather-5k: A large-
scale global station weather dataset towards comprehensive time-
series forecasting benchmark,” arXiv e-prints, pp. arXiv–2406, 2024.
[232] F. Cunningham, J. E. Allen, J. Allen, J. Alvarez-Jarreta, M. R.
Amode, I. M. Armean, O. Austine-Orimoloye, A. G. Azov, I. Barnes,
R. Bennett et al., “Ensembl 2022,” Nucleic acids research, vol. 50,
no. D1, pp. D988–D995, 2022.
[233] T. U. Consortium, “Uniprot: the universal protein knowledgebase in
2023,” Nucleic Acids Research, vol. 51, no. D1, pp. D523–D531,
2023.
[234] D. L. McGuinness, F. Van Harmelen et al., “OWL web ontology
language overview,” W3C recommendation, vol. 10, no. 10, p. 2004,
2004.
[235] B. Smith et al., “The obo foundry: coordinated evolution of ontologies
to support biomedical data integration,” Nature Biotechnology, vol. 25,
no. 11, pp. 1251–1255, 2007.
[236] M. Ashburner, C. A. Ball, J. A. Blake, D. Botstein, H. Butler, J. M.
Cherry, A. P. Davis, K. Dolinski, S. S. Dwight, J. T. Eppig et al.,
“Gene ontology: tool for the unification of biology,” Nature genetics,
vol. 25, no. 1, pp. 25–29, 2000.
[237] S. K¨ohler et al., “The human phenotype ontology in 2021,” Nucleic
Acids Research, vol. 49, no. D1, pp. D1207–D1217, 2021.
[238] J. Lin, L. Wang, X. Lu, Z. Hu, W. Zhang, and W. Lu, “Improving
knowledge graph completion with structure-aware supervised con-
trastive learning,” in Proceedings of the 2024 conference on empirical
methods in natural language processing, 2024, pp. 13 948–13 959.
[239] K. Liang, L. Meng, M. Liu, Y. Liu, W. Tu, S. Wang, S. Zhou, X. Liu,
F. Sun, and K. He, “A survey of knowledge graph reasoning on
graph types: Static, dynamic, and multi-modal,” IEEE Transactions
on Pattern Analysis and Machine Intelligence, vol. 46, no. 12, pp.
9456–9478, 2024.
[240] O. Bodenreider, “The unified medical language system (umls): inte-
grating biomedical terminology,” Nucleic Acids Research, vol. 32, no.
suppl 1, pp. D267–D270, 2004.
[241] P. Chandak, K. Huang, and M. Zitnik, “Building a knowledge graph
to enable precision medicine,” Scientific Data, vol. 10, no. 1, p. 67,
2023.
[242] H. Li, Z. Wang, J. Wang, A. K. H. Lau, and H. Qu, “Cllmate: A
multimodal llm for weather and climate events forecasting,” arXiv
preprint arXiv:2409.19058, 2024.
74

[243] E. Anderson, G. D. Veith, and D. Weininger, SMILES, a line notation
and computerized interpreter for chemical structures.
US Environ-
mental Protection Agency, Environmental Research Laboratory, 1987.
[244] K. Huang, T. Fu, W. Gao, Y. Zhao, Y. Roohani, J. Leskovec, C. W.
Coley, C. Xiao, J. Sun, and M. Zitnik, “Therapeutics data commons:
machine learning datasets and tasks for therapeutics,” NeurIPS Track
Datasets and Benchmarks, 2021.
[245] CODATA Task Group on Fundamental Constants, “Codata recom-
mended values of the fundamental physical constants: 2022,” https:
//physics.nist.gov/cuu/pdf/wall 2022.pdf, 2024, may 2024 update of
CODATA 2022 constants.
[246] Particle Data Group, “Review of particle physics,” Phys. Rev.
D,
vol.
110,
no.
3,
p.
030001,
2024.
[Online].
Available:
https://pdg.lbl.gov/2024/reviews/contents sports.html
[247] M. Wenger, F. Ochsenbein, D. Egret, P. Dubois, F. Bonnarel, S. Borde,
F. Genova, G. Jasniewicz, S. Lalo¨e, S. Lesteven et al., “The simbad
astronomical database-the cds reference database for astronomical
objects,” Astronomy and Astrophysics Supplement Series, vol. 143,
no. 1, pp. 9–22, 2000.
[248] F. Ochsenbein, P. Bauer, and J. Marcout, “The vizier database of
astronomical catalogues,” Astronomy and Astrophysics Supplement
Series, vol. 143, no. 1, pp. 23–32, 2000.
[249] S. Wang, H. Sun, H. Liu, D. Li, Y. Li, and T. Hou, “Admet evaluation
in drug discovery. 16. predicting herg blockers by combining multiple
pharmacophores and machine learning approaches,” Molecular phar-
maceutics, vol. 13, no. 8, pp. 2855–2866, 2016.
[250] C.-Y. Ma, S.-Y. Yang, H. Zhang, M.-L. Xiang, Q. Huang, and Y.-Q.
Wei, “Prediction models of human plasma protein binding rate and
oral bioavailability derived by using ga–cg–svm method,” Journal of
pharmaceutical and biomedical analysis, vol. 47, no. 4-5, pp. 677–
682, 2008.
[251] T. Hou, J. Wang, W. Zhang, and X. Xu, “ADME evaluation in
drug discovery. 7. prediction of oral absorption by correlation and
classification,” Journal of chemical information and modeling, vol. 47,
no. 1, pp. 208–218, 2007.
[252] I. F. Martins, A. L. Teixeira, L. Pinheiro, and A. O. Falcao, “A
bayesian approach to in silico blood-brain barrier penetration model-
ing,” Journal of chemical information and modeling, vol. 52, no. 6,
pp. 1686–1697, 2012.
[253] D. L. Mobley and J. P. Guthrie, “Freesolv: a database of experimental
and calculated hydration free energies, with input files,” Journal of
computer-aided molecular design, vol. 28, no. 7, pp. 711–720, 2014.
[254] A. Gaulton, A. Hersey, M. Nowotka, A. P. Bento, J. Chambers,
D. Mendez, P. Mutowo, F. Atkinson, L. J. Bellis, E. Cibri´an-Uhalte
et al., “The chembl database in 2017,” Nucleic acids research, vol. 45,
no. D1, pp. D945–D954, 2017.
[255] F. Lombardo and Y. Jing, “In silico prediction of volume of distri-
bution in humans. extensive data set and the exploration of linear
and nonlinear methods coupled with molecular interaction fields
descriptors,” Journal of Chemical Information and Modeling, vol. 56,
no. 10, pp. 2042–2052, 2016.
[256] A. M. Richard, R. S. Judson, K. A. Houck, C. M. Grulke, P. Volarath,
I. Thillainadarajah, C. Yang, J. Rathman, M. T. Martin, J. F.
Wambaugh et al., “Toxcast chemical landscape: paving the road to
21st century toxicology,” Chemical research in toxicology, vol. 29,
no. 8, pp. 1225–1251, 2016.
[257] National Center for Advancing Translational Sciences (NCATS),
NIH, “Tox21 data challenge 2014: Training, testing, and final evalu-
ation datasets,” https://tripod.nih.gov/tox21/challenge/data.jsp, 2014,
datasets (training, testing, and final evaluation files) hosted by
NCATS/NIH; available as SMILES/SDF and assay-specific files. No
DOI reported for the challenge dataset; see Tox21 public-data portal
for downloads. Accessed 2025-08-27.
[258] INSPIRE Collaboration, “Inspire-hep rest api,” https://github.com/
inspirehep/rest-api-doc,
2020,
high-energy-physics
bibliographic
knowledge graph.
[259] P. Esling and C. Agon, “Time-series data mining,” ACM Computing
Surveys (CSUR), vol. 45, no. 1, pp. 1–34, 2012.
[260] G. E. Box, G. M. Jenkins, G. C. Reinsel, and G. M. Ljung, Time
series analysis: forecasting and control.
John Wiley & Sons, 2015.
[261] B. Lim and S. Zohren, “Time-series forecasting with deep learning: a
survey,” Philosophical Transactions of the Royal Society A, vol. 379,
no. 2194, p. 20200209, 2021.
[262] S. Chmiela, A. Tkatchenko, H. E. Sauceda, I. Poltavsky, K. T. Sch¨utt,
and K.-R. M¨uller, “Machine learning of accurate energy-conserving
molecular force fields,” Science Advances, vol. 3, no. 5, p. e1603015,
2017.
[263] K. Sch¨utt, P.-J. Kindermans, H. E. Sauceda Felix, S. Chmiela,
A. Tkatchenko et al., “Schnet: A continuous-filter convolutional
neural network for modeling quantum interactions,” in Advances in
Neural Information Processing Systems, 2017.
[264] K. T. Sch¨utt, H. E. Sauceda, P.-J. Kindermans, A. Tkatchenko, and
K.-R. M¨uller, “SchNet–a deep learning architecture for molecules and
materials,” The Journal of Chemical Physics, vol. 148, no. 24, p.
241722, 2018.
[265] W. J. Borucki, “Kepler mission: development and overview,” Reports
on Progress in Physics, vol. 79, no. 3, p. 036901, 2016.
[266] B. Peng, R. Nan, Y. Su, Y. Qiu, L. Zhu, and W. Zhu, “Five-
hundred-meter aperture spherical telescope project,” in International
Astronomical Union Colloquium, vol. 182.
Cambridge University
Press, 2001, pp. 219–224.
[267] C. Binnie and P. Prior, “Electroencephalography.” Journal of Neu-
rology, Neurosurgery & Psychiatry, vol. 57, no. 11, pp. 1308–1319,
1994.
[268] N. Yeung, R. Bogacz, C. B. Holroyd, and J. D. Cohen, “Detection of
synchronized oscillations in the electroencephalogram: an evaluation
of methods,” Psychophysiology, vol. 41, no. 6, pp. 822–832, 2004.
[269] G. A. Light, L. E. Williams, F. Minow, J. Sprock, A. Rissling,
R. Sharp, N. R. Swerdlow, and D. L. Braff, “Electroencephalography
(eeg) and event-related potentials (erps) with human participants,”
Current protocols in neuroscience, vol. 52, no. 1, pp. 6–25, 2010.
[270] T. Ahern, “Iris (incorporate research institutions for seismology),”
Lettre d’information R´esif, pp. 6–7, 2015.
[271] U.S. Geological Survey, “Usgs earthquake catalog api,” https://
earthquake.usgs.gov/fdsnws/event/1/, 2025, provides GeoJSON and
QuakeML formats for seismic event time series.
[272] Y. Zhou, J. Wu, Z. Ren, Z. Yao, W. Lu, K. Peng, Q. Zheng,
C. Song, W. Ouyang, and C. Gou, “Csbrain: A cross-scale spa-
tiotemporal brain foundation model for eeg decoding,” arXiv preprint
arXiv:2506.23075, 2025.
[273] Z. Bar-Joseph, A. Gitter, and I. Simon, “Studying and modelling
dynamic biological processes using time-series gene expression data,”
Nature Reviews Genetics, vol. 13, no. 8, pp. 552–564, 2012.
[274] A. K. Shalek, R. Satija, J. Shuga, J. J. Trombetta, D. Gennert, D. Lu,
P. Chen, R. S. Gertner, J. T. Gaublomme, N. Yosef et al., “Single-
cell rna-seq reveals dynamic paracrine control of cellular variation,”
Nature, vol. 510, no. 7505, pp. 363–369, 2014.
[275] Q. Deng, D. Ramsk¨old, B. Reinius, and R. Sandberg, “Single-cell
rna-seq reveals dynamic, random monoallelic gene expression in
mammalian cells,” Science, vol. 343, no. 6167, pp. 193–196, 2014.
[276] J. L. Willems, C. Abreu-Lima, P. Arnaud, J. H. van Bemmel,
C. Brohet, R. Degani, B. Denis, J. Gehring, I. Graham, G. van
Herpen et al., “The diagnostic performance of computer programs
for the interpretation of electrocardiograms,” New England Journal
of Medicine, vol. 325, no. 25, pp. 1767–1773, 1991.
[277] F. Agrafioti and D. Hatzinakos, “Ecg biometric analysis in cardiac
irregularity conditions,” Signal, Image and Video Processing, vol. 3,
no. 4, pp. 329–343, 2009.
[278] E. Kugelberg, “Electromyograms in muscular disorders,” Journal of
Neurology, Neurosurgery, and Psychiatry, vol. 10, no. 3, p. 122, 1947.
[279] A. Merlo, D. Farina, and R. Merletti, “A fast and reliable technique
for muscle activity detection from surface emg signals,” IEEE trans-
actions on biomedical engineering, vol. 50, no. 3, pp. 316–323, 2003.
[280] D. Rodbard, “Continuous glucose monitoring: a review of successes,
challenges, and opportunities,” Diabetes technology & therapeutics,
vol. 18, no. S2, pp. S2–3, 2016.
[281] D. C. Klonoff, D. Ahn, and A. Drincic, “Continuous glucose monitor-
ing: a review of the technology and clinical use,” Diabetes Research
and Clinical Practice, vol. 133, pp. 178–192, 2017.
[282] S.-G. Kim and S. Ogawa, “Biophysical and physiological origins of
blood oxygenation level-dependent fmri signals,” Journal of Cerebral
Blood Flow & Metabolism, vol. 32, no. 7, pp. 1188–1206, 2012.
[283] M. P. Van Den Heuvel and H. E. H. Pol, “Exploring the brain network:
a review on resting-state fmri functional connectivity,” European
neuropsychopharmacology, vol. 20, no. 8, pp. 519–534, 2010.
[284] A. L. Fred, S. N. Kumar, A. Kumar Haridhas, S. Ghosh, H. Pu-
rushothaman Bhuvana, W. K. J. Sim, V. Vimalan, F. A. S. Givo,
V. Jousm¨aki, P. Padmanabhan et al., “A brief introduction to mag-
netoencephalography (meg) and its clinical applications,” Brain sci-
ences, vol. 12, no. 6, p. 788, 2022.
[285] J. Vrba and S. E. Robinson, “Signal processing in magnetoen-
cephalography,” Methods, vol. 25, no. 2, pp. 249–271, 2001.
[286] H. H. Telle, A. G. Uren¸a, and R. J. Donovan, Laser chemistry:
spectroscopy, dynamics and applications.
John Wiley & Sons, 2007.
75

[287] W. D. Pesnell, B. J. Thompson, and P. C. Chamberlin, “The
solar dynamics observatory (sdo),” Solar Physics, vol. 275, no.
1-2, pp. 3–15, 2012. [Online]. Available: https://doi.org/10.1007/
s11207-011-9841-3
[288] M. G. Bobra and S. Couvidat, “Solar flare prediction using sdo/hmi
vector magnetic field data with a machine-learning algorithm,”
Astrophysical Journal, vol. 798, no. 2, p. 135, 2015. [Online].
Available: https://doi.org/10.1088/0004-637X/798/2/135
[289] N. Menachemi and T. H. Collum, “Benefits and drawbacks of elec-
tronic health record systems,” Risk management and healthcare policy,
pp. 47–55, 2011.
[290] S. J. Vos, C. Xiong, P. J. Visser, M. S. Jasielec, J. Hassenstab, E. A.
Grant, N. J. Cairns, J. C. Morris, D. M. Holtzman, and A. M. Fagan,
“Preclinical alzheimer’s disease and its outcome: a longitudinal cohort
study,” The Lancet Neurology, vol. 12, no. 10, pp. 957–965, 2013.
[291] S. Niu, Q. Yin, J. Ma, Y. Song, Y. Xu, L. Bai, W. Pan, and X. Yang,
“Enhancing healthcare decision support through explainable ai models
for risk prediction,” Decision Support Systems, vol. 181, p. 114228,
2024.
[292] E. C. Bellm, S. R. Kulkarni, M. J. Graham, R. Dekany, R. M. Smith,
R. Riddle, F. J. Masci, G. Helou, T. A. Prince, S. M. Adams et al.,
“The zwicky transient facility: system overview, performance, and
first results,” Publications of the Astronomical Society of the Pacific,
vol. 131, no. 995, p. 018002, 2018.
[293] D. L. Tucker, “The vera c. rubin observatory legacy survey of space &
time (lsst): An astronomical data set for the future,” Fermi National
Accelerator Laboratory (FNAL), Batavia, IL (United States), Tech.
Rep., 2023.
[294] E. P. Chassignet, H. E. Hurlburt, O. M. Smedstad, G. R. Halliwell,
P. J. Hogan, A. J. Wallcraft, R. Baraille, and R. Bleck, “The hycom
(hybrid coordinate ocean model) data assimilative system,” Journal
of Marine Systems, vol. 65, no. 1-4, pp. 60–83, 2007.
[295] D. C. Guest, “Solutions network formulation report. improving noaa’s
tides and currents through enhanced data inputs from nasa’s ocean
surface topography mission,” 2006.
[296] IRIS Data Management Center, “Time series data from seis-
mic stations worldwide,” https://ds.iris.edu/ds/nodes/dmc/data/types/
time-series-data/, 2025, continuous waveform records in MiniSEED
and related formats.
[297] M. A. Morid, O. R. L. Sheng, and J. Dunbar, “Time series prediction
using deep learning methods in healthcare,” ACM Transactions on
Management Information Systems, vol. 14, no. 1, pp. 1–29, 2023.
[298] F. Di Martino and F. Delmastro, “Explainable ai for clinical and
remote health applications: a survey on tabular and time series data,”
Artificial Intelligence Review, vol. 56, no. 6, pp. 5261–5315, 2023.
[299] C. Davey, D. Sargent, K. Luger, A. Maeder, and T. Richmond,
“Solvent mediated interactions in the structure of the nucleosome core
particle at 1.9 ˚A resolution,” J. Mol. Biol., vol. 319, no. 5, pp. 1097–
1113, 2002.
[300] E. Pettersen, T. Goddard, C. Huang, G. Couch, D. Greenblatt,
E. Meng, and T. Ferrin, “UCSF chimera–a visualization system for
exploratory research and analysis,” J. Comput. Chem., vol. 25, no. 13,
pp. 1605–1612, 2004.
[301] B. Adamczyk, M. Antczak, and M. Szachniuk, “Rnasolo: a repository
of cleaned pdb-derived rna 3d structures,” Bioinformatics, vol. 38,
no. 14, pp. 3668–3670, 2022.
[302] C. Bernard, G. Postic, S. Ghannay, and F. Tahi, “State-of-the-rnart:
benchmarking current methods for rna 3d structure prediction,” NAR
Genomics and Bioinformatics, vol. 6, no. 2, p. lqae048, 2024.
[303] Y.-C. Wang, W.-H. Yang, C.-S. Yang, M.-H. Hou, C.-L. Tsai, Y.-Z.
Chou, M.-C. Hung, and Y. Chen, “Structural basis of SARS-CoV-2
main protease inhibition by a broad-spectrum anti-coronaviral drug,”
Am. J. Cancer Res., vol. 10, no. 8, pp. 2535–2545, 2020.
[304] I. Subramanian, S. Verma, S. Kumar, A. Jere, and K. Anamika,
“Multi-omics data integration, interpretation, and its application,”
Bioinformatics and biology insights, vol. 14, p. 1177932219899051,
2020.
[305] J. Xie, Y. Chen, S. Luo, W. Yang, Y. Lin, L. Wang, X. Ding, M. Tong,
and R. Yu, “Tracing unknown tumor origins with a biological-
pathway-based transformer model,” Cell Reports Methods, vol. 4,
no. 6, 2024.
[306] N. Rappoport and R. Shamir, “Multi-omic and multi-view clustering
algorithms: review and cancer benchmark,” Nucleic acids research,
vol. 46, no. 20, pp. 10 546–10 562, 2018.
[307] Y.
Lin,
L.
Luo,
Y.
Chen,
X.
Zhang,
Z.
Wang,
W.
Yang,
M. Tong, and R. Yu, “St-align: A multimodal foundation model
for image-gene alignment in spatial transcriptomics,” arXiv preprint
arXiv:2411.16793, 2024.
[308] Y. Ren, W. Han, Q. Zhang, Y. Tang, W. Bai, Y. Cai, L. Qiao, H. Jiang,
D. Yuan, T. Chen et al., “Comet: Benchmark for comprehensive
biological multi-omics evaluation tasks and language models,” arXiv
preprint arXiv:2412.10347, 2024.
[309] K. J. Karczewski and M. P. Snyder, “Integrative omics for health and
disease,” Nature Reviews Genetics, vol. 19, no. 5, pp. 299–310, 2018.
[310] T. Hubbard, D. Barker, E. Birney, G. Cameron, Y. Chen, L. Clark,
T. Cox, J. Cuff, V. Curwen, T. Down et al., “The ensembl genome
database project,” Nucleic acids research, vol. 30, no. 1, pp. 38–41,
2002.
[311] W. J. Kent, C. W. Sugnet, T. S. Furey, K. M. Roskin, T. H. Pringle,
A. M. Zahler, and D. Haussler, “The human genome browser at ucsc,”
Genome research, vol. 12, no. 6, pp. 996–1006, 2002.
[312] D. Welter, J. A. L. MacArthur, J. Morales, T. Burdett, P. Hall,
H.
Junkins,
A.
Klemm,
P.
Flicek,
T.
Manolio,
L.
Hindorff,
and H. E. Parkinson, “The NHGRI GWAS catalog, a curated
resource of snp-trait associations,” Nucleic Acids Res., vol. 42,
no. Database-Issue, pp. 1001–1006, 2014. [Online]. Available:
https://doi.org/10.1093/nar/gkt1229
[313] K. J. Karczewski, L. C. Francioli, G. Tiao, B. B. Cummings,
J. Alf¨oldi, Q. Wang, R. L. Collins, K. M. Laricchia, A. Ganna, D. P.
Birnbaum et al., “The mutational constraint spectrum quantified from
variation in 141,456 humans,” Nature, vol. 581, no. 7809, pp. 434–
443, 2020.
[314] M. J. Landrum, J. M. Lee, M. Benson, G. Brown, C. Chao, S. Chi-
tipiralla, B. Gu, J. Hart, D. Hoffman, J. Hoover et al., “Clinvar: public
archive of interpretations of clinically relevant variants,” Nucleic acids
research, vol. 44, no. D1, pp. D862–D868, 2016.
[315] A. Kundaje, W. Meuleman, J. Ernst, M. Bilenky, A. Yen, P. Kher-
adpour, Z. Zhang, A. Heravi-Moussavi, Y. Liu, V. Amin et al.,
“Integrative analysis of 111 reference human epigenomes,” Nature,
vol. 518, no. 7539, p. 317, 2015.
[316] E. Lieberman-Aiden, N. L. Van Berkum, L. Williams, M. Imakaev,
T. Ragoczy et al., “Comprehensive mapping of long-range interactions
reveals folding principles of the human genome,” Science, vol. 326,
no. 5950, pp. 289–293, 2009.
[317] S. S. Rao, M. H. Huntley, N. C. Durand, E. K. Stamenova, I. D.
Bochkov et al., “A 3d map of the human genome at kilobase resolution
reveals principles of chromatin looping,” Cell, vol. 159, no. 7, pp.
1665–1680, 2014.
[318] Z. Zhou, Y. Ji, W. Li, P. Dutta, R. Davuluri, and H. Liu, “Dnabert-2:
Efficient foundation model and benchmark for multi-species genome,”
arXiv preprint arXiv:2306.15006, 2023.
[319] H. Dalla-Torre, L. Gonzalez, J. Mendoza-Revilla, N. Lopez Carranza,
A. H. Grzywaczewski, F. Oteri, C. Dallago, E. Trop, B. P. de Almeida,
H. Sirelkhatim et al., “Nucleotide transformer: building and evaluating
robust foundation models for human genomics,” Nature Methods,
vol. 22, no. 2, pp. 287–297, 2025.
[320] A. Frankish, M. Diekhans, A.-M. Ferreira, R. Johnson, I. Jungreis,
J. Loveland, J. M. Mudge, C. Sisu, J. Wright, J. Armstrong et al.,
“Gencode reference annotation for the human and mouse genomes,”
Nucleic acids research, vol. 47, no. D1, pp. D766–D773, 2019.
[321] N. A. O’Leary, M. W. Wright, J. R. Brister, S. Ciufo, D. Haddad,
R. McVeigh, B. Rajput, B. Robbertse, B. Smith-White, D. Ako-
Adjei et al., “Reference sequence (refseq) database at ncbi: current
status, taxonomic expansion, and functional annotation,” Nucleic acids
research, vol. 44, no. D1, pp. D733–D745, 2016.
[322] N. Kolesnikov, E. Hastings, M. Keays, O. Melnichuk, Y. A. Tang,
E. Williams, M. Dylag, N. Kurbatova, M. Brandizi, T. Burdett et al.,
“Arrayexpress update—simplifying data submissions,” Nucleic acids
research, vol. 43, no. D1, pp. D1113–D1116, 2015.
[323] G. Consortium, “The gtex consortium atlas of genetic regulatory
effects across human tissues,” Science, vol. 369, no. 6509, pp. 1318–
1330, 2020.
[324] 10x Genomics, “Visium spatial platform,” https://www.10xgenomics.
com/platforms/visium, 2025, product page for the Visium Spatial
Platform (Visium HD / Visium CytAssist, assays, and analysis tools).
Accessed 2025-08-28.
[325] S. G. Rodriques, R. R. Stickels, A. Goeva, C. A. Martin, E. Murray,
C. R. Vanderburg, J. Welch, L. M. Chen, F. Chen, and E. Z.
Macosko, “Slide-seq: A scalable technology for measuring genome-
wide expression at high spatial resolution,” Science, vol. 363, no.
6434, pp. 1463–1467, 2019.
[326] A. Chen, S. Liao, M. Cheng, K. Ma, L. Wu, Y. Lai, X. Qiu, J. Yang,
J. Xu, S. Hao et al., “Spatiotemporal transcriptomic atlas of mouse
76

organogenesis using dna nanoball-patterned arrays,” Cell, vol. 185,
no. 10, pp. 1777–1792, 2022.
[327] Z. Fan, R. Chen, and X. Chen, “Spatialdb: a database for spatially
resolved transcriptomes,” Nucleic acids research, vol. 48, no. D1, pp.
D233–D237, 2020.
[328] D. Szklarczyk, A. L. Gable, D. Lyon, A. Junge, S. Wyder, J. Huerta-
Cepas, M. Simonovic, N. T. Doncheva, J. H. Morris, P. Bork et al.,
“String v11: protein–protein association networks with increased cov-
erage, supporting functional discovery in genome-wide experimental
datasets,” Nucleic acids research, vol. 47, no. D1, pp. D607–D613,
2019.
[329] H. M. Berman, J. Westbrook, Z. Feng, G. Gilliland, T. N. Bhat,
H. Weissig, I. N. Shindyalov, and P. E. Bourne, “The protein data
bank,” Nucleic acids research, vol. 28, no. 1, pp. 235–242, 2000.
[330] D. Szklarczyk, R. Kirsch, M. Koutrouli, K. Nastou, F. Mehryary,
R. Hachilif, A. L. Gable, T. Fang, N. T. Doncheva, S. Pyysalo,
P. Bork, L. J. Jensen, and C. von Mering, “The string database in 2023:
protein–protein association networks and functional enrichment anal-
yses for any sequenced genome of interest,” Nucleic Acids Research,
vol. 51, no. D1, pp. D638–D646, 2023.
[331] R. Oughtred, C. Stark, B.-J. Breitkreutz, J. Rust, L. Boucher,
C. Chang, N. Kolas, L. O’Donnell, G. Leung, and et al., “The
BioGRID interaction database: 2019 update,” Nucleic Acids Research,
vol. 47, no. D1, pp. D529–D541, 2019.
[332] H. Hermjakob, L. Montecchi-Palazzi, C. Lewington, S. Mudali,
S. Kerrien, S. Orchard, M. Vingron, B. Roechert, P. Roepstorff,
A. Valencia, H. Margalit, J. Armstrong, A. Bairoch, G. Cesareni,
D. Sherman, and R. Apweiler, “Intact: an open source molecular
interaction database,” Nucleic Acids Research, vol. 32, no. Database
issue, pp. D452–D455, 2004.
[333] The Gene Ontology Consortium, “The gene ontology resource: enrich-
ing a GOld mine of functional information,” Nucleic Acids Research,
vol. 49, no. D1, pp. D325–D334, 2021.
[334] M. Uhl´en, L. Fagerberg, B. M. Hallstr¨om, C. Lindskog, P. Oksvold,
A. Mardinoglu, ˚A. Sivertsson, C. Kampf, E. Sj¨ostedt, A. Asplund,
and et al., “Tissue-based map of the human proteome,” Science, vol.
347, no. 6220, p. 1260419, 2015.
[335] M. Varadi, D. Bertoni, P. Ma˜nana, U. Paramval, I. Pidruchna,
M. Radhakrishnan, M. Tsenkov, S. Nair, M. Mirdita, M. Steinegger,
D. Hassabis, S. Velankar, and et al., “Alphafold protein structure
database in 2024: providing structure coverage for over 214 million
protein sequences,” Nucleic Acids Research, vol. 52, no. D1, pp.
D368–D375, 2024.
[336] E. W. Deutsch, N. Bandeira, V. Sharma, Y. Perez-Riverol, J. J.
Carver, D. J. Kundu, and et al., “The proteomexchange consortium in
2020: enabling ’big data’ approaches in proteomics,” Nucleic Acids
Research, vol. 48, no. D1, pp. D1145–D1152, 2020.
[337] Y. Perez-Riverol, J. Bai, C. Bandla, J. A. Vizca´ıno, and et al., “The
PRIDE database resources in 2022: a hub for mass spectrometry-based
proteomics evidences,” Nucleic Acids Research, vol. 51, no. D1, pp.
D1539–D1548, 2023.
[338] M. D. Wilkinson, M. Dumontier, I. J. Aalbersberg, G. Appleton,
M. Axton, A. Baak, N. Blomberg, J.-W. Boiten, L. B. da Silva Santos,
P. E. Bourne et al., “The fair guiding principles for scientific data
management and stewardship,” Scientific data, vol. 3, no. 1, pp. 1–9,
2016.
[339] C. F. Taylor, N. W. Paton, K. S. Lilley, P.-A. Binz, R. K. Julian Jr,
A. R. Jones, W. Zhu, R. Apweiler, R. Aebersold, E. W. Deutsch
et al., “The minimum information about a proteomics experiment
(MIAPE),” Nature biotechnology, vol. 25, no. 8, pp. 887–893, 2007.
[340] D. S. Wishart, Y. D. Feunang, A. Marcu, A. C. Guo, K. Liang,
R. V´azquez-Fresno, T. Sajed, D. Johnson, C. Li, N. Karu et al.,
“Hmdb 4.0: the human metabolome database for 2018,” Nucleic acids
research, vol. 46, no. D1, pp. D608–D617, 2018.
[341] K. Haug, R. M. Salek, P. Conesa, J. Hastings, P. De Matos, M. Ri-
jnbeek, T. Mahendraker, M. Williams, S. Neumann, P. Rocca-Serra
et al., “Metabolights—an open-access general-purpose repository for
metabolomics studies and associated meta-data,” Nucleic acids re-
search, vol. 41, no. D1, pp. D781–D786, 2013.
[342] The Human Microbiome Project Consortium, “Structure, function and
diversity of the healthy human microbiome,” Nature, vol. 486, no.
7402, pp. 207–214, 2012.
[343] A. L. Mitchell, A. Almeida, M. Beracochea, M. Boland, J. Burgin,
G. Cochrane, M. R. Crusoe, V. Kale, S. C. Potter, L. J. Richardson
et al., “MGnify: the microbiome analysis resource in 2020,” Nucleic
acids research, vol. 48, no. D1, pp. D570–D578, 2020.
[344] V. Neveu, A. Moussy, H. Rouaix, R. Wedekind, A. Pon, C. Knox,
D. S. Wishart, and A. Scalbert, “Exposome-explorer: a manually-
curated database on biomarkers of exposure to dietary and environ-
mental factors,” Nucleic acids research, p. gkw980, 2016.
[345] B. B. Misra, C. Langefeld, M. Olivier, and L. A. Cox, “Integrated
omics: tools, advances and future approaches,” Journal of molecular
endocrinology, vol. 62, no. 1, pp. R21–R45, 2019.
[346] J. Xie, Y. Song, H. Zheng, S. Luo, Y. Chen, C. Zhang, R. Yu,
and M. Tong, “Pathmethy: an interpretable ai framework for cancer
origin tracing based on dna methylation,” Briefings in Bioinformatics,
vol. 25, no. 6, p. bbae497, 2024.
[347] Y. He, P. Fang, Y. Shan, Y. Pan, Y. Wei, Y. Chen, Y. Chen, Y. Liu,
Z. Zeng, Z. Zhou et al., “Generalized biological foundation model
with unified nucleic acid and protein language,” Nature Machine
Intelligence, pp. 1–12, 2025.
[348] R. L. Ackoff, “From data to wisdom,” Journal of applied systems
analysis, vol. 16, no. 1, pp. 3–9, 1989.
[349] J. Rowley, “The wisdom hierarchy: representations of the dikw
hierarchy,” Journal of information science, vol. 33, no. 2, pp. 163–
180, 2007.
[350] M. Zeleny, “Management support systems: Towards integrated knowl-
edge management,” Human systems management, vol. 7, no. 1, pp.
59–70, 1987.
[351] S. Baskarada and A. Koronios, “Data, information, knowledge, wis-
dom (dikw): A semiotic theoretical and empirical exploration of
the hierarchy and its quality dimension,” Australasian Journal of
Information Systems, vol. 18, no. 1, 2013.
[352] B. D. Savage and K. R. Sembach, “Interstellar abundances from
absorption-line observations with the hubble space telescope,” Annual
Review of Astronomy and Astrophysics, vol. 34, no. 1, pp. 279–329,
1996.
[353] B. P. Abbott, R. Abbott, T. Abbott, S. Abraham, F. Acernese, K. Ack-
ley, C. Adams, R. Adhikari, V. Adya, C. Affeldt et al., “GWTC-
1: a gravitational-wave transient catalog of compact binary mergers
observed by ligo and virgo during the first and second observing runs,”
Physical Review X, vol. 9, no. 3, p. 031040, 2019.
[354] S. Nurk, S. Koren, A. Rhie, M. Rautiainen, A. V. Bzikadze,
A. Mikheenko, M. R. Vollger, N. Altemose, L. Uralsky, A. Gershman
et al., “The complete sequence of a human genome,” Science, vol.
376, no. 6588, pp. 44–53, 2022.
[355] G. Buzs´aki and B. O. Watson, “Brain rhythms and neural syntax:
implications for efficient coding of cognitive content and neuropsy-
chiatric disease.” Dialogues in clinical neuroscience, vol. 14, no. 4,
pp. 345–367, 2012.
[356] A. Regev, S. A. Teichmann, E. S. Lander, I. Amit, C. Benoist,
E. Birney, B. Bodenmiller, P. Campbell, P. Carninci, M. Clatworthy
et al., “The human cell atlas,” elife, vol. 6, p. e27041, 2017.
[357] G. Yang, J. Liu, C. Zhao, Z. Li, Y. Huang, H. Yu, B. Xu, X. Yang,
D. Zhu, X. Zhang et al., “Unmanned aerial vehicle remote sensing
for field-based crop phenotyping: current status and perspectives,”
Frontiers in plant science, vol. 8, p. 1111, 2017.
[358] A. Savtchenko, D. Ouzounov, S. Ahmad, J. Acker, G. Leptoukh,
J. Koziana, and D. Nickless, “Terra and aqua modis products available
from nasa ges daac,” Advances in Space Research, vol. 34, no. 4, pp.
710–714, 2004.
[359] M. Rizhko and J. S. Bloom, “Self-supervised multimodal model
for astronomy,” in Neurips 2024 Workshop Foundation Models for
Science: Progress, Opportunities, and Challenges, 2024.
[360] I. Fountoulakis and C. P. Evangelidis, “The 2024–2025 seismic se-
quence in the santorini-amorgos region: Insights into volcano-tectonic
activity through high-resolution seismic monitoring,” Seismica, vol. 4,
no. 1, 2025.
[361] C. P. Evangelidis, N. Triantafyllis, M. Samios, K. Boukouras, K. Kon-
takos, O.-J. Ktenidou, I. Fountoulakis, I. Kalogeras, N. S. Melis,
O. Galanis et al., “Seismic waveform data from greece and cyprus:
Integration, archival, and open access,” Seismological Society of
America, vol. 92, no. 3, pp. 1672–1684, 2021.
[362] A. Reichel and P. Lienau, “Pharmacokinetics in drug discovery: an
exposure-centred approach to optimising and predicting drug efficacy
and safety,” New approaches to drug discovery, pp. 235–260, 2015.
[363] D. B. Lobell, G. Azzari, M. Burke, S. Gourlay, Z. Jin, T. Kilic,
and S. Murray, “Eyes in the sky, boots on the ground: Assessing
satellite-and ground-based approaches to crop yield measurement and
analysis,” American Journal of Agricultural Economics, vol. 102,
no. 1, pp. 202–219, 2020.
[364] W. Xu, F. Ling, T. Han, H. Chen, W. Ouyang, and L. BAI, “General-
izing weather forecast to fine-grained temporal scales via physics-
77

ai hybrid modeling,” Advances in Neural Information Processing
Systems, vol. 37, pp. 23 325–23 351, 2024.
[365] J. Gong, L. Bai, P. Ye, W. Xu, N. Liu, J. Dai, X. Yang, and W. Ouyang,
“Cascast: Skillful high-resolution precipitation nowcasting via cas-
caded modelling,” arXiv preprint arXiv:2402.04290, 2024.
[366] J. Gong, S. Tu, W. Yang, B. Fei, K. Chen, W. Zhang, X. Yang,
W. Ouyang, and L. Bai, “Postcast: Generalizable postprocessing for
precipitation nowcasting via unsupervised blurriness modeling,” arXiv
preprint arXiv:2410.05805, 2024.
[367] K. Chen, T. Han, J. Gong, L. Bai, F. Ling, J.-J. Luo, X. Chen,
L. Ma, T. Zhang, R. Su et al., “Fengwu: Pushing the skillful global
medium-range weather forecast beyond 10 days lead,” arXiv preprint
arXiv:2304.02948, 2023.
[368] W. Xu, K. Chen, T. Han, H. Chen, W. Ouyang, and L. Bai, “Extreme-
cast: Boosting extreme value prediction for global weather forecast,”
arXiv preprint arXiv:2402.01295, 2024.
[369] J. W. Hardy, Adaptive optics for astronomical telescopes.
Oxford
university press, 1998, vol. 16.
[370] U.S. Food and Drug Administration and JHU-CERSI, “Assessing
and communicating heterogeneity of treatment effects for patient
subpopulations: Challenges and opportunities,” Workshop summary,
U.S. FDA and Johns Hopkins University CERSI, Nov. 28 2018, sym-
posium hosted November 28, 2018; FDA emphasised the importance
of accounting for patient heterogeneity in clinical trial design and
communication.
[371] I. Newton, Philosophiae naturalis principia mathematica.
Jussu
Societatis Regiae ac Typis Josephi Streater. Prostat apud plures
bibliopolas, 1687.
[372] J. C. Maxwell, “VIII. a dynamical theory of the electromagnetic field,”
Philos. Trans. R. Soc. Lond., vol. 155, no. 0, pp. 459–512, Dec. 1865.
[373] E. Schr¨odinger, “An undulatory theory of the mechanics of atoms
and molecules,” Phys. Rev., vol. 28, pp. 1049–1070, Dec 1926.
[Online]. Available: https://link.aps.org/doi/10.1103/PhysRev.28.1049
[374] A. L. Hodgkin and A. F. Huxley, “A quantitative description of
membrane current and its application to conduction and excitation
in nerve,” The Journal of physiology, vol. 117, no. 4, p. 500, 1952.
[375] F. Crick, “Central dogma of molecular biology,” Nature, vol. 227, no.
5258, pp. 561–563, 1970.
[376] F. J. Vine and D. H. Matthews, Magnetic anomalies over oceanic
ridges.
Nature Publishing, 1963.
[377] S. Weinberg, “A model of leptons,” Physical review letters, vol. 19,
no. 21, p. 1264, 1967.
[378] C. Linnaeus, Systema Naturae per regna tria naturae, secundum
classes, ordines, genera, species; cum characteribus, differentiis,
synonymis, locis.
apud JB Delamolliere, 1789, vol. 1.
[379] D. Mendeleev, “On the relationship of the properties of the elements
to their atomic weights,” Zeitschrift f¨ur Chemie, vol. 12, pp. 405–406,
1869.
[380] A.-L. Barabasi and Z. N. Oltvai, “Network biology: understanding the
cell’s functional organization,” Nature reviews genetics, vol. 5, no. 2,
pp. 101–113, 2004.
[381] H. Jeong, B. Tombor, R. Albert, Z. N. Oltvai, and A.-L. Barab´asi,
“The large-scale organization of metabolic networks,” Nature, vol.
407, no. 6804, pp. 651–654, 2000.
[382] J. A. Dunne, R. J. Williams, and N. D. Martinez, “Network struc-
ture and biodiversity loss in food webs: robustness increases with
connectance,” Ecology letters, vol. 5, no. 4, pp. 558–567, 2002.
[383] O. Sporns, G. Tononi, and R. K¨otter, “The human connectome:
a structural description of the human brain,” PLoS computational
biology, vol. 1, no. 4, p. e42, 2005.
[384] W.
M.
Washington
and
C.
Parkinson,
Introduction
to
three-
dimensional climate modeling.
University science books, 2005.
[385] M. Karplus and J. A. McCammon, “Molecular dynamics simulations
of biomolecules,” Nature structural biology, vol. 9, no. 9, pp. 646–
652, 2002.
[386] L. Excoffier, G. Laval, and S. Schneider, “Arlequin (version 3.0): an
integrated software package for population genetics data analysis,”
Evolutionary bioinformatics, vol. 1, p. 117693430500100003, 2005.
[387] M. Rowland and T. N. Tozer, “Clinical pharmacokinetics and phar-
macodynamics: concepts and applications,” (No Title), 2011.
[388] J. P. Huelsenbeck, F. Ronquist, R. Nielsen, and J. P. Bollback,
“Bayesian inference of phylogeny and its impact on evolutionary
biology,” science, vol. 294, no. 5550, pp. 2310–2314, 2001.
[389] N. Aghanim et al., “Planck 2018 results. vi. cosmological parameters,”
Astron. Astrophys, vol. 641, p. A6, 2020.
[390] J. A. Doudna and E. Charpentier, “The new frontier of genome
engineering with crispr-cas9,” Science, vol. 346, no. 6213, p. 1258096,
2014.
[391] M. H. Anderson, J. R. Ensher, M. R. Matthews, C. E. Wieman,
and E. A. Cornell, “Observation of bose-einstein condensation in a
dilute atomic vapor,” Science, vol. 269, no. 5221, pp. 198–201, 1995.
[Online]. Available: https://www.science.org/doi/abs/10.1126/science.
269.5221.198
[392] N. Metropolis, A. W. Rosenbluth, M. N. Rosenbluth, A. H. Teller, and
E. Teller, “Equation of state calculations by fast computing machines,”
The journal of chemical physics, vol. 21, no. 6, pp. 1087–1092, 1953.
[393] J. Jumper, R. Evans, A. Pritzel, T. Green, M. Figurnov, O. Ron-
neberger, K. Tunyasuvunakool, R. Bates, A. ˇZ´ıdek, A. Potapenko
et al., “Highly accurate protein structure prediction with alphafold,”
nature, vol. 596, no. 7873, pp. 583–589, 2021.
[394] M. Helmstaedter, K. L. Briggman, S. C. Turaga, V. Jain, H. S. Seung,
and W. Denk, “Connectomic reconstruction of the inner plexiform
layer in the mouse retina,” Nature, vol. 500, no. 7461, pp. 168–174,
2013.
[395] G. Aad, T. Abajyan, B. Abbott, J. Abdallah, S. A. Khalek, A. A.
Abdelalim, R. Aben, B. Abi, M. Abolins, O. AbouZeid et al.,
“Observation of a new particle in the search for the standard model
higgs boson with the atlas detector at the lhc,” Physics Letters B, vol.
716, no. 1, pp. 1–29, 2012.
[396] E. Ruska, “The development of the electron microscope and of
electron microscopy,” Reviews of modern physics, vol. 59, no. 3, p.
627, 1987.
[397] T. Stuart and R. Satija, “Integrative single-cell analysis,” Nature
reviews genetics, vol. 20, no. 5, pp. 257–272, 2019.
[398] K. E. Taylor, R. J. Stouffer, and G. A. Meehl, “An overview of cmip5
and the experiment design,” Bulletin of the American meteorological
Society, vol. 93, no. 4, pp. 485–498, 2012.
[399] M. Vogelsberger, F. Marinacci, P. Torrey, and E. Puchwein, “Cos-
mological simulations of galaxy formation,” Nature Reviews Physics,
vol. 2, no. 1, pp. 42–66, 2020.
[400] M. Raissi, P. Perdikaris, and G. E. Karniadakis, “Physics-informed
neural networks: A deep learning framework for solving forward and
inverse problems involving nonlinear partial differential equations,”
Journal of Computational physics, vol. 378, pp. 686–707, 2019.
[401] S. Cai, Z. Mao, Z. Wang, M. Yin, and G. E. Karniadakis, “Physics-
informed neural networks (pinns) for fluid mechanics: A review,” Acta
Mechanica Sinica, vol. 37, no. 12, pp. 1727–1738, 2021.
[402] H. Kitano, “Systems biology: a brief overview,” science, vol. 295, no.
5560, pp. 1662–1664, 2002.
[403] G. Sliwoski, S. Kothiwale, J. Meiler, and E. W. Lowe Jr, “Computa-
tional methods in drug discovery,” Pharmacological reviews, vol. 66,
no. 1, pp. 334–395, 2014.
[404] H. Markram, E. Muller, S. Ramaswamy, M. W. Reimann, M. Abdel-
lah, C. A. Sanchez, A. Ailamaki, L. Alonso-Nanclares, N. Antille,
S. Arsever et al., “Reconstruction and simulation of neocortical
microcircuitry,” Cell, vol. 163, no. 2, pp. 456–492, 2015.
[405] S. Asseng, F. Ewert, C. Rosenzweig, J. W. Jones, J. L. Hatfield, A. C.
Ruane, K. J. Boote, P. J. Thorburn, R. P. R¨otter, D. Cammarano et al.,
“Uncertainty in simulating wheat yields under climate change,” Nature
climate change, vol. 3, no. 9, pp. 827–832, 2013.
[406] W. L. Oberkampf and C. J. Roy, Verification and validation in
scientific computing.
Cambridge university press, 2010.
[407] C. E. Shannon, “A mathematical theory of communication,” The Bell
system technical journal, vol. 27, no. 3, pp. 379–423, 1948.
[408] J. D. Watson and F. H. Crick, “Molecular structure of nucleic acids:
a structure for deoxyribose nucleic acid,” Nature, vol. 171, no. 4356,
pp. 737–738, 1953.
[409] S. Ogawa, T.-M. Lee, A. R. Kay, and D. W. Tank, “Brain magnetic
resonance imaging with contrast dependent on blood oxygenation.”
proceedings of the National Academy of Sciences, vol. 87, no. 24, pp.
9868–9872, 1990.
[410] E. M. Burbidge, G. R. Burbidge, W. A. Fowler, and F. Hoyle,
“Synthesis of the elements in stars,” Reviews of modern physics,
vol. 29, no. 4, p. 547, 1957.
[411] K. A. Dill and H. S. Chan, “From levinthal to pathways to funnels,”
Nature structural biology, vol. 4, no. 1, pp. 10–19, 1997.
[412] R. K. Varshney, W. Chen, Y. Li, A. K. Bharti, R. K. Saxena, J. A.
Schlueter, M. T. Donoghue, S. Azam, G. Fan, A. M. Whaley et al.,
“Draft genome sequence of pigeonpea (cajanus cajan), an orphan
legume crop of resource-poor farmers,” Nature biotechnology, vol. 30,
no. 1, p. 83, 2012.
78

[413] M. Planck, “Ueber das gesetz der energieverteilung im normalspec-
trum,” Ann. Phys., vol. 309, no. 3, pp. 553–563, Jan. 1901.
[414] D. Baltimore, “Viral rna-dependent dna polymerase: Rna-dependent
dna polymerase in virions of rna tumour viruses,” Nature, vol. 226,
no. 5252, pp. 1209–1211, 1970.
[415] V. C. Rubin, W. K. Ford Jr, and N. Thonnard, “Rotational properties
of 21 sc galaxies with a large range of luminosities and radii, from
ngc 4605/r= 4kpc/to ugc 2885/r= 122 kpc,” Astrophysical Journal,
Part 1, vol. 238, June 1, 1980, p. 471-487., vol. 238, pp. 471–487,
1980.
[416] M. Boolell, S. Gepi-Attee, J. Gingell, and M. Allen, “Sildenafil, a
novel effective oral therapy for male erectile dysfunction,” British
journal of urology, vol. 78, no. 2, pp. 257–261, 1996.
[417] C. Darwin, J. W. Burrow, and J. W. Burrow, The origin of species by
means of natural selection: or, the preservation of favored races in
the struggle for life.
AL Burt New York, 2009.
[418] A. Wegener and A. Vogel, Die entstehung der kontinente und ozeane.
Walter de Gruyter GmbH & Co KG, 1980.
[419] B. P. Abbott, R. Abbott, T. D. Abbott, M. R. Abernathy, F. Acernese,
K. Ackley, C. Adams, T. Adams, P. Addesso, R. X. Adhikari et al.,
“Observation of gravitational waves from a binary black hole merger,”
Physical review letters, vol. 116, no. 6, p. 061102, 2016.
[420] J. Wei, X. Wang, D. Schuurmans, M. Bosma, F. Xia, E. Chi, Q. V.
Le, D. Zhou et al., “Chain-of-thought prompting elicits reasoning in
large language models,” Advances in Neural Information Processing
systems, vol. 35, pp. 24 824–24 837, 2022.
[421] Y. Xia, R. Wang, X. Liu, M. Li, T. Yu, X. Chen, J. McAuley, and
S. Li, “Beyond chain-of-thought: A survey of chain-of-x paradigms
for llms,” arXiv preprint arXiv:2404.15676, 2024.
[422] A. Fallahpour, A. Magnuson, P. Gupta, S. Ma, J. Naimer, A. Shah,
H. Duan, O. Ibrahim, H. Goodarzi, C. J. Maddison et al., “Biorea-
son: Incentivizing multimodal biological reasoning within a dna-llm
model,” arXiv preprint arXiv:2505.23579, 2025.
[423] NIH, “Advancing health research through multimodal ai,” https://en.
wikibooks.org/wiki/LaTeX/Bibliography Management, 2025.
[424] J. Storey, M. Choate, and K. Lee, “Landsat 8 operational land imager
on-orbit geometric calibration and performance,” Remote sensing,
vol. 6, no. 11, pp. 11 127–11 152, 2014.
[425] Z. Cheng, J. Caverlee, and K. Lee, “You are where you tweet: a
content-based approach to geo-locating twitter users,” in Proceedings
of the 19th ACM international conference on Information and knowl-
edge management, 2010, pp. 759–768.
[426] C. Batini and M. Scannapieca, Data quality: concepts, methodologies
and techniques.
Springer, 2006.
[427] L. L. Pipino, Y. W. Lee, and R. Y. Wang, “Data quality assessment,”
Communications of the ACM, vol. 45, no. 4, pp. 211–218, 2002.
[428] H. Li, B. Handsaker, A. Wysoker, T. Fennell, J. Ruan, N. Homer,
G. Marth, G. Abecasis, R. Durbin, and . G. P. D. P. Subgroup,
“The sequence alignment/map format and samtools,” bioinformatics,
vol. 25, no. 16, pp. 2078–2079, 2009.
[429] D. Sims, I. Sudbery, N. E. Ilott, A. Heger, and C. P. Ponting,
“Sequencing depth and coverage: key considerations in genomic
analyses,” Nature Reviews Genetics, vol. 15, no. 2, pp. 121–132, 2014.
[430] F. Ren, L. Ward, T. Williams, K. J. Laws, C. Wolverton, J. Hattrick-
Simpers, and A. Mehta, “Accelerated discovery of metallic glasses
through iteration of machine learning and high-throughput experi-
ments,” Science advances, vol. 4, no. 4, p. eaaq1566, 2018.
[431] G. Tang, M. P. Clark, A. J. Newman, A. W. Wood, S. M. Papalexiou,
V. Vionnet, and P. H. Whitfield, “SCDNA: a serially complete
precipitation and temperature dataset for north america from 1979
to 2018,” Earth System Science Data, vol. 12, pp. 2381–2409, 2020.
[432] A. Delpeuch, T. Morris, D. Huynh, W. (bot), S. Mazzocchi, Jacky,
T. Guidry, elebitzero, O. Stephens, I. Matsunami, A. Larsson,
I. Sproat, S. Santos, A. Mayer, kushthedude, L. M. [Sannita], S. Fau-
connier, E. Mishra, M. Magdinier, A. Beaubien, L. Liu, F. Giroud,
J. Ong, F. Tacchelli, A. Nordhøy, E. Kanye, Y. Shahrabani, and
M. Saby, “Openrefine/openrefine: Openrefine 3.9.3,” https://doi.org/
10.5281/zenodo.15236589, Apr. 2025, version 3.9.3.
[433] DataCleaner contributors, “Datacleaner: The premier open source data
quality solution,” https://github.com/datacleaner/DataCleaner, 2024,
version 5.9.0 (released 2024-11-16); LGPL-3.0; Accessed 2025-08-
12.
[434] E. Dong, H. Du, and L. Gardner, “An interactive web-based dashboard
to track covid-19 in real time,” The Lancet infectious diseases, vol. 20,
no. 5, pp. 533–534, 2020.
[435] S. Lewis, “Remote sensing for natural disasters: Facts and figures,”
SciDev. net-Environment, 2009.
[436] J. Deng, W. Dong, R. Socher, L.-J. Li, K. Li, and L. Fei-Fei,
“Imagenet: A large-scale hierarchical image database,” in 2009 IEEE
conference on computer vision and pattern recognition.
Ieee, 2009,
pp. 248–255.
[437] D. Vrandeˇci´c and M. Kr¨otzsch, “Wikidata: a free collaborative knowl-
edgebase,” Communications of the ACM, vol. 57, no. 10, pp. 78–85,
2014.
[438] T. C. Redman, “The impact of poor data quality on the typical
enterprise,” Communications of the ACM, vol. 41, no. 2, pp. 79–82,
1998.
[439] OpenAIRE, “Openaire,” https://www.openaire.eu/, 2025, accessed
2025-08-12.
[440] V. Krotov, L. Johnson, and L. Silva, “Tutorial: Legality and ethics of
web scraping,” Communications of the Association for Information
Systems, vol. 47, 2020.
[441] X. Liang, S. Shetty, D. Tosh, C. Kamhoua, K. Kwiat, and L. Njilla,
“Provchain: A blockchain-based data provenance architecture in cloud
environment with enhanced privacy and availability,” in 2017 17th
IEEE/ACM International Symposium on Cluster, Cloud and Grid
Computing (CCGRID).
IEEE, 2017, pp. 468–477.
[442] X. Wang, Z. Hu, P. Lu, Y. Zhu, J. Zhang, S. Subramaniam, A. R.
Loomba, S. Zhang, Y. Sun, and W. Wang, “Scibench: Evaluating
college-level scientific problem-solving abilities of large language
models,” arXiv preprint arXiv:2307.10635, 2023.
[443] K. Feng, K. Ding, W. Wang, X. Zhuang, Z. Wang, M. Qin, Y. Zhao,
J. Yao, Q. Zhang, and H. Chen, “Sciknoweval: Evaluating multi-
level scientific knowledge of large language models,” arXiv preprint
arXiv:2406.09098, 2024.
[444] Y. Zhou, Y. Wang, X. He, R. Xiao, Z. Li, Q. Feng, Z. Guo, Y. Yang,
H. Wu, W. Huang et al., “Scientists’ first exam: Probing cognitive
abilities of mllm via perception, understanding, and reasoning,” arXiv
preprint arXiv:2506.10521, 2025.
[445] T. Brown, B. Mann, N. Ryder, M. Subbiah, J. D. Kaplan et al.,
“Language models are few-shot learners,” in Advances in Neural
Information Processing Systems, 2020.
[446] A. Grattafiori, A. Dubey, A. Jauhri, A. Pandey, A. Kadian, A. Al-
Dahle, A. Letman, A. Mathur, A. Schelten, A. Vaughan et al., “The
llama 3 herd of models,” arXiv preprint arXiv:2407.21783, 2024.
[447] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N.
Gomez, Ł. Kaiser, and I. Polosukhin, “Attention is all you need,” in
Advances in neural information processing systems, 2017, pp. 5998–
6008.
[448] S. Eger, Y. Cao, J. D’Souza, A. Geiger, C. Greisinger, S. Gross,
Y. Hou, B. Krenn, A. Lauscher, Y. Li et al., “Transforming science
with large language models: A survey on ai-assisted scientific dis-
covery, experimentation, content generation, and evaluation,” arXiv
preprint arXiv:2502.05151, 2025.
[449] T. Xie, Y. Wan, W. Huang, Z. Yin, Y. Liu, S. Wang, Q. Linghu,
C. Kit, C. Grazian, W. Zhang et al., “Darwin series: Domain
specific large language models for natural science,” arXiv preprint
arXiv:2308.13565, 2023.
[450] Q. Jin, B. Dhingra, Z. Liu, W. W. Cohen, and X. Lu, “Pubmedqa:
A dataset for biomedical research question answering,” arXiv,
abs/1909.06146,
2019.
[Online].
Available:
https://arxiv.org/abs/
1909.06146
[451] A.
Pal,
L.
K.
Umapathi,
and
M.
Sankarasubbu,
“Medmcqa:
A
large-scale
multi-subject
multi-choice
dataset
for
medical
domain question answering,” arXiv, abs/2203.14371, 2022. [Online].
Available: https://arxiv.org/abs/2203.14371
[452] L. Sun, D. Luo, D. Ma, Z. Zhao, B. Chen, Z. Shen, S. Zhu, L. Chen,
X. Chen, and K. Yu, “Scidfm: A large language model with mixture-
of-experts for science,” arXiv preprint arXiv:2409.18412, 2024.
[453] V. Prabhakar, M. A. Islam, A. Atanas, Y.-T. Wang, J. Han, A. Jhun-
jhunwala, R. Apte, R. Clark, K. Xu, Z. Wang et al., “Omniscience: A
domain-specialized llm for scientific reasoning and discovery,” arXiv
preprint arXiv:2503.17604, 2025.
[454] N. Muennighoff, Z. Yang, W. Shi, X. L. Li, L. Fei-Fei, H. Hajishirzi,
L. Zettlemoyer, P. Liang, E. Cand`es, and T. Hashimoto, “s1: Simple
test-time scaling,” arXiv preprint arXiv:2501.19393, 2025.
[455] A. Jaech, A. Kalai, A. Lerer, A. Richardson, A. El-Kishky, A. Low,
A. Helyar, A. Madry, A. Beutel, A. Carney et al., “Openai o1 system
card,” 2024.
[456] J. R. Platt, “Strong inference: Certain systematic methods of scientific
thinking may produce much more rapid progress than others.” science,
vol. 146, no. 3642, pp. 347–353, 1964.
[457] D. Guo, D. Yang, H. Zhang, J. Song, R. Zhang, R. Xu, Q. Zhu, S. Ma,
P. Wang, X. Bi et al., “Deepseek-r1: Incentivizing reasoning capability
79

in llms via reinforcement learning,” arXiv preprint arXiv:2501.12948,
2025.
[458] D. Rein, B. L. Hou, A. C. Stickland, J. Petty, R. Y. Pang, J. Dirani,
J. Michael, and S. R. Bowman, “Gpqa: A graduate-level google-proof
q&a benchmark,” Nov. 2023.
[459] A. Yang, A. Li, B. Yang, B. Zhang, B. Hui, B. Zheng, B. Yu, C. Gao,
C. Huang, C. Lv et al., “Qwen3 technical report,” arXiv preprint
arXiv:2505.09388, 2025.
[460] K. Team, Y. Bai, Y. Bao, G. Chen, J. Chen, N. Chen, R. Chen,
Y. Chen, Y. Chen, Y. Chen et al., “Kimi k2: Open agentic intelli-
gence,” arXiv preprint arXiv:2507.20534, 2025.
[461] G. Comanici, E. Bieber, M. Schaekermann, I. Pasupat, N. Sachdeva,
I. Dhillon, M. Blistein, O. Ram, D. Zhang, E. Rosen et al., “Gemini
2.5: Pushing the frontier with advanced reasoning, multimodality,
long context, and next generation agentic capabilities,” arXiv preprint
arXiv:2507.06261, 2025.
[462] xAI, “Grok 4,” 2025. [Online]. Available: https://x.ai/news/grok-4
[463] L. Phan, A. Gatti, Z. Han, N. Li, J. Hu, H. Zhang, C. B. C. Zhang,
M. Shaaban, J. Ling, S. Shi et al., “Humanity’s last exam,” arXiv
preprint arXiv:2501.14249, 2025.
[464] A. Cherian, R. Corcodel, S. Jain, and D. Romeres, “LLMPhy:
Complex physical reasoning using large language models and world
models,” arXiv preprint arXiv:2411.08027, 2024.
[465] M.
Herde,
B.
Raonic,
T.
Rohner,
R.
K¨appeli,
R.
Molinaro,
E. de B´ezenac, and S. Mishra, “Poseidon: Efficient foundation models
for PDEs,” Advances in Neural Information Processing Systems,
vol. 37, pp. 72 525–72 624, 2024.
[466] Z. Liu, H. Hu, Y. Lin, Z. Yao, Z. Xie, Y. Wei, J. Ning, Y. Cao,
Z. Zhang, L. Dong et al., “Swin transformer v2: Scaling up capacity
and resolution,” in Proceedings of the IEEE/CVF conference on
computer vision and pattern recognition, 2022, pp. 12 009–12 019.
[467] Z. Zhang, Y. Zhang, H. Yao, J. Luo, R. Zhao, B. Huang, J. Zhao,
Y. Liao, K. Li, L. Zhao et al., “Xiwu: A basis flexible and learnable
llm for high energy physics,” arXiv preprint arXiv:2404.08001, 2024.
[468] J.
Zou,
W.
Li,
Q.
Ma,
Z.
You,
S.
Sun,
Z.
Deng,
X.
Ji,
A. Zhemchugov, W. Fang, C. Fu, K. He, X. Huang, T. Lin,
C. Liu, H. Liu, Z. Mao, J. Qiu, Y. Sun, S. Wen, L. Wu,
L. Wang, Y. Yuan, Y. Zhang, X. Zhang, and G. Zhao, “Offline
data processing system of the besiii experiment,” The European
Physical Journal C, vol. 84, no. 9, p. 937, 2024. [Online]. Available:
https://doi.org/10.1140/epjc/s10052-024-13241-3
[469] H. Cao, Z. Liu, X. Lu, Y. Yao, and Y. Li, “Instructmol: Multi-modal
integration for building a versatile and reliable molecular assistant in
drug discovery,” arXiv preprint arXiv:2311.16208, 2023.
[470] Z. Zhao, D. Ma, L. Chen, L. Sun, Z. Li, Y. Xia, B. Chen, H. Xu,
Z. Zhu, S. Zhu et al., “Chemdfm: a large language foundation model
for chemistry,” arXiv preprint arXiv:2401.14818, 2024.
[471] L. Jiang, S. Sun, B. Qi, Y. Fu, X. Xu, Y. Li, D. Zhou, and T. Fu,
“Chem3dllm: 3d multimodal large language models for chemistry,”
arXiv preprint, 2025.
[472] S. Wang, Y. Guo, Y. Wang, H. Sun, and J. Huang, “Smiles-bert:
Large
scale
unsupervised
pre-training
for
molecular
property
prediction,”
in
Proceedings
of
the
10th
ACM
International
Conference on Bioinformatics, Computational Biology and Health
Informatics, ser. BCB ’19.
New York, NY, USA: Association
for Computing Machinery, 2019, p. 429–436. [Online]. Available:
https://doi.org/10.1145/3307339.3342186
[473] C. Kuenneth and R. Ramprasad, “polybert: a chemical language
model to enable fully machine-driven ultrafast polymer informatics,”
Nature Communications, vol. 14, no. 1, Jul. 2023. [Online].
Available: http://dx.doi.org/10.1038/s41467-023-39868-6
[474] P. He, X. Liu, J. Gao, and W. Chen, “Deberta: Decoding-enhanced
bert with disentangled attention,” arXiv preprint arXiv:2006.03654,
2020.
[475] V. Korolev and P. Protsenko, “Accurate, interpretable predictions of
materials properties within transformer language models,” Patterns,
vol.
4,
no.
10,
p.
100803,
Oct.
2023.
[Online].
Available:
http://dx.doi.org/10.1016/j.patter.2023.100803
[476] J.
Born
and
M.
Manica,
“Regression
transformer
enables
concurrent
sequence
regression
and
generation
for
molecular
language
modelling,”
Nature
Machine
Intelligence,
vol.
5,
no.
4,
p.
432–444,
Apr.
2023.
[Online].
Available:
http://dx.doi.org/10.1038/s42256-023-00639-z
[477] X. Bai, S. He, Y. Li, Y. Xie, X. Zhang, W. Du, and J.-R. Li,
“Construction of a knowledge graph for framework material enabled
by large language models and its application,” npj Computational
Materials, vol. 11, no. 1, p. 51, Feb 2025. [Online]. Available:
https://doi.org/10.1038/s41524-025-01540-6
[478] Z. Liu, W. Zhang, Y. Xia, L. Wu, S. Xie, T. Qin, M. Zhang, and
T.-Y. Liu, “Molxpt: Wrapping molecules with text for generative pre-
training,” 2023. [Online]. Available: https://arxiv.org/abs/2305.10688
[479] A. Radford, J. Wu, R. Child, D. Luan, D. Amodei, and I. Sutskever,
“Language models are unsupervised multitask learners,” OpenAI Blog,
2019.
[480] S. Balaji, R. Magar, Y. Jadhav, and A. B. Farimani, “Gpt-molberta:
Gpt molecular features language model for molecular property
prediction,” 2023. [Online]. Available: https://arxiv.org/abs/2310.
03030
[481] V. Bagal, R. Aggarwal, P. K. Vinod, and U. D. Priyakumar,
“MolGPT: Molecular Generation Using a Transformer-Decoder
Model,” Journal of Chemical Information and Modeling, vol. 62,
no. 9, pp. 2064–2076, May 2022. [Online]. Available: https:
//doi.org/10.1021/acs.jcim.1c00600
[482] D. Flam-Shepherd and A. Aspuru-Guzik, “Language models can
generate molecules, materials, and protein binding sites directly
in three dimensions as xyz, cif, and pdb files,” 2023. [Online].
Available: https://arxiv.org/abs/2305.05708
[483] L. M. Antunes, K. T. Butler, and R. Grau-Crespo, “Crystal structure
generation with autoregressive large language modeling,” Nature
Communications, vol. 15, no. 1, p. 10570, Dec 2024. [Online].
Available: https://doi.org/10.1038/s41467-024-54639-7
[484] R. Okabe, Z. West, A. Chotrattanapituk, M. Cheng, D. C. Carrizales,
W. Xie, R. J. Cava, and M. Li, “Large language model-guided
prediction toward quantum materials synthesis,” 2024. [Online].
Available: https://arxiv.org/abs/2410.20976
[485] Z. Song, S. Lu, M. Ju, Q. Zhou, and J. Wang, “Is large
language
model
all
you
need
to
predict
the
synthesizability
and precursors of crystal structures?” 2024. [Online]. Available:
https://arxiv.org/abs/2407.07016
[486] M. J. Buehler, “MechGPT, a language-based strategy for mechanics
and materials modeling that connects knowledge across scales, disci-
plines, and modalities,” Applied Mechanics Reviews, vol. 76, no. 2,
p. 021001, 2024.
[487] S. C. Tan and B. C. Yiap, “Dna, rna, and protein extraction: the past
and the present,” BioMed Research International, vol. 2009, no. 1, p.
574398, 2009.
[488] E. Nguyen, M. Poli, M. G. Durrant, B. Kang, D. Katrekar, D. B. Li,
L. J. Bartie, A. W. Thomas, S. H. King, G. Brixi et al., “Sequence
modeling and design from molecular to genome scale with evo,”
Science, vol. 386, no. 6723, p. eado9336, 2024.
[489] G. Brixi, M. G. Durrant, J. Ku, M. Poli, G. Brockman, D. Chang,
G. A. Gonzalez, S. H. King, D. B. Li, A. T. Merchant et al., “Genome
modeling and design across all domains of life with evo 2,” BioRxiv,
pp. 2025–02, 2025.
[490] A. Rives, J. Meier, T. Sercu, S. Goyal, Z. Lin et al., “Biological
structure and function emerge from scaling unsupervised learning to
250 million protein sequences,” Proceedings of the National Academy
of Sciences, vol. 118, no. 15, 2021.
[491] Z. Lin, H. Akin, R. Rao, B. Hie, Z. Zhu, W. Lu, N. Smetanin,
A. dos Santos Costa, M. Fazel-Zarandi, T. Sercu, S. Candido et al.,
“Language models of protein sequences at the scale of evolution
enable accurate structure prediction,” bioRxiv, 2022.
[492] T. Hayes, R. Rao, H. Akin, N. J. Sofroniew, D. Oktay, Z. Lin,
R. Verkuil, V. Q. Tran, J. Deaton, M. Wiggert, R. Badkundri,
I.
Shafkat,
J.
Gong,
A.
Derry,
R.
S.
Molina,
N.
Thomas,
Y. A. Khan, C. Mishra, C. Kim, L. J. Bartie, M. Nemeth,
P. D. Hsu, T. Sercu, S. Candido, and A. Rives, “Simulating
500 million years of evolution with a language model,” Science,
vol.
387,
no.
6736,
pp.
850–858,
2025.
[Online].
Available:
https://www.science.org/doi/10.1126/science.ads0018
[493] R. Rao, J. Liu, R. Verkuil, J. Meier, J. F. Canny, P. Abbeel, T. Sercu,
and A. Rives, “Msa transformer,” in Proceedings of the 38th
International Conference on Machine Learning, ser. Proceedings of
Machine Learning Research, M. Meila and T. Zhang, Eds., vol.
139.
PMLR, 18–24 Jul 2021, pp. 8844–8856. [Online]. Available:
https://proceedings.mlr.press/v139/rao21a.html
[494] J.
Meier,
R.
Rao,
R.
Verkuil,
J.
Liu,
T.
Sercu,
and
A.
Rives,
“Language
models
enable
zero-shot
prediction
of
the
effects
of
mutations
on
protein
function,”
in
Advances
in
Neural
Information
Processing
Systems,
vol.
34,
2021.
[Online]. Available: https://proceedings.neurips.cc/paper/2021/hash/
f51338d736f95dd42427296047067694-Abstract.html
80

[495] C. Hsu, R. Verkuil, J. Liu, Z. Lin, B. Hie, T. Sercu, A. Lerer,
and A. Rives, “Learning inverse folding from millions of predicted
structures,” in Proceedings of the 39th International Conference on
Machine Learning, ser. Proceedings of Machine Learning Research,
K. Chaudhuri, S. Jegelka, L. Song, C. Szepesvari, G. Niu, and
S. Sabato, Eds., vol. 162.
PMLR, 17–23 Jul 2022, pp. 8946–8970.
[Online]. Available: https://proceedings.mlr.press/v162/hsu22a.html
[496] Z. Lin, H. Akin, R. Rao, B. Hie, Z. Zhu, W. Lu, N. Smetanin,
R. Verkuil, O. Kabeli, Y. Shmueli, A. Dos Santos Costa, M. Fazel-
Zarandi, T. Sercu, S. Candido, and A. Rives, “Evolutionary-scale
prediction of atomic-level protein structure with a language model,”
Science, vol. 379, no. 6637, pp. 1123–1130, 2023. [Online].
Available: https://www.science.org/doi/10.1126/science.ade2574
[497] N. Ferruz, S. Schmidt, and B. H¨ocker, “Protgpt2 is a deep unsuper-
vised language model for protein design,” Nature communications,
vol. 13, no. 1, p. 4348, 2022.
[498] A. Madani, B. McCann, N. Naik, N. S. Keskar, N. Anand, R. R.
Eguchi, P.-S. Huang, and R. Socher, “Progen: Language modeling
for protein generation,” arXiv preprint arXiv:2004.03497, 2020.
[499] E. Nijkamp, J. A. Ruffolo, E. N. Weinstein, N. Naik, and A. Madani,
“Progen2: Exploring the boundaries of protein language models,” Cell
Systems, vol. 14, no. 11, pp. 968–978, 2023.
[500] A. Elnaggar, H. Essam, W. Salah-Eldin, W. Moustafa, M. Elkerdawy,
C. Rochereau, and B. Rost, “Ankh: Optimized protein language model
unlocks general-purpose modelling,” arXiv preprint, 2023.
[501] L. Lv, Z. Lin, H. Li, Y. Liu, J. Cui, C. Y. Chen, L. Yuan, and Y. Tian,
“Prollama: A protein language model for multi-task protein language
processing,” arXiv preprint, 2024.
[502] S. Liu, Y. Li, Z. Li, A. Gitter, Y. Zhu, J. Lu, Z. Xu, W. Nie,
A. Ramanathan, C. Xiao, J. Tang, H. Guo, and A. Anandkumar,
“A text-guided protein design framework,” arXiv preprint, 2023, v4,
2025.
[503] C. Yuan, S. Li, G. Ye, Y. Zhang, L. Huang, W. Huang, W. Liu,
J. Yao, and Y. Rong, “Annotation-guided protein design with multi-
level domain alignment,” arXiv preprint, 2024.
[504] F. Dai et al., “Toward de novo protein design from natural language,”
bioRxiv, 2025. [Online]. Available: https://www.biorxiv.org/content/
10.1101/2024.08.01.606258v4
[505] Y. Xiao, E. Sun, Y. Jin, Q. Wang, and W. Wang, “Proteingpt:
Multimodal llm for protein property prediction and structure under-
standing,” arXiv preprint, 2024, v2, 2025.
[506] C. Wang, H. Fan, R. Quan, and Y. Yang, “Protchatgpt: Towards
understanding proteins with large language models,” arXiv preprint,
2024, v2, 2025.
[507] H. Xu and S. Wang, “Protranslator: Zero-shot protein function pre-
diction using textual description,” arXiv preprint, 2022.
[508] H. Xu, A. Woicik, R. B. Altman, H. Poon, and S. Wang,
“Multilingual translation for zero-shot biomedical classification using
biotranslator,” Nature Communications, vol. 14, 2023. [Online].
Available: https://www.nature.com/articles/s41467-023-36476-2
[509] H. Abdine, M. Chatzianastasis, C. Bouyioukos, and M. Vazirgiannis,
“Prot2text: Multimodal protein’s function generation with gnns and
transformers,” in Proceedings of the AAAI Conference on Artificial
Intelligence, vol. 38, no. 10, 2024, pp. 10 757–10 765.
[510] X. Zhou, C. Han, Y. Zhang, J. Su, K. Zhuang, S. Jiang, Z. Yuan,
W. Zheng, F. Dai, Y. Zhou et al., “Decoding the molecular language
of proteins with evolla,” bioRxiv, pp. 2025–01, 2025.
[511] B. P. de Almeida, G. Richard, H. Dalla-Torre, C. Blum, L. Hexemer,
P. Pandey, S. Laurent, C. Rajesh, M. Lopez, A. Laterre et al., “A
multimodal conversational agent for dna, rna and protein tasks,”
Nature Machine Intelligence, pp. 1–14, 2025.
[512] Y. Liu, S. Ding, S. Zhou, W. Fan, and Q. Tan, “Moleculargpt:
Open large language model (llm) for few-shot molecular property
prediction,” arXiv preprint arXiv:2406.12950, 2024.
[513] H. Cui, C. Wang, H. Maan, K. Pang, F. Luo, N. Duan, and B. Wang,
“scgpt: toward building a foundation model for single-cell multi-omics
using generative ai,” Nature methods, vol. 21, no. 8, pp. 1470–1480,
2024.
[514] S. Chithrananda, G. Grand, and B. Ramsundar, “ChemBERTa: large-
scale self-supervised pretraining for molecular property prediction,”
in Machine Learning for Molecules Workshop at NeurIPS 2020, 2020.
[515] J. Li and X. Jiang, “Mol-bert: An effective molecular representation
with bert for molecular property prediction,” Wireless Communica-
tions and Mobile Computing, vol. 2021, no. 1, p. 7181815, 2021.
[516] K. Hatakeyama-Sato, N. Yamane, Y. Igarashi, Y. Nabae, and
T. Hayakawa, “Prompt engineering of gpt-4 for chemical research:
what can/cannot be done?” Science and Technology of Advanced
Materials: Methods, vol. 3, no. 1, p. 2260300, 2023.
[517] S. Jiang, Y. Wang, S. Song, Y. Zhang, Z. Meng, B. Lei, J. Wu, J. Sun,
and Z. Liu, “Omniv-med: Scaling medical vision-language model
for universal visual understanding,” arXiv preprint arXiv:2504.14692,
2025.
[518] Y. Labrak, A. Bazoge, E. Morin, P.-A. Gourraud, M. Rouvier, and
R. Dufour, “Biomistral: A collection of open-source pretrained large
language models for medical domains,” 2024.
[519] E. Bolton, A. Venigalla, M. Yasunaga, D. Hall, B. Xiong, T. Lee,
R. Daneshjou, J. Frankle, P. Liang, M. Carbin, and C. D. Manning,
“Biomedlm: A 2.7b parameter language model trained on biomedical
text,” 2024. [Online]. Available: https://arxiv.org/abs/2403.18421
[520] A. Toma, P. R. Lawler, J. Ba, R. G. Krishnan, B. B. Rubin, and
B. Wang, “Clinical camel: An open expert-level medical language
model with dialogue-based knowledge encoding,” arXiv preprint
arXiv:2305.12031, 2023.
[521] T. Han, L. C. Adams, J.-M. Papaioannou, P. Grundmann, T. Ober-
hauser, A. L¨oser, D. Truhn, and K. K. Bressem, “Medalpaca–an open-
source collection of medical conversational ai models and training
data,” arXiv preprint arXiv:2304.08247, 2023.
[522] D.
Jin,
E.
Pan,
N.
Oufattole,
W.
Weng,
H.
Fang,
and
P. Szolovits, “What disease does this patient have? a large-
scale
open
domain
question
answering
dataset
from
medical
exams,”
arXiv,
abs/2009.13081,
2020.
[Online].
Available:
https://arxiv.org/abs/2009.13081
[523] P. Liu, W. Yuan, J. Fu, Z. Jiang, H. Hayashi, and G. Neubig, “Pre-
train, prompt, and predict: A systematic survey of prompting methods
in natural language processing,” ACM Comput. Surv., vol. 55, no. 9,
Jan. 2023. [Online]. Available: https://doi.org/10.1145/3560815
[524] X. Wang, N. Chen, J. Chen, Y. Hu, Y. Wang, X. Wu, A. Gao, X. Wan,
H. Li, and B. Wang, “Apollo: Lightweight multilingual medical llms
towards democratizing medical ai to 6b people,” 2024.
[525] H. Zhang, J. Chen, F. Jiang, F. Yu, Z. Chen, J. Li, G. Chen, X. Wu,
Z. Zhang, Q. Xiao, X. Wan, B. Wang, and H. Li, “Huatuogpt,
towards taming language models to be a doctor,” arXiv preprint
arXiv:2305.15075, 2023.
[526] C. Wu, W. Lin, X. Zhang, Y. Zhang, Y. Wang, and W. Xie, “Pmc-
llama: Towards building open-source language models for medicine,”
2023. [Online]. Available: https://arxiv.org/abs/2304.14454
[527] Y. Tian, R. Gan, Y. Song, J. Zhang, and Y. Zhang, “Chimed-gpt: A chi-
nese medical large language model with full training regime and better
alignment to human preferences,” arXiv preprint arXiv:2311.06025,
2023.
[528] J. Zhang, R. Gan, J. Wang, Y. Zhang, L. Zhang, P. Yang, X. Gao,
Z. Wu, X. Dong, J. He, J. Zhuo, Q. Yang, Y. Huang, X. Li, Y. Wu,
J. Lu, X. Zhu, W. Chen, T. Han, K. Pan, R. Wang, H. Wang, X. Wu,
Z. Zeng, and C. Chen, “Fengshenbang 1.0: Being the foundation of
chinese cognitive intelligence,” CoRR, vol. abs/2209.02970, 2022.
[529] Y. Bai, A. Jones, K. Ndousse, A. Askell, A. Chen, N. DasSarma,
D. Drain, S. Fort, D. Ganguli, T. Henighan et al., “Training a help-
ful and harmless assistant with reinforcement learning from human
feedback,” arXiv preprint arXiv:2204.05862, 2022.
[530] S. Yang, H. Zhao, S. Zhu, G. Zhou, H. Xu, Y. Jia, and H. Zan,
“Zhongjing: Enhancing the chinese medical capabilities of large
language model through expert feedback and real-world multi-turn
dialogue,” in Proceedings of the AAAI Conference on Artificial
Intelligence, vol. 38, no. 17, 2024, pp. 19 368–19 376.
[531] Q. Xie, Q. Chen, A. Chen, C. Peng, Y. Hu, F. Lin, X. Peng,
J. Huang, J. Zhang, V. Keloth, X. Zhou, L. Qian, H. He, D. Shung,
L. Ohno-Machado, Y. Wu, H. Xu, and J. Bian, “Me llama:
Foundation large language models for medical applications,” 2024.
[Online]. Available: https://arxiv.org/abs/2402.12749
[532] B. Wang, H. Zhao, H. Zhou, L. Song, M. Xu, W. Cheng,
X. Zeng, Y. Zhang, Y. Huo, Z. Wang et al., “Baichuan-m1: Pushing
the medical capability of large language models,” arXiv preprint
arXiv:2502.12671, 2025.
[533] J. Liu, Y. Wang, J. Du, J. T. Zhou, and Z. Liu, “Medcot: Medical chain
of thought via hierarchical expert,” arXiv preprint arXiv:2412.13736,
2024.
[534] G. Reale-Nosei, E. Amador-Dom´ınguez, and E. Serrano, “From vision
to text: A comprehensive review of natural image captioning in
medical diagnosis and radiology report generation,” Medical Image
Analysis, vol. 97, p. 103264, 2024.
[535] Z. Lin, D. Zhang, Q. Tao, D. Shi, G. Haffari, Q. Wu, M. He, and Z. Ge,
“Medical visual question answering: A survey,” Artificial Intelligence
in Medicine, vol. 143, p. 102611, 2023.
81

[536] Y. Wang, J. Liu, S. Gao, B. Feng, Z. Tang, X. Gai, J. Wu, and Z. Liu,
“V2t-cot: From vision to text chain-of-thought for medical reasoning
and diagnosis,” arXiv preprint arXiv:2506.19610, 2025.
[537] C. Li, C. Wong, S. Zhang, N. Usuyama, H. Liu, J. Yang, T. Nau-
mann, H. Poon, and J. Gao, “Llava-med: Training a large language-
and-vision assistant for biomedicine in one day,” arXiv preprint
arXiv:2306.00890, 2023.
[538] S. Lee, J. Youn, H. Kim, M. Kim, and S. H. Yoon, “Cxr-llava:
a multimodal large language model for interpreting chest x-ray
images,” 2024. [Online]. Available: https://arxiv.org/abs/2310.18341
[539] Z. Liu, Y. Li, P. Shu, A. Zhong, L. Yang, C. Ju, Z. Wu, C. Ma,
J. Luo, C. Chen, S. Kim, J. Hu, H. Dai, L. Zhao, D. Zhu, J. Liu,
W. Liu, D. Shen, T. Liu, Q. Li, and X. Li, “Radiology-llama2:
Best-in-class large language model for radiology,” 2023. [Online].
Available: https://arxiv.org/abs/2309.06419
[540] M. Moor, Q. Huang, S. Wu, M. Yasunaga, C. Zakka, Y. Dalmia, E. P.
Reis, P. Rajpurkar, and J. Leskovec, “Med-flamingo: A multimodal
medical few-shot learner,” arXiv preprint arXiv:2307.15189, 2023.
[541] J. Chen, C. Gui, R. Ouyang, A. Gao, S. Chen, G. H. Chen,
X.
Wang,
R.
Zhang,
Z.
Cai,
K.
Ji,
G.
Yu,
X.
Wan,
and
B.
Wang,
“Huatuogpt-vision,
towards
injecting
medical
visual
knowledge into multimodal llms at scale,” 2024. [Online]. Available:
https://arxiv.org/abs/2406.19280
[542] T. Li, Y. Su, W. Li, B. Fu, Z. Chen, Z. Huang, G. Wang, C. Ma,
Y. Chen, M. Hu, Y. Li, P. Chen, X. Hu, Z. Deng, Y. Ji, J. Ye,
Y. Qiao, and J. He, “GMAI-VL & GMAI-VL-5.5m: A large vision-
language model and a comprehensive multimodal dataset towards
general medical ai,” arXiv preprint arXiv:2411.14522, 2025.
[543] A. Sellergren, S. Kazemzadeh, T. Jaroensri, A. Kiraly, M. Traverse,
T. Kohlberger, S. Xu, F. Jamil, C. Hughes, C. Lau et al., “Medgemma
technical report,” arXiv preprint arXiv:2507.05201, 2025.
[544] J. Chen, Z. Cai, K. Ji, X. Wang, W. Liu, R. Wang, J. Hou, and
B. Wang, “Huatuogpt-o1, towards medical complex reasoning with
llms,” arXiv preprint arXiv:2412.18925, 2024.
[545] H. Xu, Y. Nie, H. Wang, Y. Chen, W. Li, J. Ning, L. Liu, H. Wang,
L. Zhu, J. Liu et al., “Medground-r1: Advancing medical image
grounding via spatial-semantic rewarded group relative policy opti-
mization,” arXiv preprint arXiv:2507.02994, 2025.
[546] Y. Su, T. Li, J. Liu, C. Ma, J. Ning, C. Tang, S. Ju, J. Ye, P. Chen,
M. Hu et al., “GMAI-VL-R1: Harnessing reinforcement learning
for multimodal medical reasoning,” arXiv preprint arXiv:2504.01886,
2025.
[547] F. Yang, H. Kong, J. Ying, Z. Chen, T. Luo, W. Jiang, Z. Yuan,
Z. Wang, Z. Ma, S. Wang et al., “Seedllm· rice: A large language
model integrated with rice biological knowledge graph,” Molecular
Plant, 2025.
[548] G. Penedo, H. Kydl´ıˇcek, L. B. allal, A. Lozhkov, M. Mitchell,
C. Raffel, L. Von Werra, and T. Wolf, “The FineWeb datasets:
Decanting the web for the finest text data at scale,” in Advances in
Neural Information Processing Systems, vol. 37.
Curran Associates,
Inc., 2024, pp. 30 811–30 849.
[549] S. Huang, T. Cheng, J. K. Liu, W. Xu, J. Hao, L. Song, Y. Xu, J. Yang,
J. Liu, C. Zhang, L. Chai, R. Yuan, X. Luo, Q. Wang, Y. Fan, Q. Zhu,
Z. Zhang, Y. Gao, J. Fu, Q. Liu, H. Li, G. Zhang, Y. Qi, X. Yinghui,
W. Chu, and Z. Wang, “OpenCoder: The open cookbook for top-
tier code large language models,” in Proceedings of the 63rd Annual
Meeting of the Association for Computational Linguistics (Volume 1:
Long Papers), 2025, pp. 33 167–33 193.
[550] Z. Chen, W. Jiang, J. Li, Z. Yuan, H. Kong, W. Ouyang, and
N. Dong, “Graphgen: Enhancing supervised fine-tuning for llms
with knowledge-driven synthetic data generation,” arXiv preprint
arXiv:2505.20416, 2025.
[551] X. Yang, J. Gao, W. Xue, and E. Alexandersson, “Pllama: An
open-source large language model for plant science,” arXiv preprint
arXiv:2401.01600, 2024.
[552] M. Awais, A. H. S. A. Alharthi, A. Kumar, H. Cholakkal, and R. M.
Anwer, “Agrogpt: Efficient agricultural vision-language model with
expert tuning,” in 2025 IEEE/CVF Winter Conference on Applications
of Computer Vision (WACV).
IEEE, 2025, pp. 5687–5696.
[553] X. Luo, A. Rechardt, G. Sun, K. K. Nejad, F. Y´a˜nez, B. Yilmaz,
K. Lee, A. O. Cohen, V. Borghesani, A. Pashkov et al., “Large
language models surpass human experts in predicting neuroscience
results,” Nature human behaviour, vol. 9, no. 2, pp. 305–315, 2025.
[554] J. W. Kim, A. Alaa, and D. Bernardo, “EEG-GPT: Exploring
capabilities of large language models for EEG classification and
interpretation,” arXiv preprint arXiv:2401.18006, 2024.
[555] W.-B. Jiang, Y. Wang, B.-L. Lu, and D. Li, “Neurolm: A universal
multi-task foundation model for bridging the gap between language
and eeg signals,” arXiv preprint arXiv:2409.00101, 2024.
[556] W. Xia, R. de Charette, C. Oztireli, and J.-H. Xue, “Umbrae: Unified
multimodal brain decoding,” in European Conference on Computer
Vision.
Springer, 2024, pp. 242–259.
[557] A. Radford, J. W. Kim, C. Hallacy, A. Ramesh, G. Goh, S. Agarwal,
G. Sastry, A. Askell, P. Mishkin, J. Clark, G. Krueger, and
I. Sutskever, “Learning transferable visual models from natural
language supervision,” in Proceedings of the 38th International
Conference on Machine Learning, ser. Proceedings of Machine
Learning Research, M. Meila and T. Zhang, Eds., vol. 139.
PMLR,
18–24
Jul
2021,
pp.
8748–8763.
[Online].
Available:
https://proceedings.mlr.press/v139/radford21a.html
[558] J. Chen, Y. Qi, Y. Wang, and G. Pan, “Mindgpt: Interpreting what
you see with non-invasive brain recordings,” IEEE Transactions on
Image Processing, 2025.
[559] W. Qiu, Z. Huang, H. Hu, A. Feng, Y. Yan, and R. Ying, “Mindllm: A
subject-agnostic and versatile model for fmri-to-text decoding,” arXiv
preprint arXiv:2502.15786, 2025.
[560] W. Lu, C. Song, J. Wu, P. Zhu, Y. Zhou, W. Mai, Q. Zheng, and
W. Ouyang, “Unimind: Unleashing the power of llms for unified
multi-task brain decoding,” arXiv preprint arXiv:2506.18962, 2025.
[561] W. Cui, W. Jeong, P. Th¨olke, T. Medani, K. Jerbi, A. A. Joshi, and
R. M. Leahy, “Neuro-gpt: Towards a foundation model for eeg,” in
2024 IEEE International Symposium on Biomedical Imaging (ISBI).
IEEE, 2024, pp. 1–5.
[562] T. D. Nguyen, Y.-S. Ting, I. Ciuc˘a, C. O’Neill, Z.-C. Sun,
M. Jabło´nska, S. Kruk, E. Perkowski, J. Miller, J. Li et al., “Astrol-
lama: Towards specialized foundation models in astronomy,” arXiv
preprint arXiv:2309.06126, 2023.
[563] S. Zaman, M. J. Smith, P. Khetarpal, R. Chakrabarty, M. Ginolfi,
M. Huertas-Company, M. Jabło´nska, S. Kruk, M. L. Lain, S. J. R.
M´endez et al., “Astrollava: towards the unification of astronomical
data and natural language,” arXiv preprint arXiv:2504.08583, 2025.
[564] T. de Haan, Y.-S. Ting, T. Ghosal, T. D. Nguyen, A. Accomazzi,
A. Wells, N. Ramachandra, R. Pan, and Z. Sun, “Achieving gpt-4o
level performance in astronomy with a specialized 8b-parameter large
language model,” Scientific Reports, vol. 15, no. 1, p. 13751, 2025.
[565] E. J. Hu, Y. Shen, P. Wallis, Z. Allen-Zhu, Y. Li, S. Wang, L. Wang,
W. Chen et al., “Lora: Low-rank adaptation of large language models.”
The International Conference on Learning Representations (ICLR),
vol. 1, no. 2, p. 3, 2022.
[566] H. W. Leung and J. Bovy, “Deep learning of multi-element abun-
dances from high-resolution spectroscopic data,” Monthly Notices of
the Royal Astronomical Society, vol. 483, no. 3, pp. 3255–3277, 2019.
[567] T. de Haan, Y.-S. Ting, T. Ghosal, T. D. Nguyen, A. Accomazzi,
E. Herron, V. Lama, R. Pan, A. Wells, and N. Ramachandra, “As-
tromlab 4: Benchmark-topping performance in astronomy q&a with
a 70b-parameter domain-specialized reasoning model,” arXiv preprint
arXiv:2505.17592, 2025.
[568] C. Deng, T. Zhang, Z. He, Q. Chen, Y. Shi, Y. Xu, L. Fu, W. Zhang,
X. Wang, C. Zhou et al., “K2: A foundation language model for
geoscience knowledge understanding and utilization,” in Proceedings
of the 17th ACM International Conference on Web Search and Data
Mining, 2024, pp. 161–170.
[569] Z. Chen, X. Wang, Y. Liao, M. Lin, and Y. Bai, “Climatechat:
Designing data and methods for instruction tuning llms to answer
climate change queries,” arXiv preprint arXiv:2506.13796, 2025.
[570] Z. Bi, N. Zhang, Y. Xue, Y. Ou, D. Ji, G. Zheng, and H. Chen,
“Oceangpt: A large language model for ocean science tasks,” arXiv
preprint arXiv:2310.02031, 2023.
[571] H. Jiang, J. Yin, Q. Wang, J. Feng, and G. Chen, “Eaglevision: Object-
level attribute multimodal llm for remote sensing,” arXiv preprint
arXiv:2503.23330, 2025.
[572] W. Zhang, M. Cai, T. Zhang, Y. Zhuang, J. Li, and X. Mao,
“Earthmarker: A visual prompting multi-modal large language model
for remote sensing,” IEEE Transactions on Geoscience and Remote
Sensing, 2024.
[573] A. Shabbir, M. Zumri, M. Bennamoun, F. S. Khan, and S. Khan,
“Geopixel: Pixel grounding large multimodal model in remote sens-
ing,” arXiv preprint arXiv:2501.13925, 2025.
[574] F. Wang, M. Chen, Y. Li, D. Wang, H. Wang, Z. Guo, Z. Wang,
B. Shan, L. Lan, Y. Wang et al., “Geollava-8k: Scaling remote-sensing
multimodal large language models to 8k resolution,” arXiv preprint
arXiv:2505.21375, 2025.
82

[575] S. Soni, A. Dudhane, H. Debary, M. Fiaz, M. A. Munir, M. S. Danish,
P. Fraccaro, C. D. Watson, L. J. Klein, F. S. Khan et al., “Earthdial:
Turning multi-sensory earth observations to interactive dialogues,”
in Proceedings of the Computer Vision and Pattern Recognition
Conference, 2025, pp. 14 303–14 313.
[576] D. Wang, M. Hu, Y. Jin, Y. Miao, J. Yang, Y. Xu, X. Qin, J. Ma,
L. Sun, C. Li et al., “Hypersigma: Hyperspectral intelligence com-
prehension foundation model,” IEEE Transactions on Pattern Analysis
and Machine Intelligence, 2025.
[577] F. Wang, H. Wang, D. Wang, Z. Guo, Z. Zhong, L. Lan, W. Yang, and
J. Zhang, “Harnessing massive satellite imagery with efficient masked
image modeling,” arXiv preprint arXiv:2406.11933, 2024.
[578] F. Wang, H. Wang, Y. Wang, D. Wang, M. Chen, H. Zhao,
Y. Sun, S. Wang, L. Lan, W. Yang et al., “Roma: Scaling up
mamba-based foundation models for remote sensing,” arXiv preprint
arXiv:2503.10392, 2025.
[579] J.
A.
Irvin,
E.
R.
Liu,
J.
C.
Chen,
I.
Dormoy,
J.
Kim,
S. Khanna, Z. Zheng, and S. Ermon, “Teochat: A large vision-
language assistant for temporal earth observation data,” arXiv preprint
arXiv:2410.06234, 2024.
[580] E. Angeloudi, J. Audenaert, M. Bowles, B. M. Boyd, D. Chemaly,
B. Cherinka, I. Ciuc˘a, M. Cranmer, A. Do, M. Grayling et al., “The
multimodal universe: enabling large-scale machine learning with 100
tb of astronomical scientific data,” Advances in Neural Information
Processing Systems, vol. 37, pp. 57 841–57 913, 2024.
[581] C. O. de Burgh-Day and T. Leeuwenburg, “Machine learning for
numerical weather and climate modelling: a review,” Geoscientific
Model Development, vol. 16, no. 22, pp. 6433–6477, 2023.
[582] H. Touvron, L. Martin, K. Stone, P. Albert, A. Almahairi, Y. Babaei,
N. Bashlykov, S. Batra, P. Bhargava, S. Bhosale et al., “LLaMA
2: Open foundation and fine-tuned chat models,” arXiv preprint
arXiv:2307.09288, 2023.
[583] Q. Team, “Qwen2 technical report,” arXiv preprint arXiv:2407.10671,
2024.
[584] W.-L. Chiang, Z. Li, Z. Lin, Y. Sheng, Z. Wu, H. Zhang, L. Zheng,
S. Zhuang, Y. Zhuang, J. E. Gonzalez et al., “Vicuna: An open-
source chatbot impressing gpt-4 with 90%* chatgpt quality,” See
https://vicuna. lmsys. org (accessed 14 April 2023), vol. 2, no. 3,
p. 6, 2023.
[585] H. Xiong, S. Wang, Y. Zhu, Z. Zhao, Y. Liu, L. Huang, Q. Wang,
and D. Shen, “Doctorglm: Fine-tuning your chinese doctor is not a
herculean task,” arXiv preprint arXiv:2304.01097, 2023.
[586] A. English and C. A. Ford, “The hipaa privacy rule and adolescents:
legal questions and clinical challenges,” Perspectives on sexual and
reproductive health, vol. 36, no. 2, pp. 80–86, 2004.
[587] M. Reichstein, G. Camps-Valls, B. Stevens, M. Jung, J. Denzler
et al., “Deep learning and process understanding for data-driven earth
system science,” Nature, vol. 566, no. 7743, pp. 195–204, 2019.
[588] Y. He, F. Huang, X. Jiang, Y. Nie, M. Wang, J. Wang, and H. Chen,
“Foundation model for advancing healthcare: Challenges, opportuni-
ties and future directions,” IEEE Reviews in Biomedical Engineering,
2024.
[589] K. Kuckreja, M. S. Danish, M. Naseer, A. Das, S. Khan, and F. S.
Khan, “Geochat: Grounded large vision-language model for remote
sensing,” in Proceedings of the IEEE/CVF Conference on Computer
Vision and Pattern Recognition, 2024, pp. 27 831–27 840.
[590] L. L. Wang, K. Lo, Y. Chandrasekhar, R. Reas, J. Yang, D. Burdick,
D. Eide, K. Funk, Y. Katsis, R. M. Kinney, Y. Li, Z. Liu, W. Merrill,
P. Mooney, D. A. Murdick, D. Rishi, J. Sheehan, Z. Shen, B. Stilson,
A. D. Wade, K. Wang, N. X. R. Wang, C. Wilhelm, B. Xie, D. M.
Raymond, D. S. Weld, O. Etzioni, and S. Kohlmeier, “CORD-19:
The COVID-19 open research dataset,” in Proceedings of the 1st
Workshop on NLP for COVID-19 at ACL 2020.
Online: Association
for Computational Linguistics, Jul. 2020.
[591] A. Algaba, V. Holst, F. Tori, M. Mobini, B. Verbeken, S. Wen-
mackers, and V. Ginis, “How deep do large language models in-
ternalize scientific literature and citation practices?” arXiv preprint
arXiv:2504.02767, 2025.
[592] X. Guan, Y. Liu, H. Lin, Y. Lu, B. He, X. Han, and L. Sun, “Mitigat-
ing large language model hallucinations via autonomous knowledge
graph-based retrofitting,” in Proceedings of the AAAI Conference on
Artificial Intelligence, vol. 38, no. 16, 2024, pp. 18 126–18 134.
[593] H. Zhang, R. Li, Y. Zhang, T. Xiao, J. Chen, J. Ding, and
H. Chen, “The evolving role of large language models in scientific
innovation: Evaluator, collaborator, and scientist,” arXiv preprint
arXiv:2507.11810, 2025.
[594] A. Young, B. Chen, C. Li, C. Huang, G. Zhang, G. Zhang, H. Li,
J. Zhu, J. Chen, J. Chang et al., “Yi: Open foundation models by 01.
ai,” arXiv preprint arXiv:2403.04652, 2024.
[595] Common Crawl Foundation, “Common crawl: Open repository of
web crawl data,” https://commoncrawl.org/, 2008, accessed 2025-08-
28; large longitudinal web crawl (monthly snapshots) used widely in
research.
[596] A. P. Thompson, H. M. Aktulga, R. Berger, D. S. Bolintineanu, W. M.
Brown, P. S. Crozier, P. J. in ’t Veld, A. Kohlmeyer, S. G. Moore,
T. D. Nguyen, R. Shan, M. J. Stevens, J. Tranchida, C. Trott, and
S. J. Plimpton, “LAMMPS - a flexible simulation tool for particle-
based materials modeling at the atomic, meso, and continuum scales,”
Comp. Phys. Comm., vol. 271, p. 108171, 2022.
[597] M. Vogelsberger, S. Genel, V. Springel, P. Torrey, D. Sijacki, D. Xu,
G. Snyder, D. Nelson, and L. Hernquist, “Introducing the illustris
project: simulating the coevolution of dark and visible matter in the
universe,” Monthly Notices of the Royal Astronomical Society, vol.
444, no. 2, pp. 1518–1547, 2014.
[598] A. A. Klypin, S. Trujillo-Gomez, and J. Primack, “Dark matter
halos in the standard cosmological model: Results from the bolshoi
simulation,” The Astrophysical Journal, vol. 740, no. 2, p. 102, 2011.
[599] G. L. Bryan, M. L. Norman, B. W. O’Shea, T. Abel, J. H. Wise,
M. J. Turk, D. R. Reynolds, D. C. Collins, P. Wang, S. W. Skillman
et al., “Enzo: An adaptive mesh refinement code for astrophysics,”
The Astrophysical Journal Supplement Series, vol. 211, no. 2, p. 19,
2014.
[600] CERN Open Data team, “Cern open data portal,” https://opendata.
cern.ch, European Organization for Nuclear Research (CERN), 2014,
petabyte-scale collider data with documentation.
[601] LHCb Collaboration, “The large hadron collider beauty (lhcb) ex-
periment,” https://home.cern/science/experiments/lhcb, March 2022,
accessed 2025-08-28.
[602] A. Damascelli, Z. Hussain, and Z.-X. Shen, “Angle-resolved photoe-
mission studies of the cuprate superconductors,” Reviews of Modern
Physics, vol. 75, no. 2, p. 473, 2003.
[603] “Alma
science
archive,”
https://almascience.nrao.edu/alma-data/
archive, 2025, accessed 2025-08-28.
[604] D. Chapon and P. Hennebelle, “The galactica database: an open,
generic and versatile tool for the dissemination of simulation data
in astrophysics,” arXiv preprint arXiv:2411.08647, 2024.
[605] L. Li, Y. Wang, R. Xu, P. Wang, X. Feng, L. Kong, and Q. Liu,
“Multimodal arxiv: A dataset for improving scientific comprehension
of large vision-language models,” arXiv preprint arXiv:2403.00231,
2024.
[606] J. J. Irwin and B. K. Shoichet, “Zinc- a free database of commercially
available compounds for virtual screening,” Journal of chemical
information and modeling, vol. 45, no. 1, pp. 177–182, 2005.
[607] D. Polykovskiy, A. Zhebrak, B. Sanchez-Lengeling, S. Golovanov,
O. Tatanov, S. Belyaev, R. Kurbanov, A. Artamonov, V. Aladinskiy,
M. Veselov et al., “Molecular sets (MOSES): a benchmarking plat-
form for molecular generation models,” Frontiers in pharmacology,
2020.
[608] B. Xu, Y. Lu, C. Li, L. Yue, X. Wang, N. Hao, T. Fu, and J. Chen,
“Smiles-mamba: Chemical mamba foundation models for drug admet
prediction,” arXiv preprint arXiv:2408.05696, 2024.
[609] T. Fu, W. Gao, C. Xiao, J. Yasonik, C. W. Coley, and J. Sun, “Dif-
ferentiable scaffolding tree for molecular optimization,” International
Conference on Learning Representations, 2022.
[610] T. Fu, C. Xiao, X. Li, L. M. Glass, and J. Sun, “MIMOSA: Multi-
constraint molecule sampling for molecule optimization,” in Proceed-
ings of the AAAI Conference on Artificial Intelligence, vol. 35, 2021,
pp. 125–133.
[611] K. Huang, T. Fu, L. M. Glass, M. Zitnik, C. Xiao, and J. Sun,
“DeepPurpose: a deep learning library for drug–target interaction
prediction,” Bioinformatics, vol. 36, no. 22-23, pp. 5545–5547, 2020.
[612] T. Fu, W. Gao, C. W. Coley, and J. Sun, “Reinforced genetic algorithm
for structure-based drug design,” in Annual Conference on Neural
Information Processing Systems (NeurIPS), 2022.
[613] A. C. Marco, A. Myers, S. J. Graham, P. D’Agostino, and K. Apple,
The USPTO Patent Assignment Dataset: Descriptions and Analysis,
ser. USPTO Economic Working Paper.
SSRN, 2015. [Online].
Available: https://books.google.com.hk/books?id=THPfzwEACAAJ
[614] K. Huang, T. Fu, W. Gao, Y. Zhao, Y. Roohani, J. Leskovec,
C. W. Coley, C. Xiao, J. Sun, and M. Zitnik, “Artificial intelligence
foundation for therapeutic science,” Nature Chemical Biology, pp. 1–
4, 2022.
83

[615] J. E. Saal, S. Kirklin, M. Aykol, B. Meredig, and C. Wolverton,
“Materials
design
and
discovery
with
high-throughput
density
functional theory: The open quantum materials database (oqmd),”
JOM, vol. 65, no. 11, pp. 1501–1509, 2013. [Online]. Available:
https://doi.org/10.1007/s11837-013-0755-4
[616] D. Zagorac, H. M¨uller, S. Ruehl, J. Zagorac, and S. Rehme, “Recent
developments in the Inorganic Crystal Structure Database: theoretical
crystal structure data and related features,” Journal of Applied
Crystallography, vol. 52, no. 5, pp. 918–925, Oct 2019. [Online].
Available: https://doi.org/10.1107/S160057671900997X
[617] Y. G. Chung, E. Haldoupis, B. J. Bucior, M. Haranczyk, S. Lee,
H. Zhang, K. D. Vogiatzis, M. Milisavljevic, S. Ling, J. S. Camp,
B. Slater, J. I. Siepmann, D. S. Sholl, and R. Q. Snurr, “Advances,
updates, and analytics for the computation-ready, experimental
metal–organic framework database: Core mof 2019,” Journal of
Chemical & Engineering Data, vol. 64, no. 12, pp. 5985–5998,
2019. [Online]. Available: https://doi.org/10.1021/acs.jced.9b00835
[618] A. S. Rosen, S. M. Iyer, D. Ray, Z. Yao, A. Aspuru-Guzik,
L. Gagliardi, J. M. Notestein, and R. Q. Snurr, “Machine learning
the quantum-chemical properties of metal–organic frameworks for
accelerated materials discovery,” Matter, vol. 4, no. 5, pp. 1578–1597,
May 2021. [Online]. Available: https://doi.org/10.1016/j.matt.2021.
02.015
[619] K. Gubsch, R. Bence, L. Glasby, and P. Z. Moghadam, “Digimof:
A
database
of
mof
synthesis
information
generated
via
text
mining,” ChemRxiv, 2023, this content is a preprint and has not
been peer-reviewed. [Online]. Available: https://doi.org/10.26434/
chemrxiv-2022-41t70
[620] M. Scheidgen, L. Himanen, A. N. Ladines, D. Sikter, M. Nakhaee,
´A. Fekete, T. Chang, A. Golparvar, J. A. M´arquez, S. Brockhauser
et al., “NOMAD: A distributed web-based platform for managing
materials science research data,” Journal of Open Source Software,
vol. 8, no. 90, p. 5388, 2023.
[621] B. Deng, “Materials Project Trajectory (MPtrj) Dataset,” 7 2023.
[Online].
Available:
https://figshare.com/articles/dataset/Materials
Project Trjectory MPtrj Dataset/23713842
[622] K. Choudhary, K. F. Garrity, A. C. E. Reid, B. DeCost, A. J. Biacchi,
A. R. H. Walker, Z. Trautt, J. Hattrick-Simpers, A. G. Kusne,
A. Centrone, A. Davydov, J. Jiang, R. Pachter, G. Cheon, E. Reed,
A. Agrawal, X. Qian, V. Sharma, H. Zhuang, S. V. Kalinin, B. G.
Sumpter, G. Pilania, P. Acar, S. Mandal, K. Haule, D. Vanderbilt,
K. Rabe, and F. Tavazza, “The joint automated repository for various
integrated simulations (jarvis) for data-driven materials design,” npj
Computational Materials, vol. 6, no. 1, p. 173, November 2020.
[Online]. Available: https://doi.org/10.1038/s41524-020-00440-1
[623] J. J. Irwin, K. G. Tang, J. Young, C. Dandarchuluun, B. R.
Wong, M. Khurelbaatar, Y. S. Moroz, J. Mayfield, and R. A.
Sayle, “Zinc20—a free ultralarge-scale chemical database for ligand
discovery,” Journal of Chemical Information and Modeling, vol. 60,
no.
12,
pp.
6065–6073,
December
2020.
[Online].
Available:
https://doi.org/10.1021/acs.jcim.0c00675
[624] O. P. Pfeiffer, H. Liu, L. Montanelli, M. I. Latypov, F. G. Sen,
V. Hegadekatte, E. A. Olivetti, and E. R. Homer, “Aluminum
alloy compositions and properties extracted from a corpus of
scientific manuscripts and us patents,” Scientific Data, vol. 9, no. 1,
p. 128, March 2022. [Online]. Available: https://doi.org/10.1038/
s41597-022-01215-7
[625] V. Tshitoyan, J. Dagdelen, L. Weston, A. Dunn, Z. Rong et al., “Un-
supervised word embeddings capture latent knowledge from materials
science literature,” Nature, vol. 571, no. 7763, pp. 95–98, 2019.
[626] P. Eastman, P. K. Behara, D. L. Dotson, R. Galvelis, J. E. Herr, J. T.
Horton, Y. Mao, J. D. Chodera, B. P. Pritchard, Y. Wang et al., “Spice,
a dataset of drug-like molecules and peptides for training machine
learning potentials,” Scientific Data, vol. 10, no. 1, p. 11, 2023.
[627] Z. Zeng, Y. Yao, Z. Liu, and M. Sun, “A deep-learning system
bridging molecule structure and biomedical text with comprehension
comparable to human professionals,” Nature Communications, vol. 13,
no. 1, p. 862, 2022.
[628] S. Liu, W. Nie, C. Wang, J. Lu, Z. Qiao, L. Liu, J. Tang, C. Xiao,
and A. Anandkumar, “Multi-modal molecule structure–text model for
text-based retrieval and editing,” Nature Machine Intelligence, vol. 5,
no. 12, pp. 1447–1457, 2023.
[629] B. Su, D. Du, Z. Yang, Y. Zhou, J. Li, A. Rao, H. Sun, Z. Lu,
and J.-R. Wen, “A molecular multimodal foundation model as-
sociating molecule graphs with natural language,” arXiv preprint
arXiv:2209.05481, 2022.
[630] J. Li, Y. Lu, R. Akbani, Z. Ju, P. L. Roebuck, W. Liu, J.-Y. Yang,
J. N. Weinstein, I. Shmulevich, and G. B. Mills, “TCPA: a resource for
cancer functional proteomics data,” Nature Methods, vol. 10, no. 11,
pp. 1046–1047, 2013.
[631] B. E. Suzek, Y. Wang, H. Huang, P. B. McGarvey, C. H. Wu, and
U. Consortium, “Uniref clusters: a comprehensive and scalable alter-
native for improving sequence similarity searches,” Bioinformatics,
vol. 31, no. 6, pp. 926–932, 2015.
[632] Y. Ji, Z. Zhou, H. Liu, and R. V. Davuluri, “Dnabert: pre-trained
bidirectional encoder representations from transformers model for
dna-language in genome,” Bioinformatics, vol. 37, no. 15, pp. 2112–
2120, 2021.
[633] R. Consortium, “Rnacentral: a hub of information for non-coding rna
sequences,” Nucleic Acids Research, vol. 47, no. D1, pp. D221–D229,
2019.
[634] C. G. Cole, O. T. McCann, J. E. Collins, K. Oliver, D. Willey, S. M.
Gribble, F. Yang, K. McLaren, J. Rogers, Z. Ning et al., “Finishing the
finished human chromosome 22 sequence,” Genome Biology, vol. 9,
no. 5, p. R78, 2008.
[635] N. Siva, “1000 genomes project,” 2008.
[636] Z. Li, V. Subasri, Y. Shen, D. Li, Y. Zhao, G.-B. Stan, and C. Shan,
“Omni-dna: A unified genomic foundation model for cross-modal and
multi-task learning,” arXiv preprint arXiv:2502.03499, 2025.
[637] S. Dhanasekar, A. Saranathan, and P. Xie, “Genechat: A multi-modal
large language model for gene function prediction,” bioRxiv, pp.
2025–06, 2025.
[638] W. Liang, “Dnahlm–dna sequence and human language mixed large
language model,” arXiv preprint arXiv:2410.16917, 2024.
[639] F. Yang, W. Wang, F. Wang, Y. Fang, D. Tang, J. Huang, H. Lu,
and J. Yao, “scbert as a large-scale pretrained deep language model
for cell type annotation of single-cell rna-seq data,” Nature Machine
Intelligence, vol. 4, no. 10, pp. 852–866, 2022.
[640] Y. Shi, J. Yang, C. Nai, S. Li, J. Fang, X. Wang, Z. Liu, and
Y. Zhang, “Language-enhanced representation learning for single-cell
transcriptomics,” arXiv preprint arXiv:2503.09427, 2025.
[641] Y. Xiao, E. Sun, Y. Jin, and W. Wang, “Rna-gpt: Multimodal
generative system for rna sequence understanding,” arXiv preprint
arXiv:2411.08900, 2024.
[642] B. Chen, X. Cheng, P. Li, Y.-a. Geng, J. Gong, S. Li, Z. Bei, X. Tan,
B. Wang, X. Zeng et al., “xTrimoPGLM: unified 100b-scale pre-
trained transformer for deciphering the language of protein,” arXiv
preprint arXiv:2401.06199, 2024.
[643] Y. Shen, Z. Chen, M. Mamalakis, L. He, H. Xia, T. Li, Y. Su,
J. He, and Y. G. Wang, “A fine-tuning dataset and benchmark for
large language models for protein understanding,” in 2024 IEEE
International Conference on Bioinformatics and Biomedicine (BIBM).
IEEE, 2024, pp. 2390–2395.
[644] G. Stelzer, N. Rosen, I. Plaschkes, S. Zimmerman, M. Twik,
S. Fishilevich, T. I. Stein, R. Nudel, I. Lieder, Y. Mazor et al., “The
genecards suite: from gene data mining to disease genome sequence
analyses,” Current protocols in bioinformatics, vol. 54, no. 1, pp. 1–
30, 2016.
[645] J. S. Amberger, C. A. Bocchini, F. Schiettecatte, A. F. Scott, and
A. Hamosh, “Omim. org: Online mendelian inheritance in man
(omim®), an online catalog of human genes and genetic disorders,”
Nucleic acids research, vol. 43, no. D1, pp. D789–D798, 2015.
[646] P. W. Harrison, M. R. Amode, O. Austine-Orimoloye, A. G. Azov,
M. Barba, I. Barnes, A. Becker, R. Bennett, A. Berry, J. Bhai et al.,
“Ensembl 2024,” Nucleic acids research, vol. 52, no. D1, pp. D891–
D899, 2024.
[647] W.-B. Jiang, L.-M. Zhao, and B.-L. Lu, “Large brain model for
learning generic representations with tremendous eeg data in bci,”
arXiv preprint arXiv:2405.18765, 2024.
[648] Y. Li, Z. Li, K. Zhang, R. Dan, S. Jiang, and Y. Zhang, “Chatdoctor:
A medical chat model fine-tuned on a large language model meta-ai
(llama) using medical domain knowledge,” arXiv, abs/2303.14070,
2023. [Online]. Available: https://arxiv.org/abs/2303.14070
[649] A. B. Abacha, E. Agichtein, Y. Pinter, and D. Demner-Fushman,
“Overview of the medical question answering task at trec 2017
liveqa.” in TREC, 2017, pp. 1–12.
[650] S. Chen, Z. Ju, X. Dong, H. Fang, S. Wang, Y. Yang, J. Zeng,
R. Zhang, R. Zhang, M. Zhou et al., “Meddialog: a large-scale medical
dialogue dataset,” arXiv preprint arXiv:2004.03329, vol. 3, 2020.
[651] L. Luo, P.-T. Lai, C.-H. Wei, C. N. Arighi, and Z. Lu, “BioRED: a rich
biomedical relation extraction dataset,” Briefings in Bioinformatics,
vol. 23, no. 5, p. bbac282, 07 2022.
84

[652] L. Gao, S. Biderman, S. Black, L. Golding, T. Hoppe, C. Foster,
J. Phang, H. He, A. Thite, N. Nabeshima et al., “The pile: An
800gb dataset of diverse text for language modeling,” arXiv preprint
arXiv:2101.00027, 2020.
[653] S. Wang, M. B. McDermott, G. Chauhan, M. Ghassemi, M. C.
Hughes, and T. Naumann, “Mimic-extract: A data extraction, pre-
processing, and representation pipeline for mimic-iii,” in Proceedings
of the ACM conference on health, inference, and learning, 2020, pp.
222–235.
[654] S. Li, V. Balachandran, S. Feng, J. Ilgen, E. Pierson, P. W. W. Koh,
and Y. Tsvetkov, “Mediq: Question-asking llms and a benchmark for
reliable interactive clinical reasoning,” Advances in Neural Informa-
tion Processing Systems, vol. 37, pp. 28 858–28 888, 2024.
[655] J. W. Smith, J. E. Everhart, W. C. Dickson, W. C. Knowler, and R. S.
Johannes, “Using the adap learning algorithm to forecast the onset
of diabetes mellitus,” in Proceedings of the annual symposium on
computer application in medical care, 1988, p. 261.
[656] G. Zheng, X. Wang, J. Liang, N. Chen, Y. Zheng, and B. Wang, “Ef-
ficiently democratizing medical llms for 50 languages via a mixture
of language family experts,” arXiv preprint arXiv:2410.10626, 2024.
[657] P. Chambon, J.-B. Delbrouck, T. Sounack, S.-C. Huang, Z. Chen,
M. Varma, S. Q. Truong, C. T. Chuong, and C. P. Langlotz, “Chexpert
plus: Augmenting a large chest x-ray dataset with text radiology
reports, patient demographics and additional image formats,” arXiv
preprint arXiv:2405.19538, 2024.
[658] C. Wu, X. Zhang, Y. Zhang, Y. Wang, and W. Xie, “Towards generalist
foundation model for radiology by leveraging web-scale 2d & 3d
medical data,” arXiv preprint arXiv:2308.02463, 2023.
[659] J.-H. Huang, C.-H. H. Yang, F. Liu, M. Tian, Y.-C. Liu, T.-W. Wu,
I. Lin, K. Wang, H. Morikawa, H. Chang et al., “DeepOpht: medical
report generation for retinal images via deep models and visual
explanation,” in Proceedings of the IEEE/CVF winter conference on
applications of computer vision, 2021, pp. 2442–2452.
[660] F. Bai, Y. Du, T. Huang, M. Q. H. Meng, and B. Zhao, “M3d: Ad-
vancing 3d medical image analysis with multi-modal large language
models,” 2024.
[661] J. R¨uckert, L. Bloch, R. Br¨ungel, A. Idrissi-Yaghir, H. Sch¨afer, C. S.
Schmidt, S. Koitka, O. Pelka, A. B. Abacha, A. G. Seco de Herrera
et al., “ROCOv2: Radiology objects in context version 2, an updated
multimodal image dataset,” Scientific Data, vol. 11, no. 1, p. 688,
2024.
[662] S. Subramanian, L. L. Wang, S. Mehta, B. Bogin, M. Van Zuylen,
S. Parasa, S. Singh, M. Gardner, and H. Hajishirzi, “Medicat: A
dataset of medical images, captions, and textual references,” arXiv
preprint arXiv:2010.06000, 2020.
[663] R. Wu, N. Su, C. Zhang, T. Ma, T. Zhou, Z. Cui, N. Tang, T. Mao,
Y. Zhou, W. Fan et al., “MM-retinal v2: Transfer an elite knowl-
edge spark into fundus vision-language pretraining,” arXiv preprint
arXiv:2501.15798, 2025.
[664] R. Wang, J. Chen, K. Ji, Z. Cai, S. Chen, Y. Yang, and B. Wang,
“Medgen: Unlocking medical video generation by scaling granularly-
annotated medical videos,” arXiv preprint arXiv:2507.05675, 2025.
[665] M. Hu, K. Yuan, Y. Shen, F. Tang, X. Xu, L. Zhou, W. Li, Y. Chen,
Z. Xu, Z. Peng et al., “Ophclip: Hierarchical retrieval-augmented
learning for ophthalmic surgical video-language pretraining,” arXiv
preprint arXiv:2411.15421, 2024.
[666] B. Huang, H. Yuan, M. Xiang, Y. Huang, K. Xiao, S. Xu, R. Zhang,
L. Yang, Z. Niu, and H. Gu, “A comprehensive correction of the gaia
dr3 xp spectra,” The Astrophysical Journal Supplement Series, vol.
271, no. 1, p. 13, 2024.
[667] Astrophysics Data System, Harvard–Smithsonian CfA, “Nasa ads
developer api,” https://ui.adsabs.harvard.edu/help/api, 2025, program-
matic access to 15+ million astronomy & physics records.
[668] F. Grezes, S. Blanco-Cuaresma, A. Accomazzi, M. J. Kurtz, G. Sha-
purian, E. Henneken, C. S. Grant, D. M. Thompson, R. Chyla, S. Mc-
Donald et al., “Building astrobert, a language model for astronomy
& astrophysics,” arXiv preprint arXiv:2112.00590, 2021.
[669] X. Zhao, Y. Huang, G. Xue, X. Kong, J. Liu, X. Tang, T. C. Beers,
Y.-S. Ting, and A.-L. Luo, “Specclip: Aligning and translating spec-
troscopic measurements for stars,” arXiv preprint arXiv:2507.01939,
2025.
[670] M. J. Smith, R. J. Roberts, E. Angeloudi, and M. Huertas-Company,
“Astropt: Scaling large observation models for astronomy,” arXiv
preprint arXiv:2405.14930, 2024.
[671] W. Xu, X. Zhao, Y. Zhou, X. Yue, B. Fei, F. Ling, W. Zhang,
and L. Bai, “Earthse: A benchmark evaluating earth scientific
exploration capability for large language models,” arXiv preprint
arXiv:2505.17139, 2025.
[672] V. V. Manivannan, Y. Jafari, S. Eranky, S. Ho, R. Yu, D. Watson-
Parris, Y. Ma, L. Bergen, and T. Berg-Kirkpatrick, “Climaqa: An
automated evaluation framework for climate foundation models,”
arXiv preprint arXiv:2410.16701, 2024.
[673] A. E. W. Johnson, L. Bulgarelli, L. Shen, A. Gayles, A. Shammout,
S. Horng, T. J. Pollard, S. Hao, B. Moody, B. Gow, L.-w. H. Lehman,
L. A. Celi, and R. G. Mark, “MIMIC-IV, a freely accessible electronic
health record dataset,” Scientific Data, vol. 10, no. 1, 2023.
[674] M. Guevara, S. Chen, S. Thomas, T. L. Chaunzwa, I. Franco, B. H.
Kann, S. Moningi, J. M. Qian, M. Goldstein, S. Harper et al., “Large
language models to identify social determinants of health in electronic
health records,” NPJ digital medicine, vol. 7, no. 1, p. 6, 2024.
[675] T. Porian, M. Wortsman, J. Jitsev, L. Schmidt, and Y. Carmon,
“Resolving discrepancies in compute-optimal scaling of language
models,” in Advances in Neural Information Processing Systems,
A. Globerson, L. Mackey, D. Belgrave, A. Fan, U. Paquet, J. Tomczak,
and C. Zhang, Eds., vol. 37, 2024, pp. 100 535–100 570. [Online].
Available:
https://proceedings.neurips.cc/paper files/paper/2024/file/
b6341525cd84f3be0ef203e4d7cd8556-Paper-Conference.pdf
[676] S. M. Xie, H. Pham, X. Dong, N. Du, H. Liu, Y. Lu, P. Liang, Q. V.
Le, T. Ma, and A. W. Yu, “DoReMi: Optimizing data mixtures speeds
up language model pretraining,” in Thirty-seventh Conference on
Neural Information Processing Systems, 2023. [Online]. Available:
https://openreview.net/forum?id=lXuByUeHhd
[677] K. Lee, D. Ippolito, A. Nystrom, C. Zhang, D. Eck, C. Callison-
Burch, and N. Carlini, “Deduplicating training data makes language
models better,” arXiv preprint arXiv:2107.06499, 2021.
[678] H. Shi, Z. Xu, H. Wang, W. Qin, W. Wang, Y. Wang, Z. Wang,
S. Ebrahimi, and H. Wang, “Continual learning of large language
models: A comprehensive survey,” ACM Computing Surveys, 2025.
[Online]. Available: https://doi.org/10.1145/3735633
[679] Y. Guo, J. Fu, H. Zhang, D. Zhao, and Y. Shen, “Efficient con-
tinual pre-training by mitigating the stability gap,” arXiv preprint
arXiv:2406.14833, 2024.
[680] P. Tong, E. Brown, P. Wu, S. Woo, A. J. V. IYER, S. C. Akula,
S. Yang, J. Yang, M. Middepogu, Z. Wang et al., “Cambrian-1: A
fully open, vision-centric exploration of multimodal llms,” Advances
in Neural Information Processing Systems, vol. 37, pp. 87 310–87 356,
2024.
[681] Y. Bisk, R. Zellers, R. Le Bras, J. Gao, Y. Choi et al., “PIQA:
Reasoning about physical commonsense in natural language,” in
Proceedings of the AAAI conference on artificial intelligence, vol. 34,
no. 05, 2020, pp. 7432–7439.
[682] S. Dai, Y. Yan, J. Su, D. Zihao, Y. Gao, Y. Hei, J. Li, J. Zhang,
S. Tao, Z. Gao, and X. Hu, “PhysicsArena: The first multimodal
physics reasoning benchmark exploring variable, process, and solution
dimensions,” May 2025.
[683] H. Lightman, V. Kosaraju, Y. Burda, H. Edwards, B. Baker, T. Lee,
J. Leike, J. Schulman, I. Sutskever, and K. Cobbe, “Let’s verify step
by step,” arXiv preprint arXiv:2305.20050, 2023.
[684] D. Hendrycks, C. Burns, S. Kadavath, A. Arora, S. Basart, E. Tang,
D. Song, and J. Steinhardt, “Measuring mathematical problem solving
with the math dataset,” arXiv preprint arXiv:2103.03874, 2021.
[685] A. Bercovich, I. Levy, I. Golan, M. Dabbah, R. El-Yaniv, O. Puny,
I. Galil, Z. Moshe, T. Ronen, N. Nabwani et al., “Llama-nemotron:
Efficient reasoning models,” arXiv preprint arXiv:2505.00949, 2025.
[686] W.
Yuan,
J.
Yu,
S.
Jiang,
K.
Padthe,
Y.
Li,
I.
Kulikov,
K.
Cho,
D.
Wang,
Y.
Tian,
J.
E.
Weston,
and
X.
Li,
“Naturalreasoning: Reasoning in the wild with 2.8m challenging
questions,” ArXiv, vol. abs/2502.13124, 2025. [Online]. Available:
https://api.semanticscholar.org/CorpusID:276421963
[687] D. Lu, X. Tan, R. Xu, T. Yao, C. Qu, W. Chu, Y. Xu, and Y. Qi,
“Scp-116k: A high-quality problem-solution dataset and a generalized
pipeline for automated extraction in the higher education science
domain,” 2025.
[688] P. G. Francoeur, T. Masuda, J. Sunseri, A. Jia, R. B. Iovanisci,
I. Snyder, and D. R. Koes, “Three-dimensional convolutional neural
networks and a cross-docked data set for structure-based drug design,”
Journal of chemical information and modeling, vol. 60, no. 9, pp.
4200–4215, 2020.
[689] R. Wang, X. Fang, Y. Lu, and S. Wang, “The pdbbind database:
Collection of binding affinities for protein- ligand complexes with
known three-dimensional structures,” Journal of medicinal chemistry,
vol. 47, no. 12, pp. 2977–2980, 2004.
85

[690] B. Yu, F. N. Baker, Z. Chen, X. Ning, and H. Sun, “Llasmol: Ad-
vancing large language models for chemistry with a large-scale, com-
prehensive, high-quality instruction tuning dataset,” arXiv preprint
arXiv:2402.09391, 2024.
[691] D. Polykovskiy, A. Zhebrak, B. Sanchez-Lengeling, S. Golovanov,
O. Tatanov, S. Belyaev, R. Kurbanov, A. Artamonov, V. Aladinskiy,
M. Veselov, A. Kadurin, S. Johansson, H. Chen, S. Nikolenko,
A. Aspuru-Guzik, and A. Zhavoronkov, “Molecular Sets (MOSES): A
Benchmarking Platform for Molecular Generation Models,” Frontiers
in Pharmacology, 2020.
[692] C. Edwards, C. Zhai, and H. Ji, “Text2Mol: Cross-modal molecule
retrieval with natural language queries,” in Proceedings of the
2021 Conference on Empirical Methods in Natural Language
Processing, M.-F. Moens, X. Huang, L. Specia, and S. W.-t. Yih,
Eds.
Online and Punta Cana, Dominican Republic: Association
for Computational Linguistics, Nov. 2021, pp. 595–607. [Online].
Available: https://aclanthology.org/2021.emnlp-main.47/
[693] P. Liu, J. Tao, and Z. Ren, “A quantitative analysis of knowledge-
learning preferences in large language models in molecular science,”
2025. [Online]. Available: https://arxiv.org/abs/2402.04119
[694] J. M. Ede, “Warwick electron microscopy datasets,” Machine
Learning: Science and Technology, vol. 1, no. 4, p. 045003, Sep. 2020.
[Online]. Available: http://dx.doi.org/10.1088/2632-2153/ab9c3c
[695] M. Xu, Z. Zhang, J. Lu, Z. Zhu, Y. Zhang, M. Chang, R. Liu, and
J. Tang, “Peer: a comprehensive and multi-task benchmark for protein
sequence understanding,” Advances in Neural Information Processing
Systems, vol. 35, pp. 35 156–35 173, 2022.
[696] Y. Ren, Z. Chen, L. Qiao, H. Jing, Y. Cai, S. Xu, P. Ye, X. Ma, S. Sun,
H. Yan, D. Yuan, W. Ouyang, and X. Liu, “Beacon: Benchmark for
comprehensive rna tasks and language models,” Advances in Neural
Information Processing Systems, vol. 37, pp. 92 891–92 921, 2024.
[697] Y. Fang, X. Liang, N. Zhang, K. Liu, R. Huang, Z. Chen, X. Fan, and
H. Chen, “Mol-instructions: A large-scale biomolecular instruction
dataset for large language models,” arXiv preprint arXiv:2306.08018,
2023.
[698] H. Xiao, W. Lin, H. Wang, Z. Liu, and Q. Ye, “OPI: An open
instruction dataset for adapting large language models to protein-
related tasks,” in Neurips 2024 Workshop Foundation Models for
Science: Progress, Opportunities, and Challenges, 2024. [Online].
Available: https://openreview.net/forum?id=I4bA7ekJGh
[699] M.
Jin,
H.
Xue,
Z.
Wang,
B.
Kang,
R.
Ye,
K.
Zhou,
M.
Du,
and
Y.
Zhang,
“ProLLM:
Protein
chain-of-thoughts
enhanced LLM for protein-protein interaction prediction,” in First
Conference on Language Modeling, 2024. [Online]. Available:
https://openreview.net/forum?id=2nTzomzjjb
[700] M. Wesney, “Tot-biology,” https://huggingface.co/datasets/moremilk/
ToT-Biology, 2025, version v1.0.0; MIT License; accessed 2025-08-
17.
[701] H. He, Y. Ren, Y. Tang, Z. Xu, J. Li, M. Yang, D. Zhang, D. Yuan,
T. Chen, S. Zhang et al., “Biology instructions: A dataset and
benchmark for multi-omics sequence understanding capability of large
language models,” arXiv preprint arXiv:2412.19191, 2024.
[702] X. He, S. Chen, Z. Ju, X. Dong, H. Fang, S. Wang, Y. Yang, J. Zeng,
R. Zhang, R. Zhang, M. Zhou, P. Zhu, and P. Xie, “Meddialog: Two
large-scale medical dialogue datasets,” arXiv, abs/2004.03329, 2020.
[Online]. Available: https://arxiv.org/abs/2004.03329
[703] J. Wang, Z. Yao, Z. Yang, H. Zhou, R. Li, X. Wang, Y. Xu, and
H. Yu, “Notechat: a dataset of synthetic doctor-patient conversations
conditioned on clinical notes,” arXiv preprint arXiv:2310.15959,
2023.
[704] S. Bae, D. Kyung, J. Ryu, E. Cho, G. Lee, S. Kweon, J. Oh,
L. Ji, E. Chang, T. Kim et al., “EHRXQA: A multi-modal question
answering dataset for electronic health records with chest x-ray
images,” Advances in Neural Information Processing Systems, vol. 36,
pp. 3867–3880, 2023.
[705] J. J. Lau, S. Gayen, A. Ben Abacha, and D. Demner-Fushman, “A
dataset of clinically generated visual questions and answers about
radiology images,” Scientific Data, vol. 5, no. 1, pp. 1–10, 2018.
[706] T. Grootswagers, I. Zhou, A. K. Robinson, M. N. Hebart, and T. A.
Carlson, “Human eeg recordings for 1,854 concepts presented in rapid
serial visual presentation streams,” Scientific Data, vol. 9, no. 1, p. 3,
2022.
[707] A. T. Gifford, K. Dwivedi, G. Roig, and R. M. Cichy, “A large
and rich eeg dataset for modeling human visual object recognition,”
NeuroImage, vol. 264, p. 119754, 2022.
[708] E. J. Allen, G. St-Yves, Y. Wu, J. L. Breedlove, J. S. Prince,
L. T. Dowdle, M. Nau, B. Caron, F. Pestilli, I. Charest et al., “A
massive 7t fmri dataset to bridge cognitive neuroscience and artificial
intelligence,” Nature neuroscience, vol. 25, no. 1, pp. 116–126, 2022.
[709] M. N. Hebart, O. Contier, L. Teichmann, A. H. Rockter, C. Y.
Zheng, A. Kidder, A. Corriveau, M. Vaziri-Pashkam, and C. I. Baker,
“Things-data, a multimodal collection of large-scale datasets for
investigating object representations in human brain and behavior,”
Elife, vol. 12, p. e82580, 2023.
[710] R. Kneeland, P. S. Scotti, G. St-Yves, J. Breedlove, K. Kay, and
T. Naselaris, “Nsd-imagery: A benchmark dataset for extending fmri
vision decoding methods to mental imagery,” in Proceedings of the
Computer Vision and Pattern Recognition Conference, 2025, pp.
28 852–28 862.
[711] Z. Guo, J. Wu, Y. Song, J. Bu, W. Mai, Q. Zheng, W. Ouyang, and
C. Song, “Neuro-3d: Towards 3d visual decoding from eeg signals,”
in Proceedings of the Computer Vision and Pattern Recognition
Conference, 2025, pp. 23 870–23 880.
[712] N. Hollenstein, J. Rotsztejn, M. Troendle, A. Pedroni, C. Zhang, and
N. Langer, “Zuco, a simultaneous eeg and eye-tracking resource for
natural sentence reading,” Scientific data, vol. 5, no. 1, pp. 1–13, 2018.
[713] N. Hollenstein, M. Troendle, C. Zhang, and N. Langer, “Zuco 2.0:
A dataset of physiological recordings during natural reading and
annotation,” arXiv preprint arXiv:1912.00903, 2019.
[714] D. Alvarez-Estevez and R. M. Rijsman, “Inter-database validation of a
deep learning approach for automatic sleep scoring,” PloS one, vol. 16,
no. 8, p. e0256111, 2021.
[715] K. A. I. Aboalayon, M. Faezipour, W. S. Almuhammadi, and
S. Moslehpour, “Sleep stage classification using eeg signal analysis: a
comprehensive survey and new investigation,” Entropy, vol. 18, no. 9,
p. 272, 2016.
[716] S. F. Quan, B. V. Howard, C. Iber, J. P. Kiley, F. J. Nieto, G. T.
O’Connor, D. M. Rapoport, S. Redline, J. Robbins, J. M. Samet et al.,
“The sleep heart health study: design, rationale, and methods,” Sleep,
vol. 20, no. 12, pp. 1077–1085, 1997.
[717] A. Harati, M. Golmohammadi, S. Lopez, I. Obeid, and J. Picone,
“Improved eeg event classification using differential energy,” in 2015
IEEE Signal Processing in Medicine and Biology Symposium (SPMB).
IEEE, 2015, pp. 1–4.
[718] E. von Weltin, T. Ahsan, V. Shah, D. Jamshed, M. Golmohammadi,
I. Obeid, and J. Picone, “Electroencephalographic slowing: A primary
source of error in automatic seizure detection,” in 2017 IEEE signal
processing in medicine and biology symposium (SPMB). IEEE, 2017,
pp. 1–5.
[719] J. Ma, B. Yang, W. Qiu, Y. Li, S. Gao, and X. Xia, “A large eeg
dataset for studying cross-session variability in motor imagery brain-
computer interface,” Scientific Data, vol. 9, no. 1, p. 531, 2022.
[720] W.-L. Zheng and B.-L. Lu, “Investigating critical frequency bands
and channels for eeg-based emotion recognition with deep neural
networks,” IEEE Transactions on autonomous mental development,
vol. 7, no. 3, pp. 162–175, 2015.
[721] W.-L. Zheng, W. Liu, Y. Lu, B.-L. Lu, and A. Cichocki, “Emotion-
meter: A multimodal framework for recognizing human emotions,”
IEEE transactions on cybernetics, vol. 49, no. 3, pp. 1110–1122, 2018.
[722] I. Zyma, S. Tukaev, I. Seleznov, K. Kiyono, A. Popov, M. Chernykh,
and O. Shpenkov, “Electroencephalograms during mental arithmetic
task performance,” Data, vol. 4, no. 1, p. 14, 2019.
[723] H. Zhang, J. Sun, R. Chen, W. Liu, Z. Yuan, X. Zheng, Z. Wang,
Z. Yang, H. Yan, H. Zhong et al., “Empowering and assessing the
utility of large language models in crop science,” Advances in Neural
Information Processing Systems, vol. 37, pp. 52 670–52 722, 2024.
[724] E. Perkowski, R. Pan, T. D. Nguyen, Y.-S. Ting, S. Kruk, T. Zhang,
C. O’Neill, M. Jablonska, Z. Sun, M. J. Smith et al., “Astrollama-chat:
Scaling astrollama with conversational and diverse datasets,” Research
Notes of the AAS, vol. 8, no. 1, p. 7, 2024.
[725] R. Pan, T. D. Nguyen, H. Arora, A. Accomazzi, T. Ghosal, and Y.-
S. Ting, “Astromlab 2: Astrollama-2-70b model and benchmarking
specialised llms for astronomy,” in SC24-W: Workshops of the Inter-
national Conference for High Performance Computing, Networking,
Storage and Analysis.
IEEE, 2024, pp. 87–96.
[726] J. Evans, S. Sadruddin, and J. D’Souza, “Astro-ner–astronomy named
entity recognition: Is gpt a good domain expert annotator?” arXiv
preprint arXiv:2405.02602, 2024.
[727] M. Rahnemoonfar, T. Chowdhury, A. Sarkar, D. Varshney, M. Yari,
and R. R. Murphy, “Floodnet: A high resolution aerial imagery dataset
for post flood scene understanding,” IEEE Access, vol. 9, pp. 89 644–
89 654, 2021.
[728] J. Wang, Z. Zheng, Z. Chen, A. Ma, and Y. Zhong, “Earthvqa: To-
wards queryable earth via relational reasoning-based remote sensing
86

visual question answering,” in Proceedings of the AAAI conference
on artificial intelligence, vol. 38, no. 6, 2024, pp. 5481–5489.
[729] C. Ma, Z. Hua, A. Anderson-Frey, V. Iyer, X. Liu, and L. Qin,
“Weatherqa: Can multimodal language models reason about severe
weather?” arXiv preprint arXiv:2406.11217, 2024.
[730] K. X. Nguyen, F. Qiao, A. Trembanis, and X. Peng, “Seafloorai: a
large-scale vision-language dataset for seafloor geological survey,”
Advances in Neural Information Processing Systems, vol. 37, pp.
22 107–22 123, 2024.
[731] Z. Zhang, T. Zhao, Y. Guo, and J. Yin, “Rs5m and georsclip: A
large scale vision-language dataset and a large vision-language model
for remote sensing,” IEEE Transactions on Geoscience and Remote
Sensing, 2024.
[732] Z. Wang, R. Prabha, T. Huang, J. Wu, and R. Rajagopal, “Skyscript:
A large and semantically diverse vision-language dataset for remote
sensing,” in Proceedings of the AAAI Conference on Artificial Intel-
ligence, vol. 38, no. 6, 2024, pp. 5805–5813.
[733] J. Wu, W. Deng, X. Li, S. Liu, T. Mi, Y. Peng, Z. Xu, Y. Liu,
H. Cho, C.-I. Choi, Y. Cao, H. Ren, X. Li, X. Li, and Y. Zhou,
“MedReason: Eliciting factual medical reasoning steps in LLMs via
knowledge graphs,” arXiv preprint arXiv:2504.00993, 2025.
[734] Y. Sun, X. Qian, W. Xu, H. Zhang, C. Xiao, L. Li, Y. Rong, W. Huang,
Q. Bai, and T. Xu, “ReasonMed: A 370k multi-agent generated dataset
for advancing medical reasoning,” arXiv preprint arXiv:2506.09513,
2025.
[735] C. Qin, X. Chen, C. Wang, P. Wu, X. Chen, Y. Cheng, J. Zhao,
M. Xiao, X. Dong, Q. Long et al., “Scihorizon: Benchmarking ai-
for-science readiness from scientific data to large language models,”
arXiv preprint arXiv:2503.13503, 2025.
[736] A. Anand, J. Kapuriya, A. Singh, J. Saraf, N. Lal, A. Verma, R. Gupta,
and R. Shah, “MM-PhyQA: Multimodal physics question-answering
with multi-image cot prompting,” in Advances in Knowledge Discov-
ery and Data Mining, D.-N. Yang, X. Xie, V. S. Tseng, J. Pei, J.-W.
Huang, and J. C.-W. Lin, Eds.
Singapore: Springer Nature, 2024,
pp. 53–64.
[737] C. He, R. Luo, Y. Bai, S. Hu, Z. L. Thai, J. Shen, J. Hu, X. Han,
Y. Huang, Y. Zhang, J. Liu, L. Qi, Z. Liu, and M. Sun, “Olympiad-
bench: A challenging benchmark for promoting agi with olympiad-
level bilingual multimodal scientific problems,” Jun. 2024.
[738] S. Aroca-Ouellette, C. Paik, A. Roncone, and K. Kann, “PROST:
Physical reasoning of objects through space and time,” Jun. 2021.
[739] L. Wang, E. Su, J. Liu, P. Li, P. Xia, J. Xiao, W. Zhang, X. Dai,
X. Chen, Y. Meng, M. Ding, L. Bai, W. Ouyang, S. Tang, A. Wang,
and X. Ma, “PhysUniBench: An undergraduate-level physics reason-
ing benchmark for multimodal models,” Jun. 2025.
[740] X. Zhang, Y. Dong, Y. Wu, J. Huang, C. Jia, B. Fernando, M. Z. Shou,
L. Zhang, and J. Liu, “PhysReason: A comprehensive benchmark
towards physics-based reasoning,” May 2025.
[741] X. Xu, Q. Xu, T. Xiao, T. Chen, Y. Yan, J. Zhang, S. Diao,
C. Yang, and Y. Wang, “UGPhysics: A comprehensive benchmark for
undergraduate physics reasoning with large language models,” arXiv
preprint arXiv:2502.00334, 2025.
[742] H. Shen, T. Wu, Q. Han, Y. Hsieh, J. Wang, Y. Zhang, Y. Cheng,
Z. Hao, Y. Ni, X. Wang et al., “PhyX: Does your model have
the” wits” for physical reasoning?” arXiv preprint arXiv:2505.15929,
2025.
[743] K. Feng, Y. Zhao, Y. Liu, T. Yang, C. Zhao, J. Sous, and A. Cohan,
“PHYSICS: Benchmarking foundation models on university-level
physics problem solving,” arXiv preprint arXiv:2503.21821, 2025.
[744] K. Xiang, H. Li, T. J. Zhang, Y. Huang, Z. Liu, P. Qu, J. He, J. Chen,
Y.-J. Yuan, J. Han, H. Xu, H. Li, M. Sachan, and X. Liang, “Seephys:
Does seeing help thinking? – benchmarking vision-based physics
reasoning,” Jun. 2025.
[745] D. J. Chung, Z. Gao, Y. Kvasiuk, T. Li, M. M¨unchmeyer, M. Rudolph,
F. Sala, and S. C. Tadepalli, “Theoretical physics benchmark
(TPBench)-a dataset and study of ai reasoning capabilities in the-
oretical physics,” Machine Learning: Science and Technology, 2025.
[746] S. Qiu, S. Guo, Z.-Y. Song, Y. Sun, Z. Cai, J. Wei, T. Luo, Y. Yin,
H. Zhang, Y. Hu, C. Wang, C. Tang, H. Chang, Q. Liu, Z. Zhou,
T. Zhang, J. Zhang, Z. Liu, M. Li, Y. Zhang, B. Jing, X. Yin, Y. Ren,
Z. Fu, J. Ji, W. Wang, X. Tian, A. Lv, L. Man, J. Li, F. Tao, Q. Sun,
Z. Liang, Y. Mu, Z. Li, J.-J. Zhang, S. Zhang, X. Li, X. Xia, J. Lin,
Z. Shen, J. Chen, Q. Xiong, B. Wang, F. Wang, Z. Ni, B. Zhang,
F. Cui, C. Shao, Q.-H. Cao, M.-x. Luo, Y. Yang, M. Zhang, and
H. X. Zhu, “PHYBench: Holistic evaluation of physical perception
and reasoning in large language models,” May 2025.
[747] W. La Cava, P. Orzechowski, B. Burlacu, F. O. de Franc¸a, M. Virgolin,
Y. Jin, M. Kommenda, and J. H. Moore, “Contemporary symbolic
regression methods and their relative performance,” Jul. 2021.
[748] P. Shojaee, N.-H. Nguyen, K. Meidani, A. B. Farimani, K. D. Doan,
and C. K. Reddy, “Llm-srbench: A new benchmark for scientific
equation discovery with large language models,” Jun. 2025.
[749] F. Bordes, Q. Garrido, J. T. Kao, A. Williams, M. Rabbat, and
E. Dupoux, “Intphys 2: Benchmarking intuitive physics understanding
in complex synthetic environments,” Jun. 2025.
[750] B. Krojer, M. Komeili, C. Ross, Q. Garrido, K. Sinha, N. Ballas,
and M. Assran, “A shortcut-aware video-qa benchmark for physical
understanding via minimal video pairs,” Jun. 2025.
[751] K. Li, Y. Wang, Y. He, Y. Li, Y. Wang, Y. Liu, Z. Wang, J. Xu,
G. Chen, P. Luo, L. Wang, and Y. Qiao, “MVBench: A comprehensive
multi-modal video understanding benchmark,” May 2024.
[752] Y. Huang, R. Zhang, X. He, X. Zhi, H. Wang, X. Li, F. Xu,
D. Liu, H. Liang, Y. Li et al., “Chemeval: a comprehensive multi-
level chemical evaluation for large language models,” arXiv preprint
arXiv:2409.13989, 2024.
[753] H. Zhao, X. Tang, Z. Yang, X. Han, X. Feng, Y. Fan, S. Cheng,
D. Jin, Y. Zhao, A. Cohan et al., “Chemsafetybench: benchmarking
llm safety on chemistry domain,” arXiv preprint arXiv:2411.16736,
2024.
[754] J. Chen, Y. Hu, Y. Wang, Y. Lu, X. Cao, M. Lin, H. Xu, J. Wu,
C. Xiao, J. Sun et al., “Trialbench: Multi-modal artificial intelligence-
ready clinical trial datasets,” Nature Scientific Data, 2024.
[755] J. Xie, W. Wang, B. Gao, Z. Yang, H. Wan, S. Zhang, T. Fu,
and Y. Li, “Qcbench: Evaluating large language models on domain-
specific quantitative chemistry,” arXiv preprint arXiv:2508.01670,
2025.
[756] Z. Yang, J. Xie, S. Shen, D. Wang, Y. Chen, B. Gao, S. Sun, B. Qi,
D. Zhou, L. Bai, L. Chen, S. Zhang, J. Jiang, T. Fu, and Y. Li,
“Spectrumworld: Artificial intelligence foundation for spectroscopy,”
arXiv preprint, 2025.
[757] A. N. Rubungo, K. Li, J. Hattrick-Simpers, and A. B. Dieng,
“Llm4mat-bench: Benchmarking large language models for materials
property prediction,” 2024. [Online]. Available: https://arxiv.org/abs/
2411.00177
[758] V. Mishra, S. Singh, M. Zaki, H. S. Grover, S. Miret, M. ., and
N. M. A. Krishnan, “LLamat: Large language models for materials
science,” in AI for Accelerated Materials Design - Vienna 2024, 2024.
[Online]. Available: https://openreview.net/forum?id=ZUkmRy6SqS
[759] N. Brown, M. Fiscato, M. H. Segler, and A. C. Vaucher, “Guacamol:
Benchmarking models for de novo molecular design,” Journal of
Chemical Information and Modeling, vol. 59, no. 3, pp. 1096–1108,
2019. [Online]. Available: https://doi.org/10.1021/acs.jcim.8b00839
[760] J. Zhou and O. G. Troyanskaya, “Predicting effects of noncoding
variants with deep learning–based sequence model,” Nature methods,
vol. 12, no. 10, pp. 931–934, 2015.
[761] K. L. Howe, P. Achuthan, J. Allen, J. Allen, J. Alvarez-Jarreta, M. R.
Amode, I. M. Armean, A. G. Azov, R. Bennett, J. Bhai et al.,
“Ensembl 2021,” Nucleic acids research, vol. 49, no. D1, pp. D884–
D891, 2021.
[762] E. Trop, Y. Schiff, E. M. Marroquin, C. H. Kao, A. Gokaslan,
M.
Polen,
M.
Shao,
B.
P.
de
Almeida,
T.
Pierrot,
Y.
I.
Li,
and
V.
Kuleshov,
“The
genomics
long-range
benchmark:
Advancing DNA language models,” 2024. [Online]. Available:
https://openreview.net/forum?id=Cdc90HKs1I
[763] J. Li, J. Li, Y. Liu, D. Zhou, and Q. Li, “Tomg-bench: Evaluat-
ing llms on text-based open molecule generation,” arXiv preprint
arXiv:2412.14642, 2024.
[764] X. Lu, H. Cao, Z. Liu, S. Bai, L. Chen, Y. Yao, H.-T. Zheng, and Y. Li,
“Moleculeqa: A dataset to evaluate factual accuracy in molecular
comprehension,” arXiv preprint arXiv:2403.08192, 2024.
[765] J. M. Laurent, J. D. Janizek, M. Ruzo, M. M. Hinks, M. J. Hammer-
ling, S. Narayanan, M. Ponnapati, A. D. White, and S. G. Rodriques,
“Lab-bench: Measuring capabilities of language models for biology
research,” arXiv preprint arXiv:2407.10362, 2024.
[766] W. Hou and Z. Ji, “Geneturing tests gpt models in genomics,” BioRxiv,
pp. 2023–03, 2023.
[767] M. Yin, Y. Qu, D. Liu, L. Yang, L. Cong, and M. Wang, “Genome-
bench: A scientific reasoning benchmark from real-world expert
discussions,” bioRxiv, pp. 2025–06, 2025.
[768] Y. Hasson, P. Luc, L. Momeni, M. Ovsjanikov, G. L. Moing,
A. Kuznetsova, I. Ktena, J. J. Sun, S. Koppula, D. Gokay et al.,
“Scivid: Cross-domain evaluation of video models in scientific appli-
cations,” arXiv preprint arXiv:2507.03578, 2025.
87

[769] A. Krithara, A. Nentidis, K. Bougiatiotis, and G. Paliouras, “Bioasq-
qa: A manually curated corpus for biomedical question answering,”
Scientific Data, vol. 10, no. 1, p. 170, 2023.
[770] M. Liu, J. Ding, J. Xu, W. Hu, X. Li, L. Zhu, Z. Bai, X. Shi, B. Wang,
H. Song, P. Liu, X. Zhang, S. Wang, K. Li, H. Wang, T. Ruan,
X. Huang, X. Sun, and S. Zhang, “Medbench: A comprehensive,
standardized, and reliable benchmarking system for evaluating
chinese medical large language models,” arXiv, abs/2407.10990,
2024. [Online]. Available: https://arxiv.org/abs/2407.10990
[771] Y. Zuo, S. Qu, Y. Li, Z. Chen, X. Zhu, E. Hua, K. Zhang, N. Ding,
and B. Zhou, “MedXpertQA: Benchmarking Expert-Level Medical
Reasoning and Understanding,” Jun. 2025.
[772] R. K. Arora, J. Wei, R. S. Hicks, P. Bowman, J. Qui˜nonero-Candela,
F. Tsimpourlas, M. Sharman, M. Shah, A. Vallone, A. Beutel et al.,
“Healthbench: Evaluating large language models towards improved
human health,” arXiv preprint arXiv:2505.08775, 2025.
[773] B. Liu, L.-M. Zhan, L. Xu, L. Ma, Y. Yang, and X.-M. Wu, “Slake: A
semantically-labeled knowledge-enhanced dataset for medical visual
question answering,” in 2021 IEEE 18th international symposium on
biomedical imaging (ISBI).
IEEE, 2021, pp. 1650–1654.
[774] Q. Zheng, W. Zhao, C. Wu, X. Zhang, L. Dai, H. Guan, Y. Li,
Y. Zhang, Y. Wang, and W. Xie, “Large-scale long-tailed disease
diagnosis on radiology images,” Nature Communications, vol. 15,
no. 1, p. 10147, 2024.
[775] X. Chen, X. Mao, Q. Guo, L. Wang, S. Zhang, and T. Chen,
“RareBench: can LLMs serve as rare diseases specialists?” in Pro-
ceedings of the 30th ACM SIGKDD conference on knowledge discov-
ery and data mining, 2024, pp. 4850–4861.
[776] Y. Jiang, K. C. Black, G. Geng, D. Park, J. Zou, A. Y. Ng, and
J. H. Chen, “MedAgentBench: a virtual ehr environment to benchmark
medical llm agents,” NEJM AI, p. AIdbp2500144, 2025.
[777] S. Schmidgall, R. Ziaei, C. Harris, E. Reis, J. Jopling, and M. Moor,
“Agentclinic: a multimodal agent benchmark to evaluate ai in simu-
lated clinical environments,” arXiv preprint arXiv:2405.07960, 2024.
[778] J. Ying, Z. Chen, Z. Wang, W. Jiang, C. Wang, Z. Yuan, H. Su,
H. Kong, F. Yang, and N. Dong, “SeedBench: A multi-task benchmark
for evaluating large language models in seed science,” in Proceedings
of the 63rd Annual Meeting of the Association for Computational
Linguistics
(Volume
1:
Long
Papers),
W.
Che,
J.
Nabende,
E. Shutova, and M. T. Pilehvar, Eds.
Vienna, Austria: Association
for Computational Linguistics, Jul. 2025, pp. 31 395–31 449. [Online].
Available: https://aclanthology.org/2025.acl-long.1516/
[779] Y.-S. Ting, T. D. Nguyen, T. Ghosal, R. Pan, H. Arora, Z. Sun,
T. de Haan, N. Ramachandra, A. Wells, S. Madireddy et al., “Astrom-
lab 1: Who wins astronomy jeopardy!?” Astronomy and Computing,
vol. 51, p. 100893, 2025.
[780] J. Li, F. Zhao, P. Chen, J. Xie, X. Zhang, H. Li, M. Chen, Y. Wang, and
M. Zhu, “An astronomical question answering dataset for evaluating
large language models,” Scientific Data, vol. 12, no. 1, p. 447, 2025.
[781] F. Zhao, Y. Li, Y. Wang, H. Li, M. Chen, P. Chen, N. Sun, C. Wang,
and J. Liu, “Pulsar candidate classification with multimodal large
language models,” in Neurips 2024 Workshop Foundation Models for
Science: Progress, Opportunities, and Challenges, 2024. [Online].
Available: https://openreview.net/forum?id=8SKgWpZiDL
[782] S. Mishra-Sharma, Y. Song, and J. Thaler, “Paperclip: Associating
astronomical observations and natural language with multi-modal
models,” arXiv preprint arXiv:2403.08851, 2024.
[783] K. G. Iyer, M. Yunus, C. O’Neill, C. Ye, A. Hyk, K. Mccormick,
I. Ciuc˘a, J. F. Wu, A. Accomazzi, S. Astarita et al., “pathfinder: A
semantic framework for literature review and knowledge discovery in
astronomy,” The Astrophysical Journal Supplement Series, vol. 275,
no. 2, p. 38, 2024.
[784] N. Webersinke, M. Kraus, J. A. Bingler, and M. Leippold, “Climate-
bert: A pretrained language model for climate-related text,” arXiv
preprint arXiv:2110.12010, 2021.
[785] Y. Hu, J. Yuan, C. Wen, X. Lu, Y. Liu, and X. Li, “Rsgpt: A remote
sensing vision language model and benchmark,” ISPRS Journal of
Photogrammetry and Remote Sensing, vol. 224, pp. 272–286, 2025.
[786] F. Wang, H. Wang, Z. Guo, D. Wang, Y. Wang, M. Chen, Q. Ma,
L. Lan, W. Yang, J. Zhang et al., “Xlrs-bench: Could your multi-
modal llms understand extremely large ultra-high-resolution remote
sensing imagery?” in Proceedings of the Computer Vision and Pattern
Recognition Conference, 2025, pp. 14 325–14 336.
[787] F. Wang, M. Chen, X. He, Y. Zhang, F. Liu, Z. Guo, Z. Hu, J. Wang,
J. Xu, Z. Li et al., “Omniearth-bench: Towards holistic evaluation
of earth’s six spheres and cross-spheres interactions with multimodal
observational earth data,” arXiv preprint arXiv:2505.23522, 2025.
[788] Y. Huang, Y. Bai, Z. Zhu, J. Zhang, J. Zhang, T. Su, J. Liu, C. Lv,
Y. Zhang, J. Lei, Y. Fu, M. Sun, and J. He, “C-eval: A multi-level
multi-discipline chinese evaluation suite for foundation models,” Nov.
2023.
[789] W. Zhong, R. Cui, Y. Guo, Y. Liang, S. Lu, Y. Wang, A. Saied,
W. Chen, and N. Duan, “Agieval: A human-centric benchmark for
evaluating foundation models,” arXiv preprint arXiv:2304.06364,
2023.
[790] X. Yue, Y. Ni, K. Zhang, T. Zheng, R. Liu, G. Zhang, S. Stevens,
D. Jiang, W. Ren, Y. Sun, C. Wei, B. Yu, R. Yuan, R. Sun, M. Yin,
B. Zheng, Z. Yang, Y. Liu, W. Huang, H. Sun, Y. Su, and W. Chen,
“Mmmu: A massive multi-discipline multimodal understanding and
reasoning benchmark for expert agi,” Jun. 2024.
[791] X. Yue, T. Zheng, Y. Ni, Y. Wang, K. Zhang, S. Tong, Y. Sun,
B. Yu, G. Zhang, H. Sun, Y. Su, W. Chen, and G. Neubig, “MMMU-
Pro: A More Robust Multi-discipline Multimodal Understanding
Benchmark,” May 2025.
[792] X. Du, Y. Yao, K. Ma, B. Wang, T. Zheng, K. Zhu, M. Liu, Y. Liang,
X. Jin, Z. Wei et al., “Supergpqa: Scaling llm evaluation across 285
graduate disciplines,” arXiv preprint arXiv:2502.14739, 2025.
[793] L. Sun, Y. Han, Z. Zhao, D. Ma, Z. Shen, B. Chen, L. Chen,
and K. Yu, “Scieval: A multi-level large language model evaluation
benchmark for scientific research,” arXiv preprint arXiv:2308.13149,
2023.
[794] A. Anand, J. Kapuriya, A. Singh, J. Saraf, N. Lal, A. Verma, R. Gupta,
and R. Shah, “Mm-phyqa: Multimodal physics question-answering
with multi-image cot prompting,” in Pacific-Asia Conference on
Knowledge Discovery and Data Mining.
Springer, 2024, pp. 53–
64.
[795] S. Lobry, D. Marcos, J. Murray, and D. Tuia, “Rsvqa: Visual question
answering for remote sensing data,” IEEE Transactions on Geoscience
and Remote Sensing, vol. 58, no. 12, pp. 8555–8566, 2020.
[796] X. Hu, L. Gu, Q. An, M. Zhang, L. Liu, K. Kobayashi, T. Harada,
R. M. Summers, and Y. Zhu, “Expert knowledge-aware image
difference graph representation learning for difference-aware medical
visual question answering,” in Proceedings of the 29th ACM SIGKDD
Conference on Knowledge Discovery and Data Mining.
Association
for Computing Machinery, 2023, p. 4156–4165. [Online]. Available:
https://doi.org/10.1145/3580305.3599819
[797] Y. Hu, T. Li, Q. Lu, W. Shao, J. He, Y. Qiao, and P. Luo, “OmniMed-
VQA: A New Large-Scale Comprehensive Evaluation Benchmark for
Medical LVLM,” arXiv preprint arXiv:2402.09181, 2024.
[798] X. Li, J. Ding, and M. Elhoseiny, “Vrsbench: A versatile vision-
language benchmark dataset for remote sensing image understanding,”
Advances in Neural Information Processing Systems, vol. 37, pp.
3229–3242, 2024.
[799] M. Savery, A. B. Abacha, S. Gayen, and D. Demner-Fushman,
“Question-driven summarization of answers to consumer health ques-
tions,” Scientific Data, vol. 7, no. 1, p. 322, 2020.
[800] B. S. Bloom, M. D. Engelhart, E. J. Furst, W. H. Hill, D. R. Krathwohl
et al., Taxonomy of educational objectives: The classification of
educational goals. Handbook 1: Cognitive domain.
Longman New
York, 1956.
[801] T. Zhang*, V. Kishore*, F. Wu*, K. Q. Weinberger, and Y. Artzi,
“BERTScore: Evaluating text generation with bert,” in International
Conference on Learning Representations, 2020. [Online]. Available:
https://openreview.net/forum?id=SkeHuCVFDr
[802] W. Yan, H. Liu, T. Wu, Q. Chen, W. Wang, H. Chai, J. Wang, W. Zhao,
Y. Zhang, R. Zhang et al., “Clinicallab: Aligning agents for multi-
departmental clinical diagnostics in the real world,” arXiv preprint
arXiv:2406.13890, 2024.
[803] S. Pletscher-Frankild, A. Pallej`a, K. Tsafou, J. X. Binder, and L. J.
Jensen, “Diseases: Text mining and data integration of disease–gene
associations,” Methods, vol. 74, pp. 83–89, 2015.
[804] A. S. Brown and C. J. Patel, “A standard database for drug reposi-
tioning,” Scientific data, vol. 4, no. 1, pp. 1–7, 2017.
[805] N. Bogard, J. Linder, A. B. Rosenberg, and G. Seelig, “A deep neural
network for predicting and engineering alternative polyadenylation,”
Cell, vol. 178, no. 1, pp. 91–106, 2019.
[806] Y. Zhan, Z. Xiong, and Y. Yuan, “Rsvg: Exploring data and models
for visual grounding on remote sensing data,” IEEE Transactions on
Geoscience and Remote Sensing, vol. 61, pp. 1–13, 2023.
[807] J. Gu, X. Jiang, Z. Shi, H. Tan, X. Zhai, C. Xu, W. Li, Y. Shen,
S. Ma, H. Liu et al., “A survey on llm-as-a-judge,” arXiv preprint
arXiv:2411.15594, 2024.
[808] M. Zhuge, C. Zhao, D. Ashley, W. Wang, D. Khizbullin, Y. Xiong,
Z. Liu, E. Chang, R. Krishnamoorthi, Y. Tian et al., “Agent-as-a-
88

judge: Evaluate agents with agents,” arXiv preprint arXiv:2410.10934,
2024.
[809] F. Zhang, S. Tian, Z. Huang, Y. Qiao, and Z. Liu, “Evaluation agent:
Efficient and promptable evaluation framework for visual generative
models,” arXiv preprint arXiv:2412.09645, 2024.
[810] Z. Yang, W. Liu, B. Gao, T. Xie, Y. Li, W. Ouyang, S. Poria,
E. Cambria, and D. Zhou, “Moose-chem: Large language models for
rediscovering unseen chemistry scientific hypotheses,” arXiv preprint
arXiv:2410.07076, 2024.
[811] Z. Yang, W. Liu, B. Gao, Y. Liu, W. Li, T. Xie, L. Bing, W. Ouyang,
E. Cambria, and D. Zhou, “Moose-chem2: Exploring llm limits in
fine-grained scientific hypothesis discovery via hierarchical search,”
arXiv preprint arXiv:2505.19209, 2025.
[812] J. Hu, Z. Zhang, G. Chen, X. Wen, C. Shuai, W. Luo, B. Xiao, Y. Li,
and M. Tan, “Test-time learning for large language models,” arXiv
preprint arXiv:2505.20633, 2025.
[813] W. Shi, R. Xu, Y. Zhuang, Y. Yu, H. Sun, H. Wu, C. Yang,
and M. D. Wang, “MedAdapter: Efficient test-time adaptation of
large language models towards medical reasoning,” in Proceedings
of
the
2024
Conference
on
Empirical
Methods
in
Natural
Language
Processing,
Y.
Al-Onaizan,
M.
Bansal,
and
Y.-N.
Chen, Eds.
Miami, Florida, USA: Association for Computational
Linguistics, Nov. 2024, pp. 22 294–22 314. [Online]. Available:
https://aclanthology.org/2024.emnlp-main.1244/
[814] M. Thomas, A. Bou, and G. De Fabritiis, “Test-time training scaling
for chemical exploration in drug design,” arXiv e-prints, pp. arXiv–
2501, 2025.
[815] Z. Gao, T. Li, Y. Kvasiuk, S. C. Tadepalli, M. Rudolph, D. J.
Chung, F. Sala, and M. M¨unchmeyer, “Test-time scaling techniques in
theoretical physics–a comparison of methods on the tpbench dataset,”
arXiv preprint arXiv:2506.20729, 2025.
[816] X. Wang, G. H. Chen, D. Song, Z. Zhang, Z. Chen, Q. Xiao, F. Jiang,
J. Li, X. Wan, B. Wang et al., “Cmb: A comprehensive medical
benchmark in chinese,” arXiv preprint arXiv:2308.08833, 2023.
[817] R.-R. Griffiths, P. Schwaller, and A. A. Lee, “Dataset bias in the
natural sciences: a case study in chemical reaction prediction and
synthesis design,” arXiv preprint arXiv:2105.02637, 2021.
[818] Y.-N. Huang, V. Munteanu, M. I. Love, C. F. Ronkowski, D. Desh-
pande, A. Wong-Beringer, R. Corbett-Detig, M. Dimian, J. H. Moore,
L. X. Garmire et al., “Perceptual and technical barriers in sharing and
formatting metadata accompanying omics studies,” Cell Genomics,
vol. 5, no. 5, 2025.
[819] K. Dwan, C. Gamble, P. R. Williamson, J. J. Kirkham, and R. B.
Group, “Systematic review of the empirical evidence of study pub-
lication bias and outcome reporting bias—an updated review,” PloS
one, vol. 8, no. 7, p. e66844, 2013.
[820] C. Tardy, “The role of english in scientific communication: lingua
franca or tyrannosaurus rex?” Journal of English for academic pur-
poses, vol. 3, no. 3, pp. 247–269, 2004.
[821] M. Graziani, A. Foncubierta, D. Christofidellis, I. Espejo-Morales,
M. Molnar, M. Alberts, M. Manica, and J. Born, “We need improved
data curation and attribution in ai for scientific discovery,” arXiv
preprint arXiv:2504.02486, 2025.
[822] S. Gao, A. Fang, Y. Huang, V. Giunchiglia, A. Noori, J. R. Schwarz,
Y. Ektefaie, J. Kondic, and M. Zitnik, “Empowering biomedical
discovery with ai agents,” Cell, vol. 187, no. 22, pp. 6125–6151,
2024.
[823] S. Ren, P. Jian, Z. Ren, C. Leng, C. Xie, and J. Zhang, “Towards
scientific intelligence: A survey of llm-based scientific agents,” arXiv
preprint arXiv:2503.24047, 2025.
[824] Y. Huang, Y. Chen, H. Zhang, K. Li, M. Fang, L. Yang, X. Li,
L. Shang, S. Xu, J. Hao et al., “Deep research agents: A systematic
examination and roadmap,” arXiv preprint arXiv:2506.18096, 2025.
[825] Anthropic, “Introducing the model context protocol,” https://www.
anthropic.com/news/model-context-protocol, Nov. 2024, accessed:
2025-08-11.
[826] OpenAI, “Computer-using agent,” https://openai.com/zh-Hans-CN/
index/computer-using-agent/, Jan. 2025, accessed: 2025-08-11.
[827] M. Mudryi, M. Chaklosh, and G. W ˘Ałjcik, “The hidden dangers of
browsing ai agents,” arXiv preprint arXiv:2505.13076, 2025.
[828] N. Shinn, F. Cassano, A. Gopinath, K. Narasimhan, and S. Yao,
“Reflexion: Language agents with verbal reinforcement learning,”
Advances in Neural Information Processing Systems, vol. 36, pp.
8634–8652, 2023.
[829] A. Madaan, N. Tandon, P. Gupta, S. Hallinan, L. Gao, S. Wiegreffe,
U. Alon, N. Dziri, S. Prabhumoye, Y. Yang et al., “Self-refine: Itera-
tive refinement with self-feedback,” Advances in Neural Information
Processing Systems, vol. 36, pp. 46 534–46 594, 2023.
[830] G. Wang, Y. Xie, Y. Jiang, A. Mandlekar, C. Xiao, Y. Zhu, L. Fan, and
A. Anandkumar, “Voyager: An open-ended embodied agent with large
language models,” Transactions on Machine Learning Research, 2024.
[Online]. Available: https://openreview.net/forum?id=ehfRiF0R3a
[831] E. Zelikman, Y. Wu, J. Mu, and N. Goodman, “Star: Bootstrapping
reasoning with reasoning,” Advances in Neural Information Process-
ing Systems, vol. 35, pp. 15 476–15 488, 2022.
[832] W. Yuan, R. Y. Pang, K. Cho, S. Sukhbaatar, J. Xu, and J. Weston,
“Self-rewarding language models,” arXiv preprint arXiv:2401.10020,
vol. 3, 2024.
[833] Q. Guo, R. Wang, J. Guo, B. Li, K. Song, X. Tan, G. Liu, J. Bian, and
Y. Yang, “Evoprompt: Connecting llms with evolutionary algorithms
yields powerful prompt optimizers,” in The Twelfth International
Conference on Learning Representations, 2024. [Online]. Available:
https://openreview.net/forum?id=ZG3RaNIsO8
[834] T. Schick, J. Dwivedi-Yu, R. Dess`ı, R. Raileanu, M. Lomeli, E. Ham-
bro, L. Zettlemoyer, N. Cancedda, and T. Scialom, “Toolformer:
Language models can teach themselves to use tools,” Advances in
Neural Information Processing Systems, vol. 36, pp. 68 539–68 551,
2023.
[835] R. Jin, Z. Zhang, M. Wang, and L. Cong, “STELLA: Self-
evolving LLM agent for biomedical research,” arXiv preprint
arXiv:2507.02004, 2025.
[836] Z. Zhang, Z. Qiu, Y. Wu, S. Li, D. Wang, Z. Zhou, D. An, Y. Chen,
Y. Li, Y. Wang et al., “Origene: A self-evolving virtual disease
biologist automating therapeutic target discovery,” bioRxiv, pp. 2025–
06, 2025.
[837] X. Tang, T. Hu, M. Ye, Y. Shao, X. Yin, S. Ouyang, W. Zhou,
P. Lu, Z. Zhang, Y. Zhao et al., “Chemagent: Self-updating memories
in large language models improves chemical reasoning,” in The
Thirteenth International Conference on Learning Representations,
2025.
[838] P. Jansen, M.-A. Cˆot´e, T. Khot, E. Bransom, B. Dalvi Mishra, B. P.
Majumder, O. Tafjord, and P. Clark, “Discoveryworld: A virtual envi-
ronment for developing and evaluating automated scientific discovery
agents,” Advances in Neural Information Processing Systems, vol. 37,
pp. 10 088–10 116, 2024.
[839] T. Chen, S. Anumasa, B. Lin, V. Shah, A. Goyal, and D. Liu, “Auto-
bench: An automated benchmark for scientific discovery in llms,”
arXiv preprint arXiv:2502.15224, 2025.
[840] T. Ossowski, J. Chen, D. Maqbool, Z. Cai, T. Bradshaw, and J. Hu,
“Comma: A communicative multimodal multi-agent benchmark,”
arXiv preprint arXiv:2410.07553, 2024.
[841] M. Mohammadi, Y. Li, J. Lo, and W. Yip, “Evaluation and bench-
marking of llm agents: A survey,” in Proceedings of the 31st ACM
SIGKDD Conference on Knowledge Discovery and Data Mining V.
2, 2025, pp. 6129–6139.
[842] S. Bai, K. Chen, X. Liu, J. Wang, W. Ge, S. Song, K. Dang, P. Wang,
S. Wang, J. Tang et al., “Qwen2. 5-vl technical report,” arXiv preprint
arXiv:2502.13923, 2025.
[843] P. Wang, S. Bai, S. Tan, S. Wang, Z. Fan, J. Bai, K. Chen,
X. Liu, J. Wang, W. Ge et al., “Qwen2-vl: Enhancing vision-language
model’s perception of the world at any resolution,” arXiv preprint
arXiv:2409.12191, 2024.
[844] Z. Luo, Z. Yang, Z. Xu, W. Yang, and X. Du, “Llm4sr: A survey
on large language models for scientific research,” arXiv preprint
arXiv:2501.04306, 2025.
[845] T. Zheng, Z. Deng, H. T. Tsang, W. Wang, J. Bai, Z. Wang, and
Y. Song, “From automation to autonomy: A survey on large language
models in scientific discovery,” arXiv preprint arXiv:2505.13259,
2025.
[846] J. Yuan, X. Yan, B. Shi, T. Chen, W. Ouyang, B. Zhang, L. Bai,
Y. Qiao, and B. Zhou, “Dolphin: Closed-loop open-ended auto-
research through thinking, practice, and feedback,” arXiv e-prints, pp.
arXiv–2501, 2025.
[847] X. Yan, S. Feng, J. Yuan, R. Xia, B. Wang, B. Zhang, and L. Bai,
“Surveyforge: On the outline heuristics, memory-driven generation,
and multi-dimensional evaluation for automated survey writing,” arXiv
preprint arXiv:2503.04629, 2025.
[848] C. Lu, C. Lu, R. T. Lange, J. Foerster, J. Clune, and D. Ha, “The ai
scientist: Towards fully automated open-ended scientific discovery,”
arXiv preprint arXiv:2408.06292, 2024.
[849] Y. Qu, K. Huang, M. Yin, K. Zhan, D. Liu, D. Yin, H. C. Cousins,
W. A. Johnson, X. Wang, M. Shah et al., “CRISPR-GPT for agentic
89

automation of gene-editing experiments,” Nature Biomedical Engi-
neering, pp. 1–14, 2025.
[850] S. Jia, C. Zhang, and V. Fung, “Llmatdesign: Autonomous ma-
terials discovery with large language models,” arXiv preprint
arXiv:2406.13163, 2024.
[851] N. Singh, S. Lane, T. Yu, J. Lu, A. Ramos, H. Cui, and H. Zhao, “A
generalized platform for artificial intelligence-powered autonomous
enzyme engineering,” Nature Communications, vol. 16, no. 1, p. 5648,
2025.
[852] N. Team, B. Zhang, S. Feng, X. Yan, J. Yuan, Z. Yu, X. He, S. Huang,
S. Hou, Z. Nie et al., “Novelseek: When agent becomes the scientist–
building closed-loop system from hypothesis to verification,” arXiv
preprint arXiv:2505.16938, 2025.
[853] A. M. Bran, S. Cox, O. Schilter, C. Baldassari, A. D. White, and
P. Schwaller, “Augmenting large language models with chemistry
tools,” Nature Machine Intelligence, vol. 6, no. 5, pp. 525–535, 2024.
[854] Shanghai AI Lab, “Intern-discovery,” 2025. [Online]. Available:
https://discovery-invitecode.intern-ai.org.cn/
[855] Institute of Automation, Chinese Academy of Sciences, “Scienceone,”
2025. [Online]. Available: https://scienceone.ia.ac.cn
[856] G. Mialon, R. Dess`ı, M. Lomeli, C. Nalmpantis, R. Pasunuru,
R. Raileanu, B. Rozi`ere, T. Schick, J. Dwivedi-Yu, A. Celikyil-
maz et al., “Augmented language models: a survey,” arXiv preprint
arXiv:2302.07842, 2023.
[857] P. Ohm, “Broken promises of privacy: Responding to the surprising
failure of anonymization,” UCLA l. Rev., vol. 57, p. 1701, 2009.
[858] L. Sweeney, “k-anonymity: A model for protecting privacy,” Interna-
tional journal of uncertainty, fuzziness and knowledge-based systems,
vol. 10, no. 05, pp. 557–570, 2002.
[859] R. V. Atreya, J. C. Smith, A. B. McCoy, B. Malin, and R. A. Miller,
“Reducing patient re-identification risk for laboratory results within
research datasets,” Journal of the American Medical Informatics
Association, vol. 20, no. 1, pp. 95–101, 2013.
[860] A. Narayanan and V. Shmatikov, “Robust de-anonymization of large
sparse datasets,” in 2008 IEEE Symposium on Security and Privacy
(sp 2008).
IEEE, 2008, pp. 111–125.
[861] P. Regulation, “General data protection regulation,” Intouch, vol. 25,
pp. 1–5, 2018.
[862] G. Chassang, “The impact of the eu general data protection regulation
on scientific research,” ecancermedicalscience, vol. 11, p. 709, 2017.
[863] H.-D. Jacobsen, “Us export control and export administration leg-
islation,” in Economic Warfare Or Detente.
Routledge, 2019, pp.
213–225.
[864] A. Albalak, Y. Elazar, S. M. Xie, S. Longpre, N. Lambert, X. Wang,
N. Muennighoff, B. Hou, L. Pan, H. Jeong et al., “A survey on
data selection for language models,” arXiv preprint arXiv:2402.16827,
2024.
[865] B. Messmer, V. Sabolˇcec, and M. Jaggi, “Enhancing multilingual
llm pretraining with model-based data selection,” arXiv preprint
arXiv:2502.10361, 2025.
[866] J. T. Wang, T. Wu, D. Song, P. Mittal, and R. Jia, “Greats: Online
selection of high-quality data for llm training in every iteration,”
Advances in Neural Information Processing Systems, vol. 37, pp.
131 197–131 223, 2024.
[867] A. Wettig, A. Gupta, S. Malik, and D. Chen, “Qurating: Select-
ing high-quality data for training language models,” arXiv preprint
arXiv:2402.09739, 2024.
[868] M. Xia, S. Malladi, S. Gururangan, S. Arora, and D. Chen, “Less: Se-
lecting influential data for targeted instruction tuning,” in International
Conference on Machine Learning.
PMLR, 2024, pp. 54 104–54 132.
[869] S. A. Lab, Y. Bao, G. Chen, M. Chen, Y. Chen, C. Chen,
L. Chen, S. Chen, X. Chen, J. Cheng et al., “Safework-r1: Coe-
volving safety and intelligence under the AI-45◦law,” arXiv preprint
arXiv:2507.18576, 2025.
[870] N. Baghbanzadeh, S. Ashkezari, E. Dolatabadi, and A. Afkanpour,
“Open-pmc-18m: A high-fidelity large scale medical dataset for mul-
timodal representation learning,” arXiv preprint arXiv:2506.02738,
2025.
[871] A. Pal, J.-O. Lee, X. Zhang, M. Sankarasubbu, S. Roh, W. J. Kim,
M. Lee, and P. Rajpurkar, “ReXVQA: A Large-scale Visual Question
Answering Benchmark for Generalist Chest X-ray Understanding,”
Jun. 2025.
[872] X. Zhang, J. N. Acosta, J. Miller, O. Huang, and P. Rajpurkar,
“ReXGradient-160K: A Large-Scale Publicly Available Dataset of
Chest Radiographs with Free-text Reports,” May 2025.
[873] C. Liu, H. Wang, J. Pan, Z. Wan, Y. Dai, F. Lin, W. Bai, D. Rueckert,
and R. Arcucci, “Beyond distillation: Pushing the limits of med-
ical llm reasoning with minimalist rule-based RL,” arXiv preprint
arXiv:2505.17952, 2025.
[874] S. Yan, M. Hu, Y. Jiang, X. Li, H. Fei, P. Tschandl, H. Kittler, and
Z. Ge, “Derm1m: A million-scale vision-language dataset aligned
with clinical ontology knowledge for dermatology,” arXiv preprint
arXiv:2503.14911, 2025.
[875] B. Liu, K. Zou, L. Zhan, Z. Lu, X. Dong, Y. Chen, C. Xie, J. Cao,
X.-M. Wu, and H. Fu, “GEMeX: A Large-Scale, Groundable, and
Explainable Medical VQA Benchmark for Chest X-ray Diagnosis,”
Mar. 2025.
[876] C. Ma, Y. Ji, J. Ye, L. Zhang, Y. Chen, T. Li, M. Li, J. He,
and H. Shan, “Towards interpretable counterfactual generation via
multimodal autoregression,” arXiv preprint arXiv:2503.23149, 2025.
[877] T. Lin, W. Zhang, S. Li, Y. Yuan, B. Yu, H. Li, W. He, H. Jiang,
M. Li, X. Song, S. Tang, J. Xiao, H. Lin, Y. Zhuang, and B. C. Ooi,
“HealthGPT: A Medical Large Vision-Language Model for Unifying
Comprehension and Generation via Heterogeneous Knowledge Adap-
tation,” Feb. 2025.
[878] T. Olatunji, C. Nimo, A. Owodunni, T. Abdullahi, E. Ayo-
dele, M. Sanni, C. Aka, F. Omofoye, F. Yuehgoh, T. Faniran
et al., “Afrimed-qa: a pan-african, multi-specialty, medical question-
answering benchmark dataset,” arXiv preprint arXiv:2411.15640,
2024.
[879] W. Sun, X. You, R. Zheng, Z. Yuan, X. Li, L. He, Q. Li, and L. Sun,
“Bora: Biomedical generalist video generation model,” arXiv preprint
arXiv:2407.08944, 2024.
[880] G. Kumichev, P. Blinov, Y. Kuzkina, V. Goncharov, G. Zubkova,
N. Zenovkin, A. Goncharov, and A. Savchenko, “Medsyn: Llm-based
synthetic medical text generation framework,” in Joint European Con-
ference on Machine Learning and Knowledge Discovery in Databases.
Springer, 2024, pp. 215–230.
[881] G. Kell, A. Roberts, S. Umansky, Y. Khare, N. Ahmed, N. Patel,
C. Simela, J. Coumbe, J. Rozario, R.-R. Griffiths, and I. J.
Marshall, “Realmedqa: A pilot biomedical question answering
dataset
containing
realistic
clinical
questions,”
2024.
[Online].
Available: https://arxiv.org/abs/2408.08624
[882] Y. Xie, Z. Wang, Y. Shen, Z. Zhuang, Y. Wang, Z. Zhang, Y. Wu,
Y. Liu, Z. Li, M. Yuan, Z. Yan, Y. Chen, G. Qi, Z. Chen, J. Li,
Y. Zhu, J. Liu, Y. Wang, Y. Shen, and C. Xie, “Medtrinity-25m:
A large-scale multimodal dataset with multigranular annotations
for medicine,” arXiv preprint arXiv:2408.02900, 2024. [Online].
Available: https://arxiv.org/abs/2408.02900
[883] I. Siragusa, S. Contino, M. La Ciura, R. Alicata, and R. Pirrone,
“Medpix 2.0: A comprehensive multimodal biomedical data set for
advanced ai applications,” arXiv preprint arXiv:2407.02994, 2024.
[884] Y. Chen, C. Liu, X. Liu, R. Arcucci, and Z. Xiong, “BIMCV-R: A
Landmark Dataset for 3D CT Text-Image Retrieval,” Jul. 2024.
[885] S. Bae, D. Kyung, J. Ryu, E. Cho, G. Lee, S. Kweon, J. Oh, L. Ji,
E. Chang, T. Kim, and E. Choi, “MIMIC-Ext-MIMIC-CXR-VQA:
A Complex, Diverse, And Large-Scale Visual Question Answering
Dataset for Chest X-ray Images (version 1.0.0),” https://physionet.
org/content/mimic-ext-mimic-cxr-vqa/1.0.0/, 2024.
[886] J. Zhou, L. Sun, Y. Xu, W. Liu, S. Afvari, Z. Han, J. Song, Y. Ji, X. He,
and X. Gao, “Skincap: A multi-modal dermatology dataset annotated
with rich medical captions,” arXiv preprint arXiv:2405.18004, 2024.
[887] R. Wu, C. Zhang, J. Zhang, Y. Zhou, T. Zhou, and H. Fu, “MM-retinal:
Knowledge-enhanced foundational pretraining with fundus image-text
expertise,” in International Conference on Medical Image Computing
and Computer-Assisted Intervention.
Springer, 2024, pp. 722–732.
[888] X. Zhang, C. Wu, Z. Zhao, J. Lei, Y. Zhang, Y. Wang, and W. Xie,
“RadGenome-Chest CT: A Grounded Vision-Language Dataset for
Chest CT Analysis,” Apr. 2024.
[889] Y. Tan, M. Li, Z. Huang, H. Yu, and G. Fan, “Medchatzh: a better
medical adviser learns from better instructions,” 2023. [Online].
Available: https://arxiv.org/abs/2309.01114
[890] G. Xiong, Q. Jin, Z. Lu, and A. Zhang, “Benchmarking retrieval-
augmented generation for medicine,” in Findings of the Association
for Computational Linguistics ACL 2024, 2024, pp. 6233–6251.
[891] M. S. Seyfioglu, W. O. Ikezogwo, F. Ghezloo, R. Krishna, and
L. Shapiro, “Quilt-LLaVA: Visual Instruction Tuning by Extracting
Localized Narratives from Open-Source Histopathology Videos,” Jan.
2025.
[892] S. Lyu, C. Chi, H. Cai, L. Shi, X. Yang, L. Liu, X. Chen, D. Zhao,
Z. Zhang, X. Lyu et al., “Rjua-qa: A comprehensive qa dataset for
urology,” arXiv preprint arXiv:2312.09785, 2023.
90

[893] L. Luo, J. Ning, Y. Zhao, Z. Wang, Z. Ding, P. Chen, W. Fu, Q. Han,
G. Xu, Y. Qiu, D. Pan, J. Li, H. Li, W. Feng, S. Tu, Y. Liu, Z. Yang,
J. Wang, Y. Sun, and H. Lin, “Taiyi: A bilingual fine-tuned large
language model for diverse biomedical tasks,” arXiv, abs/2311.11608,
2023. [Online]. Available: https://arxiv.org/abs/2311.11608
[894] A. B. Abacha, W.-w. Yim, Y. Fan, and T. Lin, “An empirical
study of clinical note generation from doctor-patient encounters,” in
Proceedings of the 17th Conference of the European Chapter of the
Association for Computational Linguistics, 2023, pp. 2291–2302.
[895] S.-C. Huang, Z. Huo, E. Steinberg, C.-C. Chiang, M. P. Lungren, C. P.
Langlotz, S. Yeung, N. H. Shah, and J. A. Fries, “INSPECT: A Mul-
timodal Dataset for Pulmonary Embolism Diagnosis and Prognosis,”
arXiv preprint arXiv:2311.10798, 2023.
[896] K.-H. Støverud, D. Bouget, A. Pedersen, H. O. Leira, T. Langø, and
E. F. Hofstad, “Aeropath: An airway segmentation benchmark dataset
with challenging pathology,” arXiv preprint arXiv:2311.01138, 2023.
[897] Y. Labrak, M. Rouvier, and R. Dufour, “Morfitt: Un corpus multi-
labels d’articles scientifiques franc¸ais dans le domaine biom´edical,” in
18e Conf´erence en Recherche d’Information et Applications–16e Ren-
contres Jeunes Chercheurs en RI–30e Conf´erence sur le Traitement
Automatique des Langues Naturelles–25e Rencontre des ´Etudiants
Chercheurs en Informatique pour le Traitement Automatique des
Langues.
ATALA, 2023, pp. 66–70.
[898] J. Liu, Z. Wang, Q. Ye, D. Chong, P. Zhou, and Y. Hua, “Qilin-med-vl:
Towards chinese large vision-language model for general healthcare,”
arXiv preprint arXiv:2310.17956, 2023.
[899] S. Chen, M. Guevara, S. Moningi, F. Hoebers, H. Elhalawani, B. H.
Kann, F. E. Chipidza, J. Leeman, H. J. W. L. Aerts, T. Miller, G. K.
Savova, R. H. Mak, M. Lustberg, M. Afshar, and D. S. Bitterman,
“The effect of using a large language model to respond to patient
messages,” 2023.
[900] A. D. Lelkes, E. Loreaux, T. Schuster, M.-J. Chen, and A. Rajkomar,
“Sdoh-nli: a dataset for inferring social determinants of health from
clinical notes,” 2023.
[901] S. Yang, H. Zhao, S. Zhu, G. Zhou, H. Xu, Y. Jia, and H. Zan,
“Zhongjing: Enhancing the chinese medical capabilities of large
language model through expert feedback and real-world multi-turn
dialogue,” arXiv, abs/2308.03549, 2023. [Online]. Available: https:
//arxiv.org/abs/2308.03549
[902] Z. Bao, W. Chen, S. Xiao, K. Ren, J. Wu, C. Zhong, J. Peng,
X. Huang, and Z. Wei, “Disc-medllm: Bridging general large lan-
guage models and real-world medical consultation,” arXiv preprint
arXiv:2308.14346, 2023.
[903] F. Remy and T. Demeester, “Automatic glossary of clinical terminol-
ogy: a large-scale dictionary of biomedical definitions generated from
ontological knowledge,” arXiv preprint arXiv:2306.00665, 2023.
[904] W. H. Pinaya, M. S. Graham, E. Kerfoot, P.-D. Tudosiu, J. Dafflon,
V. Fernandez, P. Sanchez, J. Wolleb, P. F. Da Costa, A. Patel et al.,
“Generative ai for medical imaging: extending the monai framework,”
arXiv preprint arXiv:2307.15208, 2023.
[905] C. Li, C. Wong, S. Zhang, N. Usuyama, H. Liu, J. Yang, T. Naumann,
H. Poon, and J. Gao, “LLaVA-Med: Training a large language-and-
vision assistant for biomedicine in one day,” Advances in Neural
Information Processing Systems, vol. 36, pp. 28 541–28 564, 2023.
[906] Wei Zhu and Wenjing Yue and Xiaoling Wang, “ShenNong-TCM: A
Traditional Chinese Medicine Large Language Model,” https://github.
com/michael-wzhu/ShenNong-TCM-LLM, 2023.
[907] X. Zhang, C. Wu, Z. Zhao, W. Lin, Y. Zhang, Y. Wang, and W. Xie,
“PMC-VQA: Visual instruction tuning for medical visual question
answering,” arXiv preprint arXiv:2305.10415, 2023.
[908] Wei Zhu and Xiaoling Wang, “ChatMed: A Chinese Medical Large
Language Model,” https://github.com/michael-wzhu/ChatMed, 2023.
[909] CMKRG, “QiZhenGPT: An Open Source Chinese Medical Large
Language Model,” https://github.com/CMKRG/QiZhenGPT, 2023.
[910] X. Wang, J. Li, S. Chen, Y. Zhu, X. Wu, Z. Zhang, X. Xu, J. Chen,
J. Fu, X. Wan et al., “Huatuo-26m, a large-scale chinese medical qa
dataset,” in Findings of the Association for Computational Linguistics:
NAACL 2025, 2025, pp. 3828–3848.
[911] H. Wang, C. Liu, S. Zhao, B. Qin, and T. Liu, “Med-ChatGLM:
Chinese medical instruction-tuned chatglm-6b,” https://github.com/
SCIR-HI/Med-ChatGLM, 2023.
[912] D. Sileo, K. Uma, and M.-F. Moens, “Generating multiple-choice
questions for medical question answering with distractors and
cue-masking,” in Proceedings of the 2024 Joint International
Conference on Computational Linguistics, Language Resources
and Evaluation (LREC-COLING 2024).
Torino, Italia: ELRA
and
ICCL,
May
2024,
pp.
7647–7653.
[Online].
Available:
https://aclanthology.org/2024.lrec-main.675
[913] N. T.-H. Nguyen, P. P.-D. Ha, L. T. Nguyen, K. Van Nguyen, and
N. L.-T. Nguyen, “Spbertqa: A two-stage question answering system
based on sentence transformers for medical texts,” in International
Conference on Knowledge Science, Engineering and Management.
Springer, 2022, pp. 371–382.
[914] Z. Zhao, Q. Jin, F. Chen, T. Peng, and S. Yu, “Pmc-patients: A large-
scale dataset of patient summaries and relations for benchmarking
retrieval-based clinical decision support systems,” arXiv preprint
arXiv:2202.13876, 2022.
[915] Zhao, Zhengyun and Jin, Qiao and Chen, Fangyuan and Peng,
Tuorui and Yu, Sheng, “A large-scale dataset of patient summaries
for retrieval-based clinical decision support systems,” Scientific data,
vol. 10, no. 1, p. 909, 2023.
[916] Xia,
Fei
and
Li,
Bin
and
Weng,
Yixuan
and
He,
Shizhu
and
Liu,
Kang
and
Sun,
Bin
and
Li,
Shutao
and
Zhao,
Jun, “MedConQA: Medical Conversational Question Answering
System based on Knowledge Graphs,” in Proceedings of the
2022 Conference on Empirical Methods in Natural Language
Processing: System Demonstrations.
Abu Dhabi, UAE: Association
for Computational Linguistics, Dec. 2022, pp. 148–158. [Online].
Available: https://aclanthology.org/2022.emnlp-demos.15
[917] Zhang, Qi and others, “A framework for automatic medical consul-
tation: Dialogue understanding and task-oriented interaction,” Bioin-
formatics, vol. 39, no. 1, p. btac817, 2023.
[918] J. Li, S. Zhong, and K. Chen, “Mlec-qa: A chinese multi-choice
biomedical question answering dataset,” in Proceedings of the 2021
Conference on Empirical Methods in Natural Language Processing,
2021, pp. 8862–8874.
[919] A. Ben Abacha, M. Sarrouti, D. Demner-Fushman, S. A. Hasan, and
H. M¨uller, “Overview of the VQA-Med task at ImageCLEF 2021:
Visual question answering and generation in the medical domain,” in
Proceedings of the CLEF (Conference and Labs of the Evaluation
Forum) 2021 Working Notes, 2021.
[920] R.
Yermakov,
N.
Drago,
and
A.
Ziletti,
“Biomedical
data-
to-text generation via fine-tuning transformers,” in Proceedings
of
the
14th
International
Conference
on
Natural
Language
Generation. Aberdeen, Scotland, UK: Association for Computational
Linguistics, Aug. 2021, pp. 364–370. [Online]. Available: https:
//aclanthology.org/2021.inlg-1.40
[921] N. Zhang, M. Chen, Z. Bi, X. Liang, L. Li, X. Shang, K. Yin, C. Tan,
J. Xu, F. Huang, L. Si, Y. Ni, G. Xie, Z. Sui, B. Chang, H. Zong,
Z. Yuan, L. Li, J. Yan, H. Zan, K. Zhang, B. Tang, and Q. Chen,
“CBLUE: A chinese biomedical language understanding evaluation
benchmark,” https://github.com/CBLUEbenchmark/CBLUE, 2021.
[922] Liu, Wenge and Tang, Jianheng and Cheng, Yi and Li, Wenjie and
Zheng, Yefeng and Liang, Xiaodan, “MedDG: An Entity-Centric
Medical Consultation Dataset for Entity-Aware Medical Dialogue
Generation,” arXiv preprint arXiv:2010.07497, 2022, version 2:
submitted Jul 31, 2022. [Online]. Available: https://arxiv.org/abs/
2010.07497
[923] Toyhom, “Chinese Medical Dialogue Data,” https://github.com/
Toyhom/Chinese-medical-dialogue-data, 2024.
[924] P. Soda, N. C. D’Amico, J. Tessadori, G. Valbusa, V. Guarrasi,
C. Bortolotto, M. U. Akbar, R. Sicilia, E. Cordelli, D. Fazzini et al.,
“Aiforcovid: Predicting the clinical outcomes in patients with covid-
19 applying ai to chest-x-rays. an italian multicentre study,” Medical
image analysis, vol. 74, p. 102216, 2021.
[925] A. Ben Abacha, V. Datla V, S. A. Hasan, D. Demner-Fushman, and
H. M¨uller, “Overview of the VQA-Med task at ImageCLEF 2020:
Visual question answering and generation in the medical domain,” in
Proceedings of the CLEF (Conference and Labs of the Evaluation
Forum) 2020 Working Notes, 2020.
[926] A. Ben Abacha and D. Demner-Fushman, “A question-entailment
approach to question answering,” BMC bioinformatics, vol. 20, no. 1,
p. 511, 2019.
[927] A. Ben Abacha, S. A. Hasan, V. V. Datla, D. Demner-Fushman,
and H. M¨uller, “Vqa-med: Overview of the medical visual question
answering task at ImageCLEF 2019,” in Proceedings of CLEF (Con-
ference and Labs of the Evaluation Forum) 2019 Working Notes, 2019.
[928] He, Junqing and Fu, Mingming and Tu, Manshu, “Applying deep
matching networks to Chinese medical question answering: A study
and a dataset,” BMC Medical Informatics and Decision Making,
vol. 19, no. 2, p. 52, 2019.
[929] Zhang, S. and Zhang, X. and Wang, H. and Guo, L. and Liu, S.,
“Multi-Scale Attentive Interaction Networks for Chinese Medical
91

Question Answer Selection,” IEEE Access, vol. 6, pp. 74 061–74 071,
2018.
[930] O. Pelka, S. Koitka, J. R¨uckert, F. Nensa, and C. M. Friedrich,
“Radiology objects in context (ROCO): A multimodal image dataset,”
in Intravascular Imaging and Computer Assisted Stenting and Large-
Scale Annotation of Biomedical Data and Expert Label Synthesis.
Springer International Publishing, 2018, pp. 180–189.
[931] A. Pampari, P. Raghavan, J. Liang, and J. Peng, “emrqa: A large
corpus for question answering on electronic medical records,” arXiv
preprint arXiv:1809.00732, 2018.
[932] S. A. Hasan, Y. Ling, O. Farri, J. Liu, H. M¨uller, and M. Lungren,
“Overview of ImageCLEF 2018 medical domain visual question
answering task,” Proceedings of CLEF 2018 Working Notes, 2018.
[933] A. Ben Abacha, E. Agichtein, Y. Pinter, and D. Demner-Fushman,
“Overview
of
the
medical
question
answering
task
at
trec-
2017 liveqa,” in Proceedings of The Twenty-Sixth Text REtrieval
Conference (TREC-2017), ser. NIST Special Publication 500-324.
National Institute of Standards and Technology (NIST), 2017,
liveQA track overview for medical QA task. [Online]. Available:
https://trec.nist.gov/pubs/trec26/papers/OverviewQA.pdf
[934] E. Guidotti and D. Ardia, “Covid-19 data hub,” Journal of Open
Source Software, vol. 5, no. 51, p. 2376, 2020.
[935] J. Abreu-Vicente, H. Sonntag, T. Eidens, C. S. Mitchell, and T. Lem-
berger, “Integrating curation into scientific publishing to train ai
models,” arXiv preprint arXiv:2310.20440, 2023.
[936] R. Luo, L. Sun, Y. Xia, T. Qin, S. Zhang, H. Poon, and T.-Y.
Liu, “Biogpt: generative pre-trained transformer for biomedical text
generation and mining,” Briefings in bioinformatics, vol. 23, no. 6, p.
bbac409, 2022.
[937] N. Wang, J. Bian, Y. Li, X. Li, S. Mumtaz, L. Kong, and H. Xiong,
“Multi-purpose rna language modelling with motif-aware pretraining
and type-guided fine-tuning,” Nature Machine Intelligence, vol. 6,
no. 5, pp. 548–557, 2024.
[938] E. Boutet, D. Lieberherr, M. Tognolli, M. Schneider, P. Bansal, A. J.
Bridge, S. Poux, L. Bougueleret, and I. Xenarios, “Uniprotkb/swiss-
prot, the manually annotated section of the uniprot knowledgebase:
how to use the entry view,” in Plant bioinformatics: methods and
protocols.
Springer, 2016, pp. 23–54.
[939] K. Greˇsov´a, V. Martinek, D. ˇCech´ak, P. ˇSimeˇcek, and P. Alexiou,
“Genomic benchmarks: a collection of datasets for genomic sequence
classification,” BMC Genomic Data, vol. 24, no. 1, p. 25, 2023.
[940] J. Chen, H. Xu, W. Tao, Z. Chen, Y. Zhao, and J.-D. J. Han,
“Transformer for one stop interpretable cell type annotation,” Nature
Communications, vol. 14, no. 1, p. 223, 2023.
[941] M. Hao, J. Gong, X. Zeng, C. Liu, Y. Guo, X. Cheng, T. Wang, J. Ma,
X. Zhang, and L. Song, “Large-scale foundation model on single-cell
transcriptomics,” Nature methods, vol. 21, no. 8, pp. 1481–1491, 2024.
[942] L. F. Camarillo-Guerrero, A. Almeida, G. Rangel-Pineros, R. D. Finn,
and T. D. Lawley, “Massive expansion of human gut bacteriophage
diversity,” Cell, vol. 184, no. 4, pp. 1098–1109, 2021.
[943] S. Cheng, Z. Li, R. Gao, B. Xing, Y. Gao, Y. Yang, S. Qin, L. Zhang,
H. Ouyang, P. Du et al., “A pan-cancer single-cell transcriptional atlas
of tumor infiltrating myeloid cells,” Cell, vol. 184, no. 3, pp. 792–809,
2021.
[944] S. Lukassen, R. L. Chua, T. Trefzer, N. C. Kahn, M. A. Schneider,
T. Muley, H. Winter, M. Meister, C. Veith, A. W. Boots et al., “Sars-
cov-2 receptor ace 2 and tmprss 2 are primarily expressed in bronchial
transient secretory cells,” The EMBO journal, vol. 39, no. 10, p.
e105114, 2020.
[945] A. C. Gregory, O. Zablocki, A. A. Zayed, A. Howell, B. Bolduc,
and M. B. Sullivan, “The gut virome database reveals age-dependent
patterns of virome diversity in the human gut,” Cell host & microbe,
vol. 28, no. 5, pp. 724–740, 2020.
[946] L. Schirmer, D. Velmeshev, S. Holmqvist, M. Kaufmann, S. Werneb-
urg, D. Jung, S. Vistnes, J. H. Stockley, A. Young, M. Steindel
et al., “Neuronal vulnerability and multilineage diversity in multiple
sclerosis,” Nature, vol. 573, no. 7772, pp. 75–82, 2019.
[947] O. Franz´en, L.-M. Gan, and J. L. Bj¨orkegren, “Panglaodb: a web
server for exploration of mouse and human single-cell rna sequencing
data,” Database, vol. 2019, p. baz046, 2019.
[948] G. X. Zheng, J. M. Terry, P. Belgrader, P. Ryvkin, Z. W. Bent,
R. Wilson, S. B. Ziraldo, T. D. Wheeler, G. P. McDermott, J. Zhu
et al., “Massively parallel digital transcriptional profiling of single
cells,” Nature communications, vol. 8, no. 1, p. 14049, 2017.
[949] G. Shen, T. Horikawa, K. Majima, and Y. Kamitani, “Deep image re-
construction from human brain activity,” PLoS computational biology,
vol. 15, no. 1, p. e1006633, 2019.
[950] M. Amiri and T. Bocklitz, “Chemrxivquest: A curated chemistry
question-answer database extracted from chemrxiv preprints,” arXiv
preprint arXiv:2505.05232, 2025.
[951] K. Choudhary and M. L. Kelley, “Chemnlp: a natural language-
processing-based library for materials chemistry text data,” The Jour-
nal of Physical Chemistry C, vol. 127, no. 35, pp. 17 545–17 555,
2023.
[952] J. Xie and T. Fu, “Deepprotein: Deep learning library and benchmark
for protein sequence learning,” Bioinformatics, p. btaf165, 2025.
[953] A. Velez-Arce, K. Huang, M. M. Li, X. Lin, W. Gao, T. Fu, M. Kellis,
B. L. Pentelute, and M. Zitnik, “Tdc-2: Multimodal foundation for
therapeutic science,” bioRxiv, pp. 2024–06, 2024.
[954] T. Fu, W. Gao, C. Coley, and J. Sun, “Reinforced genetic algorithm
for structure-based drug design,” Advances in Neural Information
Processing Systems, vol. 35, pp. 12 325–12 338, 2022.
[955] T. Fu, K. Huang, C. Xiao, L. M. Glass, and J. Sun, “HINT: Hi-
erarchical interaction network for clinical-trial-outcome predictions,”
Patterns, vol. 3, no. 4, p. 100445, 2022.
[956] D. S. Wishart, Y. D. Feunang, A. C. Guo, E. J. Lo, A. Marcu, J. R.
Grant, T. Sajed, D. Johnson, C. Li, Z. Sayeeda et al., “Drugbank 5.0:
a major update to the drugbank database for 2018,” Nucleic acids
research, vol. 46, no. D1, pp. D1074–D1082, 2018.
[957] O. Ursu, J. Holmes, J. Knockel, C. G. Bologa, J. J. Yang, S. L.
Mathias, S. J. Nelson, and T. I. Oprea, “Drugcentral: online drug
compendium,” Nucleic acids research, p. gkw993, 2016.
[958] V. Sotnikov and A. Chaikova, “Language models for multimessenger
astronomy,” Galaxies, vol. 11, no. 3, p. 63, 2023.
[959] N. S. Bobbitt, K. Shi, B. J. Bucior, H. Chen, N. Tracy-Amoroso,
Z. Li, Y. Sun, J. H. Merlin, J. I. Siepmann, D. W. Siderius,
and R. Q. Snurr, “Mofx-db: An online database of computational
adsorption data for nanoporous materials,” Journal of Chemical &
Engineering Data, vol. 68, no. 2, pp. 483–498, 2023. [Online].
Available: https://doi.org/10.1021/acs.jced.2c00583
[960] C. Pang, X. Weng, J. Wu, J. Li, Y. Liu, J. Sun, W. Li, S. Wang,
L. Feng, G.-S. Xia et al., “Vhm: Versatile and honest vision language
model for remote sensing image analysis,” in Proceedings of the AAAI
Conference on Artificial Intelligence, vol. 39, no. 6, 2025, pp. 6381–
6388.
[961] J. Luo, Z. Pang, Y. Zhang, T. Wang, L. Wang, B. Dang, J. Lao,
J. Wang, J. Chen, Y. Tan et al., “Skysensegpt: A fine-grained in-
struction tuning dataset and model for remote sensing vision-language
understanding,” arXiv preprint arXiv:2406.10100, 2024.
[962] W. Zhang, M. Cai, T. Zhang, Y. Zhuang, and X. Mao, “Earthgpt:
A universal multimodal large language model for multisensor image
comprehension in remote sensing domain,” IEEE Transactions on
Geoscience and Remote Sensing, vol. 62, pp. 1–20, 2024.
[963] Z. Yuan, Z. Xiong, L. Mou, and X. X. Zhu, “Chatearthnet: A global-
scale image-text dataset empowering vision-language geo-foundation
models,” Earth System Science Data Discussions, vol. 2024, pp. 1–24,
2024.
[964] D. Muhtar, Z. Li, F. Gu, X. Zhang, and P. Xiao, “Lhrs-bot: Empow-
ering remote sensing with vgi-enhanced large multimodal language
model,” in European Conference on Computer Vision.
Springer,
2024, pp. 440–457.
[965] Y. Zhan, Z. Xiong, and Y. Yuan, “Skyeyegpt: Unifying remote sensing
vision-language tasks via instruction tuning with large language
model,” ISPRS Journal of Photogrammetry and Remote Sensing, vol.
221, pp. 64–77, 2025.
[966] R.-Z. Fan, Z. Wang, and P. Liu, “MegaScience: Pushing the Frontiers
of Post-Training Datasets for Science Reasoning,” arXiv e-prints, p.
arXiv:2507.16812, Jul. 2025.
[967] X. Liu and D. Song, “Constructing ophthalmic mllm for positioning-
diagnosis collaboration through clinical cognitive chain reasoning,”
arXiv preprint arXiv:2507.17539, 2025.
[968] Y. Li, J. Liu, T. Zhang, T. Zhang, S. Chen, T. Li, Z. Li, L. Liu,
L. Ming, G. Dong, D. Pan, C. Li, Y. Fang, D. Kuang, M. Wang,
C. Zhu, Y. Zhang, H. Guo, F. Zhang, Y. Wang, B. Ding, W. Song,
X. Li, Y. Huo, Z. Liang, S. Zhang, X. Wu, S. Zhao, L. Xiong, Y. Wu,
J. Ye, W. Lu, B. Li, Y. Zhang, Y. Zhou, X. Chen, L. Su, H. Zhang,
F. Chen, X. Dong, N. Nie, Z. Wu, B. Xiao, T. Li, S. Dang, P. Zhang,
Y. Sun, J. Wu, J. Yang, X. Lin, Z. Ma, K. Wu, J. li, A. Yang, H. Liu,
J. Zhang, X. Chen, G. Ai, W. Zhang, Y. Chen, X. Huang, K. Li,
W. Luo, Y. Duan, L. Zhu, R. Xiao, Z. Su, J. Pu, D. Wang, X. Jia,
T. Zhang, M. Ai, M. Wang, Y. Qiao, L. Zhang, Y. Shen, F. Yang,
M. Zhen, Y. Zhou, M. Chen, F. Li, C. Zhu, K. Lu, Y. Zhao, H. Liang,
Y. Li, Y. Qin, L. Sun, J. Xu, H. Sun, M. Lin, Z. Zhou, and W. Chen,
“Baichuan-Omni-1.5 Technical Report,” Jan. 2025.
92

[969] W. Wang, Y. Su, J. Huan, J. Liu, W. Chen, Y. Zhang, C.-Y. Li, K.-
J. Chang, X. Xin, L. Shen et al., “Asclepius: A spectrum evaluation
benchmark for medical multi-modal large language models,” arXiv
preprint arXiv:2402.11217, 2024.
[970] C. Chen, J. Yu, S. Chen, C. Liu, Z. Wan, D. Bitterman, F. Wang,
and K. Shu, “Clinicalbench: Can llms beat traditional ml models in
clinical prediction?” arXiv preprint arXiv:2411.06469, 2024.
[971] J. Matos, S. Chen, S. Placino, Y. Li, J. C. C. Pardo, D. Idan,
T. Tohyama, D. Restrepo, L. F. Nakayama, J. M. M. Pascual-Leone,
G. Savova, H. Aerts, L. A. Celi, A. I. Wong, D. S. Bitterman, and
J. Gallifant, “WorldMedQA-V: A multilingual, multimodal medical
examination dataset for multimodal language models evaluation,” Oct.
2024.
[972] I. Ziegler, A. K¨oksal, D. Elliott, and H. Sch¨utze, “Craft your dataset:
Task-specific synthetic dataset generation through corpus retrieval and
augmentation,” arXiv preprint arXiv:2409.02098, 2024.
[973] P. Chen, J. Ye, G. Wang, Y. Li, Z. Deng, W. Li, T. Li, H. Duan,
Z. Huang, Y. Su, B. Wang, S. Zhang, B. Fu, J. Cai, B. Zhuang, E. J.
Seibel, J. He, and Y. Qiao, “GMAI-MMBench: A Comprehensive
Multimodal Evaluation Benchmark Towards General Medical AI,”
Oct. 2024.
[974] Y. He, J. Chen, H. Dong, E. Jim´enez-Ruiz, A. Hadian, and I. Hor-
rocks, “Machine learning-friendly biomedical datasets for equivalence
and subsumption ontology matching,” in International semantic web
conference.
Springer, 2022, pp. 575–591.
[975] H. Chen, Z. Fang, Y. Singla, and M. Dredze, “Benchmarking
large language models on answering and explaining challenging
medical questions,” arXiv, abs/2402.18060, 2024. [Online]. Available:
https://arxiv.org/abs/2402.18060
[976] C. Royer, B. Menze, and A. Sekuboyina, “MultiMedEval: A Bench-
mark and a Toolkit for Evaluating Medical Vision-Language Models,”
Feb. 2024.
[977] S. Wu, M. Koo, L. Blum, A. Black, L. Kao, F. Scalzo, and I. Kurtz, “A
comparative study of open-source large language models, gpt-4 and
claude 2: Multiple-choice test taking in nephrology,” arXiv preprint
arXiv:2308.04709, 2023.
[978] T. Tu, S. Azizi, D. Driess, M. Schaekermann, M. Amin, P.-C. Chang,
A. Carroll, C. Lau, R. Tanno, I. Ktena et al., “Towards generalist
biomedical ai,” NEJM AI, vol. 1, no. 3, p. AIoa2300138, 2024.
[979] T. Zack, E. Lehman, M. Suzgun, J. A. Rodriguez, L. A. Celi,
J. Gichoya, D. Jurafsky, P. Szolovits, D. W. Bates, R.-E. E. Abdulnour
et al., “Coding inequity: assessing gpt-4’s potential for perpetuating
racial and gender biases in healthcare,” MedRxiv, pp. 2023–07, 2023.
[980] P. Hosseini, J. M. Sin, B. Ren, B. G. Thomas, E. Nouri, A. Farahanchi,
and S. Hassanpour, “A benchmark for long-form medical question
answering,” arXiv preprint arXiv:2411.09834, 2024.
[981] F. Gaschi, X. Fontaine, P. Rastin, and Y. Toussaint, “Multilingual
clinical ner: Translation or cross-lingual transfer?” in 5th Clinical
Natural Language Processing Workshop.
Association for Computa-
tional Linguistics, 2023, pp. 289–311.
[982] O. Kovaleva, C. Shivade, S. Kashyap, K. Kanjaria, J. Wu, D. Ballah,
A. Coy, A. Karargyris, Y. Guo, D. B. Beymer et al., “Towards
visual dialog for radiology,” in Proceedings of the 19th SIGBioMed
workshop on biomedical language processing, 2020, pp. 60–69.
[983] B. Yu, Y. Li, and J. Wang, “Detecting causal language use in
science findings,” in Proceedings of the 2019 Conference on Empirical
Methods in Natural Language Processing and the 9th International
Joint Conference on Natural Language Processing (EMNLP-IJCNLP),
2019, pp. 4664–4674.
[984] Q. Jin, Y. Yang, Q. Chen, and Z. Lu, “GeneGPT: Augmenting large
language models with domain tools for improved access to biomedical
information,” Bioinformatics, vol. 40, no. 2, p. btae075, 2024.
[985] A. F. Villaverde, D. Henriques, K. Smallbone, S. Bongard, J. Schmid,
D. Cicin-Sain, A. Crombach, J. Saez-Rodriguez, K. Mauch, E. Balsa-
Canto et al., “Biopredyn-bench: a suite of benchmark problems for
dynamic modelling in systems biology,” BMC systems biology, vol. 9,
no. 1, p. 8, 2015.
[986] Y. Liu, L. Lv, X. Zhang, L. Yuan, and Y. Tian, “Bioprobench: Compre-
hensive dataset and benchmark in biological protocol understanding
and reasoning,” arXiv preprint arXiv:2505.07889, 2025.
[987] L. Mitchener, J. M. Laurent, B. Tenmann, S. Narayanan, G. P.
Wellawatte, A. White, L. Sani, and S. G. Rodriques, “Bixbench:
a comprehensive benchmark for llm-based agents in computational
biology,” arXiv preprint arXiv:2503.00096, 2025.
[988] W. Cheng, Z. Song, Y. Zhang, S. Wang, D. Wang, M. Yang, L. Li,
and J. Ma, “Dnalongbench: a benchmark suite for long-range dna
prediction tasks,” bioRxiv, 2025.
[989] V. Sarwal, S. Lee, R. He, A. Kattapuram, E. Eskin, W. Wang,
S. Mangul et al., “Bioinformaticsbench: A collaboratively built large
language model benchmark for bioinformatics reasoning,” in ICML
2024 Workshop on Efficient and Accessible Foundation Models for
Biological Discovery, 2024.
[990] Q. Chen and C. Deng, “Bioinfo-Bench: A simple benchmark
framework for llm bioinformatics skills evaluation,” bioRxiv, 2023.
[Online].
Available:
https://www.biorxiv.org/content/early/2023/10/
21/2023.10.18.563023
[991] E. Nguyen, M. Poli, M. Faizi, A. Thomas, M. Wornow, C. Birch-
Sykes, S. Massaroli, A. Patel, C. Rabideau, Y. Bengio et al., “Hye-
nadna: Long-range genomic sequence modeling at single nucleotide
resolution,” Advances in neural information processing systems,
vol. 36, pp. 43 177–43 201, 2023.
[992] R. K. Umarov and V. V. Solovyev, “Recognition of prokaryotic
and eukaryotic promoters using convolutional deep learning neural
networks,” PloS one, vol. 12, no. 2, p. e0171410, 2017.
[993] E. Z. Kvon, T. Kazmar, G. Stampfel, J. O. Y´a˜nez-Cuna, M. Pa-
gani, K. Schernhuber, B. J. Dickson, and A. Stark, “Genome-scale
functional characterization of drosophila developmental enhancers in
vivo,” Nature, vol. 512, no. 7512, pp. 91–95, 2014.
[994] J. Wu, Z. Ren, J. Wang, P. Zhu, Y. Song, M. Liu, Q. Zheng, L. Bai,
W. Ouyang, and C. Song, “Adabrain-bench: Benchmarking brain
foundation models for brain-computer interface applications,” arXiv
preprint arXiv:2507.09882, 2025.
[995] J. Kim, M. Hur, and M. Min, “From rag to qa-rag: Integrating
generative ai for pharmaceutical regulatory compliance process,”
in Proceedings of the 40th ACM/SIGAPP Symposium on Applied
Computing, 2025, pp. 1293–1295.
[996] H. Yang, J. Cole, Y. Li, R. Chen, G. Min, and K. Li, “Omnigenbench:
A modular platform for reproducible genomic foundation models
benchmarking,” arXiv preprint arXiv:2505.14402, 2024.
[997] M. Nakata and T. Shimazaki, “PubChemQC project: a large-scale
first-principles electronic structure database for data-driven chem-
istry,” Journal of chemical information and modeling, vol. 57, no. 6,
pp. 1300–1308, 2017.
[998] S. Axelrod and R. Gomez-Bombarelli, “GEOM, energy-annotated
molecular conformations for property prediction and molecular gen-
eration,” Scientific Data, vol. 9, no. 1, p. 185, 2022.
[999] S. A. Joseph, S. M. Husain, S. S. Offner, S. Juneau, P. Torrey,
A. S. Bolton, J. P. Farias, N. Gaffney, G. Durrett, and J. J. Li,
“Astrovisbench: A code benchmark for scientific computing and
visualization in astronomy,” arXiv preprint arXiv:2505.20538, 2025.
[1000] N. Alampara, S. Miret, and K. M. Jablonka, “Mattext: Do language
models need more than text & scale for materials modeling?” 2024.
[Online]. Available: https://arxiv.org/abs/2406.17295
[1001] Y. Song, S. Miret, and B. Liu, “Matsci-nlp: Evaluating scientific
language models on materials science language tasks using text-to-
schema modeling,” 2023. [Online]. Available: https://arxiv.org/abs/
2305.08264
[1002] Y.-F. Zhang, H. Zhang, H. Tian, C. Fu, S. Zhang, J. Wu, F. Li,
K. Wang, Q. Wen, Z. Zhang et al., “Mme-realworld: Could your
multimodal llm challenge high-resolution real-world scenarios that
are difficult for humans?” arXiv preprint arXiv:2408.13257, 2024.
[1003] Q. Cheng, H. Huang, Y. Xu, Y. Zhou, H. Li, and Z. Wang, “Nwpu-
captions dataset and mlca-net for remote sensing image captioning,”
IEEE Transactions on Geoscience and Remote Sensing, vol. 60, pp.
1–19, 2022.
[1004] X. Lu, B. Wang, X. Zheng, and X. Li, “Exploring models and data
for remote sensing image caption generation,” IEEE Transactions on
Geoscience and Remote Sensing, vol. 56, no. 4, pp. 2183–2195, 2017.
[1005] W. Chen et al., “Theoremqa: Evaluating large language models on
theorem-based scientific reasoning,” https://arxiv.org/abs/2305.12524,
2023.
[1006] A. Agrawal et al., “Jeebench: Iit-advanced exam problems for evalu-
ating llms,” https://arxiv.org/abs/2305.15074, 2023.
[1007] D. Hendrycks, C. Burns, S. Basart, A. Zou, M. Mazeika, D. Song, and
J. Steinhardt, “Measuring massive multitask language understanding,”
Jan. 2021.
[1008] Z. Gu, X. Zhu, H. Ye, L. Zhang, J. Wang, Y. Zhu, S. Jiang,
Z. Xiong, Z. Li, W. Wu et al., “Xiezhi: An ever-updating benchmark
for holistic domain knowledge evaluation,” in Proceedings of the
AAAI Conference on Artificial Intelligence, vol. 38, no. 16, 2024,
pp. 18 099–18 107.
[1009] Z. Xi, G. Li, Y. Fan, H. Guo, Y. Liu, X. Fan, J. Liu, J. Ding, W. Zuo,
Z. Yin, L. Bai, T. Ji, T. Gui, Q. Zhang, P. Torr, and X. Huang, “Bmmr:
93

A large-scale bilingual multimodal multi-discipline reasoning dataset,”
arXiv preprint arXiv:2507.03483, 2025.
[1010] J. Yin, S. Dash, F. Wang, and M. Shankar, “Forge: Pre-training open
foundation models for science,” in Proceedings of the International
Conference for High Performance Computing, Networking, Storage
and Analysis, 2023, pp. 1–13.
[1011] C. Heneka, F. Nieser, A. Ore, T. Plehn, and D. Schiller, “Large
language models–the future of fundamental physics?” arXiv preprint
arXiv:2506.14757, 2025.
[1012] Y. Ruan, C. Lu, N. Xu, Y. He, Y. Chen, J. Zhang, J. Xuan, J. Pan,
Q. Fang, H. Gao et al., “An automatic end-to-end chemical synthesis
development platform powered by large language models,” Nature
communications, vol. 15, no. 1, p. 10160, 2024.
[1013] Y. Zhang, Y. Han, S. Chen, R. Yu, X. Zhao, X. Liu, K. Zeng, M. Yu,
J. Tian, F. Zhu et al., “Large language models to accelerate organic
chemistry synthesis,” Nature Machine Intelligence, pp. 1–13, 2025.
[1014] Z. Cao, R. Magar, Y. Wang, and A. B. Farimani, “Moformer:
Self-supervised transformer model for metal-organic framework
property prediction,” 2022. [Online]. Available: https://arxiv.org/abs/
2210.14188
[1015] R. Ghugare, S. Miret, A. Hugessen, M. Phielipp, and G. Berseth,
“Searching for high-value molecules using reinforcement learning
and transformers,” 2023. [Online]. Available: https://arxiv.org/abs/
2310.02902
[1016] N.
Gruver,
A.
Sriram,
A.
Madotto,
A.
G.
Wilson,
C.
L.
Zitnick, and Z. Ulissi, “Fine-tuned language models generate
stable inorganic materials as text,” 2025. [Online]. Available:
https://arxiv.org/abs/2402.04379
[1017] N. Alampara, S. Miret, and K. M. Jablonka, “Less can be more for
predicting properties with large language models,” 2025. [Online].
Available: https://arxiv.org/abs/2406.17295
[1018] Y. Kang and J. Kim, “Chatmof: an artificial intelligence system
for predicting and generating metal-organic frameworks using large
language models,” Nature communications, vol. 15, no. 1, p. 4705,
2024.
[1019] M. Vaˇskeviˇcius and J. Kapoˇci¯ut˙e-Dzikien˙e, “Language models for
predicting organic synthesis procedures,” Applied Sciences, vol. 14,
no. 24, 2024. [Online]. Available: https://www.mdpi.com/2076-3417/
14/24/11526
[1020] A. N. Rubungo, C. Arnold, B. P. Rand, and A. B. Dieng, “Llm-
prop: Predicting physical and electronic properties of crystalline
solids from their text descriptions,” 2023. [Online]. Available:
https://arxiv.org/abs/2310.14029
[1021] J. Chen, Z. Cai, Z. Liu, Y. Yang, R. Wang, Q. Xiao, X. Feng, Z. Su,
J. Guo, X. Wan, G. Yu, H. Li, and B. Wang, “Shizhengpt: Towards
multimodal llms for traditional chinese medicine,” arXiv preprint
arXiv:2508.14706, 2025.
[1022] W. Gao, Z. Deng, Z. Niu, F. Rong, C. Chen, Z. Gong, W. Zhang,
D. Xiao, F. Li, Z. Cao et al., “Ophglm: Training an ophthalmology
large language-and-vision assistant based on instructions and dia-
logue,” arXiv preprint arXiv:2306.12174, 2023.
[1023] C. Wu, W. Lin, X. Zhang, Y. Zhang, W. Xie, and Y. Wang, “Pmc-
llama: toward building open-source language models for medicine,”
Journal of the American Medical Informatics Association, vol. 31,
no. 9, pp. 1833–1843, 2024.
[1024] K. Singhal, T. Tu, J. Gottweis, R. Sayres, E. Wulczyn, M. Amin,
L. Hou, K. Clark, S. R. Pfohl, H. Cole-Lewis et al., “Toward expert-
level medical question answering with large language models,” Nature
Medicine, vol. 31, no. 3, pp. 943–950, 2025.
[1025] C. Peng, X. Yang, M. Lyu, K. E. Smith, A. Costa, M. G. Flores,
J. Bian, and Y. Wu, “Gatortron and gatortrongpt: large language
models for clinical narratives,” in AAAI 2024 Spring Symposium on
Clinical Foundation Models, 2024.
[1026] K.
Zhang,
R.
Zhou,
E.
Adhikarla,
Z.
Yan,
Y.
Liu,
J.
Yu,
Z. Liu, X. Chen, B. D. Davison, H. Ren, J. Huang, C. Chen,
Y. Zhou, S. Fu, W. Liu, T. Liu, X. Li, Y. Chen, L. He,
J. Zou, Q. Li, H. Liu, and L. Sun, “A generalist vision–language
foundation model for diverse biomedical tasks,” Nature Medicine,
vol. 30, no. 11, p. 3129–3141, Aug. 2024. [Online]. Available:
http://dx.doi.org/10.1038/s41591-024-03185-2
[1027] G. Wang, G. Yang, Z. Du, L. Fan, and X. Li, “Clinicalgpt: large lan-
guage models finetuned with diverse medical data and comprehensive
evaluation,” arXiv preprint arXiv:2306.09968, 2023.
[1028] V. Fishman, Y. Kuratov, A. Shmelev, M. Petrov, D. Penzar,
D. Shepelin, N. Chekanov, O. Kardymon, and M. Burtsev, “Gena-lm:
a family of open-source foundational dna language models for long
sequences,” Nucleic Acids Research, vol. 53, no. 2, p. gkae1310, 01
2025. [Online]. Available: https://doi.org/10.1093/nar/gkae1310
[1029] L. Y. Jiang, X. C. Liu, N. P. Nejatian, M. Nasir-Moin, D. Wang,
A. Abidin, K. Eaton, H. A. Riina, I. Laufer, P. Punjabi et al., “Health
system-scale language models are all-purpose prediction engines,”
Nature, vol. 619, no. 7969, pp. 357–362, 2023.
[1030] Y. Li, Z. Li, K. Zhang, R. Dan, S. Jiang, and Y. Zhang, “Chatdoctor:
A medical chat model fine-tuned on a large language model meta-ai
(llama) using medical domain knowledge,” Cureus, vol. 15, no. 6,
2023.
[1031] Y. Chen, X. Xing, J. Lin, H. Zheng, Z. Wang, Q. Liu, and X. Xu,
“Soulchat: Improving llms’ empathy, listening, and comfort abilities
through fine-tuning with multi-turn empathy conversations,” arXiv
preprint arXiv:2311.00273, 2023.
[1032] D. Zhang, W. Zhang, B. He, J. Zhang, C. Qin, and J. Yao, “DNAGPT:
A generalized pretrained tool for multiple dna sequence analysis
tasks,” bioRxiv, pp. 2023–07, 2023.
[1033] R. Wang, Y. Duan, C. Lam, J. Chen, J. Xu, H. Chen, X. Liu, P. C.-
I. Pang, and T. Tan, “Ivygpt: Interactive chinese pathway language
model in medical domain,” in CAAI International Conference on
Artificial Intelligence.
Springer, 2023, pp. 378–382.
[1034] C. Wu, X. Zhang, Y. Zhang, Y. Wang, and W. Xie, “Towards
generalist foundation model for radiology by leveraging web-scale
2d&3d medical data,” arXiv preprint arXiv:2308.02463, 2023.
[1035] O. Ben Shoham and N. Rappoport, “Cpllm: Clinical prediction with
large language models,” PLOS Digital Health, vol. 3, no. 12, p.
e0000680, 2024.
[1036] H. Wang, C. Gao, C. Dantona, B. Hull, and J. Sun, “Drg-llama:
tuning llama model to predict diagnosis-related group for hospitalized
patients,” NPJ digital medicine, vol. 7, no. 1, p. 16, 2024.
[1037] R. K. Luu and M. J. Buehler, “Bioinspiredllm: Conversational large
language model for the mechanics of biological and bio-inspired
materials,” Advanced Science, vol. 11, no. 10, p. 2306724, 2024.
[1038] Q. Ye, J. Liu, D. Chong, P. Zhou, Y. Hua, F. Liu, M. Cao,
Z. Wang, X. Cheng, Z. Lei et al., “Qilin-med: Multi-stage knowledge
injection advanced medical large language model,” arXiv preprint
arXiv:2310.09089, 2023.
[1039] Z. Wang, Q. Zhang, K. Ding, M. Qin, X. Zhuang, X. Li, and H. Chen,
“Instructprotein: Aligning human and protein language via knowledge
instruction,” arXiv preprint arXiv:2310.03269, 2023.
[1040] L. Luo, J. Ning, Y. Zhao, Z. Wang, Z. Ding, P. Chen, W. Fu, Q. Han,
G. Xu, Y. Qiu et al., “Taiyi: a bilingual fine-tuned large language
model for diverse biomedical tasks,” Journal of the American Medical
Informatics Association, vol. 31, no. 9, pp. 1865–1874, 2024.
[1041] S. L. Hyland, S. Bannur, K. Bouzid, D. C. Castro, M. Ran-
jit, A. Schwaighofer, F. P´erez-Garc´ıa, V. Salvatelli, S. Srivastav,
A. Thieme et al., “Maira-1: A specialised large multimodal model for
radiology report generation,” arXiv preprint arXiv:2311.13668, 2023.
[1042] S. Bannur, K. Bouzid, D. C. Castro, A. Schwaighofer, A. Thieme,
S. Bond-Taylor, M. Ilse, F. P´erez-Garc´ıa, V. Salvatelli, H. Sharma
et al., “Maira-2: Grounded radiology report generation,” arXiv
preprint arXiv:2406.04449, 2024.
[1043] P. Qiu, C. Wu, X. Zhang, W. Lin, H. Wang, Y. Zhang, Y. Wang,
and W. Xie, “Towards building multilingual language model for
medicine,” Nature Communications, vol. 15, no. 1, p. 8384, 2024.
[1044] L. Lv, Z. Lin, H. Li, Y. Liu, J. Cui, C. Y.-C. Chen, L. Yuan,
and Y. Tian, “Prollama: A protein large language model for multi-
task protein language processing,” IEEE Transactions on Artificial
Intelligence, 2025.
[1045] L. Zhuo, Z. Chi, M. Xu, H. Huang, H. Zheng, C. He, X.-L. Mao, and
W. Zhang, “Protllm: An interleaved protein-language llm with protein-
as-word pre-training,” arXiv preprint arXiv:2403.07920, 2024.
[1046] K. Saab, T. Tu, W.-H. Weng, R. Tanno, D. Stutz, E. Wulczyn,
F. Zhang, T. Strother, C. Park, E. Vedadi et al., “Capabilities of gemini
models in medicine,” arXiv preprint arXiv:2404.18416, 2024.
[1047] J. Abramson, J. Adler, J. Dunger, R. Evans, T. Green, A. Pritzel,
O. Ronneberger, L. Willmore, A. J. Ballard, J. Bambrick, S. W.
Bodenstein, D. A. Evans, C.-C. Hung, M. O’Neill, D. Reiman,
K. Tunyasuvunakool, Z. Wu, A. ˇZemgulyt˙e, E. Arvaniti, C. Beattie,
O. Bertolli, A. Bridgland, A. Cherepanov, M. Congreve, A. I. Cowen-
Rivers, A. Cowie, M. Figurnov, F. B. Fuchs, H. Gladman, R. Jain,
Y. A. Khan, C. M. R. Low, K. Perlin, A. Potapenko, P. Savy, S. Singh,
A. Stecula, A. Thillaisundaram, C. Tong, S. Yakneen, E. D. Zhong,
M. Zielinski, A. ˇZ´ıdek, V. Bapst, P. Kohli, M. Jaderberg, D. Hassabis,
and J. M. Jumper, “Accurate structure prediction of biomolecular
interactions with alphafold 3,” Nature, vol. 630, no. 8016, pp. 493—
-500, 2024.
94

[1048] R. Wang, R. Zhou, H. Chen, Y. Wang, and T. Tan, “CareGPT: Medical
llm, open source driven for a healthy future,” https://github.com/
WangRongsheng/CareGPT, 2023.
[1049] Z. Liu, A. Zhang, H. Fei, E. Zhang, X. Wang, K. Kawaguchi, and
T.-S. Chua, “Prott3: Protein-to-text generation for text-based protein
understanding,” arXiv preprint arXiv:2405.12564, 2024.
[1050] J. Pan, C. Liu, J. Wu, F. Liu, J. Zhu, H. B. Li, C. Chen, C. Ouyang, and
D. Rueckert, “Medvlm-r1: Incentivizing medical reasoning capability
of vision-language models (vlms) via reinforcement learning,” arXiv
preprint arXiv:2502.19634, 2025.
[1051] ˇZ. Avsec, N. Latysheva, J. Cheng, G. Novati, K. R. Taylor, T. Ward,
C. Bycroft, L. Nicolaisen, E. Arvaniti, J. Pan, R. Thomas, V. Dutor-
doir, M. Perino, S. De, A. Karollus, A. Gayoso, T. Sargeant, A. Mot-
tram, L. H. Wong, P. Drot´ar, A. Kosiorek, A. Senior, R. Tanburn,
T. Applebaum, S. Basu, D. Hassabis, and P. Kohli, “AlphaGenome:
advancing regulatory variant effect prediction with a unified DNA
sequence model,” bioRxiv, 2025.
[1052] W. Xu, H. P. Chan, L. Li, M. Aljunied, R. Yuan, J. Wang, C. Xiao,
G. Chen, C. Liu, Z. Li et al., “Lingshu: A generalist foundation model
for unified multimodal medical understanding and reasoning,” arXiv
preprint arXiv:2506.07044, 2025.
[1053] S. Jia, S. Bit, E. Searls, M. V. Lauber, L. A. Claus, P. Fan, V. H.
Jasodanand, D. Veerapaneni, W. M. Wang, R. Au et al., “Podgpt: An
audio-augmented large language model for research and education,”
medRxiv, pp. 2024–07, 2024.
[1054] Z. Xiang, “GeoGPT: Transforming Paleontology with AI-Powered
Data Extraction and Analysis,” EGU General Assembly 2025,
online, 14239, 2025. [Online]. Available: https://meetingorganizer.
copernicus.org/EGU25/EGU25-14239.html?pdf
95
