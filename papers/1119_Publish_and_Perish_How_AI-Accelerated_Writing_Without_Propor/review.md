---
title: "1119_Publish_and_Perish_How_AI-Accelerated_Writing_Without_Propor"
authors:
  - "Seok Joon Kwon"
date: "2026.04"
doi: "10.48550/arXiv.2604.05714"
arxiv: ""
score: 4.0
essence: "AI 기반 논문 작성 도구의 급속한 확산이 동료 검증(peer review) 능력을 초과하면서 과학적 지식 생산이 역설적으로 감소하는 현상을 제조업의 제약 이론(Theory of Constraints)으로 정량화한 동역학 모델 연구."
tags:
  - "cat/Science_of_Science_Research"
  - "cat/Research_Quality_and_Demographics"
  - "sub/Scientific_Publishing_and_Incentives"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Kwon_2026_Publish and Perish How AI-Accelerated Writing Without Proportional Verification Investment Degrades.pdf"
---

# Publish and Perish: How AI-Accelerated Writing Without Proportional Verification Investment Degrades Scientific Knowledge

> **저자**: Seok Joon Kwon | **날짜**: 2026-04-07 | **DOI**: [10.48550/arXiv.2604.05714](https://doi.org/10.48550/arXiv.2604.05714)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1 presents the baseline simulation over a 20-year horizon (initial point t = 0 at November 2022*

AI 기반 논문 작성 도구의 급속한 확산이 동료 검증(peer review) 능력을 초과하면서 과학적 지식 생산이 역설적으로 감소하는 현상을 제조업의 제약 이론(Theory of Constraints)으로 정량화한 동역학 모델 연구.

## Motivation

- **Known**: AI 도구가 논문 작성을 가속화하고 있으며, 동료 검증 과정에서도 AI 활용이 증가하고 있다는 실증적 증거가 존재한다. 과학 출판 시스템의 병목 현상(bottleneck)은 논문 작성이 아니라 심층적 검증 능력에 있다.
- **Gap**: AI 채택 동역학과 지식 생산량 간의 정량적 연결고리를 제공하는 수학적 프레임워크가 부재했다. 특히 검증 투자 부족이 지식 산출에 미치는 시스템 수준의 영향을 정형화한 연구가 없었다.
- **Why**: AI 도구의 비대칭적 확산(writing AI >> review AI)이 장기적 과학적 지식 품질 저하를 초래할 수 있으므로, 임계 조건 파악과 정책 개입 방안 도출이 시급하다.
- **Approach**: 2개 상태변수(리뷰 큐Q, 검증 품질q)와 1개 외생입력(논문작성 AI 채택 φw)을 갖는 최소 ODE 모델을 구성하여, 큐 압력이 리�뷰어 AI 채택(φr)을 내생적으로 유도하는 피드백 메커니즘을 포착했다.

## Achievement

![Figure 3](figures/fig3.webp)

*Figure 3 maps long time behavior of the knowledge measured by K(t = 20 yr)/K0 across the (γ, δ) parameter*

- **'허니문-역설' 현상 정량화**: 지식 산출이 2026년경 1.10K₀으로 정점에 도달 후 2028년 역설 개시, 32% 손실로 저하되는 시간 경로 예측", '**임계 조건 도출**: δ > γ (리뷰 가속도 > 논문작성 가속도) 만족 시에만 순편익 가능; 현재 운영점은 δ=0.5, γ=2.0으로 역설 영역 심화
- **실증적 검증**: NeurIPS, ICLR, arXiv, bioRxiv 데이터로 Post-ChatGPT 제출 가속화 패턴과 정성적 일치 확인
- **정책 레버 분석**: 리뷰 인프라 투자와 제도적 품질 기준의 복합 개입만이 긍정적 지식 생산 복구 가능 시사

## How

![Figure 2](figures/fig2.webp)

*Figure 2. Empirical validation. Annual submissions for (a) NeurIPS (2008-2025), (b) ICLR (2013-2026),*

- 논문작성 AI 채택을 로지스틱 함수로 모델링 (tw=3.0년, 2025년 50% 채택률)
- 리뷰어 AI 채택을 Michaelis-Menten형 포화 함수로 표현 (큐 크기의 비선형 함수)
- 제출 증가 S(t)=S₀(1+γφw)와 고정 검증 용량 R(t)=Rmax(1+δφr)의 비대칭성 포착
- 검증 품질 q(t)를 AI 채택으로의 저하와 인간 검수자의 복구력의 경합으로 모델링
- 지식 산출 K(t)=R(t)q(t)로 정의하여 시스템 전체 효율 측정
- Amdahl 법칙과 실제 제출 CAGR 데이터로 γ=2.0, δ=0.5 파라미터 설정 정당화
- 민감도 분석(sensitivity analysis)으로 9개 파라미터 중 5개의 영향도 평가

## Originality

- 제약 이론(Theory of Constraints)을 과학 출판에 처음 적용하여 병목 현상을 정량 프레임화
- 검증 채무(verification debt) 개념을 소프트웨어 공학의 기술 채무 유추로 도입
- 외생적 writing AI 채택이 내생적 review AI 채택을 유도하는 일방향 인과사슬 모델화는 선행 연구에 없는 구조
- 동역학 모델로 'productivity illusion'과 system failure 간 연결고리를 수학적으로 증명

## Limitation & Further Study

- 모델이 최소 설계(minimal)로서 협력자 효과, 저널별 차별화된 검증 표준, 분야별 이질성을 반영하지 못함
- γ=2.0은 AI 도구 효과와 커뮤니티 성장, 시장 진입장벽 하락 등을 혼합 포함하므로 순수 AI 효과 분리 필요
- 실증 검증이 NeurIPS, ICLR 등 4개 플랫폼 정성적(qualitative) 일치에 머물러 정량적(quantitative) 피팅 부족
- qmin, η 등 정책변수의 파라미터 값이 전문가 판단에 의존하므로 실제 측정 데이터로의 보정 필요
- **후속 연구**: (1) 검증 품질 q(t)를 직접 측정 지표(논문 재현성, 인용율 등)로 검증, (2) 분야별·저널별 이질성 모델, (3) 리뷰어 번아웃 동역학 포함, (4) 정책 개입의 실제 효과 A/B 테스팅

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 과학 출판 위기를 처음으로 동역학 모델로 정량화하고 임계 조건을 도출한 중요한 이론 기여. 실증 데이터와의 정량적 피팅 강화 및 정책 효과의 실제 검증이 다음 단계로 필요하다.

## Related Papers

- 🏛 기반 연구: [[papers/1021_Scientific_production_in_the_era_of_large_language_models/review]] — LLM 시대 과학 생산 증가의 역설적 결과로 동료 검증 시스템의 한계가 지식 생산 감소로 이어지는 구조적 문제를 설명한다.
- 🔗 후속 연구: [[papers/1045_The_strain_on_scientific_publishing/review]] — 과학 출판의 압박과 AI 가속화된 글쓰기가 결합되어 동료 검증 시스템에 미치는 복합적 부담을 분석할 수 있다.
- ⚖️ 반론/비판: [[papers/953_Do_Large_Language_Models_Reduce_Research_Novelty_Evidence_fr/review]] — LLM이 연구 참신성을 감소시킨다는 발견과 AI 글쓰기 도구의 급속한 확산이 과학적 지식 생산에 미치는 상반된 효과를 보여준다.
- ⚖️ 반론/비판: [[papers/1065_A_Survey_of_AI_Scientists/review]] — AI 가속 연구의 부정적 측면인 적절한 검증 없는 논문 발표 문제를 지적하여 AI 과학자 시스템의 한계를 보여준다.
- 🏛 기반 연구: [[papers/953_Do_Large_Language_Models_Reduce_Research_Novelty_Evidence_fr/review]] — AI 가속화된 글쓰기가 적절한 사고 없이 이루어질 때의 문제점이 연구 새로움 감소의 근본 원인을 설명한다.
- ⚖️ 반론/비판: [[papers/1033_The_Empowerment_of_Science_of_Science_by_Large_Language_Mode/review]] — AI 가속화된 글쓰기의 부정적 영향을 지적하여 LLM 활용의 한계를 제시한다
- 🔗 후속 연구: [[papers/1045_The_strain_on_scientific_publishing/review]] — AI 가속화된 글쓰기가 적절한 기여 없이 출판 부담을 더욱 심화시키는 메커니즘을 구체적으로 분석한다.
- 🔗 후속 연구: [[papers/1021_Scientific_production_in_the_era_of_large_language_models/review]] — AI 가속화된 논문 작성이 동료 검증 시스템에 미치는 부담을 정량적으로 분석하여 생산성 증가의 역설을 설명한다.
