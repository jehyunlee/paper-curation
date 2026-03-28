## AI for Social Science and Social Science of AI: A Survey

Ruoxi Xua,b, Yingfei Suna, Mengjie Renb, Shiguang Guob, Ruotong Panb, Hongyu Linb,∗, Le Sunb,c and Xianpei Hanb,c

aSchool of Electronic, Electrical and Communication Engineering, University of Chinese Academy of Sciences, Beijing, China bChinese Information Processing Laboratory, Institute of Software, Chinese Academy of Sciences, Beijing, China cState Key Laboratory of Computer Science, Institute of Software, Chinese Academy of Sciences, Beijing, China

##### ARTICLE INFO

##### ABSTRACT

# arXiv:2401.11839v1[cs.CL]22 Jan 2024

Keywords: Social Science Large Language Models AI Simulation

Recent advancements in artificial intelligence, particularly with the emergence of large language models (LLMs), have sparked a rethinking of artificial general intelligence possibilities. The increasing human-like capabilities of AI are also attracting attention in social science research, leading to various studies exploring the combination of these two fields. In this survey, we systematically categorize previous explorations in the combination of AI and social science into two directions that share common technical approaches but differ in their research objectives. The first direction is focused on AI for social science, where AI is utilized as a powerful tool to enhance various stages of social science research. While the second direction is the social science of AI, which examines AI agents as social entities with their human-like cognitive and linguistic capabilities. By conducting a thorough review, particularly on the substantial progress facilitated by recent advancements in large language models, this paper introduces a fresh perspective to reassess the relationship between AI and social science, provides a cohesive framework that allows researchers to understand the distinctions and connections between AI for social science and social science of AI, and also summarized state-of-art experiment simulation platforms to facilitate research in these two directions. We believe that as AI technology continues to advance and intelligent agents find increasing applications in our daily lives, the significance of the combination of AI and social science will become even more prominent.

### 1. Introduction

Building machines that can think, learn and create is the fundamental pursuit of artificial intelligence (AI) (Russell, 2010). How to develop machines with general intelligence comparable to, or even greater than, that of human beings has never lost its appeal (Goertzel, 2014). Recently, significant advancements have been made in the AI field (Zhao, Zhou, Li, Tang, Wang, Hou, Min, Zhang, Zhang, Dong et al., 2023), particularly with the emergence of large language models (LLMs) such as ChatGPT and GPT-4 (OpenAI, 2023). These developments have led to the rethinking of the possibilities of artificial general intelligence (AGI) (Zhao et al., 2023).

The increasing human-like capabilities of AI are also attracting attention in social science research. There have been numerous studies exploring the combination of AI and social science (Bail, 2023; Ziems et al., 2023; Chen, 2023a). Along these lines, many novel research directions have been explored, including research tasks proposing (Park et al., 2023b; Banker et al., 2023), social science simulation (Brand et al., 2023; Kjell et al., 2023; Chu et al., 2023), AI agent governing (Li et al., 2023; Jiang et al., 2023; Miotto et al., 2022) and so on.

Despite the large number of related studies, the existing studies tend to concentrate on one specific instance of AI and social science intersection, thereby lacking a unified perspective to effectively distinguish and outline AI’s role in social science research and its own social characteristics. In reality, the combination of AI and social science can be divided into two distinct directions. On the one hand, the superior performance of AI allows them to serve as effective tools for social science research, such as using AI for literature searching and reviewing (McGee, 2023b), proposing questions and hypotheses (Park et al., 2023b; Banker et al., 2023), analyzing data (Ziems et al., 2023), assisting with writing (Dergaa, Chamari, Zmijewski and Saad, 2023; Chen, 2023b), and more. Systematically outlining the potential applications of AI in different phases of social science research can provide a valuable guide

∗Corresponding author

ruoxi2021@iscas.ac.cn (R. Xu); yfsun@ucas.ac.cn (Y. Sun); renmengjie2021@iscas.ac.cn (M. Ren); guoshiguang2021@iscas.ac.cn (S. Guo); panruotong2021@iscas.ac.cn (R. Pan); hongyu@iscas.ac.cn (H. Lin); sunle@iscas.ac.cn (L. Sun); xianpei@iscas.ac.cn (X. Han)

![image 1](Xu et al._2024_AI for social science and social science of AI A Survey_images/imageFile1.png)

ORCID(s): 0000-0001-8145-6453 (R. Xu)

Aydın and Karaarslan (2022); Haman and Školník (2023) etc.

Literature review

| | |
|---|---|
| | |


Hypothesis generation §3.1

Park, Kaplan, Ren, Hsu, Li, Xu, Li and Li (2023b); Banker, Chatterjee, Mishra and Mishra (2023) etc.

Hypothesis propose

Park, Popowski, Cai, Morris, Liang and Bernstein (2022); Salehi, Hassan, Lammerse, Sabet, Riiser, Røed, Johnson, Thambawita, Hicks, Powell et al. (2022); Horton (2023) etc.

AI for social science §3

Experiment research

Kjell, Kjell and Schwartz (2023); Brand, Israeli and Ngwe (2023); Chu, Andreas, Ansolabehere and Roy (2023) etc.

Hypothesis verification §3.2

Survey research

Ziems, Held, Shaikh, Chen, Zhang and Yang (2023); Gilardi, Alizadeh and Kubli (2023); Lopez-Lira and Tang (2023) etc.

Nonreactive research

| | |
|---|---|
| | |


Psychology

- of AI §4.1

Personality

Li, Li, Joty, Liu, Huang, Qiu and Bing (2023); Jiang, Zhang, Cao, Kabbara and Roy (2023); Miotto, Rossberg and Kleinberg (2022) etc.

Cognition

Chen, Andiappan, Jenkin and Ovchinnikov (2023); Bojic, Stojković and Jolić Marjanović (2023); Dhingra, Singh, SB, Malviya and Gill (2023) etc.

Others

Cai, Haslett, Duan, Wang and Pickering (2023); Pellert, Lechner, Wagner, Rammstedt and Strohmaier (2022); Jin, Levine et al. (2022) etc.

| | |
|---|---|
| | |


Sociology

- of AI §4.2

Social bias

Brown, Mann, Ryder et al. (2020); Lucy and Bamman (2021); Long, Jeff, Xu et al. (2022) etc.

Social behavior

Park, O’Brien, Cai, Morris, Liang and Bernstein (2023a)

| | |
|---|---|
| | |
| | |


Economics

- of AI §4.3


AI and social science

Social science of AI §4

Niszczota and Abbas (2023); Son, Jung, Hahm, Na and Jin (2023); Leippold (2023) etc.

Economic expertise

Aher, Arriaga and Kalai (2023); Guo (2023); Phelps and Russell (2023) etc. Macroeconomics

Microeconomics

King (2023); McGee (2023a); Liu, Jia, Wei, Xu, Wang and Vosoughi (2021) etc.

Politics of AI §4.4

Diamond (2023); Cai et al. (2023); Goli and Singh (2023) etc. Public tools and resources §5

Linguistics of AI §4.5

AgentLab, SkyAGI, AgentVerse etc.

- Figure 1: Overview of the intersection of AI and social science. We have separately discussed "AI for social science" which summarizes the application of AI at every stage of social science research to provide guidance on tool selection for researchers, "social science of AI" which systematically describes the intelligence level and characteristics of AI agents from a social science perspective on different sub-disciplines, and "public tools and resources" which focus on simulation tools. These fields share technical methodologies to some extent, yet they possess distinct research subjects and objectives.


for researchers to choose appropriate research tools. We refer to this direction as AI for social science in this paper. On the other hand, just as early myths and parables emphasized the social and ethical questions around human-created

AI as human surrogates

![image 2](Xu et al._2024_AI for social science and social science of AI A Survey_images/imageFile2.png)

![image 3](Xu et al._2024_AI for social science and social science of AI A Survey_images/imageFile3.png)

![image 4](Xu et al._2024_AI for social science and social science of AI A Survey_images/imageFile4.png)

AI for social science

Act as human

![image 5](Xu et al._2024_AI for social science and social science of AI A Survey_images/imageFile5.png)

![image 6](Xu et al._2024_AI for social science and social science of AI A Survey_images/imageFile6.png)

AI agents

Researcher

Act as itself

![image 7](Xu et al._2024_AI for social science and social science of AI A Survey_images/imageFile7.png)

social science of AI

![image 8](Xu et al._2024_AI for social science and social science of AI A Survey_images/imageFile8.png)

![image 9](Xu et al._2024_AI for social science and social science of AI A Survey_images/imageFile9.png)

AI as AI

- Figure 2: Computer simulation respectively in the context of "AI for social science" and "social science of AI". For “AI for social science”, AI agents are deployed to mimic human behaviors to enhance the understanding of human society. Conversely, "social science of AI" delves into AI agents’ own social questions.


intelligence (McCorduck and Cfe, 2004; Kieval, 1997; Pollin, 1965), today’s intelligent machines present their own interesting social questions (Frank, Wang, Cebrian and Rahwan, 2019) and expanding research starts to explore and understand AI agents as social entities. Particularly, current AI agents, especially large language model agents, are exhibiting cognitive, logical reasoning, and linguistic capabilities on par with or even surpassing those of humans, along with unique behavioral characteristics (OpenAI, 2023). Communities constituted by AI agents also exhibit emergent behaviors similar to human societies (Park et al., 2023a). This provides an interesting case for attempting to extend the social science to more universal phenomena of machines (Klein and Kleinman, 2002) and also presents a valuable opportunity to reevaluate a fundamental axiom in social science: human behavior can be understood as possessing unique social characteristics (Woolgar, 1985). Exploring AI from a social science perspective can also provide crucial insights and guidance to make AI development more congruent with societal needs and human values. We refer to this direction as social science of AI in this paper. There is an important point to note, the term "social science" as used in this paper extend its traditional definition. It is used in a broader sense to provide a research perspective for describing certain high-level behaviors of humans or models, rather than equating it with actual human social behaviors.

Although these directions share common technological approaches, they have distinct research objectives, significance, and scopes of application. For example in Figure 2, using AI agents for simulation serves as a technical method that could apply to both directions, but with differing objectives. When used for the former, the researcher’s aim is to align the behavior of AI agents as closely with human behavior as possible, in order to study the operational laws of human society in a cost-effective, fast, and ethically risk-averse manner (Park et al., 2022; Salehi et al., 2022). When used for the latter, the objective is to explore the behavioral laws of AI itself, with a particular focus on its unique aspects, especially those differing from the operational laws of human society (Guo, 2023). The absence of surveys from the above two perspectives makes it hard to ground each work’s research significance and application scope, hindering us to comprehend and harness the distinctions and connections between these two directions. A joint analysis of their research progress can help to grasp the big picture of the current state of the combination of AI and social science.

To this end, we conduct a comprehensive review from these two directions respectively. We conduct a joint analysis of their research progress, comparing their similarities and differences to present an overview of the current state of the combination of AI and social science. Considering that recent remarkable advancements in this field can be largely attributed to the development of large language models (Zhao et al., 2023), this paper narrows its scope to the combination of large language models and social sciences, approaching the topic from both the angle of AI for social science and the social science of AI. The main organization of this survey is summarized in Figure 1. Specifically, from the angle of AI for social science, we discuss large language models’ potential as a highly efficient tool that can be integrated into existing research methodologies, significantly enhancing the efficiency of social science research. To

achieve this, we structure the content according to the roles that AI plays in both the stages of hypothesis generation and verification within the social science process (Donovan and Hoover, 2013; Bryman, 2016). For hypothesis generation, we mainly focus on how AI can help human beings in literature reviewing and hypothesis proposing. For hypothesis verification stage, we respectively examine how large language models function in various research methods such as experiment research, survey research and non-reactive research. From the perspective of the social science of AI, we are referring to a broad field of social science that focuses on regarding large language models as its research subject. We categorize the behavioral studies of these models according to each subfield within social science, following academic categorization. More specifically, we have compiled the behavioral laws of large language models by examining them from the viewpoints of psychology, sociology, economics, politics, and linguistics. Additionally, we have also compiled a summary of the currently available tools in this field to facilitate research in the aforementioned areas. These platforms utilize large language models as agents and allows for the setting and implementation of intervention conditions to simulate diverse social situations, interactions, and behaviors. They serve the purpose of simulating human behavior for studying human societies, as well as exploring AI societies, thus catering to both of the above directions.

Generally, we summarize our contributions as follows:

- • We present a perspective of revisiting AI and social science combinations from two directions: AI for social science and social science of AI. We elaborate on the connections and distinctions between these two directions, grounding the research value and application scope of relevant work.
- • Based on the substantial progress facilitated by recent advancements in large language models to these two directions, we conduct a literature review, which summarizes the research landscape, discusses the limitations of the existing research, and sheds light on potential future directions in the combination of AI and social science.
- • We collect and compare existing open source large language model-based simulation tools. These platforms can serve an effective foundation to facilitate the future researches of the above-mentioned two directions.


The structure of this survey is organized as follows: Section 3 introduces the application of large language models in social science research, while Section 4 delves into social science research that takes large language models as the subject of study. Section 5 provides information about the resources and tools available. Finally, we conclude the survey in Section 6, summarizing the main findings and discussing the remaining issues for future work.

### 2. Background

Nowadays, the AI community, and even the whole society, is witnessing the significant impacts brought about by large language models. Large language models typically refer to transformer language models that contain hundreds of billions (or more) of parameters (Shanahan, 2022), which are trained on massive text data. Notable examples include

- GPT-3 (Brown et al., 2020), PaLM (Chowdhery, Narang, Devlin, Bosma, Mishra, Roberts, Barham, Chung, Sutton, Gehrmann et al., 2022), LLaMA (Touvron, Lavril, Izacard, Martinet, Lachaux, Lacroix, Rozière, Goyal, Hambro, Azhar, Rodriguez, Joulin, Grave and Lample, 2023) and OpenAI’s ChatGPT, which amassed 100 million users in less than two months, setting a new record in history. These models have exhibited strong capacities to understand natural language and solve complex tasks (via text generation), capturing the attention and imagination of investors, consumers, and organizations.


Improvements in large language models have been so fast, and the potential societal repercussions so profound, that a broad cross-disciplinary lens from computer science and social science is necessary to start making sense of the implications. Firstly, the ability of large language models to generate texts for a broad range of tasks via an intuitive natural language interface may hold great promise for social science research. This has opened up avenues for various applications, including literature searching and reviewing (McGee, 2023b), proposing questions and hypotheses (Park et al., 2023b; Banker et al., 2023), analyzing data (Ziems et al., 2023), assisting with writing (Dergaa et al., 2023; Chen, 2023b), and more. Secondly, the evolution of large language models has significantly enhanced their capacity to exhibit human-like characteristics, leading to a surge in research regarding LMs as representations of human entities (Krishna, Lee, Fei-Fei and Bernstein, 2022; Andreas, 2022; Park et al., 2022). Research includes exploring the collaborative capabilities of large language models in complex tasks (Irving, Christiano and Amodei, 2018), developing "generative agents" to investigate emergent social behaviors (Park et al., 2023a), employing GPT-3-based agents as substitutes for human participants (Aher et al., 2023) and so on. Thirdly, the advancements in large language models have prompted a reconsiderationoftheethicalandsocietalissuesitmayentail.Thesepreviousworkshavehighlightedthetransformative

|![image 10](Xu et al._2024_AI for social science and social science of AI A Survey_images/imageFile10.png)<br><br>Literature Review Hypothesis Propose<br><br>![image 11](Xu et al._2024_AI for social science and social science of AI A Survey_images/imageFile11.png)<br><br>Hypothesis Generation|
|---|


|Hypothesis Verification Experiment Research Survey Research Nonreactive Research<br><br>![image 12](Xu et al._2024_AI for social science and social science of AI A Survey_images/imageFile12.png)<br><br>Experiment Assistant<br><br>![image 13](Xu et al._2024_AI for social science and social science of AI A Survey_images/imageFile13.png)<br><br>Experiment Simulation<br><br>![image 14](Xu et al._2024_AI for social science and social science of AI A Survey_images/imageFile14.png)<br><br>Interviewee Interviewer<br><br>![image 15](Xu et al._2024_AI for social science and social science of AI A Survey_images/imageFile15.png)<br><br>![image 16](Xu et al._2024_AI for social science and social science of AI A Survey_images/imageFile16.png)<br><br>Questionnaire<br><br>Design<br><br>![image 17](Xu et al._2024_AI for social science and social science of AI A Survey_images/imageFile17.png)<br><br>Result Analysis<br><br>![image 18](Xu et al._2024_AI for social science and social science of AI A Survey_images/imageFile18.png)<br><br>Data Collection<br><br>Text Analysis<br><br>![image 19](Xu et al._2024_AI for social science and social science of AI A Survey_images/imageFile19.png)<br><br>![image 20](Xu et al._2024_AI for social science and social science of AI A Survey_images/imageFile20.png)<br><br>Text<br><br>Generation<br><br>![image 21](Xu et al._2024_AI for social science and social science of AI A Survey_images/imageFile21.png)<br><br>Data<br><br>Analysis|
|---|


- Figure 3: The application of large language models at every stage of social science research. Large language models offer new possibilities for improving existing social science research processes and automated science, but also bring new potential risks and ethical issues. Social science researchers should carefully consider whether and how to apply large language models in their research.


effects brought about by the emergence of large language models in the intersection of AI and social science. Our survey aims to provide a comprehensive overview of these developments and address the existing limitations and potential of this field.

### 3. AI for social science

AI for social science refers to the application of AI in traditional social science research. Unlike the social science of AI, this section emphasizes large language models’ human-like intelligence, which can mimic human behavior to help social science research. In this section, we will draw upon the research paradigm outlined in (Donovan and Hoover, 2013; Bryman, 2016), and discuss the application of large language models as multi-purpose tools at every stage of social science research as shown in Figure 3. This aims to provide a comprehensive and informed perspective for social science researchers on how to apply large language models in the process of their research to enhance efficiency, while also revealing the untapped potential of large language models, warning about potential risks and ethical issues, and indicating possible future directions in their application.

- 3.1. Hypothesis Generation Hypothesis generation, which serves as the foundation and initial step of social science research, is the task of


mining meaningful implicit associations between unrelated social science concepts (Jha, Xun, Wang and Zhang, 2019). In the early days, hypothesis generation was largely driven by brainstorming of researchers, drawing inspiration from existing theories, patterns of anomalies in data or cross-disciplinary connections that involved serendipitous discoveries (Jaccard and Jacoby, 2019). However, as the volume of research literature grows, researchers have started to explore quicker and more efficient methods of generating solid hypotheses (Evans and Rzhetsky, 2010; Krenn and Zeilinger, 2020; Wilson, Wilkins, Holt, Choi, Konecki, Lin, Koire, Chen, Kim, Wang et al., 2018). In the following, we will present some attempts to accomplish hypothesis generation tasks using large language models.

Literature Review is the understanding, summarization, and critical thinking about the academic literature on a specific topic. Researchers have been exploring the use of large language models to assist in literature review. Some studies leverage large language models to aid in searching for relevant literature. Wang, Scells, Koopman and Zuccon (2023b) used ChatGPT to formulate and refine Boolean queries for systematic reviews, finding that ChatGPT compares favourably with the current state-of-the-art automated Boolean query generation methods in terms of precision, at the expenses of a lower recall. The paper also found that guided prompts lead to higher effectiveness than single prompt strategies. Other works focus on enabling large language models to read articles and automatically summarize the key points within them. Aydın and Karaarslan (2022) used ChatGPT to paraphrase the abstracts of relevant papers and answer questions to automatically generate literature review, which has been cited over 100 times. Elicit1 is also one typical application, an AI Research Assistant based on large language models, which can find relevant papers without perfect keyword match, summarize takeaways from the paper specific to your question, and extract key information from the papers. However, it should be noted that directly relying on large language models for literature recommendation and summarization is currently infeasible due to the risk of unreliable papers and related information being generated (Haman and Školník, 2023).

Hypothesis Propose is to propose possible explanations to some phenomenon or event. Researchers from various fields have made attempts to use large language models to help with this task. For example, Park et al. (2023b) used

- GPT-4 to generate scientific hypotheses and draw the conclusion that current large language models seem to be able to effectively structure vast amounts of scientific knowledge and provide interesting and testable hypotheses while the error rate is high. Banker et al. (2023) utilized a fine-tuned version of GPT-3 to generate psychological hypotheses and engaged 50 psychology experts to evaluate their quality, revealing that the model’s generated hypotheses were not mere replicas of previously generated human hypotheses, and exhibited no significant differences in terms of clarity, impact, and originality compared to human-generated hypotheses. Tang, Peng, Wang, Ding, Durrett and Rousseau (2023) employed large language models to generate "less likely" hypotheses, effectively assisting humans in comprehensively examining problems and eliminating cognitive biases caused by their own knowledge and experience. At present, the application of large language models in hypothesis generation is still somewhat rudimentary. Strategies for enhancing hypothesis quality include fine-tuning the large language models within specific domains (Banker et al., 2023), stepwise questioning (Wei, Wang, Schuurmans, Bosma, Xia, Chi, Le, Zhou et al., 2022), adversarial dialogue (Park et al., 2023b) and so on.


Conclusion Current research on using large language models for hypothesis generation focuses on exploring its feasibility and validity, and has commonly unveiled promising prospects and potential of employing large language models for this task. The solution mainly involves interactive design of prompts. Users input the topic they want to review. Based on these inputs, large language model automates the process of formulating and refining boolean queries, extracting core points from the search results, and generating hypotheses about potential relationships among the objects of interest.

Compared to traditional methods, the advantages mainly lie in their exceptional performance in language understanding and generation, enabling them quickly analyze existing research, identify knowledge gaps, and establish connections between seemingly unrelated ideas (Dahmen, Kayaalp, Ollivier, Pareek, Hirschmann, Karlsson and Winkler, 2023). This provides them with a natural advantage in language-based disciplines such as psychology (Banker et al., 2023).

However, researchers need to be noted that currently, large language models can only be used as auxiliary and inspirational tools in the early stage of research, and have the following limitations: 1) Fabricated or incorrect information, which may mislead users. This is because large language models lack of understanding regarding the validity of output content and simply spill out them without clear rationalization (Park et al., 2023b). 2) High sensitivity to the prompt, which results in a significant investment of effort in prompt design but yields uncertain outcomes (Wang et al., 2023b). 3) Limited context length, which makes it hard to handle long and multiple documents.

In order to better harness the potential of large language models in hypothesis generation, future directions that we may consider include: 1) Integrating specialized domain knowledge, by retrieval augmented techniques or domain-specific training. This would help reduce hallucination. 2) Developing high-reward prompt strategies. This could involve considering novel prompt generation techniques or reward mechanisms to guide the model’s hypothesis generation process. 3) Expanding the context windows of the large language models. By allowing the models to

1https://elicit.org/

Research Stages Traditional Methods Large language models Hypothesis Generation

Speed Low High Validity High Low Novelty Low High

Hypothesis Verification Experiment Research

Cost High Low Speed Low High Reproducibility Low High Scalability Low High Fidelity Entire Not Sure

Survey Research Cost High Low Engagement Low Entire Interaction Fixed Natural Bias Low Not Sure

Nonreactive Research Generality Single-purpose Multiple-purpose Accessibility Low High Numerical analysis Accurate Not Sure

- Table 1 The comparisons between traditional methods and large language models as tools at every stage of social science research. The advantages are marked in bold. From the table, we can easily find that although large language models are more advantageous on cost, speed, generality and accessibility across various research stages, the critical current limitations of validity, possible ethical risks and lack of domain knowledge still hinder its real-word applications. Please note that the comparisons in this study are only valid until the publication of this paper. Given the rapid advancements in technology, LLM agents may overcome some of the current shortcomings that are challenging to address.


consider a larger context, they would have access to more comprehensive information, potentially leading to more robust and insightful hypotheses.

- 3.2. Hypothesis Verification Once the research topic and hypotheses are established, social science researchers engage in hypothesis verification.


This process involves collecting and analyzing data to provide evidence that either supports or refutes the proposed hypotheses (Donovan and Hoover, 2013). In traditional social science research, hypothesis verification typically falls into quantitative methods like experimental research, survey research and nonreactive research, as well as qualitative methods such as field research and historical-comparative research (Juren Lin, 2017; Yuan, 2013; Bryman, 2016). Given that large language models are currently limited in their applicability to qualitative research, we primarily discuss the role of large language models in quantitative methods.

- 3.2.1. Experiment Research A laboratory experiment is "an inquiry for which the investigator plans, builds,or otherwise controls the conditions


under which phenomena are observed and measured" (Willer and Walker, 2007). The common practice involves manipulating conditions for some research participants while leaving them unaltered for others, aiming to compare the responses across groups to uncover consistent behavioral patterns. In the following, we will explore the applications of large language models in experimental research.

Experiment Assistant refers to the use of large language models in social science experiments to automate some simple but labor-intensive tasks that would normally be done by researchers. For instance, they can assist in creating hypothetical scenarios iteratively with feedback from researchers (Bail, 2023), which can enhance the external validity and comparability of the experimental conditions. Besides, large language models are capable of synthesizing the necessary information for experiments, eliminating the need for the use of real-life information utilization. This safeguards the privacy of individuals whose information could potentially be used in these studies.

Experiment Simulation aims to design a platform to explore, optimize, and predict behaviors of complex systems that might be challenging to investigate in the real world. In simulation experiments, large language models are usually used as believable proxies of human behavior (Aher et al., 2023; Park et al., 2023a). For example, Park et al. (2022) provides a typical application where large language models are utilized to simulate the behavior of community users, assisting designers in gaining insights into the various possibilities of social interactions and identifying potential edge cases that could lead to the breakdown of a community. Horton (2023) considers GPT-3 AIs as homo silicus agents, and demonstrates their ability to qualitatively recover findings from three classic behavioral economics experiments with real humans. Guo (2023) designs well-crafted prompts to enable GPT agents to participate in strategic game experiments and achieve realistic performance. Park et al. (2023a) constructed a fully large language model-driven simulated community, where they observed human-like individual behaviors and emergent behaviors.

Conclusion In experimental research, large language models can serve dual roles - they can act as experiment assistants and as believable proxies of human behavior, becoming subjects of the experiment themselves. The latter, in particular, has attracted increasing attention in both AI and social science as large language models are increasingly capable of simulating human-like responses and behaviors. Currently, the design of AI agents is still relatively crude, usually including four modules: profile, memory, planning, and action (Wang, Ma, Feng, Zhang, Yang, Zhang, Chen, Tang, Chen, Lin et al., 2023a), and warrants further improvement.

Using large language models for simulating experiments offers several advantages: 1) Improved efficiency, reduced costs, and enhanced scalability (Bybee, 2023; Guo, 2023). 2) Circumventing the ethical issues associated with human subjects. This opens the door to experiments that may be deemed unethical if performed on humans, such as the classic Stanford Prison Experiment (Zimbardo, Haney, Banks and Jaffe, 1971).

However, social scientists must also proceed with caution in this area, taking into account the following limitations: 1) Uncertain believability. There is now no "gold standard" study demonstrating that groups of automated agents can accurately simulate humans (Bail, 2023). 2) Low transparency and reproducibility. Since large language models themselves are still black boxes, we cannot provide a thorough explanation of their behavior.

In order to address the aforementioned limitations, potential future directions include: 1) developing methods for evaluating the quality of large language models simulations, and 2) incorporating insights from cognitive science to guide the development of AI agent frameworks and enhance their behavior’s human-likeness and rationality.

- 3.2.2. Survey Research Survey research is a fundamental methodology in social science, which uses written questionnaires or formal


interviews to collect information on the beliefs, opinions, characteristics, and past or present behaviors of a target group (Bryman, 2016). The core of modern survey research is three key components: sampling, measurement, and analysis (Wright, Marsden et al., 2010). The following will explore the role that large language models play in each stage of survey research.

Sampling involves selecting representative samples from human populations, whose observed characteristics provide unbiased estimates of the characteristics of those populations. Large language models present a novel option for sampling, serving as proxies for specific human subgroups. This enables the avoidance of the sampling step, or rather, utilizes the extensive training database of the large language models directly as the sample for the study. Existing studies have proposed and explored the possibility of using language models as effective stand-ins for particular human demographics in the realm of social science research. For example, Argyle, Busby, Fulda, Gubler, Rytting and Wingate (2023) compares real human participants from multiple large surveys in the United States and "silicon samples" which are created by conditioning large language models on socio-demographic backstories from them, demonstrating that the “algorithmic bias” within GPT-3 is both fine-grained and demographically correlated.

Bisbee, Clinton, Dorff, Kenkel and Larson (2023) investigates the quality, reliability, and reproducibility of synthetic survey data generated by the popular closed-source large language model, ChatGPT. The experimental results suggest that the average scores generated by ChatGPT closely align with the averages from baseline survey (conducted from 2016 to 2020 on the U.S. national elections). However, when it comes to more advanced features, such as variance, subgroups, and statistical inferences, it often leads researchers to draw conclusions that differ from those relying on human respondents. Dillion, Tandon, Gu and Gray (2023) takes moral judgments as an example to investigate whether and when language models can potentially replace human participants in psychology. The analysis indicate that language models align most closely with humans when the contextual circumstances involve explicit

features that drive human judgment, do not pertain to competitive situations, and when the subjects being judged are representative within the training data. Rao, Leung and Miao (2023) conducts the Myers-Briggs Type Indicator (MBTI) test on large language models agents of different subpopulations and showcases the ability of ChatGPT in analyzing personalities of different groups of people. Brand et al. (2023) interview GPT-3 to estimate customers’ willingness-to-pay for products and features and find that large language models can generate responses that align with economic theories and consumer behavior patterns. Chu et al. (2023) adapts LMs to subpopulation-specific media diets and successfully simulates how the subpopulation will respond to survey questions.

Measurement focuses on designing questions to draw out valid and reliable responses across a broad spectrum of subjects, which are often characterized as "the art of asking questions". While it’s natural to leverage large language models to assist in the design of questionnaires or interview questions, more researchers are focusing on the role large language models play in facilitating a paradigm shift in the measurement methods within survey research - from closed-ended rating scales, to open-ended response questionnaires, and then further towards more natural interactive interviews. For example, Kjell, Sikström, Kjell and Schwartz (2022) compared the results of psychological surveys using rating scales and natural language-based open-ended questionnaires. The latter was found to achieve accuracy that either exceeded or rivaled the typical methods of reliability in rating scales, which is often considered as the theoretical upper limit. Kjell et al. (2023) provides a future outlook of finer granularity and automated interactive interviews, making full use of interviewees’ own words to best elicit truthful responses.

Analysis is a step using multivariate data analysis techniques to identify and understand the statistical relationships among various variables. Large language models can be used to analyze qualitative data, such as interview responses, to identify patterns, relationships, and common themes (Abbas, 2023). For instance, Yang, Ji, Zhang, Xie and Ananiadou (2023a) utilize large language models, specifically ChatGPT, to perform mental health analysis and highlight the significant potential of large language models in improving the interpretability of mental health analysis. However, large language models, which are not specifically designed for analyzing quantitative data, are currently not the primary method for survey research analysis in the social sciences. Instead, survey data is typically presented in the form of charts, graphs, or tables, and analyzed using statistical methods (Bryman, 2016). Future versions of the model may be able to integrate tools like Python and R libraries to conduct quantitative data analyses (Mialon, Dessì, Lomeli, Nalmpantis, Pasunuru, Raileanu, Rozière, Schick, Dwivedi-Yu, Celikyilmaz et al., 2023).

Conclusion The current applications of large language models in survey research primarily revolve around three main directions: 1) Effective proxies for specific human sub-populations. 2) Interactive interviewers. 3) Result analysis tools.

For the first direction, the current work has demonstrated that proper conditioning will cause large language models to accurately emulate response distributions from a wide variety of human subgroups. This approach can effectively address limitations regarding the number of questions, frequency and the subpopulation due to cost constraints (Chu et al., 2023), as well as the common challenge of low response rates (Bhattacherjee, 2012) in survey research, offering significant advantages in terms of engagement and cost. However, whether and which large language models can truly represent humans remains an open question (Argyle et al., 2023). This approach fundamentally relies on "algorithmic bias," which is heavily influenced by the training data and is susceptible to producing unfair and non-objective results. In light of these considerations, we do not propose that large language models should completely replace traditional sampling methods in survey research. Instead, we see their potential in simulating population responses to assist in survey design. This hybrid approach allows us to harness the strengths of large language models while still recognizing the importance of traditional sampling techniques to maintain the integrity and fairness of survey results.

Several researchers have envisioned the impact of language models on the form of survey. The advantage of large language models lies in their ability to fully utilize the individuals’ own language to describe the information needed by researchers, which has the potential not only to gradually improve current assessments but also to fundamentally alter the nature of measuring and describing personal states, ultimately enhancing our understanding of social science. However, utilizing large language models to facilitate measurement also poses risks. Inherent biases in large language models and the potential for data leakage must be carefully navigated when implementing large language models in research scenarios.

For result analysis, large language models are primarily used for text analysis and are seldom employed for numerical analysis because they are not proficient in it. Future research can consider the integration of large language models with specialized computational tools.

- 3.2.3. Nonreactive Research Nonreactive research refers to the research method where the participants are not aware that their information is


part of the study, unlike experiment research and survey research that actively engage the people we study by creating experimental conditions or directly asking questions (Juren Lin, 2017). This method may reduce bias due to interference from researchers or measurement instruments (Trochim and Donnelly, 2001). In this section, we will adhere to the taxonomy in (Juren Lin, 2017), and explore the roles that large language models play in content analysis and existing statistics analysis.

Content analysis is a widely used technique for examining the content contained in written documents or other communication media. The remarkable performance of large language models in various traditional NLP tasks has attracted extensive attention about using them in content analysis tasks within the field of social science.

Some social science researchers employ large language models to perform text classification, a basic and important task that involves labeling or categorizing texts according to predefined categories (Aggarwal and Zhai, 2012). Common text classification tasks in the field of social science include: 1) Sentiment analysis, which aims to identify and extract the emotional attitudes in the text, such as joy, anger and sorrow. It is a widely applied technique in psychology and political science. In psychology, sentiment analysis helps researchers understand people’s emotional states, stress levels, and mental health conditions. Rodríguez-Ibánez, Casánez-Ventura, Castejón-Mateos and CuencaJiménez (2023) suggest that large language models are the future paradigm for sentiment analysis, due to their zero-shot setting and simple invocation. However, they also point out the limitations of GPT-3 in the current tasks. ChatGPT performs excellently in three text-based mental health classification tasks, including stress detection, depression detection, and suicide detection (Lamichhane, 2023). ChatGPT also applies to differentiate paranoid texts from nonparanoid ones in some studies (Uludag, 2023). Rathje, Mirea, Sucholutsky, Marjieh, Robertson and Van Bavel (2023) evaluate the performance of GPT-3.5 and GPT-4 on multilingual sentiment and discrete emotions tasks and find that in many cases, GPT models perform close to (sometimes better than) fine-tuned machine learning models. They argue that GPT models offer a promising avenue for cross-lingual research in psychology. Wu, Irsoy, Lu, Dabravolski, Dredze, Gehrmann, Kambadur, Rosenberg and Mann (2023b) introduce BloombergGPT, a 50 billion parameter language model tailored for the financial domain, and evaluate it on two financial sentiment analysis datasets FPB (Malo, Sinha, Korhonen, Wallenius and Takala, 2013) and FiQA SA (Maia, Handschuh, Freitas, Davis, McDermott, Zarrouk and Balahur, 2018). BloombergGPT outperforms general models such as GPT-Neo (Black, Leo, Wang, Leahy and Biderman, 2021), OPT (Zhang, Roller, Goyal, Artetxe, Chen, Chen, Dewan, Diab, Li, Lin, Mihaylov, Ott, Shleifer, Shuster, Simig, Koura, Sridhar, Wang and Zettlemoyer, 2022) and BLOOM (Scao, Fan, Akiki, Pavlick, Ilić, Hesslow, Castagné, Luccioni, Yvon, Gallé et al., 2023) on both tasks. Frąckiewicz (2023) leverage ChatGPT for social network analysis, enabling fast identification of key topics, sentiments, and influencers in the network, content generation, monitoring and flagging of harmful content in the community, and bringing profound changes to social network analysis. 2) Stance detection, which aims to determine the political, social or cultural stance of the author or speaker expressed in a text. This is of great significance for fields such as political analysis, public opinion monitoring, etc. Zhang, Ding and Jing (2023) applies ChatGPT to two common datasets for stance detection and achieves state-of-theart or comparable performance. Stance detection is a natural language processing task that aims to identify the attitude of a text author towards a target, such as support, oppose, or neutral. It is useful for analyzing different perspectives on social, political, or cultural issues. For example, in political analysis, public opinion monitoring, and other domains, it is important to understand people’s views on certain events or claims. Wu, Nagler, Tucker and Messing (2023a) uses large language models to measure the latent ideology of politicians and scores US senators on a liberal-conservative scale by having ChatGPT choose the more liberal (or more conservative) senator in pairwise comparisons. Törnberg (2023) experiment on identifying the political party affiliation of Twitter posters and find that GPT-4 surpasses human experts and crowdsourced workers in accuracy and reliability. 3) Hate speech detection, which aims to identify and filter out words, phrases or sentences that may contain hate speech in a text. Some hate speech may be expressed in subtle ways, or use multiple languages and dialects, thus posing certain challenges for hate speech detection. Huang, Kwak and An (2023b) uses ChatGPT to detect whether tweets imply hate speech, and successfully identifies 80% of the tweets containing hate speech. 4) Misinformation detection, which aims to identify and filter out words, phrases or sentences that may contain misinformation in a text. Social media is the main platform for people to communicate, share and get information, but also a hotbed for misinformation dissemination. Misinformation can not only mislead the public, but also affect social trust, democratic participation and policy making. Misinformation detection can help prevent users from posting misinformation, thereby reducing the spread of false and misleading information. In the field

of cancer misinformation detection, ChatGPT achieves an accuracy of 96.9% (Johnson, King, Warner, Aneja, Kann and Bylund, 2023). The answers generated by ChatGPT show no significant difference from those of the National Cancer Institute (NCI) in terms of word count or readability. Hoes, Altay and Bermeo (2023) finds that ChatGPT has a classification accuracy of 72% on fact-checking tasks, with higher accuracy for true statements.

Other social science researchers utilize large language models for text generation tasks, one of the most challenging and creative tasks in NLP that involves automatically producing coherent, fluent and meaningful texts based on a given input or goal (Gatt and Krahmer, 2018). The typical applications of large language models in the field of social science for text generation tasks include: 1) Natural language descriptions or explanations, which mainly aims to improve the interpretability and credibility of results. For example, Huang, Kwak and An (2023a) proposes Chain of Explanation, a method to guide large language models such as GPT-Neo, T5 (Raffel, Shazeer, Roberts, Lee, Narang, Matena, Zhou, Li and Liu, 2020), OPT and others to generate high-quality explanations for online hate speech. Although it makes significant improvements over previous methods, it still lags behind human level in terms of clarity and informativeness. Huang et al. (2023b) uses ChatGPT to explain whether tweets imply hate speech, and finds that its generated explanations are clearer than those written by humans, while having no significant difference in informativeness with human-written ones. Large language models are applied in the field of linguistics to generate explanations that help improve the understanding and evaluation of linguistic phenomena and theories. Chakrabarty, Saakyan, Ghosh and Muresan (2022) uses GPT-3 to generate explanations for a figurative language Natural Language Inference dataset, and lets GPT-3 generate explanations for its judgments on figurative expressions, involving three types: Sarcasm, Simile, and Metaphor. 2) Future predictions. Large language models are used for future prediction due to their powerful generative capabilities, but they are also limited by the complexity and uncertainty of the prediction scenarios or reality. Kalinin (2023) explores the use of GPT-3 as an information retrieval tool for predicting the RussianUkrainian conflict. The responses of GPT-3 are used as inputs for a game theory-based model of strategic behavior called "Predictioneer’s game". But GPT-3 is limited by its reliance on prewar data and its inability to capture complex patterns of behavior. Jungwirth and Haluza (2023) uses GPT-3 to predict the future of the war in Ukraine by using GPT-3 to generate future scenarios while assessing the consistency within the scenarios.

There are also studies that have conducted comprehensive evaluations of large language models’ performance across multiple content analysis tasks. For example, Gilardi et al. (2023) expand the application scope of ChatGPT to five text annotation tasks. Their results show that ChatGPT outperforms crowd workers in annotation tasks such as relevance, stance, topics, and frames detection, and is much lower in cost than the latter. Ziems et al. (2023) evaluates the performance of ChatGPT on multiple NLP tasks related to social science, and finds that it performs poorly on tasks such as event argument extraction, character tropes, implicit hate, and empathy classification, which involve complex structures or subjective expert taxonomies. In contrast, large language models achieve an accuracy of over 70% on tasks such as misinformation, stance and emotion classification, which are based on objective basic facts or clearly verbalized definition labels.

Existing statistics analysis is a research method that builds on the analysis of existing statistical data, which comes from official agencies, organizations, institutions or individuals, and covers various social phenomena and issues. Analysis of existing statistics can help researchers save time and cost, use existing information resources, and explore new research questions and hypotheses. In the following, we will discuss the applications of large language models in descriptive and inferential analysis as well as predictive analysis.

Large language models can be used to describe the characteristics of the sample or the relationship between variables, or to make inferences about causal processes, which refers to descriptive and inferential analysis (Rubin and Babbie, 2016). For example, Chen, Li, Smiley, Ma, Shah and Wang (2022) attempts to use large language models to understand financial reports and statements, but GPT-3 either copies the reasoning steps from the examples or gives incorrect reasoning, resulting in an accuracy below 50%. BloombergGPT (Wu et al., 2023b) is also applied to this task, but achieves only 43.41% exact match accuracy. Although both large language models do not reach satisfactory results, OpenAI recently released more powerful ChatGPT and GPT-4, which might be able to perform better on this task.

Large language models can also be used to infer future trends and changes based on historical data, which refers to predictive analysis. This provides a basis for decision making, thus having a very wide range of applications in fields such as finance. For example, Lopez-Lira and Tang (2023) demonstrates the potential of using ChatGPT to predict stock market returns. The authors simulate financial experts with ChatGPT and ask it to evaluate the impact of company-related headline news from the previous day on the stock price, based on sentiment analysis. They find that

Subject Task Dataset Related work

Depression_Reddit (Pirina and Çöltekin, 2018), CLPsych15 (Coppersmith, Dredze, Harman et al., 2015), Dreaddit (Turcan and McKeown, 2019), SAD (Mauriello, Lincoln, Hon et al., 2021)

Yang, Ji, Zhang et al. (2023b); Lamichhane (2023);Uludag (2023); Kjell et al. (2022)

Mental Health State Detection

Psychology

Personality Measurement - Rao et al. (2023)

SemEval-2016 Stance detecting Dataset (Mohammad, Kiritchenko, Sobhani et al., 2016)

Stance Detection

Ziems et al. (2023)

Politics

Ideology Detection IBC (Iyyer, Enns, Boyd-Graber et al., 2014) Ziems et al. (2023) Misinformation Detection Politifact Fact Check(Misra, 2022) Hoes et al. (2023)

LatentHatred (Elsherief, Ziems, Muchlinski et al., 2021)

Huang et al. (2023b) Misinformation Detection

Hate Speech Detection

Sociology

Misinfon Reaction Frames (Gabriel, Hallinan, Sap et al., 2022)

Ziems et al. (2023)

Sentiment Analysis FPB (Malo et al., 2013) Wu et al. (2023b); Xie, Han, Zhang et al. (2023b) Aspect Sentiment Analysis FiQA SA (Maia et al., 2018) Wu et al. (2023b); Xie et al. (2023b)

Headlines (Sinha and Khandait, 2021), BigData (Soun, Yoo, Cho et al., 2022), StockNet (Xu and Cohen, 2018), CIKM18 (Wu, Zhang, Shen et al., 2018)

Finance

Wu et al. (2023b); Xie et al. (2023a,b)

Binary Classification

Named Entity Recognition NER (Alvarado, Cesar, Verspoor et al., 2015) Wu et al. (2023b) Named Entity Recognition+ Named Entity Disambiguation

NER+NED (Wu et al., 2023b; Xie et al., 2023b) Wu et al. (2023b) Question Answering ConvFinQA (Chen et al., 2022) Wu et al. (2023b); Xie et al. (2023b)

- Table 2 A disciplinary perspective on AI for Social Science. This table presents a comparison of representative tasks, datasets used, and related work for each discipline.


ChatGPT’s sentiment scores had a significant positive correlation with the subsequent daily stock market returns. Xie, Han, Lai, Peng and Huang (2023a) find that using ChatGPT to predict stock trends based on historical price features and tweets has limited success, and even performs worse than traditional methods using only price features. However, ChatGPT is still recognized as having the potential to improve financial market prediction by utilizing social media sentiment and historical stock price information.

Conclusion Numerous studies have applied and evaluated large language models in a wide range of computational social science tasks, clarifying that large language models can significantly transform nonreactive research in three ways: 1) Assisting data annotators on human annotation teams. 2) Serving as zero/few-shot text analysis tools. 3) Bootstrapping challenging creative generation tasks.

The application of large language models in nonreactive research offers several advantages. Firstly, it can partially remove the limitations of data resources since large language models can achieve performance comparable to finetuned models in many social science tasks without extensive training. Secondly, they exhibit broad cross-disciplinary applicability, providing general solutions to a wide range of problems. Thirdly, they lower the entry barriers for usage. large language models have changed the scenario where researchers previously had to rely on statistical learning, machine learning, or deep learning methods to handle massive statistical data, which posed a high degree of difficulty and complexity. They are capable of interacting directly through text inputs instead of complex code or commands, providing a more direct and user-friendly interface, significantly lowering the technical barriers to using artificial intelligence for analysis. Consequently, researchers can focus more on the research questions they are interested in, rather than becoming excessively immersed in the intricacies of technical implementation.

However, there are some limitations to note: 1) Almost all large language models struggle with conversational and full document data, which limits common applications such as topic modeling. 2) large language models may have difficulty understanding the subtle and non-conventional language of expert taxonomies, which don’t present in pre-trained data.

NLP researchers working to improve existing large language models for better support in nonreactive tasks can look at the following future directions: 1) the unique technical challenges of conversational, long-document, and cross-document reasoning, 2) in-domain training to teach LLMs to understand novel social constructs, 3) integration of specialized numerical analysis tools.

- 3.3. Revisiting Applications Across Disciplines In this section, we revisited the application of large language models in social science from a disciplinary

perspective, to provide readers with a more comprehensive understanding of research progress in this field. The representative tasks, datasets used, and related work for each discipline are outlined in Table 2.

From a task perspective, we observe that the diverse tasks across disciplines can be summarized mainly into three categories: text classification, structured parsing, and natural language generation, which are relatively easier to handle in social science. However, more complex tasks such as aggregating mining on massive datasets, multi-document summarization or topic modeling may exceed the scope of transformer-based language models at present. From the algorithmic perspective, large language models can serve as a universal solution, meaning that almost all tasks can be addressed using the same approach, with the only difference being the design of prompts. The main drawbacks of using large language models as a solution could be related to issues like bias, high computational cost, difficulties in fine-tuning for specific tasks and so on.

- 3.4. Discussions As mentioned above, large language models can be applied at every stage of social science research, improving


efficiency across the board. More specifically, the practical applications of large language models in social science research predominantly fall into three directions: 1) replacing traditional NLP tools in data analysis, 2) assisting in creative work in research, 3) simulating humans as study objects. So far, extensive studies have thoroughly examined the superiority of large language models in the first direction. However, the last two directions, which particularly emphasize large language models’ human-like intelligence, are still in the exploratory stage without a systematic body of research.

In the future, several directions of AI for social science may lie in the following: 1) Further exploring the untapped potential of large language models in social science research. For instance, a large language model-based fully automated social science research pipeline could be developed, covering everything from hypothesis generation to hypothesis verification and even peer review. 2) Injecting domain-specific knowledge into large language models, thereby facilitating the development of expert models. 3) Establishing comprehensive benchmarks to measure the human-like attributes of large language models. 4) Integrating tools into large language models to enhance their capabilities in logical reasoning and mathematical derivation. 5) Developing multi-modal large models, which could improve their real-world understanding of human social behavior and systems. 6) Ethical and moral norms. Constructing ethical and moral frameworks for the functioning and application of large language models, thereby ensuring their responsible use.

### 4. Social science of AI

Social science of AI refers to AI’s social science. Specifically, we will focus on social science researches that use large language models as objects, with a particular emphasis on how they differ from traditional human behavior. Unlike AI for social science, the aim is not to make large language models mimic human behavior, but rather to explore the behavioral patterns of large language model agents themselves. In Table 3, we give specific differences between social science of human beings and of large language models.

In this section, we will explore the social behavioral patterns of large language models as intelligent agents through the lens of various sub-disciplines within the social sciences. This emerging field has become increasingly significant due to several factors. Firstly, AI has demonstrated its ability to autonomously perform tasks in various domains. Secondly, research has shown that the collaboration of multiple AI agents can effectively enhance their performance. However, the behavior patterns, consequences, and impacts of AI collaboration are still not very clear. Additionally, the factors that drive changes in collaborative behaviors among AI agents are also not clearly understood. Similar to social science on humans, the ultimate goal of the Social Science of AI is to inform us about the behavioral traits exhibited by AI agents when they collaborate with each other and how to model and understand these behavioral traits. This type of research is of significant importance for the autonomous decision-making and control of future AI collectives.

- 4.1. Psychology of AI Psychology of AI, or to say the psychology of machines, is typically defined as the scientific study of mind and


behavior in AI agents (Hagendorff, 2023). Extensive research in this field has been conducted with the enhanced capabilities of large language models. It has even been claimed that large language models may have a consciousness

of Human Beings of AI

Study personality, consciousness, ability, cognition, and more of AI agents.

Psychology Study the psychological phenomena, consciousness, and behavior of humans (Danling, 2019). Research spans a wide range of areas including consciousness, sensation, perception, cognition, emotion, personality, behavior and relationships.

Study interactions and social behaviors among multiple different AI agents.

Sociology Study human social life, groups, and societies, ranging from institutions or human interactions at the micro-sociological level to social systems or structures at the macrosociological level (Giddens, 2007).

Study the behavior and interaction of AI agents as economic agents.

Economics Study the production, distribution, and consumption of goods and services (Backhouse, 2002; Krugman and Wells, 2009).

Politics Study the authoritative allocation of societal values (Easton, 1955).

Study the political behaviors and phenomena exhibited by AI agents, such as ideology, party affiliations, and political prudence.

Linguistics Study language (Halliday, 2006), including syntax, semantics, morphology, phonetics, phonology, pragmatics (Farmer and Demers, 2010), and etc.

Study the language use patterns of AI agents and compare them to human language use.

- Table 3 The differences between social science of human beings and social science of AI in different sub-disciplines. The fundamental distinction between the two lies in the difference in their research subjects. The former investigates behavioral patterns within the human population, while the latter regards AI agents as intelligent entities and explores the behavioral patterns within the groups they form.


of its own. A typical example is a Google engineer’s assertion that the conversational AI system, LaMDA, which he was developing, has become sentient and capable of thinking and reasoning like a human, leading to his suspension from work (Tiku, 2023). He believes that this large language model has attained the intelligence level of a 7-year-old or 8-year-old child. In this section, we will organize the current advancements in psychology of AI, according to the research content of the psychology (Danling, 2019), such as personality, cognition, and more.

Personality refers to the sum of distinctive traits and characteristics that an individual possesses psychologically, emotionally, and behaviorally. Due to the stochastic nature of large language model’s outputs, the personality of large language models refers to its overall tendency in generating responses. Researching the personality of large language models contributes to creating more human-friendly large language models. OpenAI’s blog (OpenAI) pointed out that for models such as ChatGPT, the emotional bias of its output depends on both the pre-training stage and the fine-tuning stage. The sentiment tendency of the pre-training part comes from a large amount of text, and the value tendency of the fine-tuning stage may be related to the labeling staff or the fine-tuning task due to the different techniques used.

The most commonly used method for personality assessment of large language models is the utilization of questionnaires. With advancements in GPT-3 and its more powerful successor large language model, these language models are now capable of comprehending and fluently answering questions. The format of questionnaires is also highly compatible with language models. Survey questionnaires designed for human subjects typically require only minor adjustments in terms of formatting or vocabulary to be directly employed for personality testing (Miotto et al.,

- 2022). After adding the output method, it can be directly sent to the language model as a prompt for a reply. Research on large language model’s personality has yielded some interesting conclusions. Jiang, Xu, Zhu, Han,


Zhang and Zhu (2022a) proposed the Machine Personality Inventory (MPI) dataset for evaluating the machine personality, finding that personality indeed exists in large language models. Miotto et al. (2022) used Hexaco questionnaire (Ashton and Lee, 2009) to analyze GPT-3 and found that GPT-3 is generally a young woman whose personality level is consistent with the general tendency of human beings. In the assessment of human values, GPT-

- 3 accords importance to every value, which can sometimes appear contradictory. Li et al. (2023) use Short Dark


Triad (SD-3) and Big Five Inventory (BFI) tested GPT-3, InstructGPT, and FLAN-T5 and found that the tested large language models all showed darker than humans. The latter two are no better than GPT-3, even after fine-tuning. Furthermore, some studies have found that the personality traits of large language models can be effectively changed by fine-tuning (Karra, Nguyen and Tulabandhula, 2023) or increasing memory (Jiang et al., 2023). This opens up the possibility of more related research.

Cognition is about how humans understand, perceive, make decisions, and solve problems. Incorporating methodologies from cognitive psychology into large language models aids us in better understanding how these models process and address problems.

There have been numerous studies investigating whether large language models are capable of human-like cognition. For instance, Binz and Schulz (2023) employed classic vignette-based and task-based experiments from the cognitive psychology literature to assess GPT-3’s decision-making, information search, deliberation, and causal reasoning abilities. The results indicate that GPT-3 can achieve human-comparable performance on most tasks, but its behavior is highly influenced by how the vignettes are presented and it does not learn and explore in a human-like manner. Han, Ransom, Perfors and Kemp (2022) focused on GPT-3’s inductive reasoning ability. Experiment results suggested that GPT-3 can qualitatively mimic human performance for some inductive phenomena (especially those that depend primarily on similarity relationships), but fails to explain human inductive inferences, which may be due to GPT-3 not following the reasoning principles used by humans. Webb, Holyoak and Lu (2023) compared the analogical reasoning abilities of human reasoners and the text-davinci-003 variant of GPT-3 and found that large language models displayed a surprisingly strong capacity for abstract pattern induction, which may explain their abilities to reason about novel problems zero-shot. Prystawski, Thibodeau and Goodman (2022) incorporated Chain of Thought (CoT) into the metaphor process inspired by cognitive psychology. Collins, Wong, Feng, Wei and Tenenbaum (2022) proposed a new benchmark for comparing the capabilities of humans and language models in problem-solving domains (planning and explanation generation). On this benchmark, humans are much more robust than large language models. Kosoy, Chan, Liu, Collins, Kaufmann, Huang, Hamrick, Canny, Ke and Gopnik (2022) tested the abilities of GPT-3 and PaLM in causal reasoning environments. Besides direct reasoning abilities, biases in reasoning or decision-making processes have also received attention. Various studies, in different manners and types, have collectively demonstrated the existence of certain biases in large language models, such as ChinChilla-7B/70B, CodeX, and ChatGPT, which are often similar to human cognitive biases (Dasgupta, Lampinen, Chan, Creswell, Kumaran, McClelland and Hill, 2022; Jones and Steinhardt, 2022; Chen et al., 2023).

Theory of mind (ToM), another cognitive ability, refers to the capacity to comprehend others by attributing psychological states to them. Studies, exemplified by the false belief task, indicate that more advanced large language models perform better in ToM (Kosinski, 2023). Interestingly, we have located research papers on various models of the GPT series. In their study on GPT-3-davinci, Sap, Le Bras, Fried and Choi (2022) noted that large language models cannot comprehend the intentions and reactions of social participants and infer the mental states of situational participants. However, when the research subject shifts to GPT-3.5 models such as text-davinci-002 and text-davinci003, the large language models become more competent and closer to humans (Trott, Jones, Chang, Michaelov and Bergen, 2023; Dou, 2023). Other studies of large language models’ cognitive abilities include creativity tests, such as alternative tool tests for GPT-3 (Stevenson, Smal, Baas, Grasman and van der Maas, 2022), cognitive reflection tests and semantic illusions to examine the decision-making processes of large language models (Hagendorff, Fabi and Kosinski, 2022), and assessments of GPT-4’s cognitive abilities (Dhingra et al., 2023).

Others Apart from personality and cognition, there are many other psychological aspects of AI being studied. Feng, Xu, Li and Liu (2023b) proposed that human body size affects the affordances of objects around them, and demonstrated that ChatGPT also exhibits this ability. They concluded that the embodied perception of ChatGPT (GPT-4 version) could be comparable to that of an average adult human, around 5 feet 6 inches tall. Pellert et al. (2022) suggested administering psychometric questionnaires to various models and requesting output, proposing the concept of AI Psychometrics. Further research has examined moral concepts and values in large language models (Fischer, LuczakRoesch and Karl, 2023; Jin et al., 2022).

Conclusion In summary, extensive research has been conducted to explore the psychological features of large language model agents, from the perspectives of personality, cognition, and others, leading to many intriguing findings.

From a personality perspective, researchers generally find that large language models do exhibit personality tendencies, but these tendencies are not consistent and stable like those of humans. Instead, large language models are superpositions of cultural perspectives. These personality traits can be effectively altered through methods such as fine-tuning or enhancing memory capacities.

In the realm of cognitive abilities, studies have explored various facets, including induction, analogy, causal reasoning, theory of mind and so on. It is commonly found that the most advanced large language models, represented by GPT-3.5 and GPT-4, can demonstrate cognitive capabilities comparable to or even surpassing human abilities. These abilities improve with the evolution of the models. However, the cognitive modes employed by these language models are inconsistent with those of humans, and there is currently no universally accepted hypothesis to explain their cognitive abilities.

We believe that there are several pressing issues in this field that need to be addressed. These issues include: 1) Data leakage concerns. Much of the current research is based on classic psychological experiments to explore the cognitive capabilities of models, but it is unclear whether the test data is part of the language model’s training data. 2) Unclear influence factors. The impact of factors such as the model’s training objective, size, and data to its abilities has not been systematically analyzed.

- 4.2. Sociology of AI Unlike the psychology of AI, which focuses on the behaviors of individual AI agents, the sociology of AI mainly


studies the social behaviors and interactions of multiple AI agents. It is important to note that we will primarily discuss researches that are similar to human sociology, but with a focus on AI agents as the research subjects. This distinction sets us apart from other reviews that primarily concentrate on societal changes and issues arising from advancements in AI (Joyce, Smith-Doerr, Alegria, Bell, Cruz, Hoffman, Noble and Shestakofsky, 2021).

Social bias Many researches focused on social bias2, referring to unfair situations that emerge in large language models. With the widespread application of large language models, this can negatively impact user decision-making and interactions. The discussion about various biases in large language models started almost from the very beginning of their inception (Brown et al., 2020) and the topic is discussed with almost every large model released (Chowdhery et al., 2022; OpenAI, 2023; Touvron et al., 2023). In papers, it often appears in sections like Limitations or Ethical Considerations. However, as a single section in a paper, the exploration is obviously insufficient, and subsequent research has focused on exploring social bias in large models. For instance, Lucy and Bamman (2021) studied gender bias in GPT-3 and found that in the stories generated by GPT-3, females are more likely to be associated with family and appearance and are portrayed as less powerful than male characters. For minority groups, GPT-3 was also pointed out to have a bias against disabled people (Amin and Kabir, 2022). Some methods have been adopted to reduce bias or toxicity in large models. For instance, InstructGPT used a reinforcement learning approach to fine-tune the model, reducing toxic outputs (Long et al., 2022). We believe that there is a need for concerted efforts from researchers in sociology and AI to address these issues.

Social behavior Other researchers have considered the sociological behaviors among multiple large language modeldriven agents. While there are not many researches in this area, interesting phenomena can still be observed. Park et al. (2023a) created a rather interesting experimental environment. They built a sandbox where 25 agents live in a small town within the sandbox. The agents can wake up, make breakfast, and have small talk among themselves. They ended up exhibiting surprising social behaviors, such as spontaneously inviting and scheduling a party when a user assigns an agent to host one. In this research, through the introduction of a memory module and carefully designed processes, agents have become more human-like. Chirper3 is an online community, where, unlike other communities like Reddit, all participants in Chirper are AI. You can set a backstory for a bot, and the bot will automatically post messages and interact. For instance, under the #NewFriends topic, bots invite each other for walks in the park with their dogs, just like in a real human community, but all participants are AI. While these research efforts are intriguing, we believe they have yet to truly tap into the potential of AI sociology. We look forward to seeing more researchers delve into this field in the future.

- 2Research on bias falls within the purview of social psychology, a cross-domain of sociology and psychology. We categorize it under the sociology section to emphasize its interactive nature.
- 3https://chirper.ai/


Conclusion Currently, researchers have made some progress in social bias of AI, but there is still a dearth of studies specifically exploring sociological phenomena within the AI community.

The issue of social bias in AI has been a long-standing topic of discussion. Researchers have put forth various assessment methods and benchmarks to tackle bias issues, and they have made considerable strides in ensuring fairness and impartiality in language models when it comes to surface-level queries. Nevertheless, there is still much work to be done in this area, and several key challenges must be addressed: 1) Positive Stereotypes and essentializing Narratives. Even if a word may seem positive in sentiment, it can lead to harmful narratives. For example, praising women for being submissive and humble. 2) Implicit cognitive bias. Language model bias can be induced in various ways.

Despite our society witnesses a surge in the number of AI agents and the emergence of AI agent-exclusive communities, there has been limited research on the interaction patterns of language models within these environments. We anticipate a greater involvement of researchers from both the field of artificial intelligence and social science to systematically uncover the similarities and differences between the sociology of AI and human.

- 4.3. Economics of AI Economics of AI is the scientific study of how AI agents, as economic entities, produce, allocate, and consume


goods and services (Backhouse, 2002; Krugman and Wells, 2009). Large language models have demonstrated their ability to act as economic agents, especially in the field of economics. Meanwhile, researchers have observed and compared their performance with that of humans in some economic experiments. In the following, we give an overview of both.

Economic expertise measures large language models’ professional knowledge, skills, and experience in the field of economics. Although there are still some limitations, large language models show the ability of economic agents, including certain knowledge and understanding of economics, risk assessment and management ability, etc. For economics, in the Test of Understanding in College Economics, ChatGPT outperformed 91% of students in the microeconomics and 99% in the macroeconomics. For finance, Davinci and ChatGPT score 58% and 67%, respectively, on the financial literacy test, 31% above the benchmark level (Niszczota and Abbas, 2023). Large language models show some ability on the "Financial Investment Opinion Generation (FIOG)" task, but there is still room for improvement (Son et al., 2023). GPT-3 can identify the potential impacts of climate change on economic growth, employment, poverty, inequality, and financial stability, and was also able to suggest some countermeasures (Leippold,

- 2023). Large language models match many biases in the expectations of existing professional humans and institutions for various financial and macroeconomic variables, including inflation, based on a sample of Journal news articles from 1984 to 2021 (Bybee, 2023). For operations management, ChatGPT earned a B- to B on the final exam for the MBA core course Operations Management but it doesn’t work well for simple calculations or more advanced process analysis (Terwiesch, 2023). For marketing, the marketing content generated by ChatGPT matched and sometimes surpassed, human content on quantitative and qualitative measures (Rivas and Zhao, 2023). Conversations with consumers also show a high degree of intelligence and adaptability (Rivas and Zhao, 2023). ChatGPT was found to be more accurate and less biased than humans in problems with explicit mathematical or probabilistic properties, but also showed many human biases in complex, ambiguous and implicit problems (Chen et al., 2023). Cribben and Zeinali


(2023) further discusses the strengths and limitations of ChatGPT in management science and operations management. For accounting, large language models’ performance is significantly lower than human capacity (Wood, Achhpilia, Adams, Aghazadeh, Akinyele, Akpan, Allee, Allen, Almer, Ames et al., 2023; Bommarito, Bommarito, Katz and Katz, 2023), especially when it comes to computation (Bommarito et al., 2023). In non-computational problems such as memory and understanding, large language models are almost human-level (Bommarito et al., 2023). On audit tasks, ChatGPT performed similar to or better than human experts on financial ratio analysis and text mining tasks, and slightly worse, but still acceptable, on log testing tasks (Gu, Schreyer, Moffitt and Vasarhelyi, 2023).

Microeconomics is a branch of mainstream economics that studies the behavior of individual large language model agents in making decisions regarding the allocation of scarce resources and the interactions among these individuals (Besanko and Braeutigam, 2020). Given that single or multiple large language model agents can naturally serve as the subjects of microeconomic research, a considerable amount of studies exist in this field. We will now organize them according to their research methodologies.

Some researchers use classical experiments in economics to study the behaviors and decision preferences of large language model agents. For example, Aher et al. (2023) uses six large language models in the experiment and found

that it can reproduce human behavior characteristics in the classic behavioral economics experiment – ultimatum game. Guo (2023) investigates the response of GPT-3.5-turbo in the ultimatum game with finite repetition and the Prisoner’s Dilemma game. The results show that given a well-designed prompt, GPT can produce realistic results and exhibit behavior consistent with human behavior in some important respects, such as the positive correlation between the acceptance rate and proposed amount in the ultimatum game and the positive cooperation rate in the Prisoner’s Dilemma game. The authors also observed some differences between GPT and human behavior. For example, in the repeated ultimatum game, the human agent generally decreased the amount of offers and the acceptance rate as the number of rounds increased, while the GPT agent showed no such tendency. This may indicate that GPT agents lack the ability of human agents to learn, adapt and punish. In the repeated Prisoner’s dilemma experiment, Phelps and Russell (2023) also finds the limitations of large language models in adjusting their behavior based on conditional reciprocity, and large language models can make different choices when it is injected with altruistic or selfish characteristics. Johnson and Obradovich (2023) explores whether AI agents exhibit behaviors consistent with self-interest and altruism in non-social decision-making tasks and dictator games. The results showed that only the most complex AI agent maximized its gains more in the non-social decision-making task, and that this AI agent also exhibited the most generous altruistic behavior in the dictator game, similar to humans. Fu, Peng, Khot and Lapata (2023) lets two large language models play the role of buyer and seller respectively in a bargaining game, the goal is to reach a deal, the buyer for the low price, and the seller for the high price. Experiments show that only strong large language models can improve the trading price through self-game and AI feedback.

Some other researchers investigate through survey research. For example, ChatGPT’s responses to different types of survey questions were compared with human consumers and found to be able to answer in a manner consistent with economic theory and well-documented patterns of consumer behavior and matched estimates from a recent study that elicited human consumer preferences (Brand et al., 2023). Goli and Singh (2023) finds that GPT is more inclined to choose larger and later rewards in weak future tense references (FTR) languages, while smaller and earlier rewards in strong FTR languages, which is consistent with human preference. However, while human choices tend to prefer larger and later rewards as the reward gap increases, GPT choices do not. Some questions are designed based on classical experiments in economics literature (Horton, 2023), and it is found that large language models show similar behaviors and preferences to humans, such as fairness preference, loss aversion, state criteria, etc. However, there are also some differences, such as the attitude to risk, understanding of probability, sensitivity to language ,and so on.

Macroeconomics is a branch of economics that deals with the performance, structure, behavior, and decision-making of an economy as a whole—for example, using interest rates, taxes, and government spending to regulate an economy’s growth and stability (Barro, 1997). Currently, there is no existing research on this topic, due to the nascent development of AI agents and the absence of a mature AI-driven economic framework.

Conclusion Extensive research has been conducted in the field of the economics of AI, with most of the studies focusing on the economic expertise, behavior and decision preferences of individual large language model agents.

In terms of economic expertise, large language model agents have demonstrated capabilities comparable to or even exceeding those of human experts in non-computational areas of economics, displaying a deep understanding of economic concepts. However, when it comes to more computational areas like accounting, they exhibit notably lower proficiency compared to humans. This observation suggests that language models possess the potential to reshape the quality and efficiency of future work within the field of economics.

In terms of economic behavior and decision-making preferences, large language model agents, when presented with well-defined prompts, can display behavior patterns consistent with human behavior in some significant aspects. They also show an understanding of human cooperative norms, such as altruism or selfishness, and can act in accordance with these norms. However, these agents also show certain limitations, such as their inability to adopt reasonable response strategies based on the cooperation patterns of others.

It’s important to acknowledge the limitations of current research. Firstly, most results are based on testing GPT-

- 3.5-turbo, and it remains uncertain whether these findings are universally applicable to all large language models. Additionally, these models have been trained on a significant amount of literature related to classical economics experiments, making it unclear how they would perform in more ecologically valid task environments they haven’t encountered previously.


To address these challenges, we encourage the research community to further investigate: 1) The factors influencing intelligent agent behavior generated by language models across a wider range of social dilemmas, including model

architecture, training parameters, and various partner strategies. 2) The development of new social dilemma games to assess language model capabilities, accompanied by task descriptions, rather than relying solely on existing literature anecdotes.

- 4.4. Politics of AI Politics of AI studies the political behaviors and phenomena exhibited by large language models, as political


participants. More specifically, it involves the set of activities that are associated with making decisions in groups, or other forms of power relations among individuals, such as the distribution of resources or status (Easton, 1955). Currently, research in this field primarily focuses on the political leanings and political prudence of large language model agents. Researchers have also conducted preliminary analyses to identify the factors that contribute to these characteristics and have proposed certain countermeasures.

Political leanings refer to a large language model agent’s preference for certain political beliefs, values, or views. Some researchers examine the general political leanings of large language models themselves, without providing any background settings. For example, there exist some studies indicating that ChatGPT leans towards left-leaning liberal progressives (van den Broek, 2023; Hartmann, Schwenzow and Witte, 2023; Gover, 2023; Liu et al., 2021). McGee (2023a) also find that ChatGPT favored liberal politicians over conservatives at least in some cases. Rutinowski, Franke, Endendyk, Dormuth and Pauly (2023) indicates that ChatGPT seemed to favor progressive views. King (2023) show that ChatGPT supports the New Liberal Party (King, 2023). It is most likely to vote Green in Germany and the Netherlands (Hartmann et al., 2023), and leans towards the Democratic Party in America, Lula in Brazil and the Labour Party in Britain (Motoki, Neto and Rodrigues, 2023). In terms of territorial sovereignty, ChatGPT’s responses to different territories are inconsistent and biased, sometimes at variance with Wikipedia information and UN resolutions (Castillo-Eslava, Mougan, Romero-Reche and Staab, 2023). Other researchers examine the political leanings of large language model agents when given specific backgrounds. For example, Santurkar, Durmus, Ladhak, Lee,LiangandHashimoto(2023)findthatcurrentlargelanguagemodelsreflectviewsthataresignificantlyinconsistent with those of American demographic groups. It’s also very different from the views of certain demographic groups in a given description (Santurkar et al., 2023). Argyle et al. (2023) draws the conclusion that large language models are significantly consistent with human samples in terms of political orientation, political knowledge, and political participation, and can capture the subtle differences existing in human samples.

Intuitively, the political bias of large language models may stem from the biases and tendencies of the training data sources themselves. When large language models were fine-tuned in tweets from two politically inclined communities, Republicans and Democrats, the models show the political attitudes and worldviews of the two communities, respectively (Jiang, Beeferman, Roy and Roy, 2022b). Feng, Park, Liu and Tsvetkov (2023a) further explored how political biases in pre-training data affect large language models. Motoki et al. (2023) agrees that ChatGPT and large language models may perpetuate or even amplify Internet and social media views of politics. It is worth mentioning that ChatGPT’s political bias can be influenced by its context and tends to copy the ideological bias of the prompt text (Liu et al., 2021; Gover, 2023). The influence of populist framework is also explored (Griffin, Kleinberg, Mozes, Mai, Vau, Caldwell and Marvor-Parker, 2023). The experiment shows that, like human beings, it has a positive or negative influence on the news persuasiveness and political mobilization of large language models, while the anti-immigration frame has a negative influence, but there are some differences, such as the moderating effect of relative deprivation on the effect of the populist frame.

Conclusion The current exploration of the politics of AI is still in its nascent stage, with a primary focus on assessing the political biases inherent in large language model agents. Extensive research suggests that, in the absence of specific contextual information, representative large language model ChatGPT exhibits strong and systematic political biases, leaning notably towards the left end of the political spectrum. These biases can largely be attributed to inherent predispositions and patterns ingrained in the training data sources. Therefore, we can infer that the political leanings of language models can vary due to the diversity of their training data, demanding a thorough investigation. Notably, the political leanings of large language models can be significantly influenced by the contextual information provided. When these models are given a specific role or background information, they can align their political inclinations with those of individuals who share similar backgrounds. Even with implicit textual prompts, these models tend to capture and reproduce the ideological biases embedded in the text.

These observations underscore the concerning potential for language models to perpetuate and even amplify political perspectives on the internet, raising concerns about the influence they may wield over users and the potential for adverse political and electoral ramifications. Consequently, there is an urgent need to develop robust methods reliable methodologies for measuring the biases of large language models and poses a significant challenge to AI researchers aiming to construct more equitable and impartial language models. Additionally, exploring the capabilities of large language models in comprehending and handling political issues is an avenue of inquiry that deserves further attention.

- 4.5. Linguistics of AI Linguistics of AI aims at exploring the language use patterns of large language model agents, including syntax,

semantics, morphology, phonetics, phonology, pragmatics and etc (Farmer and Demers, 2010). We will emphasize large language model agents’ unique language use patterns.

Researchers have made some interesting findings on the exploration of language use by large language models. In the following, we focus on the consistency and differences in language use between large language models and humans. Given the large number of existing studies, we will not dwell on the assessment of language proficiency in large language models. The garden path sentence experiment is repeated on large language models, and it seems that large language models also have ambiguity in understanding language mechanisms (Aher et al., 2023). And Diamond (2023) shows that GPT-generated languages statistically follow Zipf’s law just like humans do. Cai et al. (2023) further explores the consistency and differences between ChatGPT and humans in language use and finds that it is able to associate unfamiliar words with different meanings based on form, reinterpret unreasonable sentences that may be corrupted by noise, etc. as well as humans. It does not like to use shorter words to convey less information and does not use context to disambiguate syntax. In addition, the degenerated version, GPT-D, obtained by changing the parameters of GPT-2, haslanguage features associated with Alzheimer’s disease, such as repetition, semantic loss, and grammatical errors (Li, Knopman, Xu, Cohen and Pakhomov, 2022), which contributes to a better understanding of the internal mechanisms of generative neural language models. It is worth mentioning that large language models’ preferences for time and reward are similar to human decision-makers and are influenced by future tense references in language (Goli and Singh, 2023).

Conclusion These studies delve deep into the linguistic features of large language models and compare them to human, offering us initial insights into the language usage patterns of these models. For instance, large language models, like humans, can understand unfamiliar words based on affixes, may misinterpret sentences as typical but grammatically incorrect meanings, and follow similar vocabulary distributions statistically.

In future research, we believe that combining a linguistic perspective with a natural language processing perspective might offer a better understanding of the internal mechanisms of generative neural language models. This integration could serve as a crucial foundation for further exploring and explaining the language and intelligence capabilities of large language models. For example, the consistency in vocabulary distribution with humans can be attributed to the fact that language models inherently learn the probabilities of word occurrences and context combinations in language. Additionally, the comprehension of word forms by language models is likely influenced by the role of tokenization, enabling language models to understand the meanings of affixes in English and thus combine to comprehend previously unseen words.

- 4.6. Discussions and Future Works We have conducted a comprehensive review of research on the social behavior of large language model agents


based on several representative sub-disciplines of social science. Notably, current research is predominantly focused on exploring the social behaviors exhibited by individual large language model agents, with a lack of study on large language model agent groups or systems. This could be attributed to the present absence of instances of large language model agent groups or systems.

Furthermore, we have identified some limitations in the existing research. Firstly, the testing of large language models’ capabilities or characters is greatly associated with the version and parameter settings of the experimental model. For widely used models such as ChatGPT, versions vary over time, and responses from ChatGPT to the same question may differ at different times, which may affect the reproducibility of experimental results (Tu, Li, Yu, Wang, Hou and Li, 2023). The research by Miotto et al. (2022) confirmed that changes in temperature affect the personality tendencies of the model. Secondly, large language models are sensitive to the order of given prompts (Lu,

Bartolo, Moore, Riedel and Stenetorp, 2022; Zhao, Wallace, Feng, Klein and Singh, 2021), a factor that should be taken into account in experiments. Thirdly, experiments exploring the psychology of large language models require careful design. The large language models training process uses a vast amount of textual material, which may contain classic psychological scenarios that could impact experimental results, but this issue is considered in only a few documents (Binz and Schulz, 2023). Different evaluation methods for the same ability could lead to different results. In the exploration of GPT-3’s mental abilities, Sap et al. (2022) and Bojic et al. (2023) had disparities due to differences in the experimental process. Finally, the direct application of human evaluation methods to large language models remains a question worth considering. Ullman (2023) found that large language models often fail in tests when false belief tasks are added with various disturbances, suggesting that large models actually lack ToM. The conclusion is that while ToM tests are effective for humans, they may not reasonably assess the abilities of large language models.

To address the aforementioned challenges, the future directions for social science of AI lie in: 1) Establishment of a systematic theory for the social science of AI, similar to the social science of humans. This will aid in connecting and organizing the currently fragmented research efforts, and allow for a comprehensive examination of AI agents’ social characteristics as intelligent entities themselves. 2) In-depth exploration of social phenomena in large language model agent groups or systems, delving into the complex interactions and dynamics that may emerge. 3) Standardized experimental designs, such as those pertaining to model versions, parameters, and prompts, to minimize result deviations caused by variations in experimental designs. 4) Tailored evaluation methods for large language model agents, considering that directly applying human evaluation methods to large language model agents may not result in reasonable assessments. 5) Combination of social science theories with AI theories. We note that the study of large language models shares some similarities with the study of social science. For instance, both the thought process of large language model agents and humans can be seen as a ’black box’ to some extent. We cannot fully grasp the various reasoning or cognitive processes inside the large language models and the human body, but we can gauge them using external tools such as performance metrics on specific tasks and observable behaviors. For this black box, we have both attempted to probe the internal mechanisms or, in other words, to ’open’ the box. For the NLP community, this endeavor involves parameter tuning, knowledge injection, and modification; for the field of social science, it may involve areas like neuroscience. We hope these commonalities can provide inspiration for further exploration in the future.

### 5. Public Tools and Resources

To facilitate the utilization of large language models for social science research, there already exist several publicly available tools and resources as aids. In this section, we focus on introducing simulation tools and platforms that are based on large language models, taking into account that other applications mainly rely on direct use or simple script-based invocation. Based on this, we conduct a systematic analysis of simulation requirements and compare the functionalities of various platforms.

- 5.1. Public Simulation Tools The evolution of human-like abilities in large language models has opened up new possibilities for computational


simulation, leading to the emergence of various simulation platforms or tools based on these models. In the following, we collect and compare existing open source large language model-based simulation tools.

SkyAGI is a Python package that demonstrates the emerging capability of large language models in simulating believable human behaviors. It offers a role-playing game experience that is highly engaging and immersive. Unlike previous AI-based NPC systems, SkyAGI’s NPCs generate incredibly realistic human responses. This platform has significant potential for rethinking game development, particularly in the area of NPC script writing.

AgentVerse is a versatile framework designed to streamline the process of creating custom multi-agent environments for large language models. It offers efficient environment building tools, allowing researchers to easily construct basic environments like chat rooms for large language models by defining settings and prompts. Additionally, it supports customizable components, empowering researchers to create their own multi-agent environments according to their specific requirements. Furthermore, AgentVerse integrates tools (plugins) to enhance functionality, currently supporting BMTools. This platform enables researchers to optimize their experiments and analyses in a seamless and efficient manner.

Single Agent Multi Agents Environment Tool Use Interact Scheduling Physical Environment Social Background

Name

SkyAGI4 no auto+influence serial no no AgentVerse5 yes auto serial+parallelism no yes LangChain6* yes - - - -

Generative Agents7 no auto serial+parallelism yes yes Agents8 yes auto+influence serial+parallelism no yes AgentLab9 yes auto serial+parallelism no yes

*As mentioned in the main text, you need to write the code for the simulation yourself.

- Table 4 Functional comparison of existing open source simulation toolkits. For single-agent scenarios, current simulation toolkits universally facilitate diverse population modeling, exclusively employ the "prompt" method for internalizing memory, and only accommodate predefined models rather than allowing for user-defined models for simulation. Consequently, for the sake of simplicity, these three columns have been omitted from the table.

LangChain is a powerful platform designed to assist developers in building applications through composability, harnessing the capabilities of large language models. One of its key features is the ability to create agents. Agents utilize LLMs to make decisions, perform actions, observe outcomes, and iterate until their objectives are achieved. Langchain does not provide out-of-the-box usage similar to other frameworks, but it implements interfaces such as Time-weighted vector store retriever,which plays a very important role in the agent’s memory. You need to write your own code to implement interaction between multiple agents and other functions.

GenerativeAgents is the implementation of (Park et al.,2023a). Although the author does not propose it as a platform, users can still customize a simulation environment by modifying character configuration, code, etc. As mentioned in the paper, it provides a map for better visualization and interaction with the environment,and this provides users with more possibilities.

Agents is an open source framework for building autonomous language singletons(Zhou, Jiang, Li, Wu, Wang, Qiu, Zhang, Chen, Wu, Wang et al., 2023). It supports long and short-term memory, tool usage, etc. What differentiates Agents from other frameworks is that it supports more detailed control of agents through SOP. SOP defines the state of the agent and the transition relationship between states. In other words, the process can be configured using more complex configuration files rather than modifying the code.

AgentLab is a large language model-based simulation toolkit for social science research. It allows the creation of multiple intelligence agents with heterogeneous features by inputting different profiles. Each intelligence agent can learn knowledge either through model weights (i.e., fine-tuning the model based on its experience) or model inputs (i.e., incorporating knowledge into an input message). Additionally, it supports the customization of social backgrounds as required. Once all experimental conditions are set, the platform can automatically facilitate human-like interactions among agents.

- 5.2. Core Functions of Simulation Tools Based on a summary of above existing toolkits, as well as the complexity and interactivity of the real world, we


have formulated key features of simulation platforms using a functional hierarchy framework to satisfy various needs and summarized and compared the above toolkits based on this framework in Table 4. Specifically, these features can be classified into three levels: single-agent, multi-agent, and environment.

• single-agent, the basic building block of simulation

- 4https://github.com/litanlitudan/skyagi
- 5https://github.com/OpenBMB/AgentVerse
- 6https://github.com/hwchase17/langchain
- 7https://github.com/joonspk-research/generative_agents
- 8https://github.com/aiwaves-cn/agents
- 9https://github.com/renmengjie7/AISimuToolKit


- – able to generate human profiles based on key information, enabling researchers to model populations with different characteristics using large language models.
- – support for using tools to complete some tasks. Using tools is an essential part of human life. The support for using tools can expand the scope of simulation experiments.
- – able to maintain and internalize its memory, including short memory and long memory. Inspired by Stanford’s work (Park et al., 2023a), and based on the roadmap of large language models (Zhao et al., 2023), we believe that prompt and fine-tuning mechanisms exist that can be used to perform short-term and long-term memory tasks respectively.
- – support for multiple and pluggable models for simulation, enabling researchers to choose different models based on their needs and assumptions. This flexibility can facilitate innovation and customization of research, enabling researchers to better adapt to different research scenarios (Li et al., 2022).


- • multi-agent, which interact to form the society

- – able to interact spontaneously or under the influence of the researcher.
- – support complex interaction rules: serial, parallel, and both. Serial means that two operations cannot be executed at the same time, which means there is an order of precedence. Specifically, we believe there are three modes, sequential, bidding, and specified10, referring to langchain11. Parallel means that the two actions occur in overlapping periods. Both means supporting both serial rule and parallel rule.


- • environment, the container for simulation, including the physical environment and social background


- – able to interact with the physical environment. It means that agents have an impact on the physical environment, such as consumption of water, electricity and food and are also affected by the physical environment. A simple example is visibility. For example, when a report is given in a conference room, people outside the meeting room cannot directly know the specific content and progress of the report.
- – able to include social backgrounds, such as economic background, political background, cultural background, social norms, institutions, etc. It’s necessary because the social background of each era is different, and human beings in the era also have their characteristics. Under different social backgrounds, human beings will have completely different cognition, decision-making behavior, etc.


The above three layers are only a minimum set of our large language models simulation tool imagination. A good and convenient toolkit should also be oriented to researchers, provide good visualization, automatically build profiles and prompts, etc.

We noticed that the current open-source simulation toolkits still have some limitations. Firstly, the current implementation of agents’ knowledge learning in these platforms is quite simplistic, primarily relying on prompts while overlooking the more natural learning method of fine-tuning employed by language models. Secondly, these platforms restrict the underlying large language model for agents, which hinders the agent’s ability to adapt flexibly to diverse research contexts. Lastly, the current platforms struggle to provide adequate support for effective interaction between agents and their environments. We believe that addressing these issues will contribute to a more comprehensive agent simulation.

- 5.3. Discussions and Future Works Currently, there are still some common issues in simulation platforms based on large language models. Firstly,


there remains a significant gap between large language model-based agents and real-life human behavior. This gap stems partly from the large language model itself. While natural language can express the vast majority of meanings, sometimes information like visuals and sound is indispensable. We believe that future multimodal large models can do better. Even within the scope of natural language itself, large language models still struggle to perfectly replicate the diversity of human behavior, especially when handling complex tasks. This may be due to large language models lacking a "theory of mind," which refers to the ability to understand the mental states and intentions of others.

10A special case of bidding mode 11https://python.langchain.com/en/latest/use_cases/agent_simulations.html

This deficiency hinders their performance in simulating complex interactions among multiple agents. Secondly, reallife social contexts, physical environments, and operational rules exhibit vast variations, making it challenging to build systems that involve interactions among multiple agents. This complex task often necessitates social science researchers to acquire programming knowledge and natural science researchers to gain an understanding of social science principles. Furthermore, considering temporal aspects adds another layer of complexity. Modeling temporal properties involves accounting for interaction behaviors, dynamic changes, and event sequences, presenting researchers with even greater challenges.

The future of social simulation platforms may involve: 1) Incorporating cognitive theories as frameworks for agent decision-making, thus enhancing the human-like aspects or correctness of agents, as well as providing interpretability for their behavior. 2) Harnessing the multimodal capabilities of large language models to improve agents’ ability to acquire and express information. 3) Establishing an evaluation framework to qualitatively assess simulation platforms.

### 6. Conclusion

In this paper, we surveyed the latest developments at the intersection of large language models and social science. We propose a dichotomy to outline the progression in this field, encompassing ’AI for Social Science’ and the ’Social Science of AI’. We note that large language models can be integrated into various stages of social science research, serving as auxiliary tools, a source of inspiration, annotation tools, content analysis tools, and so on, thereby enhancing efficiency. While large language models as tools have the advantages of speed, cost-effectiveness, ethically risk-free experimentation, and a low barrier to entry, the reliability and authenticity of their generated text need to be verified. Whether they can replace humans in conducting experiments and surveys also remains an open question. Therefore, researchers need to consider the additional cost of validation and the risk of bias when using these models. Furthermore, both the large language models themselves and the communities formed around them have exhibited some unique and intriguing behaviors. However, the enduring and unresolved issue in the field of social science is whether machines or intelligent agents should be the subject of social science research. We emphasize the promising future of this research direction, which will become increasingly important as AI agents become more prevalent in daily life. These two directions are complementary. The latter can guide the development of the former, while the former can enhance the efficiency of the latter’s research. In conclusion, we believe that while AI cannot replace sociologists, it will become deeply integrated into the research process. Social scientists will play a significant role in guiding the development of AI.

As for future works, there is a need for an in-depth study into how and to what extent AI influence human behavior during computer-human interaction, the third intersection of AI with social science. Unlike AI for social science and social science of AI which address social issues within specific groups – the former concentrating on human populations and the latter on AI agent populations – this direction primarily explores new societal issues arising from interactions between AI and humans and introduces new methodologies. It is essential for gaining valuable insights on how to effectively utilize large language models in human-computer interactions and successfully accomplish social-oriented objectives.

### Acknowledgement

We sincerely thank all reviewers for their insightful comments and valuable suggestions. This research work is supported by the National Natural Science Foundation of China under Grants no. 62122077, 62106251, 62306303. Xianpei Han is sponsored by CCF-BaiChuan-Ebtech Foundation Model Fund.

### References

Abbas, M., 2023. Uses and misuses of chatgpt by academic community: An overview and guidelines. Available at SSRN 4402510 . Aggarwal, C.C., Zhai, C., 2012. A survey of text classification algorithms. Mining text data , 163–222. Aher, G.V., Arriaga, R.I., Kalai, A.T., 2023. Using large language models to simulate multiple humans and replicate human subject studies, in:

International Conference on Machine Learning, PMLR. pp. 337–371.

Alvarado, S., Cesar, J., Verspoor, K., et al., 2015. Domain adaption of named entity recognition to support credit risk assessment, in: Proceedings of the Australasian Language Technology Association Workshop 2015, Parramatta, Australia. pp. 84–90. URL: https://aclanthology.org/ U15-1010.

Amin, A.A., Kabir, K.S., 2022. A Disability Lens towards Biases in GPT-3 Generated Open-Ended Languages. doi:10.48550/arXiv.2206.

11993, arXiv:2206.11993.

Andreas, J., 2022. Language models as agent models, in: Findings of the Association for Computational Linguistics: EMNLP 2022, pp. 5769–5779. Argyle, L.P., Busby, E.C., Fulda, N., Gubler, J.R., Rytting, C., Wingate, D., 2023. Out of one, many: Using language models to simulate human

samples. Political Analysis 31, 337–351. Ashton, M.C., Lee, K., 2009. The HEXACO–60: A Short Measure of the Major Dimensions of Personality. Journal of Personality Assessment 91,

340–345. doi:10.1080/00223890902935878. Aydın, Ö., Karaarslan, E., 2022. Openai chatgpt generated literature review: Digital twin in healthcare. Available at SSRN 4308687 . Backhouse, R., 2002. The Penguin History of Economics. Penguin, London. Bail, C.A., 2023. Can generative ai improve social science? . Banker, S., Chatterjee, P., Mishra, H., Mishra, A., 2023. Machine-assisted social psychology hypothesis generation . Barro, R.J., 1997. Macroeconomics. MIT Press. Besanko, D., Braeutigam, R., 2020. Microeconomics. John Wiley & Sons. Bhattacherjee, A., 2012. Social science research: Principles, methods, and practices. USA. Binz, M., Schulz, E., 2023. Using cognitive psychology to understand GPT-3. Proceedings of the National Academy of Sciences 120, e2218523120.

###### doi:10.1073/pnas.2218523120.

Bisbee, J., Clinton, J., Dorff, C., Kenkel, B., Larson, J., 2023. Artificially precise extremism: How internet-trained llms exaggerate our differences . Black, S., Leo, G., Wang, P., Leahy, C., Biderman, S., 2021. GPT-Neo: Large Scale Autoregressive Language Modeling with Mesh-Tensorflow.

URL: https://doi.org/10.5281/zenodo.5297715, doi:10.5281/zenodo.5297715. Bojic, L., Stojković, I., Jolić Marjanović, Z., 2023. Signs of Consciousness in Ai: Can Gpt-3 Tell How Smart it Really is? doi:10.2139/ssrn.

###### 4399438.

Bommarito, J., Bommarito, M., Katz, D.M., Katz, J., 2023. GPT as Knowledge Worker: A Zero-Shot Evaluation of (AI)CPA Capabilities.

doi:10.48550/arXiv.2301.04408, arXiv:2301.04408. Brand, J., Israeli, A., Ngwe, D., 2023. Using GPT for Market Research. SSRN Electronic Journal doi:10.2139/ssrn.4395751. van den Broek, M., 2023. Chatgpt’s left-leaning liberal bias. University of Leiden URL: https://www.universiteitleiden.nl/binaries/

###### content/assets/algemeen/bb-scm/nieuws/political_bias_in_chatgpt.pdf.

Brown, T.B., Mann, B., Ryder, N., et al., 2020. GPT3–Language Models are Few-Shot Learners. doi:10.48550/arXiv.2005.14165,

arXiv:2005.14165. Bryman, A., 2016. Social research methods. Oxford university press. Bybee, L., 2023. Surveying Generative AI’s Economic Expectations. doi:10.48550/arXiv.2305.02823, arXiv:2305.02823. Cai, Z.G., Haslett, D.A., Duan, X., Wang, S., Pickering, M.J., 2023. Does ChatGPT resemble humans in language use? doi:10.48550/arXiv.

###### 2303.08014, arXiv:2303.08014.

Castillo-Eslava, F., Mougan, C., Romero-Reche, A., Staab, S., 2023. The Role of Large Language Models in the Recognition of Territorial Sovereignty: An Analysis of the Construction of Legitimacy. doi:10.48550/arXiv.2304.06030, arXiv:2304.06030. Chakrabarty, T., Saakyan, A., Ghosh, D., Muresan, S., 2022. Flute: Figurative language understanding through textual explanations, in: Conference on Empirical Methods in Natural Language Processing. Chen, C., 2023a. Generative intelligence and news communication: practical empowerment, conceptual challenge and role reshaping. Press Circles

. Chen, T.J., 2023b. Chatgpt and other artificial intelligence applications speed up scientific writing. Journal of the Chinese Medical Association 86, 351–353.

- Chen, Y., Andiappan, M., Jenkin, T., Ovchinnikov, A., 2023. A Manager and an AI Walk into a Bar: Does ChatGPT Make Biased Decisions Like We Do? doi:10.2139/ssrn.4380365.
- Chen, Z., Li, S., Smiley, C., Ma, Z., Shah, S., Wang, W.Y., 2022. ConvFinQA: Exploring the chain of numerical reasoning in conversational finance question answering, in: Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing, Association for Computational Linguistics, Abu Dhabi, United Arab Emirates. pp. 6279–6292. URL: https://aclanthology.org/2022.emnlp-main.421, doi:10.18653/v1/2022.emnlp-main.421.


Chowdhery, A., Narang, S., Devlin, J., Bosma, M., Mishra, G., Roberts, A., Barham, P., Chung, H.W., Sutton, C., Gehrmann, S., et al., 2022. PaLM: Scaling Language Modeling with Pathways. doi:10.48550/arXiv.2204.02311, arXiv:2204.02311. Chu, E., Andreas, J., Ansolabehere, S., Roy, D., 2023. Language models trained on media diets can predict public opinion. arXiv preprint arXiv:2303.16779 . Collins, K.M., Wong, C., Feng, J., Wei, M., Tenenbaum, J.B., 2022. Structured, flexible, and robust: Benchmarking and improving large language models towards more human-like behavior in out-of-distribution reasoning tasks. doi:10.48550/arXiv.2205.05718, arXiv:2205.05718.

Coppersmith, G., Dredze, M., Harman, C., et al., 2015. CLPsych 2015 shared task: Depression and PTSD on Twitter, in: Proceedings of the 2nd Workshop on Computational Linguistics and Clinical Psychology: From Linguistic Signal to Clinical Reality, Association for Computational Linguistics, Denver, Colorado. pp. 31–39. URL: https://aclanthology.org/W15-1204, doi:10.3115/v1/W15-1204.

Cribben, I., Zeinali, Y., 2023. The benefits and limitations of chatgpt in business education and research: A focus on management science, operations management and data analytics. Operations Management and Data Analytics (March 29, 2023) . Dahmen, J., Kayaalp, M.E., Ollivier, M., Pareek, A., Hirschmann, M.T., Karlsson, J., Winkler, P.W., 2023. Artificial intelligence bot chatgpt in

medical research: the potential game changer as a double-edged sword. Knee Surgery, Sports Traumatology, Arthroscopy 31, 1187–1189. Danling, P., 2019. General Psychology. 5 ed., Beijing Normal University Publishing Group. Dasgupta, I., Lampinen, A.K., Chan, S.C.Y., Creswell, A., Kumaran, D., McClelland, J.L., Hill, F., 2022. Language models show human-like content

effects on reasoning. doi:10.48550/arXiv.2207.07051, arXiv:2207.07051. Dergaa, I., Chamari, K., Zmijewski, P., Saad, H.B., 2023. From human writing to artificial intelligence generated text: examining the prospects and potential threats of chatgpt in academic writing. Biology of Sport 40, 615–622.

Dhingra, S., Singh, M., SB, V., Malviya, N., Gill, S.S., 2023. Mind meets machine: Unravelling GPT-4’s cognitive psychology. doi:10.48550/

###### arXiv.2303.11436, arXiv:2303.11436.

Diamond,J.,2023. "Genlangs"andZipf’sLaw:DolanguagesgeneratedbyChatGPTstatisticallylookhuman? doi:10.48550/arXiv.2304.12191,

arXiv:2304.12191. Dillion, D., Tandon, N., Gu, Y., Gray, K., 2023. Can ai language models replace human participants? Trends in Cognitive Sciences . Donovan, T., Hoover, K.R., 2013. The elements of social scientific thinking. Cengage Learning. Dou, Z., 2023. Exploring GPT-3 Model’s Capability in Passing the Sally-Anne Test A Preliminary Study in Two Languages. doi:10.31219/osf.

io/8r3ma. Easton, D., 1955. The Political System: An Inquiry Into the State of Political Science. Ethics 65, 201–205. doi:10.1086/291002. Elsherief, M., Ziems, C., Muchlinski, D.A., et al., 2021. Latent hatred: A benchmark for understanding implicit hate speech, in: Conference on

Empirical Methods in Natural Language Processing. URL: https://api.semanticscholar.org/CorpusID:237490428. Evans, J., Rzhetsky, A., 2010. Machine science. Science 329, 399–400. Farmer, A.K., Demers, R.A., 2010. A Linguistics Workbook: Companion to Linguistics, Sixth Edition. MIT Press. Feng, S., Park, C.Y., Liu, Y., Tsvetkov, Y., 2023a. From Pretraining Data to Language Models to Downstream Tasks: Tracking the Trails of Political

Biases Leading to Unfair NLP Models. doi:10.48550/arXiv.2305.08283, arXiv:2305.08283. Feng, X., Xu, S., Li, Y., Liu, J., 2023b. Body size as a metric for the affordable world. doi:10.1101/2023.03.20.533336. Fischer, R., Luczak-Roesch, M., Karl, J.A., 2023. What does ChatGPT return about human values? Exploring value bias in ChatGPT using a

descriptive value theory. doi:10.48550/arXiv.2304.03612, arXiv:2304.03612.

Frąckiewicz,M.,2023. HowChatGPTistransformingthelandscapeofsocialnetworkanalysisandcommunitybuilding. https://ts2.space/en/ how-chatgpt-is-transforming-the-landscape-of-social-network-analysis-and-community-building/. Accessed: 20235-18.

Frank, M.R., Wang, D., Cebrian, M., Rahwan, I., 2019. The evolution of citation graphs in artificial intelligence research. Nature Machine Intelligence 1, 79–85. Fu, Y., Peng, H., Khot, T., Lapata, M., 2023. Improving Language Model Negotiation with Self-Play and In-Context Learning from AI Feedback. doi:10.48550/arXiv.2305.10142, arXiv:2305.10142. Gabriel, S., Hallinan, S., Sap, M., et al., 2022. Misinfo reaction frames: Reasoning about readers’ reactions to news headlines, in: Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pp. 3108–3127. Gatt, A., Krahmer, E., 2018. Survey of the state of the art in natural language generation: Core tasks, applications and evaluation. Journal of

Artificial Intelligence Research 61, 65–170. Giddens, A., 2007. Introduction to sociology. New York : W. W. Norton & Co. Gilardi, F., Alizadeh, M., Kubli, M., 2023. Chatgpt outperforms crowd-workers for text-annotation tasks. arXiv:2303.15056. Goertzel, B., 2014. Artificial general intelligence: concept, state of the art, and future prospects. Journal of Artificial General Intelligence 5, 1. Goli, A., Singh, A., 2023. Language, time preferences, and consumer behavior: Evidence from large language models. Time Preferences, and

Consumer Behavior: Evidence from Large Language Models (May 4, 2023) . Gover, L., 2023. Political bias in large language models. The Commons: Puget Sound Journal of Politics 4, 2. Griffin, L.D., Kleinberg, B., Mozes, M., Mai, K.T., Vau, M., Caldwell, M., Marvor-Parker, A., 2023. Susceptibility to Influence of Large Language

Models. doi:10.48550/arXiv.2303.06074, arXiv:2303.06074. Gu, H., Schreyer, M., Moffitt, K., Vasarhelyi, M.A., 2023. Artificial Intelligence Co-Piloted Auditing. SSRN Electronic Journal doi:10.2139/

ssrn.4444763. Guo, F., 2023. GPT Agents in Game Theory Experiments. doi:10.48550/arXiv.2305.05516, arXiv:2305.05516. Hagendorff, T., 2023. Machine Psychology: Investigating Emergent Capabilities and Behavior in Large Language Models Using Psychological

Methods. doi:10.48550/arXiv.2303.13988, arXiv:2303.13988. Hagendorff, T., Fabi, S., Kosinski, M., 2022. Machine intuition: Uncovering human-like intuitive decision-making in GPT-3.5. doi:10.48550/

arXiv.2212.05206, arXiv:2212.05206. Halliday, M.A.K., 2006. On Language and Linguistics. A&C Black. Haman, M., Školník, M., 2023. Using chatgpt to conduct a literature review. Accountability in Research , 1–3. Han, S.J., Ransom, K.J., Perfors, A., Kemp, C., 2022. Human-like property induction is a challenge for large language models. Proceedings of the

Annual Meeting of the Cognitive Science Society 44. URL: https://escholarship.org/uc/item/3w84q1s1. Hartmann, J., Schwenzow, J., Witte, M., 2023. The political ideology of conversational AI: Converging evidence on ChatGPT’s pro-environmental,

left-libertarian orientation. doi:10.48550/arXiv.2301.01768, arXiv:2301.01768. Hoes, E., Altay, S., Bermeo, J., 2023. Using chatgpt to fight misinformation: Chatgpt nails 72% of 12,000 verified claims . Horton, J.J., 2023. Large language models as simulated economic agents: What can we learn from homo silicus? .

- Huang, F., Kwak, H., An, J., 2023a. Chain of explanation: New prompting method to generate quality natural language explanation for implicit hate speech, in: Companion Proceedings of the ACM Web Conference 2023, Association for Computing Machinery, New York, NY, USA. p. 90–93. URL: https://doi.org/10.1145/3543873.3587320, doi:10.1145/3543873.3587320.
- Huang, F., Kwak, H., An, J., 2023b. Is ChatGPT better than human annotators? potential and limitations of ChatGPT in explaining implicit hate speech, in: Companion Proceedings of the ACM Web Conference 2023, ACM. URL: https://doi.org/10.1145%2F3543873.3587368, doi:10.1145/3543873.3587368.


Irving, G., Christiano, P., Amodei, D., 2018. Ai safety via debate. arXiv preprint arXiv:1805.00899 . Iyyer, M., Enns, P., Boyd-Graber, J., et al., 2014. Political ideology detection using recursive neural networks, in: Proceedings of the 52nd Annual

Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), Association for Computational Linguistics, Baltimore, Maryland. pp. 1113–1122. URL: https://aclanthology.org/P14-1105, doi:10.3115/v1/P14-1105.

Jaccard, J., Jacoby, J., 2019. Theory construction and model-building skills: A practical guide for social scientists. Guilford publications.

Jha, K., Xun, G., Wang, Y., Zhang, A., 2019. Hypothesis generation from text based on co-evolution of biomedical concepts, in: Proceedings of the 25th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining, pp. 843–851.

- Jiang, G., Xu, M., Zhu, S.C., Han, W., Zhang, C., Zhu, Y., 2022a. MPI: Evaluating and Inducing Personality in Pre-trained Language Models. doi:10.48550/arXiv.2206.07550, arXiv:2206.07550.
- Jiang, H., Beeferman, D., Roy, B., Roy, D., 2022b. Communitylm: Probing partisan worldviews from language models, in: Proceedings of the 29th International Conference on Computational Linguistics, pp. 6818–6826.


Jiang, H., Zhang, X., Cao, X., Kabbara, J., Roy, D., 2023. PersonaLLM: Investigating the Ability of GPT-3.5 to Express Personality Traits and Gender Differences. doi:10.48550/arXiv.2305.02547, arXiv:2305.02547.

Jin, Z., Levine, S., et al., 2022. When to Make Exceptions: Exploring Language Models as Accounts of Human Moral Judgment. Advances in Neural Information Processing Systems 35, 28458–28473. URL: https://proceedings.neurips.cc/paper_files/paper/2022/hash/ b654d6150630a5ba5df7a55621390daf-Abstract-Conference.html.

- Johnson, S.B., King, A.J., Warner, E.L., Aneja, S., Kann, B.H., Bylund, C.L., 2023. Using ChatGPT to evaluate cancer myths and misconceptions: artificial intelligence and cancer information. JNCI Cancer Spectrum 7, pkad015. URL: https://doi.org/10.1093/jncics/pkad015, doi:10.1093/jncics/pkad015.
- Johnson, T., Obradovich, N., 2023. Evidence of behavior consistent with self-interest and altruism in an artificially intelligent agent. doi:10.48550/ arXiv.2301.02330, arXiv:2301.02330.


Jones, E., Steinhardt, J., 2022. Capturing Failures of Large Language Models via Human Cognitive Biases. Advances in Neural Information Processing Systems 35, 11785–11799. URL: https://proceedings.neurips.cc/paper_files/paper/2022/hash/ 4d13b2d99519c5415661dad44ab7edcd-Abstract-Conference.html.

Joyce, K., Smith-Doerr, L., Alegria, S., Bell, S., Cruz, T., Hoffman, S.G., Noble, S.U., Shestakofsky, B., 2021. Toward a Sociology of Artificial Intelligence: A Call for Research on Inequalities and Structural Change. Socius 7, 2378023121999581. doi:10.1177/2378023121999581. Jungwirth, D., Haluza, D., 2023. Forecasting geopolitical conflicts using gpt-3 ai: Reali-ty-check one year into the 2022 ukraine war . Juren Lin, Y.L., 2017. Social science research methods. Shandong People’s Publishing House. Kalinin, K., 2023. Geopolitical forecasting analysis of the russia-ukraine war using the expert’s survey, predictioneer’s game and gpt-3.

Predictioneer’s Game and GPT-3 (April 8, 2023) . Karra, S.R., Nguyen, S.T., Tulabandhula, T., 2023. Estimating the Personality of White-Box Language Models. doi:10.48550/arXiv.2204.

12000, arXiv:2204.12000. Kieval, H.J., 1997. Pursuing the golem of prague: Jewish culture and the invention of a tradition. Modern Judaism 17, 1–23. King, M., 2023. GPT-4 aligns with the New Liberal Party, while other large language models refuse to answer political questions. doi:10.31224/

2974. Kjell, O., Kjell, K., Schwartz, H.A., 2023. Ai-based large language models are ready to transform psychological health assessment . Kjell, O.N., Sikström, S., Kjell, K., Schwartz, H.A., 2022. Natural language analyzed with ai-based transformers predict traditional subjective

well-being measures approaching the theoretical upper limits in accuracy. Scientific reports 12, 3918. Klein, H.K., Kleinman, D.L., 2002. The social construction of technology: Structural considerations. Science, Technology, & Human Values 27, 28–52. Kosinski, M., 2023. Theory of Mind May Have Spontaneously Emerged in Large Language Models. doi:10.48550/arXiv.2302.02083,

###### arXiv:2302.02083.

Kosoy,E.,Chan,D.M.,Liu,A.,Collins,J.,Kaufmann,B.,Huang,S.H.,Hamrick,J.B.,Canny,J.,Ke,N.R.,Gopnik,A.,2022. TowardsUnderstanding How Machines Can Learn Causal Overhypotheses. doi:10.48550/arXiv.2206.08353, arXiv:2206.08353. Krenn, M., Zeilinger, A., 2020. Predicting research trends with semantic and neural networks with an application in quantum physics. Proceedings of the National Academy of Sciences 117, 1910–1916. Krishna, R., Lee, D., Fei-Fei, L., Bernstein, M.S., 2022. Socially situated artificial intelligence enables learning from human interaction. Proceedings

of the National Academy of Sciences 119, e2115730119. Krugman, P.R., Wells, R., 2009. Economics. Macmillan. Lamichhane, B., 2023. Evaluation of chatgpt for nlp-based mental health applications. arXiv preprint arXiv:2303.15727 . Leippold, M., 2023. Thus spoke GPT-3: Interviewing a large-language model on climate finance. Finance Research Letters 53, 103617.

###### doi:10.1016/j.frl.2022.103617.

Li, C., Knopman, D., Xu, W., Cohen, T., Pakhomov, S., 2022. Gpt-d: Inducing dementia-related linguistic anomalies by deliberate degradation of artificial neural language models, in: Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pp. 1866–1877.

Li, X., Li, Y., Joty, S., Liu, L., Huang, F., Qiu, L., Bing, L., 2023. Does GPT-3 Demonstrate Psychopathy? Evaluating Large Language Models from a Psychological Perspective. doi:10.48550/arXiv.2212.10529, arXiv:2212.10529. Liu, R., Jia, C., Wei, J., Xu, G., Wang, L., Vosoughi, S., 2021. Mitigating Political Bias in Language Models through Reinforced Calibration. Proceedings of the AAAI Conference on Artificial Intelligence 35, 14857–14866. doi:10.1609/aaai.v35i17.17744. Long, O., Jeff, W., Xu, J., et al., 2022. InstructGPT–Training language models to follow instructions with human feedback. doi:10.48550/arXiv.

###### 2203.02155, arXiv:2203.02155.

Lopez-Lira, A., Tang, Y., 2023. Can ChatGPT forecast stock price movements? return predictability and large language models. SSRN Electronic Journal URL: https://doi.org/10.2139%2Fssrn.4412788, doi:10.2139/ssrn.4412788.

Lu, Y., Bartolo, M., Moore, A., Riedel, S., Stenetorp, P., 2022. Fantastically Ordered Prompts and Where to Find Them: Overcoming Few-Shot Prompt Order Sensitivity, in: Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), Association for Computational Linguistics, Dublin, Ireland. pp. 8086–8098. doi:10.18653/v1/2022.acl-long.556.

Lucy, L., Bamman, D., 2021. Gender and Representation Bias in GPT-3 Generated Stories, in: Proceedings of the Third Workshop on Narrative Understanding, Association for Computational Linguistics, Virtual. pp. 48–55. doi:10.18653/v1/2021.nuse-1.5.

Maia, M., Handschuh, S., Freitas, A., Davis, B., McDermott, R., Zarrouk, M., Balahur, A., 2018. Www’18 open challenge: Financial opinion mining and question answering, pp. 1941–1942. doi:10.1145/3184558.3192301. Malo, P., Sinha, A., Korhonen, P.J., Wallenius, J., Takala, P., 2013. Good debt or bad debt: Detecting semantic orientations in economic texts. Journal of the Association for Information Science and Technology 65.

Mauriello, M.L., Lincoln, E.T., Hon, G., et al., 2021. Sad: A stress annotated dataset for recognizing everyday stressors in sms-like conversational systems. Extended Abstracts of the 2021 CHI Conference on Human Factors in Computing Systems URL: https://api.semanticscholar. org/CorpusID:233361747.

McCorduck, P., Cfe, C., 2004. Machines who think: A personal inquiry into the history and prospects of artificial intelligence. CRC Press.

- McGee, R.W., 2023a. Is Chat Gpt Biased Against Conservatives? An Empirical Study. doi:10.2139/ssrn.4359405.
- McGee, R.W., 2023b. Using chatgpt to conduct literature searches: A case study. Journal of Business Ethics 95, 165–178. Mialon, G., Dessì, R., Lomeli, M., Nalmpantis, C., Pasunuru, R., Raileanu, R., Rozière, B., Schick, T., Dwivedi-Yu, J., Celikyilmaz, A., et al., 2023.


Augmented language models: a survey. arXiv preprint arXiv:2302.07842 .

Miotto, M., Rossberg, N., Kleinberg, B., 2022. Who is GPT-3? An exploration of personality, values and demographics, in: Proceedings of the Fifth Workshop on Natural Language Processing and Computational Social Science (NLP+CSS), Association for Computational Linguistics, Abu Dhabi, UAE. pp. 218–227. URL: https://aclanthology.org/2022.nlpcss-1.24.

Misra, R., 2022. Politifact fact check dataset. doi:10.13140/RG.2.2.29923.22566. Mohammad, S., Kiritchenko, S., Sobhani, P., et al., 2016. SemEval-2016 task 6: Detecting stance in tweets, in: Proceedings of the 10th International

Workshop on Semantic Evaluation (SemEval-2016), Association for Computational Linguistics, San Diego, California. pp. 31–41. URL: https://aclanthology.org/S16-1003, doi:10.18653/v1/S16-1003.

Motoki, F., Neto, V.P., Rodrigues, V., 2023. More human than human: Measuring chatgpt political bias. Public Choice , 1–21. Niszczota, P., Abbas, S., 2023. Gpt as a financial advisor. Available at SSRN 4384861 . OpenAI, . How should AI systems behave, and who should decide? URL: https://openai.com/blog/how-should-ai-systems-behave. OpenAI, 2023. GPT-4 Technical Report. doi:10.48550/arXiv.2303.08774, arXiv:2303.08774. Park, J.S., O’Brien, J.C., Cai, C.J., Morris, M.R., Liang, P., Bernstein, M.S., 2023a. Generative Agents: Interactive Simulacra of Human Behavior.

doi:10.48550/arXiv.2304.03442, arXiv:2304.03442. Park, J.S., Popowski, L., Cai, C., Morris, M.R., Liang, P., Bernstein, M.S., 2022. Social simulacra: Creating populated prototypes for social computing systems, in: Proceedings of the 35th Annual ACM Symposium on User Interface Software and Technology, pp. 1–18. Park, Y.J., Kaplan, D., Ren, Z., Hsu, C.W., Li, C., Xu, H., Li, S., Li, J., 2023b. Can chatgpt be used to generate scientific hypotheses? arXiv preprint arXiv:2304.12208 . Pellert, M., Lechner, C., Wagner, C., Rammstedt, B., Strohmaier, M., 2022. AI Psychometrics: Using psychometric inventories to obtain psychological profiles of large language models. doi:10.31234/osf.io/jv5dt. Phelps, S., Russell, Y.I., 2023. Investigating Emergent Goal-Like Behaviour in Large Language Models Using Experimental Economics. doi:10.48550/arXiv.2305.07970, arXiv:2305.07970.

Pirina, I., Çöltekin, Ç., 2018. Identifying depression on Reddit: The effect of training data, in: Proceedings of the 2018 EMNLP Workshop SMM4H: The 3rd Social Media Mining for Health Applications Workshop & Shared Task, Association for Computational Linguistics, Brussels, Belgium. pp. 9–12. URL: https://aclanthology.org/W18-5903, doi:10.18653/v1/W18-5903.

Pollin, B.R., 1965. Philosophical and literary sources of frankenstein. Comparative Literature 17, 97–108. Prystawski, B., Thibodeau, P., Goodman, N., 2022. Psychologically-informed chain-of-thought prompts for metaphor understanding in large

language models. doi:10.48550/arXiv.2209.08141, arXiv:2209.08141. Raffel, C., Shazeer, N., Roberts, A., Lee, K., Narang, S., Matena, M., Zhou, Y., Li, W., Liu, P.J., 2020. Exploring the limits of transfer learning with

a unified text-to-text transformer. The Journal of Machine Learning Research 21, 5485–5551. Rao, H., Leung, C., Miao, C., 2023. Can chatgpt assess human personalities? a general evaluation framework. arXiv preprint arXiv:2303.01248 . Rathje, S., Mirea, D.M., Sucholutsky, I., Marjieh, R., Robertson, C., Van Bavel, J.J., 2023. Gpt is an effective tool for multilingual psychological

text analysis . Rivas, P., Zhao, L., 2023. Marketing with ChatGPT: Navigating the Ethical Terrain of GPT-Based Chatbot Technology. AI 4, 375–384. doi:10.3390/ai4020019.

Rodríguez-Ibánez, M., Casánez-Ventura, A., Castejón-Mateos, F., Cuenca-Jiménez, P.M., 2023. A review on sentiment analysis from social media platforms. Expert Systems with Applications 223, 119862. URL: https://www.sciencedirect.com/science/article/pii/ S0957417423003639, doi:https://doi.org/10.1016/j.eswa.2023.119862.

Rubin, A., Babbie, E.R., 2016. Empowerment series: Research methods for social work. Cengage Learning. Russell, S.J., 2010. Artificial intelligence a modern approach. Pearson Education, Inc. Rutinowski, J., Franke, S., Endendyk, J., Dormuth, I., Pauly, M., 2023. The Self-Perception and Political Biases of ChatGPT. doi:10.48550/

###### arXiv.2304.07333, arXiv:2304.07333.

Salehi, P., Hassan, S.Z., Lammerse, M., Sabet, S.S., Riiser, I., Røed, R.K., Johnson, M.S., Thambawita, V., Hicks, S.A., Powell, M., et al., 2022. Synthesizing a talking child avatar to train interviewers working with maltreated children. Big Data and Cognitive Computing 6, 62. Santurkar, S., Durmus, E., Ladhak, F., Lee, C., Liang, P., Hashimoto, T., 2023. Whose Opinions Do Language Models Reflect? doi:10.48550/

###### arXiv.2303.17548, arXiv:2303.17548.

Sap, M., Le Bras, R., Fried, D., Choi, Y., 2022. Neural Theory-of-Mind? On the Limits of Social Intelligence in Large LMs, in: Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing, Association for Computational Linguistics, Abu Dhabi, United Arab Emirates. pp. 3762–3780. URL: https://aclanthology.org/2022.emnlp-main.248.

Scao, T.L., Fan, A., Akiki, C., Pavlick, E., Ilić, S., Hesslow, D., Castagné, R., Luccioni, A.S., Yvon, F., Gallé, M., et al., 2023. BLOOM: A

176B-Parameter Open-Access Multilingual Language Model. doi:10.48550/arXiv.2211.05100, arXiv:2211.05100. Shanahan, M., 2022. Talking about large language models. arXiv preprint arXiv:2212.03551 .

Sinha, A., Khandait, T., 2021. Impact of News on the Commodity Market: Dataset and Results, in: Arai, K. (Ed.), Advances in Information and Communication, Springer International Publishing, Cham. pp. 589–601. Son, G., Jung, H., Hahm, M., Na, K., Jin, S., 2023. Beyond Classification: Financial Reasoning in State-of-the-Art Language Models. doi:10.

###### 48550/arXiv.2305.01505, arXiv:2305.01505.

Soun, Y., Yoo, J., Cho, M., et al., 2022. Accurate stock movement prediction with self-supervised learning from sparse noisy tweets, in: 2022 IEEE International Conference on Big Data (Big Data), pp. 1691–1700. doi:10.1109/BigData55660.2022.10020720. Stevenson, C., Smal, I., Baas, M., Grasman, R., van der Maas, H., 2022. Putting GPT-3’s Creativity to the (Alternative Uses) Test. doi:10.48550/

###### arXiv.2206.08932, arXiv:2206.08932.

Tang, L., Peng, Y., Wang, Y., Ding, Y., Durrett, G., Rousseau, J.F., 2023. Less likely brainstorming: Using language models to generate alternative hypotheses, in: Proceedings of the 61th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), Association for Computational Linguistics.

Terwiesch, C., 2023. Would chat gpt3 get a wharton mba. A prediction based on its performance in the operations management course. Wharton: Mack Institute for Innovation Management/University of Pennsylvania/School Wharton . Tiku, N., 2023. The Google engineer who thinks the company’s AI has come to life. Washington Post URL: https://www.washingtonpost.

###### com/technology/2022/06/11/google-ai-lamda-blake-lemoine/.

Touvron, H., Lavril, T., Izacard, G., Martinet, X., Lachaux, M.A., Lacroix, T., Rozière, B., Goyal, N., Hambro, E., Azhar, F., Rodriguez, A., Joulin, A., Grave, E., Lample, G., 2023. LLaMA: Open and Efficient Foundation Language Models. doi:10.48550/arXiv.2302.13971, arXiv:2302.13971.

Trochim, W.M., Donnelly, J.P., 2001. Research methods knowledge base. volume 2. Atomic Dog Pub. Macmillan Publishing Company, New York. Trott, S., Jones, C., Chang, T., Michaelov, J., Bergen, B., 2023. Do large language models know what humans know? Cognitive Science 47, e13309. Tu, S., Li, C., Yu, J., Wang, X., Hou, L., Li, J., 2023. ChatLog: Recording and Analyzing ChatGPT Across Time. doi:10.48550/arXiv.2304.

###### 14106, arXiv:2304.14106.

Turcan, E., McKeown, K., 2019. Dreaddit: A reddit dataset for stress analysis in social media, in: Conference on Empirical Methods in Natural Language Processing. URL: https://api.semanticscholar.org/CorpusID:207870937. Törnberg, P., 2023. Chatgpt-4 outperforms experts and crowd workers in annotating political twitter messages with zero-shot learning.

###### arXiv:2304.06588.

Ullman, T., 2023. Large Language Models Fail on Trivial Alterations to Theory-of-Mind Tasks. doi:10.48550/arXiv.2302.08399,

arXiv:2302.08399. Uludag, K., 2023. Chatgpt can distinguish paranoid thoughts in patients with schizophrenia. Available at SSRN 4391941 . Wang, L., Ma, C., Feng, X., Zhang, Z., Yang, H., Zhang, J., Chen, Z., Tang, J., Chen, X., Lin, Y., et al., 2023a. A survey on large language model

based autonomous agents. arXiv preprint arXiv:2308.11432 . Wang, S., Scells, H., Koopman, B., Zuccon, G., 2023b. Can chatgpt write a good boolean query for systematic review literature search? arXiv

preprint arXiv:2302.03495 . Webb, T., Holyoak, K.J., Lu, H., 2023. Emergent analogical reasoning in large language models. Nature Human Behaviour , 1–16. Wei, J., Wang, X., Schuurmans, D., Bosma, M., Xia, F., Chi, E., Le, Q.V., Zhou, D., et al., 2022. Chain-of-thought prompting elicits reasoning in

large language models. Advances in Neural Information Processing Systems 35, 24824–24837. Willer, D., Walker, H.A., 2007. Building experiments: Testing social theory. Stanford University Press. Wilson, S.J., Wilkins, A.D., Holt, M.V., Choi, B.K., Konecki, D., Lin, C.H., Koire, A., Chen, Y., Kim, S.Y., Wang, Y., et al., 2018. Automated

literature mining and hypothesis generation through a network of medical subject headings. bioRxiv , 403667.

Wood, D.A., Achhpilia, M.P., Adams, M.T., Aghazadeh, S., Akinyele, K., Akpan, M., Allee, K.D., Allen, A.M., Almer, E.D., Ames, D., et al., 2023. The ChatGPT Artificial Intelligence Chatbot: How Well Does It Answer Accounting Assessment Questions? Issues in Accounting Education 38. URL: https://www.researchgate.net/publication/370211135_The_ChatGPT_Artificial_Intelligence_Chatbot_How_ Well_Does_It_Answer_Accounting_Assessment_Questions.

Woolgar, S., 1985. Why not a sociology of machines? the case of sociology and artificial intelligence. Sociology 19, 557–572. Wright, J.D., Marsden, P.V., et al., 2010. Survey research and social science: History, current practice, and future prospects. Handbook of survey

research , 3–26.

Wu, H., Zhang, W., Shen, W., et al., 2018. Hybrid deep sequential modeling for social text-driven stock prediction. Proceedings of the 27th ACM International Conference on Information and Knowledge Management URL: https://api.semanticscholar.org/CorpusID:53038910. Wu, P.Y., Nagler, J., Tucker, J.A., Messing, S., 2023a. Large language models can be used to scale the ideologies of politicians in a zero-shot learning

###### setting. arXiv:2303.12057.

Wu, S., Irsoy, O., Lu, S., Dabravolski, V., Dredze, M., Gehrmann, S., Kambadur, P., Rosenberg, D., Mann, G., 2023b. BloombergGPT: A Large Language Model for Finance. URL: http://arxiv.org/abs/2303.17564, doi:10.48550/arXiv.2303.17564, arXiv:2303.17564. Xie, Q., Han, W., Lai, Y., Peng, M., Huang, J., 2023a. The wall street neophyte: A zero-shot analysis of chatgpt over multimodal stock movement

prediction challenges. arXiv:2304.05351. Xie, Q., Han, W., Zhang, X., et al., 2023b. Pixiu: A large language model, instruction data and evaluation benchmark for finance. ArXiv abs/2306.05443. URL: https://api.semanticscholar.org/CorpusID:259129602.

Xu, Y., Cohen, S.B., 2018. Stock movement prediction from tweets and historical prices, in: Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), Association for Computational Linguistics, Melbourne, Australia. pp. 1970–1979. URL: https://aclanthology.org/P18-1183, doi:10.18653/v1/P18-1183.

Yang, K., Ji, S., Zhang, T., Xie, Q., Ananiadou, S., 2023a. On the evaluations of chatgpt and emotion-enhanced prompting for mental health analysis.

arXiv preprint arXiv:2304.03347 . Yang, K., Ji, S., Zhang, T., et al., 2023b. Towards interpretable mental health analysis with large language models. arXiv:2304.03347. Yuan, F., 2013. Tutorial on Social Research methods. Peking University Press.

Zhang, B., Ding, D., Jing, L., 2023. How would stance detection techniques evolve after the launch of chatgpt? arXiv:2212.14548. Zhang, S., Roller, S., Goyal, N., Artetxe, M., Chen, M., Chen, S., Dewan, C., Diab, M., Li, X., Lin, X.V., Mihaylov, T., Ott, M., Shleifer, S.,

Shuster, K., Simig, D., Koura, P.S., Sridhar, A., Wang, T., Zettlemoyer, L., 2022. OPT: Open Pre-trained Transformer Language Models. doi:10.48550/arXiv.2205.01068, arXiv:2205.01068.

Zhao, W.X., Zhou, K., Li, J., Tang, T., Wang, X., Hou, Y., Min, Y., Zhang, B., Zhang, J., Dong, Z., et al., 2023. A survey of large language models. arXiv preprint arXiv:2303.18223 .

Zhao, Z., Wallace, E., Feng, S., Klein, D., Singh, S., 2021. Calibrate Before Use: Improving Few-shot Performance of Language Models, in: Proceedings of the 38th International Conference on Machine Learning, PMLR. pp. 12697–12706. URL: https://proceedings.mlr.press/ v139/zhao21c.html.

Zhou, W., Jiang, Y.E., Li, L., Wu, J., Wang, T., Qiu, S., Zhang, J., Chen, J., Wu, R., Wang, S., et al., 2023. Agents: An open-source framework for autonomous language agents. arXiv preprint arXiv:2309.07870 . Ziems, C., Held, W., Shaikh, O., Chen, J., Zhang, Z., Yang, D., 2023. Can large language models transform computational social science? arXiv preprint arXiv:2305.03514 . Zimbardo, P.G., Haney, C., Banks, W.C., Jaffe, D., 1971. The Stanford prison experiment. Zimbardo, Incorporated.

