---
title: "231_Codegen_An_open_large_language_model_for_code_with_multi-tur"
authors:
  - "Erik Nijkamp"
  - "Bo Pang"
  - "Hiroaki Hayashi"
  - "Lifu Tu"
  - "Huan Wang"
date: "2023"
doi: "arXiv:2203.13474"
arxiv: ""
score: 4.0
essence: "본 논문은 프로그램 합성(program synthesis) 작업에 최적화된 16.1B 파라미터 규모의 대규모 언어 모델 CodeGen 계열을 제시하고, 사용자가 자연어로 단계적 명령을 제공하는 **다중 턴 프로그램 합성(multi-turn program synthesis)** 패러다임을 도입하여 단일 턴 방식 대비 명확한 성능 향상을 입증한다."
tags:
  - "cat/Scientific_Language_Processing_and_Visualization"
  - "sub/Domain-adapted_Instruction_Models"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Nijkamp et al._2022_Codegen An open large language model for code with multi-turn program synthesis.pdf"
---

# Codegen: An open large language model for code with multi-turn program synthesis

> **저자**: Erik Nijkamp, Bo Pang, Hiroaki Hayashi, Lifu Tu, Huan Wang, Yingbo Zhou, Silvio Savarese, Caiming Xiong | **날짜**: 2023 (ICLR 발표) | **DOI**: [arXiv:2203.13474](https://arxiv.org/abs/2203.13474)

---

## Essence

본 논문은 프로그램 합성(program synthesis) 작업에 최적화된 16.1B 파라미터 규모의 대규모 언어 모델 CodeGen 계열을 제시하고, 사용자가 자연어로 단계적 명령을 제공하는 **다중 턴 프로그램 합성(multi-turn program synthesis)** 패러다임을 도입하여 단일 턴 방식 대비 명확한 성능 향상을 입증한다.

## Motivation

- **Known**: Codex, GPT-3 등 대규모 언어모델이 프로그램 합성에서 우수한 성능을 보이고 있으나, 이러한 모델들이 대부분 폐쇄형으로 제공되어 학술 연구 접근성이 제한적이다. 또한 기존 연구는 단일 턴(single-turn) 입력에만 초점을 맞추고 있다.

- **Gap**: (1) 오픈소스 고성능 코드 생성 모델의 부재, (2) 복잡한 프로그램 요구사항을 단일 프롬프트로 지정해야 하는 사용성 문제, (3) 다중 턴 상호작용이 프로그램 합성에 미치는 영향에 대한 체계적 분석 부재.

- **Why**: 복잡하고 긴 명세를 여러 단계로 분해하면: (1) 모델이 각 부분 문제에 집중할 수 있어 검색 공간 축소, (2) GitHub 코드의 주석-코드 인터리빙 패턴이 약한 감독 신호(weak supervision)로 작용하여 자연어 기반 다중 턴 능력 학습 가능, (3) 사용자 입장에서 자연어로 점진적으로 의도 표현 가능.

- **Approach**: (1) ThePile, BigQuery, BigPython 세 가지 데이터셋에서 순차적으로 학습된 모델 계열 개발 (NL → MULTI → MONO), (2) 115개 다양한 문제로 구성된 **다중 턴 프로그래밍 벤치마크(MTPB)** 구축, (3) JAXFormer 훈련 라이브러리 오픈소스화.

## Achievement

![Figure 1](https://example.com/fig1.png) *이메일 주소에서 사용자명 추출하는 다중 턴 프로그램 합성의 예시*

1. **단일 턴 성능**: HumanEval 벤치마크에서 CODEGEN-MONO 16.1B가 pass@1 = 29.28%, pass@100 = 75.00%로 달성하여 GPT-Neo/GPT-J 대비 현저히 우수하고 Codex 300M/2.5B 수준 성능 발휘.

2. **다중 턴 우수성**: MTPB 벤치마크에서 동일한 의도를 다중 턴으로 제공했을 때 단일 턴 대비 **평균 통과율 30% 이상 향상** (Figure 2 참조). 예를 들어 일부 문제에서 단일 턴 15% → 다중 턴 45% 수준의 개선 관찰.

3. **오픈소스 기여**: 16.1B까지의 모든 모델 체크포인트 및 TPU-v4 최적화 훈련 라이브러리 공개로 학술 커뮤니티 접근성 확대.

## How

![Figure 2](https://example.com/fig2.png) *단일 턴 vs 다중 턴 평균 통과율 차이*

- **데이터셋 구성 및 순차 학습**:
  - ThePile (825.18 GiB, 22개 서브셋, GitHub 코드 7.6%): 자연어 기초 학습
  - BigQuery (6개 언어 코드): 다중언어 능력 추가
  - BigPython (대규모 GitHub Python 코드): Python 특화 학습
  - 각 단계마다 이전 가중치로 초기화하는 순차 파인튜닝(sequential fine-tuning)

- **모델 아키텍처**: 표준 자기회귀 트랜스포머(autoregressive transformer) with 다음 토큰 예측(next-token prediction) 목적함수. 파라미터 규모: 350M, 2.7B, 6.1B, 16.1B (scaling law 검증용)

- **훈련 인프라**: JAXFormer 라이브러리 개발으로 TPU-v4에서 효율적인 데이터/모델 병렬처리(data/model parallelism) 구현

- **MTPB 벤치마크 설계**:
  - 115개 문제를 2-4개 부분 문제로 분해
  - 각 턴에서 자연어 명세 + 이전 턴 코드 조각 입력
  - 전문가 작성 테스트 케이스로 통과율(pass rate) 평가

- **프롬프트 형식**: 자연어 설명 → 코드 생성 → 다음 단계 설명 → 추가 코드 생성 패턴

## Originality

- **다중 턴 프로그램 합성 패러다임 도입**: 기존 연구가 단일 프롬프트만 다루는 반면, 사용자-모델 상호작용의 반복적 특성을 처음으로 체계화.

- **다중 턴 프로그래밍 벤치마크(MTPB) 구축**: 115개 문제의 다중 턴 분해 제공 → 정량적 평가 가능한 첫 번째 벤치마크.

- **약한 감독 신호(weak supervision) 가설**: 주석-코드 인터리빙 패턴을 명시적 학습 신호로 활용하지 않음에도 불구하고 자동으로 다중 턴 능력이 emergence되는 메커니즘 분석 시도.

- **스케일 법칙(scaling laws) 분석**: 4가지 모델 크기에서 프로그램 합성 능력의 emergence 추적 → 크기와 데이터 규모의 중요성 입증.

- **JAXFormer 오픈소스화**: 기존 폐쇄형 모델에 대항하여 전체 훈련 코드 및 모델 공개 → 연구 접근성 민주화.

## Limitation & Further Study

- **약한 감독 신호의 불충분성**: 코드 주석이 부정확하거나 무관한 위치에 있을 수 있음. 명시적 comment-code 쌍 학습 데이터로의 강화가 필요할 수 있음.

- **MTPB의 제한성**: 115개 문제가 모두 인간이 수작업으로 분해한 것으로, 자동 분해 방법론 또는 더 큰 규모 벤치마크 필요.

- **다중 턴 최적 분해 전략 미결정**: 문제를 몇 개 부분으로 나누는 것이 최적인지, 어떤 순서로 분해할지에 대한 명확한 지침 부재. 자동 분해 방법 개발 필요.

- **모델 크기 한계**: 16.1B가 최대이지만, Codex-12B의 성능 초과하지 못함. 더 큰 모델 또는 전문화된 사전학습 필요.

- **프로그래밍 언어 다양성**: Python에 편향된 평가. Java, C++ 등 다른 언어에서의 성능 체계적 분석 필요.

- **후속 연구 방향**: (1) 다중 턴 분해의 자동화, (2) 인간 피드백 활용(RLHF)을 통한 다중 턴 정책 최적화, (3) 외부 도구(Python REPL, 테스트 실행) 통합, (4) 더 큰 규모 모델의 가능성 탐색.


## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 5/5
- Clarity: 4/5
- Overall: 4/5

**총평**: CodeGen은 프로그램 합성의 민주화를 위한 첫 고품질 오픈소스 모델로서, 다중 턴 패러다임 도입과 전용 벤치마크 제시를 통해 학술 기여도를 확보했으나, 성능 경쟁력과 다중 턴 성능 향상의 원인에 대한 깊이 있는 분석이 더 강화될 필요가 있다.

## Related Papers

- 🏛 기반 연구: [[papers/197_Chartcoder_Advancing_multimodal_large_language_model_for_cha/review]] — 다중 턴 프로그램 합성 방법론이 차트-코드 변환에서 단계적 생성 접근의 기반
- 🔗 후속 연구: [[papers/1092_Table-llm-specialist_Language_model_specialists_for_tables_u/review]] — 프로그램 합성 기법을 테이블 작업 특화 모델의 반복적 미세조정에 적용한 확장
- 🏛 기반 연구: [[papers/815_ToolLLM_Facilitating_Large_Language_Models_to_Master_16000_R/review]] — 코드 생성 능력이 API 도구 사용 벤치마크에서 프로그래밍 작업의 기반
- 🔄 다른 접근: [[papers/263_Deepseek-coder_When_the_large_language_model_meets_programmi/review]] — 코드 생성에 특화된 DeepSeek-Coder와 달리 대화형 프로그램 합성에 중점
- 🏛 기반 연구: [[papers/263_Deepseek-coder_When_the_large_language_model_meets_programmi/review]] — CodeGen의 다중 턴 프로그램 생성 방법론이 DeepSeek-Coder 개발의 기초가 됨
- 🔗 후속 연구: [[papers/741_Seed-coder_Let_the_code_model_curate_data_for_itself/review]] — CodeGen의 프로그램 생성 기법을 자동화된 데이터 큐레이션으로 발전시킨 연구
- 🏛 기반 연구: [[papers/197_Chartcoder_Advancing_multimodal_large_language_model_for_cha/review]] — CodeGen의 다중 턴 프로그램 합성 방법론을 차트-코드 변환에 적용한 기반
- 🏛 기반 연구: [[papers/1092_Table-llm-specialist_Language_model_specialists_for_tables_u/review]] — 다중 턴 프로그램 합성 방법론을 테이블 작업 특화 모델 훈련에 적용한 기반
