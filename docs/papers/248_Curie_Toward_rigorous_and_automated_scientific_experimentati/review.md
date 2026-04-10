---
title: "248_Curie_Toward_rigorous_and_automated_scientific_experimentati"
authors:
  - "Patrick Tser Jern Kon"
  - "Jiachen Liu"
  - "Qi Ding"
  - "Yiming Qiu"
  - "Zhenning Yang"
date: "2025"
doi: "N/A"
arxiv: ""
score: 4.3
essence: "본 논문은 대규모 언어 모델(LLM) 기반 AI 에이전트를 활용하여 엄밀하고 자동화된 과학 실험 수행을 가능하게 하는 프레임워크 Curie를 제안한다. 신뢰성(reliability), 방법론적 통제(methodical control), 해석가능성(interpretability)을 갖춘 세 가지 핵심 모듈을 통해 실험 과정에 엄밀함을 내재화하고, 기존 베이스라인 대비 3.4배 향상된 성능을 달성한다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/Autonomous_Hypothesis_Discovery"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Kon et al._2025_Curie Toward rigorous and automated scientific experimentation with ai agents.pdf"
---

# Curie: Toward rigorous and automated scientific experimentation with ai agents

> **저자**: Patrick Tser Jern Kon, Jiachen Liu, Qi Ding, Yiming Qiu, Zhenning Yang, Yibo Huang, Jayanth Srinivasa, Myungjin Lee, Mosharaf Chowdhury, Ang Chen | **날짜**: 2025 | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp)
*Figure 1. Curie overview.*

본 논문은 대규모 언어 모델(LLM) 기반 AI 에이전트를 활용하여 엄밀하고 자동화된 과학 실험 수행을 가능하게 하는 프레임워크 Curie를 제안한다. 신뢰성(reliability), 방법론적 통제(methodical control), 해석가능성(interpretability)을 갖춘 세 가지 핵심 모듈을 통해 실험 과정에 엄밀함을 내재화하고, 기존 베이스라인 대비 3.4배 향상된 성능을 달성한다.

## Motivation

- **Known**: 최근 LLM을 활용한 과학 연구 자동화 연구가 증가하고 있으며, 문헌 검토, 브레인스토밍 등 창의적 작업에서 효과적이다.
- **Gap**: 기존 LLM 기반 에이전트는 임시방편적 프롬프트 방식에 의존하여 환각(hallucination)에 취약하며, **엄밀한 과학 실험 자동화는 거의 탐구되지 않았다.** 특히 가설 수립, 실험 설계, 통제된 시행, 결과 분석의 전 단계에서 신뢰성을 달성해야 한다는 요구사항이 충족되지 않는다.
- **Why**: 과학적 엄밀성은 단순한 문제 해결(problem-solving)을 넘어 반복적 가설 정제, 복잡한 실험 환경 구성, 강건한 결과 해석을 요구한다. 기존 방법들은 체계적 절차, 신뢰성, 해석가능성 원칙을 체계적으로 강제하지 않는다.
- **Approach**: 아키텍트 에이전트와 기술자 에이전트로 구성된 다중 에이전트 시스템 내에 **Experimental Rigor Engine**을 삽입하여, (1) 에이전트 내 신뢰성 강화, (2) 에이전트 간 방법론적 통제, (3) 실험 문서화를 통한 해석가능성 확보를 체계화한다.

## Achievement

![Figure 2](figures/fig2.webp)
*Figure 2. Case Study. Curie는 반복 샘플링의 이점에 관한 기존 연구를 검증, 확장, 비판할 수 있다.*

1. **성능 향상**: 컴퓨터 과학 도메인 46개 실험 질문에서 OpenHands, Microsoft Magentic 등 최강 베이스라인 대비 **3.4배 성능 개선** 달성

2. **포괄적 벤치마크 구성**: 영향력 있는 연구 논문 및 널리 채택된 오픈소스 프로젝트로부터 파생된 현실 기반의 실험 과제 46개 개발

3. **과학적 워크플로우 지원**: 기존 연구의 재현(reproduce), 확장(extend), 비판(challenge) 등 완전한 실험 라이프사이클 자동화 시연

## How

![Figure 3](figures/fig3.webp)
*Figure 3. Curie workflow with an example task in LLM reasoning. Architect는 고수준 계획 설계와 발견 사항 반영을 담당하고, Technician은 계획에 따른 실험 구현 및 실행을 담당한다.*

- **아키텍트 에이전트(Architect Agent)**: 고수준 실험 계획 수립 (가설 정의, 변수 식별), 발견 사항에 대한 반영(reflection) 수행
  
- **기술자 에이전트(Technician Agents)**: 아키텍트의 계획에 따라 통제된 실험 환경 구성 및 실행, 세부 작업 수행

![Figure 4](figures/fig4.webp)
*Figure 4. Intra-ARM setup validation high-level workflow.*

- **Intra-Agent Rigor Module (Intra-ARM)**: 각 에이전트의 신뢰성 강화
  - 실험 계획이 목표와 일치하는지 검증
  - 실험 환경 설정 재현성 확보
  - 변수 식별, 설계, 코드 검증의 엄밀성 보장
  - 중간 단계 검증을 통한 오류 격리 및 조기 수정 가능

- **Inter-Agent Rigor Module (Inter-ARM)**: 에이전트 간 방법론적 통제
  - 제어 흐름 정책(control flow policies)을 통한 정확한 작업 전이
  - 효율적 작업 스케줄링 및 순서 관리
  - 새로운 계획을 세분화된 파티션으로 분할하여 미세한 실행 제어

- **Experiment Knowledge Module**: 해석가능성 및 추적성 확보
  - 메타데이터 기반 구조화된 문서화
  - 실험 진행 상황 체계적 추적
  - 재현성 및 협업 촉진

![Figure 5](figures/fig5.webp)
*Figure 5. Errors detected by two of Intra-ARM's many validators.*

- **다층 검증 체계**: 설정 검증(setup validator), 실행 검증(execution validator) 등 여러 검증기를 통한 LLM 환각 방지

## Originality

- **체계적 엄밀성 주입**: 기존 임시방편적 프롬프트 기반 방식 대신, 세 가지 독립적 모듈(Intra-ARM, Inter-ARM, Experiment Knowledge)을 통해 신뢰성, 절차, 해석가능성을 **체계적으로 강제**하는 첫 시도

- **중간 단계 검증 패러다임**: 실험 종료 후 단일 검증이 아닌 **각 단계에서 지속적 검증**으로 오류 격리 및 효율적 수정 가능하게 설계

- **과학 실험 특화 벤치마크**: 논리 추론(logical reasoning)이나 일반 문제 해결과 구별되는 **반복적 가설 정제, 복잡한 환경 설정, 강건한 결과 해석을 요구하는 진정한 실험 과제** 개발

- **실제 과학 논문 기반 평가**: SWE-Bench 같은 코딩 대회 기반 과제가 아닌 **영향력 있는 연구 논문과 오픈소스 프로젝트에서 파생된 현실적 과제**로 평가

## Limitation & Further Study

- **도메인 제한**: 현재 컴퓨터 과학 도메인에만 적용되었으며, 생물학, 화학, 물리학 등 타 과학 분야로의 확장 가능성 미검증

- **LLM 의존성**: 기저 모델의 능력에 크게 의존하므로, 더 강력한 LLM 기반 에이전트 개발과 통합 필요

- **복잡 실험의 확장성**: 계산 비용 및 컨텍스트 길이 제약으로 인한 매우 장기간의 대규모 실험 자동화 한계

- **인간-에이전트 협업 모델**: 연구자의 도메인 전문 지식을 더 효과적으로 통합하고 피드백 루프를 강화하는 메커니즘 개발 필요

- **결과 검증 기준**: "정확한 실험 답"의 정의가 모호한 경우 대응 방안 개선


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4/5
- Significance: 4.5/5
- Clarity: 4/5
- Overall: 4.3/5

**총평**: Curie는 LLM 기반 과학 실험 자동화에서 **체계적 엄밀성 강제**라는 중요한 공백을 최초로 해결하며, 세 가지 모듈의 통합 설계와 현실 기반 벤치마크 구성으로 상당한 기술적 기여를 제시한다. 다만 도메인 확장성과 인간-AI 협업 메커니즘 고도화가 실제 과학 연구 적용의 열쇠가 될 것으로 보인다.

## Related Papers

- 🔄 다른 접근: [[papers/558_Moose-chem3_Toward_experiment-guided_hypothesis_ranking_via/review]] — 엄격한 과학 실험 자동화 vs 시뮬레이션 기반 접근의 대조적 방법론
