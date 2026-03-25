# Unsupervised embedding of trajectories captures the latent structure of scientific migration

> **저자**: Dakota Murray, Jisung Yoon, Sadamori Kojaku, Rodrigo Costas, Woo-Sung Jung, Stasa Milojevic, Yong-Yeol Ahn | **날짜**: 2023-12-26 | **Journal**: Proceedings of the National Academy of Sciences | **DOI**: 10.1073/pnas.2305414120

---

## Essence

Word2vec(Skip-Gram Negative Sampling)가 이동의 gravity model과 수학적으로 동치임을 증명하고, 300만 명 과학자의 소속 이동 궤적에 적용하여 지리, 언어, 문화, 학술적 위신(prestige) 등 과학 이주의 다층적 구조를 단일 벡터 공간에 인코딩할 수 있음을 보여주었다. Embedding distance는 지리적 거리 대비 기관 간 이동 flux 설명력이 2배 이상(R2 = 0.48 vs. 0.22)이며, SemAxis로 추출한 prestige 축은 Times 대학 랭킹과 Spearman rho = 0.73의 강한 상관을 보인다.

## Motivation

- **알려진 것**: Gravity model은 이주 모델링의 표준 프레임워크이나, 지리적 거리만으로는 언어, 문화, 제도적 위신 등 다면적 요인을 포착하기 어려움
- **격차**: 기존 functional distance는 국가 수준의 저해상도이며 단일 요인에 초점을 맞추는 한계가 있고, 네트워크 표현은 단순 이원적(dyadic) 관계만 인코딩 가능
- **왜 중요한가**: 과학 이주는 혁신, 영향력, 협력, 지식 확산의 핵심 동인이나, 그 규모와 복잡성으로 인해 holistic한 이해가 제한적
- **접근법**: 자연어 처리의 word2vec를 이주 궤적에 적용하되, 이론적으로 gravity model과의 수학적 동치성을 증명하여 방법론의 정당성을 확보

## Achievement

1. **이론적 기여**: SGNS word2vec가 gravity model과 수학적으로 동치임을 증명 -- 위치 빈도가 mass, 벡터 내적이 거리 함수에 대응 (Eq. 16: T_ij = C*P(i)*P(j)*exp(v_j . v_i))
2. **예측 성능**: 과학 이주에서 embedding distance의 flux 설명력 R2 = 0.48 (지리적 거리 R2 = 0.22의 2배 이상), 미국 항공 R2 = 0.51, 한국 숙박 R2 = 0.57로 세 도메인 모두에서 일관된 우위
3. **다층적 구조 포착**: UMAP 투영으로 국가→지역→도시→기관 시스템→개별 기관 수준까지 다중 스케일에서 지리, 언어(스페인어권-포르투갈어권 분리), 문화(이슬람권 말레이시아-중동 근접), 제도적 관계를 시각화
4. **위신 위계 인코딩**: SemAxis로 추출한 prestige 축이 Times 랭킹과 rho = 0.73, Leiden 랭킹과 rho = 0.77 상관, 10개 국가 중 9개국에서 rho >= 0.5
5. **벡터 크기의 보편 패턴**: 기관 벡터의 L2 norm이 연구자 수 ~1,000 부근에서 오목(concave) 패턴을 보이며, 이는 미국, 중국, 호주, 브라질 등 다수 국가에서 공통적으로 관찰

## How

- **데이터**: Web of Science(2008-2019)에서 12,963,792명 저자의 소속 정보 추출, 이 중 3,007,192명(23.2%)의 이동 저자가 8,661개 기관에 걸쳐 17,700,095개 저자-소속 조합 생성. 추가로 미국 항공 여정 307M건(828개 공항), 한국 숙박 예약 1,038개 숙소
- **임베딩**: Gensim word2vec SGNS, d=300, w=1, gamma=1.0, k=5, f_min=50 (6,580개 기관). 같은 해 내 복수 소속은 매 training iteration마다 순서 무작위화
- **분석 기법**: (1) Gravity model 적합 비교(지리적 거리 power-law vs. embedding distance exponential), (2) UMAP 차원 축소로 다중 스케일 시각화, (3) 계층적 클러스터링 + element-centric clustering similarity로 지리/언어의 계층적 기여도 정량화, (4) SemAxis로 prestige 및 지리 축 추출
- **비교 기준**: SVD, Laplacian Eigenmap, Personalized PageRank, 직접 gravity model 최적화, Levy의 symmetric word2vec 등 다수의 baseline과 체계적 비교

## Originality

- Word2vec-gravity model 동치성의 수학적 증명은 neural embedding을 이주 연구에 적용하는 이론적 기반을 최초로 제공
- 단순 예측을 넘어 embedding 공간의 의미 구조(semantic topology)를 SemAxis, vector norm 분석 등으로 체계적으로 탐구하는 방법론적 프레임워크 제시
- 과학 이주, 항공 이동, 숙박 예약이라는 세 가지 상이한 도메인에서 일관된 결과를 보여 범용성 입증

## Limitation & Further Study

### 저자들이 언급한 한계
- Skip-gram 모델은 이주 흐름의 대칭성을 가정하나, 현실 이주는 비대칭적 (예: 개발도상국→선진국 방향성)
- 이산적 위치(기관, 공항) 간 이동에 최적화되어 있으며, GPS 좌표 기반 연속적 이동에는 적합하지 않음
- 학술 이주 데이터는 논문 출판 기반이므로 학회 참석, 단기 방문 등 short-term mobility를 포착하지 못함
- 전공 분야(specialty)를 무시하고 있어, 분야별 이주 패턴의 차이를 반영하지 못함
- 데이터가 2008-2019로 한정되어 COVID-19 이후 이주 패턴 변화를 반영하지 못함

### 리뷰어 판단 아쉬운 점
- Embedding dimension d=300이 과학 이주 도메인에서 과잉 차원일 가능성에 대한 논의가 부족. 6,580개 기관에 대해 300차원이 최적인지에 대한 체계적 분석이 필요
- 시간적 변화(temporal dynamics)를 포착하지 못함. 2008-2019를 단일 embedding으로 처리하여 이주 패턴의 시기별 변화를 무시
- Prestige 축 정의에 사용된 top/bottom 5개 대학의 선택이 자의적이며, seed 대학에 따른 결과 민감도가 충분히 탐구되지 않음

### 후속 연구
- 방향성 있는 embedding 모델(예: radiation model 기반)로 비대칭 이주 포착
- Diachronic embedding으로 시기별 이주 구조 변화 추적
- Persona2vec 등을 활용한 기관-전공 분야 pair 단위 embedding으로 분야별 이주 패턴 분석

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 5/5 |
| Technical Soundness | 5/5 |
| Significance | 5/5 |
| Clarity | 4/5 |
| Overall | 5/5 |

**총평**: Word2vec와 gravity model의 수학적 동치성 증명이라는 이론적 기여와, 다중 스케일에서 과학 이주의 지리-언어-문화-위신 구조를 체계적으로 밝혀낸 실증 분석이 결합된 탁월한 연구로, neural embedding을 이주 연구에 적용하는 이론적 기반과 방법론적 프레임워크를 확립한 기념비적 논문이다.
