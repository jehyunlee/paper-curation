---
title: "1099_Generative_Inversion_of_Spectroscopic_Data_for_Amorphous_Str"
authors:
  - "Jiawei Guo"
  - "Daniel Schwalbe-Koda"
date: "2026"
doi: "10.48550/ARXIV.2603.23210"
arxiv: ""
score: 4.0
essence: "GLASS는 다중 분광 측정 데이터를 역변환하여 비정질 재료의 실제적인 원자 구조를 생성하는 생성형 AI 프레임워크를 제시한다. 점수 기반 확산 모델(score-based diffusion model)과 미분 가능한 분광 시뮬레이션을 결합하여 상호작용 포텐셜 없이 구조를 복원한다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/Materials_Discovery_Hypotheses"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Guo and Schwalbe-Koda_2026_Generative Inversion of Spectroscopic Data for Amorphous Structure Elucidation.pdf"
---

# Generative Inversion of Spectroscopic Data for Amorphous Structure Elucidation

> **저자**: Jiawei Guo, Daniel Schwalbe-Koda | **날짜**: 2026 | **DOI**: [10.48550/ARXIV.2603.23210](https://doi.org/10.48550/ARXIV.2603.23210)

---

## Essence

![Figure 1](figures/fig1.webp)

*Fig. 1: Architecture of GLASS: Generative Learning of Amorphous Structures from Spectra. A. Concep-*

GLASS는 다중 분광 측정 데이터를 역변환하여 비정질 재료의 실제적인 원자 구조를 생성하는 생성형 AI 프레임워크를 제시한다. 점수 기반 확산 모델(score-based diffusion model)과 미분 가능한 분광 시뮬레이션을 결합하여 상호작용 포텐셜 없이 구조를 복원한다.

## Motivation

- **Known**: 비정질 재료의 원자 구조 결정은 회절 데이터만으로는 불충분하고, 분자동역학(MD) 시뮬레이션과 역몬테카를로(RMC) 방법이 각각 물리적 타당성과 데이터 부합성 사이의 트레이드오프를 가진다.
- **Gap**: 기존 방법들은 다중 분광 데이터를 동시에 역변환하면서도 물리적 실현성을 보장하고 상호작용 포텐셜에 의존하지 않는 통일된 프레임워크가 부재하다.
- **Why**: 비정질 및 혼합상 구조의 자동화된 규명은 재료 특성 해석을 가속화하고, 난제인 paracrystallinity, 액-액 상전이 같은 복잡한 현상을 메커니즘 수준에서 이해할 수 있게 한다.
- **Approach**: 생성 모델이 저충실도 데이터로부터 구조 선행 확률(structural prior)을 학습하고, 확산 역과정 중 미분 가능한 분광 목표함수의 그래디언트로 조건화하여 구조를 샘플링한다. 전자 구조 의존 분광(XANES, EXAFS)은 GNN 대체 모델(surrogate)로 구현된다.

## Achievement

![Figure 2](figures/fig2.webp)

*Fig. 2: Comparing reconstruction of amorphous structures with multi-modal spectroscopy. A. Schematic il-*

- **다중 분광 역변환 프레임워크**: PDF, XANES, EXAFS, X선/중성자 회절 등 6가지 분광 양식을 동시에 처리하여 구조 퇴화성(structural degeneracy) 해결
- **비정질 규명의 우수성**: 아몬드 실리콘(a-Si), Cu-Zr 금속유리, 실리카(a-SiO₂) 등에서 RMC 대비 더 정확한 스펙트럼 재현 달성
- **세 가지 난제 해결**: 비정질 실리콘의 paracrystallinity, 황의 액-액 상전이, 볼밀드 비정질 얼음의 메커니즘 규명
- **분광 양식의 상보성 정량화**: PDF가 단일 프로브로서 가장 정보량이 많음을 실증하고, 다중 양식 결합의 가치 입증
- **물리적 타당성 보증**: 학습된 구조 선행 확률이 비현실적 구조 생성을 방지하는 '소프트 제약'으로 작동

## How

![Figure 1](figures/fig1.webp)

*Fig. 1: Architecture of GLASS: Generative Learning of Amorphous Structures from Spectra. A. Concep-*

- 점수 기반 확산 모델: 확률적 미분 방정식(SDE)으로 원자 구성의 분포 학습, GNN 스코어 네트워크로 구현
- 그래프 신경망(GNN) 구조: 원자 위치, 거리, 원자 종류, 가우스 랜덤 푸리에 특성(RFF)을 입력으로 각 원자의 스코어 예측
- 미분 가능 분광 모듈: 실공간 함수(PDF, ADF)는 매끄러운 밀도 추정기, 회절은 미분 가능 디바이 합산식, XAS는 GNN 대체 모델 사용
- 조건부 생성 프로세스: 역시간 확산 과정에서 예측 스코어, 분광 그래디언트, 확률 소음을 조합하여 좌표 업데이트
- 외분포(out-of-distribution) 평가: MD 시뮬레이션으로 생성한 5가지 비정질 재료 앙상블(a-C, a-Si, a-SiO₂, Cu-Zr, Zr-Ni-Al)로 벤치마킹

## Originality

- 생성 모델과 미분 가능 시뮬레이션의 새로운 결합: 기존의 경경화(hard constraint) RMC 방식 대신 '소프트 제약' 선행 확률 도입", '다중 분광 양식의 동시 역변환: 실공간과 역공간, 2체·3체 함수, 전자 구조 의존 분광을 통일 프레임으로 처리
- 분광 양식 상보성의 정량적 분석: 각 분광 모드의 정보량을 체계적으로 비교하여 PDF의 우월성 입증
- GNN 대체 모델로 전자 분광 미분 가능화: FEFF9 계산 기반 XANES/EXAFS GNN 학습으로 확산 과정 가속화
- 포텐셜 부재 구조 복원: 상호작용 포텐셜이나 손으로 제작한 제약 없이 물리적 타당성 확보

## Limitation & Further Study

- GNN 대체 모델의 전이성: XANES/EXAFS 대체 모델을 훈련 범위 외 원소나 재료로 확장할 때 일반화 성능 검증 필요
- 분광 데이터 노이즈 강건성: 실험 스펙트럼의 노이즈, 배경 차감 오류가 역변환에 미치는 영향에 대한 분석 부족
- 계산 비용-정확성 트레이드오프: 미분 가능 PDF 구현의 평활화(smoothing) 근사가 세밀한 구조 특징 손실 가능성
- 단일 시스템 대상 최적화: 각 물질계마다 스코어 모델 재훈련 필요로 일반화 성능 제약
- 후속 연구 방향: (1) 전이 학습으로 신규 재료 확장성 개선, (2) 베이지안 불확실성 정량화 추가, (3) 고온·고압 조건 확장, (4) 동적 구조/결함 상호작용 모델링

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: GLASS는 생성 모델, 미분 가능 시뮬레이션, GNN 대체 모델을 창의적으로 결합하여 비정질 구조 복원의 자동화를 달성한 고도로 혁신적인 연구이다. 다중 분광 데이터 동시 역변환과 물리적 타당성 보증이라는 난제를 효과적으로 해결하면서도, GNN 전이성과 실험 노이즈 강건성 측면에서 추가 검증이 필요하다.

## Related Papers

- 🔄 다른 접근: [[papers/282_DMFlow_Disordered_Materials_Generation_by_Flow_Matching/review]] — 비정질 재료 구조 생성에서 흐름 매칭과 확산 모델의 다른 접근법
- 🏛 기반 연구: [[papers/343_Foundation_models_for_materials_discovery__current_state_and/review]] — 재료 발견을 위한 파운데이션 모델의 현재 상태와 이론적 기반
- 🔗 후속 연구: [[papers/695_Scaling_Deep_Learning_for_Materials_Discovery/review]] — 재료 발견을 위한 딥러닝 확장성에서 분광 데이터 역변환으로의 발전
- 🧪 응용 사례: [[papers/799_The_frontier_of_simulation-based_inference/review]] — 시뮬레이션 기반 추론의 최전선 기술을 분광 구조 복원에 적용
