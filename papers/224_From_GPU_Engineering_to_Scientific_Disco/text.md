20 March 2026

# From GPU Engineering to Scientific Discovery: Parallelism Techniques for Large Language Models

Emmanuel A Olanrewaju

Abstract

Large language models have become a transformative tool in both artificial intelligence research and scientific discovery, enabling automated analysis, hypothesis generation, and knowledge synthesis across disciplines such as chemistry, biology, and materials science. However, the increasing size and complexity of these models create significant computational and memory demands, making efficient training and deployment a critical challenge. This article provides a comprehensive survey of parallelism techniques for large language models, including data parallelism, tensor parallelism, sequence parallelism, context parallelism, pipeline parallelism, and expert parallelism. We discuss how these strategies improve scalability and resource utilization, offering practical guidance for designing models that can handle the demands of scientific applications. By combining advances in GPU engineering, optimized training algorithms, and parallel computing frameworks, researchers can effectively leverage LLMs to accelerate scientific discovery while minimizing computational cost. This work serves as both a reference and a roadmap for developing efficient, high performance models tailored to AI driven scientific research.

Posted on 20 March 2026 — CC-BY 4.0 — This is a preprint and has not been peer reviewed. Data may be preliminary. — https:// doi.org/10.26434/chemrxiv.15001091/v1

## From GPU Engineering to Scientific Discovery: Parallelism Techniques for Large Language Models

Emmanuel A. Olanrewaju

### Abstract

Large language models have become a transformative tool in both artificial intelligence research and scientific discovery, enabling automated analysis, hypothesis generation, and knowledge synthesis across disciplines such as chemistry, biology, and materials science. However, the increasing size and complexity of these models create significant computational and memory demands, making efficient training and deployment a critical challenge. This article provides a comprehensive survey of parallelism techniques for large language models, including data parallelism, tensor parallelism, sequence parallelism, context parallelism, pipeline parallelism, and expert parallelism. We discuss how these strategies improve scalability and resource utilization, offering practical guidance for designing models that can handle the demands of scientific applications. By combining advances in GPU engineering, optimized training algorithms, and parallel computing frameworks, researchers can effectively leverage LLMs to accelerate scientific discovery while minimizing computational cost. This work serves as both a reference and a roadmap for developing efficient, high performance models tailored to AI driven scientific research.

##### I. INTRODUCTION

The rapid development of large language models has placed unprecedented computational demands on modern hardware, with graphical processing units emerging as the central platform for both training and inference. GPU engineering plays a critical role in enabling these models to scale efficiently, as it directly influences memory utilization, data movement, and parallel execution. Unlike traditional workloads, large language models require careful orchestration of thousands of cores, high bandwidth memory systems, and optimized communication pathways to sustain performance. As model sizes continue to grow, engineering strategies must address challenges such as latency, energy consumption, and numerical stability while maintaining high throughput.

Recent advances in GPU architecture and software frameworks have significantly improved the feasibility of deploying large language models in both research and production settings. Techniques such as tensor parallelism [1] [2], pipeline parallelism [3] [4], and data parallelism [5] [6] have been developed to maximize hardware efficiency and reduce bottlenecks. At the same time, compiler level optimizations and memory management strategies have become essential for handling the scale and complexity of these models.

Recent years have seen a rapid expansion in the application of artificial intelligence across scientific disciplines, including chemistry, physics, biology, and materials science [7] [8] [9]. Large language models have become increasingly valuable in this context due to their ability to process and generate scientific text, assist with hypothesis generation, and support data analysis workflows. In chemistry, for example, these models are being used to interpret experimental results, suggest reaction pathways, and accelerate literature review. This growing integration of language based models into scientific practice is reshaping how researchers interact with data and knowledge, enabling more automated and scalable approaches to discovery [10] [11].

However, the widespread adoption of large language models in scientific research introduces significant computational challenges, particularly in terms of training cost and resource efficiency. Training state of the art models requires extensive GPU resources, leading to high financial and energy costs that can limit accessibility and scalability. As a result, there is an increasing need for efficient training strategies that reduce computational overhead while preserving model performance. Advances in parallelism, memory optimization, and hardware aware algorithm design are essential to address these constraints, ensuring that the benefits of large language models can be realized broadly across the scientific community without prohibitive infrastructure demands.

The purpose of this article is to provide a comprehensive overview of the various parallelism techniques used in large language model design, including data parallelism, tensor parallelism, sequence parallelism, context parallelism, pipeline parallelism, and expert parallelism. These strategies are essential for efficiently scaling LLMs while managing computational cost and memory constraints. By systematically examining these techniques, this work highlights how they can be applied when designing models specifically for applications in scientific research, where high performance and resource efficiency are critical for handling large datasets and complex computations. The discussion serves as a practical guide for researchers and engineers seeking to implement optimized architectures for AI driven scientific discovery.

##### II. OVERVIEW OF PARALLELISM TECHNIQUES

Large language models demand substantial computational resources for both training and inference, making parallelism essential for efficiency and scalability. In this section, we review the main parallelism strategies employed in LLM design, including data parallelism, tensor parallelism, sequence parallelism, context parallelism, pipeline parallelism, and expert parallelism. Each technique addresses specific challenges in memory usage, computational throughput, and scalability across multiple GPUs. All computations and experimental evaluations in this study were performed on GPUs via Runpod [12].

A. Data Parallelism

Data parallelism (DP) involves replicating the entire model on multiple GPUs and splitting input data across devices. Each GPU computes gradients independently, which are then synchronized. This technique is simple to implement and effective for scaling across many GPUs, though it may be limited by communication overhead during gradient synchronization.

For data parallelism, we conducted a series of experiments to benchmark different configurations. The Single GPU (Baseline) scenario involves standard training on one GPU without any communication overhead. The DP Naive (non-interleaved) configuration uses four GPUs, performing a full forward and backward pass on each device, followed by a blocking AllReduce on all gradients, where computation and communication are separated into distinct phases. In the DP Interleaved setup, four GPUs are used as well, but during the backward pass, non-blocking AllReduce operations are triggered per layer as soon as the gradients are available, allowing communication to overlap with computation. Finally, the PyTorch DistributedDataParallel (DDP) configuration employs PyTorch’s builtin DDP, representing a production-grade interleaved data parallel approach with bucketed AllReduce. All computations were carried out on NVIDIA H100 GPUs.

![image 1](Olanrewaju_2026_From GPU Engineering to Scientific Discovery Parallelism Techniques for Large Language Models_images/imageFile1.png)

###### FIG. 1: Effects of different DP techniques on average epoch time.

![image 2](Olanrewaju_2026_From GPU Engineering to Scientific Discovery Parallelism Techniques for Large Language Models_images/imageFile2.png)

###### FIG. 2: Scaling Efficiency: Speedup over Single-GPU Baseline.

![image 3](Olanrewaju_2026_From GPU Engineering to Scientific Discovery Parallelism Techniques for Large Language Models_images/imageFile3.png)

###### FIG. 3: Loss Convergence across different DP techniques.

![image 4](Olanrewaju_2026_From GPU Engineering to Scientific Discovery Parallelism Techniques for Large Language Models_images/imageFile4.png)

FIG. 4: Throughput across different DP techniques.

As shown in Figs. 1, 2, 3, and 4, DP is most effective for very large models, where the increased number of layers provides more opportunities for overlapping computation and communication. In terms of convergence, all DP configurations exhibit similar behavior, indicating that parallelization does not adversely affect training stability. Furthermore, incorporating DP techniques improves throughput for larger models, enabling more efficient utilization of GPU resources as model size increases.

1. Zero Redundancy Optimizer (ZeRO)

This section presents a detailed overview of DeepSpeed ZeRO (Zero Redundancy Optimizer), a widely adopted technique for training large language models that do not fit entirely in the memory of a single GPU. In standard DistributedDataParallel (DDP), each GPU maintains a full copy of the model parameters, gradients, and optimizer states. For example, with eight GPUs, eight identical copies of the optimizer states exist, resulting in seven redundant copies. ZeRO addresses this inefficiency by partitioning (sharding) model states across GPUs, significantly reducing memory overhead.

ZeRO achieves this through multiple stages, each with progressively more aggressive sharding strategies:

- • ZeRO-0: Parameters, gradients, and optimizer states (including momentum, variance and master copies) are fully replicated on all GPUs.


- • ZeRO-1: Parameters and gradients remain fully replicated, but optimizer states are sharded across N GPUs, so each GPU stores only 1/N of the optimizer state.
- • ZeRO-2: Parameters remain fully replicated, gradients and optimizer states are sharded, reducing memory usage for both.
- • ZeRO-3: Parameters, gradients, and optimizer states are all sharded across GPUs, maximizing memory efficiency and enabling the training of extremely large models.


By distributing memory requirements in this manner, ZeRO allows training of models that would otherwise exceed the capacity of individual GPUs, while maintaining computational efficiency. However, the reduction in memory usage comes at the cost of increased communication overhead. In particular, ZeRO-3 incurs additional communication between GPUs, which can slow training, illustrating that lower memory footprint requires a trade-off with communication efficiency.

To demonstrate the impact of the Zero Redundancy Optimizer, experiments were conducted using two GPUs to fine-tune a language model (Pythia-6.9B) over 500 training steps. As shown in Fig. 5, ZeRO-3 reduces memory usage compared to ZeRO-2, but exhibits lower throughput due to increased communication overhead. Despite this trade-off, both ZeRO2 and ZeRO-3 achieve comparable training loss convergence. Figure 6 presents a decision framework for selecting the appropriate Zero Redundancy Optimizer (ZeRO) strategy based on model size and memory constraints, guiding practitioners on when to apply each variant effectively.

![image 5](Olanrewaju_2026_From GPU Engineering to Scientific Discovery Parallelism Techniques for Large Language Models_images/imageFile5.png)

FIG. 5: DeepSpeed ZeRO-2 and ZeRO-3 Comparison.

![image 6](Olanrewaju_2026_From GPU Engineering to Scientific Discovery Parallelism Techniques for Large Language Models_images/imageFile6.png)

FIG. 6: Decision Framework for Zero Redundancy Optimizer.

##### B. Tensor and Sequence Parallelism

1. Tensor Parallelism

Tensor Parallelism (TP) addresses a key limitation of ZeRO-3. While ZeRO-3 shards parameters, gradients, and optimizer states across GPUs, activations remain fully replicated on each device, leading to a significant memory bottleneck. In contrast, TP partitions the computation itself across multiple GPUs, which naturally reduces activation memory by a factor of 1/N, where N is the number of devices.

Importantly, TP is the only parallelism strategy that simultaneously reduces all major memory components: parameters, gradients, optimizer states, and activations. Unlike

data parallelism, which does not reduce latency, TP improves computational efficiency by distributing the workload, enabling faster execution.

By splitting parameters across N GPUs, TP reduces per-device parameter memory, freeing up space for larger key-value (KV) caches. This directly enables support for longer context windows, higher throughput, or increased numbers of concurrent users. Furthermore, TP also partitions the KV cache itself, enhancing memory efficiency during inference.

Finally, TP accelerates inference by reducing the size of matrix multiplications performed on each GPU. Each device processes smaller computations, leading to faster execution. The final result is then reconstructed through collective communication operations such as allreduce. TP can be implemented in two primary forms: column parallelism and row parallelism. In column parallelism, the weight matrix is partitioned along its output dimension, allowing each GPU to compute a subset of the output features independently before aggregation. In contrast, row parallelism partitions the weight matrix along its input dimension, requiring intermediate communication to combine partial results. These complementary approaches are often used together within transformer architectures to efficiently distribute both forward and backward computations across devices.

To demonstrate the impact of TP, we consider a standard transformer decoder with dmodel = 512, nheads = 8, dhead = 64, dff = 2048, nlayers = 6, and vocab_size = 10000, evaluated on two NVIDIA H100 GPUs. As shown in Figure 7, TP reduces the number of parameters per GPU, overall model memory consumption, and peak memory usage compared to the no-TP baseline.

![image 7](Olanrewaju_2026_From GPU Engineering to Scientific Discovery Parallelism Techniques for Large Language Models_images/imageFile7.png)

FIG. 7: Tensor Parallelism: Side-by-Side Comparison.

2. Sequence Parallelism

Sequence parallelism (SP) partitions activations and computations for components not covered by tensor parallelism—such as dropout, residual connections, and LayerNorm—along the input sequence dimension rather than the hidden dimension.

To demonstrate the combined effects of TP+SP, we use two NVIDIA H100 GPUs with a model configuration of dmodel = 1024, nheads = 16 (dhead = 64), dff = 4096, nlayers = 8, and vocab_size = 32000.

As shown in Figures 8 and 9, the introduction of TP+SP reduces the per-layer activation memory for LayerNorm, residual connections, and dropout. Note: SP should always be used in conjunction with TP.

![image 8](Olanrewaju_2026_From GPU Engineering to Scientific Discovery Parallelism Techniques for Large Language Models_images/imageFile8.png)

FIG. 8: TP and SP+TP: Side-by-Side Comparison.

![image 9](Olanrewaju_2026_From GPU Engineering to Scientific Discovery Parallelism Techniques for Large Language Models_images/imageFile9.png)

FIG. 9: Activation Size at Each Step Through a Transformer Block.

C. Context Parallelism

Attention memory scales as O(S2) with sequence length S, posing challenges for long sequences. To address this, we employ Context Parallelism (CP), splitting queries across multiple GPUs so that each GPU computes attention for only S/CP queries, reducing perGPU memory usage.

To further optimize attention computation, we combine CP with structured attention mechanisms:

- • Ring Attention: Queries attend only to a subset of neighboring keys arranged in a circular (ring) pattern. This reduces the effective attention computation from O(S2) to O(S · r), where r is the ring size, while preserving local context.
- • Zig-Zag Attention: Queries are grouped and attend to interleaved subsets of keys in a zig-zag pattern, enabling efficient long-range interactions with sub-quadratic memory scaling. This pattern can be combined with CP to further distribute computation across GPUs.


By integrating CP with ring and zig-zag attention, each GPU handles a reduced subset of queries while exploiting sparsity patterns in attention, achieving substantial memory savings without sacrificing accuracy.

To compare the effects of using CP and no CP, we define a transformer architecture with batch size B = 4, number of heads H = 16, and head dimension D = 64. Experiments

are conducted using two NVIDIA GeForce RTX 4090 GPUs across varying sequence lengths of S = 1024, 2048, and 4096. As shown in Fig. 10, employing CP reduces memory usage across all sequence lengths compared to the standard, non-parallel setup (No CP). By splitting the sequence across multiple GPUs, CP decreases per-GPU memory requirements, and increasing the degree of CP further amplifies savings in attention memory.

![image 10](Olanrewaju_2026_From GPU Engineering to Scientific Discovery Parallelism Techniques for Large Language Models_images/imageFile10.png)

FIG. 10: Context Parallelism: Performance Analysis.

D. Pipeline Parallelism

Pipeline parallelism (PP) is a technique that distributes a model’s layers across multiple GPUs to improve memory efficiency and computational scalability. For instance, consider a system with 12 GPUs: layers 1–5 could be assigned to GPU 1, layers 6–10 to GPU 2, and so on. By partitioning the model in this manner, each GPU only needs to store and process a subset of the model’s layers, which substantially reduces the memory requirements on individual GPUs while enabling efficient parallel execution.

To evaluate the impact of PP, we conduct experiments using four NVIDIA H100 GPUs. The model under consideration consists of 48 Transformer layers, with a hidden dimension of 1536 and 24 attention heads. It employs a vocabulary size of 32,000 tokens and operates on sequences of length 1024. Dropout is disabled (dropout = 0.0) to ensure consistent and noise-free benchmarking. The total model size is approximately 1.5 billion parameters.

As a baseline, the full 1.5B-parameter model is trained on a single GPU. For the pipelineparallel configuration, the same model is partitioned evenly across four GPUs using DeepSpeed’s PipelineModule, such that each GPU is responsible for roughly 375 million param-

eters (i.e., one quarter of the model).

DeepSpeed executes the pipeline using the 1F1B scheduling strategy (also known as PipeDream-Flush), which interleaves forward and backward passes across microbatches to maximize device utilization. Gradients are accumulated over multiple microbatches before performing an optimizer step, ensuring equivalence with standard data-parallel training while improving memory efficiency and throughput. As illustrated in Fig. 11, PP significantly reduces the memory footprint on each GPU while simultaneously achieving higher training throughput.

![image 11](Olanrewaju_2026_From GPU Engineering to Scientific Discovery Parallelism Techniques for Large Language Models_images/imageFile11.png)

FIG. 11: Baseline (1 GPU) vs Pipeline Parallelism (4 GPUs).

E. Expert Parallelism

To demonstrate expert parallelism, we construct a small language model (SLM) from scratch using the TinyStories dataset. TinyStories is a synthetic corpus of short narratives composed of vocabulary typically understood by children aged 3–4, generated using GPT-3.5 and GPT-4, and made available via HuggingFace.

The model architecture is configured with a vocabulary size of 50,257, a context length (block size) of 128 tokens, 6 Transformer layers, 6 attention heads, and an embedding dimension of 384. A dropout rate of 0.1 is applied during training. All experiments are conducted on a single NVIDIA H100 GPU.

We incorporate a Mixture-of-Experts (MoE) design to enable expert parallelism. The architecture consists of the following components:

- • Router: A lightweight linear layer that assigns a score to each expert for every token and selects the top-k experts.


- • SparseMoELayer: Routes tokens to their selected top-k experts, evaluates only those experts, and aggregates their outputs.
- • MoEBlock: A modified Transformer block in which the standard feedforward (MLP) layer is replaced by the SparseMoELayer.


#### This design enables conditional computation, where only a subset of experts is activated per token, thereby improving computational efficiency and scalability. As illustrated in Fig. 12, both the dense model and the Mixture-of-Experts (MoE) model exhibit similar trends in training and validation loss, indicating comparable learning dynamics. Additionally, the auxiliary load-balancing loss remains approximately uniform, suggesting that the experts are utilized in a balanced manner during training. Furthermore, Fig. 13 shows that expert utilization across layers follows a nearly uniform distribution. This behavior is desirable, as it prevents the model from over-relying on a small subset of experts within any given layer and promotes effective load balancing across all experts.

![image 12](Olanrewaju_2026_From GPU Engineering to Scientific Discovery Parallelism Techniques for Large Language Models_images/imageFile12.png)

FIG. 12: Validation Loss, Training Loss, and Auxiliary Loss across experts.

![image 13](Olanrewaju_2026_From GPU Engineering to Scientific Discovery Parallelism Techniques for Large Language Models_images/imageFile13.png)

FIG. 13: Expert Utilization per Layer.

##### III. CONCLUSION AND RECOMMENDATIONS

In this work, we have surveyed a range of parallelism strategies for scaling large language models, highlighting how techniques such as data, tensor, sequence, context, pipeline, and expert parallelism address the growing computational and memory challenges associated with modern architectures. Each method offers distinct advantages, and their combined use enables efficient training and deployment of increasingly large and capable models. Our discussion emphasizes that no single approach is universally optimal; rather, effective system design requires carefully balancing these techniques based on model size, hardware constraints, and application requirements.

The results and analysis presented in this article suggest several practical recommendations. First, practitioners should adopt hybrid parallelism strategies, combining complementary approaches such as tensor and pipeline parallelism to maximize hardware utilization. Second, memory efficiency should be prioritized through techniques such as pipeline partitioning and expert sparsity, particularly when working with limited GPU resources. Third, load balancing mechanisms, especially in expert parallelism, are critical to ensure stable training and avoid underutilization of computational capacity. Finally, leveraging mature frameworks such as DeepSpeed and Megatron LM can significantly simplify implementation while providing optimized performance.

In the context of AI for scientific applications, these considerations become even more important. As large language models and deep learning systems are increasingly deployed in production level scientific workflows, including drug discovery, materials design, and biological modeling, scalability and efficiency are no longer optional but essential. Designing models for science requires careful integration of parallelism techniques from the outset, ensuring that systems can handle large datasets, long contexts, and complex multimodal inputs while remaining computationally feasible. As the field continues to move toward larger and more specialized models, the effective use of parallelism will be a key enabler for translating research prototypes into reliable, real world scientific tools.

Looking forward, continued progress in GPU architectures, interconnect technologies, and distributed training frameworks will further enhance the scalability of large language models. Future research should focus on adaptive and dynamic parallelism strategies that can automatically adjust to workload characteristics, as well as methods that integrate

efficiency with robustness and interpretability. By following these guidelines, researchers can develop high performance, resource efficient models that unlock the full potential of large language models in accelerating scientific discovery.

Code Availability

The code is accessible at: https://github.com/Olanrewajuemmanuelabiodun/GPU_Engineering/ tree/main

Users may clone the repository to execute the provided Python scripts and Jupyter notebooks to fully reproduce all results presented in this study.

- [1] A. Dutt et al., Scaling state space models on multiple gpus with tensor parallelism, arXiv preprint arXiv:2602.21144 (2026).
- [2] I. Lamprecht et al., Tensor parallelism with partially synchronized activations, arXiv preprint arXiv:2506.19645 (2025).
- [3] P. Qi et al., Pipeline parallelism with controllable memory, in Advances in Neural Information Processing Systems, Vol. 37 (2024) pp. 46539–46566.
- [4] M. Qi et al., Synergistic tensor and pipeline parallelism, arXiv preprint arXiv:2510.27257

(2025).

- [5] C. J. Shallue et al., Measuring the effects of data parallelism on neural network training, Journal of Machine Learning Research 20, 1 (2019).
- [6] L. Fournier and E. Oyallon, Cyclic data parallelism for efficient parallelism of deep neural networks, arXiv preprint arXiv:2403.08837 (2024).
- [7] J. Wei et al., From ai for science to agentic science: A survey on autonomous scientific discovery, arXiv preprint arXiv:2508.14111 (2025).
- [8] D. P. Woodruff et al., Accelerating scientific research with gemini: Case studies and common techniques, arXiv preprint arXiv:2602.03837 (2026).
- [9] Q. Chen et al., Ai4research: A survey of artificial intelligence for scientific research, arXiv preprint arXiv:2507.01903 (2025).
- [10] Z. Song et al., Evaluating large language models in scientific discovery, arXiv preprint


- arXiv:2512.15567 (2025).
- [11] Y. Zhang et al., A comprehensive survey of scientific large language models and their applications in scientific discovery, in Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing (2024).
- [12] Runpod, Runpod: Gpu cloud for ai workloads (2026), accessed: 2026-03-18.


