---
title: "539_Minif2f_a_cross-system_benchmark_for_formal_olympiad-level_m"
authors:
  - "Kunhao Zheng"
  - "Jesse Michael Han"
  - "Stanislas Polu"
date: "2021"
doi: "N/A"
arxiv: ""
score: 4.5
essence: "본 논문은 신경 정리 증명(neural theorem proving) 분야를 위한 최초의 통합 크로스 시스템 벤치마크인 miniF2F를 제시한다. 이는 488개의 올림피아드 수준 수학 문제(IMO, AIME, AMC)를 Metamath, Lean, Isabelle, HOL Light 등 다양한 형식 시스템에서 표준화된 형식으로 제공함으로써, 신경 정리 증명 시스템의 수학적 추론 능력을 공정하게 비교할 수 있는 공통 자원을 제공한다."
tags:
  - "cat/Scientific_Language_Processing_and_Visualization"
  - "sub/Formal_Theorem_Proving"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Zheng_2021_Minif2f a cross-system benchmark for formal olympiad-level mathematics.pdf"
---

# Minif2f: a cross-system benchmark for formal olympiad-level mathematics

> **저자**: Kunhao Zheng, Jesse Michael Han, Stanislas Polu | **날짜**: 2021 | **DOI**: N/A

---

## Essence

본 논문은 신경 정리 증명(neural theorem proving) 분야를 위한 최초의 통합 크로스 시스템 벤치마크인 miniF2F를 제시한다. 이는 488개의 올림피아드 수준 수학 문제(IMO, AIME, AMC)를 Metamath, Lean, Isabelle, HOL Light 등 다양한 형식 시스템에서 표준화된 형식으로 제공함으로써, 신경 정리 증명 시스템의 수학적 추론 능력을 공정하게 비교할 수 있는 공통 자원을 제공한다.

## Motivation

- **Known**: 신경 정리 증명 분야에서 HOList, CoqGym, LeanStep 등 개별 정리 증명 시스템별로 별도의 벤치마크와 데이터셋이 존재하고 있다. 또한 컴퓨터 비전과 NLP에서 공유 벤치마크(ImageNet, SQuAD 등)가 획기적 진전을 주도했다.

- **Gap**: 기존 벤치마크들은 각 시스템의 라이브러리 구조에 종속되어 있어 시스템 간 직접 비교가 불가능하며, 정리와 보조정리가 구현 특화적 산물로 존재하여 일반화된 수학적 추론 능력 측정이 어렵다.

- **Why**: 신경 정리 증명 커뮤니티가 통합된 크로스 시스템 벤치마크를 중심으로 조직화되지 않아 자원 낭비와 비교 불가능성이 발생한다.

- **Approach**: 여러 형식 시스템에 수동으로 형식화된 올림피아드 수준 문제 모음을 구성하되, 문제의 형식화 가능성과 난이도의 다양성을 고려하여 대수, 정수론, 부등식 중심으로 선정한다.

## Achievement

![Figure 1](figures/fig1.webp)
*Figure 1: miniF2F에서 성공적으로 증명된 명제의 개수 비교. 초록색 막대는 Lean GPT-f의 결과*

1. **벤치마크 구성**: 총 488개의 수동 형식화된 명제(244개 테스트셋, 244개 검증셋)를 IMO(20+20), AIME(15+15), AMC(45+45), MATH 난이도별(70+70), 사용자정의(34+34)로 구성하여 다양한 난이도와 주제를 포괄.

2. **크로스 시스템 호환**: Metamath, Lean, Isabelle(부분), HOL Light(부분)의 4개 형식 시스템에서 동일한 문제를 형식화하여 시스템 간 비교 가능성 확보.

3. **기선 결과 제시**: GPT-f와 GPT-f/PACT를 사용한 신경 정리 증명 성능 측정(Metamath, Lean)과 tidy 기선 프로버 구현으로 향후 비교 기준점 제시.

4. **사용자 친화적 설계**: MIT/Apache 라이선스, 공개 저장소, 버전 관리(v1), 커뮤니티 기여 장려 메커니즘으로 지속 가능한 벤치마크 구축.

## How

- **문제 선정**: 올림피아드 수준의 문제는 필요한 이론이 잘 정의되어 있고 새로운 수학 개념 도입이 불필요하며, 다양한 형식 시스템에서 표현 가능한 특성을 활용.

- **형식화 과정**: 훈련된 사용자 기준 명제 형식화 약 15분, 검수 약 7.5분 소요. 다지선다형 문제(올바른 답만 형식화), 문장 문제(자연언어 개념을 수학 표현으로 모델링), 증명 대상 찾기 문제(답과 함께 정확성/유일성 증명으로 재설정)에 대한 전략적 대응.

- **검증셋/테스트셋 분할**: 계층화 무작위 분할(stratified random split)로 문제 유형별, 난이도별 동등한 커버리지 확보.

- **평가 메트릭**: Pass@N 메트릭(N번의 증명 탐색 시도 중 하나 이상 성공)을 사용하여 확률적 비편향 추정.

## Originality

- **최초의 통합 벤치마크**: 신경 정리 증명 분야의 첫 번째 공식 크로스 시스템 벤치마크로, 기존 시스템별 고립된 벤치마크 패러다임을 혁신.

- **IMO 그랜드 챌린지와의 연계**: 형식-대-형식(F2F) 경쟁 설정을 향한 구체적 중간 단계로서, 단순히 벤치마크를 넘어 장기 연구 목표 제시.

- **다양한 정보원의 통합**: IMO, AIME, AMC, MATH 데이터셋과 고등학교/대학 수학을 하나의 일관된 형식 틀로 통합.

- **언어 모델 의존성 배제**: GPT-f를 사용한 기선 결과도 제시하지만 벤치마크 자체는 DeepHOL, Holophrasm 등 비신경망 정리 증명 시스템에도 동등하게 적용 가능하도록 설계.

## Limitation & Further Study

- **형식화 적용범위 제한**: 다중 선택, 문장 문제, 증명 대상 찾기 문제의 형식화가 어려워 Olympiad 문제의 상당 부분(특히 조합론, 기하)이 제외됨.

- **현황**: Isabelle과 HOL Light는 작성 시점에 부분적 지원만 가능하였고, Coq 확장은 미래 과제.

- **증명 제공 불완전성**: 형식화된 명제에 선택적으로만 정식 증명을 첨부하여 감독 학습 기반 접근의 제약.

- **후속 연구**: 
  - 기하학과 조합론 문제의 형식화 기술 발전에 따른 벤치마크 확대
  - 추가 형식 시스템(Coq) 지원 추가
  - 종합적 증명 데이터 수집으로 감독학습 강화
  - 인간 성능 벤치마킹과의 비교 분석

## Evaluation

- **Novelty**: 4.5/5
  - 신경 정리 증명의 첫 통합 크로스 시스템 벤치마크로 개념적 진전 명확하나, 기술적 혁신보다는 자원 통합 특성.

- **Technical Soundness**: 4/5
  - 계층화 분할, Pass@N 메트릭, 체계적 형식화 프로토콜이 기술적으로 타당하지만, 형식화 과정의 표준화 문서화 미흡.

- **Significance**: 5/5
  - 신경 정리 증명 분야의 공유 기준점으로서 거대한 실용적 영향력. IMO 그랜드 챌린지를 향한 구체적 중간 마일스톤 제시.

- **Clarity**: 4.5/5
  - 벤치마크 구성, 동기, 평가 방법이 명확하게 설명되었으나, 형식화 도전과제에 대한 다소 간결한 논의.

- **Overall**: 4.5/5

**총평**: 본 논문은 신경 정리 증명 커뮤니티의 오랫동안의 필요를 충족시키는 첫 번째 통합 벤치마크를 제공함으로써, 시스템 간 공정한 비교와 지속 가능한 연구 생태계 구축에 매우 큰 의의가 있는 작업이다.

## Related Papers

- 🔗 후속 연구: [[papers/379_Generative_language_modeling_for_automated_theorem_proving/review]] — GPT-f가 보여준 신경 정리 증명 가능성을 올림피아드 수준의 표준화된 벤치마크로 발전시킴
- 🧪 응용 사례: [[papers/264_Deepseek-prover_Advancing_theorem_proving_in_llms_through_la/review]] — DeepSeek-Prover의 대규모 형식 증명 데이터 합성 기법을 miniF2F 벤치마크로 평가할 수 있음
- 🏛 기반 연구: [[papers/288_Draft_sketch_and_prove_Guiding_formal_theorem_provers_with_i/review]] — 비형식적 증명에서 형식적 증명으로의 변환 방법론이 miniF2F 문제 해결의 기초가 됨
- 🧪 응용 사례: [[papers/1095_Towards_large_language_models_as_copilots_for_theorem_provin/review]] — miniF2F 벤치마크를 활용하여 LLM 기반 정리 증명 코파일럿의 성능을 체계적으로 평가
- 🔄 다른 접근: [[papers/339_Fimo_A_challenge_formal_dataset_for_automated_theorem_provin/review]] — IMO vs Olympiad 수준으로 유사하지만 다른 형식의 수학 정리증명 벤치마크
- 🔗 후속 연구: [[papers/808_Theoremqa_A_theorem-driven_question_answering_dataset/review]] — MinIF2F의 형식적 올림피아드 수학 벤치마크가 TheoremQA의 정리 적용 능력 평가를 더욱 엄밀하게 확장함
- 🧪 응용 사례: [[papers/379_Generative_language_modeling_for_automated_theorem_proving/review]] — GPT-f가 증명한 자동 정리 증명 가능성을 올림피아드 수준 문제로 확장한 벤치마크
- 🔗 후속 연구: [[papers/251_Data_for_mathematical_copilots_Better_ways_of_presenting_pro/review]] — miniF2F의 정적 증명 평가를 동기와 발견 과정을 포함한 풍부한 수학적 사고로 확장
- 🧪 응용 사례: [[papers/264_Deepseek-prover_Advancing_theorem_proving_in_llms_through_la/review]] — DeepSeek-Prover의 형식 증명 능력을 miniF2F 벤치마크로 체계적으로 평가할 수 있음
- 🏛 기반 연구: [[papers/482_Lean-star_Learning_to_interleave_thinking_and_proving/review]] — Lean-star의 형식 증명 생성 능력을 평가할 수 있는 표준화된 올림피아드 수준 벤치마크를 제공한다.
