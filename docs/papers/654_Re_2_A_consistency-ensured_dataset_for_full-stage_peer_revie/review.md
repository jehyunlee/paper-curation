---
title: "654_Re_2_A_consistency-ensured_dataset_for_full-stage_peer_revie"
authors:
  - "Daoze Zhang"
  - "Zhijian Bao"
  - "Sihang Du"
  - "Zhiyi Zhao"
  - "Kuangling Zhang"
date: "2025"
doi: "N/A"
arxiv: ""
score: 4.0
essence: "본 논문은 OpenReview에서 수집한 24개 학술회의와 21개 워크숍의 19,926개 논문, 70,668개 리뷰 의견, 53,818개 재반박(rebuttal)으로 구성된 Re2 데이터셋을 제시하며, 일관성이 보장된 피어리뷰 데이터를 통해 대언어모델(LLM)의 리뷰 및 재반박 능력을 향상시키고자 한다."
tags:
  - "cat/AI-Powered_Scientific_Research_Frameworks"
  - "sub/Scientific_Peer_Review"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Zhang et al._2025_Re 2 A consistency-ensured dataset for full-stage peer review and multi-turn rebuttal discussions.pdf"
---

# Re 2: A consistency-ensured dataset for full-stage peer review and multi-turn rebuttal discussions

> **저자**: Daoze Zhang, Zhijian Bao, Sihang Du, Zhiyi Zhao, Kuangling Zhang, Dezheng Bao, Yang Yang | **날짜**: 2025 | **DOI**: N/A

---

## Essence

본 논문은 OpenReview에서 수집한 24개 학술회의와 21개 워크숍의 19,926개 논문, 70,668개 리뷰 의견, 53,818개 재반박(rebuttal)으로 구성된 Re2 데이터셋을 제시하며, 일관성이 보장된 피어리뷰 데이터를 통해 대언어모델(LLM)의 리뷰 및 재반박 능력을 향상시키고자 한다.

## Motivation

- **Known**: LLM은 학술 논문 리뷰 과정에서 저자와 리뷰어를 지원할 수 있는 강력한 도구로 인식되고 있으며, 실제로 ICLR 2025는 LLM 기반 리뷰 보조 시스템을 도입했음.

- **Gap**: 기존 피어리뷰 데이터셋은 세 가지 중대한 한계를 가짐:
  1. 데이터 다양성 부족 (대부분 ICLR만 포함)
  2. 데이터 품질 문제 (수정된 논문 버전을 원본으로 착각)
  3. 재반박 및 상호작용 지원 부족 (정적 리뷰 작업만 가능)

- **Why**: 논문 리뷰 부하 증가와 반복 제출 문제를 해결하기 위해, LLM이 저자의 자기 평가 도구로 기능하고 리뷰어를 보조할 수 있어야 함. 이를 위해서는 일관성 있는 고품질 데이터가 필수적.

- **Approach**: OpenReview API를 활용하여 45개 학술회의/워크숍에서 전체 피어리뷰 데이터를 수집하되, 제출 마감일 정보를 기반으로 초기 제출 논문만 추출하고, 재반박-토의 과정을 구조화된 다중 턴 대화로 변환.

## Achievement

1. **최대 규모의 일관성 보장 데이터셋**: 기존 데이터셋 대비 가장 광범위한 학술회의 커버리지(45개 venue)와 완전한 리뷰 단계(초기 제출, 리뷰, 평점, 신뢰도, 측면별 평점, 재반박, 토의, 점수 변화, 메타리뷰, 최종 결정) 포함.

2. **데이터 일관성 검증**: 제출 마감일을 기준으로 초기 제출 버전만 포함하여, 기존 데이셋의 "수정된 논문 버전 포함" 문제 해결. Table 1에서 노란색으로 강조된 데이셋들 중 유일하게 모든 논문의 초기 제출 보장.

3. **다중 턴 대화 패러다임**: 재반박과 토의를 정적 데이터가 아닌 구조화된 다중 턴 대화로 포맷하여, 대화형 LLM 기반 리뷰 보조 시스템 학습 지원.

4. **실용적 활용성**: 전통적인 정적 작업(수용성 예측, 점수 예측, 리뷰/메타리뷰 생성)뿐 아니라 저자의 자기 개선을 위한 동적 대화형 모델 훈련 지원.

## How

- **데이터 수집**: OpenReview 공식 API를 통해 2013-2025년 68개 학술회의의 모든 공개 논문과 리뷰 기록 자동 수집

- **초기 제출 버전 확보**: 각 학술회의의 제출 마감일을 수집하고, 마감일 이전의 최신 버전을 "Revision History" 페이지에서 웹 스크래핑으로 추출

- **형식 정규화**: 45개 venue-year 조합별로 서로 다른 리뷰 데이터 포맷을 파악하고 맞춤형 추출 로직 구현

- **텍스트 변환**: PDF 논문을 Doc2X 도구로 LaTeX 및 Markdown 형식의 평문으로 변환하여 접근성 향상

- **다중 턴 대화 구조화**: 재반박-토의 데이터를 구조화된 대화 형식으로 변환하여 LLM 훈련용 형태로 정리

## Originality

- **최초의 일관성 검증 시스템**: 제출 마감일을 기반으로 초기 제출 논문을 검증하는 메커니즘은 기존 데이셋에서 수행되지 않음.

- **다중 턴 재반박 패러다임**: 재반박 데이터를 정적 문서가 아닌 대화 턴으로 구조화한 최초의 시도.

- **최광역 venue 커버리지**: 기존 데이셋의 ICLR 편중 문제를 해결하고 OpenReview 전체 공개 데이터를 통합.

- **완전한 리뷰 파이프라인**: 제출부터 최종 결정까지 모든 단계의 데이터를 일관되게 포함하는 최초 데이셋.

## Limitation & Further Study

- **PDF 변환 품질**: Doc2X 도구 의존성으로 인한 수식 및 표 인식 오류 가능성 (상용 도구의 한계).

- **데이터 개인정보 보호**: 저자 및 리뷰어 익명성 관련 고려사항이 논문에서 명시적으로 다루어지지 않음.

- **비영어 논문**: OpenReview의 특성상 영어 논문 중심일 가능성 높음.

- **후속 연구 제안**:
  1. 데이터 품질 검증을 위한 수동 감사(manual audit) 절차 확대
  2. 다중 턴 재반박 기반 LLM 모델 학습 및 평가 프레임워크 개발
  3. 리뷰 품질 변화가 논문 재제출 횟수에 미치는 영향 분석
  4. 다국어 피어리뷰 데이터 수집 및 통합

## Evaluation

- **Novelty**: 4/5
  - 데이터 일관성 검증 및 다중 턴 재반박 패러다임은 새로움. 하지만 기술적 혁신보다는 데이터 엔지니어링 기여도 높음.

- **Technical Soundness**: 4/5
  - 데이터 수집 및 형식화 방법론은 체계적임. 다만 PDF 변환 정확도 검증이 부족하고, 데이터 품질 보증 메커니즘이 상세하지 않음.

- **Significance**: 5/5
  - 리뷰 부하 증가 문제 해결에 직접 기여할 수 있는 핵심 자원. LLM 기반 리뷰 시스템 개발의 토대 제공.

- **Clarity**: 4/5
  - 전체적으로 명확하나, Table 1에서 재반박 데이터의 구체적 구조 설명 부족. 다중 턴 대화 포맷 상세 예시 필요.

- **Overall**: 4/5

**총평**: Re2는 기존 피어리뷰 데이터셋의 다양성, 일관성, 기능성 문제를 체계적으로 해결한 의미 있는 자원 기여이며, 특히 초기 제출 버전 보증과 다중 턴 재반박 구조화는 향후 LLM 기반 리뷰 시스템 개발에 실질적 가치를 제공할 것으로 기대된다.

## Related Papers

- 🏛 기반 연구: [[papers/679_Revieweval_An_evaluation_framework_for_ai-generated_reviews/review]] — AI 생성 리뷰 평가 프레임워크가 피어리뷰 데이터셋 구축과 LLM 리뷰 능력 평가의 기준을 제공합니다.
- 🔗 후속 연구: [[papers/262_Deepreview_Improving_llm-based_paper_review_with_human-like/review]] — 인간다운 논문 리뷰 개선 방법이 Re2 데이터셋을 활용한 리뷰 품질 향상으로 확장될 수 있습니다.
- 🔄 다른 접근: [[papers/608_Peer_Review_as_A_Multi-Turn_and_Long-Context_Dialogue_with_R/review]] — 피어리뷰 과정에서 일관성 보장 데이터셋과 다중 턴 대화 기반 접근법을 비교할 수 있습니다.
- 🔗 후속 연구: [[papers/803_The_open_review-based_orb_dataset_Towards_automatic_assessme/review]] — 피어 리뷰 전 과정에 대한 일관성 보장 데이터셋이 ORB의 적용 범위를 확장한다.
- 🔗 후속 연구: [[papers/145_Autoreproduce_Automatic_ai_experiment_reproduction_with_pape/review]] — AUTOREPRODUCE의 실험 자동 재현은 Re²의 전체 과정 피어 리뷰 데이터셋을 활용하여 논문의 일관성을 보장하는 재현 가능한 연구 환경을 구축합니다.
- 🏛 기반 연구: [[papers/698_Scaling_Reproducibility_An_AI-Assisted_Workflow_for_Large-Sc/review]] — 전체 단계 동료 심사를 위한 일관성 보장 데이터셋은 대규모 재현성 연구에서 AI 워크플로우 검증의 데이터 기반을 제공한다.
