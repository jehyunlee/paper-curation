---
title: "837_Training_a_Scientific_Reasoning_Model_for_Chemistry"
authors:
  - "Siddharth Narayanan"
  - "James D. Braza"
  - "Ryan-Rhys Griffiths"
  - "Albert Bou"
  - "G. Wellawatte"
date: "2025"
doi: "10.48550/arXiv.2506.17238"
arxiv: ""
score: 4.0
essence: "화학 도메인을 위해 특화된 추론 모델(reasoning model)을 강화학습으로 훈련하면, 추가 도메인 사전학습 없이도 일반 목적 모델과 전문가를 능가하는 성능을 달성할 수 있음을 입증하는 연구이다. ether0라는 24B 파라미터 모델은 자연언어 추론과 화학 구조(SMILES) 출력을 통합하여 약물 발견의 핵심 단계를 지원한다."
tags:
  - "cat/Scientific_Language_Processing_and_Visualization"
  - "sub/Domain-adapted_Instruction_Models"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Narayanan et al._2025_Training a Scientific Reasoning Model for Chemistry.pdf"
---

# Training a Scientific Reasoning Model for Chemistry

> **저자**: Siddharth Narayanan, James D. Braza, Ryan-Rhys Griffiths, Albert Bou, G. Wellawatte | **날짜**: 2025 | **DOI**: [10.48550/arXiv.2506.17238](https://doi.org/10.48550/arXiv.2506.17238)

---

## Essence

화학 도메인을 위해 특화된 추론 모델(reasoning model)을 강화학습으로 훈련하면, 추가 도메인 사전학습 없이도 일반 목적 모델과 전문가를 능가하는 성능을 달성할 수 있음을 입증하는 연구이다. ether0라는 24B 파라미터 모델은 자연언어 추론과 화학 구조(SMILES) 출력을 통합하여 약물 발견의 핵심 단계를 지원한다.

## Motivation

- **Known**: 최근 추론 모델(chain-of-thought, reinforcement learning 기반)이 수학과 프로그래밍 분야에서 탁월한 성과를 보여줌. 하지만 과학 분야, 특히 화학의 복잡한 추론 작업에 적용된 사례는 극히 드묾.

- **Gap**: 기존 화학 AI 연구는 주로 지식 문제(multiple-choice) 평가에 집중했고, 역설계(retrosynthesis), 분자 수정 같은 진정한 화학 추론 작업에 대한 대규모 강화학습 적용이 부재함.

- **Why**: 화학은 추론 모델에 매우 적합한 도메인임. 솔루션 검증이 용이(분자의 물성을 측정할 수 있음)하지만 생성은 어렵다는 "역문제(inverse problem)" 구조가 수학/프로그래밍과 유사하고, SMILES로 텍스트 표현이 가능해 모달리티별 인코더 불필요.

- **Approach**: 640,730개의 실험 기반 화학 문제(375개 작업)로 강화학습을 통해 24B 파라미터 모델 훈련. Supervised Fine-Tuning(SFT) → Group Relative Policy Optimization(GRPO)의 단계적 학습, 추론 패턴 증류, 동적 커리큘럼 등의 최적화 기법 활용.

## Achievement

![Figure 1: 훈련 방법론 개요 및 ether0의 추론 예시. 하단의 훈련 단계는 각 단계별 정확도를 동일 x축 범위로 정규화하여 표시](figures/fig1.webp)

1. **성능 우위**: ether0는 GPT-4o, Llama 같은 최첨단 LLM, 일반 화학 모델, 인간 전문가를 분자 설계 작업에서 초과. 특히 retrosynthesis, solubility editing 등 복합 추론 작업에서 두드러짐.

2. **데이터 효율성**: 전문화된 도메인 특화 모델(Molecular Transformer 등)과 비교해 월등히 적은 데이터로 더 나은 성능 달성. 이는 추론 모델의 일반성과 강화학습의 효율성을 입증.

3. **약물 발견 파이프라인 통합**: Hit discovery(후보 생성) → Hit-to-lead(효능/선택성 개선) → Lead optimization(효과 강화, 독성 감소, ADMET 개선)의 핵심 단계를 합성 가능성 제약 하에서 지원.

4. **375개 작업의 다양성**: 단순 구조 변환(IUPAC name, SMILES completion)부터 복합 특성 예측(혈뇌장벽 투과성, 수용체 결합, 냄새 특성)까지 포괄.

## How

![Figure 2: 일반 목적 LLM과의 작업별 성능 비교](figures/fig2.webp)

- **문제 구성**: 640,730개 질문-답변 쌍을 ChEMBL, COCONUT, ORD 등 실험 데이터베이스에서 추출. 모든 분자는 합성된 실제 화합물만 사용(가상 분자 제외).

- **보상 함수 설계**: 
  - **코드 기반 검증**: RDKit로 SMILES 유효성, 분자 공식 검증
  - **머신러닝 검증**: KDESol로 용해도 계산, Molecular Transformer로 반응 예측 검증
  - **합성 가능성 필터**: 고리/지역 그룹으로 분절 가능성 확인 (†로 표시된 작업)
  - **다중선택 검증**: 실험 데이터와 문자 일치

- **훈련 단계**:
  1. **SFT (Supervised Fine-Tuning)**: 전문가 출력(specialist model)에서 추론 패턴 학습. 초기 정책(π₀) 설정.
  2. **거부 샘플링 (Rejection Sampling)**: 높은 보상의 궤적만 필터링해 SFT 고품질 데이터 확보.
  3. **증류 (Distillation)**: 전문가 모델로부터 추론 행동 증류.
  4. **GRPO (Group Relative Policy Optimization)**:
     - 그룹 단위로 G개 완성도(y₁,...,yG) 샘플링
     - 정규화된 이점(advantage) Aᵢ = (rᵢ - mean) / std 계산
     - PPO 클립 함수로 정책 목표 최적화: J(θ) = Σ[1/|yᵢ|·Σ_t(clipped_ratio - β·KL_divergence)]
     - 참조 정책(πref)과의 KL 발산으로 도출(drift) 방지

- **최적화 기법**:
  - **동적 커리큘럼**: 난이도별 작업을 점진적으로 학습
  - **All-task GRPO**: 모든 375개 작업에 대해 동시 최적화로 일반화 능력 향상
  - **모델 초기화**: 다중 specialist 모델의 rejection sampling 출력으로 SFT 데이터 확장

## Originality

- **첫 대규모 화학 추론 모델**: 화학 도메인에서 RL 기반 추론 모델을 대규모로 훈련한 첫 사례. 기존 연구는 CoT 프롬프팅이나 비추론 LLM 평가에만 집중.

- **실험 기반 데이터셋**: "가상 분자" 대신 ChEMBL, COCONUT, ORD 등에서 실제 합성된 화합물만 사용해 현실성 확보.

- **다층 검증 메커니즘**: 코드, ML 모델, 합성 가능성 필터를 결합한 포괄적 보상 함수. 특히 Bloom filter 기반 합성가능 시약 확인은 실용적 제약을 반영.

- **SFT → 거부샘플링 → 증류 → GRPO의 통합 파이프라인**: 기존 단순 RL보다 복합적인 훈련 전략으로 데이터 효율성 극대화.

- **약물 발견 가치사슬 통합**: Hit discovery부터 lead optimization까지 파이프라인의 여러 단계를 단일 모델에서 지원한다는 점이 임상/상업적 의미 있음.

## Limitation & Further Study

- **SMILES 한계**: 텍스트 기반 분자 표현이 복잡한 3D 구조(입체화학, 입체선택성)를 완전히 포착하지 못할 수 있음.

- **검증 가능성 제약**: 모든 작업이 자동 검증 가능하지는 않음. 예를 들어 '냄새' 작업은 MCQ 형태로 제한되어 있으며, 이는 개방형 생성 능력을 제약.

- **도메인 일반화 미미**: 학습된 모델이 화학에만 특화되어 있으며, 다른 과학 분야(재료학, 생물학)로의 전이 학습 가능성은 제시하지 않음.

- **데이터 분포 편향**: ChEMBL 등 기존 데이터베이스의 편향(약물 같은 분자 과다)이 모델에 반영될 수 있음.

- **인간 평가 부재**: 최종 성능 평가가 주로 자동 메트릭(정확도, 정확한 일치)에 기반해 있고, 화학자 평가 또는 합성 난이도 등 정성적 측면 검토 필요.

- **향후 연구 방향**: 
  - 다른 과학 분야(생물학, 재료학, 물리학)로의 확장
  - 멀티모달 표현(2D/3D 그래프 인코더) 통합으로 SMILES 한계 극복
  - 실제 합성 시간과 원가를 고려한 보상 함수 개선
  - 소수 데이터 환경에서의 성능 분석

## Evaluation

- **Novelty (독창성)**: 4.5/5
  - 화학에서 RL 기반 추론 모델의 첫 대규모 구현은 매우 혁신적
  - 실험 기반 데이터셋과 다층 검증 메커니즘이 고도로 설계됨
  - 다만 기술 자체(GRPO, SFT → RL)는 기존 방법론의 응용

- **Technical Soundness (기술적 건전성)**: 4/5
  - GRPO 구현과 훈련 파이프라인이 명확하고 재현 가능해 보임
  - 보상 함수 정의가 일관성 있으나, 일부 작업(elucidation)의 Tanimoto 0.7 임계값이 자의적일 수 있음
  - 인간 평가 또는 화학자 피드백 부재로 완전성 제한

- **Significance (영향력)**: 4.5/5
  - 약물 발견의 핵심 단계(hit discovery, optimization)를 지원한다는 점에서 임상/상업적 가치 상당
  - 다른 과학 분야로의 방법론 확장 가능성 높음 (예: BioReason, Med-R1 선례)
  - 그러나 실제 의약품 개발에서의 검증/적용 단계는 미흡

- **Clarity (명확성)**: 4/5
  - 논문 구조가 체계적이고 Figure가 효과적으로 정보 전달
  - 보상 함수와 훈련 파이프라인 설명이 비교적 명확
  - 일부 기술 세부사항(curriculum design, specialist model 구성)이 부록 의존적

- **Overall (종합)**: 4/5

**총평**: 화학 추론을 위한 대규모 RL 기반 언어 모델 개발의 첫 사례로서, 실험 데이터 기반의 640K 문제와 375개 작업의 다양한 검증 메커니즘을 통해 데이터 효율성과 성능에서 우수성을 입증한 강력한 연구이다. 약물 발견 파이프라인 통합과 다른 과학 분야로의 확장 가능성은 높으나, 실제 합성 검증, 3D 구조 고려, 및 임상 적용 가능성에 대한 평가는 향후 과제로 남아 있다.

## Related Papers

- 🔄 다른 접근: [[papers/176_CACTUS_Chemistry_Agent_Connecting_Tool_Usage_to_Science/review]] — 둘 다 화학 도메인에서 AI 에이전트를 다루지만 하나는 추론 모델 훈련에, 다른 하나는 도구 사용 연결에 초점을 맞춘다.
- 🔗 후속 연구: [[papers/115_Augmenting_large_language_models_with_chemistry_tools/review]] — 대규모 언어 모델에 화학 도구를 증강하는 방법이 ether0의 화학 구조 출력 능력 향상에 활용될 수 있다.
- 🏛 기반 연구: [[papers/651_RAG-Enhanced_Collaborative_LLM_Agents_for_Drug_Discovery/review]] — 약물 발견을 위한 RAG 강화 협업 LLM 에이전트 기술이 ether0의 약물 발견 지원 능력에 기반을 제공한다.
- 🔄 다른 접근: [[papers/723_Sciglm_Training_scientific_language_models_with_self-reflect/review]] — 둘 다 도메인 특화 과학 추론 모델을 구축하지만 하나는 자기 성찰적 지시 데이터를 사용하고 다른 하나는 화학 도메인에 특화된 강화학습을 사용한다.
