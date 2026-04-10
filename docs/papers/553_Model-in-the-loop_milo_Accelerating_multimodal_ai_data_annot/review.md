---
title: "553_Model-in-the-loop_milo_Accelerating_multimodal_ai_data_annot"
authors:
  - "Y. Q. Wang"
  - "David Stevens"
  - "Pranay Shah"
  - "Wenwen Jiang"
  - "Miao Liu"
date: "2024"
doi: "미제공"
arxiv: ""
score: 4.3
essence: "본 논문은 전문 인간 주석자와 대규모 언어모델(LLM)의 협력을 통해 멀티모달 AI 데이터 주석 프로세스를 가속화하는 Model-in-the-Loop (MILO) 프레임워크를 제시한다. LLM을 사전 주석, 실시간 보조, 검증자로 활용하여 주석 시간 단축 및 품질 향상을 달성했다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/Multi-agent_Task_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Wang et al._2024_Model-in-the-loop (milo) Accelerating multimodal ai data annotation with llms.pdf"
---

# Model-in-the-loop (milo): Accelerating multimodal ai data annotation with llms

> **저자**: Y. Q. Wang, David Stevens, Pranay Shah, Wenwen Jiang, Miao Liu, Xu Chen, Robert Kuo, Na Li, Boying Gong, Daniel J. Lee, Jiabo Hu, Ning Zhang, Bob Kamma | **날짜**: 2024 | **DOI**: [미제공](https://doi.org/)

---

## Essence

![Figure 1](figures/fig1.webp)
*MILO 프레임워크: 데이터 주석 시스템에 AI/ML 모델을 통합하는 구조*

본 논문은 전문 인간 주석자와 대규모 언어모델(LLM)의 협력을 통해 멀티모달 AI 데이터 주석 프로세스를 가속화하는 Model-in-the-Loop (MILO) 프레임워크를 제시한다. LLM을 사전 주석, 실시간 보조, 검증자로 활용하여 주석 시간 단축 및 품질 향상을 달성했다.

## Motivation

- **Known**: AI 모델 학습을 위한 데이터 주석은 전 지구적 산업이 되었으며, 기존의 인간 주석자 중심 접근법은 시간 소비적이고 노동집약적이며 품질 불일치 문제가 존재한다. 최근 LLM의 발전으로 모델이 인간 주석자를 대체하거나 보강할 수 있다는 연구가 증가하고 있다.

- **Gap**: 기존 연구는 주로 LLM과 크라우드소싱 워커의 성능 비교에 집중했고, 전문 주석자의 생산성 향상에 대한 연구는 제한적이다. 또한 모델은 신뢰도 필터나 다중 검토 설정의 추가 라벨러 역할에만 제한적으로 적용되었으며, HCI(Human-Computer Interaction) 설계 원칙을 통한 전략적 협력 방안이 부족하다.

- **Why**: 복잡하고 주관적이며 다양한 데이터 주석은 여전히 도메인 전문성이 필요하므로, 인간 주석자와 모델을 모두 활용하는 시스템 설계가 필수적이다. 특히 LLM 개발의 사후훈련(Post-training) 단계에서 인간 주석은 필수불가결하다.

- **Approach**: 본 논문은 주석 라이프사이클 전반에서 인간-모델 협력을 위한 대화형 프레임워크(MILO)를 개발하고, 주관적 품질 평가 방법론을 제시하며, 실제 프로덕션 환경에서 3가지 경험적 연구를 수행하여 효과를 입증한다.

## Achievement

![Figure 2](figures/fig2.webp)
*미세조정된 Llama 모델의 ROC 곡선 및 AUC 메트릭*

![Figure 4](figures/fig4.webp)
*사전 주석 LLM 보조 기능의 유무에 따른 작업당 처리 시간 차이(초)*

1. **주석 효율성 향상**: 사전 주석(pre-annotation) LLM 보조 기능을 통해 주석 처리 시간을 현저히 단축. 실시간 LLM 보조 기능은 복잡한 멀티모달 주석(예: 시각적 질의응답)에서 처리 시간을 절감하고 품질을 개선.

2. **주석 품질 개선**: LLM 판정자(judge)로서의 역할을 통해 주석 일관성 확보 및 개방형 주석에 대한 세분화된 피드백 제공. 인간 검수자의 편향 감소 및 객관적 평가 기준 제시.

3. **주석자 경험 향상**: 모델 기반 제안과 컨텍스트 정보 제공으로 인지 부하 감소, 주석자 만족도 및 참여도 증가.

## How

![Figure 3](figures/fig3.webp)
*사전 주석 LLM 보조 기능이 포함된 코멘트 분류 주석 UI의 예시*

![Figure 5](figures/fig5.webp)
*시각적 질의응답(VQA) 주석을 위한 실시간 LLM 보조 기능 포함/미포함 UI 비교*

**MILO 프레임워크의 3가지 핵심 역할:**

- **사전 주석 보조(Pre-annotation Assistant)**: 미세조정된 LLM을 활용하여 주석 전 단계에서 예측 라벨과 신뢰도 점수 제공, 주석자의 선택 공간 사전 축소

- **실시간 보조(Real-time Assistant)**: 주석 작업 중 LLM이 컨텍스트 기반 제안, 설명, 관련 정보를 실시간으로 제공하여 복잡한 멀티모달 작업 지원

- **검증자(Judge)**: 주석자의 응답을 평가하고 객관적인 피드백 제공, 품질 기준 적용 및 불일치 탐지

**시스템 구성:**

- 인간 행위자: 주석자(annotators), 감사자(auditors), 연구자(researchers)
- 입력 데이터: 비라벨된 테이블형 데이터(이미지, 비디오, 텍스트, 채팅 등)
- 출력: 라벨/주석 및 메타데이터
- 품질 루브릭: 주관적 기준 평가 및 미세 조정을 위한 평가 지표

## Originality

- **첫 포괄적 협력 프레임워크**: 기존 연구와 달리 단순 비교나 제한된 역할 할당이 아닌, 주석 라이프사이클 전반에서 LLM의 다중 역할(보조, 라벨러, 판정자)을 통합한 실제적 협력 패러다임 제시

- **HCI 기반 설계**: 전통적 주석 시스템에 HCI 설계 원칙을 적용하여 인간-모델 상호작용의 효과성을 극대화

- **주관적 품질 평가 방법론**: 개방형 주석에 대한 세분화된 피드백과 품질 루브릭 도입으로 객관적 평가 기준 제시

- **프로덕션 규모의 실증 연구**: 메타(Meta)의 실제 주석 플랫폼에서 전문 주석자를 대상으로 한 3가지 실험적 연구로 현실적 효과 입증

- **양방향 LLM 개발 사이클**: 주석 과정 개선과 동시에 개선된 주석을 LLM 학습에 재활용하는 순환적 구조 제시

## Limitation & Further Study

- **모델 의존성 위험**: 논문에서 지적한 바와 같이 주석자가 모델 제안에 과도하게 의존할 수 있으며, 이로 인해 인간의 신선한 관점과 피드백이 손실될 수 있는 위험 존재

- **도메인별 일반화**: 3가지 경험적 연구가 특정 도메인/작업에 제한되어 있으므로, 다양한 산업 분야와 주석 작업 유형에 대한 일반화 가능성 미확인

- **LLM 편향 전파**: 사전학습된 LLM의 내재된 편향이 주석 과정에 영향을 미칠 수 있는 메커니즘과 완화 방안에 대한 심도 있는 논의 부족

- **비용-편익 분석 미흡**: LLM API 호출, 미세조정, 인프라 유지 비용 대비 시간 절감 효과의 정량적 분석 및 경제적 실행 가능성 분석 제시 필요

- **후속 연구 방향**: 
  - 주석자-모델 상호작용의 장기적 영향 추적(주석자 스킬 발전, 피로도, 직업만족도)
  - 다언어, 다문화 맥락에서의 MILO 적응성 연구
  - 모델 기반 품질 판정의 신뢰도 검증 및 인간 판정과의 불일치 원인 분석
  - 능동 학습(active learning) 기법과의 통합


## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 5/5
- Clarity: 4/5
- Overall: 4.3/5

**총평**: 본 논문은 대규모 AI 개발에서 실제적 가치가 큰 인간-LLM 협력 주석 프레임워크를 제시하며, 실제 프로덕션 환경에서의 검증을 통해 산업적 기여도가 높다. 다만 모델 편향 전파, 비용-편익 분석, 다양한 맥락에서의 일반화 가능성에 대한 보완이 필요하다.

## Related Papers

- 🔗 후속 연구: [[papers/297_EAA_Automating_materials_characterization_with_vision_langua/review]] — 멀티모달 AI 데이터 분석 가속화 접근법이 복잡한 미시경 실험 워크플로우 자동화로 확장될 수 있습니다.
