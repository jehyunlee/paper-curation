---
title: "834_Towards_Scientific_Discovery_with_Generative_AI_Progress_Opp"
authors:
  - "Chandan K. Reddy"
  - "P. Shojaee (Virginia Tech)"
date: "2024"
doi: "10.48550/arXiv.2412.11427"
arxiv: ""
score: 4.3
essence: "생성형 AI가 문헌 분석, 정리 증명(theorem proving), 실험 설계, 데이터 기반 발견 등 과학 연구의 개별 과제들에서 놀라운 진전을 이루었으나, 장기적 자율 과학 연구를 수행할 수 있는 통합된 AI 시스템은 여전히 부재한다. 본 논문은 과학 발견을 위한 포괄적 AI 시스템 개발의 핵심 과제와 연구 방향을 체계적으로 제시한다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/AI_Scientific_Discovery"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Reddy and Shojaee_2024_Towards Scientific Discovery with Generative AI Progress, Opportunities, and Challenges.pdf"
---

# Towards Scientific Discovery with Generative AI: Progress, Opportunities, and Challenges

> **저자**: Chandan K. Reddy, P. Shojaee (Virginia Tech) | **날짜**: 2024 | **DOI**: [10.48550/arXiv.2412.11427](https://doi.org/10.48550/arXiv.2412.11427)

---

## Essence

![Figure 1](figures/fig1.webp)
*AI 기반 과학 발견 프레임워크의 개요. 사용자 정의 문제 명세에서 시작하여 문헌 검색, 가설 생성, 실험 설계, 평가를 반복하는 과학적 탐구 사이클을 보여줌*

생성형 AI가 문헌 분석, 정리 증명(theorem proving), 실험 설계, 데이터 기반 발견 등 과학 연구의 개별 과제들에서 놀라운 진전을 이루었으나, 장기적 자율 과학 연구를 수행할 수 있는 통합된 AI 시스템은 여전히 부재한다. 본 논문은 과학 발견을 위한 포괄적 AI 시스템 개발의 핵심 과제와 연구 방향을 체계적으로 제시한다.

## Motivation

- **Known**: 
  - 심볼릭 AI(symbolic AI)에서부터 딥러닝, 대규모 언어모델(LLM)에 이르기까지 AI 기술이 과학적 추론의 자동화에 진전을 이룸
  - LLM이 문헌 분석, 가설 생성, 실험 설계, 방정식 발견 등 특정 과학 과제에서 효과를 입증함

- **Gap**: 
  - 대부분의 기존 연구는 과학적 추론의 좁은 측면만 단독으로 다룸
  - 문맥 검색(context retrieval)부터 가설 생성, 실험 설계, 평가까지 과학적 탐구의 전체 사이클을 통합하는 AI 시스템 부재
  - 과학 발견을 위한 적절한 벤치마크 및 평가 프레임워크 부족

- **Why**: 
  - 과학 발견의 복잡한 인지 과정을 자동화하기 위해서는 다양한 AI 기술의 통합 필요
  - 현존 벤치마크의 문제점(LLM의 암기 기반 해결, 이미 알려진 법칙 재발견 중심)

- **Approach**: 
  - 과학 발견 AI의 현황을 종합적으로 검토
  - (i) 개선된 벤치마크 및 평가 프레임워크 개발, (ii) 과학 지식 기반 AI 에이전트 개발, (iii) 다중모달 과학 표현 확대, (iv) 추론, 정리 증명, 데이터 기반 모델링의 통합을 핵심 과제로 제시

## Achievement

![Figure 2](figures/fig2.webp)
*과학 중심 AI 에이전트를 위한 포괄적 프레임워크. 에이전트의 구성 요소와 상호작용을 도시함*

### 최근 AI 과학 기술의 주요 진전

1. **문헌 분석 및 아이디어 발상**
   - PubMedBERT, BioBERT, SciBERT 등 과학 도메인 특화 LLM 등장
   - SciMON: 기존 문헌의 패턴을 분석하여 새로운 과학적 아이디어 생성
   - 효율적인 정보 검색, 요약, 복잡한 쿼리 기반 질의응답 가능

2. **정리 증명(Automated Theorem Proving)**
   - GPT-f: 트랜스포머 기반 언어 모델을 증명 전술(proof tactics)로 학습
   - Draft-Sketch-Prove 방식: 비형식 증명을 형식 스케치로 변환 후 증명 보조 도구로 완성
   - 복잡한 과학 이론 도출 및 형식화 가능성 제시

3. **실험 설계 자동화**
   - LLM 에이전트 기반 시스템으로 최소 인간 개입으로 실험 설계, 계획, 최적화, 실행 가능
   - 물리학: 양자 실험 설계 및 고에너지 물리 시뮬레이션 최적화
   - 화학: 화학 반응 설계 및 최적화
   - 생물학/의학: 유전자 편집 프로토콜 최적화, 임상 시험 설계

4. **데이터 기반 발견**
   - **약물 발견**: 생성형 모델과 다중모달 표현 학습으로 수백만 분자 탐색하여 신규 항생제 발견
   - **방정식 발견(symbolic regression)**: AI Feynman에서 시작하여 LLM 기반 접근으로 발전. LLM-SR은 LLM을 진화 탐색의 과학자 에이전트로 활용
   - **재료 발견**: GNoME(Graph Networks for Materials Exploration)로 알려진 안정 결정(stable crystals) 개수를 한 자릿수 배 증가. AtomAgents는 LLM을 재료 발견 파이프라인에 통합하여 합금 설계 개선

## How

### 과학 발견을 위한 AI 시스템 개발 방향

- **다중모달 과학 표현 (Multimodal Scientific Representations)**
  - 텍스트 기반 표현을 넘어 수치 데이터, 이미지, 그래프, 수식 등 다양한 형태의 통합 표현 필요
  - 예: SNIP 모델이 기호 표현(symbolic expressions)과 수치 데이터 간의 다중모달 표현 학습 시도

- **과학 중심 AI 에이전트 (Science-Focused AI Agents)**
  - 과학적 지식과 추론 능력을 활용하는 에이전트 개발
  - 실험 결과 해석, 가설 수정, 차별화된 아이디어 탐색 능력
  - 인간 과학자와의 협력 메커니즘 포함

- **벤치마크 및 평가 프레임워크 개선**
  - 이미 알려진 과학 법칙 재발견 중심의 벤치마크에서 벗어나 **진정한 새로운 발견** 중심으로 전환
  - LLM의 암기 기반 답변과 진정한 추론/발견의 구분
  - 개방형 과학 발견의 복잡성을 포착하는 평가 메트릭 설계

- **추론, 정리 증명, 데이터 기반 모델링의 통합**
  - 형식적 수학적 추론과 데이터 기반 패턴 발견의 시너지
  - 신경 기호적(neuro-symbolic) 접근법 강화

## Originality

- **포괄적 문제 정의**: 과학 발견의 전체 사이클을 다루는 통합 AI 시스템이라는 개념 제시
- **체계적 현황 분석**: 문헌 분석부터 데이터 기반 발견까지 다양한 과학 과제의 최신 AI 기술 현황을 통일된 관점에서 검토
- **구체적 과제 제시**: 단순 요구사항 나열이 아닌, 벤치마크, 에이전트, 표현 학습, 통합 프레임워크라는 구체적 연구 방향 제시
- **학제 간 기여**: 물리학, 화학, 생물학, 재료과학 등 다양한 과학 분야의 사례 통합

## Limitation & Further Study

- **추상적 레벨의 제시**: 논문은 핵심 과제를 제시하지만, 각 과제를 해결하기 위한 구체적 기술적 솔루션은 제한적
- **실제 과학 발견의 복잡성 미반영**: 논문에서 논의된 대부분의 사례는 구체적 목표가 명확한 과제(약물 발견, 재료 발견)로, 원천적 탐사(fundamental exploration)가 필요한 기초 과학에서의 적용 가능성 불명확
- **인간-AI 협력의 상세 부족**: AI 시스템이 인간 과학자와 어떻게 협력할지에 대한 구체적 메커니즘 미제시
- **계산 효율성 논의 부재**: 대규모 LLM 기반 과학 발견 시스템의 에너지 소비 및 환경 영향 미논의

**후속 연구 방향**:
- 과학 발견 벤치마크의 설계 원칙 개발
- 실제 미개척 과학 문제를 대상으로 한 파일롯 시스템 구축
- 상이한 과학 분야 간의 전이 학습(transfer learning) 메커니즘 연구


## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 5/5
- Clarity: 4/5
- Overall: 4.3/5

**총평**: 본 논문은 과학 발견을 위한 AI의 현재 진전과 미래 방향을 체계적으로 정리한 중요한 위치 논문으로, AI와 과학의 교집합에서 당면한 핵심 과제들을 명확히 제시한다. 개별 AI 기술의 구체적 혁신보다는 통합 시스템 구축을 위한 로드맵 제시라는 점에서 학계와 산업에 중요한 가이드를 제공할 수 있을 것으로 판단된다.

## Related Papers

- 🏛 기반 연구: [[papers/795_The_AI_Scientist_Towards_Fully_Automated_Open-Ended_Scientif/review]] — 완전 자동화 과학 연구 시스템의 현실적 한계와 필요 구성 요소에 대한 이론적 기반을 제공한다
- 🔗 후속 연구: [[papers/081_Ai_scientists_fail_without_strong_implementation_capability/review]] — AI 과학자의 구현 능력 부족 문제를 구체적으로 분석하고 해결 방향을 제시한다
- 🏛 기반 연구: [[papers/088_AI4Research_A_Survey_of_Artificial_Intelligence_for_Scientif/review]] — 과학 연구를 위한 AI 시스템의 전반적 프레임워크와 방법론적 기반을 제공한다
- 🧪 응용 사례: [[papers/575_Nobel_Turing_Challenge_creating_the_engine_for_scientific_di/review]] — 과학 발견 엔진 개발의 구체적 실현 방안과 도전 과제를 제시한다
- ⚖️ 반론/비판: [[papers/081_Ai_scientists_fail_without_strong_implementation_capability/review]] — 생성형 AI의 과학 연구 가능성에 대해 비판적 관점을 제시하며 실제 구현 능력의 한계를 지적한다
- 🧪 응용 사례: [[papers/795_The_AI_Scientist_Towards_Fully_Automated_Open-Ended_Scientif/review]] — 생성형 AI를 이용한 과학 발견의 이론적 프레임워크를 완전 자동화 시스템으로 구현한다
- 🔗 후속 연구: [[papers/076_AI_for_Science_An_Emerging_Agenda/review]] — 과학 발견에서 생성형 AI 활용의 진전과 기회를 구체적으로 분석
