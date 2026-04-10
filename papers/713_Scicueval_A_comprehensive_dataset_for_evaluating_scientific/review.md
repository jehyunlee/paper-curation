---
title: "713_Scicueval_A_comprehensive_dataset_for_evaluating_scientific"
authors:
  - "Jing Yu"
  - "Yuqi Tang"
  - "Kehua Feng"
  - "Lei Liang"
  - "Qiang Zhang"
date: "2025"
doi: "10.48550/arXiv.2505.15094"
arxiv: ""
score: 4.2
essence: "본 논문은 대규모 언어모델(LLM)의 과학적 맥락 이해 능력을 평가하기 위한 포괄적 벤치마크 데이터셋 SciCUEval을 제안한다. 생물학, 화학, 물리학, 생의학, 재료과학 등 5개 도메인에 걸친 10개의 부분 데이터셋으로 구성되며, 비정형 텍스트, 구조화된 표, 지식 그래프 등 다양한 데이터 모달리티를 통합하여 LLM의 과학적 맥락 이해 능력을 체계적으로 평가한다."
tags:
  - "cat/Cognitive_AI_Evaluation_and_Benchmarking"
  - "sub/Cognitive_LLM_Evaluation"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Yu et al._2025_Scicueval A comprehensive dataset for evaluating scientific context understanding in large language.pdf"
---

# Scicueval: A comprehensive dataset for evaluating scientific context understanding in large language models

> **저자**: Jing Yu, Yuqi Tang, Kehua Feng, Lei Liang, Qiang Zhang, Keyan Ding, Huajun Chen | **날짜**: 2025 | **DOI**: [10.48550/arXiv.2505.15094](https://doi.org/10.48550/arXiv.2505.15094)

---

## Essence

![Figure 1: Overview of the SciCUEval dataset](figures/fig1.webp)
*SciCUEval은 5개 과학 도메인, 3가지 데이터 모달리티, 4가지 질문 유형을 포함하는 포괄적 벤치마크*

본 논문은 대규모 언어모델(LLM)의 과학적 맥락 이해 능력을 평가하기 위한 포괄적 벤치마크 데이터셋 SciCUEval을 제안한다. 생물학, 화학, 물리학, 생의학, 재료과학 등 5개 도메인에 걸친 10개의 부분 데이터셋으로 구성되며, 비정형 텍스트, 구조화된 표, 지식 그래프 등 다양한 데이터 모달리티를 통합하여 LLM의 과학적 맥락 이해 능력을 체계적으로 평가한다.

## Motivation

- **Known**: LLM은 일반 영역에서 우수한 자연어 이해, 추론, 생성 능력을 보여주었으나, 과학 도메인 적용 시 밀도 높은 기술 용어, 다중 모달 데이터, 복잡한 개념 간 관계로 인한 어려움 존재

- **Gap**: 기존 과학 도메인 LLM 벤치마크(SciQA, MMLU-STEM 등)는 주로 직접 질문-답변 작업에 초점을 두며, 긴 맥락 처리 능력, 다양한 데이터 모달리티(표, 그래프), 정보 부재 감지 등의 중요한 능력을 평가하지 못함

- **Why**: 과학적 맥락 이해는 정보 추출, 정보 격차 인식, 다중 증거원 통합, 맥락 기반 추론을 요구하는데, 이를 종합적으로 평가할 벤치마크 부재

- **Approach**: 5개 과학 도메인, 3개 데이터 모달리티를 아우르는 11,343개 표본으로 구성된 SciCUEval 데이터셋 구축 및 4가지 핵심 역량 평가 체계 수립

## Achievement

1. **포괄적 벤치마크 구축**: 기존 벤치마크 대비 유일하게 다중 과학 도메인, 다양한 데이터 모달리티(텍스트, 표, 지식 그래프), 4가지 질문 유형(개방형 Q&A, 객관식, 참/거짓, 완성형)을 통합하는 과학적 맥락 이해 평가 스위트 제공

2. **체계적 역량 평가 프레임워크**: 관련 정보 식별(Relevant Information Identification), 정보 부재 감지(Information-absence Detection), 다중 정보원 통합(Multi-source Information Integration), 맥락 기반 추론(Context-aware Inference)의 4가지 핵심 역량을 체계적으로 측정

3. **대규모 LLM 성능 분석**: GPT-4, Claude, Gemini 등 최첨단 LLM의 강점과 한계를 세밀하게 분석하여 과학 도메인 LLM 개발 방향 제시

## How

![Figure 1에서 볼 수 있듯이 데이터 생성 파이프라인](figures/fig2.webp)
*데이터 생성 과정: 과학 데이터 수집 → 질문 답변 생성 → 검증*

- **데이터 수집**: arXiv 논문, IAEA 핵데이터, Material Project, PubChem, PrimeKG, PharmKG 등 고품질 과학 소스에서 데이터 추출

- **데이터 모달리티 다양화**: 
  - 비정형 텍스트: 최근 연구 논문 및 실험 프로토콜 (arXiv)
  - 구조화된 표: 핵 데이터, 물질 특성, 분자/단백질 정보
  - 반정형 지식 그래프: 과학적 실체와 관계 네트워크

- **질문 생성 전략**: 각 역량별로 다양한 질문 유형을 설계하되, 자동 생성과 수동 검증을 결합하여 데이터 품질 보장

- **평가 체계**: 
  - 관련 정보 식별: 긴 맥락에서 필요한 정보를 정확히 추출하는 능력
  - 정보 부재 감지: 불충분한 정보 상황에서 응답 거절 능력
  - 다중 정보원 통합: 여러 맥락 세그먼트의 정보 집계 및 비교
  - 맥락 기반 추론: 단편적 정보로부터 논리적 추론 능력

## Originality

- **첫 포괄적 과학 도메인 벤치마크**: 기존 연구들이 특정 도메인(화학) 또는 단일 모달리티(텍스트)에 초점을 둔 반면, SciCUEval은 5개 도메인 × 3개 모달리티 조합의 첫 벤치마크

- **새로운 역량 평가 차원**: 정보 부재 감지(Information-absence Detection)와 같이 LLM의 할루시네이션(hallucination) 문제를 직접 평가하는 신규 역량 도입

- **이질적 데이터 모달리티 통합**: 기존 벤치마크가 텍스트 중심인 반면, 지식 그래프와 구조화된 표를 포함하여 과학 데이터의 다양한 표현 방식 반영

- **규모와 다양성**: 11,343개 표본으로 기존 과학 도메인 데이터셋(ChemLit-QA 1,054개, CHEMRAG-BENCH 1,932개)보다 훨씬 큼

## Limitation & Further Study

- **도메인 커버리지 제한**: 5개 주요 과학 도메인만 포함되며, 지구과학, 천문학 등 다른 중요 분야 부재

- **데이터 생성 자동화 수준**: 완전 자동화된 질문-답변 생성 방식의 한계로 인해 수동 검증 비율이 높을 수 있으며, 이로 인한 규모 확장의 어려움

- **다중 모달리티 동시 처리**: 텍스트, 표, 그래프를 동시에 처리하는 멀티모달 LLM의 평가 전략이 명확하지 않음

- **맥락 길이 분석 부족**: 서로 다른 길이의 맥락이 성능에 미치는 영향을 세분화하여 분석하지 않은 점

- **후속 연구 방향**: 
  - 추가 도메인 및 언어로의 확장
  - 멀티모달 LLM(예: GPT-4V, Claude with vision)에 대한 체계적 평가
  - 벤치마크 기반 과학 도메인 특화 LLM 파인튜닝 방법론 개발
  - 동적 평가 환경 도입(새로운 과학 데이터 지속적 추가)

## Evaluation

- **Novelty**: 4.5/5
  - 포괄적 다중 도메인, 다중 모달리티 벤치마크의 첫 시도로 높은 참신성
  - 정보 부재 감지 같은 새로운 역량 평가 차원 제시
  - 다만 개별 역량 개념 자체는 기존 연구에서 영감을 받음

- **Technical Soundness**: 4/5
  - 체계적인 데이터 수집 및 검증 프로세스
  - 명확한 평가 프레임워크와 역량 정의
  - 다만 자동 생성 및 검증 방법론의 상세한 설명 부족, 수동 검증의 편향 가능성 미분석

- **Significance**: 4.5/5
  - 과학 도메인 LLM 평가의 중대한 공백을 해결
  - 다양한 LLM 개발팀에 유용한 표준 벤치마크 제공
  - 다만 벤치마크 기반 실제 과학 응용 시스템 개선 효과 실증 필요

- **Clarity**: 4/5
  - 논문 전체 구조가 명확하고 Figure 1이 전체 개요를 잘 표현
  - 4가지 역량의 정의가 분명함
  - 다만 데이터 생성 파이프라인의 상세 과정(자동화 정도, 검증 기준)에 대한 설명 부족

- **Overall**: 4.2/5

**총평**: SciCUEval은 과학 도메인 LLM 평가의 중요한 공백을 체계적으로 해결하는 포괄적 벤치마크로, 다중 도메인-다중 모달리티 조합과 4가지 핵심 역량 평가 프레임워크는 매우 우수하다. 다만 데이터 생성 방법론의 투명성 강화, 멀티모달 처리에 대한 명확한 전략 제시, 그리고 벤치마크 활용을 통한 실제 과학 LLM 개선 효과 입증이 필요하다.

## Related Papers

- 🔄 다른 접근: [[papers/016_A_practical_evaluation_of_AutoML_tools_for_binary_multiclass/review]] — AutoML 도구의 체계적 벤치마킹과 과학적 맥락 이해 평가는 모두 AI 시스템의 실제 성능을 종합적으로 측정하는 서로 다른 접근법입니다
- 🔗 후속 연구: [[papers/552_Mmsci_A_dataset_for_graduate-level_multi-discipline_multimod/review]] — 대학원 수준의 다학제 멀티모달 과학 데이터셋은 SciCUEval의 과학적 맥락 이해를 더욱 고도화한 벤치마크입니다
- 🏛 기반 연구: [[papers/706_SciBench_Evaluating_College-Level_Scientific_Problem-Solving/review]] — 대학 수준의 과학 문제 해결 평가는 과학적 맥락 이해 능력 측정의 기반이 되는 문제 해결 능력 평가 방법론입니다
- 🔗 후속 연구: [[papers/724_SciHorizon_Benchmarking_AI-for-Science_Readiness_from_Scient/review]] — 과학적 이해 평가를 위한 포괄적 데이터셋이 SciHorizon의 평가 범위를 확장한다.
- 🔄 다른 접근: [[papers/006_A_deep_subgrouping_framework_for_precision_drug_repurposing/review]] — 환자 하위군 기반 정밀 약물 재창출과 과학적 맥락 이해 평가는 모두 의료/과학 분야에서 AI의 실제 성능을 체계적으로 평가하는 서로 다른 접근법입니다
- 🔄 다른 접근: [[papers/016_A_practical_evaluation_of_AutoML_tools_for_binary_multiclass/review]] — AutoML 도구 벤치마킹과 과학적 맥락 이해 평가는 모두 AI 시스템의 실제 성능을 종합적으로 측정하는 서로 다른 접근법입니다
- 🔄 다른 접근: [[papers/726_Sciknoweval_Evaluating_multi-level_scientific_knowledge_of_l/review]] — 과학 지식 평가를 위한 서로 다른 포괄적 접근법을 제시합니다.
