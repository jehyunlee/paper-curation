---
title: "081_Ai_scientists_fail_without_strong_implementation_capability"
authors:
  - "Min Zhu"
  - "Qiujie Xie"
  - "Yixuan Weng"
  - "Jian Wu"
  - "Zhen Lin"
date: "2025"
doi: "미제공"
arxiv: ""
score: 4.25
essence: "대규모 언어모델(LLM) 기반 AI Scientist는 우수한 아이디어 생성 능력을 보유했으나, **실제 과학적 검증과 실험 구현 능력이 심각하게 부족**하여 진정한 자동화 과학 연구 달성에 실패하고 있다는 입장 논문이다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/AI_Research_Ideation"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Zhu et al._2025_Ai scientists fail without strong implementation capability.pdf"
---

# AI Scientists Fail Without Strong Implementation Capability

> **저자**: Min Zhu, Qiujie Xie, Yixuan Weng, Jian Wu, Zhen Lin, Linyi Yang, Yue Zhang | **날짜**: 2025 | **DOI**: [미제공](https://arxiv.org/abs/2506.01372)

---

## Essence

![Figure 1](figures/fig1.webp)
*AI Scientist의 발전 로드맵(2024~미래)에서 구현 격차(Implementation Gap) 해결의 중요성을 강조*

대규모 언어모델(LLM) 기반 AI Scientist는 우수한 아이디어 생성 능력을 보유했으나, **실제 과학적 검증과 실험 구현 능력이 심각하게 부족**하여 진정한 자동화 과학 연구 달성에 실패하고 있다는 입장 논문이다.

## Motivation

- **Known**: 
  - 최근 AI Scientist 시스템(AI Scientist-v2, Zochi 등)이 ICLR 2025, ACL 2025에서 논문 수락 성과 달성
  - LLM 기반 시스템이 아이디어 생성과 독립적 과학 연구 수행 능력 시연
  - AlphaFold, A-Lab 등 자동화 과학 도구에서 혁신적 성과 달성

- **Gap**: 
  - AI Scientist 시스템이 아직 컴퓨터 과학 분야에서 획기적 성과 미달성
  - 생성된 아이디어와 최종 검증된 결과물 사이의 격차 존재
  - 코드 구현 및 실험 실행 단계에서의 능력 한계 미분석

- **Why**: 
  - AI Scientist의 핵심 역량을 명확히 정의하고 현재 한계점을 체계적으로 규명할 필요성
  - 단순 아이디어 생성이 아닌 **완전 자동화 과학 연구(end-to-end execution)** 실현의 장애물 파악 필수

- **Approach**: 
  - AI Scientist 문헌의 연구 동향 분석
  - 복잡 공학 작업 벤치마크 정량 분석 (MLE-Bench, PaperBench, SciReplicate-Bench 등)
  - 28편의 AI 생성 논문에 대한 체계적 동료 검토 평가 (DeepReviewer-14B 활용)

## Achievement

![Figure 3](figures/fig3.webp)
*arXiv AI Scientist 논문 분석: 구현 세부사항 포함 논문의 인용도가 2.4배 높음(25.0 vs 10.3)*

1. **구현 격차의 정량적 입증**: 
   - Claude 3.5 Sonnet이 PaperBench에서 1.8% 정확도만 달성
   - OpenAI o1-preview가 MLE-Bench에서 16.90% 성능으로 심각한 코드 구현 능력 부족 실증

2. **출판 추세와 영향도 불일치 규명**: 
   - 구현 상세 포함 논문이 총 인용 수 325회(평균 25.0회)
   - 구현 미상세 논문이 총 인용 수 216회(평균 10.3회)로 2.4배 격차 확인
   - 높은 영향도에도 불구하고 구현 중심 연구가 상대적으로 적음은 **실행의 어려움**을 시사

3. **AI Scientist의 엄격한 개념 정의 제시**: 
   - AI Scientist = 아이디어 생성 + 검증 실행의 이중 능력 필요
   - 기존 과학 도구(scientific tools)와 근본적 차이 명확화

## How

![Figure 2](figures/fig2.webp)
*과학 도구 vs AI Scientist: 과학 도구는 인간 감독 하에 데이터→결과 처리, AI Scientist는 자율적으로 연구 질문→솔루션 도출*

**방법론 및 평가 기법:**

- **문헌 분석**: 2025년 5월 23일까지 arXiv의 AI Scientist 논문 통계 분석
  - 구현 유무 기준으로 분류 및 인용도 비교
  
- **벤치마크 종합 분석**:
  - 5개 주요 벤치마크(MLE-Bench, PaperBench, SciReplicate-Bench, CORE-Bench, ML-Dev-Bench) 종합
  - 기계학습, NLP, CV, 의학 등 다분야 커버(총 8,816개 사례)
  - 최신 LLM(o1-preview, Claude 3.5, GPT-4o) 성능 평가

- **LLM-as-a-Judge 동료 검토**: 
  - 최신 리뷰 모델(DeepReviewer-14B) 활용
  - 5개 AI Scientist 시스템이 생성한 28편 논문 정성적 평가
  - 아이디어 혁신성 vs 검증 엄밀성 비교

- **정형화된 수학적 정의**:
  - AI Scientist 𝒮_AI를 함수로 모델링: (𝒦_new, 𝒜_sci) ← max{𝒮_AI(𝒬_init, 𝒦_domain, ℛ_human | θ_AI, ℬ_res)}
  - 윤리 제약(ℛ_human), 자원 제약(ℬ_res) 명시적 포함

## Originality

- **개념적 기여**: AI Scientist의 첫 엄밀한 수학적 정의와 과학 도구와의 명확한 구분 제시
  - 기존: 단편적 시스템 평가
  - 신규: 완전 자동화 과학 연구의 필요 조건 체계화

- **대규모 실증 분석**: 8,816개 코드 구현 벤치마크 사례 종합으로 LLM 실행 능력의 광범위한 부족 입증
  - 단순 이론 비판이 아닌 다각적 정량 증거 제시

- **새로운 평가 메커니즘**: DeepReviewer-14B를 활용한 AI 생성 논문의 동료 검토 프레임워크
  - 기존 자동 메트릭(BLEU, ROUGE)의 한계 극복

- **출판 메타분석의 통찰**: 구현 포함 논문이 실제로 학계에서 2.4배 더 높이 평가받음을 실증
  - 연구 커뮤니티의 암묵적 가치 판단을 정량화

## Limitation & Further Study

- **범위 제한**: 
  - 컴퓨터 과학 중심 분석 (생물학, 화학 등 타분야 미포함)
  - 28편의 AI 생성 논문 샘플이 전체 AI Scientist 생산물을 충분히 대표하는지 불명확
  - 동료 검토 평가가 단일 LLM 기반(편향 가능성)

- **미해결 문제**:
  - **구현 능력 향상의 기술적 방안** 구체화 부족 (위치만 지적, 해결책 제시 미흡)
  - 아이디어 생성과 구현 간의 계층적 어려움 분석 필요
  - 자원 제약 조건에서 실현 가능한 아이디어 필터링 방안 미제시

- **후속 연구 방향**:
  - 코드 생성 LLM의 아키텍처 개선 (예: 실시간 피드백 루프, 자동 테스트 통합)
  - 인간-AI 협업 모델 (AI가 아이디어 제시, 인간이 검증 감독)
  - 도메인 특화 구현 도구(domain-specific tools) 개발로 실행 능력 보강
  - 재현성(reproducibility) 중심의 AI Scientist 벤치마크 구축


## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 5/5
- Clarity: 4/5
- Overall: 4.25/5

**총평**: 이 논문은 AI Scientist의 현주소를 객관적 데이터로 진단한 중요한 비판적 분석 연구로, **아이디어 생성의 성공이 실행의 실패로 귀결되는 근본 문제**를 명확히 드러낸다. 커뮤니티가 과장된 낙관론을 벗고 기술적 현실을 직시하게 하는 값진 기여이나, 해결책 제시 강화로 더욱 건설적 영향력을 발휘할 수 있을 것으로 기대된다.

## Related Papers

- ⚖️ 반론/비판: [[papers/834_Towards_Scientific_Discovery_with_Generative_AI_Progress_Opp/review]] — 생성형 AI의 과학 연구 가능성에 대해 비판적 관점을 제시하며 실제 구현 능력의 한계를 지적한다
- ⚖️ 반론/비판: [[papers/795_The_AI_Scientist_Towards_Fully_Automated_Open-Ended_Scientif/review]] — AI Scientist의 성과에 대해 구현 능력 부족이라는 근본적 한계를 제기한다
- 🔗 후속 연구: [[papers/321_Evaluating_Sakanas_AI_Scientist_Bold_Claims_Mixed_Results_an/review]] — AI Scientist 평가를 통해 자율 연구의 실제 한계를 구체적으로 분석한다
- 🧪 응용 사례: [[papers/704_SciAgentGym_Benchmarking_Multi-Step_Scientific_Tool-use_in_L/review]] — 과학 도구 사용 벤치마크를 통해 AI의 실제 과학 수행 능력을 검증할 수 있다
- 🔗 후속 연구: [[papers/834_Towards_Scientific_Discovery_with_Generative_AI_Progress_Opp/review]] — AI 과학자의 구현 능력 부족 문제를 구체적으로 분석하고 해결 방향을 제시한다
- ⚖️ 반론/비판: [[papers/795_The_AI_Scientist_Towards_Fully_Automated_Open-Ended_Scientif/review]] — AI 과학자의 성공 사례에 대해 구현 능력 부족이라는 비판적 관점을 제시한다
