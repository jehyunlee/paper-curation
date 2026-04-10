---
title: "825_Towards_an_AI_co-scientist"
authors:
  - "Juraj Gottweis"
  - "Wei-Hung Weng"
  - "Alexander Daryin"
  - "Tao Tu"
  - "Anil Palepu"
date: "2025"
doi: "https://doi.org/10.48550/arXiv.2502.18864"
arxiv: ""
score: 4.2
essence: "Gemini 2.0 기반 다중 에이전트 시스템으로 구성된 AI 공동 과학자(AI co-scientist)를 제시하며, 생성-토론-진화(generate-debate-evolve) 방식으로 기존 증거를 기반으로 참신한 연구 가설을 자동 생성하고 개선하는 시스템을 개발했다. 약물 재사용, 간섬유화 신규 표적, 박테리아 유전자 전달 메커니즘 분야에서 in vitro 검증을 통해 시스템의 과학 발견 가속화 능력을 실증했다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/AI-Powered_Research_Planning"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Gottweis et al._2025_Towards an AI co-scientist.pdf"
---

# Towards an AI co-scientist

> **저자**: Juraj Gottweis, Wei-Hung Weng, Alexander Daryin, Tao Tu, Anil Palepu, Petar Sirkovic, Artiom Myaskovsky, Felix Weissenberger, Keran Rong, Ryutaro Tanno, Khaled Saab, Dan Popovici, Jacob Blum, Fan Zhang, Katherine Chou, Avinatan Hassidim, Burak Gokturk, Amin Vahdat, Pushmeet Kohli, Yossi Matias, Andrew Carroll, Kavita Kulkarni, Nenad Tomasev, Vikram Dhillon, Eeshit Dhaval Vaishnav, Byron Lee, Tiago R D Costa, José R Penadés, Gary Peltz, Yunhan Xu, Annalisa Pawlosky, Alan Karthikesalingam, Vivek Natarajan | **날짜**: 02/18/2025 | **DOI**: [https://doi.org/10.48550/arXiv.2502.18864](https://doi.org/10.48550/arXiv.2502.18864)

---

## Essence

![Figure 1](figures/fig1.webp)
*AI 공동 과학자의 시스템 설계 및 실험 검증 요약: (a) 다중 에이전트 아키텍처와 과학자 상호작용 패러다임, (b) 약물 재사용, 신규 표적 발굴, 항생제 내성 메커니즘 해석 3가지 생의학 응용 분야에서의 검증*

Gemini 2.0 기반 다중 에이전트 시스템으로 구성된 AI 공동 과학자(AI co-scientist)를 제시하며, 생성-토론-진화(generate-debate-evolve) 방식으로 기존 증거를 기반으로 참신한 연구 가설을 자동 생성하고 개선하는 시스템을 개발했다. 약물 재사용, 간섬유화 신규 표적, 박테리아 유전자 전달 메커니즘 분야에서 in vitro 검증을 통해 시스템의 과학 발견 가속화 능력을 실증했다.

## Motivation

- **Known**: 최신 AI 시스템은 고급 추론(advanced reasoning), 다중양식 이해(multimodal understanding), 도구 사용 등 에이전트 행동이 가능하며, 추론 시간 계산 비용의 급격한 감소로 활용성이 증가하고 있음.

- **Gap**: 현대 과학 연구는 깊이(discipline-specific depth)와 너비(trans-disciplinary insight) 간의 균형이 필요하나, 급증하는 학술 출판물과 고도화된 실험 기술로 인해 이를 개별 과학자가 달성하기 어려움. 특히 약물 개발은 고비용, 장기간 소요, 높은 실패율 문제 존재.

- **Why**: 인공지능이 학제 간 지식 통합, 대규모 문헌 분석, 신규 가설 생성 등을 통해 과학 발견 과정을 가속화할 수 있는 잠재력을 가짐.

- **Approach**: 과학적 방법론을 반영한 다중 에이전트 아키텍처 설계, 토너먼트 기반 가설 진화, 테스트타임 컴퓨트(test-time compute) 스케일링, 자동 평가 및 웹 검색 등 도구 통합으로 과학자-AI 협업 시스템 구축.

## Achievement

![Figure 1b](figures/fig1.webp)
*3가지 생의학 응용 분야에서의 실험 검증: 약물 재사용(AML), 신규 표적 발굴(간섬유화), 박테리아 유전자 전달 메커니즘*

1. **약물 재사용(Drug Repurposing)**: AML(급성 골수성 백혈병) 치료를 위한 신규 약물 후보 제시. Binimetinib, Pacritinib 등 임상적 근거를 가진 후보와 KIRA6, Leflunomide 등 완전히 새로운 재사용 후보 제안. 임상 적용 가능한 농도에서 AML 세포주 MOLM13에 대한 종양 억제 활성 in vitro 검증 성공.

2. **신규 표적 발굴(Novel Target Discovery)**: 간섬유화 유발 근육섬유모세포(myofibroblast) 형성에 기여하는 3가지 신규 에피제닉 표적(epigenetic targets) 제시. 인간 간 오르가노이드(human hepatic organoids)에서 항섬유화 활성과 간세포 재생 in vitro 검증 확인.

3. **항생제 내성 메커니즘 해석(Antimicrobial Resistance)**: 박테리아의 cf-PICI(cryptic-Prophage-like ICEs) 유전자 전달 메커니즘 10년간의 과학자 연구 결과를 2일 내에 재현. 캡시드-꼬리 상호작용 등 새로운 가설 독립 제시.

## How

![Figure 2](figures/fig2.webp)
*AI 공동 과학자의 다중 에이전트 아키텍처*

- **다중 에이전트 구성**:
  - **Generation Agent**: 문헌 탐색(literature exploration)과 시뮬레이션 기반 과학적 토론(simulated scientific debate)을 통한 가설 생성
  - **Reflection Agent**: 전체 리뷰, 웹 검색, 시뮬레이션/토너먼트 리뷰, 깊이 있는 검증(deep verification)
  - **Ranking Agent**: 토너먼트 방식의 가설 비교 및 순위 매김, 승패 패턴(win-loss patterns) 분석
  - **Evolution Agent**: 다른 아이디어에서의 영감, 단순화, 연구 확장
  - **Proximity Agent**: 연관성 평가
  - **Meta-review Agent**: 연구 개요 및 계획 수립

- **핵심 메커니즘**:
  - **테스트타임 컴퓨트 스케일링**: 추론 시간의 계산량 증대로 가설 품질 향상 (Elo 자동 평가지표 지속적 개선)
  - **토너먼트 진화**: 가설들 간 경합을 통한 자가 개선(self-improving loop) 달성
  - **이질적 도구 활용**: 웹 검색, 전문 AI 모델, 추가 도구 통합으로 가설의 근거성과 품질 강화

- **과학자 협업 인터페이스**:
  - 자연언어 기반 연구 목표 입력
  - 아이디어 제시, 검토, 채팅 기반 상호작용
  - 실시간 피드백 반영 및 방향 재설정 가능

## Originality

- **혁신적 시스템 설계**: 과학적 방법론을 직접 구현한 생성-토론-진화 아키텍처는 기존 LLM 활용 방식과 구별되는 근본적으로 새로운 패러다임 제시.

- **다중 에이전트 협력 메커니즘**: 비동기식 작업 실행 프레임워크(asynchronous task execution framework)로 유연한 컴퓨팅 스케일링 및 자율적 개선 루프 구현.

- **토너먼트 기반 가설 진화**: 단순 추론이 아닌 경합과 비교를 통한 반복적 개선으로 가설의 신규성과 타당성 동시 달성.

- **생의학 분야 end-to-end 검증**: AI 생성 가설에 대한 실제 in vitro 실험 검증으로 이론적 제안을 넘어 실질적 과학적 기여 입증. 특히 10년 연구를 2일 만에 재현한 사례는 AI 가속화 효과의 강력한 증거.

- **과학자-AI 협업 패러다임**: 자동화가 아닌 "scientist-in-the-loop" 설계로 도메인 전문가의 주도성 보존.

## Limitation & Further Study

- **검증의 제한성**: 3개 생의학 분야(약물 재사용, 표적 발굴, 항생제 내성)에 국한되었으며, 다른 과학 분야(물리학, 화학, 수학 등)로의 일반화 가능성 미검증.

- **인과성 검증 부족**: AI 생성 가설이 실제로 독립적으로 혁신적인지, 아니면 기존 문헌 조합일 가능성 구별이 불명확. 특히 박테리아 유전자 전달 메커니즘 사례는 "재현"이지 독립 발견 여부 모호.

- **스케일링 비용-효과 분석 미흡**: 테스트타임 컴퓨트 스케일링의 실제 비용, 처리 시간, 수렴 특성에 대한 정량적 분석 부재.

- **평가 지표의 한계**: Elo 자동 평가지표의 타당성 검증 부족. 자동 평가와 실제 과학적 가치의 상관관계가 명확하지 않음.

- **후속 연구 방향**:
  - 물리, 화학, 수학 등 다양한 과학 분야로 확대 검증
  - 대규모 임상시험으로 제안 약물의 임상적 효과 입증
  - AI 생성 가설의 참신성을 정량화하는 새로운 메트릭 개발
  - 과학자 실제 사용 사례 및 장기 영향 평가


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4/5
- Significance: 4.5/5
- Clarity: 4/5
- Overall: 4.2/5

**총평**: 본 논문은 대규모 언어모델의 다중 에이전트 협력을 활용해 과학 발견 과정을 혁신하려는 야심 찬 시도로, 약물 재사용·신규 표적 발굴·항생제 내성 메커니즘 분야에서 in vitro 검증을 통해 실질적 가능성을 입증했다. 다만 기술 세부사항의 명확화, 다양한 과학 분야로의 확대 검증, 그리고 AI 기여도의 정량적 평가 개선이 후속 과제이다.

## Related Papers

- 🔄 다른 접근: [[papers/071_AgentRxiv_Towards_Collaborative_Autonomous_Research/review]] — AI co-scientist의 생성-토론-진화 방식과 AgentRxiv의 프리프린트 서버 기반 협업은 서로 다른 메커니즘으로 에이전트 간 지식 발전을 달성한다.
- 🔗 후속 연구: [[papers/826_Towards_Autonomous_Mathematics_Research/review]] — Aletheia의 자율적 수학 연구가 AI co-scientist의 가설 생성 및 검증 프레임워크를 전문 수학 영역으로 특화하여 확장한 적용이다.
- 🏛 기반 연구: [[papers/795_The_AI_Scientist_Towards_Fully_Automated_Open-Ended_Scientif/review]] — AI Scientist의 완전 자동화된 과학 발견 방법론이 Gemini 2.0 기반 AI co-scientist 시스템 개발의 기본적인 기술적 토대를 제공한다.
- 🔄 다른 접근: [[papers/071_AgentRxiv_Towards_Collaborative_Autonomous_Research/review]] — AgentRxiv의 협업적 연구 공유 메커니즘과 AI co-scientist의 생성-토론-진화 방식은 서로 다른 접근으로 에이전트 간 지식 축적을 달성한다.
- 🧪 응용 사례: [[papers/826_Towards_Autonomous_Mathematics_Research/review]] — AI co-scientist의 가설 생성-개선 메커니즘이 Aletheia의 자율적 수학 정리 발견에 구체적으로 적용된 전문 영역 특화 사례이다.
- 🔄 다른 접근: [[papers/059_Agent_Laboratory_Using_LLM_Agents_as_Research_Assistants/review]] — Agent Laboratory와 Towards an AI co-scientist는 모두 AI 연구 지원을 다루지만, 인간 아이디어 실행 지원과 완전 자율적 공동 연구라는 서로 다른 협업 모델을 제시합니다.
- 🏛 기반 연구: [[papers/578_Novelseek_When_agent_becomes_the_scientistbuilding_closed-lo/review]] — AI 공동 과학자 연구는 InternAgent가 인간 전문가 피드백을 통합하면서 자율 과학 연구를 수행하는 이론적 기반을 제공한다.
- 🏛 기반 연구: [[papers/436_InternAgent_When_Agent_Becomes_the_Scientist_--_Building_Clo/review]] — AI 공동 과학자의 개념적 기반과 비전을 제공한다.
