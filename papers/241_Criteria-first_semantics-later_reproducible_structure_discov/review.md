---
title: "241_Criteria-first_semantics-later_reproducible_structure_discov"
authors:
  - "Jan Bumberger"
date: "2026.02"
doi: "미제공"
arxiv: ""
score: 4.3
essence: "본 논문은 이미지 기반 과학에서 지배적인 \"의미론-우선\" 분석 패러다임을 \"기준-우선, 의미론-후순위\" 패러다임으로 전환할 것을 제안한다. 구조 추출을 도메인 온톨로지로부터 독립적인 명시적 최적화 기준에 기반하여 먼저 수행하고, 의미론적 해석은 다운스트림에서 별도로 적용함으로써 장기 모니터링, 크로스-센서 비교, 개방형 발견을 가능하게 한다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/Materials_Discovery_Hypotheses"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Bumberger_2026_Criteria-first, semantics-later reproducible structure discovery in image-based sciences.pdf"
---

# Criteria-first, semantics-later: reproducible structure discovery in image-based sciences

> **저자**: Jan Bumberger | **날짜**: 2026-02-17 | **DOI**: [미제공](https://doi.org/)

---

## Essence

![Figure 1](figures/fig1.webp)
*Figure 1: The inversion. 상단: 도메인 특정 레이블 세트가 모델 훈련을 결정하는 의미론-우선(semantics-first) 파이프라인. 하단: 명시적 최적화 기준으로 재현 가능한 의미론-무관(semantics-free) 구조적 산물을 도출하는 기준-우선(criteria-first) 파이프라인*

본 논문은 이미지 기반 과학에서 지배적인 "의미론-우선" 분석 패러다임을 "기준-우선, 의미론-후순위" 패러다임으로 전환할 것을 제안한다. 구조 추출을 도메인 온톨로지로부터 독립적인 명시적 최적화 기준에 기반하여 먼저 수행하고, 의미론적 해석은 다운스트림에서 별도로 적용함으로써 장기 모니터링, 크로스-센서 비교, 개방형 발견을 가능하게 한다.

## Motivation

- **Known**: 
  - 자연과학 및 생명과학에서 이미지는 주요 측정 방식이 됨
  - 현재 지배적 패러다임은 의미론-우선: 도메인 특정 레이블 예측 또는 강제에 의존
  - 지도학습(supervised) 또는 약지도학습(weakly supervised) 파이프라인이 표준

- **Gap**: 
  - 의미론-우선 접근은 장기 모니터링, 크로스-센서 비교, 개방형 발견에서 체계적으로 실패
  - 도메인 온톨로지와 레이블 세트는 문화적, 제도적, 생태학적으로 표류(drift)함
  - 쿤(Kuhn)의 "정상과학" 단계 이후 범주 재정리 시 온톨로지 변화로 인한 업스트림 제약 발생

- **Why**: 
  - 의미론은 이미지의 고유 속성이 아니라 관찰 공동체의 해석 체계의 산물
  - 의미론적 약속을 너무 이르게 강제하면 구조 추출이 특정 온톨로지에 인질됨
  - 사이버네틱스(cybernetics)와 정보이론(information theory) 관점에서 정보와 의미는 분리 가능

- **Approach**: 
  - 명시적 최적화 기준(안정성, 스케일 일관성, 압축, 전역 일관성)에 기반한 의미론-무관 구조 추출을 우선 수행
  - 추출된 구조적 산물(partitions, graphs, fields, hierarchies)은 도메인 온톨로지와 무관하게 정의
  - 의미론적 매핑은 다운스트림에서 명시적으로 문서화된 형태로 적용

## Achievement

![Figure 1](figures/fig1.webp)
*기준-우선 파이프라인의 재현 가능한 구조적 계층(criterion-defined reproducible structural layer)은 도메인 온톨로지 변화에도 안정적 유지*

1. **재현성 보장 프레임워크**: 의미론-무관 구조 추출이 명시적 기준에만 의존하므로 도메인, 센서, 사이트 간 완전히 재현 가능한 분석 제공

2. **온톨로지 드리프트 극복**: 다운스트림 의미론 매핑을 분리함으로써 도메인 어휘 진화에도 업스트림 구조는 불변 유지 가능 → 수십 년 단위 모니터링 가능

3. **다중 해석 지원**: 동일한 구조적 산물에 대해 여러 도메인 온톨로지를 동시에 적용 가능하며, 상호 참조(crosswalks) 명시적 기록 가능

4. **크로스도메인 이전성**: 기준 자체가 도메인 무관적이므로 원격 센싱, 의료 영상, 생태 모니터링 등 이종 분야에 동일 원리 적용 가능

## How

- **사이버네틱스 기반**: 측정은 통신(communication)이며, 센서는 노이즈를 포함한 채널을 통해 메시지 전달 → 관찰은 수동적 복사가 아닌 구분(distinction) 작업

- **정보이론의 정보-의미 분리**: Shannon의 정보이론에서 통신은 제약 하의 불확실성 감소 → 기준-정의 구조(criterion-defined structure)에 원칙적 동기 부여

- **명시적 최적화 기준 활용**:
  - Otsu 임계값: 분리 기준 최대화
  - 스케일-공간(scale-space): 스케일 간 지속성으로 구조 정의
  - 변분 공식(variational formulation): 데이터 충실도 vs 경계 복잡도 트레이드오프
  - 그래프 분할(graph partitioning): 전역 절단 목적(global cut objectives) 최적화

- **계층적 분리 원리**:
  1. 업스트림: 명시적 기준 하에서 의미론-무관 구조적 산물 도출
  2. 다운스트림: 구조적 산물 → 도메인 온톨로지 명시적 매핑
  3. 다층 의미론: 다수의 경쟁적 해석 공존 가능, 모두 문서화

## Originality

- **패러다임 역전**: "의미론-우선"에서 "기준-우선, 의미론-후순위"로의 근본적 재배치 제안 (기존에는 거의 논의되지 않은 수준의 명시적 주장)

- **학제간 이론적 토대**: 사이버네틱스(Wiener, Ashby, von Foerster), 시스템 이론(Bertalanffy, Maturana), 정보이론(Shannon), 과학철학(Kuhn, Bowker & Star)을 통합

- **구조 vs 의미 분리의 원칙화**: 이전 연구에서 암묵적이었던 구분을 명시적 설계 원칙으로 승격

- **FAIR 디지털 객체화**: 구조적 산물을 장기 모니터링, 디지털 트윈, 재사용 가능한 FAIR(Findable, Accessible, Interoperable, Reusable) 디지털 자산으로 제안

- **온톨로지 드리프트 명시화**: Bowker & Star의 분류 체계 연구를 이미지 분석의 실제 과제로 처음 정면 적용

## Limitation & Further Study

- **구체적 알고리즘 부재**: 논문(제시 범위 내)에서 새로운 구체적 기준-우선 알고리즘을 제시하지 않음 → 기존 방법(Otsu, 스케일-공간, 그래프 분할 등)을 재해석하는 수준

- **검증 체계 미완성**: "클래스 정확도 이상의 검증" 필요성은 지적하나, 구조적 산물의 품질을 평가하는 대안적 메트릭 상세 정의 부재

- **실제 구현 사례 제한적**: 전체 15,000자 중 이론 및 철학적 논의가 대부분이며, 실제 이기종 도메인에서의 적용 사례 상세 분석 미흡

- **온톨로지 매핑 비용**: 다운스트림 의미론 매핑 자체가 얼마나 비용이 많이 드는지, 실제로 노동 절감이 되는지 정량적 분석 필요

- **후속 연구 방향**:
  - 기준-우선 프레임워크에 최적화된 새로운 신경망 아키텍처 개발
  - 다양한 도메인(원격 센싱, 의료 영상, 생태학, 재료 과학)에서 실제 구현 및 비교 사례 축적
  - 구조적 산물의 안정성·이전성을 정량적으로 평가하는 벤치마크 개발
  - 의미론 매핑 시 불일치 해소 및 다중 온톨로지 조화의 실무적 프로토콜 수립


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4/5
- Significance: 5/5
- Clarity: 3.5/5
- Overall: 4.3/5

**총평**: 본 논문은 이미지 기반 과학의 지배적 "의미론-우선" 패러다임의 근본적 한계를 사이버네틱스·정보이론·과학철학의 견고한 이론적 토대 위에서 비판하고, 명시적 최적화 기준으로 정의되는 "기준-우선, 의미론-후순위" 프레임워크를 강력하게 제안한다. 개념적 기여와 이론적 깊이는 뛰어나나, 구체적 알고리즘 개발과 다양한 도메인에서의 실증적 검증 사례 축적이 추후 필수적이다. 디지털 트윈, 장기 모니터링, 온톨로지 드리프트 극복이라는 절박한 과학적 요구와 정확히 맞아떨어지는 문제 설정으로 인해, 후속 구현 연구가 충분히 이루어진다면 이미지 과학 전반의 패러다임 전환을 견인할 수 있는 중요한 선언 논문이다.

## Related Papers

- 🏛 기반 연구: [[papers/695_Scaling_Deep_Learning_for_Materials_Discovery/review]] — 구조 발견 방법론이 대규모 재료 발견 결과의 해석과 검증에 필요하다.
- 🧪 응용 사례: [[papers/313_Enabling_ai_scientists_to_recognize_innovation_A_domain-agno/review]] — 도메인 독립적 구조 추출을 과학적 혁신 인식에 적용할 수 있다.
- 🔗 후속 연구: [[papers/547_Mllm-based_discovery_of_intrinsic_coordinates_and_governing/review]] — 기준 우선 구조 발견을 멀티모달 LLM 기반 내재 좌표 발견으로 확장한다.
- 🔗 후속 연구: [[papers/695_Scaling_Deep_Learning_for_Materials_Discovery/review]] — 재료 구조 발견을 이미지 기반 구조 추출 방법론으로 확장할 수 있다.
