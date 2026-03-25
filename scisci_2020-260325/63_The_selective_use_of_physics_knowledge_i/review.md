# The selective use of physics knowledge in policy: how interdisciplinary physics bridges subfields and shapes policy influence

> **저자**: Jeongmin Lee, Jisung Yoon | **날짜**: 2026-02-11 | **Journal**: arXiv preprint | **DOI**: 10.48550/arXiv.2602.10427

---

## Essence

물리학 지식이 정책 문서에 선택적으로 활용되는 메커니즘을 실증 분석한 결과, 정책 문서는 물리학의 연구 생산 구조를 그대로 반영하지 않고 학제간(interdisciplinary) 분야를 불균형적으로 선호한다. Category 8(Interdisciplinary Physics)은 학술 생산의 5.5%에 불과하지만 정책 인용의 19.8%를 차지한다. 그러나 정책 가시성(visibility)과 정책 영향력(influence)은 분리되며, 지구물리학(Category 9) 인용 시 정책 영향력이 약 24% 증가하는 반면, 학제간 물리학은 영향력에 유의한 효과가 없다.

## Motivation

- **알려진 것**: 과학 지식이 정책 수립에 점점 더 중요해지고 있으며, 근거 기반 정책(evidence-based policy)에 대한 요구가 증가. 과학과 정책 사이에는 구조적 괴리가 존재(two-communities theory).
- **부족한 것**: 과학 지식이 정책에 선택적으로 활용되는 메커니즘, 특히 어떤 형태의 지식이 선호되고 어떤 인용이 실제 영향력으로 이어지는지에 대한 체계적 실증 연구가 부족.
- **왜 물리학인가**: 물리학은 의학이나 경제학과 달리 정책과 구조적으로 거리가 먼 분야이므로, 과학-정책 간극을 연결하는 bridging mechanism을 분리하여 관찰할 수 있는 전략적 test case.
- **접근 방식**: Overton 정책 문서 데이터베이스와 American Physical Society(APS) 출판 데이터를 DOI로 연결한 novel dataset 구축, PACS 분류 체계 활용.

## Achievement

1. **정책 수요와 학술 공급의 구조적 불일치**: Category 7(Condensed Matter: Electronic)이 학술 생산의 29.3%를 차지하지만 정책에서는 미미. 반면 Category 8(Interdisciplinary Physics)은 5.5% → 19.8%로 정책에서 3.6배 과대 대표
2. **기관별 이질성**: Think tank은 학제간 물리학을 선호하고, 정부 기관은 규제 관련 분야를, IGO는 Global Security 관련 분야를 집중 인용
3. **학제간 분야의 브로커 역할**: Co-citation 네트워크에서 학제간 물리학(PACS 05, 89 등)이 hub-and-spoke 구조의 중심에 위치하며 전문 분야를 연결하는 integrative backbone 역할
4. **가시성과 영향력의 분리**: Category 8은 정책 진입을 촉진(visibility: beta=0.04, p=0.002)하지만 하류 영향력에는 유의하지 않음(influence: beta=-0.03, p=0.50). Category 9는 visibility(beta=0.07)와 influence(beta=0.21, ~24% 증가) 모두에서 유의
5. **Two-stage model 제안**: 학제간 프레이밍이 정책 담론 진입을 촉진하고, 지속적 영향력은 광범위하게 공유되는 evidence infrastructure(예: IPCC 보고서) 통합에 의존

## How

- **데이터**: APS 출판물(1978-2015, N=435,253)과 Overton 정책 문서 데이터베이스에서 757개 정책 문서-1,156개 물리학 논문 연결
- **분류**: PACS(Physics and Astronomy Classification Scheme) 1차 분류(10개 카테고리) 활용
- **방법론**: (1) Fractional weighting으로 정책 수요 vs 학술 공급 분포 비교, (2) LDA topic modeling으로 6개 정책 주제 식별, (3) Disparity filter(alpha=0.1)로 co-citation 네트워크 backbone 추출, (4) Louvain algorithm으로 커뮤니티 탐지(Q=0.46, 5개 커뮤니티), (5) OLS 회귀분석으로 visibility와 influence 결정 요인 분석

## Originality

- Science-policy interface를 visibility와 influence로 명시적으로 분리하여 분석한 프레임워크가 참신
- 물리학이라는 정책과 구조적으로 거리가 먼 분야를 선택하여 bridging mechanism을 isolate한 연구 설계
- Overton-APS 연결 데이터셋 구축을 통한 정밀한 하위 분야 수준 분석
- 학제간 연구가 "gateway"이지만 "influencer"는 아니라는 역설적 발견

## Limitation & Further Study

### 저자들이 언급한 한계
- Overton 데이터베이스의 명시적 인용만 포착하여, agenda setting이나 자문 등 비공식적 영향 경로를 놓침
- PACS 코드가 2016년까지만 가용하여 시간적/개념적 해상도 제한
- 물리학에 한정된 분석으로 다른 학문 분야로의 일반화 제한
- 인용을 영향력의 proxy로 사용하는 것의 타당성 한계

### 리뷰어 판단 아쉬운 점
- 757개 정책 문서-1,156개 논문이라는 상대적으로 작은 표본 크기로 인한 통계적 검정력 우려
- 시간적 동학(temporal dynamics) 분석 부재 -- 물리학 지식의 정책 유입이 시기별로 어떻게 변화했는지 미탐구
- Category 9의 높은 영향력이 IPCC 보고서 소수에 의해 구동되는 것으로 보이며, 이는 일반적 메커니즘보다 특수한 사례에 가까울 수 있음
- 인과적 해석보다는 상관관계에 머무르는 한계

### 후속 연구
- 생명과학, 컴퓨터과학 등 다른 학문 분야로 프레임워크 확장 비교 연구
- 시계열 분석을 통한 과학-정책 연결의 동태적 변화 추적
- 정책 문서의 실제 정책 결과(policy outcome)까지 추적하는 연구
- 학제간 연구의 정책 영향력을 높이기 위한 중개 메커니즘(예: synthesis report) 심층 분석

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 4/5 |
| Technical Soundness | 4/5 |
| Significance | 4/5 |
| Clarity | 4/5 |
| Overall | 4/5 |

**총평**: 과학 지식의 정책 활용에서 가시성과 영향력의 분리를 실증한 참신한 연구로, 학제간 물리학이 정책 진입의 gateway이지만 영향력의 driver는 아니라는 역설적 발견이 Science of Science와 science policy 분야에 중요한 시사점을 제공한다.
