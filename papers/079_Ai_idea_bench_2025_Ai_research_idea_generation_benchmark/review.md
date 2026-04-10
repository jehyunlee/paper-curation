---
title: "079_Ai_idea_bench_2025_Ai_research_idea_generation_benchmark"
authors:
  - "Yansheng Qiu"
  - "Haoquan Zhang"
  - "Zhaopan Xu"
  - "Ming Li"
  - "Diping Song"
date: "2025"
doi: "arXiv:2504.14191"
arxiv: ""
score: 4.2
essence: "대규모 언어 모델(LLM)의 AI 연구 아이디어 생성 능력을 정량적으로 평가하기 위해 3,495개의 AI 논문과 이를 영감준 논문들로 구성된 포괄적인 벤치마크 데이터셋 및 평가 프레임워크를 제시한다. 기존 평가 방식의 데이터 누수, 불완전한 ground truth, 제한된 실행 가능성 분석 문제를 해결한다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/AI-Powered_Research_Planning"
  - "topic/ai4s"
---

# AI Idea Bench 2025: AI 연구 아이디어 생성 벤치마크

> **저자**: Yansheng Qiu, Haoquan Zhang, Zhaopan Xu, Ming Li, Diping Song, Zheng Wang, Kaipeng Zhang | **날짜**: 2025 | **DOI**: [arXiv:2504.14191](https://arxiv.org/abs/2504.14191)

---

## Essence

![Figure 1](https://example.com/fig1.png)
*그림 1: 기존 아이디어 생성 파이프라인(a)과 제안된 AI Idea Bench 2025(b)의 비교. 본 연구는 목표 논문의 내용을 먼저 파악한 후 이를 ground truth로 활용하여 아이디어 평가에 참고자료를 제공한다.*

대규모 언어 모델(LLM)의 AI 연구 아이디어 생성 능력을 정량적으로 평가하기 위해 3,495개의 AI 논문과 이를 영감준 논문들로 구성된 포괄적인 벤치마크 데이터셋 및 평가 프레임워크를 제시한다. 기존 평가 방식의 데이터 누수, 불완전한 ground truth, 제한된 실행 가능성 분석 문제를 해결한다.

## Motivation

- **Known**: 최근 LLM들이 수학, 정리 증명, 코딩 등 과학 분야에서 인간 전문가를 능가하는 성능을 보이고 있으며, 이를 과학적 발견과 가설 생성(hypothesis generation)에 적용하려는 시도가 증가하고 있다.

- **Gap**: 기존 아이디어 생성 및 평가 방식은 세 가지 주요 문제점을 가지고 있다: (1) GPT-4o의 학습 데이터 cutoff 이후 논문을 활용하면서 data leakage 위험, (2) 제목과 초록만 평가하여 동기(motivation)와 실험 설계 같은 완전한 개념이 누락된 불완전한 ground truth, (3) prompt 설계 제약으로 인한 아이디어 실행 가능성(feasibility)의 정량적 평가 부족.

- **Why**: 과학 문헌의 복잡성과 증가하는 양, 빠른 기술 진화로 인해 연구자들이 신규 아이디어 발굴을 어려워하고 있으며, 자동화된 과학 발견(automated scientific discovery)의 필요성이 대두되고 있다.

- **Approach**: October 3, 2023 이후 발표된 AI 분야 상위 컨퍼런스(ICLR, CVPR, ECCV, NeurIPS, ICML, NAACL, EMNLP, ACL)의 3,495개 논문을 ground truth로 설정하고, 이들 논문을 영감준 선행 논문들의 내용을 이용하여 아이디어를 생성한 후, 두 가지 평가 방식(목표 논문과의 일치도, 참고자료 기반 평가)으로 비교 평가하는 포괄적 벤치마크 프레임워크 구축.

## Achievement

![Figure 2](https://example.com/fig2.png)
*그림 2: AI Idea Bench 2025의 전체 파이프라인. 목표 논문에서 동기, 실험 단계, 주제, 영감 논문을 추출한 후, 영감 논문에서 추출한 동기와 실험 단계를 결합하여 아이디어를 생성하고, 6가지 평가 지표로 아이디어 생성 방법들을 비교한다.*

1. **AI Idea Bench 2025 데이터셋 구축**: AI 관련 상위 컨퍼런스에서 2023년 10월 이후 발표된 3,495개의 영향력 있는 target 논문과 이를 영감준 motivating 논문들의 매칭된 쌍으로 구성된 체계적인 벤치마크 데이터셋 개발.

2. **포괄적 평가 프레임워크 제안**: (1) 생성된 아이디어와 ground truth 논문 내용의 일치도 평가 (2) 다른 참고 자료를 기반으로 한 referenced evaluation으로 혁신성과 실행 가능성 동시 평가하는 이중 평가 체계 수립.

3. **다양한 아이디어 생성 방법 벤치마킹**: 제안된 데이터셋과 평가 프레임워크를 활용하여 다양한 아이디어 생성 방법들의 효과를 포괄적으로 검증하고 비교 가능한 평가 체계 확립.

## How

![Figure 2](https://example.com/fig2.png)
*그림 2에 상세히 표시된 전체 파이프라인*

- **데이터셋 구성**: 상위 2% ICLR 2025 논문, CVPR 2024 하이라이트, ECCV 2024 구두 발표, NeurIPS 2024 및 ICML 2024 스포트라이트/구두 발표, NAACL/EMNLP/ACL 2024 장문/메인 발표 논문들을 선별하여 October 3, 2023 이후 발표 논문으로 필터링.

- **내용 추출**: SciPDF Parser를 이용하여 논문에서 동기(motivation), 실험 단계(experiments), 주제(topic), 영감 논문 정보를 자동으로 추출.

- **아이디어 생성**: 영감 논문에서 추출한 동기와 실험 단계를 target 논문의 주제와 결합하여 다양한 아이디어 풀(idea pool) 생성.

- **6가지 평가 지표 적용**:
  1. **아이디어 선택지 평가** (MCQ): 생성 아이디어가 ground truth 아이디어와 일치하는지 multiple choice로 평가
  2. **아이디어-아이디어 매칭**: 생성 아이디어와 ground truth 아이디어의 유사도 정량화
  3. **아이디어-주제 매칭**: 생성 아이디어가 target 논문의 주제와 얼마나 일치하는지 평가
  4. **경쟁적 비교**: 서로 다른 baseline 방법들 간 상대적 강약점 비교
  5. **혁신성 평가 (Novelty)**: validated idea가 더 많은 신규 논문에서 인용될수록 높은 점수
  6. **실행 가능성 평가 (Feasibility)**: 실험 단계별로 인용도 높은 논문들과의 매칭도를 평균화하여 정량화

## Originality

- **새로운 평가 패러다임**: 기존의 open-ended evaluation에서 벗어나 명시적 ground truth(완전한 논문 내용)를 활용한 paired dataset 기반의 폐쇄형 평가 도입으로 객관성 강화.

- **Data leakage 문제 해결**: October 3, 2023 이후 발표 논문만을 ground truth로 선정하여 GPT-4o의 학습 데이터 cutoff를 명확히 인식하고 데이터 오염 문제 원천 차단.

- **완전한 논문 내용 기반 평가**: 제목과 초록만 다루던 기존 방식에서 벗어나 동기, 실험 설계, 기술적 세부사항을 포함한 논문의 전체 내용을 ground truth로 활용.

- **포괄적 평가 지표**: 혁신성, 실행 가능성, 기존 방법과의 비교 등 다차원적 평가 지표를 체계적으로 구성하여 아이디어 품질의 여러 측면을 정량화.

- **대규모 고품질 벤치마크**: 기존의 소규모 데이터셋(50~170개)에 비해 3,495개의 영향력 있는 AI 논문으로 구성된 대규모 벤치마크 구축.

## Limitation & Further Study

- **데이터셋 도메인 제약**: AI 분야의 상위 컨퍼런스 논문으로만 한정되어 있어, 다른 과학 분야(생물학, 물리학 등)로의 직접적 확장성에 제약이 있을 수 있음. 향후 다중 도메인 벤치마크로 확장 필요.

- **자동 추출 정확도**: SciPDF Parser를 통한 동기와 실험 단계의 자동 추출 과정에서의 오류가 평가 결과에 영향을 미칠 수 있으므로, 추출 정확도 검증 및 개선 필요.

- **평가 지표의 상관성 분석 부족**: 6가지 평가 지표 간의 상관관계, 가중치 최적화 등에 대한 상세한 분석이 필요하며, 인간 평가와의 일치도 검증도 후속 연구에서 다루어져야 함.

- **언어 모델 의존성**: 아이디어 생성 및 평가 과정에서 LLM을 활용하므로, 특정 모델의 편향(bias)이 결과에 미치는 영향을 체계적으로 분석할 필요 있음.

- **시간적 효과 미반영**: 현재 평가 프레임워크에서 아이디어의 장기적 영향력, 시간에 따른 관련성 변화 등을 고려하지 못하고 있어, 시계열 기반 평가 추가 필요.

## Evaluation

- **Novelty (독창성)**: 4.5/5
  기존 평가 방식의 근본적 문제점(data leakage, 불완전한 ground truth)을 명확히 진단하고 해결책을 제시한 점이 우수하나, 평가 지표들의 독립적 구성이 다소 표준화된 접근에 머물러 있음.

- **Technical Soundness (기술적 건전성)**: 4/5
  SciPDF Parser 기반의 자동 추출, 6가지 다차원 평가 지표 설계가 체계적이고 논리적이나, 자동 추출 과정의 오류 율, 평가 지표 간 가중치 결정 등에 대한 상세한 검증 데이터 부재.

- **Significance (의미성)**: 4.5/5
  3,495개의 대규모 ground truth 데이터셋과 포괄적 평가 프레임워크는 향후 과학 발견 자동화 연구에 중요한 자원이 될 것으로 기대되며, AI 커뮤니티에서 활용 가치가 높음. 다만 AI 도메인 한정으로 일반성에 제약.

- **Clarity (명확성)**: 4/5
  전체 파이프라인과 평가 지표가 그림으로 명확하게 표현되어 있으나, 데이터셋 구성 기준(상위 2% vs 하이라이트 vs 구두 발표)의 통일성, 각 평가 지표의 정확한 계산식 등에 대한 상세 설명 부족.

- **Overall (종합)**: 4.2/5

**총평**: AI Idea Bench 2025는 LLM 기반 아이디어 생성 평가의 핵심 문제점들(data leakage, 불완전한 ground truth)을 명확히 진단하고 대규모 고품질 벤치마크와 다차원 평가 프레임워크로 해결하는 의미 있는 연구이다. 다만 자동 추출 정확도 검증, 평가 지표 가중치 최적화, 인간 평가와의 일치도 검증 등 실증적 검증이 보강되면 그 가치가 더욱 높아질 것으로 예상된다.

## Related Papers

- 🔄 다른 접근: [[papers/326_Exp-bench_Can_ai_conduct_ai_research_experiments_arXiv_prepr/review]] — AI Idea Bench의 아이디어 생성 평가와 EXP-Bench의 실험 수행 평가는 AI 연구 능력을 서로 다른 단계에서 측정하는 보완적 접근이다.
- 🔗 후속 연구: [[papers/669_Researchbench_Benchmarking_llms_in_scientific_discovery_via/review]] — ResearchBench가 AI Idea Bench의 아이디어 생성 벤치마크를 실제 과학적 발견 과정 전반으로 확장한 포괄적 평가 프레임워크이다.
- 🏛 기반 연구: [[papers/187_Can_LLMs_Generate_Novel_Research_Ideas_A_Large-Scale_Human_S/review]] — 인간 평가자를 통한 LLM 연구 아이디어 평가 방법론이 AI Idea Bench 벤치마크 설계의 핵심적인 기반이다.
- 🔗 후속 연구: [[papers/518_Many_Heads_Are_Better_Than_One_Improved_Scientific_Idea_Gene/review]] — 과학 아이디어 생성이 AI 연구 아이디어 생성 벤치마크로 확장됩니다.
- 🏛 기반 연구: [[papers/391_Graph_of_ai_ideas_Leveraging_knowledge_graphs_and_llms_for_a/review]] — AI 아이디어 생성 벤치마크가 지식 그래프 기반 학습 경로의 평가 기준
- 🧪 응용 사례: [[papers/632_Predicting_the_future_of_ai_with_ai_High-quality_link_predic/review]] — AI 연구 아이디어 생성 벤치마크를 미래 AI 연구 방향 예측의 실제 평가 도구로 활용할 수 있다
- 🔄 다른 접근: [[papers/326_Exp-bench_Can_ai_conduct_ai_research_experiments_arXiv_prepr/review]] — EXP-Bench의 완전한 실험 수행 능력 평가와 AI Idea Bench의 아이디어 생성 능력 평가는 AI 연구 역량을 서로 다른 단계에서 측정하는 보완적 접근이다.
