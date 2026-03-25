# Modeling Changing Scientific Concepts with Complex Networks: A Case Study on the Chemical Revolution

> **저자**: Sofía Aguilar-Valdez, Stefania Degaetano-Ortlieb | **날짜**: 2026 | **DOI**: 10.48550/ARXIV.2603.17594

---

## 핵심 요약
본 연구는 LLM의 context embedding이 가진 해석 불가능성과 시간 비인식 문제를 극복하기 위해, 토픽 기반 복잡 네트워크(complex networks)를 통해 과학적 개념의 변화를 모델링하는 프레임워크를 개발한다. Royal Society Corpus를 활용하여 화학 혁명 시기의 phlogiston(플로지스톤)과 oxygen(산소) 이론 경쟁을 사례 연구로 분석하며, 명명적(onomasiological) 변화가 높은 엔트로피와 위상적 밀도와 연관됨을 보인다.

## 연구 배경 및 동기
언어 변화, 특히 과학적 개념의 변화를 모델링하기 위해 LLM 기반 word embedding이 활용되고 있으나, 이러한 표현은 해석이 어렵고 시간을 인식하지 못하며 역사적 데이터의 편향을 증폭시킬 위험이 있다. 과학 혁명에서의 개념 전환을 추적하려면, 개념의 중심 및 주변 의미(readings)의 경쟁과 대체를 해석 가능한 방식으로 모델링할 필요가 있다.

## 방법론
- **데이터**: Royal Society Corpus — 1665-1869년 Philosophical Transactions 논문 모음, 1750-1800년대에 집중
- **이론적 프레임워크**: Prototype semantics — 개념을 중심(core)과 주변(periphery) 의미로 구성된 구조로 모델링
- **네트워크 구성**: 토픽 기반 co-occurrence 네트워크에서 개념의 의미(readings)를 노드로, 공출현을 엣지로 표현
- **분석 지표**: Shannon 엔트로피(의미 다양성), 위상적 밀도(topological density, 연결 노력), 중심성(centrality) 변화 추적
- **사례**: phlogiston vs. oxygen 이론의 개념 네트워크 시간적 변화 비교

## 주요 결과
- 명명적 변화(onomasiological change)가 높은 엔트로피 및 위상적 밀도와 연관됨 — 아이디어 다양성과 연결 노력 증가를 시사
- Oxygen 개념이 확립되면서 네트워크 구조가 더 밀집되고 다양해짐
- Phlogiston 관련 용어(calx 등)가 주변부로 이동하고 결국 소멸
- Air가 핵심에서 주변으로 이동하고, acid가 주변에서 핵심으로 이동하는 패턴 관찰
- 과학 혁명이 네트워크의 구조적 재구성으로 가시화 가능

## 독창성 및 기여
LLM embedding의 한계를 극복하기 위해 prototype semantics와 complex network를 결합한 해석 가능한(interpretable) 개념 변화 모델링 프레임워크를 제안한 점이 독창적이다. 과학사와 전산언어학을 연결하는 학제간 접근이 특징적이다.

## 한계 및 향후 연구
- 단일 사례 연구(화학 혁명)에 기반하여 일반화에 제한
- Royal Society Corpus라는 제한된 코퍼스 사용
- 토픽 모델링의 품질이 결과에 영향을 줄 수 있으나 체계적 민감도 분석 부재
- 다른 과학 혁명(예: 양자역학, 판구조론)으로의 확장 필요
- 정량적 평가 기준(ground truth)의 부재로 검증이 주로 질적

## 평가
| 항목 | 점수 |
|------|------|
| Novelty | 4/5 |
| Technical Soundness | 3/5 |
| Significance | 3/5 |
| Clarity | 4/5 |
| Overall | 3/5 |

**총평**: 과학적 개념 변화를 해석 가능한 네트워크로 모델링하는 흥미로운 학제간 연구로, 방법론적 아이디어는 참신하지만 단일 사례 연구의 한계로 프레임워크의 일반적 적용 가능성에 대한 추가 검증이 필요하다.
