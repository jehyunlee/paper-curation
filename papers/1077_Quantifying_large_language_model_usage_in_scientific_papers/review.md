---
title: "1077_Quantifying_large_language_model_usage_in_scientific_papers"
authors:
  - "Weixin Liang"
  - "Yaohui Zhang"
  - "Zhengxuan Wu"
  - "Haley Lepp"
  - "Wenlong Ji"
date: "2025.08"
doi: "10.1038/s41562-025-02273-8"
arxiv: ""
score: 4.0
essence: "2020년 1월부터 2024년 9월까지 112만여 개의 학술논문을 분석하여 대규모언어모델(LLM, Large Language Model)의 사용 비율을 단어빈도 변화 기반 모집단 수준 프레임워크로 정량화한 연구이다."
tags:
  - "cat/Science_of_Science_Research"
  - "sub/AI_and_Large_Language_Models"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Liang et al._2025_Quantifying large language model usage in scientific papers.pdf"
---

# Quantifying large language model usage in scientific papers

> **저자**: Weixin Liang, Yaohui Zhang, Zhengxuan Wu, Haley Lepp, Wenlong Ji, Xuandong Zhao, Hancheng Cao, Sheng Liu, Siyu He, Zhi Huang, Diyi Yang, Christopher Potts, Christopher D. Manning, James Zou | **날짜**: 2025-08-04 | **DOI**: [10.1038/s41562-025-02273-8](https://doi.org/10.1038/s41562-025-02273-8)

---

## Essence

![Figure 1](figures/fig1.webp)

*Fig. 1 | Estimated fraction of LLM-modified sentences across research paper*

2020년 1월부터 2024년 9월까지 112만여 개의 학술논문을 분석하여 대규모언어모델(LLM, Large Language Model)의 사용 비율을 단어빈도 변화 기반 모집단 수준 프레임워크로 정량화한 연구이다.

## Motivation

- **Known**: ChatGPT 출시(2022년 11월) 이후 학술 논문에서 LLM 생성 콘텐츠의 사용 증가가 관찰되고 있으나, 개별 문서 수준의 정확한 탐지는 기술적·윤리적 한계가 있다.
- **Gap**: LLM 사용의 실제 규모와 학문 분야별·저자 특성별 분포 현황이 체계적으로 파악되지 않았으며, 개별 탐지 방식의 신뢰성 문제(특히 비영어권 저자에 대한 편향)가 존재한다.
- **Why**: 학술 출판의 무결성, 공정성, 투명성 확보 및 정책 입안을 위해 LLM 사용의 객관적 규모 파악이 시급하며, 어떤 분야와 저자군에서 LLM이 집중적으로 사용되는지 이해하는 것이 중요하다.
- **Approach**: 개별 문서 분류 대신 모집단 수준의 단어빈도 변화(distributional GPT quantification framework)를 활용하여 코퍼스 전체에서 LLM 수정 텍스트의 비율(α)을 추정하는 방식으로 시간대별·학문별 추이를 추적했다.

## Achievement

![Figure 1](figures/fig1.webp)

*Fig. 1 | Estimated fraction of LLM-modified sentences across research paper*

- **컴퓨터과학 분야의 급격한 LLM 사용 증가**: 2024년 9월 초록 22.5%, 서론 19.6%로 증가 (2022년 11월 2.4% 대비)
- **학문 분야별 차등적 채택**: 전기공학(18%), 물리학 > 수학(7.7%), Nature 저널(8.9%) 순으로 LLM 수정 비율이 낮아짐
- **저자 특성별 상관관계 규명**: 프리프린트 게시 빈도가 높은 제1저자, 혼잡한 연구 분야, 짧은 논문에서 더 높은 LLM 사용 추정치
- **신뢰성 검증 완료**: 2022년 11월 이전 데이터로 모델 훈련, 임계값 0-25% 범위에서 오차 3.5% 이하로 정확성 확인

## How

![Figure 2](figures/fig2.webp)

*Fig. 2 | Fine-grained validation of estimation accuracy under temporal*

- arXiv(86만 개), bioRxiv(20만 개), Nature 포트폴리오 저널(5.5만 개)에서 2020-2024년 논문 수집
- ChatGPT 출시 전(2022년 11월 이전) 데이터로 모델 훈련, 2021년 이후 데이터로 검증 및 추론
- 각 학문 분야별·시간 단위별로 초록과 서론의 단어빈도 분포 분석
- LLM 생성 텍스트로 합성한 훈련 데이터 사용 (two-stage approach)
- 부트스트래핑(bootstrapping) 방식으로 95% 신뢰구간(CI) 산출
- 컴퓨터과학 분야에서 초록, 서론, 관련연구, 방법, 실험, 결론 등 여러 섹션 상세 분석

## Originality

- 개별 문서 분류가 아닌 모집단 수준 추론으로 대규모 코퍼스 분석을 확장 가능하게 설계
- 시간 분포 변화(temporal distribution shift) 조건에서도 높은 정확성(오차 <3.5%) 달성으로 방법론 신뢰성 확보
- 학문 분야별·저자 특성별·시간대별 3차원 분석을 통해 LLM 채택의 구조적·제도적 맥락 규명
- 115만 개 논문이라는 대규모 다학제 데이터셋 활용으로 높은 일반화 가능성

## Limitation & Further Study

- LLM 수정의 정의('기본 철자·문법 교정 이상')이 주관적이며, 다른 생성AI(GPT 이전 모델 포함)의 영향 구분 어려움", '초록과 서론에만 집중(전체 논문의 일부만 분석)했으며, 다른 섹션의 LLM 사용 패턴 차이 반영 부분적
- 모델 훈련에 사용된 LLM 생성 데이터의 품질과 대표성이 실제 학술 LLM 사용과 정확히 일치하는지 검증 필요
- **후속 연구**: (1) 특정 학술 분야에서 LLM 사용이 논문 품질, 정확성, 혁신성에 미치는 영향 분석, (2) 비영어권 저자 비율이 높은 분야에서 LLM 의존도와 언어적 소외의 상관관계 심화 분석, (3) 피어리뷰 과정에서의 LLM 사용 규모 추정 확대

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 학술 출판에서 LLM 사용의 실제 규모를 처음으로 정량화한 중요한 연구로, 모집단 수준의 통계적 방법론으로 개별 탐지의 한계를 극복했다. 분야별 차등적 채택 패턴과 저자 특성 간의 상관관계 규명을 통해 학술 커뮤니케이션의 구조적 변화를 이해하는 데 기여할 수 있으나, LLM 사용이 논문의 실제 품질과 신뢰성에 미치는 영향에 대한 심층 분석은 향후 과제이다.

## Related Papers

- 🔗 후속 연구: [[papers/1021_Scientific_production_in_the_era_of_large_language_models/review]] — 대형 언어 모델 시대의 과학적 생산성 변화에 대한 포괄적 분석을 통해 LLM 사용률 정량화의 의미를 더 깊이 이해할 수 있다.
- 🏛 기반 연구: [[papers/953_Do_Large_Language_Models_Reduce_Research_Novelty_Evidence_fr/review]] — LLM이 연구 참신성에 미치는 영향에 대한 실증적 근거를 제공하여 LLM 사용률 측정의 중요성을 뒷받침한다.
- 🔗 후속 연구: [[papers/1041_The_Rise_of_Large_Language_Models_and_the_Direction_and_Impa/review]] — LLM 사용률 정량화 방법론을 통해 연구 제안서뿐만 아니라 학술논문 전반의 LLM 영향을 더 체계적으로 측정할 수 있다.
- 🏛 기반 연구: [[papers/1021_Scientific_production_in_the_era_of_large_language_models/review]] — 과학 논문에서 대규모 언어모델 사용을 정량화하여 LLM 시대 과학 생산의 변화를 실증적으로 뒷받침한다.
- 🔗 후속 연구: [[papers/1078_Quantifying_the_use_and_potential_benefits_of_artificial_int/review]] — 과학 논문에서 대규모 언어모델 사용을 정량화하는 연구를 AI의 전반적 활용과 잠재 이익 측정으로 확장한다.
