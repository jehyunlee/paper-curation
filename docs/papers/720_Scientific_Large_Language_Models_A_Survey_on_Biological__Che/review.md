---
title: "720_Scientific_Large_Language_Models_A_Survey_on_Biological__Che"
authors:
  - "Qiang Zhang"
  - "Keyang Ding"
  - "Tianwen Lyv"
  - "Xinda Wang"
  - "Qingyu Yin"
date: "2024.01"
doi: ""
arxiv: ""
score: 4.4
essence: "본 논문은 생물학 및 화학 분야의 특화된 과학 언어를 처리하도록 설계된 대규모 언어 모델(과학 LLM)에 대한 최초의 포괄적 조사연구다. 텍스트, 분자(SMILES, SELFIES), 단백질(아미노산 서열), 게놈(DNA 서열) 및 이들의 멀티모달 조합을 다루며, 모델 아키텍처, 학습 데이터셋, 평가 방법론을 상세히 분석한다."
tags:
  - "cat/AI-Powered_Scientific_Research_Frameworks"
  - "sub/Biological_Foundation_Models"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Zhang et al._2024_Scientific Large Language Models A Survey on Biological & Chemical Domains.pdf"
---

# Scientific Large Language Models: A Survey on Biological & Chemical Domains

> **저자**: Qiang Zhang, Keyang Ding, Tianwen Lyv, Xinda Wang, Qingyu Yin, Yiwen Zhang, Jing Yu, Yuhao Wang, Xiaotong Li, Zhuoyi Xiang, Kehua Feng, Xiang Zhuang, Zeyuan Wang, Ming Qin, Mengyao Zhang, Jinlu Zhang, Jiyu Cui, Tao Huang, Pengju Yan, Renjun Xu | **날짜**: 2024-01-26

---

## Essence

![Figure 2](figures/fig2.webp) *생물 및 화학 영역의 과학적 언어(분자, 단백질, 게놈, 텍스트) 및 멀티모달 조합을 포괄하는 과학 LLM의 연구 범위*

본 논문은 생물학 및 화학 분야의 특화된 과학 언어를 처리하도록 설계된 대규모 언어 모델(과학 LLM)에 대한 최초의 포괄적 조사연구다. 텍스트, 분자(SMILES, SELFIES), 단백질(아미노산 서열), 게놈(DNA 서열) 및 이들의 멀티모달 조합을 다루며, 모델 아키텍처, 학습 데이터셋, 평가 방법론을 상세히 분석한다.

## Motivation

- **Known**: 
  - 일반 LLM(GPT-3, GPT-4)은 자연언어 처리에 뛰어남
  - 분자, 단백질, 게놈 등 과학 언어에는 독특한 어휘와 문법 규칙 존재
  - 예: "C"는 자연언어에서는 문자이나 단백질 언어에서는 시스테인(Cysteine), SMILES에서는 탄소(Carbon)를 의미

- **Gap**: 
  - 과학 언어별 LLM 발전이 각 도메인 내에서만 탐색됨
  - 분자, 단백질, 게놈, 멀티모달 LLM을 통합하는 체계적 리뷰 부재
  - 텍스트와 과학 언어의 상호작용을 다루는 포괄적 분석 없음

- **Why**: 
  - Wittgenstein의 언어 철학: "언어의 한계는 세계의 한계"
  - 일반 LLM의 세계는 자연언어에 제한되며, 과학 언어 처리에는 특화된 모델 필요

- **Approach**: 
  - 생물/화학 영역의 과학 LLM을 포괄적으로 조사
  - 텍스트, 분자, 단백질, 게놈, 멀티모달 5가지 카테고리로 분류
  - 각 카테고리별 모델 아키텍처, 능력(downstream task), 데이터셋, 평가 방법론 분석

## Achievement

![Figure 3](figures/fig3.webp) *과학 LLM의 진화 트리: 텍스트 LLM, 분자 LLM, 단백질 LLM, 게놈 LLM, 멀티모달 LLM의 아키텍처별(Encoder-Only, Decoder-Only, Encoder-Decoder) 발전 흐름*

1. **포괄적 분류 체계**: 
   - 5개 카테고리(텍스트, 분자, 단백질, 게놈, 멀티모달)로 과학 LLM 체계화
   - 3가지 아키텍처 유형(Encoder-Only, Decoder-Only, Encoder-Decoder)별 분류

2. **구체적 모델 아키텍처 분석**: 
   - 분자 LLM: ChemBERTa, MolBERT, Uni-Mol, Molformer 등 30+개 모델
   - 단백질 LLM: ESM 시리즈, ProtTrans, SaProt 등 15+개 모델
   - 게놈 LLM: 게놈 서열 특화 모델군

3. **데이터셋 및 평가 벤치마크 종합**:
   - 각 도메인별 주요 학습 데이터셋 목록화
   - 분자 특성 예측, 단백질 구조 예측, 게놈 기능 예측 등 평가 기준 제시

4. **멀티모달 LLM의 첫 체계적 탐색**:
   - 텍스트와 분자/단백질/게놈 간의 교차 영역 상호작용 분석
   - 기존 리뷰에서 다루지 않은 영역 개척

## How

![Figure 1](figures/fig1.webp) *일반 LLM이 분자, RNA, 아미노산 서열 등 과학 언어를 효과적으로 처리하지 못하는 사례*

- **과학 언어 정의**:
  - 분자 언어: SMILES(Simplified Molecular Input Line Entry System), SELFIES(Self-Referencing Embedded Strings), InChI
  - 단백질 언어: 20개 표준 아미노산으로 구성된 서열
  - 게놈 언어: A, T, G, C 뉴클레오티드 서열
  - 텍스트 언어: 화학/생물학 도메인 자연언어(논문, 특허, 교과서)

- **모델 아키텍처 분석**:
  - **Encoder-Only** (BERT 계열): 분자 특성 분류, 단백질 구조 예측
  - **Decoder-Only** (GPT 계열): 분자 생성, 단백질 설계
  - **Encoder-Decoder** (Transformer 계열): 분자 변환 반응(retrosynthesis), 단백질 기능 예측

- **학습 방법론**:
  - 사전학습(Pre-training): 대규모 unlabeled 데이터(분자 DB, 게놈 시퀀스 DB)에서의 자기지도학습
  - 미세조정(Fine-tuning): 특정 downstream task에 대한 지도학습

- **평가 방법론**:
  - 판별 과제(Discriminative): 분류, 회귀 정확도(Accuracy, R²)
  - 생성 과제(Generative): 분자 생성 유효성(Validity), 다양성(Diversity), 신규성(Novelty)

## Originality

- **최초성**: 
  - 과학 LLM 분야의 첫 종합 리뷰 논문
  - 분자, 단백질, 게놈 LLM을 단일 프레임워크로 통합 분석

- **통합적 관점**: 
  - 개별 도메인 연구를 넘어 과학 언어의 공통 특성 강조
  - "과학 언어"라는 개념 정립 및 형식화

- **멀티모달 영역 개척**: 
  - 텍스트-분자, 텍스트-단백질, 분자-단백질 간 교차 모달 상호작용 최초 분석
  - 기존 리뷰에서 전혀 다루지 않은 영역

- **실용적 자원 제공**: 
  - GitHub에서 오픈 소스 모델, 데이터셋, 벤치마크 종합 자료 유지
  - 연구자 커뮤니티의 접근성 향상

## Limitation & Further Study

- **범위의 제한성**:
  - 수학 언어(명확한 어휘/문법 부재로 제외) 미포함
  - Graph Neural Network, Diffusion Model 등 비-Transformer 아키텍처 제외
  - 생물/화학 영역에 국한, 물리학·재료과학 등 다른 과학 도메인 미포함

- **평가 방법론의 한계**:
  - 도메인별 평가 기준 불균형: 단백질은 구조 정확도, 분자는 생성 유효성 등 이질적 평가 척도
  - 실제 과학적 유용성(약물 활성, 단백질 기능)과 모델 성능 간의 괴리 미분석

- **후속 연구 방향**:
  1. **멀티모달 성능 향상**: 텍스트-분자-단백질-게놈 간 더 정교한 교차 정렬(cross-alignment) 메커니즘 개발
  2. **생물물리학적 제약 통합**: 열역학, 동역학 물리 법칙을 신경망에 제약 조건으로 통합
  3. **도메인 간 전이학습**: 분자 사전학습이 단백질 작업에 기여하는 정도 정량화
  4. **실험적 검증**: 모델 예측 결과의 실제 생화학 실험 검증 시스템 구축
  5. **해석 가능성(Interpretability)**: Black-box 모델의 의사결정 근거를 화학/생물학 메커니즘으로 설명 가능하게 개선


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4/5
- Significance: 4.5/5
- Clarity: 4.5/5
- Overall: 4.4/5

**총평**: 본 논문은 빠르게 성장하는 과학 LLM 분야의 첫 포괄적 리뷰로, 분자·단백질·게놈·멀티모달 영역을 통합 분석한 점에서 기여도가 크다. 다만 이론적 혁신보다는 기존 모델들의 체계적 종합에 가까우며, 도메인 간 비교 분석 및 실제 과학적 임팩트 검증은 향후 과제로 남아있다.

## Related Papers

- 🏛 기반 연구: [[papers/025_A_Survey_of_AI_for_Materials_Science_Foundation_Models_LLM_A/review]] — 재료과학 분야 AI 연구의 포괄적 기반을 제공하여 생물학/화학 특화 LLM과 상호 보완한다
- 🔄 다른 접근: [[papers/465_Large_Language_Model_in_Materials_Science_Roles_Challenges_a/review]] — 재료과학에서 LLM 활용에 대해 생물학/화학과는 다른 도전과제와 기회를 제시한다
- 🧪 응용 사례: [[papers/167_Biomedlm_A_27_b_parameter_language_model_trained_on_biomedic/review]] — 생의학 특화 언어모델의 성공 사례를 생물학/화학 분야 LLM 개발에 참고할 수 있다
- 🔗 후속 연구: [[papers/004_A_Comprehensive_Survey_of_Scientific_Large_Language_Models_a/review]] — 생물학과 화학 분야 과학 LLM에 특화된 조사로 포괄적 조사를 세분화하여 심화한다.
- 🏛 기반 연구: [[papers/161_BioBERT_a_pre-trained_biomedical_language_representation_mod/review]] — 생의학 도메인 특화 언어모델의 초기 연구로서 이후 과학 분야 대형언어모델 발전의 중요한 기반이 되었다
- 🔄 다른 접근: [[papers/359_From_large_language_models_to_multimodal_ai_A_scoping_review/review]] — 생의학 분야 멀티모달 AI와 생물학/화학 특화 언어모델이라는 다른 접근으로 의료 AI를 발전시킨다
- 🔄 다른 접근: [[papers/029_A_Survey_of_Scientific_Large_Language_Models_From_Data_Found/review]] — 생물학과 화학 분야 과학 LLM에 대한 다른 관점의 종합 조사를 제시한다.
- 🔗 후속 연구: [[papers/025_A_Survey_of_AI_for_Materials_Science_Foundation_Models_LLM_A/review]] — 생물학적 화학적 과학 LLM 서베이가 AI 소재 과학 서베이의 생명과학 응용 분야를 보완하고 확장함
- 🔄 다른 접근: [[papers/167_Biomedlm_A_27_b_parameter_language_model_trained_on_biomedic/review]] — 생물학과 화학 분야 과학 LLM 조사와 생명의학 특화 모델의 다른 접근법
- 🏛 기반 연구: [[papers/707_SciBERT_A_Pretrained_Language_Model_for_Scientific_Text/review]] — SciBERT가 보여준 과학 도메인 적응의 성공이 과학 특화 LLM 발전의 기초가 됨
- 🔗 후속 연구: [[papers/367_Galactica_A_Large_Language_Model_for_Science/review]] — 생물학과 화학 분야 과학 언어모델 연구의 포괄적 확장 사례
- 🔗 후속 연구: [[papers/723_Sciglm_Training_scientific_language_models_with_self-reflect/review]] — 생물학 및 화학 분야의 과학 대규모 언어 모델에 대한 포괄적인 조사로서 SciGLM의 연구를 더 넓은 맥락에서 이해할 수 있게 한다.
