---
title: "284_Does_writing_with_language_models_reduce_content_diversity_a"
authors:
  - "Vishakh Padmakumar"
  - "He He"
date: "2023"
doi: "미제공"
arxiv: ""
score: 4.2
essence: "인간 피드백으로 미세조정된 언어모델(InstructGPT)을 사용한 협력 글쓰기가 통계적으로 유의미하게 내용 다양성을 감소시키는지를 제어된 실험을 통해 측정한 연구이다. 기본 모델(GPT3)은 유의미한 영향을 보이지 않았다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Academic_Writing_Diversity"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Padmakumar and He_2023_Does writing with language models reduce content diversity arXiv preprint arXiv2309.05196, 2023..pdf"
---

# Does writing with language models reduce content diversity? arXiv preprint arXiv:2309.05196, 2023.

> **저자**: Vishakh Padmakumar, He He | **날짜**: 2023 | **DOI**: 미제공

---

## Essence

![Figure 1](figures/fig1.webp) *세 그룹(Solo, GPT3, InstructGPT)이 작성한 에세이의 내용 다양성 측정. InstructGPT로 공동 작성한 에세이가 가장 유사하고 어휘 및 내용 다양성이 낮음*

인간 피드백으로 미세조정된 언어모델(InstructGPT)을 사용한 협력 글쓰기가 통계적으로 유의미하게 내용 다양성을 감소시키는지를 제어된 실험을 통해 측정한 연구이다. 기본 모델(GPT3)은 유의미한 영향을 보이지 않았다.

## Motivation

- **Known**: 대규모 언어모델(LLM)이 콘텐츠 생성에 광범위하게 사용되고 있으며, 기존 연구에서 LLM 사용이 사용자 의견 형성에 영향을 미칠 수 있음을 보여줌

- **Gap**: 같은 기본 모델에 의존하는 수백만 사용자의 협력 글쓰기가 전체 콘텐츠 다양성을 감소시키는지에 대한 실증적 증거 부재

- **Why**: LLM 기반 글쓰기 보조기가 개별 저자의 고유한 목소리를 희석하여 서로 다른 저자들이 유사한 내용을 생성할 위험이 있으며, 이는 공론장의 다양한 관점 감소로 이어질 수 있음

- **Approach**: 제어된 실험 설계를 통해 세 조건(모델 없음, 기본 GPT3, 미세조정된 InstructGPT)에서 사용자들이 작성한 논설문을 비교하고 다양성 메트릭스 개발

## Achievement

![Figure 2](figures/fig2.webp) *세 그룹의 동질화(homogenization) 점수 비교. InstructGPT 그룹이 유의미하게 높은 점수를 나타냄*

1. **동질화 효과 입증**: InstructGPT로 작성한 에세이가 다른 두 그룹 대비 저자 간 유사도가 통계적으로 유의미하게 높음. 특히 모델이 기여한 주요 포인트가 이러한 동질화의 주요 원인

2. **다양성 감소 확인**: InstructGPT 그룹의 에세이들이 (1) 어휘 다양성(lexical diversity) 감소, (2) 반복되는 고차 n-그램(higher-order n-grams) 증가, (3) 고유한 주요 포인트 수 감소를 보임

3. **모델 종류별 차이**: 미세조정되지 않은 기본 GPT3는 유사한 수준의 모델 기여도에도 불구하고 유의미한 다양성 감소 효과를 보이지 않음. 인간 피드백 강화학습(RLHF)이 모델 출력의 다양성을 감소시키는 것으로 해석

![Figure 3](figures/fig3.webp) *상위 50개 단어(a)와 5-gram(b)의 분포. InstructGPT 그룹에서 더 큰 집중도를 보임*

## How

- **데이터 수집**: Upwork에서 모집한 38명의 영어 모국어 사용자가 New York Times Student Opinion 시리즈의 10개 주제에 대해 약 300단어의 논설문 작성 (총 300편)

- **실험 설계**: 각 참가자가 세 가지 조건(Solo, GPT3, InstructGPT)에서 각각 다른 주제로 에세이 작성. TAB 키 입력 시 5개 텍스트 제안 제시, 최소 5회 쿼리 요구

- **모델 설정**: OpenAI API 사용 (GPT3: davinci, InstructGPT: text-davinci-003), temperature 0.9, frequency penalty 0.5로 높은 엔트로피 설정

- **다양성 메트릭 개발**: 
  - 동질화: 저자 간 유사도 측정 (cosine similarity 기반)
  - 어휘 다양성: Type-Token Ratio, Entropy 등
  - 내용 다양성: 주요 포인트 유니크성, n-gram 반복도
  
- **주요 포인트 추출**: GPT-3.5-turbo를 사용한 zero-shot 요약으로 각 에세이의 핵심 주장 추출, Rouge-L 기반 정렬로 모델/사용자 기여도 귀속

- **모델 기여도 분석**: 키스트로크 레벨 기록 데이터를 활용하여 문자 단위로 모델/사용자 생성 텍스트 구분

## Originality

- **첫 실증적 연구**: 협력 글쓰기 환경에서 LLM 사용이 집단 수준의 콘텐츠 다양성에 미치는 영향을 체계적으로 측정한 최초의 통제 실험

- **미세조정 효과 조사**: RLHF 미세조정 모델이 기본 모델과 다르게 다양성을 감소시킨다는 새로운 발견

- **다층적 다양성 분석**: 어휘 수준, n-gram 수준, 의미적 내용 수준 등 다양한 관점에서 다양성 측정

- **세밀한 속성 분석**: 키스트로크 기록을 통한 정밀한 모델/사용자 기여도 구분 및 주요 포인트 기여도 분석

- **데이터 공개**: 300편의 모든 에세이와 모델 제안 기록 공개로 재현 가능성 및 후속 연구 용이성 확보

## Limitation & Further Study

- **참가자 규모 제한**: 38명의 전문 작가 그룹에서만 실험 (대중 사용자와 다를 수 있음)

- **제한된 작성 도메인**: 논설문만 연구 대상 (다른 장르의 글쓰기에 대한 일반화 불가)

- **모델 범위 제한**: OpenAI 모델(davinci, text-davinci-003)만 테스트 (다른 LLM의 효과는 미확인)

- **요약 기반 메트릭 의존성**: 핵심 포인트 추출이 GPT-3.5 요약의 정확성에 의존 (오류 전파 가능성)

- **인과성 메커니즘 미완성**: 왜 RLHF 미세조정이 다양성을 감소시키는지에 대한 심화 분석 부족

- **후속 연구 방향**: 
  - 광범위한 사용자 집단(학생, 비전문가)에서의 재실험
  - 다른 LLM(Claude, LLaMA 등)의 효과 비교
  - 시간 경과에 따른 다양성 감소 누적 효과 연구
  - RLHF 과정에서의 다양성 손실 메커니즘 규명
  - 다양성 보존 미세조정 방법 개발

## Evaluation

- **Novelty**: 4.5/5 - 협력 글쓰기 환경에서 LLM의 다양성 영향을 최초로 실증하고, RLHF 효과를 구체적으로 규명한 점에서 높은 독창성을 보임. 다만 현상 발견에 그치고 메커니즘 규명은 제한적

- **Technical Soundness**: 4/5 - 제어된 실험 설계, 다층적 메트릭, 정밀한 데이터 기록 등 방법론이 견고함. 다만 요약 기반 속성 분석의 신뢰성 및 표본 대표성 문제 존재

- **Significance**: 4.5/5 - LLM이 콘텐츠 생성 파이프라인에 깊이 통합되는 현재 상황에서 중요한 사회적 함의를 가짐. 모델 설계 및 배포 정책에 영향을 미칠 수 있는 결과

- **Clarity**: 4/5 - 실험 설계와 주요 결과가 명확하게 제시됨. 일부 기술적 세부사항(요약 메트릭)은 부록에 편중되어 있음

- **Overall**: 4.2/5

**총평**: 협력 글쓰기 환경에서 인간 피드백 미세조정된 LLM이 콘텐츠 다양성을 의도하지 않게 감소시킨다는 중요한 발견을 제시한 잘 설계된 실증 연구이다. 다만 현상 규명에 주력하여 근본 원인 분석과 해결 방안 제시는 미흡한 편이며, 제한된 참가자 집단에서의 결과로 인한 일반화 가능성 문제가 있다.

## Related Papers

- 🔄 다른 접근: [[papers/283_Do_Users_Write_More_Insecure_Code_with_AI_Assistants/review]] — AI 어시스턴트 사용의 부정적 측면을 각각 다양성과 보안 관점에서 다른 각도로 조사함
- ⚖️ 반론/비판: [[papers/227_Closing_the_loop_Learning_to_generate_writing_feedback_via_l/review]] — AI가 콘텐츠 다양성을 감소시킨다는 우려와 교육적 피드백 개선에 도움된다는 관점이 상반됨
- 🔗 후속 연구: [[papers/611_People_who_frequently_use_ChatGPT_for_writing_tasks_are_accu/review]] — 언어모델 사용이 글쓰기에 미치는 영향을 다양성 감소에서 정확성 인식으로 확장하여 더 포괄적인 사용자 행동 분석을 제공함
- ⚖️ 반론/비판: [[papers/571_Neural_automated_writing_evaluation_with_corrective_feedback/review]] — 언어 모델과 함께 글쓰기할 때 내용 다양성이 감소한다는 연구는 자동 쓰기 평가 시스템이 창의성에 미칠 부정적 영향을 시사한다.
- ⚖️ 반론/비판: [[papers/107_Artificial_intelligence_tools_expand_scientists_impact_but_c/review]] — 언어 모델과의 글쓰기가 콘텐츠 다양성을 줄이는지 조사하여 본 논문의 탐색 범위 축소 현상을 다른 관점에서 검증한다.
- 🔗 후속 연구: [[papers/409_How_ai_ideas_affect_the_creativity_diversity_and_evolution_o/review]] — 언어모델과의 글쓰기가 콘텐츠 다양성을 감소시킨다는 발견이 AI 아이디어 노출의 창의성과 다양성에 대한 영향을 더 광범위한 맥락에서 검증함
- 🔗 후속 연구: [[papers/641_Prototypical_human-ai_collaboration_behaviors_from_llm-assis/review]] — 언어모델과의 글쓰기가 콘텐츠 다양성에 미치는 영향 연구가 인간-AI 협력 행동 분석을 창작물의 품질 변화 측면으로 확장한 심화 연구임
- ⚖️ 반론/비판: [[papers/227_Closing_the_loop_Learning_to_generate_writing_feedback_via_l/review]] — AI 어시스턴트가 학습에 도움이 된다는 관점과 콘텐츠 다양성을 감소시킨다는 우려가 상반됨
- 🔄 다른 접근: [[papers/283_Do_Users_Write_More_Insecure_Code_with_AI_Assistants/review]] — AI 어시스턴트 사용의 부정적 측면을 각각 보안과 다양성 관점에서 다른 각도로 조사함
- 🏛 기반 연구: [[papers/375_Generating_full_length_wikipedia_biographies_The_impact_of_g/review]] — 언어 모델과의 글쓰기가 콘텐츠 다양성에 미치는 영향 연구로 본 논문의 성별 편향 분석의 이론적 기반을 제공한다.
- 🔄 다른 접근: [[papers/414_Human-llm_coevolution_Evidence_from_academic_writing/review]] — AI 작문 도구 사용이 콘텐츠 다양성에 미치는 영향을 통계적 분석과 실험적 접근법으로 각각 다르게 탐구합니다.
- ⚖️ 반론/비판: [[papers/900_ChatGPT_has_entered_the_classroom_how_LLMs_could_transform_e/review]] — AI 도구 사용이 교육 콘텐츠 다양성에 미치는 부정적 영향을 제시한다
- 🔗 후속 연구: [[papers/607_Patterns_and_purposes_A_cross-journal_analysis_of_ai_tool_us/review]] — AI 도구 사용이 콘텐츠 다양성에 미치는 영향을 학술 저술의 구체적 맥락에서 실증한다
- ⚖️ 반론/비판: [[papers/565_Multi-novelty_Improve_the_diversity_and_novelty_of_contents/review]] — AI 생성 콘텐츠 다양성 감소 문제에 대한 구체적인 해결책을 제시한다
