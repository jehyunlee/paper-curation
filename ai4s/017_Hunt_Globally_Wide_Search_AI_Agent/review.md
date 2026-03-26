# Hunt Globally: Wide Search AI Agents for Drug Asset Scouting in Investing, Business Development, and Competitive Intelligence

> **저자**: Alisa Vinogradova, Vlad Vinogradov, Luba Greenwood, Ilya Yasny, Dmitry Kobyzev, Shoman Kasbekar, Kong Nguyen, Dmitrii Radkevich, Roman Doronin, Andrey Doronichev | **날짜**: 2026-02-16 | **arXiv**: 2602.15019 | **분야**: cs.AI

---

## Essence

바이오제약 분야에서 글로벌 약물 자산 스카우팅(drug asset scouting)을 위한 트리 기반 자기학습 AI 에이전트 시스템(Bioptic Agent)과 완전성 중심 벤치마크(Completeness Benchmark)를 제안한다. 핵심 문제는 신약 혁신의 상당 부분이 미국 외, 비영어권 지역에서 발생하는데 기존 Deep Research AI 에이전트들이 이러한 다국어/이질적 소스에서의 포괄적 자산 발견에 한계를 보인다는 것이다. Bioptic Agent는 UCB(Upper Confidence Bound) 기반 트리 탐색, 다국어 병렬 조사, 전문가 정렬 검증을 결합하여 F1 79.7%를 달성, Claude Opus 4.6(56.2%), Gemini 3 Pro Deep Research(50.6%), GPT-5.2 Pro(46.6%) 등을 크게 상회한다.

## Motivation

- **알려진 사실**: 대형 제약사의 파이프라인 대부분이 외부 혁신에 의존하며, 글로벌 특허 출원의 약 86.5%가 미국 외 지역에서 발생. 중국이 전체 약물 개발의 약 30%를 차지하며 1,200건 이상의 신약 후보물질을 보유
- **격차(Gap)**: 기존 Deep Research AI 에이전트들은 빠른 사실 확인과 보고서 합성에 최적화되어 있으며, 완전성(completeness) 중심의 개방형 집합 발견(open-world set discovery)에는 부적합. BrowseComp, ResearchRubrics 등 기존 벤치마크도 깊이(depth)를 선호하며 넓이(breadth)를 평가하지 못함
- **접근법**: (1) 비영어권 지역 뉴스에서 역방향으로 구축한 완전성 벤치마크와, (2) 몬테카를로 트리 탐색(MCTS) 스타일의 트리 기반 자기학습 에이전트를 결합하여, 글로벌 다국어 "find-all" 자산 스카우팅 문제를 해결

## Achievement

1. **Completeness Benchmark 구축**: 비미국/비영어권 지역 뉴스에서 자산을 먼저 수집한 후 역방향으로 쿼리를 생성하는 방법론으로 편향을 최소화. 10개 지역, 다수 언어, 48개 실제 투자자/BD 쿼리를 기반으로 한 의도-난이도 조건부 생성 파이프라인
2. **Bioptic Agent의 SOTA 성능**: F1 79.7% (Precision 87.7%, Recall 73.0%)로 모든 비교 대상을 크게 상회. 차선 시스템인 Claude Opus 4.6 (F1 56.2%) 대비 23.5%p 개선
3. **트리 기반 탐색의 효과 입증**: UCB 규칙으로 미탐색 분기에 계산을 할당하여 순차적 반복 대비 포화(saturation)를 지연시킴. No-tree 변형이 50회 Investigator 호출에서 포화되는 반면, 트리 버전은 20회로 더 높은 성능 달성
4. **다국어 병렬 탐색**: 영어+중국어 병렬 Investigator 인스턴스가 비영어권 지역 공개 자산의 커버리지를 추가로 확보
5. **LLM-as-Judge 평가 체계**: Multi-agent debate 기반 Precision Grader 튜닝으로 전문가 대비 88% precision 달성

## How

- **벤치마크 구축 파이프라인**: Regional News Miner (1,255 자산) -> Attributes Enrichment Agent (798개로 필터링) -> Google Search Agent (86개 "under-the-radar" 자산 선별) -> 투자자 쿼리 기반 조건부 쿼리 생성 -> Query Validator + 인간 전문가 검증
- **Bioptic Agent 아키텍처**: (1) Investigator Agent (다국어 웹 검색), (2) Criteria Match Validator Agent (쿼리 제약 조건 매칭), (3) Deduplication Agent (별칭/다국어 변형 해소), (4) Coach Agent (트리 확장 지시문 생성)
- **트리 탐색 알고리즘**: 각 에포크마다 UCB 규칙으로 리프 노드를 선택하고, Rollout(Investigator 실행) -> Evaluate(보상 계산: precision x 신규 자산 수) -> Backpropagate -> Expand(Coach가 k=3 자식 지시문 생성) 순환
- **평가**: GPT-5.1 기반 Precision/Recall Grader, 22개 테스트 쿼리-자산 쌍, 8개 비교 시스템과의 head-to-head 평가

## Originality

약물 자산 스카우팅이라는 고부가가치 실무 문제를 AI 에이전트 연구의 벤치마크로 정식화한 점이 독창적이다. 특히 "자산에서 쿼리를 역생성"하는 벤치마크 구축 방법론은 method-induced coverage bias를 효과적으로 완화한다. 또한 MCTS에서 영감을 받은 UCB 기반 트리 탐색을 웹 검색 에이전트에 적용하여, 순차적 "더 찾아라" 루프의 조기 포화 문제를 구조적으로 해결한 접근이 기술적으로 신선하다. Coach Agent가 실패 패턴을 분석하여 탐색 지시문을 점진적으로 세분화하는 자기학습 메커니즘도 주목할 만하다.

## Limitation & Further Study

### 저자들이 언급한 한계
- 벤치마크의 시드 자산 선택이 뉴스 커버리지에 편향될 수 있으며, 특정 지역/모달리티/개발 단계에 편중될 가능성
- 테스트 분할이 22개 쿼리-자산 쌍으로 매우 작아 통계적 신뢰도에 한계

### 리뷰어 판단 아쉬운 점
- **테스트셋 규모**: 22개 쌍으로는 성능 차이의 통계적 유의성을 확보하기 어려움. 신뢰 구간이나 부트스트랩 분석이 부재
- **자체 벤치마크 편향**: 벤치마크 구축에 사용된 에이전트(o4-mini-deep-research, Gemini Deep Research)가 비교 대상에도 포함되어, 벤치마크가 Bioptic Agent에 유리하게 설계되었을 가능성을 완전히 배제할 수 없음
- **비용 분석 부재**: Bioptic Agent가 수천 건의 웹 검색을 수행하는데, 실제 운영 비용(API 호출, 시간)에 대한 정량적 분석이 없음. GPT-5.2 기반이므로 비용이 상당할 것으로 추정
- **이해충돌**: 저자 전원이 Bioptic.io 소속이며, 자사 제품의 우월성을 입증하는 논문. 벤치마크와 평가 체계 모두 자체 설계
- **일반화 가능성**: 약물 자산 스카우팅 외 다른 "find-all" 도메인(특허 검색, 경쟁사 분석 등)에의 확장성이 논의되지 않음
- **Recall Grader의 한계**: 각 쿼리당 단일 GT 자산만 평가하므로, 실제 recall을 과소/과대 추정할 수 있음

### 후속 연구
- 대규모 테스트셋에서의 재현성 검증 및 제3자 독립 벤치마크 구축
- 다른 도메인(재료과학, 임상시험 매칭 등)으로의 트리 기반 탐색 프레임워크 확장
- 비용-품질 트레이드오프의 체계적 분석
- 실제 BD/투자 전문가와의 블라인드 비교 연구

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 4/5 |
| Technical Soundness | 3/5 |
| Significance | 4/5 |
| Clarity | 4/5 |
| Overall | 4/5 |

**총평**: 바이오제약 자산 스카우팅이라는 실무적으로 중요하고 학술적으로 미개척된 문제를 정식화하고, 트리 기반 자기학습 에이전트로 기존 SOTA Deep Research 시스템을 크게 상회하는 성능을 보인 의미 있는 연구이다. 벤치마크 역생성 방법론과 UCB 기반 탐색 제어가 기술적으로 잘 설계되어 있다. 다만 테스트셋 규모(22개)가 매우 작고, 벤치마크와 시스템이 모두 자사 설계라는 이해충돌이 결과 해석에 주의를 요한다.
