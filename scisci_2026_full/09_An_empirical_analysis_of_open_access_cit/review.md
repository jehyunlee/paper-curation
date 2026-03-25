# An Empirical Analysis of Open Access Citation Advantages in Library and Information Science

> **저자**: Sunwoo Lee, Wonsik Shim | **날짜**: 2026 | **DOI**: https://doi.org/10.47989/ir31iConf64133

---

## 핵심 요약
본 연구는 Web of Science에서 수집한 109,759편의 문헌정보학(LIS) 분야 학술 논문(2001-2024)을 분석하여, OA(Open Access) 논문의 인용 우위(citation advantage)가 LIS 분야에서는 조건부적(conditional)임을 밝혔다. 전체적으로 Non-OA 논문이 OA 논문보다 약간 더 높은 평균 인용(18.83 vs. 17.90)을 받았으나 효과 크기는 극히 미미하며, OA 유형별로는 Green OA가 가장 높은 인용(28.55)을 보였고, OA 인용 우위는 시간이 지남에 따라 크게 감소하고 있다.

## 연구 배경 및 동기
OA의 인용 우위(citation advantage)는 Eysenbach(2006) 이래 학술 커뮤니케이션의 핵심 논제였으나, 최근 연구들은 이 우위가 분야, 방법론, OA 유형에 따라 크게 달라짐을 보고하고 있다. 의학 및 생명과학 분야에서는 상대적으로 긍정적 결과가 보고되었으나, LIS 분야에서의 OA 인용 효과에 대한 실증 연구는 매우 부족했다. Khan et al.(2023)은 LIS 분야에서 Non-OA 저널이 더 높은 인용 영향력을 가진다고 보고하여, 분야별 심층 분석의 필요성이 제기되었다.

## 방법론
- **데이터**: WoS Core Collection에서 Information Science & Library Science 분야, 2001-2024년 학술지 논문(document type='J') 수집. 초기 426,090건에서 JCR quartile 매핑, Library Journal 제외, 인용 이상치 제거를 거쳐 최종 109,759건 분석.
- **변수**: 독립변수 -- OA 상태(이진), OA 유형(Gold, Green, Hybrid, Bronze), 출판연도, WoS 분류(단일/다학제), JIF quartile. 종속변수 -- WoS Core 피인용 횟수.
- **분석 방법**: Shapiro-Wilk 정규성 검정, Levene 등분산 검정, Welch t-test, Mann-Whitney U test, one-way ANOVA, Kruskal-Wallis test, Tukey HSD 사후검정, Cohen's d 효과크기 산출, 시계열 분석(5년 구간).

## 주요 결과
- **OA vs. Non-OA 전체**: Non-OA(평균 18.83) > OA(평균 17.90), 통계적으로 유의하나 Cohen's d = -0.024로 실질적 의미 없음.
- **OA 유형별**: Green OA(28.55) >> Bronze(15.00) > Hybrid(8.47) > Gold(5.35). 모든 쌍별 비교에서 유의한 차이(Tukey HSD, p < .001).
- **학제간 범위**: 다학제(multi-subject) 논문에서 OA가 인용 우위(28.49 vs. 26.47), 단일 학제에서는 Non-OA가 우위(10.06 vs. 9.31).
- **시간적 추이**: OA 인용 우위가 2001-2004년 9.75건에서 2020-2024년 0.74건으로 13배 감소. Cohen's d도 0.196에서 0.029-0.039으로 하락.
- **저널 품질별**: Q1, Q2 저널에서는 Non-OA가 유의하게 더 높은 인용, Q3, Q4에서는 OA가 미미하게 높으나 통계적 비유의.

## 독창성 및 기여
- LIS 분야에 특화된 OA 인용 효과의 **포괄적 실증 분석**으로, OA 유형, 학제간 범위, 시간적 추이, 저널 품질을 다차원적으로 검토.
- OA 인용 우위가 **조건부적이며 감소 추세**에 있음을 보여, 다른 분야의 결과를 LIS에 일반화하는 것에 대한 경고 제공.
- Green OA의 지속적 인용 우위를 확인하여, 자가 아카이빙(self-archiving)의 가치를 재확인.
- Simpson's paradox 유사 현상(5년 구간별로는 OA 우위이나 전체 합산에서는 Non-OA 우위)을 해체하여 설명.

## 한계 및 향후 연구
- **저자 언급 한계**: WoS 기반 OA 분류의 한계, LIS 분야의 MIS/정보시스템 저널 포함에 따른 해석 주의 필요.
- **추가 지적**: (1) 인용 횟수만을 종속변수로 사용하여 altmetrics, 다운로드 등 대안적 영향력 지표 미포함. (2) Self-selection bias -- 높은 품질의 논문이 Green OA로 아카이빙될 가능성을 통제하지 않음. (3) 인용 축적 시간(citation window)이 최근 출판물에 불리하게 작용하는 문제를 5년 구간 분석으로 부분적으로만 해결. (4) 개별 논문 수준의 인용 영향 요인(저자 명성, 연구 주제 인기도 등)에 대한 다변량 통제 미실시. (5) WoS의 OA 유형 분류 정확도에 대한 검증 없이 그대로 사용.

## 평가
| 항목 | 점수 (1-5) |
|------|-----------|
| Novelty | 3 |
| Technical Soundness | 3 |
| Significance | 3 |
| Clarity | 4 |
| Overall | 3 |

**총평**: LIS 분야의 OA 인용 효과를 다각도로 분석한 유용한 기여이나, self-selection bias 등 핵심 교란변수의 미통제와 비교적 단순한 통계 분석(회귀 모델 없이 t-test/ANOVA 중심)으로 인해 분석적 깊이가 제한적이다.
