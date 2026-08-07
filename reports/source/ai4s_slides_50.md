---
title: "AI for Science 지형도 — 발표 슬라이드 원고 50장"
topic: ai4s
slides: 50
corpus_papers: 2658
evidence_since: 2025
generated: 2026-08-06
tags:
  - ai4science
  - 슬라이드
  - 연구동향
  - ai4s
---

# AI for Science 지형도 — 슬라이드 원고 50장

> [!info] 개요
> 코퍼스 **2,658편** · 대분류 **8개** · 서브카테고리 **82개** 중 편수 상위 **5개씩**.
> 슬라이드 1장 = 서브카테고리 1개(`S06`–`S45`). 사례는 **2025년 이후 우선**(코퍼스의 83%).
> 레퍼런스 링크는 각 논문의 리뷰 문서(`../../docs/papers/<slug>/index.html`)로 연결된다.

## 목차

- **오프닝**
    - `S01` AI for Science, 2026년 지형도
    - `S02` 이 지도는 어떻게 만들어졌나
    - `S03` 코퍼스 한눈에 보기
    - `S04` 8개 대분류 지형도
    - `S05` 관통하는 한 줄: 예측 → 설계 → 자율 → 검증
- **제1부 · AI 기반 신약·신소재 발견**
    - `S06` 약물–유전자 서명 분석 — 141편
    - `S07` 단백질 결합부위 예측 — 96편
    - `S08` 조절서열·유전자 발현 예측 — 68편
    - `S09` 생물학 위상·표현 해석 — 49편
    - `S10` 과학 멀티모달 벤치마킹 — 44편
- **제2부 · LLM·에이전트 평가**
    - `S11` 웹 증강 RL 추론 에이전트 — 62편
    - `S12` 프런티어 모델·멀티모달 안전성 평가 — 57편
    - `S13` 오픈소스 코드 LLM·명령어 튜닝 — 43편
    - `S14` 자기개선·주석 공정성·통계 타당성 — 42편
    - `S15` 불확실성 인지 생성·대리모델 — 41편
- **제3부 · 물리·환경 과학 AI**
    - `S16` 신경 연산자·물리정보 PDE 해석 — 102편
    - `S17` 잠재변수 생성 솔버 — 93편
    - `S18` 과학 파운데이션 모델과 통계 엄밀성 — 88편
    - `S19` AI 수치예보·기후 모델 — 31편
    - `S20` 물리 제어 RL 견고성·real-to-sim — 14편
- **제4부 · 분자 시뮬레이션·생성 모델링**
    - `S21` 확산모델 보상 미세조정 — 66편
    - `S22` 등변 힘장·기계학습 원자간 퍼텐셜 — 59편
    - `S23` 결정구조 생성 모델링 — 47편
    - `S24` 대리 서술자 검증·반증 — 31편
    - `S25` 분자 물성·분광 검증 — 30편
- **제5부 · 과학 자동화 에이전트 AI**
    - `S26` 도구 사용 과학 에이전트 — 91편
    - `S27` 자율 과학 발견 에이전트 — 37편
    - `S28` 임상 LLM 응용 — 31편
    - `S29` 장비·시설 자동화 에이전트 — 27편
    - `S30` 다중 에이전트 사회 시뮬레이션 — 21편
- **제6부 · 형식 방법론·계산 추론**
    - `S31` 고차논리 형식 정리증명 — 157편
    - `S32` 이론 한계·AI 조력 증명 — 33편
    - `S33` 대칭성 인지 솔버·방정식 발견 — 24편
    - `S34` LLM 지원 구조·물리 설계 최적화 — 14편
    - `S35` LLM 주도 CFD·멀티피직스 자동화 — 7편
- **제7부 · 과학 정보추출·질의응답**
    - `S36` 다국어 사후학습·백본 적응 — 47편
    - `S37` 과학 도표·시각문서 이해 — 45편
    - `S38` 자동 주장 검증 — 33편
    - `S39` 생의학·임상 지식접지 QA — 23편
    - `S40` RAG와 모호성 해소 — 20편
- **제8부 · AI 지원 학술 커뮤니케이션**
    - `S41` 학술 메타데이터·연구 무결성 데이터 — 37편
    - `S42` LLM 지원 동료심사 — 34편
    - `S43` 과학 가설 재조합 — 19편
    - `S44` 그래프 기반 과학 요약 — 15편
    - `S45` 인용 문맥 추천·검증 — 12편
- **종합**
    - `S46` 수렴 신호: 경계가 무너지는 곳
    - `S47` 부상과 쇠퇴
    - `S48` 비어 있는 자리
    - `S49` 2026 검증 전환의 여섯 축
    - `S50` 그래서 무엇을 할 것인가

---

## S01 · AI for Science, 2026년 지형도

*오프닝* · **2,658편 코퍼스가 말하는 8개 지형과 40개 최전선** · *표지*

> [!abstract] 핵심 메시지
> 논문 한 편씩 읽어서는 보이지 않는 것 — 어디에 사람이 몰렸고, 어디가 비었는가.

- 대상 코퍼스: **ai4s** 토픽 2,658편(리뷰 완료 전수). 사례는 **2025년 이후를 우선**해 골랐다.
- 구조: 대분류 8개 · 서브카테고리 82개 → 편수 상위 5개씩 총 40장.
- 연도 분포: 2023년 113편 → 2024년 274편 → 2025년 377편 → 2026년 1,819편. 전체의 **83%가 2025년 이후** 논문이다.
- 슬라이드 1장 = 서브카테고리 1개. 규모·기간·상태·대표 도구·대표 논문·시사점을 한 화면에.
- 각 슬라이드 하단 레퍼런스는 코퍼스의 **논문별 리뷰 문서로 바로 연결**된다.

> [!tip] 우리에게 무엇인가
> 이 덱의 목적은 요약이 아니라 배치다. 우리가 어디에 설 것인지 정하기 위한 지도.

---

## S02 · 이 지도는 어떻게 만들어졌나

*오프닝* · **Method — SPECTER2 · UMAP · HDBSCAN · c-TF-IDF** · *방법*

> [!abstract] 핵심 메시지
> 사람이 카테고리를 먼저 정하지 않았다. 논문이 뭉친 모양에서 카테고리를 꺼냈다(bottom-up).

- 임베딩: SPECTER2(논문 특화)로 전 논문을 벡터화 → UMAP 5차원 축소 → HDBSCAN 밀도 클러스터링.
- 미세 클러스터를 c-TF-IDF로 키워드화하고 LLM이 명명 → 서브카테고리 82개 → 대분류 8개로 그룹핑.
- 각 논문은 primary_category 1개 + all_categories 최대 3개를 가진다(다중 배정).
- 편수는 두 기준으로 센다 — **고유 배정**(primary 1편=1칸, 8개 합 2,658편)과 **중복 포함**(all_categories, 8개 합 7,974편). 웹 인덱스의 카테고리 헤더 편수는 중복 포함 기준이고, 이 덱의 커버리지 산술은 고유 배정 기준이다.
- 시기(start–end)·상태(가속/안정/부상/감소)·대표 도구는 카테고리별 타임라인 분석에서 가져왔다.
- 한계 1: 편수는 '연구 관심의 밀도'이지 '중요도'가 아니다. 작지만 결정적인 칸이 있다(S35 CFD 자동화 7편).
- 한계 2: 코퍼스는 주간 신규 수집 기반이라 최신 편향이 있다. 그래서 '누적 지식'이 아니라 '현재 전선' 지도로 읽어야 한다.

> [!tip] 우리에게 무엇인가
> 분류가 흔들리면 결론도 흔들린다. 그래서 방법을 먼저 밝힌다.

---

## S03 · 코퍼스 한눈에 보기

*오프닝* · **Corpus at a glance** · *코퍼스*

> [!abstract] 핵심 메시지
> 2,658편 중 1,819편이 2026년 논문. 지금 벌어지는 일을 보고 있다.

| 연도 | 편수 |  |
|---|---|---|
| 2018 | 7편 | █ |
| 2019 | 10편 | █ |
| 2020 | 10편 | █ |
| 2021 | 18편 | █ |
| 2022 | 18편 | █ |
| 2023 | 113편 | ██ |
| 2024 | 274편 | █████ |
| 2025 | 377편 | ██████ |
| 2026 | 1,819편 | ██████████████████████████████ |

- 2023년 이후 급증 — 2023년 113편 → 2024년 274편 → 2025년 377편 → 2026년 1,819편.
- 2025년 이후 논문이 전체의 83%. 이 덱이 2025+ 사례 중심인 이유다.
- 2018년 이전 소수 논문(BERT·Neural ODE·PINN)은 전 카테고리가 인용하는 뿌리 노드라 '배경'으로만 등장시킨다.
- 피인용 데이터는 일부 논문에만 붙어 있다(최신 논문 다수는 아직 인용 이력 없음) — 편수와 인용은 따로 읽어야 한다.

> [!tip] 우리에게 무엇인가
> 전략 판단에는 '현재 전선' 지도가 오히려 유리하다. 다만 고전의 부재를 결론으로 착각하면 안 된다.

---

## S04 · 8개 대분류 지형도

*오프닝* · **The eight territories** · *지형도*

> [!abstract] 핵심 메시지
> '만드는 연구'(신약·신소재)와 '재는 연구'(평가·벤치마크)가 나란히 1·2위. 이 조합이 2026년의 성격이다.

| 대분류 | 고유 배정 | 중복 포함 | 서브카테고리 | 최대 서브카테고리 |
|---|---|---|---|---|
| AI 기반 신약·신소재 발견 | 606 | 1,383 | 13 | Drug Compound Gene Signature Analysis |
| LLM·에이전트 평가 | 457 | 1,695 | 16 | Web-Augmented RL Reasoning Agents |
| 물리·환경 과학 AI | 338 | 1,011 | 6 | Neural Operator PDE Solving |
| 분자 시뮬레이션·생성 모델링 | 307 | 1,048 | 9 | Diffusion Model Reward Fine-tuning |
| 과학 자동화 에이전트 AI | 282 | 972 | 10 | Scientific Tool-Using AI Agents |
| 형식 방법론·계산 추론 | 235 | 545 | 5 | Higher-Order Logic Proof Systems |
| 과학 정보추출·질의응답 | 221 | 761 | 8 | Crosslingual Post-Training Methods |
| AI 지원 학술 커뮤니케이션 | 212 | 559 | 15 | Academic Metadata & Causal Datasets |

- 규모 상위 3개(신약·신소재, LLM 평가, 물리·환경)가 전체의 절반을 넘는다.
- 가장 작은 학술 커뮤니케이션 카테고리는 편수는 적지만 기관 정책에 가장 직접적인 근거를 준다.
- 이후 8개 파트는 이 순서(편수 내림차순)로 진행한다.

> [!tip] 우리에게 무엇인가
> 예산 배분에서 편수는 출발점일 뿐이다. 파트마다 '우리에게 무엇인가'를 따로 달아 뒀다.

---

## S05 · 관통하는 한 줄: 예측 → 설계 → 자율 → 검증

*오프닝* · **The 2026 reliability and verification turn** · *서사*

> [!abstract] 핵심 메시지
> 2025–2026 코퍼스를 관통하는 흐름은 새 모델이 아니라 '신뢰성·검증 전환'이다.

- **예측(–2021, 배경)**: BioBERT·SciBERT가 계산 기반을, PINN·Neural ODE가 미분방정식 학습을, AlphaFold2가 구조 예측을 끝냈다.
- **설계(2022–2023, 배경)**: ProteinMPNN·RFdiffusion, Pangu-Weather·GraphCast가 운용 수치예보를 넘었고 A-Lab·Coscientist가 LLM을 실험 장비에 붙였다.
- **자율(2024–2025)**: AI Scientist·Virtual Lab·Agent Laboratory가 폐루프를 시연했지만, ScienceAgentBench·LLM-SRBench(31.5%)가 주장과 실제의 간극을 드러냈다.
- **검증(2026)**: 벤치마크 감사, PINN 실패 모드 진단, ProofGate류 형식 벤치마크 결함 점검, 희소 오토인코더 해석성, 예측기반 추론, 출처·기여 추적이 동시에 부상했다.
- 즉 2026년은 '무엇을 더 할 수 있나'가 아니라 '무엇을 믿을 수 있나'를 묻는 해다.

> [!tip] 우리에게 무엇인가
> 지금 투자할 것은 '더 센 모델'이 아니라 '감사 가능한 폐루프'다. 이 문장이 뒤 45장의 요약이다.

---

## S06 · 약물–유전자 서명 분석

*제1부 · AI 기반 신약·신소재 발견* · **Drug Compound Gene Signature Analysis** · *서브카테고리*

`141편` `2018–2026` `가속` `2025+ 138편`

<sub>AI 기반 신약·신소재 발견 고유 배정 606편(중복 포함 1,383편 · 웹 인덱스 기준) · 서브카테고리 13개 · 본 파트 5개로 66% 커버</sub>

> [!quote] 파트 도입
> 코퍼스 최대 카테고리. 구조 예측이 풀린 뒤 필드 전체가 '설계'와 '검증'으로 이동했다.

> [!abstract] 핵심 메시지
> 2025–2026년 사이 세포 모델은 '읽기'에서 '반응 예측·분자 설계'로 넘어갔고, 곧바로 해석성 검증이 따라붙었다.

- 2025 Cell2Sentence가 단일세포 데이터를 '세포 문장'으로 바꿔 27B 규모 LLM으로 확장했다 — 전사체와 생물학 텍스트 지식의 통합.
- 2025 Evo 2와 2026 EDEN 스케일링 법칙으로 게놈 규모 서열 파운데이션 모델이 표준 인프라가 됐다.
- 2026 섭동–반응·가상세포 모델(AetherCell, AlphaCell, CURE, PerturbODE)이 약물 투여 후 세포 상태를 직접 예측한다.[2]
- 2026 전사체 교란 신호를 조건으로 약물 분자를 생성하는 TBDD(Transcriptome-based Drug Design)가 정식화됐다.
- 2026 해석성·비판 전환: 희소 오토인코더, CLAMP, 인과 전이가능성, 잘못 설정된 베이스라인 지적이 동시에 나왔다.[1]

**대표 도구·시스템** — SCANPY · Evo / Evo 2 · Cell2Sentence · scLDM · BioFM/BioToken · PyHealth 2.0 · AlphaCell · CLAMP

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [CLAMP: A Mechanistic Probe of Regulatory Structure in Foundation Models under Single-Cell Perturbations](../../docs/papers/9404_CLAMP_A_Mechanistic_Probe_of_Regulatory_Structure_in_Foundat/index.html) — Amaya Gallagher-Syed 외, 2026
    - CLAMP은 single-cell foundation model이 perturbation prediction에 필요한 regulatory structure를 실제로 보존하는지 여부를 예측 정확도가 아니라 명시적 gene regulatory…
2. [AetherCell: A generative engine for virtual cell perturbation and in vivo drug discovery](../../docs/papers/3008_AetherCell_A_generative_engine_for_virtual_cell_perturbation/index.html) — 2026.03
    - 본 논문은 임상 RNA-seq와 L1000 perturbation 데이터를 통합한 생성 파운데이션 모델 AetherCell을 제시한다. Specificity-driven learning framework를 통해 메커니즘 특이적 신호를 회복하…
3. [Scaling Large Language Models for Next-Generation Single-Cell Analysis](../../docs/papers/696_Scaling_Large_Language_Models_for_Next-Generation_Single-Cel/index.html) — Syed Asad Rizvi 외, 2025.04
    - 단일세포 RNA 시퀀싱 데이터를 "세포 문장(cell sentence)" 형태의 텍스트로 변환하여 대규모언어모델(LLM)로 처리하는 Cell2Sentence 프레임워크를 270억 개의 파라미터로 확장함으로써, 전사체 데이터와 생물학적 텍스트…
4. [PhenoBrain: Phenotype-Conditioned Long-Range Communication for Multi-Modal Brain Network Analysis](../../docs/papers/10178_PhenoBrain_Phenotype-Conditioned_Long-Range_Communication_fo/index.html) — Lingyuan Meng 외, 2026
    - PhenoBrain은 표현형(phenotype) 정보를 분류기 단의 후기 융합(late fusion)이 아닌 뇌 연결망 표현학습의 메커니즘 단계에서 조건부로 주입하여, 개인별 장거리(long-range) ROI 통신 패턴을 학습하는 mult…

> [!tip] 우리에게 무엇인가
> 신약 스크리닝의 1차 필터가 실험에서 예측으로 이동했다. 국내 병목은 모델이 아니라 섭동 스크린 데이터 확보다.

---

## S07 · 단백질 결합부위 예측

*제1부 · AI 기반 신약·신소재 발견* · **Protein Binding Site Prediction** · *서브카테고리*

`96편` `2021–2026` `가속` `2025+ 89편`

> [!abstract] 핵심 메시지
> 2025–2026의 화두는 구조 정확도가 아니라 설계 성공률과 감사(audit)다.

- 2025 RFdiffusion 항체 미세조정이 지정 에피토프에 결합하는 VHH·scFv를 원자 수준 정확도로 설계했다.[1]
- 2025 오픈소스 Boltz-1·Boltz-2가 AlphaFold 3급 상호작용 모델링을 개방해 진입장벽을 없앴다.
- 2026 서브초 도킹과 양자화 코폴딩(TerraBind, ACER)으로 스크리닝 처리량이 자릿수 단위로 바뀐다.
- 2026 신뢰성 감사가 동시 등장 — ProtDBench, PDFBench, ProMiSE, 적대적 변이 테스트.[3][4]
- 배경: 2021 AlphaFold2·RoseTTAFold, 2024 AlphaFold 3가 예측 문제를 사실상 종료시켰다.

**대표 도구·시스템** — AlphaFold2/3 · RoseTTAFold · ProteinMPNN · RFdiffusion · Boltz-1/Boltz-2 · BindCraft · TerraBind · ProtDBench

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Atomically accurate de novo design of antibodies with RFdiffusion](../../docs/papers/112_Atomically_accurate_de_novo_design_of_antibodies_with_RFdiff/index.html) — Nathaniel R. Bennett 외, 2025.02 · 인용 192
    - 본 연구는 RFdiffusion 신경망의 항체 특화 미세조정을 통해 원자 수준의 정확도로 사용자가 지정한 에피토프(epitope)에 결합하는 항체 가변 영역(VHH, scFv)을 완전히 컴퓨터 기반으로 설계할 수 있음을 처음으로 입증했다.…
2. [MotifCraft: scalable functional protein binder design with AlphaFold2 hallucination](../../docs/papers/10062_MotifCraft_scalable_functional_protein_binder_design_with_Al/index.html) — Océane Follonier 외, 2026
    - MotifCraft는 AlphaFold-Multimer의 hallucination(backpropagation 기반) 프레임워크를 motif scaffolding에 확장하여, 기존 diffusion 기반 방법보다 높은 in silico 성공…
3. [PDFBench: A Benchmark for De Novo Protein Design from Function](../../docs/papers/10165_PDFBench_A_Benchmark_for_De_Novo_Protein_Design_from_Functio/index.html) — Jiahao Kuang 외, 2026
    - PDFBench는 function-guided de novo protein design 분야 최초의 통합 벤치마크로, description-guided 및 keyword-guided 두 설정에서 8개의 최신 모델을 16개 지표(6개 차원)로…
4. [ProtDBench: A Unified Benchmark of Protein Binder Design and Evaluation](../../docs/papers/10261_ProtDBench_A_Unified_Benchmark_of_Protein_Binder_Design_and/index.html) — Cong Liu 외, 2026
    - ProtDBench는 de novo protein binder design 평가를 위한 표준화되고 throughput을 고려한 통합 벤치마크 프레임워크로, wet-lab annotated dataset을 활용해 structure predic…

> [!tip] 우리에게 무엇인가
> 도구는 이미 오픈이다. 경쟁축은 습식 검증률과 실패 모드 감사로 넘어갔다.

---

## S08 · 조절서열·유전자 발현 예측

*제1부 · AI 기반 신약·신소재 발견* · **Gene Enhancer Expression Prediction** · *서브카테고리*

`68편` `2018–2026` `가속` `2025+ 64편`

> [!abstract] 핵심 메시지
> 2025 AlphaGenome 이후, 서열→발현은 '예측 가능'에서 '평가 방법을 다시 짜야 하는' 단계로 들어갔다.

- 2025 AlphaGenome이 1Mb 입력 × 염기쌍 해상도로 11개 모달리티 5,930개 게놈 트랙을 동시 예측한다.[1]
- 2026 신호 희석 보정 섭동 지표와 모듈 귀납 표현으로 벤치마크 자체가 재설계되는 중이다.
- 2026 OptiPrime은 프라임 편집 메커니즘을 ODE로 모델에 직접 넣어 해석성과 일반화를 함께 잡았다.
- 2026 조직학→전사체 번역(Pixel2Gene)과 시공간 재구성(stVCR, ChronoTILE)으로 공간 오믹스와 결합한다.[2]
- 2026 edgePython처럼 분석 생태계가 파이썬으로 수렴하며 단일세포 파이프라인 진입비용이 낮아졌다.

**대표 도구·시스템** — Enformer-style models · AlphaGenome · Seq2Exp · Pleiades · GENEB · Genome-Factory · Hi-Compass

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [AlphaGenome: advancing regulatory variant effect prediction with a unified DNA sequence model](../../docs/papers/094_AlphaGenome_advancing_regulatory_variant_effect_prediction_w/index.html) — Žiga Avsec 외, 2025 · 인용 106
    - AlphaGenome은 1 메가베이스(Mb) DNA 서열 입력과 단일 염기쌍(bp) 해상도를 통합하여, 11개의 생물학적 모달리티(유전자 발현, 스플라이싱, 크로마틴 접근성, 조직인자 결합, 3D 크로마틴 구조 등)에 걸쳐 5,930개의 게…
2. [Pixel2Gene enables histology-guided reconstruction and prediction of spatial gene expression](../../docs/papers/3209_Pixel2Gene_enables_histology-guided_reconstruction_and_predi/index.html) — 2026.02
    - Pixel2Gene는 조직병리 이미지(H&E)와 공간전사체(ST) 데이터를 통합하는 딥러닝 프레임워크로, 희소하고 노이즈가 있는 ST 데이터를 개선하고 미측정 조직 영역의 공간유전자발현을 예측한다.
3. [Learning to Discover Regulatory Elements for Gene Expression Prediction](../../docs/papers/483_Learning_to_Discover_Regulatory_Elements_for_Gene_Expression/index.html) — Xingyu Su 외, 2025
    - 유전자 발현 예측을 위해 DNA 서열과 epigenomic signal로부터 인과적으로 활성화된 regulatory element를 학습 기반으로 발견하는 Seq2Exp 프레임워크를 제안한다. information bottleneck과 Be…
4. [Mechanistic machine learning enables interpretable and generalizable prediction of prime editing outcomes](../../docs/papers/3163_Mechanistic_machine_learning_enables_interpretable_and_gener/index.html) — 2026.02
    - 프라임 편집의 생물학적 메커니즘을 ordinary differential equations(ODE)로 직접 통합한 기계학습 모델 OptiPrime을 개발했으며, 74,769개의 PE 효율 데이터(1,290개 타겟)와 297,962개의 멀티-…

> [!tip] 우리에게 무엇인가
> 의미 불명 변이(VUS) 해석과 유전자치료 설계에 직결된다. 다음 관문은 규제기관이 받아들일 신뢰구간 제시.

---

## S09 · 생물학 위상·표현 해석

*제1부 · AI 기반 신약·신소재 발견* · **Topological Data Analysis for Biology** · *서브카테고리*

`49편` `2023–2026` `가속` `2025+ 48편`

> [!abstract] 핵심 메시지
> 2026년, 잘 맞히는 모델의 내부를 여는 해석성이 독립 서브필드가 됐다.

- 2026 AlphaInterp: AlphaFold 3는 진화적 맥락에 의존하는 fold recognition 알고리즘 — '예측기는 추론하지 않는다'.[1][2]
- 2026 AlphaFold Database가 4,777개 프로테옴 3,100만 복합체로 확장되고 고신뢰 180만 건을 공개했다.[1]
- 2026 프로테옴 규모 상호작용 추론(ProteomeLM, FlashPPI)과 지속 호몰로지 기반 친화도 예측이 붙었다.[4]
- 2026 단백질 언어모델의 기계적 해석성(희소 오토인코더, cross-layer transcoder)이 본격화됐다.
- 2026 DNA 언어모델과 PLM을 결합한 다중모달 변이효과 예측이 생물물리 제약 하에서 상보성을 입증했다.

**대표 도구·시스템** — ESMFold · ProteomeLM · FlashPPI · PLIP · MolX · ProtoMech · MutAtlas · FLIP2

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [AlphaFold Database expands to proteome-scale quaternary structures](../../docs/papers/3019_AlphaFold_Database_expands_to_proteome-scale_quaternary_stru/index.html) — 2026.03
    - AlphaFold Database를 단백질 복합체(homo- 및 heteromeric)의 3D 구조 예측으로 확장하였으며, 4,777개 프로테옴에서 3,100만 개 이상의 복합체를 예측하고 신뢰도 메트릭을 기반으로 180만 개의 고신뢰 복합…
2. [AlphaInterp: Probing AlphaFold 3's Internal Representations Reveals Evolutionary Determinants of Predicted Structure and Confidence](../../docs/papers/3020_AlphaInterp_Probing_AlphaFold_3s_Internal_Representations_Re/index.html) — 2026.04
    - AlphaFold 3의 내부 표현을 체계적으로 분석하여 단백질 구조 예측이 주로 진화적 맥락에 의존하며, MSA를 통해 구조적으로 제약된 위치를 식별하고 가중치에 저장된 구조 prior를 활성화하는 민감한 fold recognition 알고…
3. [MutAtlas: A PDB-Wide Energy-Guided Atlas of Protein Mutation Effects](../../docs/papers/10079_MutAtlas_A_PDB-Wide_Energy-Guided_Atlas_of_Protein_Mutation/index.html) — Ruihan Guo 외, 2026
    - 단백질 구조 데이터베이스(PDB) 전역에 걸쳐 물리 기반 에너지 모델, 단백질 언어 모델, inverse folding 모델의 단일 부위 돌연변이 신호를 정렬한 대규모 데이터셋 MutAtlas를 구축하고, 이를 바탕으로 실험 라벨 없이 다중…
4. [ProteomeLM: A Proteome-Scale Language Model Enables Accurate and Rapid Prediction of Protein-Protein Interactions and Gene Essentiality Across Taxa](../../docs/papers/10267_ProteomeLM_A_Proteome-Scale_Language_Model_Enables_Accurate/index.html) — Cyril Malbranke 외, 2026
    - ProteomeLM은 전체 proteome을 입력으로 받아 masked protein embedding 재구성을 통해 학습하는 transformer 기반 language model로, 별도의 interaction label 없이도 atten…

> [!tip] 우리에게 무엇인가
> 해석성은 규제 대응·특허·실패 원인 분석의 전제다. 수학·위상 인력이 강한 국내 그룹의 진입 여지가 크다.

---

## S10 · 과학 멀티모달 벤치마킹

*제1부 · AI 기반 신약·신소재 발견* · **Scientific Multimodal LLM Benchmarking** · *서브카테고리*

`44편` `2019–2026` `가속` `2025+ 32편`

> [!abstract] 핵심 메시지
> 2025–2026 벤치마크는 지식이 아니라 '연구를 수행하는 능력'을 잰다.

- 2025 SciKnowEval·SciCUEval이 다층 과학지식을, SciCode가 연구 코딩 능력을 분리해 측정한다.
- 2025–2026 SciVerse·P1-VL·PhysMent로 시각–언어 과학추론 평가가 확장됐다.[2][3]
- 2026 BPL 컴파일러 검증 프로토콜과 REPA로 재현성 자동화까지 벤치마크 대상이 됐다.
- 2025 BioProBench 등 도메인 종합 벤치마크가 프로토콜 수준 수행 능력을 본다.[4]
- 배경: 2019 BioBERT·SciBERT의 도메인 사전학습, 2022 Galactica의 큐레이션 코퍼스 인터페이스.

**대표 도구·시스템** — BioBERT · SciBERT · Galactica · SciKnowEval · SciCode · SciVerse · P1-VL · REPA

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Scicueval: A comprehensive dataset for evaluating scientific context understanding in large language models](../../docs/papers/713_Scicueval_A_comprehensive_dataset_for_evaluating_scientific/index.html) — Jing Yu 외, 2025
    - 본 논문은 대규모 언어모델(LLM)의 과학적 맥락 이해 능력을 평가하기 위한 포괄적 벤치마크 데이터셋 SciCUEval을 제안한다. 생물학, 화학, 물리학, 생의학, 재료과학 등 5개 도메인에 걸친 10개의 부분 데이터셋으로 구성되며, 비정…
2. [Sciverse: Unveiling the knowledge comprehension and visual reasoning of lmms on multi-modal scientific problems](../../docs/papers/737_Sciverse_Unveiling_the_knowledge_comprehension_and_visual_re/index.html) — Z. J. Guo 외, 2025
    - SCIVERSE는 대규모 멀티모달 모델(LMM)의 과학 문제 해결 능력을 세밀하게 평가하기 위한 벤치마크로, 1,147개 문제를 5가지 버전으로 변환한 5,735개 테스트 인스턴스를 제공하며, 과학 지식 이해, 멀티모달 콘텐츠 해석, 연쇄적…
3. [P1-VL: Bridging Visual Perception and Scientific Reasoning in Physics Olympiads](../../docs/papers/10150_P1-VL_Bridging_Visual_Perception_and_Scientific_Reasoning_in/index.html) — Yun Luo 외, 2026
    - P1-VL은 물리 올림피아드 문제 해결을 위해 Curriculum Reinforcement Learning과 Agentic Augmentation을 결합한 open-source vision-language model 계열로, HiPhO 벤치…
4. [BioProBench: Comprehensive Dataset and Benchmark in Biological Protocol Understanding and Reasoning](../../docs/papers/169_Bioprobench_Comprehensive_dataset_and_benchmark_in_biologica/index.html) — Yuyang Liu 외, 2025
    - 생물학적 실험 프로토콜의 절차적 추론(procedural reasoning)을 평가하기 위한 대규모 데이터셋 및 벤치마크를 제시한다. BioProCorpus(27,000개 프로토콜)로부터 구성된 550,000개 이상의 구조화된 작업 인스턴스…

> [!tip] 우리에게 무엇인가
> 벤치마크를 설계할 수 있어야 도입을 판단할 수 있다. 국내 도메인 벤치마크 부재가 그대로 의사결정 리스크다.

---

## S11 · 웹 증강 RL 추론 에이전트

*제2부 · LLM·에이전트 평가* · **Web-Augmented RL Reasoning Agents** · *서브카테고리*

`62편` `2025–2026` `가속` `2025+ 62편`

<sub>LLM·에이전트 평가 고유 배정 457편(중복 포함 1,695편 · 웹 인덱스 기준) · 서브카테고리 16개 · 본 파트 5개로 54% 커버</sub>

> [!quote] 파트 도입
> 무엇을 못하는지 재는 일이 산업이 됐다. 벤치마크 설계 역량이 곧 도입 판단 역량.

> [!abstract] 핵심 메시지
> 62편이 사실상 2025–2026 한 구간에 몰렸다. 검증가능 보상(RLVR)이 '검색하며 생각하는' 에이전트를 1년 만에 표준으로 만들었다.

- 2025 DeepSeek-R1·Kimi k1.5: 사람이 만든 추론 궤적 없이 순수 RL만으로 자기검증·재검토가 창발했다.[1]
- 2025 Search-R1·WebThinker·WebDancer가 검색을 학습 루프 안으로 집어넣은 딥리서치 에이전트를 만들었다.[2][4]
- 2025 ReTool은 코드 인터프리터 도구 사용을, Critique-GRPO·PAG·RISE는 비평·자기검증 기반 RL을 다룬다.[3]
- 2026 DR Tulu는 루브릭이 정책과 함께 진화하는 RLER로 완전 공개 8B 딥리서치 모델을 냈다.
- 2025–2026 DRE-Bench처럼 동적 추론 평가로 '유동 지능'을 따로 재는 흐름이 붙었다.

**대표 도구·시스템** — DeepSeek-R1 · Search-R1 · WebThinker · ReTool · GRPO/Critique-GRPO · WebAgent-R1 · DR Tulu

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning](../../docs/papers/265_DeepSeek-R1_incentivizes_reasoning_in_LLMs_through_reinforce/index.html) — DeepSeek-AI 외, 2025
    - 본 논문은 인간이 주석을 단 추론 궤적(reasoning trajectory) 없이 순수 강화학습(RL)을 통해 대형언어모델(LLM)의 추론 능력을 유도할 수 있음을 보여준다. RL 훈련 과정에서 모델은 자발적으로 자기 검증, 재검토, 동적…
2. [WebThinker: Empowering Large Reasoning Models with Deep Research Capability](../../docs/papers/873_WebThinker_Empowering_Large_Reasoning_Models_with_Deep_Resea/index.html) — Xiaoxi Li 외, 2025
    - 대규모 추론 모델(LRM)의 정적 지식 의존성을 극복하기 위해, 웹 탐색과 정보 수집을 추론 과정에 통합하는 자율 딥 리서치 에이전트를 제시한다. WebThinker는 LRM이 웹 페이지를 동적으로 탐색하고 실시간으로 보고서를 작성할 수 있…
3. [ReTool: Reinforcement Learning for Strategic Tool Use in LLMs](../../docs/papers/674_ReTool_Reinforcement_Learning_for_Strategic_Tool_Use_in_LLMs/index.html) — Jiazhan Feng 외, 2025
    - 강화학습(RL)을 활용하여 LLM이 추론 과정 중 코드 인터프리터(Code Interpreter, CI)를 동적으로 호출하도록 학습시키는 프레임워크로, 수학 올림피아드 문제 해결에서 o1-preview를 27.9% 초과 달성한다.
4. [Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement Learning](../../docs/papers/740_Search-R1_Training_LLMs_to_Reason_and_Leverage_Search_Engine/index.html) — Bowen Jin 외, 2025
    - 강화학습(RL)을 통해 대언어모델(LLM)이 추론 과정 중 검색 엔진을 자동으로 호출하고 활용하는 방법을 학습하는 프레임워크 Search-R1을 제안하며, 기존 RAG 대비 최대 41%의 성능 향상을 달성한다.

> [!tip] 우리에게 무엇인가
> 정답 검증기가 존재하는 과제부터 자동화가 도착한다. 보상 설계 능력이 곧 제품 경쟁력.

---

## S12 · 프런티어 모델·멀티모달 안전성 평가

*제2부 · LLM·에이전트 평가* · **GPT Audio Safety Evaluation** · *서브카테고리*

<sub>타임라인 분석 명칭: Frontier Model & Multimodal Safety Evaluation</sub>

`57편` `2023–2026` `가속` `2025+ 46편`

> [!abstract] 핵심 메시지
> 2025–2026 안전 평가가 정렬의 기하학과 리더보드 통계 검증까지 내려갔다.

- 2025 정렬은 단일 선형 방향이 아니라 활성화 공간의 다차원 직교 구조라는 분석이 나왔다(거부 방향과 역할극 방향의 분리).
- 2025–2026 온라인 안전 모니터링과 다차원 정렬 지표(MDTA/LD-Score)가 운영 도구로 들어왔다.
- 2026 과학 멀티모달 능력·안전 벤치마크가 도메인으로 확장됐다(ECG-R1, AtomWorld, HiPhO, VT-Bench).[1][4]
- 2026 리더보드 통계와 프롬프트 효과 재현 실패 보고 — 순위표 한 줄로 벤더를 고르면 안 된다.
- 배경: GPT-4·GPT-4o·o1 시스템 카드가 탈옥·음성 리스크 분석의 문서 포맷을 정착시켰다.

**대표 도구·시스템** — GPT-4o System Card · OpenAI o1 System Card · Online Safety Monitoring · MDTA/LD-Score · Leaderboard Lottery MCB · HiPhO

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [HiPhO: How Far Are (M)LLMs from Humans in the Latest High School Physics Olympiad Benchmark?](../../docs/papers/9783_HiPhO_How_Far_Are_MLLMs_from_Humans_in_the_Latest_High_Schoo/index.html) — Fangchen Yu 외, 2026
    - HiPhO는 2024-2025년 최신 고등학교 물리 올림피아드 13개 시험(총 360문제)을 수집하여, 공식 채점 기준(rubric)에 따른 answer-level 및 step-level 평가와 금·은·동 메달 기준을 적용해 (M)LLM의…
2. [The hidden dimensions of llm alignment: A multi-dimensional safety analysis](../../docs/papers/800_The_hidden_dimensions_of_llm_alignment_A_multi-dimensional_s/index.html) — Wenbo Pan 외, 2025
    - 대규모언어모델(LLM)의 안전 정렬 행동은 단일 선형 방향이 아닌 활성화 공간의 다차원 직교 방향들의 상호작용으로 제어된다. 본 연구는 안전 미세조정 과정에서 발생하는 표현 변화를 분석하여 거부 행동을 지배하는 주도적 방향과 가설적 내러티브…
3. [Online Safety Monitoring for LLMs](../../docs/papers/10130_Online_Safety_Monitoring_for_LLMs/index.html) — Mona Schirmer 외, 2026
    - 이 논문은 LLM의 출력 안전성을 실시간으로 모니터링하기 위해, 외부 verifier 신호를 risk control 기법으로 보정한 단일 threshold로 이진 알람 결정을 내리는 간단한 방법을 제안하고, 이를 수학적 추론 및 red te…
4. [VT-Bench: A Unified Benchmark for Visual-Tabular Multi-Modal Learning](../../docs/papers/10685_VT-Bench_A_Unified_Benchmark_for_Visual-Tabular_Multi-Modal/index.html) — Ziyi Jia 외, 2026
    - VT-Bench는 visual-tabular multi-modal learning을 위한 최초의 통합 벤치마크로, discriminative prediction과 generative reasoning 두 패러다임을 동시에 아우르며 9개 도메…

> [!tip] 우리에게 무엇인가
> 도입 심사 요건은 '시스템 카드 + 독립 재현' 두 개다. 벤치마크 순위는 근거가 아니라 가설이다.

---

## S13 · 오픈소스 코드 LLM·명령어 튜닝

*제2부 · LLM·에이전트 평가* · **Open-Source Code LLM Instruction Tuning** · *서브카테고리*

<sub>타임라인 분석 명칭: Open-Source Code LLM & Instruction Tuning</sub>

`43편` `2021–2026` `가속` `2025+ 33편`

> [!abstract] 핵심 메시지
> 2025–2026 평가는 함수 맞히기를 떠나 '검증 가능성'과 '저장소 규모'로 갔다.

- 2025–2026 VeriBench·VeriScale·MathlibPR·JAXBench가 형식 검증 가능한 코드 벤치마크 축을 세웠다.[1][2]
- 2025–2026 AutoNumerics-Zero·DeltaEvolve·GAE는 LLM이 수치 알고리즘 자체를 진화시켜 새 해법을 찾는다.[3]
- 2025 Copilot·GitClear 감사에서 생산성 향상과 코드 복제 증가가 동시에 관측됐다.[4]
- 2024–2025 StarCoder2·The Stack v2(619개 언어)에서 Seed-Coder로 오픈 계보가 이어졌다.
- 배경: SWE-bench(실제 GitHub 이슈 2,294건)의 초기 최고 모델 해결률 1.96%가 격차의 기준점이다.

**대표 도구·시스템** — HumanEval · StarCoder2 · DeepSeek-Coder · Self-Debug · VeriBench · AutoNumerics-Zero · Vesper

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [VeriBench: An End-to-End Formal Verification Benchmark for AI Coding Agents in Lean 4](../../docs/papers/10676_VeriBench_An_End-to-End_Formal_Verification_Benchmark_for_AI/index.html) — Brando Miranda 외, 2026
    - VeriBench는 Python 소스 코드에서 Lean 4 형식 검증 아티팩트로의 end-to-end autoformalization을 평가하는 896개 과제 벤치마크로, SCSC(Smooth Conjunctive Score for Code…
2. [VeriScale: Adversarial Test-Suite Scaling for Verifiable Code Generation](../../docs/papers/10677_VeriScale_Adversarial_Test-Suite_Scaling_for_Verifiable_Code/index.html) — Yifan Bai 외, 2026
    - VeriScale는 적대적 구현(adversarial implementation)을 활용해 검증 가능한 코드 생성 벤치마크의 테스트 스위트를 확장(expansion)하고 다시 축약(reduction)하는 프레임워크로, VERINA에 적용해…
3. [AutoNumerics-Zero: Automated Discovery of State-of-the-Art Mathematical Functions](../../docs/papers/9282_AutoNumerics-Zero_Automated_Discovery_of_State-of-the-Art_Ma/index.html) — Esteban Real 외, 2026
    - 진화적 symbolic regression을 활용해 사전 수학적 지식 없이 처음부터(empty program) 지수함수 등 초월함수를 근사하는 컴퓨터 프로그램을 자동 발견하고, 유한 정밀도(예: float32) 정확도 목표에 최적화함으로써…
4. [AI Copilot Code Quality: 2025 Data Suggests 4x Growth in Code Clones - GitClear](../../docs/papers/894_AI_Copilot_Code_Quality_2025_Data_Suggests_4x_Growth_in_Code/index.html) — Hongjing Shao 외, 2025
    - 2024년 211백만 줄의 코드 변경 분석을 통해 AI Copilot 도입이 단기 생산성은 증대하지만 코드 복제(code clones)가 4배 증가하며 장기 유지보수성을 악화시키고 있음을 실증적으로 입증했다.

> [!tip] 우리에게 무엇인가
> 연구 코드 자동화는 이미 실용권이다. 단, 산출물을 검증 가능한 형태로 강제하는 규칙이 함께 가야 한다.

---

## S14 · 자기개선·주석 공정성·통계 타당성

*제2부 · LLM·에이전트 평가* · **Self-Improvement & Annotation Fairness** · *서브카테고리*

<sub>타임라인 분석 명칭: Self-Improvement, Annotation Fairness & Statistical Validity</sub>

`42편` `2020–2026` `가속` `2025+ 40편`

> [!abstract] 핵심 메시지
> 2025–2026, '적은 라벨로 정직하게 평가하는 통계'가 이 분야의 본체가 됐다.

- 2025–2026 예측기반 추론 계열(PPAT, PPAI, 다과제 PPI, CELEUS)이 제한된 주석에서도 유효한 신뢰구간을 만든다.[1]
- 2026 의사라벨 검증과 조건부 독립성 검정(semi-knockoffs, sequential KCI)으로 평가의 전제를 검사한다.
- 2026 공정성·일반화 격차 감사가 도메인으로 퍼졌다(BiasFilter, SzCORE, EEG-FM-Bench, MassSpecGym 감사).[2][3]
- 2026 실행 기반 자동 AI 연구: 아이디어를 실제 실행해 성능으로 검증하고 그 피드백으로 정책을 학습한다.
- 2025 AutoML 도구 16종 × 실제 데이터셋 21개 실증 벤치마킹으로 자동화 도구의 실효를 재확인했다.

**대표 도구·시스템** — Don't Stop Pretraining · BiasFilter · PPAT/PPAI · CELEUS · WATCH · EEG-FM-Bench

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [CELEUS: Certifiable and Efficient LLM Evaluation via E-Processes](../../docs/papers/9386_CELEUS_Certifiable_and_Efficient_LLM_Evaluation_via_E-Proces/index.html) — Zhijian Zhou 외, 2026
    - CELEUS는 e-process 기반의 anytime-valid confidence interval(CI)을 구성하여 LLM 평가에 통계적으로 엄밀한 인증(certification)을 제공하면서, uncertainty-guided sampl…
2. [EEG-FM-Bench: A Comprehensive Benchmark for the Systematic Evaluation and Diagnostic Analyses of EEG Foundation Models](../../docs/papers/9563_EEG-FM-Bench_A_Comprehensive_Benchmark_for_the_Systematic_Ev/index.html) — Wei Xiong 외, 2026
    - EEG-FM-Bench는 다양한 사전학습 전략과 아키텍처를 가진 EEG foundation model(EEG-FM)들을 통합된 프로토콜과 진단 도구로 체계적으로 평가할 수 있게 하는 벤치마크로, 단순한 성능 비교를 넘어 gradient co…
3. [BiasFilter: An inference-time debiasing framework for large language models](../../docs/papers/158_Biasfilter_An_inference-time_debiasing_framework_for_large_l/index.html) — Xiaoqing Cheng 외, 2025
    - BiasFilter는 추론 시간(inference-time)에 대규모 언어모델(LLM)의 사회적 편향을 완화하는 모델-무관적(model-agnostic) 프레임워크로, 모델 재학습이나 파인튜닝 없이 생성 과정 중 실시간으로 편향 출력을 필터…
4. [Pseudo-Label Validation for Unsupervised Domain Adaptation](../../docs/papers/10275_Pseudo-Label_Validation_for_Unsupervised_Domain_Adaptation/index.html) — Nathan Weill 외, 2026
    - 타깃 라벨 없이 unsupervised domain adaptation에서 모델(하이퍼파라미터, 체크포인트 등)을 선택하기 위해, imputation model로 생성한 pseudo-label을 이용한 surrogate target vali…

> [!tip] 우리에게 무엇인가
> 평가 예산이 없으면 통계로 벌어야 한다. 라벨 100개로 결론 내는 법이 조직 역량이다.

---

## S15 · 불확실성 인지 생성·대리모델

*제2부 · LLM·에이전트 평가* · **Uncertainty-Aware Generative Manufacturing Models** · *서브카테고리*

<sub>타임라인 분석 명칭: Uncertainty-Aware Generative & Scientific Surrogate Models</sub>

`41편` `2023–2026` `가속` `2025+ 38편`

> [!abstract] 핵심 메시지
> 2025–2026, 대리모델의 합격 기준이 정확도에서 커버리지 보장으로 바뀌었다.

- 2025–2026 학습된 시뮬레이터와 CT 재구성에 확률 보정(retrofitting)과 커버리지 보증을 덧입힌다.
- 2026 추론시간 RL과 제약 기반 재료·분자 생성 설계(OMatG-IRL, Autoregressive Boltzmann Generators).[1]
- 2026 임상·생체신호 파운데이션 모델이 UQ를 기본 탑재한다(SleepMaMi, SIGMA-PPG, token-free ECG SSM).[4]
- 2026 생성형 자료동화(DAISI), 다중뷰 인과 발견, 확률적 멤버십 회로로 신뢰성 검사를 구조화한다.
- 2025 의료 생성 AI 스코핑 리뷰가 LLM→멀티모달 전환의 임상 근거를 PRISMA-ScR로 정리했다.

**대표 도구·시스템** — OMatG-IRL · Autoregressive Boltzmann Generators · DAISI · Membership Circuits · SleepMaMi · ProtiCelli

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Autoregressive Boltzmann Generators](../../docs/papers/9283_Autoregressive_Boltzmann_Generators/index.html) — Danyal Rehman 외, 2026
    - 본 논문은 flow 기반 Boltzmann Generator의 위상학적 제약과 계산 비용 문제를 해결하기 위해 autoregressive 방식으로 분자 밀도를 조건부 확률의 곱으로 분해하는 ArBG를 제안하고, 이를 이용해 132M 파라미터…
2. [From large language models to multimodal AI: A scoping review on the potential of generative AI in medicine](../../docs/papers/359_From_large_language_models_to_multimodal_ai_A_scoping_review/index.html) — Lukas Buess 외, 2025
    - 본 논문은 의료 분야에서 생성형 AI의 진화를 체계적으로 검토한 스코핑 리뷰로, 텍스트 기반 대규모 언어모델(LLM)에서 의료 영상, 임상 데이터를 통합하는 멀티모달 AI 시스템으로의 전환을 추적하며, PRISMA-ScR 가이드라인을 따라…
3. [Quantum latent distributions in deep generative models](../../docs/papers/10286_Quantum_latent_distributions_in_deep_generative_models/index.html) — Omar Bacarreza 외, 2026
    - 이 논문은 deep generative model의 latent distribution으로 photonic quantum processor가 생성하는 boson sampling 분포(quantum latent distribution)를 사용…
4. [SIGMA-PPG: Statistical-prior Informed Generative Masking Architecture for PPG Foundation Model](../../docs/papers/10440_SIGMA-PPG_Statistical-prior_Informed__Generative_Masking_Arc/index.html) — Zongheng Guo 외, 2026
    - SIGMA-PPG는 PPG 신호의 내재적 중복성과 노이즈 문제를 해결하기 위해 통계적 사전지식 기반의 적대적 마스킹(Prior-Guided Adversarial Masking)과 의미론적 일관성 제약(semantic consistency c…

> [!tip] 우리에게 무엇인가
> 제조·의료 도입 게이트는 '틀릴 때 틀렸다고 말하는가'다. UQ 없는 대리모델은 반입 금지 대상.

---

## S16 · 신경 연산자·물리정보 PDE 해석

*제3부 · 물리·환경 과학 AI* · **Neural Operator PDE Solving** · *서브카테고리*

<sub>타임라인 분석 명칭: Neural Operator & Physics-Informed PDE Solving</sub>

`102편` `2017–2026` `가속` `2025+ 95편`

<sub>물리·환경 과학 AI 고유 배정 338편(중복 포함 1,011편 · 웹 인덱스 기준) · 서브카테고리 6개 · 본 파트 5개로 97% 커버</sub>

> [!quote] 파트 도입
> AI가 운용 수치예보를 이긴 뒤, 경쟁축은 속도에서 보장(guarantee)으로 옮겨갔다.

> [!abstract] 핵심 메시지
> 2025–2026, 신경 연산자는 '빠른 근사'에서 '구조를 보존하는 해'로 이동했다.

- 2025 아키텍처 비교 리뷰(DeepONet·PCANet·FNO 계열)와 산업 규모 메시 적용으로 실무 구간에 진입했다.
- 2025 Discovery of Unstable Singularities: ML과 고정밀 수치해석을 결합해 3D 오일러·Boussinesq 방정식의 불안정 특이점을 처음으로 체계 발견했다.[1]
- 2026 PINN 실패 모드를 계통 진단한다 — 기울기 병리, consistency barrier, 시간 얽힘.
- 2026 구조 보존 연산자가 등장했다: Hodge 분해, 외미분, cochain 증명서.
- 2026 연산자 학습이 역문제로 확장됐다 — 영상, 플라즈마, 중력파.

**대표 도구·시스템** — PINN · DeepONet · FNO · Transolver-3 · PGD-NO · Neural-HSS · Origo · Geo-NeWF · PINNfluence · Coupled Integral PINN · EqGINO · UniDrag

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Discovery of Unstable Singularities](../../docs/papers/276_Discovery_of_Unstable_Singularities/index.html) — Yongji Wang 외, 2025.09
    - 기계학습과 고정밀 수치해석을 결합하여 3D 오일러 방정식, 비압축성 다공질 매질 방정식, Boussinesq 방정식에서 처음으로 불안정 특이점(unstable singularities)의 체계적인 발견을 보여주는 연구이다. 불안정 특이점은…
2. [Origo: Interpretable Multi-physics PDE Foundation Model through Neural Operator Splitting](../../docs/papers/10147_Origo_Interpretable_Multi-physics_PDE_Foundation_Model_throu/index.html) — Li Sun 외, 2026
    - 여러 물리 시스템을 아우르는 PDE 파운데이션 모델에서 발생하는 negative transfer와 물리 메커니즘 뒤엉킴 문제를 해결하기 위해, 고전적 operator splitting 이론을 신경망 기반으로 확장한 Neural Operato…
3. [PGD-NO: A Neural Operator with Precomputed Geometry Decomposition for 3D Million-Scale Physics Simulations](../../docs/papers/10176_PGD-NO_A_Neural_Operator_with_Precomputed_Geometry_Decomposi/index.html) — Weiheng Zhong 외, 2026
    - PGD-NO는 기하학적 인코딩 과정을 결정론적 사전계산(precomputation) 단계로 분리하여, 학습 가능한 encoding 없이 "geometry token"을 추출함으로써 단일 노드의 VRAM 한계를 넘어 1천만 개 이상 노드의 3…
4. [PINNfluence: Interpreting PINNs through Influence Functions](../../docs/papers/10197_PINNfluence_Interpreting_PINNs_through_Influence_Functions/index.html) — Aleksander Krasowski 외, 2026
    - PINN(Physics-Informed Neural Network)의 예측 및 손실 항목을 개별 training data 포인트로 귀속시킬 수 있는 influence function 기반 해석 프레임워크인 PINNfluence를 제안하며,…

> [!tip] 우리에게 무엇인가
> '빠른 해'가 아니라 '보장 있는 해'로 경쟁축이 옮겨갔다. 기존 수치해석 인력이 가장 큰 자산이 되는 구간.

---

## S17 · 잠재변수 생성 솔버

*제3부 · 물리·환경 과학 AI* · **Latent Variable Generative Solvers** · *서브카테고리*

`93편` `2018–2026` `가속` `2025+ 92편`

> [!abstract] 핵심 메시지
> 2025–2026 확산·흐름 매칭이 장기 롤아웃 안정성을 확보하며 PDE 계열을 가로질렀다.

- 2025–2026 확산 사전분포를 PDE 제약·역물리 문제로 이식했다(PODiff, PIDDM).[2]
- 2026 흐름 매칭과 불균형 최적수송으로 집단·궤적 추론을 수행한다(WFR-MFM, Recursive Flow Matching).[1]
- 2026 Walrus 등 도메인 횡단 연속체 동역학 파운데이션 모델이 등장했다.
- 2026 정준화(canonicalization)로 등변 아키텍처 없이도 대칭 분포를 학습한다.
- 2026 메시 기반 시뮬레이션의 포트-해밀턴 정식화로 물리 보존을 구조에 넣는다.

**대표 도구·시스템** — Neural ODE · PODiff · PIDDM · WFR-MFM · PACE · Recursive Flow Matching · MENO · Latent Generative Solver · Walrus · SLE-FNO · ReViT · MERLIN

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Recursive Flow Matching](../../docs/papers/10311_Recursive_Flow_Matching/index.html) — Jiahe Huang 외, 2026
    - RecFM은 서로 다른 discretization scale에 걸친 trajectory 간 self-consistency를 강제하는 recursive flow matching 프레임워크로, one-step 및 few-step(2-4 step…
2. [PODiff: Latent Diffusion in Proper Orthogonal Decomposition Space for Scientific Super-Resolution](../../docs/papers/10208_PODiff_Latent_Diffusion_in_Proper_Orthogonal_Decomposition_S/index.html) — Onkar Jadhav 외, 2026
    - PODiff는 픽셀 공간이나 학습된 비선형 latent 공간 대신 고정된 분산-정렬(variance-ordered) POD 계수 공간에서 조건부 diffusion을 수행하여, 과학적 공간 필드의 확률적 super-resolution을 저비용…
3. [ReViT: Rotational-equivariant Vision Transformers for Neural PDE Solvers](../../docs/papers/10344_ReViT_Rotational-equivariant_Vision_Transformers_for_Neural/index.html) — Hao Wei 외, 2026
    - ReViT는 grid 기반 물리 필드(스칼라·벡터)를 처리하는 Vision Transformer가 회전 대칭성을 구조적으로 보존하도록, patch별 rotation-invariant local basis를 이용해 토큰을 구성하고 Swin-s…
4. [Latent Generative Solvers for Generalizable Long-Term Physics Simulation](../../docs/papers/3149_Latent_Generative_Solvers_for_Generalizable_Long-Term_Physic/index.html) — 2026.02
    - Physics VAE와 Pyramidal Flow-Forcing Transformer로 구성된 Latent Generative Solver (LGS)가 12개 PDE 계열에 대해 결정론적 솔버의 기하급수적 오차 축적을 해결하고 20스텝 롤아…

> [!tip] 우리에게 무엇인가
> 시뮬레이션을 대체하는 설계보다, 시뮬레이션의 사전분포로 쓰는 설계가 이긴다.

---

## S18 · 과학 파운데이션 모델과 통계 엄밀성

*제3부 · 물리·환경 과학 AI* · **AI Foundation Models for Environmental Science** · *서브카테고리*

<sub>타임라인 분석 명칭: AI Foundation Models, Agents & Statistical Rigor for Science</sub>

`88편` `2020–2026` `가속` `2025+ 78편`

> [!abstract] 핵심 메시지
> 2025–2026의 핵심은 새 모델이 아니라 통계 감사와 도메인 인프라다.

- 2025 환경과학 파운데이션 모델 서베이와 AI4Science 준비도 벤치마크(AIRS-Bench, SciHorizon)가 지형을 정리했다.[4]
- 2026 통계 감사 물결: MMD/Stein 검정, knockoff 귀인, conformal 유효성, 벤치마크 무결성 진단.
- 2026 도메인 인프라가 함께 깔린다 — IAEA Fusion Data Lake, 범용 원자간 퍼텐셜(MACE-Osaka26), 실시간 FPGA/GNN 트리거링.[3]
- 2024–2025 Virtual Lab·Spacer·LLM4SR이 'AI 과학자'를 운영 가능한 형태로 구현했다.[1]
- 2024 PathChat 같은 도메인 코파일럿이 실제 전문 업무에 진입했다.

**대표 도구·시스템** — GPT-4V · PathChat · Aletheia · CARTOGRAPH · AIRS-Bench · SciHorizon · Knockoff-C2ST · lambda-PSD · MACE-Osaka26 · FLAME · TC-Bench · IAEA Fusion Data Lake

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [LLM4SR: A Survey on Large Language Models for Scientific Research](../../docs/papers/506_LLM4SR_A_Survey_on_Large_Language_Models_for_Scientific_Rese/index.html) — Ziming Luo 외, 2025.01
    - 이 논문은 LLM이 과학 연구의 전 주기 — 가설 발견, 실험 계획 및 실행, 논문 작성, 동료 평가 — 에 걸쳐 어떻게 활용되는지를 체계적으로 정리한 최초의 종합 survey이다. 각 단계별 methodology, benchmark, ev…
2. [Foundation Models for Environmental Science: A Survey of Emerging Frontiers](../../docs/papers/342_Foundation_Models_for_Environmental_Science_A_Survey_of_Emer/index.html) — Runlong Yu 외, 2025.04
    - 본 논문은 환경과학 분야에서 파운데이션 모델(Foundation Models)의 응용을 포괄적으로 검토한 최신 서베이이며, 대규모 사전학습을 통해 복잡한 환경생태계 모델링의 새로운 패러다임을 제시한다.
3. [The IAEA Fusion Data Lake Project — Accelerating AI and Big Data Applications through Open Science and FAIR Data](../../docs/papers/3257_The_IAEA_Fusion_Data_Lake_Project__Accelerating_AI_and_Big_D/index.html) — Daljeet Singh Gahle 외, 2026.04
    - 본 논문은 IAEA AI for Fusion 이니셔티브의 핵심 인프라인 Fusion Data Lake 프로젝트를 보고하며, 국제 데이터 카탈로그·데이터 페더레이션·중앙 스토리지라는 3대 축으로 구성된 글로벌 융합 데이터 플랫폼의 아키텍처와…
4. [SciHorizon: Benchmarking AI-for-Science Readiness from Scientific Data to Large Language Models](../../docs/papers/724_SciHorizon_Benchmarking_AI-for-Science_Readiness_from_Scient/index.html) — Chuan Qin 외, 2025.03
    - 과학 AI(AI4Science)의 준비 상태를 평가하기 위한 통합 벤치마킹 프레임워크로, 과학 데이터의 AI 준비도와 대규모 언어모델(LLM)의 과학 분야별 능력을 체계적으로 평가하는 종합 평가 체계를 제시한다.

> [!tip] 우리에게 무엇인가
> 도입 기관은 모델보다 감사 파이프라인을 먼저 사야 한다. 감사 없는 파운데이션 모델은 비용이다.

---

## S19 · AI 수치예보·기후 모델

*제3부 · 물리·환경 과학 AI* · **Numerical Weather Forecasting Models** · *서브카테고리*

<sub>타임라인 분석 명칭: Numerical Weather & Climate Forecasting Models</sub>

`31편` `2022–2026` `가속` `2025+ 28편`

> [!abstract] 핵심 메시지
> 2026년의 경쟁은 정확도가 아니라 확률·스펙트럼 충실도·자료동화다.

- 2026 MOSAIC이 통계적 스펙트럼 감쇠·고주파 앨리어싱·잔차 누출을 동시에 교정하는 확률 예보를 제시했다.
- 2026 U-Cast·ClimateAR로 확률·자기회귀 기후 예측이 확장됐다.[2][4]
- 2026 SENDAI는 1.56% 초희소 관측만으로 위성 NDVI 필드를 재구성하는 계층적 자료동화를 보여줬다.
- 2026 파운데이션 모델 잔차 유도 다중해상도 정제로 가뭄을 예측한다 — 백본 동결, 추론시간 래퍼만으로.
- 2026 지역 극한현상(태풍) 하이브리드 앙상블, 질량보존 기후 에뮬레이터, 물리–ML 해양·해빙 결합 모델.
- 배경: 2022 Pangu-Weather가 운용 수치예보를 처음 상회했고 2023 GraphCast·FuXi가 중기 예보 동등성을 확보했다.

**대표 도구·시스템** — Pangu-Weather · GraphCast · FuXi · U-Cast · MOSAIC · ClimateAR · FloeNet · HybridOM · MiRS-AI · LoPhyDA · WEATHER-5K · Earth-2

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [(Sparse) Attention to the Details: Preserving Spectral Fidelity in ML-based Weather Forecasting Models](../../docs/papers/10472_Sparse_Attention_to_the_Details_Preserving_Spectral_Fidelity/index.html) — Maksim Zhdanov 외, 2026
    - MOSAIC는 ML 기반 기상 예측에서 발생하는 세 가지 스펙트럼 저하 문제(통계적 스펙트럼 감쇠, 구조적 고주파 앨리어싱, 파라메트릭 고주파 잔차 누출)를 동시에 해결하는 probabilistic weather forecasting mod…
2. [U-Cast: A Surprisingly Simple and Efficient Frontier Probabilistic AI Weather Forecaster](../../docs/papers/10652_U-Cast_A_Surprisingly_Simple_and_Efficient_Frontier_Probabil/index.html) — Salva Rühling Cachay 외, 2026
    - U-Cast는 표준 U-Net 백본에 MAE 사전학습 후 CRPS 미세조정, 그리고 MC Dropout 기반 확률화라는 단순한 3단계 레시피만으로 GenCast 및 IFS ENS 수준의 확률적 일기예보 성능을 10배 이상 적은 학습·추론 비…
3. [Benchmarking Physics-Informed Time-Series Models for Operational Global Station Weather Forecasting](../../docs/papers/9302_Benchmarking_Physics-Informed_Time-Series_Models_for_Operati/index.html) — Tao Han 외, 2026
    - 본 논문은 대규모 전지구 기상관측소 시계열 데이터셋 WEATHER-5K와 이를 기반으로 한 물리 정보 결합 시계열 예측 모델 PhysicsFormer를 제안하며, 학계 TSF 모델과 실제 운영 NWP 시스템 간의 성능 격차를 종합적으로 벤치…
4. [ClimateAR: Multi-Scale Autoregressive Generative Modeling for Climate Forecasting](../../docs/papers/9406_ClimateAR_Multi-Scale_Autoregressive_Generative_Modeling_for/index.html) — Yue Yu 외, 2026
    - ClimateAR는 visual autoregressive 생성 모델을 계절-연간(seasonal-to-interannual) 기후 예측에 처음으로 적용하여, aligned tokenizer와 mixed-scale conditioning을…

> [!tip] 우리에게 무엇인가
> 기상·해양·재난 기관에 즉시 적용 가능한 성숙도다. 관건은 극한값 외삽의 독립 검증.

---

## S20 · 물리 제어 RL 견고성·real-to-sim

*제3부 · 물리·환경 과학 AI* · **Offline Reinforcement Learning Robustness** · *서브카테고리*

`14편` `2025+ 10편`

> [!abstract] 핵심 메시지
> 2025–2026, 문제는 정책 성능이 아니라 시뮬레이터 밖에서의 재현이다.

- 2025 소프트 연속체 팔의 제로샷 sim-to-real 시각 서보잉이 실제 하드웨어에서 67% 성공률을 보고했다.
- 2024–2025 OCT 유도 자율 혈관 문합 로봇(µSTAR)이 숙련 외과의와 경쟁 가능한 수준에 도달했다.
- 2026 평형 제약 하 adjoint 학습으로 변형체 조작 같은 순차 암시적 계산 문제를 제어한다.
- 제어 배리어 함수 기반 안전 보장과 오프라인 RL 견고성 평가가 이 분야의 두 축이다.

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Zero-shot sim-to-real transfer for reinforcement learning-based visual servoing of soft continuum arms](../../docs/papers/891_Zero-shot_sim-to-real_transfer_for_reinforcement_learning-ba/index.html) — Hsin-Jung Yang 외, 2025
    - 소프트 연속 팔(Soft Continuum Arms, SCAs)의 비선형 동역학을 다루기 위해 운동학과 기계적 특성을 분리한 강화학습(RL) 기반 시각 서보잉 프레임워크를 제시하며, 시뮬레이션에서만 학습한 정책을 실제 하드웨어에 직접 배포하…
2. [Neural Control: Adjoint Learning Through Equilibrium Constraints](../../docs/papers/10090_Neural_Control_Adjoint_Learning_Through_Equilibrium_Constrai/index.html) — Dezhong Tong 외, 2026
    - 본 논문은 boundary control이 equilibrium 문제 자체를 변형시키는 sequential implicit computation 상황(예: deformable linear object 조작)에서, branch-dependen…
3. [Distinguishing Imitation Error from Intrinsic Motion Learning Difficulty](../../docs/papers/9528_Distinguishing_Imitation_Error_from_Intrinsic_Motion_Learnin/index.html) — Zhaorui Meng 외, 2026
    - 본 논문은 physics-based motion imitation에서 기존 평가지표(MPJPE 등)가 임밋에이션 오류의 원인(정책 한계 vs 모션 고유 난이도)을 구분하지 못하는 문제를 지적하고, rigid-body dynamics에 기반한…
4. [LASER: Learning Active Sensing for Continuum Field Reconstruction](../../docs/papers/9878_LASER_Learning_Active_Sensing_for_Continuum_Field_Reconstruc/index.html) — Huayu Deng 외, 2026
    - LASER는 sparse sensing 하에서 continuum physical field 복원 문제를 POMDP로 정식화하고, latent world model을 통해 예측된 미래 상태를 바탕으로 센서 위치를 능동적으로 이동시키는 강화학습…

> [!tip] 우리에게 무엇인가
> 자율 실험실의 마지막 1미터는 결국 제어 문제다. 국내 로봇·정밀기계 역량과 직접 붙는 지점.

---

## S21 · 확산모델 보상 미세조정

*제4부 · 분자 시뮬레이션·생성 모델링* · **Diffusion Model Reward Fine-tuning** · *서브카테고리*

`66편` `2024–2026` `가속` `2025+ 64편`

<sub>분자 시뮬레이션·생성 모델링 고유 배정 307편(중복 포함 1,048편 · 웹 인덱스 기준) · 서브카테고리 9개 · 본 파트 5개로 76% 커버</sub>

> [!quote] 파트 도입
> 생성은 값싸졌다. 남은 문제는 합성 가능성과 독립 재분석이다.

> [!abstract] 핵심 메시지
> 2025–2026, 보상 미세조정은 '재학습 없는 추론시간 정렬'로 정리됐다.

- 2025 SVDD가 미분 불가능한 보상에서도 재학습 없이 추론시간 정렬을 가능하게 했다.
- 2025 VIDD는 가치 유도 반복 증류로 생물분자 설계용 확산모델을 안정적으로 미세조정한다.
- 2025 테스트타임 반복 정제(부분 노이징 ↔ 보상 유도 디노이징)와 동적 빔 탐색이 단일샷 방식을 대체했다.
- 2026 SGRPO·CRYSTAL 등 GRPO 계열로 결정·분자 생성기를 사후학습한다.
- 2026 e-process 안전 입자 선택과 비용인지 베이지안 최적화 정지규칙 — 멈출 시점을 통계로 결정한다.

**대표 도구·시스템** — SVDD · VIDD · GRPO/SGRPO · MP2D · CAGenMol · GILC · PT-MDM · CSMC · LABO · RAMBO

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Iterative Distillation for Reward-Guided Fine-Tuning of Diffusion Models in Biomolecular Design](../../docs/papers/446_Iterative_Distillation_for_Reward-Guided_Fine-Tuning_of_Diff/index.html) — Xingyu Su 외, 2025
    - 생물분자 설계에서 미분불가능한 보상함수(reward function)를 최적화하기 위해 확산모델(diffusion model)을 안정적으로 미세조정하는 새로운 프레임워크 VIDD(Value-guided Iterative Distillatio…
2. [Reward-Guided Iterative Refinement in Diffusion Models at Test-Time with Applications to Protein and DNA Design](../../docs/papers/682_Reward-Guided_Iterative_Refinement_in_Diffusion_Models_at_Te/index.html) — Masatoshi Uehara 외, 2025
    - 본 논문은 확산 모델(Diffusion Models)에서 테스트 타임 보상 최적화를 위한 반복적 개선 프레임워크를 제안한다. 기존의 단일 샷(single-shot) 방식과 달리, 부분 노이징과 보상 유도 디노이징의 두 단계를 반복하여 점진적…
3. [Multi-Objective Protein Design via Memory-Aware Test-Time Scaling in Diffusion Models](../../docs/papers/10068_Multi-Objective_Protein_Design_via_Memory-Aware_Test-Time_Sc/index.html) — Ming Yang 외, 2026
    - MOMST는 diffusion 기반 단백질 설계에서 retraining 없이 test-time scaling만으로 다중 목표(multi-objective) 제약을 균형있게 만족시키는 프레임워크로, memory bank와 self-contra…
4. [CAGenMol: Condition-Aware Diffusion Language Model for Goal-Directed Molecular Generation](../../docs/papers/3050_CAGenMol_Condition-Aware_Diffusion_Language_Model_for_Goal-D/index.html) — 2026.04
    - 본 논문은 discrete diffusion과 reinforcement learning을 결합하여 단백질 결합, 약물성, 독성 등 다중 목표를 동시에 만족하는 분자를 생성하는 CAGenMol 프레임워크를 제안한다. 조건부 denoising을…

> [!tip] 우리에게 무엇인가
> 보상 함수는 도메인 지식의 코드화다. 실험으로 측정 가능한 보상을 가진 팀이 이긴다.

---

## S22 · 등변 힘장·기계학습 원자간 퍼텐셜

*제4부 · 분자 시뮬레이션·생성 모델링* · **Equivariant Force Field Symmetry** · *서브카테고리*

`59편` `2022–2026` `가속` `2025+ 58편`

> [!abstract] 핵심 메시지
> 2025–2026, 등변이 기본기가 된 순간 '정말 필요한가'라는 반론과 속도전이 시작됐다.

- 2025–2026 MACE·NequIP·TensorNet·Orb-v3가 MLIP 기본 백본으로 정착했다.
- 2026 어텐션 기반 장거리 MLIP(AllScAIP, RANGE)가 수작업 기하 귀납편향의 필요성에 도전한다.[1][3]
- 2026 IO 인지·확장 메시지 패싱 커널(FlashSchNet)로 GNN 분자동역학이 고전 힘장 속도권에 진입했다.[2]
- 2026 MeshTok은 적응 메시 세분화 발상으로 PDE 트랜스포머용 다중스케일 토큰화를 구현했다.
- 2026 대칭성 원리가 양자오류정정 디코더로 수출됐다(translation-equivariant Cascade 디코더).

**대표 도구·시스템** — MACE · NequIP · FlashSchNet · AllScAIP · RANGE · MeshTok · FluxNet · Garnet · GFFMERGE

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Extending the range of graph neural networks with global encodings](../../docs/papers/3095_Extending_the_range_of_graph_neural_networks_with_global_enc/index.html) — Alessandro Caruso 외, 2026.02
    - GNN의 장거리 상호작용 모델링 한계를 극복하기 위해 attention 기반의 RANGE 프레임워크를 제안하며, master node를 통한 가상 표현으로 선형 시간 복잡도에서 전역 정보 전달을 달성한다.
2. [FlashSchNet: Fast and Accurate Coarse-Grained Neural Network Molecular Dynamics](../../docs/papers/3102_FlashSchNet_Fast_and_Accurate_Coarse-Grained_Neural_Network/index.html) — 2026.02
    - FlashSchNet은 IO 인식 최적화를 통해 SchNet 스타일의 GNN 기반 분자동역학 시뮬레이션을 6.5배 가속화하고 메모리를 80% 감축하여, 단일 GPU에서 고전적 포스필드 수준의 속도를 달성하면서도 학습 모델의 정확도를 유지한다.
3. [A recipe for scalable attention-based ML potentials: unlocking long-range accuracy with all-to-all node attention](../../docs/papers/9159_A_recipe_for_scalable_attention-based_ML_potentials_unlockin/index.html) — Eric Qu 외, 2026
    - 이 논문은 물리 기반 inductive bias를 명시적으로 넣지 않고, all-to-all node attention을 통해 순수 데이터 기반으로 long-range 상호작용을 학습하는 attention 기반 MLIP인 AllScAIP를…
4. [GFFMERGE: Efficient Merging of Graph Neural Force Fields and Beyond](../../docs/papers/9746_GFFMERGE_Efficient_Merging_of_Graph_Neural_Force_Fields_and/index.html) — Parth Verma 외, 2026
    - GFFMERGE는 message-passing GNN 레이어의 선형 구조를 활용해 모델 병합(model merging)을 embedding-alignment 기반 convex 최적화 문제로 정식화하고, closed-form 해를 도출하여 G…

> [!tip] 우리에게 무엇인가
> 계산화학 인프라 교체 시점이다. 사내에 쌓인 DFT 계산 데이터가 곧 자산이 된다.

---

## S23 · 결정구조 생성 모델링

*제4부 · 분자 시뮬레이션·생성 모델링* · **Crystal Structure Generative Modeling** · *서브카테고리*

`47편` `2023–2026` `가속` `2025+ 46편`

> [!abstract] 핵심 메시지
> 2025–2026, 결정 생성은 '많이 만들기'에서 '맞는 분포를 만들기'로 옮겨갔다.

- 2026 리만 흐름 매칭이 주기·분자 결정 생성의 기본기가 됐다(MolCrystalFlow, OrgFlow, MCFlow, DMFlow).[4]
- 2025–2026 LLM·Wyckoff 기호 생성에 선호 정렬을 결합했다(PLaID++, CrysTune, WyFormer).[1]
- 2026 MetaDNS가 well-tempered metadynamics로 이산 신경 샘플러의 모드 붕괴를 완화했다.
- 2026 전원자 평형 분포를 직접 학습하는 생성 파운데이션 모델이 등장했다.
- 2026 역문제 구조 규명으로 확장됐다 — Boltz-Jump, GLASS, CryoACE.
- 배경: 2023 GNoME이 220만 개 신규 안정 결정 구조를 발견하며 후보 공간을 열배로 늘렸다.

**대표 도구·시스템** — GNoME · MatterGen · MolCrystalFlow · PLaID++ · Riemannian MeanFlow · Boltz-Jump · GLASS · MOTIFLOW

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [PLaID++: A Preference Aligned Language Model for Targeted Inorganic Materials Design](../../docs/papers/10199_PLaID_A_Preference_Aligned_Language_Model_for_Targeted_Inorg/index.html) — Andy Xu 외, 2026
    - PLaID++는 Wyckoff 위치 기반의 대칭성 정보를 담은 텍스트 표현과 DPO 기반 강화학습(RLIP)을 결합하여 LLM이 안정적이고(stable) 고유하며(unique) 신규한(novel) 무기 결정 구조를 생성하도록 post-tra…
2. [Generative Inversion of Spectroscopic Data for Amorphous Structure Elucidation](../../docs/papers/1099_Generative_Inversion_of_Spectroscopic_Data_for_Amorphous_Str/index.html) — Jiawei Guo 외, 2026
    - GLASS는 다중 분광 측정 데이터를 역변환하여 비정질 재료의 실제적인 원자 구조를 생성하는 생성형 AI 프레임워크를 제시한다. 점수 기반 확산 모델(score-based diffusion model)과 미분 가능한 분광 시뮬레이션을 결합하…
3. [Generative Structure Search for Efficient and Diverse Discovery of Molecular and Crystal Structures](../../docs/papers/3120_Generative_Structure_Search_for_Efficient_and_Diverse_Discov/index.html) — 2026.04
    - GSS는 diffusion 기반 생성과 물리 기반 에너지 최소화를 통합하여 분자 및 결정 구조의 다양한 준안정 구조를 효율적으로 탐색하는 프레임워크이다. RSS 대비 10배 이상 낮은 샘플링 비용으로 광범위한 구조 커버리지를 달성하면서도 물…
4. [MolCrystalFlow: Molecular Crystal Structure Prediction via Flow Matching](../../docs/papers/3173_MolCrystalFlow_Molecular_Crystal_Structure_Prediction_via_Fl/index.html) — 2026.02
    - MolCrystalFlow는 분자를 강체로 모델링하고 Riemannian manifold 위에서 flow matching을 통해 격자 파라미터, 분자 배향, 위치를 동시에 학습하여 주기적 분자 결정 구조를 예측하는 생성 모델이다.

> [!tip] 우리에게 무엇인가
> 후보 목록 과잉 시대다. 합성 경로·독립 검증과 붙이지 않으면 종이 위 물질만 늘어난다.

---

## S24 · 대리 서술자 검증·반증

*제4부 · 분자 시뮬레이션·생성 모델링* · **ML Proxy Descriptor Evaluation** · *서브카테고리*

`31편` `2021–2026` `안정` `2025+ 27편`

> [!abstract] 핵심 메시지
> 이 필드의 최대 기여는 새 모델이 아니라 자율 실험실 발견 주장을 반증한 재분석이다.

- 2024 A-Lab의 신물질 43종 주장 재분석: Rietveld 정제 오류와 무질서 미고려로 실제 신규 물질은 없었다.
- 2025 화학 파운데이션 모델 관점 논문이 MLIP·역설계 적용 범위를 정리했다.
- 2025–2026 LLM 문헌 마이닝과 에이전트 역설계(MOF 코퍼스, COF용 Ara, 제올라이트 DiffSyn).[1]
- 2026 ELECTRAFI가 국소 가우시안의 닫힌 형태 푸리에 변환으로 주기 전하밀도를 즉시 예측한다.
- 2026 서지 메타데이터에서 학습한 Clever-Hans 지름길 학습을 폭로한 연구가 평가 관행을 흔들었다.

**대표 도구·시스템** — JARVIS/ALIGNN · DiffSyn · SpbNet · PI-GP · ELECTRAFI · CatFlow · Equitrain-LoRA

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [DiffSyn: a generative diffusion approach to materials synthesis planning](../../docs/papers/3077_DiffSyn_a_generative_diffusion_approach_to_materials_synthes/index.html) — Elton Pan 외, 2026.02
    - DiffSyn은 50년치 23,961건의 제올라이트 합성 레시피로 학습된 generative diffusion model으로, 목표 제올라이트 구조와 유기 템플릿이 주어졌을 때 확률적 합성 경로를 생성하며, 실제 UFI 소재 합성을 통해 검…
2. [CatFlow: Co-generation of Slab-Adsorbate Systems via Flow Matching](../../docs/papers/9378_CatFlow_Co-generation_of_Slab-Adsorbate_Systems_via_Flow_Mat/index.html) — Minkyu Kim 외, 2026
    - CatFlow는 slab 구조와 adsorbate 좌표를 하나의 flow matching objective로 동시에 co-generation하는 프레임워크로, primitive cell 기반 factorized representation을…
3. [A Perspective on Foundation Models in Chemistry](../../docs/papers/015_A_Perspective_on_Foundation_Models_in_Chemistry/index.html) — Junyoung Choi 외, 2025.04 · 인용 39
    - 화학 분야에서 대규모 사전학습 모델(Foundation Models)의 발전 현황을 검토하는 관점 논문으로, 분자 특성 예측, 기계학습 상호작용 포텐셜(MLIP), 역설계 등 다양한 화학 문제 해결에 파운데이션 모델의 적용 가능성을 종합적으…
4. [Global Plane Waves from Local Gaussians: Periodic Charge Densities in a Blink](../../docs/papers/9748_Global_Plane_Waves_from_Local_Gaussians_Periodic_Charge_Dens/index.html) — Jonas Elsborg 외, 2026
    - ELECTRAFI는 결정 물질의 주기적 전하 밀도를 예측하기 위해 실공간에서 anisotropic Gaussians를 구성하고, 이들의 closed-form Fourier transform과 Poisson summation formula를…

> [!tip] 우리에게 무엇인가
> 발견 주장에는 독립 재분석 예산을 붙여라. 반증할 수 있는 인력이 곧 신뢰 인프라다.

---

## S25 · 분자 물성·분광 검증

*제4부 · 분자 시뮬레이션·생성 모델링* · **Molecular Thermodynamic Property Prediction** · *서브카테고리*

`30편` `2026–2026` `부상` `2025+ 30편`

> [!abstract] 핵심 메시지
> 사실상 전량 2026년 신생 분야 — 물성 예측이 '검증 계층'을 달고 재등장했다.

- 2026 Peak Risk Score: 시뮬레이션-실험 스펙트럼 불일치를 확률로 채점하는 AI 과학자용 검증 계층.
- 2026 문헌에서 추출한 미할당 스펙트럼 수백만 건을 순열불변 집합 지도학습으로 NMR 화학이동 예측에 활용한다.
- 2026 MOES-Pred가 에너지 센티널 적응 노이즈와 BRICS 모티프 분해로 디노이징 사전학습을 개선했다.[1]
- 2026 DISSOLVR 같은 해석 가능한 비딥러닝 용해도 모델이 데이터 고유 잡음(aleatoric) 한계에 도달했다.
- 2026 SYMGP와 확률적 재매개화로 대칭 제약·혼합변수 베이지안 최적화를 수행한다.

**대표 도구·시스템** — ChemFlow · DISSOLVR · SYMGP · SymSpectra · Peak Risk Score · FlexMS · MOES-Pred · SAND

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [MOES-Pred: Molecular Structural Representation Learning by Adaptive Energy-Sentinel Vibration for Generalized Property Prediction](../../docs/papers/10051_MOES-Pred_Molecular_Structural_Representation_Learning_by__A/index.html) — Zhiran Hou 외, 2026
    - MOES-Pred는 분자별로 노이즈를 적응적으로 조정하는 energy sentinel 메커니즘과 BRICS 기반 motif 분해를 결합한 denoising pre-training 프레임워크로, force field 학습의 정확도와 분자 pr…
2. [Symmetry-Constrained Gaussian Processes for Sample-Efficient Molecular Property Prediction](../../docs/papers/10523_Symmetry-Constrained_Gaussian_Processes_for_Sample-Efficient/index.html) — Kaustubh S. Bukkapatnam 외, 2026
    - SYMGP는 분자 특성 함수의 물리적 대칭성(원자 순열 불변성 및 E(3) 불변성)을 커널 수준에서 엄밀하게 보장하는 Gaussian process 프레임워크로, 대칭 평균화(symmetry-averaging)를 통해 RKHS의 유효 차원을…
3. [SymSpectra: Symmetric Information Bottleneck Framework for Molecular Structure Recognition under Imbalanced Settings](../../docs/papers/10524_SymSpectra_Symmetric_Information_Bottleneck_Framework_for_Mo/index.html) — Xiaohan Qin 외, 2026
    - SymSpectra는 다중 스펙트럼(IR, 1H-NMR, 13C-NMR) 데이터를 Symmetric Conditional Information Bottleneck(SCIB) 프레임워크로 통합하고, conditional mutual infor…
4. [Do Larger Models Really Win in Drug Discovery? A Benchmark Assessment of Model Scaling in AI-Driven Molecular Property and Activity Prediction](../../docs/papers/3078_Do_Larger_Models_Really_Win_in_Drug_Discovery_A_Benchmark_As/index.html) — Jinjiang Guo, 2026.04
    - 22개 분자 엔드포인트에서 167,056회 검증을 통해 RF·GNN·대형 사전학습 모델을 비교한 결과, 모델 규모보다 표현·귀납 편향·데이터 체계·검증 프로토콜의 정합성이 약물 발견의 예측 성능을 더 잘 설명함을 입증했다.

> [!tip] 우리에게 무엇인가
> AI 과학자 워크플로에 '실험 스펙트럼과 불일치하면 멈춤' 게이트를 넣는 설계가 핵심.

---

## S26 · 도구 사용 과학 에이전트

*제5부 · 과학 자동화 에이전트 AI* · **Scientific Tool-Using AI Agents** · *서브카테고리*

`91편` `2023–2026` `가속` `2025+ 82편`

<sub>과학 자동화 에이전트 AI 고유 배정 282편(중복 포함 972편 · 웹 인덱스 기준) · 서브카테고리 10개 · 본 파트 5개로 73% 커버</sub>

> [!quote] 파트 도입
> 습식 검증 성공 사례와 '과학적으로 추론하지 않는다'는 반증이 같은 해에 나왔다.

> [!abstract] 핵심 메시지
> 2025–2026, 에이전트 경쟁력은 모델이 아니라 도구 카탈로그·프로토콜·과정 감사로 옮겨갔다.

- 2025 표준 도구 생태계가 만들어졌다 — ToolUniverse 600+ 도구, Biomni-E1, TxAgent 211개 도구.[4]
- 2025 엔드투엔드 AI 과학자(AI Scientist-v2, Kosmos, DeepScientist, aiXiv)와 회의적 평가가 같이 나왔다.[1]
- 2025 DeepScientist는 발견을 베이지안 최적화로 정식화하고 누적 Findings Memory로 탐색–활용을 조절한다.[1]
- 2025 GeneAgent는 자기검증으로 환각을 잡아 GPT-4 대비 정확도를 끌어올렸다.
- 2026 방정식·인과법칙 발견 에이전트와 과정 단위 벤치마크가 등장했다(SR-Scientist, PIEVO, MolQuest, OpenDiscoveryTrace).[2][3]

**대표 도구·시스템** — ToolUniverse · Biomni · TxAgent · AI Scientist-v2 · Kosmos · GeneAgent · TRIAGE · SR-Scientist

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [DeepScientist: Advancing Frontier-Pushing Scientific Findings Progressively](../../docs/papers/10727_deepscientist_advancing_frontier-pushing_scientific_fi/index.html) — Yixuan Weng 외, 2025.09
    - DeepScientist는 과학적 발견을 Bayesian Optimization 문제로 형식화하고, "hypothesize-verify-analyze"의 계층적 평가 프로세스와 누적 Findings Memory를 통해 exploration과…
2. [OpenDiscoveryTrace: Process Traces for Evaluating AI Scientist Workflows](../../docs/papers/10134_OpenDiscoveryTrace_Process_Traces_for_Evaluating_AI_Scientis/index.html) — Aayam Bansal 외, 2026
    - OpenDiscoveryTrace는 AI scientist agent의 최종 출력물이 아니라 추론 과정 자체를 9-필드 구조로 기록한 558개 trajectory 데이터셋으로, 이를 통해 output-only 평가에서는 드러나지 않는 모델…
3. [SR-Scientist: Scientific Equation Discovery With Agentic AI](../../docs/papers/10488_SR-Scientist_Scientific_Equation_Discovery_With_Agentic_AI/index.html) — Shijie Xia 외, 2026
    - LLM을 단순한 equation proposer가 아닌 자율적인 AI scientist로 격상시켜, code interpreter 기반 도구를 통해 데이터 분석과 equation 평가를 반복하는 long-horizon agentic 프레임워…
4. [Democratizing AI scientists using ToolUniverse](../../docs/papers/268_Democratizing_AI_scientists_using_ToolUniverse/index.html) — Shanghua Gao 외, 2025.09
    - ToolUniverse는 600개 이상의 머신러닝 모델, 데이터셋, API 및 과학 패키지를 통합하여 어떤 LLM이나 추론 모델에서도 AI 과학자(AI scientist) 시스템을 구축할 수 있는 오픈소스 생태계이다. 표준화된 AI-도구 상…

> [!tip] 우리에게 무엇인가
> 기관 도입 단위는 '모델 계약'이 아니라 '도구 레지스트리 + 감사 로그'다.

---

## S27 · 자율 과학 발견 에이전트

*제5부 · 과학 자동화 에이전트 AI* · **Autonomous Scientific Discovery Agents** · *서브카테고리*

`37편` `2024–2026` `가속` `2025+ 28편`

> [!abstract] 핵심 메시지
> 2025–2026, 성공 시연과 인식론적 반증이 같은 구간에 도착했다.

- 2025 Agent Laboratory가 문헌조사–실험–보고 3단계를 자율 수행하며 비용을 84% 줄였다.
- 2025 ScienceAgentBench·ScienceBoard·AFMBench가 자율 에이전트의 낮은 성공률을 드러냈다.[2]
- 2025 AstroAgents 등 도메인 다중 에이전트가 질량분석 데이터에서 가설을 자동 생성한다.
- 2026 'AI scientists produce results without reasoning scientifically': 25,000회 이상 실행에서 증거 무시 68%.[1]
- 2026 에이전트 운영체제(SCION, EvoMaster)와 반증 중심 폐루프(POPPER 계열)가 대안으로 제시된다.

**대표 도구·시스템** — Virtual Lab · POPPER · CRISPR-GPT · InternAgent · ScienceAgentBench · VASPilot · FermiLink · SCION

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [AI scientists produce results without reasoning scientifically](../../docs/papers/9108_ai_scientists_produce_results_without_reasoning_scienti/index.html) — Martiño Ríos-García 외, 2026
    - 본 논문은 LLM 기반 scientific agent들이 과학적 추론의 인식론적 규범을 따르지 못한다는 점을 체계적으로 입증한다. 25,000개 이상의 agent 실행을 통해 base model이 성능과 행동의 주요 결정자임을 보였으며, 증…
2. [ScienceAgentBench: Toward Rigorous Assessment of Language Agents for Data-Driven Scientific Discovery](../../docs/papers/716_ScienceAgentBench_Toward_Rigorous_Assessment_of_Language_Age/index.html) — Ziru Chen 외, 2025.03
    - 본 논문은 대규모언어모델(LLM) 기반 언어에이전트(Language Agents)의 데이터 기반 과학 발견 수행능력을 엄밀하게 평가하기 위한 벤치마크 ScienceAgentBench를 제시한다. 최근 LLM이 과학 연구 자동화를 완전히 자동…
3. [Scienceboard: Evaluating multimodal autonomous agents in realistic scientific workflows](../../docs/papers/717_Scienceboard_Evaluating_multimodal_autonomous_agents_in_real/index.html) — Qiushi Sun 외, 2025
    - 본 논문은 현실적인 과학 워크플로우에서 멀티모달 자율 에이전트를 평가하기 위한 SCIENCEBOARD 환경과 벤치마크를 제시한다. 생화학, 천문학, 지정보학 등 6개 과학 도메인에서 169개의 고품질 작업을 통해 최신 LLM/VLM 기반 에…
4. [Autonomous Agents for Scientific Discovery: Orchestrating Scientists, Language, Code, and Physics](../../docs/papers/137_Autonomous_Agents_for_Scientific_Discovery_Orchestrating_Sci/index.html) — Lianhao Zhou 외, 2025.10
    - 대규모 언어 모델(LLM) 기반 자율 에이전트(Scientific Agents)가 과학 발견의 전체 생명주기를 자동화하고 가속화할 수 있는 새로운 패러다임을 제시한다. 이들 에이전트는 자연언어, 프로그래밍 코드, 물리 정보를 통합하여 인간…

> [!tip] 우리에게 무엇인가
> '자율'을 사지 말고 '반증 루프'를 사라. 성공률보다 실패할 때 멈추는 능력이 중요하다.

---

## S28 · 임상 LLM 응용

*제5부 · 과학 자동화 에이전트 AI* · **Clinical LLM Applications** · *서브카테고리*

`31편` `2023–2026` `가속` `2025+ 24편`

> [!abstract] 핵심 메시지
> 2025–2026, 임상 LLM의 관문은 정확도가 아니라 유보(defer)와 검증이다.

- 2025 Psyche가 다면 구성 기반 시뮬레이션 환자로 정신과 상담 에이전트를 윤리적·정량적으로 평가한다.
- 2025 PatientSim·ClientCAST 등 환자·내담자 시뮬레이터가 평가 인프라로 자리 잡았다.[2]
- 2026 EHR·생리신호 파운데이션 모델과 경로 모델링이 확산됐다(PathwayLLM, EHR-FM 희소 오토인코더).[1]
- 2026 안전·환각 완화·적응 추론·유보 결정(MEDA, AdaThink-Med, ARQS, Act-or-Defer)이 핵심 주제가 됐다.[4]
- 2024–2025 AI 대화 에이전트의 심리적 위험을 경험 기반으로 유형화한 연구가 설계 지침을 제시했다.

**대표 도구·시스템** — MedAgents · AI Hospital · PatientSim · MedSyn · PathwayLLM · MEDA · Salus · HetMedAgent

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [PathwayLLM: Explainable Clinical Trajectory Modeling with Structured Pathways for Sepsis Prediction](../../docs/papers/10162_PathwayLLM_Explainable_Clinical_Trajectory_Modeling_with_Str/index.html) — Zhengqiu Yu 외, 2026
    - PathwayLLM은 시계열, 이종 그래프(patient-diagnosis-medication), 통계적 dependency discovery 기반 pathway 신호를 pretrained LLM에 결합하여 patient-level seps…
2. [Patientsim: A Persona-Driven Simulator for Realistic Doctor-Patient Interactions](../../docs/papers/606_Patientsim_A_persona-driven_simulator_for_realistic_doctor-p/index.html) — Daeun Kyung 외, 2025
    - PATIENTSIM은 다양한 환자 페르소나를 반영하여 현실적인 의사-환자 상호작용을 시뮬레이션하는 LLM 기반 환자 시뮬레이터로, 임상 전문가의 검증을 통해 강건성을 입증했다.
3. [Psyche: A multi-faceted patient simulation framework for evaluation of psychiatric assessment conversational agents](../../docs/papers/644_Psyche_A_multi-faceted_patient_simulation_framework_for_eval/index.html) — Jingoo Lee 외, 2025
    - 정신과 진료 대화형 에이전트(PACA)의 임상 적절성을 체계적으로 평가하기 위해 다면적 정신의학적 구성(Multi-Faceted Construct, MFC)을 기반으로 한 시뮬레이션 환자 프레임워크를 제시한다. 이는 윤리적 안전성을 보장하면…
4. [MEDA: Medical-Oriented Activation Editing for Hallucination Mitigation in Medical Large Vision-Language Model](../../docs/papers/10006_MEDA_Medical-Oriented_Activation_Editing_for_Hallucination_M/index.html) — Tianbo Wang 외, 2026
    - MEDA는 의료 영상 해석에 특화된 최초의 activation editing 기법으로, Query-decisive Manifestation Steering(QMS)과 Principle-driven Diagnosis Induction(PDI)…

> [!tip] 우리에게 무엇인가
> 규제 진입 경로는 정확도가 아니라 유보(defer) 정책의 문서화다.

---

## S29 · 장비·시설 자동화 에이전트

*제5부 · 과학 자동화 에이전트 AI* · **Multi-Agent Quantum Experiment Execution** · *서브카테고리*

<sub>타임라인 분석 명칭: Multi-Agent Quantum & Laboratory Experiment Execution</sub>

`27편` `2024–2026` `가속` `2025+ 22편`

> [!abstract] 핵심 메시지
> 2025–2026, 에이전트가 장비를 잡았다 — 큐비트 보정, 방사광 빔라인, 지구관측.

- 2025 로봇 AI 화학자와 양자화학 에이전트가 실장비에 붙었다(ChemAgents, El Agente Q, QCopilot), AutoBio VLA 벤치마크도 등장.
- 2025 Earth-Agent가 다중스펙트럼·지구관측 제품을 통합 처리하고 전문가 검증 248개 과제로 평가된다.[1]
- 2025 BehaveAgent는 재학습 없이 종을 가로질러 동물 행동을 제로샷 분석한다.
- 2025–2026 시설 에이전트가 자리 잡는다 — Advanced Photon Source의 EAA, AI-native 가속기.
- 2026 체화 발견 프레임워크와 벤치 수준 바이오보안 평가(Embodied Science PLAD, ENPIRE, ABC-Bench).
- 배경: 2024 k-agents가 초전도 양자 프로세서를 자율 보정했다.

**대표 도구·시스템** — k-agents · ChemAgents · El Agente Q · QCopilot · AutoBio · EAA · Earth-Agent · SP-Mind

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Earth-Agent: Unlocking the Full Landscape of Earth Observation with Agents](../../docs/papers/298_Earth-Agent_Unlocking_the_Full_Landscape_of_Earth_Observatio/index.html) — Peilin Feng 외, 2025.09
    - 본 논문은 RGB 이미지를 넘어 다중스펙트럼 데이터와 지구 관측 제품(Earth Products)을 통합적으로 처리하는 에이전트 기반 프레임워크 Earth-Agent를 제시하며, 이를 평가하기 위한 248개의 전문가 검증 과제로 구성된 Ea…
2. [El Agente: An Autonomous Agent for Quantum Chemistry](../../docs/papers/308_El_Agente_An_Autonomous_Agent_for_Quantum_Chemistry/index.html) — Yunheng Zou 외, 2025
    - 본 연구는 LLM 기반 다중 에이전트 시스템(El Agente Q)을 통해 양자화학 워크플로우를 자연언어 프롬프트로부터 동적으로 생성·실행하는 자율 시스템을 제시한다. 계층적 메모리 프레임워크, 적응적 도구 선택, 자동 오류 복구를 특징으로…
3. [LLM-based Multi-Agent Copilot for Quantum Sensor](../../docs/papers/501_LLM-based_Multi-Agent_Copilot_for_Quantum_Sensor/index.html) — Rong Sha 외, 2025
    - 본 논문은 대규모 언어 모델(LLM) 기반 다중 에이전트 시스템인 QCopilot을 제시하여 양자 센서(특히 냉원자 원자 냉각) 개발 과정의 자동화와 진단을 실현했다. 이를 통해 수동 실험 대비 약 100배의 속도 향상을 달성하며, 다중 매…
4. [Embodied Science: Closing the Discovery Loop with Agentic Embodied AI](../../docs/papers/310_Embodied_Science_Closing_the_Discovery_Loop_with_Agentic_Emb/index.html) — Xiang Zhuang 외, 2026.03
    - 본 논문은 과학 발견을 고립된 예측 작업이 아닌 물리 세계와의 지속적 상호작용을 통한 폐쇄 루프 프로세스로 재정의하는 Embodied Science 패러다임을 제시한다. 이를 구현하기 위해 지각(Perception)–언어(Language)–…

> [!tip] 우리에게 무엇인가
> 방사광·중성자·핵융합 같은 국가 대형시설이 가장 빠른 국내 적용처다. 보안 평가를 동반해야 한다.

---

## S30 · 다중 에이전트 사회 시뮬레이션

*제5부 · 과학 자동화 에이전트 AI* · **Multi-Agent Social Simulation** · *서브카테고리*

`21편` `2021–2026` `안정` `2025+ 15편`

> [!abstract] 핵심 메시지
> 2025–2026, '에이전트를 더 붙이면 좋아지나'에 대한 정량 답이 나오기 시작했다.

- 2025 Vending-Bench 등 장기 일관성 벤치마크가 다중 에이전트가 무너지는 지점을 드러냈다.[3]
- 2025 에이전트 시스템 스케일링 법칙: 도구 활용도·모델 능력·과제 특성의 상호작용으로 MAS 이득 조건을 정식화했다.
- 2026 에이전트 신뢰성 과학이 일관성·견고성·예측가능성·안전 4축으로 문제를 분해한다.
- 2026 다수결을 넘어선 집계 이론(Optimal Weight)과 YC-Bench류 신뢰성 벤치마크가 등장했다.[1]

**대표 도구·시스템** — Vending-Bench · YC-Bench · CRAFTY institutional agents · EduMirror · AdaSociety

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [YC-Bench: Benchmarking AI Agents for Long-Term Planning and Consistent Execution](../../docs/papers/3398_YC-Bench_Benchmarking_AI_Agents_for_Long-Term_Planning_and_C/index.html) — Muyu He 외, 2026
    - YC-Bench는 LLM 에이전트의 장기 계획과 일관된 실행 능력을 평가하기 위한 벤치마크로, 1년 동안 수백 턴을 거쳐 시뮬레이션된 스타트업을 운영하도록 하는 POMDP 기반 환경을 제공한다. 불충실한 클라이언트와 증가하는 급여 비용 등…
2. [EduMirror: Modeling Educational Social Dynamics with Value-driven Multi-agent Simulation](../../docs/papers/9561_EduMirror_Modeling_Educational_Social_Dynamics_with_Value-dr/index.html) — Jingzhe Lin 외, 2026
    - EduMirror는 심리적 욕구와 사회적 가치 지향(social value orientation)에 기반한 value-driven agent와 관찰 가능한 행동·잠재적 심리 상태를 함께 측정하는 dual-track measurement pr…
3. [Vending-Bench: A Benchmark for Long-Term Coherence of Autonomous Agents](../../docs/papers/865_Vending-Bench_A_Benchmark_for_Long-Term_Coherence_of_Autonom/index.html) — Axel Backlund 외, 2025.02
    - 본 논문은 LLM 기반 에이전트가 장기간(>2천만 토큰)에 걸쳐 일관된 성능을 유지하는 능력을 평가하기 위해 자판기 운영이라는 단순하지만 장시간 지속되는 비즈니스 시뮬레이션 환경을 제시한다. 실험 결과 Claude 3.5 Sonnet과 o3…
4. [Multi-agent risks from advanced AI](../../docs/papers/562_Multi-agent_risks_from_advanced_ai/index.html) — Lewis Hammond 외, 2025
    - 다중 에이전트 AI 시스템의 대규모 배포로 인해 발생하는 새로운 위험들을 체계적으로 분류하고, 3가지 주요 실패 모드(miscoordination, conflict, collusion)와 7가지 위험 요소(information asymmet…

> [!tip] 우리에게 무엇인가
> 다중 에이전트는 만능이 아니다. 단일 에이전트가 더 낫다는 근거가 이제 존재한다.

---

## S31 · 고차논리 형식 정리증명

*제6부 · 형식 방법론·계산 추론* · **Higher-Order Logic Proof Systems** · *서브카테고리*

`157편` `2020–2026` `가속` `2025+ 139편`

<sub>형식 방법론·계산 추론 고유 배정 235편(중복 포함 545편 · 웹 인덱스 기준) · 서브카테고리 5개 · 본 파트 5개로 100% 커버</sub>

> [!quote] 파트 도입
> 검증기가 있는 도메인은 자동화가 끝나간다. 이제 검증기를 만드는 일이 병목.

> [!abstract] 핵심 메시지
> 2026, 형식 증명은 저장소 규모 자동 형식화와 벤치마크 결함 감사로 넘어갔다.

- 2026 M2F가 검증자 피드백 루프로 3주 만에 153,853줄 Lean 라이브러리를 자동 형식화했다.
- 2026 에이전트형 증명기와 저장소 규모 형식화가 표준이 됐다(Goedel-Architect, LeanFlow, Numina-Lean-Agent).[2]
- 2026 벤치마크 무결성 감사가 시작됐다 — ProofGate, Ground False, 형식 벤치마크 결함 점검.[3]
- 2026 자연어 증명 검증을 비관적·의무 커버리지 판정으로 다룬다.
- 배경: 2020 GPT-f의 Metamath 기여, 2021 miniF2F, 2024 DeepSeek-Prover의 Lean 4 합성 증명 800만 쌍.[1]

**대표 도구·시스템** — Lean 4 / Mathlib · Isabelle · Metamath · Dafny · Rocq · miniF2F · DeepSeek-Prover · Lean Copilot · SorryDB · APE-Bench · AXLE

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [miniF2F-Dafny: LLM-Guided Mathematical Theorem Proving via Auto-Active Verification](../../docs/papers/10033_miniF2F-Dafny_LLM-Guided_Mathematical_Theorem_Proving_via_Au/index.html) — Mantas Baksys 외, 2026
    - LLM이 수학 정리를 자동-능동 검증기(auto-active verifier)인 Dafny에서 증명하도록 유도하는 최초의 벤치마크 MINIF2F-DAFNY를 제시하며, SMT 자동화와 LLM의 고수준 증명 안내가 상호보완적임을 실증한다.
2. [Numina-Lean-Agent: An Open and General Agentic Reasoning System for Formal Mathematics](../../docs/papers/10115_Numina-Lean-Agent_An_Open_and_General_Agentic_Reasoning_Syst/index.html) — Junqi Liu 외, 2026
    - 범용 코딩 에이전트(Claude Code)에 Numina-Lean-MCP라는 도구 모음을 결합하여, 별도의 학습 없이도 최신 base model 교체만으로 성능을 향상시킬 수 있는 개방적이고 범용적인 formal theorem proving…
3. [ProofGate: A Reproducible Audit of Faithfulness, Alignment, and Vacuity in State-of-the-Art Lean Theorem Provers](../../docs/papers/10257_ProofGate_A_Reproducible_Audit_of_Faithfulness_Alignment_and/index.html) — Edison Yang 외, 2026
    - 최근 SOTA neural theorem prover들이 miniF2F, PutnamBench에서 보고하는 높은 pass rate가 사실은 proof faithfulness, statement alignment, problem vacuity…
4. [Agentic Separation Logic Specification Synthesis](../../docs/papers/9211_Agentic_Separation_Logic_Specification_Synthesis/index.html) — Tarun Suresh 외, 2026
    - Spec-Agent는 대규모 C++ 코드베이스에서 정적 분석과 런타임 힙 추적으로 적절한 명세 언어(propositional, first-order, propositional separation, first-order separation l…

> [!tip] 우리에게 무엇인가
> 검증기가 있는 도메인은 자동화가 끝나간다. 이제 새 병목은 검증기 자체를 만드는 일이다.

---

## S32 · 이론 한계·AI 조력 증명

*제6부 · 형식 방법론·계산 추론* · **Theoretical Complexity & Quantum Bounds** · *서브카테고리*

`33편` `2024–2026` `가속` `2025+ 32편`

> [!abstract] 핵심 메시지
> 2025–2026, AI가 실제로 새 근사 한계와 반례를 생산하기 시작했다.

- 2025 AlphaEvolve가 MAX-CUT·MAX-k-CUT·metric-TSP 근사 한계를 갱신했다.
- 2026 GPT-5 Pro가 NICD-with-erasures에서 다수결 최적성에 대한 반례를 제시했다.
- 2026 Gemini Deep Think 사례연구가 이론전산·경제학·최적화·물리 미해결 문제의 인간–AI 협업 기법을 일반화했다.
- 2026 TTT-Discover는 테스트타임에 정책 자체를 RL로 계속 학습시켜 문제 특이적으로 개선한다.
- 2026 기계 검증 이론(MerLean, Scarf-Brouwer-Nash, Lean 게임이론)과 양자 학습 한계(junta states, QAC0)가 함께 나왔다.[1]

**대표 도구·시스템** — AlphaEvolve · Gemini Deep Think · Lean 4 · MerLean · PEP/PEPFlow · Aristotle

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [MerLean: An Agentic Framework for Autoformalization in Quantum Computation](../../docs/papers/532_MerLean_An_Agentic_Framework_for_Autoformalization_in_Quantu/index.html) — Yuanjie Ren 외, 2026.02
    - 본 논문은 양자계산 이론 논문을 자동으로 기계검증 가능한 Lean 4 코드로 변환하는 완전 자동화 에이전트 프레임워크 MerLean을 제시한다. 3개 양자계산 논문에서 114개 명제로부터 2,050개 Lean 선언을 생성하며 전체 논문의 자…
2. [Optimal Quantum Speedups for Repeatedly Nested Expectation Estimation](../../docs/papers/10139_Optimal_Quantum_Speedups_for_Repeatedly_Nested_Expectation_E/index.html) — Yihang Sun 외, 2026
    - 고정된 horizon을 갖는 repeatedly nested expectations (RNEs) 추정 문제에 대해, quantum computing을 활용하여 tilde O(varepsilon^{-1}) 비용으로 varepsilon-오차를…
3. [Proving Your Way to Cooperation: Formalizing Proof-Based Open Source Game Theory in Lean](../../docs/papers/10273_Proving_Your_Way_to_Cooperation_Formalizing_Proof-Based_Open/index.html) — Colomban Duclaux 외, 2026
    - Lean 4를 이용해 proof-based Open Source Game Theory(OSGT)를 최초로 기계 검증 가능한 형태로 형식화하고, 자연어 전략 설명을 Lean으로 자동 증명하는 agentic pipeline을 구축했으며, 이를…
4. [Learning Junta Distributions, Quantum Junta States, and QAC^0 Circuits](../../docs/papers/9913_Learning_Junta_Distributions_Quantum_Junta_States_and_QAC0_C/index.html) — Jinge Bao 외, 2026
    - 이 논문은 junta 분포, 이를 양자화한 junta state, 그리고 QAC0 회로 학습 문제를 통합적으로 다루며, QAC0 회로의 Choi state가 low-degree일 뿐 아니라 실제로 junta state에 가깝다는 새로운 관찰…

> [!tip] 우리에게 무엇인가
> 'AI가 정리를 증명한다'는 이제 사례 문제다. 인간–AI 협업 프로토콜 자체가 산출물이 된다.

---

## S33 · 대칭성 인지 솔버·방정식 발견

*제6부 · 형식 방법론·계산 추론* · **Symmetry-Aware PDE Solvers** · *서브카테고리*

<sub>타임라인 분석 명칭: Symmetry-Aware PDE Solvers & Equation Discovery</sub>

`24편` `2024–2026` `가속` `2025+ 23편`

> [!abstract] 핵심 메시지
> 2025–2026, LLM 기호회귀의 실제 천장이 숫자로 찍혔다 — 31.5%.

- 2025 LLM-SRBench(4개 분야 239문제)는 암기 저항 설계에서 최고 모델 기호 정확도 31.5%를 보고했다.[2]
- 2025 CodePDE는 LLM이 PDE 솔버 코드를 직접 생성하는 추론 프레임워크를 제시했다.[1]
- 2025 DrSR은 데이터 구조 분석과 생성 이력을 함께 쓰는 이중 추론으로 기호회귀 정확도를 끌어올렸다.
- 2025–2026 AutoNumerics·RAPNet이 학습된 AMG 보정 등 고전 수치기법과 접합한다.[3][4]
- 2026 통계·견고성 프로토콜이 붙었다 — ASyMOB, GeoRepEval, Holm-Bonferroni 솔버 검증.

**대표 도구·시스템** — LLM-SR · DrSR · IGSR · LLM-SRBench · CodePDE · AutoNumerics · SIGS · RAPNet · ASyMOB

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [CodePDE: An Inference Framework for LLM-driven PDE Solver Generation](../../docs/papers/232_CodePDE_An_Inference_Framework_for_LLM-driven_PDE_Solver_Gen/index.html) — Shanda Li 외, 2025
2. [LLM-SRBench: A New Benchmark for Scientific Equation Discovery with Large Language Models](../../docs/papers/504_Llm-srbench_A_new_benchmark_for_scientific_equation_discover/index.html) — Parshin Shojaee 외, 2025
    - 본 논문은 대규모 언어 모델(LLM) 기반 과학 방정식 발견의 진정한 능력을 평가하기 위해 암기를 방지하는 종합적 벤치마크 LLM-SRBench를 제안한다. 4개 과학 분야에서 239개 도전 문제로 구성되어 있으며, 최고 성능 모델도 31.…
3. [RAPNet: Accelerating Algebraic Multigrid with Learned Sparse Corrections](../../docs/papers/10294_RAPNet_Accelerating_Algebraic_Multigrid_with_Learned_Sparse/index.html) — Yali Fink 외, 2026
    - RAPNet은 algebraic multigrid(AMG)의 coarse-grid operator(Al+1, Pl, Rl)에 대해 GNN이 sparse한 additive correction을 학습하여, sparsity와 convergence…
4. [AutoNumerics: An Autonomous, PDE-Agnostic Multi-Agent Pipeline for Scientific Computing](../../docs/papers/142_AutoNumerics_An_Autonomous_PDE-Agnostic_Multi-Agent_Pipeline/index.html) — Jianda Du 외, 2026.02
    - AutoNumerics는 자연어로 서술된 PDE 문제를 입력받아, 다중 LLM 에이전트가 협업하여 투명하고 해석 가능한 고전적 수치 해법(classical numerical solver)을 자율적으로 설계·구현·디버깅·검증하는 프레임워크이다…

> [!tip] 우리에게 무엇인가
> 방정식 발견은 아직 보조 도구다. 다만 물리 제약을 붙이면 즉시 실무 가치가 나온다.

---

## S34 · LLM 지원 구조·물리 설계 최적화

*제6부 · 형식 방법론·계산 추론* · **LLM-Assisted Structural Optimization** · *서브카테고리*

<sub>타임라인 분석 명칭: LLM-Assisted Structural & Physical Design Optimization</sub>

`14편` `2023–2026` `가속` `2025+ 10편`

> [!abstract] 핵심 메시지
> 2025–2026, 설계 루프에 시뮬레이터를 붙이자 주 단위 작업이 분 단위가 됐다.

- 2025 다중 에이전트 자동차 설계가 스케치부터 공기역학 시뮬레이션까지 전 주기를 수 주에서 수 분으로 줄였다.
- 2026 사전계산 수치 그린함수(PNGF)로 전자기 소자의 준실시간 전파 역설계가 가능해졌다.
- 2026 물리 정렬 벤치마크가 나왔다 — BuildArena, Z3 SMT 검사를 붙인 CADEngBench.[1][2]
- 2026 리소그래피 세계모델과 GRPO 튜닝 흐름 매칭(LithoDreamer, LithoGRPO)이 반도체 공정으로 확장한다.[3][4]
- 배경: 2023 LMEA가 LLM을 진화 연산자로 썼고, 2024 GraphMetaMat이 GNN+RL+MCTS로 메타물질을 역설계했다.

**대표 도구·시스템** — LMEA · LEO · ImprovEvolve · GraphMetaMat · AutoMS · AutoCircuit · CADEngBench · BuildArena · LithoGRPO

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [BuildArena: A Physics-Aligned Interactive Benchmark of LLMs for Engineering Construction](../../docs/papers/9361_BuildArena_A_Physics-Aligned_Interactive_Benchmark_of_LLMs_f/index.html) — Tian Xia 외, 2026
    - BuildArena는 자연어 지시를 물리적으로 실현 가능한 3D 구조물로 변환하는 LLM의 공학적 건설(engineering construction) 능력을 평가하기 위한 최초의 physics-aligned interactive benchm…
2. [CADEngBench: Can AI Systems Co-Author Engineering Designs? A Hierarchical Benchmark for Physics-Verified Parametric CAD Generation](../../docs/papers/9362_CADEngBench_Can_AI_Systems_Co-Author_Engineering_Designs_A_H/index.html) — Harmanjot Singh 외, 2026
    - CADEngBench는 40개의 CadQuery 기반 엔지니어링 CAD 생성 과제를 L0(컴파일/위상), L1(기하 충실도), L2(파라메트릭 무결성, perturbation robustness + Z3 SMT), L3(닫힌형 물리 검증)의…
3. [LithoDreamer: A Physics-Informed World Model for Multi-Stage Computational Lithography](../../docs/papers/9950_LithoDreamer_A_Physics-Informed_World_Model_for_Multi-Stage/index.html) — Yuqi Jiang 외, 2026
    - LithoDreamer는 computational lithography의 "Layout-Mask-Resist Image-ADI" 다단계 파이프라인을 물리 정보 기반 World Model(WM)로 정식화하여, 공정 개입(process inte…
4. [LithoGRPO: Fast Inverse Lithography via GRPO Reinforced Flow Matching](../../docs/papers/9952_LithoGRPO_Fast_Inverse_Lithography_via_GRPO_Reinforced_Flow/index.html) — Yao Lai 외, 2026
    - LithoGRPO는 flow-matching 기반 생성 모델에 GRPO 강화학습 미세조정을 결합해 Inverse Lithography Technology(ILT)의 mask 생성을 미분 가능/불가능 물리적 지표를 모두 최적화하도록 설계한 프…

> [!tip] 우리에게 무엇인가
> 제조업 R&D에 가장 직접적인 서브카테고리다. 시뮬레이터 라이선스와 설계 데이터가 진입 조건.

---

## S35 · LLM 주도 CFD·멀티피직스 자동화

*제6부 · 형식 방법론·계산 추론* · **LLM-Driven CFD Simulation Automation** · *서브카테고리*

<sub>타임라인 분석 명칭: LLM-Driven CFD & Multiphysics Simulation Automation</sub>

`7편` `2024–2026` `부상` `2025+ 5편`

> [!abstract] 핵심 메시지
> 최소 규모(7편)인데 2025–2026 보고된 성공률은 이미 운용 가능 수준이다.

- 2025 OpenFOAMGPT 2.0이 450회 이상 시뮬레이션에서 100% 성공을 보고했다.[3][4]
- 2025 MooseAgent가 FEM 입력파일 생성에서 93% 성공률을 달성했다.[2]
- 2025 MLLM 기반 VER가 비디오에서 내재 좌표계와 지배 방정식을 제로샷으로 발견한다.
- 2026 TurboAgent가 조건부 확산 + 대체모델 + LLM 최적화 + 고충실도 CFD/FEA 검증으로 터보기계 설계 폐루프를 닫았다.[1]
- 2026 PhyNiKCE는 기호 지식엔진과 결정적 RAG로 물리 타당성을 강제한다.
- 배경: 2024 MetaOpenFOAM이 자연어에서 전체 CFD 워크플로까지 다중 에이전트로 자동화했다.

**대표 도구·시스템** — MetaOpenFOAM · OpenFOAMGPT · MooseAgent · TurboAgent · PhyNiKCE · OpenFOAM · MOOSE

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [TurboAgent: An LLM-Driven Autonomous Multi-Agent Framework for Turbomachinery Aerodynamic Design](../../docs/papers/3270_TurboAgent_An_LLM-Driven_Autonomous_Multi-Agent_Framework_fo/index.html) — 2026.04
    - 이 논문은 LLM을 중심으로 하는 자율적 다중 에이전트 프레임워크 TurboAgent를 제안하여 터보기계 공력 설계의 폐루프 자동화를 실현한다. 조건부 확산 모델, Transformer 기반 대체 모델, LLM 기반 최적화, 그리고 고충실도…
2. [Mooseagent: A llm based multi-agent framework for automating moose simulation](../../docs/papers/559_Mooseagent_A_llm_based_multi-agent_framework_for_automating/index.html) — Tao Zhang 외, 2025
    - 본 논문은 대규모 언어 모델(LLM)과 다중 에이전트 기술을 활용하여 복잡한 유한요소법(FEM) 기반 Moose 멀티피직스 시뮬레이션의 자동화를 달성한 MooseAgent 시스템을 제안한다. 자연언어 요구사항으로부터 자동으로 Moose 입력…
3. [OpenFOAMGPT 2.0: end-to-end, trustworthy automation for computational fluid dynamics](../../docs/papers/588_OpenFOAMGPT_20_end-to-end_trustworthy_automation_for_computa/index.html) — Jingsen Feng 외, 2025.04
    - 자연어 쿼리로부터 완전히 자동화된 전산유체역학(CFD) 시뮬레이션을 수행하는 첫 번째 다중 에이전트 LLM 프레임워크를 제안하며, 450개 이상의 시뮬레이션에서 100% 성공률을 달성했다.
4. [OpenFOAMGPT: A retrieval-augmented large language model (LLM) agent for OpenFOAM-based computational fluid dynamics](../../docs/papers/589_OpenFOAMGPT_A_retrieval-augmented_large_language_model_LLM_a/index.html) — Sandeep Pandey 외, 2025
    - OpenFOAMGPT는 GPT-4o와 CoT 기반 o1 preview 모델을 활용해 OpenFOAM CFD 시뮬레이션의 케이스 설정, 경계조건 수정, 난류모델 변경, 코드 변환 등을 자동화하는 RAG 기반 LLM 에이전트이다.

> [!tip] 우리에게 무엇인가
> 해석 엔지니어 한 명이 팀 규모 처리량을 갖는 구간이다. 사내 케이스 DB가 곧 해자.

---

## S36 · 다국어 사후학습·백본 적응

*제7부 · 과학 정보추출·질의응답* · **Crosslingual Post-Training Methods** · *서브카테고리*

<sub>타임라인 분석 명칭: Crosslingual Post-Training & Backbone Adaptation</sub>

`47편` `2018–2026` `가속` `2025+ 30편`

<sub>과학 정보추출·질의응답 고유 배정 221편(중복 포함 761편 · 웹 인덱스 기준) · 서브카테고리 8개 · 본 파트 5개로 76% 커버</sub>

> [!quote] 파트 도입
> 과학 도메인 언어모델이 검색·도표·주장 검증까지 확장하며 연구 무결성 인프라가 됐다.

> [!abstract] 핵심 메시지
> 2025–2026, 사후학습 기술의 무게중심이 언어에서 생물·생체신호 백본으로 옮겨갔다.

- 2026 증류·RL 메커니즘이 정교해졌다 — SEAD 엔트로피 유도 OPD, vOPD 통제변량, GRAIL 토큰 재가중 RLVR.[3][4]
- 2026 사후학습 기계가 도메인 파운데이션 모델로 이식된다(MEG-XL, NeuroCLUS, CalM, Ares, BioArc, ORA).[1][2]
- 2024–2025 오픈 프런티어 기준선이 세워졌다 — DeepSeek-V3(671B MoE, 토큰당 37B 활성), Qwen2.5, Gemma 2, Phi-4.
- 배경: 2018 BERT, 2019 XLM-R(100개 언어·2TB), 2023 Toolformer·ToolLLM의 자기지도 도구 사용.

**대표 도구·시스템** — BERT · XLM-RoBERTa · SimAlign · Toolformer · ToolLLM/ToolBench · DeepSeek-V3 · Qwen2.5 · Gemma 2 · Phi-4 · SEAD · GRAIL · MEG-XL · NeuroCLUS · Mind-Omni

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [MEG-XL: Data-Efficient Brain-to-Text via Long-Context Pre-Training](../../docs/papers/10019_MEG-XL_Data-Efficient_Brain-to-Text_via_Long-Context_Pre-Tra/index.html) — Dulhan Jayalath 외, 2026
    - MEG-XL은 2.5분(191k 토큰)의 긴 MEG 컨텍스트로 사전학습하는 프레임워크로, 기존 대비 5-300배 긴 컨텍스트를 활용해 brain-to-text word decoding에서 훨씬 적은 subject-specific 데이터로도…
2. [NeuroCLUS: A Foundation Model with Functional Clustering for Intracranial Neural Decoding](../../docs/papers/10102_NeuroCLUS_A_Foundation_Model_with_Functional_Clustering_for/index.html) — Hui Zheng 외, 2026
    - NeuroCLUS는 채널 단위 토큰화나 전체 뇌를 단일 토큰으로 압축하는 기존 방식 대신, 데이터 기반으로 학습된 기능적 클러스터(functional cluster)를 통해 두개내 신경 신호(iEEG)를 표현하는 foundation mode…
3. [GRAIL: Gradient-Reweighted Advantages for Reinforcement Learning with Verifiable Rewards](../../docs/papers/9755_GRAIL_Gradient-Reweighted_Advantages_for_Reinforcement_Learn/index.html) — Tej Deep Pala 외, 2026
    - GRAIL은 GRPO 기반 RLVR에서 시퀀스 단위로 균일하게 부여되던 advantage를 gradient-activation saliency로 토큰별로 재가중하여, 최종 답변에 실제로 기여한 토큰에 더 강한 학습 신호를 주는 방법이다. 이…
4. [SEAD: Competence-Aware On-Policy Distillation via Entropy-Guided Supervision](../../docs/papers/10399_SEAD_Competence-Aware_On-Policy_Distillation_via_Entropy-Gui/index.html) — Chia-Hsuan Lee 외, 2026
    - SEAD는 on-policy distillation(OPD)에서 teacher 지도 품질이 student의 competence에 의존한다는 구조적 문제를, teacher-student 결합 entropy를 단일 관찰량으로 활용해 token/…

> [!tip] 우리에게 무엇인가
> 한국어 과학 코퍼스 사후학습은 여전히 저비용·고효율 레버다. 백본을 새로 만들 필요는 없다.

---

## S37 · 과학 도표·시각문서 이해

*제7부 · 과학 정보추출·질의응답* · **Scientific Figure Caption Datasets** · *서브카테고리*

<sub>타임라인 분석 명칭: Scientific Figure, Diagram & Visual-Document Understanding</sub>

`45편` `2021–2026` `가속` `2025+ 29편`

> [!abstract] 핵심 메시지
> 2025–2026, 도표 이해는 '캡션 생성'에서 '무결성 검증과 도메인 통합'으로 이동했다.

- 2024–2025 대학원 수준 멀티모달 과학 벤치마크가 자리 잡았다(MMSCI, SciFIBench, MatViX, ScImage).
- 2024–2025 Figure Integrity Verification(EPM)이 도표 내 텍스트–시각 정렬을 검증한다 — 연구부정 탐지와 직결.
- 2025 Paper2Poster·MLBCAP 등 논문→발표물 자동 변환이 실무 도구로 나왔다.[1]
- 2026 의료·지리공간 통합 비전-언어 모델로 선회했다(UniMedVL, SynerMedGen, MedSIGHT, UrbanMLLM, TimeSpot).[2][4]
- 배경: 2021 SciCap이 arXiv 200만 도표–캡션 쌍을, AutomaTikZ가 DaTikZ 120k를 공개했다.

**대표 도구·시스템** — SciCap · SciCap+ · FigCaps-HF · AutomaTikZ/CLiMA · TikZero · MMSCI · SciFIBench · MatViX · Paper2Poster · MLBCAP · UniMedVL · MatDeplot

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Paper2poster: Towards multimodal poster automation from scientific papers](../../docs/papers/599_Paper2poster_Towards_multimodal_poster_automation_from_scien/index.html) — Wei Pang 외, 2025
    - 본 논문은 과학 논문을 단일 페이지 학술 포스터로 자동 변환하는 첫 번째 벤치마크와 평가 지표 집합을 제시하며, 시각적-언어적 피드백 루프를 갖춘 다중 에이전트 파이프라인(PosterAgent)을 제안한다.
2. [UniMedVL: Unifying Medical Multimodal Understanding and Generation through Observation-Knowledge-Analysis](../../docs/papers/10664_UniMedVL_Unifying_Medical_Multimodal_Understanding_and_Gener/index.html) — Junzhi Ning 외, 2026
    - UniMedVL은 의료 영상의 이해(understanding)와 생성(generation)을 하나의 모델 파라미터로 통합한 최초의 unified medical multimodal model로, Observation-Knowledge-Anal…
3. [S1-MMAlign: A Large-Scale, Multi-Disciplinary Dataset for Scientific Figure-Text Understanding](../../docs/papers/691_S1-MMAlign_A_Large-Scale_Multi-Disciplinary_Dataset_for_Scie/index.html) — He Wang 외, 2026.01
    - 과학 논문의 2.5백만 편에서 수집한 1,550만 개의 이미지-텍스트 쌍으로 구성된 대규모 멀티모달 데이터셋을 제시한다. Qwen-VL 기반 의미 강화 파이프라인을 통해 희소한 원본 캡션을 논문의 추상, 인용 맥락과 결합하여 자급식의 과학적…
4. [MedSIGHT: Towards Grounded Visual Comprehension in Medical Large Vision-Language Models](../../docs/papers/10018_MedSIGHT_Towards_Grounded_Visual_Comprehension_in_Medical_La/index.html) — Aofei Chang 외, 2026
    - MedSIGHT는 Med-LVLM에서 pixel-level 이해와 visual comprehension을 하나의 생성 프레임워크로 통합하기 위해 Region Perceiver와 modality-aware region codebook을 결합한…

> [!tip] 우리에게 무엇인가
> 그림 검증은 연구 무결성 인프라다. 학회·출판사와의 협업 지점이 여기에 있다.

---

## S38 · 자동 주장 검증

*제7부 · 과학 정보추출·질의응답* · **Automated Fact-Checking Systems** · *서브카테고리*

<sub>타임라인 분석 명칭: Automated Fact-Checking & Claim Verification</sub>

`33편` `2020–2026` `가속` `2025+ 12편`

> [!abstract] 핵심 메시지
> 2025–2026, 검증은 멀티모달·코퍼스 규모·주장 수명주기 관리로 확장됐다.

- 2025 DEFAME이 6단계 동적 파이프라인으로 텍스트+이미지 주장을 검증하고 설명 가능한 보고서를 생성한다.[1]
- 2025–2026 코퍼스 규모 주장 마이닝이 가능해졌다 — NSF-SciFy 280만 주장, SciClaimHunt 8.7만.[2][4]
- 2026 ClaimGarden 등 주장 상태 수명주기(claim lifecycle) 관리가 등장했다.[3]
- 2025 Claimify·CIBER 등 LLM 기반 주장 추출·검증 파이프라인이 정착했다.
- 배경: 2021 MultiVerS, 2022 '반박 증거 부재' 비판, 2023 ProgramFC·HiSS·FactKG.

**대표 도구·시스템** — MultiVerS · ProgramFC · FactKG · HiSS · SFAVEL · ClaimVer · DEFAME · Claimify · CIBER · SciClaimHunt · NSF-SciFy · ClaimGarden · EHR-ReasonCon

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [DEFAME: Dynamic Evidence-based Fact-checking with Multimodal Experts](../../docs/papers/267_Defame_Dynamic_evidencebased_fact-checking_with_multimodal_e/index.html) — Tobias Braun 외, 2025
    - 본 논문은 텍스트와 이미지를 모두 포함하는 클레임(주장)을 검증하는 DEFAME이라는 멀티모달 팩트체킹 시스템을 제안한다. 6단계 동적 파이프라인을 통해 외부 도구와 멀티모달 LLM을 활용하여 증거를 검색하고 평가하며, 설명 가능한 검증 보…
2. [NSF-SCIFY: Mining the NSF Awards Database for Scientific Claims](../../docs/papers/579_Nsf-scify_Mining_the_nsf_awards_database_for_scientific_clai/index.html) — D. Rao 외, 2025
    - NSF(미국 국립과학재단) 지원금 데이터베이스에서 과학적 주장(scientific claims)과 연구 제안(investigation proposals)을 대규모로 추출한 데이터셋 NSF-SCIFY를 제시한다. 1970년부터 2024년까지…
3. [ClaimGarden: Update-Aware Claim-State Control for AI Scientist Workflows](../../docs/papers/9403_ClaimGarden_Update-Aware_Claim-State_Control_for_AI_Scientis/index.html) — Hafumi Nishi, 2026
    - ClaimGarden은 AI scientist workflow에서 자동화의 단위를 project나 manuscript가 아니라 개별 claim의 상태(claim state)로 전환하여, 증거(database, literature, compu…
4. [Sciclaimhunt: A large dataset for evidence-based scientific claim verification](../../docs/papers/710_Sciclaimhunt_A_large_dataset_for_evidence-based_scientific_c/index.html) — Sujit Kumar 외, 2025
    - 본 논문은 과학 논문에서 추출한 대규모 научных 주장 검증 데이터셋 SciClaimHunt와 SciClaimHunt Num을 소개한다. 정치적 주장과 달리 과학적 주장의 검증은 도메인 전문성과 복잡한 기술 용어를 요구하는 고도의 과제이…

> [!tip] 우리에게 무엇인가
> AI 생성 과학이 늘수록 주장 단위 수명주기 추적이 필수 인프라가 된다.

---

## S39 · 생의학·임상 지식접지 QA

*제7부 · 과학 정보추출·질의응답* · **Biomedical Knowledge Graph QA** · *서브카테고리*

<sub>타임라인 분석 명칭: Biomedical & Clinical Knowledge-Grounded QA</sub>

`23편` `2023–2026` `가속` `2025+ 20편`

> [!abstract] 핵심 메시지
> 2025–2026, 임상 QA 평가가 정확도에서 다국어 신뢰성 5축으로 확장됐다.

- 2026 CLINIC이 15개 언어·18개 과제·28,800 샘플로 진실성·공정성·안전·견고성·프라이버시를 평가한다.[2]
- 2025 CLEAR가 임상 엔티티 기반 검색으로 토큰 사용을 70% 이상 줄였다 — 비용이 곧 임상 채택 조건.
- 2025 IP-RAR·BioStrataKG가 딥싱킹 LLM과 RAG를 결합해 문서 간 추론 능력을 확보했다.
- 2025–2026 ClinicalGPT-R1·LLMEval-Med·MedDocBench 등 도메인 모델과 의사 검증 평가 스위트가 나왔다.[4]
- 2026 EHR-RAGp·PACE-RAG 인구집단 사전지식과 MedREK 의료 지식 편집이 붙었다.

**대표 도구·시스템** — ClinicalGPT · BioMedLM · CLEAR · MedBioLM · LLMEval-Med · MedREK · MedDocBench · MedMosaic · EHR-RAGp · OGCaReBench · CLINIC

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [A retrieval-augmented knowledge mining method with deep thinking LLMs for biomedical research and clinical support](../../docs/papers/018_A_retrieval-augmented_knowledge_mining_method_with_deep_thin/index.html) — Yichun Feng 외, 2025 · 인용 10
    - 생의학 연구를 위해 Deep Thinking LLM과 Retrieval-Augmented Generation(RAG)을 통합한 지식 채굴 방법론을 제안하며, BioStrataKG 지식 그래프와 BioCDQA 데이터셋을 구축하고 IP-RAR…
2. [CLINIC : Evaluating Multilingual Trustworthiness in Language Models for Healthcare](../../docs/papers/9407_CLINIC__Evaluating_Multilingual_Trustworthiness_in_Language/index.html) — Akash Ghosh 외, 2026
    - CLINIC은 의료 분야 language model의 신뢰성(trustworthiness)을 truthfulness, fairness, safety, robustness, privacy 5개 축에서 15개 언어, 18개 task, 28,80…
3. [Clinical entity augmented retrieval for clinical information extraction](../../docs/papers/224_Clinical_entity_augmented_retrieval_for_clinical_information/index.html) — Iván López 외, 2025
    - 임상 노트에서 정보를 추출할 때 임상 엔티티(clinical entities)를 기반으로 관련 정보만 효율적으로 검색하여 대규모 언어모델(LLM)에 제공하는 CLEAR 파이프라인을 제안하며, 기존 embedding 기반 검색 대비 70% 이…
4. [LLMEval-Med: A Real-world Clinical Benchmark for Medical LLMs with Physician Validation](../../docs/papers/507_Llmeval-med_A_real-world_clinical_benchmark_for_medical_llms/index.html) — Ming Zhang 외, 2025
    - 본 논문은 실제 전자의무기록(EHR)과 임상 시나리오에서 도출된 2,996개 문제로 구성된 종합적 의료 LLM 평가 벤치마크 LLMEval-Med를 제시한다. 의료 전문가 검증과 동적 평가 프레임워크를 통해 의료 AI 시스템의 안전하고 효과…

> [!tip] 우리에게 무엇인가
> 한국어 임상 신뢰성 벤치마크가 없다는 건 국내 도입 심사의 근거가 없다는 뜻이다.

---

## S40 · RAG와 모호성 해소

*제7부 · 과학 정보추출·질의응답* · **Retrieval-Augmented Generation Systems** · *서브카테고리*

<sub>타임라인 분석 명칭: Retrieval-Augmented Generation & Ambiguity Resolution</sub>

`20편` `2019–2026` `안정` `2025+ 8편`

> [!abstract] 핵심 메시지
> 2025–2026, RAG의 남은 난제는 검색이 아니라 되묻기와 가설 생성이다.

- 2025 가설 생성 서베이가 프롬프팅부터 프레임워크까지 과학 가설 생성 RAG를 분류하고 평가 전략을 정리했다.
- 2025 HypoGeniC·ResearchLink가 데이터와 지식그래프 위에서 가설을 생성한다.
- 2025 STORM·SurveyX가 사전작성(pre-writing)과 속성트리로 장문 서베이 자동화를 실용화했다.[1]
- 2024 RA-LLM 종합 서베이가 아키텍처·학습 전략·응용의 3관점으로 지형을 정리했다.
- 배경: 2020 REALM, 2022 Atlas(11B가 540B 모델 상회), CLAM·LaMAI의 모호 질의 명료화.

**대표 도구·시스템** — REALM · SPLADE v2 · Atlas · CLAM · INTENT-SIM · LaMAI · STORM · SurveyX · HypoGeniC · ResearchLink · OpenTSLM

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [SurveyX: Academic survey automation via large language models](../../docs/papers/781_Surveyx_Academic_survey_automation_via_large_language_models/index.html) — Xun Liang 외, 2025
    - arXiv에 매년 증가하는 학술 논문의 폭증 속에서, 대형언어모델(LLM)을 활용하여 체계적이고 고품질의 학술 서베이를 자동 생성하는 SurveyX 시스템을 제안한다. 이 시스템은 온라인 참고문헌 검색, AttributeTree 전처리 방법…
2. [A Survey on Hypothesis Generation for Scientific Discovery in the Era of Large Language Models](../../docs/papers/031_A_Survey_on_Hypothesis_Generation_for_Scientific_Discovery_i/index.html) — Atilla Kaan Alkan 외, 2025.04 · 인용 2
    - 본 논문은 과학적 발견에서 가설 생성을 위한 Large Language Models의 활용에 관한 포괄적인 서베이로, 프롬프팅부터 복잡한 프레임워크까지의 기존 방법들을 분류하고 평가 전략 및 향후 방향을 제시한다.
3. [Enhancing chart-to-code generation in multimodal large language models via iterative dual preference learning](../../docs/papers/315_Enhancing_chart-to-code_generation_in_multimodal_large_langu/index.html) — Zhihan Zhang 외, 2025
    - 차트 이미지를 실행 가능한 플로팅 코드로 변환하는 차트-to-코드 생성 작업에서, 다중모달 대규모 언어 모델(MLLM)의 성능을 향상시키기 위해 이중 모드(code + image) 보상 메커니즘과 반복적 선호도 학습을 결합한 프레임워크를 제…
4. [OpenTSLM: Time-Series Language Models for Reasoning over Multivariate Medical Text- and Time-Series Data](../../docs/papers/10136_OpenTSLM_Time-Series_Language_Models_for_Reasoning_over_Mult/index.html) — Patrick Langer 외, 2026
    - OpenTSLM은 시계열 데이터를 LLM의 네이티브 모달리티로 통합하여, soft prompting과 cross-attention(Flamingo 방식) 두 가지 방식으로 다변량 의료 시계열(HAR, 수면 단계, ECG)에 대해 자연어 ch…

> [!tip] 우리에게 무엇인가
> 사내 RAG는 이미 상품이다. 차별화는 되묻기 정책과 인용 검증기에서 난다.

---

## S41 · 학술 메타데이터·연구 무결성 데이터

*제8부 · AI 지원 학술 커뮤니케이션* · **Academic Metadata & Causal Datasets** · *서브카테고리*

`37편` `2020–2026` `가속` `2025+ 17편`

<sub>AI 지원 학술 커뮤니케이션 고유 배정 212편(중복 포함 559편 · 웹 인덱스 기준) · 서브카테고리 15개 · 본 파트 5개로 55% 커버</sub>

> [!quote] 파트 도입
> AI 저작·심사 정책을 감정이 아니라 데이터로 설계할 근거가 쌓였다.

> [!abstract] 핵심 메시지
> 2025–2026, 학술 인프라 데이터가 AI 저작 정책의 실증 근거가 됐다.

- 2025 LLM이 생성한 연구 문서의 24%가 정교한 표절이며 내장 탐지기를 우회한다는 실증이 나왔다.
- 2024–2025 WithdrarXiv가 arXiv 철회 논문 14,000편 이상을 모아 10범주 자동 분류체계를 만들었다.
- 2025 CHIME·SurveyForge가 LLM 기반 계층적 문헌 조직화를 구현했다.[1]
- 2026 SPOT·MISSCIPLUS가 과학 오류·왜곡 검증 벤치마크를 제공한다.
- 2026 AI 과학자 자율성 거버넌스 프레임워크(CRA, SciContrib-Bench)가 제안됐다.[3]

**대표 도구·시스템** — S2ORC · ORB · ReviewArena · CHIME · SurveyForge · SPOT · WithdrarXiv · MASSW · Sibyl · CauScale

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Surveyforge: On the outline heuristics, memory-driven generation, and multi-dimensional evaluation for automated survey writing](../../docs/papers/780_Surveyforge_On_the_outline_heuristics_memory-driven_generati/index.html) — Xiangchao Yan 외, 2025
    - 본 논문은 자동화된 학술 설문지(Survey) 생성을 위한 SURVEYFORGE 프레임워크를 제안하며, 휴리스틱 기반 윤곽 생성, 메모리 기반 문헌 검색, 그리고 다차원 평가 벤치마크(SurveyBench)를 통해 AI 생성 설문과 인간 작…
2. [ReviewArena: A Large-Scale Cross-Conference Dataset and Benchmark for LLM Peer Review](../../docs/papers/10341_ReviewArena_A_Large-Scale_Cross-Conference_Dataset_and_Bench/index.html) — Samarth P 외, 2026
    - ReviewArena은 7개 OpenReview venue(NeurIPS, ICLR, ICML, CoRL, COLM, EMNLP, TMLR)에서 수집한 51,529편 논문·196,099개 review로 구성된 대규모 cross-confere…
3. [SciContrib-Bench: Mapping the Autonomy Landscape of AI Scientists Through Stage-Dependent Detectability](../../docs/papers/10386_SciContrib-Bench_Mapping_the_Autonomy_Landscape_of_AI_Scient/index.html) — Raghav Agarwal 외, 2026
    - SciContrib-Bench는 연구 파이프라인의 네 단계(hypothesis, methodology, interpretation, abstract)별로 AI 생성 과학 기여물과 인간 작성물의 구분 가능성이 어떻게 달라지는지를 stylome…
4. [Sibyl: Temporal Backtesting for Literature-Based Scientific Discovery with Large Language Model Agents](../../docs/papers/10438_Sibyl_Temporal_Backtesting_for_Literature-Based_Scientific_D/index.html) — Blagoy Rangelov, 2026
    - SIBYL은 다중 에이전트 LLM 파이프라인으로 과학 문헌을 자동으로 마이닝해 반증 가능한 예측을 생성하고, 이를 금융의 backtesting과 유사한 temporal backtesting 프레임워크로 검증하는 시스템이다. X-ray bin…

> [!tip] 우리에게 무엇인가
> AI 저작 정책은 정서가 아니라 이 데이터로 설계해야 한다.

---

## S42 · LLM 지원 동료심사

*제8부 · AI 지원 학술 커뮤니케이션* · **LLM-Assisted Peer Review Feedback** · *서브카테고리*

`34편` `2022–2026` `가속` `2025+ 18편`

> [!abstract] 핵심 메시지
> 2025–2026, 논쟁은 '허용할까'에서 '무엇을 검증하게 할까'로 넘어갔다.

- 2025 Nature 보도가 AI의 동료평가 침투와 제도 가치 훼손 우려를 동시에 정리했다.
- 2025 AgentRxiv가 공유 프리프린트 서버로 에이전트 간 발견을 누적 협업하게 만들었다.
- 2025 AAAR-1.0이 방정식 추론·실험 설계·약점 식별·리뷰 비판 4과제로 연구 보조 능력을 평가한다.[2]
- 2025 MARG·OpenReviewer·REMOR·TreeReview 등 다중 에이전트·미세조정 리뷰어가 쏟아졌다.[1]
- 2026 검증 우선 입장 논문 — AI는 논문을 심판하지 말고 주장을 검증해야 한다.

**대표 도구·시스템** — R3 · CRITIC · MARG · OpenReviewer · CycleResearcher · REMOR · TreeReview · ReviewAgents · GoodPoint · AAAR-1.0

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Remor: Automated peer review generation with llm reasoning and multi-objective reinforcement learning](../../docs/papers/665_Remor_Automated_peer_review_generation_with_llm_reasoning_an/index.html) — Pawin Taechoyotin 외, 2025
    - 본 논문은 추론(reasoning) 기능을 갖춘 대형언어모델(LLM)과 다목적 강화학습(MORL)을 결합하여 인간 수준 이상의 깊이 있고 균형잡힌 학술 논문 심사평을 자동 생성하는 REMOR 시스템을 제안한다. 기존 AI 심사평의 얕은 분석…
2. [AAAR-1.0: Assessing AI's Potential to Assist Research](../../docs/papers/041_Aaar-10_Assessing_ais_potential_to_assist_research/index.html) — Renze Lou et al., 2025
    - 본 논문은 대규모 언어모델(LLM)이 연구 작업을 얼마나 효과적으로 지원할 수 있는지 평가하기 위한 벤치마크 AAAR-1.0을 제시한다. 방정식 추론, 실험 설계, 논문 약점 식별, 리뷰 비판의 4가지 전문가급 AI 연구 작업을 통해 LLM…
3. [Position: Preventing the Collapse of Peer Review Requires Verification-First AI](../../docs/papers/10216_Position_Preventing_the_Collapse_of_Peer_Review_Requires_Ver/index.html) — Lei You 외, 2026
    - 이 논문은 AI 지원 동료 심사(peer review)가 인간 심사를 모방하는 review-mimicking 방식이 아니라, 잠재적 과학적 진실과 venue 점수 간의 정렬 정도를 뜻하는 truth-coupling을 목표로 하는 verifi…
4. [GoodPoint: Learning Constructive Scientific Paper Feedback from Author Responses](../../docs/papers/9751_GoodPoint_Learning_Constructive_Scientific_Paper_Feedback_fr/index.html) — Jimin Mun 외, 2026
    - 저자 응답(author response)에서 도출한 validity와 actionability라는 두 가지 신호를 활용해 과학 논문에 대한 건설적 피드백(constructive feedback)을 생성하도록 LLM을 훈련하고 평가하는 프레임…

> [!tip] 우리에게 무엇인가
> 기관 정책 초안에 그대로 옮길 수 있는 근거 세트다. 심사 보조는 허용, 판정은 금지.

---

## S43 · 과학 가설 재조합

*제8부 · AI 지원 학술 커뮤니케이션* · **Scientific Hypothesis Recombination** · *서브카테고리*

`19편` `2015–2026` `가속` `2025+ 13편`

> [!abstract] 핵심 메시지
> 2025–2026, 평가 기준이 '새로운가'에서 '반증 가능한가'로 이동했다.

- 2025 ResearchBench가 영감 검색·가설 구성·가설 순위로 발견 능력을 분해해 측정한다.[1]
- 2025 LLM을 진단 도구로 써서 과학·사회의 '불문율'을 명시적으로 드러내자는 제안이 나왔다.
- 2025 MOOSE-Chem·SciMuse·HypoGen 등 가설 생성 프레임워크가 확산됐다.
- 2026 NOVA-Test가 반증가능성 게이트를 건 가설 감사를 제시했다.[2]
- 2026 SciPaths·EO-Agents·PaperGym으로 발견 경로 예측과 훈련 환경화가 진행 중이다.[3][4]

**대표 도구·시스템** — SciMON · MOOSE-Chem · SciMuse · HypoGen · ResearchBench · NOVA-Test · SciPaths · EO-Agents · PaperGym

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [ResearchBench: Benchmarking LLMs in Scientific Discovery via Inspiration-Based Task Decomposition](../../docs/papers/669_Researchbench_Benchmarking_llms_in_scientific_discovery_via/index.html) — Yujie Liu 외, 2025
    - 본 논문은 과학적 발견 과정에서 LLM의 역량을 평가하기 위한 첫 번째 대규모 벤치마크 ResearchBench를 제시한다. 영감 검색(inspiration retrieval), 가설 구성(hypothesis composition), 가설…
2. [NOVA-Test: Auditing LLM-Generated Research Hypotheses with Structural Analogy, Prior-Work, and Falsifiability Tests](../../docs/papers/10114_NOVA-Test_Auditing_LLM-Generated_Research_Hypotheses_with_St/index.html) — David Scott Lewis 외, 2026
    - 이 논문은 LLM이 생성한 연구 가설(research hypothesis)을 실행 전에 검증하는 문제를 hypothesis-testing 문제로 재정의하고, structural alignment, nearest-prior novelty au…
3. [SciPaths: Forecasting Pathways to Scientific Discovery](../../docs/papers/10392_SciPaths_Forecasting_Pathways_to_Scientific_Discovery/index.html) — Eric Chamoun 외, 2026
    - SciPaths는 목표 과학적 기여를 실현하는 데 필요한 선행(enabling) 기여들을 식별하고 이를 사전 문헌(prior work)에 근거(grounding)시키는 새로운 과제인 discovery pathway forecasting을 제…
4. [EO-Agents: A Three-Agent LLM Pipeline for Earth Observation Hypothesis Generation](../../docs/papers/9588_EO-Agents_A_Three-Agent_LLM_Pipeline_for_Earth_Observation_H/index.html) — Mahyar Ghazanfari 외, 2026
    - NASA Earth Observation Knowledge Graph에 기반해, heterogeneous GNN이 데이터셋 쌍의 co-usage 가능성을 예측하고 3-agent LLM 파이프라인(filter-generate-judge)이 구…

> [!tip] 우리에게 무엇인가
> '새롭다'는 평가지표를 '검증 가능하다'로 바꾸는 것이 다음 단계다.

---

## S44 · 그래프 기반 과학 요약

*제8부 · AI 지원 학술 커뮤니케이션* · **Graph-Based Scientific Summarization** · *서브카테고리*

`15편` `2019–2026` `안정` `2025+ 3편`

> [!abstract] 핵심 메시지
> 2025–2026, 요약의 쟁점은 압축률이 아니라 과잉 일반화다.

- 2025 일반화 편향 감사: 10개 LLM·4,900개 요약에서 인간 대비 결론 과잉 확장이 확인됐다.
- 2025 GLIMPSE·CGI2 등 메타리뷰 요약으로 심사 문서까지 대상이 확대됐다.
- 2023–2025 SciReviewGen(리뷰 1만 편·인용논문 69만)이 문헌리뷰 자동생성 학습 기반을 제공한다.[4]
- 2026 HAESum·MoDeST 등 계층 구조를 활용한 요약 모델이 이어진다.[1]
- 배경: 2020 SciTLDR의 극단 요약과 CATTS 학습 전략.

**대표 도구·시스템** — SciTLDR/CATTS · MS2 · KGSum · SciReviewGen · HAESum · GLIMPSE · XSum · MoDeST

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [MoDeST: A dataset for Multi Domain Scientific Title Generation](../../docs/papers/10765_modest_a_dataset_for_multi_domain_scientific_title_gen/index.html) — Necva Bölücü 외, 2025.05
    - MoDeST는 영어와 터키어, 다양한 학문 분야(사회과학, 의학, 공학 등)를 아우르는 최초의 multi-domain, multilingual 과학 논문 title generation 데이터셋으로, keywords·abstract·full…
2. [Generalization Bias in Large Language Model Summarization of Scientific Research](../../docs/papers/373_Generalization_Bias_in_Large_Language_Model_Summarization_of/index.html) — Uwe Peters 외, 2025.03
    - 대규모 언어모델(LLM)이 과학 연구를 요약할 때 원문보다 과도하게 광범위한 결론을 도출하는 체계적인 편향을 가지고 있으며, 이는 대규모 과학 오독의 위험을 초래한다. 10개의 주요 LLM을 대상으로 4,900개의 요약을 분석한 결과, LL…
3. [Ask, retrieve, summarize: A modular pipeline for scientific literature summarization](../../docs/papers/108_Ask_retrieve_summarize_A_modular_pipeline_for_scientific_lit/index.html) — Pierre Achkar 외, 2025
    - 과학 문헌의 지수적 증가 문제를 해결하기 위해, 검색-증강-생성(RAG) 기반의 모듈식 다중문서 요약(MDS) 파이프라인인 XSum을 제안한다. 질문 생성 모듈과 편집 모듈의 두 가지 혁신적 컴포넌트를 통해 정확하고 인용이 풍부한 과학 문헌…
4. [SciReviewGen: a large-scale dataset for automatic literature review generation](../../docs/papers/732_Scireviewgen_a_large-scale_dataset_for_automatic_literature/index.html) — Tetsu Kasanishi 외, 2023
    - 본 논문은 자동 문헌 리뷰 생성을 위한 최초의 대규모 데이터셋인 SciReviewGen을 제시한다. 10,000개 이상의 문헌 리뷰와 690,000개의 인용 논문으로 구성되어 있으며, 쿼리 기반 다중 문서 요약(query-focused mu…

> [!tip] 우리에게 무엇인가
> 요약 자동화를 도입하려면 '결론 범위 확장' 감지기를 함께 넣어야 한다.

---

## S45 · 인용 문맥 추천·검증

*제8부 · AI 지원 학술 커뮤니케이션* · **Citation Context Recommendation** · *서브카테고리*

`12편` `2022–2026` `안정` `2025+ 5편`

> [!abstract] 핵심 메시지
> 2025–2026, 인용 생성이 쉬워진 만큼 인용 환각 탐지가 본론이 됐다.

- 2025 ScholarCopilot이 검색을 글쓰기에 통합해 인용과 문장을 함께 생성한다.[3]
- 2025 SciRGC가 인용 의도 인식과 인용 네트워크로 다단계 추천·문장 정렬을 구현했다.[2]
- 2026 CiteCheck이 LLM 인용 환각을 탐지하고, MIRAI가 인용 영향력을 예측한다.[1][4]
- 2024 CiteBART가 인용 토큰 마스킹 사전학습으로 로컬 인용 추천을 생성형으로 전환했다.
- 배경: 2022 RL 기반 제어 가능 인용문 생성, 2023 Cited Text Span 접지.

**대표 도구·시스템** — CiteBART · ILCiteR · HiGTL · SciRGC · ScholarCopilot · CiteCheck · MIRAI

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [CiteCheck: Retrieval-Grounded Detection of LLM Citation Hallucinations in Scientific Text](../../docs/papers/3378_CiteCheck_Retrieval-Grounded_Detection_of_LLM_Citation_Hallu/index.html) — Khashayar Khajavi 외, 2026.05
    - LLM이 생성한 과학 문헌의 인용 오류를 탐지하기 위해 학술 검색, 구조화된 LLM 기반 비교, 그리고 임계값 기반 의사결정을 결합한 하이브리드 프레임워크 CiteCheck를 제시한다. 982개의 제어된 부패 물리학 인용 벤치마크에서 88.…
2. [Scirgc: Multi-granularity citation recommendation and citation sentence preference alignment](../../docs/papers/1091_Scirgc_Multi-granularity_citation_recommendation_and_citatio/index.html) — Xi Chen 외, 2025
    - SciRGC 프레임워크는 인용 의도(citation intent) 인식과 인용 네트워크를 활용하여 학술 논문의 적절한 인용 문헌을 추천하고 고품질의 인용 문장을 생성하는 다단계 시스템을 제안한다.
3. [ScholarCopilot: Training Large Language Models for Academic Writing with Accurate Citations](../../docs/papers/702_Scholarcopilot_Training_large_language_models_for_academic_w/index.html) — Yubo Wang 외, 2025
    - 학술 논문 작성을 위해 생성 과정과 인용 검색을 통합한 대규모 언어모델 프레임워크를 제시한다. 동적 검색 토큰 생성을 통해 필요한 시점에 정확한 학술 참고문헌을 검색하고 인용 정확도를 대폭 향상시킨다.
4. [MIRAI: Prediction and Generation of High-Impact Academic Research](../../docs/papers/3388_MIRAI_Prediction_and_Generation_of_High-Impact_Academic_Rese/index.html) — Alex Li 외, 2026.06
    - MIRAI는 논문의 제목, 초록, 출판 날짜만을 사용하여 deep learning framework로 5년 후 논문 영향력을 예측하는 프레임워크이다. arXiv 학술 그래프에서 PageRank와 citation counts를 예측하며, 20…

> [!tip] 우리에게 무엇인가
> 글쓰기 도구에 인용 검증기를 기본 탑재하지 않으면 그대로 기관 리스크가 된다.

---

## S46 · 수렴 신호: 경계가 무너지는 곳

*종합* · **Convergence signals** · *종합*

> [!abstract] 핵심 메시지
> 서로 다른 카테고리가 같은 문제를 풀기 시작하면, 그 지점이 다음 3년의 표준이 된다.

- **에이전트-실험실 통합** (과학 자동화 에이전트 AI × AI 기반 신약·신소재 발견) — LLM 기반 다중 에이전트 시스템과 자율 실험실(SDL) 로봇공학이 급속히 통합되고 있다. A-Lab, AMASE, SAMPLE, ChemAgents 등은 가설 생성부터 실험 실행, 결과 해석까지 폐루프를 구현하며, 이는 '에이전트형 AI'와 '약물·재료 발견' 범주의 경계를 허물고 있다.
- **물리정보 신경망 범용화** (형식 방법론·계산 추론 × 분자 시뮬레이션·생성 모델링 × 물리·환경 과학 AI) — PINNs와 신경 연산자(Neural Operators)가 전자기학, 유체역학, 기후, 양자계 등 다양한 물리 도메인에서 동시에 채택되며 범용 과학 계산 프레임워크로 수렴하고 있다. 형식적 추론 범주와 분자 시뮬레이션 범주 모두에서 PINNs 관련 논문이 급증하고 있다.
- **기초모델과 정보추출 통합** (과학 정보추출·질의응답 × AI 지원 학술 커뮤니케이션) — SciBERT, BioBERT에서 출발한 과학 도메인 언어 모델이 이제 멀티모달 검색·인용·차트 이해·동료 검토 지원으로 확장되며 과학 정보추출과 학술 커뮤니케이션 범주가 수렴하고 있다. OpenScholar, ChartGemma, HLM-Cite 등은 검색에서 생성까지 일관된 파이프라인을 구현한다.

**정책 함의**

- 자율 실험실 인프라에 대한 국가 R&D 투자 및 안전·데이터 무결성 표준 수립이 시급하다.
- 물리 정보 통합 AI 솔버의 재현성 및 검증 표준을 마련하여 산업 적용을 가속화해야 한다.
- 과학 출판 인프라에 AI 기반 정보추출·합성 도구를 표준 통합하기 위한 오픈액세스 및 데이터 공유 정책이 필요하다.

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Agentic LLM Reasoning in a Self-Driving Laboratory for Air-Sensitive Lithium Halide Spinel Conductors](../../docs/papers/3011_Agentic_LLM_Reasoning_in_a_Self-Driving_Laboratory_for_Air-S/index.html) — Yuxing Fei 외, 2026.04
    - 본 논문은 공기 차단 환경에서 작동하는 자동화 로봇 합성 플랫폼 A-Lab GPSS에 LLM 기반 에이전트의 추론 능력을 통합하여, 공기에 민감한 리튬 할라이드 스피넬 이온 전도체의 자율 발견을 실증했다. Abductive reasoning…
2. [Agentic workflow enables the recovery of critical materials from complex feedstocks via selective precipitation](../../docs/papers/3012_Agentic_workflow_enables_the_recovery_of_critical_materials/index.html) — 2026.03
    - Multi-agentic LLM과 자율 실험 장비를 결합한 CICERO 워크플로우를 통해 산업 폐기물에서 선택적 침전법으로 핵심 소재를 회수하는 과정을 수개월에서 수일로 단축했다.
3. [Bridging decision-making engines and workflow design in self-driving laboratories: A NIMO-IvoryOS integration study](../../docs/papers/3048_Bridging_decision-making_engines_and_workflow_design_in_self/index.html) — 2026.03
    - 본 논문은 AI 의사결정 엔진 NIMO와 파이썬 기반 오케스트레이터 IvoryOS를 통합하여 자율 실험실(Self-driving laboratories, SDLs) 개발의 진입장벽을 낮추는 프레임워크를 제시한다. 커피링 효과 자동화 연구를…
4. [On the Role of Consistency Between Physics and Data in Physics-Informed Neural Networks](../../docs/papers/3195_On_the_Role_of_Consistency_Between_Physics_and_Data_in_Physi/index.html) — 2026.02
    - PINN 학습 과정에서 데이터와 PDE 간의 불일치가 도달 가능한 정확도의 하한을 결정하는 'consistency barrier'를 1D Burgers 방정식을 통해 형식화하고, 고충실도 데이터 사용 시 이 장벽을 제거할 수 있음을 입증.
5. [Stochastic Dimension-Free Zeroth-Order Estimator for High-Dimensional and High-Order PINNs](../../docs/papers/3246_Stochastic_Dimension-Free_Zeroth-Order_Estimator_for_High-Di/index.html) — 2026.03
    - 본 논문은 고차원·고차 편미분방정식을 풀기 위한 Physics-Informed Neural Networks (PINNs)의 확장성 문제를 해결하기 위해 역전파 없이 작동하는 Stochastic Dimension-free Zeroth-orde…

> [!tip] 우리에게 무엇인가
> 세 수렴 모두 '인프라 + 표준'을 요구한다. 개별 모델 도입으로는 따라갈 수 없는 층이다.

---

## S47 · 부상과 쇠퇴

*종합* · **What is rising, what is fading** · *종합*

> [!abstract] 핵심 메시지
> 단독 LLM으로 과학하겠다는 접근은 접히는 중이고, 그 자리를 신경-기호와 추론시간 확장이 채운다.

- **부상 —**
- **신경-기호 과학 발견** (형식 방법론·계산 추론 × AI 기반 신약·신소재 발견 × 과학 자동화 에이전트 AI) — LLM의 생성 능력과 형식 논리·기호 규칙을 결합한 뉴로심볼릭 접근이 역합성, 정리 증명, CFD 자동화 등에서 빠르게 부상하고 있다. Protect*, PhyNiKCE, EffieDes, MerLean 등은 LLM 단독 방식의 한계인 물리적 타당성 부족을 기호 제약으로 보완한다.
- **추론 시간 확장 전략** (LLM·에이전트 평가 × 형식 방법론·계산 추론) — DeepSeek-R1, o1 계열 모델의 성공으로 학습 시간 스케일링 대신 추론 시간 계산 투자(Chain-of-Thought, 강화학습 자기검증)가 과학 추론과 벤치마크 성능을 획기적으로 향상시키는 전략으로 부상하고 있다. LLM 벤치마킹과 형식 추론 범주 모두에서 이 접근의 채택이 가속화되고 있다.
- **쇠퇴 —**
- **단독 LLM 과학 발견 한계** (과학 자동화 에이전트 AI × AI 기반 신약·신소재 발견 × LLM·에이전트 평가) — 외부 도구·검증·실험 피드백 없이 LLM 단독으로 과학 가설을 생성하고 검증하는 접근은 구현 능력 부재, 환각, 자기수정 실패 등으로 신뢰를 잃고 있다. 최신 연구들은 일관되게 멀티에이전트·도구통합·폐루프 시스템으로 전환하고 있으며, 순수 LLM 기반 과학 발견 논문 비중은 감소 추세다.

**정책 함의**

- 뉴로심볼릭 AI의 검증 가능성과 해석 가능성을 규제 요건으로 명시하여 안전-임계 과학 분야 적용을 촉진해야 한다.
- 추론 시간 스케일링 기법의 에너지 효율성 및 비용 대비 성능 지표를 표준 벤치마크에 포함해야 한다.
- LLM 기반 과학 연구 도구 도입 시 독립 검증 메커니즘 포함을 의무화하는 가이드라인을 제정해야 한다.

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Protect*: Steerable Retrosynthesis through Neuro-Symbolic State Encoding](../../docs/papers/3219_Protect_Steerable_Retrosynthesis_through_Neuro-Symbolic_Stat/index.html) — 2026.02
    - Protect*는 LLM의 생성 능력을 55+ SMARTS 규칙과 40+ 보호기 패턴의 기호 논리로 접지시켜 분자의 특정 반응 위치를 자동으로 보호하고 역합성 경로를 안내하는 신경-기호 프레임워크이다.
2. [PhyNiKCE: A Neurosymbolic Agentic Framework for Autonomous Computational Fluid Dynamics](../../docs/papers/3206_PhyNiKCE_A_Neurosymbolic_Agentic_Framework_for_Autonomous_Co/index.html) — 2026.02
    - PhyNiKCE는 LLM 기반 에이전트와 Symbolic Knowledge Engine을 결합한 neurosymbolic 프레임워크로, CFD 시뮬레이션 설정을 Constraint Satisfaction Problem으로 취급하여 물리적 제…
3. [A Generative Neuro-Symbolic AI for Protein Sequence Design](../../docs/papers/2990_A_Generative_Neuro-Symbolic_AI_for_Protein_Sequence_Design/index.html) — 2026.04
    - 자기회귀 샘플링의 "look-ahead" 부족 문제를 해결하기 위해, 신경망으로 fitness landscape을 Potts model로 인코딩한 후 자동 추론 solver로 최적화하는 neuro-symbolic 프레임워크 EffieDes를…
4. [MerLean: An Agentic Framework for Autoformalization in Quantum Computation](../../docs/papers/532_MerLean_An_Agentic_Framework_for_Autoformalization_in_Quantu/index.html) — Yuanjie Ren 외, 2026.02
    - 본 논문은 양자계산 이론 논문을 자동으로 기계검증 가능한 Lean 4 코드로 변환하는 완전 자동화 에이전트 프레임워크 MerLean을 제시한다. 3개 양자계산 논문에서 114개 명제로부터 2,050개 Lean 선언을 생성하며 전체 논문의 자…
5. [SEVerA: Verified Synthesis of Self-Evolving Agents](../../docs/papers/750_SEVerA_Verified_Synthesis_of_Self-Evolving_Agents/index.html) — Debangshu Banerjee 외, 2026.03
    - 자기 진화하는 LLM 에이전트의 합성에 형식적 안전성 보증을 제공하는 프레임워크이다. FGGM(Formally Guarded Generative Models)을 통해 각 모델 호출에 형식적 계약을 지정하고, 검증-학습 단계를 분리하여 제약…

> [!tip] 우리에게 무엇인가
> 쇠퇴 신호를 읽는 쪽이 더 돈이 된다. '순수 LLM 과학 발견' 과제는 지금 시작하면 늦다.

---

## S48 · 비어 있는 자리

*종합* · **Gaps and underserved domains** · *종합*

> [!abstract] 핵심 메시지
> 가장 큰 공백은 기술이 아니다 — AI가 만든 과학을 검증할 체계가 없다.

- **AI 생성 과학의 검증 부재** (AI 지원 학술 커뮤니케이션 × 과학 자동화 에이전트 AI × AI 기반 신약·신소재 발견) — AI가 자율 생성한 가설·논문·실험 결과에 대한 체계적 재현성 검증 및 감사 프레임워크가 부재하다. 데이터 무결성 위협(AI 생성 현미경 이미지 등)과 동료 검토 시스템의 LLM 취약성이 지적되지만, 이를 근본적으로 해결하는 검증 인프라 연구는 극히 드물다.
- **미개척 영역** — AI 생성 과학 콘텐츠의 장기 학문적 영향 및 지식재산권 귀속 연구
- **미개척 영역** — 자율 실험실의 실험실-임상 전환율 및 born-qualified 제조 가능성 통합
- **미개척 영역** — AI 에이전트 시스템의 장기 일관성 및 분포 외 신뢰성 표준 벤치마크
- **미개척 영역** — 저소득 국가 및 자원 제약 환경에서의 AI4Science 접근성 및 형평성
- **미개척 영역** — AI 기반 기후·기상 모델의 극단 이벤트 외삽 신뢰성 독립 검증

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Data integrity in materials science in the era of AI: balancing accelerated discovery with responsible science and innovation](../../docs/papers/252_Data_integrity_in_materials_science_in_the_era_of_AI_balanci/index.html) — Nik Reeves-McLaren 외, 2026
    - AI의 급속한 발전으로 재료 과학의 데이터 무결성이 심각한 위협에 직면해 있으며, 전문가조차 AI 생성 현미경 이미지를 실제 데이터와 구별하지 못하고 있다. 이 논문은 책임감 있는 과학 실천을 위한 다층적 연구 무결성 프레임워크를 제안한다.
2. [Lazyreview a dataset for uncovering lazy thinking in nlp peer reviews](../../docs/papers/481_Lazyreview_a_dataset_for_uncovering_lazy_thinking_in_nlp_pee/index.html) — Sukannya Purkayastha 외, 2025
    - NLP 동료 검토(peer review) 과정에서 발견되는 "게으른 사고(lazy thinking)" 를 자동으로 탐지하기 위한 첫 번째 주석 데이터셋 LAZYREVIEW를 제시한다. 500개의 전문가 주석 검토 세그먼트와 1,276개의 자…
3. [Detecting LLM-written Peer Reviews](../../docs/papers/270_Detecting_llm-written_peer_reviews/index.html) — Vishisht Rao 외, 2025
    - LLM을 이용해 작성된 peer review를 탐지하기 위해, 논문 PDF에 indirect prompt injection을 통한 covert watermark 삽입 기법과 이를 통계적으로 검증하는 FWER-controlling hypoth…
4. [AI Scientists Fail Without Strong Implementation Capability](../../docs/papers/081_Ai_scientists_fail_without_strong_implementation_capability/index.html) — Min Zhu 외, 2025
    - 이 position paper는 AI Scientist 시스템의 근본적 병목이 아이디어 생성 능력이 아니라 실험 검증을 위한 구현(implementation) 능력에 있다고 주장하며, 벤치마크 정량 증거와 28편의 AI Scientist 생…
5. [All that glitters is not novel: Plagiarism in ai generated research](../../docs/papers/093_All_that_glitters_is_not_novel_Plagiarism_in_ai_generated_re/index.html) — Tarun Gupta 외, 2025
    - 최근 자동화된 연구 에이전트가 혁신적인 연구 아이디어를 생성할 수 있다고 주장되고 있으나, 본 논문은 LLM이 생성한 연구 문서의 24%가 기존 논문으로부터 정교하게 표절되었음을 입증한다. 특히 이러한 표절이 내장된 표절 탐지 시스템을 우회…

> [!tip] 우리에게 무엇인가
> 공백은 곧 진입 지점이다. 검증·감사·형평성 영역은 후발 주자가 표준을 선점할 수 있는 몇 안 되는 자리.

---

## S49 · 2026 검증 전환의 여섯 축

*종합* · **Six axes of the verification turn** · *종합*

> [!abstract] 핵심 메시지
> 같은 해에, 서로 모르는 여덟 개 분야가 같은 결론에 도달했다 — 성능이 아니라 증거.

- **벤치마크 감사** — ProtDBench·GENEB·ProofGate·Ground False: 벤치마크 자체의 결함을 검사한다 (S07·S08·S31).
- **실패 모드 진단** — PINN 기울기 병리·consistency barrier, A-Lab 신물질 주장 재분석 (S16·S24).
- **기계적 해석성** — 희소 오토인코더, cross-layer transcoder, AlphaInterp (S06·S09).
- **통계적 인증** — 예측기반 추론(PPI), conformal 유효성, knockoff 귀인, 등가 검정 (S14·S18).
- **출처·기여 추적** — WithdrarXiv·CreditMap·DataJoint 계열 프로비넌스 인프라 (S41).
- **검증 우선 규범** — 'AI는 논문을 심판하지 말고 주장을 검증하라', 반증가능성 게이트 NOVA-Test (S42·S43).

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [ProtDBench: A Unified Benchmark of Protein Binder Design and Evaluation](../../docs/papers/10261_ProtDBench_A_Unified_Benchmark_of_Protein_Binder_Design_and/index.html) — Cong Liu 외, 2026
    - ProtDBench는 de novo protein binder design 평가를 위한 표준화되고 throughput을 고려한 통합 벤치마크 프레임워크로, wet-lab annotated dataset을 활용해 structure predic…
2. [ProofGate: A Reproducible Audit of Faithfulness, Alignment, and Vacuity in State-of-the-Art Lean Theorem Provers](../../docs/papers/10257_ProofGate_A_Reproducible_Audit_of_Faithfulness_Alignment_and/index.html) — Edison Yang 외, 2026
    - 최근 SOTA neural theorem prover들이 miniF2F, PutnamBench에서 보고하는 높은 pass rate가 사실은 proof faithfulness, statement alignment, problem vacuity…
3. [AlphaInterp: Probing AlphaFold 3's Internal Representations Reveals Evolutionary Determinants of Predicted Structure and Confidence](../../docs/papers/3020_AlphaInterp_Probing_AlphaFold_3s_Internal_Representations_Re/index.html) — 2026.04
    - AlphaFold 3의 내부 표현을 체계적으로 분석하여 단백질 구조 예측이 주로 진화적 맥락에 의존하며, MSA를 통해 구조적으로 제약된 위치를 식별하고 가중치에 저장된 구조 prior를 활성화하는 민감한 fold recognition 알고…
4. [Withdrarxiv: A large-scale dataset for retraction study](../../docs/papers/885_Withdrarxiv_A_large-scale_dataset_for_retraction_study/index.html) — Delip Rao 외, 2024
    - 본 논문은 arXiv 플랫폼에서 철회된 14,000개 이상의 논문을 수집한 첫 대규모 철회 연구 데이터셋(WithdrawArXiv)을 제시하며, 철회 이유를 10가지 범주로 분류하는 자동 분류 체계를 개발했다.
5. [NOVA-Test: Auditing LLM-Generated Research Hypotheses with Structural Analogy, Prior-Work, and Falsifiability Tests](../../docs/papers/10114_NOVA-Test_Auditing_LLM-Generated_Research_Hypotheses_with_St/index.html) — David Scott Lewis 외, 2026
    - 이 논문은 LLM이 생성한 연구 가설(research hypothesis)을 실행 전에 검증하는 문제를 hypothesis-testing 문제로 재정의하고, structural alignment, nearest-prior novelty au…
6. [GENEB: Why Genomic Models Are Hard to Compare](../../docs/papers/9719_GENEB_Why_Genomic_Models_Are_Hard_to_Compare/index.html) — Daria Ledneva 외, 2026
    - GENEB는 40개 genomic foundation model을 100개 태스크(13개 기능 범주)에 걸쳐 통일된 probing 기반 프로토콜로 평가하는 대규모 진단형 벤치마크로, 모델 간 직접 비교가 불가능했던 기존 평가 관행의 파편화…

> [!tip] 우리에게 무엇인가
> 이 여섯 축은 그대로 조직의 체크리스트가 된다. 도입 검토서 양식으로 바로 옮길 수 있다.

---

## S50 · 그래서 무엇을 할 것인가

*종합* · **Where to stand** · *마무리*

> [!abstract] 핵심 메시지
> 따라잡기 경쟁은 이미 졌다. 이길 수 있는 자리는 검증·도메인 데이터·대형시설이다.

- **검증 인프라를 산다** — 모델 도입 예산의 일정 비율을 독립 재현·감사에 고정 배정한다(근거: S24 A-Lab 재분석, S27 증거 무시 68%).
- **도메인 데이터가 해자다** — 섭동 스크린(S06), DFT 계산(S22), 사내 CFD 케이스(S35), 임상 노트(S28). 백본은 사 오고 데이터로 이긴다.
- **대형시설이 가장 빠른 적용처다** — 방사광·중성자·핵융합 장비 에이전트(S29)는 국내 즉시 실행 가능.
- **한국어·한국 도메인 벤치마크 부재를 메운다** — 없으면 도입 심사 근거 자체가 없다(S10·S39).
- **정책 문서는 이미 근거가 충분하다** — 심사 보조 허용·판정 금지, 인용 검증기 의무화(S42·S45).

**관전 포인트 (다음 12개월)**

- 자율 에이전트의 습식 검증 성공률이 공개 벤치마크에서 재현되는가
- 형식 검증기가 수학 밖(재료·코드·회로)으로 얼마나 확장되는가
- AI 수치예보의 극단 이벤트 외삽에 대한 독립 검증 결과
- AI 생성 논문·리뷰에 대한 학회·출판사 표준의 성립 여부

> [!tip] 우리에게 무엇인가
> 이 덱의 근거는 전부 코퍼스에 있다. 각 슬라이드 레퍼런스에서 논문 리뷰 원문으로 바로 내려갈 수 있다.

---

## 부록 · 전체 레퍼런스 176편

- [(Sparse) Attention to the Details: Preserving Spectral Fidelity in ML-based Weather Forecasting Models](../../docs/papers/10472_Sparse_Attention_to_the_Details_Preserving_Spectral_Fidelity/index.html) — Maksim Zhdanov 외, 2026
- [A Generative Neuro-Symbolic AI for Protein Sequence Design](../../docs/papers/2990_A_Generative_Neuro-Symbolic_AI_for_Protein_Sequence_Design/index.html) — 2026.04
- [A recipe for scalable attention-based ML potentials: unlocking long-range accuracy with all-to-all node attention](../../docs/papers/9159_A_recipe_for_scalable_attention-based_ML_potentials_unlockin/index.html) — Eric Qu 외, 2026
- [AI scientists produce results without reasoning scientifically](../../docs/papers/9108_ai_scientists_produce_results_without_reasoning_scienti/index.html) — Martiño Ríos-García 외, 2026
- [AetherCell: A generative engine for virtual cell perturbation and in vivo drug discovery](../../docs/papers/3008_AetherCell_A_generative_engine_for_virtual_cell_perturbation/index.html) — 2026.03
- [Agentic LLM Reasoning in a Self-Driving Laboratory for Air-Sensitive Lithium Halide Spinel Conductors](../../docs/papers/3011_Agentic_LLM_Reasoning_in_a_Self-Driving_Laboratory_for_Air-S/index.html) — Yuxing Fei 외, 2026.04
- [Agentic Separation Logic Specification Synthesis](../../docs/papers/9211_Agentic_Separation_Logic_Specification_Synthesis/index.html) — Tarun Suresh 외, 2026
- [Agentic workflow enables the recovery of critical materials from complex feedstocks via selective precipitation](../../docs/papers/3012_Agentic_workflow_enables_the_recovery_of_critical_materials/index.html) — 2026.03
- [AlphaFold Database expands to proteome-scale quaternary structures](../../docs/papers/3019_AlphaFold_Database_expands_to_proteome-scale_quaternary_stru/index.html) — 2026.03
- [AlphaInterp: Probing AlphaFold 3's Internal Representations Reveals Evolutionary Determinants of Predicted Structure and Confidence](../../docs/papers/3020_AlphaInterp_Probing_AlphaFold_3s_Internal_Representations_Re/index.html) — 2026.04
- [AutoNumerics-Zero: Automated Discovery of State-of-the-Art Mathematical Functions](../../docs/papers/9282_AutoNumerics-Zero_Automated_Discovery_of_State-of-the-Art_Ma/index.html) — Esteban Real 외, 2026
- [AutoNumerics: An Autonomous, PDE-Agnostic Multi-Agent Pipeline for Scientific Computing](../../docs/papers/142_AutoNumerics_An_Autonomous_PDE-Agnostic_Multi-Agent_Pipeline/index.html) — Jianda Du 외, 2026.02
- [Autoregressive Boltzmann Generators](../../docs/papers/9283_Autoregressive_Boltzmann_Generators/index.html) — Danyal Rehman 외, 2026
- [Benchmarking Physics-Informed Time-Series Models for Operational Global Station Weather Forecasting](../../docs/papers/9302_Benchmarking_Physics-Informed_Time-Series_Models_for_Operati/index.html) — Tao Han 외, 2026
- [Bridging decision-making engines and workflow design in self-driving laboratories: A NIMO-IvoryOS integration study](../../docs/papers/3048_Bridging_decision-making_engines_and_workflow_design_in_self/index.html) — 2026.03
- [BuildArena: A Physics-Aligned Interactive Benchmark of LLMs for Engineering Construction](../../docs/papers/9361_BuildArena_A_Physics-Aligned_Interactive_Benchmark_of_LLMs_f/index.html) — Tian Xia 외, 2026
- [CADEngBench: Can AI Systems Co-Author Engineering Designs? A Hierarchical Benchmark for Physics-Verified Parametric CAD Generation](../../docs/papers/9362_CADEngBench_Can_AI_Systems_Co-Author_Engineering_Designs_A_H/index.html) — Harmanjot Singh 외, 2026
- [CAGenMol: Condition-Aware Diffusion Language Model for Goal-Directed Molecular Generation](../../docs/papers/3050_CAGenMol_Condition-Aware_Diffusion_Language_Model_for_Goal-D/index.html) — 2026.04
- [CELEUS: Certifiable and Efficient LLM Evaluation via E-Processes](../../docs/papers/9386_CELEUS_Certifiable_and_Efficient_LLM_Evaluation_via_E-Proces/index.html) — Zhijian Zhou 외, 2026
- [CLAMP: A Mechanistic Probe of Regulatory Structure in Foundation Models under Single-Cell Perturbations](../../docs/papers/9404_CLAMP_A_Mechanistic_Probe_of_Regulatory_Structure_in_Foundat/index.html) — Amaya Gallagher-Syed 외, 2026
- [CLINIC : Evaluating Multilingual Trustworthiness in Language Models for Healthcare](../../docs/papers/9407_CLINIC__Evaluating_Multilingual_Trustworthiness_in_Language/index.html) — Akash Ghosh 외, 2026
- [CatFlow: Co-generation of Slab-Adsorbate Systems via Flow Matching](../../docs/papers/9378_CatFlow_Co-generation_of_Slab-Adsorbate_Systems_via_Flow_Mat/index.html) — Minkyu Kim 외, 2026
- [CiteCheck: Retrieval-Grounded Detection of LLM Citation Hallucinations in Scientific Text](../../docs/papers/3378_CiteCheck_Retrieval-Grounded_Detection_of_LLM_Citation_Hallu/index.html) — Khashayar Khajavi 외, 2026.05
- [ClaimGarden: Update-Aware Claim-State Control for AI Scientist Workflows](../../docs/papers/9403_ClaimGarden_Update-Aware_Claim-State_Control_for_AI_Scientis/index.html) — Hafumi Nishi, 2026
- [ClimateAR: Multi-Scale Autoregressive Generative Modeling for Climate Forecasting](../../docs/papers/9406_ClimateAR_Multi-Scale_Autoregressive_Generative_Modeling_for/index.html) — Yue Yu 외, 2026
- [Data integrity in materials science in the era of AI: balancing accelerated discovery with responsible science and innovation](../../docs/papers/252_Data_integrity_in_materials_science_in_the_era_of_AI_balanci/index.html) — Nik Reeves-McLaren 외, 2026
- [DiffSyn: a generative diffusion approach to materials synthesis planning](../../docs/papers/3077_DiffSyn_a_generative_diffusion_approach_to_materials_synthes/index.html) — Elton Pan 외, 2026.02
- [Distinguishing Imitation Error from Intrinsic Motion Learning Difficulty](../../docs/papers/9528_Distinguishing_Imitation_Error_from_Intrinsic_Motion_Learnin/index.html) — Zhaorui Meng 외, 2026
- [Do Larger Models Really Win in Drug Discovery? A Benchmark Assessment of Model Scaling in AI-Driven Molecular Property and Activity Prediction](../../docs/papers/3078_Do_Larger_Models_Really_Win_in_Drug_Discovery_A_Benchmark_As/index.html) — Jinjiang Guo, 2026.04
- [EEG-FM-Bench: A Comprehensive Benchmark for the Systematic Evaluation and Diagnostic Analyses of EEG Foundation Models](../../docs/papers/9563_EEG-FM-Bench_A_Comprehensive_Benchmark_for_the_Systematic_Ev/index.html) — Wei Xiong 외, 2026
- [EO-Agents: A Three-Agent LLM Pipeline for Earth Observation Hypothesis Generation](../../docs/papers/9588_EO-Agents_A_Three-Agent_LLM_Pipeline_for_Earth_Observation_H/index.html) — Mahyar Ghazanfari 외, 2026
- [EduMirror: Modeling Educational Social Dynamics with Value-driven Multi-agent Simulation](../../docs/papers/9561_EduMirror_Modeling_Educational_Social_Dynamics_with_Value-dr/index.html) — Jingzhe Lin 외, 2026
- [Embodied Science: Closing the Discovery Loop with Agentic Embodied AI](../../docs/papers/310_Embodied_Science_Closing_the_Discovery_Loop_with_Agentic_Emb/index.html) — Xiang Zhuang 외, 2026.03
- [Extending the range of graph neural networks with global encodings](../../docs/papers/3095_Extending_the_range_of_graph_neural_networks_with_global_enc/index.html) — Alessandro Caruso 외, 2026.02
- [FlashSchNet: Fast and Accurate Coarse-Grained Neural Network Molecular Dynamics](../../docs/papers/3102_FlashSchNet_Fast_and_Accurate_Coarse-Grained_Neural_Network/index.html) — 2026.02
- [GENEB: Why Genomic Models Are Hard to Compare](../../docs/papers/9719_GENEB_Why_Genomic_Models_Are_Hard_to_Compare/index.html) — Daria Ledneva 외, 2026
- [GFFMERGE: Efficient Merging of Graph Neural Force Fields and Beyond](../../docs/papers/9746_GFFMERGE_Efficient_Merging_of_Graph_Neural_Force_Fields_and/index.html) — Parth Verma 외, 2026
- [GRAIL: Gradient-Reweighted Advantages for Reinforcement Learning with Verifiable Rewards](../../docs/papers/9755_GRAIL_Gradient-Reweighted_Advantages_for_Reinforcement_Learn/index.html) — Tej Deep Pala 외, 2026
- [Generative Inversion of Spectroscopic Data for Amorphous Structure Elucidation](../../docs/papers/1099_Generative_Inversion_of_Spectroscopic_Data_for_Amorphous_Str/index.html) — Jiawei Guo 외, 2026
- [Generative Structure Search for Efficient and Diverse Discovery of Molecular and Crystal Structures](../../docs/papers/3120_Generative_Structure_Search_for_Efficient_and_Diverse_Discov/index.html) — 2026.04
- [Global Plane Waves from Local Gaussians: Periodic Charge Densities in a Blink](../../docs/papers/9748_Global_Plane_Waves_from_Local_Gaussians_Periodic_Charge_Dens/index.html) — Jonas Elsborg 외, 2026
- [GoodPoint: Learning Constructive Scientific Paper Feedback from Author Responses](../../docs/papers/9751_GoodPoint_Learning_Constructive_Scientific_Paper_Feedback_fr/index.html) — Jimin Mun 외, 2026
- [HiPhO: How Far Are (M)LLMs from Humans in the Latest High School Physics Olympiad Benchmark?](../../docs/papers/9783_HiPhO_How_Far_Are_MLLMs_from_Humans_in_the_Latest_High_Schoo/index.html) — Fangchen Yu 외, 2026
- [LASER: Learning Active Sensing for Continuum Field Reconstruction](../../docs/papers/9878_LASER_Learning_Active_Sensing_for_Continuum_Field_Reconstruc/index.html) — Huayu Deng 외, 2026
- [Latent Generative Solvers for Generalizable Long-Term Physics Simulation](../../docs/papers/3149_Latent_Generative_Solvers_for_Generalizable_Long-Term_Physic/index.html) — 2026.02
- [Learning Junta Distributions, Quantum Junta States, and QAC^0 Circuits](../../docs/papers/9913_Learning_Junta_Distributions_Quantum_Junta_States_and_QAC0_C/index.html) — Jinge Bao 외, 2026
- [LithoDreamer: A Physics-Informed World Model for Multi-Stage Computational Lithography](../../docs/papers/9950_LithoDreamer_A_Physics-Informed_World_Model_for_Multi-Stage/index.html) — Yuqi Jiang 외, 2026
- [LithoGRPO: Fast Inverse Lithography via GRPO Reinforced Flow Matching](../../docs/papers/9952_LithoGRPO_Fast_Inverse_Lithography_via_GRPO_Reinforced_Flow/index.html) — Yao Lai 외, 2026
- [MEDA: Medical-Oriented Activation Editing for Hallucination Mitigation in Medical Large Vision-Language Model](../../docs/papers/10006_MEDA_Medical-Oriented_Activation_Editing_for_Hallucination_M/index.html) — Tianbo Wang 외, 2026
- [MEG-XL: Data-Efficient Brain-to-Text via Long-Context Pre-Training](../../docs/papers/10019_MEG-XL_Data-Efficient_Brain-to-Text_via_Long-Context_Pre-Tra/index.html) — Dulhan Jayalath 외, 2026
- [MIRAI: Prediction and Generation of High-Impact Academic Research](../../docs/papers/3388_MIRAI_Prediction_and_Generation_of_High-Impact_Academic_Rese/index.html) — Alex Li 외, 2026.06
- [MOES-Pred: Molecular Structural Representation Learning by Adaptive Energy-Sentinel Vibration for Generalized Property Prediction](../../docs/papers/10051_MOES-Pred_Molecular_Structural_Representation_Learning_by__A/index.html) — Zhiran Hou 외, 2026
- [Mechanistic machine learning enables interpretable and generalizable prediction of prime editing outcomes](../../docs/papers/3163_Mechanistic_machine_learning_enables_interpretable_and_gener/index.html) — 2026.02
- [MedSIGHT: Towards Grounded Visual Comprehension in Medical Large Vision-Language Models](../../docs/papers/10018_MedSIGHT_Towards_Grounded_Visual_Comprehension_in_Medical_La/index.html) — Aofei Chang 외, 2026
- [MerLean: An Agentic Framework for Autoformalization in Quantum Computation](../../docs/papers/532_MerLean_An_Agentic_Framework_for_Autoformalization_in_Quantu/index.html) — Yuanjie Ren 외, 2026.02
- [MolCrystalFlow: Molecular Crystal Structure Prediction via Flow Matching](../../docs/papers/3173_MolCrystalFlow_Molecular_Crystal_Structure_Prediction_via_Fl/index.html) — 2026.02
- [MotifCraft: scalable functional protein binder design with AlphaFold2 hallucination](../../docs/papers/10062_MotifCraft_scalable_functional_protein_binder_design_with_Al/index.html) — Océane Follonier 외, 2026
- [Multi-Objective Protein Design via Memory-Aware Test-Time Scaling in Diffusion Models](../../docs/papers/10068_Multi-Objective_Protein_Design_via_Memory-Aware_Test-Time_Sc/index.html) — Ming Yang 외, 2026
- [MutAtlas: A PDB-Wide Energy-Guided Atlas of Protein Mutation Effects](../../docs/papers/10079_MutAtlas_A_PDB-Wide_Energy-Guided_Atlas_of_Protein_Mutation/index.html) — Ruihan Guo 외, 2026
- [NOVA-Test: Auditing LLM-Generated Research Hypotheses with Structural Analogy, Prior-Work, and Falsifiability Tests](../../docs/papers/10114_NOVA-Test_Auditing_LLM-Generated_Research_Hypotheses_with_St/index.html) — David Scott Lewis 외, 2026
- [Neural Control: Adjoint Learning Through Equilibrium Constraints](../../docs/papers/10090_Neural_Control_Adjoint_Learning_Through_Equilibrium_Constrai/index.html) — Dezhong Tong 외, 2026
- [NeuroCLUS: A Foundation Model with Functional Clustering for Intracranial Neural Decoding](../../docs/papers/10102_NeuroCLUS_A_Foundation_Model_with_Functional_Clustering_for/index.html) — Hui Zheng 외, 2026
- [Numina-Lean-Agent: An Open and General Agentic Reasoning System for Formal Mathematics](../../docs/papers/10115_Numina-Lean-Agent_An_Open_and_General_Agentic_Reasoning_Syst/index.html) — Junqi Liu 외, 2026
- [On the Role of Consistency Between Physics and Data in Physics-Informed Neural Networks](../../docs/papers/3195_On_the_Role_of_Consistency_Between_Physics_and_Data_in_Physi/index.html) — 2026.02
- [Online Safety Monitoring for LLMs](../../docs/papers/10130_Online_Safety_Monitoring_for_LLMs/index.html) — Mona Schirmer 외, 2026
- [OpenDiscoveryTrace: Process Traces for Evaluating AI Scientist Workflows](../../docs/papers/10134_OpenDiscoveryTrace_Process_Traces_for_Evaluating_AI_Scientis/index.html) — Aayam Bansal 외, 2026
- [OpenTSLM: Time-Series Language Models for Reasoning over Multivariate Medical Text- and Time-Series Data](../../docs/papers/10136_OpenTSLM_Time-Series_Language_Models_for_Reasoning_over_Mult/index.html) — Patrick Langer 외, 2026
- [Optimal Quantum Speedups for Repeatedly Nested Expectation Estimation](../../docs/papers/10139_Optimal_Quantum_Speedups_for_Repeatedly_Nested_Expectation_E/index.html) — Yihang Sun 외, 2026
- [Origo: Interpretable Multi-physics PDE Foundation Model through Neural Operator Splitting](../../docs/papers/10147_Origo_Interpretable_Multi-physics_PDE_Foundation_Model_throu/index.html) — Li Sun 외, 2026
- [P1-VL: Bridging Visual Perception and Scientific Reasoning in Physics Olympiads](../../docs/papers/10150_P1-VL_Bridging_Visual_Perception_and_Scientific_Reasoning_in/index.html) — Yun Luo 외, 2026
- [PDFBench: A Benchmark for De Novo Protein Design from Function](../../docs/papers/10165_PDFBench_A_Benchmark_for_De_Novo_Protein_Design_from_Functio/index.html) — Jiahao Kuang 외, 2026
- [PGD-NO: A Neural Operator with Precomputed Geometry Decomposition for 3D Million-Scale Physics Simulations](../../docs/papers/10176_PGD-NO_A_Neural_Operator_with_Precomputed_Geometry_Decomposi/index.html) — Weiheng Zhong 외, 2026
- [PINNfluence: Interpreting PINNs through Influence Functions](../../docs/papers/10197_PINNfluence_Interpreting_PINNs_through_Influence_Functions/index.html) — Aleksander Krasowski 외, 2026
- [PLaID++: A Preference Aligned Language Model for Targeted Inorganic Materials Design](../../docs/papers/10199_PLaID_A_Preference_Aligned_Language_Model_for_Targeted_Inorg/index.html) — Andy Xu 외, 2026
- [PODiff: Latent Diffusion in Proper Orthogonal Decomposition Space for Scientific Super-Resolution](../../docs/papers/10208_PODiff_Latent_Diffusion_in_Proper_Orthogonal_Decomposition_S/index.html) — Onkar Jadhav 외, 2026
- [PathwayLLM: Explainable Clinical Trajectory Modeling with Structured Pathways for Sepsis Prediction](../../docs/papers/10162_PathwayLLM_Explainable_Clinical_Trajectory_Modeling_with_Str/index.html) — Zhengqiu Yu 외, 2026
- [PhenoBrain: Phenotype-Conditioned Long-Range Communication for Multi-Modal Brain Network Analysis](../../docs/papers/10178_PhenoBrain_Phenotype-Conditioned_Long-Range_Communication_fo/index.html) — Lingyuan Meng 외, 2026
- [PhyNiKCE: A Neurosymbolic Agentic Framework for Autonomous Computational Fluid Dynamics](../../docs/papers/3206_PhyNiKCE_A_Neurosymbolic_Agentic_Framework_for_Autonomous_Co/index.html) — 2026.02
- [Pixel2Gene enables histology-guided reconstruction and prediction of spatial gene expression](../../docs/papers/3209_Pixel2Gene_enables_histology-guided_reconstruction_and_predi/index.html) — 2026.02
- [Position: Preventing the Collapse of Peer Review Requires Verification-First AI](../../docs/papers/10216_Position_Preventing_the_Collapse_of_Peer_Review_Requires_Ver/index.html) — Lei You 외, 2026
- [ProofGate: A Reproducible Audit of Faithfulness, Alignment, and Vacuity in State-of-the-Art Lean Theorem Provers](../../docs/papers/10257_ProofGate_A_Reproducible_Audit_of_Faithfulness_Alignment_and/index.html) — Edison Yang 외, 2026
- [ProtDBench: A Unified Benchmark of Protein Binder Design and Evaluation](../../docs/papers/10261_ProtDBench_A_Unified_Benchmark_of_Protein_Binder_Design_and/index.html) — Cong Liu 외, 2026
- [Protect*: Steerable Retrosynthesis through Neuro-Symbolic State Encoding](../../docs/papers/3219_Protect_Steerable_Retrosynthesis_through_Neuro-Symbolic_Stat/index.html) — 2026.02
- [ProteomeLM: A Proteome-Scale Language Model Enables Accurate and Rapid Prediction of Protein-Protein Interactions and Gene Essentiality Across Taxa](../../docs/papers/10267_ProteomeLM_A_Proteome-Scale_Language_Model_Enables_Accurate/index.html) — Cyril Malbranke 외, 2026
- [Proving Your Way to Cooperation: Formalizing Proof-Based Open Source Game Theory in Lean](../../docs/papers/10273_Proving_Your_Way_to_Cooperation_Formalizing_Proof-Based_Open/index.html) — Colomban Duclaux 외, 2026
- [Pseudo-Label Validation for Unsupervised Domain Adaptation](../../docs/papers/10275_Pseudo-Label_Validation_for_Unsupervised_Domain_Adaptation/index.html) — Nathan Weill 외, 2026
- [Quantum latent distributions in deep generative models](../../docs/papers/10286_Quantum_latent_distributions_in_deep_generative_models/index.html) — Omar Bacarreza 외, 2026
- [RAPNet: Accelerating Algebraic Multigrid with Learned Sparse Corrections](../../docs/papers/10294_RAPNet_Accelerating_Algebraic_Multigrid_with_Learned_Sparse/index.html) — Yali Fink 외, 2026
- [ReViT: Rotational-equivariant Vision Transformers for Neural PDE Solvers](../../docs/papers/10344_ReViT_Rotational-equivariant_Vision_Transformers_for_Neural/index.html) — Hao Wei 외, 2026
- [Recursive Flow Matching](../../docs/papers/10311_Recursive_Flow_Matching/index.html) — Jiahe Huang 외, 2026
- [ReviewArena: A Large-Scale Cross-Conference Dataset and Benchmark for LLM Peer Review](../../docs/papers/10341_ReviewArena_A_Large-Scale_Cross-Conference_Dataset_and_Bench/index.html) — Samarth P 외, 2026
- [S1-MMAlign: A Large-Scale, Multi-Disciplinary Dataset for Scientific Figure-Text Understanding](../../docs/papers/691_S1-MMAlign_A_Large-Scale_Multi-Disciplinary_Dataset_for_Scie/index.html) — He Wang 외, 2026.01
- [SEAD: Competence-Aware On-Policy Distillation via Entropy-Guided Supervision](../../docs/papers/10399_SEAD_Competence-Aware_On-Policy_Distillation_via_Entropy-Gui/index.html) — Chia-Hsuan Lee 외, 2026
- [SEVerA: Verified Synthesis of Self-Evolving Agents](../../docs/papers/750_SEVerA_Verified_Synthesis_of_Self-Evolving_Agents/index.html) — Debangshu Banerjee 외, 2026.03
- [SIGMA-PPG: Statistical-prior Informed Generative Masking Architecture for PPG Foundation Model](../../docs/papers/10440_SIGMA-PPG_Statistical-prior_Informed__Generative_Masking_Arc/index.html) — Zongheng Guo 외, 2026
- [SR-Scientist: Scientific Equation Discovery With Agentic AI](../../docs/papers/10488_SR-Scientist_Scientific_Equation_Discovery_With_Agentic_AI/index.html) — Shijie Xia 외, 2026
- [SciContrib-Bench: Mapping the Autonomy Landscape of AI Scientists Through Stage-Dependent Detectability](../../docs/papers/10386_SciContrib-Bench_Mapping_the_Autonomy_Landscape_of_AI_Scient/index.html) — Raghav Agarwal 외, 2026
- [SciPaths: Forecasting Pathways to Scientific Discovery](../../docs/papers/10392_SciPaths_Forecasting_Pathways_to_Scientific_Discovery/index.html) — Eric Chamoun 외, 2026
- [Sibyl: Temporal Backtesting for Literature-Based Scientific Discovery with Large Language Model Agents](../../docs/papers/10438_Sibyl_Temporal_Backtesting_for_Literature-Based_Scientific_D/index.html) — Blagoy Rangelov, 2026
- [Stochastic Dimension-Free Zeroth-Order Estimator for High-Dimensional and High-Order PINNs](../../docs/papers/3246_Stochastic_Dimension-Free_Zeroth-Order_Estimator_for_High-Di/index.html) — 2026.03
- [SymSpectra: Symmetric Information Bottleneck Framework for Molecular Structure Recognition under Imbalanced Settings](../../docs/papers/10524_SymSpectra_Symmetric_Information_Bottleneck_Framework_for_Mo/index.html) — Xiaohan Qin 외, 2026
- [Symmetry-Constrained Gaussian Processes for Sample-Efficient Molecular Property Prediction](../../docs/papers/10523_Symmetry-Constrained_Gaussian_Processes_for_Sample-Efficient/index.html) — Kaustubh S. Bukkapatnam 외, 2026
- [The IAEA Fusion Data Lake Project — Accelerating AI and Big Data Applications through Open Science and FAIR Data](../../docs/papers/3257_The_IAEA_Fusion_Data_Lake_Project__Accelerating_AI_and_Big_D/index.html) — Daljeet Singh Gahle 외, 2026.04
- [TurboAgent: An LLM-Driven Autonomous Multi-Agent Framework for Turbomachinery Aerodynamic Design](../../docs/papers/3270_TurboAgent_An_LLM-Driven_Autonomous_Multi-Agent_Framework_fo/index.html) — 2026.04
- [U-Cast: A Surprisingly Simple and Efficient Frontier Probabilistic AI Weather Forecaster](../../docs/papers/10652_U-Cast_A_Surprisingly_Simple_and_Efficient_Frontier_Probabil/index.html) — Salva Rühling Cachay 외, 2026
- [UniMedVL: Unifying Medical Multimodal Understanding and Generation through Observation-Knowledge-Analysis](../../docs/papers/10664_UniMedVL_Unifying_Medical_Multimodal_Understanding_and_Gener/index.html) — Junzhi Ning 외, 2026
- [VT-Bench: A Unified Benchmark for Visual-Tabular Multi-Modal Learning](../../docs/papers/10685_VT-Bench_A_Unified_Benchmark_for_Visual-Tabular_Multi-Modal/index.html) — Ziyi Jia 외, 2026
- [VeriBench: An End-to-End Formal Verification Benchmark for AI Coding Agents in Lean 4](../../docs/papers/10676_VeriBench_An_End-to-End_Formal_Verification_Benchmark_for_AI/index.html) — Brando Miranda 외, 2026
- [VeriScale: Adversarial Test-Suite Scaling for Verifiable Code Generation](../../docs/papers/10677_VeriScale_Adversarial_Test-Suite_Scaling_for_Verifiable_Code/index.html) — Yifan Bai 외, 2026
- [YC-Bench: Benchmarking AI Agents for Long-Term Planning and Consistent Execution](../../docs/papers/3398_YC-Bench_Benchmarking_AI_Agents_for_Long-Term_Planning_and_C/index.html) — Muyu He 외, 2026
- [miniF2F-Dafny: LLM-Guided Mathematical Theorem Proving via Auto-Active Verification](../../docs/papers/10033_miniF2F-Dafny_LLM-Guided_Mathematical_Theorem_Proving_via_Au/index.html) — Mantas Baksys 외, 2026
- [A Perspective on Foundation Models in Chemistry](../../docs/papers/015_A_Perspective_on_Foundation_Models_in_Chemistry/index.html) — Junyoung Choi 외, 2025.04 · 인용 39
- [A Survey on Hypothesis Generation for Scientific Discovery in the Era of Large Language Models](../../docs/papers/031_A_Survey_on_Hypothesis_Generation_for_Scientific_Discovery_i/index.html) — Atilla Kaan Alkan 외, 2025.04 · 인용 2
- [A retrieval-augmented knowledge mining method with deep thinking LLMs for biomedical research and clinical support](../../docs/papers/018_A_retrieval-augmented_knowledge_mining_method_with_deep_thin/index.html) — Yichun Feng 외, 2025 · 인용 10
- [AAAR-1.0: Assessing AI's Potential to Assist Research](../../docs/papers/041_Aaar-10_Assessing_ais_potential_to_assist_research/index.html) — Renze Lou et al., 2025
- [AI Copilot Code Quality: 2025 Data Suggests 4x Growth in Code Clones - GitClear](../../docs/papers/894_AI_Copilot_Code_Quality_2025_Data_Suggests_4x_Growth_in_Code/index.html) — Hongjing Shao 외, 2025
- [AI Scientists Fail Without Strong Implementation Capability](../../docs/papers/081_Ai_scientists_fail_without_strong_implementation_capability/index.html) — Min Zhu 외, 2025
- [All that glitters is not novel: Plagiarism in ai generated research](../../docs/papers/093_All_that_glitters_is_not_novel_Plagiarism_in_ai_generated_re/index.html) — Tarun Gupta 외, 2025
- [AlphaGenome: advancing regulatory variant effect prediction with a unified DNA sequence model](../../docs/papers/094_AlphaGenome_advancing_regulatory_variant_effect_prediction_w/index.html) — Žiga Avsec 외, 2025 · 인용 106
- [Ask, retrieve, summarize: A modular pipeline for scientific literature summarization](../../docs/papers/108_Ask_retrieve_summarize_A_modular_pipeline_for_scientific_lit/index.html) — Pierre Achkar 외, 2025
- [Atomically accurate de novo design of antibodies with RFdiffusion](../../docs/papers/112_Atomically_accurate_de_novo_design_of_antibodies_with_RFdiff/index.html) — Nathaniel R. Bennett 외, 2025.02 · 인용 192
- [Autonomous Agents for Scientific Discovery: Orchestrating Scientists, Language, Code, and Physics](../../docs/papers/137_Autonomous_Agents_for_Scientific_Discovery_Orchestrating_Sci/index.html) — Lianhao Zhou 외, 2025.10
- [BiasFilter: An inference-time debiasing framework for large language models](../../docs/papers/158_Biasfilter_An_inference-time_debiasing_framework_for_large_l/index.html) — Xiaoqing Cheng 외, 2025
- [BioProBench: Comprehensive Dataset and Benchmark in Biological Protocol Understanding and Reasoning](../../docs/papers/169_Bioprobench_Comprehensive_dataset_and_benchmark_in_biologica/index.html) — Yuyang Liu 외, 2025
- [Clinical entity augmented retrieval for clinical information extraction](../../docs/papers/224_Clinical_entity_augmented_retrieval_for_clinical_information/index.html) — Iván López 외, 2025
- [CodePDE: An Inference Framework for LLM-driven PDE Solver Generation](../../docs/papers/232_CodePDE_An_Inference_Framework_for_LLM-driven_PDE_Solver_Gen/index.html) — Shanda Li 외, 2025
- [DEFAME: Dynamic Evidence-based Fact-checking with Multimodal Experts](../../docs/papers/267_Defame_Dynamic_evidencebased_fact-checking_with_multimodal_e/index.html) — Tobias Braun 외, 2025
- [DeepScientist: Advancing Frontier-Pushing Scientific Findings Progressively](../../docs/papers/10727_deepscientist_advancing_frontier-pushing_scientific_fi/index.html) — Yixuan Weng 외, 2025.09
- [DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning](../../docs/papers/265_DeepSeek-R1_incentivizes_reasoning_in_LLMs_through_reinforce/index.html) — DeepSeek-AI 외, 2025
- [Democratizing AI scientists using ToolUniverse](../../docs/papers/268_Democratizing_AI_scientists_using_ToolUniverse/index.html) — Shanghua Gao 외, 2025.09
- [Detecting LLM-written Peer Reviews](../../docs/papers/270_Detecting_llm-written_peer_reviews/index.html) — Vishisht Rao 외, 2025
- [Discovery of Unstable Singularities](../../docs/papers/276_Discovery_of_Unstable_Singularities/index.html) — Yongji Wang 외, 2025.09
- [Earth-Agent: Unlocking the Full Landscape of Earth Observation with Agents](../../docs/papers/298_Earth-Agent_Unlocking_the_Full_Landscape_of_Earth_Observatio/index.html) — Peilin Feng 외, 2025.09
- [El Agente: An Autonomous Agent for Quantum Chemistry](../../docs/papers/308_El_Agente_An_Autonomous_Agent_for_Quantum_Chemistry/index.html) — Yunheng Zou 외, 2025
- [Enhancing chart-to-code generation in multimodal large language models via iterative dual preference learning](../../docs/papers/315_Enhancing_chart-to-code_generation_in_multimodal_large_langu/index.html) — Zhihan Zhang 외, 2025
- [Foundation Models for Environmental Science: A Survey of Emerging Frontiers](../../docs/papers/342_Foundation_Models_for_Environmental_Science_A_Survey_of_Emer/index.html) — Runlong Yu 외, 2025.04
- [From large language models to multimodal AI: A scoping review on the potential of generative AI in medicine](../../docs/papers/359_From_large_language_models_to_multimodal_ai_A_scoping_review/index.html) — Lukas Buess 외, 2025
- [Generalization Bias in Large Language Model Summarization of Scientific Research](../../docs/papers/373_Generalization_Bias_in_Large_Language_Model_Summarization_of/index.html) — Uwe Peters 외, 2025.03
- [Iterative Distillation for Reward-Guided Fine-Tuning of Diffusion Models in Biomolecular Design](../../docs/papers/446_Iterative_Distillation_for_Reward-Guided_Fine-Tuning_of_Diff/index.html) — Xingyu Su 외, 2025
- [LLM-SRBench: A New Benchmark for Scientific Equation Discovery with Large Language Models](../../docs/papers/504_Llm-srbench_A_new_benchmark_for_scientific_equation_discover/index.html) — Parshin Shojaee 외, 2025
- [LLM-based Multi-Agent Copilot for Quantum Sensor](../../docs/papers/501_LLM-based_Multi-Agent_Copilot_for_Quantum_Sensor/index.html) — Rong Sha 외, 2025
- [LLM4SR: A Survey on Large Language Models for Scientific Research](../../docs/papers/506_LLM4SR_A_Survey_on_Large_Language_Models_for_Scientific_Rese/index.html) — Ziming Luo 외, 2025.01
- [LLMEval-Med: A Real-world Clinical Benchmark for Medical LLMs with Physician Validation](../../docs/papers/507_Llmeval-med_A_real-world_clinical_benchmark_for_medical_llms/index.html) — Ming Zhang 외, 2025
- [Lazyreview a dataset for uncovering lazy thinking in nlp peer reviews](../../docs/papers/481_Lazyreview_a_dataset_for_uncovering_lazy_thinking_in_nlp_pee/index.html) — Sukannya Purkayastha 외, 2025
- [Learning to Discover Regulatory Elements for Gene Expression Prediction](../../docs/papers/483_Learning_to_Discover_Regulatory_Elements_for_Gene_Expression/index.html) — Xingyu Su 외, 2025
- [MoDeST: A dataset for Multi Domain Scientific Title Generation](../../docs/papers/10765_modest_a_dataset_for_multi_domain_scientific_title_gen/index.html) — Necva Bölücü 외, 2025.05
- [Mooseagent: A llm based multi-agent framework for automating moose simulation](../../docs/papers/559_Mooseagent_A_llm_based_multi-agent_framework_for_automating/index.html) — Tao Zhang 외, 2025
- [Multi-agent risks from advanced AI](../../docs/papers/562_Multi-agent_risks_from_advanced_ai/index.html) — Lewis Hammond 외, 2025
- [NSF-SCIFY: Mining the NSF Awards Database for Scientific Claims](../../docs/papers/579_Nsf-scify_Mining_the_nsf_awards_database_for_scientific_clai/index.html) — D. Rao 외, 2025
- [OpenFOAMGPT 2.0: end-to-end, trustworthy automation for computational fluid dynamics](../../docs/papers/588_OpenFOAMGPT_20_end-to-end_trustworthy_automation_for_computa/index.html) — Jingsen Feng 외, 2025.04
- [OpenFOAMGPT: A retrieval-augmented large language model (LLM) agent for OpenFOAM-based computational fluid dynamics](../../docs/papers/589_OpenFOAMGPT_A_retrieval-augmented_large_language_model_LLM_a/index.html) — Sandeep Pandey 외, 2025
- [Paper2poster: Towards multimodal poster automation from scientific papers](../../docs/papers/599_Paper2poster_Towards_multimodal_poster_automation_from_scien/index.html) — Wei Pang 외, 2025
- [Patientsim: A Persona-Driven Simulator for Realistic Doctor-Patient Interactions](../../docs/papers/606_Patientsim_A_persona-driven_simulator_for_realistic_doctor-p/index.html) — Daeun Kyung 외, 2025
- [Psyche: A multi-faceted patient simulation framework for evaluation of psychiatric assessment conversational agents](../../docs/papers/644_Psyche_A_multi-faceted_patient_simulation_framework_for_eval/index.html) — Jingoo Lee 외, 2025
- [ReTool: Reinforcement Learning for Strategic Tool Use in LLMs](../../docs/papers/674_ReTool_Reinforcement_Learning_for_Strategic_Tool_Use_in_LLMs/index.html) — Jiazhan Feng 외, 2025
- [Remor: Automated peer review generation with llm reasoning and multi-objective reinforcement learning](../../docs/papers/665_Remor_Automated_peer_review_generation_with_llm_reasoning_an/index.html) — Pawin Taechoyotin 외, 2025
- [ResearchBench: Benchmarking LLMs in Scientific Discovery via Inspiration-Based Task Decomposition](../../docs/papers/669_Researchbench_Benchmarking_llms_in_scientific_discovery_via/index.html) — Yujie Liu 외, 2025
- [Reward-Guided Iterative Refinement in Diffusion Models at Test-Time with Applications to Protein and DNA Design](../../docs/papers/682_Reward-Guided_Iterative_Refinement_in_Diffusion_Models_at_Te/index.html) — Masatoshi Uehara 외, 2025
- [Scaling Large Language Models for Next-Generation Single-Cell Analysis](../../docs/papers/696_Scaling_Large_Language_Models_for_Next-Generation_Single-Cel/index.html) — Syed Asad Rizvi 외, 2025.04
- [ScholarCopilot: Training Large Language Models for Academic Writing with Accurate Citations](../../docs/papers/702_Scholarcopilot_Training_large_language_models_for_academic_w/index.html) — Yubo Wang 외, 2025
- [SciHorizon: Benchmarking AI-for-Science Readiness from Scientific Data to Large Language Models](../../docs/papers/724_SciHorizon_Benchmarking_AI-for-Science_Readiness_from_Scient/index.html) — Chuan Qin 외, 2025.03
- [Sciclaimhunt: A large dataset for evidence-based scientific claim verification](../../docs/papers/710_Sciclaimhunt_A_large_dataset_for_evidence-based_scientific_c/index.html) — Sujit Kumar 외, 2025
- [Scicueval: A comprehensive dataset for evaluating scientific context understanding in large language models](../../docs/papers/713_Scicueval_A_comprehensive_dataset_for_evaluating_scientific/index.html) — Jing Yu 외, 2025
- [ScienceAgentBench: Toward Rigorous Assessment of Language Agents for Data-Driven Scientific Discovery](../../docs/papers/716_ScienceAgentBench_Toward_Rigorous_Assessment_of_Language_Age/index.html) — Ziru Chen 외, 2025.03
- [Scienceboard: Evaluating multimodal autonomous agents in realistic scientific workflows](../../docs/papers/717_Scienceboard_Evaluating_multimodal_autonomous_agents_in_real/index.html) — Qiushi Sun 외, 2025
- [Scirgc: Multi-granularity citation recommendation and citation sentence preference alignment](../../docs/papers/1091_Scirgc_Multi-granularity_citation_recommendation_and_citatio/index.html) — Xi Chen 외, 2025
- [Sciverse: Unveiling the knowledge comprehension and visual reasoning of lmms on multi-modal scientific problems](../../docs/papers/737_Sciverse_Unveiling_the_knowledge_comprehension_and_visual_re/index.html) — Z. J. Guo 외, 2025
- [Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement Learning](../../docs/papers/740_Search-R1_Training_LLMs_to_Reason_and_Leverage_Search_Engine/index.html) — Bowen Jin 외, 2025
- [SurveyX: Academic survey automation via large language models](../../docs/papers/781_Surveyx_Academic_survey_automation_via_large_language_models/index.html) — Xun Liang 외, 2025
- [Surveyforge: On the outline heuristics, memory-driven generation, and multi-dimensional evaluation for automated survey writing](../../docs/papers/780_Surveyforge_On_the_outline_heuristics_memory-driven_generati/index.html) — Xiangchao Yan 외, 2025
- [The hidden dimensions of llm alignment: A multi-dimensional safety analysis](../../docs/papers/800_The_hidden_dimensions_of_llm_alignment_A_multi-dimensional_s/index.html) — Wenbo Pan 외, 2025
- [Vending-Bench: A Benchmark for Long-Term Coherence of Autonomous Agents](../../docs/papers/865_Vending-Bench_A_Benchmark_for_Long-Term_Coherence_of_Autonom/index.html) — Axel Backlund 외, 2025.02
- [WebThinker: Empowering Large Reasoning Models with Deep Research Capability](../../docs/papers/873_WebThinker_Empowering_Large_Reasoning_Models_with_Deep_Resea/index.html) — Xiaoxi Li 외, 2025
- [Zero-shot sim-to-real transfer for reinforcement learning-based visual servoing of soft continuum arms](../../docs/papers/891_Zero-shot_sim-to-real_transfer_for_reinforcement_learning-ba/index.html) — Hsin-Jung Yang 외, 2025
- [Withdrarxiv: A large-scale dataset for retraction study](../../docs/papers/885_Withdrarxiv_A_large-scale_dataset_for_retraction_study/index.html) — Delip Rao 외, 2024
- [SciReviewGen: a large-scale dataset for automatic literature review generation](../../docs/papers/732_Scireviewgen_a_large-scale_dataset_for_automatic_literature/index.html) — Tetsu Kasanishi 외, 2023

*생성: `pipeline/build_slide_deck.py --topic ai4s` · 2026-08-06 · 근거 코퍼스 2,658편 (`docs/ai4s`)*
