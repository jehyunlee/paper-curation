---
title: "543_Mlcopilot_Unleashing_the_power_of_large_language_models_in_s"
authors:
  - "Lei Zhang"
  - "Yuge Zhang"
  - "Kan Ren"
  - "Dongsheng Li"
  - "Yuqing Yang"
date: "2023"
doi: "N/A"
arxiv: ""
score: 4.0
essence: "대규모 언어 모델(LLM)을 활용하여 과거 ML 작업의 경험으로부터 지식을 추출하고, 새로운 ML 작업에 대한 솔루션을 즉시 제시하는 프레임워크를 제안한다. 이는 시간이 많이 소요되는 AutoML 방식과 달리 인간의 문제 해결 방식을 모방한 해석 가능한 솔루션을 제공한다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/Specialized_Domain_Agents"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Zhang et al._2023_Mlcopilot Unleashing the power of large language models in solving machine learning tasks.pdf"
---

# MLCopilot: Unleashing the power of large language models in solving machine learning tasks

> **저자**: Lei Zhang, Yuge Zhang, Kan Ren, Dongsheng Li, Yuqing Yang | **날짜**: 2023 | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp) 
*MLCopilot의 오프라인 및 온라인 단계 개요*

대규모 언어 모델(LLM)을 활용하여 과거 ML 작업의 경험으로부터 지식을 추출하고, 새로운 ML 작업에 대한 솔루션을 즉시 제시하는 프레임워크를 제안한다. 이는 시간이 많이 소요되는 AutoML 방식과 달리 인간의 문제 해결 방식을 모방한 해석 가능한 솔루션을 제공한다.

## Motivation

- **Known**: AutoML은 ML 알고리즘 구성의 자동화를 통해 인간의 노력을 줄이지만, (1) 여러 시행착오가 필요해 시간 소모적이고, (2) 과거 경험을 활용하지 못하며, (3) 해석 불가능한 블랙박스 방식이다.

- **Gap**: 반면 인간은 새로운 작업을 접할 때 먼저 작업을 이해하고 과거 유사 경험을 회상하여 솔루션을 도출한다. 이러한 인간의 자연스러운 ML 개발 패턴을 기계 지능으로 모방할 수 있을까?

- **Why**: LLM의 발전으로 자연어 이해와 생성, 그리고 추론 능력이 크게 향상되었으므로, 이를 ML 작업 해결에 활용할 수 있는 가능성이 존재한다.

- **Approach**: 오프라인 단계에서 과거 ML 작업의 이질적 데이터(코드, 설정, 로그)를 정규화하고 LLM을 통해 지식을 추출한 후, 온라인 단계에서 유사 작업 경험을 검색하여 LLM에 프롬프트하여 새로운 작업의 솔루션을 생성한다.

## Achievement

![Figure 1](figures/fig1.webp)
*MLCopilot의 오프라인 및 온라인 단계: 과거 경험으로부터 지식 추출 및 새 작업 해결*

1. **LLM을 ML 작업 해결에 최초 적용**: LLM이 정구조화된 입력(structured inputs)을 이해하고 ML 작업에 대한 심층적 추론을 수행할 수 있음을 입증했다.

2. **고속 솔루션 생성**: 시간 소모적인 최적화 탐색 없이 단일 라운드의 LLM 인터랙션으로 여러 ML 솔루션을 거의 즉시 제시할 수 있다.

3. **해석 가능한 결과 제공**: LLM의 텍스트 이해 및 생성 능력을 활용하여 인간이 이해하고 검증할 수 있는 추론 과정과 함께 ML 솔루션을 제시한다.

4. **경쟁력 있는 성능**: 다양한 실제 ML 벤치마크에서 기존 방법과 비교할 수 있거나 더 우수한 성능을 달성한다.

## How

![Figure 1](figures/fig1.webp)
*MLCopilot의 전체 아키텍처: 오프라인 및 온라인 단계*

### 오프라인 단계 (Offline Stage)

- **데이터 정규화(Canonicalization)**: 이질적 형식의 과거 ML 작업 경험(코드, 설정 파일, 학습 로그 등)을 LLM이 처리 가능한 표준화된 형식으로 변환
- **지식 추출(Knowledge Elicitation)**: LLM을 활용하여 정규화된 경험으로부터 고수준의 추상화된 지식을 추출하고 경험 풀(Experience Pool)과 지식 풀(Knowledge Pool)을 구축

### 온라인 단계 (Online Stage)

- **작업 기술(Task Description)**: 사용자가 새로운 ML 작업을 자연어로 기술
- **경험 검색(Experience Retrieval)**: 작업 기술과 관련 있는 과거 작업들을 경험 풀에서 검색하고 가장 유사한 데모(demonstrations)를 선택
- **지식 검색(Knowledge Retrieval)**: 관련된 고수준 지식을 지식 풀에서 검색
- **LLM 프롬프팅(LLM Prompting)**: 검색된 경험과 지식을 프롬프트 컨텍스트에 포함시켜 LLM에 질의하고, 새로운 작업에 적합한 ML 솔루션을 생성

### 핵심 설계 원칙

- **인-컨텍스트 러닝(In-Context Learning)**: 제한된 컨텍스트 길이 내에서 최적의 경험과 지식을 선택하기 위한 검색 전략 적용
- **구조화된 입력 이해**: 테이블 구조의 경험 기술(structured task descriptions)을 통해 LLM의 이해도 향상
- **추론 메커니즘**: 수학적 사고와 논리적 추론을 지원하는 프롬프트 엔지니어링

## Originality

- **최초의 시도**: LLM을 ML 작업 자동화의 주요 도구로 활용한 최초의 연구 (기존 AutoML과 차별화)

- **새로운 프레임워크**: 검색(retrieve)과 프롬프팅(prompt) 기반의 하이브리드 접근법으로, 과거 경험의 활용과 해석 가능성을 동시에 달성

- **지식 중심 추론**: 단순한 in-context learning을 넘어 오프라인 단계에서 명시적인 지식 추출을 수행하는 두 단계 설계

- **인간-기계 협력**: AutoML의 최적화 중심 접근과 인간의 추론 기반 접근을 결합하는 새로운 패러다임 제시

## Limitation & Further Study

- **LLM의 수학적 추론 한계**: 논문에서 인정하듯이 LLM은 복잡한 수학적 추론과 논리적 사고에서 제한이 있으며, 이는 고급 ML 작업에서 성능 저하의 원인이 될 수 있다.

- **컨텍스트 길이 제약**: 유용한 과거 경험이 많을수록 선택 가능한 정보가 제한되는 in-context learning의 근본적 문제가 남아있다.

- **경험 품질 의존성**: 오프라인 단계의 지식 추출 품질이 전체 성능에 미치는 영향이 명확하지 않으며, 저품질 경험이 포함될 경우의 영향 분석 부족

- **도메인 특수성**: 특정 도메인(예: 이미지 분류, 의료)에 대한 최적화는 충분하나, 다양한 ML 작업 유형(시계열, 그래프 신경망 등)에 대한 적용 가능성 미검증

- **후속 연구 방향**:
  - 더 강력한 추론 능력을 갖춘 LLM 활용 및 Chain-of-Thought 등 고급 프롬프팅 기법 적용
  - 동적 경험 풀 관리 및 온라인 학습 메커니즘 도입
  - 사용자 피드백을 반영한 점진적 성능 개선
  - 더 넓은 범위의 ML 작업 유형에 대한 검증 및 벤치마크 확대

## Evaluation

- **Novelty**: 4.5/5 — LLM을 ML 작업 해결에 적용한 혁신적 아이디어이나, 기존 검색 기반 방법과 LLM의 조합은 다소 단순함

- **Technical Soundness**: 4/5 — 전체 프레임워크는 합리적이고 구현 가능하나, 오프라인 지식 추출의 엄격한 검증 방법이 부족함

- **Significance**: 4/5 — AutoML의 대안으로 해석 가능성과 속도 면에서 실질적 가치가 있으나, 성능에서 기존 방법을 크게 능가하는지는 명확하지 않음

- **Clarity**: 4/5 — 전체 구조와 개념이 명확하게 설명되었으나, 구체적인 프롬프팅 템플릿과 구현 세부사항이 더 자세히 기술될 필요가 있음

- **Overall**: 4/5

**총평**: MLCopilot은 LLM의 강력한 추론 능력과 과거 경험 기반 학습을 결합하여 해석 가능하고 신속한 ML 솔루션 생성을 가능하게 한 혁신적 프레임워크이다. 다만 수학적 추론 한계와 광범위한 성능 검증이 필요하며, 후속 연구를 통해 더욱 강력하고 일반화된 접근법으로 발전할 여지가 있다.

## Related Papers

- 🔄 다른 접근: [[papers/136_Automl-gpt_Automatic_machine_learning_with_gpt/review]] — AutoML-GPT와 MLCopilot 모두 LLM을 활용한 자동 머신러닝을 추구하지만 전자는 자동화, 후자는 경험 기반 솔루션 제시에 중점을 둔다.
- 🔗 후속 연구: [[papers/594_OSDA_Agent_Leveraging_Large_Language_Models_for_De_Novo_Desi/review]] — DS-Agent의 대규모 언어 모델 기반 자동 데이터 사이언스는 MLCopilot의 ML 작업 자동화를 데이터 과학 전반으로 확장한다.
- 🏛 기반 연구: [[papers/542_Mlagentbench_Evaluating_language_agents_on_machine_learning/review]] — 머신러닝에서 언어 에이전트 평가를 위한 MLAgentBench는 MLCopilot의 ML 문제 해결 능력 평가의 벤치마크 기반을 제공한다.
- 🔗 후속 연구: [[papers/463_Large_language_model_agent_for_hyper-parameter_optimization/review]] — MLCopilot의 기계학습 파이프라인 자동화가 하이퍼파라미터 최적화 전용 에이전트를 더 광범위한 ML 작업으로 확장한 발전된 시스템이다.
