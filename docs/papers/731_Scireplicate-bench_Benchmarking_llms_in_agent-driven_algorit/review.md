---
title: "731_Scireplicate-bench_Benchmarking_llms_in_agent-driven_algorit"
authors:
  - "Yanzheng Xiang"
  - "Hanqi Yan"
  - "Shuyin Ouyang"
  - "Lin Gui"
  - "Yulan He (King's College London"
date: "2025"
doi: "10.48550/arXiv.2504.00255"
arxiv: ""
score: 4.25
essence: "본 논문은 최근 NLP 논문들의 알고리즘 설명으로부터 코드를 생성하는 대형언어모델(LLM)의 능력을 평가하는 **SciReplicate-Bench** 벤치마크를 제안한다. 2024년 발표된 36개 NLP 논문의 100개 작업으로 구성되며, 알고리즘 이해와 코드 구현 두 가지 핵심 역량을 평가하는 신규 평가지표(reasoning graph accuracy)를 도입한다."
tags:
  - "cat/LLM-Based_Scientific_Reasoning"
  - "sub/Large_Language_Model_Agents"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Zhu et al._2025_Scireplicate-bench Benchmarking llms in agent-driven algorithmic reproduction from research papers.pdf"
---

# SciReplicate-Bench: Benchmarking LLMs in Agent-driven Algorithmic Reproduction from Research Papers

> **저자**: Yanzheng Xiang, Hanqi Yan, Shuyin Ouyang, Lin Gui, Yulan He (King's College London, The Alan Turing Institute) | **날짜**: 2025 | **DOI**: [10.48550/arXiv.2504.00255](https://doi.org/10.48550/arXiv.2504.00255)

---

## Essence

본 논문은 최근 NLP 논문들의 알고리즘 설명으로부터 코드를 생성하는 대형언어모델(LLM)의 능력을 평가하는 **SciReplicate-Bench** 벤치마크를 제안한다. 2024년 발표된 36개 NLP 논문의 100개 작업으로 구성되며, 알고리즘 이해와 코드 구현 두 가지 핵심 역량을 평가하는 신규 평가지표(reasoning graph accuracy)를 도입한다.

## Motivation

- **Known**: LLM은 기초 프로그래밍 작업 및 일반 소프트웨어 엔지니어링 작업(SWE-bench, MLE-BENCH)에서 상당한 진전을 이루었으나, 학술논문 기반 알고리즘 재현에 특화된 평가 방법은 부재
  
- **Gap**: 기존 벤치마크(MLE-BENCH, MLAgentBench, ML-BENCH)는 논문 이해, 저장소 탐색, 포괄적 테스트 케이스를 모두 포함하지 못함. 실제 peer-reviewed 논문으로부터 알고리즘을 재현하는 것은 (1) 분산된 정보 통합 및 (2) 복잡한 의존성 관리 측면에서 훨씬 어려움

- **Why**: 계산 검증은 많은 학문 분야에서 중요하지만, 코딩 전문성 부족이나 구현 접근성 부족으로 인해 연구자들이 어려움을 겪음. LLM이 학술 알고리즘을 실행 가능한 코드로 변환할 수 있다면 과학 재현성 및 발견 속도 향상 가능

- **Approach**: 논문 이해 전담 Paper Agent와 코드 구현 전담 Code Agent로 구성된 이중 에이전트 시스템(Sci-Reproducer) 개발

## Achievement

1. **SciReplicate-Bench 구축**: 2024년 발표 36개 NLP 논문에서 추출한 100개의 알고리즘 재현 작업. 상세한 주석(reasoning graph annotations), 포괄적 테스트 케이스, 의존성 명시

2. **Reasoning Graph Accuracy 지표 제안**: 알고리즘 이해 정도를 정량화. 생성된 추론 그래프와 참조 그래프 간 유사도 계산 (각 노드는 코드 주석, 엣지는 데이터 흐름 관계)

3. **Sci-Reproducer 프레임워크**: Paper Agent가 문헌에서 알고리즘 개념 해석, Code Agent가 저장소에서 의존성 검색 및 구현 수행

4. **포괄적 실증 분석**:
   - 최고 성능 LLM도 39% execution accuracy에 불과 (극도로 어려운 벤치마크)
   - Reasoning 모델의 "overthinking" 현상 발견 (도구 사용 회피)
   - LLM은 알고리즘 이해는 강하나 실제 구현에서 약함
   - 재현 실패의 주요 원인: 논문의 불완전하거나 불일치하는 설명 → Sci-Reproducer가 효과적으로 해결

## How

**SciReplicate-Bench 작업 구성:**

- **입력 요소**: 함수 시그니처, 알고리즘 설명(LaTeX), 원문 논문 및 인용 참고문헌, 저장소 전체 코드
- **평가 요소**: 참조 구현(CodeBLEU용), Reasoning graph 주석, 의존성 주석(내부/크로스파일/외부 API), 격리된 테스트 환경
- **분석 요소**: 누락/불일치 정보 주석

**Sci-Reproducer 이중 에이전트 작동:**

- Paper Agent: 논문 내용 및 인용 문헌 분석 → 알고리즘 로직 추출
- Code Agent: 저장소 구조 파악 → 의존성 식별 → 코드 생성
- 두 에이전트의 협력적 상호작용으로 알고리즘 이해와 구현 연계

**평가 지표:**

- Execution Accuracy: 테스트 케이스 통과율
- Reasoning Graph Accuracy: 알고리즘 이해도 측정
- CodeBLEU: 코드 유사도
- Dependency/API Recall: 의존성 관리 정확도

## Originality

- **최초 benchmark**: 최신 peer-reviewed NLP 논문(2024)으로부터 알고리즘 재현을 평가하는 첫 번째 벤치마크. 기존 벤치마크는 Kaggle 대회나 GitHub 저장소 기반으로 "논문 이해" 요소 부재

- **Reasoning Graph Accuracy**: 알고리즘 이해를 정량화하는 신규 지표. 데이터 흐름 기반 그래프 구조로 추상적 이해를 객관적으로 평가

- **Dual-agent 설계**: Paper-Code 간 역할 분담으로 복잡한 작업을 체계적으로 해결. 기존 단일 에이전트 접근보다 강화된 구조

- **객관적 평가 강조**: PaperBench, Paper2CodeBench 등 병렬 연구와 달리, execution accuracy 기반 객관적 검증으로 신뢰성 확보

## Limitation & Further Study

- **데이터 규모**: 100개 작업(36개 논문)은 상대적으로 소규모. 다양한 분야, 더 다양한 알고리즘 유형 포함 필요

- **논문 선택 편향**: 2024년 NLP 논문에만 제한. 다른 분야(CV, Systems 등) 및 시간적 다양성 확대 필요

- **모델 제한**: 평가 대상이 제한적일 수 있으며, 새로운 reasoning 모델에 대한 systematic 분석 부족

- **"Overthinking" 현상 심화 분석**: Reasoning 모델이 도구를 회피하는 원인의 근본적 이해 및 개선 방안 부재

- **논문 불완전성 해결**: 불완전한 알고리즘 설명에 대해 자동화된 정보 검색 강화(예: 저자 코드 블로그, GitHub issues 활용) 미흡

- **후속 연구 방향**: 
  - 멀티모달 논문 이해 (수식, 표, 그림 통합)
  - 에이전트 추론 과정 투명성 강화
  - 더 큰 규모의 멀티도메인 벤치마크 구축

## Evaluation

- **Novelty**: 4.5/5 – 논문 기반 알고리즘 재현 벤치마크는 독창적이나, 에이전트 설계 자체는 기존 기법의 조합
  
- **Technical Soundness**: 4/5 – 평가 지표 설계(reasoning graph accuracy)와 task 구성이 견실하나, reasoning graph 자동 생성 및 검증 과정의 신뢰성 문서화 부족
  
- **Significance**: 4.5/5 – 과학 재현성 및 LLM 기반 연구 자동화 분야에서 중요한 리소스 제공. 실무적 임팩트 높음
  
- **Clarity**: 4/5 – 전반적으로 명확하나, task 정의와 평가 절차(특히 reasoning graph 구성)에 대한 상세 설명 필요
  
- **Overall**: 4.25/5

**총평**: SciReplicate-Bench는 과학 논문 기반 알고리즘 재현이라는 중요하면서도 미탐사 영역에 첫 벤치마크를 제시하여 의의 있으나, reasoning graph 검증 방법론의 엄밀성 강화와 벤치마크 규모 확대가 필요하다.

## Related Papers

- 🧪 응용 사례: [[papers/230_Code_llama_Open_foundation_models_for_code/review]] — Code Llama의 코드 생성 능력이 알고리즘 복제 벤치마크에 활용됩니다.
- 🏛 기반 연구: [[papers/086_AI-Researcher_Autonomous_Scientific_Innovation/review]] — 자율적 과학 혁신이 알고리즘 복제 평가의 기반을 제공합니다.
- 🔗 후속 연구: [[papers/145_Autoreproduce_Automatic_ai_experiment_reproduction_with_pape/review]] — 알고리즘 복제가 자동 AI 실험 재현으로 확장됩니다.
- 🧪 응용 사례: [[papers/230_Code_llama_Open_foundation_models_for_code/review]] — Code Llama의 코드 생성 능력이 과학 논문의 알고리즘 복제에 활용됩니다.
- 🔗 후속 연구: [[papers/671_Researchcodebench_Benchmarking_llms_on_implementing_novel_ma/review]] — 연구 논문 아이디어 구현을 알고리즘 복제로 확장한 에이전트 기반 벤치마크
