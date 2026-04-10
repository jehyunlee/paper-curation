---
title: "238_Controllable_citation_sentence_generation_with_language_mode"
authors:
  - "Nianlong Gu"
  - "Richard H. R. Hahnloser"
date: "2022"
doi: "arXiv:2211.07066"
arxiv: ""
score: 4.0
essence: "본 논문은 저자가 인용 의도(citation intent)와 핵심 키워드를 명시적으로 지정하여 인용 문장 생성을 제어할 수 있는 언어 모델 기반 접근법을 제안한다. 지도 학습 미세조정과 강화학습(PPO)을 결합하여 생성 품질과 제어 가능성을 동시에 향상시킨다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Citation_Context_Generation"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Gu and Hahnloser_2022_Controllable citation sentence generation with language models.pdf"
---

# Controllable Citation Sentence Generation with Language Models

> **저자**: Nianlong Gu, Richard H. R. Hahnloser | **날짜**: 2022 | **DOI**: [arXiv:2211.07066](https://arxiv.org/abs/2211.07066)

---

## Essence

![Figure 1](figures/fig1.webp) *언어 모델을 이용한 인용 문장 생성 워크플로우: 지도 학습 미세조정 후 PPO를 통한 제어 가능성 최적화*

본 논문은 저자가 인용 의도(citation intent)와 핵심 키워드를 명시적으로 지정하여 인용 문장 생성을 제어할 수 있는 언어 모델 기반 접근법을 제안한다. 지도 학습 미세조정과 강화학습(PPO)을 결합하여 생성 품질과 제어 가능성을 동시에 향상시킨다.

## Motivation

- **Known**: 기존 인용 문장 생성 연구(Xing et al., 2020; Ge et al., 2021)는 sequence-to-sequence 방식으로 완전 자동화된 생성에만 집중하였으며, 저자의 의도를 반영하지 못함.

- **Gap**: 저자들은 종종 특정 인용 의도(배경 정보 제공, 방법론 소개, 결과 비교 등)나 포함되어야 할 키워드를 명확히 염두에 두고 있으나, 기존 시스템은 이러한 제어 속성(control attributes)을 받아들이지 못함.

- **Why**: 생성된 인용 문장이 저자의 의도와 맞지 않을 때, 저자가 명시적으로 속성을 변경하여 원하는 결과를 얻을 수 있어야 함. 이는 실제 학술 저술 프로세스의 상호작용성(interactivity)과 저자의 자율성을 증대.

- **Approach**: (1) 구조화된 프롬프트 템플릿을 설계하여 원고 맥락, 피인용 논문 정보, 제어 속성을 통합하고 언어 모델을 미세조정; (2) 의도 일치도(Intent Alignment Score), 키워드 회수율(Keyword Recall), 유창성 점수(Fluency Score), ROUGE-F1을 제어 가능성 메트릭으로 정의하고 PPO의 보상 함수로 활용하여 모델 최적화.

## Achievement

![Figure 1](figures/fig1.webp) *제안 방법의 전체 워크플로우: 지도 학습과 강화학습 단계*

1. **통합 제어 프레임워크 개발**: 단일 언어 모델 내에서 인용 속성 추론(uncontrolled mode)과 사용자 지정 속성 기반 생성(controlled mode)을 모두 수행 가능하게 함. 이를 통해 사용자가 필요에 따라 자동 추론 모드와 명시적 제어 모드를 유연하게 전환 가능.

2. **다중 메트릭 기반 제어 가능성 평가 체계**: 의도 정렬성, 키워드 포함률, 유창성, 내용 관련성을 종합적으로 측정하는 평가 메트릭 구성. 이를 바탕으로 PPO를 통한 강화학습으로 모델의 제어 가능성을 기존 지도 학습만으로는 달성하기 어려운 수준까지 향상.

3. **포괄적 데이터셋 구성**: 문맥 정보와 인용 속성을 파싱한 대규모 데이터셋을 구축하여 향후 제어 가능 인용 생성 연구의 토대 제공.

## How

![Figure 2](figures/fig2.webp) *Galactica-6.7B 모델의 비제어 모드에서 생성한 인용 문장 예시*

### 지도 학습 미세조정 (Supervised Fine-tuning)

- **구조화된 입력 템플릿 설계**: 원고 제목/초록, 피인용 논문 제목/초록, 원고 내 선행 텍스트, 인용 의도, 키워드, 목표 인용 문장을 계층적으로 배열한 프롬프트 구성.

- **이중 목적 학습 목표**: 식 (1)에 따라 $\log p(A|C) + \log p(S|A,C)$를 최대화하도록 최적화. 이를 통해 모델이 문맥 C에서 속성 A를 추론하고, A와 C가 주어졌을 때 문장 S를 생성하도록 동시 학습.

- **모델 선택**: GPT-NEO 같은 decoder-only 모델과 BART 같은 encoder-decoder 모델 모두에 적용 가능하도록 설계. Decoder-only 모델은 문맥 토큰을 마스킹하여 손실 계산 범위 제한.

### 제어 가능성 평가 메트릭

- **의도 일치도 (Intent Alignment Score, IAS)**: SciBERT의 [CLS] 토큰 표현을 2층 완전 연결층에 입력하여 세 가지 인용 의도('background', 'method', 'result')에 대한 로짓 계산 후 소프트맥스 적용 (식 2). SciCite 데이터셋으로 별도 훈련.

- **키워드 회수율 (Keyword Recall, KR)**: 제어 키워드가 생성 문장에 얼마나 포함되는지 측정.

- **유창성 점수 (Fluency Score, FS)**: 참조 없는(reference-less) 평가 방식으로 생성 문장의 자연스러움 평가.

- **ROUGE-F1 점수**: 생성 문장과 인간 작성 인용 문장 간 어휘 유사도 측정 (내용 관련성 대리 지표).

### 강화학습을 통한 제어 가능성 향상

- **Proximal Policy Optimization (PPO) 적용**: 위 네 메트릭을 가중합으로 결합한 보상 함수 정의. 초기 지도 학습 모델로부터 시작하여 PPO로 정책 최적화하여 제어 가능성 메트릭 개선.

- **이중 모드 최적화**: 제어 모드(사용자 지정 속성 사용)와 비제어 모드(자동 추론 속성 사용) 모두에서 성능 개선 추구.

## Originality

- **제어 속성과 생성의 통합**: 기존 연구들이 단일 속성(주로 인용 의도만) 제어에 집중한 반면, 본 논문은 의도+키워드 복합 제어를 단일 모델에서 구현.

- **구조화된 프롬프트 설계**: 명확한 섹션 구분자(###)를 이용하여 다양한 문맥 소스를 체계적으로 통합하는 템플릿 개발. 이는 decoder-only와 encoder-decoder 모델 모두에 적용 가능한 일반화 가능한 방법.

- **강화학습을 통한 메트릭 기반 최적화**: 제어 가능성을 직접 측정하는 다중 메트릭을 보상 함수로 활용하여 지도 학습의 한계를 보완. 기존 prompt-based 접근을 넘어 RL을 통한 체계적 개선.

- **비제어/제어 모드의 유연한 전환**: 동일 모델에서 두 모드를 전환하면서 공정한 비교 가능. 저자가 필요에 따라 자동 추론이나 명시적 제어를 선택 가능.

## Limitation & Further Study

- **데이터셋 규모 및 다양성**: 논문에서 구체적으로 명시되지 않았으나, 특정 학술 분야(컴퓨터 과학)에 집중되어 있을 가능성. 다른 학문 분야로의 일반화 가능성 미검증.

- **평가 메트릭의 자동화 한계**: IAS, KR, FS 등의 자동 메트릭도 인간 평가와의 상관성이 완벽하지 않을 수 있음. 특히 FS(유창성)의 reference-less 평가 방식의 신뢰도 논의 필요.

- **제어 속성의 제한성**: 현재 의도 3가지, 키워드 1-2개만 제어. 더 세밀한 제어(길이, 톤, 구체성 수준 등)는 미지원.

- **모델 크기에 따른 성능 편차**: 다양한 크기의 언어 모델(6.7B, 13B 등)에 대한 포괄적 평가 필요.

- **후속 연구 방향**: 
  - 인간 피드백 강화학습(RLHF)을 통한 추가 개선
  - 다국어, 다분야 데이터셋으로 확장
  - 더 세밀한 제어 속성의 정의 및 구현
  - 인용 그래프 정보(Ge et al., 2021)와의 결합


## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 논문은 인용 문장 생성에 사용자 제어 기능을 도입하는 실용적이고 창의적인 접근을 제시하며, 구조화된 프롬프트 템플릿과 다중 메트릭 기반 강화학습을 통해 기존 자동화 방식의 한계를 효과적으로 보완한다. 다만 평가 메트릭의 일부 신뢰도와 데이터셋의 도메인 한계 측면에서는 추가 검증이 필요하다.

## Related Papers

- 🏛 기반 연구: [[papers/220_Cited_text_spans_for_citation_text_generation/review]] — 인용 텍스트 생성을 위한 인용된 텍스트 구간 활용 연구로 본 논문의 제어 가능한 생성을 위한 입력 정보 기반을 제공한다.
- 🔗 후속 연구: [[papers/1091_Scirgc_Multi-granularity_citation_recommendation_and_citatio/review]] — 인용 의도를 포함한 다단계 인용 시스템으로 본 논문의 인용 의도 제어를 더 포괄적 프레임워크로 확장한다.
- 🏛 기반 연구: [[papers/746_Self-Refine_Iterative_Refinement_with_Self-Feedback/review]] — 자기 피드백을 통한 반복적 개선 방법으로 본 논문의 강화학습 기반 생성 품질 향상의 이론적 기반을 제공한다.
- 🔗 후속 연구: [[papers/220_Cited_text_spans_for_citation_text_generation/review]] — 제어 가능한 인용 문장 생성 연구로 본 논문의 인용 텍스트 구간 활용을 언어 모델 제어로 발전시킨다.
