# arXiv:2502.13107v3[cs.AI]26 Apr 2025

## MatterChat: A Multi-Modal LLM for Material Science

##### Yingheng Tang1*†, Wenbin Xu2*†, Jie Cao3, Weilu Gao4*, Steven Farrell2, Benjamin Erichson5,6, Michael W. Mahoney5,6,7, Andy Nonaka1, Zhi Yao1*

1Applied Mathematics and Computational Research Division, Lawrence Berkeley National Laboratory, Berkeley, CA, USA.

- 2National Energy Research Scientific Computing Center, Lawrence Berkeley National Laboratory, Berkeley, CA, USA.
- 3NSF National AI Institute for Student-AI Teaming, University of Colorado at Boulder, Boulder, USA.


4Department of Electrical and Computer Engineering, The University of Utah, Salt Lake City, UT, USA.

5Scientific Data Division, Lawrence Berkeley National Laboratory, Berkeley, CA, USA. 6International Computer Science Institute, Berkeley, CA, USA. 7Department of Statistics, University of California at Berkeley, Berkeley, CA, USA.

*Corresponding author(s). E-mail(s): ytang4@lbl.gov; wenbinxu@lbl.gov; weilu.gao@utah.edu; jackie zhiyao@lbl.gov;

†These authors contribute equally

Abstract Understanding and predicting the properties of inorganic materials is crucial for accelerating advancements in materials science and driving applications in energy, electronics, and beyond. Integrating material structure data with language-based information through multi-modal large language models (LLMs) offers great potential to support these efforts by enhancing human–AI interaction. However, a key challenge lies in integrating atomic structures at full resolution into LLMs. In this work, we introduce MatterChat, a versatile structure-aware multi-modal LLM that unifies material structural data and textual inputs into a single cohesive model. MatterChat employs a bridging module to effectively align a pretrained universal machine learning interatomic potential with a pretrained LLM, reducing training costs and enhancing flexibility. Our results demonstrate that MatterChat significantly improves performance in material property prediction and human-AI interaction, surpassing general-purpose LLMs such as GPT-4. We also demonstrate its usefulness in applications such as more advanced scientific reasoning and step-by-step material synthesis.

Keywords: Foundational model, Large Language Model, Multi-Modal Learning, Inorganic Material

### 1 Introduction

In-silico material discovery and design have traditionally relied on high-fidelity first-principles methods such as density functional theory (DFT) [1] and ab-initio molecular dynamics (AIMD) [2] to accurately model atomic interactions and predict material properties. Despite their effectiveness, these methods face significant challenges due to their prohibitive computational cost, limiting their scalability for highthroughput screening across vast chemical spaces and for simulations over large length and time scales. Moreover, many advanced materials remain beyond the reach of widespread predictive theories due to a fundamental lack of mechanistic understanding. These challenges stem from the inherent complexity of their chemical composition, phase stability, and the intricate interplay of multiple order parameters, compounded by the lack of self-consistent integration between theoretical models and multi-modal experimental findings. As a result, breakthroughs in functional materials, such as new classes of correlated oxides, nitrides, and low-dimensional quantum materials, have largely been serendipitous or guided by phenomenological intuition rather than systematic, theory-driven design. Attempts to predict new materials and functionalities have often led to mixed results, with theoretically proposed systems failing to exhibit the desired properties when synthesized and tested. Achieving reliable, scalable, and predictive design of materials requires a paradigm shift.

With the rise of artificial intelligence (AI) in materials science, there has been a surge of methods aiming to overcome these limitations, ranging from machine learning (ML) surrogate models [3, 4], ML interatomic potentials (MLIPs) [5–7], and generative models [8, 9]. These models enable rapid predictions, accelerate large-scale simulations, and facilitate the generation of novel materials. As a result, they have significantly advanced fields such as energy storage [10], electronics [11], catalysis [12], and biomedical applications [13]. Among these promising ML approaches, graph-based models in material science have become increasingly popular due to their versatile graph representation of atomistic systems, where each atom is represented as a node, and chemical bonds to neighboring atoms are represented as edges. Although these graph-based methods have shown success in accurately predicting material properties, they typically lack the capacity to handle tasks that require understanding scientific context, literaturebased insights, and domain-specific language [14]. In particular, these models do not support human–AI interaction through user prompts or textual descriptions, making it difficult to incorporate expert domain knowledge and user-specified requests to close the feedback loop.

This bottleneck has inspired a wave of exploration into how natural language processing (NLP), and particularly large language models (LLMs), might be leveraged to fill the gap. LLMs like BERT [15], GPT [16], and newer open-source LLMs such as Mistral [17], Llama [18] and DeepSeek [19] have shown substantial promise across different domains by interpreting and generating language. Trained on extensive datasets, these models can support some scientific tasks that require interpretive language capabilities, such as question-answering (QA) [20] and retrieving information from unstructured text sources [21]. In recent years, there has been several efforts incorporating LLM to solve material related problems [22, 23], either by leveraging pretrained LLMs or multi-modal LLMs. Unfortunately, these approaches rely on text-based representations, such as chemical formulas [22], Simplified Molecular Input Line Entry System (SMILES) strings [23, 24], textual descriptions [25], or Crystallographic Information File (CIF) [26], which lose the full resolution of atomic structures. Consequently, they exhibit inferior performance compared to pure graph-based models for predicting material properties [25], and they also potentially hinder other downstream tasks where structural information is crucial. Thanks to the steady development of MLIPs [5–7], particularly in their universal form (uMLIPs) [7], these models can now serve as atomistic pre-trained models capable of supporting a wide range of applications. The locality assumption underlying uMLIPs ensures that they effectively represent the local environment of each atom. Therefore, it is feasible to extract structural information from atom embeddings in a pretrained uMLIP.

In this work, we present MatterChat, a multi-modal large language model designed for materials science. MatterChat integrates material structure data with textual user queries, combining insights from materials science and NLP. It enhances the capabilities of large language models by overcoming their traditional limitations in quantitative predictions and improving the handling of scientific material-related tasks, as demonstrated through comparisons with other LLMs. MatterChat also maintains robust human–AI interaction capabilities, offering an intuitive interface for complex queries, compared to physical ML models. Furthermore, by leveraging deep, embedded knowledge from state-of-the-art pretrained LLMs, MatterChat enables advanced scientific reasoning and synthesis process guidance. The embedding visualization analysis indicates that MatterChat effectively preserves structure and property information.

This has guided the adoption of a multi-modal Retrieval-Augmented Generation (RAG) approach that can enhance MatterChat’s robustness during material task inference.

### 2 Results

#### 2.1 Overview of MatterChat

- Figure 1(a) presents the architecture of MatterChat, designed to process both material structures and user requests as inputs to generate text-based outputs for tasks such as material property prediction, structural analysis, and descriptive language generation. MatterChat consists of three core components: the Material Processing Branch, the Language Processing Branch, and the Bridge Model. The Material Processing Branch extracts atomic-level embeddings from material structures represented as graphs. These embeddings are then processed by the Bridge Model, which employs trainable queries to produce language model-compatible embeddings. Finally, the Language Processing Branch processes the user’s text-based prompt (e.g., “What is the formation energy of the material?”) into language embeddings. These embeddings are then combined with the query embeddings generated by the Bridge Model and fed into the LLM to produce the final output in text format. Below, we provide the details of each component.

Material Processing Branch. The Material Processing Branch encodes material structures as graphs that capture the atomic local environment. We use CHGNet [27], a state-of-the-art graph-based uMLIP model designed for crystal structures, to process these graphs. CHGNet is pretrained on a diverse dataset of materials, encompassing a wide range of symmetries, compositions, and bonding types, enabling it to effectively model complex atomic interactions and structural details. By capturing essential compositional features, such as atomic types and chemical bonds, along with spatial features like bond angles, CHGNet generates high-quality atom embeddings that are both physically meaningful and well-suited for downstream tasks.

Language Processing Branch. The Language Processing Branch is used to process user’s text-based prompts, such as requests for property predictions, chemical formulas, space group information, or other material characteristics. We use the Mistral 7B LLM [17], one of the latest open-source LLMs, chosen for its exceptional performance across a wide range of scientific and non-scientific tasks. This branch processes each prompt, transforming it into dense embeddings that capture the semantic content of the inquiry. These embeddings are then combined with the query embeddings processed by the bridge model using a structured fusion approach, allowing the model to effectively incorporate both textual and material information. This integration enables the LLM to generate precise and contextually relevant responses tailored to the user’s specific material-related prompts.

Bridge Model. To facilitate the integration between atom embeddings and the Language Processing Branch, we developed a bridge model inspired by the BLIP2 architecture [28] based on a multi-layer transformer framework. This bridge model includes 32 trainable query vectors that interact with atom embeddings using an alternating attention mechanism. Cross-attention in even-numbered layers extracts key features from the atom embeddings, while self-attention in odd-numbered layers enhances representational depth. This approach refines the atom embeddings into query embeddings that are most connected to text, as shown in Figure 1a. Finally, these refined representations are mapped to LLM-compatible embeddings via a linear projection layer.

Figures 1(b)-(c) provide an overview of the dataset of crystalline structures used in our training set.

- Figure 1(b) visualizes the material distribution on the periodic table, highlighting that the dataset evenly spans a diverse range of elements up to Plutonium. Figure 1(c) depicts the distribution of crystalline structures by space group across the dataset. The dataset was curated from the Materials Project [29] and contains 142,899 material structures. For each structure, we generated a corresponding text-based dataset encompassing 12 tasks: 3 descriptive tasks (chemical formula, space group, and crystal system) and 9 property prediction tasks. These property prediction tasks include metallicity, direct bandgap, stability, experimental observation (Exp Ob), magnetic status (Is Magnetic), magnetic order, formation energy, energy above the hull, and bandgap, as summarized in Figure 1(a). Further details regarding the training scheme, hyper-parameters, and dataset curation are provided in the Methods section.


#### 2.2 Multi-modal material task interactions with MatterChat

- Figure 2 illustrates examples of human-AI interaction with MatterChat across a diverse range of material property prediction and analysis tasks. It shows MatterChat’s ability to effectively address a broad


spectrum of user prompts ranging from fundamental material attributes (e.g., chemical formulas, space groups and crystal system) to complex material properties (e.g., thermal stability, bandgaps, formation energies and energy above the hull). Figure 2(a) shows three interactive examples of material property prompts from randomly selected materials from the Material Project Dataset. The top left panel presents a human-AI query interface with MatterChat for the material with mp-id of “mp-1001021”. It provides a detailed profile including the chemical formula Y2Zn4Se2, its crystalline structure denoted by the space group Fd-3m, and electronic properties such as a bandgap of 0.21350 eV. The interface also addresses the material’s lack of thermal stability. The top mid panel shows the interaction example with the material with mp-id of “mp-1028281”. It provides a comprehensive breakdown of the material’s composition attributes, including its chemical formula (Mg14VSb) and its space group (Amm2). The

![image 1](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile1.png)

(a)

- • Description:
- • Chemical formula
- • Space group
- • Crystal system


• Property:

- • Direct bandgap
- • Magnetic order
- • Stability
- • Metallic
- • Magnetic
- • Bandgap
- • Formation energy
- • Energy above hull


![image 2](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile2.png)

![image 3](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile3.png)

Q: What is the chemical formula of this material?

Q: What is the formation energy of this material?

A: The chemical formula of this material is Li32Ti3Cr13O48.

Q: Is this material stable or not?

A: The formation energy of this material is -2.38709 eV/atom.

A: This material is not stable.

![image 4](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile4.png)

(b) (c)

- Fig. 1 Overview of MatterChat: a modular multi-modal LLM for material-based question-answering. (a) MatterChat architecture: The system includes a material encoder that generates atom embeddings and a LLM that processes language data. These components are connected by a trainable bridge model, which aligns material structure with natural language to support tasks such as material description and property prediction. (b) Elemental distribution across 142,899 compositions, representing the dataset’s compositional diversity. (c) Dataset distribution shown by space groups (outer ring) and crystal Systems (inner ring), illustrating structural variation within the dataset.


![image 5](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile5.png)

![image 6](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile6.png)

![image 7](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile7.png)

![image 8](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile8.png)

###### MatterChat interaction examples on material properties

- (a)

![image 9](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile9.png)

![image 10](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile10.png)

- (b)


![image 11](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile11.png)

![image 12](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile12.png)

![image 13](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile13.png)

![image 14](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile14.png)

![image 15](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile15.png)

![image 16](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile16.png)

###### mp-1001021 mp-1028281 mp-10198

![image 17](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile17.png)

![image 18](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile18.png)

![image 19](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile19.png)

![image 20](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile20.png)

![image 21](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile21.png)

![image 22](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile22.png)

![image 23](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile23.png)

![image 24](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile24.png)

![image 25](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile25.png)

![image 26](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile26.png)

![image 27](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile27.png)

![image 28](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile28.png)

![image 29](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile29.png)

![image 30](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile30.png)

![image 31](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile31.png)

![image 32](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile32.png)

![image 33](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile33.png)

![image 34](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile34.png)

![image 35](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile35.png)

![image 36](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile36.png)

![image 37](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile37.png)

![image 38](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile38.png)

![image 39](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile39.png)

Can you describe this material in term of its chemical formula, space group and crystal system?

Can you describe this material in term of its chemical formula and space group?

![image 40](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile40.png)

What is the chemical formula of this material?

![image 41](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile41.png)

![image 42](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile42.png)

![image 43](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile43.png)

The chemical formula of this material is described as Mg14VSb. The space group of this material is described as Amm2.

![image 44](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile44.png)

![image 45](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile45.png)

![image 46](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile46.png)

![image 47](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile47.png)

The chemical formula of this material is Mn3PdN. The space group is Pm-3m and the crystal system is cubic.

![image 48](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile48.png)

![image 49](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile49.png)

![image 50](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile50.png)

![image 51](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile51.png)

![image 52](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile52.png)

The material has the chemical formula of Y2Zn4Se2.

![image 53](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile53.png)

![image 54](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile54.png)

![image 55](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile55.png)

![image 56](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile56.png)

![image 57](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile57.png)

![image 58](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile58.png)

![image 59](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile59.png)

![image 60](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile60.png)

Is this material magnetic or nonmagnetic?

![image 61](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile61.png)

![image 62](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile62.png)

![image 63](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile63.png)

![image 64](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile64.png)

What is the space group of this material?

Does the material have direct or indirect bandgap?

![image 65](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile65.png)

![image 66](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile66.png)

![image 67](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile67.png)

![image 68](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile68.png)

![image 69](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile69.png)

![image 70](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile70.png)

![image 71](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile71.png)

![image 72](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile72.png)

![image 73](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile73.png)

![image 74](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile74.png)

This material is magnetic.

The space group of this material is Fd-3m.

The material has indirect bandgap.

![image 75](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile75.png)

![image 76](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile76.png)

![image 77](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile77.png)

![image 78](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile78.png)

![image 79](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile79.png)

![image 80](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile80.png)

![image 81](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile81.png)

![image 82](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile82.png)

![image 83](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile83.png)

![image 84](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile84.png)

Is this material metallic or not metallic?

![image 85](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile85.png)

![image 86](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile86.png)

![image 87](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile87.png)

What is the magnetic order of this material?

![image 88](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile88.png)

Is this material stable or not stable?

![image 89](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile89.png)

![image 90](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile90.png)

![image 91](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile91.png)

![image 92](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile92.png)

![image 93](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile93.png)

![image 94](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile94.png)

![image 95](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile95.png)

![image 96](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile96.png)

![image 97](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile97.png)

![image 98](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile98.png)

![image 99](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile99.png)

The magnetic order of the material is FM.

The material is metal.

![image 100](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile100.png)

The material is not stable.

![image 101](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile101.png)

![image 102](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile102.png)

![image 103](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile103.png)

![image 104](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile104.png)

![image 105](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile105.png)

![image 106](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile106.png)

![image 107](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile107.png)

![image 108](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile108.png)

What is the formation energy of this material?

![image 109](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile109.png)

![image 110](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile110.png)

![image 111](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile111.png)

![image 112](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile112.png)

What is the bandgap of this material?

What is the energy above hull of this material?

![image 113](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile113.png)

![image 114](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile114.png)

![image 115](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile115.png)

![image 116](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile116.png)

![image 117](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile117.png)

![image 118](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile118.png)

![image 119](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile119.png)

The material has a formation energy of 0.07219 eV/atom.

![image 120](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile120.png)

![image 121](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile121.png)

![image 122](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile122.png)

![image 123](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile123.png)

![image 124](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile124.png)

The energy above hull value for this material is 0.01357 eV/Atom.

The material has a bandgap of 0.23870 eV.

![image 125](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile125.png)

![image 126](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile126.png)

Formation energy prediction: MatterChat vs. other LLMs on newly discovered materials.

![image 127](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile127.png)

![image 128](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile128.png)

![image 129](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile129.png)

![image 130](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile130.png)

###### Ground Truth: -0.563 eV/atom.

Ground Truth: -0.098 eV/atom. mp-3206774

![image 131](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile131.png)

![image 132](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile132.png)

![image 133](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile133.png)

![image 134](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile134.png)

mp-3202380

![image 135](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile135.png)

![image 136](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile136.png)

The estimated formation energy is around 8.18 eV per atom.

![image 137](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile137.png)

![image 138](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile138.png)

![image 139](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile139.png)

![image 140](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile140.png)

![image 141](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile141.png)

Ef(Cd2Sb2Pb) ≈ -0.28 eV/atom.

![image 142](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile142.png)

![image 143](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile143.png)

![image 144](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile144.png)

![image 145](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile145.png)

![image 146](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile146.png)

![image 147](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile147.png)

![image 148](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile148.png)

This compound is likely to have a formation energy around -6.04 eV per atom.

![image 149](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile149.png)

![image 150](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile150.png)

This compound is likely to have a formation formation energy around -0.75 eV/atom.

![image 151](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile151.png)

![image 152](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile152.png)

![image 153](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile153.png)

![image 154](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile154.png)

![image 155](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile155.png)

![image 156](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile156.png)

Estimated formation energy: ΔH_f ≈ -0.44 eV/atom.

The formation energy value is ≈ -1.83 eV/atom.

![image 157](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile157.png)

![image 158](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile158.png)

![image 159](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile159.png)

![image 160](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile160.png)

![image 161](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile161.png)

![image 162](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile162.png)

![image 163](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile163.png)

![image 164](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile164.png)

The formation energy of the material is

The formation energy of this material is

-0.52143 eV/atom.

-0.04189 eV/atom.

- Fig. 2 MatterChat accurately predicts material properties and outperforms state-of-the-art LLMs. (a) Illustration of multi-modal material property queries using MatterChat. The model accurately interprets user prompts to predict chemical formulas, crystallographic properties, stability, electronic bandgap, magnetic order, and energy metrics of materials. The three panels demonstrate the framework’s ability to address diverse material science inquiries, showing its alignment of graph-based and textual embeddings for precise question answering. (b) Comparative evaluation of formation energy predictions for newly discovered material from GNoME [30]. Predictions from Matterchat compared against the ground truth values along with evaluations from commercial LLMs (Gemini [31], GPT-4o [32] and DeepSeek [19]). The results show the accuracy and stability of the Matterchat in quantitative material evaluation tasks, which closely aligns with the ground truth, demonstrating its ability to integrate material graph embeddings for precise property prediction.


interaction further predicts that the material is both magnetic and metallic, and its formation energy is estimated at 0.05912 eV/atom. The top right panel provides an interaction example with MatterChat of the material with mp-id of “mp-10198”. This panel informs the user’s query about the chemical composition Mn3PdN and its cubic crystal structure, with the space group classified as Pm-3m. Additionally, it estimated that the material possesses an indirect bandgap, which is an important characteristic for applications in electronics. MatterChat also accurately predicts the ferromagnetic (FM) magnetic behaviors that the material exhibits, and it mentions its energy above hull value at 0.03571 eV/atom. In the bottom panel, we present a comparative evaluation of MatterChat’s performance on formation energy evaluation tasks for newly discovered materials from GNoME [30]. The model was compared against commercial LLMs, Gemini [31], GPT-4o [32] and DeepSeek [19]. The results show MatterChat’s superior accuracy in estimating formation energies, consistently delivering predictions closer to the ground truths. For example, MatterChat’s formation energy predictions for “mp-3202380” and “mp-3206774” show a remarkable alignment with the ground truth values. These results demonstrate MatterChat’s ability to integrate structural and textual data seamlessly for a wide range of material property tasks.

- Figure 3 demonstrates MatterChat’s advanced reasoning capabilities, showing how it leverages the comprehensive knowledge base of LLMs to address complex materials science challenges. By using a


(a) (b) (c)

![image 165](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile165.png)

![image 166](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile166.png)

![image 167](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile167.png)

![image 168](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile168.png)

![image 169](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile169.png)

![image 170](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile170.png)

![image 171](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile171.png)

![image 172](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile172.png)

![image 173](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile173.png)

![image 174](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile174.png)

![image 175](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile175.png)

![image 176](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile176.png)

![image 177](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile177.png)

Can you describe this material in terms of its chemical formula and space group?

What is this material in terms of chemical formula and space group?

![image 178](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile178.png)

![image 179](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile179.png)

What is the chemical formula of this material?

![image 180](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile180.png)

![image 181](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile181.png)

![image 182](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile182.png)

The material is Y3Fe5O12, with a la3d space group.

The material has the chemical formula of GaN. It has P63mc space group.

The material has the chemical formula of Si.

![image 183](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile183.png)

![image 184](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile184.png)

![image 185](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile185.png)

![image 186](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile186.png)

Can you provide the detailed step by step synthesis for this material?

![image 187](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile187.png)

![image 188](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile188.png)

What is the space group of this material?

Can you provide the detailed step by step synthesis for this material?

![image 189](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile189.png)

The space group of this material is Cmcm.

Here's a simplified version of the MOCVD process:

Creating Yttrium Iron Garnet (Y3Fe5O12, YIG) typically involves a solid-state reaction method. Here's a simplified step-by-step procedure:

![image 190](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile190.png)

![image 191](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile191.png)

![image 192](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile192.png)

![image 193](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile193.png)

Is this material stable or not?

- 1. Preparation of the Substrate: Silicon carbide (SiC) or sapphire (Al2O3) wafers are commonly used as substrates. They are cleaned ultrasonically with a detergent, rinsed with deionized water, and then dried.
- 2. The MOCVD reactor is heated to a temperature between 800-1000°C. The substrate is placed on a heated susceptor within the reactor.
- 3. Gallium and Nitrogen Source Preparation: Trimethylgallium (TMG, (CH3)3Ga) and ammonia (NH3) are typically used as the gallium and nitrogen sources, respectively.
- 4. Gallium and Nitrogen Introduction: TMG and NH3 are introduced into the reactor. The gases react on the heated substrate to form GaN.
- 5. Carrier Gas: A hydrogen (H2) or nitrogen (N2) carrier gas is used to transport the reactants into the reactor and to carry away the by-products.
- 6. Growth Time: The reaction is allowed to proceed for a certain amount of time, depending on the desired thickness and quality of the GaN layer.
- 7. Cool Down and-Situ Analysis: After growth, the reactor is cooled down. The quality of the grown GaN layer can be analyzed using techniques such as X-ray diffraction (XRD), scanning electron microscopy (SEM), and photoluminesc.


- 1. Preparation of starting materials:

- - Yttrium oxide (Y2O3)
- - Iron(III) oxide (Fe2O3)


- 2. Weigh the required amounts of Y2O3 and Fe2O3. A common ratio for YIG is 3:5, so for 10 grams of YIG, you would need 6.67 grams of Y2O3 and 13.33 grams of Fe2O3.
- 3. Mix the weighed Y2O3 and Fe2O3 powders thoroughly in a ceramic crucible.
- 4. Heat the mixture in a muffle furnace at 1200°C for 12 hours to ensure complete reaction and formation of YIG. The heating and cooling rates should be slow (around 5°C/min) to prevent cracking.
- 5. After cooling to room temperature, grind the obtained YIG powder using a ball mill or mortar and pestle.
- 6. Repeat steps 4 and 5 if necessary to achieve a higher purity or smaller particle size.
- 7. Characterize the synthesized YIG powder using techniques such as X-ray diffraction (XRD), scanning electron microscopy (SEM), and energy-dispersive X-ray spectroscopy (EDX) to confirm its composition and purity.


![image 194](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile194.png)

The material is not stable.

![image 195](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile195.png)

![image 196](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile196.png)

Why is it not stable?

![image 197](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile197.png)

The material you're referring to, Si with the space group Cmcm, is not a stable form of silicon. Silicon typically crystallizes in the diamond structure (space group Fd3m) at room temperature and pressure. The Cmcm structure is metastable and can be obtained under high pressure and temperature conditions, but it is not thermodynamically stable at standard conditions. This means that if left alone, it would transform into the more stable diamond structure over time.

- Fig. 3 MatterChat has the ability to solve more sophisticated tasks inherited from the pretrained LLM. (a) Material property query for silicon (Si), including its chemical formula, space group, stability, and the reasoning for why it is not stable under standard conditions. (b) Highlights a material query for Gallium Nitride (GaN), providing its chemical formula, space group, and a step-by-step synthesis procedure using methods like HVPE, MOCVD, and MBE.


- (c) Material query interaction, Yttrium Iron Garnet (YIG, Y3Fe5O12), detailing its chemical formula, space group, and a simplified step-by-step synthesis procedure using the solid-state reaction method.


multi-modal query system, MatterChat effectively combines material structure data with textual reasoning. This integration facilitates a working memory scheme [33], which enables the model to provide domain-specific reasoning, detailed synthesis procedures, and explanations that are deeply grounded in the structural properties of materials. Panel (a) presents the chat log for silicon with the space group of cmcm. MatterChat not only retrieves the chemical formula and correct space group, but it also provides a rationale for the structural instability of this silicon phase. The model explains that the cmcm space group exhibits higher energy per unit cell compared to the thermodynamically stable cubic diamond structure of silicon, making it less likely to occur under standard conditions. Panel (b) illustrates an interaction regarding a popular semiconductor material Gallium Nitride (GaN). Here, MatterChat accurately identifies the chemical formula and space group (P63mc) and constructs a detailed synthesis procedure that aligns with established methods such as molecular beam epitaxy (MBE), metal-organic chemical vapor deposition (MOCVD), and hydride vapor phase epitaxy (HVPE), demonstrating the model’s ability to apply structural and contextual knowledge in generating practical scientific outputs. Figure 3(c) explores an interaction for a widely used ferrite material, Yttrium Iron Garnet (YIG, Y3Fe5O12). MatterChat is able to take the structure and generate detailed text descriptions. Additionally, MatterChat can further generate the synthesis protocol from the preparation of initial materials, their precise mixing ratios, the required sintering conditions, and subsequent characterization techniques, such as X-ray diffraction (XRD) and scanning electron microscopy (SEM). This example demonstrates MatterChat’s capability to synthesize and apply domain-specific knowledge effectively, aligning closely with established scientific practice [34].

Embedding Visualization

![image 198](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile198.png)

(a) (b) (c)

(d) (e)

(f)

Multimodal Retrieval-augmented generation

Prompt

MatterChat

###### +

Stage 1: input

Stage 2: Retrieve (L2 similarity)

Response Response

Stage 3: Aggregate

Material Database (training set)

Final Output

- Fig. 4 UMAP visualization of structural embeddings extracted from the bridge model. (a) Visualization of samples containing Si and C elements from the Material Project dataset, showing how materials cluster based on their structural embeddings extracted from the bridge model. The value indicates the structural similarity calculated using the SOAP descriptor in combination with the REMatch kernel (see Methods for further details). (b, c) Visualizations of SiC subgroup color-coded by structural similarity and formation energy. The two clusters exhibit high structural similarity, with formation energy further assisting in distinguishing between them. (d, e) Visualizations of Si subgroup color-coded by structural similarity and formation energy. Two clusters demonstrate a smooth transition in both structural similarity and formation energy, indicating that both factors captured by the structural embeddings contribute to the observed clustering. (f) Proposed Multi-modal Retrieval-Augmented Generation (RAG) for robust prediction.


#### 2.3 MatterChat extracted embeddings contain structural and propertyinformation

We further explore MatterChat’s ability to leverage material structural information by providing a detailed visualization/clustering analysis with the UAMP dimension reduction technique [35]. Figures 4(a)-(e) show comprehensive visualizations of embeddings processed by the bridge model, with all material samples that contain silicon (Si), carbon (C), and their composites compounds (e.g., SiC, SixCy) from the Material Project database [36]. UMAP was used to reduce the embeddings from an original 4096 dimensions to two dimensions, with the x and y axes corresponding to the first and second reduced dimensions, respectively.

Figure 4(a) presents the visualizations containing all the selected materials; each sample is color-coded with a structure similarity score [37]. The clustering generally follows distinctions in chemical compositions. Additionally, materials with the same atomic composition are grouped into separate clusters based on crystalline structural differences (e.g., Carbon with Diamond vs. Graphite crystalline structure). Figures 4(b) and 4(d) show zoomed-in visualizations of clustering results for materials consisting exclusively of Si and SiC compositions. Figure 4(d) shows the gradient of structure similarity scores, ranging from blue (low similarity) to red (high similarity), demonstrating how closely related structural features result in spatial proximity within the embedding space. However, an interesting exception is

observed with SiC (see Figure 4(b)): despite its identical composition and similar structural phases, two distinct clusters of SiC emerge, suggesting that factors beyond composition and structure alone influence their separation. To further explore factors that influence clustering, we labeled the samples according to their formation energy, with results displayed in Figures 4(c) for SiC and 4(e) for Si. These figures clearly show a trend from low to high formation energy. This analysis reveals that clusters grouped by structural similarity also align closely in terms of formation energy. Such findings indicate that the model’s ability to produce embeddings that not only differentiate structural characteristics but also correlate with key material properties. Given that the embeddings derived from bridge model preserve both material structure and property-relevant information, we implemented a multi-modal Retrieval-Augmented Generation (RAG) mechanism during inference, as illustrated in Figure 4(f). Instead of relying solely on a single output from MatterChat for each query-sample pair, we now retrieve additional information of two more samples from the material pool (training set). This retrieval is based on the L2 similarity between the embeddings of the sample material and those in the pool. After that, we aggregate all three results to get the final output by applying a majority-voting strategy for classification tasks and averaging for quantitative tasks. Such a method could further enhance the overall robustness of MatterChat across different tasks. The details of the visualization method are provided in the Method Section.

#### 2.4 Comprehensive quantitative analysis for all material tasks

To provide a more thorough evaluation of MatterChat, we conducted a comprehensive analysis of its performance across nine material property tasks on the evaluation set (14290 samples). This analysis compares MatterChat with two open-source large language models (LLMs), Vicuna [38] and Mistral [17], as well as two physical ML models, SchNet [39] and CHGNet [27].

Classification Tasks (Figure 5(a)–(f)) Six out of the nine material property tasks are classification tasks, evaluated using prediction accuracy as the metric. These tasks include metallicity, bandgap type, stability, magnetic properties, and experimental observables. As shown in the top two rows of Figure

###### 5, MatterChat demonstrates improvements over all tested models. Compared to state-of-the-art LLMs,MatterChat achieves substantially higher accuracy, benefiting from its ability to integrate graph-basedmaterial structure data with natural language reasoning. Moreover, MatterChat even outperforms phys-ical ML models such as SchNet and CHGNet, the latter being the built-in model used in the MaterialProcessing Branch, showing its superior capability in handling multi-modal inputs for material classifi-cation.Numerical Property Prediction (Figure 5(g)–(i)) The remaining three tasks—formation energy,energy above the hull, and bandgap prediction—are numerical property prediction tasks. For these tasks,the root mean squared error (RMSE) between predicted values and ground truth is used as the evalua-tion metric. Due to the inherent limitations of LLMs in producing accurate numerical predictions [40],their performance is not included in the bar plots, as the errors were excessively large. Instead, Figure

- 5 compares MatterChat with the physical ML models. The results show that MatterChat achieves an overall lower RMSE error in the numerical property tasks, outperforming both SchNet and CHGNet. This demonstrates MatterChat’s ability to handle highly quantitative material property predictions with precision, further validating the effectiveness of its multi-modal integration approach. Such analysis demonstrates MatterChat’s versatility and robustness across diverse material property tasks. By outperforming both state-of-the-art LLMs and physical ML models, MatterChat establishes itself as a powerful tool for materials science applications, offering accurate predictions for both classification and numerical property tasks. These results demonstrate the framework’s potential to accelerate material discovery and deepen our understanding of material properties.


#### 2.5 Comparative Study

We conducted a comprehensive comparative study to evaluate the effectiveness of our multi-modal LLM approach against several alternative methods. The summary of inference results on the test set across all material property prediction tasks is presented in Table 1. The first column shows results from training the multi-modal LLM using a Simple Adapter with LowRank Adaptation (LoRA) finetuning[41], where lightweight adapter layers and the LLM (Mistral-7B) are updated during training, following the method in [42]. The second column presents a pure LLM baseline, in which the LLM is finetuned with LoRA on serialized CIF content and user queries treated as tokenized text prompts—without any structural encoding or auxiliary modality. The third column corresponds to our proposed method based on the Bootstrapping Approach [28], where only the bridge module is

| | | | | | | |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |


| | | | | | | |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |


| | | | | | | |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |


| | | | | | | |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |


| | | | | | | |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |


| | | | | | | |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |


| |![image 199](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile199.png)<br><br>❌ ❌<br><br>![image 200](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile200.png)| | | | | |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |


| |![image 201](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile201.png)<br><br>❌ ❌<br><br>![image 202](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile202.png)| | | | | |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |


| |![image 203](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile203.png)<br><br>❌ ❌<br><br>![image 204](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile204.png)| | | | | |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |


Fig. 5 Performance comparison of MatterChat, open-source LLMs (Vicuna, Mistral), and physical pretrained models (SchNet, CHGNet) across nine material property tasks. (a)–(f) show classification task accuracies, where MatterChat consistently outperforms other models. Panels (g)–(i) present root mean absolute error (RMSE) results for numerical property predictions, demonstrating MatterChat’s superior precision in formation energy, energy above the hull, and bandgap tasks.

trained, while both the graph encoder and the LLM remain frozen. This strategy focuses on aligning material structures with language representations efficiently, avoiding the need for extensive finetuning of the large-scale language model. All methods were trained on the same dataset under identical conditions and evaluated on the same test splits. The results demonstrate that our multi-modal bootstrapping approach achieves superior performance compared to both baselines. Notably, it does so without modifying the pretrained components, highlighting its efficiency and practicality for structure-aware property prediction tasks using LLM. We also include results from our approach augmented with multi-modal retrieval-augmented generation (RAG) during inference. This variant further slightly improves inference performance by having taking more similar material samples into consideration during the inference.

### 3 Discussion

In this study, we present MatterChat, a multi-modal framework that achieves superior performance in material properties prediction and scientific reasoning tasks by leveraging a more effective representation of materials. A key innovation of MatterChat is its ability to leverage existing advancements in both material science and language modeling by integrating a pretrained material foundation encoder with a pretrained large language model (LLM). Rather than training an entire model from scratch, MatterChat achieves strong performance by training only a lightweight bridge model, efficiently aligning material structure representations with textual understanding while maintaining high accuracy across diverse material science tasks. Moreover, MatterChat is designed for multitask learning, enabling it to handle both classification and numerical property prediction. This capability allows the framework to tackle a diverse range of material science tasks within a unified model. Another advantage of our approach is the use of graph-based structural embeddings instead of relying solely on Crystallographic Information

Table 1 Comparison of material property prediction performance across different multi-modal frameworks and RAG-enhanced inference

###### Task Simple Adapter w LoRA LoRA LLM only MatterChat MatterChat w/ RAG

Metallic (Accuracy) 0.6373 0.6864 0.8683 0.8873 Direct Bandgap (Accuracy) 0.8629 0.7839 0.8753 0.8797 Stability (Accuracy) 0.7418 0.7944 0.8515 0.8573 Exp Ob (Accuracy) 0.7171 0.6549 0.8504 0.8570 Is Magnetic (Accuracy) 0.8339 0.6833 0.9368 0.9333 Magnetic Order (Accuracy) 0.7759 0.4238 0.8570 0.8535 Formation Energy (RMSE) 0.4105 1.8059 0.1500 0.1212 Energy Above Hull (RMSE) 0.4415 0.4051 0.1053 0.0964 Bandgap (RMSE) 1.2516 1.4725 0.5590 0.5058

Note: RMSE units — Formation Energy and Energy Above Hull in eV/Atom, Bandgap in eV.

File (.cif) text input. While CIF files encode atomic structures, their text-based format relies entirely on attention mechanisms, which can struggle to explicitly capture geometric symmetries and increase computational overhead due to lengthy tokenization. By processing atomic graphs directly, MatterChat effectively preserves material symmetry and spatial relationships, leading to more accurate structureproperty learning while maintaining computational efficiency.

While MatterChat demonstrates strong performance in material property prediction and analysis, several limitations present opportunities for improvement. The alignment between graph-based material embeddings and language representations remains behavior-driven rather than fully representation-level aligned, requiring further investigation. Additionally, the dataset’s fixed paraphrased queries may limit linguistic diversity, suggesting the need for more comprehensive textual descriptions and a broader range of material properties. Using a frozen LLM, primarily trained on general-purpose text, may restrict domain-specific reasoning and can potentially benefit from finetuning on material science datasets and literature. Future work could focus on three key directions to enhance MatterChat. First, improving representation-level alignment between modalities by incorporating contrastive loss during end-to-end instructive fine-tuning, in addition to pretraining, could further reinforce structural-textual consistency. Second, expanding the dataset to improve generalization by increasing linguistic diversity, as the current fixed set of paraphrased queries may limit variability. Incorporating more comprehensive descriptions and a broader range of material properties would enable the model to handle diverse material science tasks more effectively. Finally, to further enhance MatterChat’s generative capabilities, integrating a graph generative module on top of the existing model could enable novel material structure discovery, extending its utility from property prediction to full-scale material design.

### 4 Method

#### 4.1 Dataset curation

In this work, we curated a comprehensive dataset from the Materials Project Trajectory (MPtrj) dataset [36], focusing specifically on relaxed samples. By selecting these stable configurations, rather than complete trajectory data, we ensure that the dataset captures the equilibrium states of materials, which are more relevant for downstream tasks such as material property prediction. The final dataset consists of 142,899 high-quality samples, offering a rich and diverse representation of inorganic materials.

To facilitate effective model training and evaluation, we partitioned the dataset into training and testing subsets using a 9:1 split ratio. This ensures that a substantial portion of the data is available for learning, while maintaining a dedicated portion for rigorous performance validation, allowing us to assess the generalization capabilities of the model.

In addition to the relaxed structural data, we retrieved detailed material property information using the Materials Project API [29]. Each material is retrieved by a unique mp-id and is enriched with a variety of key descriptors that span both structural and electronic properties. These include:

- • Structure: The full atomic structure of the material, detailing atomic positions and bonding.
- • Chemical formula: The overall chemical composition.


- • Space group: The crystallographic space group of the material, reflecting its symmetry properties.
- • Crystal system: The broader classification of the material’s crystal structure.
- • Metallicity: An indicator of whether the material is metallic or insulating.
- • Magnetic properties: Including whether the material is magnetic and its magnetic ordering (e.g., ferromagnetic, antiferromagnetic).
- • Experimental observables: Properties that can be compared directly with experimental data.
- • Direct bandgap: The direct bandgap energy, a key property for semiconductors.
- • Stability: Indicating whether the material is thermodynamically stable.
- • Energy above hull: A measure of how stable the material is compared to other phases.
- • Bandgap: The electronic bandgap, an important factor in determining a material’s electronic properties.
- • Formation energy: The energy required to form the material from its constituent elements.


These attributes offer a comprehensive view of each material, encompassing both its structural arrangement and electronic behavior. By integrating this wealth of data, our model is capable of capturing complex material-property relationships, supporting tasks such as bandgap prediction, stability analysis, and metallicity determination. This dataset not only provides a robust foundation for training ML models, but it also contributes to broader efforts in materials discovery and property optimization.

#### 4.2 Training Detail

MatterChat employs a bootstrapping strategy commonly used in multi-modal learning for vision-language tasks, adapted here for material science applications. The training process consists of two main stages: pretraining to align material structures with descriptive text; and finetuning for both descriptive and property prediction tasks with the LLM module integrated (see Figure S2 in the Supplementary Material). The pretraining phase aims to establish a foundational alignment between material structures and descriptive text. In this stage, the model connects a frozen graph encoder with pairs of graph data and corresponding textual descriptions, without attaching the LLM module. Here, the bridge model acts as a text generator, learning to extract descriptive graph representations that effectively capture structural information relevant to the text data.

This stage consists of three core optimizing targets, each with distinct interaction mechanisms between graph embeddings and text, while maintaining a consistent input format:

- 1. Graph-Text Correlation Learning (Contrastive Loss). This task aligns graph and text representations by maximizing the similarity between matched graph-text pairs and minimizing it for mismatched pairs. A contrastive loss is employed:

Lcorrelation = −

N

i=1

log

exp(sim(qi,ti)/τ)

N j=1 exp(sim(qi,tj)/τ)

, (1)

where qi and ti represent the graph and text embeddings, respectively, and τ is the temperature parameter controlling the distribution’s sharpness.

- 2. Graph-Driven Text Prediction (Conditional Language Modeling Loss). The bridge model generates descriptive text based on graph data, conditioned through attention mechanisms. The loss function is defined as:

Lprediction = −

T

t=1

log P(yt|y<t,Q), (2)

where Q represents graph query features, and yt is the token at position t in the output sequence.

- 3. Graph-Text Association (Binary Cross-Entropy Loss). This task predicts whether each graph-text pair is correctly matched. A binary cross-entropy loss


with hard negative sampling is applied:

Lassociation = −

N

(yi log(si) + (1 − yi)log(1 − si)), (3)

i=1

where si is the model’s prediction score, and yi indicates whether the pair is matched (1) or not (0). The total pretraining loss is the sum of the individual task losses:

Ltotal = Lcorrelation + Lprediction + Lassociation. (4)

After pretraining, the model undergoes instructive finetuning to optimize its performance on both descriptive and property prediction tasks. In this stage, the pretrained bridge model is integrated with the LLM to enhance multi-modal learning. A fully connected layer is introduced between the bridge model’s output and the LLM’s input. The finetuning phase includes 12 multi-modal subtasks, including 3 material description tasks and 9 property prediction tasks. Description tasks refine the model’s ability to link structural features with detailed textual explanations, while property prediction tasks focus on improving quantitative accuracy in material property estimation. Finetuning is guided by a supervised cross-entropy loss defined as:

N

T

Lfinetune = −

yi,j log P(yi,j|xi), (5)

i=1

j=1

where yi,j represents the ground truth token for the j-th position of the i-th sample, and P(yi,j|xi) is the model’s predicted probability of the correct token given the multi-modal input xi.

In the pretraining stage, the model is trained using the AdamW optimizer with a learning rate of 2×10−4, with cosine decay scheduler and linear warmup starting from 1×10−6. A weight decay of 0.05 is applied to regularize the model, with a batch size of 32 and gradient accumulation over 5 steps to manage computational efficiency. Mixed-precision training is enabled to improve performance and reduce memory usage. The model is trained for ∼ 25 epochs, with checkpoints saved every 2000 iterations. During the finetuning stage, the AdamW optimizer is again used with a learning rate of 2×10−4, featuring a warmup phase to 1 × 10−4 followed by decay to 1 × 10−5. The batch size is set to 8, with gradient accumulation over 16 batches to effectively increase the batch size. Finetuning runs for 50 epochs, with checkpoints saved every 300 steps and at the end of each epoch. Additionally, distributed training is implemented using 4 GPUs per node across 8 nodes, leveraging the Distributed Data Parallel (DDP) strategy to enhance training efficiency and scalability.

#### 4.3 Embedding Visualization

The visualization leverages UMAP to reveal chemical insights encoded in the material embeddings that are extracted from the bridge model in a lower-dimensional space. To prepare the data, each highdimensional embedding, originally structured as (32, 4096), is first flattened into a single vector, capturing the essential features of the material. UMAP is then applied to this set of vectors with number of components equals 2, reducing the data to two dimensions to enable visual interpretation, with random state is set to 1 to ensure consistency in the layout across runs.

Structural similarity scores are computed using the Smooth Overlap of Atomic Positions (SOAP) descriptor [43], combined with the Regularized Entropy Match Kernel (REMatch) [44, 45] to capture the structural characteristics within material embeddings. SOAP is a local atomic environment descriptor that encodes atomic geometries by expanding a Gaussian-smeared atomic density locally, using orthonormal functions derived from spherical harmonics and radial basis functions. From local descriptors to structure matching, we use REMatch kernel on top of SOAP descriptor. The REMatch kernel considers the best matching of local environments and employs an averaging strategy to enhance structural comparison. For SOAP construction, we consider periodic boundary conditions. The cutoff radius for the local region (rcut), the number of radial basis functions (nmax), and the maximum degree of spherical harmonics (lmax) are set to 6 ˚A, 8 ˚A, and 6 ˚A, respectively. For the REMatch kernel, the entropic penalty (α) is set to 1, and the convergence threshold is set to (1 × 10−6). A linear pairwise metric is used for the local similarity calculation.

### Data availability

Upon publication, all data that support the plots within this paper and other findings of this study will be available on a public GitHub repository.

### Code availability

Upon publication, all codes that support the plots within this paper and other findings of this study will be available on a public GitHub repository.

### Acknowledgements

Y.T., Z.Y., and A.N. were supported by Laboratory Directed Research and Development (LDRD) funding from Berkeley Lab, provided by the Director, Office of Science, of the U.S. Department of Energy under Contract No. DE-AC02-05CH11231. This research used resources of the National Energy Research Scientific Computing Center (NERSC), a DOE Office of Science User Facility supported by the Office of Science of the U.S. Department of Energy under Contract No. DE-AC02-05CH11231 and under NERSC GenAI award under No. DDR-ERCAP0030541. W.G. acknowledges support from the National Science Foundation through Grant No. 2235276.

### Author Contributions Statement

Y.T. and W.G. conceived the idea, with W.X. contributing enhancements and Y.Z. providing additional support. Y.Z. supervised the project. Y.T. constructed overall ML framework and performed ML training/inference. W.X performed the physical model training and visualization. Y.T. and W.X. wrote the manuscript with the help of Y.Z., J.C., A.N, S.F., B.E. and M.M.

### References

- [1] Kohn, W., Becke, A.D., Parr, R.G.: Density functional theory of electronic structure. The Journal of Physical Chemistry 100(31), 12974–12980 (1996)
- [2] Marx, D., Hutter, J.: Ab initio molecular dynamics: basic theory and advanced methods. Cambridge University Press (2009)
- [3] Xie, T., Grossman, J.C.: Crystal graph convolutional neural networks for an accurate and interpretable prediction of material properties. Physical review letters 120(14), 145301 (2018)
- [4] Xu, W., Reuter, K., Andersen, M.: Predicting binding motifs of complex adsorbates using machine learning with a physics-inspired graph representation. Nature Computational Science 2(7), 443–450

(2022)

- [5] Batzner, S., Musaelian, A., Sun, L., Geiger, M., Mailoa, J.P., Kornbluth, M., Molinari, N., Smidt, T.E., Kozinsky, B.: E (3)-equivariant graph neural networks for data-efficient and accurate interatomic potentials. Nature communications 13(1), 2453 (2022)
- [6] Gasteiger, J., Becker, F., Gu¨nnemann, S.: Gemnet: Universal directional graph neural networks for molecules. Advances in Neural Information Processing Systems 34, 6790–6802 (2021)
- [7] Batatia, I., Benner, P., Chiang, Y., Elena, A.M., Kov´cs, D.P., Riebesell, J., Advincula, X.R., Asta, M., Avaylon, M., Baldwin, W.J., et al.: A foundation model for atomistic materials chemistry. arXiv preprint arXiv:2401.00096 (2023)
- [8] Zeni, C., Pinsler, R., Zu¨gner, D., Fowler, A., Horton, M., Fu, X., Shysheya, S., Crabb´e, J., Sun, L., Smith, J., et al.: Mattergen: a generative model for inorganic materials design. arXiv preprint arXiv:2312.03687 (2023)
- [9] Xie, T., Fu, X., Ganea, O.-E., Barzilay, R., Jaakkola, T.: Crystal diffusion variational autoencoder for periodic material generation. arXiv preprint arXiv:2110.06197 (2021)


- [10] Ling, C.: A review of the recent progress in battery informatics. npj Computational Materials 8(1)

(2022)

- [11] Liu, D.-Y., Xu, L.-M., Lin, X.-M., Wei, X., Yu, W.-J., Wang, Y., Wei, Z.-M.: Machine learning for semiconductors. Chip 1(4), 100033 (2022)
- [12] Yang, W., Fidelis, T.T., Sun, W.-H.: Machine learning in catalysis, from proposal to practicing. ACS Omega 5(1), 83–88 (2020)
- [13] Sen, S.K., Green, E.D., Hutter, C.M., Craven, M., Ideker, T., Di Francesco, V.: Opportunities for basic, clinical, and bioethics research at the intersection of machine learning and genomics. Cell Genomics 4(1), 100466 (2024)
- [14] Birhane, A., Kasirzadeh, A., Leslie, D., Wachter, S.: Science in the age of large language models. Nature Reviews Physics 5(5), 277–280 (2023)
- [15] Devlin, J.: Bert: Pre-training of deep bidirectional transformers for language understanding. arXiv preprint arXiv:1810.04805 (2018)
- [16] Brown, T., Mann, B., Ryder, N., Subbiah, M., Kaplan, J.D., Dhariwal, P., Neelakantan, A., Shyam, P., Sastry, G., Askell, A., et al.: Language models are few-shot learners. Advances in neural information processing systems 33, 1877–1901 (2020)
- [17] Jiang, A.Q., Sablayrolles, A., Mensch, A., Bamford, C., Chaplot, D.S., Casas, D.d.l., Bressand, F., Lengyel, G., Lample, G., Saulnier, L., et al.: Mistral 7b. arXiv preprint arXiv:2310.06825 (2023)
- [18] Touvron, H., Lavril, T., Izacard, G., Martinet, X., Lachaux, M.-A., Lacroix, T., Rozie`re, B., Goyal, N., Hambro, E., Azhar, F., et al.: Llama: Open and efficient foundation language models. arXiv preprint arXiv:2302.13971 (2023)
- [19] Guo, D., Yang, D., Zhang, H., Song, J., Zhang, R., Xu, R., Zhu, Q., Ma, S., Wang, P., Bi, X., et al.: Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning. arXiv preprint arXiv:2501.12948 (2025)
- [20] Lu, P., Mishra, S., Xia, T., Qiu, L., Chang, K.-W., Zhu, S.-C., Tafjord, O., Clark, P., Kalyan, A.: Learn to explain: Multimodal reasoning via thought chains for science question answering. Advances in Neural Information Processing Systems 35, 2507–2521 (2022)
- [21] Dunn, A., Dagdelen, J., Walker, N., Lee, S., Rosen, A.S., Ceder, G., Persson, K., Jain, A.: Structured information extraction from complex scientific text with fine-tuned large language models. arXiv preprint arXiv:2212.05238 (2022)
- [22] Kim, S., Jung, Y., Schrier, J.: Large language models for inorganic synthesis predictions. Journal of the American Chemical Society 146(29), 19654–19659 (2024)
- [23] Cavanagh, J.M., Sun, K., Gritsevskiy, A., Bagni, D., Bannister, T.D., Head-Gordon, T.: Smileyllama: Modifying large language models for directed chemical space exploration. arXiv preprint arXiv:2409.02231 (2024)
- [24] Weininger, D.: Smiles, a chemical language and information system. 1. introduction to methodology and encoding rules. Journal of chemical information and computer sciences 28(1), 31–36 (1988)
- [25] Ock, J., Guntuboina, C., Barati Farimani, A.: Catalyst energy prediction with catberta: Unveiling feature exploration strategies through large language models. ACS Catalysis 13(24), 16032–16044

(2023)

- [26] Antunes, L.M., Butler, K.T., Grau-Crespo, R.: Crystal structure generation with autoregressive large language modeling. Nature Communications 15(1), 1–16 (2024)
- [27] Deng, B., Zhong, P., Jun, K., Riebesell, J., Han, K., Bartel, C.J., Ceder, G.: Chgnet as a pretrained universal neural network potential for charge-informed atomistic modelling. Nature Machine


- Intelligence 5(9), 1031–1041 (2023)
- [28] Li, J., Li, D., Savarese, S., Hoi, S.: Blip-2: Bootstrapping language-image pre-training with frozen image encoders and large language models. In: International Conference on Machine Learning, pp. 19730–19742 (2023)
- [29] Jain, A., Ong, S.P., Hautier, G., Chen, W., Richards, W.D., Dacek, S., Cholia, S., Gunter, D., Skinner, D., Ceder, G., Persson, K.A.: Commentary: The materials project: A materials genome approach to accelerating materials innovation. APL Materials 1(1) (2013)
- [30] Merchant, A., Batzner, S., Schoenholz, S.S., Aykol, M., Cheon, G., Cubuk, E.D.: Scaling deep learning for materials discovery. Nature 624(7990), 80–85 (2023)
- [31] Team, G., Anil, R., Borgeaud, S., Alayrac, J.-B., Yu, J., Soricut, R., Schalkwyk, J., Dai, A.M., Hauth, A., Millican, K., et al.: Gemini: a family of highly capable multimodal models. arXiv preprint arXiv:2312.11805 (2023)
- [32] Hurst, A., Lerer, A., Goucher, A.P., Perelman, A., Ramesh, A., Clark, A., Ostrow, A., Welihinda, A., Hayes, A., Radford, A., et al.: Gpt-4o system card. arXiv preprint arXiv:2410.21276 (2024)
- [33] Wang, S., Wei, Z., Choi, Y., Ren, X.: Symbolic working memory enhances language models for complex rule application. arXiv preprint arXiv:2408.13654 (2024)
- [34] Sharma, V., Saha, J., Patnaik, S., Kuanr, B.K.: Synthesis and characterization of yttrium iron garnet (yig) nanoparticles - microwave material. AIP Advances 7(5), 056405 (2016)
- [35] McInnes, L., Healy, J., Melville, J.: Umap: Uniform manifold approximation and projection for dimension reduction. arXiv preprint arXiv:1802.03426 (2018)
- [36] Deng, B.: Materials Project Trajectory (MPtrj) Dataset (2023)
- [37] Himanen, L., J¨ger, M.O.J., Morooka, E.V., Federici Canova, F., Ranawat, Y.S., Gao, D.Z., Rinke, P., Foster, A.S.: Dscribe: Library of descriptors for machine learning in materials science. Computer Physics Communications 247, 106949 (2020)
- [38] Chiang, W.-L., Li, Z., Lin, Z., Sheng, Y., Wu, Z., Zhang, H., Zheng, L., Zhuang, S., Zhuang, Y., Gonzalez, J.E., Stoica, I., Xing, E.P.: Vicuna: An Open-Source Chatbot Impressing GPT-4 with 90%* ChatGPT Quality (2023)
- [39] Schu¨tt, K.T., Kindermans, P.-J., Sauceda, H.E., Chmiela, S., Tkatchenko, A., M¨uller, K.-R.: Schnet: A continuous-filter convolutional neural network for modeling quantum interactions (2017)
- [40] Feng, G., Yang, K., Gu, Y., Ai, X., Luo, S., Sun, J., He, D., Li, Z., Wang, L.: How numerical precision affects mathematical reasoning capabilities of llms. arXiv preprint arXiv:2410.13857 (2024)
- [41] Hu, E.J., Shen, Y., Wallis, P., Allen-Zhu, Z., Li, Y., Wang, S., Wang, L., Chen, W., et al.: Lora: Low-rank adaptation of large language models. ICLR (2022)
- [42] Liu, H., Li, C., Wu, Q., Lee, Y.J.: Visual instruction tuning. Advances in neural information processing systems 36 (2024)
- [43] Bart´k, A.P., Kondor, R., Cs´nyi, G.: On representing chemical environments. Physical Review B—Condensed Matter and Materials Physics 87(18), 184115 (2013)
- [44] De, S., Bart´k, A.P., Cs´nyi, G., Ceriotti, M.: Comparing molecules and solids across structural and alchemical space. Physical Chemistry Chemical Physics 18(20), 13754–13769 (2016)
- [45] Musil, F., De, S., Yang, J., Campbell, J.E., Day, G.M., Ceriotti, M.: Machine learning for the structure–energy–property landscapes of molecular crystals. Chemical science 9(5), 1289–1300


(2018)

# arXiv:2502.13107v3[cs.AI]26 Apr 2025

## Supplementary Information:A Multimodal Framework for Material Discovery: Infusing Large Language Models with Atomic Structures

##### Yingheng Tang1*†, Wenbin Xu2*†, Jie Cao3, Weilu Gao4*, Steven Farrell2, Benjamin Erichson5,6, Michael W. Mahoney5,6,7, Andy Nonaka1, Zhi Yao1*

1Applied Mathematics and Computational Research Division, Lawrence Berkeley National Laboratory, Berkeley, CA, USA.

- 2National Energy Research Scientific Computing Center, Lawrence Berkeley National Laboratory, Berkeley, CA, USA.
- 3NSF National AI Institute for Student-AI Teaming, University of Colorado at Boulder, Boulder, USA.


4Department of Electrical and Computer Engineering, The University of Utah, Salt Lake City, UT, USA. 5Scientific Data Division, Lawrence Berkeley National Laboratory, Berkeley, CA, USA. 6International Computer Science Institute, Berkeley, CA, USA. 7Department of Statistics, University of California at Berkeley, Berkeley, CA, USA.

*Corresponding author(s). E-mail(s): ytang4@lbl.gov; wenbinxu@lbl.gov; weilu.gao@utah.edu; jackie zhiyao@lbl.gov; †These authors contribute equally

Keywords: Foundational model, Large Language Model, multi-modal learning, Material discovery

![image 205](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile205.png)

###### Fig. 1 UMAP visualization of structural embeddings extracted from the bridge model. (Si, O, SixOy)

![image 206](Tang et al._2025_MatterChat A Multi-Modal LLM for Material Science 1_images/imageFile206.png)

###### Fig. 2 Training Scheme.

### Instruction Templates (descriptive tasks)

|Task<br><br>|Instruction Template|
|---|---|
|Reduced Formula<br><br>|<material structure>What is the chemical formula for this material? <material structure>Can you tell me the chemical formula of this material? <material structure>Please provide the chemical formula for the material. <material structure>What is the formula for this material? <material structure>Could you tell me the formula of the material? <material structure>What elements make up this material? <material structure>How would you write the chemical formula of this material? <material structure>What is the exact chemical formula of this material? <material structure>Can you provide the chemical formula for this material?|
|Space Group|<material structure>What is the space group for this material? <material structure>To which space group does this material belong? <material structure>Can you tell me the space group of this material? <material structure>Please provide the space group for the material. <material structure>What is the crystallographic space group of this material? <material structure>How is the space group of this material classified? <material structure>Can you specify the space group for this material? <material structure>Could you tell me the space group classification of this material? <material structure>Can you provide the space group information for this material? <material structure>What is the space group number of this material?|
|Crystal System|<material structure>What is the crystal system of this material? <material structure>Can you tell me the crystal system of this material? <material structure>Please provide the crystal system for the material. <material structure>What crystal system does this material belong to? <material structure>How is the crystal system of this material classified? <material structure>Can you specify the crystal system for this material? <material structure>What is the crystallographic system of this material? <material structure>Could you tell me the crystal system classification of this material? <material structure>Which crystallographic system does this material belong to?|
|Generate<br><br>|<material structure>Can you provide another material similar to this material? <material structure>Is there another material like this material that you can provide? <material structure>Can you show me a different material similar to this one? <material structure>Can you generate another material similar to this one?|
|General<br><br>|<material structure>Can you describe this material? <material structure><s>|


### Answer Templates (descriptive tasks)

|Task|Instruction Template|
|---|---|
|Reduced Formula<br><br>|The chemical formula for this material is <material attribute >. The chemical formula of this material is <material attribute >. The chemical formula for the material is <material attribute >. The formula for this material is <material attribute >. The formula of the material is <material attribute >. The elements that make up this material are represented as <material attribute >. The chemical formula of this material is written as <material attribute >. The exact chemical formula of this material is <material attribute >. The chemical formula for this material is <material attribute >.|
|Space Group<br><br>|The space group for this material is <material attribute >. This material belongs to the space group <material attribute >. The space group of this material is <material attribute >. The space group for the material is <material attribute >. The crystallographic space group of this material is <material attribute >. The space group of this material is classified as <material attribute >. The space group for this material is specified as <material attribute >. The space group classification of this material is <material attribute >. The space group information for this material is <material attribute >. The space group number of this material is <material attribute >.|
|Crystal System<br><br>|The crystal system of this material is <material attribute >. The crystal system of this material is <material attribute >. The crystal system for the material is <material attribute >. This material belongs to the <material attribute >crystal system. The crystal system of this material is classified as <material attribute >. The crystal system for this material is specified as <material attribute >. The crystallographic system of this material is <material attribute >. The crystal system classification of this material is <material attribute >. This material belongs to the <material attribute >crystallographic system.|


### Instruction Templates (property part1)

|Task<br><br>|Instruction Template|
|---|---|
|Is Metal|<material structure>Is this material metal or non-metal? <material structure>Can you tell me if this material is metal or not? <material structure>What is the classification of this material: metal or non-metal? <material structure>Is this material considered a metal? <material structure>How is this material categorized: metal or non-metal? <material structure>Could you specify if this material is metal or non-metal? <material structure>Is the material metallic or non-metallic? <material structure>Can you provide the classification of this material: metal or non-metal? <material structure>Is this material identified as a metal or non-metal? <material structure>What type of material is this: metal or non-metal?|
|Direct Bandgap<br><br>|<material structure>Does the material have a direct bandgap or indirect bandgap? <material structure>Is the bandgap of this material direct or indirect? <material structure>Can you tell me if this material has a direct or indirect bandgap? <material structure>What type of bandgap does this material have: direct or indirect? <material structure>Is this material characterized by a direct or indirect bandgap? <material structure>Could you specify if the bandgap of this material is direct or indirect? <material structure>Does this material exhibit a direct or indirect bandgap? <material structure>Is the bandgap in this material direct or indirect? <material structure>How is the bandgap of this material classified: direct or indirect? <material structure>Is this a direct or indirect bandgap material?|
|Stability<br><br>|<material structure>Is this material stable? <material structure>Can you tell me if this material is stable? <material structure>What is the stability of this material? <material structure>Please provide the stability information for this material. <material structure>Is the material stable under standard conditions? <material structure>Is this material thermodynamically stable?|
|Experimental Observation<br><br>|<material structure>Is the material experimentally observed or not? <material structure>Can you tell me if the material is observed in experiments?|
|Is Magnetic<br><br>|<material structure>Is the material magnetic or not? <material structure>Is the material magnetic or non-magnetic? <material structure>Can you tell me if this material is magnetic? <material structure>What is the magnetic nature of this material? <material structure>Is this material classified as magnetic? <material structure>Does this material have magnetic properties? <material structure>Is this a magnetic or non-magnetic material?|
|Magnetic Order<br><br>|<material structure>What is the magnetic order of the material? <material structure>Can you tell me the magnetic order of this material? <material structure>Could you specify the magnetic order of the material? <material structure>What type of magnetic order does this material have? <material structure>Please provide the magnetic ordering of the material. <material structure>What is the magnetic arrangement in this material? <material structure>Could you tell me the type of magnetic order of this material?|


### Answer Templates (property part1)

|Task<br><br>|Instruction Template|
|---|---|
|Is Metal|This material is classified as <material attribute >. This material is a <material attribute >. The classification of this material is <material attribute >. This material is considered <material attribute >. This material is categorized as <material attribute >. This material is specified as <material attribute >. This material is <material attribute >. The classification of this material is <material attribute >. This material is identified as <material attribute >. This type of material is <material attribute >.|
|Direct Bandgap<br><br>|The material has a <material attribute >bandgap. The bandgap of this material is <material attribute >. This material has a <material attribute >bandgap. This material has a <material attribute >type of bandgap. This material is characterized by a <material attribute >bandgap. The bandgap of this material is specified as <material attribute >. This material exhibits a <material attribute >bandgap. The bandgap in this material is <material attribute >. The bandgap of this material is classified as <material attribute >. This is a <material attribute >bandgap material.|
|Stability|This material is <material attribute >. Yes, this material is <material attribute >. The stability of this material is <material attribute >. The stability information for this material is <material attribute >. This material is <material attribute >under standard conditions. This material is <material attribute >.|
|Experimental Observation<br><br>|The material is <material attribute >. The material is <material attribute >.|
|Is Magnetic<br><br>|The material is <material attribute >. This material is <material attribute >. Yes, this material is <material attribute >. The magnetic nature of this material is <material attribute >. This material is classified as <material attribute >. This material has <material attribute >properties. This is a <material attribute >material.|
|Magnetic Order|The magnetic order of the material is <material attribute >. The magnetic order of this material is <material attribute >. The magnetic order of the material is specified as <material attribute >. This material has a <material attribute >type of magnetic order. The magnetic ordering of the material is <material attribute >. The magnetic arrangement in this material is <material attribute >. The type of magnetic order of this material is <material attribute >.|


### Instruction Templates (property part2)

|Task|Instruction Template|
|---|---|
|Bandgap<br><br>|<material structure>What is the bandgap of the material? <material structure>Can you tell me the bandgap of this material? <material structure>What is the energy bandgap for this material? <material structure>Could you specify the bandgap of the material? <material structure>Could you tell me the bandgap energy level of this material?|
|Formation Energy|<material structure>Can you tell me the formation energy of this material? <material structure>Please provide the formation energy for the material. <material structure>What is the formation energy value for this material? <material structure>How much is the formation energy of this material? <material structure>Can you specify the formation energy of this material?|
|Energy Above Hull<br><br>|<material structure>Can you tell me the energy above hull of this material? <material structure>Please provide the energy above hull for the material. <material structure>What is the energy above the hull for this material? <material structure>How much is the energy above hull for this material? <material structure>Can you specify the energy above hull of this material? <material structure>Could you tell me the energy above hull of the material?|


### Answer Templates (property part2)

|Task|Instruction Template|
|---|---|
|Bandgap|The bandgap of the material is <material attribute >. The bandgap of this material is <material attribute >. The energy bandgap for this material is <material attribute >. The bandgap of the material is specified as <material attribute >. The bandgap energy level of this material is <material attribute >.|
|Formation Energy<br><br>|The formation energy of this material is <material attribute >. The formation energy for the material is <material attribute >. The formation energy value for this material is <material attribute >. The formation energy of this material is <material attribute >. The formation energy of this material is specified as <material attribute >.|
|Energy Above Hull|The energy above hull of this material is <material attribute >. The energy above hull for the material is <material attribute >. The energy above the hull for this material is <material attribute >. The energy above hull for this material is <material attribute >. The energy above hull of this material is specified as <material attribute >. The energy above hull of the material is <material attribute >.|


