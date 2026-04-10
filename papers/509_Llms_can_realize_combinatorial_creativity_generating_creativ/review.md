---
title: "509_Llms_can_realize_combinatorial_creativity_generating_creativ"
authors:
  - "Tianyang Gu"
  - "Jingjin Wang"
  - "Zhihao Zhang"
  - "HaoHong Li"
date: "2024"
doi: "arXiv:2412.14141v2"
arxiv: ""
score: 4.2
essence: "본 논문은 대규모 언어모델(LLM)이 Boden의 조합적 창의성(combinatorial creativity) 이론에 기반하여 과학 아이디어를 생성할 수 있음을 보여준다. 일반화 수준의 검색 시스템과 구조화된 조합 프로세스를 통해 LLM이 이론적으로 근거 있는 창의적 아이디어 생성을 실현할 수 있음을 실증한다."
tags:
  - "cat/Cognitive_AI_Evaluation_and_Benchmarking"
  - "sub/Cognitive_LLM_Evaluation"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Chen and Zhang_2024_Llms can realize combinatorial creativity generating creative ideas via llms for scientific researc.pdf"
---

# LLMs can realize combinatorial creativity: generating creative ideas via LLMs for scientific research

> **저자**: Tianyang Gu, Jingjin Wang, Zhihao Zhang, HaoHong Li | **날짜**: 2024 | **DOI**: [arXiv:2412.14141v2](https://arxiv.org/abs/2412.14141v2)

---

## Essence

본 논문은 대규모 언어모델(LLM)이 Boden의 조합적 창의성(combinatorial creativity) 이론에 기반하여 과학 아이디어를 생성할 수 있음을 보여준다. 일반화 수준의 검색 시스템과 구조화된 조합 프로세스를 통해 LLM이 이론적으로 근거 있는 창의적 아이디어 생성을 실현할 수 있음을 실증한다.

## Motivation

- **Known**: LLM을 활용한 연구 아이디어 생성에 대한 최근 연구들이 증가하고 있으며, 이들은 참신성(novelty)에 중점을 둔다.

- **Gap**: 기존 LLM 기반 아이디어 생성 연구들은 계산 창의성(computational creativity) 이론적 기초를 간과하고 있으며, 참신성만 추구하면서 **가치(value)** 측면을 무시하고 있다. 또한 평가 메커니즘이 단순한 의미론적 유사성에만 의존한다.

- **Why**: Boden의 개념 공간 이론에 따르면 창의성은 참신성과 가치를 동시에 충족해야 하며, 특히 조합적 창의성은 서로 다른 영역의 개념을 새로운 방식으로 결합하는 과정이다. 이론적 기틀 없이는 LLM의 창의적 잠재력을 제대로 활용할 수 없다.

- **Approach**: (1) Boden의 조합적 창의성 이론을 명시적으로 구현하는 에이전트 아키텍처 설계, (2) 일반화 수준의 검색 시스템으로 도메인 간 지식 발견 가능, (3) 구조화된 조합 프로세스로 체계적 아이디어 생성.

## Achievement

![Figure 1](figures/fig1.webp)
*그림 1: 조합적 창의성 에이전트 핵심 구조*

![Figure 2](figures/fig2.webp)
*그림 2: 반구조화된 아이디어 데이터 포맷과 수준별 검색 시스템*

1. **이론적 정합성**: Boden의 창의성 이론과 "네 가지 P(Four P's)" 프레임워크(Person, Process, Product, Press)를 LLM 시스템에 직접 매핑하여 이론과 실제 구현의 간극 해소.

2. **실증적 성과**: OAG-Bench 데이터셋에서 기존 기준 방식 대비 유사도 점수 7%-10% 향상, 실제 연구 발전과 일치하는 아이디어 생성 능력 입증.

3. **평가 방법론 개선**: 단순 의미론적 유사성을 넘어 역사적 과학 발전과의 정렬성을 통해 창의성 평가의 객관성 강화.

## How

![Figure 3](figures/fig3.webp)
*그림 3: 제안 프레임워크와 기준 방식의 유사도 점수 비교 분석*

- **일반화 수준 검색 시스템(Generalization-level Retrieval System)**:
  - 개념들을 다양한 추상화 수준으로 매핑하여 서로 다른 도메인의 개념 간 의미 있는 연결 가능
  - 반구조화된 데이터 포맷으로 개념의 계층적 관계 표현

- **조합 프로세스(Combinatorial Process)**:
  - 기존 개념의 성분을 체계적으로 분석(decomposition)
  - 분석된 성분들을 새로운 방식으로 재결합(recombination)
  - 각 조합에 대해 가치 평가(value assessment) 수행

- **에이전트 아키텍처**:
  - 구조화된 프롬프팅(structured prompting)을 통해 LLM의 인지 과정을 창의성 이론에 맞춤
  - 도메인 간 지식 교차 검색으로 예상 밖의 연결 유도
  - 반복적 생성-평가 루프(Geneplore 모델 구현)

## Originality

- **이론-실증 연결**: Boden의 조합적 창의성 이론을 LLM 시스템에 처음으로 명시적이고 체계적으로 구현한 시도. 기존 연구들은 창의성 이론을 간과하거나 피상적으로만 적용했다.

- **다층적 평가 틀**: 참신성(novelty)과 가치(value) 양측면을 동시에 고려하는 평가 프레임워크 제시. 역사적 과학 발전 데이터를 활용하여 생성된 아이디어의 실제 영향력을 검증하는 방식 도입.

- **도메인 간 지식 발견**: 일반화 수준의 검색을 통해 도메인 경계를 넘는 창의적 연결을 체계적으로 유도. 단순 키워드 기반이 아닌 개념의 추상적 유사성에 기반한 검색.

- **구조화된 창의 프로세스**: 자유로운 브레인스토밍이 아니라 이론적으로 검증된 조합 방식을 단계적으로 구현. Wallas의 단계 이론(preparation, incubation, inspiration, verification)을 계산 시스템에 구현.

## Limitation & Further Study

- **평가 데이터셋의 한계**: OAG-Bench가 컴퓨터과학 도메인 중심이므로, 다른 분야(생물학, 의학, 물리학 등)에서의 일반화 가능성이 불명확. 향후 다학제적 평가 필요.

- **가치 평가의 형식화 부족**: 창의성의 "가치" 기준을 역사적 관점으로만 평가하고 있으나, 실시간 아이디어 생성 상황에서 미래 가치 판단이 어려움. 전문가 평가나 다중 기준 평가 도입 필요.

- **인과관계 검증 부재**: 역사적으로 발생한 아이디어와의 유사성만 평가하고, 해당 아이디어가 실제로 영향을 미쳤는지 또는 LLM이 의도적으로 생성했는지 검증하지 않음.

- **계산 복잡도**: 다중 수준의 검색과 반복적 평가 프로세스의 계산 비용에 대한 분석 부족. 대규모 실제 적용 시 실시간성 확보 방안 필요.

- **향후 연구 방향**:
  - 변환적 창의성(transformational creativity)으로 확장
  - 사용자 피드백을 반영한 대화형 아이디어 생성 시스템
  - 다중 도메인, 다중 언어 환경에서의 성능 평가
  - 생성된 아이디어의 실제 실행 가능성(feasibility) 평가 추가


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4/5
- Significance: 4.5/5
- Clarity: 4/5
- Overall: 4.2/5

**총평**: 본 논문은 LLM 기반 아이디어 생성에 창의성 이론을 의도적으로 적용한 점에서 이론과 실제의 간극을 좁히는 의미 있는 기여를 하고 있으나, 평가 방법론의 제약과 실제 과학적 임팩트 검증 부족이 한계이다. 향후 다중 도메인 검증과 미래 가치 판단 메커니즘의 개발이 논문의 영향력을 더욱 높일 수 있을 것으로 예상된다.

## Related Papers

- 🔄 다른 접근: [[papers/577_Nova_An_iterative_planning_and_search_approach_to_enhance_no/review]] — Nova의 반복적 계획 수립과 조합적 창의성 이론은 모두 연구 아이디어 생성을 위한 서로 다른 체계적 접근법입니다
- 🔗 후속 연구: [[papers/494_Liveideabench_Evaluating_llms_scientific_creativity_and_idea/review]] — LiveIdeaBench의 과학적 창의성 평가는 조합적 창의성 이론 기반 아이디어 생성의 검증 방법을 제공합니다
- 🧪 응용 사례: [[papers/669_Researchbench_Benchmarking_llms_in_scientific_discovery_via/review]] — ResearchBench의 과학 발견 벤치마크는 조합적 창의성으로 생성된 아이디어의 실제 평가 플랫폼입니다
- 🔄 다른 접근: [[papers/577_Nova_An_iterative_planning_and_search_approach_to_enhance_no/review]] — 조합적 창의성 이론과 반복적 계획 수립은 모두 연구 아이디어 생성을 위한 서로 다른 체계적 접근법입니다
- 🧪 응용 사례: [[papers/669_Researchbench_Benchmarking_llms_in_scientific_discovery_via/review]] — 조합적 창의성으로 생성된 과학 아이디어는 ResearchBench의 영감 검색과 가설 구성 작업에서 실제로 평가될 수 있습니다
- 🏛 기반 연구: [[papers/409_How_ai_ideas_affect_the_creativity_diversity_and_evolution_o/review]] — LLM의 조합적 창의성 실현 가능성에 대한 연구가 AI 아이디어가 인간 창의성에 미치는 복잡한 영향을 이해하는 이론적 배경을 제공함
- 🔗 후속 연구: [[papers/153_Best_humans_still_outperform_artificial_intelligence_in_a_cr/review]] — LLM의 조합적 창의성 실현 가능성을 보여주어 본 논문의 창의성 평가를 다른 창의성 유형으로 확장한다.
