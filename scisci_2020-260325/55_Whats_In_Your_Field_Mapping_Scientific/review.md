# What's In Your Field? Mapping Scientific Research with Knowledge Graphs and Large Language Models

> **저자**: Abhipsha Das, Nicholas Lourie, Siavash Golkar, Mariel Pettee | **날짜**: 2025-05-29 | **Journal**: (arXiv preprint) | **DOI**: 10.48550/arXiv.2503.09894

---

## Essence

LLM(Llama-3 70B)을 활용하여 과학 논문의 제목과 초록에서 9가지 범주(model, task, dataset, field, modality, method, object, property, instrument)로 구조화된 개념을 추출하고, 이를 SQL 데이터베이스와 knowledge graph로 구축하여 과학 문헌의 체계적 분석을 가능하게 하는 프로토타입 시스템을 제시했다. 3개 분야(천체물리학, 유체역학, 진화생물학)의 arXiv 논문 30,000편에서 개념을 추출하여, 분야 내 modality 분포(천체물리학에서 spectra 35.36%, image 5.58%), 시간적 트렌드, 학제 간 방법론 교차 등을 정량적으로 분석할 수 있음을 시연했다.

## Motivation

과학 문헌의 기하급수적 증가로 인해 분야 전체의 연구 동향을 체계적으로 파악하는 것이 점점 어려워지고 있다. LLM은 과학 텍스트 이해에 강력하지만 대규모 문헌 전체에 걸친 세부 관계를 포착하지 못하며, RAG(Retrieval Augmented Generation) 같은 비구조적 접근은 수백만 개의 사실이 답에 영향을 미칠 때 비용이 과도해진다. 기존의 반구조적 접근(키워드 추출, 벡터 유사도 기반 knowledge graph)은 개념의 기능적 역할을 구분하지 않아 정량적 분석에 한계가 있다. 이에 LLM의 의미론적 이해력과 구조화된 과학 개념 스키마를 결합하여, 문헌 전체에 대한 정밀한 질문에 답할 수 있는 시스템을 구축하고자 했다.

## Achievement

1. **분야 횡단적 과학 개념 스키마 설계**: 9가지 범주(model, task, dataset, field, modality, method, object, property, instrument)의 분야 비의존적(domain-agnostic) 스키마를 반복적 논의와 수작업 주석을 통해 개발
2. **LLM 기반 확장 가능한 추출 파이프라인**: Llama-3 70B에 20개 수작업 주석 논문(3개 few-shot 예시 + 17개 개발 세트)만으로 최적화된 프롬프트를 구성, 문장 단위로 개념 추출; precision 44%+/-12%, recall 31%+/-11% 달성
3. **3개 분야 30,000편 적용 시연**: 천체물리학, 유체역학, 진화생물학에서 각 10,000편의 arXiv 논문 처리, 분야별 개념 유형 분포(object가 모든 분야에서 최다: 44.7-56.1%) 확인
4. **인터랙티브 쿼리 및 시각화 시스템**: SQL 기반 쿼리 인터페이스와 force-directed graph 시각화로 modality 분포, 시간적 트렌드, 학제 간 방법론 교차 분석 가능
5. **RAKE 대비 질적 우위 입증**: 통계 기반 RAKE가 평균 69.2개 키워드를 비구조적으로 추출하는 반면, 본 방법은 32.1개를 의미론적 범주로 구조화하여 더 유용한 정보 제공

## How

- **스키마 설계**: 저자들 간 반복적 논의, 예시 선정, 다분야 논문 검토를 통해 9가지 범주 정의
- **데이터**: arXiv에서 천체물리학(astro-ph), 유체역학(physics.flu-dyn), 진화생물학(q-bio.PE) 각 10,000편의 제목·초록 수집
- **추출 파이프라인**: Llama-3 70B Instruct 모델에 few-shot learning 적용; 프롬프트 최적화 실험(few-shot 예시 수/선택, 프롬프트 구조/순서, 입력 단위 크기, 출력 포맷 변경); 최종 구성은 instruction + schema + 9개 few-shot 예시(3편 논문에서 각 3문장), 문장당 약 2.8초 처리
- **저장 및 쿼리**: SQL 데이터베이스(papers, predictions 2개 테이블)에 메타데이터와 추출 결과 저장
- **시각화**: d3-force 라이브러리 기반 force-directed graph로 개념 간 공출현(co-occurrence) 관계 시각화, 태그 유형 필터링, n-hop 탐색 지원

## Originality

기존의 키워드 추출(RAKE)이나 벡터 유사도 기반 knowledge graph와 달리, 과학 개념을 기능적 역할(무엇을 연구하는가, 어떤 방법으로, 어떤 도구로, 어떤 데이터로)에 따라 범주화하는 분야 비의존적 스키마를 제안한 점이 핵심 독창성이다. 단 20편의 수작업 주석만으로 대규모 추출이 가능한 경량 접근법이며, 추출된 구조화 지식을 SQL 쿼리로 연결하여 "천체물리학에서 galaxy image만 사용하는 논문 비율"과 같은 정량적 질문에 직접 답할 수 있는 시스템을 구현한 점이 실용적 기여이다.

## Limitation & Further Study

### 저자들이 언급한 한계

- 추출 precision(44%)과 recall(31%)이 낮아 노이즈가 존재
- LLM이 특정 명명 개체("Melbourne wind tunnel")와 일반 개념("wind-tunnel data")을 구분하지 못하는 경우 발생
- 개념 간 관계가 공출현(co-occurrence)에 한정되어 인과 관계 등 정교한 관계 표현 불가
- 넓은 범주 정의로 인해 일부 개념이 복수 태그에 해당할 수 있는 모호성 존재

### 리뷰어 판단 아쉬운 점

- **낮은 추출 정확도**: Precision 44%, Recall 31%는 실용적 활용에 상당한 제약 -- 저자들이 "modest extraction accuracy"로 인정하지만, 이 수준에서 도출한 통계의 신뢰성에 대한 체계적 검증이 부족
- **극소 규모 평가 세트**: 20편(3 few-shot + 17 dev)의 천체물리학 논문만으로 평가, 유체역학과 진화생물학에 대한 별도 평가 없음 -- 분야 횡단 일반화 주장의 근거가 약함
- **제목+초록만 사용**: 본문에서만 등장하는 세부 방법론, 데이터셋, 도구 정보가 누락될 수 있음
- **스키마의 주관성**: 9가지 범주의 설계가 저자 4인의 반복적 논의에 기반하며, 분야 전문가나 커뮤니티 검증 없음
- **비교 분석 부족**: RAKE와의 비교만 수행하고, 다른 LLM 기반 개념 추출(SciMuse, Sun et al. 2024 등)과의 정량적 비교 미수행
- **확장성 미검증**: 30,000편은 시연 수준이며, 수백만 편 규모에서의 처리 시간, 비용, 품질 유지에 대한 논의 부재

### 후속 연구

- 추출 정확도 향상을 위한 도메인 특화 fine-tuning 또는 post-training
- 공출현 이상의 의미론적 관계(인과, 활용, 비교 등) 추출
- 전문가 피드백을 통한 스키마 검증 및 세분화
- 전체 논문 본문 활용 파이프라인 개발
- arXiv 전체 규모로의 확장 및 시계열 트렌드 분석

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 3/5 |
| Technical Soundness | 2/5 |
| Significance | 3/5 |
| Clarity | 4/5 |
| Overall | 3/5 |

**총평**: 과학 개념의 기능적 역할별 분류라는 아이디어와 SQL 쿼리 가능한 구조화 지식 시스템의 방향성은 흥미롭지만, 44% precision/31% recall의 낮은 추출 정확도와 20편에 불과한 평가 세트로 인해 실용성과 신뢰성 면에서 프로토타입 수준에 머무른다.
