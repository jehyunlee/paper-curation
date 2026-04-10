---
title: "1089_Prompting_llms_to_compose_meta-review_drafts_from_peer-revie"
authors:
  - "Lan Luo"
  - "Dongyijie Primo Pan"
  - "Junhua Zhu"
  - "Muzhi Zhou"
  - "Pan Hui"
date: "2024"
doi: ""
arxiv: ""
score: 4.0
essence: "본 논문은 LLM(GPT-3.5, PaLM2, LLaMA2)이 학술 논문의 피어 리뷰 의견들을 종합하여 메타리뷰 초안 작성을 지원할 수 있는지 연구한 사례 연구이다."
tags:
  - "cat/AI-Powered_Scientific_Research_Frameworks"
  - "sub/Scientific_Peer_Review"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Luo et al._2024_Prompting llms to compose meta-review drafts from peer-review narratives of scholarly manuscripts.pdf"
---

# Prompting llms to compose meta-review drafts from peer-review narratives of scholarly manuscripts

> **저자**: Lan Luo, Dongyijie Primo Pan, Junhua Zhu, Muzhi Zhou, Pan Hui | **날짜**: 2024 | **URL**: [https://arxiv.org/abs/2402.15589](https://arxiv.org/abs/2402.15589)

---

## Essence

![Figure 4](figures/fig4.webp)

*Fig. 4: Overall Rating aggregated over three LLMs and four Prompt Levels.*

본 논문은 LLM(GPT-3.5, PaLM2, LLaMA2)이 학술 논문의 피어 리뷰 의견들을 종합하여 메타리뷰 초안 작성을 지원할 수 있는지 연구한 사례 연구이다.

## Motivation

- **Known**: 메타리뷰 자동 생성 기법들이 제안되었으나, LLM의 성능이 복잡한 다중 관점 요약 작업에서 충분히 연구되지 않았다. 또한 표준화된 프롬프팅 분류체계가 부재한 상태이다.
- **Gap**: LLM이 메타리뷰 작성과 같은 다중 제약·다중 관점 요약 작업에서의 성능이 미흡하게 연구되었으며, 체계적인 프롬프팅 분류체계(TELeR)를 적용한 비교 분석이 부재하다.
- **Why**: 메타리뷰 작성은 피어 리뷰 프로세스에서 중요하지만 시간이 많이 소요되고, 인간의 피로와 편향으로 인해 일관성과 정확성이 떨어질 수 있기 때문이다.
- **Approach**: ICLR 학술지의 40개 논문과 피어 리뷰 의견을 수집하고, TELeR 분류체계에 기반한 4단계 프롬프트 레벨로 3개 LLM을 프롬프팅하여 다중 관점 요약(MPS)을 생성한 후 인간 평가와 GPT-4 자동 평가를 수행했다.

## Achievement

![Figure 4](figures/fig4.webp)

*Fig. 4: Overall Rating aggregated over three LLMs and four Prompt Levels.*

- **LLM 성능 비교**: GPT-3.5와 PaLM2가 LLaMA2보다 높은 인간 평가 점수를 받았으며, PaLM2는 높은 재현율, GPT-3.5는 높은 정밀도를 보였다
- **프롬프트 레벨 효과**: TELeR 분류체계의 4단계 프롬프트 레벨에 따른 성능 차이를 체계적으로 분석했다
- **자동 평가의 한계**: GPT-4 자동 평가가 인간 판단과 낮은 상관관계를 보여, LLM 기반 평가의 신뢰성 문제를 지적했다
- **광범위한 정성적 분석**: 4,800개의 세분화된 평가와 90개의 LLM 레벨 판단을 수집하여 깊이 있는 분석을 제공했다

## How

![Figure 1](figures/fig1.webp)

*Fig. 1: Core Contributions Ratings - rated separately across different Prompt Levels and different LLMs. Here, SA:*

- ICLR 학술지 2020-2023년 13,800개 투고 논문 중 40개 선별 (거절된 논문 10개 포함)
- GPT-3.5, PaLM2, LLaMA2 3개 LLM을 제로샷(Zero-shot) 설정에서 사용
- TELeR 분류체계의 4단계 프롬프트 레벨 설계 (Level 1: 기본 지시, Level 2-4: 점진적 상세화)
- 10명의 인간 평가자가 5개 평가 기준(핵심 기여도, 강점, 약점, 개선점, 문헌 검토)에 따라 정성적 평가 수행
- GPT-4를 이용한 자동 평가 및 인간 평가와의 상관관계(Pearson correlation) 분석

## Originality

- 자동 메타리뷰 생성이 아닌 메타리뷰 보조 도구로서의 다중 관점 요약(MPS) 작업에 초점
- 표준화된 TELeR 분류체계를 메타리뷰 작성에 처음 적용하여 체계적 비교 가능
- 대규모 정성적 인간 평가(4,800개 세분화된 판단)와 LLM 자동 평가의 신뢰성 검증을 병행
- 복수 LLM의 성능 비교뿐만 아니라 프롬프트 레벨별 효과를 체계적으로 분석

## Limitation & Further Study

- 40개 논문이라는 제한된 데이터셋으로 일반화 가능성 제약
- PaLM2는 API가 없어 수동 평가로 진행되어 일관성 문제 가능
- 프롬프트 레벨 4 이상의 더 복잡한 프롬프팅 기법 미탐구
- 메타리뷰 작성의 최종 판단 단계(conflict resolution, recommendation)는 미포함
- **후속 연구**: 더 큰 규모 데이터셋, fine-tuning을 통한 LLM 성능 개선, 메타리뷰 전체 파이프라인 자동화 연구 필요

## Evaluation

- Novelty: 3/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 논문은 표준화된 프롬프팅 분류체계를 적용하여 메타리뷰 작성 지원 작업에 대한 LLM의 성능을 최초로 체계적으로 비교 분석했으며, 대규모 정성적 평가를 통해 LLM 자동 평가의 신뢰성 문제를 밝혀냈다는 점에서 학술 출판 프로세스 자동화 연구에 유의미한 기여를 한다.

## Related Papers

- 🔄 다른 접근: [[papers/126_Automated_review_generation_method_based_on_large_language_m/review]] — LLM 기반 리뷰 생성에서 메타리뷰 작성과 자동 리뷰 생성의 서로 다른 접근 방식을 제시한다.
- 🔗 후속 연구: [[papers/608_Peer_Review_as_A_Multi-Turn_and_Long-Context_Dialogue_with_R/review]] — 피어 리뷰를 다중 턴 장문맥 대화로 확장하여 메타리뷰 작성을 발전시킨다.
- 🔄 다른 접근: [[papers/126_Automated_review_generation_method_based_on_large_language_m/review]] — 학술논문 리뷰 자동화에서 완전 자동 생성과 메타리뷰 작성 지원의 서로 다른 접근법을 제시한다.
