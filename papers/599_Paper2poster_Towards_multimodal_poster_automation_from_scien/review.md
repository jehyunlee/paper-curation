---
title: "599_Paper2poster_Towards_multimodal_poster_automation_from_scien"
authors:
  - "Wei Pang"
  - "Kevin Qinghong Lin"
  - "Xiangru Jian"
  - "Xi He"
  - "Philip H. S. Torr"
date: "2025"
doi: "N/A"
arxiv: ""
score: 4.2
essence: "본 논문은 과학 논문을 단일 페이지 학술 포스터로 자동 변환하는 첫 번째 벤치마크와 평가 지표 집합을 제시하며, 시각적-언어적 피드백 루프를 갖춘 다중 에이전트 파이프라인(PosterAgent)을 제안한다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Table_Caption_Generation"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Pang et al._2025_Paper2poster Towards multimodal poster automation from scientific papers.pdf"
---

# Paper2poster: Towards multimodal poster automation from scientific papers

> **저자**: Wei Pang, Kevin Qinghong Lin, Xiangru Jian, Xi He, Philip H. S. Torr | **날짜**: 2025 | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp) *과학 논문에서 포스터를 생성하기 위한 두 가지 핵심 도전 과제: (좌) PosterAgent를 통한 포스터 생성 방법, (우) Paper2Poster 벤치마크를 통한 평가 방법*

본 논문은 과학 논문을 단일 페이지 학술 포스터로 자동 변환하는 첫 번째 벤치마크와 평가 지표 집합을 제시하며, 시각적-언어적 피드백 루프를 갖춘 다중 에이전트 파이프라인(PosterAgent)을 제안한다.

## Motivation

- **Known**: 슬라이드 자동 생성(PPTAgent, D2S 등)은 상당히 발전했으나, 학술 포스터 생성은 미개발 상태

- **Gap**: 포스터는 전체 논문을 단일 페이지에 압축해야 하므로 슬라이드보다 훨씬 복잡함. 특히 (i) 긴 멀티모달 문맥(20K+ 토큰), (ii) 텍스트-그래픽 긴밀한 인터리빙, (iii) 공간 제약 조건 만족이 도전 과제

- **Why**: VLM/LLM만으로는 공간 레이아웃 추론, 논리적 흐름 유지, 가독성 보장이 어려움. 명시적 시각적 피드백 필요

- **Approach**: (1) 100개 논문-포스터 쌍 벤치마크 구축, (2) 시각적 품질, 텍스트 일관성, VLM 판정관(VLM-as-judge), PaperQuiz(포스터가 논문 핵심을 얼마나 잘 전달하는지 평가) 4가지 평가 지표 제안, (3) Parser-Planner-Painter-Commenter 다중 에이전트 파이프라인 개발

## Achievement

![Figure 3](figures/fig3.webp) *Paper2Poster 평가 프레임워크: 시각적 품질, 텍스트 일관성, VLM 판정관을 통한 종합 평가, PaperQuiz를 통한 독자 이해도 시뮬레이션*

1. **첫 번째 벤치마크 구축**: POSTERSUM 데이터셋을 기반으로 2022-2024년 ICML, NeurIPS, ICLR 논문 100개와 저자가 설계한 포스터 쌍 수집. 평균 22.6페이지, 20,370.3 토큰의 논문을 774.1단어, 1,416.2 토큰으로 14.4배 압축

2. **혁신적 PaperQuiz 지표**: LLM이 자동 생성한 다지선다형 문제로 VLM 리더(학생, 교수 등 다양한 전문성 수준)가 포스터만으로 논문 내용을 파악할 수 있는지 평가—인간 평가와 높은 상관관계

3. **성능 우수성**: Qwen-2.5 기반 오픈소스 모델이 GPT-4o 기반 멀티에이전트 시스템을 거의 모든 지표에서 뛰어넘으면서 87% 적은 토큰 사용(비용 $0.005)

4. **품질 인사이트**: 
   - GPT-4o는 시각적으로는 매력적이나 텍스트 노이즈 많음 및 PaperQuiz 성능 낮음
   - 인간 포스터의 주요 강점은 시각적 의미론(visual semantics)을 통한 소통
   - Reader Engagement가 심미적 병목

## How

![Figure 4](figures/fig4.webp) *PosterAgent 파이프라인: Parser(논문→자산 라이브러리), Planner(의미적 정렬 및 레이아웃 생성), Painter-Commenter 루프(렌더링 및 VLM 피드백)*

**PosterAgent 3단계 구조**:

1. **Parser (자산 추출)**
   - PDF 논문을 섹션별 텍스트 요약 및 추출된 figure/table의 자산 라이브러리로 변환

2. **Planner (레이아웃 설계)**
   - 각 섹션 요약과 시각 자산을 의미론적으로 매칭
   - 이진 트리(binary-tree) 레이아웃 생성
   - 콘텐츠 길이 추정으로 패널 할당, 읽기 순서 및 공간 균형 보존

3. **Painter-Commenter 루프 (반복 개선)**
   - **Painter**: 섹션-figure 쌍을 간결한 bullet point로 변환 후 python-pptx로 드래프트 렌더링
   - **Commenter**: VLM이 확대 참조 프롬프트로 텍스트 오버플로우, 공간 정렬 피드백 제공
   - 피드백을 Painter에 반영하여 수렴할 때까지 반복

**평가 프레임워크**:
- 시각적 유사성(Visual Similarity): 생성 포스터 vs 인간 포스터
- Figure 관련성(Figure Relevance): 선택된 figure의 적절성
- 텍스트 Perplexity (PPL): 언어 유창성
- VLM-as-Judge: 6가지 세분화된 심미적/정보 기준 점수
- PaperQuiz: 다양한 VLM 리더의 정답률

## Originality

- **최초 벤치마크**: 학술 포스터 자동 생성을 위한 첫 번째 체계적 벤치마크 및 평가 지표 제안

- **혁신적 PaperQuiz**: 포스터의 본질적 역할(저자-독자 간 지식 전달)을 정량화하는 새로운 평가 방식

- **시각적 피드백 루프**: VLM을 단순 판정관이 아닌 반복적 개선 루프의 일부로 통합한 아키텍처

- **효율성과 해석가능성**: 오픈소스 모델로 GPT-4o를 능가하면서 비용과 토큰 효율성 크게 개선

- **멀티모달 문맥 압축**: 텍스트와 시각 요소의 의미론적 정렬을 유지하면서 14.4배 압축하는 구조화된 접근

## Limitation & Further Study

- **데이터셋 규모**: 100개 쌍은 심층 학습 기반 모델 학습에는 제한적. 더 큰 규모 데이터셋 수집 필요

- **AI 분야 중심**: 현재 AI 논문에만 초점. 다른 과학 분야(생물학, 화학, 의학)로 확장성 미확인

- **자동 평가의 한계**: VLM-as-judge가 완전히 객관적이지 않을 수 있음. 대규모 인간 평가 보충 필요

- **후속 연구**:
  - 엔드-투-엔드 학습 가능 포스터 생성 모델 개발
  - 다양한 학문 분야로 벤치마크 확대
  - 포스터의 시각적 의미론을 더 잘 활용하는 설계 자동화
  - 실시간 대화형 포스터 생성 시스템

## Evaluation

- **Novelty**: 4.5/5
  - 첫 번째 공식 벤치마크와 종합적 평가 지표 제시가 매우 참신
  - PaperQuiz는 실질적 가치 있는 새로운 평가 방식
  - 다중 에이전트 파이프라인 자체는 기존 기법의 조합이나 문제에 잘 맞춤

- **Technical Soundness**: 4/5
  - 파이프라인 설계는 논리적이고 검증됨
  - VLM 피드백 루프의 수렴성 분석 부재
  - Parser의 자산 추출 품질에 대한 상세한 분석 부족

- **Significance**: 4.5/5
  - 학술 포스터 자동화는 과학 소통에 실질적 기여
  - 벤치마크는 향후 연구의 기초 제공
  - 비용 효율성(토큰 87% 감소)의 실제 영향 크나, 아직 소수 논문 도메인에 한정

- **Clarity**: 4/5
  - 논문 구조와 그림이 명확하고 잘 조직됨
  - 일부 기술적 세부사항(VLM 프롬프팅 전략, Painter 코드 생성 상세)이 부분적으로만 설명됨
  - 데이터셋 구축 과정과 정제 기준이 충분히 상세함

- **Overall**: 4.2/5

**총평**: 본 논문은 학술 포스터 자동 생성이라는 도전적이고 실용적인 문제에 처음으로 체계적으로 접근한 의미 있는 작업으로, 신뢰할 수 있는 벤치마크와 혁신적인 PaperQuiz 지표를 제공하며, 실용성 높은 PosterAgent 파이프라인으로 강력한 결과를 달성했다. 다만 데이터셋 규모 확대, 다양한 학문 분야 적용, 그리고 자동 평가 지표의 보완이 향후 필요하다.

## Related Papers

- 🔄 다른 접근: [[papers/787_Tablemaster_A_recipe_to_advance_table_understanding_with_lan/review]] — 둘 다 테이블과 관련된 멀티모달 작업을 다루지만 하나는 포스터 생성, 다른 하나는 테이블 이해에 중점을 둠
- 🏛 기반 연구: [[papers/336_FigCaps-HF_A_Figure-to-Caption_Generative_Framework_and_Benc/review]] — 과학적 그림에 대한 캡션 생성 연구가 논문을 포스터로 변환하는 멀티모달 자동화의 기초적 접근을 제공함
- 🔗 후속 연구: [[papers/597_P2p_Automated_paper-to-poster_generation_and_fine-grained_be/review]] — 논문을 포스터로 변환하는 작업을 자동화된 Paper-to-Poster 생성과 세밀한 벤치마킹으로 확장함
- 🔄 다른 접근: [[papers/787_Tablemaster_A_recipe_to_advance_table_understanding_with_lan/review]] — 둘 다 테이블과 관련된 멀티모달 작업을 다루지만 하나는 테이블 이해, 다른 하나는 포스터 생성에 중점을 둠
