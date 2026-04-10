---
title: "822_Towards_a_Science_of_AI_Agent_Reliability"
authors:
  - "Stephan Rabanser"
  - "Sayash Kapoor"
  - "Peter Kirgis"
  - "Kangheng Liu"
  - "Saiteja Utpala"
date: "2026.02"
doi: "10.48550/arXiv.2602.16666"
arxiv: ""
score: 4.6
essence: "AI 에이전트(agents)의 실제 배포 환경에서 높은 정확도에도 불구하고 신뢰성 부족이 심각한 문제임을 보여주며, 안전-임계 엔지니어링(safety-critical engineering)의 원칙을 기반으로 일관성, 견고성, 예측가능성, 안전성의 4가지 차원으로 분해한 신뢰성 평가 메트릭 12개를 제시한다."
tags:
  - "cat/Cognitive_AI_Evaluation_and_Benchmarking"
  - "sub/Cognitive_LLM_Evaluation"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Rabanser et al._2026_Towards a Science of AI Agent Reliability.pdf"
---

# Towards a Science of AI Agent Reliability

> **저자**: Stephan Rabanser, Sayash Kapoor, Peter Kirgis, Kangheng Liu, Saiteja Utpala, Arvind Narayanan | **날짜**: 2026-02-18 | **DOI**: [10.48550/arXiv.2602.16666](https://doi.org/10.48550/arXiv.2602.16666)

---

## Essence

![Figure 1](figures/fig1.webp)
*신뢰성 향상이 능력 향상보다 뒤처짐. 정확도는 꾸준히 상승하지만 신뢰성은 미미한 개선만 보임*

AI 에이전트(agents)의 실제 배포 환경에서 높은 정확도에도 불구하고 신뢰성 부족이 심각한 문제임을 보여주며, 안전-임계 엔지니어링(safety-critical engineering)의 원칙을 기반으로 일관성, 견고성, 예측가능성, 안전성의 4가지 차원으로 분해한 신뢰성 평가 메트릭 12개를 제시한다.

## Motivation

- **Known**: 표준 벤치마크에서 AI 에이전트의 정확도(accuracy) 점수가 꾸준히 상승하고 있으며, 많은 모델들이 높은 성능으로 평가받고 있음
- **Gap**: 실제 배포 환경에서는 에이전트들이 지속적으로 실패하고 있음 (Replit 데이터베이스 삭제 사건, OpenAI Operator 미승인 구매, NYC 챗봇의 위법 조언 등). 단일 성공률 메트릭만으로는 이러한 운영상 결함을 감지할 수 없음
- **Why**: 정확도는 일관된 실패와 무작위 실패를 구분하지 못하고, 경미한 오류와 치명적 오류를 구별하지 못하며, 입력 변동에 대한 민감성이나 신뢰도 보정(confidence calibration)을 평가하지 못함
- **Approach**: 안전-임계 엔지니어링 분야(항공, 원전, 자동차)의 수십 년 관행으로부터 신뢰성의 4가지 핵심 차원을 도출하고, 각 차원에 대한 구체적인 메트릭을 정의하여 14개 에이전트 모델을 2개 벤치마크에서 평가

## Achievement

![Figure 2](figures/fig2.webp)
*결과 일관성: 모델 간 편차 분석*

1. **신뢰성 평가 프레임워크 구축**: 일관성(consistency), 견고성(robustness), 예측가능성(predictability), 안전성(safety)의 4가지 독립적 차원에서 12개의 구체적이고 계산 가능한 메트릭 제안. 이 메트릭들은 원시 정확도와 무관하게 서로 다른 능력 수준의 에이전트들을 비교 가능하게 함

2. **신뢰성-능력 괴리 실증**: 18개월 동안의 모델 릴리스에서 정확도는 연 0.21 기울기로 꾸준히 향상되지만, 신뢰성(R)은 연 0.03에 불과한 미미한 개선만 달성. 벤치마크 간 정확도-신뢰성 상관계수 차이(0.63~0.73에서 0.46~0.82로 변동)는 정확도 향상이 신뢰성 향상을 보장하지 않음을 시사

3. **현대 에이전트의 신뢰성 프로필 분석**: 일관성(run-to-run repeatability)과 예측가능성이 즉각적인 연구 초점이 필요한 가장 약한 차원임을 특정. 모델들이 동일 조건에서 다양한 출력을 보이며, 자신의 실패 가능성을 충분히 인식하지 못함

## How

![Figure 3](figures/fig3.webp)
*프롬프트 견고성: 입력 변동에 따른 성능 저하*

**신뢰성 메트릭 설계:**

- **일관성** (Consistency): 
  - pass∧k (모든 k회 시도에서 성공) vs pass@k (최소 1회 성공)의 비율
  - 출력 변동성(output variance) 측정: 동일 입력에 대한 k번 반복 실행의 분산

- **견고성** (Robustness):
  - 프롬프트 변형(prompt paraphrasing)에 대한 성능 유지율
  - 입력 노이즈 주입(input noise injection) 시 성능 저하율
  - 도구/환경 변동(tool perturbation) 하에서의 성능 변화

- **예측가능성** (Predictability):
  - 보정 오차(calibration error): 모델 신뢰도와 실제 정확도의 일치도
  - 선택적 예측(selective prediction): 신뢰 임계값 설정으로 실패 사례의 인식 가능성
  - ROC-AUC 및 AURC (Area Under the Risk-Coverage curve)

- **안전성** (Safety):
  - 실패 심각도 분류(failure severity categorization): 치명적(catastrophic) vs 경미한(benign) 오류의 분포
  - 최악의 경우 오류 크기(worst-case error magnitude) 측정
  - 심각 오류 확률(probability of severe failures)

**평가 설정:**
- 벤치마크 1: GAIA (일반 지능 에이전트 능력)
- 벤치마크 2: τ-bench (에이전트 신뢰성 특화 벤치마크)
- 모델: OpenAI (GPT-4 Turbo, o1, GPT 5.2 등), Google (Gemini 2.0~3.0), Anthropic (Claude 3.5~4.5)

## Originality

- **안전-임계 엔지니어링의 체계적 적용**: 항공, 원전, 자동차, 산업 공정 제어 분야의 신뢰성 관행(수십 년 축적)을 AI 에이전트 평가에 처음으로 통합적으로 적용. 기존 ML 연구의 산발적 현상들(프롬프트 민감성, 부동소수점 비결정성, calibration, selective prediction)을 통일된 프레임워크로 연결

- **정확도 독립적 메트릭**: 원시 정확도와 완전히 독립적인 12개 메트릭 설계로, 능력 수준이 다른 모델들의 신뢰성을 동등하게 비교 가능하게 함 (기존 작업의 한계 극복)

- **대규모 실증 분석**: 14개 최신 에이전트 모델의 신뢰성 프로필을 최초로 체계적으로 매핑. 정확도-신뢰성 괴리의 정량적 증거 제시 (연간 기울기: 정확도 0.21/yr vs 신뢰성 0.03/yr)

- **상호 보완적 벤치마크 활용**: GAIA(일반 능력)와 τ-bench(신뢰성 특화)의 결과 비교로 벤치마크 간 신뢰성 특성의 변동성을 드러냄

## Limitation & Further Study

- **범위의 한정성**: 논문은 신뢰성을 실증 측정 가능한 운영상 성질(operational property)로 제한하며, 값 정렬(value alignment), 진정성(honesty), 해석가능성(interpretability) 등 광범위한 AI 안전 분류학은 다루지 않음. 신뢰성 개선 알고리즘은 제시하지 않음

- **위협 모델의 제한**: 자연 변동(natural variation)과 우발적 오류(incidental faults)만 모델링하며, 적대적 공격(adversarial attacks) 또는 최악의 경우(worst-case threat models)는 고려 대상 아님

- **일관성 차원의 해석 필요성**: LLM의 확률적 특성(stochastic nature) 때문에 완전한 결정론적 일관성은 현실적이지 않을 수 있으며, 허용 가능한 변동 수준에 대한 실무 기준 부재

- **후속 연구 방향**:
  - 신뢰성 개선을 위한 알고리즘적 접근 (예: 일관성/예측가능성 향상 기법 개발)
  - 실제 배포 환경에서의 신뢰성 메트릭 검증
  - 도메인별 신뢰성 요구사항 추상화 (각 응용 분야별 메트릭의 가중치 설정)
  - 신뢰성과 능력 향상의 trade-off 분석


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4.5/5
- Significance: 4.8/5
- Clarity: 4.5/5
- Overall: 4.6/5

**총평**: 이 논문은 AI 에이전트 평가의 근본적인 격차를 정확히 진단하고, 안전-임계 엔지니어링의 검증된 원칙을 적용하여 신뢰성의 다차원 프레임워크를 제시함으로써 이론과 실무 간의 괴리를 해소하는 데 중요한 기여를 한다. 특히 대규모 모델들의 실증적 신뢰성 프로필을 최초로 제공하고 정확도-신뢰성 괴리의 정량화는 향후 에이전트 개발의 우선순위 설정에 중요한 지침이 될 것으로 예상된다.

## Related Papers

- 🏛 기반 연구: [[papers/750_SEVerA_Verified_Synthesis_of_Self-Evolving_Agents/review]] — 형식적 안전성 보증은 AI 에이전트 신뢰성의 핵심 요소임
- 🔗 후속 연구: [[papers/471_Large_Language_Models_Cannot_Self-Correct_Reasoning_Yet/review]] — 자기 수정 불가능성 문제가 에이전트 신뢰성 평가의 중요한 차원임
- 🧪 응용 사례: [[papers/040_AAAI_Presidential_Panel_Report_on_the_Future_of_AI_Research/review]] — AI 에이전트 신뢰성의 과학적 접근을 통해 AI 연구의 미래 방향을 구체화한다.
- 🏛 기반 연구: [[papers/865_Vending-Bench_A_Benchmark_for_Long-Term_Coherence_of_Autonom/review]] — AI 에이전트 신뢰성 과학에 대한 기초 연구로 장기간 일관성 평가의 이론적 근거를 제공한다.
