---
title: "363_From_Reasoning_to_Learning_A_Survey_on_Hypothesis_Discovery"
authors:
  - "Kaiyu He"
  - "Zhiyu Chen"
date: "2025"
doi: "10.48550/arXiv.2505.21935"
arxiv: ""
score: 4.5
essence: "본 논문은 대규모 언어모델(LLM)이 단순한 정보 실행자에서 새로운 지식을 발견하는 혁신 엔진으로 진화할 수 있는지를 Peirce의 철학적 프레임워크(귀납법, 연역법, 귀추법)를 통해 체계적으로 분석한 종합 설문(survey)이다. LLM을 활용한 가설 발견과 규칙 학습의 전체 사이클을 이론적으로 정립하고 실증적으로 검토한 첫 시도이다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/AI_Hypothesis_Generation"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/He and Chen_2025_From Reasoning to Learning A Survey on Hypothesis Discovery and Rule Learning with Large Language M.pdf"
---

# From Reasoning to Learning: A Survey on Hypothesis Discovery and Rule Learning with Large Language Models

> **저자**: Kaiyu He, Zhiyu Chen | **날짜**: 2025 | **DOI**: [10.48550/arXiv.2505.21935](https://doi.org/10.48550/arXiv.2505.21935)

---

## Essence

![Figure 1](figures/fig1.webp) *Figure 1: LLM 기반 가설 발견의 분류 체계*

본 논문은 대규모 언어모델(LLM)이 단순한 정보 실행자에서 새로운 지식을 발견하는 혁신 엔진으로 진화할 수 있는지를 Peirce의 철학적 프레임워크(귀납법, 연역법, 귀추법)를 통해 체계적으로 분석한 종합 설문(survey)이다. LLM을 활용한 가설 발견과 규칙 학습의 전체 사이클을 이론적으로 정립하고 실증적으로 검토한 첫 시도이다.

## Motivation

- **Known**: 최근 LLM 연구는 주로 명령 따르기(instruction-following)와 연역적 추론(deductive reasoning) 능력 향상에 집중되어 있음. 기존 상징적 AI 시스템은 제한된 규칙 기반으로 인해 귀추법(abduction)과 귀납법(induction)을 통한 새로운 지식 발견에 취약함.

- **Gap**: 가설 발견의 세 가지 요소(생성, 적용, 검증)가 산발적으로 연구되고 있으나, 이들의 상호연결성과 반복적 순환 구조에 대한 통합적 분석이 부재함. 특히 LLM이 진정한 의미의 새로운 지식을 자율적으로 발견할 수 있는지에 대한 체계적 검토가 필요함.

- **Why**: 인공일반지능(AGI) 달성을 위해서는 정보 검색이나 명령 실행을 넘어 귀추, 연역, 귀납을 통해 새로운 가설과 이론을 수립하는 능력이 필수적임. 이는 과학 연구, 의료 진단, 정책 수립 등 고차원적 문제 해결에 핵심임.

- **Approach**: Peirce의 철학적 정의에 기반하여 가설 발견을 네 가지 구성 요소로 분해(①귀추법을 통한 생성 ②연역법을 통한 적용 ③귀납법을 통한 검증 ④전체 사이클의 동적 상호작용)하고, 각 단계별 방법론, 벤치마크, 평가 지표, 한계와 향후 방향을 체계적으로 정리.

## Achievement

![Figure 2](figures/fig2.webp) *Figure 2: Peirce의 가설 발견 프레임워크 및 실제 사례*

1. **체계적 분류 체계 수립**: 자연언어 가설과 형식언어(formal language) 가설, 프롬프트 기반과 RAG(Retrieval-Augmented Generation) 기반 방법으로 구분되는 포괄적 분류 제시. 총 50개 이상의 최신 연구를 Peirce의 세 가지 추론 유형에 맞게 체계화.

2. **LLM의 새로운 지식 발견 능력 검증**: LLM이 광범위한 상식과 도메인 지식을 내재화하여 많은 가설 수를 생성하고 검증하는 데 효과적임을 입증. 기존 상징 기반 AI의 "높은 비용-제한된 범위" 문제를 해결.

3. **결함 있는 추론(defeasible reasoning) 실현**: LLM이 새로운 증거에 따라 가설을 수정할 수 있는 동적 신념 업데이트 능력 보유를 확인. 이전에는 상징 AI로 구현 불가능했던 유연한 추론 모델화 가능.

4. **자동 과학 발견의 경로 제시**: 수동적 가설 발견(passive discovery), 능동적 발견(proactive discovery), 실제 환경 시뮬레이션을 통한 발견의 세 가지 발전 단계 제시.

## How

![Figure 1](figures/fig1.webp) *Figure 1: 가설 발견의 네 가지 구성 요소와 방법론*

### 가설 생성 (Abduction, §4)

- **자연언어 기반**: 프롬프트 방식(Wiegreffe et al. 2022), RAG 방식(Hu et al. 2024), 인간 지원 방식(Zhao et al. 2024)
- **형식언어 기반**: 형식적 관찰(formal observation) 활용(Young et al. 2022) vs. 자연언어 관찰 활용(Cheng et al. 2024)
- **평가**: 예측 기반, 실제값 기반, 인간 평가

### 가설 적용 (Deduction, §5)

- **LLM을 형식언어 파서로 활용**: 자연언어 가설을 형식 논리로 변환하여 추론 수행
- **미세 조정(fine-tuning) vs. 프롬프트 기반**: 파라미터 효율성과 정확성의 트레이드오프 존재
- **평가**: 주로 예측 정확도 기반

### 가설 검증 (Induction, §6)

- **프롬프트 기반 검증**: 새로운 관찰과 예측의 일치도 평가(Lampinen et al. 2022)
- **미세 조정 기반**: 학습 신호 활용 가설 정제(Zhao et al. 2023)
- **평가**: True/False 판정, 선택 기반(선택지 중 최고 신뢰도 가설 선택)

### 통합 가설 발견 (Entire Cycle, §7)

- **수동적 발견**: 주어진 가설 검증(Zhu et al. 2024)
- **능동적 발견**: LLM이 자율적으로 새 관찰 기획 및 가설 수정(Li et al. 2024)
- **현실 시뮬레이션**: 게임, 물리 환경 등에서 실제 상호작용 기반 학습(Xu et al. 2023)

## Originality

- **이론적 기여**: Harman의 단순화된 "최선의 설명" 프레임워크를 넘어, Peirce의 세 단계 모델의 순환적 성질과 실시간 증거 수집의 중요성을 강조. 철학적 엄밀성과 실무적 적용 가능성을 동시에 달성.

- **분야 통합**: 기존에 산발적으로 이루어진 LLM 추론, 지식 발견, 규칙 학습 연구를 단일 프레임워크 아래 통합하여 체계적 분석 가능성 확보.

- **포괄적 분류 체계**: 자연언어/형식언어 표현, 프롬프트/RAG/미세조정 방법론, 예측/실제값/인간 평가 지표를 교차 분석하는 다층적 분류.

- **벤치마크와 한계의 구체적 매핑**: 각 방법론이 어느 벤치마크에서 평가되었고 어떤 한계를 보이는지 구체적으로 기록.

## Limitation & Further Study

- **LLM의 창의성과 참신성의 정량화 부재**: 생성된 가설이 정말 "새로운" 지식인지, 단순히 학습 데이터의 조합인지 구분하는 명확한 메트릭 부족. 미래 연구는 신성도(novelty) 측정 방법 개발 필요.

- **작은 규모 데이터에서의 성능 미검증**: 대부분의 연구가 수백 개 관찰치 단위에서만 검증되었으나, 수십만 개 관찰치나 노이즈가 많은 실제 과학 데이터에서의 성능 미지수.

- **형식언어 표현과 자연언어 간 격차**: 형식적 가설은 수학적 엄밀성 보장하지만 해석 불가능성 증가, 자연언어는 해석 가능하나 모호성 존재. 두 표현 간 최적 균형점 미발견.

- **인간 전문가와의 협력 메커니즘 부족**: 현재 인간 지원은 라벨링 단계에 한정되나, 가설 생성 초기 단계에서의 상호작용적 협력 방식 미정립.

- **평가 지표의 편향성**: 기존 벤치마크 대부분이 폐쇄형 문제(closed-world assumption)를 가정하나 현실의 과학 발견은 개방형. 개방형 과학 발견 평가 벤치마크 개발 필요.

- **계산 효율성**: RAG와 미세조정의 계산 비용 분석 부재. 실제 과학 프로젝트 적용 시 비용-효과성 고려 필요.

## Evaluation

- **Novelty (5/5)**: 철학적 기초(Peirce 프레임워크)와 현대 AI(LLM)를 결합한 첫 종합 분석. 기존 산발적 연구를 통일된 이론 아래 통합.

- **Technical Soundness (4.5/5)**: 체계적 분류와 방법론 검토는 우수하나, 일부 평가 지표의 타당성(예: 자동 평가의 신뢰도)에 대한 비판적 논의 부족. 형식언어의 수학적 엄밀성 보장이 제한적.

- **Significance (5/5)**: LLM 기반 자동 과학 발견은 미래 연구, 의료, 정책 수립의 패러다임 전환 가능성 큼. 1000+ 인용 가능성 높음.

- **Clarity (4.5/5)**: 대체로 명확한 구성과 풍부한 예시 제공하나, 자연언어와 형식언어 간 기술적 구별이 특정 섹션(§4)에서 다소 모호함. Figure 1의 분류체계는 직관적이나 더 상세한 알고리즘 의사코드 추가 시 가독성 향상 가능.

- **Overall (4.5/5)**: 

**총평**: 본 설문은 LLM 기반 가설 발견 분야의 첫 체계적 종합 분석으로서, 철학적 엄밀성과 현실적 적용 가능성을 모두 갖춘 고급 논문이다. 다만 벤치마크의 폐쇄형 문제 편향, 실제 과학 데이터에서의 검증 부재, 신성도(novelty) 정량화 방법의 미성숙은 향후 개선이 필요한 핵심 과제이다. AI 커뮤니티에서 가설 발견과 자동 과학 연구의 새로운 연구 방향을 제시하는 기준점이 될 가능성이 높다.

## Related Papers

- 🧪 응용 사례: [[papers/134_Automating_the_practice_of_science_Opportunities_challenges/review]] — 가설 발견과 규칙 학습이 과학 자동화의 핵심 인지적 구성요소가 된다.
- 🏛 기반 연구: [[papers/575_Nobel_Turing_Challenge_creating_the_engine_for_scientific_di/review]] — LLM의 추론 능력이 AI Scientist의 가설 생성 엔진 구현에 필요하다.
- 🔗 후속 연구: [[papers/031_A_Survey_on_Hypothesis_Generation_for_Scientific_Discovery_i/review]] — 과학적 발견에서 가설 생성에 대한 종합적 설문을 LLM 관점에서 확장한다.
- 🏛 기반 연구: [[papers/134_Automating_the_practice_of_science_Opportunities_challenges/review]] — 가설 발견과 규칙 학습이 과학 자동화의 핵심 구성요소가 된다.
- 🏛 기반 연구: [[papers/575_Nobel_Turing_Challenge_creating_the_engine_for_scientific_di/review]] — 가설 발견과 규칙 학습이 자율적 과학 발견 엔진의 핵심 기능이다.
