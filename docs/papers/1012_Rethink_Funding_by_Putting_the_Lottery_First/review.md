---
title: "1012_Rethink_Funding_by_Putting_the_Lottery_First"
authors:
  - "Finn Luebber"
  - "Sören Krach"
  - "Marina Martinez Mateo"
  - "Frieder M. Paulus"
  - "Lena Rademacher"
date: "2023"
doi: "10.1038/s41562-023-01649-y"
arxiv: ""
score: 4.0
essence: "연구비 배분 초기 단계에 추첨(lottery)을 도입하여 기존의 편향된 동료평가(peer review) 기반 경쟁적 배분 시스템을 개선하고, GrantInq 시뮬레이션 앱을 통해 다양한 자금배분 시나리오의 비용, 다양성, 품질 효과를 비교 분석한다."
tags:
  - "cat/Research_Quality_and_Demographics"
  - "sub/Publishing_and_Incentives"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Luebber et al._2023_Rethink Funding by Putting the Lottery First.pdf"
---

# Rethink Funding by Putting the Lottery First

> **저자**: Finn Luebber, Sören Krach, Marina Martinez Mateo, Frieder M. Paulus, Lena Rademacher, Rima-Maria Rahal, Jule Specht | **날짜**: 2023 | **DOI**: [10.1038/s41562-023-01649-y](https://doi.org/10.1038/s41562-023-01649-y)

---

## Essence

![Figure 1](figures/fig1.webp)

*Fig. 1 | Exemplary grant application scenarios. The flowchart illustrates four*

연구비 배분 초기 단계에 추첨(lottery)을 도입하여 기존의 편향된 동료평가(peer review) 기반 경쟁적 배분 시스템을 개선하고, GrantInq 시뮬레이션 앱을 통해 다양한 자금배분 시나리오의 비용, 다양성, 품질 효과를 비교 분석한다.

## Motivation

- **Known**: 동료평가와 보조금 배분 결정은 전반적인 연구비 생산성을 예측하지 못하며, 심사자의 인지적 편향(reviewer bias), 신분편향(seniority bias), 성차별, 인종차별 등이 자금배분 과정에 깊숙이 근거하고 있다.
- **Gap**: 기존 연구들은 최종 단계에서의 추첨만을 제안했으나, 이는 신청 의사결정(entry bias)과 초기 심사 단계의 편향(review bias)을 해결하지 못한다는 점이 미해결된 문제다.
- **Why**: 연구 자금배분은 과학의 방향을 결정하고 미래 지식을 형성하므로, 편향과 차별을 제거하고 소외된 공동체 연구자들의 기회균등을 보장하는 것이 학문 생태계의 다양성과 건강성을 위해 필수적이다.
- **Approach**: 초기 단계 추첨(pre-lottery) 모델을 제안하여 자동 선정된 연구자만이 제안서 작성 기회를 얻도록 역행 프로세스를 구현하고, GrantInq 시뮬레이션 도구로 일원형(one-stage), 이원형(two-stage), 최종 추첨형(tiebreaker lottery), 초기 추첨형(pre-lottery) 등 네 가지 시나리오를 비교 평가한다.

## Achievement

![Figure 2](figures/fig2.webp)

*Fig. 2 | Evaluation of the four exemplary funding scenarios with regard to*

- **초기 추첨 도입의 편향 감소 효과**: 신청 단계의 자기선택(self-selection)으로 인한 진입 편향(entry bias)을 제거하고, 전체 심사 과정을 거치기 전에 구조적 장벽을 완화하여 역사적으로 소외된 집단(여성, 초기경력자, 소수집단 등)의 참여기회를 대폭 확대
- **비용 효율성 개선**: 최종 거부된 제안서에 투입된 침몰 비용(sunk cost)과 심사자의 낭비된 검토 시간을 급격히 감소시키고, 기존 시스템의 비효율적 마중복 투고(multiple submissions) 관행 제거
- **혁신 아이디어 장려**: 규범적 심사(normative review) 도입으로 경쟁적 평가 환경에서의 혁신 편향(innovation bias)을 완화하고 파격적이고 고위험-고보상의 연구 제안에 대한 지원 확대
- **GrantInq 시뮬레이션 플랫폼 개발**: 자금배분 정책 의사결정자, 연구자, 펀딩기관이 사용 가능한 대화형 도구로서 다양한 배분 시나리오의 비용, 다양성, 품질 지표를 정량적으로 비교 가능하게 함

## How

![Figure 1](figures/fig1.webp)

*Fig. 1 | Exemplary grant application scenarios. The flowchart illustrates four*

- 네 가지 자금배분 시나리오(일원형 R01, 이원형 ERC, 최종 추첨형 SNSF, 초기 추첨형) 설계 및 각 단계별 편향 지점 분석
- GrantInq 웹 애플리케이션(Shiny app) 개발으로 사전에 정의된 가정 하에서 1,000회 시뮬레이션 실행
- 각 시나리오별 침몰 비용(sunk cost), 프로세스 비용(process cost), 성별 다양성 지수, 아이디어 품질(Arbitrary Units) 측정 및 시각화
- 초기 추첨 모델에서 자동 선정(automated selection) 또는 가입 호출(call for enrollment) 방식으로 PhD 보유자 등 자격자 풀 구성
- 추첨 당선자만이 제안서 작성 단계로 진입하는 역행 프로세스(reversed process) 구현
- 사전 자금 확보(secured funding) 원칙으로 경제적 이유의 거부 배제 및 규범적 심사 도입

## Originality

- 기존 '최종 단계 추첨'에서 벗어나 **초기 단계 추첨**의 중요성을 이론적·경험적으로 강조한 혁신적 제안", '자금배분 과정의 **역행 구조**(신청 → 추첨 → 작성)로 진입 편향과 신청 단계 자기선택 문제를 근본적으로 해결
- 시뮬레이션 기반 정책 평가 도구(GrantInq)를 통해 추상적 개념이 아닌 정량화된 비용-효과 분석 제공
- 신청과정의 비효율성(낭비된 심사 시간, 침몰 비용)을 과학적으로 계량화하고 정책 개혁의 경제적 논거 제시

## Limitation & Further Study

- **시뮬레이션 가정의 단순화**: 실제 연구자 행동, 제안서 품질, 편향의 크기 등이 현실만큼 복잡하지 않을 가능성
- **문화적·제도적 저항**: 기존 동료평가 문화와 심사자 권력 구조의 변화에 대한 학계의 저항 미예측
- **초기 추첨 풀의 정의 문제**: 자격 기준(PhD, 학위 취득 시기 등) 설정에서 새로운 형태의 배제 가능성
- **후속 연구 필요**: 초기 추첨 모델의 실제 도입 사례에서 다양성, 품질, 비용 효과성 검증 필요
- **장기 영향 분석 부재**: 초기 추첨 도입이 장기적 연구 혁신성, 연구자 커리어 발전, 학문 생태계에 미치는 영향 평가 필요

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 논문은 연구비 배분 시스템의 구조적 편향 문제를 정면으로 다루며, 초기 단계 추첨이라는 급진적이면서도 논리적인 해결책을 제시한다. 시뮬레이션 도구(GrantInq)를 통해 추상적 논의를 정량화된 정책 평가로 전환한 점에서 독창성과 실용성이 높으나, 실제 제도 도입 시 다양한 저항과 부작용 가능성에 대한 추가 검토가 필요하다.

## Related Papers

- 🔄 다른 접근: [[papers/1036_The_Matthew_effect_in_science_funding/review]] — Matthew effect로 인한 펀딩 불평등을 해결하기 위한 구체적인 추첨 기반 대안 시스템을 제안한다.
- 🏛 기반 연구: [[papers/941_Big_Names_or_Big_Ideas_Do_Peer-Review_Panels_Select_the_Best/review]] — 동료평가 패널의 선택 편향 분석이 추첨 시스템 도입의 필요성을 뒷받침하는 실증적 근거를 제공한다.
- 🧪 응용 사례: [[papers/964_Funding_the_Frontier_Visualizing_the_Broad_Impact_of_Science/review]] — 과학 펀딩의 광범위한 영향을 시각화하여 추첨 시스템의 효과를 평가하고 최적화할 수 있다.
- 🔄 다른 접근: [[papers/1069_Breaking_the_gatekeepers_how_AI_will_revolutionize_scientifi/review]] — 복권 방식 펀딩을 통해 기존 권력 구조를 혁신하는 다른 접근법을 제시하여 AI 혁신과 비교할 수 있는 대안을 제공한다.
- 🔄 다른 접근: [[papers/1036_The_Matthew_effect_in_science_funding/review]] — 편향된 동료평가 시스템의 대안으로 추첨 방식을 제안하여 Matthew effect를 완화할 수 있는 방법을 제시한다.
- 🔄 다른 접근: [[papers/941_Big_Names_or_Big_Ideas_Do_Peer-Review_Panels_Select_the_Best/review]] — 기존 동료평가 시스템의 한계를 보완하기 위해 추첨제 도입을 우선시하는 근본적으로 다른 펀딩 방식을 제안한다.
