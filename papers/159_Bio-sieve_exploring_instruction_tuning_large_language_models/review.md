---
title: "159_Bio-sieve_exploring_instruction_tuning_large_language_models"
authors:
  - "Ambrose Robinson"
  - "William Thorne"
  - "Ben Wu"
  - "Abdullah Pandor"
  - "Munira Essat"
date: "2023"
doi: "arXiv:2308.06610"
arxiv: ""
score: 4.0
essence: "본 논문은 의료 체계적 문헌고찰의 가장 비용 집약적인 단계인 초록 스크리닝을 자동화하기 위해 지시어 미세조정(instruction tuning)을 통해 대규모언어모델(LLM)을 특화시킨 Bio-SIEVE를 제시한다. 이 모델은 ChatGPT를 능가하는 성능을 보이면서도 의료 영역 간 우수한 일반화 능력을 갖춘다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/Biomedical_Causal_Modeling"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Luo et al._2023_Bio-sieve exploring instruction tuning large language models for systematic review automation.pdf"
---

# Bio-SIEVE: Exploring Instruction Tuning Large Language Models for Systematic Review Automation

> **저자**: Ambrose Robinson, William Thorne, Ben Wu, Abdullah Pandor, Munira Essat, Mark Stevenson, Xingyi Song (The University of Sheffield) | **날짜**: 2023 | **DOI**: [arXiv:2308.06610](https://arxiv.org/abs/2308.06610)

---

## Essence

![Figure 1](figures/fig1.webp)
*의료 체계적 문헌고찰(Systematic Review) 프로세스에서 Bio-SIEVE가 지원하는 제목 및 초록 스크리닝 단계*

본 논문은 의료 체계적 문헌고찰의 가장 비용 집약적인 단계인 초록 스크리닝을 자동화하기 위해 지시어 미세조정(instruction tuning)을 통해 대규모언어모델(LLM)을 특화시킨 Bio-SIEVE를 제시한다. 이 모델은 ChatGPT를 능가하는 성능을 보이면서도 의료 영역 간 우수한 일반화 능력을 갖춘다.

## Motivation

- **Known**: 체계적 문헌고찰은 의료 분야에서 근거기반 의사결정을 위해 필수적이나, 평균 비용이 $141,194이고 완성까지 1.72년이 소요되는 매우 고비용 프로세스이다. 기존 활성학습(active learning) 기반 자동화 방식은 일반적이지만 충분한 중단 기준이 부족하고 만족할 만한 성능 달성까지 광범위한 스크리닝이 필요하다.

- **Gap**: BERT, T5 등 기존 언어모델은 입력 크기 제한과 낮은 영점샷(zero-shot) 성능의 한계가 있었다. ChatGPT는 희망적이지만 재현성 부족, 검은상자 특성, 명확하지 않은 계산 비용이 문제다. 또한 기존 연구는 단순한 주제나 단일 선택 기준만 다루었으며, 배제 이유 자동화는 미탐색 영역이다.

- **Why**: 특화된 소형 언어모델이 필요하며, 이는 재현성을 보장하고 계산 효율성을 제공하면서도 의료 도메인에 최적화될 수 있다.

- **Approach**: Cochrane Review 지식베이스를 활용하여 LLaMA와 Guanaco 모델에 지시어 미세조정을 적용하고, 다중작업(multi-task) 학습(PICO 추출, 배제 이유 생성)의 효과를 검증한다.

## Achievement

![Figure 2](figures/fig2.webp)
*학습 데이터셋의 포함/배제 분류에 따른 주제 분포*

1. **우수한 분류 성능**: Bio-SIEVE는 ChatGPT와 기존 학습 기반 접근법을 모두 능가하며, 특히 배제 사례에서 높은 정확도를 달성한다(예: 구강 건강 리뷰에서 근육 외상 연구 성공적 배제).

2. **도메인 간 일반화**: 여러 의료 영역에 걸쳐 더 나은 일반화 성능을 보여, 미학습 체계적 문헌고찰에 대한 적용 가능성을 입증한다.

3. **설명 가능성**: 배제 이유 자동 생성 기능으로 모델의 의사결정 과정에 대한 투명성을 제공하여 질적 검증 메커니즘으로 활용 가능하다.

4. **재현성과 투명성**: 모델 가중치, 코드, 데이터셋 재구성을 위한 DOI 목록을 공개하여 완전한 재현성을 보장한다.

## How

![Figure 3](figures/fig3.webp)
*지시어 미세조정에 사용된 Cochrane 샘플의 예시*

- **데이터**: Cochrane Review 데이터베이스의 확장 가능한 지식베이스를 활용하여 초록-포함/배제 쌍을 구성

- **기본 모델**: LLaMA(7B, 13B, 65B)와 Guanaco(지시어 미세조정 전처리된 LLaMA) 기반으로 시작

- **미세조정 전략**: 지시어 형식의 자연언어 프롬프트를 통한 작업 기반 미세조정 적용

- **다중작업 학습**: PICO(Population, Intervention, Comparison, Outcome) 추출과 배제 이유 생성을 포함한 다중작업 학습 설정 실험

- **정량적 평가**: F1-스코어, 민감도(recall), 특이도(precision) 등 다양한 메트릭으로 ChatGPT 및 전통적 방법과 비교 평가

- **절제 연구(Ablation Study)**: 서로 다른 지시어 미세조정 방식의 효과 검증 및 멀티태스크 전이학습의 유용성 평가

## Originality

- **특화된 도메인 모델**: 체계적 문헌고찰 전용 LLM 개발로, 일반용도 모델의 한계를 극복한 첫 시도

- **다양한 선택 기준 처리**: 임의적 선택 기준과 목표를 고려한 더 도전적인 필터링 작업 설정 (기존: 단순 주제 또는 단일 기준)

- **배제 이유 생성 작업**: 배제 논거(exclusion reasoning)를 자동화하는 새로운 과제 도입으로 설명 가능성 강화

- **다중 기본 모델 비교**: LLaMA와 Guanaco 기반 모델의 성능 차이 분석 및 지시어 미세조정 전처리의 효과 입증

- **투명한 재현성**: 폐쇄 모델(ChatGPT) 대비 완전 공개 자원(모델, 코드, 데이터) 제공으로 학술적 재현성 극대화

## Limitation & Further Study

- **안전성-우선(Safety-First) 적응**: 다중 검토자의 독립적 스크리닝이 필요한 안전-우선 시나리오에 대한 모델 적응 과제 미해결

- **다중작업 학습의 한계**: Bio-SIEVE-Multi는 포함 이유(inclusion reasoning)에서 일부 성과를 보였으나 ChatGPT 수준의 선호도 순위 성능 미달성

- **맥락 길이 제약**: 초록 스크리닝만 다루었으며, 전체 텍스트(full-text) 스크리닝을 위해서는 더 긴 맥락 길이 모델 필요

- **후속 연구**: 생성형 접근법으로의 확장, 데이터 추출 단계 자동화, 실시간 품질 평가 메커니즘 통합 등이 가능

- **임상 적용 검증**: 실제 체계적 문헌고찰 프로젝트에서의 성능 검증 및 임상가-AI 협력 워크플로우 개발 필요

## Evaluation

- **Novelty**: 4/5 – 체계적 문헌고찰 특화 모델 및 배제 이유 생성 작업은 신규이나, 지시어 미세조정 기법 자체는 기존 연구 활용

- **Technical Soundness**: 4/5 – 견고한 실험 설계와 다중 평가 메트릭이나, 다중작업 학습의 제한적 성과에 대한 더 깊은 분석 필요

- **Significance**: 4/5 – 의료 문헌고찰의 고비용 문제 해결에 상당한 실용적 가치를 지니며, 도메인 특화 LLM의 가능성을 시연

- **Clarity**: 4/5 – 전반적으로 명확한 구성이나, 다중작업 학습 실패 원인에 대한 상세 논의 부족

- **Overall**: 4/5

**총평**: Bio-SIEVE는 체계적 문헌고찰 자동화에 특화된 LLM을 제시함으로써 고가의 의료 리뷰 프로세스 개선에 유의미한 기여를 한다. 재현 가능한 공개 모델 공급과 배제 이유 생성이라는 새로운 과제 도입은 이 연구의 강점이나, 실제 임상 환경에서의 검증과 다중작업 학습 성능 개선이 향후 필수 과제이다.

## Related Papers

- 🧪 응용 사례: [[papers/244_Cross_sectional_pilot_study_on_clinical_review_generation_us/review]] — 임상 리뷰 생성을 위한 파일럿 연구에서 의료 문헌고찰 자동화로의 적용
- 🔗 후속 연구: [[papers/507_Llmeval-med_A_real-world_clinical_benchmark_for_medical_llms/review]] — 의료 LLM 실제 임상 벤치마크에서 체계적 문헌고찰로의 확장
- 🔄 다른 접근: [[papers/328_Explainable_biomedical_claim_verification_with_large_languag/review]] — 생명의학 주장 검증과 초록 스크리닝 자동화의 다른 의료 AI 접근법
- 🏛 기반 연구: [[papers/226_ClinicalGPT_Large_Language_Models_Finetuned_with_Diverse_Med/review]] — 다양한 의료 텍스트로 미세조정된 ClinicalGPT가 의료 특화 모델의 기반
- 🏛 기반 연구: [[papers/169_Bioprobench_Comprehensive_dataset_and_benchmark_in_biologica/review]] — 생의학 분야 LLM 지시 튜닝이 생물학적 프로토콜 이해의 기반을 제공한다
- 🧪 응용 사례: [[papers/371_GeneAgent_self-verification_language_agent_for_gene-set_anal/review]] — 자기검증 기법을 생명정보학 분야에 적용한 구체적 사례로서 Bio-SIEVE와 상호 보완적인 접근을 보여준다.
- 🏛 기반 연구: [[papers/144_AutoProteinEngine_A_Large_Language_Model_Driven_Agent_Framew/review]] — 생물정보학 분야를 위한 대규모 언어 모델 조정 방법론이 AutoProteinEngine의 생물학자 친화적 자연언어 인터페이스 구현의 기반이다.
