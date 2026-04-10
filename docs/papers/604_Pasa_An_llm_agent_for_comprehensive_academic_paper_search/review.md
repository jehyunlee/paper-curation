---
title: "604_Pasa_An_llm_agent_for_comprehensive_academic_paper_search"
authors:
  - "Yichen He"
  - "Guanhua Huang"
  - "Peiyuan Feng"
  - "Yuan Lin"
  - "Yuchen Zhang"
date: "2025"
doi: "N/A"
arxiv: ""
score: 4.25
essence: "PaSa는 복잡한 학술 논문 검색을 자동으로 수행하는 LLM 기반 에이전트로, 검색 도구 활용, 논문 읽기, 인용 네트워크 탐색을 통해 종합적이고 정확한 검색 결과를 제공한다. 합성 데이터(AutoScholarQuery)로 학습했음에도 실제 환경(RealScholarQuery)에서 Google Scholar 및 GPT-4o 기반 방법들을 크게 능가한다."
tags:
  - "cat/LLM-Based_Scientific_Reasoning"
  - "sub/Scientific_Literature_Analysis"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/He et al._2025_Pasa An llm agent for comprehensive academic paper search.pdf"
---

# PaSa: An LLM Agent for Comprehensive Academic Paper Search

> **저자**: Yichen He, Guanhua Huang, Peiyuan Feng, Yuan Lin, Yuchen Zhang, Hang Li, Weinan E | **날짜**: 2025 | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp)
*PaSa 시스템 아키텍처: Crawler와 Selector 두 개의 LLM 에이전트로 구성*

PaSa는 복잡한 학술 논문 검색을 자동으로 수행하는 LLM 기반 에이전트로, 검색 도구 활용, 논문 읽기, 인용 네트워크 탐색을 통해 종합적이고 정확한 검색 결과를 제공한다. 합성 데이터(AutoScholarQuery)로 학습했음에도 실제 환경(RealScholarQuery)에서 Google Scholar 및 GPT-4o 기반 방법들을 크게 능가한다.

## Motivation

- **Known**: Google Scholar 등 기존 학술 검색 시스템은 일반적인 쿼리에는 효과적이나, "non-stationary RL에서 UCB 기반 value-based 방법"과 같은 세밀한 학술 쿼리에는 부족하다. 연구자들은 문헌 조사에 상당한 시간을 소비한다.

- **Gap**: 기존 LLM 기반 정보 검색 연구는 쿼리 개선(query reformulation)에 중심을 두고 있으나, 실제 연구자들은 검색 도구뿐 아니라 논문 읽기, 인용 확인 등 더 깊은 활동을 수행한다.

- **Why**: 종합적이고 정확한 학술 검색을 위해서는 인간 연구자의 행동을 모방하는 자동화된 에이전트가 필요하다.

- **Approach**: 두 개의 LLM 에이전트(Crawler와 Selector)로 구성된 PaSa를 제안하고, AGILE 강화학습 프레임워크로 최적화하며, 새로운 session-level PPO 알고리즘을 설계한다.

## Achievement

![Figure 2](figures/fig2.webp)
*PaSa 워크플로우 예시: Crawler의 다양한 [Search] 실행과 인용 네트워크 탐색*

1. **성능 우수성**: PaSa-7B는 AutoScholarQuery 테스트 셋에서 Google+GPT-4o 대비 Recall@20에서 34.05%, Recall@50에서 39.36% 향상. RealScholarQuery에서는 Recall@20 37.78%, Recall@50 39.90% 향상. PaSa-GPT-4o 대비 30.36% 재현율 향상.

2. **합성 데이터의 효과성**: 합성 데이터(AutoScholarQuery, 33.5k 쿼리-논문 쌍)로만 학습했음에도 실제 환경에서 우수한 성능 달성, 도메인 전이(domain transfer) 가능성 입증.

3. **고품질 벤치마크 구축**: 실제 연구자 50명의 쿼리로 구성된 RealScholarQuery 벤치마크 개발으로 현실적 평가 환경 제공.

## How

- **Crawler 에이전트**: 사용자 쿼리를 처리하여 검색 도구 호출([Search]), 현재 논문에서 인용 확장([Expand]), 또는 중단([Stop])을 자동으로 결정하고 논문 큐(paper queue)에 추가

- **Selector 에이전트**: 논문 큐의 각 논문을 읽으며 사용자 쿼리 요구사항 충족 여부 판단

- **AGILE 강화학습 프레임워크**: 전체 에이전트 스킬을 end-to-end 방식으로 최적화

- **Session-level PPO**: 논문 검색 태스크의 특이한 도전과제 해결:
  - 희소 보상(sparse reward): 수집 논문이 실제 적격 논문의 일부 집합
  - 장문 궤적(long trajectory): 수백 개 논문의 전체 궤적을 LLM 컨텍스트에 직접 입력할 수 없음

- **AutoScholarQuery 구축**: ICLR/ICML/NeurIPS 2023, ACL/CVPR 2024의 관련 연구(Related Work) 섹션에서 GPT-4o를 이용해 쿼리와 답변 논문 자동 생성

- **RealScholarQuery 구축**: 실제 연구자 쿼리 수집 → 광범위한 필터링 → 다중 검색 방법(PaSa, Google, Google Scholar, ChatGPT 등)으로 후보 논문 수집 → 전문 어노테이터 검증

## Originality

- **자동 학술 검색 에이전트의 창의적 설계**: 기존 쿼리 개선(query reformulation)을 넘어 인용 네트워크 탐색, 논문 읽기 등 다단계 의사결정을 통합하는 최초의 포괄적 접근

- **Session-level PPO 알고리즘**: 논문 검색의 특유한 특성(희소 보상, 장문 궤적)을 해결하기 위한 맞춤형 학습 방법 설계

- **고품질 합성 데이터셋의 창의적 활용**: 학술 논문의 Related Work 섹션을 자동으로 큐레이션하여 자연스럽고 실제적인 쿼리-답변 쌍 생성

- **실제 환경 평가의 엄격함**: 단순 테스트 셋뿐 아니라 실제 연구자 50명의 쿼리로 구성된 RealScholarQuery 벤치마크 개발

## Limitation & Further Study

- **데이터 편향 가능성**: AutoScholarQuery가 상위 5개 학술대회(ICLR, ICML, NeurIPS, ACL, CVPR) 논문만으로 구성되어 다른 학문 분야나 학술 출판 형식(저널, 워크숍)의 대표성 제한

- **평가 규모의 제한**: RealScholarQuery의 50개 쿼리는 광범위한 통계적 분석에 상대적으로 작은 규모

- **도메인 일반화성**: AI 분야에 특화된 학습이 의료, 생물학, 공학 등 다른 분야에서의 성능 미검증

- **계산 비용 미분석**: 논문 읽기와 인용 확장을 반복하는 과정의 연산 비용과 응답 시간 미논의

- **후속 연구**: (1) 다양한 학문 분야로의 확장, (2) 더 큰 규모의 RealScholarQuery 벤치마크 구축, (3) 사용자 상호작용 기반 점진적 학습 메커니즘 개발, (4) 오래된 논문과 새로운 논문 사이의 시간적 불균형 해결

## Evaluation

- **Novelty**: 4.5/5
  - 에이전트 기반의 포괄적 논문 검색 개념은 창의적이나, LLM 에이전트 자체는 기존 기술의 응용

- **Technical Soundness**: 4.5/5
  - Session-level PPO, 희소 보상 처리 등 기술적으로 타당하나, 알고리즘의 이론적 분석 부족

- **Significance**: 4.5/5
  - 학술 연구 커뮤니티에 실질적 가치 제공하나, 산업적 영향은 제한적

- **Clarity**: 4/5
  - 전반적으로 명확하나 session-level PPO의 상세 구현 내용이 본문에 부족

- **Overall**: 4.25/5

**총평**: PaSa는 LLM 에이전트를 활용한 학술 논문 검색 문제의 창의적인 해법이며, 합성 데이터로의 학습이 실제 환경에서 우수한 성능을 달성하는 점이 주목할 만하다. 다만 데이터의 도메인 편향성과 평가 규모의 제한이 일반화 가능성에 대한 의문을 남긴다.

## Related Papers

- 🔄 다른 접근: [[papers/510_Llms_for_literature_review_Are_we_there_yet_arXiv_preprint_a/review]] — 학술 논문 검색을 위한 서로 다른 자동화 접근법을 제시합니다.
- 🔗 후속 연구: [[papers/087_Ai2_scholar_qa_Organized_literature_synthesis_with_attributi/review]] — 논문 검색이 조직적인 문헌 합성으로 확장됩니다.
- 🏛 기반 연구: [[papers/108_Ask_retrieve_summarize_A_modular_pipeline_for_scientific_lit/review]] — 모듈러 검색 파이프라인이 포괄적 논문 검색의 기반을 제공합니다.
- 🔄 다른 접근: [[papers/510_Llms_for_literature_review_Are_we_there_yet_arXiv_preprint_a/review]] — 문헌 리뷰 자동화를 위한 서로 다른 LLM 기반 접근법을 제시합니다.
