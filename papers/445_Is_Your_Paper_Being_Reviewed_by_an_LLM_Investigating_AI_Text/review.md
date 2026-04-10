---
title: "445_Is_Your_Paper_Being_Reviewed_by_an_LLM_Investigating_AI_Text"
authors:
  - "Sungduk Yu"
  - "Man Luo"
  - "Avinash Madasu"
  - "Vasudev Lal"
  - "Phillip Howard"
date: "2024.12"
doi: "10.48550/arXiv.2410.03019"
arxiv: ""
score: 4.0
essence: "학술 논문 심사 과정에서 LLM이 작성한 피어 리뷰(peer review)를 탐지하는 기존 방법들의 한계를 실증적으로 밝히고, 개별 리뷰 수준에서 AI 생성 텍스트를 탐지하는 새로운 앵커 임베딩(Anchor Embedding) 기반 접근법을 제안한다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/AI_Review_Detection"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Yu et al._2024_Is Your Paper Being Reviewed by an LLM Investigating AI Text Detectability in Peer Review.pdf"
---

# Is Your Paper Being Reviewed by an LLM? Investigating AI Text Detectability in Peer Review

> **저자**: Sungduk Yu, Man Luo, Avinash Madasu, Vasudev Lal, Phillip Howard | **날짜**: 2024-12-06 | **DOI**: [10.48550/arXiv.2410.03019](https://doi.org/10.48550/arXiv.2410.03019)

---

## Essence

![Figure 1](figures/fig1.webp)
*ICLR 학술대회에 제출된 리뷰 중 AI 생성 텍스트로 판정된 비율의 증가 추세(2019-2024)*

학술 논문 심사 과정에서 LLM이 작성한 피어 리뷰(peer review)를 탐지하는 기존 방법들의 한계를 실증적으로 밝히고, 개별 리뷰 수준에서 AI 생성 텍스트를 탐지하는 새로운 앵커 임베딩(Anchor Embedding) 기반 접근법을 제안한다.

## Motivation

- **Known**: 최근 LLM의 급속한 발전으로 과학 출판의 품질 보증 메커니즘인 피어 리뷰 과정이 침식될 수 있다는 우려가 제기되고 있으며, ICLR과 같은 주요 AI 학술대회에 제출된 리뷰 중 6.5~16.9%가 LLM을 실질적으로 활용했을 가능성이 지적되었다.

- **Gap**: 기존 연구는 코퍼스 수준(corpus-level)에서 AI 생성 텍스트의 존재 여부만 분석했을 뿐, 실제 심사 운영에 필수적인 **개별 리뷰 수준(individual review level)의 탐지 가능성**을 체계적으로 조사하지 못했다.

- **Why**: 부실한 심사자가 비윤리적으로 LLM을 은폐된 방식으로 활용하면 전문가 심사의 신뢰성이 훼손되고, 논문의 품질 관리 기능이 무너질 수 있기 때문에 신뢰할 만한 탐지 도구의 개발이 시급하다.

- **Approach**: ICLR 2021-2024 제출 논문에 대해 GPT-4o와 Llama-3.1 (70B)으로 생성한 AI 리뷰(16,000개)와 실제 인간 작성 리뷰를 비교하여, 기존 오픈소스 및 상용 탐지 모델들의 성능을 평가하고, 시맨틱 유사도 기반의 새로운 탐지 방법을 제안한다.

## Achievement

![Figure 2](figures/fig2.webp)
*ICLR 2022 논문의 GPT-4o 리뷰(좌)와 Llama-3.1 리뷰(우)에 대한 다양한 AI 텍스트 탐지 모델의 ROC 곡선*

1. **기존 방법의 한계 실증**: RoBERTa, Longformer 등 기존 지도학습 기반 분류기들과 Originality AI API는 거짓 양성(false positive) 비율이 높은 상태에서 GPT-4o 리뷰를 효과적으로 탐지하지 못함. 특히 FPR 0.05 수준에서 Originality AI API는 GPT-4o 리뷰의 58.56%만 탐지.

2. **새로운 앵커 임베딩 방법의 우수성**: 제안된 GPT-4o Anchor 및 Llama-3.1 Anchor 방식이 FPR 0.05 조건에서 GPT-4o 리뷰 97%와 95%를 각각 탐지하며, AUC 0.99를 달성하여 모든 기존 방법을 상회.

3. **LLM 판정자 분석**: GPT-4o를 판정자로 사용할 경우 80% 이상의 자신의 생성 리뷰를 탐지하지만 20%의 인간 리뷰를 거짓 양성으로 판정. 그 판단 근거는 반복성, 형식성, 일반적 비평 vs. 뉘앙스, 주관성, 구체성 등의 스타일 특성에 기반함.

## How

- **데이터 수집**: OpenReview API를 통해 ICLR 2019-2024 논문 및 리뷰 수집. 2021-2024년 500개 논문당 4가지 리뷰어 아키타입(균형잡힌, 까다로운, 혁신적, 보수적)별로 16,000개의 AI 생성 리뷰 생성.

- **프롬프트 설계**: ICLR 2022 심사자 가이드라인을 기반으로 한 체계화된 프롬프트 사용. 다양한 심사 스타일을 반영하는 4가지 아키타입 도입으로 현실성 강화.

- **탐지 방법 평가**: 
  - **오픈소스**: HC3 데이터로 학습한 RoBERTa, MAGE 벤치마크에서 입증된 Longformer
  - **상용 서비스**: Originality AI API
  - **LLM 기반**: GPT-4o 및 Llama-3.1을 판정자로 사용한 Chain-of-Thought 접근
  - **제안 방법**: 같은 논문에 대한 AI 생성 리뷰(Anchor)와의 코사인 유사도 비교

- **성능 지표**: 실제 운영에 실질적인 FPR (0.05, 0.20) 수준에서 진정 양성률(TPR) 측정. ROC-AUC로 임계값 변화에 따른 성능 추적.

## Originality

- **최초성**: 개별 리뷰 수준의 AI 탐지 가능성을 실증적으로 조사한 첫 연구. 기존 연구는 코퍼스 수준의 통계적 분석에만 머물렀음.

- **다각도 분석**: 5가지 이질적 탐지 방법(지도학습, 상용 API, LLM 판정자, 제안 방법)의 비교를 통해 각각의 장단점을 체계적으로 규명.

- **실무적 기여**: 기존 방법이 저 거짓 양성률 조건에서 GPT-4o 탐지에 실패하는 구체적 문제를 드러내고, 시맨틱 유사도 기반의 경량 대안 제시.

- **해석성 강화**: LLM 판정자의 판단 근거를 t-SNE 클러스터링으로 시각화하여 AI vs. 인간 리뷰의 스타일적 차이를 질적으로 규명.

## Limitation & Further Study

- **한계**: 
  - 연구 대상이 AI 학술대회(ICLR)에 국한되어 다른 분야의 피어 리뷰 특성(도메인별 용어, 필드 관행)을 반영하지 못함.
  - 생성 시에 사용된 프롬프트와 탐지 시 앵커 리뷰 생성 프롬프트가 상이하여, 공격자가 탐지를 우회하기 위해 프롬프트 최적화를 시도할 경우의 강건성 미검증.
  - 새로운 LLM 모델이나 고급 프롬프트 기법(예: 애드버서리얼 프롬프팅)에 대한 탐지 성능 평가 부재.
  - 앵커 임베딩 방법의 계산 비용 및 실시간 적용 가능성 미상세.

- **후속 연구**:
  - 적대적 설정(adversarial setting)에서 프롬프트 난독화(obfuscation) 기법에 강건한 탐지 알고리즘 개발.
  - 다양한 학문 분야(생명과학, 인문학 등)의 리뷰 데이터 수집 및 도메인 간 전이 성능 조사.
  - 탐지 우회 시도와 탐지 개선의 군비 경쟁(arms race)에 대비한 동적 탐지 체계 구축.
  - 블록체인 기반 리뷰 메타데이터 관리 또는 다중 심사자 필수화 등 제도적 보완 방안 연구.


## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 학술 심사의 AI 악용이라는 시의적절하고 중요한 문제를 개별 리뷰 수준에서 최초로 실증적으로 다룬 귀중한 연구다. 특히 기존 탐지 기법의 구체적인 한계(GPT-4o 탐지 불충분, 높은 거짓 양성률)를 드러내고 앵커 임베딩이라는 실용적 대안을 제시한 점이 강점이다. 다만 프롬프트 난독화나 다른 LLM 모델에 대한 강건성, 다양한 학문 분야로의 일반화 가능성, 그리고 탐지 회피 공격에 대한 방어 메커니즘 등에서 추가 연구가 필요하며, 제안 방법의 실무 수용성과 운영 비용 측면의 상세 분석도 향후 과제로 남아있다.

## Related Papers

- 🏛 기반 연구: [[papers/270_Detecting_llm-written_peer_reviews/review]] — LLM 작성 피어 리뷰 탐지의 기본 연구가 AI 텍스트 탐지 가능성 조사의 이론적 기반을 제공합니다.
- 🔄 다른 접근: [[papers/592_Openreviewer_A_specialized_large_language_model_for_generati/review]] — AI 생성 리뷰 탐지와 전문 AI 리뷰 생성이라는 상반된 관점에서 학술 심사의 AI 활용을 다룹니다.
- 🔗 후속 연구: [[papers/678_ReviewerGPT_An_Exploratory_Study_on_Using_Large_Language_Mod/review]] — 학술 리뷰에서 LLM 사용 탐색을 AI 텍스트 탐지 방법론 개발로 확장하여 더 정확한 식별 기술을 제시합니다.
- 🔄 다른 접근: [[papers/270_Detecting_llm-written_peer_reviews/review]] — 둘 다 학술 논문에서 AI 생성 텍스트를 탐지하는 문제를 다루지만 서로 다른 기술적 접근법을 사용함
- 🔄 다른 접근: [[papers/051_Admissions_in_the_age_of_AI_detecting_AI-generated_applicati/review]] — AI가 논문 심사에 사용되고 있는지 조사하는 다른 접근법으로 동일한 문제의식을 다른 각도에서 다룬다.
- 🔄 다른 접근: [[papers/592_Openreviewer_A_specialized_large_language_model_for_generati/review]] — AI 리뷰 생성과 AI 텍스트 탐지가 학술 심사에서 AI 활용의 상반된 두 관점을 제시합니다.
