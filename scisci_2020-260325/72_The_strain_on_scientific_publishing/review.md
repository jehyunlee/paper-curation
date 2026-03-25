# The strain on scientific publishing

> **저자**: Mark A. Hanson, Pablo Gómez Barreiro, Paolo Crosetto, Dan Brockington | **날짜**: 2024-11-01 | **Journal**: Quantitative Science Studies | **DOI**: 10.1162/qss_a_00327

---

## Essence

학술 출판물의 기하급수적 증가가 과학 인프라에 가하는 "strain"을 5개 데이터 기반 메트릭으로 정량화했다. 2022년 Scopus/WoS 색인 논문은 약 282만 편으로 2016년 대비 47% 증가했으나 연구자 수는 이에 비례하여 증가하지 않았다. 이 성장의 70% 이상이 5개 출판사(MDPI 27%, Elsevier 16%, Frontiers 11%, Springer 9.5%, Wiley 7%)에서 발생했으며, MDPI는 모든 메트릭에서 이상치였다: 논문 증가율 +1,080%, special issue 비율 88%, turnaround time 37일, 거절률 감소, 가장 높은 "impact inflation"(5.4).

## Motivation

학술 논문의 지수적 성장이 피어리뷰어 모집 난항, 과학자의 정보 과부하, paper mill 스캔들 등과 맞물려 과학 출판 시스템의 지속가능성을 위협하고 있다. "Publish or perish" 문화, gold open access APC 모델, 출판사의 수익 동기 등이 복합적으로 작용하지만, 어떤 출판사와 어떤 행동이 이 strain에 가장 크게 기여하는지는 체계적으로 분석되지 않았다. 기존 연구들이 개별 출판사나 단일 메트릭에 초점을 맞춘 반면, 다중 메트릭을 결합한 비교 분석이 필요했다.

## Achievement

1. **논문 성장 메커니즘의 이원화**: 전통 출판사(Elsevier, Springer)는 저널 수 증가 + 저널당 소폭 증가로, 신생 OA 출판사(MDPI, Frontiers, Hindawi)는 소수 저널의 폭발적 논문 증가로 성장. 두 메커니즘의 strain 기여도는 비슷
2. **Special issue의 역할 규명**: MDPI(88%), Frontiers(69%), Hindawi(62%)는 special issue를 주요 출판 경로로 활용. Special issue 논문은 일반 논문 대비 turnaround time이 짧고 거절률이 낮으며 시간 분산도 작음 -- 처음으로 체계적으로 문서화
3. **Turnaround time의 동질화**: MDPI의 평균 37일(2022)은 다른 출판사(130-198일)와 현격한 차이. 더 중요하게, turnaround time 분포가 좌편향으로 변하며 점점 동질화 -- 논문의 고유한 필요에 맞춘 심사가 이루어지지 않음을 시사
4. **"Impact inflation" 신규 메트릭 제안**: IF/SJR 비율로 자기인용·인용 카르텔에 의한 IF 팽창 탐지. MDPI와 Hindawi가 유의하게 높은 impact inflation. MDPI 저널의 자기인용률(9.5%)도 다른 출판사 대비 유의하게 높음
5. **비즈니스 모델과 strain의 관계**: Gold OA 자체가 strain의 원인이 아님(PLOS, BMC는 정상적 메트릭). 특정 출판사의 특정 행동(special issue 남용, 낮은 거절률, 짧은 turnaround)이 핵심

## How

- **데이터**: Scopus/Scimago(WoS 동시 색인 저널만), Clarivate IF 데이터(16,174 저널), 10개 출판사 웹스크래핑(500만+ 논문의 turnaround time), OECD PhD 통계, UNESCO 연구자 통계
- **메트릭**: (1) 총 논문 수 및 출판사별 분해, (2) Special issue 논문 비율, (3) Turnaround time(투고→승인) 분포 및 추이, (4) 거절률 추이, (5) Impact inflation(Cites-per-doc/SJR 또는 IF/SJR)
- **분석**: 출판사별 시계열 비교, ANOVA + Tukey HSD(impact inflation, 자기인용률), 상관분석(거절률 vs special issue 비율, 거절률 vs 저널 크기 등)
- **개념 프레임워크**: "Love triangle" -- 출판사(수익), 연구비 기관(품질 신호), 연구자(publish or perish)의 상호작용

## Originality

- **5개 메트릭의 통합 비교**: 개별 메트릭이 아닌 다중 메트릭을 결합하여 출판사별 프로파일을 체계적으로 비교한 최초의 연구
- **"Impact inflation" 신규 지표**: 공개 데이터만으로 인용 행동의 왜곡을 탐지하는 실용적 도구(IF/SJR ratio) 제안
- **Special issue 논문의 차별적 처리를 최초로 문서화**: 더 낮은 거절률, 더 짧고 동질적인 turnaround time
- Strain이 OA 모델 자체가 아닌 특정 출판사의 행동에 기인함을 실증 -- 정책 대응의 정밀 타겟팅 근거 제공

## Limitation & Further Study

### 저자들이 언급한 한계
- 웹스크래핑 기술적 한계로 Elsevier의 special issue 데이터 미포함, 일부 출판사의 거절률 데이터 미확보
- 거절률 산출 방법이 출판사마다 달라 직접 비교에 주의 필요(추세 비교는 가능)
- Scopus/WoS 동시 색인 저널만 분석 → 실제 strain 과소추정
- 저작권 문제로 웹스크래핑 데이터 공개 불가(R Shiny app으로 대체)
- 논문 품질 자체를 직접 측정하지 못함(turnaround time, 거절률은 간접 지표)

### 리뷰어 판단 아쉬운 점
- 인과 추론이 부재 — 상관관계만 보여줌. 예: special issue 확대가 turnaround time 감소를 "야기"하는지, 동시에 발생하는지 구분 불가
- Global South의 논문 증가와 strain 사이의 관계를 충분히 구분하지 못함. 포용적 성장 vs 품질 저하의 경계가 불명확
- Preprint 서버(arXiv, bioRxiv 등)의 역할이 논의되지 않음 — 전통 출판과의 상호작용이 strain에 미치는 영향
- LLM의 등장(2023~)이 향후 논문 생산 속도에 미칠 영향에 대한 전망이 없음(2022년까지 데이터)

### 후속 연구
- 논문 품질의 직접 측정(재현성, 철회율 등)과 출판 성장의 관계 분석
- LLM 시대의 논문 생산 가속이 strain에 미치는 영향 추적
- Special issue의 피어리뷰 질 직접 평가(심사 보고서 분석 등)
- Impact inflation 메트릭의 분야별 검증 및 표준화
- 연구비 기관의 정책 변화(narrative CV 도입 등)가 publish or perish 압력에 미치는 효과 평가

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 4/5 |
| Technical Soundness | 4/5 |
| Significance | 5/5 |
| Clarity | 5/5 |
| Overall | 4/5 |

**총평**: 학술 출판의 지속가능성 위기를 다중 메트릭으로 체계적으로 진단한 시의적절하고 영향력 있는 연구로, "impact inflation" 신규 지표와 special issue의 차별적 처리 문서화가 특히 가치 있으며, 출판사-연구자-연구비 기관 삼각관계의 개념 프레임워크가 정책 논의의 토대를 제공한다.
