---
title: "810_Through_the_lens_of_core_competency_Survey_on_evaluation_of"
authors:
  - "Ziyu Zhuang"
  - "Qiguang Chen"
  - "Longxuan Ma"
  - "Mingda Li"
  - "Yi Han"
date: "2023"
doi: "arXiv:2308.07902"
arxiv: ""
score: 3.5
essence: "대규모 언어 모델(LLM)의 평가 방법론을 체계화하기 위해 \"핵심 역량(Core Competency)\" 프레임워크를 제안하는 종합 조사 논문이다. 540개 이상의 평가 과제를 분석하여 LLM의 4가지 핵심 역량(지식, 추론, 신뢰성, 안전성)으로 통합함으로써 산재된 평가 벤치마크를 체계적으로 정리한다."
tags:
  - "cat/AI-Powered_Scientific_Research_Frameworks"
  - "sub/AI_for_Science_Taxonomy"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Zhuang et al._2023_Through the lens of core competency Survey on evaluation of large language models.pdf"
---

# Through the lens of core competency: Survey on evaluation of large language models

> **저자**: Ziyu Zhuang, Qiguang Chen, Longxuan Ma, Mingda Li, Yi Han, Yushan Qian, Haopeng Bai, Zixian Feng, Weinan Zhang, Ting Liu | **날짜**: 2023 | **DOI**: [arXiv:2308.07902](https://arxiv.org/abs/2308.07902)

---

## Essence

대규모 언어 모델(LLM)의 평가 방법론을 체계화하기 위해 "핵심 역량(Core Competency)" 프레임워크를 제안하는 종합 조사 논문이다. 540개 이상의 평가 과제를 분석하여 LLM의 4가지 핵심 역량(지식, 추론, 신뢰성, 안전성)으로 통합함으로써 산재된 평가 벤치마크를 체계적으로 정리한다.

## Motivation

- **Known**: ChatGPT 등 LLM의 출현으로 인한 탁월한 성능 향상과 광범위한 실제 활용이 이루어지고 있다. 기존 연구에서는 LLM 평가를 위한 다양한 벤치마크가 제안되었다.

- **Gap**: 기존 평가 작업은 크게 세 가지 문제점을 가진다: (1) 전통적 NLP 과제는 LLM의 뛰어난 성능으로 인해 구별력을 상실, (2) 기존 평가 과제가 실제 응용의 다양성을 따라가지 못함, (3) 540개 이상의 평가 과제가 산재되어 있으나 체계적으로 검토된 바 없음.

- **Why**: LLM 평가의 명확한 프레임워크 부재는 연구 방향성을 모호하게 하며, 평가 결과의 통일된 해석을 어렵게 한다. 기업의 역량 평가(Competency Test) 개념처럼 LLM도 체계적인 역량 중심 평가가 필요하다.

- **Approach**: 540개 이상의 평가 과제를 수집·분석하여 4가지 핵심 역량(Knowledge, Reasoning, Reliability, Safety)으로 분류하고, 각 역량별 정의, 분류체계, 평가 지표를 제시한다.

## Achievement

| **핵심 역량** | **세부 분류** | **역할** |
|-------------|-----------|---------|
| **Knowledge** | 언어적 지식, 세계 지식 | 기초적 의사소통 능력 |
| **Reasoning** | 인과추론, 귀납, 연역, 유추, 다중홉, 수학적 추론 | 복잡한 문제 해결 능력 |
| **Reliability** | 견고성, 보정성, 일관성 | 안정적이고 신뢰할 수 있는 출력 |
| **Safety** | 독성, 편향성, 윤리성, 프라이버시 | 해로운 결과 방지 |

1. **체계화된 평가 프레임워크**: 4가지 핵심 역량 하에 540개 이상의 평가 과제를 통일된 구조로 분류. 각 역량별 정의, 분류체계, 평가 지표를 명확히 제시.

2. **확장 가능한 프로젝트**: 역량과 과제 간의 다대다(many-to-many) 관계를 정확히 표현하는 오픈 소스 프로젝트 제공으로 새로운 과제의 추가를 용이하게 함.

3. **혼재된 평가 표준화**: 전통적 NLP 과제, 신흥 능력 평가, 내재적 특성 평가를 통합하여 중복을 제거하고 명확한 평가 결과 제시 가능.

## How

- **Knowledge 역량 평가**: 언어 문법/의미론/화용론(BLiMP, Linguistic Mappings) 및 상식/팩트/도메인 지식(WikiFact, TruthfulQA, HellaSwag) 평가 과제 활용

- **Reasoning 역량 평가**: 인과 관계(COPA), 수학적 귀납(Mathematical Induction), 구조화 데이터 해석(ToTTo), 수학 문제 해결(GSM8K) 등 6가지 세부 추론 능력 분류

- **다층적 분석**: 기존 벤치마크(GLUE, SuperGLUE, BIG-Bench, HELM)를 역량 프레임워크에 매핑하여 평가 과제의 상호 관계 파악

- **Competency 개념 도입**: 기업 채용의 역량 평가 방식을 NLP에 적용하여 각 역량의 중요도를 차등 평가 가능

## Originality

- 540개 이상의 LLM 평가 과제를 최초로 체계적으로 수집·분류한 대규모 조사 연구

- 기업 역량 평가(Competency Test) 개념을 NLP 평가에 창의적으로 적용

- 이분 그래프(bipartite graph) 기반의 역량-과제 매핑 구조로 평가 과제 간 중복을 제거하면서도 확장 가능성 확보

- 단순한 벤치마크 나열이 아닌 계층적·관계적 분류 체계 제시로 평가 방법론의 기초 마련

## Limitation & Further Study

- **완성도 한계**: 논문 길이 제약으로 인해 540개 과제 중 일부만 제시되었으며, 보다 포괄적인 버전은 추후 공개 예정

- **Reliability/Safety 역량의 상세도 부족**: 초록 및 제시된 본문에서는 Knowledge와 Reasoning 중심으로 설명되어 있으며, Reliability와 Safety의 세부 분류 및 벤치마크가 덜 구체화됨

- **평가 지표의 표준화 미흡**: 역량별 평가 지표(metrics)의 정의가 명확하지 않아 실제 평가 시 적용의 일관성 문제 가능

- **데이터 오염(Data Leakage) 해결**: 단회성 평가를 넘어 정기적인 테스트 세트 갱신 필요성을 인식하나 구체적 방안 부족

- **향후 방향**: (1) 멀티모달(multimodal) LLM 평가 확장, (2) Reliability/Safety 역량에 대한 동적 평가 메커니즘 개발, (3) 모델 간 비교의 공정성 보장을 위한 상대적 평가 방식 연구

## Evaluation

- **Novelty**: 4/5 - 기존 산재된 평가 과제를 체계적으로 분류한 점은 신선하나, 역량 개념 자체가 기업 평가에서 차용된 개념

- **Technical Soundness**: 3.5/5 - 분류체계의 논리적 타당성은 있으나, 실제 평가 지표의 수식화나 통계적 검증이 부재함. 역량 간 상호작용(예: 지식이 추론에 미치는 영향)에 대한 분석 부족

- **Significance**: 4/5 - 540개 이상의 과제를 통합하는 프로젝트로 LLM 평가 커뮤니티에 상당한 실용적 가치를 제공할 것으로 예상됨. 다만 이론적 기여는 제한적

- **Clarity**: 3.5/5 - 전체 구조는 명확하나 본문의 일부만 제시되어 Reliability, Safety 역량의 정의와 분류가 충분히 설명되지 않음. 4가지 역량을 선정한 근거가 명확하지 않음

- **Overall**: 3.5/5

**총평**: 본 논문은 빠르게 증식하는 LLM 평가 과제를 핵심 역량 중심으로 체계화한 중요한 조사 연구이며, 커뮤니티를 위한 실용적 도구를 제공한다. 다만 부분적 공개와 평가 지표의 정량화 부족으로 완성도에서 아쉬움이 있으며, 추후 완전 버전 공개와 함께 Reliability/Safety 역량에 대한 보다 깊이 있는 논의가 필요하다.

## Related Papers

- 🔗 후속 연구: [[papers/005_A_comprehensive_survey_on_long_context_language_modeling/review]] — 긴 문맥 언어 모델링에 대한 포괄적 조사가 핵심 역량 프레임워크의 평가 방법론을 확장한다.
- 🔄 다른 접근: [[papers/846_TrustLLM_Trustworthiness_in_Large_Language_Models/review]] — LLM의 신뢰성 평가가 핵심 역량 중심 평가와는 다른 관점에서 모델 성능을 분석한다.
