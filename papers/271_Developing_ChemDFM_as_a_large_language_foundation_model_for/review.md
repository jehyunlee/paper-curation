---
title: "271_Developing_ChemDFM_as_a_large_language_foundation_model_for"
authors:
  - "Zihan Zhao"
  - "Da Ma"
  - "Lu Chen"
  - "Liangtai Sun"
  - "Zihao Li"
date: "2024"
doi: "10.1016/j.xcrp.2025.102523"
arxiv: ""
score: 4.25
essence: "화학 분야의 다양한 작업을 처리할 수 있는 대규모 언어 모델 ChemDFM을 개발했으며, GPT-4를 능가하는 성능을 달성하면서도 화학 분야의 자유로운 대화형 AI 조수 역할을 수행할 수 있다."
tags:
  - "cat/Cognitive_AI_Evaluation_and_Benchmarking"
  - "sub/Evolutionary_Chemistry_Models"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Zhao et al._2024_Developing ChemDFM as a large language foundation model for chemistry.pdf"
---

# Developing ChemDFM as a large language foundation model for chemistry

> **저자**: Zihan Zhao, Da Ma, Lu Chen, Liangtai Sun, Zihao Li | **날짜**: 2024 | **DOI**: [10.1016/j.xcrp.2025.102523](https://doi.org/10.1016/j.xcrp.2025.102523)

---

## Essence

![Figure 1](figures/fig1.webp)
*화학 분야 LLM 개발을 위한 일반 영역 LLM에 화학 도메인 지식을 통합하는 개념도*

화학 분야의 다양한 작업을 처리할 수 있는 대규모 언어 모델 ChemDFM을 개발했으며, GPT-4를 능가하는 성능을 달성하면서도 화학 분야의 자유로운 대화형 AI 조수 역할을 수행할 수 있다.

## Motivation

- **Known**: 최근 대규모 언어 모델(LLM)은 자연어 처리에서 놀라운 성공을 이루었으며, 우수한 작업 일반화(task generalization)와 자유형식 대화 능력을 보여주었다. 화학 분야의 기존 AI 모델들은 특정 작업을 위해 별도로 학습·튜닝이 필요한 전문화된 모델들이다.

- **Gap**: 일반 영역 LLM은 화학 도메인의 지식이 부족하여 화학 작업에서 성능이 크게 제한된다. SMILES, IUPAC 명명법, 분자식 같은 화학 특화 표기법의 의미를 제대로 이해하지 못하고, 이로 인해 할루시네이션(hallucination) 문제가 발생하기 쉽다.

- **Why**: 화학 분야를 위한 범용 AI 모델의 필요성이 있다. 다양한 화학 작업을 처리하고 자유형식의 인간-AI 협업을 지원하며, 최종적으로 '화학 인공일반지능(Chemical AGI)'으로 나아가기 위한 단계가 필요하다.

- **Approach**: LLaMA-13B 기반으로 두 단계 훈련을 통해 화학 지식을 통합한다: (1) 도메인 사전 훈련(Domain Pre-training)으로 화학 논문과 교과서에서 지식을 획득하고, (2) 명령어 튜닝(Instruction Tuning)으로 화학 언어 패턴과 분자 표기법에 익숙하게 한다.

## Achievement

![Figure 2](figures/fig2.webp)
*ChemDFM의 두 단계 훈련 절차와 지원하는 다양한 작업*

1. **포괄적 화학 능력**: 분자 인식, 분자 설계, 분자 성질 예측, 반응 분석, 수율 예측, 역합성 등 다양한 화학 작업을 처리할 수 있으며, 미지의 상황에서의 추론과 오류 수정도 가능하다.

2. **우수한 성능**: ChemDFM-13B가 대부분의 오픈소스 LLM을 능가하며, 모델 크기의 현저한 차이에도 불구하고 많은 화학 작업에서 GPT-4의 성능을 초과한다.

3. **실제 시나리오 적응성**: 최신 화학 논문 기반의 미지의 상황(unseen scenarios)에서도 더 정확하고 관련성 높은 답변을 생성하여 데이터 누수를 방지하면서도 실무 적용성을 입증한다.

## How

![Figure 3](figures/fig3.webp)
*명령어 튜닝에 사용된 화학 반응 완성 작업의 예시*

- **도메인 사전 훈련 데이터**: 
  - 1.4K개 화학 교과서(LibreTexts, Gold Books)에서 49M 토큰
  - 2022년 1월 이전 3.9M개 오픈 액세스 화학 논문에서 34B 토큰
  - 일반 영역 데이터(Wikipedia, Arxiv, Books, StackExchange 등)를 포함하여 일반 지식 유지

- **명령어 튜닝 데이터 (총 2.7M개)**:
  - 자연언어 QA 쌍 (1.0M): 기존 QA 데이터셋(ARC, PIQA, SciQ) 및 중학 시험 문제
  - 분자 기반 작업 (1.7M):
    - 분자 기술(MD): PubChem에서 SMILES-설명 쌍 (576K)
    - 텍스트 기반 분자 설계(TBMD): 역방향 생성 (576K)
    - 분자 성질 예측(MPP): MoleculeNet 기반 (102K)
    - 반응 완성(RC): USPTO 데이터셋 (300K)
    - 분자 표기법 정렬(MNA): PubChem (120K)

- **학습 전략**:
  - SMILES를 주요 분자 표현으로 선택 (텍스트 호환성 우수, 입체화학 정보 보존)
  - 화학 특화 표기법 이해를 위한 3가지 데이터 유형(분자 기술, 성질 예측, 반응 완성)
  - 일반 영역 데이터와 화학 도메인 데이터의 균형 유지

## Originality

- **첫 번째 대규모 화학 기초 모델**: 34B 토큰의 화학 논문과 2.7M개의 화학 명령어로 훈련한 최초의 대규모 화학 LLM

- **이중 층 특화 전략**: 도메인 사전 훈련 + 명령어 튜닝의 체계적 접근으로, 단순 미세조정을 넘어 화학 지식을 깊이 있게 통합

- **화학 표기법 특화**: SMILES 기반의 분자 표현을 중심으로 분자 기술, 설계, 성질 예측, 반응 완성 등 다양한 화학 작업을 통합

- **포괄적 평가 및 오픈소스 공개**: 추론 코드, 평가 데이터셋, 모델 가중치를 HuggingFace에 공개하여 커뮤니티 기여

- **실제 시나리오 검증**: 데이터 누수 방지를 위해 최신 화학 논문 기반의 미지의 상황 테스트 수행

## Limitation & Further Study

- **모델 크기 제약**: 13B 파라미터로 제한되어 있으며, 더 큰 모델의 성능 향상 가능성이 남아있다.

- **분자 표현의 한계**: SMILES 표기법만 주로 사용되어 3D 구조 정보나 다른 화학 표현 형식(3D 좌표, 단백질 구조 등)의 이해가 부족할 수 있다.

- **평가 범위 확대 필요**: 더 다양한 화학 분야(재료 과학, 약물 발견, 계산 화학 등)에 대한 평가가 추가로 필요하다.

- **멀티모달 확장**: 화학 이미지, 분자 구조 시각화 등 멀티모달 정보 처리 능력 개발이 향후 과제이다.

- **화학 안전성과 신뢰성**: 위험한 합성 경로나 물질에 대한 안전 필터링 메커니즘 강화가 필요하다.

## Evaluation

- **Novelty**: 4.5/5
  - 화학 도메인 특화 LLM 개발의 선구적 시도이나, 기본 방법론(사전 훈련 + 명령어 튜닝)은 기존 기법의 응용

- **Technical Soundness**: 4/5
  - 체계적인 두 단계 훈련 및 포괄적 데이터 구성이 건전하나, 기술적 혁신성은 제한적

- **Significance**: 4.5/5
  - 화학 연구의 AI 지원을 위한 실질적 기여로, 학술 및 산업적 영향력이 큼

- **Clarity**: 4/5
  - 전반적으로 명확한 설명이나, 세부 훈련 하이퍼파라미터 및 일부 기술적 세부사항 기술 부족

- **Overall**: 4.25/5

**총평**: ChemDFM은 화학 분야의 LLM 개발에 있어 중요한 이정표를 세우며, 광범위한 화학 지식 통합과 우수한 실증 성능을 통해 AI 화학자의 실현 가능성을 보여준다. 다만, 분자 표현의 다양성 확대와 멀티모달 확장 등의 후속 개선이 필요하다.

## Related Papers

- 🔄 다른 접근: [[papers/210_ChemCrow_Augmenting_large-language_models_with_chemistry_too/review]] — 화학 분야 LLM의 다른 구현 방식으로 도구 통합 vs 파운데이션 모델 접근
- 🏛 기반 연구: [[papers/025_A_Survey_of_AI_for_Materials_Science_Foundation_Models_LLM_A/review]] — 재료과학 AI 조사가 화학 LLM 개발의 광범위한 맥락을 제공함
- 🔗 후속 연구: [[papers/382_Genome_modeling_and_design_across_all_domains_of_life_with_E/review]] — 화학 분야 LLM과 유전체 모델링을 결합한 더 큰 생명과학 프레임워크 구축 가능
- 🔄 다른 접근: [[papers/210_ChemCrow_Augmenting_large-language_models_with_chemistry_too/review]] — 화학 AI 에이전트의 다른 구현 방식으로 도구 통합 vs 파운데이션 모델
- 🧪 응용 사례: [[papers/167_Biomedlm_A_27_b_parameter_language_model_trained_on_biomedic/review]] — 화학 분야 대형 언어 파운데이션 모델 개발에 생명의학 모델 적용
- 🏛 기반 연구: [[papers/226_ClinicalGPT_Large_Language_Models_Finetuned_with_Diverse_Med/review]] — 화학 분야 대형 언어 기초 모델 개발 경험이 의료 분야 특화 모델 구축에 필요한 도메인 적응 전략을 제공한다.
