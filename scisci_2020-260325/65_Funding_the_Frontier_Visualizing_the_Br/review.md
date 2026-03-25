# Funding the Frontier: Visualizing the Broad Impact of Science and Science Funding

> **저자**: Yifang Wang, Yifan Qian, Xiaoyu Qi, Yian Yin, Shengqi Dang, Ziqing Qian, Benjamin F. Jones, Nan Cao, Dashun Wang | **날짜**: 2025-09-19 | **Journal**: arXiv preprint | **DOI**: 10.48550/arXiv.2509.16323

---

## Essence

과학 펀딩의 다차원적 영향을 시각적으로 분석할 수 있는 웹 기반 시스템 Funding the Frontier(FtF)를 개발했다. 7M 연구 grants를 140M 논문, 160M 특허, 10.9M 정책 문서, 800K 임상시험, 5.8M 뉴스피드와 연결하는 18억 건의 인용 링크를 활용하여, 펀딩의 직접 성과(논문, 특허, 임상시험)뿐 아니라 사회적 파급효과(정책, 미디어, 시장)까지 통합적으로 탐색할 수 있는 최초의 사용자 지향 visual analytics 시스템이다.

## Motivation

- **알려진 것**: 과학 펀딩이 과학 발전과 사회적 혜택에 핵심적이라는 인식 확산. 기존 연구는 펀딩과 논문 산출 간 관계에 집중.
- **부족한 것**: 펀딩의 하류 활용(downstream uses) -- 특허, 정책, 임상시험, 미디어 등 과학이 사회에 영향을 미치는 다양한 경로에 대한 체계적 분석 도구가 부재. 기존 시스템(NIH RePORTER, Dimensions 등)은 주로 검색 엔진 수준이며, 펀딩의 광범위한 사회적 영향을 시각화하지 못함.
- **왜 필요한가**: 한정된 펀딩 자원의 효과적 배분을 위해 의사결정자(펀딩 기관, 정책 입안자, 대학 지도자)에게 펀딩 영향의 종합적 평가와 시각화가 필요.
- **접근 방식**: 전문가 인터뷰 기반 요구사항 분석, 대규모 이종 데이터 통합, SciBERT+XGBoost 예측 모델, coordinated view 시각화 설계.

## Achievement

1. **대규모 데이터 통합**: Dimensions(7M grants, 140M 논문, 160M 특허), Overton(10.9M 정책 문서), Altmetric(5.8M 뉴스), SciSciNet을 연결한 18억 건의 인용 링크 구축
2. **다차원 영향 측정 프레임워크**: Direct outcomes(논문, 특허, 임상시험) + Broader impacts(특허 인용, 임상시험 인용, 정책 인용, 뉴스 인용)의 체계적 지표 설계. Relative Impact Index(RII) 도입
3. **예측 모델**: SciBERT 임베딩 + XGBoost로 grant 초록에서 미래 영향 예측. 대부분의 impact 유형에서 AUC 0.6-0.8 수준의 예측 성능
4. **ImpactGlyph 시각화**: 물결 파문(ripple) 메타포를 활용한 다차원 영향 시각화 기법. 직접 성과와 광범위 영향을 동심원 형태로 표현
5. **전문가 평가**: 연방 펀딩 기관 프로그램 오피서, 민간 투자사 임원 등이 "이전에 접근할 수 없었던 새로운 정보"로 평가. Alzheimer 연구의 임상 영향 예측에서 질병 이해 → 사회적/생활 차원으로의 연구 방향 전환 트렌드 발견

## How

- **데이터**: Dimensions + Overton + Altmetric + SciSciNet (2000-2021년)
- **분석 모듈**: (1) 다차원 영향 지표 계산(Direct + Broader), (2) SciBERT 임베딩 → XGBoost 이진 분류로 grant의 미래 영향 예측
- **시각화 모듈**: React.js/D3.js/TypeScript 기반. Query View(필터링), Grant View(버블 맵), PI View(연구자 프로필), Impact Landscape View(다분할 그래프), Impact Type View, Impact Entity View의 coordinated views
- **레이아웃**: Force-directed layout + Bubble treemap + Impact Force/Containment Force/Collision Force의 하이브리드 배치
- **평가**: 정량적 모델 평가(AUC), 2개 case study(펀딩 기관 관점, 시각화 커뮤니티 관점), 전문가 인터뷰

## Originality

- 과학 펀딩의 직접 성과를 넘어 정책, 미디어, 시장, 임상 등 다차원적 사회 영향까지 통합 시각화한 최초의 시스템
- 18억 건의 인용 링크를 활용한 대규모 science ecosystem 매핑
- ImpactGlyph의 ripple 메타포를 통한 직관적 다차원 영향 시각화 설계
- 펀딩 의사결정자를 1차 사용자로 설정한 실용적 시스템 설계

## Limitation & Further Study

### 저자들이 언급한 한계
- 데이터 범위가 2000-2021년으로 한정되어 최신 트렌드 반영 제한
- 인용 기반 영향 측정의 inherent limitations -- 실제 사회적 영향과의 괴리 가능성
- 예측 모델이 grant 초록만을 입력으로 사용하여 연구팀 역량, 기관 자원 등 contextual factors 미반영
- Scalability 테스트가 제한적

### 리뷰어 판단 아쉬운 점
- 시스템 논문의 특성상 분석적 깊이보다 기술적 구현에 초점. 펀딩 영향에 대한 새로운 과학적 발견이나 인사이트가 제한적
- 예측 모델의 AUC가 0.6-0.8 수준으로, 실제 의사결정에 활용하기에는 정확도가 불확실
- 인과적 영향(펀딩이 실제로 이 성과를 야기했는가)과 상관적 연결(동일 주제의 grant와 patent가 존재)의 구분이 불명확
- 사용자 평가가 소수 전문가의 정성적 피드백에 의존하며, 정량적 사용성 평가(task completion time, accuracy 등)가 부족

### 후속 연구
- 실제 펀딩 기관에 배치(deployment)하여 의사결정에 미치는 영향 측정
- 인과 추론 방법론 적용으로 펀딩의 인과적 영향 분석
- 실시간 데이터 업데이트 파이프라인 구축
- 국가/지역 간 펀딩 영향 비교 분석 기능 추가

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 4/5 |
| Technical Soundness | 3/5 |
| Significance | 4/5 |
| Clarity | 4/5 |
| Overall | 4/5 |

**총평**: 과학 펀딩의 사회적 영향을 다차원적으로 시각화하는 야심찬 시스템으로, 18억 건의 인용 링크를 활용한 대규모 데이터 통합과 직관적 시각화 설계가 인상적이나, 시스템 논문 특유의 분석적 깊이 제한과 예측 모델의 실용성 검증이 향후 과제로 남는다.
