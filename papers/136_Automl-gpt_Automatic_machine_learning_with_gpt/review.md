---
title: "136_Automl-gpt_Automatic_machine_learning_with_gpt"
authors:
  - "Shujian Zhang"
  - "Chengyue Gong"
  - "Lemeng Wu"
  - "Xingchao Liu"
  - "Mingyuan Zhou"
date: "2023"
doi: "미제공"
arxiv: ""
score: 3.5
essence: "본 논문은 GPT와 같은 대규모 언어모델(LLM)을 자동 머신러닝(AutoML) 시스템의 컨트롤러로 활용하여, 데이터 처리부터 모델 아키텍처 설계, 하이퍼파라미터 튜닝까지 전체 머신러닝 파이프라인을 자동화하는 AutoML-GPT 시스템을 제안한다. 모델 카드(Model Card)와 데이터 카드(Data Card)를 활용한 구조화된 프롬프트를 통해 LLM이 다양한 AI 작업을 자동으로 최적화할 수 있게 한다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/Specialized_Domain_Agents"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Zhang et al._2023_Automl-gpt Automatic machine learning with gpt.pdf"
---

# AutoML-GPT: Automatic Machine Learning with GPT

> **저자**: Shujian Zhang, Chengyue Gong, Lemeng Wu, Xingchao Liu, Mingyuan Zhou | **날짜**: 2023 | **DOI**: [미제공](https://arxiv.org/abs/2305.02499)

---

## Essence

![Figure 1](figures/fig1.webp)
*그림 1: AutoML-GPT의 개요. 데이터 처리부터 모델 아키텍처, 하이퍼파라미터 튜닝, 예측 훈련 로그 생성까지의 전체 파이프라인을 보여줌*

본 논문은 GPT와 같은 대규모 언어모델(LLM)을 자동 머신러닝(AutoML) 시스템의 컨트롤러로 활용하여, 데이터 처리부터 모델 아키텍처 설계, 하이퍼파라미터 튜닝까지 전체 머신러닝 파이프라인을 자동화하는 AutoML-GPT 시스템을 제안한다. 모델 카드(Model Card)와 데이터 카드(Data Card)를 활용한 구조화된 프롬프트를 통해 LLM이 다양한 AI 작업을 자동으로 최적화할 수 있게 한다.

## Motivation

- **Known**: ChatGPT와 GPT-4 같은 LLM들이 뛰어난 추론, 이해, 상호작용 능력을 보유하고 있으며, 여러 새로운 연구 분야(In-context learning, Chain-of-thought prompting 등)를 촉발함

- **Gap**: 기존 머신러닝 시스템은 적절한 모델 아키텍처, 최적화 알고리즘, 하이퍼파라미터 선택을 위해 상당한 인적 노력이 필요하며, 이를 자동화하는 일반화된 방법이 부족함

- **Why**: 언어를 범용 인터페이스로 활용하면 LLM의 강력한 언어 이해 능력으로 복잡한 머신러닝 작업을 자동화할 수 있을 것으로 예상

- **Approach**: 구조화된 모델 카드와 데이터 카드를 프롬프트로 변환하여 LLM에 입력하고, 예측 훈련 로그를 생성해 하이퍼파라미터를 자동 튜닝하는 파이프라인 설계

## Achievement

![Figure 4](figures/fig4.webp)
*그림 4: 미지의 데이터셋에 대한 AutoML-GPT의 작동 방식. 텍스트 인코더를 통한 데이터셋 유사도 계산 및 예측 훈련 로그 생성*

1. **통합 자동화 시스템**: 데이터 처리, 모델 아키텍처 설계, 하이퍼파라미터 튜닝의 전체 머신러닝 파이프라인을 LLM 기반으로 자동화하는 시스템 구현

2. **다중 도메인 적용성**: 컴퓨터 비전(Computer Vision), 자연어처리(NLP), 지속학습(Continual Learning) 등 다양한 AI 작업에서 효과적인 성능 달성

3. **미지 데이터셋 대응**: 메타데이터만으로 새로운 데이터셋에 대한 하이퍼파라미터 튜닝이 가능하여 전이 학습(Transfer Learning) 효과 제공

4. **확장 가능한 아키텍처**: 새로운 모델과 작업별 전문가 모델을 지속적으로 추가할 수 있는 확장성 있는 설계

## How

![Figure 2](figures/fig2.webp)
*그림 2: 데이터 카드는 데이터 이름, 입력 데이터 타입, 레이블 공간, 평가 지표로 구성*

![Figure 3](figures/fig3.webp)
*그림 3: 모델 카드는 모델 이름, 모델 구조, 모델 설명, 아키텍처 하이퍼파라미터로 구성*

AutoML-GPT의 작동 방식:

- **입력 분해(Input Decomposition)**: 사용자의 요청을 데이터 카드, 모델 카드, 평가 지표 및 추가 요청사항으로 구조화

- **데이터 처리(Data Processing)**: 컴퓨터 비전의 경우 이미지 리사이징, 정규화, 증강(Augmentation), 필터링 등을 적용하고, NLP의 경우 토크나이제이션(Tokenization), 불용어 제거, 소문자 변환 등을 수행

- **모델 아키텍처 선택**: In-context 작업-모델 할당 메커니즘으로 주어진 작업에 적합한 모델을 동적으로 선택

- **예측 훈련 로그 기반 하이퍼파라미터 튜닝**: 실제 학습 없이 LLM이 생성한 예측 훈련 로그(Epoch, Loss, Accuracy 등)를 기반으로 최적 하이퍼파라미터 제시

- **인간 피드백 루프**: 생성된 훈련 로그에 대해 사용자 피드백을 받아 추가 튜닝 반복

## Originality

- **LLM 기반 AutoML의 새로운 패러다임**: LLM을 머신러닝 파이프라인의 중앙 컨트롤러로 활용하는 혁신적 접근으로, 기존의 베이지안 최적화나 강화학습 기반 AutoML과 차별화

- **구조화된 프롬프트 설계**: 모델 카드와 데이터 카드라는 표준화된 형식을 활용하여 일관성 있고 재사용 가능한 프롬프트 구조 제안

- **예측 훈련 로그 기반 튜닝**: 실제 모델 훈련 없이 LLM이 생성한 예측 훈련 로그로 하이퍼파라미터를 최적화하는 창의적 접근

- **메타데이터 기반 전이 학습**: 전체 데이터 없이 데이터셋의 메타데이터만으로 미지의 데이터셋에 대한 하이퍼파라미터 추천 가능

## Limitation & Further Study

**한계점:**
- 예측 훈련 로그의 정확성 검증 부재: LLM이 생성하는 훈련 로그가 실제 훈련 결과와 얼마나 일치하는지에 대한 정량적 검증 부족
- 복잡한 모델 아키텍처의 설명 어려움: 깊고 복잡한 모델 구조를 카드 형식으로 모두 표현할 수 있는지 불명확
- 계산 비용 분석 부재: 빈번한 LLM 쿼리로 인한 실제 계산 비용 논의 없음
- 모델 카드와 데이터 카드의 수동 작성 필요성: 여전히 인적 개입이 필요한 초기 단계

**후속 연구 방향:**
- 예측 훈련 로그와 실제 훈련 결과 간의 갭을 줄이기 위한 피드백 메커니즘 강화
- 더 복잡한 멀티태스크 학습(Multi-task Learning) 시나리오로 확장
- 카드 형식의 자동 생성 방법 개발
- LLM 쿼리 최소화를 통한 효율성 개선 연구

## Evaluation

- **Novelty**: 4/5
  - LLM을 AutoML 컨트롤러로 사용하는 새로운 개념이지만, 프롬프트 엔지니어링과 LLM 활용의 기본 개념을 결합한 것으로 완전히 새로운 패러다임은 아님

- **Technical Soundness**: 3/5
  - 전체적인 파이프라인 구조는 타당하지만, 예측 훈련 로그의 정확성 메커니즘과 검증 과정이 불명확함. 실제 구현 세부사항 부족

- **Significance**: 4/5
  - 머신러닝 자동화의 접근성을 크게 높이고 실무 활용도가 높으나, 예측 로그의 신뢰성 검증이 없어 실제 프로덕션 적용의 한계 있음

- **Clarity**: 3.5/5
  - 시스템 전체 구조와 파이프라인은 명확하게 설명되었으나, 각 단계별 구현 방법과 LLM의 구체적인 프롬프팅 전략이 부족함

- **Overall**: 3.5/5

**총평**: AutoML-GPT는 LLM의 강력한 언어 이해 능력을 머신러닝 자동화에 창의적으로 적용한 흥미로운 시도이며, 다양한 도메인에서의 응용 가능성이 높다. 그러나 예측 훈련 로그의 정확성 검증 부재와 실제 구현 세부사항의 부족으로 기술적 완성도 측면에서 개선이 필요하다.

## Related Papers

- 🏛 기반 연구: [[papers/135_Automl_in_the_age_of_large_language_models_Current_challenge/review]] — LLM 시대 AutoML의 현재 도전과제와 기회에 대한 포괄적 분석을 제공한다.
- 🔄 다른 접근: [[papers/594_OSDA_Agent_Leveraging_Large_Language_Models_for_De_Novo_Desi/review]] — 데이터 과학 자동화에서 AutoML과 다중 에이전트 시스템이라는 다른 접근 방식을 보여준다.
- 🧪 응용 사례: [[papers/121_Autokaggle_A_multi-agent_framework_for_autonomous_data_scien/review]] — Kaggle 경진대회 자동화를 통한 AutoML의 구체적 적용 사례를 제시한다.
- 🔄 다른 접근: [[papers/543_Mlcopilot_Unleashing_the_power_of_large_language_models_in_s/review]] — AutoML-GPT와 MLCopilot 모두 LLM을 활용한 자동 머신러닝을 추구하지만 전자는 자동화, 후자는 경험 기반 솔루션 제시에 중점을 둔다.
