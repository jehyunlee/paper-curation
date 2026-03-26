# Foundation Models for Environmental Science: A Survey of Emerging Frontiers

> **저자**: Runlong Yu, Shengyu Chen, Yiqun Xie, Huaxiu Yao, Jared Willard, Xiaowei Jia | **날짜**: 2025 | **Link**: [https://arxiv.org/abs/2504.04280](https://arxiv.org/abs/2504.04280)

---

## Essence

환경 과학에서의 foundation model 적용을 포괄적으로 정리한 survey로, forward prediction, data generation, data assimilation, downscaling, inverse modeling, model ensembling, decision-making의 7가지 주요 use case에 걸친 최신 동향과 모델 개발 프로세스(데이터 수집 → 아키텍처 설계 → 학습 → 튜닝 → 평가)를 체계적으로 다룬다.

## Motivation

- **알려진 것**: 환경 생태계 모델링은 자원 관리, 지속가능 발전, 생태 과정 이해에 필수적
- **Gap**: 전통적 data-driven 방법은 복잡하고 상호연결된 환경 과정 포착에 한계가 있으며, 관측 데이터 부족 문제에도 직면
- **왜 중요한가**: Foundation model의 대규모 사전학습과 universal representation은 환경 과정의 시공간 역학을 포착하고 다양한 응용에 적응할 혁신적 기회 제공
- **접근법**: 환경 과학 전 분야에 걸친 foundation model 적용 사례를 7가지 use case로 분류하고, 모델 개발 전체 프로세스를 체계적으로 정리

## Achievement

1. 환경 과학에서의 FM 적용을 7가지 use case(forward prediction, data generation, assimilation, downscaling, inverse modeling, ensembling, decision-making)로 체계적 분류
2. FM 개발의 전체 프로세스(data → architecture → training → tuning → evaluation)를 환경 과학 맥락에서 상세 정리
3. 다양한 환경 도메인(기후, 기상, 해양, 생태 등)에 걸친 최신 FM 적용 동향 종합
4. 학제간 협력을 위한 향후 기회와 도전 과제 제시

## How

- **Use Case 분류**: 환경 과학의 핵심 문제를 7가지 유형으로 분류하고 각각에 대한 FM 적용 사례와 방법론 정리
- **모델 개발 프로세스**: 데이터 수집(multi-source, multi-modal), 아키텍처 설계(transformer, vision FM, graph FM 등), 학습/튜닝/평가의 전체 파이프라인 상세화
- **도메인 커버리지**: 기후 모델링, 기상 예측, 수문학, 해양학, 생태학 등 환경 과학의 다양한 하위 분야 포괄

## Originality

- **환경 과학 FM Survey**: 환경 과학 분야에 특화된 최초의 포괄적 foundation model survey로, 7가지 use case 분류 체계가 독창적
- **개발 프로세스 통합**: FM 적용 사례뿐 아니라 개발 전체 프로세스를 환경 과학 맥락에서 통합적으로 다룬 점이 차별화
- **학제간 Bridge**: ML/AI 커뮤니티와 환경 과학 커뮤니티 간의 지식 전달을 체계적으로 촉진

**Abstract에서 추출된 독창성 문장**: Foundation models, which leverages large-scale pre-training and universal representations of complex and heterogeneous data, offer transformative opportunities for capturing spatiotemporal dynamics and dependencies in environmental processes, and facilitate adaptation to a broad range of applications.. This survey presents a comprehensive overview of foundation model applications in environmental science, highlighting advancements in common environmental use cases including forward prediction, data generation, data assimilation, downscaling, inverse modeling, model ensembling, and decision-making across domains.. We also detail the process of developing these models, covering data collection, architecture design, training, tuning, and evaluation.. Through discussions on these emerging methods as well as their future opportunities, we aim to promote interdisciplinary collaboration that accelerates advancements in machine learning for driving scientific discovery in addressing critical environmental challenges.

## Limitation & Further Study

### 저자들이 언급한 한계

- 빠르게 발전하는 분야로 최신 모델의 완전한 포괄이 어려움
- 각 use case의 정량적 성능 비교가 제한적

### 자체판단 아쉬운 점

- 개별 FM의 환경 과학 적용에서의 구체적 성능 벤치마크가 부족하여 방법론 비교가 피상적
- 환경 데이터의 특수성(불규칙 시공간 격자, 결측치, 극단 이벤트 등)에 대한 FM의 대응 전략 논의가 부족
- Foundation model의 interpretability/explainability가 환경 정책 결정에 미치는 영향에 대한 논의 미흡
- Computational cost와 탄소 발자국 등 환경 과학에서의 FM 활용의 역설적 측면 미언급

### 후속 연구

- 환경 과학 특화 foundation model 벤치마크 구축
- Multi-modal 환경 데이터(위성, 센서, 시뮬레이션)의 통합 FM 개발
- FM의 interpretability 강화를 통한 환경 정책 의사결정 지원

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 3/5 |
| Technical Soundness | 4/5 |
| Significance | 4/5 |
| Clarity | 4/5 |
| Overall | 4/5 |

**총평**: 환경 과학에서의 foundation model 적용을 7가지 use case와 개발 프로세스로 체계적으로 정리한 시의적절한 survey이다. 학제간 지식 전달의 가치가 크나, 정량적 벤치마크와 환경 데이터 특수성에 대한 깊이 있는 논의가 보완되면 더욱 유용할 것이다.
