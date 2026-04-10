---
title: "1021_Scientific_production_in_the_era_of_large_language_models"
authors:
  - "Keigo Kusumegi"
  - "Xinyu Yang"
  - "Paul Ginsparg"
  - "Mathijs de Vaan"
  - "Toby Stuart"
date: "2025"
doi: "10.1126/science.adw3000"
arxiv: ""
score: 4.0
essence: "대규모 LLM(Large Language Models) 도입이 과학 논문 생산성을 36-60% 증가시키고, 특히 비영어권 연구자의 진입장벽을 낮추지만, 글쓰기 복잡도가 더 이상 연구 품질의 신뢰할 수 있는 지표가 되지 않게 변화시킨다."
tags:
  - "cat/Research_Quality_and_Demographics"
  - "sub/Research_Evaluation_and_Metrics"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Kusumegi et al._2025_Scientific production in the era of large language models 2.pdf"
---

# Scientific production in the era of large language models

> **저자**: Keigo Kusumegi, Xinyu Yang, Paul Ginsparg, Mathijs de Vaan, Toby Stuart, Yian Yin | **날짜**: 2025 | **DOI**: [10.1126/science.adw3000](https://doi.org/10.1126/science.adw3000)

---

## Essence


대규모 LLM(Large Language Models) 도입이 과학 논문 생산성을 36-60% 증가시키고, 특히 비영어권 연구자의 진입장벽을 낮추지만, 글쓰기 복잡도가 더 이상 연구 품질의 신뢰할 수 있는 지표가 되지 않게 변화시킨다.

## Motivation

- **Known**: AI 기술이 단백질 구조 예측과 신소재 발견 같은 특정 과학 분야에서 가치를 입증했으나, LLM의 거시적 과학 생산성 영향에 대한 체계적 이해는 부족했다.
- **Gap**: LLM 도입 후 과학 출판 패턴, 저자 생산성, 글쓰기 품질과 출판 성과의 관계 변화에 대한 대규모 실증 데이터가 없었다.
- **Why**: LLM이 급속히 확산되는 상황에서 과학 생산 과정의 근본적 변화를 이해하고, 과학 정책입안자들이 제도를 조정하기 위해 필수적이다.
- **Approach**: 2018년 1월-2024년 6월 arXiv, bioRxiv, SSRN 등 3개 프리프린트 저장소에서 199만 개 논문을 수집하고, AI 탐지 알고리즘(AI detection algorithm)을 적용하여 LLM 사용 여부를 판별한 후, 저자 고정효과 사건 분석(author-level fixed-effects event models)으로 LLM 채택의 인과효과를 추정했다.

## Achievement


- **생산성 증가**: LLM 채택 후 논문 제출 빈도가 arXiv 36.2%, bioRxiv 52.9%, SSRN 59.8% 증가
- **비대칭적 이점**: 아시아계 저자와 아시아 소재 기관 소속 연구자가 23.7-89.3% 생산성 향상으로 영어권 저자(23.7-46.2%)보다 더 큰 이득
- **글쓰기 복잡도 역전**: LLM 비사용 논문은 글쓰기 복잡도가 높을수록 출판 확률 증가하지만, LLM 사용 논문은 복잡도가 높을수록 출판 확률 감소(역의 관계)
- **신뢰성 약화**: LLM이 쉽게 복잡한 과학 문장을 생성하므로, 글쓰기 복잡도가 더 이상 연구 품질의 신뢰할 수 있는 신호가 아님을 입증

## How


- AI 탐지 알고리즘: 2023년 이전 인간 저술 추상을 기준으로 토큰(단어) 분포 학습, ChatGPT 이후 논문과 비교하여 LLM 사용 여부 식별
- 인과추론: LLM 미채택 저자를 대조군으로 설정하고 저자 고정효과 이벤트 스터디 모형으로 채택 전후 생산성 변화 측정
- 네이티브 언어 추정: 저자 이름과 소속 기관 정보를 바탕으로 영어 모국어 여부 분류하여 이질성 분석
- 글쓰기 복잡도 측정: Flesch Reading Ease 점수의 역수를 사용하여 평균 문장 길이와 음절 수 종합
- 출판 결과 추적: 2023년 이후 프리프린트의 동료심사 학술지·학술대회 게재 여부를 2024년 6월까지 추적

## Originality

- LLM 시대의 첫 대규모 거시적 실증 연구: 199만 개 논문 데이터로 LLM 도입의 과학 생산성 영향을 정량화
- 혁신적 인과성 식별 전략: 저자의 '첫 LLM 사용' 시점을 기준으로 한 이벤트 스터디로 순수 인과효과 추정", '글쓰기 품질-출판 성과 관계의 역전 발견: LLM 사용으로 인해 전통적 품질 신호(글쓰기 복잡도)의 예측력이 반전되는 새로운 현상 발견
- 국제 형평성 효과 규명: 비영어권 연구자의 불균형적 이익을 정량적으로 입증하여 과학 민주화의 양면성 분석

## Limitation & Further Study

- **AI 탐지 신뢰도**: 텍스트 기반 AI 탐지 알고리즘의 위양성/위음성 오류 가능성, 특히 정교한 저자의 혼합 사용(hybrid writing) 포착 미흡
- **인과성의 한계**: LLM 채택자와 미채택자 간 관찰되지 않은 이질성(unobserved heterogeneity) 존재 가능, 관찰된 공변량만으로 완전한 인과효과 추정 불가능
- **언어권 추정 오류**: 저자 이름과 소속 기관만으로 네이티브 영어 사용자 분류하므로 개인차 미반영
- **출판 시간 지연**: 프리프린트 제출 후 동료심사 및 게재까지 시간이 소요되므로, 2023년 이후 논문의 출판 결과는 아직 불완전할 수 있음
- **장기 품질 영향 미상**: 글쓰기 복잡도 역전이 실제 과학적 신뢰도 하락을 의미하는지, 아니면 단순 지표 왜곡인지는 추가 검증 필요
- **후속연구**: (1) 생성된 텍스트의 실제 과학적 정확성과 창의성을 직접 평가하는 연구, (2) 5년 이상 장기 인용 영향도(citation impact) 추적, (3) LLM 기능 고도화에 따른 동적 효과 분석, (4) 다양한 학문 분야별 차등 영향 심층 분석

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 과학 출판의 LLM 영향을 최초로 대규모 정량화한 중요한 실증 연구로, 비영어권 연구자 역량강화의 긍정적 효과와 함께 전통적 품질 평가 지표의 신뢰도 약화라는 심각한 제도적 과제를 제시한다. 과학 정책과 동료심사 체계의 근본적 개선이 시급하다.

## Related Papers

- 🔗 후속 연구: [[papers/1119_Publish_and_Perish_How_AI-Accelerated_Writing_Without_Propor/review]] — AI 가속화된 논문 작성이 동료 검증 시스템에 미치는 부담을 정량적으로 분석하여 생산성 증가의 역설을 설명한다.
- ⚖️ 반론/비판: [[papers/953_Do_Large_Language_Models_Reduce_Research_Novelty_Evidence_fr/review]] — LLM이 연구 생산성을 높이지만 동시에 연구 참신성을 감소시킬 수 있는 상반된 효과를 보여준다.
- 🏛 기반 연구: [[papers/1077_Quantifying_large_language_model_usage_in_scientific_papers/review]] — 과학 논문에서 대규모 언어모델 사용을 정량화하여 LLM 시대 과학 생산의 변화를 실증적으로 뒷받침한다.
- 🔗 후속 연구: [[papers/1077_Quantifying_large_language_model_usage_in_scientific_papers/review]] — 대형 언어 모델 시대의 과학적 생산성 변화에 대한 포괄적 분석을 통해 LLM 사용률 정량화의 의미를 더 깊이 이해할 수 있다.
- 🔗 후속 연구: [[papers/953_Do_Large_Language_Models_Reduce_Research_Novelty_Evidence_fr/review]] — 대규모 언어모델 시대의 과학적 생산성 변화를 의미론적 새로움 감소라는 구체적 지표로 확장하여 측정한다.
- 🏛 기반 연구: [[papers/1119_Publish_and_Perish_How_AI-Accelerated_Writing_Without_Propor/review]] — LLM 시대 과학 생산 증가의 역설적 결과로 동료 검증 시스템의 한계가 지식 생산 감소로 이어지는 구조적 문제를 설명한다.
- 🔗 후속 연구: [[papers/988_Misconduct_Accounts_for_the_Majority_of_Retracted_Scientific/review]] — 대규모 언어모델 시대의 과학 생산에서 새로운 형태의 부정행위 가능성을 확장하여 다룬다
