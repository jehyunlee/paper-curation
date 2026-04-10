---
title: "696_Scaling_Large_Language_Models_for_Next-Generation_Single-Cel"
authors:
  - "Syed Asad Rizvi"
  - "Daniel Levine"
  - "Aakash Patel"
  - "Shiyang Zhang"
  - "Eric Wang"
date: "2025.04"
doi: "10.1101/2025.04.14.648850"
arxiv: ""
score: 4.6
essence: "단일세포 RNA 시퀀싱 데이터를 \"세포 문장(cell sentence)\" 형태의 텍스트로 변환하여 대규모언어모델(LLM)로 처리하는 Cell2Sentence 프레임워크를 270억 개의 파라미터로 확장함으로써, 전사체 데이터와 생물학적 텍스트 정보를 통합한 차세대 단일세포 분석 플랫폼을 구현했다."
tags:
  - "cat/AI-Powered_Scientific_Research_Frameworks"
  - "sub/Single-cell_RNA_Sequencing"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Rizvi et al._2025_Scaling Large Language Models for Next-Generation Single-Cell Analysis.pdf"
---

# Scaling Large Language Models for Next-Generation Single-Cell Analysis

> **저자**: Syed Asad Rizvi, Daniel Levine, Aakash Patel, Shiyang Zhang, Eric Wang, Curtis Jamison Perry, Ivan Vrkic, Nicole Mayerli Constante, Zirui Fu, Sizhuang He, David Zhang, Cerise Tang, Zhuoyang Lyu, Rayyan Darji, Chang Li, Emily Sun, David Jeong, Lawrence Zhao, Jennifer Kwan, David Braun, Brian Hafler, Hattie Chung, Rahul M. Dhodapkar, Paul Jaeger, Bryan Perozzi, Jeffrey Ishizuka, Shekoofeh Azizi, David Van Dijk | **날짜**: 2025-04-17 | **DOI**: [10.1101/2025.04.14.648850](https://doi.org/10.1101/2025.04.14.648850)

---

## Essence

![Figure 2](figures/fig2.webp)
*Figure 2: C2S-Scale는 scRNA-seq 데이터와 자연언어를 통합하여 LLM을 이용한 단일세포 분석 수행*

단일세포 RNA 시퀀싱 데이터를 "세포 문장(cell sentence)" 형태의 텍스트로 변환하여 대규모언어모델(LLM)로 처리하는 Cell2Sentence 프레임워크를 270억 개의 파라미터로 확장함으로써, 전사체 데이터와 생물학적 텍스트 정보를 통합한 차세대 단일세포 분석 플랫폼을 구현했다.

## Motivation

- **Known**: 기존 단일세포 재단 모델(scFM: scGPT, Geneformer, scFoundation 등)은 높은 성능을 보이지만, 맞춤형 아키텍처로 인해 확장성이 제한되고 다양한 모달리티(modality) 통합이 어려우며 텍스트 정보 네이티브 통합이 불가능
- **Gap**: 현존하는 표현식-전용(expression-only) 재단 모델들은 다중 데이터셋, 모달리티, 생물학적 맥락 간 통찰 종합 능력 부재
- **Why**: 단일세포 분석의 복잡한 작업들(섭동 반응 예측, 다중세포 문맥 분석 등)은 강력한 스케일링 특성과 텍스트 통합 능력을 갖춘 모델 필요
- **Approach**: LLM의 견고한 스케일링 행동(scaling behavior)과 일반화 능력을 활용하되, Cell2Sentence 데이터 엔지니어링으로 고차원 발현 데이터를 텍스트로 변환하여 기존 LLM 인프라 활용

## Achievement

![Figure 1](figures/fig1.webp)
*Figure 1: C2S 프레임워크의 다차원적 확장 - 모델 용량, 데이터 크기, 다중 모달리티, 다중세포 지원, 생물학적 스케일 통합*

1. **확장 가능한 LLM 아키텍처**: 410M에서 27B 파라미터까지 5개 모델 크기에서 일관된 성능 향상 달성. Gemma-2 및 Pythia 기반 모델로 기존 단일세포 모델 대비 압도적 규모 확대

2. **대규모 다중모달 학습 데이터**: 5천만 개 이상의 인간 및 마우스 세포의 10억 개 토큰 코퍼스 구성 - Human Cell Atlas, CellxGene 통합. 전사체 데이터+생물학적 텍스트+메타데이터 동시 학습

3. **다양한 다운스트림 작업 성능**: 세포 타입 주석(cell type annotation), 세포 임베딩(cell embedding), 섭동 반응 예측, 자연언어 해석, 공간 추론(spatial reasoning), 질의응답(QA) 등 전방위 우수 성능

4. **강화학습 기반 성능 향상**: Group Relative Policy Optimization (GRPO)을 적용하여 목표 특정 작업 성능 추가 개선. 특히 복잡한 질의응답 벤치마크에서 현저한 개선

5. **신규 평가 지표 제안**: 단일세포 Fréchet Inception Distance (scFID) 개발 - 표현식 수준의 노이즈에 덜 민감한 생물학적으로 의미 있는 생성 모델 평가 방법

![Figure 3](figures/fig3.webp)
*Figure 3: C2S-Scale이 전사체 재단 모델과 일반 LLM을 모두 능가한 다양한 작업 성능*

## How

![Figure 4](figures/fig4.webp)
*Figure 4: 모델 용량 증가에 따른 일관된 스케일링 성능*

- **데이터 표현 변환**: 각 세포의 발현 유전자를 발현량 내림차순으로 정렬하여 "세포 문장" 생성 - 상대적 위치와 원본 발현 간의 강한 관계로 최소 정보 손실
- **이단계 학습**: (1) 자가지도학습(self-supervised) 기반 일반 사전학습 (2) 특정 작업별 추가 미세조정(fine-tuning)
- **150M 다중작업 학습 샘플 구성**: Table 1의 다양한 작업 샘플로 LLM이 문장 모델링과 프롬프트 지시 따름을 동시 학습
- **확장 문맥 길이(8192 토큰)**: 다중세포 입력, 생물학적 주석, 원문 텍스트, 섭동 조건, 상세 작업 지시 통합 가능
- **GRPO 기반 강화학습 적용**: 사용자 선호도 정렬을 위한 강화학습으로 특정 단일세포 작업 성능 추가 최적화

## Originality

- **LLM의 텍스트 기반 단일세포 데이터 표현 방식의 혁신적 확장**: Cell2Sentence 개념을 27B 파라미터 규모로 확장하여 단순한 미세조정을 넘어 기본적 LLM 아키텍처 활용 가능하도록 입증

- **전사체-자연언어 통합의 사상 초유 규모**: 50M 세포+생물학적 논문 텍스트 결합으로 진정한 다중모달 학습 실현 - 기존 발현식 전용 모델과 본질적 차별성

- **다중세포 문맥 처리 능력**: 단일 세포 분석을 넘어 세포-세포 상호작용, 복잡한 생물학적 프로세스를 다중세포 입력으로 처리하는 새로운 분석 패러다임 제시

- **강화학습의 단일세포 생물학 적용**: GRPO를 단일세포 섭동 예측 및 QA 작업에 처음 적용하여 NLP 기법의 생물학 영역 신규 응용

- **scFID 평가 지표의 개발**: FID를 단일세포 생성 모델 평가에 맞춤화하여 고차원 잡음 영향 최소화하는 생물학적으로 의미 있는 평가 방법 제시

## Limitation & Further Study

- **벤치마크 제한성**: 평가가 주로 공개 데이터 아틀라스(CellxGene, HCA)에 편중되어 있어, 특정 질병 상태(rare disease) 데이터나 특이적 실험 조건에 대한 모델 성능 검증 필요

- **해석가능성 부족**: 텍스트 기반 변환 후 LLM의 의사결정 과정이 블랙박스화되는 경향으로, 예측의 생물학적 타당성에 대한 상세 해석 메커니즘 개발 필요

- **계산 비용**: 27B 파라미터 모델의 추론 및 미세조정에 상당한 GPU 리소스 요구 - 소규모 연구기관의 접근성 제한 가능성

- **유전자 순서 정보 손실**: 발현량 순서만 유지하고 정확한 발현값(TPM, counts 등)은 손실되는 설계 - 미묘한 발현 수준 차이를 구별해야 하는 작업에서 한계

- **후속 연구 방향**:
  - 희귀 질병, 종양 미세환경 등 특수 데이터셋에 대한 도메인 특화 모델 개발
  - Attention mechanism 분석을 통한 모델 해석가능성 강화
  - 매개변수 효율적 학습(LoRA, adapter) 기법으로 계산 장벽 완화
  - 정량적 발현값 복원 기술 개발로 정밀 분석 능력 향상
  - 다중 생물학적 모달리티(단백질, 공간 정보, 이미지) 통합 확장


## Evaluation

- Novelty: 5/5
- Technical Soundness: 4.5/5
- Significance: 5/5
- Clarity: 4/5
- Overall: 4.6/5

**총평**: 이 논문은 대규모 LLM의 스케일링 효과를 단일세포 생물학에 처음 체계적으로 입증하고, 전사체 데이터와 자연언어의 통합을 전례 없는 규모(50M 세포, 1B 토큰)로 달성한 획기적 연구이다. Cell2Sentence 프레임워크의 우아한 설계, GRPO 강화학습 응용, scFID 평가 지표 개발 등에서 높은 독창성을 보이며, 공개 모델 및 자원 공개로 생물학 커뮤니티에 실질적 기여를 할 것으로 예상된다. 다만 해석가능성 부재와 계산 비용 측면에서는 개선이 필요하며, 논문의 일부 기술적 세부사항(특히 GRPO 적용 방식, scFID 검증 방법)이 다소 간략하게 기술된 점이 아쉽다.

## Related Papers

- 🔗 후속 연구: [[papers/431_Integrated_analysis_of_multimodal_single-cell_data/review]] — 단일세포 데이터를 텍스트로 변환하는 접근법이 멀티모달 단일세포 데이터 통합 분석을 위한 새로운 방법론적 확장을 제공한다
- 🔄 다른 접근: [[papers/161_BioBERT_a_pre-trained_biomedical_language_representation_mod/review]] — 단일세포 데이터 텍스트 변환 방식과 생의학 텍스트 전용 언어모델이 생의학 빅데이터 처리의 상반된 접근법을 보여준다
- 🧪 응용 사례: [[papers/193_CellAgent_An_LLM-driven_Multi-Agent_Framework_for_Automated/review]] — 대규모 언어모델을 활용한 단일세포 분석이 세포 생물학 연구 자동화를 위한 멀티 에이전트 시스템에 핵심적으로 활용될 수 있다
- 🏛 기반 연구: [[papers/700_scBaseCount_an_AI_agent-curated_uniformly_processed_and_auto/review]] — 단일세포 데이터의 LLM 처리 기술이 AI 에이전트 기반 단일세포 데이터베이스 구축과 표준화에 필수적인 기반 기술을 제공한다
- 🏛 기반 연구: [[papers/483_Learning_to_Discover_Regulatory_Elements_for_Gene_Expression/review]] — 단일 세포 분석을 위한 대규모 언어모델이 유전자 발현 예측의 기반을 제공합니다.
- 🔄 다른 접근: [[papers/161_BioBERT_a_pre-trained_biomedical_language_representation_mod/review]] — 생의학 텍스트 전용 BERT와 단일세포 데이터를 텍스트로 변환하여 처리하는 LLM이 생의학 데이터 처리의 서로 다른 접근법을 보여준다
- 🔄 다른 접근: [[papers/302_Effective_gene_expression_prediction_from_sequence_by_integr/review]] — DNA 서열 기반 유전자 발현 예측과 단일세포 데이터의 텍스트 변환 처리가 유전체학 빅데이터 분석의 서로 다른 접근법을 보여준다
- 🏛 기반 연구: [[papers/431_Integrated_analysis_of_multimodal_single-cell_data/review]] — 멀티모달 단일세포 데이터 통합 분석 방법론이 단일세포 데이터의 대형언어모델 처리를 위한 중요한 생물학적 기반을 제공한다
- 🏛 기반 연구: [[papers/700_scBaseCount_an_AI_agent-curated_uniformly_processed_and_auto/review]] — 단일세포 데이터의 대규모 언어모델 스케일링을 위한 고품질 훈련 데이터 기반을 제공한다
- 🔗 후속 연구: [[papers/344_Foundation_models_in_bioinformatics/review]] — 단일 세포 분석을 위한 대형 언어 모델 확장이 생물정보학 기초 모델의 구체적 응용 사례입니다.
- 🏛 기반 연구: [[papers/699_SCANPY_large-scale_single-cell_gene_expression_data_analysis/review]] — 대규모 단일세포 데이터 처리 기술이 차세대 LLM 기반 분석의 기초가 된다.
- 🏛 기반 연구: [[papers/306_Efficient_fine-tuning_of_single-cell_foundation_models_enabl/review]] — 대규모 언어모델과 단일세포 분석의 통합적 접근법에 대한 기반을 제공한다
