---
title: "002_34_examples_of_llm_applications_in_materials_science_and_che"
authors:
  - "Lei Wang"
  - "Chen Ma"
  - "Xueyang Feng"
  - "Zeyu Zhang"
  - "Hao Yang"
date: "2025"
doi: ""
arxiv: ""
score: 4.0
essence: "재료과학과 화학 분야에서 대규모 언어모델(LLM)의 34가지 응용 사례를 분석하여 자동화, 어시스턴트, 에이전트 및 가속화된 과학 발견을 위한 LLM의 역할을 제시한다."
tags:
  - "cat/AI-Powered_Scientific_Research_Frameworks"
  - "sub/Domain-specific_Language_Agents"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Wang et al._2025_34 examples of llm applications in materials science and chemistry Towards automation, assistants,.pdf"
---

# 34 examples of llm applications in materials science and chemistry: Towards automation, assistants, agents, and accelerated scientific discovery

> **저자**: Lei Wang, Chen Ma, Xueyang Feng, Zeyu Zhang, Hao Yang, Jingsen Zhang, Zhiyuan Chen, Jiakai Tang, Xu Chen, Yankai Lin, Wayne Xin Zhao, Zhewei Wei, Ji-Rong Wen | **날짜**: 2025 | **URL**: [https://arxiv.org/abs/2505.03049](https://arxiv.org/abs/2505.03049)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1: The LLM-Powered Research Constellation. At each stage of the research process, from initial*

재료과학과 화학 분야에서 대규모 언어모델(LLM)의 34가지 응용 사례를 분석하여 자동화, 어시스턴트, 에이전트 및 가속화된 과학 발견을 위한 LLM의 역할을 제시한다.

## Motivation

- **Known**: LLM은 분자 성질 예측, 자동화된 실험 워크플로우, 사용자 인터페이스 개발 등 화학·재료과학 연구에 활용되어 왔다. 최근 모델들은 구조화된 데이터와 비정형 데이터를 통합하고 가설 생성을 지원할 수 있다.
- **Gap**: LLM의 급속한 발전에도 불구하고 재료과학과 화학 분야의 구체적인 고영향 응용 사례, 효과적인 구현 방식, 그리고 신뢰성·해석가능성·재현성 문제에 대한 체계적 분석이 부족하다.
- **Why**: LLM은 복잡한 데이터 양식, 이질적인 데이터 포맷, 희소한 실험 데이터셋을 다루는 재료과학·화학 분야에서 특히 가치 있으며, 연구 수명주기 전체에 걸친 통합적 활용이 가능하기 때문이다.
- **Approach**: 제2회 재료과학·화학 LLM 해커톤에서 수집한 34개 프로젝트를 분자/재료 성질 예측, 설계, 자동화, 과학 커뮤니케이션, 데이터 관리, 가설 생성, 지식 추출 등 7개 연구 영역으로 분류하여 분석한다.

## Achievement

![Figure 1](figures/fig1.webp)

*Figure 1: The LLM-Powered Research Constellation. At each stage of the research process, from initial*

- **분자/재료 성질 예측**: 오비탈 기반 본딩 분석 정보, 3D 분자 특징 벡터, 분광 데이터 등을 활용하여 저데이터 환경에서 성능 향상
- **분자/재료 설계**: 거대 환형 펩타이드(MC-Peptide), 저밴드갭 금속-유기 프레임워크(MOF), 지속가능한 건설 재료 등의 자동 설계 워크플로우 개발
- **자동화 및 새로운 인터페이스**: LangSim, LLMicroscopilot 등 자연언어 기반 인터페이스로 복잡한 과학 도구의 접근성 향상
- **과학 커뮤니케이션 및 교육**: MaSTeA, LLMy-Way 등 맞춤형 교육 어시스턴트로 학습 경험 개선
- **연구 데이터 관리**: yeLLowhaMMer, LLMads, NOMAD Query Reporter 등 다중모달 에이전트를 통한 자동화된 데이터 처리
- **가설 생성 및 평가**: 다중 AI 에이전트와 통계적 접근을 통한 과학적 가설의 자동 생성 및 검증
- **지식 추출 및 추론**: 과학 문헌에서의 구조화된 정보 추출 및 지식 그래프 기반 추론

## How

![Figure 2](figures/fig2.webp)

*Figure 2: Schematic depicting the prompt for fine-tuning the LLM with Alpaca prompt format.*

- 제2회 LLM 해커톤 개최를 통한 글로벌 집단지성(crowdsourcing) 활용
- 34개 프로젝트를 7개 핵심 연구 영역으로 분류하여 체계적 분석
- 오픈소스 LLM(예: Alpaca)과 상용 LLM(GPT-4, Claude 등) 모두 활용
- ReAct 에이전트, 프롬프트 엔지니어링, 파인튜닝 등 다양한 기법 적용
- GitHub 저장소 링크 제공으로 재현성 및 접근성 확보
- 구조화된 데이터와 비정형 데이터의 통합 처리
- 저데이터 환경 및 학제간 연구에 최적화된 솔루션 개발

## Originality

- 재료과학·화학 분야의 LLM 응용을 7개 연구 영역으로 체계적으로 분류한 첫 번째 종합 분석
- 과학 해커톤이라는 혁신적 협업 프레임워크를 통한 대규모 다학제 프로젝트 수집
- LLM을 단순 예측 모델이 아닌 다목적 과학 도구 플랫폼으로 개념화
- 연구 수명주기 전체(아이디어→실험→커뮤니케이션→반복)를 망라하는 LLM 응용 제시
- 저데이터 환경에서의 LLM 효과 입증 및 실험적 검증

## Limitation & Further Study

- **신뢰성 문제**: LLM의 환각(hallucination) 현상이 과학 응용에서 검증 오류 야기 가능
- **해석가능성 부족**: 복잡한 LLM 의사결정 과정의 투명성 및 설명가능성 미흡
- **재현성 도전**: 모델 버전 변화와 확률적 특성으로 인한 결과 재현성 한계
- **도메인 특화성**: 일반 LLM의 재료과학·화학 도메인 지식 제한적
- **계산 비용**: 대규모 모델 운영의 금전적·환경적 비용
- **후속 연구 필요**: 도메인 특화 파인튜닝, 검증 메커니즘 강화, 신뢰도 평가 지표 개발, 실제 실험실 통합 연구 필요

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 논문은 재료과학·화학 분야에서 LLM의 광범위한 응용 사례를 체계적으로 분석하여 AI 기반 과학 발견의 가능성을 명확히 보여준다. 다만 신뢰성, 해석가능성, 재현성 등의 근본적 과제 해결이 실제 과학 워크플로우 통합의 선결 조건이다.

## Related Papers

- 🏛 기반 연구: [[papers/465_Large_Language_Model_in_Materials_Science_Roles_Challenges_a/review]] — 재료과학에서 대규모 언어모델의 역할과 도전과제에 대한 이론적 토대를 제공한다.
- 🧪 응용 사례: [[papers/523_MatterChat_A_Multi-Modal_LLM_for_Material_Science/review]] — 재료과학 특화 다중모달 LLM의 구체적인 구현 사례를 보여준다.
