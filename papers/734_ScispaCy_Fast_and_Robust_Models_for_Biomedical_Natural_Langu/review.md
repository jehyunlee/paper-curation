---
title: "734_ScispaCy_Fast_and_Robust_Models_for_Biomedical_Natural_Langu"
authors:
  - "Mark Neumann"
  - "Daniel King"
  - "Iz Beltagy"
  - "Waleed Ammar"
date: "2019.08"
doi: "10.18653/v1/W19-5034"
arxiv: ""
score: 4.0
essence: "생의학 분야의 급증하는 문헌을 자동으로 처리하기 위해 spaCy 라이브러리를 기반으로 한 scispaCy라는 전문화된 자연언어처리(NLP) 라이브러리를 개발하여, 도메인 전용 모델들을 제공한다. 빠른 처리 속도와 견고한 성능을 갖춘 실무용 생의학 텍스트 처리 도구를 공개했다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/Multimodal_Scientific_Reasoning"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Neumann et al._2019_ScispaCy Fast and Robust Models for Biomedical Natural Language Processing.pdf"
---

# ScispaCy: Fast and Robust Models for Biomedical Natural Language Processing

> **저자**: Mark Neumann, Daniel King, Iz Beltagy, Waleed Ammar | **날짜**: 2019-08 | **DOI**: [10.18653/v1/W19-5034](https://doi.org/10.18653/v1/W19-5034)

---

## Essence

생의학 분야의 급증하는 문헌을 자동으로 처리하기 위해 spaCy 라이브러리를 기반으로 한 scispaCy라는 전문화된 자연언어처리(NLP) 라이브러리를 개발하여, 도메인 전용 모델들을 제공한다. 빠른 처리 속도와 견고한 성능을 갖춘 실무용 생의학 텍스트 처리 도구를 공개했다.

## Motivation

- **Known**: 최근 NLP의 발전에도 불구하고 많은 통계 모델들이 도메인 변화(domain shift)에서 극히 낮은 성능을 보인다. 생의학 논문의 발행량이 지수적으로 증가하고 있다(그림 1: 1650-2012년 의학 분야 인용문헌의 연간 증가).

- **Gap**: 기존 도구(MetaMap, GENIA Tagger)들은 개체명 인식과 링킹에만 초점을 맞추거나 최신 신경망 기반 방법론을 활용하지 못하고 있다. 신속하고 견고한 end-to-end 생의학 NLP 파이프라인이 부족하다.

- **Why**: 생의학 분야에서 대량의 정보 과부하를 해결하기 위해 유전자, 약물, 단백질 등의 자동 추출이 중요하며, 실무적으로 사용 가능한 공개 모델이 필요하다.

- **Approach**: spaCy 라이브러리를 기반으로 생의학 텍스트용으로 재학습된 모델들을 개발하고, GENIA 1.0 데이터셋을 Universal Dependencies 형식으로 변환하여 공개한다.

## Achievement

![Table 2: 다양한 생의학 NLP 파이프라인의 처리 속도 비교](figures/table2.webp)
*scispaCy 모델은 C++/Java 기반 시스템과 경쟁력 있는 속도를 달성함*

1. **Two Core Packages 출시**: 
   - `en_core_sci_sm` (어휘 크기 58,338, 단어 벡터 미포함)
   - `en_core_sci_md` (어휘 크기 101,678, 98,131개 단어 벡터 포함)
   
2. **높은 처리 속도**: 추상(Abstract) 처리 시 32-33ms, 문장(Sentence) 처리 시 4ms로 MetaMapLite(293ms)보다 약 9배 빠름

3. **경쟁력 있는 성능**:
   - POS 태깅: 98.38-98.51% (GENIA 테스트셋, 최고 성능 98.89%와 비교)
   - 의존성 파싱: UAS 90.60%, LAS 88.79% (Biafﬁne 92.64% UAS 대비 약 2-3% 차이)

4. **9개 세부 NER 모델**: BC5CDR(화학물질·질병), CRAFT(세포·단백질), JNLPBA(세포라인·DNA), BioNLP13CG(암 유전학) 등 다양한 도메인별 전문화된 모델 제공

5. **GENIA 1.0 의존성 데이터셋 공개**: 원본 PubMed 추상 텍스트와 정렬된 Universal Dependencies v1.0 형식으로 변환

## How

- **기본 아키텍처**: spaCy 2.0.18 기반 arc-eager transition-based 파서(Goldberg & Nivre 2012), CNN 기반 토큰 특성 표현, 해시된 임베딩 표현 사용

- **학습 데이터 전략**:
  - 주요 데이터: GENIA 1.0 (생의학 전문), OntoNotes 5.0 (일반 텍스트)
  - 혼합 학습: 웹 데이터 비율을 증가시키면서 성능 향상 (그림 2: OntoNotes 성능 개선, 생의학 성능 유지)

- **다중 데이터셋 평가**: 9개의 서로 다른 생의학 NER 데이터셋(크기: 4,263-84,310 annotation, 개체 타입: 1-16개)에서 광범위한 벤치마킹

- **토큰화 개선**: 생의학 텍스트의 특성에 맞춘 추가 규칙 적용

- **모듈화 설계**: 사용자가 특정 요구사항에 맞는 세부 모델을 선택 가능

## Originality

- **최초의 포괄적 통합 솔루션**: 생의학 분야용 토큰화, POS 태깅, 의존성 파싱, NER을 모두 포함한 end-to-end 파이프라인

- **GENIA 의존성 데이터셋의 재구성**: Universal Dependencies 형식 변환 및 원본 텍스트 정렬 (새로운 커뮤니티 자산)

- **다중 도메인 전문화 모델**: 9개의 세부 NER 모델로 다양한 생의학 응용 분야 커버

- **웹 데이터 혼합을 통한 견고성 개선**: 도메인 전용 성능 저하 없이 일반 텍스트에 대한 강건성 향상

- **실무 중심의 설계**: 속도와 편의성을 우선하여, MetaMap 등 엔터프라이즈 도구와의 통합 용이

## Limitation & Further Study

- **성능 격차**: 의존성 파싱에서 Biafﬁne 파서(92.64% UAS)에 비해 2-3% 성능 저하

- **제한된 학습 데이터**: 생의학 텍스트가 OntoNotes에 비해 상대적으로 적음 (GENIA 1.0의 고정 데이터셋에 의존)

- **개체 타입 분류 미지원**: 기본 MedMentions 모델은 개체 타입을 예측하지 않음 (spans만 인식)

- **언어 지원 부재**: 영어만 지원 (다국어 확장 미정)

- **후속 연구**: 
  - 신경망 기반 고성능 파서의 속도 최적화 통합
  - 더 큰 규모의 생의학 말뭉치 학습
  - 임상 텍스트 특화 모델 개발
  - 개체 링킹(Entity Linking) 통합 기능 추가


## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 5/5
- Clarity: 5/5
- Overall: 4/5

**총평**: 생의학 NLP 분야에서 실제로 필요한 통합 도구를 제공하며, 공개 데이터셋 공헌과 함께 높은 실무적 가치를 지닌 우수한 논문이다. 다만 성능 면에서 최첨단 모델들에 약간 미치지 못하지만, 속도와 사용 편의성의 우월함으로 이를 충분히 보완한다.

## Related Papers

- 🔄 다른 접근: [[papers/761_spaCy_Industrial-strength_Natural_Language_Processing_in_Pyt/review]] — 동일한 scispaCy 도구에 대한 연구이지만 서로 다른 시기의 발표로 생의학 NLP 도구의 발전 과정을 보여준다.
- 🏛 기반 연구: [[papers/707_SciBERT_A_Pretrained_Language_Model_for_Scientific_Text/review]] — 생의학 텍스트를 위한 사전훈련 언어 모델인 SciBERT가 scispaCy의 도메인 특화 모델 개발에 기술적 기반을 제공한다.
- 🔗 후속 연구: [[papers/161_BioBERT_a_pre-trained_biomedical_language_representation_mod/review]] — 생의학 언어 표현 모델인 BioBERT의 발전을 실용적 NLP 파이프라인으로 확장한 사례이다.
- 🔄 다른 접근: [[papers/761_spaCy_Industrial-strength_Natural_Language_Processing_in_Pyt/review]] — 같은 scispaCy 라이브러리에 대한 연구로 생의학 자연언어처리 도구의 지속적 발전을 보여준다.
- 🏛 기반 연구: [[papers/164_BioInformatics_Agent_BIA_Unleashing_the_Power_of_Large_Langu/review]] — BIA의 생물정보학 자동화는 ScispaCy의 생물의학 자연어 처리 모델이 제공하는 도메인 특화 언어 이해 기반 위에 대화형 분석 인터페이스를 구축합니다.
