# Automated Extraction of Mechanical Constitutive Models from Scientific Literature using Large Language Models: Applications in Cultural Heritage Conservation

> **저자**: Rui Hu, Yue Wu, Tianhao Su, Yin Wang, Shunbo Hu, Jizhong Huang | **날짜**: 2026-02-18 | **Repository**: arXiv | **arXiv ID**: 2602.16551

---

## Essence

문화유산 보존을 위한 디지털 트윈 구축에 필요한 역학적 구성 방정식(constitutive model)과 보정 파라미터를 과학 문헌에서 자동 추출하는 2단계 에이전틱 프레임워크를 제안한다. 비용 효율적인 "Gatekeeper" 에이전트가 관련성을 필터링하고, 고성능 "Analyst" 에이전트가 Context-Aware Symbolic Grounding을 통해 수학적 모호성을 해결하며 정밀 추출을 수행한다. 2,000편 이상의 논문에서 113편의 핵심 문헌을 선별하여 185개 구성 모델 인스턴스와 450개 이상의 보정 파라미터로 구성된 구조화 데이터베이스를 구축하였으며, 추출 정밀도 80.4%, F1 점수 81.9%를 달성하였다.

## Motivation

- **알려진 사실**: 문화유산의 디지털 트윈은 구조적 거동 예측을 위해 유한요소해석(FEA)과 정확한 역학적 구성 모델을 필요로 함. 수십 년간 로마 콘크리트, 비잔틴 석조, 역사적 목재 등의 재료 특성 연구가 축적되어 있음
- **격차(Gap)**: 이 지식이 수천 편의 PDF 논문에 분산되어 있고, 명명법/방정식 형식/파라미터 정의가 비일관적이며, 통합 데이터베이스가 부재하여 "데이터 사일로" 문제 발생. 수학 기호의 문맥 의존적 의미(예: E가 영률/활성화 에너지/총에너지 중 어느 것인지)를 해결하는 symbolic grounding이 핵심 기술적 난제
- **접근법**: LLM 기반 2단계 에이전트(Gatekeeper + Analyst)로, coarse-to-fine 필터링과 Context-Aware Symbolic Grounding을 통해 비구조화 문헌을 구조화 데이터베이스로 변환

## Achievement

1. **대규모 문헌 필터링 및 추출**: 2,000편 이상에서 113편 핵심 문헌 선별, 185개 구성 모델 인스턴스 및 450+ 보정 파라미터 추출
2. **정량적 성능**: Precision 80.4%, Recall 83.3%, F1 81.9%, AUC 0.782, FPR 3.3%로 데이터베이스 오염 최소화
3. **수작업 90% 절감**: Human-in-the-loop 워크플로우로 전문가의 수동 문헌 검토 시간을 약 90% 감소
4. **물리적 타당성 추론 시연**: 점토 현탁액 논문에서 표 헤더의 스케일링 모호성(eta_inf x 10^3)을 물리적 도메인 지식으로 올바르게 해석하는 정성적 사례 제시
5. **웹 기반 플랫폼 구현**: 자동 수집(PDF 업로드 -> 자동 추출) 및 의미적 검색(재료 유형/역학 속성별 쿼리)을 지원하는 Heritage Materials Constitutive Database Platform 개발

## How

- **Stage I (Gatekeeper)**: 저비용 LLM이 논문 앞부분 ~8,000자를 읽고, 도메인 관련성(문화유산 재료), 이론적 내용(구성 모델 존재), 실험적 검증(파라미터 보정) 3가지 기준으로 이진 분류
- **Stage II (Analyst)**: 고성능 LLM이 전문(full-text)을 처리하여 (1) 유도 과정/기준 모델을 필터링하고 최종 구성 방정식 식별, (2) Context-Aware Symbolic Grounding으로 수학 기호-물리적 의미 매핑, (3) Schema-Constrained Decoding으로 5-tuple JSON 출력 (방정식, 기호 맵, 재료 메타데이터, 파라미터, 검증 방법)
- **오류 처리**: JSON 스키마 위반 시 오류 신호를 모델 컨텍스트에 피드백하는 폐루프 자기 수정
- **평가**: 113편 전체에 대해 고체역학 전문가가 222개 GT 엔티티 수동 주석, TP/FP/FN 기반 Precision/Recall/F1 산출
- **데이터 소스**: arXiv 물리/공학 카테고리에서 문화유산+고체역학 교차 키워드 검색

## Originality

문화유산 재료의 역학적 구성 모델이라는 고도로 전문화된 도메인에 LLM 기반 자동 추출을 적용한 최초의 시도이다. 핵심 기여는 Context-Aware Symbolic Grounding으로, 수학 기호의 물리적 의미를 문맥으로부터 확률적으로 해석하는 메커니즘이 기존 규칙 기반/NER 기반 추출과 차별화된다. Gatekeeper-Analyst의 2단계 coarse-to-fine 설계는 대규모 코퍼스 처리의 비용 효율성을 높이며, 추출 결과를 웹 플랫폼으로 연결한 end-to-end 워크플로우가 실용적이다.

## Limitation & Further Study

### 저자들이 언급한 한계
- F1 점수 ~82%로 완벽하지 않으며, 최종 데이터의 "마지막 1마일" 검증은 여전히 인간 전문가에게 의존
- 잔여 오류의 주요 원인은 오래된 PDF의 비표준 표 구조 파싱 실패이며, LLM의 의미적 추론 실패보다는 입력 품질 문제
- 문화유산 재료 도메인은 데이터가 희소하여("Data Poverty"), LLM의 사전 학습 지식에 의존하는 zero/few-shot 접근이 불가피

### 리뷰어 판단 아쉬운 점
- Gatekeeper와 Analyst에 사용된 구체적 LLM 모델명과 비용이 명시되지 않아 재현성이 부족
- arXiv만을 데이터 소스로 사용하여, 문화유산 보존의 핵심 문헌이 많이 게재되는 전문 저널(Construction and Building Materials, Journal of Cultural Heritage 등)이 누락됨
- 기존 materials informatics 도구(ChemDataExtractor, MatKG 등)나 다른 LLM 기반 추출 방법과의 비교 실험이 없음
- Symbolic Grounding의 정확도가 별도로 측정되지 않아, 기호 해석 오류와 방정식 식별 오류의 분리된 평가가 불가능
- 185개 모델/450개 파라미터라는 규모가 수십 년 문헌 축적량 대비 상당히 적어, arXiv 소스의 한계가 반영된 것으로 보임

### 후속 연구
- Scopus/WoS 등 전문 저널 데이터베이스로 소스 확장
- 멀티모달 입력(그림, 응력-변형률 곡선 등)의 직접 해석 통합
- 추출된 구성 모델의 FEA 시뮬레이션 자동 연결 검증
- 다른 재료 도메인(현대 건설 재료, 생체 재료 등)으로의 프레임워크 일반화

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 3/5 |
| Technical Soundness | 3/5 |
| Significance | 3/5 |
| Clarity | 4/5 |
| Overall | 3/5 |

**총평**: 문화유산 재료의 역학적 구성 모델 추출이라는 실용적이고 의미 있는 문제를 LLM 기반 에이전틱 프레임워크로 해결한 논문으로, 도메인 전문성과 AI 기술의 결합이 돋보인다. 그러나 arXiv 전용 소스의 한계, 기존 추출 도구와의 비교 부재, 구체적 모델 정보 미공개 등이 연구의 완성도를 낮추며, F1 82%의 성능도 자동 데이터베이스 구축에는 아직 human-in-the-loop 의존도가 높은 수준이다.
