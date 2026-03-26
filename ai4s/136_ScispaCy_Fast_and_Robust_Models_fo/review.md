# ScispaCy: Fast and Robust Models for Biomedical Natural Language Processing

> **저자**: Mark Neumann, Daniel King, Iz Beltagy, Waleed Ammar | **날짜**: 2019-08 | **학회**: BioNLP 2019 (ACL Workshop) | **DOI**: 10.18653/v1/W19-5034

---

## Essence

scispaCy는 spaCy 라이브러리 위에 구축된 생의학/과학 텍스트 전용 NLP 파이프라인으로, POS tagging, dependency parsing, NER, sentence segmentation, entity linking candidate generation을 포함하는 end-to-end 도구이다. GENIA 코퍼스와 OntoNotes 5.0을 결합하여 학습함으로써, 생의학 텍스트에서 SOTA에 근접한 성능을 유지하면서 C++/Java 기반 도구에 필적하는 처리 속도(abstract당 32-33ms)를 달성하였다.

## Motivation

- **알려진 것**: MetaMap/MetaMapLite(entity linking 특화), GENIA Tagger(POS/chunking 특화), cTakes(임상 노트 특화) 등 생의학 텍스트 처리 도구가 존재
- **Gap**: 기존 도구들은 특정 태스크에 한정되거나(MetaMap: entity linking만), 최신 NLP 기법(word representation, neural network)을 활용하지 않거나(GENIA Tagger), Python 생태계와의 통합이 어려움
- **왜 중요한가**: 생의학 출판물이 기하급수적으로 증가하는 가운데, 빠르고 robust한 범용 NLP 파이프라인이 정보 추출 자동화의 기반 인프라로 필요
- **접근법**: spaCy의 검증된 아키텍처와 API 위에 생의학 도메인 데이터로 재학습하고, GENIA+OntoNotes 혼합 학습으로 도메인 강건성을 확보

## Achievement

1. **POS tagging**: GENIA Test set에서 98.38-98.51 accuracy -- SOTA(BiLSTM-CRF-charcnn 98.89)와 0.4%p 이내
2. **Dependency parsing**: UAS 90.60-90.66 (SD 기준) -- Biaffine parser(92.64) 대비 2%p 낮으나 9배 빠른 속도
3. **NER 9개 데이터셋 벤치마크**: 5/9 데이터셋에서 단순 baseline 이상의 경쟁력 있는 성능 (en_core_sci_md 기준 BC5CDR 83.92, BioNLP13CG 77.60, BC4CHEMD 84.55)
4. **처리 속도**: Abstract당 32-33ms로 GENIA Tagger(73ms)의 2.3배, Biaffine parser(272ms)의 8.2배 빠름
5. **Entity linking candidate generation**: K=100에서 gold recall ~95%, Murty et al.(2018) 대비 +5%p 향상하면서 후보 수는 46% 적음
6. **Sentence segmentation**: In-domain 학습만으로 97.2-97.4% 문장 정확도 달성, rule-based segmenter 불필요

## How

- **기반 프레임워크**: spaCy 2.0.18 -- arc-eager transition-based parser (dynamic oracle), CNN 기반 토큰 표현
- **학습 데이터 (POS/Parsing)**: GENIA 1.0 corpus를 Universal Dependencies v1.0으로 변환 + OntoNotes 5.0 혼합 학습
- **학습 데이터 (NER)**: MedMentions(범용 mention detection) + 4개 전문 데이터셋(BC5CDR, CRAFT, JNLPBA, BioNLP13CG) + 5개 추가 데이터셋 평가
- **모델 패키지**: en_core_sci_sm (vocab 58K, 벡터 없음) / en_core_sci_md (vocab 102K, 98K 벡터 포함)
- **Tokenizer**: 생의학 텍스트 특화 rule 추가 (인용 스타일, 약어 등)
- **Entity linking**: UMLS 2017 AA subset (2.78M concepts), TF-IDF character 3-gram 기반 approximate nearest neighbor 검색, Schwartz-Hearst 약어 탐지 알고리즘 통합
- **강건성 실험**: OntoNotes 웹 데이터를 0.01-0.50 비율로 혼합 시 일반 텍스트 성능 대폭 향상 (OntoNotes UAS ~50% → ~90%)하면서 GENIA 성능 유지

## Originality

- **실용적 통합 파이프라인**: 기존 생의학 NLP 도구들이 개별 태스크에 집중하는 것과 달리, tokenization부터 entity linking candidate generation까지 단일 Python 패키지로 통합
- **Domain mixing 전략**: GENIA(생의학)와 OntoNotes(일반 텍스트)를 혼합 학습하여 도메인 강건성을 확보하는 간단하면서 효과적인 접근 -- 생의학 성능 손실 없이 일반 텍스트 성능을 크게 향상
- **GENIA UD 변환 코퍼스 공개**: GENIA 1.0을 Universal Dependencies로 변환하고 원본 텍스트/메타데이터를 정렬하여 공개 -- 커뮤니티 자원으로서의 독립적 기여
- **약어 해소 통합 candidate generation**: 생의학 텍스트에서 빈번한 약어 문제를 비지도 약어 탐지로 해결하여 entity linking recall +5%p 향상

## Limitation & Further Study

### 저자들이 언급한 한계

- Entity linking은 candidate generation 단계만 구현되어 있으며, 전체 entity linking 모델은 향후 과제
- Negation detection 등 임상 NLP에서 흔히 사용되는 파이프라인 컴포넌트가 미포함

### 자체판단 아쉬운 점

- spaCy의 비교적 단순한 아키텍처(CNN + transition-based parser)에 기반하여, Biaffine parser나 Transformer 기반 모델 대비 정확도 갭(2-3%p)이 존재하며 이를 속도-정확도 트레이드오프로만 설명
- NER에서 multi-task learning이나 pretrained LM(ELMo, BERT)을 활용한 모델과의 비교가 공정하지 않다고 스스로 인정하면서도, 이들을 통합할 계획에 대한 논의가 없음 (이후 SciBERT가 같은 그룹에서 발표됨)
- MedMentions 기반 범용 NER 모델이 entity type을 예측하지 않아, 실제 활용 시 type 정보가 필요한 경우 별도 모델 사용 필요
- 임상 노트에 대한 직접 평가가 없어, "broad biomedical domain" 주장의 근거가 PubMed abstract에 한정
- Word vector가 98K개로 제한적이며, subword embedding이나 contextual embedding 미사용

### 후속 연구

- SciBERT(같은 Allen AI 그룹)와의 통합을 통한 성능 향상
- 완전한 entity linking 파이프라인 구현 (candidate ranking 포함)
- Negation detection, relation extraction 등 파이프라인 확장
- 임상 노트, 임상시험 보고서 등 다양한 생의학 텍스트 유형에 대한 직접 평가

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 3/5 |
| Technical Soundness | 4/5 |
| Significance | 4/5 |
| Clarity | 4/5 |
| Overall | 4/5 |

**총평**: 학술적 혁신보다는 실용적 가치에 집중한 시스템 논문으로, spaCy의 검증된 아키텍처를 생의학 도메인에 맞게 재학습하고 통합 파이프라인으로 공개한 것이 핵심 기여이다. GENIA+OntoNotes 혼합 학습을 통한 domain robustness, 9개 NER 데이터셋에 대한 체계적 벤치마크, UMLS 기반 candidate generation 등 실용적 완성도가 높으며, 생의학 NLP 연구의 인프라로서 널리 채택되었다.
