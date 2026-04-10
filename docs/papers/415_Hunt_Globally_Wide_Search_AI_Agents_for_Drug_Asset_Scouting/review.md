---
title: "415_Hunt_Globally_Wide_Search_AI_Agents_for_Drug_Asset_Scouting"
authors:
  - "Alisa Vinogradova"
  - "Vlad Vinogradov"
  - "Luba Greenwood"
  - "Ilya Yasny"
  - "Dmitry Kobyzev"
date: "2026.02"
doi: "미제공"
arxiv: ""
score: 4.0
essence: "글로벌 제약 산업에서 미국 외 지역(특히 중국)의 신약 자산이 지역 언어, 비영어 채널을 통해 공개됨에 따라, 다국어 멀티에이전트 파이프라인과 완전성(Completeness) 중심의 벤치마크를 구축하고, 이를 기반으로 한 Bioptic Agent를 제안하여 기존 Deep Research AI를 크게 초과하는 성능을 달성했다."
tags:
  - "cat/AI-Powered_Scientific_Research_Frameworks"
  - "sub/Biomedical_Research_Agents"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Vinogradova et al._2026_Hunt Globally Wide Search AI Agents for Drug Asset Scouting in Investing, Business Development, and.pdf"
---

# Hunt Globally: Wide Search AI Agents for Drug Asset Scouting in Investing, Business Development, and Competitive Intelligence

> **저자**: Alisa Vinogradova, Vlad Vinogradov, Luba Greenwood, Ilya Yasny, Dmitry Kobyzev, Shoman Kasbekar, Kong Nguyen, Dmitrii Radkevich, Roman Doronin, Andrey Doronichev | **날짜**: 2026-02-16 | **DOI**: [미제공](https://doi.org/)

---

## Essence

글로벌 제약 산업에서 미국 외 지역(특히 중국)의 신약 자산이 지역 언어, 비영어 채널을 통해 공개됨에 따라, 다국어 멀티에이전트 파이프라인과 완전성(Completeness) 중심의 벤치마크를 구축하고, 이를 기반으로 한 Bioptic Agent를 제안하여 기존 Deep Research AI를 크게 초과하는 성능을 달성했다.

## Motivation

- **Known**: 대형 제약회사들은 외부 혁신을 통해 파이프라인을 유지·확장하며, 최근 특허 출원의 86.5%가 미국 외 지역에서 발생하고 중국이 약 48.2%를 차지함. 중국 내 신약 후보 약 1,200개 이상이 개발 중이며 전 세계 약물 개발의 ~30% 차지.

- **Gap**: 기존 Deep Research AI(Claude Opus, Gemini, OpenAI GPT, Perplexity 등)는 다국어·비영어 소스에 걸쳐 높은 재현율(Recall)을 달성하지 못하고 환각(Hallucination)을 생성함. 현재 벤치마크들(BrowseComp, ResearchRubrics, DRACO)은 깊이(Depth) 최적화에 편향되어 있으며 개방형 전체 집합 발견(Open-world set discovery)에서 완전성 평가 부족.

- **Why**: BD/S&E 활동에서 하나의 자산도 놓치면 수십억 달러 규모의 거래 기회 손실 위험. 따라서 속도와 완전성이 경쟁 우위의 핵심.

- **Approach**: (1) 비(非)영어 지역 뉴스 소스에서 역방향으로 자산을 채굴하여 방법 유도 편향을 감소, (2) 투자자/BD 전문가의 실제 스크리닝 쿼리를 사전 정보로 사용하여 벤치마크 쿼리 생성, (3) 완전성·비환각을 중심으로 설계한 트리 기반 자기학습 Bioptic Agent 제안.

## Achievement

![Figure 1](figures/fig1.webp)
*Figure 1: 자산 스카우팅의 품질-시간 트레이드오프. y축: F1-score (높을수록 좋음), x축: 벽시계 시간(로그 척도)*

1. **성능 초과 달성**: Bioptic Agent는 79.7% F1-score 달성
   - Claude Opus 4.6: 56.2% (↓23.5%p)
   - Gemini 3 Pro + Deep Research: 50.6% (↓29.1%p)
   - OpenAI GPT-5.2 Pro: 46.6% (↓33.1%p)
   - Perplexity Deep Research: 44.2% (↓35.5%p)
   - Exa Websets: 26.9% (↓52.8%p)

2. **계산량 확장성**: 추가 계산 투입에 따라 성능이 가파르게 향상되며, 이는 "더 많은 계산 = 더 나은 결과"를 뒷받침.

## How

![Figure 2](figures/fig2.webp)
*Figure 2: 완전성 벤치마크 구성 파이프라인. 상단: 자산 채굴 (Regional News Miner Agent, Attributes Enrichment Agent, Google Search Agent), 하단: 쿼리 생성 (실제 투자자 쿼리 클러스터링, Template Generator Agent, Query Generation Agent, Query Validator Agent)*

### 벤치마크 구성 방법론

- **역방향 설계 (Backward Construction)**: 쿼리에서 출발하는 대신, 지역 뉴스 소스에서 독립적으로 수집한 신약 자산을 시작점으로 설정하여 방법 유도 편향 감소.

- **Regional News Miner Agent**: 
  - 10개 지역 × 2~5개 고신호 바이오테크 뉴스 소스 큐레이션
  - ⟨region, language, source, stage⟩ 튜플 조합에 대해 라운드-로빈 스케줄 실행
  - OpenAI o4-mini-deep-research와 Gemini Deep Research를 병렬 실행하여 지역 언어 검색 수행

- **Attributes Enrichment Agent**: 채굴된 각 자산을 검증하고 증거 기반의 속성(attribute)으로 구조화.

- **Google Search Agent**: 영어 vs. 원어(Origin Language) 발견가능성 검사를 통해 "레이더 아래" 자산 우선순위 지정.

- **Query Generation Pipeline**:
  1. 실제 투자자/BD 쿼리를 의도(Intent)별로 클러스터링
  2. Template Generator Agent가 intent→templates 추출
  3. Query Generation Agent가 템플릿 조건부로 벤치마크 쿼리 생성
  4. Query Validator Agent + 인간 전문가 검증으로 각 쿼리-GT 쌍의 현실성 및 타당성 확보

### Bioptic Agent 설계

- **트리 기반 구조**: 탐색을 단일 진화 내러티브로 압축하지 않고, 후보 집합과 증거를 영속적 아티팩트로 보존.

- **동적 계산 할당**: 미탐색 분지(Under-explored branch)에 계산을 집중.

- **전문가 정렬 검증**: 비평가(Critic) 및 검증자(Validator) 신호를 사용하여 제약 위반과 커버리지 간격을 표면화하고, 이를 목표 지향적 하위 지시어(Targeted child directives)로 변환하여 지속적 재현율 성장 달성.

- **자가 수정의 한계 극복**: 일반적인 자가 수정 루프는 내부 일관성 개선에는 효과적이나, 최종 스크리닝 목표에 맞춤화된 검증자 없이는 작업 특화 제약을 침묵 중에 위반할 수 있음. 이를 전문가 정렬 비평자로 해결.

## Originality

- **역방향 벤치마크 설계**: 기존의 쿼리→자산 발견 방식 대신, 자산→쿼리 생성 역방향 설계로 방법 유도 편향 제거. 이는 완전성 평가에 혁신적 접근.

- **다국어 멀티에이전트 채굴 파이프라인**: 10개 지역·다양한 언어·개발 단계를 체계적으로 커버하는 규조식(Round-robin) 채굴 구조. 기존 영어 중심 접근을 명시적으로 탈피.

- **투자자 행동 기반 쿼리 생성**: 실제 BD/VC 전문가 스크리닝 쿼리를 사전 정보로 활용하여 벤치마크 현실성과 의도 분포 일치.

- **전문가 정렬 LLM-as-Judge 평가**: 엔티티 정규화(Alias resolution) 및 속성 추출에 전문가 의견을 보정한 LLM 판사 활용. 표준 인용-기반 평가와 차별화.

- **완전성 중심 에이전트 설계**: 합성 최적화 대신 후보 집합 보존, 계산 할당, 전문가 정렬 검증자를 통한 완전성·비환각 보장. 이는 기존 Deep Research 에이전트의 패러다임 전환.

## Limitation & Further Study

- **잔존 방법 유도 편향**: 뉴스 커버리지 편향이 여전히 존재할 수 있으며, 특정 지역·약물 형태·개발 단계에 대한 비균등한 표현 가능성. 파이프라인이 일부 완화하나 완전 제거 어려움.

- **채굴 소스의 언어/지역 제한**: 10개 지역, 2~5개 소스로 제한되어 있어, 미포함 지역(인도, 동남아시아, 아프리카 등)의 자산 발견 기회 제한.

- **벤치마크 규모 미명시**: 최종 벤치마크의 쿼리 수, GT 자산 총 개수, 지역별 분포가 구체적으로 제시되지 않음. 재현성 및 통계적 신뢰도 평가 어려움.

- **다중 언어 번역 오류**: 지역 언어 뉴스 채굴 및 쿼리 생성 과정에서 기계 번역 오류의 영향도 미분석.

- **실시간 업데이트 및 프로덕션 배포**: 논문은 벤치마크 평가에 중점이 있으며, 실제 BD 팀이 사용하는 프로덕션 시스템의 실시간 유지보수, 업데이트 메커니즘, 실제 거래 성공률 측정은 미포함.

**후속 연구**: 
- 추가 지역·언어 포함으로 글로벌 커버리지 확대
- 시간 흐름에 따른 벤치마크 동적 업데이트 메커니즘 개발
- 실제 거래 성공률, ROI 기반 성능 평가 도입
- 번역 오류의 영향 분석 및 다언어 견고성 강화


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4/5
- Significance: 4.5/5
- Clarity: 3.5/5
- Overall: 4/5

**총평**: 이 논문은 제약 산업의 글로벌화된 현실(비영어권 신약 자산의 증가)을 정확히 포착하여, 역방향 벤치마크 설계와 투자자 행동 기반 쿼리 생성이라는 독창적 방법론으로 완전성 중심의 평가 체계

## Related Papers

- 🔄 다른 접근: [[papers/177_Can_ai_agents_design_and_implement_drug_discovery_pipelines/review]] — 약물 자산 탐색에서 다국어 멀티에이전트와 AI 에이전트 기반 파이프라인 설계 접근법을 비교할 수 있습니다.
- 🔗 후속 연구: [[papers/651_RAG-Enhanced_Collaborative_LLM_Agents_for_Drug_Discovery/review]] — RAG 강화 협력 LLM 에이전트가 글로벌 약물 자산 스카우팅의 다국어 처리 능력을 향상시킬 수 있습니다.
- 🏛 기반 연구: [[papers/291_Drugclip_Contrastive_drug-disease_interaction_for_drug_repur/review]] — 대조 학습 기반 약물-질병 상호작용 모델이 투자 관점에서 약물 자산 평가의 방법론적 기반을 제공합니다.
