---
title: "131_Automating_exploratory_proteomics_research_via_language_mode"
authors:
  - "Ning Ding"
  - "Shang Qu"
  - "Linhai Xie 외"
date: "2024"
doi: "N/A"
arxiv: ""
score: 4.0
essence: "본 논문은 대규모 언어모델(LLM)을 활용하여 원본 단백질체학(proteomics) 데이터로부터 자동으로 과학적 발견을 수행하는 PROTEUS 시스템을 제시한다. 인간의 개입 없이 계층적 계획 수립, 생물정보학 도구 실행, 반복적 분석 워크플로우 정제를 통해 고품질의 생물학적 가설을 생성한다."
tags:
  - "cat/LLM-Based_Scientific_Reasoning"
  - "sub/Domain-specific_Scientific_Reasoning"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Langfelder and Horvath_2024_Automating exploratory proteomics research via language models.pdf"
---

# Automating exploratory proteomics research via language models

> **저자**: Ning Ding, Shang Qu, Linhai Xie 외 | **날짜**: 2024 | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp) *PROTEUS의 반복적 개선 프레임워크(a)와 상세한 작업 프로세스(b). 데이터 설명, 연구 목표 계획, 워크플로우 계획, 도구 실행, 결과 해석의 순환 구조*

본 논문은 대규모 언어모델(LLM)을 활용하여 원본 단백질체학(proteomics) 데이터로부터 자동으로 과학적 발견을 수행하는 PROTEUS 시스템을 제시한다. 인간의 개입 없이 계층적 계획 수립, 생물정보학 도구 실행, 반복적 분석 워크플로우 정제를 통해 고품질의 생물학적 가설을 생성한다.

## Motivation

- **Known**: 현대 고처리량 단백질체학 기술은 대규모 단백질 발현 데이터를 생산하며, 이를 통해 생물학적 기전, 질병 메커니즘, 치료 표적 발굴이 가능하다.

- **Gap**: 기존 단백질체학 연구는 인간 전문가에 의존하여 데이터 분석, 도구 선택, 연구 방향 결정이 이루어지며, 이는 시간 소모적이고 연구자의 편향을 초래할 수 있다. 또한 LLM을 활용한 기존 오믹스 연구는 개별 분석 단계에만 한정되어 있다.

- **Why**: LLM의 강력한 지시 따르기 능력, 복잡한 계획 수립 역량, 다양한 도구 호출 능력, 그리고 외부 정보 검색을 통한 할루시네이션 감소 능력은 전체 단백질체학 연구 프로세스 자동화에 적합하다.

- **Approach**: 계층적 계획 프레임워크(연구 목표 → 분석 워크플로우 → 분석 단계)를 통해 LLM을 조율하고, 반복적 개선 메커니즘을 도입하여 중간 결과 기반의 동적 계획 수정을 가능케 한다.

## Achievement

![Figure 2](figures/fig2.webp) *전체 191개 가설에 대한 5개 지표별 평균 점수 및 분포*

1. **포괄적 자동화 달성**: 12개의 다양한 단백질체학 데이터셋(면역세포, 종양, 단일세포/대량 샘플)에서 191개의 과학적 가설을 자동 생성하였으며, 인간 전문가 개입 없이 완전한 end-to-end 분석 수행이 가능함을 입증했다.

2. **높은 평가 점수 확보**: LLM 기반 자동 평가(5개 지표)와 인간 전문가 평가 모두에서 일관되게 높은 점수를 획득했으며, 생성된 가설들이 기존 문헌과 잘 부합하면서도 새로운 검증 가능한 가설을 제시함을 확인했다.

![Figure 3](figures/fig3.webp) *SPDB 데이터셋 10개에 대한 5개 지표별 점수 분포*

## How

- **도메인 특화 모델**: Llama 3.1 70B를 UltraMedical 데이터셋으로 미세조정하여 생물의학 분야 지식과 분석 능력 강화
  
- **계층적 계획 구조**: 
  - 상위 레벨: 연구 목표 동적 생성 및 정제
  - 중간 레벨: 각 목표별 분석 워크플로우 시퀀스 계획
  - 하위 레벨: 특화된 생물정보학 도구를 통한 단계별 실행

- **반복적 개선 메커니즘**: 각 워크플로우/목표 완료 후 최신 결과 분석하여 후속 계획 동적 갱신

- **다중 평가 체계**: 
  - 자동 평가: 5개 지표(신뢰성, 참신성, 생물학적 타당성, 논리적 일관성, 데이터 근거성)
  - 인간 평가: 동일 지표 적용 및 상세 질적 피드백

![Figure 4](figures/fig4.webp) *2개 임상 코호트 데이터셋에 대한 5개 지표별 점수 분포*

## Originality

- **완전 자동화된 end-to-end 파이프라인**: 기존 연구들이 개별 단계 자동화나 인간 개입 필요성을 보유한 것과 달리, PROTEUS는 원본 데이터에서 최종 가설 생성까지 완전 자동화 달성

- **생물정보학 도구 활용의 유연성**: CATALYST, diffcyt, BioEnricher 등 다양한 특화 도구를 동적으로 선택·실행하여 다양한 단백질체학 데이터 유형 적응

- **포괄적 평가 체계**: 자동 평가와 전문가 평가를 결합한 다층적 검증으로 결과의 신뢰성과 참신성 동시 입증

- **동적 가설 도출**: 정적인 미리 정의된 절차가 아닌 LLM의 추론 능력을 통해 데이터로부터 새로운 관점의 가설 제시

## Limitation & Further Study

- **모델 크기 및 계산 비용**: 70B 파라미터 모델의 높은 계산 요구로 확장성 제한 가능성. 경량 모델로의 최적화나 증류(distillation) 기법 필요

- **평가 지표의 객관성**: LLM 기반 자동 평가의 편향 가능성. 더 많은 데이터셋과 더 다양한 전문가 평가 필요

- **도구 라이브러리 확장**: 현재 통합된 생물정보학 도구 세트의 확장 및 다양한 오믹스 데이터(genomics, metabolomics) 통합

- **생물학적 타당성 검증**: 생성된 가설들의 실험적 검증 및 새로운 생물학적 발견으로의 전환 가능성 평가

- **해석 가능성 개선**: 가설 생성 과정의 중간 추론 단계 시각화 및 사용자 개입 지점 제공

![Figure 5](figures/fig5.webp) *PROTEUS의 백본으로 자체 모델과 GPT-4o 사용 결과 비교*

## Evaluation

- **Novelty**: 4.5/5
  - 완전 자동화된 end-to-end 단백질체학 분석 시스템 제시는 혁신적이나, LLM 기반 과학 자동화의 개념 자체는 새로운 것이 아님

- **Technical Soundness**: 4/5
  - 계층적 프레임워크 설계와 반복적 개선 메커니즘이 건전하고, 도메인 특화 모델 미세조정은 적절하나, 일부 기술적 세부사항(예: 워크플로우 간 연계 메커니즘)이 불명확함

- **Significance**: 4.5/5
  - 단백질체학 연구 자동화를 통한 실질적 시간 단축과 연구자 편향 완화 가능성이 높으며, 191개 가설 생성을 통한 규모의 입증이 강력하나, 실제 생물학적 발견으로의 전환 사례가 제한적

- **Clarity**: 3.5/5
  - 시스템 프레임워크와 전체 구조는 명확하게 설명되었으나, 각 모듈(특히 Workflow Updater, Objective Updater)의 구체적 작동 알고리즘과 프롬프트 설계가 충분히 상세히 기술되지 않음

- **Overall**: 4/5

**총평**: PROTEUS는 LLM을 활용한 단백질체학 데이터 분석 및 가설 생성의 완전 자동화를 성공적으로 구현한 혁신적 시스템이며, 포괄적 평가를 통해 신뢰성과 참신성을 입증했다. 다만 생성된 가설의 실험적 검증, 더 다양한 생물학적 영역으로의 확장, 그리고 기술적 세부사항의 투명성 개선이 필요하다.

## Related Papers

- 🏛 기반 연구: [[papers/558_Moose-chem3_Toward_experiment-guided_hypothesis_ranking_via/review]] — 단백질체학 자동 분석이 실험 피드백 기반 가설 평가의 생물정보학 기반
- 🔄 다른 접근: [[papers/176_CACTUS_Chemistry_Agent_Connecting_Tool_Usage_to_Science/review]] — 단백질체학 vs 화학정보학으로 도메인은 다르지만 유사한 자동화 도구 통합 접근
- 🔗 후속 연구: [[papers/164_BioInformatics_Agent_BIA_Unleashing_the_Power_of_Large_Langu/review]] — 생물정보학 에이전트를 단백질체학 특화 자동 발견으로 구체화한 응용
- 🔄 다른 접근: [[papers/371_GeneAgent_self-verification_language_agent_for_gene-set_anal/review]] — 단백질체학 vs 유전자 세트 분석으로 생물정보학의 서로 다른 자동화 영역
- 🔗 후속 연구: [[papers/558_Moose-chem3_Toward_experiment-guided_hypothesis_ranking_via/review]] — 단백질체학 자동 분석을 시뮬레이션 실험 설계로 확장한 방법론
- 🔄 다른 접근: [[papers/176_CACTUS_Chemistry_Agent_Connecting_Tool_Usage_to_Science/review]] — 화학정보학 vs 단백질체학으로 도메인은 다르지만 유사한 자동화 도구 통합 접근
