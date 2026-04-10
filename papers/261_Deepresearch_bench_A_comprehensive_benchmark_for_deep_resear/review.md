---
title: "261_Deepresearch_bench_A_comprehensive_benchmark_for_deep_resear"
authors:
  - "Mingxuan Du"
  - "Benfeng Xu"
  - "Chiwei Zhu"
  - "Xiaorui Wang"
  - "Zhendong Mao"
date: "2025"
doi: "미제공"
arxiv: ""
score: 4.0
essence: "본 논문은 대규모 언어모델 기반 깊이 있는 연구 에이전트(Deep Research Agents, DRAs)를 체계적으로 평가하기 위한 최초의 종합 벤치마크 DeepResearch Bench를 제시한다. 22개 분야의 박사 수준 연구 과제 100개와 두 가지 혁신적인 평가 방법론(RACE, FACT)을 통해 DRA의 보고서 생성 품질과 정보 검색 능력을 정량적으로 평가한다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/AI_Research_Ideation"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Du et al._2025_Deepresearch bench A comprehensive benchmark for deep research agents.pdf"
---

# DeepResearch Bench: A Comprehensive Benchmark for Deep Research Agents

> **저자**: Mingxuan Du, Benfeng Xu, Chiwei Zhu, Xiaorui Wang, Zhendong Mao | **날짜**: 2025 | **DOI**: [미제공](https://arxiv.org/abs/2506.11763)

---

## Essence

![Figure 1](figures/fig1.webp)
*그림 1: DeepResearch Bench에서의 에이전트 성능 개요. 좌측: 평가 차원별 생성된 보고서 품질 점수, 우측: 에이전트 인용 정확도 및 평균 효과적 인용 수*

본 논문은 대규모 언어모델 기반 깊이 있는 연구 에이전트(Deep Research Agents, DRAs)를 체계적으로 평가하기 위한 최초의 종합 벤치마크 DeepResearch Bench를 제시한다. 22개 분야의 박사 수준 연구 과제 100개와 두 가지 혁신적인 평가 방법론(RACE, FACT)을 통해 DRA의 보고서 생성 품질과 정보 검색 능력을 정량적으로 평가한다.

## Motivation

- **Known**: LLM 기반 에이전트는 웹 탐색, 정보 검색, 합성을 통해 분석가급 보고서를 생성하는 데 사용되고 있으며, 이들의 기능은 실제 사용자 수요를 반영해야 함

- **Gap**: 현존하는 벤치마크들은 웹 브라우징, 정보 검색, 생성 능력 등을 isolated하게 평가하며, 최종 보고서 품질 평가의 "ground truth" 설정이 거의 불가능해 DRA의 다층적 역량을 종합적으로 평가할 수 있는 전문화된 벤치마크가 부재

- **Why**: DRA의 내부 추론과 정보 검색 프로세스가 불투명하므로, 최종 생성 보고서가 성능 평가의 주요 인터페이스가 되며, 장문의 연구 보고서 품질 평가는 개방형 문제로 남아 있음

- **Approach**: (1) 96,147개 실제 사용자 쿼리를 기반으로 실제 수요 분포를 파악하고 비례적으로 100개 작업 구성, (2) 도메인 전문가가 정교하게 작성한 박사 수준 연구 과제 수집, (3) 참조 기반 적응형 평가 프레임워크(RACE)와 인용 신뢰성 평가 프레임워크(FACT) 개발

## Achievement

![Figure 2](figures/fig2.webp)
*그림 2: DeepResearch Bench 개요. (a) 분포 분석 및 데이터 수집 파이프라인, (b) RACE 프레임워크 개요, (c) FACT 프레임워크 개요*

1. **DeepResearch Bench 구축**: 실제 사용자 데이터 96,147개에 기반한 주제 분포 분석을 통해, 22개 분야에 걸친 박사 수준의 100개 연구 과제 벤치마크 구성 (영문 50개, 중문 50개)

2. **RACE 평가 프레임워크 개발**: 동적 가중치 생성, 적응형 기준 설정, 참조 기반 상대 점수 계산 등 세 단계를 통해 과제별 특성을 반영하고 인간 판단과 높은 일치도를 달성하는 보고서 품질 평가 방법론

3. **FACT 평가 프레임워크 개발**: 명제-URL 쌍 추출, 지원 판정, 인용 정확도(Citation Accuracy)와 평균 효과적 인용 수(Average Effective Citations) 계산을 통해 정보 검색 및 인용 신뢰성 평가

4. **인간 검증 연구**: 제안된 평가 방법론들이 인간 판단과의 일치도를 검증하는 광범위한 사용자 연구 수행

## How

![Figure 3](figures/fig3.webp)
*그림 3: 44,019개 필터링된 깊이 있는 연구 과제의 주제 분포*

### 데이터 수집 및 분포 분석
- 96,147개 실제 사용자 쿼리를 DeepSeek-V3-0324를 이용해 필터링하여 44,019개의 깊이 있는 연구 작업 식별
- WebOrganizer 분류체계를 기반으로 22개 주제 도메인 선택
- 실제 수요 분포를 유지하면서 리소스 제약을 고려해 100개 작업으로 압축

### RACE 평가 프레임워크
- **동적 가중치 및 적응형 기준 생성**: 4개 직교 차원(Comprehensiveness, Insight/Depth, Instruction-Following, Readability) 기반으로 T번 시행을 통해 과제별 차원 가중치 도출
- **참조 기반 채점**: 고품질 참조 보고서(Rref)를 기준으로 대상 보고서(Rtgt)를 비교 평가
- **종합 점수 계산**: 기준별 점수 → 차원별 점수 → 상대 점수 순으로 계산 (식 3: Sfinal(Rtgt) = Sint(Rtgt) / (Sint(Rtgt) + Sint(Rref)))

### FACT 평가 프레임워크
- **명제-URL 쌍 추출 및 중복 제거**: Judge LLM이 보고서에서 개별 진술과 인용 출처 추출
- **지원 판정**: Jina Reader API를 통해 웹페이지 텍스트 검색 후, 명제 지지 여부를 이진 판정
- **인용 지표 계산**: 인용 정확도(Citation Accuracy)와 평균 효과적 인용 수(Average Effective Citations) 산출

### 실험 설정
- Judge LLM: RACE는 Gemini-2.5-pro, FACT는 Gemini-2.5-flash 사용
- 참조 보고서: 2025년 4월 기준 Gemini-2.5-pro 기반 Deep Research 생성 보고서 선택

## Originality

- **최초의 전문화된 DRA 벤치마크**: 웹 검색, 정보 검색, 보고서 생성을 통합적으로 평가하는 최초의 종합 벤치마크 제시

- **실제 사용자 수요 기반 설계**: 96,147개의 실제 사용자 쿼리를 분석하여 벤치마크의 주제 분포를 결정함으로써 현실성 확보

- **참조 기반 적응형 평가 방법론**: 고정된 체크리스트나 정적 루브릭의 한계를 극복하고, 과제별 특성을 동적으로 반영하는 RACE 프레임워크 제안

- **상대 점수 계산 메커니즘**: 절대 점수 평가의 문제점(모델이 균일하게 높은 점수 부여)을 해결하기 위해 참조 보고서와의 비교를 통한 상대 점수 도입

- **정보 검색 신뢰성 평가**: 단순 인용 수 계산이 아닌, 인용 정확도와 효과적 인용 수를 통해 정보 검색의 질적 평가 가능

## Limitation & Further Study

- **참조 보고서 의존성**: RACE는 고품질 참조 보고서의 선택에 의존하며, 참조 보고서의 품질이 평가 결과에 영향을 미칠 수 있음

- **언어 및 도메인 제한**: 영문과 중문만 포함하고 있으며, 22개 분야로 제한된 주제 범위

- **자동화 평가의 한계**: Judge LLM 기반 평가가 인간 판정과 완전히 일치하지 않을 수 있으며, 특히 주관적인 "깊이"나 "인사이트" 판정에서 차이 가능

- **웹 콘텐츠 변동성**: FACT 평가에서 웹페이지 콘텐츠는 시간에 따라 변할 수 있어, 재현성이 제한될 수 있음

- **후속 연구 방향**: (1) 더 많은 언어와 도메인으로 벤치마크 확장, (2) 인간-LLM 하이브리드 평가 방법론 개발, (3) 다양한 DRA 아키텍처에 대한 평가, (4) 시간 경과에 따른 평가 프레임워크의 안정성 검증

## Evaluation

- **Novelty**: 4.5/5
  - DRA 평가를 위한 최초의 종합 벤치마크이며, 참조 기반 적응형 평가와 인용 신뢰성 평가는 혁신적임. 다만 개별 평가 기법들이 기존 LLM-as-a-Judge에 기반한 점은 약간의 제약

- **Technical Soundness**: 4/5
  - 동적 가중치 생성, 상대 점수 계산, 자동화된 인용 검증 등 기술적으로 견고함. 인간 검증 연구를 통해 신뢰성을 확보했으나, Judge LLM의 일관성에 대한 추가 분석 필요

- **Significance**: 4.5/5
  - DRA 개발 및 평가의 실질적 표준 제시 가능성이 높으며, 정보 검색 및 생성 능력 평가의 일반화 가능성 있음. 공개된 벤치마크와 평가 프레임워크가 커뮤니티에 실질적 기여할 수 있음

- **Clarity**: 4/5
  - 논문의 구조와 주요 개념이 명확하게 제시됨. 다만 RACE의 동적 가중치 생성 과정(T번 시행 및 평균화)과 Judge LLM의 정확한 프롬프트 구조에 대한 상세 설명 필요

- **Overall**: 4/5

**총평**: 본 논문은 빠르게 발전하는 LLM 기반 에이전트 분야에서 Deep Research Agents를 체계적으로 평가하기 위한 첫 번째 종합 벤치마크를 제시하며, 실제 사용자 데이터 기반 설계와 인간 판단과 일치하는 평가 프레임워크를 통해 높은 실용성과 신뢰성을 확보했다. 다만 평가 방법론의 일부가 기존 기법에 의존하고, 더 광범위한 언어 및 도메인 확장이 필요한 점이 보완되어야 한다.

## Related Papers

- 🧪 응용 사례: [[papers/669_Researchbench_Benchmarking_llms_in_scientific_discovery_via/review]] — 과학 발견에서 LLM 벤치마킹을 깊이 있는 연구 에이전트 평가에 적용
- 🔄 다른 접근: [[papers/724_SciHorizon_Benchmarking_AI-for-Science_Readiness_from_Scient/review]] — 과학 준비성 벤치마킹과 깊이 있는 연구 에이전트 평가의 다른 접근법
- 🏛 기반 연구: [[papers/552_Mmsci_A_dataset_for_graduate-level_multi-discipline_multimod/review]] — 대학원 수준 다중 분야 다중모달 데이터세트가 연구 벤치마크의 기반 제공
