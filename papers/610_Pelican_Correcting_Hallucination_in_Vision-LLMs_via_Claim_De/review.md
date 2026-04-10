---
title: "610_Pelican_Correcting_Hallucination_in_Vision-LLMs_via_Claim_De"
authors:
  - "Pritish Sahu"
  - "Karan Sikka"
  - "Ajay Divakaran"
date: "2024"
doi: "10.48550/ARXIV.2407.02352"
arxiv: ""
score: 4.0
essence: "시각 언어 모델(LVLM)의 환각(hallucination) 문제를 1차 술어(first-order predicates) 기반 청구 분해와 파이썬 코드 생성을 통해 검증하고 보정하는 프레임워크를 제안한다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Self-Refining_Text_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Sahu et al._2024_Pelican Correcting Hallucination in Vision-LLMs via Claim Decomposition and Program of Thought Veri.pdf"
---

# Pelican: Correcting Hallucination in Vision-LLMs via Claim Decomposition and Program of Thought Verification

> **저자**: Pritish Sahu, Karan Sikka, Ajay Divakaran | **날짜**: 2024 | **DOI**: [10.48550/ARXIV.2407.02352](https://doi.org/10.48550/ARXIV.2407.02352)

---

## Essence

![Figure 1](figures/fig1.webp)
*Pelican의 전체 파이프라인: 시각적 표(Visual Table) 구성, 청구(Claim) 분해, Program-of-Thought 코드 생성, 통합 검증 종합*

시각 언어 모델(LVLM)의 환각(hallucination) 문제를 1차 술어(first-order predicates) 기반 청구 분해와 파이썬 코드 생성을 통해 검증하고 보정하는 프레임워크를 제안한다.

## Motivation

- **Known**: 기존 LVLM은 강력한 성능을 보이지만 제한된 학습 데이터, 부정확한 시각적 접지(grounding), 언어 선행성(language priors)에 대한 과도한 의존으로 인해 환각 문제가 심각하다.

- **Gap**: 기존 청구 검증 방법(예: Woodpecker)은 정확한 객체 인스턴스 접지 부재, 약한 상황적 통합, 비효과적인 추론 등의 한계를 가진다. 특히 다중 객체를 포함하는 청구에서 중간 변수를 통한 정밀한 접지가 필요하다.

- **Why**: 시각적 청구의 정확한 검증을 위해서는 (1) 객체 인스턴스의 명확한 참조, (2) 외부 도구와 파이썬 연산자의 유연한 조합, (3) 부분 청구 간 계산 공유를 통한 일관성 검증이 필수적이다.

- **Approach**: 청구를 구조화된 부분 청구 체인으로 분해하고, Program-of-Thought 방식으로 파이썬 코드를 생성하여 중간 변수와 공유 계산을 활용하되, LLM의 추론 능력으로 최종 검증을 수행한다.

## Achievement

![Figure 2](figures/fig2.webp)
*부분 청구로부터 생성된 계산 그래프: 술어를 노드로, 의존성을 간선으로 표현*

1. **환각 감소 성능**: MMHal-Bench에서 다양한 LVLM 기준선 대비 8%-32% 환각 감소, 기존 환각 완화 방법 대비 27% 감소 달성

2. **강화된 접지**: 중간 변수($person_riding 등)를 통한 정확한 객체 인스턴스 참조로 다중 객체 청구에서의 정밀도 향상

3. **일관성 검증**: 부분 청구 간 계산 공유를 통해 불일치(inconsistency) 식별 및 적응적 보정 가능

4. **다중 벤치마크 검증**: GAVIE, MME 데이터셋에서도 일관된 성능 개선 입증

## How

![Figure 1](figures/fig1.webp)
*4단계 파이프라인: (Step 1) 시각적 표 구성, (Step 2) 청구 분해, (Step 3) Program-of-Thought 코드 생성, (Step 4) 통합 검증*

- **Visual Table 생성**: YOLO와 Grounding-DINO를 결합하여 이미지에서 핵심 시각적 객체를 탐지하고 Pandas dataframe 형태로 표현화. 이를 통해 객체 검출의 폐쇄 어휘(closed-vocabulary) 한계와 개방 어휘 모델의 거짓양성(false-positive) 문제 완화

- **청구 분해(Claim Decomposition)**: LLM의 추론 능력을 활용하여 복잡한 청구를 1차 술어 기반의 세분화된 부분 청구로 변환. 각 부분 청구는 (술어, 질문) 쌍으로 구성되며 계산 그래프의 노드 역할

- **Program-of-Thought 코드 생성**: 부분 질문들을 파이썬 코드로 번역하여 외부 시각 도구(VQA 등)와 네이티브 파이썬 연산자를 유연하게 조합. 이전 노드의 결과를 다음 질문에 공유변수로 활용

- **통합 검증 종합(Integrated Verification Synthesis)**: LLM의 Chain-of-Thought 추론으로 각 부분 청구의 답변 일관성, 신뢰도(confidence), 관련성을 평가하여 원본 청구의 정확성 판단 및 필요시 보정

## Originality

- **구조화된 분해**: 1차 술어를 기반으로 한 명시적인 청구 분해로 계산 그래프를 형성하여, 기존 자유형식 분해 방식 대비 명확한 의존성 표현

- **중간 변수 도입**: 객체 인스턴스에 대한 정밀한 참조를 위해 $dog_right, $person_riding 같은 중간 변수를 도입하여 다중 객체 상황에서의 접지 정확도 향상

- **공유 계산 메커니즘**: 부분 청구 간 계산 결과를 명시적으로 공유하여 일관성 검증과 비효율성 감지를 가능하게 하고, 단순 순차적 응답과 차별화

- **유연한 도구 조합**: Program-of-Thought를 통한 파이썬 코드 생성으로 외부 도구 간 복잡한 조합을 표현 가능(Woodpecker의 제한된 도구 활용 초과)

- **다층 추론**: 계산 기반 답변(실행)과 언어 기반 추론(평가)의 통합으로 정밀성과 유연성 동시 확보

## Limitation & Further Study

- **도구 의존성**: 여전히 객체 검출기의 성능에 의존하며, 완벽한 검출을 보장하지 못함. 검출 실패 시 청구 분해의 정확성 저하 가능성

- **계산 비용**: 부분 청구 생성, 코드 생성, 코드 실행, 최종 검증 등 다단계 파이프라인으로 인한 높은 계산 오버헤드

- **술어 집합 확장성**: 현재 제한된 1차 술어 집합(Exists, Position, Color 등)을 기반으로 설계되어, 새로운 술어 추가 시 재설계 필요

- **일반화 성능**: 현재 VQA 중심 작업에 초점, 다른 유형의 시각적 추론 작업(예: 시각적 관계 이해, 공간 추론)으로의 확장성 미검증

- **후속 연구 방향**: (1) 시각 도구의 오류 감지 및 보정 메커니즘 강화, (2) 계산 비용 최적화를 위한 스케줄링 기법, (3) 시각 도메인 밖의 다중모달 청구 검증 확대, (4) 명시적 설명 생성을 통한 해석성 향상


## Evaluation

- Novelty: 4/5
- Technical Soundness: 4.5/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: Pelican은 시각 언어 모델의 환각 문제를 체계적으로 접근하는 견고한 프레임워크로, 중간 변수와 계산 공유라는 실질적 개선을 통해 SOTA 대비 의미 있는 성능 향상을 달성했으나, 높은 계산 비용과 시각 도구 의존성이 실무 적용 시 제약이 될 수 있다.

## Related Papers

- 🏛 기반 연구: [[papers/753_Shared_imagination_Llms_hallucinate_alike/review]] — 두 논문 모두 LLM의 환각 문제를 다루며, 공유된 상상 공간 개념이 시각-언어 모델의 환각 보정 메커니즘 이해에 중요한 기반을 제공한다.
- 🔄 다른 접근: [[papers/790_Teaching_Large_Language_Models_to_Self-Debug/review]] — 코드 디버깅과 시각적 주장 검증은 모두 자기 수정 메커니즘을 활용하지만, 서로 다른 모달리티에서 오류 검출과 보정 방법을 제시한다.
- 🔗 후속 연구: [[papers/242_CRITIC_Large_Language_Models_Can_Self-Correct_with_Tool-Inte/review]] — CRITIC의 도구 기반 자기 수정 프레임워크를 시각-언어 영역으로 확장하여 더 구조화된 검증 과정을 제공한다.
- 🔗 후속 연구: [[papers/753_Shared_imagination_Llms_hallucinate_alike/review]] — LLM들의 공유된 환각 패턴 분석이 시각-언어 모델의 환각 보정에서 일관된 오류 유형을 사전에 식별하고 대응하는 데 활용된다.
- 🔄 다른 접근: [[papers/790_Teaching_Large_Language_Models_to_Self-Debug/review]] — 코드 자기 디버깅과 시각적 주장 검증은 모두 자기 수정 메커니즘을 활용하지만 실행 피드백과 논리적 분해라는 서로 다른 검증 방법을 사용한다.
