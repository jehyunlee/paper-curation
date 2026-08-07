"""AI4Science 발표용 50-슬라이드 원고 빌더.

코퍼스(`docs/{topic}/_category_summaries.json`, `_timeline_narrative.json`,
`_new_classification.json`, `_insights.json`, `docs/papers/_papers_index.json`)에서
카테고리·서브카테고리 규모, 시기, 상태, 대표 도구, 대표 논문을 뽑고
큐레이션된 한국어 내러티브와 합쳐 슬라이드 원고 두 벌을 출력한다.

  - `reports/build/{topic}_slides_50.html`  : 브라우저·인쇄용 (자기완결 HTML)
  - `reports/source/{topic}_slides_50.md`   : Obsidian 용 (frontmatter + `---` 구분)

슬라이드 구성 (총 50장):
  S01–S05  오프닝(표지·방법·코퍼스·지형도·관통 서사)
  S06–S45  카테고리 8개 × 서브카테고리 상위 5개 = 40장
  S46–S50  종합(수렴·부상/쇠퇴·공백·검증 전환·실행 제언)

Usage:
  PYTHONUTF8=1 python pipeline/build_slide_deck.py --topic ai4s
  PYTHONUTF8=1 python pipeline/build_slide_deck.py --topic ai4s --per-category 5
"""
import argparse
import html as H
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

PIPE = Path(__file__).resolve().parent
sys.path.insert(0, str(PIPE))
PROJECT_ROOT = PIPE.parent

from config_loader import PAPERS_DIR, get_topic_dir  # noqa: E402
from lib.atomic_io import atomic_write_text  # noqa: E402

REPORTS = PROJECT_ROOT / "reports"

ACCENT = {"ai4s": "#D63423", "scisci": "#2374D6"}

STATUS_KO = {
    "ACCELERATING": "가속",
    "STABLE": "안정",
    "EMERGING": "부상",
    "DECLINING": "감소",
}

CATEGORY_KO = {
    "AI-Driven Drug and Materials Discovery": "AI 기반 신약·신소재 발견",
    "LLM Benchmarking and Agent Evaluation": "LLM·에이전트 평가",
    "Scientific AI for Physics and Environment": "물리·환경 과학 AI",
    "Molecular Simulation and Generative Modeling": "분자 시뮬레이션·생성 모델링",
    "Agentic AI for Scientific Automation": "과학 자동화 에이전트 AI",
    "Formal Methods and Computational Reasoning": "형식 방법론·계산 추론",
    "Scientific Information Extraction and QA": "과학 정보추출·질의응답",
    "AI-Assisted Academic Scholarly Communication": "AI 지원 학술 커뮤니케이션",
}

CATEGORY_LEAD = {
    "AI-Driven Drug and Materials Discovery":
        "코퍼스 최대 카테고리. 구조 예측이 풀린 뒤 필드 전체가 '설계'와 '검증'으로 이동했다.",
    "LLM Benchmarking and Agent Evaluation":
        "무엇을 못하는지 재는 일이 산업이 됐다. 벤치마크 설계 역량이 곧 도입 판단 역량.",
    "Scientific AI for Physics and Environment":
        "AI가 운용 수치예보를 이긴 뒤, 경쟁축은 속도에서 보장(guarantee)으로 옮겨갔다.",
    "Molecular Simulation and Generative Modeling":
        "생성은 값싸졌다. 남은 문제는 합성 가능성과 독립 재분석이다.",
    "Agentic AI for Scientific Automation":
        "습식 검증 성공 사례와 '과학적으로 추론하지 않는다'는 반증이 같은 해에 나왔다.",
    "Formal Methods and Computational Reasoning":
        "검증기가 있는 도메인은 자동화가 끝나간다. 이제 검증기를 만드는 일이 병목.",
    "Scientific Information Extraction and QA":
        "과학 도메인 언어모델이 검색·도표·주장 검증까지 확장하며 연구 무결성 인프라가 됐다.",
    "AI-Assisted Academic Scholarly Communication":
        "AI 저작·심사 정책을 감정이 아니라 데이터로 설계할 근거가 쌓였다.",
}

# ── 큐레이션 내러티브 (키 = _category_summaries.json 의 sub_themes[].name) ──
# 원칙: 사례는 2025년 이후를 우선하고, 그 이전은 필요한 만큼만 '배경'으로 남긴다.
NARRATIVE = {
    # ── AI-Driven Drug and Materials Discovery ──────────────────────────────
    "Drug Compound Gene Signature Analysis": {
        "ko": "약물–유전자 서명 분석",
        "headline": "2025–2026년 사이 세포 모델은 '읽기'에서 '반응 예측·분자 설계'로 넘어갔고, 곧바로 해석성 검증이 따라붙었다.",
        "points": [
            "2025 Cell2Sentence가 단일세포 데이터를 '세포 문장'으로 바꿔 27B 규모 LLM으로 확장했다 — 전사체와 생물학 텍스트 지식의 통합.",
            "2025 Evo 2와 2026 EDEN 스케일링 법칙으로 게놈 규모 서열 파운데이션 모델이 표준 인프라가 됐다.",
            "2026 섭동–반응·가상세포 모델(AetherCell, AlphaCell, CURE, PerturbODE)이 약물 투여 후 세포 상태를 직접 예측한다.",
            "2026 전사체 교란 신호를 조건으로 약물 분자를 생성하는 TBDD(Transcriptome-based Drug Design)가 정식화됐다.",
            "2026 해석성·비판 전환: 희소 오토인코더, CLAMP, 인과 전이가능성, 잘못 설정된 베이스라인 지적이 동시에 나왔다.",
        ],
        "sowhat": "신약 스크리닝의 1차 필터가 실험에서 예측으로 이동했다. 국내 병목은 모델이 아니라 섭동 스크린 데이터 확보다.",
    },
    "Protein Binding Site Prediction": {
        "ko": "단백질 결합부위 예측",
        "headline": "2025–2026의 화두는 구조 정확도가 아니라 설계 성공률과 감사(audit)다.",
        "points": [
            "2025 RFdiffusion 항체 미세조정이 지정 에피토프에 결합하는 VHH·scFv를 원자 수준 정확도로 설계했다.",
            "2025 오픈소스 Boltz-1·Boltz-2가 AlphaFold 3급 상호작용 모델링을 개방해 진입장벽을 없앴다.",
            "2026 서브초 도킹과 양자화 코폴딩(TerraBind, ACER)으로 스크리닝 처리량이 자릿수 단위로 바뀐다.",
            "2026 신뢰성 감사가 동시 등장 — ProtDBench, PDFBench, ProMiSE, 적대적 변이 테스트.",
            "배경: 2021 AlphaFold2·RoseTTAFold, 2024 AlphaFold 3가 예측 문제를 사실상 종료시켰다.",
        ],
        "sowhat": "도구는 이미 오픈이다. 경쟁축은 습식 검증률과 실패 모드 감사로 넘어갔다.",
    },
    "Gene Enhancer Expression Prediction": {
        "ko": "조절서열·유전자 발현 예측",
        "headline": "2025 AlphaGenome 이후, 서열→발현은 '예측 가능'에서 '평가 방법을 다시 짜야 하는' 단계로 들어갔다.",
        "points": [
            "2025 AlphaGenome이 1Mb 입력 × 염기쌍 해상도로 11개 모달리티 5,930개 게놈 트랙을 동시 예측한다.",
            "2026 신호 희석 보정 섭동 지표와 모듈 귀납 표현으로 벤치마크 자체가 재설계되는 중이다.",
            "2026 OptiPrime은 프라임 편집 메커니즘을 ODE로 모델에 직접 넣어 해석성과 일반화를 함께 잡았다.",
            "2026 조직학→전사체 번역(Pixel2Gene)과 시공간 재구성(stVCR, ChronoTILE)으로 공간 오믹스와 결합한다.",
            "2026 edgePython처럼 분석 생태계가 파이썬으로 수렴하며 단일세포 파이프라인 진입비용이 낮아졌다.",
        ],
        "sowhat": "의미 불명 변이(VUS) 해석과 유전자치료 설계에 직결된다. 다음 관문은 규제기관이 받아들일 신뢰구간 제시.",
    },
    "Topological Data Analysis for Biology": {
        "ko": "생물학 위상·표현 해석",
        "headline": "2026년, 잘 맞히는 모델의 내부를 여는 해석성이 독립 서브필드가 됐다.",
        "points": [
            "2026 AlphaInterp: AlphaFold 3는 진화적 맥락에 의존하는 fold recognition 알고리즘 — '예측기는 추론하지 않는다'.",
            "2026 AlphaFold Database가 4,777개 프로테옴 3,100만 복합체로 확장되고 고신뢰 180만 건을 공개했다.",
            "2026 프로테옴 규모 상호작용 추론(ProteomeLM, FlashPPI)과 지속 호몰로지 기반 친화도 예측이 붙었다.",
            "2026 단백질 언어모델의 기계적 해석성(희소 오토인코더, cross-layer transcoder)이 본격화됐다.",
            "2026 DNA 언어모델과 PLM을 결합한 다중모달 변이효과 예측이 생물물리 제약 하에서 상보성을 입증했다.",
        ],
        "sowhat": "해석성은 규제 대응·특허·실패 원인 분석의 전제다. 수학·위상 인력이 강한 국내 그룹의 진입 여지가 크다.",
    },
    "Scientific Multimodal LLM Benchmarking": {
        "ko": "과학 멀티모달 벤치마킹",
        "headline": "2025–2026 벤치마크는 지식이 아니라 '연구를 수행하는 능력'을 잰다.",
        "points": [
            "2025 SciKnowEval·SciCUEval이 다층 과학지식을, SciCode가 연구 코딩 능력을 분리해 측정한다.",
            "2025–2026 SciVerse·P1-VL·PhysMent로 시각–언어 과학추론 평가가 확장됐다.",
            "2026 BPL 컴파일러 검증 프로토콜과 REPA로 재현성 자동화까지 벤치마크 대상이 됐다.",
            "2025 BioProBench 등 도메인 종합 벤치마크가 프로토콜 수준 수행 능력을 본다.",
            "배경: 2019 BioBERT·SciBERT의 도메인 사전학습, 2022 Galactica의 큐레이션 코퍼스 인터페이스.",
        ],
        "sowhat": "벤치마크를 설계할 수 있어야 도입을 판단할 수 있다. 국내 도메인 벤치마크 부재가 그대로 의사결정 리스크다.",
    },

    # ── LLM Benchmarking and Agent Evaluation ───────────────────────────────
    "Web-Augmented RL Reasoning Agents": {
        "ko": "웹 증강 RL 추론 에이전트",
        "headline": "62편이 사실상 2025–2026 한 구간에 몰렸다. 검증가능 보상(RLVR)이 '검색하며 생각하는' 에이전트를 1년 만에 표준으로 만들었다.",
        "points": [
            "2025 DeepSeek-R1·Kimi k1.5: 사람이 만든 추론 궤적 없이 순수 RL만으로 자기검증·재검토가 창발했다.",
            "2025 Search-R1·WebThinker·WebDancer가 검색을 학습 루프 안으로 집어넣은 딥리서치 에이전트를 만들었다.",
            "2025 ReTool은 코드 인터프리터 도구 사용을, Critique-GRPO·PAG·RISE는 비평·자기검증 기반 RL을 다룬다.",
            "2026 DR Tulu는 루브릭이 정책과 함께 진화하는 RLER로 완전 공개 8B 딥리서치 모델을 냈다.",
            "2025–2026 DRE-Bench처럼 동적 추론 평가로 '유동 지능'을 따로 재는 흐름이 붙었다.",
        ],
        "sowhat": "정답 검증기가 존재하는 과제부터 자동화가 도착한다. 보상 설계 능력이 곧 제품 경쟁력.",
    },
    "GPT Audio Safety Evaluation": {
        "ko": "프런티어 모델·멀티모달 안전성 평가",
        "headline": "2025–2026 안전 평가가 정렬의 기하학과 리더보드 통계 검증까지 내려갔다.",
        "points": [
            "2025 정렬은 단일 선형 방향이 아니라 활성화 공간의 다차원 직교 구조라는 분석이 나왔다(거부 방향과 역할극 방향의 분리).",
            "2025–2026 온라인 안전 모니터링과 다차원 정렬 지표(MDTA/LD-Score)가 운영 도구로 들어왔다.",
            "2026 과학 멀티모달 능력·안전 벤치마크가 도메인으로 확장됐다(ECG-R1, AtomWorld, HiPhO, VT-Bench).",
            "2026 리더보드 통계와 프롬프트 효과 재현 실패 보고 — 순위표 한 줄로 벤더를 고르면 안 된다.",
            "배경: GPT-4·GPT-4o·o1 시스템 카드가 탈옥·음성 리스크 분석의 문서 포맷을 정착시켰다.",
        ],
        "sowhat": "도입 심사 요건은 '시스템 카드 + 독립 재현' 두 개다. 벤치마크 순위는 근거가 아니라 가설이다.",
    },
    "Open-Source Code LLM Instruction Tuning": {
        "ko": "오픈소스 코드 LLM·명령어 튜닝",
        "headline": "2025–2026 평가는 함수 맞히기를 떠나 '검증 가능성'과 '저장소 규모'로 갔다.",
        "points": [
            "2025–2026 VeriBench·VeriScale·MathlibPR·JAXBench가 형식 검증 가능한 코드 벤치마크 축을 세웠다.",
            "2025–2026 AutoNumerics-Zero·DeltaEvolve·GAE는 LLM이 수치 알고리즘 자체를 진화시켜 새 해법을 찾는다.",
            "2025 Copilot·GitClear 감사에서 생산성 향상과 코드 복제 증가가 동시에 관측됐다.",
            "2024–2025 StarCoder2·The Stack v2(619개 언어)에서 Seed-Coder로 오픈 계보가 이어졌다.",
            "배경: SWE-bench(실제 GitHub 이슈 2,294건)의 초기 최고 모델 해결률 1.96%가 격차의 기준점이다.",
        ],
        "sowhat": "연구 코드 자동화는 이미 실용권이다. 단, 산출물을 검증 가능한 형태로 강제하는 규칙이 함께 가야 한다.",
    },
    "Self-Improvement & Annotation Fairness": {
        "ko": "자기개선·주석 공정성·통계 타당성",
        "headline": "2025–2026, '적은 라벨로 정직하게 평가하는 통계'가 이 분야의 본체가 됐다.",
        "points": [
            "2025–2026 예측기반 추론 계열(PPAT, PPAI, 다과제 PPI, CELEUS)이 제한된 주석에서도 유효한 신뢰구간을 만든다.",
            "2026 의사라벨 검증과 조건부 독립성 검정(semi-knockoffs, sequential KCI)으로 평가의 전제를 검사한다.",
            "2026 공정성·일반화 격차 감사가 도메인으로 퍼졌다(BiasFilter, SzCORE, EEG-FM-Bench, MassSpecGym 감사).",
            "2026 실행 기반 자동 AI 연구: 아이디어를 실제 실행해 성능으로 검증하고 그 피드백으로 정책을 학습한다.",
            "2025 AutoML 도구 16종 × 실제 데이터셋 21개 실증 벤치마킹으로 자동화 도구의 실효를 재확인했다.",
        ],
        "sowhat": "평가 예산이 없으면 통계로 벌어야 한다. 라벨 100개로 결론 내는 법이 조직 역량이다.",
    },
    "Uncertainty-Aware Generative Manufacturing Models": {
        "ko": "불확실성 인지 생성·대리모델",
        "headline": "2025–2026, 대리모델의 합격 기준이 정확도에서 커버리지 보장으로 바뀌었다.",
        "points": [
            "2025–2026 학습된 시뮬레이터와 CT 재구성에 확률 보정(retrofitting)과 커버리지 보증을 덧입힌다.",
            "2026 추론시간 RL과 제약 기반 재료·분자 생성 설계(OMatG-IRL, Autoregressive Boltzmann Generators).",
            "2026 임상·생체신호 파운데이션 모델이 UQ를 기본 탑재한다(SleepMaMi, SIGMA-PPG, token-free ECG SSM).",
            "2026 생성형 자료동화(DAISI), 다중뷰 인과 발견, 확률적 멤버십 회로로 신뢰성 검사를 구조화한다.",
            "2025 의료 생성 AI 스코핑 리뷰가 LLM→멀티모달 전환의 임상 근거를 PRISMA-ScR로 정리했다.",
        ],
        "sowhat": "제조·의료 도입 게이트는 '틀릴 때 틀렸다고 말하는가'다. UQ 없는 대리모델은 반입 금지 대상.",
    },

    # ── Scientific AI for Physics and Environment ───────────────────────────
    "Neural Operator PDE Solving": {
        "ko": "신경 연산자·물리정보 PDE 해석",
        "headline": "2025–2026, 신경 연산자는 '빠른 근사'에서 '구조를 보존하는 해'로 이동했다.",
        "points": [
            "2025 아키텍처 비교 리뷰(DeepONet·PCANet·FNO 계열)와 산업 규모 메시 적용으로 실무 구간에 진입했다.",
            "2025 Discovery of Unstable Singularities: ML과 고정밀 수치해석을 결합해 3D 오일러·Boussinesq 방정식의 불안정 특이점을 처음으로 체계 발견했다.",
            "2026 PINN 실패 모드를 계통 진단한다 — 기울기 병리, consistency barrier, 시간 얽힘.",
            "2026 구조 보존 연산자가 등장했다: Hodge 분해, 외미분, cochain 증명서.",
            "2026 연산자 학습이 역문제로 확장됐다 — 영상, 플라즈마, 중력파.",
        ],
        "sowhat": "'빠른 해'가 아니라 '보장 있는 해'로 경쟁축이 옮겨갔다. 기존 수치해석 인력이 가장 큰 자산이 되는 구간.",
    },
    "Latent Variable Generative Solvers": {
        "ko": "잠재변수 생성 솔버",
        "headline": "2025–2026 확산·흐름 매칭이 장기 롤아웃 안정성을 확보하며 PDE 계열을 가로질렀다.",
        "points": [
            "2025–2026 확산 사전분포를 PDE 제약·역물리 문제로 이식했다(PODiff, PIDDM).",
            "2026 흐름 매칭과 불균형 최적수송으로 집단·궤적 추론을 수행한다(WFR-MFM, Recursive Flow Matching).",
            "2026 Walrus 등 도메인 횡단 연속체 동역학 파운데이션 모델이 등장했다.",
            "2026 정준화(canonicalization)로 등변 아키텍처 없이도 대칭 분포를 학습한다.",
            "2026 메시 기반 시뮬레이션의 포트-해밀턴 정식화로 물리 보존을 구조에 넣는다.",
        ],
        "sowhat": "시뮬레이션을 대체하는 설계보다, 시뮬레이션의 사전분포로 쓰는 설계가 이긴다.",
    },
    "AI Foundation Models for Environmental Science": {
        "ko": "과학 파운데이션 모델과 통계 엄밀성",
        "headline": "2025–2026의 핵심은 새 모델이 아니라 통계 감사와 도메인 인프라다.",
        "points": [
            "2025 환경과학 파운데이션 모델 서베이와 AI4Science 준비도 벤치마크(AIRS-Bench, SciHorizon)가 지형을 정리했다.",
            "2026 통계 감사 물결: MMD/Stein 검정, knockoff 귀인, conformal 유효성, 벤치마크 무결성 진단.",
            "2026 도메인 인프라가 함께 깔린다 — IAEA Fusion Data Lake, 범용 원자간 퍼텐셜(MACE-Osaka26), 실시간 FPGA/GNN 트리거링.",
            "2024–2025 Virtual Lab·Spacer·LLM4SR이 'AI 과학자'를 운영 가능한 형태로 구현했다.",
            "2024 PathChat 같은 도메인 코파일럿이 실제 전문 업무에 진입했다.",
        ],
        "sowhat": "도입 기관은 모델보다 감사 파이프라인을 먼저 사야 한다. 감사 없는 파운데이션 모델은 비용이다.",
    },
    "Numerical Weather Forecasting Models": {
        "ko": "AI 수치예보·기후 모델",
        "headline": "2026년의 경쟁은 정확도가 아니라 확률·스펙트럼 충실도·자료동화다.",
        "points": [
            "2026 MOSAIC이 통계적 스펙트럼 감쇠·고주파 앨리어싱·잔차 누출을 동시에 교정하는 확률 예보를 제시했다.",
            "2026 U-Cast·ClimateAR로 확률·자기회귀 기후 예측이 확장됐다.",
            "2026 SENDAI는 1.56% 초희소 관측만으로 위성 NDVI 필드를 재구성하는 계층적 자료동화를 보여줬다.",
            "2026 파운데이션 모델 잔차 유도 다중해상도 정제로 가뭄을 예측한다 — 백본 동결, 추론시간 래퍼만으로.",
            "2026 지역 극한현상(태풍) 하이브리드 앙상블, 질량보존 기후 에뮬레이터, 물리–ML 해양·해빙 결합 모델.",
            "배경: 2022 Pangu-Weather가 운용 수치예보를 처음 상회했고 2023 GraphCast·FuXi가 중기 예보 동등성을 확보했다.",
        ],
        "sowhat": "기상·해양·재난 기관에 즉시 적용 가능한 성숙도다. 관건은 극한값 외삽의 독립 검증.",
    },
    "Offline Reinforcement Learning Robustness": {
        "ko": "물리 제어 RL 견고성·real-to-sim",
        "headline": "2025–2026, 문제는 정책 성능이 아니라 시뮬레이터 밖에서의 재현이다.",
        "points": [
            "2025 소프트 연속체 팔의 제로샷 sim-to-real 시각 서보잉이 실제 하드웨어에서 67% 성공률을 보고했다.",
            "2024–2025 OCT 유도 자율 혈관 문합 로봇(µSTAR)이 숙련 외과의와 경쟁 가능한 수준에 도달했다.",
            "2026 평형 제약 하 adjoint 학습으로 변형체 조작 같은 순차 암시적 계산 문제를 제어한다.",
            "제어 배리어 함수 기반 안전 보장과 오프라인 RL 견고성 평가가 이 분야의 두 축이다.",
        ],
        "sowhat": "자율 실험실의 마지막 1미터는 결국 제어 문제다. 국내 로봇·정밀기계 역량과 직접 붙는 지점.",
    },

    # ── Molecular Simulation and Generative Modeling ────────────────────────
    "Diffusion Model Reward Fine-tuning": {
        "ko": "확산모델 보상 미세조정",
        "headline": "2025–2026, 보상 미세조정은 '재학습 없는 추론시간 정렬'로 정리됐다.",
        "points": [
            "2025 SVDD가 미분 불가능한 보상에서도 재학습 없이 추론시간 정렬을 가능하게 했다.",
            "2025 VIDD는 가치 유도 반복 증류로 생물분자 설계용 확산모델을 안정적으로 미세조정한다.",
            "2025 테스트타임 반복 정제(부분 노이징 ↔ 보상 유도 디노이징)와 동적 빔 탐색이 단일샷 방식을 대체했다.",
            "2026 SGRPO·CRYSTAL 등 GRPO 계열로 결정·분자 생성기를 사후학습한다.",
            "2026 e-process 안전 입자 선택과 비용인지 베이지안 최적화 정지규칙 — 멈출 시점을 통계로 결정한다.",
        ],
        "sowhat": "보상 함수는 도메인 지식의 코드화다. 실험으로 측정 가능한 보상을 가진 팀이 이긴다.",
    },
    "Equivariant Force Field Symmetry": {
        "ko": "등변 힘장·기계학습 원자간 퍼텐셜",
        "headline": "2025–2026, 등변이 기본기가 된 순간 '정말 필요한가'라는 반론과 속도전이 시작됐다.",
        "points": [
            "2025–2026 MACE·NequIP·TensorNet·Orb-v3가 MLIP 기본 백본으로 정착했다.",
            "2026 어텐션 기반 장거리 MLIP(AllScAIP, RANGE)가 수작업 기하 귀납편향의 필요성에 도전한다.",
            "2026 IO 인지·확장 메시지 패싱 커널(FlashSchNet)로 GNN 분자동역학이 고전 힘장 속도권에 진입했다.",
            "2026 MeshTok은 적응 메시 세분화 발상으로 PDE 트랜스포머용 다중스케일 토큰화를 구현했다.",
            "2026 대칭성 원리가 양자오류정정 디코더로 수출됐다(translation-equivariant Cascade 디코더).",
        ],
        "sowhat": "계산화학 인프라 교체 시점이다. 사내에 쌓인 DFT 계산 데이터가 곧 자산이 된다.",
    },
    "Crystal Structure Generative Modeling": {
        "ko": "결정구조 생성 모델링",
        "headline": "2025–2026, 결정 생성은 '많이 만들기'에서 '맞는 분포를 만들기'로 옮겨갔다.",
        "points": [
            "2026 리만 흐름 매칭이 주기·분자 결정 생성의 기본기가 됐다(MolCrystalFlow, OrgFlow, MCFlow, DMFlow).",
            "2025–2026 LLM·Wyckoff 기호 생성에 선호 정렬을 결합했다(PLaID++, CrysTune, WyFormer).",
            "2026 MetaDNS가 well-tempered metadynamics로 이산 신경 샘플러의 모드 붕괴를 완화했다.",
            "2026 전원자 평형 분포를 직접 학습하는 생성 파운데이션 모델이 등장했다.",
            "2026 역문제 구조 규명으로 확장됐다 — Boltz-Jump, GLASS, CryoACE.",
            "배경: 2023 GNoME이 220만 개 신규 안정 결정 구조를 발견하며 후보 공간을 열배로 늘렸다.",
        ],
        "sowhat": "후보 목록 과잉 시대다. 합성 경로·독립 검증과 붙이지 않으면 종이 위 물질만 늘어난다.",
    },
    "ML Proxy Descriptor Evaluation": {
        "ko": "대리 서술자 검증·반증",
        "headline": "이 필드의 최대 기여는 새 모델이 아니라 자율 실험실 발견 주장을 반증한 재분석이다.",
        "points": [
            "2024 A-Lab의 신물질 43종 주장 재분석: Rietveld 정제 오류와 무질서 미고려로 실제 신규 물질은 없었다.",
            "2025 화학 파운데이션 모델 관점 논문이 MLIP·역설계 적용 범위를 정리했다.",
            "2025–2026 LLM 문헌 마이닝과 에이전트 역설계(MOF 코퍼스, COF용 Ara, 제올라이트 DiffSyn).",
            "2026 ELECTRAFI가 국소 가우시안의 닫힌 형태 푸리에 변환으로 주기 전하밀도를 즉시 예측한다.",
            "2026 서지 메타데이터에서 학습한 Clever-Hans 지름길 학습을 폭로한 연구가 평가 관행을 흔들었다.",
        ],
        "sowhat": "발견 주장에는 독립 재분석 예산을 붙여라. 반증할 수 있는 인력이 곧 신뢰 인프라다.",
    },
    "Molecular Thermodynamic Property Prediction": {
        "ko": "분자 물성·분광 검증",
        "headline": "사실상 전량 2026년 신생 분야 — 물성 예측이 '검증 계층'을 달고 재등장했다.",
        "points": [
            "2026 Peak Risk Score: 시뮬레이션-실험 스펙트럼 불일치를 확률로 채점하는 AI 과학자용 검증 계층.",
            "2026 문헌에서 추출한 미할당 스펙트럼 수백만 건을 순열불변 집합 지도학습으로 NMR 화학이동 예측에 활용한다.",
            "2026 MOES-Pred가 에너지 센티널 적응 노이즈와 BRICS 모티프 분해로 디노이징 사전학습을 개선했다.",
            "2026 DISSOLVR 같은 해석 가능한 비딥러닝 용해도 모델이 데이터 고유 잡음(aleatoric) 한계에 도달했다.",
            "2026 SYMGP와 확률적 재매개화로 대칭 제약·혼합변수 베이지안 최적화를 수행한다.",
        ],
        "sowhat": "AI 과학자 워크플로에 '실험 스펙트럼과 불일치하면 멈춤' 게이트를 넣는 설계가 핵심.",
    },

    # ── Agentic AI for Scientific Automation ────────────────────────────────
    "Scientific Tool-Using AI Agents": {
        "ko": "도구 사용 과학 에이전트",
        "headline": "2025–2026, 에이전트 경쟁력은 모델이 아니라 도구 카탈로그·프로토콜·과정 감사로 옮겨갔다.",
        "points": [
            "2025 표준 도구 생태계가 만들어졌다 — ToolUniverse 600+ 도구, Biomni-E1, TxAgent 211개 도구.",
            "2025 엔드투엔드 AI 과학자(AI Scientist-v2, Kosmos, DeepScientist, aiXiv)와 회의적 평가가 같이 나왔다.",
            "2025 DeepScientist는 발견을 베이지안 최적화로 정식화하고 누적 Findings Memory로 탐색–활용을 조절한다.",
            "2025 GeneAgent는 자기검증으로 환각을 잡아 GPT-4 대비 정확도를 끌어올렸다.",
            "2026 방정식·인과법칙 발견 에이전트와 과정 단위 벤치마크가 등장했다(SR-Scientist, PIEVO, MolQuest, OpenDiscoveryTrace).",
        ],
        "sowhat": "기관 도입 단위는 '모델 계약'이 아니라 '도구 레지스트리 + 감사 로그'다.",
    },
    "Autonomous Scientific Discovery Agents": {
        "ko": "자율 과학 발견 에이전트",
        "headline": "2025–2026, 성공 시연과 인식론적 반증이 같은 구간에 도착했다.",
        "points": [
            "2025 Agent Laboratory가 문헌조사–실험–보고 3단계를 자율 수행하며 비용을 84% 줄였다.",
            "2025 ScienceAgentBench·ScienceBoard·AFMBench가 자율 에이전트의 낮은 성공률을 드러냈다.",
            "2025 AstroAgents 등 도메인 다중 에이전트가 질량분석 데이터에서 가설을 자동 생성한다.",
            "2026 'AI scientists produce results without reasoning scientifically': 25,000회 이상 실행에서 증거 무시 68%.",
            "2026 에이전트 운영체제(SCION, EvoMaster)와 반증 중심 폐루프(POPPER 계열)가 대안으로 제시된다.",
        ],
        "sowhat": "'자율'을 사지 말고 '반증 루프'를 사라. 성공률보다 실패할 때 멈추는 능력이 중요하다.",
    },
    "Clinical LLM Applications": {
        "ko": "임상 LLM 응용",
        "headline": "2025–2026, 임상 LLM의 관문은 정확도가 아니라 유보(defer)와 검증이다.",
        "points": [
            "2025 Psyche가 다면 구성 기반 시뮬레이션 환자로 정신과 상담 에이전트를 윤리적·정량적으로 평가한다.",
            "2025 PatientSim·ClientCAST 등 환자·내담자 시뮬레이터가 평가 인프라로 자리 잡았다.",
            "2026 EHR·생리신호 파운데이션 모델과 경로 모델링이 확산됐다(PathwayLLM, EHR-FM 희소 오토인코더).",
            "2026 안전·환각 완화·적응 추론·유보 결정(MEDA, AdaThink-Med, ARQS, Act-or-Defer)이 핵심 주제가 됐다.",
            "2024–2025 AI 대화 에이전트의 심리적 위험을 경험 기반으로 유형화한 연구가 설계 지침을 제시했다.",
        ],
        "sowhat": "규제 진입 경로는 정확도가 아니라 유보(defer) 정책의 문서화다.",
    },
    "Multi-Agent Quantum Experiment Execution": {
        "ko": "장비·시설 자동화 에이전트",
        "headline": "2025–2026, 에이전트가 장비를 잡았다 — 큐비트 보정, 방사광 빔라인, 지구관측.",
        "points": [
            "2025 로봇 AI 화학자와 양자화학 에이전트가 실장비에 붙었다(ChemAgents, El Agente Q, QCopilot), AutoBio VLA 벤치마크도 등장.",
            "2025 Earth-Agent가 다중스펙트럼·지구관측 제품을 통합 처리하고 전문가 검증 248개 과제로 평가된다.",
            "2025 BehaveAgent는 재학습 없이 종을 가로질러 동물 행동을 제로샷 분석한다.",
            "2025–2026 시설 에이전트가 자리 잡는다 — Advanced Photon Source의 EAA, AI-native 가속기.",
            "2026 체화 발견 프레임워크와 벤치 수준 바이오보안 평가(Embodied Science PLAD, ENPIRE, ABC-Bench).",
            "배경: 2024 k-agents가 초전도 양자 프로세서를 자율 보정했다.",
        ],
        "sowhat": "방사광·중성자·핵융합 같은 국가 대형시설이 가장 빠른 국내 적용처다. 보안 평가를 동반해야 한다.",
    },
    "Multi-Agent Social Simulation": {
        "ko": "다중 에이전트 사회 시뮬레이션",
        "headline": "2025–2026, '에이전트를 더 붙이면 좋아지나'에 대한 정량 답이 나오기 시작했다.",
        "points": [
            "2025 Vending-Bench 등 장기 일관성 벤치마크가 다중 에이전트가 무너지는 지점을 드러냈다.",
            "2025 에이전트 시스템 스케일링 법칙: 도구 활용도·모델 능력·과제 특성의 상호작용으로 MAS 이득 조건을 정식화했다.",
            "2026 에이전트 신뢰성 과학이 일관성·견고성·예측가능성·안전 4축으로 문제를 분해한다.",
            "2026 다수결을 넘어선 집계 이론(Optimal Weight)과 YC-Bench류 신뢰성 벤치마크가 등장했다.",
        ],
        "sowhat": "다중 에이전트는 만능이 아니다. 단일 에이전트가 더 낫다는 근거가 이제 존재한다.",
    },

    # ── Formal Methods and Computational Reasoning ──────────────────────────
    "Higher-Order Logic Proof Systems": {
        "ko": "고차논리 형식 정리증명",
        "headline": "2026, 형식 증명은 저장소 규모 자동 형식화와 벤치마크 결함 감사로 넘어갔다.",
        "points": [
            "2026 M2F가 검증자 피드백 루프로 3주 만에 153,853줄 Lean 라이브러리를 자동 형식화했다.",
            "2026 에이전트형 증명기와 저장소 규모 형식화가 표준이 됐다(Goedel-Architect, LeanFlow, Numina-Lean-Agent).",
            "2026 벤치마크 무결성 감사가 시작됐다 — ProofGate, Ground False, 형식 벤치마크 결함 점검.",
            "2026 자연어 증명 검증을 비관적·의무 커버리지 판정으로 다룬다.",
            "배경: 2020 GPT-f의 Metamath 기여, 2021 miniF2F, 2024 DeepSeek-Prover의 Lean 4 합성 증명 800만 쌍.",
        ],
        "sowhat": "검증기가 있는 도메인은 자동화가 끝나간다. 이제 새 병목은 검증기 자체를 만드는 일이다.",
    },
    "Theoretical Complexity & Quantum Bounds": {
        "ko": "이론 한계·AI 조력 증명",
        "headline": "2025–2026, AI가 실제로 새 근사 한계와 반례를 생산하기 시작했다.",
        "points": [
            "2025 AlphaEvolve가 MAX-CUT·MAX-k-CUT·metric-TSP 근사 한계를 갱신했다.",
            "2026 GPT-5 Pro가 NICD-with-erasures에서 다수결 최적성에 대한 반례를 제시했다.",
            "2026 Gemini Deep Think 사례연구가 이론전산·경제학·최적화·물리 미해결 문제의 인간–AI 협업 기법을 일반화했다.",
            "2026 TTT-Discover는 테스트타임에 정책 자체를 RL로 계속 학습시켜 문제 특이적으로 개선한다.",
            "2026 기계 검증 이론(MerLean, Scarf-Brouwer-Nash, Lean 게임이론)과 양자 학습 한계(junta states, QAC0)가 함께 나왔다.",
        ],
        "sowhat": "'AI가 정리를 증명한다'는 이제 사례 문제다. 인간–AI 협업 프로토콜 자체가 산출물이 된다.",
    },
    "Symmetry-Aware PDE Solvers": {
        "ko": "대칭성 인지 솔버·방정식 발견",
        "headline": "2025–2026, LLM 기호회귀의 실제 천장이 숫자로 찍혔다 — 31.5%.",
        "points": [
            "2025 LLM-SRBench(4개 분야 239문제)는 암기 저항 설계에서 최고 모델 기호 정확도 31.5%를 보고했다.",
            "2025 CodePDE는 LLM이 PDE 솔버 코드를 직접 생성하는 추론 프레임워크를 제시했다.",
            "2025 DrSR은 데이터 구조 분석과 생성 이력을 함께 쓰는 이중 추론으로 기호회귀 정확도를 끌어올렸다.",
            "2025–2026 AutoNumerics·RAPNet이 학습된 AMG 보정 등 고전 수치기법과 접합한다.",
            "2026 통계·견고성 프로토콜이 붙었다 — ASyMOB, GeoRepEval, Holm-Bonferroni 솔버 검증.",
        ],
        "sowhat": "방정식 발견은 아직 보조 도구다. 다만 물리 제약을 붙이면 즉시 실무 가치가 나온다.",
    },
    "LLM-Assisted Structural Optimization": {
        "ko": "LLM 지원 구조·물리 설계 최적화",
        "headline": "2025–2026, 설계 루프에 시뮬레이터를 붙이자 주 단위 작업이 분 단위가 됐다.",
        "points": [
            "2025 다중 에이전트 자동차 설계가 스케치부터 공기역학 시뮬레이션까지 전 주기를 수 주에서 수 분으로 줄였다.",
            "2026 사전계산 수치 그린함수(PNGF)로 전자기 소자의 준실시간 전파 역설계가 가능해졌다.",
            "2026 물리 정렬 벤치마크가 나왔다 — BuildArena, Z3 SMT 검사를 붙인 CADEngBench.",
            "2026 리소그래피 세계모델과 GRPO 튜닝 흐름 매칭(LithoDreamer, LithoGRPO)이 반도체 공정으로 확장한다.",
            "배경: 2023 LMEA가 LLM을 진화 연산자로 썼고, 2024 GraphMetaMat이 GNN+RL+MCTS로 메타물질을 역설계했다.",
        ],
        "sowhat": "제조업 R&D에 가장 직접적인 서브카테고리다. 시뮬레이터 라이선스와 설계 데이터가 진입 조건.",
    },
    "LLM-Driven CFD Simulation Automation": {
        "ko": "LLM 주도 CFD·멀티피직스 자동화",
        "headline": "최소 규모(7편)인데 2025–2026 보고된 성공률은 이미 운용 가능 수준이다.",
        "points": [
            "2025 OpenFOAMGPT 2.0이 450회 이상 시뮬레이션에서 100% 성공을 보고했다.",
            "2025 MooseAgent가 FEM 입력파일 생성에서 93% 성공률을 달성했다.",
            "2025 MLLM 기반 VER가 비디오에서 내재 좌표계와 지배 방정식을 제로샷으로 발견한다.",
            "2026 TurboAgent가 조건부 확산 + 대체모델 + LLM 최적화 + 고충실도 CFD/FEA 검증으로 터보기계 설계 폐루프를 닫았다.",
            "2026 PhyNiKCE는 기호 지식엔진과 결정적 RAG로 물리 타당성을 강제한다.",
            "배경: 2024 MetaOpenFOAM이 자연어에서 전체 CFD 워크플로까지 다중 에이전트로 자동화했다.",
        ],
        "sowhat": "해석 엔지니어 한 명이 팀 규모 처리량을 갖는 구간이다. 사내 케이스 DB가 곧 해자.",
    },

    # ── Scientific Information Extraction and QA ────────────────────────────
    "Crosslingual Post-Training Methods": {
        "ko": "다국어 사후학습·백본 적응",
        "headline": "2025–2026, 사후학습 기술의 무게중심이 언어에서 생물·생체신호 백본으로 옮겨갔다.",
        "points": [
            "2026 증류·RL 메커니즘이 정교해졌다 — SEAD 엔트로피 유도 OPD, vOPD 통제변량, GRAIL 토큰 재가중 RLVR.",
            "2026 사후학습 기계가 도메인 파운데이션 모델로 이식된다(MEG-XL, NeuroCLUS, CalM, Ares, BioArc, ORA).",
            "2024–2025 오픈 프런티어 기준선이 세워졌다 — DeepSeek-V3(671B MoE, 토큰당 37B 활성), Qwen2.5, Gemma 2, Phi-4.",
            "배경: 2018 BERT, 2019 XLM-R(100개 언어·2TB), 2023 Toolformer·ToolLLM의 자기지도 도구 사용.",
        ],
        "sowhat": "한국어 과학 코퍼스 사후학습은 여전히 저비용·고효율 레버다. 백본을 새로 만들 필요는 없다.",
    },
    "Scientific Figure Caption Datasets": {
        "ko": "과학 도표·시각문서 이해",
        "headline": "2025–2026, 도표 이해는 '캡션 생성'에서 '무결성 검증과 도메인 통합'으로 이동했다.",
        "points": [
            "2024–2025 대학원 수준 멀티모달 과학 벤치마크가 자리 잡았다(MMSCI, SciFIBench, MatViX, ScImage).",
            "2024–2025 Figure Integrity Verification(EPM)이 도표 내 텍스트–시각 정렬을 검증한다 — 연구부정 탐지와 직결.",
            "2025 Paper2Poster·MLBCAP 등 논문→발표물 자동 변환이 실무 도구로 나왔다.",
            "2026 의료·지리공간 통합 비전-언어 모델로 선회했다(UniMedVL, SynerMedGen, MedSIGHT, UrbanMLLM, TimeSpot).",
            "배경: 2021 SciCap이 arXiv 200만 도표–캡션 쌍을, AutomaTikZ가 DaTikZ 120k를 공개했다.",
        ],
        "sowhat": "그림 검증은 연구 무결성 인프라다. 학회·출판사와의 협업 지점이 여기에 있다.",
    },
    "Automated Fact-Checking Systems": {
        "ko": "자동 주장 검증",
        "headline": "2025–2026, 검증은 멀티모달·코퍼스 규모·주장 수명주기 관리로 확장됐다.",
        "points": [
            "2025 DEFAME이 6단계 동적 파이프라인으로 텍스트+이미지 주장을 검증하고 설명 가능한 보고서를 생성한다.",
            "2025–2026 코퍼스 규모 주장 마이닝이 가능해졌다 — NSF-SciFy 280만 주장, SciClaimHunt 8.7만.",
            "2026 ClaimGarden 등 주장 상태 수명주기(claim lifecycle) 관리가 등장했다.",
            "2025 Claimify·CIBER 등 LLM 기반 주장 추출·검증 파이프라인이 정착했다.",
            "배경: 2021 MultiVerS, 2022 '반박 증거 부재' 비판, 2023 ProgramFC·HiSS·FactKG.",
        ],
        "sowhat": "AI 생성 과학이 늘수록 주장 단위 수명주기 추적이 필수 인프라가 된다.",
    },
    "Biomedical Knowledge Graph QA": {
        "ko": "생의학·임상 지식접지 QA",
        "headline": "2025–2026, 임상 QA 평가가 정확도에서 다국어 신뢰성 5축으로 확장됐다.",
        "points": [
            "2026 CLINIC이 15개 언어·18개 과제·28,800 샘플로 진실성·공정성·안전·견고성·프라이버시를 평가한다.",
            "2025 CLEAR가 임상 엔티티 기반 검색으로 토큰 사용을 70% 이상 줄였다 — 비용이 곧 임상 채택 조건.",
            "2025 IP-RAR·BioStrataKG가 딥싱킹 LLM과 RAG를 결합해 문서 간 추론 능력을 확보했다.",
            "2025–2026 ClinicalGPT-R1·LLMEval-Med·MedDocBench 등 도메인 모델과 의사 검증 평가 스위트가 나왔다.",
            "2026 EHR-RAGp·PACE-RAG 인구집단 사전지식과 MedREK 의료 지식 편집이 붙었다.",
        ],
        "sowhat": "한국어 임상 신뢰성 벤치마크가 없다는 건 국내 도입 심사의 근거가 없다는 뜻이다.",
    },
    "Retrieval-Augmented Generation Systems": {
        "ko": "RAG와 모호성 해소",
        "headline": "2025–2026, RAG의 남은 난제는 검색이 아니라 되묻기와 가설 생성이다.",
        "points": [
            "2025 가설 생성 서베이가 프롬프팅부터 프레임워크까지 과학 가설 생성 RAG를 분류하고 평가 전략을 정리했다.",
            "2025 HypoGeniC·ResearchLink가 데이터와 지식그래프 위에서 가설을 생성한다.",
            "2025 STORM·SurveyX가 사전작성(pre-writing)과 속성트리로 장문 서베이 자동화를 실용화했다.",
            "2024 RA-LLM 종합 서베이가 아키텍처·학습 전략·응용의 3관점으로 지형을 정리했다.",
            "배경: 2020 REALM, 2022 Atlas(11B가 540B 모델 상회), CLAM·LaMAI의 모호 질의 명료화.",
        ],
        "sowhat": "사내 RAG는 이미 상품이다. 차별화는 되묻기 정책과 인용 검증기에서 난다.",
    },

    # ── AI-Assisted Academic Scholarly Communication ────────────────────────
    "Academic Metadata & Causal Datasets": {
        "ko": "학술 메타데이터·연구 무결성 데이터",
        "headline": "2025–2026, 학술 인프라 데이터가 AI 저작 정책의 실증 근거가 됐다.",
        "points": [
            "2025 LLM이 생성한 연구 문서의 24%가 정교한 표절이며 내장 탐지기를 우회한다는 실증이 나왔다.",
            "2024–2025 WithdrarXiv가 arXiv 철회 논문 14,000편 이상을 모아 10범주 자동 분류체계를 만들었다.",
            "2025 CHIME·SurveyForge가 LLM 기반 계층적 문헌 조직화를 구현했다.",
            "2026 SPOT·MISSCIPLUS가 과학 오류·왜곡 검증 벤치마크를 제공한다.",
            "2026 AI 과학자 자율성 거버넌스 프레임워크(CRA, SciContrib-Bench)가 제안됐다.",
        ],
        "sowhat": "AI 저작 정책은 정서가 아니라 이 데이터로 설계해야 한다.",
    },
    "LLM-Assisted Peer Review Feedback": {
        "ko": "LLM 지원 동료심사",
        "headline": "2025–2026, 논쟁은 '허용할까'에서 '무엇을 검증하게 할까'로 넘어갔다.",
        "points": [
            "2025 Nature 보도가 AI의 동료평가 침투와 제도 가치 훼손 우려를 동시에 정리했다.",
            "2025 AgentRxiv가 공유 프리프린트 서버로 에이전트 간 발견을 누적 협업하게 만들었다.",
            "2025 AAAR-1.0이 방정식 추론·실험 설계·약점 식별·리뷰 비판 4과제로 연구 보조 능력을 평가한다.",
            "2025 MARG·OpenReviewer·REMOR·TreeReview 등 다중 에이전트·미세조정 리뷰어가 쏟아졌다.",
            "2026 검증 우선 입장 논문 — AI는 논문을 심판하지 말고 주장을 검증해야 한다.",
        ],
        "sowhat": "기관 정책 초안에 그대로 옮길 수 있는 근거 세트다. 심사 보조는 허용, 판정은 금지.",
    },
    "Scientific Hypothesis Recombination": {
        "ko": "과학 가설 재조합",
        "headline": "2025–2026, 평가 기준이 '새로운가'에서 '반증 가능한가'로 이동했다.",
        "points": [
            "2025 ResearchBench가 영감 검색·가설 구성·가설 순위로 발견 능력을 분해해 측정한다.",
            "2025 LLM을 진단 도구로 써서 과학·사회의 '불문율'을 명시적으로 드러내자는 제안이 나왔다.",
            "2025 MOOSE-Chem·SciMuse·HypoGen 등 가설 생성 프레임워크가 확산됐다.",
            "2026 NOVA-Test가 반증가능성 게이트를 건 가설 감사를 제시했다.",
            "2026 SciPaths·EO-Agents·PaperGym으로 발견 경로 예측과 훈련 환경화가 진행 중이다.",
        ],
        "sowhat": "'새롭다'는 평가지표를 '검증 가능하다'로 바꾸는 것이 다음 단계다.",
    },
    "Graph-Based Scientific Summarization": {
        "ko": "그래프 기반 과학 요약",
        "headline": "2025–2026, 요약의 쟁점은 압축률이 아니라 과잉 일반화다.",
        "points": [
            "2025 일반화 편향 감사: 10개 LLM·4,900개 요약에서 인간 대비 결론 과잉 확장이 확인됐다.",
            "2025 GLIMPSE·CGI2 등 메타리뷰 요약으로 심사 문서까지 대상이 확대됐다.",
            "2023–2025 SciReviewGen(리뷰 1만 편·인용논문 69만)이 문헌리뷰 자동생성 학습 기반을 제공한다.",
            "2026 HAESum·MoDeST 등 계층 구조를 활용한 요약 모델이 이어진다.",
            "배경: 2020 SciTLDR의 극단 요약과 CATTS 학습 전략.",
        ],
        "sowhat": "요약 자동화를 도입하려면 '결론 범위 확장' 감지기를 함께 넣어야 한다.",
    },
    "Citation Context Recommendation": {
        "ko": "인용 문맥 추천·검증",
        "headline": "2025–2026, 인용 생성이 쉬워진 만큼 인용 환각 탐지가 본론이 됐다.",
        "points": [
            "2025 ScholarCopilot이 검색을 글쓰기에 통합해 인용과 문장을 함께 생성한다.",
            "2025 SciRGC가 인용 의도 인식과 인용 네트워크로 다단계 추천·문장 정렬을 구현했다.",
            "2026 CiteCheck이 LLM 인용 환각을 탐지하고, MIRAI가 인용 영향력을 예측한다.",
            "2024 CiteBART가 인용 토큰 마스킹 사전학습으로 로컬 인용 추천을 생성형으로 전환했다.",
            "배경: 2022 RL 기반 제어 가능 인용문 생성, 2023 Cited Text Span 접지.",
        ],
        "sowhat": "글쓰기 도구에 인용 검증기를 기본 탑재하지 않으면 그대로 기관 리스크가 된다.",
    },
}


# ── 데이터 로딩 ────────────────────────────────────────────────────────────
def load_corpus(topic):
    tdir = get_topic_dir(topic)

    def read(name, root=None):
        p = (root or tdir) / name
        if not p.exists():
            raise SystemExit(f"[ERROR] 필요한 파일이 없습니다: {p}")
        return json.loads(p.read_text(encoding="utf-8"))

    summaries = read("_category_summaries.json")
    classification = read("_new_classification.json")
    timeline = read("_timeline_narrative.json")
    ins_path = tdir / "_insights.json"
    insights = json.loads(ins_path.read_text(encoding="utf-8")) if ins_path.exists() else {}
    index = read("_papers_index.json", root=Path(PAPERS_DIR))
    recount_categories(summaries, classification)
    return summaries, classification, timeline, insights, index


def recount_categories(summaries, classification):
    """`_category_summaries.json` 의 편수를 `_new_classification.json` 으로 다시 센다.

    요약본은 build_category_summaries.py 가 돌던 시점의 스냅샷이라 이후 신규 논문이
    반영되지 않는다(ai4s: 2,644 → 2,658 로 14편 누락). 여기서 두 기준을 함께 채운다.

    * `count`      — primary_category 기준 '고유 배정' 편수. 8개 대분류를 더하면
                     코퍼스 크기와 정확히 같다. 서브카테고리 커버리지 산술의 분모.
    * `card_count` — all_categories 기준 '중복 배정 포함' 편수. 토픽 인덱스
                     (`build_topic_index.py`) 의 카테고리 헤더 편수와 같은 값 —
                     사이트는 논문을 배정된 모든 카테고리에 카드로 노출한다.
    """
    primary, cards, subs = Counter(), Counter(), Counter()
    for a in classification.get("assignments", []):
        pcat = a.get("primary_category")
        primary[pcat] += 1
        subs[(pcat, a.get("sub_category"))] += 1
        for cat in (a.get("all_categories") or [pcat]):
            cards[cat] += 1
    for c in summaries:
        cat = c.get("category")
        if cat in primary:
            c["count"] = primary[cat]
        c["card_count"] = cards.get(cat, c.get("count", 0))
        for st in c.get("sub_themes", []):
            key = (cat, st.get("name"))
            if key in subs:
                st["count"] = subs[key]


_STOP = {"and", "the", "of", "for", "in", "a", "amp", "with", "on", "to", "via", "using"}
_TITLE_STOP = {"large", "language", "model", "models", "learning", "deep", "neural", "based",
               "towards", "scientific", "science", "data", "analysis", "generative", "using",
               "prediction", "framework", "network", "networks", "benchmark", "evaluation"}


def _tokens(text):
    return {t for t in re.findall(r"[a-z0-9]+", (text or "").lower())
            if t not in _STOP and len(t) > 2}


def match_timeline(analyses, category, name):
    """서브카테고리 이름은 요약본과 타임라인 내러티브에서 다르게 붙을 수 있다.
    토큰 겹침 비율이 가장 높은 항목을 고르고 0.4 미만이면 매칭 실패로 본다."""
    best, best_score = None, 0.0
    want = _tokens(name)
    for st in (analyses.get(category) or {}).get("sub_themes", []):
        score = len(want & _tokens(st.get("name"))) / max(1, len(want))
        if score > best_score:
            best, best_score = st, score
    return best if best_score >= 0.4 else None


def year_of(date_str):
    m = re.match(r"(\d{4})", str(date_str or ""))
    return int(m.group(1)) if m else 0


def ref_keys(paper, tools):
    """본문 불릿에 [n] 마커를 달 때 쓰는 '식별 가능한 고유명' 집합.

    오귀속을 막기 위해 (1) 제목에 처음 등장하는 시스템명(headword) 하나와
    (2) 제목에 실제로 등장하는 대표 도구명(5자 이상)만 인정한다.
    'AlphaFold2' 같은 범용 모델명이 다른 논문 제목에 섞여 있다는 이유로
    엉뚱한 불릿에 마커가 붙는 것을 막는다."""
    title = paper.get("title") or ""
    keys = set()
    for tok in re.findall(r"[A-Za-z][A-Za-z0-9]*(?:[-–][A-Za-z0-9]+)*", title):
        if (len(tok) >= 4 and tok.lower() not in _TITLE_STOP
                and (sum(1 for ch in tok if ch.isupper()) >= 2 or any(ch.isdigit() for ch in tok))):
            keys.add(tok)
            break
    for t in tools:
        if len(t) >= 5 and re.search(r"(?<![A-Za-z0-9])" + re.escape(t) + r"(?![A-Za-z0-9])",
                                     title, re.I):
            keys.add(t)
    return keys


def clean_title(title):
    """제목에 남은 LaTeX·마크다운 잔여물을 표시용으로 정리한다."""
    t = re.sub(r"\$?\\(?:texttt|textbf|textit|emph|mathrm|mathbf)\{([^}]*)\}\$?", r"\1", title or "")
    t = t.replace("$", "").replace("\\", "")
    t = re.sub(r"\*\*(.+?)\*\*", r"\1", t)
    return re.sub(r"\s+", " ", t).strip()


def title_fingerprint(title):
    """같은 논문이 두 슬러그로 들어온 경우를 걸러내기 위한 정규화 키."""
    return re.sub(r"[^a-z0-9]", "", clean_title(title).lower())[:60]


def title_phrase_hit(paper, text):
    """불릿이 논문 제목을 그대로 부르는지 검사한다(앞 4단어, 18자 이상일 때만)."""
    words = clean_title(paper.get("title")).split()
    if len(words) < 3:
        return False
    phrase = " ".join(words[:4]).rstrip(":,.")
    if len(phrase) < 18:
        return False
    return re.search(re.escape(phrase), text, re.I) is not None


def make_ref(paper, link_base):
    slug = paper.get("slug") or ""
    essence = clean_title(re.sub(r"\s+", " ", paper.get("essence") or "")).strip()
    if len(essence) > 135:
        essence = essence[:134].rstrip() + "…"
    authors = paper.get("authors") or []
    author = (authors[0] + " 외") if len(authors) > 1 else (authors[0] if authors else "")
    return {
        "slug": slug,
        "title": clean_title(paper.get("title")),
        "author": author,
        "date": str(paper.get("date") or ""),
        "year": str(paper.get("date") or "")[:4],
        "citations": paper.get("citation_count") or 0,
        "essence": essence,
        "url": f"{link_base}/{slug}/index.html" if slug else "",
        "doi": paper.get("doi") or "",
    }


def pick_papers(papers, tools, keywords, link_base, limit=4, since=2025):
    """대표 논문 선정. (1) 2025년 이후 우선 (2) 대표 도구·키워드가 제목에 있는 것
    (3) 피인용수 (4) 리뷰 점수 (5) 최신순."""
    probes = [t.lower() for t in tools if len(t) >= 4]
    probes += [w.lower() for w in keywords if len(w) >= 5]

    def key(p):
        title = (p.get("title") or "").lower()
        hit = sum(1 for probe in probes if probe in title)
        y = year_of(p.get("date"))
        return (0 if y >= since else 1, -min(hit, 3), -(p.get("citation_count") or 0),
                -(p.get("score") or 0), -y)

    out, seen = [], set()
    for p in sorted(papers, key=key):
        fp = title_fingerprint(p.get("title"))
        if fp in seen:
            continue
        seen.add(fp)
        out.append(make_ref(p, link_base))
        if len(out) >= limit:
            break
    return out


def _key_pattern(key):
    """단복수 차이(PINNs↔PINN)까지만 흡수하는 단어 경계 패턴."""
    base = key[:-1] if (len(key) > 4 and key.endswith("s")) else key
    return r"(?<![A-Za-z0-9])" + re.escape(base) + r"s?(?![A-Za-z0-9])"


def attach_markers(points, refs, tools):
    """불릿에 등장하는 고유명(또는 제목 그대로의 호명)이 대표 논문과 일치할 때만 [n] 을 붙인다."""
    keysets = [ref_keys({"title": r["title"]}, tools) for r in refs]
    out = []
    for text in points:
        hits = []
        for i, (keys, ref) in enumerate(zip(keysets, refs), start=1):
            if any(re.search(_key_pattern(k), text, re.I) for k in keys) \
                    or title_phrase_hit({"title": ref["title"]}, text):
                hits.append(i)
        out.append(text + "".join(f"[{i}]" for i in hits))
    return out


# ── 슬라이드 조립 ──────────────────────────────────────────────────────────
def build_slides(topic, summaries, classification, timeline, insights, index,
                 per_category=5, link_base="../../docs/papers", since=2025):
    assigned = {a["slug"]: a for a in classification.get("assignments", [])}
    idx_by_slug = {p["slug"]: p for p in index}
    papers = [idx_by_slug[s] for s in assigned if s in idx_by_slug]

    by_prefix = {}
    for p in index:
        by_prefix.setdefault(p["slug"].split("_")[0], p)

    by_sub = defaultdict(list)
    for slug, a in assigned.items():
        p = idx_by_slug.get(slug)
        if p:
            by_sub[(a.get("primary_category"), a.get("sub_category"))].append(p)

    years = Counter()
    for p in papers:
        y = year_of(p.get("date"))
        if 2015 <= y <= 2030:
            years[y] += 1

    analyses = timeline.get("category_analyses", {})
    cats = sorted(summaries, key=lambda c: -c.get("count", 0))
    total = len(papers)
    recent_share = round(sum(v for y, v in years.items() if y >= since) / max(1, total) * 100)
    cards_total = sum(c.get("card_count", 0) for c in cats)

    slides = []

    def add(**kw):
        kw["no"] = len(slides) + 1
        kw.setdefault("refs", [])
        slides.append(kw)
        return kw

    trend = " → ".join(f"{y}년 {years[y]:,}편" for y in sorted(y for y in years if y >= 2023))
    n_subs = sum(len(c.get("sub_themes", [])) for c in cats)

    # ── S01–S05 오프닝 ─────────────────────────────────────────────────────
    add(kind="표지", part="오프닝",
        title_ko="AI for Science, 2026년 지형도",
        title_en=f"{total:,}편 코퍼스가 말하는 8개 지형과 {len(cats) * per_category}개 최전선",
        headline="논문 한 편씩 읽어서는 보이지 않는 것 — 어디에 사람이 몰렸고, 어디가 비었는가.",
        points=[
            f"대상 코퍼스: **{topic}** 토픽 {total:,}편(리뷰 완료 전수). 사례는 **{since}년 이후를 우선**해 골랐다.",
            f"구조: 대분류 {len(cats)}개 · 서브카테고리 {n_subs}개 → 편수 상위 {per_category}개씩 총 {len(cats) * per_category}장.",
            f"연도 분포: {trend}. 전체의 **{recent_share}%가 {since}년 이후** 논문이다.",
            "슬라이드 1장 = 서브카테고리 1개. 규모·기간·상태·대표 도구·대표 논문·시사점을 한 화면에.",
            "각 슬라이드 하단 레퍼런스는 코퍼스의 **논문별 리뷰 문서로 바로 연결**된다.",
        ],
        sowhat="이 덱의 목적은 요약이 아니라 배치다. 우리가 어디에 설 것인지 정하기 위한 지도.")

    add(kind="방법", part="오프닝",
        title_ko="이 지도는 어떻게 만들어졌나",
        title_en="Method — SPECTER2 · UMAP · HDBSCAN · c-TF-IDF",
        headline="사람이 카테고리를 먼저 정하지 않았다. 논문이 뭉친 모양에서 카테고리를 꺼냈다(bottom-up).",
        points=[
            "임베딩: SPECTER2(논문 특화)로 전 논문을 벡터화 → UMAP 5차원 축소 → HDBSCAN 밀도 클러스터링.",
            f"미세 클러스터를 c-TF-IDF로 키워드화하고 LLM이 명명 → 서브카테고리 {n_subs}개 → 대분류 {len(cats)}개로 그룹핑.",
            "각 논문은 primary_category 1개 + all_categories 최대 3개를 가진다(다중 배정).",
            f"편수는 두 기준으로 센다 — **고유 배정**(primary 1편=1칸, 8개 합 {total:,}편)과 "
            f"**중복 포함**(all_categories, 8개 합 {cards_total:,}편). "
            "웹 인덱스의 카테고리 헤더 편수는 중복 포함 기준이고, 이 덱의 커버리지 산술은 고유 배정 기준이다.",
            "시기(start–end)·상태(가속/안정/부상/감소)·대표 도구는 카테고리별 타임라인 분석에서 가져왔다.",
            "한계 1: 편수는 '연구 관심의 밀도'이지 '중요도'가 아니다. 작지만 결정적인 칸이 있다(S35 CFD 자동화 7편).",
            "한계 2: 코퍼스는 주간 신규 수집 기반이라 최신 편향이 있다. 그래서 '누적 지식'이 아니라 '현재 전선' 지도로 읽어야 한다.",
        ],
        sowhat="분류가 흔들리면 결론도 흔들린다. 그래서 방법을 먼저 밝힌다.")

    ymax = max(years.values()) if years else 1
    add(kind="코퍼스", part="오프닝",
        title_ko="코퍼스 한눈에 보기",
        title_en="Corpus at a glance",
        headline=f"{total:,}편 중 {years.get(2026, 0):,}편이 2026년 논문. 지금 벌어지는 일을 보고 있다.",
        table={"head": ["연도", "편수", ""],
               "rows": [[str(y), f"{years[y]:,}편", "█" * max(1, round(years[y] / ymax * 30))]
                        for y in sorted(years) if y >= 2018]},
        points=[
            f"2023년 이후 급증 — {trend}.",
            f"{since}년 이후 논문이 전체의 {recent_share}%. 이 덱이 2025+ 사례 중심인 이유다.",
            "2018년 이전 소수 논문(BERT·Neural ODE·PINN)은 전 카테고리가 인용하는 뿌리 노드라 '배경'으로만 등장시킨다.",
            "피인용 데이터는 일부 논문에만 붙어 있다(최신 논문 다수는 아직 인용 이력 없음) — 편수와 인용은 따로 읽어야 한다.",
        ],
        sowhat="전략 판단에는 '현재 전선' 지도가 오히려 유리하다. 다만 고전의 부재를 결론으로 착각하면 안 된다.")

    add(kind="지형도", part="오프닝",
        title_ko="8개 대분류 지형도",
        title_en="The eight territories",
        headline="'만드는 연구'(신약·신소재)와 '재는 연구'(평가·벤치마크)가 나란히 1·2위. 이 조합이 2026년의 성격이다.",
        table={"head": ["대분류", "고유 배정", "중복 포함", "서브카테고리", "최대 서브카테고리"],
               "rows": [[CATEGORY_KO.get(c["category"], c["category"]), f"{c.get('count', 0):,}",
                         f"{c.get('card_count', 0):,}",
                         str(len(c.get("sub_themes", []))),
                         (sorted(c.get("sub_themes", []), key=lambda s: -s.get("count", 0))[0]["name"]
                          if c.get("sub_themes") else "-")]
                        for c in cats]},
        points=[
            "규모 상위 3개(신약·신소재, LLM 평가, 물리·환경)가 전체의 절반을 넘는다.",
            "가장 작은 학술 커뮤니케이션 카테고리는 편수는 적지만 기관 정책에 가장 직접적인 근거를 준다.",
            "이후 8개 파트는 이 순서(편수 내림차순)로 진행한다.",
        ],
        sowhat="예산 배분에서 편수는 출발점일 뿐이다. 파트마다 '우리에게 무엇인가'를 따로 달아 뒀다.")

    add(kind="서사", part="오프닝",
        title_ko="관통하는 한 줄: 예측 → 설계 → 자율 → 검증",
        title_en="The 2026 reliability and verification turn",
        headline="2025–2026 코퍼스를 관통하는 흐름은 새 모델이 아니라 '신뢰성·검증 전환'이다.",
        points=[
            "**예측(–2021, 배경)**: BioBERT·SciBERT가 계산 기반을, PINN·Neural ODE가 미분방정식 학습을, AlphaFold2가 구조 예측을 끝냈다.",
            "**설계(2022–2023, 배경)**: ProteinMPNN·RFdiffusion, Pangu-Weather·GraphCast가 운용 수치예보를 넘었고 A-Lab·Coscientist가 LLM을 실험 장비에 붙였다.",
            "**자율(2024–2025)**: AI Scientist·Virtual Lab·Agent Laboratory가 폐루프를 시연했지만, ScienceAgentBench·LLM-SRBench(31.5%)가 주장과 실제의 간극을 드러냈다.",
            "**검증(2026)**: 벤치마크 감사, PINN 실패 모드 진단, ProofGate류 형식 벤치마크 결함 점검, 희소 오토인코더 해석성, 예측기반 추론, 출처·기여 추적이 동시에 부상했다.",
            "즉 2026년은 '무엇을 더 할 수 있나'가 아니라 '무엇을 믿을 수 있나'를 묻는 해다.",
        ],
        sowhat="지금 투자할 것은 '더 센 모델'이 아니라 '감사 가능한 폐루프'다. 이 문장이 뒤 45장의 요약이다.")

    # ── S06–S45 카테고리별 서브카테고리 ────────────────────────────────────
    for ci, c in enumerate(cats, start=1):
        cat = c["category"]
        cat_ko = CATEGORY_KO.get(cat, cat)
        part = f"제{ci}부 · {cat_ko}"
        subs = sorted(c.get("sub_themes", []), key=lambda s: -s.get("count", 0))[:per_category]
        covered = sum(s.get("count", 0) for s in subs)
        share = round(covered / max(1, c.get("count", 1)) * 100)
        for si, st in enumerate(subs, start=1):
            name = st.get("name")
            tl = match_timeline(analyses, cat, name)
            nar = NARRATIVE.get(name, {})
            tools = (tl or {}).get("representative_tools", []) or []
            kds = [re.sub(r"\s+", " ", k) for k in ((tl or {}).get("key_developments") or [])]
            points = nar.get("points") or kds
            if not points:
                ko = re.sub(r"\s+", " ", st.get("description_ko") or "")
                points = [ko[:300] + ("…" if len(ko) > 300 else "")]
            # 본문에서 실제로 언급한 시스템명을 최우선 탐침으로 써서,
            # 슬라이드가 말하는 논문이 레퍼런스에 실리도록 한다.
            named = [w for w in re.findall(r"[A-Za-z][A-Za-z0-9]*(?:[-–][A-Za-z0-9]+)*",
                                           " ".join(points))
                     if len(w) >= 4 and (sum(1 for ch in w if ch.isupper()) >= 2
                                         or any(ch.isdigit() for ch in w))]
            probes = named + list(_tokens(name)) + [w for k in kds
                                                    for w in re.findall(r"[A-Z][A-Za-z0-9\-]{3,}", k)]
            pool = by_sub.get((cat, name), [])
            refs = pick_papers(pool, tools, probes, link_base, since=since)
            # 불릿이 논문 제목을 그대로 부르는 경우(예: 'Discovery of Unstable Singularities')
            # 해당 논문을 레퍼런스 맨 앞에 강제로 싣는다.
            body = " ".join(points)
            forced = [p for p in pool if title_phrase_hit(p, body)]
            if forced:
                seen = set()
                merged = []
                for r in [make_ref(p, link_base) for p in forced] + refs:
                    fp = title_fingerprint(r["title"])
                    if fp in seen:
                        continue
                    seen.add(fp)
                    merged.append(r)
                refs = merged[:max(4, len(forced) + 3)]
            n_recent = sum(1 for p in by_sub.get((cat, name), []) if year_of(p.get("date")) >= since)
            badges = [f"{st.get('count', 0)}편"]
            if tl:
                badges += [f"{tl.get('start')}–{tl.get('end')}", STATUS_KO.get(tl.get("status"), "")]
            badges.append(f"{since}+ {n_recent}편")
            add(kind="서브카테고리", part=part, category=cat, category_ko=cat_ko,
                position=f"{si}/{len(subs)}",
                title_ko=nar.get("ko") or name,
                title_en=name,
                alias_en=((tl or {}).get("name") if (tl and tl.get("name") != name) else ""),
                badges=[b for b in badges if b],
                context=(CATEGORY_LEAD.get(cat, "") if si == 1 else ""),
                cat_meta=(f"{cat_ko} 고유 배정 {c.get('count', 0):,}편"
                          f"(중복 포함 {c.get('card_count', 0):,}편 · 웹 인덱스 기준) · 서브카테고리 "
                          f"{len(c.get('sub_themes', []))}개 · 본 파트 {len(subs)}개로 {share}% 커버"
                          if si == 1 else ""),
                headline=nar.get("headline") or "",
                points=attach_markers(points, refs, tools),
                tools=tools, refs=refs,
                sowhat=nar.get("sowhat") or "")

    # ── S46–S50 종합 ───────────────────────────────────────────────────────
    cross = insights.get("cross_category", []) or []
    by_type = defaultdict(list)
    for item in cross:
        by_type[item.get("type")].append(item)
    meta = insights.get("meta", {}) or {}

    def insight_refs(items, limit=5):
        pool = []
        for it in items:
            for ev in it.get("evidence", []):
                p = by_prefix.get(str(ev))
                if p:
                    pool.append(p)
        seen, uniq = set(), []
        for p in sorted(pool, key=lambda p: (0 if year_of(p.get("date")) >= since else 1,
                                             -year_of(p.get("date")),
                                             -(p.get("citation_count") or 0))):
            if p["slug"] in seen:
                continue
            seen.add(p["slug"])
            uniq.append(make_ref(p, link_base))
            if len(uniq) >= limit:
                break
        return uniq

    def refs_by_names(names, limit=6):
        """본문이 지목한 시스템명을 코퍼스 제목에서 직접 찾아 레퍼런스로 만든다."""
        picked, seen = [], set()
        for nm in names:
            pat = re.compile(r"(?<![A-Za-z0-9])" + re.escape(nm) + r"(?![A-Za-z0-9])", re.I)
            hits = [p for p in papers if pat.search(p.get("title") or "")]
            hits.sort(key=lambda p: (0 if year_of(p.get("date")) >= since else 1,
                                     -(p.get("citation_count") or 0), -year_of(p.get("date"))))
            for p in hits[:1]:
                if p["slug"] not in seen:
                    seen.add(p["slug"])
                    picked.append(make_ref(p, link_base))
            if len(picked) >= limit:
                break
        return picked

    def insight_points(items):
        return [f"**{it.get('title')}** ({' × '.join(CATEGORY_KO.get(x, x) for x in it.get('categories', []))}) "
                f"— {it.get('description')}" for it in items]

    conv = by_type.get("convergence", [])
    add(kind="종합", part="종합",
        title_ko="수렴 신호: 경계가 무너지는 곳",
        title_en="Convergence signals",
        headline="서로 다른 카테고리가 같은 문제를 풀기 시작하면, 그 지점이 다음 3년의 표준이 된다.",
        points=insight_points(conv),
        extra={"정책 함의": [it.get("policy_implication") for it in conv if it.get("policy_implication")]},
        refs=insight_refs(conv),
        sowhat="세 수렴 모두 '인프라 + 표준'을 요구한다. 개별 모델 도입으로는 따라갈 수 없는 층이다.")

    rise, fall = by_type.get("emerging", []), by_type.get("declining", [])
    add(kind="종합", part="종합",
        title_ko="부상과 쇠퇴",
        title_en="What is rising, what is fading",
        headline="단독 LLM으로 과학하겠다는 접근은 접히는 중이고, 그 자리를 신경-기호와 추론시간 확장이 채운다.",
        points=(["**부상 —**"] + insight_points(rise) + ["**쇠퇴 —**"] + insight_points(fall)),
        extra={"정책 함의": [it.get("policy_implication") for it in rise + fall if it.get("policy_implication")]},
        refs=insight_refs(rise + fall),
        sowhat="쇠퇴 신호를 읽는 쪽이 더 돈이 된다. '순수 LLM 과학 발견' 과제는 지금 시작하면 늦다.")

    gaps = by_type.get("gap", [])
    add(kind="종합", part="종합",
        title_ko="비어 있는 자리",
        title_en="Gaps and underserved domains",
        headline="가장 큰 공백은 기술이 아니다 — AI가 만든 과학을 검증할 체계가 없다.",
        points=insight_points(gaps) + ["**미개척 영역** — " + x for x in (meta.get("underserved_domains") or [])],
        refs=insight_refs(gaps),
        sowhat="공백은 곧 진입 지점이다. 검증·감사·형평성 영역은 후발 주자가 표준을 선점할 수 있는 몇 안 되는 자리.")

    add(kind="종합", part="종합",
        title_ko="2026 검증 전환의 여섯 축",
        title_en="Six axes of the verification turn",
        headline="같은 해에, 서로 모르는 여덟 개 분야가 같은 결론에 도달했다 — 성능이 아니라 증거.",
        points=[
            "**벤치마크 감사** — ProtDBench·GENEB·ProofGate·Ground False: 벤치마크 자체의 결함을 검사한다 (S07·S08·S31).",
            "**실패 모드 진단** — PINN 기울기 병리·consistency barrier, A-Lab 신물질 주장 재분석 (S16·S24).",
            "**기계적 해석성** — 희소 오토인코더, cross-layer transcoder, AlphaInterp (S06·S09).",
            "**통계적 인증** — 예측기반 추론(PPI), conformal 유효성, knockoff 귀인, 등가 검정 (S14·S18).",
            "**출처·기여 추적** — WithdrarXiv·CreditMap·DataJoint 계열 프로비넌스 인프라 (S41).",
            "**검증 우선 규범** — 'AI는 논문을 심판하지 말고 주장을 검증하라', 반증가능성 게이트 NOVA-Test (S42·S43).",
        ],
        refs=refs_by_names(["ProtDBench", "ProofGate", "AlphaInterp", "WithdrarXiv",
                            "NOVA-Test", "GENEB", "CELEUS"]),
        sowhat="이 여섯 축은 그대로 조직의 체크리스트가 된다. 도입 검토서 양식으로 바로 옮길 수 있다.")

    add(kind="마무리", part="종합",
        title_ko="그래서 무엇을 할 것인가",
        title_en="Where to stand",
        headline="따라잡기 경쟁은 이미 졌다. 이길 수 있는 자리는 검증·도메인 데이터·대형시설이다.",
        points=[
            "**검증 인프라를 산다** — 모델 도입 예산의 일정 비율을 독립 재현·감사에 고정 배정한다(근거: S24 A-Lab 재분석, S27 증거 무시 68%).",
            "**도메인 데이터가 해자다** — 섭동 스크린(S06), DFT 계산(S22), 사내 CFD 케이스(S35), 임상 노트(S28). 백본은 사 오고 데이터로 이긴다.",
            "**대형시설이 가장 빠른 적용처다** — 방사광·중성자·핵융합 장비 에이전트(S29)는 국내 즉시 실행 가능.",
            "**한국어·한국 도메인 벤치마크 부재를 메운다** — 없으면 도입 심사 근거 자체가 없다(S10·S39).",
            "**정책 문서는 이미 근거가 충분하다** — 심사 보조 허용·판정 금지, 인용 검증기 의무화(S42·S45).",
        ],
        extra={"관전 포인트 (다음 12개월)": [
            "자율 에이전트의 습식 검증 성공률이 공개 벤치마크에서 재현되는가",
            "형식 검증기가 수학 밖(재료·코드·회로)으로 얼마나 확장되는가",
            "AI 수치예보의 극단 이벤트 외삽에 대한 독립 검증 결과",
            "AI 생성 논문·리뷰에 대한 학회·출판사 표준의 성립 여부",
        ]},
        sowhat="이 덱의 근거는 전부 코퍼스에 있다. 각 슬라이드 레퍼런스에서 논문 리뷰 원문으로 바로 내려갈 수 있다.")

    return slides, {"total": total, "categories": cats, "years": years, "n_subs": n_subs,
                    "per_category": per_category, "since": since,
                    "recent_share": recent_share, "link_base": link_base}


# ── 렌더링: Markdown (Obsidian) ────────────────────────────────────────────
def render_markdown(topic, slides, stats):
    today = datetime.now().strftime("%Y-%m-%d")
    L = ["---",
         f'title: "AI for Science 지형도 — 발표 슬라이드 원고 {len(slides)}장"',
         f"topic: {topic}",
         f"slides: {len(slides)}",
         f"corpus_papers: {stats['total']}",
         f"evidence_since: {stats['since']}",
         f"generated: {today}",
         "tags:"]
    L += [f"  - {t}" for t in ("ai4science", "슬라이드", "연구동향", topic)]
    L += ["---", "",
          f"# AI for Science 지형도 — 슬라이드 원고 {len(slides)}장", "",
          f"> [!info] 개요\n"
          f"> 코퍼스 **{stats['total']:,}편** · 대분류 **{len(stats['categories'])}개** · "
          f"서브카테고리 **{stats['n_subs']}개** 중 편수 상위 **{stats['per_category']}개씩**.\n"
          f"> 슬라이드 1장 = 서브카테고리 1개(`S06`–`S45`). 사례는 **{stats['since']}년 이후 우선**"
          f"(코퍼스의 {stats['recent_share']}%).\n"
          f"> 레퍼런스 링크는 각 논문의 리뷰 문서(`{stats['link_base']}/<slug>/index.html`)로 연결된다.",
          "", "## 목차", ""]
    cur = None
    for s in slides:
        if s["part"] != cur:
            cur = s["part"]
            L.append(f"- **{cur}**")
        badge = f" — {s['badges'][0]}" if s.get("badges") else ""
        L.append(f"    - `S{s['no']:02d}` {s['title_ko']}{badge}")
    L.append("")

    for s in slides:
        L += ["---", "", f"## S{s['no']:02d} · {s['title_ko']}", ""]
        meta = [f"*{s['part']}*"]
        if s.get("title_en"):
            meta.append(f"**{s['title_en']}**")
        meta.append(f"*{s['kind']}*")
        L.append(" · ".join(meta))
        if s.get("alias_en"):
            L += ["", f"<sub>타임라인 분석 명칭: {s['alias_en']}</sub>"]
        if s.get("badges"):
            L += ["", " ".join(f"`{b}`" for b in s["badges"])]
        if s.get("cat_meta"):
            L += ["", f"<sub>{s['cat_meta']}</sub>"]
        L.append("")
        if s.get("context"):
            L += [f"> [!quote] 파트 도입\n> {s['context']}", ""]
        if s.get("headline"):
            L += [f"> [!abstract] 핵심 메시지\n> {s['headline']}", ""]
        if s.get("table"):
            head = s["table"]["head"]
            L.append("| " + " | ".join(head) + " |")
            L.append("|" + "|".join(["---"] * len(head)) + "|")
            L += ["| " + " | ".join(str(x) for x in row) + " |" for row in s["table"]["rows"]]
            L.append("")
        if s.get("points"):
            L += [f"- {p}" for p in s["points"]] + [""]
        if s.get("tools"):
            L += [f"**대표 도구·시스템** — {' · '.join(s['tools'])}", ""]
        for label, items in (s.get("extra") or {}).items():
            items = [i for i in items if i]
            if items:
                L += [f"**{label}**", ""] + [f"- {i}" for i in items] + [""]
        if s.get("refs"):
            L += ["**레퍼런스** (제목 클릭 → 논문 리뷰)", ""]
            for i, r in enumerate(s["refs"], start=1):
                cit = f" · 인용 {r['citations']:,}" if r["citations"] else ""
                who = f"{r['author']}, " if r["author"] else ""
                L.append(f"{i}. [{r['title']}]({r['url']}) — {who}{r['date']}{cit}")
                if r["essence"]:
                    L.append(f"    - {r['essence']}")
            L.append("")
        if s.get("sowhat"):
            L += [f"> [!tip] 우리에게 무엇인가\n> {s['sowhat']}", ""]

    # 부록: 전체 레퍼런스
    seen, allrefs = set(), []
    for s in slides:
        for r in s.get("refs", []):
            if r["slug"] not in seen:
                seen.add(r["slug"])
                allrefs.append(r)
    allrefs.sort(key=lambda r: (-int(r["year"] or 0), r["title"]))
    L += ["---", "", f"## 부록 · 전체 레퍼런스 {len(allrefs)}편", ""]
    for r in allrefs:
        cit = f" · 인용 {r['citations']:,}" if r["citations"] else ""
        who = f"{r['author']}, " if r["author"] else ""
        L.append(f"- [{r['title']}]({r['url']}) — {who}{r['date']}{cit}")
    L += ["",
          f"*생성: `pipeline/build_slide_deck.py --topic {topic}` · {today} · "
          f"근거 코퍼스 {stats['total']:,}편 (`docs/{topic}`)*", ""]
    return "\n".join(L)


# ── 렌더링: HTML ──────────────────────────────────────────────────────────
CSS = """
:root{--accent:__ACCENT__;--ink:#161616;--muted:#6b6b6b;--soft:#9a9a9a;
--rule:#e5e5e3;--bg:#f4f4f2;--card:#fff}
*{box-sizing:border-box}
html,body{margin:0;padding:0}
body{background:var(--bg);color:var(--ink);line-height:1.62;-webkit-font-smoothing:antialiased;
font-family:-apple-system,BlinkMacSystemFont,"Pretendard","Apple SD Gothic Neo","Noto Sans KR",sans-serif}
a{color:inherit}
.wrap{max-width:1120px;margin:0 auto;padding:46px 26px 90px}
header.deck{border-bottom:3px solid var(--ink);padding-bottom:22px}
header.deck .eyebrow{font-size:11.5px;letter-spacing:.22em;color:var(--accent);font-weight:700;text-transform:uppercase}
header.deck h1{font-size:33px;line-height:1.24;margin:.35em 0 .3em;letter-spacing:-.022em}
header.deck p.lede{margin:0;color:var(--muted);font-size:14.5px}
.stats{display:flex;flex-wrap:wrap;gap:9px;margin:20px 0 0}
.stat{background:var(--card);border:1px solid var(--rule);border-radius:10px;padding:9px 14px;min-width:118px}
.stat b{display:block;font-size:20px;letter-spacing:-.01em}
.stat span{font-size:11px;color:var(--muted)}
nav.toc{background:var(--card);border:1px solid var(--rule);border-radius:12px;padding:18px 20px;margin:26px 0 30px}
nav.toc h2{font-size:12px;letter-spacing:.16em;color:var(--soft);margin:0 0 10px;text-transform:uppercase}
nav.toc ol{margin:0;padding:0;list-style:none;display:grid;
grid-template-columns:repeat(auto-fill,minmax(258px,1fr));gap:2px 18px}
nav.toc li{font-size:12.8px;color:var(--muted);padding:2px 0}
nav.toc li a{text-decoration:none}
nav.toc li a:hover{color:var(--accent)}
nav.toc li .n{display:inline-block;min-width:36px;color:var(--soft);font-size:11.5px;font-variant-numeric:tabular-nums}
nav.toc li.part{margin-top:9px;font-weight:700;color:var(--ink);font-size:12px;grid-column:1/-1;
border-top:1px solid var(--rule);padding-top:8px}
.slide{background:var(--card);border:1px solid var(--rule);border-radius:14px;
padding:28px 32px 24px;margin:0 0 18px;scroll-margin-top:14px}
.rail{display:flex;align-items:center;gap:9px;margin-bottom:13px}
.rail .no{background:var(--ink);color:#fff;font-size:11.5px;font-weight:700;letter-spacing:.06em;
padding:3px 9px;border-radius:5px;font-variant-numeric:tabular-nums}
.rail .kind{font-size:10.5px;letter-spacing:.15em;color:var(--accent);font-weight:700;text-transform:uppercase}
.rail .part{font-size:11.5px;color:var(--soft);margin-left:auto}
.slide h2{font-size:24px;line-height:1.3;margin:0 0 4px;letter-spacing:-.02em}
.slide .en{font-size:12.8px;color:var(--muted);margin:0;font-style:italic}
.slide .alias{font-size:11.5px;color:var(--soft);margin:3px 0 0}
.badges{display:flex;flex-wrap:wrap;gap:6px;margin:13px 0 0}
.badge{font-size:11.5px;border:1px solid var(--rule);border-radius:20px;padding:2px 11px;color:var(--muted);background:#fafafa}
.badge.n{border-color:var(--accent);color:var(--accent);font-weight:700}
.badge.recent{border-color:#c9c9c9;color:#4a4a4a;font-weight:600}
.badge.st-가속{background:#fdf1ef;border-color:#f0c6bf;color:#a8291a}
.badge.st-부상{background:#f1f6fd;border-color:#c3d8f0;color:#1f5b9e}
.badge.st-안정{background:#f5f5f4;border-color:#dcdcda;color:#5a5a58}
.badge.st-감소{background:#f7f7f7;border-color:#e2e2e2;color:#8a8a8a}
.catmeta{font-size:11.8px;color:var(--soft);margin:10px 0 0}
.context{margin:15px 0 0;padding:10px 15px;border-left:3px solid var(--rule);background:#fafafa;
color:var(--muted);font-size:13.4px;border-radius:0 6px 6px 0}
.headline{margin:17px 0 2px;padding:14px 18px;background:#fbf6f5;border-left:4px solid var(--accent);
border-radius:0 8px 8px 0;font-size:16px;font-weight:600;line-height:1.55}
ul.points{margin:17px 0 0;padding-left:0;list-style:none}
ul.points li{position:relative;padding-left:19px;margin-bottom:8px;font-size:14.3px}
ul.points li::before{content:"";position:absolute;left:3px;top:.62em;width:6px;height:6px;
border-radius:50%;background:var(--accent);opacity:.55}
sup.cite{font-size:10.5px;font-weight:700;color:var(--accent);vertical-align:super;margin-left:1px}
sup.cite a{text-decoration:none}
table.grid{width:100%;border-collapse:collapse;margin:17px 0 4px;font-size:13.3px}
table.grid th{text-align:left;font-size:11px;letter-spacing:.08em;color:var(--soft);text-transform:uppercase;
border-bottom:2px solid var(--ink);padding:7px 10px 7px 0}
table.grid td{border-bottom:1px solid var(--rule);padding:7px 10px 7px 0;vertical-align:top}
table.grid td:nth-child(2){font-variant-numeric:tabular-nums;white-space:nowrap}
table.grid td:last-child{color:var(--accent);letter-spacing:-1px}
.block-label{font-size:10.5px;letter-spacing:.16em;color:var(--soft);text-transform:uppercase;
margin:20px 0 7px;font-weight:700}
.tools{display:flex;flex-wrap:wrap;gap:5px}
.tool{font-size:11.8px;background:#f4f4f2;border:1px solid var(--rule);border-radius:5px;padding:2px 8px;color:#444}
ol.refs{margin:0;padding-left:20px}
ol.refs li{font-size:13.2px;margin-bottom:7px;line-height:1.5}
ol.refs a{font-weight:600;text-decoration:none;border-bottom:1px solid rgba(0,0,0,.18)}
ol.refs a:hover{color:var(--accent);border-bottom-color:var(--accent)}
ol.refs .m{color:var(--soft);font-size:11.8px;font-variant-numeric:tabular-nums}
ol.refs .e{display:block;color:var(--muted);font-size:12.4px;margin-top:2px}
.sowhat{margin:20px 0 0;padding:13px 18px;background:#f6f7f9;border:1px solid #e2e5ea;border-radius:9px;font-size:13.8px}
.sowhat b{color:var(--accent);font-size:10.5px;letter-spacing:.14em;display:block;margin-bottom:4px;text-transform:uppercase}
.appendix{background:var(--card);border:1px solid var(--rule);border-radius:14px;padding:26px 32px}
.appendix h2{font-size:20px;margin:0 0 4px}
.appendix p.sub{color:var(--muted);font-size:12.5px;margin:0 0 14px}
.appendix ol{padding-left:22px;margin:0}
.appendix li{font-size:13px;margin-bottom:5px}
footer.deck{margin-top:34px;padding-top:16px;border-top:1px solid var(--rule);
font-size:11.5px;color:var(--soft);text-align:center}
@media print{
 body{background:#fff}
 .wrap{max-width:none;padding:0}
 header.deck,nav.toc{page-break-after:always}
 .slide{page-break-inside:avoid;page-break-after:always;border:none;border-radius:0;padding:16px 0;margin:0}
 @page{size:A4 landscape;margin:13mm}
}
"""


def _inline(text):
    out = H.escape(str(text))
    out = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", out)
    out = re.sub(r"`(.+?)`", r"<code>\1</code>", out)
    out = re.sub(r"\[(\d+)\]", r'<sup class="cite">[\1]</sup>', out)
    return out


def render_html(topic, slides, stats):
    today = datetime.now().strftime("%Y-%m-%d")
    css = CSS.replace("__ACCENT__", ACCENT.get(topic, "#D63423"))
    o = ["<!DOCTYPE html><html lang='ko'><head><meta charset='utf-8'>",
         "<meta name='viewport' content='width=device-width,initial-scale=1'>",
         f"<title>AI for Science 지형도 — 슬라이드 원고 {len(slides)}장 ({topic})</title>",
         f"<style>{css}</style></head><body><div class='wrap'>"]

    o.append("<header class='deck'>")
    o.append(f"<div class='eyebrow'>{H.escape(topic)} · slide script · {today}</div>")
    o.append(f"<h1>AI for Science 지형도 — 발표 슬라이드 {len(slides)}장</h1>")
    o.append(f"<p class='lede'>슬라이드 1장 = 서브카테고리 1개. 사례는 {stats['since']}년 이후 우선. "
             f"레퍼런스 제목을 클릭하면 해당 논문의 리뷰 문서로 이동한다.</p>")
    o.append("<div class='stats'>")
    for value, label in [(f"{stats['total']:,}", "코퍼스 논문"),
                         (str(len(stats["categories"])), "대분류"),
                         (str(stats["n_subs"]), "서브카테고리"),
                         (str(len(slides)), "슬라이드"),
                         (f"{stats['recent_share']}%", f"{stats['since']}년 이후 비중")]:
        o.append(f"<div class='stat'><b>{value}</b><span>{H.escape(label)}</span></div>")
    o.append("</div></header>")

    o.append("<nav class='toc'><h2>목차</h2><ol>")
    cur = None
    for s in slides:
        if s["part"] != cur:
            cur = s["part"]
            o.append(f"<li class='part'>{H.escape(cur)}</li>")
        badge = f" · {H.escape(s['badges'][0])}" if s.get("badges") else ""
        o.append(f"<li><a href='#s{s['no']:02d}'><span class='n'>S{s['no']:02d}</span>"
                 f"{H.escape(s['title_ko'])}</a>{badge}</li>")
    o.append("</ol></nav>")

    for s in slides:
        o.append(f"<section class='slide' id='s{s['no']:02d}'>")
        o.append(f"<div class='rail'><span class='no'>S{s['no']:02d}</span>"
                 f"<span class='kind'>{H.escape(s['kind'])}</span>"
                 f"<span class='part'>{H.escape(s['part'])}</span></div>")
        o.append(f"<h2>{H.escape(s['title_ko'])}</h2>")
        if s.get("title_en"):
            o.append(f"<p class='en'>{H.escape(s['title_en'])}</p>")
        if s.get("alias_en"):
            o.append(f"<p class='alias'>타임라인 분석 명칭: {H.escape(s['alias_en'])}</p>")
        if s.get("badges"):
            o.append("<div class='badges'>")
            for i, b in enumerate(s["badges"]):
                cls = "badge n" if i == 0 else ("badge recent" if b.startswith(str(stats["since"]))
                                                else f"badge st-{b}" if b in STATUS_KO.values() else "badge")
                o.append(f"<span class='{cls}'>{H.escape(b)}</span>")
            o.append("</div>")
        if s.get("cat_meta"):
            o.append(f"<p class='catmeta'>{H.escape(s['cat_meta'])}</p>")
        if s.get("context"):
            o.append(f"<div class='context'>{_inline(s['context'])}</div>")
        if s.get("headline"):
            o.append(f"<div class='headline'>{_inline(s['headline'])}</div>")
        if s.get("table"):
            o.append("<table class='grid'><thead><tr>")
            o += [f"<th>{H.escape(h)}</th>" for h in s["table"]["head"]]
            o.append("</tr></thead><tbody>")
            for row in s["table"]["rows"]:
                o.append("<tr>" + "".join(f"<td>{H.escape(str(x))}</td>" for x in row) + "</tr>")
            o.append("</tbody></table>")
        if s.get("points"):
            o.append("<ul class='points'>")
            o += [f"<li>{_inline(p)}</li>" for p in s["points"]]
            o.append("</ul>")
        if s.get("tools"):
            o.append("<div class='block-label'>대표 도구 · 시스템</div><div class='tools'>")
            o += [f"<span class='tool'>{H.escape(t)}</span>" for t in s["tools"]]
            o.append("</div>")
        for label, items in (s.get("extra") or {}).items():
            items = [i for i in items if i]
            if items:
                o.append(f"<div class='block-label'>{H.escape(label)}</div><ul class='points'>")
                o += [f"<li>{_inline(i)}</li>" for i in items]
                o.append("</ul>")
        if s.get("refs"):
            o.append("<div class='block-label'>레퍼런스 — 제목 클릭 시 논문 리뷰</div><ol class='refs'>")
            for r in s["refs"]:
                cit = f" · 인용 {r['citations']:,}" if r["citations"] else ""
                who = f"{H.escape(r['author'])}, " if r["author"] else ""
                o.append(f"<li><a href='{H.escape(r['url'])}'>{H.escape(r['title'])}</a> "
                         f"<span class='m'>{who}{H.escape(r['date'])}{cit}</span>"
                         + (f"<span class='e'>{H.escape(r['essence'])}</span>" if r["essence"] else "")
                         + "</li>")
            o.append("</ol>")
        if s.get("sowhat"):
            o.append(f"<div class='sowhat'><b>우리에게 무엇인가</b>{_inline(s['sowhat'])}</div>")
        o.append("</section>")

    seen, allrefs = set(), []
    for s in slides:
        for r in s.get("refs", []):
            if r["slug"] not in seen:
                seen.add(r["slug"])
                allrefs.append(r)
    allrefs.sort(key=lambda r: (-int(r["year"] or 0), r["title"]))
    o.append("<section class='appendix'>")
    o.append(f"<h2>부록 · 전체 레퍼런스 {len(allrefs)}편</h2>")
    o.append(f"<p class='sub'>모든 링크는 코퍼스 내 논문 리뷰 문서({H.escape(stats['link_base'])}/&lt;slug&gt;/index.html)로 연결된다.</p><ol>")
    for r in allrefs:
        cit = f" · 인용 {r['citations']:,}" if r["citations"] else ""
        who = f"{H.escape(r['author'])}, " if r["author"] else ""
        o.append(f"<li><a href='{H.escape(r['url'])}'>{H.escape(r['title'])}</a> "
                 f"<span class='m'>{who}{H.escape(r['date'])}{cit}</span></li>")
    o.append("</ol></section>")
    o.append(f"<footer class='deck'>pipeline/build_slide_deck.py --topic {H.escape(topic)} · {today} · "
             f"근거 코퍼스 {stats['total']:,}편</footer>")
    o.append("</div></body></html>")
    return "\n".join(o)


def main():
    ap = argparse.ArgumentParser(description="토픽 코퍼스 → 발표 슬라이드 원고(HTML + Obsidian MD)")
    ap.add_argument("--topic", default="ai4s", help="토픽 alias (기본 ai4s)")
    ap.add_argument("--per-category", type=int, default=5, help="대분류당 서브카테고리 슬라이드 수")
    ap.add_argument("--since", type=int, default=2025, help="사례 우선 기준 연도 (기본 2025)")
    ap.add_argument("--link-base", default="../../docs/papers",
                    help="리뷰 문서 링크 베이스. 로컬 서버면 http://localhost:8000/papers")
    ap.add_argument("--out-dir", default=None, help="출력 루트 (기본 reports/)")
    args = ap.parse_args()

    summaries, classification, timeline, insights, index = load_corpus(args.topic)
    slides, stats = build_slides(args.topic, summaries, classification, timeline, insights, index,
                                 per_category=args.per_category, link_base=args.link_base,
                                 since=args.since)

    root = Path(args.out_dir) if args.out_dir else REPORTS
    html_path = root / "build" / f"{args.topic}_slides_{len(slides)}.html"
    md_path = root / "source" / f"{args.topic}_slides_{len(slides)}.md"
    atomic_write_text(html_path, render_html(args.topic, slides, stats))
    atomic_write_text(md_path, render_markdown(args.topic, slides, stats))

    n_refs = len({r["slug"] for s in slides for r in s.get("refs", [])})
    print(f"[OK] 슬라이드 {len(slides)}장 · 레퍼런스 {n_refs}편 "
          f"(코퍼스 {stats['total']:,}편, {stats['since']}+ {stats['recent_share']}%)")
    print(f"  HTML : {html_path}")
    print(f"  MD   : {md_path}")
    return 0


if __name__ == "__main__":
    from _env_guard import force_py312
    force_py312()
    sys.exit(main())
