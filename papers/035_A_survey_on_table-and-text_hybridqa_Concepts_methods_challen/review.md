---
title: "035_A_survey_on_table-and-text_hybridqa_Concepts_methods_challen"
authors:
  - "Dingzirui Wang"
  - "Longxu Dou"
  - "Wanxiang Che"
date: "2022"
doi: "N/A"
arxiv: ""
score: 4.25
essence: "테이블과 텍스트 혼합 질의응답(Table-and-Text Hybrid Question Answering, HybridQA)은 이질적 데이터를 결합하여 답변을 생성하는 도전적인 NLP 과제이며, 본 논문은 현재까지의 벤치마크, 방법론, 핵심 과제, 향후 방향을 체계적으로 정리한 최초의 포괄적 설문이다."
tags:
  - "cat/Cognitive_AI_Evaluation_and_Benchmarking"
  - "sub/Multi-Hop_Reasoning_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Wang et al._2022_A survey on table-and-text hybridqa Concepts, methods, challenges and future directions.pdf"
---

# A survey on table-and-text hybridqa: Concepts, methods, challenges and future directions

> **저자**: Dingzirui Wang, Longxu Dou, Wanxiang Che | **날짜**: 2022 | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp) *HybridQA 과제의 종합 요약*

테이블과 텍스트 혼합 질의응답(Table-and-Text Hybrid Question Answering, HybridQA)은 이질적 데이터를 결합하여 답변을 생성하는 도전적인 NLP 과제이며, 본 논문은 현재까지의 벤치마크, 방법론, 핵심 과제, 향후 방향을 체계적으로 정리한 최초의 포괄적 설문이다.

## Motivation

- **Known**: 텍스트 기반 QA와 테이블 기반 QA는 각각 독립적으로 광범위하게 연구되어 왔으며, 수치 추론을 요구하는 금융·과학 분야에서 활발히 활용되고 있음
  
- **Gap**: HybridQA 분야가 급속도로 발전하고 있음에도 불구하고, 벤치마크·방법론·과제를 포괄적으로 정리한 설문이 부재함
  
- **Why**: 이질적 증거(텍스트와 테이블) 모델링, 다중 홉 추론, 효율적 검색 등 HybridQA 특화 과제들이 존재하며, 이를 체계적으로 분석할 필요가 있음
  
- **Approach**: 7개 주요 벤치마크 분석, 검색기-독자(Retriever-Reader) 구조를 기반으로 한 방법론 분류, 4대 핵심 과제 도출, 4가지 향후 방향 제시

## Achievement

![Figure 2](figures/fig2.webp) *HybridQA의 예시 (테이블과 텍스트 통합 추론)*

1. **첫 번째 포괄적 설문**: HybridQA 관련 벤치마크(HybridQA, OTT-QA, FinQA, TAT-QA, TAT-HQA, MultiHiertt, GeoTSQA), 방법론, 과제를 통합적으로 정리

2. **체계적 비교 분석**: 기존 시스템의 장단점을 명확히 하는 합리적 비교 프레임워크 제시 (Table 1에서 7개 벤치마크를 6가지 차원으로 비교)

3. **과제 심층 분석**: 
   - 검색 효율성과 효과성(Retrieval Effectiveness and Efficiency)
   - 테이블 셀 위치 인식(Cell Location of Tabular Evidence)
   - 이질적 증거 관계 모델링(Relation Modeling of Heterogeneous Evidence)
   - 다중 홉 추론(Multi-Hop Reasoning)

## How

- **검색기(Retriever) 설계**:
  - 개별 검색: 셀 기반(POINTR, MT2Net), 행 기반(DuRePa)
  - 결합 검색: 셀 기반(Hybrider, CARP, CORE, MuGER), 행 기반(MITQA, DocHopper, TTGen, OTTeR), 테이블 기반(FR+CBR)
  - Pre-trained Language Model(PLM) 활용, 이질적 증거 링킹 여부에 따라 차별화

- **독자(Reader) 개선**:
  - 인코더 개선: 관계 모델링(DEHG, RegHNT), 지식 주입(TTGen, KIQA)
  - 디코더 개선: 답변 특화(TagOp, FinMath, MT2Net, L2I), 다중 홉(DocHopper, CARP, CORE, ReasonFuse)
  - 데이터 조작: 사전학습(PoEt), 형식 변환(TaCube, DuRePa, FinQANet, UniRPG)

- **벤치마크 특성**:
  - 스팬 기반 답변(HybridQA, OTT-QA)에서 수식 기반 답변(FinQA, TAT-QA)으로 진화
  - 개방형 검색(OTT-QA: 5백만 개 후보)에서 제한된 컨텍스트(TAT-QA: 5개 텍스트)로 다양화
  - 계층적 테이블(MultiHiertt), 가설 질문(TAT-HQA), 시나리오 기반(GeoTSQA) 등 특화 벤치마크 확장

## Originality

- **최초성**: HybridQA 전체 생태계를 다루는 첫 번째 설문 논문으로, 벤치마크-방법론-과제-방향을 통합 분석

- **분류 체계의 명확성**: Retriever-Reader 구조와 세부 기준(셀/행/테이블 기반, 개별/결합 검색)으로 기존 방법들을 체계적으로 분류

- **과제 추상화의 일반성**: 서로 다른 벤치마크(HybridQA vs TAT-QA)의 공통 핵심 과제를 4가지로 추상화하여 분야 전체의 도전과제 도출

- **향후 방향의 실증성**: 관계 모델링 개선, 도메인 특화 지식 주입, 다목적 데이터 증강, 컨텍스트 풍부화 등 기존 과제에서 효과가 검증된 방향 제시

## Limitation & Further Study

- **제한사항**:
  - 논문이 2022년 초 작성되어, 그 이후 BERT/GPT 기반 대규모 언어모델(LLM)의 폭발적 발전이 반영되지 않음
  - 다중 모드(멀티모달, 다중 턴 대화) 벤치마크에 대한 심화 분석 부족 (MISC 섹션에서 언급되나 제외됨)
  - 실제 산업 적용 사례나 배포 관점의 효율성(latency, 메모리) 분석 미흡

- **후속 연구 방향**:
  - 사전학습 기반 초기화보다 HybridQA 특화 사전학습(PoEt) 등의 개선 필요
  - 테이블의 의미론적 구조 이해를 위한 그래프 신경망(GNN) 활용 강화
  - 약지도학습(weak supervision)을 통한 대규모 자동 주석 생성으로 데이터 부족 해소
  - 도메인 특화(금융, 과학) 어휘·공식 사전의 외부 지식 통합


## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 4.5/5
- Clarity: 4.5/5
- Overall: 4.25/5

**총평**: HybridQA 분야의 첫 포괄적 설문으로서 벤치마크·방법론·과제를 체계적으로 정리한 의미 있는 기여이나, 초기 LLM 시대의 급속한 방법론 발전을 충분히 반영하지 못한 점과 산업 적용 관점의 분석이 미흡한 것이 아쉬운 점이다.

## Related Papers

- 🔗 후속 연구: [[papers/841_Tree-of-table_Unleashing_the_power_of_llms_for_enhanced_larg/review]] — 테이블 기반 QA가 LLM의 대규모 테이블 추론 능력으로 확장됨
- 🏛 기반 연구: [[papers/787_Tablemaster_A_recipe_to_advance_table_understanding_with_lan/review]] — 테이블 이해 기술이 하이브리드 QA의 핵심 구성 요소가 됨
- 🏛 기반 연구: [[papers/841_Tree-of-table_Unleashing_the_power_of_llms_for_enhanced_larg/review]] — 테이블-텍스트 하이브리드 QA에 대한 조사는 대규모 테이블 이해를 위한 계층적 Table-Tree 구성의 이론적 기반을 제공합니다
