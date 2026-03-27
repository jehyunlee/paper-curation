# TLDR: Extreme Summarization of Scientific Documents

> **저자**: Isabel Cachola, Kyle Lo, Arman Cohan, Daniel S. Weld | **날짜**: 2020 | **학회**: arXiv (EMNLP 2020 Findings) | **DOI**: 10.48550/ARXIV.2004.15011

---

## Essence

TLDR generation은 과학 논문을 단일 문장(평균 21단어)으로 극단적 압축하는 새로운 요약 태스크이다. 이를 위해 3,229편의 CS 논문에 대해 5,411개의 multi-target TLDR을 포함하는 SciTLDR 데이터셋을 구축하고, 논문 제목 생성을 보조 scaffold task로 활용하는 CATTS(Controlled Abstraction for TLDRs with Title Scaffolding) 학습 전략을 제안하여 BART 기반 baseline 대비 자동 메트릭과 인간 평가 모두에서 성능을 향상시켰다.

## Motivation

- **알려진 것**: 과학 문서 요약(ArXiv, PubMed, SciSummNet 등)은 150-220단어 수준의 abstract 생성에 집중하며, 뉴스 도메인에서는 XSUM이 extreme summarization을 다룸
- **Gap**: 과학 논문에 대한 extreme summarization(단일 문장, 압축비 238:1)은 미탐구 영역이며, 기존 데이터셋은 단일 gold summary만 제공하여 인간 요약의 변동성을 반영하지 못함
- **왜 중요한가**: 출판 속도의 기하급수적 증가 속에서 연구자들이 논문의 핵심을 빠르게 파악할 수 있는 TLDR은 과학 커뮤니케이션의 효율성을 근본적으로 개선
- **접근법**: OpenReview의 저자 작성 TLDR과 peer review 코멘트 재작성 TLDR을 결합한 multi-target 데이터셋 구축 + 제목 생성을 control code 기반 scaffold task로 활용

## Achievement

1. **SciTLDR 데이터셋**: 3,229편 논문, 5,411개 TLDR (train 1,992 / dev 619+1,452 / test 618+1,967), 압축비 238.1로 기존 데이터셋 대비 최고 수준
2. **CATTS 성능 향상**: AIC 입력 기준 CATTS가 BART 대비 Rouge-1 +2.0, Rouge-2 +1.8, Rouge-L +2.2 유의미한 향상 (p<0.05)
3. **Human evaluation**: CATTS_XSUM이 BART_XSUM 대비 informativeness에서 MRR 0.54 vs 0.42로 우세, gold TLDR-Auth(0.53)와 동등 수준
4. **Correctness 평가**: 원저자 29명의 직접 평가에서 CATTS_XSUM과 BART_XSUM 모두 평균 2.5/3.0 (partially accurate ~ mostly correct)
5. **Nugget 분석**: TLDR의 정보 유형을 6가지(Area, Problem, Contribution, Details, Results, Value)로 체계화하고, 저자 vs 리뷰어 TLDR의 관점 차이를 정량적으로 분석

## How

- **TLDR-Auth 수집**: OpenReview API로 저자가 작성한 논문-TLDR 쌍 수집, S2ORC 파이프라인으로 PDF를 구조화된 전문으로 변환
- **TLDR-PR 수집**: 28명 CS 학부생이 peer review 코멘트의 첫 128단어를 15-25단어의 TLDR로 재작성, 수동 품질 검수 후 20명 선별 ($20/hr)
- **CATTS**: SciTLDR(Paper→TLDR)와 arXiv 20K(Paper→Title) 데이터를 혼합, 각 소스에 `<|TLDR|>` / `<|TITLE|>` control code 부착 후 BART에 jointly 학습. TLDR 인스턴스를 title 수에 맞춰 upsampling
- **모델**: BART-large (Fairseq), lr=3e-5, max tokens/batch 1024, beam search (size 2-8) + length penalty (0.2-1.0) grid search
- **입력 공간**: Abstract-only (159 words, 압축비 7.6) vs AIC (Abstract+Intro+Conclusion, 993 words, 압축비 47.3)
- **Extractive baselines**: PACSUM (비지도, BERT encoder), BERTSumExt (지도), MatchSum (Siamese BERT)
- **평가**: Multi-target max Rouge (각 gold TLDR 중 최고 Rouge 선택), nugget 기반 informativeness (MRR), 원저자 correctness 평가 (1-3 scale)

## Originality

- **Extreme summarization for science**: 과학 논문 도메인에서 단일 문장 수준의 극단적 요약 태스크를 최초로 정의하고 벤치마크화
- **Peer review 재작성 annotation protocol**: 논문 전체를 읽지 않고도 고품질 요약을 생성할 수 있는 효율적 annotation 방법 -- peer review의 자연적 요약 활용
- **Multi-target 평가 프레임워크**: 저자(TLDR-Auth)와 리뷰어(TLDR-PR)의 다양한 관점을 반영하는 복수 gold summary, 요약 평가의 변동성 문제를 완화
- **Title scaffolding (CATTS)**: 논문 제목이라는 자연적으로 풍부한 신호를 control code 기반 scaffold task로 활용하여 데이터 부족 문제를 해결하는 간단하면서 효과적인 접근
- **Nugget 기반 정보 유형 분석**: TLDR의 정보 구성요소를 체계적으로 분류하고 저자 vs 리뷰어 관점의 차이를 정량화

## Limitation & Further Study

### 저자들이 언급한 한계

- 실험이 abstract-only와 AIC 입력 공간에 한정되며, full text 활용 실험은 oracle 분석에 그침
- CS 도메인(주로 ICLR 85.2%) 한정으로, 다른 학문 분야에서 TLDR의 정의와 내용이 달라질 수 있음
- Multi-target 평가에서 max Rouge를 사용하나, 이것이 요약 품질의 완전한 지표인지 불확실

### 자체판단 아쉬운 점

- 데이터셋 규모(3.2K 논문)가 다른 요약 데이터셋(XSUM 226K, ArXiv 215K) 대비 매우 작아, 모델의 일반화 능력이 제한적
- CATTS의 성능 향상 폭이 Rouge-1 기준 +0.5~+2.0으로, 통계적 유의성을 확보한 경우와 그렇지 못한 경우가 혼재
- Correctness 평가에서 CATTS와 BART 간 유의미한 차이가 없어(둘 다 2.5/3.0), CATTS의 factual accuracy 개선 효과가 불명확
- Peer review 재작성 과정에서 리뷰어의 해석/편향이 TLDR에 반영될 수 있으나 이에 대한 분석 부족
- 생성된 TLDR의 faithfulness(hallucination) 문제에 대한 체계적 분석이 없음

### 후속 연구

- 과학 논문의 구조적 속성(섹션, 인용 맥락, discourse role)을 활용한 TLDR 생성 모델
- Full text 입력을 위한 long-context 모델(Longformer 등) 적용
- 다른 학문 분야(생의학, 물리학 등)로의 확장 및 분야별 TLDR 특성 분석
- Faithfulness/hallucination 감소를 위한 제약 기반 생성
- Semantic Scholar TLDR 기능으로 실제 대규모 배포 (실제로 후속 구현됨)

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 4/5 |
| Technical Soundness | 4/5 |
| Significance | 4/5 |
| Clarity | 5/5 |
| Overall | 4/5 |

**총평**: 과학 논문의 extreme summarization이라는 실용적이면서 학술적으로도 흥미로운 새 태스크를 정의하고, peer review 재작성이라는 창의적 annotation protocol과 multi-target 평가 프레임워크를 제안한 것이 핵심 기여이다. CATTS의 title scaffolding 아이디어는 단순하면서 효과적이며, 풍부한 데이터 분석(nugget 분류, 변동성 분석)과 다각적 평가(자동 메트릭 + nugget informativeness + 원저자 correctness)가 논문의 완성도를 높인다. Semantic Scholar의 TLDR 기능으로 실제 대규모 서비스에 적용되어 실용적 영향력도 입증되었다.
