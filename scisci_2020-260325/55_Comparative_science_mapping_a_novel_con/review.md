# Comparative science mapping: a novel conceptual structure analysis with metadata

> **저자**: Massimo Aria, Corrado Cuccurullo, Luca D'Aniello, Michelangelo Misuraca, Maria Spano | **날짜**: 11/2024 | **Journal**: Scientometrics | **DOI**: 10.1007/s11192-024-05161-6

---

## Essence

기존 co-word analysis 기반 strategic diagram을 메타데이터(저자, 기관, 지역 등)로 세분화하여 복수 관찰 단위의 conceptual structure를 하나의 joint representation에서 비교할 수 있는 "comparative science mapping" 기법을 제안한다. 이탈리아 9개 공공 종양학 IRCCS(연구-입원-의료기관)의 2000-2019년 WoS 논문 45,320편 중 상위 25% NCS 5,686편을 분석하여, 3개 시기별 기관별 연구 주제의 centrality-density 위치를 joint strategic diagram으로 시각화했다. 그 결과 expression, survival, chemotherapy가 공통 주요 주제이며, 시간에 따라 기초 종양생물학에서 환자 중심 연구(survival, quality-of-life)로 전환되는 패턴을 기관별로 비교 가능하게 보여주었다.

## Motivation

- **기존 지식**: Co-word analysis(Callon et al., 1983)와 strategic diagram은 과학 분야의 conceptual structure를 motor/basic/niche/peripheral theme으로 분류하는 확립된 방법론이다. bibliometrix R 패키지가 이를 구현한다.
- **한계/격차**: (1) 기존 co-word analysis는 텍스트만 분석하고 메타데이터(기관, 국가 등)를 무시하여 "누가" 해당 주제를 연구하는지 알 수 없음, (2) Rafols et al.(2010)의 overlay map은 텍스트 내용을 사용하지 않음, (3) 복수 기관의 conceptual structure를 단일 시각화에서 비교할 방법이 없었음.
- **접근**: 메타데이터 변수 X로 문서-용어 행렬 F를 M개 하위 행렬 F_m으로 분할 → 각 하위 행렬에서 co-occurrence matrix A_m → association strength → Louvain community detection → Callon centrality/density 계산 → M개 strategic diagram을 표준화 후 joint plot으로 통합.

## Achievement

1. **메타데이터 기반 세분화 전략의 수학적 공식화**: 문서x용어 행렬 F에 메타데이터 변수 X를 적용하여 X^T F로 그룹별 행렬 생성 또는 F를 M개 하위 행렬로 분할하는 두 가지 경로를 공식화
2. **Joint strategic diagram**: M개 기관의 conceptual structure를 centrality-density 표준화 + reverse rank 변환으로 단일 플롯에 통합, 기관간 비교를 시각적으로 가능하게 함
3. **이탈리아 종양학 연구의 20년 진화 추적**: 3개 시기(2000-06, 2007-13, 2014-19)에 걸쳐 기초 연구(expression, carcinoma) → 번역 연구(stem-cell transplantation) → 환자 중심 연구(survival, quality-of-life)로의 전환을 기관별로 시각화
4. **정책 지원 도구로서의 활용 가능성 제시**: AMC의 triple mission(교육-연구-진료) 맥락에서 연구 전략 수립, 펀딩 배분, 기관간 협력 식별을 위한 의사결정 지원 도구로 위치 설정
5. **오픈소스 구현**: bibliometrix R 패키지(Aria & Cuccurullo, 2017) 기반으로 재현 가능

## How

- **데이터**: WoS에서 9개 이탈리아 공공 IRCCS의 2000-2019년 영문 논문 45,320편 → 종양학 분야 필터링 22,630편 → NCS 상위 25% 5,686편
- **방법**:
  - 텍스트 전처리 → 문서x용어 행렬 F (binary) → 기관 메타데이터로 분할 → 기관별 co-occurrence matrix A_m = F_m^T F_m
  - Association strength로 정규화 (AS = a_jj' / a_jj * a_j'j')
  - Louvain algorithm으로 community detection → 각 community의 Callon centrality(외부 연결 강도)와 Callon density(내부 응집도) 계산
  - 기관별 centrality/density를 표준화 후 reverse rank 변환 → joint strategic diagram으로 통합 시각화
  - 3개 시기(2000-06, 2007-13, 2014-19)에 대해 반복

## Originality

- 기존 strategic diagram의 개념적 틀(Callon centrality/density, 4사분면 분류)을 유지하면서 **메타데이터 세분화**와 **joint representation**이라는 두 가지 확장을 수학적으로 공식화한 점이 독창적
- 단일 분야 내 복수 기관의 연구 포지셔닝을 하나의 시각화에서 비교할 수 있는 최초의 체계적 방법론
- 종양학이라는 실질적으로 중요한 분야에서 정책적 활용 가능성을 구체적으로 시연

## Limitation & Further Study

### 저자들이 언급한 한계
- Bag-of-words 기반이므로 키워드와 초록 분석 시 결과가 상이할 수 있으며, 문맥 정보 포착에 한계
- Louvain algorithm의 resolution limit으로 소규모 커뮤니티 탐지 실패 가능성
- 시간 차원을 별도 time slice로 분리 처리하여 동적 커뮤니티 탐지(dynamic community detection)를 수행하지 못함
- NCS 상위 25%만 선정하여 개척적(pioneering) 연구를 놓칠 가능성
- 임상적 성과(clinical success)를 평가할 수 없음

### 리뷰어 판단 아쉬운 점
- **Joint strategic diagram의 가독성 한계**: 9개 기관 x 다수 토픽이 하나의 플롯에 표시되어 Figure 8-10이 매우 복잡하고 해석이 어려움. 정보 과부하 문제를 해결하기 위한 인터랙티브 시각화 등의 논의가 부족
- **검증 부재**: 제안된 comparative mapping 결과가 도메인 전문가(종양학자)의 판단과 일치하는지에 대한 체계적 검증이 없음
- **이탈리아 종양학 단일 사례**: 방법론의 일반화 가능성을 보여주기 위해 다른 분야나 국가에 대한 추가 사례가 필요
- **Embedding 기반 접근과의 비교 부재**: 저자들 스스로 embedding의 가능성을 언급하면서도 실제 비교 실험은 수행하지 않음

### 후속 연구
- Leiden algorithm 등 대안적 community detection 방법과의 비교
- Dynamic community detection으로 시계열 분석 개선
- Embedding 기반 용어 표현(Word2Vec, BERT)과의 결합
- 인터랙티브 웹 기반 시각화 도구 개발로 joint diagram의 가독성 향상

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 4/5 |
| Technical Soundness | 4/5 |
| Significance | 3/5 |
| Clarity | 3/5 |
| Overall | 4/5 |

**총평**: Co-word analysis에 메타데이터 세분화를 결합한 comparative science mapping은 방법론적으로 견실하고 정책적 활용 가치가 높은 독창적 기여이나, joint strategic diagram의 시각적 복잡성과 단일 사례 의존이 일반화 가능성에 제약을 준다.
