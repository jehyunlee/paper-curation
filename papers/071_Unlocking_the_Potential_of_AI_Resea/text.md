# Unlocking the Potential of AI Researchers in Scientific Discovery: What Is Missing?

#### A preprint

Hengjie Yu,1,2 Yaochu Jin1,2* 1School of Engineering, Westlake University, Hangzhou, Zhejiang 310030, China *e-mail: jinyaochu@westlake.edu.cn

2Institute of Advanced Technology, Westlake Institute for Advanced Study, Hangzhou, Zhejiang 310024, China

### Abstract

The potential of AI researchers in scientific discovery remains largely to be unleashed. Over the past decade, the presence of AI for Science (AI4Science) in the 145 Nature Index journals has increased ninefold, yet nearly 90% of AI4Science research remains predominantly led by experimental scientists. Drawing on the Diffusion of Innovation theory, we project that AI4Science's share of total publications will rise from 3.57% in 2024 to approximately 25% by 2050. Unlocking the potential of AI researchers is essential for driving this shift and fostering deeper integration of AI expertise into the research ecosystem. To this end, we propose structured and actionable workflows, alongside key strategies to position AI researchers at the forefront of scientific discovery. Furthermore, we outline three pivotal pathways: equipping experimental scientists with user-friendly AI tools to amplify the impact of AI researchers, bridging cognitive and methodological gaps to enable more direct participation in scientific discovery, and proactively cultivating a thriving AI-driven scientific ecosystem. By addressing these challenges, this work aims to empower AI researchers as a driving force in shaping the future of scientific discovery.

### 1. Introduction

Over the past decade, AI has become a powerful catalyst for scientific discovery1–3. Since 2015, its adoption and impact have expanded rapidly across scientific disciplines, driving unprecedented growth4. This surge has fueled the emergence of AI for Science (AI4Science), a field that leverages machine learning techniques to tackle complex data challenges and uncover insights that were previously beyond reach. The impact of AI4Science is exemplified by the success of deep learning models in structural biology, chemistry, and biomedical research. For instance, AlphaFold5 and ESMFold6 have revolutionized protein structure prediction, dramatically improving the accuracy and efficiency of computational modeling compared to traditional physics-based methods. Similarly, in molecular representation learning, models like MolCLR7 leverage contrastive learning to enhance the predictive power of molecular property predictions, facilitating drug discovery and materials science applications. Beyond structural and molecular biology, AI, especially large language model (LLM), has also demonstrated remarkable utility in biomedical data analysis. GPTCelltype8, an R package utilizing GPT-4, automates accurate cell type annotation from single-cell RNA sequencing data, greatly reducing the effort and expertise needed for this task. PathCha9, a vision-language AI assistant tailored for human pathology, excels in diagnostic accuracy and user preference by integrating a specialized vision encoder with a pretrained LLM. AI has been recognized as a transformative technology and powerful paradigm

in various scientific fields3, such as health and medicine10, materials11, biology12, chemistry13, and the environment14.

Transformative technologies have periodically reshaped scientific discovery. Computational modeling and numerical simulation, such as density functional theory15, revolutionized research in physics, chemistry, and engineering by enabling large-scale predictive simulations. The 1990s brought high-throughput experimental techniques like next-generation sequencing16 and mass spectrometry17, shifting biological science toward data-driven exploration. The early 2000s saw the rise of statistical learning and data science18, enhancing pattern recognition and predictive modeling across disciplines. As AI continues to reshape scientific discovery, it is essential to assess both the scope of its contributions and the challenges that remain. Moreover, “i sensed anxiety and frustration at NeurIPS’24,” remarked Kyunghyun Cho19, receiving great attention and reflecting on the intense competition in AI research. Doctoral candidates nearing graduation and early-career AI researchers face an increasingly challenging academic and industrial landscape and struggle to secure positions due to the rapid saturation of talent in core AI fields. To ensure the long-term sustainability of the AI talent pipeline, it is crucial to broaden the application of AI across diverse fields. AI has already demonstrated significant value in accelerating scientific discovery. This article explores two fundamental questions: To what extent has AI advanced scientific discovery, and what potential remains for further expansion and innovation? Additionally, what gaps still exist in the engagement of AI researchers with scientific discovery, and how can these be bridged?

To answer these questions, this research examines AI-related research papers published in leading natural and health science journals over the past decade. By analyzing these publications and their author affiliations, we aim to understand the current progress of AI4Science within high-impact research and identify pathways for AI researchers to engage in this field. Furthermore, we offer practical guidance and a structured workflow to support AI researchers in embarking on scientific discovery. By highlighting key entry points and methodological approaches, we aim to lower the barriers for AI researchers seeking to contribute to scientific advancements. Ultimately, we hope this survey serves as both an inspiration and a resource, facilitating broader integration of AI into scientific discovery while simultaneously expanding the frontiers of human knowledge, fostering mutual benefits for both AI researchers and the broader scientific community.

### 2. Results and discussion

##### 2.1 AI4Science: An exponentially growing but minor component of scientific discovery

The Nature Index journals, selected by a panel of active scientists based on their reputation and impact, have long served as a key venue for groundbreaking scientific discoveries. To assess the role of AI in high-impact scientific research, we compiled a dataset of 20,401 AI-related research articles published in these 145 journals over the past decade using the Web of Science Core Collection. Our analysis reveals a striking trend: the number of AI-related articles exhibits an exponential increase over the last ten years, with both the absolute number and proportion rising across 145 Nature Index journals (Fig.1A and Fig. S1).

![image 1](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile1.png)

![image 2](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile2.png)

![image 3](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile3.png)

![image 4](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile4.png)

![image 5](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile5.png)

![image 6](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile6.png)

![image 7](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile7.png)

![image 8](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile8.png)

![image 9](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile9.png)

![image 10](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile10.png)

![image 11](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile11.png)

![image 12](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile12.png)

![image 13](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile13.png)

![image 14](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile14.png)

![image 15](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile15.png)

![image 16](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile16.png)

![image 17](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile17.png)

![image 18](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile18.png)

![image 19](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile19.png)

![image 20](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile20.png)

![image 21](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile21.png)

![image 22](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile22.png)

![image 23](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile23.png)

![image 24](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile24.png)

![image 25](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile25.png)

![image 26](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile26.png)

![image 27](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile27.png)

![image 28](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile28.png)

###### Fig. 1 Publication and projected growth trends of AI-related research articles in 145 Nature Indexjournals. (A) Publication trends of 20,401 AI-related research articles in Nature Index journals

(2015–2024). Publication proportions are shown in Fig. S1. (B) Projected growth trend of AIrelated research in Nature Index journals with logistic growth model.

The growth in AI-related research is especially evident in recent years, with the number of such articles in 2024 being nine times higher than in 2015, and the relative proportion of AI-related articles has also surged, reaching 7.8 times the level observed in 2015. This significant rise highlights the escalating adoption of AI methodologies across various scientific disciplines. Notably, 16 journals each published over 100 AI-related articles in 2024 alone, indicating a broad integration of AI. Furthermore, 22 journals had more than 5% of their total publications focused on AI, with four surpassing 10%. Among these, Nature Methods stands out, where AI-related articles comprised 18.78% of its total output in 2024, reflecting the pivotal role of AI in advancing specific fields. However, they still represent only 3.57% of total publications, indicating that AI is still in the early stages of widespread adoption in science.

The Diffusion of Innovation theory20, developed by Everett Rogers, describes how new ideas and technologies spread through a population over time. It posits that adoption follows an S-curve, with innovations initially embraced by a small group of innovators and early adopters, followed by the early majority, late majority, and finally laggards. Based on this pattern, we anticipate that AI-related research will continue to grow rapidly over the next few decades, with its expansion gradually slowing as it reaches maturity (Fig. 1B). As the innovation matures, its adoption rate increases rapidly, then slows as it becomes widely accepted and integrated into everyday practices. AI’s application in scientific discovery is likely following a similar pattern. Early adopters in fields like computational biology, materials science, and data-driven research have led the charge, demonstrating the transformative potential of AI. As more researchers integrate AI into their work and the technology becomes more accessible, adoption will spread to the early majority and late majority, solidifying its place as a central tool in scientific research. By 2050, we project that AIrelated research will stabilize at around 25% of the total Nature Index journal publications, reflecting AI's fully integrated role in modern research.

##### 2.2 Experimental scientists lead AI4Science research

To elucidate the roles of AI researchers in the current AI4Science wave, we analyzed 80,945 author affiliations from 20,401 AI-related articles. These affiliations were categorized as belonging to AI institution, Science institution, or Unclear institution (those not clearly affiliated with either AI or Science) using a pretrained LLM. The trends in author affiliations across these 20,401 AI-related research articles from 2015 to 2024 are illustrated in Fig. 2.

AI institutions are increasingly involved in the frontlines of scientific discovery, but they largely remain in a supporting role despite their growing importance. The average number of AI institutions per paper increases from 0.19 in 2015 to 0.46 in 2024 (a 1.38-fold increase, Fig. 2A). Meanwhile, the average number of institutions per research article and the number of scientific institutions remain relatively stable, with a decline between 2018 and 2022, followed by a slight upward trend in recent years. The proportion of papers with AI institutions as an author affiliation rises from 14.41% to 28.66% (a 0.99-fold increase, Fig. 2B). The average ranking of AI institutions appearing first among author affiliations improves from 7.24 in the first three years to 4.27 in the last seven years. AI-led scientific research increases from 3.13% in 2015 to an average of 8.37% in the past two years (a 1.67-fold increase, Fig. 2C). However, scientific institutions continue to dominate AI-driven scientific discovery, with the average ranking of the first-listed scientific institution hovering around 1.1, slightly shifting from 1.1 in the first three years to 1.13 in the recent two years (Fig. 2D).

![image 29](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile29.png)

![image 30](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile30.png)

- Fig. 2 Trends in author affiliations of 20,401 AI-related research articles (2015–2024). (A)


- Number of institutions per article by institution type. (B) Number and proportion of articles involving AI-related institutions. (C) Number and proportion of articles with AI-related


- institutions as the first affiliation. (D) Rank of the first-affiliated AI and Science institution. The shaded area represents the 95% confidence interval.


Recognizing that most of these journals may not be as familiar to AI researchers, we have also conducted analysis on their participation in five well-known interdisciplinary journals that are also familiar within the AI research community, including Nature, Nature Communications, Science, Science Advances, and PNAS. The five journals contribute 4,773 articles out of a total of 20,401 articles, accounting for 23.4% of the overall publications. This trend is unsurprising, as AI researchers are more actively engaged in these interdisciplinary journals compared to the broader Nature Index journals. In 2015, the average number of AI-affiliated institutions per article, the proportion of articles involving AI institutions, and the percentage of articles with AI institutions

- as the first affiliation were all twice as high as the average for Nature Index journals (Fig. S2). By 2024, AI institutions were involved in 40% of published articles, but only 14.6% of articles listing an AI institution as the first affiliation. Furthermore, after 2022, AI institutions' participation reached a plateau, suggesting a stabilization phase in their contribution to these journals. This stagnation may indicate that AI’s integration into specific scientific fields has transitioned from a phase of rapid expansion to one of consolidation.


##### 2.3 Unlocking the potential of AI researchers in scientific discovery: Three key directions

AI has and will continue to accelerate the process of scientific discovery. While experimental scientists are increasingly leveraging AI tools in their research, the full potential of AI researchers in driving scientific breakthroughs remains largely untapped (Fig. 2). Achieving the projected growth from 3.57% to 25% in AI-driven scientific contributions will require the active and extensive involvement of AI researchers. We identify three key directions—both ongoing and yet to be fully defined—that are essential to realizing this transformation, as illustrated in Figure 3.

![image 31](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile31.png)

![image 32](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile32.png)

![image 33](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile33.png)

![image 34](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile34.png)

![image 35](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile35.png)

![image 36](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile36.png)

- Fig. 3 Schematic representation of three key strategies for unlocking the potential of AI researchers in scientific discovery: (1) equipping experimental scientists with user-friendly AI tools, (2) enabling AI researchers to take a more direct and active role in scientific discovery, and (3) fostering a thriving AI-driven scientific ecosystem to sustain long-term innovation.


Developing user-friendly AI tools for scientific discovery presents a significant opportunity for AI researchers, enhancing both the impact and practical value of their work. Moreover, such advancements hold the potential to bridge the gap between AI technology and real-world applications, facilitating the transition from research to tangible products. Equipping experimental scientists with AI tools—such as data collection21, modeling and analysis22, and experiment design and conduction23—will accelerate the discovery process across a range of scientific fields. In fact, early adopters among experimental scientists have already begun utilizing AI tools in their research. As shown in Fig. 2B and Fig. 2C, currently, 70% of AI-related articles are independently authored by experimental scientists, and they also lead the majority of collaborative research efforts. The next key step in advancing the application of AI is the development of more user-friendly tools and platforms, which will be discussed in Section 2.4. This is crucial for further driving the adoption of AI among experimental scientists.

The success of AI4Science hinges not only on experimental scientists adopting AI tools but also on the development of proactive AI researchers who are deeply embedded in scientific discovery. These researchers will bridge the gap between AI and domain-specific knowledge, developing novel AI algorithms and models tailored to specific scientific challenges, thus driving the next generation of AI-powered discoveries. The proportion of AI researchers leading AI-assisted scientific discoveries has increased from approximately 3% in 2015 to around 8% in the past three years (Fig. 2C). However, it is also observed that the rate of increase has stagnated in recent years, and the overall number remains relatively small. We attribute this limitation to two main gaps: a

cognitive gap (regarding what scientific discoveries AI can be applied to) and a methodological gap (in terms of the workflow in which AI researchers lead scientific discoveries). Discussions on bridging these gaps will be presented in Section 2.5 and Section 2.6, respectively.

Collaboration is a key driver of AI4Science research, and this collaboration extends beyond individual studies to a broader research ecosystem. A quintessential example of this is the SHapley Additive exPlanations (SHAP)24,25, a model interpretation method, initially proposed by AI researchers and widely adopted across various scientific disciplines. For instance, SHAP has been used to quantify the contributions of individual metabolites to disease risk, identifying key metabolites influencing the risk of 24 investigated diseases26. It has also been applied to interpret nanomaterial-plant-environment interactions, providing insights into the factors affecting the root uptake of metal-oxide nanoparticles and their interactions within the soil27. Additionally, SHAP was employed to analyze the contributions of raw ingredients and their interactions, offering valuable insights into the factors influencing the compressive strength of alkali-activated materials28. This is also facilitated by the development of an easily accessible package by the authors (https://shap.readthedocs.io/), which can be considered a key factor in enabling the widespread use of AI tools by experimental scientists. Another reason is that, for experimental scientists, model explanation is often more important than marginal improvements in model performance, as it enables the extraction of hypotheses that can inform subsequent research. Such an ecosystem would significantly accelerate the progress of AI4Science, creating a fertile ground for innovation and driving advancements in scientific discovery. Moreover, the establishment of standards and best practices in AI implementation across scientific discovery will ensure reproducibility, transparency, and broader adoption.

##### 2.4 Four approaches to equipping experimental scientists with AI

AI will not replace scientists because scientific discovery requires human intuition, creativity, and the ability to navigate uncertainty—capabilities that AI lacks29,30. However, scientists who leverage AI can process vast amounts of data, automate complex analyses, and generate insights more efficiently, giving them a significant advantage in accelerating breakthroughs and expanding the frontiers of knowledge31,32. Here, we discuss four key approaches—both established and emerging—that enable researchers to harness AI effectively, lowering barriers to adoption while accelerating scientific discovery (Fig. 4). These approaches not only illustrate how experimental scientists can harness AI tools but also present significant opportunities for AI and software researchers. Building user-friendly platforms of this kind, akin to existing statistical analysis software but enhanced with AI capabilities, can bridge the gap between advanced machine learning and practical scientific applications, enabling broader adoption and innovation.

![image 37](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile37.png)

![image 38](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile38.png)

![image 39](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile39.png)

![image 40](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile40.png)

![image 41](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile41.png)

![image 42](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile42.png)

![image 43](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile43.png)

- Fig. 4 Schematic diagram of four approaches to equipping experimental scientists with AI. (A) User-friendly platforms facilitate modeling and explanation when researchers have access to sufficient data available. (B) Domain-enhanced LLMs enable zero-shot and few-shot inference in data-scarce scenarios. (C) The integration of LLMs, multimodal systems, and multi-task frameworks makes automated data extraction from literature increasingly feasible. (D) Advances in LLMs and robotics are driving the development of autonomous experimental platforms, freeing researchers from labor-intensive experiments.


User-friendly AI platforms can streamline data-driven research by automating model selection, training, and model explanation (Fig. 4A). Scientists provide raw data, specify prediction targets, and define constraints such as time and computational resources. The platform then constructs an appropriate model, performs analysis, and generates an explainable report. Model explanation and the resulting reports are critical components as they directly contribute to scientific understanding, which is one of the primary objectives of scientific research33. Besides, many scientific fields lack sufficient experimental data, yet AI can still provide meaningful insights by integrating domain knowledge with LLMs (Fig. 4B). Researchers can input relevant prompts and background information into a platform, which then constructs a domain-specific vector database. By leveraging retrieval-augmented inference, the system generates predictions in zero- or few-shot learning scenarios. This approach enables scientists to explore hypotheses and obtain preliminary insights even in data-scarce environments. In fact, experimental scientists are increasingly adept

- at using AI-driven methods to tackle both data-rich34,35 and data-scarce36,37 scientific problems. User-friendly platforms will further accelerate this process by making these tools more accessible, encouraging broader adoption among scientists, and ultimately empowering AI to play a larger role in driving scientific discovery.


Data is essential for driving machine learning advancements in scientific discovery, as its quality and quantity directly influence the accuracy and reliability of predictions38. A vast amount of historical data is embedded in published literature, with an ever-growing volume emerging in scientific journal articles. However, its unstructured format, including both natural language text and figures, presents significant obstacles for immediate use by modern informatics systems that rely on structured datasets39. Therefore, the extraction of usable data from these articles is crucial for AI-assisted scientific discovery. While LLMs have advanced the way data is extracted from

literature40, their ability to extract complex text data remains limited. Additionally, their capacity to collect data from images and related research documents, such as supplementary tables, is still underdeveloped. However, with the development of more powerful LLMs, especially those finetuned specifically for data extraction41, and the rise of multimodal LLMs, we anticipate a significant enhancement in data extraction capabilities. Researchers specify target articles and parameters of interest, and the platform retrieves, preprocesses, and extracts relevant information using LLMs (Fig. 4C). The resulting dataset is automatically curated and formatted, accelerating the process of literature-based data collection and synthesis. This approach facilitates metaanalyses, comparative studies, and data-driven hypothesis generation by efficiently aggregating knowledge from published research. Furthermore, AI can further revolutionize scientific experimentation by autonomously designing and executing experiments (Fig. 4D). Researchers define hypotheses, control variables, and desired outputs, while an AI-powered platformenhanced by knowledge-augmented reasoning—develops an optimized experimental plan. Robotics then execute the experiments, and a validation module assesses the reliability and quality of the data. Although AI- and robot-driven automated laboratories are still in their early stages, initial applications have already emerged42,43, demonstrating remarkable potential to transform scientific research44. This approach minimizes manual labor, increases reproducibility, and enables high-throughput hypothesis testing, ultimately accelerating scientific progress.

##### 2.5 Scientific domain "ocean" with AI application potential

AI offers immense potential in scientific discovery, yet many opportunities remain underexplored by AI researchers. Currently, the application of AI in science is largely concentrated in fields with abundant structured datasets, such as foundational life sciences and medical research. Prominent examples include protein structure and function prediction, single-cell annotation, and drug discovery (Fig. 5A). The success of AI in these areas is largely driven by the availability of wellcurated, large-scale datasets and clearly defined machine learning tasks. However, scientific discovery extends far beyond these domains, and numerous critical challenges in other fields remain largely untapped by AI researchers.

![image 44](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile44.png)

![image 45](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile45.png)

![image 46](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile46.png)

![image 47](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile47.png)

![image 48](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile48.png)

![image 49](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile49.png)

![image 50](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile50.png)

- Fig. 5 Research areas with high AI involvement and strong application potential. (A) Hot topics in AI-driven scientific research. (B) Scientific domain "ocean" with AI application potential. (C) High-frequency non-AI terms in the titles and abstracts of 20,401 AI-related research articles. AIrelated high-frequency terms are shown in Fig. S3.


Beyond life sciences, AI holds transformative potential in broader scientific domains such as materials design, material-biology-environment interactions, biosynthesis and chemical synthesis, environmental assessment and remediation, climate prediction, and industrial process optimization (Fig. 5B). These areas pose complex, multidimensional problems that require AI-driven approaches for data integration, modeling, prediction, and explanation. Despite their importance, these domains have not received comparable attention from the AI research community, often due to the lack of easily accessible datasets or the need for specialized domain knowledge to frame AIdriven solutions effectively.

To map the current landscape of AI-driven scientific discovery, we analyzed the titles and abstracts of 20,401 AI-related research articles published in high-impact scientific journals. By identifying high-frequency scientific entities (Fig. 5C), we highlight the fields where AI is already being employed by experimental scientists to address fundamental research questions. AI researchers can expand their impact by developing advanced algorithms tailored to complex, unstructured scientific data. Additionally, AI-driven approaches to data acquisition, experimental design, and real-time analysis can accelerate discovery by optimizing research workflows.

##### 2.6 AI4Science workflow for AI researchers: From tool providers to key contributors

There are many AI4Science workflows for scientific discovery in various fields, such as proteomics45, materials34, biomedicine46, and medical imaging47, but most are designed for researchers in specific fields rather than AI researchers. We propose an AI4Science workflow for AI researchers (Fig. 6). The first and most crucial step is to identify suitable scientific problems, which can be guided by the researchers' interests, experience, and available resources. Areas where AI has already been applied may be a good starting point (Fig. 5C), as experimental scientists may have used basic machine learning methods to address such problems. Advanced algorithms and analytical techniques could revolutionize research in these specific fields. Besides, LLM has been used to generate novel scientific ideas48 and scientific hypotheses49. AI researchers can also draw on the strengths of their higher-level institutions, providing a great platform for communication and collaboration.

Understanding the chosen scientific domain is a prerequisite for conducting efficient research, and with the development of LLMs-based agents50, this will become easier. Overall, AI plays three main roles across different fields: prediction, comprehension, and innovation (discovery or design). These roles are logically connected. For example, in the case of proteins, one can first predict the structure or functional annotation of a protein51, then understand the relationship between the sequence or structure and function52, and finally, based on this understanding, design new proteins to achieve specific functions53. In data-rich fields, one can skip the understanding step, but in many cases, understanding is closely tied to scientific discovery.

![image 51](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile51.png)

![image 52](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile52.png)

![image 53](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile53.png)

![image 54](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile54.png)

![image 55](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile55.png)

![image 56](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile56.png)

![image 57](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile57.png)

![image 58](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile58.png)

- Fig. 6 AI4Science workflow for AI researchers.


Formal experiments can generally be divided into three steps: data collection, modeling and analysis, and experimental validation. For AI researchers, we do not recommend collecting data through experiments or simulations, as this increases the difficulty of conducting research. Instead, we suggest focusing on fields with available datasets or those where data can be gathered from literature. In data-rich fields, the competition is more intense. For many fields, there is a lack of publicly available high-quality data, and extracting data from literature can be an effective way to enhance competitiveness. Existing LLM and AI tools54,55 also make data collection from literature easier. Modeling and analysis are areas AI researchers are familiar with, so we will not elaborate further, but we emphasize the importance of model explanation and causal inference. Because

scientific understanding is one of the main aims of science33. Finally, we recommend experimental validation of the results obtained through computational methods. Many experiments have standardized procedures, and collaborating with other labs, shared experimental platforms, or commercialized research service institutions can help complete this step. Furthermore, the advancement of automated laboratories powered by LLMs and robotics is set to streamline experimental validation44,56, making it as accessible as the use of AI tools by experimental scientists.

### 3. Conclusion

AI4Science has seen rapid growth over the past decade, yet its full potential remains untapped, particularly the contributions of AI researchers themselves. While AI is increasingly integrated into scientific research, its application is still largely driven by experimental scientists, with AI researchers often playing a secondary or supportive role. This imbalance limits the depth of AI’s impact on scientific discovery. To accelerate progress, this work highlights the need to unlock the expertise of AI researchers, positioning them as active contributors rather than just tool developers. By fostering deeper collaboration and bridging cognitive and methodological gaps, AI researchers can drive more transformative advancements and reshape the landscape of scientific discovery. Looking ahead, the future of AI4Science depends on a well-defined human-AI collaboration paradigm—one that leverages AI’s analytical power while ensuring human researchers remain in control of scientific reasoning and validation. Addressing challenges such as AI hallucinations and setting clear boundaries for AI applications will be essential. Moreover, experimental validation stands as the ultimate safeguard of AI-driven discoveries across most disciplines, upholding scientific rigor. With these strategic shifts, AI4Science can expand from its current 3.57% share of publications to 25% by 2050, unlocking unprecedented opportunities for scientific discovery.

### 4. Methods

##### 4.1 Data collection

AI-related research articles published in 145 Nature Index journals over the past decade were retrieved from the Web of Science Core Collection. The search query used was [SO="Journal name" AND PY=2015-2024 AND DT=Article AND TS=("machine learning" OR "deep learning" OR "artificial intelligence" OR AI OR "neural network" OR "language model" OR "reinforcement learning" OR "transfer learning" OR "ensemble learning" OR "random forest" OR "decision tree" OR "foundation model" OR "tree-based model" OR "data-driven" OR "computational modeling" OR "high-throughput screening" OR "Bayesian method" OR "Bayesian modeling" OR "Bayesian learning")], which yielded a total of 20,401 AI-related research articles. The retrieved data included information such as titles, abstracts, publication years, author affiliations, and journal names. To obtain the total number of research articles published in these journals during the same period, we used the search query (SO="Journal name" AND PY=2015-2024 AND DT=Article).

##### 4.2 Author affiliation classification

To classify author affiliations, we employed prompt engineering to interact with the mixture-ofexperts language model DeepSeek-V3 API 57 for entity recognition. To enhance classification accuracy, we incorporated a self-reflection mechanism that iteratively refines the categorization. The author affiliations were classified into three categories: institutions primarily focused on AI, informatics, or data-driven research were categorized as "AI institutions," while those dedicated to natural sciences, health sciences, or non-AI engineering disciplines were classified as "science

institutions." Affiliations that did not clearly fit into these categories or exhibited overlap, such as advanced research institutes or schools of engineering, were categorized as "unclear institutions."

##### 4.3 Scientific entity recognition

For scientific entity recognition, we deployed a distilled inference model via reinforcement learning, DeepSeek-R1-Distill-Llama-8B 58, which was fine-tuned on a Llama 8B model. This model was used to extract entities from the titles and abstracts of research articles. Entities were identified through reasoning-based outputs, with the extraction process utilizing regular expressions (re) to parse the reasoning results. In cases where the initial extraction did not meet standards—such as inaccurate entity delimiters, excessive or insufficient character counts, or entities not beginning with a letter—multiple re-extraction attempts were made. Additionally, similar scientific entities were merged using semantic judgment rules to ensure consistency.

##### 4.4 Scientific entity classification and word cloud plotting

For better visualization, we employed prompt engineering with the Llama-3.1-8B-Instruct model 59 to classify the extracted entities into two categories: AI-related entities (including models, architectures, algorithms, methods, and evaluation metrics) and non-AI-related entities. The highfrequency terms were subject to minor manual adjustments, including the merging of obvious synonyms and standardization of capitalization, to enhance clarity and consistency in the visualization. After classification, we utilized the wordcloud package to visualize the highfrequency terms, providing a clear representation of the most commonly mentioned entities in the dataset.

### Acknowledgements

This work is supported by International Collaboration Fund for Creative Research of National Science Foundation of China (NSFC ICFCRT) under the Grant No. W2441019, Westlake Education Foundation under the Grant No. 103110846022301, and China Postdoctoral Science Foundation under the Grant No. 2024M762941.

### Author contributions

H.Y. and Y.J. designed research and wrote the paper. H.Y. performed research.

### Competing interests

The authors declare no competing interest.

### References

- 1. Gil, Y., Greaves, M., Hendler, J. & Hirsh, H. Amplify scientific discovery with artificial intelligence. Science 346, 171–172 (2014).
- 2. Wang, H. et al. Scientific discovery in the age of artificial intelligence. Nature 620, 47–60

(2023).

- 3. Xu, Y. et al. Artificial intelligence: A powerful paradigm for scientific research. The Innovation 2, 100179 (2021).


- 4. Gao, J. & Wang, D. Quantifying the use and potential benefits of artificial intelligence in scientific research. Nat Hum Behav 8, 2281–2292 (2024).
- 5. Jumper, J. et al. Highly accurate protein structure prediction with AlphaFold. Nature 596, 583– 589 (2021).
- 6. Lin, Z. et al. Evolutionary-scale prediction of atomic-level protein structure with a language model. Science 379, 1123–1130 (2023).
- 7. Wang, Y., Wang, J., Cao, Z. & Barati Farimani, A. Molecular contrastive learning of representations via graph neural networks. Nat Mach Intell 4, 279–287 (2022).
- 8. Hou, W. & Ji, Z. Assessing GPT-4 for cell type annotation in single-cell RNA-seq analysis. Nat Methods 21, 1462–1465 (2024).
- 9. Lu, M. Y. et al. A multimodal generative AI copilot for human pathology. Nature 634, 466– 473 (2024).
- 10. Rajpurkar, P., Chen, E., Banerjee, O. & Topol, E. J. AI in health and medicine. Nat Med 28, 31–38 (2022).
- 11. Choudhary, K. et al. Recent advances and applications of deep learning methods in materials science. npj Comput Mater 8, 59 (2022).
- 12. Angermueller, C., Pärnamaa, T., Parts, L. & Stegle, O. Deep learning for computational biology. Molecular Systems Biology 12, 878 (2016).
- 13. Baum, Z. J. et al. Artificial Intelligence in Chemistry: Current Trends and Future Directions. J. Chem. Inf. Model. 61, 3197–3212 (2021).
- 14.Konya, A. & Nematzadeh, P. Recent applications of AI to environmental disciplines: A review. Science of The Total Environment 906, 167705 (2024).
- 15. Huang, B., Von Rudorff, G. F. & Von Lilienfeld, O. A. The central role of density functional theory in the AI age. Science 381, 170–175 (2023).
- 16. Satam, H. et al. Next-Generation Sequencing Technology: Current Trends and Advancements. Biology 12, 997 (2023).
- 17. Heuckeroth, S. et al. Reproducible mass spectrometry data processing and compound annotation in MZmine 3. Nat Protoc 19, 2597–2641 (2024).
- 18. Edfeldt, K. et al. A data science roadmap for open science organizations engaged in earlystage drug discovery. Nat Commun 15, 5640 (2024).
- 19. Cho, K. I sensed anxiety and frustration at NeurIPS’24. https://kyunghyuncho.me/i-sensedanxiety-and-frustration-at-neurips24/ (2024).
- 20. Rogers, E. M., Singhal, A. & Quinlan, M. M. Diffusion of innovations. in An integrated approach to communication theory and research 432–448 (Routledge, 2014).
- 21. Polak, M. P. & Morgan, D. Extracting accurate materials data from research papers with conversational language models and prompt engineering. Nat Commun 15, 1569 (2024).
- 22. Krenn, M. et al. On scientific understanding with artificial intelligence. Nat Rev Phys 4, 761– 769 (2022).
- 23. Gottweis, J. et al. Towards an AI co-scientist. Preprint at https://doi.org/10.48550/ARXIV.2502.18864 (2025).
- 24. Lundberg, S. & Lee, S.-I. A Unified Approach to Interpreting Model Predictions. Preprint at https://doi.org/10.48550/ARXIV.1705.07874 (2017).
- 25. Lundberg, S. M. et al. From local explanations to global understanding with explainable AI for trees. Nat Mach Intell 2, 56–67 (2020).
- 26. Buergel, T. et al. Metabolomic profiles predict individual multidisease outcomes. Nat Med 28, 2309–2320 (2022).
- 27. Yu, H., Zhao, Z., Luo, D. & Cheng, F. Interpretable machine learning for investigating complex nanomaterial–plant–soil interactions. Environ. Sci.: Nano 9, 4305–4316 (2022).


- 28. Zheng, X. et al. A data-driven approach to predict the compressive strength of alkali-activated materials and correlation of influencing parameters using SHapley Additive exPlanations (SHAP) analysis. Journal of Materials Research and Technology 25, 4074–4093 (2023).
- 29. Makarov, V. A., Stouch, T., Allgood, B., Willis, C. D. & Lynch, N. Best practices for artificial intelligence in life sciences research. Drug Discovery Today 26, 1107–1110 (2021).
- 30. Messeri, L. & Crockett, M. J. Artificial intelligence and illusions of understanding in scientific research. Nature 627, 49–58 (2024).
- 31. Oviedo, F., Ferres, J. L., Buonassisi, T. & Butler, K. T. Interpretable and Explainable Machine Learning for Materials Science and Chemistry. Acc. Mater. Res. 3, 597–607 (2022).
- 32. Kapoor, S. et al. REFORMS: Consensus-based Recommendations for Machine-learningbased Science. Sci. Adv. 10, eadk3452 (2024).
- 33. Krenn, M. et al. On scientific understanding with artificial intelligence. Nat Rev Phys 4, 761– 769 (2022).
- 34. Pyzer-Knapp, E. O. et al. Accelerating materials discovery using artificial intelligence, high performance computing and robotics. npj Comput Mater 8, 84 (2022).
- 35. Wong, F. et al. Discovery of a structural class of antibiotics with explainable deep learning. Nature 626, 177–185 (2024).
- 36.Chen, Z. et al. ProBID-Net: a deep learning model for protein–protein binding interface design. Chem. Sci. 15, 19977–19990 (2024).
- 37. Liu, S., Wen, T., Pattamatta, A. S. L. S. & Srolovitz, D. J. A prompt-engineered large language model, deep learning workflow for materials classification. Materials Today 80, 240–249

(2024).

- 38. Liu, Y. et al. Data quantity governance for machine learning in materials science. National Science Review 10, nwad125 (2023).
- 39. Gupta, S., Mahmood, A., Shetty, P., Adeboye, A. & Ramprasad, R. Data extraction from polymer literature using large language models. Commun Mater 5, 269 (2024).
- 40. Polak, M. P. et al. Flexible, model-agnostic method for materials data extraction from text using general purpose language models. Digital Discovery 3, 1221–1235 (2024).
- 41. Ai, Q., Meng, F., Shi, J., Pelkie, B. & Coley, C. W. Extracting structured data from organic synthesis procedures using a fine-tuned large language model. Digital Discovery 3, 1822–1831

(2024).

- 42. Szymanski, N. J. et al. An autonomous laboratory for the accelerated synthesis of novel materials. Nature 624, 86–91 (2023).
- 43. Angello, N. H. et al. Closed-loop transfer enables artificial intelligence to yield chemical knowledge. Nature 633, 351–358 (2024).
- 44. Angelopoulos, A., Cahoon, J. F. & Alterovitz, R. Transforming science labs into automated factories of discovery. Science Robotics 9, eadm6991.
- 45. Mann, M., Kumar, C., Zeng, W.-F. & Strauss, M. T. Artificial intelligence for proteomics and biomarker discovery. Cell Systems 12, 759–770 (2021).
- 46. Gao, S. et al. Empowering biomedical discovery with AI agents. Cell 187, 6125–6151 (2024).
- 47. Najjar, R. Redefining Radiology: A Review of Artificial Intelligence Integration in Medical Imaging. Diagnostics 13, 2760 (2023).
- 48. Hu, X. et al. Nova: An Iterative Planning and Search Approach to Enhance Novelty and Diversity of LLM Generated Ideas. Preprint at https://doi.org/10.48550/ARXIV.2410.14255

(2024).

- 49. Yang, Z. et al. MOOSE-Chem: Large Language Models for Rediscovering Unseen Chemistry Scientific Hypotheses. Preprint at https://doi.org/10.48550/ARXIV.2410.07076 (2024).
- 50. Schmidgall, S. et al. Agent Laboratory: Using LLM Agents as Research Assistants. Preprint at https://doi.org/10.48550/ARXIV.2501.04227 (2025).


- 51. Gligorijević, V. et al. Structure-based protein function prediction using graph convolutional networks. Nat Commun 12, 3168 (2021).
- 52. Wang, W., Shuai, Y., Zeng, M., Fan, W. & Li, M. DPFunc: accurately predicting protein function via deep learning with domain-guided structure information. Nat Commun 16, 70

(2025).

- 53. Jiang, Y. et al. PocketFlow is a data-and-knowledge-driven structure-based molecular generative model. Nat Mach Intell 6, 326–337 (2024).
- 54. Ansari, M. & Moosavi, S. M. Agent-based learning of materials datasets from the scientific literature. Digital Discovery 3, 2607–2617 (2024).
- 55. Polak, M. P. & Morgan, D. Extracting accurate materials data from research papers with conversational language models and prompt engineering. Nat Commun 15, 1569 (2024).
- 56. M. Bran, A. et al. Augmenting large language models with chemistry tools. Nat Mach Intell 6, 525–535 (2024).
- 57. DeepSeek-AI et al. DeepSeek-V3 Technical Report. Preprint at https://doi.org/10.48550/ARXIV.2412.19437 (2024).
- 58. DeepSeek-AI et al. DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning. Preprint at https://doi.org/10.48550/ARXIV.2501.12948 (2025).
- 59. Grattafiori, A. et al. The Llama 3 Herd of Models. Preprint at https://doi.org/10.48550/ARXIV.2407.21783 (2024).


## Supplemental information

![image 59](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile59.png)

![image 60](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile60.png)

![image 61](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile61.png)

![image 62](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile62.png)

![image 63](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile63.png)

![image 64](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile64.png)

![image 65](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile65.png)

![image 66](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile66.png)

![image 67](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile67.png)

![image 68](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile68.png)

![image 69](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile69.png)

![image 70](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile70.png)

![image 71](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile71.png)

![image 72](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile72.png)

![image 73](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile73.png)

![image 74](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile74.png)

![image 75](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile75.png)

![image 76](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile76.png)

![image 77](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile77.png)

![image 78](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile78.png)

![image 79](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile79.png)

![image 80](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile80.png)

![image 81](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile81.png)

- Fig. S1 Publication ratios of 20,401 AI-related research articles in 145 Nature Index journals (2015–2024).


![image 82](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile82.png)

![image 83](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile83.png)

![image 84](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile84.png)

![image 85](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile85.png)

![image 86](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile86.png)

![image 87](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile87.png)

![image 88](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile88.png)

- Fig. S2 Trends in publication count and author affiliations of 4,773 AI-related research articles published in five well-known multidisciplinary journals (2015–2024), including Nature, Nature Communications, Science, Science Advances, and PNAS. (A) Number of publications by year. (B)


- Number of institutions per article by institution type. (C) Number and proportion of articles involving AI-related institutions. (D) Number and proportion of articles with AI-related


- institutions as the first affiliation. (E) Rank of the first-affiliated AI and Science institution. The shaded area represents the 95% confidence interval.


![image 89](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile89.png)

![image 90](Yu and Jin_2025_Unlocking the Potential of AI Researchers in Scientific Discovery What Is Missing_images/imageFile90.png)

###### Fig. S3 High-frequency AI terms in the titles and abstracts of 20,401 AI-related research articles.

