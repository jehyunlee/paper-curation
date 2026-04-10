---
title: "352_From_AI_for_Science_to_Agentic_Science_A_Survey_on_Autonomou"
authors:
  - "Jiaqi Wei"
  - "Yuejin Yang"
  - "Xiang Zhang"
  - "Yuhan Chen"
  - "Xiang Zhuang"
date: "2025.10"
doi: "10.48550/arXiv.2508.14111"
arxiv: ""
score: 3.0
essence: "본 논문은 AI가 전문화된 계산 도구에서 자율적 과학 연구 파트너로 진화하는 과정을 체계화하며, **에이전틱 사이언스(Agentic Science)**를 AI for Science의 핵심 패러다임으로 위치지었다. 대규모 언어 모델(LLM)과 멀티모달 시스템을 통해 가설 생성, 실험 설계, 데이터 분석, 반복적 개선 등 과학적 발견의 전체 사이클을 자동화하는 AI 에이전트의 등장을 다룬다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/AI_Scientific_Discovery"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Wei et al._2025_From AI for Science to Agentic Science A Survey on Autonomous Scientific Discovery.pdf"
---

# From AI for Science to Agentic Science: A Survey on Autonomous Scientific Discovery

> **저자**: Jiaqi Wei, Yuejin Yang, Xiang Zhang, Yuhan Chen, Xiang Zhuang, Zhangyang Gao, Dongzhan Zhou, Guangshuai Wang, Zhiqiang Gao, Juntai Cao, Zijie Qiu, Ming Hu, Chenglong Ma, Shixiang Tang, Junjun He, Chunfeng Song, Xuming He, Qiang Zhang, Chenyu You, Shuangjia Zheng, Ning Ding, Wanli Ouyang, Nanqing Dong, Yu Cheng, Siqi Sun, Lei Bai, Bowen Zhou | **날짜**: 2025-10-20 | **DOI**: [10.48550/arXiv.2508.14111](https://doi.org/10.48550/arXiv.2508.14111)

---

## Essence

![Figure 1: AI for Science의 진화 단계](https://arxiv.org/html/2508.14111v2/x1.png)
*그림 1: 계산 도구에서 창의적 협력자까지 – AI의 4단계 여정. 에이전틱 사이언스는 AI for Science 내의 한 단계로, 주로 3단계(완전 에이전틱 발견)와 2단계(부분 에이전틱 발견)에 대응*

본 논문은 AI가 전문화된 계산 도구에서 자율적 과학 연구 파트너로 진화하는 과정을 체계화하며, **에이전틱 사이언스(Agentic Science)**를 AI for Science의 핵심 패러다임으로 위치지었다. 대규모 언어 모델(LLM)과 멀티모달 시스템을 통해 가설 생성, 실험 설계, 데이터 분석, 반복적 개선 등 과학적 발견의 전체 사이클을 자동화하는 AI 에이전트의 등장을 다룬다.

## Motivation

- **Known**: AI는 단백질 구조 예측(AlphaFold), 신약 발견, 재료 설계 등 특정 과학 문제 해결에 성공했으나, 기존 연구들은 프로세스 중심, 자율성 중심, 메커니즘 중심으로 단편화되어 있다.

- **Gap**: AI의 자율적 과학 발견 능력에 대한 통합 프레임워크와 도메인별 체계적 종합이 부족하다. 또한 생명과학, 화학, 재료과학, 물리학 전반에 걸친 아젠틱 시스템의 현황과 도전을 통합 관점에서 분석한 연구가 없다.

- **Why**: 과학 공동체가 AI 에이전트 설계, 평가, 배포에 대한 명확한 개념 틀과 실증적 근거가 필요하며, 이는 과학적 발견 가속화의 열쇠이다.

- **Approach**: 프로세스, 자율성, 메커니즘 관점을 통합한 포괄적 프레임워크를 제시하고, AI의 진화 단계(4 레벨)를 정의하며, 과학 에이전트의 5가지 핵심 능력과 4단계 워크플로우를 모델링한다.

## Achievement

![Figure 2: 자율적 과학 발견 연구 프레임워크](https://arxiv.org/html/2508.14111v2/x2.png)
*그림 2: 기초 능력, 핵심 프로세스, 생명과학·화학·재료과학·물리학에 걸친 연구 수준을 통합하는 자율적 과학 발견 연구 프레임워크*

1. **AI for Science의 진화 단계 체계화**
   - Level 1: 계산 오라클(Expert Tools) – 전문화된 비에이전트 모델, 인간의 지도 필수
   - Level 2: 자동화된 연구 보조자(Partial Agentic Discovery) – 부분적 자율성, 특정 작업에만 에이전시 발휘
   - Level 3: 자율적 과학 파트너(Full Agentic Discovery) – **에이전틱 사이언스의 주 초점**, 가설부터 이론 정제까지 자율 수행
   - Level 4: 생성적 아키텍처(Future Prospect) – 미래 지향적 단계

2. **과학 에이전트의 5가지 핵심 능력 규정**
   - (i) **추론 및 계획 엔진(Planning & Reasoning)**: CoT(Chain-of-Thought), ToT(Tree-of-Thought) 등으로 복잡한 과학 문제 해결
   - (ii) **도구 통합(Tool Use & Integration)**: 계산, 시뮬레이션, 실험 플랫폼, 데이터베이스 연결
   - (iii) **메모리 메커니즘(Memory Mechanisms)**: 장기 기억으로 학습 축적 및 반복 개선
   - (iv) **다중 에이전트 협업(Multi-Agent Collaboration)**: 전문화된 에이전트 간 상호작용
   - (v) **최적화 및 진화(Optimization & Evolution)**: 강화 학습, 진화 알고리즘으로 성능 개선

3. **과학 발견의 동적 4단계 워크플로우 모델링**
   - **1단계 관찰 및 가설 생성**: 데이터 분석 후 초기 가설 제시
   - **2단계 실험 계획 및 실행**: 설계된 실험 자동 수행, 피드백 루프
   - **3단계 데이터 및 결과 분석**: 정량적/정성적 분석, 통계적 검증
   - **4단계 합성, 검증 및 진화**: 이론 정제, 새로운 가설 도출

4. **4대 자연과학 도메인별 종합 분석**
   - **생명과학**: 유전체학(Genomics), 단백질 공학, 약물 발견 시스템
   - **화학**: 유기 합성 최적화, 생성적 분자 설계, 계산/양자 화학
   - **재료과학**: 신소재 발견 플랫폼, 자동 시뮬레이션 및 특성화
   - **물리학**: 천문학, 계산역학, 양자 컴퓨팅

5. **에이전틱 사이언스의 핵심 도전과제 및 미래 방향 제시**
   - 재현성 및 신뢰성 문제
   - 신규성 검증의 어려움
   - 과학적 추론의 투명성 부족
   - 윤리적·사회적 함의

## How

![Figure 3: 인간-에이전트 공동 발견 루프](https://arxiv.org/html/2508.14111v2/x3.png)
*그림 3: 인간 과학자가 고수준 방향을 제시하고 AI 에이전트가 자율적으로 탐색, 실험, 분석을 수행하는 협력 구조*

**방법론 및 접근:**

- **프레임워크 통합**: 기존의 3가지 단편화된 관점(프로세스 중심, 자율성 중심, 메커니즘 중심)을 Figure 2의 통합 프레임워크로 재구성하여 기초 능력 → 핵심 프로세스 → 도메인 실현의 계층적 연결 제시

- **형식적 정의**: Agentic Science를 "자율성(autonomy), 목표 지향적 추론(goal-driven reasoning), 반복 학습(iterative learning)"을 갖춘 AI 시스템으로 형식 정의

- **동적 워크플로우 모델링**: 과학 발견을 고정 순서가 아닌 **유연하고 동적으로 조합 가능한 4단계**로 모델링하여 복잡한 다학제 문제 대응

- **LLM 중심 기술 검토**: Intern-S1 등 최신 과학 특화 LLM의 추론 능력, 도구 사용 메커니즘, 멀티모달 통합 분석

- **도메인별 사례 중심 평가**: 각 도메인(생명과학, 화학, 재료과학, 물리학)에서 10개 이상의 세부 분야를 포함한 12개 이상의 구체적 응용 사례 제시

## Originality

- **통합 프레임워크의 창신성**: 기존 연구들이 프로세스, 자율성, 메커니즘을 분리하여 다룬 것과 달리, 본 논문은 이를 단일 통합 프레임워크로 통일하여 새로운 개념적 기반 제공

- **Agentic Science의 형식적 정의**: "AI as Autonomous Scientific Partner"를 형식 정의하고 Level 3로 명확히 위치지음으로써 용어의 모호성 제거

- **5가지 핵심 능력의 체계화**: 과학 에이전트가 갖춰야 할 필수 능력을 추론, 도구, 메모리, 협업, 최적화로 분류하여 설계 지침 제공

- **동적 4단계 워크플로우의 유연성 강조**: 기존의 고정 과학 방법론과 달리 **에이전트가 4단계를 유연하게 조합**할 수 있다는 실용적 통찰

- **광범위한 도메인 커버리지**: 생명과학, 화학, 재료과학, 물리학 전 분야에 걸친 체계적 종합으로 에이전틱 사이언스의 보편적 적용성 시연

- **미래 전망의 철학적 깊이**: "Nobel-Turing Test"라는 새로운 벤치마크 제시로 AI 과학자의 창의성과 신뢰성 평가 기준 제안

## Limitation & Further Study

- **실증적 평가의 부재**: 제시된 프레임워크가 이론 중심이며, 실제 에이전틱 시스템들이 모든 핵심 능력을 충분히 갖췄는지에 대한 정량적 비교 평가 부족

- **재현성 보장 메커니즘 미흡**: 논문에서 재현성을 도전과제로 지적하나, 구체적 해결방안이 제한적임. 어떻게 에이전트의 실험 결과를 독립적으로 검증할 것인가의 방법론 부재

- **인간-에이전트 상호작용의 정규화 부족**: Figure 3에서 협력 루프를 시각화하나, 인간이 언제 개입하고 어느 정도 자율성을 부여할지에 대한 명확한 가이드라인 미제시

- **도메인별 난이도 편차 분석 부족**: 4가지 도메인이 모두 동일한 수준의 자동화 가능성을 갖는지, 생명과학과 물리학 사이의 차이가 무엇인지 상대적 분석 미흡

- **윤리 및 사회적 영향의 심화 분석 필요**: 섹션 9.4에서 윤리적 차원을 언급하나, 과학 부정행위 자동화, 데이터 편향 확대, 과학자 실직 등의 구체적 위험과 완화 전략에 대한 논의 깊이 부족

- **후속 연구 방향**:
  - 에이전틱 시스템의 성능을 정량적으로 비교하는 벤치마크 및 평가 지표 개발
  - 각 도메인별 자동화 난이도 곡선(automation difficulty curve) 분석
  - 인간 과학자와 AI 에이전트의 최적 협업 비율과 인터페이스 설계 연구
  - Nobel-Turing Test의 구체적 평가 기준 및 구현 프레임워크 제시


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4/5
- Significance: 3/5
- Clarity: 3/5
- Overall: 3/5

## Related Papers

- 🔄 다른 접근: [[papers/795_The_AI_Scientist_Towards_Fully_Automated_Open-Ended_Scientif/review]] — 에이전틱 사이언스와 AI 과학자의 서로 다른 자율적 과학 연구 패러다임을 비교하여 각각의 강점과 한계를 명확히 할 수 있다.
- 🧪 응용 사례: [[papers/575_Nobel_Turing_Challenge_creating_the_engine_for_scientific_di/review]] — 에이전틱 사이언스 프레임워크를 과학 발견 엔진 구축에 적용하여 노벨-튜링 챌린지와 같은 야심찬 목표를 달성할 수 있다.
- 🏛 기반 연구: [[papers/857_Unlocking_the_Potential_of_AI_Researchers_in_Scientific_Disc/review]] — AI for Science에서 Agentic Science로의 전환이 AI 연구자 잠재력 활용의 이론적 기반을 제공한다.
- 🏛 기반 연구: [[papers/137_Autonomous_Agents_for_Scientific_Discovery_Orchestrating_Sci/review]] — 과학을 위한 AI에서 에이전트 과학으로의 전환에 대한 포괄적 조사가 자율 과학 발견의 이론적 토대를 제공한다
- 🏛 기반 연구: [[papers/922_Vibe_physics_The_AI_grad_student/review]] — 에이전틱 사이언스의 이론적 틀이 AI 대학원생 구현의 기초 개념과 방법론을 제공한다.
