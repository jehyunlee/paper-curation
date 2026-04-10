---
title: "712_SciCode_A_Research_Coding_Benchmark_Curated_by_Scientists"
authors:
  - "Minyang Tian"
  - "Luyu Gao"
  - "Shizhuo Dylan Zhang"
  - "Xinan Chen"
  - "Cunwei Fan"
date: "2024.07"
doi: "10.48550/arXiv.2407.13168"
arxiv: ""
score: 4.5
essence: "과학자들이 직접 큐레이션한 과학 연구 문제 중심의 코딩 벤치마크를 제시하여, 언어 모델(LM)의 실제 과학 보조 능력을 평가할 수 있는 고품질 평가 도구를 개발하였다."
tags:
  - "cat/AI-Powered_Scientific_Research_Frameworks"
  - "sub/Scientific_Code_Generation"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Tian et al._2024_SciCode A Research Coding Benchmark Curated by Scientists.pdf"
---

# SciCode: A Research Coding Benchmark Curated by Scientists

> **저자**: Minyang Tian, Luyu Gao, Shizhuo Dylan Zhang, Xinan Chen, Cunwei Fan, Xuefei Guo, Roland Haas, Pan Ji, Kittithat Krongchon, Yao Li, Shengyan Liu, Di Luo, Yutao Ma, Hao Tong, Kha Trinh, Chenyu Tian, Zihan Wang, Bohao Wu, Yanyu Xiong, Shengzhu Yin, Minhui Zhu, Kilian Lieret, Yanxin Lu, Genglin Liu, Yufeng Du, Tianhua Tao, Ofir Press, Jamie Callan, Eliu Huerta, Hao Peng | **날짜**: 2024-07-18 | **DOI**: [10.48550/arXiv.2407.13168](https://doi.org/10.48550/arXiv.2407.13168)

---

## Essence

과학자들이 직접 큐레이션한 과학 연구 문제 중심의 코딩 벤치마크를 제시하여, 언어 모델(LM)의 실제 과학 보조 능력을 평가할 수 있는 고품질 평가 도구를 개발하였다.

## Motivation

- **Known**: 언어 모델이 다양한 도전적 과제에서 평균 인간 수준을 초과하여, 기존 벤치마크들이 빠르게 포화 상태에 도달하고 있음
- **Gap**: 모델의 실제 성능과 인식 간의 불일치, 그리고 과학 분야의 실제 연구 문제 해결 능력 평가의 부족
- **Why**: 합성 벤치마크들이 실제 응용 시나리오를 반영하는지 불명확하며, 과학 AI 개발의 상업적 인센티브 부족
- **Approach**: 16개 자연과학 분야(수학, 물리, 화학, 생물, 재료과학)의 과학자들과 협력하여 실제 연구 코딩 문제 중심의 벤치마크 구축

## Achievement

![Figure 1](figures/fig1.webp)
*Figure 1: SciCode 주요 문제가 여러 개의 더 작고 쉬운 부분 문제로 분해되는 구조*

1. **포괄적 벤치마크 구성**: 80개 주요 문제로부터 338개 부분 문제로 구성된 대규모 벤치마크 개발 (16개 과학 분야, 50개 개발 세트, 288개 테스트 세트)

2. **높은 난이도 수준**: 최고 성능 모델인 Claude3.5-Sonnet이 가장 현실적인 설정에서 4.6% 문제 해결, 배경 정보 제공 시에도 12.3%에 불과 (GPT-4o는 1.5%, Deepseek-Coder-v2는 3.1%)

3. **고품질 주석**: 각 문제마다 2명 이상의 박사급 이상 연구자가 검증·개정한 과학 배경 정보, 표준 솔루션, 테스트 케이스 제공

## How

![Figure 2](figures/fig2.webp)
*Figure 2: (a) 주요 문제 분포 및 (b) 부분 문제 분포 (물리 46%, 재료과학 16%, 수학 18%)*

- **문제 선택**: 수치 방법(numerical methods), 시스템 시뮬레이션(system simulation), 과학 계산(scientific calculation)에 초점
- **계층적 분해**: 복잡한 주요 문제를 작은 부분 문제로 분해하여 단계적 평가 가능하게 함
- **데이터 오염 방지**: 공개 데이터셋과 중복 제거 확인으로 데이터 신선도 보장
- **다양한 평가 설정**: 배경 정보 제공 여부, 이전 부분 문제 결과 조건화(conditioning) 등 옵션 제공
- **광범위 Python 라이브러리 활용**: NumPy, SciPy, PyTorch, TensorFlow, Qiskit 등 다양한 과학 계산 라이브러리 사용

## Originality

- **실제 연구 기반**: 과학자들의 실무 코드와 영향력 있는 논문에서 추출하여 현실성 극대화
- **과학자 큐레이션**: 다양한 분야의 과학자들이 직접 참여한 유일한 벤치마크
- **계층적 구조화**: 주요-부분 문제 분해 구조로 단계별 문제 해결 능력 평가
- **접근성 제한 데이터**: 일반적으로 LM 훈련에 포함되지 않은 내부용 과학 코드 활용
- **종합적 평가 환경**: 단순 코드 생성 능력 이상으로 지식 회상, 추론, 통합 능력을 종합적으로 평가

## Limitation & Further Study

- **모델 성능의 극저조**: 모든 모델이 낮은 성능을 보여 벤치마크 난이도 적절성에 대한 추가 검토 필요
- **오픈소스 모델의 한계**: 대부분 오픈소스 모델이 주요 문제 해결에 완전히 실패하여 모델 개선의 명확한 방향 제시 필요
- **평가 메트릭의 단순성**: 현재 pass@1 기반 평가로 부분적 해결이나 부분점수(partial credit) 반영 부족
- **후속 연구**: (1) 과학 AI 모델 개발을 위한 성능-개선 최적화 연구, (2) 모델-과학자 협업 도구 개발, (3) 추가 과학 분야 확장

## Evaluation

- **Novelty**: 5/5 (과학자 큐레이션과 현실성 중심의 완전히 새로운 접근)
- **Technical Soundness**: 4/5 (견고한 설계와 고품질 주석이나, 평가 메트릭에 제한)
- **Significance**: 5/5 (과학 AI 발전의 중요한 기준점 제시, 상업적 인센티브 부족 분야에 기여)
- **Clarity**: 4/5 (명확한 설명과 구조이나, 일부 상세 평가 방법론 보강 필요)
- **Overall**: 4.5/5

**총평**: 본 논문은 과학 분야 코딩 능력 평가에 대한 중요한 공백을 채우면서, 과학자들의 직접 참여로 벤치마크의 현실성과 신뢰성을 확보한 우수한 자원 논문이다. 현존 최고 성능 모델들도 4.6%의 저조한 성능을 보여주며 향후 과학 AI 개발의 명확한 목표와 평가 기준을 제시한다.

## Related Papers

- 🔗 후속 연구: [[papers/320_Evaluating_Large_Language_Models_in_Scientific_Discovery/review]] — 일반적인 프로그래밍 함수 생성 평가를 과학자들이 직접 설계한 실제 과학 연구 문제 해결 능력 평가로 발전시켰다
- 🏛 기반 연구: [[papers/170_Blade_Benchmarking_language_model_agents_for_data-driven_sci/review]] — 과학 연구 문제 중심의 코딩 벤치마크가 언어모델 에이전트의 데이터 기반 과학 발견 능력 평가에 중요한 기준을 제시한다
- 🔄 다른 접근: [[papers/671_Researchcodebench_Benchmarking_llms_on_implementing_novel_ma/review]] — 과학자 큐레이션 코딩 벤치마크와 기계학습 연구 코드 벤치마킹이 각각 과학 연구와 ML 연구 맥락에서 코드 생성 능력을 평가한다
- 🔗 후속 연구: [[papers/548_Mlr-bench_Evaluating_ai_agents_on_open-ended_machine_learnin/review]] — 과학 연구 중심 코딩 벤치마크가 개방형 기계학습 연구 평가로 확장되어 더 포괄적인 AI 연구 능력을 측정한다
- 🏛 기반 연구: [[papers/170_Blade_Benchmarking_language_model_agents_for_data-driven_sci/review]] — 과학 연구 문제 중심의 코딩 능력 평가가 데이터 기반 과학 발견을 위한 언어모델 에이전트 성능 측정의 중요한 기반이 된다
- 🔗 후속 연구: [[papers/320_Evaluating_Large_Language_Models_in_Scientific_Discovery/review]] — 일반적인 코드 생성 평가가 과학자들이 직접 큐레이션한 과학 연구 문제 중심의 코딩 벤치마크로 구체화되었다
- 🧪 응용 사례: [[papers/770_Starcoder_2_and_the_stack_v2_The_next_generation/review]] — 다양한 프로그래밍 언어를 지원하는 코드 생성 모델이 과학자들의 실제 연구 문제 해결 능력 평가에 핵심적인 도구로 활용된다
