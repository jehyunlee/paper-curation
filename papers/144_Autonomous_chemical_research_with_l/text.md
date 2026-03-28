# Autonomous chemical research with large language models

Daniil A. Boiko1, Robert MacKnight1, Ben Kline2 & Gabe Gomes1,3,4✉

https://doi.org/10.1038/s41586-023-06792-0 Received: 20 April 2023 Accepted: 27 October 2023 Published online: 20 December 2023 Open access

Transformer-based large language models are making significant strides in various fields, such as natural language processing1–5, biology6,7, chemistry8–10 and computer programming11,12. Here, we show the development and capabilities of Coscientist, an artificial intelligence system driven by GPT-4 that autonomously designs, plans and performs complex experiments by incorporating large language models empowered by tools such as internet and documentation search, code execution and experimental automation. Coscientist showcases its potential for accelerating research across six diverse tasks, including the successful reaction optimization of palladium-catalysed cross-couplings, while exhibiting advanced capabilities for (semi-)autonomous experimental design and execution. Our findings demonstrate the versatility, efficacy and explainability of artificial intelligence systems like Coscientist in advancing research.

Check for updates

![image 1](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile1.png)

Large language models (LLMs), particularly transformer-based models, are experiencing rapid advancements in recent years. These models have been successfully applied to various domains, including natural language1–5, biological6,7 and chemical research8–10 as well as code generation11,12. Extreme scaling of models13, as demonstrated by OpenAI, has led to significant breakthroughs in the field1,14. Moreover, techniques such as reinforcement learning from human feedback15 can considerably enhance the quality of generated text and the models’ capability to perform diverse tasks while reasoning about their decisions16.

can use tools to browse the internet and relevant documentation, use robotic experimentation application programming interfaces (APIs) and leverage other LLMs for various tasks. This work has been done independently and in parallel to other works on autonomous agents23–25, with ChemCrow26 serving as another example in the chemistry domain. In this paper, we demonstrate the versatility and performance of Coscientist in six tasks: (1) planning chemical syntheses of known compounds using publicly available data; (2) efficiently searching and navigating through extensive hardware documentation; (3) using documentation to execute high-level commands in a cloud laboratory; (4) precisely controlling liquid handling instruments with low-level instructions; (5) tackling complex scientific tasks that demand simultaneous use of multiple hardware modules and integration of diverse data sources; and (6) solving optimization problems requiring analyses of previously collected experimental data.

On 14 March 2023, OpenAI released their most capable LLM to date, GPT-414. Although specific details about the model training, sizes and data used are limited in GPT-4’s technical report, OpenAI researchers have provided substantial evidence of the model’s exceptional problem-solving abilities. Those include—but are not limited to—high percentiles on the SAT and BAR examinations, LeetCode challenges and contextual explanations from images, including niche jokes14. Moreover, the technical report provides an example of how the model can be used to address chemistry-related problems.

### Coscientist system architecture

Simultaneously, substantial progress has been made toward the automation of chemical research. Examples range from the autonomous discovery17,18 and optimization of organic reactions19 to the development of automated flow systems20,21 and mobile platforms22.

Coscientist acquires the necessary knowledge to solve a complex problem by interacting with multiple modules (web and documentation search, code execution) and by performing experiments. The main module (‘Planner’) has the goal of planning, based on the user input by invoking the commands defined below. The Planner is a GPT-4 chat completion instance serving the role of an assistant. The initial user input along with command outputs are treated as user messages to the Planner. System prompts (static inputs defining the LLMs’ goals) for the Planner are engineered1,27 in a modular fashion, described as four commands that define the action space: ‘GOOGLE’, ‘PYTHON’, ‘DOCUMENTATION’ and ‘EXPERIMENT’. The Planner calls on each of these commands as needed to collect knowledge. The GOOGLE command is responsible for searching the internet with the ‘Web searcher’ module, which is another LLM itself.

The combination of laboratory automation technologies with powerful LLMs opens the door to the development of a sought-after system that autonomously designs and executes scientific experiments. To accomplish this, we intended to address the following questions. What are the capabilities of LLMs in the scientific process? What degree of autonomy can we achieve? How can we understand the decisions made by autonomous agents?

In this work, we present a multi-LLMs-based intelligent agent (hereafter simply called Coscientist) capable of autonomous design, planning and performance of complex scientific experiments. Coscientist

1Department of Chemical Engineering, Carnegie Mellon University, Pittsburgh, PA, USA. 2Emerald Cloud Lab, South San Francisco, CA, USA. 3Department of Chemistry, Carnegie Mellon University, Pittsburgh, PA, USA. 4Wilton E. Scott Institute for Energy Innovation, Carnegie Mellon University, Pittsburgh, PA, USA. ✉e-mail: gabegomes@cmu.edu

- a
- b
- c


| |
|---|


The module does not use LLMs

The module uses LLMs

Input prompt from scientist

Command used by LLM

![image 2](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile2.png)

![image 3](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile3.png)

Coscientist

Google Search API

GOOGLE

Physical world hardware

![image 4](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile4.png)

GOOGLE EXPERIMENT

Web searcher Planner Automation

- • Cloud laboratory
- • Liquid handler
- • Manual experimentation


BROWSE

Internet

|Code| |
|---|---|
|submission| |


PYTHON

DOCUMENTATION

Docs index Retrieval and

Docker container

Hardware API documentation

Code execution summarization

Docs searcher

Performed experiments to validate the agent

- – Controlling a liquid handler
- – Using a liquid handler and UV-Vis together


Generating SLL code for a cloud laboratory

Searching for organic syntheses online

- – Performing cross-coupling reactions
- – Optimizing reaction conditions


![image 5](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile5.png)

![image 6](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile6.png)

![image 7](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile7.png)

![image 8](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile8.png)

![image 9](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile9.png)

![image 10](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile10.png)

![image 11](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile11.png)

Liquid handler’s pipettes

Heater–shaker module

Laptop, accessing a web server with deployed Coscientist

![image 12](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile12.png)

- Fig. 1 | The system’s architecture.a, Coscientist is composed of multiple modules that exchange messages. Boxes with blue background represent LLM modules, the Planner module is shown in green, and the input prompt is in red. White boxes represent modules that do not use LLMs.b, Types of experiments


performed to demonstrate the capabilities when using individual modules or their combinations.c, Image of the experimental setup with a liquid handler. UV-Vis, ultraviolet visible.

The PYTHON command allows the Planner to perform calculations to prepare the experiment using a ‘Code execution’ module. The EXPERIMENT command actualizes ‘Automation’ through APIs described by the DOCUMENTATION module. Like GOOGLE, the DOCUMENTATION command provides information to the main module from a source, in this case documentation concerning the desired API. In this study, we have demonstrated the compatibility with the Opentrons Python API and the Emerald Cloud Lab (ECL) Symbolic Lab Language (SLL). Together, these modules make up Coscientist, which receives a simple plain text input prompt from the user (for example, “perform multiple Suzuki reactions”). This architecture is depicted in Fig. 1.

### Web search module

To demonstrate one of the functionalities of the Web Searcher module, we designed a test set composed of seven compounds to synthesize, as presented in Fig. 2a. The Web Searcher module versions are represented as ‘search-gpt-4’ and ‘search-gpt-3.5-turbo’. Our baselines include OpenAI’s GPT-3.5 and GPT-4, Anthropic’s Claude 1.328 and Falcon-40B-Instruct29—considered one of the best open-source models at the time of this experiment as per the OpenLLM leaderboard30.

We prompted every model to provide a detailed compound synthesis, ranking the outputs on the following scale (Fig. 2):

- • 5 for a very detailed and chemically accurate procedure description
- • 4 for a detailed and chemically accurate description but without reagent quantities
- • 3 for a correct chemistry description that does not include stepby-step procedure
- • 2 for extremely vague or unfeasible descriptions
- • 1 for incorrect responses or failure to follow instructions
- • All scores below 3 indicate task failure. It is important to note that all answers between 3 and 5 are chemically correct but offer varying levels of detail. Despite our attempts to better formalize the scale, labelling is inherently subjective and so, may be different between the labelers.


Furthermore, some of the commands can use subactions. The GOOGLE command is capable of transforming prompts into appropriate web search queries, running them against the Google Search API, browsing web pages and funneling answers back to the Planner. Similarly, the DOCUMENTATION command performs retrieval and summarization of necessary documentation (for example, robotic liquid handler or a cloud laboratory) for Planner to invoke the EXPERIMENT command.

The PYTHON command performs code execution (not reliant upon any language model) using an isolated Docker container to protect the users’ machine from any unexpected actions requested by the Planner. Importantly, the language model behind the Planner enables code to be fixed in case of software errors. The same applies to the EXPERIMENT command of the Automation module, which executes generated code on corresponding hardware or provides the synthetic procedure for manual experimentation.

Across non-browsing models, the two versions of the GPT-4 model performed best, with Claude v.1.3 demonstrating similar performance. GPT-3 performed significantly worse, and Falcon 40B failed in most cases. All non-browsing models incorrectly synthesized ibuprofen

a

Average label

- 0

- 1

- 2

- 3

- 4

- 5


| | |
|---|---|
| | |


| | |
|---|---|
| | |


| | |
|---|---|
| | |


| | |
|---|---|
| | |


| | |
|---|---|
| | |


| | |
|---|---|
| | |


Level of detail

Correctness

Acetaminophen Aspirin Benzoic acid Ethylacetate Ibuprofen Nitroaniline Phenolphthalein

Task complexity

gpt-4-0314 gpt-3.5-turbo

claude-1.3 falcon-40b-instruct

Acceptable performance search-gpt-4

search-gpt-3.5-turbo

gpt-4

##### b

Incorrect synthesis steps but makes chemical sense (GPT-3.5, no search)

Correct synthesis, including detailed experimental procedure (GPT-4 with search)

5

2

- N+
- O


- N+
- O


- N+
- O


HNO3

HNO3

Ac2O/AcOH HCl/H2O

–O

–O NH2

–O NH2

NH

re ux

H2SO4 NH

H2SO4

NH2

NH2

O

O

##### c

Incorrect synthesis steps, does not make chemical sense (GPT-4, no search)

1

O

Cl KMnO4

O

O

- (1) C2H5COCl, py
- (2) NaOH, H2O


Ac2O

Cl2

OH

OH

OH

UV light

AlCl3, HCl

NaOH, H2O

3

Correct synthesis logic but no reagents and experimental procedure

O

O OH Cl MgCl

OH

- Fig. 2 | Coscientist’s capabilities in chemical synthesis planning tasks.a, Comparison of various LLMs on compound synthesis benchmarks. Error bars represent s.d. values.b, Two examples of generated syntheses of nitroaniline.c, Two example of generated syntheses of ibuprofen. UV, ultraviolet.


(Fig. 2c). Nitroaniline is another example; although some generalization of chemical knowledge might inspire the model to propose direct nitration, this approach is not experimentally applicable as it would produce a mixture of compounds with a very minor amount of the product (Fig. 2b). Only the GPT-4 models occasionally provided the correct answer.

### Documentation search module

Addressing the complexities of software components and their interactions is crucial for integrating LLMs with laboratory automation. A key challenge lies in enabling Coscientist to effectively utilize technical documentation. LLMs can refine their understanding of common APIs, such as the Opentrons Python API37, by interpreting and learning from relevant technical documentation. Furthermore, we show how GPT-4 can learn how to programme in the ECL SLL.

The GPT-4-powered Web Searcher significantly improves on synthesis planning. It reached maximum scores across all trials for acetaminophen, aspirin, nitroaniline and phenolphthalein (Fig. 2b). Although it was the only one to achieve the minimum acceptable score of three for ibuprofen, it performed lower than some of the other models for ethylacetate and benzoic acid, possibly because of the widespread nature of these compounds. These results show the importance of grounding LLMs to avoid ‘hallucinations’31. Overall, the performance of GPT-3.5-enabled Web Searcher trailed its GPT-4 competition, mainly because of its failure to follow specific instructions regarding output format.

Our approach involved equipping Coscientist with essential documentation tailored to specific tasks (as illustrated in Fig. 3a), allowing it to refine its accuracy in using the API and improve its performance in automating experiments.

Information retrieval systems are usually based on two candidate selection approaches: inverted search index and vector database38–41. For the first one, each unique word in the search index is mapped to the documents containing it. At inference time, all documents containing words from a query are selected and ranked based on various manually defined formulas42. The second approach starts by embedding the documents with neural networks or as term frequency–inverse document frequency embedding vectors43, followed by the construction of a vector database. Retrieval of similar vectors from this database occurs at inference time, usually using one of the approximate nearest neighbour search algorithms44. When strategies such as Transformer

Extending the Planner’s action space to leverage reaction databases, such as Reaxys32 or SciFinder33, should significantly enhance the system’s performance (especially for multistep syntheses). Alternatively, analysing the system’s previous statements is another approach to improving its accuracy. This can be done through advanced prompting strategies, such as ReAct34, Chain of Thought35 and Tree of Thoughts36.

a OT-2 implementation

b Valid OT-2 API code

Initial OT-2 API documentation request from Planner

API usage information prompt-to-OT-2

Planner

# Heat and shake the reaction hs_mod.set_target_temperature(75) hs_mod.wait_for_temperature() hs_mod.set_and_wait_for_shake_speed(500)

Query

embedding [ ... ]

DOCUMENTATION heat and shake mixtures using the OT-2 robot

# Deactivate heater and shaker

Vector search

hs_mod.deactivate_heater() hs_mod.deactivate_shaker() hs_mod.open_labware_latch()

[ ... ]

Precompiled text embeddings for sections of API documentation

...

[ ... ]

[ ... ]

‘Hardware modules’

Proper usage of heater–shaker module

Initial cloud laboratory API documentation request from Planner

c

d Valid ECL SLL code

ECL implementation

Prompt-to-SLL

Planner

# Generated HPLC Experiment SLL Function Call ExperimentHPLC[

Query embedding

Object[Sample, ...], Instrument -> Model[Instrument, ...]

[ ... ]

DOCUMENTATION analyse a mixture to see what is in it

]

ExperimentHPLC[Samples] => Protocol Experimental Principles... Instrumentation... Experiment Options... Sample Parameters...

Vector search

Text embeddings for 114 ECL experiment functions

[ ... ]

...

Targeted experiment options are set by the Planner

[ ... ]

[ ... ]

...

- Fig. 3 | Overview of documentation search.a, Prompt-to-code through ada embedding and distance-based vector search.b, Example of code for using OT-2’s heater–shaker module.c, Prompt-to-function/prompt-to-SLL (to symbolic


laboratory language) through supplementation of documentation.d, Example of valid ECL SLL code for performing high-performance liquid chromatography (HPLC) experiments.

models are used, there are more chances to account for synonyms natively without doing synonym-based query expansion, as would be done in the first approach45.

was injected along with the analyte’s solution. This demonstrates the importance of development of automated techniques for quality control in cloud laboratories. Follow-up experiments leveraging web search to specify and/or refine additional experimental parameters (column chemistry, buffer system, gradient and so on) would be required to optimize the experimental results. Further details on this investigation are in Supplementary Information section ‘Analysis of ECL documentation search results’.

Following the second approach, all sections of the OT-2 API documentation were embedded using OpenAI’s ada model. To ensure proper use of the API, an ada embedding for the Planner’s query was generated, and documentation sections are selected through a distance-based vector search. This approach proved critical for providing Coscientist with information about the heater–shaker hardware module necessary for performing chemical reactions (Fig. 3b).

A separate prompt-to-samples investigation, investigation 3, was conducted by providing a catalogue of available samples, enabling the identification of relevant stock solutions that are on ECL’s shelves. To showcase this feature, we provide the Docs searcher module with all 1,110 Model samples from the catalogue. By simply providing a search term (for example, ‘Acetonitrile’), all relevant samples are returned. This is also available in Supplementary Information.

A greater challenge emerges when applying this approach to a more diverse robotic ecosystem, such as the ECL. Nonetheless, we can explore the effectiveness of providing information about the ECL SLL, which is currently unknown to the GPT-4 model. We conducted three separate investigations concerning the SLL: (1) prompt-to-function; (2) prompt-to-SLL; and (3) prompt-to-samples. Those investigations are detailed in Supplementary Information section ‘ECL experiments’.

### Controlling laboratory hardware

For investigation 1, we provide the Docs searcher with a documentation guide from ECL pertaining to all available functions for running experiments46. Figure 3c summarizes an example of the user providing a simple prompt to the system, with the Planner receiving relevant ECL functions. In all cases, functions are correctly identified for the task.

Access to documentation enables us to provide sufficient information for Coscientist to conduct experiments in the physical world. To initiate the investigation, we chose the Opentrons OT-2, an open-source liquid handler with a well-documented Python API. The ‘Getting Started’ page from its documentation was supplied to the Planner in the system prompt. Other pages were vectorized using the approach described above. For this investigation, we did not grant access to the internet (Fig. 4a).

Figure 3c,d continues to describe investigation 2, the prompt-to-SLL investigation. A single appropriate function is selected for the task, and the documentation is passed through a separate GPT-4 model to perform code retention and summarization. After the complete documentation has been processed, the Planner receives usage information to provide EXPERIMENT code in the SLL. For instance, we provide a simple example that requires the ‘ExperimentHPLC’ function. Proper use of this function requires familiarity with specific ‘Models’ and ‘Objects’ as they are defined in the SLL. Generated code was successfully executed at ECL; this is available in Supplementary Information. The sample was a caffeine standard sample. Other parameters (column, mobile phases, gradients) were determined by ECL’s internal software (a high-level description is in Supplementary Information section ‘HPLC experiment parameter estimation’). Results of the experiment are provided in Supplementary Information section ‘Results of the HPLC experiment in the cloud lab’. One can see that the air bubble

We started with simple plate layout-specific experiments. Straightforward prompts in natural language, such as “colour every other line with one colour of your choice”, resulted in accurate protocols. When executed by the robot, these protocols closely resembled the requested prompt (Fig. 4b–e).

Ultimately, we aimed to assess the system’s ability to integrate multiple modules simultaneously. Specifically, we provided the ‘UVVIS’ command, which can be used to pass a microplate to plate reader working in the ultraviolet–visible wavelength range. To evaluate Coscientist’s capabilities to use multiple hardware tools, we designed a toy task; in 3 wells of a 96-well plate, three different colours are present—red, yellow and blue. The system must determine the colours and their positions on the plate without any prior information.

- a
- b c Colour every other row of a 96-well plate with one colour of your choice. Remember that for me to see it, you should put at least 10  l. <setup description>


“Getting started” in system prompt

Vectorized tutorial and API reference

Open source

liquid handling system UV-Vis plate reader

DOCUMENTATION PYTHON

Docs searcher Code execution

EXPERIMENT UVVIS

Planner

|![image 13](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile13.png)<br><br>![image 14](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile14.png)|
|---|


|![image 15](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile15.png)<br><br>![image 16](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile16.png)|
|---|


Draw a red cross using food colouring in the center of 96-well plate.

<setup description>

##### d e

|![image 17](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile17.png)<br><br>![image 18](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile18.png)|
|---|


|![image 19](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile19.png)<br><br>![image 20](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile20.png)|
|---|


Draw a 3 × 3 rectangle using yellow colour at upper left part of the 96-well plate. Remember that for me to see it, you should put at least 10  l.

Draw a blue diagonal starting from lower left (H1) in the 96-well plate. Remember that for me to see it, you should put at least 10  l.

<setup description>

<setup description>

- Fig. 4 | Robotic liquid handler control capabilities and integration with analytical tools.a, Overview of Coscientist’s configuration.b, Drawing a red cross. c, Colouring every other row.d, Drawing a yellow rectangle.e, Drawing a blue diagonal.


The Coscientist’s first action was to prepare small samples of the original solutions (Extended Data Fig. 1). Ultraviolet-visible measurements were then requested to be performed by the Coscientist (Supplementary Information section ‘Solving the colours problem’ and Supplementary Fig. 1). Once completed, Coscientist was provided with a file name containing a NumPy array with spectra for each well of the microplate. Coscientist subsequently generated Python code to identify the wavelengths with maximum absorbance and used these data to correctly solve the problem, although it required a guiding prompt asking it to think through how different colours absorb light.

base DBU (1,8-diazabicyclo[5.4.0]undec-7-ene) is selected more often with the PEPPSI–IPr (PEPPSI, pyridine-enhanced precatalyst preparation stabilization and initiation; IPr, 1,3-bis(2,6-diisopropylphenyl) imidazol-2-ylidene) complex, with that preference switching in Sonogashira reaction experiments; likewise, bromobenzene is chosen more often for Suzuki than for Sonogashira couplings. Additionally, the model can provide justifications on specific choices (Fig. 5g), demonstrating the ability to operate with concepts such as reactivity and selectivity (more details are in Supplementary Information section ‘Analysis of behaviour across multiple runs’). This capability highlights a potential future use case to analyse the reasoning of the LLMs used by performing experiments multiple times. Although the Web Searcher visited various websites (Fig. 5h), overall Coscientist retrieves Wikipedia pages in approximately half of cases; notably, American Chemical Society and Royal Society of Chemistry journals are amongst the top five sources.

### Integrated chemical experiment design

We evaluated Coscientist’s ability to plan catalytic cross-coupling experiments by using data from the internet, performing the necessary calculations and ultimately, writing code for the liquid handler. To increase complexity, we asked Coscientist to use the OT-2 heater–shaker module released after the GPT-4 training data collection cutoff. The available commands and actions supplied to the Coscientist are shown in Fig. 5a. Although our setup is not yet fully automated (plates were moved manually), no human decision-making was involved.

Coscientist then calculates the required volumes of all reactants and writes a Python protocol for running the experiment on the OT-2 robot. However, an incorrect heater–shaker module method name was used. Upon making this mistake, Coscientist uses the Docs searcher module to consult the OT-2 documentation. Next, Coscientist modifies the protocol to a corrected version, which ran successfully (Extended Data Fig. 2). Subsequent gas chromatography–mass spectrometry analysis of the reaction mixtures revealed the formation of the target products for both reactions. For the Suzuki reaction, there is a signal in the chromatogram at 9.53 min where the mass spectra match the mass spectra for biphenyl (corresponding molecular ion mass-to-charge ratio and fragment at 76 Da) (Fig. 5i). For the Sonogashira reaction, we see a signal at 12.92 min with a matching molecular ion mass-to-charge ratio; the fragmentation pattern also looks very close to the one from the spectra of the reference compound (Fig. 5j). Details are in Supplementary Information section ‘Results of the experimental study’.

The test challenge for Coscientist’s complex chemical experimentation capabilities was designed as follows. (1) Coscientist is provided with a liquid handler equipped with two microplates (source and target plates). (2) The source plate contains stock solutions of multiple reagents, including phenyl acetylene and phenylboronic acid, multiple aryl halide coupling partners, two catalysts, two bases and the solvent to dissolve the sample (Fig. 5b). (3) The target plate is installed on the OT-2 heater–shaker module (Fig. 5c). (4) Coscientist’s goal is to successfully design and perform a protocol for Suzuki– Miyaura and Sonogashira coupling reactions given the available resources.

To start, Coscientist searches the internet for information on the requested reactions, their stoichiometries and conditions (Fig. 5d). The correct coupling partners are selected for the corresponding reactions. Designing and performing the requested experiments, the strategy of Coscientist changes among runs (Fig. 5f). Importantly, the system does not make chemistry mistakes (for instance, it never selects phenylboronic acid for the Sonogashira reaction). Interestingly, the

Although this example requires Coscientist to reason on which reagents are most suitable, our experimental capabilities at that point limited the possible compound space to be explored. To address this, we performed several computational experiments to evaluate how a similar approach can be used to retrieve compounds from large compound libraries47. Figure 5e shows Coscientist’s performance across five common organic transformations, with outcomes depending on the

a

b

Source plate

Open source liquid handling system

DiPP

Cl

“Getting started” in system prompt

Vectorized tutorial and API reference

![image 21](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile21.png)

Cl

Cl

![image 22](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile22.png)

![image 23](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile23.png)

![image 24](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile24.png)

![image 25](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile25.png)

![image 26](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile26.png)

![image 27](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile27.png)

![image 28](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile28.png)

![image 29](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile29.png)

![image 30](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile30.png)

![image 31](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile31.png)

![image 32](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile32.png)

![image 33](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile33.png)

![image 34](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile34.png)

![image 35](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile35.png)

![image 36](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile36.png)

![image 37](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile37.png)

![image 38](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile38.png)

![image 39](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile39.png)

N

- A1 A2

C1 C2

- D1 D2
- E1


- B1 B2 B3 BB44


Ph3P Pd PPh3

N

Pd

![image 40](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile40.png)

![image 41](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile41.png)

![image 42](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile42.png)

![image 43](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile43.png)

![image 44](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile44.png)

![image 45](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile45.png)

![image 46](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile46.png)

![image 47](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile47.png)

![image 48](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile48.png)

![image 49](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile49.png)

![image 50](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile50.png)

![image 51](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile51.png)

![image 52](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile52.png)

![image 53](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile53.png)

![image 54](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile54.png)

![image 55](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile55.png)

![image 56](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile56.png)

![image 57](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile57.png)

![image 58](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile58.png)

![image 59](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile59.png)

Cl N

![image 60](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile60.png)

![image 61](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile61.png)

![image 62](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile62.png)

Docs searcher

![image 63](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile63.png)

Cl

B HO OH

![image 64](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile64.png)

![image 65](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile65.png)

![image 66](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile66.png)

![image 67](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile67.png)

![image 68](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile68.png)

![image 69](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile69.png)

![image 70](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile70.png)

![image 71](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile71.png)

![image 72](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile72.png)

![image 73](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile73.png)

![image 74](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile74.png)

![image 75](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile75.png)

![image 76](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile76.png)

![image 77](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile77.png)

![image 78](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile78.png)

![image 79](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile79.png)

![image 80](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile80.png)

![image 81](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile81.png)

![image 82](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile82.png)

![image 83](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile83.png)

![image 84](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile84.png)

![image 85](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile85.png)

EXPERIMENT

DOCUMENTATION

![image 86](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile86.png)

![image 87](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile87.png)

A1

![image 88](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile88.png)

![image 89](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile89.png)

DiPP

![image 90](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile90.png)

![image 91](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile91.png)

Planner

![image 92](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile92.png)

![image 93](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile93.png)

![image 94](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile94.png)

![image 95](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile95.png)

![image 96](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile96.png)

![image 97](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile97.png)

![image 98](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile98.png)

![image 99](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile99.png)

![image 100](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile100.png)

![image 101](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile101.png)

![image 102](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile102.png)

![image 103](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile103.png)

![image 104](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile104.png)

![image 105](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile105.png)

![image 106](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile106.png)

![image 107](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile107.png)

![image 108](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile108.png)

![image 109](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile109.png)

![image 110](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile110.png)

![image 111](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile111.png)

![image 112](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile112.png)

![image 113](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile113.png)

C1 C2

###### A2

![image 114](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile114.png)

![image 115](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile115.png)

R

UV-Vis plate reader

![image 116](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile116.png)

UVVIS

PYTHON

![image 117](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile117.png)

![image 118](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile118.png)

![image 119](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile119.png)

![image 120](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile120.png)

Code execution

![image 121](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile121.png)

![image 122](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile122.png)

![image 123](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile123.png)

![image 124](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile124.png)

![image 125](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile125.png)

![image 126](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile126.png)

![image 127](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile127.png)

![image 128](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile128.png)

![image 129](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile129.png)

![image 130](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile130.png)

![image 131](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile131.png)

![image 132](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile132.png)

![image 133](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile133.png)

![image 134](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile134.png)

![image 135](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile135.png)

![image 136](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile136.png)

![image 137](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile137.png)

![image 138](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile138.png)

![image 139](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile139.png)

![image 140](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile140.png)

![image 141](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile141.png)

![image 142](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile142.png)

![image 143](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile143.png)

![image 144](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile144.png)

![image 145](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile145.png)

![image 146](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile146.png)

![image 147](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile147.png)

![image 148](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile148.png)

- B1 — X = I, R = H
- B2 — X = Br, R = H
- B3 — X = Cl, R = H
- B4 — X = I, R = NO2


N

![image 149](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile149.png)

![image 150](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile150.png)

![image 151](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile151.png)

![image 152](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile152.png)

![image 153](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile153.png)

![image 154](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile154.png)

![image 155](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile155.png)

![image 156](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile156.png)

![image 157](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile157.png)

![image 158](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile158.png)

![image 159](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile159.png)

![image 160](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile160.png)

![image 161](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile161.png)

![image 162](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile162.png)

![image 163](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile163.png)

![image 164](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile164.png)

![image 165](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile165.png)

![image 166](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile166.png)

![image 167](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile167.png)

![image 168](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile168.png)

![image 169](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile169.png)

![image 170](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile170.png)

![image 171](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile171.png)

![image 172](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile172.png)

![image 173](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile173.png)

![image 174](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile174.png)

![image 175](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile175.png)

![image 176](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile176.png)

![image 177](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile177.png)

![image 178](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile178.png)

GOOGLE

N

![image 179](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile179.png)

![image 180](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile180.png)

![image 181](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile181.png)

![image 182](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile182.png)

![image 183](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile183.png)

![image 184](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile184.png)

![image 185](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile185.png)

![image 186](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile186.png)

![image 187](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile187.png)

![image 188](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile188.png)

![image 189](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile189.png)

![image 190](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile190.png)

![image 191](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile191.png)

![image 192](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile192.png)

![image 193](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile193.png)

![image 194](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile194.png)

![image 195](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile195.png)

![image 196](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile196.png)

![image 197](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile197.png)

![image 198](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile198.png)

![image 199](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile199.png)

![image 200](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile200.png)

![image 201](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile201.png)

![image 202](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile202.png)

![image 203](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile203.png)

![image 204](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile204.png)

![image 205](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile205.png)

![image 206](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile206.png)

N

Web searcher

Google Seach API

Internet

![image 207](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile207.png)

![image 208](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile208.png)

![image 209](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile209.png)

![image 210](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile210.png)

![image 211](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile211.png)

![image 212](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile212.png)

![image 213](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile213.png)

![image 214](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile214.png)

![image 215](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile215.png)

![image 216](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile216.png)

![image 217](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile217.png)

![image 218](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile218.png)

![image 219](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile219.png)

![image 220](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile220.png)

![image 221](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile221.png)

![image 222](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile222.png)

![image 223](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile223.png)

![image 224](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile224.png)

![image 225](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile225.png)

![image 226](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile226.png)

![image 227](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile227.png)

![image 228](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile228.png)

![image 229](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile229.png)

![image 230](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile230.png)

![image 231](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile231.png)

![image 232](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile232.png)

![image 233](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile233.png)

![image 234](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile234.png)

E1 — DMF D1 D2

X

...

c e

d

- 0

- 1

- 2

- 3

- 4

- 5


Diels–Alder reaction

Michael addition

The liquid handler setup scheme

Esteri cation

Buchwald–Hartwig amination

left pipette, 20 l single channel

User prompt

Mizoroki–Heck reaction

Total number of reactions

right pipette, 300 l single channel

10 11

Planner’s output

0.10

...

7 8 9

Total reactions proposed

Total reactions proposed

0.08

4 5 6

0.06

1 2 3

0.04

- 1 20 l tips
- 2 300 l tips 5 Source plate


0.02

(deep 96-well)

0

10 Heater–shaker module with target plate

...

0 0.05 0.10 Valid reactions

...

Average

| | |
|---|---|
| | |


Valid reaction number standard deviation

0 0.5 1.0 Valid reactions

Total reaction number standard deviation

...

f

g h i j

TIC (standard)

TIC (standard)

TIC

TIC

Suzuki

Sonogashira

Suzuki

Sonogashira

1.0

1.0

Rel. intensity

Rel. intensity

![image 235](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile235.png)

![image 236](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile236.png)

|0%|100%| | |
|---|---|---|---|
|66%|30%|1%|0%|
|91%|![image 237](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile237.png)<br><br>8%| | |
|89%|6%| | |
|8%| | | |


|100%|0%| | |
|---|---|---|---|
|84%|12%|0%|1%|
|![image 238](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile238.png)<br><br>84%|15%| | |
|75%|19%| | |
|10%| | | |


en.wikipedia.org

- A
- B
- C
- D
- E


- A
- B
- C
- D
- E


Reactivity/rates Required for the reaction

0.5

0.5

chem.libretexts.org

organic-chemistry.org

0

0

pubs.acs.org

10 20 Time (min)

10 20 Time (min)

All options are suitable

pubs.rsc.org

sciencedirect.com

1.0

1.0

Rel. intensity

Rel. intensity

Spectrum at 9.53 min

Spectrum at 12.92 min

onlinelibrary.wiley.com

Commonly used

sigmaaldrich.com

0.5

0.5

encyclopedia.pub

Availability

0

0

1 2 3 4

1 2 3 4

hepatochem.com

0 100 200 m/z

0 100 200 m/z

ncbi.nlm.nih.gov

Leaving groups

reagents.acsgcipr.org

1.0

1.0

|![image 239](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile239.png)<br><br>92% 75%<br><br>8% 25%|
|---|


|![image 240](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile240.png)<br><br>93% 45%<br><br>7% 55%|
|---|


Rel. intensity

Rel. intensity

Spectrum of biphenyl standard

Spectrum of tolane standard

researchgate.net

- D1
- D2


- D1
- D2


Side reactions

semanticscholar.org

0.5

0.5

arkat-usa.org

Higher selectivity

0

0

C1 C2

C1 C2

B1 B2 B3 B4

B1 B2 B3 B4

0 0.5 Fraction of URLs

0 100 200 m/z

0 100 200 m/z

- Fig. 5 | Cross-coupling Suzuki and Sonogashira reaction experiments designed and performed by Coscientist.a, Overview of Coscientist’s configuration.b, Available compounds (DMF, dimethylformamide; DiPP, 2,6-diisopropylphenyl). c, Liquid handler setup. d, Solving the synthesis problem. e, Comparison of reagent selection performance with a large dataset.f, Comparison of reagent choices across multiple runs.g, Overview of justifications made when selecting various aryl halides.h, Frequency of


visited URLs.i, Total ion current (TIC) chromatogram of the Suzuki reaction mixture (top panel) and the pure standard, mass spectra at 9.53 min (middle panel) representing the expected reaction product and mass spectra of the pure standard (bottom panel).j, TIC chromatogram of the Sonogashira reaction mixture (top panel) and the pure standard, mass spectra at 12.92 min (middle panel) representing the expected reaction product and mass spectra of the pure standard (bottom panel). Rel., relative.

queried reaction and its specific run (the GitHub repository has more details). For each reaction, Coscientist was tasked with generating reactions for compounds from a simplified molecular-input line-entry system (SMILES) database. To achieve the task, Coscientist uses web search and code execution with the RDKit chemoinformatics package.

believe that the community is only starting to understand all the capabilities of GPT-4 (ref. 48). OpenAI has shown that GPT-4 could rely on some of those capabilities to take actions in the physical world during their initial red team testing performed by the Alignment Research Center14.

One of the possible strategies to evaluate an intelligent agent’s reasoning capabilities is to test if it can use previously collected data to guide future actions. Here, we focused on the multi-variable design and optimization of Pd-catalysed transformations, showcasing Coscientist’s abilities to tackle real-world experimental campaigns involving thousands of examples. Instead of connecting LLMs to an

### Chemical reasoning capabilities

The system demonstrates appreciable reasoning capabilities, enabling the request of necessary information, solving of multistep problems and generation of code for experimental design. Some researchers

b

a

R2

Me

Pd(OAc)2, Li, Bj, Sk

R1

yi – —1 jyj

Me

n maxjyj – —1 jyj

+

Normalized advantage =

N

THP

N

1 min, 100 ºC

N

N

n

N

THP N

c

Average Bayesian optimization Random Maximum

GPT-4 with prior information (10 data points) GPT-4 without prior information

GPT-3.5 without prior information

Normalized maximum advantage

1.0

...yet, at the limit, the models converge to the same NMA.

0.5

Prior information improves initial conditions...

0

The small number of examples for GPT-3.5 under the  xed budget is due to its failure to follow the provided schema.

−0.5

- −0.5

- 0

0.5

1.0

- 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 Number of iterations


- −1.0


- −0.5

- 0

0.5

1.0

- 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 Number of iterations


- −1.0


For some compounds, the model starts with a very bad guess.

−1.0

−1.0

−1.0

1.0

1.0

1.0

The model continuously improves its strategy based on newly collected data.

Normalized advantage

0.5

0.5

0.5

0

0

0

NA for Bayesian optimization does not increase over time

−0.5

−0.5

−0.5

−1.0

1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 Number of iterations

d

Normalized maximum

advantage derivative

e

GPT-4 with prior information GPT-4 without prior information

R

NH2

X PdL(OTf)Li additive Aj Bk, DMSO

H N

R

Normalized

0.1

advantage

derivative

+

0.1

Me

0

Me

0

5 10 15 Number of iterations

5 10 15 Number of iterations

g

f

Average Random Maximum

GPT-4 without prior information, compound names GPT-4 without prior information, SMILES strings

Normalized maximum advantage

1.0

O N

0.5

0

−0.5

- −0.5

- 0

0.5

1.0

- 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 Number of iterations


- −1.0


−1.0

−1.0

1.0

1.0

Normalized advantage

O

0.5

0.5

O

0

0

N

O

−0.5

−0.5

−1.0

1 2 3 4 5 6 7 8 9 10 1112 13 14 15 16 17 18 19 20 Number of iterations

- Fig. 6 | Results of the optimization experiments.a, A general reaction scheme from the flow synthesis dataset analysed incandd.b, The mathematical expression used to calculate normalized advantage values.c, Comparison of the three approaches (GPT-4 with prior information, GPT-4 without prior information and GPT-3.5 without prior information) used to perform the optimization process.d, Derivatives of the NMA and normalized advantage


values evaluated inc, left and centre panels.e, Reaction from the C–N crosscoupling dataset analysed inf andg.f, Comparison of two approaches using compound names and SMILES string as compound representations. g, Coscientist can reason about electronic properties of the compounds, even when those are represented as SMILES strings. DMSO, dimethyl sulfoxide.

optimization algorithm as previously done by Ramos et al.49, we aimed to use Coscientist directly.

dataset51 (Fig. 6e), where variations in ligands, additives and bases were recorded. At this point, any reaction proposed by Coscientist would be within these datasets and accessible as a lookup table.

We selected two datasets containing fully mapped reaction condition spaces where yield was available for all combinations of variables. One is a Suzuki reaction dataset collected by Perera et al.50, where these reactions were performed in flow with varying ligands, reagents/bases and solvents (Fig. 6a). Another is Doyle’s Buchwald–Hartwig reaction

We designed the Coscientist’s chemical reasoning capabilities test as a game with the goal of maximizing the reaction yield. The game’s actions consisted of selecting specific reaction conditions with a sensible chemical explanation while listing the player’s observations

about the outcome of the previous iteration. The only hard rule was for the player to provide its actions written in JavaScript Object Notation (JSON) format. If the JSON file could not be parsed, the player is alerted of its failure to follow the specified data format. The player had a maximum of 20 iterations (accounting for 5.2% and 6.9% of the total space for the first and second datasets, respectively) to finish the game.

### Discussion

In this paper, we presented a proof of concept for an artificial intelligent agent system capable of (semi-)autonomously designing, planning and multistep executing scientific experiments. Our system demonstrates advanced reasoning and experimental design capabilities, addressing complex scientific problems and generating high-quality code. These capabilities emerge when LLMs gain access to relevant research tools, such as internet and documentation search, coding environments and robotic experimentation platforms. The development of more integrated scientific tools for LLMs has potential to greatly accelerate new discoveries.

We evaluate Coscientist’s performance using the normalized advantage metric (Fig. 6b). Advantage is defined as the difference between a given iteration yield and the average yield (advantage over a random strategy). Normalized advantage measures the ratio between advantage and maximum advantage (that is, the difference between the maximum and average yield). The normalized advantage metric has a value of one if the maximum yield is reached, zero if the system exhibits completely random behaviour and less than zero if the performance at this step is worse than random. An increase in normalized advantage over each iteration demonstrates Coscientist’s chemical reasoning capabilities. The best result for a given iteration can be evaluated using the normalized maximum advantage (NMA), which is the normalized value of the maximum advantage achieved until the current step. As NMA cannot decrease, the valuable observations come in the form of the rate of its increase and its final point. Finally, during the first step, the values for NMA and normalized advantage equal each other, portraying the model’s prior knowledge (or lack thereof) without any data being collected.

The development of new intelligent agent systems and automated methods for conducting scientific experiments raises potential concerns about the safety and potential dual-use consequences, particularly in relation to the proliferation of illicit activities and security threats. By ensuring the ethical and responsible use of these powerful tools, we are continuing to explore the vast potential of LLMs in advancing scientific research while mitigating the risks associated with their misuse. A brief dual-use study of Coscientist is provided in Supplementary Information section ‘Safety implications: Dual-use study’.

#### Technology use disclosure

For the Suzuki dataset, we compared three separate approaches: (1) GPT-4 with prior information included in the prompt (which consisted of 10 yields from random combinations of reagents); (2) GPT-4; or (3) GPT-3.5 without any prior information (Fig. 6c). When comparing GPT-4 with the inclusion and exclusion of prior information, it is clear that the initial guess for the former scenario is better, which aligns with our expectations considering the provided information about the system’s reactivity. Notably, when excluding prior information, there are some poor initial guesses, whereas there are none when the model has prior information. However, at the limit, the models converge to the same NMA. The GPT-3.5 model plots have a very limited number of data points, primarily because of its inability to output messages in the correct JSON schema as requested in the prompt. It is unclear if the GPT-4 training data contain any information from these datasets. If so, one would expect that the initial model guess would be better than what we observed.

The writing of the preprint version of this manuscript was assisted by ChatGPT (specifically, GPT-4 being used for grammar and typos). All authors have read, corrected and verified all information presented in this manuscript and Supplementary Information.

### Online content

Any methods, additional references, Nature Portfolio reporting summaries, source data, extended data, supplementary information, acknowledgements, peer review information; details of author contributions and competing interests; and statements of data and code availability are available at https://doi.org/10.1038/s41586-023-06792-0.

- 1. Brown, T. et al. in Advances in Neural Information Processing Systems Vol. 33 (eds Larochelle, H. et al.) 1877–1901 (Curran Associates, 2020).
- 2. Thoppilan, R. et al. LaMDA: language models for dialog applications. Preprint at https://arxiv.org/abs/2201.08239 (2022).
- 3. Touvron, H. et al. LLaMA: open and efficient foundation language models. Preprint at https://arxiv.org/abs/2302.13971 (2023).
- 4. Hoffmann, J. et al. Training compute-optimal large language models. In Advances in Neural Information Processing Systems 30016–30030 (NeurIPS, 2022).
- 5. Chowdhery, A. et al. PaLM: scaling language modeling with pathways. J. Mach. Learn. Res. 24, 1–113 (2022).
- 6. Lin, Z. et al. Evolutionary-scale prediction of atomic-level protein structure with a language model. Science 379, 1123–1130 (2023).
- 7. Luo, R. et al. BioGPT: generative pre-trained transformer for biomedical text generation and mining. Brief Bioinform. 23, bbac409 (2022).
- 8. Irwin, R., Dimitriadis, S., He, J. & Bjerrum, E. J. Chemformer: a pre-trained transformer for computational chemistry. Mach. Learn. Sci. Technol. 3, 015022 (2022).
- 9. Kim, H., Na, J. & Lee, W. B. Generative chemical transformer: neural machine learning of molecular geometric structures from chemical language via attention. J. Chem. Inf. Model. 61, 5804–5814 (2021).
- 10. Jablonka, K. M., Schwaller, P., Ortega-Guerrero, A. & Smit, B. Leveraging large language models for predictive chemistry. Preprint at https://chemrxiv.org/engage/chemrxiv/ article-details/652e50b98bab5d2055852dde (2023).
- 11. Xu, F. F., Alon, U., Neubig, G. & Hellendoorn, V. J. A systematic evaluation of large language models of code. In Proc. 6th ACM SIGPLAN International Symposium on Machine Programming 1–10 (ACM, 2022).
- 12. Nijkamp, E. et al. CodeGen: an open large language model for code with multi-turn program synthesis. In Proc. 11th International Conference on Learning Representations (ICLR, 2022).
- 13. Kaplan, J. et al. Scaling laws for neural language models. Preprint at https://arxiv.org/ abs/2001.08361 (2020).
- 14. OpenAI. GPT-4 Technical Report (OpenAI, 2023).
- 15. Ziegler, D. M. et al. Fine-tuning language models from human preferences. Preprint at https://arxiv.org/abs/1909.08593 (2019).
- 16. Ouyang, L. et al. Training language models to follow instructions with human feedback. In Advances in Neural Information Processing Systems 27730–27744 (NeurIPS, 2022).


The normalized advantage values increase over time, suggesting that the model can effectively reuse the information obtained to provide more specific guidance on reactivity. Evaluating the derivative plots (Fig. 6d) does not show any significant difference between instances with and without the input of prior information.

There are many established optimization algorithms for chemical reactions. In comparison with standard Bayesian optimization52, both GPT-4-based approaches show higher NMA and normalized advantage values (Fig. 6c). A detailed overview of the exact Bayesian optimization strategy used is provided in Supplementary Information section ‘Bayesian optimization procedure’. It is observed that Bayesian optimization’s normalized advantage line stays around zero and does not increase over time. This may be caused by different exploration/exploitation balance for these two approaches and may not be indicative of their performance. For this purpose, the NMA plot should be used. Changing the number of initial samples does not improve the Bayesian optimization trajectory (Extended Data Fig. 3a). Finally, this performance trend is observed for each unique substrate pairings (Extended Data Fig. 3b).

For the Buchwald–Hartwig dataset (Fig. 6e), we compared a version of GPT-4 without prior information operating over compound names or over compound SMILES strings. It is evident that both instances have very similar performance levels (Fig. 6f). However, in certain scenarios, the model demonstrates the ability to reason about the reactivity of these compounds simply by being provided their SMILES strings (Fig. 6g).

- 40. Qadrud-Din, J. et al. Transformer based language models for similar text retrieval and ranking. Preprint at https://arxiv.org/abs/2005.04588 (2020).
- 41. Paper QA. GitHub https://github.com/whitead/paper-qa (2023).
- 42. Robertson, S. & Zaragoza, H. The probabilistic relevance framework: BM25 and beyond. Found. Trends Inf. Retrieval 3, 333–389 (2009).
- 43. Data Mining. Mining of Massive Datasets (Cambridge Univ., 2011).
- 44. Johnson, J., Douze, M. & Jegou, H. Billion-scale similarity search with GPUs. IEEE Trans. Big Data 7, 535–547 (2021).
- 45. Vechtomova, O. & Wang, Y. A study of the effect of term proximity on query expansion. J. Inf. Sci. 32, 324–333 (2006).
- 46. Running experiments. Emerald Cloud Lab https://www.emeraldcloudlab.com/guides/ runningexperiments (2023).
- 47. Sanchez-Garcia, R. et al. CoPriNet: graph neural networks provide accurate and rapid compound price prediction for molecule prioritisation. Digital Discov. 2, 103–111

(2023).

- 48. Bubeck, S. et al. Sparks of artificial general intelligence: early experiments with GPT-4. Preprint at https://arxiv.org/abs/2303.12712 (2023).
- 49. Ramos, M. C., Michtavy, S. S., Porosoff, M. D. & White, A. D. Bayesian optimization of catalysts with in-context learning. Preprint at https://arxiv.org/abs/2304.05341 (2023).
- 50. Perera, D. et al. A platform for automated nanomole-scale reaction screening and micromole-scale synthesis in flow. Science 359, 429–434 (2018).
- 51. Ahneman, D. T., Estrada, J. G., Lin, S., Dreher, S. D. & Doyle, A. G. Predicting reaction performance in C–N cross-coupling using machine learning. Science 360, 186–190

(2018).

- 52. Hickman, R. et al. Atlas: a brain for self-driving laboratories. Preprint at https://chemrxiv. org/engage/chemrxiv/article-details/64f6560579853bbd781bcef6 (2023).


- 17. Granda, J. M., Donina, L., Dragone, V., Long, D.-L. & Cronin, L. Controlling an organic synthesis robot with machine learning to search for new reactivity. Nature 559, 377–381

(2018).

- 18. Caramelli, D. et al. Discovering new chemistry with an autonomous robotic platform driven by a reactivity-seeking neural network. ACS Cent. Sci. 7, 1821–1830 (2021).
- 19. Angello, N. H. et al. Closed-loop optimization of general reaction conditions for heteroaryl Suzuki–Miyaura coupling. Science 378, 399–405 (2022).
- 20. Adamo, A. et al. On-demand continuous-flow production of pharmaceuticals in a compact, reconfigurable system. Science 352, 61–67 (2016).
- 21. Coley, C. W. et al. A robotic platform for flow synthesis of organic compounds informed by AI planning. Science 365, eaax1566 (2019).
- 22. Burger, B. et al. A mobile robotic chemist. Nature 583, 237–241 (2020).
- 23. Auto-GPT: the heart of the open-source agent ecosystem. GitHub https://github.com/ Significant-Gravitas/AutoGPT (2023).
- 24. BabyAGI. GitHub https://github.com/yoheinakajima/babyagi (2023).
- 25. Chase, H. LangChain. GitHub https://github.com/langchain-ai/langchain (2023).
- 26. Bran, A. M., Cox, S., White, A. D. & Schwaller, P. ChemCrow: augmenting large-language models with chemistry tools. Preprint at https://arxiv.org/abs/2304.05376 (2023).
- 27. Liu, P. et al. Pre-train, prompt, and predict: a systematic survey of prompting methods in natural language processing. ACM Comput. Surv. 55, 195 (2021).
- 28. Bai, Y. et al. Constitutional AI: harmlessness from AI feedback. Preprint at https://arxiv.org/ abs/2212.08073 (2022).
- 29. Falcon LLM. TII https://falconllm.tii.ae (2023).
- 30. Open LLM Leaderboard. Hugging Face https://huggingface.co/spaces/HuggingFaceH4/ open_llm_leaderboard (2023).
- 31. Ji, Z. et al. Survey of hallucination in natural language generation. ACM Comput. Surv. 55, 248 (2023).
- 32. Reaxys https://www.reaxys.com (2023).
- 33. SciFinder https://scifinder.cas.org (2023).
- 34. Yao, S. et al. ReAct: synergizing reasoning and acting in language models. In Proc.11th International Conference on Learning Representations (ICLR, 2022).
- 35. Wei, J. et al. Chain-of-thought prompting elicits reasoning in large language models. In Advances in Neural Information Processing Systems 24824–24837 (NeurIPS, 2022).
- 36. Long, J. Large language model guided tree-of-thought. Preprint at https://arxiv.org/ abs/2305.08291 (2023).
- 37. Opentrons Python Protocol API. Opentrons https://docs.opentrons.com/v2/ (2023).
- 38. Tu, Z. et al. Approximate nearest neighbor search and lightweight dense vector reranking in multi-stage retrieval architectures. In Proc. 2020 ACM SIGIR on International Conference on Theory of Information Retrieval 97–100 (ACM, 2020).
- 39. Lin, J. et al. Pyserini: a python toolkit for reproducible information retrieval research with sparse and dense representations. In Proc. 44th International ACM SIGIR Conference on Research and Development in Information Retrieval 2356–2362 (ACM, 2021).


Publisher’s noteSpringer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate

credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.

© The Author(s) 2023

to Y. Benslimane, H. Gronlund, B. Smith and B. Frezza) for assisting us with parsing their documentation and executing experiments. G.G. is grateful to the Carnegie Mellon University Cloud Lab Initiative led by the Mellon College of Science for its vision of the future of physical sciences. G.G. thanks Carnegie Mellon University; the Mellon College of Sciences and its Department of Chemistry; and the College of Engineering and its Department of Chemical Engineering for the start-up support. D.A.B. was partially funded by the National Science Foundation Center for Chemoenzymatic Synthesis (Grant no. 2221346). R.M. was funded by the National Science Foundation Center for Computer-Assisted Synthesis (Grant no. 2202693).

### Data availability

Examples of the experiments discussed in the text are provided in the Supplementary Information. Because of safety concerns, data, code and prompts will be only fully released after the development of US regulations in the field of artificial intelligence and its scientific applications. Nevertheless, the outcomes of this work can be reproduced using actively developed frameworks for autonomous agent development. The reviewers had access to the web application and were able to verify any statements related to this work. Moreover, we provide a simpler implementation of the described approach, which, although it may not produce the same results, allows for deeper understanding of the strategies used in this work.

Author contributionsD.A.B. designed the computational pipeline and developed the ‘Planner’, ‘Web searcher’ and ‘Code execution’ modules. R.M. assisted in designing the computational pipeline and developed the ‘Docs searcher’ module. B.K. analysed the behaviours of the Docs searcher module to enable Coscientist to produce experiment code in Emerald Cloud Lab’s Symbolic Lab Language. D.A.B. assisted and oversaw Coscientist’s chemistry experiments. D.A.B., R.M. and G.G. designed and performed initial computational safety studies. D.A.B. designed and graded Coscientist’s synthesis capabilities study. D.A.B. co-designed with G.G. and performed the optimization experiments. R.M. performed the large compound library experiment and Bayesian optimization baseline runs. G.G. designed the concepts, performed preliminary studies and supervised the project. D.A.B., R.M. and G.G. wrote this manuscript.

### Code availability

Competing interestsG.G. is part of the AI Scientific Advisory Board of Emerald Cloud Lab. Experiments and conclusions in this manuscript were made before G.G.’s appointment to this role. B.K. is an employee of Emerald Cloud Lab. D.A.B. and G.G. are co-founders of aithera.ai, a company focusing on responsible use of artificial intelligence for research.

Simpler implementation as well as generated outputs used for quantitative analysis are provided at https://github.com/gomesgroup/ coscientist.

Additional information Supplementary informationThe online version contains supplementary material available at https://doi.org/10.1038/s41586-023-06792-0. Correspondence and requests for materials should be addressed to Gabe Gomes. Peer review information Nature thanks Sebastian Farquhar, Tiago Rodrigues and the other, anonymous, reviewer(s) for their contribution to the peer review of this work. Reprints and permissions informationis available at http://www.nature.com/reprints.

AcknowledgementsWe thank the following Carnegie Mellon University Chemistry groups for their assistance with providing the chemicals needed for the Coscientist’s experiments: Sydlik, Garcia Borsch, Matyjaszewski and Ly. We give special thanks to the Noonan group (K. Noonan and D. Sharma) for providing access to chemicals and gas chromatography–mass spectrometry analysis. We also thank the team at Emerald Cloud Lab (with special attention

![image 241](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile241.png)

- Extended Data Fig. 1 | Using UV-Vis and liquid handler to solve food colouring identification problem. Guiding prompt in the third message is shown in bold. In the first message the user prompt is provided, then code for sample


preparation is generated, resulting data is provided as NumPy array, which is then analysed to give the final answer.

![image 242](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile242.png)

- Extended Data Fig. 2 | Code, generated by Coscientist. The generated code can be split into the following steps: defining metadata for the method, loading labware modules, setting up the liquid handler, performing required reagent


transfers, setting up the heater-shaker module, running the reaction, and turning the module off.

![image 243](Boiko et al._2023_Autonomous chemical research with large language models_images/imageFile243.png)

###### Extended Data Fig. 3 | Additional results on comparison with Bayesian optimization.a, GPT-4 models compared with Bayesian optimization performedstarting with different number of initial samples.b, Compound-by-compound comparison of differences between advantages.

