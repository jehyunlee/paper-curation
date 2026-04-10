---
title: "378_Generative_AI_Uses_and_Risks_for_Knowledge_Workers_in_a_Scie"
authors:
  - "Kelly B. Wagman"
  - "Matthew T. Dearing"
  - "Marshini Chetty"
date: "2025"
doi: "10.1145/3706598.3713827"
arxiv: ""
score: 4.2
essence: "미국 국립연구소(Argonne National Laboratory)의 실제 배포 사례를 통해 과학 조직의 과학자와 운영 담당자들이 생성형 AI를 어떻게 사용하고 있으며, 어떤 우려사항을 가지고 있는지를 실증적으로 규명한 연구이다."
tags:
  - "cat/AI-Powered_Scientific_Research_Frameworks"
  - "sub/AI_for_Science_Taxonomy"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Wagman et al._2025_Generative AI Uses and Risks for Knowledge Workers in a Science Organization.pdf"
---

# Generative AI Uses and Risks for Knowledge Workers in a Science Organization

> **저자**: Kelly B. Wagman, Matthew T. Dearing, Marshini Chetty | **날짜**: 4월 25, 2025 | **DOI**: [10.1145/3706598.3713827](https://doi.org/10.1145/3706598.3713827)

---

## Essence

미국 국립연구소(Argonne National Laboratory)의 실제 배포 사례를 통해 과학 조직의 과학자와 운영 담당자들이 생성형 AI를 어떻게 사용하고 있으며, 어떤 우려사항을 가지고 있는지를 실증적으로 규명한 연구이다.

## Motivation

- **Known**: 생성형 AI가 과학 발견을 가속화할 수 있는 잠재력을 가지고 있으며, 일반적인 지식 노동(knowledge work) 환경에서의 활용 사례들이 연구되고 있음.

- **Gap**: 과학 조직의 맥락에서 생성형 AI의 실제 활용 사례와 인식된 위험성에 대한 실증적 연구가 부족함. 특히 과학자뿐만 아니라 운영 담당자(IT, HR, Finance 등)를 포함한 조직 전체 수준의 연구가 없고, 민감한 데이터를 다루는 과학 조직의 보안/개인정보 관련 우려에 초점을 맞춘 연구가 미흡함.

- **Why**: 국립연구소와 같은 과학 조직이 생성형 AI를 효과적으로 도입하려면 실제 사용자들의 요구사항과 우려사항을 이해해야 하며, 이는 다른 지식 노동 조직(금융, 법률 등)에도 시사점을 제공할 수 있음.

- **Approach**: 설문조사(N=66), 반구조화 심층 인터뷰(N=22), 그리고 내부 생성형 AI 인터페이스(Argo, GPT-3.5 Turbo 기반)의 8개월 사용 데이터 분석을 결합한 혼합 방법론 연구.

## Achievement

1. **Argo 사용 패턴**: 초기 배포 후 사용자 수가 점진적으로 증가하고 있으며, 과학 부서의 사용률이 운영 부서보다 높음. 대부분의 응답자가 LLM에 익숙하고 실험하고 있지만, 업무에 일관되게 통합한 경우는 적은 상태.

2. **사용 사례의 이분화**: 현재 및 미래 사용 사례들이 개념적으로 **코파일럿(Copilot)** 모드와 **워크플로우 에이전트(Workflow Agent)** 모드의 두 가지로 분류됨:
   - **코파일럿**: 사용자와 협력하며 대화형으로 응답 제공 (검증 가능한 코드/텍스트 작성)
   - **워크플로우 에이전트**: 자율 또는 반자율적으로 복잡한 작업을 수행 (대규모 비정형 텍스트 데이터에서 인사이트 추출)
   - 과학과 운영 부서 모두 유사한 코파일럿 상호작용을 보이지만, 에이전트 활용은 역할별로 차이를 보임.

3. **조직별 우려사항**: 신뢰성/할루시네이션(hallucination), 과도한 의존, 데이터 개인정보 보호/보안, 학술 출판 및 인용 관행의 변화, 고용과 채용에 미치는 영향에 대한 우려.

## How

![Figure 1: Argo 배포 이후 월별 운영/과학 부서의 고유 사용자 수 추이](figures/fig1.webp)
*초기 배포부터 8개월간 사용자 증가 추세*

![Figure 2: LLM(ChatGPT, Argo 등)에 대한 사용자 친숙도 설문 응답](figures/fig2.webp)
*대다수 응답자가 LLM에 대해 중간 이상의 친숙도를 보임*

![Figure 4: 업무 중 LLM 사용 빈도에 대한 설문 응답](figures/fig4.webp)
*규칙적 사용자는 소수이나 실험적 사용은 광범위함*

- **연구 방법**:
  - 설문조사: 66명 대상 폐쇄형/개방형 질문으로 LLM 친숙도, 사용 빈도, 우려사항 파악
  - 심층 인터뷰: 22명 대상 반구조화 인터뷰로 구체적 사용 사례와 맥락 파악
  - 사용 데이터 분석: 8개월간의 월별 활성 사용자 수, 부서별 비교 분석
  - 분석 기법: Thematic analysis로 반복되는 주제와 개념적 범주 추출

## Originality

- **조직 수준의 배포 사례**: 개별 과학자 연구와 달리 전 조직에 배포된 생성형 AI 인터페이스의 실제 사용 데이터를 제공하는 첫 사례 중 하나.

- **이질적 사용자 집단의 비교 분석**: 과학자와 운영 직원의 상이한 필요와 우려를 함께 연구하여, 지식 노동 조직의 폭넓은 구성을 반영.

- **보안/개인정보 관점의 중점**: 민감 데이터(분류 정보, 국가 안보, 미발표 연구)를 다루는 조직 특성을 반영하여 기술적 우려와 함께 조직 정책/윤리적 우려를 조명.

- **사용 모드의 개념적 분류**: 코파일럿 vs. 워크플로우 에이전트라는 분석 프레임이 향후 생성형 AI 시스템 설계와 기대치 관리를 위한 명확한 틀 제공.

## Limitation & Further Study

- **표본 크기 제한**: 설문 66명, 인터뷰 22명으로 조직 전체(수천 명)의 대표성이 제한적이며, 초기 도입 시기(early adopter) 편향 존재 가능성.

- **단일 조직 사례**: 단일 국립연구소에 대한 사례 연구로, 다른 과학 조직(대학, 민간 연구소) 또는 다른 지식 노동 영역(법률, 금융)으로의 일반화 제약.

- **제한된 생성형 AI 유형**: 주로 LLM(텍스트)에 초점하고 이미지 생성형 AI는 제외하여, 멀티모달 생성형 AI의 영향 미파악.

- **시간적 제약**: 8개월 초기 배포 기간 연구로, 장기적 사용 패턴 변화, 숙련도 향상에 따른 우려사항 변화, 조직 정책 정착의 영향 등 추적 불가.

- **향후 연구 방향**:
  - 반복 연구(longitudinal study): 12개월 이상 추적하여 사용 패턴의 안정화 및 조직 문화 변화 관찰
  - 비교 분석: 다양한 유형의 과학/지식 조직 간 비교 연구
  - 개입 연구(intervention study): 특정 정책(데이터 가이드라인, 윤리 교육)의 효과 측정
  - 에이전트 모드의 실제 구현: 현재 코파일럿 중심의 사용에서 워크플로우 에이전트로의 진화 추적

## Evaluation

- **Novelty**: 4.5/5 
  - 조직 수준 배포 사례와 과학 조직의 독특한 맥락 반영이 신선함. 다만 생성형 AI의 일반적 우려(할루시네이션, 일자리 영향)는 기존 문헌과 겹침.

- **Technical Soundness**: 4/5 
  - 설문, 인터뷰, 사용 데이터 분석을 적절히 결합한 혼합 방법론. 주제 분석(thematic analysis)의 구체적 절차와 신뢰도 평가 방법에 대한 설명이 다소 부족할 수 있음.

- **Significance**: 4.5/5 
  - 국립연구소, 대학, 금융/법률 기관 등 민감 데이터를 다루는 조직의 생성형 AI 정책 수립에 직접적 시사점 제공. HCI/CSCW 커뮤니티의 미충족 연구 영역을 채움.

- **Clarity**: 4/5 
  - 전체 구조와 주요 결과가 명확함. 코파일럿/워크플로우 에이전트 개념이 좋은 분석 틀을 제공하지만, 특정 인용문이나 구체적 사용 사례 예시가 더 풍부하면 가독성 향상 가능.

- **Overall**: 4.2/5

**총평**: 조직 현실에 기반한 생성형 AI 도입의 실증적 증거를 제시하며, 특히 과학 조직과 보안 민감 환경의 고유한 우려를 조명한 중요한 연구이다. 초기 도입 단계의 제한을 고려하면, 향후 종단적 후속 연구와 함께 과학 조직의 생성형 AI 거버넌스 구축에 실질적 기여를 할 것으로 예상된다.

## Related Papers

- 🔗 후속 연구: [[papers/890_Your_Brain_on_ChatGPT_Accumulation_of_Cognitive_Debt_when_Us/review]] — 과학 조직의 실제 AI 사용 패턴 분석을 개인 수준의 신경인지적 영향까지 확장하여 더 깊은 이해를 제공합니다.
- 🏛 기반 연구: [[papers/840_Transforming_Science_with_Large_Language_Models_A_Survey_on/review]] — 과학 연구에서 LLM 활용의 이론적 가능성에 대한 실제 현장 적용 사례와 한계를 제공합니다.
- 🧪 응용 사례: [[papers/562_Multi-agent_risks_from_advanced_ai/review]] — 다중 에이전트 AI 시스템의 위험 요소들이 실제 과학 조직에서 어떻게 나타나는지 구체적 사례를 보입니다.
- 🏛 기반 연구: [[papers/890_Your_Brain_on_ChatGPT_Accumulation_of_Cognitive_Debt_when_Us/review]] — 실제 과학 조직에서 생성형 AI 사용 패턴과 우려사항을 실증 분석하여 인지적 부채 현상의 맥락을 제공합니다.
- 🧪 응용 사례: [[papers/562_Multi-agent_risks_from_advanced_ai/review]] — 다중 에이전트 위험의 이론적 분석을 실제 과학 조직의 AI 도입 사례에서 검증할 수 있습니다.
- 🧪 응용 사례: [[papers/840_Transforming_Science_with_Large_Language_Models_A_Survey_on/review]] — LLM 기반 과학 연구 변혁의 이론적 전망을 실제 과학 조직의 구체적 적용 사례로 검증합니다.
- 🧪 응용 사례: [[papers/116_Augmenting_the_author_Exploring_the_potential_of_ai_collabor/review]] — 과학 연구 환경에서 생성형 AI 활용의 실제적 위험과 기회를 구체적으로 분석한다.
- 🔗 후속 연구: [[papers/517_Malinowski_in_the_age_of_ai_Can_large_language_models_create/review]] — 지식 근로자를 위한 생성형 AI 활용을 교육적 인류학 게임 창작으로 확장한 특화된 응용 연구입니다.
- 🧪 응용 사례: [[papers/912_Science_and_the_new_age_of_AI/review]] — 지식 근로자로서 과학자들의 AI 활용과 위험성을 구체적으로 분석한다
