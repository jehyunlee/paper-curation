---
title: "607_Patterns_and_purposes_A_cross-journal_analysis_of_ai_tool_us"
authors:
  - "Ziyang Xu"
date: "2025"
doi: "미제공"
arxiv: ""
score: 3.75
essence: "본 연구는 엘스비어(Elsevier) 학술지 27개 범주의 8,859개 논문에서 AI 사용 선언문 168개를 분석하여, 학술 저술에서 ChatGPT가 77% 사용되며 가독성 개선(51%)과 문법 검사(22%)가 주요 목적임을 규명했다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Academic_Writing_Diversity"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Xu_2025_Patterns and purposes A cross-journal analysis of ai tool usage in academic writing.pdf"
---

# Patterns and purposes: A cross-journal analysis of ai tool usage in academic writing

> **저자**: Ziyang Xu | **날짜**: 2025 | **DOI**: [미제공](https://doi.org/)

---

## Essence

본 연구는 엘스비어(Elsevier) 학술지 27개 범주의 8,859개 논문에서 AI 사용 선언문 168개를 분석하여, 학술 저술에서 ChatGPT가 77% 사용되며 가독성 개선(51%)과 문법 검사(22%)가 주요 목적임을 규명했다.

## Motivation

- **Known**: 생성형 AI(Generative AI)의 발전으로 ChatGPT 등이 학술 저술 과정에서 광범위하게 활용되고 있으며, COPE, ICMJE 등 주요 학술 출판 기관들이 AI 사용 공개 지침을 도입하고 있다.

- **Gap**: 현존하는 논의들은 주로 AI 사용의 윤리적 쟁점(저자성, 데이터 프라이버시, 할루시네이션, 편향성)에 집중되어 있으나, 연구자들이 실제로 **AI를 어떤 목적으로 사용하는지**, 그리고 **저자의 배경(모국어 여부, 국제 협력 팀)에 따라 사용 패턴이 어떻게 다른지에 대한 실증적 분석이 부족**하다.

- **Why**: 학술지 편집 정책 수립, AI 사용의 윤리적·사회적 함의 논의, 저자들의 실제 AI 활용 동기 파악을 위해서는 대규모 실증 데이터가 필수적이다.

- **Approach**: 엘스비어 공개 접근(Open Access) 학술지의 2024년 발표 논문들에서 AI 사용 선언문을 추출하여, 내용 분석(content analysis), 통계 분석, 텍스트 마이닝을 결합한 혼합 방법론으로 분석한다.

## Achievement

![Figure 2](figures/fig2.webp)
*AI 도구 사용 분포: ChatGPT 77% 압도적 우위*

![Figure 3](figures/fig3.webp)
*AI 도구 사용 목적 분포: 가독성 개선(51%), 문법 검사(22%)*

1. **AI 도구 사용의 불균형**: ChatGPT가 전체 AI 도구 사용의 77%를 차지하며, Grammarly, Claude, 기타 LLM들과 비교해 압도적 우위를 보인다.

2. **모국어 여부와 국제 협력에 따른 유의미한 차이**: 
   - 비영어 원어민 저자 vs. 영어 원어민: p = 0.0483 (유의)
   - 국제 협력팀 vs. 단일국가팀: p = 0.0012 (고도로 유의)
   - 특히 비영어 원어민과 국제 협력팀이 더 빈번하게 AI를 활용하는 경향

3. **AI 활용 목적의 집중화**: 가독성 개선(51%)과 문법 검사(22%)에 사용이 집중되어 있으며, 콘텐츠 생성, 아이디어 생성 등 고차원적 활용은 상대적으로 낮다.

4. **학제별 편차**: Digital Business(80.00‰), Engineering(73.17‰), Earth and Planetary Sciences(60.97‰) 등 기술 중심 분야에서 AI 선언 빈도가 높고, Medicine(1.48‰), Mathematics(2.40‰) 등에서는 낮다.

## How

![Figure 1](figures/fig1.webp)
*데이터 분석 플로우차트: 내용 분석, 정량 분석, 네트워크 분석의 통합*

- **자료 수집**: 27개 Scopus 주요 학과 분류별 최고 인용도(CiteScore) 엘스비어 저널 선정, 2024년 발표 논문 8,859개 중 AI 선언문 포함 168개 추출

- **내용 분석(Content Analysis)**: 
  - 코딩 틀(coding framework) 설계를 통해 AI 도구 유형(ChatGPT, Grammarly 등)과 활용 과제(문법 검사, 문장 다듬기, 콘텐츠 생성 등) 범주화
  - 제1저자의 모국어 여부(0/1), 팀 구성(국제/비국제)을 이진 코딩

- **정량 분석**:
  - 기술 통계: 도구별, 목적별 빈도 및 백분율 계산
  - 변수 연관성 분석: Fisher-Freeman-Halton 검정으로 범주형 변수 간 유의성 검증

- **텍스트 마이닝**:
  - 템플릿 제거, 토큰화(tokenization) 등 전처리
  - 단어 빈도(word frequency), 이중 단어(bigram) 분석
  - 네트워크 구성 및 관계 추출을 통해 AI 사용 목적의 의미적 연결 구조 파악

## Originality

- **최초의 대규모 실증 분석**: 단순한 정책 논의 수준을 넘어 168개 논문의 실제 AI 선언문 데이터를 체계적으로 분석한 첫 대규모 실증 연구

- **저자 배경 변수의 통계적 검증**: 모국어 여부와 국제 협력 팀이라는 구체적 변수로 AI 사용 패턴의 차이를 통계 검정(p값 제시)으로 입증

- **학제 간 비교 분석**: 27개 학과 분류별로 AI 선언 빈도를 측정하여 분야별 편차를 정량화

- **혼합 방법론의 통합 적용**: 내용 분석, 통계 검정, 텍스트 마이닝을 결합하여 다층적 통찰 제공

## Limitation & Further Study

- **샘플 편향**: 
  - 엘스비어의 공개 접근 저널로 제한되어 다른 주요 출판사(Springer, Taylor & Francis 등)의 저널 미포함
  - 2024년 1년 데이터만 분석하여 시계열 변화 추적 불가
  - 전체 8,859개 논문 중 168개(1.89%)만 AI 선언문 보유로, AI 미선언 논문의 실제 사용 비율은 파악 불가

- **분석의 표면성**: 
  - AI 선언문 텍스트만 분석하여 저자의 실제 AI 사용 의도, 만족도, 편익 등 주관적 차원 미해명
  - "가독성 개선"이 구체적으로 무엇을 의미하는지(문장 구조 단순화? 논리 흐름 개선? 용어 통일?)에 대한 세부 분류 부재

- **저자 배경 정보의 한계**: 
  - 제1저자만 분석하여 저자팀 전체의 언어 배경 미반영
  - 공식 저자 정보만 활용하여 이주자, 다언어 사용자 등 실제 언어 환경 파악 어려움

- **후속 연구 제언**:
  - 타 출판사 저널 및 다년도 데이터 포함으로 발견의 일반화가능성 확대
  - 저자 면담, 설문 조사를 통해 AI 사용의 실제 동기, 교육 수준별 차이, 학제별 규범 차이 규명
  - AI 선언문에 명시되지 않은 AI 사용 여부 추정(detection methods) 연구
  - 저널 정책 변화가 AI 선언 빈도에 미치는 영향 분석


## Evaluation

- Novelty: 4/5
- Technical Soundness: 3.5/5
- Significance: 4/5
- Clarity: 3.5/5
- Overall: 3.75/5

**총평**: 본 연구는 학술 저술에서의 AI 도구 실제 사용 패턴을 대규모로 규명한 시의적절한 실증 연구로, 저자 배경에 따른 차이를 통계적으로 입증함으로써 정책 입안자들에게 실질적 근거를 제공한다. 다만 샘플 제한, 선언문 기반 분석의 한계, 세부 개념화 부족 등을 보완할 필요가 있다.

## Related Papers

- 🔗 후속 연구: [[papers/284_Does_writing_with_language_models_reduce_content_diversity_a/review]] — AI 도구 사용이 콘텐츠 다양성에 미치는 영향을 학술 저술의 구체적 맥락에서 실증한다
- 🏛 기반 연구: [[papers/414_Human-llm_coevolution_Evidence_from_academic_writing/review]] — 인간-LLM 협력적 글쓰기의 진화 과정에서 AI 도구 사용 패턴의 기초 데이터를 제공한다
- 🧪 응용 사례: [[papers/889_Xtragpt_Llms_for_human-ai_collaboration_on_controllable_acad/review]] — 학술적 글쓰기에서 AI 도구의 실제 활용 방식과 목적을 구체적으로 분석한다
- 🧪 응용 사례: [[papers/508_LLMs_as_Research_Tools_A_Large_Scale_Survey_of_Researchers_U/review]] — AI 도구 사용의 패턴과 목적에 대한 학술지 간 분석이 연구자 LLM 사용 조사의 실제 적용 결과이다.
