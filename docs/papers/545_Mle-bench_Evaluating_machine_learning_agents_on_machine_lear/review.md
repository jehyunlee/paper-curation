---
title: "545_Mle-bench_Evaluating_machine_learning_agents_on_machine_lear"
authors:
  - "Jun Shern Chan"
  - "Neil Chowdhury"
  - "Oliver Jaffe"
  - "James Aung"
  - "Dane Sherburn"
date: "2024"
doi: ""
arxiv: ""
score: 4.6
essence: "본 논문은 AI 에이전트의 머신러닝 엔지니어링(MLE) 능력을 평가하기 위해 Kaggle의 75개 경쟁 문제로 구성된 벤치마크 MLE-bench를 소개한다. 최고 성능 모델(o1-preview with AIDE 스캐폴딩)이 16.9%의 경쟁에서 Kaggle 동메달 이상 수준을 달성했으며, 자원 스케일링과 사전학습 데이터 오염의 영향을 광범위하게 분석했다."
tags:
  - "cat/Scientific_Language_Processing_and_Visualization"
  - "sub/LLM_Agent_Benchmarking"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Chan et al._2024_Mle-bench Evaluating machine learning agents on machine learning engineering.pdf"
---

# MLE-bench: Evaluating machine learning agents on machine learning engineering

> **저자**: Jun Shern Chan, Neil Chowdhury, Oliver Jaffe, James Aung, Dane Sherburn, Evan Mays, Giulio Starace, Kevin Liu, Leon Maksin, Tejal Patwardhan, Lilian Weng, Aleksander Mądry | **날짜**: 2024 | **출판**: ICLR 2025

---

## Essence

![Figure 1](https://arxiv.org/html/2410.07095v6/figures/1.webp)
*MLE-bench: AI 에이전트를 위한 오프라인 Kaggle 경쟁 환경. 각 경쟁은 설명, 데이터셋, 등급 코드 및 리더보드로 구성됨*

본 논문은 AI 에이전트의 머신러닝 엔지니어링(MLE) 능력을 평가하기 위해 Kaggle의 75개 경쟁 문제로 구성된 벤치마크 MLE-bench를 소개한다. 최고 성능 모델(o1-preview with AIDE 스캐폴딩)이 16.9%의 경쟁에서 Kaggle 동메달 이상 수준을 달성했으며, 자원 스케일링과 사전학습 데이터 오염의 영향을 광범위하게 분석했다.

## Motivation

- **Known**: 언어모델(LMs)은 코딩 벤치마크와 다양한 ML 작업(아키텍처 설계, 모델 학습 등)에서 인상적인 성능을 보였으나, 에이전트 스캐폴딩의 발전에도 불구하고 자율적 end-to-end ML 엔지니어링을 종합적으로 측정하는 벤치마크가 부족함

- **Gap**: 현존하는 코딩/ML 벤치마크들은 개별 작업(코드 생성, 특정 모델 학습)에 초점을 맞추고 있으며, 실제 ML 엔지니어링에서 필요한 통합적 문제 해결 능력 평가의 공백이 존재

- **Why**: AI 에이전트의 자율적 ML 능력 평가는 과학적 진전 가속화 가능성을 측정하면서도 안전하고 통제된 배포를 위해 모델 진전을 신중히 이해해야 함

- **Approach**: Kaggle의 실제 경쟁 문제 75개를 수작업으로 선별하여 현실적이고 도전적인 ML 엔지니어링 작업을 반영하는 벤치마크 구성하고, 인간 기준선(리더보드)과의 비교 가능성 확보

## Achievement

![Figure 2](https://arxiv.org/html/2410.07095v6/figures/2.webp)
*3개의 상이한 에이전트 프레임워크(MLAB, OpenHands, AIDE)에서 실제 경쟁 시도의 궤적. 실제 R&D와 같이 시행착오를 통한 반복적 해결 필요*

1. **종합적 벤치마크 구축**: 5,673개 Kaggle 경쟁에서 기준에 맞게 75개 경쟁을 선별(저 복잡도 30%, 중 복잡도 50%, 고 복잡도 20%)하고, 각 경쟁에 대해 설명, 데이터셋, 등급 코드, 리더보드 스냅샷 제공

2. **에이전트 성능 평가 결과**:
   - o1-preview + AIDE: pass@1에서 16.9% 동메달 달성률
   - pass@8 시도 시 34.1%로 성능 2배 향상
   - GPT-4o: 24시간에 8.7%, 100시간에 11.8%
   - 에이전트는 표준 접근법으로 해결 가능한 경쟁에서는 우수하나, 디버깅과 오류 복구에 어려움

3. **자원 스케일링 분석**: 런타임, 하드웨어 자원, pass@k 시도 횟수 증가에 따른 성능 천장 분석으로 현재 에이전트의 한계 명확화

4. **데이터 오염 및 부정행위 탐지**: 사전학습 데이터 오염과 성능 간의 관계 분석 및 표절 탐지(Dolos), 규칙 위반 탐지(GPT-4o 기반) 도구 제공

## How

![Figure 3](https://arxiv.org/html/2410.07095v6/figures/3.webp)
*허용된 시도 횟수 증가에 따른 메달 달성 비율 상승. Pass@1에서 Pass@8 또는 Pass@24로 증가 시 성능 개선 명확*

### 데이터셋 구성
- **선별 과정**: Meta Kaggle 데이터셋의 5,673개 경쟁에서 586개 Community가 아닌 경쟁을 선정 → 관련성 기준으로 수작업 스크리닝 → 등급 절차 복제 가능성, 합리적 train-test 분할 가능 여부 확인
- **복잡도 주석**: 각 경쟁을 저/중/고 복잡도로 분류(모델 학습 시간 제외 2시간/2-10시간/10시간 이상 기준)
- **문제 유형 주석**: 텍스트 분류, 이미지 분할 등의 문제 유형 명시

### Train-Test 분할
- 원본 데이터셋이 공개된 경우 사용
- 테스트셋 미공개 시 공개 학습 데이터를 기반으로 새로운 분할 구성(표본 제출 점수 유사성 확인)
- 일반적으로 원본 학습셋의 10%를 테스트셋으로 설정

### 평가 지표
- **메달 기준**: Kaggle의 메달 기준(참가팀 규모별 상이한 상위 % 적용) 직접 도입
- **기본 지표**: 임의의 메달(동메달 이상) 달성 시도의 백분율
- **원점수**: 경쟁별 상세 성능 추적용 원점수 보고

### 규칙 및 부정행위 방지
- **제출 규칙**: 에이전트는 별도 모델 통해서만 예측 생성(사전학습 지식 직접 기록 금지), 온라인 솔루션 열람 금지
- **규칙 위반 탐지**: GPT-4o를 이용한 자동 로그 검사(수동 파일 작성, 외부 API 호출, 미인가 자원 접근 탐지)
- **표절 탐지**: Dolos 도구로 제출된 코드를 상위 50개 Kaggle 노트북과 비교(60% 이상 유사도 시 부적격)

### 에이전트 평가 설정
- **제출 검증**: 로컬 검증 서버를 통한 제출 유효성 확인(점수 제공 안 함)
- **런타임**: 최대 24시간 자율 실행
- **스캐폴딩**: MLAB, OpenHands(범용), AIDE(Kaggle 특화) 등 다양한 오픈소스 프레임워크 평가

## Originality

- **실제 경쟁 문제 기반 벤치마크**: Kaggle의 실제 경쟁 75개(총 상금 $1,948,016)를 체계적으로 선별하여 현실성과 도전성을 동시에 확보한 첫 종합 벤치마크
  
- **인간 기준선 통합**: Private 리더보드 스냅샷을 통해 에이전트 성능을 동메달 달성률로 정량화하여, 실제 Kaggler와의 직접 비교 가능하게 함

- **광범위한 자원 스케일링 분석**: Pass@k, 런타임, 하드웨어 자원 변수에 따른 체계적 분석으로 현재 에이전트의 성능 천장 파악

- **부정행위 탐지 메커니즘**: GPT-4o 기반 규칙 위반 탐지와 Dolos 기반 표절 탐지 도구로 벤치마크의 신뢰성 확보

- **개발자 친화적 설계**: 모든 경쟁 메타데이터, 등급 코드, 로컬 검증 환경을 오픈소스로 공개하여 향후 연구 용이성 극대화

## Limitation & Further Study

- **인간-에이전트 성능 격차**: 현재 최고 성능 에이전트(16.9%)와 Kaggle 금메달리스트 수준 사이의 큰 격차가 남아있으며, 이는 제너럴한 ML 엔지니어링 자율화의 한계를 시사

- **데이터 오염의 불명확한 영향**: 사전학습 데이터와의 오염 정도와 성능 간에 명확한 양의 상관관계가 관찰되지 않아, 원인 분석을 위한 추가 조사 필요

- **스캐폴딩 의존성**: AIDE와 같은 Kaggle 특화 스캐폴딩이 성능에 큰 영향을 미치므로, 스캐폴딩 개선 여지와 일반화 가능성에 대한 더 깊은 이해 필요

- **디버깅과 오류 복구의 약점**: 에이전트들이 시행착오 과정에서 오류로부터의 회복에 어려움을 보이는 점을 극복하는 방법론 개발 필요

- **테스트셋 분할의 근사성**: 미공개 테스트셋의 경우 새로운 분할을 구성했으나, 원본 분포와의 완전한 일치를 보장할 수 없으므로 성능 비교에 미세한 편향 가능성

- **향후 연구 방향**:
  - 에이전트의 디버깅 능력 향상 메커니즘 개발
  - 더 복잡한 고 난이도 경쟁에 대한 에이전트 성능 향상 전략
  - 다중 모달 및 구조화되지 않은 데이터를 포함한 경쟁 확대
  - 실시간 Kaggle 경쟁에서의 에이전트 성능 검증

## Evaluation

- **Novelty**: 4.5/5
  - 실제 Kaggle 경쟁 기반의 첫 종합 ML 엔지니어링 벤치마크로 높은 현실성
  - 인간 기준선 통합과 메달 시스템 도입이 독창적
  - 다만 개별 작업 평가 벤치마크는 이미 존재함

- **Technical Soundness**: 4.5/5
  - 체계적인 데이터셋 선별 절차(5,673 → 75개)와 명확한 기준 제시
  - 규칙 위반 및 표절 탐지 메커니즘이 견고함
  - Train-test 분할 재구성 시 원본 분포 완전 일치의 한계 존재

- **Significance**: 4.8/5
  - AI 에이전트의 자율 ML 능력 평가에 대한 업계의 중요한 수요 충족
  - OpenAI, Anthropic, Google DeepMind 등의 안전성 평가 프레임워크에서 직접 활용 가능
  - 오픈소스 공개로 후속 연구 기반 제공

- **Clarity**: 4.6/5
  - 벤치마크 구성, 평가 지표, 규칙이 명확하고 체계적으로 설명됨
  - 실제 에이전트 궤적 예시로 직관적 이해 용이
  - 일부 기술적 세부사항(테스트셋 분할 예외 처리)은 부록으로 축약됨

- **Overall**: 4.6/5

**총평**: 본 논문은 실제 Kaggle 경쟁 75개를 정교하게 선별하여 AI 에이전트의 현실적 ML 엔지니어링 능력을 평가하는 첫 종합 벤치마크를 제시했으며, 광범위한 실험과 부정행위 방지 메커니즘으로 벤치마크의 신뢰성과 재현성을 확보했다. 다만 현재 에이전트와 최고 수준 Kaggler 간의 큰 성능 격차, 그리고 디버깅과 오류 복구 능력의 한계는 자율적 ML 엔지니어링의 실현화를

## Related Papers

- 🔄 다른 접근: [[papers/671_Researchcodebench_Benchmarking_llms_on_implementing_novel_ma/review]] — MLE-bench가 Kaggle 기반인 반면 ResearchCodeBench는 최신 ML 연구 논문 구현에 특화됨
- 🏛 기반 연구: [[papers/146_Autosdt_Scaling_data-driven_discovery_tasks_toward_open_co-s/review]] — AutoSDT의 데이터 주도형 발견 태스크가 ML 에이전트 평가의 기초 데이터를 제공함
- 🔄 다른 접근: [[papers/542_Mlagentbench_Evaluating_language_agents_on_machine_learning/review]] — 둘 다 ML 에이전트를 평가하지만 MLAgentBench는 더 일반적인 ML 작업에 초점
- 🔗 후속 연구: [[papers/294_Dsbench_How_far_are_data_science_agents_to_becoming_data_sci/review]] — MLE-bench의 평가 방식을 데이터 사이언스 전반으로 확장한 벤치마크
- 🧪 응용 사례: [[papers/146_Autosdt_Scaling_data-driven_discovery_tasks_toward_open_co-s/review]] — AutoSDT로 생성된 고품질 데이터셋이 MLE-bench와 같은 에이전트 평가에 활용될 수 있음
- 🔄 다른 접근: [[papers/671_Researchcodebench_Benchmarking_llms_on_implementing_novel_ma/review]] — MLE-bench가 Kaggle 문제인 반면 ResearchCodeBench는 최신 연구 논문의 새로운 아이디어 구현에 집중
- 🔄 다른 접근: [[papers/548_Mlr-bench_Evaluating_ai_agents_on_open-ended_machine_learnin/review]] — 둘 다 머신러닝 연구 수행 능력을 평가하는 벤치마크이지만 하나는 오픈엔디드 연구에, 다른 하나는 특정 머신러닝 에이전트에 초점을 맞춘다.
