---
title: "134_Automating_the_practice_of_science_Opportunities_challenges"
authors:
  - "Sebastian Musslick"
  - "Laura K. Bartlett"
  - "Suyog H. Chandramouli"
  - "Marina Dubova"
  - "Fernand Gobet"
date: "2025"
doi: "10.1073/pnas.2401238121"
arxiv: ""
score: 4.5
essence: "과학적 실천(scientific practice)의 자동화(automation)가 발전함에 따라, 본 논문은 과학 자동화의 기회, 도전과제, 그리고 사회적 함의를 종합적으로 평가하고, 과학 자동화가 과학자의 업무 방식과 과학 패러다임을 어떻게 변화시킬지 탐색한다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/Structured_Research_Frameworks"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Musslick et al._2025_Automating the practice of science Opportunities, challenges, and implications.pdf"
---

# Automating the practice of science: Opportunities, challenges, and implications

> **저자**: Sebastian Musslick, Laura K. Bartlett, Suyog H. Chandramouli, Marina Dubova, Fernand Gobet, Thomas L. Griffiths, Jessica Hullman, Ross D. King, J. Nathan Kutz, Christopher G. Lucas, Suhas Mahesh, Franco Pestilli, Sabina J. Sloman, William R. Holmes | **날짜**: 2025 | **DOI**: [10.1073/pnas.2401238121](https://doi.org/10.1073/pnas.2401238121)

---

## Essence

과학적 실천(scientific practice)의 자동화(automation)가 발전함에 따라, 본 논문은 과학 자동화의 기회, 도전과제, 그리고 사회적 함의를 종합적으로 평가하고, 과학 자동화가 과학자의 업무 방식과 과학 패러다임을 어떻게 변화시킬지 탐색한다.

## Motivation

- **Known**: 산업 분야에서 자동화는 제조업 효율성과 생산성을 혁명적으로 변화시켰으며, 최근 AI, 소프트웨어, 컴퓨팅 하드웨어의 발전으로 과학에서도 자동화가 빠르게 도입되고 있음. 기능 유전체학(functional genomics), 화학 가설 생성(hypothesis generation), 신소재 발견(material discovery) 등 다양한 영역에서 자동화된 접근이 성과를 보이고 있음.

- **Gap**: 과학 자동화의 기술적 가능성에 대한 논의는 있으나, (1) 어떤 과학적 실천이 자동화되어야 하는가(규범적/인식론적 경계), (2) 현재의 기술적 제약은 무엇인가, (3) 과학의 목표와 인류 사회에 미치는 영향은 무엇인가에 대한 통합적 검토가 부족함.

- **Why**: 산업에서의 자동화가 노동자와 시장에 미친 부정적 영향을 고려할 때, 과학 자동화도 과학의 본질, 과학자의 역할, 과학적 이해의 질에 유사한 영향을 미칠 수 있으므로 사전적 검토가 필요함.

- **Approach**: 과학적 실천의 정의로부터 출발하여, 자동화의 목표적 경계(goal-related bounds)와 기술적 경계(technological bounds)를 구분하고, 현재의 자동화 실사례를 분석하며, 병목(bottleneck)과 윤리적·실천적 함의를 종합적으로 논의.

## Achievement

![Figure 1](figures/fig1.webp)

*Figure 1. 과학적 자동화의 기술적 도달 범위를 결정하는 4가지 요인: 입력 데이터의 가용성과 품질, 계산 복잡도, 하드웨어 엔지니어링 복잡도, 작업 목표의 주관성*

1. **자동화의 경계 명확화**: 
   - **목표적 경계**: 과학의 규범적 목표(윤리, 도덕, 사회적 가치)와 인식론적 목표(기술, 예측, 설명, 통제)를 구분. 규범적 가치 판단(어떤 연구 질문이 중요한가)과 이해(understanding)는 인간의 개입이 필수적이나, 예측과 통제는 자동화로부터 더 큰 이득을 얻을 수 있음.
   - **기술적 경계**: 자동화 난도를 결정하는 4가지 요인 도출 - (1) 입력의 가용성·신뢰성, (2) 계산 복잡도, (3) 하드웨어 복잡도(감각운동 작업의 로봇화), (4) 작업 목표의 주관성.

2. **현재 과학 자동화의 현황 분석**:
   - 자동화는 주로 명확한 목표와 잘 정의된 하위 작업을 가진 영역(정량적 가설 생성, 실험 설계, 데이터 수집, 분석·추론)에 집중됨.
   - 생물학(functional genomics), 화학(hypothesis generation), 재료과학(material discovery), 심리학(theory development) 등에서 새로운 발견을 촉진하는 자동화 도구들이 등장함.

3. **상호 보완성 입증**:
   - 방정식 발견(equation discovery)의 사례: 과거 고계산 복잡도의 진화 알고리즘(evolutionary computation) → 현재 대규모 저가 데이터 수집 + 개선된 컴퓨팅 하드웨어 활용으로 데이터-중심 머신러닝으로 전환. 한 요인의 개선이 다른 요인의 제약을 상쇄 가능함을 보여줌.

## How

- **목표적 검토 프레임**: 과학의 규범적 목표(사회적 필요성, 인간 건강) vs. 인식론적 목표(예측 vs. 이해)의 명시적 구분으로 각 영역별 자동화의 적절성 판단.

- **기술적 자동화 난도의 4-차원 분석**:
  - 입력 데이터: 구조화, 신뢰성, 접근성 평가
  - 계산 복잡도: 의사결정 변수 수, 탐색 공간 규모 분석
  - 하드웨어 엔지니어링: Moravec's paradox 적용 (감각운동 작업이 인지 작업보다 자동화 어려움)
  - 목표의 주관성: 작업 목표의 수학적 정의 가능성 평가

- **현황 분석 접근법**: 각 과학 분야에서 실제 성과를 낸 자동화 사례 검토를 통해 타당성 확보.

## Originality

- **통합적 프레임워크 제시**: 기존 연구들이 기술적 가능성만 강조한 반면, 목표적 경계(규범적·인식론적)와 기술적 경계를 명시적으로 구분하여 과학 자동화의 범위를 체계적으로 정의함.

- **학제적 관점**: 인지과학, 철학, 컴퓨터 과학, 심리학, 신경과학, 재료과학 등 12명의 다양한 분야 전문가가 협력하여 다각적 시각 제공.

- **Moravec's paradox의 과학 실천 적용**: 로봇공학의 잘 알려진 역설을 과학 자동화 맥락에서 새롭게 적용하여 하드웨어 복잡도의 중요성 강조.

- **윤리적·사회적 함의의 조기 검토**: 자동화가 광범위하게 도입되기 전에 과학자의 역할 변화, 과학적 이해의 침식, 과학 공동체의 접근성 등을 미리 검토.

## Limitation & Further Study

- **완성되지 않은 분석**: 논문의 처음 15,000자만 제공되었으므로, "Opportunities," "Bottlenecks," "Ethical and Practical Implications" 등 주요 섹션이 검토 대상에서 제외됨. 이들 섹션에서 구체적 기회 요소와 윤리적 논점이 상세히 논의될 것으로 예상.

- **기술적 경계의 역동성**: 4가지 요인이 시간에 따라 변하는 점(하드웨어 발전, 데이터 확보 용이성 증가)을 고려하면, 자동화 가능 범위는 지속적으로 확대될 것인데, 이에 따른 규범적 경계의 적응 방안이 추가 논의 필요.

- **구체적 정책 제안 부재**: 과학 자동화가 초래할 부정적 영향(과학자의 실업, 과학 이해의 축소, 연구 질문의 편향)을 어떻게 관리할 것인가에 대한 구체적 정책 방안은 제한적일 수 있음.

- **후속 연구 방향**:
  - 각 과학 분야별로 규범적·인식론적 목표와 현재 자동화 현황의 정렬 상태 평가
  - 자동화로 인한 과학자의 역할 변화와 과학 교육의 재설계 필요성 검토
  - 과학 자동화가 야기할 불평등(자동화 도구 접근성) 및 글로벌 과학 협력 구조 변화 예측


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4/5
- Significance: 5/5
- Clarity: 4/5
- Overall: 4.5/5

**총평**: 본 논문은 과학 자동화라는 시의적 주제를 목표적 경계(규범적·인식론적)와 기술적 경계의 구분을 통해 처음으로 체계적으로 분석한 포괄적 관점 논문으로, PNAS의 Perspective로서 과학 커뮤니티와 정책 입안자에게 중요한 개념적 틀을 제공한다. 다만 제공된 초반부만으로는 구체적 기회 분석과 윤리적 함의, 정책 제안의 깊이를 완전히 평가하기 어려우며, 자동화의 부정적 외부효과에 대한 실질적 대응 방안의 구체성이 향후 검토 대상이다.

## Related Papers

- 🏛 기반 연구: [[papers/575_Nobel_Turing_Challenge_creating_the_engine_for_scientific_di/review]] — 과학 자동화 프레임워크가 AI Scientist 구현의 실용적 기반을 제공한다.
- 🔗 후속 연구: [[papers/106_Artificial_Intelligence_in_Research_and_Development/review]] — 과학 자동화가 R&D 생산성에 미치는 경제적 영향을 구체적으로 분석한다.
- 🏛 기반 연구: [[papers/363_From_Reasoning_to_Learning_A_Survey_on_Hypothesis_Discovery/review]] — 가설 발견과 규칙 학습이 과학 자동화의 핵심 구성요소가 된다.
- 🏛 기반 연구: [[papers/099_An_autonomous_laboratory_for_the_accelerated_synthesis_of_in/review]] — 과학 자동화의 일반적 프레임워크가 자율 실험실 구현의 이론적 기반을 제공한다.
- 🧪 응용 사례: [[papers/363_From_Reasoning_to_Learning_A_Survey_on_Hypothesis_Discovery/review]] — 가설 발견과 규칙 학습이 과학 자동화의 핵심 인지적 구성요소가 된다.
- 🧪 응용 사례: [[papers/575_Nobel_Turing_Challenge_creating_the_engine_for_scientific_di/review]] — 과학 자동화의 구체적 구현체로서 AI Scientist를 통해 노벨-튜링 챌린지를 실현한다.
- 🏛 기반 연구: [[papers/878_What_ChatGPT_and_generative_AI_mean_for_science/review]] — 생성형 AI의 과학적 영향에 대한 종합적 분석이 과학 자동화 논의의 기반이 된다.
- 🔗 후속 연구: [[papers/106_Artificial_Intelligence_in_Research_and_Development/review]] — 과학 자동화가 R&D 생산성에 미치는 경제적 영향을 이론적으로 분석한다.
- 🏛 기반 연구: [[papers/705_SciAgents_Automating_Scientific_Discovery_Through_Bioinspire/review]] — 과학 실무 자동화의 기회와 도전에 대한 종합적 검토가 SciAgents 프레임워크 개발의 이론적 배경을 제공한다.
