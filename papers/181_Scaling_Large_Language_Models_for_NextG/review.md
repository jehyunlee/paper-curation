# Scaling Large Language Models for Next-Generation Single-Cell Analysis

> **저자**: Syed Asad Rizvi, Daniel Levine, Aakash Patel, Shiyang Zhang, Eric Wang, Curtis Jamison Perry, Ivan Vrkic, Nicole Mayerli Constante, Zirui Fu, Sizhuang He, David Zhang, Cerise Tang, Zhuoyang Lyu, Rayyan Darji, Chang Li, Emily Sun, David Jeong, Lawrence Zhao, Jennifer Kwan, David Braun, Brian Hafler, Hattie Chung, Rahul M. Dhodapkar, Paul Jaeger, Bryan Perozzi, Jeffrey Ishizuka, Shekoofeh Azizi, David Van Dijk | **날짜**: 2025-04-17 | **DOI**: 10.1101/2025.04.14.648850
> **리뷰 모드**: PDF

---

## Essence
In this work, we build upon the Cell2Sentence (C2S) framework, which represents scRNA-seq profiles as textual “cell sentences,” to train Large Language Models (LLMs) on a corpus comprising over one billion tokens of transcriptomic data, biological text, and metadata.

## Originality (Abstract 기반)
- [authorship, action] In this work, we build upon the Cell2Sentence (C2S) framework, which represents scRNA-seq profiles as textual “cell sentences,” to train Large Language Models (LLMs) on a corpus comprising over one billion tokens of transcriptomic data, biological text, and metadata.
- [action] Scaling the model to 27 billion parameters yields consistent improvements in predictive and generative capabilities and supports advanced downstream tasks that require synthesis of information across multi-cellular contexts.
- [continuation] Targeted fine-tuning with modern reinforcement learning techniques produces strong performance in perturbation response prediction, natural language interpretation, and complex biological reasoning.
- [action, result] This predictive strength enabled a dual-context virtual screen that nominated the kinase inhibitor silmitasertib (CX-4945) as a candidate for context-selective upregulation of antigen presentation.
- [finding, result] Experimental assessment in human cell models unseen during training supported this prediction, demonstrating that C2S-Scale can effectively guide the discovery of context-conditioned biology.
- [novelty, action, finding, result] C2S-Scale unifies transcriptomic and textual data at unprecedented scales, surpassing both specialized single-cell models and general-purpose LLMs to provide a platform for next-generation single-cell analysis and the development of “virtual cells.”

## 평가
| 항목 | 점수 (1-5) |
|------|-----------|
| Novelty | 4 |
| Technical Soundness | 3 |
| Overall | 4 |

**총평**: 높은 수준의 기여와 탄탄한 실험적 검증을 보여주는 연구.
