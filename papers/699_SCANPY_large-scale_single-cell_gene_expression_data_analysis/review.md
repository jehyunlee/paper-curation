---
title: "699_SCANPY_large-scale_single-cell_gene_expression_data_analysis"
authors:
  - "F. A. Wolf"
  - "Philipp Angerer"
  - "Fabian J Theis"
date: "2018"
doi: "10.1186/s13059-017-1382-0"
arxiv: ""
score: 4.5
essence: "SCANPY는 백만 개 이상의 세포를 포함한 대규모 단일세포 유전자 발현 데이터를 효율적으로 분석할 수 있는 Python 기반 확장 가능한 툴킷으로, 기존 R 기반 프레임워크들(Seurat, Monocle 등)보다 5-90배 빠른 성능을 제공한다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/Scientific_Memory_Calculators"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Wolf et al._2018_SCANPY large-scale single-cell gene expression data analysis.pdf"
---

# SCANPY: large-scale single-cell gene expression data analysis

> **저자**: F. A. Wolf, Philipp Angerer, Fabian J Theis | **날짜**: 2018 | **DOI**: [10.1186/s13059-017-1382-0](https://doi.org/10.1186/s13059-017-1382-0)

---

## Essence

SCANPY는 백만 개 이상의 세포를 포함한 대규모 단일세포 유전자 발현 데이터를 효율적으로 분석할 수 있는 Python 기반 확장 가능한 툴킷으로, 기존 R 기반 프레임워크들(Seurat, Monocle 등)보다 5-90배 빠른 성능을 제공한다.

## Motivation

- **Known**: Seurat, Monocle, SCDE/PAGODA 등의 R 기반 단일세포 분석 프레임워크들이 존재하며 통합 분석 워크플로우를 제공
- **Gap**: 기존 프레임워크들은 100만 개 이상의 세포를 포함한 대규모 데이터셋에 확장되지 못함; R 생태계는 고급 머신러닝 패키지(TensorFlow 등)와의 통합이 어려움
- **Why**: 10x Genomics 등의 기술 발전으로 대규모 단일세포 데이터가 급증하고 있으며, Human Cell Atlas 같은 대규모 프로젝트의 요구사항이 증가
- **Approach**: Python 기반 구현으로 NumPy, SciPy 등의 효율적 계산 라이브러리와 고급 머신러닝 도구를 활용하는 모듈식 설계

## Achievement

![Fig 1a - SCANPY 분석 기능 개요](figures/fig1.webp)
*Figure 1a: 68,579개의 말초혈액 단핵세포(PBMC)를 이용한 SCANPY의 분석 파이프라인: 전처리, 정규화, 고변이성 유전자 식별, t-SNE 및 그래프 드로잉 시각화, Louvain 알고리즘을 통한 클러스터링, 차등 발현 유전자 검증, 의사시간 순서화를 통한 분기 궤적 재구성*

1. **성능 우수성**: Cell Ranger R 킷 대비 5-16배의 속도 향상(68,579 PBMC 데이터셋); Seurat 튜토리얼 각 단계별로 5-90배 속도 향상

2. **대규모 데이터 처리**: 8개 코어의 소규모 서버에서 130만 개 세포를 몇 시간 내에 서브샘플링 없이 분석 가능; 약 100,000 개 세포 규모에서 초 단위의 인터랙티브 분석 시간 달성

3. **종합 분석 기능**: 전처리, 시각화(t-SNE, 확산맵), 클러스터링(Louvain), 마커 유전자 식별, 의사시간 순서화(diffusion pseudotime), 분기 궤적 재구성, 유전자 조절 네트워크 시뮬레이션, 딥러닝 결과 분석 등 포괄적 기능 제공

## How

- **AnnData 클래스**: 관찰값(세포), 변수(유전자), 비정형 주석을 모두 포함할 수 있는 일반화된 주석 데이터 행렬 클래스 설계
  - HDF5 기반 디스크 백킹(backing) 지원으로 메모리 제약 극복
  - 플랫폼/프레임워크/언어 독립적인 저장 형식
  - 백킹 모드에서 전체 객체를 메모리에 로드하지 않고도 접근 가능

- **효율적 그래프 표현**: 데이터 포인트 간 이웃 관계를 나타내는 그래프 클래스 도입
  - 병렬화된 행렬 곱셈으로 거리 계산 고속화
  - 무작위 보행(random-walk) 기반 메트릭 계산 함수 제공
  - 한 번 계산된 단일 그래프 표현 재사용으로 계산 비용 절감

- **모듈식 아키텍처**: 
  - 기본 의존성: NumPy, SciPy, Matplotlib, Pandas, H5PY
  - 선택적 패키지: scikit-learn, statsmodels, networkx, igraph, Louvain, t-SNE
  - 머신러닝 패키지 통합: TensorFlow, LIMIX, GPy/GPflow
  - In-place 연산(기본값) 또는 비파괴적 변환 옵션 지원

- **병렬화**: 대부분의 SCANPY 도구들에 병렬 처리 구현

## Originality

- Python 생태계에서 단일세포 데이터의 대규모 분석을 위한 최초의 포괄적 도구킷 제공

- AnnData 클래스의 혁신적 설계: HDF5 기반 동적 백킹과 메모리 모드를 모두 지원하여 대규모 데이터셋에 대한 온라인 학습(online learning) 알고리즘 실현 가능

- 그래프 기반 분석의 중심화: 클러스터링, 의사시간 순서화, 궤적 추론 등을 통일된 그래프 표현으로 수행하는 일관성 있는 접근

- 머신러닝 패키지와의 유기적 통합: Python 생태계의 고급 머신러닝 도구들(특히 딥러닝)과의 자연스러운 연동

## Limitation & Further Study

- **통계 분석의 제한성**: Python 생태계는 R에 비해 고전 통계 분석 방법이 제한적 (논문에서도 명시)

- **초기 생태계**: 논문 발표 시점(2018년)에 Python 기반 단일세포 분석 도구가 부족했으나, 이후 생태계 발전 가능성 제시

- **loom 파일 포맷과의 호환성**: 논문 개정 과정에서 loom 형식이 제안되었고, 이에 대응하여 AnnData의 동적 HDF5 백킹 확대 필요

- **후속 개선**: 더 다양한 통계 패키지 통합, 분산 컴퓨팅 지원 확대, 커뮤니티 기반 확장성 강화


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4.5/5
- Significance: 5/5
- Clarity: 4.5/5
- Overall: 4.5/5

**총평**: SCANPY는 빠르게 성장하는 단일세포 유전체 분석 분야에서 Python 생태계에 처음으로 대규모 데이터 처리가 가능한 포괄적 도구킷을 제공함으로써, 학계와 산업계에 즉각적이고 지속적인 영향을 미쳤으며, 특히 AnnData 클래스는 후속 도구들의 표준으로 채택될 정도로 기여도가 매우 높다.

## Related Papers

- 🔄 다른 접근: [[papers/306_Efficient_fine-tuning_of_single-cell_foundation_models_enabl/review]] — 단일세포 분석을 Python 기반 스케일링 vs LLM 기반 파운데이션 모델로 접근한다.
- 🏛 기반 연구: [[papers/696_Scaling_Large_Language_Models_for_Next-Generation_Single-Cel/review]] — 대규모 단일세포 데이터 처리 기술이 차세대 LLM 기반 분석의 기초가 된다.
- 🔗 후속 연구: [[papers/700_scBaseCount_an_AI_agent-curated_uniformly_processed_and_auto/review]] — SCANPY의 데이터 처리 능력을 AI 에이전트 기반 자동화로 확장한다.
