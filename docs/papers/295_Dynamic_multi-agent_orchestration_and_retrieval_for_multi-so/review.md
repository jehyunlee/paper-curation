---
title: "295_Dynamic_multi-agent_orchestration_and_retrieval_for_multi-so"
authors:
  - "Antony Seabra"
  - "Claudio Cavalcante"
  - "João Nepomuceno"
  - "Lucas Lago"
  - "Nicolaas Ruberg"
date: "2024"
doi: "해당"
arxiv: ""
score: 3.5
essence: "다양한 데이터 소스(비정형 문서, 구조화된 데이터베이스)를 통합하는 다중 에이전트 기반 질의응답 시스템을 제안한다. 동적 프롬프트 엔지니어링과 함께 SQL 에이전트, RAG(Retrieval-Augmented Generation) 에이전트, 라우터 에이전트를 조합하여 질의 특성에 따라 최적의 검색 전략을 자동으로 선택한다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/Multi-agent_Task_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Seabra et al._2024_Dynamic multi-agent orchestration and retrieval for multi-source question-answer systems using large.pdf"
---

# Dynamic multi-agent orchestration and retrieval for multi-source question-answer systems using large language models

> **저자**: Antony Seabra, Claudio Cavalcante, João Nepomuceno, Lucas Lago, Nicolaas Ruberg, Sérgio Lifschitz | **날짜**: 2024 | **DOI**: [해당 정보 없음]

---

## Essence

![Figure 4](figures/fig4.webp) *에이전트 아키텍처*

다양한 데이터 소스(비정형 문서, 구조화된 데이터베이스)를 통합하는 다중 에이전트 기반 질의응답 시스템을 제안한다. 동적 프롬프트 엔지니어링과 함께 SQL 에이전트, RAG(Retrieval-Augmented Generation) 에이전트, 라우터 에이전트를 조합하여 질의 특성에 따라 최적의 검색 전략을 자동으로 선택한다.

## Motivation

- **Known**: LLM은 자연어 이해와 생성에 뛰어나지만 환각(hallucination), 지식 부실(outdated knowledge), 도메인 특화 지식 부족 문제를 가짐. 기존 Q&A 시스템은 단일 형식의 데이터만 효과적으로 처리 가능.

- **Gap**: 비정형 문서(PDF)와 구조화된 데이터베이스 등 이질적 소스를 통합하는 다중 소스 Q&A 시스템에서 정보의 정확성과 관련성을 유지하기 어려움. 특히 계약 관리 등 복잡한 쿼리는 여러 소스의 정보를 동시에 다루어야 하는데 이를 체계적으로 지원하는 방법론 부재.

- **Why**: 계약 관리, 의료, 금융 등 많은 업무 영역에서 전문가들이 방대한 문서를 수작업으로 검색하고 구조화된 메타데이터와 교차 참조해야 하는 시간 소모적이고 오류 가능성 높은 작업을 수행 중.

- **Approach**: 동적 멀티 에이전트 오케스트레이션, RAG, Text-to-SQL 기법, 동적 프롬프트 엔지니어링을 결합하여 질의 특성에 따라 최적의 검색 전략을 자동 선택하는 시스템 제안.

## Achievement

![Figure 5](figures/fig5.webp) *애플리케이션 아키텍처*

1. **멀티소스 통합 Q&A 시스템**: 계약 관리 도메인에서 비정형 문서와 구조화된 데이터베이스로부터의 정보를 동시에 검색하여 포괄적이고 맥락 인식적 응답 제공 가능.

2. **동적 라우팅 메커니즘**: 쿼리 특성을 분석하여 SQL 에이전트(구조화 데이터용), RAG 에이전트(비정형 문서용), 또는 하이브리드 접근을 자동으로 선택함으로써 검색 정확도 향상.

3. **응답 정확도 개선**: 동적 프롬프트 엔지니어링을 통해 쿼리 컨텍스트에 맞게 LLM의 지시사항을 실시간 조정하여 도메인 특화 응답 품질 증대.

## How

![Figure 1](figures/fig1.webp) *검색-증강 생성(RAG)*

![Figure 2](figures/fig2.webp) *계약 조항별 청킹*

![Figure 3](figures/fig3.webp) *청크 메타데이터*

**멀티 에이전트 오케스트레이션 시스템 구성:**

- **에이전트 기반 아키텍처**: 라우터 에이전트가 쿼리 분석 후 적절한 에이전트(SQL, RAG, 또는 둘 모두)로 작업 위임
- **RAG 기법**: 사용자 쿼리와 외부 문서를 고차원 벡터 공간에 임베딩하고, 벡터스토어에서 의미론적으로 가장 관련성 높은 청크 검색
- **청킹 전략**: 토큰 기반 청킹(중복 포함)과 문서 구조 기반 청킹(계약 조항별 분할)을 적용하여 시맨틱 완전성 확보
- **Text-to-SQL**: 자연어 쿼리를 SQL 명령으로 변환하여 정확한 구조화 데이터 검색. 데이터베이스 스키마 매핑과 엔티티 감지 수행
- **동적 프롬프트 엔지니어링**: 검색된 데이터 타입, 쿼리 컨텍스트, 사용자 입력에 따라 프롬프트 지시사항을 실시간 적응
- **유사성 vs. 관련성 구분**: RAG에서 의미론적 유사성만으로 검색된 정보가 항상 관련성 있는 것은 아니므로 추가 필터링/정제 기법 적용

## Originality

- **에이전트 기반 동적 라우팅**: 단순 하이브리드 시스템이 아닌 쿼리 분석을 통한 지능형 라우팅으로 각 소스에 최적화된 전략 자동 선택
- **도메인 특화 청킹 전략**: 계약 같은 구조화된 문서에 대해 조항 기반 청킹을 적용하여 의미론적 완전성과 관련성 동시 확보
- **동적 프롬프트 엔지니어링**: 정적 프롬프트가 아닌 쿼리 컨텍스트에 따른 실시간 프롬프트 최적화로 응답 정확도 향상
- **멀티소스 메타데이터 통합**: 검색된 정보에 메타데이터를 첨부하여 정보의 출처와 신뢰도 추적 가능
- **유사성과 관련성의 명시적 구분**: RAG 시스템의 근본적 문제점(의미론적 유사성 ≠ 쿼리 관련성)을 인식하고 이를 해결하는 메커니즘 제시

## Limitation & Further Study

- **청킹 전략의 도메인 의존성**: 제안된 청킹 방식(토큰 기반, 구조 기반)이 계약 관리 도메인에 최적화되어 있으며, 다른 도메인으로의 일반화 가능성 제한적
- **평가 방법론 부재**: 논문의 첫 15,000자에서 정량적 평가 지표나 벤치마크 결과가 제시되지 않음. 사용자 피드백 수집만 언급됨
- **LLM 환각 문제의 완전한 해결 부재**: RAG와 Text-to-SQL이 환각을 완화하지만 완전히 제거하지는 못함
- **확장성과 성능**: 대규모 데이터셋에서의 성능, 응답 지연시간, 비용 효율성에 대한 분석 필요
- **후속 연구 방향**: 
  - 다양한 도메인에서의 일반화 및 평가
  - 검색 정확도 개선을 위한 고급 필터링 기법 개발
  - 멀티턴(multi-turn) 대화 지원
  - 실시간 API 통합
  - 시스템의 해석 가능성(explainability) 향상

## Evaluation

- **Novelty**: 4/5 - 에이전트 기반 동적 라우팅과 동적 프롬프트 엔지니어링 조합은 창신적이나, 개별 기법(RAG, Text-to-SQL)의 조합 수준에서 완전히 새로운 알고리즘적 기여는 제한적

- **Technical Soundness**: 3.5/5 - 기본 개념과 아키텍처는 건실하나, 제시된 부분에서 상세한 기술적 검증, 충돌 해결 메커니즘, 정량적 성능 분석 부족

- **Significance**: 4/5 - 실무 적용 가능성이 높고 계약 관리 등 복잡한 도메인에서의 실질적 가치 입증 가능하나, 일반적 Q&A 시스템 발전에 미치는 근본적 기여는 중간 수준

- **Clarity**: 3.5/5 - 배경 설명과 동기는 명확하지만, 전체 시스템의 구체적 구현, 에이전트 간 상호작용 흐름, 오류 처리 메커니즘에 대한 상세 설명 필요

- **Overall**: 3.5/5

**총평**: 이 논문은 실무 중심의 멀티소스 Q&A 시스템을 위해 기존 LLM 기법들(RAG, Text-to-SQL)을 에이전트 기반 오케스트레이션으로 통합한 실용적 접근방식을 제시하며, 계약 관리 도메인에서의 응용 가치가 높으나, 정량적 평가와 기술적 세부사항의 제시, 그리고 일반화 가능성에 대한 검증이 더 필요한 상태로 보인다.

## Related Papers

- 🔗 후속 연구: [[papers/602_Paperqa_Retrieval-augmented_generative_agent_for_scientific/review]] — 과학 논문 검색 증강 생성 에이전트로 다중 소스 질의응답의 과학 분야 특화 확장을 보여준다.
- 🏛 기반 연구: [[papers/034_A_Survey_on_RAG_Meeting_LLMs_Towards_Retrieval-Augmented_Lar/review]] — RAG와 LLM 결합에 대한 포괄적 조사로 검색 증강 생성의 이론적 기반을 제공한다.
- 🔄 다른 접근: [[papers/675_Retrieval-Augmented_Generation_for_Knowledge-Intensive_NLP_T/review]] — 대규모 언어모델을 위한 검색 증강 생성의 다른 체계적 접근 방법을 제시한다.
