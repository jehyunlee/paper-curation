---
title: "260_DeepCRE_Transforming_Drug_RD_via_AI-Driven_Cross-drug_Respon"
authors:
  - "Yushuai Wu"
  - "Ting Zhang"
  - "Hao Zhou"
  - "Hainan Wu"
  - "Hanwen Sunchu"
date: "2024.03"
doi: "10.48550/arXiv.2403.03768"
arxiv: ""
score: 4.2
essence: "DeepCRE는 도메인 분리 네트워크(Domain Separation Network, DSN) 기반의 AI 모델로, 세포주 데이터로 학습하여 환자 수준의 약물 반응을 예측함으로써 신약 개발 후기 단계에서의 약물 효과 비교 평가를 가능하게 한다. 이를 통해 기존 모델 대비 17.7% 성능 향상과 5배의 적응증(indication) 수준 개선을 달성했다."
tags:
  - "cat/AI-Powered_Scientific_Research_Frameworks"
  - "sub/Biomedical_Research_Agents"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Wu et al._2024_DeepCRE Transforming Drug R&D via AI-Driven Cross-drug Response Evaluation.pdf"
---

# DeepCRE: Transforming Drug R&D via AI-Driven Cross-drug Response Evaluation

> **저자**: Yushuai Wu, Ting Zhang, Hao Zhou, Hainan Wu, Hanwen Sunchu, Lei Hu, Xiaofang Chen, Suyuan Zhao, Gaochao Liu, Chao Sun, Jiahuan Zhang, Yizhen Luo, Peng Liu, Zaiqing Nie | **날짜**: 2024-03-18 | **DOI**: [10.48550/arXiv.2403.03768](https://doi.org/10.48550/arXiv.2403.03768)

---

## Essence

![Figure 1](figures/fig1.webp) *약물 R&D 과정의 다양한 단계에서 교차 약물 반응 평가(CRE)의 역할*

DeepCRE는 도메인 분리 네트워크(Domain Separation Network, DSN) 기반의 AI 모델로, 세포주 데이터로 학습하여 환자 수준의 약물 반응을 예측함으로써 신약 개발 후기 단계에서의 약물 효과 비교 평가를 가능하게 한다. 이를 통해 기존 모델 대비 17.7% 성능 향상과 5배의 적응증(indication) 수준 개선을 달성했다.

## Motivation

- **Known**: 기존 SDL(Single-Drug Learning) 모델들(ADAE, CodeAE)은 약물별 독립적 모델을 사용하여 교차 약물 비교 불가능하며, MDL(Multi-Drug Learning) 모델들(DrugCell, Paccmann, TGSA)은 세포주 수준(cell-line level)에만 제한되어 있음

- **Gap**: 약물 R&D의 후기 단계(임상 전 동물/오르가노이드 실험, 환자 수준)에서 정확한 CRE 예측 모델이 부재하며, 이로 인해 유망한 약물 후보들이 임상시험에서 실패

- **Why**: 치료 옵션의 부족과 Eroom's Law(기술 발전에도 신약개발 효율이 감소)라는 산업적 난제를 해결하기 위해 환자 수준의 약물 반응 예측이 시급함

- **Approach**: 세포주와 환자의 유전자발현프로필(GEP)을 공유 공간으로 정렬하는 도메인 적응(domain adaptation) 전략과 종양 유형별 적응형 사전학습(tumor type-adaptive pretraining) 전략 도입

## Achievement

![Figure 3](figures/fig3.webp) *13개 암 종류에서 환자 수준 CRE 성능 비교*

1. **환자 수준 성능**: DSN-adv 모델이 13개 종양 유형 중 12개에서 최고 성능 달성, P-SDL 대비 평균 27.49%, C-MDL 대비 21.38% 성능 향상

2. **적응증 수준 성능**: 233개 소분자 약물을 13개 종양 유형(적응증)에 대해 평가하여 5배의 성능 개선 달성, DrugBank 검증 결과 거짓 음성(false negative) 제로 달성

3. **임상 검증**: 대장암(CRC) 오르가노이드 실험에서 DeepCRE가 선정한 6개 약물 후보(Set A)가 8개 중 5개 오르가노이드에서 기존 승인 약물 2개(Set C) 대비 유의미하게 높은 효과성 입증

## How

![Figure 2](figures/fig2.webp) *DeepCRE 모델의 구조와 종양 유형별 적응형 사전학습 전략*

- **도메인 분리 네트워크(DSN)**: 공유 인코더와 개인 인코더를 통해 세포주-환자 간 도메인 갭을 최소화하면서 약물별 고유 정보 보존

- **적응형 사전학습 전략**: 전체 데이터 기반의 일반적 사전학습 대신, T2 환자를 모든 세포주와 정렬하는 종양 유형 특화 사전학습으로 3.51~11.28% 추가 성능 향상

- **정렬 메트릭 활용**: 상대 최대 평균 차이(relative MMD)와 쿨백-라이블러 발산(KL divergence)을 통해 사전학습 단계별 도메인 정렬 효과 정량화

- **다층 검증**: DrugBank, ClinicalTrials, Repurposing Hub 등 3개 데이터베이스를 통한 단계적 약물 후보 검증 및 습식 실험(wet-lab assay) 수행

## Originality

- 처음으로 **환자 수준 CRE 데이터셋** 구축 및 이를 기반한 후기 단계 약물 개발 평가 모델 제시

- 컴퓨터 비전에서의 DSN을 **신약 개발 분야에 최초 적용**하여 세포주-환자 간 도메인 적응 문제 해결

- **종양 유형별 적응형 사전학습** 전략으로 일반적 전이학습의 한계를 극복하는 혁신적 접근

- SDL과 MDL 패러다임의 장점을 결합하면서 약물 인코딩과 개인화 예측을 동시에 달성

- 다양한 약물 후보군을 **체계적으로** 발굴하는 능력 입증 (단순 1-2개 약물 발굴이 아님)

## Limitation & Further Study

- **데이터 한계**: 환자 수준 데이터가 여전히 세포주 데이터에 비해 부족하며, 일부 암 종류(4개)에서는 평균 이하 성능을 보임

- **설명 가능성 부족**: 모델이 특정 약물을 추천하는 생물학적 메커니즘에 대한 심층 분석 및 해석 부재

- **암 종류 편향**: 13개 암 종류 중 특히 대장암 오르가노이드만 습식 검증되어 다양한 암 종류에 대한 검증 필요

- **임상 전이**: 모델 예측이 실제 임상시험 결과로 어떻게 전환되는지에 대한 추적 및 분석 부족

- **후속 연구 방향**:
  - 단일 세포(single-cell) 수준의 유전자발현 데이터 통합으로 도메인 정렬 정확도 향상
  - 그래프 신경망(GNN)을 활용한 약물-단백질 상호작용 네트워크 모델링
  - 다기관 임상 데이터 수집을 통한 장기 임상 검증 체계 구축


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4/5
- Significance: 4.5/5
- Clarity: 4/5
- Overall: 4.2/5

**총평**: DeepCRE는 도메인 적응 기반의 효과적인 모델로 환자 수준 약물 반응 예측에서 현저한 성능 향상을 달성했으나, 다양한 암 종류 및 대규모 임상 데이터에 대한 추가 검증과 예측 결과의 생물학적 해석 강화가 신약 개발 분야의 실제 혁신으로 이어지기 위해 필수적이다.

## Related Papers

- 🏛 기반 연구: [[papers/168_Biomni_A_General-Purpose_Biomedical_AI_Agent/review]] — 통합된 생의학 AI 에이전트 환경에서 약물 반응 예측이 핵심 구성요소로 활용될 수 있습니다.
- 🧪 응용 사례: [[papers/451_Knowledge-guided_large_language_model_for_material_science/review]] — 재료과학 LLM 방법론을 약물 발견이라는 생의학 도메인에 적용하는 학제간 접근을 보입니다.
- 🏛 기반 연구: [[papers/646_QH9_A_Quantum_Hamiltonian_Prediction_Benchmark_for_QM9_Molec/review]] — 분자 수준의 정밀한 양자 계산 데이터가 약물-세포 상호작용 모델링의 물리적 기초를 제공합니다.
- 🔗 후속 연구: [[papers/168_Biomni_A_General-Purpose_Biomedical_AI_Agent/review]] — 약물 반응 예측을 포함한 포괄적 생의학 워크플로우로 약물 개발 AI를 확장합니다.
