Review of Materials Research 1 (2025) 100007

![image 1](Wang et al._2025_Knowledge-guided large language model for material science_images/imageFile1.png)

Contents lists available at ScienceDirect

![image 2](Wang et al._2025_Knowledge-guided large language model for material science_images/imageFile2.png)

# Review of Materials Research

journal homepage: www.sciencedirect.com/journal/review-of-materials-research

## Knowledge-guided large language model for material science

Guanjie Wanga,b, Jingjing Hua, Jian Zhoua, Sen Liuc, Qingjiang Li c, Zhimei Suna,*

- a School of Materials Science and Engineering, Beihang University, Beijing, 100191, China
- b School of Integrated Circuit Science and Engineering, Beihang University, Beijing, 100191, China
- c College of Electronic Science and Technology, National University of Defense Technology, Changsha, 410073, China


### A R T I C L E I N F O

A B S T R A C T

Keywords: Large language model Materials science AI agent AI for science Autonomous laboratory

With ChatGPT starting a storm of transformative applications worldwide, the advent of large language models (LLMs) has revolutionized the paradigm of scientiﬁc research, shifting from data-driven methods to AI-driven science. While LLMs have demonstrated signiﬁcant promise in many ﬁelds of science, the development of material knowledge-guided, domain-speciﬁc LLMs remains challenges. In this review, the key milestones of LLMs are discussed, and guidelines for building LLMs are provided, including determining objectives, designing model architectures, data curation, and establishing training and evaluation frameworks. Furthermore, methodologies for creating domain-speciﬁc models through ﬁne-tuning, retrieval-augmented generation, prompt engineering, and AI agents are explored. Additionally, the applications of LLMs in materials science are investigated, ranging from structured information extraction and property prediction to autonomous laboratories and robotics. Finally, challenges such as resource demands, dataset quality, benchmarking, hallucination mitigation, and AI safety are reported alongside emerging opportunities, positioning LLMs as a pivotal tool in advancing materials discovery and innovation.

- 1. Introduction


In recent years, large language models (LLMs) [1] have emerged as transformative tools across numerous scientiﬁc and industrial domains [2–4], driven by breakthroughs in natural language processing and deep learning. These models, exempliﬁed by technologies like ChatGPT, have demonstrated unprecedented capabilities in generating human-like text, processing vast amounts of information, and enabling knowledge discovery at scale [4–8]. This paradigm, shifting from traditional data-driven methods to AI-driven science, has opened new avenues for accelerating research and innovation [9–14].

Materials science is a highly interdisciplinary research ﬁeld, involving the study and manipulation of complex systems across multiple spatial and temporal scales [15–21]. It spans diverse material systems, intricate process parameters, and multiscale phenomena [20–23]. While traditional domain-speciﬁc models have been effective in solving narrowly deﬁned problems, their scalability and adaptability are often inadequate for addressing the challenges posed by such complex systems [24–32]. In contrast, LLMs, with their capacity to leverage vast datasets and incorporate billions of parameters, have demonstrated remarkable potential in handling complex, interconnected systems [33–36]. Their success in

other domains, such as healthcare, chemistry, and physics, underscores their applicability to materials science, where the demand for such advanced tools continues to grow [37–39].

This review aims to bridge the gap by providing a comprehensive roadmap for creating and utilizing domain-speciﬁc LLMs tailored to materials science. Compared to recent reviews on the application of large language models (LLMs) in materials science, our work offers a more indepth and systematic examination of the model development process, including speciﬁc strategies for adapting general-purpose LLMs to materials-related tasks. In particular, we provide a detailed analysis of training methods (e.g., ﬁne-tuning, prompt tuning, low-rank adaptation), the choice of datasets and preprocessing pipelines, and the advantages and limitations of each approach. Furthermore, we summarize the available tools and platforms commonly used in training domain-speciﬁc LLMs, offering practical guidance for researchers aiming to build or customize models for materials informatics. In detail, the milestone and guideline to build an LLMs from scratch are discussed in Section 2, which include deﬁning research objectives, curating high-quality datasets, and designing effective training, and evaluation frameworks. Section 3 introduces the methodologies to build a domain LLM such as ﬁne-tuning, retrieval-augmented generation, prompt engineering, and the

* Corresponding author. E-mail address: zmsun@buaa.edu.cn (Z. Sun).

https://doi.org/10.1016/j.revmat.2025.100007 Received 21 March 2025; Received in revised form 3 April 2025; Accepted 3 April 2025 Available online 5 April 2025 3050-9130/© 2025 The Authors. Published by Elsevier B.V. on behalf of Chinese Materials Research Society. This is an open access article under the CC BY license (http://creativecommons.org/licenses/by/4.0/).

development of AI agents, offering practical insights into adapting LLMs to domain-speciﬁc challenges. The potential applications of domain LLMs in materials science are explored in Section 4, ranging from structured information extraction and property prediction to the realization of autonomous laboratories and robotics for materials discovery. Finally, Section 5 presents the challenges and opportunities, including the need for extensive computational resources, the scarcity of high-quality datasets, and issues like hallucination, benchmarking, and AI safety.

- 2. Milestone and tutorial of LLMs


- 2.1. The development and milestone of LLMs


The evolution of large language models (LLMs) represents a remarkable journey in the ﬁeld of artiﬁcial intelligence, built on a foundation of increasingly sophisticated techniques and groundbreaking innovations. Early language models, such as statistical language models (SLMs) [38,39] in the 1990s, were built to predict sequences of words based on limited context using methods like n-grams. SLMs faced signiﬁcant limitations in natural language processing (NLP) [40–45], particularly the “curse of dimensionality”, which made it challenging to estimate high-order models due to data sparsity. Techniques like smoothing (e.g., backoff [43] and Good-Turing estimation [44]) were used to address this, but the performance was still limited.

In the early 2000s, the advent of neural language models (NLMs) [45, 46] marked a paradigm shift. Leveraging neural networks such as recurrent neural networks (RNNs) [47], these models introduced the concept of distributed word representations, enabling more effective context representation, which allowed better handling of context. Tools

like word2vec [48] made this approach popular by creating compact, high-quality word embeddings, transforming how features were extracted for NLP tasks. This progress paved the way for pre-trained language models (PLMs) like BERT [49], which brought signiﬁcant improvements by using the Transformer [1] architecture. By adopting the Transformer architecture with self-attention mechanisms, BERT pioneered a pre-training-and-ﬁne-tuning paradigm, which signiﬁcantly enhanced performance across diverse NLP tasks and spurred a wave of innovations, including GPT and BART.

As researchers realized that increasing model size and the amount of training data improved performance, large language models (LLMs) like GPT-3 (with 175 billion parameters) [50] and PaLM (with 540 billion parameters) [51] emerged. These models demonstrated remarkable new capabilities, such as in-context learning, which allows them to perform tasks by understanding examples provided during interaction. This advancement has signiﬁcantly boosted AI's potential, especially through applications like ChatGPT. Launched as a conversational AI, ChatGPT quickly gained global attention, with user numbers skyrocketing within weeks due to its ability to deliver engaging, human-like interactions. This rapid growth has cemented LLM's position as a groundbreaking tool in the whole world, sparking widespread interest and discussion across industries. With the rapid growth of computational power, more large models have been developed by various companies, with notable examples including OpenAI's GPT-4 in 2023, and models like Anthropic's Claude 3 and Meta's LLaMA 3 in 2024. Based on the previous work by Zhao et al. [5], we further summarized some of the popular and representative LLMs in recent years, as shown in Fig. 1.

LLMs are now reshaping applications across many ﬁelds [52–61]. They challenge traditional search engines by supporting chatbot-driven

![image 3](Wang et al._2025_Knowledge-guided large language model for material science_images/imageFile3.png)

Fig. 1. A timeline of large language models in recent years. The open-source LLMs are marked as yellow color.

search tools, like the New Bing. Multimodal systems like GPT-4, which can process both text and images, have further broadened their use in areas requiring richer interactions. However, researchers still do not fully understand how LLMs develop their remarkable capabilities. Additionally, building these models requires expertise in handling massive datasets and training them on distributed systems. High costs and technical barriers make it difﬁcult for smaller research groups to train their own models. Tackling these challenges is key to unlocking the full potential of LLMs while ensuring they are used responsibly in real-world settings.

- 2.2. The guide to build an LLMs from scratch


Despite the extensive computational resources, vast datasets and corpus, substantial human effort, and infrastructure are required to train and develop LLMs, we present a streamlined framework and step-by-step process for training an LLM from scratch, as shown in Fig. 2. This guide aims to provide a practical roadmap for materials scientists who are interested in leveraging large models to accelerate research and innovation in the ﬁeld.

- 2.2.1. Determination of the scope and objective Deﬁning the scope and objectives is the foundational step in training


an LLM from scratch, as it directly shapes the model's design, resource requirements, and ultimate utility. As illustrated in Fig. 2(a), when deﬁning your objective, you should take the following issues into consideration:

The primary question to address is: What will the model be used for? The use case is pivotal, as the intended application determines the model's complexity, size, and the type of data it requires. For instance, the model may aim to predict material properties, accelerate the discovery of novel compounds, or assist in interpreting experimental results. A narrowly deﬁned use case, such as optimizing the electronic properties of semi-conductors, might require a smaller, task-speciﬁc model. On the other hand, a broader goal, such as discovering materials for energy storage or catalysts across multiple chemical systems, demands a larger and more versatile model with diverse capabilities. These decisions

inﬂuence not only the model's complexity but also the data and computational resources required.

The model size should correspond to the complexity of the task. For example, creating a general-purpose model for materials design across various disciplines may require billions of parameters to capture the intricate relationships between composition, structure, and properties. However, for a focused task like formation energy prediction in speciﬁc materials, a smaller, lightweight model could sufﬁce. Determining the model's scale early on ensures efﬁcient resource allocation and avoids unnecessary computational overhead. The data requirements for training are closely tied to the deﬁned objectives. In materials science, data often comes from diverse sources, including experimental measurements, highthroughput simulations, and literature databases. A model designed for molecular discovery may require curated quantum chemistry datasets, while one focused on materials processing might need detailed thermodynamic and kinetic data. Clearly deﬁning the use case helps prioritize data collection, ensuring that the model is trained on high-quality and domain-relevant datasets while avoiding redundant or irrelevant information.

2.2.2. Design of the architecture of LLM

As shown in Fig. 2(b), the Transformer architecture [1], which are created by Vaswani et al., in 2017, forms the backbone of most modern LLMs. It is designed to process sequential data while addressing limitations of earlier recurrent neural network (RNN) or convolutional neural network (CNN) models. RNNs process input sequences sequentially, maintaining a hidden state that captures past information. This sequential nature, however, limits parallelization and often leads to challenges such as vanishing gradients when dealing with long sequences. In contrast, Transformers rely on a self-attention mechanism, which allows the model to weigh the importance of different input elements (e.g., words, atoms, or features) when generating predictions. This structure enables efﬁcient parallel processing and captures long-range dependencies, making it well-suited for large-scale applications. This architectural shift signiﬁcantly enhances model scalability and performance in language modeling tasks. The key components of the

![image 4](Wang et al._2025_Knowledge-guided large language model for material science_images/imageFile4.png)

Fig. 2. The framework to build an LLMs from scratch.

Transformer are as follows.

- ➢ Self-attention mechanism: Computes the relationship between input elements by assigning weights that reﬂect their inﬂuence on each other. This is essential for materials science tasks like predicting properties based on structural and compositional features.
- ➢ Multi-head attention: Expands the self-attention mechanism to capture information from different representation subspaces, improving the model's ability to understand diverse materials data.
- ➢ Feedforward layers: Adds non-linearity and depth, helping the model process complex interactions like those in molecular or crystalline structures.
- ➢ Positional encoding: Allows the model to understand the sequence or spatial relationships of input elements, critical for processing data like atomic arrangements or chemical reaction pathways.
- ➢ Autoregressive learning: In autoregressive Transformers, the model learns to predict the next element in a sequence based on all previous elements, one step at a time. This approach is particularly useful in materials science for generating new molecular structures, predicting synthesis pathways, or modeling time-series data such as reaction dynamics. Autoregression ensures that the model generates outputs that are coherent and follow the natural progression of materials data.


Designing the architecture of an LLM for materials science requires careful adaptation of the Transformer framework to meet the unique demands of domain-speciﬁc data and tasks, based on the PyTorch or TensorFlow framework. Materials science encompasses a wide variety of data types, including molecular graphs, crystal structures, simulation results, and experimental observations. To handle this diversity, the input representation must be carefully tailored. For instance, graph neural networks (GNNs) can be integrated with Transformers to process atomic and molecular interactions effectively, making the architecture particularly adept at capturing relational data such as chemical bonds or lattice structures. Additionally, chemical data formats like SMILES strings can be tokenized to retain key molecular features, while crystal structures may beneﬁt from encoded descriptors such as space groups or lattice parameters. In the cases that multiple data modalities, such as microscopy images and spectroscopy results, are used together, the architecture can incorporate dedicated encoders for each modality, merging the outputs with a shared attention layer to unify the information.

Additionally, the scale of the model must align with the complexity of the intended applications. Architectural optimizations, such as sparse attention mechanisms or modular designs, can help balance computational efﬁciency with model performance, enabling researchers to address a wide range of problems without unnecessary computational overhead. Finally, strategies such as mixed-precision training, gradient checkpointing, and distributed systems are vital for managing memory and computational requirements during training. Scalability can also be achieved through parameter-sharing techniques or sparse attention layers, which maintain high performance while minimizing resource consumption.

- 2.2.3. Data preparation and sampling The creation and curation of high-quality datasets are critical steps in


the development of LLMs. The quality of the data directly determines the model's accuracy, reliability, and applicability in solving speciﬁc problems. Unlike adjustable aspects such as architecture design or training techniques, poor data quality cannot be subsequently corrected. Therefore, a high-quality dataset is essential for effectively training LLMs and is characterized by several key attributes.

- ➢ Filtered for inaccuracies to ensure minimal biases and harmful datapoint.
- ➢ Cleaned data is also crucial, requiring the removal of misspellings, blank, spelling variations components.


- ➢ Deduplication is necessary to eliminate repeated information, reducing potential bias in the model.
- ➢ Diverse is important for a high-quality dataset, encompassing a broad spectrum of formats and subjects, including academic writing, prose, website text, coding samples, and mathematics.
- ➢ Reserving a portion of the curated dataset for model evaluation to avoid overﬁtting.


For materials science, high-quality datasets should be accurate, free from inconsistencies, and representative of diverse material systems within the scope, consist of ﬁltering out errors such as typos in chemical notations, cleaning irrelevant text, and ensuring consistency in units and formatting [62–74]. In addition, deduplication is particularly critical to avoid overrepresentation of speciﬁc materials or datasets, which could bias the model toward familiar material systems at the expense of broader generalization [61,69,70]. Additionally, key requirement is diversity in data sources, including computational databases like the Materials Project [71,72] and OQMD [73], experimental datasets from spectroscopy or microscopy studies, and text data from scientiﬁc literature, patents, and technical reports. A diverse dataset helps the model learn relationships across multiple material types and properties, improving its generalizability to new problems. In Table 1, we have organized and summarized the current data repositories (DR) and tools used for training LLMs, along with some commonly used general corpus (GC), domain corpus (DC) and material datasets (MD).

2.2.4. Training the LLM

Training LLMs involves massive computational workloads that exceed the capacity of a single GPU. Parallelization techniques are used to distribute tasks across multiple GPUs to optimize resource use and reduce training times, including data parallelization (divides the training dataset into smaller shards for each GPU), tensor parallelization (splits matrix multiplications across multiple GPUs), pipeline parallelization (distributes the layers of the Transformer across GPUs), and model parallelization (parameters are partitioned across GPUs for extremely large models). Selecting the right strategy depends on the hardware availability, model size, and task complexity, with many projects combining different parallelization methods for the best results.

Meanwhile, choosing the right hyperparameters is vital to optimize the training process and ensure the LLM meets its objectives. Key hyperparameters include.

- ➢ Batch size determines how many samples are processed simultaneously during training. Larger batch sizes improve computational efﬁciency and speed up training but require more memory. Smaller batch sizes reduce memory demands but may result in noisier gradient updates.
- ➢ Learning rate controls how much the model adjusts its parameters with each gradient update. A higher learning rate accelerates training but risks instability and poor convergence. A lower learning rate improves generalization and stability but lengthens training time.
- ➢ Sequence length: A ﬁxed length that accommodates most of the input data ensures that computations remain manageable while reducing truncation errors for long sequences.
- ➢ Temperature parameter controls the randomness of the outputs. Lower values prioritize deterministic results, while higher values introduce more creativity. Task-speciﬁc tuning is often necessary to balance novelty and accuracy.


We have summarized various training frameworks, as listed in Table 2, to simplify the training process of LLM. In addition, the resource consumption of training LLM primarily lies in GPU memory. Evaluating the required GPU memory based on model parameters is another critical issue. The memory required to train an LLM depends primarily on the number of model parameters. For a Transformer-based model, the memory requirement (Mtotal GB) can be approximated as:

Table 1

The datasets for training LLMs, including the current data repositories (DR) and tools used for training LLMs, along with some commonly used general corpus (GC), domain corpus (DC) and material datasets (MD).

Name Type Brief description Link Data Prep Kit DR Democratize and

https://github.com/IBM/data

-prep-kit

accelerate unstructured data preparation for LLM app developers

LLMDataHub DR Awesome Datasets for LLM Training

https://github.com/Zjh-819/LL MDataHub

Hugging Face DR An online resource hub and community that features over 100,000 public datasets

https://huggingface.co/

https://commoncrawl.org/

The Common Crawl

DR A dataset containing terabytes of raw web data extracted from billions of pages. It also has widely-used variations or subsets, including ReﬁnedWeb and C4 (Colossal Cleaned Crawled Corpus)

https://pile.eleuther.ai/

The Pile [74] GC A popular text corpus that contains data from 22 data sources across 5 categories, including Academic Writing, Online or Scraped Resources, Prose, Dialog, and miscellaneous

https://github.com/bigcod e-project/starcoder

StarCoder [75]

GC Close to 800 GB of coding samples in a variety of programming languages

https://paperswithcode.co m/dataset/lima

LIMA dataset GC High quality SFT dataset used by LIMA: Less Is More for Alignment

https://huggingface.co/dataset s/AlgorithmicResearchGroup/ arxiv-physics-instruct-tune-30k

DC Dataset consists of question-answer pairs derived from Arxiv abstracts

arxiv instructed Physics

https://github.com/allenai/pe S2o

peS2o DC A high quality academic paper dataset for pretraining.

Gutenberg project

DC A book dataset, mostly novels.

https://www.gutenberg.org /policy/robot_access.html

https://github.com/openai/p rm800k

PRM800K DC A process supervision dataset for mathematical problems

https://huggingface.co/datas ets/fairchem/OMAT24

OMat24 [76] MD Open Materials 2024:

Inorganic Materials Dataset and Models

https://fair-chem.github.io/co re/datasets/ocx24.html

OCx24 [77] MD Open Catalyst Experiments 2024: Bridging Experiments and Computational Models

Mtotal ¼ Mmodel þ Mbatch_dataset Mmodel ¼ Mparameters þ Mgradient þ Moptimizer Mparameters ¼Mgradient ¼ 0:5Moptimizer ¼ P ⋅ E;

Mbatch dataset ¼H ⋅ N ⋅ B ⋅ S ⋅ E 109;

where P is the number of parameters (in billions), E is the bytes per parameter for gradients, weights, and optimizers (fp32 accuracy need 32 bits or 4 bytes, fp16 accuracy need 16 bits or 2 bytes, int8 accuracy need 8 bits or 1bytes), H is the hidden size per forward pass, N is the number of hidden layers, B is the batch size, and S is the sequence length. For example, training a 10-billion parameter (P ¼ 10) model with fp32 accuracy (E ¼ 4) requires 40 GB model memory. Training the datasets with 4096 hidden sizes (H ¼ 4096), 32 hidden layers (N ¼ 32), a batch size of 64 (B ¼ 64) and a sequence length of 1024 tokens (S ¼ 1024) would require 4096 32 64 1024 4/109 ¼ 34.3 GB batch dataset memory.

- 2.2.5. Evaluating the performance of LLM Evaluating the performance of LLMs requires metrics and datasets

aligned with their intended applications. For predictive numeric tasks, such as estimating material properties, metrics like mean absolute error or root-mean-square error measure accuracy. For generative tasks, the focus shifts to the validity, diversity, and novelty of outputs, such as new material compositions or synthesis pathways, with validity checked against chemical rules and novelty assessed through comparisons with existing datasets. There is currently a lack of benchmark speciﬁcally for material science LLM, but we have summarized some common benchmarks for evaluating model performance as listed in Table 3. Meanwhile, computational efﬁciency, including memory usage and tokens processed per second, is also crucial for assessing practical usability, especially in real-world applications. Furthermore, interpretability tools like attention mechanisms help ensure the model identiﬁes meaningful features, such as atomic arrangements or processing conditions, which enhance trust and usability in scientiﬁc contexts.

- 2.2.6. The list of common LLMs Another key question is whether building a new model from scratch is


necessary. In many cases, existing general-purpose models can be ﬁnetuned with domain-speciﬁc materials data to achieve acceptable performance. In this section, we present a list of existing LLMs, as illustrated in Table 4, to establish a foundation for developing a material domainspeciﬁc model. The construction methodology for the domain model will be introduced in Section 3.

To bridge the gap between general-purpose large language modelsand their applications in materials science, it is essential to consider how foundational architectures are adapted to meet domain-speciﬁc requirements. While Sections 2have outlined the core design principles of LLMs, including Transformer-based architectures and training paradigms, the application of these models in materials science often necessitates customized training strategies, domain-speciﬁc vocabulary integration, and ﬁne-tuning on curated datasets. The following section (Section 3) focuses on these adaptation mechanisms, highlighting representative models and use cases that demonstrate how general LLM frameworks are tailored for tasks in materials informatics.

3. How to build a domain LLM

Building a domain-speciﬁc LLM for materials science without retraining from scratch leverages existing foundation models through targeted techniques such as parameter-efﬁcient ﬁne-tuning (PEFT) [123], prompt engineering [124], retrieval-augmented generation (RAG), and AI agents. These methods allow researchers to adapt a general-purpose model to the specialized needs of materials science, such as predicting material properties, generating synthesis pathways, or interpreting experimental data, without the computational and resource-intensive process of full-scale model training. Next, we will provide a detailed introduction to the four methods for constructing domain-speciﬁc vertical models.

The training framework of LLM.

Name Author Brief description Link DeepSpeed Logan Adams DeepSpeed is a deep learning optimization library that makes distributed training and inference easy,

https://github.com/microsoft/ DeepSpeed

efﬁcient, and effective.

MegatronDeepSpeed

ranzhejiang DeepSpeed version of NVIDIA's Megatron-LM that adds additional support for several features such as MoE model training, Curriculum Learning, 3D Parallelism, and others.

https://github.com/microsoft/ Megatron-DeepSpeed

torchtune ebsmothers A Native-PyTorch Library for LLM Fine-tuning. https://github.com/pytorch/to rchtune torchtitan ebsmothers A native PyTorch Library for large model training. https://github.com/pytorch/t

orchtitan NeMo

ananthsub Generative AI framework built for researchers and PyTorch developers working on Large Language Models (LLMs), Multimodal Models (MMs), Automatic Speech Recognition (ASR), Text to Speech (TTS), and Computer Vision (CV) domains.

https://github.com/NV IDIA/NeMo

Framework

Megatron-LM oliver konig€ Ongoing research training transformer models at scale. https://github.com/NVIDIA/Me gatron-LM Colossal-AI Hongxin Liu Making large AI models cheaper, faster, and more accessible. https://github.com/hpcaitech /ColossalAI BMTrain MayDomine Efﬁcient Training for Big Models. https://github.com/OpenBM

B/BMTrain Mesh

Juan Martinez Mesh TensorFlow: Model Parallelism Made Easier. https://github.com/tensor

ﬂow/mesh maxtext Matthew

Tensorﬂow

A simple, performant and scalable Jax LLM! https://github.com/AI-Hype

rcomputer/maxtext GPT-NeoX LouisCastricato An implementation of model parallel autoregressive transformers on GPUs, based on the DeepSpeed

Davidow

https://github.com/EleutherAI/g pt-neox

library.

- 3.1. Parameter-efﬁcient ﬁne-tuning


Parameter-efﬁcient ﬁne-tuning, a key technique for adapting pretrained LLMs to speciﬁc domains, allows researchers to build domainspeciﬁc models without the need for resource-intensive training from scratch. In the context of materials science, ﬁne-tuning can align a general-purpose LLM with tasks such as predicting material properties, generating synthesis pathways, or summarizing research articles [125, 126]. By reﬁning a pre-trained model with domain-speciﬁc data, ﬁne-tuning improves accuracy, relevance, and applicability, enabling LLMs to meet the specialized demands of materials research.

The ﬁne-tuning methodology for LLMs involves a systematic threestep process to adapt a pre-trained model for speciﬁc domains, as shown in Fig. 3(a). The ﬁrst step is supervised policy training. Highquality, domain-speciﬁc data is collected, and human experts provide demonstrations of desired outputs for given prompts. The pre-trained model is ﬁne-tuned using supervised learning on this dataset, aligning its behavior with the targeted task. Secondly, a dataset of modelgenerated outputs is created, and human labelers rank these outputs based on their quality and relevance. These preferences are used to train a reward model that predicts which outputs align best with human expectations. This step reﬁnes the model's ability to produce preferred results. Finally, the model is further reﬁned by optimizing its performance against the reward model. Using the reinforcement learning with proximal policy optimization (PPO) algorithm, the model generates outputs, receives feedback through the reward model, and iteratively improves. This loop continues until the model achieves stable, high-quality performance on the deﬁned tasks. These steps ensure that the LLM is tailored to domain-speciﬁc requirements while maintaining efﬁciency and alignment with human preferences.

Furthermore, based on ﬁne-tuning different model architectures, PEFT can be categorized into addition-based, modiﬁcation-based, and reparameterization techniques [133–139], as shown in Fig. 3(b).

- ➢ Adapters [128,129]: Small neural networks inserted within the Transformer layers, adapters modify only the added parameters during training, preserving the original model's weights. This reduces memory usage and training overhead. In materials science, adapters could focus on speciﬁc subﬁelds, such as crystallography or spectroscopy, enabling task-speciﬁc specialization.
- ➢ Soft prompts [123,130–132]: Instead of modifying the model's architecture, soft prompts adjust the input embeddings to steer the model's


behavior. For materials LLMs, soft prompts could guide the model to emphasize certain properties or experimental techniques without changing its internal weights, including P-tuning, Preﬁx-tuning, Prompt-tuning.

➢ Low-rank adaptation (LoRA) [133]: a parameter-efﬁcient ﬁne-tuning method that focuses on introducing low-rank updates to the pre-trained model's weights while keeping the majority of parameters frozen. Instead of ﬁne-tuning the entire model, LoRA inserts learnable low-rank matrices that are updated during training, signiﬁcantly reducing memory and computational requirements.

By combining these steps and techniques, ﬁne-tuning provides a scalable, efﬁcient path to developing materials-speciﬁc LLMs. It ensures adaptability, reduces training costs, and preserves the foundational knowledge of pre-trained models, making it a practical choice for advancing AI-driven materials research.

3.2. Retrieval-augmented generation

Retrieval-Augmented Generation (RAG) is a hybrid approach that combines the strengths of parametric and non-parametric memory to enhance language generation [135]. In contrast to purely parametric models, which store all knowledge in their parameters, RAG incorporates a retrieval mechanism that dynamically accesses external, non-parametric memory, such as a database or document corpus. This setup improves the model's ability to handle knowledge-intensive tasks by allowing it to retrieve relevant information on-the-ﬂy, ensuring more factual, interpretable, and up-to-date outputs.

In a RAG model, two main components work together: a retriever and a generator, as shown in Fig. 4. The retriever identiﬁes relevant documents or passages based on a query, leveraging dense vector indexes created from pre-trained neural models (e.g., Dense Passage Retrieval, DPR). These documents serve as external context for the generator, a sequence-to-sequence (seq2seq) language model such as BART or ChatGPT. The generator then combines this retrieved context with the input query to produce outputs.

To build a RAG model, the process begins with initializing a retriever using a pre-trained neural model and a dense index of external memory, such as Wikipedia or a domain-speciﬁc corpus. This setup enables efﬁcient document retrieval through Maximum Inner Product Search (MIPS), matching queries with the most relevant documents. Next, a generator, typically a pre-trained seq2seq model, is ﬁne-tuned to

Table 4 The LLMs for materials science.

The evaluating benchmark of LLM.

Name Brief description Link ARC The Abstraction and Reasoning

Model Year Author ChemBERT 2022 Jiang Guo [80] MatSciBERT 2022 Tanishq Gupta [81] MatBERT 2022 Amalie Trewartha [82] BatteryBERT 2022 Shu Huang [83] MaterialsBERT 2023 Pranav Shetty [84] CatBERTa 2023 Janghoon Ock [85] LLM-Prop 2023 Andre Niyongabo Rubungo [86] ChemDFM 2024 Zihan Zhao [87] CrystalLLM 2024 Nate Gruver [88] ChemLLM 2024 Di Zhang [89] LlaSMol 2024 Botao Yu [90] Text2Mol 2021 Carl Edwards [91] KV-PLM 2022 Zheni Zeng [92] MolT5 2022 Carl Edwards [93] MoMu 2022 Bing Su [94] MoleculeSTM 2023 Shengchao Liu [95] Text þ Chem T5 2023 Dimitrios Christoffdellis GIMLET 2023 Haiteng Zhao [96] MolFM 2023 Yizhen Luo [97] MolCA 2023 Zhiyuan Liu [98] InstructMol 2023 He Cao [99] 3D-MoLM 2024 Sihang Li [100] GIT-Mol 2024 Pengfei Liu [101] SMILES-BERT 2019 Sheng Wang [102] MAT 2020 Łukasz Maziarka [103] ChemBERTa 2020 Seyone Chithrananda [104] MolBERT 2020 Benedek Fabian [105] rxnfp 2021 Philippe Schwaller [106] RXNMapper 2021 Philippe Schwaller [107] MoLFormer 2022 Jerret Ross [108] Chemformer 2022 Ross Irwin [109] R-MAT 2024 Łukasz Maziarka [110] MolGPT 2022 Viraj Bagal [111] T5Chem 2022 Jieyu Lu [112] ChemGPT 2023 Nathan C Frey [113] TransPolymer 2023 Changwen Xu [114] polyBERT 2023 Christopher Kuenneth [115] MFBERT 2022 Hisham Abdel-Aty [116] SPMM 2024 Jinho Chang [117] BARTSmiles 2022 Gayane Chilingaryan [118] MolGen 2023 Yin Fang [119] SELFormer 2023 Atakan Yüksel [120] PolyNC 2024 Haoke Qiu [121] SteelBERT 2025 Shaohan Tian [122]

https://paperswithcode

Corpus (ARC) is a unique benchmark designed to measure AI skill acquisition and track progress towards achieving human-level AI.

.com/sota/common-sense-re asoning-on-arc-challenge

https://paperswithcode.co m/dataset/hellaswag

HellaSwag [78]

Uses sentence completion exercises to test commonsense reasoning and natural language inference (NLI) capabilities.

https://paperswithcode.c om/sota/multi-task-langu age-understanding-on-mmlu

MMLU [79] A comprehensive benchmark comprised of 15,908 questions across 57 tasks that Measure natural language understanding (NLU), i.e., how well an LLM understands language and, subsequently, can solve problems.

https://github.com/ sylinrl/TruthfulQA

TruthfulQA Measuring a model's ability to generate truthful answers, i.e., its propensity to “hallucinate”.

https://paperswithcod e.com/dataset/gsm8k

GSM8K Measures multi-step mathematical abilities through a collection of 8500 grade-school-level math word problems.

HumanEval Measures an LLM's ability to generate functionally correct code.

https://github.com/o penai/human-eval

https://paperswithcode.c om/dataset/mt-bench

MT Bench Evaluates a language model's ability to effectively engage in multi-turn dialogues – like those engaged in by chatbots.

A framework for few-shot evaluation of language models.

https://github.com/Eleuthe rAI/lm-evaluation-harness

lmevaluationharness

https://github.com/Psyco y/MixEval

MixEval A reliable click-and-go evaluation suite compatible with both opensource and proprietary models, supporting MixEval and other benchmarks.

https://github.com/hu ggingface/lighteval

lighteval A lightweight LLM evaluation suite that Hugging Face has been using internally.

OLMO-eval A repository for evaluating open language models.

https://github.com/allenai/ OLMo-Eval

https://github.com/declar e-lab/instruct-eval

instruct-eval This repository contains code to quantitatively evaluate instruction-tuned models such as Alpaca and Flan-T5 on held-out tasks.

property predictions, synthesis planning, or literature reviews. By combining retrieval with generation, RAG offers dynamic, context-aware solutions while retaining the adaptability of pre-trained language models.

simple-evals Eval tools by OpenAI. https://github.com/openai/ simple-evals

https://github.com/ Giskard-AI/giskard

Giskard Testing & evaluation library for LLM applications, in particular RAGs.

https://www.langch ain.com/langsmith

LangSmith A uniﬁed platform from LangChain framework for: evaluation, collaboration HITL (Human In The Loop), logging and monitoring LLM applications.

3.3. Prompt engineering

Prompt engineering is the process of crafting input prompts to guide LLMs toward producing accurate, relevant, and context-speciﬁc outputs [124,136]. At its core, prompt engineering bridges the gap between user intent and the LLM's output by leveraging well-structured instructions, contextual details, and speciﬁc examples. This approach allows users to tailor interactions with LLMs to address various domain-speciﬁc tasks, such as solving problems, automating workﬂows, or generating structured information.

https://github.com/explo dinggradients/ragas

Ragas A framework that helps you evaluate your Retrieval Augmented Generation (RAG) pipelines.

leverage retrieved documents as additional input context, enabling it to perform tasks such as question answering, summarization, or content generation. Finally, the model undergoes joint training, where both the retriever and generator are ﬁne-tuned end-to-end. During training, the model marginalizes over latent retrieved documents, either using the same document for all tokens or varying them token-by-token for more granular context integration. RAG excels in knowledge-intensive domains where static parametric models fall short, such as materials science. In this ﬁeld, it can retrieve real-time data from material property databases, scientiﬁc articles, or computational repositories to assist with

Similar to software patterns in programming, prompt patterns document reusable solutions to recurring problems in LLM interactions. These patterns provide a structured way to design prompts that are adaptable to diverse domains. They include key elements such as naming conventions, intent descriptions, structural ideas, and implementation examples. By codifying these patterns, prompt engineering enhances the transferability of knowledge, enabling users to apply successful prompt structures across different tasks and domains.

To construct effective prompts, the ﬁrst step is to deﬁne the intent and

![image 5](Wang et al._2025_Knowledge-guided large language model for material science_images/imageFile5.png)

Fig. 3. The framework for ﬁne-tuning LLMs. (a) A diagram illustrating the three steps of parameter-efﬁcient ﬁne-tuning (PEFT), adapted from Ref. [127] with permission. (b) The taxonomy of PEFT, adapted from Ref. [125] with permission.

![image 6](Wang et al._2025_Knowledge-guided large language model for material science_images/imageFile6.png)

Fig. 4. Overview of Retrieval-Augmented Generation (RAG), taken from Ref. [134] with permission.

context by clarifying the goal of the prompt and the problem it aims to address, including any constraints, output formats, or speciﬁc requirements, such as summarizing a research paper or generating

hypotheses for materials science. Next, identify key contextual statements that communicate the necessary ideas to the LLM, using taskspeciﬁc keywords, examples, or formatting guidelines to ensure the

model focuses on critical aspects while maintaining ﬂexibility. Finally, iteratively test and reﬁne the prompt with various inputs, incorporating examples of both desired outputs and potential errors to enhance clarity and alignment with the task's objectives. By applying prompt engineering systematically, researchers can harness the full potential of LLMs for domain-speciﬁc applications, enabling precise control over outputs without requiring modiﬁcations to the model itself. This makes prompt engineering a powerful, lightweight tool for maximizing the utility of LLMs across diverse ﬁelds.

- 3.4. AI agents


The AI Agent is an advanced system designed to iteratively interact with tasks, data, and tools, enabling it to reﬁne its responses and achieve more accurate results than conventional linear workﬂows [144–146]. Unlike standard non-agent workﬂows (Fig. 5 (a)), which involve straightforward queries to a large language model (LLM) followed by static answers, AI Agents are characterized by a dynamic feedback loop,

- as shown in Fig. 5(b). This process of iterative thinking, reﬂection, and reﬁnement allows the agent to continuously improve its outputs, often achieving a precision improvement of over 10 % compared to non-agent methods.

The key steps to the construction of an AI Agent are the practice of critique and self-reﬂection. After generating initial outputs, the agent evaluates its responses critically, identifying errors or inconsistencies, and revises its solutions in subsequent iterations. This self-correcting mechanism ensures the system not only is reactive but also progressively learns from its own mistakes to enhance performance. Another key feature of AI Agents is their ability to integrate external tools during their operational cycle. These tools, ranging from databases and retrieval systems to computational simulators and APIs, expand the agent's capabilities beyond its internal knowledge, allowing it to address tasks that require specialized or real-time information. Moreover, the collaborative use of multiple agents represents a signiﬁcant advancement in the ﬁeld,

- as shown in Fig. 5(c). When multiple agents are deployed together, they can divide complex tasks into manageable subtasks, share intermediate results, and cross-verify each other's outputs. This cooperative approach not only enhances the robustness and accuracy of the ﬁnal outcome but also ensures scalability in tackling multifaceted problems. In summary, AI Agents go beyond simple query-response systems by leveraging iterative improvement, external tool integration, and collaboration. These features make them highly effective for complex, knowledge-intensive tasks, positioning them as a pivotal innovation in artiﬁcial intelligence applications.


three efﬁcient approaches and their advancements in extracting material data. Yang et al. introduced the PIEKM (Procedural Information Extraction and Knowledge Management) system, a machine learning-based platform designed to extract and organize synthesis information from unstructured materials science literature [141]. PIEKM addresses the challenges of manually processing vast amounts of procedural data by automating the extraction of recipe steps, chemical entities, ﬁgures, and tables from scientiﬁc articles. The system integrates key functionalities, including information retrieval and interactive statistical visualization, into a user-friendly web interface, enabling researchers to explore connections across large datasets efﬁciently, as shown in Fig. 6(b). One signiﬁcant innovation is PIEKM's ability to perform well in low-resource scenarios, requiring minimal annotated data for domain adaptation, which demonstrates its versatility across various scientiﬁc ﬁelds. By accelerating the understanding and management of synthesis information, PIEKM not only supports materials science research but also provides a scalable framework applicable to other domains. Polak et al. presented a method called ChatExtract, which utilizes conversational LLMs like GPT-4, combined with carefully designed prompts and follow-up questions, to extract high-quality data from research texts [142]. As shown in Fig. 6(c), ChatExtract, employing ChatGPT with proper prompt engineering (as mentioned in section 3.3) and a series of follow-up questions, achieves precision and recall close to 90 % for tasks like creating databases of metallic glass cooling rates and high entropy alloy yield strengths. Additionally, Dagdelen et al. demonstrated significant progress in using LLMs for structured knowledge extraction in materials chemistry with parameter-efﬁcient ﬁne-tuning (as mentioned in section 3.1) [143], as shown in Fig. 6(d). This ﬁne-tuned models like GPT-3 and Llama-2 efﬁciently perform joint named entity recognition and relation extraction (NERRE) tasks, including linking dopants with host materials, cataloging metal-organic frameworks, and extracting complex composition-phase-application relationships. A key advantage is their ability to format extracted data into user-deﬁned schemas such as JSON or structured English sentences. The study highlights the models' quick improvement with limited training data, outperforming BERT-based methods in precision, recall, and F1 scores. The ﬁne-tuning efﬁciency is improved by human-in-the-loop workﬂows streamline annotation, the LoRA weights for Llama-2 further enhance reproducibility and accessibility, making this approach versatile for scaling historical scientiﬁc text conversion into structured databases. LLMs have demonstrated exceptional effectiveness in structured information extraction within materials science, substantially reducing manual effort.

4.2. Prediction of materials structures and properties based on LLMs

- 4. Applications of LLMs in materials science


- 4.1. Structured information extraction


In this section, we integrate the domain-speciﬁc LLM construction methods discussed in Section 3 with practical applications in materialstructured information extraction, as shown in Fig. 6(a), outlining

LLMs play a crucial role in materials science by enabling accurate predictions of material conﬁgurations and properties, thereby providing insights into complex material behaviors. Kang et al. presented an advanced AI agent system (the methods as mentioned in section 3.4) ChatMOF [144], leveraging LLMs like GPT-4 to revolutionize the prediction, retrieval, and generation of metal-organic frameworks (MOFs). As shown in Fig. 7(a), ChatMOF comprises three key components, i.e., an

![image 7](Wang et al._2025_Knowledge-guided large language model for material science_images/imageFile7.png)

Fig. 5. The workﬂow for (a) non-agent, (b) agent, and (c) multi agents.

![image 8](Wang et al._2025_Knowledge-guided large language model for material science_images/imageFile8.png)

- Fig. 6. Three distinct methods for constructing structured information extraction LLMs are presented: (a) the outlines of these methods, adapted from Ref. [140] with permission; corresponding examples include (b) domain speciﬁc models, adapted from Ref. [141] with permission, (c) LLM with prompt engineering, adapted from Ref. [142] with permission, and (d) ﬁne-tuning LLMs, adapted from Ref. [143] with permission.


agent, a toolkit, and an evaluator, forming a robust pipeline for tasks such as data retrieval, property prediction, and structure generation. The system operates with remarkable accuracy, achieving 96.9 % for searching, 95.7 % for property prediction, and 87.5 % for structure generation, showcasing its potential in both straightforward and complex material science tasks. ChatMOF uses LLMs as central coordinators, seamlessly integrating databases and machine learning models to process natural language queries and provide detailed responses, eliminating the need for rigid query structures. Beyond information retrieval, ChatMOF generates MOF structures with user-speciﬁed properties, demonstrating its transformative ability to facilitate material design. By following a systematic ReAct methodology, ChatMOF plans actions, selects tools, and iteratively reﬁnes results to ensure accurate outcomes. Zeni et al. reported a state-of-the-art generative model MatterGen [145], which is designed to create stable and diverse inorganic materials with desired properties, representing a signiﬁcant advancement in materials design. MatterGen employs a diffusion-based generative process that simultaneously reﬁnes atom types, atomic coordinates, and periodic lattice structures, enabling it to overcome challenges associated with generating 3D crystalline materials. Compared to prior models, MatterGen's outputs are more than twice as novel and stable, and 15 times closer to the local energy minimum, ensuring higher material stability. As shown in Fig. 7(b)–a key feature of MatterGen is its integration of adapter modules, which allow ﬁne-tuning towards speciﬁc property constraints using labeled datasets. This capability enables the generation of materials satisfying diverse property targets, such as mechanical, electronic, and magnetic characteristics. MatterGen also excels in multi-property optimization tasks, exempliﬁed by its successful design of magnets with both high magnetic density and low supply-chain risk. Using its ﬁne-tuning capabilities, the model demonstrates improved performance over traditional methods like machine-learning-assisted screening and random substitution. Ross et al. represented MoLFormer, an unsupervised transformer-based LLM designed to learn molecular representations from SMILES sequences of 1.1 billion unlabeled molecules [146]. By leveraging a linear attention mechanism, rotary positional embeddings, and highly distributed training, MoLFormer captures implicit

structure-property relationships, outperforming graph-based and supervised models across ten molecular property prediction benchmarks, as shown in Fig. 7(c). It effectively predicts quantum-chemical and physiological properties while signiﬁcantly reducing computational costs, requiring 60 times fewer GPUs for training. MoLFormer holds promise for material design and drug discovery, though ethical considerations and further exploration of its capabilities in broader molecular contexts remain critical.

For materials inverse design, Chen et al. designed MatterGPT [147], a Transformer-based generative model leveraging the SLICES notation to encode crystal structures as character strings, enabling natural language processing (NLP) techniques for materials design. As shown in Fig. 7 (d), MatterGPT excels in generating new crystal structures with targeted single and multi-objective properties, including lattice-sensitive and lattice-insensitive traits like band gap and formation energy. Despite data scarcity in crystal databases compared to molecular datasets, MatterGPT achieves high validity, uniqueness, and novelty in its outputs. As an open-source tool, it provides comprehensive resources, fostering collaboration and advancing computational materials discovery in areas such as energy and electronics.

4.3. Autonomous laboratory

Beyond materials data extraction, structure design, and property prediction, another prominent application of LLMs is in powering autonomous laboratories and robotics through LLM-based agents. Szymanski et al. presented an autonomous laboratory for solid-state synthesis [148], which is named A-Lab and integrated computations, LLMs agent, and robotics to accelerate materials discovery. The workﬂow of A-Lab is shown in Fig. 8. Over 17 days of continuous operation, A-Lab conducted 355 experiments, achieving a 71 % success rate (41 of 58 targets) in synthesizing novel inorganic compounds, including oxides and phosphates, at a rate of over two new materials per day. Using DFT-computed phase-stability data, text-mined synthesis procedures optimized by LLMs, and active learning to reﬁne failed syntheses, A-Lab demonstrated remarkable efﬁciency and precision. The platform

![image 9](Wang et al._2025_Knowledge-guided large language model for material science_images/imageFile9.png)

- Fig. 7. Overview of prediction of materials structures and properties using large language models. (a) Schematic image of ChatMOF, which comprises three core components: an agent, toolkit, and an evaluator, adapted from Ref. [144] with permission. (b) Fine-tuning of MatterGen for generating materials with speciﬁc chemistry, symmetry, and scalar property constraints, adapted from Ref. [145] with permission. (c) Overview of MoLFormer pipeline, adapted from Ref. [146] with permission. (d) Pipeline for training and sampling using the conditional MatterGPT model, adapted from Ref. [147] with permission.


highlights the potential of autonomous systems to bridge computational predictions and experimental realization, offering a modular workﬂow that combines theory-driven and data-driven techniques.

Additionally, Bran et al. reported an LLM-based chemistry agent (ChemCrow) [55] that integrates 18 computational tools with GPT-4 to tackle tasks in organic synthesis, drug discovery, and materials design, as shown in Fig. 9(a). ChemCrow successfully planned and executed the synthesis of an insect repellent (DEET), three thiourea organo-catalysts, and a novel chromophore with target properties, demonstrating autonomous interaction with physical systems via the RoboRXN platform [57]. ChemCrow achieved high accuracy in chemical reasoning and synthesis planning, outperforming GPT-4 in complex tasks due to its tool-augmented capabilities. While GPT-4 excelled in tasks reliant on memorized knowledge, ChemCrow's tool usage allowed it to address novel, challenging problems with superior chemical factuality and completeness. The system highlights the transformative role of LLMs in autonomous chemistry, though challenges such as tool integration and reproducibility remain areas for improvement. With expanded toolsets

and diversiﬁed tasks, ChemCrow promises to accelerate research in chemistry and materials science. Ni et al. reported an AI-powered materials scientist (MatPilot [149]) that enhances human-machine collaboration in materials discovery, as shown in Fig. 9(b). Integrating human cognitive abilities with AI agents' advanced abstraction and optimization skills, MatPilot generates hypotheses, designs experiments, and employs predictive models to drive automated experimental platforms. It achieves highly efﬁcient iterative optimization, reﬁning experimental parameters with each iteration and leveraging feedback to accelerate discoveries. This system balances AI's computational power with human creativity, directing research toward promising areas while optimizing resource allocation. Huang et al. introduced a visually grounded representation for robotic manipulation tasks that named Relational Keypoint Constraints (ReKep [150]) and encodes desired behaviors using 3D semantic key points. As shown in Fig. 9(c), ReKep maps these key points to numerical costs, enabling real-time hierarchical optimization for robotic actions without task-speciﬁc data or manual labeling. Leveraging large vision and LLMs, ReKep constraints are automatically synthesized from natural

![image 10](Wang et al._2025_Knowledge-guided large language model for material science_images/imageFile10.png)

Fig. 8. Autonomous materials discovery with the A-Lab, adapted from Ref. [148] with permission.

![image 11](Wang et al._2025_Knowledge-guided large language model for material science_images/imageFile11.png)

Fig. 9. Overview of frameworks for autonomous laboratory systems. (a) An overview of the task-solving process in ChemCrow, adapted from Ref. [55] with permission. (b) The architecture of MatPilot, adapted from Ref. [149] with permission. (c) Relational Keypoint Constraints (ReKep) specify diverse manipulation behaviors as an optimizable spatio-temporal series of constraint functions operating on semantic keypoints, adapted from Ref. [150] with permission.

language instructions and RGB-D observations, demonstrating versatility across multi-stage, in-the-wild, bimanual, and reactive tasks. Implemented on two robotic platforms, ReKep achieves efﬁcient closed-loop policies, though challenges remain in keypoint tracking, rigidity assumptions, and computational demands for high-frequency replanning.

In addition, there are many other AI-powered intelligent experimental agents or platforms, such as Mobile ALOHA [151], ORGANA [152], mobile robotics [153], and the Chemist-Intuited Atomic Robotic Probe (CARP) [154]. These platforms showcase the increasing integration of artiﬁcial intelligence into experimental research, enabling greater automation, precision, and scalability in novel materials discovery [155–157].

5. Challenges and opportunities ahead

5.1. Are LLMs the only path to artiﬁcial general intelligence (AGI)?

LLMs have demonstrated signiﬁcant potential in the design of new materials by accelerating property predictions, synthesis planning, and data-driven discovery. However, their true utility in the industrial application of novel material remains debatable. Challenges include their reliance on high-quality, domain-speciﬁc data, limited interpretability in complex materials systems, and the risk of generating scientiﬁcally invalid predictions. Furthermore, their static nature often struggles to

incorporate rapidly evolving knowledge. Alternative approaches, such as Joint Embedding Predictive Architecture (JEPA) [158–160], which excels in learning structured, multimodal representations, or hybrid systems integrating LLMs with Physics-informed machine learning (PIML) and simulation tools [161–163], may offer more robust paths toward AGI. These solutions emphasize reasoning, adaptability, and deeper scientiﬁc understanding beyond mere data-driven correlations.

- 5.2. Resource and parallelization


The development of materials science LLMs faces signiﬁcant challenges in resource demands and parallelization. Training large models requires immense computational power, memory, and energy, often exceeding the capacity of individual systems. Efﬁcient parallelization strategies, such as hybrid data, model, and pipeline parallelism, are critical to optimize resource usage. Techniques such as gradient checkpointing and mixed-precision training can further reduce memory requirements, while innovations in hardware, e.g., advanced GPUs and TPUs, offer scalable solutions. Future progress lies in balancing resource efﬁciency with performance, enabling broader accessibility and fostering collaborative advancements in materials science research.

- 5.3. Materials high-quality datasets


Building a high-quality corpus for materials science LLMs presents signiﬁcant challenges. Materials data is highly diverse, spanning experimental results, computational simulations, and literature, often in inconsistent formats. Ensuring data accuracy, cleaning errors, deduplication, and addressing biases are critical yet resource-intensive tasks. Additionally, integrating multimodal data, such as text, images, and graphs, adds complexity. Accessibility to proprietary or sensitive data further limits corpus comprehensiveness. Future advancements should focus on standardized data-sharing protocols, automated data curation tools, and collaborative efforts to create diverse, high-quality, and domain-relevant corpora for robust LLM development.

- 5.4. Benchmark in materials science


Establishing benchmarks for materials science LLMs faces signiﬁcant challenges due to the ﬁeld's diversity and complexity of this ﬁeld. Materials datasets often vary in quality, format, and scale, making it difﬁcult to create standardized evaluation criteria. Moreover, benchmarks must address multimodal tasks, such as integrating text, images, and simulations, while reﬂecting real-world applications like property prediction and synthesis planning. The scarcity of publicly available, domainspeciﬁc datasets further hinders comparability across models. Future efforts should focus on developing comprehensive, task-speciﬁc benchmarks, fostering collaboration for data sharing, and designing evaluation metrics that capture both scientiﬁc accuracy and practical utility.

5.5. Hallucination in LLMs

Hallucination in materials science LLMs, where models generate scientiﬁcally inaccurate or non-existent information, poses critical risks, especially in property predictions or synthesis pathways. This issue arises from overﬁtting, limited domain knowledge, or biased datasets. Avoidance strategies include integrating retrieval-augmented generation (RAG) for external validation, ﬁne-tuning with high-quality, domainspeciﬁc data, and leveraging physics-informed models for constraints. Benchmarking hallucination rates and applying robust evaluation methods are also essential. Future research must focus on grounding outputs with reliable data sources and cross-disciplinary collaboration to ensure scientiﬁc validity.

- 5.6. Effectiveness of LLMs in complex multi-scale material systems

Applying LLMs to multi-scale material systems across diverse time and spatial scales poses unique challenges. Capturing phenomena from atomic interactions to macroscopic properties requires integrating data from simulations, experiments, and theoretical models. LLMs often struggle with extrapolating across scales due to insufﬁcient multimodal and hierarchical datasets. Ensuring effectiveness demands hybrid models combining LLMs with domain-speciﬁc simulations and embedding physical laws as constraints. Developing uniﬁed datasets, scalable architectures, and tailored evaluation metrics will be critical to address these challenges and unlock the potential of LLMs in complex multi-scale material systems.

- 5.7. AI safety


AI safety in materials science LLMs presents critical challenges, including preventing hallucinations, ensuring data privacy, and avoiding misuse in sensitive applications such as hazardous material design. Models may generate scientiﬁcally invalid outputs or amplify biases, leading to unreliable or harmful outcomes. Ensuring safety requires robust validation mechanisms, integrating domain-speciﬁc knowledge, and transparent evaluation frameworks. Additionally, secure handling of proprietary or sensitive data is essential. Developing regulatory standards, ethical guidelines, and collaborative safety protocols will be crucial to mitigate risks while advancing reliable and responsible use of materials science LLMs.

6. Conclusion

In this review, the latest developments and applications of LLMs in the ﬁeld of materials science are explored. Firstly, we trace the evolution of LLMs, from early statistical language models to advanced pre-trained models like GPT-4, highlighting their breakthroughs in natural language processing. Then, a comprehensive guide on building LLMs from scratch, detailing key steps such as deﬁning model objectives and scope, designing model architecture, data preparation and sampling, model training, and performance evaluation are provided. Subsequently, for constructing domain-speciﬁc LLMs without retraining from scratch, we discuss the four methods, including parameter-efﬁcient ﬁne-tuning, retrieval-augmented generation, prompt engineering, and AI agents. Meanwhile, these techniques are illustrated with practical applications in materials science, such as structured information extraction, prediction of material structures and properties, and the development of autonomous laboratories. Finally, the challenges and future opportunities of implementing LLMs in materials science are discussed, such as resource demands and parallelization, acquisition of high-quality materials datasets, model effectiveness in complex multi-scale systems, and considerations of AI safety. This review aims to provide materials scientists with a thorough understanding of LLMs, fostering their deeper application and advancement in the ﬁeld.

CRediT authorship contribution statement

Guanjie Wang: Writing – review & editing, Writing – original draft, Validation, Resources, Methodology, Investigation, Data curation, Conceptualization. Jingjing Hu: Validation, Resources, Methodology, Investigation, Data curation. Jian Zhou: Writing – review & editing, Writing – original draft, Validation, Resources, Methodology, Data curation. Sen Liu: Resources, Methodology, Data curation. Qingjiang Li: Resources, Methodology, Data curation. Zhimei Sun: Writing – review & editing, Writing – original draft, Validation, Supervision, Resources, Project administration, Methodology, Investigation, Funding acquisition, Data curation, Conceptualization.

Declaration of competing interest

The authors declare that they have no known competing ﬁnancial interests or personal relationships that could have appeared to inﬂuence the work reported in this paper.

Acknowledgments

This work is ﬁnancially supported by the National Key Research and Development Program of China (Grant No. 2022YFB3807200), the National Natural Science Foundation of China (Grant No. 52332005), and the China Postdoctoral Science Foundation (Grant No. 2022TQ0019).

References

- [1] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A.N. Gomez, L. Kaiser,

I. Polosukhin, Attention is all you need, arXiv:1706.03762. https://doi.org/10. 48550/arxiv.1706.03762, 2023.

- [2] Z. Bi, N. Zhang, Y. Xue, Y. Ou, D. Ji, G. Zheng, H. Chen, OceanGPT: a large language model for ocean science tasks, arXiv:2310.02031, https://doi.org/10. 48550/arxiv.2310.02031, 2024.
- [3] D. Wu, W.U. Ahmad, D. Zhang, M.K. Ramanathan, X. Ma, Repoformer: selective retrieval for repository-level code completion, arXiv:2403.10059, https://doi. org/10.48550/arxiv.2403.10059, 2024.
- [4] M. Manica, J. Born, J. Cadow, D. Christoﬁdellis, A. Dave, D. Clarke, Y.G.N. Teukam, G. Giannone, S.C. Hoffman, M. Buchan, V. Chenthamarakshan, T. Donovan, H.H. Hsu, F. Zipoli, O. Schilter, A. Kishimoto, L. Hamada, I. Padhi, K. Wehden, L. McHugh, A. Khrabrov, P. Das, S. Takeda, J.R. Smith, Accelerating material design with the generative toolkit for scientiﬁc discovery, npj Comput. Mater. 9 (2023) 69, https://doi.org/10.1038/s41524-023-01028-1.
- [5] W.X. Zhao, K. Zhou, J. Li, T. Tang, X. Wang, Y. Hou, Y. Min, B. Zhang, J. Zhang, Z. Dong, Y. Du, C. Yang, Y. Chen, Z. Chen, J. Jiang, R. Ren, Y. Li, X. Tang, Z. Liu, P. Liu, J.-Y. Nie, J.-R. Wen, A survey of large language models, arXiv:2303.18223, https://doi.org/10.48550/arxiv.2303.18223, 2023.
- [6] Y. Shen, K. Song, X. Tan, D. Li, W. Lu, Y. Zhuang, HuggingGPT: solving AI tasks with ChatGPT and its friends in hugging face, arXiv:2303.17580, https://doi. org/10.48550/arxiv.2303.17580, 2023.
- [7] H. Touvron, T. Lavril, G. Izacard, X. Martinet, M.-A. Lachaux, T. Lacroix, B. Roziere, N. Goyal, E. Hambro, F. Azhar, A. Rodriguez, A. Joulin, E. Grave, G. Lample, LLaMA: open and efﬁcient foundation language models, arXiv: 2302.13971, https://doi.org/10.48550/arxiv.2302.13971, 2023.
- [8] R. Chang, Y.-X. Wang, E. Ertekin, Towards overcoming data scarcity in materials science: unifying models and datasets with a mixture of experts framework, npj Comput. Mater. 8 (2022) 242, https://doi.org/10.1038/s41524-022-00929-x.
- [9] A. Agrawal, A. Choudhary, Perspective: materials informatics and big data: realization of the “fourth paradigm” of science in materials science, APL Mater. 4

(2016) 053208, https://doi.org/10.1063/1.4946894.

- [10] R.Y. Zhong, X. Xu, E. Klotz, S.T. Newman, Intelligent manufacturing in the context of industry 4.0: a review, Engineering 3 (2017) 616–630, https://doi.org/ 10.1016/J.ENG.2017.05.015.
- [11] Z. Liu, Perspective on materials genome, Chin. Sci. Bull. 59 (2014) 1619–1623, https://doi.org/10.1007/s11434-013-0072-x.
- [12] J. Glick, Ontologies and databases knowledge engineering for materials informatics, in: K. Rajan (Ed.), Informatics for Materials Science and Engineering, Butterworth-Heinemann, Oxford, 2013, pp. 147–187. https://www.sciencedirect

.com/science/article/pii/B9780123943996000084.

- [13] Y. Su, H. Fu, Y. Bai, X. Jiang, J. Xie, Progress in materials genome engineering in China, Acta Metall. Sin. 56 (2020) 1313–1323, https://doi.org/10.11900/ 0412.1961.2020.00199.
- [14] G. Schleder, A. Padilha, C. Acosta, M. Costa, A. Fazzio, From DFT to machine learning: recent approaches to materials science–a review, J. Phys.: Mater. 2

(2019) 032001, https://doi.org/10.1088/2515-7639/ab084b.

- [15] J. Allison, Integrated computational materials engineering: a perspective on progress and future steps, JOM 63 (2011) 15–18, https://doi.org/10.1007/ s11837-011-0053-y.
- [16] W. Yi Wang, J. Li, W. Liu, Z.-K. Liu, Integrated computational materials engineering for advanced materials: a brief review, Comput. Mater. Sci. 158

(2019) 42–48, https://doi.org/10.1016/j.commatsci.2018.11.001.

- [17] J.-C. Zhao, A combinatorial approach for structural materials, Adv. Eng. Mater. 3

(2001) 143–147, https://doi.org/10.1002/1527-2648(200103)3.

- [18] W.F. Maier, K. Stoewe, S. Sieg, Combinatorial and high-throughput materials science, Angew. Chem. Int. Ed. 46 (2007) 6016–6067, https://doi.org/10.1002/ anie.200603675.
- [19] X. Xiang, X. Sun, G. Briceno, Y. Lou, K.-A. Wang, H. Chang, W.G. WallaceFreedman, S.-W. Chen, P.G. Schultz, A combinatorial approach to materials discovery, Science 268 (1995) 1738–1740, https://doi.org/10.1126/ science.268.5218.1738.
- [20] X. Chen, X. Liu, X. Shen, Q. Zhang, Applying machine learning to rechargeable batteries: from the microscale to the macroscale, Angew. Chem. Int. Ed. 133


(2021) 24558–24570, https://doi.org/10.1002/ange.202107369.

- [21] D. Shin, J. Saal (Eds.), Computational Materials System Design, Springer International Publishing, Cham, 2018. http://link.springer.com/10.100 7/978-3-319-68280-8.
- [22] E. Van Der Giessen, P.A. Schultz, N. Bertin, V.V. Bulatov, W. Cai, G. Csanyi, S.M. Foiles, M.G. Geers, C. Gonzalez, M. Hütter, Roadmap on multiscale materials modeling, Modell. Simul. Mater. Sci. Eng. 28 (2020) 043001, https://doi.org/ 10.1088/1361-651X/ab7150.
- [23] K. Choudhary, K.F. Garrity, A.C.E. Reid, B. DeCost, A.J. Biacchi, A.R. Hight Walker, Z. Trautt, J. Hattrick-Simpers, A.G. Kusne, A. Centrone, A. Davydov, J. Jiang, R. Pachter, G. Cheon, E. Reed, A. Agrawal, X. Qian, V. Sharma, H. Zhuang, S.V. Kalinin, B.G. Sumpter, G. Pilania, P. Acar, S. Mandal, K. Haule, D. Vanderbilt, K. Rabe, F. Tavazza, The joint automated repository for various integrated simulations (JARVIS) for data-driven materials design, npj Comput. Mater. 6 (2020) 173, https://doi.org/10.1038/s41524-020-00440-1.
- [24] K.T. Schütt, F. Arbabzadah, S. Chmiela, K.R. Müller, A. Tkatchenko, Quantumchemical insights from deep tensor neural networks, Nat. Commun. 8 (2017) 13890, https://doi.org/10.1038/ncomms13890.
- [25] D. Morgan, R. Jacobs, Opportunities and challenges for machine learning in materials science, Annu. Rev. Mater. Res. 50 (2020) 71–103, https://doi.org/ 10.1146/annurev-matsci-070218-010015.
- [26] J. Xie, Y. Su, D. Xue, X. Jiang, H. Fu, H. Huang, Machine learning for materials research and development, Acta Metall. Sin. 57 (2021) 1343, https://doi.org/ 10.11900/0412.1961.2021.00357.
- [27] K. Gopalakrishnan, Deep learning in data-driven pavement image analysis and automated distress detection: a review, Data 3 (2018) 28, https://doi.org/ 10.3390/data3030028.
- [28] A. Chen, X. Zhang, Z. Zhou, Machine learning: accelerating materials development for energy storage and conversion, InfoMat 2 (2020) 553–576, https://doi.org/ 10.1002/inf2.12094.
- [29] G. Pilania, Machine learning in materials science: from explainable predictions to autonomous design, Comput. Mater. Sci. 193 (2021) 110360, https://doi.org/ 10.1016/j.commatsci.2021.110360.
- [30] M.R. Douglas, Machine learning as a tool in theoretical science, Nat. Rev. Phys. 4

(2022) 145–146, https://doi.org/10.1038/s42254-022-00431-9.

- [31] G. Lei, R. Docherty, S.J. Cooper, Materials science in the era of large language models: a perspective, Digit. Discov. 3 (2024) 1257–1272, https://doi.org/ 10.1039/D4DD00074A.
- [32] Y. Songlin, R. Nian, L. Jianjun, Large-language models: the game-changers for materials science research, Artif. Intell. Chem. 2 (2024) 100076, https://doi.org/ 10.1016/j.aichem.2024.100076.
- [33] X. Xu, M. Li, C. Tao, T. Shen, R. Cheng, J. Li, C. Xu, D. Tao, T. Zhou, A survey on knowledge distillation of large language models, arXiv:2402.13116, https://doi. org/10.48550/arxiv.2402.13116, 2024.
- [34] G.E. Cacciamani, M.B. Eppler, C. Ganjavi, A. Pekan, B. Biedermann, G.S. Collins,

I.S. Gill, Development of the ChatGPT, generative artiﬁcial intelligence and natural large language models for accountable reporting and use (CANGARU) guidelines, arXiv:2307.08974, https://doi.org/10.48550/arxiv.2307.08974, 2023.

- [35] Y. LeCun, Y. Bengio, others, Convolutional networks for images, speech, and time series, Handb, Brain Theory Neural Netw. 3361 (1995) 199, https://doi.org/ 10.5555/303568.303704.
- [36] E. Cambria, B. White, Jumping NLP curves: a review of natural language processing research, IEEE Comput. Intell. Mag. 9 (2014) 48–57, https://doi.org/ 10.1109/MCI.2014.2307227.
- [37] N. Kalchbrenner, E. Grefenstette, P. Blunsom, A convolutional neural network for modelling sentences, Assoc. Comput. Linguist. 1 (2014) 655–665, https://doi.org/ 10.3115/v1/P14-1062.
- [38] C. Zhai, Statistical Language Models for Information Retrieval a Critical Review, Now Foundations and Trends, 2008, https://doi.org/10.1561/1500000008.
- [39] R. Rosenfeld, Two decades of statistical language modeling: where do we go from here? Proc. IEEE 88 (2000) 1270–1278, https://doi.org/10.1109/5.880083.
- [40] K. Chowdhary, K. Chowdhary, Natural Language processing, in: Fundamentals of Artiﬁcial Intelligence, Springer, New Delhi, 2020, pp. 603–649, https://doi.org/ 10.1007/978-81-322-3972-7_19.
- [41] P.M. Nadkarni, L. Ohno-Machado, W.W. Chapman, Natural language processing: an introduction, J. Am. Med. Inform. Assoc. 18 (2011) 544–551, https://doi.org/ 10.1136/amiajnl-2011-000464.
- [42] D. Khurana, A. Koli, K. Khatter, S. Singh, Natural language processing: state of the art, current trends and challenges, Multimed. Tools Appl. 82 (2023) 3713–3744, https://doi.org/10.1007/s11042-022-13428-4.
- [43] J. Bilmes, K. Kirchhoff, Factored language models and generalized parallel backoff, in: Companion Volume of the Proceedings of HLT-NAACL 2003-Short Papers, 2003, pp. 4–6.
- [44] W.A. Gale, G. Sampson, Good-turing frequency estimation without tears, J. Quant. Linguist. 2 (1995) 217–237, https://doi.org/10.1080/09296179508590051.
- [45] Y. Kim, Y. Jernite, D. Sontag, A. Rush, Character-aware neural language models, Proc. AAAI Conf. Artif. Intell. 30 (2016) 2741–2749, https://doi.org/10.5555/ 3016100.3016285.
- [46] J. Kaplan, S. McCandlish, T. Henighan, T.B. Brown, B. Chess, R. Child, S. Gray, A. Radford, J. Wu, D. Amodei, Scaling laws for neural language models, arXiv: 2001.08361, https://doi.org/10.48550/arxiv.2001.08361, 2020.
- [47] M. Schuster, K.K. Paliwal, Bidirectional recurrent neural networks, IEEE Trans. Signal Process. 45 (1997) 2673–2681, https://doi.org/10.1109/78.650093.
- [48] K.W. Church, Word2Vec, Nat. Lang. Eng. 23 (2017) 155–162, https://doi.org/ 10.1017/S1351324916000334.


- [49] J. Devlin, M.-W. Chang, K. Lee, K. Toutanova, Bert: pre-training of deep bidirectional transformers for language understanding, arXiv:1810.04805, htt ps://doi.org/10.48550/arXiv.1810.04805, 2018.
- [50] R. Nakano, J. Hilton, S. Balaji, J. Wu, L. Ouyang, C. Kim, C. Hesse, S. Jain, V. Kosaraju, W. Saunders, X. Jiang, K. Cobbe, T. Eloundou, G. Krueger, K. Button, M. Knight, B. Chess, J. Schulman, WebGPT: browser-assisted question-answering with human feedback, arXiv:2112.09332, https://doi.org/10.48550/arxiv.2112. 09332, 2022.
- [51] A. Chowdhery, S. Narang, J. Devlin, M. Bosma, G. Mishra, A. Roberts, P. Barham, H.W. Chung, C. Sutton, S. Gehrmann, P. Schuh, K. Shi, S. Tsvyashchenko,

- J. Maynez, A. Rao, P. Barnes, Y. Tay, N. Shazeer, V. Prabhakaran, E. Reif, N. Du, B. Hutchinson, R. Pope, J. Bradbury, J. Austin, M. Isard, G. Gur-Ari, P. Yin, T. Duke, A. Levskaya, S. Ghemawat, S. Dev, H. Michalewski, X. Garcia, V. Misra,
- K. Robinson, L. Fedus, D. Zhou, D. Ippolito, D. Luan, H. Lim, B. Zoph, A. Spiridonov, R. Sepassi, D. Dohan, S. Agrawal, M. Omernick, A.M. Dai, T.S. Pillai, M. Pellat, A. Lewkowycz, E. Moreira, R. Child, O. Polozov, K. Lee, Z. Zhou, X. Wang, B. Saeta, M. Diaz, O. Firat, M. Catasta, J. Wei, K. MeierHellstern, D. Eck, J. Dean, S. Petrov, N. Fiedel, PaLM: scaling language modeling with pathways, arXiv:2204.02311, https://doi.org/10.48550/arxiv.2204.02311, 2022.


- [52] S. Zheng, J. He, C. Liu, Y. Shi, Z. Lu, W. Feng, F. Ju, J. Wang, J. Zhu, Y. Min, H. Zhang, S. Tang, H. Hao, P. Jin, C. Chen, F. Noe, H. Liu, T.-Y. Liu, Predicting equilibrium distributions for molecular systems with deep learning, Nat. Mach. Intell. 6 (2024) 558–567, https://doi.org/10.1038/s42256-024-00837-3.
- [53] A. Diaw, M. McKerns, I. Sagert, L.G. Stanton, M.S. Murillo, Efﬁcient learning of accurate surrogates for simulations of complex systems, Nat. Mach. Intell. 6

(2024) 568–577, https://doi.org/10.1038/s42256-024-00839-1.

- [54] N. Wang, J. Bian, Y. Li, X. Li, S. Mumtaz, L. Kong, H. Xiong, Multi-purpose RNA language modelling with motif-aware pretraining and type-guided ﬁne-tuning, Nat. Mach. Intell. 6 (2024) 548–557, https://doi.org/10.1038/s42256-02400836-4.
- [55] A. Bran, S. Cox, O. Schilter, C. Baldassari, A.D. White, P. Schwaller, Augmenting large language models with chemistry tools, Nat. Mach. Intell. 6 (2024) 525–535, https://doi.org/10.1038/s42256-024-00832-8.
- [56] E. Wang, G. Wang, J. Zhou, Z. Sun, MBenes-supported single atom catalysts for oxygen reduction and oxygen evolution reaction by ﬁrst-principles study and machine learning, Natl. Sci. Open 3 (2024) 20230043, https://doi.org/10.1360/ nso/20230043.
- [57] G. Wang, E. Wang, Z. Li, J. Zhou, Z. Sun, Exploring the mathematic equations behind the materials science data using interpretable symbolic regression, Interdiscip. Mater. 3 (2024) 637–657, https://doi.org/10.1002/idm2.12180.
- [58] G. Wang, S. Liu, J. Zhou, Z. Sun, Explainable machine learning in the research of materials science, Acta Metall. Sin. 60 (2024) 1345–1361, https://doi.org/ 10.11900/0412.1961.2024.00160.
- [59] G. Wang, K. Li, L. Peng, Y. Zhang, J. Zhou, Z. Sun, High-throughput automatic integrated material calculations and data management intelligent platform and the application in novel alloys, Acta Metall. Sain. 58 (2022) 75–88, https:// doi.org/10.11900/0412.1961.2021.00041.
- [60] Y. Huang, J. Zhou, G. Wang, Z. Sun, Abnormally strong electron–phonon scattering induced unprecedented reduction in lattice thermal conductivity of two-dimensional Nb2C, J. Am. Chem. Soc. 141 (2019) 8503–8508, https:// doi.org/10.1021/jacs.9b01742.
- [61] Y. Sun, G. Wang, K. Li, L. Peng, J. Zhou, Z. Sun, Accelerating the discovery of transition metal borides by machine learning on small data sets, ACS Appl. Mater. Interfaces 15 (2023) 29278–29286, https://doi.org/10.1021/acsami.3c03657.
- [62] G. Wang, L. Peng, K. Li, L. Zhu, J. Zhou, N. Miao, Z. Sun, ALKEMIE: an intelligent computational platform for accelerating materials discovery and design, Comput. Mater. Sci. 186 (2021) 110064, https://doi.org/10.1016/ j.commatsci.2020.110064.
- [63] G. Wang, J. Zhou, S.R. Elliott, Z. Sun, Role of carbon-rings in polycrystalline GeSb2Te4 phase-change material, J. Alloys Compd. 782 (2019) 852–858, https:// doi.org/10.1016/j.jallcom.2018.12.228.
- [64] G. Wang, C. Wang, X. Zhang, Z. Li, J. Zhou, Z. Sun, Machine learning interatomic potential: bridge the gap between small-scale models and realistic device-scale simulations, iScience 27 (2024) 109673, https://doi.org/10.1016/ j.isci.2024.109673.
- [65] G. Wang, Y. Sun, J. Zhou, Z. Sun, PotentialMind: graph convolutional machine learning potential for Sb–Te binary compounds of multiple stoichiometries, J. Phys. Chem. C 127 (2023) 24724–24733, https://doi.org/10.1021/ acs.jpcc.3c07110.
- [66] G. Wang, Z. Sun, Atomic insights into device-scale phase-change memory materials using machine learning potential, Sci. Bull. 68 (2023) 3105–3107, https://doi.org/10.1016/j.scib.2023.11.038.
- [67] G. Wang, J. Zhou, Z. Sun, First principles investigation on anomalous lattice shrinkage of W alloyed rock salt GeTe, J. Phys. Chem. Solids 137 (2020) 109220, https://doi.org/10.1016/j.jpcs.2019.109220.
- [68] Y. Gan, G. Wang, J. Zhou, Z. Sun, Prediction of thermoelectric performance for layered IV-V-VI semiconductors by high-throughput ab initio calculations and machine learning, npj Comput. Mater. 7 (2021) 176, https://doi.org/10.1038/ s41524-021-00645-y.
- [69] B. Ma, X. Wu, C. Zhao, C. Lin, M. Gao, B. Sa, Z. Sun, An interpretable machine learning strategy for pursuing high piezoelectric coefﬁcients in (K0.5Na0.5)NbO3based ceramics, npj Comput. Mater. 9 (2023) 229, https://doi.org/10.1038/ s41524-023-01187-1.


- [70] L. Zhu, J. Zhou, Z. Sun, Materials data toward machine learning: advances and challenges, J. Phys. Chem. Lett. 13 (2022) 3965–3977, https://doi.org/10.1021/ acs.jpclett.2c00576.
- [71] A. Jain, S. Ong, G. Hautier, W. Chen, W.D. Richards, S. Dacek, S. Cholia, D. Gunter, D. Skinner, G. Ceder, K.A. Persson, Commentary: the Materials Project: a materials genome approach to accelerating materials innovation, APL Mater. 1 (2013) 011002, https://doi.org/10.1063/1.4812323.
- [72] A. Jain, K.A. Persson, G. Ceder, Research Update: the materials genome initiative: data sharing and the impact of collaborative ab initio databases, APL Mater. 4

(2016) 053102, https://doi.org/10.1063/1.4944683.

- [73] J.E. Saal, S. Kirklin, M. Aykol, B. Meredig, C. Wolverton, Materials design and discovery with high-throughput density functional theory: the open quantum materials database (OQMD), JOM 65 (2013) 1501–1509, https://doi.org/ 10.1007/s11837-013-0755-4.
- [74] L. Gao, S. Biderman, S. Black, L. Golding, T. Hoppe, C. Foster, J. Phang, H. He, A. Thite, N. Nabeshima, S. Presser, C. Leahy, The pile: an 800GB dataset of diverse text for language modeling, arXiv:2101.00027, https://doi.org/10.48550/arxiv.2 101.00027, 2020.
- [75] R. Li, L.B. Allal, Y. Zi, N. Muennighoff, D. Kocetkov, C. Mou, M. Marone, C. Akiki, J. Li, J. Chim, Q. Liu, E. Zheltonozhskii, T.Y. Zhuo, T. Wang, O. Dehaene,

- M. Davaadorj, J. Lamy-Poirier, J. Monteiro, O. Shliazhko, N. Gontier, N. Meade, A. Zebaze, M.-H. Yee, L.K. Umapathi, J. Zhu, B. Lipkin, M. Oblokulov, Z. Wang,

- R. Murthy, J. Stillerman, S.S. Patel, D. Abulkhanov, M. Zocca, M. Dey, Z. Zhang,

N. Fahmy, U. Bhattacharyya, W. Yu, S. Singh, S. Luccioni, P. Villegas, M. Kunakov, F. Zhdanov, M. Romero, T. Lee, N. Timor, J. Ding, C. Schlesinger, H. Schoelkopf, J. Ebert, T. Dao, M. Mishra, A. Gu, J. Robinson, C.J. Anderson, B. Dolan-Gavitt, D. Contractor, S. Reddy, D. Fried, D. Bahdanau, Y. Jernite, C.M. Ferrandis,

- S. Hughes, T. Wolf, A. Guha, L. von Werra, H. de Vries, StarCoder: may the source be with you, arXiv:2305.06161, https://doi.org/10.48550/arxiv.2305.06161, 2023.




- [76] L. Barroso-Luque, M. Shuaibi, X. Fu, B.M. Wood, M. Dzamba, M. Gao, A. Rizvi, C.L. Zitnick, Z.W. Ulissi, Open materials 2024 (OMat24) inorganic materials dataset and models, arXiv:2410.12771, https://doi.org/10.48550/arxiv.2410.12 771, 2024.
- [77] J. Abed, J. Kim, M. Shuaibi, B. Wander, B. Duijf, S. Mahesh, H. Lee, V. Gharakhanyan, S. Hoogland, E. Irtem, J. Lan, N. Schouten, A.U. Vijayakumar, J. Hattrick-Simpers, J.R. Kitchin, Z.W. Ulissi, A. van Vugt, E.H. Sargent, D. Sinton, C.L. Zitnick, Open catalyst experiments 2024 (OCx24): bridging experiments and computational models, arXiv:2411.11783, https://doi.org/10.48550/arxiv.2411. 11783, 2024.
- [78] R. Zellers, A. Holtzman, Y. Bisk, A. Farhadi, Y. Choi, HellaSwag: can a machine really ﬁnish your sentence?, arXiv:1905.07830, https://doi.org/10.48550/arxiv.1 905.07830, 2019.
- [79] D. Hendrycks, C. Burns, S. Basart, A. Zou, M. Mazeika, D. Song, J. Steinhardt, Measuring massive multitask language understanding, arXiv:2009.03300, htt ps://doi.org/10.48550/arxiv.2009.03300, 2021.
- [80] J. Guo, A.S. Ibanez-Lopez, H. Gao, V. Quach, C.W. Coley, K.F. Jensen, R. Barzilay, Automated chemical reaction extraction from scientiﬁc literature, J. Chem. Inf. Model. 62 (2022) 2035–2045, https://doi.org/10.1021/acs.jcim.1c00284.
- [81] T. Gupta, M. Zaki, N.M.A. Krishnan, Mausam, MatSciBERT: a materials domain language model for text mining and information extraction, npj Comput. Mater. 8

(2022) 102, https://doi.org/10.1038/s41524-022-00784-w.

- [82] A. Trewartha, N. Walker, H. Huo, S. Lee, K. Cruse, J. Dagdelen, A. Dunn, K.A. Persson, G. Ceder, A. Jain, Quantifying the advantage of domain-speciﬁc pretraining on named entity recognition tasks in materials science, Patterns 3 (2022) 100488, https://doi.org/10.1016/j.patter.2022.100488.
- [83] S. Huang, J.M. Cole, BatteryBERT: a pretrained language model for battery database enhancement, J. Chem. Inf. Model. 62 (2022) 6365–6377, https:// doi.org/10.1021/acs.jcim.2c00035.
- [84] P. Shetty, A.C. Rajan, C. Kuenneth, S. Gupta, L.P. Panchumarti, L. Holm, C. Zhang, R. Ramprasad, A general-purpose material property data extraction pipeline from large polymer corpora using natural language processing, npj Comput. Mater. 9

(2023) 52, https://doi.org/10.1038/s41524-023-01003-w.

- [85] J. Ock, C. Guntuboina, A. Barati Farimani, Catalyst energy prediction with CatBERTa: unveiling feature exploration strategies through large language models, ACS Catal. 13 (2023) 16032–16044, https://doi.org/10.1021/ acscatal.3c04956.
- [86] A.N. Rubungo, C. Arnold, B.P. Rand, A.B. Dieng, LLM-prop: predicting physical and electronic properties of crystalline solids from their text descriptions, arXiv: 2310.14029, https://doi.org/10.48550/arxiv.2310.14029, 2023.
- [87] Z. Zhao, D. Ma, L. Chen, L. Sun, Z. Li, Y. Xia, B. Chen, H. Xu, Z. Zhu, S. Zhu, S. Fan, G. Shen, K. Yu, X. Chen, ChemDFM: a large language foundation model for chemistry, arXiv:2401.14818, https://doi.org/10.48550/arxiv.2401.14818, 2024.
- [88] N. Gruver, A. Sriram, A. Madotto, A.G. Wilson, C.L. Zitnick, Z. Ulissi, Fine-tuned language models generate stable inorganic materials as text, arXiv:2402.04379, https://doi.org/10.48550/arxiv.2402.04379, 2024.
- [89] D. Zhang, W. Liu, Q. Tan, J. Chen, H. Yan, Y. Yan, J. Li, W. Huang, X. Yue, W. Ouyang, D. Zhou, S. Zhang, M. Su, S. Zhong, Y. Li, ChemLLM: a chemical large language model, arXiv:2402.06852, https://doi.org/10.48550/arxiv.2402.06852, 2024.
- [90] B. Yu, F.N. Baker, Z. Chen, X. Ning, H. Sun, LlaSMol: advancing large language models for chemistry with a large-scale, comprehensive, arXiv:2402.09391, HighQuality Instruction Tuning Dataset (2024) 09391, https://doi.org/10.48550/ arxiv.2402.09391.
- [91] C. Edwards, C. Zhai, H. Ji, Text2Mol: cross-modal molecule retrieval with natural language queries, in: Proceedings of the 2021 Conference on Empirical Methods in


- Natural Language Processing, 2021, pp. 595–607. Association for Computational Linguistics, Online and Punta Cana, Dominican Republic, https://aclanthology.org /2021.emnlp-main.47.
- [92] Z. Zeng, Y. Yao, Z. Liu, M. Sun, A deep-learning system bridging molecule structure and biomedical text with comprehension comparable to human professionals, Nat. Commun. 13 (2022) 862, https://doi.org/10.1038/s41467022-28494-3.
- [93] C. Edwards, T. Lai, K. Ros, G. Honke, K. Cho, H. Ji, Translation between molecules and natural language, in: Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing, Association for Computational Linguistics, Abu Dhabi, United Arab Emirates, 2022, pp. 375–413. https://aclanth ology.org/2022.emnlp-main.26.
- [94] B. Su, D. Du, Z. Yang, Y. Zhou, J. Li, A. Rao, H. Sun, Z. Lu, J.-R. Wen, A molecular multimodal foundation model associating molecule graphs with natural language, arXiv:2209.05481, https://doi.org/10.48550/arxiv.2209.05481, 2022.
- [95] S. Liu, W. Nie, C. Wang, J. Lu, Z. Qiao, L. Liu, J. Tang, C. Xiao, A. Anandkumar, Multi-modal molecule structure–text model for text-based retrieval and editing, Nat. Mach. Intell. 5 (2023) 1447–1457. https://doi.org/10.1038/s42256-02 3-00759-6.
- [96] H. Zhao, S. Liu, C. Ma, H. Xu, J. Fu, Z.-H. Deng, L. Kong, Q. Liu, GIMLET: a uniﬁed graph-text model for instruction-based molecule zero-shot learning, arXiv: 2306.13089, https://doi.org/10.48550/arxiv.2306.13089, 2023.
- [97] Y. Luo, K. Yang, M. Hong, X.Y. Liu, Z. Nie, MolFM: a multimodal molecular foundation model, arXiv:2307.09484, https://doi.org/10.48550/arxiv.2307. 09484, 2023.
- [98] Z. Liu, S. Li, Y. Luo, H. Fei, Y. Cao, K. Kawaguchi, X. Wang, T.-S. Chua, MolCA: molecular graph-language modeling with cross-modal projector and uni-modal adapter, in: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing, Association for Computational Linguistics, Singapore, 2023, pp. 15623–15638. https://aclanthology.org/2023.emnlp-main.966.
- [99] H. Cao, Z. Liu, X. Lu, Y. Yao, Y. Li, InstructMol: multi-modal integration for building a versatile and reliable molecular assistant in drug discovery, arXiv: 2311.16208, https://doi.org/10.48550/arxiv.2311.16208, 2023.
- [100] S. Li, Z. Liu, Y. Luo, X. Wang, X. He, K. Kawaguchi, T.-S. Chua, Q. Tian, Towards 3D molecule-text interpretation in language models, arXiv:2401.13923, htt ps://doi.org/10.48550/arxiv.2401.13923, 2024.
- [101] P. Liu, Y. Ren, J. Tao, Z. Ren, GIT-Mol: a multi-modal large language model for molecular science with graph, image, and text, Comput. Biol. Med. 171 (2024) 108073, https://doi.org/10.1016/j.compbiomed.2024.108073.
- [102] S. Wang, Y. Guo, Y. Wang, H. Sun, J. Huang, SMILES-BERT: large scale unsupervised pre-training for molecular property prediction, in: Proceedings of the 10th ACM International Conference on Bioinformatics, Computational Biology and Health Informatics, ACM, Niagara Falls, NY USA, 2019, pp. 429–436. https:// dl.acm.org/doi/10.1145/3307339.3342186.
- [103] Ł. Maziarka, T. Danel, S. Mucha, K. Rataj, J. Tabor, S. Jastrzębski, Molecule attention transformer, arXiv:2002.08264, https://doi.org/10.48550/arxiv.2002. 08264, 2020.
- [104] S. Chithrananda, G. Grand, B. Ramsundar, ChemBERTa: large-scale self-supervised pretraining for molecular property prediction, arXiv:2010.09885, https://doi. org/10.48550/arxiv.2010.09885, 2020.
- [105] B. Fabian, T. Edlich, H. Gaspar, M. Segler, J. Meyers, M. Fiscato, M. Ahmed, Molecular representation learning with language models and domain-relevant auxiliary tasks, arXiv:2011.13230, https://doi.org/10.48550/arxiv.2011.13230, 2020.
- [106] P. Schwaller, B. Hoover, J.-L. Reymond, H. Strobelt, T. Laino, Extraction of organic chemistry grammar from unsupervised learning of chemical reactions, Sci. Adv. 7

(2021) eabe4166, https://doi.org/10.1126/sciadv.abe4166.

- [107] P. Schwaller, D. Probst, A.C. Vaucher, V.H. Nair, D. Kreutter, T. Laino, J.L. Reymond, Mapping the space of chemical reactions using attention-based neural networks, Nat. Mach. Intell. 3 (2021) 144–152, https://doi.org/10.1038/s42256020-00284-w.
- [108] J. Ross, B. Belgodere, V. Chenthamarakshan, I. Padhi, Y. Mroueh, P. Das, Largescale chemical language representations capture molecular structure and properties, Nat. Mach. Intell. 4 (2022) 1256–1264, https://doi.org/10.1038/ s42256-022-00580-7.
- [109] R. Irwin, S. Dimitriadis, J. He, E.J. Bjerrum, Chemformer: a pre-trained transformer for computational chemistry, Mach. Learn, Sci. Technol. 3 (2022) 015022, https://doi.org/10.1088/2632-2153/ac3ffb.
- [110] Ł. Maziarka, D. Majchrowski, T. Danel, P. Gainski, J. Tabor, I. Podolak, P. Morkisz, S. Jastrzębski, Relative molecule self-attention transformer, J. Cheminf. 16 (2024) 3, https://doi.org/10.1186/s13321-023-00789-7.
- [111] V. Bagal, R. Aggarwal, P.K. Vinod, U.D. Priyakumar, MolGPT: molecular generation using a transformer-decoder model, J. Chem. Inf. Model. 62 (2022) 2064–2076, https://doi.org/10.1021/acs.jcim.1c00600.
- [112] J. Lu, Y. Zhang, Uniﬁed deep learning model for multitask reaction predictions with explanation, J. Chem. Inf. Model. 62 (2022) 1376–1387, https://doi.org/ 10.1021/acs.jcim.1c01467.
- [113] N.C. Frey, R. Soklaski, S. Axelrod, S. Samsi, R. Gomez-Bombarelli, C.W. Coley, V. Gadepally, Neural scaling of deep chemical models, Nat. Mach. Intell. 5 (2023) 1297–1305, https://doi.org/10.1038/s42256-023-00740-3.
- [114] C. Xu, Y. Wang, A. Barati Farimani, TransPolymer: a Transformer-based language model for polymer property predictions, npj Comput. Mater. 9 (2023) 64, https:// doi.org/10.1038/s41524-023-01016-5.
- [115] C. Kuenneth, R. Ramprasad, polyBERT: a chemical language model to enable fully machine-driven ultrafast polymer informatics, Nat. Commun. 14 (2023) 4099, https://doi.org/10.1038/s41467-023-39868-6.


- [116] H. Abdel-Aty, I.R. Gould, Large-scale distributed training of transformers for chemical ﬁngerprinting, J. Chem. Inf. Model. 62 (2022) 4852–4862, https:// doi.org/10.1021/acs.jcim.2c00715.
- [117] J. Chang, J.C. Ye, Bidirectional generation of structure and properties through a single molecular foundation model, Nat. Commun. 15 (2024) 2323, https:// doi.org/10.1038/s41467-024-46440-3.
- [118] G. Chilingaryan, H. Tamoyan, A. Tevosyan, N. Babayan, L. Khondkaryan, K. Hambardzumyan, Z. Navoyan, H. Khachatrian, A. Aghajanyan, BARTSmiles: generative masked language models for molecular representations, arXiv: 2211.16349, https://doi.org/10.48550/arxiv.2211.16349, 2022.
- [119] Y. Fang, N. Zhang, Z. Chen, L. Guo, X. Fan, H. Chen, Domain-agnostic molecular generation with chemical feedback, arXiv:301.11259, https://doi.org/10.4855 0/arxiv.2301.11259, 2024.
- [120] A. Yüksel, E. Ulusoy, A. Ünlü, T. Dogan, SELFormer: molecular representation learning via SELFIES language models, arXiv:2304.04662, https://doi.org/10. 48550/arxiv.2304.04662, 2023.
- [121] H. Qiu, L. Liu, X. Qiu, X. Dai, X. Ji, Z.-Y. Sun, PolyNC: a natural and chemical language model for the prediction of uniﬁed polymer properties, Chem. Sci. 15

(2024) 534–544, https://doi.org/10.1039/D3SC05079C.

- [122] S. Tian, X. Jiang, W. Wang, Z. Jing, C. Zhang, C. Zhang, T. Lookman, Y. Su, Steel design based on a large language model, Acta Mater. 285 (2025) 120663, https:// doi.org/10.1016/j.actamat.2024.120663.
- [123] M. Geva, R. Schuster, J. Berant, O. Levy, Transformer feed-forward layers are keyvalue memories, arXiv:2012.14913, https://doi.org/10.48550/arxiv.2012.14913, 2021.
- [124] J. White, Q. Fu, S. Hays, M. Sandborn, C. Olea, H. Gilbert, A. Elnashar, J. SpencerSmith, D.C. Schmidt, A prompt pattern catalog to enhance prompt engineering with ChatGPT, arXiv:2302.11382, https://doi.org/10.48550/arxiv.2302.11382, 2023.
- [125] V. Lialin, V. Deshpande, X. Yao, A. Rumshisky, Scaling down to scale up: a guide to parameter-efﬁcient ﬁne-tuning, arXiv:2303.15647, https://doi.org/10.4855 0/arxiv.2303.15647, 2024.
- [126] T. Xie, Y. Wan, W. Huang, Z. Yin, Y. Liu, S. Wang, Q. Linghu, C. Kit, C. Grazian, W. Zhang, I. Razzak, B. Hoex, Darwin series: domain speciﬁc large language models for natural science, arXiv:2308.13565, https://doi.org/10.48550/arxiv.2 308.13565, 2023.
- [127] L. Ouyang, J. Wu, X. Jiang, D. Almeida, C.L. Wainwright, P. Mishkin, C. Zhang, S. Agarwal, K. Slama, A. Ray, J. Schulman, J. Hilton, F. Kelton, L. Miller, M. Simens, A. Askell, P. Welinder, P. Christiano, J. Leike, R. Lowe, Training language models to follow instructions with human feedback, arXiv:2203.02155, https://doi.org/10.48550/arxiv.2203.02155, 2022.
- [128] S.-A. Rebufﬁ, H. Bilen, A. Vedaldi, Learning multiple visual domains with residual adapters, arXiv:1705.08045, https://doi.org/10.48550/arxiv.1705.08045, 2017.
- [129] N. Houlsby, A. Giurgiu, S. Jastrzebski, B. Morrone, Q. de Laroussilhe, A. Gesmundo, M. Attariyan, S. Gelly, Parameter-efﬁcient transfer learning for NLP, arXiv:1902.00751, https://doi.org/10.48550/arxiv.1902.00751, 2019.
- [130] X. Liu, K. Ji, Y. Fu, W.L. Tam, Z. Du, Z. Yang, J. Tang, P-tuning v2: prompt tuning can Be comparable to ﬁne-tuning universally across scales and tasks, arXiv: 2110.07602, https://doi.org/10.48550/arxiv.2110.07602, 2022.
- [131] X.L. Li, P. Liang, Preﬁx-tuning: optimizing continuous prompts for generation, arXiv:2101.00190, https://doi.org/10.48550/arxiv.2101.00190, 2021.
- [132] B. Lester, R. Al-Rfou, N. Constant, The power of scale for parameter-efﬁcient prompt tuning, arXiv:2104.08691, https://doi.org/10.48550/arxiv.2104.08691, 2021.
- [133] E.J. Hu, Y. Shen, P. Wallis, Z. Allen-Zhu, Y. Li, S. Wang, L. Wang, W. Chen, LoRA: low-rank adaptation of large language models, arXiv:2106.09685, https://doi. org/10.48550/arxiv.2106.09685, 2021.
- [134] P. Lewis, E. Perez, A. Piktus, F. Petroni, V. Karpukhin, N. Goyal, H. Küttler, M. Lewis, W. Yih, T. Rockt€aschel, S. Riedel, D. Kiela, Retrieval-augmented generation for knowledge-intensive NLP tasks, arXiv:2005.11401, https://doi. org/10.48550/arxiv.2005.11401, 2021.
- [135] A. Leto, C. Aguerrebere, I. Bhati, T. Willke, M. Tepper, V.A. Vo, Toward optimal search and retrieval for RAG, arXiv:2411.07396, https://doi.org/10.4855 0/arxiv.2411.07396, 2024.
- [136] Z. Wu, O. Zhang, X. Wang, L. Fu, H. Zhao, J. Wang, H. Du, D. Jiang, Y. Deng, D. Cao, C.-Y. Hsieh, T. Hou, Leveraging language model for advanced multiproperty molecular optimization via prompt engineering, Nat. Mach. Intell. 6

(2024) 1359–1369, https://doi.org/10.1038/s42256-024-00916-5.

- [137] A. Merchant, S. Batzner, S.S. Schoenholz, M. Aykol, G. Cheon, E.D. Cubuk, Scaling deep learning for materials discovery, Nature 624 (2023) 80–85, https://doi.org/ 10.1038/s41586-023-06735-9.
- [138] H. Li, R. Zhang, Y. Min, D. Ma, D. Zhao, J. Zeng, A knowledge-guided pre-training framework for improving molecular representation learning, Nat. Commun. 14

(2023) 7568, https://doi.org/10.1038/s41467-023-43214-1.

- [139] Y. Zhang, X. Chen, B. Jin, S. Wang, S. Ji, W. Wang, J. Han, A comprehensive survey of scientiﬁc large language models and their applications in scientiﬁc discovery, arXiv:2406.10833, https://doi.org/10.48550/arXiv.2406.10833, 2024.
- [140] W. Zhang, Q. Wang, X. Kong, J. Xiong, S. Ni, D. Cao, B. Niu, M. Chen, Y. Li, R. Zhang, Y. Wang, L. Zhang, X. Li, Z. Xiong, Q. Shi, Z. Huang, Z. Fu, M. Zheng, Fine-tuning large language models for chemical text mining, Chem. Sci. 15 (2024) 10600–10611, https://doi.org/10.1039/D4SC00924J.
- [141] H. Yang, PIEKM: ML-based procedural information extraction and knowledge management system for materials science literature, in: Proceedings of the 2nd Conference of the Asia-Paciﬁc Chapter of the Association for Computational Linguistics and the 12th International Joint Conference on Natural Language


- Processing: System Demonstrations, Association for Computational Linguistics, Taipei, 2022, pp. 57–62.
- [142] M.P. Polak, D. Morgan, Extracting accurate materials data from research papers with conversational language models and prompt engineering, Nat. Commun. 15

(2024) 1569, https://doi.org/10.1038/s41467-024-45914-8.

- [143] J. Dagdelen, A. Dunn, S. Lee, N. Walker, A.S. Rosen, G. Ceder, K.A. Persson, A. Jain, Structured information extraction from scientiﬁc text with large language models, Nat. Commun. 15 (2024) 1418, https://doi.org/10.1038/s41467-02445563-x.
- [144] Y. Kang, J. Kim, ChatMOF: an artiﬁcial intelligence system for predicting and generating metal-organic frameworks using large language models, Nat. Commun. 15 (2024) 4705, https://doi.org/10.1038/s41467-024-48998-4.
- [145] C. Zeni, R. Pinsler, D. Zügner, A. Fowler, M. Horton, X. Fu, S. Shysheya, J. Crabbe, L. Sun, J. Smith, B. Nguyen, H. Schulz, S. Lewis, C.-W. Huang, Z. Lu, Y. Zhou, H. Yang, H. Hao, J. Li, R. Tomioka, T. Xie, MatterGen: a generative model for inorganic materials design, arXiv:2312.03687, https://doi.org/10.48550/arxiv.2 312.03687, 2024.
- [146] J. Ross, B. Belgodere, V. Chenthamarakshan, I. Padhi, Y. Mroueh, P. Das, Largescale chemical language representations capture molecular structure and properties, Nat. Mach. Intell. 4 (2022) 1256–1264, https://doi.org/10.1038/ s42256-022-00580-7.
- [147] Y. Chen, X. Wang, X. Deng, Y. Liu, X. Chen, Y. Zhang, H. Xiao, MatterGPT: a generative transformer for multi- property inverse design of solid-state materials, arXiv:2408.07608, https://doi.org/10.48550/arxiv.2408.07608, 2024.
- [148] N.J. Szymanski, B. Rendy, Y. Fei, R.E. Kumar, T. He, D. Milsted, M.J. McDermott, M. Gallant, E.D. Cubuk, A. Merchant, H. Kim, A. Jain, C.J. Bartel, K. Persson, Y. Zeng, G. Ceder, An autonomous laboratory for the accelerated synthesis of novel materials, Nature 624 (2023) 86–91, https://doi.org/10.1038/s41586-02306734-w.
- [149] Z. Ni, Y. Li, K. Hu, K. Han, M. Xu, X. Chen, F. Liu, Y. Ye, S. Bai, MatPilot: an LLMenabled AI Materials Scientist under the Framework of Human-Machine Collaboration, arXiv:2411.08063, https://doi.org/10.48550/arxiv.2411.08063, 2024.
- [150] W. Huang, C. Wang, Y. Li, R. Zhang, L. Fei-Fei, ReKep: spatio-temporal reasoning of relational keypoint constraints for robotic manipulation, arXiv:2409.01652, htt ps://doi.org/10.48550/arxiv.2409.01652, 2024.
- [151] Z. Fu, T.Z. Zhao, C. Finn, Mobile ALOHA: learning bimanual mobile manipulation with low-cost whole-body teleoperation, arXiv:2401.02117, https://doi.org/10.


48550/arxiv.2401.02117, 2024.

- [152] K. Darvish, M. Skreta, Y. Zhao, N. Yoshikawa, S. Som, M. Bogdanovic, Y. Cao, H. Hao, H. Xu, A. Aspuru-Guzik, A. Garg, F. Shkurti, ORGANA: a robotic assistant for automated chemistry experimentation and characterization, arXiv: 2401.06949, https://doi.org/10.48550/arxiv.2401.06949, 2024.
- [153] B. Burger, P.M. Maffettone, V.V. Gusev, C.M. Aitchison, Y. Bai, X. Wang, X. Li, B.M. Alston, B. Li, R. Clowes, N. Rankin, B. Harris, R.S. Sprick, A.I. Cooper, A mobile robotic chemist, Nature 583 (2020) 237–241, https://doi.org/10.1038/ s41586-020-2442-2.
- [154] J. Su, J. Li, N. Guo, X. Peng, J. Yin, J. Wang, P. Lyu, Z. Luo, K. Mouthaan, J. Wu, C. Zhang, X. Wang, J. Lu, Intelligent synthesis of magnetic nanographenes via chemist-intuited atomic robotic probe, Nat. Synth. 3 (2024) 466–476, https:// doi.org/10.1038/s44160-024-00488-7.
- [155] A.L. Dias, T. Rodrigues, Chemistry automated by large language models, Nature 624 (2023) 530–531, https://doi.org/10.1038/s41586-023-06792-0.
- [156] K.J. Kanarik, W.T. Osowiecki, Y. Lu, D. Talukder, N. Roschewsky, S.N. Park, M. Kamon, D.M. Fried, R.A. Gottscho, Human–machine collaboration for improving semiconductor process development, Nature 616 (2023) 707–711, https://doi.org/10.1038/s41586-023-05773-7.
- [157] D.A. Boiko, R. MacKnight, B. Kline, G. Gomes, Autonomous chemical research with large language models, Nature 624 (2023) 570–578, https://doi.org/ 10.1038/s41586-023-06792-0.
- [158] Z. Fei, M. Fan, J. Huang, A-jepa: joint-embedding predictive architecture can listen, arXiv:2311.15830, https://doi.org/10.48550/arxiv.2311.15830, 2023.
- [159] P. Guetschel, T. Moreau, M. Tangermann, S-JEPA: towards seamless cross-dataset transfer through dynamic spatial attention, arXiv:2403.11772, https://doi.org/10. 48550/arxiv.2403.11772, 2024.
- [160] H. Thimonier, J.L.D.M. Costa, F. Popineau, A. Rimmel, B.-L. Doan, T-JEPA: augmentation-free self-supervised learning for tabular data, arXiv:2410.05016, htt ps://doi.org/10.48550/arxiv.2410.05016, 2024.
- [161] G.E. Karniadakis, I.G. Kevrekidis, L. Lu, P. Perdikaris, S. Wang, L. Yang, Physicsinformed machine learning, Nat. Rev. Phys. 3 (2021) 422–440, https://doi.org/ 10.1038/s42254-021-00314-5.
- [162] K. Kashinath, M. Mustafa, A. Albert, J. Wu, C. Jiang, S. Esmaeilzadeh, K. Azizzadenesheli, R. Wang, A. Chattopadhyay, A. Singh, Physics-informed machine learning: case studies for weather and climate modelling, Philos. Trans. R. Soc. A 379 (2021) 20200093, https://doi.org/10.1098/rsta.2020.0093.
- [163] J.-L. Wu, H. Xiao, E. Paterson, Physics-informed machine learning approach for augmenting turbulence models: a comprehensive framework, Phys. Rev. Fluids 3


(2018) 074602, https://doi.org/10.1103/PhysRevFluids.3.074602.

