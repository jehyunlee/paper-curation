---
title: "069_Agentomics-ML_Autonomous_Machine_Learning_Experimentation_Ag"
authors:
  - "Vlastimil Martinek"
  - "Andrea Gariboldi"
  - "Dimosthenis Tzimotoudis"
  - "Aitor Alberdi Escudero"
  - "Edward Blake"
date: "2025.06"
doi: "미제공"
arxiv: ""
score: 4.0
essence: "LLM 기반 자율 에이전트를 게노믹 및 트랜스크립토믹 데이터 분류 작업에 특화시킨 시스템으로, 기존 대규모 언어 모델 에이전트 방법론을 초과하는 재현성과 일반화 성능을 달성한다."
tags:
  - "cat/AI-Powered_Scientific_Research_Frameworks"
  - "sub/Scientific_Agent_Frameworks"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Martinek et al._2025_Agentomics-ML Autonomous Machine Learning Experimentation Agent for Genomic and Transcriptomic Data.pdf"
---

# Agentomics-ML: Autonomous Machine Learning Experimentation Agent for Genomic and Transcriptomic Data

> **저자**: Vlastimil Martinek, Andrea Gariboldi, Dimosthenis Tzimotoudis, Aitor Alberdi Escudero, Edward Blake, David Cechak, Luke Cassar, Alessandro Balestrucci, Panagiotis Alexiou | **날짜**: 2025-06-05 | **DOI**: [미제공](https://arxiv.org/abs/2506.05542)

---

## Essence

![Figure 1](figures/fig1.webp)
*Agentomics-ML의 아키텍처: 에이전트가 ML 개발 파이프라인의 사전정의된 단계를 따르면서 순차적으로 단계를 완료하여 최종적으로 작동하는 ML 모델을 출력한다.*

LLM 기반 자율 에이전트를 게노믹 및 트랜스크립토믹 데이터 분류 작업에 특화시킨 시스템으로, 기존 대규모 언어 모델 에이전트 방법론을 초과하는 재현성과 일반화 성능을 달성한다.

## Motivation

- **Known**: 최근 LLM 기반 에이전트가 구조화된 벤치마크에서 end-to-end ML 자동화에 유망한 결과를 보이고 있음. AutoML, zero-shot LLM 코드 생성, 그리고 에이전트 기반 접근법들이 ML 자동화 분야에서 개발 중.

- **Gap**: 이러한 기존 방법들이 고차원, 높은 노이즈, 배치 효과(batch effects), 클래스 불균형 등으로 특징지어지는 이질적 생물정보 데이터셋에 적용될 때 일반화 성능 저하 및 낮은 성공률을 보임. 기존 시스템들이 테스트 셋 정보 유출 방지 및 완전한 재현성 있는 환경 구성에 미흡함.

- **Why**: 게노믹/트랜스크립토믹 데이터는 기술적 노이즈, 배치 효과, 높은 차원성(high dimensionality)을 가지고 있으며, 데이터 기반 발견을 위해서는 품질 관리, 정규화, 특성 추출 등의 자동화된 프레임워크가 필수적.

- **Approach**: 생물정보학 도메인 특화 설계를 통해 사전정의된 ML 실험 파이프라인 단계를 따르면서, 반복적인 자기반성(reflection) 메커니즘과 엄격한 테스트 셋 추상화(abstraction)를 결합한 자율 에이전트 시스템을 개발.

## Achievement

1. **높은 성공률 달성**: Agentomics-ML이 93% 이상의 경우에서 작동하는 ML 코드 및 훈련된 모델을 성공적으로 생성하며, 다른 모든 최첨단 에이전트 기반 시스템이 실패하는 복잡한 데이터셋에서도 작동.

2. **기존 에이전트 방법론 초과 성능**: 기존 state-of-the-art 에이전트 기반 방법들(SELA, Data Interpreter, AIDE 등)의 일반화 성능과 성공률을 능가하며, 하나의 벤치마크 데이터셋에서 state-of-the-art 성능을 달성.

3. **도메인 전문가 모델과의 격차 감소**: 도메인 전문가가 구축한 모델의 절대 성능에는 미치지 못하지만, 완전 자율 시스템으로서의 격차를 현저히 축소.

4. **재현성 보장**: 훈련 및 추론을 위한 완전한 스크립트와 필요한 모든 아티팩트를 제공하여 전체 ML 워크플로우의 재현성 보장.

## How

- **사전정의된 단계 기반 구조**: 데이터 탐색 → 데이터 표현 선택 → 모델 아키텍처 설계 → 훈련/추론 스크립트 생성 → 모델 훈련의 순차적 단계를 따름으로써 불필요한 에이전트 계획을 회피.

- **프로그래매틱 검증**: Pydantic AI 프레임워크를 활용하여 생성된 파이썬 파일 및 추론 스크립트의 문법과 형식을 자동 검증하며, 검증 통과까지 에이전트가 다음 단계로 진행하지 못하도록 강제.

- **이중 피드백 메커니즘**: 검증 메트릭과 훈련 메트릭으로부터 정량적 피드백(scalar feedback)을 수집하고, 자기반성 단계에서 과적합(overfitting) 등의 문제를 식별하여 정성적 피드백(verbal feedback)으로 변환하여 다음 반복에 활용.

- **엄격한 테스트 셋 추상화**: 에이전트 개발 사이클 동안 테스트 셋을 완전히 격리하며, 최종 추론 스크립트로만 테스트 성능 평가를 수행하여 정보 유출 방지.

- **보안 격리**: Docker 컨테이너 내에서 모든 에이전트 작업을 격리 실행하여 bash 명령 실행 및 코드 실행의 보안 위험 완화.

- **도메인 기반 데이터 분할**: 데이터 탐색 단계에서 획득한 기술통계와 도메인 정보를 활용하여 무작위가 아닌(non-random) 데이터 분할 전략으로 일반화 추정 개선.

## Originality

- **생물정보학 특화 설계**: AutoML, zero-shot LLM, 기존 에이전트 방법론의 한계를 분석하고 게노믹/트랜스크립토믹 데이터의 특수성(고차원, 배치 효과, 클래스 불균형)을 명시적으로 고려한 시스템 설계.

- **이중 피드백 루프**: 정량적 메트릭에 기반한 자기반성 단계가 정성적 피드백을 생성하고 이를 후속 반복에 활용하는 반복적 개선 메커니즘은 기존 에이전트 시스템과 구별되는 특징.

- **엄격한 재현성 및 평가 프레임워크**: 프로그래매틱 검증, 엄격한 테스트 셋 추상화, 완전한 훈련/추론 스크립트 제공으로 기존 system의 평가 기준 개선.

- **공개 벤치마크 기반 평가**: Genomic Benchmarks와 miRBench 등 게노믹 데이터 특화 벤치마크를 활용하여 도메인 특화 성능 평가 수행.

## Limitation & Further Study

- **절대 성능의 격차**: 도메인 전문가가 구축한 모델의 절대 성능에 비해 여전히 낮은 경우가 대부분이며, 특정 도메인 지식 통합의 한계 존재.

- **제한된 작업 범위**: 분류(classification) 작업에 특화되어 있으며, 회귀(regression), 시계열 분석, 비정상 탐지 등 다른 ML 작업으로의 확장 필요.

- **멀티모달 데이터 통합의 미흡**: 서로 다른 데이터 양식(sequence, expression, metabolite profiles)의 효과적인 통합에 대한 명시적 전략이 부재.

- **LLM 훈련 데이터 영향**: 벤치마크 데이터셋이 LLM 훈련 데이터에 포함되어 있을 가능성에 대한 완전한 통제 불가능.

- **향후 연구 방향**: (1) 회귀 및 클러스터링 작업으로의 확장, (2) 멀티모달 데이터 처리 능력 강화, (3) 더욱 다양한 생물정보학 도메인(단백질 구조 예측, 약물 발견)으로의 적용, (4) 도메인 전문가 지식의 동적 통합 메커니즘 개발.

## Evaluation

- **Novelty**: 4/5 — 게노믹 데이터 특화 설계와 이중 피드백 메커니즘은 참신하나, 기본적인 에이전트 프레임워크는 기존 방법론의 조합.

- **Technical Soundness**: 4/5 — 프로그래매틱 검증, Docker 격리, 엄격한 테스트 셋 추상화 등 기술적으로 견고하나, 복잡한 도메인 요구사항에 대한 적응성은 제한적.

- **Significance**: 4/5 — 게노믹 데이터 분석의 자동화라는 중요한 문제를 다루고 실질적인 성능 향상을 보였으나, 절대 성능이 도메인 전문가 수준에 미치지 못함으로 인해 실무 적용의 임팩트는 부분적.

- **Clarity**: 4/5 — 방법론과 파이프라인이 명확하게 설명되었으나, 일부 기술적 세부사항(특정 LLM 모델, 하이퍼파라미터 선택 기준)에 대한 설명이 제한적.

- **Overall**: 4/5

**총평**: Agentomics-ML은 게노믹 및 트랜스크립토믹 데이터의 ML 분석을 자동화하기 위해 도메인 특화 설계와 엄격한 평가 프레임워크를 결합한 의미 있는 기여를 제시하며, 기존 에이전트 기반 방법론을 현저히 초과하는 성능을 달성했으나, 도메인 전문가 모델과의 격차와 작업 범위의 제한성이 실무 활용성을 다소 제약한다.

## Related Papers

- 🔄 다른 접근: [[papers/693_scAgent_Universal_Single-Cell_Annotation_via_a_LLM_Agent/review]] — 단일 세포 주석을 위한 LLM 에이전트의 다른 접근 방식을 제시한다.
- 🔗 후속 연구: [[papers/193_CellAgent_An_LLM-driven_Multi-Agent_Framework_for_Automated/review]] — 세포 생물학 자동화를 위한 LLM 기반 다중 에이전트 프레임워크로 확장한다.
- 🏛 기반 연구: [[papers/704_SciAgentGym_Benchmarking_Multi-Step_Scientific_Tool-use_in_L/review]] — 다단계 과학 도구 사용 벤치마킹의 이론적 기반을 제공한다.
