# Data integrity in materials science in the era of AI: balancing accelerated discovery with responsible science and innovation

> **저자**: Nik Reeves-McLaren, Sarah Moth-Lund Christensen | **날짜**: 2026 | **Journal**: Journal of Materials Chemistry A | **DOI**: 10.1039/D5TA05512A

---

## Essence

AI 시대 재료과학에서의 데이터 무결성(data integrity) 위기를 체계적으로 분석하고, 이를 해결하기 위한 다각적 프레임워크를 제안하는 관점(perspective) 논문이다. 전문가도 AI 생성 현미경 이미지를 실제 실험 데이터와 구별하지 못하며(40-51% 정확도), 재료 특성화 분석의 20-30%에 기본 오류가 존재하고, GenAI가 물리 원리를 위반하는 그럴듯한 데이터 조작 코드를 1시간 내에 생성할 수 있다는 구체적 증거를 제시한다.

## Motivation

- **알려진 것**: AI가 재료 발견을 가속화하고 있으며(GNoME의 220만 안정 결정 구조 등), GenAI 도구가 연구 전반에 빠르게 확산 중
- **Gap**: AI의 혁신적 잠재력에 대한 낙관론이 지배적이나, 학습 데이터의 편향, 데이터 조작의 용이성, "블랙박스" 문제 등 데이터 무결성에 대한 체계적 논의가 부족
- **왜 중요한가**: 재료과학 학습 데이터의 20-30%가 오류를 포함하며, XPS 분석 논문의 40% 이상이 결론에 영향을 미칠 수 있는 오류를 포함 -- 이러한 데이터로 학습된 AI 모델은 오류를 증폭시킬 위험
- **접근법**: 윤리적 거버넌스, 전문 표준, AI 기반 품질 관리, 비판적 AI 리터러시, 실무 체크리스트의 다면적 프레임워크 제안

## Achievement

1. **데이터 무결성 위협의 체계적 분류**: (1) 광범위한 오류와 미활용 검증 방법, (2) 의도적 데이터 조작과 합성 데이터 위험, (3) AI 학습 데이터셋의 내재적 편향, (4) 투명성/설명가능성/인간 감독의 과제 -- 4가지 범주로 정리
2. **구체적 위험 사례 제시**: GenAI로 1시간 내에 AFM/STEM/TEM 가짜 이미지 생성 가능, 250명 전문가가 랜덤 수준으로만 구별 (p > 0.05); 회절 데이터의 이차상 피크 제거 및 배터리 테스트 데이터 노이즈 제거 코드 생성 시연
3. **모듈식 데이터 무결성 체크리스트**: 핵심 모듈(모든 제출물 적용) + 기법별 모듈(XRD/Rietveld 정제, 전기화학 배터리 테스트)의 확장 가능한 검증 프레임워크 제안
4. **AI 학습 세트 검수 프레임워크**: (i) 출판 상태 확인(철회/정정), (ii) 공개 사후 검토 플랫폼 스크리닝, (iii) 통계적 이상/물리적 비합리성 프로그래밍 검사의 3단계 데이터 검수 절차
5. **구조적 신뢰성 향상 방안**: Adversarial collaboration, Registered Reports, Red Team 접근법 등 타 분야 검증 방법론의 재료과학 도입 제안

## How

- **문헌 분석**: 최근 연구(Davydiuk et al. 2025, Christmann 2025, Major et al. 2020 등)를 종합하여 재료과학 데이터 무결성의 현황 진단
- **위협 시나리오 구성**: 태양전지 fill factor 조작(0.83 → 0.89), Tafel slope 위조, EIS Nyquist plot 단순화 등 에너지 재료 분야의 구체적 조작 시나리오 제시
- **거버넌스 분석**: NIST 신뢰 AI, UNESCO AI 윤리, EU 윤리 가이드라인, SciHorizon 프레임워크, Nature Portfolio 정책 등 기존 규제 체계 검토
- **체크리스트 설계**: 임상 연구의 INSPECT-SR 기준에서 영감을 받아, 핵심 데이터 무결성 모듈과 기법별 검증 모듈로 구성된 모듈식 체크리스트(Table 1) 제안
- **교육 사례**: Freie Universitat Berlin, Cornell Engineering "AI for materials" 과정, Harvard "Embedded EthiCS" 프로그램 등 교육 실천 사례 소개

## Originality

- **재료과학 특화 데이터 무결성 논의**: 일반적 AI 윤리가 아닌, Rietveld 정제의 chi-squared 오해, Kramers-Kronig 관계 미검증, XPS 오류율 등 재료과학 고유의 기술적 문제에 초점
- **GenAI 데이터 조작 위험의 실증적 입증**: 추상적 우려가 아닌, 1시간 내 가짜 현미경 이미지 생성 및 전문가 구별 불가라는 구체적 실험 결과 활용
- **모듈식 검증 프레임워크**: 임상 연구의 체계적 리뷰 품질 관리(INSPECT-SR)를 재료과학에 최초로 적용한 접근
- **MAIF(Minimal Arrangement of Instrument Files)**: 구조화된 원시 기기 파일의 의무 기탁을 통해 검증 가능성을 높이는 실용적 제안
- **학습 데이터 편향의 재료과학적 구체화**: 평형상 산화물 시스템 과대표현 문제를 AI 학습 데이터 관점에서 명시적으로 지적

## Limitation & Further Study

### 저자들이 언급한 한계

- 제안된 체크리스트가 XRD/Rietveld과 전기화학 배터리 테스트 2가지 기법에만 초기 모듈 제공 -- 커뮤니티 기여를 통한 확장 필요
- 제안된 프레임워크가 일회성 해결책이 아니며, 지속적 참여와 발전이 필요한 ongoing process

### 자체판단 아쉬운 점

- Perspective 논문의 한계상 제안된 프레임워크의 실효성에 대한 실증적 검증이 부재 -- 체크리스트 적용 전후의 오류 감소율, 리뷰어 부담 변화 등 미측정
- AI 기반 사기 탐지 도구(Proog 등)의 재료과학 특성화 데이터에 대한 실제 탐지 성능이 논의되지 않음
- 학습 데이터 편향의 정량적 분석이 부족 -- "overrepresent equilibrium-phase oxide systems"라는 주장에 대한 구체적 통계 미제시
- 개발도상국이나 소규모 연구기관에서의 원시 데이터 의무 기탁 정책의 실현 가능성과 비용 부담에 대한 논의 부재
- 기존 paper mill 문제(약 800편 결정학 논문)와 AI 기반 새로운 위협의 규모 비교가 정량적으로 이루어지지 않음

### 후속 연구

- 제안된 모듈식 체크리스트의 파일럿 적용 및 효과 검증 연구
- 재료과학 특화 AI 사기 탐지 시스템(현미경 이미지, 회절 데이터, 전기화학 데이터) 개발
- 주요 데이터베이스(Materials Project, ICSD, COD)의 편향 정량적 감사(audit)
- AI 학습 세트 검수 프레임워크의 자동화 도구 개발
- 다양한 특성화 기법(SEM/TEM, XPS, Raman, NMR 등)으로의 기법별 검증 모듈 확장

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 3/5 |
| Technical Soundness | 3/5 |
| Significance | 5/5 |
| Clarity | 5/5 |
| Overall | 4/5 |

**총평**: AI가 재료과학을 혁신하는 시점에서 데이터 무결성이라는 근본적 문제를 정면으로 다룬 시의적절하고 중요한 관점 논문이다. GenAI의 데이터 조작 위험을 구체적 사례로 입증하고, 임상 연구의 검증 방법론을 재료과학에 적용한 모듈식 체크리스트는 실용적 가치가 높다. 다만 perspective 논문의 특성상 제안의 실증적 검증이 부재하며, "garbage in, garbage out"의 경고를 넘어 구체적 해결 도구의 개발과 배치가 후속 과제로 남는다.
