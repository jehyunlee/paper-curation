---
title: "571_Neural_automated_writing_evaluation_with_corrective_feedback"
authors:
  - "Izia Xiaoxiao Wang"
  - "Xihan Wu"
  - "Edith Coates"
  - "Min Zeng"
  - "Jiexin Kuang"
date: "2024"
doi: "N/A"
arxiv: ""
score: 4.0
essence: "본 논문은 자동 쓰기 평가(AWE: Automated Writing Evaluation)와 문법 오류 수정(GEC: Grammatical Error Correction) 시스템을 통합하여, 제2언어 학습자에게 즉각적인 에세이 평점과 문법 수정 피드백을 동시에 제공하는 통합 시스템을 제시한다. 이를 통해 시험 시뮬레이션 환경을 구현하여 보다 실질적인 언어 학습 경험을 제공한다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/Multi-Agent_Language_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Wang et al._2024_Neural automated writing evaluation with corrective feedback.pdf"
---

# Neural automated writing evaluation with corrective feedback

> **저자**: Izia Xiaoxiao Wang, Xihan Wu, Edith Coates, Min Zeng, Jiexin Kuang, Siliang Liu, Mengyang Qiu, Jungyeul Park | **날짜**: 2024 | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp)
*시스템 워크플로우: 학습자가 에세이를 제출하면 자동 쓰기 평가(AWE)와 문법 오류 수정(GEC)을 통합하여 점수와 수정 피드백을 제공*

본 논문은 자동 쓰기 평가(AWE: Automated Writing Evaluation)와 문법 오류 수정(GEC: Grammatical Error Correction) 시스템을 통합하여, 제2언어 학습자에게 즉각적인 에세이 평점과 문법 수정 피드백을 동시에 제공하는 통합 시스템을 제시한다. 이를 통해 시험 시뮬레이션 환경을 구현하여 보다 실질적인 언어 학습 경험을 제공한다.

## Motivation

- **Known**: AWE와 GEC 시스템은 각각 별도로 개발되어 있으며, 신경망 기반 모델들이 각 분야에서 최첨단 성능을 달성하고 있음. 제2언어 교사와 학습자 모두 충분한 에세이 피드백이 필수적이라고 인식하고 있음.

- **Gap**: 기존 연구들은 두 시스템을 통합하지 않고 있으며, 개별 시스템의 학습 효과가 아직 실증적으로 검증되지 않았음. 대부분의 이전 통합 연구는 학습자의 인식(perception)만 조사했을 뿐, 실제 쓰기 성능 향상에 미치는 영향을 다루지 않음.

- **Why**: 수동 채점과 피드백은 교사에게 매우 시간 소비적이며, 학습자는 교사의 피드백을 이해하기 어려움. 통합 시스템을 통해 효율성과 비용 효율성을 동시에 달성할 수 있음.

- **Approach**: 신경망 기반의 AWE(점수 예측)와 GEC(문법 오류 수정) 시스템을 하나의 플랫폼에 통합하여, 학습자가 에세이를 제출하면 종합적인 점수(전체 점수 + 8가지 항목별 점수)와 인라인 문법 수정을 함께 제공.

## Achievement

![Figure 2](figures/fig2.webp)
*통합 AWE-GEC 시스템의 사용자 인터페이스: 원본 텍스트의 삭제된 토큰(빨간색), 추가된 문법 수정(초록색), AWE 점수(0-100 범위)*

1. **크로스-프롬프트 점수 제공**: ASAP++과 ASAP 데이터셋을 활용하여 8개의 서로 다른 프롬프트에 대한 종합적인 루브릭 점수(content, organization, word choice, sentence fluency, conventions 등) 제시. 단순 전체 점수가 아닌 다차원적 평가 결과 제공.

2. **고성능 GEC 모델**: BEA 2019 테스트셋에서 65.29 F₀.₅ 점수 달성. BERT 기반 seq2seq 모델과 데이터 증강(spell-checked 문장 추가로 157만→172만 문장쌍으로 확대)을 통해 강력한 문법 오류 수정 성능 구현.

3. **실용적 통합 플랫폼**: 학습자가 실제 시험 상황을 시뮬레이션할 수 있는 완전한 환경 구축. 에세이 제출부터 즉각적인 객관적 점수와 수정 피드백까지의 전 과정 자동화.

## How

- **AWE 모듈**:
  - RoBERTa-base 모델을 선형 회귀 작업(linear regression)에 사용
  - ASAP/ASAP++ 데이터셋 기반 학습으로 크로스-프롬프트 성능 확보
  - 텍스트 노이징(UTF-8 인코딩 오류, 비단어 엔티티 제거) 전처리 단계 추가
  - 점수 정규화(0-1 범위 → 0-100 범위) 적용
  
- **GEC 모듈**:
  - Fairseq 기반 seq2seq 아키텍처 구현
  - BERT/BART 기반 사전학습 언어모델 앙상블
  - FCE, NUCLE, W&I+LOCNESS, Lang-8 멀티데이터셋 활용
  - 맞춤법 검사 문장 추가로 데이터 증강 (1.57M → 1.72M 문장쌍)
  - ERRANT 도구로 원본 텍스트 복원

- **통합 워크플로우**:
  - 학습자가 에세이 제출 → 두 모듈 병렬 처리 → 인라인 수정된 텍스트 + 9개 점수(전체 + 8가지 항목별) 동시 반환

## Originality

- **신경망 기반 AWE-GEC 통합**: 선행 연구들이 비신경망 시스템의 통합이나 학습자 인식만 조사한 반면, 본 연구는 최신 신경망 모델을 활용한 실질적인 통합 시스템을 최초로 제시.

- **크로스-프롬프트 루브릭 점수**: 단순 전체 점수 대신 다양한 평가 기준(내용, 조직, 어휘 선택, 문장 유창성, 관례 등)에 대한 개별 점수를 제공하여 학습자에게 구체적인 개선 방향 제시.

- **텍스트 데노이징 파이프라인**: GPT-3.5를 활용한 프롬프트 기반 인코딩 오류 및 비단어 엔티티 제거, 그리고 ERRANT를 통한 원본 유지 기법으로 데이터 품질 향상.

- **실무 중심의 시스템 설계**: 교실 및 시험 환경에 직접 적용 가능한 완전한 사용자 인터페이스와 워크플로우 제공.

## Limitation & Further Study

- **평가 범위 제한**: 논문에서 추출된 부분까지는 시스템의 실제 학습 효과(학습자 점수 향상도)를 실증적으로 검증한 내용이 없음. 학습자 수행도 개선이 실제로 이루어지는지 확인 필요.

- **언어 특정성**: ASAP/ASAP++ 데이터셋이 영어 제2언어 학습에만 제한되어 있으며, 다른 언어로의 확장 가능성이 불명확.

- **GEC 성능**: 65.29 F₀.₅ 점수는 당시 최첨단이지만, 실제 학습자 에세이의 다양한 오류 패턴에 얼마나 일반화되는지 검토 필요.

- **후속 연구**:
  - 실제 교실 환경에서의 장기 효과 연구 (학습자 성취도, 만족도 측정)
  - 다국어 지원으로 시스템 확장
  - 학습자 프로필별 개인화된 피드백 제공
  - 반복 제출 시 성적 향상 추적 분석

## Evaluation

- **Novelty**: 4/5
  - 신경망 기반 AWE-GEC 통합은 새로우나, 개별 컴포넌트 기술은 기존 방법의 조합

- **Technical Soundness**: 4/5
  - RoBERTa 기반 AWE와 seq2seq GEC 구현은 견고하며, 데이터 전처리 및 증강 기법 적절
  - 다만 하이퍼파라미터 상세 설정이나 교차 검증 결과 부족

- **Significance**: 4/5
  - 제2언어 교육에 실질적 가치 있는 시스템을 제시하나, 실제 학습 효과 검증 미흡
  - 교사 업무 감소 및 학습자 접근성 향상은 중요한 기여

- **Clarity**: 4/5
  - 시스템 설계와 워크플로우가 명확하게 설명되었으며 인터페이스 스크린샷으로 직관적 이해 용이
  - 기술 상세 설명은 충분하나 몇몇 구현 세부사항 보완 필요

- **Overall**: 4/5

**총평**: 본 논문은 자동화 쓰기 평가와 문법 오류 수정을 신경망 기반으로 처음 통합하여 제2언어 학습자에게 실질적 가치를 제공하는 시스템을 제시했으나, 실제 학습 효과에 대한 실증적 검증과 장기 영향 분석이 보완되면 더욱 강력한 기여가 될 수 있다.

## Related Papers

- 🏛 기반 연구: [[papers/423_Improving_grammatical_error_correction_via_contextual_data_a/review]] — 문법 오류 수정을 위한 맥락적 데이터 증강 연구는 자동 쓰기 평가와 문법 오류 수정 통합 시스템의 기술적 기반이다.
- 🔗 후속 연구: [[papers/512_Lm-combiner_A_contextual_rewriting_model_for_chinese_grammat/review]] — 중국어 문법을 위한 맥락적 재작성 모델은 제2언어 학습자 대상 쓰기 평가 시스템을 다국어 환경으로 확장한다.
- ⚖️ 반론/비판: [[papers/284_Does_writing_with_language_models_reduce_content_diversity_a/review]] — 언어 모델과 함께 글쓰기할 때 내용 다양성이 감소한다는 연구는 자동 쓰기 평가 시스템이 창의성에 미칠 부정적 영향을 시사한다.
