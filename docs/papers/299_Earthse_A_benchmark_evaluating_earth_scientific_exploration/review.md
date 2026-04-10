---
title: "299_Earthse_A_benchmark_evaluating_earth_scientific_exploration"
authors:
  - "Wanghan Xu"
  - "Xiangyu Zhao"
  - "Yuhao Zhou"
  - "Xiaoyu Yue"
  - "Ben Fei"
date: "2025"
doi: "arXiv:2505.17139v3"
arxiv: ""
score: 4.0
essence: "본 논문은 **지구과학 분야에 특화된 최초의 포괄적 벤치마크 EarthSE를 제시**하며, 10만 건의 학술논문 코퍼스를 기반으로 기초 지식부터 고급 과학탐사 능력까지 평가할 수 있는 다층 평가 프레임워크를 구축했다. 특히 개방형 다중 턴 대화를 통해 LLM의 과학탐사 능력(방법론 귀납, 한계 분석, 개념 제안)을 평가하는 새로운 평가 메트릭을 도입했다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/AI_Research_Ideation"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Chen and Mingins_2025_Earthse A benchmark evaluating earth scientific exploration capability for large language models.pdf"
---

# EarthSE: A benchmark evaluating earth scientific exploration capability for large language models

> **저자**: Wanghan Xu, Xiangyu Zhao, Yuhao Zhou, Xiaoyu Yue, Ben Fei, Fenghua Ling, Wenlong Zhang, Lei Bai | **날짜**: 2025 | **DOI**: [arXiv:2505.17139v3](https://arxiv.org/abs/2505.17139)

---

## Essence

![Figure 1](figures/fig1.webp)
*Figure 1: 주류 LLM들의 EarthSE에서의 교차 도메인 평가. (a) EarthSE는 지구의 5개 권역에서 다양한 LLM의 능력을 평가 (b) 다중 과제 평가는 계산 및 용어 설명 등에서 뚜렷한 한계 노출*

본 논문은 **지구과학 분야에 특화된 최초의 포괄적 벤치마크 EarthSE를 제시**하며, 10만 건의 학술논문 코퍼스를 기반으로 기초 지식부터 고급 과학탐사 능력까지 평가할 수 있는 다층 평가 프레임워크를 구축했다. 특히 개방형 다중 턴 대화를 통해 LLM의 과학탐사 능력(방법론 귀납, 한계 분석, 개념 제안)을 평가하는 새로운 평가 메트릭을 도입했다.

## Motivation

- **Known**: 최근 LLM의 과학 응용 연구가 활발하며, 다양한 과학 벤치마크(ScienceQA, SciBench, MMLU-Pro 등)가 개발되었음
  
- **Gap**: (1) 기존 벤치마크는 지구과학의 특수성을 반영하지 못한 일반 과학 중심 또는 기후학(ClimaQA), 해양학(OceanBench) 등 특정 소영역만 다룸 (2) 대부분 사실 회상과 추론 중심의 QA 형식만 평가하며, **개방형 과학탐사 능력(방법론 개선, 한계 분석, 가설 생성)을 평가하지 않음**

- **Why**: 지구과학은 5개 권역(대기권, 수권, 암석권, 생물권, 우주권)을 포함하는 광범위한 학제간 분야로서, 기초 지식부터 고급 과학적 사고까지 다층적 평가가 필요함

- **Approach**: 10만 건의 지구과학 논문을 자료로 하여 (1) 광범위한 기초 평가용 QA 데이터셋 Earth-Iron (2) 고난도 전문 지식 평가용 Earth-Silver (3) 개방형 과학탐사 능력 평가를 위한 다중 턴 대화 데이터셋 Earth-Gold 구성

## Achievement

![Figure 2](figures/fig2.webp)
*Figure 2: EarthSE가 포괄하는 지구과학 114개 학문 분야*

![Figure 3](figures/fig3.webp)
*Figure 3: EarthSE 구성 프로세스. 10만 건의 논문으로부터 3단계 벤치마크(Earth-Iron, Earth-Silver, Earth-Gold)의 자동화된 구성을 통해 지식 커버리지, 전문 숙련도, 과학탐사 능력의 포괄적 평가 가능*

1. **포괄적 다층 벤치마크 구축**: 
   - Earth-Iron: 114개 하위 학문, 11개 과제 카테고리에 걸친 4,133개 질문
   - Earth-Silver: 고영향 저널의 고난도 질문
   - Earth-Gold: 개방형 다중 턴 대화 기반 과학탐사 능력 평가

2. **새로운 평가 메트릭 도입**: 
   - SES(Scientific Exploration Score) 메트릭으로 방법론 귀납(M_{i+1}), 한계 분석(L_{i+1})을 반복적 자기부정 프로세스 (M_{i+1}, L_{i+1}) = LLM(M_i, L_i)로 평가

3. **주류 11개 LLM의 한계 노출**: 복잡한 지구과학 추론과 개방형 과학탐사에서 현저한 부족함을 실증적으로 규명

## How

![Figure 4](figures/fig4.webp)
*Figure 4: Phc(고인용도 코어 데이터셋)의 논문 인용도 분포*

- **자료 수집 및 분류**:
  - 10만 건의 지구과학 학술논문을 PDF에서 구조화된 JSON으로 변환(MinerU 활용)
  - 초록의 의미 유사도 분석과 지구 권역 키워드를 통해 5개 권역으로 분류
  - 계층적 선별: P_{base}(10만 건) → P_{hj}(고영향 저널 1만 건) → P_{hc}(고인용도 상위 10% 1천 건)

- **기초 과제 정의**: 11개 기초 과제 (1) 이해 영역: 용어 설명, 지식 QA, 사실 검증 (2) 추론 영역: 분석, 관계 추출, 계산 (3) 연구 영역: 도구 활용, 문헌 인용, 데이터셋 추천, 모델 적용, 방법론 개선

- **과학탐사 과제 정의**: 
  - "기존 작업의 한계 분석 → 새로운 방법 제안" 패턴 추출
  - 반복적 자기부정 프로세스: (M_{i+1}, L_{i+1}) = LLM(M_i, L_i)
  - 다중 턴 대화를 통해 자기비판과 자기개선 능력 평가

- **자동화 및 품질 관리**:
  - 사전 정의된 과제 공식을 활용한 고품질 QA 쌍의 자동 생성
  - 과학적 탐사 워크플로우를 추출하여 다중 턴 대화 구조화
  - 자동화된 정제와 인간 검증을 통한 품질 보증

## Originality

- **지구과학 특화**: 114개 세부 학문과 5개 권역을 포괄하는 최초의 통합 지구과학 벤치마크

- **개방형 과학탐사 평가**: 기존의 사실 회상/추론 중심 평가를 넘어 **방법론 귀납, 한계 분석, 개념 제안 등 고차 인지 능력을 평가하는 새로운 패러다임 제시**

- **신규 평가 메트릭 SES**: 반복적 자기부정 프로세스로 과학적 사고의 진정성을 정량화

- **다층 데이터셋 구조**: 동일 자료원으로부터 기초→중급→고급 수준의 평가를 위한 3단계 데이터셋 일관성 있게 구성

## Limitation & Further Study

- **자동화 파이프라인의 한계**: 자동화된 QA 쌍 생성 및 대화 구조화가 완벽하지 않을 수 있으며, 인간 검증의 규모와 기준이 명확하지 않음

- **평가 메트릭의 객관성**: SES 메트릭이 개방형 과학탐사를 정량화하는 방식의 신뢰성과 재현성에 대한 심층 분석 부족

- **모델 성능 해석의 깊이**: 11개 LLM의 한계를 노출하지만, **각 한계의 근본 원인(훈련 데이터 부족, 아키텍처 제약, 추론 능력 부족 등)에 대한 구체적 진단 부재**

- **후속 연구 방향**:
  - 멀티모달 지구 데이터(위성 영상, 지진파 등)를 포함한 확장
  - 다국어 지구과학 벤치마크 개발
  - 과학탐사 능력 향상을 위한 LLM 미세조정 방법론 연구
  - 실제 지구과학 연구 프로세스와의 정합성 검증

## Evaluation

- **Novelty**: 4.5/5
  - 지구과학 특화, 개방형 과학탐사 평가, 신규 메트릭 도입 등 다각도의 혁신성 있음
  - 다만 벤치마크 자체의 구조적 혁신성보다는 기존 접근의 확장으로 볼 여지 있음

- **Technical Soundness**: 4/5
  - 자료 수집, 분류, 계층적 선별 프로세스가 체계적임
  - 자동화 파이프라인과 인간 검증 프로세스 기술이 명확하지 않은 부분 있음
  - 11개 과제 카테고리와 SES 메트릭의 수학적 엄밀성 확인 필요

- **Significance**: 4.5/5
  - 지구과학 분야에 최초의 포괄적 벤치마크 제공으로 실무 가치 높음
  - 개방형 과학탐사 평가는 향후 LLM 과학 응용 평가의 표준 확립에 기여 가능
  - AI 과학 발견 지원의 현실성 평가에 중요한 토대 제공

- **Clarity**: 3.5/5
  - 전반적 구성과 3개 데이터셋의 목적이 명확함
  - 자동화 파이프라인의 세부 절차, 인간 검증 기준, SES 메트릭의 계산 방식이 논문에서 충분히 기술되지 않음
  - 실제 대화 사례와 메트릭 계산 예시 제시 필요

- **Overall**: 4/5

**총평**: EarthSE는 지구과학 분야에서 **기초 지식부터 개방형 과학탐사 능력까지 다층적으로 평가하는 최초의 포괄적 벤치마크**로서 상당한 학술적·실무적 가치를 제공한다. 특히 SES 메트릭을 통한 과학적 사고의 정량화는 향후 LLM 과학 응용 평가의 새로운 방향을 제시할 수 있다. 다만 자동화 파이프라인의 기술적 세부사항, 평가 메트릭의 객관성 검증, 모델 성능 저조의 근본 원인 분석 등이 보강되면 더욱 강력한 벤치마크가 될 수 있을 것으로 예상된다.

## Related Papers

- 🔗 후속 연구: [[papers/831_Towards_llm_agents_for_earth_observation/review]] — 지구 관측용 LLM 에이전트에서 지구과학 탐사 능력 벤치마크로의 확장
- 🧪 응용 사례: [[papers/298_Earth-Agent_Unlocking_the_Full_Landscape_of_Earth_Observatio/review]] — 지구 관측 전체 환경 탐색을 지구과학 탐사 벤치마크에 적용
- 🏛 기반 연구: [[papers/706_SciBench_Evaluating_College-Level_Scientific_Problem-Solving/review]] — 대학 수준 과학 문제 해결 평가가 지구과학 벤치마크의 기반 제공
- 🔄 다른 접근: [[papers/342_Foundation_Models_for_Environmental_Science_A_Survey_of_Emer/review]] — 환경과학 파운데이션 모델과 지구과학 탐사 벤치마크의 다른 접근법
