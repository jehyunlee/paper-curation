---
title: "184_Can_large_language_models_provide_useful_feedback_on_researc"
authors:
  - "Weixin Liang"
  - "Yuhui Zhang"
  - "Hancheng Cao"
  - "Binglu Wang"
  - "Daisy Ding"
date: "2023.10"
doi: "10.48550/arXiv.2310.01783"
arxiv: ""
score: 4.5
essence: "본 논문은 GPT-4를 활용한 대규모 실증 분석을 통해 LLM이 학술 논문에 대해 유용한 피드백을 제공할 수 있는지 체계적으로 평가한 첫 번째 연구이다. Nature 저널 3,096편과 ICLR 1,709편의 논문을 분석한 결과, GPT-4의 피드백이 인간 리뷰어들의 의견과 비슷한 수준의 일치도를 보였으며, 308명의 연구자 설문 조사에서 57.4%가 유용하다고 평가했다."
tags:
  - "cat/LLM-Based_Scientific_Reasoning"
  - "sub/Scientific_Literature_Analysis"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Liang et al._2023_Can large language models provide useful feedback on research papers A large-scale empirical analys.pdf"
---

# Can large language models provide useful feedback on research papers? A large-scale empirical analysis

> **저자**: Weixin Liang, Yuhui Zhang, Hancheng Cao, Binglu Wang, Daisy Ding, Xinyu Yang, Kailas Vodrahalli, Siyu He, Daniel Smith, Yian Yin, Daniel McFarland, James Zou | **날짜**: 2023-10-03 | **DOI**: [10.48550/arXiv.2310.01783](https://doi.org/10.48550/arXiv.2310.01783)

---

## Essence

본 논문은 GPT-4를 활용한 대규모 실증 분석을 통해 LLM이 학술 논문에 대해 유용한 피드백을 제공할 수 있는지 체계적으로 평가한 첫 번째 연구이다. Nature 저널 3,096편과 ICLR 1,709편의 논문을 분석한 결과, GPT-4의 피드백이 인간 리뷰어들의 의견과 비슷한 수준의 일치도를 보였으며, 308명의 연구자 설문 조사에서 57.4%가 유용하다고 평가했다.

## Motivation

- **Known**: 동료 평가(peer review)는 과학의 기초를 이루지만, 학술 출판의 기하급수적 증가로 인해 고품질의 피드백을 확보하기 어려워지고 있음. 특히 후배 연구자나 자원이 부족한 기관의 연구자들이 더 큰 어려움을 겪고 있음.

- **Gap**: GPT-4 같은 대형 언어모델(LLM)을 과학 논문 평가에 활용하려는 관심이 증가하고 있지만, LLM 생성 피드백의 효용성에 대한 대규모 체계적 연구가 부재함.

- **Why**: 피드백 부족은 과학 발전의 근본적 제약이자 과학 불평등의 원인이며, 확장 가능하고 효율적인 피드백 메커니즘이 필수적임.

- **Approach**: (1) GPT-4 기반 자동화 파이프라인 구축, (2) 회고적 평가: 인간 리뷰어의 피드백과 LLM 피드백의 중복도 비교, (3) 전향적 사용자 연구: 308명의 연구자를 대상으로 설문 조사.

## Achievement

1. **LLM 피드백과 인간 피드백의 비교 가능성**: Nature 저널에서 GPT-4 피드백의 30.85%가 개별 인간 리뷰어의 의견과 일치했으며, 이는 두 인간 리뷰어 간의 일치도(28.58%)와 유사한 수준. ICLR의 경우 GPT-4 39.23% vs 인간 리뷰어 간 35.25%로 더 높은 일치도를 보임.

2. **약한 논문에 대한 더 높은 일치도**: ICLR 거절 논문의 경우 GPT-4와 인간 리뷰어 간 일치도가 43.80%로 더 높음. 이는 LLM이 품질 문제가 명확한 논문에서 더 효과적임을 시사.

3. **사용자 인식 조사 결과**: 57.4%의 연구자가 GPT-4 피드백을 '유용' 또는 '매우 유용'으로 평가했으며, 82.4%는 일부 인간 리뷰어의 피드백보다 더 도움이 된다고 응답.

4. **광범위한 피드백 범위**: 57.55%(Nature) ~ 77.18%(ICLR)의 GPT-4 댓글이 최소한 한 명의 인간 리뷰어에 의해서도 제기되어 상당한 중복도를 입증.

## How

- **피드백 생성 파이프라인**: PDF에서 전체 논문을 파싱하고, 논문 제목, 초록, 그림·표 캡션과 본문을 결합하여 GPT-4 프롬프트 구성. 구조화된 피드백 생성(중요성/참신성, 수용 이유, 거절 이유, 개선 제안).

- **회고적 평가 방법론**: 
  - 추출적 텍스트 요약(extractive text summarization)으로 LLM과 인간 피드백에서 주석 추출
  - 의미 기반 텍스트 매칭(semantic text matching)으로 공유 주석 식별
  - 인간 검증을 통한 파이프라인 정확성 확인(추출 F1: 96.8%, 매칭 F1: 82.4%)

- **데이터셋 구성**:
  - Nature 저널: 15개 저널, 3,096편 수용 논문, 8,745개 인간 리뷰 댓글
  - ICLR: 1,709편 논문(수용/거절), 6,505개 리뷰 댓글

- **사용자 연구 설계**: 110개 미국 기관 308명 연구자(AI/전산 생물학) 대상 설문, 다양한 경험 수준과 기관 유형 포함.

## Originality

- **최초 대규모 체계적 분석**: LLM 생성 학술 피드백의 효용성을 다룬 첫 번째 포괄적 실증 연구.

- **이중 평가 체계**: 회고적 데이터 분석과 전향적 사용자 연구를 결합하여 객관적 성능과 주관적 효용성을 동시에 검증.

- **다양한 학문 영역 커버**: 생의학부터 기계학습까지 다학제적 범위의 데이터셋을 통해 일반화 가능성 입증.

- **의미 기반 매칭 방법론**: 단순 키워드 매칭을 넘어 의미적 중복도를 측정하는 고도화된 평가 방법 제시.

- **공정한 비교 설계**: 2022년 이후 데이터만 사용하여 학습 데이터 중복 문제(data leakage) 회피.

## Limitation & Further Study

- **특정 양상에 대한 편향성**: GPT-4는 '더 많은 데이터셋에서 실험 추가' 같은 표면적 제안에 치중하고, 방법론 설계의 심층적 비판은 부족함.

- **심화된 방법론 검토 한계**: LLM은 기술적 기여의 깊이와 혁신성을 평가하는 데 여전히 어려움.

- **학문 분야 편향**: AI와 전산 생물학에 집중된 사용자 연구는 인문학이나 사회과학 등 다른 분야에의 적용 가능성 미지수.

- **리뷰어 경험 수준 미반영**: 리뷰어의 전문성 수준에 따른 피드백 품질 차이가 분석에 충분히 반영되지 않음.

- **후속 연구 방향**: 
  - LLM이 약한 피드백을 생성하는 이유에 대한 심화 분석
  - 인간-LLM 협력 피드백 시스템의 개발 및 검증
  - 타 LLM 모델(Claude, Llama 등)과의 비교 분석
  - 출판 후 단계에서의 LLM 피드백 활용 방안 탐색


## Evaluation

- Novelty: 5/5
- Technical Soundness: 4.5/5
- Significance: 5/5
- Clarity: 4.5/5
- Overall: 4.5/5

**총평**: 본 논문은 LLM의 과학 피드백 생성 능력을 최초로 대규모로 체계적으로 평가한 중요한 연구이다. 다양한 학문 영역의 대규모 데이터셋(4,805편)과 엄밀한 방법론, 그리고 실제 사용자 연구를 결합하여 높은 신뢰도를 확보했으며, 결과적으로 LLM이 인간 리뷰어와 비슷한 수준의 피드백 관점을 포착할 수 있음을 입증했다. 다만 LLM의 심층적 방법론 비판 능력 부족과 특정 양상의 피드백에 대한 편향성은 향후 개선이 필요한 영역이며, 인간-LLM 협력 모델의 개발이 실질적 의의를 가질 것으로 예상된다.

## Related Papers

- 🏛 기반 연구: [[papers/506_LLM4SR_A_Survey_on_Large_Language_Models_for_Scientific_Rese/review]] — 과학 연구에서 LLM 활용 전반에 대한 체계적 분석의 기반을 제공합니다.
- 🔗 후속 연구: [[papers/250_CycleResearcher_Improving_Automated_Research_via_Automated_R/review]] — 논문 피드백 능력이 자동화된 동료 검토 시스템으로 발전됩니다.
- 🔄 다른 접근: [[papers/679_Revieweval_An_evaluation_framework_for_ai-generated_reviews/review]] — AI 생성 리뷰 평가를 위한 서로 다른 접근법을 제시합니다.
- 🧪 응용 사례: [[papers/312_Empowering_language_models_with_active_inquiry_for_deeper_un/review]] — 능동적 질의 방법이 논문 피드백의 명확화에 활용됩니다.
- 🏛 기반 연구: [[papers/250_CycleResearcher_Improving_Automated_Research_via_Automated_R/review]] — LLM의 논문 피드백 능력이 자동화된 검토 시스템의 기반을 제공합니다.
