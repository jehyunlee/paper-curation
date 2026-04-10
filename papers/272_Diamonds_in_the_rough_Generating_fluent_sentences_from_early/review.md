---
title: "272_Diamonds_in_the_rough_Generating_fluent_sentences_from_early"
authors:
  - "Takumi Ito"
  - "Tatsuki Kuribayashi"
  - "Hayato Kobayashi"
  - "Ana Brassard"
  - "Masato Hagiwara"
date: "2019"
doi: "arXiv:1910.09180"
arxiv: ""
score: 4.0
essence: "비모국어 부정확한 초안 문장을 유창하고 완성된 학술 문장으로 자동 변환하는 문장 수준 수정(Sentence-level Revision, SentRev) 작업을 제안하고, 이를 위한 SMITH 데이터셋을 구축하여 기준선 성능을 설정한다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Self-Refining_Text_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Ito et al._2019_Diamonds in the rough Generating fluent sentences from early-stage drafts for academic writing assi.pdf"
---

# Diamonds in the rough: Generating fluent sentences from early-stage drafts for academic writing assistance

> **저자**: Takumi Ito, Tatsuki Kuribayashi, Hayato Kobayashi, Ana Brassard, Masato Hagiwara, Jun Suzuki, Kentaro Inui | **날짜**: 2019 | **DOI**: [arXiv:1910.09180](https://arxiv.org/abs/1910.09180)

---

## Essence

![Figure 1](https://imgur.com/3yXkZ8J.png) *쓰기 과정의 4단계(초안 작성→수정→편집→교정)와 본 연구의 초점*

비모국어 부정확한 초안 문장을 유창하고 완성된 학술 문장으로 자동 변환하는 문장 수준 수정(Sentence-level Revision, SentRev) 작업을 제안하고, 이를 위한 SMITH 데이터셋을 구축하여 기준선 성능을 설정한다.

## Motivation

- **Known**: 기존 학술 쓰기 보조 연구(문법 오류 수정, GEC)는 최종 단계의 표면 수준 오류(오타, 맞춤법, 문법)에 주로 집중해왔다.

- **Gap**: 초안 수정 단계에서 정보 보충, 어휘 선택, 표현 방식 개선이 필요한데, 이 단계의 도움말과 평가 자원이 부족하다.

- **Why**: 비모국어 미숙한 저자들은 문법 오류뿐 아니라 유창성 부족, 어색한 스타일, 전개 오류, 누락된 단어로 인해 학술 쓰기에 어려움을 겪는다.

- **Approach**: 학술 논문의 최종 문장을 수집한 후, 이를 다른 언어(일본어)로 번역하고 모국어 사용자가 다시 영어로 번역하도록 하여 자연스러운 오류 문장을 생성하는 크라우드소싱 방법론을 개발했다.

## Achievement

![Figure 2](https://imgur.com/8K7pQQj.png) *SMITH 데이터셋 생성 절차: (i) 학술 논문에서 최종 문장 추출 → (ii) 일본어 번역 → (iii) 크라우드소싱으로 영어 재번역 → (iv) 품질 관리*

1. **새로운 작업 정의**: SentRev 작업을 학술 쓰기 보조의 새로운 영역으로 제안하여 초안 단계의 도움을 체계화했다.

2. **SMITH 데이터셋 구축**: 10,804개의 초안-최종 문장 쌍으로 구성된 공개 평가 데이터셋을 구축했으며, JFLEG 대비 약 7배 규모이고 99%의 문장 쌍에서 변화가 있다(표 3).

3. **데이터 품질 검증**: 95% 적절성 확률로 데이터 품질을 검증했으며, 문자 수준 Levenshtein 거리(47.0)가 기존 데이터셋보다 훨씬 크다는 것은 실질적인 수정이 이루어졌음을 보여준다.

4. **기준선 설정**: 비지도 모델들로 SentRev 작업의 기준선 성능을 확립했다.

## How

![Figure 2](https://imgur.com/8K7pQQj.png) *크라우드소싱 프로토콜의 4단계*

**데이터셋 생성 방법론**:
- ACL 2018 논문에서 70~120자 길이의 문장 10,804개 추출
- Google Translate를 이용한 영어→일본어 자동 번역 후 일본어 모국어자 검증
- 306명의 일본어 크라우드워커에게 일본어→영어 재번역 요청 (15분 제한시간)
- 표 2의 상세 기준(작업 시간, 답변 길이, 문장 부호, 영어 인식, Levenshtein 거리 등)으로 워커 품질 평가
- Unigram 겹침 계수(α=0.4)를 사용한 자동 필터링으로 과도한 변화 제거

**오류 유형**:
- 표면 수준: 오타, 맞춤법, 문법 오류
- 어휘 수준: 전개 오류, 부적절한 표현
- 정보 간격: 누락된 단어/구문(특수 토큰 <*>으로 표시)

## Originality

- **비모국어 쓰기의 자연스러운 오류 생성**: 자동 번역→역번역 파이프라인이 비모국어 저자의 실제 쓰기 과정(모국어에서 정신적 번역)을 모방하는 창의적 접근법

- **학술 쓰기 보조의 새로운 단계 정의**: 기존 GEC의 "교정(proofreading)" 단계를 넘어 "수정(revising)" 단계로 영역 확장

- **체계적 품질 관리**: 점수 기반 워커 평가, 다중 필터링 기준, 전문가 검증을 결합한 다층적 품질 관리 프레임워크

- **공개 데이터셋**: SMITH 데이터셋을 자유롭게 공개하여 향후 연구의 기초 자원 제공

## Limitation & Further Study

- **데이터셋 규모**: 10,804개 쌍은 현대 신경망 모델 학습에는 제한적 규모이며, 추가 확장이 필요함

- **단일 언어 쌍**: 일본어→영어 번역만 사용했으므로, 다른 모국어의 비모국어 저자 패턴을 포착하지 못함

- **맥락 부재**: 문장 수준 수정에 집중하여 단락이나 문서 수준의 맥락을 고려하지 않음

- **평가 메트릭 부재**: 이 작업의 특성상 다중 정답이 가능하나, 적절한 자동 평가 메트릭이 제시되지 않음

- **후속 연구 방향**:
  - 신경 시퀀스-투-시퀀스(seq2seq) 모델 적용
  - 다중 정답 생성 및 평가 방법 개발
  - 다국어 데이터셋 확장
  - 맥락 기반 수정 모델 개발

## Evaluation

| 평가 항목 | 점수 |
|---------|------|
| **Novelty** | 4/5 |
| **Technical Soundness** | 4/5 |
| **Significance** | 4/5 |
| **Clarity** | 5/5 |
| **Overall** | 4/5 |

**총평**: 학술 쓰기 보조의 미개척 영역인 초안 수정 단계를 새로운 작업으로 정의하고, 창의적인 크라우드소싱 방법론으로 자연스러운 오류 데이터셋을 구축했다는 점에서 중요한 기여이다. 다만 신경망 기반 모델 개발과 실제 적용 평가가 미흡하며, 향후 다양한 언어와 규모의 데이터 확장이 필요하다.

## Related Papers

- 🏛 기반 연구: [[papers/272_Diamonds_in_the_rough_Generating_fluent_sentences_from_early/review]] — 비모국어 화자의 초안을 유창한 학술 문장으로 변환하는 문장 수준 수정 작업의 핵심 방법론을 제시한다.
- 🔗 후속 연구: [[papers/791_Text_editing_by_command/review]] — 명령을 통한 텍스트 편집 방법으로 본 논문의 문장 수정을 더 일반적인 텍스트 편집으로 확장한다.
- 🔄 다른 접근: [[papers/656_Read_revise_repeat_A_system_demonstration_for_human-in-the-l/review]] — 인간-루프 반복 시스템으로 본 논문의 자동 수정과 다른 접근법인 인간 참여형 수정을 제시한다.
