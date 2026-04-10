---
title: "146_Autosdt_Scaling_data-driven_discovery_tasks_toward_open_co-s"
authors:
  - "Li"
  - "Yifei*"
  - "Moussa"
  - "Hanane Nour*"
  - "Chen"
date: "2025"
doi: "arXiv:2506.08140"
arxiv: ""
score: 4.5
essence: "LLM의 코딩 능력을 활용하여 자동으로 고품질 데이터 주도형 발견(data-driven discovery) 태스크 5,404개를 수집한 AutoSDT 파이프라인을 제시하고, 이를 통해 구축한 데이터셋으로 미세조정한 모델이 기존 오픈 가중치 모델 대비 대폭 성능 향상을 달성했다."
tags:
  - "cat/Scientific_Language_Processing_and_Visualization"
  - "sub/LLM_Agent_Benchmarking"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/2025 et al._2025_Autosdt Scaling data-driven discovery tasks toward open co-scientists.pdf"
---

# AutoSDT: Scaling Data-Driven Discovery Tasks Toward Open Co-Scientists

> **저자**: Li, Yifei*, Moussa, Hanane Nour*, Chen, Ziru, Chen, Shijie, Yu, Botao et al. (The Ohio State University, Cisco Research, University of Wisconsin–Madison) | **날짜**: 2025 | **DOI**: [arXiv:2506.08140](https://arxiv.org/abs/2506.08140)

---

## Essence

![Figure 1](https://img-placeholder.png) *AutoSDT-Coder-32B가 ScienceAgentBench에서 GPT-4o와 동등한 성능(7.8% SR) 달성*

LLM의 코딩 능력을 활용하여 자동으로 고품질 데이터 주도형 발견(data-driven discovery) 태스크 5,404개를 수집한 AutoSDT 파이프라인을 제시하고, 이를 통해 구축한 데이터셋으로 미세조정한 모델이 기존 오픈 가중치 모델 대비 대폭 성능 향상을 달성했다.

## Motivation

- **Known**: 최근 LLM 기반 AI 공동 과학자(AI co-scientist) 구축이 주목받고 있으며, 특히 투명성과 데이터 프라이버시가 중요한 분야에서 오픈 가중치 LLM의 필요성이 높다.

- **Gap**: 데이터 주도형 발견 태스크에 대한 대규모 고품질 학습 데이터의 심각한 부족 — 기존 수동 주석(annotation)은 태스크당 2.5-3시간 소요되어 수백 개 규모의 데이터셋만 구축 가능

- **Why**: 소프트웨어 엔지니어링 태스크와 달리, 데이터 주도형 발견 태스크는 실제 과학 데이터셋에 대해 작동하는 완전한 파일 수준 코드가 필요하므로 코드 저장소에서 직접 추출 불가능

- **Approach**: LLM의 매개변수 지식(parametric knowledge)과 코딩 능력을 활용하여 (1) 쿼리 증강으로 소스 다양성 확보, (2) 생태학적 타당성(ecological validity) 검증, (3) 다중 반복 적응(adaptation)과 검증을 통한 코드 품질 보장

## Achievement

![Figure 2](https://img-placeholder.png) *AutoSDT 파이프라인: Search→Select→Adapt 3단계 구성*

1. **AutoSDT-5K 데이터셋 구축**: 5,404개의 데이터 주도형 발견 태스크 자동 수집, 4개 학문 분야(생물정보학, 전산화학, 지리정보과학, 심리학/인지신경과학)와 756개의 고유 Python 패키지 포함, 태스크당 평균 $0.55 비용

2. **높은 품질 검증**: 도메인 전문가 9명(박사과정생 및 교수)이 256개 태스크 평가 결과 — 93%의 과학적 진정성(ecological validity) 확인, 92.2%의 생성 코드 정확성 달성

3. **현저한 성능 향상**: 
   - ScienceAgentBench: AutoSDT-Coder-32B가 GPT-4o(2024-05-13)와 동등한 7.8% SR 달성 (기본 모델 3.9% 대비 2배)
   - DiscoveryBench: 가설 매칭 점수 6.9→8.1로 17.4% 상대 개선, GPT-4o와의 격차 축소

## How

![Figure 3](https://img-placeholder.png) *AutoSDT-5K의 다단계 태스크 분포 및 학문 분야별 구성*

**AutoSDT-Search (소스 탐색)**
- 사용자 제공 초기 키워드(예: "bioinformatics")를 LLM 기반 쿼리 증강으로 확장
- GitHub와 PapersWithCode API를 이용한 저장소 검색
- README.md 기반 LLM 판단으로 연구 관련 저장소 필터링
- 키워드 "neuroscience" 사례: 단독 사용 시 332개 → 확장 후 693개 저장소 발견

**AutoSDT-Select (프로그램 선택)**
- Python 파일 자동 추출 및 규칙 기반 필터링(1,000줄 초과 제외, 'config'/'tests' 디렉토리 제외)
- LLM을 활용한 데이터 주도형 과학 코드 판정: (1) 과학 워크플로우 관련성, (2) 데이터셋 입력 사용 여부, (3) 수치 결과/처리 데이터/시각화 출력 생성 확인
- 의존성 자동 추출 및 작업공간 준비: 평균 264.98MB→40.42MB 크기 감축

**AutoSDT-Adapt (프로그램 적응 및 지시문 생성)**
- 3단계 프로그램 적응: (1) Claude-3.5-Sonnet을 통한 초기 적응(import/IO/경로 수정), (2) pipreqs로 의존성 추출 및 conda 환경 구성, (3) 최대 3회 반복 자동 디버깅
- 실행 오류 지속 시 폐기
- 역번역(back-translation)을 통한 자동 지시문 생성: 적응된 프로그램→명확한 태스크 설명

## Originality

- **자동화 규모의 획기성**: 수동 주석의 2.5-3시간/태스크 대비 자동 파이프라인으로 5,404개 태스크 대규모 구축 (기존 수백 개 규모 벗어남)

- **생태학적 타당성 중시**: 단순 코드 품질을 넘어 실제 과학 워크플로우에서의 진정성(93% 전문가 검증) 명시적 평가

- **다학제 범위**: 4개 학문 분야 × 756개 패키지로 단일 분야 중심의 기존 데이터셋 대비 광범위한 과학 도구 생태계 포괄

- **오픈 가중치 LLM 성과**: 기존 오픈 가중치 모델의 데이터 주도형 발견 능력 대폭 향상, GPT-4o 수준 성능 달성으로 투명성/프라이버시 중시 분야 활용 가능성 확장

## Limitation & Further Study

- **소스 다양성 한계**: GitHub/PapersWithCode만 활용 — 학술 저널 부록 코드, 산업용 코드 미포함 가능성

- **도메인 제한성**: 4개 학문 분야만 커버 — 물리학, 천문학, 경제학 등 광범위한 과학 분야 확장 필요

- **의존성 복잡성**: 대규모 외부 데이터셋이나 고도의 컴퓨팅 자원 필요 태스크 자동 처리 미흡

- **평가 범위**: 전문가 검증이 256개 태스크(약 4.7%)로 제한 — 전체 데이터셋에 대한 확률적 오류율 추정 필요

- **후속 연구**: (1) 추가 학문 분야 포함, (2) 멀티모달 과학 태스크(이미지/3D 데이터 포함) 확장, (3) 더 큰 오픈 가중치 모델(70B, 405B) 미세조정 실험, (4) 적응형 피드백 루프로 동적 품질 개선


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4.5/5
- Significance: 5/5
- Clarity: 4/5
- Overall: 4.5/5

**총평**: AutoSDT는 LLM 자동화로 고품질 과학 태스크 데이터의 수집 병목을 혁신적으로 해결하고, 구축한 데이터셋으로 오픈 가중치 모델이 폐쇄형 모델 수준 성능 도달을 실증함으로써 개방적 AI 과학자 시대의 물적 토대를 마련한 의미 있는 연구이다.

## Related Papers

- 🧪 응용 사례: [[papers/545_Mle-bench_Evaluating_machine_learning_agents_on_machine_lear/review]] — AutoSDT로 생성된 고품질 데이터셋이 MLE-bench와 같은 에이전트 평가에 활용될 수 있음
- 🔄 다른 접근: [[papers/259_DeepAnalyze_Agentic_Large_Language_Models_for_Autonomous_Dat/review]] — 둘 다 자동화된 데이터 과학을 다루지만 AutoSDT는 태스크 생성에, DeepAnalyze는 분석 실행에 특화
- 🔗 후속 연구: [[papers/277_Discoverybench_Towards_data-driven_discovery_with_large_lang/review]] — AutoSDT의 데이터 주도형 발견 방법론이 DiscoveryBench의 과학적 발견 평가에 적용될 수 있음
- 🏛 기반 연구: [[papers/293_Ds-agent_Automated_data_science_by_empowering_large_language/review]] — AutoSDT가 제공하는 데이터 발견 태스크가 DS-Agent 같은 데이터 사이언스 에이전트 학습의 기반이 됨
- 🏛 기반 연구: [[papers/545_Mle-bench_Evaluating_machine_learning_agents_on_machine_lear/review]] — AutoSDT의 데이터 주도형 발견 태스크가 ML 에이전트 평가의 기초 데이터를 제공함
- 🔄 다른 접근: [[papers/259_DeepAnalyze_Agentic_Large_Language_Models_for_Autonomous_Dat/review]] — AutoSDT가 태스크 생성에 집중하는 반면 DeepAnalyze는 실제 분석 실행을 자동화
