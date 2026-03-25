# The Price-Pareto Growth Model of Networks with Community Structure

> **저자**: Lukasz Brzozowski, Marek Gagolewski, Grzegorz Siudem, Barbara Zogala-Siudem | **날짜**: 2026년 2월 (Preprint, 2026-02-24 업데이트) | **arXiv**: 2510.13392v2

---

## 핵심 요약
본 논문은 커뮤니티 구조를 가진 네트워크의 degree sequence를 모델링하기 위한 새로운 분석적 프레임워크를 제안한다. 기존의 3DSI(Price-Pareto) 모델을 확장하여, 각 커뮤니티별로 고유한 성장 파라미터(참고문헌 수 $m_i$, preferential attachment 비율 $\rho_i$, 커뮤니티 확률 $p_i$)를 부여함으로써 과학 분야 간 인용 문화의 이질성을 포착한다. 각 커뮤니티의 citation count 분포가 Pareto type II 분포로 수렴함을 증명하고, Gini index에 대한 해석적 공식을 도출하였다.

## 연구 배경 및 동기
- Citation network 모델링에서 기존 모델(Barabasi-Albert, Price 모델)은 네트워크를 동질적(homogeneous)으로 가정하여, 분야별로 상이한 성장률, 평균 참고문헌 수, preferential citing 경향 등을 포착하지 못함
- Stochastic Block Model(SBM)이나 LFR Benchmark 등은 정적(static) 커뮤니티 구조를 생성하지만, preferential attachment 하에서의 동적 성장을 모델링하지 못함
- GNN, Graph VAE 등 데이터 기반 모델은 통계적 정밀성과 해석 가능성이 부족
- 따라서 preferential attachment와 커뮤니티 구조를 동시에 갖추면서도 해석적(analytical) 공식을 제공하는 모델이 부재

## 방법론
- **기반 모델**: 3DSI 모델 — 각 시간 단계에서 새 노드가 $m$개의 참조를 배분하되, $(1-\rho)m$개는 무작위(accidental), $\rho m$개는 preferential attachment로 할당
- **커뮤니티 확장**: 새 노드가 확률 $p_i$로 커뮤니티 $i$에 배정되며, 각 커뮤니티는 고유한 $m_i$, $\rho_i$를 가짐. Accidental citation은 전체 네트워크에서, preferential citation은 같은 커뮤니티 내에서만 할당
- **해석적 결과 도출**: Negative binomial distribution과 Beta function을 활용하여 accidental gain의 닫힌 형태(closed-form) 공식 유도, 커뮤니티별 degree sequence 공식(Gamma 함수 기반), Gini index 공식, 그리고 점근적(asymptotic) Pareto type II 분포 수렴 증명
- **파라미터 추정**: 관찰된 네트워크의 인접 행렬에서 커뮤니티별 in-degree 합, out-degree 합, 노드 수, Gini 계수를 계산하여 $\hat{m}_i$, $\hat{p}_i$, $\hat{\rho}_i$를 직접 추정
- **실험 데이터**: Cora 데이터셋(2,708 논문, 7개 커뮤니티)과 DBLP v14 저자 네트워크(481,387 저자, 8개 커뮤니티)에 적용

## 주요 결과
- 각 커뮤니티의 in-degree 분포가 점근적으로 Pareto type II(Lomax) 분포를 따름을 수학적으로 증명
- 커뮤니티별 Gini index의 해석적 공식을 도출하고, 전체 네트워크의 Gini 계수도 hypergeometric function을 통해 근사
- Cora 데이터셋에서 7개 커뮤니티 모두에 대해 모델 예측 CCDF가 실제 관측 분포와 잘 일치
- DBLP 저자 네트워크에서도 대부분의 커뮤니티(8개 중 6개)에서 양호한 적합도를 보임
- 커뮤니티별 파라미터의 이질성을 정량적으로 확인: 예를 들어 DBLP에서 Computer Science($\hat{\rho}=0.741$)와 Electronic Engineering($\hat{\rho}=0.627$)의 preferential attachment 비율 차이

## 독창성 및 기여
- Preferential attachment 규칙 하에서 커뮤니티 구조를 허용하는 **최초의 해석적 네트워크 성장 모델** — 기존 survey(Drobyshevskiy & Turdakov, 2019)에서 이러한 모델이 존재하지 않음을 지적한 바 있음
- 모델 파라미터가 직관적이고 해석 가능: $m_i$(생산성), $\rho_i$(preferential vs. accidental 비율), $p_i$(커뮤니티 크기)
- Gini index와 Pareto 분포의 해석적 연결이 bibliometrics 및 science of science에서 불평등 분석에 직접 활용 가능
- 파라미터 추정이 간단(adjacency matrix로부터 직접 계산 가능)하여 실무 적용성이 높음

## 한계 및 향후 연구
- **저자 언급 한계**: 전체 네트워크의 global degree sequence에 대한 간단한 해석적 표현을 찾지 못함; 커뮤니티 간 citation 비율을 외생적으로 고정하여 동적 커뮤니티 변화를 모델링하지 못함
- **추가 지적**: 커뮤니티 할당이 고정 확률 $p_i$에 의해 결정되므로, 시간에 따른 분야의 성장률 변화(예: AI 분야의 최근 급성장)를 반영하지 못함
- 실험이 2개 데이터셋에 한정되어 있으며, 다양한 규모와 특성의 네트워크에 대한 검증이 필요
- 커뮤니티 내 자체 인용(self-citation) 외에 커뮤니티 간 인용의 비대칭적 패턴은 모델에서 다루지 않음
- Pareto type II 수렴은 점근적 결과이므로, 소규모 커뮤니티에서의 유한 표본(finite sample) 적합도는 불확실

## 평가
| 항목 | 점수 (1-5) |
|------|-----------|
| Novelty | 4 |
| Technical Soundness | 5 |
| Significance | 4 |
| Clarity | 4 |
| Overall | 4 |

**총평**: 커뮤니티 구조를 갖는 네트워크 성장 모델의 중요한 이론적 공백을 메우는 수학적으로 엄밀한 논문으로, 해석적 공식의 도출이 인상적이나, 실증 실험의 범위를 넓히고 동적 커뮤니티 구조로의 확장이 향후 과제로 남아 있다.
