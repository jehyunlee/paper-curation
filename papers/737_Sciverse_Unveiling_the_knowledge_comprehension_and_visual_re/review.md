---
title: "737_Sciverse_Unveiling_the_knowledge_comprehension_and_visual_re"
authors:
  - "Z. J. Guo"
  - "Renrui Zhang"
  - "Hao Chen"
  - "Jialin Gao"
  - "Dongzhi Jiang"
date: "2025"
doi: "미제공"
arxiv: ""
score: 4.2
essence: "SCIVERSE는 대규모 멀티모달 모델(LMM)의 과학 문제 해결 능력을 세밀하게 평가하기 위한 벤치마크로, 1,147개 문제를 5가지 버전으로 변환한 5,735개 테스트 인스턴스를 제공하며, 과학 지식 이해, 멀티모달 콘텐츠 해석, 연쇄적 사고(CoT) 추론이라는 세 가지 핵심 차원을 체계적으로 평가한다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/Multimodal_Scientific_Reasoning"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Guo et al._2025_Sciverse Unveiling the knowledge comprehension and visual reasoning of lmms on multi-modal scientif.pdf"
---

# Sciverse: Unveiling the knowledge comprehension and visual reasoning of lmms on multi-modal scientific problems

> **저자**: Z. J. Guo, Renrui Zhang, Hao Chen, Jialin Gao, Dongzhi Jiang, Jiaze Wang, Pheng‐Ann Heng | **날짜**: 2025 | **DOI**: [미제공](https://doi.org/)

---

## Essence

![Figure 1](figures/fig1.webp)
*Figure 1: 5가지 문제 버전과 과학적 CoT 평가 전략의 개요. 지식 수준을 달리하는 3가지 버전과 시각 정보 비중을 달리하는 2가지 버전, 그리고 단계별 평가 전략을 제시.*

SCIVERSE는 대규모 멀티모달 모델(LMM)의 과학 문제 해결 능력을 세밀하게 평가하기 위한 벤치마크로, 1,147개 문제를 5가지 버전으로 변환한 5,735개 테스트 인스턴스를 제공하며, 과학 지식 이해, 멀티모달 콘텐츠 해석, 연쇄적 사고(CoT) 추론이라는 세 가지 핵심 차원을 체계적으로 평가한다.

## Motivation

- **Known**: 최근 LLM과 LMM의 발전으로 물리, 화학, 생물학 등 다양한 과학 분야의 문제 해결에 활용되고 있으며, 이미 여러 과학 평가 데이터셋(SceMQA, MMMU, CMMMU)이 존재한다.

- **Gap**: 기존 벤치마크들은 원본 문제에 대한 직접 답변 정확도만 평가하므로, 과학 문제 해결에 필요한 세 가지 핵심 능력(과학 지식 이해, 멀티모달 콘텐츠 해석, CoT 추론)에 대한 세밀한 분석이 부족하다. 특히 지식 부족으로 인한 오류와 논리적 추론 부족으로 인한 오류를 구분하지 못한다.

- **Why**: 실제 과학 문제 해결은 단순 정확도뿐 아니라 다양한 수준의 선행 지식 요구, 다양한 형태의 시각 정보 처리(문서, 필기, 스크린샷), 단계별 추론의 질 평가가 필요하다.

- **Approach**: 각 문제를 지식 수준에 따라 3가지 버전(Knowledge-free, -lite, -rich)으로, 시각-텍스트 정보 배분에 따라 2가지 버전(Vision-rich, Vision-only)으로 변환하고, GPT-4o를 활용한 과학적 CoT 평가 전략을 개발하여 단계별 지식 및 논리 오류를 분석한다.

## Achievement

![Figure 2](figures/fig2.webp)
*Figure 2: SCIVERSE의 주제 분포. 물리학 2,010개(35.0%), 화학 1,880개(32.2%), 생물학 1,845개(32.8%).*

1. **포괄적 벤치마크 구축**: 1,147개의 고품질 과학 문제를 5가지 버전으로 변환하여 5,735개의 평가 인스턴스를 포함하는 SCIVERSE 데이터셋 구축. 물리, 화학, 생물학 3개 주요 학문을 21개 세부 주제로 구분하고 고등학교부터 대학 수준까지 다양한 난이도 포함.

2. **세밀한 평가 틀**: 과학 문제 해결의 세 가지 차원을 각각 평가할 수 있는 다층 구조 제시:
   - 지식 이해: Knowledge-free → Knowledge-lite → Knowledge-rich로 점진적 지식 제공을 통해 지식 부족의 영향 측정
   - 멀티모달 해석: Vision-rich → Vision-only로 텍스트에서 시각 정보로의 점진적 전환을 통해 OCR 및 시각 인식 능력 평가
   - CoT 평가: 단순 정답 여부가 아닌 단계별 지식 오류와 논리 오류를 분리하여 평가

3. **광범위한 실증 분석**: GPT-4o, Claude, Gemini, LLaVA, Qwen-VL 등 다양한 폐쇄형 및 개방형 LMM 평가를 통해 현재 모델들의 과학 분야 한계를 드러냄:
   - 폐쇄형 모델이 개방형 모델보다 지식 이해와 시각 인식에서 우수
   - 모든 모델이 Vision-only 문제에서 심각하게 성능 저하 (실제 상황에 가까운 과제)
   - 폐쇄형 모델이 개방형 모델보다 높은 품질의 CoT 추론 단계 생성

## How

![Figure 1](figures/fig1.webp)
*Figure 1 (하단): 과학적 CoT 평가 전략. 단계별 분류, 지식 및 논리 점수 산출.*

### 데이터 수집 및 변환
- 기존 공개 데이터셋(SceMQA, MMMU, CMMMU)에서 1,200개 문제 초수집
- 박사급 과학 전문가 8명이 지식 복잡도와 시각적 풍부성을 기준으로 1,147개 선별
- 모든 텍스트를 LaTeX 형식 영문으로 표준화, 모든 문제를 객관식으로 통일

### 5가지 문제 버전 설계

**과학 지식 이해 평가:**
- **Knowledge-free**: 주어진 조건 + 핵심 질문만 포함 (배경 지식 없음)
- **Knowledge-lite**: 위에 개념명 또는 공식 참조 추가 (기본 지식 단서)
- **Knowledge-rich**: 구체적 방정식 및 정리 적용 방법 상세 제공 (전문가 수준 지식)

**멀티모달 콘텐츠 해석 평가:**
- **Vision-rich**: 핵심 정보가 다이어그램에만 포함되도록 텍스트 최소화
- **Vision-only**: 텍스트 입력 없이 시각 정보만 포함 (스캔 문서, 필기 등을 시뮬레이션)

### 과학적 CoT 평가 전략
- LMM의 추론 출력을 GPT-4o에 입력하여 단계별로 추출
- 각 단계를 **지식 검토 단계**와 **논리 추론 단계**로 분류
- 각 단계에서 지식 오류(Knowledge Score)와 논리 오류(Logical Score) 독립적 평가
- 최종 점수 산출로 정답은 맞지만 과정이 잘못된 경우 등을 분별

## Originality

- **세밀한 오류 분석**: 기존 벤치마크의 이진 정답/오답 평가를 넘어, 단계별로 지식 오류와 논리 오류를 구분하여 평가하는 새로운 과학적 CoT 평가 방법론 제시

- **계층적 지식 조절**: Knowledge-free/lite/rich 3단계로 단순히 답을 맞히는지가 아니라 얼마나 지식을 이해하고 활용하는지를 측정 가능하게 설계

- **현실적 멀티모달 평가**: Vision-only 버전을 통해 실제 세계의 스캔 문서, 필기, 스크린샷과 같은 시나리오를 평가하는 현실성 높은 설계

- **포괄적 학제 간 평가**: 물리, 화학, 생물학 3개 분야 21개 주제를 균형있게 포함하여 과학 전반의 평가 가능

## Limitation & Further Study

- **데이터 규모 제약**: 1,147개 기본 문제로부터 5가지 버전을 자동 변환하는 과정에서 인적 검증의 한계. 특히 Knowledge-rich 버전 생성 시 정보 추가의 자동화 정도가 불명확.

- **평가 도구의 의존성**: 과학적 CoT 평가 전략이 GPT-4o라는 단일 모델에 의존하므로, 평가자 모델의 편향이 최종 결과에 영향을 미칠 가능성

- **Vision-only 버전의 제한**: 실제 필기나 부분적으로 손상된 문서 등 더 다양한 시각 상황을 포괄하지 못함

- **후속 연구 방향**:
  - 다른 분야(의학, 공학, 지구과학) 확장
  - 더 큰 규모의 데이터셋으로 확대
  - 다언어 버전 개발 (현재 영문만 제공)
  - 시간 관련 추론(temporal reasoning) 등 추가 능력 평가
  - 인간 전문가와 LMM 성능의 정량적 비교 연구

## Evaluation

- **Novelty**: 4.5/5 — 과학 문제의 세밀한 지식 수준 구분과 현실적 멀티모달 시나리오는 참신하지만, 기본 벤치마크 구축 방식은 기존 접근의 확장

- **Technical Soundness**: 4/5 — 데이터 수집과 변환 과정이 체계적이고, CoT 평가 방법론이 명확하나 평가 도구가 GPT-4o에 단일 의존, 자동화 과정의 일관성 검증 부족

- **Significance**: 4.5/5 — LMM의 과학 문제 해결 능력을 정교하게 평가하는 프레임워크 제시로 학계에 중요한 기여. 다만 실제 개선 방안까지 제시하지는 못함

- **Clarity**: 4/5 — 5가지 버전의 구분과 평가 전략이 명확하게 설명되어 있으며 시각적 예시가 충분하나, 데이터 변환 과정의 구체적 기준이 일부 모호

- **Overall**: 4.2/5

**총평**: SCIVERSE는 과학 문제 해결에서 LMM의 지식 이해, 멀티모달 해석, 추론 능력을 체계적으로 분석할 수 있는 잘 설계된 벤치마크로, 특히 현실적인 Vision-only 시나리오와 단계별 오류 분석이 강점이지만, 평가 도구 의존성과 데이터 규모 측면에서 개선의 여지가 있다.

## Related Papers

- 🔄 다른 접근: [[papers/552_Mmsci_A_dataset_for_graduate-level_multi-discipline_multimod/review]] — 둘 다 과학 멀티모달 평가를 위한 벤치마크이지만 SCIVERSE는 세밀한 능력 분석에, MMSCI는 대규모 데이터 수집에 집중함
- 🔗 후속 연구: [[papers/727_Scimage_How_good_are_multimodal_large_language_models_at_sci/review]] — SCIMAGE의 과학 이미지 이해 평가가 SCIVERSE의 멀티모달 콘텐츠 해석 차원을 더욱 구체화함
- 🏛 기반 연구: [[papers/315_Enhancing_chart-to-code_generation_in_multimodal_large_langu/review]] — 차트-코드 생성 향상 기법이 SCIVERSE의 시각적 추론 평가 방법론 개발에 필수적인 기반을 제공함
- 🏛 기반 연구: [[papers/091_Aiscivision_A_framework_for_specializing_large_multimodal_mo/review]] — 지식 이해와 시각적 추론을 통해 과학 분야에서의 다중모달 모델 활용 기반을 제공한다.
- 🔄 다른 접근: [[papers/552_Mmsci_A_dataset_for_graduate-level_multi-discipline_multimod/review]] — 둘 다 과학 멀티모달 벤치마크를 제공하지만 MMSCI는 대학원 수준 복잡성에, SCIVERSE는 세밀한 능력 평가에 집중함
