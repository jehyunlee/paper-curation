---
title: "828_Towards_end-to-end_automation_of_AI_research"
authors:
  - "Chris Lu"
  - "Cong Lu"
  - "Robert Tjarko Lange"
  - "Yutaro Yamada"
  - "Shengran Hu"
date: "2026.03"
doi: "10.1038/s41586-026-10265-5"
arxiv: ""
score: 4.5
essence: "본 논문은 **The AI Scientist** 시스템을 제시하며, 이는 아이디어 창출부터 동료 검토까지 과학 연구의 전체 수명주기를 자동화하는 최초의 엔드-투-엔드 파이프라인이다. 이 시스템이 생성한 논문이 상위권 머신러닝 컨퍼런스 워크숍의 동료 검토 과정을 통과했으며, 이는 AI의 과학 기여 역량이 상당히 성숙했음을 입증한다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/Multi-Agent_Task_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Lu et al._2026_Towards end-to-end automation of AI research.pdf"
---

# Towards end-to-end automation of AI research

> **저자**: Chris Lu, Cong Lu, Robert Tjarko Lange, Yutaro Yamada, Shengran Hu, Jakob Foerster, David Ha, Jeff Clune | **날짜**: 2026-03 | **DOI**: [10.1038/s41586-026-10265-5](https://doi.org/10.1038/s41586-026-10265-5)

---

## Essence

![Figure 1](figures/fig1.webp)
*Figure 1: The AI Scientist의 워크플로우. 자동화된 아이디어 생성, 트리 기반 실험, 원고 작성 및 리뷰의 서로 다른 단계들로 구성되며, 기초 모델의 개선에 따라 논문 품질이 지속적으로 향상된다.*

본 논문은 **The AI Scientist** 시스템을 제시하며, 이는 아이디어 창출부터 동료 검토까지 과학 연구의 전체 수명주기를 자동화하는 최초의 엔드-투-엔드 파이프라인이다. 이 시스템이 생성한 논문이 상위권 머신러닝 컨퍼런스 워크숍의 동료 검토 과정을 통과했으며, 이는 AI의 과학 기여 역량이 상당히 성숙했음을 입증한다.

## Motivation

- **Known**: AI는 오래전부터 과학 발견을 돕는 데 사용되었으나, LLM 등장 이전에는 화학 구조 발견, 단백질 구조 예측 등 특정 분야의 좁은 작업들에만 적용되었음. 최근 기초 모델(Foundation Models)의 발전으로 가설 생성, 문헌 검토, 코딩 등 더 다양한 연구 활동 자동화가 가능해짐.

- **Gap**: 개별 구성 요소의 자동화 진전에도 불구하고, 개념화에서 출판까지 전체 연구 생명주기를 자율적으로 탐색하는 통합 시스템은 아직 달성되지 못함.

- **Why**: 과학 연구 자동화의 완전한 구현은 과학적 발견을 대폭 가속화할 수 있으며, AI 역량의 범위를 보여주는 중요한 지표가 될 수 있음.

- **Approach**: 기초 모델을 활용한 복합 에이전트 시스템을 구축하여, 아이디어 생성→실험 계획 및 실행→결과 분석→논문 작성→동료 검토의 전체 프로세스를 자동화. 추가로 AI 기반 검토자(Automated Reviewer)를 개발하여 생성된 논문의 품질을 자동으로 평가.

## Achievement

![Figure 1b-c](figures/fig1.webp)
*Figure 1b-c: (b) 시간에 따른 모델 개선에 따라 AI Scientist 논문의 품질이 지속적으로 상향하며, (c) 자동화된 검토자의 성능이 인간 검토자와 동등한 수준임을 보여주는 균형정확도(Balanced Accuracy) 비교.*

1. **엔드-투-엔드 자동화 달성**: The AI Scientist는 아이디어 생성, 문헌 검색, 실험 계획, 코드 작성 및 실행, 결과 시각화, 논문 작성, 동료 검토까지 모든 단계를 자동으로 수행.

2. **실제 피어 리뷰 통과**: 생성된 3개 논문 중 1개가 ICLR 워크숍의 동료 검토에서 인정받아, 수용 기준을 초과하는 점수 달성 (워크숍 수용률 70%).

3. **자동화된 검토자의 신뢰성**: 개발된 Automated Reviewer는 인간 검토자와 동등한 성능 달성 (균형정확도 약 66-69%, F1 스코어 비교에서 인간 검토자와 통계적 유의차 없음).

4. **확장성과 개선 가능성**: 더 강력한 모델과 더 많은 추론 시간 계산을 사용할수록 논문 품질이 향상되며 (R²=0.517, P<0.00001), 기초 모델의 개선에 따라 지속적 성능 향상이 예상됨.

## How

![Figure 1a](figures/fig1.webp)
*Figure 1a: The AI Scientist의 4가지 주요 단계 - 아이디어 생성, 실험 수행, 논문 작성, AI 검토.*

**단계 1: 아이디어 생성 (Ideation)**
- LLM이 사용자 지정 머신러닝 서브필드 내에서 고수준의 연구 방향과 가설을 반복적으로 생성
- 각 아이디어에 대해 제목, 추론 근거, 제안된 실험 계획 작성
- Semantic Scholar API와 웹 접근 도구를 활용하여 기존 문헌과 중복되는 아이디어 자동 필터링

**단계 2: 실험 수행 (Experimentation)**
- 템플릿 기반(Template-based): 사전 제공된 코드 템플릿을 기반으로 선형 순서로 실험 실행
- 템플릿 자유형(Template-free): 초기 코드를 자체 생성하고 트리 서치를 활용한 최적화 수행
  - 예비 조사 → 하이퍼파라미터 튜닝 → 연구 실행 → 절제 연구(Ablation Studies)의 4단계 구조
  - 각 단계에서 최고 성능 체크포인트가 다음 단계의 초기값으로 사용
- 실험 결과를 실험 일지 형식으로 기록

**단계 3: 논문 작성 (Write-up)**
- 빈 LaTeX 컨퍼런스 템플릿에 섹션별로 내용 작성
- Semantic Scholar API를 통해 관련 문헌 검색 (20라운드 반복)
- 각 인용에 대한 텍스트 정당화 생성

**단계 4: 자동 검토 (AI Review)**
- NeurIPS 컨퍼런스 가이드라인 기반의 5개 검토 앙상블
- 각 검토는 수치 점수(건전성, 표현력, 기여도, 전체 품질, 신뢰도), 강점/약점 목록, 수락/거부 결정 포함
- 메타 리뷰 단계에서 에어리어 체어 역할 수행

## Originality

- **첫 완전 자동화 시스템**: 개념화부터 출판까지의 전체 과학 연구 생명주기를 자동화하는 통합 시스템은 이전에 달성된 적 없음.

- **자동화된 과학 평가자 개발**: 인간 검토자와 동등 수준의 성능을 갖춘 Automated Reviewer 개발로, 대규모 AI 생성 논문의 자동 품질 평가 가능.

- **이중 모드 실험 설계**: 템플릿 기반과 템플릿 자유형의 두 가지 접근법으로 기초 연구와 개방형 탐색 모두를 지원.

- **현실적 피어 리뷰 검증**: 실제 학술 컨퍼런스 워크숍에 논문을 제출하는 "AI 과학자 튜링 테스트"를 통해 이상화된 평가가 아닌 현실 검증 수행.

- **계산-성능 관계 분석**: 추론 시간 계산량과 논문 품질 간의 명확한 상관관계 제시 (R²=0.517).

## Limitation & Further Study

- **제한된 평가 범위**: 머신러닝 분야의 컴퓨터 기반 실험에만 초점을 맞췄으며, 실험실 과학이나 다른 분야로의 확장 가능성은 미검증.

- **데이터 오염 우려**: 학습 데이터 전에 속한 2017-2024년 논문에 대한 Automated Reviewer의 정확도(69%)가 학습 후 데이터(2025년, 66%)보다 높아 잠재적 데이터 오염 가능성 존재.

- **과학 문헌에 대한 노이즈 증가**: AI 생성 논문의 대량화로 인한 피어 리뷰 시스템 과부하 및 과학 문헌의 품질 저하 위험.

- **투명성 및 윤리 문제**: 생성된 논문의 출처 명확성, 저자 책임 정의, 학술 출판 시스템과의 통합 방안 등이 미해결.

- **후속 연구 방향**:
  - 실험실 기반 과학(계산 화학, 생물학 등)로의 확장
  - 더 나은 아이디어 필터링 메커니즘 개발
  - 학술 출판 커뮤니티와의 협력으로 responsible AI 개발 추진
  - 오픈소스 과학(open science) 원칙 준수


## Evaluation

- Novelty: 5/5
- Technical Soundness: 4.5/5
- Significance: 5/5
- Clarity: 4/5
- Overall: 4.5/5

**총평**: 본 논문은 과학 연구의 완전한 자동화라는 오랫동안의 AI 연구 목표를 처음으로 실현하고, 실제 학술 평가 시스템을 통해 검증함으로써 높은 임팩트를 입증했다. 자동화된 검토자의 인간 수준 성능 달성도 주목할 만하다. 다만 평가 대상이 머신러닝 분야의 컴퓨터 기반 실험으로 제한되었으며, 과학 문헌에 미칠 잠재적 부작용(노이즈, 피어 리뷰 시스템 과부하)에 대한 대비책 부재는 한계점이다. 기초 모델의 지속적 개선에 따른 시스템의 향상 가능성은 매우 높다.

## Related Papers

- 🔄 다른 접근: [[papers/086_AI-Researcher_Autonomous_Scientific_Innovation/review]] — 완전 자동화된 과학 연구와 자율적 과학 혁신이라는 유사하지만 서로 다른 접근법으로 AI 과학자 구현을 시도한다.
- 🏛 기반 연구: [[papers/795_The_AI_Scientist_Towards_Fully_Automated_Open-Ended_Scientif/review]] — AI 과학자의 초기 개념과 구현을 완전한 엔드투엔드 시스템으로 발전시킨 진화 과정을 보여준다.
- 🔗 후속 연구: [[papers/718_Scientific_discovery_in_the_age_of_artificial_intelligence/review]] — AI 시대 과학 발견의 이론적 가능성을 실제 작동하는 자동화 시스템으로 구현하여 실증적 증거를 제공한다.
- 🔗 후속 연구: [[papers/321_Evaluating_Sakanas_AI_Scientist_Bold_Claims_Mixed_Results_an/review]] — AI 연구의 종단간 자동화에서 Sakana AI Scientist 평가로의 확장
- 🔗 후속 연구: [[papers/476_Large_language_models_orchestrating_structured_reasoning_ach/review]] — 데이터 과학 경쟁에서 검증된 자율 학습 능력을 과학 연구 전체 과정으로 확장하여 완전 자동화를 달성한다.
- 🧪 응용 사례: [[papers/513_M2F_Automated_Formalization_of_Mathematical_Literature_at_Sc/review]] — 수학 형식화 자동화가 과학 연구 전체 자동화의 핵심 구성요소로 작용할 수 있음을 입증한다.
- 🔄 다른 접근: [[papers/764_Sparks_Multi-Agent_Artificial_Intelligence_Model_Discovers_P/review]] — 단백질 과학 특화 발견과 일반적 과학 연구 자동화라는 서로 다른 범위의 자동화된 발견 접근법을 제시한다.
- 🧪 응용 사례: [[papers/823_Towards_a_Science_of_Scaling_Agent_Systems/review]] — 에이전트 확장 원칙을 과학 연구 자동화라는 복잡한 실제 문제에 적용한 구체적 사례를 제공한다.
- 🧪 응용 사례: [[papers/123_Automated_Hypothesis_Validation_with_Agentic_Sequential_Fals/review]] — 자동화된 가설 검증이 완전한 과학 연구 자동화의 핵심 구성요소로 작용함을 보여준다.
- ⚖️ 반론/비판: [[papers/716_ScienceAgentBench_Toward_Rigorous_Assessment_of_Language_Age/review]] — 완전 자동화 주장에 대해 개별 과학적 작업 단위에서의 체계적 평가가 우선되어야 함을 강조한다.
- 🧪 응용 사례: [[papers/147_Aviary_training_language_agents_on_challenging_scientific_ta/review]] — 과학적 작업에서 훈련된 언어 에이전트가 완전 자동화된 과학 연구의 핵심 구성요소로 활용될 수 있음을 보여준다.
- 🏛 기반 연구: [[papers/285_Dolphin_Closed-loop_open-ended_auto-research_through_thinkin/review]] — AI 연구의 end-to-end 자동화 연구는 DOLPHIN의 아이디어-실험-피드백 순환 구조의 이론적 토대를 제공한다.
- 🔗 후속 연구: [[papers/436_InternAgent_When_Agent_Becomes_the_Scientist_--_Building_Clo/review]] — AI 연구의 종단간 자동화로 과학 연구 자동화의 범위를 확장한다.
