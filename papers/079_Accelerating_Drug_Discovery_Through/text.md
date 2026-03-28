## Accelerating drug discovery with Artificial: a whole-lab orchestration and scheduling system for self-driving labs

Yao Fehlis, Paul Mandel, Charles Crain, Betty Liu, David Fullera

aArtificial Inc.,

### Abstract

Self-driving labs are transforming drug discovery by enabling automated, AI-guided experimentation, but they face challenges in orchestrating complex workflows, integrating diverse instruments and AI models, and managing data efficiently. Artificial addresses these issues with a comprehensive orchestration and scheduling system that unifies lab operations, automates workflows, and integrates AI-driven decision-making. By incorporating AI/ML models like NVIDIA BioNeMo—which facilitates molecular interaction prediction and biomolecular analysis—Artificial enhances drug discovery and accelerates data-driven research. Through real-time coordination of instruments, robots, and personnel, the platform streamlines experiments, enhances reproducibility, and advances drug discovery.

# arXiv:2504.00986v1[cs.SE]1 Apr 2025

Keywords: Self-driving labs, data silos, drug discovery, whole-lab orchestration, NVIDIA BioNeMo

### 1. Introduction

Rojas et al., 2024). Virtual screening allows researchers to rapidly evaluate large libraries of chemical compounds, prioritizing those most likely to exhibit therapeutic potential. Molecular simulations provide insights into drug-target interactions, protein folding, and binding affinities, significantly reducing the need for exhaustive trial-and-error experimentation. AI further enhances these processes by applying machine learning algorithms to predict molecular properties, optimize lead compounds, and refine drug candidates through iterative learning. By integrating these computational tools into experimental workflows, researchers can accelerate drug discovery, reduce costs, and improve the likelihood of identifying effective therapeutics. The synergy between in silico methodologies and automated laboratory processes represents a transformative shift in how drugs are developed, enabling more efficient and datadriven decision-making.

The landscape of drug discovery has long been characterized by a multitude of challenges, including the high costs of research and development, lengthy timelines, and a significant rate of failure during clinical trials (Blanco-Gonzalez et al.,

- 2023; Udegbe et al., 2024; Khanna, 2012; Moffat et al., 2017). These hurdles have necessitated the exploration of innovative approaches that can streamline drug development processes. Traditional methods are often labor-intensive and prone to human error, which can lead to inefficiencies and inconsistencies in result fidelity. As a response to these challenges, self-driving laboratories have emerged as a promising solution, leveraging automation and artificial intelligence (AI) to enhance the efficiency and efficacy of experimental workflows.

Self-driving labs are designed to automate various aspects of the drug discovery process, from hypothesis generation to experimental execution and data analysis (Edfeldt et al., 2024; Rapp et al., 2024). These labs integrate robotic systems that can autonomously perform experiments based on pre-defined protocols, significantly reducing human involvement and minimizing the chances for error. This automation is not just about increasing throughput but also about maintaining a high degree of precision and reproducibility, which are critical factors in drug development. As self-driving labs continue to evolve, they are being increasingly complemented by advances in artificial intelligence, which plays a pivotal role in orchestrating various laboratory activities and optimizing resource allocation.

A crucial aspect of modern drug discovery is the use of virtual screening (Lavecchia and Di Giovanni, 2013; Zhou et al.,

- 2024; Zhu et al., 2022; Murugan et al., 2022), molecular simulations (Adelusi et al., 2022; Casalini, 2021; Shukla and Tripathi, 2021; Adediwura et al., 2024), and AI-driven computational methods (Mak et al., 2024; Deng et al., 2022; Dodero-


Artificial intelligence in the context of drug discovery offers powerful capabilities such as predictive modeling, machine learning-based data analysis, and the automation of repetitive tasks (Schauperl and Denny, 2022; Marco et al., 2024; Obaido et al., 2024; Colliandre and Muller, 2023; Pyzer-Knapp, 2018; Guo et al., 2024). These AI-driven technologies can process vast amounts of data generated from experiments, facilitating more informed decision-making and accelerating the pace of drug discovery (Zhu, 2020; Glicksberg et al., 2019; Vergetis et al., 2021). Furthermore, the integration of AI with laboratory automation establishes a framework in which complex experimental designs can be implemented with greater accuracy and less manual oversight (Abolhasani and Kumacheva, 2023; Delgado-Licona and Abolhasani, 2023; Sanders et al., 2023). By enabling intelligent decision-making and optimizing workflows, AI enhances the efficiency of self-driving labs and contributes to more rapid identification of promising drug candi-

Preprint submitted to SLAS Technology April 2, 2025

dates.

However, the effective implementation of AI in drug discovery is not without challenges. A predominant issue that hampers AI performance is the existence of data silos—discrete sets of data that remain isolated and uncoupled from broader datasets (Denton et al., 2021; Wibowo et al., 2017; Patel, 2019; Kasturi et al., 2014; Ziegler et al., 2021). The potential for AI optimization hinges on the availability of comprehensive and high-quality datasets; thus, when relevant data is dispersed across various studies or proprietary platforms, researchers may find it difficult to train robust AI models. Addressing this issue requires strategic initiatives aimed at fostering data sharing and creating standardized data formats that facilitate integration. As the drug discovery landscape increasingly embraces AI, collaboration among institutions and industries becomes paramount to democratize access to data, thereby unleashing the full potential of AI-driven methodologies (Cheng et al., 2020; Khanna, 2012; Peeva et al., 2025).

In addition to data fragmentation, integrating AI models into scientific labs presents further challenges due to the diverse and noisy nature of experimental data (Gadiya et al., 2023; Blatter et al., 2022; Alharbi et al., 2022, 2023). AI models must be tailored to specific scientific needs, ensuring interpretability while seamlessly interacting with laboratory systems. Successful AI deployment requires robust computational pipelines capable of handling complex workflows, standardizing data preprocessing, and maintaining reproducibility. Without well-structured data pipelines, AI-driven insights may suffer from inconsistencies, ultimately reducing their reliability in guiding drug discovery efforts. Therefore, a well-orchestrated integration framework is necessary to ensure that AI not only enhances experimental workflows but also generates reproducible and actionable outcomes.

To address these challenges and maximize the potential of AI-driven self-driving laboratories, this paper presents Artificial, a platform designed to orchestrate laboratory workflows, integrate AI-driven decision-making, and facilitate seamless data management. Artificial enables the incorporation of AI models, such as those implemented in NVIDIA BioNeMo NIMs (containerized, pre-trained AI models with APIs), into self-driving virtual screening and experimental processes. This integration enhances the efficiency of drug discovery by enabling automated, data-driven decision-making and improving the reproducibility of experimental workflows.

In this paper, we present a proof-of-concept case study demonstrating the orchestration of NVIDIA BioNeMo models within a self-driving virtual screening workflow in a dry lab setting. This study highlights how Artificial automates AI model deployment, optimizes computational resource allocation, and facilitates seamless data exchange, ultimately accelerating the identification of promising drug candidates. While the case study focuses on dry lab applications, the underlying methodology and benefits of Artificial extend to both dry and wet lab environments, enabling more efficient execution of AI-driven drug discovery across the entire R&D pipeline.

We further discuss how Artificial enhances laboratory automation by integrating AI models into structured workflows,

optimizing resource utilization, and ensuring reproducible datadriven experimentation. The platform’s orchestration engine automates workflow planning, scheduling, and data consolidation, significantly improving efficiency in iterative experimentation. By streamlining AI-driven analyses and facilitating rapid hypothesis testing, Artificial enables self-driving labs to shorten discovery timelines and improve the success rate of drug development.

### 2. Artificial: a whole-lab orchestration and scheduling system

Figure 1 illustrates a modular and scalable Artificial Orchestration Platform designed to streamline laboratory workflows, automate processes, and connect people, samples, robots, and instruments. It integrates data, automation, and informatics through a series of interconnected components and services. Below is a detailed explanation of its structure and logic:

Core Components

- 1. Web Apps (User-Facing Interfaces):

• Accessible on any device, these tools are designed for scientists and operators to interact with and control the lab ecosystem:

- – Labs: Enables building and managing a digital twin of the lab environment, mapping its operations, instruments, and workflows.
- – Assistants: Provides interactive guides and instructions for scientists and lab operators to follow manual or semi-automated processes.
- – Workflows: Facilitates the definition, configuration, and management of R&D processes, supporting repeatability and process optimization.
- – LabOps: Acts as a central hub for monitoring, running, and orchestrating both manual and automated R&D workflows.
- – Digital Twin: A 3D visualization layer that mirrors the physical lab’s environment, allowing simulation, monitoring, and optimization of experiments and processes.


- 2. Services:


• These backend components provide the computational power to manage orchestration, scheduling, data storage, and optimization:

- – Orchestration: Handles planning and request management for lab operations using a simplified dialect of Python, or a graphical interface.
- – Scheduler/Executor: An orchestration engine that uses heuristics, constraints, and batching to ensure efficient resource allocation and workflow execution.


![image 1](2025_Accelerating drug discovery with artificial a whole-lab orchestration and scheduling system for sel_images/imageFile1.png)

Figure 1: The Artificial stack.

– Data Records: Consolidates lab data, including results and logs, into an accessible and organized repository.

### 3. Lab API (Connectivity Layer):

- • A central interface supporting GraphQL, gRPC, and REST protocols, enabling integration between lab hardware, software, and external systems.
- • API endpoints provide access to:


- – Lab States and Events: Real-time monitoring of instrument status, process progress, and more.
- – Client Libraries: Pre-built libraries for developers to interact with lab data and automation.


### 4. Adapters and Communication Protocols:

- • Enables secure, local, and global communication between instruments, schedulers, informatics systems, and GPUs/TPUs via:

- – HTTPS
- – gRPC (including SiLA)
- – Local APIs (including SciKit, TensorFlow/Keras, and PyTorch for AI/ML)


- • Supports the full Python programming language with its rich ecosystem.


### 5. Your Informatics (Integration with Lab Systems):

- • The platform connects to standard informatics tools like:


- – LIMS (Laboratory Information Management System): Inventory and sample management.
- – ELN (Electronic Lab Notebook): Data management and collaboration.
- – On-premises or cloud IT infrastructure: Integration with data lakes, business intelligence systems, etc.


6. Your Automation:

- • This layer interfaces with local hardware and software schedulers (e.g., Cellario, Momentum) and instrument drivers (e.g., Tecan, Thermo, Hamilton, Agilent).
- • Ensures secure and efficient connection through REST APIs with authentication.


Flow and Logic

- 1. Data Flow:

- • Samples, robots, and instruments feed data into the system via the Lab API, which consolidates and processes it using backend services such as Orchestration and Data Records.
- • The Digital Twin visualizes lab activities in realtime, providing an overview of workflows and system health.


- 2. Automation and Optimization:


- • Automated workflows are scheduled and executed using the Scheduler/Executor and Orchestration components.
- • The system ensures efficient resource usage by considering constraints and heuristics.


### 3. Integration with Existing Systems:

• The platform bridges legacy informatics systems (LIMS, ELN) with modern cloud and on-premise infrastructure, ensuring seamless operation across the lab.

### 4. User Interaction:

• Scientists interact with the platform through Web Apps, allowing them to define workflows, monitor progress, and manage lab operations with minimal complexity.

### 5. Scalability and Security:

- • Built for deployment on both cloud (EKS/AKS) and local environments (MicroK8s), ensuring flexibility and scalability.
- • Communication is secured with SSL encryption to protect sensitive lab data.


### 3. A case study

![image 2](2025_Accelerating drug discovery with artificial a whole-lab orchestration and scheduling system for sel_images/imageFile2.png)

Figure 2: The self-driving cycle.

We would like to present a case study on how Artificial powers self-driving labs by integrating design, optimization, execution, and AI-driven learning into an automated workflow.

Figure 2 illustrates how the Artificial platform supports selfdriving labs by enabling seamless integration of AI into laboratory workflows. The process is divided into four interconnected phases: Design, Run, and Learn, Optimize, creating a continuous improvement cycle powered by AI and automation:

### 1. Design:

The platform provides a Digital Lab Toolbox to design end-to-end workflows, integrating instruments, manual steps, labware, and AI systems. This ensures streamlined and reproducible processes tailored to specific experiments.

- 2. Run: LabOps enables real-time monitoring, tracking, and execution of experiments from anywhere. This ensures flawless execution, eliminates errors, and keeps experiments on schedule by automating task coordination.
- 3. Optimize: The LabOps engine optimizes lab performance by intelligently coordinating tasks and batch processes. It considers real-time availability of instruments, personnel, and resources to enhance efficiency and reduce downtime.
- 4. Learn: The platform logs all scientific and process data, providing a complete 360° context of each experiment. This data is leveraged by AI to generate insights, test hypotheses, and drive continuous improvements in workflows. This closed-loop system empowers self-driving labs to optimize operations, accelerate discovery, and achieve reproducibility through AI-driven automation and learning.


This closed-loop system empowers self-driving labs to optimize operations, accelerate discovery, and achieve reproducibility through AI-driven automation and learning.

### 4. A case study: orchestrating NVIDIA BioNeMo models in self-driving virtual screening

Virtual screening is crucial in drug discovery as it enables the rapid and cost-effective identification of potential drug candidates from vast compound libraries, significantly reducing the time and resources needed for experimental testing. It helps prioritize the most promising compounds for further development and testing.

NVIDIA BioNeMo is a platform for accelerating AI model development and deployment for digital biology applications (John et al., 2024). Designed to accelerate drug discovery, protein engineering, and virtual screening processes, BioNeMo provides pre-trained AI models as containerized microservices (NIM, i.e. NVIDIA Inference Microservices) and tools to predict molecular interactions, facilitate protein folding, and analyze biomolecular data with a high degree of acceleration and efficiency (Philippidis, 2024).

We have demonstrated the capabilities of workflows and model integration in Artificial using a proof of concept (PoC) use case for self-driving generative virtual screening. This PoC effectively showcases how NVIDIA’s BioNeMo NIM microservices are integrated with Artificial’s orchestration platform to facilitate advanced molecular screening. It specifically targets the SARS-CoV-2 virus, focusing on the main protease, a critical enzyme in viral replication and a well-established drug target in Covid-19 therapy. This use case also showcases how this process can be automated, in other words, self-driving until certain criteria are met. This is potentially useful for the concept of self-driving labs where Artificial can orchestrate the workflows and integrate the AI models in the process.

Based on the NVIDIA BioNeMo Blueprint for generative virtual screening, the self-driving virtual screening process is

![image 3](2025_Accelerating drug discovery with artificial a whole-lab orchestration and scheduling system for sel_images/imageFile3.png)

Figure 3: A proof of concept use case for self-driving virtual screening with NVIDIA BioNeMo models.

structured in iterative feedback loops, combining molecule selection, protein folding (if needed), docking, and binding affinity scoring. The workflow is executed as follows:

After three self-driving iterations, the set criteria were fulfilled:

- 1. The binding affinity threshold of -1.4 million was met.
- 2. A minimum of ten molecules were identified whose scoring values surpassed the required threshold.


This iterative approach highlights the capability of Artificial’s platform to autonomously refine molecular candidates, optimizing the selection process to focus on high-likelihood drug compounds. By combining BioNeMo’s advanced molecular modeling tools with Artificial’s automated orchestration and feedback systems, the PoC successfully demonstrated how AIdriven methodologies can accelerate virtual screening and drug discovery processes.

### 5. Artificial’s infrastructure for model integration

Artificial’s LabOps performs data management and integration for dry and wet labs, integrating purely in silico experimentation (as detailed here) with downstream laboratory automation. Central to Artificial’s architecture is the Lab Gateway, a network appliance that bridges the Artificial cloud to on-premises resources securely using bidirectional HTTP/2 streaming over an outbound connection. This allows LabOps to control and integrate data from automated laboratory equipment and secure IT infrastructure, including GPUs/TPUs for hosting AI models.

NVIDIA BioNeMo NIMs (containerized, pre-trained accelerated AI models, complete with APIs) allow models to be hosted in the cloud or securely behind a customer firewall onpremise. All data transacted between the Lab Gateway and any resource, cloud or on-premise, is kept in a permanent, immutable data record that is accessible via APIs or from other workflows. This allows data generated by inference and/or experimentation to be accessible for later training or fine-tuning of models.

Artificial’s ability to integrate AI models, such as those implemented in BioNeMo NIMs, into self-driving virtual screening workflows highlights its orchestration and data management capabilities. This approach extends beyond virtual screening, offering adaptability and scalability for a range of laboratory environments for drug discovery. By leveraging real-time simulation, sophisticated orchestration tools, and robust API integrations, Artificial’s platform enhances data quality, streamlines operations, and optimizes resource utilization, ultimately advancing both virtual screening and broader laboratory automation.

### 6. Conclusions

In conclusion, Artificial serves as a transformative solution for self-driving labs, addressing critical challenges in orchestrating complex workflows, integrating diverse instruments and AI models, and managing data efficiently. By automating scheduling, decision-making, and real-time coordination of lab resources, Artificial enhances reproducibility, accelerates discovery, and optimizes lab operations. This system not only

![image 4](2025_Accelerating drug discovery with artificial a whole-lab orchestration and scheduling system for sel_images/imageFile4.png)

Figure 4: The self-driving iterations during the virtual screening proof of concept.

streamlines experimentation but also empowers researchers to leverage AI-driven insights for more efficient drug discovery. As self-driving labs continue to evolve, Artificial provides a scalable framework that will drive the next generation of breakthroughs in drug discovery and development.

### Acknowledgments

We would like to thank Janet Paulsen for helpful conversions regarding the BioNeMo proof of concept and Youssef Nashed for technical support on BioNeMo related questions.

### References

Abolhasani, M., Kumacheva, E., 2023. The rise of self-driving labs in chemical and materials sciences. Nature Synthesis 2, 483–492.

Adediwura, V.A., Koirala, K., Do, H.N., Wang, J., Miao, Y., 2024. Understanding the impact of binding free energy and kinetics calculations in modern drug discovery. Expert Opinion on Drug Discovery 19, 671–682.

Adelusi, T.I., Oyedele, A.Q.K., Boyenle, I.D., Ogunlana, A.T., Adeyemi, R.O., Ukachi, C.D., Idris, M.O., Olaoba, O.T., Adedotun, I.O., Kolawole, O.E., et al., 2022. Molecular modeling in drug discovery. Informatics in Medicine Unlocked 29, 100880.

Alharbi, E., Gadiya, Y., Henderson, D., Zaliani, A., Delfin-Rossaro, A., Cambon-Thomsen, A., Kohler, M., Witt, G., Welter, D., Juty, N., et al., 2022. Selection of data sets for fairification in drug discovery and development: Which, why, and how? Drug discovery today 27, 2080–2085.

Alharbi, E., Skeva, R., Juty, N., Jay, C., Goble, C., 2023. A fair-decide framework for pharmaceutical r&d: Fair data cost–benefit assessment. Drug discovery today 28, 103510.

Blanco-Gonzalez, A., Cabezon, A., Seco-Gonzalez, A., Conde-Torres, D., Antelo-Riveiro, P., Pineiro, A., Garcia-Fandino, R., 2023. The role of ai in drug discovery: challenges, opportunities, and strategies. Pharmaceuticals 16, 891.

Blatter, T.U., Witte, H., Nakas, C.T., Leichtle, A.B., 2022. Big data in laboratory medicine—fair quality for ai? Diagnostics 12, 1923.

Casalini, T., 2021. Not only in silico drug discovery: Molecular modeling towards in silico drug delivery formulations. Journal of Controlled Release 332, 390–417.

Cheng, F., Ma, Y., Uzzi, B., Loscalzo, J., 2020. Importance of scientific collaboration in contemporary drug discovery and development: a detailed network analysis. BMC biology 18, 1–9.

Colliandre, L., Muller, C., 2023. Bayesian optimization in drug discovery, in: High Performance Computing for Drug Discovery and Biomedicine. Springer, pp. 101–136.

Delgado-Licona, F., Abolhasani, M., 2023. Research acceleration in selfdriving labs: Technological roadmap toward accelerated materials and molecular discovery. Advanced Intelligent Systems 5, 2200331.

Deng, J., Yang, Z., Ojima, I., Samaras, D., Wang, F., 2022. Artificial intelligence in drug discovery: applications and techniques. Briefings in Bioinformatics 23, bbab430.

Denton, N., Molloy, M., Charleston, S., Lipset, C., Hirsch, J., Mulberg, A.E., Howard, P., Marsh, E.D., 2021. Data silos are undermining drug development and failing rare disease patients. Orphanet Journal of Rare Diseases 16, 1–4.

Dodero-Rojas, E., Contessoto, V.G., Fehlis, Y., Mayala, N., Onuchic, J.N., 2024. Epigenetics is all you need: A transformer to decode chromatin structural compartments from the epigenome. bioRxiv URL: https://www. biorxiv.org/content/early/2024/07/19/2024.07.17.603864,

doi:10.1101/2024.07.17.603864.

Edfeldt, K., Edwards, A.M., Engkvist, O., G¨unther, J., Hartley, M., Hulcoop, D.G., Leach, A.R., Marsden, B.D., Menge, A., Misquitta, L., et al., 2024. A data science roadmap for open science organizations engaged in early-stage drug discovery. Nature Communications 15, 5640.

Gadiya, Y., Ioannidis, V., Henderson, D., Gribbon, P., Rocca-Serra, P., Satagopam, V., Sansone, S.A., Gu, W., 2023. Fair data management: what does it mean for drug discovery? Frontiers in Drug Discovery 3, 1226727.

Glicksberg, B.S., Li, L., Chen, R., Dudley, J., Chen, B., 2019. Leveraging big data to transform drug discovery. Bioinformatics and Drug Discovery , 91–118.

Guo, S.B., Meng, Y., Lin, L., Zhou, Z.Z., Li, H.L., Tian, X.P., Huang, W.J., 2024. Artificial intelligence alphafold model for molecular biology and drug

discovery: a machine-learning-driven informatics investigation. Molecular Cancer 23, 223.

John, P.S., Lin, D., Binder, P., Greaves, M., Shah, V., John, J.S., Lange, A., Hsu, P., Illango, R., Ramanathan, A., et al., 2024. Bionemo framework: a modular, high-performance library for ai model development in drug discovery. arXiv preprint arXiv:2411.10548 .

Kasturi, J., Brown, A.P., Brown, P., Madhavan, S., Prabakar, L., Wally, J.L., 2014. Interconnectivity of disparate nonclinical data silos for drug discovery and development. Therapeutic Innovation & Regulatory Science 48, 498– 506.

Khanna, I., 2012. Drug discovery in pharmaceutical industry: productivity challenges and trends. Drug discovery today 17, 1088–1102. Lavecchia, A., Di Giovanni, C., 2013. Virtual screening strategies in drug discovery: a critical review. Current medicinal chemistry 20, 2839–2860.

Mak, K.K., Wong, Y.H., Pichika, M.R., 2024. Artificial intelligence in drug discovery and development. Drug discovery and evaluation: safety and pharmacokinetic assays , 1461–1498.

Marco, G., Evertsson, E., Riley, D.J., Tyrchan, C., Rathi, P.C., 2024. Augmenting dmta using predictive ai modelling at astrazeneca. Drug discovery today , 103945.

Moffat, J.G., Vincent, F., Lee, J.A., Eder, J., Prunotto, M., 2017. Opportunities and challenges in phenotypic drug discovery: an industry perspective. Nature reviews Drug discovery 16, 531–543.

Murugan, N.A., Priya, G.R., Sastry, G.N., Markidis, S., 2022. Artificial intelligence in virtual screening: Models versus experiments. Drug Discovery Today 27, 1913–1923.

Obaido, G., Mienye, I.D., Egbelowo, O.F., Emmanuel, I.D., Ogunleye, A., Ogbuokiri, B., Mienye, P., Aruleba, K., 2024. Supervised machine learning in drug discovery and development: Algorithms, applications, challenges, and prospects. Machine Learning with Applications 17, 100576.

Patel, J., 2019. Overcoming data silos through big data integration. International Journal of Computer Science and Technology 3.

Peeva, E., Guttman-Yassky, E., Yamaguchi, Y., Berman, B., Oemar, B., Ramakrishna, J., Fasano, A., Evans-Molina, C., Chu, M., Ungar, B., et al., 2025. Unlocking disease insights to facilitate drug development: Pharmaceutical industry–academia collaborations in inflammation and immunology. Drug Discovery Today , 104317.

Philippidis, A., 2024. Gtc 2024: Nvidia highlights ai ‘revolution’in drug discovery, genomics. GEN Edge 6, 244–248. Pyzer-Knapp, E.O., 2018. Bayesian optimization for accelerated drug discovery. IBM Journal of Research and Development 62, 2–1.

Rapp, J.T., Bremer, B.J., Romero, P.A., 2024. Self-driving laboratories to autonomously navigate the protein fitness landscape. Nature chemical engineering 1, 97–107.

Sanders, L.M., Scott, R.T., Yang, J.H., Qutub, A.A., Garcia Martin, H., Berrios, D.C., Hastings, J.J., Rask, J., Mackintosh, G., Hoarfrost, A.L., et al., 2023. Biological research and self-driving labs in deep space supported by artificial intelligence. Nature Machine Intelligence 5, 208–219.

Schauperl, M., Denny, R.A., 2022. Ai-based protein structure prediction in drug discovery: impacts and challenges. Journal of Chemical Information and Modeling 62, 3142–3156.

Shukla, R., Tripathi, T., 2021. Molecular dynamics simulation in drug discovery: opportunities and challenges. Innovations and implementations of computer aided drug discovery strategies in rational drug design , 295–316.

Udegbe, F.C., Ebulue, O.R., Ebulue, C.C., Ekesiobi, C.S., 2024. Machine learning in drug discovery: A critical review of applications and challenges. Computer Science & IT Research Journal 5, 892–902.

Vergetis, V., Skaltsas, D., Gorgoulis, V.G., Tsirigos, A., 2021. Assessing drug development risk using big data and machine learning. Cancer research 81, 816–819.

Wibowo, M., Sulaiman, S., Shamsuddin, S.M., 2017. Machine learning in data lake for combining data silos, in: Data Mining and Big Data: Second International Conference, DMBD 2017, Fukuoka, Japan, July 27–August 1, 2017, Proceedings 2, Springer. pp. 294–306.

Zhou, G., Rusnac, D.V., Park, H., Canzani, D., Nguyen, H.M., Stewart, L., Bush, M.F., Nguyen, P.T., Wulff, H., Yarov-Yarovoy, V., et al., 2024. An artificial intelligence accelerated virtual screening platform for drug discovery. Nature Communications 15, 7761.

Zhu, H., 2020. Big data and artificial intelligence modeling for drug discovery. Annual review of pharmacology and toxicology 60, 573–589. Zhu, H., Zhang, Y., Li, W., Huang, N., 2022. A comprehensive survey of

prospective structure-based virtual screening for early drug discovery in the past fifteen years. International Journal of Molecular Sciences 23, 15961. Ziegler, J., Reimann, P., Keller, F., Mitschang, B., 2021. A metadata model to connect isolated data silos and activities of the cae domain, in: International Conference on Advanced Information Systems Engineering, Springer. pp. 213–228.

