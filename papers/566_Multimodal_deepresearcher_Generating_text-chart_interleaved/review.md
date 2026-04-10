---
title: "566_Multimodal_deepresearcher_Generating_text-chart_interleaved"
authors:
  - "Zhaorui Yang"
  - "Bo Pan"
  - "Han Wang"
  - "Yiyao Wang"
  - "Xingyu Liu"
date: "2025"
doi: "미공개"
arxiv: ""
score: 4.2
essence: "본 논문은 대규모 언어 모델(LLM)을 활용하여 텍스트와 차트가 유기적으로 통합된 멀티모달 보고서를 자동으로 생성하는 시스템을 제안한다. 핵심 혁신은 시각화를 구조화된 텍스트 표현(FDV: Formal Description of Visualization)으로 변환하여 LLM의 맥락 학습(in-context learning)을 가능하게 한 점이다."
tags:
  - "cat/Cognitive_AI_Evaluation_and_Benchmarking"
  - "sub/Cognitive_LLM_Evaluation"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Yang et al._2025_Multimodal deepresearcher Generating text-chart interleaved reports from scratch with agentic frame.pdf"
---

# Multimodal deepresearcher: Generating text-chart interleaved reports from scratch with agentic framework

> **저자**: Zhaorui Yang, Bo Pan, Han Wang, Yiyao Wang, Xingyu Liu, Luoxuan Weng, Yingchaojie Feng, Haozhe Feng, Minfeng Zhu, Bo Zhang, Wei Chen | **날짜**: 2025 | **DOI**: [미공개](https://doi.org/)

---

## Essence

![Figure 2](figures/fig2.webp)
*Figure 2: Multimodal DeepResearcher의 프레임워크 - 4단계(조사, 예시 보고서 텍스트화, 계획, 멀티모달 보고서 생성)로 분해*

본 논문은 대규모 언어 모델(LLM)을 활용하여 텍스트와 차트가 유기적으로 통합된 멀티모달 보고서를 자동으로 생성하는 시스템을 제안한다. 핵심 혁신은 시각화를 구조화된 텍스트 표현(FDV: Formal Description of Visualization)으로 변환하여 LLM의 맥락 학습(in-context learning)을 가능하게 한 점이다.

## Motivation

- **Known**: 최근 LLM의 검색 강화 생성(RAG)과 추론 능력으로 심층 연구를 수행하고 종합 보고서를 생성할 수 있게 되었다. 그러나 기존 프레임워크(OpenAI o1, Google 2024 등)는 텍스트 기반 보고서에만 집중했다.

- **Gap**: 텍스트만으로 구성된 보고서는 가독성과 정보 전달 효율이 낮다. 인간 전문가는 정교하게 설계된 시각화를 텍스트와 통합하여 보고서를 작성하지만, 이러한 멀티모달 보고서의 자동 생성은 미탐사 영역이었다.

- **Why**: 시각화는 데이터 인사이트 전달, 패턴 인식, 관객 참여도 향상에 필수적이다. 그러나 LLM이 차트를 코드로 생성할 수 있더라도, 이를 텍스트와 효과적으로 통합하고 표현하는 방법이 부재했다.

- **Approach**: 그래픽 문법(Grammar of Graphics) 이론에 영감받은 FDV 표현 방식을 제안하여, 멀티모달 콘텐츠를 LLM이 처리 가능한 구조화된 텍스트로 변환한다.

## Achievement

![Figure 1](figures/fig1.webp)
*Figure 1: Multimodal DeepResearcher가 생성한 다양한 차트 예시 (면적도, 산키도, 대시보드, 수평막대그래프, 원형차트, 인포그래픽)*

1. **새로운 작업 정의 및 평가 체계**: 텍스트-차트 통합 보고서 생성이라는 새로운 작업을 정의하고, 100개의 다양한 주제와 10개의 전담 지표(보고서 수준 5개, 차트 수준 5개)를 포함한 MultimodalReportBench 벤치마크를 구축했다.

2. **우수한 성능**: Claude 3.7 Sonnet을 기반으로 기존 방법(DataNarrative) 대비 82% 승률을 달성하였으며, 자동 평가와 인간 평가 모두에서 일관된 우월성을 입증했다.

3. **복잡한 차트 생성**: 단순한 막대/선 차트를 넘어 산키도, 대시보드, 인포그래픽 등 다양하고 정교한 시각화를 생성할 수 있다.

## How

![Figure 3](figures/fig3.webp)
*Figure 3: FDV(Formal Description of Visualization)의 작동 원리 - 레이아웃, 척도, 데이터, 마크의 4가지 관점으로 시각화 캡처*

**4단계 에이전틱 프레임워크**:

1. **조사 단계(Researching)**
   - 주어진 주제에 대해 관련 키워드 생성
   - 반복적인 웹 검색과 추론을 통해 포괄적인 정보 수집
   - 각 정보와 참고문헌 추적

2. **예시 보고서 텍스트화(Exemplar Report Textualization)**
   - 인간 전문가의 멀티모달 보고서를 FDV로 구조화
   - FDV는 차트의 (1)전체 레이아웃, (2)플롯팅 척도, (3)데이터, (4)마크 표시의 4가지 관점 캡처
   - 맥락 학습 예시로 활용

3. **계획 단계(Planning)**
   - 보고서 내용 구조 및 시각화 스타일 가이드 수립
   - 일관된 미적 표현 보장

4. **멀티모달 보고서 생성(Multimodal Report Generation)**
   - 초안 작성(Drafting)
   - 차트 코드 생성(Coding)
   - 반복적 차트 개선(Refining)

## Originality

- **FDV 표현 방식의 창안**: 시각화를 구조화된 텍스트로 표현하여 LLM의 토큰 기반 처리를 가능하게 한 혁신적 접근법

- **멀티모달 보고서 자동 생성의 선제적 탐사**: 기존 연구는 개별 차트 생성이나 텍스트 기반 보고서 생성에 국한되었으나, 본 연구는 통합 생성을 최초로 시도

- **체계적 평가 프레임워크**: 보고서 수준(정확성, 관련성, 완성도, 참고문헌) 및 차트 수준(시각적 충실도, 데이터 정확성, 설계 효율성) 지표의 이원화

- **에이전틱 프레임워크 설계**: 조사, 텍스트화, 계획, 생성의 4단계 분해로 복잡한 멀티모달 작업을 체계적으로 관리

## Limitation & Further Study

- **데이터 다양성 제한**: 100개 주제 벤치마크가 실제 산업 응용의 다양한 도메인 요구를 충분히 반영하지 못할 가능성

- **차트 유형의 확장성**: FDV는 기존의 일반적 차트에 최적화되었으나, 새로운 또는 극도로 특수화된 시각화 형식에 대한 적응성이 미검증

- **생성 품질의 주관성**: 보고서 품질 평가의 일부가 인간 평가에 의존하므로, 평가 일관성 및 재현성 문제 가능

- **후속 연구 방향**:
  - 교차 언어(multilingual) 멀티모달 보고서 생성
  - 도메인 특화 시각화 생성 능력 강화
  - 인터랙티브 차트 생성 확대
  - 사용자 피드백 기반의 실시간 보고서 개선 메커니즘

## Evaluation

- **Novelty**: 4.5/5
  - 멀티모달 보고서 자동 생성이라는 새로운 작업 정의 (높음)
  - FDV 표현 방식의 창의성 (높음)
  - 다만 개별 기술(RAG, 에이전트)은 기존 기법의 조합

- **Technical Soundness**: 4/5
  - 4단계 프레임워크의 논리적 구조 (우수)
  - FDV 설계의 일관성 (우수)
  - 실험 방법론의 충실도 (양호)
  - 한계: 기존 모델 의존성으로 인한 성능 상한(ceiling effect) 가능성

- **Significance**: 4.5/5
  - 실제 산업(보고서 자동 생성, 데이터 저널리즘) 응용성 (높음)
  - 멀티모달 AI 생성 분야의 중요 선례 (높음)
  - 다만 벤치마크 규모(100개)가 대규모 실증에는 소규모일 수 있음

- **Clarity**: 4/5
  - 논문 구성 및 그림 설명이 명확함 (우수)
  - FDV 개념 설명이 체계적 (우수)
  - 프레임워크 상세 설명이 부분적으로 부록에 치중

- **Overall**: 4.2/5

**총평**: 본 논문은 LLM 기반 멀티모달 보고서 자동 생성이라는 중요한 미충족 문제를 처음 체계적으로 다루었으며, FDV라는 창의적인 표현 방식과 4단계 에이전틱 프레임워크로 강력한 성능(82% 승률)을 달성했다. 다만 평가 데이터의 규모 확장과 더 다양한 모델에 대한 검증이 필요하다.

## Related Papers

- 🏛 기반 연구: [[papers/199_ChartInstruct_Instruction_Tuning_for_Chart_Comprehension_and/review]] — 차트 이해와 생성을 위한 인스트럭션 튜닝은 멀티모달 보고서 생성에서 FDV 표현의 기반 기술입니다
- 🔄 다른 접근: [[papers/315_Enhancing_chart-to-code_generation_in_multimodal_large_langu/review]] — 멀티모달 대형 언어모델의 차트-코드 생성과 텍스트-차트 통합 보고서는 서로 다른 형태의 시각화 자동화 접근법입니다
- 🔗 후속 연구: [[papers/337_Figgen_Text_to_scientific_figure_generation/review]] — 과학적 그림 생성 기술은 텍스트와 차트 통합 보고서에서 시각화 요소를 더욱 풍부하게 만드는 확장 기술입니다
- 🧪 응용 사례: [[papers/691_S1-MMAlign_A_Large-Scale_Multi-Disciplinary_Dataset_for_Scie/review]] — 멀티모달 과학 연구 생성에 대규모 과학 이미지-텍스트 데이터셋을 적용할 수 있다
- 🔗 후속 연구: [[papers/627_Position_Multimodal_large_language_models_can_significantly/review]] — 멀티모달 과학적 추론 능력을 텍스트-차트 상호작용 연구 생성에 구체적으로 적용할 수 있다.
