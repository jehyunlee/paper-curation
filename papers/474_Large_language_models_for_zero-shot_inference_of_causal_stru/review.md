---
title: "474_Large_language_models_for_zero-shot_inference_of_causal_stru"
authors:
  - "Izzy Newsham"
  - "Luka Kovačević"
  - "Richard Moulange"
  - "Nan Rosemary Ke"
  - "Sach Mukherjee"
date: "2025"
doi: "N/A"
arxiv: ""
score: 4.0
essence: "대규모 언어모델(LLM)이 생물학적 인과관계를 문헌 지식만으로 추론할 수 있는지를 실제 유전자 섭동 실험 데이터로 검증하는 혁신적 평가 프레임워크를 제시한다. 적절한 프롬프팅과 정보 증강 전략을 통해 작은 LLM도 생물학적 시스템의 의미 있는 인과구조를 포착할 수 있음을 보여준다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/Biomedical_Causal_Modeling"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Newsham et al._2025_Large language models for zero-shot inference of causal structures in biology.pdf"
---

# Large language models for zero-shot inference of causal structures in biology

> **저자**: Izzy Newsham, Luka Kovačević, Richard Moulange, Nan Rosemary Ke, Sach Mukherjee | **날짜**: 2025 | **DOI**: N/A

---

## Essence

대규모 언어모델(LLM)이 생물학적 인과관계를 문헌 지식만으로 추론할 수 있는지를 실제 유전자 섭동 실험 데이터로 검증하는 혁신적 평가 프레임워크를 제시한다. 적절한 프롬프팅과 정보 증강 전략을 통해 작은 LLM도 생물학적 시스템의 의미 있는 인과구조를 포착할 수 있음을 보여준다.

## Motivation

- **Known**: LLM이 단순 구조화된 문장에서 인과관계를 추출할 수 있으며, 생화학 분야에서 실험 오케스트레이션 도구로 활용되고 있음
- **Gap**: 과학 문헌의 복잡성, 노이즈, 모순을 포함하는 실제 환경에서 LLM이 생물학적 인과관계를 정확히 추론할 수 있는지 체계적으로 평가한 연구 부재
- **Why**: 질병 생물학의 분자 네트워크 메커니즘을 규명하고 대규모 실험 탐색 공간을 효율적으로 축소하기 위해 LLM의 인과추론 능력 검증이 필수적
- **Approach**: Perturb-seq 유전자 섭동 실험 데이터로부터 인과 ground truth를 구축하고, 이를 LLM의 문헌 기반 예측과 비교하는 벤치마킹 프레임워크 개발

## Achievement

![Figure 1: Directed edges are drawn between the perturbed gene k and the set of genes ∆k = {i,..., j} that change significantly under experimental intervention on k.](figures/fig1.webp)
*그림 1: 섭동된 유전자 k와 k에 대한 실험적 중재 하에서 유의하게 변하는 유전자 집합 간의 방향성 모서리*

1. **포괄적 벤치마킹 프레임워크**: 100개 이상의 변수와 수천 개의 인과 가설에 대해 LLM의 인과관계 추론 능력을 실제 개입 데이터(interventional data)로 검증하는 체계적 방법론 개발

2. **전략적 증강의 효과**: 검색 증강(retrieval-augmentation)과 맞춤형 프롬프팅을 통해 상대적으로 작은 LLM도 생물학적 시스템의 의미 있는 인과구조를 포착 가능함을 실증

3. **지식 기반 방법과의 비교**: STRING 데이터베이스 같은 전통적 구조화된 지식 기반 방법과의 비교를 통해 LLM의 추론 능력의 상대적 장단점 명확화

## How

![Figure 2: Outputs for inferring causal direction with different prompt contexts, for the example gene](figures/fig2.webp)
*그림 2: 예시 유전자에 대해 다양한 프롬프트 맥락에서 인과방향 추론 결과*

### 인과 Ground Truth 구축
- **Mann-Whitney U 검정** 활용: 각 유전자 k 섭동 시 target 유전자 j의 발현 분포 변화를 통계적으로 검정 (H₀: 동일 분포 vs H₁: 다른 분포)
- **Benjamini-Hochberg 보정**: 다중 검정 문제 해결 및 FDR 제어 (α=0.05)
- **조상 그래프(ancestral graph) 생성**: 각 섭동 유전자에서 유의하게 변한 유전자들로의 방향성 모서리 도출 (직접/간접 인과효과 모두 포함)

### LLM 프롬프팅 전략
- **확률 기반 쿼리**: "유전자 i가 유전자 j에 미치는 인과효과의 정도를 0과 1 사이의 확률로 정량화하세요"
- **모든 유전자 쌍에 대한 반복**: d개 유전자의 모든 쌍에 대해 프롬프팅하여 d×d 확률 행렬 P 생성
- **재인스턴시에이션(reinstatiation)**: 각 프롬프트 후 편향 방지를 위해 LLM 재설정

### 평가 메트릭
- **AUROC (Area Under ROC Curve)**: 확률 행렬의 비대각 원소와 ground truth 인접 행렬 비교
- **임계값 기반 그래프 생성**: 확률 행렬을 임계값 γ로 이진 그래프 변환
- **추이적 폐포(transitive closure) 분석**: 직접 인과관계뿐 아니라 간접 경로까지 고려

![Figure 3: Gemma2의 다양한 유전자별 문맥 정보 정도에 따른 결과](figures/fig3.webp)
*그림 3: 유전자 수준의 맥락 정보 제공 수준에 따른 LLM 성능 변화*

### 검색 증강 전략
- **생물학적 맥락 명시**: 실험 조건, 세포 유형, 후성유전학적 배경 정보 포함
- **PubTator 3.0 활용**: 과학 문헌에서 생물개체명 인식 및 추출
- **STRING 데이터베이스 통합**: 알려진 단백질-단백질 상호작용 정보 활용
- **노드별 세부 정보 제공**: 구체적 유전자에 대한 선택적 정보 추가

## Originality

- **인과 추론의 실험적 검증**: 대부분의 선행 연구는 구조화된 짧은 문장에서만 LLM의 인과추론을 평가했으나, 본 연구는 실제 과학 문헌의 복잡성과 실험 데이터의 지면(gold standard)을 결합한 최초의 체계적 평가

- **대규모 생물학적 데이터셋 활용**: 100+ 변수, 수천 개의 인과 가설로 구성된 규모 있는 벤치마크로 일반화 가능성 향상

- **다층적 프롬프팅 및 증강 전략 탐색**: 단순 프롬프팅을 넘어 생물학적 맥락, 유전자 수준 정보, 문헌 검색 등을 통합하는 포괄적 프레임워크 제시

- **실제 과학 워크플로우 모방**: 개입 실험(interventional experiment)을 통한 ground truth 구축으로 현실의 과학적 발견 프로세스와 부합하는 평가 방식 개발

## Limitation & Further Study

- **맥락 특이성(context-specificity)**: 세포 유형, 질병 상태, 환경 조건 등 다양한 생물학적 맥락에서 LLM의 성능 변화를 더 상세히 분석 필요

- **직접 vs 간접 인과관계 구분**: 현재 프레임워크는 조상 그래프(ancestral graph)로 직접/간접 모두를 포함하는데, 직접 인과관계만 정확히 구분하는 방법론 개발 필요

- **문헌의 노이즈와 모순 처리**: 과학 문헌의 상충하는 주장이나 잘못된 정보가 LLM 성능에 미치는 영향에 대한 심층 분석 부족

- **작은 LLM과 대규모 모델의 확장성**: 어느 규모 이상의 LLM에서 성능이 포화되는지, 미세조정(fine-tuning)이 실제로 도움이 되는지 검증 필요

- **시간적 동역학과 인과성**: 현재 static 네트워크에 집중하나, 시간적 의존성을 포함한 동적 인과관계 추론으로 확장 가능성

- **다중 유전자 섭동**: 현재는 단일 유전자 섭동만 고려하나, 조합 섭동(combinatorial perturbations) 실험과의 비교 추가

## Evaluation

- **Novelty**: 4.5/5 - 실제 개입 실험 데이터로 LLM의 인과추론을 평가하는 접근이 신선하고, 생물학과 인과추론, LLM을 포괄적으로 결합한 점이 주목할 만함

- **Technical Soundness**: 4/5 - Mann-Whitney U 검정, FDR 보정, AUROC 평가 등 통계학적 방법론이 견고하나, 재현성을 위한 세부 하이퍼파라미터나 데이터셋 접근성 명시 부족

- **Significance**: 4/5 - LLM을 과학 발견의 오케스트레이션 도구로 위치시키는 실용적 기여가 크며, 향후 인과 발견 연구에 벤치마크로 활용될 잠재력이 높음

- **Clarity**: 3.5/5 - 전반적으로 명확하나, 다양한 프롬프팅 전략과 검색 증강 방법이 상세히 기술되지 않아 재현에 어려움이 있을 수 있음. Figure 2와 3의 결과 해석이 본문에서 충분히 설명되지 않음

- **Overall**: 4/5

**총평**: 본 논문은 LLM이 과학 발견 도구로서 실제 가치를 갖는지를 검증하는 중요한 첫 걸음으로, 실험 데이터 기반 평가 프레임워크를 통해 학술적·실용적 기여를 모두 제시하나, 결과 분석의 심화와 재현성 강화가 필요하다.

## Related Papers

- 🔗 후속 연구: [[papers/505_Llm4grn_Discovering_causal_gene_regulatory_networks_with_llm/review]] — 유전자 조절 네트워크 발견을 위한 LLM 활용 연구로, 생물학적 인과관계 추론의 구체적 적용 사례이다.
- 🧪 응용 사례: [[papers/615_PerTurboAgent_A_Self-Planning_Agent_for_Boosting_Sequential/review]] — 유전자 섭동 실험 설계에 인과관계 추론 능력을 활용하여 더 효과적인 실험 계획을 수립할 수 있다.
- 🏛 기반 연구: [[papers/331_Exploring_collaboration_mechanisms_for_llm_agents_A_social_p/review]] — 프로그램 가이드 추론을 통한 복잡한 주장 검증 방법론이 생물학적 인과관계 추론의 기술적 기반이 된다.
- 🔗 후속 연구: [[papers/459_Language_Models_for_Controllable_DNA_Sequence_Design/review]] — 생물학적 인과관계 추론 능력을 DNA 서열의 기능적 특성 예측과 설계에 활용할 수 있다.
- 🏛 기반 연구: [[papers/505_Llm4grn_Discovering_causal_gene_regulatory_networks_with_llm/review]] — 생물학적 인과관계 추론의 일반적 프레임워크를 유전자 조절 네트워크 발견이라는 구체적 문제에 적용한다.
- 🧪 응용 사례: [[papers/615_PerTurboAgent_A_Self-Planning_Agent_for_Boosting_Sequential/review]] — 생물학적 인과관계 추론 능력을 유전자 섭동 실험의 순차적 선택 최적화에 활용할 수 있다.
