---
title: "291_Drugclip_Contrastive_drug-disease_interaction_for_drug_repur"
authors:
  - "Yingzhou Lu"
  - "Yaojun Hu"
  - "Chenhao Li"
date: "2024"
doi: "N/A"
arxiv: ""
score: 4.0
essence: "기존 임상시험 데이터를 기반으로 약물-질병 상호작용(drug-disease interaction)을 학습하는 대조학습(contrastive learning) 방법 DrugCLIP을 제안하여, 음성 샘플(negative samples) 부족 문제를 해결하고 약물 재창출(drug repurposing) 효율을 16.5% 향상시켰다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/AI_Drug_Discovery"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Lu et al._2024_Drugclip Contrastive drug-disease interaction for drug repurposing.pdf"
---

# DrugCLIP: Contrastive drug-disease interaction for drug repurposing

> **저자**: Yingzhou Lu, Yaojun Hu, Chenhao Li | **날짜**: 2024 | **DOI**: N/A

---

## Essence

![Figure 1: Drug repurposing의 개념 - 기존 승인된 약물을 새로운 질병 치료에 재사용하는 과정](figures/fig1.webp)

기존 임상시험 데이터를 기반으로 약물-질병 상호작용(drug-disease interaction)을 학습하는 대조학습(contrastive learning) 방법 DrugCLIP을 제안하여, 음성 샘플(negative samples) 부족 문제를 해결하고 약물 재창출(drug repurposing) 효율을 16.5% 향상시켰다.

## Motivation

- **Known**: 기존 약물을 새로운 질병 치료에 재사용하면 약 10년, 수십억 달러의 신약개발 비용과 시간을 절감할 수 있으며, DeepPurpose 등의 기계학습 방법들이 약물-표적(drug-target) 상호작용 예측에 성과를 보이고 있음

- **Gap**: 
  - C1: 임상시험 데이터의 낮은 품질, 잡음(noise), 민감성 및 개인정보 문제
  - C2: 특히 음성 샘플 부족 - 어떤 약물이 어떤 질병을 치료할 수 있는지는 알지만, 어떤 약물이 특정 질병을 **치료하지 못하는지**에 대한 정보 부재
  - C3: 약물 분자(drug molecules)와 질병 코드(disease codes) 등 다중양식(multimodal) 데이터의 통합 어려움

- **Why**: 음성 샘플이 없는 상황에서도 효과적으로 학습할 수 있는 방법이 필요하며, 약물-질병 상호작용의 복잡한 구조를 제대로 표현해야 함

- **Approach**: 
  1. 임상시험 데이터로부터 고품질 약물 재창출 데이터셋 구축
  2. 대조학습(CLIP 기반) 프레임워크로 음성 샘플 자동 생성 및 양성 샘플 판별
  3. 약물 분자에 대해 그래프신경망(GNN) 기반 표현학습, 질병 코드에 대해 계층적 임베딩 학습

## Achievement

![Figure 2: 메시지 전달 신경망(MPNN)을 이용한 약물 분자 표현 - 이웃 노드들의 표현을 반복적으로 집계하여 그래프 레벨 표현 생성](figures/fig2.webp)

1. **데이터셋 기여**: 2000년대 초부터 현재까지 약 35,000개의 임상시험으로 구성된 약물 재창출 전문 데이터셋 구축 및 공개

2. **방법론 성과**: DrugCLIP 모델이 최고 성능 기준 대비 Hit Rate에서 16.5% 향상 달성

3. **다중양식 표현**: 약물(분자 그래프)과 질병(ICD 코드 계층구조)의 서로 다른 데이터 형식을 통일된 임베딩 공간(embedding space)으로 효과적으로 변환

## How

![Figure 3: 그래프 기반 어텐션 모델 구조](figures/fig3.webp)

### 약물 분자 표현 (Drug Molecule Representation)

- **분자 그래프 구조**: SMILES 문자열 대신 분자 그래프를 사용 (노드=원자, 엣지=화학결합)
- **메시지 전달 신경망(MPNN)** 활용:
  - 식 (2): 각 방향성 엣지 임베딩 m_{uv}^{(l)}을 반복적으로 업데이트
  - 식 (3): MLP f₂를 통해 이웃 메시지들 집계하여 노드 임베딩 h_u 생성
  - 식 (4): READOUT 함수로 모든 노드 임베딩을 집계하여 그래프 레벨 표현 h_G 생성
- **결합 정보 포함**: 0(비결합), 1(단일결합), 2(이중결합), 3(삼중결합), 4(방향족결합)을 구분하여 인코딩

### 질병 코드 표현 (Disease Code Representation)

- **표준화된 코드 시스템** 활용: ICD-10-CM, ICD-9-CM, SNOMED CT 등
- **계층적 구조 활용**: ICD-10-CM을 예시로 7자리 영숫자 코드의 계층 관계 이용
  - 예: "G44" (두통 증후군) → "G44.31" (급성 외상후 두통) → "G44.311" (편두통성)
- **다중 정보원 활용**: 코드 설명(description)과 질병 온톨로지(ontology) 결합

### 대조학습 기반 약물-질병 상호작용 (Contrastive Drug-Disease Interaction Learning)

- **핵심 아이디어**: CLIP(Contrastive Language-Image Pre-training) 패러다임을 약물-질병 영역에 적용
- **음성 샘플 자동 생성**: 배치 내 다른 약물-질병 쌍을 음성 샘플로 활용 (hard negatives 포함)
- **대조 손실(contrastive loss)**: 양성 쌍(positive pairs)의 유사도는 최대화, 음성 쌍(negative pairs) 유사도는 최소화
- **라벨 요구 최소화**: 양성 샘플만 필요 → 임상시험 데이터의 실제 약물-질병 관계 활용

## Originality

- **새로운 문제 정의**: 약물-질병 상호작용을 대조학습 프레임워크로 재해석하여 라벨 부족 문제 해결

- **데이터셋 구축의 가치**: 실제 임상시험 기록(clinical trial records)을 기반한 35K 규모의 고품질 데이터셋 제공으로 재현성(reproducibility) 향상

- **다중양식 통합**: 분자 그래프(GNN)와 질병 코드 계층구조를 통합 임베딩 공간으로 학습하는 엔드투엔드 방식

- **임상 적실성**: 기존 약물-**단백질 표적** 상호작용 예측에서 약물-**질병** 상호작용으로 패러다임 전환 (실제 임상 의사결정과 더 직접적 연결)

## Limitation & Further Study

- **음성 샘플의 모호성**: 현재 프레임워크에서 "치료 불가"를 명시적으로 학습하지 않음 - 실제로 치료하지 못하는 경우와 단순히 시도하지 않은 경우의 구분 필요

- **시간적 역학(temporal dynamics) 부재**: 약물이 임상시험 과정 중 어느 단계에서 질병과 연결되었는지의 시간 정보 활용 미흡

- **외부 검증(external validation) 필요**: 제안된 데이터셋과 동일 출처의 데이터로 평가되어, 다른 임상시험 데이터베이스나 실제 임상 결과로의 일반화 검증 필요

- **생물학적 설명성(interpretability)**: 대조학습의 블랙박스 특성으로 인해 특정 약물-질병 예측의 생물학적 근거 제시 부족

- **후속 연구 방향**:
  1. 약물의 약동학(pharmacokinetics), 약력학(pharmacodynamics) 정보 통합
  2. 환자 인구통계학적 특성(demographics)이나 유전체 정보 포함
  3. 임상시험의 실패 사유(failure reasons) 분석을 통한 부정적 증거 활용
  4. 그래프 신경망의 해석 가능성(interpretability) 향상 (attention visualization 등)

## Evaluation

- **Novelty**: 4/5 
  - 약물-질병 상호작용에 CLIP 기반 대조학습 적용은 신선함
  - 다만 개별 구성 요소(GNN, 대조학습)는 기존 기술의 조합

- **Technical Soundness**: 4/5
  - MPNN과 대조학습의 기술적 구현은 견고함
  - 데이터셋 구축 방법론의 세부 기술 설명이 논문에서 충분하지 않음

- **Significance**: 4/5
  - 약물 재창출은 임상 및 경제적 중요성 높음
  - 35K 규모의 임상시험 기반 데이터셋 제공의 영향력 우수
  - 16.5% 성능 향상은 실용적 의미 있음
  - 다만 완전히 새로운 질병 치료법 발견 사례 부재

- **Clarity**: 3.5/5
  - 전반적 구조와 동기 표현은 명확함
  - 질병 코드 표현 방법의 구체적 구현 세부 사항 부족
  - 대조학습 손실 함수의 정확한 수식 제시 필요
  - 데이터셋 처리 및 전처리 과정 설명 미흡

- **Overall**: 4/5

**총평**: DrugCLIP은 약물 재창출이라는 실용적 문제에 대조학습을 창의적으로 적용하고 품질 높은 임상시험 기반 데이터셋을 제공함으로써 의약학 AI 분야에 의미 있는 기여를 한 논문이다. 다만 생물학적 검증, 외부 데이터셋을 통한 일반화 검증, 그리고 예측 결과의 해석 가능성 제고 측면에서 향상이 필요하다.

## Related Papers

- 🔗 후속 연구: [[papers/397_Hallucinations_can_improve_large_language_models_in_drug_dis/review]] — 약물 발견에서 LLM 환각 개선에서 대조학습 약물 재창출로의 확장
- 🔄 다른 접근: [[papers/490_LIDDIA_Language-based_Intelligent_Drug_Discovery_Agent/review]] — 언어 기반 지능형 약물 발견과 대조학습 재창출의 다른 접근법
- 🏛 기반 연구: [[papers/292_Drugpilot_Llm-based_parameterized_reasoning_agent_for_drug_d/review]] — 매개변수화된 추론 약물 파일럿이 약물-질병 상호작용의 기반 제공
- 🏛 기반 연구: [[papers/415_Hunt_Globally_Wide_Search_AI_Agents_for_Drug_Asset_Scouting/review]] — 대조 학습 기반 약물-질병 상호작용 모델이 투자 관점에서 약물 자산 평가의 방법론적 기반을 제공합니다.
- 🏛 기반 연구: [[papers/1106_The_BOS-Lig_Dataset_Accurate_Ligand_Charges_from_a_Consensus/review]] — 약물 재창출을 위한 대조학습이 리간드 전하 결정의 기반 방법론 제공
