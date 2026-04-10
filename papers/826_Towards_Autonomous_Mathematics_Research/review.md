---
title: "826_Towards_Autonomous_Mathematics_Research"
authors:
  - "Tony Feng"
  - "Trieu H. Trinh"
  - "Garrett Bingham"
  - "Dawsen Hwang"
  - "Yuri Chervonyi"
date: "2026.02"
doi: "arXiv:2602.10177"
arxiv: ""
score: 4.2
essence: "이 논문은 LLM 기반의 자율적 수학 연구 에이전트인 Aletheia를 소개하며, AI가 IMO 수준의 문제 해결을 넘어 전문 연구 수준의 새로운 수학적 정리를 독립적으로 발견하고 증명할 수 있음을 시연한다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/Autonomous_Hypothesis_Discovery"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Feng et al._2026_Towards Autonomous Mathematics Research.pdf"
---

# Towards Autonomous Mathematics Research

> **저자**: Tony Feng, Trieu H. Trinh, Garrett Bingham, Dawsen Hwang, Yuri Chervonyi, Junehyuk Jung, Joonkyung Lee, Carlo Pagano, Sang-hyun Kim, Federico Pasqualotto, Sergei Gukov, Demis Hassabis, Quoc V. Le, Thang Luong | **날짜**: 2026-02-10 | **DOI**: [arXiv:2602.10177](https://arxiv.org/abs/2602.10177)

---

## Essence

이 논문은 LLM 기반의 자율적 수학 연구 에이전트인 Aletheia를 소개하며, AI가 IMO 수준의 문제 해결을 넘어 전문 연구 수준의 새로운 수학적 정리를 독립적으로 발견하고 증명할 수 있음을 시연한다.

## Motivation

- **Known**: 최근 대형 언어모델(LLM)은 IMO(국제 수학 올림피아드) 금메달 수준의 경쟁 문제 해결 능력을 달성했다.

- **Gap**: 그러나 자기 완결적인 경쟁 문제와 달리, 연구 수준의 수학은 광대한 문헌의 고급 기법을 종합하고 장시간의 추론 체인을 요구한다. 기존 LLM은 훈련 데이터 부족으로 인한 환각(hallucination)과 전문 분야에 대한 얕은 이해 문제가 있다.

- **Why**: AI가 경제적·과학적으로 진정한 가치를 창출하려면, 단순 문제 해결을 넘어 새로운 수학적 발견을 자율적으로 수행할 수 있어야 한다.

- **Approach**: 세 개의 서브 에이전트(Generator, Verifier, Reviser)로 구성된 Aletheia를 개발하여 반복적으로 가설을 생성·검증·개정하고, 심화 사고(Deep Think), 추론 시간 스케일링 법칙, 웹 검색 등의 도구 활용을 통해 연구 수준의 수학 문제를 해결한다.

## Achievement

![Figure 1](figures/fig1.webp)
*Figure 1: Aletheia의 시각적 개요 - Generator, Verifier, Reviser의 반복적 상호작용*

![Figure 2](figures/fig1.webp)
*Figure 2: 2026년 1월 advanced 버전의 Deep Think는 (a) IMO 수준과 (b) 박사 수준 문제에서 우수한 스케일링 법칙을 보임*

1. **완전 자율적 연구 논문**: 인간 개입 없이 산술 기하학의 고유가중(eigenweights) 계산에 대한 출판 가능한 논문(Feng26) 생성

2. **Erdős 문제 해결**: Bloom's Erdős Conjectures 데이터베이스의 700개 미해결 문제 중 4개의 Erdős 문제를 자율적으로 해결(예: Erdős-1051), 세 수십 년간 미해결이었던 문제들을 포함

3. **하이브리드 협력**: 인간 수학자와의 협력을 통해 다중 논문에 기여(LeeSeo26, FYZ26, ACGKMP26), 이전 증명을 개선하는 중간 명제(intermediate propositions) 도출

4. **FirstProof 벤치마크**: 수학자들이 제안한 10개의 연구 수준 문제 집합에서 최고 성능 달성

## How

![Figure 1](figures/fig1.webp)

- **Deep Think 진화**: 2025년 7월 IMO Gold 버전에서 2026년 1월 advanced 버전으로 개선되어, 동등한 성능 달성에 필요한 계산량이 약 100배 감소

- **추론 시간 스케일링 법칙**: IMO 수준 문제에서 관찰된 스케일링 법칙이 박사 수준 연습 문제(FutureMath Basic)로도 이전되며, 더 많은 추론 자원이 정확도 향상으로 이어짐

- **에이전트 아키텍처**: 
  - **Generator**: Deep Think를 활용하여 초기 해결안 생성
  - **Verifier**: 생성된 해결안의 논리적 타당성 검증 (반복 생각 분리의 중요성 발견)
  - **Reviser**: 실패한 시도로부터 학습하여 해결안 개정

- **도구 활용**: Google Search와 웹 브라우징을 통해 광대한 수학 문헌에 접근하고, 환각 문제 완화

- **자연어 종단간(End-to-End) 처리**: AlphaGeometry나 AlphaProof의 형식 언어(formal language) 접근과 달리, 자연 언어로 전체 연구 과정 수행

- **자율성 분류 체계**: Level 0(무시할 만한 새로움)부터 Level 4(획기적 발견)까지의 분류 테이블(Table 1)을 제안하여 AI 보조 수학 결과의 투명한 평가 기준 제시

## Originality

- **최초의 완전 자율적 연구 논문**: 인간 수학자의 개입 없이 발표 수준의 원본 수학 논문을 생성한 첫 사례

- **아게틱 검증 프레임워크**: 추론 과정과 검증 단계의 명시적 분리가 모델의 자체 오류 인식 능력을 향상시킨다는 발견은 LLM의 추론 메커니즘에 대한 중요한 통찰

- **미해결 문제 해결**: 단순한 공개 문제 해결이 아니라, 수십 년간 미해결 상태인 Erdős 문제를 진정한 증명과 함께 해결

- **AI 연구 투명성 제안**: "Autonomous Mathematics Research Levels"라는 표준화된 분류 체계를 제안하여, 향후 AI 수학 연구의 신뢰성 있는 평가와 소통을 위한 기초 마련

- **추론 시간 스케일링의 일반화**: IMO 문제에 한정된 기존 발견을 박사 수준 문제로 성공적으로 확장

## Limitation & Further Study

- **성과의 규모 제한**: 논문에서 명시하듯이, 자율적으로 발견된 결과들은 수학 분야에서 "주요 진전(major advance)"에 해당하지 않으며, 대부분 이미 존재하는 이론의 점진적 확장 수준

- **환각 문제**: 웹 검색 없이는 논문 날조(paper fabrication)가 발생하고, 도구 활용 교육 후에도 잘못된 인용이 남아있으며, 더 정교한 검증 메커니즘 필요

- **추론 효율성**: PhD 수준 문제에서 IMO 문제보다 훨씬 낮은 정확도(Figure 2b)를 보이며, 도메인 특화 지식 부족이 여전한 과제

- **평가의 인적 의존성**: 반자율적 평가(semi-autonomous evaluation)의 많은 부분이 인간 전문가의 검증에 의존하여, 완전 자율성의 주장이 부분적으로 제한됨

- **후속 연구**: 
  - 더 복잡한 대수적 구조나 해석학 분야로의 확장 필요
  - 형식 검증(formal verification)과의 결합으로 증명의 신뢰성 강화
  - 인간 수학자와의 상호작용 메커니즘 개선
  - 자율성 분류 체계의 수학 공동체 합의 도출

## Evaluation

- **Novelty (혁신성)**: 4.5/5 
  - 완전 자율적 수학 연구 논문 생성은 처음이지만, 개별 기술(agentic harness, verification)은 기존 아이디어의 결합

- **Technical Soundness (기술적 건전성)**: 4/5
  - 체계적인 실험 설계와 전문가 평가 기반이나, 스케일링 법칙의 이론적 분석 부재
  - 환각 및 검증 한계에 대한 추가 분석 필요

- **Significance (중요성)**: 4.5/5
  - AI 과학 연구의 새로운 패러다임 시현이나, 수학 분야의 실제 영향은 아직 제한적
  - 투명성 제안(Autonomous Levels)은 장기적 의의가 높음

- **Clarity (명확성)**: 4/5
  - 전반적으로 명확하나, 일부 기술 세부사항(Deep Think의 구체적 구조) 부재
  - 자율성 분류 체계가 Table 1에만 제시되어 본문 상세 설명 필요

- **Overall (종합)**: 4.2/5

**총평**: 본 논문은 경쟁 수학 해결에서 자율적 연구 발견으로의 의미 있는 전환을 보여주며, 특히 투명한 평가 기준 제시라는 메타적 기여가 중요하다. 다만 해결된 문제들의 수학적 중요도가 제한적이고 환각 문제의 근본적 해결이 미흡하여, 진정한 "연구 자율성"의 주장이 부분적으로 경계되어야 한다.

## Related Papers

- 🧪 응용 사례: [[papers/825_Towards_an_AI_co-scientist/review]] — AI co-scientist의 가설 생성-개선 메커니즘이 Aletheia의 자율적 수학 정리 발견에 구체적으로 적용된 전문 영역 특화 사례이다.
- 🔗 후속 연구: [[papers/071_AgentRxiv_Towards_Collaborative_Autonomous_Research/review]] — AgentRxiv의 협업적 연구 프레임워크가 Aletheia의 수학 연구 자동화를 위한 다중 에이전트 지식 공유 시스템으로 확장된 형태이다.
- 🏛 기반 연구: [[papers/264_Deepseek-prover_Advancing_theorem_proving_in_llms_through_la/review]] — DeepSeek-Prover의 대규모 언어 모델 기반 정리 증명이 Aletheia의 자율적 수학 연구 및 증명 능력의 핵심적인 기술적 토대이다.
- 🔗 후속 연구: [[papers/071_AgentRxiv_Towards_Collaborative_Autonomous_Research/review]] — 수학 연구의 자율적 정리 발견을 위한 Aletheia가 AgentRxiv의 협업적 연구 프레임워크를 전문 수학 도메인으로 확장한 사례이다.
- 🔗 후속 연구: [[papers/825_Towards_an_AI_co-scientist/review]] — Aletheia의 자율적 수학 연구가 AI co-scientist의 가설 생성 및 검증 프레임워크를 전문 수학 영역으로 특화하여 확장한 적용이다.
- 🧪 응용 사례: [[papers/864_VASPilot_MCP-Facilitated_Multi-Agent_Intelligence_for_Autono/review]] — 자율적 수학 연구를 위한 자동화 시스템으로 계산 과학의 완전 자동화 비전을 공유한다.
