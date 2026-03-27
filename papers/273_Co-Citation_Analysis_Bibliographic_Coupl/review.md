# Co-Citation Analysis Bibliographic Coupling and Direct Citation: Which Citation Approach Represents the Research Front Most Accurately

> **저자**: Kevin W. Boyack, Richard Klavans | **날짜**: 2010 | **Journal**: Journal of the American Society for Information Science and Technology | **DOI**: [10.1002/asi.21419](https://doi.org/10.1002/asi.21419) | **arXiv**: N/A
> **리뷰 모드**: Web-only

---

## Essence

공동인용(co-citation), 서지 결합(bibliographic coupling), 직접 인용 세 가지 인용 접근법 중 어느 것이 연구 최전선을 가장 정확히 표현하는가? Boyack & Klavans(2010)는 MEDLINE 데이터를 이용해 세 방법 모두를 평가한 결과, 공동인용과 서지 결합이 직접 인용보다 연구 클러스터의 품질(전문가 평가 대비)이 높고, 특히 서지 결합이 최신성 측면에서 유리함을 보였다. 두 방법의 결합이 최적 성능을 낸다.

## Originality (Abstract 기반)

- [novelty] "최초로 세 가지 인용 접근법을 동일 데이터에서 체계적으로 비교 평가함"

## How (방법론)

- **데이터**: MEDLINE 2003–2007 논문 약 230만 편
- **세 가지 접근법**: co-citation(공동 인용된 논문 쌍), bibliographic coupling(공통 참고문헌 공유), direct citation
- **평가**: 전문가 분류(MeSH)와의 일치도 측정(precision, recall), 클러스터 품질 비교
- **군집화**: 각 방법별 유사도 행렬 → Louvain 커뮤니티 탐지

## Why (중요성)

- 과학 지도(science mapping)와 연구 프런트 파악에 어떤 인용 지표가 최적인지 방법론 정립
- 지식 구조 분석 도구 설계에 근거 제공
- 학술 데이터베이스 및 추천 시스템 설계에 실용적 함의

## Limitation

- MEDLINE(생의학) 단일 분야 데이터—물리학, 인문학 등 다른 분야 일반화 한계
- 전문가 분류(MeSH)를 ground truth로 사용하는 데 한계(MeSH 자체도 불완전)
- 데이터 규모와 시간 창의 선택에 결과가 민감할 수 있음

## Further Study

- 다분야 비교 및 하이브리드 지표 개발
- 동적 서지 결합(temporal bibliographic coupling)으로 연구 프런트 진화 추적
- LLM 임베딩과 인용 기반 방법의 결합 효과 평가

## 평가

| 항목 | 점수 |
|------|------|
| Novelty | 3/5 |
| Technical Soundness | 4/5 |
| Significance | 4/5 |
| Clarity | 4/5 |
| Overall | 4/5 |

**총평**: 세 가지 인용 기반 과학 지도 방법을 동일 데이터에서 체계적으로 비교하여 공동인용·서지 결합의 우수성을 입증한 계량과학 방법론 연구다.
