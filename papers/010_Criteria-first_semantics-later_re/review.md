# Criteria-first, semantics-later: reproducible structure discovery in image-based sciences

> **저자**: Jan Bumberger | **날짜**: 2026-02-17 | **arXiv**: 2602.15712 | **분야**: cs.CV

---

## Essence

이미지 기반 과학 분석에서 지배적인 "semantics-first" 패러다임(측정 데이터를 도메인 특화 라벨/온톨로지에 직접 매핑)의 근본적 한계를 지적하고, "criteria-first, semantics-later"라는 연역적 전환을 제안하는 개념 논문이다. 명시적 최적화 기준(robustness, scale coherence, compressibility, global consistency)으로 의미론과 무관한 구조적 산출물(structural product)을 먼저 추출하고, 도메인 온톨로지로의 의미 매핑은 하류에서 별도로 수행함으로써 재현성, 도메인 전이, 장기 모니터링을 가능하게 하는 통합 프레임워크를 제시한다.

## Motivation

- **알려진 것**: 자연과학/생명과학에서 이미지가 핵심 측정 양식으로 자리잡았으며, supervised/weakly-supervised 파이프라인이 도메인 온톨로지 기반 라벨링으로 높은 정확도를 달성
- **Gap**: Semantics-first 접근법은 (i) 온톨로지가 시간/기관/문화에 따라 drift하는 장기 모니터링, (ii) 센서/조명/계절 변화에 의한 domain shift, (iii) 기존 라벨 공간에 없는 새로운 현상의 open-ended discovery에서 체계적으로 실패 -- 의미(semantics)는 이미지의 내재적 속성이 아니라 커뮤니티의 해석 체계에 속하는 것
- **왜 중요한가**: Digital twin, FAIR 데이터 원칙, 장기 환경 모니터링 등에서 해석 체계가 진화하더라도 안정적으로 비교 가능한 분석 기반 레이어가 필수적
- **접근법**: Cybernetics, observation-as-distinction, Shannon 정보이론의 information/meaning 분리에 근거하여, 구조 추출을 의미 부여와 분리하는 2층 아키텍처를 연역적으로 도출

## Achievement

1. **통합 프레임워크 정립**: 측정 필드 X, 명시적 기준 C, 기준 매개변수화 구조추출 연산자 S_C, 구조적 산출물 S = S_C(X), 하류 의미 매핑 M_i: S -> O_i로 구성되는 도메인 일반적(domain-general) 수학적 프레임워크 제시
2. **4가지 재현성 공준(postulate)**: Explicitness(기준의 완전한 명세), Determinacy(결정론적 산출물), Stability(선언된 perturbation 하 안정성), Mapping pluralism(동일 S에 대한 복수 의미 매핑 공존) 정의
3. **8개 도메인 cross-domain evidence**: Earth observation, medical imaging, microscopy/bioimaging, seismology, astronomy, materials science, point clouds/3D sensing, robotics에서 criteria-first 패턴이 라벨이 부족/불안정할 때 반복적으로 출현함을 체계적으로 문서화
4. **5가지 구조적 검증 기준 제안**: Robustness, scale coherence, complexity control, global optimality, downstream pluralism -- class accuracy를 넘어서는 검증 체계
5. **FAIR Digital Object로서의 structural product**: 버전 관리, 메타데이터, provenance를 갖춘 machine-actionable 디지털 객체로 구조적 산출물을 취급하는 방안과 digital twin 상태 변수로의 활용 제안

## How

- **인식론적 기반**: Wiener(cybernetics), Spencer-Brown(observation-as-distinction), Maturana(autopoiesis), Shannon(정보/의미 분리)의 전통에서 "관찰은 구별 짓기(drawing distinctions)" 연산이며, 의미는 커뮤니티에 종속된 해석 체계라는 점을 논증
- **수학적 프레임워크**: X: Omega -> R^k (측정 필드), C (명시적 기준 -- functional, 제약 조건, 또는 에너지 E_C), S_C(X) (구조적 산출물), 다양한 구조 공간(partition P(Omega), graph G, hierarchy H, field F) 지원, 에너지 최소화 S_hat = argmin E_C(X, S) 형태로 일반화
- **Multiscale 표현**: 파티션 체인 Pi^(0) <= Pi^(1) <= ... <= Pi^(m)으로 다중 스케일 구조를 기준 정의 집약(aggregation)으로 표현
- **Cross-domain survey**: 각 도메인별 carrier set Omega, operator/solver 유형, structural product 유형, 전형적 criteria family C를 Table 1로 체계적 정리 (EO: spectral homogeneity/scale coherence, medical: data fidelity+smoothness/boundary evidence, 등)
- **FAIR-by-design 메타데이터**: DO = (S, metadata, provenance, version) 구조로 기준 C, 구현 식별자(소프트웨어 버전+hash), perturbation family, 안정성 envelope 등을 포함하는 최소 보고 요건 제안

## Originality

- **패러다임 전환의 연역적 논증**: 기존의 "라벨 먼저" 접근을 단순히 비판하는 것이 아니라, cybernetics/정보이론/과학철학에 근거하여 "구조가 의미에 선행해야 한다"는 원리를 연역적으로 도출한 점이 핵심 기여
- **도메인 횡단적 통합**: 8개 이질적 과학 분야에서 criteria-first 패턴이 독립적으로 출현하는 현상을 하나의 프레임워크로 통합 -- 개별 도메인 내에서는 이미 실천되고 있으나 명시적으로 이론화한 것은 최초
- **Structural product를 FAIR Digital Object로 격상**: 중간 산출물을 일시적 부산물이 아닌 버전 관리되는 1급 연구 산출물로 취급하자는 제안은 연구 데이터 인프라 차원에서 참신
- **Marr의 early vision least-commitment 원리를 현대 foundation model 맥락에서 재해석**: SAM, DINOv2 등을 "pre-semantic structural extractor"로 읽을 수 있다는 관점 제시

## Limitation & Further Study

### 저자들이 언급한 한계

- 순수 개념적/이론적 논문으로 경험적 실험 검증이 없음 -- 구체적 criteria-first 파이프라인의 정량적 비교 실험이 제공되지 않음
- SSL/foundation model이 자동으로 semantics-free 구조를 제공하는 것은 아니며, 학습 과정의 implicit criteria를 명시화하는 작업이 추가로 필요
- Community-maintained schema와 conformance check 등 인프라적 요구사항이 아직 미구현

### 자체판단 아쉬운 점

- 8개 도메인에 걸친 cross-domain evidence가 서술적(narrative)이어서, criteria-first가 semantics-first 대비 실제로 어떤 정량적 이점(robustness, transfer 성능 등)을 제공하는지 수치적 근거가 전무함 -- 주장의 설득력이 사례 나열에 의존
- "Semantics-free"의 경계가 모호함: foundation model의 feature space(DINOv2 등)는 대규모 자연 이미지에서 학습된 implicit semantic bias를 내포하고 있어, 진정한 criteria-only extraction이 가능한지에 대한 비판적 검토가 부족
- 단일 저자 논문으로, 8개 도메인을 모두 깊이 있게 다루기에는 한계가 있으며, 각 도메인 전문가의 검증이 필요한 부분들이 존재
- Digital twin과 FAIR 연계 논의가 추상적 수준에 머물러, 구체적 구현 사례나 프로토타입이 없음
- Scale-space, variational method, graph-cut 등 고전적 방법론을 criteria-first로 재해석하지만, deep learning 시대에 이들 방법론의 실제 경쟁력에 대한 현실적 평가가 부재

### 후속 연구

- 구체적 도메인(예: 장기 원격 탐사 모니터링)에서 criteria-first vs semantics-first 파이프라인의 정량적 비교 실험 수행
- Foundation model(SAM, DINOv2)의 feature space에서 criteria-first structural product를 추출하는 구체적 알고리즘 개발 및 stability/robustness 벤치마크 구축
- Structural product의 FAIR Digital Object 스키마 표준화 및 커뮤니티 채택 경로 설계
- Criteria 선택 자체의 자동화/meta-learning -- 어떤 기준 C가 특정 modality에 최적인지 학습
- Ontology drift 하에서의 장기 비교 가능성을 실증하는 종단(longitudinal) 연구

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 4/5 |
| Technical Soundness | 3/5 |
| Significance | 4/5 |
| Clarity | 4/5 |
| Overall | 3/5 |

**총평**: Image-based science에서 "구조 추출을 의미 부여와 분리해야 한다"는 원칙을 cybernetics와 정보이론에 근거하여 체계적으로 논증한 시의적절한 개념 논문이다. 8개 도메인에 걸친 cross-domain evidence와 FAIR Digital Object로의 연결은 인상적이나, 순수 이론적 논문으로서 경험적 검증의 부재가 가장 큰 한계이다. AI4Science 관점에서 foundation model 시대에 "어디에 이론을 넣을 것인가"라는 근본적 질문을 제기한 점에서 가치가 있으며, 향후 구체적 실험과 도구 구현이 뒷받침된다면 영향력이 클 수 있는 프레임워크이다.
