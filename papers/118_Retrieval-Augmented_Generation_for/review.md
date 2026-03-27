# Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks

- **저자**: Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman Goyal, Heinrich Kuttler, Mike Lewis, Wen-tau Yih, Tim Rocktaschel, Sebastian Riedel, Douwe Kiela
- **소속**: Facebook AI Research; University College London; New York University
- **발표**: NeurIPS 2020 (arXiv:2005.11401)
- **DOI**: [10.48550/ARXIV.2005.11401](https://doi.org/10.48550/ARXIV.2005.11401)

---

## Essence (핵심 요약)

사전학습된 seq2seq 모델(BART)의 parametric memory와 Wikipedia 기반 dense vector index의 non-parametric memory를 결합한 **Retrieval-Augmented Generation (RAG)** 프레임워크를 제안한다. 입력 쿼리에 대해 DPR(Dense Passage Retriever)로 관련 문서를 검색하고, 검색된 문서를 latent variable로 취급하여 생성 과정에서 marginalize하는 두 가지 변형(RAG-Sequence, RAG-Token)을 소개한다. 이를 통해 knowledge-intensive NLP 태스크 전반에서 범용적으로 적용 가능한 fine-tuning 레시피를 확립하였다.

---

## Motivation (연구 동기)

대규모 사전학습 언어 모델은 파라미터에 사실적 지식을 저장하지만, 지식의 **정확한 접근 및 조작이 제한**적이고, 예측의 **출처 제공(provenance)** 이 불가능하며, **hallucination** 문제가 존재한다. 또한 세상의 변화에 따라 모델의 지식을 갱신하려면 재학습이 필요하다. 기존의 REALM, ORQA 등 retrieval 결합 모델은 extractive QA에만 적용되어, **생성(generation) 태스크로의 확장**이 미개척 상태였다. 이러한 한계를 극복하기 위해 retrieval과 generation을 결합하는 범용 아키텍처가 필요하였다.

---

## Achievement (주요 성과)

1. **Open-domain QA에서 SOTA 달성**: Natural Questions (44.5 EM), WebQuestions (45.2 EM), CuratedTrec (52.2 EM) 세 벤치마크에서 기존 extractive 및 closed-book 모델을 상회
2. **생성 품질 향상**: BART 대비 더 사실적(factuality 42.7% vs 7.1%), 구체적(specificity 37.4% vs 16.8%), 다양한(distinct trigram 비율 53.8% vs 32.4%) 텍스트 생성
3. **FEVER 사실 검증**: retrieval supervision 없이도 SOTA 파이프라인 모델 대비 4.3% 이내의 성능 달성
4. **Index hot-swapping**: 문서 인덱스 교체만으로 모델의 세계 지식을 재학습 없이 갱신 가능 (2016 -> 2018 세계 지도자 질문에서 70%/68% 정확도)
5. **HuggingFace Transformers에 오픈소스 통합**

---

## How (방법론)

### 아키텍처
- **Retriever (p_eta)**: DPR 기반 bi-encoder 구조. BERT_BASE로 쿼리와 문서를 각각 인코딩하고, MIPS(Maximum Inner Product Search)로 top-K 문서 검색. Wikipedia를 100-word 청크로 분할하여 21M 문서 인덱스 구축 (FAISS + HNSW)
- **Generator (p_theta)**: BART-large (400M 파라미터). 입력 x와 검색 문서 z를 단순 concatenation하여 출력 생성

### 두 가지 변형
- **RAG-Sequence**: 전체 출력 시퀀스에 대해 동일한 문서를 사용하여 marginalize. 각 문서별로 beam search 후 결과를 합산 (Thorough/Fast Decoding)
- **RAG-Token**: 각 토큰별로 서로 다른 문서에서 정보를 가져와 marginalize. 표준 autoregressive 디코딩 가능

### 학습
- 검색 문서를 latent variable로 취급하여 negative marginal log-likelihood 최소화
- Document encoder는 고정, query encoder와 BART generator만 fine-tuning
- Adam optimizer, mixed precision training, 8x V100 GPU

---

## Originality (독창성)

1. **Parametric + Non-parametric memory의 범용적 결합**: 기존에 extractive QA에만 적용되던 retrieval-augmented 접근을 seq2seq 생성 모델로 최초 확장
2. **두 가지 marginalization 전략 (Sequence vs Token)**: 문서 활용 방식에 대한 설계 공간을 체계적으로 탐색. 특히 RAG-Token은 하나의 응답 내에서 여러 문서의 내용을 조합 가능
3. **End-to-end 학습**: retrieval supervision 없이 최종 태스크의 loss만으로 retriever와 generator를 공동 학습
4. **Index hot-swapping을 통한 지식 갱신**: parametric 모델의 재학습 없이 non-parametric memory 교체만으로 최신 지식 반영 가능성 실증

---

## Limitation & Further Study (한계 및 향후 연구)

### 한계
1. **Document encoder 고정**: 학습 중 document encoder를 업데이트하지 않아 retrieval 품질 개선에 한계. REALM처럼 주기적 인덱스 갱신 시 성능 향상 가능성 존재
2. **Wikipedia 단일 지식원 의존**: 21M 문서의 Wikipedia에 국한되어, 도메인 특화 지식이나 최신 정보에 대한 커버리지 부족
3. **Retrieval collapse 현상**: story generation 등 일부 태스크에서 retriever가 입력과 무관하게 동일 문서를 검색하는 붕괴 현상 발생
4. **확장성 제약**: 전체 Wikipedia 인덱스 저장에 ~100GB CPU 메모리 필요 (압축 후 36GB)
5. **BM25 대비 약점**: entity-centric 태스크(FEVER)에서는 단순 BM25가 dense retrieval보다 우수한 경우 존재

### 향후 연구 방향
- Retriever와 generator의 **공동 사전학습(joint pre-training)** 탐구
- Parametric/non-parametric memory 간 **상호작용 메커니즘** 심화 연구
- 다양한 도메인(의학, 법률 등)으로의 지식 인덱스 확장
- Retrieval collapse 방지를 위한 regularization 기법 개발

---

## Evaluation (총평)

RAG는 retrieval-augmented generation이라는 패러다임을 NLP 커뮤니티에 정립한 **기념비적 논문**이다. 제안 당시(2020) knowledge-intensive 태스크에서 parametric-only 모델과 extractive 모델의 한계를 명확히 진단하고, 두 메모리 유형의 결합이라는 우아한 해법을 제시하였다. 특히 RAG-Token의 토큰 단위 문서 활용과 index hot-swapping을 통한 지식 갱신 기능은 실용적 가치가 매우 높다.

다만 document encoder 고정, Wikipedia 단일 지식원, retrieval collapse 등의 한계가 있으며, 이후 RETRO, Atlas, Self-RAG 등 후속 연구에서 이러한 문제들이 점진적으로 해결되어 왔다. 현재 LLM 시대에서 RAG는 hallucination 완화와 최신 정보 반영을 위한 **사실상의 표준 접근법**으로 자리잡았으며, 본 논문은 그 이론적, 실험적 토대를 마련한 핵심 기여작이다.

논문의 실험 설계는 4개 QA 벤치마크 + 생성 + 분류 태스크를 아우르는 포괄적 평가와, retrieval ablation, BM25 비교, 인간 평가, diversity 분석 등 **체계적이고 다층적인 검증**을 수행하여 높은 신뢰도를 확보하였다. HuggingFace 통합을 통한 재현성 확보 또한 모범적이다.

## 평가
| 항목 | 점수 (1-5) |
|------|-----------|
| Novelty | 5 |
| Technical Soundness | 5 |
| Significance | 5 |
| Overall | 5.0 |

**총평**: 지식 집약적 NLP 과제에서 검색과 생성을 결합한 RAG 패러다임을 확립한 Facebook AI의 NeurIPS 2020 기념비적 논문으로, 현재 LLM 응용의 표준 아키텍처를 정초했다.
