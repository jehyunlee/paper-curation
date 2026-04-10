---
title: "326_Exp-bench_Can_ai_conduct_ai_research_experiments_arXiv_prepr"
authors:
  - "Patrick Tser Jern Kon"
  - "Jiachen Liu"
  - "Xinyi Zhu"
  - "Qiuyi Ding"
  - "Jingjia Peng"
date: "2025"
doi: "arXiv:2505.24785"
arxiv: ""
score: 4.2
essence: "AI가 완전한 종료-대-종료(end-to-end) 연구 실험을 수행할 수 있는 능력을 체계적으로 평가하기 위해 EXP-Bench 벤치마크를 제시하며, NeurIPS/ICLR 논문 461개 작업에서 현재 AI 에이전트들이 0.5%의 완전 실험 성공률에 그치고 있음을 보였다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/Realistic_Discovery_Benchmarks"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/2025_Exp-bench Can ai conduct ai research experiments arXiv preprint arXiv2505.24785, 2025..pdf"
---

# Exp-bench: Can ai conduct ai research experiments? arXiv preprint arXiv:2505.24785, 2025.

> **저자**: Patrick Tser Jern Kon, Jiachen Liu, Xinyi Zhu, Qiuyi Ding, Jingjia Peng, Jiarong Xing, Yibo Huang, Yiming Qiu, Jayanth Srinivasa, Myungjin Lee, Mosharaf Chowdhury, Matei Zaharia, Ang Chen | **날짜**: 2025 | **DOI**: [arXiv:2505.24785](https://arxiv.org/abs/2505.24785)

---

## Essence

![Figure 1](figures/fig1.webp)
*EXP-Bench는 AI 에이전트가 동료 심사 논문에서 추출한 완전한 연구 실험을 수행할 수 있는지를 평가하는 벤치마크로, 연구 질문으로부터 가설 수립, 실험 설계, 구현, 실행, 결론 도출까지의 전체 과정을 평가한다.*

AI가 완전한 종료-대-종료(end-to-end) 연구 실험을 수행할 수 있는 능력을 체계적으로 평가하기 위해 EXP-Bench 벤치마크를 제시하며, NeurIPS/ICLR 논문 461개 작업에서 현재 AI 에이전트들이 0.5%의 완전 실험 성공률에 그치고 있음을 보였다.

## Motivation

- **Known**: 최근 AI 에이전트들이 문헌 합성(literature synthesis), 가설 생성(hypothesis generation), 코드 생성(code generation) 등 개별 작업에서는 능력을 보여주고 있다.

- **Gap**: 실증적 AI 연구는 엄밀한 종료-대-종료 실험을 요구하지만, 기존 벤치마크들(DSBench, ML-Agent-Bench, MLE-Bench 등)은 실험의 부분 요소만 평가하거나 단순화된 환경에서만 평가하며, 현실적인 전체 연구 워크플로우의 복잡성을 포착하지 못한다.

- **Why**: 자동화된 AI 연구는 과학 발전을 가속화할 수 있으며, 이를 위해 디지털 특성상 AI 연구는 LLM 기반 에이전트로 자동화하기에 특히 적합하다.

- **Approach**: 영향력 있는 동료 심사 논문과 오픈소스 구현에서 추출한 461개의 실제 AI 연구 작업으로 구성된 벤치마크를 제안하되, 논문과 코드에서 산재된 실험 세부사항을 추출하는 반자동화 파이프라인(semi-automated curation pipeline)을 개발한다.

## Achievement

![Figure 2](figures/fig2.webp)
*ICLR 2024 MogaNet 논문에서 추출한 단일 연구 작업의 예시로, 연구 질문, 고수준 방법 설명, 스타터 코드를 제공받는 형태를 보여준다.*

![Figure 3](figures/fig3.webp)
*EXP-Bench 데이터셋은 Deep Learning, Reinforcement Learning, Computer Vision, Generative Models 등 다양한 ML 연구 분야에서 균형잡힌 작업들로 구성되어 있으며, NeurIPS(53%)와 ICLR(47%)에서 추출되었다.*

1. **포괄적 벤치마크 구성**: NeurIPS/ICLR 2024의 51개 논문에서 461개의 연구 작업(12,737개 세분화된 부분 작업)을 추출하여, 컴퓨터 비전, NLP, 강화학습 등 다양한 AI 하위분야를 포함한 벤치마크 구축

2. **확장 가능한 반자동화 파이프라인**: 소스 선택/필터링 → 실험 절차 추출 → 구현 추출의 3단계로 논문과 코드베이스에서 산재된 세부정보를 체계적으로 추출하며, 실행 기반 검증으로 기능성을 보장

3. **심층 평가 분석**: 설계(design), 구현(implementation), 실행(execution), 결론(conclusion)의 4개 핵심 단계 평가를 통해 OpenHands와 IterativeAgent 등 최신 에이전트의 한계를 정량화:
   - 설계 정확도: 20-35%
   - 실행 가능한 완전 실험: 0.5%
   - 설계 변수 오분류: 16.1%
   - 필수 구현 요소 누락: 39.7%
   - 환경/의존성 오설정: 29.4%

## How

![Figure 4](figures/fig4.webp)
*EXP-Bench 반자동화 데이터셋 구축 파이프라인의 3단계 프로세스*

**Dataset Specification**:
- **문제 설명**: 연구 질문(research question), 고수준 방법(high-level method), 코드 저장소 접근성 제공
- **Ground Truth**: 실험 설계(design specification), 필수 코드 수정사항(git diff), 최종 결론(conclusion) 포함

**반자동화 구축 파이프라인**:

- **Stage 1 - 소스 선택**: 인용 횟수, GitHub 활동도(stars, forks) 등을 기준으로 영향력 있고 재현 가능한 논문 선별

- **Stage 2 - 실험 절차 추출**: 다중모달(multi-modal) 추출을 통해 논문, 보충자료, 코드에서 핵심 연구 문제 요소(주요 질문, 예상 결과, 데이터셋, 평가 지표, 모델 구성) 식별

- **Stage 3 - 구현 추출**: 관련 코드 위치 파악 및 작업을 해결하는 스크립트 조립, 실행 기반 검증으로 기능성 확인

**평가 메트릭**:
- 설계 정확도(design correctness)
- 구현 정확도(implementation correctness)
- 코드 실행 성공(code execution success)
- 결론의 타당성(conclusion validity)

## Originality

- **첫 종료-대-종료 평가**: 개별 작업이 아닌 완전한 연구 실험 수행 능력을 평가하는 첫 번째 벤치마크로, 설계부터 결론까지 전체 과학 프로세스를 포괄

- **반자동화 파이프라인**: 논문과 코드의 산재된 정보를 체계적으로 추출하는 새로운 방법론으로, 수작업 부담을 최소화하면서도 높은 충실도(high-fidelity) 유지

- **현실적 작업 소싱**: 이미 동료 심사를 거친 실제 영향력 있는 논문의 구체적인 실험을 기반으로 하여, 추상적 시뮬레이션이나 단순화된 환경이 아닌 실제 AI 연구 워크플로우 반영

- **대규모 다영역 커버리지**: 51개 논문에서 461개 작업을 구성하여, 기존 벤치마크(RE-Bench 7개, PaperBench 등)대비 훨씬 큰 규모와 다양성 확보

- **세분화된 부분과제**: 12,737개의 개별 채점 가능한 부분과제(subtask)로 각 단계별 상세한 성능 분석 가능

## Limitation & Further Study

- **자동화 정도의 한계**: 파이프라인이 "반자동화(semi-automated)"에 그쳐 여전히 인간의 검증 단계가 필요하며, 완전 자동화를 위한 추가 개선이 필요

- **논문 선택 편향**: NeurIPS/ICLR 2024의 오픈소스 코드가 있는 논문만 포함하여, 이론적 연구나 코드 미공개 논문의 다양한 실험 방식을 포함하지 못함

- **정적 Ground Truth의 한계**: 추출된 ground truth가 원본 논문의 특정 구현에 고정되어 있어, 동등하지만 다른 방식의 유효한 실험 설계는 인정하지 못할 가능성

- **재현성 문제**: 복잡한 소프트웨어 스택과 의존성 문제로 인해 실행 기반 검증이 작업 환경에 따라 다를 수 있음

- **후속 연구**: 
  - 더 오래되고 다양한 시간대의 논문 포함으로 장기적 트렌드 반영
  - 다중 유효 해법(multiple valid solutions)을 인정하는 평가 메트릭 개발
  - 에이전트 학습용 데이터셋으로의 활용으로 자동화된 AI 연구 에이전트 성능 향상
  - 더 정교한 설계 오류 분류 및 진단 도구 개발

## Evaluation

- **Novelty (독창성)**: 4.5/5
  - 종료-대-종료 AI 연구 실험 평가라는 새로운 문제 정의
  - 반자동화 파이프라인의 혁신적 접근
  - 다만, 개별 구성 요소(multi-modal extraction, code extraction)는 기존 기술 활용

- **Technical Soundness (기술 정확성)**: 4/5
  - 파이프라인 설계와 평가 메트릭이 논리적으로 일관성 있음
  - 실행 기반 검증으로 객관성 확보
  - 인간 검증 비용 분석 및 파이프라인의 정확도 수치가 제시되지 않은 점이 아쉬움

- **Significance (중요성)**: 4.5/5
  - AI 자동화 연구의 핵심 과제를 다루며, 미래 AI 에이전트 개발에 중요한 기준선 제시
  - 대규모 데이터셋(461개 작업)으로 실질적 학습 자원 제공
  - 현재 에이전트들의 구체적 한계(0.5% 완전 성공률)를 정량화하여 개선 방향 제시

- **Clarity (명확성)**: 4/5
  - 전체 구조와 동기가 명확하게 설명됨
  - 구체적 예시(MogaNet)와 통계치가 이해를 돕음
  - 파이프라인의 세부 단계별 입출력 형식이 더 자세히 기술될 필요가 있음

- **Overall (전체 평가)**: 4.2/5

**총평**: EXP-Bench는 AI 에이전트의 종료-대-종료 연구 실험 수행 능력을 처음으로 체계적으로 평가하는 중요한 벤치마크이며, 반자동화 파이프라인을 통해 대규모 고충실도 데이터셋을 구축한 점이 주목할 만하다. 다만 파이프라인의 자동화 정도와 다중 유효 해법 인정 메커니즘 개선이 향후 과제이다.

## Related Papers

- 🔄 다른 접근: [[papers/079_Ai_idea_bench_2025_Ai_research_idea_generation_benchmark/review]] — EXP-Bench의 완전한 실험 수행 능력 평가와 AI Idea Bench의 아이디어 생성 능력 평가는 AI 연구 역량을 서로 다른 단계에서 측정하는 보완적 접근이다.
- 🔗 후속 연구: [[papers/669_Researchbench_Benchmarking_llms_in_scientific_discovery_via/review]] — ResearchBench가 EXP-Bench의 실험 수행 평가를 더 광범위한 과학적 발견 과정으로 확장한 종합적 벤치마크이다.
- ⚖️ 반론/비판: [[papers/795_The_AI_Scientist_Towards_Fully_Automated_Open-Ended_Scientif/review]] — AI Scientist의 완전 자동화된 과학 발견 주장에 대해 EXP-Bench가 현재 AI 에이전트의 실제 실험 성공률 한계를 실증적으로 반박한다.
- 🔗 후속 연구: [[papers/177_Can_ai_agents_design_and_implement_drug_discovery_pipelines/review]] — Exp-bench의 AI 연구 실험 수행 평가가 Deep Thought의 신약 발견 연구 자동화 성능을 검증하는 도구로 활용됨
- 🔄 다른 접근: [[papers/079_Ai_idea_bench_2025_Ai_research_idea_generation_benchmark/review]] — AI Idea Bench의 아이디어 생성 평가와 EXP-Bench의 실험 수행 평가는 AI 연구 능력을 서로 다른 단계에서 측정하는 보완적 접근이다.
