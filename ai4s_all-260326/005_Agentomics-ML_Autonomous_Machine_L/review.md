# Agentomics-ML: Autonomous Machine Learning Experimentation Agent for Genomic and Transcriptomic Data

> **저자**: Vlastimil Martinek, Andrea Gariboldi, Dimosthenis Tzimotoudis, Aitor Alberdi Escudero, Edward Blake, David Cechak, Luke Cassar, Alessandro Balestrucci, Panagiotis Alexiou | **날짜**: 2025-06-05 | **Journal**: arXiv (preprint) | **DOI**: https://arxiv.org/abs/2506.05542

---

## Essence

Genomic/transcriptomic 데이터에 대한 classification 모델을 완전 자율적으로 생성하는 LLM 기반 agent 시스템으로, 사전 정의된 ML 실험 단계(데이터 탐색 -> 분할 -> 표현 -> 아키텍처 -> 학습 -> 추론)를 반복적으로 수행하며 reflection feedback을 통해 모델을 개선한다. 6개 벤치마크 데이터셋에서 93.33%의 success rate를 달성하여, 기존 agentic 시스템(AIDE, Data Interpreter)과 zero-shot LLM을 크게 능가했다.

## Motivation

- **알려진 것**: High-throughput -omics 기술이 분자생물학을 data-driven 과학으로 전환시켰으며, ML/DL 기법이 genomics, transcriptomics, drug discovery에서 혁신을 이끌고 있음
- **Gap**: LLM 기반 agentic ML 시스템이 구조화된 벤치마크에서는 성과를 보이나, 이질적인 computational biology 데이터셋에서는 일반화와 success rate에서 실패. 특히 variable-length 서열이나 multi-sequence 입력 같은 복잡한 데이터에서 기존 시스템이 작동 불가
- **왜 중요한가**: 시퀀싱 처리량이 ~7개월마다 배증하는 반면 분석 인력은 완만하게 증가하여 분석 병목이 심화
- **접근법**: 사전 정의된 ML 파이프라인 단계를 따르면서 Bash/Python 도구를 사용하고, scalar + verbal feedback의 reflection loop로 반복 개선하는 경량 agent 시스템 설계

## Achievement

1. **93.33% success rate**: 6개 genomic/transcriptomic 벤치마크에서 5회 반복 실행 시 전체 93.33% 성공률 (5/6 데이터셋에서 100%). AIDE는 10%, Data Interpreter는 최대 60% (단일 데이터셋)
2. **복잡 데이터셋 유일 성공**: AGO2_CLASH_Hejret (두 개의 가변 길이 RNA 서열 상호작용) 데이터셋에서 유일하게 작동하는 코드 생성 -- 다른 모든 zero-shot LLM 및 agentic 시스템은 0% 성공률
3. **Human SOTA 초과 달성**: Drosophila_enhancers_stark 데이터셋에서 0.72 accuracy로 기존 Human SOTA (0.59)를 초과
4. **Feedback loop 효과**: Iterative feedback 사용 시 80%의 경우에서 no-feedback 대비 개선, 평균 3.8% 상대 성능 향상. 2/6 데이터셋에서 통계적으로 유의 (t-test)
5. **비용 효율성**: Agent 1회 실행 비용 약 2 USD 미만

## How

- **아키텍처**: 사전 정의된 순차적 단계 -- (1) Data exploration, (2) Splitting, (3) Representation reasoning, (4) Architecture reasoning, (5) Training script + model file 생성, (6) Inference script + metrics 생성
- **도구**: Bash 명령 실행, Python 파일 작성/실행. Docker 컨테이너 내에서 격리 실행으로 보안 확보
- **출력 검증**: Pydantic AI 프레임워크로 파일 출력 단계를 프로그래밍적으로 검증. Inference script는 dummy data로 즉시 실행 검증. 검증 실패 시 재시도 강제
- **Reflection mechanism**: 각 iteration 후 training/validation metrics (scalar feedback)와 전체 context를 기반으로 verbal feedback 생성. 과적합 등 문제 식별 후 다음 iteration의 데이터 표현, 모델 아키텍처, hyperparameter 조정에 반영
- **평가**: Test set은 개발 과정에서 프로그래밍적으로 완전 추상화 (data leakage 방지). 최종 inference script만으로 test 성능 보고
- **데이터셋**: Genomic Benchmarks (enhancer/promoter detection 등 5개) + miRBench (microRNA binding site prediction 1개)
- **LLM backbone**: GPT-4.1 (gpt-4.1-2025-04-14)
- **비교 대상**: 8개 zero-shot LLM, Data Interpreter (6개 LLM backbone), AIDE

## Originality

- **도메인 특화 agentic ML**: 범용 Kaggle-style 벤치마크가 아닌 computational biology의 이질적 데이터에 특화된 최초의 체계적 agentic ML 시스템
- **Step-based workflow 설계**: 복잡한 prompt engineering 대신 ML 실험의 본질적 단계를 사전 정의하여 agent의 불필요한 planning을 회피하면서 각 단계 내에서는 자율성 부여
- **Programmatic output validation**: Pydantic 기반의 단계별 출력 검증으로, agent가 올바른 형식의 실행 가능한 코드를 생성할 때까지 강제 재시도 -- 기존 시스템의 낮은 success rate 문제를 구조적으로 해결
- **Test set의 프로그래밍적 추상화**: 기존 agentic 시스템에서 흔한 test data leakage 문제를 원천적으로 차단하는 엄격한 평가 프로토콜

## Limitation & Further Study

### 저자들이 언급한 한계

- Closed-source LLM의 학습 데이터 비공개로 인한 pre-training data leakage 가능성 불확실
- API 기반 closed-source 모델 사용으로 재현성 제한 (모델 교체/제거 위험)
- Genomics/transcriptomics의 nucleotide sequence classification에 한정 -- 구조 예측, 발현량 상관, imputation, clustering 등 미포함
- Prompt engineering과 hyperparameter 조정 과정에서 의도치 않은 overfitting 위험 (prototype 데이터셋 1개로 완화 시도)

### 자체판단 아쉬운 점

- 대부분 데이터셋에서 Human SOTA 대비 여전히 성능 격차 존재 (HEE: 0.885 vs. 0.933, NTP: 0.925 vs. 0.974) -- 실용적 활용까지 거리가 있음
- 5회 반복 실행이라는 적은 시행 횟수로 통계적 신뢰도 제한적
- Reflection feedback이 2/6 데이터셋에서만 통계적으로 유의하여, feedback mechanism의 실질적 기여도에 의문
- GPT-4.1 단일 backbone에 의존하여 LLM 선택의 영향을 충분히 분석하지 못함
- Preprint 단계로 peer review 미완료

### 후속 연구

- Proteomics, metabolomics 등 다른 -omics 데이터 유형으로 확장
- Classification 외 regression, clustering, structure prediction 등 다양한 ML task 지원
- Open-source LLM backbone 활용으로 재현성 및 비용 개선
- Reflection mechanism의 iteration 수 증가 및 정교화를 통한 성능 개선
- Multi-agent 협업 구조 도입 (데이터 전처리 agent, 모델 선택 agent 등 역할 분담)

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 3/5 |
| Technical Soundness | 3/5 |
| Significance | 3/5 |
| Clarity | 4/5 |
| Overall | 3/5 |

**총평**: Computational biology 데이터의 이질성에 대응하는 도메인 특화 agentic ML 시스템으로, 93%의 높은 success rate와 복잡 데이터셋(AGO2_CLASH)에서의 유일한 성공이 핵심 기여이다. 다만 Human SOTA 대비 성능 격차, 제한된 데이터셋/task 범위, preprint 상태를 고려하면 아직 초기 단계의 연구이며, 자율적 과학 발견 시스템으로의 발전 가능성을 보여주는 proof-of-concept 수준이다.
