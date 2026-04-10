---
title: "528_MedAgentGym_A_Scalable_Agentic_Training_Environment_for_Code"
authors:
  - "Ran Xu"
  - "Yuchen Zhuang"
  - "Yishan Zhong"
  - "Yue Yu"
  - "Zifeng Wang"
date: "2025.06"
doi: "미제공"
arxiv: ""
score: 4.25
essence: "본 논문은 생의학 데이터 과학(biomedical data science)에서 코드 기반 추론 능력을 강화하기 위한 확장 가능한 LLM 에이전트 훈련 환경인 MedAgentGym을 제시한다. 72,413개의 과제 인스턴스와 실행 가능한 샌드박스 환경을 통해 오픈소스 LLM들의 생의학 코딩 역량을 대폭 향상시킬 수 있음을 입증한다."
tags:
  - "cat/LLM-Based_Scientific_Reasoning"
  - "sub/Large_Language_Model_Agents"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Xu et al._2025_MedAgentGym A Scalable Agentic Training Environment for Code-Centric Reasoning in Biomedical Data S.pdf"
---

# MedAgentGym: A Scalable Agentic Training Environment for Code-Centric Reasoning in Biomedical Data Science

> **저자**: Ran Xu, Yuchen Zhuang, Yishan Zhong, Yue Yu, Zifeng Wang, Xiangru Tang, Hang Wu, May D. Wang, Peifeng Ruan, Donghan Yang, Tao Wang, Guanghua Xiao, Xin Liu, Carl Yang, Yang Xie, Wenqi Shi | **날짜**: 2025-06-04 | **DOI**: [미제공](https://arxiv.org/abs/2506.04405v2)

---

## Essence

![Figure 1](figures/fig1.webp) *Figure 1: (a) MedAgentGym의 과제별 성능과 (b) 전체 리더보드 평가. 상용 LLM과 오픈소스 LLM 간 상당한 성능 격차를 시각화함*

본 논문은 생의학 데이터 과학(biomedical data science)에서 코드 기반 추론 능력을 강화하기 위한 확장 가능한 LLM 에이전트 훈련 환경인 MedAgentGym을 제시한다. 72,413개의 과제 인스턴스와 실행 가능한 샌드박스 환경을 통해 오픈소스 LLM들의 생의학 코딩 역량을 대폭 향상시킬 수 있음을 입증한다.

## Motivation

- **Known**: 최근 LLM들은 의료 지식 추론과 일반적인 코드 생성에서 상당한 능력을 보여주고 있음. 기존 의료 벤치마크들(MedMCQA, MedQA 등)은 주로 지식 집약적 텍스트 기반 추론에 초점.

- **Gap**: 생의학 데이터 과학의 실제 워크플로우에 필요한 데이터 추출, 변환, 분석, 모델 개발의 전체 생명주기를 포괄하는 실행 가능한 환경과 종합적인 코드 기반 벤치마크가 부재. 특히 의료 기관의 개인정보 보호 요구사항과 비용 제약으로 인해 오픈소스 LLM의 수요가 높으나 성능 격차가 심함.

- **Why**: 생의학 연구자들은 데이터베이스 쿼리, 통계 분석, 게놈 수열 처리, 전자의료기록(EHR) 기반 예측 모델 구축 등 의료 도메인 지식과 프로그래밍 능력을 모두 필요로 함. 상용 LLM(gpt-4o)은 개인정보보호 및 비용 문제로 직접 배포 불가능하며, 오픈소스 LLM의 생의학 코딩 역량이 현저히 낮은 상황.

- **Approach**: 12개의 실제 생의학 시나리오에서 파생된 129개 범주의 72,413개 과제 인스턴스를 포함하는 종합적 벤치마크 환경 구축. 각 과제를 Docker 기반 실행 가능한 격리 환경에 캡슐화하고, 상세한 과제 명세, 대화형 피드백, 검증 가능한 정답 주석, 확장 가능한 훈련 궤적(trajectory) 생성을 지원함.

## Achievement

![Figure 1b](figures/fig1.webp) *Figure 1b: MedAgentGym의 전체 점수 리더보드. 오픈소스와 상용 LLM 간의 상당한 성능 격차 시각화*

1. **대규모 생의학 코딩 벤치마크 구축**: 12개 실제 데이터소스(MIMIC-III, eICU, TREQS 등)에서 파생된 72,413개의 과제 인스턴스를 정수화. 129개 범주에 걸쳐 데이터베이스 쿼리, 의료 계산, 생물정보학, 기계학습 모델링 등을 포함하는 포괄적 범위를 제공.

2. **29개 LLM 종합 벤치마킹**: 상용 LLM(gpt-4o, gpt-4.1 등)과 오픈소스 LLM(Qwen, Llama, DeepSeek 등) 간의 생의학 데이터 과학 능력에서 상당한 성능 격차를 정량화. 특히 생의학 소프트웨어 엔지니어링과 예측 모델링에서 차이가 가장 큼.

3. **효과적인 강화학습 기반 훈련**: Med-Copilot 에이전트가 오프라인 강화학습(offline RL)에서 +43.02%, 온라인 강화학습(online RL)에서 +45.28%의 성능 향상 달성. 최종적으로 Med-Copilot-14B가 분포 내(in-distribution)와 분포 외(out-of-distribution) 과제 모두에서 gpt-4o와 경쟁 가능한 성능 달성.

## How

![Figure 2](figures/fig2.webp) *Figure 2: MedAgentGym의 전체 구조. 종합적 코드 기반 생의학 추론 과제를 포함*

**데이터 구성 및 통합 벤치마크**:
- MIMIC-III(9개 범주, 10,440개 인스턴스), eICU(9개 범주, 6,824개), TREQS(4개 범주, 9,984개) 등 8개 주요 데이터소스와 MedAgentGym 내부 데이터(113개 범주, 40,142개) 통합
- 외부 검증을 위해 EHR-SeqSQL, EHRCon, MIMIC-Extract, N-PowerAI 데이터셋 포함 (총 16개 범주, 32,271개 인스턴스)
- 59.2K 훈련 세트, 13.2K 테스트 세트, 6.7K 훈련 궤적으로 구성

**실행 가능한 격리 환경**:
- 각 과제를 독립적인 Docker 컨테이너로 캡슐화하여 재현성과 보안 보장
- 사전 설치된 생의학 라이브러리(pandas, scikit-learn, BioPython 등) 포함
- 멀티스레드 병렬 실행 및 순차 샘플링 지원으로 효율적인 궤적 수집 가능

**대화형 피드백 메커니즘**:
- 에이전트의 코드 실행 결과에 대한 실시간 피드백 제공
- 성공 궤적(y^(i) = y*)과 실패 궤적(y^(i) ≠ y*, 에러 메시지 포함) 모두를 학습 신호로 활용
- 단일 턴(single-turn)과 다중 턴(multi-turn) 궤적 모두 지원

**강화학습 기반 훈련**:
- 오프라인 RL: 수집된 궤적으로부터 기존 모델의 성능 개선
- 온라인 RL: 환경과의 상호작용을 통한 실시간 에이전트 학습
- DPO(Direct Preference Optimization) 및 PPO(Proximal Policy Optimization) 같은 다양한 RL 알고리즘 지원

**성능 검증**:
- 코드 실행 결과 e: C × Y → {0,1}를 통한 객관적 정답 검증
- 과제별 메트릭(F1, accuracy 등)과 전체 성능 점수 계산

## Originality

- **최초의 대규모 실행 가능한 생의학 코딩 환경**: 기존 벤치마크(BioCoder, BioDSBench 등)는 평가만 가능하나, MedAgentGym은 실행 가능한 격리 환경, 대화형 피드백, 훈련 가능한 궤적 수집을 통합적으로 제공하는 최초의 플랫폼.

- **포괄적 범위**: 데이터 추출(EHR 쿼리), 수치 추론(의료 계산), 생물정보학(서열 처리), 기계학습 모델링까지 생의학 데이터 과학의 전체 생명주기를 단일 플랫폼에서 다룸.

- **실제 기반 설계**: 12개의 실제 생의학 시나리오에서 파생된 과제로, 임상 실무와 연구에서 실제로 마주치는 문제들을 반영.

- **대규모 벤치마킹 및 공개**: 29개 LLM에 대한 종합적 벤치마킹으로 현재 모델들의 생의학 코딩 역량 격차를 명확히 규명하고, 코드, 데이터, 훈련된 모델을 공개하여 재현성과 확장성 확보.

- **효과적인 훈련 방법론**: 오프라인/온라인 RL을 통한 체계적 성능 향상 전략과 오픈소스 모델의 상용 모델 수준 성능 달성 경로 제시.

## Limitation & Further Study

- **그라운드 트루스의 제약**: 일부 개방형 과제(EHRSHOT, MIMIC-Extract의 기계학습 모델링)의 경우 명시적 정답이 없어 훈련/테스트 데이터셋 분리 불가. 이는 RL 훈련의 신호 품질 제한.

- **의존성 관리의 복잡성**: 다양한 생의학 라이브러리(Biopython, R 패키지 등)의 버전 호환성 관리가 장기적 유지보수 관점에서 도전적. 새로운 라이브러리 추가 시 환경 재구성 필요.

- **도메인 특화성의 한계**: 과제들이 영문 기반이고 특정 의료 시스템(주로 미국)에 맞춰 있어, 다른 언어나 의료 시스템으로의 일반화 검토 필요.

- **평가 메트릭의 제한성**: 정답 검증이 이진 판정(정답/오답)에 집중되어, 부분 정답(partially correct) 상황에서의 미묘한 성능 차이 포착 어려움.

- **후속 연구 방향**:
  - 다국어 및 다중 의료 시스템 지원 확대
  - 멀티모달 데이터(의료 이미지, 음성 기록) 포함으로 범위 확장
  - 실시간 의료 환경에서의 에러 처리 및 안전성 검증 강화
  - 도메인 특화 에이전트와 일반 에이전트의 효과적 결합 방안 연구

## Evaluation

- **Novelty**: 4.5/5 — 실행 가능한 생의학 코딩 환경과 대규모 통합 벤치마크는 충분히 새롭고, 기존 작업들과의 명확한 차별성 있으나, 개별 기술(RL, trajectory sampling)은 기존 방법론의 조합.

- **Technical Soundness**: 4/5 — 데이터 수집 및 통합 방법론이 건실하며, RL 훈련 설계도 표준적이고 실행 가능함. 다만 일부 개방형 과제의 평가 메커니즘이 다소 약할 수 있음.

- **Significance**: 4.5/5 — 생의학 연구 커뮤니티에 실질적으로 유용한 인프라 제공하며, 오픈소스 LLM의 격차 규명과 해결 방안 제시로 높은 임상적/연구적 의의. 다만 아직까지의 성능 격차 완전 해소는 아직 미흡.

- **Clarity**: 4/5 — 전반적으로 명확하고 체계적으로 구성되었으며, 그림과 표가 효과적임. 다만 강화학습 세부 설정(하이퍼파라미터, 보상 함수 디자인)에 대한 설명이 주어진 본문에서는 제한적으로 보임.

- **Overall**: 4.25/5

**총평**: MedAgentGym은 생의학 데이터 과학 분야에서 코드 기반 추론을 위한 최초의 포괄적이고 실행 가능한 훈련 환경으로, 대규모 통합 벤치마크, 효과적인 RL 훈련 방법론, 그리고 공개된 리소스를 통해 오픈소스 LLM의 의료 도메인 적응에

## Related Papers

- 🔄 다른 접근: [[papers/546_Mlgym_A_new_framework_and_benchmark_for_advancing_ai_researc/review]] — 생의학 vs 머신러닝 도메인에서의 AI 에이전트 훈련 환경을 제시합니다.
- 🏛 기반 연구: [[papers/163_Biodsa-1k_Benchmarking_data_science_agents_for_biomedical_re/review]] — 생의학 데이터 과학 벤치마크가 에이전트 훈련 환경의 기반을 제공합니다.
- 🔗 후속 연구: [[papers/429_Infiagent-dabench_Evaluating_agents_on_data_analysis_tasks/review]] — 생의학 코딩 역량이 데이터 분석 작업 평가로 확장됩니다.
- 🔄 다른 접근: [[papers/546_Mlgym_A_new_framework_and_benchmark_for_advancing_ai_researc/review]] — 머신러닝 vs 생의학 도메인에서의 AI 에이전트 개발 환경을 제시합니다.
- 🧪 응용 사례: [[papers/606_Patientsim_A_persona-driven_simulator_for_realistic_doctor-p/review]] — 코딩 능력을 위한 확장 가능한 에이전트 훈련 환경 MedAgentGym은 환자 시뮬레이터의 의료 교육 활용을 구체화한다.
- 🧪 응용 사례: [[papers/645_Pubmedqa_A_dataset_for_biomedical_research_question_answerin/review]] — MedAgentGym의 확장 가능한 에이전트 훈련 환경이 PubMedQA 데이터셋을 활용하여 의료 코딩 작업에서의 실제적 성능 향상을 달성할 수 있는 구체적 방법을 제시함
