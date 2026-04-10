---
title: "774_STELLA_Towards_a_Biomedical_World_Model_with_Self-Evolving_M"
authors:
  - "Ruofan Jin"
  - "Zaixi Zhang"
  - "Mengdi Wang"
  - "Le Cong"
date: "2025"
doi: "10.1101/2025.07.01.662467"
arxiv: ""
score: 4.0
essence: "STELLA는 바이오의학 연구 질문에 자동으로 적응하고 경험으로부터 학습하는 자기진화형(self-evolving) AI 에이전트로, 동적 템플릿 라이브러리와 확장 가능한 도구 풀을 통해 기존의 정적 도구 집합이라는 한계를 극복한다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/Multi-Agent_Scientific_Frameworks"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Jin et al._2026_STELLA Towards a Biomedical World Model with Self-Evolving Multimodal Agents.pdf"
---

# STELLA: Towards a Biomedical World Model with Self-Evolving Multimodal Agents

> **저자**: Ruofan Jin, Zaixi Zhang, Mengdi Wang, Le Cong | **날짜**: 2025 | **DOI**: [10.1101/2025.07.01.662467](https://doi.org/10.1101/2025.07.01.662467)

---

## Essence

![Figure 1](figures/fig1.webp) *STELLA의 전체 프레임워크: 매니저 에이전트, 개발 에이전트, 비평 에이전트, 도구 생성 에이전트가 협력하며, 템플릿 라이브러리와 도구 오션이 자동으로 진화한다.*

STELLA는 바이오의학 연구 질문에 자동으로 적응하고 경험으로부터 학습하는 자기진화형(self-evolving) AI 에이전트로, 동적 템플릿 라이브러리와 확장 가능한 도구 풀을 통해 기존의 정적 도구 집합이라는 한계를 극복한다.

## Motivation

- **Known**: 현대 바이오의학 연구는 대량의 데이터, 도구, 문헌으로 인해 심각하게 단편화된 연구 환경에 직면하고 있으며, 기존 AI 에이전트들은 정적이고 수동으로 큐레이션된 도구 집합(static toolsets)에 의존한다.

- **Gap**: 기존 AI 에이전트는 새로운 도구를 자동으로 발견하고 통합할 수 없으며, 신속하게 진화하는 바이오의학 과학의 속도를 따라갈 수 없다. 또한 해결 경험으로부터 학습하거나 추론 전략을 개선할 수 없다.

- **Why**: 바이오의학 연구의 복잡성과 도구의 급속한 변화로 인해, 에이전트가 자동으로 지식을 축적하고 문제 해결 능력을 확장할 수 있는 자기진화 메커니즘이 필수적이다.

- **Approach**: 네 개의 협력하는 에이전트(Manager, Developer, Critic, Tool Creation Agent)와 두 가지 자기진화 메커니즘(진화하는 Template Library와 동적 Tool Ocean)을 기반으로 STELLA를 설계했다.

## Achievement

![Figure 2](figures/fig2.webp) *벤치마크 성과: (A) Humanity's Last Exam: Biomedicine, LAB-Bench: DBQA, LAB-Bench: LitQA에서 SOTA 달성. (B) 계산 예산 증가에 따른 정확도 향상 (자기진화 효과).*

1. **벤치마크 성능 SOTA 달성**: 
   - Humanity's Last Exam: Biomedicine에서 약 26% (기존 대비 최대 8pp 향상)
   - LAB-Bench: DBQA에서 54% 
   - LAB-Bench: LitQA에서 63%

2. **자기진화 검증**: 
   - HLE: Biomedicine 벤치마크에서 경험 증가에 따라 정확도가 14%에서 26%로 거의 두 배로 향상되어, 에이전트가 시간에 따라 더 우수한 과학자가 되어간다는 핵심 가설을 실증적으로 증명

3. **복합 바이오의학 문제 해결**: 
   - 화학요법 내성 메커니즘 규명 및 재감화 전략 제안과 같은 실제 연구 질문에 대해 실행 가능한 결과 도출

## How

### 아키텍처

- **Manager Agent**: 고수준의 연구 목표를 분석하여 논리적 단계로 분해하는 "Reasoning Pathway" 수립
- **Dev Agent**: Conda 환경 생성 및 파이썬 코드 실행을 통한 복잡한 생물정보학 분석 수행
- **Critic Agent**: 중간 결과를 엄격히 평가하고 actionable한 피드백 제공
- **Tool Creation Agent**: 기존 리소스(PubMed, GitHub) 검색 후 새로운 도구 구축, 테스트, 통합

### 자기진화 메커니즘

- **Template Library 진화**: 성공한 다단계 워크플로우를 고품질 reasoning template으로 증류(distillation)하여 라이브러리에 저장, 향후 유사 문제 해결 효율성 향상

- **Tool Ocean 확장**: 세 가지 범주의 도구로 구성
  - 과학 데이터베이스 쿼리 (PubMed, ClinVar, PDB)
  - 기초 모델 활용 인터페이스 (AlphaFold 3, scGPT, ESM3)
  - 커스텀 분석 도구 (네트워크 분석, 데이터 통합 스크립트)

- **Feedback Loop**: 인간 전문가 및 습식 실험(wet experiment) 결과를 피드백으로 받아 지속적 개선

## Originality

- **자기진화 메커니즘의 이중 구조**: Template Library와 Tool Ocean을 동시에 발전시키는 통합된 설계는 기존 정적 에이전트와의 근본적 차별점

- **Tool Creation Agent의 자율적 도구 생성**: LLM 에이전트가 수동 큐레이션 없이 새로운 생물정보학 도구를 자동으로 발견하고 테스트할 수 있는 능력

- **Multi-agent Orchestration**: 네 가지 특화된 에이전트 간의 조율을 통한 robust iterative problem-solving loop 구축

- **경험학습 검증**: 벤치마크 결과가 정량적으로 자기진화 메커니즘이 작동함을 증명한 최초의 바이오의학 AI 에이전트

## Limitation & Further Study

- **낮은 절대 성능**: HLE: Biomedicine에서 26% 정확도는 여전히 상당히 낮으며, 실제 임상 응용 가능성에 의문 제기

- **벤치마크 제한성**: 평가가 객관식 또는 구조화된 벤치마크에 한정되어, 실제 바이오의학 연구의 복잡성 전체를 반영하지 못할 가능성

- **Tool Creation 메커니즘의 상세 부족**: 도구 자동 생성의 성공률, 생성된 도구의 품질 평가, 오류 도구의 감지 및 제거 메커니즘에 대한 명확한 분석 부재

- **확장성 검증 미흡**: 더 대규모의 Tool Ocean과 Template Library에서의 성능 유지 가능성과 계산 복잡도 증가 분석 필요

- **향후 연구 방향**:
  - 더 복잡한 multimodal 바이오의학 데이터(이미지, 구조, 시퀀스) 통합
  - 실제 습식 실험과의 폐쇄 루프(closed-loop) 자동화
  - 인간 전문가-AI 협력의 최적화
  - 도구 검색 및 생성의 효율성 개선


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: STELLA는 바이오의학 AI 에이전트의 자기진화 메커니즘이라는 혁신적 개념을 제시하고 이를 실증적으로 증명한 의미 있는 연구이나, 절대 성능의 낮음과 기술 상세의 부족으로 인해 실제 바이오의학 연구 현장에서의 즉각적 적용 가능성은 제한적이며, 추가적인 검증과 개선이 필요하다.

## Related Papers

- 🔗 후속 연구: [[papers/239_CRISPR-GPT_for_agentic_automation_of_gene-editing_experiment/review]] — STELLA의 자기진화형 바이오의학 에이전트는 CRISPR-GPT의 정적 도구 집합 한계를 극복하는 발전된 형태다.
- 🔄 다른 접근: [[papers/168_Biomni_A_General-Purpose_Biomedical_AI_Agent/review]] — STELLA와 Biomni 모두 범용 바이오의학 AI 에이전트를 추구하지만 자기진화형 vs 사전 훈련된 접근방식을 사용한다.
- 🏛 기반 연구: [[papers/344_Foundation_models_in_bioinformatics/review]] — 바이오인포매틱스의 기초 모델 연구는 STELLA의 자기진화형 바이오의학 월드 모델 개발에 이론적 토대를 제공한다.
- 🔗 후속 연구: [[papers/311_Empowering_Biomedical_Discovery_with_AI_Agents/review]] — 생의학 AI 에이전트를 자기진화형 세계 모델로 발전시킨 차세대 시스템
- 🔄 다른 접근: [[papers/612_PersonaAI_An_Interactive_Agentic-AI_Framework_for_Autonomous/review]] — 노화 연구 자동화에서 인터랙티브 에이전틱 AI와 자기진화 생의학 월드 모델 접근법을 비교할 수 있습니다.
- 🔗 후속 연구: [[papers/239_CRISPR-GPT_for_agentic_automation_of_gene-editing_experiment/review]] — STELLA의 자기진화형 바이오의학 에이전트는 CRISPR-GPT의 정적 도구 집합 한계를 극복하는 발전된 형태다.
