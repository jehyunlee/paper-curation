---
title: "AI for Science 지형도 — 발표 원고 v2 (58장, 줄글)"
topic: ai4s
slides: 58
corpus_papers: 2709
body_chars: 85491
evidence_since: 2025
generated: 2026-10-21
tags:
  - ai4science
  - 발표원고
  - 연구동향
  - ai4s
---

# AI for Science 지형도 — 발표 원고 58장 (v2 · 줄글)

> [!info] 읽는 법
> 슬라이드 한 장 = 절(section) 하나. `> [!abstract]` 는 **화면에 띄울 한 줄**, 그 아래 문단이 **말할 내용**이다.
> 코퍼스 **2,709편** · 대분류 **10개** · 서브카테고리 **95개** 중 상위 **5개씩** · 본문 **85,491자**.
> 사례는 **2025년 이후 우선**(코퍼스의 83%). 레퍼런스 링크는 논문별 리뷰 문서(`../../docs/papers/<slug>/index.html`)로 연결된다.

## 목차

- **오프닝**
    - `S01` AI for Science, 2026년 지형도
    - `S02` 이 지도는 어떻게 만들어졌나
    - `S03` 코퍼스 한눈에 보기
    - `S04` 10개 대분류의 지형
    - `S05` AI4S 서사: 예측에서 생성, 그리고 검증으로
- **제1부 · 생체분자 생성 모델링**
    - `S06` 단일세포 발현 모델링 — 121편
    - `S07` 단백질 언어모델 상호작용 — 53편
    - `S08` 이산 확산 분자 생성 — 43편
    - `S09` 역합성 반응 예측 — 41편
    - `S10` 유전체 파운데이션 모델 — 40편
- **제2부 · 자율 AI 과학 발견**
    - `S11` 자율 AI 과학자 에이전트 — 70편
    - `S12` 자율 과학 발견 시스템 — 46편
    - `S13` 에이전틱 신약 발굴 — 36편
    - `S14` 자율 실험실·공동 과학자 — 35편
    - `S15` 단백질 공학 에이전트 — 34편
- **제3부 · 형식 수학 정리 증명**
    - `S16` 검증 가능 보상 RL — 47편
    - `S17` LLM 형식 정리 증명 — 36편
    - `S18` 정리 자동 형식화 — 35편
    - `S19` AI 공동 수학자 — 26편
    - `S20` 증명 검증의 아첨 — 26편
- **제4부 · LLM 추론·에이전트 벤치마크**
    - `S21` 다단계 연쇄 추론 — 54편
    - `S22` 에이전트 기억·계획 — 39편
    - `S23` 임상 추론 에이전트 — 33편
    - `S24` 표·데이터 추론 — 30편
    - `S25` 주장 검증 — 29편
- **제5부 · 물리 기반 신경 시뮬레이션**
    - `S26` 물리 기반 신경 연산자 — 66편
    - `S27` 동역학계 flow matching — 46편
    - `S28` 확산 기반 자료동화 — 33편
    - `S29` 수치 기상 예보 — 31편
    - `S30` 로봇 조작·제어 — 27편
- **제6부 · 의료·신경 신호 모델링**
    - `S31` EHR 파운데이션 모델 — 56편
    - `S32` 뇌-시각 표상 정렬 — 33편
    - `S33` 의료영상 분할 — 32편
    - `S34` 멀티모달 의료영상 진단 — 27편
    - `S35` 생체신호 파운데이션 모델 — 27편
- **제7부 · 과학 문헌·동료심사**
    - `S36` 동료심사 피드백 데이터셋 — 61편
    - `S37` 과학 문헌 검색·QA — 32편
    - `S38` 신규성 기반 아이디어 — 30편
    - `S39` 자동 문헌 리뷰 생성 — 25편
    - `S40` 다문서·메타리뷰 요약 — 24편
- **제8부 · 멀티모달 인식·효율화**
    - `S41` 다국어 LLM 양자화·효율화 — 46편
    - `S42` 과학 도표 캡셔닝 — 24편
    - `S43` AutoML 도메인 전이 — 16편
    - `S44` 차트 추론·팩트체크 — 14편
    - `S45` 도시 장면 이해 — 13편
- **제9부 · 인과·통계 추론**
    - `S46` 인과 독립성 검정 — 53편
    - `S47` 관찰 데이터 처치 정책 — 23편
    - `S48` 통계 검정·리더보드 — 16편
    - `S49` 중도절단 생존분석 — 16편
- **제10부 · 계산 재료 시뮬레이션**
    - `S50` 기계학습 원자간 포텐셜 — 37편
    - `S51` 생성형 무기 재료 설계 — 33편
    - `S52` 고온 합금 포텐셜 — 19편
    - `S53` 양자 다체 시뮬레이션 — 18편
- **종합**
    - `S54` 수렴 신호: 경계가 무너지는 곳
    - `S55` 부상과 쇠퇴
    - `S56` 비어 있는 자리
    - `S57` 검증 전환의 여섯 축
    - `S58` 그래서 무엇을 할 것인가

---

## S01 · AI for Science, 2026년 지형도

*오프닝* · *표지*

<sub>코퍼스 2,709편 · 대분류 10개 · 서브카테고리 95개 · 2025년 이후 83%</sub>

> [!abstract] 화면에 띄울 한 줄
> 생성 경쟁은 끝났고, 2026년 AI4S의 승부는 검증으로 옮겨갔다. 2,709편이 그 전환을 증언한다.

**AI4S 코퍼스 2,709편을 10개 대분류와 95개 서브카테고리로 읽었다. 이 발표의 결론은 한 문장이다. 생성은 값싸졌고, 병목은 검증으로 이동했다.**

코퍼스는 2025년 이후 논문이 83%를 차지할 만큼 최신에 쏠려 있다. 그래서 이 지도는 고전의 정리가 아니라 지금 막 벌어지는 일의 스냅숏이다. 단백질·분자·재료 생성 모델, 자율 과학자 에이전트, 형식 증명기가 같은 해에 성숙했고, 그 옆에서 같은 수의 반증이 쌓였다.

반증의 모양은 분야마다 달랐으나 문장은 같았다. 형식 증명에서는 Ground False가 ProofNet 항목의 56%가 원문에 충실하지 않다고 밝혔고, QEDBench는 LLM 채점자가 점수를 부풀린다고 정량화했다. 통계 쪽에서는 The Leaderboard Lottery가 리더보드 1위가 동전 던지기일 수 있다고 보였다. 평가 자체가 연구 대상이 됐다.

긍정적 사례도 분명하다. Robin은 가설-실험-해석 루프를 돌려 ripasudil을 후보로 발굴하고 실험으로 확인했다. BFS-Prover-V2는 형식 검증기를 보상 신호로 삼아 miniF2F 95.08%를 보고했다. 두 사례의 공통점은 외부 검증기가 루프 안에 들어 있다는 것이다. 능력이 아니라 검증기와의 결합이 성과를 가른다.

48장의 본문은 대분류별로 이 전환이 어떤 모양인지 보여 준다. 오프닝 다섯 장은 코퍼스의 규모와 구성을 정리하고, 종합 다섯 장은 시기별 서사, 검증 전환의 축, 국내 행동 과제를 묶는다. 각 장은 무엇이 바뀌었는지와 우리에게 무엇인지를 한 쌍으로 적는다.

독자가 가져갈 것은 세 가지다. 첫째 코퍼스가 가리키는 방향, 둘째 그 방향을 반박하는 증거, 셋째 국내 기관이 오늘 시작할 수 있는 일이다. 숫자는 모두 빌드 시점의 코퍼스에서 채워지며, 해석은 본문 집필본의 헤드라인과 시사점에 근거한다.

> [!tip] 정리
> 좋은 소식만 나열하지 않는다. 능력의 증거와 반증을 같은 비중으로 보고, 마지막에 국내 기관이 당장 할 수 있는 일로 닫는다.

---

## S02 · 이 지도는 어떻게 만들어졌나

*오프닝* · *방법*

> [!abstract] 화면에 띄울 한 줄
> 지도는 의미 유사도로 그렸다. 편수는 크기일 뿐 중요도가 아니며, 최신 쏠림이 있다.

**이 지도는 논문 2,709편을 임베딩하고 UMAP으로 낮춘 뒤 HDBSCAN으로 묶고, c-TF-IDF로 이름을 붙인 결과다. 사람이 먼저 칸을 정하지 않았기 때문에 경계에는 자의가 적지만, 해석의 책임은 읽는 쪽에 남는다.**

논문은 여러 칸에 동시에 배정될 수 있다. 그래서 편수를 두 가지로 센다. 하나는 논문이 가장 가까운 칸 하나에만 속하는 고유 배정 편수이고, 다른 하나는 다중 배정을 모두 센 중복 포함 편수다. 중복 포함 합계는 8,127편이다. 두 숫자의 차이가 큰 대분류는 다른 분야와 맞닿은 교차 영역이다.

대분류별 수치는 다음과 같다. 생체분자 생성 고유 625편(중복 1,252편); 자율 AI 과학 발견 고유 447편(중복 1,694편); 형식 수학 증명 고유 330편(중복 883편); LLM 추론·에이전트 벤치마크 고유 284편(중복 1,088편); 물리 기반 신경 시뮬레이션 고유 272편(중복 572편); 의료·신경 신호 고유 213편(중복 592편); 과학 문헌·동료심사 고유 210편(중복 463편); 멀티모달 인식·효율화 고유 113편(중복 434편); 인과·통계 추론 고유 108편(중복 590편); 계산 재료 시뮬레이션 고유 107편(중복 559편). 고유 배정은 분야의 몸집을, 중복 포함은 다른 분야에 얼마나 걸쳐 있는지를 보여 준다.

읽는 법의 첫 번째 주의는 편수와 중요도를 분리하는 것이다. 고유 배정만 나열하면 생체분자 생성 625편, 자율 AI 과학 발견 447편, 형식 수학 증명 330편, LLM 추론·에이전트 벤치마크 284편, 물리 기반 신경 시뮬레이션 272편, 의료·신경 신호 213편, 과학 문헌·동료심사 210편, 멀티모달 인식·효율화 113편, 인과·통계 추론 108편, 계산 재료 시뮬레이션 107편 순으로 읽히지만, 이 순위는 연구 활동의 양이지 영향력이 아니다. 작은 칸인 S48는 리더보드 1위의 의미를 흔들어 다른 대분류 전체의 평가 방식을 바꾼다.

중복 포함 편수로 다시 세면 그림이 달라진다. 같은 대분류를 생체분자 생성 1,252편, 자율 AI 과학 발견 1,694편, 형식 수학 증명 883편, LLM 추론·에이전트 벤치마크 1,088편, 물리 기반 신경 시뮬레이션 572편, 의료·신경 신호 592편, 과학 문헌·동료심사 463편, 멀티모달 인식·효율화 434편, 인과·통계 추론 590편, 계산 재료 시뮬레이션 559편 로 보면, 에이전트·검증·통계처럼 여러 분야를 가로지르는 주제의 존재감이 드러난다. 두 기준을 함께 읽어야 교차점이 보인다.

두 번째 주의는 최신 편향이다. 2025년 이후 논문이 83%이므로 지도는 현재의 관심사를 과장하고 오래된 기여를 눌러 담는다. 또 최신 논문은 피인용이 적어 영향력을 직접 측정하기 어렵다.

> [!tip] 정리
> 이 지도는 어디가 붐비는지 보여 주는 도구이지 어디가 옳은지 판정하는 도구가 아니다. 편수는 출발점이고, 판단은 본문 장의 근거에서 한다.

---

## S03 · 코퍼스 한눈에 보기

*오프닝* · *코퍼스*

> [!abstract] 화면에 띄울 한 줄
> 2,709편 중 1,852편이 2026년 논문이다. 이 분야는 2025년을 전후로 폭발했다.

**코퍼스 2,709편 가운데 2025년 이후가 83%다. 연도 분포는 완만한 성장이 아니라 계단식 급등이다. 2025년과 2026년에 몰린 양은 그 이전 전체를 압도한다.**

| 연도 | 편수 |  |
|---|---|---|
| 2018 | 7편 | █ |
| 2019 | 10편 | █ |
| 2020 | 11편 | █ |
| 2021 | 18편 | █ |
| 2022 | 17편 | █ |
| 2023 | 115편 | ██ |
| 2024 | 274편 | ████ |
| 2025 | 391편 | ██████ |
| 2026 | 1,852편 | ██████████████████████████████ |

2023년 이전의 논문은 소수다. 이들은 물리정보 신경망의 제안, AlphaFold의 구조 예측, 신경 증명기의 첫 시도처럼 이후 모든 분류가 기대는 뼈대다. 편수는 적어도 이 고전들이 질문의 틀을 정했다는 점을 놓치면 안 된다.

급증은 2023년부터 시작된다. 대규모 언어모델이 과학 문제로 들어오면서 에이전트, 형식 증명, 문헌 처리, 벤치마크가 한꺼번에 열렸다. 2025년이 변곡점이고 2026년은 그 위에서 폭발했다. 이 시기 논문은 새 능력을 보이는 것만큼 그 능력을 반박하는 것도 많이 낸다.

분포에는 코퍼스 구성의 효과도 섞여 있다. 최신 논문이 수집·분류에 유리하게 잡혔을 가능성이 있어 급증 폭을 분야의 실제 성장률로 읽으면 과장이다. 그러나 방향은 분명하다. 학계의 관심은 최근 2년에 집중됐다.

피인용 데이터는 이 덱의 약한 고리다. 2026년 논문은 인용이 거의 없어 영향력 순위를 만들 수 없다. 그래서 본문은 인용 대신 헤드라인에서 읽히는 전환, 즉 어떤 주장이 새로 나왔고 어떤 반증이 따라붙었는지를 기준으로 삼았다.

국내 관점에서 이 분포는 두 가지로 읽힌다. 하나는 후발 주자에게 불리하지 않다는 점이다. 대부분의 방법이 최근 2년 안에 나왔고 도구 다수가 공개돼 있어 처음부터 따라잡을 수 있다. 다른 하나는 정보 수명이 짧다는 점이다. 지금의 최선이 1년 뒤 기본값이 되거나 반증될 수 있으므로, 도입 결정은 반증 신호와 함께 갱신해야 한다.

> [!tip] 정리
> 시간축이 짧다는 것이 이 코퍼스의 성격이다. 결론은 확정된 사실이 아니라 지금 보이는 방향이며, 국내 기관에는 빠르게 따라붙을 수 있는 시점이라는 뜻이다. 요약하면 이 코퍼스는 역사서가 아니라 관측 기록이다. 고전은 좌표를, 최근 논문은 현재의 쟁점을 제공한다. 이 때문에 연도별 편수를 비교할 때는 절대값보다 증가의 방향과 시점을 보는 것이 안전하다.

---

## S04 · 10개 대분류의 지형

*오프닝* · *지형도*

> [!abstract] 화면에 띄울 한 줄
> 10개 대분류가 코퍼스를 나눈다. 상위 몇 곳이 대부분을 차지하고, 작은 칸이 검증을 맡는다.

**2,709편은 10개 대분류로 나뉘고, 서브카테고리는 95개다. 이 장은 지형 전체를 한 번에 훑는다. 고유 배정 기준으로 생체분자 생성 625편, 자율 AI 과학 발견 447편, 형식 수학 증명 330편, LLM 추론·에이전트 벤치마크 284편, 물리 기반 신경 시뮬레이션 272편, 의료·신경 신호 213편, 과학 문헌·동료심사 210편, 멀티모달 인식·효율화 113편, 인과·통계 추론 108편, 계산 재료 시뮬레이션 107편 이다.**

| 대분류 | 고유 배정 | 중복 포함 | 서브카테고리 | 최대 서브카테고리 |
|---|---|---|---|---|
| 생체분자 생성 모델링 | 625 | 1,252 | 20 | Single-Cell Gene Expression Modeling |
| 자율 AI 과학 발견 | 447 | 1,694 | 16 | Autonomous AI Scientist Agents |
| 형식 수학 정리 증명 | 330 | 883 | 13 | Verifiable RL for Reasoning |
| LLM 추론·에이전트 벤치마크 | 284 | 1,088 | 10 | Multi-Hop Chain-of-Thought Reasoning |
| 물리 기반 신경 시뮬레이션 | 272 | 572 | 9 | Physics-Informed Neural Operators |
| 의료·신경 신호 모델링 | 213 | 592 | 7 | EHR Foundation Models |
| 과학 문헌·동료심사 | 210 | 463 | 7 | Peer Review Feedback Datasets |
| 멀티모달 인식·효율화 | 113 | 434 | 5 | Multilingual Language Model Quantization |
| 인과·통계 추론 | 108 | 590 | 4 | Causal Independence Testing |
| 계산 재료 시뮬레이션 | 107 | 559 | 4 | Machine-Learned Interatomic Potentials |

중복 포함 기준의 편수는 다음과 같다. 생체분자 생성 1,252편, 자율 AI 과학 발견 1,694편, 형식 수학 증명 883편, LLM 추론·에이전트 벤치마크 1,088편, 물리 기반 신경 시뮬레이션 572편, 의료·신경 신호 592편, 과학 문헌·동료심사 463편, 멀티모달 인식·효율화 434편, 인과·통계 추론 590편, 계산 재료 시뮬레이션 559편. 합계는 8,127편이다. 고유 배정 순위와 나란히 놓으면 어느 분야가 교차점인지가 드러난다.

상위 세 곳, 생체분자 생성 모델링, 자율 AI 과학 발견, 형식 수학 정리 증명은 코퍼스의 절반 이상을 차지한다. 이 영역은 생성과 자율화의 전선이고, 동시에 반증이 가장 많이 쌓이는 곳이다. 단일세포 모델이 단순 베이스라인을 못 이긴다는 보고, 증명 채점자가 틀린 증명을 통과시킨다는 보고가 여기서 나왔다.

순위는 기준에 따라 뒤집힌다. 자율 AI 과학 발견는 고유 447편이지만 중복 포함에서는 1,694편으로 크게 늘어 최대 분류에 올라선다. 인과·통계 추론도 고유 108편에서 중복 590편으로 뛴다. 에이전트와 통계 검증이 다른 분야에 스며든 정도를 보여 준다.

작은 대분류를 얕잡아 볼 수 없다. 계산 재료 시뮬레이션은 107편이지만 해자가 DFT 계산 데이터라는 점을 분명히 했고, 멀티모달 인식·효율화는 113편 안에서 양자화와 도표 이해의 동등성 검증 공백을 드러낸다.

이후 본문은 이 순서로 대분류를 하나씩 다룬다. 각 대분류는 서브카테고리 단위로 2025–2026의 변화와 국내 시사점을 짝지어 적는다.

> [!tip] 정리
> 지형의 요점은 큰 칸은 생성, 작은 칸은 검증이라는 비대칭이다. 이 비대칭이 종합 장의 검증 전환 논의로 이어진다.

---

## S05 · AI4S 서사: 예측에서 생성, 그리고 검증으로

*오프닝* · *서사*

> [!abstract] 화면에 띄울 한 줄
> 구조 예측이 풀린 뒤 생성과 자율화가 확산됐고, 2026년에는 검증이 경쟁축이 됐다.

**AI4S의 지난 십수 년은 예측에서 생성으로, 생성에서 검증으로 질문이 바뀌어 온 과정이다. 코퍼스 2,709편은 그 마지막 구간, 검증의 시대 초입을 촘촘히 담고 있다.**

출발점은 학습으로 과학 계산을 대체할 수 있다는 증명이었다. 물리정보 신경망이 방정식을 손실에 넣었고, AlphaFold가 원자 수준 구조 예측을 달성했으며, GPT-f가 신경망 증명이라는 흐름을 열었다. 이 세 사건이 이 코퍼스의 뼈대다.

2022–2023년에는 규모가 발견을 대신하기 시작했다. Pangu-Weather가 수치예보를 처음 넘어섰고 GNoME은 대량의 안정 결정 구조를 제시했다. 이때까지의 질문은 AI가 되는가였다.

2025년에 질문은 AI가 스스로 하는가로 바뀌었다. AI Scientist-v2가 가설·실험·집필을 자율 수행해 심사를 통과한 논문을 냈고, Kosmos는 대규모 롤아웃으로 보고서를 만들었으며, Polybot은 자율 실험실이 소재 합성 폐루프를 닫을 수 있음을 보였다. 에이전트가 과학 연구의 한 단계가 아니라 전 과정으로 확장됐다.

2026년은 두 방향이 동시에 진행됐다. 한쪽에서 Robin이 신약 후보를 실험으로 확인하고 BFS-Prover-V2가 검증기를 보상으로 쓰며 성과를 냈다. 다른 쪽에서 Ground False가 자동 형식화의 절반 이상이 문제 있다고 밝히고, QEDBench가 채점자의 점수 부풀림을, The Leaderboard Lottery가 순위의 불확실성을 보였다.

이 두 흐름이 합쳐진 지점이 검증기 결합 아키텍처다. 생성 에이전트에 Lean, 물리 시뮬레이터, 통계 검정을 붙이는 설계가 여러 대분류에서 같은 모양으로 나타났다. 생성하고 검증하고 반복하는 루프가 새로운 표준 설계다.

> [!tip] 정리
> 서사의 결론은 단순하다. 생성이 무료가 된 뒤에는 무엇을 믿을 수 있느냐가 가치를 결정한다. 이 덱의 나머지는 그 믿음을 어떻게 만드는지에 대한 증거 수집이다. 검증 전환은 한 분야의 사건이 아니라 열 개 대분류가 각자의 방식으로 같은 시기에 도달한 지점이라는 점이 이 코퍼스의 가장 강한 신호다.

---

## S06 · 단일세포 발현 모델링

*제1부 · 생체분자 생성 모델링* · **Single-Cell Gene Expression Modeling** · *서브카테고리*

`121편` `2018–2026` `가속` `2025+ 113편`

<sub>생체분자 생성 모델링 고유 배정 625편(중복 포함 1,252편 · 웹 인덱스 기준) · 서브카테고리 20개 · 본 파트 5개로 48% 커버</sub>

> [!quote] 파트 도입
> 코퍼스 최대 분류. 생성은 흔해졌고, 경쟁축은 합성가능성·베이스라인 반증·실험 검증으로 넘어갔다.

> [!abstract] 화면에 띄울 한 줄
> 단일세포 파운데이션 모델은 확산됐지만, 베이스라인 반증이 동시에 쌓이는 중이다.

**121편 중 113편이 2025년 이후다. 코퍼스에서 가장 큰 칸이며, 같은 해에 모델이 커지는 이야기와 그 모델이 정말 필요한지 따지는 이야기가 함께 나온다.**

흐름의 출발은 SCANPY로 대표되는 확장 가능한 분석 도구(2018–2021)다. 이후 Geneformer/Genecorpus-104M 같은 단일세포 파운데이션 모델이 나왔고, 2025년에는 Cell2Sentence-Scale이 단일세포 RNA 시퀀싱 데이터를 ‘세포 문장’ 텍스트로 바꿔 LLM으로 처리하는 방식을 270억 개 파라미터로 확장해 전사체와 생물학 텍스트를 한 플랫폼에 묶었다.

2026년의 확장은 모달리티 방향이다. PhenoSeq는 Cell Painting 이미징 특징에서 조건부 확산 모델로 scGPT 기반 단일세포 전사체 임베딩을 생성해, 이미지에서 전사체로 가는 생성적 매핑이 약물 발굴에 쓸모 있음을 보인다. HistoTx는 H&E 이미지와 공간 전사체를 토큰 수준에서 조기 융합하고, ChronoTILE는 흩어진 단면 스냅샷에서 조직 리모델링의 연속시간 동역학을 flow matching으로 학습한다.

응용 쪽에서는 Hepa-RAFT가 SMILES에서 가상 간세포 유전자 발현 프로파일을 생성하고, 이를 검색 키로 삼아 소규모 라벨 참조셋에서 약물유발 간손상 위험을 예측한다. gCRL은 유전자 조절 네트워크의 전사인자 군집을 인과 표현 학습의 잠재공간 귀납 편향으로 쓰고, 반사실적 인과 기여를 근사하는 erlotinib 반응 연구도 같은 인과 흐름에 있다. 생성 모델이 ‘가상 세포’ 시뮬레이터로 쓰이기 시작했다.[1]

비판적 전환은 dossier 의 타임라인에 명시돼 있다. ‘단일세포 파운데이션 모델과 그 비판(2023–2026)’, ‘섭동 반응 예측과 베이스라인 청산(2024–2026)’이 별도 흐름으로 잡혀 있고, 대표 도구에 GEARS/CPA 같은 섭동 예측 기준선이 올라 있다. 사전학습된 거대 모델이 단순한 기준선과 비교되고 감사받는 단계에 들어섰다는 뜻이다. 이 칸의 성과 주장은 베이스라인 설계를 확인한 뒤에 읽어야 한다.

국내 관점에서 시사점은 두 가지다. 첫째, 공개 파운데이션 모델은 이미 많으므로 모델 자체보다 섭동·공간 전사체 실험 데이터와 평가 프로토콜이 차별 자산이다. 둘째, 가상 세포 예측을 독성·약효 심사에 쓰려면 단순 베이스라인 대비 이득을 자체 데이터로 반복 검증할 수 있어야 한다.

> [!tip] 정리
> 이 칸은 규모의 경쟁이 아니라 반증 가능성의 경쟁으로 넘어가는 중이다. 베이스라인을 설계하고 감사하는 능력이 모델을 만드는 능력만큼 값어치를 갖는다.

**대표 도구·시스템** — SCANPY · Geneformer/Genecorpus-104M · Tahoe-X1 · Cell2Sentence-Scale · Intermediate-Layers · CLAMP · GEARS/CPA · PerturbDiff

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Hepa-RAFT: Retrieval-Augmented Virtual Hepatocyte Responses for Hepatotoxicity Prediction](../../docs/papers/9775_Hepa-RAFT_Retrieval-Augmented_Virtual_Hepatocyte_Responses_f/index.html) — Youngseok Choi 외, 2026 · 인용 2,624
2. [Bridging Gene Regulatory Networks and Causal Representation Learning in Single-Cell Genomics Data](../../docs/papers/9358_Bridging_Gene_Regulatory_Networks_and_Causal_Representation/index.html) — Vincenzo Lagani 외, 2026 · 인용 3,730
3. [Multi-Scale Flow Matching for Continuous-time Generative Modeling of Spatiotemporal Tissue Dynamics from Spatial Transcriptomics](../../docs/papers/10069_Multi-Scale_Flow_Matching_for_Continuous-time_Generative_Mod/index.html) — Pinar Demetci 외, 2026 · 인용 1,884
4. [Celcomen: spatial causal disentanglement for single-cell and tissue perturbation modeling](../../docs/papers/3051_Celcomen_spatial_causal_disentanglement_for_single-cell_and/index.html) — Stathis Megas 외, 2026.03 · 인용 8
5. [PerturbDiff: Functional Diffusion for Single-Cell Perturbation Modeling](../../docs/papers/10174_PerturbDiff_Functional_Diffusion_for_Single-Cell_Perturbatio/index.html) — Xinyu Yuan 외, 2026
6. [Scalable Single-Cell Gene Expression Generation with Latent Diffusion Models](../../docs/papers/10372_Scalable_Single-Cell_Gene_Expression_Generation_with_Latent/index.html) — Giovanni Palla 외, 2026

---

## S07 · 단백질 언어모델 상호작용

*제1부 · 생체분자 생성 모델링* · **Protein Language Model Interactions** · *서브카테고리*

`53편` `2023–2026` `가속` `2025+ 51편`

> [!abstract] 화면에 띄울 한 줄
> 단백질 언어모델은 서열 표현을 넘어 상호작용·적합도·구조를 결합하는 단계로 갔다.

**53편 중 51편이 2025년 이후다. 칸의 중심은 서열 표현 자체가 아니라 그 표현을 상호작용과 기능 예측에 어떻게 쓰느냐로 옮겨 갔다.**

진화 규모 서열 모델은 2023–2024년 ESMFold/ESM-2와 ProtT5로 기준선이 정해졌다. 2026년 논문들은 이 기준선을 그대로 쓰되 위에 무엇을 얹느냐로 갈린다. ProteomeLM은 개별 단백질이 아니라 proteome 전체를 입력해 masked 임베딩 재구성만으로 학습하는데, 상호작용 라벨 없이도 attention 계수가 단백질-단백질 상호작용을 포착하고 유전자 필수성까지 분류군을 가로질러 예측한다.[3]

구조와 진화 정보를 더하는 방향도 뚜렷하다. ProtEGNN 은 PLM 서열 표현에 단백질 3D 좌표를 경량 E(3)-등변 GNN 으로 결합해, 대규모 파인튜닝 없이 7개 벤치마크에서 100-1000배 적은 파라미터로 SOTA급 성능을 보였다. E1 은 상동 서열을 block-causal multi-sequence attention 으로 조건화해 zero-shot fitness 와 contact 예측을 올렸고, SaNano 는 VHH 서열에 Foldseek 3Di 구조 토큰을 LoRA 로 결합했다. 입력을 늘리는 대신 헤드를 가볍게 하는 전략이다.

아키텍처 효율화도 한 축이다. PRIMA 는 bidirectional Mamba 로 선형 복잡도 PPI 모델을 만들어 같은 규모의 transformer baseline 대비 긴 서열과 길이 외삽에서 낮은 비용을 보였다. Ares 는 loss-free MoE 라우팅을 단백질 인코더에 처음 도입해 Soft-MoE 가 안정적이고 ESM-2 대비 1/25 토큰으로 일부 과제에서 견줄 만하다고 밝혔다. ProtoCol 은 residue 단위 late interaction 으로 먼 상동체 검색을 개선한다.[4][5]

내부 동작과 일반화에 대한 감사도 나왔다. 단백질 언어 모델이 자연어 모델과 내부 메커니즘에서 근본적으로 다르다는 분석은 동적 early-exit 로 이어졌고, 다중 모달 VEP 연구는 DNA 언어 모델 신호가 PLM 단독 모델의 실패 지점, 특히 양전하 잔기를 교정함을 29개 ProteinGym DMS 데이터셋에서 보였다. MutAtlas 는 에너지 모델·PLM·inverse folding 의 불일치를 명시적으로 모델링한다.

국내 관점에서는 범용 PLM 학습에 경쟁하기보다 공개 모델 위에 표적 특화 상호작용·fitness 헤드를 얹는 쪽이 현실적이다. 대신 돌연변이 효과 예측처럼 PLM 이 실패하는 구간이 어디인지를 자체 실험 데이터로 확인하는 평가 체계가 필요하다.

> [!tip] 정리
> 모델 크기는 더 이상 차별점이 아니다. 어떤 입력을 더하고 어디서 실패하는지를 아는 팀이 PLM 의 가치를 가져간다.

**대표 도구·시스템** — ESMFold/ESM-2 · ProtT5 · ProtGPT2 · ProteomeLM · IsoPLM · PRIMA · FlashPPI · ProMaya

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Just Add Structure: Protein Language Models Combined with Structural Equivariance Excel at Protein Tasks](../../docs/papers/9859_Just_Add_Structure_Protein_Language_Models_Combined_with_Str/index.html) — Qurat ul ain 외, 2026 · 인용 16,139
2. [Protein Language Models Diverge from Natural Language: Comparative Analysis and Improved Inference](../../docs/papers/3221_Protein_Language_Models_Diverge_from_Natural_Language_Compar/index.html) — 2026.02 · 인용 3,225
3. [ProteomeLM: A Proteome-Scale Language Model Enables Accurate and Rapid Prediction of Protein-Protein Interactions and Gene Essentiality Across Taxa](../../docs/papers/10267_ProteomeLM_A_Proteome-Scale_Language_Model_Enables_Accurate/index.html) — Cyril Malbranke 외, 2026 · 인용 763
4. [PRIMA: a bidirectional state-space architecture and training approach for sequence modelling of protein-protein interactions](../../docs/papers/10235_PRIMA_a_bidirectional_state-space_architecture_and_training/index.html) — Arturo Fiorellini-Bernardis 외, 2026 · 인용 599
5. [ProtoCol: Late Interaction Retrieval for Protein Homolog Search](../../docs/papers/10270_ProtoCol_Late_Interaction_Retrieval_for_Protein_Homolog_Sear/index.html) — Gabrielle Cohn 외, 2026 · 인용 349
6. [From single-sequences to evolutionary trajectories: protein language models capture the evolutionary potential of SARS-CoV-2](../../docs/papers/3109_From_single-sequences_to_evolutionary_trajectories_protein_l/index.html) — Kieran D. Lamb 외, 2026.02 · 인용 7

---

## S08 · 이산 확산 분자 생성

*제1부 · 생체분자 생성 모델링* · **Discrete Diffusion Molecule Generation** · *서브카테고리*

<sub>타임라인 분석 명칭: Discrete Diffusion & Flow Molecule Generation</sub>

`43편` `2018–2026` `가속` `2025+ 42편`

> [!abstract] 화면에 띄울 한 줄
> 분자 생성의 질문이 ‘만들 수 있나’에서 ‘합성되고 개발 가능한가’로 바뀌었다.

**43편 중 42편이 2025년 이후다. 2018년 MolGAN 의 그래프 생성에서 출발한 계보가 이산 확산과 flow matching 으로 옮겨 온 뒤, 2026년에는 합성가능성이 설계의 일부가 됐다.**

그래프 생성의 기원(2018–2023) 뒤에 2024–2026년 이산 확산과 flow matching 이 분자 생성의 기본 틀이 됐다. CoCoGraph 는 Double Edge Swapping 으로 화학적 제약을 확산 과정 안에 내장해 100% 화학적으로 유효한 분자를 만들고, Diffusion model 과 Time model 의 협력으로 더 적은 매개변수에서 더 현실적인 분자를 얻는다. 유효성은 사후 필터가 아니라 모델 구조의 성질이 됐다.

더 큰 전환은 합성가능성의 내재화다. S3-GFN 은 사전학습 SMILES 언어모델 GP-MolFormer 를 prior 로 GFlowNet 후학습을 하며 합성 가능·불가능 샘플의 replay buffer 와 대조 보조 손실로 합성가능성을 soft 하게 강제한다. SynLaD 는 3D 약리단 조건에서 3D 구조와 합성 경로를 한 잠재공간에서 함께 생성하고, REINVENT 의 사용자 prior 평가는 Freedom Space 4.0 과 REAL Space 같은 합성 접근 가능 공간 안에 에이전트를 묶어 둔다.[1][6]

개발가능성 쪽에서는 GenMol 이라는 masked discrete diffusion 모델에 Iterative Importance Fine-Tuning(IIFT)을 적용해 ADMET 와 합성 접근성을 동시에 만족하도록 분포를 옮긴다. CupOFLATTE 는 PROTAC 의 warhead·linker·E3 리간드를 따로 설계해 조립하던 방식을 버리고 결합된 discrete flow 에서 동시에 생성해 조립 단계의 화학적 유효성을 생성 내내 보장한다. K-BTS 는 LLM 기반 구조 기반 설계를 DMTA 사이클 안에서 bandit 으로 돌린다.[3]

수학적 기반 작업도 병행된다. canonicalization 으로 등변 아키텍처 없이 대칭 불변 분포를 학습하는 접근, 분자 크기에 맞게 prior 를 재조정하는 Scaling the Prior, GFlowNet 을 재학습 없이 추론 시점에 합성하는 Routing by Reaching, 표본 효율을 높이는 SEGO 가 있다. 다만 이 칸 논문의 상당수는 인용이 거의 없어 아직 검증 초기 단계다.[1][2]

국내 관점에서 시사점은 생성기 개발보다 제약·평가 조합에 있다. 사내 합성 가능 화학공간과 ADMET 목적함수를 prior 와 reward 로 연결하는 작업은 공개 모델 위에서 가능하며, 여기서 만든 후보가 실제로 합성되는 비율을 기록하는 일이 차별화 근거가 된다.

> [!tip] 정리
> 유효한 분자를 만드는 일은 끝났다. 이제 쓸 만한 분자의 정의, 곧 합성 가능성과 개발 가능성을 누가 더 정확히 모델 안에 넣느냐가 승부다.

**대표 도구·시스템** — MolGAN · CoCoGraph · MolHIT · MoCDiff · GenMol/IIFT · Graph-GRPO · InertialAR · MotiFlow

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Routing by Reaching: Composition of Pre-trained GFlowNets for Multi-Objective Generation](../../docs/papers/10353_Routing_by_Reaching_Composition_of_Pre-trained_GFlowNets_for/index.html) — Seokwon Yoon 외, 2026
2. [Scaling the Prior: Size-Consistent Geometric Diffusion for 3D Molecular Generation](../../docs/papers/10378_Scaling_the_Prior_Size-Consistent_Geometric_Diffusion_for_3D/index.html) — Wenhan Gao 외, 2026
3. [CupOFLATTE: Coupled Objective-Guided Discrete Flows via Linker Assembly for Targeted PROTAC Engineering](../../docs/papers/9468_CupOFLATTE_Coupled_Objective-Guided_Discrete_Flows_via_Linke/index.html) — Ziang Li 외, 2026 · 인용 157
4. [A collaborative constrained graph diffusion model for the generation of realistic synthetic molecules](../../docs/papers/2984_A_collaborative_constrained_graph_diffusion_model_for_the_ge/index.html) — Manuel Ruiz-Botella 외, 2026.05 · 인용 3
5. [Rethinking Diffusion Models with Symmetries through Canonicalization with Applications to Molecular Graph Generation](../../docs/papers/10330_Rethinking_Diffusion_Models_with_Symmetries_through_Canonica/index.html) — Cai Zhou 외, 2026
6. [SynLaD: Latent Diffusion for Generating Synthesizable Molecules Conditioned on 3D Pharmacophore Profiles](../../docs/papers/10527_SynLaD_Latent_Diffusion_for_Generating_Synthesizable_Molecul/index.html) — Miruna Cretu 외, 2026

---

## S09 · 역합성 반응 예측

*제1부 · 생체분자 생성 모델링* · **Retrosynthesis Reaction Prediction** · *서브카테고리*

`41편` `2025+ 31편`

> [!abstract] 화면에 띄울 한 줄
> 역합성은 LLM 에이전트로 옮겨 가는 동시에 평가 지표 자체를 의심받고 있다.

**41편 중 31편이 2025년 이후다. 역합성 예측은 템플릿과 트랜스포머를 넘어 LLM 에이전트가 경로를 계획하는 단계로 갔고, 같은 시기에 평가가 틀렸다는 지적도 나왔다.**

단일단계 예측은 모듈화됐다. RETROSPECT 는 ChemAlign Transformer 제안 모델과 LambdaMART 리랭커를 결합해 역합성을 proposal-selection 분해로 보고 USPTO-50K 에서 강한 top-1/top-10 정확도를 보였다. ChemDual 은 BRICS 기반 440만 개 분자 데이터셋과 이중 과제 학습으로 LLM 의 데이터 부족 문제를 다룬다. 그러나 이 접근은 정답 하나를 맞히는 틀 안에 있다.[4]

2025–2026년의 핵심은 에이전트화다. RetrOrchestrator 는 다단계 역합성을 POMDP 로 재정의해, 각 단계에서 확장할 분자뿐 아니라 어떤 단일단계 모델을 도구로 쓸지 LLM 이 동적으로 고르고 scaffold-aware 강화학습(SA-GRPO)으로 희소 보상을 해결한다. LARC 는 발암물질 회피나 자연발화물질 제거 같은 제약 아래 계획을 세워 72.9% 성공률로 기존 LLM 방법을 크게 앞섰고, Synthegy 는 검색 알고리즘이 낸 후보를 자연어 전략 지시로 평가해 71.2% 전문가 일치율을 얻었다.[6]

해석 가능성과 대상 확장도 이어진다. Retro-Expert 는 전문 모델의 화학 지식과 LLM 추론을 결합해 순수 RL 로 자연어 추론 과정을 생성한다. Retro-Forge 는 고체 물질 합성에서 전구체 예측을 다단계 pairwise 반응 연쇄와 tree search 로 푼다. TotSyn 은 Organic Letters, JACS, Angewandte Chemie 의 전합성 반응으로 USPTO 계열보다 템플릿 다양성과 최장 선형 서열이 높은 데이터셋을 제시했다.[1][2][7]

비판적 전환이 가장 중요하다. ‘When Single Answer Is Not Enough’ 는 단일 정답 Top-K accuracy 가 타당한 대안 경로를 오답 처리한다고 보고 화학적 타당성 지표 ChemCensor, 대규모 데이터셋 CREED, 전문가 검증 벤치마크 URSA-expert-2026 을 제안했다. 한 position 논문은 AI 신약 모델이 의도한 생물·화학 특징 대신 데이터 아티팩트와 표적 분포에 기대고 있다며 misaligned baselines 진단을 제안한다. 이 분야의 정확도 수치는 그대로 믿기 어렵다.[3]

국내 관점에서 시사점은 분명하다. 합성 계획 에이전트는 공개 모델과 LLM 으로 조립할 수 있으나, 평가는 직접 해야 한다. 자사 화학 전문가가 검증한 타당성 기준과 전합성 수준의 어려운 사례 세트를 갖춘 팀만 에이전트가 실제로 쓸모 있는지 판단할 수 있다.

> [!tip] 정리
> 역합성의 병목은 모델이 아니라 잣대다. 타당성을 재는 지표와 어려운 사례 데이터를 가진 쪽이 에이전트의 진위를 판별한다.

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Retro-Expert: Collaborative Reasoning for Interpretable Retrosynthesis](../../docs/papers/10337_Retro-Expert_Collaborative_Reasoning_for_Interpretable_Retro/index.html) — Xinyi Li 외, 2026
2. [Retro-Forge: A Multi-Step Pairwise Retrosynthesis Framework for Solid-State Materials Synthesis](../../docs/papers/10338_Retro-Forge_A_Multi-Step_Pairwise_Retrosynthesis_Framework_f/index.html) — Juhan Hong 외, 2026
3. [When Single Answer Is Not Enough: Rethinking Single-Step Retrosynthesis Benchmarks for LLMs](../../docs/papers/10711_When_Single_Answer_Is_Not_Enough_Rethinking_Single-Step_Retr/index.html) — Bogdan Zagribelnyy 외, 2026
4. [RETROSPECT: RETROsynthesis via Sequential Prediction, and Chemically Transformed-ranking](../../docs/papers/10340_RETROSPECT_RETROsynthesis_via_Sequential_Prediction_and_Chem/index.html) — Raja Sekhar Pappala 외, 2026 · 인용 241
5. [Enhancing chemical reaction and retrosynthesis prediction with large language model and dual-task learning](../../docs/papers/316_Enhancing_chemical_reaction_and_retrosynthesis_prediction_wi/index.html) — Xuan Lin 외, 2025 · 인용 3
6. [RetrOrchestrator: A Multi-Step Retrosynthesis Agent Dynamically Orchestrating Single-Step Transition Models](../../docs/papers/10339_RetrOrchestrator_A_Multi-Step_Retrosynthesis_Agent_Dynamical/index.html) — Liao Chang 외, 2026
7. [TotSyn: A Total Synthesis Reaction Dataset for Machine Learning in Organic Chemistry](../../docs/papers/10605_TotSyn_A_Total_Synthesis_Reaction_Dataset_for_Machine_Learni/index.html) — Chaewon Lee 외, 2026

---

## S10 · 유전체 파운데이션 모델

*제1부 · 생체분자 생성 모델링* · **Genomic Foundation Models** · *서브카테고리*

`40편` `2019–2026` `가속` `2025+ 37편`

> [!abstract] 화면에 띄울 한 줄
> 유전체 모델은 길고 넓은 입력으로 커지며, 토큰화와 사전학습 목적을 다시 묻는다.

**40편 중 37편이 2025년 이후다. 규모가 커진 뒤, 2026년에는 입력 표현과 사전학습 목적, 내부 층의 역할을 다시 묻는 논문이 몰렸다.**

2025년의 두 이정표는 Evo 2 와 AlphaGenome 이다. Evo 2 는 9.3조 염기쌍으로 학습한 7B·40B 모델에 1백만 토큰 컨텍스트를 줘 모든 생명 영역의 게놈 모델링과 설계를 수행한다. AlphaGenome 은 1메가베이스 입력과 단일 염기쌍 해상도로 유전자 발현·스플라이싱·크로마틴 접근성·3D 크로마틴 구조 등 11개 모달리티의 5,930개 게놈 트랙을 한 번에 예측해 조절 변이 효과 예측을 통합한다.[3]

규모의 법칙도 다뤄졌다. EDEN 은 최대 28B 파라미터, 9.7조 뉴클레오타이드 토큰으로 학습한 metagenomic 모델 계열로 Transformer(Llama 계열), Mamba, Hyena 를 비교하며 대규모에서 Transformer 의 scaling 효율이 더 낫다고 보고했다. 길이를 늘린 상태 공간 모델이 우세하리라는 기대가 꼭 맞지는 않았다는 신호이며, 아키텍처 선택에 실험적 근거를 요구한다.

2026년의 신선한 흐름은 토큰화 재검토다. LDARNet 과 DNAChunker 는 k-mer, BPE, 단일 염기 같은 고정 토큰화 대신 학습 가능한 경계로 DNA 를 분절하고, OpticalDNA 는 서열을 2차원 문서 이미지로 렌더링해 OCR 스타일 비전-언어 모델로 학습한다. 진화 속도(PhyloP) 예측을 사전학습 과제로 쓰면 zero-shot 벤치마크에서 표현이 더 의미 있어진다는 연구도 같은 맥락이다.[4][5]

감사 쪽 신호도 있다. ‘Representative vs. Load-bearing Layers’ 는 NT-v2 와 Evo 2 에서 단일 특징 판별력이 가장 높은 층과 분류기가 실제로 의존하는 층이 다르다는 분리를 보였다. 마지막 층 표현에 의존하는 관행이 위험할 수 있다는 뜻이다. 한편 nested birth-death process 는 30,000개 파라미터로 수천만 파라미터 신경망 모델과 견줄 만한 perplexity 를 내, 작은 모델 기준선의 중요성을 상기시킨다.[1]

생성·설계 응용은 PlasmidLM 이 대표적이다. 부품 명세 토큰을 프롬프트로 받아 multi-kilobase plasmid 를 한 번에 생성하고 GRPO 기반 검증 가능 보상으로 useful-plasmid rate 를 개선한다. 국내에서는 최대 모델을 만들 일이 아니라, 검증 가능한 보상과 임상·합성생물학 응용(OptiPrime 의 프라임 편집 예측, ctDNA 혼합 모델)에 공개 모델을 접목하는 쪽이 현실적이다.

> [!tip] 정리
> 유전체 모델은 이제 크기만으로 평가받지 않는다. 입력 표현, 층별 역할, 작은 모델 기준선을 함께 확인하는 팀이 결과를 신뢰할 수 있다.

**대표 도구·시스템** — AlphaGenome · Seq2Exp · BlueSTARR · Hi-Compass · Evo 2 · EDEN · LDARNet · BioToken/BioFM

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Representative vs. Load-bearing Layers: A Dissociation in Genomic Foundation Models](../../docs/papers/10324_Representative_vs_Load-bearing_Layers_A_Dissociation_in_Geno/index.html) — Yoonjin Cho 외, 2026 · 인용 146
2. [Scaling Laws and Architectural Frontiers in Metagenomic Foundation Models](../../docs/papers/10375_Scaling_Laws_and_Architectural_Frontiers_in_Metagenomic_Foun/index.html) — Geraldene Munsamy 외, 2026 · 인용 519
3. [AlphaGenome: advancing regulatory variant effect prediction with a unified DNA sequence model](../../docs/papers/094_AlphaGenome_advancing_regulatory_variant_effect_prediction_w/index.html) — Žiga Avsec 외, 2025 · 인용 110
4. [LDARNet: DNA Adaptive Representation Network with Learnable Tokenization for Genomic Modeling](../../docs/papers/9884_LDARNet_DNA_Adaptive_Representation_Network_with_Learnable_T/index.html) — Daria Ledneva 외, 2026 · 인용 104
5. [DNACHUNKER: Learnable Tokenization for DNA Language Models](../../docs/papers/9536_DNACHUNKER_Learnable_Tokenization_for_DNA_Language_Models/index.html) — Taewon Kim 외, 2026 · 인용 11
6. [BioToken and BioFM – Biologically-Informed Tokenization Enables Accurate and Efficient Genomic Foundation Models](../../docs/papers/9340_BioToken_and_BioFM__Biologically-Informed_Tokenization_Enabl/index.html) — Aleksandr Medvedev 외, 2026

---

## S11 · 자율 AI 과학자 에이전트

*제2부 · 자율 AI 과학 발견* · **Autonomous AI Scientist Agents** · *서브카테고리*

`70편` `2021–2026` `가속` `2025+ 62편`

<sub>자율 AI 과학 발견 고유 배정 447편(중복 포함 1,694편 · 웹 인덱스 기준) · 서브카테고리 16개 · 본 파트 5개로 49% 커버</sub>

> [!quote] 파트 도입
> 폐루프 시연은 실험실에서 현실이 됐고, 추론 규범 위반의 증거도 같은 해에 쌓였다. 결과물보다 검증 체계가 경쟁력이다.

> [!abstract] 화면에 띄울 한 줄
> 논문을 쓰는 AI 과학자는 등장했고, 평가의 무게는 결과물에서 과정 추적으로 옮겨갔다.

**70편. 이 칸의 질문은 AI가 과학자 역할을 할 수 있는가에서, 그 결과를 어떻게 믿을 것인가로 바뀌었다. 시연은 충분히 쌓였고, 반증과 감사도 같은 속도로 쌓이고 있다.**

2024년 The AI Scientist가 아이디어 생성부터 원고 작성까지 한 줄로 잇는 파이프라인을 보였고, 2025년 AI Scientist-v2가 에이전트 트리 서치를 도입해 가설 수립, 실험 설계·실행, 분석과 시각화, 논문 작성을 자율 수행했다. 이 시스템이 낸 논문은 동료 심사를 통과한 최초의 AI 생성 학술 논문이 됐고, 2026년 Towards end-to-end automation of AI research는 같은 계보를 아이디어에서 동료 검토까지의 전 수명주기 자동화로 정리했다. 최근 62편이 쏟아졌다는 사실이 이 흐름의 속도를 말해 준다.[4][5][7]

규모를 키우는 접근도 나왔다. DeepScientist는 과학적 발견을 Bayesian Optimization 문제로 형식화하고 hypothesize-verify-analyze 평가와 누적 Findings Memory로 탐색과 활용을 조절한다. 20,000 GPU시간을 써서 약 5,000개의 아이디어를 만들고 1,100개를 실험으로 검증했다. AgentRxiv는 에이전트들이 공유 프리프린트 서버로 서로의 결과를 읽고 쌓게 했고, ToolUniverse는 600개 이상의 모델·데이터셋·API를 묶어 어떤 LLM으로도 AI 과학자를 조립하게 하는 오픈소스 생태계를 열었다. 진입장벽은 낮아지는 중이다.[8]

그러나 같은 칸에서 간극이 드러난다. 2025년 EXP-Bench는 end-to-end 성공률을 0.5%로 보고했다. NeuriCo는 20주간 180회의 에이전트 실행을 관찰해 실행(execution)에는 강하고 연구 품질 판단(judgment)에는 구조적으로 약하다는 meta-intelligence gap을 규명했다. What the Records Don't Carry는 130회 이상의 실제 협업에서, 공식 기록에 담기지 않은 연구자의 암묵적 판단을 AI가 그럴듯한 완성으로 메운다고 보였다. 논문 한 편을 통과시키는 능력과 연구를 믿을 만하게 수행하는 능력은 다르다. 2026년 INTO THE UNKNOWN은 이 간극을 열린 문제로 확인했다. 에이전트에게 미공개 연구 방향을 주고 후속 논문을 쓰게 한 뒤 해당 분야 과학자가 정한 성공 조건과 무결성 조건으로 평가했는데, 9개 최신 agent가 쓴 135편 중 조건을 모두 만족한 논문은 하나도 없었다.[2][3][9]

그래서 2026년의 평가 도구는 결과물이 아니라 과정을 본다. OpenDiscoveryTrace는 558개 trajectory를 9-필드 구조로 기록해, output-only 평가에서는 보이지 않던 모델 간 에러 유형과 자기 수정 패턴의 차이를 드러냈다. ClaimGarden은 자동화의 단위를 논문이 아니라 개별 claim의 상태로 바꿔 증거가 갱신되면 재검증하게 한다. Negative Knowledge는 실패한 시도를 재사용 가능한 기록으로 남겨 후속 에이전트가 채택하거나 기각하도록 강제한다. 또 Artificial intelligence tools expand scientists' impact but contract science's focus는 AI 도구 채택이 개인의 영향력을 키우는 반면 집단 과학의 탐색 범위를 좁힌다고 41.3백만 편 데이터로 보였다.[1][6]

국내 기관에는 두 가지 시사점이 있다. 첫째, 에이전트를 직접 만드는 비용은 ToolUniverse 같은 공개 기반으로 크게 내려갔으므로 구축 능력은 차별점이 아니다. 둘째, 도입의 병목은 검증이다. 최종 논문이 아니라 과정 추적과 인간 체크포인트를 요구하는 내부 기준을 먼저 세우고, 에이전트 산출물의 공동 탐색 축소 효과까지 감안해 연구 포트폴리오를 설계해야 한다.[8]

> [!tip] 정리
> AI 과학자의 시연은 이미 충분하다. 앞으로 가치는 무엇을 만들 수 있느냐가 아니라, 만든 것이 어떻게 추론됐는지 보여 줄 수 있느냐에 붙는다.

**대표 도구·시스템** — The AI Scientist / AI Scientist-v2 · AI-Researcher + Scientist-Bench · DeepScientist · MLR-Bench · EXP-Bench · AIRS-Bench · Curie · MARS · AutoSOTA · OpenDiscoveryTrace · FabScore · AgentRxiv · aiXiv

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Artificial intelligence tools expand scientists’ impact but contract science’s focus](../../docs/papers/107_Artificial_intelligence_tools_expand_scientists_impact_but_c/index.html) — Qianyue Hao 외, 2026.01 · 인용 105
2. [Into the Unknown: Benchmarking AI agents on open scientific research problems](../../docs/papers/11482_Into_the_Unknown_Benchmarking_AI_agents_on_open_scientific_r/index.html) — Seungone Kim 외, 2026.10
3. [Exp-bench: Can ai conduct ai research experiments? arXiv preprint arXiv:2505.24785, 2025.](../../docs/papers/326_Exp-bench_Can_ai_conduct_ai_research_experiments_arXiv_prepr/index.html) — Patrick Tser Jern Kon 외, 2025 · 인용 1
4. [The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery](../../docs/papers/795_The_AI_Scientist_Towards_Fully_Automated_Open-Ended_Scientif/index.html) — Chris Lu 외, 2024 · 인용 115
5. [Towards end-to-end automation of AI research](../../docs/papers/828_Towards_end-to-end_automation_of_AI_research/index.html) — Chris Lu 외, 2026.03 · 인용 90
6. [OpenDiscoveryTrace: Process Traces for Evaluating AI Scientist Workflows](../../docs/papers/10134_OpenDiscoveryTrace_Process_Traces_for_Evaluating_AI_Scientis/index.html) — Aayam Bansal 외, 2026 · 인용 2,072
7. [The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search](../../docs/papers/794_The_AI_Scientist-v2_Workshop-Level_Automated_Scientific_Disc/index.html) — Yutaro Yamada 외, 2025.04 · 인용 476
8. [Democratizing AI scientists using ToolUniverse](../../docs/papers/268_Democratizing_AI_scientists_using_ToolUniverse/index.html) — Shanghua Gao 외, 2025.09 · 인용 297
9. [NeuriCo: Towards reliable AI scientists](../../docs/papers/10098_NeuriCo_Towards_reliable_AI_scientists/index.html) — Haokun Liu 외, 2026 · 인용 144

---

## S12 · 자율 과학 발견 시스템

*제2부 · 자율 AI 과학 발견* · **Autonomous Scientific Discovery Systems** · *서브카테고리*

`46편` `2023–2026` `가속` `2025+ 39편`

> [!abstract] 화면에 띄울 한 줄
> 폐루프 발견 시스템이 늘어난 만큼 과학적 추론 규범을 지키지 못한다는 증거도 쌓였다.

**46편. 가설 생성, 데이터 분석, 문헌 검색을 하나의 월드 모델로 묶는 시스템이 늘었다. 한편 이 시스템들이 과학적으로 추론하지 않는다는 체계적 증거도 같은 시기에 나왔다.**

대표 사례는 Kosmos다. 구조화된 world model로 data analysis agent와 literature search agent가 정보를 공유하고, 200개 이상의 agent rollout에서 평균 42,000줄의 코드와 1,500편의 논문을 처리해 79.4% 정확도로 과학 보고서를 생성한다. Biomni는 150개 전문 도구, 105개 소프트웨어 패키지, 59개 데이터베이스를 하나의 행동 공간으로 묶어 사전 정의된 템플릿 없이 생의학 과제를 수행한다. AI-Newton은 사전 지식 없이 물리 법칙을 재발견하는 시도로 key_developments에 올랐고, Earth-Agent, BehaveAgent, LabOS 같은 도메인별 변형도 대표 도구로 등장했다.[2][6][10]

2026년에는 이 시스템을 어떻게 지을지에 대한 프레임이 갈린다. Embodied Science와 PLAD는 발견을 물리 세계와의 폐루프 상호작용으로 다시 정의했고, Autonomous Agents for Scientific Discovery는 과학자, 언어, 코드, 물리 장비를 조율하는 에이전트로 전 생애주기를 자동화하는 패러다임을 제시했다. Toward a Fully Autonomous, AI-Native Particle Accelerator는 AI 보조에서 완전 자율 운영까지 3단계 로드맵을 낸다. Machine-checked refutation은 도파민 신용 할당의 널리 쓰인 수렴 정리 재서술이 거짓임을 Lean 4로 기계 검증하고 Kairos를 제안해, 에이전트가 검증기와 결합했을 때의 가능성을 보여 준다.[5][7][8]

그러나 가장 무거운 증거는 반대편에 있다. AI scientists produce results without reasoning scientifically는 25,000개 이상의 agent 실행을 분석해, 성능과 행동의 주된 결정자는 base model이며 증거 무시가 68%, 신념 수정 부재가 26%에 달하고 수렴적 다중 증거도 부족하다고 보고했다. 좋은 결과를 내도 과정은 과학의 규범을 따르지 않는다는 뜻이다. AI Scientists Fail Without Strong Implementation Capability는 벤치마크 증거와 28편의 AI Scientist 생성 논문 평가로, 병목이 아이디어 생성이 아니라 실험 검증을 위한 구현 능력이라고 주장한다.[1][9]

자율 실험실로 넘어가면 병목은 모델 밖에 있다. Talking to instruments는 SDL 확장을 가로막는 핵심이 알고리즘이나 로봇이 아니라 이기종 장비를 orchestration하는 소프트웨어 통합 계층(device-integration layer)임을 지적하고, 표준화 지형과 procurement scorecard를 제안한다. Safe-SDL은 AI 기반 SDL의 Syntax-to-Safety Gap을 식별하고 ODD, CBF, Transactional Safety Protocol(CRUTD)을 결합한 안전 프레임워크를 내놓았다. 한편 ChatBCI는 완전 자율 대신 인간 전문가와 AI의 협업을 택했다. 자율성의 한계는 모델이 아니라 통합과 안전 인프라가 정한다.[3][4]

국내 관점의 결론은 간극을 같이 보라는 것이다. 폐루프 시연만 보고 자율 발견 플랫폼에 투자하면 추론 규범 위반을 놓친다. 반대로 반증만 보고 보류하면 물리 실험실과 결합한 성과의 기회를 놓친다. 증거 수용과 신념 수정 같은 추론 규범을 점검하는 평가와, 인간 검증을 의무화하는 연구윤리 조항을 도입 요건으로 함께 두는 것이 현실적이다.

> [!tip] 정리
> 이 칸의 핵심은 자율성의 크기가 아니라 검증의 위치다. 에이전트가 낸 결과물의 신뢰는 모델 성능이 아니라 기계 검증과 인간 검증의 배치에서 나온다.

**대표 도구·시스템** — CRESt · k-agents · Kosmos · AI-Newton · LabOS · AutoBio · Biomni · Earth-Agent · BehaveAgent · EmbodiedAct · AIGS/BABY-AIGS

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [AI Scientists Fail Without Strong Implementation Capability](../../docs/papers/081_Ai_scientists_fail_without_strong_implementation_capability/index.html) — Min Zhu 외, 2025 · 인용 2,819
2. [AI-Newton: A concept-driven physical law discovery system without prior physical knowledge](../../docs/papers/085_Ai-newton_A_concept-driven_physical_law_discovery_system_wit/index.html) — You-Le Fang 외, 2025
3. [Talking to instruments: device-integration standards for self-driving laboratories](../../docs/papers/11480_Talking_to_instruments_device-integration_standards_for_self/index.html) — Willi Gottstein 외, 2026.10
4. [Safe-SDL:Establishing Safety Boundaries and Control Mechanisms for AI-Driven Self-Driving Laboratories](../../docs/papers/11481_Safe-SDLEstablishing_Safety_Boundaries_and_Control_Mechanism/index.html) — Zihan Zhang 외, 2026.02
5. [Autonomous Agents for Scientific Discovery: Orchestrating Scientists, Language, Code, and Physics](../../docs/papers/137_Autonomous_Agents_for_Scientific_Discovery_Orchestrating_Sci/index.html) — Lianhao Zhou 외, 2025.10 · 인용 12,647
6. [Earth-Agent: Unlocking the Full Landscape of Earth Observation with Agents](../../docs/papers/298_Earth-Agent_Unlocking_the_Full_Landscape_of_Earth_Observatio/index.html) — Peilin Feng 외, 2025.09
7. [Embodied Science: Closing the Discovery Loop with Agentic Embodied AI](../../docs/papers/310_Embodied_Science_Closing_the_Discovery_Loop_with_Agentic_Emb/index.html) — Xiang Zhuang 외, 2026.03
8. [Toward a Fully Autonomous, AI-Native Particle Accelerator](../../docs/papers/816_Toward_a_Fully_Autonomous_AI-Native_Particle_Accelerator/index.html) — Chris Tennant, 2026.02 · 인용 154
9. [AI scientists produce results without reasoning scientifically](../../docs/papers/9108_ai_scientists_produce_results_without_reasoning_scienti/index.html) — Martiño Ríos-García 외, 2026 · 인용 342
10. [Kosmos: An AI Scientist for Autonomous Discovery](../../docs/papers/9098_kosmos_an_ai_scientist_for_autonomous_discovery/index.html) — Ludovico Mitchener 외, 2025 · 인용 131
11. [From AI for Science to Agentic Science: A Survey on Autonomous Scientific Discovery](../../docs/papers/352_From_AI_for_Science_to_Agentic_Science_A_Survey_on_Autonomou/index.html) — Jiaqi Wei 외, 2025.10 · 인용 5
12. [The fifth era of science: Artificial scientific intelligence](../../docs/papers/1093_The_fifth_era_of_science_Artificial_scientific_intelligence/index.html) — N. Miolane, 2025 · 인용 4
13. [RSI for Science: A Verifier-First Framework for AI Scientists](../../docs/papers/10354_RSI_for_Science_A_Verifier-First_Framework_for_AI_Scientists/index.html) — David Scott Lewis 외, 2026

---

## S13 · 에이전틱 신약 발굴

*제2부 · 자율 AI 과학 발견* · **Agentic Drug Discovery Workflows** · *서브카테고리*

`36편` `2024–2026` `가속` `2025+ 32편`

> [!abstract] 화면에 띄울 한 줄
> 신약 에이전트는 습식 검증까지 닿았고, 평가는 증거 부족을 인정하는 능력으로 넘어갔다.

**36편. 에이전트가 문헌 검색에서 분자 설계, 실험 제안까지 다루게 됐고 일부는 실험실 검증까지 완료했다. 동시에 증거가 부족할 때 멈추는 능력이 약하다는 진단도 나왔다.**

2025년은 파이프라인의 해였다. TxAgent가 211개 생의학 도구를 통합해 치료 추론을 수행했고, PharmAgents는 타겟 발굴에서 전임상 평가까지 설명 가능한 가상 제약사를 구현했다. DrugPilot은 Parameterized Memory Pool로 이질적 약물 데이터를 표준화하고 Fe-Fo 메커니즘으로 추론 오류를 감시한다. LIDDIA, CLADD, SciToolAgent는 분자 생성·선별, RAG 협업, 지식 그래프 기반 다중 도구 통합을 각각 맡았고 Tippy는 DMTA 사이클을 Safety Guardrail 아래 다섯 에이전트로 쪼갰다. 주요 구성 요소는 이미 갖춰졌다.[4][5][6]

2026년의 전환은 폐루프 검증이다. Robin은 문헌검색 에이전트 Crow, Falcon과 데이터분석 에이전트 Finch를 결합해 가설 생성, 실험 제안, 데이터 해석, 가설 갱신을 자동화하고 dAMD 치료 후보 ripasudil을 발굴해 실험적으로 검증했다. Co-Scientist는 test-time compute scaling과 tournament 기반 진화로 가설을 만들고 약물 재창출, 신규 표적, 항생제 내성 기전에서 실험 검증을 거쳤다. 또 Agentic Systems for Sample-Efficient Drug Formulation Design은 proposer-reviewer 두 에이전트와 자동화 실험실로 SEDDS 제형을 Bayesian optimization 대비 4배 적은 실험으로 동등하게 설계했다.[1]

한편 설계 철학이 바뀌고 있다. TRIAGE는 타겟 발굴을 가설 생성이 아니라 가설 반증으로 재정의하여, 생성 에이전트가 제안한 타겟을 두 적대적 에이전트가 근거 검색과 in silico perturbation 분석으로 반박한다. 좋은 후보를 더 많이 만드는 대신 나쁜 후보를 더 빨리 걸러 내는 방향이다. 이는 생성 모델의 그럴듯함이 검증의 대체물이 될 수 없다는 현장의 판단과 맞닿아 있다.[3]

감사 신호도 같은 해에 나왔다. AMR-Bench-mini는 Klebsiella pneumoniae에 국한된 924개 과제로, frontier LLM 에이전트가 항생제 내성 기전을 추론할 때 증거 충분성을 실제로 판단하는지 아니면 그럴듯한 기전을 패턴 매칭하는지를 검증했다. GPT-5.4, Gemini 3.1 Pro, Claude Opus 4.7 세 모델 모두 abstention 범주에서 약점을 보였다는 것이 핵심이다. 에이전트가 모른다고 말하지 못하면 폐루프의 자동화는 오류의 자동 증폭이 된다.[2]

국내 기관에는 세 가지 함의가 있다. 에이전트 구성 요소는 공개되어 있어 파이프라인 구축 자체는 차별점이 아니다. 차별점은 Robin처럼 습식 검증을 빠르게 붙일 수 있는 실험 파트너십이다. 마지막으로, 도입 평가에 기권 능력과 반증 능력을 포함시켜야 한다. 후보 개수가 아니라 걸러 낸 후보의 질로 에이전트를 평가해야 한다.

> [!tip] 정리
> 신약 에이전트의 병목은 생성이 아니라 반증이다. 실험으로 닫힌 루프와 모른다고 말하는 능력을 함께 갖춘 시스템만 도입 대상이 된다.

**대표 도구·시스템** — TxAgent · PharmAgents · DrugPilot · LIDDIA · CLADD · SciToolAgent · Robin (Crow/Falcon/Finch) · TRIAGE · BioMiner · MolQuest · Tippy

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Agentic Systems for Sample-Efficient Drug Formulation Design](../../docs/papers/9213_Agentic_Systems_for_Sample-Efficient_Drug_Formulation_Design/index.html) — Michael Craig 외, 2026 · 인용 5,395
2. [AMR-Bench-mini: A Diagnostic Benchmark for Agentic Mechanistic AMR Reasoning under Evidence Insufficiency](../../docs/papers/9239_AMR-Bench-mini_A_Diagnostic_Benchmark_for_Agentic_Mechanisti/index.html) — Ali Ihsan Nergiz 외, 2026 · 인용 2,475
3. [TRIAGE: An AI Scientist for Adversarial Target Falsification](../../docs/papers/10638_TRIAGE_An_AI_Scientist_for_Adversarial_Target_Falsification/index.html) — Jiawei Xing, 2026 · 인용 119
4. [Drugpilot: Llm-based parameterized reasoning agent for drug discovery](../../docs/papers/292_Drugpilot_Llm-based_parameterized_reasoning_agent_for_drug_d/index.html) — Kun Li 외, 2025 · 인용 40
5. [LIDDIA: Language-based Intelligent Drug Discovery Agent](../../docs/papers/490_LIDDIA_Language-based_Intelligent_Drug_Discovery_Agent/index.html) — Reza Averly 외, 2025 · 인용 6
6. [PharmAgents: Building a Virtual Pharma with Large Language Model Agents](../../docs/papers/616_PharmAgents_Building_a_Virtual_Pharma_with_Large_Language_Mo/index.html) — Bowen Gao 외, 2025 · 인용 2

---

## S14 · 자율 실험실·공동 과학자

*제2부 · 자율 AI 과학 발견* · **AI Co-Scientist Research Acceleration** · *서브카테고리*

`35편` `2021–2026` `가속` `2025+ 30편`

> [!abstract] 화면에 띄울 한 줄
> 자율주행 실험실이 소재 합성까지 폐루프를 닫았고, 가속 효과를 재는 법이 정리되기 시작했다.

**35편. 이 칸은 자율주행 실험실(SDL)과 공동 과학자가 실제 장비를 돌려 소재·화학 발견의 루프를 닫는 사례를 모았다. 시연이 늘자 가속 효과를 어떻게 잴 것인가가 쟁점이 됐다.**

2023년 A-Lab이 57건 가운데 36건의 무기 합성을 자율 수행한 것이 출발점이다. 이후 신규성 논란과 Author Correction이 이어지며 자율 발견 주장에 대한 검증 규범이 생겼다. 시연은 성공했지만 주장을 어떻게 확인하는지가 논점으로 남은 것이다. 2025년 이후는 이 문제를 안고 진행된다. Gemini Co-Scientist는 세 개 영역에서 시험관 내 검증을 거쳤다고 정리됐고, Polybot과 AMASE는 실험과 이론을 닫힌 루프로 연결하려 했다.[3]

Polybot은 중요도 기반 베이지안 최적화로 7차원 처리 공간을 탐색해 전자 고분자 박막의 4500 S/cm 이상의 고전도성과 저결함을 동시에 달성했다. Adaptive ai decision interface는 AI 조언자와 인간 협업 인터페이스를 얹어 MIECP의 성능을 64회 자동실험으로 150% 높였다. 2026년 Agentic LLM Reasoning in a Self-Driving Laboratory는 A-Lab GPSS에 abductive와 inductive reasoning을 결합해 공기에 민감한 리튬 할라이드 스피넬 이온 전도체를 자율 발견했다. 물리 장비와 LLM 추론이 처음으로 한 시스템에서 확인된 사례다.[1][6][8]

접근성도 바뀌고 있다. RoboChem-Flex는 약 5,000달러의 3D 프린팅 하드웨어와 Python 기반 베이지안 최적화로 반응 최적화를 자동화한다. Flow-driven data intensification은 dynamic flow experiment로 과도 상태 데이터를 정상 상태에 매핑해 무기 재료 합성의 데이터 처리량을 높인다. Toward self-driving laboratory 2.0은 interoperable, collaborative, generalizable, orchestrated, safe, creative의 여섯 특성으로 차세대 SDL을 정의했고, Born-Qualified는 제조성·비용·내구성 제약을 발견 초기부터 반영하는 패러다임을 제안했다.[2][6][7][8]

그러나 비판 축도 뚜렷하다. Benchmarking self-driving labs는 SDL이 탐색을 얼마나 가속하는지 acceleration factor와 enhancement factor의 통계적 특성을 정리하면서, 지금까지의 가속 주장이 일관된 지표 위에 서 있지 않았음을 드러낸다. Data integrity in materials science in the era of AI는 전문가조차 AI 생성 현미경 이미지를 실제 데이터와 구별하지 못한다고 경고한다. Compressing the Validation Bottleneck은 물리 실험의 라운드 수와 비용이 진짜 병목이라고 지적한다.[4][5][6][8]

국내 관점에서 소재·화학 연구기관은 장비 확보보다 평가 체계에 먼저 투자해야 한다. 저비용 SDL이 가능해진 만큼 다수 기관이 유사한 시연을 내놓을 것이고, 차별은 가속 계수를 공통 지표로 보고하고 독립 재현을 받는 데서 생긴다. 데이터 무결성 점검 절차를 도입 단계에서부터 내장하는 것도 필수다.

> [!tip] 정리
> 자율 실험실은 이제 만들 수 있다. 이 칸의 다음 경쟁은 가속을 얼마나 정직하게 측정하고 신규성을 얼마나 엄격하게 검증하느냐다.

**대표 도구·시스템** — A-Lab / A-Lab GPSS · AMASE · Polybot · Gemini Co-Scientist · RoboChem-Flex · NIMO + IvoryOS · CARTOGRAPH · AutoMat · CICERO

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Adaptive ai decision interface for autonomous electronic material discovery](../../docs/papers/048_Adaptive_ai_decision_interface_for_autonomous_electronic_mat/index.html) — Yahao Dai 외, 2025 · 인용 22
2. [Toward self-driving laboratory 2.0 for chemistry and materials discovery](../../docs/papers/10912_toward_self-driving_laboratory_20_for_chemistry_and_ma/index.html) — Heeseung Lee 외, 2026 · 인용 14
3. [Author Correction: An autonomous laboratory for the accelerated synthesis of inorganic materials](../../docs/papers/10931_Author_Correction_An_autonomous_laboratory_for_the_accelerat/index.html) — Nathan J. Szymanski 외, 2026.02 · 인용 5
4. [Benchmarking self-driving labs](../../docs/papers/10935_Benchmarking_self-driving_labs/index.html) — Adedire D. Adesiji 외, 2026 · 인용 11
5. [Data integrity in materials science in the era of AI: balancing accelerated discovery with responsible science and innovation](../../docs/papers/252_Data_integrity_in_materials_science_in_the_era_of_AI_balanci/index.html) — Nik Reeves-McLaren 외, 2026 · 인용 11
6. [Agentic LLM Reasoning in a Self-Driving Laboratory for Air-Sensitive Lithium Halide Spinel Conductors](../../docs/papers/3011_Agentic_LLM_Reasoning_in_a_Self-Driving_Laboratory_for_Air-S/index.html) — Yuxing Fei 외, 2026.04 · 인용 5
7. [Born-Qualified: An Autonomous Framework for Deploying Advanced Energy and Electronic Materials](../../docs/papers/3047_Born-Qualified_An_Autonomous_Framework_for_Deploying_Advance/index.html) — Steven R. Spurgeon 외, 2026.05 · 인용 184
8. [Compressing the Validation Bottleneck: An Agentic Self-Driving Lab for Scientific Discover](../../docs/papers/9421_Compressing_the_Validation_Bottleneck_An_Agentic_Self-Drivin/index.html) — Kyunghoon Hur 외, 2026 · 인용 36
9. [A flexible and affordable self-driving laboratory for automated reaction optimization](../../docs/papers/2989_A_flexible_and_affordable_self-driving_laboratory_for_automa/index.html) — Simone Pilon 외, 2026.04 · 인용 13
10. [Accelerating Scientific Research with Gemini in the Real-World](../../docs/papers/10911_accelerating_scientific_research_with_gemini_in_the_re/index.html) — Samuel Schmidgall 외, 2026.08

---

## S15 · 단백질 공학 에이전트

*제2부 · 자율 AI 과학 발견* · **LLM-Driven Protein Engineering Agents** · *서브카테고리*

`34편` `2021–2026` `가속` `2025+ 27편`

> [!abstract] 화면에 띄울 한 줄
> 단백질 에이전트는 도구 호출에서 강화학습 후학습으로 진화했고 벤치마크는 한계를 재고 있다.

**34편. 이 칸에서는 LLM 에이전트가 단백질 설계 도구를 호출하는 단계를 넘어 정책 최적화로 도구 사용을 학습하는 단계로 이동 중이다. 동시에 새 벤치마크가 한계를 구체적으로 재고 있다.**

2023년 SAMPLE이 자율 플랫폼으로 GH1의 열안정성을 12도 이상 높였고, 2024년 CRISPR-GPT가 유전자 편집 실험 설계를 자동화했다. 2025년에는 Sparks가 훈련 분포 안의 패턴 인식을 넘는 완전 자동화 발견 사이클을 수행해 단백질 과학의 이전에 알려지지 않은 두 가지 현상을 발견했다고 보고했다. PRIME는 65개의 검증된 도구를 동적으로 통합해 213개의 다단계 작업에서 기존 AI 에이전트를 능가했고, FROGENT는 표적 식별에서 역합성 계획까지 신약 개발 전 과정을 하나로 묶었다.[8]

2026년의 전환은 후학습이다. AgentPLM은 ESMFold, FoldX, AutoDock Vina 호출을 자기회귀 생성 안에 끼워 넣는 Reasoning-Augmented Decoding과 Contrastive Agent Policy Optimisation으로 생성 도중 구조·열역학적 제약 위반을 감지하고 교정한다. GOAgent는 GRPO로 multi-turn tool-calling을 학습해 GO annotation 품질을 높였고, State-Aware Policy Optimization은 stateful 시뮬레이션 백엔드를 고려한 GRPO로 3B 규모 모델이 24개 baseline을 능가하게 했다. Agent Rosetta는 Rosetta와 결합해 non-canonical residue 설계에서 전문가 수준 성능을 보였다.[6][7]

탐색 효율을 다루는 접근도 나왔다. CIDER는 저예산 단백질 공학을 top-tail discovery 문제로 재정의하고 conformal top-tail calibration과 information-directed acquisition을 결합한다. PDAgent는 THINK-PLAN-ACT-OBSERVE-REFLECT 폐루프로 서열을 반복 최적화하고, EffieDes는 Potts model로 인코딩한 fitness landscape를 solver로 최적화해 자기회귀 샘플링의 look-ahead 부족을 푼다. Artificial은 self-driving lab의 워크플로우와 기기를 통합하는 오케스트레이션 시스템을 제시했고 Latent-Y는 실험실 검증된 나노바디를 56배 가속으로 제공했다고 정리됐다.[4][5]

그러나 측정 도구가 낙관을 눌러 준다. SMDD-Bench는 멀티턴, 장기 호라이즌의 실제 소분자 신약 설계 과제에서 7개 최신 LLM을 평가했는데, 최고 성능 모델 GPT5.4도 과제의 40.2%만 해결했다. MolOpt-Eval은 hit-to-lead 최적화를 Structural Perception, Strategy Discovery, Strategy Execution 세 단계로 분해해 실패가 reasoning chain의 어디에서 일어나는지를 진단한다. TadA-Bench는 31라운드의 TadA directed evolution 데이터로, 이전 라운드 정보만 가지고 이후 라운드 변이체를 예측하는 future-round discovery를 요구한다.[1][2][3]

국내 기관에 중요한 것은 도구 연결의 상품화다. 이미 공개된 도구를 에이전트로 묶는 일은 어렵지 않다. 차별은 두 곳에서 생긴다. 하나는 TadA-Bench처럼 다라운드 실험 이력을 보유해 에이전트를 시간 순서대로 평가할 수 있는 데이터, 다른 하나는 실패 단계를 분해해 보는 진단 벤치마크 설계 역량이다.[3]

> [!tip] 정리
> 단백질 에이전트의 성능 주장은 이제 시연이 아니라 진단형 벤치마크로 검증된다. 라운드 단위 습식 데이터를 가진 곳이 신뢰할 만한 평가를 만든다.

**대표 도구·시스템** — SAMPLE · CRISPR-GPT · ProtAgents · PRIME · Sparks · Agent Rosetta · AgentPLM · STRIDE · Latent-Y · MolOpt-Eval · TadA-Bench · CIDER

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [MolOpt-Eval: Can Frontier LLMs Perform Structure-Based Hit-to-Lead Optimization?](../../docs/papers/10057_MolOpt-Eval_Can_Frontier_LLMs_Perform_Structure-Based_Hit-to/index.html) — Chengzhu Li 외, 2026
2. [SMDD-Bench: Can LLMs Solve Real-World Small Molecule Drug Design Tasks?](../../docs/papers/10458_SMDD-Bench_Can_LLMs_Solve_Real-World_Small_Molecule_Drug_Des/index.html) — Kevin Han 외, 2026
3. [TadA-Bench: A Million-Variant Benchmark for Future-Round Discovery Toward Agentic Protein Engineering](../../docs/papers/10537_TadA-Bench_A_Million-Variant_Benchmark_for_Future-Round_Disc/index.html) — Jin Gao 외, 2026 · 인용 7
4. [Latent-Y: A Lab-Validated Autonomous Agent for De Novo Antibody Design](../../docs/papers/3150_Latent-Y_A_Lab-Validated_Autonomous_Agent_for_De_Novo_Antibo/index.html) — Latent Labs Team 외, 2026.03
5. [CIDER: Conformal Information-Directed Agents for Low-Budget Protein Engineering](../../docs/papers/9400_CIDER_Conformal_Information-Directed_Agents_for_Low-Budget_P/index.html) — Rishabh Bhattacharya, 2026 · 인용 6,121
6. [AgentPLM: Agentic Protein Language Models with Reasoning-Augmented Decoding for Protein Sequence Design](../../docs/papers/9214_AgentPLM_Agentic_Protein_Language_Models_with_Reasoning-Augm/index.html) — Sahil Rahman 외, 2026 · 인용 1,186
7. [GOAgent: Tool-Orchestrating Language Agents for Protein Function Annotation](../../docs/papers/9749_GOAgent_Tool-Orchestrating_Language_Agents_for_Protein_Funct/index.html) — Manvitha Ponnapati 외, 2026 · 인용 518
8. [Sparks: Multi-Agent Artificial Intelligence Model Discovers Protein Design Principles](../../docs/papers/764_Sparks_Multi-Agent_Artificial_Intelligence_Model_Discovers_P/index.html) — Alireza Ghafarollahi 외, 2025 · 인용 9

---

## S16 · 검증 가능 보상 RL

*제3부 · 형식 수학 정리 증명* · **Verifiable RL for Reasoning** · *서브카테고리*

`47편` `2023–2026` `가속` `2025+ 46편`

<sub>형식 수학 정리 증명 고유 배정 330편(중복 포함 883편 · 웹 인덱스 기준) · 서브카테고리 13개 · 본 파트 5개로 52% 커버</sub>

> [!quote] 파트 도입
> 검증기가 있는 도메인은 RL로 빠르게 풀린다. 이제 병목은 증명이 아니라 진술·벤치마크·검증의 신뢰다.

> [!abstract] 화면에 띄울 한 줄
> 정답을 검사할 수 있는 도메인에서 RL이 추론을 만든다. 보상 자체를 해킹하는 문제가 따라왔다.

**47편 중 46편이 2025년 이후다. 이 칸의 질문은 모델이 얼마나 똑똑한가가 아니라, 정답을 기계가 검사할 수 있으면 학습이 어디까지 자동화되는가이다.**

2025년 DeepSeek-R1은 인간이 주석한 추론 궤적 없이 순수 강화학습만으로 LLM의 추론 능력을 끌어낼 수 있음을 보였다. 학습 중 모델은 자기 검증, 재검토, 전략 전환 같은 고급 패턴을 스스로 만들어 냈다. 이 논문의 의미는 성능 수치가 아니라 감독 비용의 구조 변화다. 검증기만 있으면 라벨러가 필요 없다는 전제가 이 칸의 출발점이다.[1]

그 위에서 보상 설계가 정교해졌다. RISE는 검증 가능한 보상으로 문제 풀이와 자기검증을 동시에 온라인 학습시켜 표면적 자기반성을 줄이려 했고, ReTool은 RL로 코드 인터프리터 호출 시점을 학습시켜 수학 올림피아드에서 o1-preview를 27.9% 앞섰다. RM-R1은 보상 모델 자체에 추론을 넣어 해석 가능성과 성능을 함께 올렸다. 보상은 이제 스칼라 하나가 아니라 설계 대상이다.[3]

2026년에는 이진 보상의 정보 부족이 공격 대상이 됐다. SD-ZERO는 한 모델이 Generator와 Reviser를 겸해 이진 보상을 토큰 수준 자기 감독으로 바꾸고, DistIL은 실행 흔적과 도구 출력 같은 풍부한 피드백을 분포형 DAgger로 쓴다. Rubric-Grounded RL은 문서 기반 루브릭의 부분점수 보상을 GRPO로 최적화한다. 한 비트로 학습하던 방식의 한계를 모두가 인정한 셈이다.

동시에 감사가 붙었다. BENCHJACK은 에이전트 벤치마크가 reward hacking에 구조적으로 취약하다는 점을 8가지 결함 유형으로 정리하고 10개 주요 벤치마크를 자동 탐지·패치 방식으로 감사했다. VeriScale은 적대적 구현으로 테스트 스위트를 확장해 VERINAPLUS와 VERINALITE를 만들었고, 기존 벤치마크가 가리고 있던 명세·코드 생성 취약점을 드러냈다. 보상이 곧 평가이므로 보상이 뚫리면 학습과 평가가 같이 무너진다.[2][4]

국내 관점에서 RL 알고리즘 자체는 이미 공개 자산이라 따라잡기의 대상이 아니다. 격차는 검증기가 존재하는 자기 도메인을 찾아 보상으로 연결하는 능력, 그리고 그 보상이 뚫리지 않는지 감사하는 능력에서 난다. SEVerA처럼 호출마다 형식 계약을 거는 방식은 산업 현장의 안전 요구와도 맞닿아 있다.

> [!tip] 정리
> 검증 가능 보상 RL은 공식이 공개된 단계에 들어섰다. 남은 일은 보상의 출처를 감사하는 것이며, 이는 S20의 문제와 같은 뿌리다.

**대표 도구·시스템** — DeepSeek-R1 · Critique-GRPO · ReTool · RM-R1 · PAG · SD-ZERO · BENCHJACK · VeRA

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning](../../docs/papers/265_DeepSeek-R1_incentivizes_reasoning_in_LLMs_through_reinforce/index.html) — DeepSeek-AI 외, 2025 · 인용 1,046
2. [VeriScale: Adversarial Test-Suite Scaling for Verifiable Code Generation](../../docs/papers/10677_VeriScale_Adversarial_Test-Suite_Scaling_for_Verifiable_Code/index.html) — Yifan Bai 외, 2026 · 인용 30
3. [RM-R1: Reward Modeling as Reasoning](../../docs/papers/683_RM-R1_Reward_Modeling_as_Reasoning/index.html) — Xiusi Chen 외, 2025 · 인용 2
4. [Do Androids Dream of Breaking the Game? Systematically Auditing AI Agent Benchmarks with BenchJack](../../docs/papers/10951_Do_Androids_Dream_of_Breaking_the_Game_Systematically_Auditi/index.html) — Hao Wang 외, 2026.05
5. [Critique-GRPO: Advancing LLM Reasoning with Natural Language and Numerical Feedback](../../docs/papers/243_Critique-GRPO_Advancing_LLM_Reasoning_with_Natural_Language/index.html) — Xiaoying Zhang 외, 2025
6. [Self-Distillation Zero: Self-Revision Turns Binary Rewards into Dense Supervision](../../docs/papers/10409_Self-Distillation_Zero_Self-Revision_Turns_Binary_Rewards_in/index.html) — Yinghui He 외, 2026

---

## S17 · LLM 형식 정리 증명

*제3부 · 형식 수학 정리 증명* · **Formal Theorem Proving with LLMs** · *서브카테고리*

`36편` `2020–2026` `가속` `2025+ 28편`

> [!abstract] 화면에 띄울 한 줄
> 증명기는 miniF2F를 거의 포화시켰고, 같은 해에 그 점수의 의미를 묻는 감사가 나왔다.

**36편 중 28편이 2025년 이후다. 증명기의 성능은 공개 벤치마크 상단에 붙었고, 이 칸의 쟁점은 얼마나 푸느냐에서 무엇을 푼 것이냐로 옮겨갔다.**

2020년 GPT-f가 Metamath set.mm에 증명을 기여한 뒤 miniF2F와 Draft-Sketch-Prove, 2024년 DeepSeek-Prover의 합성 Lean 증명 데이터로 흐름이 이어졌다. 2026년 BFS-Prover-V2는 학습 시점에는 multi-turn off-policy RL을, 추론 시점에는 planner 기반 multi-agent tree search를 결합해 miniF2F 95.08%, ProofNet 41.4%를 보고했다. 학습과 추론 양쪽에서 스케일링을 동시에 건 설계다.[1][4]

에이전트 방식은 학습 비용을 우회한다. Numina-Lean-Agent는 범용 코딩 에이전트에 Numina-Lean-MCP 도구를 붙여 별도 학습 없이 base model만 갈아 끼워 성능을 올린다. 반면 Awakening the Sleeping Agent는 반대 사례를 보인다. 180만 건 형식 수학 SFT로 특화한 GOEDEL-PROVER-V2의 도구 호출 능력이 BFCL 89.4%에서 거의 0으로 무너졌고, Lean 에이전트 트레이스 100개로 복구됐다. 특화의 대가가 숫자로 나왔다.[2][5]

검증기 신호를 어떻게 쓰느냐도 바뀌었다. VERITAS는 구문·타입·목표 진행·완료 신호를 합격/불합격 한 비트로 뭉개지 않고 Best-of-N과 critic 유도 MCTS 전 과정에 되먹인다. Peano Player는 tactic 수준 증명을 제약 MDP로 정식화해 whole-proof RLVR보다 풀이율을 크게 올렸다. DAPS는 의존 그래프로 최근 추가되거나 드문 lemma의 premise selection을 개선한다. AXLE은 Lean 4 도구를 멀티테넌트 클라우드로 제공해 대규모 요청을 받는다.[3][8]

도메인도 넓어졌다. CombiBench는 조합수학 Lean 4 문제 100개와 빈칸 채우기 평가를, OptProver는 올림피아드 증명기를 학부 최적화로 이전시켰고, miniF2F-Dafny는 SMT 자동화와 LLM 안내가 상호보완적임을 보였다. TorchLean은 신경망을 Lean 4 안에서 실행 가능한 수학적 객체로 정의한다. 증명기가 수학 밖의 검증 문제로 번지는 방향이다.[1][6]

그러나 ProofGate는 miniF2F와 PutnamBench의 높은 pass rate가 proof faithfulness, statement alignment, problem vacuity라는 세 현상을 섞은 수치라고 짚고 단일 지표로 분리 감사했다. 국내에서 증명기 점수를 도입 근거로 삼는다면 이 감사 항목을 먼저 요구해야 한다. 진술이 틀렸거나 공허하면 높은 점수는 아무것도 보증하지 않는다.[1][7]

> [!tip] 정리
> 증명 생성은 상품화 단계에 접어들었다. 가치는 증명을 만드는 모델보다, 그 증명이 올바른 진술을 향하는지 따지는 감사 체계에 있다.

**대표 도구·시스템** — GPT-f · miniF2F · DSP · DeepSeek-Prover · Lean-STaR · POETRY · BFS-Prover-V2 · VERITAS · Euclean · CombiBench

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [miniF2F-Dafny: LLM-Guided Mathematical Theorem Proving via Auto-Active Verification](../../docs/papers/10033_miniF2F-Dafny_LLM-Guided_Mathematical_Theorem_Proving_via_Au/index.html) — Mantas Baksys 외, 2026 · 인용 4
2. [Numina-Lean-Agent: An Open and General Agentic Reasoning System for Formal Mathematics](../../docs/papers/10115_Numina-Lean-Agent_An_Open_and_General_Agentic_Reasoning_Syst/index.html) — Junqi Liu 외, 2026
3. [Peano Player: Interactive Theorem Proving as a Constrained MDP](../../docs/papers/10167_Peano_Player_Interactive_Theorem_Proving_as_a_Constrained_MD/index.html) — Matthew Retchin 외, 2026
4. [Deepseek-prover: Advancing theorem proving in llms through large-scale synthetic data](../../docs/papers/264_Deepseek-prover_Advancing_theorem_proving_in_llms_through_la/index.html) — Huajian Xin 외, 2024
5. [Awakening the Sleeping Agent: Lean-Specific Agentic Data Reactivates General Tool Use in Goedel Prover](../../docs/papers/9286_Awakening_the_Sleeping_Agent_Lean-Specific_Agentic_Data_Reac/index.html) — Jui-Hui Chung 외, 2026
6. [OptProver: Bridging Olympiad and Optimization through Continual Training in Formal Theorem Proving](../../docs/papers/10144_OptProver_Bridging_Olympiad_and_Optimization_through_Continu/index.html) — Chenyi Li 외, 2026
7. [ProofGate: A Reproducible Audit of Faithfulness, Alignment, and Vacuity in State-of-the-Art Lean Theorem Provers](../../docs/papers/10257_ProofGate_A_Reproducible_Audit_of_Faithfulness_Alignment_and/index.html) — Edison Yang 외, 2026
8. [VERITAS: Verifier-Guided Proof Search for Zero-Shot Formal Theorem Proving](../../docs/papers/10678_VERITAS_Verifier-Guided_Proof_Search_for_Zero-Shot_Formal_Th/index.html) — Manish Acharya 외, 2026
9. [FIPO-Prover: Formalization-Oriented Informal Proof Optimization for Efficient Formal Theorem Proving](../../docs/papers/9650_FIPO-Prover_Formalization-Oriented_Informal_Proof_Optimizati/index.html) — Jingkun Ma 외, 2026

---

## S18 · 정리 자동 형식화

*제3부 · 형식 수학 정리 증명* · **Autoformalization of Theorems** · *서브카테고리*

`35편` `2023–2026` `가속` `2025+ 32편`

> [!abstract] 화면에 띄울 한 줄
> 자연어를 Lean으로 옮기는 일이 가속되는 만큼, 옮겨진 진술의 충실도가 새 병목이 됐다.

**35편 중 32편이 2025년 이후다. 자동 형식화는 처리량의 문제에서 충실도의 문제로 넘어왔다. 컴파일에 성공해도 옳은 진술이라는 보장이 없다는 것이 이 칸의 핵심 교훈이다.**

자동 형식화는 데이터 합성에서 시작했다. 2023~2024년 LEGO-Prover는 스킬 라이브러리를 키웠고 MUSTARD는 증명 데이터를 합성했다. 2026년에는 단계별 모듈화가 진행됐다. DSR는 명제를 분해하고 operator tree로 구조화한 뒤 오류를 국소화해 복구하는 파이프라인이고, FormalRx는 의미 실패를 28개 범주로 분류하는 SCI 분류체계를 제시했다. 실패 모드를 이름 붙여 다루기 시작한 것이다.[1][7]

규모 면에서는 논문 단위 변환이 등장했다. MerLean은 양자계산 이론 논문 3편의 명제 114개에서 Lean 선언 2,050개를 생성하며 논문 전체 자동 형식화에 성공했다. Formalizing Numerical Analysis는 mathlib에 거의 없던 상미분방정식 수치해법 교재를 코딩 에이전트로 전면 형식화했다. VeriBench는 Python에서 Lean까지 end-to-end 검증을 평가하고, Quokka는 LLM이 만든 루프 불변식을 검증기가 직접 평가해 프로그램 검증을 가속한다.[2][6]

그러나 이 칸의 가장 큰 사건은 감사 결과다. Ground False는 ProofNet 367개 항목을 전수 수작업 감사해 56%가 원문에 충실하지 않고, 그중 절반 이상은 수학적으로 거짓임을 밝혔다. 정답으로 믿어 온 벤치마크 ground truth가 사실상 무검증이었다는 뜻이다. 같은 계열로 Auditable Harness는 AI가 만든 Lean 증명이 컴파일되고 원 진술을 보존하는지 재현 가능하게 점검하고, Formalizing Numerical Analysis도 kernel acceptance만으로는 의미 정확성을 알 수 없다고 못 박는다.[2][4]

방어 수단도 나왔다. Lean Disprove는 반례 탐색을 여섯 단계 순환으로 돌리되 Lean 커널이 인증한 경우에만 REFUTED로 보고하고 나머지는 WITNESS-UNCERTIFIED와 INCONCLUSIVE로 구분한다. Graffiti3Loop는 기계 생성 그래프 추측을 Lean 4로 번역해 Comparator로 검증하는 자율 루프이며 GRAFFITI3BENCH-330을 함께 내놨다. Risk-Controlled Lean-as-Judge는 Lean 신호가 부분적이라는 점을 반영해 선택적 위험 인증서를 붙인다.[3][5][8]

국내 연구기관이 이 칸에서 취할 것은 두 가지다. 형식화 파이프라인을 쓰되 번역 충실도 점검 단계를 필수 공정으로 넣을 것, 그리고 외부 벤치마크를 쓰기 전에 샘플 감사를 먼저 수행할 것이다. 오류율이 높은 정답지 위에서 얻은 점수는 비교 근거가 되지 못한다.

> [!tip] 정리
> 형식화는 자동화됐고 검증은 아직 수작업이다. 진술 충실도를 재는 도구를 가진 쪽이 다음 단계의 기준을 쥔다.

**대표 도구·시스템** — LEGO-Prover · MUSTARD · FormalRx · FormalRx-CC · VeriBench · Quokka · CertJudge · Signal-Coverage Matrix

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Lego-prover: Neural theorem proving with growing libraries](../../docs/papers/486_Lego-prover_Neural_theorem_proving_with_growing_libraries/index.html) — Huajian Xin 외, 2023 · 인용 80
2. [Formalizing Numerical Analysis: An Agent Pipeline and Quality Audit Beyond Kernel Acceptance](../../docs/papers/9671_Formalizing_Numerical_Analysis_An_Agent_Pipeline_and_Quality/index.html) — Theodore Meek 외, 2026 · 인용 6
3. [Graffiti3Loop: Generating and Resolving Formal Machine-Generated Graph Conjectures in a Loop](../../docs/papers/9754_Graffiti3Loop_Generating_and_Resolving_Formal_Machine-Genera/index.html) — William Hu 외, 2026 · 인용 208
4. [Ground False: Dissecting Errors in Formal Mathematics Benchmarks](../../docs/papers/9759_Ground_False_Dissecting_Errors_in_Formal_Mathematics_Benchma/index.html) — One An 외, 2026 · 인용 159
5. [Lean Disprove: Certified Counterexample Search for AI-Assisted Formal Mathematics](../../docs/papers/9886_Lean_Disprove_Certified_Counterexample_Search_for_AI-Assiste/index.html) — Jan Ondras 외, 2026 · 인용 8
6. [VeriBench: An End-to-End Formal Verification Benchmark for AI Coding Agents in Lean 4](../../docs/papers/10676_VeriBench_An_End-to-End_Formal_Verification_Benchmark_for_AI/index.html) — Brando Miranda 외, 2026
7. [FormalRx: Rectify and eXamine Semantic Failures in Autoformalization](../../docs/papers/9675_FormalRx_Rectify_and_eXamine_Semantic_Failures_in_Autoformal/index.html) — Haocheng Wang 외, 2026
8. [Risk-Controlled Lean-as-Judge for Natural-Language Mathematical Reasoning](../../docs/papers/10347_Risk-Controlled_Lean-as-Judge_for_Natural-Language_Mathemati/index.html) — Pauline Bourigault 외, 2026
9. [The Signal-Coverage Matrix: Stratifying Type and Semantic Errors in Statement Autoformalization](../../docs/papers/10578_The_Signal-Coverage_Matrix_Stratifying_Type_and_Semantic_Err/index.html) — Chengxiao Dai 외, 2026

---

## S19 · AI 공동 수학자

*제3부 · 형식 수학 정리 증명* · **Formal Mathematical Theorem Proving** · *서브카테고리*

<sub>타임라인 분석 명칭: Formal Mathematical Theorem Proving / AI Co-Mathematician</sub>

`26편` `2026–2026` `부상` `2025+ 26편`

> [!abstract] 화면에 띄울 한 줄
> 2026 에이전트가 미해결 문제를 풀고 연구 수준 이론을 Lean으로 형식화하기 시작했다.

**26편이 전부 2026년 논문이다. 올림피아드 풀이가 아니라 연구 수준 문제를 대상으로 하는 신생 칸이고, 상태는 EMERGING이다.**

대표 사례는 수학 연구 워크플로 전체를 에이전트화한 시스템들이다. AI Co-Mathematician은 프로젝트 코디네이터가 전문 에이전트를 조율해 아이디어 발상, 문헌 검색, 계산 탐색, 정리 증명, 이론 구축을 지원하며 FrontierMath Tier 4에서 48%로 SOTA를 달성했다. QED는 연구 수준 문제 진술만 받아 분해·증명·검증 에이전트가 사람 개입 없이 완전한 증명을 만드는 오픈소스 시스템이다. 단일 질의 증명의 실패 양상을 역할 분리로 넘으려는 설계다.[1]

형식화 쪽에서는 사람 한 명이 쓰는 시간이 줄었다. Vlasov–Maxwell–Landau 평형 형식화는 Gemini DeepThink가 증명을 만들고 Claude Code가 Lean 4로 번역하고 Aristotle이 lemma를 자동 증명하는 파이프라인으로, 수학자 한 명이 10일간 코드를 한 줄도 쓰지 않고 마쳤다. MerLean은 양자계산 논문을 자동 형식화하고, Formalizing Scarf, Brouwer, and Nash in Lean은 조합론 증명에서 Brouwer 부동점과 Nash 균형 존재성을 Lean으로 도출했다.[3][6]

발견의 사례도 쌓였다. AlphaProof Nexus는 Erdős 문제 9개와 OEIS 추측 44개를 증명했다고 보고되며, Gemini Deep Think 사례 연구는 이론 전산·경제·최적화·물리에서 미해결 문제를 푼 협력 기법을 추출했다. Ramanujan 1/π 17개 급수의 통합 증명, Counting Cycles with AI, Potts 모델 Lyapunov 퍼텐셜은 인간 전략과 AI 계산을 섞은 하이브리드 증명이다. AI 단독이 아니라 사람이 방향을 쥔 구조가 다수다.[2]

한계 신호도 같은 칸에 있다. HorizonMath는 생성하기와 검증하기 사이의 격차로 발견을 측정하려 하고, Stellar Colosseum은 타깃형 falsification과 전역 검증을 파이프라인에 기본값으로 넣었다. Self-Supervised Theorem Discovery는 공리만으로 정리 라이브러리를 쌓는다. 생성이 빨라질수록 검증이 병목이라는 인식이 설계에 이미 반영돼 있다.[7]

국내 관점에서 이 칸은 수학 단독 주제가 아니다. 양자계산, 통계적 학습 이론, 플라스마 방정식, 게임이론이 모두 형식화 대상이 됐다. 이론 중심 분야의 연구 조직이라면 Lean 숙련 인력과 에이전트 파이프라인을 소수라도 갖춰 두는 편이 낫다. 증명을 쓰는 비용은 내려가고 검증 책임의 비용은 오른다.

> [!tip] 정리
> AI 공동 수학자는 시연 단계를 지나 첫 성과 단계에 들어섰다. 성과의 무게는 생성한 증명이 아니라 검증된 증명의 수로 가려진다.

**대표 도구·시스템** — AlphaProof Nexus · QED · ReasFlow · MerLean · Stellar Colosseum · HorizonMath · Gemini Deep Think

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [AI Co-Mathematician: Accelerating Mathematicians with Agentic AI](../../docs/papers/3014_AI_Co-Mathematician_Accelerating_Mathematicians_with_Agentic/index.html) — Daniel Zheng 외, 2026.05 · 인용 633
2. [Counting Cycles with AI](../../docs/papers/9449_Counting_Cycles_with_AI/index.html) — Jiashun Jin 외, 2026 · 인용 450
3. [Formalizing Scarf, Brouwer, and Nash in Lean](../../docs/papers/9672_Formalizing_Scarf_Brouwer_and_Nash_in_Lean/index.html) — Lyu Yuwei 외, 2026 · 인용 159
4. [Semi-Autonomous Formalization of the Vlasov–Maxwell–Landau Equilibrium](../../docs/papers/10415_Semi-Autonomous_Formalization_of_the_VlasovMaxwellLandau_Equ/index.html) — Vasily Ilin, 2026 · 인용 3,164
5. [Human-AI Hybrid Mathematical Discovery Workflow: Unifying Ramanujan's 17 Series for 1/π](../../docs/papers/9796_Human-AI_Hybrid_Mathematical_Discovery_Workflow_Unifying_Ram/index.html) — Michael Shalyt 외, 2026 · 인용 46
6. [MerLean: An Agentic Framework for Autoformalization in Quantum Computation](../../docs/papers/532_MerLean_An_Agentic_Framework_for_Autoformalization_in_Quantu/index.html) — Yuanjie Ren 외, 2026.02 · 인용 9
7. [Self-Supervised Theorem Discovery in a Formal Axiomatic System](../../docs/papers/10414_Self-Supervised_Theorem_Discovery_in_a_Formal_Axiomatic_Syst/index.html) — Kazuki Ota 외, 2026

---

## S20 · 증명 검증의 아첨

*제3부 · 형식 수학 정리 증명* · **Sycophancy in Proof Verification** · *서브카테고리*

<sub>타임라인 분석 명칭: Sycophancy & Trust in Proof Verification</sub>

`26편` `2023–2026` `가속` `2025+ 24편`

> [!abstract] 화면에 띄울 한 줄
> LLM 채점자와 자기검증이 틀린 증명을 통과시킨다는 정량 증거가 2026년에 쏟아졌다.

**26편 중 24편이 2025년 이후다. 생성 능력이 올라갈수록 검증이 병목이 된다. 이 칸은 AI가 틀린 증명에 동조하는 현상과 평가 체계의 결함을 수치로 다룬다.**

아첨의 출발점은 거짓 입력이다. 2025년 SPOT은 LLM이 출판된 과학 논문의 오류를 21% 미만만 회수한다는 점을 보였고, BrokenMath는 틀린 정리 진술에 모델이 동조하는 정도를 정량화했다. 2026년 QEDBench는 한 걸음 더 나가 judge 모델 7개와 solver 모델 5개의 이중 평가 매트릭스에 인간 전문가 1,000시간 이상을 투입해, 다수의 프론티어 judge가 결함 있는 증명에도 점수를 부풀린다는 정렬 격차를 드러냈다.[5][7]

자기검증은 구조적으로 믿을 수 없다. VOUCH는 자기 반사실적 예측을 스스로 검증하는 프로토콜이 self-coherent한 추론자라면 정답 여부와 무관하게 항상 통과한다는 점을 이론적으로 증명하고 GSM8K, MATH-algebra, SVAMP에서 확인했다. 해법은 두 에이전트가 서로의 측면에 커밋하는 dual-side counterfactual contract다. Online Learnability of Chain-of-Thought Verifiers도 오류를 놓치는 것과 옳은 추론을 거부하는 것 사이의 비대칭 trade-off를 이론으로 정식화했다.[2]

대응은 비관적 검증으로 수렴한다. Pessimistic Verification은 병렬 verifier 중 하나라도 오류를 찾으면 기각하고 증명을 세밀히 분해하는 progressive 방식을 더했다. OC-PVerify는 검증을 obligation coverage 문제로 재정의해 first-error-wins를 적용하며, Step-Level Elaboration은 각 deduction step을 구성적으로 풀어 context poisoning과 과잉 회의를 줄인다. 하나의 단호한 반증만 있으면 기각한다는 비대칭 기준이 공통점이다.[6]

평가 체계 쪽도 흔들린다. Toward Unified Evaluation of Mathematical AI는 여섯 개 검증 패러다임이 Open Proof Corpus에서 서로 불일치함을 보였고, PROOFRANK는 정답 여부 말고 간결성과 계산 부담 같은 증명 품질 5가지 축을 도입했다. No LLM Aced Yu Tsumura's 554th Problem은 해답이 학습 데이터에 있는데도 31개 최신 LLM이 안정적으로 풀지 못했다. What are the Right Symmetries for Formal Theorem Proving?은 의미가 같은 진술 변형에 증명기가 민감함을 지적한다.[3][4]

가장 불편한 결과는 Model Collapse Despite Ground-Truth Verification이다. Lean 같은 정확한 검증기가 남은 산출물을 정확히 판정해도 생성·필터링 과정에서 목표 분포의 모드가 통째로 사라질 수 있다. 검증기가 있다고 안전하다는 가정을 깬다. 국내 도입 기관은 채점자 모델 하나에 의존하지 말고 비관적 다중 검증과 형식 검증, 인간 샘플 감사를 층으로 쌓아야 한다.[1]

> [!tip] 정리
> 검증기가 있어서 풀린 칸이 검증기의 허점 때문에 다시 흔들린다. 벤치마크 정기 감사와 오류 수정 체계를 학계 공동으로 운영하는 일이 정책 과제다.

**대표 도구·시스템** — BrokenMath · QEDBench · SPOT · PROOFRANK · MathArena · Recurrence · P4Bench

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Model Collapse Despite Ground-Truth Verification](../../docs/papers/10048_Model_Collapse_Despite_Ground-Truth_Verification/index.html) — Shuo Li Liu, 2026
2. [Online Learnability of Chain-of-Thought Verifiers: Soundness and Completeness Trade-offs](../../docs/papers/10129_Online_Learnability_of_Chain-of-Thought_Verifiers_Soundness/index.html) — Maria Florina Balcan 외, 2026
3. [Toward Unified Evaluation of Mathematical AI: A Survey and Framework](../../docs/papers/10606_Toward_Unified_Evaluation_of_Mathematical_AI_A_Survey_and_Fr/index.html) — Nishitha A, 2026
4. [What are the Right Symmetries for Formal Theorem Proving?](../../docs/papers/10696_What_are_the_Right_Symmetries_for_Formal_Theorem_Proving/index.html) — Krzysztof Olejniczak 외, 2026
5. [QEDBench: Quantifying the Alignment Gap in Automated Evaluation of University-Level Mathematical Proofs](../../docs/papers/10280_QEDBench_Quantifying_the_Alignment_Gap_in_Automated_Evaluati/index.html) — Santiago Gonzalez 외, 2026
6. [Step-Level Elaboration Improves Natural Language Verification of Research-Level Mathematical Proofs](../../docs/papers/10500_Step-Level_Elaboration_Improves_Natural_Language_Verificatio/index.html) — Yifeng Sun 외, 2026
7. [BrokenMath: A Benchmark for Sycophancy in Theorem Proving with LLMs](../../docs/papers/9359_BrokenMath_A_Benchmark_for_Sycophancy_in_Theorem_Proving_wit/index.html) — Ivo Petrov 외, 2026
8. [Pessimistic Verification for Open-Ended Math Questions](../../docs/papers/10175_Pessimistic_Verification_for_Open-Ended_Math_Questions/index.html) — Yanxing Huang 외, 2026

---

## S21 · 다단계 연쇄 추론

*제4부 · LLM 추론·에이전트 벤치마크* · **Multi-Hop Chain-of-Thought Reasoning** · *서브카테고리*

`54편` `2015–2026` `가속` `2025+ 23편`

<sub>LLM 추론·에이전트 벤치마크 고유 배정 284편(중복 포함 1,088편 · 웹 인덱스 기준) · 서브카테고리 10개 · 본 파트 5개로 65% 커버</sub>

> [!quote] 파트 도입
> 무엇을 못하는지 재는 일이 산업이 됐다. 에이전트를 늘려도 나아지지 않는다는 반증까지 같은 해에 쌓였다.

> [!abstract] 화면에 띄울 한 줄
> 추론은 검색과 결합한 강화학습으로 옮겨갔고, 그 경계를 재는 진단이 함께 붙었다.

**54편 중 23편이 2025년 이후다. 이 칸의 질문은 'LLM이 단계를 밟아 답에 이르는가'에서 'RL로 검색과 추론을 묶어 학습시키면 어디까지 가고, 그 한계는 어떻게 재는가'로 이동했다.**

배경부터 짚는다. 2022년 ReAct가 추론 흔적과 행동을 하나의 흐름으로 묶었고, 2023년에는 Self-Refine과 SelfCheck의 자기개선 물결이 일었다. 같은 해에 대규모 언어 모델은 스스로 오류를 고치지 못한다는 반박도 나왔다. 이 칸은 처음부터 가능성과 반증이 나란히 간 분야이고, 그 긴장이 2025년 이후의 연구 방향을 정했다.[3]

2025년의 중심은 검색을 추론 안으로 끌어들이는 강화학습이다. Search-R1은 추론 중 검색 엔진을 자동으로 호출하도록 학습시켜 기존 RAG 대비 최대 41%의 성능 향상을 보고했다. ReSearch는 감독 데이터 없이 검색 질의, 사고, 검색 결과를 엮은 체인을 만들어 다중 홉 QA에서 8.9~22.4% 향상을 얻었다. WebAgent-R1은 이를 실제 웹의 다중턴 의사결정으로 확장했다.[2][4][6]

2026년에는 학습 신호의 해상도가 문제가 됐다. GRAIL은 GRPO 기반 RLVR에서 시퀀스 전체에 균일하게 주던 advantage를 gradient-activation saliency로 토큰별 재가중해, 최종 답에 실제로 기여한 토큰에 더 강한 신호를 준다. 별도의 process reward model 없이 세밀한 정렬을 얻겠다는 시도다. Weak Critics Make Strong Learners는 약한 모델을 정답 제공자가 아니라 비판자로 써서 강한 모델을 감독한다.[1][5]

동시에 감사가 붙는다. RBF++, DRE-Bench, InvariantBench는 추론의 경계와 질문 표현이 바뀌어도 답이 유지되는지를 따지고, Hidden-CoT 탐지는 드러난 사고 과정이 실제 계산과 일치하는지를 묻는다. 2026년 멀티모달 LLM-as-a-Judge 연구는 시각 근거와 서술이 충돌할 때 judge가 서술 쪽으로 쏠려 틀린 답을 높게 준다는 편향을 규명했다. 점수를 매기는 쪽도 감사 대상이라는 뜻이다.[7][8]

국내 관점에서 이 칸의 도구는 이미 열려 있다. RL 레시피를 따라 하는 것은 어렵지 않으나, 한국어나 국내 규제·산업 문서를 대상으로 한 추론 진단이 없으면 공개 벤치마크 점수가 현장 성능을 보증하지 못한다. 도입 판단에 쓸 수 있는 평가셋을 직접 갖는 것이 모델을 직접 학습시키는 것보다 먼저다.

> [!tip] 정리
> 추론 성능은 학습 레시피로 오르지만, 그 성능이 어디서 깨지는지는 평가자가 정한다. 경계 진단과 judge 감사 역량이 이 칸의 실질 경쟁력이다.

**대표 도구·시스템** — ReAct · Self-Refine · SelfCheck · Search-R1 · ReSearch · WebDancer · WebAgent-R1 · RBF++ · InvariantBench · GRAIL

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Weak Critics Make Strong Learners: On-Policy Critique Distillation for Scalable Oversight](../../docs/papers/10690_Weak_Critics_Make_Strong_Learners_On-Policy_Critique_Distill/index.html) — Can Jin 외, 2026
2. [Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement Learning](../../docs/papers/740_Search-R1_Training_LLMs_to_Reason_and_Leverage_Search_Engine/index.html) — Bowen Jin 외, 2025 · 인용 12
3. [Self-Refine: Iterative Refinement with Self-Feedback](../../docs/papers/746_Self-Refine_Iterative_Refinement_with_Self-Feedback/index.html) — Aman Madaan 외, 2023 · 인용 354
4. [WebAgent-R1: Training Web Agents via End-to-End Multi-Turn Reinforcement Learning](../../docs/papers/871_WebAgent-R1_Training_Web_Agents_via_End-to-End_Multi-Turn_Re/index.html) — Zhepei Wei 외, 2025 · 인용 2
5. [GRAIL: Gradient-Reweighted Advantages for Reinforcement Learning with Verifiable Rewards](../../docs/papers/9755_GRAIL_Gradient-Reweighted_Advantages_for_Reinforcement_Learn/index.html) — Tej Deep Pala 외, 2026 · 인용 56
6. [ReSearch: Learning to Reason with Search for LLMs via Reinforcement Learning](../../docs/papers/667_ReSearch_Learning_to_Reason_with_Search_for_LLMs_via_Reinfor/index.html) — Mingyang Chen 외, 2025 · 인용 10
7. [RBF++: Quantifying and optimizing reasoning boundaries across measurable and unmeasurable capabilities for chain-of-thought reasoning](../../docs/papers/652_Rbf_Quantifying_and_optimizing_reasoning_boundaries_across_m/index.html) — Qiguang Chen 외, 2025
8. [Mitigating Perceptual Judgment Bias in Multimodal LLM-as-a-Judge for Mathematical and Scientific Reasoning Evaluation](../../docs/papers/10038_Mitigating_Perceptual_Judgment_Bias_in_Multimodal_LLM-as-a-J/index.html) — Seojeong Park 외, 2026

---

## S22 · 에이전트 기억·계획

*제4부 · LLM 추론·에이전트 벤치마크* · **Agent Skill Memory Planning** · *서브카테고리*

`39편` `2023–2026` `가속` `2025+ 31편`

> [!abstract] 화면에 띄울 한 줄
> 에이전트의 병목이 '한 번 푸는 능력'에서 '길게 일관되게 수행하는 능력'으로 옮겨갔다.

**39편 중 31편이 2025년 이후로, 이 칸은 사실상 최근 연구로 채워져 있다. 에이전트가 길게 일하려면 기억하고, 재사용하고, 계획을 지켜야 한다. 이제는 그것을 재는 벤치마크와 통계가 함께 나온다.**

출발점은 2023년의 구조 설계다. Tree-Planner, HiAgent, Agent S는 계층적 폐루프 계획과 작업 기억 관리를 에이전트의 기본 틀로 세웠다. 당시의 질문은 계획을 세울 수 있는가였다. 2025년 이후에는 질문이 바뀐다. 계획을 세운 뒤 수백 단계 동안 그 계획과 자기 이전 결정에 일관될 수 있는가가 핵심이다.[3]

기억과 기술의 재사용이 첫 번째 축이다. 2025년 A-MEM은 Zettelkasten 방법론을 따라 새 기억이 추가될 때 맥락 연결을 자동 생성하고 기존 기억을 함께 진화시킨다. 2026년 SkillX는 에이전트가 각자 경험을 학습하는 비효율을 지적하며, 강한 backbone인 GLM-4.6에서 planning, functional, atomic의 3단계 skill knowledge base를 자동 구축해 다른 에이전트가 꽂아 쓰게 한다. 경험을 개인 자산에서 공유 자산으로 바꾸는 시도다.[5]

두 번째 축이 장기 일관성 벤치마크다. 2026년 YC-Bench는 POMDP 기반으로 1년, 수백 턴 동안 스타트업을 운영하게 한다. 직원 관리, 계약 선택, 현금 흐름이 얽히고 클라이언트는 불충실하며 급여 비용은 늘어난다. 한 문제를 맞히는 능력으로는 통과할 수 없는 환경이다. 2025년 Text2world는 자연어 설명에서 PDDL 기호 세계 모델을 생성하게 해, 현재 LLM의 세계 모델링이 아직 제한적임을 실행 기반 지표로 드러냈다.[1][2]

세 번째 축은 측정 자체의 통계적 엄밀성이다. 2026년 Deadline-Valid Replay는 greedy, self-consistency 같은 추론 정책의 비교를 시한 조건의 순차 검정 문제로 바꿔, 리더보드의 서술적 차이가 통계적으로 유의한지 따진다. 입자 필터로 추론 궤적을 Normal, Insight, Backtrack 모드로 온라인 추적하는 연구도 같은 계열이다. 순위표는 그 자체로 증거가 아니라는 인식이 방법론이 됐다.[4]

국내 관점에서는 에이전트 데모의 성공이 장기 운용의 성공을 뜻하지 않는다는 점을 전제해야 한다. 업무 에이전트를 도입하는 기관은 자기 업무 흐름을 YC-Bench식 장기 환경으로 옮겨 측정하고, 두 정책의 차이는 검정을 거쳐 판단해야 한다. 기억·기술 저장소 설계 역시 모델 선택만큼 비용과 성능을 좌우한다.[1]

> [!tip] 정리
> 에이전트의 가치는 한 번의 시연이 아니라 긴 운용에서 드러난다. 장기 환경 설계와 통계 검정을 갖춘 조직만 도입 효과를 숫자로 말할 수 있다.

**대표 도구·시스템** — Agent S · HiAgent · Tree-Planner · A-MEM · SkillX · Vending-Bench · YC-Bench · Text2World · TEMPO · E-valuator

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [YC-Bench: Benchmarking AI Agents for Long-Term Planning and Consistent Execution](../../docs/papers/3398_YC-Bench_Benchmarking_AI_Agents_for_Long-Term_Planning_and_C/index.html) — Muyu He 외, 2026 · 인용 1,873
2. [Text2world: Benchmarking large language models for symbolic world model generation](../../docs/papers/792_Text2world_Benchmarking_large_language_models_for_symbolic_w/index.html) — Mengkang Hu 외, 2025 · 인용 3
3. [Tree-planner: Efficient close-loop task planning with large language models](../../docs/papers/842_Tree-planner_Efficient_close-loop_task_planning_with_large_l/index.html) — Mengkang Hu 외, 2023
4. [Deadline-Valid Replay: Anytime-Valid Testing for LLM Inference Policies](../../docs/papers/9482_Deadline-Valid_Replay_Anytime-Valid_Testing_for_LLM_Inferenc/index.html) — Rui Gao, 2026 · 인용 74
5. [SkillX: Automatically Constructing Skill Knowledge Bases for Agents](../../docs/papers/10451_SkillX_Automatically_Constructing_Skill_Knowledge_Bases_for/index.html) — Chenxi Wang 외, 2026 · 인용 124
6. [Cocoa: Co-planning and co-execution with AI Agents](../../docs/papers/229_Cocoa_Co-planning_and_co-execution_with_ai_agents/index.html) — K. J. Kevin Feng 외, 2026 · 인용 6
7. [PostTrainBench: Can LLM Agents Automate LLM Post-Training?](../../docs/papers/10220_PostTrainBench_Can_LLM_Agents_Automate_LLM_Post-Training/index.html) — Ben Rank 외, 2026

---

## S23 · 임상 추론 에이전트

*제4부 · LLM 추론·에이전트 벤치마크* · **Clinical Reasoning Agents & Rewards** · *서브카테고리*

`33편` `2023–2026` `가속` `2025+ 30편`

> [!abstract] 화면에 띄울 한 줄
> 임상 추론은 단일 거대 모델에서 역할 분담형 에이전트와 단계별 보상으로 옮겨갔다.

**33편 중 30편이 2025년 이후다. 이 칸에서는 한 모델이 진단하는 그림이 사라지고 있다. 역할을 나눈 에이전트, 단계별 보상, 임상의 개입 지점이 설계의 기본 단위가 됐다.**

2023년의 MedAgents, Agent Hospital, AI Hospital은 의료 협업을 에이전트 사회로 시뮬레이션했다. 2025년 이후의 질문은 이 구조가 실제로 더 낫고 더 안전한지다. 2026년 Salus는 감별진단을 다중 라운드 순차 의사결정으로 정식화한 CompDiag-Bench를 만들고, 진단 추론을 Differential Reasoner, Strategic Controller, Workup Proposer 세 에이전트로 분리해 다중 에이전트 강화학습으로 훈련했다. 어떤 검사를 언제 낼지라는 임상의 판단을 벤치마크에 넣은 것이 요점이다.[1][2][8]

규모에 대한 반론도 같은 해에 나왔다. Small Agent Group은 단일 거대 LLM의 scaling-first 패러다임에 맞서, 소형 LLM 협업 집단이 효과·신뢰성·배포 비용에서 앞설 수 있음을 보였다. HetMedAgent는 generalist LLM, 전문 모델, 임상의를 이질적 다중 에이전트로 묶고 불확실성이 커지면 임상의 개입을 유발한다. 병원 내 배포 비용과 책임 소재를 함께 고려한 설계다.

보상 설계도 바뀌었다. Process Reward Agents는 지식 집약적 추론에서 frozen policy 모델의 추론 흔적을 단계별로 온라인 평가·조정한다. Resp-GRASP는 호흡 신호를 다루는 여섯 단계의 가드레일 RAG 파이프라인으로, 환자별 기준선과 모집단 기준선을 겹쳐 MedGemma-27B가 근거 인용 보고서를 쓰게 한다. 최종 답이 맞았는지만 보던 보상에서 근거 사슬이 타당한지를 보는 보상으로 이동했다.[3]

데이터 쪽 병목은 전자의무기록이다. EHR-ReasonCon은 MIMIC-III 기반 8,048개 entity에 전문가 검수 주석을 붙여 임상 노트와 구조화 표의 불일치를 추론으로 찾게 한다. FHIR-Hopper는 FHIR 번들을 시간순 그래프로 바꾸고 결정론적 탐색 도구로 필요한 세부를 조회한다. PopMedQA는 ICD 코드가 텍스트로 풀릴 때 컨텍스트가 폭발하는 문제를 벤치마크로 만들었다.[4]

그러나 좋은 소식만은 아니다. The Consistency Dilemma는 10개 최신 모델과 491개 개념을 측정해, 생성과 평가에서 같은 개념을 일관되게 적용하는 모델일수록 임상 환경의 실수에 더 취약하다는 역설을 보였다. 일관성이 곧 안전이라는 가정이 깨졌다. 국내 병원이 에이전트를 검토한다면 정확도 외에 이런 실패 모드를 자체 시나리오로 시험해야 한다.

> [!tip] 정리
> 임상 추론의 경쟁은 모델 크기에서 역할 설계, 단계별 검증, 개입 시점으로 옮겨갔다. 일관성이 안전을 보장하지 않으므로 실패 모드 평가가 도입의 전제 조건이다.

**대표 도구·시스템** — MedAgents · Agent Hospital · MedAgentGym · InfiMed-ORBIT · DR Tulu · GLEAN · HetMedAgent · Salus · FHIR-Hopper

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Agent hospital: A simulacrum of hospital with evolvable medical agents](../../docs/papers/058_Agent_hospital_A_simulacrum_of_hospital_with_evolvable_medic/index.html) — Junkai Li 외, 2024
2. [AI Hospital: Benchmarking Large Language Models in a Multi-agent Medical Interaction Simulator](../../docs/papers/078_Ai_hospital_Benchmarking_large_language_models_in_a_multi-ag/index.html) — Zhihao Fan 외, 2024 · 인용 6
3. [Resp-GRASP: Clinically-Grounded Reasoning for Respiratory Signal Interpretation via Guardrailed RAG with Personalized Baselines](../../docs/papers/10328_Resp-GRASP_Clinically-Grounded_Reasoning_for_Respiratory_Sig/index.html) — Excel Widjaja 외, 2026
4. [FHIR-Hopper: A Neuro-Symbolic Agent for Reasoning over EHRs](../../docs/papers/9645_FHIR-Hopper_A_Neuro-Symbolic_Agent_for_Reasoning_over_EHRs/index.html) — Chanwoo Kim 외, 2026 · 인용 104
5. [Reinforcement Learning for Tool-Calling Agents in Fast Healthcare Interoperability Resources (FHIR)](../../docs/papers/10319_Reinforcement_Learning_for_Tool-Calling_Agents_in_Fast_Healt/index.html) — Marius Knorr 외, 2026 · 인용 420
6. [Process Reward Agents for Steering Knowledge-Intensive Reasoning](../../docs/papers/10251_Process_Reward_Agents_for_Steering_Knowledge-Intensive_Reaso/index.html) — Jiwoong Sohn 외, 2026 · 인용 11
7. [MedAgentGym: A Scalable Agentic Training Environment for Code-Centric Reasoning in Biomedical Data Science](../../docs/papers/528_MedAgentGym_A_Scalable_Agentic_Training_Environment_for_Code/index.html) — Ran Xu 외, 2025.06
8. [Salus: Strategic Diagnostic Testing for Complex Diagnosis via Multi-Agent Reinforcement Learning](../../docs/papers/10364_Salus_Strategic_Diagnostic_Testing_for_Complex_Diagnosis_via/index.html) — Shuohao Gao 외, 2026

---

## S24 · 표·데이터 추론

*제4부 · LLM 추론·에이전트 벤치마크* · **Table Reasoning Intelligence Benchmarks** · *서브카테고리*

`30편` `2023–2026` `가속` `2025+ 17편`

> [!abstract] 화면에 띄울 한 줄
> 표 이해는 데이터 과학 에이전트 평가로 확장됐고, 다중 에이전트의 가치는 도전받는다.

**30편 중 17편이 2025년 이후다. 표를 읽는 능력의 평가가 데이터 과학 업무 전체를 맡기는 에이전트의 평가로 커졌고, 그 과정에서 다중 에이전트 설계의 효용을 의심하는 반증이 나왔다.**

표 추론의 기초 진단은 견고성에서 시작한다. 2025년 ToRR는 10개 데이터셋과 14개 주요 LLM으로 표 이해와 형식 변화에 대한 견고성을 체계적으로 평가했고, 최신 모델도 표 형식이 달라지면 쉽게 무너지는 brittle 행동을 보인다는 결론을 냈다. 같은 해 TableMaster는 구조화 데이터 특성에서 비롯된 네 가지 도전을 식별해 통합 프레임워크로 대응했다. 표는 단순한 입력이 아니라 형식 민감성을 가진 별도의 시험대다.[6]

과제는 표 한 장에서 분석 전 과정으로 번졌다. 2025년 R&D-Agent는 연구자 에이전트가 성능 피드백으로 아이디어를 내고 개발자 에이전트가 오류 피드백으로 코드를 고치는 이중 구조로 데이터 과학 솔루션 개발을 자동화한다. DeepAnalyze-8B는 원시 데이터에서 분석가급 심층 보고서까지 완전 자동화를 내세우며, 8B 파라미터로 독점 LLM 기반 워크플로우 에이전트를 능가했다고 보고한다. 작은 모델이 구조로 큰 모델을 이긴 사례다.[3][5]

평가 쪽은 DiscoveryBench, BLADE, DSBench 같은 데이터 기반 발견 벤치마크 위에 2026년 DDR-Bench가 올라왔다. 주어진 질문에 답하는 대신 구조화 데이터베이스에서 스스로 탐색 목표를 정하고 통찰을 뽑는 investigatory intelligence를 검증 가능하게 측정한다. 도메인 쪽에서는 극한 기상 진단 시스템 HVR-Met, 7,732개 전문가 예보문을 짝지은 AFDBench, 조합 최적화 문제를 QUBO로 옮기는 QuantumQUBO Agent와 QUBOBench가 나왔다.[1][7]

이 칸에서 가장 날카로운 신호는 2026년 1월 Rethinking the Value of Multi-Agent Workflow다. 동일한 base LLM을 쓰는 동질적 다중 에이전트 워크플로우가 KV cache를 공유하는 단일 에이전트의 다중턴 대화로도 같은 성능이 재현되며, 이를 바탕으로 OneFlow가 단일 에이전트용 워크플로우를 자동 설계한다. 대분류 전체의 통찰, 즉 에이전트가 많다고 반드시 낫지 않다는 증거와 정확히 겹친다.[2]

국내 관점에서 데이터 분석 에이전트는 공공·기업 현장에서 가장 먼저 도입될 유형이다. 그런 만큼 ToRR식 형식 변형 시험을 내부 문서·표 서식으로 수행하고, 다중 에이전트 구성은 단일 에이전트 기준선보다 낫다는 것을 보인 뒤에만 채택해야 한다. 복잡한 구조는 비용을 먼저 올린다.

> [!tip] 정리
> 표와 데이터 분석 평가의 교훈은 견고성과 기준선이다. 형식이 바뀌어도 유지되는지, 단일 에이전트보다 실제로 나은지를 먼저 확인하는 조직이 도입 비용을 줄인다.

**대표 도구·시스템** — AutoGen · Data Interpreter · AutoKaggle · DiscoveryBench · BLADE · DSBench · ToRR · TableMaster · DeepAnalyze · OneFlow

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [QuantumQUBO Agent: Automating Quadratic Unconstrained Binary Optimization (QUBO) Formulation Generation from Natural Language](../../docs/papers/10289_QuantumQUBO_Agent_Automating_Quadratic_Unconstrained_Binary/index.html) — Niloy Kumar Mondal 외, 2026 · 인용 8,635
2. [Rethinking the Value of Multi-Agent Workflow: A Strong Single Agent Baseline](../../docs/papers/11008_Rethinking_the_Value_of_Multi-Agent_Workflow_A_Strong_Single/index.html) — Jiawei Xu 외, 2026.01 · 인용 2
3. [R&D-Agent: Automating Data-Driven AI Solution Building Through LLM-Powered Automated Research, Development, and Evolution](../../docs/papers/650_RD-Agent_Automating_Data-Driven_AI_Solution_Building_Through/index.html) — Xu Yang 외, 2025.05 · 인용 1
4. [The mighty torr: A benchmark for table reasoning and robustness](../../docs/papers/802_The_mighty_torr_A_benchmark_for_table_reasoning_and_robustne/index.html) — Shir Ashury-Tahan 외, 2025
5. [DeepAnalyze: Agentic Large Language Models for Autonomous Data Science](../../docs/papers/259_DeepAnalyze_Agentic_Large_Language_Models_for_Autonomous_Dat/index.html) — Shaolei Zhang 외, 2025.10
6. [Tablemaster: A recipe to advance table understanding with language models](../../docs/papers/787_Tablemaster_A_recipe_to_advance_table_understanding_with_lan/index.html) — Lang Cao 외, 2025
7. [HVR-Met: A Hypothesis-Verification-Replanning Agentic System for Extreme Weather Diagnosis](../../docs/papers/9798_HVR-Met_A_Hypothesis-Verification-Replanning_Agentic_System/index.html) — Shuo Tang 외, 2026

---

## S25 · 주장 검증

*제4부 · LLM 추론·에이전트 벤치마크* · **Claim Verification & Misinformation Detection** · *서브카테고리*

`29편` `2021–2026` `안정` `2025+ 10편`

> [!abstract] 화면에 띄울 한 줄
> 주장 검증은 사실 대조에서 반박 증거 검색, 통계적 감사, 지식 삭제 검증으로 확장됐다.

**29편 중 10편이 2025년 이후이며 상태는 안정(STABLE)으로 분류된다. 이 칸은 주장 검증이 사실 대조 문제에서 증거 구조, 통계적 보증, 모델이 잊었는지 확인하는 문제까지 번지는 과정을 보여준다.**

기초는 2021년 MultiVers의 전체 문서 맥락과 약한 감독, 이후 ProgramFC의 프로그램 가이드 추론, FactKG의 지식 그래프 기반 검증이다. 2022년의 한 논문은 현실의 허위정보에는 반박 증거가 없는 경우가 많은데 기존 사실 확인 데이터셋은 모두 이 요건을 만족하지 못하고, 모델이 누출된 증거에 의존함을 실증했다. 이 비판은 지금 이 칸의 문제의식의 뿌리다.

2025년에는 과학과 생의학 주장으로 규모와 시스템이 늘었다. SciClaimHunt는 87,109개 주장과 이를 지지하거나 반박하는 과학 논문 증거로 구성된 대규모 데이터셋이다. CIBER는 RAG를 확장해 지지 증거와 반박 증거를 모두 찾고, 다양한 질문 프로브로 응답 일관성을 평가해 환각을 줄인다. SciClaims는 주장 추출, PubMed 검색, 단일 LLM 검증을 엮어 체계적 문헌고찰과 특허 검증 같은 고위험 용도를 겨냥한다.[2][4]

주장을 어떻게 뽑느냐도 평가 대상이 됐다. Claimify는 장문 LLM 생성물을 팩트체크하기 위해 추출된 주장의 품질을 평가하는 표준 틀을 제안하고 모호성을 다루는 추출 방법을 내놨다. 설명가능성 쪽에서는 CoENLI와 SHAP을 결합해 의료 주장 검증의 추론을 단어 수준으로 들여다보게 한 시스템이 나왔고, OVON 기반 다중 에이전트 오케스트레이션은 구조화 메시지로 환각 완화를 시도했다.

2026년의 전환은 검증을 통계와 삭제 문제로 재정의한 데 있다. jailbreak 탐지기 감사 연구는 임계값을 가설검정으로 보고 permutation test와 Paraphrase-Conformal Calibration으로 유한표본 Type-I 오류를 통제하며 다섯 벤더의 production 분류기를 감사했다. SciUnlearn은 여러 QA 형식으로 표현된 claim을 대상으로, 기존 unlearning 기법이 표면 형식만 억제할 뿐 claim 수준 지식을 제거하지 못함을 보였다.[6]

국내에서는 한국어 과학 주장과 국내 규제 문서에 대한 지지·반박 증거 데이터가 사실상 비어 있다. 영어 데이터셋에서의 성능을 그대로 믿을 근거가 없으므로, 연구 무결성이나 공공 정보 신뢰성에 이 기술을 쓰려면 반박 증거 부족 상황을 포함한 자체 시험셋과 보정 절차를 먼저 갖춰야 한다.

> [!tip] 정리
> 주장 검증의 신뢰는 정확도 점수가 아니라 반박 증거를 찾는 능력, 오류율 통제, 삭제의 실효성에서 나온다. 검증기 자체를 감사하는 일이 이 칸의 새 과제다.

**대표 도구·시스템** — MultiVers · ProgramFC · FactKG · ClaimVer · HiSS · SciClaimHunt · Claimify · CIBER · BioKGBench

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Explainable biomedical claim verification with large language models](../../docs/papers/328_Explainable_biomedical_claim_verification_with_large_languag/index.html) — Siting Liang 외, 2025 · 인용 54
2. [Sciclaimhunt: A large dataset for evidence-based scientific claim verification](../../docs/papers/710_Sciclaimhunt_A_large_dataset_for_evidence-based_scientific_c/index.html) — Sujit Kumar 외, 2025 · 인용 35
3. [LLM-based Corroborating and Refuting Evidence Retrieval for Scientific Claim Verification](../../docs/papers/500_Llm-based_corroborating_and_refuting_evidence_retrieval_for/index.html) — Siyuan Wang 외, 2025
4. [SciClaims: An end-to-end generative system for biomedical claim analysis](../../docs/papers/711_Sciclaims_An_end-to-end_generative_system_for_biomedical_cla/index.html) — Raúl Ortega 외, 2025
5. [Towards effective extraction and evaluation of factual claims](../../docs/papers/827_Towards_effective_extraction_and_evaluation_of_factual_claim/index.html) — Dasha Metropolitansky 외, 2025 · 인용 5
6. [Auditing LLM Jailbreak Detectors as Hypothesis Tests: Permutation P-values and Type-I Error Control via Paraphrase Exchangeability](../../docs/papers/9270_Auditing_LLM_Jailbreak_Detectors_as_Hypothesis_Tests_Permuta/index.html) — Vishal Narender Punjabi, 2026

---

## S26 · 물리 기반 신경 연산자

*제5부 · 물리 기반 신경 시뮬레이션* · **Physics-Informed Neural Operators** · *서브카테고리*

`66편` `2017–2026` `가속` `2025+ 58편`

<sub>물리 기반 신경 시뮬레이션 고유 배정 272편(중복 포함 572편 · 웹 인덱스 기준) · 서브카테고리 9개 · 본 파트 5개로 75% 커버</sub>

> [!quote] 파트 도입
> 신경 시뮬레이터의 경쟁축이 속도에서 보장(guarantee)과 실패 모드 진단으로 옮겨갔다.

> [!abstract] 화면에 띄울 한 줄
> 2026의 질문은 '얼마나 빠른가'가 아니라 'PINN과 연산자가 왜, 어디서 실패하는가'다.

**66편, 그중 58편이 2025년 이후다. 이 칸은 대분류 272편의 24%를 차지하는 최대 서브카테고리이며, 타임라인은 2017년 PINN 정식화에서 2026년까지 이어진다. 상태는 가속 중이지만 가속의 방향이 바뀌었다. 새 구조를 내놓는 일보다 기존 구조가 어디서 깨지는지 밝히는 일이 늘었다.[1]**

2017년 PDE 잔차를 손실에 넣는 PINN, 2018년 연속 깊이 모델 Neural ODE, 이후 DeepONet과 FNO가 이 분야의 뼈대를 만들었다. 2023년에는 FNO 사전학습과 전이학습의 스케일링 법칙이 SciML 파운데이션 모델이라는 구상을 열었다. 이 흐름은 이제 배경이다. 2025년 10월의 비교 리뷰 Architectures, variants, and performance of neural operators는 DeepONet, 적분 커널 연산자, 트랜스포머 기반 연산자를 나란히 놓고 전통 수치해석을 대체할 수 있는지를 따졌고, From Theory to Application은 DeepONet·PCANet·FNO를 입문 수준에서 비교했다. 정리 단계에 들어섰다는 신호다.[1][3][7]

2026년의 가장 뚜렷한 변화는 실패 모드 진단이다. Mitigating Gradient Pathology in PINNs through Aligned Constraint는 PINN 학습을 막는 gradient pathology를 PDE 잔차 손실의 global minimizer manifold라는 기하 구조에서 원인을 찾고, 정렬된 제약으로 해결한다. On the Role of Consistency Between Physics and Data in PINNs는 1D Burgers 방정식으로 데이터와 PDE의 불일치가 도달 가능한 정확도의 하한을 결정하는 consistency barrier를 형식화했고, 고충실도 데이터를 쓰면 이 장벽이 사라짐을 보였다. 모델이 안 되는 이유를 말할 수 있어야 한다는 요구가 논문 주제가 됐다.[1]

구조 쪽에서는 물리 사전지식을 더 강하게 넣는 방향과 생성 모델을 붙이는 방향이 병존한다. cd-PINN은 해가 초기·경계값과 매개변수에 연속적으로 의존한다는 성질을 써서 재훈련 없이 연산자를 학습하고, 제한된 라벨로 DeepONet·FNO 대비 1-3 자릿수 낮은 오차를 보고한다. Neural-HSS는 타원형 PDE Green 함수의 계층적 준분리 구조를 레이어로 옮겼고, Origo는 operator splitting 이론으로 다물리 PDE 파운데이션 모델의 negative transfer를 다룬다. MENO는 신경 연산자에 MeanFlow를 결합해 확산 모델 대비 12배 빠른 추론을 내세운다.[1][2][8]

응용 사례는 오히려 수치해석의 영역을 넓힌다. 2025년 Discovery of Unstable Singularities는 머신러닝과 고정밀 수치해석을 결합해 3D 오일러, 비압축성 다공질 매질, Boussinesq 방정식에서 불안정 특이점을 처음으로 체계적으로 발견했다. 신경망이 솔버를 대체하는 것이 아니라 솔버가 못 닿던 영역을 탐색하는 도구가 된 사례다. Solving Stiff Dark Matter Equations via Jacobian Normalization은 강성 방정식을, Neural Ensemble Kalman Filter는 충격파가 있는 압축성 유동의 데이터 동화를 다룬다. 한편 타임라인은 2026년 LLM 에이전트가 신경 연산자 구조를 자동 설계하는 흐름도 기록한다.[4][5][6]

국내 관점에서 이 칸은 도입 판단의 기준을 바꾼다. 제조·에너지·원자력의 시뮬레이션 부서가 PINN이나 신경 연산자를 검토할 때, 한 번의 정확도 수치로는 부족하다. gradient pathology와 consistency barrier가 보여 주듯 실패는 조건에 따라 달라진다. 고차원·다중스케일에서의 범용 안정성 보장은 여전히 미해결이라는 점도 분명히 해야 한다. 전통 수치해석법과의 비교 벤치마크를 의무화하고, 실패 영역을 문서로 남기는 팀이 신뢰를 얻는다.[1]

> [!tip] 정리
> 속도 경쟁은 끝나지 않았지만 더는 차별점이 아니다. 이 칸의 2026년은 실패의 원인을 설명하고 데이터와 물리의 불일치가 만드는 한계를 수치로 말하는 쪽이 앞선다는 것을 보여 준다.

**대표 도구·시스템** — PINN · DeepONet · FNO · PINO · Neural ODE · Neural-HSS · Origo · SLE-FNO · Neural-POD · Hyperbolic Neural Operator

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Mitigating Gradient Pathology in PINNs through Aligned Constraint](../../docs/papers/10037_Mitigating_Gradient_Pathology_in_PINNs_through_Aligned_Const/index.html) — Yichen Luo 외, 2026
2. [Neural-HSS: Hierarchical Semi-Separable Neural PDE Solver](../../docs/papers/10096_Neural-HSS_Hierarchical_Semi-Separable_Neural_PDE_Solver/index.html) — Pietro Sittoni 외, 2026
3. [Architectures, variants, and performance of neural operators: A comparative review](../../docs/papers/103_Architectures_variants_and_performance_of_neural_operators_A/index.html) — Shengjun Liu 외, 2025.10 · 인용 16
4. [Discovery of Unstable Singularities](../../docs/papers/276_Discovery_of_Unstable_Singularities/index.html) — Yongji Wang 외, 2025.09 · 인용 17
5. [Neural Ensemble Kalman Filter: Data Assimilation for Compressible Flows with Shocks](../../docs/papers/3187_Neural_Ensemble_Kalman_Filter_Data_Assimilation_for_Compress/index.html) — 2026.02 · 인용 1
6. [Solving Stiff Dark Matter Equations via Jacobian Normalization with Physics-Informed Neural Networks](../../docs/papers/3242_Solving_Stiff_Dark_Matter_Equations_via_Jacobian_Normalizati/index.html) — 2026.02 · 인용 458
7. [From Theory to Application: A Practical Introduction to Neural Operators in Scientific Computing](../../docs/papers/364_From_Theory_to_Application_A_Practical_Introduction_to_Neura/index.html) — Prashant K. Jha, 2025.03 · 인용 10
8. [MENO: MeanFlow-Enhanced Neural Operators for Dynamical Systems](../../docs/papers/3165_MENO_MeanFlow-Enhanced_Neural_Operators_for_Dynamical_System/index.html) — 2026.04 · 인용 1,051
9. [Neural Modular Physics for Elastic Simulation](../../docs/papers/10093_Neural_Modular_Physics_for_Elastic_Simulation/index.html) — Yifei Li 외, 2026 · 인용 560
10. [On the Role of Consistency Between Physics and Data in Physics-Informed Neural Networks](../../docs/papers/3195_On_the_Role_of_Consistency_Between_Physics_and_Data_in_Physi/index.html) — 2026.02 · 인용 11

---

## S27 · 동역학계 flow matching

*제5부 · 물리 기반 신경 시뮬레이션* · **Flow Matching for Dynamical Systems** · *서브카테고리*

`46편` `2020–2026` `가속` `2025+ 45편`

> [!abstract] 화면에 띄울 한 줄
> flow matching이 궤적 추론과 PDE 풀이의 표준 생성 골격이 됐고, 한두 단계 추론이 목표가 됐다.

**46편 중 45편이 2025년 이후로, 사실상 2026년에 몰린 칸이다. 타임라인은 2020년 시뮬레이션 기반 추론의 정착에서 시작해 2026년 최적수송 계열 flow matching, 대칭 보존 흐름, 저단계 잠재 생성 솔버로 이어진다. 확산 모델의 느린 샘플링을 어떻게 걷어내는가가 이 칸의 줄거리다.**

가장 직접적인 전환은 추론 단계의 압축이다. MENO는 신경 연산자와 개선된 MeanFlow(i-MF)를 합쳐 동역학계의 다중 스케일 거동을 맞히면서 확산 모델 대비 12배 빠른 추론을 달성했다고 보고한다. 타임라인에는 일단계·소단계 잠재 생성 PDE 솔버도 올라 있고 Latent Generative Solver가 대표 도구로 꼽힌다. 생성 모델의 비용이 확산 시절의 수십 스텝에서 몇 스텝으로 내려오면서, 생성 방식이 수치 솔버의 실시간 대안으로 검토되는 단계에 들어섰다.

둘째 갈래는 기하와 대칭을 흐름에 넣는 작업이다. STFlow는 N-body, 분자동역학, 보행자 궤적을 위해 데이터 종속 prior를 flow matching에 도입했다. SE(3)-Equivariant Flow Matching with Gaussian Process Priors는 관측된 과거 궤적에서 벡터값 가우시안 과정으로 시간 상관과 SE(3) 대칭을 함께 반영한 prior를 만든다. SMART는 메쉬 없이 점군과 시뮬레이션 매개변수만으로 임의 위치의 물리량을 예측하는 공기역학 시뮬레이션을 내놨다. 해석 격자를 만드는 비용을 건너뛴다는 점이 산업적으로 크다.[4][5]

셋째 갈래는 스냅샷에서 궤적을 복원하는 문제다. Multimarginal flow matching with optimal transport potentials는 다중 marginal 궤적 추론을 동적 최적수송에 퍼텐셜 항을 더해 푼다. MMtSBM은 짝지어지지 않은 정적 스냅샷에서 다중 marginal Schrödinger Bridge를 학습하고, PACE는 파괴적 시계열 단일세포 스냅샷에 국소 접선 방향을 반영한 비등방 수송을 쓴다. Two-Parameter Flows는 marginal 분포만으로 물리 시간의 population dynamics를 학습한다. 관측이 파괴적인 생물·물리 실험에서 쓸모가 크다.[1][8]

그러나 생성 모델을 PDE에 붙이는 순간 새 실패 모드가 생긴다. Physics-Informed Distillation of Diffusion Models for PDE-Constrained Generation은 posterior mean에 PDE 제약을 걸 때 Jensen's Gap이 생김을 규명하고 사후 distillation으로 해소한다. Particle-Guided Diffusion Models for PDEs는 PDE 잔차와 관측 제약 guidance를 Sequential Monte Carlo로 묶는다. On the Collapse of Generative Paths는 inference-time steering에서 expert를 조합할 때 중간 밀도가 비정규화되는 Marginal Path Collapse를 진단하고 ACE로 교정한다. 속도 뒤에서 보장의 문제가 따라왔다.[2][3]

국내 연구기관에는 두 가지 시사점이 있다. 첫째, 날씨·유동·분자 궤적처럼 불확실성이 본질인 문제는 점 추정 연산자보다 생성 방식이 자연스럽고, 한두 단계 추론으로 비용 장벽이 낮아졌다. 둘째, 물리 제약을 guidance로 얹는 설계는 편향 원인이 흩어져 있어 검증이 어렵다. 도입 시 제약 위반률과 분포 붕괴를 측정하는 점검표를 별도로 갖춰야 하며, 이는 S26에서 다룬 실패 모드 진단과 같은 요구다.

> [!tip] 정리
> flow matching은 확산의 대체재로 자리 잡았고, 이제 질문은 몇 단계에 끝나는가에서 그 흐름이 물리를 지키는가로 이동했다. 빠른 생성기를 검증 가능한 시뮬레이터로 만드는 일이 남은 과제다.

**대표 도구·시스템** — OTP-FM · WFR-MFM · STFlow · GP-EquiFlow · Recursive Flow Matching · Latent Generative Solver · MENO · TFMPE · FUSE · LieStoNet

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Multimarginal flow matching with optimal transport potentials](../../docs/papers/10073_Multimarginal_flow_matching_with_optimal_transport_potential/index.html) — Raghav Kansal 외, 2026
2. [Particle-Guided Diffusion Models for Partial Differential Equations](../../docs/papers/10158_Particle-Guided_Diffusion_Models_for_Partial_Differential_Eq/index.html) — Andrew Millard 외, 2026
3. [Physics-Informed Distillation of Diffusion Models for PDE-Constrained Generation](../../docs/papers/10186_Physics-Informed_Distillation_of_Diffusion_Models_for_PDE-Co/index.html) — Yi Zhang 외, 2026
4. [SE(3)-Equivariant Flow Matching with Gaussian Process Priors for Geometric Trajectory Prediction](../../docs/papers/10398_SE3-Equivariant_Flow_Matching_with_Gaussian_Process_Priors_f/index.html) — Xuyang Wang 외, 2026
5. [STFlow: Data-Coupled Flow Matching for Geometric Trajectory Simulation](../../docs/papers/10501_STFlow_Data-Coupled_Flow_Matching_for_Geometric_Trajectory_S/index.html) — Kiet Bennema ten Brinke 외, 2026 · 인용 12
6. [LieStoNet: Learning Lie Symmetries from Spatiotemporal Data for Stochastic Dynamical Systems](../../docs/papers/9943_LieStoNet_Learning_Lie_Symmetries_from_Spatiotemporal_Data_f/index.html) — Shida Liu 외, 2026
7. [FUSE: FK-Steered Multi-Modal Flow Matching for Efficient Simulation-Based Posterior Estimation](../../docs/papers/9710_FUSE_FK-Steered_Multi-Modal_Flow_Matching_for_Efficient_Simu/index.html) — Weichen Qin 외, 2026 · 인용 994
8. [Two-Parameter Flows for Learning Population Dynamics of Physical Systems](../../docs/papers/10648_Two-Parameter_Flows_for_Learning_Population_Dynamics_of_Phys/index.html) — Paul Schwerdtner 외, 2026 · 인용 2

---

## S28 · 확산 기반 자료동화

*제5부 · 물리 기반 신경 시뮬레이션* · **Diffusion-Based Data Assimilation** · *서브카테고리*

`33편` `2026–2026` `부상` `2025+ 33편`

> [!abstract] 화면에 띄울 한 줄
> 생성 prior가 희소 센서 복원에서 변분 동화를 대체하기 시작했고, 신뢰도 보증이 따라붙는다.

**33편, 모두 2025년 이후라는 점에서 이 칸은 막 생겨난 분야다. 타임라인은 2026년 하나이고 상태는 EMERGING이다. 핵심 아이디어는 변분 동화의 손으로 짠 사전분포를 학습된 생성 prior로 바꾸는 것이며, 센서가 극단적으로 성긴 문제에서 가장 먼저 효과가 보인다.**

희소성이 이 칸의 기준 지표다. SENDAI는 1.56% 커버리지의 센서 관측만으로 위성 기반 식생지수 NDVI 필드를 재구성한다. 시뮬레이션에서 얻은 저주파 prior와 학습 기반 고주파 불일치 보정을 합친 구조다. Di-BiLPS는 최소 3%의 관측에서 forward와 inverse PDE 문제를 하나의 틀로 푼다. VAE로 압축한 잠재 공간에서 확산 모델과 대조 학습을 쓴다. 관측 대부분이 비어 있어도 상태장을 복원하는 능력이 생성 모델의 장점으로 제시된다.[8][10]

두 번째 흐름은 계산 비용과 해석 가능성이다. PODiff는 픽셀 공간이나 학습된 비선형 잠재 공간 대신 분산 순서가 고정된 POD 계수 공간에서 조건부 확산을 수행해 과학 필드의 확률적 super-resolution을 한다. 어떤 성분이 복원에 기여하는지 읽을 수 있다는 점이 설득력이다. Physically-Guided Data-Space Rectified Flow for Precipitation Nowcasting은 데이터 공간 파라미터화와 Semi-Lagrangian 이류 prior로 off-manifold drift를 막는다. 물리 prior가 생성 경로를 가이드하는 방식이 반복적으로 나타난다.[1][9]

세 번째는 역문제 솔버의 이론 정리다. Plug-and-Play Diffusion Meets ADMM은 기존 PnP diffusion prior 솔버가 기억 없는 P-controller처럼 동작해 steady-state bias를 낳는다고 지적하고, ADMM의 dual variable을 되살려 적분 피드백을 주었다. Resolving Blind Inverse Problems under Dynamic Range Compression은 단조성을 물리적 불변량으로 삼는다. Scalable Bayesian Inference for Nonlinear Conservation Laws는 유한체적법을 가우시안 과정과 결합한 확률적 수치해석으로 순문제·역문제를 다룬다. 생성 모델 바깥에서도 불확실성을 수치해석에 편입하려는 움직임이 같은 시기에 나왔다.[2][4][5]

신뢰성 신호도 함께 등장했다. Principled Confidence Estimation for Deep Computed Tomography는 순차 우도 혼합 틀을 CT 재구성에 적용해 Beer-Lambert 법칙과 Poisson 잡음을 반영한 이론적 coverage 보증을 얻는다. Training-Free Adversarial Robustness in Computational MRI는 사전 학습 없이 MRI 재구성 네트워크에 대한 적대적 공격을 완화한다. Deep Ensemble Graph Neural Networks for Probabilistic Cosmic-Ray Direction은 앙상블과 불확실성 정량화로 정확도와 신뢰성을 동시에 올린다. 생성 prior가 그럴듯한 환각을 만들 수 있는 이상 복원 품질과 신뢰도 보증이 한 쌍으로 요구되기 시작했다.[3][6][7]

국내 관점에서는 위성·기상·해양처럼 관측망이 성긴 영역이 바로 적용처다. 다만 이 칸의 논문 다수는 영상 복원과 역문제 모음에 가깝고, 운용 예보 시스템에 연결된 사례는 아직 적다. 도입 순서는 명확하다. 먼저 희소 센서 복원처럼 정답을 검증할 수 있는 과제에서 쓰고, 신뢰구간과 강건성 점검을 갖춘 뒤 운용 파이프라인에 넣는다. 비교 기준은 기존 변분 동화이며, 비교 없이 도입하는 것은 위험하다.

> [!tip] 정리
> 확산 기반 자료동화는 아직 초기이며 성능 주장이 앞서 있다. 이 칸이 성숙하는 조건은 복원 능력이 아니라 복원 결과에 대한 보증을 함께 제공하느냐에 달려 있다.

**대표 도구·시스템** — DAISI · GenDA · SENDAI · LoPhyDA · PODiff · PIDDM · DC-PnPDP · ANTiC · AnyBand-Diff · WIND

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Physically-Guided Data-Space Rectified Flow for Precipitation Nowcasting](../../docs/papers/10181_Physically-Guided_Data-Space_Rectified_Flow_for_Precipitatio/index.html) — Wenjie Luo 외, 2026
2. [Plug-and-Play Diffusion Meets ADMM: Dual-Variable Coupling for Robust Medical Image Reconstruction](../../docs/papers/10205_Plug-and-Play_Diffusion_Meets_ADMM_Dual-Variable_Coupling_fo/index.html) — Chenhe Du 외, 2026
3. [Principled Confidence Estimation for Deep Computed Tomography](../../docs/papers/10239_Principled_Confidence_Estimation_for_Deep_Computed_Tomograph/index.html) — Matteo Gätzner 외, 2026
4. [Resolving Blind Inverse Problems under Dynamic Range Compression via Structured Forward Operator Modeling](../../docs/papers/10327_Resolving_Blind_Inverse_Problems_under_Dynamic_Range_Compres/index.html) — Muyu Liu 외, 2026
5. [Scalable Bayesian Inference for Nonlinear Conservation Laws](../../docs/papers/10368_Scalable_Bayesian_Inference_for_Nonlinear_Conservation_Laws/index.html) — Tim Weiland 외, 2026
6. [Training-Free Adversarial Robustness in Computational MRI](../../docs/papers/10625_Training-Free_Adversarial_Robustness_in_Computational_MRI/index.html) — Mahdi Saberi 외, 2026
7. [Deep Ensemble Graph Neural Networks for Probabilistic Cosmic-Ray Direction and Energy Reconstruction](../../docs/papers/3069_Deep_Ensemble_Graph_Neural_Networks_for_Probabilistic_Cosmic/index.html) — 2026.02 · 인용 66
8. [Di-BiLPS: Denoising induced Bidirectional Latent-PDE-Solver under Sparse Observations](../../docs/papers/9511_Di-BiLPS_Denoising_induced_Bidirectional_Latent-PDE-Solver_u/index.html) — Zhonghao Li 외, 2026 · 인용 2
9. [PODiff: Latent Diffusion in Proper Orthogonal Decomposition Space for Scientific Super-Resolution](../../docs/papers/10208_PODiff_Latent_Diffusion_in_Proper_Orthogonal_Decomposition_S/index.html) — Onkar Jadhav 외, 2026 · 인용 97
10. [SENDAI: A Hierarchical Sparse-measurement, EfficieNt Data AssImilation Framework](../../docs/papers/10422_SENDAI_A_Hierarchical_Sparse-measurement_EfficieNt_Data_AssI/index.html) — Xingyue Zhang 외, 2026
11. [GenDA: Generative Data Assimilation on Complex Urban Areas via Classifier-Free Diffusion Guidance](../../docs/papers/9717_GenDA_Generative_Data_Assimilation_on_Complex_Urban_Areas_vi/index.html) — Francisco Giral 외, 2026
12. [LoPhyDA: Low-Rank Tensor and Physics Gradient Guided Diffusion for Atmospheric Data Assimilation](../../docs/papers/9971_LoPhyDA_Low-Rank_Tensor_and_Physics_Gradient_Guided_Diffusio/index.html) — Danyang Peng 외, 2026

---

## S29 · 수치 기상 예보

*제5부 · 물리 기반 신경 시뮬레이션* · **Numerical Weather Forecasting** · *서브카테고리*

`31편` `2022–2026` `가속` `2025+ 28편`

> [!abstract] 화면에 띄울 한 줄
> AI 예보가 운용 NWP를 넘어선 뒤, 경쟁은 스케일링 법칙·하이브리드·해석가능성으로 옮겨갔다.

**31편 중 28편이 2025년 이후다. 이 칸은 2022년 Pangu-Weather가 운용 수치예보를 처음 넘어선 AI 모델이 된 사건에서 출발한다. 그 이후의 4년은 예보 skill 경쟁이 아니라, 모델을 얼마나 믿어도 되는지 설명하는 작업의 시기였다.[4]**

2022년 Pangu-Weather, 2023년 GraphCast와 FuXi가 중장기 전역 예보 skill을 입증하면서 예보는 AI가 이길 수 있는 문제임이 확인됐다. 2026년의 논문들은 그 승리 위에 서 있다. Scaling Laws of Global Weather Models는 GraphCast, AIFS, Aurora, Pangu, SFNO를 대상으로 모델 크기와 데이터셋 크기, 연산 예산의 관계를 측정했다. 더 크게 만들면 어디까지 좋아지는지를 따지는 단계이며, 이는 성능 경쟁이 자원 배분 문제로 바뀌었다는 뜻이다. 타임라인은 확률 예측을 효율적으로 하는 U-Cast, MOSAIC도 같은 갈래로 올린다.[3][4][11]

순수 데이터 기반이 아닌 하이브리드가 지역 예보의 주류가 되고 있다. HITS는 자기회귀 예측과 글로벌 모형의 동역학적 제약을 합쳐 아시아-태평양 태풍의 중기 예보를 겨냥한다. A Synergistic Approach는 O-CNOPs 섭동 방법과 FuXi를 결합한 앙상블로 열대 저기압 추적 예보를 개선한다. Advancing operational global aerosol forecasting는 Vision Transformer와 U-Net을 결합한 AI-GAMFS로 5일·3시간 단위 에어로졸 광학 성분과 표면 농도를 1분 안에 예측한다고 보고한다. 한반도 영향권의 태풍과 대기질이 바로 이 유형이다.[5][6]

기후 모델 쪽에서는 에뮬레이터가 부품 단위로 들어간다. climt-paraformer는 약 100분 길이의 과거 대기 상태를 입력해 대류 서브그리드 과정 에뮬레이션의 안정성을 높였고, FloeNet과 HybridOM은 지구시스템 에뮬레이터의 하이브리드 물리·ML 설계를 보여 준다. Assessing Emulator Design and Training for Modal Aerosol Microphysics는 E3SMv2 에어로졸 모듈의 신경망 에뮬레이션에서 최적화 수렴과 변수 정규화가 중요한 설계 선택임을 체계적으로 평가했다. Bridging the Gap Between Climate Science and Machine Learning은 에뮬레이터 설계 원칙을 튜토리얼로 정리했다.[7][8][9][12][14]

해석가능성과 오차 보정도 가시화됐다. Mechanistic Interpretability Tool for AI Weather Models는 블랙박스 기상 모델 GraphCast의 내부를 들여다보는 오픈소스 시각화 도구를 제시했다. PnP-Corrector는 결합 시공간 예측에서 서브시스템 오차가 서로를 증폭하는 Reciprocal Error Amplification을 정의하고 물리 시뮬레이션과 오차 보정을 분리한다. Residual-Guided Multi-Resolution Refinement of Foundation Models는 시계열 파운데이션 모델의 파라미터를 건드리지 않고 기상학자의 다중 스케일 오차 진단 방식을 흉내 낸다. 모델을 맞히는 일보다 고치는 일이 연구 대상이 됐다.[1][2]

국내 관점에서는 전지구 모델을 새로 만드는 일은 자원 경쟁이 되었고, 공개 모델을 이용한 지역 하이브리드와 운용 검증이 현실적이다. Scalable Cross-Facility Federated Learning for Scientific Foundation Models처럼 데이터 주권과 프라이버시 제약 아래 여러 슈퍼컴퓨터에서 학습하는 방식은 기관 간 협력 모델로 참고할 만하다. 기상청 같은 운용 기관에는 AI 예보를 도입할 때 해석 도구와 오차 보정 체계를 같이 갖추라는 점이 분명한 시사점이다.[10]

> [!tip] 정리
> AI가 운용 NWP를 이긴 뒤, 이 칸의 경쟁축은 속도에서 보장으로 옮겨갔다. 스케일링 법칙으로 투자 규모를 가늠하고 하이브리드와 해석 도구로 신뢰를 만드는 쪽이 운용 단계에 오른다.

**대표 도구·시스템** — Pangu-Weather · GraphCast · FuXi · U-Cast · MOSAIC · EMFormer · FloeNet · HybridOM · ClimateAR · WEATHER-5K

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [PnP-Corrector: A Universal Correction Framework for Coupled Spatiotemporal Forecasting](../../docs/papers/10207_PnP-Corrector_A_Universal_Correction_Framework_for_Coupled_S/index.html) — Hao Wu 외, 2026
2. [Residual-Guided Multi-Resolution Refinement of Foundation Models: A Case Study in Drought Forecasting](../../docs/papers/10325_Residual-Guided_Multi-Resolution_Refinement_of_Foundation_Mo/index.html) — Wentao Gao 외, 2026 · 인용 2
3. [Scaling Laws of Global Weather Models](../../docs/papers/10376_Scaling_Laws_of_Global_Weather_Models/index.html) — Yuejiang Yu 외, 2026
4. [Pangu-Weather: A 3D High-Resolution Model for Fast and Accurate Global Weather Forecast](../../docs/papers/2218_Pangu-Weather_A_3D_High-Resolution_Model_for_Fast_and_Accura/index.html) — Kaifeng Bi 외, 2022 · 인용 126
5. [A Synergistic Approach: Dynamics-AI Ensemble in Tropical Cyclone Forecasting](../../docs/papers/2996_A_Synergistic_Approach_Dynamics-AI_Ensemble_in_Tropical_Cycl/index.html) — 2026.02 · 인용 27
6. [Advancing operational global aerosol forecasting with machine learning](../../docs/papers/3006_Advancing_operational_global_aerosol_forecasting_with_machin/index.html) — Ke Gui 외, 2026.03 · 인용 7
7. [Assessing Emulator Design and Training for Modal Aerosol Microphysics Parameterizations in E3SMv2](../../docs/papers/3026_Assessing_Emulator_Design_and_Training_for_Modal_Aerosol_Mic/index.html) — 2026.04
8. [Bridging the Gap Between Climate Science and Machine Learning in Climate Model Emulation](../../docs/papers/3049_Bridging_the_Gap_Between_Climate_Science_and_Machine_Learnin/index.html) — 2026.03
9. [climt-paraformer: Stable Emulation of Convective Parameterization using a Temporal Memory-aware Transformer](../../docs/papers/3056_climt-paraformer_Stable_Emulation_of_Convective_Parameteriza/index.html) — 2026.04
10. [Scalable Cross-Facility Federated Learning for Scientific Foundation Models on Multiple Supercomputers](../../docs/papers/694_Scalable_Cross-Facility_Federated_Learning_for_Scientific_Fo/index.html) — Yijiang Li 외, 2026.03
11. [U-Cast: A Surprisingly Simple and Efficient Frontier Probabilistic AI Weather Forecaster](../../docs/papers/10652_U-Cast_A_Surprisingly_Simple_and_Efficient_Frontier_Probabil/index.html) — Salva Rühling Cachay 외, 2026
12. [FloeNet: A mass-conserving global sea ice emulator that generalizes across climates](../../docs/papers/3105_FloeNet_A_mass-conserving_global_sea_ice_emulator_that_gener/index.html) — 2026.03
13. [EMFormer: Efficient Multi-Scale Transformer for Accumulative Context Weather Forecasting](../../docs/papers/9580_EMFormer_Efficient_Multi-Scale_Transformer_for_Accumulative/index.html) — Hao Chen 외, 2026
14. [HybridOM: Hybrid Physics-Based and Data-Driven Global Ocean Modeling with Efficient Regional Downscaling](../../docs/papers/9801_HybridOM_Hybrid_Physics-Based_and_Data-Driven_Global_Ocean_M/index.html) — Ruiqi Shu 외, 2026

---

## S30 · 로봇 조작·제어

*제5부 · 물리 기반 신경 시뮬레이션* · **Robotic Manipulation & Control** · *서브카테고리*

`27편` `2023–2026` `가속` `2025+ 24편`

> [!abstract] 화면에 띄울 한 줄
> 신경 시뮬레이터와 연산자 정책이 로봇 제어에 들어왔고, 물리를 정말 아는지 묻는 감사가 함께 등장했다.

**27편 중 24편이 2025년 이후다. 타임라인은 2023년에 시작하지만 핵심 사건은 2026년에 집중돼 있다. 로봇 제어가 강화학습 위주에서 신경 시뮬레이터와 연산자 정책으로 넓어졌고, 동시에 모델이 물리를 이해하는지 묻는 논문이 나왔다.**

가장 눈에 띄는 변화는 영상에서 학습하는 real-to-sim 신경 시뮬레이터다. SoMA는 3D Gaussian Splat 표현 위에 로봇의 관절 공간 행동, 환경 힘, 변형체 동역학을 하나의 잠재 신경 공간으로 결합하고, 실제 매니퓰레이션 영상으로 end-to-end 학습한다. 보지 못한 행동 시퀀스에 대해서도 안정적이고 상호작용에 일관된 장기 재시뮬레이션이 가능하다는 주장이다. MoSA는 등방성 구성 모델을 물리 prior로 유지하고 잔여 이방성에 의한 응력을 학습해 real-to-sim 격차를 줄인다.[7]

제어 대상이 로봇 팔에서 필드로 확장됐다. CINOC는 PDE 상태 필드를 연속 제어 함수로 사상하는 신경 연산자를 미분 가능한 PDE 솔버로 end-to-end 학습시켜, 센서·액추에이터·에이전트 수가 변해도 재학습이 필요 없는 정책을 만든다. NeuronCtrl은 불규칙한 3D 신경 형상 위의 고차원 시공간 필드를 observer, 형상 인식 신경 연산자, flow matching 정책, barrier 기반 안전 필터로 폐루프 제어한다. Neural Control은 평형 제약을 통한 adjoint 학습으로 변형 선형 물체 조작을 다룬다. 안전 필터가 구조에 들어간 점이 눈에 띈다.[6][8]

자동화는 로봇 연구 과정까지 올라왔다. ENPIRE는 coding agent가 환경 구성, 정책 개선, 롤아웃, 진화 네 모듈로 실제 로봇 정책을 자동으로 개선하는 폐루프 시스템이며, 사람이 개입하던 절차를 자동화해 로봇 팀 규모로 확장한다. 타임라인은 로봇 공동 설계를 LLM이 이끄는 Debate2Create도 올린다. 2025년의 Zero-shot sim-to-real transfer for reinforcement learning-based visual servoing of soft continuum arms는 시뮬레이션만 학습한 정책으로 67% 성공률의 제로샷 전이를 보였다. 실물 성능 수치가 이 정도라는 점도 함께 읽어야 한다.[2][3]

이 칸의 가장 중요한 신호는 감사다. 2025년 inductive-bias 탐침은 파운데이션 모델이 세계 모델을 갖고 있는지 의문을 제기했고, From Kepler to Newton은 트랜스포머가 행성 운동 데이터로 뉴턴 세계 모델을 습득하지 못하는 원인을 밝히며 공간 매끄러움, 공간 안정성, 시간 국소성이라는 세 가지 최소 inductive bias를 제안한다. The Perception–Physics Paradox와 TC-Bench는 열대 저기압 위성 영상에서 예측 성능이 높아도 물리 구조를 인코딩한 것이 아닐 수 있음을 지적한다. Distinguishing Imitation Error from Intrinsic Motion Learning Difficulty도 지표가 오류의 원인을 구분하지 못한다고 비판한다.[1][4][5]

국내 제조·로봇 기업과 연구소에 주는 의미는 구체적이다. 현장 영상으로 시뮬레이터를 만들 수 있게 되면 시뮬레이션 구축 비용 구조가 달라진다. 반면 신경 시뮬레이터가 물리를 아는지, 단지 상관을 외웠는지는 별개의 문제다. 도입 전에 보지 못한 행동에 대한 장기 일관성, 안전 필터의 위반률, real-to-sim 격차를 직접 측정해야 한다. 이 요구는 S26의 실패 모드 진단과 같은 계열이다.

> [!tip] 정리
> 로봇 제어는 신경 시뮬레이터를 통해 물리 기반 AI의 가장 실용적인 출구가 됐다. 동시에 모델이 물리를 아는 척하는 위험을 가장 먼저 시험하는 곳이기도 하다.

**대표 도구·시스템** — SHAC-ASAM · SoMA · 3DGSim · DLO-Lab · CINOC · NeuronCtrl · ENPIRE · Debate2Create · Morpheus · TC-Bench

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [The Perception–Physics Paradox: Probing Scientific Alignment with TC-Bench](../../docs/papers/10574_The_PerceptionPhysics_Paradox_Probing_Scientific_Alignment_w/index.html) — Dingling Yao 외, 2026
2. [Zero-shot sim-to-real transfer for reinforcement learning-based visual servoing of soft continuum arms](../../docs/papers/891_Zero-shot_sim-to-real_transfer_for_reinforcement_learning-ba/index.html) — Hsin-Jung Yang 외, 2025 · 인용 1
3. [Debate2Create: Robot Co-design via Multi-Agent LLM Debate](../../docs/papers/9483_Debate2Create_Robot_Co-design_via_Multi-Agent_LLM_Debate/index.html) — Kevin Qiu 외, 2026
4. [Distinguishing Imitation Error from Intrinsic Motion Learning Difficulty](../../docs/papers/9528_Distinguishing_Imitation_Error_from_Intrinsic_Motion_Learnin/index.html) — Zhaorui Meng 외, 2026 · 인용 428
5. [From Kepler to Newton: Inductive Biases Guide Learned World Models in Transformers](../../docs/papers/9696_From_Kepler_to_Newton_Inductive_Biases_Guide_Learned_World_M/index.html) — Ziming Liu 외, 2026 · 인용 12
6. [NeuronCtrl: Geometry-Aware Safe Closed-Loop Generative Control for Neuronal Microenvironment Dynamics](../../docs/papers/10104_NeuronCtrl_Geometry-Aware_Safe_Closed-Loop_Generative_Contro/index.html) — Haowei Xu 외, 2026
7. [SoMA: A Real-to-Sim Neural Simulator for Robotic Soft-Body Manipulation](../../docs/papers/10467_SoMA_A_Real-to-Sim_Neural_Simulator_for_Robotic_Soft-Body_Ma/index.html) — Mu Huang 외, 2026
8. [CINOC: Cardinality-Invariant Neural Operator Policies for Scalable PDE Control](../../docs/papers/9401_CINOC_Cardinality-Invariant_Neural_Operator_Policies_for_Sca/index.html) — Pietro Zanotta 외, 2026
9. [Value iteration for learning concurrently executable robotic control tasks](../../docs/papers/863_Value_iteration_for_learning_concurrently_executable_robotic/index.html) — Sheikh A. Tahmid 외, 2025 · 인용 244

---

## S31 · EHR 파운데이션 모델

*제6부 · 의료·신경 신호 모델링* · **EHR Foundation Models** · *서브카테고리*

`56편` `2024–2026` `가속` `2025+ 56편`

<sub>의료·신경 신호 모델링 고유 배정 213편(중복 포함 592편 · 웹 인덱스 기준) · 서브카테고리 7개 · 본 파트 5개로 82% 커버</sub>

> [!quote] 파트 도입
> 신호를 언어와 이어 붙이는 기반모델은 늘었지만, 환자 간·기관 간 일반화 검증이 임상 문턱이다.

> [!abstract] 화면에 띄울 한 줄
> EHR 모델의 사전학습 목적이 다음 토큰 예측에서 질의 조건·사건 시간 예측으로 옮겨갔다.

**56편으로 대분류 213편 중 가장 큰 칸이며 56편이 2025년 이후다. 전자의료기록 모델은 환자 한 명의 시간 축 전체를 하나의 시퀀스로 보는 방향으로 모였고, 2026년의 질문은 어떻게 사전학습하느냐와 어디까지 믿을 수 있느냐로 옮겨갔다.**

사전학습 목적이 바뀌었다. 타임라인이 짚는 흐름은 다음 토큰 예측에서 사건 시간과 시간 조건 목적(ORA, TCF, MoRGen)으로의 이동이다. 2026년 EveryQuery는 한 걸음 더 나가, 미래 궤적을 생성해 확률을 어림하는 대신 (코드, 기간) 쿼리를 입력받아 단일 forward pass로 발생 확률을 직접 추정한다. 임상 예측 과제마다 모델을 새로 학습하는 방식에서 질의로 과제를 지정하는 방식으로 넘어가는 신호다.

규모와 구조도 달라졌다. SparseEHR는 약 50M 환자 규모에서 sparse·MoE 사전학습을 시도했고, EHR-RAGp는 검색 증강으로 종단 기록을 다룬다. 입력 구성의 세부도 성능을 좌우한다. Pretraining EHR Foundation Models with Patient-Aware Sampling은 Global Stream, Patient Chunks, Patient Sampling 세 가지 시퀀스 구성이 다운스트림 예측 성능에 미치는 영향을 비교했다. 같은 데이터라도 샘플링 설계가 결과를 바꾼다는 뜻이다.[2][6]

모달리티가 EHR 안으로 들어왔다. Autoregressive EHR Foundation Models with Multimodal Inputs는 구조화 이벤트 코드 위주의 모델에 ECG, CXR, 임상 노트를 latent compression과 게이트 교차어텐션으로 조건화한다. PaCX-MAE와 MedMIX는 결측 모달리티에도 버티는 융합을 겨냥하고, 웨어러블 신호도 종단 EHR 신호로 재해석되기 시작했다. PathwayLLM은 시계열과 환자-진단-약물 이종 그래프를 LLM에 결합해 패혈증 위험과 설명을 함께 낸다.[1][3][4]

비판적 신호가 같은 해에 나왔다. Informative Irregularity는 MIMIC-IV-ED에서 측정 타이밍 자체가 예측 신호가 된다는 점을 짚고, 모델 견고성을 irregularity regime별로 층화해 평가하자고 제안한다. Structured Evidence Routing은 환자별 증거 경로를 노출하면서도 EHRSHOT 지도학습 베이스라인 수준의 AUROC에 머물렀다. 희소 오토인코더, conformal prediction, 하위집단 감사가 쌓이는 것은 정확도 경쟁이 신뢰성 감사로 이동한다는 증거다.

국내 관점에서 병목은 모델이 아니라 데이터 접근이다. 공개 벤치마크(MIMIC-IV, EHRSHOT)에서 얻은 결과가 국내 병원 환경에 옮겨지는지는 별개 문제이고, 기록이 한국어이면 더 그렇다. Mode-Aware Phenotype Profiling은 한국어 임상 보고서에서 표현형을 추출하는 작업으로, 언어 특화 모델의 필요를 보여 준다. 환자 데이터를 반출하지 않는 연합·원내 평가 체계를 먼저 갖춘 기관이 모델을 실제로 검증할 수 있다.

> [!tip] 정리
> EHR 파운데이션 모델은 구조 경쟁이 아니라 데이터 접근과 감사 체계의 경쟁이다. 규제 기관이 묻는 것은 평균 성능이 아니라 하위집단과 기관이 달라져도 유지되는지이므로, 그 평가를 먼저 설계하는 쪽이 앞선다.

**대표 도구·시스템** — SparseEHR · EHR-RAGp · EveryQuery · ORA · MOTOR · PyHealth 2.0 · EHRSHOT · MIMIC-IV · MedTPE · ECG-R1

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [PaCX-MAE: Physiology-Augmented Chest X-Ray Masked Autoencoder](../../docs/papers/10154_PaCX-MAE_Physiology-Augmented_Chest_X-Ray_Masked_Autoencoder/index.html) — Yancheng Liu 외, 2026
2. [Pretraining EHR Foundation Models with Patient-Aware Sampling](../../docs/papers/10234_Pretraining_EHR_Foundation_Models_with_Patient-Aware_Samplin/index.html) — Joshua Cesare Placidi 외, 2026 · 인용 112
3. [Autoregressive EHR Foundation Models with Multimodal Inputs](../../docs/papers/9284_Autoregressive_EHR_Foundation_Models_with_Multimodal_Inputs/index.html) — Yuxuan Liu 외, 2026 · 인용 60
4. [MedMIX: Modality-Internal Expert Fusion for Multimodal Medical Diagnosis](../../docs/papers/10014_MedMIX_Modality-Internal_Expert_Fusion_for_Multimodal_Medica/index.html) — Seungik Cho 외, 2026 · 인용 1,331
5. [A Fairness Audit of Medical Imaging Foundation Models on a Multimodal Structured Clinical Benchmark](../../docs/papers/9147_A_Fairness_Audit_of_Medical_Imaging_Foundation_Models_on_a_M/index.html) — Milan Mohan 외, 2026
6. [SparseEHR: Scalable Foundation Modeling for Structured EHR via Conditional Computation](../../docs/papers/10473_SparseEHR_Scalable_Foundation_Modeling_for_Structured_EHR_vi/index.html) — Meysam Ghaffari 외, 2026
7. [Distilling Tabular Foundation Models for Structured Health Data](../../docs/papers/9527_Distilling_Tabular_Foundation_Models_for_Structured_Health_D/index.html) — Aditya Tanna 외, 2026 · 인용 8,430

---

## S32 · 뇌-시각 표상 정렬

*제6부 · 의료·신경 신호 모델링* · **Brain-Visual Representation Alignment** · *서브카테고리*

`33편` `2025–2026` `가속` `2025+ 33편`

> [!abstract] 화면에 띄울 한 줄
> 모델-뇌 정렬이 개별 모델 비교에서 수백 모델 규모의 스케일링 법칙 검증으로 커졌다.

**33편이며 33편이 2025년 이후로, 사실상 전부가 최근 작업이다. 뇌 신호와 시각 모델 표상을 맞대어 보는 연구는 2026년에 두 방향으로 갈렸다. 하나는 정렬을 대규모로 측정하는 방향이고, 다른 하나는 정렬이라는 척도가 무엇을 놓치는지 따지는 방향이다.**

규모의 측정이 전면에 나왔다. Alignment between Brains and AI는 언어·비전 모델 630개(1.33M~72B 파라미터)의 내부 표현을 Natural Scenes Dataset fMRI와 비교해 6천만 건 이상의 CKA 정렬 값을 만들었다. 성능이 높은 모델일수록 뇌와의 정렬이 자발적으로 강해지고, 그 정렬이 학습 성능 향상에 선행한다는 결과다. 모달리티와 규모가 달라도 표상이 수렴한다는 주장이 이 숫자 위에서 나온다.[3]

Multimodal Scaling Laws for Task & Data-Optimized Models of Visual Cortex는 전기생리, fMRI, EEG, MEG를 포함한 8개 신경 데이터셋과 600개 이상의 비전 모델을 같은 파이프라인으로 평가했다. 사전학습 규모, 신경 미세조정, 매핑 규모 세 축에서 모델-뇌 정렬의 스케일링 법칙을 체계적으로 따졌다. 통일 파이프라인이라는 점이 중요하다. 지금까지는 연구마다 데이터와 지표가 달라 정렬 수치를 서로 비교하기 어려웠다.[1]

그러나 정렬 지표 자체에 대한 의문도 같은 해에 제기됐다. Reverse predictivity는 생물학적 뇌 반응이 ANN 유닛 활성을 얼마나 예측하는지 거꾸로 재는 지표로, 순방향 예측력이 높은 모델에도 신경 활동으로 예측되지 않는 비대응 차원이 있음을 보였다. SAEs-BrainMap은 희소 오토인코더로 분해한 비전 모델 특징을 복측 시각 경로 fMRI로 검증해 개념이 어떻게 생겨나는지 추적한다. 정렬이 높다는 말이 곧 같은 계산이라는 뜻은 아니다.[2]

신호 쪽에서는 디코딩과 연결망 표현이 바뀌고 있다. MEG-XL은 2.5분(191k 토큰)의 긴 MEG 문맥으로 사전학습해 기존보다 5~300배 긴 문맥을 쓰고, brain-to-text 단어 디코딩에서 피험자별 데이터를 줄이고도 지도학습 SOTA와 뇌 파운데이션 모델을 앞섰다. 뇌 그래프 쪽은 UDGSL, HiSP-Net, PhenoBrain, SI-IGCL처럼 연결성을 학습하고 표현형을 메커니즘 단계에서 주입하며 피험자 간 변동을 흡수하는 방향이다.[4][5][6]

국내 관점에서 이 칸은 데이터가 곧 진입권이다. Natural Scenes Dataset 같은 공개 자원 위에서 새 지표를 만드는 일은 가능하지만, 임상 연결망 분석(PhenoBrain, SI-IGCL)은 피험자 간 일반화를 다기관 데이터로 입증해야 의미가 생긴다. 뇌 영상 데이터는 개인정보 민감도가 높아 접근 체계 구축이 연구 속도를 정한다.[5][6]

> [!tip] 정리
> 정렬 점수가 높다는 사실은 이제 출발점이다. 어떤 차원이 비대응인지, 피험자가 바뀌어도 유지되는지를 묻는 진단 지표를 가진 쪽이 이 칸의 논의를 이끈다.

**대표 도구·시스템** — SAEs-BrainMap · HiSP-Net · MuHL · PhenoBrain · SI-IGCL · MEG-XL · Natural Scenes Dataset · Torus Graphs · Connector

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Multimodal Scaling Laws for Task & Data-Optimized Models of Visual Cortex](../../docs/papers/10076_Multimodal_Scaling_Laws_for_Task__Data-Optimized_Models_of_V/index.html) — Abdulkadir Gokce 외, 2026
2. [SAEs-BrainMap: Unveiling the Emergence of Specialized Concepts in Deep Models via Brain Alignment](../../docs/papers/10358_SAEs-BrainMap_Unveiling_the_Emergence_of_Specialized_Concept/index.html) — Ziming Mao 외, 2026
3. [Alignment between Brains and AI: Evidence for Convergent Evolution across Modalities, Scales and Training Trajectories](../../docs/papers/9231_Alignment_between_Brains_and_AI_Evidence_for_Convergent_Evol/index.html) — Guobin Shen 외, 2026
4. [MEG-XL: Data-Efficient Brain-to-Text via Long-Context Pre-Training](../../docs/papers/10019_MEG-XL_Data-Efficient_Brain-to-Text_via_Long-Context_Pre-Tra/index.html) — Dulhan Jayalath 외, 2026
5. [PhenoBrain: Phenotype-Conditioned Long-Range Communication for Multi-Modal Brain Network Analysis](../../docs/papers/10178_PhenoBrain_Phenotype-Conditioned_Long-Range_Communication_fo/index.html) — Lingyuan Meng 외, 2026
6. [SI-IGCL: Subject Invariance-aware Inverse Graph Contrastive Learning for Psychiatric Disorder Identification](../../docs/papers/10435_SI-IGCL_Subject_Invariance-aware_Inverse_Graph_Contrastive_L/index.html) — Jiayu Lu 외, 2026
7. [Local Intrinsic Dimension of Representations Predicts Alignment and Generalization in AI Models and Human Brain](../../docs/papers/9964_Local_Intrinsic_Dimension_of_Representations_Predicts_Alignm/index.html) — Junjie Yu 외, 2026

---

## S33 · 의료영상 분할

*제6부 · 의료·신경 신호 모델링* · **Medical Image Segmentation** · *서브카테고리*

<sub>타임라인 분석 명칭: Medical Image Segmentation & Representation</sub>

`32편` `2023–2026` `안정` `2025+ 30편`

> [!abstract] 화면에 띄울 한 줄
> 분할은 성능 경쟁에서 라벨 효율·연합 학습·해석 가능성으로 무게중심이 옮겨갔다.

**32편 중 30편이 2025년 이후이고, 타임라인 상태는 STABLE이다. 대분류의 다른 칸이 가속 중인 것과 달리 이 칸은 성숙한 과제다. 새 연구는 더 높은 분할 점수보다 라벨 없이 쓰기, 병원 간 이동, 내부 해석이라는 주변 문제에 몰려 있다.**

라벨 효율이 가장 눈에 띈다. SPROUT는 H&E 염색의 화학적 특성에서 나온 self-reference prototype과 partial optimal transport(POT-Scan)로 SAM에 positive·negative point prompt를 만들어, 학습도 주석도 없이 핵 인스턴스를 분할한다. SAM/SAM2 같은 범용 분할기를 도메인 지식으로 호출하는 구조다. 주석 비용이 병목인 병리 영상에서 현실적인 경로이고, 학습 파이프라인 없이도 쓸 수 있다는 점이 크다.

병원 간 분포 이동을 다루는 연합 학습도 활발하다. Shift-Dependent Asymmetry는 인코더가 covariate shift에, 디코더가 concept shift에 지배된다는 비대칭을 규명하고, 인코더에서는 A를 디코더에서는 B를 개인화하는 Inverse Asymmetric Tuning을 제안했다. Rethinking Federated Prompt Learning은 의료 영상에서 텍스트 튜닝이 frozen visual encoder의 특징 기하를 무너뜨린다고 지적한다. 데이터를 모으지 못하는 환경이 연구의 전제가 된 것이다.[3][4]

아키텍처는 효율 쪽이다. S2M-Net은 self-attention의 O((HW)^2C) 복잡도를 스펙트럼-공간 토큰 혼합과 형태 인지 어댑터로 피하고, 3D 대형 커널 최적화는 CSLA 재매개변수화가 커널 중심부에서 빨리 수렴하는 공간적 불균일 학습률을 낳는다는 점을 이론화한다. Mosaic MAE는 patch size가 사실상 고역통과 필터처럼 작동한다고 밝혀 사전학습 설계에 근거를 줬다. 새 구조보다 기존 구조가 왜 작동하는지 설명하는 논문이 늘었다.[6]

해석과 감사가 이 칸의 비판 축이다. Med-SegLens는 분할 모델 활성을 sparse autoencoder로 분해해 아키텍처·데이터셋을 가로지르는 latent 수준 diffing을 제공한다. Auditing Sybil의 S(H)NAP은 폐암 위험 예측 모델의 근거를 상관이 아니라 3D diffusion 기반 개입으로 검증한다. 여기에 FlowPET, OT-Bridge 같은 생성·개입 영상과, 이해와 생성을 한 모델에 묶는 UniMedVL, SynerMedGen이 겹치며 분할 모델은 설명 가능한 시스템의 부품이 되어 간다.[1][5][7]

국내 관점에서 이 칸은 규제 심사와 가장 가깝다. 영상 소프트웨어는 기관마다 장비와 프로토콜이 다르므로 단일 병원 점수는 설득력이 없다. 연합 개인화, 지속 학습(MedCRP-CL), 분포 이동 평가를 갖추고 모델 내부를 감사 가능한 형태로 남기는 팀이 다기관 일반화 검증 요구에 대응할 수 있다.[2]

> [!tip] 정리
> 성숙한 과제에서 차별점은 점수가 아니라 데이터 없이 쓰는 법, 병원이 바뀌어도 유지되는 법, 내부를 설명하는 법이다. 이 세 가지가 임상 도입의 실제 관문이다.

**대표 도구·시스템** — S2M-Net · Mosaic MAE · SPROUT · SAM/SAM2 · FlowPET · UniMedVL · Med-SegLens · MedCRP-CL · IPOD

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Med-SegLens: Latent-Level Model Diffing for Interpretable Medical Image Segmentation](../../docs/papers/10005_Med-SegLens_Latent-Level_Model_Diffing_for_Interpretable_Med/index.html) — Salma J. Ahmed 외, 2026 · 인용 872
2. [MedCRP-CL: Continual Medical Image Segmentation via Bayesian Nonparametric Semantic Modality Discovery](../../docs/papers/10009_MedCRP-CL_Continual_Medical_Image_Segmentation_via_Bayesian/index.html) — Ziyuan Gao, 2026
3. [Rethinking Federated Prompt Learning for Medical Images: From Textual Tuning to Visual Manifold Anchoring](../../docs/papers/10331_Rethinking_Federated_Prompt_Learning_for_Medical_Images_From/index.html) — Yipan Wei 외, 2026
4. [Shift-Dependent Asymmetry: Orthogonal Inverse Low-Rank Adaptation for Federated Medical Segmentation](../../docs/papers/10433_Shift-Dependent_Asymmetry_Orthogonal_Inverse_Low-Rank_Adapta/index.html) — Xingyue Zhao 외, 2026
5. [Auditing Sybil: Explaining Deep Lung Cancer Risk Prediction Through Generative Interventional Attributions](../../docs/papers/9271_Auditing_Sybil_Explaining_Deep_Lung_Cancer_Risk_Prediction_T/index.html) — Bartlomiej Sobieski 외, 2026
6. [S2M-Net: Spectral-Spatial Mixing with Morphology-Aware Adaptive Loss for Medical Image Segmentation](../../docs/papers/10356_S2M-Net_Spectral-Spatial_Mixing_with_Morphology-Aware_Adapti/index.html) — Sanaullah Chowdhury 외, 2026
7. [SynerMedGen: Synergizing Medical Multimodal Understanding with Generation via Task Alignment](../../docs/papers/10526_SynerMedGen_Synergizing_Medical_Multimodal_Understanding_wit/index.html) — Weiren zhao 외, 2026

---

## S34 · 멀티모달 의료영상 진단

*제6부 · 의료·신경 신호 모델링* · **Multimodal Medical Diagnostic Imaging** · *서브카테고리*

<sub>타임라인 분석 명칭: Multimodal Medical Diagnostic Imaging & Med-LVLMs</sub>

`27편` `2023–2026` `가속` `2025+ 25편`

> [!abstract] 화면에 띄울 한 줄
> 의료 MLLM의 유창함과 진단 타당성의 간극이 2026년에 기하·환각 교정과 도구 사용으로 다뤄진다.

**27편 중 25편이 2025년 이후다. 의료 영상에 멀티모달 LLM을 붙이는 흐름은 2023년 GPT-4V 임상 사례에서 말은 유창하지만 진단은 틀릴 수 있다는 간극을 드러냈고, 2026년 연구의 상당수가 그 간극의 원인과 교정법을 직접 겨냥한다.**

원인 진단이 구체화됐다. Med-Scout는 MLLM이 의료 영상에서 스케일, 위상, 이상 일관성 같은 객관적 기하 제약을 지키지 못하는 geometric blindness를 갖는다고 규명하고, 라벨 없는 영상의 내재적 기하 논리로 RL 사후학습을 하는 방식으로 교정했다. 3D CT용 VLM을 다룬 논문은 표면적 유사도 보상이 Evaluation Hallucination을 낳는다고 지적한다. 좋은 문장과 맞는 소견은 다르다는 문제의식이 보상 설계까지 내려왔다.[1]

환각 완화는 모델 내부 개입으로 갔다. MEDA는 의료 영상 해석 전용 최초의 activation editing으로, Query-decisive Manifestation Steering과 Principle-driven Diagnosis Induction을 결합해 지각과 인지 해석을 함께 끌어올린다. MedREK는 공유 query-key MLP와 어텐션 기반 prompt encoder로 의료 지식 공간의 표상 겹침을 풀고 batch editing을 지원하는 검색 기반 편집이다. 재학습 없이 틀린 지식을 고친다는 점이 운영 관점의 장점이다.[4][5]

추론 방식은 에이전트형이다. Ophiuchus는 텍스트 CoT의 한계를 넘기 위해 SAM2, BiomedParse, zoom-in 도구를 추론 과정에 능동적으로 넣는 think with images 프레임워크이며, 3DMedAgent와 PathCTM도 같은 방향이다. ORBIT은 습성 황반변성 같은 만성 안질환을 POMDP로 정식화하고 반사실적 시각 예견으로 치료 후 해부학적 상태를 상상해 검증한다. 진단에서 예후 시뮬레이션으로 범위가 넓어졌다.[3][6][7]

평가 과학이 병행해 자란다. Seizure-Semiology-Suite(S^3)는 438개 발작 비디오와 35,000개 이상의 밀집 라벨로 ILAE 정의 20개 semiological feature의 이해를 재는 데이터셋이자 벤치마크다. SpatialMed, 병리 다중 이미지 추론 VQA, Medical VQA 견고성 분해도 같은 계열이다. ProConMV는 다중 뷰 안저 영상과 병변 마스크, 임상 텍스트를 개념 기반 인과 추론과 이중 불확실성 융합으로 묶어 검증 가능한 당뇨망막병증 진단을 제시한다.[2]

국내 관점에서 이 칸은 기술 격차보다 평가와 규제 대응의 격차다. 해외 범용 의료 MLLM을 들여올 때 어떤 소견에서 틀리는지 한국 임상 환경에서 측정할 기준이 없다면 도입 판단을 할 수 없다. 환자 영상과 판독문을 병원 밖으로 내지 않고도 오류 유형을 감사하는 평가 체계가 선행 투자 대상이다.

> [!tip] 정리
> 유창함은 이제 병목이 아니다. 어디서 틀리는지를 구조적으로 보이는 모델과 평가셋이 임상 승인에서 요구되는 증거가 된다.

**대표 도구·시스템** — GPT-4V · Med-Gemini · PathChat · MEDA · MedREK · Ophiuchus · 3DMedAgent · ORBIT · SpatialMed · EviScreen

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Med-Scout: Curing MLLMs' Geometric Blindness in Medical Perception via Geometry-Aware RL Post-Training](../../docs/papers/10004_Med-Scout_Curing_MLLMs_Geometric_Blindness_in_Medical_Percep/index.html) — Anglin Liu 외, 2026
2. [Seizure-Semiology-Suite(S^3): A Clinically Multimodal Dataset, Benchmark, and Models for Seizure Semiology Understanding](../../docs/papers/10406_Seizure-Semiology-SuiteS3_A_Clinically_Multimodal_Dataset_Be/index.html) — Lina Zhang 외, 2026
3. [3DMedAgent: Unified Perception-to-Understanding for 3D Medical Analysis](../../docs/papers/9139_3DMedAgent_Unified_Perception-to-Understanding_for_3D_Medica/index.html) — Ziyue Wang 외, 2026
4. [MEDA: Medical-Oriented Activation Editing for Hallucination Mitigation in Medical Large Vision-Language Model](../../docs/papers/10006_MEDA_Medical-Oriented_Activation_Editing_for_Hallucination_M/index.html) — Tianbo Wang 외, 2026
5. [MedREK: Retrieval-Based Editing for Medical LLMs with Key-Aware Prompts](../../docs/papers/10016_MedREK_Retrieval-Based_Editing_for_Medical_LLMs_with_Key-Awa/index.html) — Shujun Xia 외, 2026
6. [Ophiuchus: Incentivizing Tool-augmented ''Think with Images'' for Joint Medical Segmentation, Understanding and Reasoning](../../docs/papers/10137_Ophiuchus_Incentivizing_Tool-augmented_Think_with_Images_for/index.html) — Yankai Jiang 외, 2026
7. [ORBIT: A Prognostic World Model for Ocular Reasoning Based on Imagined Trajectories](../../docs/papers/10145_ORBIT_A_Prognostic_World_Model_for_Ocular_Reasoning_Based_on/index.html) — Jiangtao Yan 외, 2026

---

## S35 · 생체신호 파운데이션 모델

*제6부 · 의료·신경 신호 모델링* · **Physiological Signal Foundation Models** · *서브카테고리*

`27편` `2025–2026` `가속` `2025+ 27편`

> [!abstract] 화면에 띄울 한 줄
> ECG·수면·PPG에서 토큰 없는 인코더와 대규모 오픈 말뭉치가 생체신호 기반모델의 기본값이 되고 있다.

**27편이 전부 2026년 논문이다. 수면, ECG, PPG, EDA, 호흡음까지 생체신호 기반모델이 한꺼번에 나왔고 상태는 ACCELERATING이다. 공통 변화는 모델이 신호 종류별 설계에서 벗어나 대규모 사전학습과 표준 벤치마크를 갖추는 쪽이다.**

수면이 가장 빨리 성숙했다. OSF: On Pre-training and Scaling of Sleep Foundation Models는 대규모 다기관 수면 데이터 166,500시간으로 SleepBench를 구축해 완전 오픈소스 벤치마크로 공개하고, 채널 불변 표현 학습과 스케일링이 핵심임을 밝혔다. SleepMaMi와 PSG-M&m은 초 단위 미세 구조와 야간 전체 거시 구조를 계층적 이중 인코더로 함께 학습한다. 공통 벤치마크가 생기면서 모델 비교가 가능해졌다.[2][8]

신호와 언어의 결합도 시작됐다. SleepLM은 다중모달 polysomnography 신호를 자연어와 정렬해 수면 상태를 설명하고 질의하게 하며, 100K시간 규모의 sleep-text 데이터셋과 ReCoCa 사전학습 구조를 함께 제안했다. 임상의가 신호 파형 대신 문장으로 묻고 답을 받는 인터페이스로 가는 길이다. 다만 자연어 설명이 임상적으로 맞는지를 검증하는 평가는 아직 이 계열의 약한 고리다.[5]

인코더 설계는 고정 패치 토큰화를 버리는 쪽이다. MedMamba는 Mamba 상태공간 모델에 멀티스케일 컨볼루션과 공간 그래프 모듈을 결합해 의료 시계열의 비정상성을 다루고, NeurOCNN은 PDE용 neural operator를 EEG·EOG·ECG로 옮겨 이산화에 불변한 예측을 한다. SIGMA-PPG는 통계 사전지식 기반 적대적 마스킹으로 PPG의 중복과 잡음을 다루고, SyneCo는 ECG와 PPG 같은 동시기록 신호의 시너지를, PULSE는 동역학 모델로 전이 가능한 정보와 샘플별 잡음을 분리한다.[3][6][7]

범위는 임상 음향과 새 센싱으로도 넓어졌다. WIPSNet은 야간 임피던스 뉴모그래피를 CWT 스칼로그램 3D 볼륨으로 바꿔 소아 천명을 탐지하고, Cardio-mmFlow는 ECG로 mmWave 레이더 신호를 합성하며, NEAR-SSB는 스펙트럼 슈뢰딩거 브리지로 ECG 잡음을 제거한다. 동시에 Spherical Procrustes Alignment는 의료 오디오 모델의 과신을 기하학적 병리로 규명했다. 정확도와 함께 보정(calibration)이 평가 항목이 된 것이다.[1][4]

국내 관점에서 이 칸의 위험은 일반화다. 대분류 insight가 지적하듯 환자 간 일반화와 임상 배포 가능성의 검증이 부족하다. Robust ECG Classification이 환자 단위 평가를 택한 이유가 거기 있다. 웨어러블과 수면 센서 데이터는 기기와 인구집단에 따라 분포가 달라지므로, 다기관·다기기 검증 설계와 데이터 거버넌스를 갖춘 팀이 승인 단계에서 유리하다.

> [!tip] 정리
> 생체신호 기반모델은 모델이 아니라 말뭉치와 평가 프로토콜로 경쟁한다. 환자 단위·기관 단위 일반화를 증명하는 체계가 임상 승인의 사실상 전제가 될 것이다.

**대표 도구·시스템** — MedMamba · NeurOCNN · WaveFormer · SleepMaMi · SleepLM · SIGMA-PPG · PapaGei · wav2vec2 · PULSE · SyneCo

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [NEAR-SSB: Noisy ECG Artifact Removal via Spectral Schrodinger Bridge](../../docs/papers/10084_NEAR-SSB_Noisy_ECG_Artifact_Removal_via_Spectral_Schrodinger/index.html) — Beom Kim 외, 2026
2. [OSF: On Pre-training and Scaling of Sleep Foundation Models](../../docs/papers/10148_OSF_On_Pre-training_and_Scaling_of_Sleep_Foundation_Models/index.html) — Zitao Shuai 외, 2026
3. [SIGMA-PPG: Statistical-prior Informed Generative Masking Architecture for PPG Foundation Model](../../docs/papers/10440_SIGMA-PPG_Statistical-prior_Informed__Generative_Masking_Arc/index.html) — Zongheng Guo 외, 2026
4. [Cardio-mmFlow: A Gaussian-Prior-Free Physics-Informed Flow Matching Framework for Electrocardiogram to mmWave Radar Synthesis](../../docs/papers/9376_Cardio-mmFlow_A_Gaussian-Prior-Free_Physics-Informed_Flow_Ma/index.html) — Ziyang LIU 외, 2026 · 인용 17
5. [SleepLM: Natural-Language Intelligence for Human Sleep](../../docs/papers/10454_SleepLM_Natural-Language_Intelligence_for_Human_Sleep/index.html) — Zongzhe Xu 외, 2026
6. [MedMamba: Multi-View State Space Models with Adaptive Graph Learning for Medical Time Series Classification](../../docs/papers/10012_MedMamba_Multi-View_State_Space_Models_with_Adaptive_Graph_L/index.html) — Da Zhang 외, 2026
7. [NeurOCNN: A Neural-Operator-Based Model for Physiological Time Series](../../docs/papers/10103_NeurOCNN_A_Neural-Operator-Based_Model_for_Physiological_Tim/index.html) — Daya Kumar 외, 2026
8. [SleepMaMi: A Universal Sleep Foundation Model for Integrating Macro- and Micro-structures](../../docs/papers/10455_SleepMaMi_A_Universal_Sleep_Foundation_Model_for_Integrating/index.html) — Keondo Park 외, 2026

---

## S36 · 동료심사 피드백 데이터셋

*제7부 · 과학 문헌·동료심사* · **Peer Review Feedback Datasets** · *서브카테고리*

<sub>타임라인 분석 명칭: Peer Review Feedback Datasets & LLM Reviewers</sub>

`61편` `2019–2026` `가속` `2025+ 35편`

<sub>과학 문헌·동료심사 고유 배정 210편(중복 포함 463편 · 웹 인덱스 기준) · 서브카테고리 7개 · 본 파트 5개로 82% 커버</sub>

> [!quote] 파트 도입
> AI 저작·심사 정책을 의견이 아니라 데이터로 설계할 근거가 쌓였다. 이제 병목은 검증이다.

> [!abstract] 화면에 띄울 한 줄
> 심사 코퍼스가 쌓이자 AI 리뷰어가 AAAI-26 전 제출 논문에 실전 배치됐다.

**61편, 그중 35편이 2025년 이후다. 이 칸은 대분류에서 가장 크고, 논문이 아니라 심사라는 제도 자체를 데이터로 만든다. 2026년에는 그 데이터 위에서 만든 AI 리뷰어가 실제 학회에 투입됐다.**

기반은 공개 심사 코퍼스다. ORB, ContraSciView, ReviewMT, Re2 같은 데이터가 쌓였고, 2026년 ReviewArena는 NeurIPS, ICLR, ICML, CoRL, COLM, EMNLP, TMLR 7개 venue에서 51,529편 논문과 196,099개 리뷰를 모았다. 여기에 venue를 구분해 채점하는 1,002편 규모 ReviewArena-Eval을 붙였다. 2025년에는 OpenReview를 LLM 시대의 공동체 자산으로 보호하고 활용해야 한다는 입장 논문도 나왔다. 심사 기록이 곧 학습 자원이라는 인식이다.[6]

이 코퍼스로 리뷰어 모델이 만들어졌다. 2025년 DeepReview는 인간 전문가의 심사 과정을 모방하는 다단계 틀을 제안하고 DeepReview-13K로 DeepReviewer-14B를 학습시켰다. 이 모델은 CycleReviewer-70B, GPT-o1, DeepSeek-R1보다 좋은 결과를 내면서 토큰을 덜 썼다. 대형 모델이 아니라 전문가 리뷰로 미세조정한 중형 모델이 이긴다는 점이, 기관 내부 심사 보조 도구를 직접 만들 수 있다는 뜻이다.

2026년 AAAI-26 AI Review Pilot은 결정적 전환점이다. frontier LLM 기반 다단계 리뷰 시스템을 메인트랙 제출 22,977편 전체에 적용하고, 대규모 설문과 새 벤치마크로 품질과 유용성을 측정했다. 실험실 평가가 아니라 첫 학회 규모 현장 배포다. 같은 시기 Three AI-powered steps to faster, smarter peer review처럼 음성 받아쓰기와 오프라인 LLM으로 개별 심사자의 시간을 줄이는 워크플로우도 제시됐다.[3]

반면 감사 신호도 같은 해에 나왔다. ReviewEval은 AI 리뷰의 신뢰성을 재는 틀을 만들었고, Mind the blind spots는 LLM 리뷰가 전문가와 같은 핵심 측면을 보는지 focus 단위로 따져 사각지대를 드러냈다. 숨은 프롬프트로 AI 사용 리뷰어를 적발하려던 학회 시도는 신뢰를 해친다는 반발을 샀고, How AI slop is causing a crisis in computer science는 저품질 논문 급증으로 심사 체계가 과부하라고 전했다. Position: Preventing the Collapse of Peer Review Requires Verification-First AI는 인간 심사를 흉내 내는 방식이 아니라 검증 우선 방식을 요구한다.[1][2][4]

국내 학회·학술지·연구비 심사 기관에 이 칸이 주는 시사점은 정책의 근거다. 허용할지 금지할지를 의견으로 다투던 단계에서, AAAI-26 같은 배포 사례와 ReviewEval류 감사 도구로 일치도를 측정해 결정하는 단계로 넘어왔다. 한국어 심사 기록은 이 코퍼스에 거의 없으므로, 국내 심사 데이터의 비식별 공개 체계가 없으면 도입 판단도 해외 수치에 의존하게 된다.[4]

> [!tip] 정리
> AI 심사 도입은 이제 기술이 아니라 보고 의무의 문제다. 일치도와 실패 모드를 공개하는 쪽이 정책 논의에서 주도권을 갖는다.

**대표 도구·시스템** — OpenReviewer · DeepReviewer-14B · CycleResearcher/CycleReviewer · MARG · Reviewer2 · REMOR · ReviewEval · AgentReview · XtraGPT · ReviewArena · FIRSTPASS · LazyReview

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Position: Preventing the Collapse of Peer Review Requires Verification-First AI](../../docs/papers/10216_Position_Preventing_the_Collapse_of_Peer_Review_Requires_Ver/index.html) — Lei You 외, 2026
2. [Mind the blind spots: A focus-level evaluation framework for llm reviews](../../docs/papers/537_Mind_the_blind_spots_A_focus-level_evaluation_framework_for/index.html) — Hyungyu Shin 외, 2025 · 인용 3
3. [Three AI-powered steps to faster, smarter peer review](../../docs/papers/809_Three_AI-powered_steps_to_faster_smarter_peer_review/index.html) — Dritjon Gruda, 2025.03 · 인용 4
4. [ReviewEval: An evaluation framework for AI-generated reviews](../../docs/papers/679_Revieweval_An_evaluation_framework_for_ai-generated_reviews/index.html) — Madhav Krishan Garg 외, 2025 · 인용 2
5. [AI-Assisted Peer Review at Scale: The AAAI-26 AI Review Pilot](../../docs/papers/10928_AI-Assisted_Peer_Review_at_Scale_The_AAAI-26_AI_Review_Pilot/index.html) — Joydeep Biswas 외, 2026.04 · 인용 1
6. [ReviewArena: A Large-Scale Cross-Conference Dataset and Benchmark for LLM Peer Review](../../docs/papers/10341_ReviewArena_A_Large-Scale_Cross-Conference_Dataset_and_Bench/index.html) — Samarth P 외, 2026
7. [FIRSTPASS: A Multi-Domain, Multi-Round Peer Review Dataset Grounded in Real Editorial Outcomes](../../docs/papers/9652_FIRSTPASS_A_Multi-Domain_Multi-Round_Peer_Review_Dataset_Gro/index.html) — Prabhjot Singh 외, 2026

---

## S37 · 과학 문헌 검색·QA

*제7부 · 과학 문헌·동료심사* · **Scientific Literature Retrieval QA** · *서브카테고리*

<sub>타임라인 분석 명칭: Scientific Literature Retrieval & QA</sub>

`32편` `2019–2026` `가속` `2025+ 18편`

> [!abstract] 화면에 띄울 한 줄
> 문헌 검색이 키워드 매칭에서 관계 인지·멀티모달 에이전트로 넘어갔다.

**32편, 18편이 2025년 이후다. 문헌 검색과 QA는 SciBERT와 PubMedQA 시대의 도메인 언어모델에서 출발해, 2025–2026년에 스스로 논문을 찾고 읽고 인용을 따라가는 에이전트로 바뀌었다.**

전환의 중심은 검색 에이전트다. 2025년 PaSa는 검색 도구 사용, 논문 읽기, 인용 네트워크 탐색을 묶은 LLM 에이전트로, 합성 데이터 AutoScholarQuery로 학습했는데도 실환경 RealScholarQuery에서 Google Scholar와 GPT-4o 기반 방법을 크게 넘어섰다. 2026년 PaSaMaster는 여기서 한 걸음 더 나아가, 복잡한 연구 의도를 반복적으로 정제하며 논문을 생성하지 않고 검증된 코퍼스에서 관련도 순위만 매긴다. hallucination을 모델 개선이 아니라 구조로 제거한 설계다.

평가의 단위도 바뀌었다. SciNet은 269만 편 규모 메타데이터베이스 위에서 ego-centric, pair-wise, path-wise 세 수준의 관계 인지형 검색을 8,940개 과제로 평가한다. 논문 한 편을 찾는 것이 아니라 논문 사이의 관계와 경로를 찾는 능력을 묻는다. 같은 해 멀티모달 문헌 에이전트는 그림과 표를 1급 검색 대상으로 다루고 VLM zoom loop와 명시적 abstention을 갖춰 LAB-Bench 2의 FigQA2, LitQA3, TableQA2에서 공개 baseline 대비 최고 성능을 냈다. 모르면 모른다고 답하는 기능이 성능 지표에 들어왔다.[3]

검색은 가설 생성으로 이어진다. SciMuse는 5,800만 편 논문과 LLM으로 개인화된 연구 아이디어를 만들고 100명 이상의 연구 그룹 리더 평가로 흥미도를 예측했다. ResearchLink는 지식 그래프의 경로 특징과 임베딩을 결합해 도메인 독립적으로 가설을 만들고, EO-Agents는 NASA 지구관측 지식 그래프에서 1,475개 데이터셋을 대상으로 160개의 타당한 가설을 냈다. Training AI Co-Scientists Using Rubric Rewards는 기존 논문에서 뽑은 연구 목표와 rubric으로 연구 계획 생성 모델을 강화학습시킨다.[1][2]

문헌이 민감한 자산인 경우도 있다. 2026년 Giovanna는 DZNE와 UK DRI 두 신경퇴행성질환 연구기관의 기관 문헌만을 근거로 하는 privacy-aware RAG로, 원문 텍스트를 교환하지 않고도 기관 간 지식 융합을 가능하게 한다. 한편 PaSa류의 성능 주장은 대부분 영어 논문 중심 코퍼스 위에서 측정된 것이라는 점은 기억해야 한다. 한국어 논문과 국내 학술지를 포함한 평가는 이 칸에 보이지 않는다.

국내 연구기관에는 두 가지가 실용적이다. 첫째, 외부 API 없이 기관 내부 보고서와 특허, 과제 결과물 위에 PaSaMaster식 순위 기반 검색을 올리는 것이다. 생성하지 않으므로 인용 오류 위험이 낮다. 둘째, Giovanna 같은 구조를 참고해 기관 간 공동연구에서 원문 교환 없이 문헌 지식을 공유하는 체계를 설계하는 것이다.

> [!tip] 정리
> 문헌 검색은 더 이상 보조 기능이 아니라 자율 연구의 입력단이다. 입력의 신뢰는 생성이 아니라 검증된 코퍼스에서 순위를 매기는 설계에서 나온다.

**대표 도구·시스템** — SciBERT · PubMedQA · PaperQA2 · OpenScholar · HiPerRAG · PaSa · SciNet · EarthSE · SciQAG · AutoReproduce · PRISM

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Training AI Co-Scientists Using Rubric Rewards](../../docs/papers/10622_Training_AI_Co-Scientists_Using_Rubric_Rewards/index.html) — Shashwat Goel 외, 2026
2. [EO-Agents: A Three-Agent LLM Pipeline for Earth Observation Hypothesis Generation](../../docs/papers/9588_EO-Agents_A_Three-Agent_LLM_Pipeline_for_Earth_Observation_H/index.html) — Mahyar Ghazanfari 외, 2026
3. [SciNet: Evaluating AI Agents in Relation-Aware Scientific Literature Retrieval](../../docs/papers/10391_SciNet_Evaluating_AI_Agents_in_Relation-Aware_Scientific_Lit/index.html) — Chenyang Shao 외, 2026 · 인용 3,133
4. [Towards Self-Evolving Agentic Literature Retrieval](../../docs/papers/10617_Towards_Self-Evolving_Agentic_Literature_Retrieval/index.html) — Yuwen Du 외, 2026 · 인용 1,798
5. [IRIS: An Agentic Multi-Phase Framework for Automated Scientific Literature Review](../../docs/papers/9847_IRIS_An_Agentic_Multi-Phase_Framework_for_Automated_Scientif/index.html) — Sergey Kolchenko 외, 2026 · 인용 48
6. [ResearchAgent: Iterative Research Idea Generation over Scientific Literature with Large Language Models](../../docs/papers/668_ResearchAgent_Iterative_Research_Idea_Generation_over_Scient/index.html) — Jinheon Baek 외, 2025.02 · 인용 34

---

## S38 · 신규성 기반 아이디어

*제7부 · 과학 문헌·동료심사* · **Novelty-Driven Scientific Idea Retrieval** · *서브카테고리*

`30편` `2022–2026` `가속` `2025+ 21편`

> [!abstract] 화면에 띄울 한 줄
> 아이디어 생성은 쉬워졌고, 참신성과 표절을 재는 감사가 병목이 됐다.

**30편, 21편이 2025년 이후다. 신규성 기반 아이디어 검색은 문헌을 읽고 새 연구 방향을 제안하는 시스템을 다룬다. 2025–2026년에는 생성기보다 그 출력을 재고 의심하는 도구가 더 많이 나왔다.**

생성기의 토대는 문헌 근거형 설계다. 2022년 의미망 링크 예측으로 미래 연구 주제를 예측한 뒤, SciMON, SciPIP, Nova, Chain of Ideas, Scideator, Spacer가 문헌에서 영감을 검색해 신규성을 최적화하는 방식을 정착시켰다. 2026년 Predicting new research directions in materials science using large language models and concept graphs는 재료과학 초록에서 개념 그래프를 만들어 아직 결합되지 않은 주제 조합을 예측한다. Chimera는 28,000편 이상에서 아이디어 재조합 사례를 추출한 지식베이스를 제공한다.[5][9]

평가가 산업이 됐다. 2025년 AI Idea Bench 2025는 3,495편의 AI 논문과 그것을 촉발한 선행연구를 정답으로 삼아 데이터 누출 없이 정렬도, 참신성, 실현가능성을 잰다. RND는 절대 밀도가 아니라 의미 이웃의 상대 밀도로 도메인에 상관없이 참신성을 판단하고, GraphEval은 아이디어를 관점으로 분해해 그래프로 연결한다. 2026년 InnoEval은 이질적 지식 검색과 다중 페르소나 리뷰 보드로 사람 전문가 수준의 평가를 재현하려 한다.[4][6][8]

가장 중요한 신호는 표절과 탐지다. All that glitters is not novel은 LLM이 낸 연구 문서의 24%가 기존 논문을 정교하게 표절했고 내장 탐지 시스템도 우회했다고 보고했다. What counts as plagiarism? AI-generated papers pose new risks는 문장을 베끼지 않아도 방법과 아이디어를 출처 없이 가져오는 idea plagiarism이 쟁점이며, 원저자와 AI Scientist 개발팀의 주장이 갈려 합의가 없다고 전한다. 2026년 SciContrib-Bench는 가설부터 초록까지 단계별로 AI 기여물을 사람 글과 구별할 수 있는지 측정해 이 논의를 정량화했다.[2][3]

생성 효과 자체도 엇갈린다. 800명 이상이 참여한 실험에서 ChatGPT 아이디어에 대한 노출은 개인 창의성에는 영향이 없었지만 집단 다양성과 그 변화 속도를 높였다. 2026년 Read, Grep, and Synthesize는 PaperGym으로, cross-domain retrieval 시스템이 의미론적 근거를 쓰는지 아니면 다양한 seed에 노출되는 것만으로 이득을 보는지 진단한다. 좋아 보이는 성능의 원인을 분리해 보는 작업이다.[1]

국내 연구비 기관과 학회에는 정책 근거가 생겼다. AI 생성 아이디어의 사용 허용 여부는 표절 비율과 단계별 탐지 가능성이라는 측정치로 논의할 수 있다. 과제 평가에서 아이디어 참신성 점수를 쓰려면 RND나 InnoEval 같은 도구의 한계와 편향을 먼저 검증해야 하며, 한국어 제안서에서의 성능은 이 칸에서 확인되지 않는다.[8]

> [!tip] 정리
> 아이디어는 이제 싸다. 가치는 그 아이디어가 정말 새로운지, 누구의 것인지를 판정하는 능력에 있다.

**대표 도구·시스템** — SciMON · SciPIP · Nova · Chain of Ideas · Scideator · Spacer · GraphEval · InnoEval · AI Idea Bench 2025 · LiveIdeaBench · Chimera · MIR · SciPaths

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Read, Grep, and Synthesize: Diagnosing Cross-Domain Seed Exposure for LLM Research Ideation](../../docs/papers/10297_Read_Grep_and_Synthesize_Diagnosing_Cross-Domain_Seed_Exposu/index.html) — Yunju Choi 외, 2026 · 인용 76
2. [SciContrib-Bench: Mapping the Autonomy Landscape of AI Scientists Through Stage-Dependent Detectability](../../docs/papers/10386_SciContrib-Bench_Mapping_the_Autonomy_Landscape_of_AI_Scient/index.html) — Raghav Agarwal 외, 2026
3. [What counts as plagiarism? AI-generated papers pose new risks](../../docs/papers/10767_what_counts_as_plagiarism_ai-generated_papers_pose_new/index.html) — Ananya, 2025.08 · 인용 4
4. [Ai idea bench 2025: Ai research idea generation benchmark](../../docs/papers/10924_Ai_idea_bench_2025_Ai_research_idea_generation_benchmark/index.html) — DeepSeek-AI 외, 2025
5. [Predicting new research directions in materials science using large language models and concept graphs](../../docs/papers/3212_Predicting_new_research_directions_in_materials_science_usin/index.html) — Thomas Marwitz 외, 2026.04 · 인용 2
6. [GraphEval: A lightweight graph-based llm framework for idea evaluation](../../docs/papers/392_Grapheval_A_lightweight_graph-based_llm_framework_for_idea_e/index.html) — Tao Feng 외, 2025
7. [SciPaths: Forecasting Pathways to Scientific Discovery](../../docs/papers/10392_SciPaths_Forecasting_Pathways_to_Scientific_Discovery/index.html) — Eric Chamoun 외, 2026
8. [InnoEval: On Research Idea Evaluation as a Knowledge-Grounded, Multi-Perspective Reasoning Problem](../../docs/papers/9833_InnoEval_On_Research_Idea_Evaluation_as_a_Knowledge-Grounded/index.html) — Shuofei Qiao 외, 2026
9. [Spacer: Towards Engineered Scientific Inspiration](../../docs/papers/3394_Spacer_Towards_Engineered_Scientific_Inspiration/index.html) — Minhyeong Lee 외, 2025

---

## S39 · 자동 문헌 리뷰 생성

*제7부 · 과학 문헌·동료심사* · **Automated Literature Review Generation** · *서브카테고리*

`25편` `2023–2026` `가속` `2025+ 14편`

> [!abstract] 화면에 띄울 한 줄
> 서베이 자동 작성은 상용 deep research를 넘어섰지만 인용 신뢰성 비판이 따라붙는다.

**25편, 14편이 2025년 이후다. 자동 문헌 리뷰는 초록 스크리닝에서 시작해 이제 전문가 수준 서베이를 통째로 쓰는 단계에 왔다. 그와 함께 이 결과물을 믿어도 되는가라는 비판도 같은 해에 나왔다.**

출발점은 2023년 Bio-SIEVE다. 체계적 문헌고찰에서 비용이 가장 큰 초록 스크리닝을 지시어 미세조정 LLM으로 자동화해 ChatGPT를 능가했다. 2024년 STORM은 다관점 질문으로 아웃라인을 구성하는 사전 작성 단계를 열었다. 2025년에는 SurveyX가 AttributeTree 전처리와 다단계 최적화를, SurveyForge가 휴리스틱 아웃라인과 메모리 기반 검색, SurveyBench 평가를 내세워 자동 서베이의 품질 격차를 좁혔다. Select, read, and write는 전체 텍스트를 읽는 다중 에이전트로 관련연구 섹션을 쓴다.[1][4][6][8]

2026년에는 성능 주장이 상용 시스템과의 비교로 올라섰다. IRIS는 반복 계획, 병렬 섹션 작성, 최종 컴파일의 3단계를 반성적 확장과 critic 정제로 돌려, PubMed와 ArXiv만으로도 상용 deep research 시스템을 능가한다고 보고했다. SurveyMaster는 도메인별 writing skill 보정과 seed 논문 기반 계층 검색, 핵심 논문 앵커링으로 전문가 수준 합성을 목표로 하며 10개 분야 100개 과제 SciSurveyBench로 검증됐다. DiffResearch는 diffusion language model로 리뷰 전체를 병렬 정제하는 다른 길을 연다.[9]

평가 방식도 바뀌었다. 2025년 DeepResearch Bench는 22개 분야 박사 수준 과제 100개를 RACE와 FACT 두 방법으로 평가했다. 2026년 LitReview Arena는 대전식 전문가 평가로 3k개의 전문가 판단 데이터셋 LitReviewBench를 만들고 저비용 평가자 LitJudge를 학습시켰다. 정답이 없는 장문 생성은 점수표가 아니라 전문가 선호를 모으는 방식으로 평가하는 쪽으로 이동했다.[2][5]

비판은 구체적이다. 2025년 Generalization Bias in Large Language Model Summarization of Scientific Research는 10개 LLM의 요약 4,900개를 분석해 LLM이 사람보다 약 5배 더 높은 확률로 원문보다 넓은 결론을 낸다고 보였다. 임상 리뷰 생성 파일럿은 LLM이 빠르지만 참고문헌이 적고 논리 일관성과 인용 정확도가 낮다고 확인했다. Elicit 평가는 재현성, 신뢰성, 정확성을 따졌고, Dead Science Walking은 출판 편향이 검색-생성-평가 파이프라인에서 증폭될 수 있다고 이론화했다.[3][7]

국내 기관이 자동 서베이를 쓰려면 생성보다 검증 단계를 먼저 설계해야 한다. 인용 존재 여부와 주장 일치 여부를 사람이 샘플 검수하고, 결론의 범위가 원문을 넘지 않았는지 확인하는 절차가 최소선이다. 정책 보고서나 기술 동향 보고서의 초안 작성에는 IRIS나 SurveyX류 시스템이 시간을 크게 줄이지만, 최종 책임은 검수자에게 남는다.[6]

> [!tip] 정리
> 문헌 리뷰 자동화의 경쟁축은 문장 품질이 아니라 인용 정확도와 과일반화 통제다. 검증 절차가 있는 팀만 이 자동화의 이득을 가져간다.

**대표 도구·시스템** — STORM · SurveyForge · SurveyX · LitLLM · CHIME · DeepResearch Bench · IRIS · SurveyMaster/SciSurveyBench · LitReview Arena · DiffResearch · Bio-SIEVE · Elicit

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Bio-SIEVE: Exploring Instruction Tuning Large Language Models for Systematic Review Automation](../../docs/papers/159_Bio-sieve_exploring_instruction_tuning_large_language_models/index.html) — Ambrose Robinson 외, 2023 · 인용 59
2. [DeepResearch Bench: A Comprehensive Benchmark for Deep Research Agents](../../docs/papers/261_Deepresearch_bench_A_comprehensive_benchmark_for_deep_resear/index.html) — Mingxuan Du 외, 2025
3. [Generalization Bias in Large Language Model Summarization of Scientific Research](../../docs/papers/373_Generalization_Bias_in_Large_Language_Model_Summarization_of/index.html) — Uwe Peters 외, 2025.03 · 인용 4
4. [Select, read, and write: A multi-agent framework of full-text-based related work generation](../../docs/papers/742_Select_read_and_write_A_multi-agent_framework_of_full-text-b/index.html) — Xiaochuan Liu 외, 2025
5. [LitReview Arena: Evaluating Literature Review Agents with Battle-style Peer Review Platform](../../docs/papers/9953_LitReview_Arena_Evaluating_Literature_Review_Agents_with_Bat/index.html) — Ruotong Zhao 외, 2026 · 인용 210
6. [SurveyX: Academic survey automation via large language models](../../docs/papers/781_Surveyx_Academic_survey_automation_via_large_language_models/index.html) — Xun Liang 외, 2025 · 인용 2,819
7. [Using artificial intelligence for systematic review: the example of elicit](../../docs/papers/862_Using_artificial_intelligence_for_systematic_review_the_exam/index.html) — Nathan Bernard 외, 2025.03 · 인용 83
8. [Surveyforge: On the outline heuristics, memory-driven generation, and multi-dimensional evaluation for automated survey writing](../../docs/papers/780_Surveyforge_On_the_outline_heuristics_memory-driven_generati/index.html) — Xiangchao Yan 외, 2025 · 인용 7
9. [DiffResearch: Harnessing Diffusion Language Models for Automated Literature Review](../../docs/papers/9515_DiffResearch_Harnessing_Diffusion_Language_Models_for_Automa/index.html) — Alan-Barsag Gazzaev 외, 2026

---

## S40 · 다문서·메타리뷰 요약

*제7부 · 과학 문헌·동료심사* · **Multi-Document Review Summarization** · *서브카테고리*

<sub>타임라인 분석 명칭: Multi-Document & Meta-Review Summarization</sub>

`24편` `2018–2026` `안정` `2025+ 7편`

> [!abstract] 화면에 띄울 한 줄
> 요약 연구는 안정기에 들어섰고, 장문 확장과 상충 리뷰 종합으로 무게가 옮겨갔다.

**24편 중 2025년 이후는 7편뿐이다. 다문서 요약은 이 대분류에서 유일하게 STABLE로 분류되는 칸이다. 데이터셋과 모델이 이미 갖춰져 있고, 최근 연구는 장문 확장과 효율, 그리고 리뷰 종합으로 갈라졌다.**

기반은 2018–2024년에 닦였다. WikiSplit으로 문장 분할-재표현 데이터가 나왔고, 2020년 SciTLDR와 CATTS가 과학 논문 극단 요약을, 2021년 MS2가 의료 다문서 요약을 열었다. 2023년 BigSurvey와 CAST는 수천 편을 입력으로 하는 구조화 요약을 제안했고 SciReviewGen은 쿼리 중심 다문서 요약으로 문헌 리뷰 생성 문제를 정의했다. 그래프 쪽에서는 KGSum과 2024년 HAESum이 문장 내 관계와 문장 간 고차 관계를 계층적으로 모델링했다.

2025년의 변화는 규모와 효율이다. LLM × MapReduce-V2는 정보 병목 이론에 기반한 합성곱형 테스트 타임 스케일링으로 극도로 긴 입력 자원을 통합해 장문 기사를 쓰고, 추출적 방법의 한계를 넘으려 한다. Estimating optimal context length for hybrid retrieval-augmented multi-document summarization은 retriever, summarizer, 데이터셋마다 최적 context 길이가 다르다는 전제로 LLM 패널과 Minimum Bayes Risk decoding으로 이를 추정한다. 많이 넣을수록 좋다는 가정을 버린 작업이다.[2][3]

요약 파이프라인은 모듈화됐다. Ask, retrieve, summarize는 XSum이라는 이름의 RAG 기반 모듈식 파이프라인으로, 질문 생성 모듈과 편집 모듈을 두어 정확하고 인용이 풍부한 과학 문헌 요약을 만든다. PGraphRAG는 지식 그래프 기반 개인화 검색 증강으로 사용자 이력이 부족한 콜드스타트에서도 개인화를 돕는다. TreeReview는 같은 아이디어를 논문 심사에 옮겨 질문 트리를 만들고 토큰 사용을 80%까지 줄였다.[1][4]

리뷰 종합이 동료심사와 만나는 지점이다. 이 칸의 key development에는 상충하는 리뷰에서 메타리뷰를 생성하는 PEERSUM과 RAMMER, GLIMPSE, 갈등 인식형 CAF가 있다. 또 Pre는 동료평가 메커니즘을 가져와 여러 LLM을 평가자로 쓰고 자격 시험으로 신뢰할 평가자를 거른다. 요약은 단순 압축이 아니라 서로 다른 평가를 종합하는 일이 됐고, 이는 편집자 판단과 직접 연결된다. MoDeST와 Lag는 요약 기법이 제목 생성과 리더보드 자동화로 번지고 있음을 보여 준다.[5]

국내 관점에서 이 칸은 신규 개척지가 아니라 적용 영역이다. 영어 데이터셋 위에서 검증된 요약기를 한국어 과제 보고서나 심사 의견에 그대로 쓰기는 어렵다. 한국어 다문서 요약 데이터와, 메타리뷰 요약이 심사자 의견을 빠뜨리거나 왜곡하지 않는지 확인하는 평가가 선행되어야 한다.

> [!tip] 정리
> 성숙한 분야에서는 새 모델보다 평가와 현지화가 남은 일이다. 메타리뷰 요약은 심사 책임과 맞닿아 있어 검증 없이 도입하기 가장 위험한 응용이다.

**대표 도구·시스템** — SciTLDR/CATTS · MS2 · BigSurvey/CAST · KGSum · PEERSUM/RAMMER · GLIMPSE · TreeReview · LLM x MapReduce-V2 · XSum · MoDeST

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Ask, retrieve, summarize: A modular pipeline for scientific literature summarization](../../docs/papers/108_Ask_retrieve_summarize_A_modular_pipeline_for_scientific_lit/index.html) — Pierre Achkar 외, 2025 · 인용 91
2. [Estimating optimal context length for hybrid retrieval-augmented multi-document summarization](../../docs/papers/318_Estimating_optimal_context_length_for_hybrid_retrievalaugmen/index.html) — Adithya Pratapa 외, 2025
3. [LLM × MapReduce-V2: Entropy-Driven Convolutional Test-Time Scaling for Generating Long-Form Articles from Extremely Long Resources](../../docs/papers/495_Llm__mapreduce-v2_Entropy-driven_convolutional_test-time_sca/index.html) — Haoyu Wang 외, 2025
4. [TreeReview: A dynamic tree of questions framework for deep and efficient llm-based scientific peer review](../../docs/papers/843_Treereview_A_dynamic_tree_of_questions_framework_for_deep_an/index.html) — Yuan Chang 외, 2025 · 인용 2
5. [MoDeST: A dataset for Multi Domain Scientific Title Generation](../../docs/papers/10765_modest_a_dataset_for_multi_domain_scientific_title_gen/index.html) — Necva Bölücü 외, 2025.05 · 인용 1
6. [Lag: Llm agents for leaderboard auto generation on demanding](../../docs/papers/1088_Lag_Llm_agents_for_leaderboard_auto_generation_on_demanding/index.html) — Jian Wu 외, 2025

---

## S41 · 다국어 LLM 양자화·효율화

*제8부 · 멀티모달 인식·효율화* · **Multilingual Language Model Quantization** · *서브카테고리*

<sub>타임라인 분석 명칭: Multilingual Language Models, Compression & Efficiency</sub>

`46편` `2018–2026` `가속` `2025+ 24편`

<sub>멀티모달 인식·효율화 고유 배정 113편(중복 포함 434편 · 웹 인덱스 기준) · 서브카테고리 5개 · 본 파트 5개로 100% 커버</sub>

> [!quote] 파트 도입
> 작게 만들고 정확히 읽는 일이 배포의 조건이 됐다. 효율화와 도표 이해 모두 '동등성 검증'이 빠져 있다.

> [!abstract] 화면에 띄울 한 줄
> 2026 양자화는 모델 전체가 아니라 구성요소·토큰·하드웨어 단위로 쪼개 따진다.

**46편 중 24편이 2025년 이후이고, 2026년에 급증했다. 이 칸의 주제는 '다국어'라는 이름보다 넓어졌다. 이제 핵심은 모델을 얼마나 줄이느냐가 아니라, 줄인 모델을 어디에 올려 무엇으로 검증하느냐다.**

흐름의 바닥에는 2018년 BERT의 양방향 마스크 언어모델 사전학습과 2019년 XLM-R의 100개 언어 확장이 있다. 이후 Code Llama, StarCoder, Gemma 2, Qwen2.5, DeepSeek-V3의 MoE, Kimi k1.5로 이어지는 공개 효율 기반 모델 계열이 형성됐다. 2025년에는 장문맥 언어모델 서베이가 나와 문맥 확장 쪽 정리도 끝났다. 여기까지는 배경이다.[5][6]

2026년 사례의 특징은 단위가 작아졌다는 점이다. Rethinking Small VLM Quantization은 3B 이하 소형 VLM을 vision encoder, projector, LLM backbone 세 요소로 나누고 Jetson Orin NX/AGX에서 여섯 가지 양자화 조합에 대해 다섯 가지 가설을 검증했다. 통째로 4비트로 내린다는 관행 대신 구성요소마다 민감도가 다르다는 전제로 엣지 배포를 설계한다. Token-DiFR의 4비트 적대자 탐지, 양자 오류 정정 디코더에서 INT4 양자화가 핵심 요인으로 밝혀진 작업도 같은 방향이다.[2]

토큰을 줄이는 접근도 있다. Token-Sparse Medical Multimodal Reasoning via Dual-Stream Reinforcement Learning의 ViToS는 의료 VLM에서 진단에 유효한 시각 토큰이 극히 일부라는 관찰에서 출발해, grounding 기반 visual token pruning과 token-sparse reasoning을 하나의 정책이 동시에 학습하게 한다. Token-Only Adaptation의 Identity-Token Adaptation은 frozen DINOv2-base 위에서 종별 토큰 하나만 최적화해 동물 pose estimation을 파라미터-정확도 Pareto front로 특성화했다. 모델을 건드리지 않고 얹는 방식이다.[3][8]

학습 쪽 효율화도 뚜렷하다. SEAD는 on-policy distillation에서 teacher 지도의 질이 student 역량에 좌우된다는 문제를 엔트로피로 다루고, UniR은 경량 reasoning module을 학습해 추론 시 frozen LLM의 logit에 더하는 방식으로 추론 능력을 부여한다. Bidirectional Evolutionary Search는 순방향 진화 탐색과 역방향 목표 분해로 자기개선을 시도한다. 여기에 Are Non-BPE Tokenizers Ready to Improve LLM Numeracy?처럼 토크나이저가 수치 연산에 미치는 영향을 따지는 점검이 붙는다.[7]

비판적으로 볼 대목은 평가다. 효율화 기법이 성능 저하 없이 안전성·공정성까지 유지하는지에 대한 체계적 검증은 여전히 부족하다. Prediction-Powered Inference Across Many Tasks for AI Evaluation은 라벨이 극히 적을 때도 유효한 신뢰구간을 주는 틀을 제시하고, Total Variation Distance Estimation in Autoregressive Models는 서로 다른 추론 엔진 사이의 분포 차이를 추정한다. 줄인 모델이 원본과 같은지 통계로 묻는 도구가 이제 막 나오는 단계다.[1][4]

> [!tip] 정리
> 국내 관점에서 양자화 자체는 차별점이 못 된다. 줄인 모델이 원본과 같다는 것을 숫자로 증명하는 평가 체계가 공공 조달과 엣지 배포의 진입 조건이 될 것이다.

**대표 도구·시스템** — BERT · XLM-R · SimAlign · SPLADE v2 · DeepSeek-V3 · Qwen2.5 · Gemma 2 · Kimi k1.5 · SEAD · UniR · ViToS · SurpMark

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Prediction-Powered Inference Across Many Tasks for AI Evaluation](../../docs/papers/10231_Prediction-Powered_Inference_Across_Many_Tasks_for_AI_Evalua/index.html) — Nicolas Emmenegger 외, 2026
2. [Rethinking Small VLM Quantization: From Component-Wise Analysis to Hardware-Aware Edge Deployment](../../docs/papers/10335_Rethinking_Small_VLM_Quantization_From_Component-Wise_Analys/index.html) — Hyeju Shin 외, 2026
3. [Token-Sparse Medical Multimodal Reasoning via Dual-Stream Reinforcement Learning](../../docs/papers/10595_Token-Sparse_Medical_Multimodal_Reasoning_via_Dual-Stream_Re/index.html) — Kaitao Chen 외, 2026
4. [Total Variation Distance Estimation in Autoregressive Models](../../docs/papers/10604_Total_Variation_Distance_Estimation_in_Autoregressive_Models/index.html) — Eric Price 외, 2026
5. [Code llama: Open foundation models for code](../../docs/papers/230_Code_llama_Open_foundation_models_for_code/index.html) — Baptiste Rozière 외, 2023
6. [Kimi k1.5: Scaling reinforcement learning with llms](../../docs/papers/449_Kimi_k15_Scaling_reinforcement_learning_with_llms/index.html) — Kimi Team 외, 2025 · 인용 109
7. [Are Non-BPE Tokenizers Ready to Improve LLM Numeracy?](../../docs/papers/9255_Are_Non-BPE_Tokenizers_Ready_to_Improve_LLM_Numeracy/index.html) — Yizhan Huang 외, 2026
8. [Token-Only Adaptation of Frozen Self-Supervised Vision Foundation Models for Cross-Species Animal Pose: A Pareto-Frontier Characterization Across Eight Held-Out Mammal Species](../../docs/papers/10594_Token-Only_Adaptation_of_Frozen_Self-Supervised_Vision_Found/index.html) — Ethan Y Wang 외, 2026 · 인용 979
9. [Self-Improving Language Models with Bidirectional Evolutionary Search](../../docs/papers/10410_Self-Improving_Language_Models_with_Bidirectional_Evolutiona/index.html) — Guowei Xu 외, 2026
10. [A survey of large language models](../../docs/papers/026_A_survey_of_large_language_models/index.html) — Wayne Xin Zhao 외, 2026.12 · 인용 114
11. [A comprehensive survey on long context language modeling](../../docs/papers/005_A_comprehensive_survey_on_long_context_language_modeling/index.html) — Jiaheng Liu 외, 2025 · 인용 2

---

## S42 · 과학 도표 캡셔닝

*제8부 · 멀티모달 인식·효율화* · **Scientific Figure Captioning** · *서브카테고리*

<sub>타임라인 분석 명칭: Scientific Figure Captioning & Scholarly Visual Generation</sub>

`24편` `2021–2026` `가속` `2025+ 9편`

> [!abstract] 화면에 띄울 한 줄
> 캡션 생성에서 출발해 도표 읽기·그리기·논문 소통 자동화까지 번졌다.

**24편 중 9편이 2025년 이후다. 이 칸은 '그림에 설명 문장을 붙이는' 과제로 시작했지만, 2026년에는 도표에서 데이터를 되살리고 논문을 포스터와 영상으로 바꾸는 과학 소통 자동화로 확장됐다.**

출발점은 2021년 SciCap이다. 과학 도형과 캡션 쌍을 대규모로 모아 캡션 생성이라는 과제를 정의했고, 2023년 SciCap+가 멘션 문단과 OCR 토큰을 넣어 이를 지식 증강 캡셔닝 문제로 다시 틀었다. PatFig는 특허 도형으로, FigGen과 AutomaTikZ는 반대 방향인 텍스트에서 도형을 만드는 쪽으로 영역을 넓혔다. 모두 2025년 이전이므로 배경으로만 둔다.

2026년의 큰 변화는 데이터 품질이다. S1-MMAlign은 과학 논문 250만 편에서 수집한 1,550만 개의 이미지-텍스트 쌍을 구성하고, 원본 캡션이 희소하다는 약점을 Qwen-VL 기반 의미 강화 파이프라인으로 초록과 인용 맥락을 결합해 보강했다. MMClima는 한 걸음 더 나아가 텍스트, 비디오 전사본, 과학적 figure를 묶은 104k개 이상의 전문가 검증 QA 쌍으로 기후과학 평가 틀을 만들었다. 자동 claim 추출과 QA 합성에 사람의 검증을 결합했다는 점이 핵심이다.[2][4]

가장 날카로운 결과는 MatDeplot이다. 재료과학 논문에 흔한 line plot에 대해 VLM이 정성적 인식은 하지만 pixel-level grounding에는 사실상 실패한다는 것을 대규모로 정량화했고, 이를 축 보정된 곡선으로 복원하는 로컬 파이프라인을 제시했다. MatViX가 보여 준 재료과학 논문의 구조화 정보 추출 과제와 이어지는 지점이다. 캡션을 잘 쓰는 것과 그림에서 숫자를 읽어 내는 것은 다른 능력이라는 반증이다.[5]

생성·소통 쪽에서는 에이전트가 전면에 나온다. PaperBanana는 자율 AI 과학자의 시각화 병목을 풀기 위해 VLM과 이미지 생성 모델로 출판 수준의 다이어그램과 플롯을 만든다. Paper2poster는 논문을 한 페이지 포스터로 바꾸는 벤치마크와 PosterAgent를 내놨고, SciTalk는 논문을 짧은 영상으로 변환하는 멀티 LLM 프레임워크다. 다만 TikZero가 보이듯 캡션 정렬 데이터 없이 그래픽 프로그램을 합성하려는 시도는 아직 데이터 병목 위에 서 있다.[1][3]

그래서 이 칸은 두 갈래로 갈린다. 읽기 쪽은 곡선 복원, 구조화 추출, 근거 있는 캡션이 연구 무결성과 직결된다. 쓰기 쪽은 도식·포스터·영상 자동화가 연구자 시간을 줄이는 대신 AI 생성 그림의 정확성을 누가 책임지느냐를 남긴다. 두 갈래 모두 평가 데이터가 전문가 검증에 의존한다는 공통점이 있다.

> [!tip] 정리
> 작지 않은 칸이다. 도표에서 증거를 되살리는 기술은 문헌 검증과 재료·기후 데이터화의 하부 설비다. 국내 도메인 논문으로 전문가 검증 평가셋을 만드는 일이 선점 지점이다.

**대표 도구·시스템** — SciCap · SciCap+ · FigCaps-HF · AutomaTikZ/CLiMA · FigGen · MMSCI · SciFIBench · MatViX · PosterAgent · SciTalk · PaperBanana · S1-MMAlign

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Paper2poster: Towards multimodal poster automation from scientific papers](../../docs/papers/599_Paper2poster_Towards_multimodal_poster_automation_from_scien/index.html) — Wei Pang 외, 2025 · 인용 2
2. [S1-MMAlign: A Large-Scale, Multi-Disciplinary Dataset for Scientific Figure-Text Understanding](../../docs/papers/691_S1-MMAlign_A_Large-Scale_Multi-Disciplinary_Dataset_for_Scie/index.html) — He Wang 외, 2026.01
3. [PaperBanana: Automating Academic Illustration for AI Scientists](../../docs/papers/601_PaperBanana_Automating_Academic_Illustration_for_AI_Scientis/index.html) — Dawei Zhu 외, 2026.01 · 인용 1
4. [MMClima: A Framework for Multimodal Climate Science Data and Evaluation](../../docs/papers/10042_MMClima_A_Framework_for_Multimodal_Climate_Science_Data_and/index.html) — Muhammad Umer Sheikh 외, 2026
5. [MatDeplot: Agent-Ready Materials-Curve Understanding for Scientific Reasoning](../../docs/papers/9992_MatDeplot_Agent-Ready_Materials-Curve_Understanding_for_Scie/index.html) — Yin Liang 외, 2026
6. [Understanding how paper writers use ai-generated captions in figure caption writing](../../docs/papers/853_Understanding_how_paper_writers_use_ai-generated_captions_in/index.html) — Ho Yin (Sam) Ng 외, 2025 · 인용 6

---

## S43 · AutoML 도메인 전이

*제8부 · 멀티모달 인식·효율화* · **Cross-Domain Transferability in AutoML** · *서브카테고리*

<sub>타임라인 분석 명칭: Cross-Domain Transferability, Retrieval & AutoML</sub>

`16편` `2020–2026` `안정` `2025+ 7편`

> [!abstract] 화면에 띄울 한 줄
> 2026 전이 논의는 RAG·AutoML에서 도메인 비전 벤치마크의 맹점 진단으로 옮겨 갔다.

**16편 중 7편이 2025년 이후다. 칸 이름은 AutoML이지만 내용은 검색 증강, 도메인 적응, 해석 가능성 리뷰가 섞여 있고, 2026년에 이르러서야 도메인별 멀티모달 벤치마크라는 구체적 모양이 생겼다. 규모는 작다.**

뼈대는 2020년 전후에 세워졌다. REALM은 지식을 파라미터가 아니라 학습 가능한 검색 모듈로 끌어오는 사전학습을 제안했고, RAG는 BART와 위키피디아 DPR 검색기를 결합해 지식 집약 과업을 풀었다. Don't Stop Pretraining은 도메인·과업 적응 사전학습이 일관된 이득을 준다고 보였다. 2023년의 AutoML-GPT와 AutoML in the age of LLMs는 LLM을 AutoML 컨트롤러로 쓰는 구상을 폈다. 배경으로만 쓴다.[2][3][9]

2025년 사례로는 GeoFactory가 있다. RAG, 프롬프트 엔지니어링, 미세조정, 에이전트의 네 방법과 열네 개 세부 알고리즘을 지구과학의 사실 과업과 추론 과업에서 실증 평가하고, 이들을 앙상블한 통합 프레임워크를 제안했다. 어느 한 기법이 아니라 조합이 답이라는 결론이다. 같은 해 인간 기억 체계와 비교한 AI 메모리 서베이도 파라미터·비파라미터 구분으로 전이 논의를 정리했다.[6]

2026년의 의미 있는 변화는 비판적 진단이다. LabProc and Tacit은 자율 실험실의 인식 계층으로 쓰이는 frontier VLM이 motion-only 상태 구분에서 구조적 맹점을 가진다는 것을 여섯 과제로 정량화했고, 300M 파라미터의 도메인 적응 video encoder인 Tacit으로 대응했다. IVQA-LD는 사지 결손 인구를 위한 최초의 대규모 전문가 주석 vision-language 데이터셋이며, VLM이 이 도메인에서 심각하게 취약함을 보인 뒤 신체 구조 인식을 반영한 방법을 제안한다. 범용 모델이 도메인으로 그대로 전이되지 않는다는 증거다.[5][7]

VT-Bench는 시각 입력과 표 형식 데이터를 함께 쓰는 학습을 판별과 생성 두 패러다임에서 한꺼번에 평가하는 최초의 통합 벤치마크로, 아홉 개 도메인을 다룬다. Coupled Training with Privileged Information and Unlabeled Data는 학습 때만 존재하는 부가 특징과 비라벨 데이터를 활용해 배포 모델을 함께 학습한다. 전이를 모델 구조가 아니라 데이터 조건의 문제로 바라보는 시각이 이 둘에 공통이다.[1][4]

> [!tip] 정리
> 이 칸은 작지만 쓰임이 분명하다. 자율 실험실, 의료 보조, 지구과학처럼 범용 VLM이 놓치는 현장에서 어떤 맹점이 있는지 재는 벤치마크가 곧 도입 판단 근거가 된다.

**대표 도구·시스템** — REALM · RAG · Atlas · AutoML-GPT · GeoFactory · VT-Bench · Tacit · IVQA-LD

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [VT-Bench: A Unified Benchmark for Visual-Tabular Multi-Modal Learning](../../docs/papers/10685_VT-Bench_A_Unified_Benchmark_for_Visual-Tabular_Multi-Modal/index.html) — Ziyi Jia 외, 2026
2. [AutoML-GPT: Automatic Machine Learning with GPT](../../docs/papers/136_Automl-gpt_Automatic_machine_learning_with_gpt/index.html) — Shujian Zhang 외, 2023
3. [Don't Stop Pretraining: Adapt Language Models to Domains and Tasks](../../docs/papers/287_Dont_Stop_Pretraining_Adapt_Language_Models_to_Domains_and_T/index.html) — Suchin Gururangan 외, 2020 · 인용 2,067
4. [Coupled Training with Privileged Information and Unlabeled Data](../../docs/papers/9454_Coupled_Training_with_Privileged_Information_and_Unlabeled_D/index.html) — Jiahao Shi 외, 2026
5. [LabProc and Tacit: Quantifying the Visual-Textual Prior Gap in Autonomous Laboratory Perception](../../docs/papers/9870_LabProc_and_Tacit_Quantifying_the_Visual-Textual_Prior_Gap_i/index.html) — Jagrati Gogia 외, 2026
6. [GeoFactory: an LLM performance enhancement framework for geoscience factual and inferential tasks](../../docs/papers/10764_geofactory_an_llm_performance_enhancement_framework_fo/index.html) — Zhou Chen 외, 2025.05 · 인용 6
7. [IVQA-LD: Inclusive Multimodal Understanding for Population with Limb Deficiency](../../docs/papers/9853_IVQA-LD_Inclusive_Multimodal_Understanding_for_Population_wi/index.html) — Yan Ke 외, 2026
8. [Generative AI and the Foundation Model Era: A Comprehensive Review](../../docs/papers/377_Generative_AI_and_the_Foundation_Model_Era_A_Comprehensive_R/index.html) — Abdussalam Elhanashi 외, 2026.03 · 인용 6
9. [From Human Memory to AI Memory: A Survey on Memory Mechanisms in the Era of LLMs](../../docs/papers/355_From_Human_Memory_to_AI_Memory_A_Survey_on_Memory_Mechanisms/index.html) — Yaxiong Wu 외, 2025 · 인용 2

---

## S44 · 차트 추론·팩트체크

*제8부 · 멀티모달 인식·효율화* · **Chart Reasoning & Fact-Checking** · *서브카테고리*

<sub>타임라인 분석 명칭: Chart Reasoning, Instruction Tuning & Fact-Checking</sub>

`14편` `2023–2026` `가속` `2025+ 6편`

> [!abstract] 화면에 띄울 한 줄
> 2025–2026 차트 추론은 지시 튜닝 물결을 지나 반성·에이전트·RL 일반화 검증으로 이동했다.

**14편 중 6편이 2025년 이후다. 2023년 차트 이미지 기반 팩트체킹으로 시작해, 2024년에 지시 튜닝 모델이 쏟아졌고, 2025–2026년에는 모델이 어떻게 추론하고 왜 일반화하는지를 따지는 단계로 접어들었다.**

배경부터 보면, 2023년 ChartBERT가 차트 이미지를 증거로 텍스트 주장의 진위를 판정하는 과제를 처음 정의했다. 같은 해 ChartLlama를 시작으로 ChartAssistant, MMC, ChartInstruct, ChartGemma, ChartX와 ChartVLM, SynChart까지 2024년에 차트 지시 튜닝 물결이 이어졌다. MMC는 600k 인스턴스, ChartInstruct는 191K 지시문과 71K 차트, SynChart는 약 400만 개의 합성 차트를 내세웠다. 데이터 규모 경쟁의 시대였다.

2025년에는 추론 방식이 바뀌었다. ChartSketcher는 인간의 인지 행동에서 착안해 모델이 중간 추론 단계를 차트 위에 직접 주석으로 그리고 이를 다시 입력으로 받는 Sketch-CoT를 도입했다. Multimodal deepresearcher는 시각화를 구조화 텍스트 표현인 FDV로 바꿔 텍스트와 차트가 얽힌 보고서를 처음부터 생성한다. Chartist는 분석 과업에 따라 달라지는 사람의 시선 이동 scanpath를 예측해 차트 읽기의 인지 모델을 제시했다.[1][5][6]

학습 방식에 대한 반성도 같은 시기에 나왔다. SFT Memorizes, RL Generalizes는 사후학습에서 RL이 규칙 기반 추론과 시각 과업에서 더 잘 일반화하는 반면 SFT는 훈련 분포를 암기하는 경향이 있음을 비교했다. 차트 지시 튜닝 물결이 사실상 SFT 위에 선 것이었다는 점을 떠올리면 불편한 결과다. 데이터를 늘려 얻은 성능이 어디까지 일반화인지 다시 물어야 한다는 뜻이다.[2]

2026년에는 부정적 결과가 눈에 띈다. Diversity Over Frequency는 visual chain-of-thought 에이전트의 RL 훈련에서 도구 사용 빈도가 줄어드는데도 정확도가 오르는 tool-use collapse를 규명하고, 이를 rollout 다양성 부족으로 재해석해 엔트로피 정규화로 대응했다. Can Vision Language Models Learn Intuitive Physics from Interaction?은 상호작용 RL로 학습해도 SFT처럼 일반화되는 직관 물리를 얻지 못한다고 보고했다. 이 칸은 좋은 소식만 쌓이는 곳이 아니다.[3][4]

팩트체킹 쪽 연결고리는 약하지만 분명하다. ChartBERT의 증거 기반 검증 과제는 2023년 이후 이 칸에서 후속이 적고, 오히려 인접한 멀티모달 환각 검증에서 DEFAME와 Pelican이 같은 문제의식을 이어 갔다. 차트 팩트체크는 아직 독립 벤치마크 수준이 아니라 응용 방향으로 남아 있다.

> [!tip] 정리
> 차트는 보고서와 논문의 주장이 숫자로 압축된 곳이라, 읽기와 검증을 자동화하는 가치는 크다. 다만 일반화 한계가 드러난 만큼 국내 자료 위에서 직접 평가하지 않으면 도입 판단이 어렵다.

**대표 도구·시스템** — ChartBERT · ChartLlama · ChartAssistant · ChartGemma · ChartVLM · SynChart · ChartSketcher · Chartist · Multimodal DeepResearcher

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Multimodal deepresearcher: Generating text-chart interleaved reports from scratch with agentic framework](../../docs/papers/566_Multimodal_deepresearcher_Generating_text-chart_interleaved/index.html) — Zhaorui Yang 외, 2025 · 인용 3
2. [SFT Memorizes, RL Generalizes: A Comparative Study of Foundation Model Post-training](../../docs/papers/751_SFT_Memorizes_RL_Generalizes_A_Comparative_Study_of_Foundati/index.html) — Tianzhe Chu 외, 2025 · 인용 6
3. [Can Vision Language Models Learn Intuitive Physics from Interaction?](../../docs/papers/9373_Can_Vision_Language_Models_Learn_Intuitive_Physics_from_Inte/index.html) — Luca M. Schulze Buschoff 외, 2026
4. [Diversity Over Frequency: Rethinking Tool Use in Visual Chain-of-Thought Agents](../../docs/papers/9531_Diversity_Over_Frequency_Rethinking_Tool_Use_in_Visual_Chain/index.html) — Dong-Hee Kim 외, 2026
5. [Chartist: Task-driven Eye Movement Control for Chart Reading](../../docs/papers/200_Chartist_Task-driven_Eye_Movement_Control_for_Chart_Reading/index.html) — Danqing Shi 외, 2025 · 인용 13
6. [ChartSketcher: Reasoning with multimodal feedback and reflection for chart understanding](../../docs/papers/203_Chartsketcher_Reasoning_with_multimodal_feedback_and_reflect/index.html) — Muye Huang 외, 2025

---

## S45 · 도시 장면 이해

*제8부 · 멀티모달 인식·효율화* · **Cross-View Urban Scene Understanding** · *서브카테고리*

<sub>타임라인 분석 명칭: Cross-View, Spatial & Video Scene Understanding</sub>

`13편` `2023–2026` `부상` `2025+ 10편`

> [!abstract] 화면에 띄울 한 줄
> 2026 위성·거리뷰 융합 모델과 시공간 벤치마크가 한꺼번에 나오며 칸이 열렸다.

**13편 중 10편이 2025년 이후로, 이 대분류에서 가장 젊은 칸이다. 규모는 작고 상태는 신생(EMERGING)이다. 도시 장면을 위성, 거리뷰, 지도, 관심지점(POI)이라는 서로 다른 시점으로 함께 이해하려는 시도가 2026년에 한꺼번에 나왔다.**

배경은 네이티브 멀티모달 기반 모델이다. 2023년 Gemini가 이미지·오디오·비디오·텍스트를 처음부터 함께 다루는 모델 패밀리를 내놨고, 2024년 Gemini 1.5는 최대 1,000만 토큰의 컨텍스트로 긴 문서·영상·오디오를 처리했다. 도시 규모의 영상 데이터를 한 번에 넣을 수 있다는 가능성이 이 칸의 전제다. 다만 이 두 논문은 이 칸의 직접 주제라기보다 기반이다.[1]

2026년 핵심은 시점 융합이다. UrbanMLLM은 위성 영상과 거리뷰를 하나로 학습하기 위해 cross-view perceiver 모듈과 structural interleaved pre-training 패러다임을 도입했고, 13개 도시 이해 태스크에서 성능 향상을 보였다. UrbanFusion은 거리뷰, 원격탐사, 지도, POI를 Stochastic Multimodal Fusion이라는 대조학습 틀로 묶어 모달리티가 일부만 있어도 강건한 공간 표현을 얻는다. 현실에서는 모든 시점의 데이터가 갖춰지지 않으니 후자의 설계가 실용적이다.

평가는 약점을 드러낸다. TimeSpot은 지상 이미지만으로 계절·월·시각 같은 시간 속성과 대륙·국가·기후대·위경도 같은 지리 속성을 구조화된 형태로 함께 맞히게 하는 벤치마크이며, 최신 VLM이 특히 시간 추론에서 심각하게 저조하다고 실증했다. FrontierSpatial은 23개 기존 데이터셋을 통합해 7,838개 질문과 11,825개 이미지를 4단계 계층으로 정리한 최초의 통합 공간 추론 벤치마크다. 모델이 공간을 본다는 인상과 실제 능력의 간극을 재는 도구다.[6]

인접 주제로 환각 검증이 함께 묶여 있다. Pelican은 주장을 1차 술어로 분해하고 파이썬 코드로 검증해 LVLM의 환각을 보정하며, DEFAME는 텍스트와 이미지가 섞인 주장을 6단계 동적 파이프라인으로 검증하는 멀티모달 팩트체킹 시스템이다. How do Humans Process AI-generated Hallucination Contents는 EEG로 사람이 환각 콘텐츠를 처리하는 신경 동역학을 다뤘다. SciVideoBench는 25개 이상의 분야에서 수집한 연구 수준 실험 영상으로 1,000개 문항을 구성했다.[2][3][5]

> [!tip] 정리
> 도시 이해는 쓰임이 가장 분명한 응용 칸이다. 다만 시간 추론이 약하다는 진단이 이미 나온 만큼, 도시 변화 모니터링에 쓰려면 국내 데이터로 시간 축 평가부터 해야 한다.

**대표 도구·시스템** — Gemini · Gemini 1.5 · Pelican · DEFAME · UrbanFusion · UrbanMLLM · TimeSpot · FrontierSpatial · SciVideoBench · TikZero

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Gemini 1.5: Unlocking multimodal understanding across millions of tokens of context](../../docs/papers/368_Gemini_15_Unlocking_multimodal_understanding_across_millions/index.html) — Machel Reid 외, 2024 · 인용 296
2. [How do Humans Process AI-generated Hallucination Contents: a Neuroimaging Study](../../docs/papers/9790_How_do_Humans_Process_AI-generated_Hallucination_Contents_a/index.html) — Shuqi Zhu 외, 2026
3. [DEFAME: Dynamic Evidence-based Fact-checking with Multimodal Experts](../../docs/papers/267_Defame_Dynamic_evidencebased_fact-checking_with_multimodal_e/index.html) — Tobias Braun 외, 2025
4. [Visual thoughts: A unified perspective of understanding multimodal chain-of-thought](../../docs/papers/869_Visual_thoughts_A_unified_perspective_of_understanding_multi/index.html) — Zihui Cheng 외, 2025
5. [SciVideoBench: Benchmarking Scientific Video Reasoning in Large Multimodal Models](../../docs/papers/10395_SciVideoBench_Benchmarking_Scientific_Video_Reasoning_in_Lar/index.html) — Andong Deng 외, 2026
6. [TimeSpot: Benchmarking Geo-Temporal Understanding in Vision–Language Models in Real-World Settings](../../docs/papers/10589_TimeSpot_Benchmarking_Geo-Temporal_Understanding_in_VisionLa/index.html) — Azmine Toushik Wasi 외, 2026

---

## S46 · 인과 독립성 검정

*제9부 · 인과·통계 추론* · **Causal Independence Testing** · *서브카테고리*

`53편` `2026–2026` `가속` `2025+ 53편`

<sub>인과·통계 추론 고유 배정 108편(중복 포함 590편 · 웹 인덱스 기준) · 서브카테고리 4개 · 본 파트 4개로 100% 커버</sub>

> [!quote] 파트 도입
> AI 결과를 검정·신뢰구간으로 인증하는 일이 다른 대분류를 떠받치는 인프라가 됐다. 리더보드 1위조차 동전 던지기일 수 있다는 반증이 함께 나왔다.

> [!abstract] 화면에 띄울 한 줄
> 2026 검정은 사후 감사가 아니라 배포 중 상시 보증으로 이동했다.

**53편, 전부 2026년 논문이다. 인과·통계 추론 대분류의 절반 가까이가 여기 있고, 이 칸의 공통 주제는 AI의 출력과 AI가 쓰는 데이터를 통계적으로 인증하는 일이다.**

가장 눈에 띄는 변화는 비용 문제의 해소다. Minimax-Optimal Kernel Two-sample Testing in Sub-quadratic Time은 MMD 기반 두 표본 검정을 O(N^2 d) 대신 O((2 log N)^d N) 시간에 계산하면서 minimax 검정력을 유지한다. Fenwick tree 기반 prefix-sum과 사다리꼴 적분을 쓴 점이 핵심이다. 대규모 데이터에서 분포 비교가 계산상 불가능하다는 변명이 사라졌다는 뜻이다.[2]

조건부 독립성 검정은 모델에 구애받지 않는 방향으로 간다. Semi-knockoffs는 사전학습된 임의의 ML 모델을 그대로 쓰면서 train-test 분할 없이 유한 표본에서 유효한 p-value와 FDR 통제를 준다. Knockoff-C2ST는 classifier two-sample test의 feature attribution에 Model-X knockoff를 붙여, 상관된 covariate 아래에서도 어느 좌표가 실제로 shift 됐는지를 FDR 통제하에 가린다. 분포 이동을 감지하는 데서 원인 변수를 지목하는 데로 한 걸음 나아갔다.[7][8]

인과 발견 쪽은 가정을 줄이는 방향이다. Multi-View Causal Discovery without Non-Gaussianity는 여러 view의 이차 통계량만으로 선형 SEM을 식별 가능하게 만드는 LiMVAM을 내놨다. One Intervention per Component is Enough는 정상상태 관측과 개입만으로 Ornstein–Uhlenbeck 과정의 파라미터를 복원하며, drift graph의 강연결 성분당 개입 하나면 전역 스케일링을 제외하고 식별된다고 증명했다. Robust Causal Discovery in Real-World Time Series with Power-Laws도 실세계 시계열의 스펙트럼 특성을 활용한다. 실험 한 번이 비싼 현장에서 필요한 개입 수를 줄여 주는 결과다.[3][4][6]

배포 후 감시와 감사가 같은 도구 상자에서 나왔다. Optimal Guarantees for Auditing Rényi Differentially Private Machine Learning은 Donsker–Varadhan 변분 추정량으로 RDP 주장을 블랙박스로 감사한다. Membership Circuits는 단일 bottom-up 추론 한 번으로 정확한 다변량 p-value를 내며 FPR에 형식적 보장을 준다. Prediction-Powered Active Testing과 Prediction-Powered Adaptive Inference는 저비용 예측기를 control variate로 써서 편향 없이 분산을 줄인다. 비판할 지점도 있다. 이 칸에는 식품 점검 기록 클러스터링 같은 검정과 거리가 먼 논문도 섞여 있어, 분류가 넓게 걸쳐 있다는 점은 감안해야 한다.[1][5]

국내 관점에서 이 칸은 규제가 요구하게 될 기술이다. 모델이 어떤 분포에서 벗어났는지, 프라이버시 주장이 실제로 성립하는지를 유한 표본 보증으로 말할 수 있어야 한다. 통계 보증이 없는 AI 성능 보고는 앞으로 신뢰받기 어렵다. 이 도구들은 대부분 오픈된 이론이므로, 차별화는 알고리즘이 아니라 자사 데이터와 배포 파이프라인에 적용하는 속도에서 난다.

> [!tip] 정리
> 검정 이론은 이제 AI 개발의 하류가 아니라 상류에 놓인다. 보증을 말할 수 있는 조직과 말할 수 없는 조직의 격차가 이 칸에서 벌어진다.

**대표 도구·시스템** — MMD/HSIC · Semi-knockoffs · Knockoff-C2ST · WATCH (weighted conformal test martingales) · DP-SPRT · PLaCy · ReTimeCausal · CaDRe · λ-PSD · Membership Circuits · Anytime Tracking CUSUM

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Membership Circuits: Tractable Membership Testing via Probabilistic Circuits](../../docs/papers/10021_Membership_Circuits_Tractable_Membership_Testing_via_Probabi/index.html) — Bennet Wittelsbach 외, 2026
2. [Minimax-Optimal Kernel Two-sample Testing in Sub-quadratic Time](../../docs/papers/10034_Minimax-Optimal_Kernel_Two-sample_Testing_in_Sub-quadratic_T/index.html) — Ikjun Choi 외, 2026
3. [Multi-View Causal Discovery without Non-Gaussianity: Identifiability and Algorithms](../../docs/papers/10071_Multi-View_Causal_Discovery_without_Non-Gaussianity_Identifi/index.html) — Ambroise Heurtebise 외, 2026
4. [One Intervention per Component is Enough: Towards Identifiability in Linear Stochastic Dynamics from Steady State](../../docs/papers/10125_One_Intervention_per_Component_is_Enough_Towards_Identifiabi/index.html) — Saber Salehkaleybar, 2026
5. [Optimal Guarantees for Auditing Rényi Differentially Private Machine Learning](../../docs/papers/10138_Optimal_Guarantees_for_Auditing_Rényi_Differentially_Private/index.html) — Benjamin D. Kim 외, 2026
6. [Robust Causal Discovery in Real-World Time Series with Power-Laws](../../docs/papers/10349_Robust_Causal_Discovery_in_Real-World_Time_Series_with_Power/index.html) — Matteo Tusoni 외, 2026
7. [Semi-knockoffs: a model-agnostic conditional independence testing method with finite-sample guarantees](../../docs/papers/10416_Semi-knockoffs_a_model-agnostic_conditional_independence_tes/index.html) — Angel David REYERO LOBO 외, 2026
8. [Knockoff-C2ST: False Discovery Controlled Attribution of Distribution Shift](../../docs/papers/9863_Knockoff-C2ST_False_Discovery_Controlled_Attribution_of_Dist/index.html) — Şuayp Talha Kocabay 외, 2026 · 인용 113

---

## S47 · 관찰 데이터 처치 정책

*제9부 · 인과·통계 추론* · **Observational Treatment Policy Evaluation** · *서브카테고리*

`23편` `2025–2026` `가속` `2025+ 23편`

> [!abstract] 화면에 띄울 한 줄
> 2025–2026 관찰 데이터의 처치 정책 학습은 효과 추정에서 위험 통제로 넘어갔다.

**23편 중 23편이 2025년 이후다. 관찰 데이터로 처치 정책을 평가하고 학습하는 이 칸은 효과를 추정하는 단계를 지나 효과가 틀렸을 때의 손실을 통제하는 단계로 들어섰다.**

방법론의 중심은 시간에 따라 변하는 처치다. DeepBlip은 structural nested mean models의 g-estimation을 신경망으로 구현해 시간에 따른 조건부 평균 처치 효과를 blip effect로 추정한다. Smooth Multi-Policy Causal Effect Estimation in Longitudinal Settings는 정책마다 ICE Q-function을 따로 추정하던 관행이 이차 편향을 통제하지 못한다는 점을 겨냥해 여러 동적 정책을 동시에 평가한다. Gradient-Based Causal Tree Ensembles의 GRACE는 미분 가능한 causal tree를 신경망 층 자리에 넣는다. 이질적 처치 효과 추정이 딥러닝 부품이 됐다는 신호다.[5][10][11]

교란 처리도 확장됐다. Spatial Deconfounder는 공간 데이터에서 처치 간 간섭과 관측되지 않은 공간적 교란이 서로 연결돼 있다는 통찰에서 출발해, 이웃 처치 벡터를 multi-cause 신호로 써서 잠재 교란변수를 복원한다. Active Policy Optimization for Individualized Dosing via Gradient Variance Minimization은 최적 용량에서의 사후 gradient 분산이 정책 최적화 regret의 상한이 됨을 보여 개인별 용량 탐색의 근거를 준다.[6][9]

정책 학습은 안전장치와 같이 간다. Target-Driven Policy Optimization for Sequential Counterfactual Outcome Control의 GIFT는 오프라인 관찰 데이터로 목표 지향 순차 개입 정책을 배운다. Reinforcement Learning for Adaptive Tacrolimus Dosing with Drug-Drug Interaction은 CYP3A4 약물상호작용을 포함한 POMDP를 LSTM-PPO로 푼다. Act or Defer는 EHR foundation model의 예측에 클래스별 FDR 통제를 걸어 즉시 조치할 대상을 고르고 나머지는 보류한다. Missingness-Aware Conformal Prediction Under Cross-Hospital Distribution Shift는 병원 간 결측 패턴 차이가 교환가능성을 깨면 표준 split conformal이 하위 집단의 coverage gap을 숨긴다는 점을 보였다.[1][3][7][8]

비판적 신호는 두 가지다. 하나는 분포 변화다. Safety Generalization Under Distribution Shift in Safe Reinforcement Learning은 당뇨병 관리를 시험대로 삼아, 학습 때 만족한 안전 제약이 배포 때도 유지되는지를 별도 검증 대상으로 올렸다. 다른 하나는 제도다. Optimizing Social Utility in Sequential Experiments는 개발자와 규제기관의 principal-agent 게임으로 순차 임상시험을 모델링한다. 한편 TwinWeaver는 93,054명, 20개 암종 데이터로 Genie Digital Twin을 구축해 규모를 키웠지만, 규모가 인과적 타당성을 보장하지는 않는다.[2][4]

국내 관점에서 이 칸의 쟁점은 알고리즘이 아니라 데이터 접근과 승인 체계다. 병원 간 이식 시 coverage 보증이 무너진다는 결과는, 한 기관 데이터로 만든 임상 AI가 다른 기관에서 같은 성능을 낸다고 말할 수 없음을 뜻한다. 다기관 검증 설계와 분포 변화 감사를 처음부터 요건으로 넣은 팀만이 규제 심사를 통과할 것이다.

> [!tip] 정리
> 관찰 데이터는 싸고 많지만 틀릴 때 대가가 크다. 이 칸의 진전은 정책을 잘 배우는 법이 아니라 틀렸을 때 얼마나 틀렸는지 말하는 법에 있다.

**대표 도구·시스템** — DeepBlip · GRACE · Spatial Deconfounder · GIFT · GVALID · LSTM-PPO dosing · NOF1-BCD · TwinWeaver/Genie Digital Twin · Mondrian conformal calibration · IGRL

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Missingness-Aware Conformal Prediction Under Cross-Hospital Distribution Shift](../../docs/papers/10036_Missingness-Aware_Conformal_Prediction_Under_Cross-Hospital/index.html) — Liang You 외, 2026
2. [Optimizing Social Utility in Sequential Experiments](../../docs/papers/10142_Optimizing_Social_Utility_in_Sequential_Experiments/index.html) — Ander Artola Velasco 외, 2026
3. [Reinforcement Learning for Adaptive Tacrolimus Dosing with Drug-Drug Interaction Management](../../docs/papers/10318_Reinforcement_Learning_for_Adaptive_Tacrolimus_Dosing_with_D/index.html) — Apoorva Srinivasan 외, 2026 · 인용 1,282
4. [Safety Generalization Under Distribution Shift in Safe Reinforcement Learning: A Diabetes Testbed](../../docs/papers/10362_Safety_Generalization_Under_Distribution_Shift_in_Safe_Reinf/index.html) — Minjae Kwon 외, 2026
5. [Smooth Multi-Policy Causal Effect Estimation in Longitudinal Settings](../../docs/papers/10460_Smooth_Multi-Policy_Causal_Effect_Estimation_in_Longitudinal/index.html) — Wenxin Chen 외, 2026
6. [Spatial Deconfounder: Interference-Aware Deconfounding for Spatial Causal Inference](../../docs/papers/10475_Spatial_Deconfounder_Interference-Aware_Deconfounding_for_Sp/index.html) — Ayush Khot 외, 2026
7. [Target-Driven Policy Optimization for Sequential Counterfactual Outcome Control](../../docs/papers/10541_Target-Driven_Policy_Optimization_for_Sequential_Counterfact/index.html) — Xin Wang 외, 2026
8. [Act or Defer: Error-Controlled Decision Policies for EHR Foundation Models](../../docs/papers/9176_Act_or_Defer_Error-Controlled_Decision_Policies_for_EHR_Foun/index.html) — Intae Moon 외, 2026
9. [Active Policy Optimization for Individualized Dosing via Gradient Variance Minimization](../../docs/papers/9179_Active_Policy_Optimization_for_Individualized_Dosing_via_Gra/index.html) — Yi Wan 외, 2026
10. [Gradient-Based Causal Tree Ensembles: A Backbone Architecture for Heterogeneous Treatment Effects](../../docs/papers/9753_Gradient-Based_Causal_Tree_Ensembles_A_Backbone_Architecture/index.html) — Yusuke Kano 외, 2026
11. [DeepBlip: Estimating Conditional Average Treatment Effects Over Time](../../docs/papers/9495_DeepBlip_Estimating_Conditional_Average_Treatment_Effects_Ov/index.html) — Haorui Ma 외, 2026
12. [Learning Clinical-Trial Strategy: Offline Policy Training for Decision Agents](../../docs/papers/9900_Learning_Clinical-Trial_Strategy_Offline_Policy_Training_for/index.html) — William James Bolton 외, 2026

---

## S48 · 통계 검정·리더보드

*제9부 · 인과·통계 추론* · **Statistical Testing & Leaderboard Rankings** · *서브카테고리*

`16편` `2024–2026` `부상` `2025+ 14편`

> [!abstract] 화면에 띄울 한 줄
> 2025–2026 리더보드 1위는 신뢰구간 없이는 의미가 없다는 반증이 쌓였다.

**16편, 상태는 EMERGING이다. 이 칸은 LLM 평가를 통계 문제로 되돌려 놓는다. 리더보드의 숫자를 어디까지 믿을 수 있는지가 질문이고, 답은 생각보다 박하다.**

가장 직설적인 반증은 The Leaderboard Lottery다. N개 모델의 점추정 기반 1위 선정은 post-selection inference 문제이며, 주변 신뢰구간으로는 1위가 정말 최고인지를 답할 수 없다는 지적이다. Quantifying Ranking Uncertainty in LLM Benchmarks는 MMLU 같은 다과제 벤치마크에서 쌍별 가설검정 기반 rank confidence interval을 적용하고, 과목별 변동을 반영한다. 두 논문이 가리키는 결론은 같다. 상위권 순위는 검정을 거치기 전까지 서열이 아니다.[1][4]

진단 도구도 나왔다. Resolution Diagnostics for Paired LLM Evaluation은 쌍체 비교를 가설검정으로 재정의하고, 요구 표본 크기 N*와 관측 표본의 비율인 resolution ratio q를 지표로 내놨다. Confidence in Large Language Model Evaluation은 사전지식을 넣은 베이지안 추론으로 제한 표본에서 순위를 확률적으로 추정한다. 표본이 적은 평가에서 어디까지 결론을 낼 수 있는지를 수치로 말하는 도구들이다.[2][5]

재현성 검증의 사례도 눈에 띈다. Sticks and Stones는 EmotionPrompt가 주장한 8–115%의 정서적 프롬프트 효과가 28,000 trial 규모의 사전등록 within-subjects 설계에서 재현되지 않고, 긍정과 부정 프레이밍이 정확도상 구별되지 않음을 보였다. Behavior Is Not Representation은 steering이 행동상 성공해도 개념 특이적 표상을 바꾸지 못할 수 있다고 가설검정 프로토콜 SST로 짚었다. 행동 지표만으로 효과를 주장하는 관행이 줄줄이 흔들린다.[3][8]

한편 LLM을 통계 도구로 쓰는 시도도 병행된다. Predicting field experiments with large language models는 276개 경제학 현장 실험 결과를 예측해 78% 정확도를 보고했고, Simulating tabular datasets through LLMs는 질적 가설을 표 데이터로 빠르게 탐색한다. SciPredict는 33개 분야의 405개 과제로 LLM이 실험 결과와 자신의 신뢰도를 얼마나 맞히는지 잰다. 다만 이들은 검증 대상이지 증거가 아니라는 점을 분명히 해야 한다. 가설 선별에는 쓸 수 있어도 결론의 근거로 인용하기는 이르다.[6][7][8][10][12]

국내 관점에서 이 칸은 가장 바로 쓸 수 있다. 공공 AI 평가, 조달 모델 선정, 사내 벤치마크 모두 점수표를 순위로 바꾸는 순간 이 논문들의 지적이 적용된다. 평가 표본 수를 사전에 계산하고 순위에 신뢰구간을 붙이는 일은 비용이 거의 들지 않는다. 안 하는 것이 위험이다.

> [!tip] 정리
> 벤치마크는 측정 도구이고 측정에는 오차가 있다. 오차를 숨긴 순위표는 다른 대분류의 모든 성능 비교를 오염시킨다.

**대표 도구·시스템** — MBTIBENCH · SciPredict · TasteBench · CELEUS · rank CI / resolution ratio q · paired-bootstrap MCS · R-IDeA · Structural Specificity Testing

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Quantifying Ranking Uncertainty in LLM Benchmarks](../../docs/papers/10284_Quantifying_Ranking_Uncertainty_in_LLM_Benchmarks/index.html) — Bitya Neuhof 외, 2026 · 인용 2
2. [Resolution Diagnostics for Paired LLM Evaluation](../../docs/papers/10326_Resolution_Diagnostics_for_Paired_LLM_Evaluation/index.html) — Anany Kotawala, 2026
3. [Sticks and Stones: Positive vs. Negative Emotional Prompt Framings](../../docs/papers/10502_Sticks_and_Stones_Positive_vs_Negative_Emotional_Prompt_Fram/index.html) — Vipul Joshi 외, 2026
4. [The Leaderboard Lottery: Why Top LLM Rankings Are Often Coin Flips, and How to Fix Them](../../docs/papers/10572_The_Leaderboard_Lottery_Why_Top_LLM_Rankings_Are_Often_Coin/index.html) — Shourya Vir Jain, 2026
5. [Confidence in Large Language Model Evaluation: A Bayesian Approach to Limited-Sample Challenges](../../docs/papers/237_Confidence_in_Large_Language_Model_Evaluation_A_Bayesian_App/index.html) — Xiao Xiao 외, 2025
6. [Predicting field experiments with large language models](../../docs/papers/631_Predicting_field_experiments_with_large_language_models/index.html) — Yaoyu Chen 외, 2025
7. [Simulating tabular datasets through LLMs to rapidly explore hypotheses about real-world entities](../../docs/papers/757_Simulating_tabular_datasets_through_llms_to_rapidly_explore/index.html) — Miguel Zabaleta 외, 2024
8. [Behavior Is Not Representation: Hypothesis Tests for Concept Steering in LLMs](../../docs/papers/9300_Behavior_Is_Not_Representation_Hypothesis_Tests_for_Concept/index.html) — Siddharth Shukla, 2026
9. [Representative, Informative, and De-Amplifying: Requirements for Robust Bayesian Active Learning under Model Misspecification](../../docs/papers/1100_Representative_Informative_and_De-Amplifying_Requirements_fo/index.html) — Roubing Tang 외, 2026.03
10. [SciPredict: Can LLMs Predict the Outcomes of Scientific Experiments in Natural Sciences?](../../docs/papers/10393_SciPredict_Can_LLMs_Predict_the_Outcomes_of_Scientific_Exper/index.html) — Udari Madhushani Sehwag 외, 2026
11. [TasteBench: multimodal benchmark for sensory prediction, from molecules to sustainable foods](../../docs/papers/10542_TasteBench_multimodal_benchmark_for_sensory_prediction_from/index.html) — Anna Thomas 외, 2026
12. [Exploiting LLMs for Automatic Hypothesis Assessment via a Logit-Based Calibrated Prior](../../docs/papers/330_Exploiting_LLMs_for_Automatic_Hypothesis_Assessment_via_a_Lo/index.html) — Yue Gong 외, 2025 · 인용 10

---

## S49 · 중도절단 생존분석

*제9부 · 인과·통계 추론* · **Survival Analysis with Censoring** · *서브카테고리*

`16편` `2026–2026` `부상` `2025+ 16편`

> [!abstract] 화면에 띄울 한 줄
> 2026 생존분석은 예측에서 생성·증류·해석의 부품화 단계로 들어섰다.

**16편, 전부 2026년이고 상태는 EMERGING이다. 중도절단이 있는 시간-사건 데이터는 의료 AI의 가장 오래된 통계 문제인데, 이 칸에서는 딥러닝 부품이 한꺼번에 붙기 시작했다.**

생성 쪽의 사건은 SurvDiff다. 혼합형 공변량, 사건 시간, 우측 중도절단을 하나의 diffusion 모델로 함께 생성하고 survival 맞춤 손실로 학습해, 기존 방법보다 공변량 충실도와 하류 성능이 좋다고 보고했다. 같은 맥락에서 DCDM-ECG는 71개 SCP 진단 코드와 5개 수치 인구통계를 76차원 조건 벡터로 묶어, label-only 생성기가 왜곡하던 환자 인구통계 분포를 실제에 가깝게 재현한다. 민감한 임상 데이터를 합성으로 대체하려는 흐름이다.[2][6]

합성 데이터에는 경고가 따라붙는다. Empirical-Distribution Matching for Synthetic ECG Classification은 합성 데이터로만 학습하고 실제로 시험하는 설정에서 13가지 샘플링 정책을 비교해, CV·NLP에서 통용되는 클래스 재균형 기법이 오히려 성능을 해치고 실제 학습 분포를 그대로 재현하는 naive bootstrap이 가장 낫다고 보였다. 다른 분야의 통념을 가져다 쓰면 안 된다는 반증이다.[3]

모델 지식의 이전도 통계적으로 정식화됐다. DiSKD는 경쟁위험 분석에서 검열된 관측치와 teacher-student 간 outcome 정의 이질성을 다루며, cause-specific time-dependent KL divergence로 외부 teacher 예측을 내부 모델에 적응적으로 통합한다. Component-Wise Composite Likelihood Distillation for Censored Time-to-Event Data는 부분적으로만 특정된 outcome 분포에도 적용되는 증류 틀을 제시한다. 기관 간에 원자료를 옮기지 않고 모델 지식만 옮기는 길이다.[1]

해석과 예측의 정교화가 뒤따른다. SurvFD는 예측함수를 시간의존·시간독립 성분으로 분해하고, SurvSHAP-IQ가 시간축을 포함한 고차 상호작용을 추정한다. FunCQNet은 eGFR 궤적 같은 함수형 바이오마커로 신장이식 후 장기 생존시간의 다중 분위수를 예측하고, SYSURV는 random survival forest의 개별 생존곡선으로 예외적 생존 특성의 하위 집단을 미분 가능하게 찾는다. Interpreting Sepsis Prediction through Positional Explanation의 PaX는 무엇을 측정했는지와 언제 측정했는지를 설명에서 분리해야 한다고 짚는다. 측정 시점이 정보라는 점을 놓친 설명은 오도한다.[4][8]

국내 관점에서 이 칸은 의료 AI 상용화의 통계 기반이다. 생존 예측은 중도절단을 어떻게 다루는지에 결과가 달려 있고, 이를 문서화하지 않은 모델은 심사에서 걸린다. 합성 데이터와 증류는 데이터 반출 규제를 우회하는 요령이 아니라, 외부 검증 가능성을 높이는 수단으로 설계해야 한다.

> [!tip] 정리
> 생존분석은 인과·통계 추론이 임상 AI와 만나는 접점이다. 생성·증류·해석 모두 중도절단을 올바르게 다룬다는 전제 위에서만 의미를 갖는다.

**대표 도구·시스템** — SurvDiff · DiSKD · SurvFD / SurvSHAP-IQ · FunCQNet · SYSURV · PaX · MLCI (nHSIC) · ScoreStop · DCDM-ECG · Random Survival Forest

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Component-Wise Composite Likelihood Distillation for Censored Time-to-Event Data](../../docs/papers/9420_Component-Wise_Composite_Likelihood_Distillation_for_Censore/index.html) — Feiyang Deng 외, 2026
2. [DCDM-ECG: Demographic-Conditional Diffusion Model for 12-Lead ECG Generation](../../docs/papers/9479_DCDM-ECG_Demographic-Conditional_Diffusion_Model_for_12-Lead/index.html) — Benedikt Kolbeinsson 외, 2026
3. [Empirical-Distribution Matching for Synthetic ECG Classification](../../docs/papers/9582_Empirical-Distribution_Matching_for_Synthetic_ECG_Classifica/index.html) — Benedikt Kolbeinsson 외, 2026
4. [Interpreting Sepsis Prediction through Positional Explanation](../../docs/papers/9842_Interpreting_Sepsis_Prediction_through_Positional_Explanatio/index.html) — Chaehyeon Kim 외, 2026
5. [ScoreStop: Gradient-based early stopping using functional score tests](../../docs/papers/10397_ScoreStop_Gradient-based_early_stopping_using_functional_sco/index.html) — Oliver J. Hines 외, 2026
6. [SurvDiff: A Diffusion Model for Generating Synthetic Data in Survival Analysis](../../docs/papers/10520_SurvDiff_A_Diffusion_Model_for_Generating_Synthetic_Data_in/index.html) — Marie Brockschmidt 외, 2026
7. [Discrete Survival Knowledge Distillation for Competing Risks Analysis](../../docs/papers/9522_Discrete_Survival_Knowledge_Distillation_for_Competing_Risks/index.html) — Feiyang Deng 외, 2026
8. [FunCQNet: A Functional Censored Quantile Neural Network for Predicting Long-Term Post-Transplant Kidney Survival](../../docs/papers/9706_FunCQNet_A_Functional_Censored_Quantile_Neural_Network_for_P/index.html) — Jiaqi Men 외, 2026

---

## S50 · 기계학습 원자간 포텐셜

*제10부 · 계산 재료 시뮬레이션* · **Machine-Learned Interatomic Potentials** · *서브카테고리*

`37편` `2023–2026` `가속` `2025+ 35편`

<sub>계산 재료 시뮬레이션 고유 배정 107편(중복 포함 559편 · 웹 인덱스 기준) · 서브카테고리 4개 · 본 파트 4개로 100% 커버</sub>

> [!quote] 파트 도입
> 해자는 모델이 아니라 DFT 계산 데이터다. 생성은 값싸졌고 합성 가능성과 독립 재현이 병목이다.

> [!abstract] 화면에 띄울 한 줄
> 2026 MLIP는 DFT 대체재로 자리 잡았고, 경쟁은 오차 수치에서 곡률·불확실성으로 옮겨 갔다.

**37편 중 35편이 2025년 이후다. 이 칸은 양자 정확도와 힘장(force field) 속도를 동시에 얻는다는 약속이 실무 워크플로에 들어온 과정이고, 동시에 그 약속의 한계가 실험으로 측정되기 시작한 과정이다.**

2026년의 가장 구체적인 숫자는 자동 전이상태 탐색에서 나왔다. MACE-OMol25를 쓴 MLIP 기반 반응 경로 탐색 워크플로 벤치마크는 유기계에서 96.6%의 성공률을 보이면서 DFT 계산 비용을 94-96% 줄였다. 같은 해 'A New Paradigm for Computational Chemistry'는 파운데이션 MLIP가 시스템별 대규모 학습 데이터 없이 양자 정확도와 힘장 속도를 함께 내고, 향후 10년 안에 DFT의 주도적 지위를 대체할 수 있다고 전망했다. 이 전망은 주장이며 검증된 사실은 아니라는 점을 구분해야 한다.[1]

학습 신호 자체가 바뀌고 있다. 지금까지 MLIP는 에너지와 힘의 RMSE로 평가되고 학습됐지만, Hi-MLIP와 HINT 프로토콜은 포텐셜 에너지 표면의 곡률인 Hessian을 감독 신호로 쓰며, 전이 상태 탐색과 자유 에너지 예측, 비조화 물질의 초전도 특성 예측을 실험 정확도 수준으로 끌어올렸다고 보고한다. RMSE가 낮아도 PES가 매끄럽지 않으면 동역학이 무너진다는 인식이 학습 목표에 반영된 것이다.

아키텍처는 효율 쪽으로 재설계된다. Smooth Dynamic Cutoffs는 고정 컷오프라는 통념에 도전해 목표 이웃 수에 맞춰 반경을 부드럽게 조절하며, MACE·NequIP·Orbv3·TensorNet 네 모델에 적용했다. RANGE는 master node를 가상 표현으로 써서 선형 시간에 전역 정보를 전달하고, TriForces는 composition·structure·interaction을 세 스트림으로 나눠 자기지도 표현을 만든다. DenSNet은 등변 신경망으로 전자 밀도를 학습해 분극률·쌍극자모멘트 같은 분광 관측량까지 열어 둔다.

신뢰성 쪽 신호도 같은 해에 나왔다. Bayesian Last Layer는 마지막 층만으로 deep ensemble에 필적하는 불확실성을 싸게 얻되 과소추정 원인 두 가지를 분석해 보정한다. 반면 DFT 자체를 겨냥한 olLOSC나 FunctionalAgent는 정확도의 기준선인 범함수를 에이전트가 설계하는 단계까지 가 있다. 학습 데이터의 질을 결정하는 것이 DFT 계층이므로, MLIP 경쟁은 결국 그 아래 계산의 품질 경쟁이기도 하다.

국내 관점에서 모델 아키텍처는 해자가 되지 못한다. MACE·NequIP 계열은 공개되어 있고 파운데이션 모델도 배포된다. 해자는 자기 소재 계에서 생산한 고품질 DFT 데이터와, 불확실성 추정을 통해 모델을 신뢰해도 되는 영역과 DFT로 되돌아가야 하는 영역을 가르는 운용 능력이다. 능동학습과 불확실성 정량이 도입 비용을 결정한다.

> [!tip] 정리
> MLIP의 시대는 DFT의 종말이 아니라 DFT 데이터가 자산이 되는 시대다. 모델은 누구나 쓰고, 틀리는 곳을 아는 팀이 이긴다.

**대표 도구·시스템** — MACE · MACE-OMol25 · QHNetV2 · ORB-v3 · NequIP · TensorNet · PFP/MM · MDtrajNet-1 · DenSNet · BLIPs · CEITNet · AllScAIP · RANGE · fix pimd/langevin (LAMMPS)

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [A New Paradigm for Computational Chemistry](../../docs/papers/2995_A_New_Paradigm_for_Computational_Chemistry/index.html) — Raphael T. Husistein 외, 2026.04 · 인용 1
2. [Data-driven construction of machine-learning-based interatomic potentials for gas-surface scattering dynamics: the case of NO on graphite](../../docs/papers/3066_Data-driven_construction_of_machine-learning-based_interatom/index.html) — 2026.03 · 인용 9
3. [Reliable and Efficient Automated Transition-State Searches with Machine-Learned Interatomic Potentials](../../docs/papers/3229_Reliable_and_Efficient_Automated_Transition-State_Searches_w/index.html) — 2026.04 · 인용 2
4. [Smooth Dynamic Cutoffs for Machine Learning Interatomic Potentials](../../docs/papers/10459_Smooth_Dynamic_Cutoffs_for_Machine_Learning_Interatomic_Pote/index.html) — Kevin Han 외, 2026
5. [Benchmarking Universal Machine-Learned Interatomic Potentials for High-Temperature Metal-Organic Framework Chemistry](../../docs/papers/3038_Benchmarking_Universal_Machine-Learned_Interatomic_Potential/index.html) — Connor W. Edwards 외, 2026.04
6. [Projected Hessian Learning: Fast Curvature Supervision for Accurate Machine-Learning Interatomic Potentials](../../docs/papers/3216_Projected_Hessian_Learning_Fast_Curvature_Supervision_for_Ac/index.html) — 2026.03

---

## S51 · 생성형 무기 재료 설계

*제10부 · 계산 재료 시뮬레이션* · **Generative Inorganic Materials Discovery** · *서브카테고리*

`33편` `2023–2026` `가속` `2025+ 30편`

> [!abstract] 화면에 띄울 한 줄
> 생성은 값싸졌다. 2026의 목표함수는 합성 가능성이고, 검증 부담은 그대로다.

**33편 중 30편이 2025년 이후다. 2023년 GNoME가 안정 결정 220만 개를 제시하며 후보 발굴의 병목을 풀어 놓은 뒤, 이 칸의 질문은 얼마나 많이 만드느냐에서 만든 것이 실제로 만들어지느냐로 이동했다.**

2026년의 가장 뚜렷한 변화는 합성 가능성이 명시적 목표가 됐다는 점이다. 사전학습된 확산 모델 MatterGen을 MatInvent 기반 다목적 강화학습으로 미세조정해, bulk modulus나 자기 밀도 같은 목표 물성을 만족하면서 전구체 기반 합성 가능성까지 고려한 결정 구조를 생성하는 프레임워크가 나왔다. DiffSyn은 한 걸음 더 나아가 50년치 제올라이트 합성 레시피 23,961건으로 학습해 목표 구조와 유기 템플릿이 주어지면 확률적 합성 경로를 만들고, 실제 UFI 소재 합성으로 검증했다.[2]

생성 모델은 DFT 데이터 위에서 돌아간다. WyFormer 생성모델과 범용 원자간 포텐셜 uMLIP를 결합한 파이프라인은 기존 데이터베이스에 없는 결정 구조를 만든 뒤, uMLIP 구조 최적화와 PES 유래 기술자로 열역학적 안정성, 전기화학적 호환성, Li-ion 전도도를 싸게 거른다. 이는 앞 칸의 MLIP가 생성 설계의 스크리닝 엔진으로 흡수되는 구조이며, 생성형 설계 프레임워크는 물리 기반 재료 표현, 파운데이션 모델, 고처리량 실험을 닫힌 루프로 묶을 것을 제안한다.

표현 쪽에서는 역문제가 늘었다. GLASS는 점수 기반 확산 모델과 미분 가능한 분광 시뮬레이션을 합쳐 상호작용 포텐셜 없이 비정질 구조를 복원하고, MUSE는 분광 데이터를 공통 화학 언어로 삼아 다중 물성 분자를 생성한다. 에이전트도 들어왔다. LLM 에이전트 Ara는 가수분해 안정성과 광촉매 성능을 동시에 만족하는 COF를 역설계해 무작위 탐색 대비 11.5배 높은 52.7%의 hit rate를 기록했다. 열전 도펀트 탐색에서는 LLM이 300여 편 논문에서 조성 데이터를 뽑고 DFT/MD로 검증하는 파이프라인이 제시됐다.

비판적 신호는 두 가지다. 하나는 신규성 판단의 오류다. 질서 구조만 담은 데이터베이스로 신규성을 판정하면 무질서 상을 배제해 이미 알려진 무질서 부모의 자손을 신물질로 오인할 수 있고, group-subgroup 기반 order-(dis)order family tree가 이를 바로잡자고 제안한다. 다른 하나는 이 대분류 전체의 간극으로 지적된 점이다. 자율 실험실 A-lab 사례처럼 발견 주장의 재현성과 신뢰성 검증은 여전히 취약하다. 생성된 구조가 합성되었다는 주장과 독립 분석이 그것을 확인했다는 사실은 다른 것이다.

국내 관점에서 생성형 설계는 진입이 쉽다. MatterGen 계열과 uMLIP가 공개되어 있어 후보 목록은 누구나 만든다. 남는 희소 자원은 합성 레시피 데이터, 분광·회절 장비, 그리고 자체 주장을 독립적으로 재분석할 절차다. 생성 결과를 논문으로 내는 팀보다 합성 실패 사례까지 데이터로 쌓는 팀이 다음 모델의 학습 데이터를 쥔다.

> [!tip] 정리
> 생성은 이제 싸고, 검증은 여전히 비싸다. 합성 가능성을 목표함수에 넣은 것은 진전이지만, 독립 재분석 없이는 발견이 아니라 후보다.

**대표 도구·시스템** — GNoME · MatterGen · MatterGen-e- · MatterGPT/SLICES · CatFlow · WyFormer · DiffSyn · GLASS · MUSE · SR-CGCNN · DISSOLVR · Open Electrolyte Databank · Ara agent

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Generative design of inorganic materials](../../docs/papers/3115_Generative_design_of_inorganic_materials/index.html) — 2026.04 · 인용 10
2. [DiffSyn: a generative diffusion approach to materials synthesis planning](../../docs/papers/3077_DiffSyn_a_generative_diffusion_approach_to_materials_synthes/index.html) — Elton Pan 외, 2026.02 · 인용 6
3. [Generative Chemical Language Models for Energetic Materials Discovery](../../docs/papers/3114_Generative_Chemical_Language_Models_for_Energetic_Materials/index.html) — 2026.03
4. [Generative Pipeline for Discovering Solid-State Battery Materials with Universal Atomistic Potentials](../../docs/papers/9727_Generative_Pipeline_for_Discovering_Solid-State_Battery_Mate/index.html) — Artem Dembitskiy 외, 2026 · 인용 139
5. [A Physics-Informed Chemical Rule for Topological Materials Discovery](../../docs/papers/1104_A_Physics-Informed_Chemical_Rule_for_Topological_Materials_D/index.html) — Xinyu Xu 외, 2026
6. [Generative Structure Search for Efficient and Diverse Discovery of Molecular and Crystal Structures](../../docs/papers/3120_Generative_Structure_Search_for_Efficient_and_Diverse_Discov/index.html) — 2026.04

---

## S52 · 고온 합금 포텐셜

*제10부 · 계산 재료 시뮬레이션* · **High-Temperature Alloy Potentials** · *서브카테고리*

<sub>타임라인 분석 명칭: High-Temperature Alloy & Extreme-Condition Potentials</sub>

`19편` `2023–2026` `가속` `2025+ 17편`

> [!abstract] 화면에 띄울 한 줄
> 2026 합금·용융 계로 범위가 넓어졌고, 회절 실험이 장거리 MLIP의 한계를 드러냈다.

**19편 중 17편이 2025년 이후다. 고온 합금과 용융 계는 포텐셜이 가장 쉽게 틀리는 영역이다. 이 칸의 2026년 작업은 범위를 넓히는 일과 어디서 틀리는지를 실험으로 확인하는 일이 함께 진행된 사례다.**

합금 쪽에서는 계별 범용 포텐셜이 연이어 나왔다. 신경진화 포텐셜 NEP로 만든 CrCoNi 중엔트로피 합금 포텐셜은 성분 의존적 거동을 제1원리 정확도로 유지하면서 대규모 원자 시뮬레이션을 가능하게 한다. 용융 쪽에서는 Moment Tensor Potentials를 DFT 학습 데이터로 훈련해 칼슘 전해 공정의 용융 Ca-Cu 합금과 CaCl₂-KCl 전해질의 물성을 실험값 대비 20% 이내 편차로 예측했다. 산업 공정 변수를 직접 겨냥한 사례다.

전이 가능성의 시험도 있었다. NEP89는 고체 물성으로 학습된 모델인데, Al-Ti 액상 합금의 구조와 동역학을 분자동역학으로 계산하고 실험 데이터와 일치함을 보여 액상 영역 활용 가능성을 입증했다. MACE-Osaka26은 기존 89개 원소 한계를 넘어 97개 원소를 지원하고 minor actinide를 포함한 중원소를 처음 폭넓게 덮어 핵공학 시뮬레이션 가속을 겨냥한다. 범용성이 원소 주기율표 쪽으로 확장되는 방향이다.[4]

데이터 쪽 해자 논리가 가장 선명한 곳이 여기다. AQVolt26은 r²SCAN 수준에서 생성한 단일점 계산 322,656개로 리튬 할라이드 고체전해질을 다루며, 기존 파운데이션 ML 모델이 고온의 왜곡된 구조 영역에서 에너지 예측 정확도가 떨어지는 문제를 겨냥한다. 같은 흐름에서 자기일관 정전기 MLIP의 설계 공간 분석은 금속-물 계면과 SiO2 결함에서 장거리 정전기 처리 방식을 비교하고, 흡착물 배치 샘플링 AdsorbSample이나 GREX 같은 생성 샘플러는 열역학 샘플링을 가속한다.[1]

그리고 감사가 있다. 두 MACE 기반 포텐셜, 단거리와 장거리 모델을 중성자·X선 회절 및 분자동역학과 대조한 연구는 장거리 상호작용이 액체 구조는 개선하나 켄칭 후 비정질 유리의 중거리 질서(MRO)는 여전히 복원하지 못한다고 결론 냈다. 에너지·힘 오차가 낮아도 실험 관측량이 맞지 않을 수 있다는 직접 증거다. 모델 평가를 학습 데이터 분포 안의 오차가 아니라 회절 같은 독립 실험과의 대조로 옮겨야 한다는 신호다.

국내 관점에서 이 칸은 제조업 연계 가능성이 가장 높다. 합금, 용융염 전해질, 고체전해질, 원자력 소재 모두 실험 대조 데이터가 비싸고 희소한 영역이다. 포텐셜을 만드는 능력보다 고온에서 DFT 데이터를 생산하고 회절·분광 측정으로 포텐셜을 교차 검증하는 체계를 가진 기관이 신뢰할 수 있는 시뮬레이션 서비스를 낼 수 있다.

> [!tip] 정리
> 고온 영역의 범용 포텐셜은 범위가 넓어질수록 검증 지점이 늘어난다. 회절 실험과 맞닿은 데이터 파이프라인이 이 칸의 실질적 진입장벽이다.

**대표 도구·시스템** — NEP / NEP89 · Moment Tensor Potentials · MACE-Osaka26 · AQVolt26 · MAD-1.5 · AMDAT · GREX · AdsorbSample · MADField · Hi-MLIP/HINT · AlloyVAE · PI-GP

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [AQVolt26: High-Temperature r²SCAN Halide Dataset for Universal ML Potentials and Solid-State Batteries](../../docs/papers/3023_AQVolt26_High-Temperature_r²SCAN_Halide_Dataset_for_Universa/index.html) — 2026.04 · 인용 1,079
2. [General-Purpose Machine-Learned Potential for CrCoNi Alloys Enabling Large-Scale Atomistic Simulations with First-Principles Accuracy](../../docs/papers/372_General-Purpose_Machine-Learned_Potential_for_CrCoNi_Alloys/index.html) — Yong-Chao Wu 외, 2026.03
3. [AlloyVAE: A Generative Model for Complex Probabilistic Field-to-Field Relationships in Alloys](../../docs/papers/3018_AlloyVAE_A_Generative_Model_for_Complex_Probabilistic_Field-/index.html) — 2026.04
4. [Molecular Dynamics Simulations of Al-Ti Metallic Alloy Melts Using a Transferable Machine-Learning Potential](../../docs/papers/3174_Molecular_Dynamics_Simulations_of_Al-Ti_Metallic_Alloy_Melts/index.html) — Yuna Kato 외, 2026.04
5. [Neutron and X-ray Diffraction Reveal the Limits of Long-Range Machine Learning Potentials for Medium-Range Order in Silica Glass](../../docs/papers/3190_Neutron_and_X-ray_Diffraction_Reveal_the_Limits_of_Long-Rang/index.html) — 2026.04
6. [AMDAT: An Open-Source Molecular Dynamics Analysis Toolkit for Supercooled Liquids, Glass-Forming Materials, and Complex Fluids](../../docs/papers/095_AMDAT_An_Open-Source_Molecular_Dynamics_Analysis_Toolkit_for/index.html) — Pierre Kawak 외, 2026.02 · 인용 5

---

## S53 · 양자 다체 시뮬레이션

*제10부 · 계산 재료 시뮬레이션* · **Quantum Many-Body Simulation** · *서브카테고리*

<sub>타임라인 분석 명칭: Quantum Many-Body & Quantum-Device Simulation</sub>

`18편` `2024–2026` `부상` `2025+ 15편`

> [!abstract] 화면에 띄울 한 줄
> 2026 신경망 양자 상태는 산일·개방계로 확장되고 정밀도·벤치마크가 정비되는 초기 국면이다.

**18편 중 15편이 2025년 이후다. 양자 다체 시뮬레이션은 이 대분류에서 가장 이른 단계의 칸이다. 타임라인은 2024년에 시작해 EMERGING 상태이며, 재료 시뮬레이션과의 접점은 신경망 파동함수와 전자구조 방법에서 온다.**

가장 큰 변화는 적용 범위의 확장이다. Neural quantum states를 빛-물질 결합계의 산일 동역학에 처음 적용해 약 40개 원자의 1·2차원 조밀 배열에서 다체 방출 동역학을 계산했고, 특히 subradiance에서 다체 효과를 포착하는 것이 핵심이다. 같은 해 개방계와 비마르코프 동역학으로의 확장이 타임라인에 올랐다. 닫힌계의 바닥상태 추정을 넘어 실제 장치에 가까운 조건을 다루기 시작했다는 뜻이다.

계산 자원 측면의 진전도 있다. Neural Quantum States in Mixed Precision은 VMC의 Metropolis-Hastings 샘플링을 half precision으로 수행할 때의 오차에 이론적 경계를 유도하고 실제 사례에서 검증해, 정확도 손실 없이 최대 3.5배의 샘플링 속도 향상을 얻었다. Universal Neural Propagator는 구동 프로토콜을 시간 진화 연산자로 사상하는 범용 신경망으로 정확 대각화 한계를 넘는 동역학 시뮬레이션을 시도한다. 격자 게이지 이론에서는 Gauge-Equivariant GNN이 국소 게이지 대칭을 메시지 패싱에 내장했다.[1][2][4]

평가 기반이 막 생기고 있다. WF-Bench는 topological states, Wigner crystals, superconducting wavefunction 등 30여 개 목표 파동함수를 대상으로 신경망 파동함수의 표현력을 fidelity 기준으로 정량 벤치마킹한다. 아키텍처 비교가 임의 시스템에 대한 일회성 보고에서 공통 척도로 옮겨 가는 단계다. 한편 양자화학 쪽에서는 MoLe가 Hartree-Fock 분자 궤도를 입력으로 coupled cluster의 T-amplitude를 직접 예측한다.

양자 장치 쪽 작업은 시뮬레이션이라기보다 제어와 신뢰성에 가깝다. Cascade 디코더는 surface code와 고비율 BB qLDPC 코드를 하나의 합성곱 구조로 처리해 정확도-지연 trade-off를 개선하고, D-RUT는 연속변수 해밀토니안 계수를 Heisenberg 한계 정밀도로 학습하며, 양자 게이트 캘리브레이션에서 메타러닝이 이득을 주는 조건의 scaling law가 도출됐다. Q-Tag처럼 양자 회로 생성 모델의 워터마킹이라는 지식재산 문제도 등장했다. 다만 이들은 재료 시뮬레이션과 직접 연결된 결과가 아니다.[5]

국내 관점에서 이 칸은 재료 부문 투자 우선순위가 낮다. 근거 논문 상당수가 이론 도출이나 소규모 시스템 시연이며 산업 재료 문제에 대한 정량 이득은 dossier에 없다. 다만 신경망 파동함수와 혼합 정밀도 VMC는 전자구조 방법의 연장선에 있어 MLIP·DFT 계층의 정확도 기준을 높일 후보이므로, 도구와 WF-Bench 같은 벤치마크를 추적할 가치가 있다.

> [!tip] 정리
> 양자 다체 칸은 아직 재료 현장의 도구가 아니라 방법론의 실험실이다. 속도와 벤치마크가 정비되는 속도를 보며 접점을 기다릴 단계다.

**대표 도구·시스템** — Neural Quantum States / VMC · PINN-DQME · GQKAE · Cascade decoder · MetaDNS · D-RUT · Universal Neural Propagator · Q-Tag · Gauge-equivariant GNN

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Neural Quantum States in Mixed Precision](../../docs/papers/10094_Neural_Quantum_States_in_Mixed_Precision/index.html) — Massimo Solinas 외, 2026
2. [Universal Neural Propagator: Learning Time Evolution in Many-Body Quantum Systems](../../docs/papers/3272_Universal_Neural_Propagator_Learning_Time_Evolution_in_Many-/index.html) — Zihao Qi 외, 2026.05 · 인용 777
3. [Scalable Neural Decoders for Practical Fault-Tolerant Quantum Computation](../../docs/papers/10370_Scalable_Neural_Decoders_for_Practical_Fault-Tolerant_Quantu/index.html) — Andi Gu 외, 2026 · 인용 780
4. [Gauge-Equivariant Graph Neural Networks for Lattice Gauge Theories](../../docs/papers/3111_Gauge-Equivariant_Graph_Neural_Networks_for_Lattice_Gauge_Th/index.html) — 2026.04
5. [Q-Tag: Watermarking Quantum Circuit Generative Models](../../docs/papers/3226_Q-Tag_Watermarking_Quantum_Circuit_Generative_Models/index.html) — 2026.02
6. [MetaDNS: Enhancing Exploration in Discrete Neural Samplers via Metadynamics](../../docs/papers/10028_MetaDNS_Enhancing_Exploration_in_Discrete_Neural_Samplers_vi/index.html) — Xiaochen Du 외, 2026

---

## S54 · 수렴 신호: 경계가 무너지는 곳

*종합* · *종합*

> [!abstract] 화면에 띄울 한 줄
> 생성 에이전트가 형식 검증기·물리 시뮬레이터·통계 검정과 결합하는 설계로 수렴한다.

**대분류들은 서로 다른 문제를 풀지만 설계는 닮아 간다. 수렴의 축은 생성기를 외부 검증기와 묶는 것이고, 이 장은 그 접점을 정리한다.**

가장 강한 수렴은 AI 과학자와 검증기의 결합이다. 자율 AI 과학 발견, 형식 수학 정리 증명, LLM 추론·에이전트 벤치마크에 걸쳐 DeepScientist, Co-Scientist, Robin, BFS-Prover-V2가 생성-검증-반복 루프를 핵심 설계로 채택했다. 가설 에이전트에 Lean 같은 형식 검증기를 붙이는 조합은 코퍼스에서 가장 빠르게 늘어난 조합으로 꼽힌다.[2]

두 번째 수렴은 생체신호와 언어모델의 결합이다. 의료·신경 신호 모델링과 멀티모달 인식·효율화에서 EEG·ECG·fMRI를 언어모델 토큰 공간에 올리는 기반모델 구조가 공통 패턴이 됐다. SleepLM 같은 시도가 대표적이다.[5]

세 번째는 평가의 통계화다. 인과·통계 추론의 anytime-valid 검정과 conformal 예측이 LLM 추론·에이전트 벤치마크의 벤치마크 신뢰성 문제에 투입된다. 리더보드의 순위를 신뢰구간으로 바꾸는 작업이다.

수렴에는 비용이 있다. 같은 설계가 여러 곳에서 반복되면 같은 실패도 반복된다. 검증기 자체가 틀리면 전체 루프가 틀린 답을 확신한다. 증명 채점자의 아첨과 형식화의 불충실이 이를 이미 보였다.

> [!tip] 정리
> 수렴의 정책적 함의는 연구비를 생성 능력뿐 아니라 검증 인프라, 즉 형식 검증기와 재현 하네스에 병행 투입하라는 것이다. 국내 관점에서는 한 분야에서 만든 검증기를 다른 분야에 이식하는 전략이 유효하다. 형식 검증 역량은 가설 검증으로, 통계 검정 역량은 벤치마크 감사로 옮겨 쓸 수 있다. 수렴이 강한 곳일수록 검증기의 품질이 곧 시스템 전체의 품질이므로, 검증기 자체를 감사하는 층도 함께 필요하다.

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [AI scientists produce results without reasoning scientifically](../../docs/papers/9108_ai_scientists_produce_results_without_reasoning_scienti/index.html) — Martiño Ríos-García 외, 2026 · 인용 342
2. [Accelerating scientific discovery with Co-Scientist](../../docs/papers/3001_Accelerating_scientific_discovery_with_Co-Scientist/index.html) — Juraj Gottweis 외, 2026.05 · 인용 97
3. [Scaling up Multi-Turn Off-Policy RL and Multi-Agent Tree Search for LLM Step-Provers](../../docs/papers/10379_Scaling_up_Multi-Turn_Off-Policy_RL_and_Multi-Agent_Tree_Sea/index.html) — Ran Xin 외, 2026
4. [Propose, Critique, Falsify: Benchmarking Self-Verifying AI Scientists](../../docs/papers/10259_Propose_Critique_Falsify_Benchmarking_Self-Verifying_AI_Scie/index.html) — Aayam Bansal 외, 2026
5. [SleepLM: Natural-Language Intelligence for Human Sleep](../../docs/papers/10454_SleepLM_Natural-Language_Intelligence_for_Human_Sleep/index.html) — Zongzhe Xu 외, 2026
6. [BrainJanus: A Unified Model for Understanding and Generation across Brain, Vision, and Language](../../docs/papers/9354_BrainJanus_A_Unified_Model_for_Understanding_and_Generation/index.html) — Haitao Wu 외, 2026

---

## S55 · 부상과 쇠퇴

*종합* · *종합*

> [!abstract] 화면에 띄울 한 줄
> anytime-valid 검정이 부상하고, 복잡한 모델이 단순 베이스라인에 지는 사례가 쌓이며 낡은 가정이 쇠퇴한다.

**코퍼스에서 부상하는 흐름과 쇠퇴하는 흐름은 같은 뿌리에서 나왔다. 평가의 엄밀성에 대한 요구가 새 방법을 밀어올리고 느슨한 관행을 밀어낸다.**

부상하는 쪽은 anytime-valid 통계검정이다. e-process와 martingale 기반 검정이 LLM 평가, SAE 특징 검증, 확산 샘플링으로 번졌다. 데이터를 보면서 멈춰도 유효한 검정은 지속 배포되는 AI 시스템의 상시 보증이라는 요구에 맞는다. 인과·통계 추론가 작은 규모로도 중요한 이유다.[1][3]

쇠퇴하는 쪽은 복잡한 지도학습 모델이 단순 선형·부스팅 베이스라인을 이긴다는 암묵적 가정이다. 유전자 섭동 예측, 분자 파운데이션 모델, 도메인 적응에서 부정적 결과가 반복됐다. 단일세포 파운데이션 모델이 확산되는 동시에 반증이 쌓이는 모습이 S06 에 그대로 보인다.

쇠퇴의 대상은 모델 종류가 아니라 보고 방식이다. 베이스라인 없는 성능 주장, 단일 점추정 순위, 사람 검증 없는 자동 채점이 퇴조한다. S48 는 점추정 1위가 사후 선택 문제임을 보였다.

두 흐름의 합은 연구 문화의 변화다. 새 모델의 가치는 얼마나 복잡한가가 아니라 얼마나 단순한 대안을 확실히 이기는가로 측정된다. 이 기준은 국내 연구 평가에도 곧바로 적용할 수 있다.

국내 시사점은 구체적이다. 평가 사업과 심사에서 단순 베이스라인 비교를 필수 항목으로 넣고, 통계 방법론 교육에 순차·anytime-valid 추론을 포함시켜야 한다. 이 두 조치는 비용이 적고, 어떤 대분류의 연구에도 즉시 적용되며, 부풀려진 성능 주장이 예산을 소진하는 것을 막는다.[1][3]

> [!tip] 정리
> 부상과 쇠퇴 모두 증명 책임의 이동을 가리킨다. 주장하는 쪽이 비교와 불확실성 추정을 함께 내야 한다. 이 장의 두 흐름을 함께 보면, 앞으로 1년은 새 모델의 등장보다 평가 규범의 정착이 더 큰 변화를 만들 가능성이 높다.

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Anytime-Valid Hypothesis Testing for Sparse Autoencoder Feature Validation](../../docs/papers/9250_Anytime-Valid_Hypothesis_Testing_for_Sparse_Autoencoder_Feat/index.html) — Rudransh Khera, 2026 · 인용 675
2. [Evaluating out of distribution generalization of protein language models](../../docs/papers/9606_Evaluating_out_of_distribution_generalization_of_protein_lan/index.html) — Kumaresh Krishnan 외, 2026 · 인용 5
3. [Anytime-Valid Confirmation of Label-Shift Corrections](../../docs/papers/9249_Anytime-Valid_Confirmation_of_Label-Shift_Corrections/index.html) — Seungjin Choi, 2026
4. [CITE: Anytime-Valid Statistical Inference in LLM Self-Consistency](../../docs/papers/9402_CITE_Anytime-Valid_Statistical_Inference_in_LLM_Self-Consist/index.html) — Hirofumi Ota 외, 2026
5. [DP-SPRT: Differentially Private Sequential Probability Ratio Tests](../../docs/papers/9544_DP-SPRT_Differentially_Private_Sequential_Probability_Ratio/index.html) — Thomas Michel 외, 2026
6. [Safe Particle Selection for Diffusion Steering](../../docs/papers/10359_Safe_Particle_Selection_for_Diffusion_Steering/index.html) — Kianoosh Ashouritaklimi 외, 2026

---

## S56 · 비어 있는 자리

*종합* · *종합*

> [!abstract] 화면에 띄울 한 줄
> 생성은 풍부한데 검증, 귀속, 장기 재현성, 자율 실험실 거버넌스는 비어 있다.

**코퍼스는 무엇이 많은지만큼 무엇이 없는지도 말해 준다. 공백은 대개 능력이 아니라 책임과 검증 쪽에 있다.**

첫째 공백은 검증 없는 생성의 남용이다. 생체분자 생성 모델링과 계산 재료 시뮬레이션에서 수백 편의 확산·플로 매칭 생성 모델이 쏟아지지만, Rietveld 정제 오류와 자기 일관성 검사에서 상당수 탈락하는 사례, 딥러닝이 단순 베이스라인을 못 이기는 사례가 반복 보고됐다. 생성은 쉽고 검증은 어렵다는 구조 문제다.

둘째는 AI 저자성과 귀속이다. LLM이 가설부터 논문까지 쓰는 사례가 늘었지만 기여도를 어떻게 표기하고 표절을 어떻게 판별할지에 합의된 기준이 없다. 아이디어 표절 논쟁이 이어지고 있어 S38 같은 감사 도구가 필요하다.

셋째는 저조하게 다뤄진 영역이다. AI가 낸 과학적 주장의 장기 재현성 추적, 자율 실험실의 안전·보안 거버넌스, 비영어권 저자원 언어 문헌의 접근성, AI 과학자 시스템이 출판 편향을 증폭하는 문제가 코퍼스에서 거의 보이지 않는다.

넷째는 리더보드 신뢰성이다. 보상 해킹, 순위 불확실성, 평가 프로토콜 아티팩트, 숨은 프롬프트 사용이 줄줄이 보고돼 벤치마크의 벤치마크가 필요한 상황이다.

국내 시사점은 공백이 곧 선점 기회라는 것이다. 학술 출판 기관과 연구비 기관이 AI 기여도 공개 표준, 예컨대 출처 기록 장부를 공동으로 제정하면 해외 표준을 수입하는 입장에서 벗어난다. 한국어를 포함한 저자원 언어 문헌의 접근성은 국내만이 채울 수 있는 칸이다.

**미개척 영역(코퍼스 메타 분석)**

- AI 생성 과학적 주장의 장기적 재현성 추적
- 자율 실험실의 안전·보안 거버넌스
- 비영어권/저자원 언어 과학 문헌의 AI 접근성
- AI 과학자 시스템의 publication bias 증폭 문제

> [!tip] 정리
> 공백의 공통점은 기술이 아니라 제도다. 표준과 거버넌스를 먼저 만드는 쪽이 기술 경쟁에서도 유리한 규칙을 쓴다. 공백 목록은 연구 주제 후보이기도 하다. 재현성 추적과 거버넌스는 기술 논문보다 제도 연구와 공동 표준화 사업으로 먼저 채워질 것이다. 어느 공백이든 해소의 첫 단계는 측정이다. 무엇을 얼마나 놓치고 있는지 재는 지표가 없으면 정책도 설계할 수 없다.

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Credit Where Credit Is Due: A Taxonomy of AI Contributions to Scientific Discovery and Recommendations for Authorship Policy](../../docs/papers/9459_Credit_Where_Credit_Is_Due_A_Taxonomy_of_AI_Contributions_to/index.html) — Luiz Felipe Caparelli Piochi, 2026 · 인용 678
2. [CreditMap: Provenance Ledgers for Attribution in Human--AI Scientific Collaboration](../../docs/papers/9460_CreditMap_Provenance_Ledgers_for_Attribution_in_Human--AI_Sc/index.html) — Aayam Bansal 외, 2026 · 인용 401
3. [Data integrity in materials science in the era of AI: balancing accelerated discovery with responsible science and innovation](../../docs/papers/252_Data_integrity_in_materials_science_in_the_era_of_AI_balanci/index.html) — Nik Reeves-McLaren 외, 2026 · 인용 11
4. [Quantifying Ranking Uncertainty in LLM Benchmarks](../../docs/papers/10284_Quantifying_Ranking_Uncertainty_in_LLM_Benchmarks/index.html) — Bitya Neuhof 외, 2026 · 인용 2
5. [Scientists decry conference’s use of hidden prompts to snare AI peer reviews](../../docs/papers/11015_Scientists_decry_conferences_use_of_hidden_prompts_to_snare/index.html) — Dalmeet Singh Chawla, 2026 · 인용 1
6. [Rethinking Self-Consistency in Protein Generative Models](../../docs/papers/10334_Rethinking_Self-Consistency_in_Protein_Generative_Models/index.html) — Minji Lee 외, 2026

---

## S57 · 검증 전환의 여섯 축

*종합* · *종합*

> [!abstract] 화면에 띄울 한 줄
> 2026년의 공통 주제는 생성이 아니라 검증이다. 여섯 축에서 같은 방향의 증거가 나온다.

**이 코퍼스를 한 줄로 줄이면 생성에서 검증으로의 이동이다. 이 장은 그 이동이 어떤 축으로 나타나는지를 시스템 이름으로 정리한다.**

첫째 축은 검증기와의 결합이다. BFS-Prover-V2는 형식 검증 결과를 강화학습 보상으로 써서 miniF2F 95.08%를 보고했고, Robin은 가설-실험-해석 루프의 끝에 습식 실험을 두어 후보를 확인했다. 검증기가 생성기를 훈련하고 걸러낸다.

둘째 축은 평가물의 감사다. Ground False는 ProofNet 전 항목을 수작업으로 감사해 56%가 불충실하고 그중 절반 이상이 수학적으로 거짓임을 보였다. QEDBench는 일곱 채점자와 인간 전문가 1,000시간 이상으로 채점자의 점수 부풀림을 수치화했다. 벤치마크가 곧 연구 대상이다.[2][3]

셋째 축은 통계화다. The Leaderboard Lottery는 점추정 1위 선정을 사후 선택 추론 문제로 규정했다. 그 결과 순위 대신 순위 신뢰구간과 표본 해상도를 요구해야 한다는 정책이 따라온다. YC-Bench와 ToRR는 장기 운영과 형식 변화라는 적대적 조건에서 에이전트와 모델의 취약성을 재서 평가의 폭을 넓혔다.[4][5]

넷째 축은 닫힌 고리다. MatterGen은 합성 가능성을 목표함수에 넣었고, Polybot은 자율 실험으로 소재 합성의 고리를 닫았다. 생성 결과가 합성과 재분석으로 확인될 때 비로소 자산이 된다. 마지막으로 임상과 정책 영역에서는 기권과 위험 상한이 평가 기준으로 올라왔다.

여섯 축을 관통하는 원리는 하나다. 주장의 가치는 그 주장을 반증할 수 있는 장치의 품질에 비례한다. 장치가 약하면 도구가 공개되어 있어도 격차를 만들지 못한다.

> [!tip] 정리
> 검증 전환은 유행이 아니라 구조다. 생성이 값싸질수록 검증기를 가진 쪽의 프리미엄은 커진다. 국내에서는 이 여섯 축을 조직의 체크리스트로 바꿔 도입 심사에 쓰는 것이 가장 낮은 비용의 첫걸음이다. 검증기가 있는지, 베이스라인이 있는지, 독립 재현이 있는지 세 가지만 물어도 대부분의 과장이 걸러진다. 이 장의 시스템 이름은 이후 본문 장에서 각각 해당 서브카테고리의 근거로 다시 등장한다.

**레퍼런스** (제목 클릭 → 논문 리뷰)

1. [Robin: A multi-agent system for automating scientific discovery](../../docs/papers/10726_robin_a_multi-agent_system_for_automating_scientific_d/index.html) — Ali E. Ghareeb 외, 2026.05 · 인용 50
2. [Ground False: Dissecting Errors in Formal Mathematics Benchmarks](../../docs/papers/9759_Ground_False_Dissecting_Errors_in_Formal_Mathematics_Benchma/index.html) — One An 외, 2026 · 인용 159
3. [QEDBench: Quantifying the Alignment Gap in Automated Evaluation of University-Level Mathematical Proofs](../../docs/papers/10280_QEDBench_Quantifying_the_Alignment_Gap_in_Automated_Evaluati/index.html) — Santiago Gonzalez 외, 2026
4. [The Leaderboard Lottery: Why Top LLM Rankings Are Often Coin Flips, and How to Fix Them](../../docs/papers/10572_The_Leaderboard_Lottery_Why_Top_LLM_Rankings_Are_Often_Coin/index.html) — Shourya Vir Jain, 2026
5. [YC-Bench: Benchmarking AI Agents for Long-Term Planning and Consistent Execution](../../docs/papers/3398_YC-Bench_Benchmarking_AI_Agents_for_Long-Term_Planning_and_C/index.html) — Muyu He 외, 2026 · 인용 1,873
6. [The mighty torr: A benchmark for table reasoning and robustness](../../docs/papers/802_The_mighty_torr_A_benchmark_for_table_reasoning_and_robustne/index.html) — Shir Ashury-Tahan 외, 2025

---

## S58 · 그래서 무엇을 할 것인가

*종합* · *마무리*

> [!abstract] 화면에 띄울 한 줄
> 국내 연구기관·기업은 생성 경쟁에서 한 발 물러나 검증 인프라를 먼저 세워야 한다.

**분석의 결론은 행동으로 닫아야 한다. 국내 연구기관과 기업이 코퍼스의 증거에서 끌어낼 수 있는 과제는 다섯 가지다.**

첫째는 검증기 우선 투자다. BFS-Prover-V2가 형식 검증을 보상으로 쓰고 Robin이 습식 실험으로 후보를 확인한 방식은 능력이 아니라 구조를 보여 준다. 에이전트 도입 예산의 일부를 검증기와 재현 하네스에 먼저 배정해야 한다.

둘째는 내부 감사 체계다. Ground False와 QEDBench가 보여 주듯 공개 벤치마크도 틀린다. 자체 데이터로 단순 베이스라인과 불충실 사례를 가려내는 평가셋을 갖추면 외부 주장을 걸러내는 눈이 생긴다. 단일세포 모델 도입 시 자체 섭동 실험 데이터가 그 역할을 한다.

셋째는 데이터 자산화다. MLIP와 생성 소재 모델은 공개돼 있어 차별점은 DFT 학습 데이터와 독립 재분석에 있다. 넷째는 통계 문화다. 조달·선정 보고서에 순위 신뢰구간을 요구하고, 통계 인력을 보조가 아닌 검증 인프라 팀으로 세운다.

다섯째는 제도 선점이다. AI 저자성, 기여도 공개, 자율 실험실 안전은 아직 합의된 기준이 없다. 표준이 만들어지는 시기에 참여하면 규칙을 따르는 쪽이 아니라 쓰는 쪽에 선다.

실행 순서도 제안한다. 비용이 가장 낮고 효과가 즉시 나는 것은 통계 보고 규칙과 베이스라인 의무 비교이고, 중기 과제는 검증기와 내부 평가셋 구축, 장기 과제는 데이터 자산화와 거버넌스 참여다. 앞 단계가 뒤 단계의 신뢰 기반이 된다. 마지막으로 주의할 점이 있다. 다섯 과제는 서로 대체재가 아니다. 검증기만 세우고 데이터가 없으면 검증할 대상이 약하고, 데이터만 쌓고 통계 규율이 없으면 성능 주장이 다시 부풀려진다. 최소한 하나씩 착수해 서로를 보완하게 해야 한다.

**관전 포인트 (다음 12개월)**

- 형식 검증기를 결합한 AI 과학자가 증명 외 영역(물리·화학)에서 독립 재현을 통과하는가
- LLM 채점자의 아첨과 형식화 불충실을 줄이는 감사 표준이 자리잡는가
- 리더보드가 신뢰구간 보고를 의무화하는 방향으로 바뀌는가
- 자율 실험실의 안전·귀속 기준이 학술지·연구비 기관의 정책으로 명문화되는가

> [!tip] 정리
> 다섯 과제는 모두 검증이라는 한 축으로 모인다. 지금 투자한 검증 역량은 어떤 모델이 다음에 나오더라도 이전된다. 실행 주체는 연구기관과 기업이 다르다. 연구기관은 평가셋과 표준 논의에, 기업은 검증 파트너십과 데이터 자산화에 무게를 두는 분업이 현실적이다. 각 과제는 12개월 안에 점검 가능한 산출물, 예컨대 내부 평가셋, 보고 양식, 파트너 협약으로 정의해야 실행 여부를 확인할 수 있다.

---

## 부록 · 전체 레퍼런스 395편

- [3DMedAgent: Unified Perception-to-Understanding for 3D Medical Analysis](../../docs/papers/9139_3DMedAgent_Unified_Perception-to-Understanding_for_3D_Medica/index.html) — Ziyue Wang 외, 2026
- [A Fairness Audit of Medical Imaging Foundation Models on a Multimodal Structured Clinical Benchmark](../../docs/papers/9147_A_Fairness_Audit_of_Medical_Imaging_Foundation_Models_on_a_M/index.html) — Milan Mohan 외, 2026
- [A New Paradigm for Computational Chemistry](../../docs/papers/2995_A_New_Paradigm_for_Computational_Chemistry/index.html) — Raphael T. Husistein 외, 2026.04 · 인용 1
- [A Physics-Informed Chemical Rule for Topological Materials Discovery](../../docs/papers/1104_A_Physics-Informed_Chemical_Rule_for_Topological_Materials_D/index.html) — Xinyu Xu 외, 2026
- [A Synergistic Approach: Dynamics-AI Ensemble in Tropical Cyclone Forecasting](../../docs/papers/2996_A_Synergistic_Approach_Dynamics-AI_Ensemble_in_Tropical_Cycl/index.html) — 2026.02 · 인용 27
- [A collaborative constrained graph diffusion model for the generation of realistic synthetic molecules](../../docs/papers/2984_A_collaborative_constrained_graph_diffusion_model_for_the_ge/index.html) — Manuel Ruiz-Botella 외, 2026.05 · 인용 3
- [A flexible and affordable self-driving laboratory for automated reaction optimization](../../docs/papers/2989_A_flexible_and_affordable_self-driving_laboratory_for_automa/index.html) — Simone Pilon 외, 2026.04 · 인용 13
- [A survey of large language models](../../docs/papers/026_A_survey_of_large_language_models/index.html) — Wayne Xin Zhao 외, 2026.12 · 인용 114
- [AI Co-Mathematician: Accelerating Mathematicians with Agentic AI](../../docs/papers/3014_AI_Co-Mathematician_Accelerating_Mathematicians_with_Agentic/index.html) — Daniel Zheng 외, 2026.05 · 인용 633
- [AI scientists produce results without reasoning scientifically](../../docs/papers/9108_ai_scientists_produce_results_without_reasoning_scienti/index.html) — Martiño Ríos-García 외, 2026 · 인용 342
- [AI-Assisted Peer Review at Scale: The AAAI-26 AI Review Pilot](../../docs/papers/10928_AI-Assisted_Peer_Review_at_Scale_The_AAAI-26_AI_Review_Pilot/index.html) — Joydeep Biswas 외, 2026.04 · 인용 1
- [AMDAT: An Open-Source Molecular Dynamics Analysis Toolkit for Supercooled Liquids, Glass-Forming Materials, and Complex Fluids](../../docs/papers/095_AMDAT_An_Open-Source_Molecular_Dynamics_Analysis_Toolkit_for/index.html) — Pierre Kawak 외, 2026.02 · 인용 5
- [AMR-Bench-mini: A Diagnostic Benchmark for Agentic Mechanistic AMR Reasoning under Evidence Insufficiency](../../docs/papers/9239_AMR-Bench-mini_A_Diagnostic_Benchmark_for_Agentic_Mechanisti/index.html) — Ali Ihsan Nergiz 외, 2026 · 인용 2,475
- [AQVolt26: High-Temperature r²SCAN Halide Dataset for Universal ML Potentials and Solid-State Batteries](../../docs/papers/3023_AQVolt26_High-Temperature_r²SCAN_Halide_Dataset_for_Universa/index.html) — 2026.04 · 인용 1,079
- [Accelerating Scientific Research with Gemini in the Real-World](../../docs/papers/10911_accelerating_scientific_research_with_gemini_in_the_re/index.html) — Samuel Schmidgall 외, 2026.08
- [Accelerating scientific discovery with Co-Scientist](../../docs/papers/3001_Accelerating_scientific_discovery_with_Co-Scientist/index.html) — Juraj Gottweis 외, 2026.05 · 인용 97
- [Act or Defer: Error-Controlled Decision Policies for EHR Foundation Models](../../docs/papers/9176_Act_or_Defer_Error-Controlled_Decision_Policies_for_EHR_Foun/index.html) — Intae Moon 외, 2026
- [Active Policy Optimization for Individualized Dosing via Gradient Variance Minimization](../../docs/papers/9179_Active_Policy_Optimization_for_Individualized_Dosing_via_Gra/index.html) — Yi Wan 외, 2026
- [Advancing operational global aerosol forecasting with machine learning](../../docs/papers/3006_Advancing_operational_global_aerosol_forecasting_with_machin/index.html) — Ke Gui 외, 2026.03 · 인용 7
- [AgentPLM: Agentic Protein Language Models with Reasoning-Augmented Decoding for Protein Sequence Design](../../docs/papers/9214_AgentPLM_Agentic_Protein_Language_Models_with_Reasoning-Augm/index.html) — Sahil Rahman 외, 2026 · 인용 1,186
- [Agentic LLM Reasoning in a Self-Driving Laboratory for Air-Sensitive Lithium Halide Spinel Conductors](../../docs/papers/3011_Agentic_LLM_Reasoning_in_a_Self-Driving_Laboratory_for_Air-S/index.html) — Yuxing Fei 외, 2026.04 · 인용 5
- [Agentic Systems for Sample-Efficient Drug Formulation Design](../../docs/papers/9213_Agentic_Systems_for_Sample-Efficient_Drug_Formulation_Design/index.html) — Michael Craig 외, 2026 · 인용 5,395
- [Alignment between Brains and AI: Evidence for Convergent Evolution across Modalities, Scales and Training Trajectories](../../docs/papers/9231_Alignment_between_Brains_and_AI_Evidence_for_Convergent_Evol/index.html) — Guobin Shen 외, 2026
- [AlloyVAE: A Generative Model for Complex Probabilistic Field-to-Field Relationships in Alloys](../../docs/papers/3018_AlloyVAE_A_Generative_Model_for_Complex_Probabilistic_Field-/index.html) — 2026.04
- [Anytime-Valid Confirmation of Label-Shift Corrections](../../docs/papers/9249_Anytime-Valid_Confirmation_of_Label-Shift_Corrections/index.html) — Seungjin Choi, 2026
- [Anytime-Valid Hypothesis Testing for Sparse Autoencoder Feature Validation](../../docs/papers/9250_Anytime-Valid_Hypothesis_Testing_for_Sparse_Autoencoder_Feat/index.html) — Rudransh Khera, 2026 · 인용 675
- [Are Non-BPE Tokenizers Ready to Improve LLM Numeracy?](../../docs/papers/9255_Are_Non-BPE_Tokenizers_Ready_to_Improve_LLM_Numeracy/index.html) — Yizhan Huang 외, 2026
- [Artificial intelligence tools expand scientists’ impact but contract science’s focus](../../docs/papers/107_Artificial_intelligence_tools_expand_scientists_impact_but_c/index.html) — Qianyue Hao 외, 2026.01 · 인용 105
- [Assessing Emulator Design and Training for Modal Aerosol Microphysics Parameterizations in E3SMv2](../../docs/papers/3026_Assessing_Emulator_Design_and_Training_for_Modal_Aerosol_Mic/index.html) — 2026.04
- [Auditing LLM Jailbreak Detectors as Hypothesis Tests: Permutation P-values and Type-I Error Control via Paraphrase Exchangeability](../../docs/papers/9270_Auditing_LLM_Jailbreak_Detectors_as_Hypothesis_Tests_Permuta/index.html) — Vishal Narender Punjabi, 2026
- [Auditing Sybil: Explaining Deep Lung Cancer Risk Prediction Through Generative Interventional Attributions](../../docs/papers/9271_Auditing_Sybil_Explaining_Deep_Lung_Cancer_Risk_Prediction_T/index.html) — Bartlomiej Sobieski 외, 2026
- [Author Correction: An autonomous laboratory for the accelerated synthesis of inorganic materials](../../docs/papers/10931_Author_Correction_An_autonomous_laboratory_for_the_accelerat/index.html) — Nathan J. Szymanski 외, 2026.02 · 인용 5
- [Autoregressive EHR Foundation Models with Multimodal Inputs](../../docs/papers/9284_Autoregressive_EHR_Foundation_Models_with_Multimodal_Inputs/index.html) — Yuxuan Liu 외, 2026 · 인용 60
- [Awakening the Sleeping Agent: Lean-Specific Agentic Data Reactivates General Tool Use in Goedel Prover](../../docs/papers/9286_Awakening_the_Sleeping_Agent_Lean-Specific_Agentic_Data_Reac/index.html) — Jui-Hui Chung 외, 2026
- [Behavior Is Not Representation: Hypothesis Tests for Concept Steering in LLMs](../../docs/papers/9300_Behavior_Is_Not_Representation_Hypothesis_Tests_for_Concept/index.html) — Siddharth Shukla, 2026
- [Benchmarking Universal Machine-Learned Interatomic Potentials for High-Temperature Metal-Organic Framework Chemistry](../../docs/papers/3038_Benchmarking_Universal_Machine-Learned_Interatomic_Potential/index.html) — Connor W. Edwards 외, 2026.04
- [Benchmarking self-driving labs](../../docs/papers/10935_Benchmarking_self-driving_labs/index.html) — Adedire D. Adesiji 외, 2026 · 인용 11
- [BioToken and BioFM – Biologically-Informed Tokenization Enables Accurate and Efficient Genomic Foundation Models](../../docs/papers/9340_BioToken_and_BioFM__Biologically-Informed_Tokenization_Enabl/index.html) — Aleksandr Medvedev 외, 2026
- [Born-Qualified: An Autonomous Framework for Deploying Advanced Energy and Electronic Materials](../../docs/papers/3047_Born-Qualified_An_Autonomous_Framework_for_Deploying_Advance/index.html) — Steven R. Spurgeon 외, 2026.05 · 인용 184
- [BrainJanus: A Unified Model for Understanding and Generation across Brain, Vision, and Language](../../docs/papers/9354_BrainJanus_A_Unified_Model_for_Understanding_and_Generation/index.html) — Haitao Wu 외, 2026
- [Bridging Gene Regulatory Networks and Causal Representation Learning in Single-Cell Genomics Data](../../docs/papers/9358_Bridging_Gene_Regulatory_Networks_and_Causal_Representation/index.html) — Vincenzo Lagani 외, 2026 · 인용 3,730
- [Bridging the Gap Between Climate Science and Machine Learning in Climate Model Emulation](../../docs/papers/3049_Bridging_the_Gap_Between_Climate_Science_and_Machine_Learnin/index.html) — 2026.03
- [BrokenMath: A Benchmark for Sycophancy in Theorem Proving with LLMs](../../docs/papers/9359_BrokenMath_A_Benchmark_for_Sycophancy_in_Theorem_Proving_wit/index.html) — Ivo Petrov 외, 2026
- [CIDER: Conformal Information-Directed Agents for Low-Budget Protein Engineering](../../docs/papers/9400_CIDER_Conformal_Information-Directed_Agents_for_Low-Budget_P/index.html) — Rishabh Bhattacharya, 2026 · 인용 6,121
- [CINOC: Cardinality-Invariant Neural Operator Policies for Scalable PDE Control](../../docs/papers/9401_CINOC_Cardinality-Invariant_Neural_Operator_Policies_for_Sca/index.html) — Pietro Zanotta 외, 2026
- [CITE: Anytime-Valid Statistical Inference in LLM Self-Consistency](../../docs/papers/9402_CITE_Anytime-Valid_Statistical_Inference_in_LLM_Self-Consist/index.html) — Hirofumi Ota 외, 2026
- [Can Vision Language Models Learn Intuitive Physics from Interaction?](../../docs/papers/9373_Can_Vision_Language_Models_Learn_Intuitive_Physics_from_Inte/index.html) — Luca M. Schulze Buschoff 외, 2026
- [Cardio-mmFlow: A Gaussian-Prior-Free Physics-Informed Flow Matching Framework for Electrocardiogram to mmWave Radar Synthesis](../../docs/papers/9376_Cardio-mmFlow_A_Gaussian-Prior-Free_Physics-Informed_Flow_Ma/index.html) — Ziyang LIU 외, 2026 · 인용 17
- [Celcomen: spatial causal disentanglement for single-cell and tissue perturbation modeling](../../docs/papers/3051_Celcomen_spatial_causal_disentanglement_for_single-cell_and/index.html) — Stathis Megas 외, 2026.03 · 인용 8
- [Cocoa: Co-planning and co-execution with AI Agents](../../docs/papers/229_Cocoa_Co-planning_and_co-execution_with_ai_agents/index.html) — K. J. Kevin Feng 외, 2026 · 인용 6
- [Component-Wise Composite Likelihood Distillation for Censored Time-to-Event Data](../../docs/papers/9420_Component-Wise_Composite_Likelihood_Distillation_for_Censore/index.html) — Feiyang Deng 외, 2026
- [Compressing the Validation Bottleneck: An Agentic Self-Driving Lab for Scientific Discover](../../docs/papers/9421_Compressing_the_Validation_Bottleneck_An_Agentic_Self-Drivin/index.html) — Kyunghoon Hur 외, 2026 · 인용 36
- [Counting Cycles with AI](../../docs/papers/9449_Counting_Cycles_with_AI/index.html) — Jiashun Jin 외, 2026 · 인용 450
- [Coupled Training with Privileged Information and Unlabeled Data](../../docs/papers/9454_Coupled_Training_with_Privileged_Information_and_Unlabeled_D/index.html) — Jiahao Shi 외, 2026
- [Credit Where Credit Is Due: A Taxonomy of AI Contributions to Scientific Discovery and Recommendations for Authorship Policy](../../docs/papers/9459_Credit_Where_Credit_Is_Due_A_Taxonomy_of_AI_Contributions_to/index.html) — Luiz Felipe Caparelli Piochi, 2026 · 인용 678
- [CreditMap: Provenance Ledgers for Attribution in Human--AI Scientific Collaboration](../../docs/papers/9460_CreditMap_Provenance_Ledgers_for_Attribution_in_Human--AI_Sc/index.html) — Aayam Bansal 외, 2026 · 인용 401
- [CupOFLATTE: Coupled Objective-Guided Discrete Flows via Linker Assembly for Targeted PROTAC Engineering](../../docs/papers/9468_CupOFLATTE_Coupled_Objective-Guided_Discrete_Flows_via_Linke/index.html) — Ziang Li 외, 2026 · 인용 157
- [DCDM-ECG: Demographic-Conditional Diffusion Model for 12-Lead ECG Generation](../../docs/papers/9479_DCDM-ECG_Demographic-Conditional_Diffusion_Model_for_12-Lead/index.html) — Benedikt Kolbeinsson 외, 2026
- [DNACHUNKER: Learnable Tokenization for DNA Language Models](../../docs/papers/9536_DNACHUNKER_Learnable_Tokenization_for_DNA_Language_Models/index.html) — Taewon Kim 외, 2026 · 인용 11
- [DP-SPRT: Differentially Private Sequential Probability Ratio Tests](../../docs/papers/9544_DP-SPRT_Differentially_Private_Sequential_Probability_Ratio/index.html) — Thomas Michel 외, 2026
- [Data integrity in materials science in the era of AI: balancing accelerated discovery with responsible science and innovation](../../docs/papers/252_Data_integrity_in_materials_science_in_the_era_of_AI_balanci/index.html) — Nik Reeves-McLaren 외, 2026 · 인용 11
- [Data-driven construction of machine-learning-based interatomic potentials for gas-surface scattering dynamics: the case of NO on graphite](../../docs/papers/3066_Data-driven_construction_of_machine-learning-based_interatom/index.html) — 2026.03 · 인용 9
- [Deadline-Valid Replay: Anytime-Valid Testing for LLM Inference Policies](../../docs/papers/9482_Deadline-Valid_Replay_Anytime-Valid_Testing_for_LLM_Inferenc/index.html) — Rui Gao, 2026 · 인용 74
- [Debate2Create: Robot Co-design via Multi-Agent LLM Debate](../../docs/papers/9483_Debate2Create_Robot_Co-design_via_Multi-Agent_LLM_Debate/index.html) — Kevin Qiu 외, 2026
- [Deep Ensemble Graph Neural Networks for Probabilistic Cosmic-Ray Direction and Energy Reconstruction](../../docs/papers/3069_Deep_Ensemble_Graph_Neural_Networks_for_Probabilistic_Cosmic/index.html) — 2026.02 · 인용 66
- [DeepBlip: Estimating Conditional Average Treatment Effects Over Time](../../docs/papers/9495_DeepBlip_Estimating_Conditional_Average_Treatment_Effects_Ov/index.html) — Haorui Ma 외, 2026
- [Di-BiLPS: Denoising induced Bidirectional Latent-PDE-Solver under Sparse Observations](../../docs/papers/9511_Di-BiLPS_Denoising_induced_Bidirectional_Latent-PDE-Solver_u/index.html) — Zhonghao Li 외, 2026 · 인용 2
- [DiffResearch: Harnessing Diffusion Language Models for Automated Literature Review](../../docs/papers/9515_DiffResearch_Harnessing_Diffusion_Language_Models_for_Automa/index.html) — Alan-Barsag Gazzaev 외, 2026
- [DiffSyn: a generative diffusion approach to materials synthesis planning](../../docs/papers/3077_DiffSyn_a_generative_diffusion_approach_to_materials_synthes/index.html) — Elton Pan 외, 2026.02 · 인용 6
- [Discrete Survival Knowledge Distillation for Competing Risks Analysis](../../docs/papers/9522_Discrete_Survival_Knowledge_Distillation_for_Competing_Risks/index.html) — Feiyang Deng 외, 2026
- [Distilling Tabular Foundation Models for Structured Health Data](../../docs/papers/9527_Distilling_Tabular_Foundation_Models_for_Structured_Health_D/index.html) — Aditya Tanna 외, 2026 · 인용 8,430
- [Distinguishing Imitation Error from Intrinsic Motion Learning Difficulty](../../docs/papers/9528_Distinguishing_Imitation_Error_from_Intrinsic_Motion_Learnin/index.html) — Zhaorui Meng 외, 2026 · 인용 428
- [Diversity Over Frequency: Rethinking Tool Use in Visual Chain-of-Thought Agents](../../docs/papers/9531_Diversity_Over_Frequency_Rethinking_Tool_Use_in_Visual_Chain/index.html) — Dong-Hee Kim 외, 2026
- [Do Androids Dream of Breaking the Game? Systematically Auditing AI Agent Benchmarks with BenchJack](../../docs/papers/10951_Do_Androids_Dream_of_Breaking_the_Game_Systematically_Auditi/index.html) — Hao Wang 외, 2026.05
- [EMFormer: Efficient Multi-Scale Transformer for Accumulative Context Weather Forecasting](../../docs/papers/9580_EMFormer_Efficient_Multi-Scale_Transformer_for_Accumulative/index.html) — Hao Chen 외, 2026
- [EO-Agents: A Three-Agent LLM Pipeline for Earth Observation Hypothesis Generation](../../docs/papers/9588_EO-Agents_A_Three-Agent_LLM_Pipeline_for_Earth_Observation_H/index.html) — Mahyar Ghazanfari 외, 2026
- [Embodied Science: Closing the Discovery Loop with Agentic Embodied AI](../../docs/papers/310_Embodied_Science_Closing_the_Discovery_Loop_with_Agentic_Emb/index.html) — Xiang Zhuang 외, 2026.03
- [Empirical-Distribution Matching for Synthetic ECG Classification](../../docs/papers/9582_Empirical-Distribution_Matching_for_Synthetic_ECG_Classifica/index.html) — Benedikt Kolbeinsson 외, 2026
- [Evaluating out of distribution generalization of protein language models](../../docs/papers/9606_Evaluating_out_of_distribution_generalization_of_protein_lan/index.html) — Kumaresh Krishnan 외, 2026 · 인용 5
- [FHIR-Hopper: A Neuro-Symbolic Agent for Reasoning over EHRs](../../docs/papers/9645_FHIR-Hopper_A_Neuro-Symbolic_Agent_for_Reasoning_over_EHRs/index.html) — Chanwoo Kim 외, 2026 · 인용 104
- [FIPO-Prover: Formalization-Oriented Informal Proof Optimization for Efficient Formal Theorem Proving](../../docs/papers/9650_FIPO-Prover_Formalization-Oriented_Informal_Proof_Optimizati/index.html) — Jingkun Ma 외, 2026
- [FIRSTPASS: A Multi-Domain, Multi-Round Peer Review Dataset Grounded in Real Editorial Outcomes](../../docs/papers/9652_FIRSTPASS_A_Multi-Domain_Multi-Round_Peer_Review_Dataset_Gro/index.html) — Prabhjot Singh 외, 2026
- [FUSE: FK-Steered Multi-Modal Flow Matching for Efficient Simulation-Based Posterior Estimation](../../docs/papers/9710_FUSE_FK-Steered_Multi-Modal_Flow_Matching_for_Efficient_Simu/index.html) — Weichen Qin 외, 2026 · 인용 994
- [FloeNet: A mass-conserving global sea ice emulator that generalizes across climates](../../docs/papers/3105_FloeNet_A_mass-conserving_global_sea_ice_emulator_that_gener/index.html) — 2026.03
- [FormalRx: Rectify and eXamine Semantic Failures in Autoformalization](../../docs/papers/9675_FormalRx_Rectify_and_eXamine_Semantic_Failures_in_Autoformal/index.html) — Haocheng Wang 외, 2026
- [Formalizing Numerical Analysis: An Agent Pipeline and Quality Audit Beyond Kernel Acceptance](../../docs/papers/9671_Formalizing_Numerical_Analysis_An_Agent_Pipeline_and_Quality/index.html) — Theodore Meek 외, 2026 · 인용 6
- [Formalizing Scarf, Brouwer, and Nash in Lean](../../docs/papers/9672_Formalizing_Scarf_Brouwer_and_Nash_in_Lean/index.html) — Lyu Yuwei 외, 2026 · 인용 159
- [From Kepler to Newton: Inductive Biases Guide Learned World Models in Transformers](../../docs/papers/9696_From_Kepler_to_Newton_Inductive_Biases_Guide_Learned_World_M/index.html) — Ziming Liu 외, 2026 · 인용 12
- [From single-sequences to evolutionary trajectories: protein language models capture the evolutionary potential of SARS-CoV-2](../../docs/papers/3109_From_single-sequences_to_evolutionary_trajectories_protein_l/index.html) — Kieran D. Lamb 외, 2026.02 · 인용 7
- [FunCQNet: A Functional Censored Quantile Neural Network for Predicting Long-Term Post-Transplant Kidney Survival](../../docs/papers/9706_FunCQNet_A_Functional_Censored_Quantile_Neural_Network_for_P/index.html) — Jiaqi Men 외, 2026
- [GOAgent: Tool-Orchestrating Language Agents for Protein Function Annotation](../../docs/papers/9749_GOAgent_Tool-Orchestrating_Language_Agents_for_Protein_Funct/index.html) — Manvitha Ponnapati 외, 2026 · 인용 518
- [GRAIL: Gradient-Reweighted Advantages for Reinforcement Learning with Verifiable Rewards](../../docs/papers/9755_GRAIL_Gradient-Reweighted_Advantages_for_Reinforcement_Learn/index.html) — Tej Deep Pala 외, 2026 · 인용 56
- [Gauge-Equivariant Graph Neural Networks for Lattice Gauge Theories](../../docs/papers/3111_Gauge-Equivariant_Graph_Neural_Networks_for_Lattice_Gauge_Th/index.html) — 2026.04
- [GenDA: Generative Data Assimilation on Complex Urban Areas via Classifier-Free Diffusion Guidance](../../docs/papers/9717_GenDA_Generative_Data_Assimilation_on_Complex_Urban_Areas_vi/index.html) — Francisco Giral 외, 2026
- [General-Purpose Machine-Learned Potential for CrCoNi Alloys Enabling Large-Scale Atomistic Simulations with First-Principles Accuracy](../../docs/papers/372_General-Purpose_Machine-Learned_Potential_for_CrCoNi_Alloys/index.html) — Yong-Chao Wu 외, 2026.03
- [Generative AI and the Foundation Model Era: A Comprehensive Review](../../docs/papers/377_Generative_AI_and_the_Foundation_Model_Era_A_Comprehensive_R/index.html) — Abdussalam Elhanashi 외, 2026.03 · 인용 6
- [Generative Chemical Language Models for Energetic Materials Discovery](../../docs/papers/3114_Generative_Chemical_Language_Models_for_Energetic_Materials/index.html) — 2026.03
- [Generative Pipeline for Discovering Solid-State Battery Materials with Universal Atomistic Potentials](../../docs/papers/9727_Generative_Pipeline_for_Discovering_Solid-State_Battery_Mate/index.html) — Artem Dembitskiy 외, 2026 · 인용 139
- [Generative Structure Search for Efficient and Diverse Discovery of Molecular and Crystal Structures](../../docs/papers/3120_Generative_Structure_Search_for_Efficient_and_Diverse_Discov/index.html) — 2026.04
- [Generative design of inorganic materials](../../docs/papers/3115_Generative_design_of_inorganic_materials/index.html) — 2026.04 · 인용 10
- [Gradient-Based Causal Tree Ensembles: A Backbone Architecture for Heterogeneous Treatment Effects](../../docs/papers/9753_Gradient-Based_Causal_Tree_Ensembles_A_Backbone_Architecture/index.html) — Yusuke Kano 외, 2026
- [Graffiti3Loop: Generating and Resolving Formal Machine-Generated Graph Conjectures in a Loop](../../docs/papers/9754_Graffiti3Loop_Generating_and_Resolving_Formal_Machine-Genera/index.html) — William Hu 외, 2026 · 인용 208
- [Ground False: Dissecting Errors in Formal Mathematics Benchmarks](../../docs/papers/9759_Ground_False_Dissecting_Errors_in_Formal_Mathematics_Benchma/index.html) — One An 외, 2026 · 인용 159
- [HVR-Met: A Hypothesis-Verification-Replanning Agentic System for Extreme Weather Diagnosis](../../docs/papers/9798_HVR-Met_A_Hypothesis-Verification-Replanning_Agentic_System/index.html) — Shuo Tang 외, 2026
- [Hepa-RAFT: Retrieval-Augmented Virtual Hepatocyte Responses for Hepatotoxicity Prediction](../../docs/papers/9775_Hepa-RAFT_Retrieval-Augmented_Virtual_Hepatocyte_Responses_f/index.html) — Youngseok Choi 외, 2026 · 인용 2,624
- [How do Humans Process AI-generated Hallucination Contents: a Neuroimaging Study](../../docs/papers/9790_How_do_Humans_Process_AI-generated_Hallucination_Contents_a/index.html) — Shuqi Zhu 외, 2026
- [Human-AI Hybrid Mathematical Discovery Workflow: Unifying Ramanujan's 17 Series for 1/π](../../docs/papers/9796_Human-AI_Hybrid_Mathematical_Discovery_Workflow_Unifying_Ram/index.html) — Michael Shalyt 외, 2026 · 인용 46
- [HybridOM: Hybrid Physics-Based and Data-Driven Global Ocean Modeling with Efficient Regional Downscaling](../../docs/papers/9801_HybridOM_Hybrid_Physics-Based_and_Data-Driven_Global_Ocean_M/index.html) — Ruiqi Shu 외, 2026
- [IRIS: An Agentic Multi-Phase Framework for Automated Scientific Literature Review](../../docs/papers/9847_IRIS_An_Agentic_Multi-Phase_Framework_for_Automated_Scientif/index.html) — Sergey Kolchenko 외, 2026 · 인용 48
- [IVQA-LD: Inclusive Multimodal Understanding for Population with Limb Deficiency](../../docs/papers/9853_IVQA-LD_Inclusive_Multimodal_Understanding_for_Population_wi/index.html) — Yan Ke 외, 2026
- [InnoEval: On Research Idea Evaluation as a Knowledge-Grounded, Multi-Perspective Reasoning Problem](../../docs/papers/9833_InnoEval_On_Research_Idea_Evaluation_as_a_Knowledge-Grounded/index.html) — Shuofei Qiao 외, 2026
- [Interpreting Sepsis Prediction through Positional Explanation](../../docs/papers/9842_Interpreting_Sepsis_Prediction_through_Positional_Explanatio/index.html) — Chaehyeon Kim 외, 2026
- [Into the Unknown: Benchmarking AI agents on open scientific research problems](../../docs/papers/11482_Into_the_Unknown_Benchmarking_AI_agents_on_open_scientific_r/index.html) — Seungone Kim 외, 2026.10
- [Just Add Structure: Protein Language Models Combined with Structural Equivariance Excel at Protein Tasks](../../docs/papers/9859_Just_Add_Structure_Protein_Language_Models_Combined_with_Str/index.html) — Qurat ul ain 외, 2026 · 인용 16,139
- [Knockoff-C2ST: False Discovery Controlled Attribution of Distribution Shift](../../docs/papers/9863_Knockoff-C2ST_False_Discovery_Controlled_Attribution_of_Dist/index.html) — Şuayp Talha Kocabay 외, 2026 · 인용 113
- [LDARNet: DNA Adaptive Representation Network with Learnable Tokenization for Genomic Modeling](../../docs/papers/9884_LDARNet_DNA_Adaptive_Representation_Network_with_Learnable_T/index.html) — Daria Ledneva 외, 2026 · 인용 104
- [LabProc and Tacit: Quantifying the Visual-Textual Prior Gap in Autonomous Laboratory Perception](../../docs/papers/9870_LabProc_and_Tacit_Quantifying_the_Visual-Textual_Prior_Gap_i/index.html) — Jagrati Gogia 외, 2026
- [Latent-Y: A Lab-Validated Autonomous Agent for De Novo Antibody Design](../../docs/papers/3150_Latent-Y_A_Lab-Validated_Autonomous_Agent_for_De_Novo_Antibo/index.html) — Latent Labs Team 외, 2026.03
- [Lean Disprove: Certified Counterexample Search for AI-Assisted Formal Mathematics](../../docs/papers/9886_Lean_Disprove_Certified_Counterexample_Search_for_AI-Assiste/index.html) — Jan Ondras 외, 2026 · 인용 8
- [Learning Clinical-Trial Strategy: Offline Policy Training for Decision Agents](../../docs/papers/9900_Learning_Clinical-Trial_Strategy_Offline_Policy_Training_for/index.html) — William James Bolton 외, 2026
- [LieStoNet: Learning Lie Symmetries from Spatiotemporal Data for Stochastic Dynamical Systems](../../docs/papers/9943_LieStoNet_Learning_Lie_Symmetries_from_Spatiotemporal_Data_f/index.html) — Shida Liu 외, 2026
- [LitReview Arena: Evaluating Literature Review Agents with Battle-style Peer Review Platform](../../docs/papers/9953_LitReview_Arena_Evaluating_Literature_Review_Agents_with_Bat/index.html) — Ruotong Zhao 외, 2026 · 인용 210
- [LoPhyDA: Low-Rank Tensor and Physics Gradient Guided Diffusion for Atmospheric Data Assimilation](../../docs/papers/9971_LoPhyDA_Low-Rank_Tensor_and_Physics_Gradient_Guided_Diffusio/index.html) — Danyang Peng 외, 2026
- [Local Intrinsic Dimension of Representations Predicts Alignment and Generalization in AI Models and Human Brain](../../docs/papers/9964_Local_Intrinsic_Dimension_of_Representations_Predicts_Alignm/index.html) — Junjie Yu 외, 2026
- [MEDA: Medical-Oriented Activation Editing for Hallucination Mitigation in Medical Large Vision-Language Model](../../docs/papers/10006_MEDA_Medical-Oriented_Activation_Editing_for_Hallucination_M/index.html) — Tianbo Wang 외, 2026
- [MEG-XL: Data-Efficient Brain-to-Text via Long-Context Pre-Training](../../docs/papers/10019_MEG-XL_Data-Efficient_Brain-to-Text_via_Long-Context_Pre-Tra/index.html) — Dulhan Jayalath 외, 2026
- [MENO: MeanFlow-Enhanced Neural Operators for Dynamical Systems](../../docs/papers/3165_MENO_MeanFlow-Enhanced_Neural_Operators_for_Dynamical_System/index.html) — 2026.04 · 인용 1,051
- [MMClima: A Framework for Multimodal Climate Science Data and Evaluation](../../docs/papers/10042_MMClima_A_Framework_for_Multimodal_Climate_Science_Data_and/index.html) — Muhammad Umer Sheikh 외, 2026
- [MatDeplot: Agent-Ready Materials-Curve Understanding for Scientific Reasoning](../../docs/papers/9992_MatDeplot_Agent-Ready_Materials-Curve_Understanding_for_Scie/index.html) — Yin Liang 외, 2026
- [Med-Scout: Curing MLLMs' Geometric Blindness in Medical Perception via Geometry-Aware RL Post-Training](../../docs/papers/10004_Med-Scout_Curing_MLLMs_Geometric_Blindness_in_Medical_Percep/index.html) — Anglin Liu 외, 2026
- [Med-SegLens: Latent-Level Model Diffing for Interpretable Medical Image Segmentation](../../docs/papers/10005_Med-SegLens_Latent-Level_Model_Diffing_for_Interpretable_Med/index.html) — Salma J. Ahmed 외, 2026 · 인용 872
- [MedCRP-CL: Continual Medical Image Segmentation via Bayesian Nonparametric Semantic Modality Discovery](../../docs/papers/10009_MedCRP-CL_Continual_Medical_Image_Segmentation_via_Bayesian/index.html) — Ziyuan Gao, 2026
- [MedMIX: Modality-Internal Expert Fusion for Multimodal Medical Diagnosis](../../docs/papers/10014_MedMIX_Modality-Internal_Expert_Fusion_for_Multimodal_Medica/index.html) — Seungik Cho 외, 2026 · 인용 1,331
- [MedMamba: Multi-View State Space Models with Adaptive Graph Learning for Medical Time Series Classification](../../docs/papers/10012_MedMamba_Multi-View_State_Space_Models_with_Adaptive_Graph_L/index.html) — Da Zhang 외, 2026
- [MedREK: Retrieval-Based Editing for Medical LLMs with Key-Aware Prompts](../../docs/papers/10016_MedREK_Retrieval-Based_Editing_for_Medical_LLMs_with_Key-Awa/index.html) — Shujun Xia 외, 2026
- [Membership Circuits: Tractable Membership Testing via Probabilistic Circuits](../../docs/papers/10021_Membership_Circuits_Tractable_Membership_Testing_via_Probabi/index.html) — Bennet Wittelsbach 외, 2026
- [MerLean: An Agentic Framework for Autoformalization in Quantum Computation](../../docs/papers/532_MerLean_An_Agentic_Framework_for_Autoformalization_in_Quantu/index.html) — Yuanjie Ren 외, 2026.02 · 인용 9
- [MetaDNS: Enhancing Exploration in Discrete Neural Samplers via Metadynamics](../../docs/papers/10028_MetaDNS_Enhancing_Exploration_in_Discrete_Neural_Samplers_vi/index.html) — Xiaochen Du 외, 2026
- [Minimax-Optimal Kernel Two-sample Testing in Sub-quadratic Time](../../docs/papers/10034_Minimax-Optimal_Kernel_Two-sample_Testing_in_Sub-quadratic_T/index.html) — Ikjun Choi 외, 2026
- [Missingness-Aware Conformal Prediction Under Cross-Hospital Distribution Shift](../../docs/papers/10036_Missingness-Aware_Conformal_Prediction_Under_Cross-Hospital/index.html) — Liang You 외, 2026
- [Mitigating Gradient Pathology in PINNs through Aligned Constraint](../../docs/papers/10037_Mitigating_Gradient_Pathology_in_PINNs_through_Aligned_Const/index.html) — Yichen Luo 외, 2026
- [Mitigating Perceptual Judgment Bias in Multimodal LLM-as-a-Judge for Mathematical and Scientific Reasoning Evaluation](../../docs/papers/10038_Mitigating_Perceptual_Judgment_Bias_in_Multimodal_LLM-as-a-J/index.html) — Seojeong Park 외, 2026
- [Model Collapse Despite Ground-Truth Verification](../../docs/papers/10048_Model_Collapse_Despite_Ground-Truth_Verification/index.html) — Shuo Li Liu, 2026
- [MolOpt-Eval: Can Frontier LLMs Perform Structure-Based Hit-to-Lead Optimization?](../../docs/papers/10057_MolOpt-Eval_Can_Frontier_LLMs_Perform_Structure-Based_Hit-to/index.html) — Chengzhu Li 외, 2026
- [Molecular Dynamics Simulations of Al-Ti Metallic Alloy Melts Using a Transferable Machine-Learning Potential](../../docs/papers/3174_Molecular_Dynamics_Simulations_of_Al-Ti_Metallic_Alloy_Melts/index.html) — Yuna Kato 외, 2026.04
- [Multi-Scale Flow Matching for Continuous-time Generative Modeling of Spatiotemporal Tissue Dynamics from Spatial Transcriptomics](../../docs/papers/10069_Multi-Scale_Flow_Matching_for_Continuous-time_Generative_Mod/index.html) — Pinar Demetci 외, 2026 · 인용 1,884
- [Multi-View Causal Discovery without Non-Gaussianity: Identifiability and Algorithms](../../docs/papers/10071_Multi-View_Causal_Discovery_without_Non-Gaussianity_Identifi/index.html) — Ambroise Heurtebise 외, 2026
- [Multimarginal flow matching with optimal transport potentials](../../docs/papers/10073_Multimarginal_flow_matching_with_optimal_transport_potential/index.html) — Raghav Kansal 외, 2026
- [Multimodal Scaling Laws for Task & Data-Optimized Models of Visual Cortex](../../docs/papers/10076_Multimodal_Scaling_Laws_for_Task__Data-Optimized_Models_of_V/index.html) — Abdulkadir Gokce 외, 2026
- [NEAR-SSB: Noisy ECG Artifact Removal via Spectral Schrodinger Bridge](../../docs/papers/10084_NEAR-SSB_Noisy_ECG_Artifact_Removal_via_Spectral_Schrodinger/index.html) — Beom Kim 외, 2026
- [NeurOCNN: A Neural-Operator-Based Model for Physiological Time Series](../../docs/papers/10103_NeurOCNN_A_Neural-Operator-Based_Model_for_Physiological_Tim/index.html) — Daya Kumar 외, 2026
- [Neural Ensemble Kalman Filter: Data Assimilation for Compressible Flows with Shocks](../../docs/papers/3187_Neural_Ensemble_Kalman_Filter_Data_Assimilation_for_Compress/index.html) — 2026.02 · 인용 1
- [Neural Modular Physics for Elastic Simulation](../../docs/papers/10093_Neural_Modular_Physics_for_Elastic_Simulation/index.html) — Yifei Li 외, 2026 · 인용 560
- [Neural Quantum States in Mixed Precision](../../docs/papers/10094_Neural_Quantum_States_in_Mixed_Precision/index.html) — Massimo Solinas 외, 2026
- [Neural-HSS: Hierarchical Semi-Separable Neural PDE Solver](../../docs/papers/10096_Neural-HSS_Hierarchical_Semi-Separable_Neural_PDE_Solver/index.html) — Pietro Sittoni 외, 2026
- [NeuriCo: Towards reliable AI scientists](../../docs/papers/10098_NeuriCo_Towards_reliable_AI_scientists/index.html) — Haokun Liu 외, 2026 · 인용 144
- [NeuronCtrl: Geometry-Aware Safe Closed-Loop Generative Control for Neuronal Microenvironment Dynamics](../../docs/papers/10104_NeuronCtrl_Geometry-Aware_Safe_Closed-Loop_Generative_Contro/index.html) — Haowei Xu 외, 2026
- [Neutron and X-ray Diffraction Reveal the Limits of Long-Range Machine Learning Potentials for Medium-Range Order in Silica Glass](../../docs/papers/3190_Neutron_and_X-ray_Diffraction_Reveal_the_Limits_of_Long-Rang/index.html) — 2026.04
- [Numina-Lean-Agent: An Open and General Agentic Reasoning System for Formal Mathematics](../../docs/papers/10115_Numina-Lean-Agent_An_Open_and_General_Agentic_Reasoning_Syst/index.html) — Junqi Liu 외, 2026
- [ORBIT: A Prognostic World Model for Ocular Reasoning Based on Imagined Trajectories](../../docs/papers/10145_ORBIT_A_Prognostic_World_Model_for_Ocular_Reasoning_Based_on/index.html) — Jiangtao Yan 외, 2026
- [OSF: On Pre-training and Scaling of Sleep Foundation Models](../../docs/papers/10148_OSF_On_Pre-training_and_Scaling_of_Sleep_Foundation_Models/index.html) — Zitao Shuai 외, 2026
- [On the Role of Consistency Between Physics and Data in Physics-Informed Neural Networks](../../docs/papers/3195_On_the_Role_of_Consistency_Between_Physics_and_Data_in_Physi/index.html) — 2026.02 · 인용 11
- [One Intervention per Component is Enough: Towards Identifiability in Linear Stochastic Dynamics from Steady State](../../docs/papers/10125_One_Intervention_per_Component_is_Enough_Towards_Identifiabi/index.html) — Saber Salehkaleybar, 2026
- [Online Learnability of Chain-of-Thought Verifiers: Soundness and Completeness Trade-offs](../../docs/papers/10129_Online_Learnability_of_Chain-of-Thought_Verifiers_Soundness/index.html) — Maria Florina Balcan 외, 2026
- [OpenDiscoveryTrace: Process Traces for Evaluating AI Scientist Workflows](../../docs/papers/10134_OpenDiscoveryTrace_Process_Traces_for_Evaluating_AI_Scientis/index.html) — Aayam Bansal 외, 2026 · 인용 2,072
- [Ophiuchus: Incentivizing Tool-augmented ''Think with Images'' for Joint Medical Segmentation, Understanding and Reasoning](../../docs/papers/10137_Ophiuchus_Incentivizing_Tool-augmented_Think_with_Images_for/index.html) — Yankai Jiang 외, 2026
- [OptProver: Bridging Olympiad and Optimization through Continual Training in Formal Theorem Proving](../../docs/papers/10144_OptProver_Bridging_Olympiad_and_Optimization_through_Continu/index.html) — Chenyi Li 외, 2026
- [Optimal Guarantees for Auditing Rényi Differentially Private Machine Learning](../../docs/papers/10138_Optimal_Guarantees_for_Auditing_Rényi_Differentially_Private/index.html) — Benjamin D. Kim 외, 2026
- [Optimizing Social Utility in Sequential Experiments](../../docs/papers/10142_Optimizing_Social_Utility_in_Sequential_Experiments/index.html) — Ander Artola Velasco 외, 2026
- [PODiff: Latent Diffusion in Proper Orthogonal Decomposition Space for Scientific Super-Resolution](../../docs/papers/10208_PODiff_Latent_Diffusion_in_Proper_Orthogonal_Decomposition_S/index.html) — Onkar Jadhav 외, 2026 · 인용 97
- [PRIMA: a bidirectional state-space architecture and training approach for sequence modelling of protein-protein interactions](../../docs/papers/10235_PRIMA_a_bidirectional_state-space_architecture_and_training/index.html) — Arturo Fiorellini-Bernardis 외, 2026 · 인용 599
- [PaCX-MAE: Physiology-Augmented Chest X-Ray Masked Autoencoder](../../docs/papers/10154_PaCX-MAE_Physiology-Augmented_Chest_X-Ray_Masked_Autoencoder/index.html) — Yancheng Liu 외, 2026
- [PaperBanana: Automating Academic Illustration for AI Scientists](../../docs/papers/601_PaperBanana_Automating_Academic_Illustration_for_AI_Scientis/index.html) — Dawei Zhu 외, 2026.01 · 인용 1
- [Particle-Guided Diffusion Models for Partial Differential Equations](../../docs/papers/10158_Particle-Guided_Diffusion_Models_for_Partial_Differential_Eq/index.html) — Andrew Millard 외, 2026
- [Peano Player: Interactive Theorem Proving as a Constrained MDP](../../docs/papers/10167_Peano_Player_Interactive_Theorem_Proving_as_a_Constrained_MD/index.html) — Matthew Retchin 외, 2026
- [PerturbDiff: Functional Diffusion for Single-Cell Perturbation Modeling](../../docs/papers/10174_PerturbDiff_Functional_Diffusion_for_Single-Cell_Perturbatio/index.html) — Xinyu Yuan 외, 2026
- [Pessimistic Verification for Open-Ended Math Questions](../../docs/papers/10175_Pessimistic_Verification_for_Open-Ended_Math_Questions/index.html) — Yanxing Huang 외, 2026
- [PhenoBrain: Phenotype-Conditioned Long-Range Communication for Multi-Modal Brain Network Analysis](../../docs/papers/10178_PhenoBrain_Phenotype-Conditioned_Long-Range_Communication_fo/index.html) — Lingyuan Meng 외, 2026
- [Physically-Guided Data-Space Rectified Flow for Precipitation Nowcasting](../../docs/papers/10181_Physically-Guided_Data-Space_Rectified_Flow_for_Precipitatio/index.html) — Wenjie Luo 외, 2026
- [Physics-Informed Distillation of Diffusion Models for PDE-Constrained Generation](../../docs/papers/10186_Physics-Informed_Distillation_of_Diffusion_Models_for_PDE-Co/index.html) — Yi Zhang 외, 2026
- [Plug-and-Play Diffusion Meets ADMM: Dual-Variable Coupling for Robust Medical Image Reconstruction](../../docs/papers/10205_Plug-and-Play_Diffusion_Meets_ADMM_Dual-Variable_Coupling_fo/index.html) — Chenhe Du 외, 2026
- [PnP-Corrector: A Universal Correction Framework for Coupled Spatiotemporal Forecasting](../../docs/papers/10207_PnP-Corrector_A_Universal_Correction_Framework_for_Coupled_S/index.html) — Hao Wu 외, 2026
- [Position: Preventing the Collapse of Peer Review Requires Verification-First AI](../../docs/papers/10216_Position_Preventing_the_Collapse_of_Peer_Review_Requires_Ver/index.html) — Lei You 외, 2026
- [PostTrainBench: Can LLM Agents Automate LLM Post-Training?](../../docs/papers/10220_PostTrainBench_Can_LLM_Agents_Automate_LLM_Post-Training/index.html) — Ben Rank 외, 2026
- [Predicting new research directions in materials science using large language models and concept graphs](../../docs/papers/3212_Predicting_new_research_directions_in_materials_science_usin/index.html) — Thomas Marwitz 외, 2026.04 · 인용 2
- [Prediction-Powered Inference Across Many Tasks for AI Evaluation](../../docs/papers/10231_Prediction-Powered_Inference_Across_Many_Tasks_for_AI_Evalua/index.html) — Nicolas Emmenegger 외, 2026
- [Pretraining EHR Foundation Models with Patient-Aware Sampling](../../docs/papers/10234_Pretraining_EHR_Foundation_Models_with_Patient-Aware_Samplin/index.html) — Joshua Cesare Placidi 외, 2026 · 인용 112
- [Principled Confidence Estimation for Deep Computed Tomography](../../docs/papers/10239_Principled_Confidence_Estimation_for_Deep_Computed_Tomograph/index.html) — Matteo Gätzner 외, 2026
- [Process Reward Agents for Steering Knowledge-Intensive Reasoning](../../docs/papers/10251_Process_Reward_Agents_for_Steering_Knowledge-Intensive_Reaso/index.html) — Jiwoong Sohn 외, 2026 · 인용 11
- [Projected Hessian Learning: Fast Curvature Supervision for Accurate Machine-Learning Interatomic Potentials](../../docs/papers/3216_Projected_Hessian_Learning_Fast_Curvature_Supervision_for_Ac/index.html) — 2026.03
- [ProofGate: A Reproducible Audit of Faithfulness, Alignment, and Vacuity in State-of-the-Art Lean Theorem Provers](../../docs/papers/10257_ProofGate_A_Reproducible_Audit_of_Faithfulness_Alignment_and/index.html) — Edison Yang 외, 2026
- [Propose, Critique, Falsify: Benchmarking Self-Verifying AI Scientists](../../docs/papers/10259_Propose_Critique_Falsify_Benchmarking_Self-Verifying_AI_Scie/index.html) — Aayam Bansal 외, 2026
- [Protein Language Models Diverge from Natural Language: Comparative Analysis and Improved Inference](../../docs/papers/3221_Protein_Language_Models_Diverge_from_Natural_Language_Compar/index.html) — 2026.02 · 인용 3,225
- [ProteomeLM: A Proteome-Scale Language Model Enables Accurate and Rapid Prediction of Protein-Protein Interactions and Gene Essentiality Across Taxa](../../docs/papers/10267_ProteomeLM_A_Proteome-Scale_Language_Model_Enables_Accurate/index.html) — Cyril Malbranke 외, 2026 · 인용 763
- [ProtoCol: Late Interaction Retrieval for Protein Homolog Search](../../docs/papers/10270_ProtoCol_Late_Interaction_Retrieval_for_Protein_Homolog_Sear/index.html) — Gabrielle Cohn 외, 2026 · 인용 349
- [Q-Tag: Watermarking Quantum Circuit Generative Models](../../docs/papers/3226_Q-Tag_Watermarking_Quantum_Circuit_Generative_Models/index.html) — 2026.02
- [QEDBench: Quantifying the Alignment Gap in Automated Evaluation of University-Level Mathematical Proofs](../../docs/papers/10280_QEDBench_Quantifying_the_Alignment_Gap_in_Automated_Evaluati/index.html) — Santiago Gonzalez 외, 2026
- [Quantifying Ranking Uncertainty in LLM Benchmarks](../../docs/papers/10284_Quantifying_Ranking_Uncertainty_in_LLM_Benchmarks/index.html) — Bitya Neuhof 외, 2026 · 인용 2
- [QuantumQUBO Agent: Automating Quadratic Unconstrained Binary Optimization (QUBO) Formulation Generation from Natural Language](../../docs/papers/10289_QuantumQUBO_Agent_Automating_Quadratic_Unconstrained_Binary/index.html) — Niloy Kumar Mondal 외, 2026 · 인용 8,635
- [RETROSPECT: RETROsynthesis via Sequential Prediction, and Chemically Transformed-ranking](../../docs/papers/10340_RETROSPECT_RETROsynthesis_via_Sequential_Prediction_and_Chem/index.html) — Raja Sekhar Pappala 외, 2026 · 인용 241
- [RSI for Science: A Verifier-First Framework for AI Scientists](../../docs/papers/10354_RSI_for_Science_A_Verifier-First_Framework_for_AI_Scientists/index.html) — David Scott Lewis 외, 2026
- [Read, Grep, and Synthesize: Diagnosing Cross-Domain Seed Exposure for LLM Research Ideation](../../docs/papers/10297_Read_Grep_and_Synthesize_Diagnosing_Cross-Domain_Seed_Exposu/index.html) — Yunju Choi 외, 2026 · 인용 76
- [Reinforcement Learning for Adaptive Tacrolimus Dosing with Drug-Drug Interaction Management](../../docs/papers/10318_Reinforcement_Learning_for_Adaptive_Tacrolimus_Dosing_with_D/index.html) — Apoorva Srinivasan 외, 2026 · 인용 1,282
- [Reinforcement Learning for Tool-Calling Agents in Fast Healthcare Interoperability Resources (FHIR)](../../docs/papers/10319_Reinforcement_Learning_for_Tool-Calling_Agents_in_Fast_Healt/index.html) — Marius Knorr 외, 2026 · 인용 420
- [Reliable and Efficient Automated Transition-State Searches with Machine-Learned Interatomic Potentials](../../docs/papers/3229_Reliable_and_Efficient_Automated_Transition-State_Searches_w/index.html) — 2026.04 · 인용 2
- [Representative vs. Load-bearing Layers: A Dissociation in Genomic Foundation Models](../../docs/papers/10324_Representative_vs_Load-bearing_Layers_A_Dissociation_in_Geno/index.html) — Yoonjin Cho 외, 2026 · 인용 146
- [Representative, Informative, and De-Amplifying: Requirements for Robust Bayesian Active Learning under Model Misspecification](../../docs/papers/1100_Representative_Informative_and_De-Amplifying_Requirements_fo/index.html) — Roubing Tang 외, 2026.03
- [Residual-Guided Multi-Resolution Refinement of Foundation Models: A Case Study in Drought Forecasting](../../docs/papers/10325_Residual-Guided_Multi-Resolution_Refinement_of_Foundation_Mo/index.html) — Wentao Gao 외, 2026 · 인용 2
- [Resolution Diagnostics for Paired LLM Evaluation](../../docs/papers/10326_Resolution_Diagnostics_for_Paired_LLM_Evaluation/index.html) — Anany Kotawala, 2026
- [Resolving Blind Inverse Problems under Dynamic Range Compression via Structured Forward Operator Modeling](../../docs/papers/10327_Resolving_Blind_Inverse_Problems_under_Dynamic_Range_Compres/index.html) — Muyu Liu 외, 2026
- [Resp-GRASP: Clinically-Grounded Reasoning for Respiratory Signal Interpretation via Guardrailed RAG with Personalized Baselines](../../docs/papers/10328_Resp-GRASP_Clinically-Grounded_Reasoning_for_Respiratory_Sig/index.html) — Excel Widjaja 외, 2026
- [Rethinking Diffusion Models with Symmetries through Canonicalization with Applications to Molecular Graph Generation](../../docs/papers/10330_Rethinking_Diffusion_Models_with_Symmetries_through_Canonica/index.html) — Cai Zhou 외, 2026
- [Rethinking Federated Prompt Learning for Medical Images: From Textual Tuning to Visual Manifold Anchoring](../../docs/papers/10331_Rethinking_Federated_Prompt_Learning_for_Medical_Images_From/index.html) — Yipan Wei 외, 2026
- [Rethinking Self-Consistency in Protein Generative Models](../../docs/papers/10334_Rethinking_Self-Consistency_in_Protein_Generative_Models/index.html) — Minji Lee 외, 2026
- [Rethinking Small VLM Quantization: From Component-Wise Analysis to Hardware-Aware Edge Deployment](../../docs/papers/10335_Rethinking_Small_VLM_Quantization_From_Component-Wise_Analys/index.html) — Hyeju Shin 외, 2026
- [Rethinking the Value of Multi-Agent Workflow: A Strong Single Agent Baseline](../../docs/papers/11008_Rethinking_the_Value_of_Multi-Agent_Workflow_A_Strong_Single/index.html) — Jiawei Xu 외, 2026.01 · 인용 2
- [RetrOrchestrator: A Multi-Step Retrosynthesis Agent Dynamically Orchestrating Single-Step Transition Models](../../docs/papers/10339_RetrOrchestrator_A_Multi-Step_Retrosynthesis_Agent_Dynamical/index.html) — Liao Chang 외, 2026
- [Retro-Expert: Collaborative Reasoning for Interpretable Retrosynthesis](../../docs/papers/10337_Retro-Expert_Collaborative_Reasoning_for_Interpretable_Retro/index.html) — Xinyi Li 외, 2026
- [Retro-Forge: A Multi-Step Pairwise Retrosynthesis Framework for Solid-State Materials Synthesis](../../docs/papers/10338_Retro-Forge_A_Multi-Step_Pairwise_Retrosynthesis_Framework_f/index.html) — Juhan Hong 외, 2026
- [ReviewArena: A Large-Scale Cross-Conference Dataset and Benchmark for LLM Peer Review](../../docs/papers/10341_ReviewArena_A_Large-Scale_Cross-Conference_Dataset_and_Bench/index.html) — Samarth P 외, 2026
- [Risk-Controlled Lean-as-Judge for Natural-Language Mathematical Reasoning](../../docs/papers/10347_Risk-Controlled_Lean-as-Judge_for_Natural-Language_Mathemati/index.html) — Pauline Bourigault 외, 2026
- [Robin: A multi-agent system for automating scientific discovery](../../docs/papers/10726_robin_a_multi-agent_system_for_automating_scientific_d/index.html) — Ali E. Ghareeb 외, 2026.05 · 인용 50
- [Robust Causal Discovery in Real-World Time Series with Power-Laws](../../docs/papers/10349_Robust_Causal_Discovery_in_Real-World_Time_Series_with_Power/index.html) — Matteo Tusoni 외, 2026
- [Routing by Reaching: Composition of Pre-trained GFlowNets for Multi-Objective Generation](../../docs/papers/10353_Routing_by_Reaching_Composition_of_Pre-trained_GFlowNets_for/index.html) — Seokwon Yoon 외, 2026
- [S1-MMAlign: A Large-Scale, Multi-Disciplinary Dataset for Scientific Figure-Text Understanding](../../docs/papers/691_S1-MMAlign_A_Large-Scale_Multi-Disciplinary_Dataset_for_Scie/index.html) — He Wang 외, 2026.01
- [S2M-Net: Spectral-Spatial Mixing with Morphology-Aware Adaptive Loss for Medical Image Segmentation](../../docs/papers/10356_S2M-Net_Spectral-Spatial_Mixing_with_Morphology-Aware_Adapti/index.html) — Sanaullah Chowdhury 외, 2026
- [SAEs-BrainMap: Unveiling the Emergence of Specialized Concepts in Deep Models via Brain Alignment](../../docs/papers/10358_SAEs-BrainMap_Unveiling_the_Emergence_of_Specialized_Concept/index.html) — Ziming Mao 외, 2026
- [SE(3)-Equivariant Flow Matching with Gaussian Process Priors for Geometric Trajectory Prediction](../../docs/papers/10398_SE3-Equivariant_Flow_Matching_with_Gaussian_Process_Priors_f/index.html) — Xuyang Wang 외, 2026
- [SENDAI: A Hierarchical Sparse-measurement, EfficieNt Data AssImilation Framework](../../docs/papers/10422_SENDAI_A_Hierarchical_Sparse-measurement_EfficieNt_Data_AssI/index.html) — Xingyue Zhang 외, 2026
- [SI-IGCL: Subject Invariance-aware Inverse Graph Contrastive Learning for Psychiatric Disorder Identification](../../docs/papers/10435_SI-IGCL_Subject_Invariance-aware_Inverse_Graph_Contrastive_L/index.html) — Jiayu Lu 외, 2026
- [SIGMA-PPG: Statistical-prior Informed Generative Masking Architecture for PPG Foundation Model](../../docs/papers/10440_SIGMA-PPG_Statistical-prior_Informed__Generative_Masking_Arc/index.html) — Zongheng Guo 외, 2026
- [SMDD-Bench: Can LLMs Solve Real-World Small Molecule Drug Design Tasks?](../../docs/papers/10458_SMDD-Bench_Can_LLMs_Solve_Real-World_Small_Molecule_Drug_Des/index.html) — Kevin Han 외, 2026
- [STFlow: Data-Coupled Flow Matching for Geometric Trajectory Simulation](../../docs/papers/10501_STFlow_Data-Coupled_Flow_Matching_for_Geometric_Trajectory_S/index.html) — Kiet Bennema ten Brinke 외, 2026 · 인용 12
- [Safe Particle Selection for Diffusion Steering](../../docs/papers/10359_Safe_Particle_Selection_for_Diffusion_Steering/index.html) — Kianoosh Ashouritaklimi 외, 2026
- [Safe-SDL:Establishing Safety Boundaries and Control Mechanisms for AI-Driven Self-Driving Laboratories](../../docs/papers/11481_Safe-SDLEstablishing_Safety_Boundaries_and_Control_Mechanism/index.html) — Zihan Zhang 외, 2026.02
- [Safety Generalization Under Distribution Shift in Safe Reinforcement Learning: A Diabetes Testbed](../../docs/papers/10362_Safety_Generalization_Under_Distribution_Shift_in_Safe_Reinf/index.html) — Minjae Kwon 외, 2026
- [Salus: Strategic Diagnostic Testing for Complex Diagnosis via Multi-Agent Reinforcement Learning](../../docs/papers/10364_Salus_Strategic_Diagnostic_Testing_for_Complex_Diagnosis_via/index.html) — Shuohao Gao 외, 2026
- [Scalable Bayesian Inference for Nonlinear Conservation Laws](../../docs/papers/10368_Scalable_Bayesian_Inference_for_Nonlinear_Conservation_Laws/index.html) — Tim Weiland 외, 2026
- [Scalable Cross-Facility Federated Learning for Scientific Foundation Models on Multiple Supercomputers](../../docs/papers/694_Scalable_Cross-Facility_Federated_Learning_for_Scientific_Fo/index.html) — Yijiang Li 외, 2026.03
- [Scalable Neural Decoders for Practical Fault-Tolerant Quantum Computation](../../docs/papers/10370_Scalable_Neural_Decoders_for_Practical_Fault-Tolerant_Quantu/index.html) — Andi Gu 외, 2026 · 인용 780
- [Scalable Single-Cell Gene Expression Generation with Latent Diffusion Models](../../docs/papers/10372_Scalable_Single-Cell_Gene_Expression_Generation_with_Latent/index.html) — Giovanni Palla 외, 2026
- [Scaling Laws and Architectural Frontiers in Metagenomic Foundation Models](../../docs/papers/10375_Scaling_Laws_and_Architectural_Frontiers_in_Metagenomic_Foun/index.html) — Geraldene Munsamy 외, 2026 · 인용 519
- [Scaling Laws of Global Weather Models](../../docs/papers/10376_Scaling_Laws_of_Global_Weather_Models/index.html) — Yuejiang Yu 외, 2026
- [Scaling the Prior: Size-Consistent Geometric Diffusion for 3D Molecular Generation](../../docs/papers/10378_Scaling_the_Prior_Size-Consistent_Geometric_Diffusion_for_3D/index.html) — Wenhan Gao 외, 2026
- [Scaling up Multi-Turn Off-Policy RL and Multi-Agent Tree Search for LLM Step-Provers](../../docs/papers/10379_Scaling_up_Multi-Turn_Off-Policy_RL_and_Multi-Agent_Tree_Sea/index.html) — Ran Xin 외, 2026
- [SciContrib-Bench: Mapping the Autonomy Landscape of AI Scientists Through Stage-Dependent Detectability](../../docs/papers/10386_SciContrib-Bench_Mapping_the_Autonomy_Landscape_of_AI_Scient/index.html) — Raghav Agarwal 외, 2026
- [SciNet: Evaluating AI Agents in Relation-Aware Scientific Literature Retrieval](../../docs/papers/10391_SciNet_Evaluating_AI_Agents_in_Relation-Aware_Scientific_Lit/index.html) — Chenyang Shao 외, 2026 · 인용 3,133
- [SciPaths: Forecasting Pathways to Scientific Discovery](../../docs/papers/10392_SciPaths_Forecasting_Pathways_to_Scientific_Discovery/index.html) — Eric Chamoun 외, 2026
- [SciPredict: Can LLMs Predict the Outcomes of Scientific Experiments in Natural Sciences?](../../docs/papers/10393_SciPredict_Can_LLMs_Predict_the_Outcomes_of_Scientific_Exper/index.html) — Udari Madhushani Sehwag 외, 2026
- [SciVideoBench: Benchmarking Scientific Video Reasoning in Large Multimodal Models](../../docs/papers/10395_SciVideoBench_Benchmarking_Scientific_Video_Reasoning_in_Lar/index.html) — Andong Deng 외, 2026
- [Scientists decry conference’s use of hidden prompts to snare AI peer reviews](../../docs/papers/11015_Scientists_decry_conferences_use_of_hidden_prompts_to_snare/index.html) — Dalmeet Singh Chawla, 2026 · 인용 1
- [ScoreStop: Gradient-based early stopping using functional score tests](../../docs/papers/10397_ScoreStop_Gradient-based_early_stopping_using_functional_sco/index.html) — Oliver J. Hines 외, 2026
- [Seizure-Semiology-Suite(S^3): A Clinically Multimodal Dataset, Benchmark, and Models for Seizure Semiology Understanding](../../docs/papers/10406_Seizure-Semiology-SuiteS3_A_Clinically_Multimodal_Dataset_Be/index.html) — Lina Zhang 외, 2026
- [Self-Distillation Zero: Self-Revision Turns Binary Rewards into Dense Supervision](../../docs/papers/10409_Self-Distillation_Zero_Self-Revision_Turns_Binary_Rewards_in/index.html) — Yinghui He 외, 2026
- [Self-Improving Language Models with Bidirectional Evolutionary Search](../../docs/papers/10410_Self-Improving_Language_Models_with_Bidirectional_Evolutiona/index.html) — Guowei Xu 외, 2026
- [Self-Supervised Theorem Discovery in a Formal Axiomatic System](../../docs/papers/10414_Self-Supervised_Theorem_Discovery_in_a_Formal_Axiomatic_Syst/index.html) — Kazuki Ota 외, 2026
- [Semi-Autonomous Formalization of the Vlasov–Maxwell–Landau Equilibrium](../../docs/papers/10415_Semi-Autonomous_Formalization_of_the_VlasovMaxwellLandau_Equ/index.html) — Vasily Ilin, 2026 · 인용 3,164
- [Semi-knockoffs: a model-agnostic conditional independence testing method with finite-sample guarantees](../../docs/papers/10416_Semi-knockoffs_a_model-agnostic_conditional_independence_tes/index.html) — Angel David REYERO LOBO 외, 2026
- [Shift-Dependent Asymmetry: Orthogonal Inverse Low-Rank Adaptation for Federated Medical Segmentation](../../docs/papers/10433_Shift-Dependent_Asymmetry_Orthogonal_Inverse_Low-Rank_Adapta/index.html) — Xingyue Zhao 외, 2026
- [SkillX: Automatically Constructing Skill Knowledge Bases for Agents](../../docs/papers/10451_SkillX_Automatically_Constructing_Skill_Knowledge_Bases_for/index.html) — Chenxi Wang 외, 2026 · 인용 124
- [SleepLM: Natural-Language Intelligence for Human Sleep](../../docs/papers/10454_SleepLM_Natural-Language_Intelligence_for_Human_Sleep/index.html) — Zongzhe Xu 외, 2026
- [SleepMaMi: A Universal Sleep Foundation Model for Integrating Macro- and Micro-structures](../../docs/papers/10455_SleepMaMi_A_Universal_Sleep_Foundation_Model_for_Integrating/index.html) — Keondo Park 외, 2026
- [Smooth Dynamic Cutoffs for Machine Learning Interatomic Potentials](../../docs/papers/10459_Smooth_Dynamic_Cutoffs_for_Machine_Learning_Interatomic_Pote/index.html) — Kevin Han 외, 2026
- [Smooth Multi-Policy Causal Effect Estimation in Longitudinal Settings](../../docs/papers/10460_Smooth_Multi-Policy_Causal_Effect_Estimation_in_Longitudinal/index.html) — Wenxin Chen 외, 2026
- [SoMA: A Real-to-Sim Neural Simulator for Robotic Soft-Body Manipulation](../../docs/papers/10467_SoMA_A_Real-to-Sim_Neural_Simulator_for_Robotic_Soft-Body_Ma/index.html) — Mu Huang 외, 2026
- [Solving Stiff Dark Matter Equations via Jacobian Normalization with Physics-Informed Neural Networks](../../docs/papers/3242_Solving_Stiff_Dark_Matter_Equations_via_Jacobian_Normalizati/index.html) — 2026.02 · 인용 458
- [SparseEHR: Scalable Foundation Modeling for Structured EHR via Conditional Computation](../../docs/papers/10473_SparseEHR_Scalable_Foundation_Modeling_for_Structured_EHR_vi/index.html) — Meysam Ghaffari 외, 2026
- [Spatial Deconfounder: Interference-Aware Deconfounding for Spatial Causal Inference](../../docs/papers/10475_Spatial_Deconfounder_Interference-Aware_Deconfounding_for_Sp/index.html) — Ayush Khot 외, 2026
- [Step-Level Elaboration Improves Natural Language Verification of Research-Level Mathematical Proofs](../../docs/papers/10500_Step-Level_Elaboration_Improves_Natural_Language_Verificatio/index.html) — Yifeng Sun 외, 2026
- [Sticks and Stones: Positive vs. Negative Emotional Prompt Framings](../../docs/papers/10502_Sticks_and_Stones_Positive_vs_Negative_Emotional_Prompt_Fram/index.html) — Vipul Joshi 외, 2026
- [SurvDiff: A Diffusion Model for Generating Synthetic Data in Survival Analysis](../../docs/papers/10520_SurvDiff_A_Diffusion_Model_for_Generating_Synthetic_Data_in/index.html) — Marie Brockschmidt 외, 2026
- [SynLaD: Latent Diffusion for Generating Synthesizable Molecules Conditioned on 3D Pharmacophore Profiles](../../docs/papers/10527_SynLaD_Latent_Diffusion_for_Generating_Synthesizable_Molecul/index.html) — Miruna Cretu 외, 2026
- [SynerMedGen: Synergizing Medical Multimodal Understanding with Generation via Task Alignment](../../docs/papers/10526_SynerMedGen_Synergizing_Medical_Multimodal_Understanding_wit/index.html) — Weiren zhao 외, 2026
- [TRIAGE: An AI Scientist for Adversarial Target Falsification](../../docs/papers/10638_TRIAGE_An_AI_Scientist_for_Adversarial_Target_Falsification/index.html) — Jiawei Xing, 2026 · 인용 119
- [TadA-Bench: A Million-Variant Benchmark for Future-Round Discovery Toward Agentic Protein Engineering](../../docs/papers/10537_TadA-Bench_A_Million-Variant_Benchmark_for_Future-Round_Disc/index.html) — Jin Gao 외, 2026 · 인용 7
- [Talking to instruments: device-integration standards for self-driving laboratories](../../docs/papers/11480_Talking_to_instruments_device-integration_standards_for_self/index.html) — Willi Gottstein 외, 2026.10
- [Target-Driven Policy Optimization for Sequential Counterfactual Outcome Control](../../docs/papers/10541_Target-Driven_Policy_Optimization_for_Sequential_Counterfact/index.html) — Xin Wang 외, 2026
- [TasteBench: multimodal benchmark for sensory prediction, from molecules to sustainable foods](../../docs/papers/10542_TasteBench_multimodal_benchmark_for_sensory_prediction_from/index.html) — Anna Thomas 외, 2026
- [The Leaderboard Lottery: Why Top LLM Rankings Are Often Coin Flips, and How to Fix Them](../../docs/papers/10572_The_Leaderboard_Lottery_Why_Top_LLM_Rankings_Are_Often_Coin/index.html) — Shourya Vir Jain, 2026
- [The Perception–Physics Paradox: Probing Scientific Alignment with TC-Bench](../../docs/papers/10574_The_PerceptionPhysics_Paradox_Probing_Scientific_Alignment_w/index.html) — Dingling Yao 외, 2026
- [The Signal-Coverage Matrix: Stratifying Type and Semantic Errors in Statement Autoformalization](../../docs/papers/10578_The_Signal-Coverage_Matrix_Stratifying_Type_and_Semantic_Err/index.html) — Chengxiao Dai 외, 2026
- [TimeSpot: Benchmarking Geo-Temporal Understanding in Vision–Language Models in Real-World Settings](../../docs/papers/10589_TimeSpot_Benchmarking_Geo-Temporal_Understanding_in_VisionLa/index.html) — Azmine Toushik Wasi 외, 2026
- [Token-Only Adaptation of Frozen Self-Supervised Vision Foundation Models for Cross-Species Animal Pose: A Pareto-Frontier Characterization Across Eight Held-Out Mammal Species](../../docs/papers/10594_Token-Only_Adaptation_of_Frozen_Self-Supervised_Vision_Found/index.html) — Ethan Y Wang 외, 2026 · 인용 979
- [Token-Sparse Medical Multimodal Reasoning via Dual-Stream Reinforcement Learning](../../docs/papers/10595_Token-Sparse_Medical_Multimodal_Reasoning_via_Dual-Stream_Re/index.html) — Kaitao Chen 외, 2026
- [TotSyn: A Total Synthesis Reaction Dataset for Machine Learning in Organic Chemistry](../../docs/papers/10605_TotSyn_A_Total_Synthesis_Reaction_Dataset_for_Machine_Learni/index.html) — Chaewon Lee 외, 2026
- [Total Variation Distance Estimation in Autoregressive Models](../../docs/papers/10604_Total_Variation_Distance_Estimation_in_Autoregressive_Models/index.html) — Eric Price 외, 2026
- [Toward Unified Evaluation of Mathematical AI: A Survey and Framework](../../docs/papers/10606_Toward_Unified_Evaluation_of_Mathematical_AI_A_Survey_and_Fr/index.html) — Nishitha A, 2026
- [Toward a Fully Autonomous, AI-Native Particle Accelerator](../../docs/papers/816_Toward_a_Fully_Autonomous_AI-Native_Particle_Accelerator/index.html) — Chris Tennant, 2026.02 · 인용 154
- [Toward self-driving laboratory 2.0 for chemistry and materials discovery](../../docs/papers/10912_toward_self-driving_laboratory_20_for_chemistry_and_ma/index.html) — Heeseung Lee 외, 2026 · 인용 14
- [Towards Self-Evolving Agentic Literature Retrieval](../../docs/papers/10617_Towards_Self-Evolving_Agentic_Literature_Retrieval/index.html) — Yuwen Du 외, 2026 · 인용 1,798
- [Towards end-to-end automation of AI research](../../docs/papers/828_Towards_end-to-end_automation_of_AI_research/index.html) — Chris Lu 외, 2026.03 · 인용 90
- [Training AI Co-Scientists Using Rubric Rewards](../../docs/papers/10622_Training_AI_Co-Scientists_Using_Rubric_Rewards/index.html) — Shashwat Goel 외, 2026
- [Training-Free Adversarial Robustness in Computational MRI](../../docs/papers/10625_Training-Free_Adversarial_Robustness_in_Computational_MRI/index.html) — Mahdi Saberi 외, 2026
- [Two-Parameter Flows for Learning Population Dynamics of Physical Systems](../../docs/papers/10648_Two-Parameter_Flows_for_Learning_Population_Dynamics_of_Phys/index.html) — Paul Schwerdtner 외, 2026 · 인용 2
- [U-Cast: A Surprisingly Simple and Efficient Frontier Probabilistic AI Weather Forecaster](../../docs/papers/10652_U-Cast_A_Surprisingly_Simple_and_Efficient_Frontier_Probabil/index.html) — Salva Rühling Cachay 외, 2026
- [Universal Neural Propagator: Learning Time Evolution in Many-Body Quantum Systems](../../docs/papers/3272_Universal_Neural_Propagator_Learning_Time_Evolution_in_Many-/index.html) — Zihao Qi 외, 2026.05 · 인용 777
- [VERITAS: Verifier-Guided Proof Search for Zero-Shot Formal Theorem Proving](../../docs/papers/10678_VERITAS_Verifier-Guided_Proof_Search_for_Zero-Shot_Formal_Th/index.html) — Manish Acharya 외, 2026
- [VT-Bench: A Unified Benchmark for Visual-Tabular Multi-Modal Learning](../../docs/papers/10685_VT-Bench_A_Unified_Benchmark_for_Visual-Tabular_Multi-Modal/index.html) — Ziyi Jia 외, 2026
- [VeriBench: An End-to-End Formal Verification Benchmark for AI Coding Agents in Lean 4](../../docs/papers/10676_VeriBench_An_End-to-End_Formal_Verification_Benchmark_for_AI/index.html) — Brando Miranda 외, 2026
- [VeriScale: Adversarial Test-Suite Scaling for Verifiable Code Generation](../../docs/papers/10677_VeriScale_Adversarial_Test-Suite_Scaling_for_Verifiable_Code/index.html) — Yifan Bai 외, 2026 · 인용 30
- [Weak Critics Make Strong Learners: On-Policy Critique Distillation for Scalable Oversight](../../docs/papers/10690_Weak_Critics_Make_Strong_Learners_On-Policy_Critique_Distill/index.html) — Can Jin 외, 2026
- [What are the Right Symmetries for Formal Theorem Proving?](../../docs/papers/10696_What_are_the_Right_Symmetries_for_Formal_Theorem_Proving/index.html) — Krzysztof Olejniczak 외, 2026
- [When Single Answer Is Not Enough: Rethinking Single-Step Retrosynthesis Benchmarks for LLMs](../../docs/papers/10711_When_Single_Answer_Is_Not_Enough_Rethinking_Single-Step_Retr/index.html) — Bogdan Zagribelnyy 외, 2026
- [YC-Bench: Benchmarking AI Agents for Long-Term Planning and Consistent Execution](../../docs/papers/3398_YC-Bench_Benchmarking_AI_Agents_for_Long-Term_Planning_and_C/index.html) — Muyu He 외, 2026 · 인용 1,873
- [climt-paraformer: Stable Emulation of Convective Parameterization using a Temporal Memory-aware Transformer](../../docs/papers/3056_climt-paraformer_Stable_Emulation_of_Convective_Parameteriza/index.html) — 2026.04
- [miniF2F-Dafny: LLM-Guided Mathematical Theorem Proving via Auto-Active Verification](../../docs/papers/10033_miniF2F-Dafny_LLM-Guided_Mathematical_Theorem_Proving_via_Au/index.html) — Mantas Baksys 외, 2026 · 인용 4
- [A comprehensive survey on long context language modeling](../../docs/papers/005_A_comprehensive_survey_on_long_context_language_modeling/index.html) — Jiaheng Liu 외, 2025 · 인용 2
- [AI Scientists Fail Without Strong Implementation Capability](../../docs/papers/081_Ai_scientists_fail_without_strong_implementation_capability/index.html) — Min Zhu 외, 2025 · 인용 2,819
- [AI-Newton: A concept-driven physical law discovery system without prior physical knowledge](../../docs/papers/085_Ai-newton_A_concept-driven_physical_law_discovery_system_wit/index.html) — You-Le Fang 외, 2025
- [Adaptive ai decision interface for autonomous electronic material discovery](../../docs/papers/048_Adaptive_ai_decision_interface_for_autonomous_electronic_mat/index.html) — Yahao Dai 외, 2025 · 인용 22
- [Ai idea bench 2025: Ai research idea generation benchmark](../../docs/papers/10924_Ai_idea_bench_2025_Ai_research_idea_generation_benchmark/index.html) — DeepSeek-AI 외, 2025
- [AlphaGenome: advancing regulatory variant effect prediction with a unified DNA sequence model](../../docs/papers/094_AlphaGenome_advancing_regulatory_variant_effect_prediction_w/index.html) — Žiga Avsec 외, 2025 · 인용 110
- [Architectures, variants, and performance of neural operators: A comparative review](../../docs/papers/103_Architectures_variants_and_performance_of_neural_operators_A/index.html) — Shengjun Liu 외, 2025.10 · 인용 16
- [Ask, retrieve, summarize: A modular pipeline for scientific literature summarization](../../docs/papers/108_Ask_retrieve_summarize_A_modular_pipeline_for_scientific_lit/index.html) — Pierre Achkar 외, 2025 · 인용 91
- [Autonomous Agents for Scientific Discovery: Orchestrating Scientists, Language, Code, and Physics](../../docs/papers/137_Autonomous_Agents_for_Scientific_Discovery_Orchestrating_Sci/index.html) — Lianhao Zhou 외, 2025.10 · 인용 12,647
- [ChartSketcher: Reasoning with multimodal feedback and reflection for chart understanding](../../docs/papers/203_Chartsketcher_Reasoning_with_multimodal_feedback_and_reflect/index.html) — Muye Huang 외, 2025
- [Chartist: Task-driven Eye Movement Control for Chart Reading](../../docs/papers/200_Chartist_Task-driven_Eye_Movement_Control_for_Chart_Reading/index.html) — Danqing Shi 외, 2025 · 인용 13
- [Confidence in Large Language Model Evaluation: A Bayesian Approach to Limited-Sample Challenges](../../docs/papers/237_Confidence_in_Large_Language_Model_Evaluation_A_Bayesian_App/index.html) — Xiao Xiao 외, 2025
- [Critique-GRPO: Advancing LLM Reasoning with Natural Language and Numerical Feedback](../../docs/papers/243_Critique-GRPO_Advancing_LLM_Reasoning_with_Natural_Language/index.html) — Xiaoying Zhang 외, 2025
- [DEFAME: Dynamic Evidence-based Fact-checking with Multimodal Experts](../../docs/papers/267_Defame_Dynamic_evidencebased_fact-checking_with_multimodal_e/index.html) — Tobias Braun 외, 2025
- [DeepAnalyze: Agentic Large Language Models for Autonomous Data Science](../../docs/papers/259_DeepAnalyze_Agentic_Large_Language_Models_for_Autonomous_Dat/index.html) — Shaolei Zhang 외, 2025.10
- [DeepResearch Bench: A Comprehensive Benchmark for Deep Research Agents](../../docs/papers/261_Deepresearch_bench_A_comprehensive_benchmark_for_deep_resear/index.html) — Mingxuan Du 외, 2025
- [DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning](../../docs/papers/265_DeepSeek-R1_incentivizes_reasoning_in_LLMs_through_reinforce/index.html) — DeepSeek-AI 외, 2025 · 인용 1,046
- [Democratizing AI scientists using ToolUniverse](../../docs/papers/268_Democratizing_AI_scientists_using_ToolUniverse/index.html) — Shanghua Gao 외, 2025.09 · 인용 297
- [Discovery of Unstable Singularities](../../docs/papers/276_Discovery_of_Unstable_Singularities/index.html) — Yongji Wang 외, 2025.09 · 인용 17
- [Drugpilot: Llm-based parameterized reasoning agent for drug discovery](../../docs/papers/292_Drugpilot_Llm-based_parameterized_reasoning_agent_for_drug_d/index.html) — Kun Li 외, 2025 · 인용 40
- [Earth-Agent: Unlocking the Full Landscape of Earth Observation with Agents](../../docs/papers/298_Earth-Agent_Unlocking_the_Full_Landscape_of_Earth_Observatio/index.html) — Peilin Feng 외, 2025.09
- [Enhancing chemical reaction and retrosynthesis prediction with large language model and dual-task learning](../../docs/papers/316_Enhancing_chemical_reaction_and_retrosynthesis_prediction_wi/index.html) — Xuan Lin 외, 2025 · 인용 3
- [Estimating optimal context length for hybrid retrieval-augmented multi-document summarization](../../docs/papers/318_Estimating_optimal_context_length_for_hybrid_retrievalaugmen/index.html) — Adithya Pratapa 외, 2025
- [Exp-bench: Can ai conduct ai research experiments? arXiv preprint arXiv:2505.24785, 2025.](../../docs/papers/326_Exp-bench_Can_ai_conduct_ai_research_experiments_arXiv_prepr/index.html) — Patrick Tser Jern Kon 외, 2025 · 인용 1
- [Explainable biomedical claim verification with large language models](../../docs/papers/328_Explainable_biomedical_claim_verification_with_large_languag/index.html) — Siting Liang 외, 2025 · 인용 54
- [Exploiting LLMs for Automatic Hypothesis Assessment via a Logit-Based Calibrated Prior](../../docs/papers/330_Exploiting_LLMs_for_Automatic_Hypothesis_Assessment_via_a_Lo/index.html) — Yue Gong 외, 2025 · 인용 10
- [From AI for Science to Agentic Science: A Survey on Autonomous Scientific Discovery](../../docs/papers/352_From_AI_for_Science_to_Agentic_Science_A_Survey_on_Autonomou/index.html) — Jiaqi Wei 외, 2025.10 · 인용 5
- [From Human Memory to AI Memory: A Survey on Memory Mechanisms in the Era of LLMs](../../docs/papers/355_From_Human_Memory_to_AI_Memory_A_Survey_on_Memory_Mechanisms/index.html) — Yaxiong Wu 외, 2025 · 인용 2
- [From Theory to Application: A Practical Introduction to Neural Operators in Scientific Computing](../../docs/papers/364_From_Theory_to_Application_A_Practical_Introduction_to_Neura/index.html) — Prashant K. Jha, 2025.03 · 인용 10
- [Generalization Bias in Large Language Model Summarization of Scientific Research](../../docs/papers/373_Generalization_Bias_in_Large_Language_Model_Summarization_of/index.html) — Uwe Peters 외, 2025.03 · 인용 4
- [GeoFactory: an LLM performance enhancement framework for geoscience factual and inferential tasks](../../docs/papers/10764_geofactory_an_llm_performance_enhancement_framework_fo/index.html) — Zhou Chen 외, 2025.05 · 인용 6
- [GraphEval: A lightweight graph-based llm framework for idea evaluation](../../docs/papers/392_Grapheval_A_lightweight_graph-based_llm_framework_for_idea_e/index.html) — Tao Feng 외, 2025
- [Kimi k1.5: Scaling reinforcement learning with llms](../../docs/papers/449_Kimi_k15_Scaling_reinforcement_learning_with_llms/index.html) — Kimi Team 외, 2025 · 인용 109
- [Kosmos: An AI Scientist for Autonomous Discovery](../../docs/papers/9098_kosmos_an_ai_scientist_for_autonomous_discovery/index.html) — Ludovico Mitchener 외, 2025 · 인용 131
- [LIDDIA: Language-based Intelligent Drug Discovery Agent](../../docs/papers/490_LIDDIA_Language-based_Intelligent_Drug_Discovery_Agent/index.html) — Reza Averly 외, 2025 · 인용 6
- [LLM × MapReduce-V2: Entropy-Driven Convolutional Test-Time Scaling for Generating Long-Form Articles from Extremely Long Resources](../../docs/papers/495_Llm__mapreduce-v2_Entropy-driven_convolutional_test-time_sca/index.html) — Haoyu Wang 외, 2025
- [LLM-based Corroborating and Refuting Evidence Retrieval for Scientific Claim Verification](../../docs/papers/500_Llm-based_corroborating_and_refuting_evidence_retrieval_for/index.html) — Siyuan Wang 외, 2025
- [Lag: Llm agents for leaderboard auto generation on demanding](../../docs/papers/1088_Lag_Llm_agents_for_leaderboard_auto_generation_on_demanding/index.html) — Jian Wu 외, 2025
- [MedAgentGym: A Scalable Agentic Training Environment for Code-Centric Reasoning in Biomedical Data Science](../../docs/papers/528_MedAgentGym_A_Scalable_Agentic_Training_Environment_for_Code/index.html) — Ran Xu 외, 2025.06
- [Mind the blind spots: A focus-level evaluation framework for llm reviews](../../docs/papers/537_Mind_the_blind_spots_A_focus-level_evaluation_framework_for/index.html) — Hyungyu Shin 외, 2025 · 인용 3
- [MoDeST: A dataset for Multi Domain Scientific Title Generation](../../docs/papers/10765_modest_a_dataset_for_multi_domain_scientific_title_gen/index.html) — Necva Bölücü 외, 2025.05 · 인용 1
- [Multimodal deepresearcher: Generating text-chart interleaved reports from scratch with agentic framework](../../docs/papers/566_Multimodal_deepresearcher_Generating_text-chart_interleaved/index.html) — Zhaorui Yang 외, 2025 · 인용 3
- [Paper2poster: Towards multimodal poster automation from scientific papers](../../docs/papers/599_Paper2poster_Towards_multimodal_poster_automation_from_scien/index.html) — Wei Pang 외, 2025 · 인용 2
- [PharmAgents: Building a Virtual Pharma with Large Language Model Agents](../../docs/papers/616_PharmAgents_Building_a_Virtual_Pharma_with_Large_Language_Mo/index.html) — Bowen Gao 외, 2025 · 인용 2
- [Predicting field experiments with large language models](../../docs/papers/631_Predicting_field_experiments_with_large_language_models/index.html) — Yaoyu Chen 외, 2025
- [R&D-Agent: Automating Data-Driven AI Solution Building Through LLM-Powered Automated Research, Development, and Evolution](../../docs/papers/650_RD-Agent_Automating_Data-Driven_AI_Solution_Building_Through/index.html) — Xu Yang 외, 2025.05 · 인용 1
- [RBF++: Quantifying and optimizing reasoning boundaries across measurable and unmeasurable capabilities for chain-of-thought reasoning](../../docs/papers/652_Rbf_Quantifying_and_optimizing_reasoning_boundaries_across_m/index.html) — Qiguang Chen 외, 2025
- [RM-R1: Reward Modeling as Reasoning](../../docs/papers/683_RM-R1_Reward_Modeling_as_Reasoning/index.html) — Xiusi Chen 외, 2025 · 인용 2
- [ReSearch: Learning to Reason with Search for LLMs via Reinforcement Learning](../../docs/papers/667_ReSearch_Learning_to_Reason_with_Search_for_LLMs_via_Reinfor/index.html) — Mingyang Chen 외, 2025 · 인용 10
- [ResearchAgent: Iterative Research Idea Generation over Scientific Literature with Large Language Models](../../docs/papers/668_ResearchAgent_Iterative_Research_Idea_Generation_over_Scient/index.html) — Jinheon Baek 외, 2025.02 · 인용 34
- [ReviewEval: An evaluation framework for AI-generated reviews](../../docs/papers/679_Revieweval_An_evaluation_framework_for_ai-generated_reviews/index.html) — Madhav Krishan Garg 외, 2025 · 인용 2
- [SFT Memorizes, RL Generalizes: A Comparative Study of Foundation Model Post-training](../../docs/papers/751_SFT_Memorizes_RL_Generalizes_A_Comparative_Study_of_Foundati/index.html) — Tianzhe Chu 외, 2025 · 인용 6
- [SciClaims: An end-to-end generative system for biomedical claim analysis](../../docs/papers/711_Sciclaims_An_end-to-end_generative_system_for_biomedical_cla/index.html) — Raúl Ortega 외, 2025
- [Sciclaimhunt: A large dataset for evidence-based scientific claim verification](../../docs/papers/710_Sciclaimhunt_A_large_dataset_for_evidence-based_scientific_c/index.html) — Sujit Kumar 외, 2025 · 인용 35
- [Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement Learning](../../docs/papers/740_Search-R1_Training_LLMs_to_Reason_and_Leverage_Search_Engine/index.html) — Bowen Jin 외, 2025 · 인용 12
- [Select, read, and write: A multi-agent framework of full-text-based related work generation](../../docs/papers/742_Select_read_and_write_A_multi-agent_framework_of_full-text-b/index.html) — Xiaochuan Liu 외, 2025
- [Spacer: Towards Engineered Scientific Inspiration](../../docs/papers/3394_Spacer_Towards_Engineered_Scientific_Inspiration/index.html) — Minhyeong Lee 외, 2025
- [Sparks: Multi-Agent Artificial Intelligence Model Discovers Protein Design Principles](../../docs/papers/764_Sparks_Multi-Agent_Artificial_Intelligence_Model_Discovers_P/index.html) — Alireza Ghafarollahi 외, 2025 · 인용 9
- [SurveyX: Academic survey automation via large language models](../../docs/papers/781_Surveyx_Academic_survey_automation_via_large_language_models/index.html) — Xun Liang 외, 2025 · 인용 2,819
- [Surveyforge: On the outline heuristics, memory-driven generation, and multi-dimensional evaluation for automated survey writing](../../docs/papers/780_Surveyforge_On_the_outline_heuristics_memory-driven_generati/index.html) — Xiangchao Yan 외, 2025 · 인용 7
- [Tablemaster: A recipe to advance table understanding with language models](../../docs/papers/787_Tablemaster_A_recipe_to_advance_table_understanding_with_lan/index.html) — Lang Cao 외, 2025
- [Text2world: Benchmarking large language models for symbolic world model generation](../../docs/papers/792_Text2world_Benchmarking_large_language_models_for_symbolic_w/index.html) — Mengkang Hu 외, 2025 · 인용 3
- [The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search](../../docs/papers/794_The_AI_Scientist-v2_Workshop-Level_Automated_Scientific_Disc/index.html) — Yutaro Yamada 외, 2025.04 · 인용 476
- [The fifth era of science: Artificial scientific intelligence](../../docs/papers/1093_The_fifth_era_of_science_Artificial_scientific_intelligence/index.html) — N. Miolane, 2025 · 인용 4
- [The mighty torr: A benchmark for table reasoning and robustness](../../docs/papers/802_The_mighty_torr_A_benchmark_for_table_reasoning_and_robustne/index.html) — Shir Ashury-Tahan 외, 2025
- [Three AI-powered steps to faster, smarter peer review](../../docs/papers/809_Three_AI-powered_steps_to_faster_smarter_peer_review/index.html) — Dritjon Gruda, 2025.03 · 인용 4
- [Towards effective extraction and evaluation of factual claims](../../docs/papers/827_Towards_effective_extraction_and_evaluation_of_factual_claim/index.html) — Dasha Metropolitansky 외, 2025 · 인용 5
- [TreeReview: A dynamic tree of questions framework for deep and efficient llm-based scientific peer review](../../docs/papers/843_Treereview_A_dynamic_tree_of_questions_framework_for_deep_an/index.html) — Yuan Chang 외, 2025 · 인용 2
- [Understanding how paper writers use ai-generated captions in figure caption writing](../../docs/papers/853_Understanding_how_paper_writers_use_ai-generated_captions_in/index.html) — Ho Yin (Sam) Ng 외, 2025 · 인용 6
- [Using artificial intelligence for systematic review: the example of elicit](../../docs/papers/862_Using_artificial_intelligence_for_systematic_review_the_exam/index.html) — Nathan Bernard 외, 2025.03 · 인용 83
- [Value iteration for learning concurrently executable robotic control tasks](../../docs/papers/863_Value_iteration_for_learning_concurrently_executable_robotic/index.html) — Sheikh A. Tahmid 외, 2025 · 인용 244
- [Visual thoughts: A unified perspective of understanding multimodal chain-of-thought](../../docs/papers/869_Visual_thoughts_A_unified_perspective_of_understanding_multi/index.html) — Zihui Cheng 외, 2025
- [WebAgent-R1: Training Web Agents via End-to-End Multi-Turn Reinforcement Learning](../../docs/papers/871_WebAgent-R1_Training_Web_Agents_via_End-to-End_Multi-Turn_Re/index.html) — Zhepei Wei 외, 2025 · 인용 2
- [What counts as plagiarism? AI-generated papers pose new risks](../../docs/papers/10767_what_counts_as_plagiarism_ai-generated_papers_pose_new/index.html) — Ananya, 2025.08 · 인용 4
- [Zero-shot sim-to-real transfer for reinforcement learning-based visual servoing of soft continuum arms](../../docs/papers/891_Zero-shot_sim-to-real_transfer_for_reinforcement_learning-ba/index.html) — Hsin-Jung Yang 외, 2025 · 인용 1
- [AI Hospital: Benchmarking Large Language Models in a Multi-agent Medical Interaction Simulator](../../docs/papers/078_Ai_hospital_Benchmarking_large_language_models_in_a_multi-ag/index.html) — Zhihao Fan 외, 2024 · 인용 6
- [Agent hospital: A simulacrum of hospital with evolvable medical agents](../../docs/papers/058_Agent_hospital_A_simulacrum_of_hospital_with_evolvable_medic/index.html) — Junkai Li 외, 2024
- [Deepseek-prover: Advancing theorem proving in llms through large-scale synthetic data](../../docs/papers/264_Deepseek-prover_Advancing_theorem_proving_in_llms_through_la/index.html) — Huajian Xin 외, 2024
- [Gemini 1.5: Unlocking multimodal understanding across millions of tokens of context](../../docs/papers/368_Gemini_15_Unlocking_multimodal_understanding_across_millions/index.html) — Machel Reid 외, 2024 · 인용 296
- [Simulating tabular datasets through LLMs to rapidly explore hypotheses about real-world entities](../../docs/papers/757_Simulating_tabular_datasets_through_llms_to_rapidly_explore/index.html) — Miguel Zabaleta 외, 2024
- [The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery](../../docs/papers/795_The_AI_Scientist_Towards_Fully_Automated_Open-Ended_Scientif/index.html) — Chris Lu 외, 2024 · 인용 115
- [AutoML-GPT: Automatic Machine Learning with GPT](../../docs/papers/136_Automl-gpt_Automatic_machine_learning_with_gpt/index.html) — Shujian Zhang 외, 2023
- [Bio-SIEVE: Exploring Instruction Tuning Large Language Models for Systematic Review Automation](../../docs/papers/159_Bio-sieve_exploring_instruction_tuning_large_language_models/index.html) — Ambrose Robinson 외, 2023 · 인용 59
- [Code llama: Open foundation models for code](../../docs/papers/230_Code_llama_Open_foundation_models_for_code/index.html) — Baptiste Rozière 외, 2023
- [Lego-prover: Neural theorem proving with growing libraries](../../docs/papers/486_Lego-prover_Neural_theorem_proving_with_growing_libraries/index.html) — Huajian Xin 외, 2023 · 인용 80
- [Self-Refine: Iterative Refinement with Self-Feedback](../../docs/papers/746_Self-Refine_Iterative_Refinement_with_Self-Feedback/index.html) — Aman Madaan 외, 2023 · 인용 354
- [Tree-planner: Efficient close-loop task planning with large language models](../../docs/papers/842_Tree-planner_Efficient_close-loop_task_planning_with_large_l/index.html) — Mengkang Hu 외, 2023
- [Pangu-Weather: A 3D High-Resolution Model for Fast and Accurate Global Weather Forecast](../../docs/papers/2218_Pangu-Weather_A_3D_High-Resolution_Model_for_Fast_and_Accura/index.html) — Kaifeng Bi 외, 2022 · 인용 126
- [Don't Stop Pretraining: Adapt Language Models to Domains and Tasks](../../docs/papers/287_Dont_Stop_Pretraining_Adapt_Language_Models_to_Domains_and_T/index.html) — Suchin Gururangan 외, 2020 · 인용 2,067

*생성: `pipeline/build_slide_essay.py --topic ai4s` · 2026-10-21 · 근거 코퍼스 2,709편 · 본문 85,491자*
