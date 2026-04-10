---
title: "036_A_survey_on_transformer_context_extension_Approaches_and_eva"
authors:
  - "Yijun Liu"
  - "Jinzheng Yu"
  - "Yang Xu"
  - "Zhongyang Li"
  - "Qingfu Zhu"
date: "2025"
doi: "arXiv:2503.13299v2"
arxiv: ""
score: 4.0
essence: "Transformer 기반 대규모 언어 모델(LLM)은 사전 학습된 컨텍스트 길이를 초과하는 장문(long context)에서 성능 저하를 보이는데, 본 논문은 이를 해결하기 위한 접근 방식(위치 인코딩, 컨텍스트 압축, 검색 증강, 주의 패턴)과 평가 방법을 체계적으로 분류한 종합 서베이이다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Long_Context_Embeddings"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Wang et al._2025_A survey on transformer context extension Approaches and evaluation.pdf"
---

# A survey on transformer context extension: Approaches and evaluation

> **저자**: Yijun Liu, Jinzheng Yu, Yang Xu, Zhongyang Li, Qingfu Zhu | **날짜**: 2025 | **DOI**: [arXiv:2503.13299v2](https://arxiv.org/abs/2503.13299v2)

---

## Essence

Transformer 기반 대규모 언어 모델(LLM)은 사전 학습된 컨텍스트 길이를 초과하는 장문(long context)에서 성능 저하를 보이는데, 본 논문은 이를 해결하기 위한 접근 방식(위치 인코딩, 컨텍스트 압축, 검색 증강, 주의 패턴)과 평가 방법을 체계적으로 분류한 종합 서베이이다.

## Motivation

- **Known**: Transformer 아키텍처가 NLP 분야에서 광범위하게 적용되어 우수한 성능을 보임. 다만 책/저장소 수준 작업, 장문 대화 시스템, in-context learning 등 장문 처리가 필요한 시나리오 증가.

- **Gap**: 기존 서베이들은 (1) 방법의 일부만 다루어 종합적 개요 부족, (2) 위치 인코딩이나 KV 캐시 관점에서만 접근, (3) 카테고리 간 명확한 구분 및 겹침 문제, (4) 평가 측면에 거의 주목하지 않음.

- **Why**: 장문 처리는 실무에서 중요한 문제이며, 체계적이고 포괄적인 분류 및 평가 체계가 필요함.

- **Approach**: 세 가지 핵심 도전 과제(OOD 문제, "Lost in the Middle" 현상, 이차 복잡도)를 식별하고, 이를 기반으로 4가지 접근 방식과 평가 프레임워크를 제시.

## Achievement

![Figure 1: Framework of survey](figures/fig1.webp)
*Figure 1: 서베이의 프레임워크. 3가지 핵심 도전 과제(섹션 2)와 4가지 접근 방식 분류(섹션 3), 평가 관점(섹션 4), 향후 방향(섹션 5)*

1. **새로운 분류 체계**: 장문 처리 방법을 위치 인코딩(Positional Encoding), 컨텍스트 압축(Context Compression), 검색 증강(Retrieval Augmented), 주의 패턴(Attention Pattern) 4가지로 체계화하여 기존 접근의 중복성 제거

2. **포괄적 평가 프레임워크**: 데이터(길이 수준, 도메인, 예제 수), 작업(QA, Needle-in-a-Haystack, 코드, 통계, In-Context Learning, 텍스트 생성), 메트릭(알고리즘 기반, 모델 기반, LLM 기반) 3개 차원으로 구성

3. **미해결 문제 명시**: 방법 통합, "Train Short, Test Long" 학습, 장문 생성, 정보 필터링과 생성 효과 간 trade-off, sparse attention의 "Lost-in-the-Middle" 문제 등 5가지 미래 연구 방향 제시

## How

### 핵심 도전 과제 (Challenges)

- **OOD 문제**: 사전 학습 컨텍스트 창을 초과한 시퀀스 처리 시 세 가지 요인 (미해결 토큰 거리, 증가된 attended 토큰 수, 시작 토큰의 암시적 위치 인코딩)으로 인한 외삽 능력 제한

- **"Lost in the Middle" 현상**: LLM이 입력 시퀀스의 시작과 끝 정보에 집중하고 중간 내용을 간과

- **이차 복잡도**: Self-attention의 O(n²) 복잡도로 인한 장문 처리의 시간/자원 소비

### 접근 방식 상세 분류

**1. 위치 인코딩 (Positional Encoding)**
- **RoPE 변형**: 
  - 위치 인덱스 조정 (Position Index Adjustment): 토큰 할당 수정, 스케일링, 재할당 조합
  - 기본 주파수 조정 (Base Frequency Adjustment): NTK 이론 기반 θᵢ 수정, 지수항 기반 b 변경, θᵢ 직접 스케일링
  - 구조 수정 (Structural Modification): RoPE 공식 자체 최적화

- **Attention Bias**: 쿼리-키 유사도 계산 시 상대 거리 정보 추가
  ```
  sim(qₘ, kₙ) = qₘᵀkₙ + f_bias(m, n)
  ```

**2. 컨텍스트 압축 (Context Compression)**
- 소프트 압축 (Soft Compression): 요약 토큰 추가 등 간접적 방법
- 하드 압축 (Hard Compression): 텍스트 요약, 선택 등 직접적 방법

**3. 검색 증강 (Retrieval Augmented)**
- 검색 세분화 (Retrieval Granularity): 어느 단위로 검색할 것인가
- 유사도 계산 (Similarity Computation): 관련성 평가 방식
- 위치 인코딩: 검색된 컨텍스트의 위치 처리
- 주의 계산 (Attention Calculation): 검색된 내용의 주의 적용

**4. 주의 패턴 (Attention Pattern)**
- Sliding Window: 이전 토큰만 참조
- Parallel Context: 프롬프트와 컨텍스트 병렬 처리
- Sparse Attention: 선택적 토큰 참조

### 평가 방법론

**데이터**: 길이 수준별(짧음/중간/긴), 도메인별, 예제 수 등으로 분류

**작업**:
- QA: 질의응답 능력 평가
- Needle-in-a-Haystack: 큰 텍스트에서 특정 정보 찾기
- 코드: 코드 이해 및 생성
- 통계: 문서 통계 정보 추출
- In-Context Learning: 장문 few-shot 학습
- 텍스트 생성: 장문 생성 능력

**메트릭**:
- 알고리즘 기반: 정확도, F1 스코어 등
- 모델 기반: BERTScore 등 임베딩 유사도
- LLM 기반: GPT-4 등으로 평가

## Originality

- **새로운 분류 체계의 명확성**: 기존 5분류의 중복성 제거, RoPE 변형을 세부적으로 분류(위치 인덱스, 기본 주파수, 구조 수정)

- **평가 프레임워크의 체계성**: 방법론뿐 아니라 평가 측면을 데이터-작업-메트릭 3차원으로 종합적으로 조직화

- **핵심 도전 과제의 명시화**: OOD, "Lost in the Middle", 이차 복잡도를 기초 이론 차원에서 명확히 정의

- **미해결 문제의 구체화**: 방법 통합, Train Short Test Long, 정보 필터링-생성 trade-off 등 5가지 미래 방향 제시

## Limitation & Further Study

- **범위 제한**: 장문 chain-of-thought 추론, 멀티모달 장문, 효율적 Transformer, State Space Model 등은 제외 (명확히 선언)

- **RAG 제외**: 외부 지식 주입 관점의 RAG는 범위 밖 (입력 컨텍스트 확장에만 집중)

- **이론적 연결 부족**: 제시된 3가지 도전 과제와 실제 방법들의 인과 관계가 명확하지 않음. 많은 방법이 이들 도전 과제에서 출발하지 않고 작업 성능 개선을 직접 목표로 함

- **후속 연구**: 
  - 다양한 방법의 조합 및 통합 전략 개발
  - 사전 학습 길이보다 짧게 학습하면서 긴 시퀀스에서 작동하는 방법 ("Train Short, Test Long")
  - 장문 생성 능력의 평가 및 개선
  - Sparse attention과 정보 필터링 간 trade-off 분석
  - 더 신뢰할 수 있는 LLM 기반 평가 메트릭 개발

## Evaluation

- **Novelty**: 4/5 - 명확한 4분류 체계와 평가 프레임워크는 신규적이나, 개별 방법들은 기존 연구의 종합

- **Technical Soundness**: 4/5 - 체계적 분류와 논리적 조직화가 탄탄하나, 이론적 근거(OOD 등)와 방법들의 연결이 부족

- **Significance**: 4/5 - 장문 처리는 현실적으로 중요한 문제이며 포괄적 가이드로서 학계에 기여도 높음

- **Clarity**: 4/5 - 계층적 구조와 Figure 1의 프레임워크가 명확하나, 세부 방법 설명이 간략함

- **Overall**: 4/5

**총평**: 본 논문은 Transformer 기반 장문 처리를 위한 첫 번째 포괄적이고 체계적인 서베이로서, 새로운 분류 체계와 평가 프레임워크를 통해 빠르게 성장하는 이 분야에 명확한 구조를 제공한다. 특히 방법론뿐 아니라 평가 측면을 동등하게 다룬 것과 미해결 문제를 명시한 점이 차별적이나, 기초 이론(OOD 등)과 실제 방법들 간의 더 명확한 인과 연결이 이루어진다면 더욱 통찰력 있는 가이드가 될 것이다.

## Related Papers

- 🔄 다른 접근: [[papers/005_A_comprehensive_survey_on_long_context_language_modeling/review]] — 긴 컨텍스트 언어 모델링에 대한 또 다른 포괄적 서베이로 상호 보완적 관점을 제공한다.
- 🧪 응용 사례: [[papers/318_Estimating_optimal_context_length_for_hybrid_retrievalaugmen/review]] — 하이브리드 검색-증강 생성에서 최적 컨텍스트 길이 추정 방법으로 본 논문의 컨텍스트 확장 기법을 실용적으로 활용한다.
- 🔗 후속 연구: [[papers/452_L-citeeval_Do_longcontext_models_truly_leverage_context_for/review]] — 긴 컨텍스트 모델이 실제로 컨텍스트를 활용하는지 평가하는 벤치마크로 본 논문의 평가 방법론을 구체화한다.
- 🏛 기반 연구: [[papers/005_A_comprehensive_survey_on_long_context_language_modeling/review]] — 트랜스포머 맥락 확장 접근법과 평가에 대한 조사는 장문맥 언어모델링의 핵심 기술적 기반을 제공합니다
- 🔗 후속 연구: [[papers/495_Llm__mapreduce-v2_Entropy-driven_convolutional_test-time_sca/review]] — 트랜스포머 컨텍스트 확장 접근법들이 엔트로피 기반 테스트 타임 스케일링의 구체적인 확장 기술이다.
- 🏛 기반 연구: [[papers/368_Gemini_15_Unlocking_multimodal_understanding_across_millions/review]] — 트랜스포머 컨텍스트 확장 방법에 대한 조사가 Gemini 1.5의 1천만 토큰 컨텍스트 처리 기술을 이해하는 기반을 제공한다.
- 🏛 기반 연구: [[papers/318_Estimating_optimal_context_length_for_hybrid_retrievalaugmen/review]] — 트랜스포머 문맥 확장에 대한 전반적 조사를 바탕으로 실용적 최적화를 제시한다
