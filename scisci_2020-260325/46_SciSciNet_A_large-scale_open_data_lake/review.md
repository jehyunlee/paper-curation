# SciSciNet: A large-scale open data lake for the science of science research

> **저자**: Zihang Lin, Yian Yin, Lu Liu, Dashun Wang | **날짜**: 2023-06-01 | **Journal**: Scientific Data | **DOI**: 10.1038/s41597-023-02198-9

---

## Essence
과학학(science of science) 연구를 위한 통합 데이터 인프라를 어떻게 구축할 수 있는가? SciSciNet은 1억 3,400만 편 이상의 과학 출판물과 펀딩(NIH, NSF), 특허 인용, 임상시험, 미디어/소셜미디어 언급 등 수백만 개의 외부 연결을 포괄하는 대규모 오픈 데이터 레이크다. 전처리 단계와 분석 선택을 상세히 문서화하고, 자주 사용되는 지표(disruption index, novelty, interdisciplinarity 등)를 사전 계산하여 제공함으로써, 진입 장벽 낮추기, 중복 노력 감소, 재현성 향상, 아이디어 다양성 확대에 기여한다.

## Motivation
과학학 커뮤니티는 급격히 성장하면서 세 가지 핵심 도전에 직면했다: (1) 산재한 데이터셋과 그 연결을 추적하기 어려움, (2) 복잡한 전처리에서 연구자마다 다른 분석 선택이 재현성을 저해, (3) 정교한 지표 계산에 상당한 시간·자원 투자가 필요. 공통 데이터 자원이 없어 이러한 문제가 중복적으로 발생하고 있었다.

## Achievement
1. **1억 3,400만+ 출판물** 메타데이터 통합 (OpenAlex/MAG 기반)
2. **상류-하류 연결**: NIH/NSF 펀딩 → 출판물 → 특허 인용, 임상시험, 미디어 언급
3. **사전 계산 지표**: disruption index(CD₅), novelty(Uzzi et al. z-score), interdisciplinarity(Rao-Stirling), 팀 크기, 경력 연차 등
4. **상세 문서화**: 전처리 단계, 분석 선택, 데이터 검증 방법을 투명하게 공개
5. **커뮤니티 기여 모델**: 연구자들이 새로운 지표와 데이터를 추가할 수 있는 구조

## How
- **핵심 데이터**: OpenAlex/MAG 기반 출판물, 저자, 기관, 저널 메타데이터
- **외부 연결**: NIH RePORTER, NSF Awards, PatentsView, ClinicalTrials.gov, Altmetric
- **지표 계산**: Python 기반 대규모 계산, 검증을 위한 기존 연구 재현
- **배포**: 공개 다운로드, 정기 업데이트 예정
- **검증**: 여러 기존 연구의 주요 발견을 SciSciNet 데이터로 재현

## Originality
- 과학학 연구를 위한 **최초의 포괄적 오픈 데이터 레이크** — 출판물, 펀딩, 사회적 영향을 하나로 통합
- "데이터 인프라"로서 **사전 계산 지표 + 교차 연결 + 커뮤니티 기여**를 결합한 모델
- 전처리와 분석 선택의 투명한 문서화로 **재현성 표준** 제시

## Limitation & Further Study
### 저자들이 언급한 한계
- OpenAlex/MAG의 메타데이터 품질에 의존
- 모든 기존 데이터셋을 포괄하지 못함
- 지표 계산의 특정 분석 선택이 모든 연구 질문에 최적이 아닐 수 있음

### 리뷰어 판단 아쉬운 점
- MAG 서비스 종료(2021) 이후 OpenAlex로의 전환이 데이터 연속성에 미치는 영향 불확실
- 지표의 사전 계산이 오히려 "블랙박스" 사용을 조장할 위험 — 연구자가 지표의 한계를 인식하지 못할 수 있음
- 업데이트 주기와 지속가능성에 대한 구체적 계획이 불명확

### 후속 연구
- Scopus/WoS 등 상업적 데이터와의 교차 검증
- 실시간 또는 정기적 데이터 업데이트 체계 구축
- 표준화된 API를 통한 프로그래밍적 접근 확대

## Evaluation
| 항목 | 점수 |
|------|------|
| Novelty | 4/5 |
| Technical Soundness | 5/5 |
| Significance | 5/5 |
| Clarity | 5/5 |
| Overall | 5/5 |

**총평**: 과학학 연구의 데이터 인프라를 혁신적으로 통합한 커뮤니티 자원으로, 분야의 재현성과 접근성을 근본적으로 개선할 잠재력을 가진다.
