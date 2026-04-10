---
title: "114_Augmented_Language_Models_a_Survey"
authors:
  - "G. Mialon"
  - "Roberto Dessì"
  - "M. Lomeli"
  - "Christoforos Nalmpantis"
  - "Ramakanth Pasunuru"
date: "2023"
doi: "arXiv:2302.07842"
arxiv: ""
score: 4.4
essence: "본 논문은 언어 모델(Language Models, LMs)을 추론 능력과 도구 사용 능력으로 확대하는 증강 언어 모델(Augmented Language Models, ALMs)에 대한 포괄적인 조사 논문이다. ALMs는 복잡한 작업을 단순한 부작업으로 분해하거나 외부 모듈(코드 인터프리터, 검색 엔진 등)을 활용하여 기존 LMs의 해석 가능성, 일관성, 확장성 문제를 해결할 수 있다."
tags:
  - "cat/AI-Powered_Scientific_Research_Frameworks"
  - "sub/Scientific_Agent_Frameworks"
  - "topic/ai4s"
---

# Augmented Language Models: a Survey

> **저자**: G. Mialon, Roberto Dessì, M. Lomeli, Christoforos Nalmpantis, Ramakanth Pasunuru | **날짜**: 2023 | **DOI**: [arXiv:2302.07842](https://arxiv.org/abs/2302.07842)

---

## Essence

본 논문은 언어 모델(Language Models, LMs)을 추론 능력과 도구 사용 능력으로 확대하는 증강 언어 모델(Augmented Language Models, ALMs)에 대한 포괄적인 조사 논문이다. ALMs는 복잡한 작업을 단순한 부작업으로 분해하거나 외부 모듈(코드 인터프리터, 검색 엔진 등)을 활용하여 기존 LMs의 해석 가능성, 일관성, 확장성 문제를 해결할 수 있다.

## Motivation

- **Known**: 
  - 대규모 언어 모델(LLMs)은 NLP에서 극적인 진전을 이루었으나, 환각(hallucination), 산술 오류, 추론 체인의 일관성 문제 등 심각한 한계를 지님
  - 기존 LMs는 단일 매개변수 모델과 제한된 문맥(n개의 이전 토큰)에만 의존하여 학습됨

- **Gap**: 
  - LMs의 성능 향상을 위해 추론과 도구 사용을 별도로 다루는 연구가 다수 존재하지만, 이들을 체계적으로 통합하는 프레임워크와 분류체계가 부재함
  - 서로 다른 의도로 사용되는 기술 용어들이 정의되지 않아 커뮤니티 간 소통의 어려움 존재

- **Why**: 
  - 추론과 도구의 결합은 휴리스틱 없이도 복잡한 작업을 해결할 수 있으며, 더 나은 일반화 성능을 제공
  - 추론은 LM이 문제를 부작업으로 분해하도록 유도하고, 도구는 각 단계를 올바르게 수행하도록 보조 (상호보완적)

- **Approach**: 
  - 추론(Reasoning), 도구 및 행동(Using Tools and Act), 학습 방법(Learning)의 세 축으로 ALM 관련 연구를 분류
  - 각 범주에서 최신 연구 동향과 기술을 체계적으로 검토하고 한계를 분석

## Achievement

![Figure 1](https://img.shields.io/badge/Figure-1-blue) **Few-shot Chain-of-Thought 프롬핑**: Wei et al. (2022c)이 제시한 방법으로, 중간 추론 단계를 포함한 예시를 통해 LM의 추론 능력을 향상

![Figure 2](https://img.shields.io/badge/Figure-2-blue) **Zero-shot Chain-of-Thought**: Kojima et al. (2022)이 제시한 방법으로, 예시 없이도 "단계별로 생각해보자"와 같은 간단한 프롬프트로 추론 성능 개선

1. **추론 능력 강화**: 
   - 프롬팅을 통한 추론 유도(Chain-of-Thought, 재귀적 프롬팅)
   - 작업 메모리(Working Memory)와 반복적 프롬팅 활용
   - 명시적 학습을 통한 추론 능력 개선

2. **도구 활용 확대**: 
   - 다른 모델 호출, 정보 검색(문서 검색, 검색 엔진, 웹 네비게이션)
   - 코드 인터프리터와 기호 모듈을 통한 계산
   - 가상/물리 세계에 대한 행동(로봇 조작 등)

3. **학습 방법론 다양화**: 
   - 지도 학습(Supervision), 강화 학습(Reinforcement Learning)을 통한 ALM 학습
   - 휴리스틱 기반 접근과 학습 기반 접근의 비교

## How

![Figure 3](https://img.shields.io/badge/Figure-3-blue) **재귀적 프롬팅(Recursive Prompting)**: LM이 복잡한 문제를 단계적으로 분해하여 해결하는 프롬팅 방식

![Figure 4](https://img.shields.io/badge/Figure-4-blue) **작업 메모리(Working Memory)**: Taylor et al. (2022)이 제안한 방법으로, 중간 계산 결과를 저장하고 참조하여 추론 과정을 체계화

![Figure 5](https://img.shields.io/badge/Figure-5-blue) **반복적 프롬팅(PEER)**: Schick et al. (2022)의 방법으로, LM이 계획을 생성하고 실행하는 반복 과정

- **추론 방법**:
  - Few-shot Chain-of-Thought: 중간 단계 예시를 통한 유도
  - Zero-shot Chain-of-Thought: "Let's think step by step" 같은 트리거 프롬프트
  - 재귀적/반복적 분해: 복잡한 문제를 체계적으로 부분 문제로 분해
  - 명시적 학습: 훈련 데이터를 통해 추론 능력을 직접 학습

- **도구 통합 메커니즘**:
  - 규칙 또는 특수 토큰을 통한 도구 호출
  - 도구 출력을 LM의 문맥에 포함시켜 다음 토큰 예측에 활용
  - 정보 검색 도구(Retrieval-Augmented Generation, RAG)
  - 코드 실행 환경을 통한 수학 계산 및 논리 연산

- **학습 전략**:
  - 감독 신호(라벨된 추론 체인)를 통한 지도 학습
  - 강화 학습을 통한 자율적 도구 사용 학습
  - 휴리스틱과 학습의 결합

## Originality

- **포괄적 분류체계**: 추론과 도구 사용을 동일한 프레임워크에서 다루는 최초의 체계적 분류 (기존 연구는 이들을 분리하여 다룸)

- **명확한 정의**: "추론", "도구", "행동"에 대한 기술적 정의를 제공하여 커뮤니티 간 개념의 혼동 해소

- **ALM 개념의 도입**: 순수 언어 모델링 패러다임을 벗어나 매개변수 외부의 모듈을 활용하는 새로운 모델 범주를 제시

- **통합적 관점**: 추론과 도구가 모두 LM의 문맥을 확장하여 토큰 예측을 개선한다는 통일된 설명 제공

- **실무적 관점**: 추론이 현재 기술 수준에서 "진정한 추론"인지 불명확하다는 점을 인정하면서도 실용적 정의를 제시

## Limitation & Further Study

- **이론적 한계**: 
  - ALMs가 실제로 "추론"하는지 아니면 단순히 더 큰 문맥을 생성하여 토큰 예측 확률을 증가시키는지 명확하지 않음 (Huang and Chang, 2022의 논의 필요)
  - 복잡한 추론 문제에서 LMs가 계속 실패하는 이유에 대한 깊이 있는 분석 부족

- **실무적 한계**:
  - 도구 호출의 정확성: LM이 올바른 도구와 시점을 선택하는 데 실패할 수 있음
  - 문맥 크기 제약: ALMs도 여전히 유한한 문맥 크기로 제한되어 있음
  - 확장성 문제: 지속적 학습(continual learning)에서 ALMs의 효율성 불명확

- **후속 연구 방향**:
  - ALMs의 해석 가능성 향상: 도구 호출과 추론 경로의 투명성 확보
  - 강화 학습을 통한 자율적 도구 사용 학습의 더 효율적 방법론 개발
  - 물리적 세계에서의 행동 학습: 로봇 조작 등 실제 환경에서의 ALM 적용
  - 멀티-스텝 추론에서의 오류 전파 문제 해결


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4/5
- Significance: 4.5/5
- Clarity: 4.5/5
- Overall: 4.4/5

**총평**: 본 논문은 빠르게 발전하는 ALM 분야를 체계적으로 정리한 우수한 서베이로, 추론과 도구 사용을 통합적으로 다루고 명확한 분류체계를 제시하여 커뮤니티에 실질적 기여를 한다. 다만 일부 핵심 개념의 철학적 기초가 여전히 명확하지 않다는 한계가 있다.

## Related Papers

- 🏛 기반 연구: [[papers/052_Advances_and_challenges_in_foundation_agents_From_brain-insp/review]] — 추론과 도구 사용으로 확장된 증강 언어모델의 개념이 뇌 기능 기반 파운데이션 에이전트 설계의 핵심적 이론적 기반을 제공한다
- 🔗 후속 연구: [[papers/499_LLM_With_Tools_A_Survey/review]] — 언어모델의 추론 및 도구 사용 확장에 대한 조사가 도구를 활용하는 LLM에 대한 더 포괄적이고 구체적인 서베이로 발전했다
- 🏛 기반 연구: [[papers/813_Toolformer_Language_Models_Can_Teach_Themselves_to_Use_Tools/review]] — 증강 언어모델의 도구 사용 개념이 언어모델이 스스로 도구 사용을 학습하는 자율적 시스템 개발의 중요한 이론적 토대가 되었다
- 🧪 응용 사례: [[papers/815_ToolLLM_Facilitating_Large_Language_Models_to_Master_16000_R/review]] — 언어모델의 도구 사용 능력 확장 연구가 16000개 이상의 다양한 도구를 마스터하는 대형언어모델 개발에 직접 적용되었다
- 🔗 후속 연구: [[papers/052_Advances_and_challenges_in_foundation_agents_From_brain-insp/review]] — 뇌 기능 기반 모듈식 에이전트 아키텍처가 추론과 도구 사용 능력으로 확장된 증강 언어모델의 구체적 구현 방향을 제시한다
