# AIRS-Bench: a Suite of Tasks for Frontier AI Research Science Agents

**저자:** Alisia Lupidi, Bhavul Gauri, Thomas Simon Foster, Bassel Al Omari, Despoina Magka, Alberto Pepe, Alexis Audran-Reiss, Muna Aghamelu, Nicolas Baldwin, Lucia Cipolina-Kun, Jean-Christophe Gagnon-Audet, Chee Hau Leow, Sandra Lefdal, Hossam Mossalam, Abhinav Moudgil, Saba Nazir, Emanuel Tewolde, Isabel Urrego, Jordi Armengol Estape, Amar Budhiraja, Gaurav Chaurasia, Abhishek Charnalia, Derek Dunfield, Karen Hambardzumyan, Daniel Izcovich, Martin Josifoski, Ishita Mediratta, Kelvin Niu, Parth Pathak, Michael Shvartsman, Edan Toledo, Anton Protopopov, Roberta Raileanu, Alexander Miller, Tatiana Shavrina, Jakob Foerster, Yoram Bachrach
**출처:** arXiv preprint (2026)
**DOI:** 10.48550/ARXIV.2602.06855
**PDF:** [arXiv](https://arxiv.org/abs/2602.06855)

---

## 한줄 요약 (Essence)
최신 ML 논문에서 추출한 20개 태스크로 구성된 AIRS-Bench를 제안하여, AI 에이전트의 아이디어 생성부터 실험 분석 및 반복 개선까지 전체 연구 생애주기에 걸친 에이전트 역량을 평가하는 벤치마크 연구.

---

## 연구 동기 (Motivation)
- LLM 에이전트가 과학 연구를 가속화할 잠재력이 크지만, 실제 연구 워크플로 전반에 걸친 에이전트 역량을 평가할 **종합적 벤치마크가 부재**
- 기존 벤치마크는 단일 태스크나 특정 단계에 초점을 맞추며, **아이디어 생성 → 실험 설계 → 분석 → 반복 개선**이라는 연구의 전체 사이클을 다루지 못함
- 베이스라인 코드를 제공하지 않는 조건에서 에이전트가 **처음부터 독립적으로 연구를 수행**할 수 있는지 평가할 필요성
- 다양한 에이전트 프레임워크 간의 **공정하고 엄격한 비교**를 가능하게 하는 표준화된 평가 체계 필요

---

## 주요 성과 (Achievement)
- 언어 모델링, 수학, 생물정보학, 시계열 예측 등 **다양한 도메인을 아우르는 20개 태스크** 구축
- 베이스라인 코드 없이 전체 연구 생애주기를 평가하는 **AIRS-Bench 태스크 포맷** 설계
- Sequential 및 parallel scaffold를 사용한 frontier 모델 기반 **베이스라인 결과** 확립
- 핵심 발견:
  - 에이전트가 **4개 태스크에서 인간 SOTA를 초과** 달성
  - 그러나 **16개 태스크에서는 인간 SOTA에 미달**, 벤치마크가 아직 포화되지 않음
  - 인간 벤치마크를 초과한 경우에도 **이론적 성능 상한에는 도달하지 못함**
- 태스크 정의 및 평가 코드를 오픈소스로 공개

---

## 방법론 (How)
1. **태스크 소싱:** 최신 ML 논문(state-of-the-art)에서 실제 연구 문제를 추출하여 20개 태스크 구성
2. **도메인 다양성:** 언어 모델링, 수학, 생물정보학, 시계열 예측 등 다양한 분야 포괄
3. **평가 설계:** 베이스라인 코드를 제공하지 않아, 에이전트가 문제 이해 → 접근법 설계 → 구현 → 실험 → 분석의 전 과정을 독립적으로 수행해야 함
4. **에이전트 scaffold:** Frontier 모델에 sequential(순차적) 및 parallel(병렬) scaffold를 적용하여 베이스라인 확립
5. **태스크 포맷:** 새로운 태스크를 쉽게 추가하고 다양한 에이전트 프레임워크를 비교할 수 있는 범용적 포맷 설계

---

## 독창성 (Originality)
- **전체 연구 생애주기**를 아우르는 벤치마크라는 점에서 기존의 단일 능력 평가 벤치마크와 근본적으로 차별화
- 베이스라인 코드를 제공하지 않는 설계는 에이전트의 **진정한 자율 연구 능력**을 시험하는 도전적 설정
- 인간 SOTA와의 비교뿐 아니라 **이론적 성능 상한**까지 설정하여 벤치마크의 남은 여지를 정량적으로 제시
- 다양한 에이전트 프레임워크를 공정하게 비교할 수 있는 **범용 태스크 포맷**의 설계가 실용적

---

## 한계 (Limitation)
- 20개 태스크가 주로 **ML/CS 관련 분야에 편중**되어 있으며, 실험과학(화학, 물리 실험 등)의 포괄 범위가 제한적
- 베이스라인 코드 미제공이 현실적 연구 상황을 반영하는지 의문 -- 실제 연구자도 기존 코드를 참고하는 경우가 대부분
- 평가 메트릭이 **최종 성과(정량 스코어) 중심**이며, 에이전트의 연구 과정(탐색 전략, 가설 수립 품질 등)에 대한 질적 평가가 부족할 수 있음
- Frontier 모델만 베이스라인으로 사용하여, 중소 규모 모델이나 오픈소스 에이전트의 성능 분포는 알 수 없음
- 태스크 난이도의 균일성과 **도메인 간 비교 가능성**에 대한 논의가 필요

---

## 총평 (Evaluation)
AIRS-Bench는 AI 연구 에이전트의 역량을 전체 연구 생애주기 관점에서 평가한다는 점에서 시의적절하고 야심찬 벤치마크이다. 4/20 태스크에서만 인간 SOTA를 초과한다는 결과는 현재 AI 에이전트의 자율 연구 능력에 대한 현실적 그림을 제시한다. 범용적 태스크 포맷과 오픈소스 공개는 커뮤니티의 후속 연구를 촉진할 것으로 기대된다. 다만 ML 분야 편중과 최종 성과 중심의 평가는 벤치마크의 범용성과 깊이를 동시에 확보하기 어려운 근본적 한계를 보인다. 전반적으로 **자율 과학 연구 에이전트 평가의 중요한 이정표**가 될 수 있는 연구이며, 태스크 확장과 과정 평가 도입이 향후 과제로 남아 있다.

## 평가
| 항목 | 점수 (1-5) |
|------|-----------|
| Novelty | 4 |
| Technical Soundness | 3 |
| Significance | 4 |
| Overall | 3.7 |

**총평**: AI 연구 에이전트의 프론티어 역량을 평가하는 체계적 벤치마크로 범위와 설계가 우수하나 평가 자동화에 추가 보완이 필요하다.
