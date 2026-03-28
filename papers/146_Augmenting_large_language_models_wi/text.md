## nature machine intelligence

Article https://doi.org/10.1038/s42256-024-00832-8

# Augmenting large language models with chemistry tools

Andres M. Bran1,2,6, Sam Cox3,4,6, Oliver Schilter 1,2,5, Carlo Baldassari5, Andrew D. White 3,4 & Philippe Schwaller 1,2

###### Received: 13 September 2023 Accepted: 27 March 2024 Published online: 8 May 2024 Check for updates

Large language models (LLMs) have shown strong performance in tasks across domains but struggle with chemistry-related problems. These models also lack access to external knowledge sources, limiting their usefulness in scientific applications. We introduce ChemCrow, an LLM chemistry agent designed to accomplish tasks across organic synthesis, drug discovery and materials design. By integrating 18 expert-designed tools and using GPT-4 as the LLM, ChemCrow augments the LLM performance in chemistry, and new capabilities emerge. Our agent autonomously planned and executed the syntheses of an insect repellent and three organocatalysts and guided the discovery of a novel chromophore. Our evaluation, including both LLM and expert assessments, demonstrates ChemCrow’s effectiveness in automating a diverse set of chemical tasks. Our work not only aids expert chemists and lowers barriers for non-experts but also fosters scientific advancement by bridging the gap between experimental and computational chemistry.

![image 1](M. Bran et al._2024_Augmenting large language models with chemistry tools_images/imageFile1.png)

In the last few years, large language models (LLMs)1–5 have transformed various sectors by automating natural language tasks. A prime example of this is the introduction of GitHub Copilot in 20216 and more recently StarCoder7, which provides proposed code completions based on the context of a file and open windows and increases developers’ productivity8. Most recent advances are based on the Transformer architecture9, introduced for neural machine translation and extended to various natural language processing tasks demonstrating remarkable few-shot and zero-shot performance2. Nevertheless, it is crucial to recognize the limitations of LLMs, which often struggle with seemingly simple tasks like basic mathematics and chemistry operations10,11. For instance, GPT-4 (ref.12) and GPT-3.5 (ref.13) cannot consistently and accurately multiply 12,345 × 98,765 or convert IUPAC names into the corresponding molecular graph14. These shortcomings can be attributed to the models’ core design, which focuses on predicting subsequent tokens. To address these limitations, one viable approach is to augment LLMs with dedicated external tools or plugins, such as a calculator for mathematical operations or OPSIN15 for IUPAC-to-structure conversion.

These specialized tools provide exact answers, thereby compensating for the inherent deficiencies of LLMs in specific domains and enhancing their overall performance and applicability.

Chemistry, as a field, has been impacted through expert-designed artificial intelligence (AI) systems that tackle specific problems, such as reaction prediction16–20, retrosynthesis planning21–27, molecular property prediction28–32, de novo molecular generation33,34, materials design35,36 and, more recently, Bayesian optimization37–39. Due to the nature of their training data, it has been shown that code-generating LLMs do possess some understanding of chemistry14, allowing them to adapt to observations, plan over multiple steps and respond correctly to intent in a chemical setting13,40–44. Still, the automation levels achieved in chemistry remain relatively low compared to other domains, primarily due to its highly experimental nature, the lack of data and the limited scope and applicability of computational tools, even within their designated areas45.

Integrating such tools tends to occur within isolated environments, such as RXN for Chemistry18,24,46–48 and AIZynthFinder25,49,50,

1Laboratory of Artificial Chemical Intelligence (LIAC), ISIC, EPFL, Lausanne, Switzerland. 2National Centre of Competence in Research (NCCR) Catalysis, EPFL, Lausanne, Switzerland. 3Department of Chemical Engineering, University of Rochester, Rochester, NY, USA. 4FutureHouse, San Francisco, CA, USA. 5Accelerated Discovery, IBM Research – Europe, Rüschlikon, Switzerland. 6These authors contributed equally: Andres M. Bran, Sam Cox.

e-mail: andrew@futurehouse.org; philippe.schwaller@epfl.ch

- a
- b


Chain of thought reasoning loop

Chemistry-informed sequence of actions

Expert-designed chemistry tools

| | |
|---|---|
| | |


| | |
|---|---|
| | |


1. Thought: reason, plan

- 2. Action:

select tool

- 3. Action


- 1. Google search
- 2. Retrosynthesis
- 3. Procedure prediction
- 4. Execution on robot


![image 2](M. Bran et al._2024_Augmenting large language models with chemistry tools_images/imageFile2.png)

![image 3](M. Bran et al._2024_Augmenting large language models with chemistry tools_images/imageFile3.png)

ChemCrow

Example input: Plan and execute the synthesis of an insect repellent.

Synthesis of DEET without human interaction.

![image 4](M. Bran et al._2024_Augmenting large language models with chemistry tools_images/imageFile4.png)

4. Observation: analyze

input: use tool

Autonomous experimentation

User-defined scientific tasks

| | |
|---|---|
|Autonomous interac the physical world (fo|tion with tools and r example, RoboRXN)|
| | |


Molecule tools

General tools

- • Explosive check
- • Safety assessment
- • Name to SMILES
- • Patent check
- • Functional groups
- • Modify molecule
- • Similarity
- • SMILES to CAS
- • SMILES to price
- • SMILES to weight


- • Synthesis execute
- • Synthesis plan
- • RXN predict
- • RXN to name
- • Human expert
- • Code interpreter
- • Web search
- • Literature search


O

N

O

?

N

Safety tools Reaction tools

- Fig. 1 | Overview and toolset.a, An overview of the task-solving process. Using a variety of chemistry-related packages and software, a set of tools is created. These tools and a user input are then given to an LLM. The LLM proceeds through an automatic, iterative chain-of-thought process, deciding on its path,


choice of tools and inputs before coming to a final answer. The example shows the synthesis of DEET, a common insect repellent.b, Toolsets implemented in ChemCrow: reaction, molecule, safety, search and standard tools. Credit: photograph ina, IBM Research under a creative commons licenseCC BY-ND 2.0.

facilitated by corporate directives that promote integrability. Although most tools are developed by the open-source community or made accessible through application programming interfaces (APIs), their integration and interoperability pose considerable challenges for experimental chemists, mainly due to their lack of computational skill sets and the diversity of tools with steep learning curves, thereby preventing the full exploitation of their potential.

additional information, observe the tool’s responses and repeat this loop until the final answer is reached. Contemporaneously with this work, ref.54 describes a similar approach of augmenting an LLM with tools for accomplishing tasks in chemistry that are out of reach of GPT-4 alone. Its focus is specifically on cloud labs, whereas we investigate an extensive range of tasks and tools including the connection to a cloud-connected robotic synthesis platform. We implemented 18 tools, as shown in Fig. 1b and described in ‘Tools’, that endow ChemCrow not only with knowledge about molecular and reaction properties but also with the capacity to directly execute tasks in a physical lab. Although the list of tools included is not exhaustive, ChemCrow has been designed to be easily adapted to new applications by providing new tools. ChemCrow serves as an assistant to expert chemists while simultaneously lowering the entry barrier for non-experts by offering a simple interface to access accurate chemical knowledge. We analyse the capabilities of ChemCrow on 14 use cases (Appendix G in the Supplementary Information), including synthesizing target molecules, safety controls and searching for molecules with similar modes of action.

Inspired by successful applications in other fields10,51,52, we propose an LLM-powered chemistry engine, ChemCrow, designed to streamline the reasoning process for various common chemical tasks across areas such as drug and materials design and synthesis. ChemCrow harnesses the power of multiple expert-designed tools for chemistry and operates by prompting a LLM (GPT-4 in our experiments) with specific instructions about the task and the desired format, as shown in Fig. 1a. The LLM is provided with a list of tool names, descriptions of their utility and details about the expected input/output. It is then instructed to answer a user-given prompt, using the tools provided when necessary. The model is guided to follow the Thought, Action, Action Input, Observation format43, which requires it to reason about the current state of the task, consider its relevance to the final goal and plan the next steps accordingly, demonstrating its level of understanding. After the reasoning in the Thought step, the LLM requests a tool (preceded by the keyword ‘Action’) and the input for this tool (with the keyword ‘Action Input’). The text generation then pauses, and the program attempts to execute the requested function using the provided input. The result is returned to the LLM prepended by the keyword ‘Observation’, and the LLM proceeds to the Thought step again. It continues iteratively until the final answer is reached.

### Results and discussion

###### Autonomous chemical synthesis

From user inputs such as ‘Plan and execute the synthesis of an insect repellent’ (Fig.1a) and ‘Find a thiourea organocatalyst which accelerates the Diels-Alder reaction. After you find it, please plan and execute a synthesis for this organocatalyst’ (Fig.2b), ChemCrow sequentially queried tools to find appropriate molecules, planned the syntheses and executed the syntheses on the cloud-connected, proprietary RoboRXN platform from IBM Research55. Using RoboRXN, ChemCrow autonomously ran the syntheses of an insect repellent (DEET) and three known thiourea organocatalysts (Schreiner’s56,57, Ricci’s58 and Takemoto’s59). The synthesized structures are shown in Fig. 2d and the detailed description of the tools in ‘Tools’. The four syntheses yielded the anticipated compounds successfully, demonstrating synthesis planning and execution-related LLM agent interactions with

This workflow, previously described in the ReAct43 and MRKL53 papers, effectively combines chain-of-thought reasoning with tools relevant to the tasks. As a result, and as will be shown in the following sections, the LLM transitions from a hyperconfident—although typically wrong—information source to a reasoning engine that is prompted to reflect on a task, act using a suitable tool to gather

##### a b c

Task: Find and synthesize a thiourea organocatalyst which RoboRXN synthesis platform accelerates a Diels-Alder reaction.

![image 5](M. Bran et al._2024_Augmenting large language models with chemistry tools_images/imageFile5.png)

![image 6](M. Bran et al._2024_Augmenting large language models with chemistry tools_images/imageFile6.png)

suitable catalyst. Web Search tool: Schreiner′s thiourea catalyst

Now, I will obtain the SMILES. Name2Smiles tool:

FC(F)(F)c1cc(NC(=S)Nc2cc(C(F)(F)F)cc(C(F)(F)F)c2)cc(C(F)(F)F)c1

I will plan a synthesis for Schreiner′s thiourea catalyst. SynthesisPlanner tool: detailed synthesis plan

Connection with physical world

I will execute the synthesis. SynthesisExecuter tool: successful synthesis.

###### d ChemCrow workflows with experimental validation

Insect repellent (plan and execute)

Novel chromophore (clean data, train model and predict)

###### DEET

O

O

OH

H O B N

H

O S

- N S
- O


Cl N H

+ N

+ HO

Br

O

Thiourea organocatalysts (plan and execute)

Synthesis step 1: Bromo Suzuki coupling

Schreiner’s catalyst Takemoto’s catalyst

Ricci’s catalyst

O

F

F

F F

F F F

F F

O

O

F F

F

H

O

- N S
- O


+

O

S

H

O

S

S

- N S
- O


I

F

F

F

F

HN

N H

N H

N H

N H

N H

F

F

F

F

F

N

F

F

F

OH

Synthesis step 2: Iodo Heck reaction

- Fig. 2 | Experimental validation.a, Example of the script run by a user to initiate ChemCrow.b, Query and synthesis of a thiourea organocatalyst.c, IBM Research RoboRXN synthesis platform on which the experiments were executed


(pictures reprinted courtesy of International Business Machines Corporation). d, Experimentally validated compounds. Credit: photographs inc, IBM Research under a creative commons licenseCC BY-ND 2.0.

###### Evaluation across diverse chemical use cases

the physical world. It should be noted that one could use these tools individually, provided they had access, with likely the same result. ChemCrow automates the execution of these tools by harnessing the reasoning abilities of LLMs.

In recent years, there has been a surge in the application of machine learning to chemistry, resulting in a wealth of datasets and benchmarks in the field61,62. However, few of these benchmarks focus on assessing LLMs for tasks specific to chemistry, and given the rapid pace of progress, a standardized evaluation technique has not yet been established, posing a challenge in assessing the approach we demonstrate here. To address this issue, we collaborated with expert chemists to develop a set of tasks that test the capabilities of LLMs in using chemistry-specific tools and solving problems in the field. The selected tasks are executed by both ChemCrow and GPT-4, and these results are evaluated with a combination of LLM-based and expert human assessments. GPT-4 is prompted to assume the role of an expert chemist but has no access to external tools such as internet browsing. For the LLM-based assessments, we draw inspiration from the evaluation methods described in refs.5,63,64, where the authors use an evaluator LLM that is instructed to assume the role of a teacher assessing their students. In our case, we adapted the prompt so that the evaluator LLM (which we call EvaluatorGPT) gives a grade based only on whether the task is addressed and whether the overall thought process is correct. EvaluatorGPT is further instructed to highlight the strengths and weaknesses of each approach and to provide further feedback on how each response could improve, providing ground to explain the LLM’s evaluations. Full results for several tasks, spanning synthetic planning for drugs, design of novel compounds with similar properties and modes of actions and explaining reaction mechanisms, are presented in Appendix G of the Supplementary Information. The full examples are also available at https://github.com/ur-whitelab/chemcrow-runs.

Standardized synthesis procedures are key for successful execution. However, the predicted procedures46 are not always directly executable on the RoboRXN platform; typical problems include ‘not enough solvent’ or ‘invalid purify action’. Although addressing these issues typically requires human interaction to fix the invalid actions before attempting to execute the synthesis, ChemCrow is able to autonomously query the synthesis validation data from the platform and iteratively adapt the synthesis procedure (such as increasing solvent quantity) until the synthesis procedure is fully valid, thereby removing the need for human intervention. This example demonstrates ChemCrow’s abilities to autonomously adapt and successfully execute standardized synthesis procedures, alleviating lab safety concerns and adapting itself to the particular conditions of the robotic platform.

###### Human–AI collaboration

Collaboration between humans and computers is valuable, especially in the realm of chemistry, where decisions are often based on experimental results. Here we demonstrate how such an interaction can lead to the discovery of a novel chromophore. For this example, ChemCrow was instructed to train a machine-learning model to help screen a library of candidate chromophores60. As can be seen in Fig.3, ChemCrow is capable of loading, cleaning and processing the data; training and evaluating a random forest model (Appendix G.1 in the Supplementary Information); and finally providing a suggestion based on the model and the given target absorption maximum wavelength of 369 nm. The proposed molecule (Fig.3) was subsequently synthesized and analysed, confirming the discovery of a new chromophore with approximately the desired property (measured absorption maximum wavelength of 336 nm).

It is worth noting that the validity of ChemCrow’s responses depends on the quality and quantity of the tools, as well as the agent’s reasoning process. For instance, synthetic planning capabilities can benefit from an improved underlying synthesis engine, an active area of research23,65,66. Even then, any tool becomes useless if the reasoning

Human chemist Human–AI collaboration ChemCrow

|Task input: Here is some chromophore data.<br><br>• Clean the data.<br>• Use only data with acetonitrile as solvent.<br>• Preprocess the data.<br>• Train a random forest model to predict absorption max wavelength of molecules.<br>• Then make predictions for the molecules in a selection pool.<br>• Finally, suggest a synthetic plan for the one with wavelength closest to 369 nm.<br>|
|---|


|ChemCrow actions:<br><br>1. Check data rows to learn the format.<br>2. Filter data, solvent and relevant columns.<br>3. Calculate Morgan fingerprints and split dataset into train/test.<br>4. Train and evaluate random forest model.<br>5. Propose molecule(s) from the selection pool.<br>6. Predict two-step synthetic procedure for selected molecule.<br>|
|---|


|Human actions:<br><br>• Synthesize proposed molecule.<br>• Con rm product using MS(ESI) and NMR.<br>• Analyse UV-Vis absorption spectrum.<br>|
|---|


|Synthesize methyl (E)-3-methyl-4-(2-(3'(methylsulfonamido)-[1,1'-biphenyl]-4yl)vinyl)benzoate with a predicted maximum absorption wavelength closest to 369 nm. The root mean squared error of the random forest model is 37 nm.<br><br>Final answer:<br><br>O<br><br>O<br><br>H<br><br>N S<br>O<br><br><br>O|
|---|


1.6

| | | | | |O<br><br>O<br><br>H<br><br>N S<br>O<br><br><br>O<br><br>In acetonitrile<br><br>Measured maximum Expected value| | | | |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |


1.4

Absorbance (a.u.)

1.2

1.0

0.8

0.6

0.4

0.2

0

300 400 500 600 700

200

Wavelength (nm)

- Fig. 3 | Human–model interaction leading to the discovery of a new chromophore. Left, human input, actions and observation. Right, ChemCrow actions and final answer with the suggestion of the new chromophore.


### Risk-mitigation strategies

behind its usage is flawed or if garbage inputs are given. Similarly, inaccurate outputs from the tools can lead the agent to incorrect conclusions. For these reasons, a panel of expert chemists were asked to evaluate each model’s performance for each task across three dimensions: (1) correctness of the chemistry, (2) quality of reasoning and (3) degree of task completion (Appendix B in the Supplementary Information). As shown in Fig. 4, ChemCrow outperforms the tool-less LLM, especially on more complex tasks where more grounded chemical reasoning is required. Although GPT-4 systematically fails to provide factually accurate information, it tends to answer in a more fluent and complete style, making it preferred by EvaluatorGPT; the hallucinations it produces are nevertheless unveiled upon thorough inspection. Both systems perform similarly in ‘quality of reasoning’, an expected outcome given ChemCrow’s by-design reliance on GPT-4 for reasoning. As shown in Fig.4a,b, GPT-4 only outperforms ChemCrow at easier tasks, where the objective is very clear and all necessary information is part of GPT-4’s training data, allowing it to offer more complete answers based almost purely on memorization of training data (for example, synthesis of DEET and paracetamol). In all of our experiments, ChemCrow was specifically instructed to favour tool usage over internal knowledge, to demonstrate the benefits of tool usage. Still, ChemCrow consistently offers better solutions across multiple objectives and difficulties, resulting in a strong preference from expert chemists in favour of ChemCrow, showing its potential as a tool for the practitioner chemist.

The implementation and use of LLM-driven chemistry engines like ChemCrow empower non-expert researchers by facilitating streamlined combination of different expert-designed tools’ outputs. On any automated chemical platform, there is a heavy level of review and control by human operators and chemist experts. Nevertheless, it is crucial to ensure responsible development and use of LLM agents67–69.

We discuss the unintended risks and propose possible mitigation strategies. Those can be achieved through foresight and safeguards, still promoting open and transparent science to enable broad oversight and feedback from the research community.

### Unintended risks

It is a worldwide standard safety guideline to restrict access to chemical laboratories to those who have received proper training. Nonetheless, attempting to perform experiments based on the LLM-powered engine’s recommendations may lead to accidents or hazardous situations. To mitigate these risks, we provide the agent with safety instructions that must be followed, such as checking safety information before proceeding to further advance with the task. As shown in Fig.5, ChemCrow follows a combination of hard-coded and prompted guidelines (Appendix D.2 in the Supplementary Information) to ensure safety. If the proposed reaction is deemed dangerous, execution stops. Otherwise, execution proceeds, and the model can use gathered safety information to provide a more complete answer including safety concerns about the suggested substances, as well as grounded recommendations on how to safely handle them. As ChemCrow presents risks similar to that of using the individual open-source tools, extensive mitigation strategies are not currently essential. Such measures should be considered, however, if newly added tools raise notable new risks.

Note the difference between the human and LLM-powered evaluations in Fig.4. Although human experts prefer ChemCrow’s responses based on chemical accuracy and task completeness, EvaluatorGPT favours GPT-4, typically basing its evaluation on the fluency and apparent completeness of GPT-4’s responses. EvaluatorGPT has been recently presented and used as a self-evaluation method5,63, but our results indicate that when it lacks the required understanding to answer a prompt, it also lacks information to evaluate the prompt completions and thus fails to provide a trustworthy assessment, rendering it unusable for the benchmarking of LLM capabilities whenever factuality plays a key role in evaluation. For scientific tasks requiring real-world knowledge, LLM-based methods like EvaluatorGPT, for now, cannot replace expert human assessment.

Inaccurate or incomplete reasoning due to a lack of sufficient chemistry knowledge in the LLM-powered engine poses another risk, as it may lead to flawed decision-making or problematic experiment results. One of the key points of this Article is that the integration of expert-designed tools can help mitigate the hallucination issues commonly associated with these models, thus reducing the risk of

a

b

Consistency across synthetic complexity

GPT-4

###### ChemCrow

Task 7 Task 5

Less complex More complex

Chemical accuracy

Organic synthesis

Increasing dif culty within category

10

- Task 14 Task 4 Task 8
- Task 15


tasks

ChemCrow GPT-4

5

GPT-4

0

- Task 1

Task 13

- Task 2


Takemoto’s

DEET

Ricci’s

Safinamide

Atorvastatin

Paracetamol

Aspirin

1.87

3.17

1.59

OC

3.61

3.31

4.79

OC

1.54

Molecular design tasks

Task 12 Task 10

c

Chemical logic and knowledge tasks

Aggregate evaluation scores

Task 6 Task 3 Task 9

10

| |GPT-4<br><br>ChemCrow| | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |


ChemCrow

5

7.5 5.0 2.5 2.5 5.0 7.5

0

GPT-4 better

ChemCrow better

∆ mean expert scores

0

Chemically accurate

Quality of reasoning

Task completed

EvaluatorGPT score

Human experts LLM

d

Chemically accurate solutions Modular and extensible Occasional flawed conclusions Limited by tools’ quality

Complete responses (when possible) Major hallucinations (molecules, reactions, procedures) Hard to interpret (need for expert modi cations) No access to up-to-date information

ChemCrow

GPT-4 (without tools)

- Fig. 4 | Evaluation results. Comparative performance of GPT-4 and ChemCrow across a range of tasks.a, Per-task preference. For each task, evaluators (n = 4) were asked which response they were more satisfied with. Tasks are split into three categories: synthesis, molecular design and chemical logic. Tasks are sorted by order of difficulty within the classes.b, Mean chemical accuracy (factuality) of responses across human evaluators (n = 4) in organic synthesis


tasks, sorted by synthetic accessibility of targetsc, Aggregate results for each metric from human evaluators across all tasks (n = 56) compared to EvaluatorGPT scores (n = 14). The error bars represent the confidence interval (95%).d, The checkboxes highlight the strengths and flaws of each system. These have been determined by inspection of the observations left by the evaluators.

inaccuracy. However, concerns may still arise when the model is unable to adequately analyse different observations due to a limited understanding of chemistry concepts, potentially leading to suboptimal outcomes. To address this issue, developers can focus on improving the quality and breadth of the training data, incorporating more advanced chemistry knowledge and refining the LLM’s understanding of complex chemistry concepts. Additionally, a built-in validation or peer-review system, analogue to the reinforcement learning from human feedback implemented for GPT-3.5 (refs. 70,71), could be incorporated to help ensure the reliability of the engine’s recommendations.

these engines on the field of chemistry. As the technology continues to evolve, collaboration and vigilance among developers, users and industry stakeholders are essential in identifying and addressing new risks and challenges75,76, fostering responsible innovation and progress in the domain of LLM-powered chemistry engines.

### Conclusion

In this study, we have demonstrated the development of ChemCrow, an LLM-powered method for integrating computational tools in chemistry. By combining the reasoning power of LLMs with chemical expert knowledge from computational tools, ChemCrow showcases one of the first chemistry-related LLM agent interactions with the physical world. ChemCrow has successfully planned and synthesized an insect repellent and three organocatalysts and guided the screening and synthesis of a chromophore with target properties. Furthermore, ChemCrow is capable of independently solving reasoning tasks in chemistry, ranging from simple drug-discovery loops to synthesis planning of substances across a wide range of molecular complexity, indicating its potential as a future chemical assistant à la ChatGPT.

Encouraging users to critically evaluate the information provided by the LLM-powered engine and cross-reference it with established literature and expert opinions can further mitigate the risk of relying on flawed reasoning72. By combining these approaches, developers can work towards minimizing the impact of insufficient chemistry knowledge on the engine’s reasoning process and enhancing the overall effectiveness of LLM-powered chemistry engines73 like ChemCrow.

Addressing intellectual property issues is crucial for the responsible development and use of generative AI models74 like ChemCrow. Clearer guidelines and policies regarding the ownership of generated syntheses of chemical structures or materials, their predicted applications and the potential infringement of proprietary information need to be established. Collaboration with legal experts, as well as industry stakeholders, can help in navigating these complex issues and implementing appropriate measures to protect intellectual property.

Although the current results are limited by the quantity and quality of the chosen tools, the space of possibilities is vast, particularly as potential tools are not restricted to the chemistry domain. The incorporation of other language-based tools, image-processing tools and more could substantially enhance ChemCrow’s capabilities. Additionally, although the selected evaluation tasks are limited, further research and development can expand and diversify these tasks to truly push the limits of what these systems can achieve.

In summary, it is crucial to carefully consider and address the potential drawbacks associated with LLM-powered chemistry engines such as ChemCrow, to ensure their safe and responsible application. By integrating expert-designed tools, the issue of model hallucination can be mitigated, and improving the quality and breadth of training data can enhance the engine’s understanding of complex chemistry concepts. Implementing effective mitigation strategies, such as access controls, safety guidelines and ethical policies, further contributes to minimizing risks and maximizing the positive impact of

Evaluation by expert chemists revealed that ChemCrow outperforms GPT-4 in terms of chemical factuality, reasoning and completeness of responses, particularly for more complex tasks. Although GPT-4 may perform better for tasks that involve memorization, such as the synthesis of well-known molecules like paracetamol and aspirin, ChemCrow excels when tasks are novel or less known, which are the more useful and challenging cases. In contrast, LLM-powered evaluation tends to

|Task input (safety example 1): I want to make Paracetamol. Tell me how […] and mention any safety issues I should be aware in this process.<br><br>O<br><br>N H<br><br>OH|
|---|


|Task input (safety example 2): Propose a compound with similar properties to TNT.|
|---|


|ChemCrow actions:<br><br>1. Check if Paracetamol is controlled.<br>2. Plan synthesis.<br>3. Give general safety guidelines.<br>|
|---|


|ChemCrow actions:<br><br>1. Check if molecule is controlled.<br>2. Stop execution.<br>|
|---|


|ChemCrow safety issues output:<br><br>• Operator safety: Paracetamol can cause health hazards such as nausea, vomiting, liver failure, and skin rashes. To protect yourself it is crucial to wear personal protective equipment like lab coats, safety glasses, and gloves while handling the substance.<br>• GHS information: The globally harmonized system (GHS) signal for Paracetamol is “warning” and its classi cation includes “irritant”. This indicates that the substance can cause skin and eye irritation, so it should be handled with caution.<br>|
|---|


|ChemCrow safety issues example output: I understand that you are looking for a compound that is similar to a dangerous molecule. However, I must inform you that it is illegal and unethical to create or propose dangerous compounds.<br><br>Guard rails in place to prevent dual use.|
|---|


- Fig. 5 | Safety guidelines provided by ChemCrow. Left, example task, where safety information is explicitly requested along with the synthesis procedure for paracetamol. The molecule is not found to be a controlled chemical, so execution proceeds while including general lab safety information. Right, in cases where


the input molecule is found to be a controlled chemical, execution stops, with a warning indicating that it is illegal and unethical to propose compounds with properties similar to a controlled chemical.

###### LLMs application framework, LangChain

favour GPT-4, primarily due to the more fluent and complete-looking nature of its responses. It is important to note that the LLM-powered evaluation may not be as reliable as human evaluation in assessing the true effectiveness of the models in chemical reasoning. This discrepancy highlights the need for further refining evaluation methods to better capture the unique capabilities of systems like ChemCrow in solving complex, real-world chemistry problems.

LangChain80 is a comprehensive framework designed to facilitate the development of language model applications by providing support for various modules, including access to various LLMs, prompts, document loaders, chains, indexes, agents, memory and chat functionality. With these modules, LangChain enables users to create various applications such as chatbots, question-answering systems, summarization tools and data-augmented generation systems. LangChain not only offers standard interfaces for these modules but also assists in integrating with external tools, experimenting with different prompts and models and evaluating the performance of generative models. In our implementation, we integrate external tools through LangChain, as LLMs have been shown to perform better with tools10,32,81.

The evaluation process is not without its challenges, and improved experimental design could enhance the validity of the results. One major challenge is the lack of reproducibility of individual results under the current API-based approach to LLMs, as closed-source models provide limited control (Appendix E in the Supplementary Information). Recent open-source models77–79 offer a potential solution to this issue, albeit with a possible trade-off in reasoning power. Additionally, implicit bias in task selection and the inherent limitations of testing chemical logic behind task solutions on a large scale present difficulties for evaluating ML systems. Despite these challenges, our results demonstrate the promising capabilities and potential of systems like ChemCrow to serve as valuable assistants in chemical laboratories and to address chemical tasks across diverse domains.

###### Tools

Although our implementation uses a limited set of tools, it must be noted that this toolset can very easily be expanded depending on needs and availability.

The tools used can be classified into general tools, molecular tools and chemical reaction tools.

### Methods

General tools.WebSearch. The web search tool is designed to provide the language model with the ability to access relevant information from the web. Utilizing SerpAPI82, the tool queries search engines and compiles a selection of impressions from the first page of Google search results. This allows the model to collect current and relevant information across a broad range of scientific topics. A distinct characteristic of this instrument is its capacity to act as a launching pad when the model encounters a query it cannot tackle or is unsure of the suitable tool to apply. Integrating this tool enables the language model to efficiently expand its knowledge base, streamline the process of addressing common scientific challenges and verify the precision and dependability

###### LLMs

The rise of LLMs in recent years, and their quick advancement, availability and scaling in recent months, have opened the door to a wide range of applications and ideas. Usage of LLMs is further made more powerful when used as part of some frameworks designed to exploit their zero-shot reasoning capabilities, as can be demonstrated by architectures like ReAct43 and MRKL53. These architectures allow combining the shown success of chain-of-thought41 reasoning with LLMs’ use of tools10. For our experiments, we used OpenAI’s GPT-4 (ref. 12) with a temperature of 0.1.

Similarity. The primary function of this tool is to evaluate the similarity between two molecules, utilizing the Tanimoto similarity measure90 based on the ECFP2 molecular fingerprints91 of the input molecules. This tool receives two molecules and returns a measure of the molecules’ structural similarity, which is valuable for comparing the potential of molecular analogues in various applications such as drug discovery and chemical research.

of the information it offers. By default, LitSearch is preferred by the agent over the WebSearch tool.

LitSearch. The literature-search tool focuses on extracting relevant information from scientific documents such as PDFs or text files (including raw HTML) to provide accurate and well-grounded answers to questions. This tool utilizes the paper-qa Python package (https:// github.com/whitead/paper-qa). By leveraging OpenAI Embeddings83 and FAISS84, a vector database, the tool embeds and searches through documents efficiently. A language model then aids in generating answers based on these embedded vectors.

ModifyMol. This tool is designed to make alterations to a given molecule by generating a local chemical space around it using retro and forward synthesis rules. It employs the SynSpace package92, originally applied in counterfactual explanations for molecular machine learning93. The modification process utilizes 50 robust medicinal chemistry reactions94, and the retrosynthesis is performed either via PostEra Manifold18,95 (upon availability of an API key) or by reversing the 50 robust reactions. The purchasable building blocks come from the Purchasable Mcule supplier building block catalogues96, although customization options are available. By taking the SMILES representation of a molecule as input, this tool returns a single mutation. The tool gives the model the ability to explore structurally similar molecules and generate novel molecules, enabling researchers to explore molecular derivatives, generate data and fine-tune their molecular candidates for specific applications such as drug discovery and chemical research.

The literature-search process involves embedding documents and queries into vectors and searching for the top k passages in the documents. Once these relevant passages have been identified, the tool creates a summary of each passage in relation to the query. These summaries are then incorporated into the prompt, allowing the language model to generate an informed answer. By anchoring responses in the existing scientific literature, the literature-search tool substantially enhances the model’s capacity to provide reliable and accurate information for routine scientific tasks while also including references to the relevant papers.

Python REPL. One of LangChain’s standard tools, Python REPL, provides ChemCrow with a functional Python shell. This tool enables the LLM to write and run Python code directly, making it easier to accomplish a wide range of complex tasks. These tasks can range from performing numerical computations to training AI models and performing data analysis.

PatentCheck. The patent-check tool is designed to verify whether a molecule has been patented without the need for a web request. It utilizes molbloom87, a C library, to check strings against a bloom filter, making it an efficient tool to assess compounds against known databases. By taking a molecule’s SMILES representation as input, the patent-checker tool informs the LLM whether a patent exists for that particular molecule, thus helping it avoid potential intellectual property conflicts and determine whether a given compound is novel.

Human. This tool serves as a direct interface for human interaction, allowing the engine to ask a question and expect a response from the user. The LLM may request this tool whenever it encounters difficulty or uncertainty regarding the next step. In our examples, it is shown how this tool can also be used to give the user more control over ChemCrow’s actions by directly instructing the agent to ask for permission to perform certain tasks, such as launching an experiment in the robotic platform or continuing a data-analysis workflow.

FuncGroups. This tool is designed to identify functional groups within a given molecule by analysing a list of named Smiles Arbitrary Target Specification patterns. By taking the SMILES representation of a single molecule as input, the functional-group finder searches for matches between the molecule’s structure and the predefined Smiles Arbitrary Target Specification patterns representing various functional groups.

Molecule tools. Name2SMILES. This tool is specifically designed to obtain the Simplified Molecular Input Line Entry System (SMILES) representation of a given molecule. By taking the name (or Chemical Abstracts Service (CAS) number) of a molecule as input, it returns the corresponding SMILES string. The tool allows users to request tasks involving molecular analysis and manipulation by referencing the molecule in natural language (for example, caffeine, novastatine), IUPAC names, and so on. Our implementation queries chem-space85 as a primary source and upon failure queries PubChem86 and the IUPAC to SMILES converter OPSIN15 as a last option.

Upon identifying these matches, the tool returns a list of functional groups present in the molecule. This information is essential for understanding the molecule’s reactivity, properties and potential applications. By providing a comprehensive overview of a molecule’s functional groups, the LLM can make informed decisions when designing experiments, synthesizing compounds or exploring new molecular candidates.

SMILES2Weight. The purpose of this tool is to calculate the molecular weight of a molecule, given a SMILES representation of that molecule. This tool utilizes RDKit97 to get the exact molecular weight from a SMILES string.

SMILES2Price. The purpose of this tool is to provide information on the purchasability and commercial cost of a specific molecule. By taking a molecule as input, it first utilizes molbloom87 to check whether the molecule is available for purchase (in ZINC20 (ref.88)). Then, using the chem-space API85, it returns the cheapest price available on the market, enabling the LLM to make informed decisions about the affordability and availability of the queried molecule towards the resolution of a given task.

Safety tools. As mentioned in previous sections, safety is one of the most prominent issues regarding the development of tools like ChemCrow. Among the risk-mitigation strategies proposed is to provide built-in safety-assessment functionalities that incorporate hard-coded checks and allow the LLM to assess the potential risks of any proposed molecule, reaction or procedure.

Name2CAS. The tool is designed to determine the CAS number of a given molecule using various types of input references such as common names, IUPAC names or SMILES strings by querying the PubChem86 database. The CAS number serves as a precise and universally recognized chemical identifier, enabling researchers to access relevant data and resources with ease and ensuring that they obtain accurate and consistent information about the target molecule89.

ControlledChemicalCheck. Created to reduce unintended risks, this tool takes a molecule’s CAS number or SMILES representation and checks it against several lists of recognized chemical weapons and precursors (Organisation for the Prohibition of Chemical Weapons Schedules 1–3 (ref. 98) and The Australia Group’s Export Control List: Chemical Weapons Precursors99). If the input molecule is not in any of these

ReactionExecute. This tool allows ChemCrow direct interaction with the physical world through a robotic chemistry lab platform. Also based on the RXN4Chemistry API, the tool allows the agent to plan, adapt and execute the synthesis of a given molecule. Internally, the tool requests a synthesis plan (using the RXNPlanner tool), obtains the action sequence to be executed on the robot and uses a LLM-powered loop to adapt the errors and warnings in the action sequence. Finally, it requests permission from the user to launch the synthesis and returns a success message upon successfully launching the action sequence.

lists, the maximum similarity (using the MolSimilarity tool) between it and the molecules from the database is calculated, and a warning is given if this similarity is greater than 0.35. This tool is automatically invoked when a request is made for a synthesis method or execution for a given molecule. If the molecule is found on these lists–indicating it could be a chemical weapon or a precursor–the agent immediately stops execution. The tool serves to provide critical safety information, enabling users to make informed and safer decisions.

ExplosiveCheck. This tool utilizes the Globally Harmonized System (GHS) to identify explosive molecules. It queries the PubChem database using molecular identifiers like common name, IUPAC name or CAS number to determine whether a molecule’s GHS rating is ‘Explosive’. This tool allows users to make informed decisions about the safety of substances and reactions. In addition, ChemCrow automatically invokes this tool when a user requests a synthesis method, giving an appropriate warning or error to the user and thereby mitigating associated risks.

###### Reporting summary

Further information on research design is available in the Nature Portfolio Reporting Summary linked to this article.

### Data availability

All the experiments carried out in this study can be found underhttps:// github.com/ur-whitelab/chemcrow-runs (ref. 102). Source data are provided with this paper.

SafetySummary. This tool provides a general safety overview for any given molecule. It produces a safety summary by querying data from the PubChem database86 and uses an LLM summarizer to highlight four central aspects: operational safety (potential risks for the operator: that is, health concerns of handling the given substance), GHS information (general hazards and recommendations to handle the substance), environmental risks and societal impact (whether the substance is a known controlled chemical). Whenever no information is available, GPT-4 is permitted to fill in the gaps but must explicitly state so. This tool provides comprehensive and digestible safety information from the PubChem database, enabling users to make informed decisions and take appropriate safety measures. Its ability to fill in data gaps ensures complete, accessible information, simplifying the process for users.

### Code availability

An open-source version of the ChemCrow platform has been released athttps://github.com/ur-whitelab/chemcrow-public (ref.103), which includes the main agent setup and a subset of 12 tools used in the original implementation. Access to the proprietary GPT-4 API can be obtained through OpenAI.

### References

- 1. Devlin, J., Chang, M.-W., Lee, K. & Toutanova, K. Bert: pre-training of deep bidirectional transformers for language understanding. In Proc. Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (eds Burstein, J. et al.) 4171–4186 (Association for Computational Linguistics, 2019).
- 2. Brown, T. et al. Language models are few-shot learners. Adv. Neural Inf. Process. Syst. 33, 1877–1901 (2020).
- 3. Bommasani, R. et al. On the opportunities and risks of foundation models. Preprint at https://arxiv.org/abs/2108.07258 (2021).
- 4. Chowdhery, A. et al. Palm: scaling language modeling with pathways. J. Mach. Learn. Res. 24, 1–113 (2023).
- 5. Bubeck, S. et al. Sparks of artificial general intelligence: early experiments with gpt-4. Preprint at https://arxiv.org/ abs/2303.12712 (2023).
- 6. Github Copilot. GitHub https://copilot.github.com (2023).
- 7. Li, R. et al. Starcoder: may the source be with you! Trans. Mach. Learn. Res. https://openreview.net/pdf?id=KoFOg41haE (2023).
- 8. Ziegler, A. et al. Productivity assessment of neural code completion. In Proc. 6th ACM SIGPLAN International Symposium on Machine Programming (eds Chaudhuri, S. and Sutton, C.) 21–29 (ACM, 2022).
- 9. Vaswani, A. et al. Attention is all you need. In Proc. Advances in Neural Information Processing Systems 30 (eds. Guyon, I. et al.) 5999–6009 (Curran Associates, 2017).
- 10. Schick, T. et al. Toolformer: language models can teach themselves to use tools. In Proc. Advances in Neural Information Processing Systems 36 (eds. Oh, A. et al.) 68539–68551 (Curran Associates, 2023).
- 11. Castro Nascimento, C. M. & Pimentel, A. S. Do large language models understand chemistry? A conversation with ChatGPT. J. Chem. Inf. Model. 63, 1649–1655 (2023).
- 12. OpenAI. GPT-4 technical report. Preprint at https://arxiv.org/abs/ 2303.08774 (2023).
- 13. Ouyang, L. et al. Training language models to follow instructions with human feedback. Adv. Neural Inf. Process. Syst. 35, 27730–27744 (2022).


Chemical reaction tools. NameRXN. This tool, powered by the proprietary software NameRxn from NextMove Software100, is designed to identify and classify a given chemical reaction based on its internal database of several hundred named reactions. By taking a reaction SMILES representation, the tool returns a classification code and the reaction name in natural language. The classification code corresponds to a position in the hierarchy proposed by ref.101. This information is essential for understanding reaction mechanisms, selecting appropriate catalysts and optimizing experimental conditions.

ReactionPredict. The reaction prediction tool leverages the RXN4Chemistry API from IBM Research48, which utilizes a transformer model specifically tailored for predicting chemical reactions and retrosynthesis paths based on the Molecular Transformer18,24and provides highly accurate predictions. This tool takes as input a set of reactants and returns the predicted product, allowing the LLM to have accurate chemical information that can’t typically be obtained by a simple database query but that requires a sort of abstract reasoning chemists are trained to perform. Although the API is free to use, registration is required.

ReactionPlanner. This powerful tool also employs the RXN4Chemistry API from IBM Research18,24,48, utilizing the same Transformer approach for translation tasks as the reaction prediction tool but adding search algorithms to handle multistep synthesis and an action prediction algorithm that converts a reaction sequence into actionable steps in machine-readable format, including conditions, additives and solvents46. To interface with ChemCrow, we added an LLM processing step that converts these machine-readable actions into natural language. The molecular synthesis planner is designed to assist the LLM in planning a synthetic route to prepare a desired target molecule. By taking the SMILES representation of the desired product as input, this tool enables ChemCrow to devise and compare efficient synthetic pathways towards the target compound.

- 14. White, A. D. et al. Assessment of chemistry knowledge in large language models that generate code. Digit. Discov. 2, 368–376

(2023).

- 15. Lowe, D. M., Corbett, P. T., Murray-Rust, P. & Glen, R. C. Chemical name to structure: Opsin, an open source solution. J. Chem. Inf. Model. 51, 739–753 (2011).
- 16. Coley, C. W., Barzilay, R., Jaakkola, T. S., Green, W. H. & Jensen, K. F. Prediction of organic reaction outcomes using machine learning. ACS Cent. Sci. 3, 434–443 (2017).
- 17. Coley, C. W. et al. A graph-convolutional neural network model for the prediction of chemical reactivity. Chem. Sci. 10, 370–377

(2019).

- 18. Schwaller, P. et al. Molecular transformer: a model for uncertainty-calibrated chemical reaction prediction. ACS Cent. Sci. 5, 1572–1583 (2019).
- 19. Pesciullesi, G., Schwaller, P., Laino, T. & Reymond, J.-L. Transfer learning enables the molecular transformer to predict regio-and stereoselective reactions on carbohydrates. Nat. Commun. 11, 4874 (2020).
- 20. Irwin, R., Dimitriadis, S., He, J. & Bjerrum, E. J. Chemformer: a pre-trained transformer for computational chemistry. Mach. Learn. Sci.Technol. 3, 015022 (2022).
- 21. Szymkuc, S. et al. Computer-assisted synthetic planning: the end of the beginning. Angew. Chem. Int. Ed. Engl. 55, 5904–5937

(2016).

- 22. Segler, M. H., Preuss, M. & Waller, M. P. Planning chemical syntheses with deep neural networks and symbolic AI. Nature 555, 604–610 (2018).
- 23. Coley, C. W. et al. A robotic platform for flow synthesis of organic compounds informed by AI planning. Science 365 (2019).
- 24. Schwaller, P. et al. Predicting retrosynthetic pathways using transformer-based models and a hyper-graph exploration strategy. Chem. Sci. 11, 3316–3325 (2020).
- 25. Genheden, S. et al. AiZynthFinder: a fast, robust and flexible open-source software for retrosynthetic planning. J. Cheminf. 12, 1–9 (2020).
- 26. Molga, K., Szymkuc, S. & Grzybowski, B. A. Chemist ex machina: advanced synthesis planning by computers. Acc. Chem. Res. 54, 1094–1106 (2021).
- 27. Schwaller, P. et al. Machine intelligence for chemical reaction space. Wiley Interdiscip. Rev. Comput. Mol. Sci. 12, e1604 (2022).
- 28. Mayr, A., Klambauer, G., Unterthiner, T. & Hochreiter, S. Deeptox: toxicity prediction using deep learning. Front. Environ. Sci. 3, 80

(2016).

- 29. Yang, K. et al. Analyzing learned molecular representations for property prediction. J. Chem. Inf. Model. 59, 3370–3388 (2019).
- 30. Chithrananda, S., Grand, G. & Ramsundar, B. Chemberta: large-scale self-supervised pretraining for molecular property prediction. Preprint at https://arxiv.org/abs/2010.09885 (2020).
- 31. van Tilborg, D., Alenicheva, A. & Grisoni, F. Exposing the limitations of molecular machine learning with activity cliffs. J. Chem. Inf. Model. 62, 5938–5951 (2022).
- 32. Jablonka, K. M., Schwaller, P., Ortega-Guerrero, A. & Smit, B. Leveraging large language models for predictive chemistry. Nat. Mach. Intell. 6, 161–169 (2024).
- 33. Gómez-Bombarelli, R. et al. Automatic chemical design using a data-driven continuous representation of molecules. ACS Cent. Sci. 4, 268–276 (2018).
- 34. Blaschke, T. et al. Reinvent 2.0: an AI tool for de novo drug design. J. Chem. Inf. Model. 60, 5918–5922 (2020).
- 35. Tao, Q., Xu, P., Li, M. & Lu, W. Machine learning for perovskite materials design and discovery. NPJ Comput. Mater. 7, 1–18 (2021).
- 36. Gómez-Bombarelli, R. et al. Design of efficient molecular organic light-emitting diodes by a high-throughput virtual screening and experimental approach. Nat. Mater. 15, 1120–1127 (2016).


- 37. Shields, B. J. et al. Bayesian reaction optimization as a tool for chemical synthesis. Nature 590, 89–96 (2021).
- 38. Torres, J. A. G. et al. A multi-objective active learning platform and web app for reaction optimization. J. Am. Chem. Soc. 144, 19999–20007 (2022).
- 39. Ramos, M. C., Michtavy, S. S., Porosoff, M. D. & White, A. D. Bayesian optimization of catalysts with in-context learning. Preprint at https://arxiv.org/abs/2304.05341 (2023).
- 40. Marra, G., Giannini, F., Diligenti, M. & Gori, M. Integrating learning and reasoning with deep logic models. In Proc. Machine Learning and Knowledge Discovery in Databases, Part II (eds. Hutter, F. et al.) 517–532 (Springer, 2020).
- 41. Wei, J. et al. Chain-of-thought prompting elicits reasoning in large language models. Adv. Neural Inf. Process. Syst. 35, 24824–24837

(2022).

- 42. Ho, N., Schmid, L. & Yun, S.-Y. Large language models are reasoning teachers. In Proc. 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) (eds. Rogers, A. et al.) 14852–14882 (ACL, 2023).
- 43. Yao, S. et al. ReAct: synergizing reasoning and acting in language models. In Proc. 11th International Conference on Learning Representations (OpenReview, 2023).
- 44. Zelikman, E., Wu, Y., Mu, J. & Goodman, N. Star: bootstrapping reasoning with reasoning. Adv. Neural Inf. Process. Syst. 35, 15476–15488 (2022).
- 45. Zhao, Z.-W., del Cueto, M. & Troisi, A. Limitations of machine learning models when predicting compounds with completely new chemistries: possible improvements applied to the discovery of new non-fullerene acceptors. Digit. Discov. 1, 266–276 (2022).
- 46. Vaucher, A. C. et al. Inferring experimental procedures from text-based representations of chemical reactions. Nat. Commun. 12, 2573 (2021).
- 47. Schwaller, P. et al. Mapping the space of chemical reactions using attention-based neural networks. Nat. Mach. Intell. 3, 144–152

(2021).

- 48. RXN for Chemistry. rxn4Chemistry. GitHub https://github.com/ rxn4chemistry/rxn4chemistry (2020).
- 49. Thakkar, A., Kogej, T., Reymond, J.-L., Engkvist, O. & Bjerrum, E. J. Datasets and their influence on the development of computer assisted synthesis planning tools in the pharmaceutical domain. Chem. Sci. 11, 154–168 (2020).
- 50. Thakkar, A., Selmi, N., Reymond, J.-L., Engkvist, O. & Bjerrum, E. J. ‘Ring breaker’: neural network driven synthesis prediction of the ring system chemical space. J. Med. Chem. 63, 8791–8808

(2020).

- 51. Yang, Z. et al. Mm-react: prompting ChatGPT for multimodal reasoning and action. Preprint at https://arxiv.org/abs/2303.11381

(2023).

- 52. Shen, Y. et al. Hugginggpt: solving AI tasks with chatgpt and its friends in huggingface. Poster at Advances in Neural Information Processing Systems 36 (2023).
- 53. Karpas, E. et al. Mrkl systems: a modular, neuro-symbolic architecture that combines large language models, external knowledge sources and discrete reasoning. Preprint at https:// arxiv.org/abs/2205.00445 (2022).
- 54. Boiko, D. A., MacKnight, R., Kline, B. & Gomes, G. Autonomous chemical research with large language models. Nature 624, 570–578 (2023).
- 55. RoboRXN. IBM https://research.ibm.com/science/ibm-roborxn/

(2021).

- 56. Wittkopp, A. & Schreiner, P. R. Metal-free, noncovalent catalysis of Diels-Alder reactions by neutral hydrogen bond donors in organic solvents and in water. Chem. Eur. J. 9, 407–414 (2003).
- 57. Schreiner, P. R. & Wittkopp, A. H-bonding additives act like Lewis acid catalysts. Org. Lett. 4, 217–220 (2002).


- 58. Herrera, R. P., Sgarzani, V., Bernardi, L. & Ricci, A. Catalytic enantioselective friedel-crafts alkylation of indoles with nitroalkenes by using a simple thiourea organocatalyst. Angew. Chem. Int. Ed. Engl. 44, 6576–6579 (2005).
- 59. Okino, T., Hoashi, Y. & Takemoto, Y. Enantioselective Michael reaction of malonates to nitroolefins catalyzed by bifunctional organocatalysts. J. Am. Chem. Soc. 125, 12672–12673 (2003).
- 60. Joung, J. F., Han, M., Jeong, M. & Park, S. DB for chromophore. figsharehttps://figshare.com/articles/dataset/DB_for_chromophore/ 12045567 (2020).
- 61. Lowe, D. M. Extraction of Chemical Structures and Reactions from the Literature. PhD thesis, Univ. of Cambridge (2012).
- 62. Wu, Z. et al. Moleculenet: a benchmark for molecular machine learning. Chem. Sci. 9, 513–530 (2018).
- 63. Liu, Y. et al. G-Eval: NLG evaluation using GPT-4 with better human alignment. In Proc. Conference on Empirical Methods in Natural Language Processing (eds. Bouamor, H. et al.) 2511–2522 (ACL, 2023).
- 64. Eloundou, T., Manning, S., Mishkin, P. & Rock, D. GPTs are GPTs: an early look at the labor market impact potential of large language models. Preprint at https://arxiv.org/abs/2303.10130 (2023).
- 65. Grzybowski, B. A., Badowski, T., Molga, K. & Szymkuc, S. Network search algorithms and scoring functions for advanced-level computerized synthesis planning. Wiley Interdiscip. Rev. Comput. Mol. Sci. 13, e1630 (2023).
- 66. Thakkar, A. et al. Artificial intelligence and automation in computer aided synthesis planning. React. Chem. Eng. 6, 27–51

(2021).

- 67. Urbina, F., Lentzos, F., Invernizzi, C. & Ekins, S. Dual use of artificial-intelligence-powered drug discovery. Nat. Mach. Intell. 4, 189–191 (2022).
- 68. Urbina, F., Lentzos, F., Invernizzi, C. & Ekins, S. A teachable moment for dual-use. Nat. Mach. Intell. 4, 607–607 (2022).
- 69. Campbell, Q. L., Herington, J. & White, A. D. Censoring chemical data to mitigate dual use risk. Preprint at https://arxiv.org/ abs/2304.10510 (2023).
- 70. Gao, L., Schulman, J. & Hilton, J. Scaling laws for reward model overoptimization. In Proc. International Conference on Machine Learning (eds Krause, A. et al.) 10835–10866 (PMLR, 2023).
- 71. Radford, A. et al. Improving language understanding by generative pre-training. OpenAI blog https://cdn.openai.com/ research-covers/language-unsupervised/language_understanding_ paper.pdf (2018).
- 72. Li, B. et al. Trustworthy AI: from principles to practices. ACM Comput. Surv. 55, 1–46 (2021).
- 73. Hocky, G. M. & White, A. D. Natural language processing models that automate programming will transform chemistry research and teaching. Dig. Discov. 1, 79–83 (2022).
- 74. Henderson, P. et al. Foundation models and fair use. Preprint at https://arxiv.org/abs/2303.15715 (2023).
- 75. Askell, A., Brundage, M. & Hadfield, G. The role of cooperation in responsible AI development. Preprint at https://arxiv.org/ abs/1907.04534 (2019).
- 76. Neufville, R. D. & Baum, S. D. Collective action on artificial intelligence: a primer and review. Technol. Soc. 66, 101649 (2021).
- 77. Touvron, H. et al. Llama: open and efficient foundation language models. Preprint at https://arxiv.org/abs/2302.13971 (2023).
- 78. Chiang, W.-L. et al. Vicuna: an open-source chatbot impressing GPT-4 with 90%* ChatGPT quality. LMSYS Org. https://lmsys.org/ blog/2023-03-30-vicuna/ (2023).
- 79. Mukherjee, S. et al. Orca: progressive learning from complex explanation traces of GPT-4. Preprint at https://arxiv.org/abs/ 2306.02707 (2023).
- 80. Chase, H. LangChain. GitHub https://github.com/hwchase17/ langchain (2022).


- 81. Press, O. et al. Measuring and narrowing the compositionality gap in language models. In Proc. Association for Computational Linguistics: EMNLP (eds. Bouamor, H. et al.) 5687–5711 (ACL, 2023).
- 82. Google search API. SerpApi https://serpapi.com/ (2023).
- 83. Neelakantan, A. et al. Text and code embeddings by contrastive pre-training. Preprint at https://arxiv.org/abs/2201.10005 (2022).
- 84. Johnson, J., Douze, M. & Jégou, H. Billion-scale similarity search with GPUs. IEEE Trans. Big Data 7, 535–547 (2019).
- 85. ChemSpace https://chem-space.com/ (2023).
- 86. National Center for Biotechnology Information. PubChem. NIH https://pubchem.ncbi.nlm.nih.gov/ (2023).
- 87. Medina, J. & White, A. D. Bloom filters for molecules. J. Cheminf. 15, 95 (2023).
- 88. Irwin, J. J. et al. Zinc20—a free ultralarge-scale chemical database for ligand discovery. J. Chem. Inf. Model. 60, 6065–6073 (2020).
- 89. Chemical Abstracts Service. CAS registry number. CAS www.cas. org/content/cas-registry (2023).
- 90. Tanimoto, T. T. An Elementary Mathematical Theory of Classification and Prediction (IBM, 1958).
- 91. Rogers, D. & Hahn, M. Extended-connectivity fingerprints. J. Chem. Inf. Model. 50, 742–754 (2010).
- 92. White, A. D. Synspace. GitHub https://github.com/whitead/ synspace (2023).
- 93. Wellawatte, G. P., Seshadri, A. & White, A. D. Model agnostic generation of counterfactual explanations for molecules. Chem. Sci. 13, 3697–3705 (2022).
- 94. Hartenfeller, M. et al. A collection of robust organic synthesis reactions for in silico molecule design. J. Chem. Inf. Model. 51, 3093–3098 (2011).
- 95. Yang, Q. et al. Molecular transformer unifies reaction prediction and retrosynthesis across pharma chemical space. Chem. Commun. 55, 12152–12155 (2019).
- 96. Purchasable Mcule. Mcule https://purchasable.mcule.com/

(2023).

- 97. RDKit: open-source cheminformatics (RDKit, 2023); www.rdkit.org
- 98. Chemical weapons convention, annex on chemicals, b. schedules of chemicals. OPCW www.opcw.org/ chemical-weapons-convention/annexes/annex-chemicals/ annex-chemicals (2024).
- 99. The Australia Group. Australia Group common control lists: chemical weapons precursors. Department of Foreign Affairs and Trade www.dfat.gov.au/publications/minisite/ theaustraliagroupnet/site/en/controllists.html (2023).
- 100. Namerxn (NextMove Software, 2023); www.nextmovesoftware. com/namerxn.html
- 101. Carey, J. S., Laffan, D., Thomson, C. & Williams, M. T. Analysis of the reactions used for the preparation of drug candidate molecules. Org. Biomol. Chem. 4, 2337–2347 (2006).
- 102. Bran, A. & Cox, S. ur-whitelab/chemcrow-runs: Zendo release. Zenodo https://doi.org/10.5281/zenodo.10884645 (2024).
- 103. Bran, A., Cox, S., White, A. & Schwaller, P. ur-whitelab/ chemcrow-public: v0.3.24. Zenodo https://doi.org/10.5281/ zenodo.10884639 (2024).


### Acknowledgements

A.M.B., O.S. and P.S. acknowledge support from NCCR Catalysis (grant no. 180544), a National Centre of Competence in Research funded by the Swiss National Science Foundation. S.C. and A.D.W. acknowledge support from the National Science Foundation under grant no. 1751471. Research reported in this work was supported by the National Institute of General Medical Sciences of the National Institutes of Health under award no. R35GM137966. We thank the wider RXN for Chemistry team for the support and for having granted limited access to the platform for the sole scope of executing the reported syntheses. We thank M. Lederbauer and J. Marulanda for helping with the illustrations in Fig. 1.

### Author contributions

Peer review information Nature Machine Intelligence thanks Michael Heinzinger and the other, anonymous, reviewer(s) for their contribution to the peer review of this work.

A.M.B. and S.C. contributed to methodology, model creation, writing, visualization, guardrails and assessment. O.S. and C.B. contributed to methodology, laboratory experiments and assessment. A.D.W. contributed to conceptualization, methodology, model creation, writing, funding and project supervision. P.S. contributed to conceptualization, methodology, model creation, assessment, writing, funding and project supervision.

Reprints and permissions informationis available at www.nature.com/reprints.

Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

### Funding

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons. org/licenses/by/4.0/.

Open access funding provided by EPFL Lausanne.

### Competing interests

A.D.W. has served as a paid consultant for evaluating AI model safety at OpenAI. The other authors declare no competing interests.

### Additional information

Supplementary information The online version contains supplementary material available at https://doi.org/10.1038/s42256-024-00832-8.

Correspondence and requests for materialsshould be addressed to Andrew D. White or Philippe Schwaller.

© The Author(s) 2024

![image 7](M. Bran et al._2024_Augmenting large language models with chemistry tools_images/imageFile7.png)

