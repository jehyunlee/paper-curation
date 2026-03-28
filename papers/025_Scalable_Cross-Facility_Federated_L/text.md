# arXiv:2603.19544v1[cs.LG]20 Mar 2026

## Scalable Cross-Facility Federated Learning for Scientific Foundation Models on Multiple Supercomputers

Yijiang Li1, Zilinghan Li2, Kyle Chard3, Ian Foster2,3, Todd Munson1, Ravi Madduri2, and Kibaek Kim1

1Mathematics and Computer Science Division, Argonne National Laboratory 2Data Science and Learning Division, Argonne National Laboratory 3Department of Computer Science, University of Chicago

Abstract

Artificial Intelligence for scientific applications increasingly requires training large models on data that cannot be centralized due to privacy constraints, data sovereignty, or the sheer volume of data generated. Federated learning (FL) addresses this by enabling collaborative training without centralizing raw data, but scientific applications demand model scales that requires extensive computing resources, typically offered at High Performance Computing (HPC) facilities. Deploying FL experiments across HPC facilities introduces challenges beyond cloud or enterprise settings. We present a comprehensive cross-facility FL framework for heterogeneous HPC environments, built on Advanced Privacy-Preserving Federated Learning (APPFL) framework with Globus Compute and Transfer orchestration, and evaluate it across four U.S. Department of Energy (DOE) leadership-class supercomputers. We demonstrate that FL experiments across HPC facilities are practically achievable, characterize key sources of heterogeneity impacting the training performance, and show that algorithmic choices matter significantly under realistic HPC scheduling conditions. We validate the scientific applicability by fine-tuning a large language model on a chemistry instruction dataset, and identify scheduler-aware algorithm design as a critical open challenge for future deployments.

### 1 Introduction

Artificial Intelligence for scientific applications increasingly faces a structural mismatch between where data are generated and stored and where model training occurs. There exist two distinct barriers preventing the centralization of raw training data. The first is privacy and data sovereignty: sensitive datasets in regulated domains such as healthcare and power grid operations cannot be shared across institutional boundaries due to policy, regulation, or security requirements. The second is practical scale: experimental facilities such as synchrotron beamlines can produce terabytes of data per experiment, resulting in datasets that are too large or operationally embedded to centralize, even when sharing is technically permissible. In both cases, collaborative model training across all data sources is infeasible without moving computation to the data, a challenge particularly acute for scientific facilities, where both barriers often apply simultaneously.

Federated learning (FL) enables collaborative model training without moving raw data [26,38]. In FL, clients train on local data and periodically send model updates to a central server, which aggregates them into a global model. There are two key distinct settings in FL: cross-device and cross-silo settings [23,26]. Cross-device FL involves many small, and often intermittently available, devices each holding small data volumes. Cross-silo FL involves a modest number of participating organizations or facilities, each usually holding large datasets and substantial compute resources, and are expected to participate reliably throughout training. FL experiments among scientific facilities naturally fit the cross-silo profile.

Cross-silo FL for large-scale scientific applications demands distributed GPU clusters with hundreds to thousands of GPU accelerators, computational resources that High Performance Computing (HPC) infrastructure is well-positioned to provide. However, HPC environments introduce constraints that standard FL

frameworks do not address: job schedulers with unpredictable queueing delays, strict site firewalls, heterogeneous accelerator architectures, independent operational policies across sites, and system interruptions from both scheduled and unscheduled maintenance that can disrupt long-running workloads. These constraints fundamentally reshape the FL system problem beyond what cloud or enterprise deployments encounter.

Despite the maturity of FL and HPC as independent fields, only limited prior work has explored their integration in hybrid cloud-HPC or cross-facility settings [11,33]. Prior studies mainly demonstrate feasibility, whereas our focus is a systematic empirical characterization of federated training across heterogeneous leadership-class HPC facilities. Existing cross-silo frameworks such as FATE [37], OpenFL [16], NVIDIA FLARE [46], and FedML [19] are primarily designed for cloud and enterprise settings and do not address HPC-specific constraints. Kim et al. [28] discuss privacy and computational heterogeneity challenges for cross-silo FL on HPC systems, but empirical evaluation across multiple facilities remains absent.

Here we present and evaluate a cross-facility FL framework designed for heterogeneous HPC environments. We evaluate this framework by using four U.S. Department of Energy (DOE) leadership-class supercomputers: Polaris and Aurora at the Argonne Leadership Computing Facility (ALCF), Frontier at the Oak Ridge Leadership Computing Facility (OLCF), and Perlmutter at the National Energy Research Scientific Computing Center (NERSC). These four systems span NVIDIA, AMD, and Intel accelerator architectures, multiple scheduler types, and distinct security and scheduling policies, making them a strong proxy for the diversity of modern HPC infrastructure. Our framework is built on the Advanced Privacy-Preserving Federated Learning framework (APPFL) [34,47] with orchestration via Globus Compute [10] for training task dispatch and Globus Transfer [57] for model and training configuration transfer, enabling local training jobs to execute under site-specific scheduling and security policies while model updates are exchanged reliably across wide-area networks.

Our contributions are as follows:

- 1. Cross-HPC facility FL framework: We design and implement a generalizable FL framework for orchestrating training across heterogeneous HPC facilities, supporting diverse models, datasets, and scientific tasks, while addressing challenges in communication, scheduling, and computation unique to this setting.
- 2. Performance characterization: We systematically characterize heterogeneity in computational throughput, communication costs, and queueing dynamics, revealing performance variations that existing FL algorithms do not adequately address.
- 3. Algorithm evaluation: We evaluate various existing FL algorithms under large-scale synchronous co-scheduled conditions and small-scale runs under realistic queueing conditions, revealing how heterogeneous schedulers and memory constraints impact algorithm performance.
- 4. Scientific validation: We verify the framework’s applicability to real scientific workloads by finetuning a large language model (LLM) on a chemistry instruction dataset, demonstrating that crossHPC facility FL can support large-scale scientific model development.


### 2 Results

In this section, we present experimental results for cross-HPC facility FL and provide the empirical groundings that inform the design principles of cross-HPC FL frameworks discussed in Section 3. In the experiment, we evaluate our framework through federated fine-tuning of an LLM on a chemistry instruction dataset. We distribute this task across four DOE leadership-class supercomputers acting as clients, with a CPU-only cluster at Argonne National Laboratory serving as the central server. We conduct two sets of experiments: (1) large-scale co-scheduled runs using HPC reservations to characterize upper-bound performance of crossfacility FL, and (2) smaller queue-based runs to evaluate algorithmic robustness under realistic scheduling conditions. Full details of hardware, software, and orchestration are provided in Section 4.

#### 2.1 Use Case and Data Distribution

We use SMolInstruct [55], a chemistry instruction tuning dataset containing over three million training samples, as our use case. SMolInstruct organizes its data into 14 distinct tasks, each corresponding to a

specific chemistry problem type, which are further grouped into four broader task groups: name conversion, property prediction, chemical reaction, and molecule description. The number of samples (i.e., instruction– response pairs) varies substantially across tasks, ranging from roughly 1,100 samples for the task of ESOL (Water Solubility) to nearly 978,000 for the task of forward synthesis. We fine-tune a pretrained Llama2-7B model [50] on this dataset in a federated manner.

In our FL setup, we use four leadership-class supercomputers, Aurora, Frontier, Perlmutter, and Polaris, each as an FL client, performing local model training on its assigned data. We use a CPU-only cluster at Argonne National Laboratory, Improv, as the central server, coordinating global model aggregation.

We distribute samples to clients by the task groups: Perlmutter handles samples from the four name conversion tasks, Polaris manages samples from the six property prediction tasks, Aurora focuses on samples from the two chemical reaction tasks, and Frontier covers samples from the two molecule description tasks. This partitioning creates a natural non-IID data distribution across clients, mirroring real-world scenarios where different institutions possess specialized knowledge and proprietary data in specific subdomains, such as pharmaceutical companies with drug discovery data, research labs with synthesis expertise, and academic centers with molecular property datasets. The details of the instruction tuning dataset, SMolInstruct, and its distribution to the supercomputers are presented in Table 1.

- Table 1: We distribute the 3.3M SMolInstruct training data samples across four facilities and group them by task group as follows. Refer to Yu et al. [55] for more details on the tasks and samples.


Samples Task Group HPC Task Per Task Per Group

IUPAC to molecular formula 304,490

IUPAC to SMILES 304,379 SMILES to molecular formula 304,379 SMILES to IUPAC 304,379

Name Conversion Perlmutter

1,217,627

ESOL(Water Solubility) 1,111

Lipo (Octanol/Water Distribution Coefficient) 4,200 BBBP (Blood-Brain Barrier Penetratio) 1,962 ClinTox (Toxicity to Human Body) 1,431 HIV (HIV Replication Inhibition) 41,075 SIDER (Side Effects of Drugs) 28,540

Property Prediction Polaris

78,319

Molecule captioning 60,305

Molecule Description Frontier

120,565 Molecule generation 60,260

Forward synthesis 977,920

Chemical Reaction Aurora

1,925,903 Retrosynthesis 947,983

Overall 3,342,414

#### 2.2 FL Configurations

We conduct two sets of experiments to evaluate our framework under different operational conditions. First, we utilize HPC reservations of 64 nodes at each of the four supercomputers to enable co-scheduling, where all systems execute synchronously, a common approach in distributed computing [12]. This approach eliminates unpredictable queueing delays and supports large-scale deployment. Under these co-scheduled conditions, we focus on a single synchronous FL algorithm (FedAvg [38]) because the absence of queueing uncertainty allows us to tune local training parameters based on preliminary computational capability estimates at each supercomputer, effectively eliminating stragglers and ensuring synchronized global aggregation. This controlled configuration isolates the performance characteristics of FL at scale from the effects of scheduling variability, enabling us to demonstrate and assess the upper bound of cross-facility FL performance when computational heterogeneity can be proactively managed.

Second, we conduct experiments without reservations, where each client job enters the standard scheduling queue before running local training. For this scenario, we deploy a smaller configuration of two nodes per supercomputer, which is more accessible in the presence of queueing delays and scheduling randomness. This

setup allows us to systematically benchmark four FL algorithms, FedAvg [38], FedAsync [52], FedBuff [39], and FedCompass [32], under heterogeneous queueing policies, scheduling behaviors, and computational capabilities across facilities. These algorithms represent different synchronization paradigms in FL: FedAvg follows a fully synchronous aggregation scheme, FedAsync and FedBuff adopt asynchronous updates, and FedCompass leverages a semi-asynchronous design using a computational power-aware scheduler to balance staleness tolerance and coordination. This dual experimental design allows us to assess both the optimized performance potential of cross-facility FL under co-scheduled conditions and its algorithmic robustness under real-world HPC constraints.

#### 2.3 Scalability and Throughput

We evaluate throughput performance across the four supercomputers with configurations detailed in Table 2. Throughput is measured as average samples processed per second during one-hour runs, with experiments scaling from one to 64 nodes. To ensure a fair comparison of raw computational capability, all supercomputers train on the same dataset rather than their assigned task partitions, isolating throughput differences to hardware and configuration rather than data distribution.

For each supercomputer, we follow the recommended optimization flags and system-specific configurations provided by the operating facilities, meaning different supercomputers employ different settings. This is intentional, as we are comparing the best achievable performance at each site rather than enforcing a uniform configuration. Polaris and Frontier additionally leverage AWS OFI NCCL/RCCL [1] plugins that enable high-performance collective communication over fabric interfaces such as Slingshot.

Figure 1 reveals dramatic heterogeneity in both absolute throughput and scaling efficiency. Aurora achieves the highest throughput, reaching over 2,100 samples per second at 64 nodes with nearly linear scaling throughout. Perlmutter 80GB and Frontier achieve approximately 1,200 and 1,000 samples per second respectively at maximum scale, while Polaris and Perlmutter 40GB both plateau around 250 samples per second.

The performance disparity reflects a fundamental trade-off driven by GPU memory capacity. Smaller memory GPUs require aggressive memory optimization strategies such as DeepSpeed ZeRO-3 [42,43], which achieve memory efficiency at the cost of increased communication overhead. Larger memory GPUs avoid this penalty by using less communication-intensive approaches such as ZeRO-1. This is most clearly illustrated by Perlmutter’s two configurations: the 40GB variant must employ ZeRO-3 and achieves only 250 samples per second, while the 80GB variant uses ZeRO-1 and reaches 1,200 samples per second, an over four-fold difference attributable entirely to the memory-driven optimization trade-off.

When viewed by total GPU count rather than node count, these scaling patterns remain consistent, confirming that memory capacity and the resulting optimization strategy are the primary drivers of observed heterogeneity. This variation, from 250 samples per second for memory-constrained configurations to over 2,100 for Aurora, underscores a critical challenge for cross-facility FL: facilities exhibit qualitatively different scaling behaviors that make computational capability-aware algorithms like FedCompass essential. Naive approaches that treat all clients equally result in severe load imbalance, with faster clients waiting on slower clients in synchronous settings, or slower clients’ contributions being overwhelmed in asynchronous settings.

- Table 2: Configurations for throughput scaling experiments. GPU memory capacity largely determines the required DeepSpeed ZeRO optimization stage: supercomputers with smaller memory GPUs must employ ZeRO-3, which achieves memory efficiency at the cost of increased inter-GPU communication overhead, while supercomputers with larger memory GPUs can use the less communication-intensive ZeRO-1. Micro batch size is set per GPU and held fixed across node counts.


##### Supercomputer GPU architecture GPU memory DeepSpeed stage Micro batch size

Polaris NVIDIA A100 40GB ZeRO-3 6 Perlmutter NVIDIA A100 40GB ZeRO-3 6 Perlmutter NVIDIA A100 80GB ZeRO-1 16 Aurora Intel Max 1550 Series 64GB ZeRO-1 8 Frontier AMD MI250X 64GB ZeRO-1 12

![image 1](Li et al._2026_Scalable Cross-Facility Federated Learning for Scientific Foundation Models on Multiple Supercompute_images/imageFile1.png)

- Figure 1: Throughput scaling with fixed micro-batch size per GPU. The left panel shows throughput (samples per second) as a function of node count, while the right panel shows the same results as a function of total GPU count. The consistent scaling patterns across both panels confirm that memory capacity and the resulting optimization strategy, rather than node or GPU count alone, are the primary drivers of throughput heterogeneity across supercomputers.

2.4 Training Performance

We evaluate the training performance under the two experiment configurations mentioned previously: largescale co-scheduled deployment (64 nodes per supercomputer starting synchronously using reservations) and small-scale queued deployment (two nodes per supercomputer with algorithm comparison). All experiments evaluate models on all 14 tasks across the dataset, even for local client models, to demonstrate knowledge transfer from clients to server without requiring data movement. Our experiments focus on demonstrating a functional cross-facility FL framework rather than training to full convergence; accordingly, we conduct eight global (synchronous) rounds for the 64-node experiment and distribute 40 total local training rounds across clients for the two-node comparison. Model evaluation is performed on a fixed subset of the test set using standard evaluation protocols with deterministic random seeds to ensure fair comparison across experiments.

- 2.4.1 Large-Scale Co-Scheduled Deployment


- Figure 2 presents the training dynamics observed for FedAvg across all four supercomputers under coscheduled conditions with 64 nodes per supercomputer, utilizing over 1,700 GPUs in total. Hardware specifications are shown in Table 3. We tune local training steps at each supercomputer based on throughput measurements from our scaling study in Section 2.3, targeting approximately 40 minutes per local training round including initialization and computational overhead. This tuning ensures near-simultaneous completion across the supercomputers.


This experiment demonstrates the fundamental functioning of FL at scale, with the global model loss decreasing consistently and monotonically from 1.39 to 0.37 over eight aggregation rounds, confirming that the framework successfully orchestrates collaborative learning across distributed supercomputers. The results inform four general observations.

First, the global model, represented by the purple line, consistently achieves the lowest test loss throughout training, demonstrating that the federated aggregation successfully integrates knowledge across the distributed, domain-specialized datasets. This validates that our framework enables effective cross-facility collaborative learning without raw data centralization.

Second, all individual client models exhibit higher test loss when evaluated on all tasks compared to the global model, with notable variance across clients. This behavior reflects the client drift phenomenon [27,30]: as each client trains exclusively on its specialized domain subset (with 64 nodes enabling more samples per local training round), local models optimize toward domain-specific patterns that may not generalize well

to the full task distribution. Polaris and Aurora, handling property prediction and chemical reaction tasks respectively, show particularly high losses on the full evaluation set, underscoring their specialization.

Third, the consistent performance ordering across supercomputers reveals interesting patterns about task transferability. Perlmutter, despite handling only name conversion tasks (conversions between IUPAC, SMILES, and Molecular Formula), achieves the lowest test losses on the full evaluation. Name conversion tasks require broad knowledge of molecular representations that underlies much of chemistry, which naturally limits local model drift. Conversely, Aurora exhibits higher losses from chemical reaction tasks, indicating that synthesis and retrosynthesis reasoning is highly specialized and less generalizable. Polaris, with the smallest total sample count distributed across six diverse property prediction tasks (solubility, toxicity, blood-brain barrier permeability, HIV inhibition, ClinTox, and SIDER), shows the highest losses, reflecting the effect of limited samples available for this task group. This ordering persists across training, suggesting fundamental differences in how knowledge from different chemistry domains contributes to the federated model.

Fourth, despite different computational characteristics and task distributions, all clients demonstrate consistent downward loss trajectories, with the global model maintaining steady improvement. The synchronized nature of co-scheduled training is evident in the smooth, regular updates across all clients.

![image 2](Li et al._2026_Scalable Cross-Facility Federated Learning for Scientific Foundation Models on Multiple Supercompute_images/imageFile2.png)

- Figure 2: FedAvg test loss over eight global aggregation rounds using 64 nodes per supercomputer (client). The global model (purple) consistently achieves the lowest test loss across all 14 tasks, decreasing from 1.39 to 0.37, while local client models show higher losses reflecting specialization to their assigned task groups.


- Table 3: Hardware specifications for the 64-node large-scale co-scheduled experiment. Aurora and Frontier’s higher total GPU counts result in substantially larger effective batch sizes compared to Polaris and Perlmutter. Polaris operated with 63 nodes due to a single node failure during the reservation.


##### Facility GPU architecture Nodes Total GPUs Effective batch size

Polaris NVIDIA A100 63 (1 node failure) 252 1512 Perlmutter NVIDIA A100 40GB 64 256 1536 Aurora Intel Max 1550 Series 64 768 6144 Frontier AMD MI250X 64 512 4096

##### 2.4.2 Small-Scale Algorithm Comparison

We next examine results from two-node experiments without HPC reservations, comparing FedAvg, FedAsync, FedBuff, and FedCompass, under heterogeneous queueing conditions, where each local training job enters the standard scheduling queue of the corresponding HPC facility. Table 4 details the hardware specifications,

showing the same per-GPU batch size as the large-scale co-scheduled deployment. The four algorithms handle heterogeneity in training completion times differently: FedAvg must wait for all clients to complete each round before aggregation, making it sensitive to stragglers. FedAsync allows clients to update the global model independently, tolerating delays at the clients. FedBuff aggregates updates in batches, offering a middle ground between synchrony and flexibility. FedCompass adapts local training steps to individual computational throughput, enabling more balanced contributions across heterogeneous clients. All algorithms perform 40 total local training rounds distributed across clients, with initial local training steps set proportional to sample size in the assigned task groups, creating inherent heterogeneity in training completion times. Table 5 shows the resulting distribution of training rounds per client: FedAvg distributes rounds evenly due to its synchronous aggregation requirement, while asynchronous algorithms produce uneven distributions driven by each client’s computational speed and queue behavior, with FedCompass partially counteracting this imbalance through its adaptive step adjustment.

Figure 3 compares the loss progression of the local models at each client and the aggregated global model from the four algorithms. To ensure a fair comparison, all algorithms are evaluated within the same wallclock time budget of 17,000 seconds, allowing us to assess convergence efficiency under real-world uncertain queue conditions. In each panel, a data point for a client model appears when that client completes a local training round, while a data point for the global model marks a global aggregation event. The four algorithms exhibit distinct behaviors under these conditions.

In particular, within the given wall-clock time budget, FedCompass achieves the best global model performance with a final test loss of 0.4345, representing improvements of 4.5% upon FedAvg, 19.3% upon FedAsync, and 12.9% upon FedBuff, respectively. FedBuff outperforms FedAsync by moderating the impact of stragglers through buffered aggregation. Across all algorithms, the global model consistently outperforms individual local models on the full task evaluation test set, reinforcing that FL successfully transfers knowledge across domain-specialized datasets.

Examining client trajectories reveals further distinctions. FedAvg shows the most consistent client convergence, with all clients following smooth downward trajectories that closely track the global model. Individual local models maintain similar loss values throughout training with minimal divergence. FedAsync and FedBuff produce notably erratic client behavior, particularly for Polaris and Aurora, whose loss trajectories oscillate significantly even as the global model improves steadily. FedCompass displays the most volatile individual client behavior, with pronounced oscillations across clients, due to its adaptive step adjustments. Despite this volatility, FedCompass’ global model achieves the largest overall improvement, ultimately reaching the lowest final loss among all algorithms.

These results highlight a key insight: algorithms that explicitly account for computational heterogeneity outperform those that merely tolerate asynchrony. FedAsync and FedBuff reduce the impact of stragglers but treat all clients as roughly equivalent contributors, which can bias the global model toward faster clients’ data distributions. FedCompass’ superior performance demonstrates that proactively adapting to known computational differences yields better outcomes. However, FedCompass does not yet model queue time variability or system-specific scheduling policies, suggesting a clear avenue for further improvement.

- Table 4: Hardware specifications for the two-node small-scale experiment. Same as the 64-node setup, Aurora and Frontier’s higher multi-GPU-per-node architectures result in larger effective batch sizes relative to Polaris and Perlmutter despite the same node count.


##### Facility GPU architecture Nodes Total GPUs Effective batch size

Polaris NVIDIA A100 2 8 48 Perlmutter NVIDIA A100 40GB 2 8 48 Aurora Intel Max 1550 Series 2 24 192 Frontier AMD MI250X 2 16 128

#### 2.5 Globus Transfer Communication

When using FL to train large models with billions of parameters, communication overhead becomes an increasingly important factor and can emerge as a significant performance bottleneck, particularly in cross-

- Table 5: Distribution of local training rounds across four clients for each algorithm over 40 total rounds. FedAvg distributes rounds evenly due to its synchronous aggregation requirement. Asynchronous algorithms produce uneven distributions driven by each client’s computational speed and queue behavior.


##### Algorithm Total Polaris Aurora Frontier Perlmutter

FedAvg 40 10 10 10 10 FedAsync 40 11 6 14 9 FedCompass 40 11 9 11 9 FedBuff 40 8 5 17 10

![image 3](Li et al._2026_Scalable Cross-Facility Federated Learning for Scientific Foundation Models on Multiple Supercompute_images/imageFile3.png)

- Figure 3: Test loss progression of four FL algorithms under realistic queueing conditions using two nodes per facility. Each panel shows local client models alongside the global aggregated model within the same wall-clock time budget of 17,000 seconds. FedCompass achieves the lowest final global test loss, while FedAvg produces the most stable client trajectories.


![image 4](Li et al._2026_Scalable Cross-Facility Federated Learning for Scientific Foundation Models on Multiple Supercompute_images/imageFile4.png)

- Figure 4: Globus Transfer communication efficiency across clients for five models ranging from OPT-125m to Llama2-13b. Panel a shows the linear relationship between model parameters and storage size in BF16 format. Panel b shows transfer speed versus model size, with Aurora and Polaris achieving the highest speeds due to co-location with the server at Argonne. Panel c summarizes average transfer speeds over all five models per destination facility.


facility deployments where large model parameters must be transferred across geographically distributed HPC facilities. To quantify this cost, we analyze the efficiency of transferring LLMs across clients using Globus Transfer, with all transfers originating from the server to the four clients. We evaluate five models ranging from OPT-125m to Llama2-13b in BF16 format. For a comprehensive review of Globus Transfer and its performance characteristics, we refer readers to [57].

Figure 4 presents three views of transfer performance. Panel a demonstrates the linear relationship between model parameters and storage requirements, scaling from approximately 250 MB for 125 million parameters to 26 GB for 13 billion parameters. Panels b and c reveal how transfer speeds vary significantly across both clients and model sizes.

Model size significantly impacts transfer efficiency, with speeds increasing substantially from the smallest to the largest models, indicating that larger transfers better amortize connection establishment overhead and benefit more from high-bandwidth local networks. Aurora and Polaris demonstrate the strongest scaling behavior, improving more than 10-fold in transfer speed from OPT-125m to Llama2-13b, while Perlmutter exhibits slightly weaker scaling.

Aurora and Polaris consistently achieve the highest transfer speeds, which we attribute to co-location: both the server and ALCF destinations (hosting Aurora and Polaris) reside at Argonne National Laboratory, enabling transfers over high-bandwidth local networks. Table 6 confirms this co-location advantage quantitatively: Aurora and Polaris exhibit sub-millisecond round-trip latency to the server, compared to 17ms for Frontier and 45ms for Perlmutter, directly reflecting the difference between intra-campus and wide-area network paths.

- Table 6: Round-trip latency (ms) between the server and each client, measured via ping over 20 rounds. Aurora and Polaris exhibit sub-millisecond latency due to co-location with the server at Argonne National Laboratory, while Frontier and Perlmutter face substantially higher wide-area network latency.


##### Destination Min Avg Max Mean Dev.

Aurora (ALCF) 0.122 0.266 0.432 0.094 Polaris (ALCF) 0.112 0.210 0.342 0.074 Frontier (OLCF) 17.236 17.281 17.321 0.167 Perlmutter (NERSC) 45.178 45.205 45.264 0.286

Notably, the performance gap between clients widens substantially with model size. For OPT-125m, speeds are comparable across all destinations, but for Llama2-13b the gap expands to nearly 200 MB/s. The weaker scaling at Perlmutter suggests that some wide-area network paths may be bandwidth-limited,

preventing large transfers from fully exploiting available link capacity. These findings have important implications for cross-facility FL and complement recent cross-silo communication-

compression efforts [56]. Transfer costs vary significantly by client location and model size, and speeds can be further influenced by temporal factors such as facility workload, time of day, and network congestion, introducing variability that FL algorithms must accommodate. In practical deployments, these heterogeneous transfer characteristics necessitate careful consideration of FL scheduling and aggregation strategies.

### 3 Discussion

We discuss related work and broader context situating our contributions, and two aspects informed by our results: practical considerations for future FL algorithm design on HPC infrastructure, and lessons learned from our cross-facility deployments.

#### 3.1 Related Work and Context

FL has matured across two broad deployment contexts [26]. Cross-device FL, exemplified by Google’s production systems [5], Meta’s Papaya [24], and Apple’s on-device personalization [40], targets large populations of resource-constrained devices. Cross-silo FL connects institutional participants with substantial compute, supported by frameworks including FATE [37], OpenFL [16], NVIDIA FLARE [46], FederatedScope [53], Flower [4], FedML [19], and Flight [25]. Our work employs APPFL [34,47], an open-source privacy-preserving FL framework designed for scalability across heterogeneous computing environments, which we extend to operate across geographically distributed HPC facilities.

FL algorithm development has addressed heterogeneity from multiple angles. FedProx [29] and SCAFFOLD [27] tackle statistical heterogeneity under non-IID data distributions. Asynchronous approaches including FedAsync [52] and FedBuff [39] reduce the impact of stragglers, while FedCompass [32] adapts local training steps to computational throughput. Hierarchical FL [36] and related multi-tier systems [8] organize aggregation to exploit network topology and mitigate heterogeneity. Adaptive server-side optimizers such as FedYogi and FedAdam [44] improve convergence under heterogeneous client datasets. However, none of these algorithms model batch job scheduling dynamics or wide-area communication variability, which are shown to be crucial factors in cross-HPC FL performance from our results.

Modern HPC facilities rely on job schedulers, such as SLURM [54], PBS [20], and Cobalt [15], to manage competing workloads through priority queues and backfilling. These schedulers are often designed for independent batch jobs rather than iterative federated workloads. Multi-site workflow systems including Condor [17], Pegasus [14], and StreamFlow [11] coordinate distributed scientific computations but lack FL’s iterative synchronization requirements. Predictive scheduling [18] and performance variability analysis [22] inform the understanding of HPC dynamics but have not been applied to FL. Large-scale distributed training frameworks including DeepSpeed with ZeRO optimization and communication primitives from Horovod [48] provide the foundation for local training at each facility, with gradient compression techniques such as PowerSGD [51] further relevant for bandwidth-constrained wide-area settings.

FL is increasingly applied across scientific domains where data sensitivity or sovereignty prevents centralization. Medical imaging [45,49] and pharmaceutical research through MELLODDY [21] demonstrate collaborative model development across institutions. Power grid applications present a particularly compelling case: foundation models for electrical load prediction and AC optimal power flow have demonstrated strong performance [6,31], and federated training enables collaboration without sharing operational data [7]. Light source facilities face similar challenges, generating massive imaging datasets where competing scientific interests necessitate federated approaches. Model pruning techniques [3] and their federated variants [2] represent an emerging direction for enabling FL participants with heterogeneous computational capabilities to collaborate on large model development. These applications share a common need for the cross-HPC facility FL infrastructure our work provides.

#### 3.2 Practical FL Algorithm Design

Our systematic comparison reveals that while existing FL algorithms demonstrate the feasibility of crossfacility collaborative training, significant algorithmic innovation remains necessary for production-ready FL

on HPC infrastructure. An ideal FL algorithm for geographically distributed HPC environments must address multiple dimensions of heterogeneity simultaneously, including computational capability, queue and scheduling dynamics, and network topology, rather than optimizing for any single factor in isolation.

While FedCompass’ success in adapting to computational heterogeneity provides a strong foundation, future algorithms must extend this principle to incorporate queue-aware scheduling. Waiting in a queue effectively removes the client from participation regardless of its processing speed, making queue dynamics

- as important as computational throughput. To investigate the significance of queueing delays, we analyze historical queue data from Polaris obtained


from ACLF. Figure 5 presents these results. Historical analysis shows that large allocations (64+ nodes) face median wait times exceeding 100 hours with high variability, explaining why our large-scale experiments required advance reservations.

The temporal variability we observed, where transfer speeds and throughput fluctuate with facility workload and network congestion, further necessitates algorithms that maintain running performance estimates and adapt aggregation strategies accordingly.

The substantial communication cost differences across geographically distributed facilities additionally motivate hierarchical aggregation strategies that exploit geographic locality, aggregating models within colocated facilities before exchanging updates across expensive wide-area links.

Adaptive synchronization that dynamically adjusts between synchronous and bounded-asynchronous modes based on observed heterogeneity could combine FedAvg’s convergence quality under favorable conditions with FedAsync’s resilience to stragglers.

Addressing the client drift observed under aggressive local training, where client models diverged more in large-scale configurations, further requires mechanisms such as control variates from SCAFFOLD [27] or other drift-correcting updates to maintain global model coherence.

The convergence of these principles, queue awareness, temporal robustness, hierarchical communication, and drift mitigation, defines the frontier for next-generation HPC FL algorithms. These insights align with and extend recent practical experiences in building FL systems [35], which similarly emphasize the importance of system-aware algorithm design for real-world deployments.

![image 5](Li et al._2026_Scalable Cross-Facility Federated Learning for Scientific Foundation Models on Multiple Supercompute_images/imageFile5.png)

- Figure 5: Polaris queue time with varying number of nodes and walltime requested. Solid lines represent the mean queue wait time and shaded regions represent one standard deviation. Different queues are designed to handle jobs with different characteristics in order to maximize supercomputer utilization. Each queue imposes its own constraints on the maximum number of nodes requestable, the maximum walltime allowed, and the allocation of available node-hours.


#### 3.3 Lessons Learned

Our deployment across four DOE supercomputers yields several concrete lessons for future cross-facility FL deployments. We organize these around four areas: infrastructure, algorithms, communication and scaling, and operations.

Infrastructure. Globus provides a strong foundation for authentication, authorization, and data transfer, and its broad deployment across research computing facilities means new participants can join a federation without requiring new infrastructure. However, each facility generally requires users to set up their own Globus Compute endpoints and authenticate using facility-specific credentials, and not all facilities currently allow transfer and computation to be triggered by credentials from external institutions. Multi-user Globus Compute endpoints remain limited in deployment. Standardized interfaces for job submission, monitoring, and failure recovery across heterogeneous HPC schedulers exist in various forms but lack broad deployment, generally requiring custom engineering per site.

Algorithms. We observe in our experiments that queue times can affect significantly clients’ local trainings and their contributions to the global model, yet no existing FL algorithm explicitly models or adapts to scheduling dynamics. FedCompass’ computational adaptation improves over naive approaches, but future algorithms must jointly optimize for compute speed, queue behavior, and network topology. Client drift under non-IID partitioning remains a core challenge, especially in real-world FL across diverse scientific institutions which may encounter extreme heterogeneity, and at large node counts where more local updates amplify local model drift before aggregation.

Communication and scaling. Our results motivate hierarchical aggregation that exploits geographic locality. Larger models improve per-byte transfer efficiency but increase absolute synchronization costs linearly, eventually making frequent aggregation prohibitive without update compression or less frequent synchronization. At very large scales within a single supercomputer, intra-node communication during local training may become a bottleneck, particularly if distributed training frameworks are not optimized for the specific network topology or hardware architecture of the HPC systems.

Operational sustainability. Securing large reservations (64+ nodes) across multiple HPC systems simultaneously required extensive advance coordination with supercomputer operators, a process that does not scale. Smaller queue-based deployments are more accessible but introduce unpredictable delays. Dedicated FL scheduling infrastructure, or a shift to fully asynchronous algorithms that eliminate co-scheduling requirements, will be necessary for production deployments.

Despite these challenges, our work demonstrates that cross-facility FL with HPC systems is an achievable reality, with clear pathways forward through both algorithmic innovation and systems engineering investment to address the heterogeneity, coordination, and operational complexities inherent in production deployments

- at scale.


### 4 Methods

We describe the methods underlying our cross-facility FL deployment, covering the APPFL framework, the DOE supercomputer infrastructure, and the orchestration tools that enable coordinated training across facilities.

#### 4.1 APPFL and DOE Supercomputers

APPFL (Advanced Privacy-Preserving Federated Learning) is an open-source software framework whose development is led by researchers from Argonne National Laboratory. APPFL is designed to address heterogeneity and security challenges in FL environments [34]. The framework features a modular architecture comprising six core technical components: Aggregator, Scheduler, Trainer, Privacy, Communicator, and Compressor, all with user-friendly interfaces for customization and extensibility. APPFL supports both synchronous and asynchronous aggregation strategies, incorporates robust privacy-preserving mechanisms including differential privacy and secure aggregation, and provides comprehensive solutions for various FL paradigms, including vertical, hierarchical, and decentralized configurations. APPFL’s extensible design enables researchers to implement, test, and validate novel FL algorithms while facilitating real-world deployment across diverse computational infrastructures, making it an ideal foundation for the heterogeneous, security-conscious environments characteristic of scientific HPC deployments.

The four DOE supercomputers used in this study represent some of the world’s most advanced HPC systems, each with distinct architectures and operational policies. ALCF Polaris, located at Argonne National Laboratory, features 560 nodes with each node equipped with one AMD EPYC processor and four

NVIDIA A100 GPUs, connected via HPE Slingshot 11 networking and managed by the PBS scheduler. Also at Argonne, ALCF Aurora represents an exascale system with over 9000 nodes, each containing two Intel Xeon Max processors and six Intel Data Center GPU Max 1550 Series accelerators (equivalently 12 GPUs), interconnected through HPE Slingshot 11 networking and employing the PBS scheduler optimized for exascale computing and AI workloads. OLCF Frontier, hosted at Oak Ridge National Laboratory, is an exascale system with over 9400 nodes, each featuring one AMD EPYC processor and four AMD MI250X Graphics Compute Die (eight logical GPUs) connected through HPE Slingshot 11, and operates under a customized SLURM scheduler with complex queue structures designed for diverse scientific workloads. NERSC Perlmutter, based at Lawrence Berkeley National Laboratory, comprises a heterogeneous configuration with over 1500 GPU nodes (each with four NVIDIA A100 GPUs) and over 3000 CPU-only nodes, managed by SLURM with fair share scheduling policies and specialized queues tailored to different workload types.

These systems differ not only in hardware specifications but also in software environments, job submission interfaces, allocation policies, and operational schedules, creating unique challenges for executing coordinated FL workloads across facilities.

#### 4.2 Orchestration Tools

- Figure 6 shows the overall architecture of our cross-facility framework. We employ Globus Compute [10] to submit local training jobs to distributed HPC clients. As Globus Compute imposes a 10 MB data transfer limit, which is inadequate for transferring model parameters and training metadata of modern machine learning tasks, we integrate Globus Transfer, which provides high-throughput and reliable data movement capabilities.


More specifically, we employ ProxyStore [41] to orchestrate Globus transfers directly from application code. ProxyStore is a pass-by-reference system that enables transparent object movement across distributed environments by replacing large data objects with lightweight proxies that automatically resolve to the actual data when accessed. This design decision enables automated, seamless integration within our FL workflow while maintaining fine-grained control over data movement timing and destination management. It also enables use of the dedicated data transfer nodes [9, 13] supported by many HPC systems, ensuring that data movement activities do not interfere with computational workloads and providing consistent transfer performance across the distributed infrastructure.

We leverage DeepSpeed, a distributed training framework that provides multiple levels of parallelism essential for modern large-scale machine learning tasks. Specifically, our current implementation uses distributed data parallelism and ZeRO optimization stages, which collectively address two critical computational challenges: efficient utilization of multiple GPU resources for parallel data processing and memory optimization for large model accommodation. The ZeRO optimization stages enable controlled parameter and optimizer state offloading to CPU memory, thereby allowing models such as Llama2-7B to be trained or fine-tuned within the memory constraints of individual GPU devices where they would otherwise be infeasible. Furthermore, adopting DeepSpeed allows for future expansion of parallelism capabilities.

DeepSpeed’s default process launcher, pdsh, is typically unavailable on DOE HPC clusters; we therefore adopt the MPI protocol for parallel job launching, accomplished through the Globus MPI Engine. This engine restricts function execution to MPI and shell-based operations rather than standard Python function calls, which would normally allow direct transfer of function arguments and return values. To overcome this, we introduce a three-engine architecture. A client-side Globus Compute Engine manages local staging of proxied model parameters, training configurations, and metadata from the server, ensuring all training artifacts are available to the MPI Engine before training begins. Following local training, a server-side Globus Compute Engine collects and stages proxied client model parameters and metadata for retrieval during aggregation. Together, these three engines enable efficient coordination of training and aggregation across distributed HPC facilities.

### 5 Conclusion

We have demonstrated the feasibility and characterized the performance of FL across four DOE leadershipclass supercomputers, as a representative case of more general cross-facility FL of heterogeneous HPC systems. Our experiments reveal substantial heterogeneity in computational throughput, communication costs,

![image 6](Li et al._2026_Scalable Cross-Facility Federated Learning for Scientific Foundation Models on Multiple Supercompute_images/imageFile6.png)

Figure 6: Overall implementation of the cross-facility FL framework. The FL server (blue) comprises a Server Agent handling aggregation and scheduling, and a Server Communicator using Globus Compute and ProxyStore for model exchange. The FL client (yellow) comprises a Client Agent running the Trainer and DeepSpeed via a Globus Compute MPI Engine, and a Client Communicator mirroring the serverside communication components. Model parameters are transferred between server and clients via Globus Transfer.

and queueing dynamics across these systems: heterogeneities that existing FL algorithms do not adequately address. Our comparison of algorithms under realistic HPC conditions shows that while computational capability adaptation improves performance, future algorithms must simultaneously account for queue-aware scheduling and temporal variability to achieve practical production deployments. This work establishes both the infrastructure and empirical foundation necessary to enable privacy-preserving collaborative machine learning across geographically distributed scientific institutions, opening pathways for FL applications in domains where data sensitivity, institutional policies, or sheer data scale have previously prevented collaborative model development.

### Acknowledgment

This work was supported by the U.S. Department of Energy, Office of Science, Advanced Scientific Computing Research, under Contract DE-AC02-06CH11357. We gratefully acknowledge the computing resources provided on Improv, a high-performance computing cluster operated by the Laboratory Computing Resource Center at Argonne National Laboratory. An award of computer time was provided by the ASCR Leadership Computing Challenge (ALCC) program. This research used resources of the Argonne Leadership Computing Facility, which is a U.S. Department of Energy Office of Science User Facility operated under contract DE-AC02-06CH11357. This research used resources of the Oak Ridge Leadership Computing Facility at the Oak Ridge National Laboratory, which is supported by the Office of Science of the U.S. Department of Energy under Contract No. DE-AC05-00OR22725. This research used resources of the National Energy Research Scientific Computing Center (NERSC), a Department of Energy User Facility using NERSC award ALCC-ERCAP0038201.

### References

- [1] Amazon Web Services. AWS OFI NCCL: AWS libfabric plugin for NCCL and RCCL, 2025. Accessed: 2026-02-19.
- [2] Guangji Bai, Yijiang Li, Zilinghan Li, Kibaek Kim, and Liang Zhao. FedSpaLLM: Federated pruning of large language models. In Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics:, volume 1, 2025.
- [3] Guangji Bai, Yijiang Li, Chen Ling, Kibaek Kim, and Liang Zhao. SparseLLM: Towards global pruning of pre-trained language models. In Advances in Neural Information Processing Systems, volume 38, 2024.
- [4] Daniel J. Beutel, Taner Topal, Akhil Mathur, Xinchi Qiu, Javier Fernandez-Marques, Yan Gao, Lorenzo Sani, Kwing Hei Li, Titouan Parcollet, Pedro Porto Buarque de Gusm˜o, and Nicholas D. Lane. Flower: A friendly federated learning research framework. Preprint arXiv:2007.14390, 2022.
- [5] Keith Bonawitz, Hubert Eichner, Wolfgang Grieskamp, Dzmitry Huba, Alex Ingerman, Vladimir Ivanov, Chloe Kiddon, Jakub Koneˇcny´, Stefano Mazzocchi, H. Brendan McMahan, Timon Van Overveldt, David Petrou, Daniel Ramage, and Jason Roselander. Towards federated learning at scale: System design. In Proceedings of Machine Learning and Systems, volume 1, pages 374–388. MLSys, 2019.
- [6] Shourya Bose, Yijiang Li, Amy Van Sant, Yu Zhang, and Kibaek Kim. From RNNs to foundation models: An empirical study on commercial building energy consumption. Preprint arXiv:2411.14421, 2024.
- [7] Shourya Bose, Yu Zhang, and Kibaek Kim. Privacy-preserving load forecasting via personalized model obfuscation. Preprint arXiv:2312.00036, 2023.
- [8] Zheng Chai, Yujing Chen, Ali Anwar, Liang Zhao, Yue Cheng, and Huzefa Rangwala. FedAT: A high-performance and communication-efficient federated learning system with asynchronous tiers. In Proceedings of the international conference for high performance computing, networking, storage and analysis, pages 1–16, 2021.
- [9] Kyle Chard, Eli Dart, Ian Foster, David Shifflett, Steven Tuecke, and Jason Williams. The Modern Research Data Portal: A design pattern for networked, data-intensive science. PeerJ Computer Science, 4:e144, 2018.
- [10] Ryan Chard, Yadu Babuji, Zhuozhao Li, Tyler Skluzacek, Anna Woodard, Ben Blaiszik, Ian Foster, and Kyle Chard. FuncX: A federated function serving fabric for science. In Proceedings of the 29th International symposium on high-performance parallel and distributed computing, pages 65–76, 2020.
- [11] Iacopo Colonnelli, Robert Birke, Giulio Malenza, Gianluca Mittone, Alberto Mulone, Jeroen Galjaard, Lydia Y Chen, Sanzio Bassini, Gabriella Scipione, Jan Martinoviˇc, et al. Cross-facility federated learning. Procedia Computer Science, 240:3–12, 2024.
- [12] Karl Czajkowski, Ian Foster, Carl Kesselman, Volker Sander, and Steven Tuecke. SNAP: A protocol for negotiating service level agreements and coordinating resource management in distributed systems. In Workshop on Job Scheduling Strategies for Parallel Processing, pages 153–183. Springer, 2002.
- [13] Eli Dart, Lauren Rotman, Brian Tierney, Mary Hester, and Jason Zurawski. The Science DMZ: A network design pattern for data-intensive science. In Proceedings of the International Conference on High Performance Computing, Networking, Storage and Analysis, pages 1–10, 2013.
- [14] Ewa Deelman, Karan Vahi, Gideon Juve, Mats Rynge, Scott Callaghan, Philip J Maechling, Rajiv Mayani, Weiwei Chen, Rafael Ferreira Da Silva, Miron Livny, and Kent Wenger. Pegasus: A workflow management system for science automation. Future Generation Computer Systems, 46:17–35, 2015.


- [15] Narayan Desai. Cobalt: An open source platform for HPC system software research. In Edinburgh BG/L System Software Workshop, pages 803–820, 2005. https://ftp.mcs.anl.gov/pub/cobalt/papers/ cobalt-epcc-10-05.pdf.
- [16] Patrick Foley, Micah J Sheller, Brandon Edwards, Sarthak Pati, Walter Riviera, Mansi Sharma, Prakash Narayana Moorthy, Shih-han Wang, Jason Martin, Parsa Mirhaji, Prashant Shah, and Spyridon Bakas. Openfl: the open federated learning library. Physics in Medicine &amp; Biology, 67(21):214001, October 2022.
- [17] James Frey, Todd Tannenbaum, Miron Livny, Ian Foster, and Steven Tuecke. Condor-G: A computation management agent for multi-institutional grids. Cluster Computing, 5(3):237–246, 2002.
- [18] Ana Gainaru, Guillaume Aupy, Anne Benoit, Franck Cappello, Yves Robert, and Marc Snir. Scheduling the I/O of HPC applications under congestion. In IEEE International Parallel and Distributed Processing Symposium, pages 1013–1022, 2015.
- [19] Chaoyang He, Songze Li, Jinhyun So, Xiao Zeng, Mi Zhang, Hongyi Wang, Xiaoyang Wang, Praneeth Vepakomma, Abhishek Singh, Hang Qiu, et al. FedML: A research library and benchmark for federated machine learning. arXiv preprint arXiv:2007.13518, 2020.
- [20] Robert L. Henderson. Job scheduling under the Portable Batch System. In Job Scheduling Strategies for Parallel Processing, pages 279–294, Berlin, Heidelberg, 1995. Springer Berlin Heidelberg.
- [21] Wouter Heyndrickx, Lewis Mervin, Tobias Morawietz, No´e Sturm, Lukas Friedrich, Adam Zalewski, Anastasia Pentina, Lina Humbeck, Martijn Oldenhof, Ritsuya Niwayama, Peter Schmidtke, Nikolas Fechner, Jaak Simm, Adam Arany, Nicolas Drizard, Rama Jabal, Arina Afanasyeva, Regis Loeb, Shlok Verma, Simon Harnqvist, Matthew Holmes, Balazs Pejo, Maria Telenczuk, Nicholas Holway, Arne Dieckmann, Nicola Rieke, Friederike Zumsande, Djork-Arn´e Clevert, Michael Krug, Christopher Luscombe, Darren Green, Peter Ertl, Peter Antal, David Marcus, Nicolas Do Huu, Hideyoshi Fuji, Stephen Pickett, Gergely Acs, Eric Boniface, Bernd Beck, Yax Sun, Arnaud Gohier, Friedrich Rippmann, Ola Engkvist, Andreas H G¨ller, Yves Moreau, Mathieu N Galtier, Ansgar Schuffenhauer, and Hugo Ceulemans. MELLODDY: Cross-pharma federated learning at unprecedented scale unlocks benefits in qsar without compromising proprietary information. Journal of chemical information and modeling, 64(7):2331–2344, 2024.
- [22] Torsten Hoefler and Roberto Belli. Scientific benchmarking of parallel computing systems: Twelve ways to tell the masses when reporting performance results. SC’15: International Conference for High Performance Computing, Networking, Storage and Analysis, 2015.
- [23] Chao Huang, Jianwei Huang, and Xin Liu. Cross-silo federated learning: Challenges and opportunities. Preprint arXiv:2206.12949, 2022.
- [24] Dzmitry Huba, John Nguyen, Kshitiz Malik, Ruiyu Zhu, Mike Rabbat, Ashkan Yousefpour, Carole-Jean Wu, Hongyuan Zhan, Pavel Ustinov, Harish Srinivas, Kaikai Wang, Anthony Shoumikhin, Jesik Min, and Mani Malek. Papaya: Practical, private, and scalable federated learning. In Proceedings of Machine Learning and Systems, volume 4, pages 922–939. MLSys, 2022.
- [25] Nathaniel Hudson, Valerie Hayot-Sasson, Yadu Babuji, Matt Baughman, J Gregory Pauloski, Ryan Chard, Ian Foster, and Kyle Chard. Flight: A FaaS-based framework for complex and hierarchical federated learning. Future Generation Computer Systems, 174:107998, 2026.
- [26] Peter Kairouz, H. Brendan McMahan, Brendan Avent, Aur´elien Bellet, Mehdi Bennis, Arjun Nitin Bhagoji, Kallista Bonawitz, Zachary Charles, Graham Cormode, Rachel Cummings, Rafael G. L. D’Oliveira, Hubert Eichner, Salim El Rouayheb, David Evans, Josh Gardner, Zachary Garrett, Adri` Gasc´n, Badih Ghazi, Phillip B. Gibbons, Marco Gruteser, Zaid Harchaoui, Chaoyang He, Lie He, Zhouyuan Huo, Ben Hutchinson, Justin Hsu, Martin Jaggi, Tara Javidi, Gauri Joshi, Mikhail Khodak, Jakub Konecˇny´, Aleksandra Korolova, Farinaz Koushanfar, Sanmi Koyejo, Tancre`de Lepoint, Yang Liu, Prateek Mittal, Mehryar Mohri, Richard Nock, Ayfer Ozgu¨r,¨ Rasmus Pagh, Mariana Raykova,


- Hang Qi, Daniel Ramage, Ramesh Raskar, Dawn Song, Weikang Song, Sebastian U. Stich, Ziteng Sun, Ananda Theertha Suresh, Florian Tram`er, Praneeth Vepakomma, Jianyu Wang, Li Xiong, Zheng Xu, Qiang Yang, Felix X. Yu, Han Yu, and Sen Zhao. Advances and open problems in federated learning. Foundations and trends® in machine learning, 14(1–2):1–210, 2021.
- [27] Sai Praneeth Karimireddy, Satyen Kale, Mehryar Mohri, Sashank Reddi, Sebastian Stich, and Ananda Theertha Suresh. SCAFFOLD: Stochastic controlled averaging for federated learning. In International Conference on Machine Learning, pages 5132–5143. PMLR, 2020.
- [28] Kibaek Kim, Krishnan Raghavan, Olivera Kotevska, Matthieu Dorier, Ravi Madduri, Minseok Ryu, Todd Munson, Rob Ross, Thomas Flynn, Ai Kagawa, Byung-Jun Yoon, Christian Engelmann, and Farzad Yousefian. Privacy-preserving federated learning for science: Challenges and research directions. In 2024 IEEE International Conference on Big Data (BigData), page 7849–7853. IEEE, December 2024.
- [29] Tian Li, Anit Kumar Sahu, Manzil Zaheer, Maziar Sanjabi, Ameet Talwalkar, and Virginia Smith. Federated optimization in heterogeneous networks. In Proceedings of Machine Learning and Systems, volume 2, pages 429–450, 2020.
- [30] Xiang Li, Kaixuan Huang, Wenhao Yang, Shusen Wang, and Zhihua Zhang. On the convergence of fedavg on non-iid data. In International Conference on Learning Representations, 2020.
- [31] Yijiang Li, Zeeshan Memon, Hongwei Jin, Stefano Fenu, Keunju Song, Sunash B Sharma, Parfait Gasana, Hongseok Kim, Liang Zhao, and Kibaek Kim. LUMINA: Foundation models for topology transferable ACOPF. Preprint arXiv:2603.04300, 2026.
- [32] Zilinghan Li, Pranshu Chaturvedi, Shilan He, Han Chen, Gagandeep Singh, Volodymyr Kindratenko, Eliu A Huerta, Kibaek Kim, and Ravi Madduri. FedCompass: Efficient cross-silo federated learning on heterogeneous client devices using a computing power aware scheduler. In The International Conference on Learning Representations, 2024.
- [33] Zilinghan Li, Shilan He, Pranshu Chaturvedi, Volodymyr Kindratenko, Eliu A Huerta, Kibaek Kim, and Ravi Madduri. Secure federated learning across heterogeneous cloud and high-performance computing resources: A case study on federated fine-tuning of LLaMA 2. Computing in Science & Engineering, 26(3):52–58, 2024.
- [34] Zilinghan Li, Shilan He, Ze Yang, Minseok Ryu, Kibaek Kim, and Ravi Madduri. Advances in APPFL: a comprehensive and extensible federated learning framework. In IEEE 25th International Symposium on Cluster, Cloud and Internet Computing (CCGrid), pages 103–113. IEEE, May 2025.
- [35] Zilinghan Li, Aditya Sinha, Yijiang Li, Kyle Chard, Kibaek Kim, and Ravi Madduri. Experiences building enterprise-level privacy-preserving federated learning to power AI for science. Preprint arXiv:2511.08998, 2025.
- [36] Lumin Liu, Jun Zhang, S H Song, and Khaled B Letaief. Client-edge-cloud hierarchical federated learning. In IEEE International Conference on Communications, pages 1–6. IEEE, 2020.
- [37] Yang Liu, Tao Fan, Tianjian Chen, Qian Xu, and Qiang Yang. FATE: An industrial grade platform for collaborative learning with data protection. Journal of Machine Learning Research, 22(226):1–6, 2021.
- [38] Brendan McMahan, Eider Moore, Daniel Ramage, Seth Hampson, and Blaise Aguera y Arcas. Communication-efficient learning of deep networks from decentralized data. In Proceedings of the Twentieth International Conference on Artificial Intelligence and Statistics, volume 54 of Proceedings of Machine Learning Research. PMLR, 2017.
- [39] John Nguyen, Kshitiz Malik, Hongyuan Zhan, Ashkan Yousefpour, Mike Rabbat, Mani Malek, and Dzmitry Huba. FedBuff: Federated learning with buffered asynchronous aggregation. In Proceedings of the Twenty-fifth International Conference on Artificial Intelligence and Statistics, volume 151 of Proceedings of Machine Learning Research. PMLR, 2022.


- [40] Matthias Paulik, Matt Seigel, Henry Mason, Dominic Telaar, Joris Kluivers, Rogier van Dalen, Chi Wai Lau, Luke Carlson, Filip Granqvist, Chris Vandevelde, Sudeep Agarwal, Julien Freudiger, Andrew Byde, Abhishek Bhowmick, Gaurav Kapoor, Si Beaumont, Aine´ Cahill, Dominic Hughes, Omid Javidbakht, Fei Dong, Rehan Rishi, and Stanley Hung. Federated evaluation and tuning for on-device personalization: System design & applications. Preprint arXiv:2102.08503, 2021.
- [41] J Gregory Pauloski, Valerie Hayot-Sasson, Logan Ward, Alexander Brace, Andr´e Bauer, Kyle Chard, and Ian Foster. Object proxy patterns for accelerating distributed applications. IEEE Transactions on Parallel and Distributed Systems, 36(2):253–265, 2025.
- [42] Samyam Rajbhandari, Jeff Rasley, Olatunji Ruwase, and Yuxiong He. ZeRO: Memory optimizations toward training trillion parameter models. SC20: International Conference for High Performance Computing, Networking, Storage and Analysis, pages 1–16, 2020.
- [43] Jeff Rasley, Samyam Rajbhandari, Olatunji Ruwase, and Yuxiong He. DeepSpeed: System optimizations enable training deep learning models with over 100 billion parameters. Proceedings of the 26th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining, pages 3505–3506, 2020.
- [44] Sashank Reddi, Zachary Charles, Manzil Zaheer, Zachary Garrett, Keith Rush, Jakub Koneˇcny`, Sanjiv Kumar, and H Brendan McMahan. Adaptive federated optimization. In International Conference on Learning Representations, 2021.
- [45] Nicola Rieke, Jonny Hancox, Wenqi Li, Fausto Milletari, Holger R. Roth, Shadi Albarqouni, Spyridon Bakas, Mathieu N Galtier, Bennett A Landman, Klaus Maier-Hein, Sebastien Ourselin, Micah Sheller, Ronald M. Summers, Andrew Trask, Daguang Xu, Maximilian Baust, and M. Jorge Cardoso. The future of digital health with federated learning. NPJ Digital Medicine, 3(119), 2020.
- [46] Holger R. Roth, Yan Cheng, Yuhong Wen, Isaac Yang, Ziyue Xu, Yuan-Ting Hsieh, Kristopher Kersten, Ahmed Harouni, Can Zhao, Kevin Lu, Zhihong Zhang, Wenqi Li, Andriy Myronenko, Dong Yang, Sean Yang, Nicola Rieke, Abood Quraini, Chester Chen, Daguang Xu, Nic Ma, Prerna Dogra, Mona Flores, and Andrew Feng. NVIDIA FLARE: Federated learning from simulation to real-world. Preprint arXiv:2210.13291, 2022.
- [47] Minseok Ryu, Youngdae Kim, Kibaek Kim, and Ravi K. Madduri. APPFL: Open-source software framework for privacy-preserving federated learning. In IEEE International Parallel and Distributed Processing Symposium Workshops (IPDPSW), pages 1074–1083. IEEE, May 2022.
- [48] Alexander Sergeev and Mike Del Balso. Horovod: Fast and easy distributed deep learning in TensorFlow. Preprint arXiv:1802.05799, 2018.
- [49] Micah J Sheller, Brandon Edwards, G Anthony Reina, Jason Martin, Sarthak Pati, Aikaterini Kotrotsou, Mikhail Milchenko, Weilin Xu, Daniel Marcus, Rivka R Colen, and Spyridon Bakas. Federated learning in medicine: Facilitating multi-institutional collaborations without sharing patient data. Scientific Reports, 10(12598), 2020.
- [50] Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert, Amjad Almahairi, Yasmine Babaei, Nikolay Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti Bhosale, Dan Bikel, Lukas Blecher, Cristian Canton Ferrer, Moya Chen, Guillem Cucurull, David Esiobu, Jude Fernandes, Jeremy Fu, Wenyin Fu, Brian Fuller, Cynthia Gao, Vedanuj Goswami, Naman Goyal, Anthony Hartshorn, Saghar Hosseini, Rui Hou, Hakan Inan, Marcin Kardas, Viktor Kerkez, Madian Khabsa, Isabel Kloumann, Artem Korenev, Punit Singh Koura, Marie-Anne Lachaux, Thibaut Lavril, Jenya Lee, Diana Liskovich, Yinghai Lu, Yuning Mao, Xavier Martinet, Todor Mihaylov, Pushkar Mishra, Igor Molybog, Yixin Nie, Andrew Poulton, Jeremy Reizenstein, Rashi Rungta, Kalyan Saladi, Alan Schelten, Ruan Silva, Eric Michael Smith, Ranjan Subramanian, Xiaoqing Ellen Tan, Binh Tang, Ross Taylor, Adina Williams, Jian Xiang Kuan, Puxin Xu, Zheng Yan, Iliyan Zarov, Yuchen Zhang, Angela Fan, Melanie Kambadur, Sharan Narang, Aurelien Rodriguez, Robert Stojnic, Sergey Edunov, and Thomas Scialom. Llama 2: Open foundation and fine-tuned chat models. Preprint arXiv:2307.09288, 2023.


- [51] Thijs Vogels, Sai Praneeth Karimireddy, and Martin Jaggi. PowerSGD: Practical low-rank gradient compression for distributed optimization. In Advances in Neural Information Processing Systems, volume 32, 2019.
- [52] Cong Xie, Sanmi Koyejo, and Indranil Gupta. Asynchronous federated optimization. Preprint arXiv:1903.03934, 2020.
- [53] Yuexiang Xie, Zhen Wang, Dawei Gao, Daoyuan Chen, Liuyi Yao, Weirui Kuang, Yaliang Li, Bolin Ding, and Jingren Zhou. FederatedScope: A flexible federated learning platform for heterogeneity. Proceedings of the VLDB Endowment, 16(5):1059–1072, 2023.
- [54] Andy B. Yoo, Morris A. Jette, and Mark Grondona. SLURM: Simple Linux utility for resource management. In Workshop on Job Scheduling Strategies for Parallel Processing, pages 44–60. Springer, 2003.
- [55] Botao Yu, Frazier N. Baker, Ziqi Chen, Xia Ning, and Huan Sun. LlaSMol: Advancing large language models for chemistry with a large-scale, comprehensive, high-quality instruction tuning dataset. In First Conference on Language Modeling, 2024.
- [56] Zhaorui Zhang, Sheng Di, Kai Zhao, Sian Jin, Dingwen Tao, Zhuoran Ji, Benben Liu, Khalid Ayed Alharthi, Jiannong Cao, and Franck Cappello. FedCSpc: A cross-silo federated learning system with error-bounded lossy parameter compression. IEEE Transactions on Parallel and Distributed Systems, 2025.
- [57] Weijian Zheng, Jack Kordas, Tyler J Skluzacek, Raj Kettimuthu, and Ian Foster. Globus service enhancements for exascale applications and facilities. The International Journal of High Performance Computing Applications, 38(6):658–670, 2024.


|The submitted manuscript has been created by UChicago Argonne, LLC, Operator of Argonne National Laboratory (“Argonne”). Argonne, a U.S. Department of Energy Office of Science laboratory, is operated under Contract No. DE-AC02-06CH11357. The U.S. Government retains for itself, and others acting on its behalf, a paid-up nonexclusive, irrevocable worldwide license in said article to reproduce, prepare derivative works, distribute copies to the public, and perform publicly and display publicly, by or on behalf of the Government. The Department of Energy will provide public access to these results of federally sponsored research in accordance with the DOE Public Access Plan (http://energy.gov/downloads/doe-public-access-plan).|
|---|


