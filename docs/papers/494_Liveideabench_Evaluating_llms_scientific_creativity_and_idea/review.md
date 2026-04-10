---
title: "494_Liveideabench_Evaluating_llms_scientific_creativity_and_idea"
authors:
  - "Kai Ruan"
  - "Xuan Wang"
  - "Jixiang Hong"
  - "Peng Wang"
  - "Yang Liu"
date: "2024"
doi: "N/A"
arxiv: ""
score: 4.0
essence: "본 논문은 최소한의 맥락(단일 키워드)을 사용하여 대규모 언어모델(LLM)의 과학적 아이디어 생성 능력과 발산적 사고(divergent thinking) 능력을 평가하는 포괄적인 벤치마크 LiveIdeaBench를 제시한다. 40개 이상의 모델을 22개 과학 분야의 1,180개 키워드로 평가한 결과, 과학적 아이디어 생성 능력이 일반 지능 점수로 잘 예측되지 않음을 보여준다."
tags:
  - "cat/Cognitive_AI_Evaluation_and_Benchmarking"
  - "sub/AI_Benchmarking_Taxonomy"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Ruan et al._2024_Liveideabench Evaluating llms’ scientific creativity and idea generation with minimal context.pdf"
---

# Liveideabench: Evaluating llms' scientific creativity and idea generation with minimal context

> **저자**: Kai Ruan, Xuan Wang, Jixiang Hong, Peng Wang, Yang Liu, Hao Sun | **날짜**: 2024 | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp)
*LiveIdeaBench의 전체 설계: (a) 1,000개 이상의 과학 키워드를 사용한 발산적 사고 촉진, (b) 판정 LLM이 5가지 차원으로 평가, (c) 상위 10개 최첨단 모델로 구성된 동적 평가 패널, (d-f) Guilford 창의성 이론 기반 5가지 차원 평가 방법론*

본 논문은 최소한의 맥락(단일 키워드)을 사용하여 대규모 언어모델(LLM)의 과학적 아이디어 생성 능력과 발산적 사고(divergent thinking) 능력을 평가하는 포괄적인 벤치마크 LiveIdeaBench를 제시한다. 40개 이상의 모델을 22개 과학 분야의 1,180개 키워드로 평가한 결과, 과학적 아이디어 생성 능력이 일반 지능 점수로 잘 예측되지 않음을 보여준다.

## Motivation

- **Known**: LLM은 문헌 분석, 실험 설계 등 다양한 과학 작업에서 뛰어난 성능을 보이며, 창의성 검사에서 인간 수준의 성능을 달성하고 있다. 기존 창의성 이론(Getzels & Jackson, 1962)에서는 높은 IQ가 높은 창의성을 보장하지 않으며, 창의성과 지능이 상대적으로 독립적인 특성임을 제시했다.

- **Gap**: 기존 LLM 평가 벤치마크는 풍부한 맥락 입력을 기반으로 성능을 평가하며, 특히 최소 맥락에서의 과학적 아이디어 생성 능력에 대한 체계적 평가가 부족하다. 또한 일반 지능 점수와 과학적 창의성 간의 관계가 명확하지 않다.

- **Why**: LLM의 창의성 평가에는 인간 창의성 이론의 통찰이 필요하며, Guilford의 발산적 사고 이론(유창성, 유연성, 독창성, 정교성)을 적용한 다차원적 평가가 필요하다. 

- **Approach**: Guilford의 창의성 이론에서 영감을 얻어, 단일 키워드 프롬프트로 발산적 사고를 촉진하고, 최첨단 LLM의 동적 패널을 판정자로 활용하여 5가지 차원(독창성, 실현가능성, 유창성, 유연성, 명확성)에서 생성된 아이디어를 평가하는 벤치마크를 구축했다.

## Achievement

![Figure 2](figures/fig2.webp)
*LiveIdeaBench에서의 모델 성능 비교: (a) 개방 가중치 및 독점 모델의 5가지 차원별 점수 및 전체 성능, (b) 주요 모델들의 다차원 성능 프로필, (c) 과학 키워드의 워드클라우드*

1. **일반 지능과 창의성의 독립성 실증**: QwQ-32B-preview는 일반 지능 점수에서 claude-3.5-sonnet:thinking보다 현저히 낮음에도 불구하고, 과학적 아이디어 생성의 창의적 성능에서 비교 가능한 수준을 달성했다. 이는 threshold theory를 LLM 맥락에서 실증적으로 지지한다.

2. **포괄적 벤치마크 구축**: 22개 과학 분야에 걸친 1,180개 키워드로 40개 이상의 모델을 평가하여, 일반 지능 점수로 설명되지 않는 창의성의 변동성을 체계적으로 문서화했다.

3. **창의성과 지능의 다른 발달 경로 발견**: 과학적 아이디어 생성 능력이 일반 문제 해결 능력과 다른 훈련 전략으로 향상될 가능성을 시사한다.

## How

![Figure 3](figures/fig3.webp)
*과학 분류별 LiveIdeaBench의 모델 성능: 다양한 과학 영역(물리학, 화학, 생물학 등)에서 평균 성능을 시각화한 히트맵*

- **데이터 수집**: 22개 과학 분야에서 1,180개의 대표적 키워드 선정 (예: "날씨 예측", "양자 컴퓨팅")

- **아이디어 생성**: 각 키워드에 대해 여러 LLM이 과학적 아이디어 생성 수행

- **다차원 평가 체계**:
  - **독창성(Originality)**: 생성 아이디어의 새로움 정도
  - **실현가능성(Feasibility)**: 아이디어의 과학적 타당성 및 실행 가능성
  - **명확성(Clarity)**: 아이디어 표현의 명확함
  - **유창성(Fluency)**: 같은 키워드에서 생성한 아이디어의 다양성 및 실질적 차이
  - **유연성(Flexibility)**: 다른 4가지 차원 평균 점수의 30 백분위수

- **판정자 모델**: LiveBench에서 선정된 상위 10개 최첨단 모델의 동적 패널을 평가자로 활용 (robust한 앙상블 점수 확보)

- **통계 분석**: 40개 이상 모델의 성능을 일반 지능 점수(예: 벤치마크 종합 점수)와 비교하여 상관관계 분석

## Originality

- **이론과 실증의 통합**: 인간 창의성 심리학 이론(Guilford, Getzels & Jackson, Boden, Amabile)을 LLM 평가에 체계적으로 적용한 최초의 시도

- **최소 맥락 평가의 창의성**: 기존의 풍부한 문맥 기반 평가와 달리, 단일 키워드로 순수한 발산적 사고 능력을 측정함으로써 새로운 평가 관점 제시

- **동적 판정자 패널**: 고정된 평가 기준이 아닌, 최첨단 모델들의 진화하는 패널을 활용하여 벤치마크의 적응성과 타당성 확보

- **일반 지능-창의성 분리의 실증**: LLM 맥락에서 Getzels & Jackson의 고전 이론을 재검증하여, 창의성과 지능이 서로 다른 메커니즘을 따를 수 있음을 보임

- **대규모 평가 규모**: 22개 도메인, 1,180개 키워드, 40개 이상 모델의 포괄적 평가로 통계적 신뢰성 확보

## Limitation & Further Study

- **평가 차원의 한계**: Guilford 이론의 "정교성(elaboration)" 차원이 미포함되었으며, 발산적 사고에 중점을 두어 수렴적 사고(convergent thinking)의 역할을 간과할 수 있다. 실제 창의적 성과는 두 사고 방식의 상호작용이 필요하다.

- **맥락 최소화의 타당성**: 단일 키워드로의 평가가 실제 과학 연구의 복잡한 상황을 충분히 반영하지 못할 가능성. 현실의 과학적 창의성은 더 풍부한 도메인 지식과 문헌 정보를 기반으로 한다.

- **판정 LLM 편향**: 상위 10개 모델의 앙상블 점수도 특정 모델 계열(예: Claude, GPT)의 선호도를 가질 가능성이 있으며, 독립적 인간 평가자 검증이 부재하다.

- **창의성 동질성 문제**: Wenger & Kenett, Doshi et al.의 선행 연구처럼, LLM 생성 아이디어의 높은 동질성 문제가 완전히 해결되지 않았을 가능성.

- **후속 연구 방향**:
  - 인간 창의성 전문가와 AI 생성 아이디어에 대한 독립적 평가 비교
  - 도메인별 깊은 지식 기반의 다단계 프롬프트 평가
  - 특정 과학 분야(예: 신약 개발)에서의 실제 성과 추적
  - LLM 훈련 전략의 개선(창의성 특화 파인튜닝, 발산적 사고 명시적 학습)
  - 모델 규모, 아키텍처, 훈련 데이터와 창의성 간의 인과관계 분석

## Evaluation

- **Novelty**: 4/5
  - LLM 창의성 평가에 인간 심리학 이론을 체계적으로 적용한 점과 일반 지능-창의성 분리를 실증한 점이 우수하나, Guilford 이론 자체는 고전적이며, 실제 창의성과의 연결 고리가 여전히 미흡함.

- **Technical Soundness**: 4/5
  - 포괄적인 평가 체계, 동적 판정자 패널, 대규모 실험이 기술적으로 견고하나, 독립적 인간 평가 검증 부재와 판정 LLM 편향 가능성이 약점. 통계적 신뢰구간 제시는 긍정적.

- **Significance**: 4/5
  - LLM의 창의성을 일반 지능과 분리하여 평가해야 한다는 실무적 시사가 중요하며, 향후 AI 모델 개발 전략 수정의 근거를 제공함. 다만, 실제 과학 발견으로의 전환이 입증되지 않아 영향력의 현실성에 제약.

- **Clarity**: 4/5
  - 논문 구조, 방법론, 결과 제시가 대체로 명확하고, Figure들이 잘 설계되었으나, 평가 차원 간 상관관계, 모델별 상세 성능 해석이 더 풍부했으면 더 좋았을 것.

- **Overall**: 4/5

**총평**: LiveIdeaBench는 LLM의 과학적 창의성 평가에 새로운 관점을 제시하며, 일반 지능과 창의성의 독립성을 실증한 의미 있는 벤치마크다. 다만 평가의 최소 맥락화, 판정자 편향, 실제 과학 성과로의 연결 고리 등 여러 한계가 있어 추가 검증과 개선이 필요하다.

## Related Papers

- 🔄 다른 접근: [[papers/495_Llm__mapreduce-v2_Entropy-driven_convolutional_test-time_sca/review]] — 과학적 아이디어 생성 능력 평가와 장문 기사 생성 능력 평가 모두 LLM의 창의적 생성 능력을 다루지만 평가 방식이 다르다.
- 🏛 기반 연구: [[papers/187_Can_LLMs_Generate_Novel_Research_Ideas_A_Large-Scale_Human_S/review]] — LLM이 새로운 연구 아이디어를 생성할 수 있는지에 대한 대규모 인간 평가가 과학적 창의성 벤치마크의 기반 연구이다.
- 🔗 후속 연구: [[papers/392_Grapheval_A_lightweight_graph-based_llm_framework_for_idea_e/review]] — 그래프 기반 LLM 프레임워크를 통한 아이디어 평가가 과학적 아이디어 생성 벤치마크의 평가 체계를 확장한다.
- 🔗 후속 연구: [[papers/509_Llms_can_realize_combinatorial_creativity_generating_creativ/review]] — LiveIdeaBench의 과학적 창의성 평가는 조합적 창의성 이론 기반 아이디어 생성의 검증 방법을 제공합니다
- 🧪 응용 사례: [[papers/577_Nova_An_iterative_planning_and_search_approach_to_enhance_no/review]] — LiveIdeaBench의 과학적 창의성 평가는 Nova가 생성한 새로운 아이디어의 품질을 측정하는 실제 응용 플랫폼입니다
- 🔗 후속 연구: [[papers/669_Researchbench_Benchmarking_llms_in_scientific_discovery_via/review]] — LiveIdeaBench의 과학적 창의성 평가는 ResearchBench의 과학 발견 벤치마크를 더욱 구체적인 아이디어 생성 평가로 확장합니다
- 🔗 후속 연구: [[papers/366_Futuregen_Llm-rag_approach_to_generate_the_future_work_of_sc/review]] — LiveIdeaBench의 과학적 창의성 평가는 FutureGen이 생성한 미래 연구 방향의 품질과 창의성을 측정하는 확장된 평가 방법입니다
- 🔄 다른 접근: [[papers/495_Llm__mapreduce-v2_Entropy-driven_convolutional_test-time_sca/review]] — 발산적 사고와 과학적 창의성 평가와 달리 극도로 긴 입력에서 장문 기사 생성이라는 다른 LLM 능력을 측정한다.
- 🔗 후속 연구: [[papers/417_HypoBench_Towards_Systematic_and_Principled_Benchmarking_for/review]] — 가설 생성 벤치마크를 창의성과 아이디어 품질 평가로 확장한 연구
- 🧪 응용 사례: [[papers/484_Learning_to_generate_research_idea_with_dynamic_control/review]] — LiveIdeaBench의 LLM 과학적 창의성 평가는 동적 제어 기반 연구 아이디어 생성의 실제 성능을 체계적으로 벤치마킹할 수 있다.
- 🔄 다른 접근: [[papers/155_Beyond_Brainstorming_What_Drives_High-Quality_Scientific_Ide/review]] — LLM의 과학적 창의성 평가와 고품질 아이디어 생성 동인의 다른 접근법
- 🏛 기반 연구: [[papers/313_Enabling_ai_scientists_to_recognize_innovation_A_domain-agno/review]] — LLM의 과학적 창의성과 아이디어 생성 평가 벤치마크로 본 논문의 혁신성 평가 방법론의 기반을 제공한다.
- 🔗 후속 연구: [[papers/411_How_do_humans_and_language_models_reason_about_creativity_a/review]] — 창의성과 아이디어 평가에서 인간과 LLM의 차이를 더 포괄적인 과학적 창의성 벤치마크로 확장한 연구입니다.
- 🔗 후속 연구: [[papers/762_Spark_A_system_for_scientifically_creative_idea_generation/review]] — LLM의 과학적 창의성과 아이디어 품질을 평가하는 벤치마크를 제공한다
