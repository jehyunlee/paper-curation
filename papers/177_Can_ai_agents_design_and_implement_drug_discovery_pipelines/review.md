---
title: "177_Can_ai_agents_design_and_implement_drug_discovery_pipelines"
authors:
  - "Khachik Smbatyan"
  - "Tsolak Ghukasyan"
  - "Tigran Aghajanyan"
  - "Hovhannes Dabaghyan"
  - "Sergey Adamyan"
date: "2025"
doi: "N/A"
arxiv: ""
score: 4.1
essence: "본 논문은 대규모 언어모델(LLM) 기반 자율 AI 에이전트가 신약 발견(drug discovery) 파이프라인을 독립적으로 설계하고 구현할 수 있는지 평가하기 위한 **DO Challenge 벤치마크**를 제시하고, 이에 기반한 멀티-에이전트 시스템 **Deep Thought**의 성능을 분석한 연구이다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/AI_Drug_Discovery"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Smbatyan et al._2025_Can ai agents design and implement drug discovery pipelines arXiv preprint arXiv2504.19912, 2025..pdf"
---

# Can ai agents design and implement drug discovery pipelines? arXiv preprint arXiv:2504.19912, 2025.

> **저자**: Khachik Smbatyan, Tsolak Ghukasyan, Tigran Aghajanyan, Hovhannes Dabaghyan, Sergey Adamyan, Aram Bughdaryan, Vahagn Altunyan, Gagik Navasardyan, Aram Davtyan, Anush Hakobyan, A. Gharibyan, Arman Fahradyan, A. Hakobyan, Hasmik Mnatsakanyan, Narek Ginoyan, Garik Petrosyan | **날짜**: 2025 | **DOI**: N/A

---

## Essence

본 논문은 대규모 언어모델(LLM) 기반 자율 AI 에이전트가 신약 발견(drug discovery) 파이프라인을 독립적으로 설계하고 구현할 수 있는지 평가하기 위한 **DO Challenge 벤치마크**를 제시하고, 이에 기반한 멀티-에이전트 시스템 **Deep Thought**의 성능을 분석한 연구이다.

## Motivation

- **Known**: 최근 AI 에이전트 시스템들(AlphaFold, 자동 소프트웨어 엔지니어링 등)은 복잡한 문제 해결에서 뛰어난 성능을 보이고 있으며, AI 기반 신약 발견 가속화의 가능성이 높아지고 있음

- **Gap**: 기존 신약 발견 벤치마크들(TDC, DrugOOD, GuacaMol 등)은 대부분 **고립된 예측 작업(isolated predictive tasks)**에만 초점을 맞추고 있으며, AI 에이전트의 독립적 의사결정, 코드 개발, 자율 실행 능력을 평가하는 **통합적이고 전문화된 벤치마크가 부족함**

- **Why**: 신약 발견의 실제 파이프라인은 문헌 검토, 화학 공간 탐색, 모델 선택, 자원 제약 하에서의 다목적 최적화 등 복합적인 전략적 의사결정을 요구함

- **Approach**: (1) 가상 스크리닝(virtual screening)에 영감을 받은 통합형 벤치마크(DO Challenge) 개발, (2) 이를 기반으로 한 멀티-에이전트 시스템 구현, (3) 인간 전문가 및 경진대회 참가자와의 광범위한 비교 분석

## Achievement

1. **DO Challenge 벤치마크 제시**: 100만 개의 분자 구조로부터 DO Score가 가장 높은 상위 1,000개 분자 식별이라는 단일 통합 문제로서, 자원 제약(상위 10% 라벨링 가능, 3회 제출 제한) 하에서 AI 에이전트의 전략적 계획, 코드 작성/실행, 적응성 평가

2. **Deep Thought 멀티-에이전트 시스템 개발 및 성능 검증**:
   - **시간 제약 조건(10시간)**: 상위 1,000개 분자와의 겹침률(overlap) 33.5% 달성 → 최고 인간 전문가(33.6%)와 거의 동등, 경진대회 최우수팀(16.4%)을 크게 상회
   - **시간 무제약 조건**: 33.5% → 인간 전문가 최고 성능(77.8%)에는 여전히 미치지 못함
   - LLM 역할별 성능: Claude 3.7 Sonnet, Gemini 2.5 Pro, o3이 주요 에이전트로 우수, GPT-4o와 Gemini 2.0 Flash는 보조 역할에서 효과적

3. **경진대회 기반 상세 비교 분석**: DO Challenge 2025 참가 40개 팀 중 선발 20개 팀의 다양한 전략(능동 학습, 어텐션 기반 모델, 반복적 제출 등) 분석 및 인간 전문가 참조 솔루션과의 체계적 비교

## How

- **벤치마크 설계**: 
  - 100만 개 분자 데이터셋에 대해 사용자 정의 DO Score 레이블 생성
  - 10% 라벨 획득 제약(100,000개), 3회 제출 제한으로 자원 제약 시뮬레이션
  - 시간 제약(10시간) 및 무제약 두 가지 설정 제공

- **Deep Thought 아키텍처**:
  - 이질적(heterogeneous) LLM 기반 에이전트들의 협력 시스템
  - 각 에이전트는 특정 역할(문헌 검토, 코드 작성, 결과 분석 등)을 담당하며 상호 통신
  - 환경과의 상호작용을 위한 도구 활용(파일 작성, 코드 실행, 웹 브라우징)

- **평가 지표**:
  - 주요: 실제 상위 1,000개 분자와 에이전트 선택 분자의 겹침률(%)
  - 부수: 런타임, LLM 토큰 사용량(Fig 3)

## Originality

- **신규 벤치마크 개발**: 기존의 고립된 작업 중심 벤치마크와 달리, **신약 발견의 실제 복잡성을 통합적으로 반영**하는 최초의 벤치마크 제시(화학 공간 탐색, 다목적 최적화, 자원 제약, 모델 선택의 동시 평가)

- **멀티-에이전트 코디네이션**: 이질적 LLM을 활용한 계층적 협력 구조로, 단순한 다중 LLM 호출을 넘어 **역할 분담과 피드백 루프 설계**

- **광범위한 비교 분석**: AI 에이전트 vs. 인간 전문가 vs. 경진대회 참가자의 **3원 비교**를 통해 상대적 강점/약점의 체계적 규명

- **공개 리소스**: 벤치마크(Zenodo) 및 소스코드(GitHub) 공개로 재현성 및 향후 연구 기반 제공

## Limitation & Further Study

- **성능 격차**: 시간 무제약 조건에서 인간 전문가(77.8%)와의 상당한 격차(43.3% 포인트) 존재 → AI 에이전트의 **장기 전략 수립 및 적응적 학습 능력 한계** 시사

- **높은 불안정성(instability)**: Deep Thought의 런타임 및 성능이 실행마다 변동하는 문제 지적 → 에이전트 의사결정 경로의 **재현성 및 신뢰성 개선 필요**

- **제한된 평가 시나리오**: 단일 벤치마크 작업만으로 평가 → 다양한 신약 발견 시나리오(표적 식별, 분자 생성, 바이오 마커 예측 등)로의 **확장성 미지수**

- **후속 연구**: 
  - 에이전트의 불안정성 원인 규명 및 개선 방안(프롬프트 최적화, 에이전트 아키텍처 개선)
  - 인간-AI 협력 모델 개발 → 인간 전문성의 87.8%(33.6%/38.3%) 수준까지만 달성한 부분 보완
  - 다양한 신약 발견 작업으로의 벤치마크 확대 및 통합 평가 프레임워크 개발

## Evaluation

- **Novelty**: 4.5/5 
  - 신약 발견 특화 벤치마크는 신규이나, 일반적 에이전트 시스템 아키텍처는 기존 연구의 조합

- **Technical Soundness**: 4/5
  - 벤치마크 설계 및 평가 방법론은 견고하나, 에이전트 불안정성의 근본 원인 분석 부족

- **Significance**: 4/5
  - 신약 발견 AI 에이전트 연구에 중요한 기준점(benchmark) 제시이나, 실제 임상 신약 발견 파이프라인과의 간극 존재

- **Clarity**: 4/5
  - 벤치마크 및 결과 기술는 명확하나, Deep Thought 아키텍처의 세부 구현(에이전트 간 통신 메커니즘, 프롬프트 설계)에 대한 상세 기술 부족

- **Overall**: 4.1/5

**총평**: 본 논문은 신약 발견 맥락에서 AI 에이전트의 **통합적 능력을 평가하는 신규 벤치마크**를 제시하고, 멀티-에이전트 시스템의 경쟁력 있는 성능을 입증했다는 점에서 의미 있으나, 시간 무제약 조건에서의 인간 전문가와의 큰 격차와 높은 불안정성은 현재 AI 에이전트가 **실제 신약 발견 자동화에는 아직 부족함**을 시사한다.

## Related Papers

- 🔄 다른 접근: [[papers/490_LIDDIA_Language-based_Intelligent_Drug_Discovery_Agent/review]] — 둘 다 AI 기반 신약 발견을 다루지만 Deep Thought는 파이프라인 설계에, LIDDIA는 전체 전임상 과정에 집중함
- 🏛 기반 연구: [[papers/594_OSDA_Agent_Leveraging_Large_Language_Models_for_De_Novo_Desi/review]] — DS-Agent의 데이터 과학 자동화 방법론이 Deep Thought의 신약 발견 파이프라인 구현 능력의 기반이 됨
- 🔗 후속 연구: [[papers/326_Exp-bench_Can_ai_conduct_ai_research_experiments_arXiv_prepr/review]] — Exp-bench의 AI 연구 실험 수행 평가가 Deep Thought의 신약 발견 연구 자동화 성능을 검증하는 도구로 활용됨
- 🔄 다른 접근: [[papers/415_Hunt_Globally_Wide_Search_AI_Agents_for_Drug_Asset_Scouting/review]] — 약물 자산 탐색에서 다국어 멀티에이전트와 AI 에이전트 기반 파이프라인 설계 접근법을 비교할 수 있습니다.
- 🔄 다른 접근: [[papers/490_LIDDIA_Language-based_Intelligent_Drug_Discovery_Agent/review]] — 같은 신약개발 자동화를 다루지만 LIDDIA는 전임상 과정 전반을, Deep Thought는 파이프라인 설계에 집중한 차이점을 보임
- 🏛 기반 연구: [[papers/514_MAC-AMP_A_Closed-Loop_Multi-Agent_Collaboration_System_for_M/review]] — AI 에이전트의 약물 발견 파이프라인 설계 능력이 MAC-AMP의 폐루프 항균펩타이드 개발 시스템 구축의 기본적인 기술적 토대이다.
- 🧪 응용 사례: [[papers/616_PharmAgents_Building_a_Virtual_Pharma_with_Large_Language_Mo/review]] — AI 에이전트가 약물 발견 파이프라인을 설계하고 구현할 수 있는지에 대한 구체적 검증을 제공한다.
