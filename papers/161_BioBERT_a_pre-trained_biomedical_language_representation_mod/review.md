---
title: "161_BioBERT_a_pre-trained_biomedical_language_representation_mod"
authors:
  - "Jinhyuk Lee"
  - "WonJin Yoon"
  - "Sungdong Kim"
  - "Donghyeon Kim"
  - "Sunkyu Kim"
date: "2019"
doi: "10.1093/bioinformatics/btz682"
arxiv: ""
score: 4.6
essence: "생의학 문헌의 급증에 따라 생의학 텍스트 마이닝의 중요성이 높아지고 있으나, 일반 도메인에서 사전학습된 BERT를 직접 적용하면 어휘 분포의 차이로 인해 성능이 저하되는 문제를 해결하기 위해, 저자들은 PubMed와 PMC 생의학 코퍼스에서 추가 사전학습한 BioBERT를 제안하여 명명된 개체 인식(NER), 관계 추출(RE), 질의응답(QA)에서 기존 최고 성능 모델을 능가하는 성과를 달성했다."
tags:
  - "cat/AI-Powered_Scientific_Research_Frameworks"
  - "sub/Biological_Foundation_Models"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Lee et al._2019_BioBERT a pre-trained biomedical language representation model for biomedical text mining.pdf"
---

# BioBERT: a pre-trained biomedical language representation model for biomedical text mining

> **저자**: Jinhyuk Lee, WonJin Yoon, Sungdong Kim, Donghyeon Kim, Sunkyu Kim | **날짜**: 2019 | **DOI**: [10.1093/bioinformatics/btz682](https://doi.org/10.1093/bioinformatics/btz682)

---

## Essence

생의학 문헌의 급증에 따라 생의학 텍스트 마이닝의 중요성이 높아지고 있으나, 일반 도메인에서 사전학습된 BERT를 직접 적용하면 어휘 분포의 차이로 인해 성능이 저하되는 문제를 해결하기 위해, 저자들은 PubMed와 PMC 생의학 코퍼스에서 추가 사전학습한 BioBERT를 제안하여 명명된 개체 인식(NER), 관계 추출(RE), 질의응답(QA)에서 기존 최고 성능 모델을 능가하는 성과를 달성했다.

## Motivation

- **Known**: BERT와 같은 최신 자연언어처리(NLP) 모델은 일반 도메인(Wikipedia, BooksCorpus) 코퍼스에서 사전학습되었으며, 다양한 NLP 과제에서 강력한 성능을 보임. 생의학 텍스트 마이닝은 LSTM-CRF 등 딥러닝 기법의 발전으로 진전되고 있음.

- **Gap**: 일반 도메인과 생의학 도메인의 어휘 분포가 현저히 다름. BRCA1, c.248T>C 같은 도메인 특화 고유명사와 용어들이 생의학 코퍼스에 풍부하게 존재하여, 일반 도메인에서 사전학습된 모델을 직접 적용하면 성능이 저하됨.

- **Why**: 일일 평균 3,000개 이상의 새 논문이 발표되고 PubMed에만 2,900만 개 이상의 기사가 존재하는 상황에서, 생의학 텍스트에서 정보를 효율적으로 추출하기 위한 도구가 절실함.

- **Approach**: BERT를 생의학 코퍼스(PubMed 초록 및 PMC 전문 기사)에서 추가로 사전학습하여 도메인 특화 BioBERT 모델을 개발하고, 이를 NER, RE, QA 등 다양한 생의학 텍스트 마이닝 과제에 적용 평가함.

## Achievement

![Figure 1](figure1_overview.png)
*Figure 1. BioBERT의 사전학습 및 미세조정 개요*

1. **생의학 NER 성능**: 기존 최고 성능 모델 대비 0.62% F1 점수 향상 달성. BioBERT는 WordPiece 임베딩을 직접 학습하여 생의학 도메인 특화 표현 습득.

2. **관계 추출 성능**: 기존 최고 성능 모델 대비 2.80% F1 점수 향상. [CLS] 토큰 기반 문장 분류로 엔티티 간의 관계를 효과적으로 판별.

3. **질의응답 성능**: BioASQ 데이터셋에서 12.24% MRR(Mean Reciprocal Rank) 향상. SQuAD 사전학습을 활용한 추가 성능 개선.

4. **일관된 아키텍처**: 거의 동일한 구조로 여러 과제에 최소한의 수정만으로 적용 가능한 범용성 입증.

## How

![Figure 2](figure2_pretraining.png)
*Figure 2. (a) PubMed 코퍼스 크기 변화에 따른 성능 (b) 다양한 사전학습 단계에서 BioBERT의 NER 성능*

**사전학습 전략**:
- BERT 가중치로 초기화 후 PubMed 초록과 PMC 전문 기사로 추가 사전학습 (8개 NVIDIA V100 GPU에서 23일간 학습)
- 마스크 언어 모델(Masked Language Model) 기반 양방향 학습으로 생의학 용어의 문맥 의존적 표현 학습
- 원본 BERT의 WordPiece 어휘 유지하여 호환성 보장하면서도 생의학 도메인에 최적화

**미세조정 전략**:
- **NER**: 각 토큰 수준의 BIO2 확률 계산, 엔티티 수준 평가 메트릭(정확도, 재현율, F1) 사용
- **RE**: [CLS] 토큰 기반 문장 분류, 대상 엔티티를 @GENE$, @DISEASE$ 같은 태그로 익명화
- **QA**: SQuAD 아키텍처 차용, 답변 구간의 시작/종료 위치에 대한 토큰 수준 확률 계산. 추출 불가능한 질문 약 30% 제외

**코퍼스 조합 실험**:
- Wiki+Books, Wiki+Books+PubMed, Wiki+Books+PubMed+PMC 등 다양한 조합으로 사전학습 전략 검증
- PubMed 코퍼스 크기 확대에 따른 점진적 성능 향상 관찰

## Originality

- **최초 도메인 특화 BERT 모델**: BioBERT는 대규모 생의학 코퍼스에서 사전학습된 최초의 BERT 기반 도메인 특화 모델 제시.

- **다중 과제 범용성**: 기존 생의학 텍스트 마이닝 연구는 NER 또는 QA 같은 단일 과제에 집중했으나, BioBERT는 최소한의 아키텍처 수정으로 여러 과제에서 최고 성능 달성.

- **양방향 문맥 표현**: 생의학 텍스트의 복잡한 엔티티 관계 이해에 양방향 표현이 필수적임을 실증적으로 입증.

- **재현성과 개방성**: 사전학습 가중치, 소스 코드, 전처리된 데이터셋을 공개하여 연구 재현성 보장 및 후속 연구 가능성 제공.

## Limitation & Further Study

- **어휘 선택의 보수성**: 호환성을 위해 BERT 원본 어휘를 유지했으나, 생의학 도메인에 최적화된 새로운 WordPiece 어휘 구성이 추가 성능 향상을 가져올 가능성 미검증.

- **추출 기반 QA의 한계**: BioASQ 질문의 약 30%가 추출 방식으로는 답변 불가능하여, 생성 기반 QA 모델 개발 필요.

- **도메인 외 일반화**: 생의학 이외의 다른 특화 도메인(법률, 금융 등)에 대한 동일 접근의 효과성 미검증.

- **언어 범위**: 영어 중심의 분석으로, 다국어 생의학 텍스트 마이닝에의 확장 필요.

- **후속 연구 방향**: (1) 동적 어휘 확장 메커니즘, (2) 다중 도메인 적응 사전학습 전략, (3) 생의학 분야별(임상, 유전학 등) 특화 모델 개발.


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4.5/5
- Significance: 5/5
- Clarity: 4.5/5
- Overall: 4.6/5

**총평**: BioBERT는 도메인 특화 사전학습의 중요성을 명확히 입증하며, 생의학 텍스트 마이닝 커뮤니티에 실질적이고 즉시 활용 가능한 기여를 제공한 연구다. 공개된 모델과 코드는 이후 생의학 NLP 분야의 발전을 견인한 중요한 기초 자산이 되었다.

## Related Papers

- 🔄 다른 접근: [[papers/696_Scaling_Large_Language_Models_for_Next-Generation_Single-Cel/review]] — 생의학 텍스트 전용 BERT와 단일세포 데이터를 텍스트로 변환하여 처리하는 LLM이 생의학 데이터 처리의 서로 다른 접근법을 보여준다
- 🏛 기반 연구: [[papers/720_Scientific_Large_Language_Models_A_Survey_on_Biological__Che/review]] — 생의학 도메인 특화 언어모델의 초기 연구로서 이후 과학 분야 대형언어모델 발전의 중요한 기반이 되었다
- 🔄 다른 접근: [[papers/367_Galactica_A_Large_Language_Model_for_Science/review]] — 도메인 특화 사전학습과 범용 과학 언어모델이 각각 전문성과 범용성 측면에서 다른 접근법을 제시한다
- 🏛 기반 연구: [[papers/707_SciBERT_A_Pretrained_Language_Model_for_Scientific_Text/review]] — 생의학 도메인 특화 BERT 모델의 선구적 연구로서 과학 텍스트 처리를 위한 언어모델 개발의 중요한 출발점이다
- 🔄 다른 접근: [[papers/696_Scaling_Large_Language_Models_for_Next-Generation_Single-Cel/review]] — 단일세포 데이터 텍스트 변환 방식과 생의학 텍스트 전용 언어모델이 생의학 빅데이터 처리의 상반된 접근법을 보여준다
- 🏛 기반 연구: [[papers/344_Foundation_models_in_bioinformatics/review]] — BioBERT의 생의학 언어 표현 사전훈련이 생물정보학 기초 모델 발전의 중요한 선행 연구입니다.
- 🔗 후속 연구: [[papers/734_ScispaCy_Fast_and_Robust_Models_for_Biomedical_Natural_Langu/review]] — 생의학 언어 표현 모델인 BioBERT의 발전을 실용적 NLP 파이프라인으로 확장한 사례이다.
- 🔗 후속 연구: [[papers/152_BERT_Pre-training_of_Deep_Bidirectional_Transformers_for_Lan/review]] — BERT를 생의학 도메인에 특화시켜 의료 텍스트 이해 성능을 개선함
- 🏛 기반 연구: [[papers/707_SciBERT_A_Pretrained_Language_Model_for_Scientific_Text/review]] — BioBERT의 생의학 도메인 특화 아이디어를 더 넓은 과학 분야로 확장한 연구
