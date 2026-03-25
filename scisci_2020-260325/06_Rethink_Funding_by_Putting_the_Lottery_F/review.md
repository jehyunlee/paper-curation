# Rethink Funding by Putting the Lottery First

> **저자**: Finn Luebber, Sören Krach, Marina Martinez Mateo, Frieder M. Paulus, Lena Rademacher, Rima-Maria Rahal, Jule Specht | **날짜**: 2023 | **Journal**: Nature Human Behaviour | **DOI**: 10.1038/s41562-023-01649-y

---

## Essence

연구비 배분 과정의 편향을 줄이려면 추첨(lottery)을 심사 마지막 단계가 아닌 **맨 처음 단계에 배치**해야 한다. 시뮬레이션 결과, 'pre-lottery' 시나리오는 기존 1단계(R01), 2단계(ERC), tiebreaker lottery(SNSF) 방식 대비 매몰 비용(sunk cost)을 대폭 줄이면서도 다양성(diversity)과 연구 품질(quality)을 동시에 개선할 수 있다.

## Motivation

- **알려진 것**: 동료심사(peer review) 기반 연구비 배분은 연구 생산성 예측력이 낮고, 선임·명성·소속·성별 등 체계적 편향이 심사 전 과정에 내재되어 있다.
- **문제**: SNSF, Volkswagen Foundation 등이 도입한 tiebreaker lottery는 심사의 **마지막** 단계에서만 작동하므로, 그 이전 단계에서 이미 발생한 entry bias와 review bias를 해소하지 못한다.
- **왜 중요한가**: 국제 펀딩 기관의 성공률이 7%까지 떨어지는 상황에서 탈락 제안서에 투입되는 자원 낭비가 연구 자체의 가치에 필적하며, 소외 집단은 거절의 상대적 비용이 더 커서 지원 자체를 포기하는 악순환이 발생한다.
- **접근법**: 4가지 펀딩 시나리오(1-stage, 2-stage, tiebreaker lottery, pre-lottery)를 비용·다양성·품질 측면에서 시뮬레이션하는 Shiny 앱 'GrantInq'를 개발하고, pre-lottery의 우위를 논증한다.

## Achievement

1. **GrantInq Shiny 앱 개발**: 연구자, 정책입안자, 펀딩 기관이 다양한 펀딩 시나리오의 비용·다양성·품질 효과를 시뮬레이션할 수 있는 오픈소스 도구를 제공했다 (1,000회 시뮬레이션 기반).
2. **Pre-lottery 시나리오의 비용 우위**: 기존 시나리오 대비 매몰 비용이 현저히 낮다. 지원자가 추첨에 당첨된 후에만 제안서를 작성하므로 탈락에 따른 자원 낭비가 최소화된다.
3. **다양성 개선 효과**: Pre-lottery는 entry bias(자기 선택 편향)를 원천적으로 제거하여, 여성·초기경력 연구자·소수집단의 참여 기회를 균등화한다.
4. **혁신 편향(innovation bias) 완화**: 기존 경쟁적 심사는 보수적·점진적 연구에 유리하나, pre-lottery + 규범적 심사(normative review) 방식은 혁신적·탐색적 아이디어의 펀딩 가능성을 높인다.
5. **규범적 심사(normative review) 제안**: 경쟁적 순위 매기기 대신 저널 피어리뷰와 유사한 규범적 심사를 도입하고, 추첨 당첨자 전원에 대한 사전 예산 확보를 주장했다.

## How

- **시뮬레이션 도구**: R Shiny 앱 'GrantInq' (GitHub 공개, OSI Lubeck 호스팅)
- **비교 시나리오 4종**: (1) 1단계 full proposal 심사 (R01/DFG형), (2) 2단계 synopsis + oral defence (ERC형), (3) full proposal 심사 후 tiebreaker lottery (SNSF형), (4) pre-lottery 후 full proposal 규범적 심사
- **시뮬레이션 조건**: 1,000회 반복, 다양한 사전 가정(entry bias, review bias, 성별 비율 등) 적용
- **평가 지표**: 매몰 비용(sunk costs), 프로세스 비용(process costs, MU 단위), 다양성(성별 기반 비율), 아이디어 품질(AU 단위)

## Originality

- **추첨 시점의 전환**: 기존 논의가 tiebreaker(마지막 단계) 추첨에 집중된 반면, 본 논문은 추첨을 **첫 번째 단계**로 이동시키는 발상의 전환을 제시했다.
- **정량적 시뮬레이션 프레임워크**: 펀딩 시나리오의 비용·다양성·품질을 동시에 모델링하는 오픈소스 시뮬레이션 도구를 최초로 제공했다.
- **프로세스 역전(reversed process)**: 연구자가 먼저 지원하는 것이 아니라, 추첨에 당첨된 후 제안서를 작성하는 역발상 프로세스를 제안했다.

## Limitation & Further Study

### 저자들이 언급한 한계
- 본 논문은 3페이지 Comment 형식으로, 시뮬레이션의 구체적 파라미터와 민감도 분석 결과가 상세히 제시되지 않았다 (Shiny 앱 참조 유도).
- 다양한 가정(assumptions)에 따라 결과가 달라질 수 있음을 인정하며, 투명한 모델링의 필요성을 강조했다.

### 리뷰어 판단 아쉬운 점
- **실증 검증 부재**: 시뮬레이션 기반 주장이며, 실제 pre-lottery 시스템을 운영한 기관의 데이터가 없다. 현실의 제도적·정치적 저항에 대한 논의가 부족하다.
- **품질 필터링 우려**: Pre-lottery로 선발된 연구자가 해당 분야의 실질적 역량을 갖추었는지에 대한 품질 보장 메커니즘이 불명확하다. "PhD 보유자 전원 자동 등록"이라는 기준은 지나치게 단순할 수 있다.
- **규범적 심사의 구체성 부족**: 경쟁적 심사 대비 규범적 심사가 어떻게 작동하는지, 탈락 기준이 무엇인지에 대한 구체적 설계가 제시되지 않았다.
- **분야별 차이 미고려**: STEM, 인문사회, 예술 등 분야별로 연구비 규모와 심사 문화가 크게 다른데, 이에 대한 차별화된 분석이 없다.

### 후속 연구
- 실제 펀딩 기관에서 pre-lottery 파일럿 프로그램을 운영하고 그 효과를 실증적으로 검증하는 연구가 필요하다.
- 분야별·규모별로 최적의 추첨-심사 조합을 탐색하는 시뮬레이션 확장 연구가 가능하다.
- Pre-lottery 시스템 하에서 연구자의 행태 변화(도덕적 해이, 참여 동기 등)에 대한 행동경제학적 분석이 요구된다.

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 4/5 |
| Technical Soundness | 2/5 |
| Significance | 4/5 |
| Clarity | 4/5 |
| Overall | 3/5 |

**총평**: 연구비 배분의 추첨 시점을 처음으로 옮기자는 발상은 신선하고 시의적절하나, 3페이지 Comment 특성상 실증 근거와 구체적 제도 설계가 부족하여 정책 제언으로서의 설득력이 아직 제한적이다.
