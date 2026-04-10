---
title: "657_Reading_and_Reasoning_over_Chart_Images_for_Evidence-based_A"
authors:
  - "Mubashara Akhtar"
  - "Oana Cocarascu"
  - "Elena Simperl"
date: "2023"
doi: "10.48550/ARXIV.2301.11843"
arxiv: ""
score: 4.0
essence: "본 논문은 차트 이미지를 증거로 하여 텍스트 청구의 진위를 판정하는 새로운 자동 팩트-체킹(AFC) 과제를 제안하고, 이를 위한 첫 번째 모델인 ChartBERT를 소개한다. 텍스트, 구조, 시각 정보를 결합하여 차트 기반 주장 검증의 복잡한 추론 문제를 해결한다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Fact_Verification_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Akhtar et al._2023_Reading and Reasoning over Chart Images for Evidence-based Automated Fact-Checking.pdf"
---

# Reading and Reasoning over Chart Images for Evidence-based Automated Fact-Checking

> **저자**: Mubashara Akhtar, Oana Cocarascu, Elena Simperl | **날짜**: 2023 | **DOI**: [10.48550/ARXIV.2301.11843](https://doi.org/10.48550/ARXIV.2301.11843)

---

## Essence

![Figure 1](figures/fig1.webp)
*ChartFC 데이터셋의 예: 청구(claim)가 증거 차트로 지지되는 경우*

본 논문은 차트 이미지를 증거로 하여 텍스트 청구의 진위를 판정하는 새로운 자동 팩트-체킹(AFC) 과제를 제안하고, 이를 위한 첫 번째 모델인 ChartBERT를 소개한다. 텍스트, 구조, 시각 정보를 결합하여 차트 기반 주장 검증의 복잡한 추론 문제를 해결한다.

## Motivation

- **Known**: 자동 팩트-체킹 연구는 텍스트, 표(table) 증거를 중심으로 진행되었으며, 이미지 기반 AFC는 주로 조작되거나 가짜 이미지 탐지에 집중했다.

- **Gap**: 뉘앙스 있는 차트 왜곡(예: 잘못된 비교, 상관관계를 인과관계로 표현, 오도적 해석)을 감지하는 증거 기반 차트 팩트-체킹 과제가 부재하다.

- **Why**: 차트는 뉴스, 보고서, 소셜 미디어에서 광범위하게 사용되며(COVID-19 대시보드 예시), 차트의 설계 및 해석을 통한 오정보 확산은 심각한 문제이다.

- **Approach**: OCR 기반 텍스트 추출, 시퀀스 생성, 구조 임베딩이 강화된 BERT 아키텍처를 통해 통합적 차트 이해 모델을 제안하고, 15,886개 차트로 구성된 ChartFC 벤치마크 데이터셋을 구축한다.

## Achievement

![Figure 2](figures/fig2.webp)
*ChartBERT 아키텍처: 읽기(Reading), 시퀀스 생성, 인코딩 세 가지 구성 요소*

1. **신규 과제 및 데이터셋**: 차트 기반 팩트-체킹 과제를 최초 제안하고, 다양한 방향성, 색상, 배경을 갖춘 15,886개의 인간-작성 청구 기반 ChartFC 데이터셋 구축

2. **모델 성능**: ChartBERT가 63.8% 정확도를 달성하며, 75개 비전-언어(VL) 기준 모델(5개 비전 인코더, 3개 언어 인코더, 5개 융합 방법의 조합)을 체계적으로 평가하여 최상의 VL 기준선 초과

3. **포괄적 벤치마킹**: 최신 비전-언어 모델들의 한계를 명확히 하고, 모델 실패 패턴에 대한 상세 분석 제공

## How

![Figure 3](figures/fig3.webp)
*ChartBERT 입력 표현: 추출된 텍스트와 구조 임베딩(x, y 좌표, 라벨 임베딩)*

**1단계 - 텍스트 및 구조 정보 추출**
- Tesseract OCR 모델을 사용하여 차트 이미지에서 텍스트 영역 감지
- 각 텍스트 영역에 대해 토큰 시퀀스와 바운딩 박스(x, y, w, h) 추출

**2단계 - 텍스트 시퀀스 생성**
- **연결(Concatenation)**: 좌표 기반 정렬하여 텍스트 영역을 순차적으로 연결 (예: "usain bolt ; 1 ; andy stanfield ; 2")
- **템플릿**: 구조 정보를 활용한 3가지 템플릿으로 의미 있는 시퀀스 생성
  - tmp1: "entry [num]: [lx] is [textx]; [ly] is [texty]"
  - tmp2: "row [num]: [lx] is [textx]; [ly] is [texty]"
  - tmp3: "[lx] is [textx] when [ly] is [texty]"

**3단계 - 인코딩 및 분류**
- 청구(claim)와 추출된 시퀀스를 [SEP] 토큰으로 분리하고 [CLS]를 앞에 추가
- BERT 임베딩(토큰, 세그먼트, 위치)에 3개 구조 임베딩 추가:
  - x 좌표 임베딩: 텍스트의 수평 위치 정보
  - y 좌표 임베딩: 텍스트의 수직 위치 정보
  - 라벨 임베딩: x축/y축 라벨 여부 표시
- 768차원 표현을 완전 연결 계층과 시그모이드를 통해 지지(supports)/반박(refutes) 분류

**데이터셋 구축**
- TabFact 시드 데이터셋(117,784개 청구, 16,000개 위키피디아 표)에서 출발
- 문자열 매칭 및 레벤슈타인 거리 기반 부분 표 추출
- Python seaborn/matplotlib을 이용하여 다양한 변형의 차트 자동 생성

## Originality

- **최초 과제 제안**: 증거 기반 차트 팩트-체킹을 처음 정의하고 문제를 체계적으로 정립

- **구조화된 차트 표현**: OCR 정보(텍스트, 바운딩 박스)와 구조 임베딩을 결합하여 차트의 공간적 배치를 인코딩하는 혁신적 접근

- **포괄적 벤치마킹**: 75개 VL 기준 모델에 대한 철저한 비교 분석으로 시각-언어 모델의 한계 명확화

- **대규모 인간-검증 데이터셋**: TabFact를 기반으로 체계적으로 구축한 15,886개 규모의 고품질 벤치마크 데이터셋

## Limitation & Further Study

**한계점**
- 낮은 정확도(63.8%): 과제의 복잡성을 시사하며 상당한 개선 여지 존재
- 제한된 차트 유형: 막대 차트만 포함하며, 선 그래프, 파이 차트 등 다양한 차트 유형 미포함
- 합성 데이터(synthetic): 자동 생성된 차트로만 평가되어 실제 뉘스 기사의 차트와의 차이 존재
- OCR 의존성: OCR 오류의 영향을 분리 분석하지 않음
- 이진 분류: 청구의 검증 불가(Not Enough Info) 범주 미포함

**후속 연구 방향**
- 다양한 차트 유형(선 그래프, 파이 차트, 히트맵 등)으로 확대
- 실제 뉴스 기사 및 소셜 미디어의 자연 차트 적용
- 시각적 왜곡 감지(축 조작, 크기 왜곡 등) 통합
- 다중 증거 모달리티(텍스트 + 차트) 결합 검증
- 추론 과정 설명 가능성(explainability) 강화

## Evaluation

- **Novelty**: 4.5/5 — 차트 팩트-체킹이 새로운 과제이고 데이터셋도 신규이나, 모델 아키텍처 자체는 기존 기법의 조합

- **Technical Soundness**: 4/5 — 방법론은 타당하고 체계적 평가가 있으나, OCR 오류 영향 분석 부족 및 제한된 차트 유형 가정

- **Significance**: 4/5 — 오정보 문제의 실제 중요성 높고 벤치마크 기여도 크나, 낮은 성능과 합성 데이터 의존으로 실용성 제한

- **Clarity**: 4.5/5 — 전반적으로 명확하고 구조화된 설명이나, 템플릿 선택 기준 및 실패 사례 분석 더 상세 필요

- **Overall**: 4/5

**총평**: 차트 기반 팩트-체킹이라는 중요하고 미충족된 문제를 신규 제안하며 체계적 벤치마킹을 제공하는 의미 있는 연구이나, 63.8%의 정확도와 제한된 차트 유형으로 인해 실용적 영향은 아직 제한적이다. 해결해야 할 도전 과제가 많이 남아있는 초기 단계의 기초 연구로 평가된다.

## Related Papers

- 🔄 다른 접근: [[papers/711_Sciclaims_An_end-to-end_generative_system_for_biomedical_cla/review]] — 차트 기반 팩트 체킹과 생의학 주장 검증은 서로 다른 증거 유형을 활용하지만 동일한 증거 기반 검증 프레임워크를 공유한다.
- 🏛 기반 연구: [[papers/880_What_makes_medical_claims_un_verifiable_analyzing_entity_and/review]] — 의료 주장의 검증 가능성 분석이 차트 기반 증거를 활용한 의료 팩트 체킹에서 검증 가능한 주장을 식별하는 기준을 제공한다.
- 🔗 후속 연구: [[papers/315_Enhancing_chart-to-code_generation_in_multimodal_large_langu/review]] — 차트에서 코드 생성 능력을 차트 기반 팩트 체킹으로 확장하여 더 정교한 차트 정보 추출과 검증이 가능하다.
- 🏛 기반 연구: [[papers/783_Synchart_Synthesizing_charts_from_language_models/review]] — 차트 이미지 읽기 및 추론을 위한 증거 기반 답변 생성 기법이 SynChart의 QA 주석 생성에 이론적 기반을 제공한다.
- 🔄 다른 접근: [[papers/711_Sciclaims_An_end-to-end_generative_system_for_biomedical_cla/review]] — 생의학 주장 분석과 차트 기반 팩트 체킹은 모두 증거 기반 검증을 수행하지만 텍스트와 시각적 증거라는 다른 정보원을 활용한다.
- 🔗 후속 연구: [[papers/880_What_makes_medical_claims_un_verifiable_analyzing_entity_and/review]] — 의료 주장 검증 가능성 분석을 차트 기반 증거 활용으로 확장하여 더 다양한 증거 유형에 대한 검증 가능성 평가가 가능하다.
