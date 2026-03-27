# StableToolBench: Towards Stable Large-Scale Benchmarking on Tool Learning of Large Language Models

> **저자**: Zhicheng Guo, Sijie Cheng, Hao Wang, Shihao Liang, Yujia Qin, Peng Li, Zhiyuan Liu, Maosong Sun, Yang Liu | **날짜**: 2025-03-05 | **arXiv**: 2403.07714 | **DOI**: 10.48550/arXiv.2403.07714

---

## Essence

StableToolBench는 기존 ToolBench의 불안정성 문제(API 상태 변화, 평가 무작위성)를 해결하기 위해 가상 API 서버(캐싱 시스템 + LLM 기반 API 시뮬레이터)와 안정적 평가 시스템(Solvable Pass Rate/Win Rate + GPT-4 평가자)을 제안한 벤치마크이다. 50%의 API가 비가용 상태에서도 성능 변동이 분산 범위 내에 머물러, 대규모 tool learning 벤치마크의 재현성과 비교 가능성을 크게 향상시켰다.

## Motivation

- **알려진 것**: LLM의 tool learning 능력 평가를 위한 벤치마크가 다수 제안되었으며, ToolBench는 16,000개 이상의 실제 API를 활용한 대표적 대규모 벤치마크
- **Gap**: ToolBench의 실제 API 중 55.6%가 비가용 상태이며, gpt-3.5-turbo 기반 평가자의 판별 능력 부족으로 성능 재현이 불가능 (최대 40.4% 성능 하락). 이는 벤치마크의 핵심 요건인 시간적 일관성과 비교 가능성을 훼손
- **왜 중요한가**: Tool learning은 LLM을 실세계 응용에 연결하는 핵심 능력이며, 안정적 벤치마크 없이는 기법 간 공정한 비교와 진보 측정이 불가능
- **접근법**: 캐싱 시스템으로 API 응답 고정 + LLM(GPT-4-turbo) 시뮬레이터로 비가용 API 대체 + 3개 SOTA LLM 다수결로 solvable task 사전 필터링 + GPT-4 평가자로 교체

## Achievement

1. **API 안정성 확보**: 50% API 비가용 시에도 성능 변동이 분산 범위 내 (기존 ToolBench: 최대 40.4% 하락 vs StableToolBench: 유의미한 변화 없음)
2. **높은 캐시 히트율**: 기존 방법 재실행 시 96.5-97.0%, 새로운 모델에서도 75.8-91.4% 캐시 히트율 달성
3. **API 시뮬레이터의 현실성**: Turing Test에서 인간 평가자가 시뮬레이션 API를 실제 API와 구분하지 못함 (Overall: 67.1% tie, Format Accuracy: 94.3% tie). 문서 준수율 90%
4. **평가 안정성**: GPT-4 평가자가 task solvability 80%, answer solving 74%, comparison 78% 정확도 달성 (GPT-3.5: 각각 65%, 68%, 56%)
5. **Solvable 태스크 필터링**: 1,100개 중 765개 solvable 태스크를 사전 확정하여 unsolvable/unsure 태스크로 인한 무작위성 제거

## How

- **캐싱 시스템**: API 호출의 (category, tool, API name, arguments) 키로 응답 저장. ToolBench 학습/테스트 데이터 + 새 실험 데이터로 164,980개 유효 캐시 항목 구축. 유효하지 않은 응답은 키워드 기반 필터링으로 제거
- **API 시뮬레이터**: GPT-4-turbo에 API 문서 + 캐시의 few-shot 실제 호출 예시(최대 5개)를 제공하여 API 동작 시뮬레이션. 캐시 미스 + 실제 API 비가용 시에만 호출
- **API 호출 규칙**: Cache hit -> 캐시 응답 반환; Cache miss -> 실제 API 호출 시도; 실제 API 실패 -> 시뮬레이터 호출. 결과는 항상 캐시 업데이트
- **Solvable 태스크 판별**: GPT-4-turbo, Gemini-Pro, Claude-2 3개 모델 다수결 투표로 solvable 여부 사전 결정
- **평가 메트릭**: SoPR(Solvable Pass Rate) -- Solved/Unsure/Unsolved에 1/0.5/0점 부여; SoWR(Solvable Win Rate) -- 쌍대 비교 기반. 모든 평가에 GPT-4-turbo 사용
- **다양성 검증**: S-BERT 임베딩 + UMAP 시각화로 실제/시뮬레이션 API 응답 분포 유사성 확인

## Originality

- **캐싱 + LLM 시뮬레이션의 상보적 결합**: 캐시로 안정성을 확보하되, 캐시 미스 시 LLM 시뮬레이터로 API를 가상 구현하는 계층적 설계가 실용적이고 독창적
- **Solvable 태스크 사전 필터링**: 다수 LLM 다수결로 unsolvable 태스크를 사전 제거하여 평가의 무작위성을 구조적으로 해결
- **API 시뮬레이터의 Turing Test 검증**: 시뮬레이션 API의 현실성을 체계적으로 검증한 최초의 시도
- **벤치마크 안정성의 정량적 분석**: API 비가용 비율별 성능 변화를 체계적으로 측정하여 안정성 문제를 정량화

## Limitation & Further Study

### 저자들이 언급한 한계

- GPT-4를 API 시뮬레이터와 평가자로 사용하여 벤치마크 운영 비용이 높음
- GPT-4 백본 LLM의 업그레이드가 시뮬레이션 결과에 영향을 줄 수 있음
- 현재 오픈소스 LLM은 API 시뮬레이션 성능이 부족하여 상용 모델 의존 불가피
- 새로운 방법론 등장 시 캐시 히트율이 낮아질 수 있어 지속적 캐시 업데이트 필요

### 자체판단 아쉬운 점

- 시뮬레이션 API가 실시간 데이터를 필요로 하는 경우(날씨, 주가, 실시간 교통 등)의 한계가 충분히 논의되지 않음 -- "합리적" 응답이 실제 응용에서는 오류를 유발할 수 있음
- Solvable 태스크 필터링이 3개 특정 모델(GPT-4, Gemini, Claude)에 의존하여, 이 모델들의 bias가 태스크 선택에 반영될 수 있음
- 캐시 시스템의 키가 exact match 기반이므로, argument의 사소한 변경(순서, 포맷)에도 캐시 미스가 발생할 수 있는 한계가 분석되지 않음
- Turing Test 샘플 크기(70개 API)가 16,000개 이상의 전체 API 규모에 비해 매우 작음
- ToolBench 이외의 다른 tool learning 벤치마크로의 일반화 가능성이 검증되지 않음

### 후속 연구

- 오픈소스 LLM 성능 향상에 맞춰 시뮬레이터/평가자를 오픈소스 모델로 전환
- 캐시의 fuzzy matching 도입으로 유사 인수의 캐시 히트율 향상
- 실시간 데이터 의존 API에 대한 별도 처리 전략 개발
- 다른 tool learning 벤치마크(API-Bank, T-Eval 등)로의 프레임워크 확장

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 3/5 |
| Technical Soundness | 4/5 |
| Significance | 4/5 |
| Clarity | 4/5 |
| Overall | 4/5 |

**총평**: ToolBench의 재현성 문제를 캐싱과 LLM 시뮬레이션이라는 실용적 접근으로 해결한 엔지니어링 기여가 탁월한 논문이다. API 비가용률 50%에서도 안정적 성능을 유지하며, Turing Test를 통해 시뮬레이션의 현실성을 입증한 점이 인상적이다. 다만, GPT-4 의존성이 높아 비용과 재현성 측면에서 근본적 한계가 있으며, 실시간 데이터 의존 API 처리 등 해결해야 할 과제가 남아 있다. Tool learning 연구 커뮤니티에 안정적 벤치마킹 기반을 제공하는 중요한 인프라 수준의 기여이다.
