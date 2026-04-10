---
title: "180_Can_foundation_models_actively_gather_information_in_interac"
authors:
  - "Danny P. Sawyer"
  - "Nan Rosemary Ke"
  - "Hubert Soyer"
  - "Martin Engelcke"
  - "David Reichert"
date: "2024"
doi: "---"
arxiv: ""
score: 4.0
essence: "본 연구는 파운데이션 모델(Foundation Models)의 대화형 환경에서의 능동적 탐색(active exploration) 능력을 체계적으로 평가한다. Feature World와 Alchemy 환경을 통해 효율적 정보 수집, 메타러닝(meta-learning), 전략 적응(strategy adaptation)의 세 가지 핵심 능력을 측정하며, 특히 요약(summarization) 프롬프팅이 복잡한 다중 시행 환경에서 메타러닝을 가능하게 함을 발견했다."
tags:
  - "cat/Scientific_Language_Processing_and_Visualization"
  - "sub/LLM_Agent_Benchmarking"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Sawyer et al._2024_Can foundation models actively gather information in interactive environments to test hypotheses ar.pdf"
---

# Can foundation models actively gather information in interactive environments to test hypotheses? arXiv preprint arXiv:2412.06438, 2024.

> **저자**: Danny P. Sawyer, Nan Rosemary Ke, Hubert Soyer, Martin Engelcke, David Reichert, Drew A. Hudson, John Reid, Alexander Lerchner, Danilo Jimenez Rezende, Timothy Lillicrap, Michael C. Mozer, Jane X. Wang | **날짜**: 2024 | **DOI**: 

---

## Essence

본 연구는 파운데이션 모델(Foundation Models)의 대화형 환경에서의 능동적 탐색(active exploration) 능력을 체계적으로 평가한다. Feature World와 Alchemy 환경을 통해 효율적 정보 수집, 메타러닝(meta-learning), 전략 적응(strategy adaptation)의 세 가지 핵심 능력을 측정하며, 특히 요약(summarization) 프롬프팅이 복잡한 다중 시행 환경에서 메타러닝을 가능하게 함을 발견했다.

## Motivation

- **Known**: 파운데이션 모델은 정적 단일 턴(single-turn) 추론 작업에서 탁월한 성능을 보임
- **Gap**: 과학 연구부터 기술 개발까지 현실의 많은 문제들은 동적 대화형 환경에서의 다중 턴 탐색(multi-turn exploration)과 가설 검증을 요구하는데, 파운데이션 모델의 이러한 능력은 거의 탐구되지 않음
- **Why**: 인간이 생성한 데이터에 대한 학습이 한계에 도달하면서 "경험의 시대"로 진입하고 있으며, 모델이 환경과의 상호작용을 통해 스스로 학습 데이터를 생성해야 함. 파운데이션 모델이 이러한 능력을 보유하고 있는지가 중요한 미해결 문제
- **Approach**: 세 가지 환경(텍스트 기반 Feature World, 멀티모달 Feature World, 텍스트 기반 Alchemy)에서 여러 파운데이션 모델(Gemini 1.5/2.5, Claude 3.7, ChatGPT-4o/o4-mini)을 제로샷(zero-shot) 인-컨텍스트 프롬팅으로 평가

## Achievement

![Figure 1: Feature World 작업 구조 및 실험 설정 - (a) 텍스트 기반 작업 예시](figures/fig1.webp)
*텍스트 기반 Feature World의 단순한 상태 비의존 보상 함수 학습 환경*

![Figure 2: Feature World에서 보상 대상을 발견한 에피소드의 비율 비교](figures/fig2.webp)
*모델별 정보 수집 효율성: 최적 정책과의 근접성*

1. **정보 수집 능력 (Information Gathering)**: 모든 평가 대상 LLM이 간단한 보상 함수를 가진 Feature World 작업에서 최적(near-optimal) 성능에 근접. 특히 고정 스텝 예산 내에서 보상 대상을 찾는 성공률이 높음

2. **메타러닝의 조건부 성공**: 기본 Alchemy 환경에서는 메타러닝 실패(시행 간 성능 개선 없음)를 보였으나, **요약 프롬팅(summarization prompting)** 을 도입하면 시행을 거듭하면서 성능이 유의미하게 향상됨

![Figure 4: Alchemy 작업 구조 및 실험 설정 - 잠재적 인과 구조 추론 환경](figures/fig4.webp)
*다중 상태 의존 시행을 요구하는 메타러닝 벤치마크*

![Figure 5: 다양한 모델과 조건 간 Alchemy 에피소드 점수 비교](figures/fig5.webp)
*요약 여부에 따른 성능 차이: Gemini 2.5 우수, ChatGPT 낮음*

3. **모델 간 강한 이질성**: Alchemy 환경에서 명확한 성능 격차 - Gemini 2.5 > Claude 3.7 >> ChatGPT-4o/o4-mini. 이는 Alchemy이 파운데이션 모델의 탐색 능력 벤치마크로서의 가치를 입증

4. **전략 적응과 재학습**: 일부 모델(특히 Gemini 2.5)에서 환경 규칙이 예기치 않게 변경될 때 요약을 통해 새로운 세계 모델(world model)의 적응적 재학습 가능

## How

![Figure 3: 3D 탐색 작업의 개략도 및 성능 지표 (15 에피소드/조건)](figures/fig3.webp)
*멀티모달 Feature World에서의 시각적 피드백과 성능 한계*

- **Feature World 설계**: 정적이고 상태 비의존적인 숨겨진 보상 함수에 대한 정보 수집만 측정하는 최소 환경. 단순화를 통해 즉각적 정보 수집 효율성을 독립적으로 분석

- **Alchemy 구현**: 원본 Alchemy(Wang et al., 2021) 벤치마크의 텍스트 기반 커스텀 버전 개발. 에이전트가 다중 상태 의존 시행을 통해 잠재적 인과 구조를 추론해야 함

- **메타러닝 측정 방식**: 동일 에피소드 내 연속 시행에서의 성능 개선도를 정량화. 무작위 정책 대비 우월성 평가

- **프롬팅 전략 체계적 변이**: 
  - 기본 프롬팅 (베이스라인)
  - 정기적 요약 프롬팅 (시행 완료 후 관찰 내용 요약)
  - 사전 정보량 및 시연(demonstration) 구조 변이

- **시각적 피드백 처리**: 3D Feature World에서 VLM의 비전 처리 능력 평가 및 한계점 검증

## Originality

- **첫 번째의 체계적 기초 모델 탐색 능력 평가**: 효율적 정보 수집, 메타러닝, 전략 적응을 명확히 분리하여 정의하고 정량 측정. 기존 연구는 종합적 과제 성능에만 초점

- **제어된 최소 환경 설계**: 기존 RL 벤치마크의 스파스 보상, 기만적 보상, 노이즈 등 혼재 요인을 제거하고 탐색의 기계적 특성에만 집중

- **요약을 통한 메타러닝 출현 현상**: LLM이 내생적(intrinsic) 메타러닝 메커니즘을 갖지 않으나, 간단한 프롬팅 개입으로 학습-학습(learning-to-learn) 능력이 창발한다는 발견은 기술적으로 중요

- **다중 파운데이션 모델 비교**: Gemini, Claude, ChatGPT의 세 계열 모델을 체계적으로 비교하여 건축적 차이의 영향 분석

- **전략 적응의 첫 LLM 연구**: 동적 환경에서의 전략 재학습 능력을 처음으로 LLM에서 체계적으로 측정

## Limitation & Further Study

- **시각적 신호 처리 한계**: 3D Feature World에서 VLM의 비전 처리 오류가 성능을 제한. 멀티모달 모델의 시각 이해 개선이 필요

- **확장성 미검증**: 현재 환경들이 상대적으로 단순하며, 더 복잡한 대규모 상태 공간과 더 깊은 추론 깊이(reasoning depth)를 요구하는 환경에서의 성능은 미지수

- **메커니즘 분석 부족**: 요약 프롬팅이 왜 메타러닝을 가능하게 하는지의 기저 메커니즘에 대한 심층 분석 필요. 주의(attention) 기작, 컨텍스트 창 활용, 학습 업데이트 메커니즘 등의 상세 조사 필요

- **일반화 범위의 제한**: 평가가 제로샷 프롬팅에 한정. 소수샷(few-shot) 또는 강화학습적 파인튜닝(RL fine-tuning)과의 비교 부재

- **환경 동역학 변화의 단순성**: Alchemy에서의 환경 변화가 제한적. 더 다양하고 급격한 규칙 변화 시나리오에서의 적응 능력 평가 필요

- **최신 모델 포함 필요**: o1, o3 등 최신 추론 특화 모델의 탐색 능력 평가. 더 장기간의 다중 턴 추론 능력 측정

## Evaluation

- **Novelty**: 4/5
  - 파운데이션 모델의 탐색 능력을 체계적으로 측정한 첫 연구로, 메타러닝과 전략 적응의 조건부 출현이라는 새로운 발견
  - 다만 개별 능력의 개념화 자체는 기존 문헌에서 도출됨

- **Technical Soundness**: 4/5
  - 명확한 측정 기준 정의 및 체계적 실험 설계가 강점
  - 환경 설계의 단순성과 비전 피드백 처리의 한계, 메커니즘 분석 부족이 약점

- **Significance**: 4/5
  - 파운데이션 모델이 "경험의 시대"로 진입할 때 필요한 핵심 능력 평가로 중요함
  - Alchemy를 활용한 벤치마크 기여, 모델 간 이질성 드러냄
  - 다만 현실 응용까지의 거리 있음

- **Clarity**: 4/5
  - 명확한 문제 정의, 논리적 진행, 좋은 시각화
  - 메커니즘 분석 섹션이 더 깊이 있으면 좋음

- **Overall**: 4/5

**총평**: 본 논문은 파운데이션 모델의 대화형 탐색 능력을 최초로 체계적으로 평가하여 학계와 산업에 중요한 벤치마크와 통찰을 제공한다. 특히 요약 프롬팅을 통한 창발적 메타러닝은 기술적 관심이 높으며, Alchemy 벤치마크 도입으로 향후 연구의 기초를 마련했다. 다만 메커니즘 분석 심화와 더 복잡한 환경에서의 검증이 필요하다.

## Related Papers

- 🏛 기반 연구: [[papers/672_ResearchGym_Evaluating_Language_Model_Agents_on_Real-World_A/review]] — 대화형 환경에서의 능동적 탐색 능력 평가가 AI 연구 에이전트 평가의 방법론적 기반
- 🔄 다른 접근: [[papers/815_ToolLLM_Facilitating_Large_Language_Models_to_Master_16000_R/review]] — API 도구 사용과 달리 환경과의 능동적 상호작용을 통한 정보 수집 능력에 집중
- 🔗 후속 연구: [[papers/542_Mlagentbench_Evaluating_language_agents_on_machine_learning/review]] — ML 실험 에이전트가 능동적 탐색을 통해 효율적으로 실험을 설계하는 능력 평가로 확장
- 🔄 다른 접근: [[papers/400_Hiagent_Hierarchical_working_memory_management_for_solving_l/review]] — 계층적 메모리 관리와 달리 능동적 환경 탐색을 통한 문제 해결 접근
- 🔗 후속 연구: [[papers/890_Your_Brain_on_ChatGPT_Accumulation_of_Cognitive_Debt_when_Us/review]] — 대화형 정보 수집에서 기초 모델의 능력을 탐구하여 AI 의존성의 인지적 영향을 더 깊이 이해할 수 있습니다.
- 🏛 기반 연구: [[papers/672_ResearchGym_Evaluating_Language_Model_Agents_on_Real-World_A/review]] — 대화형 환경에서의 능동적 탐색 능력 평가 방법론을 연구 에이전트 평가에 적용한 기반
- 🔄 다른 접근: [[papers/815_ToolLLM_Facilitating_Large_Language_Models_to_Master_16000_R/review]] — 능동적 정보 수집에 중점을 둔 접근과 달리 구체적 API 도구 활용 능력에 집중
