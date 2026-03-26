# BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding

> **저자**: Jacob Devlin, Ming-Wei Chang, Kenton Lee, Kristina Toutanova | **날짜**: 2018 | **학회**: arXiv (NAACL 2019 발표) | **DOI**: 10.48550/ARXIV.1810.04805

---

## Essence

BERT(Bidirectional Encoder Representations from Transformers)는 Masked Language Model(MLM)과 Next Sentence Prediction(NSP)이라는 두 가지 비지도 사전학습 목표를 통해 깊은 양방향 Transformer 표현을 학습하는 언어 모델이다. 사전학습된 BERT에 단일 출력 레이어만 추가하여 fine-tuning하면, 11개 NLP 태스크에서 동시에 SOTA를 달성하며, task-specific architecture 설계의 필요성을 근본적으로 감소시켰다.

## Motivation

- **알려진 것**: ELMo(feature-based, 독립적 L2R+R2L LSTM 결합)와 OpenAI GPT(fine-tuning, 단방향 left-to-right Transformer)가 사전학습 언어 표현의 유효성을 입증
- **Gap**: 기존 방법들은 단방향 언어 모델에 기반하여 좌우 문맥을 동시에 활용하지 못하며, 특히 QA, NER 등 토큰 수준 태스크에서 양방향 문맥이 필수적임에도 구조적으로 이를 제한
- **왜 중요한가**: 범용적 양방향 사전학습 표현을 확보하면, 다양한 NLP 태스크에 대해 task-specific architecture를 최소화하면서 SOTA 성능 달성 가능
- **접근법**: Cloze task에서 영감받은 MLM으로 양방향 conditioning을 가능하게 하고, NSP로 문장 간 관계 학습을 추가하여 통합된 pre-train & fine-tune 프레임워크 구축

## Achievement

1. **GLUE 벤치마크**: 평균 82.1% (7.0%p 향상) -- MNLI 86.7% (+4.6%p), CoLA 60.5 (+15.1), RTE 70.1 (+8.4) 등 8개 태스크 전부에서 SOTA
2. **SQuAD v1.1**: Test F1 93.2 (앙상블) -- 인간 성능(91.2) 및 기존 최고 시스템(91.7) 초과, 단일 모델도 F1 91.1로 앙상블 시스템 수준
3. **SQuAD v2.0**: Test F1 83.1 -- 기존 최고 대비 +5.1 F1 향상 (답이 없는 질문 포함)
4. **SWAG**: Test accuracy 86.3% -- OpenAI GPT(78.0%) 대비 +8.3%p, 인간 전문가(85.0%) 초과
5. **NER (CoNLL-2003)**: Feature-based 접근(상위 4개 레이어 결합)으로도 F1 96.1 달성, fine-tuning(96.6)과 0.5 차이로 feature-based 활용 가능성 입증

## How

- **모델 구조**: Multi-layer bidirectional Transformer encoder -- BERT_BASE (L=12, H=768, A=12, 110M params), BERT_LARGE (L=24, H=1024, A=16, 340M params)
- **입력 표현**: WordPiece embedding (30K vocab) + Segment embedding (A/B) + Position embedding의 합, [CLS] 토큰(분류용) + [SEP] 토큰(문장 구분)
- **사전학습 Task 1 -- MLM**: 입력 토큰의 15%를 랜덤 선택하여 80% [MASK], 10% 랜덤 토큰, 10% 원본 유지 → 원본 토큰 예측. 양방향 conditioning의 trivial prediction 문제 회피
- **사전학습 Task 2 -- NSP**: 50% 실제 다음 문장 / 50% 랜덤 문장 → 이진 분류. QA, NLI 등 문장 관계 태스크에 유효
- **사전학습 데이터**: BooksCorpus (800M words) + English Wikipedia (2,500M words), document-level corpus 사용
- **학습 설정**: Batch 256 sequences (128K tokens/batch), 1M steps (~40 epochs), Adam lr=1e-4, warmup 10K steps, dropout 0.1, GELU activation
- **인프라**: BERT_BASE 4 Cloud TPUs (16 chips), BERT_LARGE 16 Cloud TPUs (64 chips), 각 4일 소요
- **Fine-tuning**: Task-specific 출력 레이어만 추가, 전체 파라미터 fine-tune, batch 16-32, lr 2e-5~5e-5, 2-4 epochs, 단일 TPU에서 최대 1시간

## Originality

- **Masked Language Model (MLM)**: Cloze task의 현대적 재해석으로, 양방향 Transformer 사전학습을 가능하게 한 핵심 혁신. 단순히 L2R과 R2L을 결합(ELMo)하는 것이 아닌, 모든 레이어에서 좌우 문맥을 jointly conditioning
- **Pre-train/Fine-tune mismatch 해결**: [MASK] 토큰이 fine-tuning에 없는 문제를 80/10/10 masking 전략으로 완화 -- 개념적으로 단순하면서도 실용적
- **통합된 Fine-tuning 패러다임**: 단일 사전학습 모델로 sentence-level(분류, NLI)과 token-level(QA, NER) 태스크를 동일한 구조로 처리. Task-specific architecture 설계 패러다임의 근본적 전환
- **Scaling의 보편적 효과 실증**: 극소량 학습 데이터(MRPC 3.6K, RTE 2.5K)에서도 대형 모델(340M)이 일관되게 소형 모델(110M)을 능가함을 최초로 체계적으로 입증

## Limitation & Further Study

### 저자들이 언급한 한계

- MLM은 배치당 15% 토큰만 예측하므로 LTR 대비 수렴이 느림 (더 많은 사전학습 step 필요)
- BERT_LARGE는 소규모 데이터셋에서 fine-tuning이 불안정하여 random restart 필요
- [CLS] 벡터는 NSP 학습 없이는 의미 있는 문장 표현이 되지 않음

### 자체판단 아쉬운 점

- 생성(generation) 태스크에 대한 평가가 전혀 없음 -- encoder-only 구조의 한계로 text generation, summarization, translation 등에 직접 적용 불가
- NSP의 실제 기여도가 후속 연구(RoBERTa 등)에서 논란이 되었으나, 본 논문에서는 NSP 제거 시 성능 하락만 보고하고 대안적 문장 관계 학습 방법을 탐색하지 않음
- 사전학습에 English 텍스트만 사용하여 다국어 일반화에 대한 논의 부재 (후속 mBERT에서 다룸)
- 계산 비용(64 TPU chips, 4일)에 대한 분석이나 효율성 관점의 논의가 부족
- 512 토큰 제한으로 인한 장문 문서 처리 한계가 언급되지 않음

### 후속 연구

- RoBERTa: NSP 제거 및 dynamic masking으로 최적화
- ALBERT: 파라미터 효율화 (factorized embedding, cross-layer sharing)
- XLNet: Permutation language modeling으로 MLM의 한계 극복
- 다국어 확장 (mBERT, XLM)
- Domain-specific BERT (SciBERT, BioBERT, ClinicalBERT 등)
- BERT의 attention 패턴 해석 연구 (BERTology)

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 5/5 |
| Technical Soundness | 5/5 |
| Significance | 5/5 |
| Clarity | 5/5 |
| Overall | 5/5 |

**총평**: NLP 분야의 패러다임을 근본적으로 전환시킨 landmark 논문이다. MLM이라는 개념적으로 단순한 혁신을 통해 깊은 양방향 사전학습을 가능하게 하고, "pre-train then fine-tune" 패러다임을 확립하여 task-specific architecture 설계의 시대를 종식시켰다. 11개 벤치마크에서의 압도적 성능 향상, 풍부한 ablation study, 그리고 코드/모델 공개를 통해 후속 연구의 폭발적 성장을 촉발한 점에서 NLP 역사상 가장 영향력 있는 논문 중 하나이다.
