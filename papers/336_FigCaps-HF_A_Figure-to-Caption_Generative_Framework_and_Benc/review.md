---
title: "336_FigCaps-HF_A_Figure-to-Caption_Generative_Framework_and_Benc"
authors:
  - "Ashish Singh"
  - "Prateek Agarwal"
  - "Zixuan Huang"
  - "Arpita Singh"
  - "Tong Yu"
date: "2023"
doi: "10.48550/ARXIV.2307.10867"
arxiv: ""
score: 4.0
essence: "과학 논문의 그림을 설명하는 캡션 생성 모델을 인간 피드백과 강화학습(RLHF)으로 최적화하는 프레임워크와 대규모 벤치마크 데이터셋을 제시한다. 기존의 낮은 품질 캡션 데이터를 학습한 모델 대신, 도메인 전문가 피드백으로 학습된 보상 모델을 통해 독자 선호도에 정렬된 고품질 캡션 생성을 달성한다."
tags:
  - "cat/Scientific_Language_Processing_and_Visualization"
  - "sub/Scientific_Figure_Captioning"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Singh et al._2023_FigCaps-HF A Figure-to-Caption Generative Framework and Benchmark with Human Feedback.pdf"
---

# FigCaps-HF: A Figure-to-Caption Generative Framework and Benchmark with Human Feedback

> **저자**: Ashish Singh, Prateek Agarwal, Zixuan Huang, Arpita Singh, Tong Yu, Sungchul Kim, Victor Bursztyn, Nikos Vlassis, Ryan A. Rossi | **날짜**: 2023 | **DOI**: [10.48550/ARXIV.2307.10867](https://doi.org/10.48550/ARXIV.2307.10867)

---

## Essence

과학 논문의 그림을 설명하는 캡션 생성 모델을 인간 피드백과 강화학습(RLHF)으로 최적화하는 프레임워크와 대규모 벤치마크 데이터셋을 제시한다. 기존의 낮은 품질 캡션 데이터를 학습한 모델 대신, 도메인 전문가 피드백으로 학습된 보상 모델을 통해 독자 선호도에 정렬된 고품질 캡션 생성을 달성한다.

## Motivation

- **Known**: 과학 논문의 그림 캡션은 독자 이해에 필수적이며, 기존 연구는 문서에서 추출한 그림-캡션 쌍으로 학습하고 있음
- **Gap**: arXiv cs.CL 논문의 50% 이상의 캡션이 도메인 전문가들에게 도움이 되지 않는다고 평가되었으며, 기존 모델은 '유용성(helpfulness)', '명확성(explainability)', '시각적 설명력(visual-descriptiveness)' 측면에서 독자 선호도를 반영하지 못함
- **Why**: 저품질 학습 데이터로 훈련된 모델은 자동으로 생성된 캡션이 독자 선호도와 불일치하는 문제 발생
- **Approach**: (1) 작은 규모의 인간 주석 데이터로 피드백 예측 모델 학습, (2) 오프라인 Upside-Down RL(UDRL)을 이용한 보상 조건부 행동 복제(reward-conditioned behavioral cloning) 기반 효율적 최적화

## Achievement

![Figure 1](figures/fig1.webp)
*Figure 1: RLHF Framework for Figure-Caption Generative Models - 소수의 인간 피드백 그림-캡션 쌍에서 학습한 피드백 예측 모델을 통해 대규모 학습 코퍼스에 대한 피드백 추론*

1. **성능 향상**: BLIP을 기반 모델로 사용할 때, ROUGE에서 35.7%, BLEU에서 16.9%, METEOR에서 9% 평균 성능 향상 달성
2. **확장 가능한 피드백 생성**: 작은 규모의 인간 주석 데이터(M ≪ N, 예: N=100,000일 때 M=100)로부터 대규모 학습 데이터셋에 대한 자동 피드백 점수 예측 가능
3. **보정된 보상 모델**: 훈련된 보상 모델이 잘 보정되어 있으며, 지면 진실 주석 통계가 추론된 주석 통계와 일치함을 실증적으로 입증
4. **공개 벤치마크**: 향후 RLHF 기술 개발을 위한 대규모 벤치마크 데이터셋 공개

## How

![Figure 2](figures/fig2.webp)
*Figure 2: Human Feedback Prediction Model의 결과 - 세 가지 그림-캡션 평가 지표에 대한 예측 성능*

**프레임워크 구성**:

- **Step 1 - 인간 피드백 수집**: M개의 그림-캡션 쌍 {I_h, T_h}에 대해 도메인 전문가가 k개의 평가 메트릭(유용성, OCR 콘텐츠, 핵심 내용 등) 점수 부여
- **Step 2 - 피드백 예측 모델 학습**: 회귀 모델 R(x_i, θ)_k를 학습하여 각 캡션의 k개 평가 점수 예측
  - 임베딩 함수 l(·, θ_l): 캡션을 고정된 차원 표현으로 변환
  - 회귀 함수 g(·, θ_g): 평가 점수 생성
  - MSE 손실 L_R = Σ(ŷ_i - y_i)²로 회귀 함수만 학습
- **Step 3 - 대규모 데이터셋에 점수 할당**: 학습된 모델로 N개의 훈련 샘플 모두에 대한 피드백 점수 자동 예측
- **Step 4 - 오프라인 UDRL 기반 최적화**: 예측된 보상 점수를 기반으로 reward-conditioned behavioral cloning 수행
  - 온정책(on-policy) 알고리즘 대비 계산 효율성 우수
  - 모델 훈련 중 보상 모델 필요 없음

## Originality

- **새로운 RLHF 접근법**: 기존의 온정책 강화학습 대신 오프라인 Upside-Down RL을 적용하여 계산 효율성과 단순성 달성
- **확장 가능한 피드백 메커니즘**: 소수의 인간 주석만으로 대규모 데이터셋에 대한 자동 품질 평가 가능하도록 설계한 일반화된 캡션 점수 메커니즘
- **다중 그래뉼래러티(granularity) 피드백**: 여러 차원의 평가 지표(유용성, 설명력, 시각적 설명력)를 동시에 모델에 반영 가능
- **공개 벤치마크 데이터셋**: 향후 그림-캡션 생성 연구를 위한 인간 피드백이 포함된 첫 대규모 벤치마크 제공

## Limitation & Further Study

- **데이터셋 크기 및 도메인**: 실험이 주로 과학 논문(arXiv)의 그림에 국한되어 있으며, 다른 도메인(의료 영상, 뉴스 기사 등)에 대한 일반화 가능성 미검증
- **피드백 메트릭의 범위**: 현재 '유용성', 'OCR 콘텐츠', '핵심' 등 제한된 평가 차원만 사용하고 있으며, 추가 차원(창의성, 간결성 등) 탐색 필요
- **인간 평가의 주관성**: 도메인 전문가 간 평가 불일치(inter-annotator agreement)에 대한 상세 분석 부재
- **모델 아키텍처 의존성**: BLIP 등 특정 기반 모델에서의 성능만 주로 보고되어 있으며, 다양한 최신 비전-언어 모델에 대한 검증 필요
- **후속 연구 방향**: 
  - 온라인 RLHF 방식과의 정량적 비교 연구
  - 멀티모달 입력(이미지 + 표 데이터 + 메타데이터)을 활용한 고도화
  - 전이 학습을 통한 저자원 도메인 적응

## Evaluation

- **Novelty**: 4/5
  - 그림 캡션 생성에 RLHF 적용 자체는 새로운 시도이며, 오프라인 UDRL 기반의 효율적 최점화가 핵심 기여
  - 다만 RLHF 및 보상 모델 학습의 기본 개념은 기존 기술 활용

- **Technical Soundness**: 4/5
  - 회귀 기반 피드백 예측 모델과 reward-conditioned behavioral cloning의 조합이 기술적으로 타당함
  - 단, 인간 평가와 자동 점수 간의 상관관계, inter-annotator agreement 등 통계적 검증 상세 부족
  - 오프라인 방식의 안정성과 수렴성 증명 미흡

- **Significance**: 4/5
  - 과학 논문 이해 향상과 시각장애 독자 접근성 개선에 실질적 기여 가능
  - 대규모 벤치마크 데이터셋 공개로 향후 연구 촉진 기대
  - 응용 범위가 과학 논문에 주로 한정되어 있으며 산업적 임팩트는 중간 수준

- **Clarity**: 4/5
  - 프레임워크 설명과 실험 구성이 명확하고 논리적
  - 수식과 알고리즘 표현이 이해하기 좋으나, 일부 구현 세부사항(embedding 함수 선택, hyperparameter 등)이 보충 필요

- **Overall**: 4/5

**총평**: 이 논문은 그림 캡션 생성의 현실적 문제(저품질 학습 데이터)를 인간 피드박과 오프라인 강화학습으로 효과적으로 해결하고, 대규모 공개 벤치마크 기여로 커뮤니티 가치를 제공한다. 다만 평가 메트릭 검증의 엄밀성 강화와 다양한 도메인·모델에 대한 일반화 검증이 진행되면 더욱 강한 논문이 될 수 있다.

## Related Papers

- 🧪 응용 사례: [[papers/722_Scifibench_Benchmarking_large_multimodal_models_for_scientif/review]] — 과학 그림 해석 벤치마크에서 캡션 생성 모델의 성능을 체계적으로 평가
- 🔗 후속 연구: [[papers/708_SciCap_Generating_Captions_for_Scientific_Figures/review]] — 기본적인 과학 캡션 생성을 인간 피드백 기반 최적화로 발전시킨 확장
- 🏛 기반 연구: [[papers/709_SciCap_A_Knowledge_Augmented_Dataset_to_Study_the_Challenges/review]] — 과학 캡션 생성의 도전과제 분석이 RLHF 기반 개선 방법론의 기반
- 🔄 다른 접근: [[papers/435_Interfeedback_Unveiling_interactive_intelligence_of_large_mu/review]] — 멀티모달 상호작용과 달리 과학 그림 캡션 생성에 특화된 인간 피드백 활용
- 🔗 후속 연구: [[papers/727_Scimage_How_good_are_multimodal_large_language_models_at_sci/review]] — 그림-캡션 생성 프레임워크가 과학적 이미지 생성과 이해 평가를 시각-텍스트 변환 관점에서 확장한다.
- 🏛 기반 연구: [[papers/323_Every_part_matters_Integrity_verification_of_scientific_figu/review]] — 그림 캡션 생성이 과학 그림 검증의 기반을 제공합니다.
- 🔗 후속 연구: [[papers/600_Paper2Web_Lets_Make_Your_Paper_Alive/review]] — 과학 도표 캡션 생성을 논문 전체의 멀티미디어 변환으로 확장한 연구
- 🏛 기반 연구: [[papers/853_Understanding_how_paper_writers_use_ai-generated_captions_in/review]] — 과학 도표 캡션 생성의 기본 기법이 AI 생성 캡션의 인간 활용 방식 연구에 이론적 기반을 제공한다.
- 🏛 기반 연구: [[papers/691_S1-MMAlign_A_Large-Scale_Multi-Disciplinary_Dataset_for_Scie/review]] — 그림-캡션 생성 프레임워크가 과학 논문 멀티모달 정렬의 기반을 제공한다
- 🔗 후속 연구: [[papers/601_PaperBanana_Automating_Academic_Illustration_for_AI_Scientis/review]] — FigCaps-HF의 캡션 생성을 넘어 전체 다이어그램과 플롯을 자동 생성하는 발전된 시스템
- 🧪 응용 사례: [[papers/722_Scifibench_Benchmarking_large_multimodal_models_for_scientif/review]] — 과학 그림 캡션 생성 모델의 성능을 체계적으로 평가할 수 있는 벤치마크 제공
- 🔄 다른 접근: [[papers/708_SciCap_Generating_Captions_for_Scientific_Figures/review]] — 둘 다 과학 도형 캡션 생성을 다루지만 하나는 arXiv 데이터셋 구축에, 다른 하나는 벤치마크 프레임워크 개발에 초점을 맞춘다.
- 🔄 다른 접근: [[papers/524_MatViX_Multimodal_Information_Extraction_from_Visually_Rich/review]] — FigCaps-HF의 그림-캡션 생성 프레임워크가 MatViX의 멀티모달 추출과 다른 접근법으로 과학 문서의 시각적 정보를 처리하는 상호 보완적 방법론임
- 🏛 기반 연구: [[papers/599_Paper2poster_Towards_multimodal_poster_automation_from_scien/review]] — 과학적 그림에 대한 캡션 생성 연구가 논문을 포스터로 변환하는 멀티모달 자동화의 기초적 접근을 제공함
- 🔄 다른 접근: [[papers/564_Multi-llm_collaborative_caption_generation_in_scientific_doc/review]] — 과학 도형 캡션 생성에서 다중 LLM 협업과 단일 생성 프레임워크의 서로 다른 접근법을 비교할 수 있습니다.
