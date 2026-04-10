---
title: "398_Harnessing_large_language_models_for_scientific_novelty_dete"
authors:
  - "Yeonghun Kang"
  - "Wonseok Lee"
  - "Taeun Bae"
  - "Seunghee Han"
  - "Huiwon Jang"
date: "2025.02"
doi: "10.1021/jacs.4c11085"
arxiv: ""
score: 4.5
essence: "대규모 언어모델(LLM)을 활용하여 과학 문헌에서 40,000개 이상의 금속-유기 골격(MOF) 관련 논문을 분석하고, 32개의 핵심 특성과 21개 합성 조건 카테고리를 자동으로 추출한 포괄적인 데이터셋을 구축했다. 이 데이터셋을 통해 합성 조건과 실험 데이터 간의 차이를 규명하고 합성 조건 추천 시스템을 개발했다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/Multi-Agent_Scientific_Frameworks"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Kang et al._2025_Harnessing Large Language Models to Collect and Analyze Metal–Organic Framework Property Data Set.pdf"
---

# Harnessing Large Language Models to Collect and Analyze Metal–Organic Framework Property Data Set

> **저자**: Yeonghun Kang, Wonseok Lee, Taeun Bae, Seunghee Han, Huiwon Jang, Jihan Kim | **날짜**: 2025-02-05 | **DOI**: [10.1021/jacs.4c11085](https://doi.org/10.1021/jacs.4c11085)

---

## Essence

![Figure 1](figures/fig1.webp) *L2M3 모델의 전체 구조: (a) 테이블과 텍스트에서 정보를 추출하는 통합 프레임워크, (b) 테이블 마이닝 프로세스, (c) 텍스트 마이닝 프로세스*

대규모 언어모델(LLM)을 활용하여 과학 문헌에서 40,000개 이상의 금속-유기 골격(MOF) 관련 논문을 분석하고, 32개의 핵심 특성과 21개 합성 조건 카테고리를 자동으로 추출한 포괄적인 데이터셋을 구축했다. 이 데이터셋을 통해 합성 조건과 실험 데이터 간의 차이를 규명하고 합성 조건 추천 시스템을 개발했다.

## Motivation

- **Known**: 지난 10년간 계산 시뮬레이션과 실험 데이터가 급증했으며, 머신러닝을 통한 물질 특성 예측이 중요해짐. 기존 연구(Park et al., Nandy et al., Manning et al.)에서 규칙 기반 기법(Rule-based NLP), PU 학습 등으로 MOF 데이터 마이닝을 수행함.

- **Gap**: 기존의 규칙 기반 또는 전통적 머신러닝 방식은 (1) 복잡한 테이블과 비정형 텍스트 추출의 낮은 정확도, (2) 한정된 규모의 데이터셋, (3) 시뮬레이션 데이터와 실험 데이터의 불일치에 대한 체계적 분석 부재.

- **Why**: MOF의 수천 가지 금속-리간드 조합으로부터 나오는 다양성과 넓은 응용 영역(기체 저장, 분리, 촉매, 약물 전달)을 고려할 때, 포괄적인 실험 데이터 수집이 이론 예측과 실제 결과 간의 간격을 줄이는 데 필수적.

- **Approach**: ChatGPT 등의 LLM의 문맥 이해 능력과 few-shot 학습 성능을 활용하여, Yaghi 그룹의 선행 연구를 확장하는 자동화된 "L2M3" (Large Language Model MOF Miner) 시스템을 개발. 테이블 추출, 합성 조건 추출, 특성 추출을 위한 세 가지 전문화된 에이전트를 구성.

## Achievement

![Figure 2](figures/fig2.webp) *데이터 추출 및 조직화 시스템: (a) 분류 및 포함 단계 결과에 따라 적응적으로 수정되는 LLM 프롬프트, (b) 메타데이터 태깅을 통한 동일 물질의 정보 통합*

1. **대규모 데이터셋 구축**: 40,000개 이상 논문에서 39,476개 유효 데이터셋 추출. 32개 정의된 특성(surface area, pore volume 등)과 일반 형식의 특성들을 추출. MOF 합성 프로세스를 21개 카테고리로 분류하여 세밀한 데이터 구조화 실현.

2. **높은 추출 정확도 달성**: 다양한 출판사로부터 150개 논문의 무작위 표본 평가에서 분류(categorization), 포함(inclusion), 추출(extraction) 작업에 대한 정확도 검증. 프롬프트 엔지니어링, 온도 제어, 할루시네이션 최소화 기법으로 신뢰성 확보.

3. **시뮬레이션-실험 데이터 간극 규명**: 머신러닝 분석을 통해 이론 예측값과 실험값 사이의 체계적 차이를 발견하고, 그 원인(합성 조건 변동성, 물질 순도, 측정 환경 등)을 분석.

4. **실용적 도구 개발**: 추출된 합성 조건 데이터로부터 합성 조건 추천 시스템 구축. 사용자가 제공한 전구체(precursor)를 기반으로 최적 합성 조건을 제시하여 합성 전략 개선에 활용 가능.

## How

![Figure 2](figures/fig2.webp) *적응형 LLM 프롬프트와 데이터 조직화 에이전트의 상세 프로세스*

- **테이블 에이전트**: 세 단계 프로세스 적용
  - *분류*: 테이블을 특성 테이블(property table), 결정 정보 테이블(crystal information table), 기타로 분류
  - *포함*: 각 테이블에 포함된 정보 범위 결정
  - *추출*: LLM 기반 신뢰성 높은 정보 추출로 규칙 기반 방식의 한계 극복

- **텍스트 에이전트** (합성 조건 에이전트 & 특성 에이전트):
  - 문단을 합성 조건, 특성, 무관 정보로 분류
  - 특정 합성 방법 또는 특성 유형에 맞추어 추출 프롬프트를 동적으로 조정 (Figure 2a)
  - JSON 형식 출력 표준화

- **적응형 프롬프트 설계**: 분류 단계 결과에 따라 시스템 프롬프트를 자동 수정하여 프롬프트 길이 증가로 인한 정확도 저하, 비용 증가 문제 해결

- **데이터 조직화 에이전트** (Figure 2b):
  - 각 데이터 포인트에 메타데이터(이름, 기호, 화학식, 동의어, refcode, 격자) 태깅
  - 동일 메타데이터를 가진 데이터 통합으로 하나의 MOF에 대한 통합 데이터셋 형성
  - CCDC (Cambridge Crystallographic Data Centre) 데이터베이스와의 구조 매칭을 통해 합성-구조-특성의 연계 확립

- **정제 단계**: MOF 필터링 에이전트로 추출 정보가 목표 물질(MOF)에만 해당하는지 검증하여 링커나 복합체 등 비대상 물질 제외

- **할루시네이션 최소화**: 프롬프트 엔지니어링, 모델 선택, 온도 제어, 검증 프로세스 적용 (Note S1 참조)

## Originality

- **LLM의 완전 자동화 활용**: Yaghi 그룹의 선행 연구를 확장하여 테이블/텍스트 추출, 데이터 조직화, 정제까지 전 과정을 LLM으로 자동화. 기존 규칙 기반 방식의 한계 극복.

- **다중 에이전트 아키텍처**: 테이블, 합성 조건, 특성 추출을 위한 세 가지 전문화된 에이전트의 계층적 구성으로, 각 정보 유형에 최적화된 추출 가능.

- **적응형 프롬프트 생성**: 분류 및 포함 단계 결과에 기반하여 추출 프롬프트를 동적으로 수정함으로써 프롬프트 길이와 정확도 간의 균형 달성. 새로운 프롬프트 최적화 패러다임 제시.

- **대규모 체계적 분석**: 40,000개 논문에서 구축한 포괄적 데이터셋을 통해 합성-구조-특성 관계를 처음으로 대규모 통계적으로 분석하고, 시뮬레이션-실험 간극의 원인 규명.

- **실용적 응용**: 추출된 데이터로부터 합성 조건 추천 시스템을 개발하여, 데이터 마이닝의 실제 연구 활용도 향상.

## Limitation & Further Study

- **할루시네이션 위험**: 아무리 체계적이더라도 LLM의 할루시네이션(거짓 정보 생성) 가능성 완전 제거 불가. 150개 표본만으로 정확도 검증한 점에서 더 광범위한 표본에 대한 검증 필요.

- **메타데이터 정합성**: CCDC 데이터베이스와의 매칭 시 이름 변이, 약자 다양성 등으로 인한 누락이나 잘못된 연계 가능성. 완벽한 구조-특성 연계의 어려움.

- **미포함 데이터**: 논문의 보조 자료(supplementary materials)나 그래프 기반 데이터는 추출 대상에서 제외되어, 실제 정보의 일부만 수집된 가능성.

- **합성 조건 추천 시스템의 신뢰도**: 데이터 불균형(특정 합성 조건이 더 많이 보고됨), 문헌 출판 편향 등의 영향으로 추천 결과의 일반화 가능성 제한.

- **후속 연구 방향**:
  - 다국어 문헌 확장으로 더 넓은 데이터 커버리지 확보
  - 보조 자료와 그래프 정보 추출 기술 개발
  - 합성 조건 추천 시스템의 임상 검증 (실제 합성 시도를 통한 검증)
  - 다른 소재군(페로브스카이트, 그래프 산화물 등)으로의 확장 가능성 검토


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4.2/5
- Significance: 4.8/5
- Clarity: 4.3/5
- Overall: 4.5/5

**총평**: 본 논문은 LLM 기반 자동화된 데이터 마이닝의 뛰어난 실례로, 40,000개 논문에서 포괄적 MOF 데이터셋을 체계적으로 구축하고 시뮬레이션-실험 간극을 규명했으며 실용적 추천 시스템을 제시함으로써 데이터 기반 물질 과학의 새로운 표준을 제시한다. 다만 LLM 고유의 할루시네이션 위험과 검증 표본의 제한으로 인해 완전한 정확성 보증에는 미치지 못한다.

## Related Papers

- 🔄 다른 접근: [[papers/208_ChatMOF_an_artificial_intelligence_system_for_predicting_and/review]] — MOF와 화학 소재라는 유사한 영역에서 LLM 기반 지식 추출과 AI 시스템 구축의 서로 다른 접근법을 비교한다.
- 🏛 기반 연구: [[papers/025_A_Survey_of_AI_for_Materials_Science_Foundation_Models_LLM_A/review]] — 재료과학에서 AI와 LLM 활용의 포괄적 조망을 제공하여 MOF 연구의 이론적 맥락을 제시한다.
- 🔗 후속 연구: [[papers/764_Sparks_Multi-Agent_Artificial_Intelligence_Model_Discovers_P/review]] — 문헌 기반 데이터 수집을 넘어 완전 자동화된 과학 발견으로 나아가는 발전 경로를 보여준다.
- 🔄 다른 접근: [[papers/208_ChatMOF_an_artificial_intelligence_system_for_predicting_and/review]] — MOF 예측과 생성에서 AI 시스템과 LLM 기반 데이터 수집이라는 서로 다른 접근법으로 화학 소재 연구를 자동화한다.
