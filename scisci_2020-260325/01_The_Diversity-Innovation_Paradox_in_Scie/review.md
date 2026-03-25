# The Diversity-Innovation Paradox in Science

> **저자**: Bas Hofstra, Vivek V. Kulkarni, Sebastian Munoz-Najar Galvez, Bryan He, Dan Jurafsky, Daniel A. McFarland | **날짜**: 2020 | **Journal**: Proceedings of the National Academy of Sciences | **DOI**: 10.1073/pnas.1915378117

---

## Essence

다양성은 혁신을 낳지만, 그 혁신을 만들어낸 소수자 집단은 보상받지 못한다. 미국 박사학위 수여자 약 120만 명(1977-2015)의 학위논문을 분석한 결과, 성별/인종 소수자 그룹이 더 높은 비율로 새로운 개념적 연결(novelty)을 도입하지만, 이들의 새로운 기여는 다수자 그룹 대비 낮은 비율로 후속 연구에 채택(uptake)되며, 동일한 수준의 혁신성을 가져도 교수직 획득 확률이 5~25% 더 낮다.

## Motivation

- **알려진 사실**: 인구통계학적 다양성이 혁신을 촉진한다는 것은 널리 알려져 있으며(Granovetter 1973, Burt 2004, Page 2009), 혁신은 성공적 학술 경력과 양의 상관관계를 가짐
- **격차(Gap)**: 다양성이 혁신을 낳고, 혁신이 성공적 경력으로 이어진다면, 소수자 집단의 학술 경력이 왜 지속적으로 불평등한지 설명할 수 없음
- **접근법**: NLP 기반 텍스트 분석과 머신러닝으로 약 120만 건의 박사 논문에서 과학적 개념 쌍의 새로운 연결(novel conceptual linkages)을 식별하고, 이것이 인구통계학적 그룹별로 어떻게 생성, 채택, 보상되는지를 체계적으로 추적

## Achievement

1. **소수자의 높은 혁신율**: 성별/인종 소수자 그룹이 다수자 대비 통계적으로 유의하게 더 많은 새로운 개념적 연결을 도입 (P < 0.001)
2. **혁신의 차별적 채택**: 여성과 비백인 학자의 새로운 개념 연결은 남성/백인 학자 대비 낮은 비율로 후속 연구에 채택됨 (P < 0.05)
3. **원거리 혁신(distal novelty) 메커니즘**: 소수자 그룹이 의미적으로 더 먼 개념 간 연결을 도입하는 경향이 있으며(P < 0.001), 이러한 원거리 연결은 채택률이 더 낮음
4. **경력 보상의 불평등**: novelty 2SD 증가 시 성별 소수자-다수자 간 교수직 획득 확률 격차가 3.5%에서 9.5%로, impactful novelty 기준으로는 4.3%에서 15%로 확대
5. **인종적 불평등**: 인종 소수자는 교수직 획득 odds가 25% 낮고, 연구 경력 지속 odds가 10% 낮음 (novelty와 impactful novelty를 통제한 후에도)

## How

- **데이터**: ProQuest 박사논문 데이터베이스(1977-2015, ~120만 건) + Web of Science(~3,800만 건 출판물) + US Census/SSA 데이터(성별/인종 추론)
- **개념 추출**: Structural Topic Model(K=500)과 FREX 점수를 활용한 핵심 과학 개념 추출 (논문당 평균 56.5개 개념)
- **혁신 측정**: 논문 내 개념 쌍의 최초 동시 출현(co-occurrence)을 novelty로, 후속 논문에서의 채택 빈도를 impactful novelty로 정의
- **의미적 거리**: Skip-gram word embedding(100차원)으로 개념 간 cosine distance 계산하여 distal novelty 측정
- **통계 분석**: Negative binomial regression(novelty, impactful novelty), Linear regression(distal novelty), Logistic regression(경력 변수), 기관/학문분야/연도 고정효과 포함
- **인구통계 추론**: 이름 기반 성별/인종 분류 알고리즘(US Census + SSA + 사립대학 검증 데이터 n=20,264)

## Originality

과학적 혁신을 텍스트 기반 개념 재조합으로 정의하고, 이를 인구통계학적 다양성-혁신-경력 보상의 전체 파이프라인으로 연결한 최초의 대규모 시스템 수준 연구이다. 기존의 인용 기반 혁신 측정 방식과 달리, 학문 분야 간 저널 색인 편향에 영향받지 않는 개념 재조합 메트릭을 제안했으며, word embedding을 활용한 "원거리 혁신(distal novelty)" 개념을 도입하여 소수자 혁신이 저평가되는 메커니즘을 규명했다.

## Limitation & Further Study

### 저자들이 언급한 한계
- 성별/인종 분류가 이름 기반 추론에 의존하여 자기 정체성과 괴리될 수 있음
- 소수 인종 그룹(Hispanic, African American, Native American)을 통합한 "underrepresented minority" 범주가 다소 조잡함
- 개념 embedding이 시간에 따른 의미 변화를 반영하지 못함 (글로벌 평균 사용)

### 리뷰어 판단 아쉬운 점
- 박사논문 초록만을 분석 대상으로 하여, 이후 출판 논문의 혁신성과의 관계가 명확하지 않음
- "채택(uptake)"이 낮은 이유가 편견인지, 아니면 실제로 해당 연결이 생산적이지 않았는지 구분하기 어려움
- 학문 분야별 분석이 부족하여, 특정 분야에서 역설이 더 심한지 알 수 없음
- 인과관계 주장이 어려운 관찰 연구임에도 불구하고, "discounting"이라는 표현이 의도적 차별을 암시하는 측면이 있음

### 후속 연구
- 분야별(STEM vs. 인문사회) 다양성-혁신 역설의 차이 분석
- 시간에 따른 역설의 변화 추이 (개선되고 있는지 여부)
- 소수자 혁신의 "지연된 인정(delayed recognition)" 가능성 탐구
- 기관 유형별(연구중심대학 vs. 교육중심대학) 차별적 보상 패턴 분석

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 5/5 |
| Technical Soundness | 4/5 |
| Significance | 5/5 |
| Clarity | 4/5 |
| Overall | 4/5 |

**총평**: 과학에서 다양성과 혁신, 그리고 경력 보상 사이의 구조적 역설을 120만 명 규모의 데이터로 실증한 획기적 연구로, Science of Science 분야에서 다양성 담론의 기초가 되는 핵심 논문이다. 다만 이름 기반 인구통계 추론과 관찰 연구 설계의 한계로 인과적 해석에는 신중함이 필요하다.
