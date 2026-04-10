---
title: "1024_Software_survey_VOSviewer_a_computer_program_for_bibliometri"
authors:
  - "Nees Jan Van Eck"
  - "Ludo Waltman"
date: "2010.08"
doi: "10.1007/s11192-009-0146-3"
arxiv: ""
score: 4.0
essence: "VOSviewer는 서지학적 지도(bibliometric map)를 구성하고 시각화하기 위한 무료 컴퓨터 프로그램으로, 특히 대규모 지도의 그래픽 표현에 특화되어 있다."
tags:
  - "cat/Bibliometric_Network_Analysis"
  - "sub/Scientific_Mapping_and_Visualization"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Van Eck and Waltman_2010_Software survey VOSviewer, a computer program for bibliometric mapping.pdf"
---

# Software survey: VOSviewer, a computer program for bibliometric mapping

> **저자**: Nees Jan Van Eck, Ludo Waltman | **날짜**: 8/2010 | **DOI**: [10.1007/s11192-009-0146-3](https://doi.org/10.1007/s11192-009-0146-3)

---

## Essence

![Figure 3](figures/fig3.webp)

*Fig. 3 Screenshot of the main window of VOSviewer*

VOSviewer는 서지학적 지도(bibliometric map)를 구성하고 시각화하기 위한 무료 컴퓨터 프로그램으로, 특히 대규모 지도의 그래픽 표현에 특화되어 있다.

## Motivation

- **Known**: 서지학적 지도 작성은 SPSS, Pajek 등의 프로그램으로 수행되어 왔으나, 이들은 단순한 그래픽 표현만 제공하여 레이블 겹침 문제가 심하다.
- **Gap**: 대규모 서지학적 지도(100개 이상 항목)의 경우 기존 프로그램들의 단순한 시각화 방식으로는 해석이 어렵고, 줌(zoom), 특수 레이블 알고리즘, 밀도 메타포(density metaphor) 등의 고급 기능이 부재하다.
- **Why**: 과학 분야의 구조와 발전 과정을 파악하기 위해 대규모 서지학적 지도를 효과적으로 시각화하고 탐색할 수 있는 도구의 필요성이 증가하고 있다.
- **Approach**: VOS 매핑 기법(Visualization of Similarities)을 기반으로 거리 기반 지도(distance-based map)에 특화된 뷰어를 개발하고, 줌, 스크롤, 검색 기능 및 다양한 시각화 모드를 통합했다.

## Achievement


- **거리 기반 지도 시각화**: 항목 간 거리가 관계의 강도를 반영하는 거리 기반 지도 표현에 최적화되어 클러스터 식별이 용이하다.
- **고급 상호작용 기능**: 줌, 스크롤, 검색 기능으로 수천 개 항목의 대규모 지도도 상세히 탐색할 수 있다.
- **다중 시각화 모드**: 표준 뷰(standard view), 레이블 뷰(label view), 밀도 뷰(density view) 등으로 지도의 다양한 측면을 강조할 수 있다.
- **VOS 매핑 기법 통합**: VOS 기법이 완전히 통합되어 다양한 서지학적 지도(저자, 저널, 키워드 등) 구성과 표현이 가능하다.
- **대규모 지도 처리 검증**: 5,000개 저널의 공동인용 지도 구성으로 대규모 데이터셋 처리 능력을 입증했다.

## How


- VOS 매핑 기법을 사용하여 거리 기반 지도 구성
- 다차원 척도법(multidimensional scaling) 등 다른 기법으로 생성된 지도도 표시 가능하도록 설계
- 레이블 오버래핑 문제 해결을 위한 특수 레이블링 알고리즘 적용
- 밀도 메타포를 활용한 지도 영역의 항목 집중도 시각화
- 동적 줌 및 스크롤 기능으로 상세 검토 지원
- 서로 다른 관점을 강조하는 여러 뷰(view) 모드 제공
- 다양한 하드웨어 및 운영체제에서 실행 가능하도록 개발

## Originality

- 기존 프로그램과 달리 서지학적 지도의 **그래픽 표현**에 특별한 주의를 기울인 첫 번째 도구
- 대규모 지도의 가독성 문제를 해결하기 위해 밀도 메타포와 특수 레이블링 알고리즘을 종합적으로 적용
- VOS 매핑 기법을 개발자가 직접 통합하여 맞춤형 성능 최적화
- 거리 기반 지도에 특화하되 다양한 매핑 기법의 결과물도 표시할 수 있는 유연한 아키텍처

## Limitation & Further Study

- 거리 기반 지도만 지원하며 그래프 기반 지도(graph-based map)는 불가능 - 추후 그래프 기반 지도 지원 추가 필요
- 시간 발전을 보여주는 시계열 지도 기능 미포함
- 정성적 평가 중심으로 정량적 성능 벤치마킹 부족 - 다양한 규모의 지도에 대한 성능 메트릭 제시 필요
- 사용자 인터페이스 설계에 대한 사용성 평가 연구 부재
- 다양한 서지학적 데이터소스(Scopus, WoS, PubMed 등)와의 직접 연동 기능 제한

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: VOSviewer는 대규모 서지학적 지도의 시각화 문제를 효과적으로 해결하고 무료로 공개된 도구로서 학술 커뮤니티에 실질적인 기여를 한다. VOS 기법과 고급 인터랙티브 기능의 통합으로 기존 도구의 한계를 극복하였으나, 기술적 혁신성보다는 기존 기법의 효과적인 구현에 주력한 점이 특징이다.

## Related Papers

- 🧪 응용 사례: [[papers/949_Comparative_science_mapping_a_novel_conceptual_structure_ana/review]] — VOSviewer의 시각화 기능을 메타데이터 기반 개념 구조 분석이라는 혁신적 과학 매핑에 적용한다.
- 🔗 후속 연구: [[papers/1053_Visualizing_the_context_of_citations_referencing_papers_publ/review]] — 전통적 서지학적 지도를 인용 맥락 기반 키워드 네트워크 시각화로 확장한다.
- 🏛 기반 연구: [[papers/1018_Science_Mapping_and_Science_Maps/review]] — 과학 매핑과 과학 지도의 이론적 배경과 다양한 시각화 접근법을 제공한다.
- 🧪 응용 사례: [[papers/982_Mapping_Knowledge_Topic_Analysis_of_Science_Locates_Research/review]] — VOSviewer의 시각화 기능을 연구 분야의 지리적 분포 매핑에 적용한다.
- 🧪 응용 사례: [[papers/961_Fast_Unfolding_of_Communities_in_Large_Networks/review]] — VOSviewer는 Louvain 알고리즘을 구현하여 학술 네트워크의 커뮤니티 구조를 시각화하는 도구이다.
- 🧪 응용 사례: [[papers/1018_Science_Mapping_and_Science_Maps/review]] — VOSviewer와 같은 구체적인 소프트웨어 도구를 통해 과학 지도 작성의 실용적 구현 방법을 제공한다.
- 🔄 다른 접근: [[papers/939_BibFusion_A_Python_package_to_integrate_deduplicate_and_harm/review]] — VOSviewer의 서지계량 분석 도구와 다른 접근으로 데이터 전처리 단계에서 Scopus와 Web of Science 통합을 위한 Python 기반 솔루션을 제공한다.
