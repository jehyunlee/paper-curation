---
title: "1058_Why_Most_Published_Research_Findings_Are_False"
authors:
  - "John P. A. Ioannidis"
date: "2005"
doi: "10.1371/journal.pmed.0020124"
arxiv: ""
score: 4.0
essence: "통계적 유의성(p < 0.05)만을 기준으로 발표되는 대부분의 연구 결과는 실제로는 거짓일 수 있으며, 이는 낮은 통계력, 편향, 그리고 다중 독립 연구팀의 반복 검증 부재로 인해 발생한다."
tags:
  - "cat/Research_Quality_and_Demographics"
  - "sub/Research_Evaluation_and_Metrics"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Ioannidis_2005_Why Most Published Research Findings Are False.pdf"
---

# Why Most Published Research Findings Are False

> **저자**: John P. A. Ioannidis | **날짜**: 2005 | **DOI**: [10.1371/journal.pmed.0020124](https://doi.org/10.1371/journal.pmed.0020124)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1. PPV (Probability That a Research*

통계적 유의성(p < 0.05)만을 기준으로 발표되는 대부분의 연구 결과는 실제로는 거짓일 수 있으며, 이는 낮은 통계력, 편향, 그리고 다중 독립 연구팀의 반복 검증 부재로 인해 발생한다.

## Motivation

- **Known**: 발표된 연구 결과 중 상당수가 후속 연구에 의해 반박되고 있으며, 단일 연구의 p-value만으로 결론을 내리는 관행이 널리 퍼져 있다.
- **Gap**: 통계적 유의성 달성이 실제 참(true positive)을 의미한다는 암묵적 가정이 존재하지만, 사전 확률(prior probability), 통계력(statistical power), 편향(bias)을 고려한 체계적 분석이 부족하다.
- **Why**: 현대 의학 및 과학 연구의 신뢰성 위기를 수학적으로 증명함으로써 연구 방법론 개선과 결과 해석의 신중성을 촉구할 수 있다.
- **Approach**: 양성 예측값(PPV; Positive Predictive Value)을 중심으로 한 수학적 프레임워크를 구성하여, 통계력(1-β), 제1종 오류(α), 사전 확률(R), 편향(u), 그리고 독립 반복 연구(n)의 영향을 정량화한다.

## Achievement

![Figure 1](figures/fig1.webp)

*Figure 1. PPV (Probability That a Research*

- **PPV 수학 모델 개발**: 연구 결과가 참일 확률을 PPV = (1-β)R/[R-βR+α]로 표현하여 주요 영향 인자를 명확히 함
- **편향의 정량적 영향**: 편향 계수(u)를 도입하여 선택적 보고와 조작이 PPV를 현저히 감소시킴을 수학적으로 증명
- **독립 연구팀의 누적 효과**: 여러 팀이 동일 질문을 연구할 때 최소 하나의 위양성 발견 확률을 모델링하여 PPV 감소 메커니즘 규명
- **6가지 핵심 추론(Corollary)**: 소규모 샘플, 작은 효과 크기, 다중 검정, 설계 유연성, 이해관계 충돌, 경쟁적 연구팀이 모두 거짓 양성을 증가시킨다는 실증적 결론 도출

## How

![Figure 2](figures/fig2.webp)

*Figure 2. PPV (Probability That a Research*

- 2×2 분할표(contingency table)를 이용한 참/거짓 양성 및 음성 관계 매핑
- 사전 확률 R/(R+1)을 기반으로 사후 확률(PPV) 계산
- Type I 오류(α=0.05)와 Type II 오류(β)의 상호작용 분석
- 편향 계수 u를 포함한 확장된 PPV 공식 도출: PPV = ([1-β]R+uβR)/[R+α-βR+u-uα+uβR]
- n개 독립 연구의 누적 위양성 확률 모델링
- 다양한 통계력 및 사전 확률 조건에서 시뮬레이션을 통한 시각화

## Originality

- 연구 결과의 참/거짓 비율을 역학적 2×2 표 프레임워크로 처음 체계화
- 사전 확률(R) 개념을 의학 연구에 도입하여 베이지안 관점의 통계 해석 제시
- 편향을 정량 파라미터(u)로 모델링하여 방법론적 문제를 수학적으로 정식화
- 단순 통계 유의성 관행의 이론적 허점을 증명적(proof) 형태로 제시한 최초 시도

## Limitation & Further Study

- R 값의 실제 추정이 어려움: 각 연구 분야에서 '참 관계'의 사전 확률을 정확히 파악하기 곤란", '편향 계수 u의 정량화 부재: 실제 연구에서 선택적 보고, p-해킹(p-hacking) 등의 편향 크기를 측정하는 방법 미제시
- 역편향(reverse bias) 빈도에 대한 경험적 증거 부족: 측정 오류나 이해관계 충돌로 인한 참 발견 누락의 실제 발생률 미상
- 후속 연구 필요: (1) 다양한 연구 분야별 R 값 추정 메타분석, (2) 편향 크기 정량화 방법론 개발, (3) 재현 위기(replication crisis) 실제 데이터를 통한 모델 검증

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 5/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 이 논문은 통계적 유의성 중심 패러다임의 근본적 결함을 수학적으로 증명한 획기적 저작으로, 현대 과학 연구의 신뢰성 위기를 정량적으로 설명한다. 단순한 이론 제시를 넘어 구체적 정책 개선(효과 크기 보고, 사전등록, 메타분석 필수화 등)의 과학적 근거를 제공함으로써 의학 및 생명과학 분야에 지대한 영향을 미쳤다.

## Related Papers

- 🔗 후속 연구: [[papers/925_1500_scientists_lift_the_lid_on_reproducibility/review]] — 재현성 위기에 대한 과학자들의 인식 조사와 거짓 연구 결과의 통계적 분석을 결합하여 과학 신뢰성 문제를 종합적으로 이해할 수 있다.
- 🧪 응용 사례: [[papers/958_Estimating_the_Reproducibility_of_Psychological_Science/review]] — 심리과학의 재현성 추정 연구가 Ioannidis의 이론적 예측을 구체적 분야에서 실증적으로 검증하는 사례를 제공한다.
- 🏛 기반 연구: [[papers/987_Meta-assessment_of_Bias_in_Science/review]] — 과학에서의 편향에 대한 메타 평가가 거짓 연구 결과 발생의 구조적 원인을 더 체계적으로 분석하는 방법론을 제공한다.
- 🏛 기반 연구: [[papers/959_Evaluating_the_Replicability_of_Social_Science_Experiments_i/review]] — 발표된 대부분의 연구 결과가 거짓이라는 이론적 주장에 대해 실제 재현 실험을 통한 실증적 증거를 제공한다.
- 🏛 기반 연구: [[papers/925_1500_scientists_lift_the_lid_on_reproducibility/review]] — 과학자들이 인식하는 재현성 위기가 통계적으로 예측되는 거짓 연구 결과 문제와 일치하는 실증적 증거를 제공한다.
- 🏛 기반 연구: [[papers/987_Meta-assessment_of_Bias_in_Science/review]] — 연구 결과의 거짓 양성 문제와 편향의 체계적 발생이 과학의 신뢰성 위기를 공통으로 다룸
- 🏛 기반 연구: [[papers/988_Misconduct_Accounts_for_the_Majority_of_Retracted_Scientific/review]] — 연구 부정행위와 거짓 연구 결과가 모두 과학의 신뢰성과 품질 문제를 다루는 핵심 이슈
