---
title: "186_Can_large_language_models_unlock_novel_scientific_research_i"
authors:
  - "Sandeep Kumar"
  - "Tirthankar Ghosal"
  - "Vinayak Goyal"
  - "Asif Ekbal"
date: "2024"
doi: "N/A"
arxiv: ""
score: 3.5
essence: "본 논문은 대규모 언어모델(LLM)이 과학 논문으로부터 새로운 미래 연구 아이디어를 생성할 수 있는지를 체계적으로 평가한다. 이를 위해 자동 평가 메트릭(IAScore, Idea Distinctness Index)을 제안하고 인간 평가를 병행하여 LLM의 아이디어 생성 능력과 한계를 분석한다."
tags:
  - "cat/LLM-Based_Scientific_Reasoning"
  - "sub/Scientific_Hypothesis_Generation"
  - "topic/ai4s"
---

# Can Large Language Models Unlock Novel Scientific Research Ideas? arXiv:2409.06185, 2024

> **저자**: Sandeep Kumar, Tirthankar Ghosal, Vinayak Goyal, Asif Ekbal | **날짜**: 2024 | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp) *대규모 언어모델이 연구논문을 읽고 미래 연구 아이디어를 제안하는 과정*

본 논문은 대규모 언어모델(LLM)이 과학 논문으로부터 새로운 미래 연구 아이디어를 생성할 수 있는지를 체계적으로 평가한다. 이를 위해 자동 평가 메트릭(IAScore, Idea Distinctness Index)을 제안하고 인간 평가를 병행하여 LLM의 아이디어 생성 능력과 한계를 분석한다.

## Motivation

- **Known**: LLM은 요약, 번역 등 다양한 NLP 작업에서 뛰어난 성능을 보이며, 다양한 도메인의 광범위한 지식을 보유하고 있다.

- **Gap**: 아이디어 생성은 명확한 참조 집합(reference set)이나 구조가 없어 자동 평가 메트릭이 부재하며, 인간 평가는 높은 도메인 전문성과 맥락 이해가 필요해 비용이 많이 든다.

- **Why**: 새로운 LLM이 빠르게 출시되는 상황에서 확장 가능한 평가 방법이 필수적이며, LLM의 실제 아이디어 생성 능력을 이해해야 한다.

- **Approach**: 5개 도메인(컴퓨터과학, 경제학, 물리학, 화학, 의학)의 1,250개 논문으로 데이터셋을 구성하고, 저자가 제시한 미래 연구 아이디어와의 정렬도를 측정하는 IAScore와 아이디어 다양성을 평가하는 Idea Distinctness Index를 제안한다.

## Achievement

![Figure 3](figures/fig3.webp) *도메인별 및 모델별 IAScore 비교; 높은 값은 저자의 아이디어와 더 나은 정렬을 의미*

![Figure 4](figures/fig4.webp) *아이디어 다양성 지수 분석; 인간은 논문의 저자*

1. **자동 평가 메트릭 개발**: IAScore는 생성된 아이디어가 저자가 제시한 미래 연구 방향과 얼마나 잘 정렬되는지를 측정하며, 해석 가능하고 확장 가능한 하한(lower-bound) 지표로 기능한다.

2. **포괄적 데이터셋 구축**: 5개 도메인의 최신 논문들로부터 FRI(Future Research Ideas) 말뭉치를 구성하고, 저자의 미래 연구 아이디어를 AP-FRI 코퍼스로 정리하여 벤치마크를 제공한다.

3. **LLM 비교 분석**: Gemini, Claude-2, GPT-3.5, GPT-4의 성능을 평가하여 모델별 강점과 약점을 파악하고, 컴퓨터과학 분야 660개 아이디어에 대한 인간 평가를 통해 참신성, 관련성, 실행 가능성을 검증한다.

## How

![Figure 2](figures/fig2.webp) *도메인별 논문 내 평균 단어 수 비교 (미래연구 섹션 포함/제외)*

- **데이터셋 구성**: S2ORC에서 각 도메인별 250개씩 총 1,250개 논문 수집; 전체 내용과 미래연구 섹션 포함 논문만 선별
  
- **미래 연구 아이디어 제거**: 논문에서 언급된 FRI를 식별하여 제거(Direct FRI는 전체 제거, Mixed FRI는 부분 제거)하여 LLM이 사전 정보를 갖지 않도록 처리

- **아이디어 생성 프롬프트**: 단계적 추론(step-by-step reasoning) 방식의 구조화된 프롬프트 사용; 맥락 길이 초과 시 논문을 분할하여 처리 후 통합

- **IAScore 계산**: 저자 아이디어와 생성된 아이디어 간 의미적 유사성을 기반으로 정렬도 측정

- **Idea Distinctness Index**: 생성된 여러 아이디어들 간의 다양성 평가

- **인간 평가**: 도메인 전문가가 생성된 아이디어의 참신성(novelty), 관련성(relevance), 실행 가능성(feasibility) 평가

## Originality

- **체계적 평가 프레임워크**: 아이디어 생성 작업에 특화된 최초의 자동 평가 메트릭(IAScore)을 제안하여 인간 평가의 비용 문제를 부분적으로 해결

- **다중 도메인 벤치마크**: 5개 학문 분야의 통합 데이터셋으로 도메인 간 LLM 성능 비교 가능하게 구성

- **엄격한 데이터 정제**: FRI 제거 과정을 통해 LLM의 사전 정보 이용을 방지하고 공정한 평가 환경 조성

- **혼합 평가 방식**: 자동 메트릭과 인간 평가를 병행하여 평가의 신뢰성과 범위를 동시에 강화

## Limitation & Further Study

- **IAScore의 한계**: 저자가 제시하지 않은 진정 참신한 아이디어는 감지할 수 없으며, 오직 기존 아이디어와의 정렬도만 측정하므로 완전한 평가 메트릭이 아니다.

- **인간 평가의 확장성**: 660개 아이디어만 인간 평가되어 컴퓨터과학 분야에 편중되었으며, 다른 도메인에서의 인간 평가 데이터 부족

- **프롬프트 엔지니어링**: 단일 프롬프트만 사용되었으므로 다양한 프롬프트 변형에 따른 성능 변화 미분석

- **모델의 진정한 능력 평가**: 학습 데이터 오염(data contamination) 가능성과 저자 아이디어에 대한 사전 노출 우려

- **후속 연구**: (1) 다른 도메인에서의 인간 평가 확대, (2) 진정한 참신성을 감지할 수 있는 고도화된 메트릭 개발, (3) 아이디어 실행 가능성 검증을 위한 장기 추적 연구

## Evaluation

- **Novelty**: 3.5/5 — 자동 평가 메트릭 제안은 신선하나, 아이디어 생성 자체는 기존 연구의 확장이며 IAScore의 개념적 한계가 있음

- **Technical Soundness**: 4/5 — 데이터셋 구성과 평가 방법론이 체계적이나, 프롬프트 선택과 학습 데이터 오염에 대한 논의 부족

- **Significance**: 3.5/5 — 과학 연구 가속화를 위한 실용적 기여가 있으나, IAScore가 저자 아이디어 정렬에만 제한되어 진정한 참신성 평가에 미흡

- **Clarity**: 4/5 — 전반적으로 명확하게 기술되었으나, Direct/Mixed FRI 분류와 데이터 정제 과정의 상세 설명이 주로 부록에 위치

- **Overall**: 3.5/5

**총평**: 본 논문은 LLM의 아이디어 생성 능력을 체계적으로 평가하기 위한 첫 시도로 의의가 있으나, 제안된 IAScore의 근본적 한계(저자 아이디어와의 정렬도만 측정)로 인해 완전한 평가 프레임워크로 보기 어렵다. 다양한 도메인에 걸친 광범위한 인간 평가와 더불어 진정한 참신성을 감지할 수 있는 개선된 메트릭 개발이 필요하다.

## Related Papers

- 🔄 다른 접근: [[papers/603_PaperRobot_Incremental_Draft_Generation_of_Scientific_Ideas/review]] — LLM 기반 아이디어 생성 평가와 PaperRobot의 지식 그래프 기반 아이디어 생성이 과학적 아이디어 창출의 서로 다른 접근법을 제시한다.
- 🔗 후속 연구: [[papers/728_SciMON_Scientific_Inspiration_Machines_Optimized_for_Novelty/review]] — LLM의 기본적인 아이디어 생성 능력 평가가 SciMON의 참신성 최적화를 통한 품질 향상 연구의 기반이 된다.
- 🏛 기반 연구: [[papers/820_Toward_Reliable_Scientific_Hypothesis_Generation_Evaluating/review]] — LLM의 아이디어 생성 능력에 대한 기본 평가가 TruthHypo의 진실성 검증 연구의 필요성을 입증하는 기초 연구이다.
- 🔄 다른 접근: [[papers/730_Sciqag_A_framework_for_auto-generated_science_question_answe/review]] — LLM의 아이디어 생성과 과학 QA 쌍 생성이 모두 과학 문헌으로부터 지식을 자동 추출하지만 다른 형태의 결과물을 산출한다.
- 🔄 다른 접근: [[papers/603_PaperRobot_Incremental_Draft_Generation_of_Scientific_Ideas/review]] — PaperRobot의 자동 아이디어 생성과 LLM의 과학적 아이디어 생성 능력을 직접 비교하여 방법론적 차이점을 이해할 수 있다.
- 🔄 다른 접근: [[papers/631_Predicting_field_experiments_with_large_language_models/review]] — 경제학 실험 예측과 일반적인 과학 아이디어 생성에서 LLM의 예측 능력을 다른 도메인에서 비교 검증할 수 있다.
- 🏛 기반 연구: [[papers/728_SciMON_Scientific_Inspiration_Machines_Optimized_for_Novelty/review]] — SciMON의 참신성 최적화 방법론이 LLM의 과학 아이디어 생성 능력 평가에서 제시하는 기본적인 아이디어 품질 메트릭을 발전시킨 것이다.
- 🔗 후속 연구: [[papers/729_Scipip_An_llm-based_scientific_paper_idea_proposer/review]] — SciPIP의 구체적인 아이디어 생성 시스템이 LLM의 일반적인 과학 아이디어 생성 능력 평가를 실용적으로 구현한 사례이다.
- 🔄 다른 접근: [[papers/730_Sciqag_A_framework_for_auto-generated_science_question_answe/review]] — SciQAG의 자동 QA 생성과 LLM의 아이디어 생성 평가가 모두 과학 문헌으로부터 자동으로 지식을 추출하지만 서로 다른 형태의 산출물을 생성한다.
- 🔗 후속 연구: [[papers/820_Toward_Reliable_Scientific_Hypothesis_Generation_Evaluating/review]] — LLM의 일반적인 아이디어 생성 능력 평가에서 TruthHypo의 구체적인 진실성 검증 방법론으로 발전하여 더 신뢰할 수 있는 평가를 가능하게 한다.
