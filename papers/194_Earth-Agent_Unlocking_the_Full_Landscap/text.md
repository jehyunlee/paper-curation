# arXiv:2509.23141v3[cs.CV]3 Mar 2026

![image 1](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1.png)

### EARTH-AGENT: UNLOCKING THE FULL LANDSCAPE OF EARTH OBSERVATION WITH AGENTS

Peilin Feng1∗‡ Zhutao Lv2,1∗‡ Junyan Ye2,1‡ Xiaolei Wang2 Xinjie Huo2 Jinhua Yu2 Wanghan Xu1 Wenlong Zhang1 Lei Bai1 Conghui He1 Weijia Li3,2,1†

1 Shanghai Artificial Intelligence Laboratory 2 Sun Yat-sen University 3 Tsinghua Shenzhen International Graduate School, Tsinghua University

Github: https://github.com/opendatalab/Earth-Agent

Dataset: https://huggingface.co/datasets/Sssunset/Earth-Bench Project Page: https://opendatalab.github.io/Earth-Agent/

![image 2](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile2.png)

|MLLM-Based EO ResearchMLLM-Based EO Research|
|---|
|![image 3](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile3.png)<br><br>RGB images<br><br>Drawbacks<br><br>-step 4.<br><br>RGB<br><br>-<br><br>MLLM<br><br>Final Answer<br><br>|![image 4](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile4.png)<br><br>![image 5](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile5.png)<br><br>![image 6](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile6.png)<br><br>![image 7](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile7.png)<br><br>![image 8](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile8.png)<br><br>![image 9](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile9.png)<br><br>![image 10](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile10.png)<br><br>![image 11](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile11.png)|
|---|
<br><br>![image 12](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile12.png)<br><br>1. Only support processing RGB images<br>2. Only process one/ a few images at a time<br><br>Drawbacks<br><br>3. Limited to single-step and shallow reasoning<br>4. Can’t integrate external tools or expert models<br><br><br>Describe/Classify this image<image><br><br>RGB<br><br>Pretrained-<br><br>MLLM<br><br>Final Answer|


|Existing Agent-Based EO Research-Based EO Research|
|---|
|![image 13](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile13.png)<br><br>![image 14](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile14.png)<br><br>![image 15](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile15.png)<br><br>![image 16](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile16.png)<br><br>Drawbacks<br><br>and<br><br>RGB<br><br>|![image 17](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile17.png)<br><br>![image 18](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile18.png)<br><br>![image 19](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile19.png)<br><br>![image 20](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile20.png)<br><br>![image 21](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile21.png)<br><br>![image 22](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile22.png)<br><br>![image 23](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile23.png)<br><br>![image 24](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile24.png)|
|---|
<br><br>![image 25](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile25.png)<br><br>...<br><br>Final Answer<br><br>3.<br><br>ChangeAgent RSAgent ThinkGeo<br><br>![image 26](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile26.png)<br><br>![image 27](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile27.png)<br><br>![image 28](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile28.png)<br><br>![image 29](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile29.png)<br><br>Drawbacks<br><br>1. Still limited to remote sensing datasets(RGB)<br>2. Tool usage remains shallow and limited<br><br>4. Evaluation overlooking reasoning trajectory<br><br>RGB<br><br>Model 1<br><br>Model n<br><br>![image 30](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile30.png)<br><br>...<br><br>Final Answer<br><br>Is the second car classified as a Sedan?<br><br>3. Lack of the predefined tool ecosystem<br><br><br>|


|Earth-Earth-Agent (Ours)|
|---|
||![image 31](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile31.png)<br><br>![image 32](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile32.png)<br><br>![image 33](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile33.png)<br><br>![image 34](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile34.png)<br><br>![image 35](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile35.png)<br><br>![image 36](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile36.png)|
|---|
<br><br>![image 37](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile37.png)<br><br>- and RGB images images<br><br>3. -step<br>4.<br><br><br>![image 38](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile38.png)<br><br>![image 39](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile39.png)<br><br>![image 40](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile40.png)<br><br>![image 41](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile41.png)<br><br>![image 42](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile42.png)<br><br>...<br><br>Final Answer<br><br>![image 43](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile43.png)<br><br>![image 44](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile44.png)<br><br>![image 45](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile45.png)<br><br>Advantages<br><br>1. Able to process Multi-Spetral and RGB images<br>2. Able to process numerous images<br>3. Complex & multi-step interactive reasoning<br>4. Interact with external tools/models, extensible<br><br>Calculate the trend of building volume<br><br>![image 46](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile46.png)<br><br>Tool 1<br><br>![image 47](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile47.png)<br><br>Tool 2<br><br><br>![image 48](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile48.png)<br><br>![image 49](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile49.png)<br><br>![image 50](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile50.png)<br><br>Tool n<br><br>...<br><br>Final Answer<br><br>![image 51](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile51.png)<br><br>![image 52](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile52.png)<br><br>5. Systemic evaluation: trajectory & result<br>|


Pretrained-

-

MLLM

MLLM

...

...

Earth- Earth-

Earth-Bench Earth-Agent Evaluation

![image 53](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile53.png)

![image 54](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile54.png)

![image 55](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile55.png)

![image 56](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile56.png)

Annotations

248 expert-curated Questions

- Answer

Query LLM Toolkit

13729 Images

Answer

Step by Step

|Final Answer Reference steps<br><br>name input params output params|
|---|


![image 57](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile57.png)

![image 58](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile58.png)

Spectrum

-

![image 59](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile59.png)

![image 60](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile60.png)

Response

Tools_any_order Tools_in_order Tools_exact_match Parameters

![image 61](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile61.png)

![image 62](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile62.png)

![image 63](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile63.png)

![image 64](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile64.png)

![image 65](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile65.png)

![image 66](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile66.png)

![image 67](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile67.png)

![image 68](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile68.png)

Folder

Steps

RGB

RGB

![image 69](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile69.png)

![image 70](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile70.png)

Call

End to End

![image 71](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile71.png)

![image 72](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile72.png)

GEE, EarthData

Efficiency

ReAct

Accuracy

RS Dataset

Figure 1: Overview of our work: The top panel contrasts prior paradigms: MLLM-based EO research (left), Existing agent-based EO research (middle), and our Earth-Agent (right). The bottom panel illustrates our contributions, including Earth-Bench construction, Earth-Agent ReAct with the predefined toolkit, and dual-level evaluation of both reasoning trajectories and final results.

ABSTRACT

Earth observation (EO) is essential for understanding the evolving states of the Earth system. Although recent MLLMs have advanced EO research, they still lack the capability to tackle complex tasks that require multi-step reasoning and the use of domain-specific tools. Agent-based methods offer a promising direction, but current attempts remain in their infancy, confined to RGB perception, shallow reasoning, and lacking systematic evaluation protocols. To overcome these limitations, we introduce Earth-Agent, the first agentic framework that unifies RGB and spectral EO data within an MCP-based tool ecosystem, enabling cross-modal, multi-step, and quantitative spatiotemporal reasoning beyond pretrained MLLMs. Earth-Agent supports complex scientific tasks such as geophysical parameter retrieval and quantitative spatiotemporal analysis by dynamically invoking expert

*Equal contribution. ‡This work was done during their internship at OpenDataLab of Shanghai AI Lab. †Corresponding author. E-mail: liweijia@sz.tsinghua.edu.cn

tools and models across modalities. To support comprehensive evaluation, we further propose Earth-Bench, a benchmark of 248 expert-curated tasks with 13,729 images, spanning spectrum, products and RGB modalities, and equipped with a dual-level evaluation protocol that assesses both reasoning trajectories and final outcomes. We conduct comprehensive experiments varying different LLM backbones, comparisons with general agent frameworks, and comparisons with MLLMs on remote sensing benchmarks, demonstrating both the effectiveness and potential of Earth-Agent. Earth-Agent establishes a new paradigm for EO analysis, moving the field toward scientifically grounded, next-generation applications of LLMs in Earth observation. More information about Earth-Agent can be found at https://github.com/opendatalab/Earth-Agent

- 1 INTRODUCTION


Earth observation (EO) (Transon et al., 2018; Kokkoris et al., 2024; Li et al., 2023a) plays a critical role in understanding the evolving states of the Earth system in spatial and temporal dimensions (Anderson et al., 2017; Li et al., 2024a; Brown et al., 2025), and has been successfully applied to urban planning (Shaker et al., 2019), agriculture (W´ojtowicz et al., 2016), resources management (Li et al., 2020; Wang et al., 2025a), building extraction (Li et al., 2023b; 2024c), disaster monitoring (Joyce et al., 2009; Van Westen, 2000), etc. Typically, EO data is categorized into two types (Samadzadegan et al., 2025): Perceptual data, such as RGB Imagery (RGB) aligned with human vision, and Raw Observational Data, including Raw Spectral Data (Spectrum) and Processed Earth Products (Products) stored in geodatabases such as Google Earth Engine (GEE)* and NASA Earthdata†. Both types of data are indispensable for EO research: perceptual data provides intuitive and human-interpretable insights, while raw observational data offers rich spectral and spatiotemporal information that enables quantitative analysis (Valipour et al., 2025; Xiong et al., 2022).

In recent years, multimodal large language models (MLLMs) have achieved excellent performance on classical remote sensing perceptual tasks such as VQA (Kuckreja et al., 2024; Muhtar et al.,

- 2024), scene classification (Kuckreja et al., 2024; Muhtar et al., 2024; Liu et al., 2024c; Wang et al., 2024e; Hu et al., 2025b; Zhan et al., 2025), object detection (Zhang et al., 2024b), and semantic segmentation (Mall et al., 2023; Guo et al., 2024a). However, despite their promising results, existing MLLM-based EO research still faces several fundamental drawbacks: (1) they cannot process diverse EO modalities beyond RGB, such as thermal infrared (TIR), synthetic aperture radar (SAR), or hyperspectral imagery (Zhang et al., 2024b); (2) they typically operate on only one or a few images at a time (Li et al., 2024b), making it difficult to scale to large EO corpora; (3) they are limited to executing only single-step or shallow reasoning like VQA and classification, struggling with complex multi-hop analytical tasks; and (4) their reasoning is bounded by the static knowledge encoded in pretrained parameters, without the ability to integrate external scientific tools or expert models, making it difficult to extend beyond the generic capabilities of the foundation model; This naturally raises the question: how can we move beyond basic RGB perception and single-step reasoning to design models that integrate diverse EO modalities and support complex multi-step scientific analysis?

Tool-augmented LLM agents represent a promising trajectory beyond MLLMs (Xi et al., 2025; Sun et al., 2025; Si et al., 2024; Tian et al., 2024; Tang et al., 2025). Unlike MLLMs that are restricted to RGB inputs, simple reasoning, and limited image contexts, agents are not inherently constrained by input modality or data volume (Xie et al., 2024; Gao et al., 2024). By leveraging the reasoning capabilities of LLMs and dynamically interacting with external tools (Xu et al., 2025), they can flexibly process diverse EO modalities, perform multi-step analytical reasoning, and integrate domainspecific tools and expert models that go beyond the scope of the pretrained MLLM model (Ding et al., 2025; Wang et al., 2024c). This mechanism directly tackles the core weaknesses of MLLMs, extending beyond RGB to diverse modalities, scaling from single-image inputs to tasks involving hundreds of images, advancing from shallow perception to multi-step reasoning, and bridging LLMs with external scientific tools for domain-specific analysis.

However, existing agent-based research in Earth science is still at an early stage (Pantiukhin et al.,

- 2025), with existing attempts largely confined to perceptual tasks such as change detection (Liu


*https://earthengine.google.com †https://search.earthdata.nasa.gov

et al., 2024b; 2025) and classification (Xu et al., 2024a; Hu et al., 2025a), often emphasizing caption ability rather than scientific analysis. Efforts on Raw Observational Data are even more limited. UnivEarth (Kao et al., 2025) considers EO data from GEE but operates essentially as a code generation agent, without implementing genuine tool calling, making it difficult to handle complex and realistic geoscientific analysis tasks that require professional tool use. These efforts reveal several key limitations: (1) current EO agents support only limited data modalities, with most efforts still centered on conventional remote sensing datasets dominated by RGB imagery (Xu et al., 2024a); (2) their tool usage remains shallow, limited to a few expert models and reasoning steps, even some agents lack a predefined tool ecosystem, making them insufficient for complex analytical workflows (Shabbir et al., 2025); and (3) their evaluation remains unsystematic, with emphasis only on final answers while overlooking reasoning trajectory. This raises another question: how can we design an EO agent with a structured tool ecosystem and systematic evaluation, capable of bridging perceptual and spectral data like Earth scientists?

###### Spectrum Products RGB

![image 73](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile73.png)

![image 74](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile74.png)

![image 75](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile75.png)

To support international maritime planning, calculate the difference between the harbor areas of the two images (GSD: A = 0.50m/px, B = 0.30m/px).

Based on the temperature and vegetation indicators (LST and NDVI) in the Yellow River Basin region from June to September 2023, calculate the number of spikes in the drought index, which may correspond to severe drought events.

Analyze the nighttime light intensity trend in Leon (2013-2024) using linear regression.

- A. Slope: 0.10; Intercept: 1.85
- B. Slope: 0.12; Intercept: 1.96
- C. Slope: 0.14; Intercept: 2.05
- D. Slope: 0.16; Intercept: 2.12


B. 15000 C. 20000 D. 30000

A. 10000

A. 1 B. 2 C. 5 D. 6

get_filelist SM3Det

![image 76](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile76.png)

![image 77](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile77.png)

![image 78](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile78.png)

get_filelist compute_tvdi

![image 79](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile79.png)

![image 80](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile80.png)

![image 81](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile81.png)

get_filelist calc_batch_ image_mean

![image 82](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile82.png)

![image 83](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile83.png)

![image 84](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile84.png)

![image 85](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile85.png)

![image 86](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile86.png)

calculate_area SAM2

![image 87](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile87.png)

![image 88](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile88.png)

![image 89](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile89.png)

count_spikes _from_values

![image 90](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile90.png)

calc_batch_ image_mean

![image 91](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile91.png)

![image 92](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile92.png)

![image 93](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile93.png)

Final Answer: B

![image 94](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile94.png)

compute_ linear_trend

![image 95](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile95.png)

![image 96](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile96.png)

![image 97](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile97.png)

###### difference Final Answer : D

![image 98](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile98.png)

![image 99](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile99.png)

Final Answer : B

- Figure 2: Earth-Agent solving tasks across Spectrum, Products, and RGB data through multi-step reasoning with expert tool calls.


To address these questions and unlock the full landscape of EO, we propose Earth-Agent, an agentic framework that unifies perceptual and spectral EO data within a single architecture in section 3. By coupling LLM reasoning with a structured toolkit in 3.2, Earth-Agent supports diverse modalities and complex multi-step analysis, enabling agents to tackle real-world geoscientific tasks beyond the limits of existing MLLMs and EO agents. Concretely, Earth-Agent integrates 104 specialized tools, built upon the Model Context Protocol (MCP) (Hou et al., 2025; Ray, 2025) for interoperability, and grouped into five domain-specific tool kits: Index, Inversion, Perception, Analysis, and Statistics. This structured design not only enables the agent to go beyond classical perceptual tasks toward quantitative analysis and spatiotemporal reasoning, but also makes the framework easily extensible with additional domain-specific tools. To systematically evaluate its effectiveness, we further introduce Earth-Agent Benchmark (Earth-Bench) in section 4, which reflects realistic EO workflows and supports both Auto-Planning and Instruction-Following query regimes, together with a dual-level evaluation protocol that measures reasoning trajectories as well as final outcomes. We comprehensively evaluate Earth-Agent by varying LLM backbones on Earth-Bench, comparing with general agents, and benchmarking against MLLMs on remote sensing datasets.

To sum up, our main contributions are summarized as follows:

- • We propose Earth-Agent, the first agentic framework for EO, built upon the MCP and a ReAct (Yao et al., 2023) reasoning, integrating 104 specialized tools and expert models within predefined tool ecosystem, while remaining easily extensible with additional domain-specific tools and models.
- • We construct Earth-Bench, a benchmark of 248 expert-curated questions with 13,729 images, spanning perceptual and spectral modalities beyond RGB. Each question requires multi-step reasoning with explicit tool use, and the benchmark supports a dual-level evaluation protocol that assesses both reasoning trajectories and final answers.
- • Through comprehensive evaluation, we show that Earth-Agent substantially outperforms general agents such as Operator (OpenAI, 2025b) and Manus (Shen et al., 2025) on Earthspecific tasks in Earth-Bench, and also surpasses remote sensing MLLMs on remote sensing benchmarks, demonstrating both its effectiveness and potential for advancing EO research.


- 2 RELETED WORK

MLLM-based Earth Observation Research The rise of multimodal large language models (MLLMs) has stimulated growing interest in their use for Earth observation (EO) (Aleissaee et al., 2023; Lu et al., 2025; Li et al., 2024b). Early studies mainly explored captioning (Hu et al., 2025b) and question answering (Kuckreja et al., 2024) for single remote sensing images (Shi & Zou, 2017; Wang et al., 2020), aiming to align visual features with natural language. With the availability of larger datasets (Xiong et al., 2022; Zhou et al., 2025) and stronger backbones (Team, 2024; Liu

- et al., 2024d), subsequent works extended this paradigm to broader perception tasks: for instance, GeoChat (Kuckreja et al., 2024) enabled interactive scene understanding, while RS-GPT (Hu et al., 2025b) combined captioning with visual question answering. More recently, simple temporal reasoning has been introduced, with ChangeCLIP (Dong et al., 2024) addressing bi-temporal change captioning and SkyEye-GPT (Zhan et al., 2025) extending to video-based analysis. However, the scope of MLLM-based EO research remains narrow: existing approaches are still centered on RGB imagery and struggle with complex multi-step reasoning without domain-specific tool integration.

Agent-based Earth Observation Research. Tool-augmented agents have gained traction in general AI, achieving remarkable progress in domains such as code generation (Qian & Cong, 2023; Zhang et al., 2024a), web search (Xu et al., 2024b), and video understanding (Ren et al., 2025; Wang et al., 2024d), but their application to Earth observation (EO) is still at an early stage (Kao

- et al., 2025). Early systems such as Change-Agent (Liu et al., 2024b) focus on bi-temporal change detection, while RS-ChatGPT (Guo et al., 2024a) and RS-Agent (Xu et al., 2024a) combine LLMs with pretrained detectors or tool suites for scene classification, detection, and segmentation. More recently, ThinkGeo (Shabbir et al., 2025) introduces agentic workflows for simple geospatial calculations on perceptual data, and UnivEarth (Kao et al., 2025) requires LLMs to generate GEE code for spectral analysis, with high execution failure rates. Despite these advances, existing EO agents remain constrained: they operate mainly on RGB perception tasks, rely on remote sensing models for simple reasoning that does not extend to multi-step analysis, and lack a predefined tool ecosystem, making them insufficient for complex real-world geoscientific workflows. Moreover, current benchmarks cover limited task types and annotations, lacking systematic evaluation protocols that assess both the correctness of outcomes and the quality of reasoning trajectories. As a result, current frameworks remain limited in modality coverage, constrained to shallow reasoning with remote sensing models, and hindered by the absence of a predefined tool ecosystem, highlighting the necessity for EO agents and benchmarks that support diverse data, multi-step analytical workflows, and systematic evaluation.


- 3 EARTH-AGENT FRAMEWORK


In this section, we detail the operation mechanisms of Earth-Agent. We first formulate its operation pipeline as a ReAct-style (Yao et al., 2023) Partially Observable Markov Decision Processes (POMDP) formulation (Huang et al., 2024; Chala et al., 2025) in section 3.1 , including the observation process, policy reasoning and memory update, as shown in Figure 3. Then we introduce the functionality of the specialized tool kits that enable EO analysis across perceptual and spectral data in section 3.2. Finally, we define the dual-level evaluation protocol, which assesses EO agents in both end-to-end and step-by-step modes to evaluate not only final accuracy but also reasoning trajectories in section 3.3.

- 3.1 OPERATION MECHANISMS


Earth-Agent receives a task goal g, interprets user queries and intermediate tool outputs, and selects actions from a modular toolkit to progressively solve the task. This process is formulated as a POMDP, defined by the tuple ⟨g,S,A,O,T ⟩, where g is the task goal, S is the state space (unobservable environment status such as geospatial data files or raster values), A is the action space (tool calls in the kit), O is the observation space (outputs returned by tools, including text, numerical values, and images), and T : S × A → S is the state transition function.

At each time step t, given a policy π, the agent selects an action conditioned on the goal g and its interaction history, which records past observations and actions:

###### mt = (o0,a0,o1,a1,...,ot),





###### Query Folder

###### Query Folder

Based on the built_volume_total and built_volume_nres data of Shanghai from 1980 to 2025, calculate the linear trend of the overall change in residential volume in Shanghai from 1980 to 2025.

0 0













<Folder>

















...

- A. 267.13 units/year, showing a strong increasing trend









20 images

...

- B. 134.57 units/year, showing a weak increasing trend
- C. 107.95 units/year, showing a slight decreasing trend
- D. 570.72 units/year, showing a rapid increasing trend


267.13

Call Response ReAct

<tool> <tool>

<tool>get_filelist<tool>

- Step1:
- Step2:
- Step3:
- Step4:






Input Params: {dir_path: "data/question187"} Output Params:

Input Params: { :

{built_volume_nres_1980,...,built_volume_total_2025}

:

<tool> <tool>

<tool>subtract<tool>

Input Params: { , , } Output Params: }

Input Params: {img1_path, img2_path, output_path} Output Params: {residential_volume_1980,...residential_volume_2025}

<tool> <tool>

<tool>calc_batch_image_mean<tool>









Input Params: { : } Output Params: { }

Input Params: {file_list: residential_volume_1980, ...} Output Params: {5146.838867,...13707.931641}













<tool> <tool>

<tool>compute_linear_trend<tool>

Input Params: { : : } Index Inversion Perception Analysis Statistics Output Params:{267.13}

Input Params: {y: [5146.838867,...13707.931641], x: [1980,...2025]} Index Inversion Perception Analysis Statistics Output Params:{267.13}

12 18 15 10 49

###### 12 18 15 10 49

<Answer>A<Answer>

<Answer>A<Answer>

Answer:

Published as a conference paper at ICLR 2026

![image 132](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile132.png)

![image 133](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile133.png)

![image 134](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile134.png)

![image 135](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile135.png)

![image 136](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile136.png)

![image 137](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile137.png)

Things happen before step t+1

t+1

Query

Query

![image 138](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile138.png)

![image 139](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile139.png)

![image 140](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile140.png)

![image 141](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile141.png)

Things happen after step t+1

t+1

Folder

Folder

###### Dual-level Evaluation

###### -

③ Think

| |......<br><br>| |......<br><br>| |
|---|---|---|---|---|


|Memory| | |......| || |
|---|
<br><br>|......| | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|


Tool Trajectory

###### Memory

Action

Updata②

④

“name”(t) “ ”(t) “ ”(t)

“name”(t) “input”(t) “output”(t)

Annotations

Annotations

|Step- -Step<br><br>[A,D,C,B] [A,D,B ]<br><br>√<br><br>×<br><br>[A,D,B,C]<br>[A,D,C,B] [A,B,C] [A,D,B,C]<br><br><br>√<br><br>×<br><br>√<br><br>×<br><br>Step-by-Step<br><br>Tools_any_order Tools_in_order Tools_exact_match<br><br>Parameters<br><br>Expected Tools: [A,B,C]<br><br>[A,D,C,B] [A,D,B,F]<br><br>√<br><br>×Not include all tools<br><br>[A,D,B,C]<br>[A,D,C,B] Not call in order [A,B,C] [A,D,B,C] Not exact match<br><br><br>A(input,output) = GT<br>B(input,output) = GT<br>C(input,output) ≠ GT<br><br><br>0.67 Score<br><br>√<br><br>×<br><br>√<br><br>×|
|---|


|name<br><br>Reference steps<br><br>name input params output params<br><br>|
|---|


![image 142](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile142.png)

![image 143](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile143.png)

![image 144](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile144.png)

![image 145](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile145.png)

![image 146](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile146.png)

![image 147](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile147.png)

|End-End-to-End-End<br><br>Efficiency<br><br>Accuracy<br><br>|
|---|


![image 148](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile148.png)

![image 149](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile149.png)

![image 150](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile150.png)

![image 151](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile151.png)

![image 152](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile152.png)

![image 153](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile153.png)

Annotations

Annotations

|Final Answer<br><br>|
|---|


Index Inversion Perception Analysis Statistics 12 18 15 10 49

Index Inversion Perception Analysis Statistics 12 18 15 10 49

- Figure 3: Earth-Agent Framework: The left part illustrates the ReAct-style workflow, where Earth-Agent iteratively performs tool calling, memory update, thinking, and action using domainspecific toolkits. The right panel presents the dual-level evaluation protocol, assessing both step-bystep reasoning trajectories and end-to-end outcomes.


The action distribution is modeled as:

at ∼ π(at | g,mt).

The full agent trajectory τ = [s0,o0,a0,s1,o1,a1,...,sT,oT] is determined jointly by the policy π and the environment dynamics:

① Tool calling Z(ot+1 | st+1)T (st+1 | st,at)

T−1

###### pπ(τ) = p(s0)Z(o0 | s0)

π(at | g,mt)

###### .

t=0

Initial state

③ Think & ④ Action

where Z denotes the observation distribution induced by tool outputs.

In this formulation, the LLM controller functions as the policy π, reasoning over the history mt and task goal g to decide the next tool calling, while the Toolkit provides executable atomic actions categorized into Index, Inversion, Perception, Analysis, and Statistics. Concretely, as illustrated in Figure 3, each loop proceeds as follows: ① Tool calling At step t, the agent invokes the most suitable tool conditioned on the current memory mt and task goal g, which yields the tool response for observation ot+1. ② Memory update At step t, the agent appends the pair (ot,at) together with the resulting observation ot+1 into the memory stack, ensuring that the complete interaction history is preserved for subsequent reasoning. ③ Think At step t+1, the LLM controller reasons over the updated memory mt together with the task goal g to plan the next action, determining which tool to invoke and how to configure its inputs. ④ Action Selecting and executing the subsequent tool call at+1 that produces ot+2. The ReAct loop continues until the stopping condition is satisfied, yielding both the final answer and a reproducible sequence of tool calling trajectory.

- 3.2 TOOL KIT


To enable comprehensive EO analysis, Earth-Agent integrates 104 specialized tools organized into five functional kits. The Index kit provides implementations of widely used EO indices (e.g., NDVI, NDWI, NBR) (Montero et al., 2023) for rapid environmental characterization. The Inversion kit focuses on geophysical parameter retrieval, including land surface temperature (LST) (Li et al., 2013),

precipitable water vapor (PWV) (He & Liu, 2020), vegetation water content (Ceccato et al., 2001), sea ice concentration (DiGirolamo et al., 2022), and others. The Perception kit supports visionoriented tasks such as scene classification (Ma et al., 2025), object detection (Li et al., 2024e), and segmentation (Ravi et al., 2024). The Analysis kit targets spatiotemporal reasoning, offering trend detection, seasonality decomposition, change point analysis, and spatial autocorrelation. Finally, the Statistics kit provides large-scale data preprocessing and statistical computation (e.g., variance, skewness, batch operations, cloud masking). Together, these tool kits cover the diverse types of EO tasks from perceptual to spectral, and from descriptive to quantitative analysis. The detailed list and description of tools can be found in Appendix G.

- 3.3 EVALUATION PROTOCOL

Prior benchmarks have primarily emphasized final accuracy, overlooking the reasoning trajectory that leads to the final output (Mialon et al., 2023; Jimenez et al., 2024; Chen et al., 2025). To address this, we adopt a dual-level evaluation protocol: agents are assessed in a step-by-step mode to capture the quality of their reasoning trajectories, and in an end-to-end mode to measure final task performance. This dual perspective enables fine-grained diagnostics of both reasoning and outcomes. The detailed calculation formulas can be found in Appendix B.2.

End-to-End evaluation measures task-level performance, including Accuracy of the final answer and Efficiency of the trajectory relative to expert solutions.

Step-by-Step evaluation assesses the quality of intermediate reasoning. We consider four complementary aspects: Tool-Any-Order, which checks whether all necessary tools are used in LLM planning; Tool-In-Order, which evaluates whether tools are invoked in the correct sequence; ToolExact-Match, which evaluates the exact prefix-level accuracy between the predicted and expert trajectories; and Parameter Accuracy, which verifies whether both tool identifiers and their arguments are correctly matched.

- 4 EARTH-AGENT BENCHMARK


- 4.1 OVERVIEW OF EARTH-AGENT BENCHMARK


We introduce Earth-Agent Benchmark (Earth-Bench), a dataset designed to evaluate toolaugmented EO agents in realistic Earth science analysis scenarios. The benchmark integrates three major types of Earth observation data: RGB Imagery (RGB), Raw Spectral Data (Spectrum), and Processed Earth Products (Products). It supports 14 representative tasks, including classification, detection, temperature monitoring, weather forecasting, etc., with a particular emphasis on scientific analysis that requires quantitative reasoning rather than qualitative description.

![image 154](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile154.png)

![image 155](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile155.png)

Cross Modality

Image Samples

Requiring Tools

Reasoning Steps

Quantitative Analysis

Trajectory Eval.

Cassfcaton

Dataset

![image 156](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile156.png)

etection

Temperature Monitoring

![image 157](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile157.png)

Questions 248

Grounding

D

![image 158](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile158.png)

RSVQA-HR 1.7M 1

![image 159](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile159.png)

![image 160](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile160.png)

![image 161](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile161.png)

Weather Forecasting Climate

![image 162](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile162.png)

Images 13729

![image 163](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile163.png)

![image 164](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile164.png)

Segmentation

RGB

![image 165](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile165.png)

![image 166](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile166.png)

![image 167](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile167.png)

![image 168](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile168.png)

![image 169](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile169.png)

EarthVQA 6K 1

Spectrum

Analysis

![image 170](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile170.png)

Average per Question 55.4

Counting

Water Management

![image 171](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile171.png)

VRSBench 103K 1

![image 172](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile172.png)

![image 173](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile173.png)

![image 174](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile174.png)

![image 175](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile175.png)

Maximum per Ques. 670 Steps 1345

Products

Change Detection

Polution Regulation

Vegetation

tn

![image 176](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile176.png)

![image 177](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile177.png)

Monitoring

![image 178](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile178.png)

Geo-Bench 1.5M 1

![image 179](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile179.png)

e

nt

m

n

er

a

e

![image 180](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile180.png)

e

Average per Ques. 5.42 Maximum per Ques. 19

b

Disast

m

g

rU

a

- d

g

- e


n

a

M

u

J

PEACE 0.12K 1

![image 181](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile181.png)

![image 182](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile182.png)

![image 183](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile183.png)

![image 184](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile184.png)

![image 185](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile185.png)

![image 186](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile186.png)

###### 80 Specturm Products RGB

Thinkgeo 0.3K 14 <3

![image 187](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile187.png)

![image 188](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile188.png)

![image 189](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile189.png)

74

![image 190](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile190.png)

70

61

60

61

59

![image 191](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile191.png)

55

55

60

![image 192](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile192.png)

![image 193](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile193.png)

55

![image 194](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile194.png)

![image 195](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile195.png)

![image 196](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile196.png)

Univearth - 1

52

![image 197](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile197.png)

![image 198](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile198.png)

![image 199](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile199.png)

50

![image 200](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile200.png)

![image 201](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile201.png)

46

48

47

![image 202](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile202.png)

![image 203](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile203.png)

50

45

![image 204](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile204.png)

![image 205](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile205.png)

![image 206](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile206.png)

![image 207](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile207.png)

38

40

![image 208](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile208.png)

Earth-Bench (Ours)

![image 209](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile209.png)

![image 210](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile210.png)

![image 211](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile211.png)

30

13K 104 >5

![image 212](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile212.png)

GPT-5 Gemini-2.5 Kimik2 Deepseek-V3.1 Qwen3-max

- Figure 4: Dataset Comparison and Overview: The left panel compares Earth-Bench with prior MLLM and agentbased EO benchmarks. The right panel presents the statistics of Earth-Bench and its evaluation with SOTA LLMs using Earth-Agent, highlighting the difficulty of Earth-Bench.


- As shown in Figure 4, MLLM-based benchmarks including RSVQA-HR (Lobry et al., 2020), EarthVQA (Wang et al., 2024b), VRSBench (Li et al., 2024d) and Geo-Bench (Lacoste et al.,


- 2023) are mainly limited to single-step perceptual for RGB data using pretrained MLLMs (Liu


et al., 2024d; Team, 2024; OpenAI, 2024), without requiring external tool use for scientific quantitative analysis (e.g., spatiotemporal trend estimation), not to mention reasoning trajectory evaluation. On the other hand, Earth-Bench advances beyond prior Agent-based EO benchmarks, such as PEACE (Huang et al., 2025), Thinkgeo (Shabbir et al., 2025) and UnivEarth (Kao et al., 2025), by incorporating 13K+ images across spectrum, product and RGB modalities, while requiring interaction with 104 domain tools. It consists of 248 expert-curated questions, requiring an average of

- 5.4 reasoning steps of quantitative analysis. Even with the state-of-the-art (SOTA) LLM backbones, performance remains limited, which underscores not only the benchmark’s difficulty and diagnostic value but also the necessity of reasoning trajectory evaluation. Therefore, we need to annotate on both trajectories and final answers in section 4.2.


- 4.2 DATA ANNOTATION PIPELINE


To construct Earth-Bench, we collected raw data from platforms such as Google Earth Engine, NASA EarthData, and public remote sensing datasets (Xia et al., 2017; Zhan et al., 2023; Xia et al., 2018; Su et al., 2019). From these data sources, a team of domain experts curated 248 problems that require multi-step quantitative reasoning. The annotation team was composed of 2 computer science experts, 7 remote sensing specialists, and 3 Earth science specialists. Each problem is accompanied by a step-by-step Python solution and is designed to reflect the complexity of real-world Earth science workflows, which demand the coordinated use of multiple tool kits.

In prior benchmarks, queries have been designed either as step-implicit, where no intermediate step guidance is provided (Mialon et al., 2023; Wang et al., 2024a), or as step-explicit, where the query itself contains step guidance (Guo et al., 2024b; Ma et al., 2024). Motivated by the complexity of EO workflows, which often require multi-step processing, Earth-Bench incorporates both regimes: Auto-Planning corresponds to the step-implicit setting and evaluates the agent’s ability to autonomously plan its solution trajectory, while Instruction-Following corresponds to the stepexplicit setting and evaluates the agent’s ability to follow and translate human instructions into executable actions. Both regimes contain 248 complete questions for evaluation. Together, these two regimes provide a comprehensive assessment of both autonomous reasoning and guided execution in EO contexts. Details can refer to Appendix A.4.

###### Question Construction Data Annotation

![image 213](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile213.png)

![image 214](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile214.png)

![image 215](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile215.png)

![image 216](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile216.png)

![image 217](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile217.png)

![image 218](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile218.png)

Google Earth Engine

###### Question Generation

NASA Earth Data

###### Python Solution Python Result Json Annotation

![image 219](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile219.png)

![image 220](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile220.png)

![image 221](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile221.png)

![image 222](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile222.png)

![image 223](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile223.png)

![image 224](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile224.png)

![image 225](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile225.png)

![image 226](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile226.png)

![image 227](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile227.png)

![image 228](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile228.png)

![image 229](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile229.png)

![image 230](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile230.png)

![image 231](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile231.png)

![image 232](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile232.png)

![image 233](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile233.png)

![image 234](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile234.png)

|![image 235](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile235.png)<br><br>![image 236](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile236.png)|
|---|


![image 237](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile237.png)

![image 238](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile238.png)

![image 239](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile239.png)

![image 240](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile240.png)

Param.

|![image 241](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile241.png)<br><br>![image 242](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile242.png)|
|---|


![image 243](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile243.png)

![image 244](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile244.png)

![image 245](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile245.png)

<tool>

- Func.1
- Func.2
- Func.3


![image 246](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile246.png)

Img_Path Img_List

![image 247](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile247.png)

![image 248](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile248.png)

![image 249](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile249.png)

Input

![image 250](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile250.png)

Remote Sensing Image Data

![image 251](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile251.png)

![image 252](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile252.png)

![image 253](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile253.png)

![image 254](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile254.png)

![image 255](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile255.png)

![image 256](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile256.png)

& Task

|![image 257](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile257.png)<br><br>![image 258](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile258.png)<br><br>![image 259](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile259.png)<br><br>![image 260](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile260.png)<br><br>AID|
|---|


|![image 261](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile261.png)<br><br>![image 262](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile262.png)<br><br>![image 263](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile263.png)<br><br>![image 264](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile264.png)<br><br>DIOR-<br><br>RSVG|
|---|


|![image 265](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile265.png)<br><br>![image 266](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile266.png)<br><br>![image 267](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile267.png)<br><br>![image 268](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile268.png)<br><br>DOTA|
|---|


|![image 269](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile269.png)<br><br>![image 270](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile270.png)<br><br>![image 271](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile271.png)<br><br>![image 272](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile272.png)<br><br>NWPUVHR10|
|---|


Output

def：

Result

![image 273](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile273.png)

![image 274](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile274.png)

![image 275](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile275.png)

![image 276](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile276.png)

![image 277](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile277.png)

![image 278](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile278.png)

Calculation result

![image 279](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile279.png)

Func.1 Func.2

![image 280](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile280.png)

Answer

![image 281](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile281.png)

Main()

Func.3

###### Example

Tool 1

Tool 2

Tool 3

Output/Input

Output

###### Output/Input

###### Input

![image 282](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile282.png)

![image 283](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile283.png)

![image 284](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile284.png)

![image 285](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile285.png)

![image 286](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile286.png)

![image 287](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile287.png)

![image 288](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile288.png)

![image 289](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile289.png)

Query

![image 290](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile290.png)

![image 291](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile291.png)

![image 292](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile292.png)

bt_path”xx/xx” red_path“xx/xx” nir_path“xx/xx”

”xx_1.tif”

![image 293](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile293.png)

![image 294](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile294.png)

![image 295](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile295.png)

![image 296](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile296.png)

![image 297](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile297.png)

![image 298](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile298.png)

![image 299](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile299.png)

Value: 12

![image 300](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile300.png)

- “xx_2.tif”
- “xx_3.tif”


![image 301](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile301.png)

Path

![image 302](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile302.png)

![image 303](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile303.png)

Using Landsat 8 Band 10 brightness temperature data for 2021, how many days did more than 25% of the Chicago metropolitan area exceed 300 K?

Step 1

Step 2

Step 3

“xx/xx/xx”

![image 304](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile304.png)

![image 305](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile305.png)

![image 306](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile306.png)

![image 307](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile307.png)

![image 308](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile308.png)

![image 309](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile309.png)

![image 310](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile310.png)

![image 311](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile311.png)

![image 312](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile312.png)

![image 313](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile313.png)

![image 314](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile314.png)

![image 315](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile315.png)

![image 316](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile316.png)

![image 317](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile317.png)

![image 318](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile318.png)

![image 319](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile319.png)

###### Calculate

Answer: 12 days

A. 7 days C. 15 Days

B. 12days D. 18 Days

Chicago Landset

![image 320](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile320.png)

![image 321](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile321.png)

![image 322](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile322.png)

![image 323](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile323.png)

![image 324](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile324.png)

![image 325](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile325.png)

data

Figure

Choice

bt + Red nir

- Figure 5: Construction and Annotation of Earth-Bench. The left shows question generation from EO data, the right illustrates the data annotation pipeline that simulates ReAct-style trajectories, and the bottom provides an example explaining the multi-step annotation process.


To enable dual-level evaluation, we explicitly annotated both the final answers and the full reasoning trajectories. As illustrated in Fig. 5, the annotation process was designed to mimic the ReAct loop of agents: Python Solution. Annotators first identify the domain tools such as compute ndwi and split window) required to solve a problem and then assemble them into a step-by-step main() program. Each tool is represented as a Python function, and the functions are planned in the correct order to form an executable workflow that mirrors the agent’s reasoning trajectory. Python Result.

When executed, the program produces explicit input and output arguments for each function call, as well as the final output of the main() function. JSON Annotation. Each function call is then translated into a structured JSON record to align with the ReAct-style trajectory annotation. The function name corresponds to the action tool name, the function input arguments corresponds to the action passed by the agent, and the function output arguments corresponds to the tool responses returned to the agent. The final output of the main() function is recorded as the ground-truth answer for the problem. This provides a complete record of both the reasoning trajectory and the final answer.

- 5 EXPERIMENTS


- 5.1 EXPERIMENTAL SETUP


Evaluated Models. We evaluate 3 closed-source and 10 leading open-source LLMs. For closedsource models, we consider GPT-5 (OpenAI, 2025a), GPT-4o (OpenAI, 2024), and Gemini2.5 (Comanici et al., 2025). For open-source models, including Deepseek-V3.1 (Liu et al.,

- 2024a), Kimik2 (Team et al., 2025), Qwen3-max-Preview, Qwen3-32B (Yang et al., 2025), and InternVL3.5 (Wang et al., 2025b), which represent the smartest open LLMs available to date.


- 5.2 EARTH-AGENT WITH DIFFERENT LLM BACKBONES


As shown in Table 1, we evaluate the impact of different LLM backbones on Earth-Bench. Results are reported under both step-by-step and end-to-end evaluation protocols, allowing us to jointly assess the quality of reasoning trajectories and final outcomes. The following observations can be made:

- Table 1: Performance of different LLM backbones on Earth-Bench under both Auto-Planning (AP) and Instruction-Following (IF) regimes. Results are reported with dual-level evaluation, covering Accuracy, Efficiency for final outcomes and Tool-Any-Order, Tool-In-Order, Tool-Exact-Match, Parameters for trajectory quality. We bold the best results and underline the runner-ups.


Accuracy Efficiency Tool-Any-Order Tool-In-Order Tool-Exact-Match Parameters AP IF AP IF AP IF AP IF AP IF AP IF

Model

GPT-5 65.99 62.35↓ 2.3560 2.9093 68.74 71.41↑ 57.71 61.06↑ 44.97 46.01↑ 26.11 25.91↓ Gemini-2.5 52.23 53.04↑ 2.9958 2.4595 58.04 61.63↑ 45.31 50.72↑ 31.32 41.04↑ 17.26 23.43↑

- GPT-4o 43.72 44.94↑ 2.1211 2.6007 65.65 67.02↑ 50.76 53.04↑ 46.26 47.41↑ 26.55 27.92↑


Kimik2 50.61 56.68↑ 1.8542 2.1793 71.03 78.86↑ 57.57 68.83↑ 42.11 51.15↑ 25.90 30.45↑ DeepSeek-V3.1 51.42 52.23↑ 2.6116 2.6303 78.31 78.66↑ 62.73 64.50↑ 48.54 49.58↑ 30.81 31.36↑ Qwen3-Max 50.20 47.37↓ 1.8810 1.9511↓ 69.56 70.14↑ 53.28 56.02↑ 37.02 42.74↑ 21.83 26.27↑ Seed-1.6 52.48 59.51↑ 1.3110 1.3408↓ 55.43 59.44↑ 40.67 46.79↑ 28.39 35.47↑ 18.32 23.13↑ LLaMA-4 44.94 38.46↓ 0.2886 0.3211↓ 16.51 22.41↑ 2.45 12.05↑ 1.70 9.05↑ 1.30 6.46↑ Qwen-Plus 42.51 38.46↓ 1.5119 1.5854↓ 52.04 55.96↑ 30.75 39.77↑ 11.69 25.51↑ 9.12 16.95↑ GLM-4.5v 32.86 35.25↑ 1.7123 2.0129↓ 42.48 46.69↑ 28.57 35.24↑ 14.12 19.95↑ 11.02 15.37↑ Mistral 29.96 22.67↓ 0.9552 0.8802↑ 27.73 29.64↑ 11.78 20.90↑ 9.13 18.13↑ 7.24 11.66↑ Qwen3-32B 20.65 24.80↑ 2.7274 1.9010↑ 39.76 42.39↑ 21.56 33.79↑ 9.51 26.10↑ 8.17 17.73↑ InternVL-3.5 26.72 26.72 0.1206 0.1750↓ 8.83 16.62↑ 3.87 10.59↑ 2.02 9.32↑ 1.46 5.32↑

- Obs.1. LLM models pretrained with tool calling, such as GPT-5, Gemini-2.5, DeepSeek-V3.1, Kimik2, and Qwen3, demonstrate strong performance across both step-by-step and end-to-end evaluations. Further, closed-source models like GPT-5 typically achieve higher final accuracy, while open-source models, particularly DeepSeek-V3.1 and Kimik2, outperform GPT-5 in tool-use accuracy, demonstrating superior performance in reasoning trajectory alignment. We have provided a detailed analysis of the LLMs’ performance across the Spectrum, Products, and RGB modalities, which can be found in Appendix C.
- Obs.2. Instruction-following regimes enhance tool calling by providing explicit step guidance in the query, leading to improved tool calling accuracy across nearly all models. Interestingly, despite the improved reasoning trajectories, this does not necessarily lead to higher final accuracy. In fact, for some advanced models, this added complexity may even result in a decrease in final accuracy. We have conducted a detailed error analysis of Earth-Agent’s performance in the Earth-Bench benchmark, focusing on representative models such as GPT-5, DeepSeek-V3.1, Kimik2, and Qwen3-max. This can be found in Appendix D.


- Obs.3. Across nearly all models, the ability to identify the correct set of tools, as reflected in Tool-Any-Order and Tool-In-Order metrics, remains consistently strong. However, models often introduce irrelevant steps during reasoning, which undermines their accuracy on Tool-Exact-Match and parameter execution. Crucially, these two fine-grained capabilities are indispensable in real EO analysis workflows. For example, if additional transformations are mistakenly applied to the EO data process, it becomes extremely difficult to obtain correct results in the subsequent steps. Their weakness therefore exposes a key bottleneck that prevents EO Agents from achieving higher final accuracy in EO data processing.


- 5.3 COMPARISON WITH GENERAL AGENTS

Since many Earth-Bench tasks involve processing hundreds of images, existing open-source agent frameworks cannot handle these questions due to input size constraints. To enable fair comparison, we construct Earth-Bench-Lite, a reduced yet representative subset that preserves modality diversity while remaining within the capacity of general-purpose agents. It consists of 60 questions evenly distributed across the three EO modalities: Spectrum, Products, and RGB. As shown in Table 2, we report results across three modalities: Spectrum, Products, and RGB.

- Table 2: Comparison with general agents on Earth-Bench-Lite. Results are reported across Spectrum, Products, RGB modalities. We bold the best results and underline the runner-ups.

|Method<br><br>|Spectrum Products RGB Avg.<br><br>|Latency|
|---|---|---|
|GPT-Agent MGX Manus Coze|45.00 31.60 45.26 40.42 40.00 15.80 0.00 18.60 15.00 15.80 47.62 26.14 35.00 10.50 0.00 15.30<br><br>|≈ 300 min ≈ 60 min ≈ 150 min ≈ 120 min|
|Earth-Agent(GPT5) Earth-Agent(Deepseek-V3.1) Earth-Agent(Kimik2)|65.00 36.84 65.71 55.83 50.00 42.11 51.43 47.84 36.84 50.00 50.00 45.95<br><br>|158 min 79 min 131 min<br><br>|


By comparison, general agents show limited modality coverage. They can handle relatively simple Spectrum tasks by writing ad-hoc code, but perform poorly on Products tasks due to the lack of domain-specific spatiotemporal analysis tools. For the RGB modality, MGX and Coze even fail to complete any tasks. In contrast, by interacting with 104 predefined geoscience tools, Earth-Agent consistently achieves superior performance across all three modalities, whether driven by the closedsource GPT-5 or the open-source DeepSeek-V3.1. We also compared the latency of our Earth-Agent framework with that of the baseline agents. The latency remains within a reasonable range when compared to existing general agents. The substantial performance improvements in task completion more than justify the additional computational cost. A detailed discussion can be found in the Appendix E.

5.4 COMPARISON WITH MLLM-BASED EO METHODS We further compare Earth-Agent with remote sensing large models on classification, detection, and segmentation tasks. The results are summarized in Table 3.

- Table 3: Comparison with MLLMs on Remote sense benchmarks. Results are reported on classification, detection, and segmentation tasks. We bold the best results and underline the runner-ups.




|Model|Classification AID WHU-RS19<br><br>|Detection DOTA HRSC2016<br><br>|Grounding DIOR-RSVG<br><br>|
|---|---|---|---|
|MiniGPT-v2 (Chen et al., 2023) LLaVA-1.5 (Liu et al., 2024d) Sphinx (Lin et al., 2023) Geochat (Kuckreja et al., 2024) VHM (Pang et al., 2025) LHRS-Bot (Muhtar et al., 2024)<br><br>|32.96 64.80 51.00 74.52 58.20 72.03 86.47 91.70 95.80 91.26 93.17<br><br>|14.8 24.8 17.5 22.1<br><br>15.1 25.7<br><br>16.5 24.0<br><br>- -<br><br>17.1 24.4<br><br><br>|29.892 12.085 0.939 10.024 11.826<br><br>|
|Earth-Agent (ours)|93.42 96.12<br><br>|60.88 65.60|60.46|


Earth-Agent demonstrates clear superiority over existing MLLMs across classification, detection, and segmentation benchmarks (Table 3). Prior MLLM-based approaches often lack generalization

across diverse EO tasks: for example, LHRS-Bot achieves strong results in classification but struggles on detection and grounding, while VHM attains high classification accuracy but cannot even handle detection or segmentation tasks. In contrast, Earth-Agent interacts with a predefined toolkit of 104 geoscience functions and expert models, allowing it to adaptively invoke specialized tools or models for each task type. This modular design enables Earth-Agent to maintain robust performance across modalities, overcoming the limited extensibility of previous MLLM-based EO systems.

- 6 CONCLUSION


Earth-Agent marks a significant advancement in applying (M)LLMs to EO analysis, extending RGB perception to Spectrum, Products and RGB modalities. By shifting from single-step inference with pretrained MLLMs to multi-step reasoning through external tool/model integration, it overcomes key limitations of prior MLLM-based approaches, such as handling numerous image inputs and quantitative spatiotemporal analysis. To support rigorous evaluation, we introduced Earth-Bench, which requires multi-step quantitative reasoning and dual-level evaluation, which evaluate both reasoning trajectories and final outcomes. Our experiments further reveal the current bottlenecks of Earth-Agent in EO applications and provide detailed diagnostics. Finally, by comparing with both general agents and domain MLLMs, we highlight the transformative potential of Earth-Agent as a foundation for the revolutio of LLM applications in Earth observation.

ETHICS STATEMENT

This work adheres to the ICLR Code of Ethics. In this study, no human subjects or animal experimentation was involved. All datasets used, including GEE, NASA EarthData, AID, DOTA, HRSC2016, DIOR-RSVG, were sourced in compliance with relevant usage guidelines, ensuring no violation of privacy. We have taken care to avoid any biases or discriminatory outcomes in our research process. No personally identifiable information was used, and no experiments were conducted that could raise privacy or security concerns. We are committed to maintaining transparency and integrity throughout the research process.

REPRODICIBILITY STATEMENT

We are committed to ensuring the full reproducibility of our work. The proposed Agent framework is described in Section 3, while the evaluated models and metrics are detailed in Appendix B. To further support transparency, we will release our codebase, which includes the Agent framework, evaluation scripts, and other relevant components, and we will also provide the evaluation logs from the agent experiments, enabling the community to replicate our results and build upon them.

ACKNOWLEDGEMENTS

This project was funded by National Natural Science Foundation of China (Grant No. 62571560) and Shanghai AI Laboratory.

REFERENCES

Abdulaziz Amer Aleissaee, Amandeep Kumar, Rao Muhammad Anwer, Salman Khan, Hisham Cholakkal, Gui-Song Xia, and Fahad Shahbaz Khan. Transformers in remote sensing: A survey. Remote Sensing, 15(7):1860, 2023.

Katherine Anderson, Barbara Ryan, William Sonntag, Argyro Kavvada, and Lawrence Friedl. Earth observation in service of the 2030 agenda for sustainable development. Geo-spatial Information Science, 20(2):77–96, 2017.

Christopher F Brown, Michal R Kazmierski, Valerie J Pasquarella, William J Rucklidge, Masha Samsikova, Chenhui Zhang, Evan Shelhamer, Estefania Lahera, Olivia Wiles, Simon Ilyushchenko, et al. Alphaearth foundations: An embedding field model for accurate and efficient global mapping from sparse label data. arXiv preprint arXiv:2507.22291, 2025.

Pietro Ceccato, St´ephane Flasse, Stefano Tarantola, St´ephane Jacquemoud, and Jean-Marie Gr´egoire. Detecting vegetation leaf water content using reflectance in the optical domain. Remote Sensing of Environment, 77(1):22–33, 2001. ISSN 0034-4257. doi: https://doi.org/10. 1016/S0034-4257(01)00191-2. URL https://www.sciencedirect.com/science/ article/pii/S0034425701001912.

Olena Chala, Vladyslav Yevsieiev, Svitlana Maksymova, and Amer Abu-Jassar. Mathematical model based on multi-agent reinforcement learning (marl) and partially observable markov decision process (pomdp) for modeling cargo movement for a mobile robots group. Multidisciplinary Journal of Science and Technology, 5(4):480–489, 2025.

Chen Chen, Xinlong Hao, Weiwen Liu, Xu Huang, Xingshan Zeng, Shuai Yu, Dexun Li, Shuai Wang, Weinan Gan, Yuefeng Huang, et al. Acebench: Who wins the match point in tool usage? arXiv preprint arXiv:2501.12851, 2025.

Jun Chen, Deyao Zhu, Xiaoqian Shen, Xiang Li, Zechun Liu, Pengchuan Zhang, Raghuraman Krishnamoorthi, Vikas Chandra, Yunyang Xiong, and Mohamed Elhoseiny. Minigpt-v2: large language model as a unified interface for vision-language multi-task learning. arXiv preprint arXiv:2310.09478, 2023.

Gheorghe Comanici, Eric Bieber, Mike Schaekermann, Ice Pasupat, Noveen Sachdeva, Inderjit Dhillon, Marcel Blistein, Ori Ram, Dan Zhang, Evan Rosen, et al. Gemini 2.5: Pushing the frontier with advanced reasoning, multimodality, long context, and next generation agentic capabilities. arXiv preprint arXiv:2507.06261, 2025.

N. DiGirolamo, C. L. Parkinson, D. J. Cavalieri, P. Gloersen, and H. J. Zwally. Sea ice concentrations from nimbus-7 smmr and dmsp ssm/i-ssmis passive microwave data, 2022. URL https:// doi.org/10.5067/MPYG15WAA4WX. NSIDC-0051. [Data Set]. Accessed: 2025-09-23.

Keyan Ding, Jing Yu, Junjie Huang, Yuchen Yang, Qiang Zhang, and Huajun Chen. Scitoolagent: a knowledge-graph-driven scientific agent for multitool integration. Nature Computational Science, pp. 1–11, 2025.

Sijun Dong, Libo Wang, Bo Du, and Xiaoliang Meng. Changeclip: Remote sensing change detection with multimodal vision-language representation learning. ISPRS Journal of Photogrammetry and Remote Sensing, 208:53–69, 2024.

Chen Gao, Xiaochong Lan, Nian Li, Yuan Yuan, Jingtao Ding, Zhilun Zhou, Fengli Xu, and Yong Li. Large language models empowered agent-based modeling and simulation: A survey and perspectives. Humanities and Social Sciences Communications, 11(1):1–24, 2024.

Haonan Guo, Xin Su, Chen Wu, Bo Du, Liangpei Zhang, and Deren Li. Remote sensing chatgpt: Solving remote sensing tasks with chatgpt and visual models. In IGARSS 2024-2024 IEEE International Geoscience and Remote Sensing Symposium, pp. 11474–11478. IEEE, 2024a.

Zhicheng Guo, Sijie Cheng, Hao Wang, Shihao Liang, Yujia Qin, Peng Li, Zhiyuan Liu, Maosong Sun, and Yang Liu. Stabletoolbench: Towards stable large-scale benchmarking on tool learning of large language models. arXiv preprint arXiv:2403.07714, 2024b.

Jia He and Zhizhao Liu. Water vapor retrieval from modis nir channels using ground-based gps data. IEEE Transactions on Geoscience and Remote Sensing, 58(5):3726–3737, 2020. doi: 10.1109/ TGRS.2019.2962057.

Xinyi Hou, Yanjie Zhao, Shenao Wang, and Haoyu Wang. Model context protocol (mcp): Landscape, security threats, and future research directions. arXiv preprint arXiv:2503.23278, 2025.

Huiyang Hu, Peijin Wang, Yingchao Feng, Kaiwen Wei, Wenxin Yin, Wenhui Diao, Mengyu Wang, Hanbo Bi, Kaiyue Kang, Tong Ling, et al. Ringmo-agent: A unified remote sensing foundation model for multi-platform and multi-modal reasoning. arXiv preprint arXiv:2507.20776, 2025a.

Yuan Hu, Jianlong Yuan, Congcong Wen, Xiaonan Lu, Yu Liu, and Xiang Li. Rsgpt: A remote sensing vision language model and benchmark. ISPRS Journal of Photogrammetry and Remote Sensing, 224:272–286, 2025b.

Yangyu Huang, Tianyi Gao, Haoran Xu, Qihao Zhao, Yang Song, Zhipeng Gui, Tengchao Lv, Hao Chen, Lei Cui, Scarlett Li, et al. Peace: Empowering geologic map holistic understanding with mllms. In Proceedings of the Computer Vision and Pattern Recognition Conference, pp. 3899– 3908, 2025.

Zhiyu Huang, Chen Tang, Chen Lv, Masayoshi Tomizuka, and Wei Zhan. Learning online belief prediction for efficient pomdp planning in autonomous driving. arXiv preprint arXiv:2401.15315, 2024.

Carlos E Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, and Karthik R Narasimhan. SWE-bench: Can language models resolve real-world github issues? In The Twelfth International Conference on Learning Representations, 2024. URL https://openreview. net/forum?id=VTF8yNQM66.

Karen E Joyce, Kim C Wright, Sergey V Samsonov, and Vincent G Ambrosia. Remote sensing and the disaster management cycle. Advances in geoscience and remote sensing, 48(7):317–346, 2009.

Chia Hsiang Kao, Wenting Zhao, Shreelekha Revankar, Samuel Speas, Snehal Bhagat, Rajeev Datta, Cheng Perng Phoo, Utkarsh Mall, Carl Vondrick, Kavita Bala, et al. Towards llm agents for earth observation. arXiv preprint arXiv:2504.12110, 2025.

Ioannis P. Kokkoris, Bruno Smets, Lars Hein, Giorgos Mallinis, Marcel Buchhorn, Stefano Balbi, J´an Cerneck´ˇ y, Marc Paganini, and Panayotis Dimopoulos. The role of earth observation in ecosystem accounting: A review of advances, challenges and future directions. Ecosystem Services, 70:101659, 2024. ISSN 2212-0416. doi: https://doi.org/10.1016/j.ecoser. 2024.101659. URL https://www.sciencedirect.com/science/article/pii/ S2212041624000664.

Kartik Kuckreja, Muhammad Sohail Danish, Muzammal Naseer, Abhijit Das, Salman Khan, and Fahad Shahbaz Khan. Geochat: Grounded large vision-language model for remote sensing. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp. 27831–27840, 2024.

Alexandre Lacoste, Nils Lehmann, Pau Rodriguez, Evan Sherwin, Hannah Kerner, Bj¨orn L¨utjens, Jeremy Irvin, David Dao, Hamed Alemohammad, Alexandre Drouin, et al. Geo-bench: Toward foundation models for earth monitoring. Advances in Neural Information Processing Systems, 36:51080–51093, 2023.

Jinpeng Li, Jun He, Weijia Li, Jiabin Chen, and Jinhua Yu. Roadcorrector: A structure-aware road extraction method for road connectivity and topology correction. IEEE Transactions on Geoscience and Remote Sensing, 62:1–18, 2024a.

Ming Li, Keyu Chen, Ziqian Bi, Ming Liu, Benji Peng, Qian Niu, Junyu Liu, Jinlang Wang, Sen Zhang, Xuanhe Pan, et al. Surveying the mllm landscape: A meta-review of current surveys. arXiv preprint arXiv:2409.18991, 2024b.

Weijia Li, Runmin Dong, Haohuan Fu, Jie Wang, Le Yu, and Peng Gong. Integrating google earth imagery with landsat data to improve 30-m resolution land cover mapping. Remote Sensing of Environment, 237:111563, 2020.

Weijia Li, Yawen Lai, Linning Xu, Yuanbo Xiangli, Jinhua Yu, Conghui He, Gui-Song Xia, and Dahua Lin. Omnicity: Omnipotent city understanding with multi-level and multi-view images. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp. 17397–17407, 2023a.

Weijia Li, Wenqian Zhao, Jinhua Yu, Juepeng Zheng, Conghui He, Haohuan Fu, and Dahua Lin. Joint semantic–geometric learning for polygonal building segmentation from high-resolution remote sensing images. ISPRS Journal of Photogrammetry and Remote Sensing, 201:26–37, 2023b.

Weijia Li, Haote Yang, Zhenghao Hu, Juepeng Zheng, Gui-Song Xia, and Conghui He. 3d building reconstruction from monocular remote sensing images with multi-level supervisions. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp. 27728– 27737, 2024c.

Xiang Li, Jian Ding, and Mohamed Elhoseiny. Vrsbench: A versatile vision-language benchmark dataset for remote sensing image understanding. Advances in Neural Information Processing Systems, 37:3229–3242, 2024d.

Yuxuan Li, Xiang Li, Yunheng Li, Yicheng Zhang, Yimian Dai, Qibin Hou, Ming-Ming Cheng, and Jian Yang. Sm3det: A unified model for multi-modal remote sensing object detection. arXiv preprint arXiv:2412.20665, 2024e.

Zhao-Liang Li, Bo-Hui Tang, Hua Wu, Huazhong Ren, Guangjian Yan, Zhengming Wan, Isabel F. Trigo, and Jos´e A. Sobrino. Satellite-derived land surface temperature: Current status and perspectives. Remote Sensing of Environment, 131:14–37, 2013. ISSN 0034-4257. doi: https://doi. org/10.1016/j.rse.2012.12.008. URL https://www.sciencedirect.com/science/ article/pii/S0034425712004749.

Ziyi Lin, Chris Liu, Renrui Zhang, Peng Gao, Longtian Qiu, Han Xiao, Han Qiu, Chen Lin, Wenqi Shao, Keqin Chen, et al. Sphinx: The joint mixing of weights, tasks, and visual embeddings for multi-modal large language models. arXiv preprint arXiv:2311.07575, 2023.

Aixin Liu, Bei Feng, Bing Xue, Bingxuan Wang, Bochao Wu, Chengda Lu, Chenggang Zhao, Chengqi Deng, Chenyu Zhang, Chong Ruan, et al. Deepseek-v3 technical report. arXiv preprint arXiv:2412.19437, 2024a.

Chenyang Liu, Keyan Chen, Haotian Zhang, Zipeng Qi, Zhengxia Zou, and Zhenwei Shi. Changeagent: Toward interactive comprehensive remote sensing change interpretation and analysis. IEEE Transactions on Geoscience and Remote Sensing, 62:1–16, 2024b. doi: 10.1109/TGRS.2024. 3425815.

Fan Liu, Delong Chen, Zhangqingyun Guan, Xiaocong Zhou, Jiale Zhu, Qiaolin Ye, Liyong Fu, and Jun Zhou. Remoteclip: A vision language foundation model for remote sensing. IEEE Transactions on Geoscience and Remote Sensing, 2024c.

Haotian Liu, Chunyuan Li, Yuheng Li, and Yong Jae Lee. Improved baselines with visual instruction tuning. In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, pp. 26296–26306, 2024d.

Zhuoran Liu, Danpei Zhao, Bo Yuan, and Zhiguo Jiang. Rescueadi: adaptive disaster interpretation in remote sensing images with autonomous agents. IEEE Transactions on Geoscience and Remote Sensing, 2025.

Sylvain Lobry, Diego Marcos, Jesse Murray, and Devis Tuia. Rsvqa: Visual question answering for remote sensing data. IEEE Transactions on Geoscience and Remote Sensing, 58(12):8555–8566, 2020.

Siqi Lu, Junlin Guo, James R Zimmer-Dauphinee, Jordan M Nieusma, Xiao Wang, Steven A Wernke, Yuankai Huo, et al. Vision foundation models in remote sensing: A survey. IEEE Geoscience and Remote Sensing Magazine, 2025.

Jingjing Ma, Wei Jiang, Xu Tang, Xiangrong Zhang, Fang Liu, and Licheng Jiao. Multiscale sparse cross-attention network for remote sensing scene classification. IEEE Transactions on Geoscience and Remote Sensing, 2025.

Zixian Ma, Weikai Huang, Jieyu Zhang, Tanmay Gupta, and Ranjay Krishna. m & m’s: A benchmark to evaluate tool-use for m ulti-step m ulti-modal tasks. In European Conference on Computer Vision, pp. 18–34. Springer, 2024.

Utkarsh Mall, Cheng Perng Phoo, Meilin Kelsey Liu, Carl Vondrick, Bharath Hariharan, and Kavita Bala. Remote sensing vision-language foundation models without annotations via ground remote alignment. arXiv preprint arXiv:2312.06960, 2023.

Gr´egoire Mialon, Cl´ementine Fourrier, Thomas Wolf, Yann LeCun, and Thomas Scialom. Gaia: a benchmark for general ai assistants. In The Twelfth International Conference on Learning Representations, 2023.

David Montero, Cesar Aybar, Miguel D. Mahecha, Sebastian Wieneke, et al. A standardized catalogue of spectral indices to advance the use of remote sensing in earth system research. Scientific Data, 10(1):197, 2023. doi: 10.1038/s41597-023-02096-0. URL https://doi.org/10. 1038/s41597-023-02096-0.

Dilxat Muhtar, Zhenshi Li, Feng Gu, Xueliang Zhang, and Pengfeng Xiao. Lhrs-bot: Empowering remote sensing with vgi-enhanced large multimodal language model. In European Conference on Computer Vision, pp. 440–457. Springer, 2024.

OpenAI. Hello gpt-4o. https://openai.com/index/hello-gpt-4o/, 2024. OpenAI. Gpt-5 is here. https://openai.com/gpt-5/, 2025a. OpenAI. Introducingoperator. https://openai.com/index/

introducing-operator/, 2025b.

Chao Pang, Xingxing Weng, Jiang Wu, Jiayu Li, Yi Liu, Jiaxing Sun, Weijia Li, Shuai Wang, Litong Feng, Gui-Song Xia, et al. Vhm: Versatile and honest vision language model for remote sensing image analysis. In Proceedings of the AAAI Conference on Artificial Intelligence, volume 39, pp. 6381–6388, 2025.

Dmitrii Pantiukhin, Boris Shapkin, Ivan Kuznetsov, Antonia Anna Jost, and Nikolay Koldunov. Accelerating earth science discovery via multi-agent llm systems. arXiv preprint arXiv:2503.05854, 2025.

Chen Qian and Xin Cong. Communicative agents for software development. arXiv preprint arXiv:2307.07924, 6(3):1, 2023.

Nikhila Ravi, Valentin Gabeur, Yuan-Ting Hu, Ronghang Hu, Chaitanya Ryali, Tengyu Ma, Haitham Khedr, Roman R¨adle, Chloe Rolland, Laura Gustafson, et al. Sam 2: Segment anything in images and videos. arXiv preprint arXiv:2408.00714, 2024.

Partha Pratim Ray. A survey on model context protocol: Architecture, state-of-the-art, challenges and future directions. Authorea Preprints, 2025.

Xubin Ren, Lingrui Xu, Long Xia, Shuaiqiang Wang, Dawei Yin, and Chao Huang. Videorag: Retrieval-augmented generation with extreme long-context videos. arXiv preprint arXiv:2502.01549, 2025.

Farhad Samadzadegan, Ahmad Toosi, and Farzaneh Dadrass Javan. A critical review on multisensor and multi-platform remote sensing data fusion approaches: current status and prospects. International journal of remote sensing, 46(3):1327–1402, 2025.

Akashah Shabbir, Muhammad Akhtar Munir, Akshay Dudhane, Muhammad Umer Sheikh, Muhammad Haris Khan, Paolo Fraccaro, Juan Bernabe Moreno, Fahad Shahbaz Khan, and Salman Khan. Thinkgeo: Evaluating tool-augmented agents for remote sensing tasks. arXiv preprint arXiv:2505.23752, 2025.

Ahmed Shaker, Wai Yeung Yan, and Paul E LaRocque. Automatic land-water classification using multispectral airborne lidar data for near-shore and river environments. ISPRS journal of photogrammetry and remote sensing, 152:94–108, 2019.

Minjie Shen, Yanshu Li, Lulu Chen, and Qikai Yang. From mind to machine: The rise of manus ai as a fully autonomous digital agent. arXiv preprint arXiv:2505.02024, 2025.

Zhenwei Shi and Zhengxia Zou. Can a machine generate humanlike language descriptions for a remote sensing image? IEEE Transactions on Geoscience and Remote Sensing, 55(6):3623– 3634, 2017.

Chenglei Si, Diyi Yang, and Tatsunori Hashimoto. Can llms generate novel research ideas? a largescale human study with 100+ nlp researchers. arXiv preprint arXiv:2409.04109, 2024.

Hao Su, Shunjun Wei, Min Yan, Chen Wang, Jun Shi, and Xiaoling Zhang. Object detection and instance segmentation in remote sensing imagery based on precise mask r-cnn. In IGARSS 20192019 IEEE International Geoscience and Remote Sensing Symposium, pp. 1454–1457. IEEE, 2019.

Qiushi Sun, Zhoumianze Liu, Chang Ma, Zichen Ding, Fangzhi Xu, Zhangyue Yin, Haiteng Zhao, Zhenyu Wu, Kanzhi Cheng, Zhaoyang Liu, et al. Scienceboard: Evaluating multimodal autonomous agents in realistic scientific workflows. arXiv preprint arXiv:2505.19897, 2025.

Jiabin Tang, Lianghao Xia, Zhonghang Li, and Chao Huang. Ai-researcher: Autonomous scientific innovation. arXiv preprint arXiv:2505.18705, 2025.

Kimi Team, Yifan Bai, Yiping Bao, Guanduo Chen, Jiahao Chen, Ningxin Chen, Ruijue Chen, Yanru Chen, Yuankun Chen, Yutian Chen, et al. Kimi k2: Open agentic intelligence. arXiv preprint arXiv:2507.20534, 2025.

Qwen Team. Qwen2 technical report. arXiv preprint arXiv:2407.10671, 2, 2024. Minyang Tian, Luyu Gao, Shizhuo Zhang, Xinan Chen, Cunwei Fan, Xuefei Guo, Roland Haas,

Pan Ji, Kittithat Krongchon, Yao Li, et al. Scicode: A research coding benchmark curated by scientists. Advances in Neural Information Processing Systems, 37:30624–30650, 2024.

Julie Transon, Rapha¨el D’Andrimont, Alexandre Maugnard, and Pierre Defourny. Survey of hyperspectral earth observation applications from space in the sentinel-2 context. Remote Sensing, 10(2), 2018. ISSN 2072-4292. doi: 10.3390/rs10020157. URL https://www.mdpi.com/ 2072-4292/10/2/157.

Mojtaba Valipour, Kelly Zheng, James Lowman, Spencer Szabados, Mike Gartner, and Bobby Braswell. Agi for the earth, the path, possibilities and how to evaluate intelligence of models that work with earth observation data? arXiv preprint arXiv:2508.06057, 2025.

CJ Van Westen. Remote sensing for natural disaster management. International archives of photogrammetry and remote sensing, 33(B7/4; PART 7):1609–1617, 2000.

Jize Wang, Ma Zerun, Yining Li, Songyang Zhang, Cailian Chen, Kai Chen, and Xinyi Le. Gta: a benchmark for general tool agents. Advances in Neural Information Processing Systems, 37: 75749–75790, 2024a.

Junjue Wang, Zhuo Zheng, Zihang Chen, Ailong Ma, and Yanfei Zhong. Earthvqa: Towards queryable earth via relational reasoning-based remote sensing visual question answering. In Proceedings of the AAAI conference on artificial intelligence, volume 38, pp. 5481–5489, 2024b.

Lei Wang, Chen Ma, Xueyang Feng, Zeyu Zhang, Hao Yang, Jingsen Zhang, Zhiyuan Chen, Jiakai Tang, Xu Chen, Yankai Lin, et al. A survey on large language model based autonomous agents. Frontiers of Computer Science, 18(6):186345, 2024c.

Luting Wang, Yinghao Xiang, Hongliang Huang, Dongjun Li, Chen Gao, and Si Liu. Towards realistic earth-observation constellation scheduling: Benchmark and methodology. arXiv preprint arXiv:2510.26297, 2025a.

Qi Wang, Wei Huang, Xueting Zhang, and Xuelong Li. Word–sentence framework for remote sensing image captioning. IEEE Transactions on Geoscience and Remote Sensing, 59(12):10532– 10543, 2020.

Weiyun Wang, Zhangwei Gao, Lixin Gu, Hengjun Pu, Long Cui, Xingguang Wei, Zhaoyang Liu, Linglin Jing, Shenglong Ye, Jie Shao, et al. Internvl3. 5: Advancing open-source multimodal models in versatility, reasoning, and efficiency. arXiv preprint arXiv:2508.18265, 2025b.

Xiaohan Wang, Yuhui Zhang, Orr Zohar, and Serena Yeung-Levy. Videoagent: Long-form video understanding with large language model as agent. In European Conference on Computer Vision, pp. 58–76. Springer, 2024d.

Zhecheng Wang, Rajanie Prabha, Tianyuan Huang, Jiajun Wu, and Ram Rajagopal. Skyscript: A large and semantically diverse vision-language dataset for remote sensing. In Proceedings of the AAAI Conference on Artificial Intelligence, volume 38, pp. 5805–5813, 2024e.

Marek W´ojtowicz, Andrzej W´ojtowicz, Jan Piekarczyk, et al. Application of remote sensing methods in agriculture. Communications in biometry and crop science, 11(1):31–50, 2016.

Zhiheng Xi, Wenxiang Chen, Xin Guo, Wei He, Yiwen Ding, Boyang Hong, Ming Zhang, Junzhe Wang, Senjie Jin, Enyu Zhou, et al. The rise and potential of large language model based agents: A survey. Science China Information Sciences, 68(2):121101, 2025.

Gui-Song Xia, Jingwen Hu, Fan Hu, Baoguang Shi, Xiang Bai, Yanfei Zhong, Liangpei Zhang, and Xiaoqiang Lu. Aid: A benchmark data set for performance evaluation of aerial scene classification. IEEE Transactions on Geoscience and Remote Sensing, 55(7):3965–3981, 2017.

Gui-Song Xia, Xiang Bai, Jian Ding, Zhen Zhu, Serge Belongie, Jiebo Luo, Mihai Datcu, Marcello Pelillo, and Liangpei Zhang. Dota: A large-scale dataset for object detection in aerial images. In Proceedings of the IEEE conference on computer vision and pattern recognition, pp. 3974–3983, 2018.

Junlin Xie, Zhihong Chen, Ruifei Zhang, Xiang Wan, and Guanbin Li. Large multimodal agents: A survey. arXiv preprint arXiv:2402.15116, 2024.

Zhitong Xiong, Fahong Zhang, Yi Wang, Yilei Shi, and Xiao Xiang Zhu. Earthnets: Empowering ai in earth observation. arXiv preprint arXiv:2210.04936, 2022.

Weikai Xu, Chengrui Huang, Shen Gao, and Shuo Shang. Llm-based agents for tool learning: A survey: W. xu et al. Data Science and Engineering, pp. 1–31, 2025.

Wenjia Xu, Zijian Yu, Boyang Mu, Zhiwei Wei, Yuanben Zhang, Guangzuo Li, and Mugen Peng. Rs-agent: Automating remote sensing tasks through intelligent agent. arXiv preprint arXiv:2406.07089, 2024a.

Yiheng Xu, Dunjie Lu, Zhennan Shen, Junli Wang, Zekun Wang, Yuchen Mao, Caiming Xiong, and Tao Yu. Agenttrek: Agent trajectory synthesis via guiding replay with web tutorials. arXiv preprint arXiv:2412.09605, 2024b.

An Yang, Anfeng Li, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu, Chang Gao, Chengen Huang, Chenxu Lv, et al. Qwen3 technical report. arXiv preprint arXiv:2505.09388, 2025.

Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, and Yuan Cao. React: Synergizing reasoning and acting in language models. In International Conference on Learning Representations (ICLR), 2023.

Yang Zhan, Zhitong Xiong, and Yuan Yuan. Rsvg: Exploring data and models for visual grounding on remote sensing data. IEEE Transactions on Geoscience and Remote Sensing, 61:1–13, 2023.

Yang Zhan, Zhitong Xiong, and Yuan Yuan. Skyeyegpt: Unifying remote sensing vision-language tasks via instruction tuning with large language model. ISPRS Journal of Photogrammetry and Remote Sensing, 221:64–77, 2025.

Kechi Zhang, Jia Li, Ge Li, Xianjie Shi, and Zhi Jin. Codeagent: Enhancing code generation with tool-integrated agent systems for real-world repo-level coding challenges. arXiv preprint arXiv:2401.07339, 2024a.

Wei Zhang, Miaoxin Cai, Tong Zhang, Yin Zhuang, and Xuerui Mao. Earthgpt: A universal multimodal large language model for multi-sensor image comprehension in remote sensing domain. IEEE Transactions on Geoscience and Remote Sensing, 2024b.

Baichuan Zhou, Haote Yang, Dairong Chen, Junyan Ye, Tianyi Bai, Jinhua Yu, Songyang Zhang, Dahua Lin, Conghui He, and Weijia Li. Urbench: A comprehensive benchmark for evaluating large multimodal models in multi-view urban scenarios. In Proceedings of the AAAI Conference on Artificial Intelligence, volume 39, pp. 10707–10715, 2025.

- A DATASET ILLUSTRATION


- A.1 DATASET COMPOSITION

The remote sensing imagery used in our dataset primarily comes from Landsat and MODIS, with additional high-resolution imagery sourced from open datasets. All the remote sensing data products are obtained through Google Earth Engine (GEE). The following Table 4 is a more detailed breakdown of the data sources, products, and their distribution:

Table 4: Sensor and Data Source Statistics

Category Sensor/Data Source Dataset Samples Spectrum Landsat Landsat 8 / 9 1684

MODIS - 10273

ASTER - 110

Products GEE LST 183 NDVI 369 GPM 160 VIIRS 164 GHSL 68

QA PIXEL 212

NDWI 69

fire MaxFRP 194 RGB Public Datasets AID 169

DIOR-RSVG 7

DOTA 22 NWPU-VHR-10 21 xBD 32

Total - - 13737

This table provides an overview of the data sources and the distribution of samples across three categories (Spectrum, Product, RGB). It includes a diverse set of remote sensing products, such as Landsat, MODIS, ASTER, and various other publicly available high-resolution datasets, ensuring comprehensive coverage for a wide range of Earth observation tasks.

- A.2 BENCHMARK STATISTICS


Table 5: Statistics of the benchmark dataset, including average verification code length, number of images, query length, reasoning steps, and question counts for different task types.

Avg. Query Length

Type Avg. Code Lines Avg. Images

Avg. Steps Question Count

AP IF

Spectrum 361.19 96.82 331.54 497.94 4.38 100 Products 283.64 43.23 505.72 648.09 6.35 88 RGB 176.42 4.18 333.80 464.70 5.77 60

Avg. 288.97 55.39 393.89 543.18 5.42 Total 71664 13737 97685 134708 1343 248

As illustrated in Table 5, Earth-Bench consists of 248 questions associated with approximately 13.7K images. We recruited a team of domain experts to annotate these questions. The annotation

process was as follows: experts first designed solution steps based on their expertise, then selected appropriate tools from the Agent Toolkit, implemented the steps by writing Python code to invoke the selected tools for data processing, and finally generated the corresponding answers. In total, the expert team annotated 1345 solution steps and produced 71,664 lines of verification code for the 248 benchmark questions.

- A.3 QUESTION TYPES AND CATEGORY

As shown in Figure 5, Earth-Bench questions are categorized into three types based on their data sources: Spectrum, Products, and RGB. The Table 6 below summarizes the number and proportion of questions within each category:

Table 6: Distribution of Question Types and Their Proportions

Question Types Number Proportion (%)

Temperature Monitoring 44 17.74 Weather Forecasting 11 4.44 Climate Analysis 20 8.06 Water Management 22 8.87 Pollution Regulation 14 5.65 Vegetation Monitoring 28 11.29 Disaster Judgement 24 9.68 Urban Management 25 10.08 Classification 15 6.05 Detection 15 6.05 Grounding 7 2.82 Segmentation 3 1.21 Counting 7 2.82 Change Detection 13 5.24

This table provides a detailed distribution of question types within Earth-Bench, reflecting the variety of Earth observation tasks addressed by the dataset.

- A.4 QUERY REGIMES

Earth-Bench categorizes each task into two regimes: Auto-Planning and Instruction-Following. The key distinction is that in Instruction-Following, the query explicitly provides the Agent with a solution approach, while preserving the original intent of the task. As shown in Table 5, the statistics of query length highlight this difference: on average, queries in the Instruction-Following regime are about 150 characters longer than those in Auto-Planning, due to the inclusion of solution guidance. For illustration, Appendix H presents examples of the same task under both regimes, along with the performance of different LLMs. In summary, Instruction-Following emphasizes LLMs’ instruction-following and tool-use capabilities, whereas Auto-Planning additionally evaluates their ability to decompose and plan Earth observation tasks.

- A.5 DATASET QUALITY CONTROL


Our annotation team was composed of 2 computer science experts, 7 remote sensing specialists (including one professor) and 3 Earth science specialists (including one professor).

Three core authors who served as senior reviewers led the pipeline of dataset construction. Each senior reviewer was responsible for guiding the development of the question sets and templates for

the Spectrum, Products, and RGB categories. They played a key role in providing strategic direction for the overall question pool.

The remaining 7 team members, consisting of graduate students and senior undergraduates, contributed in the following areas:

- • Creation of initial questions (approximately 400 questions)
- • Raw data collection
- • Development of Python-based solution scripts


Once the questions were created, they were thoroughly reviewed by the 3 senior reviewers. The review process focused on two key criteria:

- 1. Data Integrity: Ensuring that the raw data involved (e.g., Landsat or MODIS) has complete band information within the task’s time range and does not contain anomalies. Any questions and TIF files with missing or anomalous large values were discarded.
- 2. Task Difficulty Assessment: Senior reviewers assessed the difficulty of questions based on the number and complexity of the functions defined in the Python solutions. For simpler tasks (e.g., only calculating NDVI index to finish a task), these were removed to ensure an appropriate challenge across questions.


This collaborative structure ensured that the dataset was curated by a diverse team with expertise from the full landscape of Earth observation fields, enabling a well-rounded and comprehensive dataset for evaluation.

- A.6 BIAS ABLATION EXPERIMENT


To examine whether Earth-Bench exhibits bias toward specific models, i.e., whether certain models inherently find its tasks easier and thus risk skewing conclusions, we conducted an ablation study. Specifically, we removed all tools and allowed LLMs to directly answer questions given only the Query and Folder, then compared the results with those of tool-augmented Agents that had access to both Query and Data.

Model Performance: No tool vs Tool use

No Tool Tool Use

Band Product RGB Base64 Encoding

| |
|---|


Large Improvement

80

| |
|---|


Moderate improvement

| |
|---|


| |
|---|


Weak improvement

70

| |
|---|


60

Accuracy

50

40

30

20

Accuracy

10

0

GPT5-B Gemini-2.5-A Gemini-2.5-B GPT-4o-A

Kimik2-BQwen3-max-A

GPT-4oDeepSeek-V3.1-A-B DeepSeek-V3.1-B Kimik2-A

Qwen3-max-B

GPT5-A

Figure 6: Dataset Ablation Experiment

As shown in Fig. 6, without tool access, mainstream LLMs achieved comparable performance across the three task types, with an overall Accuracy of about 37%. This indicates that the dataset is fair in its raw form and that models cannot rely solely on parametric knowledge to solve all benchmark questions. In contrast, with tool access, different models exhibited varying degrees of improvement:

- GPT-5 achieved the largest gain, whereas GPT-4o showed a more modest increase. These results highlight differences in problem decomposition and tool-use capabilities among LLMs, and further corroborate the conclusions presented in the main experiments.


In the No Tool setting, LLMs/MLLMs were restricted from using any tools, and base64 encoding was not applied in RGB tasks specifically. To ensure integrity in the comparison, we added experiments with base64 encoding for RGB tasks. We observed that while models like GPT-5 showed some improvement in accuracy (compared with not applying base64 encoding), the performance remained at relatively low levels. DeepSeek and Kimik2 were unable to handle RGB tasks yet. The conclusions derived from the ablation study remain unchanged.

- B EVALUATION


- B.1 EVALUATION MODEL

Our evaluation covers 13 recent LLMs, including both closed-source and open-source ones, to understand their capabilities across multiple Earth observation tasks. The baseline models are listed in Table 7.

Table 7: Models evaluated in our benchmark and their corresponding API references.

Model Model Version API Links GPT5 GPT-5 https://platform.openai.com/docs/models/

gpt-5 GPT4 GPT-4o https://platform.openai.com/docs/models/

gpt-4o Gemini Gemini-2.5-Flash https://ai.google.dev/gemini-api/docs/

models#gemini-2.5-flash Mistral Mistral-Large https://docs.mistral.ai/getting-started/

models/

Qwen

Qwen3-Max-Previous https://www.alibabacloud.

com/help/en/model-studio/ use-qwen-by-calling-api

Qwen3-32B Qwen-Plus

Kimi Kimi-K2 https://platform.moonshot.ai/docs/guide/

start-using-kimi-api Deepseek Deepseek-V3.1 https://api-docs.deepseek.com Seed Seed-1.6 https://www.volcengine.com/docs/82379/

1099455 LLaMA LLaMA-4-Maverick https://www.llama.com/products/llama-api/

GLM GLM-4.5v https://docs.z.ai/guides/vlm/glm-4.5v InternVL InternVL-3.5 https://internlm.intern-ai.org.cn/api/

document

- B.2 EVALUATION METRIC


Formally, for each task goal g, our geoscience experts provide (i) a ground-truth final answer y⋆, and (ii) an expert-annotated reasoning trajectory.

τ⋆ = (o⋆0,a⋆0), (o⋆1,a⋆1), ..., (o⋆m,a⋆m) , where each action is defined as

a⋆k = (t⋆k, in⋆k, out⋆k),

with t⋆k ∈ V denoting the tool identifier (from the tool vocabulary), in⋆k ∈ X the input arguments, and out⋆k ∈ O the corresponding output. In other words, each tool is characterized by its name in the vocabulary, its input arguments, and its output results.

Given a policy π, the agent generates an output trajectory

τ = (o0,a0), (o1,a1), ..., (on,an) , together with a predicted final answer y.

To comprehensively evaluate the performance of the Agent on the Earth Benchmark, we assess its execution process from two perspectives: End-to-End and Step-by-Step. The corresponding evaluation metrics are defined as follows:

End-to-End protocol. End-to-end metrics evaluate the task-level performance of the agent, independent of its intermediate reasoning. We consider two complementary measures:

- (1) Accuracy. The correctness of the final answer is computed as Acc = Eg∼G I{y = y⋆} , (1)

where I{·} is the indicator function and G is the distribution of benchmark tasks.

- (2) Efficiency. To penalize unnecessarily long trajectories, we measure the relative optimality of tool usage:


Eff(τ,τ⋆) = |τ|

, (2)

|τ⋆|

where |τ| and |τ⋆| denote the number of tool calls in the predicted and ground-truth trajectories, respectively.

Step-by-Step protocol. In addition to outcome-based metrics, we also evaluate the fidelity of the reasoning trajectory relative to expert annotations. Let t⋆ = (t⋆1,...,t⋆m) and t = (t1,...,tn) denote the tool sequences, and in⋆ = (in⋆1,...,in⋆m), in = (in1,...,inn) the corresponding parameter sequences. We define four metrics:

- (1) Tools-Any-Order (TAO). Coverage of required tools, ignoring order and duplicates:

TAO(τ,τ⋆) =

Set(t⋆) ∩ Set(t) |Set(t⋆)|

, (3)

where Set(·) extracts the set of unique tools.

- (2) Tools-In-Order(TIO). Fraction of ground-truth tools matched as a subsequence in the predicted sequence:

k⋆ = max k : ∃1≤ j1 < ··· < jk ≤ n, tj

i

= t⋆i , ∀i ≤ k , TIO(τ,τ⋆) =

k⋆ m

. (4)

- (3) Tool-Exact-Match(TEM). Length of the longest common prefix (LCP), normalized by the ground-truth length:

ℓlcp = max ℓ ≤ min(m,n) : ti = t⋆i , ∀i ≤ ℓ , TEM(τ,τ⋆) =

ℓlcp m

. (5)

- (4) Parameter Accuracy. Exact match of both tool identifiers and arguments under the prefix rule:


ℓparam = max ℓ ≤ min(m,n) : ti = t⋆i ∧ ini ≡ in⋆i , ∀i ≤ ℓ , Sparam =

Here ini ≡ in⋆i denotes structural equality of arguments (e.g., dictionary match).

ℓparam m

. (6)

- C BREAKDOWN RESULTS ON DIFFERENT MODALITIES


Table 8, Table 9, and Table 10 present the detailed evaluation results on different subsets of EarthBench. In the main analysis, we report only the overall performance across the entire benchmark to ensure clarity and comparability. Nevertheless, the breakdown results of individual subsets provide valuable insights into potential directions for improving LLMs in Earth Observation tasks.

- Table 8: Performance of different LLM-based agents on the Spectrum subset of Earth-Bench. We bold the best results and underline the runner-ups.

Model

Accuracy Efficiency Tool-Any-Order Tool-In-Order Tool-Exact-Match Parameters AP IF AP IF AP IF AP IF AP IF AP IF

GPT-5 61.00 64.00↑ 3.5510 4.6657↓ 72.67 78.37↑ 65.80 74.71↑ 49.64 52.07↑ 21.74 24.97↑ Gemini-2.5 52.00 52.00 4.3584 4.5585↑ 71.35 71.90↑ 65.14 64.84↓ 40.12 49.89↑ 17.57 21.41↑ GPT-4o 37.00 42.00↑ 3.7736 4.5726↓ 69.55 72.83↑ 56.12 62.07↑ 48.27 51.02↑ 21.62 24.08↑

Kimik2 38.00 50.00↑ 2.5758 3.1005↓ 71.92 86.02↑ 62.27 78.91↑ 43.04 54.81↑ 20.73 25.67↑ DeepSeek-V3.1 47.00 45.00↓ 3.9014 4.0685↓ 76.48 75.97↓ 67.64 66.57↓ 50.22 50.52↑ 26.32 26.13↓ Qwen3-Max 45.00 40.00↓ 3.1981 3.2864↓ 77.67 74.27↓ 66.47 65.58↓ 33.97 48.54↑ 16.04 24.43↑ Seed-1.6 40.00 57.00↑ 1.7525 1.9186↓ 55.07 63.92↑ 42.00 54.94↑ 24.53 34.37↓ 12.56 16.83↑ LLaMA-4 36.00 37.00↑ 0.3648 0.4275↓ 16.89 25.20↑ 3.57 18.26↑ 2.69 13.58↑ 2.02 8.17↑ Qwen-Plus 33.00 36.00↑ 2.2833 2.4157↓ 55.95 57.38↑ 36.27 48.89↑ 5.67 35.14↑ 2.87 17.47↑ GLM-4.5v 33.33 28.28↓ 3.1121 3.0709↑ 47.53 49.87↑ 41.93 45.63↑ 14.26 25.22↑ 9.13 16.41↑ Mistral 24.00 18.00↓ 1.3825 0.8316↑ 23.73 19.58↓ 4.58 16.13↑ 1.87 13.37↑ 1.33 6.15↑ Qwen3-32B 12.00 29.00↑ 4.3328 3.4380↑ 45.02 65.25↑ 26.60 57.17↑ 5.53 38.86↑ 3.43 20.52↑ InternVL-3.5 19.00 25.00↑ 0.1127 0.2411↓ 7.50 18.77↑ 3.58 16.09↑ 0.58 13.02↑ 0.33 5.65↑

On the Spectrum subset, the accuracy of the Agent’s responses is generally below the average, and the overall efficiency is also lower than the benchmark mean. This indicates that the Agent encounters significant difficulties when addressing tasks in this subset. A likely reason is that the LLMs involved in the evaluation have limited familiarity with processing raw Earth Observation data. Furthermore, tasks in this subset often require analyzing a larger number of images, making them inherently more challenging compared to tasks in other subsets.

In contrast, on the Product subset, the Agent’s responses are substantially above the average in terms of accuracy, and its efficiency is comparable to that of expert annotations. This suggests that LLMs are more adept at handling structured, product-level information, where tasks often align with general reasoning and statistical capabilities rather than requiring specialized domain expertise.

- Table 9: Performance of different LLM-based agents on the Products subset of Earth-Bench. We bold the best results and underline the runner-ups.


Accuracy Efficiency Tool-Any-Order Tool-In-Order Tool-Exact-Match Parameters AP IF AP IF AP IF AP IF AP IF AP IF

Model

GPT-5 75.00 71.59↓ 1.7154 1.6190↑ 60.04 62.35↑ 38.43 40.44↑ 31.52 34.03↑ 17.62 16.75↓ Gemini-2.5 62.50 63.64↑ 3.0055 1.1600↑ 48.94 51.46↑ 33.82 35.26↑ 29.54 27.63↓ 16.33 17.11↑ GPT-4o 54.55 54.55 1.1800 1.5270↓ 57.27 60.11↑ 33.89 37.80↑ 31.31 35.02↑ 19.13 18.71↓

Kimik2 62.50 60.23↓ 1.2489 1.6481↓ 66.91 69.83↑ 42.99 49.96↑ 34.75 38.84↑ 20.23 21.32↑ DeepSeek-V3.1 50.00 59.09↑ 1.8111 1.6449↑ 73.48 72.75↓ 43.35 46.16↑ 32.18 33.32↑ 20.50 19.92↓ Qwen3-Max 56.82 61.36↑ 1.0688 1.0859↓ 63.24 66.80↑ 40.30 44.78↑ 33.22 30.24↓ 20.23 16.52↓ Seed-1.6 65.06 67.05↑ 0.8776 0.9359↓ 54.02 55.57↑ 36.75 37.20↑ 28.84 31.27↑ 16.79 19.82↑ LLaMA-4 60.23 47.73↓ 0.1641 0.1614↑ 8.92 9.83↑ 2.51 2.61↑ 1.39 1.65↑ 1.05 1.31↑ Qwen-Plus 53.41 40.91↓ 0.9972 1.0016↓ 47.71 51.57↑ 25.33 27.37↑ 10.16 4.14↓ 6.52 2.97↓ GLM-4.5v 43.18 47.67↑ 0.9342 1.1979↓ 35.06 41.97↑ 19.36 24.68↑ 8.77 9.04↑ 6.60 7.77↑ Mistral 36.36 22.73↓ 0.6263 1.0206↓ 26.61 30.36↑ 12.80 13.43↑ 8.83 10.40↑ 5.42 4.40↓ Qwen3-32B 27.27 18.39↓ 2.2108 0.6987↑ 29.66 6.97↓ 11.81 1.93↓ 2.70 1.14↓ 2.07 1.14↓ InternVL-3.5 36.36 28.41↓ 0.0495 0.0424↑ 4.91 5.27↑ 1.94 2.32↑ 0.52 2.26↑ 0.52 0.55↑

For the RGB subset, the Agent demonstrates above-average performance in tool utilization and achieves efficiency close to that of expert annotations. However, its response accuracy remains substantially below the average. This limitation is closely tied to the capabilities of the tools within the Perception Toolkit. In certain cases, even when the Agent selects the same tools as those used in expert annotations, the outputs still diverge from the ground-truth answers due to the constraints of the underlying expert models. As the first attempt to develop an Agent framework for Earth Observation, our work highlights this challenge and encourages future EO Agent research to adopt more advanced expert models in order to overcome these limitations.

- Table 10: Performance of different LLM-based agents on the RGB subset of Earth-Bench. We bold the best results and underline the runner-ups.


Accuracy Efficiency Tool-Any-Order Tool-In-Order Tool-Exact-Match Parameters AP IF AP IF AP IF AP IF AP IF AP IF

Model

GPT-5 59.32 49.15↓ 1.5312 1.5784↓ 76.61 72.09↓ 75.04 67.08↓ 59.60 52.71↓ 46.15 40.73↓ Gemini-2.5 47.46 47.46 0.7926 0.8878↓ 48.70 60.11↑ 29.38 50.11↑ 21.33 45.54↑ 19.07 36.75↑ GPT-4o 45.76 35.59↓ 0.8779 0.8939↓ 71.86 66.89↓ 66.60 61.13↓ 64.76 60.00↓ 46.65 47.54↑

Kimik2 54.24 62.71↑ 1.5341 1.4104↑ 75.65 80.62↑ 71.37 79.90↑ 51.48 63.32↑ 43.12 52.19↑ DeepSeek-V3.1 55.93 54.24↓ 1.6895 1.7966↓ 88.98 89.21↑ 85.49 87.64↑ 71.54 74.05↑ 53.57 57.22↑ Qwen3-Max 49.15 38.98↓ 0.8601 0.9785↓ 65.25 68.14↑ 50.28 56.58↑ 47.88 51.55↑ 34.04 43.93↑ Seed-1.6 55.93 52.54↓ 1.1948 0.9589↑ 57.99 57.59↓ 44.00 47.30↑ 34.11 43.74↑ 29.93 39.02↑ LLaMA-4 37.29 27.12↓ 0.3464 0.3790↓ 27.20 36.52↑ 0.47 15.61↑ 0.47 12.43↑ 0.47 11.25↑ Qwen-Plus 42.37 38.98↓ 0.9721 1.0488↓ 51.89 60.11↑ 29.51 42.80↑ 24.18 41.07↑ 23.62 36.89↑ GLM-4.5v 16.95 28.81↑ 1.3070 1.4535↓ 47.91 48.42↑ 27.36 33.54↑ 21.93 27.38↑ 19.73 24.98↑ Mistral 30.51 30.51 0.7215 0.7531↓ 36.16 45.59↑ 22.46 40.11↑ 21.89 37.71↑ 19.97 31.84↑ Qwen3-32B 25.42 27.12↑ 0.7767 1.0891↓ 45.93 56.47↑ 27.54 41.69↑ 26.41 41.69↑ 25.28 37.74↑ InternVL-3.5 25.42 27.12↑ 0.2398 0.2606↓ 16.95 29.92↑ 7.23 13.58↑ 6.67 13.58↑ 4.75 11.88↑

Overall, the comparative analysis across subsets highlights both the strengths and limitations of LLM-based Agents in Earth Observation. While LLMs achieve relatively strong performance on Product tasks, where success relies more on general reasoning and statistical skills, they remain less effective on tasks that demand specialized knowledge, such as those in the Spectrum subset, which involve interpreting raw spectral data. Moreover, Earth-Agent incorporates expert models within the Perception Toolkit for tasks such as segmentation and object detection, which significantly improves performance in the corresponding scenarios. However, the generalization ability of these expert models remains limited, as their outputs do not always align with ground-truth answers, even when the correct tools are selected. These findings suggest that future progress in EO Agents will depend not only on enhancing LLMs with domain-specific knowledge, but also on developing more robust and versatile expert models to ensure reliable performance across the diverse spectrum of Earth Observation tasks.

- D ERROR ANALYSIS


To analyze the errors made by Agents with different LLM backbones on Earth-Bench tasks, we selected GPT-5 as a representative closed-source model, and Kimi-K2, Qwen3-Max, and DeepseekV3.1 as representative open-source models. We counted the number of errors and categorized them into five types:

- • Unaware of Termination Conditions: failure to recognize the task’s termination condition, leading to repeated tool calls until reaching the maximum step limit;
- • Tool Hallucination: attempts to invoke non-existent tools;
- • File Hallucination: attempts to process non-existent files, i.e., providing invalid file or folder paths as tool inputs;
- • Invalid Parameters: inputs that do not conform to the expected parameter format or are otherwise invalid;
- • System Error: system-level failures caused by the runtime environment or external dependencies.


Figure 7 presents the frequency and distribution of these error types. Results show that GPT-5 produced the largest number of errors, while Kimi-K2 had the fewest. Except for GPT-5, the other models exhibited similar error counts across different regimes, and their error distributions did not vary significantly, suggesting that providing more detailed execution steps does not substantially improve tool-use proficiency.

In terms of error types, GPT-5 errors were dominated by Invalid Parameters, with occasional System Errors and File Hallucinations, but no Tool Hallucinations. In contrast, the three open-source

models demonstrated different error patterns: while Invalid Parameters remained a notable factor, it was not the primary source of errors. Instead, nearly 60% of their errors stemmed from Hallucinations and Unaware of Termination Conditions. We hypothesize that this difference is related to training strategies. Open-source models are often trained with reinforcement learning, which may encourage more exploratory outputs, thereby increasing the likelihood of hallucinations. Moreover, their reward functions are typically designed to shape behavioral style and output preferences rather than enhance factual knowledge, which could make models more prone to generating divergent or repetitive outputs and to overlooking termination conditions.

24.2% 24.2%

29.2% 23.9%

7.7%

6.8%

2.3% 9.1%

3.0% 13.3%

76.0%

81.8%

0.9%

3.2%

14.7%

10.6%

35.4%

33.7%

29.5%

30.5%

24.2%

50.0%

18.2%

26.8%

26.5%

5.8%

7.8%

4.8%

8.9%

22.9% 22.3%

42.4%

36.1%

43.2%

Figure 7: Error analysis.

- E LATENCY EXPERIMENT


- E.1 BREAKDOWN RESULTS ON LATENCY


We further break down the latency into LLM Latency and Tool Latency. It is evident that the majority of the latency is spent on model calls (LLM Latency), rather than on external tool calls (Tool Latency). This suggests that reducing the frequency of model calls could further improve latency. The results are shown in Table 11.

We observe that the majority of the latency is attributed to LLM Latency, while the impact of Tool Latency is relatively minimal. Therefore, reducing the frequency of model calls could significantly improve overall latency. This suggests that optimizing the model call frequency would further enhance system performance.

Table 11: Latency Breakdown for Different Models on Earth-Bench-Lite

###### Model Latency Tool Call Number LLM Latency Tool Latency

Earth-Agent (GPT) 9494.92s 669 6969.26s 2525.66s Earth-Agent (DeepSeek-V3.1) 4716.99s 540 3066.76s 1650.23s Earth-Agent (Kimik2) 7903.07s 502 6306.59s 1596.47s

- E.2 OUR PROPOSED STRATEGY


We addressed this issue in the design of the Earth-Agent architecture. Specifically, we optimized the tool design to minimize unnecessary interactions with the model. For instance, by leveraging batch calculations for Earth indices, such as the NDVI calculation, we significantly reduce the frequency of model interactions, thereby lowering the overall latency. Below is an example of our approach:

Batch Computing Strategy

- 1 def calculate_ndvi(input_nir_path, input_red_path, output_path):
- 2 with rasterio.open(input_nir_path) as nir_src:
- 3 nir_band = nir_src.read(1) # Read the first band (assuming single-band rasters )
- 4 nir_profile = nir_src.profile # Get the metadata profile
- 5 with rasterio.open(input_red_path) as red_src:
- 6 red_band = red_src.read(1) # Read the first band (assuming single-band rasters )
- 7 nir_band = np.array(nir_band, dtype=np.float32)
- 8 red_band = np.array(red_band, dtype=np.float32)
- 9 nir_band = np.clip(nir_band, 0, 10000)
- 10 red_band = np.clip(red_band, 0, 10000)
- 11 valid_mask = (nir_band >= 0) & (nir_band <= 10000) & (red_band >= 0) & (red_band <= 10000)
- 12 denominator = nir_band + red_band + 1e-6
- 13 ndvi = (nir_band - red_band) / denominator
- 14 # Set invalid pixels to -9999
- 15 ndvi[˜valid_mask] = -9999
- 16 ndvi_profile = nir_profile.copy()
- 17 ndvi_profile.update(
- 18 dtype=rasterio.float32, # NDVI values are floating-point numbers
- 19 nodata=-9999, # Set a NoData value
- 20 compress=’lzw’ # Optional: compress the output file
- 21 )
- 22 # Save the NDVI result to the specified output path
- 23 os.makedirs((TEMP_DIR / output_path).parent, exist_ok=True)
- 24 with rasterio.open(TEMP_DIR / output_path, ’w’, **ndvi_profile) as dst:
- 25 dst.write(ndvi.astype(rasterio.float32), 1)
- 26
- 27 return f’Result save at {TEMP_DIR / output_path}’
- 28 @mcp.tool(description="""
- 29 Batch-calculate NDVI from multiple pairs of NIR/Red raster files and save results.
- 30
- 31 Parameters:
- 32 input_nir_paths (list[str]): Paths to Near-Infrared (NIR) band raster files.
- 33 input_red_paths (list[str]): Paths to Red band raster files.
- 34 output_paths (list[str]): Relative output paths (e.g., "question17/ndvi_2022-01-16. tif") for each pair.
- 35
- 36 Returns:
- 37 list[str]: A list of result messages (one per output), as returned by ‘ calculate_ndvi‘.
- 38 """)
- 39 def calculate_batch_ndvi(
- 40 input_nir_paths: list[str],
- 41 input_red_paths: list[str],
- 42 output_paths: list[str]
- 43 ) -> list[str]:
- 44 return [
- 45 calculate_ndvi(nir_path, red_path, out_path)
- 46 for nir_path, red_path, out_path in zip(input_nir_paths, input_red_paths, output_paths)
- 47 ]


- F SCALABILITY DISCUSSION


Understanding the performance trends as the number of tool calls increases is crucial for evaluating the system’s behavior, particularly in terms of latency and scalability under increasing task complexity.

- F.1 PERFORMANCE WITH RESPECT TO TOOL NUMBER


To address this, we conducted an ablation study examining the relationship between the number of tools used and the system’s performance across three SOTA models: GPT5, DeepSeek-V3.1, and Kimik2. The following Table 12 presents the results, highlighting the high performance range for each model:

Table 12: Performance of Earth-Agent Models with respect to Tool Numbers. The high performance range is highlighted.

GPT5 DeepSeek-V3.1 Kimik2 Questions Accuracy (%) Questions Accuracy (%) Questions Accuracy (%)

Tool Numbers

- 0 25 8.00 - - 25 4.00

- 1 3 66.67 2 0.00 1 0.00

- 2 8 75.00 - - 5 40.00

- 3 42 80.95 23 73.91 17 76.47

- 4 29 89.66 23 86.96 21 66.67

- 5 30 60.00 19 68.42 21 71.43

- 6 7 85.71 15 60.00 27 70.37

- 7 10 90.00 15 40.00 16 56.25

- 8 10 80.00 8 87.50 20 65.00

- 9 4 75.00 10 60.00 4 25.00

- 10 10 70.00 11 54.55 5 40.00

- 11 4 50.00 8 75.00 11 54.55

- 12 3 33.33 8 75.00 9 66.67

- 13 6 100.00 17 70.59 20 80.00

- 14 4 75.00 4 50.00 3 33.33

- 15 2 0.00 5 100.00 4 50.00

- 16 2 100.00 3 66.67 1 0.00

- 17 4 50.00 4 25.00 3 66.67

- 18 4 50.00 4 25.00 2 50.00

- 19 3 0.00 3 0.00 1 0.00

- 20 3 33.33 3 33.33 1 100.00


... ... ... ... ... ... ... 159 1 100.00 - - - -

From the results, we observe distinct performance trends for each model:

- • For Earth-Agent driven by GPT5, high accuracy is primarily concentrated within the tool number range of 1 to 14.
- • For Earth-Agent driven by DeepSeek-V3.1, the high-performance range is within the tool number range of 3 to 15.
- • For Earth-Agent driven by Kimik2, the high-performance range falls within the tool number range of 3 to 13.


These high performance ranges align with expectations and indicate that task complexity plays a key role in system performance. Using too few tools (with the extreme case being zero tools) results in low accuracy, as the agent is unable to solve the task effectively, often leading to early errors. Conversely, performance tends to degrade when too many tools are employed, suggesting that the current capabilities of the base LLMs may not be sufficient to handle long chains of reasoning efficiently.

- F.2 PERFORMANCE WITH RESPECT TO UNIQUE TOOL NUMBER


We also investigated the relationship between the unique number of tools used and performance trends. Below is a visual representation using a bubble chart, where the size of each bubble is proportional to the number of questions.

![image 326](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile326.png)

![image 327](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile327.png)

High Performance Range

###### Figure 8: GPT5: Performance with respect to Unique Tool Number

![image 328](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile328.png)

![image 329](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile329.png)

High Performance Range

###### Figure 9: DeepSeek-V3.1: Performance with respect to Unique Tool Number

![image 330](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile330.png)

![image 331](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile331.png)

High Performance Range

###### Figure 10: Kimik2: Performance with respect to Unique Tool Number

Based on Figures 8, 9, and 10, we observed the following trends in the Earth-Agent system: When driven by GPT5, high accuracy is primarily observed within the range of 2 to 5 unique tool calls. For DeepSeek, the optimal accuracy is concentrated in the range of 2 to 6 unique tool calls, while for Kimik2, high accuracy is predominantly found in the range of 1 to 6 unique tool calls. We also observed a performance decline when the number of tool calls becomes excessive. These findings align with our expectations, highlighting the current limitations of LLMs in handling tasks that involve long chains of reasoning or excessive tool interactions.

This analysis provides valuable insights into the scalability of the system as task complexity increases. It also offers important directions for future agent training, including (1) optimizing the agent’s startup phase and (2) developing datasets for long-chain reasoning to enhance the agent’s ability to handle multiple tool calls effectively.

- G TOOL KIT LIST


The Index Toolkit offers a comprehensive suite of automated functions for computing a wide range of remote sensing indices directly from raster data. It supports efficient batch processing and covers commonly used indices related to vegetation, water, soil, snow, and burn severity, such as NDVI, NDWI, and NDBI. A detailed list of the implemented indices is provided in Table 13.

Table 13: List of detailed information of Index Toolkit.

Tool Name Category Description Summary calculate batch ndvi Index Batch-calculate NDVI from multiple pairs of

NIR/Red raster files and save results. calculate batch ndwi Index Batch-calculate NDWI from multiple pairs of

NIR/SWIR raster files and save results. calculate batch ndbi Index Batch-calculate NDBI from multiple pairs of

SWIR/NIR raster files and save results.

calculate batch evi Index Batch-calculate EVI from multiple sets of

NIR/Red/Blue raster files and save results. calculate batch nbr Index Batch-calculate NBR from multiple pairs of

NIR/SWIR raster files and save results. calculate batch fvc Index Batch-calculate FVC from multiple pairs of

NIR/Red raster files and save results.

calculate batch wri Index Batch-calculate WRI from multiple sets of Green/Red/NIR/SWIR raster files and save results.

calculate batch ndti Index Batch-calculate NDTI from multiple pairs of

Red/Green raster files and save results.

calculate batch frp Index Batch-calculate Fire Radiative Power (FRP) masks from multiple raster files and save results.

calculate batch ndsi Index Calculate NDSI for multiple pairs of Green

and SWIR band images. calc extreme snow loss

Index Calculate the percentage of extreme snow and ice loss areas from a binary map.

percentage from binary map

compute tvdi Index Compute TVDI (Temperature Vegetation Dryness Index) using NDVI and LST from local raster files.

The Inversion Toolkit integrates a collection of algorithms for retrieving key geophysical and environmental parameters from optical, thermal infrared, and microwave remote sensing data. It supports multiple retrieval methods for parameters such as land surface temperature (LST), land surface emissivity, and precipitable water vapor (PWV), including single-channel, multi-channel, and splitwindow approaches. By enabling flexible, efficient, and reproducible parameter estimation across multi-source Earth Observation data, the toolkit provides a versatile foundation for quantitative remote sensing applications. A detailed list of the implemented algorithms is provided in Table 14.

Table 14: List of detailed information of Inversion Toolkit.

Tool Name Category Description Summary band ratio Inversion Compute Precipitable Water Vapor (PWV) im-

age from local MODIS surface reflectance band files using the band ratio method.

lst single channel Inversion Estimate Land Surface Temperature (LST) using the Single-Channel method, with NDVIbased emissivity estimation from RED and NIR bands.

lst multi channel Inversion Estimate Land Surface Temperature (LST) us-

ing the multi-channel algorithm.

split window Inversion Estimate Land Surface Temperature (LST) or Precipitable Water Vapor (PWV) using the split-window algorithm.

temperature emissivity separation Inversion Estimate Land Surface Temperature (LST) using an enhanced Temperature Emissivity Separation (TES) algorithm with empirical emissivity estimation.

modis day night lst Inversion Estimate land surface temperature (LST) from local MODIS Day and Night brightness temperatures using a single-channel correction method.

ttm lst Inversion Estimate land surface temperature (LST) and emissivity using improved Three-Temperature Method (TTM) from three local thermal band GeoTIFF files. Uses all three bands to form a system of equations and solves per-pixel with physical constraints.

calculate mean lst by ndvi Inversion Calculate the average Land Surface Temperature (LST) across multiple images where NDVI is either above or below a given threshold.

calculate max lst by ndvi Inversion Calculate the maximum Land Surface Temperature (LST) in areas where NDVI is above or below a given threshold.

ATI Inversion Estimate Apparent Thermal Inertia (ATI) using the Thermal Inertia Method. This method calculates ATI as (1 − albedo)/(day temp − night temp), which serves as a proxy for land surface temperature stability over diurnal cycles.

dual polarization differential Inversion Dual-Polarization Differential Method (DPDM) for microwave remote sensing parameter inversion. Supports soil moisture and vegetation index estimation with improved data handling and flexible parameters.

dual frequency diff Inversion Dual-frequency Differential Method (DDM) for parameter inversion using local raster data. Supports inversion of multiple parameters via empirical linear models: Soil Moisture (SM): param = alpha*(band1 - band2) + beta; Vegetation Index (VI): param = alpha*(band1 band2) + beta; Leaf Area Index (LAI): param = alpha*(band1 - band2) + beta

multi freq bt Inversion Multi-frequency Brightness Temperature Method for parameter inversion using local raster data.

chang single param inversion Inversion Chang algorithm for inversion of a single parameter using multi-frequency dual-polarized microwave brightness temperatures from local raster files.

nasa team sea ice concentration Inversion Estimate Sea Ice Concentration using NASA Team Algorithm from local passive microwave brightness temperature GeoTIFF files.

dual polarization ratio Inversion Estimate Vegetation Water Content (VWC) or Soil Moisture (SM) using Dual-Polarization Ratio Method (PRM) from local passive microwave brightness temperature GeoTIFF files. The polarization ratio is computed as: (V - H) / (V + H), where V and H are brightness temperatures of vertical and horizontal polarizations.

calculate water turbidity ntu Inversion Calculate water turbidity in NTU (Nephelometric Turbidity Units) from red band raster file and save the result to a specified output path.

The Perception Toolkit provides a comprehensive set of remote sensing perception tools, covering a wide range of tasks such as scene classification, object detection, and change detection. In addition, it supports threshold-based segmentation and offers a series of post-processing utilities for bounding box and contour refinement. Overall, the toolkit enables diverse perception tasks on RGB remote sensing imagery, including scene recognition, semantic segmentation, and spatiotemporal change detection. A detailed list of the implemented tools is provided in Table 15.

Table 15: List of detailed information of Perception Toolkit.

###### Tool Name Category Description Summary

MSCN Perception MSCN is a scene and land-use image classifier, effective for categories such as Airport, BareLand, BaseballField, Beach, Bridge, Center, Church, Commercial, DenseResidential, Desert, Farmland, Forest, Industrial, Meadow, MediumResidential, Mountain, Park, Parking, Playground, Pond, Port, RailwayStation, Resort, River, School, SparseResidential, Square, Stadium, StorageTanks, and Viaduct.

RemoteCLIP Perception RemoteCLIP is a scene and land-use image classifier, specialized for categories such as Airport, Beach, Bridge, Commercial, Desert, Farmland, FootballField, Forest, Industrial, Meadow, Mountain, Park, Parking, Pond, Port, RailwayStation, Residential, River, and Viaduct.

Strip R CNN Perception Strip R CNN is a remote sensing object detection model with a strong focus on maritime and ship-related targets. Compared to SM3Det, it is particularly specialized in detecting and localizing different types of ships and naval vessels. This model is highly effective at detecting the following categories: L3 ship, L3 warcraft, L3 merchant ship, L3 aircraft carrier, Arleigh Burke, Container, Ticonderoga, Perry, Tarawa, WhidbeyIsland, CommanderA, Austen, Nimitz, Sanantonio, Container, Car carrierB, Enterprise, Car carrierA, Medical

SM3Det Perception SM3Det is a remote sensing object detection model. Given an input image and a natural language prompt specifying the target object (e.g., “plane”, “ship”, “storage tank”), it detects all instances of that object and returns their bounding boxes. This model is particularly strong at detecting and localizing the following categories:plane, ship, storage tank, baseball diamond, tennis court, basketball court, ground track field, harbor, bridge, large vehicle, small vehicle, helicopter, roundabout, soccer ball field, swimming pool.

RemoteSAM Perception RemoteSAM is a remote sensing visual grounding model. Given an input image and a text prompt describing a region of interest (e.g., “the football field located on the westernmost side”), it outputs the corresponding bounding box coordinates.

InstructSAM Perception InstructSAM is an instruction-guided counting model for remote sensing images. Given an input image and a natural language prompt specifying the target object (e.g., “storage tank”, “football field”), it detects and counts the number of instances matching the description.

SAM2 Perception Use SAM2 to segment the input image and re-

turn the path of the segmented image.

ChangeOS Perception Use ChangeOS to detect the change between two images and return the change mask. Can also be used to segment building by providing same image path in pre image path and post image path.

threshold segmentation Perception Perform threshold-based segmentation on a single-band raster image. The function reads a raster image from the specified path, converts it to a binary mask by applying a fixed threshold, and writes the resulting binary image to a new file. Pixel values greater than the threshold are set to 255 (white), and values less than or equal to the threshold are set to 0 (black).

bbox expansion Perception Expands bounding boxes by a given radius and

returns the expanded bounding boxes. count above threshold Perception Count the number of pixels in an image whose

values are greater than the specified threshold. count connected components Perception Read a binary image and return the count of

connected components.

bboxes2centroids Perception Convert bounding boxes from [x min, y min, x max, y max] format to centroid coordinates (x, y).

centroid distance extremes Perception Compute pairwise distances between centroids and return both the closest and farthest pairs with their indices and distances.

calculate bbox area Perception Calculate the total area of a list of bounding

boxes in [x, y, w, h] format.

The Analysis Toolkit provides a suite of statistical and spatiotemporal analysis methods tailored for remote sensing and geoscience data. Its functionalities include classical time-series trend detection and decomposition techniques such as linear regression, the Mann–Kendall test, Sen’s slope estimation, and STL decomposition. It also supports change-point detection and seasonal analysis based on autocorrelation. In addition, the toolkit integrates spatial statistical approaches, including hotspot direction analysis, as well as methods for spike detection in numerical sequences. A detailed list of the implemented tools is provided in Table 16.

Table 16: List of detailed information of Analysis Toolkit.

Tool Name Category Description Summary compute linear trend Analysis Computes the linear trend (slope and intercept)

of a time series by fitting a line of the form: y = a · x + b using the least squares method.

mann kendall test Analysis Perform the non-parametric Mann-Kendall trend test on a univariate time series. The test evaluates whether there is a monotonic upward or downward trend without requiring the data to conform to any particular distribution.

sens slope Analysis Compute Sen’s Slope estimator for a univariate time series. Sen’s Slope is a robust nonparametric method for estimating the median rate of change over time, often used with the Mann-Kendall test to assess both trend and magnitude.

stl decompose Analysis Apply Seasonal-Trend decomposition using LOESS (STL) to a univariate time series. Decomposes the series into trend, seasonal, and residual components.

detect change points Analysis Detect structural change points in a univariate time series using the ruptures library with the PELT algorithm. A change point marks a location where the statistical properties of the signal shift (e.g., mean or variance).

autocorrelation function Analysis Compute the Autocorrelation Function (ACF) for a univariate time series. The ACF measures the correlation of the series with its own lags, which is useful for detecting seasonality, persistence, and lag dependence.

detect seasonality acf Analysis Detect the dominant seasonality (period) in a univariate time series using the Autocorrelation Function (ACF). The method searches for significant peaks in the ACF beyond lag=1 to identify repeating cycles.

getis ord gi star Analysis Compute the Getis-Ord Gi* statistic for local spatial autocorrelation on a raster image. This method identifies statistically significant spatial clusters of high (hot spots) or low (cold spots) values using a user-specified spatial weight kernel.

analyze hotspot direction Analysis Analyze the main directional concentration of hotspots in a binary hotspot map. The function counts the number of hotspot pixels (value=1) in each cardinal direction relative to the map center, and returns the dominant direction.

count spikes from values Analysis Count the number of upward spikes in a sequence of numerical values. A spike is defined as a positive difference between consecutive valid values greater than the given threshold.

The Statistics Toolkit offers a comprehensive set of functions for descriptive statistics, image-based statistical analysis, and geospatial data processing. Its capabilities cover the calculation of classical statistical measures such as mean, variance, and skewness, as well as the extraction of statistical information from imagery and intersection-based threshold analysis. In addition, the toolkit provides fundamental arithmetic operations, temperature unit conversions, and image differencing functions. It also supports essential preprocessing tasks, including radiometric correction and cloud masking. Overall, the toolkit enables flexible and efficient extraction and analysis of statistical features from geoscience and remote sensing data. A detailed list of the implemented tools is provided in Table 17.

Table 17: List of detailed information of Statistics Toolkit.

###### Tool Name Category Description Summary

coefficient of variation Statistics Compute the Coefficient of Variation (CV) for a dataset. The CV is defined as the ratio of the standard deviation to the mean and is commonly used as a normalized measure of dispersion.

skewness Statistics Compute the skewness of a dataset, which measures the asymmetry of the probability distribution.

kurtosis Statistics Compute the kurtosis of a dataset, which mea-

sures the ¨tailedness¨of the distribution. calc batch image mean Statistics Compute mean value of an batch of images. calc batch image std Statistics Compute the standard deviation (spread of

pixel values) for a batch of images. calc batch image median Statistics Compute the median pixel value for a batch of

images. calc batch image min Statistics Compute the minimum pixel value for a batch

of images. calc batch image max Statistics Compute the maximum pixel value for a batch

of images.

calc batch image skewness Statistics Compute the skewness of pixel value distributions for a batch of images. Skewness quantifies the asymmetry of the distribution:1. Positive skew → longer right tail; 2. Negative skew → longer left tail; 3. Zero skew → symmetric distribution.

calc batch image kurtosis Statistics Compute the kurtosis of pixel value distributions for a batch of images. Kurtosis measures the ¨tailedness¨of the distribution relative to a normal distribution.

calc batch image sum Statistics Compute the sum of pixel values for a batch of

images. calc batch image hotspot

Statistics Compute the hotspot percentage (fraction of pixels above a threshold) for a batch of images.

percentage

calc batch image hotspot tif Statistics Create binary hotspot maps for a batch of images, where pixels below a specified threshold are set to 1 (hotspot) and others set to 0. The output is saved as GeoTIFF files, preserving georeference metadata from the input images.

difference Statistics Compute the absolute difference between two

numbers. division Statistics Perform division between two numbers. percentage change Statistics Calculate the percentage change between two

numbers, useful for comparing relative growth or decline.

kelvin to celsius Statistics Convert temperature from Kelvin to Celsius. celsius to kelvin Statistics Convert temperature from Celsius to Kelvin. max value and index Statistics Find the maximum value in a list and return

both the maximum value and its index. min value and index Statistics Find the minimum value in a list and return

both the minimum value and its index. ceil number Statistics Return the ceiling (rounded up integer) of a

given number. multiply Statistics Multiply two numbers and return their prod-

uct. get list object via indexes Statistics Retrieve elements from a list using a list or tu-

ple of indices. mean Statistics Compute the arithmetic mean (average) of a

dataset.

calculate threshold ratio Statistics Calculate the average percentage of pixels above a given threshold for one or more images and a specified band.

calc batch fire pixels Statistics Compute the number of fire pixels (FRP ¿

threshold) for a batch of images. create fire increase map Statistics Create a binary map highlighting areas where

fire increase exceeds a specified threshold. identify fire prone areas Statistics Identify fire-prone areas from a hotspot map

based on a given percentile threshold.

get percentile value from image Statistics Calculate the N-th percentile value of pixel values in a raster image, and return it as a native Python type matching the image’s data type.

image division mean Statistics Calculate the mean of pixel-wise division between two images or between two bands of the same image.

calculate intersection percentage Statistics Calculate the percentage of pixels that simultaneously satisfy threshold conditions in two raster images.

calc batch image mean mean Statistics Compute the average of mean pixel values

across a batch of images. calc batch image mean max Statistics Compute the mean pixel values of a batch of

images and return the maximum mean.

calc batch image mean max min Statistics Compute the batch-wise statistics across multiple images, including: Mean of mean values, Maximum of maximum values, Minimum of minimum values.

calc batch image mean threshold Statistics Calculate the percentage or count of images whose mean pixel values (in a specified band) are above or below a given threshold.

calculate multi band threshold ratio

Statistics Calculate the percentage of pixels that simultaneously satisfy multiple band threshold conditions.

count pixels satisfying conditions Statistics Count the number of pixels that simultaneously satisfy multiple band threshold conditions.

count images exceeding threshold ratio

Statistics Count how many images have a percentage of pixels above or below a threshold that exceeds a specified ratio.

average ratio exceeding threshold Statistics Calculate the average percentage of pixels exceeding a value threshold, considering only images where the ratio is greater than a specified ratio threshold.

count images exceeding mean multiplier

Statistics Count how many images have a mean pixel value above or below a multiple of the overall mean pixel value across all images.

calculate band mean by condition Statistics Calculate the mean value of a target band over pixels where a condition band satisfies a threshold.

calc threshold value mean Statistics Calculate the mean value of corresponding raster pixels in path2 where the raster values in path1 exceed the given threshold.

calculate tif difference Statistics Calculate difference between two tif files (im-

age b - image a) and save result. subtract Statistics Subtract two images and save result. calculate area Statistics This function calculates the area of non-zero

pixels in the input image and returns the result. grayscale to colormap Statistics Apply a colormap to a grayscale image and

save as a color image.

get filelist Statistics Returns a list of files in the specified directory. radiometric correction sr Statistics Apply Landsat 8 surface reflectance (SR B*)

radiometric correction.

apply cloud mask Statistics Apply cloud / shadow mask to a single Landsat 8 surface reflectance band using QA PIXEL band.

G.1 TOOL PROMPT

To better illustrate the functionality of the toolkits, we provide a representative example. Specifically, we focus on the lst multi channel tool, which estimates LST using a multi-channel algorithm. This method leverages multiple thermal infrared bands from remote sensing imagery and applies empirical formulas to derive accurate LST values. The corresponding implementation is provided below:

Tool Example

- 1 @mcp.tool(description=’’’
- 2 Estimate Land Surface Temperature (LST) using the multi-channel algorithm.
- 3 Requires local input files:
- 4 - Two thermal infrared bands (e.g., Band 31 and Band 32) as GeoTIFF files.
- 5
- 6 Parameters:
- 7 band31_path (str): Path to local GeoTIFF file for thermal band 31 (˜11 \mu m}).
- 8 band32_path (str): Path to local GeoTIFF file for thermal band 32 (˜12 \mu m).
- 9 output_path (str): Relative path for the output raster file, e.g. "question17/ lst_2022-01-16.tif"
- 10
- 11 Returns:
- 12 str: Local file path of the exported LST image.
- 13 ’’’)
- 14 def lst_multi_channel(band31_path: str, band32_path: str, output_path: str) -> str:
- 15 """
- 16 Description:
- 17 Estimate Land Surface Temperature (LST) using the multi-channel algorithm.
- 18 This method combines two thermal infrared bands to reduce atmospheric effects.
- 19
- 20 Parameters:
- 21 band31_path (str): Path to GeoTIFF file for thermal band 31 (˜11 \mu m)
- 22 band32_path (str): Path to GeoTIFF file for thermal band 32 (˜12 \mu m)
- 23 output_path (str): Relative path for the output LST GeoTIFF
- 24
- 25 Returns:
- 26 str: Full path to the saved LST GeoTIFF
- 27 """
- 28 import os, rasterio
- 29 import numpy as np
- 30
- 31 with rasterio.open(band31_path) as src31:
- 32 band31 = src31.read(1).astype(np.float32)
- 33 profile = src31.profile
- 34
- 35 with rasterio.open(band32_path) as src32:
- 36 band32 = src32.read(1).astype(np.float32)
- 37
- 38 a = 1.022
- 39 b = 0.47
- 40 c = 0.43
- 41
- 42 lst = a * band31 + b * (band31 - band32) + c
- 43
- 44 profile.update(dtype=rasterio.float32, count=1, compress=’lzw’)
- 45
- 46 os.makedirs((TEMP_DIR / output_path).parent, exist_ok=True)
- 47
- 48 with rasterio.open(TEMP_DIR / output_path, ’w’, **profile) as dst:
- 49 dst.write(lst.astype(np.float32), 1)
- 50
- 51 return f’Result saved at {TEMP_DIR / output_path}’


###### H EARTH-AGENT WITH DIFFERENT LLM BACKBONES

![image 332](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile332.png)

![image 333](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile333.png)

Spectrum: [Climate Analysis]

Autonomous Planning

![image 334](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile334.png)

Question: Using Landsat 8 thermal and reflectance data in 2022 over New York City, estimate LST based on NDVI and thermal band 10 using the single-channel method, then calculate the average LST for summer and autumn, and determine the mean difference to assess seasonal temperature variation between these two periods.

- A. 8.65K
- B. 10.89K
- C. 12.42K
- D. 14.75K


![image 335](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile335.png)

BT10 × 21

|![image 336](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile336.png)|
|---|


|![image 337](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile337.png)|
|---|


|![image 338](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile338.png)|
|---|


|![image 339](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile339.png)|
|---|


… B4×21

B5 × 21

![image 340](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile340.png)

###### GPT-5

![image 341](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile341.png)

"name": get_filelist "input": { "dir_path": "benchmark/data/question51"}

Step1Step25Step2-22Final

![image 342](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile342.png)

"output": [\"New York_2022-01-10_BT10.tif\“,…, \"New York_2022-12-28_b5.tif\"]

"name": lst_single_channel "input": "bt_path": ["benchmark/data/question51/New York_2022-06-03_BT10.tif,…, "benchmark/data/question51/New York_2022-11-26_BT10.tif“], "nir_path": ["benchmark/data/question51/New York_2022-06-03_b5.tif",…, "benchmark/data/question51/New York_2022-11-26_b5.tif"], "output_path": ["question51/lst_2022-06-03.tif",…, "question51/lst_2022-11-26.tif"], "red_path": ["benchmark/data/question51/New York_2022-06-03_b4.tif",…, "benchmark/data/question51/New York_2022-11-26_b4.tif"]

![image 343](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile343.png)

![image 344](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile344.png)

"output": ["Result saved at out/question51/lst_2022-11-26.tif",…, "Result saved at out/question51/lst_2022-06-03.tif"]

v

"name": difference "input": {"a": 286.42960357666016,"b": 298.8459999778054}

![image 345](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile345.png)

![image 346](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile346.png)

"output": "12.41639640114522"

![image 347](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile347.png)

"final answer": "C"

![image 348](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile348.png)

![image 349](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile349.png)

![image 350](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile350.png)

![image 351](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile351.png)

![image 352](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile352.png)

TIO: 1.0 TEM: 0.4 Param.: 0.0 Acc: 100%

Step-by-Step: TAO: 1.0 End-to-End: Efficiency: 5.0000

![image 353](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile353.png)

![image 354](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile354.png)

![image 355](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile355.png)

###### GT

×𝟐 -> Tool 4

Tool 1 -> Tool 2 -> Tool 3 -> C

Tool 1: get_filelist Tool 4: difference

Tool 2: lst_single_channel Tool 3: calc_batch_image_mean_mean Tool 5: calculate_batch_ndvi Tool 6: calculate_mean_lst_by_ndvi

###### Agent

![image 356](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile356.png)

![image 357](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile357.png)

Tool 1 -> Tool 2 ×𝟐𝟏 -> Tool 3 ×𝟐 -> Tool 4 -> C

![image 358](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile358.png)

GPT-5

![image 359](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile359.png)

![image 360](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile360.png)

![image 361](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile361.png)

![image 362](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile362.png)

![image 363](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile363.png)

![image 364](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile364.png)

Tool 1 -> Tool 2 ×𝟐𝟏 -> Tool 3 ×𝟐 -> FAIL

Kimi-K2

![image 365](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile365.png)

![image 366](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile366.png)

![image 367](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile367.png)

![image 368](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile368.png)

![image 369](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile369.png)

Tool 1 -> Tool 2 ×𝟐𝟏 -> Tool 3 ×𝟐 -> FAIL

Deepseek V3.1

![image 370](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile370.png)

![image 371](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile371.png)

![image 372](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile372.png)

- Figure 11: Example of Climate Analysis with Spectrum Data under the Auto-Planning Regime.


![image 373](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile373.png)

![image 374](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile374.png)

Spectrum: [Climate Analysis]

Instruction Following

![image 375](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile375.png)

Question: Based on Landsat 8 thermal band 10 and reflectance bands (Red and NIR) data over New York City in 2022, first list the input TIFF files, then calculate NDVI and estimate land surface temperature (LST) using the single-channel NDVI-based method. Classify the images into four seasons (spring, summer, autumn, winter) based on acquisition dates, compute the average LST for summer and autumn, and finally calculate the mean LST difference between these two seasons to analyze seasonal temperature variation.

- A. 8.65K
- B. 10.89K
- C. 12.42K
- D. 14.75K


![image 376](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile376.png)

BT10 × 21

|![image 377](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile377.png)|
|---|


|![image 378](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile378.png)|
|---|


|![image 379](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile379.png)|
|---|


|![image 380](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile380.png)|
|---|


… B4×21

B5 × 21

![image 381](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile381.png)

###### GPT-5

![image 382](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile382.png)

"name": get_filelist "input": { "dir_path": "benchmark/data/question51"}

Step1Step24Final

![image 383](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile383.png)

"output": [\"New York_2022-01-10_BT10.tif\“,…, \"New York_2022-12-28_b5.tif\"]

"name": lst_single_channel "input": "bt_path": ["benchmark/data/question51/New York_2022-06-03_BT10.tif,…, "benchmark/data/question51/New York_2022-11-26_BT10.tif“], "nir_path": ["benchmark/data/question51/New York_2022-06-03_b5.tif",…, "benchmark/data/question51/New York_2022-11-26_b5.tif"], "output_path": ["question51/lst_2022-06-03.tif",…, "question51/lst_2022-11-26.tif"], "red_path": ["benchmark/data/question51/New York_2022-06-03_b4.tif",…, "benchmark/data/question51/New York_2022-11-26_b4.tif"]

![image 384](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile384.png)

Step2-22

![image 385](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile385.png)

"output": ["Result saved at out/question51/lst_2022-11-26.tif",…, "Result saved at out/question51/lst_2022-06-03.tif"]

…

v

"name": calc_batch_image_mean_mean "input": {"file_list": [out/question51/lst_2022-06-03.tif",…, "out/question51/lst_2022-11-26.tif"}

![image 386](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile386.png)

![image 387](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile387.png)

"output": ["298.8459999778054","286.42960357666016"]

![image 388](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile388.png)

"final answer": "C"

![image 389](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile389.png)

![image 390](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile390.png)

![image 391](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile391.png)

![image 392](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile392.png)

![image 393](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile393.png)

TIO: 0.8 TEM: 0.4 Param.: 0.0 Acc: 100%

Step-by-Step: TAO: 0.75 End-to-End: Efficiency: 4.8000

![image 394](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile394.png)

![image 395](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile395.png)

![image 396](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile396.png)

###### GT

×𝟐 -> Tool 4

Tool 1 -> Tool 2 -> Tool 3 -> C

Tool 1: get_filelist Tool 4: difference

Tool 2: lst_single_channel Tool 5: calculate_batch_ndvi

###### Agent

![image 397](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile397.png)

![image 398](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile398.png)

![image 399](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile399.png)

Tool 1 -> Tool 2 ×𝟐𝟏 -> Tool 3 ×𝟐 -> C

GPT-5

![image 400](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile400.png)

![image 401](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile401.png)

![image 402](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile402.png)

![image 403](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile403.png)

![image 404](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile404.png)

Tool 1 -> Tool 5 ×𝟐 -> Tool 2 -> Tool 6 ×𝟐 -> Tool 4 -> C

Kimi-K2

![image 405](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile405.png)

![image 406](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile406.png)

![image 407](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile407.png)

![image 408](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile408.png)

![image 409](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile409.png)

![image 410](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile410.png)

![image 411](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile411.png)

Tool 1 -> Tool 2 ×𝟐𝟏 -> Tool 3 ×𝟐 -> FAIL

Deepseek V3.1

![image 412](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile412.png)

![image 413](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile413.png)

![image 414](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile414.png)

- Figure 12: Example of Climate Analysis with Spectrum Data under the Instruction-Following


![image 415](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile415.png)

![image 416](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile416.png)

###### Spectrum: [Disaster Judgement]

Autonomous Planning

![image 417](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile417.png)

Question: Based on temperature and vegetation indices (NDVI and LST) in the Central Valley of California, U.S., from May to October 2021, calculate the number of times when more than 40% of the area exhibited a drought index value exceeding 0.7, indicating widespread extreme drought.

- A. The proportion of pixels with TVDI values exceeding 0.7 surpassed 40% occurred 10 times
- B. The proportion of pixels with TVDI values exceeding 0.7 surpassed 40% occurred 8 times
- C. The proportion of pixels with TVDI values exceeding 0.7 surpassed 40% occurred 4 times
- D. The proportion of pixels with TVDI values exceeding 0.7 surpassed 40% occurred 2 times


![image 418](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile418.png)

## …

|![image 419](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile419.png)|
|---|


|![image 420](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile420.png)|
|---|


|![image 421](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile421.png)|
|---|


NDVI × 11

|![image 422](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile422.png)|
|---|


LST × 11

![image 423](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile423.png)

GPT-5

![image 424](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile424.png)

"name": get_filelist "input": { "dir_path": "benchmark/data/question5"}

###### Step1

![image 425](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile425.png)

"output": ["Central Valley_2021-05-09_LST.tif","Central Valley_2021-05-09_NDVI.tif","Central Valley_2021-0525_LST.tif","Central Valley_2021-05-25_NDVI.tif",...,"Central Valley_2021-10-16_NDVI.tif"]

"name": compute_tvdi "input": {

![image 426](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile426.png)

“ndvi_path”: ["Central Valley_2021-05-09_NDVI.tif",…, "Central Valley_2021-10-16_NDVI.tif "], “lst_path”: ["Central Valley_2021-05-09_LST.tif",…,"Central Valley_2021-05-09_LST.tif”] "output_path": ["question5/tvdi_2021-05-09.tif”,…,"question5/tvdi_2021-05-09.tif"]

Step13Step2-12

}

![image 427](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile427.png)

“output": ["Result saved at out/question5/tvdi_2021-05-09.tif", …,"Result saved at out/question5/tvdi_2021-10-16.tif"]

"name": count_images_exceeding_threshold_ratio "input":{

v

![image 428](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile428.png)

“image_paths”: [“out/question5/tvdi_2021-05-09.tif ”,…, "out/question5/tvdi_2021-10-16.tif"] "mode": "above ", "ratio_threshold": 40, "value_threshold": 0.7,

}

![image 429](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile429.png)

"output": "4"

Final

![image 430](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile430.png)

"final answer": "C"

![image 431](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile431.png)

TIO: 1.0 TEM: 0.67 Param.: 0.33 Acc: 100%

Step-by-Step: TAO: 1.0 End-to-End: Efficiency: 4.33

![image 432](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile432.png)

###### GT

Tool 1 -> Tool 2 -> Tool 3

-> C

- Tool 1: get_filelist
- Tool 2: compute_tvdi


- Tool 3: count_images_exceeding_threshold_ratio
- Tool 4: calculate_threshold_ratio


###### Agent

![image 433](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile433.png)

![image 434](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile434.png)

![image 435](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile435.png)

Tool 1 -> Tool 2 ×11 -> Tool 3

- -> C
- -> C


GPT-5

![image 436](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile436.png)

![image 437](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile437.png)

![image 438](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile438.png)

![image 439](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile439.png)

![image 440](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile440.png)

Tool 1 -> Tool 2 -> Tool 3

×11

Kimi-K2

![image 441](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile441.png)

![image 442](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile442.png)

![image 443](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile443.png)

![image 444](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile444.png)

![image 445](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile445.png)

Tool 1 -> Tool 2 -> Tool 4 × 12

-> C

×11

Deepseek V3.1

![image 446](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile446.png)

![image 447](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile447.png)

![image 448](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile448.png)

###### Figure 13: Example of Disaster Judgement with Spectrum Data under the Auto-Planning

![image 449](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile449.png)

![image 450](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile450.png)

###### Spectrum: [Disaster Judgement]

Instruction Following

![image 451](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile451.png)

Question: Based on temperature and vegetation indices (NDVI and LST) in the Central Valley of California, U.S., from May to October 2021, first list the input TIFF files, then calculate the Temperature-Vegetation Dryness Index (TVDI) for each date, compute the proportion of pixels with TVDI values exceeding 0.7 for each image, and finally count the number of times this proportion surpassed 40%, indicating widespread extreme drought.

A. The proportion of pixels with TVDI values exceeding 0.7 surpassed 40% occurred 10 times B. The proportion of pixels with TVDI values exceeding 0.7 surpassed 40% occurred 8 times

- C. The proportion of pixels with TVDI values exceeding 0.7 surpassed 40% occurred 4 times
- D. The proportion of pixels with TVDI values exceeding 0.7 surpassed 40% occurred 2 times


![image 452](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile452.png)

## …

|![image 453](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile453.png)|
|---|


|![image 454](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile454.png)|
|---|


|![image 455](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile455.png)|
|---|


NDVI × 11

|![image 456](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile456.png)|
|---|


LST × 11

![image 457](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile457.png)

GPT-5

![image 458](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile458.png)

"name": get_filelist "input": { "dir_path": "benchmark/data/question5"}

- Step1

"output": ["Result saved at out/question5/tvdi_2021-05-09.tif", …,"Result saved at out/question5/tvdi_2021-10-16.tif"]

![image 459](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile459.png)

"name": count_images_exceeding_threshold_ratio "input":{

“image_paths”: [“out/question5/tvdi_2021-05-09.tif ”,…, "out/question5/tvdi_2021-10-16.tif"] "mode": "above ", "ratio_threshold": 40, "value_threshold": 0.7,

}

![image 460](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile460.png)

![image 461](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile461.png)

"output": "4"

- Step2-12Step13


![image 462](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile462.png)

"output": ["Central Valley_2021-05-09_LST.tif","Central Valley_2021-05-09_NDVI.tif","Central Valley_2021-1016_LST.tif\",...,"Central Valley_2021-10-16_NDVI.tif"]

"name": compute_tvdi "input": {

![image 463](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile463.png)

“ndvi_path”: ["Central Valley_2021-05-09_NDVI.tif",…, "Central Valley_2021-10-16_NDVI.tif "], “lst_path”: ["Central Valley_2021-05-09_LST.tif",…,"Central Valley_2021-10-16_LST.tif "] "output_path": ["question5/tvdi_2021-05-09.tif”,…,"question5/tvdi_2021-10-16.tif"]

}

v

Final

![image 464](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile464.png)

"final answer": "C"

![image 465](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile465.png)

TIO: 1.0 TEM: 0.67 Param.: 0.33 Acc: 100%

Step-by-Step: TAO: 1.0 End-to-End: Efficiency: 4.33

![image 466](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile466.png)

###### GT

Tool 1 -> Tool 2 -> Tool 3

-> C

- Tool 1: get_filelist
- Tool 2: compute_tvdi


- Tool 3: count_images_exceeding_threshold_ratio
- Tool 4: calculate_threshold_ratio


###### Agent

![image 467](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile467.png)

![image 468](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile468.png)

![image 469](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile469.png)

Tool 1 -> Tool 2 -> Tool 3

×11

-> C

GPT-5

![image 470](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile470.png)

![image 471](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile471.png)

![image 472](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile472.png)

![image 473](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile473.png)

![image 474](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile474.png)

Tool 1 -> Tool 2 ×11 -> Tool 4 -> Tool 3 -> C

Kimi-K2

![image 475](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile475.png)

![image 476](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile476.png)

![image 477](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile477.png)

![image 478](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile478.png)

![image 479](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile479.png)

![image 480](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile480.png)

Tool 1 -> Tool 2 -> Tool 4 × 12

-> C

×11

Deepseek V3.1

![image 481](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile481.png)

![image 482](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile482.png)

![image 483](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile483.png)

###### Figure 14: Example of Disaster Judgement with Spectrum Data under the Instruction-Following Regime.

![image 484](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile484.png)

###### Figure 15: Example of Temperature Monitoring with Spectrum Data under the Auto-Planning

![image 485](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile485.png)

###### Figure 16: Example of Temperature Monitoring with Spectrum Data under the Instruction-

![image 486](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile486.png)

![image 487](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile487.png)

###### Spectrum: [Urban Management]

Autonomous Planning

![image 488](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile488.png)

Question: Using TES-derived land surface temperature from ASTER Bands 10-14 on June 15, 2022, over the specified Los Angeles metropolitan area, calculate the percentage of urban pixels exhibited LST > 300 K combined with emissivity < 0.96, indicating urban heat island intensity during early summer.

- A. 15.34%
- B. 28.67%
- C. 37.93%
- D. 41.13%


![image 489](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile489.png)

|![image 490](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile490.png)|
|---|


|![image 491](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile491.png)|
|---|


|![image 492](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile492.png)|
|---|


|![image 493](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile493.png)|
|---|


|![image 494](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile494.png)|
|---|


![image 495](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile495.png)

![image 496](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile496.png)

"name": get_filelist "input": { "dir_path":"benchmark/supported_data/question21"}

- Step1Final

GPT-5

- Step2


![image 497](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile497.png)

"output": [\"answer_21.py\",\"lst_tes_result.tif\"]

"name": calculate_multi_band_threshold_ratio "input": "image_path": "benchmark/supported_data/question21/lst_tes_result.tif", "band_conditions": [[0,300,"above"],[1,0.96,"below"]]}

![image 498](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile498.png)

![image 499](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile499.png)

v

"output": "41.13315833506345"

![image 500](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile500.png)

"final answer": "C"

![image 501](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile501.png)

![image 502](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile502.png)

![image 503](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile503.png)

![image 504](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile504.png)

![image 505](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile505.png)

Step-by-Step: TAO: 0.67 End-to-End: Efficiency: 0.6667

TIO: 0.33 TEM: 0.33 Param.: 0.0 Acc: 100%

![image 506](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile506.png)

![image 507](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile507.png)

![image 508](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile508.png)

###### GT

Tool 1 -> Tool 4 -> Tool 3 -> D

- Tool 1: get_filelist
- Tool 2: calc_batch_image_std
- Tool 3: calculate_multi_band_threshold_ratio


Tool 4: temperature_emissivity_separation Tool 6:calc_batch_image_skewness

###### Tool 5: calc_batch_image_mean

Tool 8: calc_batch_image_mean_max_min

###### Agent

![image 509](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile509.png)

![image 510](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile510.png)

Tool 1 -> Tool 3 ×𝟑 -> D

![image 511](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile511.png)

GPT-5

![image 512](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile512.png)

![image 513](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile513.png)

![image 514](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile514.png)

Tool 1 -> Tool 3 ×𝟑 -> D

![image 515](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile515.png)

Kimi-K2

![image 516](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile516.png)

![image 517](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile517.png)

![image 518](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile518.png)

×𝟐 Tool 5 -> Tool 8 -> Tool 6 -> Tool 7 -> Tool 2 -> Tool 3 ×𝟑 -> D

Tool 1 ->

![image 519](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile519.png)

Deepseek V3.1

![image 520](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile520.png)

![image 521](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile521.png)

![image 522](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile522.png)

![image 523](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile523.png)

![image 524](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile524.png)

![image 525](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile525.png)

![image 526](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile526.png)

###### Figure 17: Example of Urban Management with Spectrum Data under the Auto-Planning

![image 527](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile527.png)

![image 528](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile528.png)

###### Spectrum: [Urban Management]

Instruction Following

![image 529](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile529.png)

Question: Using TES-derived land surface temperature from ASTER Bands 10–14 on June 15, 2022, over the Los Angeles metropolitan area, first list the input TIFF files, then apply the Temperature and Emissivity Separation (TES) algorithm to estimate land surface temperature. Finally, calculate the percentage of urban pixels where LST exceeds 300 K and emissivity is below 0.96, indicating the intensity of the urban heat island during early summer.

- A. 15.34%
- B. 28.67%
- C. 37.93%
- D. 41.13%


![image 530](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile530.png)

|![image 531](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile531.png)|
|---|


|![image 532](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile532.png)|
|---|


|![image 533](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile533.png)|
|---|


|![image 534](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile534.png)|
|---|


|![image 535](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile535.png)|
|---|


GPT-5

![image 536](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile536.png)

![image 537](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile537.png)

"name": get_filelist "input": { "dir_path":"benchmark/supported_data/question21"}

Step1Step2Final

![image 538](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile538.png)

"output": [\"answer_21.py\",\"lst_tes_result.tif\"]

"name": calculate_multi_band_threshold_ratio "input": "image_path": "benchmark/supported_data/question21/lst_tes_result.tif", "band_conditions": [[0,300,"above"],[1,0.96,"below"]]}

![image 539](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile539.png)

![image 540](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile540.png)

"output": "41.13315833506345"

v

![image 541](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile541.png)

"final answer": "C"

![image 542](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile542.png)

![image 543](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile543.png)

![image 544](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile544.png)

![image 545](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile545.png)

![image 546](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile546.png)

TIO: 0.33 TEM: 0.33 Param.: 0.0 Acc: 100%

Step-by-Step: TAO: 0.67 End-to-End: Efficiency: 0.6667

![image 547](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile547.png)

![image 548](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile548.png)

![image 549](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile549.png)

###### GT

Tool 1 -> Tool 4 -> Tool 3 -> D

- Tool 1: get_filelist
- Tool 2: calc_batch_image_std
- Tool 3: calculate_multi_band_threshold_ratio


Tool 4: temperature_emissivity_separation Tool 6:calc_batch_image_skewness

Tool 5: calc_batch_image_mean

Tool 8: calc_batch_image_mean_max_min

![image 550](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile550.png)

###### Agent

![image 551](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile551.png)

Tool 1 -> Tool 3 -> D

![image 552](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile552.png)

GPT-5

![image 553](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile553.png)

![image 554](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile554.png)

![image 555](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile555.png)

Tool 1 -> Tool 3 -> D

![image 556](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile556.png)

Kimi-K2

![image 557](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile557.png)

![image 558](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile558.png)

![image 559](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile559.png)

×𝟑 -> Tool 3 -> D

![image 560](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile560.png)

Tool 1

Deepseek V3.1

![image 561](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile561.png)

![image 562](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile562.png)

###### Figure 18: Example of Urban Management with Spectrum Data under the Instruction-

![image 563](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile563.png)

Spectrum: [Vegetation Monitoring]

![image 564](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile564.png)

Autonomous Planning

![image 565](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile565.png)

Question: Based on TES output from ASTER thermal bands on March 24, 2020 in the Sahara Desert region near Tamanrasset, Algeria, calculate the proportion of the area where emissivity variation (Δε) exceeds 0.05, indicating possible land cover heterogeneity.

- A. 7.63%
- B. 11.13%
- C. 21.85%
- D. 29.39%


![image 566](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile566.png)

|![image 567](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile567.png)|
|---|


|![image 568](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile568.png)|
|---|


|![image 569](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile569.png)|
|---|


|![image 570](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile570.png)|
|---|


|![image 571](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile571.png)|
|---|


###### Deepseek V3.1

![image 572](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile572.png)

![image 573](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile573.png)

"name": get_filelist "input": { "dir_path": "benchmark/data/question23"}

- Step1FinalStep10 …

![image 574](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile574.png)

- Step2


![image 575](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile575.png)

d

"output": [\“2020_03_24_BT_10.tif\”,…, \"2020_03_24_BT_14.tif\"]

"name": temperature_emissivity_separation "input": "tir_band_paths": ["benchmark/data/question23/2020_03_24_BT_10.tif",…, "benchmark/data/question23/2020_03_24_BT_14.tif“], "representative_band_index": 3, "output_path":"question23/tes_output.tif"

![image 576](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile576.png)

![image 577](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile577.png)

"output": ["Result saved at out/question23/tes_output.tif“]

"name": calculate_area "input": "input_image_path": "out/question23/tes_output.tif",

![image 578](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile578.png)

"gsd": 1

v

![image 579](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile579.png)

“output": "2351880.0"

![image 580](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile580.png)

"final answer": "C"

![image 581](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile581.png)

TIO: 1.0 TEM: 0.67 Param.: 0.33 Acc: 0%

![image 582](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile582.png)

![image 583](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile583.png)

![image 584](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile584.png)

![image 585](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile585.png)

Step-by-Step: TAO: 1.0 End-to-End: Efficiency:3.3333

![image 586](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile586.png)

![image 587](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile587.png)

![image 588](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile588.png)

###### GT

Tool 1 -> Tool 7 -> Tool 4 -> B

Tool 1: get_filelist Tool 4: calculate_threshold_ratio Tool 7: temperature_emissivity_separation

Tool 2: calc_batch_image_hotspot_percentage Tool 3: threshold_segmentation

Tool 5: identify_fire_prone_areas

Tool 8: calc_batch_image_hotspot_tif

Tool 10: calc_batch_image_sum Tool 11: calc_extreme_snow_loss_percentage_from_binary_map

Tool 12: count_pixels_satisfying_conditions Tool 13: calculate_multi_band_threshold_ratio Tool 14: get_percentile_value_from_image

###### Agent

![image 589](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile589.png)

![image 590](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile590.png)

Tool 1 -> Tool 7 -> Tool 4 ×𝟐 -> Tool 13 ->

×𝟑 Tool 4 -> Tool 13 ×𝟑 -> C

GPT-5

![image 591](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile591.png)

![image 592](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile592.png)

![image 593](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile593.png)

![image 594](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile594.png)

![image 595](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile595.png)

![image 596](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile596.png)

![image 597](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile597.png)

![image 598](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile598.png)

-> Fail

Kimi-K2

-> -> -> -> --

Tool 7 Tool 5 Tool 3 Tool 8

![image 599](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile599.png)

Tool 1

Deepseek V3.1

![image 600](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile600.png)

![image 601](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile601.png)

![image 602](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile602.png)

![image 603](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile603.png)

->

![image 604](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile604.png)

![image 605](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile605.png)

--

-> -> -> -> C

Tool 4 Tool 9

->

Tool 6 Tool 10

×𝟐

![image 606](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile606.png)

![image 607](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile607.png)

![image 608](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile608.png)

![image 609](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile609.png)

###### Figure 19: Example of Vegetation Monitoring with Spectrum Data under the Auto-Planning

![image 610](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile610.png)

Spectrum: [Vegetation Monitoring]

![image 611](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile611.png)

Instruction Following

![image 612](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile612.png)

Question: Based on TES output from ASTER thermal bands on March 24, 2020, in the Sahara Desert region near Tamanrasset, Algeria, first list the input TIFF files, then apply the Temperature and Emissivity Separation (TES) algorithm to estimate land surface temperature and emissivity. Finally, calculate the proportion of the area where emissivity variation (Δε) exceeds 0.05, indicating potential land cover heterogeneity.

- A. 7.63%
- B. 11.13%
- C. 21.85%
- D. 29.39%


![image 613](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile613.png)

Spectrum

|![image 614](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile614.png)|
|---|


|![image 615](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile615.png)|
|---|


|![image 616](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile616.png)|
|---|


|![image 617](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile617.png)|
|---|


|![image 618](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile618.png)|
|---|


###### Deepseek V3.1

![image 619](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile619.png)

![image 620](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile620.png)

"name": get_filelist "input": { "dir_path": "benchmark/data/question23"}

Step2Step1FinalStep9

![image 621](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile621.png)

d

"output": [\“2020_03_24_BT_10.tif\”,…, \"2020_03_24_BT_14.tif\"]

"name": temperature_emissivity_separation "input": "tir_band_paths": ["benchmark/data/question23/2020_03_24_BT_10.tif",…, "benchmark/data/question23/2020_03_24_BT_14.tif“], "representative_band_index": 3, "output_path":"question23/tes_output.tif"

![image 622](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile622.png)

![image 623](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile623.png)

"output": ["Result saved at out/question23/tes_output.tif“]

…

"name": calculate_area "input": "input_image_path": "out/question23/tes_output.tif",

![image 624](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile624.png)

"gsd": 1

v

![image 625](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile625.png)

"output": "2351880.0"

![image 626](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile626.png)

"final answer": "C"

![image 627](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile627.png)

TIO: 1.0 TEM: 0.67 Param.: 0.33 Acc: 0%

![image 628](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile628.png)

![image 629](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile629.png)

![image 630](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile630.png)

![image 631](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile631.png)

Step-by-Step: TAO: 1.0 End-to-End: Efficiency: 3.3333

![image 632](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile632.png)

![image 633](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile633.png)

![image 634](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile634.png)

###### GT

Tool 1 -> Tool 7 -> Tool 4 -> B

Tool 1: get_filelist Tool 4: calculate_threshold_ratio Tool 7: temperature_emissivity_separation

Tool 2: calc_batch_image_hotspot_percentage Tool 3: threshold_segmentation

Tool 5: identify_fire_prone_areas

Tool 8: calc_batch_image_hotspot_tif

Tool 10: calc_batch_image_sum

Tool 11: calc_extreme_snow_loss_percentage_from_binary_map

Tool 12: count_pixels_satisfying_conditions Tool 13: calculate_multi_band_threshold_ratio Tool 14: get_percentile_value_from_image

###### Agent

![image 635](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile635.png)

Tool 1 -> Tool 7 -> Tool 4 ×𝟐 -> Tool 13 -> Tool 4 -> Tool 12 ×𝟐 -> Tool 4 ×𝟓 -> B

![image 636](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile636.png)

![image 637](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile637.png)

GPT-5

![image 638](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile638.png)

![image 639](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile639.png)

![image 640](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile640.png)

![image 641](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile641.png)

![image 642](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile642.png)

![image 643](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile643.png)

![image 644](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile644.png)

Tool 1 Tool 7 -> Tool 14 -> Tool 12 -> B

![image 645](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile645.png)

![image 646](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile646.png)

- ->
- -> -> Tool 4


###### ->

×𝟐 Tool 13

Kimi-K2

![image 647](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile647.png)

![image 648](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile648.png)

![image 649](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile649.png)

![image 650](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile650.png)

![image 651](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile651.png)

![image 652](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile652.png)

-> -> -> -> --

Tool 7 Tool 11 Tool 4 Tool 2

Tool 1

![image 653](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile653.png)

![image 654](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile654.png)

![image 655](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile655.png)

->

Deepseek V3.1

![image 656](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile656.png)

![image 657](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile657.png)

![image 658](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile658.png)

![image 659](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile659.png)

--

-> -> -> -> C

Tool 6 ->

Tool 8 Tool 9

Tool 3 Tool 10

![image 660](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile660.png)

![image 661](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile661.png)

![image 662](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile662.png)

![image 663](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile663.png)

![image 664](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile664.png)

###### Figure 20: Example of Vegetation Monitoring with Spectrum Data under the Instruction-Following Regime.

![image 665](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile665.png)

![image 666](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile666.png)

Products: [Pollution Regulation]

Autonomous Planning

![image 667](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile667.png)

Question: Based on the sur_refl_b01 and sur_refl_b04 data of the Arctic Ocean, calculate the NDTI. Determine whether ocean turbidity in the Arctic Ocean increased or decreased over this period, and report the magnitude of the change.

- A. The average NDTI decreased slightly from about -0.0472 in July 2012 to about -0.0502 in July 2022, meaning turbidity weakened and the magnitude of change was roughly 0.0030.
- B. The average NDTI increased from about -0.050162 in July 2012 to about -0.047156 in July 2022, so ocean turbidity increased (less negative NDTI) with a magnitude of about 0.003006.
- C. The average NDTI increased from about -0.0472 to -0.0502, indicating much clearer water, with a magnitude near 0.0030.
- D. Average NDTI values of roughly -0.0502 and -0.0472 show no detectable change in turbidity between 2012 and 2022.
- E. Average NDTI stayed at about -0.05 for both years, so there was virtually zero change.


![image 668](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile668.png)

|![image 669](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile669.png)|
|---|


|![image 670](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile670.png)|
|---|


|![image 671](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile671.png)|
|---|


|![image 672](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile672.png)|
|---|


###### … …

###### B1 × 72

B4 × 72

![image 673](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile673.png)

GPT-5

![image 674](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile674.png)

"name": get_filelist "input": { "dir_path": "benchmark/data/question182"}

Step1Step7Step2-3

![image 675](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile675.png)

"output": [\"Arctic_Ocean_sur_refl_b01_2012-07-01.tif\",…, \"Arctic_Ocean_sur_refl_b04_2022-07-29.tif\"]

"name": calculate_batch_ndti "input":"input_red_paths": ["benchmark/data/question182/Arctic_Ocean_sur_refl_b04_2012-0701.tif",…,"benchmark/data/question182/Arctic_Ocean_sur_refl_b04_2022-07-29.tif"], "input_green_paths": ["benchmark/data/question182/Arctic_Ocean_sur_refl_b01_2012-07-01.tif",…, "benchmark/data/question182/Arctic_Ocean_sur_refl_b01_2022-07-29.tif"], "output_paths": ["question182/ndti_201207-01.tif",..., "question182/ndti_2022-07-29.tif"]

![image 676](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile676.png)

"output": [\"Result save at out/question182/ndti_2012-07-01.tif\",…, \"Result save at out/question182/ndti_2022-07-29.tif\"]

![image 677](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile677.png)

v

…

"name": mean "input": ["-13.095973014831543",..."-5.5260844230651855"]

![image 678](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile678.png)

![image 679](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile679.png)

"output": "-15.605616776148478"

Final

![image 680](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile680.png)

"final answer": "B"

![image 681](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile681.png)

![image 682](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile682.png)

![image 683](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile683.png)

![image 684](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile684.png)

![image 685](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile685.png)

TIO: 0.03 TEM: 0.03 Param.: 0.03 Acc: 100%

Step-by-Step: TAO: 0.5 End-to-End: Efficiency:0.2258

![image 686](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile686.png)

![image 687](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile687.png)

![image 688](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile688.png)

###### GT

Tool 1 -> Tool 2 -> Tool 3 -> B

-> Tool 4 Tool 3: calc_batch_image_mean

×𝟐 ×𝟐

Tool 1: get_filelist Tool 4: difference

Tool 2: calculate_ndti Tool 5: calculate_batch_ndti

Tool 7: calc_batch_image_mean_mean

###### Agent

![image 689](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile689.png)

![image 690](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile690.png)

![image 691](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile691.png)

Tool 1 -> Tool 5 ×𝟐 -> Tool 7 ×𝟐 -> B

GPT-5

![image 692](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile692.png)

![image 693](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile693.png)

![image 694](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile694.png)

![image 695](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile695.png)

![image 696](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile696.png)

Tool 1 -> Tool 5 ×𝟐 -> Tool 7 ×𝟐 -> A

Kimi-K2

![image 697](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile697.png)

![image 698](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile698.png)

![image 699](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile699.png)

![image 700](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile700.png)

![image 701](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile701.png)

Deepseek V3.1

Tool 1 -> Tool 5 ×𝟐 -> Tool 7 ×𝟑 -> Tool 4 -> A

![image 702](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile702.png)

![image 703](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile703.png)

![image 704](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile704.png)

![image 705](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile705.png)

###### Figure 21: Example of Pollution Regulation with Products Data under the Auto-Planning

![image 706](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile706.png)

![image 707](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile707.png)

Products: [Pollution Regulation]

###### Instruction Following

![image 708](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile708.png)

Question:Based on the sur_refl_b01 and sur_refl_b04 data of the Arctic Ocean, calculate the NDTI and compute the average NDTI values for July 2012 and July 2022. Determine whether ocean turbidity in the Arctic Ocean increased or decreased over this period, and report the magnitude of the change.

- A. The average NDTI decreased slightly from about -0.0472 in July 2012 to about -0.0502 in July 2022, meaning turbidity weakened and the magnitude of change was roughly 0.0030.
- B. The average NDTI increased from about -0.050162 in July 2012 to about -0.047156 in July 2022, so ocean turbidity increased (less negative NDTI) with a magnitude of about 0.003006.
- C. The average NDTI increased from about -0.0472 to -0.0502, indicating much clearer water, with a magnitude near 0.0030.
- D. Average NDTI values of roughly -0.0502 and -0.0472 show no detectable change in turbidity between 2012 and 2022.
- E. Average NDTI stayed at about -0.05 for both years, so there was virtually zero change.


![image 709](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile709.png)

![image 710](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile710.png)

|![image 711](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile711.png)|
|---|


|![image 712](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile712.png)|
|---|


|![image 713](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile713.png)|
|---|


|![image 714](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile714.png)|
|---|


##### … …

B1 × 72

B4 × 72

![image 715](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile715.png)

###### GPT-5

![image 716](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile716.png)

"name": get_filelist "input": { "dir_path": "benchmark/data/question182"}

FinalStep1Step11Step2-3

![image 717](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile717.png)

"output": [\"Arctic_Ocean_sur_refl_b01_2012-07-01.tif\",…, \"Arctic_Ocean_sur_refl_b04_2022-07-29.tif\"]

"name": calculate_batch_ndti "input":"input_red_paths": ["benchmark/data/question182/Arctic_Ocean_sur_refl_b04_2012-0701.tif",…,"benchmark/data/question182/Arctic_Ocean_sur_refl_b04_2022-07-29.tif"], "input_green_paths": ["benchmark/data/question182/Arctic_Ocean_sur_refl_b01_2012-07-01.tif",…, "benchmark/data/question182/Arctic_Ocean_sur_refl_b01_2022-07-29.tif"], "output_paths": ["question182/ndti_201207-01.tif",..., "question182/ndti_2022-07-29.tif"]

![image 718](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile718.png)

"output": [\"Result save at out/question182/ndti_2012-07-01.tif\",…, \"Result save at out/question182/ndti_2022-07-29.tif\"]

![image 719](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile719.png)

v

…

![image 720](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile720.png)

"name": mean "input": ["-13.095973014831543",..."-5.5260844230651855"]

![image 721](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile721.png)

"output": "-15.605616776148478"

![image 722](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile722.png)

"final answer": "B"

![image 723](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile723.png)

![image 724](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile724.png)

![image 725](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile725.png)

![image 726](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile726.png)

![image 727](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile727.png)

TIO: 0.03 TEM: 0.03 Param.: 0.03 Acc: 100%

Step-by-Step: TAO: 0.5 End-to-End: Efficiency: 0.3548

![image 728](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile728.png)

![image 729](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile729.png)

![image 730](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile730.png)

###### GT

Tool 1 -> Tool 2 -> Tool 3 -> B

-> Tool 4 Tool 3: calc_batch_image_mean

×𝟐 ×𝟐

Tool 1: get_filelist Tool 4: difference

Tool 2: calculate_ndti Tool 5: calculate_batch_ndti

Tool 7: calc_batch_image_mean_mean Tool 6: get_list_object_via_indexes

###### Agent

![image 731](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile731.png)

![image 732](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile732.png)

![image 733](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile733.png)

Tool 1 -> Tool 5 ×𝟐 -> Tool 7 ×𝟐 -> B

GPT-5

![image 734](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile734.png)

![image 735](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile735.png)

![image 736](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile736.png)

![image 737](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile737.png)

![image 738](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile738.png)

Tool 1 -> Tool 3 -> A

Kimi-K2

![image 739](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile739.png)

![image 740](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile740.png)

![image 741](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile741.png)

Deepseek V3.1

Tool 1 -> Tool 6 ×𝟒 -> Tool 5 ×𝟐 -> Tool 4 -> A

Tool 7 ×𝟑 ->

![image 742](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile742.png)

![image 743](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile743.png)

![image 744](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile744.png)

![image 745](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile745.png)

![image 746](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile746.png)

![image 747](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile747.png)

###### Figure 22: Example of Pollution Regulation with Products Data under the Instruction-Following Regime.

![image 748](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile748.png)

![image 749](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile749.png)

###### Products: [Urban Management]

![image 750](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile750.png)

Question: Based on the built_volume_total data of Shanghai from 1980 to 2025, calculate the total change in building volume for Shanghai between 1985 and 2020 and compute the percentage change.

- A. The total change is 10,392.58 and the percentage change is 179.96%
- B. The total change is 5,777.68 and the percentage change is 100.34%
- C. The total change is 16,170.27 and the percentage change is 279.96%
- D. The total change is 8,392.58 and the percentage change is 159.96%
- E. The total change is 13,459.37 and the percentage change is 233.00%


![image 751](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile751.png)

|![image 752](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile752.png)|
|---|


|![image 753](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile753.png)|
|---|


|![image 754](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile754.png)|
|---|


|![image 755](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile755.png)|
|---|


###### …

Build volume × 46

###### Deepseek V3.1

![image 756](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile756.png)

"name": get_filelist "input": { "dir_path":"benchmark/data/question186"}

![image 757](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile757.png)

- Step1Step4Final

![image 758](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile758.png)

Autonomous Planning

- Step2


![image 759](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile759.png)

"output": [\"Shanghai_built_volume_total_1980-01-01.tif\",…, \"Shanghai_built_volume_total_2025-01-01.tif\"]

"name": calc_batch_image_sum "input": "file_list": ["benchmark/data/question186/Shanghai_built_volume_total_1985-01-01.tif“, "benchmark/data/question186/Shanghai_built_volume_total_2020-01-01.tif"]

![image 760](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile760.png)

![image 761](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile761.png)

"output": [5034765847.0, 14091027671.0]

…

"name": percentage_change "input": {"a": 5034765847.0, "b": 14091027671.0}

![image 762](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile762.png)

v

![image 763](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile763.png)

"output": "179.87453834414634"

![image 764](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile764.png)

"final answer": “A"

![image 765](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile765.png)

![image 766](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile766.png)

![image 767](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile767.png)

![image 768](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile768.png)

![image 769](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile769.png)

TIO: 0.25 TEM: 0.25 Param.: 0.25 Acc: 100%

Step-by-Step: TAO: 0.75 End-to-End: Efficiency: 1.0

![image 770](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile770.png)

![image 771](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile771.png)

![image 772](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile772.png)

###### GT

-> Tool 4

Tool 1 -> Tool 2 -> Tool 3 -> A

Tool 1: get_filelist Tool 4: percentage_change

Tool 2: calc_batch_image_mean Tool 3: difference Tool 5: calc_batch_image_sum

###### Agent

![image 773](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile773.png)

Tool 1 -> Tool 5 -> Tool 3 -> Tool 4 -> A

![image 774](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile774.png)

GPT-5

![image 775](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile775.png)

![image 776](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile776.png)

![image 777](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile777.png)

![image 778](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile778.png)

![image 779](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile779.png)

Tool 1 -> Tool 2 -> A

![image 780](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile780.png)

Kimi-K2

![image 781](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile781.png)

![image 782](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile782.png)

![image 783](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile783.png)

![image 784](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile784.png)

Tool 1 -> Tool 5 -> Tool 3 -> Tool 4 -> A

Deepseek V3.1

![image 785](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile785.png)

![image 786](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile786.png)

![image 787](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile787.png)

![image 788](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile788.png)

- Figure 23: Example of Urban Management with Products Data under the Auto-Planning


![image 789](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile789.png)

![image 790](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile790.png)

Products: [Water Mangement]

![image 791](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile791.png)

Question: Process Lake Geneva's NDVI data (August 2022) to determine peak vegetation coverage and NDVI extremes.

- A.2022-08-01 (NDVI: 0.5636)
- B. 2022-08-03 (NDVI: 0.5443) C. 2022-08-12 (NDVI: 0.4755) D. 2022-08-29 (NDVI: 0.4958)


|![image 792](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile792.png)|
|---|


|![image 793](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile793.png)|
|---|


|![image 794](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile794.png)|
|---|


|![image 795](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile795.png)|
|---|


|![image 796](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile796.png)|
|---|


|![image 797](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile797.png)|
|---|


###### …

B2 × 31 B4 × 31

![image 798](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile798.png)

Kimi-K2

![image 799](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile799.png)

"name": get_filelist "input": { "dir_path": "benchmark/data/question125"}

- Step1Step5

![image 800](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile800.png)

![image 801](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile801.png)

Autonomous Planning

- Step2


"output": [\"Geneva-Lake_sur_refl_b01_2022-08-01.tif\",…, \"Geneva-Lake_sur_refl_b01_2022-08-30.tif\", \"Geneva-Lake_sur_refl_b02_2022-08-01.tif\",\"Geneva-Lake_sur_refl_b02_2022-08-30.tif\" ]

![image 802](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile802.png)

"name": calculate_ndvi "input": "red_band_file": ["benchmark/data/question125/Geneva-Lake_sur_refl_b01_2022-08-01.tif",…,

![image 803](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile803.png)

"benchmark/data/question125/Geneva-Lake_sur_refl_b01_2022-08-30.tif"] "nir_band_file": ["benchmark/data/question125/Geneva-Lake_sur_refl_b02_2022-08-

01.tif",...,"benchmark/data/question125/Geneva-Lake_sur_refl_b02_2022-08-30.tif"]

![image 804](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile804.png)

"output": ["geneva_ndvi_2022-08-01.tif",...,"geneva_ndvi_2022-08-30.tif"]

…

"name": calc_batch_image_mean "input": {"file_list": ["geneva_ndvi_2022-08-01.tif",…, "geneva_ndvi_2022-08-30.tif"]}

![image 805](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile805.png)

v

![image 806](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile806.png)

"output": [0.5636, 0.4441,0.5443,..., 0.0733]

![image 807](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile807.png)

Final

"final answer": “A"

![image 808](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile808.png)

TIO: 0.5 TEM: 0.25 Param.: 0.0 Acc: 100%

![image 809](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile809.png)

![image 810](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile810.png)

![image 811](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile811.png)

Step-by-Step: TAO: 0.67 End-to-End: Efficiency: 1.2500

![image 812](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile812.png)

![image 813](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile813.png)

![image 814](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile814.png)

![image 815](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile815.png)

###### GT

Tool 1 -> Tool 2 -> Tool 4 -> A

×𝟑 -> Tool 3 ×𝟒 ×𝟐

Tool 1: get_filelist Tool 4: max_value_and_index Tool 5: calc_batch_image_max Tool 6: calc_batch_image_median Tool 7: get_percentile_value_from_image Tool 8: calc_batch_image_hotspot_percentage

Tool 2: calculate_ndvi Tool 3: calc_batch_image_mean

###### Agent

![image 816](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile816.png)

![image 817](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile817.png)

Tool 1 -> Tool 2 -> Tool 6 -> C

GPT-5

![image 818](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile818.png)

![image 819](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile819.png)

![image 820](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile820.png)

![image 821](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile821.png)

![image 822](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile822.png)

Tool 1 -> Tool 4 -> Tool 3 -> Tool 6 -> Tool 9 -> A

Kimi-K2

![image 823](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile823.png)

![image 824](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile824.png)

![image 825](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile825.png)

![image 826](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile826.png)

![image 827](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile827.png)

![image 828](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile828.png)

×𝟑

Tool 1 -> Tool 2 -> Tool 3 -> Tool 5 -> Tool 5 A

-> Tool 6 -> Tool 7 --> Tool 8

-->

Deepseek V3.1

![image 829](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile829.png)

![image 830](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile830.png)

![image 831](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile831.png)

![image 832](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile832.png)

![image 833](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile833.png)

![image 834](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile834.png)

![image 835](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile835.png)

![image 836](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile836.png)

![image 837](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile837.png)

###### Figure 24: Example of Water Management with Products Data under the Auto-Planning

![image 838](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile838.png)

![image 839](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile839.png)

Products: [Water Mangement]

###### Instruction Following

Question: Define the area where NDVI is greater than 0.3 as vegetation cover. Based on the multispectral

![image 840](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile840.png)

remote sensing data of Lake Geneva in August 2022, calculate the NDVI vegetation index, determine the daily vegetation coverage proportion of the lake area, and identify the date with the highest NDVI value during this month.

- A.2022-08-01 (NDVI: 0.5636)
- B. 2022-08-03 (NDVI: 0.5443)
- C. 2022-08-12 (NDVI: 0.4755)
- D. 2022-08-29 (NDVI: 0.4958)


![image 841](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile841.png)

|![image 842](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile842.png)|
|---|


|![image 843](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile843.png)|
|---|


|![image 844](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile844.png)|
|---|


|![image 845](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile845.png)|
|---|


|![image 846](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile846.png)|
|---|


|![image 847](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile847.png)|
|---|


#### …

B2 × 31 B4 × 31

![image 848](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile848.png)

Kimi-K2

![image 849](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile849.png)

"name": get_filelist "input": { "dir_path": "benchmark/data/question125"}

Step14FinalStep1Step2-5

![image 850](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile850.png)

"output": [\"Geneva-Lake_sur_refl_b01_2022-08-01.tif\",…, \"Geneva-Lake_sur_refl_b01_2022-08-30.tif\", \"Geneva-Lake_sur_refl_b02_2022-08-01.tif\",\"Geneva-Lake_sur_refl_b02_2022-08-30.tif\" ]

"name": calculate_ndvi "input": "red_band_file": ["benchmark/data/question125/Geneva-Lake_sur_refl_b01_2022-08-01.tif",…,

![image 851](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile851.png)

"benchmark/data/question125/Geneva-Lake_sur_refl_b01_2022-08-30.tif"] "nir_band_file": ["benchmark/data/question125/Geneva-Lake_sur_refl_b02_2022-08-

01.tif",...,"benchmark/data/question125/Geneva-Lake_sur_refl_b02_2022-08-30.tif"]

![image 852](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile852.png)

"output": ["geneva_ndvi_2022-08-01.tif",...,"geneva_ndvi_2022-08-30.tif"]

…

"name": calc_batch_image_max "input": {"file_list": ["benchmark/data/question125/geneva_ndwi_2022-08-01.tif",…, "benchmark/data/question125/geneva_ndwi_2022-08-04.tif"]}

![image 853](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile853.png)

v

![image 854](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile854.png)

"output": ["43.874401612496854","22.91341227849164"]

![image 855](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile855.png)

"final answer": “A"

![image 856](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile856.png)

![image 857](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile857.png)

![image 858](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile858.png)

![image 859](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile859.png)

![image 860](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile860.png)

TIO: 0.25 TEM: 0.25 Param.: 0.0 Acc: 100%

Step-by-Step: TAO: 0.33 End-to-End: Efficiency: 3.7500

![image 861](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile861.png)

![image 862](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile862.png)

![image 863](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile863.png)

GT

###### Tool 1 -> Tool 2 ×𝟑 -> Tool 3 ×𝟒 -> Tool 4 ×𝟐 -> A

Tool 1: get_filelist Tool 4: max_value_and_index Tool 5: calc_batch_image_max Tool 6: calc_batch_image_median Tool 7: get_percentile_value_from_image Tool 8: calc_batch_image_hotspot_percentage

Tool 2: calculate_ndvi Tool 3: calc_batch_image_mean

max_value_and_index

Agent

![image 864](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile864.png)

![image 865](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile865.png)

![image 866](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile866.png)

Tool 1 -> Tool 3 -> Tool 6 -> C

GPT-5

![image 867](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile867.png)

![image 868](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile868.png)

![image 869](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile869.png)

![image 870](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile870.png)

Tool 1 -> Tool 12 ×𝟒 -> Tool 6 -> Tool 12 ×𝟒 -> Tool 6 ×𝟒 -> A

Kimi-K2

![image 871](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile871.png)

![image 872](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile872.png)

![image 873](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile873.png)

![image 874](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile874.png)

![image 875](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile875.png)

![image 876](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile876.png)

![image 877](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile877.png)

![image 878](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile878.png)

Tool 1 -> Tool 2 -> Tool 8 -> Tool 3 -> Tool 4 -> B

Deepseek V3.1

![image 879](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile879.png)

![image 880](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile880.png)

![image 881](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile881.png)

![image 882](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile882.png)

![image 883](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile883.png)

###### Figure 25: Example of Water Management with Products Data under the Instruction-Following Regime.

![image 884](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile884.png)

![image 885](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile885.png)

Products: [Weather Forecasting]

![image 886](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile886.png)

Question: Based on the precipitation index of the Congo Rainforest from May 1 to May 31, 2025. Calculate the daily average rainfall of the region during this period, and use a linear trend to determine the rainfall trend over these 31 days.

- A. The daily average rainfall is 6.18 mm, and the rainfall shows a slightly increasing trend.
- B. The daily average rainfall is 6.18 mm, and the rainfall shows a slightly decreasing trend.
- C. The daily average rainfall is 8.25 mm, and the rainfall shows a slightly increasing trend.
- D. The daily average rainfall is 8.25 mm, and the rainfall shows a slightly decreasing trend.
- E. The daily average rainfall is 5.03 mm, and the rainfall shows a slightly decreasing trend.


![image 887](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile887.png)

|![image 888](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile888.png)|
|---|


|![image 889](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile889.png)|
|---|


|![image 890](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile890.png)|
|---|


… precipitation×30

![image 891](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile891.png)

Kimi-K2

![image 892](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile892.png)

"name": get_filelist "input": { "dir_path": "benchmark/data/question145"}

- Step1Step4

Autonomous Planning

- Step2


![image 893](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile893.png)

"output": [\"Congo_precipitation_2025-05-01.tif\",…, \"Congo_precipitation_2025-05-30.tif"]

"name": calc_batch_image_mean "input": "file_list": ["benchmark/data/question145/Congo_precipitation_2025-05-01.tif",..., "benchmark/data/question145/Congo_precipitation_2025-05-30.tif"]

![image 894](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile894.png)

![image 895](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile895.png)

"output": [16.150558471679688,…, 12.77880573272705]

…

"name": mean "input":"x": [16.150558471679688,…, 12.77880573272705]

![image 896](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile896.png)

v

![image 897](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile897.png)

"output": "6.546580737829208"

Final

![image 898](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile898.png)

"final answer": “A"

![image 899](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile899.png)

![image 900](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile900.png)

![image 901](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile901.png)

![image 902](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile902.png)

![image 903](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile903.png)

TIO: 0.75 TEM: 0.5 Param.: 0.5 Acc: 100%

Step-by-Step: TAO: 1.0 End-to-End: Efficiency: 1.0

![image 904](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile904.png)

![image 905](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile905.png)

![image 906](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile906.png)

###### GT

Tool 1 -> Tool 2 -> Tool 3 -> C

-> Tool 4

Tool 1: get_filelist Tool 4: compute_linear_trend

Tool 2: calc_batch_image_mean Tool 5: calc_batch_image_mean_mean

Tool 3: mean

###### Agent

![image 907](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile907.png)

![image 908](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile908.png)

![image 909](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile909.png)

Tool 1 ×𝟐 -> Tool 5 -> Tool 2 -> Tool 4 -> A

GPT-5

![image 910](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile910.png)

![image 911](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile911.png)

![image 912](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile912.png)

![image 913](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile913.png)

![image 914](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile914.png)

![image 915](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile915.png)

Tool 1 -> Tool 2 -> Tool 4 -> Tool 3 -> A

Kimi-K2

![image 916](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile916.png)

![image 917](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile917.png)

![image 918](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile918.png)

![image 919](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile919.png)

![image 920](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile920.png)

Tool 1 -> Tool 5 -> Tool 2 -> Tool 4 -> Tool 3 -> A

Deepseek V3.1

![image 921](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile921.png)

![image 922](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile922.png)

![image 923](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile923.png)

![image 924](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile924.png)

![image 925](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile925.png)

![image 926](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile926.png)

###### Figure 26: Example of Weather Management with Products Data under the Auto-Planning

![image 927](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile927.png)

![image 928](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile928.png)

Products: [Weather Forecasting]

Instruction Following

![image 929](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile929.png)

Question: Analyze the precipitation index of the Congo Rainforest from May 1 to May 31, 2025. Calculate the daily average rainfall of the region during this period, and use a linear trend to determine the rainfall trend over these 31 days.

- A. The daily average rainfall is 6.18 mm, and the rainfall shows a slightly increasing trend.
- B. The daily average rainfall is 6.18 mm, and the rainfall shows a slightly decreasing trend.
- C. The daily average rainfall is 8.25 mm, and the rainfall shows a slightly increasing trend.
- D. The daily average rainfall is 8.25 mm, and the rainfall shows a slightly decreasing trend.
- E. The daily average rainfall is 5.03 mm, and the rainfall shows a slightly decreasing trend.


![image 930](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile930.png)

|![image 931](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile931.png)|
|---|


|![image 932](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile932.png)|
|---|


|![image 933](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile933.png)|
|---|


… precipitation×30

![image 934](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile934.png)

Kimi-K2

![image 935](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile935.png)

"name": get_filelist "input": { "dir_path": "benchmark/data/question145"}

Step1-2Step4

![image 936](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile936.png)

"output": [\"Congo_precipitation_2025-05-01.tif\",…, \"Congo_precipitation_2025-05-30.tif"]

"name": calc_batch_image_mean "input": "file_list": ["benchmark/data/question145/Congo_precipitation_2025-05-01.tif",..., "benchmark/data/question145/Congo_precipitation_2025-05-30.tif"]

![image 937](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile937.png)

Step3

![image 938](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile938.png)

"output": [16.150558471679688,…, 12.77880573272705]

"name": compute_linear_trend "input":"y": [16.150558471679688,…, 12.77880573272705]

![image 939](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile939.png)

v

![image 940](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile940.png)

"output": [0.02519952430077995,6.181187635467897]

Final

![image 941](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile941.png)

"final answer": “A"

![image 942](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile942.png)

![image 943](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile943.png)

![image 944](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile944.png)

![image 945](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile945.png)

![image 946](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile946.png)

TIO: 1.0 TEM: 0.25 Param.: 0.25 Acc: 100%

Step-by-Step: TAO: 1.0 End-to-End: Efficiency: 1.2500

![image 947](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile947.png)

![image 948](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile948.png)

![image 949](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile949.png)

###### GT

Tool 1 -> Tool 2 -> Tool 3 -> C

-> Tool 4

Tool 1: get_filelist Tool 4: compute_linear_trend

Tool 2: calc_batch_image_mean Tool 5: calc_batch_image_mean_mean

Tool 3: mean

###### Agent

![image 950](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile950.png)

![image 951](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile951.png)

Tool 1 ×𝟐 -> Tool 2 -> Tool 3 -> Tool 5 -> A

Tool 4 ->

![image 952](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile952.png)

GPT-5

![image 953](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile953.png)

![image 954](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile954.png)

![image 955](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile955.png)

![image 956](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile956.png)

![image 957](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile957.png)

![image 958](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile958.png)

![image 959](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile959.png)

Tool 1 -> Tool 2 -> Tool 3 -> Tool 4 -> A

×𝟐

Kimi-K2

![image 960](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile960.png)

![image 961](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile961.png)

![image 962](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile962.png)

![image 963](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile963.png)

![image 964](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile964.png)

![image 965](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile965.png)

Tool 1 -> Tool 5 -> Tool 2 -> Tool 4 -> A

Deepseek V3.1

![image 966](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile966.png)

![image 967](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile967.png)

![image 968](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile968.png)

![image 969](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile969.png)

###### Figure 27: Example of Weather Management with Products Data under the Instruction-Following Regime.

![image 970](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile970.png)

###### Figure 28: Example of Change Detection with RGB Data under the Auto-Planning Regime.

![image 971](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile971.png)

###### Figure 29: Example of Change Detection with RGB Data under the Instruction-FollowingRegime.

![image 972](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile972.png)

###### Figure 30: Example of Classification with RGB Data under the Auto-Planning Regime.

![image 973](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile973.png)

###### Figure 31: Example of Classification with RGB Data under the Instruction-Following Regime.

![image 974](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile974.png)

###### Figure 32: Example of Detection with RGB Data under the Auto-Planning Regime.

![image 975](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile975.png)

![image 976](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile976.png)

###### RGB: [detection]

Instruction Following

![image 977](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile977.png)

Question: As part of a regional sports infrastructure audit, you are tasked with identifying all baseball

diamonds visible in the satellite imagery and estimating their total area using bounding boxes (GSD = 0.13 m/px).

- A.“About 500 m^2"
- B.“About 1500 m^2"
- C.“About 3500 m^2 "
- D.“About 80119 m^2 "


![image 978](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile978.png)

|![image 979](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile979.png)|
|---|


![image 980](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile980.png)

Kimi-K2

"name": get_filelist "input": { "dir_path":"benchmark/data/question210"}

![image 981](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile981.png)

###### Step1

![image 982](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile982.png)

"output": [\"P0382.png\"]

“output”:

![image 983](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile983.png)

"name": InstructSAM "input": "input_image_path": "benchmark/data/question210/P0382.png",

FinalStep4Step2

"text_prompt": "baseball diamond"

![image 984](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile984.png)

"output": Failed to call model

v

…

"name": calculate_bbox_area "input": "bboxes": [[324.6867656820466, 226.69173840553316, 533.4624042398284, 413.52994128196684], [820.7124196099571, 522.3619154364535, 1027.0236643744179, 721.6341783135465]]

![image 985](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile985.png)

![image 986](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile986.png)

"output": "961738.0548508337"

![image 987](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile987.png)

"final answer": “B"

![image 988](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile988.png)

![image 989](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile989.png)

![image 990](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile990.png)

![image 991](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile991.png)

![image 992](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile992.png)

TIO: 1.0 TEM: 0.0 Param.: 0.0 Acc: 100%

Step-by-Step: TAO: 1.0 End-to-End: Efficiency: 1.33

![image 993](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile993.png)

![image 994](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile994.png)

![image 995](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile995.png)

###### GT

-> Tool 3

Tool 1 -> Tool 2 -> B

Tool 2: SM3Det Tool 3: calculate_bbox_area Tool 4: InstructSAM

Tool 1: get_filelist

###### Agent

![image 996](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile996.png)

![image 997](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile997.png)

![image 998](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile998.png)

Tool 1 -> Tool 4 ×𝟐 -> Tool 2 -> B

GPT-5

![image 999](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile999.png)

![image 1000](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1000.png)

![image 1001](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1001.png)

![image 1002](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1002.png)

![image 1003](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1003.png)

Tool 1 -> Tool 4 -> Tool 2 -> Tool 3 -> B

Kimi-K2

![image 1004](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1004.png)

![image 1005](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1005.png)

![image 1006](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1006.png)

![image 1007](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1007.png)

![image 1008](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1008.png)

![image 1009](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1009.png)

Tool 1 -> Tool 4 -> Tool 2 -> Tool 3 ×𝟐 -> C

Deepseek V3.1

![image 1010](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1010.png)

![image 1011](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1011.png)

![image 1012](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1012.png)

![image 1013](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1013.png)

###### Figure 33: Example of Detection with RGB Data under the Instruction-Following Regime.

![image 1014](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1014.png)

###### Figure 34: Example of Visual Grounding with RGB Data under the Auto-Planning Regime.

![image 1015](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1015.png)

###### Figure 35: Example of Visual Grounding with RGB Data under the Instruction-FollowingRegime.

###### I CASE STUDY: COMPARE WITH OTHER AGENTS

![image 1016](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1016.png)

![image 1017](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1017.png)

###### Products: [Urban Management]

![image 1018](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1018.png)

Ground Truth :C

![image 1019](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1019.png)

Question: Analyze the nighttime light intensity trend in Leon (2013-2024) using linear regression.

![image 1020](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1020.png)

![image 1021](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1021.png)

![image 1022](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1022.png)

Operator :A

A."Slope: 0.10; Intercept: 1.85", B."Slope: 0.12; Intercept: 1.96", C."Slope: 0.14; Intercept: 2.05", D."Slope: 0.16; Intercept: 2.12"

![image 1023](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1023.png)

![image 1024](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1024.png)

![image 1025](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1025.png)

MGX :B

![image 1026](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1026.png)

![image 1027](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1027.png)

![image 1028](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1028.png)

v

Manus :FAIL

![image 1029](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1029.png)

![image 1030](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1030.png)

![image 1031](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1031.png)

![image 1032](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1032.png)

![image 1033](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1033.png)

![image 1034](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1034.png)

![image 1035](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1035.png)

Coze :B

...

![image 1036](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1036.png)

![image 1037](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1037.png)

![image 1038](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1038.png)

Earth-Agent(GPT5) :B

![image 1039](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1039.png)

![image 1040](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1040.png)

![image 1041](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1041.png)

Earth-Agent(DeepSeek-V3.1) :B

avg_rad×12

###### Figure 36: A Question Case of the Urban Management Task using Products Data with Re-sponses from Different Agent.

![image 1042](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1042.png)

![image 1043](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1043.png)

Products: [Urban Management]

![image 1044](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1044.png)

Ground Truth :B

![image 1045](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1045.png)

Question: Compare the nighttime light intensity between Mtwara and Santiago de Chile from January to March 2015, and calculate their average intensity difference.

![image 1046](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1046.png)

![image 1047](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1047.png)

![image 1048](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1048.png)

Operator :C

![image 1049](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1049.png)

![image 1050](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1050.png)

![image 1051](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1051.png)

MGX :C

- A."4.87",
- B."5.02",
- C."5.21",
- D."5.36"


![image 1052](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1052.png)

![image 1053](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1053.png)

![image 1054](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1054.png)

v

Manus :C

![image 1055](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1055.png)

![image 1056](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1056.png)

![image 1057](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1057.png)

Coze :C

![image 1058](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1058.png)

![image 1059](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1059.png)

![image 1060](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1060.png)

![image 1061](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1061.png)

![image 1062](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1062.png)

![image 1063](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1063.png)

![image 1064](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1064.png)

![image 1065](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1065.png)

![image 1066](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1066.png)

Earth-Agent(GPT5) :C

![image 1067](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1067.png)

![image 1068](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1068.png)

![image 1069](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1069.png)

Earth-Agent(DeepSeek-V3.1) :C

###### Figure 37: A Question Case of the Urban Management Task using Products Data with Re-sponses from Different Agent.

![image 1070](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1070.png)

![image 1071](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1071.png)

RGB: [change detection][detection]

![image 1072](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1072.png)

![image 1073](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1073.png)

Ground Truth :B

![image 1074](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1074.png)

Question:Based on satellite imagery before and after the natural disaster, determine how many buildings were completely destroyed using pre- and postdisaster satellite images.

![image 1075](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1075.png)

![image 1076](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1076.png)

![image 1077](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1077.png)

Operator :C

- A.“None building was completely destroyed.",
- B.“1 building was completely destroyed. ",
- C.“2 building was completely destroyed. ",
- D.“3 building was completely destroyed."


![image 1078](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1078.png)

![image 1079](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1079.png)

![image 1080](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1080.png)

MGX :FAIL

![image 1081](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1081.png)

![image 1082](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1082.png)

![image 1083](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1083.png)

v

Manus :B

![image 1084](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1084.png)

![image 1085](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1085.png)

![image 1086](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1086.png)

![image 1087](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1087.png)

![image 1088](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1088.png)

Coze :FAIL

![image 1089](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1089.png)

![image 1090](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1090.png)

![image 1091](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1091.png)

Earth-Agent(GPT5) :A

![image 1092](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1092.png)

![image 1093](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1093.png)

![image 1094](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1094.png)

Earth-Agent(DeepSeek-V3.1) :FAIL

###### Figure 38: A Question Case of the Change Detection Task using RGB Data with Responsesfrom Different Agent.

RGB: [classification]

![image 1095](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1095.png)

![image 1096](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1096.png)

![image 1097](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1097.png)

Ground Truth :A

![image 1098](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1098.png)

Question: Based on the following images, every image belongs to Airport, BareLand, BaseballField, Beach, Bridge, Center, Church, Commercial, DenseResidential, Desert, Farmland, Forest, Industrial, Meadow, MediumResidential, Mountain, Park, Parking, Playground, Pond, Port, RailwayStation, Resort, River, School, SparseResidential, Square, Stadium, StorageTanks, Viaduct, determine the number of images captured in bareland areas.

![image 1099](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1099.png)

![image 1100](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1100.png)

![image 1101](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1101.png)

Operator :B

![image 1102](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1102.png)

- A."3",
- B.“8",
- C."10",
- D."6"


![image 1103](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1103.png)

![image 1104](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1104.png)

MGX :FAIL

v

![image 1105](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1105.png)

![image 1106](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1106.png)

![image 1107](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1107.png)

Manus :B

![image 1108](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1108.png)

![image 1109](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1109.png)

![image 1110](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1110.png)

![image 1111](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1111.png)

![image 1112](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1112.png)

![image 1113](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1113.png)

![image 1114](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1114.png)

Coze :FAIL

###### …

![image 1115](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1115.png)

![image 1116](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1116.png)

![image 1117](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1117.png)

Earth-Agent(GPT5) :A

![image 1118](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1118.png)

![image 1119](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1119.png)

![image 1120](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1120.png)

Earth-Agent(DeepSeek-V3.1) :A

RBG×12

###### Figure 39: A Question Case of the Classification Task using RGB Data with Responses fromDifferent Agent.

RGB: [classification]

![image 1121](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1121.png)

![image 1122](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1122.png)

![image 1123](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1123.png)

![image 1124](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1124.png)

Question:Based on the following images, every image belongs to {Airport, BareLand, BaseballField, Beach, Bridge, Center, Church, Commercial, DenseResidential, Desert, Farmland, Forest, Industrial, Meadow, MediumResidential, Mountain, Park, Parking, Playground, Pond, Port, RailwayStation, Resort, River, School, SparseResidential, Square, Stadium, StorageTanks, Viaduct}, determine the number of images captured in mountain areas.

Ground Truth :B

![image 1125](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1125.png)

![image 1126](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1126.png)

![image 1127](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1127.png)

Operator :B

![image 1128](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1128.png)

![image 1129](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1129.png)

![image 1130](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1130.png)

- A.“11",
- B.“3",
- C.“2",
- D.“7"


MGX :FAIL

v

![image 1131](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1131.png)

![image 1132](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1132.png)

![image 1133](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1133.png)

Manus :B

![image 1134](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1134.png)

![image 1135](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1135.png)

![image 1136](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1136.png)

![image 1137](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1137.png)

![image 1138](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1138.png)

![image 1139](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1139.png)

![image 1140](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1140.png)

Coze :FAIL

…

![image 1141](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1141.png)

![image 1142](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1142.png)

![image 1143](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1143.png)

Earth-Agent(GPT5) :B

![image 1144](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1144.png)

![image 1145](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1145.png)

![image 1146](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1146.png)

Earth-Agent(DeepSeek-V3.1) :B

RGB×11

###### Figure 40: A Question Case of the Classification Task using RGB Data with Responses fromDifferent Agent.

![image 1147](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1147.png)

###### Figure 41: A Question Case of the Detection Task using RGB Data with Responses from Dif-ferent Agent.

![image 1148](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1148.png)

![image 1149](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1149.png)

RGB:RGB: [Visual Grounding][detection]

![image 1150](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1150.png)

![image 1151](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1151.png)

Ground Truth :A

![image 1152](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1152.png)

Question: Based on the following images, calculate the centroid-to-centroid distance between the two farthest plane in the image? (GSD = 0.14 m/px).

![image 1153](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1153.png)

![image 1154](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1154.png)

![image 1155](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1155.png)

Operator :D

- A.“About 265 m.",
- B.“About 270 m. ",
- C.“About 275 m. ",
- D.“About 280 m."


![image 1156](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1156.png)

![image 1157](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1157.png)

![image 1158](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1158.png)

MGX :FAIL

![image 1159](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1159.png)

![image 1160](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1160.png)

![image 1161](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1161.png)

v

Manus :C

![image 1162](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1162.png)

![image 1163](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1163.png)

![image 1164](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1164.png)

![image 1165](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1165.png)

Coze :FAIL

![image 1166](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1166.png)

![image 1167](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1167.png)

![image 1168](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1168.png)

Earth-Agent(GPT5) :A

![image 1169](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1169.png)

![image 1170](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1170.png)

![image 1171](Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents_images/imageFile1171.png)

Earth-Agent(DeepSeek-V3.1) :B

###### Figure 42: A Question Case of the Visual Grounding Task using RGB Data with Responsesfrom Different Agent.

