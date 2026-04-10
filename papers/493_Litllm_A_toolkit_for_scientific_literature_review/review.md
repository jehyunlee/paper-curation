---
title: "493_Litllm_A_toolkit_for_scientific_literature_review"
authors:
  - "Shubham Agarwal"
  - "Gaurav Sahu"
  - "Abhay Puri"
  - "Issam H. Laradji"
  - "Krishnamurthy DJ Dvijotham"
date: "2024"
doi: "N/A"
arxiv: ""
score: 3.5
essence: "LitLLM은 대규모 언어모델(LLM)과 검색 증강 생성(RAG) 기술을 결합하여 과학 논문의 관련 연구(Related Work) 섹션 작성을 자동화하는 대화형 도구이다. 시스템은 사용자 제공 초록으로부터 키워드 추출, 논문 검색 및 재순위화, 문헌 리뷰 생성의 모듈화된 파이프라인을 통해 환각(hallucination) 문제를 해결한다."
tags:
  - "cat/Cognitive_AI_Evaluation_and_Benchmarking"
  - "sub/AI_Benchmarking_Taxonomy"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Agarwal et al._2024_Litllm A toolkit for scientific literature review.pdf"
---

# Litllm: A toolkit for scientific literature review

> **저자**: Shubham Agarwal, Gaurav Sahu, Abhay Puri, Issam H. Laradji, Krishnamurthy DJ Dvijotham, Jason Stanley, Laurent Charlin, Christopher Pal | **날짜**: 2024 | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp)
*LitLLM 인터페이스: 사용자 제공 초록을 기반으로 Retrieval Augmented Generation(RAG) 원칙을 적용하여 문헌 리뷰를 생성하는 시스템*

LitLLM은 대규모 언어모델(LLM)과 검색 증강 생성(RAG) 기술을 결합하여 과학 논문의 관련 연구(Related Work) 섹션 작성을 자동화하는 대화형 도구이다. 시스템은 사용자 제공 초록으로부터 키워드 추출, 논문 검색 및 재순위화, 문헌 리뷰 생성의 모듈화된 파이프라인을 통해 환각(hallucination) 문제를 해결한다.

## Motivation

- **Known**: 최근 LLM 기반 문헌 리뷰 생성 시스템이 개발되고 있으며, ChatGPT 같은 모델들이 높은 품질의 텍스트를 생성할 수 있다. 또한 Semantic Scholar, Google Scholar 같은 학술 검색 엔진이 논문 검색을 돕고 있다.

- **Gap**: 기존 LLM 기반 시스템들은 존재하지 않는 논문이나 잘못된 인용을 생성하는 심각한 환각 문제를 보인다(Galactica 사례). 또한 학습 데이터에 포함되지 않은 최신 연구를 반영하지 못한다.

- **Why**: 문헌 리뷰는 과학 연구의 필수 단계지만 매우 시간 소모적이며, 정확성이 중요한 작업이다. 자동화된 도구로 연구자들의 부담을 줄일 수 있다면 학술 공동체에 큰 도움이 될 것이다.

- **Approach**: Retrieval Augmented Generation(RAG) 원칙을 적용하여 검색된 실제 논문들을 컨텍스트로 활용함으로써 LLM의 환각을 억제하고, 모듈화된 파이프라인(키워드 추출 → 논문 검색 → 재순위화 → 생성)을 통해 체계적으로 문헌 리뷰를 생성한다.

## Achievement

![Figure 2](figures/fig2.webp)
*모듈화된 파이프라인 구조: 초록 → 키워드 생성 → 논문 검색 → 재순위화 → 최종 문헌 리뷰 생성*

1. **실용적 도구 개발**: 사용자 친화적 인터페이스를 갖춘 완전한 문헌 리뷰 생성 시스템을 구현했으며, 데모 및 공개 툴킷을 제공한다(https://litllm.github.io).

2. **환각 문제 해결**: RAG 기반 접근으로 검색된 실제 논문들을 기반으로 생성하도록 조건화하여 환각 현상을 크게 감소시킨다.

3. **유연한 검색 전략**: 초록 기반 키워드 추출, 사용자 제공 키워드, 시드 논문 추천 등 다양한 검색 전략을 제공하여 학제적 연구(interdisciplinary research)에도 대응할 수 있다.

4. **제어 가능한 생성**: 문장 계획(sentence-based planning) 기능을 통해 생성된 문헌 리뷰의 길이와 형식을 사용자가 제어할 수 있다.

## How

![Figure 3](figures/fig3.webp)
*다양한 검색 전략: 초록 기반 키워드 요약, 사용자 제공 키워드, 시드 논문 기반 추천*

### 3.1 논문 검색 모듈 (Paper Retrieval Module)
- Semantic Scholar API와 OpenAlex API를 활용하여 300M+ 학술 메타데이터에 접근
- 사용자 제공 초록을 LLM으로 최대 5개의 키워드로 요약하여 검색 쿼리 생성
- 선택적으로 사용자가 제공한 추가 키워드로 검색 결과 개선
- 관련 시드 논문으로부터 Recommendations API를 통해 유사 논문 검색

![Figure 4](figures/fig4.webp)
*키워드 요약 프롬프트: 연구 초록을 5개 이하의 검색 키워드로 변환*

### 3.2 논문 재순위화 모듈 (Paper Re-Ranking Module)
- Permutation generation 방식: LLM이 사용자 초록과의 연관성에 따라 논문들을 내림차순으로 순위화하도록 프롬프트
- Debate-ranking 방식: LLM이 각 논문에 대해 포함 찬성/반대 논거를 생성 후 확률 기반 순위 결정
- 최상위 k개 후보를 LLM이 최종 순위화하여 생성 품질 향상

![Figure 5](figures/fig5.webp)
*재순위화 프롬프트: 초록과 후보 논문들의 추상을 입력하여 관련성 기반 순위 생성*

### 3.3 요약 생성 모듈 (Summary Generation Module)
- **Zero-shot 생성**: 초록과 재순위화된 논문들의 초록을 직접 LLM에 입력하여 관련 연구 섹션 생성
- **계획 기반 생성**: 문장 계획(sentence plan)을 사용하여 각 문장의 인용 정보와 문장 수를 명시적으로 제어하며 생성

## Originality

- **RAG 원칙의 체계적 적용**: 단순히 LLM을 사용하는 것이 아니라, 검색 → 재순위화 → 생성의 모듈화된 파이프라인으로 환각을 구조적으로 해결

- **다양한 검색 전략 통합**: 키워드 추출, 사용자 입력, 시드 논문 추천을 통합하여 유연하고 포괄적인 검색 지원

- **문장 계획 기반 제어**: Agarwal et al. (2024)의 문장 계획 기법을 적극 활용하여 LLM 생성 결과의 환각을 감소시키고 사용자 선호도를 반영

- **LLM 기반 재순위화**: 최신 permutation generation과 debate-ranking 방식을 적용하여 단순 검색 순위보다 의미적 관련성 기반 순위화 달성

- **완전한 실용적 시스템**: 이론적 기여를 넘어 실제 사용 가능한 인터페이스와 공개 툴킷으로 구현

## Limitation & Further Study

- **초록 기반 제한**: 시스템이 사용자 제공 초록을 주요 입력으로 사용하므로, 초록의 품질이 검색과 생성 결과에 큰 영향을 미칠 수 있다.

- **재순위화 성능 미검증**: 논문에서 재순위화 모듈의 성능을 정량적으로 평가하지 않았으며, 실제 재순위화 정확도가 불명확하다.

- **생성 품질 평가 부재**: 생성된 문헌 리뷰의 품질(정확성, 완성도, 유용성)에 대한 정량적 평가 지표나 사용자 연구가 제시되지 않았다.

- **확장성 미지수**: 매우 특수한 도메인이나 신흥 연구 분야에서의 성능, 대규모 논문 처리 시 시스템의 확장성이 불명확하다.

- **후속 연구 방향**:
  - 생성된 리뷰에 대한 인간 평가 및 정량적 성능 지표 개발
  - 재순위화 모듈의 정확성 평가 및 하이브리드 재순위화 방식 탐색
  - 다양한 LLM 모델 간 성능 비교 및 최적 모델 선택 연구
  - 실제 연구자 사용성 평가를 통한 인터페이스 개선
  - 도메인 특화 모델 미세조정(fine-tuning) 가능성 탐색

## Evaluation

- **Novelty**: 3.5/5
  - RAG 원칙 자체는 기존 개념이지만, 문헌 리뷰 생성에 체계적으로 적용한 점은 가치 있다. 다만 개별 기술(문장 계획, permutation ranking 등)은 기존 연구에서 제시된 것들의 조합이다.

- **Technical Soundness**: 3/5
  - 파이프라인 구조는 논리적이고 합리적이나, 각 모듈의 성능 검증(특히 재순위화 정확도)이 부족하다. 프롬프트 설계는 적절하지만 다양한 LLM에 대한 일반화 가능성이 미검증 상태이다.

- **Significance**: 4/5
  - 실제 연구자들의 문헌 리뷰 작업 시간을 대폭 절감할 수 있는 실용적 가치가 높다. 환각 문제를 해결한 점은 의미 있으며, 공개 도구 제공으로 학술 공동체에 기여한다. 그러나 성능 평가 부재로 실제 영향력 검증이 필요하다.

- **Clarity**: 4/5
  - 전체 파이프라인이 명확하게 설명되었고, 다양한 그림으로 시각화되어 이해하기 쉽다. 각 모듈의 목적과 구현 방식이 잘 제시되었다. 다만 구체적인 실험 결과나 정량적 성능 분석이 없어 실제 효과 검증이 제한적이다.

- **Overall**: 3.5/5

**총평**: LitLLM은 과학 문헌 리뷰 작성을 위한 실용적이고 잘 설계된 도구로, RAG 원칙을 통해 LLM의 환각 문제를 효과적으로 해결하고 모듈화된 파이프라인으로 체계적인 접근을 제시한다. 다만 개별 모듈의 성능 평가(특히 재순위화 정확도)와 생성 결과의 품질 검증이 부재하여, 학술적 엄밀성과 실제 유용성을 입증하기 위해서는 정량적 평가 및 사용자 연구가 필요하다.

## Related Papers

- 🧪 응용 사례: [[papers/064_Agentic_AI_for_Scientific_Discovery_A_Survey_of_Progress_Cha/review]] — 과학 문헌 리뷰 자동화 도구가 과학 발견을 위한 에이전틱 AI 시스템의 구체적인 문헌 분석 응용 사례이다.
- 🏛 기반 연구: [[papers/090_AIRS-Bench_a_Suite_of_Tasks_for_Frontier_AI_Research_Science/review]] — 프론티어 AI 연구 과학 에이전트 평가에서 문헌 분석과 리뷰 생성이 중요한 구성 요소로서 기반을 제공한다.
- 🔗 후속 연구: [[papers/593_Openscholar_Synthesizing_scientific_literature_with_retrieva/review]] — 검색 증강 생성을 통한 과학 문헌 합성이 LitLLM의 관련 연구 섹션 작성을 더 포괄적인 문헌 통합으로 확장한다.
- 🧪 응용 사례: [[papers/090_AIRS-Bench_a_Suite_of_Tasks_for_Frontier_AI_Research_Science/review]] — 과학 문헌 리뷰 자동화가 AI 연구 과학 에이전트의 실제 연구 워크플로우 중 하나인 문헌 분석에 적용된다.
- 🔗 후속 연구: [[papers/510_Llms_for_literature_review_Are_we_there_yet_arXiv_preprint_a/review]] — 문헌 리뷰가 더 포괄적인 과학 문헌 검토 도구로 확장됩니다.
