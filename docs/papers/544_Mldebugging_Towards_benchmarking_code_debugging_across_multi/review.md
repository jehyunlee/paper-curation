---
title: "544_Mldebugging_Towards_benchmarking_code_debugging_across_multi"
authors:
  - "Jinyang Huang"
  - "Xiachong Feng"
  - "Qiguang Chen"
  - "Hanzhang Zhao"
  - "Zheng Cheng"
date: "2025"
doi: "N/A"
arxiv: ""
score: 4.0
essence: "본 논문은 실제 소프트웨어 개발 환경에서 흔히 나타나는 **다중 라이브러리 시나리오에서의 코드 디버깅**을 체계적으로 평가하기 위한 MLDebugging 벤치마크를 제시한다. 126개의 Python 라이브러리를 포함하고 7가지 버그 유형으로 분류된 1,175개의 샘플로 구성되어 있다."
tags:
  - "cat/Cognitive_AI_Evaluation_and_Benchmarking"
  - "sub/AI_Benchmarking_Taxonomy"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Huang et al._2025_Mldebugging Towards benchmarking code debugging across multi-library scenarios.pdf"
---

# MLDebugging: Towards benchmarking code debugging across multi-library scenarios

> **저자**: Jinyang Huang, Xiachong Feng, Qiguang Chen, Hanzhang Zhao, Zheng Cheng, Jie Bai, Jingxuan Zhou, Min Li, L. Q. Qin | **날짜**: 2025 | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp) *다중 라이브러리 코드 디버깅의 예시: (a) 단순 정적 버그 vs (b) 라이브러리 간 변수 적응 문제*

본 논문은 실제 소프트웨어 개발 환경에서 흔히 나타나는 **다중 라이브러리 시나리오에서의 코드 디버깅**을 체계적으로 평가하기 위한 MLDebugging 벤치마크를 제시한다. 126개의 Python 라이브러리를 포함하고 7가지 버그 유형으로 분류된 1,175개의 샘플로 구성되어 있다.

## Motivation

- **Known**: 대규모 언어모델(LLM)의 발전으로 코드 디버깅 연구가 활발해졌으며, HumanEval, QuickBugs, MdEval 등의 벤치마크가 존재한다.

- **Gap**: 기존 연구들은 라이브러리가 없거나 단일 라이브러리 환경에만 집중하고 있어, 실제 소프트웨어 개발에서 일반적인 **다중 라이브러리 시나리오를 간과**하고 있다.

- **Why**: 현실의 프로그래밍 작업에서는 여러 라이브러리를 동시에 사용하며, 이는 고유한 도전과제를 야기한다: (1) 버그 위치 파악을 위한 다중 라이브러리 이해, (2) 버그 수정을 위한 다중 라이브러리 활용.

- **Approach**: 다중 라이브러리 코드 디버깅 벤치마크를 구축하고, 버그 카테고리 균형 조정 프로세스를 설계하며, 기존 오픈소스 및 클로즈드소스 LLM들의 성능을 종합 평가한다.

## Achievement

![Figure 2](figures/fig2.webp) *데이터셋 구축 파이프라인: (1) 데이터셋 수집, (2) LLM을 통한 디버깅, (3) 카테고리 균형 조정, (4) 수동 검증*

1. **다중 라이브러리 디버깅 벤치마크 구축**: 126개의 widely-used 라이브러리를 포함하는 1,175개의 고품질 샘플 생성. 기존 벤치마크(xCodeEval, HumanEval, MdEval)와 달리 2-6개의 라이브러리 사용 및 실제 시나리오 반영.

2. **체계적 버그 분류 체계**: Type Mismatch(TM), Data Transfer Issues(DTI), Function Parameter Errors(FPE), Parameter Configuration Errors(PCE), Function Misuse(FM), Requirement Misunderstanding(RM), Import Errors(IE) 등 7개 카테고리로 분류.

3. **종합적 LLM 평가**: GPT-4o, Claude-3.5-sonnet, DeepSeek-V3, DeepSeek-r1 등 주요 모델 평가 결과:
   - 모든 LLM이 다중 라이브러리 디버깅에서 제한된 성능 보임
   - 방법 클래스 에러(method class error)는 잘 처리하나 개념적 오류와 import 누락에 취약
   - 런타임 정보(테스트 케이스, 피드백) 접근성이 성능 향상에 기여

## How

![Figure 2](figures/fig2.webp) *데이터셋 구축의 4단계 프로세스*

**1. 소스 코드 수집**
- BigCodeBench(Zhuo et al., 2024)에서 다중 라이브러리 코드 쿼리 수집
- GPT-4o를 통해 1,038개의 다중 라이브러리 코드 스니펫 생성
- 테스트 케이스 실행으로 609개의 버그 코드 스니펫 식별

**2. LLM을 통한 어노테이션 및 디버깅**
- 7개 버그 카테고리별로 상세한 설명 및 예시 제공
- GPT-4o, DeepSeek-V3, Claude-3.5-sonnet 3개 LLM 활용
- 실패한 디버깅 시도에 대해 최대 5회 추가 시도(test-time scaling)

**3. 버그 카테고리 균형 조정**
- Abstract Syntax Tree(AST) 분석으로 다중 라이브러리 정보 추출
  - 라이브러리 간 변수 전이 관계
  - 각 단계에서의 라이브러리 역할
  - 라이브러리 간 협력 방식
- 불균형 데이터셋에서 특정 버그 타입 추출 및 자동 버그 주입
- 수동 필터링으로 각 카테고리당 약 200개 샘플로 표준화 (566개 버그 주입)

**4. 품질 제어**
- **수동 버그 검수 및 수정**: 4명의 4년 이상 경력 프로그래머 투입
  - 50개 샘플로 사전 훈련으로 일관성 확보
  - 겹치는 교차 검증으로 신뢰성 확보
  - 119개 버그 설명 수정, 340개 분류 수정, 185개 샘플 수동 수정
  - 356개 불량 샘플 제거

## Originality

- **최초 다중 라이브러리 디버깅 벤치마크**: 기존 연구가 간과한 실제 소프트웨어 개발의 복잡한 다중 라이브러리 시나리오를 처음으로 체계적으로 다룸.

- **AST 기반 다중 라이브러리 정보 추출**: 단순한 코드 분석을 넘어 Abstract Syntax Tree를 활용하여 라이브러리 간 변수 전이, 협력 관계 등 추상적 의미론을 포착하는 혁신적 접근.

- **체계적 버그 분류 체계**: 변수 전이, 라이브러리 함수 파라미터, 기능 이해도 등 세 관점에서의 다층적 버그 분류로 더욱 정밀한 성능 평가 가능.

- **엄격한 품질 관리 프로토콜**: 다중 프로그래머 검수, 교차 검증, 사전 훈련 등을 포함한 체계적 품질 보증으로 데이터셋 신뢰성 확보.

- **카테고리 균형 조정 방법론**: 단순 필터링이 아닌 AST 분석 기반 버그 자동 주입으로 불균형 문제를 창의적으로 해결.

## Limitation & Further Study

- **데이터셋 규모**: 1,175개 샘플은 대규모 벤치마크 기준으로 상대적으로 소규모이며, 126개 라이브러리 중 일부 라이브러리의 샘플 부족 가능성.

- **생성된 버그의 현실성**: GPT-4o 기반 버그 생성이 실제 개발 환경의 버그 분포와 완전히 일치하지 않을 수 있음. 저자들이 "실제 버그 분포와의 비교"를 언급했으나 구체적 검증 방법 미흡.

- **언어 제한**: Python에만 국한되어 있어 Java, C++, JavaScript 등 다른 주요 언어로의 확장 필요.

- **모델 버전 고정**: 평가 시점 기준 최신 LLM만 포함되어 있어, 향후 더 강력한 모델 출현 시 재평가 필요.

- **후속 연구 방향**:
  - 다른 프로그래밍 언어로의 벤치마크 확장
  - 더 큰 규모의 다중 라이브러리 샘플 수집
  - 라이브러리별 특성을 고려한 세부 분석
  - 다중 라이브러리 디버깅 특화 LLM 미세조정(fine-tuning) 연구

## Evaluation

- **Novelty**: 4.5/5
  - 다중 라이브러리 시나리오는 명확한 연구 공백을 채우는 새로운 관점
  - AST 기반 정보 추출, 버그 주입 방식은 창의적이나, 전반적 방법론 혁신성은 중간 수준

- **Technical Soundness**: 4/5
  - 데이터 수집, 분류, 품질 관리 프로세스가 체계적이고 엄격함
  - 다만, 버그 생성의 현실성 검증이 다소 약하고, AST 활용 방식의 기술적 깊이 부족
  - 통계적 유의성 검정이나 inter-annotator agreement 지표 명시 필요

- **Significance**: 4/5
  - 실제 소프트웨어 개발 환경의 요구를 반영하여 높은 실용성
  - 개방된 데이터셋으로 향후 연구 확대 가능성
  - 다만 단일 언어(Python) 제한으로 인한 영향력 제한

- **Clarity**: 4/5
  - 전반적으로 명확한 구조와 설명
  - Figure 2 파이프라인이 이해하기 쉽고, 버그 분류가 체계적
  - 일부 기술 세부사항(AST 활용, 균형 조정 알고리즘)의 설명 보충 필요

- **Overall**: 4/5

**총평**: MLDebugging은 코드 디버깅 연구의 중요한 공백인 다중 라이브러리 시나리오를 처음으로 체계적으로 다루는 실질적인 기여를 한다. 엄격한 데이터 수집 및 품질 관리 프로세스와 포괄적인 LLM 평가를 통해 이 분야의 토대를 마련했으나, 언어 제한, 샘플 규모, 버그 현실성 검증 측면에서 개선 여지가 있다.

## Related Papers

- 🔄 다른 접근: [[papers/090_AIRS-Bench_a_Suite_of_Tasks_for_Frontier_AI_Research_Science/review]] — 프론티어 AI 연구 과학 에이전트 평가와 다중 라이브러리 코드 디버깅 평가 모두 AI의 복잡한 기술적 문제 해결 능력을 측정하지만 접근법이 다르다.
- 🏛 기반 연구: [[papers/542_Mlagentbench_Evaluating_language_agents_on_machine_learning/review]] — 머신러닝 에이전트 평가를 위한 언어 모델 벤치마크가 다중 라이브러리 환경에서의 코드 디버깅 평가의 기반을 제공한다.
- 🔗 후속 연구: [[papers/548_Mlr-bench_Evaluating_ai_agents_on_open-ended_machine_learnin/review]] — 오픈엔드 머신러닝 연구 평가가 실제 소프트웨어 개발에서의 디버깅 능력 평가를 연구 차원으로 확장한다.
- 🔄 다른 접근: [[papers/090_AIRS-Bench_a_Suite_of_Tasks_for_Frontier_AI_Research_Science/review]] — AI 에이전트의 연구 생명주기 전체 평가와 다중 라이브러리 코드 디버깅 평가 모두 복잡한 AI 능력을 측정하지만 평가 범위가 다르다.
- 🔗 후속 연구: [[papers/550_MLRC-Bench_Can_Language_Agents_Solve_Machine_Learning_Resear/review]] — 코드 디버깅 벤치마크로서 MLRC-Bench에서 요구되는 코드 구현 및 수정 능력 평가를 보완한다.
