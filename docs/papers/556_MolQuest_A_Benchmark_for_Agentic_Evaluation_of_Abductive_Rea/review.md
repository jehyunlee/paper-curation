---
title: "556_MolQuest_A_Benchmark_for_Agentic_Evaluation_of_Abductive_Rea"
authors:
  - "Taolin Han"
  - "Shuang Wu"
  - "Jinghang Wang"
  - "Yuhao Zhou"
  - "Renquan Lv"
date: "2026.03"
doi: "N/A"
arxiv: ""
score: 4.3
essence: "본 논문은 화학 구조 해석 작업을 동적 다중 턴 에이전트 평가 벤치마크로 재정의한 MolQuest를 제안한다. 정적 QA 형식의 기존 과학 벤치마크의 한계를 극복하기 위해, 실제 화학 문헌 데이터 기반의 상호작용적 환경에서 LLM의 귀추적 추론(abductive reasoning) 및 전략적 의사결정 능력을 평가한다."
tags:
  - "cat/LLM-Based_Scientific_Reasoning"
  - "sub/Domain-specific_Scientific_Reasoning"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Han et al._2026_MolQuest A Benchmark for Agentic Evaluation of Abductive Reasoning in Chemical Structure Elucidatio.pdf"
---

# MolQuest: A Benchmark for Agentic Evaluation of Abductive Reasoning in Chemical Structure Elucidation

> **저자**: Taolin Han, Shuang Wu, Jinghang Wang, Yuhao Zhou, Renquan Lv, Bing Zhao, Wei Hu | **날짜**: 2026-03-26 | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp) *분자 구조 해석을 제약 만족 문제(CSP)로 표현*

본 논문은 화학 구조 해석 작업을 동적 다중 턴 에이전트 평가 벤치마크로 재정의한 MolQuest를 제안한다. 정적 QA 형식의 기존 과학 벤치마크의 한계를 극복하기 위해, 실제 화학 문헌 데이터 기반의 상호작용적 환경에서 LLM의 귀추적 추론(abductive reasoning) 및 전략적 의사결정 능력을 평가한다.

## Motivation

- **Known**: 최근 LLM(GPT-5.2, Gemini 3-Pro, Qwen-3-Max 등)의 추론 능력이 급속히 발전하고 있으며, AI for Science 분야에서 중요성이 증대되고 있음

- **Gap**: 기존 과학 벤치마크(ChemBench, ChemIQ 등)는 세 가지 핵심 한계 보유:
  1. 정적 단일턴 QA 형식으로 실제 과학 연구의 복잡성 미반영
  2. 합성 시뮬레이션 데이터 사용으로 실제 노이즈, 피크 오버랩 등 현실 요소 부재
  3. 실험 계획 및 전략적 의사결정 능력 평가 부족

- **Why**: 실제 과학자는 불완전한 정보 환경에서 비용 제약 하에 가장 유익한 다음 실험을 선택하는 적극적 에이전트로 활동하므로, 이러한 동적 특성을 평가해야 함

- **Approach**: 화학 문헌 지원정보(Supporting Information)에서 추출한 실제 데이터와 상태머신 기반 상호작용 환경을 통합하여, 모델이 도구를 호출하고 가설을 반복적으로 정제하는 과정을 평가

## Achievement

![Figure 2](figures/fig2.webp) *MolQuest 벤치마크의 핵심 특성(동적 상호작용, 실데이터 기반, 다차원 평가)*

1. **혁신적 평가 패러다임**: 정적 QA에서 동적 순차적 의사결정(sequential decision-making) 문제로의 재정의로, 실제 실험실 워크플로우를 반영한 "계획-요청-추론" 루프 구현

2. **고품질 실데이터셋 구성**: 2025년 이후 발표된 화학 문헌에서 추출한 데이터로 50% 이상의 테스트 케이스 확보, 학습 데이터 오염 위험 최소화

3. **심각한 성능 격차 발견**: SOTA 모델도 약 50% 정도의 정확도만 달성하며, 대부분 모델은 30% 이하의 성능을 보임. 이는 LLM의 전략적 과학적 추론 능력의 심각한 부족을 입증

4. **포괄적 평가 프레임워크**: 12개 SOTA LLM에 대한 광범위한 평가 수행, 최종 답변 정확도를 넘어 의사결정 로직과 추론 과정 평가

## How

![Figure 3](figures/fig3.webp) *데이터 처리 파이프라인: LLM 자동화와 전문가 검증의 인루프 결합*

- **작업 정의**: 분자 구조 해석을 제약 만족 문제(CSP)로 형식화. 미지의 샘플로부터 시작하여 NMR, MS 등 스펙트럼 증거와 일치하는 화학적으로 유효한 분자 구조 식별

- **데이터 구성 파이프라인**:
  - 최근 화학 문헌의 지원정보(Supporting Information)로부터 직접 추출
  - LLM 자동화: 초기 데이터 추출 시간 단축
  - 휴먼-인-더-루프 검증: 4가지 주요 오류 모드 수정
    - 교환 가능한 양성자(−OH, −COOH) 인식 실패
    - SMILES 문자열 원자 계산 오류
    - 스펙트럼 피크 편차 오판
    - 질량분석 애덕트 혼동([M+H]⁺ vs [M+Na]⁺)

- **동적 상호작용 환경 설계**:
  - 상태머신 기반 에이전트 인터페이스
  - 도구 호출 메커니즘("분자량 측정", "¹H NMR 스펙트럼 획득" 등)
  - 정보 비대칭성: 초기 스펙트럼 데이터 미공개, 필요시 요청
  - 비용 제약 시뮬레이션: 자원 효율적 의사결정 평가

- **다차원 평가 메트릭**:
  - 최종 답변 정확도
  - 의사결정 로직과 추론 과정의 질
  - 복잡한 환경에서의 전략적 선택

## Originality

- **최초성**: 화학 구조 해석을 실제 화학 문헌 기반 데이터로 다중턴 에이전트 태스크로 공식화한 최초 벤치마크

- **메타데이터 진정성**: 2025년 이후 발표 논문 활용으로 학습 데이터 오염 위험을 체계적으로 배제

- **인루프 설계의 엄밀성**: LLM의 자동화 효율성과 도메인 전문가의 정확성을 결합한 데이터 구성 파이프라인으로 높은 신뢰성 확보

- **현실 시나리오 재현**: 단순 정규화된 데이터가 아닌 실제 노이즈, 피크 오버랩, 정보 부족을 포함한 현실적 과학 문제 반영

- **에이전트 관점의 전환**: 수동적 응답 대신 적극적 실험 계획과 비용-효과적 의사결정을 요구하는 근본적 문제 재정의

## Limitation & Further Study

- **데이터 규모 미시**: 논문에서 구체적인 벤치마크 크기(테스트 케이스 수)가 명시되지 않아 통계적 신뢰성 평가 어려움

- **모델 성능 저조의 원인 분석 부족**: SOTA 모델의 50% 성능이 도메인 지식 부족, 추론 능력 한계, 또는 도구 호출 전략 미숙 중 어느 것 때문인지에 대한 심층 분석 필요

- **스펙트럼 복잡도의 이질성**: 실제 화학 문헌의 스펙트럼은 복잡도가 매우 이질적이므로, 작업 난이도의 체계적 분류 및 제어 전략 필요

- **후속 연구**:
  - 저성능 원인 분석 및 특정 추론 모듈 개선 연구
  - 비용 제약 파라미터 변화에 따른 에이전트 적응 능력 평가
  - 다중 에이전트 협력 시나리오로의 확장
  - 다른 과학 도메인(단백질 구조, 신약 발견 등)으로의 벤치마크 일반화


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4/5
- Significance: 4.5/5
- Clarity: 4/5
- Overall: 4.3/5

**총평**: MolQuest는 기존의 정적 QA 기반 과학 벤치마크의 근본적 한계를 인식하고, 실제 과학 연구의 동적·상호작용적 특성을 충실히 반영한 혁신적 평가 프레임워크를 제시한다. 특히 인루프 데이터 구성과 실제 문헌 기반 데이터 활용으로 높은 신뢰성을 확보했으며, SOTA 모델들의 심각한 성능 격차 발견은 AI for Science 연구의 중요한 방향을 제시한다. 다만 저성능의 원인 분석 심화와 벤치마크 규모에 대한 상세 기술이 추가되면 더욱 완성도 높은 논문이 될 것으로 예상된다.

## Related Papers

- 🧪 응용 사례: [[papers/209_ChemAgent_Self-updating_Library_in_Large_Language_Models_Imp/review]] — ChemAgent의 화학 추론 능력이 분자 구조 해석 평가에 활용됩니다.
- 🔗 후속 연구: [[papers/704_SciAgentGym_Benchmarking_Multi-Step_Scientific_Tool-use_in_L/review]] — 분자 추론이 다단계 과학 도구 사용 벤치마크로 확장됩니다.
- 🏛 기반 연구: [[papers/726_Sciknoweval_Evaluating_multi-level_scientific_knowledge_of_l/review]] — 다층적 과학 지식 평가가 화학 귀추적 추론의 기반을 제공합니다.
- 🏛 기반 연구: [[papers/209_ChemAgent_Self-updating_Library_in_Large_Language_Models_Imp/review]] — 화학 추론을 위한 자체 업데이트 라이브러리가 분자 구조 해석의 기반을 제공합니다.
- 🧪 응용 사례: [[papers/726_Sciknoweval_Evaluating_multi-level_scientific_knowledge_of_l/review]] — 다층적 과학 지식 평가가 화학 추론 벤치마크에 적용됩니다.
