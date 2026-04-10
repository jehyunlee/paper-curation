---
title: "671_Researchcodebench_Benchmarking_llms_on_implementing_novel_ma"
authors:
  - "Tianyu Hua"
  - "Harper Hua"
  - "Violet Xiang"
  - "Benjamin Klieger"
  - "Sang T. Truong"
date: "2025"
doi: "arXiv:2506.02314v1"
arxiv: ""
score: 4.4
essence: "최신 기계학습 연구 논문에서 제시된 새로운 아이디어를 실행 가능한 코드로 변환하는 LLM의 능력을 평가하는 벤치마크로, 2024-2025년 상위 학회(NeurIPS, ICLR, CVPR) 논문 20개로부터 구성된 212개의 코딩 챌린지를 통해 현재 최고 성능 LLM도 40% 미만의 성공률을 보임을 입증한다."
tags:
  - "cat/Scientific_Language_Processing_and_Visualization"
  - "sub/LLM_Agent_Benchmarking"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Baskin et al._2025_Researchcodebench Benchmarking llms on implementing novel machine learning research code.pdf"
---

# ResearchCodeBench: Benchmarking LLMs on Implementing Novel Machine Learning Research Code

> **저자**: Tianyu Hua, Harper Hua, Violet Xiang, Benjamin Klieger, Sang T. Truong, Weixin Liang, Fan-Yun Sun, Nick Haber (Stanford University) | **날짜**: 2025 | **DOI**: [arXiv:2506.02314v1](https://arxiv.org/abs/2506.02314v1)

---

## Essence

![Figure 1](figures/fig1.webp)
*ResearchCodeBench 작업 설정 개요. LLM은 연구 논문, TODO 마커가 포함된 목표 코드 스니펫, 동일 프로젝트의 주변 컨텍스트 코드에 접근하여 누락된 코드를 작성한다.*

최신 기계학습 연구 논문에서 제시된 새로운 아이디어를 실행 가능한 코드로 변환하는 LLM의 능력을 평가하는 벤치마크로, 2024-2025년 상위 학회(NeurIPS, ICLR, CVPR) 논문 20개로부터 구성된 212개의 코딩 챌린지를 통해 현재 최고 성능 LLM도 40% 미만의 성공률을 보임을 입증한다.

## Motivation

- **Known**: LLM은 코드 생성 작업에서 유망한 성과를 보였으며, AI가 과학 연구 과정을 혁신할 가능성을 제시하고 있음
- **Gap**: 기존 벤치마크는 주로 주관적 평가(LLM 기반 판정, 동료 검토 시뮬레이션)에 의존하거나, 모델 훈련 데이터에 포함된 확립된 알고리즘의 재현에 초점을 맞춤. 모델의 훈련 시간 이후에 나타난 진정으로 새로운 연구 아이디어를 구현하는 능력을 평가하지 못함
- **Why**: 과학 연구 수준의 코드 생성은 본질적으로 혁신에 관한 것으로, 새로운 아이디어(훈련 분포 외부)를 충실히 구현해야 하며, 객관적이고 실행 가능한 평가 메커니즘이 필요함
- **Approach**: 최근 발표된 ML 논문의 핵심 기여를 구현하는 코딩 챌린지를 구성하고, 공식 저장소의 참조 구현을 기반으로 단위 테스트(Unit tests)와 동등성 테스트(Equivalence tests)의 하이브리드 평가 전략을 도입

## Achievement

![Figure 2](figures/fig2.webp)
*32개 LLM의 ResearchCodeBench에서의 Scaled Pass@1 결과 (탐욕적 디코딩)*

1. **포괄적 벤치마크 구성**: 20개의 최신 ML 논문(생성 모델, 컴퓨터 비전, 이론, 강화학습 등 다양한 분야)으로부터 212개의 코딩 챌린지 구성, 논문 저자 및 도메인 전문가와의 협력으로 신뢰성 확보

2. **LLM 성능 평가 결과**: 32개 이상의 상용 및 오픈소스 LLM 평가 수행
   - Gemini-2.5-Pro-Preview: 37.3% (최고 성능)
   - O3 (High): 32.3%
   - O4-mini (High): 30.8%
   - 최고 성능 모델도 40% 미만의 성공률로 신규 연구 코드 구현의 난이도 입증

3. **신뢰성 높은 평가 방법론**: 단순한 문자열 거리나 LLM 판정자 대신, 실행 기반의 하이브리드 평가 전략으로 기능적 정확성 검증

## How

![Figure 4](figures/fig4.webp)
*논문 접근성에 따른 LLM 성능 차이. 논문 접근 시 더 높은 성능을 보임*

- **논문 선택**: 상위 학회 및 arXiv에서 핵심 기여가 명확하고 오픈소스 저장소가 있으며 저자 협력 가능성이 높은 논문 20개 선정

- **핵심 기여 식별**: 각 논문의 구현 관련 혁신 기여(손실 함수에서 전체 훈련 파이프라인까지)를 파악하여 1개 이상의 기여 추출

- **문맥 코드 구성**: 핵심 기여 코드 실행에 필요한 의존성 파일을 import 문 분석을 통해 최소 필요 세트로 수집

- **코드 스니펫 주석화 및 작업 구성**: XML 스타일 태그로 관심 영역 표시 → 프로그래밍 방식으로 제거 → 다중 세분화 수준(함수 수준, 행 수준)의 계층적 작업 구조 생성 → 각 스니펫에 의도 설명 힌트 제공

- **평가 전략**: 
  - **동등성 테스트(Equivalence tests)**: 예측 및 참조 구현을 동일 입력으로 실행하여 출력 비교
  - **단위 테스트(Unit tests)**: 엣지 케이스와 논리적 오류 감지
  - **하이브리드**: 둘의 결합으로 강건한 정확성 평가

- **성능 메트릭**:
  - **Pass Rate**: 모든 스니펫을 동등하게 처리
  - **Scaled Pass Rate**: 실행 가능한 코드 라인(LoC)으로 가중치 부여하여 복잡도 반영

## Originality

- **시간-민감한 평가**: 모델 훈련 시간 이후의 새로운 연구 아이디어(논문 저자들과 협력하여 작성된 실제 코드)를 평가하므로 진정한 신규성 평가 가능

- **저자 협력 검증**: 단순한 벤치마크 구성을 넘어 논문 저자 및 도메인 전문가와의 공동 작업으로 원래 의도의 충실성 보장

- **계층적 작업 구조**: 단일 난이도 평가 대신 동일 기여를 여러 세분화 수준으로 분해하여 범위 있는 난이도 범위 제공

- **실행 기반 평가**: 주관적 평가나 유사성 메트릭 대신 실제 코드 실행을 통한 객관적 정확성 검증

- **커뮤니티 확장성**: 오픈소스 벤치마킹 프레임워크로 설계하여 새로운 논문과 코딩 챌린지의 지속적 추가 지원

## Limitation & Further Study

- **벤치마크 규모**: 20개 논문 212개 챌린지는 모든 ML 분야를 대표하기에는 제한적이며, 향후 더 많은 논문과 도메인 추가 필요

- **모델 접근성 제약**: 평가 시점의 모델 지식 시간(knowledge cutoff) 편향이 있을 수 있으며, 오픈소스 모델의 부족한 성능이 평가 프레임워크의 한계인지 모델 능력의 한계인지 구분 필요

- **프롬프트 설계 효과**: 논문 접근 여부에 따른 큰 성능 차이를 보이므로, 최적의 프롬프트 공학(prompt engineering) 영향에 대한 심화 분석 필요

- **오염(Contamination) 분석**: 모델이 훈련 데이터에서 유사한 코드 패턴을 접했을 가능성 평가는 여전히 불완전하므로, 더 정교한 오염 감지 기법 개발

- **오류 패턴 분석 심화**: 에러 범주별 성능 차이를 보이나, 특정 에러 타입을 감소시키는 구체적 전략 제시 필요

- **확장성**: 더 큰 코드 기여(현재보다 훨씬 길고 복잡한)에 대한 평가와 다중 챌린지 자동 생성 기법 개발


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4.5/5
- Significance: 4.5/5
- Clarity: 4/5
- Overall: 4.4/5

**총평**: ResearchCodeBench는 LLM의 진정한 혁신 코드 구현 능력을 평가하는 시간-민감하고 객관적인 벤치마크를 제시함으로써, AI 보조 과학 연구의 현실적 한계를 규명하고 향후 LLM 개선 방향의 기준점을 제공하는 가치 있는 기여이다.

## Related Papers

- 🔄 다른 접근: [[papers/545_Mle-bench_Evaluating_machine_learning_agents_on_machine_lear/review]] — MLE-bench가 Kaggle 문제인 반면 ResearchCodeBench는 최신 연구 논문의 새로운 아이디어 구현에 집중
- 🔗 후속 연구: [[papers/731_Scireplicate-bench_Benchmarking_llms_in_agent-driven_algorit/review]] — 연구 논문 아이디어 구현을 알고리즘 복제로 확장한 에이전트 기반 벤치마크
- 🧪 응용 사례: [[papers/670_ResearchCodeAgent_An_LLM_Multi-Agent_System_for_Automated_Co/review]] — ResearchCodeAgent의 자동화된 연구 코딩 능력을 ResearchCodeBench로 평가할 수 있음
- 🔄 다른 접근: [[papers/550_MLRC-Bench_Can_Language_Agents_Solve_Machine_Learning_Resear/review]] — 둘 다 연구 관련 코딩을 다루지만 MLRC-Bench는 재현보다는 리뷰에 초점
- 🔗 후속 연구: [[papers/320_Evaluating_Large_Language_Models_in_Scientific_Discovery/review]] — 함수 생성 중심의 코드 평가가 새로운 기계학습 방법 구현을 위한 연구 코드 벤치마킹으로 확장되었다
- 🔄 다른 접근: [[papers/712_SciCode_A_Research_Coding_Benchmark_Curated_by_Scientists/review]] — 과학자 큐레이션 코딩 벤치마크와 기계학습 연구 코드 벤치마킹이 각각 과학 연구와 ML 연구 맥락에서 코드 생성 능력을 평가한다
- 🧪 응용 사례: [[papers/549_Mlr-copilot_Autonomous_machine_learning_research_based_on_la/review]] — 새로운 ML 방법론 구현을 벤치마킹하는 ResearchCodeBench는 MLR-COPILOT의 자동 코드 구현 능력을 평가하는 실용적 도구다.
- 🔄 다른 접근: [[papers/545_Mle-bench_Evaluating_machine_learning_agents_on_machine_lear/review]] — MLE-bench가 Kaggle 기반인 반면 ResearchCodeBench는 최신 ML 연구 논문 구현에 특화됨
- 🔗 후속 연구: [[papers/548_Mlr-bench_Evaluating_ai_agents_on_open-ended_machine_learnin/review]] — 새로운 머신러닝 방법 구현에 특화된 벤치마크로서 MLR-Bench의 실제 연구 과제 평가를 보완한다.
