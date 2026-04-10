---
title: "1118_Paper_Circle_An_Open-source_Multi-agent_Research_Discovery_a"
authors:
  - "Komal Kumar"
  - "Aman Chadha"
  - "Salman Khan"
  - "Fahad Shahbaz Khan"
  - "Hisham Cholakkal"
date: "2026.04"
doi: "10.48550/arXiv.2604.06170"
arxiv: ""
score: 4.0
essence: "Paper Circle는 학술 문헌 발견과 분석을 위한 다중 에이전트 LLM 기반 프레임워크로, Discovery Pipeline과 Analysis Pipeline을 통해 논문 검색, 평가, 구조화된 지식 그래프 생성을 자동화한다."
tags:
  - "cat/Scientific_Information_Systems"
  - "sub/AI-Driven_Research_Discovery"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Kumar et al._2026_Paper Circle An Open-source Multi-agent Research Discovery and Analysis Framework.pdf"
---

# Paper Circle: An Open-source Multi-agent Research Discovery and Analysis Framework

> **저자**: Komal Kumar, Aman Chadha, Salman Khan, Fahad Shahbaz Khan, Hisham Cholakkal | **날짜**: 2026-04-07 | **DOI**: [10.48550/arXiv.2604.06170](https://doi.org/10.48550/arXiv.2604.06170)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1: Overview of the Paper Circle pipeline. Given a user query, Paper Circle builds a paper set from multiple*

Paper Circle는 학술 문헌 발견과 분석을 위한 다중 에이전트 LLM 기반 프레임워크로, Discovery Pipeline과 Analysis Pipeline을 통해 논문 검색, 평가, 구조화된 지식 그래프 생성을 자동화한다.

## Motivation

- **Known**: 과학 문헌의 급증으로 연구자들이 관련 논문을 효율적으로 발견하고 평가하기 어려워지고 있으며, LLM 기반 다중 에이전트 시스템이 사용자 의도 이해와 도구 활용에서 강점을 보이고 있다.
- **Gap**: 기존 자동화 시스템들은 완전 자동화에 초점을 맞추거나 단편적 기능만 제공하며, 재현 가능성(Reproducibility)과 다양한 출력 형식을 동시에 지원하는 통합 플랫폼이 부족하다.
- **Why**: 연구자의 문헌 검토 부담을 줄이고 논문 간 연관성을 파악하며 인간-AI 협업을 통해 더 효율적이고 신뢰할 수 있는 문헌 분석 워크플로우를 제공할 수 있기 때문이다.
- **Approach**: CodeAgent 기반 다중 에이전트 오케스트레이션 위에 (1) 다중 소스 검색 및 다중 기준 점수 매기기 기반의 Discovery Pipeline과 (2) 논문을 타입화된 노드(개념, 방법, 실험 등)를 가진 지식 그래프로 변환하는 Analysis Pipeline을 구현하였다.

## Achievement

![Figure 1](figures/fig1.webp)

*Figure 1: Overview of the Paper Circle pipeline. Given a user query, Paper Circle builds a paper set from multiple*

**다중 소스 통합 검색**: 오프라인 및 온라인 검색을 여러 소스(arXiv, 논문 그래프, 커뮤니티)에서 통합하고 중복 제거
**구조화된 지식 그래프**: 타입화된 노드와 엣지를 가진 동적 지식 그래프 생성으로 그래프 기반 질의응답 지원
**완전 재현 가능성**: JSON, CSV, BibTeX, Markdown, HTML 등 다양한 출력 형식으로 각 에이전트 단계마다 결과물 제공
**다중 평가 메트릭**: Hit rate, MRR, Recall@K 등으로 검색 및 리뷰 생성 성능 벤치마킹
**오픈소스 공개**: 웹사이트 및 깃허브 코드 공개로 재사용성과 투명성 확보

## How

![Figure 2](figures/fig2.webp)

*Figure 2: The main iterative diagram for the paper dis-*

- Intent Classification Agent: 사용자 쿼리를 검색 모드, 학회 필터, 연도 범위로 파싱
- Paper Search Agent: 오프라인/온라인 검색 실행, 결과 병합 및 중복 제거
- Sorting Agent: 최근성, 인용도, 유사성, 신규성, BM25, 크로스 인코더 등 다양한 기준으로 논문 재정렬
- Analysis Agent: 개별 논문을 지식 그래프로 변환하여 개념, 방법, 실험, 그림 등을 타입화된 노드로 표현
- Export Agent: 구조화된 출력을 다양한 형식으로 생성
- State Tracker: 모든 에이전트 단계의 공유 상태를 유지하고 저장소에 영속화

## Originality

- 기존 자동화 시스템과 달리 인간-AI 협업을 위한 '콜라보레이션 워크벤치'로 설계
- 타입화된 노드를 가진 구조화된 지식 그래프로 단순 텍스트 분석을 넘어선 깊이 있는 이해 지원
- 완전한 재현성(deterministic runs)과 다양한 구조화된 출력 형식을 동시에 제공하는 통합 시스템
- 다중 소스 다중 기준 점수 매기기를 통한 다양성 인식 순위 매김(diversity-aware ranking)
- CodeAgent 기반 오케스트레이션으로 각 도구 호출과 다단계 계획이 추적 가능하고 확장 가능

## Limitation & Further Study

- 평가가 제한된 데이터셋에서 수행되어 일반화 가능성 확인 필요
- 매우 큰 규모의 문헌 컬렉션에 대한 확장성 및 성능 영향 미흡
- LLM 모델 성능에 크게 의존하므로 더 약한 모델의 경우 품질 저하 가능
- 사용자 피드백 루프와 지속적 개선 메커니즘에 대한 설명 부족
- 도메인 특화 지식 그래프 스키마 커스터마이제이션 방안 미제시

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: Paper Circle는 학술 문헌 발견과 분석을 위한 포괄적이고 실용적인 다중 에이전트 시스템으로, 재현 가능성과 구조화된 출력을 강조하며 인간 연구자를 증강하는 협업 플랫폼으로서 명확한 가치를 제시한다.

## Related Papers

- 🔗 후속 연구: [[papers/1022_SciSciGPT_advancing_humanAI_collaboration_in_the_science_of/review]] — 과학의 과학 분야에서 인간-AI 협력을 다중 에이전트 시스템으로 확장하여 연구 발견과 분석을 자동화한다.
- 🧪 응용 사례: [[papers/1076_Predicting_research_trends_with_semantic_and_neural_networks/review]] — 의미 네트워크와 신경망을 활용한 연구 트렌드 예측을 다중 에이전트 파이프라인으로 구현하여 실용화한다.
