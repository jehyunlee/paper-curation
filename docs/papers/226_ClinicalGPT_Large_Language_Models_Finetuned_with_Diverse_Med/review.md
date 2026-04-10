---
title: "226_ClinicalGPT_Large_Language_Models_Finetuned_with_Diverse_Med"
authors:
  - "Guangyu Wang"
  - "Guoxing Yang"
  - "Zongxin Du"
  - "Longjun Fan"
  - "Xiaohu Li"
date: "2023"
doi: "10.48550/arXiv.2306.09968"
arxiv: ""
score: 3.5
essence: "본 논문은 의료 도메인에 특화된 대규모 언어 모델 ClinicalGPT를 제시한다. 다양한 임상 데이터와 포괄적 평가 프레임워크를 활용하여 의료 분야의 고정확도, 해석성, 안전성 요구사항을 충족하도록 설계되었다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/AI_Drug_Discovery"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Wang et al._2023_ClinicalGPT Large Language Models Finetuned with Diverse Medical Data and Comprehensive Evaluation.pdf"
---

# ClinicalGPT: Large Language Models Finetuned with Diverse Medical Data and Comprehensive Evaluation

> **저자**: Guangyu Wang, Guoxing Yang, Zongxin Du, Longjun Fan, Xiaohu Li | **날짜**: 2023 | **DOI**: [10.48550/arXiv.2306.09968](https://doi.org/10.48550/arXiv.2306.09968)

---

## Essence

![Figure 1](figures/fig1.webp) 
*ClinicalGPT의 전체 구조: 다양한 의료 데이터와 감독 미세조정(SFT), 보상 모델(Reward Model), 강화학습(RL) 파이프라인을 통합*

본 논문은 의료 도메인에 특화된 대규모 언어 모델 ClinicalGPT를 제시한다. 다양한 임상 데이터와 포괄적 평가 프레임워크를 활용하여 의료 분야의 고정확도, 해석성, 안전성 요구사항을 충족하도록 설계되었다.

## Motivation

- **Known**: GPT-3, ChatGPT 등 대규모 사전학습 언어 모델은 NLP 작업에서 뛰어난 성능을 보이고 있으며, 의료 분야에 적용할 수 있는 잠재력이 있다.

- **Gap**: 그러나 일반 목적 LLM은 의료 응용에서 사실 부정확성(factual inaccuracies), 제한된 추론 능력, 실제 임상 경험 부재 등으로 인해 효과가 제한적이다. ChatGPT는 의료 전문성이 부족하고 과도하게 일반화된 답변을 생성한다.

- **Why**: 의료 분야는 높은 정확도, 해석성, 민감한 건강 데이터의 안전한 처리를 필수적으로 요구하므로, 도메인-특화 모델이 필요하다.

- **Approach**: 의료 기록, 의료 시험 문제, 다중 회차 의료 대화, 의료 지식 그래프 등 대규모 및 다양한 실제 의료 데이터로 미세조정하고, 감독 미세조정(SFT), 보상 모델 학습, 강화학습(RL) 파이프라인을 통해 임상 성능을 향상시킨다.

## Achievement

1. **다양한 의료 데이터셋 통합**: cMedQA2 (120k 질문), cMedQA-KG (100k Q&A 쌍), MEDQA-MCMLE (34k 의료 시험 문제), MedDialog (100k 학습 대화), MD-EHR (100k 전자의료기록)을 활용한 포괄적 학습 데이터 구성

2. **포괄적 평가 프레임워크**: 의료 지식 질답(QA), 의료 시험, 환자 상담, 의료 기록 진단 분석 등 4가지 임상 작업을 통해 모델 성능을 다각도로 검증

3. **감독 미세조정과 강화학습 조합**: 지식 그래프 기반 템플릿으로 생성된 prompt-response 쌍으로 SFT 수행 후, 인간 피드백 기반 보상 모델과 PPO(Proximal Policy Optimization)로 추가 최적화

4. **성능 향상**: ClinicalGPT가 기존 모델들(FlanPaLM 포함)을 모든 임상 작업에서 초과 성능 달성

## How

- **기본 모델**: BLOOM-7B를 베이스 모델로 선택 (오픈소스, 다국어 지원)

- **감독 미세조정(SFT)**: 
  - 의료 지식 그래프의 구조화된 삼중항(subject, relation, object)을 템플릿을 통해 질답 쌍으로 변환
  - 학습률 5e-5, 배치 크기 128, 최대 길이 1,024, 3 에포크로 학습

- **보상 모델(Reward Model)**:
  - 인간 평가자가 각 입력에 대해 선호 응답(Rw)과 비선호 응답(Rl) 비교 쌍 생성
  - 손실함수: -log(σ(rμ(I, Rw) - rμ(I, Rl)))로 순위 기반 학습
  - 학습률 2e-5, 3 에포크

- **강화학습(RL)**:
  - 보상함수: R(x,y) = rμ(x,y) - β log(πRL_φ(y|x)/πSFT(y|x))
  - PPO를 통해 최적화하며, KL 발산 페널티로 원본 모델로부터 과도한 편차 방지
  - 학습률 1e-5, 4000 스텝

- **효율성 최적화**: LoRA (Low-Rank Approximated adapter)를 활용한 매개변수 효율적 미세조정

## Originality

- **도메인-특화 데이터 통합**: 중국 의료 환경의 다양한 실제 임상 데이터(전자의료기록, 시험 문제, 대화 로그)를 체계적으로 수집하여 활용한 점

- **지식 그래프 활용**: 의료 지식 그래프의 구조화된 정보를 템플릿 기반 변환으로 학습 데이터로 활용하는 방식

- **포괄적 다중 작업 평가 프레임워크**: 의료 분야의 다양한 임상 시나리오(QA, 시험, 상담, 기록 분석)를 아우르는 체계적 평가 체계 구축

- **인간 피드백 기반 강화학습**: InstructGPT 방식을 의료 도메인에 적응시켜 인간 선호도를 직접 학습

## Limitation & Further Study

- **데이터 편향성**: 중국 의료 데이터에 중심화되어 있어 다른 언어권 및 의료 체계에 대한 일반화 가능성 제한 가능

- **평가 제한**: 인간 임상의의 성능과 직접 비교 부족 (FlanPaLM이 임상의에 비해 낮은 성능을 보였음을 언급하나, ClinicalGPT와의 비교 미상세)

- **확장성**: BLOOM-7B 기반으로 더 큰 모델 규모에서의 성능 검증 필요

- **안전성 및 윤리**: 의료 분야의 민감성에도 불구하고 모델의 할루시네이션(hallucination) 방지 메커니즘, 설명 가능성, 개인정보보호에 대한 상세 논의 부족

- **후속 연구**: (1) 다국어 및 다중 의료 체계 데이터 확대, (2) 임상의 레벨의 성능 달성을 위한 추가 최적화, (3) 실제 임상 환경 도입 전 규제 요구사항 충족 방안 연구

## Evaluation

- **Novelty (독창성)**: 3.5/5
  - 의료 도메인 적용은 시의적절하나, 기술적 기법 자체(SFT+RM+PPO)는 InstructGPT를 따른 것이며 주로 데이터 수집과 평가 프레임워크에서 기여

- **Technical Soundness (기술적 타당성)**: 3.5/5
  - SFT, 보상 모델, PPO 적용이 표준적이고 명확하나, 구현 세부사항 부족 (배치 정규화, 수렴성 분석 등). 기저 모델 선택 근거 제한적

- **Significance (중요성)**: 4/5
  - 의료 AI의 실질적 필요성이 높고, 포괄적 평가 프레임워크 제시는 이후 의료 LLM 연구의 벤치마크 역할 가능. 다만 임상 배포까지의 경로가 모호함

- **Clarity (명확성)**: 3.5/5
  - 전체 구조는 명확하나, 데이터셋 분할 비율의 일관성 부족 (cMedQA2는 10k/4k 어노테이션, MedDialog는 100k/1k/1k로 매우 불균형). 결과 섹션이 제시문에 완전히 포함되지 않아 정량적 성능 지표 판단 불가

- **Overall (종합)**: 3.5/5

**총평**: ClinicalGPT는 의료 도메인에 특화된 LLM 개발의 실용적 접근을 보여주며 다양한 임상 데이터 통합과 포괄적 평가 프레임워크가 주요 기여이나, 기술적 혁신성이 제한적이고 실제 임상 성능 검증 및 실무 적용 경로에 대한 논의가 부족하다.

## Related Papers

- 🔄 다른 접근: [[papers/168_Biomni_A_General-Purpose_Biomedical_AI_Agent/review]] — 의료 특화 대규모 언어모델의 두 가지 다른 설계 철학을 비교하여 의료 AI의 범용성과 특화성 간의 균형점을 찾을 수 있다.
- 🔗 후속 연구: [[papers/530_Medbiolm_Optimizing_medical_and_biological_qa_with_fine-tune/review]] — ClinicalGPT의 의료 데이터 활용 방법론을 생물의학 QA 최적화로 확장하여 더 정밀한 의료 언어모델을 구축할 수 있다.
- 🏛 기반 연구: [[papers/271_Developing_ChemDFM_as_a_large_language_foundation_model_for/review]] — 화학 분야 대형 언어 기초 모델 개발 경험이 의료 분야 특화 모델 구축에 필요한 도메인 적응 전략을 제공한다.
- 🏛 기반 연구: [[papers/159_Bio-sieve_exploring_instruction_tuning_large_language_models/review]] — 다양한 의료 텍스트로 미세조정된 ClinicalGPT가 의료 특화 모델의 기반
- 🏛 기반 연구: [[papers/225_Clinicalgpt-r1_Pushing_reasoning_capability_of_generalist_di/review]] — ClinicalGPT의 기본 의료 언어모델 구조가 추론 능력 강화를 위한 ClinicalGPT-R1의 기술적 기반을 제공한다.
