---
title: "752_Shallow_synthesis_of_knowledge_in_gpt-generated_texts_A_case"
authors:
  - "Anna Martin-Boyle"
  - "Aahan Tyagi"
  - "Marti A. Hearst"
  - "Dongyeop Kang"
date: "2024"
doi: "N/A"
arxiv: ""
score: 4.0
essence: "본 논문은 학술 논문의 관련 연구(Related Work) 섹션 작성에서 GPT-4의 능력을 실증적으로 평가한다. 인용 그래프(citation graph) 분석을 통해 GPT는 거시적 인용 그룹화는 가능하나, 인간의 개입 없이 정교한 문헌 종합을 실패함을 보여준다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/AI_Review_Detection"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Martin-Boyle et al._2024_Shallow synthesis of knowledge in gpt-generated texts A case study in automatic related work compos.pdf"
---

# Shallow synthesis of knowledge in gpt-generated texts: A case study in automatic related work composition

> **저자**: Anna Martin-Boyle, Aahan Tyagi, Marti A. Hearst, Dongyeop Kang | **날짜**: 2024 | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp)
*인용 그래프 비교: (상단) 인간이 작성한 관련 연구 섹션, (중단) ScholaCite를 통한 GPT 협력 버전, (하단) GPT 전적 생성 버전. 노드는 인용 문헌을, 간선은 같은 문장 내 인용의 동시 출현을 나타냄*

본 논문은 학술 논문의 관련 연구(Related Work) 섹션 작성에서 GPT-4의 능력을 실증적으로 평가한다. 인용 그래프(citation graph) 분석을 통해 GPT는 거시적 인용 그룹화는 가능하나, 인간의 개입 없이 정교한 문헌 종합을 실패함을 보여준다.

## Motivation

- **Known**: 과학 문헌의 지수적 성장(1952-2020년 5.08% 연간 증가율, 14년마다 2배)에 대응하여 ChatGPT 등 대규모 언어모델(LLM)이 학술 저술에 활용되고 있음. 2022-2023년 1,226개 논문이 ChatGPT 사용을 인정함

- **Gap**: AI 기반 학술 저술 도구의 출력물에 대한 형식적 평가가 거의 이루어지지 않았음. 특히 관련 연구 섹션의 핵심 요소인 '종합(synthesis)'과 '맥락화(contextualization)' 능력 평가 부재

- **Why**: 저술은 단순한 결과 전파가 아니라 연구자의 이해도 발전에 중요한 역할을 함. 따라서 AI-인간 상호작용의 질과 적절성 평가가 중요

- **Approach**: 인용 그래프 구조 분석이라는 객관적, 재현가능하고 확장 가능한 평가 방법론을 개발하여, (1) 인간 저술, (2) GPT 협력 저술, (3) GPT 단독 저술 간 비교

## Achievement

![Figure 2](figures/fig2.webp)
*ScholaCite 워크플로우: 원본 인간 저술 텍스트, ScholaCite 기반 GPT 협력 텍스트, GPT 단독 생성 텍스트의 생성 과정*

1. **ScholaCite 도구 개발**: GPT-4를 통합하여 (a) 인용 그룹화 및 근거 생성, (b) 그룹 기반 관련 연구 섹션 초안 작성을 지원하는 2단계 협력 시스템 구축

2. **인용 그래프 분석 방법론**: 인용 문헌을 노드로, 같은 문장 내 인용 동시 출현을 간선으로 하는 그래프 구조를 통해, 전통적 True/False Positive 분류를 벗어난 객관적 평가 메커니즘 제시

3. **실증적 발견**: GPT-4는 조사(brainstorming)를 위한 거시적 인용 그룹화는 성공적이나, 세부 문헌 종합 없이는 다중 인용 간 상호 연결성이 현저히 낮음

## How

- **3조건 비교 구조**: 
  - 원본 논문 10개에서 초록, 인용 문헌, 관련 연구 섹션 추출하여 '진행 중인 논문(WIP)' 구성
  - 각 조건에서 관련 연구 섹션 독립적 생성
  - 인용 그래프 메트릭 계산 및 비교

- **ScholaCite 2단계 설계**:
  1. 사용자가 GPT 제시 인용 그룹화 및 근거 검토·수정
  2. 정제된 그룹화를 기반으로 GPT가 최종 관련 연구 섹션 초안 생성
  - 이 순차적 구조가 직접 초안 생성보다 우수한 구조화 달성

- **인용 그래프 메트릭**:
  - 노드 밀도(density): 인용 간 연결 정도
  - 평균 차수(average degree): 각 인용의 평균 동시 출현 빈도
  - 연결 요소(connected components): 별개 인용 클러스터 수

## Originality

- **신규 평가 방법론**: 기존 시스템 기반 관련 연구 생성 연구는 신경망 모델의 BLEU, ROUGE 점수 등 표면적 메트릭 사용. 본 논문은 **구조적 복잡도를 통한 종합 능력 평가**라는 개념적 전환 제시

- **인간-AI 협력 프레임워크**: 기존 자동 생성 연구와 달리, 인간 저자의 의사결정을 보존하면서 AI의 조사 보조 역할을 강조하는 설계

- **학술 맥락 중심 평가**: 전체 논문 맥락(abstract, introduction, conclusion)을 제공하여 개별 인용 검증이 아닌 **문헌 조직화 능력의 차원에서 평가**

## Limitation & Further Study

- **제한사항**:
  - 샘플 크기 소규모(논문 10개): 분야별·학문별 차이 미검토
  - GPT-4만 평가: 다른 LLM(Claude, Gemini 등)과의 비교 부재
  - 정성적 검증 부족: 종합 품질에 대한 전문가 평가 통합 필요
  - 인용 그래프 메트릭이 '좋은' 종합의 필요충분조건인지 미확인

- **후속 연구**:
  - 다양한 학문 분야(사회과학, 인문학, 자연과학)에서의 성능 평가
  - 문헌 간 의미적 거리(semantic distance) 반영하여 무의미한 인용 연결 필터링
  - 사용자 연구: 협력 저술이 최종 논문 품질과 저작 과정 이해에 미치는 영향 측정
  - 인용 그래프 메트릭과 인간 평가자의 합의도(inter-rater agreement) 검증

## Evaluation

- **Novelty**: 4/5 - 인용 그래프 분석이라는 객관적 평가 방법론은 신규이나, 관련 연구 생성 자체는 기존 연구 축적
- **Technical Soundness**: 4/5 - 방법론 설계는 논리적이나 통계적 유의성 검증 및 확장성 논증 보강 필요
- **Significance**: 3.5/5 - AI 저술 도구의 한계를 실증적으로 보이나, 개선 방안이나 설계 권고사항이 제한적
- **Clarity**: 4/5 - 전체 논문 구조와 Figure 설명이 명확하나, 인용 그래프 메트릭의 수식 및 계산 절차 상세 서술 부족
- **Overall**: 4/5

**총평**: 본 논문은 급증하는 AI 기반 학술 저술 도구 사용 속에서 GPT의 문헌 종합 능력을 구조적으로 평가하려는 시의적절한 시도이다. 특히 인용 그래프 분석이라는 객관적 방법론은 재현가능하고 확장 가능한 평가 프레임으로 가치가 있으나, 샘플 규모 제약과 정성적 검증 부재로 인해 결론의 일반화 가능성이 제한된다. "인간 개입 없이 독립적 텍스트 초안 생성을 권하지 않는다"는 결론은 AI 도구 설계에 대한 실질적 권고를 제공한다.

## Related Papers

- ⚖️ 반론/비판: [[papers/742_Select_read_and_write_A_multi-agent_framework_of_full-text-b/review]] — GPT의 문헌 종합 한계와 전체 텍스트 기반 관련 연구 생성의 가능성을 비교하여 현재 AI 기술의 실제 성능과 개선 방향을 파악할 수 있다.
- 🏛 기반 연구: [[papers/753_Shared_imagination_Llms_hallucinate_alike/review]] — LLM의 공유된 환각 패턴이 관련 연구 섹션 작성에서 나타나는 얕은 지식 종합 문제의 근본적 원인을 이해하는 데 중요한 통찰을 제공한다.
- 🔄 다른 접근: [[papers/789_Taxonomy_tree_generation_from_citation_graph/review]] — 인용 그래프 분석과 분류 체계 생성은 문헌 종합의 구조적 한계를 극복하기 위한 대안적 접근 방법을 제시한다.
- 🏛 기반 연구: [[papers/373_Generalization_Bias_in_Large_Language_Model_Summarization_of/review]] — GPT 생성 텍스트의 피상적 지식 합성 분석으로 과학 요약에서 과도한 일반화가 발생하는 메커니즘을 설명한다.
- ⚖️ 반론/비판: [[papers/742_Select_read_and_write_A_multi-agent_framework_of_full-text-b/review]] — 전체 텍스트 기반 관련 연구 자동 생성의 가능성과 GPT의 문헌 종합 한계를 대비하여 현재 기술의 실제 능력과 한계를 균형있게 파악할 수 있다.
- 🔗 후속 연구: [[papers/753_Shared_imagination_Llms_hallucinate_alike/review]] — 공유된 상상 공간 개념이 GPT의 얕은 문헌 종합 문제를 더 깊이 이해하는 이론적 틀을 제공한다.
- 🔄 다른 접근: [[papers/789_Taxonomy_tree_generation_from_citation_graph/review]] — 구조적 인용 그래프 분석을 통한 체계적 분류 생성이 GPT의 얕은 문헌 종합 문제에 대한 대안적 해결 방안을 제시한다.
