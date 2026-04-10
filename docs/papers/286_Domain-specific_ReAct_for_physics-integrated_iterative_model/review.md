---
title: "286_Domain-specific_ReAct_for_physics-integrated_iterative_model"
authors:
  - "Tao Song"
  - "Yuwei Fan"
  - "Chen Feng"
  - "Keyu Song"
  - "Chao Liu"
date: "2024"
doi: "10.48550/arXiv.2406.07572"
arxiv: ""
score: 3.75
essence: "본 논문은 LLM(대규모 언어 모델)을 에너지·발전 공학 영역의 실제 문제 해결에 활용하기 위해 ReAct 프롬프팅과 도구 호출 메커니즘을 결합한 도메인 특화 프레임워크를 제시한다. 가스터빈의 가스 경로 분석(gas path analysis)을 사례로 하여 다양한 규모의 LLM들의 능력과 한계를 체계적으로 평가한다."
tags:
  - "cat/LLM-Based_Scientific_Reasoning"
  - "sub/Domain-specific_Scientific_Reasoning"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Song et al._2024_Domain-specific ReAct for physics-integrated iterative modeling A case study of LLM agents for gas.pdf"
---

# Domain-specific ReAct for physics-integrated iterative modeling: A case study of LLM agents for gas path analysis of gas turbines

> **저자**: Tao Song, Yuwei Fan, Chen Feng, Keyu Song, Chao Liu | **날짜**: 2024 | **DOI**: [10.48550/arXiv.2406.07572](https://doi.org/10.48550/arXiv.2406.07572)

---

## Essence

![Figure 2](figures/fig2.webp)
*그림 2: 이중 에이전트 도구 호출 프로세스*

본 논문은 LLM(대규모 언어 모델)을 에너지·발전 공학 영역의 실제 문제 해결에 활용하기 위해 ReAct 프롬프팅과 도구 호출 메커니즘을 결합한 도메인 특화 프레임워크를 제시한다. 가스터빈의 가스 경로 분석(gas path analysis)을 사례로 하여 다양한 규모의 LLM들의 능력과 한계를 체계적으로 평가한다.

## Motivation

- **Known**: LLM은 자연어 처리 및 추론 작업에서 뛰어난 성능을 보이며, RAG, Chain-of-Thought, ReAct 등의 향상 기법이 환각(hallucination)과 설명 불가능성을 완화시킨다.

- **Gap**: 기존 AI 도구들은 에너지 시스템의 복잡성을 이해할 이론적 기초가 부족하고 블랙박스 특성으로 인해 신뢰성과 해석 가능성이 떨어진다. LLM을 도메인 특화 공학 문제에 체계적으로 적용한 사례가 제한적이다.

- **Why**: 에너지·발전 공학은 물리적 법칙 준수가 필수적이고, 복잡한 다중 성분 계산이 필요하므로 LLM의 순수 텍스트 추론만으로는 신뢰할 수 없다.

- **Approach**: 물리 기반 도구를 사전 정의하고 ReAct 기반 이중 에이전트 구조를 설계하여 LLM의 추론 능력과 도메인 지식을 통합한다. 다양한 규모(8B~70B+)의 모델을 비교 평가한다.

## Achievement

![Figure 1](figures/fig1.webp)
*그림 1: 가스터빈의 가스 경로 분석 개요*

1. **이중 에이전트 도구 호출 프로세스 개발**: 기본 도구 호출을 지원하지 않는 모델들도 통일된 프레임워크에서 작동하도록 하는 구조 설계 성공. 에이전트 1은 ReAct 추론으로 행동 결정, 에이전트 2는 JSON 형식으로 도구 파라미터 추출.

2. **모델 성능 차이 규명**: 
   - 소형 모델(LLama3 8B, Qwen1.5 32B): 도구 사용과 파라미터 추출에 실패
   - 대형 모델(LLama3 70B, Qwen1.5 72B, GPT-4o, GLM-4): 도구 기반 계산에서 정확한 결과 도출
   - 모든 모델이 다중 성분의 복잡한 문제에서 어려움을 겪음

3. **규모-능력 관계 제시**: 약 100억 개 파라미터 규모의 LLM이 미세 조정(fine-tuning)과 고급 프롬프트 설계를 통해 전문 시나리오 요구사항을 충족할 가능성 제시.

## How

- **도메인 도구 사전 정의**: 압축기(compressor), 연소실(combustion chamber), 터빈(turbine), 노즐(nozzle) 각각에 대해 열역학 방정식 기반 계산 함수 개발. 근사를 통해 단순화하되, 필요시 더 정교한 모델로 대체 가능한 구조 설계.

- **ReAct 프롬프팅 적용**: 
  - Thought (생각): 현재 상황 분석
  - Action (행동): 사용할 도구 선택
  - Action Input (입력): 도구 파라미터 지정
  - Observation (관찰): 도구 실행 결과
  - Final Answer (최종 답): 결론 도출

- **JSON 기반 파라미터 추출**: 에이전트 2가 LLM 생성 텍스트를 고정 스키마의 JSON으로 변환하여 파싱 오류 최소화.

- **비교 평가 설정**: 로컬 배포 모델(LLama3, Qwen1.5)과 API 기반 모델(GPT-3.5, GPT-4o, GLM-4)을 동일한 프레임워크에서 테스트.

- **단일 성분 vs. 다중 성분 테스트**: 초기 단일 성분 계산 성공 여부와 이후 가스 유량 → 연소실 온도·압력 → 터빈 효율 등의 순차적 다중 단계 문제 해결 능력 평가.

## Originality

- **도메인 특화 프레임워크**: 일반적인 도구 호출 메커니즘을 물리 방정식 기반 에너지 공학 문제에 맞게 맞춤형 설계한 최초의 시도.

- **이중 에이전트 구조**: 네이티브 도구 호출을 지원하지 않는 모델들도 통일된 인터페이스로 활용 가능하게 하는 일반화된 접근법.

- **체계적 모델 비교**: 파라미터 규모(8B~100B+), 제조사(Meta, Alibaba, OpenAI, Zhipu), 배포 방식(로컬/API)을 달리하는 모델들을 동일 기준으로 평가.

- **물리 제약 통합**: 열역학 도구를 강제함으로써 LLM의 순수 텍스트 생성 문제를 해결하고 물리적 타당성 보장.

## Limitation & Further Study

- **근사 및 단순화**: 기체 열물성 상수와 유동 보존 관계식에 다수의 근사 적용. 실제 엔지니어링 정확도 요구 시 더 정교한 모델로의 대체 필요.

- **다중 성분 복잡도**: 모든 모델이 여러 단계의 순차적 계산이 필요한 복잡한 문제에서 추론 연쇄를 유지하지 못함. 메모리(memory)와 계획(planning) 강화 필요.

- **소형 모델의 근본적 한계**: 8B, 32B 규모 모델은 도구 파라미터 추출 자체에 실패. 사전 학습 데이터 또는 아키텍처 수준의 개선 필요.

- **프롬프트 엔지니어링 의존성**: 성능이 프롬프트 설계에 크게 의존하므로, 상이한 도메인 문제에 대한 일반화 가능성 검증 필요.

- **상용 모델 접근성**: GPT, GLM 등 최고 성능 모델의 로컬 배포 불가로 인한 실용적 제약. 오픈소스 모델의 성능 격차 지속.

- **후속 연구**:
  - 100B 규모 오픈소스 모델(예: LLama3 400B)의 성능 평가
  - 도메인 특화 미세 조정 데이터셋 구축 및 적용
  - 트리 탐색(tree search) 등 고급 에이전트 추론 전략 도입
  - 불확실성 정량화 및 신뢰도 평가 프레임워크 개발
  - 다른 에너지 공학 문제(연소 불안정성, 구조 최적화 등)로 확장 검증

## Evaluation

- **Novelty**: 4/5 — 도메인 특화 ReAct 구조와 이중 에이전트 설계는 참신하나, 개별 기술 요소는 기존 방법의 조합.

- **Technical Soundness**: 4/5 — 열역학 도구 구현과 실험 설계는 견고하나, 근사 및 단순화에 대한 영향 분석 부재. 통계적 유의성 검정 없음.

- **Significance**: 3/5 — 에너지 공학 분야에서의 LLM 응용 가능성을 보여주나, 현 시점에서 실무 적용 가능성은 제한적. 파라미터 규모에 따른 임계값(~100B) 제시는 실용적 가치.

- **Clarity**: 4/5 — 방법론과 결과 서술이 명확하나, 결과 섹션이 15,000자 이전에 끝나 전체 평가 내용 파악 어려움. 성능 정량화(정확도, F1 스코어 등) 부재.

- **Overall**: 3.75/5 — 좋음(Good)

**총평**: 본 논문은 LLM을 물리 기반 도메인 문제에 체계적으로 적용한 의미 있는 사례 연구로, 도메인 특화 프레임워크의 설계와 모델 규모별 성능 평가에 기여한다. 다만 현재는 정성적 관찰 중심이며, 통계적 검증과 실제 산업 데이터를 통한 검증이 추가되면 영향력을 크게 확대할 수 있을 것으로 판단된다.

## Related Papers

- 🧪 응용 사례: [[papers/835_Towards_Scientific_Intelligence_A_Survey_of_LLM-based_Scient/review]] — 에너지 공학의 도메인 특화 ReAct 프레임워크가 Scientific Agent 서베이에서 제시하는 도메인 전문성 통합 방법론의 실제 구현 사례이다.
- 🔄 다른 접근: [[papers/191_Causal_learning_for_socially_responsible_ai/review]] — 물리학 통합 모델링과 사회적 책임 AI 인과학습이 모두 복잡한 시스템의 인과관계를 다루지만 물리적 vs 사회적 도메인으로 구분된다.
- 🔄 다른 접근: [[papers/748_Semi-Supervised_2D_Human_Pose_Estimation_Driven_by_Position/review]] — 물리학 통합 모델링과 컴퓨터 비전 포즈 추정이 모두 도메인 특화 과학적 추론이지만 서로 다른 과학 영역에 특화되어 있다.
- 🏛 기반 연구: [[papers/820_Toward_Reliable_Scientific_Hypothesis_Generation_Evaluating/review]] — 물리학 도메인의 정확한 모델링 요구사항이 과학 가설 생성에서 진실성과 검증 가능성의 중요성을 보여주는 기반 사례이다.
- 🔗 후속 연구: [[papers/631_Predicting_field_experiments_with_large_language_models/review]] — 경제학에서의 실험 예측 방법론을 물리학 통합 모델링에 적용하여 도메인 간 방법론 전이 가능성을 탐구할 수 있다.
- 🔄 다른 접근: [[papers/748_Semi-Supervised_2D_Human_Pose_Estimation_Driven_by_Position/review]] — 컴퓨터 비전 영역의 도메인 특화 추론과 물리학 통합 모델링이 모두 특정 과학 도메인에서의 LLM 활용이지만 접근 방식이 다르다.
- 🧪 응용 사례: [[papers/835_Towards_Scientific_Intelligence_A_Survey_of_LLM-based_Scient/review]] — Scientific Agent의 도메인 특화 지식 통합 방법론이 물리학 통합 모델링의 ReAct 프레임워크에서 실제 적용 사례로 구현된다.
- 🔄 다른 접근: [[papers/191_Causal_learning_for_socially_responsible_ai/review]] — 사회적 책임 AI를 위한 인과학습과 물리학 통합 모델링이 모두 복잡한 인과관계를 다루지만 사회적 vs 물리적 시스템으로 구분된다.
- 🔗 후속 연구: [[papers/911_Resummation_of_the_C-Parameter_Sudakov_Shoulder_Using_Effect/review]] — 물리학 통합 반복 모델링 접근법을 입자물리학의 복잡한 재합 계산으로 확장하여 더 정밀한 예측을 가능하게 한다.
