# Sci2Pol: Evaluating and Fine-tuning LLMs on Scientific-to-Policy Brief Generation

> **저자**: Weimin Wu, Alexander C. Furnas, Eddie Yang, Gefei Liu, Akhil Pandey Akella, Xuefeng Song, Dashun Wang, Han Liu | **날짜**: 2025-09-25 | **Journal**: arXiv preprint | **DOI**: [10.48550/arXiv.2509.21493](https://doi.org/10.48550/arXiv.2509.21493)
> **리뷰 모드**: Abstract 기반 (PDF 없음)

---

## Essence

LLM이 과학 논문으로부터 정책 브리프를 얼마나 잘 생성할 수 있는가? 이 논문은 과학-정책 브리프 생성 작업을 위한 최초의 벤치마크(Sci2Pol-Bench)와 학습 데이터셋(Sci2Pol-Corpus)을 구축한다. 핵심 발견은 두 가지다: (1) BERTScore와 ROUGE 같은 기존 평가 지표가 브리프 작성 품질을 포착하지 못하며, LLM 기반 평가 지표가 전문가 판단과 더 잘 정렬된다; (2) Sci2Pol-Corpus로 파인튜닝한 Gemma-27B가 훨씬 큰 GPT-4o와 DeepSeek-V3(671B)를 능가한다. 5.6백만 정책 기록에서 출발하여 LLM-as-a-judge 필터링으로 최종 639개 고품질 쌍을 구성한 방법론이 핵심 기여다.

## Originality (Abstract 기반)

- [authorship, novelty] "We propose Sci2Pol-Bench and Sci2Pol-Corpus, the first benchmark and training dataset for evaluating and fine-tuning large language models (LLMs) on policy brief generation from a scientific paper."
- [authorship, action] "We build Sci2Pol-Bench on a five-stage taxonomy to mirror the human writing process: (i) Autocompletion, (ii) Understanding, (iii) Summarization, (iv) Generation, and (v) Verification."
- [result, finding] "for the Generation stage, we show that BERTScore and ROUGE scores fail to capture the quality of brief writing, and introduce a new LLM-based evaluation metric aligned with expert judgement."
- [result] "after fine-tuning, Gemma-27B surpasses the much larger GPT-4o and DeepSeek-V3 (671B)."

## How (방법론)

- **Sci2Pol-Bench 구축**:
  - 5단계 분류 체계: Autocompletion → Understanding → Summarization → Generation → Verification
  - 18개 태스크 (객관식 + 개방형 형식)
  - 13개 LLM 평가 (오픈소스 + 상용)
- **Sci2Pol-Corpus 구축**:
  - 580만 정책 기록에서 인용된 과학 논문 추적 → 14만 후보 쌍 생성
  - LLM-as-a-judge로 고품질 예시 필터링
  - 전문가 작성 3개 샘플을 참조로 in-context 정제(polishing)
  - 최종 639개 고품질 과학논문-정책브리프 쌍
- **파인튜닝**: LLaMA-3.1-8B, Gemma-12B, Gemma-27B 세 모델 Sci2Pol-Corpus로 파인튜닝
- **평가 지표**: BERTScore, ROUGE의 한계 실증 후 LLM 기반 새 지표 도입 및 전문가 판단과의 정렬 검증

## Why (중요성)

- 과학과 정책 사이의 간극을 줄이는 것은 기후, 보건, 기술 분야에서 증거 기반 의사결정의 필수 조건
- 기존 요약 지표(BERTScore, ROUGE)가 정책 브리프 작성 품질을 포착하지 못한다는 발견은 도메인 특화 평가 지표 개발의 필요성을 실증
- 639개 고품질 쌍이라는 소규모 데이터로 Gemma-27B가 671B 모델을 능가한다는 결과는 **데이터 품질이 모델 크기보다 중요**할 수 있음을 시사
- 580만 정책 기록과의 연결로 구축한 Sci2Pol-Corpus는 과학-정책 번역 자동화 연구의 핵심 인프라가 될 잠재력

## Limitation

### 저자들이 언급한 한계
- 639개의 최종 데이터셋이 소규모 — 다양한 과학 분야와 정책 유형을 충분히 커버하는지 의문
- LLM-as-a-judge 필터링이 특정 LLM의 편향을 상속할 수 있음

### 자체판단 아쉬운 점
- 5단계 분류 체계가 실제 정책 브리프 작성 프로세스를 얼마나 정확히 반영하는지 정책 전문가의 검증이 필요
- Gemma-27B의 GPT-4o 능가가 Sci2Pol-Bench에 한정된 결과인지, 실제 정책 활용에서도 검증되는지 불명확
- 생성된 정책 브리프가 실제 정책 입안자에게 유용한지에 대한 downstream 평가 부재

### 후속 연구
- 더 많은 과학 분야(의학, 공학, 사회과학)와 정책 유형(입법, 행정, 국제)으로 Sci2Pol-Corpus 확장
- 정책 입안자 대상 실제 활용성 평가 (user study)
- 과학-정책 번역에 특화된 도메인 적응 사전학습 탐색

## 평가

| 항목 | 점수 |
|------|------|
| Novelty | 5/5 |
| Technical Soundness | 4/5 |
| Significance | 4/5 |
| Clarity | 4/5 |
| Overall | 4/5 |

**총평**: 과학-정책 브리프 생성을 위한 최초의 벤치마크와 학습 데이터셋을 구축하고, 기존 평가 지표의 한계를 실증하며, 소규모 고품질 데이터로 대형 모델을 능가하는 파인튜닝 방법을 제시한 시의적절한 기여다. 639개 데이터의 소규모성이 주요 한계이나, 과학-정책 인터페이스 자동화 연구의 중요한 출발점을 제공한다.
