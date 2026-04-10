---
title: "007_A_fine-tuned_large_language_model_based_molecular_dynamics_a"
authors:
  - "Zhuo-Fan Shi"
  - "Chunxiao Xin"
  - "Tong Huo"
  - "Yun-Tao Jiang"
  - "Bowen Wu"
date: "2025"
doi: "10.1038/s41598-025-92337-6"
arxiv: ""
score: 4.0
essence: "LAMMPS 기반 분자동역학(MD) 시뮬레이션을 위해 미세조정된 대규모언어모델(LLM)을 활용하여 재료의 열역학 파라미터를 자동으로 계산하는 MDAgent 프레임워크를 제안한다. 텍스트-코드 생성 기술로 코드 개발 시간을 42.22% 단축하였다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/LLM_Drug_Discovery"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Shi et al._2025_A fine-tuned large language model based molecular dynamics agent for code generation to obtain mater.pdf"
---

# A fine-tuned large language model based molecular dynamics agent for code generation to obtain material thermodynamic parameters

> **저자**: Zhuo-Fan Shi, Chunxiao Xin, Tong Huo, Yun-Tao Jiang, Bowen Wu | **날짜**: 2025 | **DOI**: [10.1038/s41598-025-92337-6](https://doi.org/10.1038/s41598-025-92337-6)

---

## Essence

![Figure 1](figures/fig1.webp)

*Fig. 1.  Comparison of thermodynamic analysis workflow with and without the use of Molecular Dynamics*

LAMMPS 기반 분자동역학(MD) 시뮬레이션을 위해 미세조정된 대규모언어모델(LLM)을 활용하여 재료의 열역학 파라미터를 자동으로 계산하는 MDAgent 프레임워크를 제안한다. 텍스트-코드 생성 기술로 코드 개발 시간을 42.22% 단축하였다.

## Motivation

- **Known**: 분자동역학 시뮬레이션은 재료의 열역학적 성질 연구에 필수적이지만, LAMMPS 같은 전문 소프트웨어 사용은 높은 전문성과 많은 수작업을 요구한다. 최근 ChatGPT, Qwen 등 LLM 기술이 발전하면서 재료과학 분야에 AI 적용 사례가 증가하고 있다.
- **Gap**: 기존 연구는 텍스트-텍스트 생성에 초점을 두었으며, LAMMPS 기반 텍스트-코드 생성을 위한 대규모 고품질 데이터셋이 부족하다. 또한 이론 계산과 코드 개발 분야에서 LLM의 잠재력이 충분히 탐색되지 않았다.
- **Why**: 재료과학 연구에서 열역학 특성 계산은 필수적이며, 자동화된 코드 생성은 시간 비용을 절감하고 진입 장벽을 낮춘다. 이는 재료과학 연구의 효율성과 접근성을 크게 향상시킬 수 있다.
- **Approach**: Manager, Planner, Worker, Evaluator로 구성된 모듈형 에이전트 아키텍처를 설계하고, 두 개의 맞춤형 데이터셋(LSCF-Dataset, LEQS-Dataset)으로 LLM을 미세조정하여 LAMMPS 스크립트 생성 및 평가 능력을 향상시킨다.

## Achievement

![Figure 3](figures/fig3.webp)

*Fig. 3.  Simulation models and results: (a) copper molecular model for volumetric heat capacity, (b) energy–*

- **MDAgent 프레임워크 개발**: 자연언어 입력을 분석하여 자동으로 LAMMPS 시뮬레이션 스크립트를 생성, 실행, 검토하고 반복적으로 개선하는 통합 시스템 구축
- **전문 데이터셋 구축**: LAMMPS 스크립트 생성용 LSCF-Dataset과 전문가 주석 평가용 LEQS-Dataset 개발으로 재료과학 분야의 데이터 부족 문제 해결
- **성능 개선**: 평균 작업 완료 시간을 기존 방법 대비 42.22% 단축하고, 코드 생성 및 검토 능력 향상을 전문가 평가로 검증
- **다중 열역학 작업 검증**: 구리의 체적열용량, 다이아몬드 격자상수, 구리 용융점, 구리 선팽창계수 등 4가지 대표 작업에서 신뢰할 수 있는 결과 도출

## How

![Figure 2](figures/fig2.webp)

*Fig. 2.  (a) Architecture diagram: MDAgent with Manager, Worker, and evaluator powered by large language*

- Manager 컴포넌트가 자연언어 사용자 입력을 파싱하여 작업 의도를 해석
- Planner가 고수준 목표를 LAMMPS 관련 세부 작업(subtask)으로 분해
- Worker가 LAMMPS 전문 LLM을 활용하여 시뮬레이션 스크립트 생성
- Evaluator가 미세조정된 모델을 통해 생성된 스크립트를 평가하고 점수/근거 제시
- 반복적 개선 루프를 통해 스크립트 품질 지속적 향상
- LSCF-Dataset으로 스크립트 생성 능력 학습, LEQS-Dataset으로 평가 능력 학습

## Originality

- 재료과학 분야에서 LAMMPS 기반 텍스트-코드 생성을 체계적으로 다룬 최초 연구
- 도메인 전문가 협력을 통해 구축한 LSCF-Dataset과 LEQS-Dataset 제시로 데이터 기반 부족 문제 해결
- Manager-Planner-Worker-Evaluator 4단계 모듈형 에이전트 구조로 복잡한 시뮬레이션 작업 자동화
- LLM의 코드 생성뿐만 아니라 전문가 수준의 코드 평가 및 자가 개선 능력 구현

## Limitation & Further Study

- 현재는 LAMMPS의 열역학 계산 작업에만 제한되어 있으며, 다른 MD 소프트웨어나 재료과학 분야로의 확대 검증 필요
- 4가지 테스트 작업만 평가하였으므로, 더 광범위한 열역학 계산 시나리오에 대한 추가 검증 필요
- 예측된 열역학값이 이론값과 약간의 편차가 있으므로(예: 용융점 1440.8K vs 이론값 1357.7K), 정확도 향상을 위한 추가 최적화 필요
- 인간-AI 협업 모델이므로 완전 자동화가 아니며, 복잡한 도메인 문제는 여전히 전문가 개입 필요
- 데이터셋 규모, 미세조정 전략, 다양한 LLM 백본 모델에 대한 체계적 비교 연구 부족

## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 이 논문은 LLM 기반 텍스트-코드 생성 기술을 재료과학의 LAMMPS 시뮬레이션 자동화에 최초로 적용하여, 전문 데이터셋 구축과 함께 혁신적인 에이전트 프레임워크를 제시한다. 42% 시간 단축과 전문가 평가 검증으로 현실적 가치를 입증했으며, 향후 다른 도메인으로의 확장 가능성이 높다.

## Related Papers

- 🧪 응용 사례: [[papers/516_Machine-Learned_Interatomic_Potentials_for_Predicting_Physic/review]] — 분자동역학 자동화를 위한 MDAgent는 Machine-Learned Interatomic Potentials 연구에서 개발된 물리적 특성 예측 기법을 실제 재료 설계에 적용합니다.
