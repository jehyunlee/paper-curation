# R&D-Agent: Automating Data-Driven AI Solution Building Through LLM-Powered Automated Research, Development, and Evolution

* **저자**: Xu Yang, Xiao Yang, Shikai Fang, Bowen Xian, Yuante Li, Jian Wang, Minrui Xu, Haoran Pan, Xinpeng Hong, Weiqing Liu, Yelong Shen, Weizhu Chen, Jiang Bian (Microsoft Research Asia / Microsoft GenAI)
* **출처**: arXiv:2505.14738 (2025-05-20)
* **링크**: http://arxiv.org/abs/2505.14738

---

## 한줄 요약 (Essence)
LLM 기반 Researcher-Developer 이중 에이전트 프레임워크를 통해 데이터 과학 문제의 반복적 탐색-개발 사이클을 자동화하고, 다중 병렬 탐색 트레이스(Multi-Trace)의 융합으로 MLE-Bench에서 최고 성능을 달성한 ML 엔지니어링 에이전트 시스템이다.

## 연구 동기 (Motivation)
데이터 과학 프로젝트는 본질적으로 반복적(iterative)이다. 피처 엔지니어링, 모델 선택, 하이퍼파라미터 튜닝 등 매 단계에서 피드백을 기반으로 전략을 수정해야 하며, 이는 높은 수준의 전문성과 시간을 요구한다. 기존 LLM 기반 에이전트들은 단일 경로 탐색에 의존하여 최적해에 수렴하지 못하거나 조기 수렴(premature convergence) 문제를 보였다. Kaggle 등 크라우드소싱 플랫폼에서도 여전히 고난도 데이터 과학 문제는 전문가 수준에 못 미치는 자동화 성능을 나타내고 있었다.

## 핵심 성과 (Achievement)
- MLE-Bench에서 기존 최고 에이전트(AIDE o1-preview, 전체 16.9%)를 크게 상회하는 **24.0%** 전체 성공률 달성
- 동일 LLM(o1-preview) 사용 시에도 AIDE 대비 Low 카테고리에서 34.3% -> 48.18%, High 카테고리에서 10.0% -> 18.67%로 대폭 향상
- o3(Research) + GPT-4.1(Development) 하이브리드 구성으로 역할 특화의 효과를 실증
- 오픈소스 공개 (https://github.com/microsoft/RD-Agent)

## 방법론 (How)
R&D-Agent는 두 가지 핵심 설계 원칙으로 구성된다:

**1. Dedicated R&D Role (전담 R&D 역할)**
- **Research Agent**: 성능 피드백을 분석하여 아이디어를 생성하고 탐색 방향을 제안. 과거 경험을 지식 베이스로 축적하여 학습(Learning)과 탐색(Exploration)을 반복
- **Development Agent**: 실행 에러 로그를 기반으로 코드를 반복 디버깅. (1) 샘플 데이터셋에서 실행 가능한 솔루션 개발 -> (2) 전체 데이터셋에서 평가하는 2단계 프로세스
- 각 역할에 최적화된 LLM 배정 가능 (예: o3는 창의적 아이디어 생성에, GPT-4.1은 지시 수행/구현에 특화)

**2. Multi-Trace Idea Explorations (다중 트레이스 탐색)**
- 서로 다른 초기 설정(프롬프트, 모델, 도구, 지식 범위)으로 다수의 탐색 트레이스를 병렬 실행
- 트레이스 간 정보 교환 프로토콜: 이전 트레이스의 탐색 이력과 실패 사례를 후속 트레이스에 제공하여 중복 탐색 방지
- **Multi-Trace Fusion**: 탐색 종료 후 각 트레이스의 피처 엔지니어링, 모델 아키텍처, 후처리 등을 선별적으로 병합하여 복합 솔루션 생성
- 성능 프로파일 기반으로 비생산적 트레이스 종료, 새 트레이스 생성 등 동적 의사결정

실험에서는 2개 독립 트레이스를 각 11시간 실행 후, 마지막 2시간에 코드 모듈, 아이디어, 피드백을 융합하여 최종 솔루션을 선정하는 방식을 사용했다.

## 독창성 (Originality)
- **연구자-개발자 역할 분리**: 단순한 CoT나 ReAct와 달리, 인간 R&D 조직의 분업 구조를 LLM 에이전트에 명시적으로 반영한 점이 독창적이다. 특히 각 역할에 서로 다른 LLM을 배정하는 이종(heterogeneous) 모델 전략은 실용적이면서도 효과적이다.
- **Multi-Trace 융합 메커니즘**: 기존의 단일 경로 탐색이나 단순 앙상블과 달리, 탐색 과정 자체를 병렬화하고 중간 결과를 교환-융합하는 구조는 협력적 탐색(collaborative exploration)이라는 새로운 패러다임을 제시한다.

## 한계 및 개선점 (Limitation)
- **실험 규모가 제한적**: MLE-Bench 단일 벤치마크에서만 평가했으며, 다른 데이터 과학 벤치마크(DSBench, DiscoveryBench 등)에 대한 검증이 없다.
- **Ablation 부족**: Multi-Trace의 각 구성 요소(정보 교환, 융합 전략, 트레이스 수)에 대한 체계적 ablation study가 미완으로, 어떤 요소가 성능 향상에 핵심적인지 불분명하다.
- **비용 분석 부재**: o3 + GPT-4.1 조합은 상당한 API 비용이 예상되나, 비용 대비 성능 분석이 제공되지 않는다. 24시간 * 2 트레이스의 실제 비용이 실용적인지 논의가 필요하다.
- **Technical Report 수준**: 전체적으로 상세한 알고리즘 기술(fusion 전략의 구체적 구현, 지식 베이스 구축 방법 등)이 부족하며, 향후 보완 예정이라고 밝히고 있다.
- **재현성 우려**: 오픈소스이나, Azure OpenAI 서비스 의존 및 고비용 GPU 환경(V100, 220GB RAM) 요구로 일반 연구자의 재현이 어려울 수 있다.

## 종합 평가 (Evaluation)
R&D-Agent는 "인간 R&D 팀의 분업 구조를 LLM 에이전트로 재현한다"는 직관적이면서도 강력한 아이디어를 제시하며, MLE-Bench에서의 SOTA 달성으로 그 효과를 입증했다. 특히 역할별 이종 모델 배정과 Multi-Trace 융합은 향후 LLM 기반 자동화 연구의 중요한 설계 패턴이 될 수 있다. 다만, 현 시점에서는 기술 보고서 수준으로 실험적 검증의 깊이가 부족하며, 비용 효율성과 다양한 도메인에서의 일반화 가능성이 추가로 검증되어야 한다. Microsoft Research의 후속 연구가 기대되는 프레임워크이다.
