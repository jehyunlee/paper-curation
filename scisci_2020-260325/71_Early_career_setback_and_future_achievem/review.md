# Early career setback and future achievement in professional sports

> **저자**: Suman Kalyan Maity, Yang Wang, Nima Dehmamy, Victoria Medvec, Brian Uzzi, Dashun Wang | **날짜**: 2025-09-29 | **Journal**: Scientific Reports | **DOI**: 10.1038/s41598-025-17271-z

---

## Essence

초기 커리어에서 아슬아슬하게 승리를 놓친 선수(non-winner)가 장기적으로 근소하게 이긴 선수(winner)를 능가할 수 있다. 육상 4위 입상자는 동메달리스트보다 향후 4년간 평균 1.72개 vs 1.35개의 메달을 획득했으며, 직접 재대결 시 59.2%의 승률을 기록했다(p=0.0001). 테니스에서도 "unlucky loser"가 "lucky loser"보다 유의하게 높은 미래 승률을 보였다(p=8.67×10⁻⁸).

## Motivation

과거 성공이 미래 성공을 예측한다는 것은 사회과학의 가장 견고한 발견 중 하나이며, Matthew effect와 winner-take-all 역학으로 설명되어 왔다. 그러나 NIH 연구비 near-miss 연구(Wang et al., 2019)에서 실패 경험이 오히려 장기 성과를 높일 수 있다는 증거가 제시되었다. 하지만 이 결과가 (1) 과학 외 다른 도메인에서도 성립하는지, (2) 객관적 성과 지표로 측정 가능한지, (3) 승자가 내생적으로(endogenously) 더 우수한 상황에서도 역전이 일어나는지는 미해결 질문이었다. 스포츠는 성과가 객관적·투명하게 측정되므로 이상적인 실증 환경을 제공한다.

## Achievement

1. 육상(IAAF) 5,101명 분석: 4위 입상자가 동메달리스트를 유의하게 능가(Mann-Whitney U test, p=0.04). 이 패턴은 1-2년, 3-4년, 8년, 전체 커리어에 걸쳐 일관됨
2. 4위 입상자의 기록 경신 확률(5.81%)이 은메달·동메달리스트를 초과하며, 기록 보유자 중 19.4%가 4위 출발
3. 직접 재대결에서 4위가 동메달리스트를 59.2% 이김(Binomial test, p=0.0001) — 유일하게 upset probability > 0인 인접 순위 쌍
4. 테니스 ATP Tour(2007-2018, n=2,688): unlucky loser가 lucky loser보다 미래 매치 승률이 유의하게 높음(p=8.67×10⁻⁸). 대조군(철수 없는 토너먼트)에서는 기존 통념대로 상위 랭킹이 더 나은 성과
5. 생존 편향(screening effect), 자기 선택, 평균 회귀 등 대안 설명을 체계적으로 배제

## How

- **데이터**: IAAF 육상 대회(1987-2009, 40,816명 중 21세 이하 5,101명 결선 진출자), ATP Tour 테니스(2007-2018, 2,688명, 54,084 매치)
- **방법론 1 (육상)**: 첫 결선 순위별 그룹화 → 향후 4년간 메달 수, 순위 분포, 기록 경신 확률 비교. 인접 순위 쌍별 직접 대결 승률(pairwise comparison) 계산. 생존 편향 통제를 위한 보수적 제거 절차(conservative removal)
- **방법론 2 (테니스)**: Lucky loser 자연실험(quasi-experiment) — 본선 선수 부상/철수로 인한 외생적 cutoff 이동. Treatment(철수 발생) vs Control(미발생) 비교. 매치 승률, 8강 이상 진출 확률 등 다양한 성과 지표
- **통계**: Mann-Whitney U test, Binomial test, proportion test, 다양한 robustness check(시간대별, 종목별, quartile별, cohort별)

## Originality

- NIH 연구비 맥락(Wang et al., 2019)의 "early-career setback" 발견을 스포츠라는 완전히 다른 도메인으로 확장. 특히 승자가 **내생적으로** 더 우수한 상황에서도 성과 역전을 실증한 최초의 연구
- 테니스 lucky loser라는 독창적인 자연실험 설계를 통해 인과 추론 강화
- 단순한 동기 부여 효과(단기)가 아닌 장기적 발달적 효과를 구분하여 분석

## Limitation & Further Study

### 저자들이 언급한 한계
- 관찰 불가능한 이질성(코칭 접근성, 훈련 강도, 심리적 지원 등)이 통제되지 않아 엄밀한 인과 추론에 한계
- 메커니즘(grit, growth mindset, resilience 등)은 이론적으로 제시했으나 데이터로 검증하지 못함
- 개인 종목 중심이므로 팀 스포츠로의 일반화는 추가 연구 필요
- 성과 역전이 특정 조건(초기 커리어, 좁은 순위 차이)에서만 관측될 수 있음

### 리뷰어 판단 아쉬운 점
- 육상 데이터에서 3위 vs 4위 차이의 실질적 크기(effect size)가 보고되지 않음. 통계적 유의성은 있으나 실용적 의미 판단이 어려움
- "Podium cutoff"라는 설명이 핵심적인데, 이것이 실제로 선수에게 어떤 심리적·물질적 차이를 만드는지(예: 후원금, 미디어 노출)에 대한 데이터가 없음
- 테니스 lucky loser 분석에서 표본 크기(n=223 lucky losers, 172 unlucky losers)가 비교적 작아 하위 그룹 분석의 검정력이 제한적
- Wang et al. (2019) NIH 연구와의 직접 비교가 제한적 — 효과 크기의 도메인 간 비교가 있었으면 더 풍부한 논의 가능

### 후속 연구
- 스포츠 외 도메인(교육, 비즈니스, 예술)에서의 재현 연구
- 심리적 메커니즘(grit, resilience, growth mindset)을 직접 측정하는 종단 연구
- 팀 스포츠에서의 near-miss 효과 검증
- Near-miss 경험의 "임계 조건" 규명 (어느 정도의 차이까지 역전이 가능한가)

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 3/5 |
| Technical Soundness | 4/5 |
| Significance | 3/5 |
| Clarity | 4/5 |
| Overall | 3/5 |

**총평**: Wang et al. (2019)의 "early-career setback" 패러다임을 스포츠로 확장한 견실한 실증 연구로, 두 가지 독립적 스포츠 맥락과 다양한 robustness check가 인상적이나, 메커니즘 규명 없이 현상 기술에 머물러 있어 이론적 기여는 제한적이다.
