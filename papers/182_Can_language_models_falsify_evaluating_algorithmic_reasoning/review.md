---
title: "182_Can_language_models_falsify_evaluating_algorithmic_reasoning"
authors:
  - "Shiven Sinha"
  - "Shashwat Goel"
  - "P. Kumaraguru"
  - "Jonas Geiping"
  - "Matthias Bethge"
date: "2025"
doi: "10.48550/arXiv.2502.19414"
arxiv: ""
score: 4.25
essence: "언어 모델(LM)이 프로그래밍 문제의 **부정확한 해결책에 대한 반례(counterexample)를 생성할 수 있는가**라는 질문에 답하는 논문으로, REFUTE 벤치마크를 통해 최신 LM들이 반례 생성 능력에서 심각한 한계를 보임을 실증적으로 입증한다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/Mechanistic_AI_Interpretability"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Sinha et al._2025_Can language models falsify evaluating algorithmic reasoning with counterexample creation.pdf"
---

# Can language models falsify? evaluating algorithmic reasoning with counterexample creation

> **저자**: Shiven Sinha, Shashwat Goel, P. Kumaraguru, Jonas Geiping, Matthias Bethge, Ameya Prabhu | **날짜**: 2025 | **DOI**: [10.48550/arXiv.2502.19414](https://doi.org/10.48550/arXiv.2502.19414)

---

## Essence

![Figure 1](https://arxiv.org/html/2502.19414v1/x1.png)
*그림 1: 표준 벤치마크는 모델의 해결책 생성 능력을 평가하는 반면, 본 논문은 부정확한 해결책을 반박(falsify)하는 역 벤치마크를 제안한다.*

언어 모델(LM)이 프로그래밍 문제의 **부정확한 해결책에 대한 반례(counterexample)를 생성할 수 있는가**라는 질문에 답하는 논문으로, REFUTE 벤치마크를 통해 최신 LM들이 반례 생성 능력에서 심각한 한계를 보임을 실증적으로 입증한다.

## Motivation

- **Known**: 
  - 언어 모델은 알고리즘 문제 해결에서 전문가 수준의 성능을 보임 (LiveCodeBench 기준 최대 50% 정확도)
  - 현존 벤치마크는 모두 "올바른 해결책 생성" 능력 평가에 집중
  
- **Gap**: 
  - 과학 발전의 핵심인 "가설 반박(falsification)" 능력을 평가하는 벤치마크 부재
  - 연구자들이 부정확한 주장의 반례를 찾기 위해 투입하는 막대한 노력과 창의성에 대한 LM의 능력 미평가

- **Why**: 
  - 모델이 자신의 오류를 찾지 못하면 자가 수정(self-repair)이 불가능
  - 인간이 지식을 제공할 수 없는 신규 문제 영역에서 모델의 신뢰성 확보 필수
  - 반박 능력은 검증(verification) 능력의 핵심으로, 향후 AI 안전성과 oversight에 중요

- **Approach**: 
  - 반례 생성이 코드 실행으로 자동 검증 가능한 알고리즘 영역에서 시작
  - 2024-2025년 Codeforces 대회의 부정확한 제출 코드(324개 샘플)로 REFUTE 벤치마크 구성
  - OpenAI o3-mini, DeepSeek R1 등 최신 모델들을 ReAct 에이전트 프레임워크로 평가

## Achievement

![Figure 2](https://arxiv.org/html/2502.19414v1/x2.png)
*그림 2: 데이터 수집 파이프라인. 647개 문제에서 필터링을 통해 최종 324개 샘플로 구성된 REFUTE 벤치마크 생성.*

1. **성능 격차의 실증적 입증**: 
   - 50% 해결 능력을 보이는 o3-mini가 반례 생성에서는 **<9% 성공률만 기록**
   - DeepSeek R1도 유사한 성능 (약 8-9%)
   - Few-shot prompting, chain-of-thought, code execution feedback을 모두 적용해도 개선 미미

2. **검증-생성 격차(generator-verifier gap) 규명**:
   - 부정확한 해결책 검증이 때로 그 문제를 올바르게 푸는 것보다 **더 어려움**을 증명
   - 자동 테스트 케이스 생성만으로는 불충분 (반례는 조합론적으로 큰 입력 공간의 비자명한 영역에 위치)
   - 모델이 오류 탐지 능력이 부족하면 자동 수정도 불가능함을 시사

3. **동적 업데이트 벤치마크 제공**:
   - Codeforces의 최신 문제(2024-2025)로 훈련 데이터 오염 방지
   - LiveCodeBench 방식 따르며 정기적 업데이트로 장기적 평가 체계 구축

## How

![Figure 3](https://arxiv.org/html/2502.19414v1/x3.png)
*그림 3: 부정확한 해결책이 통과하는 테스트 케이스 분포. 중앙값이 65-85% 통과로, 단순 무작위 탐색으로는 반례 발견 불가능함을 보여줌.*

**데이터 수집 및 필터링:**
- Codeforces 문제(647개) → 필터링 단계별 감소 → 최종 324개 샘플
  - "쉽게 평가 가능": 자동 검증 인프라 필요
  - "자명하지 않은 해결책": 단순 휴리스틱으로 풀 수 없어야 함
  - "무작위 입력으로 실패 가능성 낮음": 반례 발견이 추론 요구
  - "해킹 미끼 아님": 의도적 함정 제외

**반례 검증 메커니즘:**
- 모델이 입력을 생성하는 **프로그램 코드** 출력 (직접 입력 대신)
- 두 단계 검증:
  1. 생성 코드 실행 → 입력이 제약조건 만족 확인 (H 검증)
  2. 부정확 코드 A와 정답 코드 A*의 출력 비교 (P 검증)

**평가 설정:**
- 모델: LiveCodeBench 랭킹 상위 5개 개발사의 최신 모델
- 프롬프팅: Few-shot (2-3 예시) + Chain-of-Thought + ReAct 에이전트 (코드 실행 피드백)
- 비교 기준: 같은 문제를 해결할 때 각 모델의 성공률

**필터링 엄격성:**
- 개별 테스트만으로 95%+ 통과하는 샘플 제외 (무작위 탐색 가능)
- 메타데이터: 문제 난이도, 주제(그래프/DP/수학 등), 필터 원인 주석

## Originality

- **역 벤치마크 개념 정립**: "생성 능력" 중심에서 "검증/반박 능력"으로 패러다임 전환
  - 기존 fact-checking, code repair와 다르게 **자동 검증 가능한 정량적 평가** 가능

- **알고리즘 도메인 선택의 전략성**: 
  - 형식 검증(formal verification)과 달리, **자명하지 않은 테스트 케이스** 발견에 창의적 추론 필수
  - Codeforces 부정확 제출의 사용으로 "실제 인간 오류" 기반

- **동적 벤치마크 관리**: 
  - 정기 업데이트로 훈련 데이터 오염 방지 (LiveCodeBench 따라)
  - 장기 추적 가능한 평가 인프라

- **이론적 명확화**: 
  - 반례 생성을 형식적으로 정의 (H⟹P 명제와 부정 입력 x*)
  - 검증-생성 격차의 정량적 증거 제시

## Limitation & Further Study

- **도메인 제약**:
  - 알고리즘 문제로만 평가 (과학 주장, 수학 증명 등 일반화 미검토)
  - 자동 검증 불가능한 영역(자연어 주장 등)에의 적용 방법 미제시

- **반례 난이도 분석 부족**:
  - 어떤 특성의 반례가 더 어려운지 분석 미흡
  - 필터링이 과도하여 남은 샘플의 특성 편향 가능성

- **모델 크기/능력 범위**:
  - 평가 대상이 최신 대형 모델(o3, R1)에 한정
  - 소형 모델, 파인튜닝 모델의 성능 미평가

- **개선 방법 제시 부재**:
  - 낮은 성능 원인의 상세 분석 부족
  - 반례 생성 능력 향상 방법(특화 학습, 프롬프팅 전략 등) 미제시

- **후속 연구 방향**:
  - 다른 도메인(수학, 과학 주장)으로 확대 및 자동 검증 메커니즘 개발
  - 반례 생성과 자가 수정 능력의 연관성 심화 연구
  - 모델의 "창의적 탐색" vs "체계적 탐색" 전략 비교 분석


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4/5
- Significance: 4.5/5
- Clarity: 4/5
- Overall: 4.25/5

**총평**: 언어 모델의 "반박(falsification)" 능력이라는 과학적으로 중요하면서도 벤치마크되지 않은 영역을 처음 정식화하고, 자동 검증 가능한 알고리즘 도메인에서 체계적으로 평가한 점에서 선도적 공헌이다. 다만 도메인의 제약성, 개선 방법의 부재, 일반화 가능성 미검증이 아쉬우므로, 후속 연구에서 다양한 도메인으로의 확대와 모델 개선 전략 연구가 필수적이다.

## Related Papers

- 🏛 기반 연구: [[papers/527_Mechanistic_interpretability_for_ai_safetya_review/review]] — 신경망의 내부 작동 메커니즘 이해가 언어모델의 반례 생성 실패 원인을 분석하는 기반을 제공한다
- 🔗 후속 연구: [[papers/471_Large_Language_Models_Cannot_Self-Correct_Reasoning_Yet/review]] — LLM의 추론 자체 수정 능력 한계와 반례 생성 실패가 연결된 근본적 문제를 다룬다
- 🧪 응용 사례: [[papers/264_Deepseek-prover_Advancing_theorem_proving_in_llms_through_la/review]] — 정리 증명에서 LLM의 논리적 추론 능력을 반례 생성 맥락에서 평가할 수 있다
- 🔄 다른 접근: [[papers/339_Fimo_A_challenge_formal_dataset_for_automated_theorem_provin/review]] — 형식 추론에서 LLM vs 전통적 자동 정리 증명의 다른 접근법을 비교할 수 있다
- 🧪 응용 사례: [[papers/527_Mechanistic_interpretability_for_ai_safetya_review/review]] — 기계론적 해석가능성을 언어모델의 반례 생성 실패 메커니즘 분석에 적용할 수 있다
