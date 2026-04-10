---
title: "723_Sciglm_Training_scientific_language_models_with_self-reflect"
authors:
  - "Dan Zhang"
  - "Ziniu Hu"
  - "Sining Zhoubian"
  - "Zhengxiao Du"
  - "Kaiyu Yang"
date: "2024"
doi: "arXiv:2401.07950"
arxiv: ""
score: 4.0
essence: "SciGLM은 자기 성찰적(self-reflective) 주석 생성 프레임워크를 통해 고품질의 과학 지시 데이터를 자동으로 큐레이션하고, 이를 이용해 여러 언어 모델을 파인튜닝함으로써 대학 수준의 과학 추론 능력을 갖춘 과학 언어 모델을 구축한다. GPT-3.5와 GPT-4 같은 고급 LLM도 기본적인 과학 문제에서 28.52%의 낮은 정확도를 보이는 문제를 해결하기 위해, 물리, 화학, 수학, 형식적 증명(Lean)을 포함하는 254,051개의 고품질 과학 지시문을 포함한 SciInstruct 데이터셋을 구축했다."
tags:
  - "cat/Scientific_Language_Processing_and_Visualization"
  - "sub/Domain-adapted_Instruction_Models"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Zhang et al._2024_Sciglm Training scientific language models with self-reflective instruction annotation and tuning.pdf"
---

# Sciglm: Training scientific language models with self-reflective instruction annotation and tuning

> **저자**: Dan Zhang, Ziniu Hu, Sining Zhoubian, Zhengxiao Du, Kaiyu Yang, Zihan Wang, Yisong Yue, Yuxiao Dong, Jie Tang | **날짜**: 2024 | **DOI**: [arXiv:2401.07950](https://arxiv.org/abs/2401.07950)

---

## Essence

![Figure 3: 다양한 LLM의 과학 벤치마크 평균 정확도](figures/fig3.webp)
*다양한 파라미터 크기의 LLM들에 대한 SciGLM의 성능 개선 효과*

SciGLM은 자기 성찰적(self-reflective) 주석 생성 프레임워크를 통해 고품질의 과학 지시 데이터를 자동으로 큐레이션하고, 이를 이용해 여러 언어 모델을 파인튜닝함으로써 대학 수준의 과학 추론 능력을 갖춘 과학 언어 모델을 구축한다. GPT-3.5와 GPT-4 같은 고급 LLM도 기본적인 과학 문제에서 28.52%의 낮은 정확도를 보이는 문제를 해결하기 위해, 물리, 화학, 수학, 형식적 증명(Lean)을 포함하는 254,051개의 고품질 과학 지시문을 포함한 SciInstruct 데이터셋을 구축했다.

## Motivation

- **Known**: LLM들이 과학 발견 보조에 잠재력을 보이고 있으며, 단순 추론 작업에서는 우수한 성능을 달성함.

- **Gap**: GPT-3.5, GPT-4와 같은 고급 LLM도 물리 상수 계산, 기호적 방정식 도출, 고급 수치 계산 등 대학 수준의 과학 문제에서 심각한 성능 부족(28.52% 정확도)을 보임. 과학 분야의 고품질 지시 데이터 부족으로 인해 LLM의 과학적 추론 능력 향상이 저해됨.

- **Why**: 과학 지식은 높은 전문성을 요구하고, 양질의 정보는 지적재산권으로 보호되어 합법적으로 접근 가능한 데이터는 대부분 질문-답변(QA) 쌍 형태이며 단계별 추론 과정(chain-of-thought, CoT)이 부재함. 이러한 데이터로만 훈련하면 모델 성능이 악화되고 일반 언어 이해 능력도 손상됨.

- **Approach**: LLM이 자율적으로 추론 단계를 주석 처리하고, 오류를 자가 진단하며, 개선하는 자기 성찰적 주석 생성 프레임워크를 제안. 이를 통해 최소한의 인간 개입으로 고품질 지시 데이터를 대규모로 생성하고, 여러 언어 모델(ChatGLM3 6B/32B, Llama3-8B-Instruct, Mistral-7B)을 파인튜닝.

## Achievement

![Figure 4: SciInstruct 구축 파이프라인](figures/fig4.webp)
*다양한 소스로부터 데이터 수집, 자기 성찰적 주석, 필터링을 거쳐 고품질 지시문 생성*

![Figure 5: 자기 성찰적 주석 생성 프레임워크의 워크플로우](figures/fig5.webp)
*3단계 반복 과정을 통한 단계별 정확한 추론 과정 생성의 예시*

1. **포괄적 과학 지시 데이터셋 구축**: 물리학, 화학, 수학, 형식적 증명(Lean)을 포함하는 254,051개의 검증된 고품질 지시문으로 구성된 SciInstruct 데이터셋 완성. 도메인별 비중은 물리&화학 48.8%, 수학 35.4%, 형식적 증명 15.8%이며, 질문 유형은 채우기형(33.2%), 선택형(32.0%), 복잡한 풀이형(20.1%), 간단한 풀이형(14.6%)으로 다양화.

2. **성능 향상 검증**: ChatGLM3 6B 모델에서 4.87%, 32B 모델에서 2.67% 정확도 개선 달성. 동일 파라미터 크기의 선행 모델들(Galactica, MAmmoTH)을 능가하며, GPT-4와의 격차를 축소. 과학 벤치마크(CEval-Sci, Sci-Eval, SciBench, MATH, SAT-Math)에서 평균 정확도 향상을 보임.

3. **일반 언어 능력 보존**: 지시 튜닝을 통한 성능 향상이 기본 모델의 일반 언어 이해 및 코딩 능력을 손상시키지 않음을 검증. SciGLM이 인간-AI 상호작용 및 과학 도메인 전문 지식 모두에 적합한 균형잡힌 모델임을 입증.

## How

![Figure 1: 도메인 비중](figures/fig1.webp)
![Figure 2: 질문 유형 비중](figures/fig2.webp)

**데이터 수집 및 큐레이션**:
- 물리, 화학, 수학, 형식적 증명(Lean) 등 다양한 과학 분야의 교과서, 교육 자료, 문제집으로부터 기본 QA 데이터 수집
- 기존 공개 데이터셋(Fundamentals of Physics, Physical Chemistry 등)의 부족한 부분을 고등 교육 수준의 문제로 보완

**자기 성찰적 주석 생성 프레임워크 (3단계 반복)**:
- **Stage 1 (초기 생성)**: LLM에 과학 문제만 제시하여 단계별 풀이와 답변 생성. 42,497개 질문 중 19,824개가 정답 달성
- **Stage 2 (오류 반영)**: 오답을 받은 22,673개 문제에 대해 LLM에 오류를 반영하도록 지시. 5,458개 추가 정답 달성
- **Stage 3 (개선된 반영)**: 여전히 오답인 17,215개 문제에 대해 정답을 제공하고 오류를 분석하도록 재지시. 7,687개 추가 정답 달성
- 최종 32,969개의 정확한 솔루션 획득

**오류 분류 및 자동 필터링**:
- 이해 오류(comprehension mistakes), 계산 오류(calculation mistakes), 잘못된 추론(false reasoning) 등으로 오류 유형화
- 머신러닝 기반 지시문 품질 분류기(instruction-quality classifier) 훈련하여 자동 필터링 수행

**모델 파인튜닝**:
- ChatGLM3 (6B, 32B), Llama3-8B-Instruct, Mistral-7B:MetaMATH 등 여러 기본 모델에 SciInstruct를 통한 지시 튜닝(instruction tuning) 적용
- 다양한 과학 및 수학 벤치마크에서 평가

## Originality

- **혁신적 데이터 큐레이션 방법론**: 인간 주석이 아닌 LLM의 자기 성찰적 비판-개선(critic-and-revise) 프로세스를 통해 고품질 지시 데이터를 자동 생성하는 방식의 창의성. 기존 방식의 비용 및 확장성 문제를 획기적으로 해결.

- **포괄적 과학 도메인 통합**: 물리, 화학, 수학, 형식적 증명을 모두 포함하는 통합 과학 지시 데이터셋 구축. 단일 분야 과적합(overfitting)을 방지하고 일반화된 과학적 추론 능력 개발.

- **다단계 반복적 개선 프레임워크**: 단순한 일회성 생성이 아닌 3단계 반복 과정을 통해 점진적으로 정확도를 향상시키는 구조의 체계성. 오류 분석 및 자동 필터링으로 데이터 품질 보증.

- **광범위한 검증 및 공개**: 여러 기본 모델(ChatGLM3, Llama3, Mistral)에 걸친 일관된 성능 향상 입증. 코드 및 데이터셋 공개로 학술 커뮤니티의 재현성과 확장성 확보.

## Limitation & Further Study

- **기본 모델의 제약**: 파인튜닝의 효과가 기본 모델의 초기 성능과 능력에 크게 의존. 더 우수한 기본 모델 사용 시 개선 폭이 제한될 가능성.

- **정확도 수준의 절대적 한계**: GPT-4 대비 여전히 정확도 격차가 존재하며, 복잡한 과학 추론 문제에서 기대 이상의 성능 달성에 제약.

- **도메인 균형의 한계**: 물리&화학(48.8%)에 대한 가중치가 높아 다른 과학 분야(예: 생물학, 지구과학)의 상대적 부족.

- **자동 필터링의 정확도**: 지시문 품질 분류기의 완벽도가 100%가 아니어서 일부 저품질 데이터가 포함될 가능성. 휴먼-인-더-루프(human-in-the-loop) 검증의 추가 필요성.

**후속 연구 방향**:
- 다국어 과학 지시 데이터셋 확장 및 학제간(interdisciplinary) 과학 추론 능력 개발
- 더 복잡한 멀티스텝 과학 문제 및 실험 설계 능력 포함
- 과학 모델과 도메인 특화 도구(수학 엔진, 화학 시뮬레이터)의 통합

## Evaluation

| 항목 | 점수 | 근거 |
|------|------|------|
| **Novelty** | 4/5 | 자기 성찰적 주석 생성 프레임워크는 창의적이고, 포괄적 과학 지시 데이터셋은 기여도가 높음. 다만 기본 개념 자체는 기존 CoT 및 자동 주석 연구에 기초한 점수정. |
| **Technical Soundness** | 4/5 | 방법론이 체계적이고 실행 가능하며, 다단계 반복 프레임워크는 논리적 구조를 가짐. 자동 필터링 메커니즘의 기술적 세부사항이 다소 부족하고, 편향(bias) 분석이 제한적. |
| **Significance** | 4/5 | 과학적 추론 능력 향상이라는 중요한 과제를 다루며, 254,051개 데이터셋과 다중 모델 검증의 실질적 영향이 큼. 다만 절대 성능이 여전히 기대에 못 미치는 부분이 있음. |
| **Clarity** | 4.5/5 | 논문의 구조가 명확하고 Figure들이 프로세스를 잘 시각화함. 파이프라인 설명이 이해하기 쉬우나, 필터링 및 분류기 훈련 부분의 기술 상세도가 개선 필요. |
| **Overall** | 4/5 | 과학 LLM 분야의 중요한 데이터셋과 방법론을 제시한 견실한 연구. 자기 성찰적 주석 생성의 창의성과 광범위한 실험 검증이 강점이나, 절대 성능 향상과 기술 세부사항에서 개선의 여지 있음. |

**총평**: SciGLM은 과학 도메인 LLM 훈련을 위한 자동화된 고품질 데이터셋 구축이라는 실질적 문제를 해결하며, 자기 성찰적 비판-개선 프레임워크는 데이터 부족 분야의 확장성 있는 솔루션을 제시한다. 다만 절대 정확도 수준은 여전히 GPT-4에 미치지 못하고, 도메인 간 균형 개선과 더 복잡한 과학 문제 포

## Related Papers

- 🔄 다른 접근: [[papers/837_Training_a_Scientific_Reasoning_Model_for_Chemistry/review]] — 둘 다 도메인 특화 과학 추론 모델을 구축하지만 하나는 자기 성찰적 지시 데이터를 사용하고 다른 하나는 화학 도메인에 특화된 강화학습을 사용한다.
- 🏛 기반 연구: [[papers/707_SciBERT_A_Pretrained_Language_Model_for_Scientific_Text/review]] — 과학 텍스트를 위한 사전훈련된 언어 모델로서 SciGLM의 과학 도메인 특화 학습에 기반을 제공한다.
- 🔗 후속 연구: [[papers/720_Scientific_Large_Language_Models_A_Survey_on_Biological__Che/review]] — 생물학 및 화학 분야의 과학 대규모 언어 모델에 대한 포괄적인 조사로서 SciGLM의 연구를 더 넓은 맥락에서 이해할 수 있게 한다.
