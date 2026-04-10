---
title: "1029_The_altering_landscape_of_USChina_science_collaboration_from"
authors:
  - "Kensei Kitajima"
  - "Keisuke Okamura"
date: "2025.03"
doi: "10.1057/s41599-025-04550-3"
arxiv: ""
score: 4.0
essence: "본 논문은 bibliometric 데이터를 활용하여 미국-중국 과학 협력의 장기적 변화를 추적하며, 초기의 수렴(convergence) 단계에서 최근의 발산(divergence) 단계로의 전환을 실증적으로 분석했다."
tags:
  - "cat/Research_Quality_and_Demographics"
  - "sub/Collaboration_and_Team_Effects"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Kitajima and Okamura_2025_The altering landscape of US–China science collaboration from convergence to divergence.pdf"
---

# The altering landscape of US–China science collaboration: from convergence to divergence

> **저자**: Kensei Kitajima, Keisuke Okamura | **날짜**: 2025-03-03 | **DOI**: [10.1057/s41599-025-04550-3](https://doi.org/10.1057/s41599-025-04550-3)

---

## Essence

![Figure 3](figures/fig3.webp)

*Fig. 3 Change in the Collaboration Distance among the scientiﬁc*

본 논문은 bibliometric 데이터를 활용하여 미국-중국 과학 협력의 장기적 변화를 추적하며, 초기의 수렴(convergence) 단계에서 최근의 발산(divergence) 단계로의 전환을 실증적으로 분석했다.

## Motivation

- **Known**: 국제 과학 협력은 지난 수십 년간 전반적으로 심화되었으며, 미국과 중국은 전 학문 분야에서 협력을 확대해왔다. 다만 최근 보도들은 두 국가 간 협력의 잠재적 감소를 시사하고 있다.
- **Gap**: 미국-중국 과학 협력의 변화를 시간과 학문 분야에 걸쳐 포괄적으로 정량화한 연구가 부족하며, 전체적 수렴 추세 속에서 이들의 발산 패턴을 설명하는 연구 증거가 미흡하다.
- **Why**: 미국-중국 관계는 글로벌 과학 협력의 미래 궤적을 결정하는 핵심 요소이며, 이러한 변화 양상을 이해하는 것은 과학정책 수립과 과학 외교(science diplomacy) 추진에 중요한 근거를 제공한다.
- **Approach**: OpenAlex의 bibliometric 데이터로부터 논문 식별자(paper identifiers)와 연구자 식별자(researcher identifiers) 두 가지 방식을 활용하여 미국-중국 간 협력 거리(collaboration distance)의 시간적 변화를 분석했다.

## Achievement


- **수렴 후 발산 패턴의 실증화**: 미국-중국 과학 협력이 2000년대부터 급속한 수렴을 보이다가 2019년경을 기점으로 발산(decoupling) 추세로 전환됨을 정량적으로 입증
- **다중 지표 분석**: 협력 거리(collaboration distance), 지식 흐름률(Knowledge Flow Rate, KFR) 등 여러 메트릭을 통해 미국-중국 관계의 복잡한 동역학을 다각도로 포착
- **학제 간 비교 분석**: 주요 5개 과학 강국(미국, 중국, EU27&UK, 일본)의 상호 거리 변화를 시계열로 비교하여 미국-중국 관계의 특이성을 부각
- **정책적 함의 제시**: 미국의 '중국 이니셔티브'(China Initiative, 2018-2022)와 같은 정책 변화와 과학 협력 추이의 연관성을 시사

## How

![Figure 2](figures/fig2.webp)

*Fig. 2 Conceptualisation and quantiﬁcation of bilateral distances using the Jaccard distance. Focusing on a speciﬁc coun*

- OpenAlex 플랫폼에서 bibliometric 데이터 수집 (1970-2021년)
- 논문 식별자 방식: 국가 간 공저 논문 비율을 기반으로 협력 거리 산출
- 연구자 식별자 방식: 연구자의 국제 협력 네트워크를 추적하여 대안적 거리 계산
- Jaccard 유사도(similarity) 등 지표를 역변환하여 거리 메트릭 구성
- 5년 단위 시계열 시각화로 시간적 변화 추적
- 지식 흐름률(KFR) 분석을 통해 협력의 방향성과 강도 평가
- Python 소프트웨어를 활용한 데이터 분석 및 시각화

## Originality

- 미국-중국 과학 협력의 '수렴 후 발산' 패턴을 명확히 입증한 최초의 종합적 정량 분석", '논문 식별자와 연구자 식별자 두 가지 방법론의 병행으로 robust한 결과 도출
- 단순 공저논문 수가 아닌 협력 거리(distance) 개념을 도입하여 상대적 친밀도 변화를 포착
- 국가 간 협력뿐 아니라 학문 분야별 차이를 분석할 수 있는 분석 틀 제시
- 과학 외교(science diplomacy)와 연결한 정책적 해석 제공

## Limitation & Further Study

- OpenAlex 데이터의 완전성과 정확성에 대한 검증이 제한적일 수 있음
- 협력 거리 감소/증가의 원인을 과학 데이터만으로는 인과적으로 규명할 수 없으며, 정치·경제·안보 정책 변수와의 인과관계 추적 필요
- 2021년까지의 데이터로 제한되어 최근 3-4년의 동향을 놓칠 가능성
- 학문 분야별 세부 분석 결과 해석에 있어 각 분야의 특성(예: 국방 관련 연구의 규제)을 더욱 세밀하게 고려해야 함
- 후속 연구: 정성적 심층 인터뷰, 정책 문헌 분석, 자금 흐름 추적 등을 통한 발산 원인의 다층적 규명

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 논문은 OpenAlex 데이터와 다중 방법론을 활용하여 미국-중국 과학 협력의 동적 변화를 실증적으로 분석한 중요한 연구이며, 글로벌 과학 정책과 과학 외교 논의에 실질적인 근거를 제공한다.

## Related Papers

- 🔗 후속 연구: [[papers/967_Global_patterns_of_migration_of_scholars_with_economic_devel/review]] — 경제 발전에 따른 글로벌 학자 이동 패턴이 미중 과학 협력의 수렴-발산 전환에 어떤 영향을 미쳤는지 분석할 수 있다.
- 🏛 기반 연구: [[papers/960_Evolution_of_the_social_network_of_scientific_collaborations/review]] — 과학 협력 네트워크의 진화 원리를 미중 협력의 구체적 사례에 적용하여 지정학적 요인의 영향을 이해할 수 있다.
- 🧪 응용 사례: [[papers/935_Atlas_of_Science_Collaboration_19712020/review]] — 1971-2020년 과학 협력 지도를 통해 미중 협력 변화를 더 넓은 글로벌 맥락에서 비교 분석할 수 있다.
- 🔗 후속 연구: [[papers/967_Global_patterns_of_migration_of_scholars_with_economic_devel/review]] — 전 세계 학자 이동의 거시적 패턴을 미중 과학 협력 변화라는 구체적 사례로 심화 분석 가능
- 🔗 후속 연구: [[papers/935_Atlas_of_Science_Collaboration_19712020/review]] — 미중 과학 협력의 변화하는 지형을 50년간의 국제 과학 협력 아틀라스의 맥락에서 구체적으로 분석한다.
