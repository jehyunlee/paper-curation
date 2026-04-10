---
title: "823_Towards_a_Science_of_Scaling_Agent_Systems"
authors:
  - "Yubin Kim"
  - "Ken Gu"
  - "Chanwoo Park"
  - "Chunjong Park"
  - "Samuel Schmidgall"
date: "2025.12"
doi: "10.48550/arXiv.2512.08296"
arxiv: ""
score: 4.5
essence: "본 논문은 언어 모델 기반 에이전트 시스템의 성능을 결정하는 정량적 확장 원칙(scaling laws)을 최초로 체계적으로 도출한 연구이다. 도구 활용도, 모델 능력, 작업 특성 간의 상호작용을 분석하여 다중 에이전트 시스템(MAS)이 언제 성능을 향상시키고 언제 저하시키는지 정량화하는 예측 프레임워크를 제시한다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/Multi-Agent_Task_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Kim et al._2025_Towards a Science of Scaling Agent Systems.pdf"
---

# Towards a Science of Scaling Agent Systems

> **저자**: Yubin Kim, Ken Gu, Chanwoo Park, Chunjong Park, Samuel Schmidgall, A. Ali Heydari, Yao Yan, Zhihan Zhang, Yuchen Zhuang, Mark Malhotra, Paul Pu Liang, Hae Won Park, Yuzhe Yang, Xuhai Xu, Yilun Du, Shwetak Patel, Tim Althoff, Daniel McDuff, Xin Liu | **날짜**: 2025-12-17 | **DOI**: [10.48550/arXiv.2512.08296](https://doi.org/10.48550/arXiv.2512.08296)

---

## Essence

![Figure 1](figures/fig1.webp)
*Figure 1: 모델 지능(Intelligence Index)과 에이전트 구조에 따른 성능 변화. 세 가지 LLM 계열(OpenAI, Google, Anthropic)에서 다중 에이전트 시스템(MAS) 변형이 단일 에이전트 시스템(SAS) 대비 상이한 확장 특성을 보임.*

본 논문은 언어 모델 기반 에이전트 시스템의 성능을 결정하는 정량적 확장 원칙(scaling laws)을 최초로 체계적으로 도출한 연구이다. 도구 활용도, 모델 능력, 작업 특성 간의 상호작용을 분석하여 다중 에이전트 시스템(MAS)이 언제 성능을 향상시키고 언제 저하시키는지 정량화하는 예측 프레임워크를 제시한다.

## Motivation

- **Known**: 최근 "더 많은 에이전트가 필요하다(More agents is all you need)"는 주장과 MAS가 복잡한 작업에서 SAS를 일관되게 능가한다는 통설이 존재함. 실제로 코드 생성(HumanEval)과 같은 정적 벤치마크에서는 에이전트 수 증가가 선형적 성능 개선을 보임.

- **Gap**: (1) MAS 평가가 서로 다른 프롬프트, 도구, 계산 예산을 사용하여 아키텍처 효과와 구현 선택을 혼동함. (2) 동적 환경과의 상호작용을 필요로 하는 진정한 "에이전틱(agentic)" 작업과 정적 벤치마크 간의 근본적 차이가 간과됨. (3) 좌표화 오버헤드, 오류 전파, 정보 흐름과 같은 프로세스 동역학(process dynamics) 분석 부재.

- **Why**: 실제 배포(금융 거래, 웹 네비게이션, 소프트웨어 엔지니어링)에서는 환경과의 지속적 상호작용이 필수적이며, 이 경우 다중 에이전트 시스템의 가치는 작업 특성과 아키텍처에 따라 크게 달라질 수 있음. 현재 휴리스틱에 의존하는 설계는 비효율적이고 비용이 높음.

- **Approach**: (1) 에이전틱 평가 정의 정형화: 환경과의 다중 스텝 상호작용, 부분 관찰(partial observability) 하에서의 반복적 정보 수집, 환경 피드백 기반 적응적 전략 개선이 필요. (2) 동일한 프롬프트, 도구, 토큰 예산을 유지하면서 5가지 에이전트 아키텍처를 비교. (3) 180개 제어된 구성을 통해 정량적 좌표화 메트릭(효율성, 오버헤드, 오류 증폭, 중복성)을 도출하고 예측 모델 구축.

## Achievement

![Figure 2](figures/fig2.webp)
*Figure 2: 다양한 작업 도메인에서 단일 에이전트 시스템과 다중 에이전트 시스템의 성능 비교. 웹 네비게이션과 금융 추론에서 상이한 아키텍처 효과가 관찰됨.*

1. **세 가지 지배적 확장 패턴 발견**
   - **도구-좌표화 트레이드오프** (β=-0.267, p<0.001): 도구가 많은 작업(예: 16개 도구 소프트웨어 엔지니어링)에서 MAS는 에이전트당 토큰 예산 감소로 인해 복잡한 도구 조율이 어려워짐.
   - **능력 포화(capability ceiling)** (β=-0.404, p<0.001): 단일 에이전트 기준 성능이 ~45% 초과 시 추가 에이전트는 좌표화 비용이 증분 개선보다 커져 성능 저하.
   - **토폴로지 의존적 오류 증폭**: 독립적 에이전트는 17.2배 오류 증폭, 중앙화된 좌표화는 4.4배로 억제.

2. **작업 조건부 아키텍처 성능**
   - 중앙화 좌표화(Centralized): 병렬화 가능한 금융 추론에서 +80.8% 성능 향상
   - 분산 좌표화(Decentralized): 동적 웹 네비게이션에서 +9.2% 개선 (+0.2% vs SAS)
   - 모든 MAS 변형: 순차 추론 작업에서 -39% ~ -70% 성능 저하

3. **예측 프레임워크 수립**
   - 교차 검증 R²=0.524: 데이터셋 특화 파라미터 없이 보유한(held-out) 작업 도메인에 대한 성능 예측 가능
   - 최적 아키텍처 예측 정확도 87%
   - GPT-5.2 비표본 검증(out-of-sample validation): MAE=0.071, 5가지 확장 원칙 중 4가지가 미공개 최신 모델로 일반화됨 확인

## How

![Figure 3](figures/fig3.webp)
*Figure 3: 모델 계열과 아키텍처 간의 비용-성능 트레이드오프. 좌표화 오버헤드의 상대적 중요성이 모델 능력과 작업 유형에 따라 변함.*

- **제어된 실험 설계**
  - 5개 정준 아키텍처: SAS, Independent MAS, Centralized MAS, Decentralized MAS, Hybrid MAS
  - 3개 LLM 계열 (OpenAI GPT, Google Gemini, Anthropic Claude)
  - 4개 대표적 에이전틱 벤치마크: BrowseComp-Plus (웹), Finance-Agent (금융), PlanCraft (게임), Workbench (실무)
  - 모든 구성에서 동일한 프롬프트, 도구 세트, 토큰 예산 적용

- **좌표화 메트릭 정량화**
  - **효율성(Efficiency)**: 성공/오버헤드 비율
  - **오류 증폭계수(Error Amplification Factor)**: 아키텍처별 오류 전파 정도
  - **메시지 밀도(Message Density)**: 에이전트 간 통신 부하
  - **중복성(Redundancy)**: 에이전트 간 중복된 계산

- **예측 모델 구축**
  - 선형 회귀: 좌표화 메트릭을 독립변수, 성능을 종속변수로 활용
  - 작업 속성(task properties) 기반 모델링으로 데이터셋 오버피팅 방지
  - 87% 정확도의 아키텍처 선택 규칙 도출 (Section 4.3)

## Originality

- **첫 대규모 제어 비교 연구**: 기존 MAS 평가는 서로 다른 설정을 사용했으나, 본 연구는 프롬프트/도구/예산을 통제하여 순수 아키텍처 효과만 분리
- **에이전틱 vs 비에이전틱 작업 구분 정형화**: Agentic Benchmark Checklist(ABC) 확장으로 진정한 상호작용 작업의 특성 명시
- **프로세스 동역학 분석**: 최종 정확도만이 아니라 좌표화 오버헤드, 오류 전파, 정보 흐름 같은 메커니즘 분석
- **일반화 가능한 예측 프레임워크**: R²=0.524 달성 후 미공개 모델(GPT-5.2)에서 검증되어 확장성 증명
- **이론-실무 연결**: 인간 팀 성과 연구(composition, coordination, differentiation)의 아이디어를 인공 에이전트에 체계화

## Limitation & Further Study

- **모델 다양성 제한**: 세 가지 LLM 계열만 평가. 오픈소스 모델(LLaMA, Qwen) 및 멀티모달 모델 포함 시 결과 일반성 검증 필요
- **벤치마크 범위**: 4개 벤치마크가 주요 도메인을 대표하나, 과학 발견, 의료 의사결정 같은 고위험 도메인에서 검증 부족
- **R²=0.524의 설명력**: 절반가량의 분산만 설명. 작업 복잡도, 에이전트 이질성(heterogeneity), 프롬프트 민감도 같은 추가 요인 고려 필요
- **동적 환경 모델링 부족**: 본 연구는 고정된 환경 분석. 적대적(adversarial) 또는 비정상(non-stationary) 환경에서의 MAS 동작 미평가
- **좌표화 메커니즘 상세 분석 부족**: 에이전트 간 메시지 내용, 의사결정 순서, 실시간 오류 감지 메커니즘의 역할 심화 필요
- **비용-편익 분석 불완전**: 계산 효율성(FLOPs, 레이턴시)과 성능의 파레토 경계(Pareto frontier) 분석 필요
- **후속 연구 방향**:
  1. 에이전트 역할 특화 효과 체계적 탐색 (일반가(generalist) vs 전문가(specialist))
  2. 적응적 아키텍처 전환: 작업 진행 중 동적으로 구조 변경
  3. 인간-에이전트 협력 시나리오: MAS 원칙이 인간 팀 개입 시 어떻게 변하는지
  4. 오류 복구 메커니즘 설계: 중앙화된 검증 병목(validation bottleneck)의 최적 구성

## Evaluation

- **Novelty**: 4.5/5 — 에이전틱 작업의 명확한 정의, 제어된 대규모 비교, 일반화 가능한 예측 프레임워크는 기존 문헌의 주요 격차를 메움. 다만 좌표화 메커니즘의 깊이 있는 분석은 제한적.

- **Technical Soundness**: 4/5 — 실험 설계가 체계적이고 통계적 검증(p-값, 교차 검증)이 명확함. 단, R²=0.524는 약간 낮은 수준이며, 특히 동적 환경에서의 일반성 검증 필요.

- **Significance**: 5/5 — 에이전트 시스템의 디자인에 대한 실용적 지침을 최초로 제공. 금융, 웹 네비게이션, 소프트웨어 엔지니어링 같은 고가치 응용에 직접 영향. 학계 및 산업 양쪽에서 중요한 기여.

- **Clarity**: 4/5 — 주요 발견과 프레임워크는 명확히 서술됨. 다만 좌표화 메트릭(efficiency, overhead, error amplification) 정의가 본문 15000자 이내에서는 완전히 전개되지 않음. Figure 2-5의 설명이 보완되면 더 명확해질 것.

- **Overall**: 4.5/5

**총평**: 본 논문은 에이전트 시스템의 확장 원칙을 정량화하는 첫 대규모 제어 실험으로서, "다중 에이전트 = 항상 이득"이라는 통설을 정교하게 반박하고 작업-아키텍처 정렬이 성공의 핵심임을 증명했다. 특히 도구-좌표화 트레이드오프, 능력 포화, 토

## Related Papers

- 🏛 기반 연구: [[papers/464_Large_Language_Model_based_Multi-Agents_A_Survey_of_Progress/review]] — 다중 에이전트 시스템 확장의 이론적 원칙을 머신러닝 하이퍼파라미터 최적화 등 구체적 응용에 적용할 수 있는 기반을 제공한다.
- 🔗 후속 연구: [[papers/120_AutoGen_Enabling_Next-Gen_LLM_Applications_via_Multi-Agent_C/review]] — AutoGen의 다중 에이전트 프레임워크에 정량적 확장 법칙을 적용하여 성능 예측 가능성을 높인다.
- 🧪 응용 사례: [[papers/828_Towards_end-to-end_automation_of_AI_research/review]] — 에이전트 확장 원칙을 과학 연구 자동화라는 복잡한 실제 문제에 적용한 구체적 사례를 제공한다.
- 🏛 기반 연구: [[papers/052_Advances_and_challenges_in_foundation_agents_From_brain-insp/review]] — 대규모 언어모델 기반 에이전트의 종합적 검토가 에이전트 시스템 확장에 대한 과학적 연구의 중요한 이론적 토대를 제공한다
- 🏛 기반 연구: [[papers/033_A_survey_on_large_language_model_based_autonomous_agents/review]] — 에이전트 시스템 확장의 과학적 기반을 제공한다.
- 🏛 기반 연구: [[papers/792_Text2world_Benchmarking_large_language_models_for_symbolic_w/review]] — 에이전트 시스템의 확장 법칙 연구에 필요한 기본적인 세계 모델링 능력 평가 기준을 제공한다.
- 🏛 기반 연구: [[papers/596_OWL_Optimized_Workforce_Learning_for_General_Multi-Agent_Ass/review]] — 에이전트 시스템 확장의 과학이 OWL의 일반화된 다중 에이전트 지원 시스템 설계의 이론적 기반과 확장성 원리를 제공한다.
- 🏛 기반 연구: [[papers/760_Small_Language_Models_are_the_Future_of_Agentic_AI/review]] — 에이전트 시스템 확장의 과학은 소규모 언어모델이 에이전트 AI에서 어떻게 효과적으로 확장될 수 있는지에 대한 이론적 기반을 제공한다.
