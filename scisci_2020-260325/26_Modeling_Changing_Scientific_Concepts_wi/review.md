# Modeling Changing Scientific Concepts with Complex Networks: A Case Study on the Chemical Revolution

> **저자**: Sofía Aguilar-Valdez, Stefania Degaetano-Ortlieb | **날짜**: 2026 | **Journal**: arXiv (physics.soc-ph) | **DOI**: 10.48550/ARXIV.2603.17594

---

## Essence
복잡 네트워크 구조는 과학적 개념의 변천을 반영할 수 있는가? 그렇다. 화학혁명 시기 Royal Society Corpus를 분석한 결과, 산소 이론이 플로지스톤 이론을 대체하는 과정에서 개념 네트워크의 엔트로피(topic diversity)와 위상 밀도(topological density)가 유의미하게 증가했다. 즉, onomasiological change(동일 개념을 지칭하는 언어 표현의 변화)가 일어날 때 네트워크의 다양성과 연결 복잡성이 함께 증가하며, 이는 과학혁명의 정량적 지표로 활용될 수 있다.

## Motivation
LLM 기반 단어 임베딩은 개념 변화를 추정할 수 있지만, 해석가능성이 낮고 시간 인식이 부족하며, 역사 데이터의 편향 증폭 위험이 있다. 기존 의미 변화 연구는 단어 수준(semasiological)에 머물렀으나, 과학혁명에서는 개념 전체가 교체되는 onomasiological 변화가 핵심이다. 이 gap을 메우기 위해 해석 가능하고 시간 인식적인 네트워크 기반 프레임워크가 필요했다.

## Achievement
1. **프로토타입 의미론 기반 개념 네트워크 프레임워크** 제안: 과학 텍스트를 토픽 모델링 후 클러스터링하여 개념의 중심-주변(core-periphery) 구조를 그래프로 표현
2. **화학혁명 사례 분석**: 1750년대~1800년대 Royal Society Corpus에서 phlogiston → oxygen 전환 과정을 정량적으로 추적
3. **Jensen-Shannon distance**와 **엔트로피** 두 지표를 통해 개념 구조 변화의 크기와 방향성을 측정
4. onomasiological 변화가 높은 엔트로피 및 위상 밀도와 연관됨을 확인 — 아이디어 다양성 증가와 연결 노력의 증대를 의미

## How
- **데이터**: Royal Society Corpus (18세기 과학 출판물)
- **방법**: 토픽 모델링으로 문서-토픽 분포 추출 → 유사도 기반 클러스터링으로 개념 네트워크 구축 → 시기별(10년 단위) 네트워크 비교
- **평가 지표**: Jensen-Shannon distance (시기 간 토픽 클러스터 차이), Shannon entropy (토픽 다양성)
- **이론적 기반**: Geeraerts(1997)의 프로토타입 의미론, Kuhn(2012)의 과학혁명론

## Originality
- 의미 변화 탐지를 단어 수준이 아닌 **개념 네트워크 수준**으로 격상시킨 최초의 시도
- "Conceptual Structure Shift Detection"이라는 새로운 NLP 태스크를 정의하고 형식화
- 정보이론 지표(JSD, entropy)를 개념 네트워크의 시간적 변화 측정에 적용

## Limitation & Further Study
### 저자들이 언급한 한계
- 단일 사례 연구(화학혁명)에 기반하므로 일반화에 한계
- Royal Society Corpus의 규모와 시대적 제약

### 리뷰어 판단 아쉬운 점
- 정량적 검증이 주로 기술적 수준에 머물러 있으며, ground truth와의 체계적 비교가 부족
- 다른 과학혁명 사례(예: 다윈 진화론, 양자역학)에 대한 적용 없이는 프레임워크의 보편성을 주장하기 어려움
- 토픽 모델링의 하이퍼파라미터 민감도 분석이 부족

### 후속 연구
- 다양한 과학혁명 사례로의 확장
- 현대 과학 텍스트(arXiv 등)에 대한 적용
- LLM 기반 방법과의 체계적 비교

## Evaluation
| 항목 | 점수 |
|------|------|
| Novelty | 4/5 |
| Technical Soundness | 3/5 |
| Significance | 3/5 |
| Clarity | 4/5 |
| Overall | 3/5 |

**총평**: 과학적 개념 변화를 네트워크 구조로 모델링하는 독창적 프레임워크를 제안했으나, 단일 사례에 의존하여 일반화 가능성의 검증이 부족하다.
