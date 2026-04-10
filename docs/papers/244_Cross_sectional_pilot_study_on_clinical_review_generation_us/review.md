---
title: "244_Cross_sectional_pilot_study_on_clinical_review_generation_us"
authors:
  - "Zining Luo"
  - "Yang Qiao"
  - "Xinyu Xu"
  - "Xiangyu Li"
  - "Mengyan Xiao"
date: "2025.03"
doi: "10.1038/s41746-025-01535-z"
arxiv: ""
score: 3.5
essence: "대규모 언어모델(LLM)이 생성한 임상 리뷰와 인간 저자의 리뷰를 체계적으로 비교한 결과, LLM이 빠르게 리뷰를 생성할 수 있지만 참고문헌 수가 적고, 논리적 일관성이 낮으며, 인용 정확도와 신뢰성이 부족함을 발견했다."
tags:
  - "cat/Academic_Peer_Review_Automation"
  - "sub/Expert_Review_Automation"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Luo et al._2025_Cross sectional pilot study on clinical review generation using large language models.pdf"
---

# Cross sectional pilot study on clinical review generation using large language models

> **저자**: Zining Luo, Yang Qiao, Xinyu Xu, Xiangyu Li, Mengyan Xiao, Aijia Kang, Dunrui Wang, Yueshan Pang, Xing Xie, Sijun Xie, Dachen Luo, Xuefeng Ding, Zhenglong Liu, Ying Liu, Aimin Hu, Yixing Ren, Jiebin Xie | **날짜**: 2025-03-19 | **DOI**: [10.1038/s41746-025-01535-z](https://doi.org/10.1038/s41746-025-01535-z)

---

## Essence

대규모 언어모델(LLM)이 생성한 임상 리뷰와 인간 저자의 리뷰를 체계적으로 비교한 결과, LLM이 빠르게 리뷰를 생성할 수 있지만 참고문헌 수가 적고, 논리적 일관성이 낮으며, 인용 정확도와 신뢰성이 부족함을 발견했다.

## Motivation

- **Known**: 의료 문헌의 폭발적 증가로 인한 임상 리뷰 자동화 필요성이 증가하고 있으며, LLM은 자연어 이해와 생성에서 뛰어난 성능을 보임
- **Gap**: LLM 기반 리뷰 생성 플랫폼들이 개발되고 있지만, 실제 생성된 임상 리뷰의 질과 신뢰성을 직접 평가한 연구가 부재함. 또한 AI 생성 콘텐츠 탐지 시스템의 효과성에 대한 검증도 미흡함
- **Why**: 거짓 인용(false citations)과 할루시네이션(hallucination) 문제가 보도되었고, AI 기반 논문 생성의 악용 가능성이 제기되었으므로, 임상 연구에 LLM을 책임감 있게 통합하기 위해 질적 격차를 파악하고 탐지 시스템의 효과성을 검증할 필요가 있음
- **Approach**: 2,169개의 AI 생성 임상 리뷰와 인간 저자 리뷰를 기본 질, 참고문헌 분포, 인용 특성, 학술 출판 위험 등 다양한 지표로 체계적으로 비교하고, 표절 검사 및 8개의 AI 생성 콘텐츠(AIGC) 탐지 플랫폼의 성능을 평가함

## Achievement

1. **기본 질적 차이**: AI 리뷰는 인간 리뷰 대비 단락 수(중앙값 13 vs 36), 참고문헌 수(20 vs 87)가 현저히 적으며, 참고문헌의 종합성(0.367% vs 2.113%), 신뢰성, 정확도가 모두 유의하게 낮음. 주관적 평가에서도 언어 품질, 참고문헌 깊이 분석, 논리성, 혁신성, 전체 품질이 모두 부족함

2. **참고문헌 편향성**: AI 리뷰는 최근 5년 내 논문의 비율이 높으나(46.7% vs 36.9%), JCR Q1 저널의 비율은 낮고(34.3% vs 60.4%), 영향력지수 ≥10인 고품질 논문의 비율도 현저히 낮음(12.3% vs 30.2%). 이는 AI가 품질 낮은 저널의 논문을 우선적으로 참조함을 시사함

3. **탐지 시스템의 비효율성**: AI 리뷰의 표절 탐지율은 매우 낮고(28%), AIGC 탐지 플랫폼의 성능은 극도로 불균형적(8-100%)이어서 현재의 AI 생성 콘텐츠 탐지 시스템이 신뢰성 있는 스크리닝 도구로 기능하지 못함을 드러냄

4. **세부 분석**: 생성 방법(outline 방법 > objective 방법), 임상 영역(소화기계 vs 신경계), LLM vs 제너레이티브 플랫폼 간에 성능 차이를 보임. The Lancet 기반 제어 논문이 더 높은 품질을 생성함

## How

- **연구 설계**: 2,439개의 AI 생성 임상 리뷰에서 부실한 사례(단락 수 또는 문자 수 큰 차이, 참고문헌 0)를 제외한 2,169개 분석. 9개 임상 영역(순환계, 소화계, 내분비계, 면역계, 신경계, 생식계, 호흡계, 비뇨계, 기타 종합)에 걸쳐 진행
  
- **평가 지표**: 
  - 기본 질: 단락/문자/참고문헌 수, 종합성, 신뢰성, 정확성
  - 주관적 평가: 언어 품질, 참고문헌 깊이, 논리성, 혁신성(ICC = 0.858-0.932)
  - 참고문헌 분포: 출판 연도, JCR 분류(Q1-Q4), 영향력지수, CiteScore
  - 인용 품질: 누적/평균 인용 수
  - 출판 위험: 표절 탐지율, AIGC 탐지율(8개 플랫폼)

- **통계 분석**: 중앙값과 사분위수 범위(IQR) 제시, p < 0.001 기준 유의성 판정, 급내 상관계수(ICC) 또는 단일 측정값(Single Measures)으로 평가자 간 일치도 평가

- **세부 분석**: 제어 논문 출처 저널(The Lancet, NEJM, BMJ), 임상 영역, 생성 방법(objective vs outline), AI 플랫폼/모델별 성능 비교

## Originality

- 실제 LLM 기반 임상 리뷰 생성 플랫폼의 출력물에 대한 최초의 포괄적 질적 평가 연구로, 이전 연구들이 검색 구성이나 정보 추출 등 부분적 요소만 평가한 것과 달리 완성된 리뷰 전체를 다각적으로 비교 분석함

- 표절 검사 및 AIGC 탐지의 비효율성을 경험적 데이터로 입증한 첫 연구로, 현재 학술 출판 감시 시스템의 근본적 한계를 드러냄

- 9개 임상 영역 × 3개 생성 방법 × 다양한 LLM 플랫폼에 걸친 체계적 서브그룹 분석으로 AI 성능의 일관된 편향성(저품질 논문 편향, 최근 출판물 편향)을 규명함

- 학술 윤리 및 투명성 관점에서 LLM의 책임감 있는 임상 연구 통합을 위한 정책 근거를 제공하는 실용적 중요성을 갖춤

## Limitation & Further Study

- **표본 한계**: AI 생성 임상 리뷰의 크기가 제한적이고, 특정 LLM 플랫폼 또는 프롬프트 방식에 따른 편향이 존재할 수 있으며, 인간 저자 논문의 선택 기준(The Lancet, NEJM, BMJ 등 고품질 저널 우선)이 AI의 절대적 성능을 과소평가할 가능성

- **평가 방법론**: 주관적 지표(언어 품질, 논리성, 혁신성)의 점수화가 평가자의 편견에 영향받을 수 있으며, 단일 평가자 또는 제한된 평가자 수의 경우 ICC 신뢰도가 낮을 수 있음

- **기술 진화**: 연구 수행 시점(2025년 3월)과 LLM의 빠른 발전으로 인해 최신 모델(GPT-4, Claude 등)의 성능 변화가 반영되지 않았을 가능성

- **후속 연구 방향**:
  - 더 정교한 AI 생성 콘텐츠 탐지 알고리즘 개발 및 검증
  - LLM의 인용 정확도 개선 메커니즘(고품질 저널 기반 학습, 사실 검증 모듈 강화) 연구
  - 임상 영역별, 리뷰 유형별(narrative vs systematic vs meta-analysis) 맞춤형 성능 평가
  - AI 생성 리뷰의 임상 실용성과 의료 결과에 미치는 실제 영향 평가
  - 학술 출판 윤리 가이드라인 및 AI 사용 투명성 표시 제도 개발

## Evaluation

- **Novelty**: 4/5 — LLM 기반 임상 리뷰 생성의 질적 평가를 처음 수행했으나, 기존 AI 성능 한계(할루시네이션, 거짓 인용)를 확인하는 수준의 예상된 결과

- **Technical Soundness**: 3.5/5 — 체계적이고 다각적인 평가 지표를 사용했으나, 주관적 지표의 점수화 기준이 명확하지 않으며, 통계 분석이 기술적으로 단순함. 인간 저자 논문의 선택 편향이 존재

- **Significance**: 4/5 — 학술 윤리, 출판 정책, LLM 임상 통합 가이드라인 수립에 직접적 근거를 제공하며, AIGC 탐지 시스템의 비효율성 적시 고발은 높은 정책적 가치를 가짐

- **Clarity**: 4/5 — 논문 구성이 명확하고 결과 제시가 체계적이나, 생성 방법과 프롬프트 상세 내용이 부분적으로 제시되어 재현성 제한

- **Overall**: 3.5/5

**총평**: 본 논문은 LLM 기반 임상 리뷰 생성의 현실적 한계를 최초로 체계적으로 규명한 귀중한 실증 연구로, 학술 출판 투명성과 윤리 강화의 시급함을 강조한다. 다만 예상된 결과의 확인 수준이며, 기술적 개선 방향보다는 문제 지적에 더 초점을 두어 실질적 해결책 제시는 부족하다.

## Related Papers

- 🏛 기반 연구: [[papers/126_Automated_review_generation_method_based_on_large_language_m/review]] — 대규모 언어 모델 기반 자동 리뷰 생성 방법이 임상 리뷰 생성의 기초 방법론을 제공한다.
- 🔄 다른 접근: [[papers/225_Clinicalgpt-r1_Pushing_reasoning_capability_of_generalist_di/review]] — 임상 분야 특화 GPT 모델이 일반 LLM과 다른 임상 리뷰 생성 접근법을 보여준다.
- 🔗 후속 연구: [[papers/529_MedAgents_Large_Language_Models_as_Collaborators_for_Zero-sh/review]] — 제로샷 협업을 위한 의료 에이전트들이 임상 리뷰 생성을 다중 에이전트 협업으로 확장한다.
- 🧪 응용 사례: [[papers/055_Advancing_multimodal_medical_capabilities_of_gemini/review]] — Gemini의 다중모달 의료 능력 향상이 임상 리뷰 생성에 적용될 수 있다.
- 🧪 응용 사례: [[papers/159_Bio-sieve_exploring_instruction_tuning_large_language_models/review]] — 임상 리뷰 생성을 위한 파일럿 연구에서 의료 문헌고찰 자동화로의 적용
