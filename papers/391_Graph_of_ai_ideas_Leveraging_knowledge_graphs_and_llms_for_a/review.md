---
title: "391_Graph_of_ai_ideas_Leveraging_knowledge_graphs_and_llms_for_a"
authors:
  - "Lei Wang"
  - "Chen Ma"
  - "Xueyang Feng"
  - "Zeyu Zhang"
  - "Hao Yang"
date: "2025"
doi: "-"
arxiv: ""
score: 4.0
essence: "본 논문은 지식 그래프(Knowledge Graph)와 대형 언어모델(LLM)을 활용하여 AI 학생들의 개인화된 학습 경로를 제시하고 연구 아이디어 생성을 지원하는 GoAI 시스템을 제안한다. 이는 빠르게 확장되는 AI 문헌의 바다에서 학생들이 겪는 \"정보-혁신 간극\"을 해소한다."
tags:
  - "cat/LLM-Based_Scientific_Reasoning"
  - "sub/Scientific_Hypothesis_Generation"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Wang et al._2025_Graph of ai ideas Leveraging knowledge graphs and llms for ai research idea generation.pdf"
---

# Graph of AI Ideas: Leveraging Knowledge Graphs and LLMs for AI Research Idea Generation

> **저자**: Lei Wang, Chen Ma, Xueyang Feng, Zeyu Zhang, Hao Yang, Jingsen Zhang, Zhiyuan Chen, Jiakai Tang, Xu Chen, Yankai Lin, Wayne Xin Zhao, Zhewei Wei, Ji-Rong Wen | **날짜**: 2025 | **DOI**: -

---

## Essence

![Figure 1](figures/fig1.webp) *GoAI 프레임워크 개요: 문헌 검색 및 필터링 → 지식 그래프 구성 → 경로 생성 → 경로 일관성 검증의 4단계*

본 논문은 지식 그래프(Knowledge Graph)와 대형 언어모델(LLM)을 활용하여 AI 학생들의 개인화된 학습 경로를 제시하고 연구 아이디어 생성을 지원하는 GoAI 시스템을 제안한다. 이는 빠르게 확장되는 AI 문헌의 바다에서 학생들이 겪는 "정보-혁신 간극"을 해소한다.

## Motivation

- **Known**: LLM 기반 학술 보조 도구는 논문 요약, 질문 답변, 아이디어 생성이 가능하다. 또한 교육 분야에서 지식 그래프는 학습 경로 계획과 과정 설계에 성공적으로 적용되었다.

- **Gap**: 기존 LLM 방식은 세 가지 한계가 있다: (1) 교육학적 선행 지식(prerequisite knowledge)을 간과하고 (2) 인용 관계의 의미론적 역할(기초선, 확장, 비교, 비판)을 포착하지 못하며 (3) 연구 발전의 복잡한 구조를 선형적으로만 표현한다.

- **Why**: AI 교육에서 학생들은 급증하는 문헌을 탐색하고, 연구 분야의 발전을 추적하며, 선행 지식을 파악하고, 이를 바탕으로 실현 가능한 혁신 아이디어를 생성해야 한다. 이 과정은 본질적으로 그래프 구조를 가지고 있다: 논문과 아이디어가 노드, 의미론적 인용 관계가 간선, 개념과 기술이 선행 체인을 형성한다.

- **Approach**: 의미론적으로 주석이 달린 인용 관계와 선행 지식 메타데이터를 포함하는 AI 교육용 지식 그래프를 구성하고, 빔 서치(beam search) 기반 경로 탐색으로 개인화된 학습 경로를 생성한 후, Idea Studio에서 구조화된 피드백을 제공한다.

## Achievement

![Figure 2](figures/fig2.webp) *그래프 탐색 및 아이디어 생성의 예시 워크플로우: "Tree of Thoughts" 논문을 핵심 참조 논문으로 하여 발전 궤적과 학습 경로를 생성*

1. **지식 그래프 구성**: AI 교육을 위한 연구 중심 지식 그래프를 개발하여 논문 엔티티, 의미론적으로 주석된 인용 관계(baseline, extension, contrast/ablation, critique/response), 및 선행 개념·기술을 통합한다.

2. **개인화된 학습 경로**: LLM을 에이전트로 활용하여 그래프를 동적으로 탐색하고, 인용 의미론을 고려한 빔 서치로 여러 발전 궤적을 생성하며, 선행 지식의 복잡도를 기준으로 학습 커리큘럼을 구성한다.

3. **구조화된 아이디어 평가**: Idea Studio에서 Chain-of-Thought(CoT) 리뷰어가 학생 아이디어의 참신성(novelty), 명확성(clarity), 실현 가능성(feasibility), 학습 목표 부합도를 종합적으로 평가한다.

4. **실증적 성과**: 학습 성과, 창의성 품질, 인지 부하 측정을 통해 그래프 기반 학습 경로 계획, 창의성 생성, 구조화된 피드백이 학생들의 경계 요약(frontier summarization), 핵심 기술 식별, 실현 가능한 개념 생성 능력을 향상시킴을 입증한다.

## How

![Figure 3](figures/fig3.webp) *GoAI의 참신성 평가 처리 흐름: 기존 문헌과의 비교를 통한 다각적 평가*

### 4단계 GoAI 프레임워크:

1. **문헌 검색 및 필터링**: Semantic Scholar API와 ArXiv API를 활용하여 초기 연구 주제와 관련된 상위 논문(key references)을 검색하고, 이들의 참고 목록(backward extension)과 인용 논문(forward extension)을 양방향으로 확장한다.

2. **지식 그래프 구성**:
   - 각 논문에서 핵심 아이디어(core idea) 추출
   - AI 특화 선행 지식(concepts, skills, tools) 수집
   - 인용 관계를 의미론적으로 분류 (기초선, 확장, 비교, 비판)
   - 논문-개념-기술 간 관계를 간선으로 모델링

3. **경로 생성**:
   - 빔 서치 알고리즘으로 인용 의미론을 고려한 다중 발전 궤적 탐색
   - 선행 지식의 복잡도에 따라 논문을 정렬한 학습 경로 수립
   - "Hint Ideas"를 생성하여 창의적 방향성 제시

4. **일관성 검증**: 다중 에이전트 시스템이 생성된 학습 경로와 아이디어의 학술적 타당성을 반복적으로 검증하고 정제한다.

### 핵심 기술 특성:

- **의미론적 인용 라벨링**: 단순 인용 네트워크를 넘어 각 인용의 기능적 역할을 명시화
- **선행 지식 체인**: 학습 순서를 교육학적으로 정렬
- **LLM-as-Agent**: 그래프 정보를 자연언어 프롬프트로 변환하여 LLM에 입력

## Originality

- **신규 결합**: 지식 그래프의 구조화된 표현과 LLM의 추론 능력을 학술 논문 도메인에 통합하여 학습 경로와 창의성 지원을 동시에 수행한 점이 참신하다.

- **의미론적 인용 관계**: 기존 단순 인용 네트워크 대비, 인용의 기능적 역할(baseline, extension 등)을 명시적으로 모델링하여 논문 간 관계의 깊이를 포착한다.

- **교육학적 설계**: 선행 지식의 복잡도를 학습 경로에 반영하여 순수 학술 그래프를 교육용으로 변환한 점이 차별적이다.

- **다단계 평가 체계**: CoT 기반 구조화된 피드백(참신성, 명확성, 실현 가능성)으로 학생의 아이디어 개선을 투명하게 지원한다.

## Limitation & Further Study

- **확장성 한계**: 본 연구는 AI 분야에 집중되어 있으며, 다른 학문 분야로의 일반화 가능성이 불명확하다.

- **의미론적 라벨링의 수작업**: 인용 관계의 의미론적 분류가 자동화되지 않아 수작업 주석이 필요하거나, 자동 분류의 정확도 평가가 제시되지 않는다.

- **LLM 성능 의존성**: 핵심 아이디어 추출과 선행 지식 식별이 LLM의 기본 모델 성능에 의존하므로, 모델 선택과 성능 편차에 대한 분석이 부족하다.

- **학생 평가의 주관성**: 생성된 아이디어의 "참신성"과 "실현 가능성"을 평가하는 CoT 리뷰어의 평가 일관성(inter-rater reliability) 검증이 제시되지 않는다.

- **후속 연구**:
  - 의미론적 인용 분류의 자동화 및 정확도 개선
  - 타 학문 분야로의 확장 및 도메인 간 이전 학습(transfer learning) 연구
  - 학생-시스템 상호작용의 장기 추적으로 학습 효과의 지속성 평가
  - 실시간 그래프 업데이트 메커니즘 개발

## Evaluation

- **Novelty**: 4/5 - 지식 그래프와 LLM을 교육 + 창의성 지원에 결합한 것은 참신하나, 개별 기술의 새로움은 제한적이다.

- **Technical Soundness**: 3.5/5 - 전반적 설계는 합리적이나, 의미론적 라벨링의 자동화 부재, 평가자 신뢰도 검증 부족, LLM 모델 의존성에 대한 상세 분석 미흡하다.

- **Significance**: 4/5 - AI 교육에서의 실질적 적용 가능성이 높고, 학습 성과 개선을 실증했으나, 다른 분야로의 일반화 가능성이 제한적이다.

- **Clarity**: 4/5 - 전반적으로 명확하고 구조적이며, 예시(Figure 2)를 통해 이해를 돕지만, 의미론적 라벨링 프로토콜과 평가 메트릭의 상세 정의가 보충되면 더 좋을 것이다.

- **Overall**: 4/5

**총평**: GoAI는 지식 그래프의 구조화된 표현과 LLM의 추론 능력을 활용하여 AI 학생들의 개인화된 학습 경로 계획과 창의적 아이디어 생성을 동시에 지원하는 실용적이고 교육학적으로 의미 있는 시스템이다. 다만 의미론적 인용 분류의 자동화, 평가 신뢰도 검증, 타 분야 확장성에 대한 보완이 필요하다.

## Related Papers

- 🔄 다른 접근: [[papers/426_Improving_Scientific_Hypothesis_Generation_with_Knowledge_Gr/review]] — AI 연구 vs 일반 과학 가설 생성으로 지식 그래프 활용의 서로 다른 도메인 적용
- 🔗 후속 연구: [[papers/540_Mir_Methodology_inspiration_retrieval_for_scientific_researc/review]] — AI 아이디어 지식 그래프를 방법론적 영감 검색으로 확장한 연구 지원 시스템
- 🏛 기반 연구: [[papers/079_Ai_idea_bench_2025_Ai_research_idea_generation_benchmark/review]] — AI 아이디어 생성 벤치마크가 지식 그래프 기반 학습 경로의 평가 기준
- 🔄 다른 접근: [[papers/518_Many_Heads_Are_Better_Than_One_Improved_Scientific_Idea_Gene/review]] — 지식 그래프 vs 다중 헤드 접근으로 과학 아이디어 생성의 서로 다른 방법론
- 🔄 다른 접근: [[papers/426_Improving_Scientific_Hypothesis_Generation_with_Knowledge_Gr/review]] — 같은 지식 그래프 활용 접근이지만 AI 연구 아이디어 생성에 특화된 시스템
- 🏛 기반 연구: [[papers/540_Mir_Methodology_inspiration_retrieval_for_scientific_researc/review]] — AI 아이디어 지식 그래프가 방법론적 영감 검색의 구조적 표현 기반
- 🔗 후속 연구: [[papers/632_Predicting_the_future_of_ai_with_ai_High-quality_link_predic/review]] — AI 아이디어 지식 그래프를 활용한 연구 방향 예측으로 링크 예측 접근법을 확장할 수 있다
- 🔗 후속 연구: [[papers/392_Grapheval_A_lightweight_graph-based_llm_framework_for_idea_e/review]] — AI 아이디어의 지식 그래프를 경량 그래프 기반 평가 프레임워크로 확장한 연구다
