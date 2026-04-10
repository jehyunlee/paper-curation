---
title: "176_CACTUS_Chemistry_Agent_Connecting_Tool_Usage_to_Science"
authors:
  - "Andrew D. McNaughton"
  - "Gautham Ramalaxmi"
  - "Agustin Kruel"
  - "C. Knutson"
  - "R. Varikoti"
date: "2024"
doi: "10.1021/acsomega.4c08408"
arxiv: ""
score: 4.0
essence: "대규모 언어 모델(LLM)과 화학정보학 도구를 통합한 CACTUS라는 지능형 에이전트를 개발하여, 약물 설계 및 분자 발견 업무에서 기존 LLM의 성능을 대폭 향상시켰다. 오픈소스 LLM 5개 모델의 벤치마킹을 통해 도메인 특화 프롬프트 엔지니어링의 중요성을 입증했다."
tags:
  - "cat/LLM-Based_Scientific_Reasoning"
  - "sub/Large_Language_Model_Agents"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/McNaughton et al._2024_CACTUS Chemistry Agent Connecting Tool Usage to Science.pdf"
---

# CACTUS: Chemistry Agent Connecting Tool Usage to Science

> **저자**: Andrew D. McNaughton, Gautham Ramalaxmi, Agustin Kruel, C. Knutson, R. Varikoti | **날짜**: 2024 | **DOI**: [10.1021/acsomega.4c08408](https://doi.org/10.1021/acsomega.4c08408)

---

## Essence

대규모 언어 모델(LLM)과 화학정보학 도구를 통합한 CACTUS라는 지능형 에이전트를 개발하여, 약물 설계 및 분자 발견 업무에서 기존 LLM의 성능을 대폭 향상시켰다. 오픈소스 LLM 5개 모델의 벤치마킹을 통해 도메인 특화 프롬프트 엔지니어링의 중요성을 입증했다.

## Motivation

- **Known**: 최신 LLM(GPT-4, LLaMA, Gemma 등)들은 다양한 작업에서 우수한 성능을 보이지만, 정적 학습 데이터에만 의존하므로 실시간 데이터나 동적 정보에 접근 불가능하다는 한계가 있다.

- **Gap**: 특히 화학, 생물학, 재료과학과 같은 도메인 특화 분야에서 LLM의 한계가 더욱 두드러진다. 복잡한 화학 데이터와 약물 발견의 동적 특성을 순수 계산 모델만으로는 효과적으로 처리할 수 없다.

- **Why**: 신약 개발, 촉매 설계, 신소재 탐색 등의 과학적 발견을 가속화하려면 LLM의 인지 능력과 화학정보학 전문 도구의 기능을 결합한 지능형 에이전트가 필요하다.

- **Approach**: Tool-Augmented Language Model (TALM) 프레임워크를 기반으로 LangChain을 활용하여 LLM, 프롬프트 엔지니어링, 그리고 RDKit, PubChem, ChEMBL 등의 화학정보학 도구를 통합한 CACTUS 에이전트를 개발했다.

## Achievement

![Figure 1](figures/fig1.webp) *CACTUS 에이전트의 일반적인 워크플로우: 사용자 입력에서 시작하여 Planning-Action-Execution-Observation 단계를 거쳐 적절한 도구를 선택하고 최종 결과를 도출*

1. **성능 향상**: Gemma-7b와 Mistral-7b 모델이 프롬프팅 전략과 관계없이 가장 높은 정확도를 달성하였으며, 기존 LLM 대비 CACTUS가 화학 질문에 대해 현저히 우수한 성능을 시현했다.

2. **도메인 특화 임팩트**: 도메인 특화 프롬프트(domain-specific prompting)와 하드웨어 구성이 모델 성능에 미치는 영향을 체계적으로 분석하여, 프롬프트 엔지니어링의 중요성과 소비자 등급 하드웨어에서 작은 모델 배포의 실행 가능성을 입증했다.

3. **확장 가능한 도구 생태계**: 분자 성질 예측, 유사성 검색, 약물 유사성 평가(drug-likeness assessment) 등 다양한 화학 작업을 지원하는 10개 도구를 통합했다.

## How

![Figure 2, 3](figures/fig2.webp) *Gemma-7b 모델의 다양한 프롬프팅 전략에 대한 성능 비교 및 7B 매개변수 모델들 간의 성능 비교*

- **아키텍처**: LangChain 기반 커스텀 MRKL 에이전트 구현으로 도구(Tools), LLMChain, 에이전트 클래스의 3가지 핵심 컴포넌트 통합

- **ReAct 프레임워크**: 도구 설명(tool descriptions)을 기반으로 사용자 입력에 가장 적합한 도구를 선택하는 제로샷(zero-shot) 에이전트 방식 적용

- **화학정보학 도구 스택**:
  - 분자 기술자(Molecular Weight, LogP, TPSA, QED, SA)
  - 약동학 속성 예측(BOILED-Egg 방법으로 BBB 투과성, GI 흡수)
  - 구조/독성 필터(Lipinski Rule of 5, Brenk filter, PAINS filter)
  - 데이터베이스 인터페이스(PubChem, ChEMBL, ZINC)

- **프롬프트 엔지니어링**: Chain-of-thought 추론 방식으로 화학정보학 질문 답변을 위한 전형적 단계를 명시하여 모델 성능 극대화

- **평가 방법론**: 다양한 오픈소스 LLM(Gemma-7b, Falcon-7b, MPT-7b, Llama2-7b, Mistral-7b)을 대상으로 수천 개의 화학 질문 벤치마크 구성

## Originality

- **통합 시스템**: 화학정보학 전문 도구와 LLM을 체계적으로 통합한 최초의 오픈소스 기반 지능형 에이전트로, ChemCrow와 달리 합성 계획뿐 아니라 약물 설계와 분자 발견 전반을 포괄

- **도메인 특화 벤치마킹**: 5개 서로 다른 오픈소스 LLM의 화학 작업 성능을 체계적으로 비교하여, 도메인 특화 프롬프트의 효과를 정량적으로 입증

- **확장 가능한 프레임워크**: LangChain을 활용한 모듈식 구조로 신규 도구 통합이 용이하며, KNIME이나 Galaxy와 같은 대규모 도구 기반 플랫폼과의 자연어 인터페이스 구축 가능성 제시

- **소규모 모델 적용성**: 소비자 등급 하드웨어에서 7B 매개변수 모델의 실행 가능성을 입증함으로써 접근성 향상

## Limitation & Further Study

- **입력 형식 제한**: 현재 SMILES 문자열만 입력으로 받으나, 향후 화합물명, 분자식, InChI 키, CAS 번호, ChEMBL ID, ZINC ID 등 다양한 형식 지원 예정

- **추론 정확성 미흡**: 기존 LLM 문제인 "hallucination"(환각 현상)이 완전히 해결되지 않아, 화학 질문에 대해 통계적 관계 학습 오류가 여전히 나타날 가능성 존재

- **자동화 실험 플랫폼 미통합**: 논문에서 자동화 실험 플랫폼과의 통합 가능성을 제시했으나, 실제 구현 및 실시간 데이터 기반 의사결정에 대한 구체적 검증 부족

- **인간-기계 협업 프레임워크**: 사람이 개입하는 루프(human-in-the-loop) 시나리오에서의 효과성과 의사결정 프로토콜에 대한 더 심화된 연구 필요

- **도구 신뢰성 검증**: 통합된 도구들의 화학적 정확성 및 최신성에 대한 독립적 검증 프로세스 강화 필요


## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: CACTUS는 LLM과 화학정보학 도구의 통합을 통해 약물 설계 및 분자 발견 분야에서 의미 있는 진전을 이루었으며, 오픈소스 기반 접근성과 확장 가능한 아키텍처로 실제 과학 연구에 즉시 적용 가능한 가치를 제공하나, 입력 형식 제한과 추론 정확성 문제에 대한 개선이 필요하다.

## Related Papers

- 🔄 다른 접근: [[papers/131_Automating_exploratory_proteomics_research_via_language_mode/review]] — 화학정보학 vs 단백질체학으로 도메인은 다르지만 유사한 자동화 도구 통합 접근
- 🔄 다른 접근: [[papers/110_AstroAgents_A_Multi-Agent_AI_for_Hypothesis_Generation_from/review]] — 화학정보학 vs 우주생물학으로 도메인은 다르지만 유사한 다중 에이전트 도구 활용
- 🔗 후속 연구: [[papers/210_ChemCrow_Augmenting_large-language_models_with_chemistry_too/review]] — 화학정보학 도구 통합을 화학 증강 대화형 시스템으로 발전시킨 연구
- 🔄 다른 접근: [[papers/213_ChemReasoner_Heuristic_Search_over_a_Large_Language_Models_K/review]] — 화학 도구 연결 vs 휴리스틱 탐색으로 화학 LLM의 서로 다른 접근법
- 🔄 다른 접근: [[papers/110_AstroAgents_A_Multi-Agent_AI_for_Hypothesis_Generation_from/review]] — 우주생물학 vs 화학정보학으로 도메인은 다르지만 유사한 다중 에이전트 도구 활용
- 🔄 다른 접근: [[papers/131_Automating_exploratory_proteomics_research_via_language_mode/review]] — 단백질체학 vs 화학정보학으로 도메인은 다르지만 유사한 자동화 도구 통합 접근
- 🏛 기반 연구: [[papers/211_ChemGymRL_A_Customizable_Interactive_Framework_for_Reinforce/review]] — 화학정보학 도구 통합이 화학 실험 자동화의 소프트웨어 기반
- 🧪 응용 사례: [[papers/242_CRITIC_Large_Language_Models_Can_Self-Correct_with_Tool-Inte/review]] — CRITIC의 도구 기반 자기수정 프레임워크는 CACTUS의 화학 도구 활용에서 실험 결과 검증과 오류 수정에 직접 적용될 수 있다.
- 🧪 응용 사례: [[papers/214_ChemToolAgent_The_Impact_of_Tools_on_Language_Agents_for_Che/review]] — 과학과 도구 사용 연결 화학 에이전트를 화학 문제 해결에 적용
- 🔄 다른 접근: [[papers/837_Training_a_Scientific_Reasoning_Model_for_Chemistry/review]] — 둘 다 화학 도메인에서 AI 에이전트를 다루지만 하나는 추론 모델 훈련에, 다른 하나는 도구 사용 연결에 초점을 맞춘다.
