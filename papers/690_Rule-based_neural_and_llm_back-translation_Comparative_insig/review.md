---
title: "690_Rule-based_neural_and_llm_back-translation_Comparative_insig"
authors:
  - "Samuel Frontull"
  - "Georg Moser"
date: "2024"
doi: "N/A"
arxiv: ""
score: 4.0
essence: "저자원(low-resource) 언어인 라딘어(Ladin)의 Val Badia 방언에 대해 규칙 기반(RBMT), 신경망(NMT), 대규모 언어모델(LLM) 기반의 세 가지 역번역(back-translation) 기법을 비교 분석하여, 저자원 시나리오에서는 역번역 모델 선택이 최종 성능에 유의미한 영향을 미치지 않음을 실증했다."
tags:
  - "cat/Scientific_Language_Processing_and_Visualization"
  - "sub/Scientific_Text_Translation"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Frontull and Moser_2024_Rule-based, neural and llm back-translation Comparative insights from a variant of ladin.pdf"
---

# Rule-based, neural and llm back-translation: Comparative insights from a variant of ladin

> **저자**: Samuel Frontull, Georg Moser | **날짜**: 2024 | **DOI**: N/A

---

## Essence

저자원(low-resource) 언어인 라딘어(Ladin)의 Val Badia 방언에 대해 규칙 기반(RBMT), 신경망(NMT), 대규모 언어모델(LLM) 기반의 세 가지 역번역(back-translation) 기법을 비교 분석하여, 저자원 시나리오에서는 역번역 모델 선택이 최종 성능에 유의미한 영향을 미치지 않음을 실증했다.

## Motivation

- **Known**: 역번역 기법은 저자원 언어의 기계번역(MT) 성능 향상에 효과적으로 알려져 있으며, 각 번역 패러다임(규칙 기반, 신경망, LLM)은 고유한 장단점을 가지고 있다.

- **Gap**: 저자원 언어에서 어떤 역번역 모델을 선택하는 것이 최종 MT 성능에 실제로 미치는 영향에 대한 실증적 비교 연구가 부재하며, 라딘어는 MT 연구에서 완전히 미개척 상태다.

- **Why**: 라딘어는 약 30,000명의 사용자를 가진 공식 소수 언어로 학교 교육, 미디어, 공공행정에 사용되어 효과적인 MT 시스템이 필요하지만, 병렬 데이터(18k 문장 쌍)가 극도로 부족하다.

- **Approach**: 세 가지 역번역 전략(미세조정된 NMT, 언어 쌍 맞춤형 RBMT, LLM 프롬프팅)으로 라딘어 단일언어 텍스트를 이탈리아어로 자동 번역하여 합성 데이터를 생성하고, 이를 활용해 사전학습 다중언어 NMT 모델을 미세조정하여 성능을 비교 평가한다.

## Achievement

| 데이터셋 | 문장 수 | 특징 |
|---------|--------|------|
| **병렬 데이터** | 18,139 | 라딘-이탈리아 사전의 예시 문장 |
| **단일언어 데이터** | 274,665 | 신문 'La Usc di Ladins' (2012년 이후) |
| **테스트셋 1** | 424 | 법률/공식 용어 (재단 규정) |
| **테스트셋 2** | 833 | 역사·행정·법률 혼합 텍스트 |
| **테스트셋 3** | 1,563 | 문학 텍스트 (피노키오, 문체·관용표현 도전) |

1. **최초 라딘어 MT 연구 수행**: 라딘어(특히 Val Badia 방언)를 대상으로 한 첫 기계번역 연구 수행 및 벤치마크 구축

2. **세 가지 역번역 기법 비교**: RBMT, 미세조정 NMT, LLM 기반 역번역이 저자원 시나리오에서 비슷한 BLEU/chrF++ 점수 달성 → 역번역 모델 선택의 영향이 제한적임을 실증

3. **자원 공개**: 테스트 데이터, RBMT 시스템, 최고 성능 모델을 공개하여 향후 연구 기반 제공

## How

### 데이터 구축

- **병렬 데이터 추출**: 라딘 Val Badia-이탈리아 사전(Moling et al., 2016)의 표제어 설명 예시 문장에서 18,139 병렬 문장 쌍 추출
  
- **단일언어 데이터 수집**: 신문 'La Usc di Ladins'의 PDF 아카이브(2012년 이후)에서 1,937,608 문장 추출 후 NLTK로 분할

- **방언 분류**: XGBoost 분류기(3-gram 문자 특성, 94.48% 정확도)를 활용하여 5개 라딘 방언 중 Val Badia 방언 274,665 문장 선별

- **데이터 정제**: 2015년 철자 개혁 후 규칙 기반 시스템으로 미등록어 식별·수정하여 최종 학습 데이터 구성

- **다양한 테스트셋**: 법률 문서(424), 역사·행정 혼합(833), 문학 텍스트(1,563) 등 도메인 외 데이터로 일반화 성능 평가

### 역번역 전략

**1) 신경망 기반 (N1)**
- 사전학습 다중언어 모델 Helsinki-NLP/opus-mt-ine-ine 미세조정
- 양방향 번역(lvb↔ita)을 단일 모델로 처리 (언어 태그 접두사 사용)
- AdamW 최적화기, 빔 탐색 크기 6

**2) 규칙 기반 (RBMT)**
- Apertium 프레임워크 기반 라딘-이탈리아 번역 시스템 구축
- 사전의 19,034 개 표제어를 742개 활용 패러다임으로 매핑
- 597개 형용사, 동사, 명사 등 다양한 품사 커버
- 강건성과 계산 효율성 장점 활용

**3) LLM 기반**
- 대규모 언어모델을 프롬프팅으로 활용 (8개 예시 샘플 동반)
- 유창하고 일관성 있는 텍스트 생성 능력 활용
- 환각(hallucination) 위험 내포

## Originality

- **최초 라딘어 MT 연구**: 라딘어(특히 Val Badia 방언)의 기계번역을 처음으로 체계적으로 다룬 연구

- **이질적 패러다임 비교**: 규칙 기반, 신경망, LLM이라는 근본적으로 다른 세 가지 번역 방식을 동일 저자원 환경에서 직접 비교한 최초 분석

- **라딘 관련 자원 개발**: 공식 RBMT 시스템, 병렬/단일언어 코퍼스, 테스트셋 등을 처음 구축하여 공개

- **저자원 언어 데이터 수집 방법론**: 신문 아카이브, 사전, 웹 사이트를 활용한 체계적 데이터 추출 및 방언 분류 기법 제시

## Limitation & Further Study

**한계:**
- 병렬 데이터가 매우 제한적(18k 문장) → 일반화 능력 제약
- 테스트 데이터가 모두 도메인 외(out-of-domain) 데이터 → 학습 데이터의 대표성 부족
- 단일언어 데이터 중 약 31%만 정제되어 사용 → 미활용 데이터 약 100k 문장 존재

**후속 연구:**
- 추가 병렬 텍스트 수집으로 학습 데이터 확대
- 미정제 100k 문장에 대한 추가 분석 및 정제 로직 개선
- 다른 라딘 방언(Gherdëina, Fascia, Fodom, Anpezo)으로 확장
- 라운드-트립 번역(round-trip translation) 분석을 통한 모델 성능 심화 연구
- 도메인 적응(domain adaptation) 기법 적용


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4/5
- Significance: 3.5/5
- Clarity: 4.5/5
- Overall: 4/5

**총평**: 본 논문은 라딘어라는 미개척 저자원 언어에 대해 규칙, 신경망, LLM 세 가지 역번역 기법을 처음으로 비교 분석하여 흥미로운 실증 결과를 제공했으며, 공개 자원과 벤치마크를 통해 향후 연구 기반을 마련한 점에서 의의가 있으나, 제한된 데이터와 단일 언어 쌍에 대한 초기 탐색 연구로서 일반화 가능성은 아직 미지수다.

## Related Papers

- 🔄 다른 접근: [[papers/125_Automated_latex_code_generation_from_handwritten_math_expres/review]] — 둘 다 언어 간 변환을 다루지만 하나는 저자원 언어 역번역이고 다른 하나는 필기 수학식의 LaTeX 변환이다.
- 🏛 기반 연구: [[papers/340_Fine-tuning_large_language_models_for_domain_adaptation_expl/review]] — 도메인 적응을 위한 대규모 언어 모델 파인튜닝 경험이 저자원 언어 번역 모델 선택에 유용한 통찰을 제공한다.
- 🔗 후속 연구: [[papers/858_Unsupervised_crosslingual_representation_learning_at_scale/review]] — 대규모 무감독 교차언어 표현 학습이 라딘어와 같은 저자원 언어의 역번역 성능 향상에 적용될 수 있다.
