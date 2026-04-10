---
title: "840_Transforming_Science_with_Large_Language_Models_A_Survey_on"
authors:
  - "Steffen Eger"
  - "Yong Cao"
  - "Jennifer D'Souza"
  - "Andreas Geiger"
  - "Christian Greisinger"
date: "2025.02"
doi: "N/A"
arxiv: ""
score: 4.2
essence: "대규모 다중모드 언어 모델(LLM)의 등장으로 과학 연구가 AI 기반의 기술적 변환의 임계점에 도달했으며, 본 논문은 문헌 검색, 실험 설계, 콘텐츠 생성, 동료 평가에 이르는 전체 연구 생명주기에서 AI의 역할을 체계적으로 검토하는 종합 서베이이다."
tags:
  - "cat/AI-Powered_Scientific_Research_Frameworks"
  - "sub/AI_for_Science_Taxonomy"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Eger et al._2025_Transforming Science with Large Language Models A Survey on AI-assisted Scientific Discovery, Exper.pdf"
---

# Transforming Science with Large Language Models: A Survey on AI-assisted Scientific Discovery, Experimentation, Content Generation, and Evaluation

> **저자**: Steffen Eger, Yong Cao, Jennifer D'Souza, Andreas Geiger, Christian Greisinger, Stephanie Gross, Yufang Hou, Brigitte Krenn, Anne Lauscher, Yizhi Li, Chenghua Lin, Nafise Sadat Moosavi, Wei Zhao, Tristan Miller | **날짜**: 2025-02-07 | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp) 
*Figure 1: AI 보조 과학 연구 워크플로우 및 남은 과제들의 개요. 문헌 검색부터 동료 평가까지 각 단계에서 AI 지원의 현황과 한계를 보여줌.*

대규모 다중모드 언어 모델(LLM)의 등장으로 과학 연구가 AI 기반의 기술적 변환의 임계점에 도달했으며, 본 논문은 문헌 검색, 실험 설계, 콘텐츠 생성, 동료 평가에 이르는 전체 연구 생명주기에서 AI의 역할을 체계적으로 검토하는 종합 서베이이다.

## Motivation

- **Known**: 최근 ChatGPT, Gemini 등 대규모 언어 모델이 다양한 분야에서 널리 활용되고 있으며, 비컴퓨터과학 분야(148,000개 논문 기준)에서도 LLM 인용이 급증하고 있음. 전 세계 연구자들은 향후 2년 내 AI 사용이 과학 실무의 주류가 될 것으로 예상.

- **Gap**: 기존 서베이들은 특정 분야(예: 사회과학, 물리학)나 좁은 범위의 연구 과제만 다루고 있어, 전체 과학 연구 워크플로우를 아우르는 종합적 관점의 자료가 부족.

- **Why**: AI4Science 생태계가 빠르게 발전하면서 전문가와 신입 모두를 위한 구조화된 가이드, 기술·윤리적 고려사항의 통합 검토가 필요.

- **Approach**: 워크플로우 중심의 내러티브 서베이 방법론 채택. 5가지 핵심 과제 (①문헌 검색 및 요약, ②실험 및 아이디어 생성, ③텍스트 콘텐츠 생성, ④다중모드 콘텐츠 생성, ⑤동료 평가)를 데이터셋, 방법론, 평가 전략, 한계, 윤리 문제로 분석.

## Achievement

1. **포괄적 분류 체계**: 과학 연구의 6단계 기본 프로세스(연구 질문 수립 → 문헌 조사 → 가설 수립 → 실험 설계·실행 → 데이터 분석 → 결과 보고)에 맞춘 AI 지원 기능의 체계적 매핑.

2. **성숙도별 현황 분석**: 
   - **성숙 단계**: 문헌 검색(의미론적 검색, 논문 채팅, 그래프 기반 분석) 및 텍스트 생성(제목, 초록, 인용) 기술
   - **초기 단계**: 실험 자동화(실험 계획, 코드 생성, 자동 벤치마킹) - 신뢰성 부족
   - **유망하나 미성숙**: 동료 평가 자동화 - 단독 평가자로는 부적절

3. **통합 윤리 프레임워크**: 환각(hallucination), 편향(bias), 제한된 추론 능력, 환경 비용뿐만 아니라 "가짜 과학", 표절, 연구 무결성 침식 등 광범위한 위험 식별 및 분석.

## How

- **선택 기준**: 도메인 전문가로 구성된 공동 저자 팀이 기술적 깊이, 영향력, 방법론적 대표성을 고려하여 문헌 선정. Seed papers부터 시작해 순방향·역방향 인용 추적 및 보완 검색 수행.

- **내러티브 서베이 방법론**: 체계적 리뷰의 엄격한 포함·배제 기준 대신 개념적 응집성, 방법론적 대표성, 과제 간 비교 가능성을 우선. 이질적이고 빠르게 진화하는 문헌을 합성하는 데 적합.

- **구조화**: 
  - §3.1: 의미론적 검색, 페이퍼 채팅, 그래프 기반 분석, 개인화 요약
  - §3.2: 연구 아이디어 생성, 가설 생성, 자동화 실험, 코드/파이프라인 생성
  - §3.3: 제목, 초록, 장문 텍스트, 인용, 관련 연구, 교정 및 스타일 전이
  - §3.4: 도표 생성·해석, 과학 슬라이드·포스터 생성
  - §3.5: 자동화된 리뷰 및 피드백 생성, 과학적 주장 검증, 메타 리뷰 분석

- **윤리 고려**: 각 과제별 섹션 내에 윤리 문제 통합, §4에서 집중 논의.

## Originality

- **최초 시도**: 과학 연구의 전체 생명주기를 단일 서베이로 아우르는 워크플로우 중심 접근법. 기존 도메인별, 과제별 서베이와 달리 횡단적 관점 제시.

- **포괄성**: 텍스트 생성뿐 아니라 도표, 슬라이드 등 다중모드 콘텐츠, 실험 자동화, 동료 평가 등 과학 활동의 소외된 영역까지 포함.

- **윤리적 초점**: AI 도구의 기술적 성능뿐 아니라 연구 무결성, 저작권, 표절, 환경 영향 등 광범위한 사회적 영향을 구조적으로 다룸.

- **실용적 자원 제공**: GitHub 저장소 운영으로 주기적 업데이트 및 추가 자료 제공, 신입자부터 정책결정자까지 다층 독자를 목표.

## Limitation & Further Study

- **범위의 제약**: 내러티브 방법론 채택으로 철저한 상태 파악(SOTA) 또는 모든 관련 논문의 포함을 보장하지 않음. 빠르게 발전하는 분야의 특성상 발행 시점에 이미 일부 내용이 구식화될 가능성.

- **도메인 편향**: LLM 중심 관점으로 인해 기존 생물정보학 도구(BLAST 등)나 물리 시뮬레이션 소프트웨어 등 전통적 AI/과학 도구와의 연계 부족.

- **평가 메트릭 미성숙**: 특히 실험 자동화와 아이디어 생성 분야에서 신뢰할 만한 벤치마크 및 평가 기준이 부재. 기존 평가는 LLM의 자체 평가(self-evaluation)에 의존하는 경우 다수.

- **후속 연구 방향**:
  - 멀티모드 콘텐츠(도표, 슬라이드) 생성 및 검증 기술의 고도화
  - 과학 특화 LLM의 신뢰성 향상 (hallucination 감소, 도메인 지식 강화)
  - 인간-AI 협력 프레임워크 개발 (효과적 감독과 자동화의 균형)
  - 학제 간 표준화된 평가 데이터셋 구축
  - 가짜 과학 탐지 기술 및 연구 무결성 모니터링 도구 개발

## Evaluation

- **Novelty**: 4.5/5
  - 전체 과학 생명주기를 아우르는 첫 종합 서베이로 높은 가치. 다만 개별 영역(예: 요약, 리뷰)의 기본 개념은 기존 연구에 의존.

- **Technical Soundness**: 4/5
  - 내러티브 방법론 투명성 우수. 그러나 "대표성 있는" 논문 선정 기준이 명시적이지 않아 재현성 제한. 보존적 기준 적용으로 최신 발전 (2024-2025) 일부 누락 가능성.

- **Significance**: 4.5/5
  - 정책입안자, 연구자, AI 개발자 등 다층 이해관계자에게 높은 실용적 가치. 특히 윤리 및 무결성 논의로 AI4Science의 책임 있는 발전에 기여. 다만 구체적 솔루션 제시보다는 현황 진단에 중점.

- **Clarity**: 4/5
  - 명확한 구조(5대 과제 분류, Figure 1의 워크플로우) 및 접근성 높은 기술 설명. 그러나 각 섹션의 상세도 차이 발생 가능성, 초록에서 주요 발견(key findings)이 부각되지 않음.

- **Overall**: 4.2/5
  - **총평**: 이 논문은 급속히 발전하는 AI4Science 분야에 대한 종합적이고 구조화된 첫 번째 가이드로서, 신입 연구자부터 정책결정자까지 폭넓은 대상에게 높은 참고가치를 제공한다. 특히 윤리 및 연구 무결성 논의의 통합은 기술 발전을 넘어선 책임 있는 과학 지원 시스템 구축에 중요한 기초를 마련한다. 다만 내러티브 접근법의 한계로 인한 완전성 부족과 빠르게 변화하는 분야에서의 시간성 격차 극복이 과제이다.

## Related Papers

- 🧪 응용 사례: [[papers/378_Generative_AI_Uses_and_Risks_for_Knowledge_Workers_in_a_Scie/review]] — LLM 기반 과학 연구 변혁의 이론적 전망을 실제 과학 조직의 구체적 적용 사례로 검증합니다.
- 🔄 다른 접근: [[papers/044_Accelerating_Scientific_Research_with_Gemini_Case_Studies_an/review]] — AI를 활용한 과학 연구 가속화라는 동일한 목표를 일반적 서베이와 특정 모델 사례로 상호 보완합니다.
- ⚖️ 반론/비판: [[papers/562_Multi-agent_risks_from_advanced_ai/review]] — AI의 과학 연구 변혁 가능성에 대한 낙관적 전망과 대조적으로 다중 에이전트 시스템의 위험성을 제시합니다.
- 🏛 기반 연구: [[papers/004_A_Comprehensive_Survey_of_Scientific_Large_Language_Models_a/review]] — LLM이 과학을 변화시키는 방식에 대한 조사로 과학 분야 LLM 응용의 이론적 배경을 제공한다.
- 🔄 다른 접근: [[papers/088_AI4Research_A_Survey_of_Artificial_Intelligence_for_Scientif/review]] — 과학 연구에서 대규모 언어모델의 역할을 다른 관점에서 체계화하고 분류한다
- 🏛 기반 연구: [[papers/377_Generative_AI_and_the_Foundation_Model_Era_A_Comprehensive_R/review]] — 과학에서 대규모 언어모델 변환에 대한 조사가 생성형 AI 시대의 이론적 맥락을 제공한다
- 🔄 다른 접근: [[papers/475_Large_language_models_meet_nlp_A_survey/review]] — 과학에서 LLM의 역할을 NLP 응용과 과학 연구 변환이라는 다른 관점에서 조명한다
- ⚖️ 반론/비판: [[papers/890_Your_Brain_on_ChatGPT_Accumulation_of_Cognitive_Debt_when_Us/review]] — AI의 과학 연구 변혁 가능성을 긍정적으로 조망하는 반면, 뇌 수준의 인지적 비용이라는 부정적 측면을 제시합니다.
- 🔄 다른 접근: [[papers/044_Accelerating_Scientific_Research_with_Gemini_Case_Studies_an/review]] — 과학 연구 가속화를 위한 AI 활용이라는 동일한 목표를 다른 AI 모델(Gemini vs 일반 LLM)로 접근합니다.
- 🏛 기반 연구: [[papers/089_Aigs_Generating_science_from_ai-powered_automated_falsificat/review]] — LLM 기반 과학 연구 변혁의 이론적 배경을 제공하여 자동 과학 생성의 맥락을 이해할 수 있습니다.
- 🏛 기반 연구: [[papers/378_Generative_AI_Uses_and_Risks_for_Knowledge_Workers_in_a_Scie/review]] — 과학 연구에서 LLM 활용의 이론적 가능성에 대한 실제 현장 적용 사례와 한계를 제공합니다.
- 🧪 응용 사례: [[papers/486_Lego-prover_Neural_theorem_proving_with_growing_libraries/review]] — LLM의 과학 연구 활용을 수학적 정리 증명이라는 구체적 영역에 적용하는 전문화된 사례입니다.
- ⚖️ 반론/비판: [[papers/562_Multi-agent_risks_from_advanced_ai/review]] — 과학 연구 변혁의 긍정적 전망과 대조적으로 AI 시스템 배포의 잠재적 위험성을 체계적으로 분석합니다.
- 🧪 응용 사례: [[papers/785_T-sciq_Teaching_multimodal_chain-of-thought_reasoning_via_mi/review]] — LLM의 과학 연구 활용을 멀티모달 과학 교육이라는 구체적 응용 분야에 적용하는 실용적 사례입니다.
- 🔗 후속 연구: [[papers/869_Visual_thoughts_A_unified_perspective_of_understanding_multi/review]] — 시각적 사고 메커니즘을 과학 연구의 멀티모달 AI 시스템으로 확장하여 더 효과적인 과학적 추론을 가능하게 합니다.
- 🔗 후속 연구: [[papers/029_A_Survey_of_Scientific_Large_Language_Models_From_Data_Found/review]] — 대규모 언어모델이 과학을 변화시키는 방법에 대한 서베이로 확장한다.
- 🔗 후속 연구: [[papers/1093_The_fifth_era_of_science_Artificial_scientific_intelligence/review]] — 대규모 언어모델이 과학을 변혁시키는 방법을 인공 과학 지능의 관점에서 확장한다.
- 🔗 후속 연구: [[papers/878_What_ChatGPT_and_generative_AI_mean_for_science/review]] — ChatGPT의 과학적 영향을 LLM 전반의 과학 변화로 확장하여 분석한다.
