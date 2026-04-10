---
title: "436_InternAgent_When_Agent_Becomes_the_Scientist_--_Building_Clo"
authors:
  - "InternAgent Team"
  - "Bo Zhang"
  - "Shiyang Feng"
  - "Xiangchao Yan"
  - "Jiakang Yuan"
date: "2025.05"
doi: "제공되지"
arxiv: ""
score: 3.0
essence: "본 논문은 다양한 과학 연구 분야에서 가설 생성부터 검증까지 완전 폐쇄 루프를 구성하는 통합 다중 에이전트 프레임워크 InternAgent를 제시한다. 반응 수율 예측에서 27.6%에서 35.4%로 12시간 내에 성능을 향상시키는 등 인간 연구자 대비 획기적인 효율성을 달성했다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/Autonomous_Hypothesis_Discovery"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Team et al._2025_InternAgent When Agent Becomes the Scientist -- Building Closed-Loop System from Hypothesis to Veri.pdf"
---

# InternAgent: When Agent Becomes the Scientist -- Building Closed-Loop System from Hypothesis to Verification

> **저자**: InternAgent Team, Bo Zhang, Shiyang Feng, Xiangchao Yan, Jiakang Yuan, Runmin Ma, Yusong Hu, Zhiyin Yu, Xiaohan He, Songtao Huang, Shaowei Hou, Zheng Nie, Zhilong Wang, Jinyao Liu, Tianshuo Peng, Peng Ye, Dongzhan Zhou, Shufei Zhang, Xiaosong Wang, Yilan Zhang | **날짜**: 2025-05-22 | **DOI**: [제공되지 않음](https://arxiv.org/abs/2505.16938)

---

## Essence

![Figure 1](https://example.com/fig1.png)
*InternAgent가 지원하는 12개 유형의 과학 연구 과제: 반응 수율 예측부터 자율주행까지 화학, 생물학, CV&NLP 분야 포괄*

본 논문은 다양한 과학 연구 분야에서 가설 생성부터 검증까지 완전 폐쇄 루프를 구성하는 통합 다중 에이전트 프레임워크 InternAgent를 제시한다. 반응 수율 예측에서 27.6%에서 35.4%로 12시간 내에 성능을 향상시키는 등 인간 연구자 대비 획기적인 효율성을 달성했다.

## Motivation

- **Known**: 대규모 언어 모델(LLM)과 로봇공학을 이용한 자동 과학 발견(ASD)은 데이터 분석, 가설 생성, 실험 설계 자동화를 통해 과학 연구의 속도를 가속화할 수 있는 잠재력을 보유하고 있다.

- **Gap**: 기존 자동 과학 연구(ASR) 시스템의 두 가지 핵심 문제: (1) 효과적이고 혁신적인 제안 생성의 어려움 - AI 모델은 기존 데이터와 패턴에 의존하면서 과학적 타당성과 창의성의 균형 유지가 곤란, (2) 완전한 폐쇄 루프 피드백 구현의 난제 - 실험 설계, 실행, 분석, 반복 개선의 통합이 필요하며 실험 변수와 노이즈 대응이 어려움.

- **Why**: 현존하는 자동화 시스템은 서로 다른 분야(로봇공학, 분석)의 통합, 불확실성 처리, 적응성 확보에 기술적·개념적 장벽을 가지고 있으며, 이를 해결하는 통합 프레임워크의 필요성이 대두됨.

- **Approach**: 자동 진화하는 아이디어 생성(Self-Evolving Idea Generation), 인간-상호작용 피드백(Human-interactive Feedback), 아이디어-방법론 변환(Idea-to-Methodology Construction), 다중 라운드 실험 계획 및 실행(Multi-round Experiment Planning and Execution)의 4개 핵심 모듈로 구성된 종단간(end-to-end) 자동 연구 파이프라인을 제안.

## Achievement

![Figure 2](https://example.com/fig2.png)
*InternAgent의 3대 주요 기능: (1) 인간-상호작용이 포함된 자동 진화 아이디어 생성, (2) 아이디어-방법론 변환, (3) 진화적 실험 계획 및 실행*

1. **확장성(Scalability)**: 반응 수율 예측, 분자 동역학, 전력 흐름 추정, 시계열 예측, 전사 예측, 인핸서 활성 예측, 감정 분류, 2D/3D 이미지 분류, 의미론적 분할, 자율주행 등 12개 과학 연구 과제에 검증됨. 기본 코드의 성능을 향상시키는 혁신적 아이디어 자동 생성 가능.

2. **효율성(Efficiency)**: 인간 연구자 대비 현저히 단축된 시간으로 우수한 성능 달성:
   - 반응 수율 예측: 24.2% ± 4.2 → 34.8% ± 1.1 (12시간)
   - 인핸서 활성 예측: 0.65 → 0.79 (4시간, Pearson 상관계수)
   - 2D 의미론적 분할: 78.8% → 81.0% (30시간)
   - 대조: 인간 연구자는 유사한 성능 향상에 수 개월 소요

3. **상호작용성(Interactivity)**: 자동화 종단간 프로세스 내에서 인간 전문가 피드백과 다중 에이전트 상호작용 인터페이스 제공. 도메인 전문가 지식의 원활한 통합 가능. 복수 코드 파일로 구성된 프로젝트 수준 수정 및 디버깅 지원.

## How

![Figure 2](https://example.com/fig2.png)
*InternAgent 시스템 아키텍처 및 워크플로우*

### 자동 진화하는 아이디어 생성 (Self-Evolving Idea Generation)

- **Survey Agent (조사 에이전트)**: 
  - 문헌 검토 모드(Literature Review Mode): 연구 과제를 다중 키워드 조합으로 분해 → 광범위한 학술 데이터베이스 검색 → 초록 분석을 통한 관련성 평가 (함수: R : L_abs × T → [0,1])
  - 깊은 연구 모드(Deep Research Mode): 관련 논문의 전문 다운로드 및 정밀 분석 → 신규 키워드 조합 생성 (함수: P : L → K')
  - 연구 단계별 맥락에 따른 동적 검색 전략 조정

- **Idea Innovation Agent (아이디어 혁신 에이전트)**: 생성된 문헌과 도메인 지식을 기반으로 혁신적 연구 아이디어 자동 제안

- **Assessment Agent (평가 에이전트)**: 생성된 아이디어의 참신성, 과학적 타당성, 실행 가능성을 평가 및 점수화

- **자동 진화 메커니즘**: 에이전트들의 반복적 상호작용을 통해 초기 아이디어를 점진적으로 정제 및 개선

### 아이디어-방법론 변환 (Idea-to-Methodology Construction)

- **Method Development Agent (방법론 개발 에이전트)**: 추상적 아이디어를 구체적이고 구현 가능한 방법론으로 변환
  - 알고리즘 명세 생성 (수식 및 의사코드)
  - 구현 요구사항 명시
  - 코드 구조 설계
  
- **문맥-인지 정제(Context-aware Refinement)**: 기존 코드베이스의 파일 구조, 함수, 설정을 분석하여 일관된 방법론 생성

### 진화적 실험 계획 및 실행 (Evolutionary Experimental Planning and Execution)

- **Orchestration Agent (조율 에이전트)**: 전체 워크플로우 관리 및 메모리 관리
  - 실험 계획 분해: 대규모 실험을 실행 가능한 단계로 분해
  - 메모리 관리: 이전 실험 결과, 생성된 아이디어, 피드백 기록 관리

- **Coding Agent (코딩 에이전트)**: OpenHands, Aider 등의 도구 활용하여 자동 코드 생성 및 구현
  - 파일 수준(File-Level), 저장소 수준(Repo-Level) 코드 수정 가능

- **AutoDebug 서버**: 실행 오류 추적(Error Traceback) 수집 및 자동 디버깅
  - 런타임 오류 자동 분석
  - 반복적 디버깅을 통한 코드 수렴

- **Code Review Agent (코드 검토 에이전트)**: 생성된 코드의 품질, 효율성, 과학적 타당성 검증

- **다중 라운드 검증**: 각 생성 모듈의 효과성을 실험을 통해 개별 검증

## Originality

- **통합 폐쇄 루프 프레임워크**: 가설 생성부터 검증까지 완전하게 통합된 자동 과학 연구 파이프라인은 기존 연구에서 부분적으로만 다루어진 과제임. 특히 여러 에이전트 간 협업 메커니즘과 인간-기계 상호작용을 정교하게 설계함.

- **횡단 분야 적용성**: 화학, 생물학, 컴퓨터 비전, 자연어처리 등 12개 이질적 과학 연구 분야에 동일한 프레임워크를 적용 가능하도록 설계한 점은 주목할 만함. 단순한 도메인 적응이 아닌 근본적 범용성 추구.

- **자동 진화 메커니즘**: Survey Agent의 문헌 검토 모드와 깊은 연구 모드의 이원화, 아이디어 생성 후 다중 라운드 평가 및 정제를 통한 자동 진화는 창의성과 과학적 엄밀성의 균형을 추구한 독창적 접근.

- **인간-기계 협업 인터페이스**: 완전 자동화 대신 인간 전문가의 피드백을 수용하는 상호작용 인터페이스는 현실적 과학 연구 환경을 반영한 설계.

- **광범위한 인간 평가**: 도메인 전문가를 초대하여 생성 아이디어의 참신성을 평가하고, 인간 연구자와의 효율성 비교 연구를 수행한 점은 정량적 및 정성적 검증의 균형을 맞춤.

## Limitation & Further Study

- **제한사항**:
  1. 12개 과제 중 일부는 완전 자동화보다는 특정 도메인 최적화된 설정이 필요할 수 있으며, 극도로 새로운 연구 영역에 대한 적용 가능성은 미지수.
  2. 자동 생성 아이디어의 '혁신성' 정의와 측정이 주관적일 수 있음. 논문에서는 도메인 전문가 평가에 의존하는데, 평가자 간 합의도(inter-rater agreement) 등의 정량적 메트릭 부재.
  3. 실험 시간 단축의 대부분이 컴퓨팅 리소스(병렬 처리, GPU 활용)에 의존할 가능성 있음. 인간과의 순수 알고리즘 효율성 비교가 명확하지 않을 수 있음.
  4. 폐쇄 루프 피드백에서 실패 사례(negative results) 처리 및 학습 메커니즘에 대한 상세 분석 부족.
  5. 생성된 아이디어의 재현성(reproducibility) 및 장기적 과학적 영향에 대한 후속 추적 연구 필요.

- **후속 연구 방향**:
  1. 더 극단적인 새로운 연구 분야(예: 이론 물리학, 수학적 정리 증명)에 InternAgent 적용 및 성능 평가.
  2. 실패 데이터와 부정적 결과(negative results)의 체계적 학습 및 적응 메커니즘 강화.
  3. 다중 모달 입력(이미지, 동영상, 실험 센서 데이터)을 수용하는 확장.
  4. 인간 전문가와의 협업에서 최적의 개입 시점(intervention points) 도출을 위한 의사결정 이론 연구.
  5. 생성 아이디어의 참신성을 정량적으로 측정하는 메트릭 개발 및 표준화.
  6. 장기적 과학 영향: 1년 이상 추적 연구를 통해 생성된 아이디어가 실제 후속 출판, 인용, 실제 적용으로 이어지는지 검증.


## Evaluation

- Novelty: 4.2/5
- Technical Soundness: 4/5
- Significance: 4.5/5
- Clarity: 3/5
- Overall: 3/5

## Related Papers

- 🔄 다른 접근: [[papers/795_The_AI_Scientist_Towards_Fully_Automated_Open-Ended_Scientif/review]] — 완전 자동화된 과학 발견에서 폐쇄 루프 시스템과 오픈엔드 시스템이라는 다른 접근법을 제시한다.
- 🔗 후속 연구: [[papers/828_Towards_end-to-end_automation_of_AI_research/review]] — AI 연구의 종단간 자동화로 과학 연구 자동화의 범위를 확장한다.
- 🏛 기반 연구: [[papers/825_Towards_an_AI_co-scientist/review]] — AI 공동 과학자의 개념적 기반과 비전을 제공한다.
