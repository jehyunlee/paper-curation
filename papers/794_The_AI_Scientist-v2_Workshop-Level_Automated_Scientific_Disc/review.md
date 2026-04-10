---
title: "794_The_AI_Scientist-v2_Workshop-Level_Automated_Scientific_Disc"
authors:
  - "Yutaro Yamada"
  - "Robert Tjarko Lange"
  - "Cong Lu"
  - "Shengran Hu"
  - "Chris Lu"
date: "2025.04"
doi: "N/A"
arxiv: ""
score: 4.0
essence: "AI Scientist-v2는 에이전트 기반 트리 서치(agentic tree search)를 활용하여 가설 수립, 실험 설계·실행, 데이터 분석 및 시각화, 논문 자동 작성까지 완전히 자율적으로 수행하는 과학 발견 시스템으로, 최초로 동료 심사(peer review)를 통과한 AI 생성 학술 논문을 배출했다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/Autonomous_Hypothesis_Discovery"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Yamada et al._2025_The AI Scientist-v2 Workshop-Level Automated Scientific Discovery via Agentic Tree Search.pdf"
---

# The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search

> **저자**: Yutaro Yamada, Robert Tjarko Lange, Cong Lu, Shengran Hu, Chris Lu, Jakob Foerster, Jeff Clune, David Ha | **날짜**: 2025-04-10 | **DOI**: N/A

---

## Essence

AI Scientist-v2는 에이전트 기반 트리 서치(agentic tree search)를 활용하여 가설 수립, 실험 설계·실행, 데이터 분석 및 시각화, 논문 자동 작성까지 완전히 자율적으로 수행하는 과학 발견 시스템으로, 최초로 동료 심사(peer review)를 통과한 AI 생성 학술 논문을 배출했다.

## Motivation

- **Known**: The AI Scientist-v1은 자동화된 과학 발견의 가능성을 입증했으나, 인간이 작성한 코드 템플릿(human-authored code templates)에 의존하고 선형적 실험 프로세스만 지원함
- **Gap**: v1은 새로운 주제별로 수작업 템플릿 제작이 필요하고, 얕은 탐색으로 인해 복잡한 가설의 심도 있는 검증 불가능
- **Why**: 진정한 과학적 자율성을 달성하려면 템플릿 의존도 제거, 다양한 ML 도메인에 일반화 가능해야 하며, 인간 과학자처럼 반복적 가설 정제 필요
- **Approach**: 
  - 템플릿 독립적 일반화된 아이디어 생성 단계 도입
  - 실험 진행 관리자(Experiment Progress Manager)와 트리 서치 기반 탐색 알고리즘 개발
  - Vision-Language Model(VLM) 피드백 루프 통합으로 도형·캡션 반복 개선
  - 병렬 실험 실행 지원

## Achievement

1. **첫 피어 리뷰 통과**: 3개의 완전 자동 생성 논문을 ICLR 2025 워크숍에 투고하여 1편이 평균 점수 6.33(상위 45%)으로 수용 기준 달성 - AI 생성 논문의 역사적 첫 성공
2. **자율성 강화**: 인간 작성 템플릿 제거로 다양한 ML 도메인에 즉시 배포 가능
3. **탐색 깊이 증대**: 트리 서치 기반 실험 관리로 복잡한 가설에 대한 체계적 탐색 가능
4. **품질 향상**: VLM 기반 피드백 루프로 도형, 캡션, 텍스트 해석의 일관성 및 명확성 개선

## How

**아이디어 생성 단계**
- 기존 코드 기반 증분 수정 방식에서 벗어나 추상적 수준의 개방형 사고 도입
- Semantic Scholar 등 문헌 검색 도구 통합으로 제안 개념의 신규성 평가 및 선행 연구 파악

**템플릿 의존도 제거**
- 실험 진행 관리자(Experiment Progress Manager): 실행 가능성 평가→기본 구현→세부 실험 단계로 구조화된 과학적 워크플로우 모방
- 트리 서치 기반 코드 생성: 각 노드가 코드 상태를 표현하고, 평가 점수를 기반으로 반복적 선택·정제하여 최적 코드 체크포인트 탐색

**VLM 피드백 통합**
- 실험 및 리뷰 단계에서 도형·캡션의 내용과 미적 품질 반복 개선
- 시각화 및 텍스트 해석의 일관성 강화

**원고 작성 및 리뷰**
- 단계적 생성(single-pass generation) + 별도 반영 단계(o1 같은 추론 모델 활용)로 기존 점진적 Aider 기반 방식 대체
- 병렬 실험 실행으로 효율성 증대

## Originality

- **트리 서치 적용의 창의성**: AIDE의 트리 서치 아이디어를 과학 발견의 다단계 특성에 맞게 적응시켜 구조화된 탐색 전략 구현
- **VLM 피드백 루프**: 도형과 텍스트 해석의 반복 개선을 위한 VLM 통합은 과학 논문 생성의 품질 향상에 신규 기여
- **템플릿 독립 일반화**: 사전 정의된 기본 코드 없이 순수 LLM 기반 코드 생성으로 범용성 확보
- **문헌 기반 아이디어 검증**: 생성 단계에서 즉시 문헌 검색을 통한 신규성 평가로 더 과학적인 접근

## Limitation & Further Study

**한계**
- 피어 리뷰 통과 논문도 reviewers가 지적한 대로 방법 설명 미흡, 직관적 설명 부족, 도형 캡션 부정확성 등 여전한 품질 문제 존재
- 구성성 정규화(compositional regularization) 기법 선택의 정당화 부족 - AI 시스템이 '왜 이 방법이 작동할 것인가'를 충분히 추론하지 못함
- 데이터셋 중복 우려, 컨퍼런스 수준의 엄격성에는 미흡
- 트리 서치의 계산 오버헤드 및 확장성 한계 미논의
- 윤리 및 AI 안전 문제에 대한 심도 있는 논의 부족

**후속 연구**
- 방법론적 타당성 강화: AI가 선택한 기법의 이론적 근거를 더 엄격히 검증하는 메커니즘
- 장기 탐색 전략: 더 복잡하고 시간이 오래 걸리는 실험 문제로의 확장
- 인간-AI 협력 모델: 완전 자동화가 아닌 인간 과학자와의 상호작용 최적화
- 컨퍼런스 수준 논문 생성으로의 도약을 위한 체계적 개선

## Evaluation

- **Novelty (독창성)**: 4.5/5 - 트리 서치 적용 및 VLM 피드백 루프는 창의적이나, 개별 기술 자체는 기존 방법의 조합
- **Technical Soundness (기술적 타당성)**: 3.5/5 - 시스템 설계는 합리적이나, 피어 리뷰 통과 논문도 방법론적 정당화 및 직관성이 부족함을 보임
- **Significance (중요성)**: 4.5/5 - AI 생성 논문의 첫 피어 리뷰 통과는 획기적 마일스톤이며, 과학 연구의 자동화 가능성을 입증
- **Clarity (명확성)**: 4/5 - 워크플로우 설명은 명확하나, 트리 서치 알고리즘의 상세한 수학적 표현 부족
- **Overall**: 4/5

**총평**: 본 논문은 AI 기반 과학 발견의 실질적 진전을 보여주는 중요한 작업으로, 템플릿 독립성 달성과 피어 리뷰 통과라는 역사적 성과를 기록했으나, 여전히 방법론적 엄격성과 컨퍼런스 수준의 논문 품질 달성까지는 거리가 있으며, AI 안전 및 윤리적 함의에 대한 더 깊은 논의가 필요하다.

## Related Papers

- 🔗 후속 연구: [[papers/285_Dolphin_Closed-loop_open-ended_auto-research_through_thinkin/review]] — AI Scientist-v2는 DOLPHIN의 폐쇄 루프 연구 프레임워크를 에이전트 기반 트리 서치로 발전시켜 동료 심사까지 포함한다.
- 🔄 다른 접근: [[papers/795_The_AI_Scientist_Towards_Fully_Automated_Open-Ended_Scientif/review]] — AI Scientist-v2와 원래 AI Scientist 모두 완전 자동화된 과학 발견을 추구하지만 에이전트 기반 트리 서치 vs 기본적인 자동화 접근을 사용한다.
- ⚖️ 반론/비판: [[papers/628_Position_The_ai_conference_peer_review_crisis_demands_author/review]] — AI 학회 동료 심사 위기에 대한 우려는 AI Scientist-v2가 동료 심사를 통과한 논문을 생성했다는 성과와 상반된 시각을 제시한다.
- 🔗 후속 연구: [[papers/857_Unlocking_the_Potential_of_AI_Researchers_in_Scientific_Disc/review]] — AI Scientist 자동화 시스템이 과학 발견에서 AI 연구자 역할 확대를 구체화한다.
- 🔗 후속 연구: [[papers/086_AI-Researcher_Autonomous_Scientific_Innovation/review]] — 자율적 과학 혁신이 워크샵 수준의 과학 발견으로 확장됩니다.
- 🔗 후속 연구: [[papers/705_SciAgents_Automating_Scientific_Discovery_Through_Bioinspire/review]] — AI 과학자의 워크샵 수준 자동화된 과학적 발견을 생물 영감 재료 분야로 확장 적용한 사례이다.
- 🔗 후속 연구: [[papers/285_Dolphin_Closed-loop_open-ended_auto-research_through_thinkin/review]] — AI Scientist-v2는 DOLPHIN의 폐쇄 루프 연구 프레임워크를 에이전트 기반 트리 서치로 발전시켜 동료 심사까지 포함한다.
- 🔗 후속 연구: [[papers/549_Mlr-copilot_Autonomous_machine_learning_research_based_on_la/review]] — AI Scientist-v2는 MLR-COPILOT의 자동화된 ML 연구를 에이전트 기반 트리 서치와 동료 심사까지 포함한 완전한 과학 발견으로 발전시킨다.
- 🔗 후속 연구: [[papers/578_Novelseek_When_agent_becomes_the_scientistbuilding_closed-lo/review]] — AI Scientist-v2는 InternAgent의 통합 폐루프 다중 에이전트 프레임워크를 에이전트 기반 트리 서치로 발전시켜 동료 심사까지 포함한다.
- 🔗 후속 연구: [[papers/672_ResearchGym_Evaluating_Language_Model_Agents_on_Real-World_A/review]] — AI Scientist의 자동화된 과학 발견을 실제 연구 환경에서 체계적으로 벤치마킹하는 확장 연구
- 🏛 기반 연구: [[papers/548_Mlr-bench_Evaluating_ai_agents_on_open-ended_machine_learnin/review]] — 워크샵 수준의 자동화된 과학 발견 시스템으로서 MLR-Bench가 평가하는 AI 에이전트의 이상적인 목표 모델을 제시한다.
- 🏛 기반 연구: [[papers/630_Predicting_empirical_ai_research_outcomes_with_language_mode/review]] — 자동화된 과학적 발견 시스템에서 연구 아이디어의 사전 평가가 전체 연구 파이프라인의 핵심 구성 요소로 작용한다.
- 🏛 기반 연구: [[papers/868_Virtual_lab_powered_by_AI_scientists_super-charges_biomedica/review]] — 가상 실험실에서의 AI 과학자 협업 사례가 완전 자동화된 과학적 발견 시스템의 실현 가능성을 보여주는 중요한 실증적 기반을 제공한다.
