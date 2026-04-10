---
title: "387_Gpt-4_technical_report"
authors:
  - "OpenAI"
date: "2023"
doi: "N/A"
arxiv: ""
score: 4.5
essence: "GPT-4는 이미지와 텍스트를 입력받아 텍스트를 출력하는 멀티모달 대규모 언어 모델로, 법학시험(Bar Exam) 상위 10% 수준의 성능을 달성하며 인간 수준의 전문가 및 학업 벤치마크 성능을 보여준다. 특히 훈련 규모 확장 시 성능 변화를 정확히 예측할 수 있는 인프라 구축을 핵심으로 한다."
tags:
  - "cat/Scientific_Language_Processing_and_Visualization"
  - "sub/Scientific_Language_Models"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/OpenAI and N._2023_Gpt-4 technical report.pdf"
---

# GPT-4 Technical Report

> **저자**: OpenAI | **날짜**: 2023 | **DOI**: N/A

---

## Essence

GPT-4는 이미지와 텍스트를 입력받아 텍스트를 출력하는 멀티모달 대규모 언어 모델로, 법학시험(Bar Exam) 상위 10% 수준의 성능을 달성하며 인간 수준의 전문가 및 학업 벤치마크 성능을 보여준다. 특히 훈련 규모 확장 시 성능 변화를 정확히 예측할 수 있는 인프라 구축을 핵심으로 한다.

## Motivation

- **Known**: 대규모 언어 모델의 자연언어 이해 및 생성 능력이 계속 개선되고 있으며, 이들은 대화 시스템, 텍스트 요약, 기계 번역 등 광범위한 응용 분야를 가짐.

- **Gap**: 매우 거대한 훈련 실행(training run)의 경우 모델별 튜닝이 불가능하며, 훈련 전 모델의 성능을 예측하기 어려움. 또한 기존 모델들은 신뢰성 부족, 문맥 길이 제한, 경험 학습 불가능 등의 한계를 가짐.

- **Why**: 초대규모 모델의 배포 전 성능 예측은 정렬(alignment), 안전성, 배포 전략 결정에 중요하며, 일관된 확장 법칙(scaling laws) 발견은 과학적 이해도 향상.

- **Approach**: (1) 다양한 규모에서 예측 가능한 동작을 하는 딥러닝 인프라 및 최적화 방법 개발, (2) 소규모 모델(GPT-4의 1/1,000 ~ 1/10,000 규모)로부터 성능 예측, (3) 인간 시험을 통한 광범위한 능력 평가, (4) 강화학습 피드백(RLHF) 기반 정렬.

## Achievement

![Figure 1](figures/fig1.webp)
*그림 1: GPT-4 및 소규모 모델의 성능. 내부 코드베이스 데이터셋에서의 최종 손실값(bits per word). 소규모 모델로부터의 전력 법칙 적합이 GPT-4의 최종 손실을 정확히 예측.*

![Figure 2](figures/fig2.webp)
*그림 2: HumanEval 부분집합에서의 평균 로그 통과율. 전력 법칙 적합이 GPT-4 성능을 매우 정확히 예측.*

1. **확장 법칙의 정확한 예측**: 손실값(loss) 예측에서 L(C) = aC^b + c 형태의 전력 법칙을 사용하여 GPT-4의 최종 손실을 높은 정확도로 사전 예측. 코딩 능력(HumanEval)도 −E_P[log(pass_rate(C))] = α·C^−k 관계로 1,000배 이상 작은 모델로부터 정확히 예측.

2. **인간 수준의 시험 성적**: 법학시험(Bar Exam) 상위 10%, LSAT 상위 12%, SAT 수학 상위 11%, GRE 언어 상위 1% 수준의 성능 달성. 기존 GPT-3.5는 법학시험에서 하위 10%였음.

3. **다언어 우수성**: MMLU 벤치마크 26개 언어 중 24개에서 영어 최고 성능(SOTA) 초과.

4. **역확장 현상 해결**: Inverse Scaling Prize의 Hindsight Neglect 과제에서 기존 모델은 규모가 클수록 성능 저하를 보였으나, GPT-4는 이 추세를 반전시킴.

5. **멀티모달 능력**: 이미지와 텍스트를 동시에 처리 가능하며, 비전 기능 제거 후에도 대부분의 시험에서 동일하거나 유사한 성능 유지.

## How

- **확장 가능한 인프라**: 광범위한 컴퓨팅 규모에서 일관되게 동작하는 최적화 방법 개발으로 모델별 튜닝 의존도 최소화.

- **전력 법칙 적합(Power Law Fitting)**: 소규모 모델(최대 GPT-4의 1/10,000 규모)의 손실값과 능력 지표(HumanEval 통과율)에 대해 전력 함수 형태로 적합하고, 이를 외삽(extrapolation)하여 GPT-4 성능 예측.

- **Transformer 기반 아키텍처**: 다음 토큰 예측(next token prediction)으로 사전 훈련, 공개 데이터 및 제3자 라이선스 데이터 사용.

- **강화학습 정렬(RLHF)**: 인간 피드백 기반 보상 모델을 통한 사후 훈련으로 사실성(factuality)과 원하는 행동 준수 개선.

- **오염(Contamination) 제어**: 시험에 포함된 훈련 데이터를 식별하여 제거한 변형(variant) 실행, 낮은 점수 보고 원칙.

- **적대적 테스팅 및 안전 파이프라인**: 도메인 전문가와의 적대적 테스팅, 모델 보조 안전 파이프라인 구축으로 편향, 허위정보, 과신뢰, 개인정보, 사이버 보안, 확산 등의 위험 완화.

## Originality

- **확장 예측의 시스템화**: 소규모 모델 실행으로부터 거대 모델 성능을 사전에 정확히 예측하는 일반적 방법론 제시. 기존 연구(Henighan et al., Wei et al.)를 발전시켜 역확장 현상까지 포착.

- **멀티모달 통합**: 텍스트만이 아닌 이미지 입력 처리로 모달리티 확장. 시각 정보가 필요한 시험 문제 평가 가능.

- **포괄적 벤치마킹**: 30개 이상의 학업 및 전문 시험(Bar Exam, LSAT, SAT, GRE, AP, AMC 등)에 대한 체계적 평가로 인간 수준 성능을 객관적으로 입증. 기존 연구는 NLP 특화 벤치마크에 집중.

- **성능 예측의 사전 등록(Pre-registration)**: 대규모 훈련 완료 전 예측값을 공식 등록하여 사후 분석 편향(hindsight bias) 제거.

- **안전성 체계화**: 비용-편익 투명성 밸런싱과 시스템 카드(System Card) 작성으로 위험 공개 및 완화 방안 제시.

## Limitation & Further Study

- **신뢰성 부족**: 환각(hallucination), 추론 오류 등 발생 가능. 신뢰성이 중요한 문맥(의료, 법률 등)에서 신중한 사용 필요.

- **문맥 길이 제한**: 처리할 수 있는 최대 입력 길이 제약이 존재하여 장문 문서 처리에 한계.

- **비경험 학습**: 단일 세션 내에서 새로운 정보를 학습하지 못하며, 배포 후 변화하는 세계에 적응 불가능.

- **예측 불가능한 능력**: Inverse Scaling Prize의 일부 과제처럼 특정 능력은 여전히 예측 어려움. 문제별로 성능이 규모 증가에 따라 때로 악화되는 경우 존재.

- **아키텍처 및 훈련 세부사항 미공개**: 경쟁 및 안전 고려로 모델 크기, 하드웨어, 훈련 계산, 데이터셋 구성 등 공개하지 않음. 향후 독립 감시(independent auditing)와 선별된 제3자 공개 계획.

- **후속 연구 방향**: (1) 더 정확한 능력 예측 방법론 정제, (2) 대규모 훈련 전 다양한 능력에 대한 성능 예측의 사전 등록 관행화, (3) 사회경제적 영향 및 규제 필요성 분석, (4) 멀티모달 이해 능력 심화.

## Evaluation

- **Novelty (독창성)**: 4.5/5
  - 확장 예측 방법론 및 멀티모달 통합은 신선하나, Transformer 기반 아키텍처 자체는 기존 기술 활용. 시험 기반 평가 프레임워크는 창의적.

- **Technical Soundness (기술적 건전성)**: 4.5/5
  - 전력 법칙 적합 방법론이 견고하고 예측 검증도 체계적. 다만 아키텍처 세부사항 미공개로 재현성 제한. RLHF 정렬 과정의 상세 내용 부족.

- **Significance (중요성)**: 5/5
  - 인간 수준 성능 달성은 AI 발전의 이정표. 확장 예측 능력은 거대 모델 개발 전략의 패러다임 변화. 멀티모달 능력은 실용성 대폭 확대. 산업 및 학계에 막대한 영향.

- **Clarity (명확성)**: 4/5
  - 전반적으로 명확한 구성과 광범위한 벤치마크 제시. 그러나 훈련 방법론, 안전 개입의 구체적 효과, 공개하지 않은 세부사항이 많아 완전한 이해는 어려움.

- **Overall (종합)**: 4.5/5
  - 매우 강력한 실증적 결과와 신선한 방법론을 제시하나, 투명성 제한과 재현성 제약이 있음.

---

## 총평

GPT-4는 Transformer 기반 멀티모달 모델로서 인간 수준의 시험 성적 달성, 정확한 확장 예측 능력, 다언어 우수성을 통해 대규모 언어 모델 개발의 새로운 경지를 보여준다. 특히 소규모 모델로부터 거대 모델 성능을 사전 예측할 수 있다는 발견은 과학적 이해도와 배포 안전성을 동시에 향상시키는 기여이다. 다만 아키텍처 및 훈련 세부사항 미공개, 환각·신뢰성 부족, 제한된 문맥 길이 등 한계가 존재하며, 독립적 검증과 추가 투명성이 필요하다.

## Related Papers

- 🔄 다른 접근: [[papers/369_Gemini_a_family_of_highly_capable_multimodal_models/review]] — Gemini와 함께 멀티모달 AI의 양대 모델로 서로 다른 회사의 접근법을 대표함
- 🧪 응용 사례: [[papers/477_Large_language_models_pass_the_turing_test/review]] — GPT-4의 발전된 언어 능력이 튜링 테스트 통과라는 구체적 성과로 입증됨
- 🔗 후속 연구: [[papers/322_Evaluation_of_openai_o1_Opportunities_and_challenges_of_agi/review]] — GPT-4를 기반으로 한 OpenAI o1의 추론 능력 평가 연구
- 🔄 다른 접근: [[papers/801_The_llama_3_herd_of_models/review]] — GPT-4와 경쟁하는 Meta의 오픈소스 언어 모델 시리즈
- 🔄 다른 접근: [[papers/266_Deepseek-v3_technical_report/review]] — GPT-4와 경쟁하는 대규모 MoE 모델로 효율성과 성능 면에서 다른 접근법을 제시
- 🔄 다른 접근: [[papers/369_Gemini_a_family_of_highly_capable_multimodal_models/review]] — GPT-4와 경쟁하는 Google의 멀티모달 모델로 다른 회사의 접근법을 보여줌
- 🧪 응용 사례: [[papers/477_Large_language_models_pass_the_turing_test/review]] — GPT-4 같은 고성능 LLM이 인간과 구별되지 않을 정도로 발전했음을 실증적으로 증명
- 🔄 다른 접근: [[papers/370_Gemma_2_Improving_open_language_models_at_a_practical_size/review]] — GPT-4와 경쟁할 수 있는 성능을 훨씬 작은 모델 크기로 달성하는 다른 접근법
