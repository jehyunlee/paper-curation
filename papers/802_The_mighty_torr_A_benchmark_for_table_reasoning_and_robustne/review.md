---
title: "802_The_mighty_torr_A_benchmark_for_table_reasoning_and_robustne"
authors:
  - "Shir Ashury-Tahan"
  - "Yifan Mai"
  - "C Rajmohan"
  - "Ariel Gera"
  - "Yotam Perlitz"
date: "2025"
doi: "N/A"
arxiv: ""
score: 4.3
essence: "본 논문은 **ToRR(Table Reasoning and Robustness) 벤치마크**를 제시하여, 대규모 언어모델(LLM)의 표 데이터 이해 능력과 다양한 표 형식에 대한 견고성(robustness)을 체계적으로 평가한다. 10개의 데이터셋을 통해 14개 주요 LLM을 평가한 결과, 최신 모델들도 표 형식 변화에 취약한 '깨지기 쉬운(brittle)' 행동을 보인다는 것을 발견했다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Table_Caption_Generation"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Ashury-Tahan et al._2025_The mighty torr A benchmark for table reasoning and robustness.pdf"
---

# The mighty torr: A benchmark for table reasoning and robustness

> **저자**: Shir Ashury-Tahan, Yifan Mai, C Rajmohan, Ariel Gera, Yotam Perlitz, Asaf Yehudai, Elron Bandel, Leshem Choshen, Eyal Shnarch, Percy Liang, Michal Shmueli-Scheuer | **날짜**: 2025 | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp)
*Figure 1: ToRR의 개요. LLM을 다양한 프롬프트 구성으로 표 추론 데이터셋에서 평가하고, 테이블 직렬화(serialization) 및 섭동(perturbation) 변형을 포함하여 성능과 신뢰성을 분석*

본 논문은 **ToRR(Table Reasoning and Robustness) 벤치마크**를 제시하여, 대규모 언어모델(LLM)의 표 데이터 이해 능력과 다양한 표 형식에 대한 견고성(robustness)을 체계적으로 평가한다. 10개의 데이터셋을 통해 14개 주요 LLM을 평가한 결과, 최신 모델들도 표 형식 변화에 취약한 '깨지기 쉬운(brittle)' 행동을 보인다는 것을 발견했다.

## Motivation

- **Known**: 표 데이터는 현실에서 매우 중요하며, 표 질의응답(Table QA), 사실 검증, 표-텍스트 변환 등 다양한 NLP 작업에 활용된다. 하지만 LLM의 표 처리 능력에 대한 체계적 평가는 부족하다.

- **Gap**: 기존 연구는 특정 작업, 좁은 도메인, 제한된 모델 집합에만 초점을 맞추었고, 실제 응용에서 표가 다양한 형식(JSON, HTML, CSV 등)으로 나타난다는 점을 무시했다. 표 형식 변화에 대한 모델의 견고성 평가가 없었다.

- **Why**: 실제 환경에서 동일한 의미의 표가 여러 형식으로 표현되므로, 모델이 다양한 표 형식에서 일관된 성능을 보이는지 확인하는 것이 중요하다. 이는 모델의 내부 표현과 일반화 능력을 이해하는 데 필수적이다.

- **Approach**: 10개 데이터셋(6개 작업 유형, 다양한 도메인)으로 구성된 포괄적 벤치마크를 설계하고, 7가지 표 직렬화 형식과 4가지 구조적 섭동(행 셔플, 열 전치 등)을 적용하여 35가지 프롬프트 구성으로 14개 LLM을 평가했다.

## Achievement

![Figure 2](figures/fig2.webp)
*Figure 2: 동일한 질문이지만 서로 다른 표 형식(마크다운 vs. 셔플된 CSV)의 프롬프트 예시. 최신 모델들도 이 두 형식에서 일관되지 않은 답변을 생성한다.*

1. **표 추론의 심각한 한계 발견**: 14개 주요 LLM(GPT-4o, DeepSeek v3 등 포함)이 표 기반 작업에서 상당한 성능 저하를 보였으며, 특히 수치 추론(numerical reasoning)이 필요한 작업에서 취약함을 확인했다.

2. **견고성의 취약성 입증**: 동일한 의미의 표가 다른 형식으로 제시되면, 대부분의 모델이 일관되지 않은 성능을 보였다. 예를 들어, 마크다운과 CSV 형식 사이에서 오답을 다르게 생성하는 현상이 빈번했다.

3. **형식 의존성 부재**: 특정 표 직렬화 형식(예: HTML, JSON)이 모든 모델에서 일관되게 우수한 성능을 보이지 않았으며, 모델마다 선호하는 형식이 상이했다.

4. **메타-평가 통찰**: 단일 프롬프트로 100개 예제를 평가하는 것보다, 35개 프롬프트 구성으로 평가할 때 모델 순위의 안정성이 크게 향상되었으며, 이는 테스트 셋 크기 증가와 비슷한 신뢰성 개선 효과를 제공한다.

## How

![Figure 3](figures/fig3.webp)
*Figure 3: 각 예제에 대해 35가지 프롬프트 구성에서 얻은 성능 분포*

**벤치마크 설계:**
- **데이터셋 선정**: FinQA(금융), WikiTQ(위키피디아), TabFact(사실검증), TableBench(데이터 분석), QTSumm, SciGen, NumericNLG(표-텍스트 변환), TURL CTA(분류) 등 10개 데이터셋
  
- **기술 스킬 분류**:
  - 지식 추출(Knowledge Extraction): 표에서 특정 정보 추출
  - 텍스트 추론(Textual Reasoning): 표의 데이터와 동반 텍스트를 결합한 추론
  - 수치 추론(Numerical Reasoning): 표의 여러 셀에 대한 계산

- **프롬프트 구성 설계**:
  - **7가지 직렬화**: CSV, JSON, HTML, Markdown, Latex, 키-값 쌍, 자연어 기술
  - **4가지 섭동**: 행 셔플, 열 셔플, 행-열 전치, 열 정렬 변경
  - 조합: 7 × 4 + 7(섭동 미적용) = 35가지 프롬프트

- **평가 지표**:
  - **성능(Performance)**: 모든 프롬프트 구성에 걸친 평균 점수
  - **견고성(Robustness)**: 예제당 최대-최소 성능 범위의 평균 (낮을수록 견고함)

- **실험 설정**:
  - 각 데이터셋 100개 예제 (TableBench FC는 79개)
  - 5-shot 프롬프팅 (WikiTQ는 1-shot)
  - Greedy decoding, 최대 토큰 512
  - Unitxt 라이브러리 활용으로 재현성 보장

## Originality

- **포괄적 평가 범위**: 기존 연구가 특정 작업만 평가한 반면, 6가지 작업 유형, 10개 데이터셋, 14개 모델을 체계적으로 다룬 최초의 벤치마크 구성
  
- **견고성 중심 설계**: 표 형식 변화에 대한 모델의 일관성을 정량화한 Robustness 메트릭(R_M) 도입으로, 성능 이상의 신뢰성 평가 실현

- **메타-평가 분석**: 프롬프트 다양성이 평가 신뢰성에 미치는 영향을 정량적으로 분석하여, 벤치마크 설계 원칙에 대한 실증적 근거 제시

- **실용적 통찰**: 표 형식 선호도의 모델-의존성 발견은 단순히 "최적 형식" 탐색이 아닌, 다중 형식 평가의 필수성을 강조

## Limitation & Further Study

- **샘플 크기 제한**: 각 데이터셋 100개 예제는 대규모 벤치마크 기준으로 제한적일 수 있으며, 더 큰 표나 복잡한 구조의 표는 미포함

- **폐쇄형 테이블 중심**: 텍스트로 직렬화 가능한 표만 포함하여, 이미지 기반 표나 매우 큰 표(Wide/Tall tables)의 처리 능력 평가 부재

- **섭동 유형의 제한**: 4가지 기본 구조적 섭동만 포함하여, 더 실제적인 데이터 품질 문제(오류, 불완전성 등)에 대한 평가 미흡

- **모델 범위**: 공개 API 기반 모델 중심이며, 오픈소스 소규모 모델(7B 미만)의 표 처리 능력에 대한 분석 부족

- **후속 연구 방향**:
  - 이미지 형식 표와 매우 큰 표에 대한 평가 확대
  - 테이블 검색(Table Retrieval)과 에이전트 기반 접근법 통합
  - 표 데이터의 노이즈 견고성(noise robustness) 심층 분석
  - 소규모 LLM 및 파인튜닝 방법론에 대한 성능 개선 방안 모색


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4.5/5
- Significance: 4.5/5
- Clarity: 4/5
- Overall: 4.3/5

**총평**: 본 논문은 LLM의 표 데이터 처리 능력에 대한 가장 포괄적인 평가를 제공하며, 특히 표 형식 변화에 따른 모델의 취약성을 실증적으로 드러냈다는 점에서 높은 가치를 지닌다. 견고성 메트릭과 메타-평가 분석은 향후 NLP 벤치마크 설계의 방향성을 제시하는 중요한 기여이다.

## Related Papers

- 🔄 다른 접근: [[papers/715_Scidqa_A_deep_reading_comprehension_dataset_over_scientific/review]] — ToRR이 표 추론 견고성에 초점을 맞춘 반면, SciDQA는 과학 논문의 깊이 있는 이해를 평가하여 서로 다른 각도에서 LLM 평가를 다룸
- 🔗 후속 연구: [[papers/787_Tablemaster_A_recipe_to_advance_table_understanding_with_lan/review]] — TableMaster가 제시하는 표 이해 방법론이 ToRR 벤치마크에서 발견된 LLM의 표 형식 취약성 문제를 해결하는 솔루션으로 활용될 수 있음
- 🔄 다른 접근: [[papers/715_Scidqa_A_deep_reading_comprehension_dataset_over_scientific/review]] — SciDQA가 과학 논문의 깊이 있는 이해에 초점을 맞춘 반면, ToRR는 표 형식 견고성 평가에 특화되어 서로 다른 각도에서 LLM의 과학 텍스트 처리 능력을 평가함
- 🏛 기반 연구: [[papers/787_Tablemaster_A_recipe_to_advance_table_understanding_with_lan/review]] — 테이블 추론과 견고성에 대한 벤치마크 연구가 언어 모델의 테이블 이해 능력 향상 프레임워크 개발의 기초를 제공함
