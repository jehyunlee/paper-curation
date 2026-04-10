---
title: "694_Scalable_Cross-Facility_Federated_Learning_for_Scientific_Fo"
authors:
  - "Yijiang Li"
  - "Zilinghan Li"
  - "Kyle Chard"
  - "Ian Foster"
  - "Todd Munson"
date: "2026.03"
doi: "미제공"
arxiv: ""
score: 4.5
essence: "본 논문은 프라이버시 제약, 데이터 주권, 대규모 데이터 생성으로 인해 중앙화할 수 없는 과학 데이터를 다중 슈퍼컴퓨터 환경에서 연합학습(Federated Learning, FL)으로 훈련하는 확장 가능한 프레임워크를 제시하며, DOE 리더십급 슈퍼컴퓨터 4대에서의 실증을 통해 크로스-시설 FL의 실용성을 입증한다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/AI_Scientific_Discovery"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Li et al._2026_Scalable Cross-Facility Federated Learning for Scientific Foundation Models on Multiple Supercompute.pdf"
---

# Scalable Cross-Facility Federated Learning for Scientific Foundation Models on Multiple Supercomputers

> **저자**: Yijiang Li, Zilinghan Li, Kyle Chard, Ian Foster, Todd Munson, Ravi Madduri, Kibaek Kim | **날짜**: 2026-03-20 | **DOI**: [미제공](https://doi.org/)

---

## Essence

본 논문은 프라이버시 제약, 데이터 주권, 대규모 데이터 생성으로 인해 중앙화할 수 없는 과학 데이터를 다중 슈퍼컴퓨터 환경에서 연합학습(Federated Learning, FL)으로 훈련하는 확장 가능한 프레임워크를 제시하며, DOE 리더십급 슈퍼컴퓨터 4대에서의 실증을 통해 크로스-시설 FL의 실용성을 입증한다.

## Motivation

- **Known**: 연합학습은 원본 데이터를 중앙화하지 않고 협업 훈련을 가능하게 하는 기술로 성숙도가 높으며, HPC(High Performance Computing) 인프라는 과학 응용에 필요한 대규모 계산 자원을 제공한다.

- **Gap**: FATE, OpenFL, NVIDIA FLARE, FedML 등 기존 크로스-사일로(cross-silo) FL 프레임워크들은 클라우드와 엔터프라이즈 환경을 중심으로 설계되었으며, HPC 특유의 제약—예측 불가능한 작업 스케줄 대기 지연, 엄격한 방화벽, 이질적 가속기 아키텍처, 독립적 운영 정책, 시스템 중단—을 충분히 다루지 못한다.

- **Why**: 과학 시설은 데이터 개인정보보호와 운영 임베딩된 대규모 데이터 생성이라는 두 가지 장벽에 직면하며, 이를 해결하려면 계산을 데이터로 이동시켜야 한다. 특히 신크로트론 빔라인과 같은 실험 시설에서는 실험당 테라바이트 규모 데이터를 생성한다.

- **Approach**: Advanced Privacy-Preserving Federated Learning (APPFL) 프레임워크를 Globus Compute(훈련 작업 디스패치) 및 Globus Transfer(모델/훈련 설정 전송)와 결합하여 크로스-시설 FL 시스템을 구축하고, 4대의 DOE 리더십급 슈퍼컴퓨터(Aurora, Frontier, Perlmutter, Polaris)를 클라이언트로 사용하여 평가한다.

## Achievement

![Figure 1](figures/fig1.webp)
*Figure 1: 고정 마이크로배치 크기당 처리량 스케일링. 왼쪽 패널은 처리량(초당 샘플)을 보여주며, Aurora는 64개 노드에서 2,100 샘플/초을, Perlmutter 80GB와 Frontier는 각각 1,200과 1,000 샘플/초을 달성한다.*

1. **크로스-HPC 시설 FL 프레임워크 설계 및 구현**: 이질적 HPC 시설 간 훈련을 조율하고, 다양한 모델, 데이터셋, 과학 작업을 지원하며, 통신, 스케줄링, 계산 측면의 HPC 특유 도전을 해결하는 일반화 가능한 프레임워크 제시.

2. **성능 특성화**: GPU 메모리 용량에 의해 주도되는 극단적 처리량 이질성을 발견—Perlmutter 40GB는 ZeRO-3을 사용하여 250 샘플/초이지만, Perlmutter 80GB는 ZeRO-1을 사용하여 1,200 샘플/초를 달성(4배 차이). 통신 비용과 큐잉 역학 특성화를 통해 기존 FL 알고리즘의 부적절함을 드러냄.

3. **알고리즘 평가**: 예약(co-scheduled) 환경에서는 FedAvg, 현실적 큐잉 조건에서는 FedAvg, FedAsync, FedBuff, FedCompass를 평가하여, 이질적 스케줄러와 메모리 제약이 알고리즘 성능에 미치는 영향 분석.

4. **과학적 검증**: SMolInstruct 화학 명령 튜닝 데이터셋(3.3M 샘플)에서 Llama2-7B를 연합 미세조정하여 크로스-HPC 시설 FL이 대규모 과학 모델 개발을 지원함을 입증.

## How

![Figure 2](figures/fig2.webp)
*Figure 2: 예약된 환경에서 모든 4개 슈퍼컴퓨터에 걸친 FedAvg의 훈련 역학*

![Figure 3](figures/fig3.webp)
*Figure 3: 2개 노드를 사용한 현실적 큐잉 조건 하에서 4가지 FL 알고리즘의 테스트 손실 진행*

- **이중 실험 설계**: (1) HPC 예약을 통한 64노드 동기화 공동 스케줄 실행으로 상한 성능 특성화, (2) 표준 큐(2노드)에서의 예약 없는 실행으로 현실적 조건 하 알고리즘 견고성 평가

- **데이터 분배 전략**: 4개 시설에 SMolInstruct 작업군을 분산(Perlmutter: 이름 변환, Polaris: 성질 예측, Aurora: 화학 반응, Frontier: 분자 설명)하여 실제 비-IID(non-IID) 데이터 분포 모방—서로 다른 기관이 특정 하위 도메인에 전문화된 데이터 보유 시나리오 반영

- **현장별 최적화 활용**: 각 슈퍼컴퓨터의 권장 최적화 플래그와 시스템별 설정 적용(Polaris/Frontier는 AWS OFI NCCL/RCCL 플러그인 활용), 메모리 기반 최적화 선택(작은 메모리 GPU는 DeepSpeed ZeRO-3, 큰 메모리는 ZeRO-1)

- **조율 인프라**: Globus Compute로 작업 디스패치, Globus Transfer로 모델 업데이트 교환을 통해 광역 네트워크(wide-area network) 신뢰성 확보 및 현장별 보안/스케줄링 정책 준수

## Originality

- **HPC-FL 통합의 실증적 특성화**: 기존 연구는 주로 가능성 입증에 그쳤으나, 본 논문은 리더십급 슈퍼컴퓨터 4대 간 다중 차원(처리량, 통신, 큐잉)의 이질성을 체계적으로 분석

- **실제 과학 워크로드 검증**: 화학 명령 튜닝 데이터셋 3.3M 샘플 규모의 대규모 언어모델(LLM) 미세조정을 통해 추상적 FL 개념을 과학 응용으로 구체화

- **스케줄러 인식 알고리즘 설계의 필요성 제시**: HPC 큐잉 불확실성 하에서 기존 동기화 중심 알고리즘들의 부족함을 드러내고, 비동기/반동기 알고리즘(FedAsync, FedBuff, FedCompass) 비교를 통해 미래 방향 제시

- **GPU 메모리-통신 트레이드오프 분석**: 메모리 최적화 전략(ZeRO-3 vs ZeRO-1)에 따른 4배 처리량 차이를 정량화하여 이질적 환경에서의 근본적 설계 고민 드러냄

## Limitation & Further Study

- **제한점**:
  - 예약 기반 실험(64노드)과 현실적 큐잉 실험(2노드) 간 규모 차이로 인해 대규모 현실적 시나리오 평가 부족
  - 프라이버시 보장 메커니즘(차등 개인정보보호 등) 미포함—APPFL의 기능이지만 본 논문에서는 미측정
  - 다중 시설 간 네트워크 대역폭 제약 미분석(Globus Transfer 효율만 평가, 병목 분석 부족)
  - 세로운 모델 아키텍처나 비전 모델 같은 다른 과학 도메인 검증 부재

- **후속 연구**:
  - **스케줄러 인식 FL 알고리즘 개발**: HPC 큐잉 지연과 계산 이질성을 사전 예측하여 동적으로 동기화 정책 조정
  - **적응형 메모리-통신 트레이드오프**: 각 시설의 메모리 용량과 네트워크 특성에 따라 ZeRO 설정 자동 최적화
  - **프라이버시-성능 트레이드오프 분석**: 차등 개인정보보호 수준에 따른 수렴 속도 영향 정량화
  - **장기 실행 안정성**: 계획된/예기치 않은 시스템 중단 복구 메커니즘 및 체크포인트 전략 개발
  - **다중 도메인 확장**: 재료과학, 기후 모델링, 바이오인포매틱스 등 추가 과학 응용 검증


## Evaluation

- Novelty: 4/5
- Technical Soundness: 4.5/5
- Significance: 4/5
- Clarity: 4.5/5
- Overall: 4.5/5

**총평**: 본 논문은 과학 응용을 위한 크로스-시설 연합학습의 실용성을 리더십급 HPC 환경에서 처음으로 포괄적으로 입증하였으며, GPU 메모리-통신 트레이드오프와 스케줄러 이질성이라는 구체적 병목을 드러내어 향후 HPC-aware FL 알고리즘 설계에 중요한 기초를 제공한다. 다만 대규모 현실적 조건 평가와 프라이버시 보장 검증 강화가 필요하다.

## Related Papers

- 🏛 기반 연구: [[papers/829_Towards_Foundation_Models_for_Scientific_Machine_Learning_Ch/review]] — 과학 머신러닝을 위한 파운데이션 모델의 분산 학습 구현 사례이다.
- 🧪 응용 사례: [[papers/254_DataJoint_20_A_Computational_Substrate_for_Agentic_Scientifi/review]] — 연합학습을 과학 데이터 분석을 위한 계산 기반으로 활용한다.
- 🧪 응용 사례: [[papers/516_Machine-Learned_Interatomic_Potentials_for_Predicting_Physic/review]] — 분산 학습을 원자간 포텐셜 같은 물리 모델 훈련에 적용한다.
