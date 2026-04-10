---
title: "487_Leveraging_biomolecule_and_natural_language_through_multi-mo"
authors:
  - "Qizhi Pei"
  - "Zhimeng Zhou"
  - "Kaiyuan Gao"
  - "Jinhua Zhu"
  - "Yue Wang"
date: "2024"
doi: "arXiv:2403.01528"
arxiv: ""
score: 4.2
essence: "생물분자(단백질, 분자)의 구조 정보와 자연언어 텍스트 데이터를 통합하는 다중모달 학습 방법론을 종합적으로 조사한 논문으로, AI-화학-생물학의 교차 분야에서 생물분자 표현의 새로운 패러다임을 제시한다."
tags:
  - "cat/LLM-Based_Scientific_Reasoning"
  - "sub/Domain-specific_Scientific_Reasoning"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Dou et al._2024_Leveraging biomolecule and natural language through multi-modal learning A survey.pdf"
---

# Leveraging biomolecule and natural language through multi-modal learning: A survey

> **저자**: Qizhi Pei, Zhimeng Zhou, Kaiyuan Gao, Jinhua Zhu, Yue Wang, Zun Wang, Tao Qin, Lijun Wu, Rui Yan | **날짜**: 2024 | **DOI**: [arXiv:2403.01528](https://arxiv.org/abs/2403.01528)

---

## Essence

생물분자(단백질, 분자)의 구조 정보와 자연언어 텍스트 데이터를 통합하는 다중모달 학습 방법론을 종합적으로 조사한 논문으로, AI-화학-생물학의 교차 분야에서 생물분자 표현의 새로운 패러다임을 제시한다.

## Motivation

- **Known**: 
  - 생물분자는 SMILES(1D), 그래프(2D), 3D 구조 등 다양한 형태로 표현 가능
  - PubMed, PubChem, UniProtKB 등 방대한 생물의약 문헌과 데이터베이스 존재
  - 컴퓨터 비전과 NLP의 다중모달 모델(BLIP2, LLaVA 등)이 성공적 성과 입증

- **Gap**: 
  - 현재 생물분자 모델링은 구조 정보만 활용하며, 풍부한 외부 언어 지식(biomedical literature, 주석 정보)을 체계적으로 활용하지 못함
  - 생물분자-자연언어 통합 모델링 분야에 대한 통합적인 리뷰 부재

- **Why**: 
  - 텍스트의 상징적 표현과 분자의 정량적 구조 정보를 결합하면 더 포괄적인 생물분자 이해 가능
  - 약물 발견, 성질 예측, 분자 최적화 등 다양한 응용 분야 확대

- **Approach**: 
  - 생물분자 표현 방식(1D 수열, 2D 그래프, 3D 구조) 분류
  - 다중모달 통합 프레임워크(GPT 기반 사전학습, 다중 스트림 신경망) 분석
  - 응용 사례 및 데이터셋 종합 정리
  - 미래 연구 방향 제시

## Achievement

![Figure 1](figures/fig1.webp)
*그림 1: 생물분자-언어 교차모달 통합 방법들의 계층적 분류 (모달리티 및 생물표현 기준)*

1. **종합적 분류체계**: 텍스트+분자, 텍스트+단백질, 텍스트+다중 생물표현 등 230개 이상의 모델을 체계적으로 분류하는 계층적 택소노미 제시

2. **이중 관점 분석 프레임워크**: 생물분자-언어 모델링의 목표를 "Knowledgeable(지식통합형)" vs "Versatile(다목적형)"의 두 가지 관점으로 통일하여 분석

3. **포괄적 기술 분석**: 
   - 생물분자 표현: SMILES, FASTA, 분자 그래프, 3D 좌표 등
   - 통합 방법: 이중 인코더, 융합 아키텍처, 프롬프트 기반 학습
   - 사전학습 전략: 대조 학습, 마스킹 언어 모델링, 교차모달 정렬

## How

![Figure 1](figures/fig1.webp)

- **생물분자 표현 다양화**:
  - 1D 수열: SMILES(분자), FASTA(단백질) 기반 모델
  - 2D 그래프: 원자를 노드, 화학결합을 엣지로 표현한 그래프 신경망(GNN)
  - 3D 구조: 좌표 정보를 활용한 심층학습(AlphaFold, Uni-Mol 등)

- **다중모달 통합 아키텍처**:
  - 양방향 대조 학습(contrastive learning)으로 텍스트-분자 정렬 학습
  - 융합 트랜스포머로 이종 모달리티 정보 통합
  - 지시문(instruction) 기반 미세조정으로 다양한 하위 작업 수행

- **사전학습 목표**:
  - 마스킹 언어 모델링(MLM)
  - 분자-텍스트 쌍 매칭
  - 생물분자 성질 예측

- **주요 모델 클래스**:
  - BERT 기반: BioBERT, PubMedBERT, KV-PLM (분자-텍스트 정렬)
  - GPT 기반: BioGPT, BioMedGPT, MolT5 (생성 과제)
  - 비전-언어 방식: MolCA, 3D-MoLM (다양한 표현 통합)

## Originality

- **포괄적 분류 체계의 부재 해결**: 생물분자-언어 분야의 첫 번째 체계적 리뷰로, 230+개 모델을 명확한 기준으로 분류

- **이중 목표 분석 프레임워크**: 기존 단순 분류(구조 예측 vs 언어 생성)를 넘어 "지식 깊이"와 "과제 다양성"의 이중 관점 도입

- **교차 학문적 종합**: 계산화학, 생물정보학, 자연언어처리의 관점을 통합한 최초의 통일된 분석

- **자원 집계**: 벤치마크 데이터셋, 모델, 코드 리소스를 정기적으로 업데이트하는 온라인 저장소 제공

## Limitation & Further Study

- **한계**:
  - 3D 구조 정보의 제한된 가용성으로 인한 실무 적용 어려움
  - 대규모 정렬된 생물분자-텍스트 데이터셋의 부족
  - 생물분자의 동적 특성(단백질 구조 변화 등) 미흡한 모델링
  - 생성된 분자의 생물 활성 검증 절차 부재

- **후속 연구 필요 영역**:
  - 약사 일관성(pharmacological consistency) 검증을 위한 실험 검증 통합
  - 다중 단백질 복합체, 세포 수준의 생물분자 시스템 모델링
  - 설명 가능성(interpretability) 향상으로 생물학적 인사이트 도출
  - 희귀 질병 약물 발견 등 저자원 환경 적용
  - 대규모 멀티리링게이 생물분자-언어 데이터셋 구축

## Evaluation

- **Novelty**: 4.5/5
  - 종합적이고 체계적인 첫 리뷰로, 이중 관점 프레임워크 신참 (다만 개별 모델의 기술적 참신성은 논문이 아닌 각 모델 단위)

- **Technical Soundness**: 4/5
  - 기술 분류와 분석이 견고하나, 심화된 방법론 비교보다는 개요 중심

- **Significance**: 4.5/5
  - 약물 발견, 분자 최적화 등 중요 응용 분야 다수
  - AI4Science 교차 분야 발전에 높은 영향력

- **Clarity**: 4/5
  - 계층적 분류와 시각적 표현이 명확하나, 230+개 모델 나열로 인한 정보 과부하

- **Overall**: 4.2/5

**총평**: 본 논문은 급속도로 성장하는 생물분자-자연언어 통합 학습 분야에서 첫번째 체계적 리뷰를 제공하며, 명확한 분류체계와 이중 목표 분석 틀로 학제 간 연구자들에게 유용한 나침반 역할을 한다. 다만 개별 방법론에 대한 심화 비교 분석과 실제 생물학적 검증 통합이 강화되면 더욱 임팩트 있는 리뷰가 될 수 있다.

## Related Papers

- 🏛 기반 연구: [[papers/1060_Accurate_prediction_of_protein_structures_and_interactions_u/review]] — 단백질 구조 예측 연구가 생물분자 다중모달 학습의 핵심 기반 기술
- 🔄 다른 접근: [[papers/439_Invariant_Tokenization_of_Crystalline_Materials_for_Language/review]] — 생물분자 vs 결정 구조로 대상은 다르지만 동일한 다중모달 토큰화 접근법
- 🔗 후속 연구: [[papers/343_Foundation_models_for_materials_discovery__current_state_and/review]] — 재료과학 파운데이션 모델을 생물분자 영역으로 확장한 연구
- 🔄 다른 접근: [[papers/345_Foundation_Molecular_Grammar_Multi-Modal_Foundation_Models_I/review]] — 분자 문법 기반 파운데이션 모델과 생물분자 다중모달 학습의 대조적 방법론
- 🔄 다른 접근: [[papers/439_Invariant_Tokenization_of_Crystalline_Materials_for_Language/review]] — 결정 구조 vs 생물분자로 대상은 다르지만 동일한 다중모달 토큰화 접근법
- 🔗 후속 연구: [[papers/1060_Accurate_prediction_of_protein_structures_and_interactions_u/review]] — 단백질 구조 예측을 생물분자 다중모달 학습으로 확장한 포괄적 연구
- 🏛 기반 연구: [[papers/345_Foundation_Molecular_Grammar_Multi-Modal_Foundation_Models_I/review]] — 생체분자와 자연어의 멀티모달 결합 방법론이 분자 이미지와 텍스트 표현 통합의 핵심 기반이 됨
