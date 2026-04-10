---
title: "674_ReTool_Reinforcement_Learning_for_Strategic_Tool_Use_in_LLMs"
authors:
  - "Jiazhan Feng"
  - "Shijue Huang"
  - "Xingwei Qu"
  - "Ge Zhang"
  - "Yujia Qin"
date: "2025"
doi: "10.48550/arXiv.2504.11536"
arxiv: ""
score: 4.2
essence: "강화학습(RL)을 활용하여 LLM이 추론 과정 중 코드 인터프리터(Code Interpreter, CI)를 동적으로 호출하도록 학습시키는 프레임워크로, 수학 올림피아드 문제 해결에서 o1-preview를 27.9% 초과 달성한다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/Multi-Agent_Language_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Feng et al._2025_ReTool Reinforcement Learning for Strategic Tool Use in LLMs.pdf"
---

# ReTool: Reinforcement Learning for Strategic Tool Use in LLMs

> **저자**: Jiazhan Feng, Shijue Huang, Xingwei Qu, Ge Zhang, Yujia Qin | **날짜**: 2025 | **DOI**: [10.48550/arXiv.2504.11536](https://doi.org/10.48550/arXiv.2504.11536)

---

## Essence

강화학습(RL)을 활용하여 LLM이 추론 과정 중 코드 인터프리터(Code Interpreter, CI)를 동적으로 호출하도록 학습시키는 프레임워크로, 수학 올림피아드 문제 해결에서 o1-preview를 27.9% 초과 달성한다.

## Motivation

- **Known**: DeepSeek R1 등 RL 기반 추론 모델은 텍스트 추론에 탁월하지만, 기하학적 추론, 정밀 계산, 복잡한 방정식 풀이 등 구조화된 문제해결이 필요한 작업에서는 약점을 보임.

- **Gap**: 기존 프롬프팅/지도학습(SFT) 기반 도구 활용 방식은 학습된 데이터 분포 모방에 국한되어 도구 호출 시기와 방식을 적응적으로 학습하지 못함.

- **Why**: 텍스트 기반 추론은 수치 계산 오류 누적과 불확실성 증가 문제를 해결할 수 없으나, 코드 인터프리터는 형식적이고 검증 가능한 기호 계산 기능을 제공함.

- **Approach**: 냉시작(Cold-start) SFT 데이터 생성 + 코드 실행 피드백이 통합된 RL 학습으로 모델이 도구 호출 전략을 자율적으로 발견하도록 유도.

## Achievement

![Figure 1](figures/fig1.webp)
*AIME 2024 & 2025에서 ReTool(CI-powered RL)과 텍스트 기반 RL 베이스라인의 성능 비교*

1. **우수한 성능**: Qwen2.5-32B-Instruct 기반 ReTool이 AIME 2024에서 400 스텝으로 67.0% 달성 (텍스트 기반 RL은 1080 스텝에 40.0%). DeepSeek-R1-Distill-Qwen-32B 기반 72.5% 달성하여 o1-preview 초과.

2. **훈련 효율성**: 텍스트 기반 RL 대비 2.7배 빠른 수렴(400 vs 1080 스텝), 응답 길이 40% 감소로 토큰 효율성 개선.

3. **창발 행동**: 코드 자체 수정, 적응적 도구 선택, 동적 코드 호출 타이밍 조정 등 RL 학습 중 자동 발생.

## How

![Figure 2](figures/fig2.webp)
*텍스트 기반 RL(a)과 ReTool의 인터리빙된 코드 실행 RL(b) 비교*

**1단계: 냉시작 SFT**
- OpenThoughts 등 다양한 수학 추론 데이터 수집 및 DeepSeek-R1 검증으로 초기 데이터셋 D_init 구성
- 구조화된 프롬프트 템플릿으로 D_init을 자동 변환하여 수작업 계산 단계를 코드 스니펫 + 실행 결과로 대체
- 형식 검증(syntax) + 답변 검증(correctness) 2단계 필터링으로 D_CI 생성
- SFT로 모델에 도구 호출 기초 능력 부여

**2단계: 도구 통합 RL 학습**
- PPO 알고리즘 기반, 정책 모델이 코드 샌드박스와 협력하여 다중 턴 실시간 코드 실행 포함 롤아웃 생성
- `<code></code>` 태그로 코드 구간 표시, 종료 태그(</code>) 감지 시 코드 파싱 → 실행 → 피드백 필링 → 계속 생성
- 규칙 기반 정확도 보상(Equation 2): 최종 답안이 정답과 동치면 +1, 아니면 -1 (도구 실행 가능성 보상 미사용)
- 피드백 기반 outcome-driven 학습으로 도구 호출 시기, 방식, 선택 기준 자율 발견

## Originality

- **새로운 패러다임**: 텍스트/코드 혼합 롤아웃(hybrid rollout)을 RL 루프에 처음 통합하여 실시간 코드 실행 피드백으로 학습

- **데이터 파이프라인 혁신**: 구조화된 변환 + 이중 검증으로 코드 통합 추론 데이터셋 자동 생성 방법론 개발

- **단순한 보상 설계**: 도구 실행 가능성이 아닌 최종 정확도만 보상하여 reward hacking 방지 및 다양한 문제해결 전략 발현 유도

- **창발 현상 분석**: 코드 자체 수정, 동적 호출 타이밍 등이 감독 신호 없이 자율적으로 학습됨을 실증적 관찰

## Limitation & Further Study

- **보상 설계의 한계**: 이진 정확도 보상만 사용하여 부분 정답, 중간 계산 과정의 질, 코드 효율성 등을 반영하지 못함. 다단계 보상 함수 개발 필요.

- **도메인 특화성**: AIME 수학 문제에만 평가했으므로 다른 구조화된 문제(기하학, 과학 실험, 코드 생성 등)에 일반화 가능성 미검증.

- **코드 인터프리터 의존성**: 샌드박스 보안, 시간초과 처리, 복잡한 라이브러리 호출 등 실무 장애 요인에 대한 분석 부족.

- **후속 연구 방향**:
  - 계층적/혼합 보상 함수로 중간 단계 학습 품질 개선
  - 기하학, 자연과학, 프로그래밍 등 타 도메인 확대 실험
  - 모델 크기/RL 스텝에 따른 수렴 곡선 분석
  - 도구 호출 실패 시 fallback 메커니즘 연구

## Evaluation

- **Novelty**: 4.5/5 — 코드 실행을 RL 루프에 통합하는 아이디어는 신선하나, 개별 구성(SFT 데이터 변환, PPO, 규칙 기반 보상)은 기존 기법들의 조합.

- **Technical Soundness**: 4/5 — 방법론이 명확하고 실험 설계가 합리적이나, 보상 함수의 단순성과 샌드박스 안정성에 대한 상세 논의 부족.

- **Significance**: 4.5/5 — AIME 벤치마크에서 o1-preview 초과 달성은 임팩트 높으나, 도메인 특화 평가 및 일반화 가능성이 제한적.

- **Clarity**: 4/5 — 전반적으로 잘 작성되었으나, 롤아웃 메커니즘의 세부 구현(에러 처리, 타임아웃 등)과 창발 행동 분석이 더 상세하면 좋음.

- **Overall**: 4.2/5

**총평**: ReTool은 LLM의 도구 활용을 RL로 학습시키는 실용적이고 효과적인 프레임워크이며, AIME에서의 강한 성능과 창발 행동 관찰이 하이브리드 신경-기호 추론의 가능성을 시사한다. 다만 보상 설계 정교화와 다영역 일반화 검증이 필요하다.

## Related Papers

- 🔄 다른 접근: [[papers/390_Grammars_of_formal_uncertainty_When_to_trust_llms_in_automat/review]] — ReTool의 강화학습 기반 전략적 도구 사용과 확률문맥자유문법 기반 불확실성 정량화는 LLM 신뢰성을 서로 다른 방식으로 개선하는 접근이다.
- 🏛 기반 연구: [[papers/498_LLM_as_a_Mastermind_A_Survey_of_Strategic_Reasoning_with_Lar/review]] — LLM의 전략적 추론 능력에 대한 종합적 조사가 ReTool의 강화학습 기반 도구 사용 전략 개발의 이론적 토대를 제공한다.
- 🔗 후속 연구: [[papers/265_DeepSeek-R1_incentivizes_reasoning_in_LLMs_through_reinforce/review]] — DeepSeek-R1의 강화학습을 통한 추론 인센티브화가 ReTool의 전략적 도구 사용 학습을 더 광범위한 추론 능력으로 확장한 발전 형태이다.
- 🔄 다른 접근: [[papers/390_Grammars_of_formal_uncertainty_When_to_trust_llms_in_automat/review]] — 확률문맥자유문법 기반 불확실성 정량화와 강화학습 기반 전략적 도구 사용은 LLM의 신뢰성 문제를 서로 다른 방식으로 해결하는 접근이다.
- 🔗 후속 연구: [[papers/498_LLM_as_a_Mastermind_A_Survey_of_Strategic_Reasoning_with_Lar/review]] — ReTool의 강화학습 기반 전략적 도구 사용이 LLM의 전략적 추론 능력을 실제 문제 해결에 적용한 구체적 확장 사례이다.
