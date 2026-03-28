Agents for self-driving laboratories applied to quantum computing
Shuxiang Cao1,♦,∗Zijian Zhang2,3,♦,† Mohammed Alghadeer1, Simone D Fasciati1,
Michele Piscitelli1, Mustafa Bakr1, Peter Leek1,‡ and Aln Aspuru-Guzik2,3,4,5,6,7,8§
1Clarendon Laboratory, Department of Physics, University of Oxford, Oxford, OX1 3PU, UK
2Department of Computer Science, University of Toronto, Toronto, ON M5S 2E4, Canada
3Vector Institute for Artificial Intelligence, Toronto, ON, M5G 1M1, Canada
4Department of Chemistry, University of Toronto, Toronto, ON M5S 3H6, Canada
5Department of Materials Science & Engineering,
University of Toronto, Toronto, ON M5S 3E4, Canada
6Department of Chemical Engineering & Applied Chemistry,
University of Toronto, Toronto, ON M5S 3E5, Canada
7Canadian Institute for Advanced Research (CIFAR), Toronto, ON M5G 1M1, Canada and
8Acceleration Consortium, Toronto, ON M5S 3H6, Canada
Fully automated self-driving laboratories are promising to enable high-throughput and large-
scale scientific discovery by reducing repetitive labour. However, effective automation requires deep
integration of laboratory knowledge, which is often unstructured, multimodal, and difficult to incor-
porate into current AI systems. This paper introduces the k-agents framework, designed to support
experimentalists in organizing laboratory knowledge and automating experiments with agents. Our
framework employs large language model-based agents to encapsulate laboratory knowledge includ-
ing available laboratory operations and methods for analyzing experiment results. To automate
experiments, we introduce execution agents that break multi-step experimental procedures into
agent-based state machines, interact with other agents to execute each step and analyze the experi-
ment results. The analyzed results are then utilized to drive state transitions, enabling closed-loop
feedback control. To demonstrate its capabilities, we applied the agents to calibrate and operate a
superconducting quantum processor, where they autonomously planned and executed experiments
for hours, successfully producing and characterizing entangled quantum states at the level achieved
by human scientists. Our knowledge-based agent system opens up new possibilities for managing
laboratory knowledge and accelerating scientific discovery.
I.
MAIN
Automating laboratory experiments has the potential to accelerate scientific discovery by closing the loop between
experimental execution, artificial intelligence (AI) and human-in-the-loop decision-making [1]. Although it is increas-
ingly common in laboratories that experiments can be implemented through programming interfaces [2–4], automating
experiments still requires detailed laboratory knowledge to set the parameters of each experiment, interpret the results
of the experiment, and execute complicated experiment workflows. Traditional methods of automating experiments
require human experts to translate their knowledge into code for machine execution [5–9]. However, the knowledge
required for laboratory work has increased significantly over the past decades due to the growing complexity of the
experimental apparatus, which now involves more intricate technical details for operation. This makes translating
the required knowledge and maintaining consistency an increasingly significant human effort, which compromises the
efficiency brought about by automation. In addition, the multimodal and complex nature of laboratory knowledge
also makes it challenging to develop automated programs that can perform these tasks at a level comparable to that
of humans.
The advent of large language models (LLMs) and multimodal LLMs has sparked new hope for more efficient
experiment automation due to their universal ability to process text and image information [10–16]. Although limited
by the length of their context windows, LLMs offer the hope of efficiently understanding laboratory documents,
performing analyses, generating code, and interpreting experimental images. The development of multi-agent systems
has further enhanced LLM’s capabilities by integrating multiple LLM-based agents to work together on a complex
objective, improving both accuracy and scalability [17–23]. The merits of LLM-based agents make them well suited
for assisting laboratory automation without the need for extensive human intervention. However, several challenges
remain. First, much of the media, such as code and documents, that carry laboratory knowledge is proprietary and
♦These two authors contributed equally to this work
∗shuxiang.cao@physics.ox.ac.uk; Present address: NVIDIA Corporation, 2788 San Tomas Expressway, Santa Clara, 95051, CA, USA
† zijian@cs.toronto.edu
‡ peter.leek@physics.ox.ac.uk
§ alan@aspuru.com
arXiv:2412.07978v2  [cs.AI]  5 Jun 2025

2
Human scientists
or other agents 
Execution agent
Translation agents
Instructions to executable 
code or other experiment 
procedures
Experiment report
Code /
Procedure
Reports in 
text
Experiment 
procedure
Finished
Generate code/procedure 
for the current stage
Decide and move to the 
next stage
Gather and analyze 
experiment results
Inspection agents 
Experiment results to text 
reports
Generate stages of 
experiment
1
2
3
</>
</>
</>
(a)
(c)
(b)
</>
Experiment procedure:
- Conduct a Rabi experiment to 
determine the Rabi rate for 
rough amplitude calibration. 
Retry and adjust parameters 
when failed.
- Run Ping-pong amplitude 
calibration. If failed, the whole 
procedure is failed.
Stage 1: Rabi Experiment
Description: Conduct the Rabi experiment to determine the 
Rabi rate for rough amplitude calibration. 
Next Stage: Proceed to Stage2 if successful, adjust the 
parameters and retry Stage1 if not. 
Stage 2: Ping-pong Amplitude Calibration
Description: Run the Ping-pong amplitude calibration.
Next Stage: Proceed to Complete if standards are met. Else, 
proceed to Failed.
Complete
Failed
Tree of execution
State machine of an experiment procedure
</>
Execute
Figure 1: (a) Overview of the k-agents framework. Given a procedure in natural language, the execution agent first
decomposes it into an agent-based state machine, which contains experiment stages. Each stage holds an
independent experiment instruction to be translated with the translation agents. The transition between stages is
driven by the generated transition rules and the reports from the inspection agents. (b) Agent-based state machine
of instructions. The figure demonstrates how an experiment procedure can be decomposed into an agent-based state
machine. The decomposition divides experiment procedures into experiment stages that hold single instructions,
along with a transition rule for deciding the next stage. (c) Tree of translation. The translating of instructions can
be viewed as an expansion of a tree, in which the translation results are represented as the child nodes. An
instruction can be translated as a simple experiment (code node) or an experiment procedure (agent node) that
needs further execution and translation with another execution agent.
inaccessible online, meaning that it is unlikely to be included in the training data of publically available LLMs. In
addition, the amount of text that includes such specialized laboratory knowledge is often insufficient to effectively
fine-tune an LLM [24]. Furthermore, laboratory knowledge is usually dynamic and frequently updated, making fine-
tuning models impractical, as it is often hard to rewrite the knowledge in LLMs [25–27]. As a result, incorporating
laboratory-specific knowledge into LLMs remains difficult. Recent work on retrieval-augmented generation (RAG)
offers a foundation to equip LLM-based agents with larger-scale knowledge without fine-tuning [28–30]. However,
laboratory knowledge is usually heterogeneous and multimodal, making it challenging to apply standard RAG methods
directly [5, 9, 31].
Despite challenges, pioneering efforts to develop automated LLM-based agents to carry out experiments are already
underway [32–35]. For example, in [32] and [33], researchers equipped LLM-based agents with tools that allow them
to acquire professional knowledge from the expert-designed toolkit and even the Internet. Then, these agents are
capable of performing chemistry experiments on the basis of this knowledge. However, in general, previous results lack
a scalable memory system and rely on keeping the conversation history when calling LLMs. This inherently restricts
the agents’ ability to automate long-duration tasks involving many sequential steps, as most current LLMs exhibit
diminishing performance as the input length increases [36–38]. This construction also prohibits further extensions of
the system, such as supporting the handling of scientific plots.
In this work, we introduce k-agents (see Figure 1), a knowledge-based multi-agent system designed to automate
experiments, particularly those requiring large-scale, multimodal laboratory knowledge and complex workflow. We
developed tools for users to transfer their knowledge, creating LLM-based knowledge agents to manage laboratory
knowledge without fine-tuning. These knowledge agents can help operate laboratories by holding knowledge ranging
from single experiments to complex procedures and how to inspect the results of each experiment. These agents are
designed to be activated selectively, allowing the system to scale efficiently as the number of agents increases. In order

3
class RamseyExperiment(Experiment):
def run(qubit, start=0.0, offset=10.0, ...):
””””
This method runs the Ramsey experiment
Parameters:
qubit: the qubit to be measured
… 
””””
… (Implementation omitted)
(a)
# Full gate frequency calibration
## Background
This procedure is used to calibrate the frequency 
of the qubit gates. It should be used when the 
frequency calibration parameters are not known.
## Steps
- Run Ramsey experiment with frequency offset 
10 MHz, stop at 0.3us, step 0.005us. When 
failed, adjust the parameters and retry.
- …
Translation agent group
Proposal 1:
RamseyExperiment(qubit, start=start)
Proposal 2:
MultiQubitRamsey([qubit], start=start)
Instruction: Run a Ramsey experiment to measure the 
frequency of `qubit`, with the start of the sweep being `start`.
Variables: qubit (TransmonElement), start (float)
(b)
Reflection: The 
experiment I hold 
is not for this 
instruction.
Execution agent
Analysis: There is just one qubit to be 
measured. Therefore, I should adopt the 
first suggestion.
Code for instruction: 
RamseyExperiment(qubit, start=start)
Compare vectors
to find agents
Trigger
Figure 2: (a) Translation agents. Translation agents are responsible for translating an incoming instruction into
executable code. The agents will be activated when their characterizing vectors (blue fingerprints) have a significant
overlap with the instruction’s vector (orange fingerprint). The activated agents will try to translate the instruction
based on their knowledge. If the translation agent deems the translation as valid, the result will be output to the
execution agent for a final selection and execution. (b) Accuracy of instruction translation. We prepare a test set
containing 80 instructions from 8 experiments to be translated. We compare k-agents (marked as Agents), which
uses Algorithm 1, with standard RAG methods (marked as RAG), which directly load the signature of the
experiment class into the prompt. In our setup with 17 code translation agents, we found that k-agents
demonstrates better performance than standard RAG methods in choosing the correct experiment class. Further,
k-agents can support heterogeneous translation agents working together, which is hard to achieve with standard
RAG methods. Details of this benchmark can be found in the Appendix C.
to fully exploit the knowledge agents, we further introduce the execution agent, which is responsible for coordinating
the knowledge agents, gathering and filtering knowledge, generating code (scripts) to operate the laboratory and
controlling the progress of complex experiment procedures with intelligent closed-loop feedback planning. To handle
multi-step experiments, the execution agent decomposes complex procedures into independent experiment stages and
creates an agent-based state machine.
The agent-based state machine differs from a traditional state machine in
that state transitions are determined by agents, rather than by rigid deterministic rules. This state-machine-based
approach minimizes the experimental history that needs to be loaded into LLMs, making it feasible to conduct long-
duration experiments at a human-like level of performance. The agents are created by prompting a language model
on a distinct context and the details of the prompt construction can be found in Appendix B.
As a demonstration, we applied our framework to automate the calibration and characterization of single- and
two-qubit gates on our superconducting quantum processor. Superconducting qubits have become one of the most
widely adopted platforms for quantum computing, with recent advancements pushing the scale to hundreds of qubits,
along with active quantum error correction [39–43]. As these systems grow in complexity, calibrating the operations of
hundreds of qubits has emerged as a substantial bottleneck. Given this rapid progress, it is timely and essential to study
automation solutions that can support the scalability and performance requirements of large-scale superconducting
quantum devices. In addition, our framework demonstrates its ability to conduct custom experiments. Specifically,
preparing the GreenbergerHorneZeilinger (GHZ) state requires the calibration of multiple qubits to execute the desired
quantum operations. We selected this experiment to demonstrate the capabilities of our automation technique in
generating an entangled quantum state and evaluating its fidelity. We propose that this framework could be adapted
to other fields as a model for future research and industrial methodologies.
A.
Knowledge agents
We define knowledge agents as AI agents whose performance is measured by their ability to receive and transfer
knowledge. For instance, an agent qualifies as a strong knowledge agent if it accepts knowledge from natural language
inputs and responds correctly to related queries using natural language. Developing more advanced knowledge agents

4
offers significant advantages. First, a more general ability to accept knowledge reduces the effort needed for humans
to translate knowledge into computer-friendly formats. Furthermore, the ability to transfer knowledge facilitates more
rigorous testing of agents [44] and avoids treating the system as a black box, improving the general trustworthiness
of AI systems.
Prior works [32–35] has limitations in scalability, which constrain their ability to manage complex toolsets and long-
horizon tasks. These systems typically construct a single prompt that embeds both task instructions and the entire
tool set. However, as shown in [45, 46], performance degrades significantly as the length of input increases. Moreover,
these approaches are generally limited to simpler tasks where the entire execution context can be accommodated
within the prompt window.
To address some of these issues, works such as [32] introduce modular architectures that allows the developer to
mannually divide tools into components. Additionally, they rely on retrieval-augmented generation (RAG) [32, 33]
for data access, which often screens and retrieves documents based on relevance rather than deeper procedural or
understanding.
To resolve the above issue, we introduce the k-agents framework, which provides tools to implement the afore-
mentioned bidirectional knowledge transferability and the scalablity towards large number of tools and long-horizen
tasks. In k-agents, we implement user-friendly interfaces that enable users to encapsulate knowledge within different
LLM-based agents.
These agents can then transfer their knowledge to the users and other agents in the format
of natural language with LLMs. Our framework has a scalable memory architecture with an agent-based retrieval
mechanism. This enables agents to dynamically interact with a large, indexed memory of procedural knowledge and
existing experiments. During retrieval, the agents conduct the reflection and selection processes to improve the accu-
racy and contextual relevance of retrieved information. This design allows our framework to support more complex
and long-duration tasks.
(Code translation agent) This first kind of knowledge agent in k-agents is the code translation agent, which is
designed to accept and apply the knowledge of the available experiment interfaces that can be called by code. Here, the
term “experiment” stands for not only a direct experiment on an instrument, but any general action that is available
in the laboratory. It can also be a call to a tool or even another agent. Given instructions in natural language, these
agents are responsible for translating natural language instructions into the corresponding code. To help the users
of k-agents construct code translation agents, we provide an abstract Python class that allows users to define the
set of experiments available in the laboratory explicitly. The users can then define all possible experiment interfaces,
ensuring that the AI system can access and utilize them. As illustrated in Figure 2(a), human experimentalists are
expected to document background knowledge, required parameters, and implementation code for each experiment in
the run method of the subclass representing the experiment. After indexing all available experiment classes, k-agents
will construct a code translation agent for each of the classes.
(Procedure translation agent) Experiment procedures in laboratories can involve complex workflows. These
workflows may require experimentalists to determine a sequence of experiments based on the results of the experiments
executed. Traditionally, this knowledge has been maintained either through unstructured documentation or by relying
on the memory of the experimentalists themselves. To address this, as shown in Figure 2(a), k-agents introduces a
standardized format to store examples of how to implement instructions using multistep experiment procedures. These
examples are then used to produce another kind of knowledge agent that we call the procedure translation agent, which
is capable of translating an instruction into its corresponding procedure based on stored examples. Similarly to code
translation agents, procedure translation agents also output code. The code will call an execution agent to execute
the procedure, which we will introduce later.
(Inspection agent) A major burden for experimentalists has been the need to wait for experimental results and
decide on the next step based on them. In many scenarios, experimentalists must analyze figures to assess the success
of an experiment and determine the next steps. In the k-agents framework, we introduce inspection agents that have
the knowledge needed to evaluate the results of each experiment. These agents will be called after the execution
of each experiment to analyze its outcomes.
We provide an interface to inject knowledge for each function that
produces experiment figures. This feature is implemented as a Python decorator. In the decorator, the users can
add instructions for how to analyze the figure. Besides, as illustrated in Figure 3(a), our interface allows users to
add example figures to help others understand the new figures. Based on the knowledge from the interfaces, we
construct inspection agents equipped with multimodal LLMs to inspect and analyze new experiment figures and
output text-based reports based on their knowledge.
B.
Execution agent
We introduce the execution agent to coordinate knowledge agents and manage complex experiment procedures.
This agent takes experiment procedures written in natural language as input, and driven by a text-only LLM. Since

5
Prompt: The experiment is considered success if 
there are two clear peaks located symmetrically. 
For example, this is a successful experiment:
Image(”Success.jpg”)
This is a failed experiment:
Image(”Failure.jpg”)
New figures from experiment
Reference figures (from human)
class StarkShiftRepeatedGate(Experiment):
@visual_inspection(”””
The experiment is considered success if…
”””)
def fourier_plot():
… (Implementation omitted)
return figure
Response if successful:
{”analysis”: ”There are two clear and 
symmetric peaks in the figure, 
indicating the experiment is 
success.”, 
”success”: true}
(a)
Success.jpg
Failure.jpg
(b)
Few-shot not 
supported
Visual inspection agent 
with knowledge
Response if failed:
{”analysis”: ”There are too many 
peaks in the figure, indicating this 
experiment is failed.”, 
”success”: false}
Figure 3: (a) Visual inspection agent. Our framework introduces visual inspection agents by attaching decorators to
the member methods of the experiment class that produce figures. The decorator accepts a prompt as input, and
users can add example figures to the prompt. Whenever the experiment is carried out, the execution agent can call
the inspection agents to generate a text-based report based on the outcome figure and their knowledge (prompts).
(b) Performance benchmarking of visual inspection. We compare the performance of the visual inspection method in
determining whether a certain experiment is successful or not. We added three types of inspection agents. Visual
agents with a text description of success criteria (zero-shot), visual agents with text descriptions and example figures
(few-shot), and fitting agents who provide reports based on fitting results. We test the accuracy of inspection on
each type of agent. We also combine the results of fitting agents and visual agents in the “Combined” setup. We
found that providing example figures significantly improves accuracy. Additionally, we found that reports
synthesized from multiple inspection agents can give better accuracy in some cases.
the selection of the next experiment in a procedure could depend on the result of previous experiments, we design
the execution agent to first decompose the procedure into a “state machin”, in which each state represents a distinct
experiment stage of the procedure (See Figure 1(c)). Each stage of the experiment is assigned a single instruction
that contains only one experiment or sub-procedure. As an agent-based state machine, there is also a transition rule
at each stage in natural language that determines how to select the next stage based on the result of the experiment.
By constructing the agent-based state machine, the execution agent transforms the task of executing the procedure
into executing the agent-based state machine. The execution is illustrated in Figure 1(a). Starting from the initial
stage, at each stage, the execution first translates the instruction at the stage into executable code with the assistance
of translation agents. To increase the accuracy and efficiency of the translation, the execution agent will activate only
translation agents related to the context. The relevance score will be calculated based on the embedding similarity
between the context and the description of the translation agents. The execution will select a reasonable response
from the translation agents and execute the translated code. After executing the code, the agent gathers a natural
language report from inspection agents and, based on the report and the transition rules, determines the next stage
to transition to.
If the reports suggest updating the parameters in the new stage, the execution agent will also
pass the update to it. This state-machine architecture enables the execution agent to focus on executing each stage
of the procedure efficiently without needing to monitor the entire experimental history when deciding on the next
experiment.

6
(a)
Agent:
The experiment was successful. The 
data shows a clear, regular oscillatory 
pattern with a good fit. …The number 
of oscillations is approximately 3.981, 
which is within the acceptable range 
of 3 to 10 oscillations.
Ramsey
Agent:
... The estimated optimal DRAG 
coefficient is -0.0061…  indicating 
that the sweep was appropriately 
centered. Overall, the experiment 
meets the success criteria.
DRAG
Agent:
The amplitude plot shows a 
decreasing trend initially, followed by 
stabilization around the 5th iteration, 
indicating that the amplitude 
converges through the iterations. …
Pingpong
Agent:
The experiment was successful. The 
plot shows a clear, regular oscillatory 
pattern with consistent amplitude and 
frequency, which is characteristic of a 
successful Rabi oscillation 
experiment. …
Rabi
Agent:
… The experiment duration may be 
too short… The 'stop' parameter 
should be increased by 0.1 
microseconds to allow for more 
oscillations
Ramsey
(b)
Decompose, execute, and inspect results
Human:
Fully calibrate the 
single qubit gates 
on `Q1`.
Agent:
Do full gate frequency calibration on qubit `Q1`. 
Do full gate amplitude calibration on qubit ` Q1`.
Do DRAG Calibration on the qubit ` Q1`.
Randomized benchmarking results:
Physical gate fidelity: 99.869% ± 0.013%
Figure 4: Automated single qubit parameter recalibration automated by k-agents. The human scientist instructs the
k-agents framework for calibrating the single qubit gate parameters. Based on the reference documents provided in
natural language, k-agents successfully breaks the calibration into four steps, followed by the randomized
benchmarking experiment to characterize the single-qubit gate fidelity. In this example, k-agents found the first
Ramsey experiment had not collected enough oscillations to estimate the frequency. Therefore, it repeats this
experiment by increasing the experiment time. The following experiments all passed the success criteria of the
k-agents. In the end, the k-agents implements the randomized benchmarking and reports the gate fidelity.
II.
RESULTS
In this section, we demonstrate how the k-agents framework can be applied to the calibration and operation of
a superconducting quantum processor. Superconducting circuits provide a popular physical platform for building
quantum information processors. These circuits are fabricated on a chip using nanofabrication techniques. These
circuit components operate under quantum mechanical principles at millikelvin temperatures, forming non-linear
quantum resonators which can be excited similarly to atoms using microwave signals. Information can be stored in
the quantum states of these resonators, which serve as qubits on the processor [47–50]. To control these qubits, external
electronics connected to the chip generate precise microwave signals. These signals must be carefully calibrated to
accurately set the operational parameters, which are crucial for executing logical quantum gates.
Typically, the
parameters include the shape of the pulse (the duration and amplitude at a certain time 𝑡) and the initial phase and
the frequency of the pulse. For a two-qubit gate, multiple pulses may be required to send at the same time to generate
the entanglement [49, 51, 52].
A significant challenge in superconducting circuit research is identifying these optimal operation parameters. Al-
though automated scripts can determine some parameters, they still require customization by scientists based on
different hardware setups. Moreover, programmatically validating the correctness of the result of these scripts is
usually difficult to implement. Scientists must continuously monitor experimental status and adjust the calibration
scripts to optimize operational parameters. Moreover, these parameters drift over time and occasionally require recal-
ibration. This process is time-consuming and repetitive, often not yielding direct results for physical research, yet it
is essential for conducting superconducting circuit research. This calibration process is complex and labour-intensive,
leading to significant challenges for scaling quantum computing systems. These difficulties are not limited to the su-
perconducting circuit platform, but also extend to ion traps [53–55], spin qubits [56–59], and Rydberg atom systems
[60–62]. Moreover, the techniques developed for these tasks have broader implications beyond quantum computing,
which has great potential to accelerate scientific and technological research in general.
The above challenges fit the targeting scenario of the k-agents framework. We adapt our existing control software

7
stack to the k-agents framework, which enables monitoring experimental results, recommending further parameter
adjustment, and executing automated calibrations and experiments. To demonstrate its capabilities and assess effec-
tiveness, we conducted three experiments. Before moving on to the hardware demonstration, we first benchmarked
the performance of k-agents in the context of superconducting qubits. We adopted the LeeQ software [63], originally
used to control superconducting quantum processors in the lab, to work with the k-agents system and provided it
with additional multimodal information to determine the success or failure of the experiments (See Appendix D for
more detail). First, we benchmarked the translation process using different LLM models, comparing the typical RAG
method with our approach. Our results show that the GPT-4o model has the best performance and archives an
accuracy of 97%, which we consider sufficient for practical application (see Figure 2(b)). In practice, when code gen-
eration fails, producing unusable code or syntax errors, we prompt the agent to retry, further improving the success
rate. We also evaluated the inspection agents to determine if they could accurately identify the success or failure of
experiments. We found that the best performance is achieved when using inspection agents constructed with example
figures (See Figure 3(b)).
Following the successful benchmarking results, we designed the experiments to further evaluate the performance of
k-agents on real hardware. First, we demonstrate fully automated recalibration of single-qubit parameters. Second,
we showcase the automated discovery and calibration of two-qubit gates on our platform. Third, we highlighted the
AI agent’s ability to generate quantum states based on natural language descriptions, including the creation of a GHZ
state across three qubits, utilizing previous calibrations.
Our experimental platform is a 16-qubit superconducting quantum processor configured in a four-by-four square
lattice connectivity layout, the characterization details of this device has been reported in [64]. The qubits employed
are standard fixed frequency transmon qubits with coaxial geometry [65–67]. For the demonstration of our framework,
we selected a subset of adjacent 3 qubits. In superconducting qubit systems, two-qubit gates are usually have to be
implemented between adjacent qubits, and the crosstalk and noise are more significant. Our demonstration using an
adjacent 3-qubit subset is consistent with current hardware constraints and design practices. Although it involves
only a few qubits, this setup reflects the typical conditions of academic labs, where small-scale experiments suffice
for exploring quantum phenomena and improving qubit performance. For further details about the hardware setup,
please refer to Appendix F.
In the first experiment, we demonstrate automated calibration and benchmarking of a single qubit with k-agents.
To facilitate the calibration process, we provided the agent with a document detailing the general procedure for single-
qubit calibration in natural language. At the start of the experiment, we manually adjusted the initial parameters
to deviate from their optimal values. Based on the document, the execution agent first decomposes the procedure
into two distinct stages: calibration and benchmarking. The calibration stage was further broken down into multiple
steps, in which the agent sequentially adjusted the qubit’s frequency, amplitude, and DRAG parameters. If a failure
occurs during the procedure, the step will be re-tried. After several unsuccessful attempts, it reverts to the previous
stage to try again. This process is driven by the agent to emulate the typical behavior of a human scientist who
implements the calibration process. We observed that the agent is able to perform transition correctly between stages
based on the experiment result and find the acceptable parameters. At the benchmarking stage, the agent successfully
performed a randomized benchmarking on the single qubit and validated its fidelity (See Figure 4).
Following the single-qubit calibration experiment, we demonstrated the automated discovery of two-qubit gate
parameters. Specifically, we focused on the siZZle (Stark-induced ZZ by level excursions) gate [68–71], which creates
entanglement between two fixed-frequency superconducting qubits. By driving both qubits off-resonance at the same
frequency simultaneously, the ZZ term in the qubits Hamiltonian is altered compared to when the qubits are undriven.
Leveraging this effect, we constructed a pulse sequence with calibrated amplitude and frequency to adjust the ZZ
interaction strength, followed by fine-tuning the pulse duration to achieve precise qubit entanglement. The most
challenging part of the process was the search for optimal driving amplitude and frequency, while the pulse duration
calibration was relatively straightforward, accomplished programmatically by measuring the ZZ interaction rate during
the drive. In this experiment, the AI agent autonomously identified a set of working parameters for the siZZle gate.
For a human scientist, searching these parameters typically requires starting with empirical knowledge and mea-
suring the ZZ interaction strength at specific driving frequencies and amplitude. The search process then proceeds by
adjusting the frequency and amplitude based on the experimental outcomes. When an experiment succeeds, we often
increase the pulse amplitude to enhance the ZZ interaction rate or adjust the driving frequency closer to the qubits
transition frequency. Conversely, when an experiment fails, we either decrease the amplitude or move the frequency
away from the transition frequency. There are three regions that need to be explored: below both qubits’ transition
frequencies, between the two, and above both qubits’ transition frequencies. We inject this empirical knowledge of
parameter selection into two LLM-based agents which are accessible to the experiment history for what parameters
have been tried. By wraping these agents into two special experiments, the execution agent can call them to get the
next frequency and amplitude to try. The parameter searching can then be formulated as an alternate calling to these
special experiments and the experiments for testing the proposed parameters.

8
Inspection result:
The experiment failed due to the following reasons: 1) The Fourier plot 
shows multiple peaks that are not symmetric around the center, indicating a 
failure in the ZZ interaction Hamiltonian tomography. 2) The population of 
the control qubit does not meet the criteria, as the minimum difference 
between the ground and excited state is less than 25% of the maximum 
difference.
Inspection result:
The experiment is considered successful based on the visual inspection of 
the Fourier transform plot and the fitting results. The Fourier transform plot 
shows two clear, symmetric peaks for the ground and excited states, 
indicating a successful ZZ interaction Hamiltonian tomography. The fitting 
results show that the expectation value of the control qubit along the Z axis 
is stable throughout the experiment, and the minimum difference between 
the ground and excited states is greater than 25% of the maximum 
difference, meeting the success criteria.
Experiment History
Select drive amplitude
and frequency
Frequency: 4830 MHz   Drive amplitude: 0.2725
Frequency: 4726 MHz   Drive amplitude: 0.3049
Conduct experiment 
with the parameters
Inspect results of 
experiment
Inspect with 
lab knowledge
Inspect with 
lab knowledge
Inspect with 
lab knowledge
Inspect with 
lab knowledge
Check for 
symmetric peaks
Check for 
symmetric peaks
Check for 
non-crossing lines
Check for 
non-crossing lines
(a)
(b)
(c)
Figure 5: Two-qubit gate parameter discovery driven by k-agents. (a) The workflow of the discovery process, where
k-agents continuously read the history of previous experiments and suggest the next parameter set likely to succeed.
(b) The set of discovered parameters and the corresponding parameter search space. The background indicates the
ZZ interaction strengths, visualized from data collected during an overnight experiment, which the agent has no
prior knowledge of. The green circles denote locations where the agent identified an acceptable parameter set, while
the black regions indicate failed attempts. For more details on the search for siZZle gate parameters, refer to
Appendix E. (c) Examples of figures observed by the agent, along with its response, illustrate a typical success case
and a failure case, respectively.
For each parameter pair (frequency and amplitude), we measured the ZZ interaction rate by performing Hamiltonian
tomography on the ZZ term using two methods: continuous-time tomography and repeated gate tomography. The
latter method, which accounts for the effects of the pulse’s rising and falling edges, yielded more accurate ZZ interaction
measurements per pulse.
The most challenging aspect was determining the success of each experiment. To address this, we plotted the
Fourier transform of the Hamiltonian tomography results and let an inspection agent decide whether the experiment
was successful, where the agent is equipped with a few-shot visual knowledge about the success criteria. Furthermore,
we monitored the state of the control qubit, plotting its expectation value of ⟨𝑍⟩, and tasked another inspection agent
with ensuring that it remained stable during the driving process, avoiding any unwanted excitation.
We ran the experiment for 3 hours, limiting the execution agent to carry out 100 experiments to search for parameters
and test a maximum of 20 frequencies. By the end of the experiment (See Figure 5), the agent successfully identified

9
Human:
Implement state tomography with measurement mitigation 
of a GHZ state. The GHZ state should be prepared by first 
applying a Hadamard gate to Q1, followed by a CNOT 
gate with Q1 and Q2, and another CNOT gate with Q1 
and Q8. Provide the ideal state vector for the calculation 
of the fidelity. 
Translation Agent:
c1 = dutq1.get_c1('f01')
lpb = c1.hadamard() + c2_q1q2.get_cnot() + c2_q1q8.get_cnot()
state_vec_ideal = np.array([1, 0, 0, 0, 0, 0, 0, 1]) / np.sqrt(2)
experiment_tomo = MultiQubitsStateTomography( 
duts=[dutq1, dutq2, dutq8], 
initial_lpb=lpb, 
measurement_mitigation=True, 
state_vec_ideal=state_vec_ideal
)
Inspection Agent:
The experiment successfully reported a density matrix. The density 
matrix appears to be physically meaningful, as it is Hermitian and has 
no obvious violations of quantum mechanical principles. The fidelity of 
83.83% was calculated, indicating a reasonable match between the 
experimental and ideal state vectors.
Tomography 
Experiment
Figure 6: Automation of the GHZ state generation and tomography with k-agents. First, the instructions are
provided by human scientists. Then, the code is generated by the translation agent to implement the experiment.
The density matrix plot of the generated GHZ state is constructed from the experiment result. Finally, a report in
natural language is generated by an inspection agent.
an optimal set of parameters (frequency 4726MHz and amplitude 0.3049).
Finally, we demonstrate the ability of the AI agent to carry out experiments based on natural language instructions.
After successfully calibrating the gates, we instructed the execution agent to perform state tomography for a GHZ
state. Additionally, we requested the agent to perform process tomography for the two-qubit gate parameters it had
calibrated. The agent successfully implemented this experiment and reported the state fidelity (See Figure 6).
III.
DISCUSSION
In this study, we introduce the k-agents framework for creating laboratory-related knowledge agents and demon-
strate its capability to automate experiments. We applied the system in a real-world setting, successfully demon-
strating the ability of k-agents by performing single-qubit and two-qubit gate calibrations, as well as generating
and characterizing a GHZ state on a quantum processor based on human instructions. The k-agents succeeded in
orchestrating the experiments, interpreting the multimodal experimental results, and guiding the execution of the
experiment with closed-loop feedback. These achievements suggest that our system is a valuable tool for research
groups working with superconducting quantum processors, with the potential for broader applications in research
automation across other fields. Additionally, we also applied two benchmark experiments on k-agents. We found our
agent-based translation of natural language instructions outperforms standard RAG approaches in terms of accuracy.
By our benchmark of the inspection agents, we showed that current multimodal LLMs have the ability to analyze
experiment figures based on human instructions, especially when provided with example figures.
While methods such as rule-based systems, reinforcement learning, and Bayesian optimization have been used for
calibrating quantum devices, our approach is fundamentally different. First the k-agents framework is designed to
automate entire experimental procedures, rather than focusing on the tuning of specific parameters. Optimization
methods like reinforcement learning and Bayesian optimization typically require extensive manual tuning, carefully
crafted reward functions, and are limited to narrow, predefined tasks. In contrast, our framework provides a more
general, interpretable, and adaptable solution, particularly well-suited for dynamic and evolving quantum laboratory
environments. Moreover, unlike traditional rule-based systems that depend on rigid, hand-coded logic, the k-agents
framework uses multimodal prompts (natural language and images) and LLMs to enable more flexible and efficient
automation.
One of the strengths of the k-agents framework is its approach to knowledge representation. It requires no more
effort than maintaining standard laboratory documentation and fits naturally into routine protocol management.
While we acknowledge that adopting any new framework involves some onboarding and training, the setup effort
is comparable to preparing laboratory manuals or protocols for new PhD students or junior staff. Once standard

10
documents are already existwhich is common practice in most laboratoriesour agents can be configured with minimal
additional work.
While our framework shares conceptual similarities with prior agent systems like ChemCrow [33] and Voyager [72],
it introduces several important distinctions that enhance agent-based AI for laboratory automation. First, our frame-
work is specifically tailored for quantum computing laboratories, where experiment automation involves breaking
down long-horizon workflows and dynamically adjusting parameterized experiments by analyzing previous results. In
contrast, ChemCrow targets open-ended challenges in general chemistry, focusing on relatively straightforward, short-
horizon tasks that require less iterative reasoning and fewer re-executions. Second, unlike Voyager, which utilizes
large internet-scale corpora about Minecraft that has already trained into large language models, our system operates
effectively without depending on such extensive external data, making it better suited for laboratory environments.
Additionally, Voyager develops agent skills through simulated environmentsa resource not always available in labo-
ratory settingswhereas our k-agents framework emphasizes practical application by building on existing laboratory
codebases. These distinctions reflect our commitment to improving the practicality and scalability of agent-based AI
for real-world scientific experimentation.
However, the k-agents framework has some potential weaknesses that make full automation challenging. First, our
method relies on clean and well-formatted codebases and procedure documents. However, such structured knowledge
may not always exist, and transforming existing knowledge could take considerable human effort. Future research on
structuralizing unstructured documents and codebases is still needed to completely automate knowledge translation.
A possible direction of research could involve enabling the framework to generate structured code and procedures
based on unstructured project files and human inputs. Secondly, using LLM, the execution of k-agents exhibits higher
latency than traditional automation methods that do not require LLM-based planning and translation of knowledge
at runtime. We note that this problem can be well mitigated by caching the response of LLMs and using the same
response whenever the input is the same.
In addition, our current implementation of execution agents within the agent-based state machine does not support
fine-grained, interruptible execution; it only allows for termination of the entire program in response to external
signals or emergency conditions. However, we acknowledge that in quantum systems, it would be beneficial to provide
an interactive mechanism for human scientists to monitor and intervene in the experiment’s progress. Addressing
this limitation is a priority for future development, and we plan to explore the integration of real-time interrupt
mechanisms, hardware-level hooks, and human-in-the-loop safety protocols.
We monitor the cost of the k-agents system. During the parameter search for the two-qubit gate, we observed that
the LLM used 1,373,207 input tokens (including image tokens) and 168,039 output tokens in 3 hours, costing less
than 5 US dollars. We believe that there is potential for further optimization to reduce these costs. Regarding time
efficiency, despite network delays, LLMs currently take longer than humans to perform inspections. The inspection
agent utilizes multimodal LLMs and requires a few seconds to evaluate each experimental result, with an inference
time comparable to that of the standard LLM agents without the multimodal ability. However, LLMs tend to be
more efficient than humans in generating code. Therefore, overall efficiency is comparable.
The use of superconducting quantum processors simplifies some challenges, such as safety control and error tolerance.
In our system, the risk of the agent executing code that causes significant damage or unacceptable costs is very low.
If it fails, we can simply allow it to try again. However, this may not be the case in other applications. Prior research
[1, 73, 74] has focused heavily on safety control, and this is an area we plan to explore further in the future.
IV.
METHOD
A.
Details on the knowledge agents developed
1.
Definition of knowledge agents
The concept of knowledge agents is defined based on the work proposed by Zhang et al. [16], in which an agent’s
learning ability is defined as its ability to internalize knowledge given related inputs. A knowledge agent can then
be interpreted as an agent with the ability to learn (i.e., acquire knowledge) and to apply the learned knowledge to
respond to other agents (i.e. transfer knowledge). A bare LLM can be regarded as a knowledge agent as it is able to
absorb knowledge from its training data. However, it is difficult for LLMs to internalize laboratory documents and
codes as their knowledge because of the current pitfalls in model editing [25]. Therefore, we regard bare LLMs as
weak knowledge agents compared to the knowledge agents we proposed, which are good at accepting knowledge from
laboratory documentation.

11
2.
Translation Agents
In k-agents, we included two types of translation agents: code translation agent, which translates instructions into
code, and procedure translation agent, which translates instructions into experiment procedures that may contain
multiple institutions.
Each translation agent is designed to only process instructions that are very close to the
description of an existing experiment. However, by recursively translating the instructions, the whole system can
achieve higher generalizability.
(Initialization) Each code translation agent is directly constructed from a class of experiments. Similarly, pro-
cedure translation agents are also constructed from the structured documents of procedures mentioned above. The
document translation agent will try to translate the instructions that resemble the title of the experiment item into
code that invokes an execution agent to execute the corresponding procedure.
(Activation) Many translation agents might exist based on the complexity of the experimental system. However,
not all translation agents are needed to translate a certain instruction. Therefore, we designed to use embedding
similarity and only activate the agents related to the instruction to be translated. When generating the agent, we use
LLMs to generate a series of natural language instructions {𝐼} that the agent should translate. We further calculate
the embeddings { ®𝐸} of these instructions. When there is an incoming instruction with embedding ®𝐸𝐼, the score 𝑆of
a translation agent is calculated by the maximal inner product between 𝐸𝐼and the vectors in { ®𝐸}.
𝑆= max
®𝐸𝑖∈{ ®𝐸}
®𝐸𝐼· ®𝐸𝑖
†
(1)
(Code translation) When activated, the code translation agent attempts to translate the instruction into exe-
cutable code. The Python class signature for the experiment and the instruction will be passed to an LLM to generate
a code translation based on the class. We employ two strategies to improve the translation accuracy throughout this
process. First, we implement the chain of thought (CoT) [75] strategy to improve performance. Before generating
code, the LLM is first asked to provide a paragraph of analysis on how to approach the translation. This helps guide
the LLM in retrieving key points from the context and making useful inferences. Next, we adopt a self-reflection
strategy to improve the accuracy. The agent will determine whether the instruction should be translated using the
experiment class based on the previous analysis. This step selects out cases where the class is not suitable for the
instruction, helping to avoid hallucinations. If the agent concludes that the instruction should be translated into code
using the class, it proceeds to generate a candidate code snippet. This candidate code is then sent to the execution
agent for comparison with other potential candidates.
(Procedure translation) Our procedure translation agents are designed similarly to code translation agents. If
an agent deems an incoming instruction matches the procedure it holds, it will try to rewrite the procedure title to
suit the instruction. A code snippet that calls an execution agent to execute the rewritten title will then be generated
and sent to the execution agent as a code candidate.
(Generalizability) In both types of translations, the agents generate new code and new instructions based on the
input instruction and therefore generalize the knowledge they have. However, this generalizability is well-controlled
as translations that deviate too much from the agent’s knowledge will be decided as improper by the strategy we
described. This limited generalizability mitigates the negative effect of the LLM’s knowledge from the public corpus
that is not suitable for a private experimental setup.
B.
Details on execution agents
In k-agents, the execution of experiments is controlled by the execution agents. The execution process involves
decomposing the incoming procedure into experiment stages, translating the instruction at each stage into code by
translation agents, executing the generated code, and analyzing the experiment results to determine the next step.
(Instruction decomposition) When handling experiment procedures, we ask the execution agent to decompose
the instructions into experimental stages and make an agent-based state machine. Each stage in the agent-based state
machine contains a single step of the instructions that only includes one experiment or sub-procedure to be translated
by the translation agents. In addition, an experiment procedure might have a complex control flow. For example,
selecting the next instruction to execute might depend on the result of the previous instructions. Therefore, at each
stage, we also attach a prompt on how to select the next stage given the result of this stage.
The stage generation is done roughly in two calls to an LLM. First, we employ the LLM to extract a list of inde-
pendent experiments from the procedure. This step removes all the sentences controlling the procedure’s progression
and generates the instructions at each stage. Then, we add indices to the stages, such as Stage 1 and Stage 2, so their
indices can be used to refer to them when generating the transition rules. We also add two special stages: COMPLETE

12
and FAILED to the list of stages. Finally, we provide the LLM with the list of stages and the original procedure,
asking it to attach the transition rule for each experiment.
(Translation candidate selection) When executing a stage, the execution agent activates the translation agents
Algorithm 1: Translation with self-reflection
1. Set the group of translation agents {𝐴}, the number 𝑁𝑘for the number of activated agents and the number 𝑁max for
the maximal number of activated agents.
2. Input the instruction 𝐼to be translated.
3. Calculate the score of each agent in {𝐴} by Equation 1.
4. For each agent 𝐴whose score is ranked top 𝑁𝑘in {𝐴}, do the following
(a) Using LLM, check whether the instruction can be translated by the knowledge held by 𝐴. If so, generate the code
𝐶that implements the instruction. Else, output nothing.
(b) Add 𝐶to the set of code candidates.
5. If the set of code candidates {𝐶} is empty, increase the number of 𝑁𝑘by 2 and do the following: If 𝑁𝑘< 𝑁max, go back
to step 2. Else, the algorithm fails.
6. If {𝐶} is non-empty, add the instruction and the set of code candidates {𝐶} to the context of LLM and generate the
code 𝐶∗for 𝐼.
7. Output 𝐶∗as the result of translation.
and gathers candidate code from them. Then, the execution agent synthesizes the code to execute on the basis of
the candidates it receives. Specifically, all the candidate code will be input into a LLM with a prompt that ask the
LLM to generate an analysis and the final code for the translation. This synthesis process has two merits. First,
there might be two experiments with similar descriptions. The translation agents for them are likely to generate
candidate code together. By providing them as candidates, we make it possible for LLM to analyze which solution is
more suitable. Further, as the activating mechanism might not be perfect, there might not be any answer from the
translation agents because the desired translation agent is not activated. In this case, we design the execution agent
to try to activate more translation agents until a proper candidate appears. We summarize the translation process in
Algorithm 1. When applying the algorithm in Section II, we set the 𝑁𝑘= 3 and 𝑁max = 9.
(Execution) Starting from the first stage, the execution agent executes the instruction in the current stage by
executing the translated code with the help of the translation agents, as described in the previous section. After
execution, the inspection agent generates a report of the experiment in natural language. Based on the report, the
execution agent chooses the next state to transition to. Finally, after reaching the COMPLETE or the FAILED state,
the execution agent will generate a report of the entire execution. We summarize the execution process in Algorithm 2.
We note that the execution agent also maintains a variable table. At the end of each experiment, variables might
be injected from the experiment for the use of other experiments. The injection of variables can be programmed by
the users when they implement the class for the experiment.
Algorithm 2: Execution agent workflow
1. Input the experiment procedure 𝑃.
2. Using LLM, decompose 𝑃into experiment stages (states) {𝑆} and transition rules {𝑇} at each stage. The decomposition
also specifies an initial state 𝑆0 as the current state 𝑆∗. Two final states COMPLETE and FAILED are also in the {𝑆}.
3. At the current experiment stage 𝑆∗, do the followings
(a) Translate the instruction contained in 𝑆∗into code with the Algorithm 1.
(b) Execute the translated code.
(c) Activate available inspection agents in the executed experiment and summarize the results from them with LLM,
giving a summarized report 𝑅. Add 𝑆∗and 𝑅to the experiment history
(d) Using LLM, decide the next stage to transition to, based on the transition rule 𝑇∗of 𝑆∗and the report 𝑅.
(e) If the next stage is COMPLETE or FAILED, add them to the experiment history and break the loop (i.e., go to
step 4). Else, set 𝑆∗to be the next stage and go to step 3(a).
4. Using LLM, summarize the experiment history and produce a report 𝑅for 𝑃.

13
C.
Quantum processor hardware
The quantum processor used in this experiment consists of 16 coaxmon qubits arranged in a square lattice configu-
ration. Coaxmon qubits, a variant of transmon qubits with coaxial geometry and off-chip wiring, have demonstrated
high coherence, low cross-talk, and stable higher excited states [65, 66, 76, 77].
To enable the execution agents to conduct experiments, we integrated the k-agents framework with the LeeQ
framework [63], customized software used for controlling superconducting quantum processors in the lab. The LeeQ
framework, which has been independently used by human scientists, manages the composition, compilation, and
optimization of quantum gates into executable instructions.
These processed microwave sequences are then sent
to the QubiC system [4], an electronic system that generates and processes microwave signals and connects to the
quantum processor.
In practice, human scientists write code that predefines experiments and reuse it in different scenarios by modifying
the arguments of these experiments. Typically, scientists manually adjust the parameters of these experiments until
they achieve their desired outcome. We adapted these predefined experiments to be compatible with and indexable
by k-agents. In total, the LeeQ framework includes more than 40 built-in experiments, of which we selected 17 for
indexing by the k-agents. For further details on the experiments, please refer to Appendix D.
CODE AVAILABLILITY
The source codes of k-agents can be found in [78]. The codes for experiments and benchmarks can be found in [63].
CONFLICT OF INTEREST DISCLOSURE
A.A.-G. is a founder of Kebotix, Inc., a company specializing in closed-loop molecular discovery, and IntrepidLabs,
Inc. a company using self-driving laboratories for pharmaceuticals. P.L. is the founder and Chief Science Officer of
Oxford Quantum Circuits Limited, a company developing superconducting circuit quantum computers.
ACKNOWLEDGMENTS
The authors thank Yuning Zhang for the insightful discussion. This project is supported by Schmidt Sciences,
LLC. S.C. acknowledges support from Schmidt Science. P.L. acknowledges support from the EPSRC [EP/T001062/1,
EP/N015118/1, EP/M013243/1]. M.B. acknowledges support from EPSRC QT Fellowship grant [EP/W027992/1].
A.A.-G. thanks Anders G. Frseth for his generous support. A.A.-G. also acknowledges the generous support of Natural
Resources Canada and the Canada 150 Research Chairs program. This research is part of the University of Torontos
Acceleration Consortium, which receives funding from the Canada First Research Excellence Fund (CFREF).
[1] G. Tom, S. P. Schmid, S. G. Baird, Y. Cao, K. Darvish, H. Hao, S. Lo, S. Pablo-Garc´ıa, E. M. Rajaonson, M. Skreta,
et al., Chemical Reviews 124, 9633 (2024).
[2] M. Sim, M. G. Vakili, F. Strieth-Kalthoff, H. Hao, R. J. Hickman, S. Miret, S. Pablo-Garc´ıa,
and A. Aspuru-Guzik,
Matter 7, 2959 (2024).
[3] M. Seifrid, F. Strieth-Kalthoff, M. Haddadnia, T. C. Wu, E. Alca, L. Bodo, S. Arellano-Rubach, N. Yoshikawa, M. Skreta,
R. Keunen, et al., Digital Discovery (2024).
[4] Y. Xu, G. Huang, N. Fruitwala, A. Rajagopala, R. K. Naik, K. Nowrouzi, D. I. Santiago, and I. Siddiqi, “Qubic 2.0: An
extensible open-source qubit control system capable of mid-circuit measurement and feed-forward,” (2023).
[5] H. S. Stein and J. M. Gregoire, Chemical Science 10, 96409649 (2019).
[6] Y. Shi, P. L. Prieto, T. Zepel, S. Grunert, and J. E. Hein, Accounts of Chemical Research 54, 546 (2021).
[7] Y. Xie, K. Sattari, C. Zhang, and J. Lin, Progress in Materials Science 132, 101043 (2023).
[8] X. J. Yu, X. Chi, A. T. S. Wee, A. Rusydi,
and M. B. H. Breese, Review of Scientific Instruments 90, 103902 (2019),
https://pubs.aip.org/aip/rsi/article-pdf/doi/10.1063/1.5096007/14710054/103902 1 online.pdf.
[9] M. Seifrid, R. Pollice, A. Aguilar-Granda, Z. Morgan Chan, K. Hotta, C. T. Ser, J. Vestfrid, T. C. Wu, and A. Aspuru-
Guzik, Accounts of Chemical Research 55, 2454 (2022).
[10] T. Brown, B. Mann, N. Ryder, M. Subbiah, J. D. Kaplan, P. Dhariwal, A. Neelakantan, P. Shyam, G. Sastry, A. Askell,
et al., Advances in neural information processing systems 33, 1877 (2020).

14
[11] OpenAI, “Gpt-4 technical report,” (2023), arXiv:2303.08774 [cs.CL].
[12] G. Team, R. Anil, S. Borgeaud, Y. Wu, J.-B. Alayrac, J. Yu, R. Soricut, J. Schalkwyk, A. M. Dai, A. Hauth, et al., arXiv
preprint arXiv:2312.11805 (2023).
[13] A. Dubey, A. Jauhri, A. Pandey, A. Kadian, A. Al-Dahle, A. Letman, A. Mathur, A. Schelten, A. Yang, A. Fan, et al.,
arXiv preprint arXiv:2407.21783 (2024).
[14] H. Liu, C. Li, Q. Wu, and Y. J. Lee, Advances in neural information processing systems 36 (2024).
[15] H. Liu, C. Li, Y. Li,
and Y. J. Lee, in Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern
Recognition (2024) pp. 26296–26306.
[16] Z. Zhang, S. Aronowitz, and A. Aspuru-Guzik, arXiv preprint arXiv:2408.08463 (2024).
[17] G. Li, H. Hammoud, H. Itani, D. Khizbullin, and B. Ghanem, Advances in Neural Information Processing Systems 36,
51991 (2023).
[18] C.-M. Chan, W. Chen, Y. Su, J. Yu, W. Xue, S. Zhang, J. Fu, and Z. Liu, arXiv preprint arXiv:2308.07201 (2023).
[19] Q. Wu, G. Bansal, J. Zhang, Y. Wu, S. Zhang, E. Zhu, B. Li, L. Jiang, X. Zhang,
and C. Wang, arXiv preprint
arXiv:2308.08155 (2023).
[20] Y. Talebirad and A. Nadiri, arXiv preprint arXiv:2306.03314 (2023).
[21] Y. Zhang, S. Yang, C. Bai, F. Wu, X. Li, X. Li, and Z. Wang, arXiv preprint arXiv:2405.14314 (2024).
[22] T. Guo, X. Chen, Y. Wang, R. Chang, S. Pei, N. V. Chawla, O. Wiest, and X. Zhang, arXiv preprint arXiv:2402.01680
(2024).
[23] X. Li, S. Wang, S. Zeng, Y. Wu, and Y. Yang, Vicinagearth 1, 9 (2024).
[24] J. Kaplan, S. McCandlish, T. Henighan, T. B. Brown, B. Chess, R. Child, S. Gray, A. Radford, J. Wu, and D. Amodei,
arXiv preprint arXiv:2001.08361 (2020).
[25] Z. Li, N. Zhang, Y. Yao, M. Wang, X. Chen,
and H. Chen, in The Twelfth International Conference on Learning
Representations (2024).
[26] J. Hoelscher-Obermaier, J. Persson, E. Kran, I. Konstas, and F. Barez, arXiv preprint arXiv:2305.17553 (2023).
[27] N. Zhang, Y. Yao, B. Tian, P. Wang, S. Deng, M. Wang, Z. Xi, S. Mao, J. Zhang, Y. Ni, et al., arXiv preprint
arXiv:2401.01286 (2024).
[28] P. Lewis, E. Perez, A. Piktus, F. Petroni, V. Karpukhin, N. Goyal, H. K¨uttler, M. Lewis, W.-t. Yih, T. Rockt¨aschel, et al.,
Advances in Neural Information Processing Systems 33, 9459 (2020).
[29] Y. Gao, Y. Xiong, X. Gao, K. Jia, J. Pan, Y. Bi, Y. Dai, J. Sun, and H. Wang, arXiv preprint arXiv:2312.10997 (2023).
[30] V. Karpukhin, B. O˘guz, S. Min, P. Lewis, L. Wu, S. Edunov, D. Chen, and W.-t. Yih, arXiv preprint arXiv:2004.04906
(2020).
[31] A. Franklin and S. Perovic, (1998).
[32] D. A. Boiko, R. MacKnight, B. Kline, and G. Gomes, Nature 624, 570 (2023).
[33] A. M. Bran, S. Cox, O. Schilter, C. Baldassari, A. D. White, and P. Schwaller, Nature Machine Intelligence , 1 (2024).
[34] K. Darvish, M. Skreta, Y. Zhao, N. Yoshikawa, S. Som, M. Bogdanovic, Y. Cao, H. Hao, H. Xu, A. Aspuru-Guzik, et al.,
arXiv preprint arXiv:2401.06949 (2024).
[35] N. Yoshikawa, M. Skreta, K. Darvish, S. Arellano-Rubach, Z. Ji, L. Bjørn Kristensen, A. Z. Li, Y. Zhao, H. Xu, A. Ku-
ramshin, et al., Autonomous Robots 47, 1057 (2023).
[36] N. F. Liu, K. Lin, J. Hewitt, A. Paranjape, M. Bevilacqua, F. Petroni,
and P. Liang, arXiv preprint arXiv:2307.03172
(2023).
[37] T. Li, G. Zhang, Q. D. Do, X. Yue, and W. Chen, arXiv preprint arXiv:2404.02060 (2024).
[38] D. Li, R. Shao, A. Xie, Y. Sheng, L. Zheng, J. Gonzalez, I. Stoica, X. Ma, and H. Zhang, in NeurIPS 2023 Workshop on
Instruction Tuning and Instruction Following (2023).
[39] R. Acharya, L. Aghababaie-Beni, I. Aleiner, T. I. Andersen, M. Ansmann, F. Arute, K. Arya, A. Asfaw, N. Astrakhantsev,
J. Atalaya, et al., arXiv preprint arXiv:2408.13687 (2024).
[40] B. W. Reichardt, D. Aasen, R. Chao, A. Chernoguzov, W. van Dam, J. P. Gaebler, D. Gresh, D. Lucchetti, M. Mills, S. A.
Moses, et al., arXiv preprint arXiv:2409.04628 (2024).
[41] H. Putterman, K. Noh, C. T. Hann, G. S. MacCabe, S. Aghaeimeibodi, R. N. Patel, M. Lee, W. M. Jones, H. Moradinejad,
R. Rodriguez, et al., arXiv preprint arXiv:2409.13025 (2024).
[42] B. L. Brock, S. Singh, A. Eickbusch, V. V. Sivak, A. Z. Ding, L. Frunzio, S. M. Girvin, and M. H. Devoret, arXiv preprint
arXiv:2409.15065 (2024).
[43] M. Mohseni, A. Scherer, K. G. Johnson, O. Wertheim, M. Otten, N. A. Aadit, K. M. Bresniker, K. Y. Camsari, B. Chapman,
S. Chatterjee, G. A. Dagnew, A. Esposito, F. Fahim, M. Fiorentino, A. Khalid, X. Kong, B. Kulchytskyy, R. Li, P. A.
Lott, I. L. Markov, R. F. McDermott, G. Pedretti, A. Gajjar, A. Silva, J. Sorebo, P. Spentzouris, Z. Steiner, B. Torosov,
D. Venturelli, R. J. Visser, Z. Webb, X. Zhan, Y. Cohen, P. Ronagh, A. Ho, R. G. Beausoleil, and J. M. Martinis, “How
to build a quantum supercomputer: Scaling challenges and opportunities,” (2024), arXiv:2411.10406.
[44] M. Krenn, R. Pollice, S. Y. Guo, M. Aldeghi, A. Cervera-Lierta, P. Friederich, G. dos Passos Gomes, F. H¨ase, A. Jinich,
A. Nigam, et al., Nature Reviews Physics 4, 761 (2022).
[45] S. Yao, N. Shinn, P. Razavi, and K. Narasimhan, arXiv preprint arXiv:2406.12045 (2024).
[46] H. Wang, R. Wang, B. Xue, H. Xia, J. Cao, Z. Liu, J. Z. Pan, and K.-F. Wong, arXiv preprint arXiv:2410.19743 (2024).
[47] A. Blais, R.-S. Huang, A. Wallraff, S. M. Girvin, and R. J. Schoelkopf, Phys. Rev. A 69, 062320 (2004).
[48] R. Acharya, I. Aleiner, R. Allen, T. I. Andersen, M. Ansmann, F. Arute, K. Arya, A. Asfaw, J. Atalaya, R. Babbush,
D. Bacon, J. C. Bardin, J. Basso, A. Bengtsson, S. Boixo, G. Bortoli, A. Bourassa, J. Bovaird, L. Brill, M. Broughton,
B. B. Buckley, D. A. Buell, T. Burger, B. Burkett, N. Bushnell, Y. Chen, Z. Chen, B. Chiaro, J. Cogan, R. Collins,

15
P. Conner, W. Courtney, A. L. Crook, B. Curtin, D. M. Debroy, A. Del Toro Barba, S. Demura, A. Dunsworth, D. Eppens,
C. Erickson, L. Faoro, E. Farhi, R. Fatemi, L. Flores Burgos, E. Forati, A. G. Fowler, B. Foxen, W. Giang, C. Gidney,
D. Gilboa, M. Giustina, A. Grajales Dau, J. A. Gross, S. Habegger, M. C. Hamilton, M. P. Harrigan, S. D. Harrington,
O. Higgott, J. Hilton, M. Hoffmann, S. Hong, T. Huang, A. Huff, W. J. Huggins, L. B. Ioffe, S. V. Isakov, J. Iveland,
E. Jeffrey, Z. Jiang, C. Jones, P. Juhas, D. Kafri, K. Kechedzhi, J. Kelly, T. Khattar, M. Khezri, M. Kieferov´a, S. Kim,
A. Kitaev, P. V. Klimov, A. R. Klots, A. N. Korotkov, F. Kostritsa, J. M. Kreikebaum, D. Landhuis, P. Laptev, K.-M.
Lau, L. Laws, J. Lee, K. Lee, B. J. Lester, A. Lill, W. Liu, A. Locharla, E. Lucero, F. D. Malone, J. Marshall, O. Martin,
J. R. McClean, T. McCourt, M. McEwen, A. Megrant, B. Meurer Costa, X. Mi, K. C. Miao, M. Mohseni, S. Montazeri,
A. Morvan, E. Mount, W. Mruczkiewicz, O. Naaman, M. Neeley, C. Neill, A. Nersisyan, H. Neven, M. Newman, J. H.
Ng, A. Nguyen, M. Nguyen, M. Y. Niu, T. E. O’Brien, A. Opremcak, J. Platt, A. Petukhov, R. Potter, L. P. Pryadko,
C. Quintana, P. Roushan, N. C. Rubin, N. Saei, D. Sank, K. Sankaragomathi, K. J. Satzinger, H. F. Schurkus, C. Schuster,
M. J. Shearn, A. Shorter, V. Shvarts, J. Skruzny, V. Smelyanskiy, W. C. Smith, G. Sterling, D. Strain, M. Szalay, A. Torres,
G. Vidal, B. Villalonga, C. Vollgraff Heidweiller, T. White, C. Xing, Z. J. Yao, P. Yeh, J. Yoo, G. Young, A. Zalcman,
Y. Zhang, N. Zhu, and G. Q. AI, Nature 614, 676 (2023).
[49] P. Krantz, M. Kjaergaard, F. Yan, T. P. Orlando, S. Gustavsson, and W. D. Oliver, Applied Physics Reviews 6, 021318
(2019), https://pubs.aip.org/aip/apr/article-pdf/doi/10.1063/1.5089550/16667201/021318 1 online.pdf.
[50] M. Kjaergaard, M. E. Schwartz, J. Braum¨uller, P. Krantz, J. I.-J. Wang, S. Gustavsson, and W. D. Oliver, Annual Review
of Condensed Matter Physics 11, 369 (2020).
[51] S. Sheldon, E. Magesan, J. M. Chow, and J. M. Gambetta, Phys. Rev. A 93, 060302 (2016).
[52] K. X. Wei, I. Lauer, E. Pritchett, W. Shanks, D. C. McKay, and A. Javadi-Abhari, PRX Quantum 5, 020338 (2024).
[53] A. Maksymov, P. Niroula, and Y. Nam, Quantum Science and Technology 6, 034009 (2021).
[54] Z. D. Romaszko, S. Hong, M. Siegele, R. K. Puddy, F. R. Lebrun-Gallagher, S. Weidt,
and W. K. Hensinger, Nature
Reviews Physics 2, 285 (2020).
[55] C. D. Bruzewicz, J. Chiaverini, R. McConnell, and J. M. Sage, Applied Physics Reviews 6 (2019).
[56] T. Botzem, M. D. Shulman, S. Foletti, S. P. Harvey, O. E. Dial, P. Bethke, P. Cerfontaine, R. P. McNeil, D. Mahalu,
V. Umansky, et al., Physical Review Applied 10, 054026 (2018).
[57] G. Burkard, T. D. Ladd, A. Pan, J. M. Nichol, and J. R. Petta, Reviews of Modern Physics 95, 025003 (2023).
[58] A. Chatterjee, P. Stevenson, S. De Franceschi, A. Morello, N. P. de Leon, and F. Kuemmeth, Nature Reviews Physics 3,
157 (2021).
[59] P. Stano and D. Loss, Nature Reviews Physics 4, 672 (2022).
[60] X. Wu, X. Liang, Y. Tian, F. Yang, C. Chen, Y.-C. Liu, M. K. Tey, and L. You, Chinese Physics B 30, 020305 (2021).
[61] C. S. Adams, J. D. Pritchard, and J. P. Shaffer, Journal of Physics B: Atomic, Molecular and Optical Physics 53, 012002
(2019).
[62] I. Cong, H. Levine, A. Keesling, D. Bluvstein, S.-T. Wang, and M. D. Lukin, Physical Review X 12, 021049 (2022).
[63] S. Cao, Z. Zhang,
and M. Alghadeer, “Leeq: a python package for orchestrating quantum computing experiments,”
https://github.com/ShuxiangCao/LeeQ (2024).
[64] M. Alghadeer, S. Cao, S. D. Fasciati, M. Piscitelli, P. C. Gow, J. C. Gates, M. Bakr, and P. J. Leek, “Low crosstalk in a
scalable superconducting quantum lattice,” (2025), arXiv:2505.22276.
[65] P. A. Spring, S. Cao, T. Tsunoda, G. Campanaro, S. Fasciati, J. Wills, M. Bakr, V. Chidambaram, B. Shteynas, L. Car-
penter, P. Gow, J. Gates, B. Vlastakis, and P. J. Leek, Science Advances 8 (2022), 10.1126/sciadv.abl6698.
[66] J. Rahamim, T. Behrle, M. J. Peterer, A. Patterson, P. A. Spring, T. Tsunoda, R. Manenti, G. Tancredi, and P. J. Leek,
Applied Physics Letters 110, 222602 (2017), https://doi.org/10.1063/1.4984299.
[67] M. Alghadeer, S. D. Fasciati, S. Cao, M. Piscitelli, M. C. Spink, D. G. Hopkinson, M. Danaie, S. C. Speller, P. J.
Leek,
and M. Bakr, “Characterization of nanostructural imperfections in superconducting quantum circuits,”
(2025),
arXiv:2501.15059.
[68] B. K. Mitchell, R. K. Naik, A. Morvan, A. Hashim, J. M. Kreikebaum, B. Marinelli, W. Lavrijsen, K. Nowrouzi, D. I.
Santiago, and I. Siddiqi, Phys. Rev. Lett. 127, 200502 (2021).
[69] H. Xiong, Q. Ficheux, A. Somoroff, L. B. Nguyen, E. Dogan, D. Rosenstock, C. Wang, K. N. Nesterov, M. G. Vavilov,
and V. E. Manucharyan, Phys. Rev. Res. 4, 023040 (2022).
[70] K. Wei, E. Magesan, I. Lauer, S. Srinivasan, D. Bogorin, S. Carnevale, G. Keefe, Y. Kim, D. Klaus, W. Landers, et al.,
arXiv preprint arXiv:2106.00675 (2021).
[71] K. X. Wei, E. Magesan, I. Lauer, S. Srinivasan, D. F. Bogorin, S. Carnevale, G. A. Keefe, Y. Kim, D. Klaus, W. Landers,
N. Sundaresan, C. Wang, E. J. Zhang, M. Steffen, O. E. Dial, D. C. McKay,
and A. Kandala, Phys. Rev. Lett. 129,
060501 (2022).
[72] G. Wang, Y. Xie, Y. Jiang, A. Mandlekar, C. Xiao, Y. Zhu, L. Fan, and A. Anandkumar, arXiv preprint arXiv:2305.16291
(2023).
[73] Z. S. Wattoo, P. Vitis, R. Zhu, N. Depner, I. Zhang, J. Hein, A. Gujarati, and M. Seltzer, in 2024 54th Annual IEEE/IFIP
International Conference on Dependable Systems and Networks (DSN) (IEEE, 2024) pp. 353–361.
[74] S. X. Leong, C. E. Griesbach, R. Zhang, K. Darvish, Y. Zhao, A. Mandal, Y. Zou, H. Hao, V. Bernales, and A. Aspuru-
Guzik, (2024).
[75] J. Wei, X. Wang, D. Schuurmans, M. Bosma, F. Xia, E. Chi, Q. V. Le, D. Zhou, et al., Advances in neural information
processing systems 35, 24824 (2022).
[76] S. Cao, D. Lall, M. Bakr, G. Campanaro, S. D. Fasciati, J. Wills, V. Chidambaram, B. Shteynas, I. Rungger, and P. J.
Leek, Phys. Rev. Lett. 133, 120802 (2024).

16
[77] S. Cao, M. Bakr, G. Campanaro, S. D. Fasciati, J. Wills, D. Lall, B. Shteynas, V. Chidambaram, I. Rungger, and P. Leek,
Quantum Science and Technology 9, 035003 (2024).
[78] Z. Zhang and S. Cao, “k-agents: knowledge-based agents for automation,” https://github.com/EvoEvolver/k_agents
(2024).
[79] N. Research, “Nous hermes 2 - yi-34b,” https://huggingface.co/NousResearch/Nous-Hermes-2-Yi-34B (2024).
[80] J. Emerson, R. Alicki, and K. ˙Zyczkowski, Journal of Optics B: Quantum and Semiclassical Optics 7, S347 (2005).
[81] C. Dankert, R. Cleve, J. Emerson, and E. Livine, Phys. Rev. A 80, 012304 (2009).
[82] E. Magesan, J. M. Gambetta, B. R. Johnson, C. A. Ryan, J. M. Chow, S. T. Merkel, M. P. da Silva, G. A. Keefe, M. B.
Rothwell, T. A. Ohki, M. B. Ketchen, and M. Steffen, Phys. Rev. Lett. 109, 080505 (2012).
Appendix A: Details on knowledge representation
1.
Representing knowledge of available experiments
In k-agents, laboratory experiments (and actions) are formulated as sub-classes of an abstract class Experiment. The
abstract class provides a few interfaces to put the documentation and code of the experiment. We use the following
example to demonstrate how the interfaces are used.
An example of experiment class
class
SimpleRamseyMultilevel (Experiment):
_experiment_result_analysis_instructions = """
␣␣␣␣The␣Ramsey␣experiment␣is␣a␣quantum␣mechanics␣experiment ␣that␣involves␣the␣measurement ␣of␣oscillations ␣
in␣the␣quantum␣state␣of␣a␣qubit.␣Typically ,␣a␣successful ␣Ramsey␣experiment ␣will␣show␣a␣clear ,␣regular␣
oscillatory␣pattern␣with␣an␣amplitude␣greater␣than␣0.2.␣If␣less␣than␣approximately ␣3␣oscillations ␣are␣
observed ,␣the␣experiment␣requires␣an␣increase␣in␣the␣time␣of␣the␣experiment .␣If␣more␣than␣10␣
oscillations ␣are␣observed ,␣the␣experiment ␣requires␣a␣decrease␣in␣the␣time␣of␣the␣experiment .␣The␣
frequency␣of␣the␣oscillations ␣should␣be␣less␣than␣the␣expected␣offset␣value.
␣␣␣␣"""
def run(self ,
qubit ,
collection_name : str = ’f01’,
mprim_index: int = 0,
initial_lpb: Optional[Any] = None ,
start: float = 0.0,
stop: float = 1.0,
step: float = 0.005 ,
set_offset: float = 10.0 ,
update: bool = True) -> None:
"""
␣␣␣␣␣␣␣␣Ramsey␣experiment␣for␣estimating␣the␣qubit␣frequency␣or␣T2␣Ramsey.
␣␣␣␣␣␣␣␣Parameters:
␣␣␣␣␣␣␣␣␣␣␣␣qubit:␣The␣qubit␣on␣which␣the␣experiment␣is␣performed.
␣␣␣␣␣␣␣␣␣␣␣␣collection_name :␣The␣name␣of␣the␣frequency␣collection␣(e.g.,␣’f01 ’).
␣␣␣␣␣␣␣␣␣␣␣␣mprim_index:␣The␣index␣of␣the␣measurement ␣primitive.
␣␣␣␣␣␣␣␣␣␣␣␣initial_lpb:␣Initial␣set␣of␣commands ,␣if␣any.
␣␣␣␣␣␣␣␣␣␣␣␣start:␣The␣start␣time␣for␣the␣sweep.
␣␣␣␣␣␣␣␣␣␣␣␣stop:␣The␣stop␣time␣for␣the␣sweep.
␣␣␣␣␣␣␣␣␣␣␣␣step:␣The␣step␣size␣for␣the␣frequency␣sweep.
␣␣␣␣␣␣␣␣␣␣␣␣set_offset:␣The␣frequency␣offset.
␣␣␣␣␣␣␣␣␣␣␣␣update:␣Whether␣to␣update␣parameters ␣after␣the␣experiment .
␣␣␣␣␣␣␣␣"""
...
@visual_inspection ("""
␣␣␣␣␣␣␣␣Here␣is␣a␣plot␣of␣data␣from␣a␣quantum␣mechanics␣experiment ␣involving␣Ramsey␣oscillations .␣Can␣you␣
analyze␣whether␣this␣plot␣shows␣a␣successful ␣experiment␣or␣a␣failed␣one?␣Please␣consider␣the␣following
␣aspects␣in␣your␣analysis:
␣␣␣␣␣␣␣␣1.␣Clarity␣of␣Oscillation:␣Describe␣if␣the␣data␣points␣show␣a␣clear ,␣regular␣oscillatory ␣pattern.
␣␣␣␣␣␣␣␣2.␣Fit␣Quality:␣Evaluate␣whether␣the␣fit␣line␣closely␣follows␣the␣data␣points␣throughout ␣the␣plot.
␣␣␣␣␣␣␣␣3.␣Data␣Spread:␣Assess␣if␣the␣data␣points␣are␣tightly␣clustered␣around␣the␣fit␣line␣or␣if␣they␣are␣
widely␣dispersed.
␣␣␣␣␣␣␣␣4.␣Amplitude␣and␣Frequency:␣Note␣any␣inconsistencies ␣in␣the␣amplitude␣and␣frequency␣of␣the␣
oscillations .␣For␣a␣perfect␣experiment ,␣the␣amplitude␣should␣be␣around␣1,␣and␣the␣frequency␣should␣be␣
close␣to␣the␣expected␣value.␣If␣the␣amplitude␣is␣smaller␣than␣0.2,␣the␣experiment␣is␣likely␣considered
␣failed.
␣␣␣␣␣␣␣␣5.␣Overall␣Pattern:␣Provide␣a␣general␣assessment␣of␣the␣plot␣based␣on␣the␣typical␣characteristics ␣
of␣successful␣Ramsey␣oscillation␣experiments .
␣␣␣␣␣␣␣␣Here␣is␣an␣example␣of␣a␣successful␣experiment :
␣␣␣␣␣␣␣␣Image("sucecss.jpg")
␣␣␣␣␣␣␣␣Here␣is␣an␣example␣of␣a␣failed␣experiment :
␣␣␣␣␣␣␣␣Image("fail.jpg")
␣␣␣␣␣␣␣␣""")
def
plot(self):
...
@text_inspection
def
fitting(self):

17
...
return {
"success": True ,
"analysis": "The␣experiment␣is␣successful␣based␣on␣the␣fitting␣results."
}
The run method of the class holds the lower-level code that carries out the experiment. The docstring of this
method holds the description of the experiment and the required arguments. This information will be used when the
corresponding code translation agent tries to interpret instructions into code with this class.
The results of many experiments are more intuitive if they are represented in figures. However, interpreting these
figures requires domain-specific knowledge, which is beyond the scope of most multimodal LLMs. For this, we provide
a function decorator visual inspection to represent the knowledge of how to analyze the figure. The decorator accepts a
prompt as a parameter and uses it to generate a visual inspection agent that keeps the prompt as its knowledge. When
the experiment is finished, and the experiment results are available in the experiment object, visual inspection agents
will be called with the newly produced figures. The visual inspection agent will put the figure into a multimodal LLM
along with the prompt to produce the report. We additionally note that our decorator accepts few-shot prompting.
All the patterns Image(”*”) in the parameter, where * is a path to an image, will be automatically detected and
replaced by the corresponding image located at the path.
Besides visual methods to analyze experiment results, we also provide an interface to produce inspection agents in
a more general form. For example, an experiment’s result can also be analyzed by numerical methods such as fittings.
In these cases, the k-agents framework encourages the users to implement methods that produce reports in texts for
the reference of execution agents. The users can use the decorator text inspection to mark the methods that produce
a report for inspecting experiment results. Similarly, the decorator also produces inspection agents that will be called
when the experiment is finished.
There might exist many inspection agents in an experiment class, and the reports they produce may be too long for
the execution agent to use directly. The class variable experiment result analysis instructions provides an interface to
inject the knowledge of how to summarize the reports from the inspection agents. Execution agents use this knowledge
to summarize the reports and decide the next stage to transition to.
2.
Representing knowledge of experiment procedures
The knowledge of a laboratory can also exist in experiment procedures, which describe how to decompose an
instruction into a procedure that may contain many dependent instructions. To help our agents extract this knowledge
more efficiently, we propose the following structured format for them.
An example of structured experiment procedure
# Complete
Calibrating
Single
Qubit ‘dut ‘
##
Background
The
process
of
recalibrating a single
qubit is
crucial
to
maintaining
optimal
quantum
computation
performance. This
recalibration
process
involves
three
key
steps: frequency
calibration , amplitude
calibration , and
DRAG
parameter
calibration . Each
step is aimed at
refining
different
aspects
of the
qubit ’s operational
parameters
to
ensure
accurate
and
reliable
qubit
control. The
sequence
of these
steps is critical , as each
builds
on the
stability
achieved
in the
previous
step.
## Steps
- Do
frequency
Calibration
on ‘dut ‘
- Do
amplitude
Calibration
on ‘dut ‘
- Do DRAG
Calibration
on ‘dut ‘
##
Results
- Whether
the
experiments
are
successful
In our format, each experiment procedure is organized in the Markdown format. Each procedure starts from a
first-level header, which starts with # and the title of the experiment. Then, our format accepts three sub-sections:
Background, Steps and Results, in which the Steps section is necessary. Each sub-section should start from a second-
level header as shown in the example.
The Background section is provided to place important background knowledge of the procedure. It can be included
in the prompts of the agents to clarify the usage of the procedure.

18
A procedure translation agent who carries the above information will try to match instructions that are similar to
the title of the procedure and modify the procedure in the Steps section to implement the incoming instruction.
Finally, knowledge in the Results section is used to summarize the results of the execution of the procedure and
generate a report for the reference of execution agents.
Appendix B: Details on implementing agents
We discuss the details of the implementation of the agents in the k-agents framework. We especially select important
prompts that are used to implement the key functionalities of the agents. We omit the inspection agents as their
structure is relatively simple, as we have discussed in previous sections.
1.
Code translation agent
When constructing a code translation agent from an experiment class, a few instructions that match the class will
be generated with the following prompt.
Prompt for generating possible instructions
You are
trying to
produce
imperative
sentences
that
would
invoke
the
execution
of action
‘{exp_name}‘ based
on its
documentation .
<docstring >
{ doc_string}
</docstring >
<example >
Here
are a few of
examples
of
imperative
sentences:
- Run the
calibration
experiment
with
duts=‘duts ‘ and
start =0.0
- Carry
out a calibration
on ‘duts ‘
- Please
execute
the
Ramsey
experiment
- Do the
Drag
experiment.
</example >
<instruction >
You
should
output a JSON
dict. The
keys
should be string of
indices
of the
sentences
and the
values
should
be the
sentences.
Each
sentence
should be
complete
and
independent . Name of the
experiment
should be
transformed
to
natural
language
and be
mentioned.
The
sentences
should
be
imperative
and
should be based on the
documentation .
You
should
output 4 sentences.
</instruction >
The instructions will be converted to a list of feature vectors (embeddings) that represent their semantic meaning
using an embedding model. These vectors will be used to calculate the matching score of the experiment given a
set of instructions to be translated. The score is calculated as the maximum value of the inner product between the
embeddings of the instructions to be translated and the generated instructions.
After being activated, the code translation agent will try to generate candidate code that implements the instruction.
The prompt for generation is listed below.
Prompt for generating candidate code
You are
trying to call an
experiment
to fill
the
code_to_complete
in Python. The
description
of the
task is
written
in the
slot.
<experiment >
{self. get_exp_description ()}
</experiment >
<code_to_complete >
# [slot: {instruction }]
</code_to_complete >
<available_variables >
{ available_variables }
</available_variables >
<requirements >
You
should
output a JSON
dict. The
keys
should be
- " experiment_name_in_slot " (string): The
name of the
experiment
extracted
from
the
slot.
- "analysis" : The
brief
analysis
of the
relation
between
the
experiment
and the
code_to_complete . You
should
notice
that
the
code_to_complete
might be
irrelevant
to the
experiment . You
should be
careful
not to assume
additional
information. The
experiment
should
considered
irrelevant
if it
contains
extra
keywords
or
irrelevant
information.
- " applicable ": A boolean
whether
the
experiment
you
hold is
suitable
for
implementing
the
task.
- "code ": A code
snippet
that is
helpful
for
filling
the
slot. The
last
line of the
snippet
must be in the
format: ‘experiment_ <name > = {self.exp_cls.__name__ }( argument1 ,argument2 , ...) ‘. No import
statements
are
needed.

19
- "explanation ": A detailed
explanation
of what
the
code
snippet
does
based
solely on the
documentation .
- "suitable ": A boolean
whether
the
code
snippet
matches
the
task
based on the
documentation .
</requirements >
2.
Procedure translation agent
When initializing procedure translation agents, similar to code translation agents, a few variants of the procedure’s
title will be generated for their activation.
When activated, a procedure translation agent first checks whether the given instruction to translate matches the
procedure title it holds. Then, the agent tries to rewrite the given instruction into a format that is closer to the
procedure’s title it knows. In the meantime, as many experiment procedures require inputs, the agent also generates
a map that maps the available variables in the context to the required inputs of the procedure.
Prompt for rewriting instructions based on knowledge of an experiment procedure
You are
trying to
rewrite
the
following
instruction
based on your
knowledge
to suit
more
general
parameters
.
<input_instruction >
{ instruction }
</input_instruction >
The
following
variables
names
are
defined
in the
context
and you can
directly
use the
variables
names.
<available_variables >
{ available_variables }
</available_variables >
By your
knowledge , there is an
existing
instruction
that is
available
<knowledge >
<instruction >
{ procedure_title }
</instruction >
</knowledge >
<requirements >
You are
required
to output a JSON
dict
with
the
following
keys
- " parameter_specification " (string): The
specification
of the
parameters
of the
input_instruction
- "analysis" (string): An
analysis
of the
relation
between
the
input_instruction
and
your
knowledge. You
should
notice
that
your
knowledge
is likely to be
improper
if the
experiment
name
contains
different
keywords. However , the
parameter_specification
of the
experiment
can be
different.
- "proper" (bool): Whether
the
input_instruction
can be
regarded
as a proper
instance
of the
experiment
in
your
knowledge.
- " rewritten_instruction " (string): The
input_instruction
rewritten
in a way
based on the
instruction
in
your
knowledge. You
should
not
change
the
parameter
specification
of the
input_instruction .
- " parameter_mapping " (dict): A mapping
from
the
parameters
in the
input_instruction
to the
parameters
in
the
rewrote_instruction . The
keys
should
be the
parameters
in the
rewrote_instruction
and the
values
should
be the
parameters
in the
input_instruction
or the
value
from
the
description .
- " annotation " (string): A concise
annotation
that
describe
how you are
confident
that
the
rewritten_instruction
is
correct.
</requirements >
After the rewriting, the procedure translation agent wraps the rewritten instruction into a new experiment that
runs the instruction with a new execution agent. The code that calls the new experiment is sent to the execution
agent as a code candidate.
3.
Execution agent (Stage generation)
Given an experiment procedure, an execution agent will decompose it into stages. Specifically, the decomposition
is implemented by a pipeline of LLM calls. The core step in the pipeline is to extract the stages with all the other
information dropped.
Prompt for stage extraction
<experiment_description >
{ description }
</ experiment_description >
<objective >
Your
objective
is to
decompose
the
experiment
description
into
standalone
instruction .
Each
instruction
should
include
an
experiment .
The
instructions
should
make a minimal
modification
to the
original
description .
You
should
not
make
any
inferences
or
interpret
the
description .
You are
encouraged
to copy
the
description
as is.
You
should
output as few
instructions
as
possible. You
must
not
expand
the
instructions .

20
The
instructions
must
not
contain
any
information
about
what to do next
after
the
instruction , such as a
change
of
parameter
and go to fail.
</requirements >
<example >
For
example , if a piece of
description
is:
"Run
experiment A with
frequency =10. If failed , retry 3 times ."
You
should
change it into:
"Run
experiment A with
frequency =10."
<output_format >
You are
required
to output a JSON
dict
with a single
key " instructions ", which
contains a list of
instructions . Each
instruction
should be
represented
as a string.
</output_format >
After the extraction, the generated stages are input to LLM again to generate the corresponding transition rules.
We also add additional steps to extract the numbers in the instructions and save them as a key-value map in each
stage. This allows the execution agent to change these numbers in a state transition when needed.
4.
Execution agent (Stage transition)
After executing the experiment in a stage, the execution agent decides the next stage to transition to based on the
summary of the reports from the inspection agents. The prompt for deciding the next stage includes the summary, the
information of the current stage, including how many times it has been executed, and transition rules. A maximum
retry limit has been included in the prompt to prevent the model from entering an endless loop.
Prompt for stage transition
You are
analyzing
experiment
result
from
current
stage
and use the
rule of
transition
to
determine
the
next
stage of the
experiment.
<current_stage >
{ current_stage .label }:{ current_stage .description }
The
current
stage
has
been
executed { current_stage . n_executed } times.
There
are { current_stage .n_failed} failed
attempts
and { current_stage .n_success} successful
attempts.
</current_stage >
Here
are the
results
from
the
experiments . Note
that
results
must be
consistent
to
indicate
the
validity.
Otherwise
they
are
both
invalid.
<experiment_reports >
{ result_prompt }
</experiment_reports >
<rule_of_transition >
{rules}
</rule_of_transition >
<requirements >
Return
your
decision
in JSON
format
With
the
following
keys:
"analysis" (string): an
analysis
of the
results
and the
rule of
transition
to
determine
the
next
stage.
"next" (string): the
name of the
next
stage.
</requirements >
After deciding on the next stage, we also include additional steps to modify the variables in the next stage because
the inspection agent might propose modifying the parameters. This step is especially important when an instruction
needs to be retried with a different set of parameters.
Appendix C: Benchmarking our methods
1.
Benchmarking translation
To test the performance of translating instructions into code, we manually make a test set that consists of 80 pairs
of experiments and instructions. This dataset is for benchmarking the performance and it is not required to use our
framework in practice. For example, for the NormalisedRabi experiment, which calibrates the driving frequency of a
single qubit, we set the following instructions in the test set.

21
Examples of the instructions for NormalisedRabi
- Run
rabi
experiment
to
calibrate
single
qubit
gate
driving
amplitudes
- Measure
Rabi
oscillations
to
determine
single
qubit
gate
driving
amplitudes
- Implement
Rabi
experiment
to find pi pulse
duration
- Calibrate
the
driving
amplitudes
for
single
qubit
gate by Rabi
- Determine
single
qubit
gate
parameter
using
Rabi
experiment
- Run
Rabi
experiment
with
default
parameters
on the
single
qubit ‘dut ‘
- Single
qubit
gate
amplitudes
estimation
using
Rabi
experiments
- Do Rabi
experiment
to
measure
single
qubit
drive
amplitudes
- Run
Rabi
experiment
on single
qubit ‘dut ‘ with
amp =0.3
- Calibrate
single
qubit
drive
amplitudes
using
Rabi
experiment ’
In k-agents, the translation is done by calling the related translation agents, and the execution agent picks one
of the code candidates from the translation agents. Specifically, this selection is implemented by inputting all the
code candidates, together with the instruction to translate, to an LLM for analysis (See Algorithm 1). To implement
the standard RAG implementation of this process, after retrieving the related translation agents, we extract the
experiment classes from them and use the signature and documentation of these classes to generate a translation
of the instruction (See Algorithm 3 for detail). The same process of embedding-based retrieving ensures that the
increase in performance is caused by our agent-based reflexion and selection process.
Algorithm 3: Translation with standard RAG
1. Set the group of translation agents {𝐴}, the number 𝑁𝑘for the number of activated agents and the number 𝑁max for
the maximal number of activated agents.
2. Input the instruction 𝐼to be translated.
3. Calculate the score of each agent in {𝐴} by Equation 1.
4. For each agent 𝐴whose score is ranked top 𝑁𝑘in {𝐴}, add the experiment description it carries to {𝐶}.
5. Input the instruction and the experiment descriptions in {𝐶} to LLM and generate the code 𝐶∗for 𝐼.
6. Output 𝐶∗as the result of translation.
For a fair comparison, we only included code translation agents in the benchmark as the information as the prompt
for code generation with procedures is different from that with experiment classes (See Section B 2). Finally, we
include 17 experiment classes in the benchmark.
When triggering the translation agents, we select the 2 agents
with the highest score. If there is no available code candidate, we increase the number of agents to trigger by 2.
Accordingly, we set 2 as the number of experiment classes retrieved in the RAG method being compared.
After
the instructions are translated into code, we check the correctness of the code by analyzing its abstract syntax tree.
A search for a function call to the correct experiment will be carried out. If such a function call is not found, the
translation is marked as incorrect. If a function call to the correct experiment exists, the format of the call will be
further checked to ensure the call is valid. Translations that pass this check will be marked as correct. We note that
we only check the format of the function and do not verify whether the values of the inputs are correct.
We additionally note that we use the text-embedding-3-large model from OpenAI as the embedding model throughout
all the experiments, even when the LLM we use is not from OpenAI. We use the same embedding model to control
the variables and compare differences just in the performance of LLMs.
2.
Comparison with long-prompt apporach
Many large language models (LLMs) now support long inputs, enabling them to process entire codebses. However,
aside from the significant cost implications, prior studies have shown that providing long inputs can impair LLM
performance [36, 45, 46]. For instance, tool-use performance may degrade substantially when too many tools are
included in the prompt. This implies that systems like ChemCrow[33] and CoScientists[32]both of which present all
the available tools to the model at once-may face scalability issues. To address this, and in addition to the benchmark
introduced in the previous section, we conduct another benchmark to compare our agent-based translation method
with long prompt-based methods.
In the benchmark, to evaluate the ability of models to handle long inputs, we inserted the descriptions of each of
the 17 experiments twice with a random order, resulting in inputs totaling around 11,000 tokensexceeding the input
limits of many LLMs such as GPT-4 (first release) and LLaMA-3-70B. For a fair comparison, we set the number
of agents recalled during each translation to nine, meaning that nine translation agents were activated whenever an

22
instruction needed to be translated. The results, shown in Figure 7, indicate that long-context methods can perform
well in many cases; for instance, both GPT-4o and Gemini 1.5 Pro achieved high translation accuracy. However,
this high performance is not consistent across all models. For example, Claude 3 Opus exhibited a notable decline
in instruction-following ability with longer inputs, leading to poor translation results. In contrast, even when only a
subset of translation agents is activated, these agents can still outperform their long-context counterparts. Our result
shows that activiating more translation agents can provide better accuracy than inputting all the tools to LLMs.
0.5
0.6
0.7
0.8
0.9
1.0
93.33%
93.75%
95.42%
96.25%
97.08%
97.92%
97.92%
98.75%
99.17%
Claude-3-Opus (LongContext)
GPT-4o-Mini (LongContext)
Llama-3-70B (Agents)
GPT-4o-Mini (Agents)
Gemini-1.5-Pro (LongContext)
Gemini-1.5-Pro (Agents)
GPT-4o (LongContext)
Claude-3-Opus (Agents)
GPT-4o (Agents)
Translation accuracy
Figure 7: Comparison of translation success rates using a long context versus our agent-based approach. Long
context were found to significantly reduce translation accuracy under certain conditions, such as in the case of
Claude 3 Opus, highlighting the advantage of our method.
3.
Benchmarking visual inspection
Here, we describe the method for benchmarking the performance of inspection agents to assess their ability to
determine the success of an experiment. The agent has three methods for evaluating success: (1) by reading only the
fitting report generated by human-written code, (2) by analyzing only the figures generated from the experimental
data, or (3) by first analyzing the figures and generating a report, then combining this report with the fitting results
to assess success. These methods are referred to as “Fitting”, “Visual”, and “Combined”, respectively.
It is challenging to precisely define success criteria using natural language for the inspection of plots. To address
this, we employ a few-shot prompting approach. This involves providing the agent with example images of a successful
experiment and a failed experiment, followed by a new image. The agent is asked to determine whether the new image
more closely resembles the successful or failed example, with some guidance from natural language descriptions.
The benchmarking dataset consists of four typical experimental results representing common types of plots in
quantum computing experiments.
To evaluate the agents, we specifically crafted a synthetic dataset where it is
difficult to assess success based solely on fitting resultshighlighting the need for language model assistance. Each
experiment produces 100 successful and 100 failed examples, and the agent is tasked with determining whether each
experiment is successful or not. Detailed prompts and reference images are provided below.
a.
Rabi experiment
The rabi experiment represents a set of examples where we expect to observe a set of oscilla-
tions. To observe these oscillations, we do a Fourier transform of the input data and plot its spectrum for the LLMs
to determine its correctness. Benchmark one sample of this experiment costs on average 6,056 input tokens and 1,220
output tokens.

23
Examples of the instructions for NormalisedRabi
Analyze
this
quantum
mechanics
Rabi
oscillation
experiment
plot in the
Fourier
frequency
domain. A
successful
experiment
should
have a significant
peak in the
figure.
For
example , the
following
Image is a successful
Rabi
oscillation
experiment
plot:
the
following
Image is a failure
case
for the
Rabi
experiment :
b.
Resonator spectroscopy
The resonator spectroscopy experiment involves looking for a resonator feature in a
1D space. The failure example observes noise and cannot find a clear resonator. Benchmark one sample of this
experiment costs on average 6,886 input tokens and 1,365 output tokens.
Examples of the instructions for ResonatorSpectroscopy
Analyze
the
resonator
spectroscopy
magnitude
plot to
determine
if it
exhibits
characteristics
indicative
of
a resonator.
Specifically , look
for a sharp
dip or peak in the plot , which
would
signal
the
presence
of a resonator.
The
rest of the
plot
should
remain
relatively
stable , without
significant
fluctuations .
Provide a detailed
analysis
of the
magnitude
and
frequency
data. Identifying a resonator
indicates a
successful
experiment.
For
example , the
following
Image is a successful
experiment
plot:
the
following
Image is a failure
case
for the
experiment:

24
c.
Qubit Readout with Gaussian Mixture model
The experiment visualizes the integrated readout signal on the
IQ plane. Typically, the effectiveness of a Gaussian mixture model can be assessed using a spherical Gaussian mixture
model (where the covariance matrix is diagonal) by examining the signal-to-noise ratio (SNR), which is the distance
between the Gaussian centers divided by the average standard deviation of the two distributions.
However, this
approach becomes less effective when there are more than two clusters in the response signal, which can occur if the
resonator is overdriven or the driving frequency excites higher energy states. In such cases, using the SNR as a metric
for model accuracy is not straightforward. In this synthetic dataset, we introduce scenarios where higher excited
states may exhibit small leakage or significant population. Describing such complex criteria in natural language also
poses challenges. Benchmark one sample of this experiment costs on average 7,840 input tokens and 1,857 output
tokens.
Examples of the instructions for Gaussian Mixture Model readout
Analyze a plot of
collected
signal
data to
determine
experiment
success:
1.
Identify
clusters: The
signal
represents
hidden
system
states , with
each
state
generating a 2D Gaussian
distribution (spherical
blobs).
2. Count
and
evaluate
distributions :
- Treat
partially
overlapped
clusters
with
two
visible
density
centers
as
separate
distributions .
- Consider
elliptical
distributions
with
only
one
visible
density
center as a single
distribution .
- Compare
densities
of
observed
distributions .
- If three or more
distributions
are
present , but
only
two
have
major
density , consider
only
the two
high -density
distributions
and
ignore
the low -density
ones.
3.
Experiment
outcome:
- Success: Exactly
two
major
distributions
observed (after
accounting
for
density).
- Failure: Any
other
outcome (e.g., one
distribution , or more
than
two
major
distributions ).
For
example , the
following
Image is a successful
experiment
plot:
the
following
Image is a failure
case
for the
experiment:

25
d.
DRAG experiment
The goal of the DRAG experiment calibration is to identify the intersection point of two
lines. We synthesize a dataset where the fitting process will always predict a crossing point between the blue and
red lines, though the data may be too noisy to be reliable. The language model is designed to assess whether the
input data from the experiment is valid and whether the fitting result can be trusted. Benchmark one sample of this
experiment costs on average 7,899 input tokens and 1,980 output tokens.
Examples of the instructions for DRAG
Analyze
the
scatter
plot
with
blue
and red
data
points
and
trend
lines:
1. Compare
the
slopes
of the
trend
lines.
2. Assess
how
well
data
points
fit
their
trend
lines , noting
outliers
or
patterns.
3. Evaluate
data
point
distribution
along
the
DRAG
coefficient
axis.
4. Determine
if trend
lines
accurately
represent
their
datasets.
5. Compare
trends
between
the two
datasets.
6. Estimate
the
fitting
residuals.
Success
criteria:
1. Distinct
trends
for
each
color
2. Appropriate
line
fitting , with
the
blue
and red
lines
has
significant
difference
in
distribution .
3. Lines
intersect
near
the plot ’s center
region , small
shifts
away
from
the
center is
acceptable .
4.
Residuals
are
within
acceptable
range.
If
criteria
aren ’t met , mark
the
experiment
as
failed
and
suggest a new
range
for the
sweep.
For
example , the
following
Image is a successful
experiment
plot:
the
following
Image is a failure
case
for the
experiment:
We additionally note that the Llama-3-70B+LLaVA-v1.6-34B setup in the figure uses the Llama 3 70B model [13]
when there is no image involved. When inspecting a figure, we adopt an LLaVA 1.6 model [14, 15] using the Nous-
Hermes-2-Yi-34B model [79] as its base model. As LLaVA 1.6 does not support including multiple images in the

26
conversation, we only demonstrate its performance with the zero-shot prompt for visual inspection.
Appendix D: Built-in experiments
Here we detail the implementation of the built-in experiments for single qubit calibration and provide details on
how the language model gets prompted. These experiments are standard for superconducting quantum processor
calibration, please refer to [49] for more details. For the two-qubit gate related built-in experiments, please refer to
appendix E.
a.
Ramsey experiment
The Ramsey experiment measures the qubit frequency and coherence time of a qubit by
applying two 𝜋/2 pulses separated by a free evolution period, during which the qubit’s phase oscillation reflects the
offset between the driving frequency and the qubit frequency.
Ramsey experiment example
Execution agent (input): Conduct the Ramsey experiment with parameters ”frequency offset=0.1 MHz”,
”stop time=35 microseconds”, ”step size=0.5 microseconds”.
Code translation agent (output):
experiment_ramsey = SimpleRamseyMultilevel (dut=dut , set_offset =0.1 , stop =35, step =0.5)
Experiment plot (input):
Fitting (input): The Ramsey experiment for qubit Q1 has been analyzed. The expected offset was set to
0.100 MHz, and the measured oscillation is 0.102+/-0.000 MHz. Oscillation amplitude is 0.599+/-0.019. The
number of oscillations is 3.562+/-0.011.
Visual inspection agent (output): The plot shows data from a quantum mechanics experiment involving
Ramsey oscillations. The data points exhibit a clear, regular oscillatory pattern, indicating successful oscil-
lations. The fit line closely follows the data points throughout the plot, suggesting a good fit quality. The
data points are relatively tightly clustered around the fit line, with some minor dispersion. The amplitude
of the oscillations is around 0.8, which is close to the ideal value of 1, and the frequency is approximately
0.10176 MHz, which is within the expected range. Overall, the plot demonstrates the typical characteristics
of a successful Ramsey oscillation experiment, with clear oscillations, a good fit, and consistent amplitude and
frequency.
Final analysis (output): The Ramsey experiment for qubit Q1 was successful. The plot shows a clear,
regular oscillatory pattern with a good fit. The amplitude of the oscillations is 0.599, which is slightly lower

27
than the ideal value of 1 but still within an acceptable range. The frequency of the oscillations is 0.102 MHz,
which is very close to the expected offset of 0.100 MHz. The number of oscillations observed is 3.562, which
is within the acceptable range (greater than 3 and less than 10).
Execution Agent (output): The results from the experiment indicate that the Ramsey experiment was
successful. The plot shows a clear oscillatory pattern with a good fit, and the final analysis confirms that
the frequency and amplitude are within acceptable ranges. The experiment success flag is also set to True,
meaning the experiment was successful. Therefore, based on the rules, the next state should be ’Complete’.
b.
Rabi experiment
The Rabi experiment involves driving a qubit with an external electromagnetic pulse on
resonance to the qubit frequency, to induce transitions between its quantum states. The oscillation speed of the
experiment can be used to infer the rough optimal single-qubit gate pulse amplitude.
Rabi experiment example
Execution agent (input): Conduct the Rabi experiment to determine the Rabi rate for rough amplitude
calibration.
Code translation agent (output):
rabi_experiment = NormalisedRabi (dut_qubit=dut , amp =0.2 ,
start =0.01 ,
stop =0.3 , step =0.002 ,
fit=True ,
collection_name =’f01 ’, mprim_index =0,
pulse_discretization =True , update=True)
Experiment plot (input):
Fitting (input): The fitting result of the Rabi oscillation suggests the amplitude of 0.5893195663534404,
the frequency of 17.602131636706986, the phase of 1.5439919053018119. The offset of 0.2087721909927606.
The suggested new driving amplitude is 0.19815270673482663.From the fitting results, the plot should exhibit
5.104618174645026 oscillations.
Visual inspection agent (output): The plot shows data points that exhibit a clear, regular oscillatory
pattern, indicative of Rabi oscillations. The amplitude of the oscillations appears consistent, with peaks and
troughs occurring at regular intervals. The frequency of the oscillations also seems stable throughout the time
range. Overall, the plot demonstrates the typical characteristics of successful Rabi oscillation experiments,
with well-defined oscillations and consistent amplitude and frequency.

28
Final analysis (output): The experiment was successful. The plot shows a clear, regular oscillatory pattern
with consistent amplitude and frequency, which is characteristic of a successful Rabi oscillation experiment.
The fitting results suggest an amplitude of 0.5893, a frequency of 17.6021, and a phase of 1.5440. The plot
should exhibit approximately 5.1 oscillations, which is within the acceptable range of 5 oscillations.
Execution Agent (output): Transitioning to the next stage Stage2 with the following description: Conduct
the Pingpong experiment. The experiment was successful based on the results provided. The plot shows a
clear, regular oscillatory pattern with consistent amplitude and frequency, which is characteristic of a successful
Rabi oscillation experiment. The fitting results are consistent with the plot, and the final analysis confirms the
success of the experiment. Since the experiment was successful, the next stage should be Stage2 (Pingpong
Experiment) as per the rules.
c.
Pingpong experiment
The ping-pong experiment repeatedly applies sequences of quantum gates to estimate
the precise amplitude of the single-qubit drive pulse.
Pingpong experiment example
Execution agent (input): Conduct the Pingpong experiment.
Code translation agent (output):
experiment_pingpong = AmpPingpongCalibrationSingleQubitMultilevel (dut=dut , iteration =9, points =10,
mprim_index =0,
repeated_gate =’X’, flip_other =False , ai_inspection =True)
Experiment plot (input):
Visual inspection agent (output): The amplitude plot shows a decreasing trend initially, followed by a
stabilization around the 5th iteration. This indicates that the amplitude converges through the iterations, as
the values become relatively constant after the initial decrease.
Final analysis (output): The amplitude plot shows a decreasing trend initially, followed by stabilization
around the 5th iteration, indicating that the amplitude converges through the iterations. This suggests that
the experiment was successful in achieving fine calibration of the single qubit pulses.

29
Execution Agent (output): The results from both the plot and Final analysis indicate that the amplitude
converges and stabilizes around the 5th iteration, which suggests that the experiment was successful in achieving
fine calibration of the single qubit pulses. Additionally, the ’Experiment success’ result is marked as True,
confirming that the experiment was successful.
Therefore, based on the rules, the next stage should be
’Complete’ as the experiment has been successful.
d.
DRAG calibration experiment
The DRAG (Derivative Removal by Adiabatic Gate) calibration experiment we
used in this experiment reduces phase errors during gate operations by sweeping the DRAG parameter of the pulse.
DRAG experiment example
Execution agent (input): Conduct the DRAG calibration on the single qubit gate.
Code translation agent (output):
experiment_drag = DragCalibrationSingleQubitMultilevel (dut=dut , collection_name =’f01 ’, mprim_index =0,
initial_lpb=None , N=1, num =21)
Experiment plot (input):
Fitting (input): Sweep start: -0.009333333333333334 Sweep stop: 0.0026666666666666666 The fitting results
are as follows: The estimated optimal DRAG coefficient is -0.0061392677674084704 The estimated optimal
DRAG coefficient falls within the central half of the sweep.Residual average for Xp: 0.0023451666048237476,
Residual average for Xm: 0.0012794699649556793
Visual inspection agent (output): 1. The slope of the blue trend line is positive, indicating an increasing
trend, while the slope of the red trend line is negative, indicating a decreasing trend. 2. The data points for
both colors generally fit their respective trend lines, though there are a few outliers, particularly among the
red data points. 3. The data points are distributed along the DRAG coefficient axis, with blue points more
concentrated on the right side and red points more concentrated on the left side. 4. The trend lines appear to
accurately represent their datasets, capturing the overall direction of the data points. 5. The trends between
the two datasets are distinct, with one increasing and the other decreasing. 6. The fitting residuals seem to
be within an acceptable range, though there are some deviations, particularly among the red data points.

30
Final analysis (output): The experiment shows distinct trends between the two datasets, with the blue
trend line increasing and the red trend line decreasing. The fitting residuals are within an acceptable range,
although there are some deviations, particularly among the red data points. The estimated optimal DRAG
coefficient is -0.0061, which falls within the central half of the sweep range, indicating that the sweep was
appropriately centered. Overall, the experiment meets the success criteria.
Execution Agent (output): The experiment has been successful based on the results provided. The final
analysis confirms that the experiment meets the success criteria, with the estimated optimal DRAG coeffi-
cient falling within the central half of the sweep range and the residuals being within an acceptable range.
Additionally, the ’Experiment success’ result is marked as ’True’, indicating no need for further retries or
adjustments.
e.
Randomized benchmarking experiment
The randomized benchmarking experiment evaluates the error rates of
quantum gates by applying a sequence of random gate operations followed by their inverse, measuring how well the
system returns to its initial state [80–82].
Randomized benchmarking example
Execution agent (input): Measure the single qubit gate fidelity using randomized benchmarking.
Code translation agent (output):
experiment_rb = SingleQubitRandomizedBenchmarking (dut=dut , collection_name =’f01 ’, seq_length =1024 ,
kinds
=10,
cliff_set=’XY’, pi_half_only =False , mprim_index =0, seed =42)
Experiment plot (input):
Fitting (input): The randomized benchmarking experiment suggest the infidelity per clifford is 0.00240+/-
0.00023 and the infidelity per gate is 0.00131+/-0.00013.
Visual inspection agent (output): The plot shows the population of the |0⟩state (blue) and |1⟩state (red)
as a function of sequence length in a randomized benchmarking experiment. The |0⟩state exhibits a clear
exponential decay, indicating that the experiment is successful. The decay rate appears to be neither too fast
nor too slow, suggesting that the sequence length is appropriate.

31
Final analysis (output): The experiment shows a clear exponential decay in the population of the |0⟩state,
indicating that the experiment is successful. The infidelity per Clifford and per gate are within reasonable
physical limits, suggesting that the experiment was conducted properly.
Execution Agent (output): The results from the experiment indicate a successful measurement. The plot
shows a clear exponential decay in the population of the |0⟩state, which is consistent with the expected
behavior in a randomized benchmarking experiment.
The infidelity per Clifford and per gate are within
reasonable physical limits, and there are no suggested parameter updates. Additionally, the final analysis
confirms that the experiment was successful, and the ’Experiment success’ flag is set to True. Therefore, the
fidelity measurement is successful, and the next stage should be ’Complete’.
Appendix E: Two-qubit siZZle gate
The siZZle gate (Stark-induced ZZ by level excursions) is one method to implement two-qubit interactions on fixed-
frequency transmon qubits [68–71]. The siZZle gate off-resonantly drives two qubits, inducing a shift in the energy
levels of the two-qubit system, which modifies the ZZ interaction. An approximate formula for the ZZ interaction
rate, denoted as ˜𝜈𝑍𝑍, is [70]:
˜𝜈𝑍𝑍= 𝜈𝑍𝑍,𝑠+
2𝐽𝛼0𝛼1Ω0Ω1 cos(𝜙0 −𝜙1)
Δ0,𝑑Δ1,𝑑(Δ0,𝑑+ 𝛼0)(Δ1,𝑑+ 𝛼1)
(E1)
where 𝜈𝑍𝑍,𝑠is the static ZZ interaction rate without any applied drives. 𝛼0 and 𝛼1 represent the anharmonicity
of the two qubits. Δ0,𝑑and Δ1,𝑑are the detunings of the driving frequencies relative to the transition frequencies of
the two qubits. 𝜙0 −𝜙1 is the relative phase between the two drives applied to the qubits. 𝐽denotes the capacitive
coupling strength between the qubits, while Ω0 and Ω1 are the driving amplitudes of the pulses applied to each qubit.
To calibrate a siZZle gate, the objective is to find the optimal method to drive the two qubits such that the
accumulation of the 𝑍𝑍interaction over time is precisely 𝜋/4. This involves adjusting the driving frequency, which
determines Δ0,𝑑and Δ1,𝑑, the driving amplitude (which sets Ω0 and Ω1), and the driving time. Since the ZZ interaction
is proportional to Ω0Ω1, we typically choose Ω0 = Ω1 in experiments to maximize the ZZ interaction. However, this
does not imply that the amplitudes are exactly the same, as variations in cable attenuations and microwave component
performance can cause discrepancies. Therefore, to reproduce the above behavior, we request the agent modify the
drive amplitude of the first qubit, while our code infers the amplitude for the second qubit based on previous calibration
results of single-qubit gates. In the formula, the relative phase of the two drives, 𝜙0 −𝜙1, is also significant. Due to
the experimental setup, the phase reaching the qubits may differ from the phase difference sent by the electronics. In
our experiment, we found that our phase was close to the optimal value, so we did not optimize this parameter.
The pulse sequence for implementing a siZZle gate is shown in figure 8(a). Typically, in the manual calibration
approach, a human scientist selects a pair of driving frequency and amplitude of the Stark drive and then observes the
stability of the quantum system. The stability is observed by implementing the Hamiltoniain tomography experiment
followed by repeated gate tomography experiment, shown in figure 8(b) and (c), respectively. If the chosen parameters
are not optimal, the oscillation of the expectation value of the quantum state tends to be chaotic and noisy. The
scientist then reviews the experimental results and, based on empirical knowledge, suggests a new set of parameters
to test. This iterative process is often the most time-consuming aspect of tuning a two-qubit gate. Once a stable and
clear result is observedindicating that the quantum system’s dynamics are behaving as expected, an automated code
can be employed to determine the necessary time duration, which is the final parameter required to execute the gate.
To provide the human evaluator with an intuitive understanding of the agent’s exploration behavior, we perform a
grid scan over the domain of frequency and amplitude, gathering information related to the ZZ interaction strength.
While the ideal approach would be directly measuring the interaction strength at each point, this is impractical and
too time-consuming. Instead, we employ the pulse sequence shown in figure 8(b), where the duration of the Stark
drive pulse is fixed at 1𝜇𝑠, and we measure the difference in the expectation value when 𝑄1 is prepared to the ground
and excited state. The entire experiment takes approximately 12 hours to generate the background figure.
An example of the search iteration on the real hardware is shown as follows. The inspection agent only inspects
the control qubit state plot and the Fourier transform of the phase oscillation. The other plots are for humans to
evaluate the experiment result.

32
Figure 8: Pulse sequences for calibrating the siZZle gate. (a) The pulse sequence used to implement a single siZZle
gate consists of two off-resonance drives to induce a Stark shift (the Stark drive), followed by single-qubit 𝜋pulses
inserted between and at the end of the drive. These 𝜋pulses are used to cancel the single qubit phase accumulated
on individual qubits. (b) The experimental pulse sequence for Hamiltonian tomography to measure the ZZ
interaction strength. In this experiment, the pulse width is varied to observe the oscillatory behavior in the phase of
the second qubit, which allows inference of the ZZ interaction strength. The dashed line on the pulse for 𝑄1
indicates that the experiment is performed both with and without preparing 𝑄1 in the excited state. (c) Repeated
gate tomography experiment. Unlike Hamiltonian tomography, this experiment uses discrete pulses rather than
continuously sweeping the width of the Stark pulse. This approach offers more precise calibration of the
accumulated ZZ interaction over one repetition block, which can then be used to implement an entangling gate.
siZZle gate parameter search
Parameter agent: Since no experiments have been run yet, we should start by trying a frequency between
the two qubits, which is around 4858 MHz. We can start with a gentle amplitude of 0.2 for the control qubit,
which is close to its single qubit gate amplitude. The other parameters are set based on the given rules.
params: {’frequency’: 4858.0, ’amp control’: 0.2, ’amp target’: 0.0, ’rise’: 0.015, ’width’: 0.1, ’phase diff’:
0.0, ’zz interaction positive’: True}
Translation agent:
experiment_conditional_stark_shift_continuous = ConditionalStarkShiftContinuous (qubits=duts , frequency
=4858.0 ,
amp_control =0.2 ,
amp_target =0.09943319110052375 ,
rise =0.015 ,
start =0, stop =20,
sweep_points
=40,
phase_diff =0.0 , echo=True)
Experiment plots:

33
Inspection agent: The experiment failed due to the Fourier transform plot showing no clear symmetric peaks
around the center frequency for the ground and excited states, indicating unsuccessful measurement of IZ and
ZZ interactions.
Parameter agent: The previous experiment failed because the frequency was too close to the qubits’ fre-
quencies. We should try a frequency further away from the qubits. Let’s start with a frequency below the

34
lowest qubit frequency and a gentle control amplitude.
params: {’frequency ’: 4800.0 , ’amp_control ’: 0.2, ’amp_target ’: 0.09776666514167257 ,
’rise ’: 0.015 , ’width ’
: 1.1730133547479822 ,
’phase_diff ’: 0.0, ’zz_interaction_positive ’: True}
Translation agent::
experiment_conditional_stark_shift_continuous = ConditionalStarkShiftContinuous (qubits=duts , frequency
=4858.0 ,
amp_control =0.2 ,
amp_target =0.09943319110052375 ,
rise =0.015 ,
start =0, stop =20, sweep\
_points =40,
phase_diff =0.0 , echo=True)
Experiment plots:

35
Inspection agent: The experiment was successful based on the clear, symmetric peaks in the Fourier plot,
stable control qubit expectation value, and reasonable fitting results showing a ZZ interaction strength of
0.16543846027754651 MHz.
Translation agent:
experiment_result = ConditionalStarkShiftRepeatedGate (duts=duts , frequency =4800.0 ,
amp_control =0.2 ,
amp_target =0.09943319110052375 ,
rise =0.015 ,
start_gate_number =0, gate_count =32, width
=0.3778425958178225 ,
phase_diff =0.0 , echo=True)
Experiment plots:

36
Inspection agent: The data inspection AI reports that the Fourier transform plot shows two clear, symmetric
peaks for the ground and excited states, and the expectation value of the control qubit along the Z axis remains
stable throughout the experiment. The minimum difference between the ground and excited states is greater
than 25% of the maximum difference, indicating a successful experiment. The fitting results estimate the ZZ
interaction strength to be -0.1170390305626309 MHz, which is a reasonable and physical value. Both the data
inspection and fitting results suggest that the experiment was successful.
Appendix F: Experimental Hardware and Setup
The quantum device contains 16 transmon qubits in 3D-integrated coaxial circuit quantum electrodynamics (cQED)
architecture [65–67]. The details of this device has been reported in [64]. Each qubit consists of a Josephson junction
(JJ) and a readout resonator positioned on opposite sides of the chip, enabling precise couplings to off-chip coaxial
ports for control and readout. The qubits are arranged in a 4 × 4 lattice and are statically coupled through capacitive
elements, facilitating interactions characterized by exchange energy rates (𝐽) between each pair of qubits. The layout
of the chip, depicted in Figure 9(a), illustrates the positioning of the three qubits used in this work.
The basic characterization of the three selected qubits is detailed in Table I. These qubits operate in the straddling
regime, that is, detuning frequencies smaller than the average anharmonicity (⟨𝛼⟩= 196.4 MHz) across the device.
This ensures that most qubits remain within a regime where their interactions can be effectively controlled and utilized
to drive two-qubit gates [80–82].
Table I: Basic characterization of the three qubits used in this work. 𝑄int is the internal Q factor of the resonator,
𝜅ext is the external decay rate of the resonator, and F is single-qubit gate fidelity by randomized benchmarking,
where all Clifford gates are decomposed into physical X and Y gates.
Qubit 𝜔𝑞/2𝜋𝜔𝑟/2𝜋
𝑄int
𝜅ext/2𝜋𝜒/2𝜋𝛼/2𝜋
𝑇1
𝑇2𝑅
𝑇2𝐸
F
𝐽𝑄1−𝑄2 𝐽𝑄1−𝑄8
GHz
GHz
104
MHz
kHz MHz
𝜇s
𝜇s
𝜇s
%
MHz
𝑄1
4.888
9.997 11.661
2.645
-200 -197 126 (18) 107 (12) 124 (23) 99.993
0.760
-
𝑄2
4.795
9.386 11.785
1.337
-225 -197
89 (13)
56 (15)
86 (12) 99.861
0.702
𝑄8
4.829
9.908
5.843
2.040
-175 -197
63 (8)
32 (7)
71 (8)
99.944
-

37
(a)
(b)
Figure 9: (a) The photo of the superconducting quantum processor chip used in this experiment. The three qubits
involved in this experiment are highlighted in green color. (b) The photo of the hardware setup in the lab.
The experimental setup operates at a base temperature of approximately 15 mK using a 3He/4He dilution refrig-
erator. The control and readout of qubits are facilitated by the wiring configurations shown in Figure 10. For qubit
control, microwave pulses are synthesized directly using the QubiC system [4]. See Figure 9(b) for the lab photo. The
pulses are carefully shaped for single and two-qubit gates to align at the desired frequencies. For readout, reflected
signals from the resonators undergo amplification and down-conversion and are then captured by Analog-to-Digital
Converters (ADCs) connected to the FPGA for measurements and further data analysis.
Figure 10: Schematic diagrams of the full experimental setup, including wiring and cryogenic components.
