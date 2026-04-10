---
title: "227_Closing_the_loop_Learning_to_generate_writing_feedback_via_l"
authors:
  - "Inderjeet Nair"
  - "Jiaye Tan"
  - "Xiaotian Su"
  - "Anne Gere"
  - "Xu Wang"
date: "2024"
doi: "arXiv:2410.08058"
arxiv: ""
score: 4.2
essence: "본 논문은 **언어 모델 기반 학생 시뮬레이터를 활용하여 작문 피드백 생성 모델(PROF)을 반복적으로 최적화하는 방법**을 제안한다. 실제 학생 참여 없이 피드백의 실효성을 직접 측정하고 개선할 수 있는 자동화된 시스템을 구축한다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Academic_Writing_Personalization"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Schmidt et al._2024_Closing the loop Learning to generate writing feedback via language model simulated student revisio.pdf"
---

# Closing the loop: Learning to generate writing feedback via language model simulated student revisions

> **저자**: Inderjeet Nair, Jiaye Tan, Xiaotian Su, Anne Gere, Xu Wang, Lu Wang | **날짜**: 2024 | **DOI**: [arXiv:2410.08058](https://arxiv.org/abs/2410.08058)

---

## Essence

![Figure 1](figures/fig1.webp) *PROF 파이프라인: 피드백 생성기가 여러 피드백을 샘플링하고, 학생 시뮬레이터를 통해 수정 결과를 평가하며, 선호도 관계를 기반으로 DPO를 통해 반복적으로 최적화되는 과정*

본 논문은 **언어 모델 기반 학생 시뮬레이터를 활용하여 작문 피드백 생성 모델(PROF)을 반복적으로 최적화하는 방법**을 제안한다. 실제 학생 참여 없이 피드백의 실효성을 직접 측정하고 개선할 수 있는 자동화된 시스템을 구축한다.

## Motivation

- **Known**: 언어 모델을 통한 자동 피드백 생성이 가능하며, 정교한 프롬프트 엔지니어링으로 특정 속성을 갖춘 피드백을 생성할 수 있다.

- **Gap**: ① 생성된 피드백이 실제로 학생의 수정 성능을 향상시키는지 명확하지 않다. ② 효과적인 피드백의 속성에 대한 학계적 합의가 부족하여 명시적 지침 작성이 어렵다. ③ 실제 학생을 반복적으로 모집하여 평가하는 것은 비실용적이다.

- **Why**: 피드백의 효과성은 최종적으로 학생이 얼마나 잘 수정하는가로 결정되어야 하며, 이를 측정하기 위한 비용 효율적 방법이 필요하다.

- **Approach**: (1) 학생의 피드백 적용 과정을 에뮬레이션하는 LM 기반 학생 시뮬레이터 개발, (2) 온도(temperature) 조절로 다양한 학생 행동 시뮬레이션, (3) 시뮬레이터의 수정 품질을 기반으로 DPO(Direct Preference Optimization)를 통해 피드백 생성기를 반복 최적화.

## Achievement

![Figure 2](figures/fig2.webp) *온도 변화에 따른 문장 수준의 수정 수 변화: llama3-8b와 gpt-3.5 모두 온도가 증가할수록 추가와 삭제가 증가하며, 실제 학생과 유사한 패턴을 보임*

![Figure 3](figures/fig3.webp) *수정된 에세이 품질 비교: 학생 시뮬레이터들의 성능이 실제 학생과 유사한 궤적을 따르며, 초기 에세이 품질 대비 개선도를 확인*

1. **기존 모델 초월**: GPT-3.5/GPT-4의 소수 샷 프롬프팅보다 **피드백 적용 성능에서 우수**하면서도 8B 파라미터 모델로 훨씬 효율적

2. **레이블 없는 학습**: 고품질 피드백의 대규모 주석 데이터셋 없이도, 그리고 원하는 피드백 속성을 명시하지 않고도 학습 가능

3. **다중 학생 행동 포용성**: 온도 조절을 통해 다양한 학생 수정 양식(보수적 수정부터 공격적 수정까지)에 대응하는 피드백 생성 가능

4. **실제 수정과의 정렬성**: 생성 피드백이 실제 학생 수정과 양호한 정렬을 보이며, LM 시뮬레이터의 신뢰성 입증

## How

![Figure 1](figures/fig1.webp) *반복적 최적화 파이프라인의 상세 프로세스*

- **학생 시뮬레이터 구축 (§3.1)**
  - 363개의 (초기 에세이, 피드백, 수정 에세이) 삼중쌍 데이터 수집
  - 3개 피드백을 GPT-3.5로 통합하여 단일 피드백 생성
  - llama3-8b와 gpt-3.5를 미세 조정하여 피드백 적용 모델 구축
  - 온도 변수를 조절하여 다양한 행동 시뮬레이션

- **피드백 생성기 초기화 (§3.2)**
  - llama3-8b 기반으로 291개 훈련 샘플(873개 피드백)로 미세 조정
  - (초기 에세이, 개별 피드백) 쌍으로 학습

- **반복적 최적화 (§3.3)**
  - **반복 t에서**: 
    1. 현재 생성기 Mt에서 K개 피드백 샘플링
    2. 학생 시뮬레이터로 각 피드백에 대한 수정 생성
    3. GPT-4로 수정된 에세이 품질 평가 (코스 루브릭 기준)
    4. 최고/최저 품질 수정 쌍을 기반으로 선호도 관계 구성
    5. DPO 손실함수로 Mt+1 업데이트
  
- **DPO 손실함수 (Eq. 2)**
  - 고품질 피드백의 로그 확률을 증가, 저품질 피드백을 감소시켜 판별 능력 강화
  - 선호도 관계를 통한 약한 감독(weak supervision) 방식

## Originality

- **새로운 문제 정의**: 피드백의 추상적 속성 대신 **학생의 실제 수정 성능을 직접 최적화 목표**로 설정 (기존 피드백 생성 연구와 차별화)

- **LM 시뮬레이터의 창의적 활용**: 온도 파라미터로 **다양한 학생 행동을 체계적으로 생성**하여 포괄적 테스트 환경 구축

- **레이블 자유 학습**: 고가의 전문가 주석이나 명시적 속성 정의 없이 **자동 선호도 관계 구성**으로 학습

- **폐쇄 루프 설계**: 피드백-수정-평가의 완전한 순환 구조를 통해 **실제 교육 효과를 직접 최적화**

## Limitation & Further Study

- **시뮬레이터 신뢰도**: LM 학생 시뮬레이터가 실제 학생의 인지 과정을 완벽히 재현하지 못할 가능성 (정성적 피드백 해석 능력 제한)

- **단일 과제 평가**: 경제학 개론 에세이(최소 임금 정책)라는 특정 도메인에서만 검증되어 **일반화 가능성 미검증**

- **평가자 의존성**: GPT-4를 에세이 품질 판정자로 사용하여 LM 기반 평가의 편향성 내재

- **온도 조절의 제한**: 다양한 학생 행동 생성에 온도만 사용하여, 다른 생성 파라미터(top-p, top-k)의 효과는 미탐색

- **후속 연구**: 
  - 실제 학생 그룹과의 대규모 검증 연구
  - 다양한 교과(수학, 과학, 언어)와 과제 유형으로의 확대
  - 다국어 피드백 생성 확장
  - 학생의 개인 특성(배경, 학습 스타일)을 고려한 맞춤형 피드백

## Evaluation

- **Novelty**: 4.5/5
  - 피드백 효과성을 직접 최적화하는 접근은 참신하고, 온도를 통한 학생 시뮬레이터 다양화도 창의적이나, LM 시뮬레이터 자체는 기존 기술의 응용

- **Technical Soundness**: 4/5
  - DPO 기반 최적화 프레임워크는 견고하고, 실험 설계도 논리적이나, 단일 과제 데이터와 제한된 규모(363개)로 인한 일반화 우려

- **Significance**: 4/5
  - 교육 AI에 실질적 기여(비용 효율적 피드백 최적화)이지만, 실제 학생 검증 부족으로 현장 임팩트 미확인

- **Clarity**: 4.5/5
  - 논문 구조가 명확하고 파이프라인 설명이 직관적이며, 대부분 재현 가능하나 일부 하이퍼파라미터(K값, 반복 횟수, β값) 상세 기술 미흡

- **Overall**: 4.2/5

**총평**: 본 논문은 LM 시뮬레이터를 활용하여 피드백 생성을 반복적으로 최적화하는 창의적 방법론을 제시하며, 기존 대형 모델을 능가하는 효율적이고 효과적인 시스템을 구현했다. 다만 단일 과제 검증과 실제 학생 참여 평가 부재가 실제 교육 현장으로의 전환 가능성을 제한한다.

## Related Papers

- ⚖️ 반론/비판: [[papers/284_Does_writing_with_language_models_reduce_content_diversity_a/review]] — AI 어시스턴트가 학습에 도움이 된다는 관점과 콘텐츠 다양성을 감소시킨다는 우려가 상반됨
- 🔄 다른 접근: [[papers/656_Read_revise_repeat_A_system_demonstration_for_human-in-the-l/review]] — 둘 다 인간-AI 협력 글쓰기를 다루지만, 하나는 학생 시뮬레이터 기반 피드백, 다른 하나는 직접적 인간 피드백 방식임
- 🔗 후속 연구: [[papers/414_Human-llm_coevolution_Evidence_from_academic_writing/review]] — 인간-LLM 협력 글쓰기의 일반적 패턴을 교육적 맥락으로 확장하여 피드백 생성에 특화된 방법론을 개발함
- ⚖️ 반론/비판: [[papers/284_Does_writing_with_language_models_reduce_content_diversity_a/review]] — AI가 콘텐츠 다양성을 감소시킨다는 우려와 교육적 피드백 개선에 도움된다는 관점이 상반됨
- 🔄 다른 접근: [[papers/656_Read_revise_repeat_A_system_demonstration_for_human-in-the-l/review]] — 둘 다 인간-AI 협력 글쓰기를 다루지만 하나는 직접적 인간 피드백, 다른 하나는 학생 시뮬레이터 기반 접근임
- 🔗 후속 연구: [[papers/423_Improving_grammatical_error_correction_via_contextual_data_a/review]] — 작문 피드백 생성을 문법 오류 수정의 문맥 기반 증강으로 확장하여 더 정교한 오류 패턴 학습을 제공합니다.
