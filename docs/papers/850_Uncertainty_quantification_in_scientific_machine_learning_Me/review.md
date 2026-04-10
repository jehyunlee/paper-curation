---
title: "850_Uncertainty_quantification_in_scientific_machine_learning_Me"
authors:
  - "Apostolos F. Psaros"
  - "Xuhui Meng"
  - "Zongren Zou"
  - "Ling Guo"
  - "George Em Karniadakis"
date: "2023.03"
doi: "10.1016/j.jcp.2022.111902"
arxiv: ""
score: 4.25
essence: "신경망(Neural Networks, NN) 기반의 과학 기계학습(Scientific Machine Learning, SciML)에서 예측 불확실성을 체계적으로 정량화하는 포괄적 프레임워크를 제시하고, 다양한 UQ 방법들을 함수 근사, 편미분방정식 풀이, 연산자 학습 문제에서 비교 평가한다. 특히 물리정보신경망(Physics-Informed Neural Network, PINN)과 심층연산자망(DeepONet)을 중심으로 불확실성 모델링, 정량화 방법, 평가 지표를 통합적으로 다룬다."
tags:
  - "cat/AI-Powered_Scientific_Research_Frameworks"
  - "sub/Physics-informed_Neural_Networks"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Psaros et al._2023_Uncertainty quantification in scientific machine learning Methods, metrics, and comparisons.pdf"
---

# Uncertainty quantification in scientific machine learning: Methods, metrics, and comparisons

> **저자**: Apostolos F. Psaros, Xuhui Meng, Zongren Zou, Ling Guo, George Em Karniadakis | **날짜**: 03/2023 | **DOI**: [10.1016/j.jcp.2022.111902](https://doi.org/10.1016/j.jcp.2022.111902)

---

## Essence

신경망(Neural Networks, NN) 기반의 과학 기계학습(Scientific Machine Learning, SciML)에서 예측 불확실성을 체계적으로 정량화하는 포괄적 프레임워크를 제시하고, 다양한 UQ 방법들을 함수 근사, 편미분방정식 풀이, 연산자 학습 문제에서 비교 평가한다. 특히 물리정보신경망(Physics-Informed Neural Network, PINN)과 심층연산자망(DeepONet)을 중심으로 불확실성 모델링, 정량화 방법, 평가 지표를 통합적으로 다룬다.

## Motivation

- **Known**: 신경망은 노이즈 데이터와 물리 법칙을 결합하여 역문제(inverse problems)와 부정형 문제(ill-posed problems)를 효과적으로 해결할 수 있으며, 전통적 방법의 한계를 극복할 수 있다.

- **Gap**: NN 기반 추론의 오차와 불확실성 정량화는 데이터 노이즈(aleatoric uncertainty) 외에도 제한된 데이터, 하이퍼파라미터, 과다 매개변수화(overparametrization), 최적화 오류, 표본 추출 오류, 모형 오명시(model misspecification)에 기인한 불확실성까지 고려해야 하므로 전통 방법보다 훨씬 복잡하다. 특히 함수 근사를 넘어 편미분방정식 풀이와 무한차원 함수공간 간 연산자 매핑 학습에서의 체계적 UQ 방법이 부재하다.

- **Why**: 물리 및 생물 시스템을 다루는 임계적 응용에서 신경망의 신뢰성 있는 사용을 위해서는 불확실성 정량화가 필수적이다. 또한 SciML은 미지의 또는 불확실한 항과 매개변수를 포함한 미분방정식을 다루므로 UQ는 더욱 중요하다.

- **Approach**: (1) 다양한 문제 클래스와 해결 방법 요약 (2) 심층 학습 기반 불확실성 모델링 절차 (3) 선택된 UQ 방법의 검토 및 SciML 통합 (4) 불확실성 평가 지표 및 사후 개선 방법 제시 (5) 광범위한 비교 연구 수행

## Achievement

![Figure 2: 데이터 노이즈, 제한된 데이터, 모형 오명시 등으로부터의 전체 불확실성 분해](figures/fig2.webp)
*그림 2: 데이터(노이즈, 갭), 물리 모형, 신경망으로부터의 불확실성 기여도 정성적 분석*

1. **포괄적 UQ 프레임워크 제시**: 함수 근사, PINN 기반 PDE 풀이, DeepONet 기반 연산자 학습에서의 통일된 불확실성 모델링 및 정량화 방법론 개발. 총 불확실성을 인식론적 불확실성(epistemic uncertainty)과 우연적 불확실성(aleatoric uncertainty)으로 분해.

2. **다양한 UQ 방법론 통합**: Bayesian 방법(Variational Inference, MCMC, Laplace approximation), 앙상블(ensemble) 방법, 함수 사전분포(Functional Priors, FP), 확률미분방정식(Stochastic PDE, SPDE) 해석 방법을 체계적으로 비교 평가. 각 방법의 계산 비용(computational cost)과 성능을 정량화.

3. **평가 지표 및 보정 방법 개발**: 예측 불확실성의 품질을 평가하기 위한 지표(coverage probability, negative log-likelihood, prediction interval coverage probability, calibration) 및 사후 보정(post-hoc calibration) 기법 제시. 분포 시프트 감지 능력 평가.

4. **광범위한 실증 비교 연구**: 불연속 함수 근사, 혼합 결정론적 PDE(비선형 시간-의존 확산-반응 방정식), 혼합 확률적 타원 방정식, 2D 다공질 매질 유동 연산자 학습 등 5개 프로토타입 문제에서 모든 방법 검증.

5. **오픈소스 라이브러리 개발**: NeuralUQ 파이썬 라이브러리(github.com/Crunch-UQ4MI/neuraluq) 제공으로 재현성과 접근성 확보. 교육용 튜토리얼 및 추가 계산 실험 포함.

## How

![Figure 4: 입력 함수 λ(x; ξ)와 대응되는 출력 u_θ(x; ξ)를 가진 DeepONet 구조](figures/fig4.webp)
*그림 4: DeepONet 아키텍처로 분기 네트워크(branch net)가 함수 입력을 인코딩하고 트렁크 네트워크(trunk net)가 공간 위치를 처리*

- **불확실성 모델링**: 
  - 예측 분포 $\bar{p}(u|x)$를 통해 인식론적(모형 및 데이터 부족) 및 우연적(측정 노이즈) 불확실성을 동시 모델링
  - 변분 추론(Variational Inference, VI)으로 가중치 분포 근사
  - Laplace 근사를 통한 사후분포(posterior) 국소 근사

- **Bayesian 방법**:
  - Variational Inference: 가중치 분포를 학습 가능한 근사분포로 표현
  - MCMC: 사후분포로부터 정확한 샘플링 (계산 비용 높음)
  - Laplace 근사: 최적 가중치 주변의 Hessian을 이용한 2차 근사

- **앙상블 방법**:
  - 다중 독립 학습 또는 최적화 이력 활용으로 가중치 분포 추정
  - 계산 효율성과 구현 단순성의 우수한 균형

- **함수 사전분포(FP)**:
  - 신경망 출력에 직접 Gaussian Process 사전분포 부과
  - 물리 제약(boundary conditions 등) 자연스럽게 통합 가능

- **확률미분방정식(SPDE) 풀이**:
  - 매개변수 불확실성이 있는 PDE를 직접 확률론적으로 해석
  - 몬테카를로 샘플링으로 해 분포 추정

- **불확실성 평가 지표**:
  - Coverage Probability: 예측 구간이 참 값을 포함하는 비율
  - Negative Log-Likelihood (NLL): 확률론적 예측 정확도
  - Prediction Interval Coverage Probability (PICP): 지정된 신뢰도 달성도
  - Calibration curve: 예측 확률과 경험 주파수 일치도

- **사후 보정(Calibration)**:
  - 온도(temperature) 재조정으로 불확실성 대역폭 조율
  - Platt scaling, isotonic regression 등 보정 방법 적용

## Originality

- **SciML 분야의 첫 체계적 UQ 통합**: PINN, DeepONet과 같은 주요 SciML 방법론에 대한 최초의 포괄적 UQ 프레임워크. 함수 근사를 넘어 PDE 풀이와 연산자 학습까지 확장.

- **총 불확실성 분해 체계화**: 데이터 노이즈, 제한된 데이터, 하이퍼파라미터, 최적화 오류, 모형 오명시 등 다양한 불확실성 원천을 명시적으로 식별하고 모델링 (그림 2).

- **다양한 이종 방법론의 통일적 비교**: Bayesian 방법, 앙상블, 함수 사전분포, SPDE 등 개념적으로 상이한 접근법들을 동일 평가 지표로 체계적 비교. 방법 간 등가성과 차이점 규명.

- **새로운 평가 지표 개발**: 표준 신경망 검증 데이터 기반 평가가 불가능한 UQ 상황을 위해 coverage probability, PICP 등 맞춤형 평가 지표 제시.

- **분포 시프트 감지 능력 평가**: 분포 외(out-of-distribution) 입력에 대한 UQ 모델의 "무지 인정(ignorance admission)" 능력 평가 - SciML의 안전한 배포에 필수.

- **재현성 및 실용성 확보**: 오픈소스 NeuralUQ 라이브러리 제공으로 장벽 없는 접근성 확보. 비교 연구에 사용된 모든 코드 공개.

## Limitation & Further Study

- **희귀 사건(rare events) 미처리**: 논문에서 명시적으로 희귀 사건 시나리오는 다루지 않음. 극단 사건의 확률이 매우 낮은 상황에서 UQ의 신뢰성 검증 필요.

- **능동 학습(active learning) 미포함**: 측정 위치 최적화를 통한 정보 획득 최적화 문제 미해결. SciML에서 측정 비용이 높은 경우 중요한 미래 과제.

- **결합 예측(joint predictions) 미흡**: 대부분의 방법이 단일 입력에 대한 한계분포(marginal distribution)만 예측하며, 도메인의 인접 점들 간 상관성을 무시. 공간 상관구조 포함 예측 필요.

- **하이퍼파라미터 튜닝의 계산 비효율**: UQ 맥락에서 사전분포, 정규화 상수, 신경망 아키텍처 등 하이퍼파라미터 선택 및 튜닝이 여전히 어렵고 비효율적. 자동 선택 방법 개발 필요.

- **과다 매개변수화로 인한 다중 모달성**: NN 과다 매개변수화가 사후분포의 극심한 다중 모달성(multimodality)을 야기. 이러한 분포로부터의 효율적 샘플링은 미해결 문제.

- **측정 노이즈 분포 미지**: 이분산(heteroscedastic) 노이즈 분포가 미지인 경우 신뢰성 있는 불확실성 추정 어려움. 노이즈 학습 방법 필요.

- **이론적 정당성 부족**: 일부 방법(예: ensemble, FP)에 대한 확률론적 정당화 부족. 수렴 보장 및 일관성 증명 필요.


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4/5
- Significance: 4.5/5
- Clarity: 4/5
- Overall: 4.25/5

**총평**: 본 논문은 과

## Related Papers

- 🏛 기반 연구: [[papers/619_Physics_Informed_Deep_Learning_Part_I_Data-driven_Solutions/review]] — 물리 정보 딥러닝의 데이터 기반 솔루션이 과학 기계학습에서 불확실성 정량화의 이론적 토대를 제공한다
- 🔗 후속 연구: [[papers/037_A_Survey_on_Uncertainty_Quantification_Methods_for_Deep_Lear/review]] — 딥러닝에서 불확실성 정량화 조사를 과학 기계학습 특화 방법론으로 확장할 수 있다
- 🧪 응용 사례: [[papers/527_Mechanistic_interpretability_for_ai_safetya_review/review]] — AI 안전성을 위한 기계적 해석가능성을 과학 기계학습의 불확실성 정량화에 적용할 수 있다
- 🏛 기반 연구: [[papers/037_A_Survey_on_Uncertainty_Quantification_Methods_for_Deep_Lear/review]] — 과학적 머신러닝에서 불확실성 정량화의 광범위한 맥락과 이론적 토대를 제공합니다.
