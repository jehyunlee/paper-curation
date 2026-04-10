---
title: "143_AutoP2C_An_LLM-Based_Agent_Framework_for_Code_Repository_Gen"
authors:
  - "Zijie Lin"
  - "Yiqing Shen"
  - "Qilin Cai"
  - "He Sun"
  - "Jinrui Zhou"
date: "2025.04"
doi: "N/A"
arxiv: ""
score: 4.2
essence: "학술 논문의 텍스트, 다이어그램, 표 등 다중모달 콘텐츠를 자동으로 처리하여 완전히 실행 가능한 코드 저장소를 생성하는 혁신적인 다중에이전트 LLM 프레임워크를 제시한다. 이는 기존의 단순 코드 스니펫 생성을 넘어 연구 논문 구현의 전체 자동화를 목표로 한다."
tags:
  - "cat/Cognitive_AI_Evaluation_and_Benchmarking"
  - "sub/AI_Benchmarking_Taxonomy"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Lin et al._2025_AutoP2C An LLM-Based Agent Framework for Code Repository Generation from Multimodal Content in Acad.pdf"
---

# AutoP2C: An LLM-Based Agent Framework for Code Repository Generation from Multimodal Content in Academic Papers

> **저자**: Zijie Lin, Yiqing Shen, Qilin Cai, He Sun, Jinrui Zhou, Mingjun Xiao | **날짜**: 2025-04-28 | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp) *"Paper-to-Code" (P2C) 작업의 개요: 학술 논문의 다중모달 콘텐츠(텍스트, 이미지, 표)를 처리하여 완전히 실행 가능한 코드 저장소와 설명 다이어그램 생성*

학술 논문의 텍스트, 다이어그램, 표 등 다중모달 콘텐츠를 자동으로 처리하여 완전히 실행 가능한 코드 저장소를 생성하는 혁신적인 다중에이전트 LLM 프레임워크를 제시한다. 이는 기존의 단순 코드 스니펫 생성을 넘어 연구 논문 구현의 전체 자동화를 목표로 한다.

## Motivation

- **Known**: 기존 LLM 기반 코드 생성은 텍스트만 처리하는 단일모달 방식이며, 멀티에이전트 프레임워크는 일반 소프트웨어 개발에만 초점을 맞추고 있음. AutoML은 정해진 워크플로우와 사전정의된 모델에만 의존하여 새로운 아키텍처 구현 불가.

- **Gap**: 학술 논문의 풍부한 시각적 정보(아키텍처 다이어그램, 수학 방정식, 표), 다중파일 저장소 생성, 실제 결과 재현 등을 동시에 다루는 자동화 방법 부재.

- **Why**: ML 연구의 재현성과 실제 응용을 위해 논문을 완전한 코드 저장소로 자동 변환할 필요가 있음. 현재 이는 ML 전문 지식이 필요한 시간 소모적 작업.

- **Approach**: 4단계 다중에이전트 프레임워크(저장소 청사진 추출 → 다중모달 콘텐츠 파싱 → 계층적 작업 분해 → 반복적 피드백 기반 디버깅)로 체계적 자동화.

## Achievement

![Figure 2](figures/fig2.webp) *AutoP2C 프레임워크 개요: (1) 기존 ML 저장소 분석을 통한 표준화된 저장소 청사진 생성, (2) PDF 논문을 통합 표현으로 변환, (3) 구조화된 구현 계획 생성, (4) 반복적 피드백을 통한 실행 가능한 코드 저장소 생성*

1. **혁신적 작업 정의 및 공식화**: "Paper-to-Code"를 다중모달 콘텐츠에서 구조화된 멀티파일 저장소와 설명 시각화를 생성하는 새로운 작업으로 최초 정의. 공식: f_P2C: P → R (P: 텍스트, 이미지, 표 / R: 모듈 집합 + 설명 다이어그램)

2. **높은 실행 성공률**: 8개 논문 벤치마크에서 AutoP2C는 모든 8개 논문의 실행 가능한 코드 저장소 생성 성공(100%), 반면 OpenAI-o1과 DeepSeek-R1은 단 1개 논문만 성공(12.5%). 이는 8배 우월성을 입증.

3. **투명성 향상**: 파일 의존성 그래프(dependency graph) 자동 생성으로 사용자의 코드 이해와 검토 용이성 증대.

## How

- **Stage 1 - Repository Blueprint Extraction**: 기존 ML 저장소 {R₁, R₂, ..., Rₘ}를 LLM으로 분석하여 저장소 아키텍처, 파일 상호의존성, 함수 설계, 클래스 구조의 4개 차원에서 표준 템플릿 T 추출. 전처리 단계로 일회만 수행.

- **Stage 2 - Multimodal Content Parsing**: 
  - OCR(광학 문자 인식)로 텍스트 추출
  - Vision Language Model(VLM)으로 아키텍처 다이어그램 이해
  - LLM으로 수학 방정식과 알고리즘 분석
  - 구조화된 표 데이터 추출 및 설정/결과 파싱
  - 모든 다중모달 요소를 LLM으로 통합 텍스트 표현 P_distilled로 합성

- **Stage 3 - Hierarchical Task Decomposition**: 복잡한 구현 요구사항을 분할정복 방식으로 명확한 인터페이스를 가진 계층적 소작업으로 분해. 각 작업에 책임 에이전트 할당으로 모듈화된 생성 보장.

- **Stage 4 - Iterative Feedback-Driven Debugging**: 
  - 생성된 코드 실행 및 에러 감지
  - 실행 피드백을 기반으로 에러 위치 파악
  - 논문의 다중모달 사양과 일치하도록 반복적 수정
  - 성능과 기능성 검증

## Originality

- **첫 P2C 작업 공식화**: 단순 코드 스니펫 생성 대신 학술 논문의 다중모달 콘텐츠에서 구조화된 멀티파일 저장소 생성이라는 새로운 문제 정의.

- **다중모달 이해의 통합**: 기존 다중에이전트 프레임워크가 텍스트만 처리하는 것과 달리, 다이어그램, 수학 방정식, 표를 통합적으로 처리하는 최초 접근.

- **저장소 수준 코드 생성**: 개별 함수/클래스 생성이 아닌 파일 의존성과 모듈 구조를 고려한 완전한 저장소 생성 자동화.

- **새로운 평가 메트릭**: 구조적 완전성 평가를 위한 2개 신규 메트릭 + 런타임 성능을 결합한 포괄적 평가 체계.

- **투명성 메커니즘**: 파일 의존성 그래프 자동 생성으로 생성 과정의 설명 가능성 향상.

## Limitation & Further Study

- **제한 사항**:
  - 벤치마크 규모: 8개 논문에 불과하여 다양성 제한 가능성. 더 광범위한 ML 분야 및 논문 규모에서 검증 필요.
  - 복잡도 제한: 매우 복잡한 하이브리드 아키텍처나 새로운 패러다임의 논문에 대한 성능 미상.
  - 의존성 관리: 외부 라이브러리 버전 호환성 및 복잡한 환경 설정에 대한 자동화 정도가 명확하지 않음.
  - 수렴성: 반복적 디버깅이 항상 수렴하는지, 무한 루프 가능성 미분석.

- **후속 연구**:
  - 다양한 ML 도메인(자연어처리, 컴퓨터 비전, 강화학습 등)의 더 큰 벤치마크 구축.
  - 매개변수 최적화, 하이퍼파라미터 튜닝 자동화 확대.
  - 논문의 실험 환경 재현(특정 CUDA 버전, 하드웨어 설정 등) 수준 향상.
  - 실시간 상호작용형 프로토타입으로 사용자 피드백 통합.

## Evaluation

- **Novelty (독창성)**: 4.5/5
  - P2C라는 새로운 작업 정의와 다중모달 이해의 체계적 통합이 혁신적. 다만 개별 구성 요소(VLM, 다중에이전트)는 기존 기술 활용.

- **Technical Soundness (기술적 타당성)**: 4/5
  - 4단계 파이프라인이 논리적이고 체계적. 다만 반복적 디버깅의 수렴 조건, 복잡한 의존성 처리의 완전성 논증 부족.

- **Significance (중요도)**: 4.5/5
  - ML 재현성 위기와 연구 재현 자동화라는 중요한 문제를 다룸. 8배 성능 향상으로 실무 적용 가치 높음. 다만 평가 규모가 소규모인 점은 일반화 신뢰성 약화.

- **Clarity (명확성)**: 4/5
  - 문제 정의와 프레임워크 구조가 명확하게 제시됨. 각 단계의 구체적 구현 방법(특히 Stage 2-3)은 본문 제한으로 일부 불명확.

- **Overall (종합)**: 4.2/5

**총평**: AutoP2C는 학술 논문의 자동 코드화라는 실제적이고 중요한 문제를 다중모달 이해와 다중에이전트 협력으로 효과적으로 해결한 혁신적 연구이다. 기존 방법 대비 8배 우월한 성공률은 실무적 가치를 입증하나, 벤치마크 규모 확대와 복잡한 시나리오에 대한 검증이 필요하며, 반복적 디버깅 메커니즘의 이론적 보장도 강화되어야 한다.

## Related Papers

- 🔄 다른 접근: [[papers/232_CodePDE_An_Inference_Framework_for_LLM-driven_PDE_Solver_Gen/review]] — 논문에서 코드 생성이라는 동일 목표를 PDE와 일반 저장소 관점에서 접근
- 🔗 후속 연구: [[papers/145_Autoreproduce_Automatic_ai_experiment_reproduction_with_pape/review]] — 논문 기반 실험 재현이 코드 저장소 생성으로 확장됨
- 🔄 다른 접근: [[papers/232_CodePDE_An_Inference_Framework_for_LLM-driven_PDE_Solver_Gen/review]] — 논문에서 코드로의 자동 변환이라는 동일한 목표를 PDE와 일반 코드 관점에서 접근
