---
title: "1057_Which_stylistic_features_fool_ChatGPT_research_evaluations"
authors:
  - "Kayvan Kousha"
  - "Mike Thelwall"
date: "2026.03"
doi: ""
arxiv: ""
score: 4.0
essence: "ChatGPT는 추상(abstract)의 언어적 복잡성과 길이에 과도하게 반응하여 연구 품질을 평가하는데, 이는 인간 전문가의 평가와 달리 스타일 편향(stylistic bias)을 보인다."
tags:
  - "cat/Scientific_Impact_and_Innovation"
  - "sub/Artificial_intelligence_and_science"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Kousha and Thelwall_2026_Which stylistic features fool ChatGPT research evaluations.pdf"
---

# Which stylistic features fool ChatGPT research evaluations?

> **저자**: Kayvan Kousha, Mike Thelwall | **날짜**: 2026-03-16 | **URL**: [https://arxiv.org/abs/2603.14919](https://arxiv.org/abs/2603.14919)

---

## Essence


ChatGPT는 추상(abstract)의 언어적 복잡성과 길이에 과도하게 반응하여 연구 품질을 평가하는데, 이는 인간 전문가의 평가와 달리 스타일 편향(stylistic bias)을 보인다.

## Motivation

- **Known**: LLM은 논문 제목과 초록만으로도 연구 품질을 적당한 수준으로 추정할 수 있으며, 전체 텍스트보다 이 짧은 정보로 더 나은 성과를 보인다.
- **Gap**: LLM 기반 연구 평가가 왜 인간 전문가 점수와 적당히 일치하는지 메커니즘이 불명확하며, 연구 품질과 무관한 언어적 특성이 LLM 점수에 미치는 영향을 체계적으로 분석한 연구가 부재하다.
- **Why**: LLM이 점점 더 연구 평가 지원에 활용되고 있으므로, 스타일 편향을 파악하여 저자의 조작 가능성을 평가하고 LLM 기반 평가 시스템의 신뢰성을 확보할 필요가 있다.
- **Approach**: UK REF 2021에 제출된 99,277개 논문 데이터셋에서 초록의 가독성, 언어적 복잡성, 길이 등의 지표를 계산하여 ChatGPT 점수 및 전문가 점수와의 상관관계를 비교 분석한다.

## Achievement


- **언어적 복잡성에 대한 편향 발견**: ChatGPT는 많은 학문 분야에서 언어적 복잡성과 길이를 인간 전문가보다 훨씬 강하게 고려하여 점수를 부여한다.
- **분야별 차이 규명**: 주제 영역(UoA)에 따라 스타일 특성과 점수 간 상관관계의 강도와 패턴이 상이하게 나타난다.
- **실무적 위험성 제시**: 긴 초록과 낮은 가독성이 실제 연구 품질과 무관하게 ChatGPT 점수를 높일 수 있어 평가 조작 가능성을 시사한다.

## How


- REF 2021 데이터셋(99,277개 논문)에서 학문 분야별로 층화 샘플링 수행
- 초록의 가독성 지표 계산(Flesch Reading Ease, Gunning Fog Index 등)
- 초록 길이, 단어 수, 문장 수 등의 언어적 특성 추출
- ChatGPT에 제목과 초록을 입력하여 연구 품질 점수 획득
- Pearson/Spearman 상관분석으로 스타일 특성과 LLM 점수의 관계 분석
- 동일 자료에 대해 REF 전문가 점수와의 상관관계도 병렬 분석
- 학문 분야별 부분군 분석으로 차이점 검증

## Originality

- 초록의 객관적 스타일 특성(가독성, 복잡성, 길이)과 LLM 점수의 관계를 체계적으로 규명한 첫 연구
- LLM 편향을 인간 전문가와 직접 비교하는 설계로 '속임수(cheating)' 가설을 실증적으로 검증", 'REF 같은 실제 정책 평가 데이터셋(99,277개)을 사용하여 높은 현실 타당성 제공
- 학문 분야별 차이를 규명하여 분야 특성에 따른 편향의 이질성 입증

## Limitation & Further Study

- **인과관계 미규명**: 상관관계만 분석했으므로 스타일이 점수를 직접 결정하는지 간접요인인지 확실하지 않음
- **프록시 점수 사용**: 개별 논문 점수가 아닌 부서 평균 점수를 대리변수로 사용하여 측정오차 존재
- **ChatGPT 버전 특정성**: 특정 모델 버전만 분석했으므로 다른 LLM이나 최신 버전으로의 일반화 제한
- **인과성 실험 필요**: 향후 A/B 테스트(예: 동일 내용의 고/저 복잡성 초록 제시)로 인과관계 검증
- **개선 방안 연구**: LLM 프롬프트 엔지니어링이나 파인튜닝으로 스타일 편향 완화 방안 모색 필요

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: LLM의 스타일 편향을 대규모 실증 데이터로 처음 규명한 중요한 연구로, 연구 평가 시스템의 신뢰성 문제를 제기하고 향후 LLM 개선 방향을 제시한다.

## Related Papers

- 🔄 다른 접근: [[papers/941_Big_Names_or_Big_Ideas_Do_Peer-Review_Panels_Select_the_Best/review]] — 인간 전문가의 동료평가와 AI의 연구 평가에서 각각 나타나는 서로 다른 형태의 편향을 비교 분석한다.
- 🔗 후속 연구: [[papers/987_Meta-assessment_of_Bias_in_Science/review]] — 과학에서의 편향을 메타 평가하는 연구를 AI 시스템의 평가 편향으로 확장하여 새로운 차원의 편향을 규명한다.
- 🧪 응용 사례: [[papers/1068_Artificial_intelligence_and_illusions_of_understanding_in_sc/review]] — ChatGPT 연구 평가에서 문체적 특성이 미치는 영향을 통해 AI 도구의 이해 환상 메커니즘을 구체적으로 분석한다.
