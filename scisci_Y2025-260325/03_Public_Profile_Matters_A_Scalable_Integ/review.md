# Public Profile Matters: A Scalable Integrated Approach to Recommend Citations in the Wild

> **저자**: Karan Goyal, Dikshant Kukreja, Vikram Goyal, Mukesh Mohania | **날짜**: 2026-03-18 | **DOI**: 10.48550/arXiv.2603.17361

---

## 핵심 요약
본 연구는 local citation recommendation(LCR) 시스템의 성능을 개선하기 위해 Profiler라는 경량 비학습(non-learnable) 모듈과 DAVINCI라는 새로운 reranking 모델을 제안한다. 기존 시스템의 confirmation bias 문제와 높은 계산 비용을 해결하면서, 실제 환경을 반영한 inductive evaluation setting을 도입하여 state-of-the-art 성능을 달성하였다.

## 연구 배경 및 동기
과학 문헌의 폭발적 증가로 관련 선행 연구를 식별하고 인용하는 작업이 점점 어려워지고 있다. 기존 LCR 시스템(SymTax 등)은 인간의 인용 패턴을 모방하는 enricher를 사용하지만, 이는 confirmation bias를 영속화하고 계산 비용이 높으며 특정 메타데이터(taxonomy)에 의존하는 한계가 있다. CiteBART 같은 생성 기반 접근법은 존재하지 않는 인용을 환각(hallucinate)하는 문제가 있다.

## 방법론
- **Profiler**: 논문의 "public profile"(인용 생태계에서의 인식)을 활용하는 경량 비학습 모듈로, prefetcher와 enricher를 단일 모듈로 대체하여 candidate retrieval 효율성 향상
- **DAVINCI reranker**: Profiler에서 도출된 confidence prior와 semantic 정보를 adaptive vector-gating mechanism으로 통합하는 판별적 reranking 모델
- **Inductive evaluation**: 엄격한 시간적 제약을 적용하여 실제 환경(newly authored papers)을 시뮬레이션하는 새로운 평가 프로토콜 도입
- 벤치마크 데이터셋(ACL, RefSeer 등)에서 평가 수행

## 주요 결과
- Profiler가 기존 prefetcher+enricher 조합을 능가하면서도 confirmation bias 없이 동작
- DAVINCI가 기존 SOTA(SymTax) 및 대규모 open-source reranker를 상회하는 성능 달성
- Inductive setting에서도 robust한 성능을 보여 실제 환경 적용 가능성 입증
- Taxonomy 등 특수 메타데이터 없이도 다양한 데이터셋에서 일반화 가능

## 독창성 및 기여
논문의 "public profile"이라는 개념을 citation recommendation에 도입한 점이 독창적이다. 비학습 모듈로 bias-free한 candidate retrieval을 달성하고, 기존의 transductive evaluation의 한계를 지적하며 inductive evaluation을 최초로 제안한 것은 분야에 대한 중요한 방법론적 기여이다.

## 한계 및 향후 연구
- Inductive setting에서의 cold-start 문제(새로운 논문의 profile 부재)에 대한 추가 연구 필요
- 특정 학문 분야에 대한 편향 가능성 미검증
- Profiler의 효과가 인용 네트워크의 밀도에 따라 달라질 수 있음
- 대규모 LLM 기반 reranker와의 비교가 더 폭넓게 이루어질 필요 있음

## 평가
| 항목 | 점수 |
|------|------|
| Novelty | 4/5 |
| Technical Soundness | 4/5 |
| Significance | 3/5 |
| Clarity | 4/5 |
| Overall | 4/5 |

**총평**: Citation recommendation의 실용적 한계를 잘 파악하고, bias-free retrieval과 현실적 evaluation이라는 두 가지 중요한 문제를 동시에 해결한 체계적인 연구이다.
