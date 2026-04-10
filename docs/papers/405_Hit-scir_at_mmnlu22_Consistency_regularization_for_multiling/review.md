---
title: "405_Hit-scir_at_mmnlu22_Consistency_regularization_for_multiling"
authors:
  - "Bo Zheng"
  - "Zhouyang Li"
  - "Fuxuan Wei"
  - "Qiguang Chen"
  - "Libo Qin"
date: "2023"
doi: "N/A"
arxiv: ""
score: 4.0
essence: "다국어 음성언어이해(multilingual spoken language understanding, SLU) 태스크에서 일관성 정규화(consistency regularization)와 하이브리드 데이터 증강(hybrid data augmentation) 전략을 결합하여 의도 탐지(intent detection)와 슬롯 채우기(slot filling) 성능을 향상시킨 연구이다. MASSIVE 데이터셋에서 전체 데이터셋 설정에서 1위를 달성했다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Scientific_Document_Analysis_and_Retrieval"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Zheng et al._2023_Hit-scir at mmnlu22 Consistency regularization for multilingual spoken language understanding.pdf"
---

# Hit-scir at mmnlu22: Consistency regularization for multilingual spoken language understanding

> **저자**: Bo Zheng, Zhouyang Li, Fuxuan Wei, Qiguang Chen, Libo Qin, Wanxiang Che | **날짜**: 2023 | **DOI**: N/A

---

## Essence

다국어 음성언어이해(multilingual spoken language understanding, SLU) 태스크에서 일관성 정규화(consistency regularization)와 하이브리드 데이터 증강(hybrid data augmentation) 전략을 결합하여 의도 탐지(intent detection)와 슬롯 채우기(slot filling) 성능을 향상시킨 연구이다. MASSIVE 데이터셋에서 전체 데이터셋 설정에서 1위를 달성했다.

## Motivation

- **Known**: 사전학습된 다국어 언어모델(cross-lingual language model)을 미세조정(fine-tuning)하면 다국어 간 지식 전이가 가능하며, 기계 번역이나 코드스위칭 같은 데이터 증강 기법이 다국어 전이 성능을 향상시킨다.

- **Gap**: 기존 연구들은 데이터 증강 결과를 단순히 추가 학습 데이터로 활용하며, 원본 데이터와 의미론적으로 동등한 증강 데이터 간의 내재적 상관성을 충분히 활용하지 못한다.

- **Why**: 모델이 의미론적으로 보존된 증강에 대해 일관된 예측을 하도록 강제하면, 이러한 상관성을 더 효과적으로 활용할 수 있다.

- **Approach**: 기계 번역(machine translation)과 부분단어 샘플링(subword sampling) 두 가지 데이터 증강 전략을 기반으로 의도 탐지와 슬롯 채우기 태스크에 일관성 정규화를 적용한다.

## Achievement

![Figure 2](figures/fig2.webp)
*일관성 정규화 기반 미세조정 프레임워크. 하이브리드 데이터 증강으로 기계 번역(MT)과 부분단어 샘플링(SS)을 활용*

1. **경쟁 우위**: MMNLU-22 경쟁에서 전체 데이터셋 설정 하에 1위 달성 (정확 매칭 정확도 49.65점, 2위보다 1.02점 우수)

2. **성능 향상**: 
   - XLM-Align Base: 의도 정확도 86.16% → 87.12%, 슬롯 F1 76.36 → 77.99
   - mT5 Base: 의도 정확도 85.33% → 87.60%, 슬롯 F1 76.77 → 78.22

3. **포괄적 효과**: 전체 데이터셋 설정과 제로샷(zero-shot) 설정 모두에서 지속적인 성능 개선 달성

## How

![Figure 1](figures/fig1.webp)
*MASSIVE 데이터셋의 영어 예제: 의도(set alarm)와 슬롯 레이블(time, date) 표기*

### 일관성 정규화(Consistency Regularization)

- 원본 입력 x와 증강된 입력 A(x, z)에 대한 예측 분포를 대칭 쿨백-라이블러 발산(symmetric KL divergence)으로 정렬
- stopgrad 연산으로 역전파 차단하여 안정적 학습

### 하이브리드 데이터 증강 전략

- **부분단어 샘플링**: SentencePiece 라이브러리의 유니그램 언어모델 기반 온더플라이(on-the-fly) 샘플링으로 의도 탐지와 슬롯 채우기 모두에 적용 가능

- **기계 번역**: 
  - 의도 탐지 태스크에만 적용 (슬롯 레이블 정렬의 어려움)
  - 순수 텍스트 번역과 괄호로 표시된 슬롯 기반 번역을 조합하여 슬롯 정렬 정확도 향상

### 손실 함수

```
L = L_I + λ₁L_S + λ₂R_I + λ₃R_S
```
- L_I, L_S: 의도/슬롯 태스크 교차 엔트로피 손실
- R_I, R_S: 의도/슬롯 일관성 정규화 항
- λ 계수로 각 성분의 가중치 조정

### 구현 세부사항

- XLM-Align Base (인코더 전용) 및 mT5 Base (Text-to-Text) 모델 활용
- 하이퍼파라미터: 배치 크기 32-256, 드롭아웃 0.05-0.15, λ₁∈[1,2,4], λ₂,λ₃∈[2,3,5,10]

## Originality

- **증강-원본 상관성 활용**: 기존의 데이터 증강을 단순 데이터 추가에서 일관성 정규화 신호로 전환

- **태스크별 맞춤형 증강**: 의도 탐지에는 기계 번역 추가, 슬롯 채우기에는 부분단어 샘플링 추가로 각 태스크 특성에 맞게 설계

- **슬롯 정렬 기법**: 번역 결과에서 슬롯 값 추적으로 다국어 슬롯 레이블 정렬 문제 해결

- **포괄적 평가**: 전체 데이터셋/제로샷 두 설정에서 실용적 효과 입증

## Limitation & Further Study

- **슬롯 정렬 한계**: 기계 번역에서 슬롯 레이블 정렬이 완벽하지 않으면 슬롯 채우기에 활용 불가능 (의도 탐지만 사용)

- **상용 번역 API 의존성**: 영어-50개 언어 번역에 DeepL/Google 번역기 의존으로 재현성 및 독립성 제약

- **슬롯 정렬 개선**: 더 정교한 슬롯 정렬 알고리즘으로 기계 번역을 슬롯 채우기에도 직접 활용

- **언어별 성능 분석**: 개별 언어별 상세 분석으로 저자원 언어에 대한 개선 전략 수립

- **다른 SLU 데이터셋 검증**: ATIS, SNIPS 등 다른 데이터셋에서의 일관성


## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 일관성 정규화와 하이브리드 데이터 증강의 결합으로 다국어 SLU에서 체계적이고 효과적인 성능 향상을 달성했으며, MMNLU-22 경쟁 우승으로 실용성을 입증한 견고한 연구이다. 다만 기계 번역에서의 슬롯 정렬 한계와 상용 API 의존성이 개선 여지를 남긴다.

## Related Papers

- 🏛 기반 연구: [[papers/206_ChatGPT_outperforms_crowd_workers_for_text-annotation_tasks/review]] — 텍스트 주석 작업에서 ChatGPT의 기본 성능이 다국어 음성언어이해의 데이터 증강 전략 개발에 기초가 됩니다.
- 🔄 다른 접근: [[papers/421_Improving_demonstration_diversity_by_human-free_fusing_for_t/review]] — Text-to-SQL에서의 무인 융합 다양성 향상과 SLU에서의 일관성 정규화가 서로 다른 다양성 증진 방법을 제시합니다.
- 🔗 후속 연구: [[papers/423_Improving_grammatical_error_correction_via_contextual_data_a/review]] — 문법 오류 수정의 문맥 기반 데이터 증강 방법을 다국어 음성언어이해에 적용하여 성능을 향상시킬 수 있습니다.
- 🔄 다른 접근: [[papers/421_Improving_demonstration_diversity_by_human-free_fusing_for_t/review]] — 다양성 향상에서 무인 융합 방법과 일관성 정규화 방법이 서로 다른 접근 방식을 제시합니다.
- 🔄 다른 접근: [[papers/423_Improving_grammatical_error_correction_via_contextual_data_a/review]] — 문법 오류 수정과 다국어 음성언어이해에서 각각 문맥 기반과 일관성 기반의 서로 다른 데이터 증강 방법을 사용합니다.
