---
title: "650_RD-Agent_Automating_Data-Driven_AI_Solution_Building_Through"
authors:
  - "Xu Yang"
  - "Xiao Yang"
  - "Shikai Fang"
  - "Bowen Xian"
  - "Yuante Li"
date: "2025.05"
doi: "10.48550/arXiv.2505.14738"
arxiv: ""
score: 4.0
essence: "본 논문은 LLM 기반의 이중 에이전트 프레임워크인 R&D-Agent를 제안하여, 데이터 과학 솔루션 개발을 자동화하고 전문가 수준의 성능에 근접하도록 설계했다. 연구자 에이전트는 성능 피드백을 바탕으로 아이디어를 생성하고, 개발자 에이전트는 오류 피드백을 바탕으로 코드를 개선하는 협력적 탐색 과정을 통해 기존 자동화 솔루션의 한계를 극복한다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/AI-Powered_Research_Planning"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Yang et al._2025_R&D-Agent Automating Data-Driven AI Solution Building Through LLM-Powered Automated Research, Devel.pdf"
---

# R&D-Agent: Automating Data-Driven AI Solution Building Through LLM-Powered Automated Research, Development, and Evolution

> **저자**: Xu Yang, Xiao Yang, Shikai Fang, Bowen Xian, Yuante Li, Jian Wang, Minrui Xu, Haoran Pan, Xinpeng Hong, Weiqing Liu, Yelong Shen, Weizhu Chen, Jiang Bian | **날짜**: 2025-05-20 | **DOI**: [10.48550/arXiv.2505.14738](https://doi.org/10.48550/arXiv.2505.14738)

---

## Essence

![Figure 1](figures/fig1.webp)
*R&D-Agent 프레임워크: 연구자(Researcher) 에이전트와 개발자(Developer) 에이전트가 협력하여 다중 탐색 경로를 병렬로 실행하고 상호 강화하는 구조*

본 논문은 LLM 기반의 이중 에이전트 프레임워크인 R&D-Agent를 제안하여, 데이터 과학 솔루션 개발을 자동화하고 전문가 수준의 성능에 근접하도록 설계했다. 연구자 에이전트는 성능 피드백을 바탕으로 아이디어를 생성하고, 개발자 에이전트는 오류 피드백을 바탕으로 코드를 개선하는 협력적 탐색 과정을 통해 기존 자동화 솔루션의 한계를 극복한다.

## Motivation

- **Known**: 최근 AI/ML 기술이 데이터 과학을 혁신했으나, 증가하는 복잡성으로 인해 전문 지식을 갖춘 데이터 과학자의 수요가 계속 증가하고 있다. Kaggle 같은 크라우드소싱 플랫폼도 고난이도 데이터 과학 문제의 노동 집약적·반복적 특성을 근본적으로 해결하지 못한다.

- **Gap**: 최신 LLM 기반 에이전트들(MLE-Bench, DSBench 등의 벤치마크 기준)이 머신러닝 엔지니어링 작업에서 인간 전문가 대비 현저히 낮은 성능을 보이고 있다. 특히 단일 선형 탐색 경로로는 부분최적(suboptimal) 해에 수렴할 위험이 있다.

- **Why**: 데이터 과학 프로젝트의 성공은 반복적 인사이트(exploring, testing, refining의 순환)에 달려 있으며, 데이터 분포, 샘플 크기, 도메인 제약에 따라 최적 솔루션으로 가는 경로가 근본적으로 달라진다. 전문가는 각 반복의 피드백(특성 중요도, 모델 적합도, 리소스 제약)을 활용해 체계적으로 방법을 적응시킨다.

- **Approach**: 성능 피드백과 실행 오류 피드백이라는 두 가지 피드백 타입에 대응하는 전담 에이전트(Researcher, Developer)와 다중 탐색 경로의 병렬 실행 및 상호 강화(trace fusion) 메커니즘을 통해 효율적인 반복 탐색을 가능하게 한다.

## Achievement

1. **최고 성능 달성**: MLE-Bench 벤치마크에서 기계 학습 엔지니어링 에이전트 중 최우수 성능 달성

2. **이중 에이전트 설계의 효율성**: 역할 분담을 통해 적합한 LLM 모델 할당 가능 (예: o1은 추론/아이디어 생성, GPT-4.1은 명령 추종/구현)

3. **다중 탐색 경로의 상호 강화**: 평행 탐색 흔적(traces)의 선택적 병합(fusion)을 통해 개별 해보다 우수한 합성 솔루션(composite solution) 생성

4. **개발 효율성 향상**: 샘플 데이터셋에서의 반복 디버깅 → 전체 데이터셋 실행의 이단계 접근으로 개발 속도 대폭 개선

5. **오픈소스 공개**: GitHub에서 코드 공개로 재현성 및 접근성 확보

## How

### 이중 역할 전담(Dedicated R&D Role)
- **Researcher 에이전트**: 과거 경험/외부 지식으로부터 학습, 성능 피드백을 분석하여 아이디어 제시, 지식 베이스 구축으로 아이디어 개선
- **Developer 에이전트**: 고수준 자연어 아이디어를 구현 가능한 솔루션으로 구체화, 부분 데이터셋에서 반복 디버깅 후 전체 데이터셋 실행

### 다중 탐색 경로 탐색(Multi-Trace Idea Exploration)
- **다양성**: 각 탐색 흔적(trace)이 이질적 파라미터(프롬프트 전략, LLM 모델, 도메인 도구, 휴리스틱)로 초기화되어 서로 다른 관점에서 해공간 탐색
- **확장성**: 논리적·물리적 병렬성을 지원하여 분산 환경(노드, 컨테이너, 스레드)에서 수평 확장 가능
- **협력 메커니즘**: 중앙 집중식 추적(centralized tracking)으로 성능 프로필(해의 품질, 새로움, 리소스 비용, 오류 복원력) 기반 동적 의사결정 (비효율 흔적 종료, 새 흔적 생성, 흔적 병합)

### 다중 탐색 경로 융합(Multi-Trace Fusion for Stronger Solutions)
- 여러 유망한 흔적의 부분 결과를 조합하여 상호 보완적 장점 활용
- 다양한 입도(feature generation, model architecture, post-processing)에서 구성적 통합 가능
- 사용자 정의 가능한 융합 전략(greedy selection, weighted voting, optimization-guided fusion)

### 유연한 제어
- 성능 임계값, 시간 제약, 탐색 단계 수 등을 기준으로 조기 종료 및 새 흔적 생성 규칙 사용자 정의 가능

## Originality

- **이중 에이전트 아키텍처의 명확한 역할 분담**: 피드백 타입별 전담 에이전트 설계는 인간 연구개발팀 구조의 원리를 체계적으로 LLM 에이전트에 반영한 독창적 접근
- **다중 탐색 경로의 동적 병합 메커니즘**: 단순 병렬 탐색을 넘어 성능 기반의 지능형 추적(trace) 생성, 종료, 병합 전략으로 탐색 공간을 효율적으로 활용
- **샘플 데이터셋 기반 반복 디버깅**: 대규모 데이터셋 학습 비용을 감안한 단계적 개발 프로세스 도입으로 실용성 강화
- **도메인별 맞춤형 제어점 제공**: 사용자가 성능 임계값, 융합 규칙 등을 정의할 수 있는 유연한 API 설계

## Limitation & Further Study

- **계산 비용 분석 부재**: 다중 병렬 탐색이 단일 에이전트 대비 총 계산량 증가에 대한 정량적 비용-편익 분석 미제시
- **LLM 모델 선택의 휴리스틱성**: Researcher에 o1, Developer에 GPT-4.1 할당 기준이 명시적으로 제시되지 않아 다른 모델 조합의 효과 불명확
- **벤치마크 제한**: MLE-Bench만으로 평가되었으며, 다른 데이터 과학 벤치마크(DSBench, DiscoveryBench 등)에서의 성능 미보고
- **융합 전략의 세부 구현**: greedy selection, weighted voting, optimization-guided fusion의 구체적 알고리즘과 성능 차이 미설명
- **실제 프로젝트 사례 부재**: 학술 벤치마크 중심이며 실무 데이터 과학 프로젝트에서의 적용 사례 및 시간/비용 절감 효과 미제시
- **지식 베이스 구축의 메커니즘**: Researcher 에이전트의 지식 베이스가 어떻게 자동으로 구성되고 관리되는지 상세히 설명되지 않음

## Evaluation

- **Novelty**: 4.5/5 
  - 이중 에이전트 역할 분담과 다중 추적 병합 개념은 창신적이나, 개별 요소들(LLM 기반 코드 생성, 피드백 기반 반복)은 기존 연구의 확장

- **Technical Soundness**: 4/5 
  - 아키텍처와 설계 원칙이 논리적이며 실제 구현(오픈소스)을 통해 검증되었으나, 융합 알고리즘, 추적 관리 정책 등의 수학적 형식화 미부족

- **Significance**: 4/5 
  - MLE-Bench에서 최우수 성능으로 기계 학습 엔지니어링 자동화의 중요한 진전을 보여주나, 실무 적용 사례 미제시로 영향 범위 불확실

- **Clarity**: 3.5/5 
  - 전체 프레임워크 개요는 명확하나, 다중 탐색 경로의 동적 제어, 융합 규칙, 지식 베이스 관리 등의 핵심 메커니즘이 충분히 상세하게 설명되지 않음

- **Overall**: 4/5

**총평**: R&D-Agent는 LLM 기반 데이터 과학 자동화의 중요한 진전을 이루었으며, 이중 에이전트 설계와 다중 추적 병합이라는 창신적 개념을 통해 기존 솔루션의 한계를 극복하려는 시도가 높이 평가된다. 다만, 계산 비용 분석, 실무 적용 사례, 핵심 메커니즘의 세부 기술 설명이 보강되면 논문의 실용성과 완성도가 더욱 향상될 것으로 예상된다.

## Related Papers

- 🔄 다른 접근: [[papers/594_OSDA_Agent_Leveraging_Large_Language_Models_for_De_Novo_Desi/review]] — R&D-Agent와 DS-Agent 모두 LLM 기반 데이터 과학 자동화를 추구하지만 이중 에이전트 vs 단일 에이전트 아키텍처를 사용한다.
- 🔗 후속 연구: [[papers/121_Autokaggle_A_multi-agent_framework_for_autonomous_data_scien/review]] — AutoKaggle의 자율 데이터 과학을 위한 다중 에이전트 프레임워크는 R&D-Agent의 협력적 탐색 과정을 캐글 경쟁 환경으로 확장한다.
- 🏛 기반 연구: [[papers/294_Dsbench_How_far_are_data_science_agents_to_becoming_data_sci/review]] — 데이터 과학 에이전트의 발전 수준을 평가하는 DSBench는 R&D-Agent의 전문가 수준 성능 달성 목표를 벤치마킹하는 기준을 제공한다.
