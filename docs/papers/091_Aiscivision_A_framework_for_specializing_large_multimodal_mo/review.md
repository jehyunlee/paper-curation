---
title: "091_Aiscivision_A_framework_for_specializing_large_multimodal_mo"
authors:
  - "Brian Hogan"
  - "Anmol Kabra"
  - "F. Pacheco"
  - "Laura Greenstreet"
  - "Joshua Fan"
date: "2024"
doi: "arXiv:2410.21480"
arxiv: ""
score: 4.0
essence: "대규모 다중모달 모델(LMM)을 과학 영상 분류 작업에 특화시키는 프레임워크로, 시각적 검색 기반 생성(VisRAG)과 도메인 특화 도구를 활용하여 해석 가능하고 신뢰할 수 있는 AI 시스템을 구현했다."
tags:
  - "cat/AI-Powered_Scientific_Research_Frameworks"
  - "sub/Visual_Scientific_Reasoning"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Hogan et al._2024_Aiscivision A framework for specializing large multimodal models in scientific image classification.pdf"
---

# Aiscivision: A framework for specializing large multimodal models in scientific image classification

> **저자**: Brian Hogan, Anmol Kabra, F. Pacheco, Laura Greenstreet, Joshua Fan, Aaron Ferber, Marta Eichemberger Ummus, Agostinho M. Brito, Olivia Graham, Lillian R. Aoki, C. Drew Harvell, Alexander S. Flecker, Carla Gomes | **날짜**: 2024 | **DOI**: [arXiv:2410.21480](https://arxiv.org/abs/2410.21480)

---

## Essence

![Figure 1: AISciVision 프레임워크의 개념도](figures/fig1.webp)
*Visual Retrieval-Augmented Generation(VisRAG)과 도메인 특화 도구를 결합하여 과학 이미지 분류를 수행하는 AISciVision의 워크플로우. 테스트 이미지에 대해 유사한 긍정/부정 예시를 검색한 후, LMM 에이전트가 여러 라운드에서 도구를 사용하여 분석을 정제하고 최종 예측과 추론 기록(transcript)을 생성한다.*

대규모 다중모달 모델(LMM)을 과학 영상 분류 작업에 특화시키는 프레임워크로, 시각적 검색 기반 생성(VisRAG)과 도메인 특화 도구를 활용하여 해석 가능하고 신뢰할 수 있는 AI 시스템을 구현했다.

## Motivation

- **Known**: GPT-4, Gemini, Llama 같은 대규모 다중모달 모델들이 일반적인 대화형 AI로 광범위하게 활용되고 있으며, 큰 컨텍스트 윈도우를 통해 인컨텍스트 학습(in-context learning)이 가능하다.

- **Gap**: 이러한 범용 LMM들은 의학, 법률, 과학 연구 같은 매우 전문화된 도메인에서 필요한 깊이 있는 도메인 특화 추론 능력이 부족하며, 또한 과학 연구에서는 AI의 투명성과 해석 가능성(interpretability)이 신뢰도 확보에 필수적이다.

- **Why**: 과학 이미지 분류는 전문가 부족으로 인한 접근성 제약과 고비용 레이블링 문제가 있으며, 특히 저데이터 환경에서 신뢰할 수 있는 의사결정 지원 도구가 필요하다.

- **Approach**: 검색 기반 생성(RAG)과 에이전트 기반 도구 사용을 결합하여, 인간 전문가의 이미지 비교 및 도구 기반 검사 과정을 모방하는 프레임워크를 제안한다.

## Achievement

![Figure 2: 세 가지 과학 이미지 분류 데이터셋](figures/fig2.webp)
*양식장(Aquaculture), 병든 피그래스(Eelgrass), 태양광 패널(Solar) 감지 작업의 예시 이미지들*

1. **프레임워크 개발**: VisRAG(시각적 검색 기반 생성)과 도메인 특화 도구를 통합한 혁신적 프레임워크 제안. LMM이 멀티라운드 대화를 통해 도구를 선택적으로 활용하면서 추론 과정을 투명하게 기록한다.

2. **성능 우수성**: 양식장 감지, 병든 피그래스, 태양광 패널 3개 실제 과학 데이터셋에서 완전 지도학습(fully supervised) 모델 및 영점샷(zero-shot) 방식을 능가하면서 동시에 추론 기록을 생성한다.

3. **실제 배포**: 웹 애플리케이션을 통해 생태학자들이 실시간으로 이미지를 분류하고 추론 기록과 상호작용하며 피드백을 제공할 수 있는 실운영 시스템 구축.

## How

- **VisRAG 구성요소**: 훈련 데이터를 임베딩 공간에 매핑하고, 테스트 이미지에 대해 코사인 유사도 기반으로 가장 유사한 긍정/부정 클래스 예시들을 검색한다. 이를 LMM의 프롬프트에 컨텍스트로 포함시킨다.

- **도메인 특화 도구**: 대비도 조정(contrast), 줌(zoom), 팬(pan) 같은 기본 이미지 조작부터 위성 이미지 특화 도구까지 사용자가 지정한 도구들을 LMM 에이전트가 다중 라운드에서 선택적으로 활용한다.

- **에이전트 워크플로우**: (1) VisRAG로 유사 예시 검색 → (2) 비교 분석 요청 → (3) 도구 활용 결정 → (4) 도구 결과 해석 → (5) 확신도와 함께 최종 예측 생성. 각 단계가 자연언어 기록에 남겨진다.

- **모델 무관성(Model-agnostic)**: 임의의 LMM(GPT-4, Gemini 등)과 함께 동작 가능하도록 설계되어 확장성과 유연성을 제공한다.

## Originality

- 과학 이미지 분류에 VisRAG와 인터랙티브 도구 사용을 처음으로 통합한 점이 특징적이다.

- 인간 전문가의 인지 과정(예: 유사 사례 비교, 도구 기반 검사)을 명시적으로 모델 아키텍처에 반영했다.

- 단순 Chain-of-Thought 프롬프팅을 넘어 실제 도구 조작과 피드백 루프를 통한 반복적 정제(iterative refinement)를 구현했다.

- 분류 성능과 함께 추론 투명성을 동시에 달성하려는 통합적 접근이 이전 연구와 차별화된다.

## Limitation & Further Study

- **데이터 의존성**: VisRAG의 성능이 양질의 레이블 훈련 데이터 충분성에 크게 의존하며, 도메인 특화 도구의 사용자 정의 필요성이 확장성 장벽이 될 수 있다.

- **도구 설계 비용**: 새로운 과학 도메인 적용 시 도메인 전문가와의 협력을 통한 도구 커스터마이제이션이 필수적이다.

- **피드백 학습**: 현재는 전문가 피드백을 수집하는 인프라만 구축했으나, 이를 실제로 VisRAG 개선에 반영하는 메커니즘 개발이 향후 과제다.

- **일반화 평가**: 현재 3개 데이터셋만 평가했으므로, 더 다양한 과학 영상 도메인(의료, 현미경, 분자 이미징 등)에서의 성능 검증이 필요하다.

- **계산 효율성**: 멀티라운드 도구 사용과 LMM 호출로 인한 지연시간 및 비용 분석이 부족하다.

## Evaluation

- **Novelty**: 4/5 — 과학 영상 분류에 VisRAG와 인터랙티브 도구를 결합한 것은 신선하나, 개별 기술 자체는 기존 연구의 조합이다.

- **Technical Soundness**: 4/5 — 전반적으로 잘 구성된 방법론이나, 도구 선택 메커니즘의 세부 사항(예: 도구 선택 정책, 라운드 제한 설정)이 충분히 설명되지 않았다.

- **Significance**: 4/5 — 실제 배포된 시스템이며 과학 연구에 직접 기여하는 점은 매우 긍정적이지만, 정량적 성능 개선폭이 명확하게 제시되지 않았다.

- **Clarity**: 3/5 — Figure 1은 직관적이나, 알고리즘 세부사항과 평가 메트릭 정의가 본문에서 명확하지 않다. 특히 VisRAG 임베딩 모델 선택과 도구별 구현 상세가 부족하다.

- **Overall**: 4/5

**총평**: AISciVision은 투명성과 성능을 결합한 실용적인 과학 AI 프레임워크로, 실제 배포를 통해 과학 연구에 기여하는 점이 강점이다. 다만 기술적 세부사항과 광범위한 평가 분석이 보강되면 더욱 견고한 논문이 될 수 있다.

## Related Papers

- 🔗 후속 연구: [[papers/722_Scifibench_Benchmarking_large_multimodal_models_for_scientif/review]] — 과학적 수치 이해를 위한 대규모 다중모달 모델 벤치마킹으로 과학 영상 분류를 확장한다.
- 🧪 응용 사례: [[papers/727_Scimage_How_good_are_multimodal_large_language_models_at_sci/review]] — 과학 이미지에서 다중모달 대규모 언어모델의 성능을 구체적으로 평가한다.
- 🏛 기반 연구: [[papers/737_Sciverse_Unveiling_the_knowledge_comprehension_and_visual_re/review]] — 지식 이해와 시각적 추론을 통해 과학 분야에서의 다중모달 모델 활용 기반을 제공한다.
