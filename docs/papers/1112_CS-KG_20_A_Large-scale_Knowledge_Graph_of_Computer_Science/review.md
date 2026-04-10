---
title: "1112_CS-KG_20_A_Large-scale_Knowledge_Graph_of_Computer_Science"
authors:
  - "Danilo Dessí"
  - "Francesco Osborne"
  - "Davide Buscaldi"
  - "Diego Reforgiato Recupero"
  - "Enrico Motta"
date: "2025.06"
doi: "10.1038/s41597-025-05200-8"
arxiv: ""
score: 4.0
essence: "150만 개의 컴퓨터과학 논문에서 자동 추출한 2,500만 개 엔티티와 6,700만 개 관계로 구성된 CS-KG 2.0 지식그래프를 제시하며, 이를 통해 연구 트렌드 분석, 가설 생성, 지능형 문헌 검색 등을 지원한다."
tags:
  - "cat/Scientific_Information_Systems"
  - "cat/Bibliometric_Network_Analysis"
  - "sub/Knowledge_Graphs_and_Semantic_Mapping"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Dessí et al._2025_CS-KG 2.0 A Large-scale Knowledge Graph of Computer Science.pdf"
---

# CS-KG 2.0: A Large-scale Knowledge Graph of Computer Science

> **저자**: Danilo Dessí, Francesco Osborne, Davide Buscaldi, Diego Reforgiato Recupero, Enrico Motta | **날짜**: 2025-06-09 | **DOI**: [10.1038/s41597-025-05200-8](https://doi.org/10.1038/s41597-025-05200-8)

---

## Essence

![Figure 1](figures/fig1.webp)

*Fig. 1  The modules used to create our resource from the SCICERO52 pipeline.*

150만 개의 컴퓨터과학 논문에서 자동 추출한 2,500만 개 엔티티와 6,700만 개 관계로 구성된 CS-KG 2.0 지식그래프를 제시하며, 이를 통해 연구 트렌드 분석, 가설 생성, 지능형 문헌 검색 등을 지원한다.

## Motivation

- **Known**: 지식그래프(Knowledge Graph)는 구조화된 데이터로 도메인의 핵심 엔티티와 관계를 표현하여 AI 시스템의 정보 통합 능력을 향상시킨다. 기존 AI-KG와 CS-KG는 제한된 커버리지와 의미적 깊이의 한계를 보였다.
- **Gap**: 기존 CS-KG는 인용된 논문만 포함하여 최신 논문을 제외하고, 시간 정보가 부족하며, 중단된 MAG에 기반하여 현재 메타데이터 카탈로그와 연결할 수 없다.
- **Why**: 연구 논문이 연간 250만 건 이상 발표되는 상황에서 구조화된 지식그래프는 LLM 기반 도구의 한계를 극복하고 대규모 문헌 분석을 가능하게 하며, 연구 커뮤니티가 생성하는 메서드와 데이터셋을 효과적으로 탐색할 수 있게 한다.
- **Approach**: OpenAlex의 오픈 메타데이터를 기반으로 SCICERO 파이프라인을 통해 2010-2022년의 컴퓨터과학 논문에서 Task, Method, Metric, Material 등의 엔티티와 관계를 자동 추출하고, 시간 정보와 문맥 정보를 추가하여 CS-KG 2.0을 구축했다.

## Achievement

![Figure 2](figures/fig2.webp)

*Fig. 2  The distribution of the entities across the classes Method, Task, Material, Metric, and OtherEntity.*

- **규모의 대폭 확대**: 전작 대비 50배 이상 확대된 10억 개 이상의 RDF 트리플과 2,400만 개의 연구 엔티티, 6,700만 개의 관계 포함
- **시간 정보 통합**: 엔티티와 진술에 연결된 시간 데이터를 포함하여 연구 트렌드의 시간별 분석 가능
- **포괄적 커버리지**: 1,500만 개의 컴퓨터과학 논문을 포함하며 인용 여부와 무관하게 최신 논문도 수록
- **상호운용성**: OpenAlex와의 완전한 연동으로 지속적 업데이트와 현재 메타데이터 카탈로그와의 연계 가능
- **평가 벤치마크**: 링크 예측 알고리즘 평가용 CSKG-2M, CSKG-490K, CSKG-132K 등 3개의 대규모 벤치마크 제공

## How

![Figure 1](figures/fig1.webp)

*Fig. 1  The modules used to create our resource from the SCICERO52 pipeline.*

- OpenAlex 카탈로그에서 컴퓨터과학 분야 2010-2022년 논문 메타데이터 수집
- SCICERO 파이프라인을 통한 자동 엔티티 추출 (Task, Method, Metric, Material, OtherEntity)
- RDF 형식의 <subject, predicate, object> 트리플로 엔티티 간 관계 형식화
- 시간 정보(연도, 기간)와 문맥 정보(co-occurrence 패턴 등) 추가
- 링크 예측 기법을 통한 지식그래프 향상 및 검증
- OpenAlex API 및 데이터 덤프를 통한 메타데이터 접근 제공

## Originality

- 자동화된 대규모 컨텐츠 기반 지식그래프로서 크라우드소싱의 확장성 한계를 극복
- OpenAlex 기반의 지속 가능한 인프라 구축으로 중단된 MAG의 한계 해결
- 엔티티와 관계에 시간 정보를 통합한 첫 시도로 트렌드 분석 능력 제공
- 1억 개 이상의 RDF 트리플 규모로 기존 학술 지식그래프 대비 획기적인 규모 확장

## Limitation & Further Study

- 2010-2022년으로 시간 범위가 제한되어 2023년 이후 최신 연구 반영 불가
- 컴퓨터과학 분야에만 제한되어 타 학문 분야 적용 불가
- 자동 추출의 정확성이 100%가 아니어서 일부 오류나 누락 존재 가능성
- 엔티티 간 의미 관계의 깊이가 여전히 제한적일 수 있음
- **후속연구**: 다른 학문 분야로의 확대, 실시간 업데이트 메커니즘 개발, 자동 추출 정확도 향상, 시맨틱 웹 기술을 통한 사용자 검증 및 큐레이션 프로세스 구축

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: CS-KG 2.0은 자동화된 대규모 학술 지식그래프로서 기존의 한계를 상당 부분 극복하였으며, OpenAlex 기반의 지속 가능한 인프라와 시간 정보 통합을 통해 학술 문헌 분석 연구에 혁신적인 자원을 제공한다. 다만 시간 범위와 학문 분야 제한, 자동 추출의 정확성 개선이 필요하다.

## Related Papers

- 🧪 응용 사례: [[papers/1073_MOLIERE_Automatic_Biomedical_Hypothesis_Generation_System/review]] — 컴퓨터과학 지식그래프를 생의학 분야 자동 가설 생성 시스템으로 응용한다.
- 🔄 다른 접근: [[papers/1109_A_comprehensive_large-scale_biomedical_knowledge_graph_for_A/review]] — 컴퓨터과학 특화 지식그래프 대신 생의학 분야의 포괄적 지식그래프를 제안한다.
- 🧪 응용 사례: [[papers/1114_GoAI_Enhancing_AI_Students_Learning_Paths_and_Idea_Generatio/review]] — CS-KG 2.0을 AI 학습자의 학습 경로 최적화와 아이디어 생성 도구로 활용한다.
- 🏛 기반 연구: [[papers/1054_Whats_In_Your_Field_Mapping_Scientific_Research_with_Knowled/review]] — 지식그래프 구축을 연구 분야 매핑과 과학적 지식 체계화의 방법론적 기반으로 제공한다.
- 🏛 기반 연구: [[papers/930_A_Survey_on_Knowledge_Organization_Systems_of_Research_Field/review]] — 연구 분야의 지식 조직 시스템에 대한 이론적 기반을 제공하여 컴퓨터과학 지식그래프 구축의 개념적 토대가 된다.
- 🧪 응용 사례: [[papers/982_Mapping_Knowledge_Topic_Analysis_of_Science_Locates_Research/review]] — 주제 수준에서 과학 연구를 매핑하는 구체적 사례로 컴퓨터과학 분야의 지식그래프 활용을 보여준다.
- 🔄 다른 접근: [[papers/1015_S2ORC_The_Semantic_Scholar_Open_Research_Corpus/review]] — 범학문적 대규모 코퍼스 대신 컴퓨터과학 특화된 지식그래프로 구조화된 학술 정보를 제공한다.
