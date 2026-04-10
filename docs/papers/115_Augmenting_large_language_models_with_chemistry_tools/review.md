---
title: "115_Augmenting_large_language_models_with_chemistry_tools"
authors:
  - "Andres M. Bran"
  - "Sam Cox"
  - "Oliver Schilter"
  - "Carlo Baldassari"
  - "Andrew D. White"
date: "2024.05"
doi: "10.1038/s42256-024-00832-8"
arxiv: ""
score: 4.2
essence: "ChemCrow는 GPT-4에 18개의 화학 전문가 도구를 통합하여 합성 계획, 약물 발견, 재료 설계 등 다양한 화학 작업을 자동으로 수행할 수 있는 LLM 화학 에이전트이다. 이 시스템은 곤충 기피제와 유기촉매 합성을 자율적으로 실행하고 새로운 색소체 발견을 주도하여, 계산 화학과 실험 화학 사이의 격차를 효과적으로 연결한다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/AI_Research_Ideation"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/M. Bran et al._2024_Augmenting large language models with chemistry tools.pdf"
---

# Augmenting large language models with chemistry tools

> **저자**: Andres M. Bran, Sam Cox, Oliver Schilter, Carlo Baldassari, Andrew D. White, Philippe Schwaller | **날짜**: 2024-05-08 | **DOI**: [10.1038/s42256-024-00832-8](https://doi.org/10.1038/s42256-024-00832-8)

---

## Essence

ChemCrow는 GPT-4에 18개의 화학 전문가 도구를 통합하여 합성 계획, 약물 발견, 재료 설계 등 다양한 화학 작업을 자동으로 수행할 수 있는 LLM 화학 에이전트이다. 이 시스템은 곤충 기피제와 유기촉매 합성을 자율적으로 실행하고 새로운 색소체 발견을 주도하여, 계산 화학과 실험 화학 사이의 격차를 효과적으로 연결한다.

## Motivation

- **Known**: LLM(특히 GPT-4, GPT-3.5)은 자연언어 처리 분야에서 우수한 성능을 보이나 기초 수학이나 화학 연산에 취약하다(예: 12,345 × 98,765 계산 불가, IUPAC 명명법을 분자 구조로 변환 불능). 또한 외부 지식 출처에 대한 접근이 제한적이다.

- **Gap**: 화학 분야는 반응 예측, 역합성 계획, 분자 생성 등 다양한 AI 도구들이 존재하지만, 이들이 독립적인 환경(RXN for Chemistry, AIZynthFinder 등)에서 통합되어 실험 화학자들의 접근성이 낮고 도구 간 상호운용성이 부족하다.

- **Why**: 화학의 자동화 수준이 타 분야에 비해 낮은 이유는 높은 실험 의존성, 데이터 부족, 계산 도구의 제한된 적용 범위 때문이다.

- **Approach**: 전문가 설계 화학 도구들을 LLM의 추론 능력과 결합하여 자동화된 화학 에이전트를 구축한다. Thought-Action-Action Input-Observation 반복 루프를 통해 LLM이 작업을 추론하고, 적절한 도구를 선택하며, 결과를 분석하는 방식으로 작동시킨다.

## Achievement

1. **자율적 화학 합성 실행**: ChemCrow는 사용자 입력(예: "곤충 기피제의 합성 계획 및 실행")을 받아 클라우드 연결 로보틱 플랫폼(RoboRXN)에서 자율적으로 DEET(곤충 기피제) 및 3개의 티오우레아 유기촉매(Schreiner's, Ricci's, Takemoto's) 합성을 성공적으로 계획하고 실행했다. 합성 절차 검증 데이터를 반복적으로 쿼리하여 용매량 조정 등 자동 수정을 수행하는 능력도 시연했다.

2. **인간-AI 협력을 통한 신규 색소체 발견**: ChemCrow는 기계학습 모델 학습을 통해 색소체 후보 라이브러리를 스크리닝하고, 목표 흡수 최대 파장(369 nm)을 기준으로 새로운 분자를 제안했으며, 이 분자는 실제 합성되어 약 336 nm의 흡수 최대 파장을 가진 새로운 색소체로 검증되었다.

3. **다양한 화학 작업에서의 평가 우월성**: 14개 사용 사례에서 GPT-4 단독 사용 대비 ChemCrow의 성능이 LLM 기반 평가(EvaluatorGPT)와 전문가 인간 평가 모두에서 우수함을 입증했다.

## How

![Figure 1](figures/fig1.webp)
*Fig. 1 | 개요 및 도구 집합. (a) 작업 해결 과정의 개요 및 DEET 합성 예시, (b) 구현된 18개의 화학 도구 (반응, 분자, 안전, 검색, 표준 도구)*

- **도구 통합**: 18개의 전문가 설계 도구 구현
  - 반응 도구: 역합성(Retrosynthesis), 절차 예측(Procedure prediction), 반응 예측(Reaction prediction)
  - 분자 도구: 이름-SMILES 변환, 유사성 검색, 분자 수정(Modify molecule)
  - 안전 도구: 폭발물 검사(Explosive check), 안전 평가(Safety assessment)
  - 검색 도구: Google 검색, 문헌 검색(Literature search), 특허 검사(Patent check)
  - 표준 도구: 웹 검색, 코드 해석기(Code interpreter), 인간 전문가 상담

- **ReAct 프레임워크 적용**: 체인-오브-소트(Chain-of-thought) 추론과 도구 사용을 결합
  1. Thought: 현재 작업 상태 추론 및 계획
  2. Action: 사용할 도구 선택
  3. Action Input: 도구 입력값 제공
  4. Observation: 도구 결과 분석 후 다음 단계 결정
  - 반복 루프: 최종 답변에 도달할 때까지 반복

- **합성 절차 자동 적응**: RoboRXN 플랫폼 검증 데이터 쿼리를 통해 불유효한 합성 절차(예: "용매 부족")를 자동으로 수정하여 인간 개입 제거

- **평가 방법론**: 
  - LLM 기반 평가: EvaluatorGPT를 교사 역할로 설정하여 작업 해결 여부 및 추론 과정 정확성 평가
  - 전문가 인간 평가: 화학자 협력을 통한 검증

## Originality

- **새로운 통합 아키텍처**: 화학 분야에서 처음으로 다양한 전문가 도구들을 단일 LLM 에이전트에 체계적으로 통합하여 자동화된 추론 엔진을 구현했다.

- **자율적 실행 능력 확장**: 단순 계획을 넘어 클라우드 연결 로보틱 시스템과의 직접 연동을 통해 실제 화학 실험 자동화를 최초로 시연했다.

- **적응형 절차 수정**: 합성 검증 피드백을 반복적으로 받아 절차를 자동 조정하는 능력은 기존 자동화 도구에서 부재한 새로운 기능이다.

- **포괄적 평가 프레임워크**: 화학 관련 LLM 작업을 위한 표준화된 평가 방법론 개발(LLM 기반 + 전문가 평가 조합)

## Limitation & Further Study

- **도구 품질 의존성**: 합성 계획 능력은 기반 합성 엔진의 개선에 크게 의존하며, 현재 도구 집합이 완전하지 않다. 저자들은 새로운 도구 추가로 쉽게 확장 가능하도록 설계했음을 언급했다.

- **평가 방법론의 한계**: 화학 분야의 표준화된 벤치마크 부족으로 인해 평가 신뢰성이 제한적이며, LLM 기반 평가와 전문가 평가 간 불일치 가능성이 존재한다.

- **확장성 및 일반화**: 주로 GPT-4 기반 실험이므로 다른 LLM 모델에서의 성능 검증이 필요하다. 또한 도구의 확장성과 새로운 화학 도메인으로의 적용 가능성에 대한 체계적 분석이 부족하다.

- **후속 연구**: 
  - 더 강력한 합성 예측 엔진 개발
  - 실시간 피드백을 활용한 학습 능력 강화
  - 다양한 LLM 모델과의 비교 평가
  - 화학 벤치마크 표준화 추진
  - 산업 규모 실험실 시스템과의 통합

## Evaluation

- **Novelty**: 4.5/5  
  화학 분야에서 LLM을 도구와 통합하는 아이디어는 참신하고, 자율적 합성 실행은 새로운 시도이나, ReAct 프레임워크 자체는 기존 방법론의 화학 적용이다.

- **Technical Soundness**: 4/5  
  18개 도구의 통합, 자동 절차 수정, 인간-AI 협력 시연 등 기술적 구현이 견고하나, 평가 방법론(특히 LLM 기반 평가)의 객관성에 대한 우려가 있다.

- **Significance**: 4.5/5  
  화학 분야의 자동화와 접근성 향상에 상당한 기여를 하며, 전문가와 비전문가 모두에게 가치 있으나, 현재는 주로 이미 알려진 분자의 합성에 국한되어 있다.

- **Clarity**: 4/5  
  논문 구조가 명확하고 사례 설명이 구체적이나, 도구 세부 사항과 평가 결과가 부록으로 제한되어 본문에서의 이해도를 다소 제약한다.

- **Overall**: 4.2/5

**총평**: ChemCrow는 LLM을 화학 도구와 체계적으로 통합하여 자율적 합성 실행과 신약 발견을 실현한 획기적인 작업으로, 화학 자동화 분야에 명확한 진전을 보여준다. 다만 평가 방법론의 표준화와 다양한 화학 도메인으로의 확장성 검증이 향후 과제이다.

## Related Papers

- 🏛 기반 연구: [[papers/557_MOOSE-Chem_Large_Language_Models_for_Rediscovering_Unseen_Ch/review]] — LLM에 화학 도구를 통합하는 방법론이 미발견 화학 가설 재발견의 기반을 제공한다
- 🔄 다른 접근: [[papers/638_ProtAgents_protein_discovery_via_large_language_model_multi-/review]] — 화학 vs 단백질 분야에서 LLM 기반 전문 도구 통합의 다른 적용을 비교할 수 있다
- 🔄 다른 접근: [[papers/210_ChemCrow_Augmenting_large-language_models_with_chemistry_too/review]] — 화학 분야에서 LLM 도구 증강의 다른 접근법과 구현 방식을 비교할 수 있다
- 🔗 후속 연구: [[papers/292_Drugpilot_Llm-based_parameterized_reasoning_agent_for_drug_d/review]] — 화학 도구 통합 방법론을 신약 개발의 전체 파이프라인으로 확장한 연구다
- 🏛 기반 연구: [[papers/210_ChemCrow_Augmenting_large-language_models_with_chemistry_too/review]] — LLM에 화학 도구 통합의 기본 연구가 ChemCrow의 직접적 기반
- 🔄 다른 접근: [[papers/209_ChemAgent_Self-updating_Library_in_Large_Language_Models_Imp/review]] — LLM의 화학 능력 향상을 위한 서로 다른 접근법을 제시합니다.
- 🔗 후속 연구: [[papers/557_MOOSE-Chem_Large_Language_Models_for_Rediscovering_Unseen_Ch/review]] — LLM에 화학 도구를 통합한 방법론을 미발견 화학 가설 재발견에 확장 적용할 수 있다
- 🏛 기반 연구: [[papers/638_ProtAgents_protein_discovery_via_large_language_model_multi-/review]] — LLM에 전문 도구를 통합하는 방법론이 단백질 설계 다중 에이전트 시스템의 기반을 제공한다
- 🏛 기반 연구: [[papers/292_Drugpilot_Llm-based_parameterized_reasoning_agent_for_drug_d/review]] — LLM에 전문 도구를 통합하는 방법론이 매개변수화된 추론 에이전트의 기반을 제공한다
- 🔗 후속 연구: [[papers/480_Large-Language-Model-Based_AI_Agent_for_Organic_Semiconducto/review]] — LLM과 머신러닝 알고리즘 결합을 화학 도구 통합에서 반도체 소자 개발로 확장한 연구다
- 🏛 기반 연구: [[papers/214_ChemToolAgent_The_Impact_of_Tools_on_Language_Agents_for_Che/review]] — 화학 도구로 LLM 확장하기가 화학 문제 해결 도구의 기반 제공
- 🏛 기반 연구: [[papers/554_Modular_large_language_model_agents_for_multi-task_computati/review]] — 화학 도구로 증강된 대규모 언어 모델이 PharmAgents의 신약 개발 전 과정 자동화를 위한 핵심적인 기술적 토대를 제공한다.
- 🏛 기반 연구: [[papers/239_CRISPR-GPT_for_agentic_automation_of_gene-editing_experiment/review]] — 화학 도구로 강화된 LLM 연구는 CRISPR-GPT가 유전체 공학 도메인 지식을 통합하는 방법론적 기반을 제공한다.
- 🔗 후속 연구: [[papers/837_Training_a_Scientific_Reasoning_Model_for_Chemistry/review]] — 대규모 언어 모델에 화학 도구를 증강하는 방법이 ether0의 화학 구조 출력 능력 향상에 활용될 수 있다.
- 🧪 응용 사례: [[papers/1106_The_BOS-Lig_Dataset_Accurate_Ligand_Charges_from_a_Consensus/review]] — 화학 도구로 대규모 언어 모델을 증강하여 본 논문의 리간드 전하 데이터를 화학 언어 모델링에 활용할 수 있다.
