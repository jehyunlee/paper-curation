# AutoP2C: An LLM-Based Agent Framework for Code Repository Generation from Multimodal Content in Academic Papers

> **저자**: Zijie Lin, Yiqing Shen, Qilin Cai, He Sun, Jinrui Zhou, Mingjun Xiao | **날짜**: 2025-04-28 | **Journal**: arXiv | **Link**: [https://arxiv.org/abs/2504.20115](https://arxiv.org/abs/2504.20115)

---

## Essence

We introduce ``Paper-to-Code'' (P2C), a novel task that transforms the multimodal content of scientific publications into fully executable code repositories, which extends beyond the existing formulation of code generation that merely converts textual descriptions into isolated code snippets. To automate the P2C process, we propose AutoP2C, a multi-agent framework based on large language models that processes both textual and visual content from research papers to generate complete code repositories.

## Motivation

- **배경**: We introduce ``Paper-to-Code'' (P2C), a novel task that transforms the multimodal content of scientific publications into fully executable code repositories, which extends beyond the existing formulation of code generation that merely converts textual descriptions into isolated code snippets.
- **Gap**: However, translating these multimodal elements into executable code remains a challenging and time-consuming process that requires substantial ML expertise.

## Achievement

1. Machine Learning (ML) research is spread through academic papers featuring rich multimodal content, including text, diagrams, and tabular results.
2. Evaluation on a benchmark of eight research papers demonstrates the effectiveness of AutoP2C, which can successfully generate executable code repositories for all eight papers, while OpenAI-o1 or DeepSeek-R1 can only produce runnable code for one paper.

## How

- To automate the P2C process, we propose AutoP2C, a multi-agent framework based on large language models that processes both textual and visual content from research papers to generate complete code repositories.
- Specifically, AutoP2C contains four stages: (1) repository blueprint extraction from established codebases, (2) multimodal content parsing that integrates information from text, equations, and figures, (3) hierarchical task decomposition for structured code generation, and (4) iterative feedback-driven debugging to ensure functionality and performance.

## Originality

- We introduce ``Paper-to-Code'' (P2C), a novel task that transforms the multimodal content of scientific publications into fully executable code repositories, which extends beyond the existing formulation of code generation that merely converts textual descriptions into isolated code snippets.

**Trigger-based extraction**: We introduce ``Paper-to-Code'' (P2C), a novel task that transforms the multimodal content of scientific publications into fully executable code repositories, which extends beyond the existing formulation of code generation that merely converts textual descriptions into isolated code snippets.. To automate the P2C process, we propose AutoP2C, a multi-agent framework based on large language models that processes both textual and visual content from research papers to generate complete code repositories.. Specifically, AutoP2C contains four stages: (1) repository blueprint extraction from established codebases, (2) multimodal content parsing that integrates information from text, equations, and figures, (3) hierarchical task decomposition for structured code generation, and (4) iterative feedback-driven debugging to ensure functionality and performance.. Evaluation on a benchmark of eight research papers demonstrates the effectiveness of AutoP2C, which can successfully generate executable code repositories for all eight papers, while OpenAI-o1 or DeepSeek-R1 can only produce runnable code for one paper.. The code is available at https://github.com/shoushouyu/Automated-Paper-to-Code.

## Limitation & Further Study

### 저자들이 언급한 한계

- Abstract에서 명시적 한계 언급 없음

### 후속 연구

- 해당 연구의 확장 및 다른 도메인 적용 가능성 탐구

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 5/5 |
| Technical Soundness | 4/5 |
| Significance | 5/5 |
| Clarity | 4/5 |
| Overall | 4/5 |

**총평**: AutoP2C: An LLM-Based Agent Framework for Code Repository Generation from Multimodal Content in Academic Papers은(는) evaluation on a benchmark of eight research papers demonstrates the effectiveness of autop2c, which can successfully generate executable code repositories for all eight papers, while openai-o1 or deepseek-r1 can only produce runnable code for one paper을 보여주는 연구이다.
