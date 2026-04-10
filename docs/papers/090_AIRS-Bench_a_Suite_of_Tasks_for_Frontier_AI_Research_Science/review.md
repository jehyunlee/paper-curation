---
title: "090_AIRS-Bench_a_Suite_of_Tasks_for_Frontier_AI_Research_Science"
authors:
  - "Alisia Lupidi"
  - "Bhavul Gauri"
  - "Thomas Simon Foster"
  - "Bassel Al Omari"
  - "Despoina Magka"
date: "2026"
doi: "10.48550/ARXIV.2602.06855"
arxiv: ""
score: 0
essence: "LLM 기반 AI 연구 에이전트의 종합적 성능을 평가하기 위해, 최신 머신러닝 논문에서 추출한 20개의 다양한 작업으로 구성된 표준화된 벤치마크 AIRS-Bench를 제시한다. 본 벤치마크는 아이디어 생성부터 실험 분석 및 반복적 개선에 이르는 완전한 연구 생명주기를 평가하며, 현재 프론티어 LLM 모델들은 4개 작업에서만 인간 수준의 최고 성능(SOTA)을 초과하고 대부분의 작업에서 여전히 개선 여지가 있음을 보여준다."
tags:
  - "cat/Cognitive_AI_Evaluation_and_Benchmarking"
  - "sub/AI_Benchmarking_Taxonomy"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Lupidi et al._2026_AIRS-Bench a Suite of Tasks for Frontier AI Research Science Agents.pdf"
---

# AIRS-Bench: a Suite of Tasks for Frontier AI Research Science Agents

> **저자**: Alisia Lupidi, Bhavul Gauri, Thomas Simon Foster, Bassel Al Omari, Despoina Magka, Alberto Pepe, Alexis Audran-Reiss, Muna Aghamelu, Nicolas Baldwin, Lucia Cipolina-Kun, Jean-Christophe Gagnon-Audet, Chee Hau Leow, Sandra Lefdal, Hossam Mossalam, Abhinav Moudgil, Saba Nazir, Emanuel Tewolde, Isabel Urrego, Jordi Armengol Estape, Amar Budhiraja, Gaurav Chaurasia, Abhishek Charnalia, Derek Dunfield, Karen Hambardzumyan, Daniel Izcovich, Martin Josifoski, Ishita Mediratta, Kelvin Niu, Parth Pathak, Michael Shvartsman, Edan Toledo, Anton Protopopov, Roberta Raileanu, Alexander Miller, Tatiana Shavrina, Jakob Foerster, Yoram Bachrach | **날짜**: 2026 | **DOI**: [10.48550/ARXIV.2602.06855](https://doi.org/10.48550/ARXIV.2602.06855)

---

## Essence

LLM 기반 AI 연구 에이전트의 종합적 성능을 평가하기 위해, 최신 머신러닝 논문에서 추출한 20개의 다양한 작업으로 구성된 표준화된 벤치마크 AIRS-Bench를 제시한다. 본 벤치마크는 아이디어 생성부터 실험 분석 및 반복적 개선에 이르는 완전한 연구 생명주기를 평가하며, 현재 프론티어 LLM 모델들은 4개 작업에서만 인간 수준의 최고 성능(SOTA)을 초과하고 대부분의 작업에서 여전히 개선 여지가 있음을 보여준다.

## Motivation

- **Known**: LLM의 능력이 과학 연구 자동화에 잠재력을 가지고 있으며, 테스트 타임 컴퓨팅(test-time compute)의 증가와 스캐폴드(scaffold) 기법을 통해 더욱 강력한 에이전트 구축이 가능하다는 것이 알려져 있다.

- **Gap**: 현존하는 AI 연구 에이전트 평가 벤치마크는 데이터 오염(data contamination), 환경 표준화 부재, 높은 계산 비용, 재현성 문제 등으로 인해 에이전트의 진정한 연구 능력을 정확히 측정하지 못하고 있다. 또한 베이스라인 코드 제공 여부, 과학적 방법론의 완전성(가설 생성, 구현, 실험, 분석), 평가 메트릭의 일관성 등이 벤치마크마다 상이하다.

- **Why**: ML 발전이 벤치마크-중심 패러다임으로 이루어져온 만큼, AI 연구 에이전트 개발도 견고한 표준화 평가 체계를 필요로 한다. 현재의 평가 위기(evaluation crisis)를 극복하려면 데이터 오염이 없고, 환경이 표준화되며, 완전한 연구 사이클을 평가하는 통합 벤치마크가 필수적이다.

- **Approach**: 
  1. 최첨단 ML 논문 20개에서 추출한 다양한 도메인의 작업으로 구성
  2. 베이스라인 코드 미제공으로 에이전트의 독립적 문제 해결 능력 평가
  3. {문제(problem), 데이터셋(dataset), 메트릭(metric)} 표준화 구조 정의
  4. 순차(sequential) 및 병렬(parallel) 스캐폴드를 지원하는 통일된 평가 체계 구축
  5. 여러 프론티어 모델(GPT-4o, o3-mini, CWM, Devstral 등)과 하네스(AIRA-dojo, MLGym)로 종합 평가

## Achievement

![Figure 1](figures/fig1.webp)
*그림 1: AIRS-Bench 작업 예시. 각 작업은 {문제, 데이터셋, 메트릭} 삼중쌍으로 명시되며, 에이전트는 전체 작업 명세를 받고 테스트 레이블 파일에 대한 예측을 생성하는 솔루션을 개발한다.*

1. **표준화된 벤치마크 구축**: 
   - 20개의 NLP, 수학, 코드, 생화학, 시계열 예측 작업으로 구성된 균형 잡힌 벤치마크 개발
   - 데이터 오염 방지를 위해 베이스라인 코드 미제공
   - 아이디어 생성(H), 구현(I), 실험(E), 분석(A) 4단계 과학적 방법론 완전 포괄

2. **종합적 성능 분석**:
   - 14개의 에이전트 평가를 통해 명확한 성능 차등화 확인
   - 4개 작업에서만 인간 SOTA 초과, 16개 작업에서 미달
   - 인간 SOTA를 초과한 경우에도 이론적 성능 상한(theoretical ceiling)에 미달
   - 벤치마크가 포화되지 않았으며 상당한 개선 여지 존재

3. **평가 방법론 정립**:
   - 유효 제출 비율(valid submission rate), 정규화 성능 점수(normalized performance score), Elo 등급제 도입
   - 다양한 메트릭을 통한 다각적 성능 평가
   - 시드와 작업 전반에 걸친 통계적으로 견고한 집계 방식

4. **오픈소스 기여**:
   - AIRS-Bench 작업 정의 및 평가 코드 공개
   - 자동화된 과학 연구 개발 가속화에 기여

## How

![Table 1](figures/table1.webp)
*표 1: AIRS-Bench와 14개 인기 에이전트 AI 연구 벤치마크의 주요 평가 차원 비교. AIRS-Bench는 장기 작업 수행, 완전한 과학적 방법론 포괄, 높은 GPU 요구, 베이스라인 코드 미제공으로 차별화된다.*

- **작업 설계 및 검증**:
  - 17개의 최신 ML 논문에서 작업 추출
  - 반자동 소싱, 생성, 검토, 검증 파이프라인 구축
  - 인간 검토를 통한 품질 보장

- **에이전트 정의**:
  - 에이전트 = LLM + 스캐폴드
  - LLM: 자체 호스팅 OSS 모델 또는 API 기반 모델
  - 스캐폴드: 솔루션 공간의 체계적 탐색을 위한 조율 계층
  - 순차 스캐폴드(ReAct): 선형 피드백 루프 구현
  - 병렬 스캐폴드(MCTS): 트리 구조를 활용한 모집단 기반 탐색

- **평가 설계**:
  1. 모든 에이전트에서 비교 가능한 실행 환경 구성 (인프라 문제 고려)
  2. 정규화 변환: 0.0 = 가장 약한 유효 솔루션, 1.0 = 인간 SOTA
  3. 다중 시드를 통한 통계적 신뢰성 확보
  4. 14개 에이전트 조합 평가:
     - 모델: CWM, GPT-4o, gpt-oss-20b, gpt-oss-120b, o3-mini, Devstral
     - 하네스: AIRA-dojo, MLGym

- **작업 분포**:
  - 7가지 범주: Code, Math, NLP, Time Series, Bioinformatics, Graph, Chemistry
  - 각 범주가 실제 연구 문제의 실제적 도전을 대표하도록 구성

## Originality

- **벤치마크 설계의 혁신성**:
  - 베이스라인 코드 미제공 방식으로 에이전트의 독립적 문제 해결 능력 신규 평가
  - 과학적 방법론의 4단계를 모두 포괄하는 첫 종합 벤치마크
  - 환경 표준화 및 데이터 오염 방지에 대한 체계적 접근

- **평가 방법론의 창신성**:
  - 정규화 기법을 통한 이질적 작업 간의 공정한 성능 비교
  - 다중 메트릭(유효 제출율, 정규화 점수, Elo)을 통한 다층적 분석
  - 테스트-타임 컴퓨팅의 영향을 분석하기 위한 순차 vs 병렬 스캐폴드 비교

- **스케일과 다양성**:
  - 20개 작업으로 기존 벤치마크 대비 충분한 규모 (비교: MLGym-Bench 13개, ML-Agent-Bench 13개)
  - 7개 도메인에 걸친 광범위한 커버리지
  - 14개 에이전트 조합의 광범위한 평가

- **실무적 가치**:
  - 오픈소스 공개로 커뮤니티의 자유로운 재사용 및 확장 가능
  - 작업 표준 형식({문제, 데이터셋, 메트릭})을 통해 새로운 작업 추가의 민주화

## Limitation & Further Study

- **벤치마크 포화도의 제한**:
  - 20개 작업이라는 크기 제약으로 인해 일부 연구 영역(예: 가설 생성, 문헌 검토)이 충분히 대표되지 않을 가능성
  - 장기 작업(>12시간)의 계산 비용으로 인한 광범위한 하이퍼파라미터 탐색 제한

- **평가의 일관성 문제**:
  - 작업별로 이상적인 솔루션 수행 방식이 상이할 수 있어 일괄적 평가 메트릭의 해석에 주의 필요
  - 환경 변수(하드웨어, 타이밍, 네트워크)의 영향 완전 제거 불가

- **에이전트 설계의 제약**:
  - 현재 정의(LLM + 스캐폴드)로 제한되어 있어, 더 복잡한 하이브리드 시스템이나 멀티에이전트 협력 모형 평가 부재
  - 도구 사용(tool use) 능력의 균등한 평가 어려움

- **후속 연구 방향**:
  1. 장기 다중 라운드 협상 작업, 논문 작성 평가 등 추가 작업 개발
  2. 에이전트가 발견한 혁신적 솔루션에 대한 정성적 분석 심화
  3. 계산 효율성(낮은 GPU 리소스)을 갖춘 작업 추가
  4. 실시간 온라인 학습(online learning) 작업 포함
  5. 에이전트의 실패 사례에 대한 원인 분석 프레임워크 개발

## Evaluation

- **Novelty**: 4.5/5
  - 베이스라인 코드 미제공 방식과 완전한 과학적 사이클 평가는 신기함
  - 하지만 개별 평가 방법론(정규화, Elo)은 기존 기법의 조합

- **Technical Soundness**: 4/5
  - 표준화 절차와 통계적 엄밀성이 우수함
  - 환경 변수 제어 시도가 체계적이나, 완전한 제어는 불가능한 점 인정 필요
  - 정규화 방법의 수학적 정당성이 명확히 제시되어야 함

- **Significance**: 4.5/5
  - AI 연구 자동화 분야의 성숙을 위한 중요한 기반 제공
  - 오픈소스 공개로 높은 커뮤니티 영향력 예상
  - 다만 4개 작업만 인간 SOTA 초과라는 결과의 실제적 의미 해석 필요

- **Clarity**: 4.5/5
  - 벤치마크 구조, 작업 설계, 평가 방법론이 명

## Related Papers

- 🔄 다른 접근: [[papers/544_Mldebugging_Towards_benchmarking_code_debugging_across_multi/review]] — AI 에이전트의 연구 생명주기 전체 평가와 다중 라이브러리 코드 디버깅 평가 모두 복잡한 AI 능력을 측정하지만 평가 범위가 다르다.
- 🏛 기반 연구: [[papers/064_Agentic_AI_for_Scientific_Discovery_A_Survey_of_Progress_Cha/review]] — 과학 발견을 위한 에이전틱 AI 체계가 프론티어 AI 연구 과학 에이전트의 벤치마크 설계 기반을 제공한다.
- 🧪 응용 사례: [[papers/493_Litllm_A_toolkit_for_scientific_literature_review/review]] — 과학 문헌 리뷰 자동화가 AI 연구 과학 에이전트의 실제 연구 워크플로우 중 하나인 문헌 분석에 적용된다.
- 🏛 기반 연구: [[papers/724_SciHorizon_Benchmarking_AI-for-Science_Readiness_from_Scient/review]] — 프론티어 AI 연구 과학을 위한 작업 모음이 SciHorizon의 평가 체계 설계에 기반을 제공한다.
- 🔄 다른 접근: [[papers/544_Mldebugging_Towards_benchmarking_code_debugging_across_multi/review]] — 프론티어 AI 연구 과학 에이전트 평가와 다중 라이브러리 코드 디버깅 평가 모두 AI의 복잡한 기술적 문제 해결 능력을 측정하지만 접근법이 다르다.
- 🔗 후속 연구: [[papers/064_Agentic_AI_for_Scientific_Discovery_A_Survey_of_Progress_Cha/review]] — 프론티어 AI 연구 과학 에이전트 평가가 과학 발견을 위한 에이전틱 AI의 실제 성능 측정으로 확장된다.
- 🏛 기반 연구: [[papers/493_Litllm_A_toolkit_for_scientific_literature_review/review]] — 프론티어 AI 연구 과학 에이전트 평가에서 문헌 분석과 리뷰 생성이 중요한 구성 요소로서 기반을 제공한다.
- 🏛 기반 연구: [[papers/706_SciBench_Evaluating_College-Level_Scientific_Problem-Solving/review]] — 최전선 AI 연구 과학을 위한 기초적 벤치마크 역할을 한다.
