---
title: "228_CoAuthor_Designing_a_Human-AI_Collaborative_Writing_Dataset"
authors:
  - "Mina Lee"
  - "Percy Liang"
  - "Qian Yang"
date: "2022.04"
doi: "10.1145/3491102.3502030"
arxiv: ""
score: 4.5
essence: "본 논문은 GPT-3의 창작 및 논증적 글쓰기 지원 능력을 탐구하기 위해 설계된 대규모 인간-AI 협력 글쓰기 데이터셋 CoAuthor를 제시하며, 상호작용 데이터셋 분석을 통해 언어 모델의 역량을 HCI 관점에서 체계적으로 이해할 수 있음을 보여준다."
tags:
  - "cat/AI-Powered_Scientific_Research_Frameworks"
  - "sub/Scientific_Peer_Review"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Lee et al._2022_CoAuthor Designing a Human-AI Collaborative Writing Dataset for Exploring Language Model Capabiliti.pdf"
---

# CoAuthor: Designing a Human-AI Collaborative Writing Dataset for Exploring Language Model Capabilities

> **저자**: Mina Lee, Percy Liang, Qian Yang | **날짜**: 2022-04-29 | **DOI**: [10.1145/3491102.3502030](https://doi.org/10.1145/3491102.3502030)

---

## Essence

![Figure 1](figures/fig1.webp) *CoAuthor 데이터셋: 63명의 작가와 GPT-3의 4개 인스턴스 간 1445개 쓰기 세션에서 수집된 인간-AI 협력 상호작용*

본 논문은 GPT-3의 창작 및 논증적 글쓰기 지원 능력을 탐구하기 위해 설계된 대규모 인간-AI 협력 글쓰기 데이터셋 CoAuthor를 제시하며, 상호작용 데이터셋 분석을 통해 언어 모델의 역량을 HCI 관점에서 체계적으로 이해할 수 있음을 보여준다.

## Motivation

- **Known**: 최근 대규모 언어 모델(GPT-3 등)은 전례 없는 수준의 유창한 텍스트 생성 능력을 제공하며, HCI 커뮤니티에서 상호작용 설계의 새로운 기회로 주목받고 있다. 그러나 이들 모델의 능력은 문맥에 따라 크게 변동한다.

- **Gap**: 언어 모델의 능력은 선행 텍스트, 디코딩 파라미터 등에 따라 크게 달라지므로, 인터뷰나 임시 실험만으로는 상호작용 설계에 필요한 포괄적 이해를 얻기 어렵다. 특히 인간-AI 협력 상황에서 모델의 기여도를 정량화하고 분석하는 것이 매우 도전적이다.

- **Why**: HCI 설계자들이 언어 모델을 효과적으로 활용하려면 이들의 언어 생성 능력, 아이디어 제시 능력, 협력 능력을 구체적인 상황 속에서 정확히 파악해야 한다.

- **Approach**: 이 문제를 해결하기 위해 저자들은 대규모 상호작용 데이터셋(CoAuthor)을 설계하고 수집하여 분석함으로써 언어 모델의 능력을 체계적으로 탐구할 수 있음을 제안한다.

## Achievement

![Figure 2](figures/fig2.webp) *창작과 논증적 글쓰기에서 높은 및 낮은 무작위성(randomness)의 GPT-3 능력 비교*

1. **포괄적 상호작용 데이터셋 구축**: 63명의 작가와 GPT-3의 4개 인스턴스 간 1445개 글쓰기 세션으로부터 수집된 CoAuthor 데이터셋을 제시. 이는 실제 사용자의 자연스러운 상호작용을 기록한 최초의 대규모 인간-AI 협력 글쓰기 데이터셋이다.

2. **언어 모델 능력의 다각적 분석**: 언어 능력(fluency), 아이디어 창출 능력(ideation), 협력 능력(collaboration)의 세 가지 차원에서 GPT-3의 역량을 실증적으로 분석하고, 다양한 "좋은 협력(good collaboration)"의 정의 하에서 모델의 기여도를 평가했다.

3. **재생 인터페이스 제공**: 모든 글쓰기 세션을 재생할 수 있는 대화형 도구를 공개하여, 설계자들이 실제 상호작용의 역학관계를 직관적으로 이해할 수 있게 했다.

## How

![Figure 3](figures/fig3.webp) *CoAuthor 데이터 수집용 인터페이스*

![Figure 4](figures/fig4.webp) *작가와 GPT-3이 작성한 문장의 특성 비교*

- **데이터 수집 설계**: 참여자들이 자유롭게 글을 쓰고, GPT-3의 제안을 요청하거나 거절하고, 제안된 텍스트를 수정할 수 있는 유연한 인터페이스 제공. 창작(creative) 및 논증적(argumentative) 글쓰기 두 가지 작업 유형 포함.

- **능력 평가 메트릭**: 
  - 언어 능력: 유창성(fluency), 문법, 용어 적절성 평가
  - 아이디어 능력: GPT-3 제안이 새로운 아이디어를 포함하는지, 기존 아이디어의 확장인지 분류
  - 협력 능력: 작가의 제안 수용률, 수정 패턴, 최종 텍스트에서의 기여도 분석

- **문맥-종속 분석**: 디코딩 파라미터(temperature), 작업 유형, 작가 특성에 따른 모델 능력의 변동성 조사

- **정성적 분석**: 사용자 피드백, 상호작용 패턴, 협력 품질에 대한 심층 사례 분석

## Originality

- **데이터셋-중심 HCI 연구 패러다임**: 기존의 사용자 인터뷰나 임시 실험 대신 대규모 상호작용 데이터셋을 구축하고 분석하여 기술 능력을 이해하는 새로운 방법론을 제안한다.

- **인간-AI 협력의 실제 기록**: 통제된 실험실 환경이 아닌 자연스러운 글쓰기 상황에서 수집된 진정한 협력 상호작용 데이터로, 실제 사용 맥락을 반영한다.

- **다면적 능력 분석 프레임워크**: 단순 성능 지표가 아닌 언어 능력, 아이디어 능력, 협력 능력의 세 가지 보완적 차원에서 모델을 평가하는 통합적 분석 틀을 제시한다.

- **재생 인터페이스의 설계 기여**: 개별 상호작용을 대규모로 탐색할 수 있는 도구를 제공하여, 설계자들의 "felt understanding"(직관적 이해)을 가능하게 한다.

- **HCI-NLP 학제 간 접근**: 자연언어처리의 데이터셋 중심 방법론을 인간-컴퓨터 상호작용 설계에 적용한 창의적 융합이다.

## Limitation & Further Study

- **모델 특화성**: 본 연구는 GPT-3에만 초점을 맞추고 있어, 다른 대규모 언어 모델(GPT-J, Jurassic-1 등)의 협력 능력 비교가 부재하다. 향후 연구에서 여러 모델의 비교 분석이 필요하다.

- **작업 범위의 제한**: 창작 및 논증적 글쓰기의 두 가지 유형에만 국한되었으며, 다양한 도메인(코딩, 이메일 작성 등)으로의 확대가 필요하다.

- **사용자 샘플 다양성**: 63명의 작가가 참여했으나, 글쓰기 경험, 문화적 배경, 도메인 전문성 등에서 더 다양한 표본 확보가 요구된다.

- **협력 품질의 주관성**: "좋은 협력"의 정의가 여전히 설계자의 관점에 의존적이며, 작가들이 실제로 경험하는 협력의 질과의 불일치 가능성이 있다.

- **장기 사용 효과 미포함**: 모든 세션이 단일 작업이므로, 시간에 따른 사용자-모델 상호작용의 진화나 학습 효과를 분석하지 못했다.

- **후속 연구 방향**: (1) 다양한 도메인과 언어 모델로의 확장, (2) 협력 효과성의 객관적 평가 지표 개발, (3) 사용자 만족도와 생산성 향상에 미치는 실질적 영향 측정, (4) 언어 모델의 한계(hallucination, bias 등)를 드러내는 부정적 사례의 심층 분석

## Evaluation

- **Novelty**: 4.5/5
  - HCI 커뮤니티에서 인간-AI 협력을 체계적으로 분석하기 위해 대규모 상호작용 데이터셋을 활용한 접근이 참신하며, 데이터셋 공개를 통한 커뮤니티 기여가 높다. 다만 단일 모델 분석의 한계가 있다.

- **Technical Soundness**: 4/5
  - 데이터 수집 설계, 분석 방법론, 평가 지표가 전반적으로 견고하고, 정성적·정량적 분석을 균형있게 제시했다. 다만 통계적 유의성 검증이 일부 부족하고, 평가자 간 신뢰도(inter-rater reliability) 보고가 미흡한 부분이 있다.

- **Significance**: 4.5/5
  - HCI 분야에서 대규모 언어 모델의 능력을 이해하고 설계에 활용하는 방식을 근본적으로 제시하며, 공개 데이셋과 도구가 학계와 산업에 큰 영향을 미칠 수 있다. 실제 설계 실무에 직접 적용되는 통찰을 제공한다.

- **Clarity**: 4.5/5
  - 논문의 구조가 논리적이고 명확하며, 동기 부여부터 방법론, 분석 결과까지 일관되게 서술되었다. 시각화와 예시가 풍부하여 독자의 이해를 돕는다. 다만 일부 기술적 세부사항(파라미터 설정 등)의 설명이 더 상세할 수 있다.

- **Overall**: 4.5/5

**총평**: 본 논문은 대규모 언어 모델의 인간-AI 협력 능력을 체계적으로 탐구하기 위한 새로운 데이터셋-중심 방법론을 제시하며, 공개된 CoAuthor 데이터셋과 재생 인터페이스는 HCI 커뮤니티에 매우 실질적인 자산이 될 것으로 예상된다. 다만 단일 모델에 대한 분석과 제한된 작업 범위의 확대가 향후 과제이다.

## Related Papers

- 🏛 기반 연구: [[papers/154_Best_Practices_for_Using_AI_When_Writing_Scientific_Manuscri/review]] — 인간-AI 협력 글쓰기 데이터셋 연구가 과학 논문 작성에서 AI 활용의 구체적 모범 사례 개발에 중요한 실증적 기반을 제공한다
- 🔗 후속 연구: [[papers/886_Wordcraft_A_human-ai_collaborative_editor_for_story_writing/review]] — GPT-3 기반 창작 글쓰기 협력 연구가 스토리 작성을 위한 인간-AI 협력 에디터 개발로 확장되었다
- 🧪 응용 사례: [[papers/889_Xtragpt_Llms_for_human-ai_collaboration_on_controllable_acad/review]] — 인간-AI 협력 글쓰기 패턴 분석이 학술 논문 작성을 위한 제어 가능한 AI 협력 시스템 개발에 직접 활용된다
- 🔗 후속 연구: [[papers/414_Human-llm_coevolution_Evidence_from_academic_writing/review]] — 인간-AI 협력 글쓰기 데이터셋 연구가 학술 글쓰기에서 인간과 LLM의 공진화 현상 분석으로 확장되었다
- 🔗 후속 연구: [[papers/595_Overleafcopilot_Empowering_academic_writing_in_overleaf_with/review]] — 인간-AI 협업 글쓰기 데이터셋 연구로 Overleaf 환경에서의 협업 패턴 분석에 활용할 수 있다.
- 🏛 기반 연구: [[papers/116_Augmenting_the_author_Exploring_the_potential_of_ai_collabor/review]] — 인간-AI 협력 글쓰기 데이터셋 설계의 이론적 기반과 방법론을 제공한다.
- 🧪 응용 사례: [[papers/109_Assisting_in_writing_wikipedia-like_articles_from_scratch_wi/review]] — CoAuthor 데이터셋이 STORM 시스템을 활용한 인간-AI 협업 글쓰기의 실제 사례와 패턴을 분석할 수 있는 구체적 자료를 제공함
- 🔗 후속 연구: [[papers/702_Scholarcopilot_Training_large_language_models_for_academic_w/review]] — 인간-AI 협업 글쓰기 데이터셋을 학술 논문 작성이라는 전문 영역으로 확장하여 더 정교한 협업 모델을 구축한다.
