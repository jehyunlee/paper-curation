---
title: "390_Grammars_of_formal_uncertainty_When_to_trust_llms_in_automat"
authors:
  - "Debargha Ganguly"
  - "Vikash Singh"
  - "Sreehari Sankar"
  - "B. X. Zhang"
  - "Xuecen Zhang"
date: "2025"
doi: "미제공"
arxiv: ""
score: 4.2
essence: "LLM의 본질적인 확률성(probabilistic nature)과 형식검증의 결정론적 요구(deterministic guarantees) 사이의 근본적 긴장을 해소하기 위해, 확률문맥자유문법(PCFG, Probabilistic Context-Free Grammar) 기반 프레임워크를 도입하여 LLM 생성 SMT-LIB 프로그램의 불확실성을 체계적으로 정량화하고, 이를 통해 선택적 검증(selective verification)으로 14-100% 오류율을 감소시킨다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/Multi-Agent_Language_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Ganguly et al._2025_Grammars of formal uncertainty When to trust llms in automated reasoning tasks.pdf"
---

# Grammars of formal uncertainty: When to trust llms in automated reasoning tasks

> **저자**: Debargha Ganguly, Vikash Singh, Sreehari Sankar, B. X. Zhang, Xuecen Zhang, Srinivasan Iyengar, Xiaotian Han, Amit Sharma, Shivkumar Kalyanaraman, Vipin Chaudhary | **날짜**: 2025 | **DOI**: [미제공](https://arxiv.org/abs/2505.20047)

---

## Essence

LLM의 본질적인 확률성(probabilistic nature)과 형식검증의 결정론적 요구(deterministic guarantees) 사이의 근본적 긴장을 해소하기 위해, 확률문맥자유문법(PCFG, Probabilistic Context-Free Grammar) 기반 프레임워크를 도입하여 LLM 생성 SMT-LIB 프로그램의 불확실성을 체계적으로 정량화하고, 이를 통해 선택적 검증(selective verification)으로 14-100% 오류율을 감소시킨다.

## Motivation

- **Known**: LLM은 형식명세(formal artifacts) 생성에 뛰어난 성능을 보이며, 형식방법의 대중화 가능성을 제시함. 기존 불확실성 정량화(UQ) 기법으로는 토큰 확률의 엔트로피 등이 존재.

- **Gap**: LLM은 본질적으로 확률적이나 형식검증은 결정론적 보증을 요구하는 근본적 인식론적 간극(epistemological gap)이 존재. SMT 기반 자동형식화(autoformalization)의 효과가 작업별로 극단적으로 다르며(+34.8% from -44.5%), 기존 UQ 기법들이 형식산출물의 오류를 식별하지 못함.

- **Why**: 형식검증이 안전-임계 시스템으로 제한되는 핵심 이유는 전문성 필요 및 노동 비용. LLM의 불확실성을 신뢰할 수 있는 방식으로 활용하면 형식방법을 민주화할 수 있음.

- **Approach**: LLM 출력의 확률분포를 PCFG로 모델링하고, 이로부터 도출된 25개 불확실성 메트릭을 작업별로 융합하여 선택적 검증을 수행.

## Achievement

![Figure 1: LLM 생성 SMT-LIB 형식화의 실증 분석 - 실제 출력, PCFG 규칙 빈도, 계산된 확률분포](https://arxiv.org/html/2505.20047v1/x1.png)
*그림 1: '수학이나 물리를 공부하고 열심히 일하는 모든 사람은 성공할 것이다'라는 명제에 대한 LLM 생성 논리적 변형, 측정된 PCFG 규칙 빈도, 계산된 확률분포. 실제 데이터 사용, 합성 데이터 없음.*

1. **실증적 실패모드 분석**: 5개 최신 LLM을 4개 형식추론 데이터셋으로 평가하여 SMT 기반 자동형식화의 도메인 특이성을 정량화. ProofWriter에서 +34.8% 정확도 향상, FOLIO에서 -44.5% 저하. 기존 UQ 기법(토큰 확률 엔트로피)이 이러한 오류를 포착하지 못함을 증명.

2. **PCFG 기반 확률 프레임워크**: 측정 가능한 확률공간(Σ*, F)을 정의하고, LLM이 유도하는 확률측도(probability measure) µ_{T,θ,SMT}를 SMT-LIB v2 문법 기반 PCFG로 근사. 최대우도추정(MLE)과 Lidstone 평활화(smoothing)를 통해 규칙 확률을 추정하며, 커버리지 보증 정리(Coverage Guarantee Theorem 1)로 샘플 크기의 필요성을 이론화.

3. **세분화된 불확실성 분류법**: 기존 epistemic/aleatoric 이분법을 넘어 4개 범주(epistemic-knowledge, epistemic-procedural, recursive-complexity, capacity-limited)로 확장한 정제된 분류체계 제시. 25개 메트릭 개발 및 평가 완료.

4. **작업 종속적 신호 식별 및 선택적 검증**: 불확실성 신호가 작업에 따라 달라짐을 입증 (예: 논리 작업에서 문법 엔트로피 AUROC > 0.93). 경량의 모델-불가지론적(model-agnostic) 신호 융합으로 개별 메트릭 성능 초과. 최소 기각(minimal abstention)으로 오류율 14-100% 감소.

## How

![Figure 2-5: 온도 변수에 따른 메트릭 변화 - 스펙트럼 반경, 문법 엔트로피, KLD, 엔트로피 비율](https://arxiv.org/html/2505.20047v1/figures.png)

### 이론적 기초
- **확률공간 정형화**: 문자 집합 Σ에 대해 모든 유한 문자열의 집합 Σ*을 측정가능 공간 (Σ*, F)으로 정의 (F는 실린더 집합 σ-대수)
- **LLM 확률측도**: 작업 T와 파라미터 θ에 대해 LLM이 유도하는 조건부 측도 µ_{T,θ,SMT} = µ_{T,θ}(A∩L_{SMT})/µ_{T,θ}(L_{SMT}) 정의

### PCFG 근사 방법
- **샘플 수집**: 목표 LLM에서 N개의 SMT-LIB 프로그램 샘플 P_N = {P₁, ..., P_N} 생성
- **구문분석**: SMT-LIB v2 문법 G_{SMT}으로 각 프로그램 구문분석, 적용된 규칙(production rules) 기록
- **MLE 추정**: 규칙 r = (A → β)의 상대빈도 p̂_MLE(r) = C(r)/C(A)로 계산 (C(r): 규칙 적용 횟수, C(A): LHS 비단말 총 적용 횟수)
- **평활화**: Lidstone 평활화 p̂^(β_s)_N(r) = (C(r) + β_s)/(C(A) + β_s|R_A|)로 영(zero) 카운트 처리

### 메트릭 도출 (정적/동적)
- **정적 메트릭**: 비단말 개수 |V_{SMT}|, 규칙 개수 |R_{SMT}|, 비단말당 평균 규칙, 최대 분기 인수(branching factor), 재귀 유형 감지
- **스펙트럼 성질**: 평균 행렬 B의 스펙트럼 반경 ρ(B) = max{|λ| | det(B - λI) = 0} (ρ < 1: 유한 유도 길이, ρ ≥ 1: 구조 복잡도 높음)
- **정보이론 메트릭**: 비단말별 Shannon 엔트로피 H(A) = -∑_{A→β∈R_A} p(A→β)log₂p(A→β), 문법 전체 엔트로피, KL 발산(KLD), 엔트로피 비율

### 선택적 검증 파이프라인
- 다중 불확실성 신호의 경량 융합(lightweight fusion)
- 임계값(threshold) 기반 신뢰도 추정 및 검증 대상 선택
- 형식 검증 엔진(SMT solver) 호출 최소화로 계산 효율성 확보

## Originality

- **뉴로-심볼 시스템의 인식론적 갭 해결**: LLM의 확률성과 형식방법의 결정론적 요구를 PCFG 기반 수학 프레임워크로 연결한 첫 시도

- **구조화된 불확실성 정량화**: 단순 토큰 확률 엔트로피 대신 문맥자유문법 규칙 수준의 확률 분포를 체계적으로 모델링

- **세분화된 분류체계**: epistemic-knowledge, epistemic-procedural, recursive-complexity, capacity-limited 4개 범주로 기존 이분법 확장

- **작업별 메트릭 최적성 발견**: 동일한 메트릭이 작업마다 다른 성능을 보이며, 작업 인식형 신호 융합의 필요성을 실증적으로 입증

- **카버리지 보증 이론**: 샘플링 기반 근사의 이론적 신뢰성을 정식화 (Theorem 1: 실패 확률의 상한 도출)

## Limitation & Further Study

- **PCFG 근사의 한계**: 실제 LLM 분포 µ_{T,θ,SMT}와 PCFG 모델 µ_G의 괴리. KL 발산 최소화 보증 있으나, 문맥 의존성(context-dependency) 미포함 (Neural PCFG로 일부 완화 제시)

- **샘플 크기 의존성**: 신뢰할 수 있는 PCFG 파라미터 추정에 필요한 최소 샘플 수 N에 대한 명시적 지침 부재. Coverage Guarantee는 상한만 제공.

- **평가 범위 제한**: 4개 형식추론 데이터셋과 5개 LLM으로 평가했으나, 더 다양한 도메인(기하, 프로그램 검증 등)과 최신 모델(GPT-4o, Claude 3.5 등) 포함 필요

- **선택적 검증의 실제 비용 미계산**: 기각 시 인간 검토 또는 대체 방법의 실제 비용 분석 부재. 오류 감소의 trade-off 정량화 부족

- **후속 연구 방향**:
  - Neural PCFG 기반 문맥 의존 모델로 근사 정확도 향상
  - 다중 LLM 앙상블에서의 신호 융합 최적화
  - 형식증명(formal proofs), 프로그램 합성 등 다른 형식산출물로 확장
  - 모달리티 인식 아키텍처(modality-aware architectures) 설계로 신뢰성 강화

## Evaluation

| 항목 | 점수 | 근거 |
|------|------|------|
| **Novelty** | 4.5/5 | PCFG 기반 LLM 분포 모델링 및 세분화된 불확실성 분류는 독창적. 다만, PCFG 자체는 확립된 기법이므로 적용의 창의성 중심 |
| **Technical Soundness** | 4/5 | 측도론적 정형화, MLE 수렴성, Coverage Guarantee 정리 등 수학적 기초 견고. 그러나 신경 PCFG는 간단히 언급만 되고, 실증적 검증 부족. 스펙트럼 반경과 PCFG 추정의 연결 고리 약화 가능 |
| **Significance** | 4.5/5 | 형식방법의 실용화를 위한 신뢰성 문제 해결에 직접 기여. 25개 메트릭, 작업 종속성 발견, 선택적 검증으로 오류 14-100% 감소는 실무적 영향 크다. 다만 평가 범위의 제한성 고려 |
| **Clarity** | 3.5/5 | 이론 부분은 엄밀하나 복잡. 메인 메시지(PCFG가 언제 어떻게 도움이 되는지)가 다수 메트릭과 분류법에 묻힘. 선택적 검증 파이프라인 설명 부족 |
| **Overall** | 4.2/5 | 강점: 근본적 인식론적 문제에 대한 수학적 솔루션, 실증적 다층 평가, 실용적 성과(오류 감소). 약점: PCFG 근사 한계에 대한 충분한 분석 부족, 선택적 검증의 실제 cost-benefit 분석 미흡, 기술 설명의 명확성 개선 필요 |

**총평**: 

LLM과 형식검증 간의 근본적 긴장을 PCFG 프레임워크로 우아하게 해결하고, 작업별

## Related Papers

- 🔄 다른 접근: [[papers/674_ReTool_Reinforcement_Learning_for_Strategic_Tool_Use_in_LLMs/review]] — 확률문맥자유문법 기반 불확실성 정량화와 강화학습 기반 전략적 도구 사용은 LLM의 신뢰성 문제를 서로 다른 방식으로 해결하는 접근이다.
- 🔗 후속 연구: [[papers/846_TrustLLM_Trustworthiness_in_Large_Language_Models/review]] — 대규모 언어 모델의 신뢰성 종합 평가가 형식 검증에서의 불확실성 정량화를 더 광범위한 신뢰성 차원으로 확장한 연구이다.
- ⚖️ 반론/비판: [[papers/471_Large_Language_Models_Cannot_Self-Correct_Reasoning_Yet/review]] — LLM의 자기 수정 추론 한계 연구가 확률적 언어 모델의 결정론적 보장 제공 가능성에 대한 반대 관점을 제시한다.
- 🔄 다른 접근: [[papers/674_ReTool_Reinforcement_Learning_for_Strategic_Tool_Use_in_LLMs/review]] — ReTool의 강화학습 기반 전략적 도구 사용과 확률문맥자유문법 기반 불확실성 정량화는 LLM 신뢰성을 서로 다른 방식으로 개선하는 접근이다.
