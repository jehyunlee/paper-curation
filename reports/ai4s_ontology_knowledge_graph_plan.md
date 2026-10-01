# ai4s 온톨로지·지식그래프 구축 계획

## 결론

현재의 SQLite 서지 DB를 진실 원본으로 유지하고, 여기에 **경량 property graph 테이블과 버전드 JSON export**를 추가하는 방식을 권장한다. 현재 규모(전체 4,258편, ai4s 2,707편, ai4s+scisci 2,940편, 논문 관계 51,892개)에서는 별도 그래프 서버보다 **사실과 모델 파생 주장의 분리, 근거 위치, 신뢰도, 버전 관리**가 먼저다.

RDF/OWL 또는 Neo4j는 외부 연동이나 대화형 다중 홉 탐색이라는 명확한 요구가 생겼을 때 SQLite에서 재생성하는 파생 projection으로 도입한다.

## 장점

- 논문–저자–기관–주제–방법–데이터셋–발견 간 관계를 한 번에 탐색할 수 있다.
- 단순 유사 논문보다 “같은 방법을 다른 분야에 적용”, “같은 데이터셋에서 상반된 결론” 같은 설명 가능한 연결을 제공한다.
- RAG 검색에서 관련 문서뿐 아니라 경로와 근거 문장을 함께 반환할 수 있다.
- 신규 논문이 들어왔을 때 기존 연구 흐름·기관·방법론에 자동 연결할 수 있다.
- 현재 보유한 저자 22,158명, 기관 3,577개, 저자–기관 관계 40,047개와 분류·연결 데이터를 재사용할 수 있다.

## 단점과 위험

- LLM이 추출한 관계를 서지 사실과 섞으면 그럴듯한 오류가 영구 저장된다.
- 동일 개체 병합(Method/Dataset/기관 별칭)이 잘못되면 오류가 여러 경로로 전파된다.
- 지나치게 상세한 ontology를 먼저 설계하면 추출 규칙과 유지 비용만 커진다.
- RDF/Neo4j를 바로 도입하면 SQLite와 이중 원본, 동기화·백업·권한·서비스 운영 문제가 생긴다.
- 현재 `paper_connections`와 분류 결과에는 원문 근거 위치·confidence·입력 해시 이력이 충분하지 않다.

## 선택지

| 선택지 | 장점 | 단점 | 선택 조건 |
|---|---|---|---|
| **A. SQLite property graph + JSON** | 기존 PK/FK·증분 해시·검증·백업 재사용, 운영비 최소 | 복잡한 가변 길이 탐색·표준 추론은 제한적 | **현재 권장안** |
| **B. RDF/OWL + SHACL** | 표준 URI, 외부 ontology 연결, SHACL 검증, SPARQL/추론 | provenance 표현과 운영이 복잡하고 triple 수 증가 | Linked Data 공개·외부 기관 교환·OWL 추론이 필수일 때 |
| **C. Neo4j** | Cypher 다중 홉 탐색과 대화형 분석이 편리 | 별도 서비스·동기화·백업·라이선스 비용 | SQLite 질의가 실제 SLA를 못 맞출 때 |

## 최소 스키마

### 노드

- `Paper`: `paper:<slug>`; DOI/arXiv/Scopus/Zotero key는 alias
- `Author`: `author:<author_id>`; 확인된 경우에만 ORCID alias
- `Institution`: ROR가 있으면 `ror:<id>`, 없으면 내부 institution ID
- `Category`, `Subcategory`: topic과 taxonomy version을 ID에 포함
- 내용 개체: 우선 `Method`, `Dataset`, `Task`, `Domain/Material`, `Metric`, `Finding`만 사용
- `SourceDocument`, `Claim`: 원문과 추출 주장을 독립 객체로 관리

### 관계

- 관찰 사실: `AUTHORED_BY`, `AFFILIATED_WITH`, `HAS_SOURCE_DOCUMENT`, `HAS_CITATION_SNAPSHOT`, `PARENT_INSTITUTION`
- 파생 관계: `IN_CATEGORY`, `PROPOSES`, `USES`, `EVALUATES`, `APPLIES_TO`, `REPORTS`
- 논문 관계: `FOUNDATION_OF`, `ALTERNATIVE_TO`, `EXTENDS`, `APPLIES`, `COUNTERPOINT_TO`
- `CITES`는 실제 참고문헌 대상 DOI/arXiv가 확인될 때만 생성한다. 인용 횟수에서 역산하지 않는다.

저자–기관은 논문 문맥을 잃지 않도록 단순 2항 edge가 아니라 `(paper, author, institution)` link entity로 보존한다.

## 사실과 파생 주장 분리

모든 claim에 다음 필드를 둔다.

```text
claim_id, subject_id, predicate, object_id/object_literal,
claim_kind(observed_bibliographic|rule_derived|embedding_derived|llm_derived|human_curated),
source_document_id, source_sha256, evidence_section,
evidence_start/end 또는 evidence_quote_sha256,
extractor, extractor_version, model, prompt_schema_version,
confidence, generated_at, validation_status, reviewer, supersedes_claim_id
```

- DOI·저자·기관·문서 해시 등은 관찰 사실이다.
- 분류·originality·논문 관계·내용 개체는 파생 주장이다.
- 자유문 `reason`은 설명용이며 원문 evidence를 대체하지 않는다.
- LLM은 `same_as` 최종 병합 권한을 갖지 않는다. 불확실한 동일성은 검토 큐로 보낸다.

## 실시 방법

1. **계약 고정**: ID, node type, predicate, claim/provenance 필드, 허용 enum과 무결성 SQL을 정의한다.
2. **사실 그래프**: 기존 DB에 `kg_entities`, `kg_aliases`, `kg_claims`, `kg_evidence`, `kg_runs`를 추가한다. 기존 논문·저자·기관·문서·citation snapshot과 51,892개 논문 연결을 버전드 JSON으로 export한다.
3. **100–200편 파일럿**: category·연도·score별 층화 표본에서 Method/Dataset/Task/Domain/Metric/Finding만 원문 근거와 함께 추출한다.
4. **품질 평가**: 관계별 precision, entity-link 정확도, 근거 문장 일치율을 사람이 평가한다. 고신뢰는 자동 공개, 중간신뢰는 검토, 저신뢰는 폐기한다.
5. **ai4s 전체 증분 적재**: `source_documents.sha256 + extractor_version + schema_version`이 같으면 재사용하고, 바뀐 문서의 해당 extractor claim만 교체한다. 실패·빈 결과도 attempt로 기록한다.
6. **ai4s+scisci 확대**: 2,940편으로 확대하고 taxonomy 버전 간 매핑도 claim으로 관리한다.
7. **필요 시 projection**: 외부 표준 연동이면 RDF/SHACL export, 다중 홉 성능 요구가 확인되면 Neo4j projection을 추가한다. 둘 다 SQLite 원본에서 완전 재생성 가능해야 한다.

## 필수 품질 게이트

- dangling edge, 자기 연결, 허용되지 않은 predicate, 중복 claim: 0
- 모든 파생 claim에 source SHA-256, evidence locator, extractor/model/schema version 존재
- evidence 범위가 실제 원문 내부에 존재
- DOI/ROR 정규형 및 author order·삼항 affiliation 무결성 유지
- 분류·관계별 층화 표본 precision 기준 충족
- 삭제 논문 참조 0, 이전 release 대비 노드·edge 증감 및 실패 수를 manifest에 기록

## 권장 의사결정

**A안부터 실시한다.** 첫 산출물은 서버가 아니라 재생성 가능한 `kg snapshot JSON + manifest + 검증 보고서`여야 한다. 이 단계에서 실제 연구 질의와 정밀도가 입증된 뒤에만 RDF 또는 Neo4j를 추가한다. 핵심 과제는 저장 엔진 교체가 아니라 **문장 수준 provenance가 있는 주장 계층을 만드는 것**이다.
