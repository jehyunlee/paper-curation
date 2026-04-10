---
title: "128_Automatically_evaluating_the_paper_reviewing_capability_of_l"
authors:
  - "Hyungyu Shin"
  - "Jingyu Tang"
  - "Yoonjoo Lee"
  - "Nayoung Kim"
  - "Hyunseung Lim"
date: "2025"
doi: "arXiv:2502.17086"
arxiv: ""
score: 4.2
essence: "본 논문은 LLM이 생성한 학술지 리뷰의 신뢰성을 평가하기 위해 **포커스 레벨 평가 프레임워크**를 제안한다. 기존 표면적/내용적 평가와 달리, 리뷰가 문제점(problem), 방법(method), 실험(experiment) 등 다양한 측면을 얼마나 균형있게 다루는지를 분석하여 LLM 리뷰의 맹점(blind spots)을 체계적으로 드러낸다."
tags:
  - "cat/Cognitive_AI_Evaluation_and_Benchmarking"
  - "sub/Cognitive_LLM_Evaluation"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Ouzzani et al._2025_Automatically evaluating the paper reviewing capability of large language models.pdf"
---

# Automatically evaluating the paper reviewing capability of large language models

> **저자**: Hyungyu Shin, Jingyu Tang, Yoonjoo Lee, Nayoung Kim, Hyunseung Lim, Ji Yong Cho, Hwajung Hong, Moontae Lee, Juho Kim | **날짜**: 2025 | **DOI**: [arXiv:2502.17086](https://arxiv.org/abs/2502.17086)

---

## Essence

![Figure 1](figures/fig1.webp) 
*그림 1: LLM 리뷰 평가를 위한 포커스 레벨 평가 프레임워크. 사전정의된 패싯(facet)을 기반으로 포커스 분포를 계산하고 인간 리뷰어와 비교*

본 논문은 LLM이 생성한 학술지 리뷰의 신뢰성을 평가하기 위해 **포커스 레벨 평가 프레임워크**를 제안한다. 기존 표면적/내용적 평가와 달리, 리뷰가 문제점(problem), 방법(method), 실험(experiment) 등 다양한 측면을 얼마나 균형있게 다루는지를 분석하여 LLM 리뷰의 맹점(blind spots)을 체계적으로 드러낸다.

## Motivation

- **Known**: 기존 LLM 리뷰 평가는 표면적 유사도(BLEU, ROUGE)나 내용 수준(구체성, 사실 정확성) 또는 의사결정 수준(수용/거절 분류)에만 초점을 맞춤
- **Gap**: LLM 리뷰가 인간 전문가들이 중요하게 여기는 **핵심 패싯들(논문의 참신성, 명확성, 유효성 등)에 균형있게 주의를 기울이는지 여부를 체계적으로 평가하는 방법이 부재**
- **Why**: 기술적 타당성에만 집중하면서 참신성을 완전히 무시하는 리뷰처럼, 포커스가 편향된 리뷰는 정확하고 구체적이어도 의미있는 피드백을 제공하지 못하며 주니어 리뷰어들에게 불완전한 관점을 강화할 수 있음
- **Approach**: ICLR 2021-2024 OpenReview 데이터의 676개 논문과 3,657개 강점/약점 주석으로부터 자동 포커스 분포 계산 파이프라인 개발 및 8개 LLM 평가

## Achievement

![Figure 2](figures/fig1.webp)
*그림 2: 자동화된 포커스 레벨 평가 프로세스. 메타리뷰에서 강점/약점 추출 → 자동 annotator로 target/aspect 레이블링 → 포커스 분포 계산*

1. **LLM 리뷰의 구조적 맹점 규명**: 모든 오프더셀프 LLM이 기술적 타당성(validity) 검토에 편향되어 있으면서 참신성(novelty) 평가를 현저히 간과하는 일관된 패턴 발견

2. **자동 평가 파이프라인 개발**: Target 패싯 7개(문제, 방법, 이론, 실험, 결론, 논문, 선행연구)와 Aspect 패싯 5개(타당성, 명확성, 참신성, 영향, 실현가능성)를 정의하여 코헨의 카파 0.81(target), 0.79(aspect)의 실질적 일치도 달성

3. **세분화된 평가 결과**: 
   - 최고 성능 모델도 인간 리뷰어와 target/aspect 매칭에서 F1 스코어 0.373에 불과
   - 미세조정(fine-tuning) gpt-4o 모델이 포커스 분포에서 인간과 가장 유사
   - Llama-405B는 텍스트 유사도에서 최고 성능 (다차원 평가의 중요성 시사)

4. **대규모 벤치마크 데이터셋 공개**: 676개 논문, 전문가 리뷰, 8개 LLM의 43,042개 강점/약점 자동 주석 데이터 공개로 재현성 및 향후 연구 기반 제공

## How

![Figure 4](figures/fig1.webp)
*그림 4: Target/Aspect별 강점/약점의 포커스 분포 시각화. 인간과 LLM의 분포 비교*

- **포커스 정의**: 리뷰의 포커스를 사전정의된 패싯 집합 A에 대한 정규화된 주의 분포로 정의. 강점(F+) 및 약점(F-)에 대해 각각 계산

- **데이터 구축**: 
  - OpenReview에서 ICLR 2021-2024의 18,407개 제출 논문 수집
  - 메타리뷰 자동 추출 + 개별 리뷰어 의견으로 증강하여 자체 포함적(self-contained) 강점/약점 생성
  - 3단계 프롬프트 체인으로 추출 작업 자동화

- **Facet 정의**: 9개 AI 컨퍼런스 투고 가이드라인과 선행 문헌 분석을 통해 target-aspect 쌍 추출

- **자동 Annotator 개발**: LLM 기반 자동 분류기로 각 강점/약점에 target과 aspect 레이블 할당 (상당한 일치도 달성)

- **포커스 분포 비교**: 
  - 정규화된 빈도 계산으로 인간과 LLM의 포커스 분포 구성
  - KL 발산, 지구 이동 거리(Earth Mover's Distance) 등으로 분포 간 거리 측정

## Originality

- **혁신적 평가 관점**: 기존의 표면적·내용적·의사결정 수준 평가를 넘어 **포커스 레벨이라는 새로운 평가 차원** 도입으로 리뷰의 다차원적 균형성 평가

- **구조화된 패싯 체계**: 9개 컨퍼런스 가이드라인과 문헌 기반의 체계적인 target-aspect 패싯 정의로 분석의 신뢰성 강화

- **자동화와 확장성**: 완전 자동화된 평가 파이프라인으로 다양한 LLM과 도메인에 확장 가능하도록 설계

- **포괄적 실증 분석**: GPT(4o, 4-turbo, 3.5), Llama(405B, 70B), DeepSeek 등 8개 LLM 평가로 다양한 모델족 간 패턴 비교 가능

- **대규모 공개 데이터셋**: 676개 논문의 3,657개(인간) + 43,042개(LLM) 강점/약점 주석 데이터 공개로 재현성 및 커뮤니티 기여

## Limitation & Further Study

- **Facet 정의의 한계**: AI 컨퍼런스에 중심화되어 있어 다른 학문 분야(의학, 물리학 등)의 리뷰 특성 반영 부족 가능성

- **추출 파이프라인 오류**: 메타리뷰 + 개별 리뷰 증강 과정에서 중복이나 누락 발생 가능성, 자동 annotator의 0.81/0.79 코헨 카파는 완벽하지 않음

- **인과성 규명 부족**: LLM의 포커스 편향이 발생하는 근본 원인(학습 데이터 편향, 아키텍처 특성, 프롬프팅 방식 등)에 대한 심층 분석 미흡

- **평가-개선 피드백 루프 부족**: 포커스 분포 차이를 발견했으나, 이를 바탕으로 LLM을 개선하는 구체적 방법론(지도(supervision), 강화학습 등)의 효과 검증 제한적

- **후속 연구 방향**:
  - 다른 학문 분야와 컨퍼런스로 프레임워크 확장
  - 포커스 편향 원인 분석 및 완화 전략 개발
  - 인간 리뷰어가 LLM 리뷰를 효과적으로 활용하는 방법 연구
  - 포커스 분포 개선을 위한 미세조정 및 프롬프팅 기법 개발

## Evaluation

- **Novelty**: 4.5/5  
  포커스 레벨 평가라는 새로운 차원을 도입한 점은 혁신적이나, 리뷰 분석 자체는 기존 연구(facet 분석)의 확장

- **Technical Soundness**: 4/5  
  자동 annotator 개발, 대규모 데이터셋 구축, 8개 LLM 평가까지 기술적으로 견고하나, 추출 파이프라인의 오류 가능성과 완벽하지 않은 annotator 성능

- **Significance**: 4.5/5  
  LLM 리뷰의 구조적 맹점(참신성 간과, 기술적 타당성 편향)을 규명함으로써 인간이 LLM 리뷰를 더 효과적으로 활용하도록 가이드할 수 있으나, 개선 방법론이 부족함

- **Clarity**: 4/5  
  프레임워크 정의, 파이프라인 설명이 명확하나, Facet 선정 기준 상세화 및 일부 기술적 세부사항 부재

- **Overall**: 4.2/5

**총평**: 본 논문은 LLM 생성 리뷰의 평가에 새로운 관점(포커스 레벨)을 도입하여 기존 평가의 맹점을 보완하고, 대규모 벤치마크 데이터셋을 공개함으로써 학술 출판의 질 향상에 실질적 기여를 한다. 다만 원인 규명과 개선 방법론이 후속 연구로 남겨있으며, 다른 분야로의 확장성 검증이 필요하다.

## Related Papers

- 🔄 다른 접근: [[papers/537_Mind_the_blind_spots_A_focus-level_evaluation_framework_for/review]] — 동일한 포커스 레벨 평가 프레임워크를 다른 관점에서 접근함
- 🧪 응용 사례: [[papers/678_ReviewerGPT_An_Exploratory_Study_on_Using_Large_Language_Mod/review]] — LLM 기반 피어 리뷰 탐색의 구체적 실증 연구 사례
- 🔗 후속 연구: [[papers/507_Llmeval-med_A_real-world_clinical_benchmark_for_medical_llms/review]] — LLM의 논문 리뷰 능력 평가 방법론을 의료 도메인에 적용하여 전문가 검증의 중요성을 입증한다.
- 🔗 후속 연구: [[papers/537_Mind_the_blind_spots_A_focus-level_evaluation_framework_for/review]] — 논문 리뷰 능력의 자동 평가는 LLM 리뷰의 맹점을 정량화하는 포커스 레벨 평가의 확장된 응용입니다
- 🏛 기반 연구: [[papers/237_Confidence_in_Large_Language_Model_Evaluation_A_Bayesian_App/review]] — LLM 리뷰 능력 자동 평가가 베이지안 신뢰도 평가의 구체적 적용 사례
- 🔗 후속 연구: [[papers/905_If_in_a_Crowdsourced_Data_Annotation_Pipeline_a_GPT-4__Proce/review]] — LLM의 논문 리뷰 능력 자동 평가 프레임워크가 GPT-4와 크라우드소싱 데이터 라벨링 품질 비교 연구에 적용될 수 있다.
