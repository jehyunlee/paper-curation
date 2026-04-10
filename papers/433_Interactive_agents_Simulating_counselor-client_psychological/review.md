---
title: "433_Interactive_agents_Simulating_counselor-client_psychological"
authors:
  - "Huachuan Qiu"
  - "Zhenzhong Lan"
date: "2024"
doi: "논문"
arxiv: ""
score: 4.0
essence: "본 논문은 두 개의 대규모 언어모델(LLM)을 상담사와 내담자 역할로 활용하여 심리 상담 대화를 자동으로 생성하는 프레임워크를 제안한다. 인간 주석의 비용과 개인정보 문제를 해결하면서도 고품질의 합성 상담 데이터를 대규모로 생성할 수 있다는 점이 핵심이다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/Multi-Agent_Language_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Qiu and Lan_2024_Interactive agents Simulating counselor-client psychological counseling via role-playing llm-to-llm.pdf"
---

# Interactive agents: Simulating counselor-client psychological counseling via role-playing llm-to-llm interactions

> **저자**: Huachuan Qiu, Zhenzhong Lan | **날짜**: 2024 | **DOI**: [논문 링크 미제공](https://arxiv.org/abs/2408.15787)

---

## Essence

![Figure 1](figures/fig1.webp)
*그림 1: 시뮬레이션 프레임워크의 전체 아키텍처. 좌측: 클라이언트 풀 구성, 중앙: 대화형 시뮬레이션을 통한 데이터 수집, 우측: 모델 훈련*

본 논문은 두 개의 대규모 언어모델(LLM)을 상담사와 내담자 역할로 활용하여 심리 상담 대화를 자동으로 생성하는 프레임워크를 제안한다. 인간 주석의 비용과 개인정보 문제를 해결하면서도 고품질의 합성 상담 데이터를 대규모로 생성할 수 있다는 점이 핵심이다.

## Motivation

- **Known**: 기존 심리 상담 대화 시스템은 전문 상담사와 내담자 간의 실제 대화를 통해 데이터를 수집하고 있으며, 일부 연구는 장문의 단일 턴 상담 텍스트를 다중 턴 대화로 변환하려고 시도하고 있다.

- **Gap**: 
  1. 대규모 상담 대화 수집은 시간이 오래 걸리고, 비용이 많이 들며, 개인정보 보호가 필요하고, 확장성이 낮다
  2. 기존 데이터 변환 접근법은 상담사가 처음부터 내담자의 모든 문제를 알고 있다는 비현실적 가정을 하므로, 실제 상담의 점진적 탐색 과정을 반영하지 못한다

- **Why**: 상담사가 특정 경험이 부족한 문제(예: 연애 경험 없는 상담사는 연애 문제를 덜 효과적으로 다룸)를 해결하고, 실시간 상호작용(back-and-forth interaction)이 있는 자연스러운 상담 시뮬레이션이 필요하다.

- **Approach**: GPT-4를 이용한 제로샷 프롬프팅으로 LLM 기반 내담자와 상담사를 동시에 구현하여 역할 극화(role-playing)하는 LLM-to-LLM 상호작용 프레임워크를 제안한다.

## Achievement

![Figure 2](figures/fig2.webp)
*그림 2: 내담자 시뮬레이션을 위한 프롬프트. 사용자 프로필에 기반한 대화형 요구사항*

![Figure 3](figures/fig3.webp)
*그림 3: 상담사 시뮬레이션을 위한 프롬프트. 통합 치료 기법 기반 3단계 모델*

1. **SimPsyDial 데이터셋 구축**: 1,000개의 실제 사용자 포스팅을 기반으로 LLM이 생성한 고품질 합성 상담 데이터셋 개발. 제로샷 프롬프팅만으로 전문적 수준의 상담 대화 자동 생성 가능

2. **포괄적 평가 프레임워크 제안**: 
   - 내담자 평가: 역할 충실성(role fidelity) 및 집단 다양성 측정
   - 상담사 평가: Working Alliance Inventory (WAI-O-S)를 활용한 대화 품질 평가
   - 실제 vs 생성 대화 비교 분석으로 LLM 생성 데이터의 신뢰성 검증

3. **최첨단 성능 달성**: 합성 데이터로 미세조정한 7B 파라미터 오픈소스 모델이 기존 최첨단 모델은 물론, 실제 상담 대화로 훈련한 모델까지도 초과하는 성능 달성

## How

![Figure 4](figures/fig4.webp)
*그림 4: 내담자 시뮬레이션의 일관성*

![Figure 5](figures/fig5.webp)
*그림 5: 실제 상담 데이터(RealPsyDial)와 생성 데이터(SimPsyDial) 간의 주제 분포 비교*

**방법론의 주요 구성요소:**

- **클라이언트 풀 구성**: 공개 온라인 심리 플랫폼(PsyQA)에서 수집한 300자 이상의 장문 게시물 1,000개를 사용자 프로필로 활용

- **내담자 시뮬레이션**: 
  - 제공된 사용자 프로필을 기반으로 실제 내담자의 대화 스타일, 표정, 감정을 모방
  - 문제를 단계적으로 설명하도록 유도
  - 턴당 1-2 문장으로 제한하여 자연스러운 대화 유지

- **상담사 시뮬레이션**:
  - 통합 치료(integrative therapy) 기반 3단계 모델 적용
  - 탐색(exploration) → 통찰(insight) → 행동(action) 단계 진행
  - 최대 50턴 또는 상담사가 정의한 종료 토큰 출력까지 진행

- **대화 생성 및 평가**:
  - 내담자가 "안녕하세요"로 시작하는 자연스러운 초기화
  - 실시간 상호작용 방식으로 각 턴마다 상담사 응답 생성
  - WAI-O-S 지표로 작업 동맹(working alliance) 품질 평가

- **모델 훈련**: Llama-2 7B 및 기타 오픈소스 LLM을 합성 데이터로 미세조정하여 대화 시스템 개발

## Originality

- **혁신적 프레임워크**: LLM-to-LLM 상호작용을 통한 자동 심리 상담 대화 생성이라는 새로운 접근법. 기존 데이터 변환 방식과 달리 동적 탐색 과정을 시뮬레이션

- **실제 상담 시뮬레이션**: 상담사가 처음부터 모든 정보를 알고 있는 비현실적 가정을 벗어나, 점진적 탐색을 통한 자연스러운 상담 프로세스 재현

- **통합 치료 기반 설계**: 심리 치료의 "도도새 판결(dodo bird verdict)" 원리를 바탕으로 다양한 치료 기법을 통합하는 3단계 모델 개발

- **포괄적 평가 방법론**: 내담자-상담사 양측 평가, 실제 vs 생성 데이터 비교, 다운스트림 태스크 성능 검증 등 다층적 평가

- **대규모 합성 데이터셋**: SimPsyDial 데이터셋의 공개를 통해 심리 상담 AI 커뮤니티 기여

## Limitation & Further Study

- **제한사항**:
  1. GPT-4만 사용하여 다른 LLM의 성능 비교 부재. 오픈소스 모델의 역할 극화 능력이 더 제한적일 가능성
  2. 최대 50턴으로 제한되어 있어 장기 상담 세션의 특성을 완전히 반영하지 못함
  3. 중국어 데이터 기반이므로 다국어 일반화 가능성이 미확인
  4. 내담자 프로필이 고정되어 있어 상담 과정 중 동적 변화(내담자의 태도/인식 변화) 제한적
  5. 결과 평가가 제한된 규모의 인간 평가에 의존

- **후속 연구 방향**:
  1. 다양한 LLM(Claude, Llama 등)을 활용한 비교 연구
  2. 더 장기간의 상담 시뮬레이션 및 추적(follow-up) 세션 포함
  3. 실제 상담사와 LLM 기반 상담사의 직접 비교 연구
  4. 내담자 상태의 동적 진화를 반영한 향상된 프롬프팅
  5. 다국어 및 문화별 상담 패턴 적응
  6. 윤리적 고려사항(정신 건강 위기 상황 처리) 연구


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 논문은 LLM 기반 역할 극화를 통한 심리 상담 대화 자동 생성이라는 창의적이고 실용적인 접근법을 제시하며, 포괄적인 평가 방법론으로 신뢰성을 입증한다. 특히 합성 데이터로 훈련한 모델이 실제 상담 데이터 모델을 초과하는 성능을 달성한 점은 주목할 만하다. 다만 단일 LLM(GPT-4) 사용, 중국어 데이터 기반, 개인정보 보호 및 윤리적 고려에 대한 깊이 있는 논의 부재가 아쉬우며, 향후 다양한 LLM과 문화권에서의 검증이 필요하다.

## Related Papers

- 🔄 다른 접근: [[papers/606_Patientsim_A_persona-driven_simulator_for_realistic_doctor-p/review]] — Interactive agents와 PATIENTSIM 모두 의료 상담 시뮬레이션을 다루지만 상담사-내담자 vs 의사-환자 관계에 초점을 둔다.
- 🔗 후속 연구: [[papers/058_Agent_hospital_A_simulacrum_of_hospital_with_evolvable_medic/review]] — Agent hospital의 진화하는 의료진 시뮬레이션은 심리 상담 에이전트의 상호작용을 복잡한 병원 환경으로 확장한다.
- 🧪 응용 사례: [[papers/821_Towards_a_client-centered_assessment_of_llm_therapists_by_cl/review]] — 클라이언트 중심 LLM 치료사 평가 연구는 심리 상담 대화 생성 프레임워크의 실제 치료 효과성을 검증한다.
- 🔄 다른 접근: [[papers/606_Patientsim_A_persona-driven_simulator_for_realistic_doctor-p/review]] — PATIENTSIM과 Interactive agents 모두 의료 상담 시뮬레이션을 다루지만 의사-환자 vs 상담사-내담자 관계에 초점을 둔다.
