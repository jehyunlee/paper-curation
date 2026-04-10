---
title: "600_Paper2Web_Lets_Make_Your_Paper_Alive"
authors:
  - "Yuhang Chen"
  - "Tianpeng Lv"
  - "Siyi Zhang"
  - "Yixiang Yin"
  - "Yao Wan"
date: "2025.10"
doi: "N/A"
arxiv: ""
score: 4.2
essence: "학술 논문을 정적인 PDF 형식에서 벗어나 대화형(interactive) 멀티미디어 웹사이트로 변환하는 작업을 새롭게 정의하고, 이를 위한 벤치마크 데이터셋과 평가 프레임워크를 제시한다. 제안된 PWAgent는 반복적 개선을 통해 기존 방법들을 큰 폭으로 능가한다."
tags:
  - "cat/LLM-Based_Scientific_Reasoning"
  - "sub/Scientific_Literature_Analysis"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Chen et al._2025_Paper2Web Let's Make Your Paper Alive!.pdf"
---

# Paper2Web: Let's Make Your Paper Alive!

> **저자**: Yuhang Chen, Tianpeng Lv, Siyi Zhang, Yixiang Yin, Yao Wan, Philip S. Yu, Dongping Chen | **날짜**: 2025-10-17 | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp)
*학술 논문을 다양한 형식(슬라이드, 포스터, 비디오, 웹사이트, AI 어시스턴트)으로 변환하는 통합 플랫폼의 일부로서 Paper2Web 위치*

학술 논문을 정적인 PDF 형식에서 벗어나 대화형(interactive) 멀티미디어 웹사이트로 변환하는 작업을 새롭게 정의하고, 이를 위한 벤치마크 데이터셋과 평가 프레임워크를 제시한다. 제안된 PWAgent는 반복적 개선을 통해 기존 방법들을 큰 폭으로 능가한다.

## Motivation

- **Known**: 
  - PDF 형식의 학술 논문은 정적 텍스트와 이미지만 제공하며 상호작용성과 멀티미디어 콘텐츠 지원이 제한적임
  - Paper2Poster, PresentAgent 등 기존 변환 방법들은 세부 정보를 버리거나 멀티미디어 이점을 간과함
  - arXiv HTML, alphaXiv 등 기존 웹페이지 생성 시도는 레이아웃 오류, 중복 텍스트, 제한된 상호작용성 문제 존재

- **Gap**: 
  - 핵심 텍스트 지식을 보존하면서 동시에 멀티미디어를 통합하고 대화형 요소를 갖춘 웹페이지 생성 방법의 부재
  - 이 작업을 평가하기 위한 포괄적 벤치마크 데이터셋 및 평가 메트릭 부재

- **Why**: 
  - 웹기반 학술 정보 공유는 PDF 형식보다 접근성과 가독성이 높고 다양한 커뮤니티 확산에 유리
  - 적절한 공간 구성으로 멀티미디어와 대화형 요소를 조화롭게 배치하는 것이 중요

- **Approach**: 
  - PAPER2WEB 데이터셋 구축(논문-웹페이지 쌍 10,716개)
  - 다차원 평가 프레임워크 개발(연결성, 완전성, LLM-as-a-Judge, PaperQuiz)
  - PWAgent: MCP(Model Context Protocol) 기반 멀티에이전트 파이프라인으로 반복적 개선

## Achievement

![Figure 2](figures/fig2.webp)
*현재 학술 웹페이지 생성의 문제점: (a) arXiv HTML 버전의 이미지 오버플로우, (b) alphaXiv 생성 웹페이지의 이미지-텍스트 불균형*

![Figure 3](figures/fig3.webp)
*파레토 프론트 비교: PWAgent가 적정 수준의 비용으로 최고 품질 달성*

1. **데이터셋 구축**: ICML, NeurIPS, WWW, ICLR 등 주요 AI 컨퍼런스(2020-2025)에서 10,716개의 논문-웹페이지 쌍을 수집하고 특성 분석(정적 42.4%, 멀티미디어 38.9%, 대화형 9.8%)

2. **평가 프레임워크**: 
   - 규칙기반 메트릭(연결성, 완전성) 
   - 인간검증 MLLM-as-a-Judge(대화형성, 미학성, 정보성)
   - PaperQuiz(웹페이지 스크린샷에서의 지식 전이 평가)

3. **성능 개선**: 
   - 연결성/완전성에서 약 12% 평균 개선
   - arXiv HTML 대비 28% 향상
   - MLLM-as-a-Judge에서 18% 평균 개선
   - 가장 강력한 end-to-end 베이스라인 대비 3배 성능 달성

## How

![Figure 4](figures/fig4.webp)
*데이터 수집 파이프라인: 논문 메타데이터 수집 → 프로젝트 웹사이트 검색 → LLM/인간 판별을 통한 필터링*

**PWAgent 파이프라인**:

- **단계 1: 논문 분해 및 자산화**
  - 논문을 구조화된 자산(텍스트, 이미지, 링크, 실행 가능한 구성요소)으로 분해
  - 통합 스키마 하에 자원 정렬

- **단계 2: MCP 기반 자원 저장소 구축**
  - Model Context Protocol을 통한 의미론적 자원 정렬
  - 관계형 메타데이터 및 표준화된 도구 노출

- **단계 3: 콘텐츠 인식 공간 할당**
  - 각 자산의 공간적 풍경(spatial footprint) 추정
  - 임시 레이아웃 예산 할당으로 렌더링 및 네비게이션 가이드

- **단계 4: 에이전트 기반 반복적 개선**
  - 초기 웹사이트 초안 생성
  - 렌더링된 뷰 검사
  - 도구 호출을 통한 대상화된 편집(시각적 불균형 수정, 정보 계층 강화, 멀티미디어 앵커링)
  - 글로벌 평가와 국소적 조정의 반복 루프

## Originality

- **새로운 작업 정의**: 학술 논문→대화형 웹사이트 변환 작업을 체계적으로 정의한 첫 사례

- **대규모 벤치마크 데이터셋**: 10,716개의 논문-웹페이지 쌍으로 이루어진 첫 종합 데이터셋 구축

- **다차원 평가 메트릭**: 
  - 웹페이지 상호작용성을 측정하는 첫 메트릭
  - 지식 보존을 평가하는 PaperQuiz(장황성 패널티 포함)
  - 인간 선호도와 잘 정렬된 자동 평가 메트릭

- **MCP 기반 혁신**: Model Context Protocol을 학술 웹페이지 생성에 처음 적용하여 구조화된 자원 관리 실현

- **반복적 개선 프레임워크**: 스크린샷과 HTML 파편 간 연결을 통한 정밀한 시각적 편집 메커니즘

## Limitation & Further Study

- **데이터셋 편향**: AI 논문 중심으로 수집되어 다른 학문 분야의 웹사이트 특성이 제한적으로 반영될 수 있음

- **평가 범위**: PaperQuiz는 정적 스크린샷 기반이므로 동적 상호작용성을 완전히 평가하지 못함

- **확장성**: 매우 긴 논문이나 복잡한 구조의 논문에 대한 성능 평가 부족

- **비용-품질 트레이드오프**: Pareto-front 달성하였으나 고비용 시나리오에서의 추가 개선 여지 존재

- **후속 연구**:
  - 다양한 학문 분야 확대를 위한 크로스 도메인 평가
  - 실제 사용자 상호작용 데이터를 통한 평가 강화
  - 언어별 다국어 웹페이지 생성 지원
  - 학생, 초기 연구자 등 다양한 사용자 그룹의 요구사항 반영

## Evaluation

- **Novelty**: 4.5/5
  - 웹페이지 생성 작업 정의와 대규모 벤치마크는 창의적이나, 개별 기술 요소는 기존 방법 활용

- **Technical Soundness**: 4/5
  - MCP 기반 파이프라인과 반복적 개선 메커니즘은 견고하나, 평가 메트릭 중 일부(PaperQuiz)의 타당성 검증 필요

- **Significance**: 4.5/5
  - 학술 정보 공유의 중요한 문제를 다루고 실용적 솔루션 제시하며, 관련 커뮤니티에 큰 영향 기대

- **Clarity**: 4/5
  - 전반적으로 명확하나, PWAgent의 반복적 개선 루프 세부 사항과 MCP 도구 명세 설명 강화 필요

- **Overall**: 4.2/5

**총평**: Paper2Web은 학술 논문의 웹기반 공유라는 중요하면서도 미해결된 문제를 체계적으로 정의하고, 포괄적인 벤치마크 데이터셋과 다차원 평가 프레임워크를 제공한다는 점에서 상당한 가치가 있다. PWAgent의 성능 개선도 인상적이나, 기술적 독창성 측면에서는 기존 방법들의 조합 수준이므로 전체적으로는 높은 수준의 실질적 기여를 하는 작업으로 평가된다.

## Related Papers

- 🏛 기반 연구: [[papers/579_Nsf-scify_Mining_the_nsf_awards_database_for_scientific_clai/review]] — 대규모 과학적 주장 데이터셋이 논문 웹사이트 변환의 콘텐츠 기반 제공
- 🔗 후속 연구: [[papers/336_FigCaps-HF_A_Figure-to-Caption_Generative_Framework_and_Benc/review]] — 과학 도표 캡션 생성을 논문 전체의 멀티미디어 변환으로 확장한 연구
- 🔄 다른 접근: [[papers/597_P2p_Automated_paper-to-poster_generation_and_fine-grained_be/review]] — PDF를 웹사이트로 vs 논문을 포스터로 변환하는 유사하지만 다른 접근법
- 🔗 후속 연구: [[papers/601_PaperBanana_Automating_Academic_Illustration_for_AI_Scientis/review]] — 논문 일러스트레이션 자동화를 전체 웹사이트 변환으로 확장한 발전된 형태
- 🔗 후속 연구: [[papers/579_Nsf-scify_Mining_the_nsf_awards_database_for_scientific_clai/review]] — 과학적 주장 데이터셋을 활용한 논문의 멀티미디어 변환 및 상호작용화
- 🔗 후속 연구: [[papers/773_Stealing_creators_workflow_A_creator-inspired_agentic_framew/review]] — 논문을 웹으로 변환하는 Paper2Web 시스템이 SciTalk의 과학 논문 콘텐츠 변환 아이디어를 다른 매체로 확장한 사례를 제공한다.
