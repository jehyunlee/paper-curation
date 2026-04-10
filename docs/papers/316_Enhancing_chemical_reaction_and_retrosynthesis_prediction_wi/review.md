---
title: "316_Enhancing_chemical_reaction_and_retrosynthesis_prediction_wi"
authors:
  - "Xuan Lin"
  - "Qingrui Liu"
  - "Hongxin Xiang"
  - "Daojian Zeng"
  - "Xiangxiang Zeng"
date: "2025"
doi: "arXiv:2505.02639"
arxiv: ""
score: 4.0
essence: "본 논문은 대규모 언어 모델(LLM)을 화학 반응 및 역합성 예측에 적용할 때 직면하는 데이터 부족과 과제 간 상관관계 무시 문제를 해결하기 위해, BRICS 기반 440만 개 분자 데이터셋과 이중 과제 학습 전략을 갖춘 ChemDual 프레임워크를 제안한다."
tags:
  - "cat/Cognitive_AI_Evaluation_and_Benchmarking"
  - "sub/Retrosynthesis_Strategy_Planning"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Reiser et al._2025_Enhancing chemical reaction and retrosynthesis prediction with large language model and dual-task le.pdf"
---

# Enhancing chemical reaction and retrosynthesis prediction with large language model and dual-task learning

> **저자**: Xuan Lin, Qingrui Liu, Hongxin Xiang, Daojian Zeng, Xiangxiang Zeng | **날짜**: 2025 | **DOI**: [arXiv:2505.02639](https://arxiv.org/abs/2505.02639)

---

## Essence

![Figure 1](figures/fig1.webp) *BRICS 기반 단편(fragment)과 반응물(reactant) 간의 유사성 분포(평균 66.5%) 및 이중 과제 학습을 통한 성능 향상(6.3% 개선)*

본 논문은 대규모 언어 모델(LLM)을 화학 반응 및 역합성 예측에 적용할 때 직면하는 데이터 부족과 과제 간 상관관계 무시 문제를 해결하기 위해, BRICS 기반 440만 개 분자 데이터셋과 이중 과제 학습 전략을 갖춘 ChemDual 프레임워크를 제안한다.

## Motivation

- **Known**: 대규모 언어 모델(LLaMA, ChatGLM 등)이 다양한 영역에서 우수한 성능을 보이고 있으며, Mol-Instruction 등이 화학 반응 예측에 유망한 결과를 제시했음
  
- **Gap**: 
  1. 고품질 화학 합성 데이터는 실험실 기반이라 획득 비용이 높고 규모가 제한적 (기존 연구: ~30k 샘플)
  2. 기존 방법들은 분자→반응물(Molecule-to-Reactants)과 반응물→분자(Reactants-to-Molecules)를 독립적인 단일 과제로 취급하여 역방향 과정 간의 상관관계를 무시

- **Why**: BRICS 알고리즘으로 생성된 단편(fragment)이 실제 반응물과 높은 유사성(평균 66.5%)을 보이며, 두 예측 과제는 본질적으로 역 프로세스이므로 함께 최적화될 수 있음

- **Approach**: (1) BRICS 기반 저비용 대규모 데이터셋(440만) 구축, (2) 다중 규모 토크나이저를 통한 원자·함수기·단편 수준의 분자 정보 캡처, (3) 단편 재조합 및 반응 예측을 동시에 최적화하는 이중 과제 학습 전략 도입

## Achievement

![Figure 2](figures/fig1.webp) *ChemDual의 전체 구조: 데이터셋 구축, 다중 규모 토크나이저, 이중 과제 학습 모듈*

1. **성능 향상**: Mol-Instruction 및 USPTO-50K 데이터셋에서 기존 단일 과제 접근법 및 일반 오픈소스 LLM을 능가하는 정확도 달성 (반응 예측에서 이중 과제 학습 적용 시 6.3% Exact Match Score 개선)

2. **약물 설계 잠재력**: 분자 도킹 분석 결과 ChemDual이 단백질 결합 친화도가 우수하고 다양한 화합물을 생성하여 신약 설계에 강한 응용 가능성 입증

3. **효율적 데이터 구축**: 20M SMILES 시퀀스로부터 440만 개의 학습용 지시문 자동 생성으로 데이터 획득 비용 대폭 절감

## How

![Figure 3](figures/fig1.webp) *지시문 세트 예시: 역합성(전방 과제)과 반응 예측(후방 과제)*

**Dataset Construction (3.1절)**
- ChEMBL-34 데이터베이스에서 20M 분자 SMILES 수집 → 중복 제거, 유효성 검증, 분자량 필터링 → 2.2M 분자 라이브러리 구축
- BRICS 알고리즘으로 단편 생성 및 원래 SMILES로 재조합 (적응형 단편화로 메모리 오버플로우 방지)
- 식(1): `n = L` (L<k일 때) 또는 `min(L, ⌊L/k^α⌋)` (그 외)로 단편 수 동적 조정
- 지정된 템플릿으로 440만 개 지시문 자동 생성

**Multi-scale Tokenizer (3.2절)**
- 원본 LLaMA 토크나이저 확장으로 분자 토큰(BOM/EOM), 단편 토큰(BOF/EOF), 더미 원자(dummy atom) [1*]~[16*] 등을 구분
- 0-15: 더미 원자 토큰, 16-195: 단편 토크나이저, 196-197: 분자 토큰, 198-199: 특수 토큰, 200-131072: 원본 LLaMA 토큰

**Dual-task Learning (3.3절)**
- 사전학습(Pre-training): 분자↔단편 이중 과제로 일반적 화학 합성 지식 학습
- 지시문 미세조정(Instruction Fine-tuning): 분자↔반응물 이중 과제로 작업별 예측 능력 습득
- 손실 함수: 두 과제의 손실을 동시에 최소화하여 전방향(반응 예측)과 후방향(역합성) 과정 간 상관관계 포착

## Originality

- **대규모 저비용 데이터셋**: BRICS 기반으로 단편-반응물의 높은 상관성(66.5%)을 활용하여 440만 개 데이터 자동 생성—기존 30k 수준 대비 대규모 확보
  
- **이중 과제 학습의 화학적 근거**: 단순히 멀티태스크 학습이 아니라 분자→반응물과 반응물→분자가 역 프로세스임을 명시적으로 모델링하여 상호 연관성 활용

- **다중 규모 토크나이저**: 원자 수준, 함수기 수준, 단편 수준의 계층적 분자 정보를 토크나이저 설계에 반영한 구조적 혁신

- **통합 프레임워크**: 데이터 구축→토크나이저→학습 전략이 유기적으로 연결된 일관된 설계

## Limitation & Further Study

- **단편화의 한계**: BRICS는 화학적으로 타당한 절단만 수행하므로, 모든 가능한 합성 경로를 충분히 표현하지 못할 가능성

- **토큰 길이 제약**: 512 이상의 토큰 길이 분자를 전처리 단계에서 제외하므로 초대형 분자 처리 불가

- **평가 범위 제한**: Mol-Instruction과 USPTO-50K만으로 검증되었으며, 다른 화학 작업(분자 특성 예측 등)으로의 일반화 미흡

- **해석 가능성 부족**: 이중 과제 학습이 LLM의 내부 표현을 어떻게 개선하는지에 대한 심층 분석 부재

- **후속 연구**: (1) 다양한 단편화 전략(예: 머신러닝 기반 절단점 학습) 적용, (2) 더 긴 분자 처리를 위한 토큰 압축 기법, (3) 단백질-리간드 상호작용 등 생물의약화학 문제로 확장

## Evaluation

- **Novelty**: 4.5/5 — BRICS 기반 대규모 데이터 구축과 이중 과제 학습의 화학적 동기 부여는 신선하나, 개별 기법(BRICS, 멀티태스크 학습)의 기본성은 제한

- **Technical Soundness**: 4/5 — 방법론 전개가 명확하고 데이터 구축 파이프라인이 체계적이나, 손실 함수 상세 정의 및 초매개변수 선택 근거가 부분적으로 부족

- **Significance**: 4/5 — 실제 약물 설계 응용 가능성(분자 도킹 분석) 입증 및 기존 모델 대비 명확한 성능 향상으로 실질적 가치 높음. 다만 단일 LLM 기반(LLaMA) 평가 범위 제한

- **Clarity**: 4/5 — 전반적으로 잘 구성되었으나, 다중 규모 토크나이저의 구체적 작동 메커니즘(Figure 2(b))에 대한 설명이 충분하지 않으며, 적응형 단편화 식(1)의 직관 제시 부족

- **Overall**: 4/5

**총평**: ChemDual은 BRICS 기반 저비용 대규모 데이터셋과 화학적 직관에 기반한 이중 과제 학습으로 화학 반응/역합성 예측에서 의미 있는 성능 향상을 달성했으며, 약물 설계 응용 가능성을 실증했다. 다만 단편화 방법의 한계, 해석 가능성 부족, 평가 범위 확대의 필요성이 향후 개선 방향이다.

## Related Papers

- 🔄 다른 접근: [[papers/856_Unimatch_Universal_matching_from_atom_to_task_for_few-shot_d/review]] — 화학 반응 예측에서 원자 수준부터 과제 수준까지의 계층적 접근법을 사용하지만 메타러닝과 듀얼 태스크 학습이라는 다른 전략을 채택한다.
- 🔗 후속 연구: [[papers/210_ChemCrow_Augmenting_large-language_models_with_chemistry_too/review]] — 화학 도구를 활용한 LLM 확장이 ChemDual의 화학 반응 예측 프레임워크와 상호 보완적인 접근법이다.
- 🧪 응용 사례: [[papers/461_LARC_Towards_Human-level_Constrained_Retrosynthesis_Planning/review]] — 인간 수준의 제약 조건을 고려한 역합성 계획이 ChemDual의 역합성 예측 기능의 실제 적용 영역이다.
- 🔄 다른 접근: [[papers/856_Unimatch_Universal_matching_from_atom_to_task_for_few-shot_d/review]] — few-shot 약물 발견에서 계층적 매칭과 메타러닝을 사용하는 반면 ChemDual은 듀얼 태스크 학습을 채택하는 다른 접근법이다.
- 🧪 응용 사례: [[papers/1106_The_BOS-Lig_Dataset_Accurate_Ligand_Charges_from_a_Consensus/review]] — 화학 반응 및 역합성 예측 성능 향상에서 본 논문의 정확한 리간드 전하 정보를 활용할 수 있다.
