---
title: "780_Surveyforge_On_the_outline_heuristics_memory-driven_generati"
authors:
  - "Xiangchao Yan"
  - "Shiyang Feng"
  - "Jiakang Yuan"
  - "Renqiu Xia"
  - "Bin Wang"
date: "2025"
doi: "N/A"
arxiv: ""
score: 4.2
essence: "본 논문은 자동화된 학술 설문지(Survey) 생성을 위한 SURVEYFORGE 프레임워크를 제안하며, 휴리스틱 기반 윤곽 생성, 메모리 기반 문헌 검색, 그리고 다차원 평가 벤치마크(SurveyBench)를 통해 AI 생성 설문과 인간 작성 설문 간의 품질 격차를 줄인다."
tags:
  - "cat/Scientific_Language_Processing_and_Visualization"
  - "sub/Scientific_Language_Models"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Yan et al._2025_Surveyforge On the outline heuristics, memory-driven generation, and multi-dimensional evaluation f.pdf"
---

# Surveyforge: On the outline heuristics, memory-driven generation, and multi-dimensional evaluation for automated survey writing

> **저자**: Xiangchao Yan, Shiyang Feng, Jiakang Yuan, Renqiu Xia, Bin Wang, Lei Bai, Bo Zhang | **날짜**: 2025 | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp)
*그림 1: AI 생성 설문과 인간 작성 설문의 비교. 윤곽(Outline)의 논리적 일관성 부족과 참고문헌(References)의 관련성 문제가 주요 과제임*

본 논문은 자동화된 학술 설문지(Survey) 생성을 위한 SURVEYFORGE 프레임워크를 제안하며, 휴리스틱 기반 윤곽 생성, 메모리 기반 문헌 검색, 그리고 다차원 평가 벤치마크(SurveyBench)를 통해 AI 생성 설문과 인간 작성 설문 간의 품질 격차를 줄인다.

## Motivation

- **Known**: LLM을 이용한 자동 설문지 생성(GPT-Researcher, AutoSurvey 등)이 연구의 효율성을 높이고 있음
  
- **Gap**: 
  1. AI 생성 설문의 윤곽이 논리적 일관성과 구조적 조직화를 결여함 (너무 광범위하거나 협소함)
  2. 핵심 참고문헌을 놓치고 무관한 논문을 인용하는 경향
  3. 설문 품질 평가가 전체 내용에만 초점을 두어 윤곽, 참고문헌, 내용의 세부적 분석이 부족함

- **Why**: 설문지는 광활한 학술문헌의 체계적 정리로서 연구 시작점 역할을 하므로, 논리적 구조와 신뢰성 있는 참고문헌이 필수적

- **Approach**: (1) 인간 작성 설문의 구조 패턴과 도메인 관련 논문을 활용한 휴리스틱 윤곽 생성, (2) Scholar Navigation Agent(SANA)의 메모리 기반 고품질 문헌 검색, (3) 다차원 평가 벤치마크 구성

## Achievement

![Figure 2](figures/fig2.webp)
*그림 2: SURVEYFORGE 개요. 윤곽 생성 단계와 콘텐츠 작성 단계 2단계로 구성되며, 휴리스틱 학습과 메모리 기반 Scholar Navigation Agent를 활용*

1. **구조적으로 우수한 윤곽 생성**: 휴리스틱 학습을 통해 인간 작성 설문의 논리적 깊이와 폭을 모방하여 균형잡힌 계층적 윤곽 생성

2. **고품질 참고문헌 검색**: SANA의 시간 인식 재순위 지정(Temporal-aware Reranking)으로 각 섹션에 최적의 핵심 논문 선별

3. **포괄적 평가 시스템**: SurveyBench를 통해 참고문헌 품질, 윤곽 품질, 콘텐츠 품질의 세 차원에서 정량적 평가 메트릭 제공

4. **AutoSurvey 대비 성능 개선**: 실험 결과 SURVEYFORGE가 선행 연구를 능가하는 다중 차원의 우수성 입증

## How

![Figure 4](figures/fig4.webp)
*그림 4: 기존 방법(좌)과 SURVEYFORGE(우)의 윤곽 생성 비교. SURVEYFORGE는 더 체계적이고 계층적인 구조 제시*

### 단계 1: 휴리스틱 윤곽 생성 (Heuristic Outline Generation)

- **이중 지식베이스 활용**:
  - Research Paper Database (Dr): 도메인의 최신 논문들 인코딩
  - Survey Outline Database (Da): 인간 작성 설문의 구조적 패턴 저장

- **Top-down 접근**:
  - 입력 주제(Topic)에 대한 RAG(Retrieval-Augmented Generation)로 관련 논문과 기존 설문의 윤곽 검색
  - LLM이 원본 설문의 구조 패턴을 학습하여 2-레벨 계층 윤곽(Outline Level-1, Level-2) 생성
  - 너비(Width)와 깊이(Depth) 밸런싱을 통해 과도한 세분화나 불충분한 커버리지 방지

### 단계 2: 메모리 기반 콘텐츠 생성 (Memory-Driven Content Generation)

- **Scholar Navigation Agent (SANA)**:
  - 각 서브섹션(Subsection)별로 문헌을 검색하기 위한 서브쿼리(Sub-queries) 생성
  - 논문 데이터베이스에서 섹션 수준의 청크(Chunk) 단위로 관련 논문의 제목, 초록, 콘텐츠 검색

- **시간 인식 재순위 지정 (Temporal-Aware Reranking)**:
  - 논문의 발표 시간, 인용도, 도메인 관련성을 종합적으로 고려하여 최고 품질의 참고문헌 우선순위 결정

- **병렬 콘텐츠 생성 (LLM-Parallel)**:
  - 각 섹션별로 병렬적으로 콘텐츠 생성으로 효율성 증대
  - 조합(Combination)과 정제(Refinement) 단계를 거쳐 일관성 있는 최종 설문 산출

### 단계 3: SurveyBench를 통한 다차원 평가

- **참고문헌 품질 (Reference Quality)**:
  - 인용된 논문이 실제로 관련성이 높고 영향력 있는지 평가
  - 관련성, 핵심성, 시간적 신뢰도 메트릭 포함

- **윤곽 품질 (Outline Quality)**:
  - 계층적 구조, 섹션 간 논리적 흐름, 커버리지 균형성 평가
  - 인간 작성 설문과의 구조적 유사도 비교

- **콘텐츠 품질 (Content Quality)**:
  - 텍스트의 일관성, 명확성, 학술적 엄밀성 평가
  - 인간 작성 설문과의 Win-rate 비교

## Originality

- **휴리스틱 윤곽 생성의 혁신성**: 단순한 프롬프트 기반 접근에서 벗어나 인간 설문의 구조적 패턴을 학습하고 도메인 지식을 결합하는 점진적 접근법 제시

- **메모리 기반 Scholar Navigation Agent**: 각 섹션별 맞춤형 검색 및 시간 인식 재순위 지정으로 기존의 일괄적 검색 방식 개선

- **다차원 평가 벤치마크의 도입**: 참고문헌, 윤곽, 콘텐츠의 세 가지 차원을 정량적으로 평가할 수 있는 체계적 벤치마크(SurveyBench) 구축으로 평가의 객관성과 세분성 확보

- **공개 벤치마크와 재현성**: 100개의 인간 작성 설문을 포함하는 SurveyBench를 공개하여 커뮤니티의 재현성과 지속적 개선 가능성 제고

## Limitation & Further Study

- **데이터베이스 규모의 제한**: 현재 arXiv 기반의 논문 데이터베이스는 특정 분야(AI, CS)에 편향되어 있으며, 다른 학문 분야로의 확장 가능성 검토 필요

- **참고문헌 검색의 정확도**: 시간 인식 재순위 지정이 최신 논문을 과도하게 우선순위할 가능성이 있으므로, 다양한 분야의 인용 패턴과 중요도 가중치 재조정 필요

- **계산 효율성**: 병렬 콘텐츠 생성에도 불구하고 대규모 설문 생성 시 계산 비용이 높을 수 있으므로, 프롬프트 최적화 및 모델 경량화 연구 필요

- **주관적 평가 메트릭의 보완**: 현재 SurveyBench의 일부 평가(콘텐츠 품질)는 LLM 기반이므로, 인간 평가자를 포함한 혼합 평가 체계 구축 필요

- **후속 연구 방향**:
  - 다국어 및 다학문 분야로의 확장
  - 동적 업데이트: 새로운 논문 발표에 따른 설문 자동 갱신 메커니즘
  - 인간-AI 협업 모델: 연구자의 수정 피드백을 통한 지속적 학습 및 개선

## Evaluation

- **Novelty (독창성)**: 4/5
  - 휴리스틱 윤곽 생성과 메모리 기반 Scholar Navigation Agent의 결합은 참신하나, 개별 기술 요소들(RAG, 재순위 지정 등)은 기존 방법의 응용

- **Technical Soundness (기술적 건전성)**: 4.5/5
  - 2단계 프레임워크의 설계는 논리적이고 실증적 검증이 충분하나, 시간 인식 재순위 지정의 가중치 결정 기준이 명확하지 않은 부분 있음

- **Significance (학술적 의미)**: 4/5
  - 자동화된 설문지 생성의 실질적 개선을 제시하며, SurveyBench는 향후 연구의 표준 평가 도구로 기여할 수 있음
  - 다만 실제 연구자의 설문 작성 시간 단축 효과에 대한 사용성 평가 부재

- **Clarity (명확성)**: 4.5/5
  - 논문의 구조와 방법론 설명이 명확하며, Figure 2의 전체 파이프라인 시각화가 이해를 돕는 반면, 알고리즘 1의 구체적 구현 세부사항이 일부 생략됨

- **Overall (종합)**: 4.2/5

**총평**: 본 논문은 LLM 기반 설문지 자동 생성의 실질적인 문제점(구조적 결함, 참고문헌 부정확성)을 명확히 파악하고, 휴리스틱 윤곽 생성과 메모리 기반 문헌 검색을 통해 실효성 있는 해결책을 제시하는 의미 있는 연구이다. 특히 다차원 평가 벤치마크(SurveyBench)의 구축은 해당 분야의 평가 표준화에 기여할 수 있는 강점이다.

## Related Papers

- 🧪 응용 사례: [[papers/367_Galactica_A_Large_Language_Model_for_Science/review]] — 과학 지식에 특화된 Galactica의 능력을 자동 설문지 생성이라는 구체적 작업에 활용
- 🔗 후속 연구: [[papers/672_ResearchGym_Evaluating_Language_Model_Agents_on_Real-World_A/review]] — AI 연구 평가에서 자동화된 문헌 검토와 설문 생성 능력을 체계적으로 평가
- 🔄 다른 접근: [[papers/519_MARG_Multi-Agent_Review_Generation_for_Scientific_Papers/review]] — 다중 에이전트 리뷰 생성과 달리 단일 프레임워크로 포괄적 설문지를 생성하는 접근
- 🏛 기반 연구: [[papers/732_Scireviewgen_a_large-scale_dataset_for_automatic_literature/review]] — 대규모 문헌 리뷰 데이터셋 구축 방법론을 자동 설문지 생성에 적용한 기반
- 🔄 다른 접근: [[papers/374_Generating_a_structured_summary_of_numerous_academic_papers/review]] — 메모리 기반 설문 생성 프레임워크로 대규모 학술 논문 요약과 다른 접근 방식의 구조화된 요약을 제공한다.
- 🔗 후속 연구: [[papers/781_Surveyx_Academic_survey_automation_via_large_language_models/review]] — 메모리 기반 서베이 생성과 개요 휴리스틱이 SurveyX 시스템의 다단계 최적화를 보완할 수 있습니다.
- 🧪 응용 사례: [[papers/367_Galactica_A_Large_Language_Model_for_Science/review]] — 과학 문헌 생성에 특화된 Galactica의 능력을 자동 설문지 생성에 활용하는 응용
