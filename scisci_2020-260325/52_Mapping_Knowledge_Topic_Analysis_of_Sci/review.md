# Mapping Knowledge: Topic Analysis of Science Locates Researchers in Disciplinary Landscape

> **저자**: Radim Hladik, Yann Renisio | **날짜**: 2024-02-22 | **Journal**: (preprint, OSF) | **DOI**: 10.31235/osf.io/94jd5

---

## Essence

Topic modeling과 compositional data analysis(CoDa), 기하학적 데이터 분석(GDA)을 결합하여 개별 연구자를 학문 분야의 지식 공간 내에 배치하는 "인식론적 좌표계(epistemological coordinate system)"를 구축했다. 체코 공화국의 R&D 정보 시스템에서 수집한 1,039,577편의 논문(838,428편 텍스트 포함)과 118,560명의 저자 데이터를 사용하여, 과학 지식 공간의 주요 구조축이 Culture-Nature(분산의 25.1%), Life-Non-life(15.3%), Materials-Methods(7.7%)의 세 가지임을 밝혔다.

## Motivation

과학 지도 작성(science mapping)은 전통적으로 계량서지학(scientometrics)과 사회학이라는 두 전통으로 분리되어 있었다. 계량서지학은 인용·공저 네트워크 기반의 bottom-up 분류를, 사회학은 설문·인물 조사 기반의 사회적 차원 분석을 각각 강조했다. Pierre Bourdieu의 장(field) 이론이 제시한 "위치(positions)의 공간"과 "입장 표명(position-takings)의 공간" 간 상동성(homology)이라는 통합적 프레임워크가 있었지만, 이를 경험적으로 구현하는 방법론이 부재했다. 이 연구는 topic modeling의 확률적·관계적 속성이 Bourdieu 사회학과 이론적으로 양립 가능하다는 점에 착안하여, 텍스트 기반 지식 분류와 연구자 개인의 인식론적 위치를 동시에 파악하는 방법론을 제안한다.

## Achievement

1. **계층적 클러스터링과 FORD 분류의 정합성 확인**: Bottom-up topic model에서 도출한 분야 클러스터가 전문가 기반 FORD(Fields of Research and Development) 분류 체계의 중첩 구조와 대체로 일치하며, 2-클러스터 해에서 SSH/STEM 구분, 3-클러스터 해에서 생명/비생명과학 구분이 재현됨 (silhouette score 최고 0.31)
2. **세 가지 인식론적 축 발견**: PCA를 통해 Culture-Nature(25.1%), Life-Non-life(15.3%), Materials-Methods(7.7%) 축을 식별하고, 추가로 Synthesis-Analysis(6.1%), Applied-Fundamental(4.7%), Description-Prescription(3.6%) 축까지 해석
3. **개별 연구자의 인식론적 좌표 생성**: 112,835명 연구자의 topic portfolio를 PCA 공간에 투사하여 연속적 인식론적 좌표를 부여, Piaget의 인식론적 원과 Klavans & Boyack(2009) 합의 지도와 유사한 원형 패턴 관찰
4. **성별 편향의 인식론적 차원 규명**: 여성 연구자가 Life 축 방향에 집중 분포하며, 대부분 분야에서 성별 차이가 수학·공학·물리학 교차점을 향한 일관된 방향성을 보임
5. **보조 변수를 통한 검증**: 출판 형태(논문 비율), 성별, 공저자 수, 기관 유형(체코 과학아카데미, 병원, 예술학교), 연구비 출처 등이 인식론적 좌표와 체계적으로 연관됨을 확인

## How

- **데이터**: 체코 R&D Information System의 2000-2021년 출판 기록 1,039,577편, 838,428편의 제목·초록·키워드 텍스트, 118,560명 저자, 55,603건 연구비
- **Topic modeling**: TopSBM(hierarchical stochastic block model 기반) 알고리즘 사용, 하이퍼파라미터 없이 3,656개 토픽 도출, 256GB RAM 서버에서 실행
- **Compositional data transformation**: 분야별 topic portfolio에 centred log-ratio(clr) 변환 후 z-score 표준화
- **기하학적 분석**: Ward 방법 계층적 클러스터링, 분야-토픽 행렬의 전치 후 PCA 수행, 개별 연구자 topic portfolio를 PCA 공간에 barycenter로 투사
- **검증**: 백분위 기반 보조 변수 분포 분석, Genderize.io 기반 성별 추정(정확도 98%), silhouette 및 Dunn's index로 클러스터링 검증

## Originality

이 연구의 핵심 독창성은 topic modeling, compositional data analysis, geometric data analysis를 결합한 방법론적 프로토콜에 있다. 기존 science mapping이 분야 수준의 집합적 지도에 머물렀다면, 이 연구는 개별 연구자를 텍스트 내용에 기반한 연속적 인식론적 좌표 위에 배치하는 최초의 체계적 시도이다. 특히 topic model의 확률 분포를 compositional data로 재해석하여 clr 변환을 적용한 점, 그리고 분야를 "활성 변수"로 사용하여 언어적·사회적 효과로부터 지식의 자율적 구조를 분리한 이중 참조(double recourse) 전략은 방법론적으로 새롭다. Bourdieu의 position-takings 개념을 대규모 텍스트 데이터로 경험적으로 조작화(operationalize)한 점도 사회학적 기여가 크다.

## Limitation & Further Study

### 저자들이 언급한 한계

- Topic modeling의 확률적 초기화와 ground truth 부재로 인한 재현성 문제
- TopSBM이 단어를 단일 토픽에만 배정하여 동음이의어(homonymy) 처리 미흡
- 체코 단일 국가 데이터의 대표성 한계 — 세계 과학 전체로의 일반화에 제약
- 분야 내부의 세부 지식 조직 체계와 전체 좌표계의 관련성 추가 연구 필요
- 인용 데이터 미활용 — 출판물 가중치가 동일하여 영향력 반영 불가

### 리뷰어 판단 아쉬운 점

- **시간적 동태성 부재**: 20년간의 데이터를 정적 스냅샷으로 분석하여 연구자 개인의 궤적 변화나 분야 간 이동 패턴을 파악하지 못함
- **영어 텍스트만 사용**: 체코어 출판물은 언어 감지에서 제외되어 인문·사회과학의 상당 부분이 누락되었을 가능성
- **TopSBM의 확장성 문제**: 256GB RAM이 필요한 만큼 다른 국가나 더 큰 데이터셋에 적용하기 어려울 수 있음
- **학제 간 연구의 측정**: 잔여 범주(Other)가 학제 간 영역으로 해석되었으나, 이에 대한 정량적 학제 간 지표가 부족
- **인과 관계 미확립**: 보조 변수(성별, 기관 등)와 인식론적 좌표 간 연관성은 확인하였으나, 인과적 해석은 부재

### 후속 연구

- 시계열 분석을 통한 연구자의 인식론적 궤적 추적 및 분야 이동 동학 연구
- 다국가 비교 연구를 통한 인식론적 좌표계의 보편성 검증
- 인용 가중치를 결합한 확장 모델 개발
- LLM 기반 embedding과의 비교 연구로 topic model 접근법의 상대적 장점 검증
- 과학 이외의 문화 생산 영역(문학, 영화, 정치)에의 방법론 확장

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 4/5 |
| Technical Soundness | 4/5 |
| Significance | 4/5 |
| Clarity | 4/5 |
| Overall | 4/5 |

**총평**: Topic modeling과 compositional/geometric data analysis를 결합하여 개별 연구자를 인식론적 좌표 위에 배치하는 독창적이고 방법론적으로 정교한 연구이나, 체코 단일 국가 데이터와 정적 분석이라는 한계가 일반화 가능성을 제약한다.
