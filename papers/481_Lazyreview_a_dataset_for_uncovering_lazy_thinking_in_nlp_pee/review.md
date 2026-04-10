---
title: "481_Lazyreview_a_dataset_for_uncovering_lazy_thinking_in_nlp_pee"
authors:
  - "Sukannya Purkayastha"
  - "Zhuang Li"
  - "Anne Lauscher"
  - "Lizhen Qu"
  - "Iryna Gurevych"
date: "2025"
doi: "-"
arxiv: ""
score: 4.4
essence: "NLP 동료 검토(peer review) 과정에서 발견되는 \"게으른 사고(lazy thinking)\" 를 자동으로 탐지하기 위한 첫 번째 주석 데이터셋 LAZYREVIEW를 제시한다. 500개의 전문가 주석 검토 세그먼트와 1,276개의 자동 주석 세그먼트로 구성되며, 지시 기반 미세 조정(instruction-based fine-tuning)을 통해 대규모 언어 모델(LLM) 성능을 10-20 포인트 향상시킬 수 있음을 보여준다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Expert_Review_Annotation"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Purkayastha et al._2025_Lazyreview a dataset for uncovering lazy thinking in nlp peer reviews.pdf"
---

# Lazyreview a dataset for uncovering lazy thinking in nlp peer reviews

> **저자**: Sukannya Purkayastha, Zhuang Li, Anne Lauscher, Lizhen Qu, Iryna Gurevych | **날짜**: 2025 | **DOI**: -

---

## Essence

NLP 동료 검토(peer review) 과정에서 발견되는 "게으른 사고(lazy thinking)" 를 자동으로 탐지하기 위한 첫 번째 주석 데이터셋 LAZYREVIEW를 제시한다. 500개의 전문가 주석 검토 세그먼트와 1,276개의 자동 주석 세그먼트로 구성되며, 지시 기반 미세 조정(instruction-based fine-tuning)을 통해 대규모 언어 모델(LLM) 성능을 10-20 포인트 향상시킬 수 있음을 보여준다.

## Motivation

- **Known**: 피어 리뷰는 과학 출판의 핵심 품질 관리 메커니즘이며, ACL Rolling Review(ARR)는 2021년 NLP 주요 학회의 기본 검토 플랫폼으로 채택되었다. 게으른 사고는 명확한 근거 없이 피상적 휴리스틱(heuristics)을 바탕으로 연구를 비판하는 행위로 정의되어 있다.

- **Gap**: 검토자의 과중한 업무 부담과 정보 과부하로 인해 게으른 사고가 광범위하게 발생하고 있으나(ARR 2023 보고서: 저자 보고 이슈의 24.3%), NLP에서 이를 자동 탐지하기 위한 실제 데이터셋과 연구가 부재하다.

- **Why**: 자동화된 탐지 방법은 피어 리뷰 품질을 향상시킬 수 있고, 주니어 검토자 훈련 가이드라인으로 활용될 수 있다. Kuznetsov et al. (2024)도 이러한 자동 방법의 필요성을 제기했다.

- **Approach**: ARR 2022 및 EMNLP 2020 가이드라인을 바탕으로 NLPEER 데이터셋의 ARR 2022 검토 684개(476개 논문, 11,245개 문장)에서 GPT-4를 통해 게으른 사고 후보 세그먼트를 추출한 후, 3라운드의 반복적 주석 작업을 수행하며 가이드라인을 점진적으로 개선한다.

## Achievement

1. **첫 번째 게으른 사고 주석 데이터셋 구축**: 500개의 전문가 주석 세그먼트와 1,276개의 은(silver) 주석 세그먼트(최고 성능 모델 예측)를 포함한 LAZYREVIEW 데이터셋 공개. 3라운드 반복 작업을 통해 Cohen's κ가 0.32 → 0.48로 꾸준히 향상되어 가이드라인 개선의 효과성을 입증.

2. **LLM 성능 대폭 향상**: 제로 샷(zero-shot) 설정에서 LLM의 게으른 사고 탐지 능력이 매우 제한적이나, 본 데이터셋으로 지시 미세 조정(instruction fine-tuning)하면 약 10-20 포인트의 정확도 향상 달성.

3. **인간 검토 품질 개선 실증**: 게으른 사고 피드백을 반영하여 재작성한 검토문이 원본보다 더 포괄적(comprehensive)이고 실행 가능(actionable)함을 인간 선호도 기반 평가로 확인.

4. **긍정 예시(positive examples)의 효과**: 각 클래스에 대한 주석 예시를 제공하면 주석자의 이해도와 합의도, 그리고 문맥 내 학습(in-context learning) 성능이 모두 향상됨.

## How

- **GPT-4 기반 세그먼트 추출**: 'Summary of Weaknesses' 섹션에서 14개의 게으른 사고 클래스에 해당하는 검토 세그먼트 1,776개 자동 추출. 검증 100개 샘플에서 κ=0.82, F1=0.85 달성.

- **반복적 가이드라인 개선**:
  - Round 1 (κ=0.31): 원본 ARR 가이드라인 사용 → 낮은 합의도와 주석자 신뢰도 발견
  - Round 2 (κ=0.36): EMNLP 2020 가이드라인 통합, 누락된 클래스('Non-mainstream Approaches') 추가, 클래스 설명 정제
  - Round 3 (κ=0.48): 긍정 예시 추가, 'Not Enough Information' 클래스 신설, 기준 명확화

- **전문가 주석**: 2명의 박사 학생이 반복 주석, 1명의 선임 박사후연구원이 불일치 사항 중재. 가이드라인 확정 후 새로운 주석자 집단으로 재검증.

- **LLM 성능 평가**: GPT-3.5, GPT-4, Llama 2 등 다양한 LLM에 대해 제로 샷, 퓨 샷(few-shot), 지시 미세 조정 세팅에서 성능 비교.

- **통제 실험**: 인간 검토자가 게으른 사고 주석 있음/없음 조건에서 검토문 재작성. 5명의 평가자가 포괄성, 실행 가능성, 구체성 차원에서 선호도 평가.

## Originality

- 피어 리뷰의 게으른 사고 탐지를 위한 **첫 번째 실제 주석 데이터셋** 제공. 기존 ARR 가이드라인을 실증적으로 데이터화한 첫 시도.

- 문제 정의의 **높은 주관성**을 인식하고 Cohen's κ를 중심으로 반복적 가이드라인 개선 프로토콜 고안. 포지티브 예시의 체계적 도입이 주석 품질과 LLM 성능 모두에 미치는 영향을 실증적으로 검증.

- **게으른 사고 피드백의 실제 효과**를 인간 평가로 검증한 점이 독창적. 자동 탐지 도구의 실용적 가치를 증명.

- 데이터셋 및 강화된 가이드라인의 공개를 통해 커뮤니티의 주니어 검토자 훈련에 직접 기여.

## Limitation & Further Study

- **주석 규모의 제한성**: 500개의 전문가 주석은 중규모 데이터셋. 더 큰 규모의 주석으로 모델 성능을 추가 향상시킬 가능성.

- **단일 언어/지역 편향**: ARR 2022 영어 검토만 포함. 다국어 환경의 게으른 사고 패턴은 미탐사.

- **클래스 불균형**: 일부 게으른 사고 클래스는 표현이 드물어 균형 잡힌 샘플링 필요.

- **검토 세그먼트 정의의 모호성**: 1-5개 문장의 가변 길이 세그먼트 사용으로 인한 경계 판정의 어려움.

- **후속 연구 방향**:
  - 다국어 게으른 사고 탐지로 확장
  - 자동 탐지 모델을 실제 ARR 플랫폼에 통합하여 검토자 실시간 피드백 시스템 구축
  - 검토 개선의 장기 영향 추적 연구
  - 게으른 사고의 발생 원인(시간 부압, 검토자 경험 수준 등)에 대한 사회과학적 분석


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4/5
- Significance: 4.5/5
- Clarity: 4.5/5
- Overall: 4.4/5

**총평**: 본 논문은 NLP 커뮤니티의 실제 문제인 피어 리뷰의 게으른 사고 탐지를 위한 첫 번째 실제 데이터셋을 제공하며, 반복적 가이드라인 개선과 긍정 예시의 효과를 체계적으로 검증했다. LLM의 지시 미세 조정으로 높은 성능 향상을 보였으며, 인간 평가를 통해 실제 검토 품질 개선을 입증한 점이 강점이다. 다만 데이터셋 규모와 언어 다양성 측면에서 개선 여지가 있으며, 실제 검토 플랫폼 통합을 통한 장기 영향 평가가 필요하다.

## Related Papers

- 🔗 후속 연구: [[papers/677_Reviewer2_Optimizing_Review_Generation_Through_Prompt_Genera/review]] — 동료 검토의 게으른 사고 탐지 연구가 LLM 기반 리뷰 생성 최적화 연구의 품질 평가 기준을 제공합니다.
- ⚖️ 반론/비판: [[papers/206_ChatGPT_outperforms_crowd_workers_for_text-annotation_tasks/review]] — ChatGPT의 텍스트 주석 우수성과 대조적으로 동료 검토에서 나타나는 LLM의 한계와 게으른 사고 문제를 지적합니다.
- 🏛 기반 연구: [[papers/883_When_reviewers_lock_horn_Finding_disagreement_in_scientific/review]] — 과학적 검토에서의 의견 불일치 연구가 게으른 사고 탐지 연구의 이론적 배경을 제공합니다.
- 🔄 다른 접근: [[papers/206_ChatGPT_outperforms_crowd_workers_for_text-annotation_tasks/review]] — 텍스트 주석 작업에서 ChatGPT의 우수성을 보인 반면, 동료 검토에서 LLM의 한계를 다루는 상반된 관점을 제시합니다.
- 🏛 기반 연구: [[papers/677_Reviewer2_Optimizing_Review_Generation_Through_Prompt_Genera/review]] — 동료 검토의 게으른 사고 문제를 해결하기 위한 측면 프롬프트 기반 리뷰 생성 최적화 접근법을 제시합니다.
