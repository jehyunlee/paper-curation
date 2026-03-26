# Agentic Personas for Adaptive Scientific Explanations with Knowledge Graphs

> **저자**: Susana Nunes, Tiago Guerreiro, Catia Pesquita | **날짜**: 2026-03-23 | **arXiv**: 2603.21846

---

## Essence

Knowledge graph 기반 설명 생성에서 전문가의 다양한 인식론적 입장(epistemic stance)을 반영하는 적응형 설명(adaptive explanation) 프레임워크를 제안한 연구이다. "Agentic persona"라는 개념을 도입하여, 전문가 피드백으로부터 클러스터링과 LLM 합성을 통해 해석 전략의 구조적 표현을 만들고, 이를 강화학습의 보상 함수에 통합하여 사용자별 맞춤형 KG 경로 설명을 생성한다. Drug discovery 도메인에서 22명 대상 사용자 연구 결과, persona 기반 적응형 설명이 비적응형 baseline 대비 63.3-76.0% 선호되었다.

## Motivation

- **알려진 것**: Knowledge graph 기반 설명은 path-based reasoning을 통해 해석 가능한 AI 설명을 제공할 수 있으며, REx 등의 방법이 fidelity와 relevance를 동시에 최적화
- **Gap**: 기존 XAI 시스템은 정적(static) 사용자 모델을 가정하여, 같은 분야 전문가라도 서로 다른 인지 전략과 인식론적 입장을 가진다는 사실을 반영하지 못함. 개별 전문가 프로파일링은 전문가 희소성으로 인해 비실용적
- **왜 중요한가**: 과학적 발견, 신약 개발 등 고위험 도메인에서 AI 설명이 전문가의 실제 추론 방식에 맞지 않으면 신뢰와 의사결정 품질이 저하됨
- **접근법**: 전문가 피드백을 Sentence-BERT로 임베딩하고 클러스터링하여 epistemic stance를 발견한 후, LLM으로 내러티브 persona를 합성하고 이를 RL reward에 통합

## Achievement

1. **Persona 신뢰도**: 두 persona(Elena, Leo)의 평가 점수가 실제 전문가 평가와 높은 상관관계 (Pearson r = 0.56-0.91, 모두 p < .001)
2. **사용자 선호**: 22명 대상 연구에서 적응형 설명이 비적응형 대비 63.3%(Leo, p = .005) 및 76.0%(Elena, p < .001) 선호
3. **평가 지표 향상**: Relevance(Leo 4.02 vs. REx 3.44), Validity(Leo 4.06 vs. REx 3.50), Completeness(Elena 3.88 vs. REx 3.45) 전반적 개선
4. **예측 성능 유지**: Drug repurposing에서 Hits@1 0.358, MRR 0.438로 기존 SOTA(REx: 0.338, 0.427) 대비 오히려 향상
5. **확장성**: Persona 기반 피드백이 전문가 직접 피드백 대비 187배 빠르며 (1.34시간 vs. 250시간), 단일 평가 기준 86배 속도 향상

## How

- **데이터**: Hetionet (이종 생의학 knowledge graph), 11명 전문가의 40개 설명 평가 (DR 및 DTI 태스크)
- **Phase I - Persona 생성**: (1) 전문가 피드백을 Sentence-BERT (all-mpnet-base-v2)로 768차원 임베딩 (2) K-Means, Agglomerative, HDBSCAN 3가지 클러스터링으로 k=2 최적 발견 (3) OpenAI o3-pro로 클러스터별 내러티브 persona 합성 (Elena: 기계론적 엄밀성, Leo: 간결한 명확성)
- **Phase II - 적응형 설명**: REx 프레임워크 기반 RL에서 persona-conditioned reward 도입. GPT-4o-mini가 persona 역할로 각 경로를 validity, completeness, relevance로 평가. Curriculum learning으로 relevance threshold를 점진적으로 높여 학습 효율화
- **보상 함수**: R(p, t) = alpha(p) * R_persona(p) (높은 relevance 경로), 중간/낮은 relevance에는 고정 보상(0.25, 0.10) 부여
- **평가**: 22명 신규 참여자 대상, 3개 프로파일링 질문으로 persona 배정 후 10개 가설 x 2개 설명 비교 평가

## Originality

- **Agentic Persona 개념**: 전문가의 인구통계적 속성이 아닌 "인식론적 입장"을 클러스터링하여 구조화된 해석 전략 표현을 만드는 최초의 시도. 기존 persona 기반 접근이 role-based 단순화에 머물렀던 것을 극복
- **RLHF의 XAI 적용**: LLM persona를 reward model로 사용하여 KG path selection을 조건화하는 방식은, human feedback의 확장성 문제를 해결하는 새로운 패러다임
- **Curriculum Learning 통합**: Fidelity → relevance → persona alignment 순으로 점진적 학습 난이도를 높이는 self-paced curriculum을 설명 생성 RL에 적용

## Limitation & Further Study

### 저자들이 언급한 한계

- Drug discovery 도메인에서만 검증되어, 법률, 교육, 기후 모델링 등 다른 도메인으로의 일반화 필요
- Leo persona가 단 2명의 전문가 피드백에서 도출되어 대표성에 한계 (ICC 분석에서 Leo 조건의 inter-annotator agreement가 poor)

### 자체판단 아쉬운 점

- 11명이라는 극히 제한된 초기 전문가 풀에서 2개 클러스터만 발견한 것이 실제 전문가 해석 다양성을 충분히 포착하는지 의문. 더 큰 표본에서는 더 세분화된 epistemic stance가 존재할 가능성
- Persona의 LLM 평가(GPT-4o-mini)와 실제 전문가 평가 간의 alignment이 태스크(DR vs DTI)에 따라 크게 변동 (Elena DTI validity r=0.56). LLM evaluator의 도메인 특이적 한계가 충분히 분석되지 않음
- 3개 단순 질문으로 사용자를 persona에 배정하는 방식이 실제 epistemic stance의 복잡성을 포착하기에 너무 단순할 수 있음
- Persona 생성에 사용된 LLM(o3-pro)과 평가에 사용된 LLM(GPT-4o-mini)이 다른데, 이 불일치가 결과에 미치는 영향이 분석되지 않음
- KG 설명의 텍스트 verbalization도 GPT-4o-mini가 수행하므로, persona alignment 향상이 설명 경로 자체의 개선인지 verbalization의 개선인지 분리가 어려움

### 후속 연구

- 더 다양한 도메인(법률 추론, 교육 평가, 기후 모델링)에서의 적응형 설명 검증
- Persona 수 확장 및 동적 persona 전환 메커니즘 개발
- Real-time 상호작용을 통한 persona 정제 및 개인화 심화

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 4/5 |
| Technical Soundness | 3/5 |
| Significance | 3/5 |
| Clarity | 4/5 |
| Overall | 3/5 |

**총평**: XAI에서 전문가의 인식론적 다양성을 포착하여 맞춤형 설명을 생성한다는 개념적 기여가 인상적이다. 그러나 11명의 극소 표본에서 도출한 2개 persona의 대표성, LLM evaluator의 태스크 의존적 변동성, 그리고 verbalization과 경로 선택의 효과 분리 부재 등 방법론적 한계가 있다. Drug discovery라는 특정 도메인에서의 초기 검증으로서 가치가 있으나, 확장성과 일반화에 대한 더 엄밀한 검증이 필요하다.
