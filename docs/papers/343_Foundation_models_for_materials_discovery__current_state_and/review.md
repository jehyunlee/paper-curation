---
title: "343_Foundation_models_for_materials_discovery__current_state_and"
authors:
  - "Edward O. Pyzer-Knapp"
  - "Matteo Manica"
  - "Peter Staar"
  - "Lucas Morin"
  - "Patrick Ruch"
date: "2025.03"
doi: "10.1038/s41524-025-01538-0"
arxiv: ""
score: 4.5
essence: "본 논문은 대규모 언어모델(LLM)과 파운데이션 모델(Foundation Models)이 재료 발견(materials discovery) 분야에 어떻게 적용되고 있으며, 향후 어떤 방향으로 발전할 것인지를 종합적으로 리뷰한 관점 논문이다. 데이터 추출, 물성 예측, 분자 생성, 합성 계획 등 현재의 최첨단 적용 사례와 함께 새로운 데이터 수집 방법과 다중 모달리티의 영향을 검토한다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/Materials_Discovery_Hypotheses"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Pyzer-Knapp et al._2025_Foundation models for materials discovery – current state and future directions 1.pdf"
---

# Foundation models for materials discovery – current state and future directions

> **저자**: Edward O. Pyzer-Knapp, Matteo Manica, Peter Staar, Lucas Morin, Patrick Ruch, Teodoro Laino, John R. Smith, Alessandro Curioni | **날짜**: 2025-03-06 | **DOI**: [10.1038/s41524-025-01538-0](https://doi.org/10.1038/s41524-025-01538-0)

---

## Essence

![Figure 1: AI 머신러닝 표현의 진화 타임라인](figures/fig1.webp)
*수동 기술된 기호적 표현에서 오늘날의 파운데이션 모델까지의 진화를 보여주는 타임라인*

본 논문은 대규모 언어모델(LLM)과 파운데이션 모델(Foundation Models)이 재료 발견(materials discovery) 분야에 어떻게 적용되고 있으며, 향후 어떤 방향으로 발전할 것인지를 종합적으로 리뷰한 관점 논문이다. 데이터 추출, 물성 예측, 분자 생성, 합성 계획 등 현재의 최첨단 적용 사례와 함께 새로운 데이터 수집 방법과 다중 모달리티의 영향을 검토한다.

## Motivation

- **Known**: 트랜스포머 아키텍처(2017)와 GPT 모델의 등장으로 자기 지도학습(self-supervised learning)을 통한 일반화된 표현 학습이 가능해짐. 자연어 처리에서의 성공이 다양한 분야로 전이되고 있음.

- **Gap**: 재료 과학 분야에서 파운데이션 모델의 적용이 증가하고 있지만, 1) 활동절벽(activity cliff) 현상으로 인한 미세한 데이터의 중요성, 2) 고품질 대규모 데이터셋의 부족, 3) 다중 모달리티 데이터 통합의 어려움, 4) 3D 구조 정보 누락 등의 과제가 해결되지 않음.

- **Why**: 재료 과학은 언어 생성보다 복잡한 과제이며, 미량의 물질 조성 변화가 초전도 임계 온도 등 물성에 극적인 영향을 미칠 수 있어 고품질의 풍부한 학습 데이터가 필수적.

- **Approach**: 파운데이션 모델의 정의와 구조(인코더, 디코더)를 설명하고, 데이터 추출, 물성 예측, 분자 생성, 합성 계획의 네 가지 핵심 응용 분야에서의 현황과 과제를 체계적으로 분석.

## Achievement

![Figure 2: 공유 잠재 공간의 생성 및 활용](figures/fig2.webp)
*인코더, 디코더 및 예측기 모델을 통해 분자 표현을 잠재 공간으로 변환하는 프로세스 시각화*

1. **데이터 추출 모달리티 확장**: 전통적인 텍스트 기반 추출을 넘어 표(table), 이미지, 분자 구조 등 다중 모달리티 데이터 통합이 진행 중. PubChem, ZINC, ChEMBL 등 주요 화학 데이터베이스 활용 및 특수 알고리즘(Plot2Spectra, DePlot)을 통한 분광 데이터 추출 가능.

2. **물성 예측 모델의 다양화**: BERT 기반 인코더 모델이 주류이지만, GPT 기반 아키텍처의 비중이 증가 중. 2D 표현(SMILES, SELFIES)에서 3D 구조 기반 예측으로의 진화, 특히 결정체(crystals) 같은 무기 고체에서 그래프 기반 표현 적용.

3. **파운데이션 모델 접근의 강점**: 핵심 모델과 아키텍처 컴포넌트의 재사용성으로 효율성 향상. 대규모 자기 지도학습을 통한 일반화된 표현 학습이 다양한 다운스트림 과제에 적응 가능.

## How

![Figure 3: 현재 보고된 모델의 일반적인 아키텍처 유형 분류](figures/fig3.webp)
*다양한 파운데이션 모델 아키텍처의 구성 비율 분석*

- **파운데이션 모델 구조**: 비지도 사전학습(unsupervised pretraining)으로 기반 모델(base model) 구축 → 라벨된 데이터로 세부 과제 미세조정(fine-tuning) → 사용자 선호도에 따른 정렬(alignment) 수행

- **아키텍처 선택**: 
  - 인코더 전용(encoder-only): 데이터 이해 및 표현 중심 (BERT 기반)
  - 디코더 전용(decoder-only): 새로운 분자 생성 중심
  - 인코더-디코더: 합성 계획 등 변환 과제

- **다중 모달리티 데이터 처리**: 대규모 언어모델이 모든 형태의 정보를 독립적으로 처리하기보다는, 영역 특화 알고리즘과 통합되는 오케스트레이터 역할 수행. 이미지에서 테이블로의 변환(DePlot) 등 모듈식 접근법 채택.

- **데이터 품질 확보**: 명명 규칙 불일치, 모호한 물성 설명, 저품질 이미지 등의 노이즈 해결을 위해 강건한 데이터 추출 모델 필요. 특히 특허 문서의 Markush 구조 같은 고가치 다중 모달 데이터 활용.

## Originality

- 파운데이션 모델이라는 새로운 패러다임을 재료 과학 분야에 체계적으로 적용하고 정의(broad data, self-supervision, fine-tuning, alignment)하는 종합적 관점 제시

- 다중 모달리티 데이터 통합의 중요성을 강조하고, 단순 통합이 아닌 모듈식 오케스트레이션 접근법 제안

- 활동절벽과 같은 재료 과학 고유의 도전 과제를 파운데이션 모델 관점에서 명확히 제시하고, 3D 구조 정보 부족의 원인(데이터셋 규모 불균형)을 구체적으로 분석

- 인코더, 디코더, 예측기의 분리와 공유 잠재 공간 개념으로 표현 학습과 다운스트림 과제의 분리를 명확히 구조화

## Limitation & Further Study

- **제한점**:
  1. 현재 모델들이 주로 2D 분자 표현(SMILES)에 의존하여 3D 입체 정보 손실. 3D 데이터셋의 규모가 2D(10^9 수준)에 미치지 못함
  2. 화학 정확성(chemical correctness) 및 합성 가능성(synthesisability)을 보장하는 정렬(alignment) 방법론이 아직 미성숙
  3. 라이선싱 제한, 독점 데이터베이스 접근성 부족으로 인한 편향된 데이터 소싱
  4. 특허 문서 등 비정형 소스에서의 신뢰성 있는 대규모 데이터 추출 기술의 여전한 도전

- **후속 연구**:
  1. 3D 분자 구조 학습을 위한 대규모 데이터셋 구축 및 멀티모달 3D 기반 파운데이션 모델 개발
  2. 화학적 제약과 합성 실현성을 인코딩한 개선된 정렬 기법
  3. 비정형 과학 문헌, 특허, 보유 자료로부터의 자동화된 고품질 데이터 추출 파이프라인 고도화
  4. 특정 재료 시스템(예: 고온 초전도체)에 최적화된 도메인 특화 파운데이션 모델의 개발


## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 5/5
- Clarity: 5/5
- Overall: 4.5/5

**총평**: 본 논문은 파운데이션 모델이라는 최신 AI 패러다임을 재료 과학 분야에 포괄적으로 적용하는 중요한 관점 논문으로, 현재의 최첨단 사례와 함께 데이터 품질, 다중 모달리티 통합, 3D 구조 정보 결핍 등 구체적인 과제들을 명확히 제시한다. 다만 각 응용 분야별 기술적 심화 논의와 구체적인 사례 분석이 제한적이며, 향후 데이터셋 확충과 도메인 특화 모델 개발에 대한 실행 로드맵이 추가될 수 있다.

## Related Papers

- 🧪 응용 사례: [[papers/695_Scaling_Deep_Learning_for_Materials_Discovery/review]] — 파운데이션 모델 이론을 GNoME 같은 대규모 재료 발견에 실제 적용한 사례이다.
- 🏛 기반 연구: [[papers/287_Dont_Stop_Pretraining_Adapt_Language_Models_to_Domains_and_T/review]] — 도메인 적응 기법이 재료과학 파운데이션 모델 개발의 핵심 방법론이다.
- 🔗 후속 연구: [[papers/025_A_Survey_of_AI_for_Materials_Science_Foundation_Models_LLM_A/review]] — 재료과학 AI의 포괄적 현황을 파운데이션 모델 관점에서 체계화한다.
- 🧪 응용 사례: [[papers/788_Targeted_materials_discovery_using_Bayesian_algorithm_execut/review]] — 재료 발견을 위한 파운데이션 모델은 베이지안 알고리즘 실행이 타겟으로 하는 재료 설계 분야의 실제 응용 사례입니다
- 🔗 후속 연구: [[papers/487_Leveraging_biomolecule_and_natural_language_through_multi-mo/review]] — 재료과학 파운데이션 모델을 생물분자 영역으로 확장한 연구
- 🏛 기반 연구: [[papers/1086_Foundational_models_for_scientific_discovery/review]] — 재료 발견을 위한 파운데이션 모델의 현재 상태와 미래 전망의 이론적 토대를 제공한다.
- 🏛 기반 연구: [[papers/695_Scaling_Deep_Learning_for_Materials_Discovery/review]] — GNoME의 성공이 재료발견 분야 파운데이션 모델 발전의 중요한 사례가 된다.
- 🏛 기반 연구: [[papers/287_Dont_Stop_Pretraining_Adapt_Language_Models_to_Domains_and_T/review]] — 도메인 적응 기법이 재료과학 파운데이션 모델의 특화 학습에 필수적이다.
- 🔗 후속 연구: [[papers/829_Towards_Foundation_Models_for_Scientific_Machine_Learning_Ch/review]] — 재료 발견을 위한 파운데이션 모델의 현재 상태를 과학 머신러닝 전반으로 확장한다
- 🏛 기반 연구: [[papers/025_A_Survey_of_AI_for_Materials_Science_Foundation_Models_LLM_A/review]] — 소재 발견을 위한 기초 모델의 현재 상태 분석이 AI 소재 과학 서베이의 기초 모델 섹션에 핵심 정보를 제공함
- 🏛 기반 연구: [[papers/1099_Generative_Inversion_of_Spectroscopic_Data_for_Amorphous_Str/review]] — 재료 발견을 위한 파운데이션 모델의 현재 상태와 이론적 기반
- 🏛 기반 연구: [[papers/633_Prim_Principle-inspired_material_discovery_through_multi-age/review]] — 재료 발견을 위한 기초 모델의 현재 상태와 도전 과제에 대한 이론적 배경을 제공한다.
- 🔗 후속 연구: [[papers/1104_A_Physics-Informed_Chemical_Rule_for_Topological_Materials_D/review]] — 재료과학 파운데이션 모델을 물리 기반 위상 물질 발견 규칙으로 구체화한 응용
- 🧪 응용 사례: [[papers/1106_The_BOS-Lig_Dataset_Accurate_Ligand_Charges_from_a_Consensus/review]] — 재료 발견 파운데이션 모델을 리간드 기능 분류에 적용한 사례
