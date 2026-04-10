---
title: "727_Scimage_How_good_are_multimodal_large_language_models_at_sci"
authors:
  - "Leixin Zhang"
  - "Steffen Eger"
  - "Yinjie Cheng"
  - "Weihe Zhai"
  - "Jonas Belouadi"
date: "2024"
doi: "arXiv:2412.02368"
arxiv: ""
score: 4.0
essence: "본 논문은 멀티모달 대규모 언어모델(LLM)의 과학적 이미지 생성 능력을 평가하기 위한 ScImage 벤치마크를 제시한다. 5가지 모델(GPT-4o, Llama, AutomaTikZ, DALL-E, StableDiffusion)을 공간(spatial), 수치(numeric), 속성(attribute) 이해 차원에서 평가한 결과, 모든 모델이 특히 복합 프롬프트에서 상당한 어려움을 겪는 것으로 나타났다."
tags:
  - "cat/Cognitive_AI_Evaluation_and_Benchmarking"
  - "sub/Cognitive_LLM_Evaluation"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Jeyaram et al._2024_Scimage How good are multimodal large language models at scientific text-to-image generation arXiv.pdf"
---

# Scimage: How good are multimodal large language models at scientific text-to-image generation? arXiv preprint arXiv:2412.02368, 2024.

> **저자**: Leixin Zhang, Steffen Eger, Yinjie Cheng, Weihe Zhai, Jonas Belouadi, Christoph Leiter, Simone Paolo Ponzetto, Fahimeh Moafian, Zhixue Zhao | **날짜**: 2024 | **DOI**: [arXiv:2412.02368](https://arxiv.org/abs/2412.02368)

---

## Essence

![Figure 1](figures/fig1.webp) *과학적 텍스트-이미지 생성의 예시. 일반 이미지(좌측)와 달리 과학 이미지는 정확한 공간 배치, 수치 표현, 객체 속성의 정확성을 요구한다.*

본 논문은 멀티모달 대규모 언어모델(LLM)의 과학적 이미지 생성 능력을 평가하기 위한 ScImage 벤치마크를 제시한다. 5가지 모델(GPT-4o, Llama, AutomaTikZ, DALL-E, StableDiffusion)을 공간(spatial), 수치(numeric), 속성(attribute) 이해 차원에서 평가한 결과, 모든 모델이 특히 복합 프롬프트에서 상당한 어려움을 겪는 것으로 나타났다.

## Motivation

- **Known**: 
  - AI는 학술 연구의 다양한 측면(문헌 검색, 텍스트 생성, 논문 작성 등)을 지원하고 있다
  - 일반 목적의 텍스트-이미지 생성 모델들이 상당한 진전을 이루었다
  - 과학적 시각화는 복잡한 아이디어와 데이터를 전달하는 핵심 수단이다

- **Gap**: 
  - 과학 이미지 생성의 자동화는 상대적으로 미탐색 영역이다
  - 일반 이미지 벤치마크(MS COCO, T2I-CompBench 등)는 과학 도메인의 특수성을 다루지 못한다
  - 과학 이미지에 필요한 정밀한 공간 배치, 수치 정확성, 도메인 특화 객체 표현에 대한 평가 부족

- **Why**: 
  - 과학 이미지는 실제 이미지와 달리 정밀한 수치 표현, 공간 관계의 정확성, 도메인 컨벤션 준수가 필수적이다
  - 자동화된 과학 이미지 생성은 과학 커뮤니케이션의 효율성과 정확성을 크게 향상시킬 수 있다

- **Approach**: 
  - 공간, 수치, 속성 이해라는 3가지 핵심 차원을 평가하는 구조화된 벤치마크 구축
  - 코드 기반(Python, TikZ)과 직접 래스터 이미지 출력 모두 평가
  - 4개 언어(영어, 독일어, 페르시아어, 중국어)에서의 다국어 평가
  - 11명의 박사급 과학자에 의한 정확성, 관련성, 과학적 정확도 기준의 인간 평가

## Achievement

![Figure 2](figures/fig2.webp) *세 가지 이해 차원의 설명. 속성(attribute), 공간(spatial), 수치(numeric) 이해가 개별적으로 및 조합된 형태로 평가된다.*

1. **벤치마크 구축**: ~3,000개의 생성된 과학 이미지에 대한 약 3,000 USD 규모의 인간 평가 점수를 포함한 포괄적인 ScImage 벤치마크 제시

2. **광범위한 모델 평가**: 코드 기반 및 멀티모달 모델 5개(최대 8개의 서로 다른 구성)를 체계적으로 비교하여 각 모델의 장단점 분석

3. **성능 분석**: 객체 유형, 이해 차원, 입력 언어에 걸친 상세한 성능 분석으로 현재 모델들의 한계를 명확히 파악

4. **평가 메트릭 검증**: 표준 자동화 메트릭(CLIPScore, FID 등)이 과학 이미지 평가에 신뢰도가 낮음을 입증하고 인간 평가의 필요성 확인

## How

![Figure 3](figures/fig3.webp) *텍스트-코드-이미지 생성과 직접 텍스트-이미지 생성의 비교.*

- **프롬프트 설계**: 3가지 이해 차원(공간, 수치, 속성)을 개별적으로 및 조합된 형태로 테스트하는 404개의 영어 프롬프트 구성

- **모델 범위**: 
  - 코드 기반: GPT-4o, Llama 3.1 8B (Python/TikZ 출력), AutomaTikZ
  - 멀티모달: DALL-E, StableDiffusion
  - 다국어 평가: OpenAI-o1 추가 포함

- **평가 프레임워크**:
  - 정확성(Correctness): 생성된 이미지가 프롬프트의 요구사항을 정확히 충족하는가
  - 관련성(Relevance): 생성된 이미지의 과학적 맥락 적절성
  - 과학적 정확도(Scientificness): 도메인 컨벤션 준수 및 과학적 타당성

- **다국어 평가**: 영어, 독일어, 페르시아어, 중국어 4개 언어에서의 성능 비교를 통해 언어 의존성 분석

- **인간 평가**: 11명의 박사급 과학자(PhD 학생 이상)에 의한 세밀한 인간 평가로 "지상의 진실(ground truth)" 제공

## Originality

- **도메인 특화성**: 일반 이미지 벤치마크와 달리 과학 도메인의 고유한 요구사항(정밀한 수치 표현, 도메인 특화 객체 표현)을 명시적으로 다룬 최초의 체계적 평가

- **차원별 분해**: 공간, 수치, 속성 이해를 개별 및 조합 형태로 테스트하는 구조화된 평가 방식

- **다양한 출력 형식**: 코드 기반(Python, TikZ)과 직접 이미지 생성을 동시에 평가하여 접근 방식의 장단점 분석

- **다국어 평가**: 언어 의존성을 고려한 4개 언어에서의 성능 비교

- **인간 평가 기반**: 자동화 메트릭의 한계를 지적하고 과학 도메인에 적합한 인간 평가 기반의 벤치마크 제시

## Limitation & Further Study

- **평가자 규모**: 11명의 과학자에 의한 평가는 통계적 강건성 측면에서 제한적일 수 있으며, 더 많은 평가자 확보 필요

- **객체 범위 제한**: 특정 과학 도메인(예: 화학, 생물학의 복잡한 구조)에 대한 평가가 부족할 수 있음

- **자동화 메트릭 부재**: 현재 자동화 메트릭이 신뢰도가 낮다는 발견에도 불구하고, 과학 이미지 평가용 새로운 자동화 메트릭 개발이 필요

- **후속 연구 방향**:
  - 과학 이미지 생성에 최적화된 파인튜닝된 모델 개발
  - 도메인 특화 메타데이터(좌표, 수치 범위 등)를 활용한 향상된 생성 방법 연구
  - 과학 텍스트-이미지 생성용 새로운 자동화 평가 메트릭 개발
  - 더 광범위한 과학 도메인(화학, 생물학, 의학 등)으로의 벤치마크 확장

## Evaluation

- **Novelty**: 4.5/5
  - 과학 도메인 특화 벤치마크는 새로운 기여이나, 차원별 분해 접근은 기존 T2I-CompBench 아이디어를 응용한 부분이 있음

- **Technical Soundness**: 4/5
  - 체계적인 프롬프트 설계와 다국어 평가가 강점이나, 평가자 규모가 상대적으로 제한적
  - 인간 평가 프로토콜이 상세히 기술되지 않은 부분 있음

- **Significance**: 4/5
  - 과학 커뮤니케이션의 중요성과 현재 모델들의 한계를 명확히 드러냄
  - 향후 과학 이미지 생성 모델 개발에 중요한 벤치마크 역할 가능

- **Clarity**: 4.5/5
  - 논문의 동기, 과제 설정, 평가 기준이 명확함
  - 결과 분석과 시각화가 직관적이나, 일부 통계적 세부사항 설명 부족

- **Overall**: 4/5

**총평**: 본 논문은 과학 이미지 생성이라는 중요하면서도 미탐색된 영역에 처음으로 체계적이고 광범위한 벤치마크를 제시한 점에서 가치있는 기여이다. 특히 현재의 멀티모달 LLM들이 복잡한 과학 이미지 생성에서 여전히 상당한 어려움을 겪고 있음을 명확히 보여줌으로써, 향후 연구의 방향성을 제시한다는 점에서 의미있다. 다만 인간 평가 규모 확대와 더 광범위한 과학 도메인 포함을 통한 벤치마크 보강이 필요할 것으로 보인다.

## Related Papers

- 🏛 기반 연구: [[papers/388_GPT-4o_System_Card/review]] — GPT-4o의 멀티모달 기능이 과학적 이미지 생성 능력 평가의 기술적 토대를 제공한다.
- 🔗 후속 연구: [[papers/336_FigCaps-HF_A_Figure-to-Caption_Generative_Framework_and_Benc/review]] — 그림-캡션 생성 프레임워크가 과학적 이미지 생성과 이해 평가를 시각-텍스트 변환 관점에서 확장한다.
- 🔄 다른 접근: [[papers/708_SciCap_Generating_Captions_for_Scientific_Figures/review]] — 과학적 그림에 대한 캡션 생성과 달리 텍스트에서 과학적 이미지를 생성하는 역방향 능력을 평가한다.
- 🔗 후속 연구: [[papers/388_GPT-4o_System_Card/review]] — 멀티모달 과학 이미지 생성 능력 평가가 GPT-4o의 멀티모달 기능에 대한 구체적인 확장 평가이다.
- 🧪 응용 사례: [[papers/091_Aiscivision_A_framework_for_specializing_large_multimodal_mo/review]] — 과학 이미지에서 다중모달 대규모 언어모델의 성능을 구체적으로 평가한다.
- 🔗 후속 연구: [[papers/737_Sciverse_Unveiling_the_knowledge_comprehension_and_visual_re/review]] — SCIMAGE의 과학 이미지 이해 평가가 SCIVERSE의 멀티모달 콘텐츠 해석 차원을 더욱 구체화함
- 🧪 응용 사례: [[papers/181_Can_gpt-4v_ision_serve_medical_applications_case_studies_on/review]] — 과학 이미지에서 다중모달 LLM 성능 평가를 의료 영상 진단에 적용
