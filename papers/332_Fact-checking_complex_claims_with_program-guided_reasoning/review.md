---
title: "332_Fact-checking_complex_claims_with_program-guided_reasoning"
authors:
  - "Liangming Pan"
  - "Xiaobao Wu"
  - "Xinyuan Lu"
  - "Anh Tuan Luu"
  - "William Yang Wang"
date: "2023"
doi: "arXiv:2305.12744"
arxiv: ""
score: 4.2
essence: "복잡한 주장(claim)의 사실 확인을 위해 대규모 언어 모델(LLM)의 인-컨텍스트 학습(in-context learning) 능력을 활용하여 추론 프로그램(reasoning program)을 생성하고, 이를 특화된 하위 태스크 함수들로 순차적으로 실행하는 프로그램 가이드 팩트 체킹(PROGRAMFC) 프레임워크를 제안한다. 이는 설명 가능성과 데이터 효율성을 동시에 만족하면서 복잡한 다단계 추론이 필요한 주장 검증에서 우수한 성능을 달성한다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Fact_Verification_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Pan et al._2023_Fact-checking complex claims with program-guided reasoning.pdf"
---

# Fact-checking complex claims with program-guided reasoning

> **저자**: Liangming Pan, Xiaobao Wu, Xinyuan Lu, Anh Tuan Luu, William Yang Wang, Min‐Yen Kan, Preslav Nakov | **날짜**: 2023 | **DOI**: [arXiv:2305.12744](https://arxiv.org/abs/2305.12744)

---

## Essence

복잡한 주장(claim)의 사실 확인을 위해 대규모 언어 모델(LLM)의 인-컨텍스트 학습(in-context learning) 능력을 활용하여 추론 프로그램(reasoning program)을 생성하고, 이를 특화된 하위 태스크 함수들로 순차적으로 실행하는 프로그램 가이드 팩트 체킹(PROGRAMFC) 프레임워크를 제안한다. 이는 설명 가능성과 데이터 효율성을 동시에 만족하면서 복잡한 다단계 추론이 필요한 주장 검증에서 우수한 성능을 달성한다.

## Motivation

- **Known**: 기존의 단순 사실 확인(fact-checking) 연구는 단일 문서에서 충분한 정보를 찾을 수 있는 경우가 대부분이었으나, 실제 환경의 주장들은 다중 근거(evidence) 수집과 복잡한 추론을 요구함. 예: "제임스 카메론과 인터스텔라의 감독이 모두 캐나다에서 태어났는가"라는 주장은 감독이 누구인지 파악하고, 각각의 출생지를 확인한 후 논리적 결합이 필요함.

- **Gap**: 기존 그래프 기반 모델(graph-based model)들은 다단계 추론 성능은 우수하나 모델의 추론 과정이 불명확(불설명 가능)하며, 대량의 태스크 특화 학습 데이터를 필요로 함. 따라서 설명 가능성과 데이터 효율성을 동시에 만족하는 방법이 필요함.

- **Why**: 신뢰할 수 있는 팩트 체킹 시스템은 단순히 진위 판정뿐만 아니라 명확한 추론 과정의 설명을 제공하여 사용자의 이해와 신뢰를 얻어야 하며, 인간 주석 작업의 시간·비용·편향을 고려하면 최소한의 학습 데이터로도 작동하는 모델이 필요함.

- **Approach**: LLM의 인-컨텍스트 학습을 활용하여 복잡한 주장을 구조화된 프로그램 형식으로 분해하고, 각 단계를 전문화된 함수(질문 답변, 사실 검증, 논리 추론 등)에 위임하는 방식으로 설명 가능하면서도 데이터 효율적인 팩트 체킹을 구현.

## Achievement

![Figure 1: PROGRAMFC 모델 개요. 프로그램 생성 단계에서 Codex를 이용해 추론 프로그램을 생성하고, 프로그램 실행 단계에서 각 단계를 특화된 함수(QA 모델, Fact Checker, Logical Reasoner)에 위임](figures/fig1.webp)

1. **다중 데이터셋에서 우수한 성능 달성**: HOVER와 FEVEROUS라는 복잡한 주장 검증 데이터셋에서 7개의 파우 샷(few-shot) 기준 모델들을 능가하며, 특히 추론 깊이(reasoning depth)가 증가할수록 프로그램 가이드 추론의 효과가 증가함을 입증.

2. **설명 가능한 추론 과정**: 생성된 프로그램 자체가 명확한 단계별 추론 경로를 제시하므로, 사용자가 모델의 의사결정 과정을 이해하고 디버깅할 수 있음.

3. **유연하고 견고한 아키텍처**: 하위 태스크 함수들을 쉽게 교체 가능하여 금 증거(gold evidence), 오픈북(open-book), 클로즈드북(closed-book) 등 다양한 팩트 체킹 환경에 대응 가능하며, 약한 모델을 하위 솔버로 사용해도 상대적으로 견고한 성능 유지.

4. **근거 검색 향상**: 오픈 도메인 설정에서 추론 프로그램이 관련 근거의 검색 성능(retrieval)을 개선하는 효과를 확인.

## How

![Figure 1: 프로그램 생성-실행 패러다임. S1-S4는 순차적 추론 단계를 나타내며, 각 단계는 특정 함수를 호출하고 결과를 변수에 저장](figures/fig1.webp)

- **프로그램 생성(Program Generation)**: 
  - Codex(또는 GPT-3) 같은 대규모 언어 모델에 인-컨텍스트 학습 프롬프트를 제공
  - 입력 주장을 ACTION[ARGUMENT] 형식의 구조화된 프로그램으로 변환
  - 각 단계 Si = (fi, Ai, Vi)로 구성: fi는 함수 타입, Ai는 인자, Vi는 반환값 저장 변수
  - 소수의 시연(demonstration) 예제만으로 프로그램 생성 가능

- **프로그램 실행(Program Execution)**:
  - 순차적으로 프로그램의 각 단계를 파싱하고 해석
  - 각 단계의 함수 fi를 호출하며, 인자 Ai는 이전 단계의 반환값을 참조 가능
  - 질문 답변(QA), 사실 검증(Fact Verification), 논리 추론(Logical Reasoning) 등 특화된 함수 활용

- **다중 경로 집계(Aggregating Reasoning Paths)**:
  - N개의 다양한 후보 프로그램을 생성하여 모두 실행
  - 다수결 투표(majority voting)로 최종 판정 도출

- **유연한 지식 원천 활용**:
  - 금 증거 설정: 주어진 근거 문서 사용
  - 오픈북: 위키피디아 같은 대규모 코퍼스에서 검색
  - 클로즈드북: 모델의 매개변수에 내재된 지식만 활용

## Originality

- **프로그래밍 패러다임의 창의적 적용**: 사실 확인에 제어된 자연언어(controlled natural language) 프로그램을 도입하여, 단순 자유형식 설명이 아닌 구조화되고 실행 가능한 형태의 추론 과정을 제시.

- **LLM 능력의 효율적 활용**: 대규모 언어 모델을 프로그램 생성만에 활용하고, 각 하위 태스크는 전문화된 함수에 위임함으로써 LLM의 부담을 줄이면서도 유연성 극대화.

- **체인-오브-소트(Chain-of-Thought) 확장**: 기존 CoT와 달리 단일 LLM이 아닌 다중 전문 모듈 조합으로 확장하여, 더 강력하고 신뢰할 수 있는 추론 프레임워크 구축.

- **설명성과 효율성의 동시 달성**: 기존 방식들이 설명성 또는 효율성 중 하나를 희생했으나, PROGRAMFC는 명확한 프로그램 형태의 설명과 동시에 파우 샷 학습으로 최소 데이터 요구를 실현.

## Limitation & Further Study

- **프로그램 생성의 품질 의존성**: 생성된 프로그램의 정확성이 최종 성능에 큰 영향을 미치므로, 불완전하거나 부정확한 프로그램 생성 시 cascade 오류(cascading errors) 발생 가능성. 프로그램 생성 과정의 오류 정정 메커니즘 개발 필요.

- **하위 태스크 함수의 성능 의존성**: 각 하위 태스크 솔버(QA 모델, 사실 검증 모델 등)의 성능이 전체 시스템의 bottleneck이 될 수 있으므로, 더 견고한 하위 함수 개발이 필요.

- **제한된 함수 라이브러리**: 현재는 QA, 사실 검증, 논리 추론 등 기본 함수만 포함되어 있으며, 특정 도메인의 복잡한 추론(수학적 계산, 시간적 추론 등)을 위한 함수 확장이 필요.

- **다국어 및 도메인 이전성(generalizability)**: 영어 중심의 평가이며, 다른 언어나 특정 도메인(의료, 법률 등)으로의 이전 가능성 탐색 필요.

- **후속 연구 방향**: 
  - 자동 프로그램 정정(self-correction) 메커니즘
  - 더 복잡한 논리 연산자(예: OR, NOT의 다양한 조합)를 포함한 함수 라이브러리 확장
  - 프로그램 생성 오류에 대한 강건성 강화
  - 인간-AI 협력 팩트 체킹 시스템으로의 발전

## Evaluation

- **Novelty**: 4.5/5
  - 팩트 체킹 분야에서 프로그래밍 패러다임을 창의적으로 도입하고, 설명성과 효율성을 동시에 추구하는 점에서 혁신적. 다만, 개별 기술(인-컨텍스트 학습, 체인-오브-소트, 도구 활용 LLM)은 기존 방향의 자연스러운 확장이라는 점에서 약간의 감점.

- **Technical Soundness**: 4/5
  - 문제 정의, 프로그램 생성-실행 프레임워크, 다중 경로 집계 등 기술적 접근이 논리적이고 건실함. 다만, 프로그램 생성의 오류 처리나 인자 변수 참조 시의 복잡한 케이스에 대한 상세한 논의가 부족할 수 있음.

- **Significance**: 4.5/5
  - 실제 환경의 복잡한 주장 검증이라는 중요한 문제를 다루고, HOVER와 FEVEROUS에서 입증된 성능 향상과 설명 가능성은 실무적 가치가 높음. 팩트 체킹 분야 뿐만 아니라 다른 NLP 추론 태스크에도 영향력 있을 수 있음.

- **Clarity**: 4/5
  - Figure 1의 예제를 통해 전체 파이프라인이 직관적으로 설명되며, 문제 정의와 방법론이 명확함. 다만, 프로그램 생성 시 사용된 프롬프트의 상세한 디자인 원칙이나 특정 설계 선택에 대한 동기 설명이 더 자세할 수 있음.

- **Overall**: 4.2/5

**총평**: PROGRAMFC는 설명 가능성과 데이터 효율성을 동시에 달성하면서 복잡한 주장의 사실 확인 성능을 현저히 개선하는 혁신적인 프레임워크로, 프로그래밍 패러다임의 창의적 적용과 LLM의 인-컨텍스트 학습 능력을 효과적으로 결합한 점에서 높이 평가된다. 다만, cascade 오류에 대한 강건성 강화와 함수 라이브러리의 확장이 향후 실무 적용의 핵심 과제이다.

## Related Papers

- 🔗 후속 연구: [[papers/441_Investigating_zero-and_few-shot_generalization_in_fact_verif/review]] — 기본적인 팩트 체킹을 복잡한 주장의 프로그램 가이드 추론으로 확장하여 더 정교한 사실 검증 방법을 제시함
- 🔄 다른 접근: [[papers/827_Towards_effective_extraction_and_evaluation_of_factual_claim/review]] — 둘 다 팩트체킹을 다루지만 하나는 프로그램 기반 추론, 다른 하나는 주장 추출에 중점을 둠
- 🏛 기반 연구: [[papers/333_Factkg_Fact_verification_via_reasoning_on_knowledge_graphs/review]] — 지식 그래프를 활용한 팩트체킹의 기초적 접근이 프로그램 가이드 추론 시스템의 이론적 배경을 제공함
- 🔗 후속 연구: [[papers/117_Augmenting_the_veracity_and_explanations_of_complex_fact_che/review]] — 프로그램 안내 추론을 통한 복잡한 주장 사실 검증은 TrendFact의 중국어 사실 검증을 더욱 정교한 추론 방식으로 확장한 방법론입니다
- 🔄 다른 접근: [[papers/500_Llm-based_corroborating_and_refuting_evidence_retrieval_for/review]] — 증거 검색 vs 프로그램 가이드 추론으로 사실 확인의 서로 다른 접근법
- 🧪 응용 사례: [[papers/317_Enhancing_natural_language_inference_performance_with_knowle/review]] — 프로그램 가이드 추론을 통한 복잡한 클레임 팩트체킹이 지식그래프 기반 NLI의 고도화된 응용이다.
- 🔄 다른 접근: [[papers/448_Kgvalidator_A_framework_for_automatic_validation_of_knowledg/review]] — 복잡한 주장에 대한 사실 확인에서 프로그램 가이드 추론이라는 다른 검증 접근법을 제시한다.
- 🔗 후속 연구: [[papers/859_Unsupervised_pretraining_for_fact_verification_by_language_m/review]] — 프로그램 가이드 추론을 통한 복잡한 클레임 검증이 SFAVEL의 기본적인 클레임-근거 정렬 학습을 더 정교한 추론 체계로 발전시킨 연구임
- 🔗 후속 연구: [[papers/832_Towards_llm-based_fact_verification_on_news_claims_with_a_hi/review]] — 프로그램 가이드 추론을 통한 복잡한 클레임 팩트 체킹이 HiSS의 계층적 분해 방법을 더 정교한 논리적 추론 체계로 발전시킨 연구임
- 🔄 다른 접근: [[papers/394_Grounding_fallacies_misrepresenting_scientific_publications/review]] — 둘 다 복잡한 사실 검증을 다루지만 하나는 과학 논문 오용, 다른 하나는 일반적 복잡한 주장에 중점을 둠
- 🏛 기반 연구: [[papers/441_Investigating_zero-and_few-shot_generalization_in_fact_verif/review]] — 팩트 검증 모델의 일반화 능력 분석이 복잡한 주장의 프로그램 가이드 팩트체킹 시스템 개발의 기초를 제공함
- 🔄 다른 접근: [[papers/827_Towards_effective_extraction_and_evaluation_of_factual_claim/review]] — 둘 다 팩트체킹을 다루지만 하나는 주장 추출에, 다른 하나는 프로그램 기반 추론에 중점을 둠
