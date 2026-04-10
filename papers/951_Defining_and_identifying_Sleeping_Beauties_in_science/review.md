---
title: "951_Defining_and_identifying_Sleeping_Beauties_in_science"
authors:
  - "Qing Ke"
  - "Emilio Ferrara"
  - "Filippo Radicchi"
  - "Alessandro Flammini"
date: "2015.06"
doi: "10.1073/pnas.1424329112"
arxiv: ""
score: 4.0
essence: "과학 논문 중 발표 후 수십 년간 인용되지 않다가 갑자기 높은 인용도를 보이는 '잠자는 미녀(Sleeping Beauty)' 현상을 정량화하는 매개변수 무관(parameter-free) 지표를 제시하고, 2천2백만 개 논문 분석으로 이 현상이 예외가 아닌 보편적 현상임을 규명했다."
tags:
  - "cat/Scientific_Impact_and_Innovation"
  - "cat/Science_of_Science_Research"
  - "sub/Citation_metrics_and_impact_measurement"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Ke et al._2015_Defining and identifying Sleeping Beauties in science.pdf"
---

# Defining and identifying Sleeping Beauties in science

> **저자**: Qing Ke, Emilio Ferrara, Filippo Radicchi, Alessandro Flammini | **날짜**: 2015-06-16 | **DOI**: [10.1073/pnas.1424329112](https://doi.org/10.1073/pnas.1424329112)

---

## Essence


과학 논문 중 발표 후 수십 년간 인용되지 않다가 갑자기 높은 인용도를 보이는 '잠자는 미녀(Sleeping Beauty)' 현상을 정량화하는 매개변수 무관(parameter-free) 지표를 제시하고, 2천2백만 개 논문 분석으로 이 현상이 예외가 아닌 보편적 현상임을 규명했다.

## Motivation

- **Known**: 과학 논문의 인용은 발표 후 수 년간 최고조에 달했다가 감소하는 패턴을 보인다. 소수의 논문들은 장기간의 '잠눈 기간' 이후 갑작스러운 인용 급증을 경험하지만, 이러한 경우가 매우 드물다고 여겨졌다.
- **Gap**: 기존 연구는 자의적 임계값(sleeping time, citation count)에 의존하고 소규모 또는 단일 학문 데이터셋에 적용되었으며, 잠자는 미녀 현상을 예외적 사례로만 취급했다. 매개변수 없는 정량적 정의와 대규모 다학제 분석이 부재했다.
- **Why**: 인용 메트릭스는 학자 평가, 연구비 배분, 승진 결정 등에 광범위하게 사용되므로, 지연된 인정 현상을 이해하는 것은 단기 인용 지표의 한계를 규명하고 과학 영향력 평가의 신뢰성을 높이는 데 중요하다.
- **Approach**: 논문 발표년, 최대 연간 인용수, 최대값 달성 시점만을 이용하여 기준선(reference line)을 설정하고, 실제 인용 궤적과의 편차를 누적한 '뷰티 계수(Beauty Coefficient, B)'를 개발했다. 1세기 이상의 모든 학문 분야 2천2백만 논문에 적용하여 B의 분포를 분석했다.

## Achievement

![Figure 2](figures/fig2.webp)

*Fig. 2D is characterized by a negative B value, as ct is above the reference line.*

- **매개변수 무관 정량 지표 개발**: 임의의 임계값 없이 모든 논문의 지연 인정 정도를 정량화할 수 있는 뷰티 계수 B를 제시
- **보편적 현상 규명**: 잠자는 미녀 현상이 예외가 아닌 continuous spectrum을 이루는 보편적 현상임을 규명하고, B의 분포가 power-law 거동을 보임
- **초장기 지연 인정 확인**: 많은 논문이 발표 50년 이상 후에 최고 인용도에 도달하며, 단기 인용 지표의 부적절함을 실증적으로 입증
- **다학제 특성 발견**: 물리학·화학·수학 등 특정 학문이 top sleeping beauties를 더 높은 비율로 생성하며, 많은 최상 사례가 원래 학문과 다른 분야에서 지연 인정을 받음

## How


- 뷰티 계수 B = Σ(기준선-실제인용수)/max(1, 실제인용수), 여기서 기준선은 (0, c₀)과 (tₘ, cₜₘ)을 연결하는 직선
- 발표년도와 최대 연간 인용수 달성 시점 정보만으로 각 논문의 B값 계산
- Web of Science, Scopus 등 대규모 서지 데이터베이스에서 2천2백만 논문 추출
- 단일 학문별 분석과 다학제 간 교차 인용 분석 수행
- B값 분포의 통계적 특성(power-law, continuous spectrum) 검증
- 깨어남 시점(awakening time) 식별 알고리즘 적용

## Originality

- 기존의 arbitrary thresholds (van Raan의 3가지 차원, Redner의 명확한 기준값)를 완전히 제거한 parameter-free 접근법 개발
- 잠자는 미녀를 '희귀한 예외'가 아닌 '연속 스펙트럼의 일부'로 재개념화", '단순한 기준선(reference line) 기하학적 개념으로 sleeping period와 awakening intensity를 동시에 포착
- 세기 단위의 시간 스케일과 수천만 개 논문의 대규모 데이터로 현상의 보편성 입증
- 학문 간 지연 인정 패턴 분석으로 새로운 다학제 특성 발견

## Limitation & Further Study

- B값이 0 이상의 범위만 가지므로, 비선형 성장(예: 지수적 성장)의 경우 충분히 포착하지 못할 가능성
- 각 학문 분야의 인용 문화 및 maturation time의 차이를 명시적으로 고려하지 않음
- 깨어남 메커니즘의 근본 원인(paradigm shift, new technology availability 등)에 대한 분석 부재
- 후속 연구: 뷰티 계수의 예측 모델 개발, 학문별 인용 역학의 차이 분석, 깨어남 트리거 요인의 질적 분석
- 후속 연구: 다중 깨어남 현상(multiple awakenings) 및 비단조적 인용 패턴 연구

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 논문은 과학적 영향력 평가의 기본 가정을 도전하는 중요한 실증 연구로서, 매개변수 무관의 우아한 정량 지표를 제시하고 대규모 다학제 데이터를 통해 지연된 인정이 보편적 현상임을 규명했다. 단기 인용 지표의 한계를 명확히 하고 향후 과학 평가 체계 개선을 위한 중요한 근거를 제공한다.

## Related Papers

- 🔗 후속 연구: [[papers/954_Do_novel_papers_attract_more_social_attention/review]] — 잠자는 미녀 논문의 지연된 학술적 인정이 소셜 미디어에서는 어떤 관심을 받는지 확장하여 분석할 수 있다.
- 🔄 다른 접근: [[papers/956_Early_career_setback_and_future_achievement_in_professional/review]] — 경력 초기 좌절과 잠자는 미녀 현상 모두 지연된 인정이라는 공통점을 가지지만 서로 다른 메커니즘을 보여준다.
- 🧪 응용 사례: [[papers/936_Atypical_Combinations_and_Scientific_Impact/review]] — 비전형적 조합과 과학적 영향력 연구와 연결되어 잠자는 미녀 논문들이 보이는 비전형적 특성과 지연된 인정 패턴을 설명한다.
- 🔗 후속 연구: [[papers/1004_Quantifying_spatialtemporal_citation_diffusion_of_individual/review]] — 잠자는 미녀 논문의 지연된 인용 패턴을 공간-시간적 확산 모델로 더 정교하게 분석할 수 있는 방법론을 제시한다.
- 🔄 다른 접근: [[papers/934_Are_disruptive_papers_more_likely_to_impact_technology_and_s/review]] — 즉각적 파괴성 대신 장기간 잠들어 있다가 재발견되는 논문의 특성을 분석한다.
