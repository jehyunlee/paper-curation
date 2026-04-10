---
title: "631_Predicting_field_experiments_with_large_language_models"
authors:
  - "Yaoyu Chen"
  - "Yuheng Hu"
  - "Yingda Lu"
date: "2025"
doi: "미제공"
arxiv: ""
score: 4.0
essence: "대규모 언어 모델(LLM)을 이용하여 경제학 문헌의 현장 실험(field experiment) 결과를 자동으로 예측하는 프레임워크를 제안하고, 276개 실험에서 78%의 예측 정확도를 달성했다."
tags:
  - "cat/LLM-Based_Scientific_Reasoning"
  - "sub/Human-AI_Experimental_Design"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Chen et al._2025_Predicting field experiments with large language models.pdf"
---

# Predicting field experiments with large language models

> **저자**: Yaoyu Chen, Yuheng Hu, Yingda Lu | **날짜**: 2025 | **DOI**: 미제공

---

## Essence

대규모 언어 모델(LLM)을 이용하여 경제학 문헌의 현장 실험(field experiment) 결과를 자동으로 예측하는 프레임워크를 제안하고, 276개 실험에서 78%의 예측 정확도를 달성했다.

## Motivation

- **Known**: LLM은 인간 행동 시뮬레이션, 콘텐츠 생성 등 뛰어난 능력을 보유하고 있으며, 기존 연구에서 심리학·사회학 분야의 실험실(lab) 실험을 성공적으로 복제함
- **Gap**: 기존 연구는 (1) 실험실 실험에만 집중하고 현장 실험은 미다룸, (2) 수동 프로세스로 소규모 실험만 검증, (3) 리커트 척도 기반 설문 실험에 제한됨, (4) 복잡한 사회 이슈별 성능 차이를 미분석
- **Why**: 현장 실험은 비용이 크고 오래 걸리므로, LLM을 통한 사전 예측이 가능하면 연구 효율성을 크게 향상시킬 수 있음
- **Approach**: 자동화된 3단계 프레임워크(정보 추출 → 변형 생성 → 예측)를 통해 대규모 현장 실험 예측

## Achievement

![Figure 1: The Data Collection Workflow](figures/fig1.webp)
*논문 수집 및 필터링 과정: 6,544개 논문에서 최종 276개의 현장 실험 선정*

1. **대규모 자동화 평가**: 2000-2024년 경제학 주요 저널 276개 논문(1,261개 결론)에서 78% 평균 예측 정확도 달성 - 기존 소규모 수동 방식의 한계 극복

2. **이분포/왜도 특성 발견**: 예측 결과가 양극단 분포 - 71%의 결론에서 거의 100% 정확도, 18%에서는 거의 0% 정확도로 나타나, 특정 주제에 대한 LLM의 근본적 한계 시사

3. **데이터 누수 방지 및 복잡성 증대**: Claude(추출/검증용)와 GPT(예측용) 분리 사용, 인간-객체 상호작용 포함 복잡한 처치 설계 지원

## How

![Figure 2: Prediction Framework](figures/fig2.webp)
*3단계 프레임워크: 정보 추출(Claude) → 변형 생성(Claude) → 예측(GPT)*

**프레임워크 구성:**
- **정보 추출 단계**: Claude를 사용하여 논문에서 실험 설정(participant, intervention, outcome 등) 자동 추출
- **변형 생성 단계**: 실제 결론과 유사한 거짓 변형(distractor)을 자동 생성하여 LLM 혼동 방지
- **예측 단계**: Chain-of-Thought 프롬프트 템플릿 2개 활용, GPT에 다지선다형 결론 예측 요청
- **데이터 검증**: 2층 검증(제목+초록 → 전체 논문) + 수동 규칙 기반 최종 검증으로 자동화 정확성 보장

**주요 특징:**
- 미세 조정(fine-tuning) 또는 정렬 기술 미사용
- 2024년 실험으로 최근성 테스트 수행
- 민족, 사회규범, 윤리적 딜레마 등 복잡 사안 성능 저하 분석

## Originality

- **첫 대규모 필드 실험 시뮬레이션**: 기존의 소규모 실험실 실험 복제를 현장 실험으로 확장하며, 다양한 참여자 배경과 복잡한 처치 설계를 다룸
- **완전 자동화 프레임워크**: 정보 추출부터 예측까지 전체 파이프라인 자동화로 확장성 확보
- **한계 조건 명시화**: 단순히 성공 사례가 아닌, LLM이 실패하는 주제 영역(사회적 편향, 윤리 이슈 등)을 체계적으로 분석하여 신뢰성 있는 응용 범위 제시
- **방법론적 엄격성**: 데이터 누수 방지를 위해 서로 다른 LLM 모델 사용, 이중 검증 프로세스 적용

## Limitation & Further Study

**한계:**
- 경제학 논문 중심으로 데이터셋 편향 (타 분야 일반화 불명확)
- 완전 자동화된 정보 추출이 복잡한 논문 설명에서 정보 손실 가능
- 78% 정확도는 높지만, 특정 주제(민족 차별, 사회규범)에서 심각한 성능 저하 미해결
- LLM의 학습 데이터 컷오프와 2024년 실험의 실제 누수 여부 불명확
- 왜 특정 주제에서 실패하는지에 대한 깊이 있는 인과 분석 부족

**후속 연구:**
- 실패 케이스에 대한 정성적 분석 및 프롬프트 최적화 연구
- 다양한 학문 분야(의학, 심리학, 마케팅) 현장 실험으로 확대
- LLM 편향(gender bias, social norm bias)과 예측 성능 관계 정량 분석
- 구조화된 결론 정보(가설, 기제, 효과 크기)와의 상호작용 분석
- 예측 기반 실험 설계 최적화 방법론 개발


## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 현장 실험 예측이라는 새로운 도메인으로 LLM 시뮬레이션을 확장하고 대규모 자동화 평가를 통해 실질적 적용 가능성을 보였으나, LLM의 근본적 한계(복잡한 사회 이슈 처리 부족)가 명확하여 실무 적용 시 주의가 필요한 연구이다.

## Related Papers

- 🔄 다른 접근: [[papers/186_Can_large_language_models_unlock_novel_scientific_research_i/review]] — 경제학 실험 예측과 일반적인 과학 아이디어 생성에서 LLM의 예측 능력을 다른 도메인에서 비교 검증할 수 있다.
- 🔗 후속 연구: [[papers/286_Domain-specific_ReAct_for_physics-integrated_iterative_model/review]] — 경제학에서의 실험 예측 방법론을 물리학 통합 모델링에 적용하여 도메인 간 방법론 전이 가능성을 탐구할 수 있다.
- ⚖️ 반론/비판: [[papers/820_Toward_Reliable_Scientific_Hypothesis_Generation_Evaluating/review]] — 실험 예측의 높은 정확도와 과학 가설 생성의 진실성 문제를 대조하여 LLM의 도메인별 신뢰성 차이를 분석할 수 있다.
- 🧪 응용 사례: [[papers/191_Causal_learning_for_socially_responsible_ai/review]] — 경제학 실험 예측 방법론을 사회적 책임 AI의 인과학습 도구 평가에 적용하여 편향성 완화 효과를 실증적으로 검증할 수 있다.
- 🧪 응용 사례: [[papers/558_Moose-chem3_Toward_experiment-guided_hypothesis_ranking_via/review]] — 시뮬레이션 기반 실험 설계를 실제 필드 실험 예측에 적용한 사례
