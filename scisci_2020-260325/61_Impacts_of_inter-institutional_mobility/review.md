# Impacts of inter-institutional mobility on scientific performance from research capital and social capital perspectives

> **저자**: Yitong Chen, Keye Wu, Yue Li, Jianjun Sun | **날짜**: 06/2023 | **Journal**: Scientometrics | **DOI**: 10.1007/s11192-023-04690-w

---

## Essence

AI 분야 연구자 9,950명의 기관 간 이동(학계→학계 vs. 학계→산업계)이 개인 성과에 미치는 영향을 propensity score matching(PSM)과 negative binomial regression으로 분석한 결과, 학계→산업계(aca.ind) 이동은 research capital(논문 수, 교신저자 논문 수) 축적에는 부정적이나, social capital(공저자 수, 고영향력 공저자 수) 축적에는 학계→학계(aca.aca) 이동보다 더 긍정적인 영향을 미친다.

## Motivation

- **알려진 것**: 연구자 이동이 지식 전파와 혁신에 기여한다는 것은 널리 알려져 있으며, 학계 간 이동(aca.aca)의 성과 영향에 대한 연구는 다수 존재함
- **격차**: AI 분야에서 학계→산업계(aca.ind) 이동이 연구자 개인 수준의 성과에 미치는 영향에 대한 정량적 분석이 부족하며, 기존 연구는 주로 기업 수준의 혁신 성과에 초점을 맞춤
- **왜 중요한가**: AI 분야에서 학계→산업계 이동이 점점 보편화되고 있어(전체 이동 연구자의 20.79%), 이 이동 패턴이 개인 연구 역량과 협력 네트워크에 미치는 차별적 영향을 이해할 필요가 있음
- **접근법**: Microsoft Academic Graph(MAG) 데이터베이스에서 AI 톱 저널/학회 91,557편의 논문을 추출하고, PSM으로 내생성을 통제한 후 두 이동 패턴의 성과 차이를 비교

## Achievement

1. AI 분야 이동 연구자의 68.72%가 aca.aca 이동, 20.79%가 aca.ind 이동으로, 학계→산업계 이동이 기관 유형 간 이동의 대부분을 차지함
2. 연구자들은 평균 academic age 6년(이동 전) vs. 9년(이동 후)으로, 경력 초기에 이동하는 경향이 뚜렷함
3. PSM 기반 회귀분석 결과, aca.ind 이동은 논문 수(coeff = -0.094, p<0.05)와 교신저자 논문 수(coeff = -0.176, p<0.05) 모두에서 aca.aca 대비 부정적 영향
4. 반면 aca.ind 이동은 공저자 수(coeff = 0.161, p<0.05)와 고영향력 공저자 수(coeff = 0.248, p<0.05)에서 aca.aca 대비 긍정적 영향
5. 이동 전 기업 연구자와의 협력 비율이 aca.ind 그룹에서 24.94%로 aca.aca 그룹(11.70%)의 약 2배이며, 기업 공저자와의 사전 협력이 aca.ind 이동의 핵심 촉진 요인

## How

- **데이터**: MAG 데이터베이스에서 AI 분야 톱 4개 저널 + 7개 학회(AAAI, NeurIPS, ACL, CVPR, ICCV, ICML, IJCAI 등) 논문 91,557편 추출, 102,022명 저자 식별 후 9,950명 이동 연구자 확정
- **저자 동정(disambiguation)**: 2단계 프레임워크 -- (1) MAG 내 공저자/기관 정보 기반, (2) ORCID API 활용. Asian name 15명에 대한 검증에서 평균 F1 0.65→0.85로 개선
- **기관 분류**: 3,465개 기관을 키워드 기반 + 수작업으로 학계/산업계/기타로 분류
- **분석 방법**: PSM(exact matching, R MatchIt 패키지)으로 treatment(aca.ind, 795명) vs. control(aca.aca, 3,117명) 매칭 후, negative binomial regression 적용
- **변수**: 종속변수 4개(이동 후 논문 수, 교신저자 논문 수, 공저자 수, 고영향력 공저자 수), 매칭변수 6개(성별, 이동 전 academic age, 논문 수, 공저자 수, 기업 공저자 수, 고영향력 공저자 수)

## Originality

- Research capital과 social capital이라는 이중 프레임워크를 통해 이동 유형별 성과 차이를 체계적으로 분석한 점이 독창적
- AI 분야에 특화하여 학계→산업계 이동의 개인 수준 성과를 PSM으로 내생성을 통제하며 분석한 최초의 연구 중 하나
- 이동 전 기업 공저자 비율이 aca.ind 이동의 촉진 요인임을 정량적으로 입증

## Limitation & Further Study

### 저자들이 언급한 한계
- 내생성 요인을 완전히 제거할 수 없으며, PSM으로 줄일 수 있을 뿐임
- 연구자 성과 측정 지표(논문 수, 공저자 수)의 신뢰성에 대한 논쟁이 존재

### 리뷰어 판단 아쉬운 점
- MAG 데이터베이스가 2021년 서비스 종료되어 재현성에 한계가 있음
- 이동의 정의가 "첫 번째 기관 변경"으로만 한정되어, 다중 이동이나 겸직(dual affiliation) 패턴을 포착하지 못함
- 논문의 질적 측면(인용 수, impact factor 등)은 종속변수에 포함되지 않아 research capital의 측정이 양적 지표에 치우침
- gender-guesser 패키지 기반 성별 추정은 특히 아시아 이름에서 정확도가 낮을 수 있으며, null 값(2.57%)을 남성으로 가정한 처리가 편향을 유발할 가능성
- "고영향력 연구자"의 기준을 상위 10%로 설정한 것은 다소 관대하며, 이에 대한 민감도 분석이 부족

### 후속 연구
- 인용 수, h-index 등 질적 성과 지표를 포함한 확장 분석
- 다중 이동 경로 및 "brain circulation"(산업계→학계 복귀) 패턴의 장기적 성과 추적
- AI 이외 분야와의 비교 연구를 통한 분야별 이동 효과의 이질성 검증

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 3/5 |
| Technical Soundness | 3/5 |
| Significance | 3/5 |
| Clarity | 3/5 |
| Overall | 3/5 |

**총평**: Research capital과 social capital 프레임워크를 통해 AI 분야 연구자의 이동 유형별 성과 차이를 체계적으로 분석한 유의미한 연구이나, 성과 측정이 양적 지표에 한정되고 MAG 데이터의 서비스 종료로 재현성에 한계가 있어 방법론적 보완이 필요하다.
