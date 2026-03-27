# AgentRxiv: Towards Collaborative Autonomous Research

> **저자**: Samuel Schmidgall, Michael Moor | **날짜**: 2025-03-23 | **arXiv**: 2503.18102 | **DOI**: 10.48550/arXiv.2503.18102

---

## Essence

AgentRxiv는 LLM 기반 자율 연구 에이전트들이 공유 프리프린트 서버를 통해 연구 결과를 업로드, 검색, 상호 참조하며 협업적으로 연구를 수행할 수 있게 하는 프레임워크이다. 단일 실험실이 MATH-500에서 gpt-4o mini 기준 70.2%에서 78.2%로 11.4% 상대적 성능 향상을 달성했으며, 3개 병렬 실험실 운영 시 79.8%(13.7% 상대 향상)까지 도달하여, 에이전트 간 누적적 지식 공유가 고립된 연구보다 우월함을 입증했다.

## Motivation

- **알려진 것**: AI Scientist, Agent Laboratory, Virtual Lab 등 LLM 에이전트 기반 자율 연구 시스템이 등장하여 end-to-end 연구 수행이 가능해졌음
- **Gap**: 기존 자율 연구 프레임워크들은 각각 독립적으로 작동하며, 이전 에이전트의 연구 결과를 참조하거나 누적적으로 발전시키는 메커니즘이 부재
- **왜 중요한가**: 실제 과학 발전은 수백 명의 연구자가 점진적으로 기여하는 누적적 과정이므로, 자율 에이전트도 이러한 협업적 지식 축적 구조를 갖추어야 진정한 연구 가속화가 가능
- **접근법**: arXiv를 모델로 한 중앙 집중식 프리프린트 서버(AgentRxiv)를 구축하여, 에이전트 실험실 간 비동기적 연구 공유 및 검색 기반 참조 체계를 구현

## Achievement

1. **단일 실험실 점진적 향상**: 40편의 논문 생성을 통해 MATH-500 정확도가 70.2%에서 78.2%로 꾸준히 증가 (+11.4% 상대 향상)
2. **발견 알고리즘의 일반화**: 최고 성능 기법 Simultaneous Divergence Averaging(SDA)가 GPQA (+6.8%), MMLU-Pro (+12.2%), MedQA (+8.9%) 등 타 벤치마크에서도 평균 +9.3% 향상
3. **모델 간 일반화**: SDA가 gpt-4o mini, gpt-4o, DeepSeek-v3, Gemini-1.5 Pro, Gemini-2.0 Flash 등 5개 모델에서 평균 +3.3% 향상
4. **병렬 실험실 가속**: 3개 병렬 실험실이 협업하여 79.8% 달성 (13.7% 상대 향상), 순차 실행 대비 7편 만에 76.2% 도달 (순차: 23편 필요)
5. **이전 연구 참조의 중요성**: 이전 논문 참조 제거 시 73.8%에서 정체 vs. 참조 시 78.2% 달성 (+6.0% 차이)

## How

- **기반 시스템**: Agent Laboratory (Schmidgall et al., 2025) -- Literature Review, Experimentation, Report Writing 3단계 파이프라인의 multi-agent 시스템
- **AgentRxiv 서버**: 로컬 웹 애플리케이션으로 구현. 논문 업로드 시 텍스트/메타데이터 추출, SentenceTransformer 기반 임베딩 생성, cosine similarity 기반 검색
- **연구 방향 설정**: 기존 Agent Laboratory의 "research idea" 대신 "research direction" (예: "Improve accuracy on MATH-500 using reasoning and prompt engineering")을 제공하고, 에이전트가 자체적으로 아이디어 생성
- **LLM 백엔드**: o3-mini (medium)를 실험실 운영 LLM으로 사용, gpt-4o mini를 실험 대상 모델로 사용
- **논문 참조**: 각 세대에서 AgentRxiv 5편 + arXiv 5편을 리뷰하여 이전 연구 기반으로 새로운 기법 개발
- **병렬 실험**: 3개 독립 Agent Laboratory 인스턴스를 동시 실행, 비동기적으로 AgentRxiv를 통해 결과 공유
- **비용**: 논문당 평균 $3.11, 순차 실험 총 $92.0, 병렬 실험 총 $279.6

## Originality

- **에이전트 간 프리프린트 서버**: 자율 연구 에이전트들이 arXiv와 유사한 공유 플랫폼을 통해 연구를 축적하고 상호 참조하는 최초의 프레임워크
- **연구 방향 기반 자율 아이디어 생성**: 구체적 아이디어 대신 연구 방향만 제공하여 에이전트가 스스로 아이디어를 발전시키는 패러다임 전환
- **에이전트의 자연발생적 누적 연구**: 명시적 지시 없이도 에이전트가 이전 기법(예: Meta-Mirror Prompting)을 자연스럽게 개선하여 v2를 만드는 현상 발견
- **병렬 자율 연구의 속도-효율 트레이드오프 분석**: 다수 실험실 병렬 운영의 wall-clock 시간 단축 효과와 자원 중복 사용 문제를 정량적으로 분석

## Limitation & Further Study

### 저자들이 언급한 한계

- **높은 hallucination 비율**: Agent Laboratory가 실험 결과를 hallucinate하거나, code repair 메커니즘이 핵심 코드를 placeholder로 대체하는 문제가 빈번하게 발생하여 수동 검증 필수
- **Reward hacking**: 논문 작성 단계에서 NeurIPS 기준 점수를 최적화하면서 허위 높은 성능을 보고하는 논문이 더 높은 점수를 받는 문제
- **불가능한 계획 수립**: o1/o3-mini 등 temperature sampling이 비활성화된 모델에 대해 temperature 기반 방법을 계획하는 등의 오류
- **높은 실험 실패율**: 코드 버그로 ~0% 정확도를 보이는 실험이 다수 존재
- **LaTeX 작성 오류**: 미학적/가독성 문제 (수식 기호 오류, 과대 테이블 등)

### 자체판단 아쉬운 점

- MATH-500 reasoning/prompting이라는 매우 좁은 연구 방향에서만 검증되었으며, 실험 설계나 wet-lab 연구 등 더 open-ended한 과학적 발견에 대한 적용 가능성은 미검증
- 발견된 알고리즘(SDA 등)의 실질적 novelty가 self-consistency, multi-agent debate 등 기존 기법의 변형에 가까워, "새로운 과학적 발견"이라 보기 어려움
- hallucination 문제로 인해 모든 결과를 수동 검증해야 하므로, 진정한 의미의 "자율" 연구라 할 수 없음
- 병렬 실험의 경우 순차 대비 3배 비용($279.6 vs $92.0)으로 1.6% 포인트 향상에 그쳐 비용 효율성이 낮음
- 에이전트 간 communication이 논문이라는 고수준 매체로만 이루어져, 코드나 중간 결과 공유 등 더 효율적인 협업 채널에 대한 탐색이 부족

### 후속 연구

- hallucination 탐지 및 자동 검증 모듈 개발을 통한 수동 검증 의존도 감소
- 병렬 실험실 간 중복 연구 감소를 위한 explicit coordination 메커니즘 도입
- Exploration reward 기반 연구 다양성 유도 및 ELO/tournament 기반 연구 계획 필터링
- MATH-500 이외의 open-ended 과학 연구 방향으로의 확장
- 연구 과정에서의 plan adjustment 허용 (실험 중 계획 수정 가능)

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 4/5 |
| Technical Soundness | 3/5 |
| Significance | 4/5 |
| Clarity | 4/5 |
| Overall | 3/5 |

**총평**: 자율 연구 에이전트들이 공유 프리프린트 서버를 통해 협업적으로 연구를 수행하는 매력적인 비전을 제시한 논문이다. 누적적 지식 공유가 고립된 연구보다 우월하다는 점을 정량적으로 입증한 것은 의미 있으나, 높은 hallucination 비율과 수동 검증 의존성, 좁은 실험 범위(MATH-500 prompting), 그리고 발견된 알고리즘의 제한적 novelty는 현재 시스템의 실용적 가치에 대한 의문을 남긴다. 자율 과학 연구의 미래 방향을 탐색하는 시의적절한 연구이지만, 신뢰성 확보를 위한 후속 개선이 필수적이다.
