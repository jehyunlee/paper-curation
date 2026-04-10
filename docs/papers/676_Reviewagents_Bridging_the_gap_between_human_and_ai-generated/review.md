---
title: "676_Reviewagents_Bridging_the_gap_between_human_and_ai-generated"
authors:
  - "Xiaojin Gao"
  - "Jiacheng Ruan"
  - "Zongyun Zhang"
  - "Jingsheng Gao"
  - "Ting Liu"
date: "2025"
doi: ""
arxiv: ""
score: 4.0
essence: "대규모 언어모델(LLM)을 활용하여 학술 논문 심사를 자동화하되, 인간 심사자의 다단계 추론 과정을 모방한 다중 에이전트 프레임워크를 제안한다. 구조화된 사고(Chain-of-Thought) 방식과 관련 논문 인식(relevant-paper-aware) 학습을 통해 AI 생성 심사의 품질을 인간 심사에 가깝게 향상시킨다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/LLM_Review_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Gao et al._2025_Reviewagents Bridging the gap between human and ai-generated paper reviews.pdf"
---

# ReviewAgents: Bridging the Gap Between Human and AI-Generated Paper Reviews

> **저자**: Xiaojin Gao, Jiacheng Ruan, Zongyun Zhang, Jingsheng Gao, Ting Liu, Yuzhuo Fu | **날짜**: 2025 | **기관**: Shanghai Jiao Tong University

---

## Essence

대규모 언어모델(LLM)을 활용하여 학술 논문 심사를 자동화하되, 인간 심사자의 다단계 추론 과정을 모방한 다중 에이전트 프레임워크를 제안한다. 구조화된 사고(Chain-of-Thought) 방식과 관련 논문 인식(relevant-paper-aware) 학습을 통해 AI 생성 심사의 품질을 인간 심사에 가깝게 향상시킨다.

## Motivation

- **Known**: LLM이 복잡한 텍스트 이해 및 추론 능력을 보유하고 있으며, 학술 심사 자동화에 잠재력이 있다는 점이 알려져 있음

- **Gap**: 기존 LLM 기반 접근법은 심사 의견을 직접 생성하는 단순화된 방식으로, 인간 심사자의 실제 인지 과정(논문 요약 → 강점/약점 분석 → 결론 도출 → 메타리뷰)을 반영하지 못함. 따라서 생성된 의견이 인간 심사자의 판단과 큰 괴리가 발생

- **Why**: 실제 심사 과정은 (1) 다단계 추론, (2) 다중 역할 참여(심사자, 영역 의장), (3) 최신 관련 문헌 참고를 포함하므로, 이를 모방해야 더 일관되고 신뢰할 수 있는 자동화 심사가 가능

- **Approach**: (1) 142k개 심사 의견을 구조화된 형식으로 변환한 Review-CoT 데이터셋 구축, (2) 관련 논문 인식 학습법 적용, (3) 다중 에이전트 심사 프레임워크(ReviewAgents) 개발, (4) 자동 생성 심사의 품질 평가를 위한 ReviewBench 벤치마크 제안

## Achievement

1. **Review-CoT 데이터셋**: ICLR(2017-2024), NeurIPS(2016-2024)의 37,403개 논문과 142,324개 심사 의견을 구조화된 형식으로 정제. 제출 시점까지의 최신 관련 논문 정보를 포함한 최초의 대규모 구조화 심사 데이터셋

2. **ReviewAgents 프레임워크**: 세 단계 구조화 추론(요약→분석→결론)을 거쳐 인간 심사자의 인지 과정을 모방하는 다중 역할, 다중 에이전트 심사 시스템. 기존 LLM 기반 접근법 대비 인간 심사와의 정렬도(alignment) 향상

3. **ReviewBench 벤치마크**: LLM 생성 심사 의견의 품질을 4개 차원에서 정량적으로 평가하는 전문 벤치마크. 최신 심사 데이터로 구성하여 기존 LLM 사전학습 데이터 오염 문제 회피

## How

![Figure 1](figures/fig1.webp)
*Figure 1: 사전 정의된 구조화 사고 과정에 따른 심사 의견 변환 프로세스 (요약→분석→결론)*

### 데이터셋 구축

- **메타데이터 수집**: OpenReview, NeurIPS Proceedings에서 논문 전문, 심사 의견, 메타리뷰, 채택 여부 등 원본 정보 수집
  
- **구조화 변환(Transcription)**: 고급 LLM을 이용해 기존 심사 의견을 세 단계로 재구성
  - `<SUMMARY>`: 논문의 주요 기여도 및 방법론 요약
  - `<STRENGTHS_AND_WEAKNESSES>`: 강점 및 약점 분석
  - `<CONCLUSION>`: 최종 평가 및 결론
  - 원본 의미 보존하면서 명시적 구조 부가

- **관련 논문 검색**: Semantic Scholar API를 통해 제출 시점까지의 관련 논문 검색, 유사도 기반으로 상위 2개 논문 추출. 인간 심사자의 신규성(novelty) 평가 과정 모방

### ReviewAgents 프레임워크

- **심사자 에이전트(Reviewer Agent)**: 구조화된 3단계 추론을 수행하여 개별 심사 의견 생성
- **영역 의장 에이전트(Area Chair Agent)**: 다수 심사자의 의견을 종합하여 메타리뷰 작성
- **다중 심사자 통합**: 여러 심사자 에이전트의 독립적 평가 후 영역 의장이 종합, 개별 심사자 편향(bias) 완화

### 학습 및 평가 방법

- **관련-논문-인식 학습(Relevant-Paper-Aware Training)**: 논문 본문 + 관련 논문 정보를 입력으로 하여 모델 학습. 시간 변화에 따른 신규성 판단의 일관성 향상
- **ReviewBench 평가**: 자동생성 심사의 품질을 인간 심사와 비교하는 다차원 평가 체계

## Originality

- **최초의 구조화 심사 데이터셋**: 단순 심사 텍스트 수집 수준을 넘어 인간의 인지 과정(요약→분석→결론)을 명시적으로 구조화한 첫 대규모 데이터셋

- **관련 논문 인식 학습**: 심사 시점의 최신 문헌 정보를 학습 데이터에 포함하여, 시간축에서의 신규성 판단 일관성 확보 (기존 방법 미비점 보완)

- **다중 역할 에이전트 설계**: 실제 심사 제도(심사자→영역 의장)의 다단계 구조를 그대로 모방하여 개별 편향 완화 및 인간 심사 절차의 신뢰성 있는 자동화

- **전문 벤치마크 제시**: 생성 심사 평가를 위한 표준화된 다차원 평가 체계로 향후 연구의 기준점 제공

## Limitation & Further Study

- **데이터 시간성**: 데이터셋 구축 이후 급속도로 증가하는 신규 논문에 대한 적응 메커니즘 필요. 온라인 학습(online learning) 또는 점진적 업데이트 전략 검토 필요

- **언어 및 도메인 제한**: ICLR, NeurIPS 중심의 영어권 머신러닝 논문에 편중. 타 학문 분야(생물학, 화학 등) 및 다국어 확장 미흡

- **인간-AI 협업 모델 부재**: 완전 자동화 심사 대신 인간 심사자를 보조하는 상호작용 설계 미비. 심사자가 AI 생성 의견을 수정/선별하는 워크플로우 개발 필요

- **일관성 및 공정성 검증**: 다중 에이전트 시스템의 출력 일관성, 논문 특성(저자 명성, 소속 기관 등)에 대한 편향 가능성에 대한 심층 분석 부족

- **평가 기준의 주관성**: ReviewBench의 정량적 평가 지표가 심사의 주관적 판단(예: 창의성 평가)을 충분히 포착하지 못할 가능성

## Evaluation

- **Novelty(독창성)**: 4.5/5
  - 구조화 심사 데이터셋과 관련-논문-인식 학습은 신규적이나, 다중 에이전트 개념 자체는 선행 연구(AgentReview 등)에서 부분적 제시

- **Technical Soundness(기술적 건전성)**: 4/5
  - 데이터 수집, 구조화, 에이전트 설계 방법론은 타당하나, 학습 알고리즘(예: fine-tuning 상세 사항), 하이퍼파라미터, 수렴성 증명 부족

- **Significance(중요성)**: 4/5
  - 학술 심사 자동화는 연구 공동체의 실질적 문제 해결이나, 현실 도입 시 윤리적 논쟁(peer review의 품질 보증, 심사자 역할 축소 등) 미검토

- **Clarity(명확성)**: 4/5
  - 전반적 구조 명확하나, 관련 논문 검색의 수량(상위 2개 선정 이유), 에이전트 간 상호작용 상세(메타리뷰 생성 과정) 약간 모호

- **Overall(종합)**: 4/5

**총평**: 본 논문은 인간 심사자의 구조화된 사고 과정을 체계적으로 모방한 첫 대규모 데이터셋과 다중 에이전트 프레임워크로 AI 심사의 현실화 가능성을 높였다. 다만, 데이터 시간성 문제, 평가 지표의 한계, 실제 심사 제도 도입 시 윤리적·제도적 과제에 대한 보충 논의가 필요하다.

## Related Papers

- 🔄 다른 접근: [[papers/665_Remor_Automated_peer_review_generation_with_llm_reasoning_an/review]] — 다중 에이전트 프레임워크와 강화학습 기반 접근법은 모두 AI 심사평의 품질 향상을 목표로 하지만 다른 구조적 해결책을 제시한다.
- ⚖️ 반론/비판: [[papers/881_When_ai_co-scientists_fail_Spot-a_benchmark_for_automated_ve/review]] — AI 생성 심사평의 품질 향상 연구와 과학 논문 오류 검증의 한계 연구를 대비하여 AI 심사 시스템의 현실적 적용 가능성을 평가할 수 있다.
- 🏛 기반 연구: [[papers/519_MARG_Multi-Agent_Review_Generation_for_Scientific_Papers/review]] — 다중 에이전트 리뷰 생성의 기본 프레임워크가 인간-AI 격차 해소를 위한 구조화된 추론 과정 설계에 핵심적인 기반을 제공한다.
- 🏛 기반 연구: [[papers/679_Revieweval_An_evaluation_framework_for_ai-generated_reviews/review]] — 인간과 AI 생성 리뷰 간 격차를 분석한 연구로 ReviewEval 평가 프레임워크 설계의 기준점을 제공한다.
- 🔄 다른 접근: [[papers/665_Remor_Automated_peer_review_generation_with_llm_reasoning_an/review]] — 다목적 강화학습과 다중 에이전트 접근법은 모두 심사평 품질 향상을 목표로 하지만 서로 다른 최적화 전략을 사용한다.
