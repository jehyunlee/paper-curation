---
title: "672_ResearchGym_Evaluating_Language_Model_Agents_on_Real-World_A"
authors:
  - "Aniketh Garikaparthi"
  - "Manasi Patwardhan"
  - "Arman Cohan"
date: "2026.02"
doi: "N/A"
arxiv: ""
score: 4.25
essence: "본 논문은 실제 AI 연구 논문의 저장소를 기반으로 엔드-투-엔드 연구 루프를 평가하는 벤치마크 ResearchGym을 제시한다. GPT-5 기반 에이전트가 인상적인 성능을 보이기도 하지만 신뢰성이 매우 낮다는 \"능력-신뢰성 격차(capability-reliability gap)\"를 실증적으로 입증한다."
tags:
  - "cat/Scientific_Language_Processing_and_Visualization"
  - "sub/LLM_Agent_Benchmarking"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Garikaparthi et al._2026_ResearchGym Evaluating Language Model Agents on Real-World AI Research.pdf"
---

# ResearchGym: Evaluating Language Model Agents on Real-World AI Research

> **저자**: Aniketh Garikaparthi, Manasi Patwardhan, Arman Cohan | **날짜**: 2026-02-16 | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp) 
*그림 1: ResearchGym은 아이디어 제시와 실험 수행을 결합하여 LLM 에이전트를 객관적 점수로 평가*

본 논문은 실제 AI 연구 논문의 저장소를 기반으로 엔드-투-엔드 연구 루프를 평가하는 벤치마크 ResearchGym을 제시한다. GPT-5 기반 에이전트가 인상적인 성능을 보이기도 하지만 신뢰성이 매우 낮다는 "능력-신뢰성 격차(capability-reliability gap)"를 실증적으로 입증한다.

## Motivation

- **Known**: 기존 벤치마크들은 연구 사이클의 단편적 부분만 평가함 (아이디어 생성 또는 구현 중 하나)
  - 아이디어 벤치마크: 실행 없이 가설 생성만 평가
  - ML 엔지니어링 벤치마크: Kaggle 경쟁 기반으로 창의성 여지 부족
  - 재현 벤치마크: 오래된 작업으로 인한 오염(contamination) 위험

- **Gap**: 실제 폐쇄 루프(closed-loop) 연구를 수행하는 능력 평가의 부재
  - 기존 폐쇄 루프 벤치마크: LLM 판사 의존, 고비용 GPU 요구, 인간 기준점 부재

- **Why**: 최근 많은 연구들이 자동화된 연구 시스템을 제안하지만 체계적인 비교 기준이 없어 능력이 과장되는 경향

- **Approach**: 
  - 2025년 ICML/ICLR/ACL 구두/스팟라이트 논문 5편 선정
  - 논문의 데이터셋, 평가 스크립트, 베이스라인은 유지하되 제안 방법만 제거
  - 객관적 실행 기반 평가로 신뢰성 확보
  - 단일 GPU에서 24시간 이내 실행 가능하도록 설계

## Achievement

![Figure 2](figures/fig1.webp)
*그림 2: 1,387개 논문에서 자동 필터링과 인간 평가를 통해 5개 작업 선정*

1. **포괄적 벤치마크 구성**: 
   - 5개 작업, 39개 부작업 (지속 학습, 강화학습, 토크나이제이션, 교차모달 검색, 시계열 설명)
   - 객관적 평가 지표(원본 논문의 평가 스크립트 사용)
   - 하한선(베이스라인)과 상한선(저자 솔루션) 제공으로 보정된 비교

2. **GPT-5 에이전트의 신뢰성 격차 실증**:
   - 15회 평가(5개 작업 × 3시드) 중 베이스라인 개선: 1회(6.7%)만 성공
   - 평균 부작업 완료율: 26.5%
   - 성능이 ~9시간 후 고착(plateau)
   - 하나의 성공 사례: ICML 2025 스팟라이트 작업에서 인간 솔루션 초과

3. **다양한 에이전트 아키텍처 평가**:
   - Claude Code(Opus-4.5), Codex(GPT-5.2) 모두 유사한 격차 확인
   - 최신 폐쇄 소스 에이전트 프레임워크의 한계 드러냄

## How

![Figure 3](figures/fig1.webp)
*그림 3: 벤치마크 구성 과정: LLM 기반 정보 추출 → 휴리스틱 필터링 → 인간 QA*

**태스크 설계**:
- 태스크 인스턴스 I = (R, T, g): 시작 저장소, 작업 설명, 평가자
- 예산 제약 B (시간, API 비용) 선택적 포함
- 각 태스크는 다중 부작업 + 하나의 기본 부작업(primary task)

**벤치마크 구성 파이프라인**:
- **1단계**: LLM 기반 정보 추출 및 휴리스틱 필터링
  - GROBID 기반 doc2json으로 PDF→JSON 변환
  - GPT-5로 구조화된 카드(C) 생성
  - 평가 목표 객관성, 코드 가용성, GPU 메모리 필터링
  - 1,387개 → 90개 논문으로 축소

- **2단계**: 인간 선별 및 태스크 패키징
  - 실행 가능성 평가 (객관적 평가 여부, 알고리즘 창의성 여지, 시간 제약)
  - 다양성 확보 (5개 도메인)
  - 개발 세트 3개 작업으로 에이전트 스캐폴딩 조정

**오염 인식 설계**:
- 2025년 이후 발행 논문 선정 (주요 LLM의 학습 데이터 컷오프 이후)
- 90개 중 수작업 검증

**평가 메커니즘**:
- 목표: 원본 논문의 평가 스크립트 사용 (LLM 판사 배제)
- 평가자 g는 에이전트 워크스페이스 ŝ 상태 입력
- 객관적 점수 벡터 v̂ 반환

**에이전트 아키텍처**:
- 제공 도구: Python, Bash, 파일 읽기/쓰기, PDF 리더, 인용 순회, 웹 검색
- 마인드 모듈: 사고(Think), 초안 작성(Draft), 피드백 루프
- 트리 서치 능력 지원
- 동기 작업 관리 (병렬 실험 조율)

## Originality

- **혁신적 벤치마크 설계**: 기존 단편적 평가를 벗어나 폐쇄 루프 연구의 전체 사이클 평가 (아이디어 → 실험 → 검증)
  
- **객관적 평가 메커니즘**: LLM 판사의 신뢰성 문제를 원본 논문의 실행 기반 평가로 해결

- **오염 인식 구성**: 2025년 최신 논문 사용으로 데이터 누수 위험 최소화

- **접근성**: 단일 GPU에서 실행 가능한 폐쇄 루프 연구 벤치마크 (기존 640GB GPU 요구 대비)

- **대규모 실증 평가**: 35회 이상의 엔드-투-엔드 실행으로 신뢰성 격차 체계적 실증

- **확장성**: 인프라 공개로 향후 작업 추가 용이 (저장소 공개)

## Limitation & Further Study

**한계**:
- **제한된 작업 규모**: 5개 작업만 평가 (깊이 우선 설계이지만 일반화 제한)
- **확인된 장기 실패 모드들**:
  - 인내심 부족 (조기 포기)
  - 시간/자원 관리 미흡
  - 약한 가설에 대한 과신
  - 병렬 실험 조율 어려움
  - 컨텍스트 길이 제한 (hard limit)
  - 이러한 실패 모드의 근본 원인 분석 부족

- **평가 범위**: 신규 에이전트 아키텍처 검증 필요, 다른 도메인(생물학, 화학 등) 확대 필요

- **인간 기준점 부재**: 인간 연구자와의 직접 비교 (같은 제약 하에서의 성능)

**후속 연구 방향**:
- 식별된 실패 모드를 해결하는 에이전트 설계 개선
- 장기 수평(long-horizon) 추론 능력 강화
- 병렬 실험 조율 메커니즘 개발
- 컨텍스트 효율성 개선 (희소화, 요약 기법)
- ResearchGym 확대: 더 많은 도메인, 더 많은 작업
- 인간 연구자 평가 추가로 상대적 능력 평가

## Evaluation

- **Novelty (혁신성)**: 4.5/5
  - 폐쇄 루프 연구 평가의 새로운 프레임워크로 기존 단편적 평가 초월
  - 객관적 실행 기반 평가로 신뢰성 확보
  - 다만 작업 규모는 제한적

- **Technical Soundness (기술적 타당성)**: 4.5/5
  - 벤치마크 구성 방법론 체계적이고 투명함 (2단계 파이프라인)
  - 오염 인식 설계로 데이터 누수 최소화
  - 35회 이상 평가로 통계적 신뢰성 확보
  - 다만 확인된 실패 모드 분석이 현상 기술 수준

- **Significance (중요성)**: 4.5/5
  - AI 에이전트의 실제 연구 능력을 처음으로 체계적 평가
  - 능력-신뢰성 격차 실증는 현장에 중대한 시사
  - 재현 가능하고 확장 가능한 인프라 제공
  - 다만 5개 작업 기반 일반화는 제약

- **Clarity (명확성)**: 4/5
  - 벤치마크 설계 및 평가 메트릭 명확히 기술
  - 도표와 표로 비교 가능한 설명
  - 다만 실패 모드 분석의 정성적 기술이 더 필요할 수 있음

- **Overall (종합)**: 4.25/5

**총평**: 본 논문은 AI 에이전트의 실제 연구 수행 능력 평가를 위한 첫 번째 체계적 벤치마크를 제시함으로써 학계에 중요한 기여를 한다. 특히 객관적 실행 기반 평가, 오염 인식 설계, 접근성 있는 인프라 제공은 우수하나, 제한된 작업 규모와 현상적 실패 분석 수준은 향후 보완이 필요하다. 최신 LLM이 가끔 SOTA 성능에 도달하지만 대체로 신뢰할 수 없다는 발견은 에이전트 개발 커뮤니티에 중대한 경종을 울린다.

## Related Papers

- 🔄 다른 접근: [[papers/542_Mlagentbench_Evaluating_language_agents_on_machine_learning/review]] — ML 실험 자동화에 특화된 MLAgentBench와 달리 전체 AI 연구 프로세스를 평가하는 포괄적 접근
- 🏛 기반 연구: [[papers/815_ToolLLM_Facilitating_Large_Language_Models_to_Master_16000_R/review]] — 도구 사용 능력을 평가하는 ToolLLM의 방법론을 연구 에이전트 평가로 확장한 기반
- 🔗 후속 연구: [[papers/794_The_AI_Scientist-v2_Workshop-Level_Automated_Scientific_Disc/review]] — AI Scientist의 자동화된 과학 발견을 실제 연구 환경에서 체계적으로 벤치마킹하는 확장 연구
- 🏛 기반 연구: [[papers/180_Can_foundation_models_actively_gather_information_in_interac/review]] — 대화형 환경에서의 능동적 탐색 능력 평가 방법론을 연구 에이전트 평가에 적용한 기반
- 🏛 기반 연구: [[papers/542_Mlagentbench_Evaluating_language_agents_on_machine_learning/review]] — ML 실험 특화 에이전트 평가 방법론이 전체 AI 연구 프로세스 평가로 확장된 기반
- 🔗 후속 연구: [[papers/780_Surveyforge_On_the_outline_heuristics_memory-driven_generati/review]] — AI 연구 평가에서 자동화된 문헌 검토와 설문 생성 능력을 체계적으로 평가
- 🔗 후속 연구: [[papers/815_ToolLLM_Facilitating_Large_Language_Models_to_Master_16000_R/review]] — API 도구 사용 능력 평가 방법론을 AI 연구 자동화 평가로 확장한 발전
- 🏛 기반 연구: [[papers/180_Can_foundation_models_actively_gather_information_in_interac/review]] — 대화형 환경에서의 능동적 탐색 능력 평가가 AI 연구 에이전트 평가의 방법론적 기반
