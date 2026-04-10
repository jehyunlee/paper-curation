---
title: "485_Learning_to_split_and_rephrase_from_wikipedia_edit_history"
authors:
  - "Jan A. Botha"
  - "Manaal Faruqui"
  - "John Alex"
  - "Jason Baldridge"
  - "Dipanjan Das"
date: "2018"
doi: "N/A"
arxiv: ""
score: 4.5
essence: "본 논문은 위키피디아 편집 이력을 마이닝하여 문장 분할-재표현(split-and-rephrase) 작업을 위한 100만 개 규모의 대규모 자연 데이터셋 WikiSplit을 구축하고, 이를 활용하여 기존 방법 대비 32 BLEU 포인트 향상을 달성했다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Academic_Writing_Personalization"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Botha et al._2018_Learning to split and rephrase from wikipedia edit history.pdf"
---

# Learning to split and rephrase from wikipedia edit history

> **저자**: Jan A. Botha, Manaal Faruqui, John Alex, Jason Baldridge, Dipanjan Das | **날짜**: 2018 | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp)
*위키피디아 편집 이력에서 추출한 문장 분할-재표현(split-and-rephrase) 예시. 원본 문장이 두 개의 더 단순한 문장으로 분해되며, 삭제된 단어(노랑)와 추가된 단어(파랑)를 표시함.*

본 논문은 위키피디아 편집 이력을 마이닝하여 문장 분할-재표현(split-and-rephrase) 작업을 위한 100만 개 규모의 대규모 자연 데이터셋 WikiSplit을 구축하고, 이를 활용하여 기존 방법 대비 32 BLEU 포인트 향상을 달성했다.

## Motivation

- **Known**: Narayan et al. (2017)이 제안한 WebSplit 코퍼스는 split-and-rephrase 작업의 벤치마크로 사용되고 있으며, 신경망 기반 인코더-디코더 모델이 이 작업에서 성능이 낮다는 것이 알려져 있음.

- **Gap**: WebSplit은 단 17,000개의 고유 복잡 문장만 포함하고 있으며, 매우 제한된 어휘(7k 단어)와 부자연스러운 언어 표현을 가지고 있어 학습 데이터로 적합하지 않음. 또한 문장 길이 증가에 따른 성능 저하 문제가 자동 텍스트 단순화, 관계 추출, 기계 번역 등 여러 NLP 작업에서 지속되고 있음.

- **Why**: 보다 규모가 크고 다양하며 자연스러운 문장 분할 예시를 포함한 학습 데이터가 필요함. 위키피디아의 편집 이력은 실제 편집자들의 자연스러운 재표현을 담고 있어 이 목적에 적합한 자원임.

- **Approach**: 위키피디아 편집 이력을 자동으로 마이닝하여 문장 분할 사례를 추출하는 확장 가능한 휴리스틱 기반 방법을 제안하고, 추출된 데이터의 품질을 검증하며, 기존 WebSplit과 결합하여 모델 성능을 평가함.

## Achievement

![Table 3](figures/table3.webp)
*WebSplit과 WikiSplit의 코퍼스 통계 비교. WikiSplit은 복잡 문장 수, 단순 문장 수, 토큰 다양성 모두에서 훨씬 더 큰 규모와 다양성을 제공함.*

1. **WikiSplit 데이터셋 구축**: 100만 개의 자연스러운 문장 분할-재표현 예시 추출. 기존 WebSplit 대비 60배 많은 고유 분할 예시와 90배 더 큰 어휘 규모(633k 토큰) 달성.

2. **성능 대폭 향상**: WebSplit 벤치마크에서 BLEU 점수 30.5에서 62.4로 상향(104% 향상), 이전 최고 성능(Aharoni and Goldberg 2018의 30.5 BLEU) 대비 32 포인트 개선.

![Table 5](figures/table5.webp)
*다양한 학습 데이터 조합에 따른 WebSplit 테스트 셋 성능. WikiSplit만 사용했을 때 60.4 BLEU, WebSplit과 결합했을 때 62.4 BLEU 달성.*

3. **언어 간 일반화 가능성**: 위키피디아가 다국어로 존재하므로 제안된 추출 방법을 다른 언어로도 확장 가능한 기반 제공.

## How

- **위키피디아 편집 이력 마이닝**: 시간적으로 인접한 위키피디아 페이지 스냅샷을 비교하여 문장 분할 사례를 식별. 문장 경계 감지기를 사용하여 HTML/마크업 제거 후 처리.

- **고정밀 휴리스틱 필터링**: 
  - 복잡 문장 C와 단순 문장 S1의 삼중어(trigram) 접두사 일치 확인
  - 복잡 문장 C와 단순 문장 S2의 삼중어 접미사 일치 확인
  - S1과 S2의 서로 다른 삼중어 접미사 요구
  - BLEU 점수 임계값 δ=0.2를 사용한 원본-분할 유사도 검증

- **품질 관리**: 무작위 샘플 100개를 수동 평가하여 정확도 68%, 노이즈 포함 32% 확인. 반복 토큰, 과도하게 긴 토큰, 욕설 편집 등 추가 필터링 적용.

- **모델 아키텍처**: Copy512 모델 사용 (1층 양방향 LSTM, 셀 크기 512, 주의 메커니즘, 복사 메커니즘). 다양한 학습 데이터 조합 실험(WebSplit만, WikiSplit만, 병합).

## Originality

- **첫 대규모 자연 문장 분할 데이터셋**: 기계 생성이나 크라우드소싱이 아닌 실제 위키피디아 편집자의 자연스러운 재표현을 대규모로 수집한 최초 시도.

- **확장 가능한 자동 추출 방법**: 언어 독립적이고 단순한 휴리스틱 기반 접근으로 다른 언어/도메인으로 쉽게 확장 가능한 방법론 제시.

- **실질적 성능 개선**: 단순한 데이터 규모 증가를 넘어 자연 다양성 있는 데이터의 질적 우월성을 실증적으로 입증.

- **공개 자원 제공**: 백만 규모의 고품질 데이터셋을 커뮤니티에 공개하여 후속 연구의 기반 마련.

## Limitation & Further Study

- **노이즈 수용**: 추출된 데이터의 32%에 근거 없는 사실(unsupported facts) 또는 누락된 정보 포함. 평가용보다는 학습용으로만 권장하며, 저자들은 이를 인정하고 수용.

- **단일 분할 구조**: WebSplit은 각 복잡 문장에 여러 참조 분해(multiple reference decompositions)를 제공하지만, WikiSplit은 단일 분할만 제공하여 평가 메트릭의 신뢰도 감소.

- **평가 메트릭의 한계**: BLEU 점수만 보고되었으며, 인간 평가(human evaluation) 부재. 자동 메트릭이 분할-재표현 작업의 품질을 완전히 포착하지 못할 수 있음.

- **후속 연구 방향**:
  - 품질이 매우 높은 서브셋 구성을 위한 더 정교한 노이즈 필터링 방법 개발
  - 인간 평가 기반 성능 검증
  - 다국어 WikiSplit 확장(타 언어 위키피디아 활용)
  - 더 복잡한 모델 아키텍처(트랜스포머 등) 적용 시 성능 검증
  - 단순화 외 다른 텍스트 생성 작업으로의 확장 가능성 탐색

## Evaluation

- **Novelty**: 4.5/5 - 자연 편집 이력 기반 대규모 데이터셋은 혁신적이나, 추출 휴리스틱 자체는 비교적 단순함.

- **Technical Soundness**: 4/5 - 방법론은 견고하나 노이즈 평가가 제한적(샘플 크기 100개)이고, 인간 평가 부재로 자동 메트릭의 신뢰도 검증 부족.

- **Significance**: 5/5 - 100만 규모의 자연 데이터셋 공개는 커뮤니티에 매우 큰 영향을 미쳤으며, 벤치마크 성능을 획기적으로 향상시킴. 문장 단순화 외 다양한 NLP 작업에 실질적 기여.

- **Clarity**: 4.5/5 - 전반적으로 명확하게 구성되었으나, 노이즈 범주화(unsupported vs. missing)의 정의가 다소 모호하고, 추출 휴리스틱의 상세 설명 부족.

- **Overall**: 4.5/5

**총평**: 본 논문은 위키피디아 편집 이력이라는 풍부한 자연 자원을 효과적으로 활용하여 기존 소규모 합성 데이터셋의 한계를 극복한 우수한 데이터셋 논문이다. 비록 추출 방법론이 단순하고 노이즈가 존재하나, 공개된 대규모 자연 데이터와 입증된 성능 향상의 실용성이 충분히 가치 있으며, 텍스트 단순화 분야에서 중요한 기초 자원으로 널리 활용될 수 있다.

## Related Papers

- 🏛 기반 연구: [[papers/703_Scholawrite_A_dataset_of_end-to-end_scholarly_writing_proces/review]] — 위키피디아 편집 이력을 활용한 문장 분할-재표현 연구가 학술 글쓰기 과정의 텍스트 변경 패턴 분석의 기초가 됩니다.
- 🔗 후속 연구: [[papers/884_Wikiatomicedits_A_multilingual_corpus_of_wikipedia_edits_for/review]] — 영어 위키피디아 편집에서 다국어 위키피디아 편집 데이터셋으로 확장하여 더 포괄적인 텍스트 편집 연구를 가능하게 합니다.
- 🔄 다른 접근: [[papers/791_Text_editing_by_command/review]] — 데이터 마이닝 기반 문장 분할과 명령어 기반 텍스트 편집이라는 서로 다른 텍스트 변형 접근법을 제시합니다.
- 🔗 후속 연구: [[papers/884_Wikiatomicedits_A_multilingual_corpus_of_wikipedia_edits_for/review]] — 위키피디아 편집 이력을 활용한 분할 및 재작성 학습이 WikiAtomicEdits 코퍼스에서 발견된 편집 패턴을 실제 텍스트 처리 작업에 적용한 후속 연구임
- 🏛 기반 연구: [[papers/791_Text_editing_by_command/review]] — 위키피디아 편집 이력을 활용한 텍스트 분할과 재구성 연구가 자연어 명령 기반 텍스트 편집의 방법론적 기초를 제공함
