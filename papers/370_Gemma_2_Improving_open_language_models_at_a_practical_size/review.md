---
title: "370_Gemma_2_Improving_open_language_models_at_a_practical_size"
authors:
  - "Gemma Team Morgane Riviere"
  - "Shreya Pathak"
  - "Pier Giuseppe Sessa"
  - "Cassidy Hardin"
  - "Surya Bhupatiraju"
date: "2024"
doi: "-"
arxiv: ""
score: 4.25
essence: "Google DeepMind이 공개한 Gemma 2는 2B, 9B, 27B 매개변수 규모의 경량 오픈 언어모델 계열로, 지식 증류(Knowledge Distillation) 기반 학습과 Transformer 아키텍처 개선을 통해 같은 규모 모델 대비 최고 성능을 달성하고 2-3배 큰 모델과 경쟁 가능한 수준의 성능을 제공한다."
tags:
  - "cat/Scientific_Language_Processing_and_Visualization"
  - "sub/Scientific_Language_Models"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Riviere et al._2024_Gemma 2 Improving open language models at a practical size.pdf"
---

# Gemma 2: Improving open language models at a practical size

> **저자**: Gemma Team Morgane Riviere, Shreya Pathak, Pier Giuseppe Sessa, Cassidy Hardin, Surya Bhupatiraju, L'eonard Hussenot, Thomas Mesnard, Bobak Shahriari, Alexandre Ramé, Johan Ferret, Peter Liu, P. Tafti, Abe Friesen, Michelle Casbon, Sabela Ramos, Ravin Kumar, Charline Le Lan, Sammy Jerome, Anton Tsitsulin, Nino Vieillard | **날짜**: 2024 | **DOI**: -

---

## Essence

Google DeepMind이 공개한 Gemma 2는 2B, 9B, 27B 매개변수 규모의 경량 오픈 언어모델 계열로, 지식 증류(Knowledge Distillation) 기반 학습과 Transformer 아키텍처 개선을 통해 같은 규모 모델 대비 최고 성능을 달성하고 2-3배 큰 모델과 경쟁 가능한 수준의 성능을 제공한다.

## Motivation

- **Known**: 대형 언어모델(LLM)은 스케일 증가로 인한 성능 향상이 증명되었으나, 소규모 모델은 학습 토큰 수 증가로만 성능 개선이 가능하며 이는 데이터셋 크기에 로그스케일로만 확장된다.

- **Gap**: 최신 소규모 모델들도 여전히 과소 학습(under-trained) 상태이며, 단순히 학습 길이를 늘리는 방식은 한계가 있다. 컴퓨팅 최적 토큰 수의 50배 이상을 학습해야 1-2% 성능 향상만 가능하다.

- **Why**: 각 학습 단계에서 네트워크가 받는 정보의 질을 개선하여 소규모 모델의 성능 향상을 달성할 필요가 있다.

- **Approach**: (1) 지식 증류(Knowledge Distillation)로 대규모 교사 모델의 토큰 분포 정보를 전달하여 더 풍부한 그래디언트 제공, (2) 로컬-글로벌 주의 메커니즘(Local-Global Attention) 교차 배치, (3) 그룹 쿼리 주의(Grouped-Query Attention) 적용

## Achievement

| 모델 | 매개변수 | 학습 토큰 | 주요 특징 |
|------|--------|---------|---------|
| 2B | 2.6B | 2T | 지식 증류 적용 |
| 9B | 9.2B | 8T | 지식 증류 적용 |
| 27B | 27.2B | 13T | 처음부터 학습 |

1. **소규모 모델 성능 혁신**: 2B 모델이 500B 토큰으로 지식 증류 학습 시 처음부터 학습한 모델 대비 평균 3개 벤치마크에서 60.3 → 67.7로 향상(표 6)

2. **규모 대비 경쟁력**: 같은 크기 오픈 모델 대비 최고 성능 달성, 2-3배 큰 모델들과 경쟁 가능한 수준의 성능 제시 (질문 답변, 상식 추론, 수학, 코딩 등 다양한 도메인)

3. **효율적 추론**: GQA(Grouped-Query Attention)와 슬라이딩 윈도우 주의로 추론 속도 향상

## How

**아키텍처 혁신**:
- **로컬-글로벌 주의 교차배치**: 짝수 레이어에서 슬라이딩 윈도우(4096 토큰), 홀수 레이어에서 전역 주의(8192 토큰) 교차 적용으로 계산 효율과 모델링 능력의 균형 달성
- **Logit Soft-Capping**: 주의층과 최종층의 로짓을 tanh 함수로 상한(-soft_cap~+soft_cap) 설정하여 학습 안정성 향상 (soft_cap: 50.0/30.0)
- **그룹 쿼리 주의(GQA)**: num_groups=2로 설정하여 메모리 효율 개선 및 추론 속도 향상

**학습 방법**:
- **지식 증류**: 교사 모델의 토큰 조건부 확률 P_T(x|x_c)와 학생 모델의 P_S(x|x_c) 간 KL 발산 최소화
- **감독 미세조정(SFT)**: 합성 및 실제 프롬프트로 행동 복제 + 교사 모델 증류
- **강화학습 인간 피드백(RLHF)**: 개선된 보상 모델(대화 능력 중심) 적용
- **모델 병합(Model Merging)**: 다양한 하이퍼파라미터로 학습한 모델들의 가중 평균화로 전반 성능 개선

**학습 데이터**:
- 27B: 13T 토큰, 9B: 8T 토큰, 2B: 2T 토큰 (웹 문서, 코드, 과학 논문)
- SentencePiece 토크나이저 (256k 어휘)
- 개인정보 제거, 안전성 필터링, 평가셋 오염 제거, 민감 출력 최소화

## Originality

- **지식 증류의 새로운 활용**: 학습 시간 단축이 아닌 **컴퓨팅 최적값의 50배 토큰으로 학습**하여 소규모 모델을 "과도 학습"시키는 혁신적 접근 방식

- **아키텍처 조합의 실용성**: 기존 기법들(Longformer의 로컬-글로벌 주의, GQA)을 소규모 모델에 체계적으로 적용하여 실증

- **공개 모델로서의 가치**: 모든 모델 가중치를 커뮤니티에 공개하여 접근성 제고

- **포괄적 평가**: 자동화 벤치마크(QA, 추론, 수학, 코딩) + 인간 평가 포함한 다층적 검증

## Limitation & Further Study

- **데이터 한정성**: 영어 중심 학습으로 다국어 능력이 제한적, 멀티모달 기능 미지원

- **교사 모델 의존성**: 지식 증류 성능이 교사 모델 품질에 의존하며, 교사 모델 선정 기준의 상세 분석 부족

- **안전성 평가 한계**: 광범위한 필터링에도 불구하고 모든 적용 시나리오에서의 안전성 보장 불가능 → 사용자 맞춤형 안전 테스트 강조

- **메모리 효율 추가 최적화**: 슬라이딩 윈도우 주의로 메모리 절약이 있으나, 매우 제한된 환경에서의 추가 최적화 방안 미제시

- **후속 연구 방향**: 
  - 더 큰 규모의 교사 모델에서의 증류 효과 분석
  - 다국어 및 멀티모달 확장
  - 극저자원 환경(모바일 등)에서의 성능 특성 연구

## Evaluation

- **Novelty**: 4/5
  - 지식 증류의 과도 학습 활용은 혁신적이나, 개별 아키텍처 요소는 기존 기법 조합

- **Technical Soundness**: 4.5/5
  - 체계적인 아키텍처 설계 및 광범위한 실험 기반이나, 일부 하이퍼파라미터 선택의 정당성 분석 부족

- **Significance**: 4.5/5
  - 소규모 오픈 모델의 실용적 성능 향상으로 높은 영향력, 커뮤니티 기여도 높음

- **Clarity**: 4/5
  - 구체적 수치와 표로 명확하나, 일부 모델 병합 등 후처리 단계의 상세 설명 필요

- **Overall**: 4.25/5

**총평**: Gemma 2는 지식 증류를 활용한 소규모 모델 성능 개선의 실증적 성공 사례로, 경량 모델의 실용적 가치를 극대화한 의미 있는 기여다. 다만 다국어/멀티모달 확장과 교사 모델 선정 기준의 깊이 있는 분석이 추가되면 더욱 강화될 것으로 예상된다.

## Related Papers

- ⚖️ 반론/비판: [[papers/266_Deepseek-v3_technical_report/review]] — DeepSeek-V3의 대규모 MoE와 달리 Gemma 2는 소형 모델의 효율성과 실용성 강조
- 🔄 다른 접근: [[papers/387_Gpt-4_technical_report/review]] — GPT-4와 경쟁할 수 있는 성능을 훨씬 작은 모델 크기로 달성하는 다른 접근법
- 🔄 다른 접근: [[papers/617_Phi-4_technical_report/review]] — Phi-4와 함께 경량 고성능 모델의 대표적 사례로 서로 다른 최적화 전략 제시
- 🔄 다른 접근: [[papers/801_The_llama_3_herd_of_models/review]] — Llama 3와 유사한 성능을 지식 증류 기반으로 더 작은 크기로 달성
- ⚖️ 반론/비판: [[papers/266_Deepseek-v3_technical_report/review]] — DeepSeek-V3의 대규모 MoE 접근법과 달리 Gemma 2는 경량화된 효율적 모델에 집중
- 🏛 기반 연구: [[papers/649_Qwen25_technical_report/review]] — Google의 Gemma 2 모델이 실용적 규모에서 오픈 언어 모델을 개선하는 방법을 제시하여 Qwen2.5의 성능 향상 기법과 비교할 수 있는 기준을 제공한다.
