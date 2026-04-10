---
title: "748_Semi-Supervised_2D_Human_Pose_Estimation_Driven_by_Position"
authors:
  - "Linzhi Huang"
  - "Yulong Li"
  - "Hongbo Tian"
  - "Yue Yang"
  - "Xiangang Li"
date: "2023.03"
doi: "미제공"
arxiv: ""
score: 4.0
essence: "반인체 포즈 추정을 위한 준지도학습(semi-supervised learning)에서 **위치 불일치 기반 의사 레이블 수정 모듈(SSPCM)**을 제안하여, 노이즈 의사 레이블을 효과적으로 제거하고 SOTA 성능을 달성한 연구이다."
tags:
  - "cat/LLM-Based_Scientific_Reasoning"
  - "sub/Domain-specific_Scientific_Reasoning"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Huang et al._2023_Semi-Supervised 2D Human Pose Estimation Driven by Position Inconsistency Pseudo Label Correction Mo.pdf"
---

# Semi-Supervised 2D Human Pose Estimation Driven by Position Inconsistency Pseudo Label Correction Module

> **저자**: Linzhi Huang, Yulong Li, Hongbo Tian, Yue Yang, Xiangang Li, Weihong Deng, Jieping Ye | **날짜**: 2023-03-08 | **DOI**: [미제공](https://doi.org/)

---

## Essence

![Figure 2](figures/fig2.webp)
*그림 2: 위치 불일치(Position Inconsistency) 개념 설명. 신뢰도(confidence)가 낮아도 위치 일관성이 높은 고품질 의사 레이블이 존재함을 보여줌*

반인체 포즈 추정을 위한 준지도학습(semi-supervised learning)에서 **위치 불일치 기반 의사 레이블 수정 모듈(SSPCM)**을 제안하여, 노이즈 의사 레이블을 효과적으로 제거하고 SOTA 성능을 달성한 연구이다.

## Motivation

- **Known**: 기존 방법(DUAL 등)은 신뢰도(confidence)를 기준으로 의사 레이블 필터링을 수행하며, 일관성 기반 준지도학습으로 우수한 성능을 보임

- **Gap**: 
  1. 대형 모델(teacher)과 경량 모델(student) 구조가 다를 때 상호 학습에서 경량 모델의 저품질 의사 레이블이 대형 모델을 훈련하는 문제
  2. 신뢰도만으로는 의사 레이블 품질을 판단 불가 - 신뢰도가 낮아도 위치 정확도는 높은 경우 다수 존재
  3. 노이즈 의사 레이블의 학습에 미치는 부정적 영향 미흡

- **Why**: 반인체 포즈 추정의 레이블은 키포인트 범주(category)와 위치(position) 두 가지 복잡한 정보 포함. 위치 정확도(localization quality)가 신뢰도와 괴리 발생 가능

- **Approach**: 
  1. 보조 교사 모델 추가 도입
  2. 두 교사 모델의 서로 다른 시점의 예측 결과 간 위치 불일치 점수(position inconsistency score) 계산
  3. 위치 불일치 기반 의사 레이블 보정 및 아웃라이어 제거

## Achievement

![Figure 1](figures/fig1.webp)
*그림 1: COCO 데이터셋에서 레이블된 인스턴스 수에 따른 성능 비교. 모든 설정에서 기존 SOTA 대비 우수한 성능*

1. **성능 향상**: COCO 데이터셋에서
   - 1,000개 레이블: +2.3 mAP (46.9% → 49.2%)
   - 5,000개 레이블: +1.9 mAP (51.1% → 53.0%)
   - 10,000개 레이블: +1.1 mAP (56.6% → 57.7%)

2. **신규 데이터셋**: 실내 오버헤드 어안카메라(fisheye) 기반 WEPDTOF-Pose 데이터셋 공개

3. **다중 벤치마크 검증**: MPII, COCO, AI-Challenger에서 일관된 성능 우수성 입증

## How

![Figure 3](figures/fig3.webp)
*그림 3: SSPCM의 전체 훈련 파이프라인. 4단계 상호 학습(interactive training) 구조*

### 핵심 방법론

**1. 위치 불일치 의사 레이블 수정 모듈(PCM)**
- 두 교사 모델(Network A, B)의 N개 시점 예측 결과 수집
- 각 키포인트의 N개 예측 위치 간 픽셀 거리(pixel distance) 계산
  ```
  Position Inconsistency Score = min distance among N predictions
  ```
- 불일치 점수가 가장 작은 2개 의사 레이블 선택 후 앙상블(ensemble)
- 신뢰도 필터링 기반 아웃라이어 제거보다 우수한 품질 보정

**2. 반지도학습 Cut-Occlude (SSCO)**
- 교사 모델의 의사 레이블로 각 키포인트 위치 파악
- 해당 위치 근처의 사지(limb) 로컬 이미지 추출
- 다른 이미지의 키포인트 중심에 랜덤하게 붙여넣기 → 국소 폐색(occlusion) 모의
- 모델의 견고성(robustness) 향상

**3. 상호 학습 구조**
- Train Step 1: 레이블 데이터로 3개 네트워크 초기 훈련
- Train Steps 2-4: Network A(teacher) → Network B,C(student), Network B(teacher) → Network A,C(student)로 번갈아 진행
- 각 스텝에서 SSCO 기반 어려운 샘플 생성

## Originality

- **위치 불일치 기반 의사 레이블 필터링**: 신뢰도 중심의 기존 방식에서 벗어나 서로 다른 모델/시점의 예측 일관성으로 품질 판단 - 포즈 추정의 위치 정확도 특성에 부합

- **보조 교사 모델 도입**: 구조가 다른 teacher-student 쌍에서도 상호 학습 가능하도록 설계, 실제 적용성 향상

- **의사 레이블 기반 Cut-Occlude**: 어안카메라 등 특수 환경에서의 폐색 상황 모의, 키포인트 인식 기반 선택적 증강

- **신규 어안카메라 포즈 데이터셋**: WEPDTOF-Pose 공개로 재현성 및 추가 연구 기초 제공

## Limitation & Further Study

- **교사 모델 개수**: 2개 교사 모델 고정 - 추가 교사 도입 시 성능 변화에 대한 분석 부족

- **하이퍼파라미터 민감도**: 위치 불일치 임계값, 앙상블 레이블 개수(N=2) 선택 근거 명확하지 않음

- **계산 비용**: 다중 모델 유지로 인한 메모리/계산량 증가에 대한 분석 미흡

- **후속 연구 방향**:
  1. 적응형 위치 불일치 임계값 자동 선택 메커니즘 개발
  2. 3D 포즈 추정으로 확장
  3. 다양한 카메라 뷰(뒤에서 본 포즈 등)에 대한 일반화 개선
  4. 온라인 학습 환경에서의 적용

## Evaluation

- **Novelty**: 4/5 - 위치 불일치 개념은 신선하나, 기본 프레임워크는 기존 방법 연장선

- **Technical Soundness**: 4/5 - 논리적 타당성 높으나, 하이퍼파라미터 선택 근거 부족

- **Significance**: 4/5 - SOTA 성능 달성 및 실용적 가치 높음, 어안카메라 데이터셋 기여

- **Clarity**: 4/5 - 전반적으로 명확하나 PCM 모듈의 수식 표현 개선 필요

- **Overall**: 4/5

**총평**: 준지도학습 기반 반인체 포즈 추정에서 위치 기반 의사 레이블 수정을 통해 실질적 성능 개선을 달성한 실용적인 연구이다. 특히 이질적인 teacher-student 구조 지원과 어안카메라 데이터셋 공개는 실제 응용 가치를 높이지만, 하이퍼파라미터 설정의 일반화 가능성에 대한 심화 분석이 필요하다.

## Related Papers

- 🧪 응용 사례: [[papers/191_Causal_learning_for_socially_responsible_ai/review]] — 반지도학습 포즈 추정의 편향 제거 기법이 사회적 책임 AI의 인과학습 도구에서 편향 완화 방법론으로 적용될 수 있다.
- 🔄 다른 접근: [[papers/286_Domain-specific_ReAct_for_physics-integrated_iterative_model/review]] — 컴퓨터 비전 영역의 도메인 특화 추론과 물리학 통합 모델링이 모두 특정 과학 도메인에서의 LLM 활용이지만 접근 방식이 다르다.
- 🏛 기반 연구: [[papers/835_Towards_Scientific_Intelligence_A_Survey_of_LLM-based_Scient/review]] — 도메인 특화 과학 추론 사례로서 Scientific Agent 설계에서 특정 영역 전문성 통합 방법론의 실제 구현 예시를 제공한다.
- ⚖️ 반론/비판: [[papers/820_Toward_Reliable_Scientific_Hypothesis_Generation_Evaluating/review]] — 포즈 추정의 정확한 성능 측정과 과학 가설 생성의 진실성 평가 문제를 대조하여 과학적 검증의 도메인별 차이를 보여준다.
- 🔄 다른 접근: [[papers/286_Domain-specific_ReAct_for_physics-integrated_iterative_model/review]] — 물리학 통합 모델링과 컴퓨터 비전 포즈 추정이 모두 도메인 특화 과학적 추론이지만 서로 다른 과학 영역에 특화되어 있다.
- 🧪 응용 사례: [[papers/191_Causal_learning_for_socially_responsible_ai/review]] — 사회적 책임 AI의 편향 완화 방법론이 반지도학습 포즈 추정의 의사 레이블 노이즈 제거 기법과 연결되어 AI 시스템의 공정성을 향상시킬 수 있다.
- 🏛 기반 연구: [[papers/125_Automated_latex_code_generation_from_handwritten_math_expres/review]] — 위치 임베딩 기반의 반지도 학습 방법이 필기 수학식의 공간적 구조 인식에 이론적 기반을 제공한다.
