---
title: "AI for Science 지형도 — 발표 슬라이드 원고 58장"
topic: ai4s
slides: 58
corpus_papers: 2709
evidence_since: 2025
generated: 2026-10-21
tags:
  - ai4science
  - 슬라이드
  - 연구동향
  - ai4s
---

# AI for Science 지형도 — 슬라이드 원고 58장

> [!info] 개요
> 코퍼스 **2,709편** · 대분류 **10개** · 서브카테고리 **95개** 중 편수 상위 **5개씩**.
> 슬라이드 1장 = 서브카테고리 1개(`S06`–`S53`). 사례는 **2025년 이후 우선**(코퍼스의 83%).
> 레퍼런스 링크는 각 논문의 리뷰 문서(`../../docs/papers/<slug>/index.html`)로 연결된다.

## 목차

- **오프닝**
    - `S01` AI for Science, 2026년 지형도
    - `S02` 이 지도는 어떻게 만들어졌나
    - `S03` 코퍼스 한눈에 보기
    - `S04` 10개 대분류 지형도
    - `S05` AI4S 서사: 예측에서 생성, 그리고 검증으로
- **제1부 · 생체분자 생성 모델링**
    - `S06` 단일세포 발현 모델링 — 121편
    - `S07` 단백질 언어모델 상호작용 — 53편
    - `S08` 이산 확산 분자 생성 — 43편
    - `S09` 역합성 반응 예측 — 41편
    - `S10` 유전체 파운데이션 모델 — 40편
- **제2부 · 자율 AI 과학 발견**
    - `S11` 자율 AI 과학자 에이전트 — 70편
    - `S12` 자율 과학 발견 시스템 — 46편
    - `S13` 에이전틱 신약 발굴 — 36편
    - `S14` 자율 실험실·공동 과학자 — 35편
    - `S15` 단백질 공학 에이전트 — 34편
- **제3부 · 형식 수학 정리 증명**
    - `S16` 검증 가능 보상 RL — 47편
    - `S17` LLM 형식 정리 증명 — 36편
    - `S18` 정리 자동 형식화 — 35편
    - `S19` AI 공동 수학자 — 26편
    - `S20` 증명 검증의 아첨 — 26편
- **제4부 · LLM 추론·에이전트 벤치마크**
    - `S21` 다단계 연쇄 추론 — 54편
    - `S22` 에이전트 기억·계획 — 39편
    - `S23` 임상 추론 에이전트 — 33편
    - `S24` 표·데이터 추론 — 30편
    - `S25` 주장 검증 — 29편
- **제5부 · 물리 기반 신경 시뮬레이션**
    - `S26` 물리 기반 신경 연산자 — 66편
    - `S27` 동역학계 flow matching — 46편
    - `S28` 확산 기반 자료동화 — 33편
    - `S29` 수치 기상 예보 — 31편
    - `S30` 로봇 조작·제어 — 27편
- **제6부 · 의료·신경 신호 모델링**
    - `S31` EHR 파운데이션 모델 — 56편
    - `S32` 뇌-시각 표상 정렬 — 33편
    - `S33` 의료영상 분할 — 32편
    - `S34` 멀티모달 의료영상 진단 — 27편
    - `S35` 생체신호 파운데이션 모델 — 27편
- **제7부 · 과학 문헌·동료심사**
    - `S36` 동료심사 피드백 데이터셋 — 61편
    - `S37` 과학 문헌 검색·QA — 32편
    - `S38` 신규성 기반 아이디어 — 30편
    - `S39` 자동 문헌 리뷰 생성 — 25편
    - `S40` 다문서·메타리뷰 요약 — 24편
- **제8부 · 멀티모달 인식·효율화**
    - `S41` 다국어 LLM 양자화·효율화 — 46편
    - `S42` 과학 도표 캡셔닝 — 24편
    - `S43` AutoML 도메인 전이 — 16편
    - `S44` 차트 추론·팩트체크 — 14편
    - `S45` 도시 장면 이해 — 13편
- **제9부 · 인과·통계 추론**
    - `S46` 인과 독립성 검정 — 53편
    - `S47` 관찰 데이터 처치 정책 — 23편
    - `S48` 통계 검정·리더보드 — 16편
    - `S49` 중도절단 생존분석 — 16편
- **제10부 · 계산 재료 시뮬레이션**
    - `S50` 기계학습 원자간 포텐셜 — 37편
    - `S51` 생성형 무기 재료 설계 — 33편
    - `S52` 고온 합금 포텐셜 — 19편
    - `S53` 양자 다체 시뮬레이션 — 18편
- **종합**
    - `S54` 수렴 신호: 경계가 무너지는 곳
    - `S55` 부상과 쇠퇴
    - `S56` 비어 있는 자리
    - `S57` 검증 전환의 여섯 축
    - `S58` 그래서 무엇을 할 것인가

---

## S01 · AI for Science, 2026년 지형도

*오프닝* · **2,709편 코퍼스가 말하는 10개 지형과 48개 최전선** · *표지*

> [!abstract] 핵심 메시지
> 생성 경쟁은 끝났고, 2026년 AI4S의 승부는 검증으로 옮겨갔다. 2,709편이 그 전환을 증언한다.

- 대상 코퍼스: **ai4s** 토픽 2,709편(리뷰 완료 전수). 사례는 **2025년 이후를 우선**해 골랐다.
- 구조: 대분류 10개 · 서브카테고리 95개 → 편수 상위 최대 5개씩 총 48장.
- 연도 분포: 2023년 115편 → 2024년 274편 → 2025년 391편 → 2026년 1,852편. 전체의 **83%가 2025년 이후** 논문이다.
- 슬라이드 1장 = 서브카테고리 1개. 규모·기간·상태·대표 도구·대표 논문·시사점을 한 화면에.
- 각 슬라이드 하단 레퍼런스는 코퍼스의 **논문별 리뷰 문서로 바로 연결**된다.

> [!tip] 우리에게 무엇인가
> 2,709편의 83%가 2025년 이후 논문이다. 이 덱은 국내 연구기관·기업이 생성 능력이 아니라 검증 인프라에 투자해야 하는 이유를 코퍼스 증거로 보인다.

---

## S02 · 이 지도는 어떻게 만들어졌나

*오프닝* · **Method — SPECTER2 · UMAP · HDBSCAN · c-TF-IDF** · *방법*

> [!abstract] 핵심 메시지
> 지도는 의미 유사도로 그렸다. 편수는 크기일 뿐 중요도가 아니며, 최신 쏠림이 있다.

- 임베딩: SPECTER2(논문 특화)로 전 논문을 벡터화 → UMAP 5차원 축소 → HDBSCAN 밀도 클러스터링.
- 미세 클러스터를 c-TF-IDF로 키워드화하고 LLM이 명명 → 서브카테고리 95개 → 대분류 10개로 그룹핑.
- 각 논문은 primary_category 1개 + all_categories 최대 3개를 가진다(다중 배정).
- 편수는 두 기준으로 센다 — **고유 배정**(primary 1편=1칸, 10개 합 2,709편)과 **중복 포함**(all_categories, 10개 합 8,127편). 웹 인덱스의 카테고리 헤더 편수는 중복 포함 기준이고, 이 덱의 커버리지 산술은 고유 배정 기준이다.
- 시기(start–end)·상태(가속/안정/부상/감소)·대표 도구는 카테고리별 타임라인 분석에서 가져왔다.
- 한계 1: 편수≠중요도. 작은 칸이 큰 칸의 신뢰를 떠받친다 — S48, S20, S18 는 규모보다 감사 기능으로 읽어야 한다.
- 한계 2: 최신 편향. 코퍼스의 83%가 2025년 이후라 고전의 위치와 장기 영향은 과소 반영되고, 최근 주장은 아직 독립 재현을 거치지 않았다.

> [!tip] 우리에게 무엇인가
> 편수가 적은 칸이 결정적일 수 있다. S48 같은 칸은 규모는 작아도 다른 대분류의 결과를 인증하는 층이다.

---

## S03 · 코퍼스 한눈에 보기

*오프닝* · **Corpus at a glance** · *코퍼스*

> [!abstract] 핵심 메시지
> 2,709편 중 1,852편이 2026년 논문이다. 이 분야는 2025년을 전후로 폭발했다.

| 연도 | 편수 |  |
|---|---|---|
| 2018 | 7편 | █ |
| 2019 | 10편 | █ |
| 2020 | 11편 | █ |
| 2021 | 18편 | █ |
| 2022 | 17편 | █ |
| 2023 | 115편 | ██ |
| 2024 | 274편 | ████ |
| 2025 | 391편 | ██████ |
| 2026 | 1,852편 | ██████████████████████████████ |

- 2023년 이후 급증 — 2023년 115편 → 2024년 274편 → 2025년 391편 → 2026년 1,852편.
- 2025년 이후 논문이 전체의 83%. 이 덱이 2025+ 사례 중심인 이유다.
- 고전의 위치: 물리정보 신경망, AlphaFold, 초기 형식 증명 연구는 소수만 남아 뼈대 역할을 하고, 본문의 대부분은 그 위에서 쓴 최근 작업이다.
- 피인용 데이터의 한계: 2026년 논문은 인용이 쌓일 시간이 없어 영향력을 인용으로 줄 세울 수 없다. 이 덱은 인용 대신 헤드라인과 반증 신호로 읽는다.

> [!tip] 우리에게 무엇인가
> 최근 논문이 83%다. 정립된 정설이 아니라 움직이는 표적을 보고 있으며, 그만큼 국내 진입 창구도 아직 열려 있다.

---

## S04 · 10개 대분류 지형도

*오프닝* · **The 10 territories** · *지형도*

> [!abstract] 핵심 메시지
> 10개 대분류가 코퍼스를 나눈다. 상위 몇 곳이 대부분을 차지하고, 작은 칸이 검증을 맡는다.

| 대분류 | 고유 배정 | 중복 포함 | 서브카테고리 | 최대 서브카테고리 |
|---|---|---|---|---|
| 생체분자 생성 모델링 | 625 | 1,252 | 20 | Single-Cell Gene Expression Modeling |
| 자율 AI 과학 발견 | 447 | 1,694 | 16 | Autonomous AI Scientist Agents |
| 형식 수학 정리 증명 | 330 | 883 | 13 | Verifiable RL for Reasoning |
| LLM 추론·에이전트 벤치마크 | 284 | 1,088 | 10 | Multi-Hop Chain-of-Thought Reasoning |
| 물리 기반 신경 시뮬레이션 | 272 | 572 | 9 | Physics-Informed Neural Operators |
| 의료·신경 신호 모델링 | 213 | 592 | 7 | EHR Foundation Models |
| 과학 문헌·동료심사 | 210 | 463 | 7 | Peer Review Feedback Datasets |
| 멀티모달 인식·효율화 | 113 | 434 | 5 | Multilingual Language Model Quantization |
| 인과·통계 추론 | 108 | 590 | 4 | Causal Independence Testing |
| 계산 재료 시뮬레이션 | 107 | 559 | 4 | Machine-Learned Interatomic Potentials |

- 상위 집중도: 생체분자 생성 모델링은 625편으로 최대이고, 자율 AI 과학 발견 (447편)와 형식 수학 정리 증명 (330편)이 뒤따라 세 곳이 절반 이상을 차지한다.
- 가장 작은 대분류의 의미: 계산 재료 시뮬레이션 (107편)과 인과·통계 추론 (108편)는 작지만 각각 DFT 데이터와 통계 보증이라는 해자·인증층이다.
- 중복 포함 기준의 순위 역전: 인과·통계 추론는 고유 108편이 중복 590편으로, 자율 AI 과학 발견는 447편이 1,694편으로 늘어나 다른 분야에 걸친 정도가 크다.
- 이후 10개 파트는 이 순서(고유 배정 편수 내림차순)로 진행한다.

> [!tip] 우리에게 무엇인가
> 규모가 큰 곳은 생성의 영토이고 규모가 작은 곳은 검증의 영토다. 투자 판단은 두 쪽을 함께 보고 해야 한다.

---

## S05 · AI4S 서사: 예측에서 생성, 그리고 검증으로

*오프닝* · **Arc of AI4S: From Prediction to Generation to Verification** · *서사*

> [!abstract] 핵심 메시지
> 구조 예측이 풀린 뒤 생성과 자율화가 확산됐고, 2026년에는 검증이 경쟁축이 됐다.

- 배경: 2017 물리정보 신경망(PINN), 2020 GPT-f의 신경 증명, 2021 AlphaFold가 학습 기반 과학 계산이라는 축을 세웠다.
- 2022–2023 Pangu-Weather가 수치예보를 넘어서고 GNoME이 대량의 안정 결정 구조를 찾아 규모가 발견을 대체하기 시작했다.
- 2025 에이전트의 해. AI Scientist-v2가 동료 심사를 통과한 논문을, Kosmos가 대규모 롤아웃 보고서를, Polybot이 자율 실험실 폐루프를 시연했다.
- 2026 생성이 범용화되고 반증이 쏟아졌다. Robin의 습식 검증, BFS-Prover-V2의 형식 증명 성과와 함께 Ground False, QEDBench, The Leaderboard Lottery가 평가의 허점을 드러냈다.
- 2026 결론: 능력은 더 이상 희소하지 않다. 검증기·베이스라인·독립 재현을 갖춘 곳이 성과를 인정받는다.

> [!tip] 우리에게 무엇인가
> 서사의 중심은 능력에서 신뢰로의 이동이다. 국내 기관은 생성 모델 경쟁보다 검증 역량에서 차별화할 수 있다.

---

## S06 · 단일세포 발현 모델링

*제1부 · 생체분자 생성 모델링* · **Single-Cell Gene Expression Modeling** · *서브카테고리*

`121편` `2018–2026` `가속` `2025+ 113편`

<sub>생체분자 생성 모델링 고유 배정 625편(중복 포함 1,252편 · 웹 인덱스 기준) · 서브카테고리 20개 · 본 파트 5개로 48% 커버</sub>

> [!quote] 파트 도입
> 코퍼스 최대 분류. 생성은 흔해졌고, 경쟁축은 합성가능성·베이스라인 반증·실험 검증으로 넘어갔다.

> [!abstract] 핵심 메시지
> 단일세포 파운데이션 모델은 확산됐지만, 베이스라인 반증이 동시에 쌓이는 중이다.

- 2025 Cell2Sentence-Scale: 세포를 ‘세포 문장’ 텍스트로 바꿔 270억 파라미터 LLM으로 확장했다.
- 2026 PhenoSeq는 Cell Painting 이미징에서 조건부 확산으로 scGPT 기반 전사체 임베딩을 생성한다.
- 2026 ChronoTILE·HistoTx가 공간 전사체를 연속시간 flow matching과 H&E 조기 융합으로 확장했다.
- 2026 Hepa-RAFT가 가상 간세포 발현 반응을 검색 키로 써 약물유발 간손상(DILI) 위험을 예측한다.
- 배경: 2018–2021 SCANPY류 도구가 표준이 된 뒤, 2023–2026 ‘파운데이션 모델과 그 비판’, ‘섭동 예측과 베이스라인 청산’이 한 흐름으로 묶인다.

**대표 도구·시스템** — SCANPY · Geneformer/Genecorpus-104M · Tahoe-X1 · Cell2Sentence-Scale · Intermediate-Layers · CLAMP · GEARS/CPA · PerturbDiff

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Bridging Gene Regulatory Networks and Causal Representation Learning in Single-Cell Genomics Data](../../docs/papers/9358_Bridging_Gene_Regulatory_Networks_and_Causal_Representation/index.html) — Vincenzo Lagani 외, 2026 · 인용 3,730
    - GRN(gene regulatory network) 추론과 causal representation learning(CRL)이라는 서로 분리된 두 패러다임을 연결하기 위해, GRN에서 추출한 transcription factor(TF) com…
2. [Multi-Scale Flow Matching for Continuous-time Generative Modeling of Spatiotemporal Tissue Dynamics from Spatial Transcriptomics](../../docs/papers/10069_Multi-Scale_Flow_Matching_for_Continuous-time_Generative_Mod/index.html) — Pinar Demetci 외, 2026 · 인용 1,884
    - ChronoTILE는 spatial transcriptomics의 시간적으로 흩어진 단면 스냅샷들로부터 조직 리모델링의 연속시간 동역학을 학습하는 multi-scale, multi-marginal flow matching 프레임워크로, ce…
3. [Celcomen: spatial causal disentanglement for single-cell and tissue perturbation modeling](../../docs/papers/3051_Celcomen_spatial_causal_disentanglement_for_single-cell_and/index.html) — Stathis Megas 외, 2026.03 · 인용 8
    - Celcomen은 공간 전사체 데이터에서 세포 내·세포 간 유전자 조절을 분리하는 생성적 그래프 신경망이며, 수학적으로 증명된 인식 가능성(identiﬁability)을 바탕으로 섭동 후 반사실적 공간 전사체를 예측할 수 있다.
4. [PerturbDiff: Functional Diffusion for Single-Cell Perturbation Modeling](../../docs/papers/10174_PerturbDiff_Functional_Diffusion_for_Single-Cell_Perturbatio/index.html) — Xinyu Yuan 외, 2026
    - PerturbDiff는 단일 세포 수준이 아닌 분포(distribution) 수준에서 perturbation 반응을 모델링하기 위해, 세포 분포를 RKHS(reproducing kernel Hilbert space)의 kernel mean…

> [!tip] 우리에게 무엇인가
> 모델 규모보다 ‘단순 베이스라인을 이기는가’가 도입 기준이다. 국내는 자체 섭동 실험 데이터로 반증 가능한 평가셋을 먼저 갖춰야 한다.

---

## S07 · 단백질 언어모델 상호작용

*제1부 · 생체분자 생성 모델링* · **Protein Language Model Interactions** · *서브카테고리*

`53편` `2023–2026` `가속` `2025+ 51편`

> [!abstract] 핵심 메시지
> 단백질 언어모델은 서열 표현을 넘어 상호작용·적합도·구조를 결합하는 단계로 갔다.

- 2026 ProteomeLM이 proteome 전체를 입력해 interaction 라벨 없이 attention 으로 PPI 를 포착한다.[3]
- 2026 E1 이 상동 서열을 명시 조건화한 검색 증강 인코더로 zero-shot fitness·contact 예측을 낸다.
- 2026 ProtEGNN 은 PLM 에 경량 E(3)-등변 GNN 을 붙여 100-1000배 적은 파라미터로 7개 벤치마크 SOTA급을 냈다.
- 2026 PRIMA(BiMamba)·Ares(Soft-MoE) 등 아키텍처 효율화, MutAtlas·AURORA 등 돌연변이 효과 도구가 나왔다.[4]
- 배경: 2023–2024 ESMFold/ESM-2, ProtT5 가 진화 규모 서열 모델의 기준선을 놓았다.

**대표 도구·시스템** — ESMFold/ESM-2 · ProtT5 · ProtGPT2 · ProteomeLM · IsoPLM · PRIMA · FlashPPI · ProMaya

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Just Add Structure: Protein Language Models Combined with Structural Equivariance Excel at Protein Tasks](../../docs/papers/9859_Just_Add_Structure_Protein_Language_Models_Combined_with_Str/index.html) — Qurat ul ain 외, 2026 · 인용 16,139
    - PLM의 sequence representation과 protein structure의 3D 좌표 정보를 경량 E(3)-Equivariant GNN(ProtEGNN)으로 결합하여, 대규모 fine-tuning 없이도 protein prope…
2. [Protein Language Models Diverge from Natural Language: Comparative Analysis and Improved Inference](../../docs/papers/3221_Protein_Language_Models_Diverge_from_Natural_Language_Compar/index.html) — 2026.02 · 인용 3,225
    - 단백질 언어 모델(PLM)이 자연어 모델(NLM)과 내부 메커니즘에서 근본적으로 다르게 작동함을 분석하고, 동적 early-exit 기법을 적용하여 성능과 효율을 동시에 개선한다.
3. [ProteomeLM: A Proteome-Scale Language Model Enables Accurate and Rapid Prediction of Protein-Protein Interactions and Gene Essentiality Across Taxa](../../docs/papers/10267_ProteomeLM_A_Proteome-Scale_Language_Model_Enables_Accurate/index.html) — Cyril Malbranke 외, 2026 · 인용 763
    - ProteomeLM은 전체 proteome을 입력으로 받아 masked protein embedding 재구성을 통해 학습하는 transformer 기반 language model로, 별도의 interaction label 없이도 atten…
4. [PRIMA: a bidirectional state-space architecture and training approach for sequence modelling of protein-protein interactions](../../docs/papers/10235_PRIMA_a_bidirectional_state-space_architecture_and_training/index.html) — Arturo Fiorellini-Bernardis 외, 2026 · 인용 599
    - PRIMA는 bidirectional Mamba(BiMamba) 기반의 선형 복잡도 state-space model을 이용해 단백질-단백질 상호작용(PPI)을 위한 protein language model(PLM)을 제안하며, 동일 파라미터…

> [!tip] 우리에게 무엇인가
> 범용 PLM 은 이미 바닥재다. 우리 몫은 자체 표적에 맞는 상호작용·적합도 헤드와 일반화 감사다.

---

## S08 · 이산 확산 분자 생성

*제1부 · 생체분자 생성 모델링* · **Discrete Diffusion Molecule Generation** · *서브카테고리*

<sub>타임라인 분석 명칭: Discrete Diffusion & Flow Molecule Generation</sub>

`43편` `2018–2026` `가속` `2025+ 42편`

> [!abstract] 핵심 메시지
> 분자 생성의 질문이 ‘만들 수 있나’에서 ‘합성되고 개발 가능한가’로 바뀌었다.

- 2026 CoCoGraph 는 Double Edge Swapping 으로 화학 제약을 확산 과정에 내장해 100% 유효 분자를 생성한다.
- 2026 GenMol 에 IIFT 후학습을 얹어 ADMET 와 합성 접근성을 동시에 겨냥했다.
- 2026 SynLaD·S3-GFN 이 3D 약리단 조건과 합성 경로, 합성가능성 soft 제약을 생성에 직접 넣는다.[4]
- 2026 CupOFLATTE 가 PROTAC 의 warhead·linker·E3 리간드를 결합 discrete flow 로 동시 생성한다.[1]
- 배경: 2018 MolGAN 의 그래프 생성에서 출발해 2024 이후 이산 확산·flow matching 으로 이동했다.

**대표 도구·시스템** — MolGAN · CoCoGraph · MolHIT · MoCDiff · GenMol/IIFT · Graph-GRPO · InertialAR · MotiFlow

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [CupOFLATTE: Coupled Objective-Guided Discrete Flows via Linker Assembly for Targeted PROTAC Engineering](../../docs/papers/9468_CupOFLATTE_Coupled_Objective-Guided_Discrete_Flows_via_Linke/index.html) — Ziang Li 외, 2026 · 인용 157
    - PROTAC의 warhead-linker-E3 ligand를 개별적으로 설계 후 조립하는 기존 방식과 달리, CupOFLATTE는 세 구성요소를 결합된 discrete flow 상에서 동시에 생성하여 조립 단계에서의 화학적 유효성과 기능적…
2. [A collaborative constrained graph diffusion model for the generation of realistic synthetic molecules](../../docs/papers/2984_A_collaborative_constrained_graph_diffusion_model_for_the_ge/index.html) — Manuel Ruiz-Botella 외, 2026.05 · 인용 3
    - CoCoGraph는 Double Edge Swapping(DES)을 통해 화학적 제약조건을 확산 과정에 직접 내장하여 100% 화학적으로 유효한 분자를 생성하는 협력형 제약 그래프 확산 모델이다. Diffusion model과 Time mo…
3. [Rethinking Diffusion Models with Symmetries through Canonicalization with Applications to Molecular Graph Generation](../../docs/papers/10330_Rethinking_Diffusion_Models_with_Symmetries_through_Canonica/index.html) — Cai Zhou 외, 2026
    - 분자 생성과 같이 순열 및 회전 대칭에 불변인 분포를 학습할 때, 기존의 equivariant 아키텍처 대신 각 샘플을 canonical orbit representative로 매핑한 뒤 제약 없는(non-equivariant) diffus…
4. [SynLaD: Latent Diffusion for Generating Synthesizable Molecules Conditioned on 3D Pharmacophore Profiles](../../docs/papers/10527_SynLaD_Latent_Diffusion_for_Generating_Synthesizable_Molecul/index.html) — Miruna Cretu 외, 2026
    - SynLaD은 3D pharmacophore profile에 조건화된 latent diffusion을 통해 3D 구조 생성과 합성 경로(synthesis pathway) 생성을 하나의 latent space에서 동시에 수행하는 프레임워크이다…

> [!tip] 우리에게 무엇인가
> 생성 능력은 범용화됐다. 합성가능성·개발가능성 제약을 내장한 모델과 그 평가가 실제 후보를 가른다.

---

## S09 · 역합성 반응 예측

*제1부 · 생체분자 생성 모델링* · **Retrosynthesis Reaction Prediction** · *서브카테고리*

`41편` `2025+ 31편`

> [!abstract] 핵심 메시지
> 역합성은 LLM 에이전트로 옮겨 가는 동시에 평가 지표 자체를 의심받고 있다.

- 2026 RetrOrchestrator 는 다단계 역합성을 POMDP 로 재정의해 단일단계 모델을 도구로 선택하는 LLM 에이전트다.[3]
- 2025 LARC 는 발암물질 회피 등 제약 아래 역합성 계획에서 72.9% 성공률을 냈다.
- 2026 Synthegy 가 LLM 화학 추론으로 경로를 전략 지시에 따라 평가하고 전문가 일치율 71.2% 를 얻었다.
- 2026 ChemCensor·CREED·URSA-expert-2026 이 단일 정답 Top-K 정확도의 한계를 지적했다.
- 2026 AIDD position 논문은 모델이 의도한 특징을 배우지 못한다며 misaligned baselines 진단을 제안했다.

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Enhancing chemical reaction and retrosynthesis prediction with large language model and dual-task learning](../../docs/papers/316_Enhancing_chemical_reaction_and_retrosynthesis_prediction_wi/index.html) — Xuan Lin 외, 2025 · 인용 3
    - 본 논문은 대규모 언어 모델(LLM)을 화학 반응 및 역합성 예측에 적용할 때 직면하는 데이터 부족과 과제 간 상관관계 무시 문제를 해결하기 위해, BRICS 기반 440만 개 분자 데이터셋과 이중 과제 학습 전략을 갖춘 ChemDual 프…
2. [RETROSPECT: RETROsynthesis via Sequential Prediction, and Chemically Transformed-ranking](../../docs/papers/10340_RETROSPECT_RETROsynthesis_via_Sequential_Prediction_and_Chem/index.html) — Raja Sekhar Pappala 외, 2026 · 인용 241
    - 단일 Transformer 기반 제안 모델(ChemAlign Transformer)과 LambdaMART 리랭커를 결합해 단일단계 retrosynthesis를 proposal-selection 분해 관점에서 모듈화하고, USPTO-50K에서…
3. [RetrOrchestrator: A Multi-Step Retrosynthesis Agent Dynamically Orchestrating Single-Step Transition Models](../../docs/papers/10339_RetrOrchestrator_A_Multi-Step_Retrosynthesis_Agent_Dynamical/index.html) — Liao Chang 외, 2026
    - RetrOrchestrator는 multi-step retrosynthesis planning을 POMDP로 재정의하여, 각 단계마다 확장할 분자뿐 아니라 어떤 single-step retrosynthesis model(SSR)을 tool로…
4. [Order Matters in Retrosynthesis: Structure-aware Generation via Reaction-Center-Guided Discrete Flow Matching](../../docs/papers/3196_Order_Matters_in_Retrosynthesis_Structure-aware_Generation_v/index.html) — 2026.02
    - 이 논문은 원자 순서를 구조적 귀납 편향으로 활용하여 역합성 예측을 수행하는 RetroDiT를 제안한다. 반응 중심 원자를 시퀀스 맨 앞에 배치함으로써 화학 반응의 두 단계 특성(반응 중심 식별 및 반응물 생성)을 위치 기반 편향으로 인코딩…

> [!tip] 우리에게 무엇인가
> 합성 계획은 지표가 문제다. Top-K 정확도가 아니라 화학적 타당성으로 평가하는 내부 벤치마크가 먼저다.

---

## S10 · 유전체 파운데이션 모델

*제1부 · 생체분자 생성 모델링* · **Genomic Foundation Models** · *서브카테고리*

`40편` `2019–2026` `가속` `2025+ 37편`

> [!abstract] 핵심 메시지
> 유전체 모델은 길고 넓은 입력으로 커지며, 토큰화와 사전학습 목적을 다시 묻는다.

- 2025 Evo 2 가 9.3조 염기쌍, 7B·40B, 1백만 토큰 컨텍스트로 전 생명 영역의 게놈 설계를 겨냥했다.
- 2025 AlphaGenome 이 1Mb 입력·bp 해상도로 11개 모달리티 5,930개 트랙을 동시에 예측한다.
- 2026 EDEN 이 최대 28B 파라미터로 Transformer·Mamba·Hyena 의 scaling 을 비교, 대규모에서 Transformer 우위를 보였다.
- 2026 LDARNet·DNAChunker·OpticalDNA 가 고정 토큰화를 학습형 분절과 이미지 렌더링으로 대체한다.[3][4]
- 2026 representative vs. load-bearing layer 분리 등 해석성 감사가 NT-v2·Evo 2 의 층별 의존을 문제 삼는다.

**대표 도구·시스템** — AlphaGenome · Seq2Exp · BlueSTARR · Hi-Compass · Evo 2 · EDEN · LDARNet · BioToken/BioFM

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Scaling Laws and Architectural Frontiers in Metagenomic Foundation Models](../../docs/papers/10375_Scaling_Laws_and_Architectural_Frontiers_in_Metagenomic_Foun/index.html) — Geraldene Munsamy 외, 2026 · 인용 519
    - EDEN이라는 최대 28B 파라미터, 9.7조 뉴클레오타이드 토큰으로 학습된 metagenomic foundation model 계열을 통해 Transformer(Llama-style), State-Space Model(Mamba), Lon…
2. [Representative vs. Load-bearing Layers: A Dissociation in Genomic Foundation Models](../../docs/papers/10324_Representative_vs_Load-bearing_Layers_A_Dissociation_in_Geno/index.html) — Yoonjin Cho 외, 2026 · 인용 146
    - Genomic foundation model(NT-v2, Evo 2)의 layer별 hidden-state shift(‖Δhℓ‖2)를 이용해, 단일 feature 판별력이 가장 높은 representative layer와 joint clas…
3. [LDARNet: DNA Adaptive Representation Network with Learnable Tokenization for Genomic Modeling](../../docs/papers/9884_LDARNet_DNA_Adaptive_Representation_Network_with_Learnable_T/index.html) — Daria Ledneva 외, 2026 · 인용 104
    - LDARNet은 H-Net의 동적 청킹(dynamic chunking) 아이디어를 autoregressive 생성에서 masked language modeling(MLM)으로 확장하여, 고정된 tokenization(k-mer, BPE, s…
4. [DNACHUNKER: Learnable Tokenization for DNA Language Models](../../docs/papers/9536_DNACHUNKER_Learnable_Tokenization_for_DNA_Language_Models/index.html) — Taewon Kim 외, 2026 · 인용 11
    - DNAChunker는 masked DNA language model에 학습 가능한 adaptive segmentation 모듈을 결합하여, 고정된 tokenization(단일 nucleotide, k-mer, BPE) 대신 context-d…

> [!tip] 우리에게 무엇인가
> 규모 경쟁은 해외 몫이다. 국내는 PlasmidLM류 검증 가능한 보상과 도메인 특화 설계에서 승부할 수 있다.

---

## S11 · 자율 AI 과학자 에이전트

*제2부 · 자율 AI 과학 발견* · **Autonomous AI Scientist Agents** · *서브카테고리*

`70편` `2021–2026` `가속` `2025+ 62편`

<sub>자율 AI 과학 발견 고유 배정 447편(중복 포함 1,694편 · 웹 인덱스 기준) · 서브카테고리 16개 · 본 파트 5개로 49% 커버</sub>

> [!quote] 파트 도입
> 폐루프 시연은 실험실에서 현실이 됐고, 추론 규범 위반의 증거도 같은 해에 쌓였다. 결과물보다 검증 체계가 경쟁력이다.

> [!abstract] 핵심 메시지
> 논문을 쓰는 AI 과학자는 등장했고, 평가의 무게는 결과물에서 과정 추적으로 옮겨갔다.

- 2025 AI Scientist-v2가 에이전트 트리 서치로 가설·실험·논문 작성을 자율 수행해 동료 심사를 통과한 AI 생성 논문을 냈다.[2]
- 2025 DeepScientist가 약 5,000개 아이디어를 만들고 1,100개를 검증하는 데 20,000 GPU시간을 썼다.[3]
- 2025 EXP-Bench는 end-to-end 성공률 0.5%를 보고해 시연과 실제 실험 수행 능력의 간극을 드러냈다.
- 2026 OpenDiscoveryTrace와 FabScore가 최종 출력 대신 추론 과정 추적과 조작 감사로 평가축을 옮겼다.[1]
- 배경: 2024 The AI Scientist가 아이디어에서 원고까지 이어지는 파이프라인 자동화의 출발점을 만들었다.

**대표 도구·시스템** — The AI Scientist / AI Scientist-v2 · AI-Researcher + Scientist-Bench · DeepScientist · MLR-Bench · EXP-Bench · AIRS-Bench · Curie · MARS · AutoSOTA · OpenDiscoveryTrace · FabScore · AgentRxiv · aiXiv

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [OpenDiscoveryTrace: Process Traces for Evaluating AI Scientist Workflows](../../docs/papers/10134_OpenDiscoveryTrace_Process_Traces_for_Evaluating_AI_Scientis/index.html) — Aayam Bansal 외, 2026 · 인용 2,072
    - OpenDiscoveryTrace는 AI scientist agent의 최종 출력물이 아니라 추론 과정 자체를 9-필드 구조로 기록한 558개 trajectory 데이터셋으로, 이를 통해 output-only 평가에서는 드러나지 않는 모델…
2. [The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search](../../docs/papers/794_The_AI_Scientist-v2_Workshop-Level_Automated_Scientific_Disc/index.html) — Yutaro Yamada 외, 2025.04 · 인용 476
    - AI Scientist-v2는 에이전트 기반 트리 서치(agentic tree search)를 활용하여 가설 수립, 실험 설계·실행, 데이터 분석 및 시각화, 논문 자동 작성까지 완전히 자율적으로 수행하는 과학 발견 시스템으로, 최초로 동료…
3. [DeepScientist: Advancing Frontier-Pushing Scientific Findings Progressively](../../docs/papers/10727_deepscientist_advancing_frontier-pushing_scientific_fi/index.html) — Yixuan Weng 외, 2025.09 · 인용 73
    - DeepScientist는 과학적 발견을 Bayesian Optimization 문제로 형식화하고, "hypothesize-verify-analyze"의 계층적 평가 프로세스와 누적 Findings Memory를 통해 exploration과…
4. [SafeScientist: Toward Risk-Aware Scientific Discoveries by LLM Agents](../../docs/papers/692_Safescientist_Toward_risk-aware_scientific_discoveries_by_ll/index.html) — Kunlun Zhu 외, 2025 · 인용 1
    - 본 논문은 LLM 기반 AI 과학자 에이전트의 자동화된 과학 발견 과정에서 발생하는 윤리적, 안전 문제를 체계적으로 해결하기 위해 SafeScientist 프레임워크를 제안한다. 이는 다층 방어 메커니즘(prompt monitoring, a…

> [!tip] 우리에게 무엇인가
> AI 과학자는 만들 수 있게 됐지만 믿을 수 있는지는 별개다. 과정 로그와 인간 체크포인트를 설계하는 쪽이 도입 판단의 주도권을 쥔다.

---

## S12 · 자율 과학 발견 시스템

*제2부 · 자율 AI 과학 발견* · **Autonomous Scientific Discovery Systems** · *서브카테고리*

`46편` `2023–2026` `가속` `2025+ 39편`

> [!abstract] 핵심 메시지
> 폐루프 발견 시스템이 늘어난 만큼 과학적 추론 규범을 지키지 못한다는 증거도 쌓였다.

- 2025 Kosmos가 200개 이상의 agent rollout로 평균 42,000줄 코드와 1,500편 논문을 처리해 79.4% 정확도의 보고서를 냈다.[5]
- 2026 AI scientists produce results without reasoning scientifically가 25,000개 이상 실행에서 증거 무시 68%, 신념 수정 부재 26%를 보고했다.[3]
- 2025 AI Scientists Fail Without Strong Implementation Capability가 병목을 아이디어가 아니라 구현 능력에 있다고 주장했다.[1]
- 2026 Autonomous biomedical research with an artificial intelligence agent의 Biomni가 150개 도구와 59개 데이터베이스를 묶었다.[2]
- 배경: 2023 CRESt, k-agents가 LLM을 물리 실험실의 조력자로 끌어들인 출발점이다.

**대표 도구·시스템** — CRESt · k-agents · Kosmos · AI-Newton · LabOS · AutoBio · Biomni · Earth-Agent · BehaveAgent · EmbodiedAct · AIGS/BABY-AIGS

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [AI Scientists Fail Without Strong Implementation Capability](../../docs/papers/081_Ai_scientists_fail_without_strong_implementation_capability/index.html) — Min Zhu 외, 2025 · 인용 2,819
    - 이 position paper는 AI Scientist 시스템의 근본적 병목이 아이디어 생성 능력이 아니라 실험 검증을 위한 구현(implementation) 능력에 있다고 주장하며, 벤치마크 정량 증거와 28편의 AI Scientist 생…
2. [Autonomous biomedical research with an artificial intelligence agent](../../docs/papers/10933_Autonomous_biomedical_research_with_an_artificial_intelligen/index.html) — Kexin Huang 외, 2026.07 · 인용 14
    - Biomni는 150개 전문 도구, 105개 소프트웨어 패키지, 59개 데이터베이스로 구성된 통합 biomedical action space(Biomni-E1)와 이를 활용해 LLM 기반 추론·검색증강 계획·코드 실행을 결합한 범용 에이전트…
3. [AI scientists produce results without reasoning scientifically](../../docs/papers/9108_ai_scientists_produce_results_without_reasoning_scienti/index.html) — Martiño Ríos-García 외, 2026 · 인용 342
    - 본 논문은 LLM 기반 scientific agent들이 과학적 추론의 인식론적 규범을 따르지 못한다는 점을 체계적으로 입증한다. 25,000개 이상의 agent 실행을 통해 base model이 성능과 행동의 주요 결정자임을 보였으며, 증…
4. [Autonomous Agents for Scientific Discovery: Orchestrating Scientists, Language, Code, and Physics](../../docs/papers/137_Autonomous_Agents_for_Scientific_Discovery_Orchestrating_Sci/index.html) — Lianhao Zhou 외, 2025.10 · 인용 12,647
    - 대규모 언어 모델(LLM) 기반 자율 에이전트(Scientific Agents)가 과학 발견의 전체 생명주기를 자동화하고 가속화할 수 있는 새로운 패러다임을 제시한다. 이들 에이전트는 자연언어, 프로그래밍 코드, 물리 정보를 통합하여 인간…
5. [Kosmos: An AI Scientist for Autonomous Discovery](../../docs/papers/9098_kosmos_an_ai_scientist_for_autonomous_discovery/index.html) — Ludovico Mitchener 외, 2025 · 인용 131
    - Kosmos는 structured world model을 활용하여 data analysis agent와 literature search agent 간에 정보를 공유함으로써 data-driven scientific discovery를 자동화하…
6. [From AI for Science to Agentic Science: A Survey on Autonomous Scientific Discovery](../../docs/papers/352_From_AI_for_Science_to_Agentic_Science_A_Survey_on_Autonomou/index.html) — Jiaqi Wei 외, 2025.10 · 인용 5
    - 본 논문은 AI가 전문화된 계산 도구에서 자율적 과학 연구 파트너로 진화하는 과정을 체계화하며, 에이전틱 사이언스(Agentic Science)를 AI for Science의 핵심 패러다임으로 위치지었다. 대규모 언어 모델(LLM)과 멀티모…

> [!tip] 우리에게 무엇인가
> 시스템 능력과 추론 신뢰도가 따로 움직인다. 검증기를 먼저 세우고 자율성을 단계적으로 늘리는 설계가 안전하다.

---

## S13 · 에이전틱 신약 발굴

*제2부 · 자율 AI 과학 발견* · **Agentic Drug Discovery Workflows** · *서브카테고리*

`36편` `2024–2026` `가속` `2025+ 32편`

> [!abstract] 핵심 메시지
> 신약 에이전트는 습식 검증까지 닿았고, 평가는 증거 부족을 인정하는 능력으로 넘어갔다.

- 2026 Robin이 Crow, Falcon, Finch 에이전트로 가설-실험-해석 루프를 돌려 dAMD 후보 ripasudil을 발굴하고 실험 검증했다.
- 2026 Co-Scientist가 tournament 기반 진화로 약물 재창출, 신규 표적, 항생제 내성 기전 가설을 실험 검증했다.
- 2026 TRIAGE가 표적 발굴을 가설 생성이 아니라 적대적 반증 문제로 재정의했다.[1]
- 2026 AMR-Bench-mini가 GPT-5.4 등 세 모델 모두 증거 불충분 인정(abstention)에서 약점을 보이는지 진단했다.[4]
- 배경: 2025 TxAgent가 211개 생의학 도구를, PharmAgents가 가상 제약사 전체 파이프라인을 구현했다.[2][3]

**대표 도구·시스템** — TxAgent · PharmAgents · DrugPilot · LIDDIA · CLADD · SciToolAgent · Robin (Crow/Falcon/Finch) · TRIAGE · BioMiner · MolQuest · Tippy

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [TRIAGE: An AI Scientist for Adversarial Target Falsification](../../docs/papers/10638_TRIAGE_An_AI_Scientist_for_Adversarial_Target_Falsification/index.html) — Jiawei Xing, 2026 · 인용 119
    - TRIAGE는 신약개발에서 타겟 발굴을 '가설 생성'이 아닌 '가설 반증(falsification)'의 문제로 재정의하여, 생성 에이전트가 제안한 후보 타겟을 두 개의 적대적(adversarial) 에이전트가 근거 검색과 in silico…
2. [PharmAgents: Building a Virtual Pharma with Large Language Model Agents](../../docs/papers/616_PharmAgents_Building_a_Virtual_Pharma_with_Large_Language_Mo/index.html) — Bowen Gao 외, 2025 · 인용 2
    - PharmAgents는 대규모 언어모델(LLM) 기반의 다중 에이전트 시스템으로 신약 발견의 전체 파이프라인(타겟 발굴부터 전임상 평가까지)을 자동화하고 설명 가능하게 구현한 가상 제약사 플랫폼이다.
3. [TxAgent: An AI Agent for Therapeutic Reasoning Across a Universe of Tools](../../docs/papers/848_TxAgent_An_AI_Agent_for_Therapeutic_Reasoning_Across_a_Unive/index.html) — Shanghua Gao 외, 2025.03
    - 정밀 치료(precision therapeutics)를 위해 211개의 생의학 도구(biomedical tools)를 활용한 다단계 추론 AI 에이전트 TxAgent를 제시하며, FDA 승인 약물 정보와 Open Targets 임상 정보를…
4. [AMR-Bench-mini: A Diagnostic Benchmark for Agentic Mechanistic AMR Reasoning under Evidence Insufficiency](../../docs/papers/9239_AMR-Bench-mini_A_Diagnostic_Benchmark_for_Agentic_Mechanisti/index.html) — Ali Ihsan Nergiz 외, 2026 · 인용 2,475
    - 이 논문은 Klebsiella pneumoniae에 국한된 924개 과제로 구성된 진단형 벤치마크 AMR-Bench-mini를 제안하여, frontier LLM 에이전트가 항생제 내성(AMR) 기전을 추론할 때 evidence suffici…

> [!tip] 우리에게 무엇인가
> 신약 에이전트의 가치는 후보 생성이 아니라 반증과 기권을 설계하는 데 있다. 습식 검증 파트너십이 있는 곳이 앞선다.

---

## S14 · 자율 실험실·공동 과학자

*제2부 · 자율 AI 과학 발견* · **AI Co-Scientist Research Acceleration** · *서브카테고리*

`35편` `2021–2026` `가속` `2025+ 30편`

> [!abstract] 핵심 메시지
> 자율주행 실험실이 소재 합성까지 폐루프를 닫았고, 가속 효과를 재는 법이 정리되기 시작했다.

- 2025 Polybot이 7차원 공정 공간을 베이지안 최적화로 탐색해 전자 고분자 박막에서 4500 S/cm 이상의 전도도를 달성했다.
- 2026 Agentic LLM Reasoning이 A-Lab GPSS에 연역·귀납 추론을 얹어 공기 민감 리튬 할라이드 스피넬을 자율 발견했다.
- 2026 RoboChem-Flex가 약 5,000달러 모듈형 자율 실험실로 반응 최적화 비용을 낮췄다.
- 2026 Benchmarking self-driving labs가 acceleration factor와 enhancement factor로 가속 주장을 정량화했다.[1]
- 배경: 2023 A-Lab이 57건 중 36건의 자율 무기 합성을 달성했고, 이후 신규성 논란과 정정(Author Correction)이 검증 규범의 계기가 됐다.

**대표 도구·시스템** — A-Lab / A-Lab GPSS · AMASE · Polybot · Gemini Co-Scientist · RoboChem-Flex · NIMO + IvoryOS · CARTOGRAPH · AutoMat · CICERO

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Benchmarking self-driving labs](../../docs/papers/10935_Benchmarking_self-driving_labs/index.html) — Adedire D. Adesiji 외, 2026 · 인용 11
    - 이 리뷰 논문은 self-driving labs(SDLs)가 재료 탐색 과정을 얼마나 가속하는지 정량화하는 두 지표인 acceleration factor(AF)와 enhancement factor(EF)의 이론적 배경을 정리하고, 문헌 조사…
2. [Author Correction: An autonomous laboratory for the accelerated synthesis of inorganic materials](../../docs/papers/10931_Author_Correction_An_autonomous_laboratory_for_the_accelerat/index.html) — Nathan J. Szymanski 외, 2026.02 · 인용 5
    - 이 문서는 2023년 Nature에 발표된 "An autonomous laboratory for the accelerated synthesis of inorganic materials" 논문에 대한 Author Correction으로, 회절…
3. [Accelerating Scientific Research with Gemini in the Real-World](../../docs/papers/10911_accelerating_scientific_research_with_gemini_in_the_re/index.html) — Samuel Schmidgall 외, 2026.08
    - Gemini 기반 멀티에이전트 시스템 Co-Scientist를 in silico 가설 생성 단계에서 실행 기반(execution-grounded) 연구 파트너로 확장하여, 재료과학·생물학·컴퓨터과학 세 분야에서 실제 폐루프(closed-lo…
4. [A flexible and affordable self-driving laboratory for automated reaction optimization](../../docs/papers/2989_A_flexible_and_affordable_self-driving_laboratory_for_automa/index.html) — Simone Pilon 외, 2026.04 · 인용 13
    - RoboChem-Flex는 약 5,000달러의 저비용 모듈형 자율주행 실험실 플랫폼으로, 3D 프린팅 하드웨어와 Python 기반 Bayesian 최적화 소프트웨어를 결합하여 다양한 합성 반응의 자동 최적화를 지원한다.

> [!tip] 우리에게 무엇인가
> 하드웨어 장벽은 낮아졌고 승부는 가속 효과를 증명하는 평가 체계다. 신규성 주장은 독립 재현으로 닫아야 한다.

---

## S15 · 단백질 공학 에이전트

*제2부 · 자율 AI 과학 발견* · **LLM-Driven Protein Engineering Agents** · *서브카테고리*

`34편` `2021–2026` `가속` `2025+ 27편`

> [!abstract] 핵심 메시지
> 단백질 에이전트는 도구 호출에서 강화학습 후학습으로 진화했고 벤치마크는 한계를 재고 있다.

- 2026 Latent-Y가 실험실 검증을 마친 나노바디를 56배 가속으로 제공했다고 key_developments에 올랐다.
- 2025 Sparks가 완전 자동화된 발견 사이클로 단백질 과학의 미지 현상 두 가지를 발견했다.[3]
- 2026 AgentPLM과 state-aware GRPO가 도구 호출을 후학습에 편입해 제약 위반을 생성 중에 교정한다.[2]
- 2026 SMDD-Bench에서 최고 성능 GPT5.4도 과제의 40.2%만 해결해 실제 신약 설계의 난도를 보였다.
- 배경: 2023 SAMPLE이 자율 플랫폼으로 GH1 열안정성을 12도 이상 높였다.

**대표 도구·시스템** — SAMPLE · CRISPR-GPT · ProtAgents · PRIME · Sparks · Agent Rosetta · AgentPLM · STRIDE · Latent-Y · MolOpt-Eval · TadA-Bench · CIDER

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [CIDER: Conformal Information-Directed Agents for Low-Budget Protein Engineering](../../docs/papers/9400_CIDER_Conformal_Information-Directed_Agents_for_Low-Budget_P/index.html) — Rishabh Bhattacharya, 2026 · 인용 6,121
    - 저예산(fixed-budget) 단백질 엔지니어링을 top-tail discovery 문제로 재정의하고, ProteinGym DMS assay를 안전 필터링된 순차적 batched design-build-test-learn 캠페인으로 변환하…
2. [AgentPLM: Agentic Protein Language Models with Reasoning-Augmented Decoding for Protein Sequence Design](../../docs/papers/9214_AgentPLM_Agentic_Protein_Language_Models_with_Reasoning-Augm/index.html) — Sahil Rahman 외, 2026 · 인용 1,186
    - AgentPLM은 사전학습된 단백질 언어모델(PLM)에 ESMFold, FoldX, AutoDock Vina 등 외부 도구 호출을 자기회귀 생성 과정에 삽입하는 Reasoning-Augmented Decoding(RAD)과, 궤적 수준 대비…
3. [Sparks: Multi-Agent Artificial Intelligence Model Discovers Protein Design Principles](../../docs/papers/764_Sparks_Multi-Agent_Artificial_Intelligence_Model_Discovers_P/index.html) — Alireza Ghafarollahi 외, 2025 · 인용 9
    - Sparks는 기존 AI 시스템의 훈련 분포 내 패턴 인식을 넘어 완전히 자동화된 과학적 발견 사이클을 수행하는 다중모달 다중에이전트 AI 모델이다. 본 연구는 단백질 과학에서 이전에 알려지지 않은 두 가지 현상을 발견함으로써 진정한 자동화…
4. [TadA-Bench: A Million-Variant Benchmark for Future-Round Discovery Toward Agentic Protein Engineering](../../docs/papers/10537_TadA-Bench_A_Million-Variant_Benchmark_for_Future-Round_Disc/index.html) — Jin Gao 외, 2026 · 인용 7
    - TadA-Bench는 31라운드에 걸친 TadA directed evolution 실험 데이터를 활용해, 이전 라운드 데이터로 이후 라운드 변이체의 활성을 예측·순위화하는 future-round discovery 벤치마크를 제안하며, Seq…

> [!tip] 우리에게 무엇인가
> 도구 연결은 상품화되고 후학습과 벤치마크가 새 축이다. 라운드 단위 실험 데이터를 갖춘 기관이 평가 주도권을 쥔다.

---

## S16 · 검증 가능 보상 RL

*제3부 · 형식 수학 정리 증명* · **Verifiable RL for Reasoning** · *서브카테고리*

`47편` `2023–2026` `가속` `2025+ 46편`

<sub>형식 수학 정리 증명 고유 배정 330편(중복 포함 883편 · 웹 인덱스 기준) · 서브카테고리 13개 · 본 파트 5개로 52% 커버</sub>

> [!quote] 파트 도입
> 검증기가 있는 도메인은 RL로 빠르게 풀린다. 이제 병목은 증명이 아니라 진술·벤치마크·검증의 신뢰다.

> [!abstract] 핵심 메시지
> 정답을 검사할 수 있는 도메인에서 RL이 추론을 만든다. 보상 자체를 해킹하는 문제가 따라왔다.

- 2025 DeepSeek-R1이 사람이 단 추론 궤적 없이 순수 RL만으로 자기 검증·재검토 패턴을 유도했다.[1]
- 2025 RISE는 풀이와 자기검증을 검증 가능한 보상으로 동시에 온라인 학습해 '표면적 자기반성'을 겨냥했다.
- 2026 SD-ZERO·DistIL이 이진 보상을 토큰 단위 밀집 감독과 풍부한 피드백으로 바꿔 보상 신호를 키웠다.
- 2026 BENCHJACK은 에이전트 벤치마크의 reward hacking 결함을 8가지 유형으로 분류하고 10개를 감사했다.[2]
- 배경: 2023 CRITIC의 도구 상호작용 자기수정이 이 흐름의 출발점이다.

**대표 도구·시스템** — DeepSeek-R1 · Critique-GRPO · ReTool · RM-R1 · PAG · SD-ZERO · BENCHJACK · VeRA

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning](../../docs/papers/265_DeepSeek-R1_incentivizes_reasoning_in_LLMs_through_reinforce/index.html) — DeepSeek-AI 외, 2025 · 인용 1,046
    - 본 논문은 인간이 주석을 단 추론 궤적(reasoning trajectory) 없이 순수 강화학습(RL)을 통해 대형언어모델(LLM)의 추론 능력을 유도할 수 있음을 보여준다. RL 훈련 과정에서 모델은 자발적으로 자기 검증, 재검토, 동적…
2. [Do Androids Dream of Breaking the Game? Systematically Auditing AI Agent Benchmarks with BenchJack](../../docs/papers/10951_Do_Androids_Dream_of_Breaking_the_Game_Systematically_Auditi/index.html) — Hao Wang 외, 2026.05
    - AI agent benchmark들이 reward hacking에 구조적으로 취약하다는 점을 8가지 결함 유형 taxonomy로 정리하고, 이를 자동으로 탐지·패치하는 red-teaming 시스템 BENCHJACK을 제안해 10개 주요 ag…
3. [Critique-GRPO: Advancing LLM Reasoning with Natural Language and Numerical Feedback](../../docs/papers/243_Critique-GRPO_Advancing_LLM_Reasoning_with_Natural_Language/index.html) — Xiaoying Zhang 외, 2025
    - 본 논문은 순수 수치 보상(numerical rewards)의 한계를 극복하기 위해 자연언어 비판(natural language critiques)을 온라인 강화학습(online RL) 프레임워크에 통합한 Critique-GRPO를 제안한다…
4. [Self-Distillation Zero: Self-Revision Turns Binary Rewards into Dense Supervision](../../docs/papers/10409_Self-Distillation_Zero_Self-Revision_Turns_Binary_Rewards_in/index.html) — Yinghui He 외, 2026
    - SD-ZERO는 단일 모델이 Generator와 Reviser 두 역할을 수행하도록 학습시켜, binary reward를 dense token-level self-supervision으로 변환하는 self-distillation 기법이다.…

> [!tip] 우리에게 무엇인가
> RL 레시피는 공개돼 있어 차별점이 아니다. 자체 도메인의 검증기와 보상 감사 체계를 갖추는 쪽이 경쟁력이다.

---

## S17 · LLM 형식 정리 증명

*제3부 · 형식 수학 정리 증명* · **Formal Theorem Proving with LLMs** · *서브카테고리*

`36편` `2020–2026` `가속` `2025+ 28편`

> [!abstract] 핵심 메시지
> 증명기는 miniF2F를 거의 포화시켰고, 같은 해에 그 점수의 의미를 묻는 감사가 나왔다.

- 2026 BFS-Prover-V2가 multi-turn off-policy RL과 multi-agent tree search로 miniF2F 95.08%, ProofNet 41.4%를 보고했다.[1]
- 2026 Numina-Lean-Agent는 범용 코딩 에이전트에 도구 모음을 붙여, 학습 없이 base model 교체만으로 성능을 올린다.
- 2026 VERITAS·Peano Player가 Lean 검증기의 구조화된 신호와 CMDP 정식화로 whole-proof RLVR을 앞섰다.[4]
- 2026 ProofGate는 pass rate가 faithfulness·alignment·vacuity를 뒤섞은 수치임을 분리해 감사했다.[3]
- 배경: 2020 GPT-f, 2021 miniF2F, 2024 DeepSeek-Prover의 800만 건 합성 Lean 증명이 출발점이다.[1]

**대표 도구·시스템** — GPT-f · miniF2F · DSP · DeepSeek-Prover · Lean-STaR · POETRY · BFS-Prover-V2 · VERITAS · Euclean · CombiBench

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [miniF2F-Dafny: LLM-Guided Mathematical Theorem Proving via Auto-Active Verification](../../docs/papers/10033_miniF2F-Dafny_LLM-Guided_Mathematical_Theorem_Proving_via_Au/index.html) — Mantas Baksys 외, 2026 · 인용 4
    - LLM이 수학 정리를 자동-능동 검증기(auto-active verifier)인 Dafny에서 증명하도록 유도하는 최초의 벤치마크 MINIF2F-DAFNY를 제시하며, SMT 자동화와 LLM의 고수준 증명 안내가 상호보완적임을 실증한다.
2. [OptProver: Bridging Olympiad and Optimization through Continual Training in Formal Theorem Proving](../../docs/papers/10144_OptProver_Bridging_Olympiad_and_Optimization_through_Continu/index.html) — Chenyi Li 외, 2026
    - OptProver는 Olympiad 수준 formal theorem proving 모델을 undergraduate 수준의 optimization 도메인으로 continual training을 통해 안전하게 transfer시키는 방법을 제안하…
3. [ProofGate: A Reproducible Audit of Faithfulness, Alignment, and Vacuity in State-of-the-Art Lean Theorem Provers](../../docs/papers/10257_ProofGate_A_Reproducible_Audit_of_Faithfulness_Alignment_and/index.html) — Edison Yang 외, 2026
    - 최근 SOTA neural theorem prover들이 miniF2F, PutnamBench에서 보고하는 높은 pass rate가 사실은 proof faithfulness, statement alignment, problem vacuity…
4. [VERITAS: Verifier-Guided Proof Search for Zero-Shot Formal Theorem Proving](../../docs/papers/10678_VERITAS_Verifier-Guided_Proof_Search_for_Zero-Shot_Formal_Th/index.html) — Manish Acharya 외, 2026
    - VERITAS는 Lean 검증기가 제공하는 syntax/type/goal-progress/completion 신호를 단일 pass/fail 비트로 뭉개지 않고, Best-of-N sampling과 critic-guided MCTS라는 두 단…

> [!tip] 우리에게 무엇인가
> 점수 경쟁은 끝물이다. 도구 인프라와 감사 가능한 평가를 먼저 갖추는 쪽이 오래 간다.

---

## S18 · 정리 자동 형식화

*제3부 · 형식 수학 정리 증명* · **Autoformalization of Theorems** · *서브카테고리*

`35편` `2023–2026` `가속` `2025+ 32편`

> [!abstract] 핵심 메시지
> 자연어를 Lean으로 옮기는 일이 가속되는 만큼, 옮겨진 진술의 충실도가 새 병목이 됐다.

- 2026 Ground False가 ProofNet 전 항목을 수작업 감사해 56%가 unfaithful이고 그중 절반 이상이 수학적으로 거짓임을 밝혔다.
- 2026 DSR가 분해-구조화-복구 파이프라인으로 operator tree 기반 오류 국소화를 도입했다.
- 2026 Formalizing Numerical Analysis가 kernel acceptance를 넘어 의미 정확성·mathlib 재사용으로 품질을 감사했다.
- 2026 Lean Disprove는 Lean 커널이 인증한 경우에만 REFUTED를 보고하는 반증 프레임워크다.
- 배경: 2023 LEGO-Prover의 스킬 라이브러리와 MUSTARD 데이터 합성이 자동 형식화 데이터의 출발점이다.

**대표 도구·시스템** — LEGO-Prover · MUSTARD · FormalRx · FormalRx-CC · VeriBench · Quokka · CertJudge · Signal-Coverage Matrix

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [FormalRx: Rectify and eXamine Semantic Failures in Autoformalization](../../docs/papers/9675_FormalRx_Rectify_and_eXamine_Semantic_Failures_in_Autoformal/index.html) — Haocheng Wang 외, 2026
    - FormalRx는 autoformalization 평가를 이진 판정 또는 스칼라 점수라는 블랙박스 방식에서 벗어나, 28개 오류 범주를 갖는 SCI Error Taxonomy에 기반한 verdict·categorization·localiza…
2. [Ground False: Dissecting Errors in Formal Mathematics Benchmarks](../../docs/papers/9759_Ground_False_Dissecting_Errors_in_Formal_Mathematics_Benchma/index.html) — One An 외, 2026 · 인용 159
    - 공식 수학 벤치마크(formal mathematics benchmark)의 ground truth(GT)가 사실상 무검증 상태로 신뢰되어 왔음을 지적하고, ProofNet 전체 367개 항목을 수작업 감사한 결과 56%가 unfaithful…
3. [The Signal-Coverage Matrix: Stratifying Type and Semantic Errors in Statement Autoformalization](../../docs/papers/10578_The_Signal-Coverage_Matrix_Stratifying_Type_and_Semantic_Err/index.html) — Chengxiao Dai 외, 2026
    - LLM autoformalization의 headline type-correctness(TC%) 향상이 실제로 어떤 오류 유형을 해소하는지 불투명하다는 문제를 지적하며, Lean elaborator의 pass/fail과 semantic-eq…
4. [VeriBench: An End-to-End Formal Verification Benchmark for AI Coding Agents in Lean 4](../../docs/papers/10676_VeriBench_An_End-to-End_Formal_Verification_Benchmark_for_AI/index.html) — Brando Miranda 외, 2026
    - VeriBench는 Python 소스 코드에서 Lean 4 형식 검증 아티팩트로의 end-to-end autoformalization을 평가하는 896개 과제 벤치마크로, SCSC(Smooth Conjunctive Score for Code…

> [!tip] 우리에게 무엇인가
> 컴파일되는 형식화는 이제 쉽다. 진술이 원문과 같은 뜻인지 검증하는 일을 직접 설계해야 한다.

---

## S19 · AI 공동 수학자

*제3부 · 형식 수학 정리 증명* · **Formal Mathematical Theorem Proving** · *서브카테고리*

<sub>타임라인 분석 명칭: Formal Mathematical Theorem Proving / AI Co-Mathematician</sub>

`26편` `2026–2026` `부상` `2025+ 26편`

> [!abstract] 핵심 메시지
> 2026 에이전트가 미해결 문제를 풀고 연구 수준 이론을 Lean으로 형식화하기 시작했다.

- 2026 AlphaProof Nexus가 Erdős 문제 9개와 OEIS 추측 44개를 증명했다.
- 2026.05 AI Co-Mathematician이 FrontierMath Tier 4에서 48%로 SOTA를 달성했다.
- 2026 Vlasov–Maxwell–Landau 평형을 수학자 1명이 10일간 코드 없이 Lean 4로 형식화했다.
- 2026 QED, ReasFlow, Stellar Colosseum이 분해·증명·전역 검증을 멀티에이전트로 구조화했다.
- 배경: HorizonMath는 생성-검증 격차로 발견 능력을 재려는 시도이며, 인간-AI 하이브리드 증명이 병행된다.

**대표 도구·시스템** — AlphaProof Nexus · QED · ReasFlow · MerLean · Stellar Colosseum · HorizonMath · Gemini Deep Think

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Semi-Autonomous Formalization of the Vlasov–Maxwell–Landau Equilibrium](../../docs/papers/10415_Semi-Autonomous_Formalization_of_the_VlasovMaxwellLandau_Equ/index.html) — Vasily Ilin, 2026 · 인용 3,164
    - Gemini DeepThink이 증명을 생성하고 Claude Code가 이를 LEAN 4 코드로 번역하며 Aristotle이 개별 lemma를 자동 증명하는 완전한 AI 보조 연구 파이프라인을 통해, Vlasov-Maxwell-Landau…
2. [Human-AI Hybrid Mathematical Discovery Workflow: Unifying Ramanujan's 17 Series for 1/π](../../docs/papers/9796_Human-AI_Hybrid_Mathematical_Discovery_Workflow_Unifying_Ram/index.html) — Michael Shalyt 외, 2026 · 인용 46
    - Ramanujan의 1/π에 대한 17개 급수 공식을 human-AI hybrid research workflow를 통해 단일 Conservative Matrix Field (CMF) 구조로 통합하는 새로운 elementary proof를…
3. [MerLean: An Agentic Framework for Autoformalization in Quantum Computation](../../docs/papers/532_MerLean_An_Agentic_Framework_for_Autoformalization_in_Quantu/index.html) — Yuanjie Ren 외, 2026.02 · 인용 9
    - 본 논문은 양자계산 이론 논문을 자동으로 기계검증 가능한 Lean 4 코드로 변환하는 완전 자동화 에이전트 프레임워크 MerLean을 제시한다. 3개 양자계산 논문에서 114개 명제로부터 2,050개 Lean 선언을 생성하며 전체 논문의 자…
4. [From LLM-Generated Conjectures to Lean Formalizations: Automated Polynomial Inequality Proving via Sum-of-Squares Certificates](../../docs/papers/9697_From_LLM-Generated_Conjectures_to_Lean_Formalizations_Automa/index.html) — Ruobing Zuo 외, 2026
    - LLM이 생성한 근사 SOS(Sum-of-Squares) 분해 conjecture를 symbolic computation으로 정제하여 정확한 SOS 인증서를 얻고, 이를 Lean으로 형식 검증까지 자동화하는 neuro-symbolic 프레임…

> [!tip] 우리에게 무엇인가
> 연구자의 역할이 증명 작성에서 문제 설정과 검증 책임으로 이동한다. 전담 검증 인력이 필요하다.

---

## S20 · 증명 검증의 아첨

*제3부 · 형식 수학 정리 증명* · **Sycophancy in Proof Verification** · *서브카테고리*

<sub>타임라인 분석 명칭: Sycophancy & Trust in Proof Verification</sub>

`26편` `2023–2026` `가속` `2025+ 24편`

> [!abstract] 핵심 메시지
> LLM 채점자와 자기검증이 틀린 증명을 통과시킨다는 정량 증거가 2026년에 쏟아졌다.

- 2026 QEDBench가 7개 judge와 5개 solver, 인간 전문가 1,000시간 이상으로 judge의 점수 부풀림을 정량화했다.[2]
- 2026 VOUCH는 자기검증이 정답 여부와 무관하게 통과된다는 점을 이론으로 증명하고 두 에이전트 계약으로 해결했다.
- 2026 Pessimistic Verification과 OC-PVerify가 하나의 오류만 찾아도 기각하는 비관적 검증을 도입했다.
- 2026 Model Collapse Despite Ground-Truth Verification은 정확한 검증기가 있어도 모드가 사라질 수 있음을 보였다.[1]
- 배경: 2025 SPOT은 LLM이 출판된 과학 오류를 21% 미만만 회수함을 보였고, BrokenMath는 거짓 정리에 대한 아첨을 정량화했다.[3]

**대표 도구·시스템** — BrokenMath · QEDBench · SPOT · PROOFRANK · MathArena · Recurrence · P4Bench

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Model Collapse Despite Ground-Truth Verification](../../docs/papers/10048_Model_Collapse_Despite_Ground-Truth_Verification/index.html) — Shuo Li Liu, 2026
    - Lean 등 정확한 검증기(verifier)가 모든 남은 산출물(artifact)을 정확히 accept/reject하더라도, 생성 또는 필터링 과정에서 target 분포의 특정 mode가 source 분포에서 아예 사라질 수 있다는 점을 f…
2. [QEDBench: Quantifying the Alignment Gap in Automated Evaluation of University-Level Mathematical Proofs](../../docs/papers/10280_QEDBench_Quantifying_the_Alignment_Gap_in_Automated_Evaluati/index.html) — Santiago Gonzalez 외, 2026
    - 이 논문은 LLM을 자동 채점자(judge)로 사용할 때 대학 수준 수학 증명 평가에서 발생하는 체계적인 정렬 격차(Alignment Gap)를 정량화하는 벤치마크인 QEDBench를 제안한다. 7개의 judge 모델과 5개의 solver…
3. [BrokenMath: A Benchmark for Sycophancy in Theorem Proving with LLMs](../../docs/papers/9359_BrokenMath_A_Benchmark_for_Sycophancy_in_Theorem_Proving_wit/index.html) — Ivo Petrov 외, 2026
    - 이 논문은 자연어 정리 증명(theorem proving) 맥락에서 LLM의 sycophancy(아첨성 행동)를 측정하기 위한 최초의 벤치마크인 BrokenMath를 제안한다. 2025년 고급 수학 경시대회 문제를 LLM으로 변형하여 거짓…
4. [Pessimistic Verification for Open-Ended Math Questions](../../docs/papers/10175_Pessimistic_Verification_for_Open-Ended_Math_Questions/index.html) — Yanxing Huang 외, 2026
    - 본 논문은 수학 증명의 자동 검증(automatic verification)에서 오류 탐지 능력이 핵심 병목이라는 점을 지적하고, 여러 병렬 verifier 중 하나라도 오류를 발견하면 해당 solution을 기각하는 pessimistic…

> [!tip] 우리에게 무엇인가
> LLM 채점자를 단독 검증기로 쓰는 설계는 위험하다. 비관적 검증과 형식 검증을 결합한 이중 장치가 필요하다.

---

## S21 · 다단계 연쇄 추론

*제4부 · LLM 추론·에이전트 벤치마크* · **Multi-Hop Chain-of-Thought Reasoning** · *서브카테고리*

`54편` `2015–2026` `가속` `2025+ 23편`

<sub>LLM 추론·에이전트 벤치마크 고유 배정 284편(중복 포함 1,088편 · 웹 인덱스 기준) · 서브카테고리 10개 · 본 파트 5개로 65% 커버</sub>

> [!quote] 파트 도입
> 무엇을 못하는지 재는 일이 산업이 됐다. 에이전트를 늘려도 나아지지 않는다는 반증까지 같은 해에 쌓였다.

> [!abstract] 핵심 메시지
> 추론은 검색과 결합한 강화학습으로 옮겨갔고, 그 경계를 재는 진단이 함께 붙었다.

- 2025 Search-R1·ReSearch가 추론 도중 검색 호출 시점을 강화학습으로 익혔다. Search-R1은 기존 RAG 대비 최대 41%, ReSearch는 다중 홉 QA에서 8.9~22.4% 향상을 보고했다.[3][4]
- 2025 WebAgent-R1이 종단 간 다중턴 강화학습으로 실제 웹 환경의 장기 의사결정을 학습시켰다. WebDancer·WebWatcher도 같은 흐름이다.
- 2026 GRAIL이 GRPO 기반 RLVR의 시퀀스 단위 advantage를 토큰별 saliency로 재가중해, process reward model 없이 세밀한 정렬을 노렸다.[2]
- 2025–2026 RBF++, DRE-Bench, InvariantBench, Hidden-CoT 탐지가 추론의 경계와 불변성을 진단한다. 2026 Weak Critics Make Strong Learners는 약한 모델을 판정자가 아닌 비판자로 쓴다.[1]
- 배경: 2022 ReAct가 추론 흔적과 행동을 통합했고, 2023 Self-Refine 물결과 '스스로 고치지 못한다'는 반박이 맞섰다.

**대표 도구·시스템** — ReAct · Self-Refine · SelfCheck · Search-R1 · ReSearch · WebDancer · WebAgent-R1 · RBF++ · InvariantBench · GRAIL

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Weak Critics Make Strong Learners: On-Policy Critique Distillation for Scalable Oversight](../../docs/papers/10690_Weak_Critics_Make_Strong_Learners_On-Policy_Critique_Distill/index.html) — Can Jin 외, 2026
    - 약한 모델(weak model)을 정답 제공자나 판단자(labeler/judge)가 아니라 비판자(critic)로 활용해, 강한 모델(strong model)이 스스로의 지식을 더 잘 활용하도록 유도하는 weak-critic strong o…
2. [GRAIL: Gradient-Reweighted Advantages for Reinforcement Learning with Verifiable Rewards](../../docs/papers/9755_GRAIL_Gradient-Reweighted_Advantages_for_Reinforcement_Learn/index.html) — Tej Deep Pala 외, 2026 · 인용 56
    - GRAIL은 GRPO 기반 RLVR에서 시퀀스 단위로 균일하게 부여되던 advantage를 gradient-activation saliency로 토큰별로 재가중하여, 최종 답변에 실제로 기여한 토큰에 더 강한 학습 신호를 주는 방법이다. 이…
3. [Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement Learning](../../docs/papers/740_Search-R1_Training_LLMs_to_Reason_and_Leverage_Search_Engine/index.html) — Bowen Jin 외, 2025 · 인용 12
    - 강화학습(RL)을 통해 대언어모델(LLM)이 추론 과정 중 검색 엔진을 자동으로 호출하고 활용하는 방법을 학습하는 프레임워크 Search-R1을 제안하며, 기존 RAG 대비 최대 41%의 성능 향상을 달성한다.
4. [ReSearch: Learning to Reason with Search for LLMs via Reinforcement Learning](../../docs/papers/667_ReSearch_Learning_to_Reason_with_Search_for_LLMs_via_Reinfor/index.html) — Mingyang Chen 외, 2025 · 인용 10
    - ReSearch는 강화학습(RL)을 통해 대규모 언어모델(LLM)이 추론 과정 중 언제 어떻게 검색을 수행할지를 자동으로 학습하는 프레임워크이다. 감독 데이터 없이 검색 쿼리, 텍스트 기반 사고(thinking), 검색 결과를 통합한 추론…

> [!tip] 우리에게 무엇인가
> 추론 성능을 올리는 레시피는 공개돼 있다. 국내에서 모자란 것은 한국어·국내 도메인에서 추론이 어디서 무너지는지 재는 자체 진단 벤치마크다.

---

## S22 · 에이전트 기억·계획

*제4부 · LLM 추론·에이전트 벤치마크* · **Agent Skill Memory Planning** · *서브카테고리*

`39편` `2023–2026` `가속` `2025+ 31편`

> [!abstract] 핵심 메시지
> 에이전트의 병목이 '한 번 푸는 능력'에서 '길게 일관되게 수행하는 능력'으로 옮겨갔다.

- 2026 YC-Bench가 1년·수백 턴에 걸쳐 시뮬레이션 스타트업을 운영시켜 장기 계획과 일관된 실행을 잰다. 불충실한 클라이언트와 증가하는 급여 비용 같은 적대적 환경이다.[1]
- 2025 A-MEM이 Zettelkasten 원리로 새 기억이 들어올 때 맥락 연결을 만들고 기존 기억을 진화시킨다. 2026 SkillX는 GLM-4.6에서 3단계 계층의 skill knowledge base를 자동 구축한다.[2]
- 2025 Text2world가 PDDL 기반으로 기호적 세계 모델 생성을 평가했고, 현재 LLM의 세계 모델링 능력이 여전히 제한적임을 밝혔다.
- 2026 Deadline-Valid Replay, 입자 필터 기반 온라인 모니터링이 리더보드 차이가 통계적으로 의미 있는지, 추론 궤적이 건전한지를 순차 검정으로 따진다.[3]
- 배경: 2023 Tree-Planner, HiAgent, Agent S가 계층적 폐루프 계획과 작업 기억 관리의 틀을 놓았다.

**대표 도구·시스템** — Agent S · HiAgent · Tree-Planner · A-MEM · SkillX · Vending-Bench · YC-Bench · Text2World · TEMPO · E-valuator

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [YC-Bench: Benchmarking AI Agents for Long-Term Planning and Consistent Execution](../../docs/papers/3398_YC-Bench_Benchmarking_AI_Agents_for_Long-Term_Planning_and_C/index.html) — Muyu He 외, 2026 · 인용 1,873
    - YC-Bench는 LLM 에이전트의 장기 계획과 일관된 실행 능력을 평가하기 위한 벤치마크로, 1년 동안 수백 턴을 거쳐 시뮬레이션된 스타트업을 운영하도록 하는 POMDP 기반 환경을 제공한다. 불충실한 클라이언트와 증가하는 급여 비용 등…
2. [SkillX: Automatically Constructing Skill Knowledge Bases for Agents](../../docs/papers/10451_SkillX_Automatically_Constructing_Skill_Knowledge_Bases_for/index.html) — Chenxi Wang 외, 2026 · 인용 124
    - SkillX는 LLM 에이전트가 개별적으로 경험을 학습하는 self-evolving 패러다임의 비효율성을 극복하기 위해, 강력한 backbone agent(GLM-4.6)로부터 재사용 가능한 plug-and-play skill knowled…
3. [Deadline-Valid Replay: Anytime-Valid Testing for LLM Inference Policies](../../docs/papers/9482_Deadline-Valid_Replay_Anytime-Valid_Testing_for_LLM_Inferenc/index.html) — Rui Gao, 2026 · 인용 74
    - 이 논문은 LLM inference policy(예: greedy, self-consistency, budget branch, selective abstain) 간의 비교를 deadline 조건 하에서 paired sequential tes…
4. [Cocoa: Co-planning and co-execution with AI Agents](../../docs/papers/229_Cocoa_Co-planning_and_co-execution_with_ai_agents/index.html) — K. J. Kevin Feng 외, 2026 · 인용 6
    - Cocoa는 과학 연구자를 위한 문서 편집기 환경에서 AI agent와의 co-planning(공동 계획)과 co-execution(공동 실행)을 인터리빙하여 유연한 human-agent 협업을 지원하는 인터랙티브 시스템이다.

> [!tip] 우리에게 무엇인가
> 에이전트 도입 평가는 단발 정확도가 아니라 장기 일관성과 통계적 유의성으로 해야 한다. 이 두 축의 평가 설계가 곧 도입 판단 역량이다.

---

## S23 · 임상 추론 에이전트

*제4부 · LLM 추론·에이전트 벤치마크* · **Clinical Reasoning Agents & Rewards** · *서브카테고리*

`33편` `2023–2026` `가속` `2025+ 30편`

> [!abstract] 핵심 메시지
> 임상 추론은 단일 거대 모델에서 역할 분담형 에이전트와 단계별 보상으로 옮겨갔다.

- 2026 Salus가 감별진단을 다중 라운드 순차 의사결정으로 정식화한 CompDiag-Bench를 내놓고, Differential Reasoner 등 세 에이전트로 풀었다.
- 2026 Small Agent Group이 소형 LLM 협업 집단이 임상 추론의 효과·신뢰성·배포 비용에서 단일 거대 모델을 능가할 수 있음을 실증했다.
- 2026 Process Reward Agents와 Resp-GRASP가 추론 단계를 실시간으로 검증하거나 근거 인용·가드레일로 묶는다. 호흡 신호 해석에서 COPD 악화 탐지의 false positive를 줄이려 했다.
- 2026 EHR-ReasonCon은 MIMIC-III 기반 8,048개 entity로 노트와 구조화 표의 일관성을 검증하고, FHIR-Hopper와 PopMedQA는 EHR 장문맥 문제를 다룬다.[2]
- 비판 신호: 2026 The Consistency Dilemma — 10개 최신 모델·491개 개념에서 자기일관성이 높은 모델일수록 임상 환경에서 실수에 더 취약했다.

**대표 도구·시스템** — MedAgents · Agent Hospital · MedAgentGym · InfiMed-ORBIT · DR Tulu · GLEAN · HetMedAgent · Salus · FHIR-Hopper

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Reinforcement Learning for Tool-Calling Agents in Fast Healthcare Interoperability Resources (FHIR)](../../docs/papers/10319_Reinforcement_Learning_for_Tool-Calling_Agents_in_Fast_Healt/index.html) — Marius Knorr 외, 2026 · 인용 420
    - FHIR 그래프 상에서 임상 질의응답을 수행하는 tool-calling agent를 CodeAct 방식으로 구현하고, GRPO 기반 강화학습으로 post-training하여 FHIR-AgentBench에서 정답률을 o4-mini의 50%에서…
2. [FHIR-Hopper: A Neuro-Symbolic Agent for Reasoning over EHRs](../../docs/papers/9645_FHIR-Hopper_A_Neuro-Symbolic_Agent_for_Reasoning_over_EHRs/index.html) — Chanwoo Kim 외, 2026 · 인용 104
    - FHIR-Hopper는 FHIR 번들을 episodic chronological graph로 변환하고, 토큰 예산 내에서 saliency 기반 linearization(SBL)을 초기 컨텍스트로 제공한 뒤 결정론적 graph-traversa…
3. [Process Reward Agents for Steering Knowledge-Intensive Reasoning](../../docs/papers/10251_Process_Reward_Agents_for_Steering_Knowledge-Intensive_Reaso/index.html) — Jiwoong Sohn 외, 2026 · 인용 11
    - 지식집약적(knowledge-intensive) 추론에서 중간 단계를 실시간으로 검증하고 보상을 제공하는 inference-time 에이전트인 Process Reward Agent (PRA)를 제안하여, frozen policy 모델의 re…
4. [MedAgentGym: A Scalable Agentic Training Environment for Code-Centric Reasoning in Biomedical Data Science](../../docs/papers/528_MedAgentGym_A_Scalable_Agentic_Training_Environment_for_Code/index.html) — Ran Xu 외, 2025.06
    - 본 논문은 생의학 데이터 과학(biomedical data science)에서 코드 기반 추론 능력을 강화하기 위한 확장 가능한 LLM 에이전트 훈련 환경인 MedAgentGym을 제시한다. 72,413개의 과제 인스턴스와 실행 가능한 샌드…

> [!tip] 우리에게 무엇인가
> 임상 AI는 정확도 하나로 승인할 수 없다. 의료기관과 규제기관은 실패 모드 평가와 임상의 개입 지점 설계를 요건으로 삼아야 한다.

---

## S24 · 표·데이터 추론

*제4부 · LLM 추론·에이전트 벤치마크* · **Table Reasoning Intelligence Benchmarks** · *서브카테고리*

`30편` `2023–2026` `가속` `2025+ 17편`

> [!abstract] 핵심 메시지
> 표 이해는 데이터 과학 에이전트 평가로 확장됐고, 다중 에이전트의 가치는 도전받는다.

- 2025 ToRR가 10개 데이터셋으로 14개 주요 LLM을 평가해, 최신 모델도 표 형식 변화에 취약한 brittle 행동을 보임을 확인했다.
- 2025 DeepAnalyze-8B가 원시 데이터에서 분석 보고서까지 자동화한 첫 에이전틱 LLM으로, 8B 파라미터로 독점 LLM 기반 워크플로우 에이전트를 능가했다.[4]
- 2026 DDR-Bench가 질문 없이 데이터베이스에서 스스로 탐색 목표를 세우는 investigatory intelligence를 검증 가능하게 잰다.
- 2026 AFDBench가 7,732개 전문가 작성 예보문으로 AI 기상 예보 해설을, QuantumQUBO Agent의 QUBOBench가 QUBO 공식화를 평가한다.[1]
- 비판 신호: 2026.01 OneFlow — 같은 base LLM의 동질적 다중 에이전트 워크플로우를 KV cache 공유 단일 에이전트의 다중턴 대화로 재현했다.

**대표 도구·시스템** — AutoGen · Data Interpreter · AutoKaggle · DiscoveryBench · BLADE · DSBench · ToRR · TableMaster · DeepAnalyze · OneFlow

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [QuantumQUBO Agent: Automating Quadratic Unconstrained Binary Optimization (QUBO) Formulation Generation from Natural Language](../../docs/papers/10289_QuantumQUBO_Agent_Automating_Quadratic_Unconstrained_Binary/index.html) — Niloy Kumar Mondal 외, 2026 · 인용 8,635
    - 자연어로 기술된 조합 최적화 문제 설명을 자동으로 QUBO(Quadratic Unconstrained Binary Optimization) 공식으로 변환하는 end-to-end multi-agent framework를 제안하고, 이를 평가하…
2. [R&D-Agent: Automating Data-Driven AI Solution Building Through LLM-Powered Automated Research, Development, and Evolution](../../docs/papers/650_RD-Agent_Automating_Data-Driven_AI_Solution_Building_Through/index.html) — Xu Yang 외, 2025.05 · 인용 1
    - 본 논문은 LLM 기반의 이중 에이전트 프레임워크인 R&D-Agent를 제안하여, 데이터 과학 솔루션 개발을 자동화하고 전문가 수준의 성능에 근접하도록 설계했다. 연구자 에이전트는 성능 피드백을 바탕으로 아이디어를 생성하고, 개발자 에이전트…
3. [The mighty torr: A benchmark for table reasoning and robustness](../../docs/papers/802_The_mighty_torr_A_benchmark_for_table_reasoning_and_robustne/index.html) — Shir Ashury-Tahan 외, 2025
    - 본 논문은 ToRR(Table Reasoning and Robustness) 벤치마크를 제시하여, 대규모 언어모델(LLM)의 표 데이터 이해 능력과 다양한 표 형식에 대한 견고성(robustness)을 체계적으로 평가한다. 10개의 데이터셋…
4. [DeepAnalyze: Agentic Large Language Models for Autonomous Data Science](../../docs/papers/259_DeepAnalyze_Agentic_Large_Language_Models_for_Autonomous_Dat/index.html) — Shaolei Zhang 외, 2025.10
    - 본 논문은 원시 데이터에서 분석가급 심층 연구 보고서까지 완전 자동화된 데이터 과학(autonomous data science)을 달성하는 최초의 에이전틱 LLM인 DeepAnalyze-8B를 제안한다. 단 8B 파라미터로 고급 독점 LLM…

> [!tip] 우리에게 무엇인가
> 데이터 분석 에이전트 도입 전에 표 형식 변화에 대한 견고성과 단일 에이전트 대비 비용 효과를 먼저 재야 한다.

---

## S25 · 주장 검증

*제4부 · LLM 추론·에이전트 벤치마크* · **Claim Verification & Misinformation Detection** · *서브카테고리*

`29편` `2021–2026` `안정` `2025+ 10편`

> [!abstract] 핵심 메시지
> 주장 검증은 사실 대조에서 반박 증거 검색, 통계적 감사, 지식 삭제 검증으로 확장됐다.

- 2025 SciClaimHunt가 87,109개 주장과 이를 지지·반박하는 과학 논문 증거로 구성된 대규모 데이터셋을 공개했다.[2]
- 2025 CIBER가 지지 증거와 반박 증거를 함께 검색해 과학 주장을 검증하고, 질문 프로브로 응답 일관성을 평가해 환각을 완화한다.
- 2025 Claimify가 장문 LLM 생성물의 주장 추출 품질을 평가하는 표준 틀과 모호성 처리 방법을 제시했다. SciClaims는 SLR·특허 검증을 지원한다.[4]
- 2026 jailbreak 탐지기 감사가 가설검정으로 재해석돼 다섯 벤더의 production 분류기를 점검했고, SciUnlearn은 unlearning이 claim 수준 지식을 못 지움을 보였다.
- 배경: 2022 연구는 실제 허위정보에는 반박 증거가 부족해 기존 사실 확인 데이터셋이 비현실적이라고 지적했다.

**대표 도구·시스템** — MultiVers · ProgramFC · FactKG · ClaimVer · HiSS · SciClaimHunt · Claimify · CIBER · BioKGBench

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Explainable biomedical claim verification with large language models](../../docs/papers/328_Explainable_biomedical_claim_verification_with_large_languag/index.html) — Siting Liang 외, 2025 · 인용 54
    - 대규모 언어 모델(LLM)과 SHAP 설명가능성을 결합하여 의료 주장 검증의 투명성을 높이는 대화형 시스템을 제시한다. 사용자는 과학 문헌에서 관련 연구를 검색하고, CoENLI 프레임워크를 통해 LLM의 추론 과정을 검토하며, SHAP 값…
2. [Sciclaimhunt: A large dataset for evidence-based scientific claim verification](../../docs/papers/710_Sciclaimhunt_A_large_dataset_for_evidence-based_scientific_c/index.html) — Sujit Kumar 외, 2025 · 인용 35
    - 본 논문은 과학 논문에서 추출한 대규모 научных 주장 검증 데이터셋 SciClaimHunt와 SciClaimHunt Num을 소개한다. 정치적 주장과 달리 과학적 주장의 검증은 도메인 전문성과 복잡한 기술 용어를 요구하는 고도의 과제이…
3. [LLM-based Corroborating and Refuting Evidence Retrieval for Scientific Claim Verification](../../docs/papers/500_Llm-based_corroborating_and_refuting_evidence_retrieval_for/index.html) — Siyuan Wang 외, 2025
    - CIBER는 검색 증강 생성(RAG) 프레임워크를 확장하여 과학적 주장(claim)을 검증하기 위해 지지 증거와 반박 증거를 체계적으로 식별하고 검색하는 프레임워크이다. 다양한 질문 프로브(probe)를 통해 LLM의 응답 일관성을 평가함으…
4. [SciClaims: An end-to-end generative system for biomedical claim analysis](../../docs/papers/711_Sciclaims_An_end-to-end_generative_system_for_biomedical_cla/index.html) — Raúl Ortega 외, 2025
    - SciClaims는 생의학 텍스트에서 과학적 주장을 자동으로 추출하고, PubMed에서 관련 증거를 검색한 후, 단일 대규모 언어모델(LLM)을 사용하여 검증하는 통합 시스템이다. 체계적 문헌고찰(Systematic Literature Re…

> [!tip] 우리에게 무엇인가
> 연구 무결성과 정보 신뢰성 인프라에서 검증 도구는 증거 부족 상황과 지식 삭제의 실효성까지 시험해야 한다. 한국어 주장 검증 데이터는 직접 쌓아야 한다.

---

## S26 · 물리 기반 신경 연산자

*제5부 · 물리 기반 신경 시뮬레이션* · **Physics-Informed Neural Operators** · *서브카테고리*

`66편` `2017–2026` `가속` `2025+ 58편`

<sub>물리 기반 신경 시뮬레이션 고유 배정 272편(중복 포함 572편 · 웹 인덱스 기준) · 서브카테고리 9개 · 본 파트 5개로 75% 커버</sub>

> [!quote] 파트 도입
> 신경 시뮬레이터의 경쟁축이 속도에서 보장(guarantee)과 실패 모드 진단으로 옮겨갔다.

> [!abstract] 핵심 메시지
> 2026의 질문은 '얼마나 빠른가'가 아니라 'PINN과 연산자가 왜, 어디서 실패하는가'다.

- 2026 Mitigating Gradient Pathology in PINNs through Aligned Constraint가 gradient pathology의 원인을 손실 함수 공간의 기하로 규명하고 교정한다.[1]
- 2026 On the Role of Consistency Between Physics and Data in PINNs가 데이터와 PDE의 불일치가 정확도 하한을 정하는 consistency barrier를 형식화했다.[1]
- 2026 cd-PINN은 해의 연속 의존성을 활용해 라벨이 적어도 DeepONet·FNO 대비 1-3 자릿수 낮은 오차를 보고한다.[1]
- 2025 Discovery of Unstable Singularities가 3D Euler·Boussinesq에서 불안정 특이점을 ML과 고정밀 수치해석으로 처음 체계 발견했다.[2]
- 배경: 2017 PINN, 2018 Neural ODE가 출발점이고 2023 FNO 사전학습·전이 스케일링이 파운데이션 모델 논의를 열었다.[1]

**대표 도구·시스템** — PINN · DeepONet · FNO · PINO · Neural ODE · Neural-HSS · Origo · SLE-FNO · Neural-POD · Hyperbolic Neural Operator

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Mitigating Gradient Pathology in PINNs through Aligned Constraint](../../docs/papers/10037_Mitigating_Gradient_Pathology_in_PINNs_through_Aligned_Const/index.html) — Yichen Luo 외, 2026
    - 본 논문은 PINNs(Physics-Informed Neural Networks) 학습을 저해하는 gradient pathology의 근본 원인을 PDE 잔차 손실의 함수 공간 내 연결된 global minimizer manifold로부터…
2. [Discovery of Unstable Singularities](../../docs/papers/276_Discovery_of_Unstable_Singularities/index.html) — Yongji Wang 외, 2025.09 · 인용 17
    - 기계학습과 고정밀 수치해석을 결합하여 3D 오일러 방정식, 비압축성 다공질 매질 방정식, Boussinesq 방정식에서 처음으로 불안정 특이점(unstable singularities)의 체계적인 발견을 보여주는 연구이다. 불안정 특이점은…
3. [MENO: MeanFlow-Enhanced Neural Operators for Dynamical Systems](../../docs/papers/3165_MENO_MeanFlow-Enhanced_Neural_Operators_for_Dynamical_System/index.html) — 2026.04 · 인용 1,051
    - 신경 연산자(Neural Operator)와 개선된 MeanFlow(i-MF) 생성 모델을 결합하여 동역학계의 다중 스케일 거동을 정확히 예측하면서 확산 모델 대비 12배 빠른 추론을 달성하는 하이브리드 프레임워크 MENO를 제안한다.
4. [Neural Modular Physics for Elastic Simulation](../../docs/papers/10093_Neural_Modular_Physics_for_Elastic_Simulation/index.html) — Yifei Li 외, 2026 · 인용 560
    - 본 논문은 elastic simulation을 위한 Neural Modular Physics (NMP) 프레임워크를 제안하며, 전통적 numerical simulator의 modular한 계산 흐름(constitutive model, tim…
5. [Solving Stiff Dark Matter Equations via Jacobian Normalization with Physics-Informed Neural Networks](../../docs/papers/3242_Solving_Stiff_Dark_Matter_Equations_via_Jacobian_Normalizati/index.html) — 2026.02 · 인용 458
    - Physics-Informed Neural Networks(PINN)에서 Jacobian 정규화 기법을 적용하여 강성 미분방정식을 안정적으로 해결하고, 이를 WIMP 암흑물질의 Boltzmann 방정식에 적용함.

> [!tip] 우리에게 무엇인가
> PINN 도입 검토 시 성능 수치보다 실패 영역 진단 결과를 먼저 요구해야 한다. 국내 해석·시뮬레이션 조직은 전통 솔버 대비 벤치마크를 내부 표준으로 삼을 시점이다.

---

## S27 · 동역학계 flow matching

*제5부 · 물리 기반 신경 시뮬레이션* · **Flow Matching for Dynamical Systems** · *서브카테고리*

`46편` `2020–2026` `가속` `2025+ 45편`

> [!abstract] 핵심 메시지
> flow matching이 궤적 추론과 PDE 풀이의 표준 생성 골격이 됐고, 한두 단계 추론이 목표가 됐다.

- 2026 MENO는 신경 연산자와 개선된 MeanFlow(i-MF)를 결합해 확산 모델 대비 12배 빠른 추론을 달성했다.
- 2026 STFlow와 SE(3)-Equivariant Flow Matching with Gaussian Process Priors가 데이터 종속 prior로 N-body·분자 궤적을 예측한다.[3][4]
- 2026 Multimarginal flow matching with optimal transport potentials, MMtSBM, PACE가 스냅샷만으로 궤적을 추론한다.[1]
- 2026 Particle-Guided Diffusion Models for PDEs와 Physics-Informed Distillation이 PDE 잔차 guidance와 Jensen's Gap 문제를 다룬다.[2]
- 배경: 2020 시뮬레이션 기반 추론(simulation-based inference)이 하나의 분야로 굳어지며 생성 모델 적용의 토대가 됐다.

**대표 도구·시스템** — OTP-FM · WFR-MFM · STFlow · GP-EquiFlow · Recursive Flow Matching · Latent Generative Solver · MENO · TFMPE · FUSE · LieStoNet

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Multimarginal flow matching with optimal transport potentials](../../docs/papers/10073_Multimarginal_flow_matching_with_optimal_transport_potential/index.html) — Raghav Kansal 외, 2026
    - multimarginal 궤적 추론 문제를 dynamic optimal transport(OT)에 potential energy 항을 추가하는 방식으로 완화하여, 중간 marginal에 대해 soft하게 정렬되면서도 simulation-fr…
2. [Particle-Guided Diffusion Models for Partial Differential Equations](../../docs/papers/10158_Particle-Guided_Diffusion_Models_for_Partial_Differential_Eq/index.html) — Andrew Millard 외, 2026
    - Diffusion model 기반 생성적 PDE 솔버에 PDE residual과 관측 제약을 기반으로 한 physics-based guidance를 결합하고, 이를 새로운 Sequential Monte Carlo (SMC) 프레임워크에 내장…
3. [SE(3)-Equivariant Flow Matching with Gaussian Process Priors for Geometric Trajectory Prediction](../../docs/papers/10398_SE3-Equivariant_Flow_Matching_with_Gaussian_Process_Priors_f/index.html) — Xuyang Wang 외, 2026
    - N-body 시스템의 궤적 예측을 위해, 관측된 과거 궤적으로부터 vector-valued Gaussian process(VVGP)를 이용해 시간적 상관관계와 SE(3) 대칭성을 모두 반영하는 데이터 종속적 prior 분포를 구성하고, 이를…
4. [STFlow: Data-Coupled Flow Matching for Geometric Trajectory Simulation](../../docs/papers/10501_STFlow_Data-Coupled_Flow_Matching_for_Geometric_Trajectory_S/index.html) — Kiet Bennema ten Brinke 외, 2026 · 인용 12
    - STFlow는 N-body 시스템, 분자동역학, 보행자 궤적 예측 등 기하학적 궤적(geometric trajectory) 시뮬레이션을 위해 Flow Matching 프레임워크에 data-dependent coupling을 도입하여, Gau…
5. [LieStoNet: Learning Lie Symmetries from Spatiotemporal Data for Stochastic Dynamical Systems](../../docs/papers/9943_LieStoNet_Learning_Lie_Symmetries_from_Spatiotemporal_Data_f/index.html) — Shida Liu 외, 2026
    - LieStoNet은 확률미분방정식(SDE)의 궤적 데이터만으로부터 사전에 대칭군, 템플릿, 정준 좌표를 지정하지 않고 Lie-point symmetry generator를 종단간(end-to-end)으로 발견하는 프레임워크이다. Gaeta…
6. [FUSE: FK-Steered Multi-Modal Flow Matching for Efficient Simulation-Based Posterior Estimation](../../docs/papers/9710_FUSE_FK-Steered_Multi-Modal_Flow_Matching_for_Efficient_Simu/index.html) — Weichen Qin 외, 2026 · 인용 994
    - FUSE는 dual-track 아키텍처와 FK-steered sampling을 결합한 flow matching 기반 방법으로, parameter와 observation의 구조적 차이를 보존하면서 posterior 추정 정확도와 효율성을 동시…

> [!tip] 우리에게 무엇인가
> 생성 기반 PDE 풀이는 한두 단계 추론으로 실용권에 들어왔다. 다만 guidance가 만드는 편향을 점검하는 절차 없이는 검증 가능한 시뮬레이터로 보기 어렵다.

---

## S28 · 확산 기반 자료동화

*제5부 · 물리 기반 신경 시뮬레이션* · **Diffusion-Based Data Assimilation** · *서브카테고리*

`33편` `2026–2026` `부상` `2025+ 33편`

> [!abstract] 핵심 메시지
> 생성 prior가 희소 센서 복원에서 변분 동화를 대체하기 시작했고, 신뢰도 보증이 따라붙는다.

- 2026 SENDAI는 1.56% 커버리지의 초희소 센서 관측만으로 위성 NDVI 필드를 복원한다.[3]
- 2026 Di-BiLPS가 최소 3%의 희소 관측에서 forward·inverse PDE 문제를 잠재 공간 확산으로 푼다.
- 2026 Plug-and-Play Diffusion Meets ADMM이 PnP diffusion의 steady-state bias를 dual variable로 교정한다.[1]
- 2026 Principled Confidence Estimation for Deep Computed Tomography가 이론적 coverage를 갖춘 신뢰구간을 제시한다.[2]
- 배경: 이 칸은 타임라인이 2026년에 시작돼 상태가 EMERGING이고, 변분 동화를 생성 prior로 대체하려는 시도가 막 모였다.

**대표 도구·시스템** — DAISI · GenDA · SENDAI · LoPhyDA · PODiff · PIDDM · DC-PnPDP · ANTiC · AnyBand-Diff · WIND

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Plug-and-Play Diffusion Meets ADMM: Dual-Variable Coupling for Robust Medical Image Reconstruction](../../docs/papers/10205_Plug-and-Play_Diffusion_Meets_ADMM_Dual-Variable_Coupling_fo/index.html) — Chenhe Du 외, 2026
    - 기존 PnP diffusion prior 솔버가 memoryless한 P-controller처럼 동작하여 steady-state bias가 발생함을 지적하고, ADMM의 dual variable을 재도입해 integral feedback을…
2. [Principled Confidence Estimation for Deep Computed Tomography](../../docs/papers/10239_Principled_Confidence_Estimation_for_Deep_Computed_Tomograph/index.html) — Matteo Gätzner 외, 2026
    - 이 논문은 sequential likelihood mixing framework를 CT 재구성에 적용하여, Beer-Lambert 법칙과 Poisson noise를 반영한 realistic forward model 하에서 이론적 covera…
3. [SENDAI: A Hierarchical Sparse-measurement, EfficieNt Data AssImilation Framework](../../docs/papers/10422_SENDAI_A_Hierarchical_Sparse-measurement_EfficieNt_Data_AssI/index.html) — Xingyue Zhang 외, 2026
    - SENDAI는 초희소(1.56% 커버리지) 센서 관측만으로 위성 기반 식생지수(NDVI) 필드를 재구성하기 위해, simulation 유래 저주파 사전(prior)과 학습 기반 고주파 불일치 보정(discrepancy correction)을…
4. [GenDA: Generative Data Assimilation on Complex Urban Areas via Classifier-Free Diffusion Guidance](../../docs/papers/9717_GenDA_Generative_Data_Assimilation_on_Complex_Urban_Areas_vi/index.html) — Francisco Giral 외, 2026
    - GenDA는 unstructured mesh 상에서 희소 센서 관측으로부터 고해상도 도시 풍속장을 재구성하는 generative data assimilation 프레임워크로, multiscale graph-based diffusion 모델과…
5. [LoPhyDA: Low-Rank Tensor and Physics Gradient Guided Diffusion for Atmospheric Data Assimilation](../../docs/papers/9971_LoPhyDA_Low-Rank_Tensor_and_Physics_Gradient_Guided_Diffusio/index.html) — Danyang Peng 외, 2026
    - 희소한 관측치로부터 low-rank tensor completion을 통해 전역적으로 조밀한 사전 필드를 복원하고, 이를 PDE 기반 physics gradient와 함께 diffusion 기반 data assimilation의 revers…

> [!tip] 우리에게 무엇인가
> 관측망이 성긴 환경·위성 분야에서 생성 prior 기반 복원이 후보 기술이다. 복원 결과의 신뢰구간과 적대적 강건성이 도입 조건이 된다.

---

## S29 · 수치 기상 예보

*제5부 · 물리 기반 신경 시뮬레이션* · **Numerical Weather Forecasting** · *서브카테고리*

`31편` `2022–2026` `가속` `2025+ 28편`

> [!abstract] 핵심 메시지
> AI 예보가 운용 NWP를 넘어선 뒤, 경쟁은 스케일링 법칙·하이브리드·해석가능성으로 옮겨갔다.

- 2026 Scaling Laws of Global Weather Models가 GraphCast, AIFS, Aurora, Pangu, SFNO의 모델·데이터·연산 스케일링을 비교했다.[1]
- 2026 HITS는 자기회귀 예측에 글로벌 모형의 동역학적 제약을 결합한 아시아-태평양 태풍 중기 예보를 제시했다.
- 2026 O-CNOPs와 FuXi를 결합한 앙상블이 물리적으로 일관된 섭동으로 열대 저기압 추적을 개선한다.
- 2026 climt-paraformer가 시간 메모리 트랜스포머로 대류 서브그리드 과정 에뮬레이션의 안정성을 높였다.
- 배경: 2022 Pangu-Weather가 운용 NWP를 넘은 첫 AI 모델이 됐고, 2023 GraphCast·FuXi가 중장기 전역 skill을 보였다.

**대표 도구·시스템** — Pangu-Weather · GraphCast · FuXi · U-Cast · MOSAIC · EMFormer · FloeNet · HybridOM · ClimateAR · WEATHER-5K

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Scaling Laws of Global Weather Models](../../docs/papers/10376_Scaling_Laws_of_Global_Weather_Models/index.html) — Yuejiang Yu 외, 2026
    - 본 논문은 데이터 기반 전지구 기상예측 모델(GraphCast, AIFS, Aurora, Pangu, SFNO)에 대해 model size(N), dataset size(D), compute budget(C)에 따른 scaling law를…
2. [U-Cast: A Surprisingly Simple and Efficient Frontier Probabilistic AI Weather Forecaster](../../docs/papers/10652_U-Cast_A_Surprisingly_Simple_and_Efficient_Frontier_Probabil/index.html) — Salva Rühling Cachay 외, 2026
    - U-Cast는 표준 U-Net 백본에 MAE 사전학습 후 CRPS 미세조정, 그리고 MC Dropout 기반 확률화라는 단순한 3단계 레시피만으로 GenCast 및 IFS ENS 수준의 확률적 일기예보 성능을 10배 이상 적은 학습·추론 비…
3. [EMFormer: Efficient Multi-Scale Transformer for Accumulative Context Weather Forecasting](../../docs/papers/9580_EMFormer_Efficient_Multi-Scale_Transformer_for_Accumulative/index.html) — Hao Chen 외, 2026
    - EMFormer는 사전학습-미세조정-예측 파이프라인 전반에 걸쳐, 단일 convolution으로 multi-scale 특징을 추출하는 효율적 Transformer 구조와 누적 컨텍스트 finetuning, sinusoidal weighted…
4. [(Sparse) Attention to the Details: Preserving Spectral Fidelity in ML-based Weather Forecasting Models](../../docs/papers/10472_Sparse_Attention_to_the_Details_Preserving_Spectral_Fidelity/index.html) — Maksim Zhdanov 외, 2026
    - MOSAIC는 ML 기반 기상 예측에서 발생하는 세 가지 스펙트럼 저하 문제(통계적 스펙트럼 감쇠, 구조적 고주파 앨리어싱, 파라메트릭 고주파 잔차 누출)를 동시에 해결하는 probabilistic weather forecasting mod…

> [!tip] 우리에게 무엇인가
> 전지구 AI 예보 모델은 이미 기성품이다. 국내 차별점은 태풍·에어로졸 같은 지역 문제의 하이브리드화와 운용 검증 체계에 있다.

---

## S30 · 로봇 조작·제어

*제5부 · 물리 기반 신경 시뮬레이션* · **Robotic Manipulation & Control** · *서브카테고리*

`27편` `2023–2026` `가속` `2025+ 24편`

> [!abstract] 핵심 메시지
> 신경 시뮬레이터와 연산자 정책이 로봇 제어에 들어왔고, 물리를 정말 아는지 묻는 감사가 함께 등장했다.

- 2026 SoMA가 3D Gaussian Splat 위에서 로봇 행동·환경 힘·변형체 동역학을 결합한 real-to-sim 신경 시뮬레이터를 제시했다.[2]
- 2026 CINOC는 센서·액추에이터 수가 바뀌어도 재학습 없이 동작하는 신경 연산자 PDE 제어 정책이다.[3]
- 2026 ENPIRE가 coding agent로 실제 로봇 정책을 폐루프에서 자동 개선한다.
- 2025 inductive-bias 탐침과 From Kepler to Newton이 파운데이션 모델이 세계 모델을 갖는지 의문을 제기했다.[1]
- 배경: 2024 SHAC-ASAM 등 미분 가능 시뮬레이터 기반 1차 정책 경사 방법이 이 흐름의 출발점이다.

**대표 도구·시스템** — SHAC-ASAM · SoMA · 3DGSim · DLO-Lab · CINOC · NeuronCtrl · ENPIRE · Debate2Create · Morpheus · TC-Bench

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [From Kepler to Newton: Inductive Biases Guide Learned World Models in Transformers](../../docs/papers/9696_From_Kepler_to_Newton_Inductive_Biases_Guide_Learned_World_M/index.html) — Ziming Liu 외, 2026 · 인용 12
    - 본 논문은 transformer가 행성 운동 데이터를 학습할 때 뉴턴 세계 모델을 습득하지 못하는 원인을 규명하고, spatial smoothness, spatial stability, temporal locality라는 세 가지 최소한의…
2. [SoMA: A Real-to-Sim Neural Simulator for Robotic Soft-Body Manipulation](../../docs/papers/10467_SoMA_A_Real-to-Sim_Neural_Simulator_for_Robotic_Soft-Body_Ma/index.html) — Mu Huang 외, 2026
    - SoMA는 3D Gaussian Splat 표현 위에서 로봇의 joint-space action, 환경 힘, 변형체 동역학을 하나의 latent neural space로 결합하여, real-world 로봇 매니퓰레이션 영상으로부터 end-t…
3. [CINOC: Cardinality-Invariant Neural Operator Policies for Scalable PDE Control](../../docs/papers/9401_CINOC_Cardinality-Invariant_Neural_Operator_Policies_for_Sca/index.html) — Pietro Zanotta 외, 2026
    - PDE 상태 필드를 연속 제어 함수로 매핑하는 neural operator를 differentiable PDE solver를 통해 end-to-end로 학습시켜, 센서·액추에이터·에이전트 수가 바뀌어도 재학습 없이 동작하는 cardinali…
4. [Value iteration for learning concurrently executable robotic control tasks](../../docs/papers/863_Value_iteration_for_learning_concurrently_executable_robotic/index.html) — Sheikh A. Tahmid 외, 2025 · 인용 244
    - 중복도(redundancy)를 가진 로봇 시스템이 여러 제어 태스크를 동시에 실행할 수 있도록 강화학습(RL)으로 학습된 가치 함수들 간의 독립성(independence)을 정의하고, 이를 만족하도록 학습하는 새로운 방법을 제안한다. 제안된…

> [!tip] 우리에게 무엇인가
> 로봇 정책 학습의 병목이 데이터에서 시뮬레이터 충실도로 옮겨간다. 실물-시뮬레이션 격차(gap)를 수치로 보고하는 팀이 신뢰를 얻는다.

---

## S31 · EHR 파운데이션 모델

*제6부 · 의료·신경 신호 모델링* · **EHR Foundation Models** · *서브카테고리*

`56편` `2024–2026` `가속` `2025+ 56편`

<sub>의료·신경 신호 모델링 고유 배정 213편(중복 포함 592편 · 웹 인덱스 기준) · 서브카테고리 7개 · 본 파트 5개로 82% 커버</sub>

> [!quote] 파트 도입
> 신호를 언어와 이어 붙이는 기반모델은 늘었지만, 환자 간·기관 간 일반화 검증이 임상 문턱이다.

> [!abstract] 핵심 메시지
> EHR 모델의 사전학습 목적이 다음 토큰 예측에서 질의 조건·사건 시간 예측으로 옮겨갔다.

- 2026 EveryQuery가 (코드, 기간) 쿼리를 조건으로 단일 forward pass에서 발생 확률을 추정하는 zero-shot 예측을 내놨다.
- 2026 SparseEHR는 약 50M 환자 규모의 sparse/MoE 사전학습을, EHR-RAGp는 검색 증강 종단 모델링을 제시했다.[4]
- 2026 PaCX-MAE·MedMIX와 멀티모달 자기회귀 EHR 모델이 ECG·CXR·임상 노트를 게이트 교차어텐션으로 결합했다.[1]
- 2026 Informative Irregularity가 측정 타이밍 자체를 feature로 보고 irregularity regime별 층화 평가를 요구했고, 희소 오토인코더·conformal·하위집단 감사가 뒤따랐다.
- 배경: 2025 CLEAR는 임상 엔티티 기반 검색으로 임상 노트 추출의 토큰 사용을 70% 이상 줄였다.

**대표 도구·시스템** — SparseEHR · EHR-RAGp · EveryQuery · ORA · MOTOR · PyHealth 2.0 · EHRSHOT · MIMIC-IV · MedTPE · ECG-R1

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [MedMIX: Modality-Internal Expert Fusion for Multimodal Medical Diagnosis](../../docs/papers/10014_MedMIX_Modality-Internal_Expert_Fusion_for_Multimodal_Medica/index.html) — Seungik Cho 외, 2026 · 인용 1,331
    - MedMIX는 여러 소형 전문가 모델(FM)의 임베딩을 모달리티 내부에서 MoE 방식으로 융합하고, 모달리티 간에는 샘플별 학습된 가중치로 결합하며, 학습 시에만 teacher-student distillation을 적용하여 결측 모달리티에…
2. [Autoregressive EHR Foundation Models with Multimodal Inputs](../../docs/papers/9284_Autoregressive_EHR_Foundation_Models_with_Multimodal_Inputs/index.html) — Yuxuan Liu 외, 2026 · 인용 60
    - 구조화된 EHR 이벤트 코드만 사용하는 autoregressive EHR foundation model에 ECG, CXR, clinical notes 등 보조 모달리티를 latent compression과 gated cross-attenti…
3. [A Fairness Audit of Medical Imaging Foundation Models on a Multimodal Structured Clinical Benchmark](../../docs/papers/9147_A_Fairness_Audit_of_Medical_Imaging_Foundation_Models_on_a_M/index.html) — Milan Mohan 외, 2026
    - 세 가지 의료 영상 foundation model(MedImageInsight, MedSigLIP, BiomedCLIP)을 INSPECT 벤치마크에서 최초로 체계적인 fairness audit을 수행하여, 연령(age)이 인종/성별보다 훨씬…
4. [SparseEHR: Scalable Foundation Modeling for Structured EHR via Conditional Computation](../../docs/papers/10473_SparseEHR_Scalable_Foundation_Modeling_for_Structured_EHR_vi/index.html) — Meysam Ghaffari 외, 2026
    - SparseEHR는 dense warm-start layer와 shared expert + top-1 routed expert 구조의 mixture-of-experts(MoE) layer를 결합한 hybrid transformer로, 약 5…

> [!tip] 우리에게 무엇인가
> 이 칸은 모델 구조보다 데이터 접근권이 경쟁력을 정한다. 국내는 MIMIC-IV 같은 공개 코퍼스와 한국어 임상 보고서 모델링(Mode-Aware Phenotype Profiling)을 병행하되, 병원 데이터 반출 없이 학습·평가하는 구조를 먼저 설계해야 한다.

---

## S32 · 뇌-시각 표상 정렬

*제6부 · 의료·신경 신호 모델링* · **Brain-Visual Representation Alignment** · *서브카테고리*

`33편` `2025–2026` `가속` `2025+ 33편`

> [!abstract] 핵심 메시지
> 모델-뇌 정렬이 개별 모델 비교에서 수백 모델 규모의 스케일링 법칙 검증으로 커졌다.

- 2026 Alignment between Brains and AI가 630개 모델과 Natural Scenes Dataset fMRI를 6천만 건 이상의 CKA로 비교했다.[1]
- 2026 Multimodal Scaling Laws가 8개 신경 데이터셋과 600개 이상의 비전 모델로 정렬의 스케일링 법칙을 규명했다.
- 2026 Reverse predictivity가 뇌 반응으로 ANN 유닛을 예측하는 양방향 진단을 도입해 순방향 정렬의 한계를 짚었다.
- 2026 MEG-XL은 191k 토큰의 긴 MEG 문맥 사전학습으로 brain-to-text 디코딩의 피험자별 데이터 요구를 줄였다.[2]
- 배경: 뇌 그래프 학습은 수작업 기능 연결성에서 HiSP-Net, SI-IGCL 같은 학습형·스펙트럼 표현으로 옮겨 가고 있다.

**대표 도구·시스템** — SAEs-BrainMap · HiSP-Net · MuHL · PhenoBrain · SI-IGCL · MEG-XL · Natural Scenes Dataset · Torus Graphs · Connector

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Alignment between Brains and AI: Evidence for Convergent Evolution across Modalities, Scales and Training Trajectories](../../docs/papers/9231_Alignment_between_Brains_and_AI_Evidence_for_Convergent_Evol/index.html) — Guobin Shen 외, 2026
    - 630개 AI 모델(언어·비전, 1.33M~72B 파라미터)의 내부 표현을 Natural Scenes Dataset fMRI와 비교하여 6천만 건 이상의 CKA 정렬 측정치를 산출하고, 성능이 높은 모델일수록 뇌와의 정렬도가 자발적으로 강해…
2. [MEG-XL: Data-Efficient Brain-to-Text via Long-Context Pre-Training](../../docs/papers/10019_MEG-XL_Data-Efficient_Brain-to-Text_via_Long-Context_Pre-Tra/index.html) — Dulhan Jayalath 외, 2026
    - MEG-XL은 2.5분(191k 토큰)의 긴 MEG 컨텍스트로 사전학습하는 프레임워크로, 기존 대비 5-300배 긴 컨텍스트를 활용해 brain-to-text word decoding에서 훨씬 적은 subject-specific 데이터로도…
3. [SAEs-BrainMap: Unveiling the Emergence of Specialized Concepts in Deep Models via Brain Alignment](../../docs/papers/10358_SAEs-BrainMap_Unveiling_the_Emergence_of_Specialized_Concept/index.html) — Ziming Mao 외, 2026
    - 인간 뇌의 ventral visual pathway fMRI 활성 패턴을 객관적 probe로 활용하여, Sparse Autoencoders(SAEs)로 분해된 deep vision model의 특징(feature)이 어떻게 일반적 개념(ge…
4. [Local Intrinsic Dimension of Representations Predicts Alignment and Generalization in AI Models and Human Brain](../../docs/papers/9964_Local_Intrinsic_Dimension_of_Representations_Predicts_Alignm/index.html) — Junjie Yu 외, 2026
    - 신경망의 표현이 잘 일반화될수록 다른 모델 및 인간 뇌 신경 활동과 더 강하게 정렬(alignment)되며, 이 세 가지 현상(generalization, AI-AI alignment, AI-Brain alignment) 모두가 embedd…

> [!tip] 우리에게 무엇인가
> 이 칸은 임상 제품보다 기초 신경과학 인프라에 가깝다. 신경 데이터셋 확보와 피험자 간 일반화 검증 역량이 있는 연구실이 비전 모델 평가 지표를 선점할 수 있다.

---

## S33 · 의료영상 분할

*제6부 · 의료·신경 신호 모델링* · **Medical Image Segmentation** · *서브카테고리*

<sub>타임라인 분석 명칭: Medical Image Segmentation & Representation</sub>

`32편` `2023–2026` `안정` `2025+ 30편`

> [!abstract] 핵심 메시지
> 분할은 성능 경쟁에서 라벨 효율·연합 학습·해석 가능성으로 무게중심이 옮겨갔다.

- 2026 SPROUT는 학습·주석 없이 SAM에 point prompt를 만들어 핵 인스턴스를 분할하는 training-free 방식을 보였다.
- 2026 FedMAP·Inverse Asymmetric Tuning이 인코더는 외형 변화, 디코더는 개념 변화에 좌우된다는 비대칭을 연합 개인화에 썼다.
- 2026 S2M-Net이 스펙트럼-공간 토큰 혼합으로 self-attention의 제곱 복잡도를 피했고 3D 대형 커널 재매개변수화가 이를 이었다.[4]
- 2026 Med-SegLens가 SAE로 분할 모델 내부를 분해해 모델 간 diffing을 하고 S(H)NAP이 Sybil의 근거를 인과 개입으로 감사했다.[1]
- 배경: 2023~2024 SAM 계열이 범용 분할의 출발점이었고 UniMedVL, SynerMedGen이 이해와 생성의 통합을 시도한다.

**대표 도구·시스템** — S2M-Net · Mosaic MAE · SPROUT · SAM/SAM2 · FlowPET · UniMedVL · Med-SegLens · MedCRP-CL · IPOD

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Med-SegLens: Latent-Level Model Diffing for Interpretable Medical Image Segmentation](../../docs/papers/10005_Med-SegLens_Latent-Level_Model_Diffing_for_Interpretable_Med/index.html) — Salma J. Ahmed 외, 2026 · 인용 872
    - segmentation 모델의 내부 activation을 sparse autoencoder(SAE)로 분해하여 해석 가능한 latent feature로 만들고, cross-architecture·cross-dataset latent alig…
2. [MedCRP-CL: Continual Medical Image Segmentation via Bayesian Nonparametric Semantic Modality Discovery](../../docs/papers/10009_MedCRP-CL_Continual_Medical_Image_Segmentation_via_Bayesian/index.html) — Ziyuan Gao, 2026
    - MedCRP-CL은 Chinese Restaurant Process(CRP)를 활용해 임상 텍스트 프롬프트로부터 online으로 task 구조(semantic modality)를 발견하고, 이를 기반으로 modality별 LoRA adapt…
3. [Rethinking Federated Prompt Learning for Medical Images: From Textual Tuning to Visual Manifold Anchoring](../../docs/papers/10331_Rethinking_Federated_Prompt_Learning_for_Medical_Images_From/index.html) — Yipan Wei 외, 2026
    - Federated Prompt Learning(FPL)에서 기존 "textual tuning" 패러다임이 의료 영상에서는 frozen visual encoder의 특징 기하 구조가 무너진다는 점을 지적하고, LLM 기반 codebook을 이…
4. [S2M-Net: Spectral-Spatial Mixing with Morphology-Aware Adaptive Loss for Medical Image Segmentation](../../docs/papers/10356_S2M-Net_Spectral-Spatial_Mixing_with_Morphology-Aware_Adapti/index.html) — Sanaullah Chowdhury 외, 2026
    - S2M-Net은 self-attention의 O((HW)^2C) 복잡도 문제를 해결하기 위해 spectral-spatial token mixing(SSTM)과 morphology-aware adaptive loss(MASL)를 결합한 경량…

> [!tip] 우리에게 무엇인가
> 타임라인이 STABLE인 성숙 과제다. 병원별 영상 분포 차이를 다루는 연합·적응 기술과 해석 가능성 감사가 도입 가능성을 가른다.

---

## S34 · 멀티모달 의료영상 진단

*제6부 · 의료·신경 신호 모델링* · **Multimodal Medical Diagnostic Imaging** · *서브카테고리*

<sub>타임라인 분석 명칭: Multimodal Medical Diagnostic Imaging & Med-LVLMs</sub>

`27편` `2023–2026` `가속` `2025+ 25편`

> [!abstract] 핵심 메시지
> 의료 MLLM의 유창함과 진단 타당성의 간극이 2026년에 기하·환각 교정과 도구 사용으로 다뤄진다.

- 2026 Med-Scout가 MLLM의 기하학적 맹점(스케일·위상·이상 일관성 위반)을 규명하고 라벨 없는 기하 RL로 교정했다.[2]
- 2026 MEDA는 의료 LVLM 최초의 activation editing으로, MedREK는 검색 기반 모델 편집으로 환각을 줄이려 했다.[3][4]
- 2026 Ophiuchus·3DMedAgent·PathCTM이 SAM2, BiomedParse 등 도구를 추론에 끌어들이는 에이전트형 진단을 보였다.
- 2026 ORBIT은 안과 만성질환을 POMDP로 두고 반사실적 시각 예견으로 치료 후 해부 상태를 상상하는 예후 월드모델이다.
- 배경: 2023 GPT-4V 임상 사례 연구가 간극을 드러냈고, 2024 PathChat·Med-Gemini가 도메인 특화 코파일럿을 열었다.

**대표 도구·시스템** — GPT-4V · Med-Gemini · PathChat · MEDA · MedREK · Ophiuchus · 3DMedAgent · ORBIT · SpatialMed · EviScreen

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Seizure-Semiology-Suite(S^3): A Clinically Multimodal Dataset, Benchmark, and Models for Seizure Semiology Understanding](../../docs/papers/10406_Seizure-Semiology-SuiteS3_A_Clinically_Multimodal_Dataset_Be/index.html) — Lina Zhang 외, 2026
    - 발작 비디오에서 ILAE 정의 20개 semiological feature를 세밀하게 이해하고 진단까지 이어지는 능력을 평가하기 위해, 438개 발작 비디오와 35,000개 이상의 dense label로 구성된 Seizure-Semiolog…
2. [Med-Scout: Curing MLLMs' Geometric Blindness in Medical Perception via Geometry-Aware RL Post-Training](../../docs/papers/10004_Med-Scout_Curing_MLLMs_Geometric_Blindness_in_Medical_Percep/index.html) — Anglin Liu 외, 2026
    - MLLM이 의료 영상 진단에서 언어적 유창함은 뛰어나지만 스케일, 위상, 이상 일관성 등 객관적 기하학적 제약을 지키지 못하는 "geometric blindness"를 가진다는 것을 밝히고, 이를 라벨 없는 의료 영상의 내재적 기하 논리를…
3. [MEDA: Medical-Oriented Activation Editing for Hallucination Mitigation in Medical Large Vision-Language Model](../../docs/papers/10006_MEDA_Medical-Oriented_Activation_Editing_for_Hallucination_M/index.html) — Tianbo Wang 외, 2026
    - MEDA는 의료 영상 해석에 특화된 최초의 activation editing 기법으로, Query-decisive Manifestation Steering(QMS)과 Principle-driven Diagnosis Induction(PDI)…
4. [MedREK: Retrieval-Based Editing for Medical LLMs with Key-Aware Prompts](../../docs/papers/10016_MedREK_Retrieval-Based_Editing_for_Medical_LLMs_with_Key-Awa/index.html) — Shujun Xia 외, 2026
    - MedREK은 의료 LLM을 위한 retrieval-based model editing 프레임워크로, shared query-key MLP와 attention 기반 prompt encoder를 결합해 의료 지식 공간의 representati…

> [!tip] 우리에게 무엇인가
> 진단 보조는 정확도 시연이 아니라 오류 유형의 공개와 벤치마크 설계 역량이 신뢰를 만든다. 국내 임상 데이터로 만든 평가셋이 해외 모델의 도입 검증 기준이 될 수 있다.

---

## S35 · 생체신호 파운데이션 모델

*제6부 · 의료·신경 신호 모델링* · **Physiological Signal Foundation Models** · *서브카테고리*

`27편` `2025–2026` `가속` `2025+ 27편`

> [!abstract] 핵심 메시지
> ECG·수면·PPG에서 토큰 없는 인코더와 대규모 오픈 말뭉치가 생체신호 기반모델의 기본값이 되고 있다.

- 2026 OSF가 SleepBench(166,500시간 다기관 수면 데이터)로 수면 기반모델의 사전학습·스케일링 설계를 오픈소스로 분석했다.
- 2026 SleepLM이 PSG 신호와 자연어를 정렬해 수면 상태를 개방형으로 질의하는 sleep-language 모델 계열을 열었다.[1]
- 2026 MedMamba, NeurOCNN이 고정 패치 토큰화 대신 상태공간·신경 연산자 인코더로 ECG·EEG 시계열을 다룬다.[2][3]
- 2026 SIGMA-PPG, SyneCo, PULSE가 사전지식 마스킹, 동시기록 신호의 시너지 대조학습, 동역학 기반 표현 분리를 시도했다.[4]
- 배경: Robust ECG Classification은 환자 단위(LOSO) 평가에서 표현 방식을 비교해 일반화 점검의 기준을 제시한다.

**대표 도구·시스템** — MedMamba · NeurOCNN · WaveFormer · SleepMaMi · SleepLM · SIGMA-PPG · PapaGei · wav2vec2 · PULSE · SyneCo

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [SleepLM: Natural-Language Intelligence for Human Sleep](../../docs/papers/10454_SleepLM_Natural-Language_Intelligence_for_Human_Sleep/index.html) — Zongzhe Xu 외, 2026
    - SleepLM은 다중모달 polysomnography(PSG) 신호와 자연어를 정렬하여 수면 상태를 개방형으로 설명·질의·해석할 수 있게 하는 최초의 sleep-language foundation model 계열이며, 이를 위해 100K시간…
2. [MedMamba: Multi-View State Space Models with Adaptive Graph Learning for Medical Time Series Classification](../../docs/papers/10012_MedMamba_Multi-View_State_Space_Models_with_Adaptive_Graph_L/index.html) — Da Zhang 외, 2026
    - MedMamba는 medical time series 분류를 위해 state space model(Mamba)에 도메인 특화 inductive bias를 결합한 end-to-end 아키텍처로, multi-scale convolutional…
3. [NeurOCNN: A Neural-Operator-Based Model for Physiological Time Series](../../docs/papers/10103_NeurOCNN_A_Neural-Operator-Based_Model_for_Physiological_Tim/index.html) — Daya Kumar 외, 2026
    - NeurOCNN은 PDE 지향의 neural operator를 생리학적 시계열(EEG, EOG, ECG) 도메인에 맞게 재설계한 모델로, continuous-time spline-parameterized convolution과 Fourier…
4. [SIGMA-PPG: Statistical-prior Informed Generative Masking Architecture for PPG Foundation Model](../../docs/papers/10440_SIGMA-PPG_Statistical-prior_Informed__Generative_Masking_Arc/index.html) — Zongheng Guo 외, 2026
    - SIGMA-PPG는 PPG 신호의 내재적 중복성과 노이즈 문제를 해결하기 위해 통계적 사전지식 기반의 적대적 마스킹(Prior-Guided Adversarial Masking)과 의미론적 일관성 제약(semantic consistency c…

> [!tip] 우리에게 무엇인가
> 웨어러블·수면 센서의 국내 보급을 데이터 자산으로 바꾸려면 기기 간 이질성과 환자 단위 평가를 먼저 갖춰야 한다. 허가 단계에서는 다기관 일반화가 핵심 증빙이 될 것이다.

---

## S36 · 동료심사 피드백 데이터셋

*제7부 · 과학 문헌·동료심사* · **Peer Review Feedback Datasets** · *서브카테고리*

<sub>타임라인 분석 명칭: Peer Review Feedback Datasets & LLM Reviewers</sub>

`61편` `2019–2026` `가속` `2025+ 35편`

<sub>과학 문헌·동료심사 고유 배정 210편(중복 포함 463편 · 웹 인덱스 기준) · 서브카테고리 7개 · 본 파트 5개로 82% 커버</sub>

> [!quote] 파트 도입
> AI 저작·심사 정책을 의견이 아니라 데이터로 설계할 근거가 쌓였다. 이제 병목은 검증이다.

> [!abstract] 핵심 메시지
> 심사 코퍼스가 쌓이자 AI 리뷰어가 AAAI-26 전 제출 논문에 실전 배치됐다.

- 2026 AI-Assisted Peer Review at Scale: AAAI-26 AI Review Pilot이 제출 22,977편 전체에 다단계 AI 리뷰를 배포한 첫 학회 규모 현장 실증이다.[1]
- 2026 ReviewArena가 7개 OpenReview venue의 51,529편·196,099개 리뷰와 1,002편 평가 벤치마크 ReviewArena-Eval을 공개했다.[4]
- 2025 DeepReview의 DeepReviewer-14B가 CycleReviewer-70B, GPT-o1, DeepSeek-R1을 넘어서면서 토큰은 더 적게 썼다.
- 2025–2026 ReviewEval, Mind the blind spots, 철회 논문 기반 오류 검출이 AI 리뷰의 신뢰성 감사를 시작했다. 숨은 프롬프트 적발은 연구자 반발을 샀다.[2][3]
- 배경: 2023 GPT-4 대규모 피드백 연구와 ORB·Re2 같은 공개 코퍼스가 이 흐름의 출발점이다.

**대표 도구·시스템** — OpenReviewer · DeepReviewer-14B · CycleResearcher/CycleReviewer · MARG · Reviewer2 · REMOR · ReviewEval · AgentReview · XtraGPT · ReviewArena · FIRSTPASS · LazyReview

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [AI-Assisted Peer Review at Scale: The AAAI-26 AI Review Pilot](../../docs/papers/10928_AI-Assisted_Peer_Review_at_Scale_The_AAAI-26_AI_Review_Pilot/index.html) — Joydeep Biswas 외, 2026.04 · 인용 1
    - AAAI-26 전체 메인트랙 제출 논문(22,977편)에 대해 frontier LLM 기반 multi-stage AI review 시스템을 실제 동료심사 과정에 배포하고, 대규모 설문과 새로운 벤치마크를 통해 AI 리뷰의 품질과 유용성을 실…
2. [Mind the blind spots: A focus-level evaluation framework for llm reviews](../../docs/papers/537_Mind_the_blind_spots_A_focus-level_evaluation_framework_for/index.html) — Hyungyu Shin 외, 2025 · 인용 3
    - LLM이 생성한 논문 리뷰가 인간 전문가와 동일한 핵심 측면에 주목하는지 평가하기 위해 focus-level 평가 프레임워크를 제안하며, 자동 주석 처리를 통해 LLM의 blind spot을 체계적으로 분석한다.
3. [ReviewEval: An evaluation framework for AI-generated reviews](../../docs/papers/679_Revieweval_An_evaluation_framework_for_ai-generated_reviews/index.html) — Madhav Krishan Garg 외, 2025 · 인용 2
    - 학술 논문 동료 평가(peer review) 부족 문제를 해결하기 위해 LLM 기반 리뷰 시스템의 신뢰성을 평가하는 종합 프레임워크 ReviewEval과 자체 개선 루프를 갖춘 AI 리뷰어 ReviewAgent를 제안한다.
4. [ReviewArena: A Large-Scale Cross-Conference Dataset and Benchmark for LLM Peer Review](../../docs/papers/10341_ReviewArena_A_Large-Scale_Cross-Conference_Dataset_and_Bench/index.html) — Samarth P 외, 2026
    - ReviewArena은 7개 OpenReview venue(NeurIPS, ICLR, ICML, CoRL, COLM, EMNLP, TMLR)에서 수집한 51,529편 논문·196,099개 review로 구성된 대규모 cross-confere…
5. [FIRSTPASS: A Multi-Domain, Multi-Round Peer Review Dataset Grounded in Real Editorial Outcomes](../../docs/papers/9652_FIRSTPASS_A_Multi-Domain_Multi-Round_Peer_Review_Dataset_Gro/index.html) — Prabhjot Singh 외, 2026
    - 기존 peer review 데이터셋이 CS/ML 학회에 국한된 문제를 해결하기 위해, Nature Communications의 transparent peer review 제도를 활용해 5개 과학 분야(biology, chemistry, ne…

> [!tip] 우리에게 무엇인가
> AI 저작·심사 정책을 감정이 아니라 데이터로 설계할 근거가 쌓였다. 도입 여부보다 인간-AI 일치도의 공개 보고 체계를 먼저 갖춰야 한다.

---

## S37 · 과학 문헌 검색·QA

*제7부 · 과학 문헌·동료심사* · **Scientific Literature Retrieval QA** · *서브카테고리*

<sub>타임라인 분석 명칭: Scientific Literature Retrieval & QA</sub>

`32편` `2019–2026` `가속` `2025+ 18편`

> [!abstract] 핵심 메시지
> 문헌 검색이 키워드 매칭에서 관계 인지·멀티모달 에이전트로 넘어갔다.

- 2025 PaSa가 합성 데이터 AutoScholarQuery로 학습하고도 RealScholarQuery에서 Google Scholar와 GPT-4o 기반 방법을 크게 앞섰다.
- 2026 PaSaMaster는 논문을 생성하지 않고 검증된 코퍼스에서 순위만 매겨 hallucination 없는 자기 진화형 검색을 한다.
- 2026 SciNet이 269만 편 메타데이터 위에 관계 인지형 에이전트 평가 8,940개 과제를 만들었고, 멀티모달 문헌 에이전트는 LAB-Bench 2 FigQA2·LitQA3·TableQA2 최고 성능을 냈다.[1]
- 2025–2026 SciMuse, ResearchLink, EO-Agents가 지식 그래프에서 연구 가설을 생성한다. 기관 간 문헌 공유는 privacy-aware RAG Giovanna가 다룬다.
- 배경: SciBERT, PubMedQA 같은 도메인 사전학습과 PaperQA2 계열 agentic RAG가 기반을 놓았다.

**대표 도구·시스템** — SciBERT · PubMedQA · PaperQA2 · OpenScholar · HiPerRAG · PaSa · SciNet · EarthSE · SciQAG · AutoReproduce · PRISM

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [SciNet: Evaluating AI Agents in Relation-Aware Scientific Literature Retrieval](../../docs/papers/10391_SciNet_Evaluating_AI_Agents_in_Relation-Aware_Scientific_Lit/index.html) — Chenyang Shao 외, 2026 · 인용 3,133
    - SciNet은 269만 편 규모의 과학 논문 메타데이터베이스를 기반으로, ego-centric·pair-wise·path-wise 세 가지 수준의 관계 인지형(retrieval agent) 평가를 위한 8,940개 태스크로 구성된 최초의 s…
2. [Towards Self-Evolving Agentic Literature Retrieval](../../docs/papers/10617_Towards_Self-Evolving_Agentic_Literature_Retrieval/index.html) — Yuwen Du 외, 2026 · 인용 1,798
    - PaSaMaster는 자연어로 표현된 복잡한 연구 의도를 반복적으로 정제하며, 논문을 생성하지 않고 검증된 코퍼스에서 관련도 순위를 매기는 self-evolving agentic literature retrieval 시스템으로, halluc…
3. [IRIS: An Agentic Multi-Phase Framework for Automated Scientific Literature Review](../../docs/papers/9847_IRIS_An_Agentic_Multi-Phase_Framework_for_Automated_Scientif/index.html) — Sergey Kolchenko 외, 2026 · 인용 48
    - IRIS는 과학 문헌 리뷰를 자동화하는 agentic framework로, 반복적 계획, 병렬 섹션별 연구·작성, 최종 보고서 컴파일의 3단계를 directed state graph로 orchestration하며, reflective res…
4. [ResearchAgent: Iterative Research Idea Generation over Scientific Literature with Large Language Models](../../docs/papers/668_ResearchAgent_Iterative_Research_Idea_Generation_over_Scient/index.html) — Jinheon Baek 외, 2025.02 · 인용 34
    - 대규모 언어 모델(LLM)의 백과사전적 지식과 추론 능력을 활용하여 과학 문헌으로부터 자동으로 새로운 연구 아이디어를 생성하고 인간 선호도 기반의 피어 리뷰 에이전트를 통해 반복적으로 개선하는 시스템을 제안한다.

> [!tip] 우리에게 무엇인가
> 검색 에이전트는 이미 사람 검색을 넘어선 사례가 있다. 국내는 논문 검색 자체보다 기관 내부 문헌을 외부 유출 없이 쓰는 RAG 설계에서 차별화할 수 있다.

---

## S38 · 신규성 기반 아이디어

*제7부 · 과학 문헌·동료심사* · **Novelty-Driven Scientific Idea Retrieval** · *서브카테고리*

`30편` `2022–2026` `가속` `2025+ 21편`

> [!abstract] 핵심 메시지
> 아이디어 생성은 쉬워졌고, 참신성과 표절을 재는 감사가 병목이 됐다.

- 2025 All that glitters is not novel: Plagiarism in ai generated research가 LLM 생성 연구 문서의 24%가 기존 논문에서 정교하게 표절됐다고 보였다.
- 2025 Relative Neighbor Density(RND)와 GraphEval, AI Idea Bench 2025(3,495편 기반)가 아이디어 참신성·실현가능성 평가를 정량화했다.[1][2]
- 2026 InnoEval은 아이디어 평가를 지식 기반 다관점 추론 문제로 정의하고, SciPaths는 262개 전문가 주석 gold pathway로 발견 경로를 예측한다.[3][4]
- 2026 SciContrib-Bench가 hypothesis·methodology·interpretation·abstract 단계별로 AI 생성 기여물의 탐지 가능성을 측정했다. PaperGym은 retrieval의 실효를 진단한다.
- 배경: 2022 의미망 링크 예측으로 미래 주제를 예측했고, 이후 SciMON·SciPIP·Nova가 문헌 근거형 생성기를 세웠다.

**대표 도구·시스템** — SciMON · SciPIP · Nova · Chain of Ideas · Scideator · Spacer · GraphEval · InnoEval · AI Idea Bench 2025 · LiveIdeaBench · Chimera · MIR · SciPaths

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Ai idea bench 2025: Ai research idea generation benchmark](../../docs/papers/10924_Ai_idea_bench_2025_Ai_research_idea_generation_benchmark/index.html) — DeepSeek-AI 외, 2025
    - LLM 기반 AI 연구 아이디어 생성을 정량적으로 평가하기 위한 벤치마크인 AI Idea Bench 2025를 제안하며, 3,495편의 AI 논문과 이를 촉발한 선행연구(inspiration papers)를 ground truth로 활용해…
2. [GraphEval: A lightweight graph-based llm framework for idea evaluation](../../docs/papers/392_Grapheval_A_lightweight_graph-based_llm_framework_for_idea_e/index.html) — Tao Feng 외, 2025
    - 복잡한 연구 아이디어를 이해 가능한 관점들로 분해하고 이를 그래프로 연결하여 라벨 전파(label propagation) 또는 그래프 신경망(GNN)을 통해 견고하고 편향 없는 아이디어 평가를 수행하는 경량 프레임워크다.
3. [SciPaths: Forecasting Pathways to Scientific Discovery](../../docs/papers/10392_SciPaths_Forecasting_Pathways_to_Scientific_Discovery/index.html) — Eric Chamoun 외, 2026
    - SciPaths는 목표 과학적 기여를 실현하는 데 필요한 선행(enabling) 기여들을 식별하고 이를 사전 문헌(prior work)에 근거(grounding)시키는 새로운 과제인 discovery pathway forecasting을 제…
4. [InnoEval: On Research Idea Evaluation as a Knowledge-Grounded, Multi-Perspective Reasoning Problem](../../docs/papers/9833_InnoEval_On_Research_Idea_Evaluation_as_a_Knowledge-Grounded/index.html) — Shuofei Qiao 외, 2026
    - 연구 아이디어 평가를 knowledge-grounded, multi-perspective reasoning 문제로 재정의하고, 이질적 심층 지식 검색 엔진과 다중 페르소나 리뷰 보드를 결합한 InnoEval 프레임워크를 제안하여 인간 전문가…

> [!tip] 우리에게 무엇인가
> AI가 만든 아이디어를 쓸지 말지는 표절 비율과 탐지 가능성이라는 데이터로 정할 수 있다. 연구윤리 지침은 이 수치를 기준선으로 삼아야 한다.

---

## S39 · 자동 문헌 리뷰 생성

*제7부 · 과학 문헌·동료심사* · **Automated Literature Review Generation** · *서브카테고리*

`25편` `2023–2026` `가속` `2025+ 14편`

> [!abstract] 핵심 메시지
> 서베이 자동 작성은 상용 deep research를 넘어섰지만 인용 신뢰성 비판이 따라붙는다.

- 2026 IRIS가 PubMed와 ArXiv만으로 상용 deep research 시스템을 능가했고, SurveyMaster는 SciSurveyBench의 10개 분야 100개 과제로 검증됐다.
- 2026 LitReview Arena가 3k 전문가 판단의 LitReviewBench와 저비용 평가자 LitJudge를 만들었고, 2025 DeepResearch Bench는 22개 분야 100개 과제를 제공한다.[3]
- 2025 SurveyX, SurveyForge(SurveyBench), Select, read, and write가 아웃라인·메모리·전문 읽기로 서베이와 관련연구 작성을 자동화했다.[1][2]
- 2025 Generalization Bias는 LLM 요약이 사람보다 약 5배 자주 결론을 과일반화한다고 보였고, 임상 리뷰 비교 연구는 인용 정확도 부족을 확인했다.
- 배경: 2023 Bio-SIEVE가 체계적 문헌고찰 초록 스크리닝을 자동화했고, 2024 STORM이 아웃라인 생성을 열었다.

**대표 도구·시스템** — STORM · SurveyForge · SurveyX · LitLLM · CHIME · DeepResearch Bench · IRIS · SurveyMaster/SciSurveyBench · LitReview Arena · DiffResearch · Bio-SIEVE · Elicit

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Select, read, and write: A multi-agent framework of full-text-based related work generation](../../docs/papers/742_Select_read_and_write_A_multi-agent_framework_of_full-text-b/index.html) — Xiaochuan Liu 외, 2025
    - 학술 논문의 관련 연구(Related Work) 섹션 자동 생성을 위해 전체 텍스트 기반 다중 에이전트 프레임워크를 제안한다. 셀렉터-리더-라이터 구조와 그래프 기반 제약을 통해 참고 문헌 간의 관계를 명시적으로 포착하고 깊이 있는 이해를…
2. [SurveyX: Academic survey automation via large language models](../../docs/papers/781_Surveyx_Academic_survey_automation_via_large_language_models/index.html) — Xun Liang 외, 2025 · 인용 2,819
    - arXiv에 매년 증가하는 학술 논문의 폭증 속에서, 대형언어모델(LLM)을 활용하여 체계적이고 고품질의 학술 서베이를 자동 생성하는 SurveyX 시스템을 제안한다. 이 시스템은 온라인 참고문헌 검색, AttributeTree 전처리 방법…
3. [LitReview Arena: Evaluating Literature Review Agents with Battle-style Peer Review Platform](../../docs/papers/9953_LitReview_Arena_Evaluating_Literature_Review_Agents_with_Bat/index.html) — Ruotong Zhao 외, 2026 · 인용 210
    - 본 논문은 자동 생성 literature review의 품질을 평가하기 어려운 문제를 해결하기 위해 battle-style 전문가 평가 플랫폼인 LitReview Arena를 제안하고, 이를 통해 3k개의 전문가 판단 데이터셋 LitRevi…
4. [Using artificial intelligence for systematic review: the example of elicit](../../docs/papers/862_Using_artificial_intelligence_for_systematic_review_the_exam/index.html) — Nathan Bernard 외, 2025.03 · 인용 83
    - Elicit이라는 AI 도구를 이용한 체계적 문헌고찰(systematic review) 과정이 기존의 전통적 선별 방법과 비교하여 부가가치를 제공하는지 검증한 연구이다. 재현성, 신뢰성, 정확성 세 가지 기준으로 Elicit의 성능을 평가하…

> [!tip] 우리에게 무엇인가
> 자동 서베이는 초안 도구로는 충분히 쓸 만하다. 인용 정확도와 과일반화 점검을 통과시키는 절차가 없다면 기관 보고서에 넣으면 안 된다.

---

## S40 · 다문서·메타리뷰 요약

*제7부 · 과학 문헌·동료심사* · **Multi-Document Review Summarization** · *서브카테고리*

<sub>타임라인 분석 명칭: Multi-Document & Meta-Review Summarization</sub>

`24편` `2018–2026` `안정` `2025+ 7편`

> [!abstract] 핵심 메시지
> 요약 연구는 안정기에 들어섰고, 장문 확장과 상충 리뷰 종합으로 무게가 옮겨갔다.

- 2025 TreeReview가 질문-답변 트리로 토큰 사용량을 80%까지 줄이면서 LLM 논문 리뷰의 깊이와 전문가 정렬성을 높였다.[1]
- 2025 LLM × MapReduce-V2가 엔트로피 기반 합성곱형 테스트 타임 스케일링으로 극도로 긴 입력에서 장문 글을 생성한다.[4]
- 2025 XSum 모듈식 RAG 파이프라인, 최적 context 길이 추정, PGraphRAG가 검색 증강 요약의 설계 변수를 정리했다.
- 2025 MoDeST(영어·터키어 다분야 제목 생성)와 Lag 리더보드 자동 생성이 요약을 데이터셋·결과 집계로 확장했다.[2]
- 배경: SciTLDR, MS2, BigSurvey, SciReviewGen, KGSum, HAESum 등 2018–2024 데이터셋과 모델이 기반이며 상충 리뷰 종합은 PEERSUM·GLIMPSE가 다뤘다.

**대표 도구·시스템** — SciTLDR/CATTS · MS2 · BigSurvey/CAST · KGSum · PEERSUM/RAMMER · GLIMPSE · TreeReview · LLM x MapReduce-V2 · XSum · MoDeST

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [TreeReview: A dynamic tree of questions framework for deep and efficient llm-based scientific peer review](../../docs/papers/843_Treereview_A_dynamic_tree_of_questions_framework_for_deep_an/index.html) — Yuan Chang 외, 2025 · 인용 2
    - 본 논문은 긴 학술 논문의 동료평가(peer review)를 효율적이면서도 깊이 있게 수행하기 위해 질문-답변 트리 구조를 활용하는 TreeReview 프레임워크를 제안한다. 계층적 질문 분해와 동적 질문 확장 메커니즘을 통해 LLM 기반…
2. [MoDeST: A dataset for Multi Domain Scientific Title Generation](../../docs/papers/10765_modest_a_dataset_for_multi_domain_scientific_title_gen/index.html) — Necva Bölücü 외, 2025.05 · 인용 1
    - MoDeST는 영어와 터키어, 다양한 학문 분야(사회과학, 의학, 공학 등)를 아우르는 최초의 multi-domain, multilingual 과학 논문 title generation 데이터셋으로, keywords·abstract·full…
3. [Estimating optimal context length for hybrid retrieval-augmented multi-document summarization](../../docs/papers/318_Estimating_optimal_context_length_for_hybrid_retrievalaugmen/index.html) — Adithya Pratapa 외, 2025
    - 본 논문은 hybrid retrieval-augmented multi-document summarization에서 retriever, summarizer, dataset에 특화된 최적의 retrieval context length를 추정하는…
4. [LLM × MapReduce-V2: Entropy-Driven Convolutional Test-Time Scaling for Generating Long-Form Articles from Extremely Long Resources](../../docs/papers/495_Llm__mapreduce-v2_Entropy-driven_convolutional_test-time_sca/index.html) — Haoyu Wang 외, 2025
    - 본 논문은 극도로 긴 입력 자원으로부터 장문 기사를 생성하는 LLM의 능력을 향상시키기 위해, 정보 병목 이론에 기반한 합성곱 신경망 영감의 테스트 타임 스케일링 방법을 제안한다. 추출적 방법의 한계를 극복하기 위해 자원을 통합적으로 활용하…

> [!tip] 우리에게 무엇인가
> 데이터셋 중심 시기는 지났다. 국내는 한국어 다문서 요약 데이터와 심사 메타리뷰 요약의 일치도 검증을 확보하는 것이 실익이다.

---

## S41 · 다국어 LLM 양자화·효율화

*제8부 · 멀티모달 인식·효율화* · **Multilingual Language Model Quantization** · *서브카테고리*

<sub>타임라인 분석 명칭: Multilingual Language Models, Compression & Efficiency</sub>

`46편` `2018–2026` `가속` `2025+ 24편`

<sub>멀티모달 인식·효율화 고유 배정 113편(중복 포함 434편 · 웹 인덱스 기준) · 서브카테고리 5개 · 본 파트 5개로 100% 커버</sub>

> [!quote] 파트 도입
> 작게 만들고 정확히 읽는 일이 배포의 조건이 됐다. 효율화와 도표 이해 모두 '동등성 검증'이 빠져 있다.

> [!abstract] 핵심 메시지
> 2026 양자화는 모델 전체가 아니라 구성요소·토큰·하드웨어 단위로 쪼개 따진다.

- 2026 Rethinking Small VLM Quantization이 sVLM을 vision encoder·projector·LLM backbone으로 분리해 Jetson Orin NX/AGX에서 검증했다.[2]
- 2026 ViToS가 의료 VLM의 시각 토큰을 pruning하고 token-sparse reasoning을 dual-stream RL로 함께 학습시킨다.
- 2026 SEAD, UniR, Bidirectional Evolutionary Search가 증류·plug-and-play 추론·자기개선으로 작은 모델의 성능을 끌어올린다.
- 2026 Prediction-Powered Inference Across Many Tasks와 TV 거리 추정이 효율화된 모델의 평가·출처 검증을 통계로 뒷받침한다.[1]
- 배경: 2018 BERT, 2019 XLM-R 이후 Gemma 2, Qwen2.5, DeepSeek-V3, Kimi k1.5가 효율 기반 모델 계열을 형성했다.

**대표 도구·시스템** — BERT · XLM-R · SimAlign · SPLADE v2 · DeepSeek-V3 · Qwen2.5 · Gemma 2 · Kimi k1.5 · SEAD · UniR · ViToS · SurpMark

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Prediction-Powered Inference Across Many Tasks for AI Evaluation](../../docs/papers/10231_Prediction-Powered_Inference_Across_Many_Tasks_for_AI_Evalua/index.html) — Nicolas Emmenegger 외, 2026
    - 여러 관련 task에 걸쳐 공유되는 proxy-ground truth 구조를 활용하여, task별 라벨이 극히 적은 상황에서도 통계적으로 유효한 신뢰구간과 점추정을 얻는 multi-task prediction-powered inference…
2. [Rethinking Small VLM Quantization: From Component-Wise Analysis to Hardware-Aware Edge Deployment](../../docs/papers/10335_Rethinking_Small_VLM_Quantization_From_Component-Wise_Analys/index.html) — Hyeju Shin 외, 2026
    - 3B 이하 소형 vision-language model(sVLM)을 vision encoder, projector, LLM backbone 세 요소로 분리하여 Jetson Orin NX/AGX에서 6가지 quantization 조합에 대한…
3. [Self-Improving Language Models with Bidirectional Evolutionary Search](../../docs/papers/10410_Self-Improving_Language_Models_with_Bidirectional_Evolutiona/index.html) — Guowei Xu 외, 2026
    - 본 논문은 forward evolutionary search와 backward goal decomposition을 결합한 Bidirectional Evolutionary Search (BES)를 제안하여, best-of-N sampling과…
4. [Token-Only Adaptation of Frozen Self-Supervised Vision Foundation Models for Cross-Species Animal Pose: A Pareto-Frontier Characterization Across Eight Held-Out Mammal Species](../../docs/papers/10594_Token-Only_Adaptation_of_Frozen_Self-Supervised_Vision_Found/index.html) — Ethan Y Wang 외, 2026 · 인용 979
    - frozen DINOv2-base backbone 위에 종(species)별로 학습된 단일 토큰(d=768)만을 최적화하여 cross-attention decoder를 조건화함으로써, 새로운 동물 종에 대한 pose estimation을 b…
5. [A survey of large language models](../../docs/papers/026_A_survey_of_large_language_models/index.html) — Wayne Xin Zhao 외, 2026.12 · 인용 114
    - 본 논문은 large language models(LLM)의 등장 배경, 기술적 진화 과정, 그리고 pre-training, adaptation tuning, utilization, capacity evaluation의 네 가지 핵심 측면을…

> [!tip] 우리에게 무엇인가
> 경량화는 이미 일상이다. 국내 기관은 원본 대비 성능·안전성 동등성을 재는 평가 체계를 갖춘 쪽이 배포 판단에서 앞선다.

---

## S42 · 과학 도표 캡셔닝

*제8부 · 멀티모달 인식·효율화* · **Scientific Figure Captioning** · *서브카테고리*

<sub>타임라인 분석 명칭: Scientific Figure Captioning & Scholarly Visual Generation</sub>

`24편` `2021–2026` `가속` `2025+ 9편`

> [!abstract] 핵심 메시지
> 캡션 생성에서 출발해 도표 읽기·그리기·논문 소통 자동화까지 번졌다.

- 2026 S1-MMAlign이 논문에서 수집한 대규모 이미지-텍스트 쌍을 초록·인용 맥락과 결합해 과학적으로 근거 있는 설명으로 바꿨다.[4]
- 2026 MatDeplot이 VLM이 line plot의 pixel-level grounding에 실패함을 정량화하고 축 보정된 (x, y) 곡선 복원 파이프라인을 제시했다.
- 2026 PaperBanana와 2025 Paper2poster·SciTalk가 논문에서 도식·포스터·영상을 만드는 에이전트 파이프라인으로 확장됐다.[1][2]
- 2026 MMClima가 텍스트·영상 전사본·figure를 아우르는 104k개 이상의 전문가 검증 QA 쌍으로 기후과학 멀티모달 평가를 구축했다.[3]
- 배경: 2021 SciCap이 도형-캡션 대규모 데이터셋을 열었고 2023 SciCap+, FigGen, AutomaTikZ가 이어졌다.

**대표 도구·시스템** — SciCap · SciCap+ · FigCaps-HF · AutomaTikZ/CLiMA · FigGen · MMSCI · SciFIBench · MatViX · PosterAgent · SciTalk · PaperBanana · S1-MMAlign

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Paper2poster: Towards multimodal poster automation from scientific papers](../../docs/papers/599_Paper2poster_Towards_multimodal_poster_automation_from_scien/index.html) — Wei Pang 외, 2025 · 인용 2
    - 본 논문은 과학 논문을 단일 페이지 학술 포스터로 자동 변환하는 첫 번째 벤치마크와 평가 지표 집합을 제시하며, 시각적-언어적 피드백 루프를 갖춘 다중 에이전트 파이프라인(PosterAgent)을 제안한다.
2. [PaperBanana: Automating Academic Illustration for AI Scientists](../../docs/papers/601_PaperBanana_Automating_Academic_Illustration_for_AI_Scientis/index.html) — Dawei Zhu 외, 2026.01 · 인용 1
    - 본 논문은 자율 AI 과학자(Autonomous AI Scientists)의 시각화 병목을 해결하기 위해, 에이전트 기반 프레임워크 PaperBanana를 제안한다. 이는 VLM(Vision Language Model)과 이미지 생성 모델을…
3. [MMClima: A Framework for Multimodal Climate Science Data and Evaluation](../../docs/papers/10042_MMClima_A_Framework_for_Multimodal_Climate_Science_Data_and/index.html) — Muhammad Umer Sheikh 외, 2026
    - MMClima는 텍스트, 비디오 전사본, 과학적 figure를 아우르는 104k개 이상의 전문가 검증 QA 쌍으로 구성된 대규모 멀티모달 기후과학 QA 벤치마크로, 자동 claim extraction과 QA synthesis에 human-i…
4. [S1-MMAlign: A Large-Scale, Multi-Disciplinary Dataset for Scientific Figure-Text Understanding](../../docs/papers/691_S1-MMAlign_A_Large-Scale_Multi-Disciplinary_Dataset_for_Scie/index.html) — He Wang 외, 2026.01
    - 과학 논문의 2.5백만 편에서 수집한 1,550만 개의 이미지-텍스트 쌍으로 구성된 대규모 멀티모달 데이터셋을 제시한다. Qwen-VL 기반 의미 강화 파이프라인을 통해 희소한 원본 캡션을 논문의 추상, 인용 맥락과 결합하여 자급식의 과학적…

> [!tip] 우리에게 무엇인가
> 도표는 논문의 증거 단위다. 국내에서는 재료·기후처럼 도표 비중이 큰 분야부터 곡선 복원과 구조화 추출을 쓸 만하다.

---

## S43 · AutoML 도메인 전이

*제8부 · 멀티모달 인식·효율화* · **Cross-Domain Transferability in AutoML** · *서브카테고리*

<sub>타임라인 분석 명칭: Cross-Domain Transferability, Retrieval & AutoML</sub>

`16편` `2020–2026` `안정` `2025+ 7편`

> [!abstract] 핵심 메시지
> 2026 전이 논의는 RAG·AutoML에서 도메인 비전 벤치마크의 맹점 진단으로 옮겨 갔다.

- 2026 VT-Bench가 시각-표 형식 멀티모달 학습을 판별·생성 두 패러다임에서 아우르는 최초의 통합 벤치마크로 나왔다.[3]
- 2026 LabProc and Tacit이 frontier VLM이 motion-only 상태 구분에 구조적 맹점이 있음을 보이고 도메인 적응 video encoder Tacit을 제안했다.[4]
- 2026 IVQA-LD가 사지 결손 인구용 전문가 주석 데이터셋으로 VLM이 이 도메인에서 심각하게 취약함을 드러냈다.[2]
- 2025 GeoFactory가 RAG·프롬프트·미세조정·에이전트를 지구과학 과업에서 평가하고 앙상블 프레임워크로 묶었다.[1]
- 배경: 2020 REALM·RAG와 Don't Stop Pretraining, 2023 AutoML-GPT가 전이·검색 증강의 틀을 놓았다.

**대표 도구·시스템** — REALM · RAG · Atlas · AutoML-GPT · GeoFactory · VT-Bench · Tacit · IVQA-LD

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [GeoFactory: an LLM performance enhancement framework for geoscience factual and inferential tasks](../../docs/papers/10764_geofactory_an_llm_performance_enhancement_framework_fo/index.html) — Zhou Chen 외, 2025.05 · 인용 6
    - GeoFactory는 RAG, prompt engineering, fine-tuning, agent라는 4가지 LLM 성능 향상 방법과 14개 세부 알고리즘을 지구과학의 factual/inferential 과업에서 실증 평가하고, 이들을 앙…
2. [IVQA-LD: Inclusive Multimodal Understanding for Population with Limb Deficiency](../../docs/papers/9853_IVQA-LD_Inclusive_Multimodal_Understanding_for_Population_wi/index.html) — Yan Ke 외, 2026
    - 사지 결손(limb deficiency) 인구를 위한 최초의 대규모 전문가 주석 vision-language 데이터셋인 IVQA-LD를 구축하고, VLM들이 이 도메인에서 심각하게 취약함을 보인 뒤, 신체 구조 인식을 반영한 BSI(Body…
3. [VT-Bench: A Unified Benchmark for Visual-Tabular Multi-Modal Learning](../../docs/papers/10685_VT-Bench_A_Unified_Benchmark_for_Visual-Tabular_Multi-Modal/index.html) — Ziyi Jia 외, 2026
    - VT-Bench는 visual-tabular multi-modal learning을 위한 최초의 통합 벤치마크로, discriminative prediction과 generative reasoning 두 패러다임을 동시에 아우르며 9개 도메…
4. [LabProc and Tacit: Quantifying the Visual-Textual Prior Gap in Autonomous Laboratory Perception](../../docs/papers/9870_LabProc_and_Tacit_Quantifying_the_Visual-Textual_Prior_Gap_i/index.html) — Jagrati Gogia 외, 2026
    - 자율 실험실 시스템의 인식 계층으로 널리 쓰이는 frontier VLM이 실제로는 motion-only 상태 구분에 구조적 맹점을 가진다는 것을 6개 과제로 구성된 LabProc 벤치마크로 정량화하고, 300M 파라미터의 도메인 적응 vid…

> [!tip] 우리에게 무엇인가
> 범용 VLM은 도메인에서 쉽게 깨진다. 국내 현장 데이터로 맹점을 재는 소규모 벤치마크가 가장 값싼 투자다.

---

## S44 · 차트 추론·팩트체크

*제8부 · 멀티모달 인식·효율화* · **Chart Reasoning & Fact-Checking** · *서브카테고리*

<sub>타임라인 분석 명칭: Chart Reasoning, Instruction Tuning & Fact-Checking</sub>

`14편` `2023–2026` `가속` `2025+ 6편`

> [!abstract] 핵심 메시지
> 2025–2026 차트 추론은 지시 튜닝 물결을 지나 반성·에이전트·RL 일반화 검증으로 이동했다.

- 2025 ChartSketcher가 중간 추론을 차트에 직접 주석으로 그리고 다시 입력하는 Sketch-CoT로 반성형 차트 추론을 시도했다.[5]
- 2025 Multimodal deepresearcher가 시각화를 FDV로 구조화 텍스트화해 텍스트-차트 교차 보고서를 처음부터 생성한다.[4]
- 2025 SFT Memorizes, RL Generalizes가 규칙 기반 추론·시각 과업에서 RL의 일반화 우위를 보였다.[1]
- 2026 Diversity Over Frequency가 tool-use collapse를 규명했고, Can Vision Language Models Learn Intuitive Physics from Interaction?은 부정적 결과를 냈다.[2]
- 배경: 2023 ChartBERT 이후 ChartLlama, ChartAssistant, MMC, ChartInstruct, ChartGemma, ChartX/ChartVLM, SynChart가 지시 튜닝 물결을 이뤘다.

**대표 도구·시스템** — ChartBERT · ChartLlama · ChartAssistant · ChartGemma · ChartVLM · SynChart · ChartSketcher · Chartist · Multimodal DeepResearcher

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [SFT Memorizes, RL Generalizes: A Comparative Study of Foundation Model Post-training](../../docs/papers/751_SFT_Memorizes_RL_Generalizes_A_Comparative_Study_of_Foundati/index.html) — Tianzhe Chu 외, 2025 · 인용 6
    - 본 논문은 기초 모델의 사후훈련(post-training) 단계에서 지도학습 미세조정(SFT)과 강화학습(RL)의 일반화(generalization) 능력을 비교하는 체계적 연구로, RL은 규칙 기반 추론과 시각 작업에서 우수한 일반화 성능…
2. [Can Vision Language Models Learn Intuitive Physics from Interaction?](../../docs/papers/9373_Can_Vision_Language_Models_Learn_Intuitive_Physics_from_Inte/index.html) — Luca M. Schulze Buschoff 외, 2026
    - Vision language model이 시뮬레이션 환경과의 interaction(강화학습, GRPO)을 통해 학습하더라도, supervised fine-tuning(SFT)과 마찬가지로 일반화 가능한 intuitive physics 직관을…
3. [Chartist: Task-driven Eye Movement Control for Chart Reading](../../docs/papers/200_Chartist_Task-driven_Eye_Movement_Control_for_Chart_Reading/index.html) — Danqing Shi 외, 2025 · 인용 13
    - Chartist는 차트를 읽을 때 사용자의 분석 task(value retrieval, filtering, find extreme)에 따라 달라지는 인간의 시선 이동 scanpath를 예측하는 계산 모델로, LLM 기반 고수준 인지 cont…
4. [Multimodal deepresearcher: Generating text-chart interleaved reports from scratch with agentic framework](../../docs/papers/566_Multimodal_deepresearcher_Generating_text-chart_interleaved/index.html) — Zhaorui Yang 외, 2025 · 인용 3
    - 본 논문은 대규모 언어 모델(LLM)을 활용하여 텍스트와 차트가 유기적으로 통합된 멀티모달 보고서를 자동으로 생성하는 시스템을 제안한다. 핵심 혁신은 시각화를 구조화된 텍스트 표현(FDV: Formal Description of Visual…
5. [ChartSketcher: Reasoning with multimodal feedback and reflection for chart understanding](../../docs/papers/203_Chartsketcher_Reasoning_with_multimodal_feedback_and_reflect/index.html) — Muye Huang 외, 2025
    - 본 논문은 멀티모달 대규모 언어 모델(MLLM)이 차트를 이해할 때 시각적 피드백을 통한 반복적 스케칭(Sketch-CoT)으로 추론 과정을 개선하는 방법을 제안한다. 인간의 인지 행동에서 영감을 받아, 모델이 중간 추론 단계를 차트에 직접…

> [!tip] 우리에게 무엇인가
> 차트 이해는 데이터 규모 경쟁이 끝나고 추론 방식 경쟁이 됐다. 국내 보고서·통계 자료로 사실 검증 평가를 설계할 가치가 있다.

---

## S45 · 도시 장면 이해

*제8부 · 멀티모달 인식·효율화* · **Cross-View Urban Scene Understanding** · *서브카테고리*

<sub>타임라인 분석 명칭: Cross-View, Spatial & Video Scene Understanding</sub>

`13편` `2023–2026` `부상` `2025+ 10편`

> [!abstract] 핵심 메시지
> 2026 위성·거리뷰 융합 모델과 시공간 벤치마크가 한꺼번에 나오며 칸이 열렸다.

- 2026 UrbanMLLM이 cross-view perceiver와 structural interleaved pre-training으로 위성·거리뷰를 통합 학습하고 13개 도시 이해 태스크에서 향상을 보였다.
- 2026 UrbanFusion이 Stochastic Multimodal Fusion으로 거리뷰·원격탐사·지도·POI 중 임의 부분집합에서도 강건한 표현을 학습한다.[4]
- 2026 TimeSpot이 이미지 하나로 시간·지리 속성을 예측하게 해, 최신 VLM이 특히 시간 추론에서 저조함을 실증했다.[3]
- 2026 FrontierSpatial이 7,838개 질문 규모의 통합 공간 추론 벤치마크를, SciVideoBench가 연구 수준 실험 영상 추론 평가를 제시했다.[2]
- 배경: 2023 Gemini, 2024 Gemini 1.5가 백만 토큰 컨텍스트의 네이티브 멀티모달 기반을 놓았다.

**대표 도구·시스템** — Gemini · Gemini 1.5 · Pelican · DEFAME · UrbanFusion · UrbanMLLM · TimeSpot · FrontierSpatial · SciVideoBench · TikZero

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Visual thoughts: A unified perspective of understanding multimodal chain-of-thought](../../docs/papers/869_Visual_thoughts_A_unified_perspective_of_understanding_multi/index.html) — Zihui Cheng 외, 2025
    - 대규모 비전-언어 모델(LVLM)의 멀티모달 체인-오브-쏘트(MCoT) 추론에서 시각적 사고(Visual Thoughts)라는 통합된 메커니즘을 발견하였으며, 이는 텍스트 기반과 이미지 교차 방식의 MCoT 모두를 설명하는 새로운 관점을 제…
2. [SciVideoBench: Benchmarking Scientific Video Reasoning in Large Multimodal Models](../../docs/papers/10395_SciVideoBench_Benchmarking_Scientific_Video_Reasoning_in_Lar/index.html) — Andong Deng 외, 2026
    - SciVideoBench는 연구 수준(research-level)의 과학 실험 비디오에 대한 고난도 추론 능력을 평가하기 위한 새로운 비디오 벤치마크로, 25개 이상의 전문 학문 분야에서 수집된 실험 영상을 기반으로 1,000개의 정교한 m…
3. [TimeSpot: Benchmarking Geo-Temporal Understanding in Vision–Language Models in Real-World Settings](../../docs/papers/10589_TimeSpot_Benchmarking_Geo-Temporal_Understanding_in_VisionLa/index.html) — Azmine Toushik Wasi 외, 2026
    - TimeSpot는 ground-level 이미지만으로 시간(계절, 월, 시각, 낮/밤 단계)과 지리(대륙, 국가, 기후대, 환경 유형, 위경도) 속성을 구조화된 형태로 동시에 예측하도록 요구하는 geo-temporal reasoning 벤치…
4. [UrbanFusion: Stochastic Multimodal Fusion for Contrastive Learning of Robust Spatial Representations](../../docs/papers/10667_UrbanFusion_Stochastic_Multimodal_Fusion_for_Contrastive_Lea/index.html) — Dominik J. Mühlematter 외, 2026
    - UrbanFusion은 street view imagery, remote sensing, cartographic maps, POIs 등 다양한 지리공간 모달리티를 Stochastic Multimodal Fusion(SMF)이라는 대조학습 프…

> [!tip] 우리에게 무엇인가
> 13편의 작은 칸이지만 대부분 2026년이다. 국내 위성·거리뷰 데이터를 가진 기관은 도시 모델링 입력으로 바로 쓸 수 있다.

---

## S46 · 인과 독립성 검정

*제9부 · 인과·통계 추론* · **Causal Independence Testing** · *서브카테고리*

`53편` `2026–2026` `가속` `2025+ 53편`

<sub>인과·통계 추론 고유 배정 108편(중복 포함 590편 · 웹 인덱스 기준) · 서브카테고리 4개 · 본 파트 4개로 100% 커버</sub>

> [!quote] 파트 도입
> AI 결과를 검정·신뢰구간으로 인증하는 일이 다른 대분류를 떠받치는 인프라가 됐다. 리더보드 1위조차 동전 던지기일 수 있다는 반증이 함께 나왔다.

> [!abstract] 핵심 메시지
> 2026 검정은 사후 감사가 아니라 배포 중 상시 보증으로 이동했다.

- 2026 Minimax-Optimal Kernel Two-sample Testing in Sub-quadratic Time이 MMD 검정을 이차 시간에서 준이차 시간으로 낮추고도 minimax 검정력을 유지했다.[1]
- 2026 Semi-knockoffs와 Knockoff-C2ST가 사전학습 임의 모델 위에서 유한 표본 FDR 통제를 제공해, 어느 좌표가 shift 됐는지 짚는다.[3][4]
- 2026 Multi-View Causal Discovery without Non-Gaussianity(LiMVAM)가 비가우시안 가정 없이 이차 통계량만으로 식별 가능성을 증명했다.[2]
- 2026 WATCH, DP-SPRT, Membership Circuits가 배포 모델의 감시·프라이버시 감사·OOD 탐지에 type I error 보장을 붙였다.
- 배경: 이 칸의 논문은 모두 2026년 것이다. 검정 이론이 AI 시스템 검증 도구로 옮겨 간 시점이 지난 한 해로 압축돼 있다.

**대표 도구·시스템** — MMD/HSIC · Semi-knockoffs · Knockoff-C2ST · WATCH (weighted conformal test martingales) · DP-SPRT · PLaCy · ReTimeCausal · CaDRe · λ-PSD · Membership Circuits · Anytime Tracking CUSUM

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Minimax-Optimal Kernel Two-sample Testing in Sub-quadratic Time](../../docs/papers/10034_Minimax-Optimal_Kernel_Two-sample_Testing_in_Sub-quadratic_T/index.html) — Ikjun Choi 외, 2026
    - MMD 기반 kernel two-sample test를 quadratic time O(N^2 d) 대신 subquadratic time O((2 log N)^d N)에 계산하면서도 minimax-optimal power를 유지하는 방법을 제…
2. [Multi-View Causal Discovery without Non-Gaussianity: Identifiability and Algorithms](../../docs/papers/10071_Multi-View_Causal_Discovery_without_Non-Gaussianity_Identifi/index.html) — Ambroise Heurtebise 외, 2026
    - 이 논문은 non-Gaussianity 가정 없이도 여러 view 간 상관관계(second-order statistics, SOS)를 활용해 linear SEM의 causal discovery를 식별 가능하게 만드는 multi-view 모델…
3. [Knockoff-C2ST: False Discovery Controlled Attribution of Distribution Shift](../../docs/papers/9863_Knockoff-C2ST_False_Discovery_Controlled_Attribution_of_Dist/index.html) — Şuayp Talha Kocabay 외, 2026 · 인용 113
    - Classifier two-sample test(C2ST)의 feature attribution을 Model-X knockoff와 sign-symmetric contrast statistic으로 보강하여, 상관된 covariate 하에서도…
4. [Semi-knockoffs: a model-agnostic conditional independence testing method with finite-sample guarantees](../../docs/papers/10416_Semi-knockoffs_a_model-agnostic_conditional_independence_tes/index.html) — Angel David REYERO LOBO 외, 2026
    - Semi-knockoffs는 사전학습된 임의의 ML 모델을 그대로 활용하면서도 train-test split 없이 유한 표본에서 유효한 p-value와 FDR 제어를 제공하는 model-agnostic conditional independe…

> [!tip] 우리에게 무엇인가
> AI 결과물에 p-value와 FDR 보증을 요구하는 문화가 먼저 자리 잡는 쪽이 이긴다. 통계 인력은 보조가 아니라 검증 인프라 팀이다.

---

## S47 · 관찰 데이터 처치 정책

*제9부 · 인과·통계 추론* · **Observational Treatment Policy Evaluation** · *서브카테고리*

`23편` `2025–2026` `가속` `2025+ 23편`

> [!abstract] 핵심 메시지
> 2025–2026 관찰 데이터의 처치 정책 학습은 효과 추정에서 위험 통제로 넘어갔다.

- 2026 DeepBlip이 SNMM의 g-estimation을 신경망으로 구현해 시간에 따른 CATE를 blip effect로 추정한다.[3]
- 2026 Smooth Multi-Policy Causal Effect Estimation in Longitudinal Settings가 여러 동적 치료 정책을 한 번에 평가하며 이차 편향을 통제한다.[2]
- 2026 Act or Defer와 Missingness-Aware Conformal Prediction이 EHR 모델에 클래스별 FDR 통제와 병원 간 coverage 보장을 붙였다.[5]
- 2026 TwinWeaver가 종단 환자 기록을 텍스트로 직렬화해 Genie Digital Twin을 만들고, 93,054명 20개 암종 데이터로 학습했다.
- 배경: Safety Generalization Under Distribution Shift in Safe Reinforcement Learning은 학습 시 안전 제약이 배포 환경 분포 변화에서도 유지되는지를 따로 시험해야 함을 보인다.[1]

**대표 도구·시스템** — DeepBlip · GRACE · Spatial Deconfounder · GIFT · GVALID · LSTM-PPO dosing · NOF1-BCD · TwinWeaver/Genie Digital Twin · Mondrian conformal calibration · IGRL

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Safety Generalization Under Distribution Shift in Safe Reinforcement Learning: A Diabetes Testbed](../../docs/papers/10362_Safety_Generalization_Under_Distribution_Shift_in_Safe_Reinf/index.html) — Minjae Kwon 외, 2026
    - 본 논문은 당뇨병 관리를 안전 필수(safety-critical) 테스트베드로 삼아, 학습 시점의 safe RL 제약 만족이 분포 변화(distribution shift)가 있는 배포 환경에서도 유지되는지를 검증하고, test-time pr…
2. [Smooth Multi-Policy Causal Effect Estimation in Longitudinal Settings](../../docs/papers/10460_Smooth_Multi-Policy_Causal_Effect_Estimation_in_Longitudinal/index.html) — Wenxin Chen 외, 2026
    - 여러 개의 동적 치료 정책(dynamic treatment policy)을 종단자료(longitudinal data)에서 동시에 평가할 때, 기존처럼 정책마다 별도로 ICE Q-function을 추정하면 LTMLE로 디바이어싱해도 구조적으로…
3. [DeepBlip: Estimating Conditional Average Treatment Effects Over Time](../../docs/papers/9495_DeepBlip_Estimating_Conditional_Average_Treatment_Effects_Ov/index.html) — Haorui Ma 외, 2026
    - DeepBlip는 structural nested mean models(SNMMs)의 g-estimation을 신경망 기반으로 구현하여, 시간에 따른 conditional average treatment effect(CATE)를 blip e…
4. [Learning Clinical-Trial Strategy: Offline Policy Training for Decision Agents](../../docs/papers/9900_Learning_Clinical-Trial_Strategy_Offline_Policy_Training_for/index.html) — William James Bolton 외, 2026
    - 임상시험 전략 수립을 date-gated offline decision-making 문제로 정식화하고, 45개 종양학 약물 프로그램에서 881개의 (state, action, reward) 에피소드로 구성된 시계열 데이터셋을 구축하여 beh…
5. [Missingness-Aware Conformal Prediction Under Cross-Hospital Distribution Shift](../../docs/papers/10036_Missingness-Aware_Conformal_Prediction_Under_Cross-Hospital/index.html) — Liang You 외, 2026
    - 병원 간 배포 시 missingness pattern 차이로 인해 exchangeability 가정이 깨지면서 표준 split conformal prediction (CP)이 subgroup 단위에서 심각한 coverage gap을 숨긴다는…

> [!tip] 우리에게 무엇인가
> 임상·정책 데이터의 AI 의사결정은 예측 정확도가 아니라 보증 가능한 위험 상한으로 평가받는다. 국내 병원 데이터 연계 사업은 이 요건부터 설계해야 한다.

---

## S48 · 통계 검정·리더보드

*제9부 · 인과·통계 추론* · **Statistical Testing & Leaderboard Rankings** · *서브카테고리*

`16편` `2024–2026` `부상` `2025+ 14편`

> [!abstract] 핵심 메시지
> 2025–2026 리더보드 1위는 신뢰구간 없이는 의미가 없다는 반증이 쌓였다.

- 2026 The Leaderboard Lottery가 점추정 1위 선정을 post-selection inference 문제로 짚으며 상위 순위가 동전 던지기일 수 있다고 보였다.
- 2026 Quantifying Ranking Uncertainty in LLM Benchmarks가 MMLU 등 다과제 벤치마크 순위에 rank CI를 적용했다.[1]
- 2026 Resolution Diagnostics for Paired LLM Evaluation이 필요 표본 N*와 관측 N의 비 q를 진단 지표로 제안했다.[2]
- 2026 Sticks and Stones가 28,000 trial 규모의 사전등록 실험으로 EmotionPrompt의 8–115% 효과가 재현되지 않음을 보였다.
- 배경: Predicting field experiments with large language models는 276개 실험에서 78% 예측 정확도를 보고해, LLM이 가설 선별에 쓰이는 방향도 열었다.[3]

**대표 도구·시스템** — MBTIBENCH · SciPredict · TasteBench · CELEUS · rank CI / resolution ratio q · paired-bootstrap MCS · R-IDeA · Structural Specificity Testing

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Quantifying Ranking Uncertainty in LLM Benchmarks](../../docs/papers/10284_Quantifying_Ranking_Uncertainty_in_LLM_Benchmarks/index.html) — Bitya Neuhof 외, 2026 · 인용 2
    - MMLU와 같은 multi-task 벤치마크에서 LLM 순위의 불확실성을 정량화하기 위해, pairwise hypothesis test를 기반으로 한 rank confidence interval(rank CI) 방법을 적용하고, subjec…
2. [Resolution Diagnostics for Paired LLM Evaluation](../../docs/papers/10326_Resolution_Diagnostics_for_Paired_LLM_Evaluation/index.html) — Anany Kotawala, 2026
    - LLM 리더보드의 pairwise 순위 비교를 paired hypothesis-testing 문제로 재정의하고, 실제 paired 평가 설계 하에서 요구되는 표본 크기 N*와 관측된 N의 비율인 resolution ratio q를 진단 지표…
3. [Predicting field experiments with large language models](../../docs/papers/631_Predicting_field_experiments_with_large_language_models/index.html) — Yaoyu Chen 외, 2025
    - 대규모 언어 모델(LLM)을 이용하여 경제학 문헌의 현장 실험(field experiment) 결과를 자동으로 예측하는 프레임워크를 제안하고, 276개 실험에서 78%의 예측 정확도를 달성했다.
4. [Representative, Informative, and De-Amplifying: Requirements for Robust Bayesian Active Learning under Model Misspecification](../../docs/papers/1100_Representative_Informative_and_De-Amplifying_Requirements_fo/index.html) — Roubing Tang 외, 2026.03
    - 베이지안 최적실험설계(BOED) 하에서 모델 오명시(model misspecification)로 인한 일반화 오차를 분석하고, 대표성(representativeness), 정보성(informativeness), 오차 완화(de-amplifi…
5. [The Leaderboard Lottery: Why Top LLM Rankings Are Often Coin Flips, and How to Fix Them](../../docs/papers/10572_The_Leaderboard_Lottery_Why_Top_LLM_Rankings_Are_Often_Coin/index.html) — Shourya Vir Jain, 2026
    - LLM 리더보드에서 point-estimate 기반 1위 선정은 N개 모델에 대한 post-selection inference 문제임을 지적하고, marginal confidence interval이 "top-ranked 모델이 진짜 최고인…
6. [Confidence in Large Language Model Evaluation: A Bayesian Approach to Limited-Sample Challenges](../../docs/papers/237_Confidence_in_Large_Language_Model_Evaluation_A_Bayesian_App/index.html) — Xiao Xiao 외, 2025
    - 본 논문은 제한된 샘플 크기 조건에서 대규모언어모델(LLM)을 평가하기 위해 베이지안 추론을 활용한 새로운 방법론을 제시한다. 사전지식(Prior Knowledge)을 통합하여 모델 간 순위를 확률적으로 추정하며, 결정론적 메트릭의 한계를…

> [!tip] 우리에게 무엇인가
> 모델 선정 보고서에는 순위가 아니라 순위 신뢰구간과 표본 해상도를 요구해야 한다. 국내 벤치마크 평가 사업의 첫 번째 개선점이다.

---

## S49 · 중도절단 생존분석

*제9부 · 인과·통계 추론* · **Survival Analysis with Censoring** · *서브카테고리*

`16편` `2026–2026` `부상` `2025+ 16편`

> [!abstract] 핵심 메시지
> 2026 생존분석은 예측에서 생성·증류·해석의 부품화 단계로 들어섰다.

- 2026 SurvDiff가 혼합형 공변량, 사건 시간, 우측 중도절단을 하나의 end-to-end diffusion으로 합성 생성한다.[2]
- 2026 DiSKD가 경쟁위험 생존분석에서 외부 teacher 예측을 cause-specific KL로 내부 student에 증류한다.
- 2026 SurvFD와 SurvSHAP-IQ가 hazard를 시간의존·비의존 성분으로 분해해 시간축 포함 고차 상호작용을 정량화한다.
- 2026 FunCQNet이 eGFR trajectory를 반영해 신장이식 후 장기 생존시간의 다중 분위수를 예측한다.[4]
- 배경: 합성 ECG의 Empirical-Distribution Matching은 CV·NLP식 클래스 재균형이 성능을 해치고 naive bootstrap이 최우수라고 보였다.

**대표 도구·시스템** — SurvDiff · DiSKD · SurvFD / SurvSHAP-IQ · FunCQNet · SYSURV · PaX · MLCI (nHSIC) · ScoreStop · DCDM-ECG · Random Survival Forest

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [ScoreStop: Gradient-based early stopping using functional score tests](../../docs/papers/10397_ScoreStop_Gradient-based_early_stopping_using_functional_sco/index.html) — Oliver J. Hines 외, 2026
    - ScoreStop은 gradient boosting에서 각 반복마다 현재 예측기가 population risk minimizer인지 검정하는 functional score test 기반의 early stopping 규칙으로, scale-in…
2. [SurvDiff: A Diffusion Model for Generating Synthetic Data in Survival Analysis](../../docs/papers/10520_SurvDiff_A_Diffusion_Model_for_Generating_Synthetic_Data_in/index.html) — Marie Brockschmidt 외, 2026
    - SurvDiff는 mixed-type covariates, event time, right-censoring을 하나의 end-to-end diffusion model로 결합 생성하고 survival-tailored loss로 학습하여, 기존…
3. [Discrete Survival Knowledge Distillation for Competing Risks Analysis](../../docs/papers/9522_Discrete_Survival_Knowledge_Distillation_for_Competing_Risks/index.html) — Feiyang Deng 외, 2026
    - 경쟁위험(competing risks) 생존분석에서 검열된 관측치와 teacher-student 간 outcome 정의 이질성을 다루는 discrete-time knowledge distillation 프레임워크인 DiSKD를 제안하고, c…
4. [FunCQNet: A Functional Censored Quantile Neural Network for Predicting Long-Term Post-Transplant Kidney Survival](../../docs/papers/9706_FunCQNet_A_Functional_Censored_Quantile_Neural_Network_for_P/index.html) — Jiaqi Men 외, 2026
    - FunCQNet은 functional biomarker(예: eGFR trajectory)와 scalar covariate 간 상호작용을 반영하는 quantile-specific coefficient function을 deep neural…

> [!tip] 우리에게 무엇인가
> 병원 데이터의 외부 반출이 어려운 환경에서는 합성 생성과 모델 증류가 현실적 돌파구다. 단, 중도절단 처리 방식의 검증이 먼저다.

---

## S50 · 기계학습 원자간 포텐셜

*제10부 · 계산 재료 시뮬레이션* · **Machine-Learned Interatomic Potentials** · *서브카테고리*

`37편` `2023–2026` `가속` `2025+ 35편`

<sub>계산 재료 시뮬레이션 고유 배정 107편(중복 포함 559편 · 웹 인덱스 기준) · 서브카테고리 4개 · 본 파트 4개로 100% 커버</sub>

> [!quote] 파트 도입
> 해자는 모델이 아니라 DFT 계산 데이터다. 생성은 값싸졌고 합성 가능성과 독립 재현이 병목이다.

> [!abstract] 핵심 메시지
> 2026 MLIP는 DFT 대체재로 자리 잡았고, 경쟁은 오차 수치에서 곡률·불확실성으로 옮겨 갔다.

- 2026 MACE-OMol25 기반 자동 전이상태 탐색이 유기계에서 96.6% 성공률, DFT 비용 94-96% 절감을 보였다.
- 2026 'A New Paradigm for Computational Chemistry'가 파운데이션 MLIP가 향후 10년 내 DFT의 주도적 지위를 대체할 수 있다고 주장했다.[1]
- 2026 Hi-MLIP/HINT는 에너지·힘 RMSE 대신 Hessian(PES 곡률)을 학습 신호로 삼아 자유 에너지와 초전도 특성까지 겨냥했다.
- 2026 Smooth Dynamic Cutoffs, RANGE, TriForces, Bayesian Last Layer 등 효율·장거리·불확실성 개선이 MACE·NequIP·ORB-v3·TensorNet 위에 쌓인다.
- 배경: 2023 QH9가 해밀토니안 행렬 예측을 학습 목표로 세웠고, 이후 DenSNet·QHNetV2로 전자 구조 직접 예측이 이어졌다.

**대표 도구·시스템** — MACE · MACE-OMol25 · QHNetV2 · ORB-v3 · NequIP · TensorNet · PFP/MM · MDtrajNet-1 · DenSNet · BLIPs · CEITNet · AllScAIP · RANGE · fix pimd/langevin (LAMMPS)

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [A New Paradigm for Computational Chemistry](../../docs/papers/2995_A_New_Paradigm_for_Computational_Chemistry/index.html) — Raphael T. Husistein 외, 2026.04 · 인용 1
    - 이 논문은 machine learning interatomic potentials (MLIPs) 기반 파운데이션 모델이 DFT를 대체할 수 있는 새로운 계산화학 패러다임을 제시한다. 양자 정확도와 force-field 수준의 속도를 동시에…
2. [Data-driven construction of machine-learning-based interatomic potentials for gas-surface scattering dynamics: the case of NO on graphite](../../docs/papers/3066_Data-driven_construction_of_machine-learning-based_interatom/index.html) — 2026.03 · 인용 9
    - 본 논문은 ab initio MD 시뮬레이션으로부터 생성한 데이터에 기반하여 NO/HOPG 기체-표면 산란 역학 연구용 머신러닝 포텐셜을 개발한다. SOAP 디스크립터, 주성분분석, 먼점 샘플링, Deep Potential 모델, 그리고 q…
3. [Reliable and Efficient Automated Transition-State Searches with Machine-Learned Interatomic Potentials](../../docs/papers/3229_Reliable_and_Efficient_Automated_Transition-State_Searches_w/index.html) — 2026.04 · 인용 2
    - 본 연구는 MLIP를 활용한 자동 반응 경로 탐색 워크플로우를 체계적으로 벤치마킹하여, MACE-OMol25가 유기계에서 96.6% 성공률을 달성하면서 DFT 계산 비용을 94-96% 감소시킬 수 있음을 입증한다. 이는 전자구조 계산의 계산…
4. [Smooth Dynamic Cutoffs for Machine Learning Interatomic Potentials](../../docs/papers/10459_Smooth_Dynamic_Cutoffs_for_Machine_Learning_Interatomic_Pote/index.html) — Kevin Han 외, 2026
    - 고정된(fixed) cutoff radius를 사용해야 한다는 기존 통념에 도전하여, 목표 이웃 수(target number of neighbors)에 맞춰 반경이 부드럽게 조절되는 smooth dynamic cutoff 함수를 제안하고,…

> [!tip] 우리에게 무엇인가
> 범용 MLIP는 이미 공개 자산이다. 차별점은 우리 계에 맞는 DFT 학습 데이터와, 장거리·무질서 구조에서 모델이 틀리는 지점을 아는 검증 능력이다.

---

## S51 · 생성형 무기 재료 설계

*제10부 · 계산 재료 시뮬레이션* · **Generative Inorganic Materials Discovery** · *서브카테고리*

`33편` `2023–2026` `가속` `2025+ 30편`

> [!abstract] 핵심 메시지
> 생성은 값싸졌다. 2026의 목표함수는 합성 가능성이고, 검증 부담은 그대로다.

- 2026 MatterGen을 MatInvent 기반 다목적 강화학습으로 미세조정해 목표 물성과 전구체 기반 합성 가능성을 함께 최적화했다.
- 2026 DiffSyn은 23,961건의 제올라이트 합성 레시피로 학습한 확산 모델로 확률적 합성 경로를 만들고 UFI 소재 합성으로 검증했다.[2]
- 2026 WyFormer와 uMLIP를 묶은 생성-스크리닝-검증 파이프라인이 고체전지 보호코팅 소재를 DB 밖에서 찾는다.
- 2026 GLASS와 MUSE는 분광 데이터에서 비정질 구조와 분자를 역으로 생성하고, 에이전트 Ara는 광촉매 COF에서 무작위 대비 11.5배(52.7%)의 hit rate를 냈다.
- 배경: 2023 GNoME가 안정 결정 220만 개를 발굴해 알려진 안정 물질을 약 10배 늘렸으나, 합성·재현 검증은 별개 문제로 남았다.

**대표 도구·시스템** — GNoME · MatterGen · MatterGen-e- · MatterGPT/SLICES · CatFlow · WyFormer · DiffSyn · GLASS · MUSE · SR-CGCNN · DISSOLVR · Open Electrolyte Databank · Ara agent

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Generative design of inorganic materials](../../docs/papers/3115_Generative_design_of_inorganic_materials/index.html) — 2026.04 · 인용 10
    - 본 논문은 무기 소재의 생성형 설계를 위해 물리기반 재료 표현, 파운데이션 AI 모델, 고처리량 실험 검증의 세 가지 핵심 요소를 닫힌 루프로 통합하는 통합 프레임워크를 제안한다. 이는 데이터 주도 역설계를 통해 조성, 구조, 결함을 포함한…
2. [DiffSyn: a generative diffusion approach to materials synthesis planning](../../docs/papers/3077_DiffSyn_a_generative_diffusion_approach_to_materials_synthes/index.html) — Elton Pan 외, 2026.02 · 인용 6
    - DiffSyn은 50년치 23,961건의 제올라이트 합성 레시피로 학습된 generative diffusion model으로, 목표 제올라이트 구조와 유기 템플릿이 주어졌을 때 확률적 합성 경로를 생성하며, 실제 UFI 소재 합성을 통해 검…
3. [Generative Chemical Language Models for Energetic Materials Discovery](../../docs/papers/3114_Generative_Chemical_Language_Models_for_Energetic_Materials/index.html) — 2026.03
    - 약학 중심으로 발전한 화학 언어모델을 에너지 물질 도메인으로 전이학습을 통해 확장하고, fragment 기반 분자 인코딩으로 합성 가능 구조 생성 능력을 향상시킨 generative AI 프레임워크를 제시한다.
4. [Generative Pipeline for Discovering Solid-State Battery Materials with Universal Atomistic Potentials](../../docs/papers/9727_Generative_Pipeline_for_Discovering_Solid-State_Battery_Mate/index.html) — Artem Dembitskiy 외, 2026 · 인용 139
    - 이 논문은 WyFormer 생성모델과 uMLIP(범용 원자간 포텐셜)를 결합하여 고체전지용 보호코팅 소재를 발굴하는 3단계 계산 파이프라인(생성-스크리닝-검증)을 제안한다. 기존 데이터베이스에 없는 새로운 결정구조를 생성하고, uMLIP 기…

> [!tip] 우리에게 무엇인가
> 후보 생성은 이제 차별점이 아니다. 합성 레시피와 독립 재분석까지 닫는 실험 파트너가 있어야 생성 결과가 자산이 된다.

---

## S52 · 고온 합금 포텐셜

*제10부 · 계산 재료 시뮬레이션* · **High-Temperature Alloy Potentials** · *서브카테고리*

<sub>타임라인 분석 명칭: High-Temperature Alloy & Extreme-Condition Potentials</sub>

`19편` `2023–2026` `가속` `2025+ 17편`

> [!abstract] 핵심 메시지
> 2026 합금·용융 계로 범위가 넓어졌고, 회절 실험이 장거리 MLIP의 한계를 드러냈다.

- 2026 NEP 기반 CrCoNi 중엔트로피 합금 범용 포텐셜이 제1원리 정확도로 대규모 원자 시뮬레이션을 가능하게 했다.
- 2026 NEP89가 고체 물성으로만 학습하고도 Al-Ti 액상 합금의 구조·동역학을 실험과 맞게 재현했다.[4]
- 2026 MACE-Osaka26이 97개 원소로 확장해 minor actinide를 포함한 핵공학 시뮬레이션을 열었다.
- 2026 AQVolt26은 r²SCAN 수준 단일점 계산 322,656개로 고온 왜곡 구조에서 파운데이션 모델이 약해지는 영역을 메웠다.[1]
- 감사: 2026 중성자·X선 회절이 MACE 장거리 모델도 켄칭 후 비정질 유리의 중거리 질서를 복원하지 못함을 보였다.

**대표 도구·시스템** — NEP / NEP89 · Moment Tensor Potentials · MACE-Osaka26 · AQVolt26 · MAD-1.5 · AMDAT · GREX · AdsorbSample · MADField · Hi-MLIP/HINT · AlloyVAE · PI-GP

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [AQVolt26: High-Temperature r²SCAN Halide Dataset for Universal ML Potentials and Solid-State Batteries](../../docs/papers/3023_AQVolt26_High-Temperature_r²SCAN_Halide_Dataset_for_Universa/index.html) — 2026.04 · 인용 1,079
    - 이 논문은 고온 영역에서의 리튬 할라이드 고체전해질 물질의 신뢰성 있는 동역학 모사를 위해 r²SCAN 레벨에서 생성된 322,656개의 단일점 계산으로 구성된 AQVolt26 데이터셋을 제시한다. 기존 파운데이션 ML 모델이 높은 온도의…
2. [General-Purpose Machine-Learned Potential for CrCoNi Alloys Enabling Large-Scale Atomistic Simulations with First-Principles Accuracy](../../docs/papers/372_General-Purpose_Machine-Learned_Potential_for_CrCoNi_Alloys/index.html) — Yong-Chao Wu 외, 2026.03
    - CrCoNi 중엔트로피 합금의 성분 의존적 거동을 정확하게 모사할 수 있는 신경진화 포텐셜(NEP, Neuroevolution Potential) 기반의 머신러닝 상호작용 포텐셜을 개발하였으며, 제1원리 정확도를 유지하면서 대규모 원자시뮬레…
3. [AlloyVAE: A Generative Model for Complex Probabilistic Field-to-Field Relationships in Alloys](../../docs/papers/3018_AlloyVAE_A_Generative_Model_for_Complex_Probabilistic_Field-/index.html) — 2026.04
    - AlloyVAE는 조건부 VAE 기반의 물리정보 생성모델로, 다주성분 합금의 조성장에서 잔류응력장으로의 복잡한 확률적 일대다 관계를 학습하며, 학습형 평활 연산자와 자기일관성 메커니즘으로 물리적 타당성을 보장한다.
4. [Molecular Dynamics Simulations of Al-Ti Metallic Alloy Melts Using a Transferable Machine-Learning Potential](../../docs/papers/3174_Molecular_Dynamics_Simulations_of_Al-Ti_Metallic_Alloy_Melts/index.html) — Yuna Kato 외, 2026.04
    - 고체 물성으로 학습된 전이 가능한 기계학습 퍼텐셜(NEP89)을 사용하여 Al-Ti 액상 합금의 구조 및 동역학 특성을 분자동역학 시뮬레이션으로 조사하고, 실험 데이터와의 일치를 통해 액상 영역에서의 활용 가능성을 입증했다.

> [!tip] 우리에게 무엇인가
> 고온 계에서는 모델 범용성보다 해당 온도·상에서 만든 DFT 데이터와 회절 실험의 대조가 신뢰를 결정한다.

---

## S53 · 양자 다체 시뮬레이션

*제10부 · 계산 재료 시뮬레이션* · **Quantum Many-Body Simulation** · *서브카테고리*

<sub>타임라인 분석 명칭: Quantum Many-Body & Quantum-Device Simulation</sub>

`18편` `2024–2026` `부상` `2025+ 15편`

> [!abstract] 핵심 메시지
> 2026 신경망 양자 상태는 산일·개방계로 확장되고 정밀도·벤치마크가 정비되는 초기 국면이다.

- 2026 Neural Quantum States를 빛-물질 결합계의 산일 동역학에 처음 적용해 약 40개 원자 배열의 super-/sub-radiance를 계산했다.
- 2026 혼합 정밀도 VMC가 샘플링 오차의 이론적 경계를 유도하고 정확도 손실 없이 최대 3.5배 속도 향상을 얻었다.
- 2026 Universal Neural Propagator가 구동 프로토콜을 시간 진화 연산자로 사상해 정확 대각화 한계를 넘는 동역학을 시도했다.[3]
- 2026 Cascade 디코더가 surface code와 BB qLDPC 코드를 한 구조로 다뤘고, GQKAE는 고전 오버헤드를 약 66% 줄였다.
- 배경: 2024 Meta-designing quantum experiments with language models가 언어 모델로 양자 상태 클래스의 메타 해법을 코드로 찾았다.[1]

**대표 도구·시스템** — Neural Quantum States / VMC · PINN-DQME · GQKAE · Cascade decoder · MetaDNS · D-RUT · Universal Neural Propagator · Q-Tag · Gauge-equivariant GNN

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Meta-designing quantum experiments with language models](../../docs/papers/533_Meta-designing_quantum_experiments_with_language_models/index.html) — Sören Arlt 외, 2024 · 인용 3
    - 언어 모델을 활용하여 단일 양자 상태 하나가 아닌 양자 상태의 전체 클래스를 해결하는 메타-솔루션(Python 코드)을 자동 발견함으로써, 인간이 이해 가능한 설계 원칙을 추출하고 임의의 크기로 실험을 확대할 수 있는 새로운 AI 기반 과학…
2. [Scalable Neural Decoders for Practical Fault-Tolerant Quantum Computation](../../docs/papers/10370_Scalable_Neural_Decoders_for_Practical_Fault-Tolerant_Quantu/index.html) — Andi Gu 외, 2026 · 인용 780
    - 양자 오류정정에서 디코딩을 translation-equivariant convolution 기반 신경망 구조로 통일적으로 다뤄, surface code와 고비율 quantum LDPC code(BB code) 모두에 적용 가능한 Cascad…
3. [Universal Neural Propagator: Learning Time Evolution in Many-Body Quantum Systems](../../docs/papers/3272_Universal_Neural_Propagator_Learning_Time_Evolution_in_Many-/index.html) — Zihao Qi 외, 2026.05 · 인용 777
    - 양자 많은-체 시스템에서 구동 프로토콜을 시간 진화 연산자로 매핑하는 범용 신경망 모델(UNP)을 제안하며, 정확 대각화 한계를 넘어 확장 가능한 동역학 시뮬레이션을 실현한다.
4. [MetaDNS: Enhancing Exploration in Discrete Neural Samplers via Metadynamics](../../docs/papers/10028_MetaDNS_Enhancing_Exploration_in_Discrete_Neural_Samplers_vi/index.html) — Xiaochen Du 외, 2026
    - MetaDNS는 well-tempered metadynamics를 discrete neural sampler(diffusion 또는 autoregressive) 학습에 통합하여, mode collapse를 완화하고 에너지 장벽 사이의 고에너…

> [!tip] 우리에게 무엇인가
> 재료 응용과 거리가 있는 기초 단계다. 당장의 투자 대상은 신경망 파동함수 도구 숙련과 벤치마크 참여 정도다.

---

## S54 · 수렴 신호: 경계가 무너지는 곳

*종합* · **Convergence signals** · *종합*

> [!abstract] 핵심 메시지
> 생성 에이전트가 형식 검증기·물리 시뮬레이터·통계 검정과 결합하는 설계로 수렴한다.

- **AI 과학자-검증기 통합** (자율 AI 과학 발견 × 형식 수학 정리 증명 × LLM 추론·에이전트 벤치마크) — Autonomous AI Scientific Discovery, Formal Mathematical Theorem Proving, LLM Reasoning & Agentic Benchmarks 카테고리 전반에서 LLM 기반 가설/코드 생성 에이전트를 Lean4, 물리 시뮬레이터, statistical test 등 외부 검증기와 결합하는 verifier-grounded 아키텍처가 급증하고 있다. DeepScientist, Co-Scientist, Robin, BFS-Prover-V2, PCF 파이프라인 등이 공통적으로 '생성-검증-반복' 루프를 핵심 설계 원칙으로 채택한다.
- **멀티모달-의료 신호 융합** (의료·신경 신호 모델링 × 멀티모달 인식·효율화) — Medical & Neural Signal Modeling과 Multimodal Perception & Efficiency 카테고리에서 EEG/ECG/fMRI 등 생체신호을 언어모델 토큰 공간에 통합하는 foundation model(SleepLM, BrainJanus, OpenTSLM, ViEEG)이 동시다발적으로 등장하여, 신호-텍스트 정렬이 새로운 표준 패러다임으로 자리잡고 있다.

**정책 함의**

- AI4S 연구비 지원시 생성 능력뿐 아니라 검증 인프라(formal verifier, 실험 재현 harness) 구축에 대한 투자를 병행해야 한다.
- 의료 AI 규제기관은 멀티모달 생체신호-언어 통합 모델의 임상 검증 프레임워크를 별도로 마련해야 한다.

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [AI scientists produce results without reasoning scientifically](../../docs/papers/9108_ai_scientists_produce_results_without_reasoning_scienti/index.html) — Martiño Ríos-García 외, 2026 · 인용 342
    - 본 논문은 LLM 기반 scientific agent들이 과학적 추론의 인식론적 규범을 따르지 못한다는 점을 체계적으로 입증한다. 25,000개 이상의 agent 실행을 통해 base model이 성능과 행동의 주요 결정자임을 보였으며, 증…
2. [Accelerating scientific discovery with Co-Scientist](../../docs/papers/3001_Accelerating_scientific_discovery_with_Co-Scientist/index.html) — Juraj Gottweis 외, 2026.05 · 인용 97
    - Google이 개발한 Gemini 기반 multi-agent AI 시스템인 Co-Scientist를 제안하며, test-time compute scaling과 tournament 기반 진화 과정을 통해 과학적 가설을 생성·검증하고, 이를 약…
3. [Scaling up Multi-Turn Off-Policy RL and Multi-Agent Tree Search for LLM Step-Provers](../../docs/papers/10379_Scaling_up_Multi-Turn_Off-Policy_RL_and_Multi-Agent_Tree_Sea/index.html) — Ran Xin 외, 2026
    - BFS-Prover-V2는 LLM 기반 Lean 4 정리 증명기에서 학습 시점과 추론 시점의 스케일링을 동시에 다루는 시스템으로, multi-turn off-policy RL(expert iteration 기반)과 planner 기반 mul…
4. [Propose, Critique, Falsify: Benchmarking Self-Verifying AI Scientists](../../docs/papers/10259_Propose_Critique_Falsify_Benchmarking_Self-Verifying_AI_Scie/index.html) — Aayam Bansal 외, 2026
    - 이 논문은 여러 LLM 에이전트가 과학적 주장을 제안-비판-반증(Propose-Critique-Falsify, PCF)하는 다중 에이전트 검증 파이프라인이 실제로 허위 발견율(false discovery rate, FDR)을 줄이는지 벤치마…
5. [SleepLM: Natural-Language Intelligence for Human Sleep](../../docs/papers/10454_SleepLM_Natural-Language_Intelligence_for_Human_Sleep/index.html) — Zongzhe Xu 외, 2026
    - SleepLM은 다중모달 polysomnography(PSG) 신호와 자연어를 정렬하여 수면 상태를 개방형으로 설명·질의·해석할 수 있게 하는 최초의 sleep-language foundation model 계열이며, 이를 위해 100K시간…

> [!tip] 우리에게 무엇인가
> 분야 간 경계가 아니라 생성-검증 루프라는 공통 설계가 연구를 묶는다. 한 분야의 검증기 투자는 다른 분야로 이전된다.

---

## S55 · 부상과 쇠퇴

*종합* · **What is rising, what is fading** · *종합*

> [!abstract] 핵심 메시지
> anytime-valid 검정이 부상하고, 복잡한 모델이 단순 베이스라인에 지는 사례가 쌓이며 낡은 가정이 쇠퇴한다.

- **부상 —**
- **Anytime-valid 통계검정 확산** (인과·통계 추론) — Causal & Statistical Inference 카테고리에서 e-process/martingale 기반 anytime-valid hypothesis testing(9249, 9250, 9402, 9544, 10359)이 LLM 평가, SAE feature 검증, diffusion sampling 등 다양한 응용에 빠르게 확산되고 있어, 고전적 고정 표본 검정을 대체하는 새로운 표준으로 부상하고 있다.
- **쇠퇴 —**
- **순수 지도학습 베이스라인 열세** (자율 AI 과학 발견 × 생체분자 생성 모델링 × 인과·통계 추론) — 여러 영역(유전자 perturbation 예측 10900/10714, 분자 foundation model 10566, domain adaptation 3079)에서 복잡한 딥러닝 모델이 단순 선형/gradient boosting baseline을 능가하지 못한다는 negative result가 반복되며, 복잡성 대비 실질적 이득에 대한 회의론이 확산되고 있다.

**정책 함의**

- 통계 방법론 교육 과정에 sequential/anytime-valid inference를 포함시켜 AI 평가 신뢰성을 제고해야 한다.
- 신규 모델 발표 시 단순 baseline과의 엄격한 비교를 필수 요건으로 요구하는 심사 기준을 강화해야 한다.

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Anytime-Valid Hypothesis Testing for Sparse Autoencoder Feature Validation](../../docs/papers/9250_Anytime-Valid_Hypothesis_Testing_for_Sparse_Autoencoder_Feat/index.html) — Rudransh Khera, 2026 · 인용 675
    - Sparse autoencoder(SAE) feature를 인과적 필요성(causal necessity) 기준으로 검증하기 위해, paired ablation intervention에서 e-process를 구성하고 e-BH procedure…
2. [Evaluating out of distribution generalization of protein language models](../../docs/papers/9606_Evaluating_out_of_distribution_generalization_of_protein_lan/index.html) — Kumaresh Krishnan 외, 2026 · 인용 5
    - 단백질 언어모델(pLM) 사전학습 데이터와 다운스트림 평가 데이터 간의 서열 유사성(leakage)이 실제 일반화 성능 측정을 왜곡할 수 있음을 대규모의 homology-free split을 이용한 통제 실험으로 정량적으로 입증한 연구이다.
3. [Anytime-Valid Confirmation of Label-Shift Corrections](../../docs/papers/9249_Anytime-Valid_Confirmation_of_Label-Shift_Corrections/index.html) — Seungjin Choi, 2026
    - 사전에 도메인 지식으로 지정된 label-shift 보정(weight w(y))이 실제로 관측되는 target labeled 데이터와 부합하는지를, e-value/martingale 이론을 이용해 anytime-valid하게 확인(confi…
4. [CITE: Anytime-Valid Statistical Inference in LLM Self-Consistency](../../docs/papers/9402_CITE_Anytime-Valid_Statistical_Inference_in_LLM_Self-Consist/index.html) — Hirofumi Ota 외, 2026
    - LLM의 self-consistency에서 특정 정답 후보 r이 응답 분포의 유일한 mode임을 인증하는 문제를 anytime-valid sequential testing으로 정식화하고, 미리 알 수 없는 무한 카테고리 집합 하에서도 임의의…
5. [DP-SPRT: Differentially Private Sequential Probability Ratio Tests](../../docs/papers/9544_DP-SPRT_Differentially_Private_Sequential_Probability_Ratio/index.html) — Thomas Michel 외, 2026
    - Wald의 SPRT를 differential privacy 제약 하에서 재설계하여, 원하는 오류 확률과 privacy 수준을 동시에 보장하는 DP-SPRT를 제안하고, 이를 위해 OutsideInterval이라는 새로운 private mec…

> [!tip] 우리에게 무엇인가
> 신규 모델은 단순 베이스라인과의 엄격한 비교 없이는 인정받기 어려워진다. 통계 방법론 교육에 순차 추론을 넣는 것이 AI 평가 신뢰성의 선결 조건이다.

---

## S56 · 비어 있는 자리

*종합* · **Gaps and underserved domains** · *종합*

> [!abstract] 핵심 메시지
> 생성은 풍부한데 검증, 귀속, 장기 재현성, 자율 실험실 거버넌스는 비어 있다.

- **검증 없는 생성 모델 남용** (생체분자 생성 모델링 × 계산 재료 시뮬레이션 × 인과·통계 추론) — Biomolecular Generative Modeling과 Computational Materials Simulation에서 수백 편의 diffusion/flow-matching 생성 모델이 쏟아지지만, Rietveld refinement 오류(1070), self-consistency 44% reject(10334), deep learning이 단순 baseline을 못 이기는 사례(10900, 3079, 10714) 등 '생성은 쉽지만 검증은 어렵다'는 구조적 문제가 반복적으로 보고된다.
- **AI 저자성·귀속 공백** (과학 문헌·동료심사 × 자율 AI 과학 발견) — LLM이 가설 생성부터 논문 작성까지 수행하는 사례(10909, 11016, 9124)가 늘면서 AI 기여도를 어떻게 credit하고 표절을 판별할지에 대한 연구(9459, 9460, 10767)가 등장하지만, 여전히 합의된 기준이 없고 Idea plagiarism 논쟁(10767)이 지속되고 있다.
- **AI 리더보드 신뢰성 위기** (LLM 추론·에이전트 벤치마크 × 인과·통계 추론) — LLM Reasoning & Agentic Benchmarks 전반에서 벤치마크 reward-hacking(10951), leaderboard 불확실성(10572, 10284), evaluation protocol artifact(10593), hidden-prompt 사용(11015) 등 평가 자체의 타당성에 의문을 제기하는 논문이 급증하여 '벤치마크의 벤치마크'가 필요한 상황이다.
- **미개척 영역** — AI 생성 과학적 주장의 장기적 재현성 추적
- **미개척 영역** — 자율 실험실의 안전·보안 거버넌스
- **미개척 영역** — 비영어권/저자원 언어 과학 문헌의 AI 접근성
- **미개척 영역** — AI 과학자 시스템의 publication bias 증폭 문제

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Credit Where Credit Is Due: A Taxonomy of AI Contributions to Scientific Discovery and Recommendations for Authorship Policy](../../docs/papers/9459_Credit_Where_Credit_Is_Due_A_Taxonomy_of_AI_Contributions_to/index.html) — Luiz Felipe Caparelli Piochi, 2026 · 인용 678
    - 이 논문은 AI가 과학적 발견에 기여하는 정도를 tool, assistant, collaborator, autonomous discoverer의 4단계로 구분하는 taxonomy를 제안하고, 각 단계에 상응하는 credit framework…
2. [CreditMap: Provenance Ledgers for Attribution in Human--AI Scientific Collaboration](../../docs/papers/9460_CreditMap_Provenance_Ledgers_for_Attribution_in_Human--AI_Sc/index.html) — Aayam Bansal 외, 2026 · 인용 401
    - CreditMap은 인간-AI 협업 연구에서 기여도를 세밀하게 기록하기 위해 W3C PROV ontology를 9가지 AI 특화 contribution role로 확장하고, append-only hash chaining 기반의 JSON-LD…
3. [Data integrity in materials science in the era of AI: balancing accelerated discovery with responsible science and innovation](../../docs/papers/252_Data_integrity_in_materials_science_in_the_era_of_AI_balanci/index.html) — Nik Reeves-McLaren 외, 2026 · 인용 11
    - AI의 급속한 발전으로 재료 과학의 데이터 무결성이 심각한 위협에 직면해 있으며, 전문가조차 AI 생성 현미경 이미지를 실제 데이터와 구별하지 못하고 있다. 이 논문은 책임감 있는 과학 실천을 위한 다층적 연구 무결성 프레임워크를 제안한다.
4. [Quantifying Ranking Uncertainty in LLM Benchmarks](../../docs/papers/10284_Quantifying_Ranking_Uncertainty_in_LLM_Benchmarks/index.html) — Bitya Neuhof 외, 2026 · 인용 2
    - MMLU와 같은 multi-task 벤치마크에서 LLM 순위의 불확실성을 정량화하기 위해, pairwise hypothesis test를 기반으로 한 rank confidence interval(rank CI) 방법을 적용하고, subjec…
5. [Scientists decry conference’s use of hidden prompts to snare AI peer reviews](../../docs/papers/11015_Scientists_decry_conferences_use_of_hidden_prompts_to_snare/index.html) — Dalmeet Singh Chawla, 2026 · 인용 1
    - NeurIPS와 ICML 등 주요 AI 학회가 논문에 숨겨진 LLM 프롬프트를 삽입해 동료평가 과정에서 AI를 부적절하게 사용하는 리뷰어를 적발하려 시도했으나, 이 방식이 연구자 신뢰를 훼손한다는 반발이 일고 있다는 보도이다.

> [!tip] 우리에게 무엇인가
> 빈칸은 곧 기회다. AI 저자성 기준, 자율 실험실 안전, 저자원 언어 접근성은 국내 기관이 표준 제정 과정에 일찍 들어갈 수 있는 영역이다.

---

## S57 · 검증 전환의 여섯 축

*종합* · **Six Axes of the Shift to Verification** · *종합*

> [!abstract] 핵심 메시지
> 2026년의 공통 주제는 생성이 아니라 검증이다. 여섯 축에서 같은 방향의 증거가 나온다.

- **검증기 결합** — BFS-Prover-V2, Robin: 형식 증명기와 습식 실험을 생성 루프의 보상·판정으로 삼는다 (S17·S13)
- **벤치마크 감사** — Ground False, QEDBench: 데이터셋 충실도와 LLM 채점자의 점수 부풀림을 정량화한다 (S18·S20)
- **순위 통계화** — The Leaderboard Lottery: 점추정 1위는 사후 선택 문제이며 신뢰구간이 필요하다 (S48)
- **장기·적대 평가** — YC-Bench, ToRR: 1년 규모 운영과 표 형식 변화에서 에이전트와 모델의 취약성을 드러낸다 (S22·S24)
- **합성·독립 재현** — MatterGen, Polybot: 생성 결과를 합성 가능성과 자율 실험으로 닫는다 (S51·S14)
- **기권과 위험 통제** — Salus, DeepBlip: 증거 부족을 인정하고 위험 상한을 보증하는 평가로 옮겨간다 (S23·S47)

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Robin: A multi-agent system for automating scientific discovery](../../docs/papers/10726_robin_a_multi-agent_system_for_automating_scientific_d/index.html) — Ali E. Ghareeb 외, 2026.05 · 인용 50
    - Robin은 문헌검색 에이전트(Crow, Falcon)와 데이터분석 에이전트(Finch)를 결합해 가설생성-실험제안-데이터해석-가설갱신의 과학적 발견 전 과정을 자동화하는 멀티에이전트 시스템이며, 이를 통해 dAMD 치료 후보물질인 ripa…
2. [Ground False: Dissecting Errors in Formal Mathematics Benchmarks](../../docs/papers/9759_Ground_False_Dissecting_Errors_in_Formal_Mathematics_Benchma/index.html) — One An 외, 2026 · 인용 159
    - 공식 수학 벤치마크(formal mathematics benchmark)의 ground truth(GT)가 사실상 무검증 상태로 신뢰되어 왔음을 지적하고, ProofNet 전체 367개 항목을 수작업 감사한 결과 56%가 unfaithful…
3. [QEDBench: Quantifying the Alignment Gap in Automated Evaluation of University-Level Mathematical Proofs](../../docs/papers/10280_QEDBench_Quantifying_the_Alignment_Gap_in_Automated_Evaluati/index.html) — Santiago Gonzalez 외, 2026
    - 이 논문은 LLM을 자동 채점자(judge)로 사용할 때 대학 수준 수학 증명 평가에서 발생하는 체계적인 정렬 격차(Alignment Gap)를 정량화하는 벤치마크인 QEDBench를 제안한다. 7개의 judge 모델과 5개의 solver…
4. [The Leaderboard Lottery: Why Top LLM Rankings Are Often Coin Flips, and How to Fix Them](../../docs/papers/10572_The_Leaderboard_Lottery_Why_Top_LLM_Rankings_Are_Often_Coin/index.html) — Shourya Vir Jain, 2026
    - LLM 리더보드에서 point-estimate 기반 1위 선정은 N개 모델에 대한 post-selection inference 문제임을 지적하고, marginal confidence interval이 "top-ranked 모델이 진짜 최고인…
5. [YC-Bench: Benchmarking AI Agents for Long-Term Planning and Consistent Execution](../../docs/papers/3398_YC-Bench_Benchmarking_AI_Agents_for_Long-Term_Planning_and_C/index.html) — Muyu He 외, 2026 · 인용 1,873
    - YC-Bench는 LLM 에이전트의 장기 계획과 일관된 실행 능력을 평가하기 위한 벤치마크로, 1년 동안 수백 턴을 거쳐 시뮬레이션된 스타트업을 운영하도록 하는 POMDP 기반 환경을 제공한다. 불충실한 클라이언트와 증가하는 급여 비용 등…
6. [The mighty torr: A benchmark for table reasoning and robustness](../../docs/papers/802_The_mighty_torr_A_benchmark_for_table_reasoning_and_robustne/index.html) — Shir Ashury-Tahan 외, 2025
    - 본 논문은 ToRR(Table Reasoning and Robustness) 벤치마크를 제시하여, 대규모 언어모델(LLM)의 표 데이터 이해 능력과 다양한 표 형식에 대한 견고성(robustness)을 체계적으로 평가한다. 10개의 데이터셋…

> [!tip] 우리에게 무엇인가
> 검증 역량은 개별 논문이 아니라 조직의 자산이다. 검증기, 베이스라인 세트, 독립 재현 체계를 먼저 구축한 기관이 생성 경쟁에서도 신뢰를 얻는다.

---

## S58 · 그래서 무엇을 할 것인가

*종합* · **Where to stand** · *마무리*

> [!abstract] 핵심 메시지
> 국내 연구기관·기업은 생성 경쟁에서 한 발 물러나 검증 인프라를 먼저 세워야 한다.

- **검증기 우선 투자** — 형식 검증기·재현 하네스·습식 검증 파트너십을 에이전트 도입보다 앞세운다 (S17·S13)
- **내부 감사 벤치마크 구축** — 외부 리더보드가 아니라 자체 데이터로 베이스라인과 불충실 사례를 가려내는 평가셋을 만든다 (S18·S06)
- **순위 대신 신뢰구간** — 모델 선정·조달 보고서에 순위 신뢰구간과 다중 비교 보정을 의무화한다 (S48)
- **DFT·섭동 실험 데이터 자산화** — 범용 모델은 공개돼 있으므로 우리 계의 학습 데이터와 독립 재분석이 해자다 (S50·S51)
- **AI 귀속·거버넌스 선점** — AI 기여도 공개 표준과 자율 실험실 안전 지침 논의에 일찍 참여한다 (S11·S38)

**관전 포인트 (다음 12개월)**

- 형식 검증기를 결합한 AI 과학자가 증명 외 영역(물리·화학)에서 독립 재현을 통과하는가
- LLM 채점자의 아첨과 형식화 불충실을 줄이는 감사 표준이 자리잡는가
- 리더보드가 신뢰구간 보고를 의무화하는 방향으로 바뀌는가
- 자율 실험실의 안전·귀속 기준이 학술지·연구비 기관의 정책으로 명문화되는가

> [!tip] 우리에게 무엇인가
> 도구는 이미 공개돼 있다. 국내 기관의 차별점은 생성 능력이 아니라 반증 능력, 즉 데이터와 검증 체계다.

---

## 부록 · 전체 레퍼런스 217편

- [(Sparse) Attention to the Details: Preserving Spectral Fidelity in ML-based Weather Forecasting Models](../../docs/papers/10472_Sparse_Attention_to_the_Details_Preserving_Spectral_Fidelity/index.html) — Maksim Zhdanov 외, 2026
- [A Fairness Audit of Medical Imaging Foundation Models on a Multimodal Structured Clinical Benchmark](../../docs/papers/9147_A_Fairness_Audit_of_Medical_Imaging_Foundation_Models_on_a_M/index.html) — Milan Mohan 외, 2026
- [A New Paradigm for Computational Chemistry](../../docs/papers/2995_A_New_Paradigm_for_Computational_Chemistry/index.html) — Raphael T. Husistein 외, 2026.04 · 인용 1
- [A collaborative constrained graph diffusion model for the generation of realistic synthetic molecules](../../docs/papers/2984_A_collaborative_constrained_graph_diffusion_model_for_the_ge/index.html) — Manuel Ruiz-Botella 외, 2026.05 · 인용 3
- [A flexible and affordable self-driving laboratory for automated reaction optimization](../../docs/papers/2989_A_flexible_and_affordable_self-driving_laboratory_for_automa/index.html) — Simone Pilon 외, 2026.04 · 인용 13
- [A survey of large language models](../../docs/papers/026_A_survey_of_large_language_models/index.html) — Wayne Xin Zhao 외, 2026.12 · 인용 114
- [AI scientists produce results without reasoning scientifically](../../docs/papers/9108_ai_scientists_produce_results_without_reasoning_scienti/index.html) — Martiño Ríos-García 외, 2026 · 인용 342
- [AI-Assisted Peer Review at Scale: The AAAI-26 AI Review Pilot](../../docs/papers/10928_AI-Assisted_Peer_Review_at_Scale_The_AAAI-26_AI_Review_Pilot/index.html) — Joydeep Biswas 외, 2026.04 · 인용 1
- [AMR-Bench-mini: A Diagnostic Benchmark for Agentic Mechanistic AMR Reasoning under Evidence Insufficiency](../../docs/papers/9239_AMR-Bench-mini_A_Diagnostic_Benchmark_for_Agentic_Mechanisti/index.html) — Ali Ihsan Nergiz 외, 2026 · 인용 2,475
- [AQVolt26: High-Temperature r²SCAN Halide Dataset for Universal ML Potentials and Solid-State Batteries](../../docs/papers/3023_AQVolt26_High-Temperature_r²SCAN_Halide_Dataset_for_Universa/index.html) — 2026.04 · 인용 1,079
- [Accelerating Scientific Research with Gemini in the Real-World](../../docs/papers/10911_accelerating_scientific_research_with_gemini_in_the_re/index.html) — Samuel Schmidgall 외, 2026.08
- [Accelerating scientific discovery with Co-Scientist](../../docs/papers/3001_Accelerating_scientific_discovery_with_Co-Scientist/index.html) — Juraj Gottweis 외, 2026.05 · 인용 97
- [AgentPLM: Agentic Protein Language Models with Reasoning-Augmented Decoding for Protein Sequence Design](../../docs/papers/9214_AgentPLM_Agentic_Protein_Language_Models_with_Reasoning-Augm/index.html) — Sahil Rahman 외, 2026 · 인용 1,186
- [Alignment between Brains and AI: Evidence for Convergent Evolution across Modalities, Scales and Training Trajectories](../../docs/papers/9231_Alignment_between_Brains_and_AI_Evidence_for_Convergent_Evol/index.html) — Guobin Shen 외, 2026
- [AlloyVAE: A Generative Model for Complex Probabilistic Field-to-Field Relationships in Alloys](../../docs/papers/3018_AlloyVAE_A_Generative_Model_for_Complex_Probabilistic_Field-/index.html) — 2026.04
- [Anytime-Valid Confirmation of Label-Shift Corrections](../../docs/papers/9249_Anytime-Valid_Confirmation_of_Label-Shift_Corrections/index.html) — Seungjin Choi, 2026
- [Anytime-Valid Hypothesis Testing for Sparse Autoencoder Feature Validation](../../docs/papers/9250_Anytime-Valid_Hypothesis_Testing_for_Sparse_Autoencoder_Feat/index.html) — Rudransh Khera, 2026 · 인용 675
- [Author Correction: An autonomous laboratory for the accelerated synthesis of inorganic materials](../../docs/papers/10931_Author_Correction_An_autonomous_laboratory_for_the_accelerat/index.html) — Nathan J. Szymanski 외, 2026.02 · 인용 5
- [Autonomous biomedical research with an artificial intelligence agent](../../docs/papers/10933_Autonomous_biomedical_research_with_an_artificial_intelligen/index.html) — Kexin Huang 외, 2026.07 · 인용 14
- [Autoregressive EHR Foundation Models with Multimodal Inputs](../../docs/papers/9284_Autoregressive_EHR_Foundation_Models_with_Multimodal_Inputs/index.html) — Yuxuan Liu 외, 2026 · 인용 60
- [Benchmarking self-driving labs](../../docs/papers/10935_Benchmarking_self-driving_labs/index.html) — Adedire D. Adesiji 외, 2026 · 인용 11
- [Bridging Gene Regulatory Networks and Causal Representation Learning in Single-Cell Genomics Data](../../docs/papers/9358_Bridging_Gene_Regulatory_Networks_and_Causal_Representation/index.html) — Vincenzo Lagani 외, 2026 · 인용 3,730
- [BrokenMath: A Benchmark for Sycophancy in Theorem Proving with LLMs](../../docs/papers/9359_BrokenMath_A_Benchmark_for_Sycophancy_in_Theorem_Proving_wit/index.html) — Ivo Petrov 외, 2026
- [CIDER: Conformal Information-Directed Agents for Low-Budget Protein Engineering](../../docs/papers/9400_CIDER_Conformal_Information-Directed_Agents_for_Low-Budget_P/index.html) — Rishabh Bhattacharya, 2026 · 인용 6,121
- [CINOC: Cardinality-Invariant Neural Operator Policies for Scalable PDE Control](../../docs/papers/9401_CINOC_Cardinality-Invariant_Neural_Operator_Policies_for_Sca/index.html) — Pietro Zanotta 외, 2026
- [CITE: Anytime-Valid Statistical Inference in LLM Self-Consistency](../../docs/papers/9402_CITE_Anytime-Valid_Statistical_Inference_in_LLM_Self-Consist/index.html) — Hirofumi Ota 외, 2026
- [Can Vision Language Models Learn Intuitive Physics from Interaction?](../../docs/papers/9373_Can_Vision_Language_Models_Learn_Intuitive_Physics_from_Inte/index.html) — Luca M. Schulze Buschoff 외, 2026
- [Celcomen: spatial causal disentanglement for single-cell and tissue perturbation modeling](../../docs/papers/3051_Celcomen_spatial_causal_disentanglement_for_single-cell_and/index.html) — Stathis Megas 외, 2026.03 · 인용 8
- [Cocoa: Co-planning and co-execution with AI Agents](../../docs/papers/229_Cocoa_Co-planning_and_co-execution_with_ai_agents/index.html) — K. J. Kevin Feng 외, 2026 · 인용 6
- [Credit Where Credit Is Due: A Taxonomy of AI Contributions to Scientific Discovery and Recommendations for Authorship Policy](../../docs/papers/9459_Credit_Where_Credit_Is_Due_A_Taxonomy_of_AI_Contributions_to/index.html) — Luiz Felipe Caparelli Piochi, 2026 · 인용 678
- [CreditMap: Provenance Ledgers for Attribution in Human--AI Scientific Collaboration](../../docs/papers/9460_CreditMap_Provenance_Ledgers_for_Attribution_in_Human--AI_Sc/index.html) — Aayam Bansal 외, 2026 · 인용 401
- [CupOFLATTE: Coupled Objective-Guided Discrete Flows via Linker Assembly for Targeted PROTAC Engineering](../../docs/papers/9468_CupOFLATTE_Coupled_Objective-Guided_Discrete_Flows_via_Linke/index.html) — Ziang Li 외, 2026 · 인용 157
- [DNACHUNKER: Learnable Tokenization for DNA Language Models](../../docs/papers/9536_DNACHUNKER_Learnable_Tokenization_for_DNA_Language_Models/index.html) — Taewon Kim 외, 2026 · 인용 11
- [DP-SPRT: Differentially Private Sequential Probability Ratio Tests](../../docs/papers/9544_DP-SPRT_Differentially_Private_Sequential_Probability_Ratio/index.html) — Thomas Michel 외, 2026
- [Data integrity in materials science in the era of AI: balancing accelerated discovery with responsible science and innovation](../../docs/papers/252_Data_integrity_in_materials_science_in_the_era_of_AI_balanci/index.html) — Nik Reeves-McLaren 외, 2026 · 인용 11
- [Data-driven construction of machine-learning-based interatomic potentials for gas-surface scattering dynamics: the case of NO on graphite](../../docs/papers/3066_Data-driven_construction_of_machine-learning-based_interatom/index.html) — 2026.03 · 인용 9
- [Deadline-Valid Replay: Anytime-Valid Testing for LLM Inference Policies](../../docs/papers/9482_Deadline-Valid_Replay_Anytime-Valid_Testing_for_LLM_Inferenc/index.html) — Rui Gao, 2026 · 인용 74
- [DeepBlip: Estimating Conditional Average Treatment Effects Over Time](../../docs/papers/9495_DeepBlip_Estimating_Conditional_Average_Treatment_Effects_Ov/index.html) — Haorui Ma 외, 2026
- [DiffSyn: a generative diffusion approach to materials synthesis planning](../../docs/papers/3077_DiffSyn_a_generative_diffusion_approach_to_materials_synthes/index.html) — Elton Pan 외, 2026.02 · 인용 6
- [Discrete Survival Knowledge Distillation for Competing Risks Analysis](../../docs/papers/9522_Discrete_Survival_Knowledge_Distillation_for_Competing_Risks/index.html) — Feiyang Deng 외, 2026
- [Do Androids Dream of Breaking the Game? Systematically Auditing AI Agent Benchmarks with BenchJack](../../docs/papers/10951_Do_Androids_Dream_of_Breaking_the_Game_Systematically_Auditi/index.html) — Hao Wang 외, 2026.05
- [EMFormer: Efficient Multi-Scale Transformer for Accumulative Context Weather Forecasting](../../docs/papers/9580_EMFormer_Efficient_Multi-Scale_Transformer_for_Accumulative/index.html) — Hao Chen 외, 2026
- [Evaluating out of distribution generalization of protein language models](../../docs/papers/9606_Evaluating_out_of_distribution_generalization_of_protein_lan/index.html) — Kumaresh Krishnan 외, 2026 · 인용 5
- [FHIR-Hopper: A Neuro-Symbolic Agent for Reasoning over EHRs](../../docs/papers/9645_FHIR-Hopper_A_Neuro-Symbolic_Agent_for_Reasoning_over_EHRs/index.html) — Chanwoo Kim 외, 2026 · 인용 104
- [FIRSTPASS: A Multi-Domain, Multi-Round Peer Review Dataset Grounded in Real Editorial Outcomes](../../docs/papers/9652_FIRSTPASS_A_Multi-Domain_Multi-Round_Peer_Review_Dataset_Gro/index.html) — Prabhjot Singh 외, 2026
- [FUSE: FK-Steered Multi-Modal Flow Matching for Efficient Simulation-Based Posterior Estimation](../../docs/papers/9710_FUSE_FK-Steered_Multi-Modal_Flow_Matching_for_Efficient_Simu/index.html) — Weichen Qin 외, 2026 · 인용 994
- [FormalRx: Rectify and eXamine Semantic Failures in Autoformalization](../../docs/papers/9675_FormalRx_Rectify_and_eXamine_Semantic_Failures_in_Autoformal/index.html) — Haocheng Wang 외, 2026
- [From Kepler to Newton: Inductive Biases Guide Learned World Models in Transformers](../../docs/papers/9696_From_Kepler_to_Newton_Inductive_Biases_Guide_Learned_World_M/index.html) — Ziming Liu 외, 2026 · 인용 12
- [From LLM-Generated Conjectures to Lean Formalizations: Automated Polynomial Inequality Proving via Sum-of-Squares Certificates](../../docs/papers/9697_From_LLM-Generated_Conjectures_to_Lean_Formalizations_Automa/index.html) — Ruobing Zuo 외, 2026
- [FunCQNet: A Functional Censored Quantile Neural Network for Predicting Long-Term Post-Transplant Kidney Survival](../../docs/papers/9706_FunCQNet_A_Functional_Censored_Quantile_Neural_Network_for_P/index.html) — Jiaqi Men 외, 2026
- [GRAIL: Gradient-Reweighted Advantages for Reinforcement Learning with Verifiable Rewards](../../docs/papers/9755_GRAIL_Gradient-Reweighted_Advantages_for_Reinforcement_Learn/index.html) — Tej Deep Pala 외, 2026 · 인용 56
- [GenDA: Generative Data Assimilation on Complex Urban Areas via Classifier-Free Diffusion Guidance](../../docs/papers/9717_GenDA_Generative_Data_Assimilation_on_Complex_Urban_Areas_vi/index.html) — Francisco Giral 외, 2026
- [General-Purpose Machine-Learned Potential for CrCoNi Alloys Enabling Large-Scale Atomistic Simulations with First-Principles Accuracy](../../docs/papers/372_General-Purpose_Machine-Learned_Potential_for_CrCoNi_Alloys/index.html) — Yong-Chao Wu 외, 2026.03
- [Generative Chemical Language Models for Energetic Materials Discovery](../../docs/papers/3114_Generative_Chemical_Language_Models_for_Energetic_Materials/index.html) — 2026.03
- [Generative Pipeline for Discovering Solid-State Battery Materials with Universal Atomistic Potentials](../../docs/papers/9727_Generative_Pipeline_for_Discovering_Solid-State_Battery_Mate/index.html) — Artem Dembitskiy 외, 2026 · 인용 139
- [Generative design of inorganic materials](../../docs/papers/3115_Generative_design_of_inorganic_materials/index.html) — 2026.04 · 인용 10
- [Ground False: Dissecting Errors in Formal Mathematics Benchmarks](../../docs/papers/9759_Ground_False_Dissecting_Errors_in_Formal_Mathematics_Benchma/index.html) — One An 외, 2026 · 인용 159
- [Human-AI Hybrid Mathematical Discovery Workflow: Unifying Ramanujan's 17 Series for 1/π](../../docs/papers/9796_Human-AI_Hybrid_Mathematical_Discovery_Workflow_Unifying_Ram/index.html) — Michael Shalyt 외, 2026 · 인용 46
- [IRIS: An Agentic Multi-Phase Framework for Automated Scientific Literature Review](../../docs/papers/9847_IRIS_An_Agentic_Multi-Phase_Framework_for_Automated_Scientif/index.html) — Sergey Kolchenko 외, 2026 · 인용 48
- [IVQA-LD: Inclusive Multimodal Understanding for Population with Limb Deficiency](../../docs/papers/9853_IVQA-LD_Inclusive_Multimodal_Understanding_for_Population_wi/index.html) — Yan Ke 외, 2026
- [InnoEval: On Research Idea Evaluation as a Knowledge-Grounded, Multi-Perspective Reasoning Problem](../../docs/papers/9833_InnoEval_On_Research_Idea_Evaluation_as_a_Knowledge-Grounded/index.html) — Shuofei Qiao 외, 2026
- [Just Add Structure: Protein Language Models Combined with Structural Equivariance Excel at Protein Tasks](../../docs/papers/9859_Just_Add_Structure_Protein_Language_Models_Combined_with_Str/index.html) — Qurat ul ain 외, 2026 · 인용 16,139
- [Knockoff-C2ST: False Discovery Controlled Attribution of Distribution Shift](../../docs/papers/9863_Knockoff-C2ST_False_Discovery_Controlled_Attribution_of_Dist/index.html) — Şuayp Talha Kocabay 외, 2026 · 인용 113
- [LDARNet: DNA Adaptive Representation Network with Learnable Tokenization for Genomic Modeling](../../docs/papers/9884_LDARNet_DNA_Adaptive_Representation_Network_with_Learnable_T/index.html) — Daria Ledneva 외, 2026 · 인용 104
- [LabProc and Tacit: Quantifying the Visual-Textual Prior Gap in Autonomous Laboratory Perception](../../docs/papers/9870_LabProc_and_Tacit_Quantifying_the_Visual-Textual_Prior_Gap_i/index.html) — Jagrati Gogia 외, 2026
- [Learning Clinical-Trial Strategy: Offline Policy Training for Decision Agents](../../docs/papers/9900_Learning_Clinical-Trial_Strategy_Offline_Policy_Training_for/index.html) — William James Bolton 외, 2026
- [LieStoNet: Learning Lie Symmetries from Spatiotemporal Data for Stochastic Dynamical Systems](../../docs/papers/9943_LieStoNet_Learning_Lie_Symmetries_from_Spatiotemporal_Data_f/index.html) — Shida Liu 외, 2026
- [LitReview Arena: Evaluating Literature Review Agents with Battle-style Peer Review Platform](../../docs/papers/9953_LitReview_Arena_Evaluating_Literature_Review_Agents_with_Bat/index.html) — Ruotong Zhao 외, 2026 · 인용 210
- [LoPhyDA: Low-Rank Tensor and Physics Gradient Guided Diffusion for Atmospheric Data Assimilation](../../docs/papers/9971_LoPhyDA_Low-Rank_Tensor_and_Physics_Gradient_Guided_Diffusio/index.html) — Danyang Peng 외, 2026
- [Local Intrinsic Dimension of Representations Predicts Alignment and Generalization in AI Models and Human Brain](../../docs/papers/9964_Local_Intrinsic_Dimension_of_Representations_Predicts_Alignm/index.html) — Junjie Yu 외, 2026
- [MEDA: Medical-Oriented Activation Editing for Hallucination Mitigation in Medical Large Vision-Language Model](../../docs/papers/10006_MEDA_Medical-Oriented_Activation_Editing_for_Hallucination_M/index.html) — Tianbo Wang 외, 2026
- [MEG-XL: Data-Efficient Brain-to-Text via Long-Context Pre-Training](../../docs/papers/10019_MEG-XL_Data-Efficient_Brain-to-Text_via_Long-Context_Pre-Tra/index.html) — Dulhan Jayalath 외, 2026
- [MENO: MeanFlow-Enhanced Neural Operators for Dynamical Systems](../../docs/papers/3165_MENO_MeanFlow-Enhanced_Neural_Operators_for_Dynamical_System/index.html) — 2026.04 · 인용 1,051
- [MMClima: A Framework for Multimodal Climate Science Data and Evaluation](../../docs/papers/10042_MMClima_A_Framework_for_Multimodal_Climate_Science_Data_and/index.html) — Muhammad Umer Sheikh 외, 2026
- [Med-Scout: Curing MLLMs' Geometric Blindness in Medical Perception via Geometry-Aware RL Post-Training](../../docs/papers/10004_Med-Scout_Curing_MLLMs_Geometric_Blindness_in_Medical_Percep/index.html) — Anglin Liu 외, 2026
- [Med-SegLens: Latent-Level Model Diffing for Interpretable Medical Image Segmentation](../../docs/papers/10005_Med-SegLens_Latent-Level_Model_Diffing_for_Interpretable_Med/index.html) — Salma J. Ahmed 외, 2026 · 인용 872
- [MedCRP-CL: Continual Medical Image Segmentation via Bayesian Nonparametric Semantic Modality Discovery](../../docs/papers/10009_MedCRP-CL_Continual_Medical_Image_Segmentation_via_Bayesian/index.html) — Ziyuan Gao, 2026
- [MedMIX: Modality-Internal Expert Fusion for Multimodal Medical Diagnosis](../../docs/papers/10014_MedMIX_Modality-Internal_Expert_Fusion_for_Multimodal_Medica/index.html) — Seungik Cho 외, 2026 · 인용 1,331
- [MedMamba: Multi-View State Space Models with Adaptive Graph Learning for Medical Time Series Classification](../../docs/papers/10012_MedMamba_Multi-View_State_Space_Models_with_Adaptive_Graph_L/index.html) — Da Zhang 외, 2026
- [MedREK: Retrieval-Based Editing for Medical LLMs with Key-Aware Prompts](../../docs/papers/10016_MedREK_Retrieval-Based_Editing_for_Medical_LLMs_with_Key-Awa/index.html) — Shujun Xia 외, 2026
- [MerLean: An Agentic Framework for Autoformalization in Quantum Computation](../../docs/papers/532_MerLean_An_Agentic_Framework_for_Autoformalization_in_Quantu/index.html) — Yuanjie Ren 외, 2026.02 · 인용 9
- [MetaDNS: Enhancing Exploration in Discrete Neural Samplers via Metadynamics](../../docs/papers/10028_MetaDNS_Enhancing_Exploration_in_Discrete_Neural_Samplers_vi/index.html) — Xiaochen Du 외, 2026
- [Minimax-Optimal Kernel Two-sample Testing in Sub-quadratic Time](../../docs/papers/10034_Minimax-Optimal_Kernel_Two-sample_Testing_in_Sub-quadratic_T/index.html) — Ikjun Choi 외, 2026
- [Missingness-Aware Conformal Prediction Under Cross-Hospital Distribution Shift](../../docs/papers/10036_Missingness-Aware_Conformal_Prediction_Under_Cross-Hospital/index.html) — Liang You 외, 2026
- [Mitigating Gradient Pathology in PINNs through Aligned Constraint](../../docs/papers/10037_Mitigating_Gradient_Pathology_in_PINNs_through_Aligned_Const/index.html) — Yichen Luo 외, 2026
- [Model Collapse Despite Ground-Truth Verification](../../docs/papers/10048_Model_Collapse_Despite_Ground-Truth_Verification/index.html) — Shuo Li Liu, 2026
- [Molecular Dynamics Simulations of Al-Ti Metallic Alloy Melts Using a Transferable Machine-Learning Potential](../../docs/papers/3174_Molecular_Dynamics_Simulations_of_Al-Ti_Metallic_Alloy_Melts/index.html) — Yuna Kato 외, 2026.04
- [Multi-Scale Flow Matching for Continuous-time Generative Modeling of Spatiotemporal Tissue Dynamics from Spatial Transcriptomics](../../docs/papers/10069_Multi-Scale_Flow_Matching_for_Continuous-time_Generative_Mod/index.html) — Pinar Demetci 외, 2026 · 인용 1,884
- [Multi-View Causal Discovery without Non-Gaussianity: Identifiability and Algorithms](../../docs/papers/10071_Multi-View_Causal_Discovery_without_Non-Gaussianity_Identifi/index.html) — Ambroise Heurtebise 외, 2026
- [Multimarginal flow matching with optimal transport potentials](../../docs/papers/10073_Multimarginal_flow_matching_with_optimal_transport_potential/index.html) — Raghav Kansal 외, 2026
- [NeurOCNN: A Neural-Operator-Based Model for Physiological Time Series](../../docs/papers/10103_NeurOCNN_A_Neural-Operator-Based_Model_for_Physiological_Tim/index.html) — Daya Kumar 외, 2026
- [Neural Modular Physics for Elastic Simulation](../../docs/papers/10093_Neural_Modular_Physics_for_Elastic_Simulation/index.html) — Yifei Li 외, 2026 · 인용 560
- [OpenDiscoveryTrace: Process Traces for Evaluating AI Scientist Workflows](../../docs/papers/10134_OpenDiscoveryTrace_Process_Traces_for_Evaluating_AI_Scientis/index.html) — Aayam Bansal 외, 2026 · 인용 2,072
- [OptProver: Bridging Olympiad and Optimization through Continual Training in Formal Theorem Proving](../../docs/papers/10144_OptProver_Bridging_Olympiad_and_Optimization_through_Continu/index.html) — Chenyi Li 외, 2026
- [Order Matters in Retrosynthesis: Structure-aware Generation via Reaction-Center-Guided Discrete Flow Matching](../../docs/papers/3196_Order_Matters_in_Retrosynthesis_Structure-aware_Generation_v/index.html) — 2026.02
- [PRIMA: a bidirectional state-space architecture and training approach for sequence modelling of protein-protein interactions](../../docs/papers/10235_PRIMA_a_bidirectional_state-space_architecture_and_training/index.html) — Arturo Fiorellini-Bernardis 외, 2026 · 인용 599
- [PaperBanana: Automating Academic Illustration for AI Scientists](../../docs/papers/601_PaperBanana_Automating_Academic_Illustration_for_AI_Scientis/index.html) — Dawei Zhu 외, 2026.01 · 인용 1
- [Particle-Guided Diffusion Models for Partial Differential Equations](../../docs/papers/10158_Particle-Guided_Diffusion_Models_for_Partial_Differential_Eq/index.html) — Andrew Millard 외, 2026
- [PerturbDiff: Functional Diffusion for Single-Cell Perturbation Modeling](../../docs/papers/10174_PerturbDiff_Functional_Diffusion_for_Single-Cell_Perturbatio/index.html) — Xinyu Yuan 외, 2026
- [Pessimistic Verification for Open-Ended Math Questions](../../docs/papers/10175_Pessimistic_Verification_for_Open-Ended_Math_Questions/index.html) — Yanxing Huang 외, 2026
- [Plug-and-Play Diffusion Meets ADMM: Dual-Variable Coupling for Robust Medical Image Reconstruction](../../docs/papers/10205_Plug-and-Play_Diffusion_Meets_ADMM_Dual-Variable_Coupling_fo/index.html) — Chenhe Du 외, 2026
- [Prediction-Powered Inference Across Many Tasks for AI Evaluation](../../docs/papers/10231_Prediction-Powered_Inference_Across_Many_Tasks_for_AI_Evalua/index.html) — Nicolas Emmenegger 외, 2026
- [Principled Confidence Estimation for Deep Computed Tomography](../../docs/papers/10239_Principled_Confidence_Estimation_for_Deep_Computed_Tomograph/index.html) — Matteo Gätzner 외, 2026
- [Process Reward Agents for Steering Knowledge-Intensive Reasoning](../../docs/papers/10251_Process_Reward_Agents_for_Steering_Knowledge-Intensive_Reaso/index.html) — Jiwoong Sohn 외, 2026 · 인용 11
- [ProofGate: A Reproducible Audit of Faithfulness, Alignment, and Vacuity in State-of-the-Art Lean Theorem Provers](../../docs/papers/10257_ProofGate_A_Reproducible_Audit_of_Faithfulness_Alignment_and/index.html) — Edison Yang 외, 2026
- [Propose, Critique, Falsify: Benchmarking Self-Verifying AI Scientists](../../docs/papers/10259_Propose_Critique_Falsify_Benchmarking_Self-Verifying_AI_Scie/index.html) — Aayam Bansal 외, 2026
- [Protein Language Models Diverge from Natural Language: Comparative Analysis and Improved Inference](../../docs/papers/3221_Protein_Language_Models_Diverge_from_Natural_Language_Compar/index.html) — 2026.02 · 인용 3,225
- [ProteomeLM: A Proteome-Scale Language Model Enables Accurate and Rapid Prediction of Protein-Protein Interactions and Gene Essentiality Across Taxa](../../docs/papers/10267_ProteomeLM_A_Proteome-Scale_Language_Model_Enables_Accurate/index.html) — Cyril Malbranke 외, 2026 · 인용 763
- [QEDBench: Quantifying the Alignment Gap in Automated Evaluation of University-Level Mathematical Proofs](../../docs/papers/10280_QEDBench_Quantifying_the_Alignment_Gap_in_Automated_Evaluati/index.html) — Santiago Gonzalez 외, 2026
- [Quantifying Ranking Uncertainty in LLM Benchmarks](../../docs/papers/10284_Quantifying_Ranking_Uncertainty_in_LLM_Benchmarks/index.html) — Bitya Neuhof 외, 2026 · 인용 2
- [QuantumQUBO Agent: Automating Quadratic Unconstrained Binary Optimization (QUBO) Formulation Generation from Natural Language](../../docs/papers/10289_QuantumQUBO_Agent_Automating_Quadratic_Unconstrained_Binary/index.html) — Niloy Kumar Mondal 외, 2026 · 인용 8,635
- [RETROSPECT: RETROsynthesis via Sequential Prediction, and Chemically Transformed-ranking](../../docs/papers/10340_RETROSPECT_RETROsynthesis_via_Sequential_Prediction_and_Chem/index.html) — Raja Sekhar Pappala 외, 2026 · 인용 241
- [Reinforcement Learning for Tool-Calling Agents in Fast Healthcare Interoperability Resources (FHIR)](../../docs/papers/10319_Reinforcement_Learning_for_Tool-Calling_Agents_in_Fast_Healt/index.html) — Marius Knorr 외, 2026 · 인용 420
- [Reliable and Efficient Automated Transition-State Searches with Machine-Learned Interatomic Potentials](../../docs/papers/3229_Reliable_and_Efficient_Automated_Transition-State_Searches_w/index.html) — 2026.04 · 인용 2
- [Representative vs. Load-bearing Layers: A Dissociation in Genomic Foundation Models](../../docs/papers/10324_Representative_vs_Load-bearing_Layers_A_Dissociation_in_Geno/index.html) — Yoonjin Cho 외, 2026 · 인용 146
- [Representative, Informative, and De-Amplifying: Requirements for Robust Bayesian Active Learning under Model Misspecification](../../docs/papers/1100_Representative_Informative_and_De-Amplifying_Requirements_fo/index.html) — Roubing Tang 외, 2026.03
- [Resolution Diagnostics for Paired LLM Evaluation](../../docs/papers/10326_Resolution_Diagnostics_for_Paired_LLM_Evaluation/index.html) — Anany Kotawala, 2026
- [Rethinking Diffusion Models with Symmetries through Canonicalization with Applications to Molecular Graph Generation](../../docs/papers/10330_Rethinking_Diffusion_Models_with_Symmetries_through_Canonica/index.html) — Cai Zhou 외, 2026
- [Rethinking Federated Prompt Learning for Medical Images: From Textual Tuning to Visual Manifold Anchoring](../../docs/papers/10331_Rethinking_Federated_Prompt_Learning_for_Medical_Images_From/index.html) — Yipan Wei 외, 2026
- [Rethinking Small VLM Quantization: From Component-Wise Analysis to Hardware-Aware Edge Deployment](../../docs/papers/10335_Rethinking_Small_VLM_Quantization_From_Component-Wise_Analys/index.html) — Hyeju Shin 외, 2026
- [RetrOrchestrator: A Multi-Step Retrosynthesis Agent Dynamically Orchestrating Single-Step Transition Models](../../docs/papers/10339_RetrOrchestrator_A_Multi-Step_Retrosynthesis_Agent_Dynamical/index.html) — Liao Chang 외, 2026
- [ReviewArena: A Large-Scale Cross-Conference Dataset and Benchmark for LLM Peer Review](../../docs/papers/10341_ReviewArena_A_Large-Scale_Cross-Conference_Dataset_and_Bench/index.html) — Samarth P 외, 2026
- [Robin: A multi-agent system for automating scientific discovery](../../docs/papers/10726_robin_a_multi-agent_system_for_automating_scientific_d/index.html) — Ali E. Ghareeb 외, 2026.05 · 인용 50
- [S1-MMAlign: A Large-Scale, Multi-Disciplinary Dataset for Scientific Figure-Text Understanding](../../docs/papers/691_S1-MMAlign_A_Large-Scale_Multi-Disciplinary_Dataset_for_Scie/index.html) — He Wang 외, 2026.01
- [S2M-Net: Spectral-Spatial Mixing with Morphology-Aware Adaptive Loss for Medical Image Segmentation](../../docs/papers/10356_S2M-Net_Spectral-Spatial_Mixing_with_Morphology-Aware_Adapti/index.html) — Sanaullah Chowdhury 외, 2026
- [SAEs-BrainMap: Unveiling the Emergence of Specialized Concepts in Deep Models via Brain Alignment](../../docs/papers/10358_SAEs-BrainMap_Unveiling_the_Emergence_of_Specialized_Concept/index.html) — Ziming Mao 외, 2026
- [SE(3)-Equivariant Flow Matching with Gaussian Process Priors for Geometric Trajectory Prediction](../../docs/papers/10398_SE3-Equivariant_Flow_Matching_with_Gaussian_Process_Priors_f/index.html) — Xuyang Wang 외, 2026
- [SENDAI: A Hierarchical Sparse-measurement, EfficieNt Data AssImilation Framework](../../docs/papers/10422_SENDAI_A_Hierarchical_Sparse-measurement_EfficieNt_Data_AssI/index.html) — Xingyue Zhang 외, 2026
- [SIGMA-PPG: Statistical-prior Informed Generative Masking Architecture for PPG Foundation Model](../../docs/papers/10440_SIGMA-PPG_Statistical-prior_Informed__Generative_Masking_Arc/index.html) — Zongheng Guo 외, 2026
- [STFlow: Data-Coupled Flow Matching for Geometric Trajectory Simulation](../../docs/papers/10501_STFlow_Data-Coupled_Flow_Matching_for_Geometric_Trajectory_S/index.html) — Kiet Bennema ten Brinke 외, 2026 · 인용 12
- [Safety Generalization Under Distribution Shift in Safe Reinforcement Learning: A Diabetes Testbed](../../docs/papers/10362_Safety_Generalization_Under_Distribution_Shift_in_Safe_Reinf/index.html) — Minjae Kwon 외, 2026
- [Scalable Neural Decoders for Practical Fault-Tolerant Quantum Computation](../../docs/papers/10370_Scalable_Neural_Decoders_for_Practical_Fault-Tolerant_Quantu/index.html) — Andi Gu 외, 2026 · 인용 780
- [Scaling Laws and Architectural Frontiers in Metagenomic Foundation Models](../../docs/papers/10375_Scaling_Laws_and_Architectural_Frontiers_in_Metagenomic_Foun/index.html) — Geraldene Munsamy 외, 2026 · 인용 519
- [Scaling Laws of Global Weather Models](../../docs/papers/10376_Scaling_Laws_of_Global_Weather_Models/index.html) — Yuejiang Yu 외, 2026
- [Scaling up Multi-Turn Off-Policy RL and Multi-Agent Tree Search for LLM Step-Provers](../../docs/papers/10379_Scaling_up_Multi-Turn_Off-Policy_RL_and_Multi-Agent_Tree_Sea/index.html) — Ran Xin 외, 2026
- [SciNet: Evaluating AI Agents in Relation-Aware Scientific Literature Retrieval](../../docs/papers/10391_SciNet_Evaluating_AI_Agents_in_Relation-Aware_Scientific_Lit/index.html) — Chenyang Shao 외, 2026 · 인용 3,133
- [SciPaths: Forecasting Pathways to Scientific Discovery](../../docs/papers/10392_SciPaths_Forecasting_Pathways_to_Scientific_Discovery/index.html) — Eric Chamoun 외, 2026
- [SciVideoBench: Benchmarking Scientific Video Reasoning in Large Multimodal Models](../../docs/papers/10395_SciVideoBench_Benchmarking_Scientific_Video_Reasoning_in_Lar/index.html) — Andong Deng 외, 2026
- [Scientists decry conference’s use of hidden prompts to snare AI peer reviews](../../docs/papers/11015_Scientists_decry_conferences_use_of_hidden_prompts_to_snare/index.html) — Dalmeet Singh Chawla, 2026 · 인용 1
- [ScoreStop: Gradient-based early stopping using functional score tests](../../docs/papers/10397_ScoreStop_Gradient-based_early_stopping_using_functional_sco/index.html) — Oliver J. Hines 외, 2026
- [Seizure-Semiology-Suite(S^3): A Clinically Multimodal Dataset, Benchmark, and Models for Seizure Semiology Understanding](../../docs/papers/10406_Seizure-Semiology-SuiteS3_A_Clinically_Multimodal_Dataset_Be/index.html) — Lina Zhang 외, 2026
- [Self-Distillation Zero: Self-Revision Turns Binary Rewards into Dense Supervision](../../docs/papers/10409_Self-Distillation_Zero_Self-Revision_Turns_Binary_Rewards_in/index.html) — Yinghui He 외, 2026
- [Self-Improving Language Models with Bidirectional Evolutionary Search](../../docs/papers/10410_Self-Improving_Language_Models_with_Bidirectional_Evolutiona/index.html) — Guowei Xu 외, 2026
- [Semi-Autonomous Formalization of the Vlasov–Maxwell–Landau Equilibrium](../../docs/papers/10415_Semi-Autonomous_Formalization_of_the_VlasovMaxwellLandau_Equ/index.html) — Vasily Ilin, 2026 · 인용 3,164
- [Semi-knockoffs: a model-agnostic conditional independence testing method with finite-sample guarantees](../../docs/papers/10416_Semi-knockoffs_a_model-agnostic_conditional_independence_tes/index.html) — Angel David REYERO LOBO 외, 2026
- [SkillX: Automatically Constructing Skill Knowledge Bases for Agents](../../docs/papers/10451_SkillX_Automatically_Constructing_Skill_Knowledge_Bases_for/index.html) — Chenxi Wang 외, 2026 · 인용 124
- [SleepLM: Natural-Language Intelligence for Human Sleep](../../docs/papers/10454_SleepLM_Natural-Language_Intelligence_for_Human_Sleep/index.html) — Zongzhe Xu 외, 2026
- [Smooth Dynamic Cutoffs for Machine Learning Interatomic Potentials](../../docs/papers/10459_Smooth_Dynamic_Cutoffs_for_Machine_Learning_Interatomic_Pote/index.html) — Kevin Han 외, 2026
- [Smooth Multi-Policy Causal Effect Estimation in Longitudinal Settings](../../docs/papers/10460_Smooth_Multi-Policy_Causal_Effect_Estimation_in_Longitudinal/index.html) — Wenxin Chen 외, 2026
- [SoMA: A Real-to-Sim Neural Simulator for Robotic Soft-Body Manipulation](../../docs/papers/10467_SoMA_A_Real-to-Sim_Neural_Simulator_for_Robotic_Soft-Body_Ma/index.html) — Mu Huang 외, 2026
- [Solving Stiff Dark Matter Equations via Jacobian Normalization with Physics-Informed Neural Networks](../../docs/papers/3242_Solving_Stiff_Dark_Matter_Equations_via_Jacobian_Normalizati/index.html) — 2026.02 · 인용 458
- [SparseEHR: Scalable Foundation Modeling for Structured EHR via Conditional Computation](../../docs/papers/10473_SparseEHR_Scalable_Foundation_Modeling_for_Structured_EHR_vi/index.html) — Meysam Ghaffari 외, 2026
- [SurvDiff: A Diffusion Model for Generating Synthetic Data in Survival Analysis](../../docs/papers/10520_SurvDiff_A_Diffusion_Model_for_Generating_Synthetic_Data_in/index.html) — Marie Brockschmidt 외, 2026
- [SynLaD: Latent Diffusion for Generating Synthesizable Molecules Conditioned on 3D Pharmacophore Profiles](../../docs/papers/10527_SynLaD_Latent_Diffusion_for_Generating_Synthesizable_Molecul/index.html) — Miruna Cretu 외, 2026
- [TRIAGE: An AI Scientist for Adversarial Target Falsification](../../docs/papers/10638_TRIAGE_An_AI_Scientist_for_Adversarial_Target_Falsification/index.html) — Jiawei Xing, 2026 · 인용 119
- [TadA-Bench: A Million-Variant Benchmark for Future-Round Discovery Toward Agentic Protein Engineering](../../docs/papers/10537_TadA-Bench_A_Million-Variant_Benchmark_for_Future-Round_Disc/index.html) — Jin Gao 외, 2026 · 인용 7
- [The Leaderboard Lottery: Why Top LLM Rankings Are Often Coin Flips, and How to Fix Them](../../docs/papers/10572_The_Leaderboard_Lottery_Why_Top_LLM_Rankings_Are_Often_Coin/index.html) — Shourya Vir Jain, 2026
- [The Signal-Coverage Matrix: Stratifying Type and Semantic Errors in Statement Autoformalization](../../docs/papers/10578_The_Signal-Coverage_Matrix_Stratifying_Type_and_Semantic_Err/index.html) — Chengxiao Dai 외, 2026
- [TimeSpot: Benchmarking Geo-Temporal Understanding in Vision–Language Models in Real-World Settings](../../docs/papers/10589_TimeSpot_Benchmarking_Geo-Temporal_Understanding_in_VisionLa/index.html) — Azmine Toushik Wasi 외, 2026
- [Token-Only Adaptation of Frozen Self-Supervised Vision Foundation Models for Cross-Species Animal Pose: A Pareto-Frontier Characterization Across Eight Held-Out Mammal Species](../../docs/papers/10594_Token-Only_Adaptation_of_Frozen_Self-Supervised_Vision_Found/index.html) — Ethan Y Wang 외, 2026 · 인용 979
- [Towards Self-Evolving Agentic Literature Retrieval](../../docs/papers/10617_Towards_Self-Evolving_Agentic_Literature_Retrieval/index.html) — Yuwen Du 외, 2026 · 인용 1,798
- [U-Cast: A Surprisingly Simple and Efficient Frontier Probabilistic AI Weather Forecaster](../../docs/papers/10652_U-Cast_A_Surprisingly_Simple_and_Efficient_Frontier_Probabil/index.html) — Salva Rühling Cachay 외, 2026
- [Universal Neural Propagator: Learning Time Evolution in Many-Body Quantum Systems](../../docs/papers/3272_Universal_Neural_Propagator_Learning_Time_Evolution_in_Many-/index.html) — Zihao Qi 외, 2026.05 · 인용 777
- [UrbanFusion: Stochastic Multimodal Fusion for Contrastive Learning of Robust Spatial Representations](../../docs/papers/10667_UrbanFusion_Stochastic_Multimodal_Fusion_for_Contrastive_Lea/index.html) — Dominik J. Mühlematter 외, 2026
- [VERITAS: Verifier-Guided Proof Search for Zero-Shot Formal Theorem Proving](../../docs/papers/10678_VERITAS_Verifier-Guided_Proof_Search_for_Zero-Shot_Formal_Th/index.html) — Manish Acharya 외, 2026
- [VT-Bench: A Unified Benchmark for Visual-Tabular Multi-Modal Learning](../../docs/papers/10685_VT-Bench_A_Unified_Benchmark_for_Visual-Tabular_Multi-Modal/index.html) — Ziyi Jia 외, 2026
- [VeriBench: An End-to-End Formal Verification Benchmark for AI Coding Agents in Lean 4](../../docs/papers/10676_VeriBench_An_End-to-End_Formal_Verification_Benchmark_for_AI/index.html) — Brando Miranda 외, 2026
- [Weak Critics Make Strong Learners: On-Policy Critique Distillation for Scalable Oversight](../../docs/papers/10690_Weak_Critics_Make_Strong_Learners_On-Policy_Critique_Distill/index.html) — Can Jin 외, 2026
- [YC-Bench: Benchmarking AI Agents for Long-Term Planning and Consistent Execution](../../docs/papers/3398_YC-Bench_Benchmarking_AI_Agents_for_Long-Term_Planning_and_C/index.html) — Muyu He 외, 2026 · 인용 1,873
- [miniF2F-Dafny: LLM-Guided Mathematical Theorem Proving via Auto-Active Verification](../../docs/papers/10033_miniF2F-Dafny_LLM-Guided_Mathematical_Theorem_Proving_via_Au/index.html) — Mantas Baksys 외, 2026 · 인용 4
- [AI Scientists Fail Without Strong Implementation Capability](../../docs/papers/081_Ai_scientists_fail_without_strong_implementation_capability/index.html) — Min Zhu 외, 2025 · 인용 2,819
- [Ai idea bench 2025: Ai research idea generation benchmark](../../docs/papers/10924_Ai_idea_bench_2025_Ai_research_idea_generation_benchmark/index.html) — DeepSeek-AI 외, 2025
- [Autonomous Agents for Scientific Discovery: Orchestrating Scientists, Language, Code, and Physics](../../docs/papers/137_Autonomous_Agents_for_Scientific_Discovery_Orchestrating_Sci/index.html) — Lianhao Zhou 외, 2025.10 · 인용 12,647
- [ChartSketcher: Reasoning with multimodal feedback and reflection for chart understanding](../../docs/papers/203_Chartsketcher_Reasoning_with_multimodal_feedback_and_reflect/index.html) — Muye Huang 외, 2025
- [Chartist: Task-driven Eye Movement Control for Chart Reading](../../docs/papers/200_Chartist_Task-driven_Eye_Movement_Control_for_Chart_Reading/index.html) — Danqing Shi 외, 2025 · 인용 13
- [Confidence in Large Language Model Evaluation: A Bayesian Approach to Limited-Sample Challenges](../../docs/papers/237_Confidence_in_Large_Language_Model_Evaluation_A_Bayesian_App/index.html) — Xiao Xiao 외, 2025
- [Critique-GRPO: Advancing LLM Reasoning with Natural Language and Numerical Feedback](../../docs/papers/243_Critique-GRPO_Advancing_LLM_Reasoning_with_Natural_Language/index.html) — Xiaoying Zhang 외, 2025
- [DeepAnalyze: Agentic Large Language Models for Autonomous Data Science](../../docs/papers/259_DeepAnalyze_Agentic_Large_Language_Models_for_Autonomous_Dat/index.html) — Shaolei Zhang 외, 2025.10
- [DeepScientist: Advancing Frontier-Pushing Scientific Findings Progressively](../../docs/papers/10727_deepscientist_advancing_frontier-pushing_scientific_fi/index.html) — Yixuan Weng 외, 2025.09 · 인용 73
- [DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning](../../docs/papers/265_DeepSeek-R1_incentivizes_reasoning_in_LLMs_through_reinforce/index.html) — DeepSeek-AI 외, 2025 · 인용 1,046
- [Discovery of Unstable Singularities](../../docs/papers/276_Discovery_of_Unstable_Singularities/index.html) — Yongji Wang 외, 2025.09 · 인용 17
- [Enhancing chemical reaction and retrosynthesis prediction with large language model and dual-task learning](../../docs/papers/316_Enhancing_chemical_reaction_and_retrosynthesis_prediction_wi/index.html) — Xuan Lin 외, 2025 · 인용 3
- [Estimating optimal context length for hybrid retrieval-augmented multi-document summarization](../../docs/papers/318_Estimating_optimal_context_length_for_hybrid_retrievalaugmen/index.html) — Adithya Pratapa 외, 2025
- [Explainable biomedical claim verification with large language models](../../docs/papers/328_Explainable_biomedical_claim_verification_with_large_languag/index.html) — Siting Liang 외, 2025 · 인용 54
- [From AI for Science to Agentic Science: A Survey on Autonomous Scientific Discovery](../../docs/papers/352_From_AI_for_Science_to_Agentic_Science_A_Survey_on_Autonomou/index.html) — Jiaqi Wei 외, 2025.10 · 인용 5
- [GeoFactory: an LLM performance enhancement framework for geoscience factual and inferential tasks](../../docs/papers/10764_geofactory_an_llm_performance_enhancement_framework_fo/index.html) — Zhou Chen 외, 2025.05 · 인용 6
- [GraphEval: A lightweight graph-based llm framework for idea evaluation](../../docs/papers/392_Grapheval_A_lightweight_graph-based_llm_framework_for_idea_e/index.html) — Tao Feng 외, 2025
- [Kosmos: An AI Scientist for Autonomous Discovery](../../docs/papers/9098_kosmos_an_ai_scientist_for_autonomous_discovery/index.html) — Ludovico Mitchener 외, 2025 · 인용 131
- [LLM × MapReduce-V2: Entropy-Driven Convolutional Test-Time Scaling for Generating Long-Form Articles from Extremely Long Resources](../../docs/papers/495_Llm__mapreduce-v2_Entropy-driven_convolutional_test-time_sca/index.html) — Haoyu Wang 외, 2025
- [LLM-based Corroborating and Refuting Evidence Retrieval for Scientific Claim Verification](../../docs/papers/500_Llm-based_corroborating_and_refuting_evidence_retrieval_for/index.html) — Siyuan Wang 외, 2025
- [MedAgentGym: A Scalable Agentic Training Environment for Code-Centric Reasoning in Biomedical Data Science](../../docs/papers/528_MedAgentGym_A_Scalable_Agentic_Training_Environment_for_Code/index.html) — Ran Xu 외, 2025.06
- [Mind the blind spots: A focus-level evaluation framework for llm reviews](../../docs/papers/537_Mind_the_blind_spots_A_focus-level_evaluation_framework_for/index.html) — Hyungyu Shin 외, 2025 · 인용 3
- [MoDeST: A dataset for Multi Domain Scientific Title Generation](../../docs/papers/10765_modest_a_dataset_for_multi_domain_scientific_title_gen/index.html) — Necva Bölücü 외, 2025.05 · 인용 1
- [Multimodal deepresearcher: Generating text-chart interleaved reports from scratch with agentic framework](../../docs/papers/566_Multimodal_deepresearcher_Generating_text-chart_interleaved/index.html) — Zhaorui Yang 외, 2025 · 인용 3
- [Paper2poster: Towards multimodal poster automation from scientific papers](../../docs/papers/599_Paper2poster_Towards_multimodal_poster_automation_from_scien/index.html) — Wei Pang 외, 2025 · 인용 2
- [PharmAgents: Building a Virtual Pharma with Large Language Model Agents](../../docs/papers/616_PharmAgents_Building_a_Virtual_Pharma_with_Large_Language_Mo/index.html) — Bowen Gao 외, 2025 · 인용 2
- [Predicting field experiments with large language models](../../docs/papers/631_Predicting_field_experiments_with_large_language_models/index.html) — Yaoyu Chen 외, 2025
- [R&D-Agent: Automating Data-Driven AI Solution Building Through LLM-Powered Automated Research, Development, and Evolution](../../docs/papers/650_RD-Agent_Automating_Data-Driven_AI_Solution_Building_Through/index.html) — Xu Yang 외, 2025.05 · 인용 1
- [ReSearch: Learning to Reason with Search for LLMs via Reinforcement Learning](../../docs/papers/667_ReSearch_Learning_to_Reason_with_Search_for_LLMs_via_Reinfor/index.html) — Mingyang Chen 외, 2025 · 인용 10
- [ResearchAgent: Iterative Research Idea Generation over Scientific Literature with Large Language Models](../../docs/papers/668_ResearchAgent_Iterative_Research_Idea_Generation_over_Scient/index.html) — Jinheon Baek 외, 2025.02 · 인용 34
- [ReviewEval: An evaluation framework for AI-generated reviews](../../docs/papers/679_Revieweval_An_evaluation_framework_for_ai-generated_reviews/index.html) — Madhav Krishan Garg 외, 2025 · 인용 2
- [SFT Memorizes, RL Generalizes: A Comparative Study of Foundation Model Post-training](../../docs/papers/751_SFT_Memorizes_RL_Generalizes_A_Comparative_Study_of_Foundati/index.html) — Tianzhe Chu 외, 2025 · 인용 6
- [SafeScientist: Toward Risk-Aware Scientific Discoveries by LLM Agents](../../docs/papers/692_Safescientist_Toward_risk-aware_scientific_discoveries_by_ll/index.html) — Kunlun Zhu 외, 2025 · 인용 1
- [SciClaims: An end-to-end generative system for biomedical claim analysis](../../docs/papers/711_Sciclaims_An_end-to-end_generative_system_for_biomedical_cla/index.html) — Raúl Ortega 외, 2025
- [Sciclaimhunt: A large dataset for evidence-based scientific claim verification](../../docs/papers/710_Sciclaimhunt_A_large_dataset_for_evidence-based_scientific_c/index.html) — Sujit Kumar 외, 2025 · 인용 35
- [Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement Learning](../../docs/papers/740_Search-R1_Training_LLMs_to_Reason_and_Leverage_Search_Engine/index.html) — Bowen Jin 외, 2025 · 인용 12
- [Select, read, and write: A multi-agent framework of full-text-based related work generation](../../docs/papers/742_Select_read_and_write_A_multi-agent_framework_of_full-text-b/index.html) — Xiaochuan Liu 외, 2025
- [Sparks: Multi-Agent Artificial Intelligence Model Discovers Protein Design Principles](../../docs/papers/764_Sparks_Multi-Agent_Artificial_Intelligence_Model_Discovers_P/index.html) — Alireza Ghafarollahi 외, 2025 · 인용 9
- [SurveyX: Academic survey automation via large language models](../../docs/papers/781_Surveyx_Academic_survey_automation_via_large_language_models/index.html) — Xun Liang 외, 2025 · 인용 2,819
- [The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search](../../docs/papers/794_The_AI_Scientist-v2_Workshop-Level_Automated_Scientific_Disc/index.html) — Yutaro Yamada 외, 2025.04 · 인용 476
- [The mighty torr: A benchmark for table reasoning and robustness](../../docs/papers/802_The_mighty_torr_A_benchmark_for_table_reasoning_and_robustne/index.html) — Shir Ashury-Tahan 외, 2025
- [TreeReview: A dynamic tree of questions framework for deep and efficient llm-based scientific peer review](../../docs/papers/843_Treereview_A_dynamic_tree_of_questions_framework_for_deep_an/index.html) — Yuan Chang 외, 2025 · 인용 2
- [TxAgent: An AI Agent for Therapeutic Reasoning Across a Universe of Tools](../../docs/papers/848_TxAgent_An_AI_Agent_for_Therapeutic_Reasoning_Across_a_Unive/index.html) — Shanghua Gao 외, 2025.03
- [Using artificial intelligence for systematic review: the example of elicit](../../docs/papers/862_Using_artificial_intelligence_for_systematic_review_the_exam/index.html) — Nathan Bernard 외, 2025.03 · 인용 83
- [Value iteration for learning concurrently executable robotic control tasks](../../docs/papers/863_Value_iteration_for_learning_concurrently_executable_robotic/index.html) — Sheikh A. Tahmid 외, 2025 · 인용 244
- [Visual thoughts: A unified perspective of understanding multimodal chain-of-thought](../../docs/papers/869_Visual_thoughts_A_unified_perspective_of_understanding_multi/index.html) — Zihui Cheng 외, 2025
- [Meta-designing quantum experiments with language models](../../docs/papers/533_Meta-designing_quantum_experiments_with_language_models/index.html) — Sören Arlt 외, 2024 · 인용 3

*생성: `pipeline/build_slide_deck.py --topic ai4s` · 2026-10-21 · 근거 코퍼스 2,709편 (`docs/ai4s`)*
