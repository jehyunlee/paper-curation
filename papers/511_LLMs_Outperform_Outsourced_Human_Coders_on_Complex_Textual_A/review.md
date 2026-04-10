---
title: "511_LLMs_Outperform_Outsourced_Human_Coders_on_Complex_Textual_A"
authors:
  - "Vicente J. Bermejo"
  - "Andres Gago"
  - "Ramiro H. Gálvez"
  - "Nicolás Harari"
date: "2024"
doi: "10.2139/ssrn.5020034"
arxiv: ""
score: 4.0
essence: "본 연구는 스페인어 뉴스 기사 210개를 대상으로 GPT-3.5-turbo, GPT-4-turbo, Claude 3 Opus, Claude 3.5 Sonnet 등의 대형언어모델(LLMs)과 외주 인간 코더의 성능을 5가지 자연언어처리(NLP) 과제에서 비교하여, LLMs가 특히 심층적 문맥 이해가 필요한 복잡한 텍스트 분석에서 인간 코더를 일관되게 능가함을 입증한다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/Multi-Agent_Language_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Bermejo et al._2024_LLMs Outperform Outsourced Human Coders on Complex Textual Analysis.pdf"
---

# LLMs Outperform Outsourced Human Coders on Complex Textual Analysis

> **저자**: Vicente J. Bermejo, Andres Gago, Ramiro H. Gálvez, Nicolás Harari | **날짜**: 2024 | **DOI**: [10.2139/ssrn.5020034](https://doi.org/10.2139/ssrn.5020034)

---

## Essence

본 연구는 스페인어 뉴스 기사 210개를 대상으로 GPT-3.5-turbo, GPT-4-turbo, Claude 3 Opus, Claude 3.5 Sonnet 등의 대형언어모델(LLMs)과 외주 인간 코더의 성능을 5가지 자연언어처리(NLP) 과제에서 비교하여, LLMs가 특히 심층적 문맥 이해가 필요한 복잡한 텍스트 분석에서 인간 코더를 일관되게 능가함을 입증한다.

## Motivation

- **Known**: 텍스트 데이터 분석은 사회과학 연구에서 점증적으로 중요해지고 있으며, 전통적인 수동 코딩, 사전 기반 방법(dictionary methods), 지도학습 머신러닝(SML) 모델 등 여러 방법론이 존재한다.

- **Gap**: 기존 연구(Gilardi et al., 2023)는 콘텐츠 모더레이션 등 상대적으로 단순한 과제에서 LLMs를 평가했으나, 명명된 개체 인식(NER), 광범위한 문맥 지식, 전체 텍스트에 대한 정교한 분석이 요구되는 복잡한 과제에서의 성능 비교는 부재했다.

- **Why**: 수동 코딩은 비용이 높고 확장성이 낮으며, SML 모델은 높은 코딩 숙련도와 수동 학습 데이터를 요구한다. LLMs의 영점 학습(zero-shot learning) 방식이 이러한 한계를 극복할 수 있는지 검증이 필요하다.

- **Approach**: 스페인 재정 통합 프로그램 관련 뉴스 기사 210개에서 5가지 NLP 과제(지자체 나열, 지자체 수 계산, 비판 여부 판단, 비판 출처 파악, 비판 대상 파악)를 수행하도록 LLMs와 대학생 외주 코더, 전문가 코더(금표준)에게 요청하고 성능을 비교한다.

## Achievement

1. **LLMs의 일관된 우월성**: 모든 5가지 과제에서 LLMs이 외주 인간 코더를 능가하였으며, 고급 LLMs(GPT-4-turbo, Claude 3.5 Sonnet)일수록 성능이 더 높았다.

2. **복잡한 과제에서의 특히 큰 격차**: 광범위한 문맥 지식이 필요한 과제(T4: 비판 출처 파악, T5: 비판 대상 파악)에서 성능 격차가 더욱 두드러졌으며, LLMs은 복잡하고 긴 기사에서 인간 코더가 단순하고 짧은 기사에서 달성하는 수준보다 더 나은 성능을 보였다.

3. **높은 내적 일관성**: LLM 응답이 인간 코더 응답보다 더 높은 내적 일관성(internal consistency)을 나타냈으며, 중위수 이상의 역량을 가진 인간 코더만으로 필터링해도 LLMs가 여전히 우수했다.

4. **비용 효율성**: 프로그래밍 기술이나 수동 학습 데이터 없이 단순 API 호출만으로 달성할 수 있어 확장성과 경제성이 뛰어나다.

## How

- **데이터 수집**: Factiva 데이터베이스에서 2011-2013년 사이 스페인 지자체와 공급업체 결제 프로그램을 언급한 스페인어 뉴스 기사 210개 추출

- **과제 설계**: 다섯 가지 NLP 과제 (T1: 지자체 나열, T2: 지자체 수 계산, T3: 비판 여부 판단, T4: 비판 출처 파악, T5: 비판 대상 파악) 설정

- **LLM 평가**: 각 기사에 대해 GPT-3.5-turbo, GPT-4-turbo, Claude 3 Opus, Claude 3.5 Sonnet에 영점 학습 프롬프트로 API 호출

- **인간 코더 평가**: 대학생(주로 스페인)을 인센티브 온라인 연구에 참여시켜 동일 과제 수행

- **금표준 설정**: 전문가 인간 코더가 신중한 체계적 접근과 심화 논의를 통해 각 질문의 최적 답변 결정

- **성능 비교**: 모든 방법의 답변을 금표준 레이블과 비교하여 정확도, 내적 일관성, 과제 난이도별 성능 분석

## Originality

- **광범위한 NLP 과제 평가**: 기존 연구에서 미흡했던 명명된 개체 인식(NER) 과제를 포함하여 더 다양한 범위의 NLP 과제 평가

- **깊은 문맥 이해가 필요한 복잡한 과제**: 단순 텍스트 내용 분석을 넘어 외부 문맥 지식(예: 바르셀로나 도시 정부 vs. 바르셀로나 주 정부 구분)이 요구되는 과제 평가

- **전체 텍스트 분석 기반 평가**: 고립된 발췌문이 아닌 완전한 텍스트에 대한 정교한 분석이 필요한 과제(T4, T5) 평가로 실제 연구 현장의 과제를 더 잘 반영

- **비영어권 언어 평가**: 스페인어 문서에 대한 다국어 LLMs 성능을 평가함으로써 언어별 편향 문제를 다룸

## Limitation & Further Study

- **표본 크기**: 210개 기사는 원본 21,627개 기사의 약 1%로, 더 큰 표본에서의 일반화 가능성 검증이 필요하다.

- **언어 편향**: LLMs은 영어로 학습된 데이터가 대부분이므로 스페인어 성능은 상한선이 아니며, 영어 문서에서는 더 큰 성능 우위가 예상된다.

- **인간 코더 선별**: 외주 코더의 질과 숙련도에 대한 더 세밀한 통제가 필요하며, 전문 코더와의 비교도 추가로 필요하다.

- **과제 특화**: 다른 도메인(예: 과학 논문, 의료 기록, 법률 문서)과 언어(예: 동아시아 언어)에서의 성능 검증이 필요하다.

- **프롬프트 최적화**: 영점 학습 프롬프트의 다양한 설계 변형에 따른 성능 변화 분석

- **비용-성능 분석**: LLM API 비용과 정확도를 고려한 정교한 경제성 분석

## Evaluation

- **Novelty**: 4/5 - 기존 연구를 확장한 포괄적 평가이나, LLMs의 우월성 자체는 어느 정도 예상된 결과
- **Technical Soundness**: 4/5 - 명확한 방법론과 금표준 설정이 우수하나, 표본 크기와 통제 변수 측면에서 개선 여지 있음
- **Significance**: 5/5 - 프로그래밍 기술이 없는 연구자들에게 매우 실용적이며, 사회과학 연구의 방법론적 지평을 크게 확대함
- **Clarity**: 4/5 - 전반적으로 명확하나, 일부 기술 세부사항 설명이 본문의 15,000자 범위 내에서 제한적
- **Overall**: 4/5

**총평**: 본 논문은 LLMs이 외주 인간 코더를 복잡한 텍스트 분석에서 명확히 능가한다는 실증적 증거를 제시함으로써, 프로그래밍 숙련도 없는 연구자들이 대규모 텍스트 데이터를 효과적으로 분석할 수 있는 새로운 방법론을 확립하는 데 크게 기여한다.

## Related Papers

- 🔗 후속 연구: [[papers/206_ChatGPT_outperforms_crowd_workers_for_text-annotation_tasks/review]] — 텍스트 주석 작업에서 ChatGPT가 크라우드 워커를 능가한다는 발견은 LLM이 복잡한 텍스트 분석에서 인간을 능가한다는 연구의 확장이다.
- ⚖️ 반론/비판: [[papers/611_People_who_frequently_use_ChatGPT_for_writing_tasks_are_accu/review]] — ChatGPT 사용자가 더 정확한 글쓰기 능력 평가를 받는다는 연구는 LLM이 모든 텍스트 작업에서 우수하지 않을 수 있음을 시사한다.
- 🔄 다른 접근: [[papers/153_Best_humans_still_outperform_artificial_intelligence_in_a_cr/review]] — 비판적 사고가 필요한 작업에서 인간이 AI를 능가한다는 연구는 복잡한 텍스트 분석 영역에서의 상반된 관점을 제시한다.
