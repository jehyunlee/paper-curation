---
title: "135_Automl_in_the_age_of_large_language_models_Current_challenge"
authors:
  - "Alexander Tornede"
  - "Difan Deng"
  - "Theresa Eimer"
  - "Joseph Giovanelli"
  - "Aditya Mohan"
date: "2023"
doi: "arXiv:2306.08107"
arxiv: ""
score: 4.5
essence: "본 논문은 AutoML(자동 기계학습)과 LLM(대규모 언어 모델)의 상생적(symbiotic) 통합을 제안하며, 양 분야가 서로를 어떻게 강화할 수 있는지를 포괄적으로 탐색한다. AutoML이 LLM 최적화에 가져오는 도전과제, LLM이 AutoML 개선에 제공하는 기회, 그리고 통합 과정에서 발생할 수 있는 위험을 체계적으로 분석한다."
tags:
  - "cat/AI-Powered_Scientific_Research_Frameworks"
  - "sub/Scientific_Code_Generation"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Dong et al._2023_Automl in the age of large language models Current challenges, future opportunities and risks.pdf"
---

# Automl in the age of large language models: Current challenges, future opportunities and risks

> **저자**: Alexander Tornede, Difan Deng, Theresa Eimer, Joseph Giovanelli, Aditya Mohan, Tim Ruhkopf, Sarah Segel, Daphne Theodorakopoulos, Tanja Tornede, Henning Wachsmuth, Marius Lindauer | **날짜**: 2023 | **DOI**: [arXiv:2306.08107](https://arxiv.org/abs/2306.08107)

---

## Essence

![Figure 1](figures/fig1.webp) 
*AutoML이 LLM 생명주기(사전학습, 미세조정, 추론)의 모든 단계에 적용될 수 있으며, 각 단계의 서로 다른 목표, 하이퍼파라미터, 설계 결정에 맞춰 조정되어야 함을 보여줌*

본 논문은 AutoML(자동 기계학습)과 LLM(대규모 언어 모델)의 상생적(symbiotic) 통합을 제안하며, 양 분야가 서로를 어떻게 강화할 수 있는지를 포괄적으로 탐색한다. AutoML이 LLM 최적화에 가져오는 도전과제, LLM이 AutoML 개선에 제공하는 기회, 그리고 통합 과정에서 발생할 수 있는 위험을 체계적으로 분석한다.

## Motivation

- **Known**: AutoML은 ML 파이프라인 자동화를 통해 민주화를 달성했으며, LLM은 NLP 분야에서 획기적 성과를 이뤘다. 각 분야는 독립적으로 remarkable 진전을 이루었다.

- **Gap**: 현재 AutoML 방법론은 LLM의 전체 생명주기(사전학습, 미세조정, 추론)를 holistic하게 최적화하기 위해 설계되지 않았으며, 반대로 LLM의 강력한 NLP 능력이 AutoML 도구 자체를 개선하는 데 충분히 활용되지 않고 있다.

- **Why**: LLM의 사전학습은 극도로 비용이 높고, 다단계 훈련 프로세스는 서로 다른 학습 패러다임(자기지도학습, 지도학습, 강화학습)을 필요로 하며, 각 단계가 다른 평가 지표를 사용한다. 동시에 LLM의 자연언어 처리 및 meta-learning 능력은 AutoML 도구의 인터페이스와 내부 컴포넌트를 혁신할 수 있다.

- **Approach**: AutoML for LLM(제2장), LLM for AutoML(제3장), 그리고 위험 평가(제4장)라는 세 가지 관점에서 상생 관계를 체계적으로 조사한다.

## Achievement

![Figure 1](figures/fig1.webp)
*LLM 생명주기 전체에 걸친 AutoML 적용의 도전과제와 최적화 대상*

1. **AutoML for LLM의 주요 도전과제 규정**: 
   - 사전학습의 극도의 계산 비용으로 인한 제한된 학습 실행
   - 다단계 훈련 프로세스에서 joint optimization의 불가능성
   - Neural Architecture Search(NAS) 성숙도 부족
   - 단계별 다른 평가 지표의 노이즈와 편향 문제
   - 다양한 학습 패러다임 동시 고려의 어려움

2. **LLM for AutoML의 기회 제시**:
   - 자연언어를 통한 Human-Machine Interaction (HMI) 개선
   - AutoML 시스템 설정의 자동화 및 설명 가능성 강화
   - Meta-learning을 통한 AutoML 컴포넌트 개선
   - 비정형 텍스트 데이터로부터의 AutoML 지식 추출

3. **통합의 잠재적 위험 분류**:
   - LLM hallucination으로 인한 catastrophic failures
   - AutoML 결과에 대한 과도한 신뢰
   - 평가 방법론 부족
   - 계산 자원 수요의 지수적 증가

## How

![Figure 1](figures/fig1.webp)
*각 LLM 생명주기 단계별 AutoML 적용 방식*

### AutoML for LLMs 접근법:

- **사전학습 최적화**: Transfer learning 활용, 데이터 선택(data selection), 토크나이제이션(tokenization) 최적화, 네트워크 아키텍처 설계
- **미세조정 최적화**: Hyperparameter Optimization (HPO)를 통한 학습률, 배치 크기, 옵티마이저 선택; Adapter 기반 파라미터 효율적 미세조정(Parameter-Efficient Fine-Tuning, PEFT)
- **Alignment 최적화**: Reinforcement Learning from Human Feedback (RLHF)의 Reward Model(RM)과 Policy 최적화
- **추론 최적화**: 온도(temperature), Top-K 샘플링, 가지치기(pruning), 혼합정밀도(mixed precision) 등의 설정 자동화

### LLMs for AutoML 접근법:

- **Human-Machine Interaction 강화**: 자연언어 프롬프트를 통한 직관적 시스템 상호작용, 결과 설명의 자동 생성
- **Configuration Assistance**: 사용자의 도메인 지식 없이도 AutoML 도구의 복잡한 설정을 자동으로 수행
- **Meta-learning Component**: 웹의 비정형 텍스트에 포함된 AutoML 관련 지식을 추출하여 모델 선택 및 하이퍼파라미터 추천에 활용
- **AutoML Components 대체**: 특정 AutoML 서브컴포넌트를 LLM 기반 솔루션으로 대체

## Originality

- **학제적 통합 관점의 신선성**: AutoML과 LLM 두 분야의 상생적 관계를 처음으로 체계적으로 탐색하는 종합 분석 제공
- **LLM 생명주기에 대한 AutoML 적용의 현실적 평가**: 단순히 기존 AutoML 기법을 적용하는 것이 아닌, LLM의 고유한 특성(극도의 계산 비용, 다단계 프로세스, 다양한 학습 패러다임)에 따른 새로운 도전과제를 명확히 정의
- **위험 요소의 명시적 분석**: 기술적 기회뿐 아니라 hallucination, 평가 방법론 부족, 과도한 신뢰 등의 구체적 위험을 제시
- **양방향 시너지 강조**: AutoML→LLM뿐 아니라 LLM→AutoML 개선 경로도 동등하게 상세히 분석

## Limitation & Further Study

- **현재 한계**:
  - 제시된 많은 기회(opportunities)는 개념적 수준이며, 실제 구현과 평가 사례가 제한적
  - AutoML for LLM의 실행 가능성이 현재 기술로는 낮은 이유에 대한 깊이 있는 분석 부족
  - LLM hallucination 방지 메커니즘의 구체적 기술 솔루션 제시 부족
  - Multi-modal LLM으로의 확장 논의가 제한적

- **후속 연구 방향**:
  - AutoML for LLM의 실제 프로토타입 구현 및 벤치마킹 연구 필요
  - LLM 기반 AutoML 컴포넌트의 신뢰성 및 안정성 평가 체계 개발
  - 사전학습 비용 문제를 해결하기 위한 경량 surrogate 모델 연구
  - AutoML과 LLM 통합의 환경 영향(computational footprint) 평가


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4/5
- Significance: 4.5/5
- Clarity: 4.5/5
- Overall: 4.5/5

**총평**: 본 논문은 AutoML과 LLM의 상생적 통합에 대한 최초의 포괄적 분석으로, 현실적인 도전과제 규정과 함께 양방향 기회를 체계적으로 제시함으로써 향후 연구 방향을 명확히 한다. 다만 개념적 수준의 제안이 많고 구체적 구현 사례가 부족한 점이 아쉬우며, 제시된 위험 요소에 대한 미티게이션 전략 개발이 후속 연구의 중요한 과제가 될 것으로 예상된다.

## Related Papers

- 🏛 기반 연구: [[papers/770_Starcoder_2_and_the_stack_v2_The_next_generation/review]] — AutoML과 LLM의 통합이 코드 생성 모델의 자동 최적화와 성능 향상에 필수적인 방법론적 기반을 제공한다
- 🏛 기반 연구: [[papers/771_Starcoder_may_the_source_be_with_you_arXiv_preprint_arXiv230/review]] — 대형언어모델과 자동 기계학습의 상생적 통합 연구가 오픈소스 코드 생성 모델의 개발과 최적화에 핵심적인 이론적 토대가 된다
- 🔗 후속 연구: [[papers/253_Data_Interpreter_An_LLM_Agent_For_Data_Science/review]] — AutoML과 LLM의 통합 원리가 데이터 사이언스 자동화를 위한 LLM 에이전트 개발에 직접적으로 적용되고 확장된다
- 🧪 응용 사례: [[papers/549_Mlr-copilot_Autonomous_machine_learning_research_based_on_la/review]] — AutoML과 LLM의 상생적 통합 개념이 자율적인 기계학습 연구 수행을 위한 LLM 기반 코파일럿 시스템 구현에 핵심적으로 활용된다
- 🏛 기반 연구: [[papers/016_A_practical_evaluation_of_AutoML_tools_for_binary_multiclass/review]] — 대형 언어모델 시대의 AutoML 현재 도전과 미래 방향은 AutoML 도구 실제 평가의 이론적 맥락과 발전 방향을 제시합니다
- 🏛 기반 연구: [[papers/253_Data_Interpreter_An_LLM_Agent_For_Data_Science/review]] — LLM 기반 데이터 사이언스 에이전트가 AutoML과 LLM의 상생적 통합 원리를 데이터 분석 자동화에 구체적으로 적용한 결과이다
- 🧪 응용 사례: [[papers/770_Starcoder_2_and_the_stack_v2_The_next_generation/review]] — 대규모 코드 생성 모델의 성능 향상이 AutoML과 LLM의 상생적 통합을 통한 자동 최적화에 핵심적으로 기여한다
- 🏛 기반 연구: [[papers/771_Starcoder_may_the_source_be_with_you_arXiv_preprint_arXiv230/review]] — 오픈소스 코드 LLM의 투명성과 성능이 AutoML과 LLM의 상생적 통합을 통한 코드 생성 최적화에 필수적인 기반을 제공한다
- 🏛 기반 연구: [[papers/136_Automl-gpt_Automatic_machine_learning_with_gpt/review]] — LLM 시대 AutoML의 현재 도전과제와 기회에 대한 포괄적 분석을 제공한다.
