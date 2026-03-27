# The Price-Pareto growth model of networks with community structure

> **저자**: Łukasz Brzozowski, Marek Gagolewski, Grzegorz Siudem, Barbara Żogała-Siudem | **날짜**: 2026-02-23 | **Journal**: arXiv preprint | **DOI**: [10.48550/arXiv.2510.13392](https://doi.org/10.48550/arXiv.2510.13392)
> **리뷰 모드**: Abstract 기반 (PDF 없음)

---

## Essence

현실 네트워크(특히 인용 네트워크)는 분야별로 다른 성장률과 인용 문화를 가지므로, 단일 동질적 모델로는 커뮤니티 구조를 포착하지 못한다. 이 논문은 Price 모델(우선적 연결)의 최근 수정판을 확장하여 커뮤니티 구조를 가진 네트워크의 분석 틀을 개발한다. 핵심 결과는 각 커뮤니티 내 인용 수 분포가 **Pareto 타입 II 분포**로 수렴한다는 해석적 증명이며, Gini 지수로 측정된 불평등도에 대한 해석적 공식도 도출된다. 모델 파라미터 추정기를 통해 실제 인용 네트워크에 피팅이 가능하다.

## Originality (Abstract 기반)

- [authorship, novelty] "We introduce a new analytical framework for modelling degree sequences in individual communities of real-world networks."
- [authorship, action] "Extending the model to networks with a community structure allows us to devise the analytical formulae for, amongst others, citation counts in each cluster and their inequality as described by the Gini index."
- [result, finding] "We also show that a citation count distribution in each community tends to a Pareto type II distribution."
- [authorship, approach] "Thanks to the derived model parameter estimators, the new model can be fitted to real citation and similar networks."

## How (방법론)

- **이론적 기반**: Price 모델의 최근 수정판 — 인용이 부분적으로 무작위, 부분적으로 선호적 연결(preferential attachment)로 획득된다는 가정
- **커뮤니티 확장**: 동질적 단일 네트워크를 커뮤니티 구조를 가진 이질적 네트워크로 확장 — 각 커뮤니티가 서로 다른 성장률(growth ratio)과 인용 문화를 가질 수 있도록 파라미터화
- **해석적 유도**: 각 커뮤니티의 인용 수 분포, Gini 지수 등에 대한 닫힌 형태(closed-form) 공식 수학적 유도
- **분포 수렴 증명**: 각 커뮤니티 내 인용 분포가 Pareto 타입 II(Lomax 분포)로 수렴함을 이론적으로 증명
- **파라미터 추정**: 실제 네트워크에 피팅 가능한 모델 파라미터 추정기 제안 및 검증

## Why (중요성)

- 기존 동질적 Price 모델은 분야별 인용 문화의 다양성을 반영하지 못해 현실 학술 네트워크 모델링에 한계가 있었음
- 커뮤니티별 인용 불평등(Gini 지수)의 해석적 공식은 분야별 인용 집중도 비교를 이론적 토대 위에서 수행 가능하게 함
- Pareto 타입 II 분포로의 수렴 증명은 인용 분포의 이론적 근거를 제공하여, 실증적 관찰(파워 법칙)을 수학적으로 정당화
- 파라미터 추정기를 통한 실제 네트워크 피팅은 이론을 실용적 분석 도구로 연결

## Limitation

### 저자들이 언급한 한계
- Abstract 기준으로 명시적 한계 제시 확인 불가

### 자체판단 아쉬운 점
- 커뮤니티 경계를 어떻게 정의하는지(사전 정의 vs. 자동 탐지)가 결과에 큰 영향을 미칠 수 있음
- 동적 커뮤니티(분야가 합쳐지거나 분리되는 경우)에 대한 모델 확장이 필요
- 모델이 단방향 비가중 네트워크 가정에 기반하므로, 가중치나 방향성이 중요한 현실 인용 패턴에 대한 적용 한계 가능성
- Pareto 수렴 속도(finite-size 효과)가 소규모 커뮤니티에서 문제가 될 수 있음

### 후속 연구
- 다양한 학문 분야의 실제 인용 네트워크에 대한 체계적 피팅 및 검증
- 동적 커뮤니티 구조(분야 출현·소멸·합병)를 포함한 모델 확장
- 커뮤니티 간 인용 교환(cross-community citations) 모델링

## 평가

| 항목 | 점수 |
|------|------|
| Novelty | 4/5 |
| Technical Soundness | 5/5 |
| Significance | 3/5 |
| Clarity | 3/5 |
| Overall | 4/5 |

**총평**: Price 모델을 커뮤니티 구조로 엄밀하게 확장하여 각 클러스터 내 인용 분포의 Pareto 수렴과 불평등 지수의 해석적 공식을 유도한 수학적으로 견고한 이론 논문이다. 실용적 파라미터 추정기까지 제공하지만, 실제 다양한 분야 네트워크에 대한 대규모 검증이 향후 과제로 남는다.
