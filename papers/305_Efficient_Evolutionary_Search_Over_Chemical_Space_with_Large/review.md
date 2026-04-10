---
title: "305_Efficient_Evolutionary_Search_Over_Chemical_Space_with_Large"
authors:
  - "Haorui Wang"
  - "Marta Skreta"
  - "C. Ser"
  - "Wenhao Gao"
  - "Lingkai Kong"
date: "2024"
doi: "10.48550/arXiv.2406.16976"
arxiv: ""
score: 4.4
essence: "대규모 언어모델(LLM)을 진화 알고리즘(EA)의 유전 연산자로 통합하여 화학 공간 탐색의 효율성을 획기적으로 향상시키는 MOLLEO 프레임워크를 제안한다. 이는 검은 상자 분자 최적화 문제에서 필요한 목적 함수 평가 횟수를 대폭 감소시킨다."
tags:
  - "cat/AI-Powered_Scientific_Research_Frameworks"
  - "sub/Domain-specific_Language_Agents"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Wang et al._2024_Efficient Evolutionary Search Over Chemical Space with Large Language Models.pdf"
---

# Efficient Evolutionary Search Over Chemical Space with Large Language Models

> **저자**: Haorui Wang, Marta Skreta, C. Ser, Wenhao Gao, Lingkai Kong | **날짜**: 2024 | **DOI**: [10.48550/arXiv.2406.16976](https://doi.org/10.48550/arXiv.2406.16976)

---

## Essence

![Figure 1](figures/fig1.webp) *MOLLEO 프레임워크 개요: 초기 분자 풀에서 출발하여 LLM을 교차(crossover) 및 돌연변이(mutation) 연산자로 활용하는 진화 알고리즘*

대규모 언어모델(LLM)을 진화 알고리즘(EA)의 유전 연산자로 통합하여 화학 공간 탐색의 효율성을 획기적으로 향상시키는 MOLLEO 프레임워크를 제안한다. 이는 검은 상자 분자 최적화 문제에서 필요한 목적 함수 평가 횟수를 대폭 감소시킨다.

## Motivation

- **Known**: 진화 알고리즘은 기울기 정보 없이 검은 상자 목적 함수를 최적화할 수 있어 분자 발견에 적합하지만, 무작위 돌연변이와 교차로 인해 수많은 목적 함수 평가가 필요함.

- **Gap**: 기존 EA 기반 분자 최적화는 작업 특화 정보를 활용하지 않아 샘플 효율성이 낮고, LLM 기반 접근법은 순수 프롬프팅에 의존하여 화학적 유효성과 수치 제약 만족도가 떨어짐.

- **Why**: 분자 성질 평가는 실험실 실험이나 계산 시뮬레이션으로 매우 비용이 크므로, 평가 횟수 최소화는 실무 적용의 핵심 요구사항.

- **Approach**: SMILES/SELFIES 표현을 통해 분자를 텍스트로 변환하고, 화학 지식으로 훈련된 LLM(GPT-4, BioT5, MoleculeSTM)을 EA의 유전 연산자로 활용하여 목적에 맞는 분자 제안을 생성.

## Achievement

![Figure 1 (상세)](figures/fig1.webp) *LLM 기반 돌연변이/교차 연산: 텍스트 프롬프트를 통해 목적 함수 정보를 전달하고 개선된 분자 후보 생성*

1. **효율성 개선**: 모든 단일-목적 및 다중-목적 최적화 과제에서 기준 EA, 강화학습(RL), 베이지안 최적화(BO) 방법 대비 우수한 성능 달성. 동일한 평가 예산 내에서 수렴 속도 가속화.

2. **화학적 유효성**: 단순 LLM 기반 분자 생성과 달리, EA 프레임워크와의 통합으로 유효한 SMILES 생성률 증가 및 물리적 접지(physical grounding) 향상.

3. **실무 적용성**: JNK3 억제제 최적화 사례에서 ZINC 250K 데이터베이스의 기존 최고 분자보다 개선된 후보 제시, 신약 발견 시나리오의 실현 가능성 입증.

## How

![Figure 1 (프로세스)](figures/fig1.webp) *반복적 진화: 분자 풀 선택 → LLM 기반 유전 연산 → 오라클 평가 → 풀 업데이트 → 종료 조건까지 반복*

- **문제 정식화**: 검은 상자 단일-목적 최적화 m* = argmax F(m)과 파레토 최적성 기반 다중-목적 최적화 지원.

- **LLM 통합 전략**:
  - 교차 연산(Crossover Mode): 두 부모 분자의 SMILES/SELFIES와 목적 함수 점수를 텍스트 프롬프트로 LLM에 입력하여 특성을 혼합한 자식 분자 생성.
  - 돌연변이 연산(Mutation Mode): 단일 분자와 목표(예: "JNK3 억제 증대")를 프롬프트로 LLM이 구조 개선 제안.

- **하이브리드 아키텍처**: 기존 Graph-GA의 선택 휴리스틱 유지 + LLM 기반 유전 연산으로 샘플 효율성 극대화.

- **다중 LLM 평가**: GPT-4(폐쇄형), BioT5/MoleculeSTM(오픈소스)로 모델 독립성 검증.

## Originality

- **최초 시도**: EA 프레임워크 내 LLM을 유전 연산자로 공식 통합한 첫 연구로, 기존 LLM 분자 편집(molecular editing) 연구와 구별.

- **이중 최적화 관점**: EA의 전역 탐색 능력과 LLM의 화학적 추론 능력을 체계적으로 결합하는 설계 철학.

- **포괄적 검증**: 단일/다중-목적 최적화, 단백질-리간드 도킹(structure-based drug design) 등 다양한 실무 시나리오에서 일관된 개선 입증.

- **절제 연구(Ablation Study)**: 교차/돌연변이 모드 설계 선택의 정당성을 체계적으로 입증.

## Limitation & Further Study

- **LLM 질량 제약**: 초기 LLM 미세조정(fine-tuning) 없이 기본 프롬프팅만 사용하므로, 특정 화학 도메인(예: 극단적 성질 최적화)에서 성능 한계 가능성.

- **계산 비용 불명확**: EA 평가 횟수는 감소하나, LLM 호출 비용(특히 GPT-4)의 실제 경제성 분석 부재.

- **프롬프트 민감성**: 텍스트 프롬프트 설계의 영향 범위와 최적화 전략에 대한 상세 분석 필요.

- **확장성**: 더 큰 분자(>1000원자) 또는 극도로 복잡한 다중-목적 문제로의 확장 가능성 검증 필요.

- **후속 방향**: (1) 화학 특화 LLM의 지속적 미세조정; (2) 강화학습과의 하이브리드 접근; (3) 실제 습식실험 피드백 루프 통합.


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4.5/5
- Significance: 4.5/5
- Clarity: 4/5
- Overall: 4.4/5

**총평**: MOLLEO는 LLM과 EA의 시너지를 체계적으로 입증한 혁신적 연구로, 분자 최적화 분야의 샘플 효율성 문제를 실질적으로 해결하며 ICLR 2025 게재 기준의 높은 수준을 충족한다. 다만 실제 산업 적용을 위한 경제성 분석과 프롬프트 최적화 전략의 심화가 후속 과제로 남아있다.

## Related Papers

- 🔄 다른 접근: [[papers/046_Accurate_structure_prediction_of_biomolecular_interactions_w/review]] — LLM을 활용한 분자 진화 탐색과 확산 모델 기반 생체분자 구조 예측이 각각 서열과 구조 관점에서 분자 설계 문제에 접근한다
- 🔗 후속 연구: [[papers/557_MOOSE-Chem_Large_Language_Models_for_Rediscovering_Unseen_Ch/review]] — LLM 기반 화학 공간 진화 탐색이 미발견 화학 지식 재발견을 위한 더 포괄적인 대형언어모델 시스템으로 확장되었다
- 🔄 다른 접근: [[papers/440_Inverse_designing_metamaterials_with_programmable_nonlinear/review]] — 화학 공간에서 LLM 기반 진화 탐색과 메타물질에서 GNN 기반 역설계가 각각 다른 도메인에서 유사한 최적화 문제를 해결한다
- 🏛 기반 연구: [[papers/214_ChemToolAgent_The_Impact_of_Tools_on_Language_Agents_for_Che/review]] — LLM 기반 분자 최적화 연구가 화학 도구를 활용하는 언어 에이전트의 분자 설계 능력에 중요한 방법론적 기반을 제공한다
- 🧪 응용 사례: [[papers/749_Sequence_modeling_and_design_from_molecular_to_genome_scale/review]] — 진화적 탐색 방법론이 게놈 설계와 생성에 실제 적용됨
- 🔄 다른 접근: [[papers/046_Accurate_structure_prediction_of_biomolecular_interactions_w/review]] — 확산 기반 생체분자 구조 예측과 LLM 기반 화학 공간 탐색이 각각 구조와 서열 관점에서 분자 설계 문제에 접근한다
- 🔄 다른 접근: [[papers/440_Inverse_designing_metamaterials_with_programmable_nonlinear/review]] — 메타물질 역설계를 위한 GNN-RL 접근법과 화학 공간 탐색을 위한 LLM 기반 진화 알고리즘이 각각 다른 도메인에서 유사한 역설계 문제를 해결한다
- 🧪 응용 사례: [[papers/469_Large_Language_Models_as_Evolutionary_Optimizers/review]] — 대형 언어 모델을 활용한 화학 공간 진화 탐색이 LLM 기반 진화 최적화의 실제 적용 사례입니다.
- 🔗 후속 연구: [[papers/472_Large_language_models_design_sequence-defined_macromolecules/review]] — 화학 공간에서의 효율적인 진화 탐색 기법을 거대분자 설계에 확장 적용할 수 있다.
