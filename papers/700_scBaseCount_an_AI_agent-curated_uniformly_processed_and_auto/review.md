---
title: "700_scBaseCount_an_AI_agent-curated_uniformly_processed_and_auto"
authors:
  - "Nicholas D. Youngblut"
  - "Christopher Carpenter"
  - "Jaanak Prashar"
  - "Chiara Ricci-Tam"
  - "Rajesh Ilango"
date: "2025"
doi: "10.1101/2025.02.27.640494"
arxiv: ""
score: 4.4
essence: "AI 에이전트 기반의 자동화된 워크플로우를 통해 공개 10X Genomics 단일세포 RNA 시퀀싱 데이터를 발굴하고 표준화된 방식으로 처리하여, 가장 규모가 크고 다양한 단일세포 데이터 저장소 scBaseCamp를 구축했다. 이는 AI 기반 가상세포 모델 개발을 위한 훈련 데이터로 활용될 수 있으며, 데이터 처리 파이프라인의 표준화를 통해 분석 아티팩트를 최소화한다."
tags:
  - "cat/AI-Powered_Scientific_Research_Frameworks"
  - "sub/Bioinformatics_Data_Integration"
  - "topic/ai4s"
---

# scBaseCamp: an AI agent-curated, uniformly processed, and autonomously updated single cell data repository

> **저자**: Nicholas D. Youngblut, Christopher Carpenter, Jaanak Prashar, Chiara Ricci-Tam, Rajesh Ilango, Noam Teyssier, Silvana Konermann, Patrick D. Hsu, Alexander Dobin, David P. Burke, Hani Goodarzi, Yusuf H. Roohani | **날짜**: 2025 | **DOI**: [10.1101/2025.02.27.640494](https://doi.org/10.1101/2025.02.27.640494)

---

## Essence

![Figure 1](figures/fig1.webp)
*scBaseCamp은 종(species)과 조직(tissue)에 걸쳐 2억 3천만 개 이상의 세포를 포함하는 가장 큰 공개 단일 세포 유전자 발현 데이터셋 저장소이다.*

AI 에이전트 기반의 자동화된 워크플로우를 통해 공개 10X Genomics 단일세포 RNA 시퀀싱 데이터를 발굴하고 표준화된 방식으로 처리하여, 가장 규모가 크고 다양한 단일세포 데이터 저장소 scBaseCamp를 구축했다. 이는 AI 기반 가상세포 모델 개발을 위한 훈련 데이터로 활용될 수 있으며, 데이터 처리 파이프라인의 표준화를 통해 분석 아티팩트를 최소화한다.

## Motivation

- **Known**: 지난 10년간 Human Cell Atlas, CZ CELLxGENE 등 단일세포 RNA 시퀀싱 데이터 통합 노력이 증가했으며, 이는 AI 기반 가상세포(Virtual Cell) 모델 개발의 기초 자료로 활용되고 있다.

- **Gap**: 기존 저장소들은 기여 기반 큐레이션(contributed datasets)에 의존하기 때문에 NIH의 Sequence Read Archive(SRA)에 공개된 전체 데이터의 극히 일부만 포함한다. 또한 서로 다른 정렬 도구(alignment tools), 참조 게놈(reference genomes), 계산 전략(counting strategies)으로 인한 분석 편차가 존재한다.

- **Why**: AI 모델 훈련에는 일반적으로 세포 레이블이 불필요하므로, 대규모 표준화된 데이터 저장소가 필요하다. 벌크 RNA-seq의 Recount 프로젝트처럼 표준화된 파이프라인을 통한 재처리가 분석 배치 효과를 최소화할 수 있다.

- **Approach**: AI 에이전트(SRAgent)를 통한 자동 발굴 및 메타데이터 추출, 그리고 표준화된 처리 파이프라인(scRecounter)을 통한 단일 세포 데이터의 대규모 재처리.

## Achievement

![Figure 1](figures/fig1.webp)
*scBaseCamp의 규모와 다양성: (A) 인간, 마우스, 제브라피시, 초파리의 조직별 색상 UMAP, (B-C) CZ CELLxGENE과의 종과 조직 분포 비교, (D) SRAgent의 자동 조직 주석과 CZ CELLxGENE 레이블의 일치도*

1. **최대 규모의 데이터 저장소 구축**: 현재 2억 3천만 개 이상의 세포를 포함하고 있으며, CZ CELLxGENE(1억 7백만 개)과 Human Cell Atlas(6천 5백만 개)를 능가한다. 평균적으로 세포당 7,614개의 고유 분자 식별자(UMI)를 보유한다.

2. **광범위한 종과 조직 다양성**: 21개 종과 72개 조직에 걸친 데이터를 포함하여 기존 저장소보다 훨씬 더 광범위한 생물학적 맥락을 제공한다.

3. **자동 메타데이터 추출**: SRAgent가 10X 화학(chemistry), 세포 vs 핵(cell vs nuclei), 질병, 조직 정보 등 핵심 메타데이터를 자동으로 추출하며, 조직 레이블의 경우 CZ CELLxGENE와 높은 일치도(confusion matrix)를 보인다.

4. **지속적 확장**: 현재까지 63,892개의 SRA 실험을 식별했고 이 중 43,587개가 10X Genomics 라이브러리로 확인되었으며, 30,387개를 재처리했다.

## How

![Figure 2](figures/fig2.webp)
*AI 기반 큐레이션 및 표준화된 처리: (A) SRAgent의 계층적 AI 파이프라인, (B) scRecounter의 Nextflow 기반 처리 워크플로우, (C) 다양한 특성 주석 및 멀티맵핑 전략*

- **SRAgent (자동 발굴 및 메타데이터 추출)**:
  - LangGraph를 사용한 계층적 ReAct 에이전트 워크플로우 구현
  - NCBI 도구(eSearch, eSummary, eFetch, eLink) 및 SRA BigQuery를 비동기적으로 접근
  - GCP Cloud Run 배포: 1-5분마다 작업 실행, 시간당 최대 300개 데이터셋 처리
  - 관계형 데이터베이스(GCP SQL)에 메타데이터 저장

- **scRecounter (표준화된 재처리)**:
  - Nextflow 기반 파이프라인으로 GCP Cloud Run 및 GCP Batch 활용
  - 10X Genomics 화학 자동 식별: 먼저 100만 개의 paired-end 읽음으로 화학 버전과 STARsolo 파라미터 결정
  - STARsolo를 이용한 맵핑 및 세포×유전자 계산 테이블 생성
  - h5ad 형식으로 조화된 발현 행렬 저장
  - 총 7.7×10^12개의 읽음 처리
  - 다양한 특성 주석 및 멀티맵핑 전략으로 여러 count 테이블 제공

- **메타데이터 관리**: PostgreSQL 데이터베이스를 통한 처리 추적

## Originality

- **AI 에이전트 기반 자동화**: LangGraph를 활용한 계층적 ReAct 에이전트 워크플로우는 수동 큐레이션의 확장성 한계를 극복하는 혁신적 접근법이다.

- **대규모 표준화 재처리**: 벌크 RNA-seq의 Recount 프로젝트 개념을 단일세포 영역으로 확장하여 처음 대규모 표준화 재처리를 시도했다.

- **지속적 자동 업데이트**: 새로운 데이터 공개 시 자동으로 발굴 및 처리되는 동적 시스템 구축으로 데이터 저장소의 연속성을 보장한다.

- **공개 코드 제공**: SRAgent 코드를 공개하여 연구 커뮤니티의 추가 확장을 지원한다.

- **멀티플 처리 옵션**: 다양한 특성 주석 및 멀티맵핑 전략을 제공하여 사용자의 응용 목적에 맞는 선택이 가능하다.

## Limitation & Further Study

- **화학 버전 자동 식별의 한계**: SRA 메타데이터의 불완전성으로 인해 100만 개 읽음 샘플만 사용하여 화학 버전을 결정하는데, 이것이 전체 데이터셋의 화학을 정확히 반영하지 못할 가능성이 있다.

- **제한된 게놈 참조**: 현재 10X Genomics 저장소의 인간 및 마우스 참조 게놈만 사용하고 있어, 다른 종에 대한 처리 방식의 체계적 기술이 부재하다.

- **검증 데이터 부족**: 논문에서 제공된 본문에서는 표준화 처리가 실제로 분석 아티팩트를 감소시키는지에 대한 상세한 정량적 검증이 제한적으로 제시되어 있다(Figure 3은 언급되나 캡션이 완전하지 않음).

- **후속 연구 방향**:
  - 다양한 게놈에 대한 참조 구축 확대
  - 단일세포 및 단일 핵(single nucleus) 데이터 처리의 기술적 차이 표준화
  - 세포 유형 주석 자동화의 정확도 향상
  - 가상세포 모델 훈련에서의 성능 개선 평가

## Evaluation

- **Novelty**: 4.5/5
  - AI 에이전트 기반 자동화와 대규모 표준화는 혁신적이나, 기술 기초(STAR, STARsolo, LLM)는 기존 도구에 의존함.

- **Technical Soundness**: 4/5
  - 파이프라인 설계가 합리적이나, 화학 자동 식별의 정확성 검증과 다양한 게놈 참조 처리 방식에 대한 기술적 세부사항이 제한적임.

- **Significance**: 5/5
  - 2억 3천만 개의 세포 규모, 21개 종 및 72개 조직, 그리고 지속적 자동 업데이트는 단일세포 생물학 및 AI 모델 개발 분야에 변혁적 자원을 제공함.

- **Clarity**: 4/5
  - 전반적으로 명확하고 구조화되어 있으나, 일부 기술적 세부사항(특히 다양한 게놈에 대한 처리)과 검증 결과가 더 상세하게 제시될 필요가 있음.

- **Overall**: 4.4/5

**총평**: scBaseCamp는 AI 에이전트 기반 자동화 및 표준화된 대규모 재처리를 통해 단일세포 생물학과 AI 모델 개발을 위한 획기적인 자원을 제공하며, 지속적 확장 메커니즘은 이 분야의 향후 발전을 크게 가속화할 것으로 예상된다. 다만 기술적 세부사항과 정량적 검증 데이터의 보강이 필요하다.

## Related Papers

- 🔄 다른 접근: [[papers/193_CellAgent_An_LLM-driven_Multi-Agent_Framework_for_Automated/review]] — 단일세포 RNA 시퀀싱 데이터 처리를 위해 AI 에이전트 기반 자동화와 대규모 표준화라는 다른 접근법을 사용한다
- 🏛 기반 연구: [[papers/696_Scaling_Large_Language_Models_for_Next-Generation_Single-Cel/review]] — 단일세포 데이터의 대규모 언어모델 스케일링을 위한 고품질 훈련 데이터 기반을 제공한다
- 🧪 응용 사례: [[papers/306_Efficient_fine-tuning_of_single-cell_foundation_models_enabl/review]] — 표준화된 단일세포 데이터를 파운데이션 모델의 효율적 파인튜닝에 활용할 수 있다
- 🏛 기반 연구: [[papers/696_Scaling_Large_Language_Models_for_Next-Generation_Single-Cel/review]] — 단일세포 데이터의 LLM 처리 기술이 AI 에이전트 기반 단일세포 데이터베이스 구축과 표준화에 필수적인 기반 기술을 제공한다
- 🧪 응용 사례: [[papers/431_Integrated_analysis_of_multimodal_single-cell_data/review]] — 멀티모달 단일세포 데이터 분석 기술이 AI 에이전트 기반 단일세포 데이터베이스 구축과 표준화 작업에 핵심적으로 활용된다
- 🔄 다른 접근: [[papers/193_CellAgent_An_LLM-driven_Multi-Agent_Framework_for_Automated/review]] — 단일세포 분석 자동화를 위해 LLM 다중 에이전트 프레임워크와 AI 기반 대규모 데이터 표준화라는 다른 접근법을 사용한다
- 🔗 후속 연구: [[papers/699_SCANPY_large-scale_single-cell_gene_expression_data_analysis/review]] — SCANPY의 데이터 처리 능력을 AI 에이전트 기반 자동화로 확장한다.
