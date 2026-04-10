---
title: "555_Molgan_An_implicit_generative_model_for_small_molecular_grap"
authors:
  - "Nicola De Cao"
  - "Thomas Kipf"
date: "2018"
doi: "arXiv:1805.11973"
arxiv: ""
score: 4.2
essence: "본 논문은 그래프 구조 데이터에 직접 작동하는 GAN 기반 암묵적(implicit) 생성 모델을 제안하여, 분자 설계에서 비용이 큰 그래프 매칭 절차와 노드 순서 휴리스틱을 우회하고 높은 유효성의 화학 화합물을 생성한다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/3D_Molecular_Generation"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Cao and Kipf_2018_Molgan An implicit generative model for small molecular graphs.pdf"
---

# Molgan: An implicit generative model for small molecular graphs

> **저자**: Nicola De Cao, Thomas Kipf | **날짜**: 2018 | **DOI**: [arXiv:1805.11973](https://arxiv.org/abs/1805.11973)

---

## Essence

![Figure 1](figures/fig1.webp)
*MolGAN의 전체 구조: 잠재변수 z로부터 생성기가 분자 그래프를 생성하고, 판별기는 실제/생성 데이터 분류, 보상망은 화학적 성질을 평가한다.*

본 논문은 그래프 구조 데이터에 직접 작동하는 GAN 기반 암묵적(implicit) 생성 모델을 제안하여, 분자 설계에서 비용이 큰 그래프 매칭 절차와 노드 순서 휴리스틱을 우회하고 높은 유효성의 화학 화합물을 생성한다.

## Motivation

- **Known**: 기존 분자 생성 모델들(VAE, RNN 기반)은 SMILES 문자열 표현을 사용하거나, 그래프 직접 생성 시 노드 순서 문제로 인해 비싼 그래프 매칭 절차나 모든 가능한 노드 순열의 우도(likelihood) 계산이 필요함

- **Gap**: 그래프 기반 분자 생성에서 노드 순서 불변성(permutation invariance)을 처리하면서도 계산 효율성을 유지하는 방법의 부재

- **Why**: 신약 개발(de novo drug design)은 이산적이고 광대한 화학 구조 공간에서 원하는 특성을 가진 분자를 찾아야 하며, 직접 그래프 공간에서 작동하면 SMILES의 구문 규칙 학습 오버헤드를 제거 가능

- **Approach**: GAN을 그래프에 맞게 적응시키되, 판별기와 보상망은 그래프 합성곱(graph convolution)으로 노드 순서 불변성을 확보하고, 생성기는 우도 제약 없이 자유롭게 노드 순서 선택

## Achievement

![Figure 2](figures/fig2.webp)
*MolGAN 아키텍처: 생성기는 인접 행렬 A와 주석 행렬 X를 생성한 후 카테고리 샘플링으로 이산화하여 분자 그래프를 완성한다.*

1. **높은 유효성**: QM9 데이터셋에서 거의 100%에 가까운 유효한 화학 화합물 생성 달성

2. **우수한 비교 성능**: SMILES 기반 방법들(RNN-VAE, ORGAN)과 likelihood 기반 그래프 생성 방법보다 우수한 성능 입증

3. **화학적 특성 최적화**: 강화학습(RL) 목표와 결합하여 약물 유사성(druglikeness, QED) 등 특정 화학 성질 최적화 가능

## How

![Figure 3](figures/fig3.webp)
*QM9 데이터셋 샘플(좌)과 약물 유사성(QED)으로 최적화된 MolGAN 생성 분자(우)*

- **생성기(Generator)**: 
  - 잠재 벡터 z ~ p(z)에서 샘플링하여 조밀한(dense) 인접 행렬 Ã ∈ ℝ^(N×N×Y)와 주석 행렬 X̃ ∈ ℝ^(N×T) 생성
  - 카테고리 샘플링을 통해 이산화하여 이산 그래프 표현 획득
  - 비순차적(non-sequential) 한 번 생성으로 계산 효율성 확보

- **판별기(Discriminator)**: 
  - Improved WGAN 손실함수 사용(기울기 페널티 포함)
  - 그래프 합성곱 네트워크(GCN) 기반으로 노드 순서 불변성 확보
  - 미니배치 판별(minibatch discrimination)로 모드 붕괴(mode collapse) 완화

- **보상망(Reward Network)**: 
  - 생성된 분자의 화학적 성질을 예측하는 미분 가능한 근사함수 R̂_ψ(G)
  - 외부 소프트웨어(RDKit)의 실제 보상과 MSE 손실로 학습
  - 결정적 정책 그래디언트(Deterministic Policy Gradient, DPG)로 생성기 최적화

- **손실함수**: 생성기는 WGAN 손실과 보상 손실의 가중 결합으로 훈련

## Originality

- **최초 적용**: 그래프 구조의 분자 생성에 GAN을 처음으로 적용한 연구

- **노드 순서 문제 해결**: 우도 기반 방법의 비싼 그래프 매칭을 피하고, 암묵적 모델의 자유도로 노드 순서 선택의 유연성 확보

- **다중 목표 최적화**: GAN의 유효성 학습과 RL 기반 화학적 성질 최적화를 통합하는 새로운 프레임워크

- **순열 불변 아키텍처**: GCN 기반 판별기와 보상망으로 그래프의 구조적 특성 활용

## Limitation & Further Study

- **모드 붕괴 취약성**: 논문에서 인정하듯이 GAN의 근본적 한계인 모드 붕괴(mode collapse)에 여전히 취약하며, 미니배치 판별과 WGAN으로 완전히 해결하지 못함

- **소분자 제한**: "small molecular graphs"로 제한되어 있으며, 더 큰 분자나 복잡한 구조로의 확장성 미검증

- **보상 함수 학습**: 외부 보상 평가 시스템(RDKit)에 의존하므로, 유효하지 않은 분자에 대해 영점 보상만 할당하는 단순한 처리

- **순차 생성 미탐색**: 논문에서 순차적 변형 가능성을 언급했지만 구현 및 비교 실험 부재

- **후속 연구 방향**:
  - 더 안정적인 GAN 변형 또는 다른 암묵적 모델 탐색
  - 분자 크기 및 복잡도 증대에 대한 확장성 연구
  - 보상 함수의 더 정교한 설계 및 학습 방식
  - 그래프 정규화(normalization) 기법 도입으로 생성 품질 개선

## Evaluation

- **Novelty**: 4.5/5
  - GAN을 그래프 기반 분자 생성에 처음 적용한 점과 노드 순서 불변 아키텍처는 혁신적이나, 개별 기술들(WGAN, GCN, DPG)은 기존 방법의 조합

- **Technical Soundness**: 4/5
  - 수학적 기초가 견고하고 Improved WGAN 및 DPG 적용이 타당하나, 모드 붕괴 문제와 비유효 분자에 대한 보상 처리가 단순함

- **Significance**: 4/5
  - 분자 생성 분야에서 의미 있는 진전을 보이고 높은 유효성 달성하나, 소분자 제한과 실제 신약 개발 적용 가능성 검증 부족

- **Clarity**: 4.5/5
  - 명확한 그림 설명과 논리적 흐름이 우수하나, 일부 기술 세부사항(예: 카테고리 샘플링 구체적 과정)의 추가 설명 필요

- **Overall**: 4.2/5

**총평**: MolGAN은 그래프 기반 분자 생성에 GAN을 성공적으로 적용한 선구적 연구로, 노드 순서 불변성 문제를 우아하게 해결하고 높은 유효성의 화합물을 생성하나, 모드 붕괴 취약성과 소분자 제한이라는 근본적 과제를 안고 있다.

## Related Papers

- 🔄 다른 접근: [[papers/867_Verifier-Constrained_Flow_Expansion_for_Discovery_Beyond_the/review]] — 분자 생성에서 MolGAN은 GAN 기반 암묵적 방법을, Flow 확장은 명시적 확률 모델을 사용하는 대조적 접근법
- 🔗 후속 연구: [[papers/345_Foundation_Molecular_Grammar_Multi-Modal_Foundation_Models_I/review]] — Foundation Molecular Grammar의 해석 가능한 분자 문법이 MolGAN의 생성 결과를 체계적으로 분석하는 도구로 활용됨
- 🏛 기반 연구: [[papers/282_DMFlow_Disordered_Materials_Generation_by_Flow_Matching/review]] — DMFlow의 무질서 물질 생성 방법론이 MolGAN의 분자 그래프 생성 알고리즘 개발에 기초가 됨
- 🏛 기반 연구: [[papers/349_Fragment_and_Geometry_Aware_Tokenization_of_Molecules_for_St/review]] — 소분자 그래프 생성을 위한 암시적 생성 모델이 구조 기반 분자 토큰화의 방법론적 기반을 제공합니다.
- 🔄 다른 접근: [[papers/867_Verifier-Constrained_Flow_Expansion_for_Discovery_Beyond_the/review]] — 분자 생성에서 Flow 확장은 명시적 확률 모델을, MolGAN은 GAN 기반 암묵적 방법을 사용하는 대조적 접근법
- 🔗 후속 연구: [[papers/345_Foundation_Molecular_Grammar_Multi-Modal_Foundation_Models_I/review]] — MolGAN의 분자 생성 결과를 Foundation Molecular Grammar의 해석 가능한 문법 구조로 체계적으로 분석할 수 있음
- 🏛 기반 연구: [[papers/282_DMFlow_Disordered_Materials_Generation_by_Flow_Matching/review]] — 소분자용 암시적 생성모델 MolGAN이 무질서 재료 생성의 기반 제공
