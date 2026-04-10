---
title: "692_Safescientist_Toward_risk-aware_scientific_discoveries_by_ll"
authors:
  - "Kunlun Zhu"
  - "Jiaxun Zhang"
  - "Ziheng Qi"
  - "Ning Shang"
  - "Zijia Liu"
date: "2025"
doi: "arXiv:2505.23559"
arxiv: ""
score: 4.25
essence: "본 논문은 LLM 기반 AI 과학자 에이전트의 자동화된 과학 발견 과정에서 발생하는 윤리적, 안전 문제를 체계적으로 해결하기 위해 SafeScientist 프레임워크를 제안한다. 이는 다층 방어 메커니즘(prompt monitoring, agent collaboration monitoring, tool-use monitoring, ethical reviewer)을 통합하여 과학 연구 파이프라인 전반에 걸쳐 안전성을 보장한다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/Autonomous_Hypothesis_Discovery"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Zhu et al._2025_Safescientist Toward risk-aware scientific discoveries by llm agents.pdf"
---

# SafeScientist: Toward Risk-Aware Scientific Discoveries by LLM Agents

> **저자**: Kunlun Zhu, Jiaxun Zhang, Ziheng Qi, Ning Shang, Zijia Liu, Pengfei Han, Yue Su, Haofei Yu, Jiaxuan You | **날짜**: 2025 | **DOI**: [arXiv:2505.23559](https://arxiv.org/abs/2505.23559)

---

## Essence

![Figure 1](figures/fig1.webp)
*SafeScientist는 악의적이거나 위험한 프롬프트에 대해 거절 응답을 제시하며, 일반 AI 과학자 프레임워크와 달리 위험 인식(Risk-Awareness)을 통해 안전하게 고위험 주제를 다룬다.*

본 논문은 LLM 기반 AI 과학자 에이전트의 자동화된 과학 발견 과정에서 발생하는 윤리적, 안전 문제를 체계적으로 해결하기 위해 SafeScientist 프레임워크를 제안한다. 이는 다층 방어 메커니즘(prompt monitoring, agent collaboration monitoring, tool-use monitoring, ethical reviewer)을 통합하여 과학 연구 파이프라인 전반에 걸쳐 안전성을 보장한다.

## Motivation

- **Known**: 최근 GPT-o3, Gemini-2.5-Pro 등 강력한 LLM들이 가설 생성, 실험 설계, 데이터 분석, 논문 작성 등 과학 연구의 자동화를 가능하게 함. 기존 LLM 안전 연구는 단일 모델의 대적 공격(adversarial attack), 데이터 편향(pretraining bias), 안전 파인튜닝 등 고립된 측면에만 집중.

- **Gap**: 다중 에이전트 환경에서 복잡한 상호작용으로 인한 신흥 위험(emergent risks)과 과학 연구 맥락의 고유한 안전 요구사항이 간과됨. 과학 AI 커뮤니티를 위한 포괄적 평가 벤치마크와 방어 프레임워크 부재.

- **Why**: AI 과학자의 도구 사용(tool-use), 에이전트 간 협력(agent collaboration), 논문 생성 등 각 단계에서 악용 가능성, 해로운 편향 증폭, 위험 지식 전파 등의 위험 존재.

- **Approach**: 과학 맥락의 안전을 명시적으로 설계한 SafeScientist 프레임워크와 240개의 고위험 과학 발견 과제 + 120개의 도구 관련 위험 시나리오로 구성된 SciSafetyBench 벤치마크 도입.

## Achievement

![Figure 2](figures/fig2.webp)
*SafeScientist의 엔드-투-엔드 파이프라인: 입력 감지(Prompt Monitor), 다중 에이전트 토론(Discussion Stage), 도구 사용(Tool Use Stage), 논문 작성(Writing Stage)을 거쳐 SciSafetyBench 기반 공격/방어 평가를 통합.*

1. **SafeScientist 프레임워크**: 기존 AI Scientist/Tiny Scientist 등의 경량 프레임워크에 4가지 방어 메커니즘(Prompt Monitor, Agent Collaboration Monitor, Tool-Use Monitor, Paper Ethic Reviewer)을 통합하여 과학 연구 파이프라인 전반의 안전 감독을 실현. 기존 AI 과학자 프레임워크 대비 안전 성능 34.69% 향상.

2. **SciSafetyBench 벤치마크**: 6개 과학 도메인(물리학, 화학, 생물학, 재료과학, 컴퓨터과학, 의학)에 걸친 240개 고위험 과학 발견 과제와 30개 과학 도구 + 120개 도구별 위험 시나리오로 구성. 다양한 대적 공격(Base64, DAN, Inception 등)에 대한 강건성 검증 완료.

## How

![Figure 2](figures/fig2.webp)

**방어 메커니즘 (Defense Methods)**:

- **Prompt Monitor**: 
  - LLaMA-Guard-3-8B로 프롬프트의 의미적 의도와 위험도 평가 (안전 레이블 + 설명)
  - SafeChecker로 구조적 분석 수행: 17개 위험 카테고리 평가, jailbreak/roleplay 패턴 탐지
  - 3단계 분류: pass/warning/reject (warning은 위험하지만 탐색할 가치 있는 연구)
  - 두 모듈 중 하나라도 reject 플래그 → 프롬프트 거절, 모호한 경우 경량 폴백 메커니즘 적용

- **Agent Collaboration Monitor**: 
  - 다중 에이전트 상호작용 단계에서 윤리/안전 중심 모니터 에이전트 배치
  - 논의 과정 지속 감시, 악의적 에이전트 영향에 대한 윤리적 개입 제공
  - Round별 피드백 메커니즘으로 악의적 아이디어 제거

- **Tool-Use Monitor**: 
  - 도구 사용 단계에서 실행 전 도구 응답/결과 검증
  - 도구별 위험 시나리오에 대한 방어 로직 적용

- **Paper Ethic Reviewer**: 
  - 최종 논문 작성 단계에서 윤리 검토 수행
  - 논문의 안전성, 책임감, 도덕성 평가

**연구 파이프라인**:
1. 사용자 명령 입력 → Prompt Monitor에서 안전성 검사
2. 도메인/과제 유형 분석 → 전문 에이전트 그룹 동적 활성화
3. 다중 에이전트 협력 토론 (Agent Collaboration Monitor 감시)
4. 과학 도구/검색 모듈 호출 (Tool-Use Monitor로 결과 검증)
5. 쓰기/정제 모듈 → Paper Ethic Reviewer로 최종 검증

## Originality

- **첫 종합적 과학 AI 안전 프레임워크**: 단일 모델 안전이 아닌 end-to-end 과학 연구 파이프라인의 다층 안전 설계를 처음 제시. 기존 AI Scientist 프레임워크들과 달리 input detection + agent defense + tool defense를 모두 통합 (Table 1 참조).

- **과학 맥락 특화 벤치마크**: 일반적인 LLM 안전 벤치마크(HarmBench, ToxiGen 등)와 달리 6개 과학 도메인의 실제 고위험 과제 240개와 도구별 위험 시나리오 120개를 포함하는 SciSafetyBench는 과학 연구 고유의 위험을 반영.

- **다양한 공격 방법 통합 검증**: Base64, DAN (Do Anything Now), Inception 등 다양한 대적 공격 기법으로 안전 파이프라인의 강건성을 체계적으로 검증.

- **경량성과 실용성**: 기존 프레임워크의 구조를 유지하면서 플러그인 방식으로 안전 메커니즘을 추가하여 구현의 경량성과 적용 용이성 확보.

## Limitation & Further Study

- **도메인 제한**: 6개 과학 도메인에 국한되어 있으며, 공학(Engineering), 환경과학 등 추가 도메인으로의 확장 필요.

- **현실적 검증 부족**: 벤치마크가 시뮬레이션 환경 중심이므로, 실제 연구실 환경(wet lab)에서의 안전성 평가는 미흡. 특히 화학·생물 실험의 실제 위험도를 완전히 반영하기 어려움.

- **거짓 양성 비율**: Prompt Monitor와 Tool-Use Monitor의 거짓 양성(false positive)으로 인한 정상 연구 아이디어 거절 가능성. 이와 안전성 간의 균형 조정 필요.

- **에이전트 협력 모니터의 한계**: 악의적 에이전트의 정교한 위장(sophisticated evasion) 기법에 대한 방어 효과가 불명확. 향후 보다 정교한 탐지 알고리즘 개발 필요.

- **확장성**: 더 강력한 LLM(GPT-o3, Gemini-3)에 대한 대적 공격 방법과 방어 메커니즘의 진화 필요. Safety fine-tuning 등 내재적 안전 강화 기법의 통합 가능성 탐색.

## Evaluation

- **Novelty (독창성)**: 4/5 - 과학 AI 안전의 first comprehensive framework이며 domain-specific 벤치마크는 신규이나, 개별 방어 기법들(LLaMA-Guard, ethical review 등)은 기존 방법들의 조합.

- **Technical Soundness (기술 타당성)**: 4/5 - 다층 방어 메커니즘의 설계와 파이프라인 통합은 합리적이나, Agent Collaboration Monitor의 정교한 악의 탐지 능력과 Tool-Use Monitor의 구체적 구현 세부사항이 다소 모호함.

- **Significance (의의)**: 5/5 - AI 과학자의 실제 배포 전 안전성 보장이 중요한 시점에서 체계적이고 실용적인 프레임워크 제시. 향후 과학 AI 연구의 표준으로 역할할 가능성 높음.

- **Clarity (명확성)**: 4/5 - 전반적 논문 구조와 방법론은 명확하나, 각 방어 메커니즘의 상세 알고리즘(특히 SafeChecker의 17개 위험 카테고리 정의)과 실험 세부사항(특정 평가 메트릭 정의)에서 개선 필요.

- **Overall (종합)**: 4.25/5

**총평**: SafeScientist는 LLM 기반 AI 과학자의 윤리적, 안전한 배포를 위한 시의적절하고 포괄적인 프레임워크를 제시하며, SciSafetyBench는 과학 맥락의 고유한 위험을 체계적으로 평가할 수 있는 귀중한 자산이다. 다만, 실제 과학 환경에서의 거짓 양성 비율 감소와 더욱 정교한 대적 공격에 대한 방어 강화는 향후 과제이다.

## Related Papers

- 🔗 후속 연구: [[papers/680_Reviewing_scientific_papers_for_critical_problems_with_reaso/review]] — 안전한 과학적 발견을 위한 위험 인식 시스템으로 확장하여 오류 검출을 넘어 예방적 안전 조치까지 포함한다.
