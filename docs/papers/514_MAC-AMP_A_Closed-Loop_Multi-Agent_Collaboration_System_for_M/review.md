---
title: "514_MAC-AMP_A_Closed-Loop_Multi-Agent_Collaboration_System_for_M"
authors:
  - "Gen Zhou"
  - "Sugitha Janarthanan"
  - "Lianghong Chen"
  - "Pingzhao Hu"
date: "2026.02"
doi: "미제공"
arxiv: ""
score: 4.2
essence: "항생제 내성(Antimicrobial Resistance, AMR)에 대응하기 위해 대규모언어모델(LLM) 기반 다중 에이전트 협업 시스템을 활용하여 항균펩타이드(AMP)를 설계하는 완전 자동화된 폐루프(closed-loop) 시스템을 제시한다. 기존 AMP 설계 모델들의 단순 점수화 및 블랙박스 문제를 극복하기 위해 에이전트 간 협의적 리뷰, 강화학습 기반 보상 함수 자동 생성, 설명가능성을 갖춘 구조를 도입했다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/Multi-agent_Task_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Zhou et al._2026_MAC-AMP A Closed-Loop Multi-Agent Collaboration System for Multi-Objective Antimicrobial Peptide De.pdf"
---

# MAC-AMP: A Closed-Loop Multi-Agent Collaboration System for Multi-Objective Antimicrobial Peptide Design

> **저자**: Gen Zhou, Sugitha Janarthanan, Lianghong Chen, Pingzhao Hu | **날짜**: 2026-02-16 | **DOI**: 미제공

---

## Essence

항생제 내성(Antimicrobial Resistance, AMR)에 대응하기 위해 대규모언어모델(LLM) 기반 다중 에이전트 협업 시스템을 활용하여 항균펩타이드(AMP)를 설계하는 완전 자동화된 폐루프(closed-loop) 시스템을 제시한다. 기존 AMP 설계 모델들의 단순 점수화 및 블랙박스 문제를 극복하기 위해 에이전트 간 협의적 리뷰, 강화학습 기반 보상 함수 자동 생성, 설명가능성을 갖춘 구조를 도입했다.

## Motivation

- **Known**: 최근 AI 기반 AMP 발견 및 설계가 진전되고 있으며, GAN 기반(AMPGAN v2), 확산 모델(Diff-AMP), 기초모델(AMP Designer) 등이 개발되었다. LLM 기반 다중 에이전트 시스템도 단백질 설계, 물질 화학 등에서 성공 사례를 보이고 있다.

- **Gap**: (1) 기존 AMP 설계 모델은 주로 항균 활성만 최적화하며, 다중 목표 최적화 시 정적 가중치(static weighting)로 인한 보상 해킹(reward hacking) 또는 다양성 붕괴 문제 발생 (2) 현재 LLM 기반 MAC 시스템들은 자연언어 또는 이질적 점수를 출력하여 강화학습에 사용 가능한 명확한 신호 부재 (3) 대부분의 MAC 시스템이 개방 루프(open-loop) 방식으로 인간 개입이 필요함

- **Why**: 항생제 내성으로 인해 2021년 약 114만 명 사망, 2025-2050년 3,900만 명 이상의 직접 사망이 예상되므로, 다중 목표(활성, 안전성, 안정성, 신규성)를 동시에 최적화하는 자동화 시스템이 필수적이다.

- **Approach**: 폐루프 다중 에이전트 협업 시스템을 구축하여 (1) 속성 예측 모듈, (2) AI 시뮬레이션 피어 리뷰 모듈, (3) 강화학습 정제 모듈, (4) 펩타이드 생성 모듈을 통해 평가 결과를 기계 실행 가능한 보상 함수로 변환하고, 반복적 최적화를 수행한다.

## Achievement

![Figure 1: MAC-AMP 프레임워크](figures/fig1.webp)
*Figure 1: (a) 입력에서 출력까지 반복적으로 AMP 설계를 안내하는 폐루프 워크플로우 개요 (b) 모듈 간 상호작용을 보여주는 MAC-AMP 파이프라인 개요*

1. **다중 목표 최적화 성과**: 항균 활성(antibacterial activity), AMP 유사성(AMP-likeness), 독성 규정 준수(toxicity compliance), 구조적 신뢰성(structural reliability)에서 기존 생성 모델 대비 우수한 성과 달성. 정적 가중치 대신 에이전트 합의 기반의 다중 목표 조정으로 안정적 최적화 실현.

2. **설명가능성과 감시 가능성**: 투명한 로그, 재생 추적(replay traces), 합의 인식 의사결정 추적을 통해 에이전트 전역의 단계별 설명가능성 제공. 블랙박스 AI 모델의 한계 극복.

3. **완전 자동화 폐루프 시스템**: 사용자로부터 표적 박테리아명과 예시 데이터셋(MIC 값 포함)만 입력받아 평가, 합의 형성, 보상 함수 생성, 설계를 자동으로 반복 수행.

4. **도메인 전이 가능성**: AMP 설계 특화 구조를 유지하면서도 다른 분자 설계 문제로의 일반화 가능성 제시.

## How

![Figure 2: AI 시뮬레이션 피어 리뷰 모듈](figures/fig2.webp)
*Figure 2: 인공지능 시뮬레이션 피어 리뷰 모듈 개요*

![Figure 3: 강화학습 정제 모듈](figures/fig3.webp)
*Figure 3: 강화학습 정제 모듈 개요*

### 속성 예측 모듈 (Property Prediction Module)
- **항균 활성**: ProtBERT 기반 LLM 회귀모델을 입력 데이터셋으로 전이학습하여 표적 특화 MIC 예측기 개발 (8:1:1 train:validation:test)
- **추가 속성**: Macrel 1.5 (AMP 유사성), ToxinPred 3.0 (독성), OmegaFold v1 (구조 신뢰성), ProtParam (물리화학적 특성), Foldseek (템플릿 유사성)
- **결과 분류**: 명시적 보상 신호(S: 항균 활성 + AMP 유사성) vs 보조 증거(V: 독성, 구조 신뢰성, 물리화학, 템플릿 유사성). 에이전트별 접근 권한 차등화.

### AI 시뮬레이션 피어 리뷰 모듈
- 학술 피어 리뷰의 위원회식 숙의 방식을 모방한 다중 역할 에이전트 설계
- 개별 에이전트: Evaluator (S 기반 개별 평가), Predictor (V 기반 보조 증거 종합), Unifier (상충하는 목표 간 합의 형성)
- 자연언어 출력을 구조화된 수치 합의로 변환하여 강화학습 입력 신호로 활용 가능

### 강화학습 정제 모듈 (RL Refinement Module)
- 에이전트 합의를 실행 가능한 보상 코드(Python 함수)로 자동 변환
- 동적 가중치 조정: 훈련 중 상충하는 목표 간 보상 밸런스 자동 재계산
- Eureka 스타일 접근법으로 LLM이 보상 함수를 자동 생성하고 개선

### 펩타이드 생성 모듈
- LLM 기반 순차 생성기로, 강화학습 정제 모듈에서 생성된 보상 함수를 훈련 신호로 수용
- 폐루프: 생성된 펩타이드 → 속성 예측 → 피어 리뷰 → 보상 생성 → 다음 세대 생성

### 검증 방법
- 모듈별 절제 연구(Ablation studies)로 각 속성 예측 도구의 필요성 확인
- 대체 분석(Substitution analyses)으로 ToxinPred 3.0과 MIC 예측기 검증
- 분자동역학(MD) 시뮬레이션으로 OmegaFold를 구조 신뢰성 대리지표로 사용 타당성 확인

## Originality

- **폐루프 다중 에이전트 시스템의 최초 구현**: 기존 MAC 시스템이 개방 루프 방식이었던 것과 달리, 평가→협의→보상 생성→최적화를 자동으로 반복하는 완전 폐루프 구조 제시

- **에이전트 합의 기반 다중 목표 최적화**: 정적 가중치나 수동 임계값 대신 협의 기반의 구조화된 합의로 상충하는 생물학적 제약 간 동적 조정 실현

- **자동 보상 함수 생성**: Eureka의 코드 생성 기법을 처음 다중 에이전트 시스템에 통합하여 자연언어 평가를 기계 실행 가능한 신호로 변환

- **투명한 감시 가능성(Auditability)**: 에이전트 간 상호작용 로그, 의사결정 추적, 재생 기능으로 "검은 상자" 비판 극복 및 오류 국소화(localization) 가능

- **도메인 불가지론적 설계**: AMP 특화 모듈을 유지하면서도 속성 예측 도구 교체로 다른 분자 설계 분야 적용 가능성 설계

## Limitation & Further Study

- **계산 비용**: 다중 에이전트 협업, LLM 추론, 강화학습 반복으로 인한 높은 계산 비용에 대한 분석 부재. 대규모 실험 시 확장성(scalability) 의문

- **생체 외(In vitro) 검증 부재**: 논문에서는 계산 기반 평가만 수행되었으며, 실제 생물학적 실험(항균성 시험, 독성 측정, 안정성 검증)에 대한 검증 데이터 제시 부족

- **LLM 의존성**: 시스템의 성능이 기반 LLM의 질에 크게 의존. 모델 업데이트 시 영향 범위 및 재훈련 필요성 미명시

- **속성 예측 도구의 정확도**: 기존 도구(ToxinPred, OmegaFold 등)에 의존하므로, 이들의 오류가 누적될 수 있는 리스크

- **후속 연구**: (1) 생체 외 및 생체 내 검증 실험 수행 (2) 계산 비용 최적화 및 엣지 컴퓨팅(edge computing) 적용 (3) 다양한 박테리아/진균에 대한 적응성 평가 (4) 다른 분자 설계 영역(단백질, 소분자) 적용 검증

## Evaluation

- **Novelty (독창성): 4.5/5**
  - 폐루프 MAC 시스템의 최초 구현 및 에이전트 합의 기반 다중 목표 최적화는 신규성 높음
  - LLM 기반 자동 보상 함수 생성을 MAC에 통합한 점 우수
  - 다만 개별 기술(에이전트 협업, 강화학습, 보상 설계)은 기존 연구에서 개별 적용된 바 있음

- **Technical Soundness (기술적 타당성): 4/5**
  - 모듈별 설계가 논리적이며, 절제 연구와 대체 분석으로 각 요소의 필요성 입증
  - MD 시뮬레이션을 통한 구조 신뢰성 검증 수행
  - 다만 생체 외 검증 부재로 계산 예측과 실제 성능의 괴리 가능성 미해결

- **Significance (중요성): 4.5/5**
  - 항생제 내성은 전 지구적 보건 위협이며, 본 연구는 실질적 영향력 있는 문제 해결 시도
  - 다중 목표 최적화로 실용적인 AMP 설계 가능성 높임
  - 도메인 전이 가능성으로 다른 분자 설계 분야 영향 예상
  - 다만 현재 생물학적 검증 부재로 임상 영향력 미확인

- **Clarity (명확성): 4/5**
  - 프레임워크 구조(4개 모듈)가 체계적이고 명확함
  - Figure 1-3이 전체 워크플로우를 잘 시각화
  - 다만 일부 기술 상세(예: 에이전트 프롬프트 설계, 하이퍼파라미터)가 부록에 많이 분산되어 본문 가독성 다소 감소

- **Overall: 4.2/5**

**총평**: MAC-AMP는 다중 에이전트 협업을 AMP 설계에 성공적으로 적용한 혁신적 연구로, 폐루프 구조와 설명가능성이라는 핵심 장점을 제시한다. 계산 기반 평가에서 기존 모델을 능가했으나, 생체 외 검증과 계산

## Related Papers

- 🔄 다른 접근: [[papers/554_Modular_large_language_model_agents_for_multi-task_computati/review]] — MAC-AMP의 항균펩타이드 특화 다중 에이전트와 PharmAgents의 포괄적 신약 개발 시스템은 서로 다른 범위에서 약물 설계를 자동화하는 접근이다.
- 🔗 후속 연구: [[papers/805_The_Virtual_Lab_of_AI_agents_designs_new_SARS-CoV-2_nanobodi/review]] — Virtual Lab의 나노바디 설계 성공이 MAC-AMP의 항균펩타이드 설계를 위한 다중 에이전트 협업 방법론의 효과를 다른 단백질 영역에서 확장 검증한다.
- 🏛 기반 연구: [[papers/177_Can_ai_agents_design_and_implement_drug_discovery_pipelines/review]] — AI 에이전트의 약물 발견 파이프라인 설계 능력이 MAC-AMP의 폐루프 항균펩타이드 개발 시스템 구축의 기본적인 기술적 토대이다.
- 🔄 다른 접근: [[papers/554_Modular_large_language_model_agents_for_multi-task_computati/review]] — PharmAgents의 포괄적 신약 개발과 MAC-AMP의 항균펩타이드 특화 시스템은 서로 다른 범위에서 약물 개발을 자동화하는 접근이다.
