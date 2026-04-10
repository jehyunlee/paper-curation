---
title: "151_Benchmarking_ai_scientists_in_omics_data-driven_biological_r"
authors:
  - "Erpai Luo"
  - "Jinmeng Jia"
  - "Yifan Xiong"
  - "Xiangyu Li"
  - "Xiaobo Guo"
date: "2025"
doi: "arXiv:2505.08341"
arxiv: ""
score: 4.2
essence: "단일세포 전사체(single-cell transcriptomics) 데이터를 활용하여 AI 과학자(AI scientist) 시스템의 생물학적 발견 능력을 평가하는 BAISBench 벤치마크를 제시한다. 현재 AI 과학자들은 완전한 자동화된 생물학적 발견에는 못 미치지만, 데이터 기반 생물학 연구 지원에 상당한 잠재력을 보이고 있음을 실증적으로 보여준다."
tags:
  - "cat/AI-Powered_Scientific_Research_Frameworks"
  - "sub/Bioinformatics_Data_Integration"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Bajwa et al._2025_Benchmarking ai scientists in omics data-driven biological research.pdf"
---

# Benchmarking AI Scientists in Omics Data-Driven Biological Research

> **저자**: Erpai Luo, Jinmeng Jia, Yifan Xiong, Xiangyu Li, Xiaobo Guo, Baoqi Yu, Minsheng Hao, Lei Wei, Xuegong Zhang | **날짜**: 2025 | **DOI**: [arXiv:2505.08341](https://arxiv.org/abs/2505.08341)

---

## Essence

![Figure 1](figures/fig1.webp)
*BAISBench의 개요: (A) 두 가지 보완적 태스크 구성, (B) BAIS-DPTA의 구축 방식, (C) BAIS-SD의 구축 방식*

단일세포 전사체(single-cell transcriptomics) 데이터를 활용하여 AI 과학자(AI scientist) 시스템의 생물학적 발견 능력을 평가하는 BAISBench 벤치마크를 제시한다. 현재 AI 과학자들은 완전한 자동화된 생물학적 발견에는 못 미치지만, 데이터 기반 생물학 연구 지원에 상당한 잠재력을 보이고 있음을 실증적으로 보여준다.

## Motivation

- **Known**: 대규모 언어모델(LLM)의 발전으로 생물학 데이터를 자동으로 분석하고 과학 발견을 지원하는 AI 과학자 시스템들이 등장하고 있으며, AutoBA, scChat, BioChatter, Biomni, Pantheon, STELLA 등 다양한 시스템이 개발되었다.

- **Gap**: 기존 벤치마크들은 추론만 평가하거나(데이터 없이), 사전 정의된 분석 결과에만 초점을 맞추어 실제 데이터 기반 생물학 연구의 특성을 반영하지 못한다. BLADE나 BixBench 같은 데이터 기반 벤치마크도 생물 통찰력 도출 능력을 직접 평가하지 못한다.

- **Why**: 생물학 연구는 새로운 실험 데이터로부터 의미 있는 해석과 발견을 도출하는 것이 핵심이므로, 이를 반영하는 현실적이고 데이터 중심의 평가 프레임워크가 필수적이다.

- **Approach**: 15개의 전문가 주석 단일세포 데이터셋을 이용한 세포형 주석(cell type annotation) 태스크와 41개의 발표된 단일세포 연구에서 도출한 193개의 객관식 질문으로 구성된 벤치마크를 개발하고, 여러 AI 과학자 시스템과 6명의 대학원 수준 생물정보학자의 성능을 비교 평가한다.

## Achievement

![Figure 4](figures/fig4.webp)
*BAIS-DPTA 태스크에서 다양한 AI 모델의 세포형 주석 정확도: (A) 전체 결과, (B) 조직별 결과*

1. **세포형 주석 능력**: AI 과학자들은 표준 전처리 및 분석 워크플로우를 안정적으로 실행할 수 있으며, 기본 LLM 모델의 성능에 따라 크게 좌우됨을 보였다. uHAF 기반의 계층적 평가 지표(SCTA)를 도입하여 정확도뿐 아니라 생물학적 세분화 정도도 평가 가능하게 했다.

2. **과학적 발견 능력**: 최고 성능 AI 과학자들이 대학원 수준 연구자들과 비슷한 수준의 성능을 달성했으나, 깊은 생물학적 판단이 필요한 태스크에서는 여전히 인간 전문가에 미치지 못한다. 193개의 질문에서 산출된 결과는 AI 시스템의 강점과 약점을 명확히 구분한다.

3. **평가 프레임워크 확립**: 실제 생물학 연구 워크플로우를 반영하는 현실적이고 해석 가능한 벤치마크를 제시함으로써 AI 과학자의 진전을 평가하고 개선 방향을 제시할 수 있는 기초를 마련했다.

## How

![Figure 2](figures/fig2.webp)
*BAIS-DPTA 태스크의 파이프라인: AI 과학자에게 단일세포 유전자 발현 데이터셋이 제공되고 전처리 및 주석을 수행*

![Figure 3](figures/fig3.webp)
*BAIS-SD 태스크의 파이프라인: 배경 정보와 대응하는 데이터셋이 제공되고 발표된 발견과 일치하는 결론을 찾도록 요구*

- **BAIS-DPTA 구축**: 15개 장기·조직 유래 최근 발표 scRNA-seq 데이터셋(세포 수: 2,312~58,706, 세포형: 4~42종) 수집 후 경험 많은 생물정보학자들이 통합 계층적 세포 주석 프레임워크(uHAF)를 기준으로 수동 주석

- **평가 메트릭**: 워크플로우 완성도(품질관리, 정규화, 고변이 유전자 선택, 차원 축소, 클러스터링, 마커 유전자 동정) 확인 후 uHAF 기반 계층적 점수(SCTA)로 정확한/부분적/약한 일치도 평가

- **BAIS-SD 구축**: 41개 발표 단일세포 연구에서 도출한 193개 객관식 질문(10개 범주) 작성, 각 질문마다 대응하는 데이터셋과 정답 지정

- **인간 기준선**: BAIS-DPTA는 1명의 생물정보학자가 자동화 도구(CellTypist) 사용, BAIS-SD는 5명이 집단으로 완료하여 인간 성능 기준선 제공

- **평가 시스템**: 다양한 기반 LLM 모델(GPT-4, Claude 등)을 가진 여러 AI 과학자 시스템에 대해 일관된 프롬프트와 평가 절차 적용

## Originality

- **실제 생물학 워크플로우 반영**: 기존 벤치마크와 달리 정적 지식이 아닌 새로운 실험 데이터 분석을 통한 발견을 직접 평가하는 진정한 데이터 중심 벤치마크 설계

- **계층적 평가 체계**: uHAF를 기반으로 단순 정확도를 넘어 생물학적 세분화 정도를 고려한 다단계 평가 메트릭(SCTA) 개발

- **현실성 있는 질문 세트**: 발표된 연구에서 직접 도출한 193개 질문으로 실제 과학적 발견 과정과 유사한 평가 시나리오 구성

- **인간-AI 직접 비교**: 동일한 태스크를 대학원 수준 전문가가 수행한 결과와 직접 비교하여 상대적 능력 평가 가능

- **공개 자원 제공**: GitHub와 HuggingFace에서 전체 벤치마크와 데이터셋을 공개하여 재현성과 확장성 보장

## Limitation & Further Study

- **한계**: 
  - 평가 대상이 단일세포 전사체 데이터에 한정되어 단백질체학(proteomics), 대사체학(metabolomics) 등 다른 오믹스 데이터로의 일반화 불확실
  - BAIS-DPTA 평가에 전문가 1명이 자동화 도구를 사용한 것으로 기준선 수립하여 순수 인간 능력과의 비교 부분적
  - 객관식 질문 형식의 BAIS-SD는 개방형 발견(open-ended discovery) 능력 평가에 한계
  - AI 과학자 시스템의 투명성 부족으로 성능 차이의 원인 분석 어려움

- **후속 연구**:
  - 프로테오믹스, 대사체학, 이미징 데이터 등을 포함한 다중 오믹스 벤치마크 확장
  - 장기 종단 분석(longitudinal analysis), 질병 상태 추론 등 더 복잡한 생물학적 시나리오 포함
  - 개방형 질문 기반 평가 방식 도입으로 AI의 창의적 가설 생성 능력 평가
  - AI 과학자의 추론 과정 분석을 위한 설명 가능성(explainability) 평가 추가


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4/5
- Significance: 4.5/5
- Clarity: 4/5
- Overall: 4.2/5

**총평**: 이 논문은 단순한 지식 기반 평가를 넘어 실제 생물학 데이터 분석 능력을 평가하는 현실적이고 실용적인 벤치마크를 제시함으로써, 빠르게 발전하는 AI 과학자 분야에 타당성 있는 평가 기준을 마련했다. 계층적 평가 체계와 공개 자원은 학계에 즉각적인 기여를 할 수 있으나, 평가 범위의 다양화와 개방형 발견 능력 평가 추가를 통해 더욱 포괄적인 벤치마크로 발전할 여지가 있다.

## Related Papers

- 🔄 다른 접근: [[papers/168_Biomni_A_General-Purpose_Biomedical_AI_Agent/review]] — 생물의학 AI의 성능 평가라는 동일한 목표를 다른 접근법(벤치마크 vs 통합 에이전트)으로 달성합니다.
- 🏛 기반 연구: [[papers/089_Aigs_Generating_science_from_ai-powered_automated_falsificat/review]] — 자동화된 과학 발견의 일반적 프레임워크를 생물학 연구라는 특정 도메인에 적용하는 기초를 제공합니다.
- 🔗 후속 연구: [[papers/710_Sciclaimhunt_A_large_dataset_for_evidence-based_scientific_c/review]] — 과학적 주장 검증을 생물학적 발견 평가로 확장하여 AI 과학자의 신뢰성을 높입니다.
- 🧪 응용 사례: [[papers/089_Aigs_Generating_science_from_ai-powered_automated_falsificat/review]] — 자동 반증 기반 과학 시스템을 생물학적 발견이라는 구체적 도메인에 적용하여 실용성을 검증합니다.
- 🧪 응용 사례: [[papers/139_Autonomous_microscopy_experiments_through_large_language_mod/review]] — 자동화된 실험 벤치마크 개발 방법론을 생물학적 데이터 분석에 적용하는 사례를 제공합니다.
- 🔄 다른 접근: [[papers/168_Biomni_A_General-Purpose_Biomedical_AI_Agent/review]] — 생의학 연구 지원이라는 동일한 목표를 통합 에이전트와 벤치마크 평가라는 상호 보완적 접근으로 달성합니다.
- 🏛 기반 연구: [[papers/710_Sciclaimhunt_A_large_dataset_for_evidence-based_scientific_c/review]] — 과학적 주장의 증거 기반 검증이 AI 과학자의 생물학적 발견 능력 평가의 기준을 제공합니다.
- 🔗 후속 연구: [[papers/041_Aaar-10_Assessing_ais_potential_to_assist_research/review]] — 일반적인 AI 연구 지원 평가에서 오믹스 데이터 기반 생물학 연구라는 구체적 도메인으로 확장한 전문 분야 벤치마크입니다.
