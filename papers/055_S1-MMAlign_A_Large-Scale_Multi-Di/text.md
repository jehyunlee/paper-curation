# arXiv:2601.00264v1[cs.CV]1 Jan 2026

## S1-MMAlign: A Large-Scale, Multi-Disciplinary Dataset for Scientific Figure–Text Understanding

##### He Wang1,2,†, Longteng Guo1,†, Pengkang Huo1, Xuanxu Lin1, Yichen Yuan1, Jie Jiang1 & Jing Liu1,∗

1 Institute of Automation, Chinese Academy of Sciences, Beijing, China 2 School of Advanced Interdisciplinary Sciences, University of Chinese Academy of Sciences, Beijing, China

† These authors contributed equally to this work. ∗ Corresponding author: jliu@nlpr.ia.ac.cn

###### Abstract

Multimodal learning has revolutionized general domain tasks, yet its application in scientific discovery is hindered by the profound semantic gap between complex scientific imagery and sparse textual descriptions. We present S1-MMAlign, a large-scale, multi-disciplinary multimodal dataset comprising over 15.5 million high-quality image-text pairs derived from 2.5 million open-access scientific papers. Spanning disciplines from physics and biology to engineering, the dataset captures diverse visual modalities including experimental setups, heatmaps, and microscopic imagery. To address the pervasive issue of weak alignment in raw scientific captions, we introduce an AI-ready semantic enhancement pipeline that utilizes the Qwen-VL multimodal large model series to recaption images by synthesizing context from paper abstracts and citation contexts. Technical validation demonstrates that this enhancement significantly improves data quality: SciBERT-based pseudo-perplexity metrics show reduced semantic ambiguity, while CLIP scores indicate an 18.21% improvement in image-text alignment. S1-MMAlign provides a foundational resource for advancing scientific reasoning and cross-modal understanding in the era of AI for Science.The dataset is publicly available at https://huggingface.co/datasets/ScienceOne-AI/S1-MMAlign.

### Background & Summary

The paradigm of "AI for Science" is accelerating, shifting towards a data-driven era where scientific foundation models are poised to automate discovery and reasoning1;2. However, a critical bottleneck impedes the development of multimodal scientific agents: the profound semantic misalignment inherent in raw scientific publications. Unlike general domain images (e.g., COCO3, LAION4) where captions offer self-contained visual descriptions (e.g., “a cat sitting on a mat”), scientific figures are fundamentally distinct. They encapsulate complex logic, physical mechanisms, and variable relationships that are often implicitly defined5.

Critically, the textual captions found in raw PDFs are frequently context-dependent and sparse. A typical caption might read “Figure 3: Ablation study results,” relying entirely on the

Preprint. Work in progress.

main text for interpretation. This indexical nature creates a significant “semantic gap” for machine learning models, as the visual signal is divorced from its theoretical grounding. Training on such data leads to superficial alignment, where models learn to recognize chart types but fail to comprehend the underlying scientific implications6. Existing datasets often lack the structural depth to bridge this gap, serving merely as aggregations of raw, noisy pairs2;7.

To address this, we release S1-MMAlign, a comprehensive foundational corpus designed to ground scientific intelligence. Beyond scale, our core contribution lies in a novel AI-driven semantic enhancement pipeline. We construct over 15.5 million image-text pairs where raw visual signals are fused with paper-level context (e.g., abstracts, citations) to generate dense, scientifically rigorous descriptions. Sourced from open-access repositories (e.g., arXiv, bioRxiv8), S1-MMAlign transforms sparse scientific figures into self-contained knowledge units, enabling models to learn not just what a figure looks like, but why it is scientifically significant.

Table 1: Overview of S1-MMAlign Dataset Specifications. Dataset Feature Details Total Image-Text Pairs ∼15.5 Million Total Source Papers ∼2.5 Million Total Storage Size 3.03 TB Avg. Raw Caption Length 267 ± 261 characters Avg. Enhanced Caption Length 759 ± 251 characters Disciplinary Coverage Physics, CS, Biology, Mathematics, Engineering, etc. Data Sources arXiv, bioRxiv, medRxiv, ChemRxiv, Nature Comms. Data Format JSONL (Metadata) & TAR (Image Archives) License CC-BY-4.0

To analyze the disciplinary diversity of S1-MMAlign, we aggregated high-cardinality source tags into major scientific domains. Figure 1 illustrates the final distribution of the corpus, which ensures a holistic representation of scientific knowledge.

As illustrated in Figure 1, the corpus is heavily anchored in quantitative disciplines, mirroring the publication volume of open-access repositories. Physics and Computer Science together comprise over half of the dataset, serving as the primary sources of multimodal scientific data. Significant contributions also stem from domains like Astronomy and Biology, ensuring a diverse coverage of visual taxonomies.

![image 1](Wang et al._2026_S1-MMAlign A Large-Scale, Multi-Disciplinary Dataset for Scientific Figure-Text Understanding_images/imageFile1.png)

- Figure 1: Subject Distribution of S1-MMAlign. Physics (33%) and Computer Science (25%) constitute the dominant subsets, followed by Astronomy (13%), Biology (10%), and Mathematics (9%). The ’Others’ category (10%) encompasses diverse fields such as Engineering and Earth Science.


#### Semantic Enrichment Analysis

Beyond disciplinary breadth, the dataset is distinguished by its novel Semantic Enhancement Strategy. By integrating contextual information from paper titles, abstracts, and citation contexts, S1-MMAlign provides augmented captions that clarify the implicit scientific context, experimental conditions, and variable definitions associated with each visual element.

This enhancement significantly increases caption informativeness. As demonstrated in Figure 2, the recaptioning process substantially expands the textual content compared to raw captions, effectively addressing the issue of semantic sparsity in original scientific figures.

Distribution of Caption Lengths

| |Recaption| |
|---|---|---|
| |Caption| |
| | | |
| | | |
| | | |
| | | |
| | | |
| | | |
| | | |


60000

50000

40000

Count

30000

20000

10000

0

0 200 400 600 800 1000

Length (characters)

- Figure 2: Character Length Distribution Analysis. Comparative statistics reveal a significant shift in information density between the raw and enhanced corpora. Raw captions (orange) exhibit high volatility with a character count of 267±261 (mean ± std), reflecting the pervasive semantic sparsity and inconsistency inherent in original scientific metadata. In contrast, the semantically enhanced descriptions (blue) achieve a robust 2.8× expansion, yielding 759±251 characters. The reduction in the coefficient of variation (CV ≈ 33%) for the recaptioned data indicates a more homogeneous and standardized semantic representation, effectively bridging the "semantic gap" for downstream multimodal training.


The availability of such a large-scale, semantically aligned corpus provides a robust foundation for investigating cross-modal scientific reasoning. By offering grounded textual descriptions, S1-MMAlign addresses the critical challenge of generative hallucinations in current VLMs9;10.

### Methods

The construction of S1-MMAlign follows a rigorous four-phase pipeline: Data Ingestion, Preprocessing, Core AI Processing, and Structured Output Generation. The overall workflow is illustrated in Figure 3.

![image 2](Wang et al._2026_S1-MMAlign A Large-Scale, Multi-Disciplinary Dataset for Scientific Figure-Text Understanding_images/imageFile2.png)

- Figure 3: Overview of the S1-MMAlign Data Construction Pipeline. The workflow consists of four distinct phases: (1) Data Ingestion from diverse sources including arXiv (LaTeX) and web crawls (PDF); (2) Preprocessing Pipeline, featuring archive integrity checks, Regexbased parsing, EPS-to-PNG conversion, and strict quality filtering; (3) Core AI Processing, employing the Qwen-VL architecture on an H100 GPU cluster to generate semantically dense captions; and (4) Structured Output Generation, organizing the final data into JSONL format for public release.


#### Phase 1: Data Acquisition and Source Selection

To ensure a holistic representation of scientific knowledge, we implemented a systematic data acquisition protocol spanning diverse open-access repositories. Our harvesting strategy targets the primary preprint platforms—specifically arXiv, bioRxiv8, medRxiv, and ChemRxiv—as well as the open-access subsets of high-impact journals such as Nature Communications. This multisource approach ensures that the dataset captures a wide spectrum of visual modalities across physical, biological, and engineering sciences.

#### Phase 2: Preprocessing Pipelines

###### The arXiv Extraction Pipeline

We leveraged the rich semantic structure inherent in source code by retrieving raw LaTeX source packages via the arXiv bulk data access protocol. A custom extraction pipeline was implemented to handle the heterogeneity of user-uploaded sources. The process began with a rigorous integrity verification of the retrieved bundles; archives that were corrupted, failed decompression, or lacked essential image directories were systematically excluded, resulting in a rejection rate of approximately 20%. Following validation, we employed a robust parsing module based on Regular Expressions to navigate the LaTeX syntax. This module extracted figure environments to establish precise mappings between image filenames and their corresponding semantic metadata, including captions, labels, and local referencing contexts.

Visual assets underwent a standardization process to ensure compatibility with the input requirements of mainstream vision encoders11;12. Since scientific publications frequently utilize vector graphics (EPS/PDF), we implemented a rasterization step to convert these assets into high-quality PNG formats. Finally, a multi-stage heuristic filter was applied to eliminate noise and prioritize high-information scientific figures. This quality control stage discarded files smaller than 5KB, corrupted bytestreams, and non-semantic visual content, such as pure LaTeX tables rendered as images.

###### The PDF Extraction Pipeline

Given that raw LaTeX source files are generally unavailable for repositories beyond arXiv (e.g., bioRxiv, medRxiv), we developed a custom extraction workflow anchored by the MinerU intelligent document processing engine13 to process the compiled PDF documents. This pipeline addresses the challenge of parsing unstructured layouts through a multi-stage approach described below.

Deep Layout Detection. We utilized MinerU’s advanced layout analysis models to parse the document structure. This step precisely identifies and localizes key document elements—specifically figure boundaries and text blocks—generating precise bounding box coordinates for each component.

Geometry-based Association. Since layout detection outputs independent elements, we implemented a custom spatial proximity matching algorithm to link figures with their corresponding captions. By leveraging the coordinate information provided by MinerU, this heuristic logic associates image regions with the nearest valid caption text, effectively resolving figure-caption pairs even in complex multi-column layouts.

Content Extraction and Cleaning. Based on the detected coordinates, figure regions were extracted directly from the PDF source files. The associated caption text was simultaneously parsed and cleaned to remove non-semantic artifacts (e.g., indexing numbers), yielding structured image-text pairs aligned with the LaTeX-sourced data.

###### Phase 3: Semantic Enhancement via Context-Aware Recaptioning

The core challenge in scientific multimodal learning lies in the "semantic gap" between raw visual signals and their high-level theoretical implications. A standard visual encoder might perceive a chart merely as geometric lines, whereas scientific reasoning requires interpreting these lines as manifestations of specific physical laws or experimental trends. To bridge this gap and generate descriptions that are not only visually accurate but also theoretically grounded, we implemented a semantic enhancement pipeline using the Qwen3-VL architecture14. We selected this model for its specialized SigLIP-2 encoder15, which utilizes 2D-RoPE to process dynamic high-resolution inputs. This capability is critical for preserving fine-grained scientific details—such as logarithmic axis scales, chemical bond structures, and error bars—that are often lost in standard low-resolution processing.

Knowledge-Augmented Context Injection. To ground visual perception in scientific narrative, we implemented a rigorous context-injection strategy. Rather than relying on generic captioning instructions, we constructed a holistic semantic window for each figure, integrating the paper’s Title, Abstract, and the Local Citation Context—the specific text surrounding the figure’s reference. This multi-source input compels the model to function as a scientific inter-

preter rather than a passive observer. By synthesizing the "global" research objective (from the abstract) with the "local" experimental analysis (from the citation context), the model generates captions that explain why the visual pattern exists, explicitly linking pixel-level features to domain-specific theoretical constructs. This approach effectively minimizes hallucinations and ensures the generated descriptions capture the underlying scientific causality.

High-Throughput Inference Optimization. Processing 15.5 million scientific figures required a robust computational framework. We deployed a parallelized inference pipeline on an 8x H100 GPU cluster, leveraging the vLLM library16 to handle the massive throughput requirements. By utilizing PagedAttention for efficient memory management and continuous batching strategies, we maximized hardware utilization and token generation speed. This optimized infrastructure enabled the efficient transformation of the entire corpus at scale, converting sparse raw images into a dense, knowledge-rich multimodal dataset ready for downstream scientific reasoning tasks.

### Data Records

The S1-MMAlign dataset is hosted on the Hugging Face Hub (see Data Availability). To facilitate modular access and efficient subsetting across diverse scientific domains, the corpus is organized into a stratified hierarchy based on source provenance (e.g., arXiv, bioRxiv).

#### File Organization

The repository implements a decoupled storage architecture designed to optimize the retrieval and processing of high-volume multimodal data. As illustrated in Figure 4, this architecture separates lightweight semantic metadata from heavy visual assets to support flexible access patterns.

Metadata Serialization. Semantic annotations, bibliographic metadata, and alignment information are serialized in the JSONL (JSON Lines) format and housed within the jsonl/ directory. This line-oriented standard was specifically selected to support large-scale streaming and compatibility with distributed processing frameworks (e.g., Apache Spark), allowing researchers to parse text-based features without the latency of loading binary image data.

Sharded Visual Archival. Corresponding visual content (e.g., plots, diagrams) is maintained in standard formats (PNG/JPEG) and packaged into compressed .tar.gz archives. To mitigate I/O bottlenecks and ensure download stability for terabyte-scale subsets, we adopted a multivolume sharding strategy: archives exceeding 30GB are segmented into sequential parts (e.g., images.tar.gz.partaa). This segmentation facilitates parallelized data transfer and allows for robust recovery during interrupted downloads.

Cryptographic Integrity Verification. To guarantee data reliability and optimize storage efficiency for redundant visual assets, the repository is managed via the Xet version control extension17. Unlike traditional Git-LFS, Xet utilizes Merkle-tree based deduplication, which segments large files into content-addressable blocks. The system exposes a dual-layer verification mechanism: a SHA-256 checksum ensures the bit-level consistency of the reconstructed file content, while the Xet Hash validates the structural integrity of the stored blocks. Researchers can utilize these cryptographic fingerprints (contained within the 135-byte pointer files) to algorithmically verify that downloaded artifacts are exact, corruption-free replicas of the source.

S1-MMAlign/ .................................................. Root Repository arxiv/ ...................Structure Type A: Large-scale split archives jsonl/ ......................................... Contains metadata files

- 07_recaption.jsonl

- 08_recaption.jsonl


...

25_recaption.jsonl

- images_2007.tar.gz .....................................Yearly archives

- images_2008.tar.gz

- images_2009.tar.gz.partaa ............ Split volumes for large years


images_2009.tar.gz.partab

... biorxiv/ .........................Structure Type B: Multi-part archives

jsonl/

biorxiv_recaption.jsonl

- images.tar.gz.partaa

- images.tar.gz.partab


... chemrxiv/ ..............................Structure Type C: Single archive

jsonl/

chemrxiv_recaption.jsonl images.tar.gz

[nature_communications] ............................................ Type B [edrxiv, engrxiv, medrxiv, metarxiv, psyarxiv] ..................Type C README.md

.gitattributes

- Figure 4: File Organization of S1-MMAlign. The repository structure adapts to data volume: (A) Yearly Archives for massive sources like arXiv (e.g., images_2007.tar.gz); (B) Multi-Part Archives for large sources like bioRxiv (e.g., images.tar.gz.partaa); and (C) Single Archives for smaller datasets. All subsets include a jsonl directory for metadata.


#### Metadata Schema

The dataset follows a flat JSON structure where each key corresponds to a specific semantic attribute. The detailed schema definition and data types are presented in Table 2.

### Technical Validation

To rigorously quantify the efficacy of our semantic enhancement strategy, we performed a comprehensive evaluation focusing on linguistic quality and information content.

Table 2: Metadata Schema Definitions. Description of semantic attributes present in each JSONL record.

###### Field Key Description

doi / arxiv_id Unique identifier for the source publication (DOI or arXiv ID). title Title of the source scientific paper. image_path Relative file path pointing to the image file. caption Raw figure caption extracted directly from the source. recaption Semantically enhanced description generated by the

Qwen3-VL pipeline. categories Disciplinary classification.

#### Textual Quality Assessment

We employed SciBERT18 to compute the pseudo-Perplexity (pseudo-PPL) of the generated captions, serving as a robust proxy for linguistic fluency and domain adaptation. Unlike generalpurpose language models, SciBERT is pre-trained specifically on scientific corpora, making it uniquely sensitive to the syntactic structures and terminologies inherent in academic discourse. Lower pseudo-PPL values indicate higher sequence probability, reflecting text that is more linguistically coherent and aligned with standard scientific language patterns19.

###### Figure 5: Empirical CDF of Text Quality (Pseudo-PPL). The plot illustrates the Cumu-

lative Distribution Function of log10(pseudo-PPL) scores derived from SciBERT18. The blue curve (Enhanced Captions) demonstrates a pronounced leftward shift compared to the original captions, confirming a significant reduction in perplexity and superior alignment with scientific linguistic norms.

- As visualized in Figure 5, the distribution of enhanced captions exhibits a significant left-


ward shift towards lower perplexity values. This statistical trend confirms that the enhancement process effectively mitigates ambiguity and improves the syntactic completeness of the

descriptions, resulting in higher-fidelity scientific text.

#### Semantic Consistency Verification

The CLIP Score metric, rooted in cosine similarity embeddings11;20, was employed to rigorously quantify cross-modal alignment between visual content and textual descriptions. Specifically, we conducted a comparative analysis between the original raw captions and our semantically enhanced counterparts to validate the efficacy of the recaptioning pipeline.

Quantitative Alignment Improvement. The evaluation reveals a substantial quality uplift, with the mean CLIP score increasing by 18.21%. This metric shift indicates that the contextaware recaptioning generates descriptions with significantly higher semantic congruity to the visual data, successfully recovering visual details often omitted in sparse original captions.

Distributional Homogeneity. Beyond mean improvements, the variance of the score distribution decreased by approximately 27.77%. This reduction in volatility signifies improved quality consistency across the corpus. It suggests that the pipeline effectively mitigates lowquality outliers, transforming a highly variable raw dataset into a standardized corpus with stable cross-modal alignment.

| | | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | |
| | | | | | | | | | | | |
| | | | | | | | | | | | |
| | | | | | | | | | | | |
| | | | | | | | | | | | |
| | | | | | | | | | | | |


- Figure 6: Distribution of CLIP Image-Text Consistency Scores. The histogram compares the alignment scores of original (orange) versus enhanced (blue) captions. The pronounced rightward shift and narrower spread of the blue distribution indicate that the enhancement strategy yields a dataset with higher semantic fidelity and greater consistency, providing a stronger supervision signal for multimodal representation learning.


- As visualized in Figure 6, the distribution for enhanced captions is clearly distinguished from


the baseline. The observed rightward shift confirms that the recaptioned text provides a much stronger and more reliable supervision signal for downstream multimodal training tasks.

### Usage Notes

The dataset is designed for pre-training scientific multimodal models21. We recommend using the Hugging Face datasets library to stream the data, as downloading the entire 15.5 million set may require significant storage. Standard image processing libraries (e.g., PIL) can be used to load images from the provided paths.

### Data Availability

The S1-MMAlign dataset is available for download at the following Hugging Face repository: https://huggingface.co/datasets/ScienceOne-AI/S1-MMAlign.

### References

- [1] Jumper, J. et al. Highly accurate protein structure prediction with alphafold. Nature 596, 583–589 (2021).
- [2] Taylor, R. et al. Galactica: A large language model for science. arXiv preprint arXiv:2211.09085 (2022).
- [3] Lin, T.-Y. et al. Microsoft coco: Common objects in context. In European conference on computer vision, 740–755 (Springer, 2014).
- [4] Schuhmann, C. et al. Laion-5b: An open large-scale dataset for training next generation image-text models. In Thirty-sixth Conference on Neural Information Processing Systems Datasets and Benchmarks Track (2022).
- [5] Hsu, T.-Y., Yang, C. et al. Scicap: Generating captions for scientific figures. arXiv preprint arXiv:2110.11624 (2021).
- [6] Lin, Z., Yin, Y., Liu, L. & Wang, D. Sciscinet: A large-scale open data lake for the science of science research. Scientific Data 10, 315 (2023).
- [7] Methani, N., Ganguly, P., Khapra, M. M. & Kumar, P. Plotqa: Reasoning over scientific plots. arXiv preprint arXiv:1909.00997 (2020).
- [8] Sever, R. et al. biorxiv: the preprint server for biology. bioRxiv (2019).
- [9] Liu, H., Li, C., Wu, Q. & Lee, Y. J. Visual instruction tuning. In NeurIPS (2023).
- [10] Bai, J. et al. Qwen-vl: A versatile vision-language model for understanding, localization, text reading, and beyond (2023).
- [11] Radford, A. et al. Learning transferable visual models from natural language supervision. In International conference on machine learning, 8748–8763 (PMLR, 2021).
- [12] Dosovitskiy, A. et al. An image is worth 16x16 words: Transformers for image recognition at scale. arXiv preprint arXiv:2010.11929 (2020).
- [13] OpenDataLab. Mineru: An open-source intelligent data extraction tool (2024).
- [14] Team, Q. Qwen3-vl technical report. arXiv preprint arXiv:2511.21631 (2025).


- [15] Tschannen, M. et al. Siglip 2: Multilingual vision-language encoders with improved semantic understanding, localization, and dense features. arXiv preprint arXiv:2502.14786 (2025).
- [16] Kwon, W. et al. Efficient memory management for large language model serving with pagedattention (2023).
- [17] Low, Y. et al. Git is for data. In Proceedings of the 13th Annual Conference on Innovative Data Systems Research (CIDR) (Amsterdam, The Netherlands, 2023). Published under CC BY 4.0 license.
- [18] Beltagy, I., Lo, K. & Cohan, A. SciBERT: A pretrained language model for scientific text. arXiv preprint arXiv:1903.10676 (2019).
- [19] Devlin, J., Chang, M.-W., Lee, K. & Toutanova, K. Bert: Pre-training of deep bidirectional transformers for language understanding (2019).
- [20] Li, J., Li, D., Xiong, C. & Hoi, S. BLIP: Bootstrapping language-image pre-training for unified vision-language understanding and generation. In International conference on machine learning, 12888–12900 (PMLR, 2022).
- [21] Tarsi, T. et al. Sciol and mulms-img: Introducing a large-scale multimodal scientific dataset and models for image-text tasks in the scientific domain. In 2024 IEEE/CVF Winter Conference on Applications of Computer Vision (WACV), 4548–4559 (2024).


### Competing Interests

The authors declare no competing interests.

