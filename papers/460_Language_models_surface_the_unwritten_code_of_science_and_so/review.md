---
title: "460_Language_models_surface_the_unwritten_code_of_science_and_so"
authors:
  - "Honglin Bao"
  - "Siyang Wu"
  - "Jiwoong Choi"
  - "Yingrong Mao"
  - "James A. Evans (University of Chicago)"
date: "2025"
doi: "arXiv:2505.18942"
arxiv: ""
score: 4.2
essence: "대규모 언어모델(LLM)이 내재된 편향을 진단 도구로 활용하여 과학과 사회의 \"불문율(unwritten code)\" — 암묵적 고정관념, 휴리스틱, 암수정인 규범 — 을 명시적으로 드러내고 비판 대상으로 만들 수 있다는 주장."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/AI_in_Scientific_Research"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Tuck and Yang_2025_Language models surface the unwritten code of science and society.pdf"
---

# Language models surface the unwritten code of science and society

> **저자**: Honglin Bao, Siyang Wu, Jiwoong Choi, Yingrong Mao, James A. Evans (University of Chicago) | **날짜**: 2025 | **DOI**: [arXiv:2505.18942](https://arxiv.org/abs/2505.18942)

---

## Essence

![Figure 1](figures/fig1.webp)
*자기-강화(self-reinforcement)를 통해 암묵적 규범을 점진적으로 증폭시켜 모델이 명시적으로 표현하도록 유도하는 개념적 틀*

대규모 언어모델(LLM)이 내재된 편향을 진단 도구로 활용하여 과학과 사회의 "불문율(unwritten code)" — 암묵적 고정관념, 휴리스틱, 암수정인 규범 — 을 명시적으로 드러내고 비판 대상으로 만들 수 있다는 주장.

## Motivation

- **Known**: LLM은 훈련 데이터에 내재된 인간의 편향을 흡수하며, 이러한 편향이 사회적 불평등을 재생산할 수 있다는 것이 알려져 있음.

- **Gap**: 기존 연구는 LLM의 편향을 적발하는 데 집중했으나, 더 깊은 수준의 암묵적 규범(reasoning과정에서 작동하는 휴리스틱)을 추출할 수 없었음. 단순한 연관어 분석(word association) 등의 기법은 표면적 편향만 드러냄.

- **Why**: 암묵적 규범들이 "불문율"로 남아있으면 형식화되거나 체계적으로 분석되지 않아 시스템적 부등을 영속화함. 이를 명시화하려면 LLM의 내재적 편향을 의도적으로 증폭시켜 외부화할 필요가 있음.

- **Approach**: 동료 심사(peer review)의 암묵적 평가 기준을 사례로, 가설 생성-자기일관성 검증-반복 탐색을 통해 LLM의 선험적 신념(prior)을 사후적 판단(posterior)으로 업데이트하는 프레임워크 제시.

## Achievement

![Figure 2](figures/fig2.webp)
*가설 탐색을 통한 선험적 신념에서 사후적 신념으로의 전환 과정*

1. **은폐된 동료심사 기준 발굴**: 46개 학술 컨퍼런스의 26,731편 논문 데이터를 분석하여, 심사자들이 명시적으로 언급하지 않으면서도 암묵적으로 보상하는 평가 기준을 식별. 이론적 엄밀성(theoretical rigor)은 LLM의 선험적 신념과 부합하지만(상관계수=0.49), 맥락화와 스토리텔링(contextualization & storytelling)은 심사자들이 명시적으로 피하면서(상관계수=-0.14) 동시에 점수로는 암묵적으로 보상함.

2. **일관된 편향 패턴 확인**: 선험적 신념의 우위에서 사후적 판단으로의 전환이 다양한 모델과 표본 외(out-of-sample) 평가에서 강건하게 나타남. 4라운드 반복 탐색으로 20개 가설이 97%의 사례를 설명.

## How

![Figure 4](figures/fig4.webp)
*선험적 신념 대비 사후적 신념: 각 가설의 지수는 선험 빈도 변화의 순위를 나타냄*

**방법론적 특징:**

- **데이터 표현**: 전체 논문 텍스트 대신 확장 초록(extended abstract)을 사용. GPT-4o로 배경, 핵심 아이디어, 방법론, 실험 결과, 영향력을 통합한 구조화된 표현 생성. (문맥 윈도우 제약과 장문 입력의 할루시네이션 위험 해소)

- **가설 생성**: 점수 격차가 1 표준편차 이상인 논문 쌍(총 50쌍 샘플) 비교를 통해 LLM이 5개 가설 자동 생성.

- **자기일관성 검증**: 각 가설을 전체 논문 쌍에 적용하여 0~10 신뢰도 점수로 설명력 평가. 3회 투표와 신뢰도 가중 방식(confidence-weighted voting) 적용.

- **반복 탐색**: 설명되지 않은 사례들(unexplained pairs)에 대해 기존 가설과 구별되는 새로운 가설 생성. 설명 불가능 사례가 5% 이하로 떨어질 때까지 반복.

- **선험/사후 추출**: 데이터 없이 "좋은 논문의 요건"을 물어 선험 P(hypothesis) 추출(250회 시뮬레이션×5 가설×4라운드=5,000 사전 가설). 실제 논문 쌍 비교 시 업데이트된 사후 P(hypothesis|data) 획득.

- **위치 편향 완화**: 논문 위치를 무작위화하며 투표 진행, 위치 간 일관성 77% 달성.

## Originality

- **새로운 관점**: LLM 편향을 제거 대상이 아닌 **진단 도구**로 역전시킨 독창적 프레임. 인간의 불문율을 명시화하는 도구로서의 LLM 활용 제시.

- **체계적 프레임워크**: Bayesian 선험-사후 업데이트 논리와 자기일관성 검증, 반복 탐색을 결합한 구조화된 방법론. 기존 가설 생성 AI 연구와 구별되는 **증폭과 외부화(amplification & externalization)** 메커니즘.

- **학제적 통찰**: 과학철학의 동료심사 비판과 AI의 편향 연구를 연결. 논문 평가의 "미학(aesthetic)"을 경험적으로 규명한 첫 사례.

- **확장성**: 과학뿐 아니라 사회 전반의 암묵적 규범(채용 기준, 신용평가, 정책 우선순위 등)에 적용 가능한 범용 프레임.

## Limitation & Further Study

- **데이터 표현의 손실**: 확장 초록으로의 변환 과정에서 원문 정보가 압축되어, 미묘한 글쓰기 스타일, 도표, 표 등이 손실될 수 있음. 일관성 0.89는 높지만 11% 정보 손실 존재.

- **인과성 미해결**: 가설이 점수 차이를 "설명"하더라도 인과적 메커니즘(causality)은 확인되지 않음. 예: "스토리텔링"이 좋은 점수의 원인인지 결과인지 불분명.

- **모델 종속성**: LLM의 선험적 신념이 훈련 데이터 분포에 크게 의존. 다른 시기, 다른 언어 모델에서 선험이 어떻게 달라질지 검토 필요.

- **심사자 다양성 부재**: 리뷰 점수만 사용하고 심사자의 인구통계학적 배경, 전문 분야, 개인적 편향을 고려하지 않음. 동일 논문에 대한 심사자 간 이질성 분석 부족.

- **윤리적 함의의 심화**: LLM이 사회의 편향을 증폭시킬 위험성. 이러한 "불문율" 공개가 오히려 고정관념을 정당화하는 데 악용될 가능성에 대한 논의 부족.

**후속 연구:**
- 인과 추론 기법(causal inference) 도입으로 발견된 가설의 인과성 검증
- 전체 논문 텍스트 처리 가능한 거대 언어모델의 발전에 따른 재검증
- 심사자 특성을 고려한 조건부 분석(conditional analysis)
- 불문율 공개 후 실제 학술평가 제도 개선 효과 측정


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4/5
- Significance: 4.5/5
- Clarity: 4/5
- Overall: 4.2/5

**총평**: 이 논문은 LLM의 편향을 사회 진단의 도구로 재해석하는 혁신적 관점을 제시하며, 과학 평가의 암묵적 기준을 최초로 규명한 엄밀한 실증 연구다. 다만 인과성 확립, 실제 제도 개선 효과 검증, 그리고 이러한 "불문율" 공개의 윤리적 함의에 대한 더 깊은 성찰이 필요하다.

## Related Papers

- ⚖️ 반론/비판: [[papers/192_Cchall_A_novel_benchmark_for_joint_cross-lingual_and_cross-m/review]] — LLM의 편향을 진단 도구로 활용하자는 관점과 교차-언어/모달 환각을 문제로 보는 관점이 대조됨
- 🔗 후속 연구: [[papers/394_Grounding_fallacies_misrepresenting_scientific_publications/review]] — 과학과 사회의 암묵적 편향을 드러내는 일반적 접근을 과학 출판물 오용 탐지라는 구체적 응용으로 확장함
- 🏛 기반 연구: [[papers/247_Cultural_evolution_in_populations_of_large_language_models/review]] — 대규모 언어모델 집단에서의 문화적 진화 연구가 과학과 사회의 불문율을 드러내는 LLM 활용의 이론적 배경을 제공함
- 🏛 기반 연구: [[papers/410_How_deep_do_large_language_models_internalize_scientific_lit/review]] — 언어 모델이 과학과 사회의 암묵적 코드를 드러내는 연구로 마태 효과 강화 현상의 이론적 배경을 제공한다.
- ⚖️ 반론/비판: [[papers/192_Cchall_A_novel_benchmark_for_joint_cross-lingual_and_cross-m/review]] — LLM의 편향을 진단 도구로 활용하자는 관점과 교차-언어/모달 환각을 문제로 보는 관점이 대조됨
- 🏛 기반 연구: [[papers/394_Grounding_fallacies_misrepresenting_scientific_publications/review]] — 과학과 사회의 암묵적 편향을 드러내는 연구가 과학 출판물을 잘못 인용하는 논리적 오류 탐지의 맥락을 제공함
