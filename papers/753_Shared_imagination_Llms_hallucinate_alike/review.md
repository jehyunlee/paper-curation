---
title: "753_Shared_imagination_Llms_hallucinate_alike"
authors:
  - "Yilun Zhou"
  - "Caiming Xiong"
  - "Silvio Savarese"
  - "Chien-Sheng Wu"
date: "2024"
doi: "arXiv:2407.16604"
arxiv: ""
score: 4.0
essence: "최신 대규모 언어모델(LLM)들이 서로 다른 아키텍처와 학습 데이터를 가짐에도 불구하고, 허구적(imaginary) 개념에 대해 놀라울 정도로 일관성 있게 환각(hallucination)을 생성하며 이를 \"공유된 상상 공간(shared imagination space)\"이라고 명명한다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/AI_Review_Detection"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Zhou et al._2024_Shared imagination Llms hallucinate alike.pdf"
---

# Shared imagination: Llms hallucinate alike

> **저자**: Yilun Zhou, Caiming Xiong, Silvio Savarese, Chien-Sheng Wu | **날짜**: 2024 | **DOI**: [arXiv:2407.16604](https://arxiv.org/abs/2407.16604)

---

## Essence

![Figure 2](https://arxiv.org/html/2407.16604v1/x2.png) *직접 질문(DQ)과 맥락 기반 질문(CQ)에 대한 정확도 및 응답률*

최신 대규모 언어모델(LLM)들이 서로 다른 아키텍처와 학습 데이터를 가짐에도 불구하고, 허구적(imaginary) 개념에 대해 놀라울 정도로 일관성 있게 환각(hallucination)을 생성하며 이를 "공유된 상상 공간(shared imagination space)"이라고 명명한다.

## Motivation

- **Known**: 최근 LLM들은 유사한 트랜스포머 아키텍처, 공통 사전학습 데이터, SGD 기반 최적화를 공유하고 있음
- **Gap**: 이러한 구조적 유사성이 실제로 모델들의 출력 행동에 어떻게 반영되는지는 미지의 영역
- **Why**: LLM의 근본적 특성 이해와 환각 탐지, 창의성 활용에 대한 시사점 도출 필요
- **Approach**: 허구적 개념에 대한 질문 생성 및 답변 과정을 통해 모델 간 암묵적 합의 정도 측정

## Achievement

![Figure 1](https://arxiv.org/html/2407.16604v1/x1.png) *상상적 질문 답변(IQA) 프레임워크의 개요*

1. **높은 일관성 발견**: 직접 질문(DQ)에서 평균 54% 정확도(무작위 확률 25%), 맥락 기반 질문(CQ)에서 86% 정확도 달성
2. **모델 군집화**: 동일 모델 또는 같은 모델 계열 내에서 정확도가 더욱 향상되며, 특정 (QM, AM) 쌍에서 96% 도달
3. **6개 핵심 연구 질문 해결**: 데이터 특성, 휴리스틱 기반 선택, 허구성 인식, 모델 워밍업 효과, 현상의 보편성, 다른 콘텐츠 유형 적용성에 대한 포괄적 분석
4. **모델 동질성 증명**: 벤치마크 성능이 크게 다른 모델들도 환각 공간에서 높은 동질성 보유

## How

- **IQA 설계**: 질문 모델(QM)이 허구적 개념에 대한 객관식 질문 생성 → 답변 모델(AM)이 (QM과 독립적으로) 답변 시도
- **두 가지 생성 방식**:
  - 직접 질문(DQ): QM이 단독으로 허구 개념 질문 생성
  - 맥락 질문(CQ): QM이 먼저 허구 개념 설명 문단 작성 후 질문 생성
- **모델 군**: GPT(3.5, 4, 4-Turbo, 4o), Claude(3-Haiku, 3-Sonnet, 3-Opus, 3.5-Sonnet), Mistral(7B, 8x7B, Large), Llama 3(8B, 70B) 등 13개 모델 실험
- **평가 지표**: 정확도(κ) = 정답률/답변한 질문 수, 응답률(α) = 답변한 질문 수/전체 질문 수
- **분석**: 임베딩 공간 시각화, 코사인 유사도 측정, 단어 클라우드, 휴리스틱 검증, 허구성 인식 평가, 순차 생성 효과 검토

## Originality

- **새로운 평가 프레임워크**: 환각 연구의 새로운 관점으로서 IQA 설계—실제 사실이 아닌 허구적 내용에 대한 모델 간 암묵적 합의 측정
- **"공유된 상상 공간" 개념 제시**: LLM들이 마치 같은 "수학적 표현 공간"에 내재된 허구적 개념을 공유하는 현상 발견
- **포괄적 실증 분석**: 단순 현상 보고를 넘어 6개 핵심 질문을 통한 체계적 조사(데이터 동질성, 휴리스틱 기제 부재, 모델 인식 능력의 한계 등)
- **구조적 차이의 부재 발견**: ChatGPT 이후 모델들의 예외적 동질성과 사전학습 모델의 상대적 이질성 구분

## Limitation & Further Study

- **샘플 규모**: 주제당 모델당 20개 질문은 통계적 견고성 측면에서 다소 제한적일 수 있음
- **인과 메커니즘 미해명**: 왜 "공유된 상상 공간"이 형성되는지의 근본 원인(사전학습 데이터의 중첩, 유사 아키텍처의 수렴, 인스트럭션 튜닝의 정렬화 등)이 완전히 설명되지 않음
- **제한된 도메인**: 학문적 개념과 창작 글에 초점—다른 유형의 환각(사실 왜곡, 시간적 비일관성 등)에 대한 확장 필요
- **후속 연구 방향**:
  - 모델 스케일, 학습 데이터, 아키텍처 변수 간 동질성 관계의 원인 분석
  - 환각 탐지 및 완화 기법 개발
  - 모델 간 "상상 공간" 차원 축소 표현(latent representation) 추출
  - 미세조정(fine-tuning)이 공유 상상 공간에 미치는 영향 분석

## Evaluation

- **Novelty**: 4.5/5 — IQA 프레임워크와 "공유된 상상 공간" 개념이 참신하나, 환각 연구의 근본 원인은 미해명
- **Technical Soundness**: 4/5 — 실험 설계는 체계적이나, 통계 검증(유의성 테스트 등)이 부재하고 샘플 규모 제한
- **Significance**: 4/5 — LLM 동질성, 환각의 구조적 이해에 중요한 통찰을 제공하지만, 실제 응용 영향은 아직 제한적
- **Clarity**: 4.5/5 — 명확한 시각화와 논리적 구성이지만, 일부 기술적 세부사항(임베딩 계산, 통계 방법)에 대한 상세 설명 부족
- **Overall**: 4/5

**총평**: 이 논문은 LLM들의 동질성을 환각의 관점에서 창의적으로 조명하는 신선한 연구로, 6가지 연구질문을 통한 포괄적 실증 분석이 돋보인다. 다만 현상의 근본 메커니즘 해명 및 실제적 활용 가능성 제시가 보강되면 더욱 영향력 있는 기여가 될 것으로 예상된다.

## Related Papers

- 🔗 후속 연구: [[papers/610_Pelican_Correcting_Hallucination_in_Vision-LLMs_via_Claim_De/review]] — LLM들의 공유된 환각 패턴 분석이 시각-언어 모델의 환각 보정에서 일관된 오류 유형을 사전에 식별하고 대응하는 데 활용된다.
- 🔗 후속 연구: [[papers/752_Shallow_synthesis_of_knowledge_in_gpt-generated_texts_A_case/review]] — 공유된 상상 공간 개념이 GPT의 얕은 문헌 종합 문제를 더 깊이 이해하는 이론적 틀을 제공한다.
- 🏛 기반 연구: [[papers/881_When_ai_co-scientists_fail_Spot-a_benchmark_for_automated_ve/review]] — LLM의 일관된 환각 패턴이 과학 논문 오류 검증에서 예측 가능한 실패 모드를 이해하는 핵심 개념적 기반을 제공한다.
- 🏛 기반 연구: [[papers/396_Hallucination_mitigation_using_agentic_ai_natural_language-b/review]] — LLM이 유사한 환각을 생성하는 현상에 대한 기초 연구로 환각 완화 접근법의 이론적 배경을 제공한다.
- 🏛 기반 연구: [[papers/192_Cchall_A_novel_benchmark_for_joint_cross-lingual_and_cross-m/review]] — LLM들이 유사한 환각을 보인다는 기초 연구가 교차-언어/모달 환각 벤치마크 개발의 이론적 근거를 제공함
- 🏛 기반 연구: [[papers/610_Pelican_Correcting_Hallucination_in_Vision-LLMs_via_Claim_De/review]] — 두 논문 모두 LLM의 환각 문제를 다루며, 공유된 상상 공간 개념이 시각-언어 모델의 환각 보정 메커니즘 이해에 중요한 기반을 제공한다.
- 🏛 기반 연구: [[papers/752_Shallow_synthesis_of_knowledge_in_gpt-generated_texts_A_case/review]] — LLM의 공유된 환각 패턴이 관련 연구 섹션 작성에서 나타나는 얕은 지식 종합 문제의 근본적 원인을 이해하는 데 중요한 통찰을 제공한다.
- 🔗 후속 연구: [[papers/881_When_ai_co-scientists_fail_Spot-a_benchmark_for_automated_ve/review]] — LLM의 공유된 환각 패턴이 과학 논문 오류 검증에서 나타나는 낮은 성능의 근본적 원인을 설명하는 이론적 틀을 제공한다.
- 🔄 다른 접근: [[papers/565_Multi-novelty_Improve_the_diversity_and_novelty_of_contents/review]] — LLM의 유사한 환각 패턴 문제를 다중 관점 임베딩으로 해결하려는 접근법이다
