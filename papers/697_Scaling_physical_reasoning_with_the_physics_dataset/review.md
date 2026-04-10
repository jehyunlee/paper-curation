---
title: "697_Scaling_physical_reasoning_with_the_physics_dataset"
authors:
  - "Shenghe Zheng"
  - "Qianjia Cheng"
  - "Junchi Yao"
  - "Mengsong Wu"
  - "Haonan He"
date: "2025"
doi: "arXiv:2506.00022v4"
arxiv: ""
score: 4.2
essence: "대규모 언어 모델(LLM)이 물리학 추론 능력 개발에 충분한 주목을 받지 못했던 문제를 해결하기 위해, 100개 이상의 교과서로부터 정제된 16,568개의 고품질 물리 문제를 포함하는 PHYSICS 데이터셋을 소개한다. 물리 분야에 특화된 평가 프레임워크(Rule+Model)를 최초로 제안하여 단위 변환, 수치 간단히 하기 등의 물리 고유 특성을 반영한 정확한 평가를 가능하게 한다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/Structured_Research_Frameworks"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Zheng et al._2025_Scaling physical reasoning with the physics dataset.pdf"
---

# Scaling physical reasoning with the physics dataset

> **저자**: Shenghe Zheng, Qianjia Cheng, Junchi Yao, Mengsong Wu, Haonan He, Ning Ding, Yu Cheng, Shuyue Hu, Lei Bai, Dongzhan Zhou, Ganqu Cui, Peng Ye | **날짜**: 2025 | **DOI**: [arXiv:2506.00022v4](https://arxiv.org/abs/2506.00022)

---

## Essence

![Figure 1](figures/fig1.webp)
*PHYSICS 데이터셋 구축 파이프라인(좌)과 주요 특성(우)*

대규모 언어 모델(LLM)이 물리학 추론 능력 개발에 충분한 주목을 받지 못했던 문제를 해결하기 위해, 100개 이상의 교과서로부터 정제된 16,568개의 고품질 물리 문제를 포함하는 PHYSICS 데이터셋을 소개한다. 물리 분야에 특화된 평가 프레임워크(Rule+Model)를 최초로 제안하여 단위 변환, 수치 간단히 하기 등의 물리 고유 특성을 반영한 정확한 평가를 가능하게 한다.

## Motivation

- **Known**: LLM은 수학과 코딩 경쟁에서 올림피아드 수준의 성능을 달성했으나, 현실 세계 이해의 기초인 물리학은 제한된 주목을 받음

- **Gap**: (1) 고품질 물리 훈련 데이터 부족 (2) 기존 평가 프레임워크가 물리 고유 문제(단위 변환, 수치 근사 등)를 제대로 처리하지 못함 (3) 난이도와 주제 분포가 불균형한 테스트 데이터

- **Why**: AI가 현실 세계를 정확히 모델링하고 상호작용하기 위해서는 물리학적 추론 능력이 필수적이며, 이는 LLM 발전의 중요한 방향

- **Approach**: 규모 있는 고품질 물리 데이터셋 구축 + 물리 특화 평가 프레임워크 개발 + 현재 모델들의 물리 능력 광범위 평가

## Achievement

![Figure 1](figures/fig1.webp)
*PHYSICS 데이터셋의 구축 파이프라인과 특징*

1. **최대 규모 물리 데이터셋**: 16,568개 문제(한영 이중언어), 5개 물리 분야, 4단계 난이도 수준(고등학교~대학원), 명확한 훈련/테스트 분할(7:1 비율)

2. **물리 특화 평가 프레임워크**: Rule+Model 하이브리드 방식으로 물리 특유의 평가 문제(단위 변환, 수치 간단히 하기, 정밀도) 해결. 인공 주석 테스트셋으로 개선 효과 검증

3. **광범위한 모델 평가**: 오픈소스/클로즈드소스 모델 평가 결과, OpenAI-o3, Gemini-2.5-pro 등 최강 모델도 물리 문제에서 성능 부족 명시

## How

- **데이터 수집**: 100개 이상 교과서의 PDF를 OCR로 Markdown 변환 → GPT-4o로 QA쌍 추출 → 메타데이터 기반 매칭

- **품질 관리**: (1) OCR 오류 보정 (2) 다중모달/외부 문맥 의존 문제 제거 (3) 인간 전문가 검수 → 8,284개 최종 정제

- **데이터 분할**: 훈련셋 14,568개(강력한 추론 모델의 reasoning path 제공), 테스트셋 1,000개(균형잡힌 난이도/주제 분포)

- **Rule+Model 평가**: 
  - Rule: 단위 변환(km↔m), 수학 식 정규화 등 규칙 기반 사전 처리
  - Model: 훈련셋 수동 주석으로 파인튜닝한 판정 모델로 미묘한 의미론적 차이 판단

- **누설 탐지(Leak Detection)**: 테스트셋이 훈련 데이터에 포함되어 있지 않음을 검증

## Originality

- **최초 시도**: 물리학에 특화된 Rule+Model 하이브리드 평가 프레임워크 설계

- **광범위한 커버리지**: 기존 물리 데이터셋 대비 최대 난이도 범위(고등학교~대학원), 가장 큰 규모(16,568문제)

- **체계적 구축 파이프라인**: OCR 기반 자동 추출 + LLM 보조 + 인간 검수의 3단계 품질 관리 절차

- **이중언어 구성**: 영어/중국어 1:1 비율로 대역 제공, 다양한 평가 시나리오 가능

- **상세한 reasoning path**: 훈련셋에 강력한 추론 모델이 생성한 중간 과정 제공(감독 학습 용이)

## Limitation & Further Study

- **평가 프레임워크의 한계**: Rule+Model 방식도 복잡한 물리 현상의 미묘한 해석 차이를 완전히 포착하지 못할 수 있음

- **데이터 원본 편향**: 100개 교과서는 특정 국가/교육 시스템에 편중될 가능성(영어권, 중국어권 교과서 주로 사용)

- **실험 데이터 제한**: 테스트셋 1,000개는 대규모 벤치마크 기준에서 다소 제한적(다양한 세부 분야 상세 분석 어려움)

- **비전 문제 미포함**: PDF에서 추출하는 과정에서 도형, 그래프, 이미지 기반 문제가 의도적으로 제외되어 시각적 물리 추론 능력 평가 불가

- **후속 연구 방향**: 
  - 다중모달 물리 문제 확장
  - 동적 평가 프레임워크(새로운 물리 현상에 자동 적응)
  - 강화 학습 기반 물리 모델 개선 기법 개발


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4/5
- Significance: 4.5/5
- Clarity: 4/5
- Overall: 4.2/5

**총평**: PHYSICS 데이터셋은 물리학이 과소평가된 분야임을 명확히 하고, 체계적인 구축 파이프라인과 물리 특화 평가 프레임워크로 LLM의 물리 추론 능력 발전을 위한 견고한 기반을 제공한다. 다만 비전 문제 포함 및 더 대규모 테스트셋 확보로 실용성을 높일 여지가 있다.

## Related Papers

- 🔗 후속 연구: [[papers/808_Theoremqa_A_theorem-driven_question_answering_dataset/review]] — TheoremQA의 정리 기반 평가 방식이 PHYSICS 데이터셋의 물리 문제 해결 능력 평가를 더욱 체계화함
- 🔄 다른 접근: [[papers/706_SciBench_Evaluating_College-Level_Scientific_Problem-Solving/review]] — 둘 다 과학 문제 해결 벤치마크이지만 PHYSICS는 물리 특화, SciBench는 대학 수준 전반을 다루는 차이가 있음
- 🏛 기반 연구: [[papers/785_T-sciq_Teaching_multimodal_chain-of-thought_reasoning_via_mi/review]] — T-SciQ의 멀티모달 과학 추론 방법이 PHYSICS 데이터셋의 물리 문제 해결 평가 프레임워크 구축에 기여함
- 🏛 기반 연구: [[papers/279_Distinguishing_Neutron_Star_vs_Low-Mass_Black_Hole_Binaries/review]] — 물리 추론 스케일링이 중력파 신호 분석의 기반이 됨
- 🏛 기반 연구: [[papers/808_Theoremqa_A_theorem-driven_question_answering_dataset/review]] — PHYSICS 데이터셋의 물리 문제 평가 방식이 TheoremQA의 정리 기반 질문 답변 벤치마크 설계에 참고가 됨
- 🔗 후속 연구: [[papers/497_LLM_and_Simulation_as_Bilevel_Optimizers_A_New_Paradigm_to_A/review]] — 물리적 추론을 위한 물리학 데이터셋 확장은 LLM과 시뮬레이션의 이단계 최적화를 더 광범위한 물리 현상으로 확장한다.
