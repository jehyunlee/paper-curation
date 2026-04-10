---
title: "792_Text2world_Benchmarking_large_language_models_for_symbolic_w"
authors:
  - "Mengkang Hu"
  - "Tianxing Chen"
  - "Yude Zou"
  - "Yuheng Lei"
  - "Qiguang Chen"
date: "2025"
doi: "---"
arxiv: ""
score: 4.5
essence: "대규모 언어모델(LLM)이 자연언어 설명으로부터 기호적 세계 모델(symbolic world model)을 생성할 수 있는지 평가하기 위해 PDDL 기반의 포괄적인 벤치마크 TEXT2WORLD를 제안하고, 수백 개의 다양한 도메인과 실행 기반 평가 지표를 통해 현재 LLM의 세계 모델링 능력이 여전히 제한적임을 밝혔다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/Realistic_Discovery_Benchmarks"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Hu et al._2025_Text2world Benchmarking large language models for symbolic world model generation.pdf"
---

# Text2world: Benchmarking large language models for symbolic world model generation

> **저자**: Mengkang Hu, Tianxing Chen, Yude Zou, Yuheng Lei, Qiguang Chen, Ming Li, Yao Mu, Hongyuan Zhang, Wenqi Shao, Ping Luo | **날짜**: 2025 | **DOI**: 

---

## Essence

![Figure 1](figures/fig1.webp)
*TEXT2WORLD 벤치마크의 전체 파이프라인: 자연언어 설명으로부터 PDDL 도메인 모델 생성, 자동 수정, 다중 기준 평가*

대규모 언어모델(LLM)이 자연언어 설명으로부터 기호적 세계 모델(symbolic world model)을 생성할 수 있는지 평가하기 위해 PDDL 기반의 포괄적인 벤치마크 TEXT2WORLD를 제안하고, 수백 개의 다양한 도메인과 실행 기반 평가 지표를 통해 현재 LLM의 세계 모델링 능력이 여전히 제한적임을 밝혔다.

## Motivation

- **Known**: 최근 LLM이 세계 모델 생성에 활용되고 있으며, 심리학적으로 세계 모델은 지능적 행동의 핵심 요소로 인정받고 있음
- **Gap**: 기존 연구들이 (i) 제한된 도메인 범위(보통 20개 이하), (ii) LLM 기반 평가의 높은 무작위성(Cohen's κ = 0.10), (iii) 간접적 평가 방식(end-to-end 성공률)에 의존하는 문제를 가짐
- **Why**: 이러한 한계들은 세계 모델링 능력의 정확한 평가와 구체적인 실패 원인 파악을 어렵게 하며, 평가의 신뢰성을 훼손함
- **Approach**: PDDL 기반의 대규모 벤치마크를 구축하여 직접적이고 다중 기준의 실행 기반 평가 지표(executability, structural similarity, component-wise F1 scores)를 제안

## Achievement

![Figure 2](figures/fig2.webp)
*벤치마크 구성 과정: (a) 데이터 수집(1,801개), (b) 자동 필터링 및 수동 선택(264개), (c) 주석 작성 및 품질 보증(최종 103개)*

1. **포괄적 벤치마크 구축**: 1,801개 PDDL 파일에서 출발하여 자동 필터링(검증, 중복 제거, 복잡도 제어, 토큰 길이 필터링)과 수동 선택을 거쳐 103개의 고품질 도메인 벤치마크 완성(Fleiss Kappa = 0.82의 높은 주석자 간 일치도)

2. **신뢰성 높은 평가 지표**: n-gram 기반 데이터 오염 분석(μ = 0.04)으로 낮은 오염율 확인, 구조적 유사도(Levenshtein ratio)와 성분별 F1 점수(술어, 매개변수, 전제조건, 효과)를 통한 다차원적 평가 체계 구현

3. **LLM 성능 벤칭마킹**: 9개 모델 패밀리 16개 LLM 평가 결과, 강화학습으로 훈련된 추론 모델(reasoning models)이 가장 우수한 성능 보임. 오류 수정을 통해 성능 유의미 향상. 주요 오류는 필수 전제조건이나 효과 누락(omission of essential preconditions/effects)으로 분석됨

## How

![Figure 2](figures/fig2.webp)

**벤치마크 구성 방법론**:
- **데이터 수집**: 공개 저장소 및 계획 경진대회에서 1,801개 원본 PDDL 파일 수집
- **자동 필터링**: (i) PDDL 파서를 통한 구문 검증, (ii) TF-IDF 코사인 유사도(>0.9)로 중복 제거, (iii) 술어 40개/행동 20개 초과 도메인 제거, (iv) GPT-2 토크나이저로 5,000 토큰 초과 파일 제거
- **수동 선택**: 세계 모델링용이 아닌 도메인(blocksworld-mystery) 제거 및 자동 필터링에서 누락된 저품질 사례 제거
- **주석 작성**: CS 대학원생 6명이 구조화된 형식(일반 설명, 술어 설명, 행동 설명)으로 주석 작성
- **품질 보증**: 2명의 시니어 전문가가 이중 검증(dual verification) 수행, 정기적 재검사(regular inspection)
- **오염 분석**: n-gram 매칭으로 데이터 오염율 측정(0.04 평균)

**평가 메트릭**:
- **Executability (EXEC.)**: 생성된 PDDL이 표준 PDDL 검증기로 파싱/검증 가능 여부
- **Structural Similarity (SIM.)**: 정규화된 Levenshtein ratio로 생성 PDDL과 정답 PDDL 간 텍스트 유사도 측정
- **Component-wise F1 Scores**: 실행 가능한 PDDL에 대해 술어(F1_PRED), 매개변수(F1_PARAM), 전제조건(F1_PRECOND), 효과(F1_EFF)별로 매크로-평균 F1 점수 계산

**성능 향상 전략**:
- 테스트타임 스케일링(test-time scaling) 적용으로 일관된 성능 개선
- 오류 수정(error correction) 메커니즘 도입
- 미세조정(fine-tuning) 및 맥락 내 학습(in-context learning) 활용
- 에이전트 궤적 데이터(agent trajectory data)에 대한 지도 미세조정으로 의외의 성능 향상

## Originality

- **다차원 평가 체계의 혁신**: 기존의 간접적 end-to-end 평가와 LLM 기반 평가의 무작위성 문제를 해결하기 위해 실행 가능성(executability), 구조적 유사도, 성분별 F1 점수를 결합한 다중 기준 직접 평가 지표 제안

- **대규모 고품질 벤치마크**: 1,801개에서 103개로 엄격하게 정제된 도메인 컬렉션으로, 자동화된 필터링(4단계)과 수동 검증을 결합하여 Fleiss Kappa 0.82의 높은 신뢰성 달성

- **포괄적 오염 분석**: n-gram 기반 데이터 오염 분석으로 0.04의 낮은 오염율을 정량적으로 증명하여 벤치마크가 진정한 모델링 능력을 평가함을 보증

- **상세한 오류 분석 및 성능 개선 전략**: 단순 점수 제시 없이 필수 전제조건/효과 누락 같은 구체적 오류 패턴을 식별하고, 테스트타임 스케일링, 에이전트 궤적 학습 등 효과적인 개선 전략을 제시

## Limitation & Further Study

- **도메인 다양성의 한계**: 최종 103개 도메인은 여전히 제한적이며, 특정 유형의 도메인(예: 매우 복잡한 도메인)에 대한 충분한 표현이 부족할 수 있음

- **자연언어 표현의 단순화**: 실제 세계 모델 생성 시나리오에서 자연언어 설명이 더 모호하고 불완전할 수 있으나, 벤치마크의 설명은 구조화된 형식으로 상대적으로 명확함

- **LLM 성능의 여전한 한계**: 최고 성능 모델도 낮은 수준의 성능을 보이므로, 세계 모델링 능력을 근본적으로 향상시키는 방법론 개발이 필수적

- **후속 연구 방향**: 
  - 더 큰 규모의 도메인 컬렉션 확장(수백~수천 개)
  - 다중언어 벤치마크 구축
  - 시각적 또는 하이브리드 입력 양식에 대한 확장
  - 동적 세계 모델(temporal dynamics) 생성 평가
  - 실제 로봇/시뮬레이션 환경에서의 생성 모델 검증

## Evaluation

- **Novelty**: 4/5 — 실행 기반의 다중 기준 평가 지표와 대규모 정제된 벤치마크는 신선하고, 기존 한계를 구체적으로 해결하지만, 벤치마크 구성의 기본 아이디어는 점진적 개선에 가까움

- **Technical Soundness**: 5/5 — 체계적인 필터링 파이프라인, 엄격한 품질 보증 프로세스(dual verification, Fleiss Kappa 0.82), 낮은 데이터 오염율(0.04)로 기술적 신뢰성 우수. 평가 지표의 설계도 건실함

- **Significance**: 4/5 — 세계 모델 생성 연구에 중요한 자원 제공하며, 추론 모델의 우수성 등 유의미한 발견 제시. 다만 LLM의 근본적인 한계 해결책까지는 제시하지 못함

- **Clarity**: 5/5 — 논문 구조가 명확하고 논리적이며, Figure 1-2가 전체 파이프라인을 잘 시각화함. 벤치마크 구성 과정과 평가 메트릭이 상세하고 이해하기 쉬움

- **Overall**: 4.5/5

**총평**: TEXT2WORLD는 기호적 세계 모델 생성 평가의 신뢰성과 포괄성을 크게 향상시킨 중요한 벤치마크로, 엄격한 품질 관리와 다차원 평가 지표로 기존 연구의 한계를 효과적으로 해결하였다. 다만 최종 103개 도메인의 규모 제약과 LLM의 여전한 성능 한계 개선 방안에 대해서는 추가적인 논의가 필요하다.

## Related Papers

- 🔄 다른 접근: [[papers/704_SciAgentGym_Benchmarking_Multi-Step_Scientific_Tool-use_in_L/review]] — 기호적 세계 모델링과 다단계 도구 활용이라는 서로 다른 방식으로 LLM의 복합적 추론 능력을 평가한다.
- 🏛 기반 연구: [[papers/823_Towards_a_Science_of_Scaling_Agent_Systems/review]] — 에이전트 시스템의 확장 법칙 연구에 필요한 기본적인 세계 모델링 능력 평가 기준을 제공한다.
- 🔗 후속 연구: [[papers/033_A_survey_on_large_language_model_based_autonomous_agents/review]] — 자율 에이전트 연구의 포괄적 조망에서 세계 모델링이라는 핵심 기능의 구체적 평가 방법을 제시한다.
- 🏛 기반 연구: [[papers/704_SciAgentGym_Benchmarking_Multi-Step_Scientific_Tool-use_in_L/review]] — 복잡한 도구 활용 평가에 필요한 기본적인 세계 모델링 능력의 중요성을 입증한다.
