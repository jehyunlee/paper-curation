---
title: "478_Large_language_models_penetration_in_scholarly_writing_and_p"
authors:
  - "Li Zhou"
  - "Ruijie Zhang"
  - "Xiao Dai"
  - "Daniel Hershcovich"
  - "Haizhou Li"
date: "2025"
doi: "arXiv:2502.11193"
arxiv: ""
score: 4.0
essence: "본 논문은 학술 저술 및 피어 리뷰 과정에서 대규모 언어모델(LLM)의 침투 정도를 측정하기 위한 포괄적 평가 프레임워크를 제시한다. ScholarLens 데이터셋과 LLMetrica 도구를 통해 규칙 기반 지표와 모델 기반 탐지기를 결합하여 학술 워크플로우에서의 LLM 사용 추세를 다각도로 분석한다."
tags:
  - "cat/Academic_Peer_Review_Automation"
  - "sub/AI_Publishing_Trends"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Zhou et al._2025_Large language models penetration in scholarly writing and peer review.pdf"
---

# Large language models penetration in scholarly writing and peer review

> **저자**: Li Zhou, Ruijie Zhang, Xiao Dai, Daniel Hershcovich, Haizhou Li | **날짜**: 2025 | **DOI**: [arXiv:2502.11193](https://arxiv.org/abs/2502.11193)

---

## Essence

본 논문은 학술 저술 및 피어 리뷰 과정에서 대규모 언어모델(LLM)의 침투 정도를 측정하기 위한 포괄적 평가 프레임워크를 제시한다. ScholarLens 데이터셋과 LLMetrica 도구를 통해 규칙 기반 지표와 모델 기반 탐지기를 결합하여 학술 워크플로우에서의 LLM 사용 추세를 다각도로 분석한다.

## Motivation

- **Known**: LLM은 학술 저술의 아이디어 개발, 논문 작성, 피어 리뷰 과정에서 광범위하게 활용되고 있다. 그러나 LLM 생성 콘텐츠는 낮은 품질, 사실적 오류, 환각(hallucination) 등의 문제를 보인다.

- **Gap**: 기존 연구들은 인간 작성자 관점에 집중하고 있으며, 학술 영역에서의 LLM 침투 정도를 체계적으로 측정할 수 있는 방법론이 부재하다. 특히 피어 리뷰 과정에서의 LLM 활용에 대한 종합적 분석이 미흡하다.

- **Why**: 학술 출판의 신뢰성과 과학 연구의 엄밀성을 유지하기 위해서는 LLM 사용의 투명성, 책임성, 윤리적 실천이 필수적이다.

- **Approach**: 인간 저술과 LLM 생성 콘텐츠로 구성된 큐레이션된 데이터셋(ScholarLens)을 구축하고, 언어학적 특성 분석과 의미적 유사성 측정을 결합한 다차원 평가 프레임워크(LLMetrica)를 제안한다.

## Achievement

![Figure 1](figures/fig1.webp)
*파이프라인 개요: (1) ScholarLens 큐레이션, (2) LLMetrica 프레임워크, (3) 학술 저술 및 피어 프로세스의 LLM 침투율 평가*

1. **ScholarLens 데이터셋 구축**: ICLR 2019년 이전 2,831개 논문의 초록, 리뷰, 메타-리뷰로 구성된 큐레이션 데이터셋 개발. GPT-4o, Gemini-1.5, Claude-3 Opus 등 3개의 최신 LLM으로 생성된 대응 텍스트 포함.

2. **LLMetrica 프레임워크 개발**: 10개의 일반 언어학적 특성 지표(어휘 길이, 문장 복잡도, 가독성 등)와 4개의 전문 의미론적 특성 지표(의미적 유사성, 문장 수준 특수성)를 통합한 종합 평가 도구 개발.

3. **ScholarDetect 탐지기**: ScholarLens를 기반으로 학술 영역 특화 LLM 탐지 모델 개발로 높은 정확도의 LLM 생성 콘텐츠 식별 달성.

## How

![Figure 2](figures/fig2.webp)
*ScholarLens의 일반 특성에 기반한 인간 저술과 LLM 생성 텍스트 비교*

**규칙 기반 지표(Rule-Based Metrics)**:
- **일반 언어학적 특성**: 평균 단어 길이(AWL), 장어 비율(LWR), 정지어 비율(SWR), 유형-토큰 비율(TTR), 평균 문장 길이(ASL), 의존성 관계 다양성(DRV), 종속절 밀도(SCD), Flesch Reading Ease(FRE), 감정 극성(PS), 감정 주관성(SS) 등 10개 지표
  
- **의미론적 특성**: 
  - MRSim: 메타-리뷰와 참조 리뷰 집합 간 의미적 유사성 측정
  - RSim: 리뷰 집합 내 최대 유사도 계산
  - SF-IRF (Sentence Frequency-Inverse Reference Frequency): 문장 수준의 특수성 정량화로 TF-IDF 개념을 학술 리뷰에 적용

**모델 기반 탐지기(Model-Based Detectors)**:
- ScholarLens 데이터셋의 인간 저술/LLM 생성 텍스트 쌍을 활용한 지도학습 기반 탐지 모델 학습
- 학술 영역 특화 학습으로 도메인 특수성 확보
- 7:3의 학습/테스트 분할을 통한 엄격한 평가

**다차원 평가 방식**:
- 다양한 언어학적 관점에서의 선호도 분석(Preference)
- 모델 기반 구분 능력(Distinction) 검증
- 시간적 추이 분석을 통한 침투율 추적

## Originality

- **학술 영역 특화 접근**: 초록, 리뷰, 메타-리뷰 등 학술 저술 과정 전체를 포괄하는 종합적 데이터셋 및 평가 프레임워크 제시. 기존 일반 텍스트 LLM 탐지 연구와 달리 학술 워크플로우 특화 설계.

- **의미론적 지표의 혁신**: SF-IRF 지표를 통해 문장 수준의 특수성과 반복성을 동시에 측정하는 새로운 방법론 제안. Du et al. (2024)의 ITF-IDF 개념을 학술 영역에 맞게 발전시킴.

- **다각도 평가 체계**: 규칙 기반 지표와 모델 기반 탐지기를 결합한 하이브리드 접근으로 LLM 사용의 다차원적 특성 파악.

- **대규모 현실 데이터 검증**: 3개의 주요 LLM(GPT-4o, Gemini-1.5, Claude-3 Opus)에서 생성된 2,831개 논문의 대응 데이터로 결과의 일반화 가능성 강화.

## Limitation & Further Study

- **데이터 시간성 제약**: ICLR 2019년 이전 논문만 활용하여 최근의 학술 저술 패턴 변화를 완전히 반영하지 못함. 최근 LLM 발전에 따른 탐지 성능 저하 가능성.

- **도메인 편향성**: ICLR이라는 특정 학술 분야(기계학습)에 편중된 데이터로 인문학, 의학, 자연과학 등 다른 분야의 특수성 미반영.

- **모델 특화 문제**: 특정 3개 LLM으로 학습한 탐지기의 새로운 또는 미세조정된 LLM에 대한 일반화 능력 제한. 오픈소스 LLM(LLaMA, Mistral 등)에 대한 성능 미검증.

- **문맥 정보 한계**: 전문가 수동 검증이나 외부 정보원과의 검증 없이 순수 텍스트 특성만 활용한 탐지의 신뢰성 문제.

**후속 연구 방향**:
- 2019년 이후 최근 논문을 포함한 시계열 데이터 확보로 시간에 따른 LLM 침투 추이의 정밀 추적
- 여러 학문 분야로의 데이터 확대를 통한 도메인 적응 방법론 개발
- 다양한 오픈소스 및 폐쇄형 LLM 추가를 통한 강건한 탐지기 설계
- LLM 인위적 조작(paraphrasing, 역번역 등)에 대한 저항성 개선 연구

## Evaluation

- **Novelty**: 4/5
  - 학술 영역 특화 평가 프레임워크와 SF-IRF 지표는 창의적이나, 기본 개념(TF-IDF, 텍스트 특성 분석)은 기존 방법론의 확장

- **Technical Soundness**: 4/5
  - 방법론은 엄밀하고 일관성 있으나, 모델 기반 탐지기의 도메인 일반화 능력에 대한 교차 검증이 부족하고 통계적 유의성 검증 필요

- **Significance**: 4/5
  - 학술 출판의 신뢰성이라는 중대한 문제를 다루며 실제 침투율 측정 결과 제시로 학술계에 의미 있는 기여. 그러나 규제나 정책 수립을 위한 명확한 임계값(threshold) 제시 부족

- **Clarity**: 4/5
  - 전체 파이프라인과 지표 설명이 명확하고 체계적이나, 4장의 SF-IRF 수식과 의미론적 지표 계산 과정이 다소 복잡하게 표현됨

- **Overall**: 4/5

**총평**: 본 논문은 학술 커뮤니티에서 시급한 LLM 투명성 문제를 다루는 실질적 도구와 데이터셋을 제공하며, 다각도 평가 프레임워크와 학술 영역 특화 지표 개발이 돋보인다. 다만 시간성과 도메인 일반화 측면의 한계를 보완한다면 학술 출판 거버넌스 개선에 더욱 기여할 수 있을 것이다.

## Related Papers

- 🔗 후속 연구: [[papers/373_Generalization_Bias_in_Large_Language_Model_Summarization_of/review]] — LLM의 일반화 편향 연구의 한 부분으로 학술 저술 침투도 측정을 통해 편향의 실제 영향을 분석한다.
- 🔄 다른 접근: [[papers/410_How_deep_do_large_language_models_internalize_scientific_lit/review]] — LLM이 과학 문헌을 내재화하는 방식과 함께 학술 워크플로우 전반의 LLM 영향을 종합적으로 이해할 수 있다.
- 🏛 기반 연구: [[papers/611_People_who_frequently_use_ChatGPT_for_writing_tasks_are_accu/review]] — ChatGPT 사용자의 AI 생성 텍스트 탐지 정확도 연구로 LLM 침투도 측정의 기술적 기반을 제공한다.
- 🔗 후속 연구: [[papers/373_Generalization_Bias_in_Large_Language_Model_Summarization_of/review]] — 학술 저술에서 LLM 침투도 측정 연구의 한 부분으로 과도한 일반화 편향의 실증적 증거를 제공한다.
- 🔗 후속 연구: [[papers/410_How_deep_do_large_language_models_internalize_scientific_lit/review]] — 학술 저술에서 LLM 사용 추세 분석의 한 부분으로 참고문헌 생성 시 편향 패턴을 실증적으로 입증한다.
- 🔗 후속 연구: [[papers/444_Is_it_OK_for_AI_to_write_science_papers_Nature_survey_shows/review]] — 학술 작문에서 LLM 침투에 대한 기초 분석을 연구자 태도와 윤리적 합의 필요성으로 확장한 연구입니다.
- 🔄 다른 접근: [[papers/796_The_AI_writing_on_the_wall/review]] — 과학 저술 분야의 생성형 AI 영향과 학술 글쓰기 침투 현상은 서로 다른 관점에서 AI의 학술 환경 변화를 분석한다.
