---
title: "353_From_Automation_to_Autonomy_A_Survey_on_Large_Language_Model"
authors:
  - "Tianshi Zheng"
  - "Zheye Deng"
  - "Hong Ting Tsang"
  - "Weiqi Wang"
  - "Jiaxin Bai"
date: "2025.05"
doi: "미제공"
arxiv: ""
score: 4.4
essence: "대규모 언어모델(LLM)이 과학 발견에서 단순한 작업 자동화 도구에서 자율적 에이전트로 진화하는 패러다임 변화를 체계적으로 분석한 종합 조사 논문이다. 과학적 방법론의 단계별 관점에서 LLM의 자율성 수준을 3단계 분류법으로 제시하며, 미래의 AI 기반 과학 발견의 방향을 제시한다."
tags:
  - "cat/Academic_Peer_Review_Automation"
  - "sub/AI_Publishing_Trends"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Zheng et al._2025_From Automation to Autonomy A Survey on Large Language Models in Scientific Discovery.pdf"
---

# From Automation to Autonomy: A Survey on Large Language Models in Scientific Discovery

> **저자**: Tianshi Zheng, Zheye Deng, Hong Ting Tsang, Weiqi Wang, Jiaxin Bai, Zihao Wang, Yangqiu Song | **날짜**: 2025-05-19 | **DOI**: [미제공](https://doi.org/)

---

## Essence

![Figure 1](figures/fig1.webp)
*과학적 방법의 6단계와 각 단계의 LLM 응용 분야*

대규모 언어모델(LLM)이 과학 발견에서 단순한 작업 자동화 도구에서 자율적 에이전트로 진화하는 패러다임 변화를 체계적으로 분석한 종합 조사 논문이다. 과학적 방법론의 단계별 관점에서 LLM의 자율성 수준을 3단계 분류법으로 제시하며, 미래의 AI 기반 과학 발견의 방향을 제시한다.

## Motivation

- **Known**: LLM의 계획 능력, 복잡한 추론, 명령 따르기 능력 등이 이미 입증되었으며, 이를 에이전트 워크플로우와 통합하면 웹 탐색, 도구 사용, 코드 실행, 데이터 분석 등 고급 기능 수행 가능
- **Gap**: 기존 조사 연구들은 학문 분야별 응용(domain-specific)이나 LLM 능력의 정적 스냅샷에 초점을 두어, **LLM의 증가하는 자율성과 과학적 방법 전반에 걸친 진화하는 역할**을 종합적으로 다루지 못함
- **Why**: LLM 기술의 빠른 발전과 복잡한 연구 시스템으로의 심화된 통합으로 인해, 현재의 이해를 구조화하고 미래 방향을 명확히 하기 위한 개념적 프레임워크가 필수적
- **Approach**: 과학적 방법의 6단계(관찰-문제 정의, 가설 개발, 실험 및 데이터 수집, 데이터 분석, 결론 도출, 반복 및 개선)를 기축으로 하여 3단계 자율성 분류법(Tool/Analyst/Scientist) 제시

## Achievement

![Figure 2](figures/fig2.webp)
*LLM 기반 과학 발견 연구의 분류 및 진화*

1. **3단계 자율성 분류 프레임워크 개발**: 
   - **Level 1 (Tool)**: 명시적 인간 감독 하에 특정 작업 자동화 (문헌 요약, 코드 생성 등)
   - **Level 2 (Analyst)**: 중간 단계에서 인간 개입 감소, 복잡한 정보 처리 및 분석 수행
   - **Level 3 (Scientist)**: 가설 수립부터 결과 해석까지 거의 모든 연구 단계 자율적 수행

2. **과학적 방법의 6단계별 LLM 응용 체계화**: 각 단계(문헌 검색, 아이디어 생성, 실험 설계, 데이터 분석, 결론 도출, 반복 개선)에서의 LLM 역할 명확화

3. **주요 도전과제 및 미래 방향 제시**: 
   - 완전 자율적 발견 사이클
   - 로봇 자동화 및 물리적 세계와의 상호작용
   - 지속적 자기 개선
   - 투명성과 해석 가능성
   - 윤리적 거버넌스

## How

- **과학적 방법론 기반 분류**: Popper와 Kuhn의 과학적 방법을 6단계로 재구성하여 LLM 응용의 체계적 맵핑
- **자율성 스펙트럼 설정**: 인간 개입 수준, LLM 역할, 작업 범위, 에이전트 워크플로우의 복잡성을 기준으로 3단계 정의
- **문헌 기반 사례 분류**: 기계학습, 자연과학, 일반 연구 등 분야별로 200+개 연구 사례를 분류하고 단계별 매핑
- **통합 분석**: 각 분야의 방법론/프레임워크, 벤치마크/평가, 에이전트 워크플로우를 통합 분석하여 진화 추이 파악

## Originality

- **혁신적 분류 체계**: 기존의 도메인별 또는 기술별 분류와 달리, **LLM의 자율성 진화 추이**를 중심으로 한 새로운 분류법 제시
- **과학적 방법론과의 정렬**: 과학의 근본적 방법론을 LLM 능력과 체계적으로 연결하여 이론적 근거 제공
- **포괄적 범위**: 문헌 검색부터 완전 자율적 발견 사이클까지, 과학 발견의 모든 단계를 통합적으로 분석
- **미래 지향적 프레임워크**: 현재 기술 동향뿐 아니라 로봇 자동화, 자기 개선, 윤리 거버넌스 등 향후 중요 과제를 명시적으로 제시

## Limitation & Further Study

**한계**:
- 조사 논문 특성상 각 분야의 깊이 있는 기술적 분석 제한
- Level 3 (Scientist) 수준의 시스템은 아직 초기 단계로, 실제 과학 발견의 유효성 검증 사례 제한
- 특정 과학 분야(예: 실험 생물학, 천문학)에서의 실제 도입 사례 부족
- 윤리적, 사회적 영향에 대한 심층 분석 미흡

**후속 연구**:
- 각 자율성 단계별 성능 평가 벤치마크 개발
- 인간-AI 협업의 최적 지점 규명
- 과학 분야별(물리학, 화학, 생물학, 의학 등) 맞춤형 에이전트 설계
- 재현 가능성(reproducibility)과 신뢰성 검증 메커니즘
- LLM 기반 발견 시스템의 장기적 사회적 영향 평가


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4/5
- Significance: 4.5/5
- Clarity: 4.5/5
- Overall: 4.4/5

**총평**: LLM의 과학 발견 응용을 자율성 진화라는 새로운 관점에서 체계적으로 분석한 중요한 종합 논문으로, 학문 분야 간 통합적 이해를 제공하고 미래 연구 방향을 명확히 제시하나, 각 사례의 실제 과학적 유효성 검증과 윤리적 논의의 심화가 필요하다.

## Related Papers

- 🔄 다른 접근: [[papers/004_A_Comprehensive_Survey_of_Scientific_Large_Language_Models_a/review]] — 과학 분야 LLM의 포괄적 조사로 자율성보다는 응용 분야에 초점을 맞춘 상호 보완적 관점을 제공한다.
- 🔗 후속 연구: [[papers/795_The_AI_Scientist_Towards_Fully_Automated_Open-Ended_Scientif/review]] — 완전 자동화된 AI 과학자 개발 사례로 본 논문이 제시한 자율적 에이전트로의 진화를 실제 구현한다.
- 🏛 기반 연구: [[papers/824_Towards_AI_for_science_developing_a_conceptual_basis_for_tra/review]] — AI for Science의 개념적 기반을 제공하여 자동화에서 자율성으로의 패러다임 전환을 이론적으로 뒷받침한다.
- 🔄 다른 접근: [[papers/004_A_Comprehensive_Survey_of_Scientific_Large_Language_Models_a/review]] — LLM의 자율성 진화보다는 분야별 응용에 초점을 맞춘 상호 보완적 조사 연구이다.
