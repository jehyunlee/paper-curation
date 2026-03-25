# Public Profile Matters: A Scalable Integrated Approach to Recommend Citations in the Wild

> **저자**: Karan Goyal, Dikshant Kukreja, Vikram Goyal, Mukesh Mohania | **날짜**: 2026-03-18 | **Journal**: arXiv preprint | **DOI**: 10.48550/arXiv.2603.17361

---

## Essence

논문의 "공적 프로필(public profile)" -- 인용 네트워크에서 다른 논문들이 해당 논문을 어떻게 인용하는지의 집합적 인식 -- 이 인용 추천의 핵심 신호임을 실증한다. 비학습(non-learnable) Profiler 모듈은 기존 SOTA 대비 검색 시간을 최대 44배 단축하면서 MRR을 45-64% 향상시키고, 110M 파라미터의 DAVINCI 리랭커는 8B 규모의 범용 리랭커를 모든 데이터셋에서 능가한다.

## Motivation

- **알려진 사실**: 과학 문헌의 폭발적 증가로 연구자가 관련 선행 연구를 식별하기 어려워지고 있으며, 자동 인용 추천 시스템(특히 local citation recommendation, LCR)이 필요
- **격차(Gap)**: 기존 SOTA인 SymTax는 3단계 아키텍처(prefetcher-enricher-reranker)로 높은 계산 비용, 확인 편향(confirmation bias) 영속화, 분류 체계(taxonomy) 메타데이터 의존이라는 세 가지 한계 보유. 또한 기존 평가 프로토콜이 transductive 설정으로 실제 사용 시나리오를 반영하지 못함
- **접근법**: (1) 인용 네트워크의 정적 변환으로 "공적 프로필"을 구축하는 비학습 Profiler 모듈, (2) 엄격한 시간적 제약을 적용하는 inductive 평가 설정, (3) 검색 단계의 confidence prior와 의미 정보를 adaptive vector-gating으로 융합하는 DAVINCI 리랭커 제안

## Achievement

1. **Profiler의 효율성**: ArSyTa(최대 데이터셋)에서 검색 시간 32.5배 단축(236시간 -> 7.26시간), MRR 63.85% 향상(7.94 -> 13.01). FullTextPeerRead에서 44배 속도 향상, MRR 45.3% 향상
2. **End-to-End SOTA**: 5개 벤치마크 데이터셋(ACL-200, FullTextPeerRead, RefSeer, arXiv, ArSyTa) 전체에서 MRR, Recall@K, NDCG@K 모든 메트릭에서 기존 SOTA(SymTax) 능가
3. **소형 모델의 대형 모델 초과 성능**: 110M 파라미터 DAVINCI가 Qwen3-Reranker-8B(8.19B)와 bge-reranker-v2(2.72B)를 모든 데이터셋에서 능가. 최대 70배 작은 모델이 더 높은 성능
4. **Inductive 평가 설정 도입**: 시간적 일관성을 강제하는 엄격한 귀납적 평가 프레임워크를 도입하여, 실제 환경에서의 인용 추천 성능을 보다 정확하게 평가
5. **프로필 제거 시 성능 급락**: 프로필 enrichment를 비활성화하면 모든 데이터셋에서 검색 성능이 심각하게 하락, "공적 프로필"이 필수적 신호임을 확인

## How

- **Profiler (1단계 검색)**:
  - 각 논문의 기본 벡터(specter2_base 인코더)를 인용 네트워크의 inward ego network(인용 논문들의 내용 + 인용 맥락)으로 보강
  - 정적, 비학습 변환: `v_hat_i = v_i + (1/|N_in|) * sum(alpha * v_sji + beta * v_j)`
  - 코사인 유사도 기반 효율적 검색, cold start 문제 자연 처리
- **DAVINCI (2단계 리랭킹)**:
  - Prior Discriminator: 검색 순위를 지수 감쇠(`p_i = lambda^r_i`)로 비선형 변환
  - Adaptive Vector-Gating: SciBERT 기반 의미 표현과 confidence prior를 독립 MLP tower로 프로젝션 후, gating network으로 차원별 soft masking 수행
  - Margin-based triplet loss로 직접 랭킹 최적화
- **데이터셋**: ACL-200, FullTextPeerRead, RefSeer(350만 컨텍스트), arXiv(300만), ArSyTa(800만)
- **평가**: Inductive 설정 하 MRR, Recall@K, NDCG@K

## Originality

"공적 프로필(public profile)"이라는 개념을 인용 추천에 도입한 것이 핵심 기여이다. 논문의 관련성이 내재적 내용뿐 아니라 학술 네트워크에서의 "인식된 정체성"에도 의존한다는 통찰을 비학습 모듈로 구현하여, 확인 편향 없이도 기존 3단계 시스템을 능가한다. 또한 transductive에서 inductive로의 평가 패러다임 전환을 제안하여 LCR 벤치마킹의 방법론적 표준을 높였다. 소형 특화 모델이 대형 범용 모델을 능가할 수 있다는 실증도 의미 있다.

## Limitation & Further Study

### 저자들이 언급한 한계
- 영어 및 컴퓨터 과학 분야에 한정된 평가로, 인문/사회과학의 인용 맥락 차이를 반영하지 못함
- 인용이 전혀 없는 완전히 새로운 논문에 대한 cold start 문제 (base semantic vector에만 의존)
- Transformer 기반 리랭커의 512토큰 입력 제한으로 긴 문서의 전체 맥락 포착 어려움
- 메타데이터(초록, 제목) 품질에 성능이 의존

### 리뷰어 판단 아쉬운 점
- arXiv 프리프린트로 아직 동료심사를 거치지 않음
- 비학습 하이퍼파라미터(alpha, beta, gamma, delta)의 최적값이 소규모 데이터셋에서 결정되어 대규모 적용 시 일반화 보장이 불확실
- "공적 프로필"이 결국 인용 네트워크 정보의 활용이므로, popularity bias를 완전히 제거했다고 보기 어려움 (많이 인용된 논문의 프로필이 더 풍부)
- Science of Science 관점에서의 분석(왜 공적 프로필이 효과적인지에 대한 이론적 고찰)이 부족하고 순수 공학적 기여에 집중

### 후속 연구
- 다국어 및 다학문(인문/사회과학) 확장
- 시간에 따라 변화하는 동적 프로필 모델링
- 인용 추천의 diversity/novelty 메트릭 도입 (인기 논문 편향 완화)
- Science of Science 연구와의 연계: 인용 행동 모델링, 인용 편향 분석

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 4/5 |
| Technical Soundness | 4/5 |
| Significance | 3/5 |
| Clarity | 4/5 |
| Overall | 4/5 |

**총평**: 인용 추천 시스템에서 "공적 프로필"이라는 직관적이면서도 효과적인 개념을 제안하고, 비학습 모듈과 경량 리랭커의 조합으로 대규모 범용 모델을 능가하는 실용적 시스템을 구축했다. 방법론적 완성도가 높으나, Science of Science 관점에서의 이론적 기여보다는 정보검색 공학 기여에 가까운 논문이다.
