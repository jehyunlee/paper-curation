# Automating the practice of science: Opportunities, challenges, and implications

> **저자**: Sebastian Musslick, Laura K. Bartlett, Suyog H. Chandramouli, Marina Dubova, Fernand Gobet, Thomas L. Griffiths, Jessica Hullman, Ross D. King, J. Nathan Kutz, Christopher G. Lucas, Suhas Mahesh, Franco Pestilli, Sabina J. Sloman, William R. Holmes | **날짜**: 2025 | **Journal**: PNAS | **DOI**: 10.1073/pnas.2401238121

---

## Essence

과학 실천(scientific practice)의 자동화 범위와 한계를 체계적으로 평가한 perspective 논문으로, 자동화의 goal-related bounds (규범적/인식론적 목표와의 정합성)와 technological bounds (입력 가용성, 계산 복잡도, 하드웨어 복잡도, 목표 주관성)를 분석 프레임워크로 제시한다. 현재 closed-loop 자동화 시스템(Adam, A-Lab, AutoRA)의 성과와 한계를 검토하고, LLM의 역할, 그리고 "automation paradox" 등 실천적/윤리적 함의를 논의한다.

## Motivation

- **알려진 것**: 자동화가 산업을 혁신한 것처럼 과학 연구에서도 가설 생성(AlphaFold), 재료 발견(GNoME), 실험 설계(Bayesian optimization) 등에 자동화가 적용되고 있음
- **Gap**: 과학 실천 자동화의 범위와 한계에 대한 체계적 평가가 부족하며, 기술적 가능성과 목표 정합성, 윤리적 함의를 통합적으로 다루는 논의가 필요
- **왜 중요한가**: AI, LLM, 로보틱스의 급속한 발전으로 과학 자동화의 범위가 확대되고 있으나, 인간 과학자의 역할, 교육, 평가 체계, 편향, 책임 등 근본적 질문에 답해야 함
- **접근법**: 과학 실천의 각 단계(가설 생성, 실험 설계, 데이터 수집, 통계/과학적 추론)를 자동화 관점에서 분석하고, 기회/과제/함의를 다학제적 시각에서 논의

## Achievement

1. **자동화 가능성의 4요인 프레임워크**: 입력 가용성/품질, 계산 복잡도, 하드웨어 복잡도, 목표 주관성의 4차원으로 과학 과제의 자동화 난이도를 체계적으로 분류
2. **Closed-loop 자동화 시스템의 비교 분석**: Adam (기능 유전체학, 효모 orphan enzyme 발견), Eve (약물 재배치, triclosan의 항말라리아 효과 발견), A-Lab (무기 분말 자율 합성), AutoRA (행동과학 online 실험), LLM-based AI Scientist (ML 연구 자동화, 논문 1편당 ~15 USD)
3. **Goal-related bounds의 이원적 분석**: 규범적 목표 (사회적 가치)와 인식론적 목표 (이해 vs. 예측)의 긴장 관계 -- 자동화가 예측력을 높이지만 인간 이해를 제한할 수 있는 epistemic dilemma 지적
4. **"Automation paradox" 개념 적용**: 자동화된 시스템이 효율적일수록 인간 감독이 더 중요해진다는 역설 -- 오류 누적의 cascade 위험
5. **LLM의 과학적 역할 평가**: 문헌 합성 (수천~수백만 편), 가설 생성, 실험 설계 공간 확장, 연구 문서화에서의 잠재력과 한계 (기존 지식 재발견 위험, 사기/재현 불가 논문 포함 위험)

## How

- **구조**: Perspective article로, 과학 실천의 자동화를 bounds (what should/can automation achieve) -> current state -> opportunities -> challenges -> implications의 흐름으로 논의
- **범위**: 생물학, 화학, 재료과학, 심리학, 신경과학, 수학, 물리학 등 다양한 분야의 자동화 사례를 132개 참고문헌으로 커버
- **분석 프레임워크**: Fig. 1의 4요인 모델 (입력 가용성, 계산 복잡도, 하드웨어 복잡도, 목표 주관성)과 Fig. 2의 3개 closed-loop 시스템 비교 다이어그램

## Originality

- **자동화의 Goal-related vs. Technological bounds 이원 분석**: 과학 자동화를 "할 수 있는가"(기술적)와 "해야 하는가"(규범적/인식론적)의 두 축으로 분리하여 분석한 독창적 프레임워크
- **Epistemic dilemma의 명시적 정의**: 자동화가 예측 정확도를 높이면서 동시에 인간 이해를 저해할 수 있다는 기초과학과 응용과학 간의 근본적 긴장 관계를 명확히 공식화
- **Closed-loop 시스템의 체계적 비교**: Adam, A-Lab, AutoRA를 통일된 다이어그램으로 비교하여, 각 시스템에서 인간이 제공하는 지식/프로세스(점선 박스)와 자동화된 부분을 시각적으로 구분
- **Automation paradox의 과학 맥락 적용**: 산업 자동화 이론인 Bainbridge의 "ironies of automation"을 과학 발견에 최초로 체계적으로 적용

## Limitation & Further Study

### 저자들이 언급한 한계

- Closed-loop 자동화가 현재 명확히 정의된 공학적/발견 문제에 한정
- 데이터 가용성/품질, 계산 복잡도, 하드웨어 한계, 목표 주관성이 기초과학에서의 자동화를 근본적으로 제약
- 인지과학에서의 과학적 발견은 무한한 데이터가 있어도 계산적으로 intractable할 수 있음
- LLM이 기존 가설/실험을 재발견할 위험, 사기 논문 포함 시 오류 전파 위험
- 자동화된 연구의 책임 소재 불분명 (시스템 개발자 vs. 사용자 vs. 결과 적용자)

### 자체판단 아쉬운 점

- Perspective 논문으로서 실증적 데이터나 정량적 분석이 부족하며, 주로 정성적 논의에 의존
- 자연과학(물리학, 화학)에서의 자동화 성공 사례에 비해 사회과학/행동과학 사례가 상대적으로 초기 단계에 치중
- LLM의 과학적 역할에 대한 논의가 다소 일반적이며, 구체적 평가 기준이나 benchmark 제시 부족
- 자동화의 경제적 비용-편익 분석이 거의 없음 (A-Lab 등의 투자 대비 성과 정량화 필요)

### 후속 연구

- 과학 분야별 자동화 성숙도 평가 지표(readiness index) 개발
- Closed-loop 시스템의 발견 효율성을 인간 연구자 대비 정량적으로 비교하는 benchmark 연구
- LLM 기반 과학 에이전트의 hallucination 및 오류 전파 메커니즘 분석
- 자동화된 과학 연구의 peer review 체계 재설계
- Automation paradox를 실증적으로 검증하는 메타과학 연구

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 4/5 |
| Technical Soundness | 3/5 |
| Significance | 4/5 |
| Clarity | 5/5 |
| Overall | 4/5 |

**총평**: 과학 실천 자동화의 범위와 한계를 goal-related/technological bounds로 구분하고, epistemic dilemma와 automation paradox라는 핵심 개념을 과학 맥락에 적용한 통찰적 perspective이다. 다만 정성적 논의 중심이라 실증적 근거가 부족하며, 급변하는 LLM 생태계에서의 구체적 방향 제시가 아쉽다.
