---
title: "042_Academicbrowse_Benchmarking_academic_browse_ability_of_llms"
authors:
  - "Junting Zhou"
  - "Wang Li"
  - "Yiyan Liao"
  - "Nengyuan Zhang"
  - "Tingjia Miao"
date: "2025"
doi: "10.48550/arXiv.2506.13784"
arxiv: ""
score: 4.2
essence: "본 논문은 LLM의 복잡한 학술 정보 검색 능력을 평가하기 위한 첫 번째 전문 벤치마크인 **ScholarSearch**를 제시한다. 기존의 학술 벤치마크(MMLU, GPQA)나 일반 웹 검색 벤치마크(BrowseComp)로는 충분하지 않은 깊이 있는 학술 연구 검색 능력을 측정한다."
tags:
  - "cat/Academic_Peer_Review_Automation"
  - "sub/AI_Peer_Review"
  - "topic/ai4s"
---

# ScholarSearch: Benchmarking Scholar Searching Ability of LLMs

> **저자**: Junting Zhou, Wang Li, Yiyan Liao, Nengyuan Zhang, Tingjia Miao, Zhihui Qi, Yuhan Wu, Tong Yang (Peking University) | **날짜**: 2025 | **DOI**: [10.48550/arXiv.2506.13784](https://doi.org/10.48550/arXiv.2506.13784)

---

## Essence

![Figure 1](figures/fig1.webp)
*ScholarSearch의 데이터 수집 파이프라인: 학생들이 수집한 데이터를 여러 LLM으로 필터링한 후 전문 검토팀이 유일성, 출처 접근성, 학술적 정확성을 검증*

본 논문은 LLM의 복잡한 학술 정보 검색 능력을 평가하기 위한 첫 번째 전문 벤치마크인 **ScholarSearch**를 제시한다. 기존의 학술 벤치마크(MMLU, GPQA)나 일반 웹 검색 벤치마크(BrowseComp)로는 충분하지 않은 깊이 있는 학술 연구 검색 능력을 측정한다.

## Motivation

- **Known**: 
  - 기존 학술 벤치마크(MMLU, SuperGPQA, GPQA)는 정적 지식과 추론 평가에 중점
  - 기존 웹 브라우징 벤치마크(BrowseComp, GAIA, WebVoyager)는 일반 웹 검색에 초점
  - Grok DeepSearch, Gemini Deep Research 등 깊이 있는 검색 기능의 등장

- **Gap**: 
  - 다단계 반복 검색이 필요한 학술 정보 검색 능력을 체계적으로 평가할 수 없음
  - 기존 벤치마크는 "Deep Research" 능력(복잡한 다단계 정보 검색)을 충분히 측정하지 못함

- **Why**: 
  - 과학 연구 분야는 빠르게 변화하며 최신 정보 접근이 필수적
  - LLM의 정적 지식 기반만으로는 최신 학술 발견을 따라갈 수 없음

- **Approach**: 
  - 단일 검색으로 답변할 수 없고, 최신 깊이 검색 모델도 실패하는 질문들로 구성된 벤치마크 구축
  - 학술 실용성, 높은 난이도, 간결한 평가, 광범위한 학문 분야 커버

## Achievement

![Figure 2](figures/fig2.webp)
*15개 이상의 학문 분야에 걸친 ScholarSearch의 균형잡힌 분포*

1. **223개의 고품질 학술 질문 데이터셋**: 
   - 15개 이상의 학문 분야를 포함
   - 각 질문이 평균 3회 이상의 깊이 검색 필요
   - Grok DeepSearch와 Gemini Deep Research도 해결 불가능한 수준의 난이도

2. **엄격한 데이터 수집 및 검증 메커니즘**:
   - 학부/대학원 학생 및 전문 검토팀의 다단계 검증
   - 유일성(uniqueness), 출처 접근성(source accessibility), 학술 정확성(academic correctness) 검증
   - 기존 벤치마크 대비 더 높은 투명성과 추적 가능성

## How

![Figure 3](figures/fig3.webp)
*ScholarSearch 데이터셋의 구조: 질문, 답변, 설명, 학문 분야*

**데이터 수집 프로세스:**

- **1단계: 질문 생성**
  - 학생 자원봉사자들이 공개 온라인 학술 자료에서 질문 수집
  - Grok 3의 표준 사고(thinking) 모드로 답변 불가능한 질문 선별

- **2단계: 난이도 검증**
  - Grok 3 DeepSearch와 Gemini 2.5 Pro Deep Research 중 최소 하나 이상이 실패하는 질문만 선정
  - 복잡한 멀티홉(multi-hop) 검색 능력 필요

- **3단계: 전문 검토팀 검증**
  - 답변의 유일성과 명확성 확인
  - 모든 참고 자료의 인터넷 접근성 확인
  - 학술적 가치와 정확성 검증

**평가 프레임워크:**
- 깊이 연구 조건: ① 답변이 LLM의 내부 지식에서 도출 불가능 (A ∉ K_LLM), ② 필수 정보가 외부 코퍼스에만 존재
- 별도의 판별기 모델을 사용한 자동화된 정답 검증

## Originality

- **학술 검색 특화 벤치마크**: 기존 일반 웹 검색 벤치마크와 달리 학술 연구의 특수한 요구사항(문헌 추적, 학술 데이터베이스 지원, 롱테일 지식 탐색, 학술적 엄밀성) 반영

- **엄격한 난이도 관리**: 현존 최고 수준의 깊이 검색 모델(Grok 3, Gemini 2.5 Pro)도 해결할 수 없는 질문으로 구성하여 벤치마크의 실질적 가치 보장

- **다단계 검증 메커니즘**: 학부/대학원생 수집 → LLM 필터링 → 전문팀 검증의 3단계 엄격한 프로세스로 데이터 품질 확보

- **투명성 강화**: 각 질문에 명확한 출처, 간략한 해결책 설명이 포함되어 감시(audit)와 검증이 용이함

- **광범위한 학문 커버**: 단일 분야가 아닌 15개 이상의 학문 분야를 포괄적으로 포함

## Limitation & Further Study

- **데이터셋 규모**: 223개의 질문은 BrowseComp(1,266개)에 비해 제한적이며, 추가 확장 필요

- **모델 평가의 선택성**: Grok 3와 Gemini 2.5 Pro 중심의 난이도 검증으로, 다른 깊이 검색 모델(OpenAI Deep Research, Alibaba WebDancer 등)에 대한 포괄성 부재

- **자동화된 평가의 한계**: 판별기 모델 기반 평가가 완전히 자동화되어 있으나, 복잡한 학술 답변의 미묘한 정확성 검증 부족 가능성

- **후속 연구**:
  - 추가 학문 분야 및 질문 확장으로 벤치마크 규모 증대
  - 다양한 깊이 검색 모델의 성능 종합 비교 분석
  - 검색 과정(reasoning trace)에 대한 상세한 분석과 평가 지표 개발
  - 한국어 등 다국어 버전 개발을 통한 국제화

## Evaluation

- **Novelty (창의성)**: 4.5/5
  - 학술 검색에 특화된 첫 벤치마크로 새로운 평가 영역 개척
  - 그러나 데이터 수집 방법론 자체는 기존 접근과 유사

- **Technical Soundness (기술적 건전성)**: 4/5
  - 엄격한 다단계 검증 프로세스로 데이터 품질 확보
  - 자동화된 평가 메커니즘은 효율적이나, 복잡한 학술 텍스트 평가의 신뢰성 개선 필요

- **Significance (중요성)**: 4.5/5
  - LLM의 실제 학술 연구 활용에 매우 실질적인 벤치마크
  - 향후 깊이 검색 기능 개발의 핵심 평가 기준으로 작용 가능

- **Clarity (명확성)**: 4/5
  - 전체 구조와 방법론이 명확하게 제시됨
  - 예시와 데이터셋 공개로 접근성 우수
  - 추가적인 정량적 통계(질문 길이, 난이도 분포 등) 분석 가능

- **Overall (종합 평가)**: 4.2/5

**총평**: ScholarSearch는 LLM의 학술 정보 검색 능력을 평가하기 위한 실질적이고 도전적인 벤치마크로서, 기존 벤치마크의 공백을 효과적으로 메운다. 데이터 수집의 엄격성과 학문 분야의 다양성이 강점이나, 규모 확장과 평가 메커니즘의 정교화를 통해 더욱 강력한 평가 도구로 발전할 수 있는 잠재력을 보유하고 있다.

## Related Papers

- 🔄 다른 접근: [[papers/041_Aaar-10_Assessing_ais_potential_to_assist_research/review]] — AI가 연구 지원에 미치는 영향을 평가하는 다른 접근법으로 학술 검색 능력과 함께 고려해야 한다.
- 🔗 후속 연구: [[papers/450_Knowledge_navigator_Llm-guided_browsing_framework_for_explor/review]] — LLM 기반 탐색적 검색 프레임워크로 ScholarSearch 벤치마크의 실제 활용 사례를 제시한다.
- 🏛 기반 연구: [[papers/602_Paperqa_Retrieval-augmented_generative_agent_for_scientific/review]] — 과학 문헌의 검색 증강 생성 에이전트로 학술 정보 검색 능력 평가의 기술적 기반을 제공한다.
- 🧪 응용 사례: [[papers/862_Using_artificial_intelligence_for_systematic_review_the_exam/review]] — 학술 검색 능력 벤치마킹이 AI 도구 기반 체계적 문헌고찰의 검색 단계 성능 평가에 활용된다.
- 🔗 후속 연구: [[papers/520_Massw_A_new_dataset_and_benchmark_tasks_for_ai-assisted_scie/review]] — 학자 검색 능력 벤치마킹을 과학 연구 워크플로우의 5가지 측면으로 확장한 포괄적인 AI 보조 연구 평가 체계입니다.
