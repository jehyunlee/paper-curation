# arXiv:2508.07035v1[cond-mat.mtrl-sci]9 Aug 2025

### VASPilot: MCP-Facilitated Multi-Agent Intelligence for Autonomous VASP Simulations

Jiaxuan Liu,1, 2 Tiannian Zhu,1, 2 Caiyuan Ye,1, 2 Zhong Fang,1, 2, 3 Hongming Weng,1, 2, 3, ∗ and Quansheng Wu1, 2, †

1Beijing National Laboratory for Condensed Matter Physics and Institute of Physics, Chinese Academy of Sciences, Beijing 100190, China 2University of Chinese Academy of Sciences, Beijing 100049, China 3Songshan Lake Materials Laboratory, Dongguan, Guangdong 523808, China (Dated: August 12, 2025)

Density-functional-theory (DFT) simulations with the Vienna Ab initio Simulation Package (VASP) are indispensable in computational materials science but often require extensive manual setup, monitoring, and postprocessing. Here, we introduce VASPilot, an open-source platform that fully automates VASP workflows via a multi-agent architecture built on the CrewAI framework and a standardized Model Context Protocol (MCP). VASPilot’s agent suite handles every stage of a VASP study-from retrieving crystal structures and generating input files to submitting Slurm jobs, parsing error messages, and dynamically adjusting parameters for seamless restarts. A lightweight Flask-based web interface provides intuitive task submission, real-time progress tracking, and drilldown access to execution logs, structure visualizations, and plots. We validate VASPilot on both routine and advanced benchmarks: automated band-structure and density-of-states calculations (including on-the-fly symmetry corrections), plane-wave cutoff convergence tests, lattice-constant optimizations with various van der Waals corrections, and cross-material band-gap comparisons for transition-metal dichalcogenides. In all cases, VASPilot completed the missions reliably and without manual intervention. Moreover, its modular design allows easy extension to other DFT codes simply by deploying the appropriate MCP server. By offloading technical overhead, VASPilot enables researchers to focus on scientific discovery and accelerates high-throughput computational materials research.

##### I. INTRODUCTION

With the advancement of computer hardware and algorithm, density functional theory (DFT) calculations have become one of the most important research tools in materials science, chemistry, and condensed matter physics. Starting from quantum mechanics, DFT can predict the mechanical, electromagnetic, and optical properties of materials, playing a crucial role in areas such as batteries[1–3], topological phenomena[4–6] and transport[7–9].

Researchers have developed numerous DFT software packages based on different basis sets and treatments of core electrons. For example, Vienna Ab initio Simulation Package (VASP)[10], Quantum Espresso[11, 12], and CASTEP[13] employ plane-wave basis sets, while OpenMX[14, 15] and Siesta[16] are based on atomic orbital basis sets. Additionally, there are codes like WIEN2k[17] and Elk[18] that utilize all-electron wavefunctions in calculations. Although these software are widely used in various research fields, researchers still need to invest considerable effort in the complicated workflow of these software.

VASPKIT[19], ASE[20], and Pymatgen[21] have alleviated this pain point to a certain extent. VASPKIT is a command-line-based software that can quickly generate corresponding input files for calculations based on crystal

∗ hmweng@iphy.ac.cn † quansheng.wu@iphy.ac.cn

structures upon user’s command. Moreover, it facilitates rapid plotting using predefined templates after the computations are completed. ASE is a Python-based molecular dynamics simulation software that integrates interfaces with various DFT packages such as VASP, Quantum Espresso, CASTEP, and Siesta. By writing Python scripts, researchers can efficiently conduct Density Functional Theory (DFT) calculations. Furthermore, ASE supports interfaces with machine learning interatomic potentials software like DeepMD[22], NequIP[23], and CHGNET[24]. This capability enables rapid and accurate predictions of mechanical properties, bridging the gap between traditional DFT calculations and large-scale atomistic simulations. Pymatgen is a Python-based highthroughput computational materials science library with extensive interfaces for VASP. Through tailored Python scripting, researchers can efficiently prepare input files and seamlessly import calculation results into Python for data analysis and visualization.

These robust interfaces have made high-throughput Density Functional Theory (DFT) calculations a practical reality. For repetitive tasks, these tools, when used in conjunction with custom scripts, can drastically cut down on redundant work. However, in practical research scenarios, scientists often encounter far more intricate challenges. They may need to analyze certain properties across different materials or compare the behavior of a single material under varying conditions and parameters. Such diverse and complex computational tasks demand not only the preparation of various input files tailored to each specific case but also the repetitive submission

of jobs and waiting for their completion. This process can be time-consuming and labor-intensive, highlighting the necessity for further advancements in automation and integration within computational workflows. Automatic execution and management of these tasks will allow researchers to focus more on scientific discovery rather than on the fussy details of computation.

In recent years, the rapid advancement of large language models (LLMs)[25–30] and agent-based technologies has opened new possibilities for building automatic DFT calculation schema. Large language models are deep neural networks pretrained on vast amounts of general textual corpora and further fine-tuned on dialogue data, enabling them to emulate human-like language understanding and reasoning to a significant extent. LLMs have been applied to research in chemistry and material science. Some use LLMs as predictive model to predict the synthesizability of crystal structures[31, 32] and other properties. Others utilize LLM to extract data from articles[33, 34]. There is also research to fine-tune LLM on data of domain-specific data[35].

Based on conversational capabilities, LLM developers have incorporated structured input-output formats into the fine-tuning process, equipping these models with the ability to invoke external programs. This ability is known as function calling or tool use. As LLMs continue to improve in performance, agent systems augmenting LLMs by tools and context have attracted wide attention. These systems not only provide more accurate responses but also gain the ability to interact with computational tools and environments.

Due to the accumulation of lengthy context from multiple tool invocations, single-agent systems often struggle to maintain optimal performance when executing complex, multistep tasks. To address this limitation, multiagent frameworks such as MetaGPT[36], LangGraph[37], and CrewAI[38] have emerged as preferred solutions for managing complex workflows. These frameworks decompose intricate tasks into a series of simpler subtasks, which are then assigned to specialized agents equipped with distinct tools, domain knowledge, and independent contextual states. By enabling coordinated execution, such frameworks achieve improved robustness and scalability, empowering LLMs to effectively handle complex scientific computing tasks. In this way, multi agent systems have potentials to become an AI coworker of human researchers.

There have been some successful attempts to leverage LLM-based multi-agent frameworks (MAF) to assist materials research. For instance, AtomAgents[39] aims to automate alloy design by integrating a knowledge base with LAMMPS[40]-based molecular dynamics simulation tools. TopoMAS[41] accelerates the discovery and investigation of topological materials by combining literature mining, generative models, and VASP calculations. There are attempts such as MatPilot[42] and ChemAgent[43] that leverage robotic arms to oversee and conduct experimental procedures. Moreover, El Agente

Q[44] and DREAMS[45], respectively, explore the MAF on xTB[46] and Quantum Espresso to accelerate DFT computations.

Despite these initial demonstrations for multi-agent frameworks (MAFs) to contribute to chemistry and materials science research, several challenges remain to be addressed for their effective use in facilitating practical computations. Firstly, beyond routine tasks like band structure and DOS calculations, MAFs should also handle complex tasks without task-specific examples to maximize its adaptability. Secondly, although MAFs can expedite research processes, the role of human scientists remains indispensable. Consequently, the user interface is crucial. Scientists need real-time, intuitive understanding of the status of MAF to ensure the validity and correctness of results. Lastly, while VASP software boasts a substantial user base within the field of condensed matter physics, there has been a notable lack of focus on developing MAFs specifically tailored for VASP, indicating an area ripe for further exploration and development.

To bridge these gaps, in this work, we introduce an open source software, VASPilot. VASPilot leverages the CrewAI framework for multi-agent cooperation, facilitating automated DFT calculation and visualization for more complicated misssions. This tool aims to further simplify the workflow of VASP even for zero-shot mission and practically reduce the researchers’ effort executing VASP calculation.

In the following, we first describe the VASPilot architecture, covering the CrewAI-based multi-agent collaboration core, the Model Context Protocol (MCP) tool server, and the web-based user interface. We then demonstrate VASPilots robustness and versatility through a series of benchmark studies. Finally, we present a concise conclusion and outlook.

Human

![image 1](Liu et al._2025_VASPilot MCP-Facilitated Multi-Agent Intelligence for Autonomous VASP Simulations_images/imageFile1.png)

|Web Server|
|---|


![image 2](Liu et al._2025_VASPilot MCP-Facilitated Multi-Agent Intelligence for Autonomous VASP Simulations_images/imageFile2.png)

structure tools

![image 3](Liu et al._2025_VASPilot MCP-Facilitated Multi-Agent Intelligence for Autonomous VASP Simulations_images/imageFile3.png)

Mission Final Report

serach_MP

###### Agents

||VASP agent|
|---|
<br><br>|Crystal structure agent|
|---|
<br><br>|Result validate agent|
|---|
<br><br>|
|---|


Task & Context

|Manager Agent|
|---|


VASP tools

Agent results

wait_calc

check_calc_results

(CrewAI tool)

Useful Context

|Memory|
|---|


python_plot

Agent results

check_ﬁle_exist

read_calc_results

FIG. 1. Overall stucture of VASPilot. VASPilot consists of three main components: Web server (blue background box), CrewAI based multi agent cooperation core (gray background box) and Model Context Protocol type tool server (yellow backgound box).

VASP Tools

![image 4](Liu et al._2025_VASPilot MCP-Facilitated Multi-Agent Intelligence for Autonomous VASP Simulations_images/imageFile4.png)

II. METHODS

||vasp_relaxation|
|---|
<br><br>|vasp_scf|
|---|
<br><br>|vasp_nscf|
|---|
|
|---|


+

![image 5](Liu et al._2025_VASPilot MCP-Facilitated Multi-Agent Intelligence for Autonomous VASP Simulations_images/imageFile5.png)

A. Overall structure of VASPilot

Input

Slurm job ID Full Data

Client Database

Calculation ID

The VASPilot program is primarily composed of three components: a web-based interface, a multi-agent collaborative core, and a tool server for the agents (Fig. 1). The multi-agent collaboration module is implemented using the CrewAI framework [38], an open-source Python library for constructing cooperative AI agent teams. CrewAI facilitates the automation of complex tasks through modular workflows, role-specific agents, and flexible tool integration. The tool server is encapsulated within the Model Context Protocol (MCP)[47], a standardized interface for tool invocation and data provisioning. By adhering to MCP, our tools can be seamlessly incorporated into other frameworks with minimal additional effort.

Slurm job ID

|check_calc_results|
|---|


Calculation ID

Status & LLM friendly results

Status & Full Results

Calculation ID & Python Code Calculation ID Status & Fig path Full Data

|python_plot|
|---|


![image 6](Liu et al._2025_VASPilot MCP-Facilitated Multi-Agent Intelligence for Autonomous VASP Simulations_images/imageFile6.png)

xxx.png

FIG. 2. Specially tailored tools in VASPilot. VASP tools prepare input files and submits the calculation through pymatgen and slurm. ’check calc results’ check the calculation status, read the results and store full data into database. ’python plot’ reads full calculation data from database and execute the python code given by client.

Within this framework, we deploy one manager agent (orange box in Fig. 1) alongside three specialized worker agents (dashed box in Fig. 1): the Crystal Structure Agent, the VASP Agent, and the Result Validation Agent. In this work, all agents are powered by DeepSeekV3-0324[26], but they can be easily replaced with other LLMs in practice. The Crystal Structure Agent performs crystalstructure searches, manipulations, and analyses. When the user did not specify a certain crystal structure file, the agent will search and download a structure from Materials Project [48]. The VASP Agent orchestrates VASP calculations and produces the corresponding visualizations. The Result Validation Agent evaluates the accuracy and reliability of the computed outcomes.

utilities built on the pymatgen library to manage every stage of the VASP workflow, as shown in Fig. 2.

First, our input-preparation tools (dashed box in Fig. 2) automatically generate all necessary VASP input files and submit jobs to a Slurm scheduler. Each submission is tagged with a unique calculation ID, which, together with its Slurm job number, is recorded in a centralized database. To minimize communication overhead, only the calculation ID is returned to the agent. In the event of a workflow restart (for example, a nonselfconsistent band-structure run), the tool retrieves the relevant metadata and input files by calculation ID, reconstructs the working directory, and resubmits the job seamlessly.

Each worker agent maintains its own independent context and system prompt and can invoke only the subset of MCP-provided tools relevant to its tasks. In the case of the VASP Agent, we supplement the standard VASP-specific MCP tools with a custom CrewAI utility, ’wait calc tool’. This tool periodically polls the MCP server to determine whether ongoing calculations have finished, thereby mitigating potential network timeouts during long-running jobs.

Second, we provide a status-query utility that reports on both failed and successful calculations (check calc results tool in Fig. 2). For failed jobs, the tool returns the VASP error messages; for successful runs, it reads the full result set via pymatgen, archives the data in the database, and extracts a concise summary of key properties (e.g., total energy, band gap, and Fermi energy) for downstream LLM consumption.

When a user submits a mission via the web interface, the manager agent decomposes it into discrete tasks and dispatches each to the appropriate worker agent. Upon completion, each agent returns a detailed execution report to the manager. All outputs are archived in a Retrieval-Augmented Generation (RAG)[49]-based memory pool: as an agent begins a task, it retrieves relevant historical entries to enrich its context and inform its decisions.

Finally, to enable flexible post-processing, we developed a plotting tool that executes clientprovided Python code(python plot tool in Fig. 2). Given a list of calculation IDs and plotting instructions, the tool retrieves the corresponding datasets, runs the plotting code, and returns either the path to the generated image or any error messages encountered. This end-to-end framework offloads heavy I/O from the LLM, guarantees full traceability of every task, and supports reliable, error-tolerant computation and visualization.

B. Tools and Model Context Protocol Server

In agentic LLM systems, tool design plays a pivotal role in ensuring both efficient performance and robust task execution. Because VASP generates extensive output that exceeds the native I/O capacity of most language models, we have implemented a coherent suite of

C. Intuitive web interface

Although VASPilot automates complex workflows, user oversight remains indispensable to ensure the accuracy of both intermediate steps and final outcomes. To

## (a) (b)

![image 7](Liu et al._2025_VASPilot MCP-Facilitated Multi-Agent Intelligence for Autonomous VASP Simulations_images/imageFile7.png)

|| |
|---|
<br><br>|
|---|


![image 8](Liu et al._2025_VASPilot MCP-Facilitated Multi-Agent Intelligence for Autonomous VASP Simulations_images/imageFile8.png)

| |
|---|


| |
|---|


|![image 9](Liu et al._2025_VASPilot MCP-Facilitated Multi-Agent Intelligence for Autonomous VASP Simulations_images/imageFile9.png)<br><br>| |
|---|
<br><br>|![image 10](Liu et al._2025_VASPilot MCP-Facilitated Multi-Agent Intelligence for Autonomous VASP Simulations_images/imageFile10.png)|
|---|
<br><br>|
|---|


| |
|---|


| |
|---|


- FIG. 3. Web user interface of VASPilot. (a), The overview of the web user interface. By clicking the mission record in green box, the detail of mission will be shown on the right. The yellow box is the real-time workflow of the VASPilot. The blue box is the execution history of agents and tools. The red box is the details of selected execution history. (b), enlarged view of the execution history. The detailed information will be shown when user select an event. In detailed information area, figures and crystal structure files can be immediately shown by clicking the button.


facilitate this interaction, we have developed an intuitive, web-based interface using Python’s Flask framework[50] (Fig. 3).

On the main page, users submit mission directives in natural language via a dedicated input dialog. Directly below this dialog, a chronological history of all previously submitted tasks is presented. By selecting any entry (green box in Fig. 3 (a)), the user is navigated to a detailed task view in which a flowchart (yellow box in Fig. 3 (a)) graphically represents the execution sequence and current status. Beneath the flowchart, expandable ”Agent Execution” and ”Tool Execution” logs (Fig. 3 (b)) provide full visibility into each agent’s and tool’s inputs and outputs. Moreover, within these logs, crystal-structure visualizations and generated plots can be inspected in greater detail via clearly labeled buttons (Marked by gray dashed box in Fig. 3(b)). This design empowers users to both monitor overall progress at a glance and drill down into the computational data for rigorous verification.

##### III. EXAMPLES

To evaluate VASPilots reliability, we performed bandstructure and density-of-states (DOS) calculations for 2H-MoS2, as illustrated in Fig. 4. The workflow began when the Manager Agent instructed the Crystal Structure Agent to supply the crystal structure. This agent automatically retrieved the structure from the Materials Project database [48] using the specified spacegroup. Following task delegation, the VASP Agent sequentially executed structural relaxation and self-consistent field (SCF) calculations by invoking requisite tools. During the initial SCF calculation, VASP returned a Bravais lattice inconsistency error. In response, VASPilot intelligently adjusted the symmetry tolerance parameter, resolving the issue and enabling successful completion of the subsequent SCF calculation. The VASP Agent then performed a non-self-consistent field (NSCF) bandstructure calculation and generated the electronic band structure plot via built-in visualization tools. The Man-

(a) (b)

![image 11](Liu et al._2025_VASPilot MCP-Facilitated Multi-Agent Intelligence for Autonomous VASP Simulations_images/imageFile11.png)

|Calculate the band structure for 2H phase MoS2. Use IVDW=11 in relaxation.|
|---|


Manager agent

|Find and provide the crystal structure of 2H phase MoS2|
|---|


|Perform VASP calculation for band structure of 2H phase MoS2 with IVDW=11 during relaxation|
|---|


|Validate the VASP calculation results for 2H phase MoS2|
|---|


Crystal structure agent VASP agent Result validate agent

serach materials project

VASP relaxation

Read calculation results

(c)

![image 12](Liu et al._2025_VASPilot MCP-Facilitated Multi-Agent Intelligence for Autonomous VASP Simulations_images/imageFile12.png)

Error: inconsistent Bravais lattice types

VASP SCF

mp-1018809.vasp

Check ﬁles exist

adjust symprec

VASP SCF

Completed

|Success|
|---|


VASP NSCF

|Final Report|
|---|


|xxx.png|
|---|


Plot ﬁgures

- FIG. 4. Band structure and density of states calculation of 2H-MoS2 utilizing VASPilot. (a), workflow of band structure calculation. (b), Band structure figure calculated and plotted by VASPilot. (c), Density of states figure calculated and plotted by VASPilot. The workflow of Density of states calculation is almost the same as the band structure calculation.

Use diﬀerent ENCUT (from 300 to 500) to calculate the total energy of 2H phase MoS2.

Calculate and compare the c lattice constant of 2H MoS2 with 12.294 Å (experiment value) using diﬀerent vdW corrections. The settings of diﬀerent vdW functionals are listed below: ….. Plot an intuitve ﬁgure as result.

Calculate and compare the bandgap of MoS2, MoSe2, WS2 and WSe2. Plot an intuitive ﬁgure as result.

![image 13](Liu et al._2025_VASPilot MCP-Facilitated Multi-Agent Intelligence for Autonomous VASP Simulations_images/imageFile13.png)

![image 14](Liu et al._2025_VASPilot MCP-Facilitated Multi-Agent Intelligence for Autonomous VASP Simulations_images/imageFile14.png)

![image 15](Liu et al._2025_VASPilot MCP-Facilitated Multi-Agent Intelligence for Autonomous VASP Simulations_images/imageFile15.png)

VASPilot

- FIG. 5. Prompts and results of three complex missions. The resulting figures are given by VASPilot in its final report. All these missions are finished without examples as context. In the second column, IVDW=10 is the DFT-D2 method of Grimme[51]. IVDW=11 is the DFT-D3 method of Grimme with zero-damping function[52]. IVDW=12 is the DFT-D3 method with BeckeJohnson damping function [53]. IVDW=20 is the Tkatchenko-Scheffler method[54]. optB86[55], optB88[56], SCAN+rVV10[57], r2SCAN+rVV10[58], rVV10[59] and optPBE-vdW[56] are nonlocal vdW corrections.


ager Agent subsequently directed the Result Validation Agent to verify the computational results. Acting autonomously, this agent confirmed the existence of the band structure image and the integrity of the computation using its dedicated validation tools. Finally, the Manager Agent synthesized all the results and compiled a comprehensive task report. The workflow of DOS calculation is almost the same as band structure calculation.

We further evaluated VASPilot’s ability to execute novel, more complex workflows by defining three benchmark scenarios. First, we performed a plane-wave cutoff convergence test by calculating the total energy of 2HMoS2 over a range of ENCUT values from 300 eV to 500 eV. Second, we conducted structural relaxations of 2H-

MoS2 using several van der Waals correction schemes, then compared the optimized lattice constants against experimental measurements. Third, we computed and contrasted the band gaps of the 2H phases of MoS2, MoSe2, WS2, and WSe2. VASPilot successfully completed all three tasks. The detailed prompts and resulting data for these test cases are summarized in Fig. 5.

These case studies underscore VASPilot’s robustness and flexibility. The platform reliably executed standard workflows-such as electronic band-structure and densityof-states calculations-and, upon encountering VASP execution errors, automatically parsed the error messages, adjusted input parameters, and successfully resumed the runs. Moreover, even for complex missions lacking any

contextual examples, VASPilot completed the tasks without intervention. Overall, these results demonstrate that VASPilot is a powerful and adaptable framework for fully automated DFT calculations.

##### IV. CONCLUSIONS

In this work, we have developed VASPilot, an opensource framework for fully automated VASP calculations. Built atop the CrewAI architecture and the Model Context Protocol (MCP), VASPilot seamlessly invokes specialized tools for structure retrieval and manipulation, inputfile generation, Slurm job orchestration, and postprocessing of results. We demonstrated its capability by executing automated band-structure and density-of-states workflows in which VASPilot parsed error messages, adapted input parameters on the fly, and successfully resumed interrupted runs. Beyond standard tasks, VASPilot handled more demanding benchmarks-converging total energies over a range of ENCUT values, optimizing lattice constants under different van der Waals correction schemes, and comparing band gaps across multiple 2H phase transitionmetal dichalcogenides.

These case studies attest to VASPilot’s robustness and adaptability, enabling truly autonomous DFT workflows. Moreover, these capabilities can be readily extended through the integration of additional agents and tools, and the underlying framework can be easily adapted to

other DFT codes by deploying the corresponding MCP server. We anticipate that VASPilot will streamline VASP-based research pipelines, reducing both the technical overhead and turnaround time for complex simulations. More broadly, we hope this work will inspire the development of similar agent-tool ecosystems for other computational platforms, accelerating automation across materials modeling and computational physics.

##### V. DATA AND CODE AVAILABILITY

The VASPilot source code and comprehensive documentation are publicly available under an open-source license on GitHub (https://github.com/JiaxuanLiuArsko/VASPilot), and an interactive demo can be accessed via the MaterialsGalaxy service portal (https://cmpdc.iphy.ac.cn/materialsgalaxy/tools/vaspilot).

##### ACKNOWLEDGMENTS

This work was supported by the Science Center of the National Natural Science Foundation of China (Grant No. 12188101), the National Key R&D Program of China (Grant No. 2023YFA1607400, 2022YFA1403800), the National Natural Science Foundation of China (Grant No.12274436, 11925408, 11921004), and H.W. acoknowledge support from the New Cornerstone Science Foundation through the XPLORER PRIZE.

- [1] R. Xiao, H. Li, and L. Chen, Density functional investigation on li2mno3, Chemistry of Materials 24, 4242 (2012), https://doi.org/10.1021/cm3027219.
- [2] Y. Wang, X. Yu, S. Xu, J. Bai, R. Xiao, Y.-S. Hu, H. Li, X.-Q. Yang, L. Chen, and X. Huang, A zero-strain layered metal oxide as the negative electrode for long-life sodium-ion batteries, Nature Communications 4, 2365

(2013).

- [3] X. Wang, R. Xiao, H. Li, and L. Chen, Oxysulfide LiAlSO: A Lithium Superionic Conductor from First Principles, Physical Review Letters 118, 195901 (2017).
- [4] Y. Jia, J. Yu, J. Liu, J. Herzog-Arbeitman, Z. Qi, H. Pi, N. Regnault, H. Weng, B. A. Bernevig, and Q. Wu, Moir fractional Chern insulators. I. First-principles calculations and continuum models of twisted bilayer MoTe 2, Physical Review B 109, 205121 (2024).
- [5] C. Wang, X.-W. Zhang, X. Liu, Y. He, X. Xu, Y. Ran, T. Cao, and D. Xiao, Fractional Chern Insulator in Twisted Bilayer MoTe 2, Physical Review Letters 132, 036501 (2024).
- [6] T. Devakul, V. Crpel, Y. Zhang, and L. Fu, Magic in twisted transition metal dichalcogenide bilayers, Nature Communications 12, 6730 (2021).
- [7] S. Zhang, Q. Wu, Y. Liu, and O. V. Yazyev, Magnetoresistance from Fermi surface topology, Physical Review B 99, 035142 (2019).


- [8] Z. Liu, S. Zhang, Z. Fang, H. Weng, and Q. Wu, Firstprinciples Methodology for studying magnetotransport in magnetic materials (2024), arXiv:2401.15146 [cond-mat].
- [9] H. Pi, S. Zhang, Y. Xu, Z. Fang, H. Weng, and Q. Wu, First-principles methodology for studying magnetotransport in narrow-gap semiconductors: an application to Zirconium Pentatelluride ZrTe5 (2024), arXiv:2401.15151 [cond-mat].
- [10] G. Kresse and J. Furthmller, Efficient iterative schemes for ab initio total-energy calculations using a plane-wave basis set, Physical Review B 54, 11169 (1996).
- [11] P. Giannozzi, S. Baroni, N. Bonini, M. Calandra, R. Car, C. Cavazzoni, D. Ceresoli, G. L. Chiarotti, M. Cococcioni, I. Dabo, A. Dal Corso, S. De Gironcoli, S. Fabris, G. Fratesi, R. Gebauer, U. Gerstmann, C. Gougoussis, A. Kokalj, M. Lazzeri, L. Martin-Samos, N. Marzari, F. Mauri, R. Mazzarello, S. Paolini, A. Pasquarello, L. Paulatto, C. Sbraccia, S. Scandolo, G. Sclauzero, A. P. Seitsonen, A. Smogunov, P. Umari, and R. M. Wentzcovitch, QUANTUM ESPRESSO: a modular and opensource software project for quantum simulations of materials, Journal of Physics: Condensed Matter 21, 395502

(2009).

- [12] P. Giannozzi, O. Andreussi, T. Brumme, O. Bunau, M. Buongiorno Nardelli, M. Calandra, R. Car, C. Cavazzoni, D. Ceresoli, M. Cococcioni, N. Colonna, I. Carn-


- imeo, A. Dal Corso, S. De Gironcoli, P. Delugas, R. A. DiStasio, A. Ferretti, A. Floris, G. Fratesi, G. Fugallo, R. Gebauer, U. Gerstmann, F. Giustino, T. Gorni, J. Jia, M. Kawamura, H.-Y. Ko, A. Kokalj, E. Kkbenli, M. Lazzeri, M. Marsili, N. Marzari, F. Mauri, N. L. Nguyen, H.-V. Nguyen, A. Otero-de-la Roza, L. Paulatto, S. Ponc, D. Rocca, R. Sabatini, B. Santra, M. Schlipf, A. P. Seitsonen, A. Smogunov, I. Timrov, T. Thonhauser, P. Umari, N. Vast, X. Wu, and S. Baroni, Advanced capabilities for materials modelling with Quantum ESPRESSO, Journal of Physics: Condensed Matter 29, 465901 (2017).
- [13] S. J. Clark, M. D. Segall, C. J. Pickard, P. J. Hasnip, M. I. J. Probert, K. Refson, and M. C. Payne, First principles methods using CASTEP, Zeitschrift fr Kristallographie - Crystalline Materials 220, 567 (2005).
- [14] T. Ozaki, Variationally optimized atomic orbitals for large-scale electronic structures, Physical Review B 67, 155108 (2003).
- [15] H. Weng, T. Ozaki, and K. Terakura, Revisiting magnetic coupling in transition-metal-benzene complexes with maximally localized Wannier functions, Physical Review B 79, 235118 (2009).
- [16] J. M. Soler, E. Artacho, J. D. Gale, A. Garca, J. Junquera, P. Ordejn, and D. Snchez-Portal, The SIESTA method for ab initio order- N materials simulation, Journal of Physics: Condensed Matter 14, 2745 (2002).
- [17] P. Blaha, K. Schwarz, F. Tran, R. Laskowski, G. K. H. Madsen, and L. D. Marks, WIEN2k: An APW+lo program for calculating the properties of solids, The Journal of Chemical Physics 152, 074101 (2020).
- [18] The Elk Code.
- [19] V. Wang, N. Xu, J.-C. Liu, G. Tang, and W.-T. Geng, Vaspkit: A user-friendly interface facilitating highthroughput computing and analysis using vasp code, Computer Physics Communications 267, 108033 (2021).
- [20] A. Hjorth Larsen, J. Jrgen Mortensen, J. Blomqvist,

- I. E. Castelli, R. Christensen, M. Duak, J. Friis, M. N. Groves, B. Hammer, C. Hargus, E. D. Hermes, P. C. Jennings, P. Bjerre Jensen, J. Kermode, J. R. Kitchin, E. Leonhard Kolsbjerg, J. Kubal, K. Kaasbjerg, S. Lysgaard, J. Bergmann Maronsson, T. Maxson, T. Olsen, L. Pastewka, A. Peterson, C. Rostgaard,
- J. Schitz, O. Schtt, M. Strange, K. S. Thygesen, T. Vegge, L. Vilhelmsen, M. Walter, Z. Zeng, and K. W. Jacobsen, The atomic simulation environmenta Python library for working with atoms, Journal of Physics: Condensed Matter 29, 273002 (2017).


- [21] S. P. Ong, W. D. Richards, A. Jain, G. Hautier, M. Kocher, S. Cholia, D. Gunter, V. L. Chevrier, K. A. Persson, and G. Ceder, Python Materials Genomics (pymatgen): A robust, open-source python library for materials analysis, Computational Materials Science 68, 314

(2013).

- [22] H. Wang, L. Zhang, J. Han, and W. E, DeePMD-kit: A deep learning package for many-body potential energy representation and molecular dynamics, Computer Physics Communications 228, 178 (2018).
- [23] S. Batzner, A. Musaelian, L. Sun, M. Geiger, J. P. Mailoa, M. Kornbluth, N. Molinari, T. E. Smidt, and B. Kozinsky, E(3)-equivariant graph neural networks for data-efficient and accurate interatomic potentials, Nature Communications 13, 2453 (2022).


- [24] B. Deng, P. Zhong, K. Jun, J. Riebesell, K. Han, C. J. Bartel, and G. Ceder, CHGNet as a pretrained universal neural network potential for charge-informed atomistic modelling, Nature Machine Intelligence 5, 1031 (2023).
- [25] A. Yang, A. Li, B. Yang, B. Zhang, B. Hui, B. Zheng, B. Yu, C. Gao, C. Huang, C. Lv, C. Zheng, D. Liu, F. Zhou, F. Huang, F. Hu, H. Ge, H. Wei, H. Lin, J. Tang, J. Yang, J. Tu, J. Zhang, J. Yang, J. Yang, J. Zhou, J. Zhou, J. Lin, K. Dang, K. Bao, K. Yang, L. Yu, L. Deng, M. Li, M. Xue, M. Li, P. Zhang, P. Wang, Q. Zhu, R. Men, R. Gao, S. Liu, S. Luo, T. Li, T. Tang, W. Yin, X. Ren, X. Wang, X. Zhang, X. Ren, Y. Fan,

- Y. Su, Y. Zhang, Y. Zhang, Y. Wan, Y. Liu, Z. Wang,
- Z. Cui, Z. Zhang, Z. Zhou, and Z. Qiu, Qwen3 Technical Report (2025), arXiv:2505.09388 [cs].


- [26] DeepSeek-AI, A. Liu, B. Feng, B. Xue, B. Wang, B. Wu, C. Lu, C. Zhao, C. Deng, C. Zhang, C. Ruan, D. Dai, D. Guo, D. Yang, D. Chen, D. Ji, E. Li, F. Lin, F. Dai, F. Luo, G. Hao, G. Chen, G. Li, H. Zhang, H. Bao, H. Xu, H. Wang, H. Zhang, H. Ding, H. Xin, H. Gao, H. Li, H. Qu, J. L. Cai, J. Liang, J. Guo, J. Ni, J. Li, J. Wang,

- J. Chen, J. Chen, J. Yuan, J. Qiu, J. Li, J. Song, K. Dong,
- K. Hu, K. Gao, K. Guan, K. Huang, K. Yu, L. Wang,
- L. Zhang, L. Xu, L. Xia, L. Zhao, L. Wang, L. Zhang,
- M. Li, M. Wang, M. Zhang, M. Zhang, M. Tang, M. Li,
- N. Tian, P. Huang, P. Wang, P. Zhang, Q. Wang, Q. Zhu,


- Q. Chen, Q. Du, R. J. Chen, R. L. Jin, R. Ge, R. Zhang,
- R. Pan, R. Wang, R. Xu, R. Zhang, R. Chen, S. S. Li,
- S. Lu, S. Zhou, S. Chen, S. Wu, S. Ye, S. Ye, S. Ma,


- S. Wang, S. Zhou, S. Yu, S. Zhou, S. Pan, T. Wang,
- T. Yun, T. Pei, T. Sun, W. L. Xiao, W. Zeng, W. Zhao,


- W. An, W. Liu, W. Liang, W. Gao, W. Yu, W. Zhang,
- X. Q. Li, X. Jin, X. Wang, X. Bi, X. Liu, X. Wang,

- X. Shen, X. Chen, X. Zhang, X. Chen, X. Nie, X. Sun,

- X. Wang, X. Cheng, X. Liu, X. Xie, X. Liu, X. Yu,

- X. Song, X. Shan, X. Zhou, X. Yang, X. Li, X. Su,

- X. Lin, Y. K. Li, Y. Q. Wang, Y. X. Wei, Y. X. Zhu,
- Y. Zhang, Y. Xu, Y. Xu, Y. Huang, Y. Li, Y. Zhao,


- Y. Sun, Y. Li, Y. Wang, Y. Yu, Y. Zheng, Y. Zhang,


- Y. Shi, Y. Xiong, Y. He, Y. Tang, Y. Piao, Y. Wang,


- Y. Tan, Y. Ma, Y. Liu, Y. Guo, Y. Wu, Y. Ou, Y. Zhu,

- Y. Wang, Y. Gong, Y. Zou, Y. He, Y. Zha, Y. Xiong,

- Y. Ma, Y. Yan, Y. Luo, Y. You, Y. Liu, Y. Zhou, Z. F. Wu, Z. Z. Ren, Z. Ren, Z. Sha, Z. Fu, Z. Xu, Z. Huang,
- Z. Zhang, Z. Xie, Z. Zhang, Z. Hao, Z. Gou, Z. Ma,


- Z. Yan, Z. Shao, Z. Xu, Z. Wu, Z. Zhang, Z. Li, Z. Gu,


- Z. Zhu, Z. Liu, Z. Li, Z. Xie, Z. Song, Z. Gao, and Z. Pan, DeepSeek-V3 Technical Report (2025), arXiv:2412.19437 [cs].




- [27] DeepSeek-AI, D. Guo, D. Yang, H. Zhang, J. Song, R. Zhang, R. Xu, Q. Zhu, S. Ma, P. Wang, X. Bi, X. Zhang, X. Yu, Y. Wu, Z. F. Wu, Z. Gou, Z. Shao, Z. Li, Z. Gao, A. Liu, B. Xue, B. Wang, B. Wu, B. Feng, C. Lu, C. Zhao, C. Deng, C. Zhang, C. Ruan, D. Dai, D. Chen, D. Ji, E. Li, F. Lin, F. Dai, F. Luo, G. Hao, G. Chen,


- G. Li, H. Zhang, H. Bao, H. Xu, H. Wang, H. Ding,
- H. Xin, H. Gao, H. Qu, H. Li, J. Guo, J. Li, J. Wang,


- J. Chen, J. Yuan, J. Qiu, J. Li, J. L. Cai, J. Ni, J. Liang,
- J. Chen, K. Dong, K. Hu, K. Gao, K. Guan, K. Huang,


- K. Yu, L. Wang, L. Zhang, L. Zhao, L. Wang, L. Zhang,
- L. Xu, L. Xia, M. Zhang, M. Zhang, M. Tang, M. Li,
- M. Wang, M. Li, N. Tian, P. Huang, P. Zhang, Q. Wang,


- Q. Chen, Q. Du, R. Ge, R. Zhang, R. Pan, R. Wang,
- R. J. Chen, R. L. Jin, R. Chen, S. Lu, S. Zhou, S. Chen,


S. Ye, S. Wang, S. Yu, S. Zhou, S. Pan, S. S. Li, S. Zhou, S. Wu, S. Ye, T. Yun, T. Pei, T. Sun, T. Wang, W. Zeng,

- W. Zhao, W. Liu, W. Liang, W. Gao, W. Yu, W. Zhang,

- W. L. Xiao, W. An, X. Liu, X. Wang, X. Chen, X. Nie,
- X. Cheng, X. Liu, X. Xie, X. Liu, X. Yang, X. Li, X. Su,

- X. Lin, X. Q. Li, X. Jin, X. Shen, X. Chen, X. Sun,

- X. Wang, X. Song, X. Zhou, X. Wang, X. Shan, Y. K. Li, Y. Q. Wang, Y. X. Wei, Y. Zhang, Y. Xu, Y. Li,
- Y. Zhao, Y. Sun, Y. Wang, Y. Yu, Y. Zhang, Y. Shi,


- Y. Xiong, Y. He, Y. Piao, Y. Wang, Y. Tan, Y. Ma,


- Y. Liu, Y. Guo, Y. Ou, Y. Wang, Y. Gong, Y. Zou,

- Y. He, Y. Xiong, Y. Luo, Y. You, Y. Liu, Y. Zhou, Y. X. Zhu, Y. Xu, Y. Huang, Y. Li, Y. Zheng, Y. Zhu, Y. Ma,

- Y. Tang, Y. Zha, Y. Yan, Z. Z. Ren, Z. Ren, Z. Sha, Z. Fu,
- Z. Xu, Z. Xie, Z. Zhang, Z. Hao, Z. Ma, Z. Yan, Z. Wu,


- Z. Gu, Z. Zhu, Z. Liu, Z. Li, Z. Xie, Z. Song, Z. Pan,


- Z. Huang, Z. Xu, Z. Zhang, and Z. Zhang, DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning (2025), arXiv:2501.12948 [cs].




- [28] G.-V. Team, W. Hong, W. Yu, X. Gu, G. Wang, G. Gan, H. Tang, J. Cheng, J. Qi, J. Ji, L. Pan, S. Duan, W. Wang, Y. Wang, Y. Cheng, Z. He, Z. Su, Z. Yang, Z. Pan, A. Zeng, B. Wang, B. Shi, C. Pang, C. Zhang, D. Yin, F. Yang, G. Chen, J. Xu, J. Chen, J. Chen, J. Chen, J. Lin, J. Wang, J. Chen, L. Lei, L. Gong, L. Pan, M. Zhang, Q. Zheng, S. Yang, S. Zhong,

- S. Huang, S. Zhao, S. Xue, S. Tu, S. Meng, T. Zhang,
- T. Luo, T. Hao, W. Li, W. Jia, X. Lyu, X. Huang, Y. Wang, Y. Xue, Y. Wang, Y. An, Y. Du, Y. Shi, Y. Huang, Y. Niu, Y. Wang, Y. Yue, Y. Li, Y. Zhang, Y. Zhang, Z. Du, Z. Hou, Z. Xue, Z. Du, Z. Wang, P. Zhang, D. Liu, B. Xu, J. Li, M. Huang, Y. Dong, and J. Tang, GLM-4.1V-Thinking: Towards Versatile Multimodal Reasoning with Scalable Reinforcement Learning


(2025), arXiv:2507.01006 [cs].

- [29] Meta AI, Llama 4: A new era in multimodal intelligence

(2025), accessed: 2025-08-07.

- [30] G. Team, A. Kamath, J. Ferret, S. Pathak, N. Vieillard, R. Merhej, S. Perrin, T. Matejovicova, A. Ram,


- M. Rivire, L. Rouillard, T. Mesnard, G. Cideron, J.b. Grill, S. Ramos, E. Yvinec, M. Casbon, E. Pot,

I. Penchev, G. Liu, F. Visin, K. Kenealy, L. Beyer, X. Zhai, A. Tsitsulin, R. Busa-Fekete, A. Feng,

- N. Sachdeva, B. Coleman, Y. Gao, B. Mustafa, I. Barr, E. Parisotto, D. Tian, M. Eyal, C. Cherry, J.-T. Peter, D. Sinopalnikov, S. Bhupatiraju, R. Agarwal, M. Kazemi, D. Malkin, R. Kumar, D. Vilar, I. Brusilovsky, J. Luo, A. Steiner, A. Friesen, A. Sharma, A. Sharma, A. M. Gilady, A. Goedeckemeyer, A. Saade, A. Feng, A. Kolesnikov, A. Bendebury, A. Abdagic, A. Vadi, A. Gyrgy, A. S. Pinto, A. Das, A. Bapna, A. Miech, A. Yang, A. Paterson, A. Shenoy, A. Chakrabarti, B. Piot, B. Wu, B. Shahriari, B. Petrini, C. Chen, C. L. Lan, C. A. ChoquetteChoo, C. J. Carey, C. Brick, D. Deutsch, D. Eisenbud, D. Cattle, D. Cheng, D. Paparas, D. S. Sreepathihalli,


- D. Reid, D. Tran, D. Zelle, E. Noland, E. Huizenga,
- E. Kharitonov, F. Liu, G. Amirkhanyan, G. Cameron, H. Hashemi, H. Klimczak-Pluciska, H. Singh, H. Mehta,


- H. T. Lehri, H. Hazimeh, I. Ballantyne, I. Szpektor,
- I. Nardini, J. Pouget-Abadie, J. Chan, J. Stanton, J. Wieting, J. Lai, J. Orbay, J. Fernandez, J. Newlan, J.-y. Ji, J. Singh, K. Black, K. Yu, K. Hui, K. Vodrahalli, K. Greff, L. Qiu, M. Valentine, M. Coelho, M. Ritter,


- M. Hoffman, M. Watson, M. Chaturvedi, M. Moynihan, M. Ma, N. Babar, N. Noy, N. Byrd, N. Roy,
- N. Momchev, N. Chauhan, N. Sachdeva, O. Bunyan, P. Botarda, P. Caron, P. K. Rubenstein, P. Culliton, P. Schmid, P. G. Sessa, P. Xu, P. Stanczyk, P. Tafti,

- R. Shivanna, R. Wu, R. Pan, R. Rokni, R. Willoughby,

- R. Vallu, R. Mullins, S. Jerome, S. Smoot, S. Girgin,
- S. Iqbal, S. Reddy, S. Sheth, S. Pder, S. Bhatnagar,


- S. R. Panyam, S. Eiger, S. Zhang, T. Liu, T. Yacovone, T. Liechty, U. Kalra, U. Evci, V. Misra, V. Roseberry, V. Feinberg, V. Kolesnikov, W. Han, W. Kwon,


- X. Chen, Y. Chow, Y. Zhu, Z. Wei, Z. Egyed, V. Cotruta, M. Giang, P. Kirk, A. Rao, K. Black, N. Babar, J. Lo, E. Moreira, L. G. Martins, O. Sanseviero, L. Gonzalez, Z. Gleicher, T. Warkentin, V. Mirrokni, E. Senter, E. Collins, J. Barral, Z. Ghahramani, R. Hadsell,
- Y. Matias, D. Sculley, S. Petrov, N. Fiedel, N. Shazeer,


- O. Vinyals, J. Dean, D. Hassabis, K. Kavukcuoglu, C. Farabet, E. Buchatskaya, J.-B. Alayrac, R. Anil, Dmitry, Lepikhin, S. Borgeaud, O. Bachem, A. Joulin, A. Andreev, C. Hardin, R. Dadashi, and L. Hussenot, Gemma 3 Technical Report (2025), arXiv:2503.19786 [cs].


- [31] S. Kim, Y. Jung, and J. Schrier, Large language models for inorganic synthesis predictions, Journal of the American Chemical Society 146, 19654 (2024), pMID: 38991051, https://doi.org/10.1021/jacs.4c05840.
- [32] Z. Song, S. Lu, M. Ju, Q. Zhou, and J. Wang, Is large language model all you need to predict the synthesizability and precursors of crystal structures? (2024), 2407.07016 [cond-mat].
- [33] Z. Zheng, O. Zhang, C. Borgs, J. T. Chayes, and O. M. Yaghi, Chatgpt chemistry assistant for text mining and the prediction of mof synthesis, Journal of the American Chemical Society 145, 18048 (2023), pMID: 37548379, https://doi.org/10.1021/jacs.3c05819.
- [34] S. Lee, K. Cruse, V. Baibakova, G. Ceder, and A. Jain, Text-mined dataset of solid-state syntheses with impurity phases using large language model (2025).
- [35] X.-D. Wang, Z.-R. Chen, P.-J. Guo, Z.-F. Gao, C. Mu, and Z.-Y. Lu, Perovskite-r1: A domain-specialized LLM for intelligent discovery of precursor additives and experimental design (2025), 2507.16307 [cs].
- [36] S. Hong, M. Zhuge, J. Chen, X. Zheng, Y. Cheng, J. Wang, C. Zhang, Z. Wang, S. K. S. Yau, Z. Lin, L. Zhou, C. Ran, L. Xiao, C. Wu, and J. Schmidhuber, MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework, in The Twelfth International Conference on Learning Representations (2024).
- [37] LangChain AI, LangGraph: Build resilient language agents as graphs (2023).
- [38] CrewAI, CrewAI: The Leading Multi-Agent Platform

(2024).

- [39] A. Ghafarollahi and M. J. Buehler, AtomAgents: Alloy design and discovery through physics-aware multi-modal multi-agent artificial intelligence (2024), arXiv:2407.10022 [cs].
- [40] A. P. Thompson, H. M. Aktulga, R. Berger, D. S. Bolintineanu, W. M. Brown, P. S. Crozier, P. J. In ’T Veld, A. Kohlmeyer, S. G. Moore, T. D. Nguyen, R. Shan, M. J. Stevens, J. Tranchida, C. Trott, and S. J. Plimpton, LAMMPS - a flexible simulation tool for particle-based materials modeling at the atomic, meso, and continuum scales, Computer Physics Communications 271, 108171


- (2022).
- [41] B. Zhang, X. Li, H. Xu, Z. Jin, Q. Wu, and C. Li, TopoMAS: Large Language Model Driven Topological Materials Multiagent System (2025), arXiv:2507.04053 [condmat].
- [42] Z. Ni, Y. Li, K. Hu, K. Han, M. Xu, X. Chen, F. Liu, Y. Ye, and S. Bai, MatPilot: an LLM-enabled AI Materials Scientist under the Framework of Human-Machine Collaboration (2025), arXiv:2411.08063 [physics.soc-ph].
- [43] T. Song, M. Luo, X. Zhang, L. Chen, Y. Huang, J. Cao, Q. Zhu, D. Liu, B. Zhang, G. Zou, G. Zhang, F. Zhang, W. Shang, Y. Fu, J. Jiang, and Y. Luo, A Multiagent-Driven Robotic AI Chemist Enabling Autonomous Chemical Research On Demand, Journal of the American Chemical Society 147, 12534 (2025), eprint: https://doi.org/10.1021/jacs.4c17738.

- [44] Y. Zou, A. H. Cheng, A. Aldossary, J. Bai, S. X. Leong, J. A. Campos-Gonzalez-Angulo, C. Choi, C. T. Ser, G. Tom, A. Wang, Z. Zhang, I. Yakavets, H. Hao, C. Crebolder, V. Bernales, and A. Aspuru-Guzik, El Agente: An Autonomous Agent for Quantum Chemistry (2025), arXiv:2505.02484 [cs].
- [45] Z. Wang, H. Huang, H. Zhao, C. Xu, S. Zhu, J. Janssen, and V. Viswanathan, DREAMS: Density Functional Theory Based Research Engine for Agentic Materials Simulation (2025), arXiv:2507.14267 [cs].
- [46] C. Bannwarth, E. Caldeweyher, S. Ehlert, A. Hansen, P. Pracht, J. Seibert, S. Spicher, and S. Grimme, Extended tightbinding quantum chemistry methods, WIREs Computational Molecular Science 11, e1493

(2021).

- [47] Model Context Protocol, Model context protocol (2024).
- [48] A. Jain, S. P. Ong, G. Hautier, W. Chen, W. D. Richards, S. Dacek, S. Cholia, D. Gunter, D. Skinner, G. Ceder, and K. a. Persson, The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1, 011002 (2013).
- [49] P. Lewis, E. Perez, A. Piktus, F. Petroni, V. Karpukhin, N. Goyal, H. Kttler, M. Lewis, W. tau Yih, T. Rock-


- tschel, S. Riedel, and D. Kiela, Retrieval-augmented generation for knowledge-intensive nlp tasks (2021), arXiv:2005.11401 [cs.CL].
- [50] Pallets Projects, Flask (2025).
- [51] S. Grimme, Semiempirical GGAtype density functional constructed with a longrange dispersion correction, Journal of Computational Chemistry 27, 1787 (2006).
- [52] S. Grimme, J. Antony, S. Ehrlich, and H. Krieg, A consistent and accurate ab initio parametrization of density functional dispersion correction (DFT-D) for the 94 elements H-Pu, The Journal of Chemical Physics 132, 154104 (2010).
- [53] S. Grimme, S. Ehrlich, and L. Goerigk, Effect of the damping function in dispersion corrected density functional theory, Journal of Computational Chemistry 32, 1456 (2011).
- [54] A. Tkatchenko and M. Scheffler, Accurate Molecular Van Der Waals Interactions from Ground-State Electron Density and Free-Atom Reference Data, Physical Review Letters 102, 073005 (2009).
- [55] J. Klime, D. R. Bowler, and A. Michaelides, Van der Waals density functionals applied to solids, Physical Review B 83, 195131 (2011).
- [56] J. Klime, D. R. Bowler, and A. Michaelides, Chemical accuracy for the van der Waals density functional, Journal of Physics: Condensed Matter 22, 022201 (2010).
- [57] H. Peng, Z.-H. Yang, J. P. Perdew, and J. Sun, Versatile van der Waals Density Functional Based on a MetaGeneralized Gradient Approximation, Physical Review X 6, 041005 (2016).
- [58] J. Ning, M. Kothakonda, J. W. Furness, A. D. Kaplan, S. Ehlert, J. G. Brandenburg, J. P. Perdew, and J. Sun, Workhorse minimally empirical dispersion-corrected density functional with tests for weakly bound systems: r2 SCAN + rVV10, Physical Review B 106, 075422 (2022).
- [59] R. Sabatini, T. Gorni, and S. De Gironcoli, Nonlocal van der Waals density functional made simple and efficient, Physical Review B 87, 041108 (2013).


