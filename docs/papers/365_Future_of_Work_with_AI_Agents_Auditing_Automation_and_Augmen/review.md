---
title: "365_Future_of_Work_with_AI_Agents_Auditing_Automation_and_Augmen"
authors:
  - "Yijia Shao"
  - "Humishka Zope"
  - "Yucheng Jiang"
  - "Jiaxin Pei"
  - "David Nguyen"
date: "2025.06"
doi: "10.48550/arXiv.2506.06576"
arxiv: ""
score: 0
essence: "본 논문은 미국 전역 104개 직종, 844개 과제에 걸쳐 1,500명의 현장 워커와 52명의 AI 전문가 데이터를 통합한 WORKBank 데이터베이스를 구축하여, AI 에이전트의 자동화 및 증강 가능성에 대한 체계적인 감시 평가를 제시한다. 특히 단순 자동화-비자동화 이분법을 벗어나 Human Agency Scale (HAS) 이라는 인간 중심의 스케일을 도입함으로써, 워커 선호도와 기술 역량 간의 불일치를 드러내고 향후 인적 역량의 변화를 예측한다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/Multi-agent_Task_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Shao et al._2025_Future of Work with AI Agents Auditing Automation and Augmentation Potential across the U.S. Workfo.pdf"
---

# Future of Work with AI Agents: Auditing Automation and Augmentation Potential across the U.S. Workforce

> **저자**: Yijia Shao, Humishka Zope, Yucheng Jiang, Jiaxin Pei, David Nguyen, Erik Brynjolfsson, Diyi Yang | **날짜**: 2025-06-11 | **DOI**: [10.48550/arXiv.2506.06576](https://doi.org/10.48550/arXiv.2506.06576)

---

## Essence

![Figure 1](figures/fig1.webp)
*Figure 1: 감시 프레임워크의 개요 및 핵심 통찰. 프레임워크는 워커 선호도와 기술적 타당성에 대한 이중 관점을 포착하며, 구조화된 프롬프트와 음성 강화 인터페이스를 통해 참여자의 추론을 안내한다.*

본 논문은 미국 전역 104개 직종, 844개 과제에 걸쳐 1,500명의 현장 워커와 52명의 AI 전문가 데이터를 통합한 WORKBank 데이터베이스를 구축하여, AI 에이전트의 자동화 및 증강 가능성에 대한 체계적인 감시 평가를 제시한다. 특히 단순 자동화-비자동화 이분법을 벗어나 Human Agency Scale (HAS) 이라는 인간 중심의 스케일을 도입함으로써, 워커 선호도와 기술 역량 간의 불일치를 드러내고 향후 인적 역량의 변화를 예측한다.

## Motivation

- **Known**: LLM과 기초 모델(foundation model) 기반 AI 에이전트(goal-directed systems)가 직업 영역에 빠르게 통합되고 있으며, 미국 노동자의 약 80%가 LLM의 영향을 받을 가능성이 제기되고 있음. 일부 연구는 생산성 향상을 보여주지만 일자리 대체, 인간 자율성 감소, 과도한 자동화 의존성에 대한 우려가 존재.

- **Gap**: 기존 연구는 소프트웨어 엔지니어링, 고객 지원 등 제한된 분야에 집중되어 다양한 직무의 복잡성을 포착하지 못함. 또한 자본의 이익(수익성 높은 과제)을 중심으로 분석하여 워커의 가치관을 충분히 반영하지 못함. 현존 데이터 기반 접근법은 미래 전망이 제한적.

- **Why**: AI 에이전트 개발을 워커의 실제 요구와 정렬하고, 책임감 있는 AI 도입을 위해서는 직무 수준의 세분화된 감사와 워커 중심의 관점이 필수적.

- **Approach**: O*NET 데이터베이스 기반의 과제별 감시 프레임워크 개발. 음성 강화 미니 인터뷰를 통해 워커의 미묘한 선호도 포착. Human Agency Scale (H1-H5)을 통해 자동화-증강 스펙트럼의 인간 관여도 정량화. AI 전문가 평가와의 이중 관점 통합.

## Achievement

![Figure 2](figures/fig2.webp)
*Figure 2: Human Agency Scale (HAS) 단계. H1(완전 자동화)부터 H5(인간 관여 필수)까지 5단계로 인간 중심의 렌즈를 제공한다.*

![Figure 4](figures/fig4.webp)
*Figure 4: 현장 워커의 1차 데이터는 AI 에이전트 자동화에 대한 긍정적 태도를 드러낸다.*

1. **워커의 자동화 선호도**: 과제의 46.1%에서 워커들은 일자리 손실 우려와 업무 만족도를 고려한 후에도 AI 에이전트 자동화에 긍정적 태도를 표현. 자동화 동기는 주로 고가치 업무에 집중하기 위한 시간 확보이며, 산업별로 상이한 트렌드 존재.

2. **선호도-역량 불일치의 시각화**: 워커 선호도와 기술 역량 간 불일치를 "Automation Green Light Zone"(높은 선호도·높은 역량), "Automation Red Light Zone"(높은 역량·낮은 선호도), "R&D Opportunity Zone"(높은 선호도·낮은 역량), "Low Priority Zone"(낮은 선호도·낮은 역량)의 4개 영역으로 분류. Y Combinator 회사-과제 매핑의 41.0%가 Low Priority Zone과 Red Light Zone에 집중되어 있는 반면, Green Light Zone과 Opportunity Zone의 유망 과제는 저평가.

3. **Human Agency Scale의 공유 언어**: 45.2%의 직종에서 H3(동등한 파트너십)이 워커 선호도의 주된 수준이며, 이는 인간-에이전트 협력의 잠재력을 강조. 그러나 전반적으로 워커들은 더 높은 인간 자율성을 선호하여, AI 역량 발전에 따른 마찰 가능성을 시사.

4. **인적 역량의 구조적 변화**: 정보 처리 능력에서 대인 관계 역량으로의 이동. 과제-핵심 기술 매핑 분석 결과, 전통적 고임금 기술인 정보 분석(analyzing information)의 중요도는 감소 반면, 대인 관계 및 조직 관리 기술의 중요성 증가. 개인에게 요구되는 기술 범위의 확대 경향.

## How

![Figure 2](figures/fig2.webp)
*Figure 2: Human Agency Scale (HAS)의 5단계 구조와 팀 역학 모델*

**감시 프레임워크의 핵심 설계 원칙 및 방법:**

- **과제 수준의 세분화**: O*NET 데이터베이스에서 추출한 복잡한 다단계 직무 과제(예: "Marketing Managers: Compile lists describing product or service offerings") 중심의 감사. 직종 수준이 아닌 과제 수준의 분석으로 문맥의존적 특성 포착.

- **컴퓨터 호환 과제 범위**: AI 에이전트의 영향 범위를 소프트웨어 도구 활용 가능 과제로 제한(물리적 행동 제외). AI 에이전트 정의: "사용자 또는 다른 시스템을 대신하여 워크플로우를 설계하고 이용 가능한 소프트웨어 도구를 활용하여 자율적으로 과제를 수행할 수 있는 시스템."

- **음성 강화 미니 인터뷰**: 구조화된 프롬프트와 음성 인터페이스를 통해 현장 워커(domain workers)로부터 미묘하고 맥락적 선호도 수집. 대면 설문조사에 가까운 풍부한 응답 유도.

- **Human Agency Scale (HAS) 도입**: SAE 자동화 수준(SAE L0-L5)의 "AI 우선" 관점과 달리, HAS는 인간 중심의 렌즈를 제공:
  - H1: AI 에이전트가 과제를 완전 자동 처리
  - H2: AI 에이전트가 최적 성능을 위해 최소한의 인간 입력 필요
  - H3: AI 에이전트와 인간의 동등한 파트너십
  - H4: AI 에이전트가 과제 완료를 위해 인간 입력 필요
  - H5: AI 에이전트가 지속적 인간 관여 없이 기능 불가

- **이중 관점 통합**: 1,500명의 현장 워커 선호도 + 52명의 AI 전문가 기술 역량 평가. 2025년 1월-5월 수집된 데이터로 WORKBank 데이터베이스 구축(104개 직종, 844개 과제).

- **선호도-역량 매트릭스**: 워커 선호도(자동화 열망)와 기술적 역량을 교차 분석하여 4개 영역 도출. 각 영역에 대한 전략적 시사점 제시.

- **핵심 기술-임금-인간 자율성 연계**: 각 과제의 필요 기술을 분류하고, 임금 수준 및 요구되는 인간 관여도와 비교하여 인적 역량의 장기적 변화 추적.

## Originality

- **최초의 대규모 다직종 과제 수준 감시**: 104개 직종, 844개 과제에 걸친 미국 최초의 체계적 AI 에이전트 감시 평가. 기존의 소수 분야(SW 엔지니어링, CS) 중심 연구에서 탈피하여 전국 노동력의 다양성 포착.

- **Human Agency Scale의 혁신적 도입**: 자동화-증강 스펙트럼을 인간 중심의 5단계 척도로 재개념화. SAE 등 기존 자동화 스케일의 기술 중심 관점을 보완하는 인간 자율성 프레임워크 제시.

- **워커 중심의 과학적 방법론**: 기술적 가능성 평가뿐 아니라 현장 워커의 1차 선호도를 음성 인터뷰 방식으로 수집. 자본 이익이 아닌 노동자 가치관에 기반한 균형잡힌 분석.

- **선호도-역량 불일치의 시각화 및 분류**: 4개 영역 매트릭스를 통해 현재 AI 개발 투자와 워커 실제 요구 간 갭을 명확히 드러냄. Y Combinator 데이터 분석으로 산업 현황 검증.

- **확장 가능한 데이터 기반**: WORKBank를 공개 가능한 구조의 데이터베이스로 설계하여, 기술 발전과 워커 선호도 변화를 지속적으로 추적할 수 있는 기반 제공.

- **인적 역량 변화의 조기 신호 제시**: 정보 처리 → 대인 관계 역량으로의 구조적 이동을 데이터 기반으로 시각화. 향후 교육 및 인력 양성 정책의 방향성 제시.

## Limitation & Further Study

- **시간 제약성**: 2025년 1월-5월 수집 데이터로 구성되어 빠르게 진화하는 AI 기술 역량의 시간 경과에 따른 변화를 포착하지 못함. 정기적 업데이트 및 종단적(longitudinal) 추적 필요.

- **워커 표본의 표대표성**: 1,500명의 워커 샘플이 각 직종 및 인구통계학적 집단을 충분히 대표하는지 불명확. 특히 저소득층, 소수집단, 지역적 다양성에 대한 샘플 대표성 검증 필요.

- **과제 정의의 주관성**: O*NET의 과제 설명이 일반화되어 있어, 실제 직장의 구체적이고 맥락적 변이(contextual variation)를 완전히 포착하지 못할 가능성. 특정 기업/조직 수준의 세분화 분석 필요.

- **AI 전문가 평가의 편향**: 52명의 AI 전문가 선정 기준, 배경 다양성, 평가 방법론의 객관성 정도가 명확하지 않음. 기술적 낙관주의 편향 가능성.

- **인과성 규명의 부족**: 선호도와 역량의 불일치가 과제 특성, 워커 특성, 산업 특성 중 어느 것에서 비롯되었는지의 원인 분석 부재.

- **워커 저항(resistance) 및 적응 비용 미포함**: 기술적으로 가능하고 워커가 선호하더라도, 조직 수준의 저항, 전환 비용(reskilling cost), 사회적 부작용 등의 현실적 장벽이 충분히 분석되지 않음.

- **후속 연구 방향**:
  - 업종별·지역별·인구통계학적 세분화 분석 확대
  - AI 에이전트 실제 도입 기업과의 연계 연구로 현실성 검증

## Related Papers

- 🏛 기반 연구: [[papers/865_Vending-Bench_A_Benchmark_for_Long-Term_Coherence_of_Autonom/review]] — AI 에이전트의 장기간 일관성 평가에서 업무 자동화 감시 평가의 이론적 기반을 제공한다.
- 🔗 후속 연구: [[papers/793_The_Adoption_and_Usage_of_AI_Agents_Early_Evidence_from_Perp/review]] — 개인 사용자 관점에서 AI 에이전트 채택과 사용에 대한 초기 증거를 확장하여 제시한다.
- 🧪 응용 사례: [[papers/033_A_survey_on_large_language_model_based_autonomous_agents/review]] — 자율 에이전트에 대한 포괄적 조사로 업무 자동화 에이전트의 구체적 적용 가능성을 보여준다.
- 🧪 응용 사례: [[papers/102_Architecture_Design_for_Human-Driven_Systems/review]] — 인간 중심 아키텍처 설계 방법론을 AI 에이전트와의 미래 업무 환경 구축에 적용하여 더 효과적인 인간-AI 협업 시스템을 만들 수 있다.
- 🧪 응용 사례: [[papers/865_Vending-Bench_A_Benchmark_for_Long-Term_Coherence_of_Autonom/review]] — AI 에이전트의 업무 자동화 평가에서 유사한 장기 성능 일관성 문제를 다룬다.
