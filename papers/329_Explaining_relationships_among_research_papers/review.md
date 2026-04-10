---
title: "329_Explaining_relationships_among_research_papers"
authors:
  - "Xiangci Li"
  - "Jessica Ouyang"
date: "2024"
doi: "N/A"
arxiv: ""
score: 4.0
essence: "본 논문은 연구 논문들 간의 복잡한 관계를 포착하기 위해 특성 기반(feature-based) LLM 프롬프팅 접근법을 제안하며, 단순 인용문 생성을 넘어 여러 논문을 한 번에 처리하고 이들을 연결하는 전환 문장(transition sentence)을 생성한다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Hierarchical_Knowledge_Graphs"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Gartner and Cardon_2024_Explaining relationships among research papers.pdf"
---

# Explaining relationships among research papers

> **저자**: Xiangci Li, Jessica Ouyang | **날짜**: 2024 | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp)
*그림 1: GPT-4 기반 Bing Chat과 본 논문의 접근 방식 비교. Bing Chat의 출력은 일반적이고 부정확한 반면, 제안 방식은 구조화된 특성(features)을 활용하여 보다 정확한 인용문을 생성한다.*

본 논문은 연구 논문들 간의 복잡한 관계를 포착하기 위해 특성 기반(feature-based) LLM 프롬프팅 접근법을 제안하며, 단순 인용문 생성을 넘어 여러 논문을 한 번에 처리하고 이들을 연결하는 전환 문장(transition sentence)을 생성한다.

## Motivation

- **Known**: 
  - 기존 연구는 인용문 생성 작업을 단일 인용문 수준의 고립된 문제로 접근
  - Seq2seq 신경망 기반 말단간(end-to-end) 방식들이 주류를 이룸
  - 장문서 처리의 길이 제한으로 인한 제약 존재

- **Gap**: 
  - 여러 인용 논문 간의 관계(relationships among cited papers)를 무시
  - 문학 검토(literature review)에 필요한 설명문(expository sentences)과 전환문(transition sentences)이 부재
  - 최신 LLM(GPT-4)조차 사실적 오류(hallucination)와 주제 벗어남 문제 해결 불가

- **Why**: 
  - 급속한 학술 출판으로 인해 연구자가 관련 논문을 추적하기 어려움
  - 맞춤형 문학 검토 요약의 필요성 증대
  - LLM이 지도(guidance) 없이는 정확한 생성 불가능

- **Approach**: 
  - 인용 논문들 간의 관계를 포착하는 자동 추출 특성(features) 설계
  - LLM 프롬프팅을 통한 특성 추출 및 이를 바탕으로 한 다중 인용문 생성
  - 계획(plan) 기반 설정에서 고수준 관계 설명을 통한 생성 유도

## Achievement

![Figure 2](figures/fig2.webp)
*그림 2: 문학 검토 생성을 위한 프롬프트 형식. 추출된 특성들이 구조화되어 LLM에 입력된다.*

![Figure 3](figures/fig3.webp)
*그림 3: 인간 평가 점수 분포. 적분적 글쓰기 스타일을 보인 생성문이 더 높은 선호도를 보인다.*

1. **특성 기반 생성 프레임워크**: 인용 논문의 기여도, 논문 간 관계, 인용의 담화 역할(discourse role)을 표현하는 해석 가능한(human-interpretable) 자연언어 특성들을 정의하고 자동 추출

2. **다중 인용 동시 생성**: 단일 인용문이 아닌 여러 논문의 인용과 이를 연결하는 전환 문장을 한 번에 생성하여 응집력 있는 문학 검토 구성

3. **계획 기반 생성의 효과성**: 고수준 관계 설명(plan)을 통한 유도가 생성 품질 향상에 기여함을 실증적으로 입증

4. **적분적 글쓰기 선호도 발견**: 인간 평가 결과 고수준의 추상적 인용과 전환 문장이 포함된 응집력 있는 문서를 강하게 선호

## How

![Figure 4](figures/fig4.webp)
*그림 4: 사실적 오류(factual errors) 개수 비교. 제안 방식이 Bing Chat 대비 오류를 크게 감소시킨다.*

- **특성 추출 단계**:
  - LLM 프롬프팅을 통해 각 인용 논문의 주요 기여도(key contributions) 추출
  - 인용 논문들 간의 관계(방법론적 유사성, 상호보완성, 비교 대상 등) 식별
  - 각 인용의 담화 역할(background, motivation, comparison 등) 분류

- **계획 기반 생성**:
  - 인간이 제공한 고수준 계획(여러 문장으로 논문 간 관계 설명)을 입력으로 사용
  - 계획 정보가 생성기의 조직화에 미치는 영향을 조사(preliminary study)

- **프롬프트 구성**:
  - 추출된 특성들을 구조화된 형식으로 종합
  - 다중 인용과 전환 문장 생성을 위한 통합 프롬프트 작성
  - LLM에 입력하여 단락 수준의 응집력 있는 텍스트 생성

- **평가 기준**:
  - 관련 작업 섹션(Related Work sections)을 평가 대상으로 활용
  - 전문가 평가(expert evaluation)를 통한 질적 분석
  - ROUGE 메트릭 및 인간 선호도 조사

## Originality

- 기존 단일 인용문 중심 접근에서 **다중 논문 간 관계 생성**으로 확대한 첫 시도
- **해석 가능한 자연언어 특성**을 통한 LLM 지도 방식으로 할루시네이션 감소 실현
- 논문 간 관계를 명시적으로 모델링하는 **계획 기반 접근법** 도입
- 응집력 있는 문학 검토 구성에 **전환 문장의 중요성**을 실증적으로 입증
- 자동 추출된 관련 작업 섹션을 평가 데이터로 활용한 실용적 데이터셋 활용

## Limitation & Further Study

- **예비 연구 수준**: 계획 기반 실험이 인간이 제공한 계획을 사용하므로 자동 계획 생성의 필요성 존재
- **규모의 제한**: 전문가 평가 규모가 제한적이어서 일반화 가능성 검증 필요
- **데이터셋 부재**: 맞춤형 일일 피드 요약 데이터셋이 없어 관련 작업 섹션을 프록시로 사용한 간접적 평가
- **비교 평가 어려움**: 선행 연구들이 서로 다른 데이터셋과 과제 정의를 사용하여 직접 비교 불가
- **후속 연구**:
  - 자동 계획 생성 알고리즘 개발
  - 맞춤형 피드 요약 데이터셋 구축
  - 더 대규모의 인간 평가 실시
  - 다양한 도메인과 주제에 대한 일반화 검증
  - 추출된 특성의 정확성 향상 방법 탐색

## Evaluation

- **Novelty**: 4/5
  - 다중 논문 간 관계 생성이 신규이나, LLM 프롬프팅 자체는 기존 기법

- **Technical Soundness**: 3.5/5
  - 특성 추출과 프롬프팅 기법은 타당하나, 자동 계획 생성 부재로 완전성 미흡
  - 평가 지표의 보완 필요(ROUGE만으로는 부족)

- **Significance**: 4/5
  - 응집력 있는 문학 검토 생성의 실질적 필요성 해결
  - 하지만 실제 시스템 통합까지의 거리 존재

- **Clarity**: 4/5
  - 동기와 접근법이 명확하나, 특성 추출의 구체적 과정 기술 미흡
  - 도형과 사례가 이해도 향상에 도움

- **Overall**: 4/5

**총평**: 본 논문은 연구 논문 간의 복잡한 관계를 포착하여 응집력 있는 문학 검토를 생성하는 실질적인 문제를 다루며, 특성 기반 LLM 프롬프팅의 유효성을 입증했으나, 계획의 자동 생성 및 대규모 평가를 통한 완성이 필요하다.

## Related Papers

- 🏛 기반 연구: [[papers/215_Chime_Llm-assisted_hierarchical_organization_of_scientific_s/review]] — 과학 연구의 계층적 조직화 시스템으로 본 논문의 논문 간 관계 설명을 위한 구조적 기반을 제공한다.
- 🔗 후속 연구: [[papers/564_Multi-llm_collaborative_caption_generation_in_scientific_doc/review]] — 과학 문서에서 다중 LLM 협업 캡션 생성으로 본 논문의 여러 논문 처리를 다중 모델 협업으로 확장한다.
- 🔄 다른 접근: [[papers/789_Taxonomy_tree_generation_from_citation_graph/review]] — 인용 그래프에서 분류 체계 트리 생성으로 본 논문과 다른 방식의 논문 간 관계 구조화를 제시한다.
- 🏛 기반 연구: [[papers/338_Figuring_out_figures_Using_textual_references_to_caption_sci/review]] — 연구 논문 간의 관계 설명 기법이 과학 도형과 텍스트 참조 간의 연결 관계를 이해하는 이론적 기반을 제공한다.
- 🔗 후속 연구: [[papers/215_Chime_Llm-assisted_hierarchical_organization_of_scientific_s/review]] — 연구 논문들 간의 관계 설명을 통해 본 논문의 계층적 조직화를 논문 간 연결성 분석으로 확장한다.
