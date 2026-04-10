---
title: "047_ActionIE_Action_Extraction_from_Scientific_Literature_with_P"
authors:
  - "Xianrui Zhong"
  - "Yufeng Du"
  - "Siru Ouyang"
  - "Ming Zhong"
  - "Tingfeng Luo"
date: "2024"
doi: "10.18653/v1/2024.acl-long.683"
arxiv: ""
score: 4.0
essence: "과학 문헌의 비정형 자연언어로 표현된 실험 절차를 Python 코드 생성 문제로 재정의하여 대규모 언어모델(LLM)을 활용해 화학 합성 행동을 추출하는 방법론을 제시한다. 프로그래밍 언어의 구조적 특성(클래스, 상속, 타입)을 활용하여 엔티티 간 관계를 명확히 포착한다."
tags:
  - "cat/Cognitive_AI_Evaluation_and_Benchmarking"
  - "sub/Multi-Hop_Reasoning_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Zhong et al._2024_ActionIE Action Extraction from Scientific Literature with Programming Languages.pdf"
---

# ActionIE: Action Extraction from Scientific Literature with Programming Languages

> **저자**: Xianrui Zhong, Yufeng Du, Siru Ouyang, Ming Zhong, Tingfeng Luo | **날짜**: 2024 | **DOI**: [10.18653/v1/2024.acl-long.683](https://doi.org/10.18653/v1/2024.acl-long.683)

---

## Essence

![Figure 1](figures/fig1.webp) *화학 반응 절차를 자연언어에서 구조화된 행동 시퀀스로 추출하는 예시*

과학 문헌의 비정형 자연언어로 표현된 실험 절차를 Python 코드 생성 문제로 재정의하여 대규모 언어모델(LLM)을 활용해 화학 합성 행동을 추출하는 방법론을 제시한다. 프로그래밍 언어의 구조적 특성(클래스, 상속, 타입)을 활용하여 엔티티 간 관계를 명확히 포착한다.

## Motivation

- **Known**: 기존 NLP 기반 화학 정보 추출은 (1) 트랜스포머 모델이 도메인 특화 언어의 복잡성을 처리하기 어렵고, (2) 대규모 인간 어노테이션 데이터셋에 의존하며, (3) 액션 정의가 변경되면 규칙/데이터를 재작성해야 함

- **Gap**: 현존 방법들은 순차 태깅(sequential tagging) 방식으로 작동명령(operation)과 속성(attribute) 간의 관계 파악에 실패하고, 상용 화학 데이터베이스(Reaxys, SciFinder)도 반응 조건보다는 시약/생성물만 저장하며 실제 실험 절차 시퀀스는 부재

- **Why**: 화학자들이 문헌을 수작업으로 검색·해석하여 프로토콜을 선택하는 과정을 자동화하고, 로봇 실험실(robotic laboratory) 환경에서 자동 실행 가능한 형식으로 변환할 필요가 있음

- **Approach**: 액션 추출을 코드 생성 문제로 재정의하여 각 액션 타입을 Python 클래스로 변환하고, LLM의 인-컨텍스트 러닝(few-shot learning) 능력을 활용하여 어노테이션 데이터 부족 문제 해결

## Achievement

![Figure 2](figures/fig2.webp) *ActionIE 프레임워크 개요: 패턴 마이닝 → 텍스트 재표현 → 코드 생성 → 자연언어 변환*

1. **코드 기반 구조화**: 프로그래밍 언어의 클래스 상속과 컴포지션 관계를 통해 액션 간 의존성과 중첩된 구조를 명확하게 표현하여, LLM의 할루시네이션(hallucination) 문제 완화 및 액션 정의 변경에 대한 유연성 제공

2. **신규 평가 메트릭**: 기존 토큰 수준 평가의 한계를 지적하고, 그래프 매칭(graph-based matching) 기반 메트릭을 제안하여 추출 정확도와 인간 판단의 상관관계 향상

3. **신규 테스트셋**: 기존 특허 데이터 중심의 벤치마크(평균 158.2자)를 보완하여 화학 문헌 기반 대규모 테스트셋(평균 770.8자) 구축으로 현실적 평가 환경 조성

4. **우수한 성능**: 기존 강력한 베이스라인(fine-tuned T5, GPT-3.5) 대비 일관된 성능 우월성 입증

## How

![Figure 3](figures/fig3.webp) *텍스트 재표현 예시*

- **패턴 마이닝 모듈**: Flan-T5-Large와 GPT-4를 활용하여 자연언어에서 액션 관련 유언어 패턴(linguistic cues)을 자동 탐지하고, 빈도 분석을 통해 도메인 특화 표현 패턴 축적

- **텍스트 재표현(Text Rephrasing)**: GPT-4를 이용해 복잡하고 불명확한 원문을 더 명확한 형태로 변환하여, 코드 생성 단계의 입력 품질 향상

- **코드 생성(Code Generation)**: 각 액션 타입을 미리 정의된 Python 클래스로 설계하고, 재표현된 텍스트를 입력으로 하여 GPT-4가 클래스 인스턴스 생성 코드를 생성하도록 유도 (few-shot 프롬프팅)

- **코드-자연언어 변환**: 생성된 Python 코드를 사전정의된 규칙으로 자연언어 액션 시퀀스로 역변환하여 최종 출력 생성

- **다중 모듈 파이프라인**: 각 모듈이 독립적으로 작동하여 특정 스텝의 실패가 전체 시스템에 미치는 영향 최소화

## Originality

- **프로그래밍 언어 재포장**: 구조화된 정보 추출을 코드 생성 문제로 재정의함으로써, 기존 텍스트-투-구조(text-to-structure) 태스크의 패러다임 전환 제시

- **LLM 기반 패턴 마이닝**: 도메인 전문가의 수동 규칙 작성 없이 LLM 자체로부터 언어 패턴을 자동 추출하는 자동화된 접근법 도입

- **그래프 매칭 메트릭**: 기존 토큰 수준 평가(F1-score)의 한계를 극복하고 액션 구조의 위계적·의존적 관계를 정량화할 수 있는 신규 평가 방식 제안

- **현실 중심의 벤치마크**: 특허 데이터 중심의 기존 벤치마크와 달리 화학 논문 기반의 더 복잡하고 현실적인 데이터셋 구축

## Limitation & Further Study

- **모델 의존성**: GPT-4 등 상용 LLM에 의존하여 재현성(reproducibility) 제한 및 접근성 문제 가능성 (오픈소스 모델 적용 시험 부족)

- **도메인 특화성**: 화학 합성을 중심으로 평가되었으므로, 타 과학 도메인(생물학, 재료공학 등)으로의 일반화 가능성 미검증

- **액션 정의의 완전성**: 사전정의된 26개 액션 타입이 모든 실험 절차를 포괄하는지 검증 부족, 새로운 액션 타입 추가 시 프레임워크 수정 필요

- **패턴 마이닝의 신뢰도**: LLM 기반 패턴 자동 추출 과정에서의 오류 전파(error propagation) 분석 미흡

- **후속 연구**: (1) 오픈소스 LLM(Llama, Mistral)으로의 확장, (2) 다국어 과학 문헌으로의 적용, (3) 로봇 언어(예: PDDL) 직접 생성으로의 확대, (4) 인간-in-the-loop 피드백 메커니즘 통합

## Evaluation

- **Novelty**: 4/5 — 코드 생성 기반 재정의와 그래프 메트릭은 신선하나, LLM 기반 정보추출 자체는 이미 여러 연구에서 다룬 주제

- **Technical Soundness**: 4/5 — 파이프라인 설계가 논리적이고 실험이 충실하나, 모듈 간 오류 누적 분석 및 ablation study가 심화 필요

- **Significance**: 4/5 — 화학 실험 자동화 및 로봇 실험실 시대에 높은 실용 가치를 가지나, 현재는 화학 도메인에 제한됨

- **Clarity**: 4/5 — 전반적으로 명확하나, 패턴 마이닝 및 코드 생성 과정의 프롬프트 구체화가 더 상세할 필요 있음

- **Overall**: 4/5

**총평**: ActionIE는 프로그래밍 언어의 구조적 특성을 활용하여 과학 문헌의 복잡한 실험 절차를 추출하는 창의적인 접근법을 제시하며, 신규 벤치마크와 평가 메트릭을 통해 실질적 기여를 하였다. 다만 LLM 의존성, 도메인 특화성, 패턴 마이닝의 신뢰도 분석 강화로 더욱 견고한 연구가 될 수 있다.

## Related Papers

- 🔄 다른 접근: [[papers/210_ChemCrow_Augmenting_large-language_models_with_chemistry_too/review]] — Python 코드 생성을 통한 화학 행동 추출과 화학 도구로 증강된 대형 언어모델은 모두 과학 문헌의 실험 절차를 자동화하는 서로 다른 접근법입니다
- 🏛 기반 연구: [[papers/230_Code_llama_Open_foundation_models_for_code/review]] — 코드 생성을 위한 오픈 대형 언어모델은 과학 문헌의 실험 절차를 Python 코드로 변환하는 ActionIE의 기술적 기반입니다
- 🔗 후속 연구: [[papers/212_Chemist-X_Large_Language_Model-empowered_Agent_for_Reaction/review]] — 반응 예측을 위한 대형 언어모델 기반 에이전트는 ActionIE의 화학 합성 행동 추출을 실제 반응 설계로 확장한 응용입니다
