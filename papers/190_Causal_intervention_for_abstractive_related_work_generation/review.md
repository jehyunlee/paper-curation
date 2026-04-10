---
title: "190_Causal_intervention_for_abstractive_related_work_generation"
authors:
  - "Jiachang Liu"
  - "Qi Zhang"
  - "Chongyang Shi"
  - "Usman Naseem"
  - "Shoujin Wang"
date: "2023"
doi: "N/A"
arxiv: ""
score: 4.0
essence: "본 논문은 학술 논문의 관련 업무(Related Work) 섹션을 자동으로 생성하는 과정에서 인과 관계 이론을 도입하여, 문장 순서와 같은 허위 상관관계(spurious correlation)를 제거하고 문서 간 실제 의미 관계에 기반한 고품질 요약을 생성한다."
tags:
  - "cat/Academic_Peer_Review_Automation"
  - "sub/Expert_Review_Automation"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Liu et al._2023_Causal intervention for abstractive related work generation.pdf"
---

# Causal intervention for abstractive related work generation

> **저자**: Jiachang Liu, Qi Zhang, Chongyang Shi, Usman Naseem, Shoujin Wang, Liang Hu, Ivor W. Tsang | **날짜**: 2023 | **DOI**: N/A

---

## Essence

![Figure 2](figures/fig2.webp) *관련 업무 생성을 위한 인과 그래프. do-calculus를 적용하여 경로 c→x를 차단하고 허위 상관관계 c→x→y의 영향을 완화*

본 논문은 학술 논문의 관련 업무(Related Work) 섹션을 자동으로 생성하는 과정에서 인과 관계 이론을 도입하여, 문장 순서와 같은 허위 상관관계(spurious correlation)를 제거하고 문서 간 실제 의미 관계에 기반한 고품질 요약을 생성한다.

## Motivation

- **Known**: 기존 추상화 기반 관련 업무 생성 모델들은 참고문헌의 추상(abstract)을 입력받아 coherent한 관련 업무 섹션을 생성함. 다양한 인코딩 전략과 외부 지식을 활용하여 성능을 개선해왔음.

- **Gap**: 기존 모델들은 고빈도 단어/문구 패턴이나 글쓰기 습관처럼 표면적인 허위 상관관계를 학습하는 경향이 있음. 이는 학습 데이터와 테스트 데이터 간 분포 변화(distribution shift)에서 모델의 일반화 능력을 크게 저하시킴.

- **Why**: 문장 순서(c)는 문서 간 실제 관계(x)와 무관하게 전이 표현(y)에 직접 영향을 미칠 수 있음. 딥러닝 모델은 접근이 쉬운 문장 순서 정보를 우선학습하여 경로 c→x→y의 허위 상관관계에 의존하게 됨.

- **Approach**: 인과 그래프 모델링을 통해 허위 상관관계를 식별하고, do-calculus와 백도어 기준(backdoor criterion)을 활용한 인과 개입(causal intervention)으로 경로 c→x를 차단. 이를 통해 실제 인과관계 x→y에 기반한 생성을 유도.

## Achievement

![Figure 3](figures/fig3.webp) *디코더에 통합된 CaM의 구조. 세 가지 구성 요소: Primitive Intervention, Context-aware Remapping, Optimal Intensity Learning*

1. **첫 시도**: 관련 업무 생성 과제에 인과 이론을 처음 도입. 기존 연구들이 간과했던 인과관계의 중요성을 체계적으로 다룸.

2. **새로운 모듈 제안**: CaM(Causal Intervention Module for Related Work Generation)을 제안하여 Transformer와 end-to-end로 통합. Primitive Intervention, Context-aware Remapping, Optimal Intensity Learning의 세 부분으로 구성.

3. **실험 성능**: S2ORC와 Delve 두 개의 실제 데이터셋에서 기존 최신 모델들을 능가하는 성능 달성. 인과 개입의 효과성 및 관련 업무 생성에 인과 이론 도입의 정당성 입증.

## How

![Figure 1](figures/fig1.webp) *관련 업무 생성에서 인과관계(실선 화살표)와 허위 상관관계(점선 화살표)의 효과 차이 설명*

- **Causal Graph Modeling**: 문장 순서(c), 문서 관계(x), 전이 표현(y) 간의 관계를 인과 그래프로 모델링. 문장 순서는 전이 표현에 직접 영향을 미치면서 동시에 문서 관계에 간접 영향을 미치는 교란 변수(confounder)로 작동.

- **Primitive Intervention**: do-calculus 및 백도어 기준을 적용하여 식 (1) p(y|do(x)) = Σ_c p(y|x,c)p(c)를 유도. 순서 정보를 임베딩에 통합하고(식 2), 문장 위치 확률을 예측한 후(식 3), 순서 강화 임베딩과 위치 확률의 가중 합으로 개입된 임베딩 계산(식 4).

- **Context-aware Remapping**: 개입된 임베딩과 원본 임베딩 간의 매핑 공간 불일치 문제와 개별 단어 개입으로 인한 문맥 손상을 해결. 고정 크기의 문맥 윈도우를 사용하여 스캔하고 필요한 정보를 재매핑.

- **Optimal Intensity Learning**: 전체 인과 개입의 최적 강도를 학습. 다양한 부분의 출력을 제어하여 모델이 개입의 강도를 동적으로 조절할 수 있도록 함.

- **Integration with Transformer**: CaM을 Transformer 디코더에 전략적으로 통합하여 개입된 정보가 전체 생성 과정에 전파될 수 있도록 설계.

## Originality

- 관련 업무 생성 분야에서 인과 이론 적용의 선도적 시도로, 기존 연구들이 간과했던 허위 상관관계 문제를 체계적으로 분석하고 해결.

- 추상화 기반 생성 모델에 do-calculus와 백도어 기준을 적용한 새로운 인과 개입 방식의 제안.

- 개입된 임베딩의 문맥 정보 손상 문제를 해결하기 위한 Context-aware Remapping 메커니즘은 인과 개입 이후의 실질적 문제 해결에 기여.

- 모듈식 설계로 Transformer 기반 다양한 생성 모델에 적용 가능한 확장성 제시.

## Limitation & Further Study

- **제한점**: 
  - 인과 그래프에서 고려하는 변수가 3개(문장 순서, 문서 관계, 전이 표현)로 제한되어 있으며, 더 복잡한 인과 관계 구조는 모델링하지 않음.
  - 문장 시작 단어에만 개입을 적용하는 휴리스틱 방식이 모든 생성 단계를 포괄하지 못할 가능성.
  - 실험이 영문 데이터셋에 한정되어 다국어 성능에 대한 검증 부재.

- **후속 연구**:
  - 더 복잡한 인과 구조(예: 참고문헌 간 상호작용, 대상 논문과의 관계)를 포함한 확장 인과 그래프 설계.
  - 다양한 문서 생성 과제(다중 문서 요약, 기술 보고서 생성 등)로의 확대 적용.
  - 다국어 환경에서의 성능 평가 및 문화적 글쓰기 습관 차이에 대한 인과 분석.
  - 개입 강도의 자동 조정 메커니즘의 더욱 정교한 학습 방식 개발.

## Evaluation

- **Novelty**: 4.5/5
  - 관련 업무 생성에 인과 이론을 처음 적용한 점에서 높은 독창성을 보유. 다만 인과 개입 자체는 기존 연구에서 활용되어온 기법이므로 완전한 신규성은 아님.

- **Technical Soundness**: 4/5
  - do-calculus 및 백도어 기준의 수학적 기초는 견고함. 구현 세부사항에서 문장 시작 단어 선택의 정당성이 다소 휴리스틱으로 보임. Context-aware Remapping의 효과 메커니즘이 충분히 명확하지 않은 부분 있음.

- **Significance**: 4/5
  - 실제 데이터셋에서 성능 개선을 입증했으나, 정량적 개선 정도가 중간 수준. 학술 논문 작성 커뮤니티에 대한 실질적 임팩트는 제한적일 수 있음. 그러나 인과 기반 NLG 연구에 대한 새로운 방향 제시.

- **Clarity**: 3.5/5
  - 인과 그래프와 do-calculus 유도는 명확하나, 각 모듈의 상호작용과 정확한 수학적 동작이 부분적으로 불명확. 일부 기호와 개념 정의가 불완전함.

- **Overall**: 4/5

**총평**: 관련 업무 생성 분야에 인과 이론을 창의적으로 도입한 우수한 논문으로, 허위 상관관계 제거의 중요성을 체계적으로 다루었다. 다만 인과 모델의 단순성과 구현의 일부 휴리스틱 선택이 기술적 엄밀성을 다소 감소시킨다.

## Related Papers

- 🔄 다른 접근: [[papers/573_Neural_related_work_summarization_with_a_joint_context-drive/review]] — 공동 맥락 기반 관련 업무 요약과 다른 접근으로 인과 개입을 통한 관련 업무 생성을 제시한다.
- 🔗 후속 연구: [[papers/581_Oarelatedwork_A_large-scale_dataset_of_related_work_sections/review]] — 오픈액세스 관련 업무 섹션 대규모 데이터셋을 활용하여 인과 개입 기법의 효과를 검증할 수 있다.
- 🏛 기반 연구: [[papers/191_Causal_learning_for_socially_responsible_ai/review]] — 사회적 책임감 있는 AI를 위한 인과 학습 연구로 관련 업무 생성에서 편향 제거의 이론적 기반을 제공한다.
