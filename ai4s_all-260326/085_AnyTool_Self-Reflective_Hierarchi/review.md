# AnyTool: Self-Reflective, Hierarchical Agents for Large-Scale API Calls

> **저자**: Yu Du, Fangyun Wei, Hongyang Zhang | **날짜**: 2024-02-06 | **arXiv**: 2402.04253 | **DOI**: 10.48550/arXiv.2402.04253

---

## Essence

AnyTool은 GPT-4의 function calling 기능을 활용하여 16,000개 이상의 API 풀에서 계층적 에이전트 구조(meta-agent -> category agent -> tool agent)로 관련 API를 검색하고, self-reflection 메커니즘으로 실패한 쿼리를 반복 재시도하는 plug-and-play tool learning 에이전트이다. ToolBench에서 ToolLLM 대비 평균 pass rate +35.4% 향상을 달성했으며, 기존 평가 프로토콜의 인위적 pass rate 부풀림 문제를 지적하고 수정된 평가 기준을 제안했다.

## Motivation

- **알려진 것**: ToolLLM 등 기존 연구가 16,000개 이상의 실제 API를 활용한 tool learning 프레임워크를 제안했으며, retrieve-then-solve 2단계 접근법이 표준으로 자리잡음
- **Gap**: 기존 API retriever는 학습이 필요하고 정확도가 낮아 관련 API를 놓치는 경우가 빈번. 또한 피드백 메커니즘이 부재하여 잘못된 API 후보가 제공되면 쿼리 해결 실패. 기존 ToolBench 평가 프로토콜은 non-solvable 쿼리를 pass로 간주하여 99.0%의 인위적 pass rate 발생 가능
- **왜 중요한가**: LLM의 tool 활용 능력은 실세계 응용의 핵심이며, 16,000개 이상의 대규모 API를 효과적으로 탐색하고 활용하는 것은 LLM의 context length 제한으로 인해 근본적 도전
- **접근법**: Rapid API의 Category-Tool-API 3계층 구조를 활용한 divide-and-conquer 방식의 계층적 에이전트 + 실패 시 원인 분석 후 에이전트를 bottom-up으로 재활성화하는 self-reflection 메커니즘

## Achievement

1. **ToolBench SOTA**: 필터링된 ToolBench 6개 서브셋 평균 pass rate 58.2% 달성 -- ToolLLM(22.9%) 대비 +35.3%, GPT-4+reference APIs(38.9%) 대비 +19.3%
2. **AnyToolBench**: 자체 벤치마크(400 인스턴스)에서 73.8% pass rate 달성 -- ToolLLM+GPT-4(36.6%) 대비 2배 이상 향상
3. **Self-reflection 효과**: 4-6회 self-reflection으로 모든 데이터셋에서 최대 20% pass rate 향상
4. **평가 프로토콜 개선**: Non-solvable 쿼리를 pass로 간주하는 기존 메트릭(Eq 1)의 문제점을 지적하고, Solved/(Solved+Unsolved)로 수정(Eq 2). 수동 검토로 solvable 쿼리만 필터링
5. **Plug-and-play**: 외부 모듈 학습 불필요 -- GPT-4 function calling만으로 작동
6. **GPT-4 평가 일치율**: 인간 평가와 96.5% 일치율 확인 (GPT-3.5는 73.9%)

## How

- **계층적 API Retriever**: 3계층 에이전트 구조 -- (1) Meta-agent: 쿼리 분석 후 관련 카테고리 식별, category agent 생성; (2) Category agent: 카테고리 내 관련 tool 식별, tool agent 생성; (3) Tool agent: tool 내 관련 API를 API-candidate pool에 추가. 각 에이전트는 독립적 히스토리 컨텍스트 유지, 멀티스레드 병렬 실행
- **Solver**: DFSDT(Depth-First Search Decision Tree) 또는 CoT 기반으로 API-candidate pool의 API를 사용하여 쿼리 해결. "Give Solution", "Try Backtrack", "Give Up" 3가지 결과 생성
- **Self-Reflection**: 실패 원인 파악 후 bottom-up(tool -> category -> meta) 순서로 "Finished" 상태가 아닌 에이전트만 재활성화. Solver에서는 무관 API 제거 후 확장된 candidate pool로 재시도
- **종료 조건**: Tool agent가 `check_if_request_solvable` 호출 시 True 반환, 또는 최대 self-reflection 횟수 도달
- **리소스**: 쿼리당 평균 13.5만 토큰, 14.1개 API 후보, 43.3회 OpenAI API 호출, 4.6회 self-reflection

## Originality

- **계층적 에이전트 기반 API 검색**: Rapid API의 자연스러운 분류 체계를 활용하여 16,000개 이상의 API를 LLM context length 제한 내에서 탐색 가능하게 한 divide-and-conquer 설계
- **Closed-loop Self-Reflection**: API retriever와 solver 모두에 적용되는 self-reflection이 실패 원인을 분석하고 bottom-up 재활성화를 수행하여, 단순 재시도가 아닌 지능적 재탐색 구현
- **평가 프로토콜 결함 식별 및 수정**: Random API 선택 시 99.0% pass rate가 나오는 기존 메트릭의 근본적 결함을 실험적으로 입증하고 수정안 제시
- **Training-free 접근**: ToolLLM의 학습 기반 API retriever와 달리, GPT-4 function calling만으로 동등 이상의 성능을 달성하는 plug-and-play 설계

## Limitation & Further Study

### 저자들이 언급한 한계

- 극도로 복잡한 시나리오에서의 성능이 적절한 데이터셋 부재로 검증되지 않음
- GPT-4 function calling에 전적으로 의존하므로 GPT-4의 능력이 솔루션 품질의 상한선
- 쿼리당 평균 13.5만 토큰 소비로 비용이 높음

### 자체판단 아쉬운 점

- GPT-4 의존성으로 인해 오픈소스 LLM으로의 이식이 불가능하며, 비용 측면에서 실용적 배포가 어려움
- Self-reflection의 반복 횟수 증가에 따른 비용 대비 성능 향상의 효율성 분석이 부족 -- Figure 3에서 10회 이후 수렴하나 비용 증가는 선형적
- API candidate pool의 최대 크기(64개)가 고정되어 있어, 매우 복잡한 multi-tool 쿼리에서는 병목이 될 수 있음
- ToolBench 필터링 과정에서 수동 검토의 기준이 주관적일 수 있으며(예: "unreasonable queries"), 필터링 후 G3-I 서브셋이 38개로 줄어 통계적 신뢰도 우려
- 실제 API 호출의 안정성 문제(API 비가용, 인증 실패 등)에 대한 대응이 논의되지 않음 -- StableToolBench와 같은 가상 API 시스템과의 결합이 필요

### 후속 연구

- API 조직 구조 최적화를 통한 검색 성능 및 효율 향상
- API 활용에 특화된 오픈소스 LLM 개발로 로컬 배포 지원
- Self-reflection의 비용 효율적 종료 조건 연구
- 가상 API 시스템과의 통합으로 안정성 확보

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 4/5 |
| Technical Soundness | 4/5 |
| Significance | 4/5 |
| Clarity | 4/5 |
| Overall | 4/5 |

**총평**: 16,000개 이상의 대규모 API 풀에서 효과적으로 API를 검색하고 활용하는 문제를 계층적 에이전트와 self-reflection 메커니즘으로 우아하게 해결한 논문이다. 학습 없이 GPT-4 function calling만으로 ToolLLM 대비 +35% 이상의 성능 향상을 달성한 점, 그리고 기존 평가 프로토콜의 근본적 결함을 실험적으로 입증한 점이 핵심 기여이다. 다만, 높은 GPT-4 의존성과 비용, 그리고 실제 API의 안정성 문제 미처리는 실용화의 걸림돌이다. Tool learning 분야에서 LLM의 에이전트적 활용 가능성을 설득력 있게 보여준 중요한 연구이다.
