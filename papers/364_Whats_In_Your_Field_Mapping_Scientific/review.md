# What's In Your Field? Mapping Scientific Research with Knowledge Graphs and Large Language Models

> **저자**: Abhipsha Das, Nicholas Lourie, Siavash Golkar, Mariel Pettee | **날짜**: 2025-05-29 | **Journal**: arXiv preprint | **DOI**: [10.48550/arXiv.2503.09894](https://doi.org/10.48550/arXiv.2503.09894)
> **리뷰 모드**: Abstract 기반 (PDF 없음)

---

## Essence

대규모 학술 문헌을 체계적으로 분석하려면 구조화된 지식 표현이 필요하지만, LLM 기반 비구조적 접근법은 수백만 건의 사실이 답변에 영향을 미칠 때 비용이 폭발적으로 증가한다. 이 논문은 LLM의 의미론적 이해와 구조화된 스키마를 결합하여 30,000편의 arXiv 논문(천체물리학·유체역학·진화생물학)으로부터 knowledge graph를 구축하는 시스템 "Surveyor"를 제시한다. 단 20개의 수동 주석 초록만으로 스키마를 학습시켜 분야 전체의 신흥 트렌드를 식별하고 지식 지형을 시각화하는 데 성공했다.

## Originality (Abstract 기반)

- [authorship, action] "we try extracting structured representations using LLMs."
- [authorship, novelty] "By combining LLMs' semantic understanding with a schema of scientific concepts, we prototype a system that answers precise questions about the literature as a whole."
- [result] "Our schema applies across scientific fields and we extract concepts from it using only 20 manually annotated abstracts."

## How (방법론)

- **데이터**: arXiv 30,000편 논문 — 천체물리학, 유체역학, 진화생물학 3개 분야 포함
- **스키마 설계**: 분야 횡단적으로 적용 가능한 과학적 개념 스키마 정의; 20개 수동 주석 초록으로 학습
- **LLM 기반 개념 추출**: 정의된 스키마에 따라 LLM이 논문 초록에서 구조화된 개념과 관계를 추출
- **Knowledge Graph 구축**: 추출된 개념-관계 쌍으로 전체 코퍼스에 걸친 구조화 DB 구축
- **시각화**: Knowledge graph 탐색 인터페이스로 신흥 연구 트렌드 및 분야 지형 시각화
- **시연**: HuggingFace Spaces(abby101/surveyor-0)에 데모 공개, GitHub 코드 오픈소스

## Why (중요성)

- 학술 문헌의 지수적 증가로 연구자가 분야 전체를 파악하기 어려워지고 있으며, 기존 RAG 방식은 수백만 건 규모에서 비용 문제가 있음
- LLM 단독으로는 전체 코퍼스에 걸친 체계적 패턴 분석이 불가능하며, 구조화된 표현과의 결합이 필수적임
- 20개 주석만으로 새로운 분야에 스키마를 적용할 수 있다면, 신흥 분야 모니터링의 비용이 획기적으로 낮아짐
- Science of Science 연구에서 대규모 지식 구조 자동 추출은 연구 동향 분석의 새 패러다임을 제시

## Limitation

### 저자들이 언급한 한계
- Abstract 기준으로 명시적 한계 서술이 제한적이나, "prototype"임을 명시하여 시스템의 초기 단계성을 인정

### 자체판단 아쉬운 점
- 20개 주석 초록으로 학습한 스키마의 품질과 완전성에 대한 정량적 검증이 충분히 제시되었는지 불명확
- 3개 분야(천체물리학·유체역학·진화생물학) 선택이 대표성 있는지 — 사회과학, 의학 등 다른 분야에서의 일반화 성능 미검증
- LLM 추출 오류의 누적이 knowledge graph 품질에 미치는 영향 분석 필요

### 후속 연구
- 스키마의 분야 독립성 검증 및 더 많은 학문 분야로 확장
- 실시간 문헌 업데이트와 연동한 동적 knowledge graph 구축
- 추출 정확도와 그래프 기반 분석 결과의 정량적 평가 체계 확립

## 평가

| 항목 | 점수 |
|------|------|
| Novelty | 4/5 |
| Technical Soundness | 3/5 |
| Significance | 4/5 |
| Clarity | 4/5 |
| Overall | 4/5 |

**총평**: 최소한의 수동 주석으로 대규모 학술 코퍼스의 구조화된 지식 표현을 자동 구축하는 실용적 시스템을 제시하며, LLM의 의미론적 능력과 구조화 표현의 장점을 효과적으로 결합했다. 프로토타입 단계의 한계가 있으나 Science of Science 자동화의 유망한 방향성을 제시한다.
