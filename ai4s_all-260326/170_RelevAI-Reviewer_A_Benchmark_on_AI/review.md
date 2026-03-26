# RelevAI-Reviewer: A Benchmark on AI Reviewers for Survey Paper Relevance

> **저자**: Paulo Henrique Couto, Quang Phuoc Ho, Nageeta Kumari, Benedictus Kent Rachmat, Thanh Gia Hieu Khuong, Ihsan Ullah, Lisheng Sun-Hosoya | **날짜**: 2024 | **Conference**: CAp 2024 (Conf. sur l'Apprentissage automatique) | **소속**: Universite Paris-Saclay, ChaLearn

---

## Essence

서베이 논문의 "관련성(relevance)" 평가를 4-class 분류 문제로 정식화하고, 이를 위한 벤치마크 데이터셋(25,164 인스턴스, 총 100,656 prompt-paper 쌍)과 베이스라인 시스템(RelevAI-Reviewer)을 제안한 연구이다. BERT + thermometer encoding 조합이 Kendall's Tau 0.928을 달성하여, SVM(0.761)과 cosine similarity baseline(0.774)을 크게 상회했다.

## Motivation

- **알려진 것**: 학술 피어리뷰 프로세스는 느리고 편향에 취약하며, AI를 활용한 리뷰 자동화 연구가 증가 추세
- **Gap**: 기존 연구는 피어리뷰의 전반적 품질 평가에 집중했으나, "call for papers" 프롬프트에 대한 논문의 관련성(relevance)이라는 구체적 기준을 체계적으로 벤치마킹한 데이터셋과 과제가 부재
- **왜 중요한가**: 관련성 평가는 피어리뷰의 가장 기본적이고 중요한 기준 중 하나로, 이를 자동화하면 리뷰어 배정, 데스크 리젝트, 서베이 논문 큐레이션 등에 즉시 활용 가능
- **접근법**: Semantic Scholar에서 서베이 논문을 수집하고, reverse-engineering으로 프롬프트를 생성한 후 4단계 관련성 레이블을 부여하여 분류 벤치마크를 구축

## Achievement

1. **데이터셋 구축**: 22개 학문 분야에서 25,164개 인스턴스(각 인스턴스: 1 프롬프트 + 4개 후보 논문)를 수집, 4단계 관련성 레이블(most/second most/second least/least relevant) 부여
2. **BERT 최고 성능**: BERT + thermometer encoding이 Kendall's Tau 0.928(SE 0.002), most relevant 클래스 F1 0.994를 달성
3. **Thermometer encoding 효과 검증**: One-hot(0.893) 대비 thermometer encoding(0.928)이 약 3% 향상 -- 동일 프롬프트 내 중복 랭크 문제를 해소
4. **데이터 효율성 발견**: 전체 학습 데이터의 약 10%(~5,032개)만으로도 성능 plateau에 근접, 학습 리소스 절감 가능
5. **공개 벤치마크 챌린지**: CodaBench 플랫폼에 공개 챌린지를 개설하여 커뮤니티 참여 유도

## How

- **데이터 수집**: Semantic Scholar API에서 서베이 논문(title, abstract) 수집, ~30,000편에서 품질 관리 후 25,164편 선정
- **프롬프트 생성**: "Write a systematic survey or overview about [paper title + abstract]" 형식으로 reverse-engineering
- **관련성 레이블링**: most relevant(프롬프트 원본 논문), second most(원본의 참고문헌), second least(같은 분야 랜덤), least relevant(다른 분야)
- **Related Work 생성**: Semantic Scholar로 접근 불가한 경우 GPT-3.5-turbo로 인공 Related Work 섹션 생성
- **베이스라인 모델**:
  - Cosine similarity baseline (SentenceTransformer 임베딩 기반 고정 임계값)
  - SentenceTransformer + scikit-learn 분류기 (SVM, KNN, Random Forest, Logistic Regression)
  - BERT (bert-base-uncased) + one-hot encoding / thermometer encoding
- **평가 지표**: Kendall's Tau (랭킹 상관), 클래스별 F1-score, bootstrap standard error
- **학습 환경**: Kaggle P100 GPU, batch size 4, Adam optimizer, 80/20 train-test split

## Originality

- **Relevance 중심 벤치마크**: 피어리뷰의 5가지 기준(relevance, contribution, soundness, clarity, responsibility) 중 가장 기본적인 relevance에 특화된 최초의 대규모 벤치마크 데이터셋
- **Reverse-engineering 프롬프트**: 기존 서베이 논문의 제목+초록에서 역으로 "call for papers" 프롬프트를 생성하는 방식으로 대규모 레이블링을 자동화
- **Thermometer encoding 적용**: 순서형(ordinal) 관련성 레이블의 특성을 살려 thermometer encoding을 도입, 동일 프롬프트 내 중복 랭크 문제를 구조적으로 해결
- **공개 챌린지 설계**: CodaBench 기반 공개 벤치마크로 설계하여 재현성과 커뮤니티 참여를 제도적으로 보장

## Limitation & Further Study

### 저자들이 언급한 한계

- 서베이 논문에만 한정되어, 일반 연구 논문으로의 확장이 필요
- 제목, 초록, 인공 생성 Related Work만 사용하여 논문 전문(full-text)의 깊이를 반영하지 못함
- 프롬프트가 기존 논문 기반으로 역생성되어 데이터셋에 편향이 유입될 가능성
- 인용 논문을 ground truth로 사용하지만, 인용되지 않은 더 관련 있는 논문이 존재할 수 있음
- 4-class 분류 정식화로 인해 동일 관련성을 가진 두 논문을 구분하지 못하는 한계

### 자체판단 아쉬운 점

- **관련성 레이블의 조잡함**: "같은 분야 랜덤 논문 = second least", "다른 분야 논문 = least"라는 휴리스틱은 실제 관련성의 미세한 차이를 포착하지 못하며, 특히 second most(참고문헌)와 second least(같은 분야 랜덤) 간 경계가 자의적
- **LLM 기반 방법 미비교**: GPT-3.5/4, Claude 등 최신 LLM의 zero-shot/few-shot 관련성 판단과 비교하지 않아, BERT 기반 접근의 상대적 위치가 불분명
- **인공 Related Work의 품질**: GPT-3.5-turbo로 생성한 Related Work 섹션이 실제 논문의 Related Work와 얼마나 유사한지에 대한 품질 검증이 부족하여, 모델이 인공 텍스트의 패턴을 학습했을 가능성
- **태스크의 실용적 가치 제한**: "most relevant 논문 = 프롬프트 원본 논문"이므로, 모델이 단순히 프롬프트와 논문의 어휘적 유사도를 학습하는 것일 수 있음 -- cosine similarity baseline이 이미 most relevant에서 F1 0.943 달성
- **단일 모델 아키텍처**: BERT-base만 실험하고, RoBERTa, DeBERTa, SciBERT 등 학술 텍스트에 특화된 모델과의 비교가 없음

### 후속 연구

- 서베이 논문 외 일반 연구 논문, 다양한 문서 유형으로 데이터셋 확장
- 논문 전문(full-text) 분석 통합 및 새로운 유사도 메트릭 탐구
- GPT-4, Claude 등 최신 LLM과의 zero-shot/few-shot 성능 비교
- Relevance 외 나머지 4개 기준(Contribution, Soundness, Clarity, Responsibility)으로 벤치마크 확장
- 인간 전문가 평가와의 일치도(inter-annotator agreement) 분석을 통한 벤치마크 검증

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 3/5 |
| Technical Soundness | 3/5 |
| Significance | 2/5 |
| Clarity | 4/5 |
| Overall | 3/5 |

**총평**: 서베이 논문의 관련성 평가를 분류 문제로 정식화하고 대규모 벤치마크를 구축한 점은 실용적 기여가 있다. Thermometer encoding의 도입과 데이터 효율성 분석도 유의미하다. 그러나 관련성 레이블링의 휴리스틱이 조잡하고(특히 second most/second least 경계), 프롬프트가 원본 논문에서 역생성되어 태스크 자체가 어휘 유사도 판별에 가까워질 수 있다는 근본적 한계가 있다. 최신 LLM과의 비교가 없어 2024년 시점에서의 실질적 baseline 가치가 제한적이며, 서베이 논문만을 대상으로 한 범위 제한도 일반화를 어렵게 한다.
