---
title: "101_AnyTool_Self-Reflective_Hierarchical_Agents_for_Large-Scale"
authors:
  - "Yu Du"
  - "Fangyun Wei"
  - "Hongyang Zhang"
date: "2024.02"
doi: "10.48550/arXiv.2402.04253"
arxiv: ""
score: 4.25
essence: "16,000개 이상의 API를 활용하여 사용자 쿼리를 해결하는 GPT-4 기반 에이전트로, 계층적 API 검색기, 문제 해결기, 자기 반성 메커니즘을 통합하여 기존 방식 대비 35.4% 향상된 성능을 달성했다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/Multi-Agent_Language_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Du et al._2024_AnyTool Self-Reflective, Hierarchical Agents for Large-Scale API Calls.pdf"
---

# AnyTool: Self-Reflective, Hierarchical Agents for Large-Scale API Calls

> **저자**: Yu Du, Fangyun Wei, Hongyang Zhang | **날짜**: 2024-02-06 | **DOI**: [10.48550/arXiv.2402.04253](https://doi.org/10.48550/arXiv.2402.04253)

---

## Essence

![Figure 1](figures/fig1.webp)
*AnyTool의 구조 및 ToolLLM과의 성능 비교*

16,000개 이상의 API를 활용하여 사용자 쿼리를 해결하는 GPT-4 기반 에이전트로, 계층적 API 검색기, 문제 해결기, 자기 반성 메커니즘을 통합하여 기존 방식 대비 35.4% 향상된 성능을 달성했다.

## Motivation

- **Known**: 이전 연구(ToolLLM)는 대규모 API 풀에서 관련 API를 검색한 후 이를 이용해 쿼리를 해결하는 이원화 접근방식을 제안했으나, 별도의 API 검색기 학습이 필요하고 검색 정확도가 낮으며 피드백 메커니즘이 부족함.

- **Gap**: 규모가 큰 API 풀에서 효율적으로 API를 탐색하면서도 잘못된 선택에 대한 복구 메커니즘이 없고, 평가 프로토콜에 체계적인 결함이 존재(논-소비 가능 쿼리를 해결된 것으로 간주).

- **Why**: LLM의 함수 호출(function calling) 기능을 직접 활용하면 별도 학습 없이 대규모 API를 탐색할 수 있으며, 자기 반성을 통해 실패 사례에서 학습하여 단계적 개선이 가능함.

- **Approach**: (1) 계층적 API 검색기로 검색 공간 축소, (2) 자기 반성 메커니즘으로 반복 개선, (3) 실제 시나리오를 반영한 개선된 평가 프로토콜 제안.

## Achievement

![Figure 2](figures/fig2.webp)
*AnyTool의 전체 구조: 계층적 API 검색기, 솔버, 자기 반성 메커니즘*

1. **성능 향상**: ToolBench에서 ToolLLM 대비 평균 pass rate 35.4% 증가 달성.

2. **학습 불필요**: GPT-4의 함수 호출 기능만으로 작동하여 추가 모듈 학습이 불필요(Plug-and-Play).

3. **반성을 통한 점진적 개선**: 4-6회 자기 반성 반복으로 모든 데이터셋에서 최대 20% pass rate 향상(Figure 3 참조).

4. **평가 프로토콜 개선**: 실제 응용 시나리오를 반영한 개선된 평가 방식 제안 및 AnyToolBench 벤치마크 도입.

## How

![Figure 4](figures/fig4.webp)
*기존 평가 프로토콜의 결함과 개선된 평가 방식 비교*

### 계층적 API 검색기 (Hierarchical API Retriever)
- **3계층 구조**: 메타 에이전트 → 카테고리 에이전트 → 도구 에이전트
- RapidAPI의 자연스러운 카테고리 분류 활용으로 검색 범위 축소
- 각 에이전트는 특화된 함수 세트로 API 공간 탐색
- 문맥 길이 제약 극복

### 솔버 (Solver)
- 검색된 API 후보군을 이용하여 사용자 쿼리에 대한 실제 해결책 구성
- 선택된 API들의 상세 정보와 파라미터 활용

### 자기 반성 메커니즘 (Self-Reflection Mechanism)
- 초기 솔루션 제안 → GPT-4에 의한 실행 가능성 평가
- 실패 시 실패 원인과 과거 맥락을 고려하여 AnyTool 재활성화
- 폐쇄-루프 시스템으로 단순 쿼리의 "과도한 탐색" 방지 및 복잡 쿼리의 심층 탐색 지원

### 개선된 평가 프로토콜
- **기존 문제** (Eq. 1): 완전히 무관한 API 선택 시에도 논-소비 가능으로 분류되어 인위적 높은 pass rate
- **개선안** (Eq. 2): 모든 쿼리의 수동 검증을 통해 실제로 API 풀로 해결 가능한 쿼리만 평가 포함

## Originality

- **함수 호출 기반 검색**: 사전학습된 텍스트 임베딩이나 미세조정 대신 GPT-4의 함수 호출 기능을 직접 활용하여 학습 불필요.

- **계층적 구조의 창의적 적용**: 분할 정복 전략을 API 검색에 적용하여 맥락 길이 제약을 효과적으로 해결.

- **폐쇄-루프 자기 반성**: 단순히 반성만 하는 것이 아니라 실패 원인을 고려한 재시도로 점진적 개선을 실현.

- **평가 프로토콜 재검토**: 기존 평가 방식의 근본적 결함을 지적하고 현실적 시나리오 반영 프로토콜 제안 및 새로운 벤치마크 도입.

## Limitation & Further Study

- **GPT-4 의존성**: 에이전트의 모든 의사결정이 GPT-4에 의존하므로 다른 LLM으로의 일반화 가능성 미검토.

- **평가 메트릭의 제한**: 자동 평가를 위해 GPT-4-as-a-Judge를 사용하는데, 96.5% 인간 평가 상관도는 높지만 여전히 5% 오류 가능성 존재.

- **API 구조 가정**: RapidAPI의 카테고리 분류에 의존하므로 다른 API 저장소로의 적용 시 재구조화 필요.

- **자기 반성 반복의 한계**: 최적 반영 횟수가 데이터셋마다 다를 수 있으며, 너무 많은 반복은 컴퓨팅 비용 증가.

- **향후 연구**: (1) 더 작은 LLM 모델에서의 성능 검증, (2) 실시간 API 변경에 대한 적응성, (3) 다국어 쿼리 지원 확대.


## Evaluation

- Novelty: 4/5
- Technical Soundness: 4.5/5
- Significance: 4.5/5
- Clarity: 4/5
- Overall: 4.25/5

**총평**: AnyTool은 대규모 API 활용 문제에 대해 학습 불필요한 실용적 솔루션을 제공하며, 특히 자기 반성 메커니즘과 평가 프로토콜 개선으로 실제 응용 가치가 높은 논문이다. 다만 GPT-4 특화 설계와 더 광범위한 일반화 검증이 한계로 남는다.