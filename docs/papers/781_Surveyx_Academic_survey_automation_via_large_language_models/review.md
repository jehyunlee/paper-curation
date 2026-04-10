---
title: "781_Surveyx_Academic_survey_automation_via_large_language_models"
authors:
  - "Xun Liang"
  - "Jiawei Yang"
  - "Yezhaohui Wang"
  - "Chen Tang"
  - "Zifan Zheng"
date: "2025"
doi: "arXiv:2502.14776"
arxiv: ""
score: 4.0
essence: "arXiv에 매년 증가하는 학술 논문의 폭증 속에서, 대형언어모델(LLM)을 활용하여 체계적이고 고품질의 학술 서베이를 자동 생성하는 SurveyX 시스템을 제안한다. 이 시스템은 온라인 참고문헌 검색, AttributeTree 전처리 방법, 그리고 다단계 최적화를 통해 기존 자동 서베이 생성 시스템의 한계를 극복한다."
tags:
  - "cat/AI-Powered_Scientific_Research_Frameworks"
  - "sub/Scientific_Agent_Frameworks"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Liang et al._2025_Surveyx Academic survey automation via large language models.pdf"
---

# SurveyX: Academic survey automation via large language models

> **저자**: Xun Liang, Jiawei Yang, Yezhaohui Wang, Chen Tang, Zifan Zheng, Shichao Song, Zehao Lin, Yebin Yang, Simin Niu, Hanyu Wang, Bo Tang, Feiyu Xiong, Keming Mao, Zhiyu Li | **날짜**: 2025 | **DOI**: [arXiv:2502.14776](https://arxiv.org/abs/2502.14776)

---

## Essence

![Figure 2](figures/fig2.webp) 
*SurveyX의 전체 파이프라인: 준비 단계(Part 1: 논문 검색 및 자료 전처리)와 생성 단계(Part 2: 논문 작성 및 개선)로 구성*

arXiv에 매년 증가하는 학술 논문의 폭증 속에서, 대형언어모델(LLM)을 활용하여 체계적이고 고품질의 학술 서베이를 자동 생성하는 SurveyX 시스템을 제안한다. 이 시스템은 온라인 참고문헌 검색, AttributeTree 전처리 방법, 그리고 다단계 최적화를 통해 기존 자동 서베이 생성 시스템의 한계를 극복한다.

## Motivation

- **Known**: LLM은 우수한 텍스트 생성 능력과 광범위한 지식을 보유하고 있으며, 자동 서베이 생성에 활용 가능할 것으로 예상됨.

- **Gap**: 
  1. **기술적 문제**: (a) LLM의 내부 지식은 시대에 뒤떨어질 수 있고 부정확한 참고문헌 제공; (b) 컨텍스트 윈도우 제한으로 수백 개의 논문(약 10K 토큰/논문)을 포함할 수 없음
  2. **응용 문제**: (a) 최신 참고문헌 대량 검색 도구 부족; (b) 자동 생성 서베이 평가를 위한 통합 메트릭 및 벤치마크 부재

- **Why**: 학술 논문 수가 2022-2024년에 50% 이상 증가(186,339→285,174)했고, 2025년에는 368,292개에 도달할 것으로 예측되어, 수동 서베이 작성은 더 이상 지속 불가능.

- **Approach**: 인간의 글쓰기 과정에서 영감을 얻어 서베이 작성을 준비 단계와 생성 단계 두 가지로 분해하고, 온라인 검색, 지능형 전처리, 다단계 최적화를 통합한 통합 시스템 구축.

## Achievement

![Figure 1](figures/fig1.webp)
*arXiv 웹사이트의 연간 논문 수 추이(2010-2025): 2025년 제출 건수는 2010년의 5배 이상으로 예상*

1. **높은 품질의 콘텐츠**: 자동 생성 서베이의 콘텐츠 품질을 0.259 포인트 향상시켜 기존 시스템(AutoSurvey)을 능가함.

2. **향상된 인용 품질**: 참고문헌 품질을 1.76 포인트 개선하여 학술적 엄밀성 증대.

3. **인간 전문가 수준에 근접**: 다양한 평가 차원에서 인간 전문가의 성과에 근접한 성능 달성.

4. **풍부한 표현 형식**: 텍스트, 도표, 표, 그림 등 다양한 시각화 요소 포함으로 가독성 향상.

## How

![Figure 2](figures/fig2.webp)
*SurveyX 파이프라인의 상세 구성: Part 1은 11단계, Part 2는 11단계로 순차적으로 진행*

**준비 단계 (Preparation Phase)**:
- **키워드 확장 (1-4단계)**: 초기 주제에서 출발하여 관련 키워드를 다단계로 확장하여 검색 범위 극대화
- **온라인 검색 및 필터링 (1-5~1-9단계)**: 다중 라운드 키워드로 후보 논문 검색, 클러스터링, 재순위 지정, 지지도(Supportiveness) 분류로 고품질 논문만 선별
- **AttributeTree 구성 (1-10~1-11단계)**: 파싱 템플릿 이론 기반으로 논문의 핵심 속성을 트리 구조로 추출하여 정보 밀도 향상 및 토큰 효율성 증대

**생성 단계 (Generation Phase)**:
- **개요 생성 (2-1~2-4단계)**: Level 1 개요(주요 섹션) 생성 후, Level 2 개요(소단계) 생성, 최적화 단계에서 중복 제거 및 논리적 재정렬
- **콘텐츠 작성 (2-5~2-7단계)**: RAG(Retrieval Augmented Generation) 기법으로 관련 논문 재검색, 초안 생성 후 세밀한 재작성으로 품질 향상
- **멀티모달 모델링 (2-8~2-10단계)**: 논리 다이어그램, 표, 그림 생성 및 LaTeX 코드 변환으로 최종 PDF 생성

## Originality

- **효율적 온라인 검색 알고리즘**: 기존 AutoSurvey의 오프라인 검색 방식을 개선하여 최신 논문 접근 가능.

- **AttributeTree 전처리 방법**: 기존 제목과 초록만 활용하는 방식에서 논문의 본문 내용까지 구조화된 트리 형태로 추출하여 정보 밀도 및 컨텍스트 윈도우 효율성 대폭 향상.

- **개요 최적화 기법**: "분리-후-재정렬(separate-then-reorganize)" 전략으로 더욱 논리적이고 구조화된 개요 생성.

- **멀티모달 표현 확장**: 기존 텍스트 중심의 서베이에서 도표, 표, 그림 등을 자동 생성하여 가독성과 학술적 가치 향상.

- **확장된 평가 프레임워크**: 기존 AutoSurvey의 평가 메트릭을 보완하여 생성 서베이와 검색 논문의 품질을 더욱 포괄적으로 평가.

## Limitation & Further Study

- **한계**:
  1. 현재 평가는 주로 자동 메트릭에 의존하며, 인간 평가의 규모가 제한적일 수 있음.
  2. AttributeTree의 구성이 파싱 템플릿 이론에 기반하므로, 특정 학문 분야나 언어에 대한 일반화 가능성 미확인.
  3. 온라인 검색 알고리즘의 효율성이 검색 엔진의 성능과 가용성에 의존.
  4. 생성된 서베이의 학술적 엄밀성(특히 오류 인용)에 대한 더 심층적 분석 필요.

- **후속 연구**:
  1. 대규모 인간 평가를 통한 생성 서베이의 실제 학술적 가치 검증.
  2. 다국어 및 크로스 도메인 적용을 위한 AttributeTree 확장 연구.
  3. 생성된 콘텐츠의 사실성(factuality) 검증 메커니즘 개발.
  4. 전문가 피드백을 반영한 반복적 개선 루프 구축.

## Evaluation

- **Novelty**: 4/5
  - 온라인 검색, AttributeTree 전처리, 멀티모달 확장 등 여러 창의적 개선 제안. 다만 기본 구조는 AutoSurvey의 연장선상.

- **Technical Soundness**: 4/5
  - 체계적인 파이프라인 설계와 명확한 각 단계별 방법론 제시. 다만 AttributeTree의 수학적 형식화 및 이론적 근거가 다소 약함.

- **Significance**: 4/5
  - 학술 정보 폭증 시대에 매우 실용적이고 시의성 있는 연구. 자동 서베이 생성의 실제 적용 가능성 증대. 다만 평가 대상 분야의 다양성 확대 필요.

- **Clarity**: 4/5
  - 전체 파이프라인이 명확하게 시각화되어 있고, 각 단계별 설명이 충분. 다만 AttributeTree 구성의 구체적 사례 제시 부족.

- **Overall**: 4/5
  - 학술 문헌 합성 분야에서 현실적이고 효과적인 솔루션을 제시한 우수한 연구. 다만 더욱 철저한 이론적 기초와 광범위한 검증이 보완되면 더욱 강력한 기여가 될 것으로 예상.

**총평**: SurveyX는 LLM 기반 자동 서베이 생성의 실용적 한계를 체계적으로 해결하고, 온라인 검색, 지능형 전처리, 멀티모달 확장을 통해 기존 AutoSurvey 대비 명확한 성능 향상을 입증한 의미 있는 연구이나, 평가의 포괄성과 방법론의 이론적 깊이 강화가 필요하다.

## Related Papers

- 🏛 기반 연구: [[papers/520_Massw_A_new_dataset_and_benchmark_tasks_for_ai-assisted_scie/review]] — AI 보조 과학 작문을 위한 새로운 데이터셋과 벤치마크가 학술 서베이 자동화의 기초 자료를 제공합니다.
- 🔄 다른 접근: [[papers/374_Generating_a_structured_summary_of_numerous_academic_papers/review]] — 학술 서베이 생성에서 LLM 기반 자동화와 구조화된 요약 접근법을 비교할 수 있습니다.
- 🔗 후속 연구: [[papers/780_Surveyforge_On_the_outline_heuristics_memory-driven_generati/review]] — 메모리 기반 서베이 생성과 개요 휴리스틱이 SurveyX 시스템의 다단계 최적화를 보완할 수 있습니다.
