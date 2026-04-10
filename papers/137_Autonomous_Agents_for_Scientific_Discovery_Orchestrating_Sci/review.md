---
title: "137_Autonomous_Agents_for_Scientific_Discovery_Orchestrating_Sci"
authors:
  - "Lianhao Zhou"
  - "Hongyi Ling"
  - "Cong Fu"
  - "Yepeng Huang"
  - "Michael Sun"
date: "2025.10"
doi: "-"
arxiv: ""
score: 4.25
essence: "대규모 언어 모델(LLM) 기반 자율 에이전트(Scientific Agents)가 과학 발견의 전체 생명주기를 자동화하고 가속화할 수 있는 새로운 패러다임을 제시한다. 이들 에이전트는 자연언어, 프로그래밍 코드, 물리 정보를 통합하여 인간 과학자, 계산 도구, 물리 장비와 유연하게 상호작용한다."
tags:
  - "cat/AI-Powered_Scientific_Research_Frameworks"
  - "sub/Scientific_Agent_Frameworks"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Zhou et al._2025_Autonomous Agents for Scientific Discovery Orchestrating Scientists, Language, Code, and Physics.pdf"
---

# Autonomous Agents for Scientific Discovery: Orchestrating Scientists, Language, Code, and Physics

> **저자**: Lianhao Zhou, Hongyi Ling, Cong Fu, Yepeng Huang, Michael Sun, Wendi Yu, Xiaoxuan Wang, Xiner Li, Xingyu Su, Junkai Zhang, Xiusi Chen, Chenxing Liang, Xiaofeng Qian, Heng Ji, Wei Wang, Marinka Zitnik, Shuiwang Ji | **날짜**: 2025-10-10 | **DOI**: -

---

## Essence

![Figure 1](https://arxiv.org/html/2510.09901v1/x1.png) *그림 1: AI 기반 과학 발견을 위한 3단계 워크플로우 개요. 가설 발견(Phase 1) → 실험 설계 및 실행(Phase 2) → 결과 분석 및 개선(Phase 3)*

대규모 언어 모델(LLM) 기반 자율 에이전트(Scientific Agents)가 과학 발견의 전체 생명주기를 자동화하고 가속화할 수 있는 새로운 패러다임을 제시한다. 이들 에이전트는 자연언어, 프로그래밍 코드, 물리 정보를 통합하여 인간 과학자, 계산 도구, 물리 장비와 유연하게 상호작용한다.

## Motivation

- **Known**: 컴퓨팅은 과학 발견의 핵심이며, 최근 LLM의 발전으로 자동화된 과학 에이전트가 등장했다. 기존 연구들은 일반 LLM 에이전트나 특정 분야의 에이전트를 다루지만, 전체 과학 발견 사이클을 포괄하는 통합 시스템 분석이 부족하다.

- **Gap**: 개별 과학 작업에 특화된 LLM은 많지만, 가설 발견부터 결과 분석까지 전체 과학 발견 사이클을 지원하는 통합적이고 체계적인 에이전트 프레임워크의 리뷰와 분석이 부재한다.

- **Why**: 인간 주도 발견 과정은 높은 비용, 장시간 투자, 인지편향, 방대한 가설 공간의 제한된 탐색 등의 문제가 있다. 증가하는 데이터의 복잡성과 규모를 효율적으로 분석하기 위한 새로운 접근이 필요하다.

- **Approach**: 과학 발견 프로세스를 3단계(가설 발견, 실험 설계 및 실행, 결과 분석 및 개선)로 구조화하고, 각 단계에서 LLM 에이전트가 사용하는 다양한 방법론들을 체계적으로 분석하며, 영역별(화학, 생물학, 물리학, 재료과학 등) 응용 성과와 한계를 통합적으로 검토한다.

## Achievement

![Figure 2](https://arxiv.org/html/2510.09901v1/x2.png) *그림 2: 과학 발견의 세 단계별 LLM 기반 에이전트의 역할에 대한 포괄적 개요*

1. **3단계 과학 발견 프레임워크 제시**: 
   - Phase 1 (가설 발견): 지식 추출(Knowledge Extraction) → 가설 생성(Hypothesis Generation) → 가설 검증(Hypothesis Screening & Validation)
   - Phase 2 (실험 설계 및 실행): RAG 기반 계획, 템플릿 기반 설계, 기존 도구 활용, 새로운 도구 생성
   - Phase 3 (결과 분석 및 개선): 자동 자체 수정, 인간-in-the-loop 반복 개선, 외부 피드백 통합

2. **다양한 응용 성과 분류 및 정리**:
   - 과학 기초 모델(BioBERT, BioGPT, Galactica, ChemDFM 등) 활용
   - 실제 구현 사례: ChemMiner, MatViX, nanoMINER(다중모달 지식 추출), CLADD, CASSIA(가설 생성), POPPER, SCIMON(가설 검증)
   - 영역별 성공 사례: ChemCrow, AgentMD(화학), CRISPR-GPT, Biomni(생물학), 재료 설계 에이전트(재료과학) 등

3. **에이전트 자율성 수준 및 기능 구조 체계화**: 
   - RAG 기반 전략, 지식 그래프 통합, 다중 에이전트 협력, 진화 알고리즘 기반 최적화 등 다양한 구현 방식의 장단점 분석

## How

![Figure 3](https://arxiv.org/html/2510.09901v1/x3.png) *그림 3: 자율 과학 발견을 위한 정보이론적 프레임워크*

**Phase 1: 가설 발견 메커니즘**
- 지식 추출: 과학 문헌, 데이터베이스(PubMed, Materials Project), 논문 및 도표에서 RAG(Retrieval-Augmented Generation) 또는 다중모달 LLM을 통해 구조화된 지식 추출
- 가설 생성: 프롬프트 기반(prompt-based), 지식 그래프 활용, 다중 에이전트 상호작용, 진화 알고리즘 결합을 통한 새로운 가설 생성
- 검증: 메트릭 기반 필터링(novelty, feasibility, significance) 또는 에이전트 기반 평가

**Phase 2: 실험 설계 및 실행**
- 설계: RAG 기반 계획(유사 선행 연구 참고), 인간의 고수준 지침(human guidance), 사전 정의된 액션 템플릿, 실행 후 피드백 통합
- 실행: 도구 사용(Tool Use) - 기존 시뮬레이터/로봇/DB 활용 코드 생성
- 실행: 도구 생성(Tool Creation) - 새로운 알고리즘/도구의 코드 자동 생성 (ToolUniverse, MAPPS, CodePDE, AlphaEvolve, TOOLMAKER 등)
- 다중 에이전트 계층 구조: 단일 에이전트의 한계를 극복하기 위해 전문가 역할(설계자, 실행자, 평가자) 분담

**Phase 3: 결과 분석 및 개선**
- 자동 자체 수정: 에이전트가 결과를 검토하고 문제를 식별하여 워크플로우 개선
- 인간-in-the-loop: 인간 피드백을 반복적으로 통합하여 점진적 개선
- 외부 평가: 실험 재검증, 동료 검토(peer review) 프로세스 자동화

## Originality

- **포괄적 통합 분석**: 기존 논문들이 특정 단계나 분야에 집중한 반면, 본 논문은 가설 발견부터 결과 정제까지 전체 과학 발견 사이클을 통일된 프레임워크로 분석
  
- **정보이론 기반 형식화**: 단순한 사례 모음이 아닌 정보이론적(information-theoretic) 관점에서 자율 과학 발견의 수학적 기초 제시

- **다양한 도구 생성 전략의 체계화**: RAG 기반, 템플릿 기반, 반사적(reflective) 접근, 다중 에이전트 계층 구조 등 도구 생성/활용의 다양한 패러다임을 분류

- **영역별 응용의 상세 분류**: 화학, 생물학, 물리학, 재료과학, 천문학, 의학 등 여러 과학 분야에서의 구체적 구현 사례를 체계적으로 정리한 분류 체계(taxonomy)

- **한계와 개방형 문제의 명확한 제시**: 단순히 성과만이 아니라 현존 방법론의 제약 조건과 미해결 문제를 비판적으로 평가

## Limitation & Further Study

**주요 한계:**

1. **에이전트의 일반화 능력 부족**: 특정 분야나 문제 유형에 최적화된 에이전트가 다른 영역으로의 전이(transfer)가 어렵다. 기초 모델의 도메인 한계가 여전하다.

2. **정확성 및 신뢰성 문제**: LLM의 할루시네이션(hallucination), 잘못된 화학식 생성, 부정확한 물리 계산 등으로 인한 검증 단계의 필요성이 증가하며 실제 실험 자동화에서 오류율이 여전히 높다.

3. **인간-AI 협력의 부정확한 정의**: 많은 시스템이 "자율"이라 표방하지만 실제로는 인간의 지속적인 감독과 개입을 요구한다. 진정한 자율성의 수준을 정량적으로 정의하기 어렵다.

4. **계산 효율성과 비용**: 반복적인 LLM 호출, 다중 모달 정보 처리로 인한 높은 계산 비용과 지연. 특히 대규모 병렬 실험에는 부적합하다.

5. **물리 제약과 안전성**: 신약 개발, 화학 합성 등 위험 물질 취급 시 에이전트의 안전성 검증 부재. 규제 요구사항(FDA 승인 등)과의 불일치.

6. **동적 적응성 제한**: 예상 밖의 결과나 새로운 현상 발생 시 에이전트의 적응 능력이 제한적. 장기간의 반복 실험에서의 학습 능력 부족.

**향후 연구 방향:**

- 크로스 도메인 전이 학습(cross-domain transfer) 향상을 위한 메타학습(meta-learning) 적용
- 물리 기반 제약(physics-informed constraints) 통합으로 신뢰성 있는 도구 생성
- 명시적 지식 그래프와 신경망 모델의 하이브리드 접근
- 실시간 환경 피드백을 통한 온라인 학습(online learning) 메커니즘
- 윤리 및 안전 프레임워크 개발(safety-critical discovery tasks)
- 다학제적 에이전트 시스템의 표준화된 평가 벤치마크 구축

## Evaluation

- **Novelty**: 4/5
  - 전체 과학 발견 사이클을 다루는 통합 프레임워크는 참신하나, 개별 단계에서의 기술 혁신은 기존 연구의 조합
  
- **Technical Soundness**: 4/5
  - 체계적인 분류와 정보이론 기반 형식화가 견고하나, 구체적인 기술 검증 실험이 제시되지 않았고 개별 방법론의 수학적 엄밀성 검토 필요
  
- **Significance**: 5/5
  - LLM 기반 과학 에이전트의 발전을 위한 로드맵 제공, 산학계에 즉시 적용 가능한 실전적 가치, 향후 자율 과학 발견의 표준 참고자료로 활용 가능성 높음
  
- **Clarity**: 4/5
  - 명확한 3단계 프레임워크와 상세한 분류 체계가 있으나, 초반부의 정보량이 많아 진입 난이도가 높으며, 각 방법론 간 성능 비교가 정량적으로 부족
  
- **Overall**: 4.25/5

**총평**: 이 논문은 LLM 기반 과학 에이전트의 현황을 가장 포괄적으로 정리한 의미 있는 리뷰 논문으로, 과학 발견의 전체 사이클을 통합하는 프레임워크와 정보이론적 형식화를 제시한 점에서 학술적·실무적 기여가 크다. 다만 상위 아키텍처의 통합보다는 기존 방법들의 조직적 분류에 무게가 있으며, 제시된 한계점들(일반화 능력, 안전성, 실제 효율성)이 실제 응용 단계에서 얼마나 극복되었는지에 대한 심화 분석이 필요하다.

## Related Papers

- 🧪 응용 사례: [[papers/088_AI4Research_A_Survey_of_Artificial_Intelligence_for_Scientif/review]] — 과학 발견 자동화의 구체적 구현체로서 AI4Research 프레임워크의 실제 적용 사례를 보여준다
- 🏛 기반 연구: [[papers/352_From_AI_for_Science_to_Agentic_Science_A_Survey_on_Autonomou/review]] — 과학을 위한 AI에서 에이전트 과학으로의 전환에 대한 포괄적 조사가 자율 과학 발견의 이론적 토대를 제공한다
- 🔗 후속 연구: [[papers/795_The_AI_Scientist_Towards_Fully_Automated_Open-Ended_Scientif/review]] — 완전 자동화된 과학 발견을 자율 과학 에이전트의 구체적 실현으로 확장할 수 있다
