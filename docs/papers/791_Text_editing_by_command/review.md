---
title: "791_Text_editing_by_command"
authors:
  - "Felix Faltings"
  - "Michel Galley"
  - "Gerold Hintz"
  - "Chris Brockett"
  - "Chris Quirk"
date: "2020"
doi: "arXiv:2010.12826"
arxiv: ""
score: 4.2
essence: "기존의 원샷(one-shot) 텍스트 생성 패러다임을 벗어나, 사용자의 자연어 명령(command)을 따르는 대화형 텍스트 편집 작업을 제안한다. 위키피디아 편집 이력에서 수집한 WikiDocEdits 데이터셋과 트랜스포머 기반 편집 모델을 통해 동적 제약조건을 반영한 문서 생성이 가능함을 보인다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Self-Refining_Text_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Team_2020_Text editing by command.pdf"
---

# Text editing by command

> **저자**: Felix Faltings, Michel Galley, Gerold Hintz, Chris Brockett, Chris Quirk, Jianfeng Gao, Bill Dolan | **날짜**: 2020 | **DOI**: [arXiv:2010.12826](https://arxiv.org/abs/2010.12826)

---

## Essence

![Figure 1](figures/fig1.webp) *사용자 명령에 따른 대화형 텍스트 편집의 예시. "expand"와 "add years in office" 명령을 통해 문장이 점진적으로 확장된다.*

기존의 원샷(one-shot) 텍스트 생성 패러다임을 벗어나, 사용자의 자연어 명령(command)을 따르는 대화형 텍스트 편집 작업을 제안한다. 위키피디아 편집 이력에서 수집한 WikiDocEdits 데이터셋과 트랜스포머 기반 편집 모델을 통해 동적 제약조건을 반영한 문서 생성이 가능함을 보인다.

## Motivation

- **Known**: GPT-2/GPT-3 같은 대규모 언어 모델은 유창한 텍스트 생성이 가능하지만, 생성 과정에서의 제어가 어렵고 환각(hallucination) 현상이 발생한다. 기존 연구는 주로 한 번의 생성(one-shot generation)을 기준으로 한다.

- **Gap**: 실제 인간의 저작 과정은 다중 반복(multi-iteration draft-edit cycle)을 거치며, 초기 요구사항이 동적으로 변할 수 있다. 기존 시스템은 이러한 대화형 편집 요구를 충족하지 못한다.

- **Why**: Grammarly나 MS Word 같은 기존 도구들은 주로 작은 규모의 편집(paraphrase)에 중점을 두고 있으며, 내용 추가/삭제 또는 의미 변경 같은 광범위한 편집을 지원하지 않는다.

- **Approach**: 사용자 명령(q), 원본 문장(D), 그라운딩(G)을 입력받아 편집된 문장(D')을 생성하는 조건부 생성 작업을 정의하고, 위키피디아 편집 이력을 활용하여 대규모 데이터셋을 구축한다.

## Achievement

1. **새로운 텍스트 편집 작업 정의 및 대규모 데이터셋 구축**: 위키피디아 2020년 2월 덤프에서 약 1,185만 개의 문장 수준 편집(WikiDocEdits)을 추출했으며, 편집자 댓글을 자연어 명령으로, 검색 엔진 쿼리 결과를 그라운딩으로 활용했다.

2. **모델 성능**: Transformer 기반 Interactive Editor가 파라핏(parrot) 및 GPT-2 베이스라인을 능가하며, 자동 평가와 인간 평가에서 모두 긍정적 결과를 달성했다.

3. **정밀한 분석**: 명령과 그라운딩의 중요성을 실증적으로 입증하고, 데이터셋 내 편집의 난이도 차이를 분석했다.

## How

- **데이터 구성**: Wikipedia 편집 이력에서 문장 수준의 매칭을 통해 편집 쌍(edit pairs)을 추출하며, BLEU 점수(ε=0.1)를 기준으로 필터링한다. 단일 문장 편집만을 포함하여 편집자 댓글의 관련성을 보장한다.

- **그라운딩 검색**: 페이지/섹션 제목과 대상 문장의 키워드를 조합하여 상용 검색 엔진에 쿼리하고, 상위 200개 스니펫을 수집한 후 4-gram 중복도를 제거하고 정보 추출 점수로 재정렬한다.

- **입력 설계**: 명령(q), 원본 문장(s), 그라운딩 텍스트(G)를 모두 모델 입력으로 사용하며, 이는 검색/QA 설정의 쿼리 역할을 한다.

- **편집 유형 분류**: Yang et al. (2017)의 분류기를 활용하여 편집을 유창성(fluency, 57%) 및 내용(content, 24.77%) 편집으로 분류한다.

- **커버리지 평가**: BERTScore 기반 회수율(RBERT)을 사용하여 그라운딩이 삽입된 단어를 얼마나 잘 포함하는지 측정한다(그라운딩만으로도 51% 평균 커버리지).

## Originality

- **새로운 작업 정의**: 종래의 원샷 생성과 달리 명시적인 사용자 명령과 외부 그라운딩을 포함하는 조건부 텍스트 편집 작업을 처음 제안한다.

- **대규모 실제 데이터셋**: Wikipedia 편집 이력에서 자동 추출한 1,185만 개의 실제 편집 데이터로, 자연어 명령(편집자 댓글)과 그라운딩을 포함한 유일한 대규모 자원이다.

- **상태 유지 편집 개념**: 문서의 현재 상태를 유지하며 점진적으로 편집하는 개념을 도입하여, 기존의 상태 무관(stateless) 텍스트 재생성과 구분한다.

- **BERTScore 기반 커버리지 측정**: 동의어와 문맥을 고려한 퍼지 매칭을 통해 편집 커버리지를 더 정교하게 평가한다.

## Limitation & Further Study

- **문장 수준 제한**: 현재 작업은 문장 단위 편집만 고려하며, 문서 수준의 구조적 편집(단락 재배열 등)은 미처리 상태이다. 향후 복합 편집을 다중 문장 편집의 조합으로 모델링할 필요가 있다.

- **그라운딩 의존성**: 테스트 시에는 사용자가 그라운딩을 제공해야 하며, 자동 검색 시스템의 성능에 큰 영향을 받는다. 실제 사용 시나리오에서 그라운딩 검색 메커니즘의 견고성이 과제이다.

- **편집자 댓글의 대리성**: 위키피디아 편집자 댓글을 자연어 명령으로 사용했으나, 이들이 편집의 의도를 완벽하게 표현하지 못할 수 있다.

- **향후 확장**: 실시간 상호작용 시스템의 구축, 다중 문서 수준 편집의 지원, 그리고 구조화된 데이터(표, 그래프)를 그라운딩으로 활용하는 확장이 필요하다.

## Evaluation

- **Novelty**: 4.5/5 - 새로운 작업 정의와 대규모 실제 데이터셋이 충분히 독창적이나, 모델 아키텍처 자체는 기존 Transformer 활용

- **Technical Soundness**: 4/5 - 데이터 구축 방법론이 명확하고 타당하나, 자동 편집 추출의 정확도에 대한 검증이 제한적

- **Significance**: 4/5 - 실제 사용 사례가 있는 중요한 문제이며, 향후 대화형 생성 시스템의 기초가 될 수 있음

- **Clarity**: 4.5/5 - 논문 구성과 설명이 전반적으로 명확하며 충분한 예시 제시

- **Overall**: 4.2/5

**총평**: 본 논문은 기존의 원샷 생성 패러다임을 넘어 사용자와의 대화형 상호작용을 통한 문서 생성을 처음 체계적으로 제안한 점에서 의미가 있으며, 실제 위키피디아 데이터를 기반한 대규모 데이터셋은 향후 연구의 기초가 될 만큼 가치가 있다.

## Related Papers

- 🔗 후속 연구: [[papers/656_Read_revise_repeat_A_system_demonstration_for_human-in-the-l/review]] — 자연어 명령 기반 텍스트 편집을 인간 피드백과 통합한 더 발전된 대화형 편집 시스템으로 확장함
- 🏛 기반 연구: [[papers/485_Learning_to_split_and_rephrase_from_wikipedia_edit_history/review]] — 위키피디아 편집 이력을 활용한 텍스트 분할과 재구성 연구가 자연어 명령 기반 텍스트 편집의 방법론적 기초를 제공함
- 🔗 후속 연구: [[papers/884_Wikiatomicedits_A_multilingual_corpus_of_wikipedia_edits_for/review]] — 위키피디아 편집의 기본적 접근을 자연어 명령을 통한 더 사용자 친화적인 대화형 편집으로 확장함
- 🔄 다른 접근: [[papers/485_Learning_to_split_and_rephrase_from_wikipedia_edit_history/review]] — 데이터 마이닝 기반 문장 분할과 명령어 기반 텍스트 편집이라는 서로 다른 텍스트 변형 접근법을 제시합니다.
- 🏛 기반 연구: [[papers/884_Wikiatomicedits_A_multilingual_corpus_of_wikipedia_edits_for/review]] — 명령어 기반 텍스트 편집의 이론적 기반이 WikiAtomicEdits에서 관찰된 원자적 편집 패턴의 체계적 분석에서 도출되었음
- 🏛 기반 연구: [[papers/656_Read_revise_repeat_A_system_demonstration_for_human-in-the-l/review]] — 자연어 명령을 통한 텍스트 편집의 기초적 접근이 인간 피드백 기반 반복적 텍스트 개정 시스템의 이론적 토대를 제공함
- 🔗 후속 연구: [[papers/272_Diamonds_in_the_rough_Generating_fluent_sentences_from_early/review]] — 명령을 통한 텍스트 편집 방법으로 본 논문의 문장 수정을 더 일반적인 텍스트 편집으로 확장한다.
