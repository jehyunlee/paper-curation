---
title: "005_A_comprehensive_survey_on_long_context_language_modeling"
authors:
  - "Jiaheng Liu"
  - "Dawei Zhu"
  - "Zhiqi Bai"
  - "Yancheng He"
  - "Huanxuan Liao"
date: "2025"
doi: ""
arxiv: ""
score: 4.0
essence: "장문맥 언어모델(LCLM) 구축, 훈련, 배포, 평가를 위한 포괄적 조사로, 데이터 전략부터 인프라, 평가 패러다임, 응용 분야까지 체계적으로 정리한 대규모 서베이 논문."
tags:
  - "cat/Cognitive_AI_Evaluation_and_Benchmarking"
  - "sub/Working_Memory_Benchmarks"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Liu et al._2025_A comprehensive survey on long context language modeling.pdf"
---

# A comprehensive survey on long context language modeling

> **저자**: Jiaheng Liu, Dawei Zhu, Zhiqi Bai, Yancheng He, Huanxuan Liao, Haoran Que, Zekun Wang, Chenchen Zhang, Ge Zhang, Jiebin Zhang, Yuanxing Zhang, Zhuo Job Chen, Hangyu Guo, S. Li, Ziqiang Liu, Yong Shan, Yifan Song, Jiayi Tian, Wenhao Wu, Zongqing Zhou | **날짜**: 2025 | **URL**: [https://arxiv.org/abs/2503.17407](https://arxiv.org/abs/2503.17407)

---

## Essence

![Figure 2](figures/fig2.webp)

*Figure 2. Taxonomy of Long Context Language Modeling.*

장문맥 언어모델(LCLM) 구축, 훈련, 배포, 평가를 위한 포괄적 조사로, 데이터 전략부터 인프라, 평가 패러다임, 응용 분야까지 체계적으로 정리한 대규모 서베이 논문.

## Motivation

- **Known**: 기존 언어모델들은 고정된 컨텍스트 윈도우 내에서 작동하며, 최근 몇 년간 컨텍스트 길이가 4K에서 128K, 1M, 심지어 10M 토큰으로 기하급수적으로 확장되었다.
- **Gap**: 장문맥 처리의 효율성, 훈련 인프라, 신뢰할 수 있는 평가 프레임워크, 모델 내부 메커니즘 해석에 대한 체계적이고 포괄적인 이해가 부족하다.
- **Why**: Tolstoy 규모의 장편 텍스트를 단일 패스로 처리하고, o1형 추론, 복잡한 에이전트 워크플로우, 효율적 정보 검색 등 새로운 능력을 가능하게 하기 때문에 중요하다.
- **Approach**: 3개의 핵심 연구 질문(RQ1: 효과적이고 효율적인 LCLM 구축, RQ2: 효율적 훈련 및 배포, RQ3: 포괄적 평가 및 분석)을 중심으로 데이터, 아키텍처, 워크플로우, 인프라, 평가, 분석, 응용을 체계적으로 검토한다.

## Achievement

![Figure 4](figures/fig4.webp)

*Figure 4. Taxonomy of Long Context Model Architectures.*

- **데이터 전략**: 사전학습(pre-training)과 후학습(post-training) 단계의 데이터 필터링, 혼합, 합성 방법론 정리
- **아키텍처 설계**: 위치 임베딩(Position Embedding), 트랜스포머 기반 수정, 선형 복잡도(Linear-Complexity) 아키텍처, 하이브리드 접근법 분류 및 분석
- **워크플로우 설계**: 프롬프트 압축(Hard/Soft), 메모리 기반 방법, RAG, 에이전트 기반 방법 체계화
- **인프라**: 훈련 최적화(I/O, GPU 메모리, 통신-계산 오버래핑), 추론 최적화(양자화, 메모리 관리, 예측 디코딩)
- **평가 패러다임**: 장문맥 이해(comprehension) 및 장문 생성(long-form generation) 평가 벤치마크 및 방법론
- **분석**: 성능 분석, 모델 구조 분석(위치 임베딩, 어텐션, 계층 상호작용) 및 메커니즘 해석

## How

![Figure 3](figures/fig3.webp)

*Figure 3. Illustration of training pipeline of LCLMs.*

- 데이터 엔지니어링: 필터링(filtering), 혼합(mixture), 합성(synthesis) 기법을 사전/후학습 단계별로 검토
- 위치 임베딩 분석: 절대/상대/회전/별리 임베딩(RoPE, ALiBi) 등과 외삽(Extrapolation) 방법 비교
- 어텐션 메커니즘: 표준 트랜스포머, 스파스(Sparse), 선형 복잡도(Linear) 어텐션, 계층적(Hierarchical) 방법 검토
- 프롬프트 최적화: Hard compression(토큰 선택), Soft compression(학습 가능 표현) 구분
- 메모리/RAG/에이전트: 외부 메모리 활용, 검색 기반, 행동 기반 워크플로우 통합
- 훈련 최적화: Flash Attention, Paged Attention, FSDP 등 인프라 기법 적용
- 추론 최적화: KV 캐시 양자화, 분산 추론, Speculative decoding 등 배포 기법
- 벤치마크: Needle-in-haystack, LongBench, LongEval 등 장문맥 평가 데이터셋 정리
- 기계적 해석: 어텐션 패턴 분석, 계층별 정보 흐름, 위치 인코딩 속성 검토

## Originality

- **첫 번째 포괄적 장문맥 LLM 서베이**: 데이터, 아키텍처, 워크플로우, 인프라, 평가, 분석, 응용을 통합한 체계적 정리
- **3층 구조의 연구 질문**: RQ1-RQ3를 명확히 구분하여 학술적 깊이와 실무적 유용성 동시 확보
- **평가 패러다임의 비판적 분석**: 'Support context length의 거짓 약속' 등 성과 주장의 신뢰성 문제 제기", '**메커니즘 해석 중심**: 어텐션 분석, 계층 상호작용, 위치 인코딩 속성 등 내부 동작 원리 체계화
- **다양한 응용 영역 통합**: 에이전트, RAG, 챗봇, 코드, 전통 NLP, 멀티모달, 도메인 특화 응용 분류

## Limitation & Further Study

- **논문 커버리지**: 2025년 11월 이전 발표 논문 중심으로, 이후 최신 발전(예: Grok 2, GPT-4.5 등)은 제외 가능성
- **이론적 분석 부족**: 왜 특정 아키텍처가 장문맥에서 우수한지에 대한 근본적 이론 분석이 제한적
- **평가 신뢰성 문제**: Needle-in-haystack 같은 인공 평가가 실제 성능과 괴리된 사례 언급하나, 대안 부족
- **응용 사례 실증 부족**: 각 응용 분야의 성공 사례와 정량적 효과 비교 미흡
- **향후 연구 방향**: o1형 추론, 기계적 해석, 더 신뢰할 수 있는 평가 프레임워크 개발 필요

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 장문맥 언어모델의 전체 생명주기를 최초로 체계적으로 정리한 필수 참고 자료로, 데이터부터 배포까지 실무자에게 유용하며, 평가 신뢰성 문제 지적 등 비판적 통찰도 제공한다.

## Related Papers

- 🧪 응용 사례: [[papers/452_L-citeeval_Do_longcontext_models_truly_leverage_context_for/review]] — 장문맥 언어모델의 포괄적 조사에서 제시된 이론과 방법론은 L-CiteEval의 장문맥 모델 인용 정확도 평가에 직접 적용됩니다
- 🔗 후속 연구: [[papers/876_What_are_the_essential_factors_in_crafting_effective_long_co/review]] — 효과적인 장문맥 제작 요소 연구는 장문맥 언어모델링 조사에서 다룬 데이터 전략과 평가 방법을 더욱 구체화한 연구입니다
- 🏛 기반 연구: [[papers/036_A_survey_on_transformer_context_extension_Approaches_and_eva/review]] — 트랜스포머 맥락 확장 접근법과 평가에 대한 조사는 장문맥 언어모델링의 핵심 기술적 기반을 제공합니다
- 🏛 기반 연구: [[papers/876_What_are_the_essential_factors_in_crafting_effective_long_co/review]] — 장문맥 언어 모델링에 대한 종합적 조사가 다중 홉 데이터 합성의 이론적 배경
- 🏛 기반 연구: [[papers/452_L-citeeval_Do_longcontext_models_truly_leverage_context_for/review]] — 장문맥 모델의 포괄적 조사는 인용 정확도 평가 벤치마크의 이론적 기반을 제공합니다
- 🏛 기반 연구: [[papers/495_Llm__mapreduce-v2_Entropy-driven_convolutional_test-time_sca/review]] — 긴 컨텍스트 언어 모델링에 대한 종합적 조사가 극도로 긴 입력 처리 방법론의 이론적 토대를 제공한다.
- 🔗 후속 연구: [[papers/810_Through_the_lens_of_core_competency_Survey_on_evaluation_of/review]] — 긴 문맥 언어 모델링에 대한 포괄적 조사가 핵심 역량 프레임워크의 평가 방법론을 확장한다.
- 🔗 후속 연구: [[papers/368_Gemini_15_Unlocking_multimodal_understanding_across_millions/review]] — 긴 컨텍스트 언어 모델링에 대한 포괄적인 조사가 Gemini 1.5의 초장기 컨텍스트 처리 능력의 이론적 배경과 한계를 분석한다.
- 🔄 다른 접근: [[papers/036_A_survey_on_transformer_context_extension_Approaches_and_eva/review]] — 긴 컨텍스트 언어 모델링에 대한 또 다른 포괄적 서베이로 상호 보완적 관점을 제공한다.
