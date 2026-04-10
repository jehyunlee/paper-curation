---
title: "043_Accelerating_Drug_Discovery_Through_Agentic_AI_A_Multi-Agent"
authors:
  - "Yao Fehlis"
  - "Paul Mandel"
  - "Charles Crain"
  - "Betty Liu"
  - "David Fuller (Artificial Inc.)"
date: "2025"
doi: "arXiv:2504.00986"
arxiv: ""
score: 4.0
essence: "자동화된 AI 기반 실험(self-driving labs)에서 복잡한 워크플로우를 조정하고, 다양한 기기와 AI 모델을 통합하며, 데이터를 효율적으로 관리하는 통합 플랫폼인 Artificial을 제시한다. NVIDIA BioNeMo 같은 AI/ML 모델을 통해 분자 상호작용 예측 및 생물분자 분석을 가능하게 함으로써 신약 개발을 가속화한다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/AI_Drug_Discovery"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Abdollahi et al._2025_Accelerating drug discovery with artificial a whole-lab orchestration and scheduling system for sel.pdf"
---

# Accelerating drug discovery with artificial: a whole-lab orchestration and scheduling system for self-driving labs

> **저자**: Yao Fehlis, Paul Mandel, Charles Crain, Betty Liu, David Fuller (Artificial Inc.) | **날짜**: 2025 | **DOI**: [arXiv:2504.00986](https://arxiv.org/abs/2504.00986)

---

## Essence

![Figure 1](figures/fig1.webp) *Artificial 플랫폼의 모듈식 및 확장 가능한 아키텍처*

자동화된 AI 기반 실험(self-driving labs)에서 복잡한 워크플로우를 조정하고, 다양한 기기와 AI 모델을 통합하며, 데이터를 효율적으로 관리하는 통합 플랫폼인 Artificial을 제시한다. NVIDIA BioNeMo 같은 AI/ML 모델을 통해 분자 상호작용 예측 및 생물분자 분석을 가능하게 함으로써 신약 개발을 가속화한다.

## Motivation

- **Known**: 자동화 및 AI 기반의 자동 실험실(self-driving labs)이 신약 개발의 비용, 개발 기간, 임상시험 실패율 등의 문제를 해결할 수 있는 유망한 솔루션으로 부상했으며, 가상 스크리닝(virtual screening), 분자 시뮬레이션(molecular simulation), AI 기반 계산 방법들이 약물 개발을 가속화하고 있음.

- **Gap**: 현존하는 자동 실험실은 (1) 복잡한 워크플로우 조정의 어려움, (2) 다양한 기기 및 AI 모델의 통합 문제, (3) 데이터 사일로(data silos)로 인한 AI 성능 저하, (4) 실험 데이터의 다양성과 노이즈로 인한 AI 모델 배포의 복잡성 등의 문제를 해결하지 못함.

- **Why**: 데이터 파편화와 AI 모델의 낮은 재현성은 신약 개발의 신뢰성과 효율성을 크게 저하시키며, 이를 극복하려면 AI 모델을 과학 실험실에 체계적으로 통합할 수 있는 강력한 오케스트레이션 프레임워크가 필수적임.

- **Approach**: Artificial이라는 통합 플랫폼을 제시하여 (1) 실험실 워크플로우를 조정하고, (2) AI 기반 의사결정을 통합하며, (3) 데이터 관리를 원활하게 하고, (4) NVIDIA BioNeMo NIM(컨테이너화된 사전 학습 AI 모델)을 자동 약물 스크리닝 및 실험 프로세스에 통합함.

## Achievement

![Figure 2](figures/fig2.webp) *자동 실험실의 4단계 사이클: Design → Run → Optimize → Learn*

1. **통합 오케스트레이션 플랫폼 구축**: Web Apps(Labs, Assistants, Workflows, LabOps, Digital Twin), 백엔드 Services(Orchestration, Scheduler/Executor, Data Records), Lab API(GraphQL, gRPC, REST), 그리고 적응형 통신 프로토콜(HTTPS, gRPC, Local APIs)을 통해 기기, 소프트웨어, 외부 시스템 간의 완전한 통합을 달성함.

2. **자동화된 워크플로우 최적화**: Scheduler/Executor가 휴리스틱(heuristic)과 제약조건(constraints)을 고려하여 자원 할당을 최적화하고, Digital Twin 기술로 실시간 모니터링 및 시뮬레이션을 가능하게 함으로써 실험 효율성을 극대화함.

3. **폐루프 학습 시스템**: Design-Run-Optimize-Learn의 4단계 순환 구조를 통해 실험 데이터를 체계적으로 로깅하고, AI가 이를 분석하여 가설 검증 및 워크플로우 개선을 자동으로 수행하게 함.

## How

![Figure 3](figures/fig3.webp) *NVIDIA BioNeMo 모델을 통합한 자동 가상 스크리닝 증명 개념(Proof of Concept)*

- **Web Apps 계층**: 
  - Labs: 실험실 환경의 디지털 트윈 구축 및 관리
  - LabOps: 수동 및 자동 R&D 워크플로우의 중앙 허브로서 모니터링, 실행, 조정 수행
  - Workflows: R&D 프로세스 정의, 설정, 관리로 재현성 및 최적화 지원

- **Backend Services 계층**:
  - Orchestration: Python 간소화 방언 또는 그래픽 인터페이스를 통해 실험실 작업 계획 및 요청 관리
  - Scheduler/Executor: 휴리스틱과 배치 처리를 활용한 효율적인 자원 할당 및 워크플로우 실행
  - Data Records: 실험 결과 및 로그를 통합 저장소에 정리

- **Lab API 연결 계층**:
  - GraphQL, gRPC, REST 프로토콜을 통해 하드웨어, 소프트웨어, 외부 시스템 간 통합
  - 실시간 기기 상태 및 프로세스 진행 상황 모니터링

- **적응 계층(Adapters)**:
  - HTTPS, gRPC(SiLA 포함), 로컬 APIs(scikit-learn, TensorFlow, PyTorch)를 통해 보안 통신 지원
  - Python 전체 프로그래밍 언어 및 풍부한 생태계 지원

- **통합 계층**:
  - LIMS(Laboratory Information Management System) 및 ELN(Electronic Lab Notebook)과의 연동
  - 클라우드(EKS/AKS) 및 로컬 환경(MicroK8s) 배포 지원
  - SSL 암호화를 통한 민감한 실험실 데이터 보호

![Figure 4](figures/fig4.webp) *가상 스크리닝 증명 개념 중 자동 반복 횟수*

## Originality

- **처음으로 제시하는 완전 통합 플랫폼**: 실험실 오케스트레이션, AI/ML 모델 통합, 워크플로우 자동화, 데이터 관리를 하나의 통합 시스템으로 구현하여 신약 개발 전체 파이프라인을 지원함.

- **폐루프 자동 학습 사이클**: Design-Run-Optimize-Learn 구조를 통해 실험 데이터를 기반으로 한 지속적인 개선과 가설 검증이 자동으로 이루어지는 시스템을 제시함.

- **NVIDIA BioNeMo 통합**: 사전 학습된 생물분자 AI 모델(NIM)을 컨테이너화하여 자동 가상 스크리닝 워크플로우에 직접 통합함으로써 계산 효율성을 높임.

- **데이터 사일로 해결**: 통합 Data Records 서비스와 표준화된 Lab API를 통해 실험실 전체의 데이터를 하나의 저장소에 통합하여 AI 모델 학습에 필요한 포괄적이고 고품질의 데이터 확보 가능.

- **다양한 프로토콜 및 시스템 지원**: GraphQL, gRPC(SiLA), REST를 동시에 지원하고 Python 생태계와 완벽하게 호환되도록 설계하여 기존 실험실 시스템과의 호환성을 극대화함.

## Limitation & Further Study

- **증명 개념 수준의 검증**: 본 논문은 건식 실험실(dry lab) 환경에서의 가상 스크리닝 사례만을 제시하였으며, 습식 실험실(wet lab)의 로봇, 기기, 수작업이 포함된 복잡한 실제 환경에서의 검증이 부족함.

- **AI 모델 신뢰성 및 검증 체계 부재**: NVIDIA BioNeMo 같은 AI 모델의 예측 정확도, 신뢰도 구간(confidence interval), 모델 불확실성(model uncertainty) 관리에 대한 상세한 논의 및 실제 검증 결과가 제시되지 않음.

- **확장성 및 성능 평가의 부족**: 대규모 실험실(수십 개 이상의 기기, 수백 개의 동시 워크플로우)에서의 Scheduler/Executor의 성능, 응답 시간, 자원 활용률에 대한 벤치마크 데이터가 없음.

- **데이터 보안 및 규제 준수**: 제약 업계의 엄격한 규제 요구사항(FDA 21 CFR Part 11, GxP 준수)에 대한 플랫폼의 대응 방안이 명확하지 않음.

- **비용-효과 분석 부재**: 플랫폼 도입 및 운영 비용 대비 신약 개발 시간 단축, 비용 절감, 성공률 향상 등의 정량적 비교 분석이 없음.

- **후속 연구 방향**:
  - 습식 실험실 환경에서의 로봇 제어 및 여러 장비 간의 동시성(concurrency) 관리에 대한 사례 연구 수행
  - AI 모델 예측의 불확실성을 정량화하고 관리하는 고급 검증 프레임워크 개발
  - 대규모 실험실 배포에서의 성능 최적화 및 스케일링 전략 연구
  - 규제 준수 모듈(audit trail, version control, role-based access control) 강화
  - 실제 제약회사와의 장기 파일럿 수행으로 ROI 및 효과성 검증

## Evaluation

- **Novelty (독창성)**: 4/5
  - 실험실 오케스트레이션, AI/ML 통합, 자동화 워크플로우를 통합한 완전한 플랫폼은 혁신적이며, 폐루프 학습 사이클도 흥미로우나, 개별 기술 요소(스케줄러, API, 디지털 트윈 등)는 기존에 알려진 기술들의 조합임.

- **Technical Soundness (기술적 건전성)**: 3.5/5
  - 플랫폼 아키텍처는 논리적이고 기술적으로 타당하나, 증명 개념이 건식 실험실에만 제한되었으며, 습식 실험실의 복잡성(기기 제어, 동시성, 실패 처리)에 대한 해결책이 충분히 보여지지 않음. AI 모델의 신뢰도 평가 메커니즘이 명확하지 않음.

- **Significance (중요성)**: 4/5
  - 신약 개발의 비용, 기간, 성공률을 개선할 수 있는 중요한 도구로서 산업적 가치가 높으며, 데이터 사일로 문제 해결과 AI 통합은 매우 의미 있음. 다만 실제 임상적 영향이나 검증된 결과가 부족함.

- **Clarity (명확성)**: 4/5
  - 플랫폼 구조와 워크플로우가 명확하게 설명되고, Figure들이 이해를 돕지만, 기술적 상세(Scheduler 알고리즘, 오류 처리, 재시도 로직 등)가 부족하며, 실제 코드나 구현 세부사항이 없음.

- **Overall (종합)**: 4/5

**총평**: 자동 신약 개발 실험실의 오케스트레이션과 AI 통합이라는 중요한 문제를 해결하기 위한 실용적이고 포괄적인 플랫폼을 제시한 논문으로, 아키텍처와 설계 개념은 혁신적이나 실제 환경(습식 실험실)에서의 검증과 AI 모델 신뢰도 평가, 대규모 배포 성능 평가 등이 더 보완되어야 하는 초기 단계의 성숙한 산업 솔루션 논문이다.

## Related Papers

- 🔗 후속 연구: [[papers/099_An_autonomous_laboratory_for_the_accelerated_synthesis_of_in/review]] — 자율 실험실의 무기 고체 합성 자동화가 Artificial 플랫폼의 신약 개발 워크플로우 조정 능력을 소재 과학으로 확장함
- 🏛 기반 연구: [[papers/133_Automating_quantum_computing_laboratory_experiments_with_an/review]] — 양자 컴퓨팅 실험실 자동화 방법이 Artificial의 복잡한 기기 통합과 AI 모델 조정 기술의 기반이 됨
