---
title: "641_Prototypical_human-ai_collaboration_behaviors_from_llm-assis"
authors:
  - "Sheshera Mysore"
  - "Debarati Das"
  - "Hancheng Cao"
  - "Bahar Sarrafzadeh"
date: "2025"
doi: "arXiv:2505.16023v3"
arxiv: ""
score: 4.25
essence: "본 논문은 실제 환경(in-the-wild)에서 LLM 기반 글쓰기 보조 시스템(Bing Copilot, WildChat)을 사용하는 사용자들의 협력 행동을 대규모로 분석한다. 사용자들이 초기 요청 이후 후속 상호작용을 통해 생성물을 개선하고 탐색하는 프로토타입적 행동 패턴(PATHs)을 식별하며, 이들이 작성 의도(writing intent)와 어떻게 상관되는지를 규명한다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Human-AI_Performance_Detection"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Wang et al._2025_Prototypical human-ai collaboration behaviors from llm-assisted writing in the wild.pdf"
---

# Prototypical human-ai collaboration behaviors from llm-assisted writing in the wild

> **저자**: Sheshera Mysore, Debarati Das, Hancheng Cao, Bahar Sarrafzadeh | **날짜**: 2025 | **DOI**: [arXiv:2505.16023v3](https://arxiv.org/abs/2505.16023)

---

## Essence

![Figure 1](figures/fig1.webp)
*그림 1: 사용자들은 원래 요청 이후 후속 상호작용을 통해 LLM과 협력한다. 연구팀은 프로토타입 인간-AI 협력 행동(PATHs)을 식별하고, 사용자의 작성 의도와 PATHs 사이의 통계적 상관관계를 발견했다.*

본 논문은 실제 환경(in-the-wild)에서 LLM 기반 글쓰기 보조 시스템(Bing Copilot, WildChat)을 사용하는 사용자들의 협력 행동을 대규모로 분석한다. 사용자들이 초기 요청 이후 후속 상호작용을 통해 생성물을 개선하고 탐색하는 프로토타입적 행동 패턴(PATHs)을 식별하며, 이들이 작성 의도(writing intent)와 어떻게 상관되는지를 규명한다.

## Motivation

- **Known**: LLM의 자연어 인터페이스가 접근성을 높였고, 사용자-LLM 상호작용 로그가 풍부한 연구 데이터원(data source)이 되고 있다. 선행 연구는 사용자 작업 분류(task classification)나 만족도 추정(satisfaction estimation)에 초점을 맞추었다.

- **Gap**: 실제 환경에서 사용자들이 LLM과 어떻게 협력하는지, 특히 초기 요청 이후의 후속 상호작용을 통해 어떤 협력 행동이 나타나는지에 대한 체계적 분석이 부족하다. 특히 작성 작업에 관한 연구가 미흡하다.

- **Why**: LLM 기반 글쓰기는 보도자료, 채용공고, 논문 심사 등 영향력 있는 영역에서 이미 광범위하게 사용되고 있다. 실제 사용 패턴을 이해하는 것은 LLM 정렬(alignment)과 시스템 개선에 필수적이다.

- **Approach**: 두 개의 대규모 대화 로그 데이터셋(Bing Copilot 250만 세션, WildChat 68,000세션)에서 사용자의 후속 발화(follow-up utterances)를 분류하고, PCA를 통해 공동 발생 패턴을 클러스터링하며, 로지스틱 회귀분석으로 작성 의도와의 상관관계를 분석한다.

## Achievement

![Figure 2](figures/fig2.webp)
*그림 2: 분석 방법론 - PATHs 발견(위)과 원래 요청(OR)의 작성 의도와 PATHs의 상관관계 식별(아래)*

1. **7개의 프로토타입 협력 행동(PATHs) 발견**: 의도 수정(revising intents), 텍스트 탐색(exploring texts), 질문 제시(posing questions), 스타일 조정(adjusting style), 새로운 콘텐츠 주입(injecting new content) 등 7가지 핵심 행동이 데이터셋 전체 분산의 80-85%를 설명한다.

2. **작성 의도별 협력 행동의 통계적 차이 규명**: 브레인스토밍 작업에서 사용자는 다양한 생성물 탐색(exploration)을 요청하고, 긴 텍스트 생성에서는 대화식 피드백을 통한 단계적 생성(staging generation)을 선호하며, 전문/기술 문서 작성 시 학습 목적의 질문(learning-oriented questions)을 제기한다.

3. **배포 간 일관된 행동 패턴**: 서로 다른 기반 LLM, 인터페이스, 사용자 기반을 가진 두 플랫폼에서 공유되는 협력 행동이 확인되어 발견의 일반화 가능성을 증명한다.

## How

![Figure 3](figures/fig3.webp)
*그림 3: (a) 각 후속 발화 유형을 포함하는 세션의 비율 (b) 후속 발화 유형 간 상관관계*

- **후속 발화 분류(fFollowU)**: GPT-4o 기반 분류기로 12개의 후속 발화 유형(RESTATES REQUEST, ELABORATES REQUEST, REQUESTS ANSWERS, REQUESTS MORE OUTPUTS, CHANGE STYLE, ADDS CONTENT, REMOVES CONTENT 등)으로 사용자 발화 분류

- **PCA 기반 PATH 추출**: 각 세션의 후속 발화 유형을 tf-idf 표현으로 변환하고 PCA 적용하여 상호 공동 발생 패턴을 식별. 80-85% 분산 설명력을 갖는 주성분들을 PATH로 정의

- **작성 의도 분류(fWritingI)**: GPT-4o 기반 다중 레이블 분류기로 18가지 작성 의도(IMPROVE TEXT, GENERATE PROFESSIONAL DOC, GENERATE CATCHY TEXT, GENERATE SUMMARY 등) 식별

- **로지스틱 회귀분석**: 작성 의도를 예측변수, PATH를 목표변수로 설정하여 통계적으로 유의한 상관관계 검출. 회귀계수 분석을 통해 의도별 협력 행동 특성화

- **검증 프로토콜**: fFollowU, fWritingI 모두 반복적으로 개발되고 수동으로 검증되어 후속 분석의 정확성 보장

## Originality

- 실제 환경 대규모 데이터(2백만+ 세션)에 기반한 첫 번째 체계적 협력 행동 분석으로, 기존의 UI 기반 글쓰기 보조 도구 분석과 달리 대화형 인터페이스에 초점

- 단순 작업 분류를 넘어 사용자-LLM 상호작용의 **동적 과정(process)**을 특성화하고, 의도-행동 상관관계를 통해 LLM 정렬 연구에 구체적 시사점 제공

- 공개 데이터셋(WildChat) 활용으로 재현성(reproducibility) 보장하면서도, 비공개 Bing Copilot 데이터로 검증하여 발견의 일반화 가능성 증명

- PCA의 선형성으로 인한 직관적 해석가능성(interpretability): 가중치 행렬 W를 통해 후속 발화 유형이 각 PATH에 어떻게 결합되는지 시각화 가능

## Limitation & Further Study

- **분류기의 잠재적 오류**: GPT-4o 기반 분류기의 오차가 누적될 수 있으며, 수동 검증의 샘플 크기가 전체 데이터에 비해 제한적일 수 있음

- **영어-중심 분석**: 영어 세션만 분석하여 다국어 협력 행동의 다양성을 포착하지 못함

- **시간적 동역학 미흡**: PCA는 정적 패턴만 포착하며, 세션 내 후속 발화의 시간적 순서와 진화 과정을 충분히 모델링하지 못함

- **인과성 미확립**: 상관관계 분석만 수행하여 작성 의도가 협력 행동을 **직접 인과적으로** 결정하는지는 불명확

- **후속 연구 방향**: (1) 세션 내 협력 행동의 시간적 진화를 추적하는 동적 모델, (2) 인과 추론을 통한 의도-행동 관계의 인과성 검증, (3) 협력 행동의 글쓰기 품질/사용자 만족도에 대한 인과 효과 분석, (4) 발견된 협력 패턴을 기반으로 한 적응형 LLM 응답 전략 개발

## Evaluation

- **Novelty**: 4.5/5 – 대규모 실제 환경 데이터에 기반한 첫 체계적 협력 행동 분석이며, 의도-행동 상관관계 규명은 새로우나, 개별 행동 유형(탐색, 질문 제시 등)은 선행 소규모 연구에서 언급된 바 있음

- **Technical Soundness**: 4/5 – PCA와 로지스틱 회귀의 표준적 적용이며, 분류기 검증이 명확하나, 시간적 의존성을 고려하지 않은 선형 모델의 한계와 GPT-4o 분류 오차에 대한 민감도 분석 부족

- **Significance**: 4.5/5 – LLM 정렬 연구에 구체적 실증 근거를 제공하고, 플랫폼 간 일관된 패턴이 실제 배포 시스템 개선에 직결될 수 있으나, 품질 개선 효과를 직접 검증하지 않음

- **Clarity**: 4.5/5 – 동기와 방법론이 명확하게 제시되었으나, 일부 분류 체계의 경계(예: ELABORATES REQUEST vs. ADDS CONTENT)가 모호할 수 있음. Figure의 시각화가 효과적

- **Overall**: 4.25/5

**총평**: 본 논문은 실제 환경의 대규모 대화 로그 분석을 통해 LLM 기반 글쓰기 협력의 프로토타입적 행동 패턴을 최초로 체계적으로 규명한 가치 있는 실증 연구이다. 작성 의도별 협력 행동의 차이를 통계적으로 입증하고 LLM 정렬에 구체적 시사점을 제시하는 점이 강점이나, 시간적 역학 모델링과 인과성 검증을 통해 심화될 여지가 있다.

## Related Papers

- 🧪 응용 사례: [[papers/223_Clarify_when_necessary_Resolving_ambiguity_through_interacti/review]] — 명확화 질문을 통한 모호성 해결 프레임워크가 실제 LLM 지원 글쓰기 환경에서 관찰된 사용자-AI 상호작용 패턴의 이론적 설명을 제공함
- 🔗 후속 연구: [[papers/284_Does_writing_with_language_models_reduce_content_diversity_a/review]] — 언어모델과의 글쓰기가 콘텐츠 다양성에 미치는 영향 연구가 인간-AI 협력 행동 분석을 창작물의 품질 변화 측면으로 확장한 심화 연구임
- 🏛 기반 연구: [[papers/414_Human-llm_coevolution_Evidence_from_academic_writing/review]] — 인간-LLM 공진화에 대한 학술 글쓰기 증거가 프로토타입적 협력 행동 패턴의 장기적 발전과 상호 적응 과정의 이론적 배경을 제공함
- 🧪 응용 사례: [[papers/223_Clarify_when_necessary_Resolving_ambiguity_through_interacti/review]] — LLM 지원 글쓰기에서의 인간-AI 협력 행동 분석이 명확화 질문을 통한 상호작용 패턴의 실제 사용 사례를 보여줌
