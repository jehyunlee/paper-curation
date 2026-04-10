---
title: "029_A_Survey_of_Scientific_Large_Language_Models_From_Data_Found"
authors:
  - "Ming Hu"
  - "Chenglong Ma"
  - "Wei Li"
  - "Wanghan Xu"
  - "Jiamin Wu"
date: "2025.08"
doi: ""
arxiv: ""
score: 4.0
essence: "본 논문은 과학 분야 대규모 언어 모델(Scientific Large Language Models, Sci-LLMs)의 발전을 데이터 중심으로 종합 분석하는 설문연구로, 270개 이상의 사전/후학습 데이터셋과 190개 이상의 벤치마크를 검토하여 과학 AI의 로드맵을 제시한다."
tags:
  - "cat/AI-Powered_Scientific_Research_Frameworks"
  - "sub/Biological_Foundation_Models"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Hu et al._2025_A Survey of Scientific Large Language Models From Data Foundations to Agent Frontiers.pdf"
---

# A Survey of Scientific Large Language Models: From Data Foundations to Agent Frontiers

> **저자**: Ming Hu, Chenglong Ma, Wei Li, Wanghan Xu, Jiamin Wu, Jucheng Hu, Tianbin Li, Guohang Zhuang, Jiaqi Liu, Yingzhou Lu, Ying Chen, Chaoyang Zhang, Cheng Tan, Jie Ying, Guocheng Wu, Shujian Gao, Pengcheng Chen, Jiashi Lin, Haitao Wu, Lulu Chen | **날짜**: 2025-08-28 | **URL**: [https://arxiv.org/abs/2508.21148](https://arxiv.org/abs/2508.21148)

---

## Essence

![Figure 1](figures/fig1.webp)

*Fig. 1: The song of humanity is a song of courage. The diagram depicts the continuum of scientific inquiry spanning from*

본 논문은 과학 분야 대규모 언어 모델(Scientific Large Language Models, Sci-LLMs)의 발전을 데이터 중심으로 종합 분석하는 설문연구로, 270개 이상의 사전/후학습 데이터셋과 190개 이상의 벤치마크를 검토하여 과학 AI의 로드맵을 제시한다.

## Motivation

- **Known**: 일반 NLP 분야의 대규모 언어 모델은 널리 발전했으나, 과학 분야 특화 모델의 발전은 과학 데이터의 복잡성(다중모달, 교차 스케일, 도메인 특화)으로 인해 제한되어 있다. 기존 연구들은 개별 도메인 또는 단편적 관점에서만 Sci-LLMs을 다루었다.
- **Gap**: 과학 데이터의 특성(이질적, 다중 스케일, 불확실성 포함)에 대한 체계적 분류체계와 Sci-LLMs 개발의 데이터-모델 공진화 관계에 대한 통합적 분석이 부재하다. 또한 정적 평가에서 발견 지향적 평가로의 패러다임 전환에 대한 체계적 논의가 필요하다.
- **Why**: Sci-LLMs은 과학 지식의 표현, 통합, 적용 방식을 근본적으로 변화시키고 있으며, 데이터 기반의 이해는 신뢰할 수 있는 과학 발견 자동화 시스템 개발에 필수적이다. 이는 인류의 과학 발견 가속화에 직결되는 중요한 문제이다.
- **Approach**: 본 논문은 과학 데이터의 통일된 분류체계와 과학 지식의 계층 모델을 수립하고, 270개 이상의 데이터셋과 190개 이상의 벤치마크를 체계적으로 검토하여 Sci-LLMs의 발전을 추적한다. 또한 자율 에이전트 기반 폐쇄 루프 시스템으로의 패러다임 전환을 제안한다.

## Achievement

![Figure 2](figures/fig2.webp)

*Fig. 2: Cumulative trend of publications on major preprint platforms whose titles or abstracts mention the keyword “lang*

1. **과학 데이터의 통합 분류체계**: 텍스트, 시각, 기호, 구조화, 시계열, 멀티오믹스 등 6가지 주요 데이터 형식과 사실, 이론, 방법론, 모델링, 통찰의 5단계 지식 계층을 정의
2. **대규모 데이터 분석**: 270개+ 사전/후학습 데이터셋과 190개+ 벤치마크를 체계적으로 분석하여 과학 AI의 데이터 수요 특성 규명
3. **Sci-LLMs 진화 추적**: 2018-2025년의 4단계 패러다임 전환(일반 LLM → 과학 특화 → 도메인 특화 → 자율 에이전트)을 파악
4. **평가 패러다임 전환**: 정적 시험에서 발견 지향적 평가로의 변화와 고급 평가 프로토콜 제시
5. **자동화 파이프라인 제안**: 준자동화 주석 및 전문가 검증 기반 데이터 개선 방안 제시

## How


- 6개 주요 과학 도메인(물리, 화학, 재료과학, 생명과학, 천문학, 지구과학)별 데이터셋 및 모델 분류
- 정량적 분석을 통한 데이터 트렌드 추적(누적 발행물 수, 데이터셋 규모, 도메인 분포)
- 데이터-모델 공진화 관계의 시계열 분석
- 정확성, 완정성, 적시성, 추적성 등 과학 데이터 품질 기준 정의
- 다중 차원 평가 프레임워크 구축(전문 지식, 추론, 다중모달)
- 준자동화 주석 파이프라인과 전문가 검증 메커니즘 분석

## Originality

- **데이터 중심 관점**: 기존의 모델 중심 관점에서 벗어나 데이터-모델 공진화를 강조하는 혁신적 프레임워크
- **통합 분류체계**: 다양한 과학 도메인의 데이터와 지식을 아우르는 최초의 통일된 분류 체계 제시
- **광범위한 실증 분석**: 270개+ 데이터셋과 190개+ 벤치마크를 단일 논문에서 종합 분석
- **자율 에이전트 패러다임**: 폐쇄 루프 시스템으로의 미래 방향 제시로 현재의 한계를 넘는 구상 제공
- **다중 스케일 통합**: 아원자에서 우주론적 현상까지 아우르는 계층적 지식 모델의 시각화

## Limitation & Further Study

- 매우 광범위한 주제로 인해 각 도메인에 대한 심화 분석이 제한적일 수 있음
- 2025년 10월 논문이므로 이후 급속 발전하는 분야의 변화를 반영하지 못할 가능성
- 반자동화 주석 파이프라인과 전문가 검증의 실제 구현 방안에 대한 상세 기술 부족
- 도메인 특정 불확실성 정량화 방법론에 대한 구체적 제시 미흡
- 폐쇄 루프 에이전트 시스템의 현실적 구현 로드맵이 개념적 수준에 머물러 있음
- 후속 연구: (1) 각 과학 도메인별 심화된 데이터 기준 개발, (2) 실제 반자동화 주석 파이프라인 구현 사례 축적, (3) 도메인 불변성 유지 방법론 실증, (4) 자율 에이전트의 검증 및 신뢰성 평가 프레임워크 개발

## Evaluation

- Novelty: 5/5
- Technical Soundness: 4/5
- Significance: 5/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 설문연구는 과학 AI의 발전을 데이터 중심으로 종합적으로 분석하는 최초의 시도로, 혁신적인 분류체계와 광범위한 실증 분석을 통해 Sci-LLMs의 현황을 명확히 하고 자율 에이전트 기반 폐쇄 루프 시스템이라는 미래 방향을 제시한다. 과학 분야 AI의 로드맵으로서 높은 학술적 가치와 실용적 중요성을 가지고 있으나, 실제 구현 방안에 대한 상세한 기술과 각 도메인별 심화 분석은 후속 연구로 남겨져 있다.

## Related Papers

- 🔄 다른 접근: [[papers/720_Scientific_Large_Language_Models_A_Survey_on_Biological__Che/review]] — 생물학과 화학 분야 과학 LLM에 대한 다른 관점의 종합 조사를 제시한다.
- 🔗 후속 연구: [[papers/840_Transforming_Science_with_Large_Language_Models_A_Survey_on/review]] — 대규모 언어모델이 과학을 변화시키는 방법에 대한 서베이로 확장한다.
