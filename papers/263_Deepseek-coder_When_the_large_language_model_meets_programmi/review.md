---
title: "263_Deepseek-coder_When_the_large_language_model_meets_programmi"
authors:
  - "Daya Guo"
  - "Qihao Zhu"
  - "Dejian Yang"
  - "Zhenda Xie"
  - "Kai Dong"
date: "2024"
doi: "-"
arxiv: ""
score: 4.5
essence: "본 논문은 1.3B에서 33B 규모의 오픈소스 코드 전문 대규모 언어모델(LLM) 시리즈를 제시하며, 폐쇄형 모델인 Codex와 GPT-3.5를 능가하는 성능을 달성했다. 2조 개의 토큰으로 학습된 이 모델들은 저작권 제약 없이 상용 사용 가능한 오픈소스로 제공된다."
tags:
  - "cat/Scientific_Language_Processing_and_Visualization"
  - "sub/Domain-adapted_Instruction_Models"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Guo et al._2024_Deepseek-coder When the large language model meets programming–the rise of code intelligence.pdf"
---

# Deepseek-coder: When the large language model meets programming–the rise of code intelligence

> **저자**: Daya Guo, Qihao Zhu, Dejian Yang, Zhenda Xie, Kai Dong, Wentao Zhang, Guanting Chen, Xiao Bi, Y. Wu, Y.K. Li, Fuli Luo, Yingfei Xiong, Wenfeng Liang | **날짜**: 2024 | **DOI**: -

---

## Essence

![Figure 1](figures/fig1.webp) *DeepSeek-Coder의 성능 비교*

본 논문은 1.3B에서 33B 규모의 오픈소스 코드 전문 대규모 언어모델(LLM) 시리즈를 제시하며, 폐쇄형 모델인 Codex와 GPT-3.5를 능가하는 성능을 달성했다. 2조 개의 토큰으로 학습된 이 모델들은 저작권 제약 없이 상용 사용 가능한 오픈소스로 제공된다.

## Motivation

- **Known**: 대규모 언어모델이 코드 인텔리전스를 혁명적으로 발전시켰으나, 폐쇄형 모델(OpenAI, Google)의 지배로 인해 광범위한 연구개발이 제약되어 있음

- **Gap**: 오픈소스 모델과 폐쇄형 모델 간의 성능 격차가 상당하며, 기존 오픈소스 코드 모델들은 프로젝트 수준의 크로스파일 코드 생성 능력 부재

- **Why**: 실제 소프트웨어 개발 환경에서는 여러 파일 간의 의존성이 중요한데, 기존 파일 단위 학습은 이를 간과함

- **Approach**: 
  1. 저장소 수준의 의존성 분석을 통한 데이터 구성
  2. Fill-In-Middle(FIM) 학습 방식 도입
  3. 16K 토큰 컨텍스트 윈도우 확장
  4. 87개 프로그래밍 언어 포함 및 고품질 코드 코퍼스 구축

## Achievement

![Figure 2](figures/fig2.webp) *데이터셋 생성 절차: 데이터 크롤링 → 규칙 필터링 → 의존성 파싱 → 저장소 수준 중복 제거 → 품질 스크리닝*

1. **오픈소스 최고 성능 달성**: DeepSeek-Coder-Base 33B는 모든 오픈소스 코드 모델을 능가하며, 다양한 벤치마크에서 일관되게 우수한 성능 시현

2. **폐쇄형 모델 추월**: DeepSeek-Coder-Instruct 33B가 OpenAI GPT-3.5 Turbo를 대부분의 코드 관련 벤치마크에서 초월하며, GPT-4와의 성능 격차 감소

3. **효율적 스케일링**: 7B 모델이 CodeLlama-33B(5배 더 큼)와 경쟁 가능한 성능 달성으로 매개변수 효율성 입증

4. **상용 접근성**: 허용적 오픈소스 라이센스로 제한 없는 상용 사용 허가

## How

### 데이터 수집 및 전처리

- **GitHub 데이터 수집**: 2023년 2월 이전의 공개 저장소에서 87개 프로그래밍 언어 데이터 수집
- **규칙 기반 필터링**: 라인당 평균 길이 100자 초과, 최대 길이 1000자 초과, 알파벳 문자 25% 미만인 파일 제거. 원본 대비 32.8%로 축소
- **의존성 파싱**: 위상 정렬(topological sort) 알고리즘을 통해 파일 간 import/include 관계 분석. 순환 의존성 처리를 위해 최소 내차수(minimal in-degree) 노드 선택
- **저장소 수준 중복 제거**: 파일 단위가 아닌 저장소 전체를 단일 샘플로 취급하여 중복 제거, 저장소 구조 무결성 유지
- **품질 스크리닝**: 컴파일러 및 품질 모델 사용으로 문법 오류, 낮은 가독성, 낮은 모듈성 코드 필터링
- **오염 제거(Decontamination)**: HumanEval, MBPP, GSM8K, MATH 등의 테스트셋 포함 코드를 10-gram 매칭으로 제거

### 학습 구성

- **데이터 규모**: 총 798GB, 603백만 개 파일 (Python 15.12%, C# 7.34%, C++ 11.39% 등)
- **데이터 구성**: 87% 소스코드, 10% 영문 코드 관련 자연언어(GitHub Markdown, StackExchange), 3% 중문 자연언어
- **학습 목표**: 다음 토큰 예측(next token prediction) 손실 + Fill-In-Middle(FIM) 접근법
- **컨텍스트 길이**: 16K 토큰 윈도우로 더 복잡한 코드 작업 처리 가능

## Originality

- **저장소 수준 데이터 구성**: 기존 파일 단위 학습을 넘어 저장소 내 크로스파일 의존성을 최초 도입하여 실제 개발 환경 반영

- **체계적 의존성 분석**: 순환 의존성 처리를 포함한 정교한 위상 정렬 알고리즘으로 파일 순서 최적화

- **저장소 수준 중복 제거**: 기존 파일/근처 중복 제거 대비 저장소 구조 무결성을 보존하는 혁신적 접근

- **포괄적 품질 관리**: 컴파일러 검증, 품질 모델, 휴리스틱 규칙을 결합한 다층적 필터링

- **FIM 전략의 체계적 분석**: 코드 모델 사전학습에서 FIM 학습 구성의 영향을 광범위하게 검토

## Limitation & Further Study

- **의존성 분석의 한계**: 정규표현식 기반 import/include 추출로 인한 복잡한 동적 의존성 누락 가능성

- **언어 편향**: Python(15.12%), C#(7.34%), C++(11.39%) 등 특정 언어 편중으로 저자원 언어에서 성능 편차 가능

- **단일 국가 데이터**: GitHub 기반 서구 코딩 관례 편향, 다양한 코딩 스타일 미반영

- **테스트셋 오염 완전성**: 10-gram 필터링의 충분성에 대한 입증 부족

- **후속 연구 방향**: 
  - 고급 정적 분석 도구 활용한 정밀 의존성 추출
  - 다국어/다양한 코딩 스타일의 균형잡힌 데이터셋 구성
  - 더 장기적 컨텍스트(32K 이상) 활용 가능성 탐색
  - 팀 협업 및 버전 관리 정보 통합 가능성 조사

## Evaluation

- **Novelty**: 4.5/5 - 저장소 수준 의존성 분석과 체계적 FIM 분석은 신선하나, 개별 기술 요소는 기존 기법 조합

- **Technical Soundness**: 4.5/5 - 데이터 처리 파이프라인이 철저하고 체계적이나, 의존성 분석의 정확성 검증 상세도 부족

- **Significance**: 4.5/5 - 오픈소스 모델의 실질적 성능 향상으로 상당한 학계/산업 임팩트 예상. 폐쇄형 모델과의 격차 감소는 중대한 성과

- **Clarity**: 4/5 - 전반적으로 명확하나, 의존성 파싱 알고리즘의 순환 처리 로직 설명이 간결함. 구체적 FIM 구성 상세 부족

- **Overall**: 4.5/5

**총평**: DeepSeek-Coder는 저장소 수준 의존성 분석이라는 신선한 접근과 철저한 데이터 관리를 통해 오픈소스 코드 모델의 새로운 기준을 수립했으며, GPT-3.5 추월 성과는 코드 AI의 민주화에 중대한 기여를 한다. 다만 의존성 추출의 정확성 검증과 언어 편향 완화가 후속 과제이다.

## Related Papers

- 🔄 다른 접근: [[papers/741_Seed-coder_Let_the_code_model_curate_data_for_itself/review]] — 둘 다 코드 생성 모델이지만 Seed-Coder는 LLM 기반 자동 필터링으로 차별화됨
- 🏛 기반 연구: [[papers/231_Codegen_An_open_large_language_model_for_code_with_multi-tur/review]] — CodeGen의 다중 턴 프로그램 생성 방법론이 DeepSeek-Coder 개발의 기초가 됨
- 🔄 다른 접근: [[papers/230_Code_llama_Open_foundation_models_for_code/review]] — Code Llama와 유사한 코드 특화 LLM이지만 상용 사용 가능한 오픈소스로 차별화
- 🔗 후속 연구: [[papers/770_Starcoder_2_and_the_stack_v2_The_next_generation/review]] — StarCoder의 코드 생성 기술을 더 큰 규모와 상용 라이센스로 발전시킴
- 🔄 다른 접근: [[papers/741_Seed-coder_Let_the_code_model_curate_data_for_itself/review]] — DeepSeek-Coder와 달리 Seed-Coder는 LLM 기반 자동 필터링으로 인간 수작업을 제거
- 🔄 다른 접근: [[papers/231_Codegen_An_open_large_language_model_for_code_with_multi-tur/review]] — 코드 생성에 특화된 DeepSeek-Coder와 달리 대화형 프로그램 합성에 중점
- 🏛 기반 연구: [[papers/894_AI_Copilot_Code_Quality_2025_Data_Suggests_4x_Growth_in_Code/review]] — DeepSeek-Coder가 대규모 코드 언어 모델의 기반 기술로서 AI Copilot의 코드 생성 품질 개선에 영향을 미친다.
