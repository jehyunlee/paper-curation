---
title: "849_UI-TARS_Pioneering_Automated_GUI_Interaction_with_Native_Age"
authors:
  - "Yujia Qin"
  - "Yining Ye"
  - "Junjie Fang"
  - "Haoming Wang"
  - "Shihao Liang"
date: "2025"
doi: "10.48550/arXiv.2501.12326"
arxiv: ""
score: 4.5
essence: "스크린샷만을 입력으로 받아 마우스, 키보드 조작 등 인간 같은 상호작용을 수행하는 네이티브 GUI 에이전트 모델로, 상용 모델(GPT-4o)에 기반한 프레임워크들을 뛰어넘는 엔드-투-엔드(end-to-end) 성능을 달성했다."
tags:
  - "cat/LLM-Based_Scientific_Reasoning"
  - "sub/Large_Language_Model_Agents"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Qin et al._2025_UI-TARS Pioneering Automated GUI Interaction with Native Agents.pdf"
---

# UI-TARS: Pioneering Automated GUI Interaction with Native Agents

> **저자**: Yujia Qin, Yining Ye, Junjie Fang, Haoming Wang, Shihao Liang | **날짜**: 2025 | **DOI**: [10.48550/arXiv.2501.12326](https://doi.org/10.48550/arXiv.2501.12326)

---

## Essence

![Figure 1](figures/fig1.webp) *UI-TARS가 항공편 검색을 돕는 데모 사례*

스크린샷만을 입력으로 받아 마우스, 키보드 조작 등 인간 같은 상호작용을 수행하는 네이티브 GUI 에이전트 모델로, 상용 모델(GPT-4o)에 기반한 프레임워크들을 뛰어넘는 엔드-투-엔드(end-to-end) 성능을 달성했다.

## Motivation

- **Known**: 기존 GUI 에이전트는 HTML, 접근성 트리 등 텍스트 기반 표현에 의존하는 모듈식 프레임워크(framework) 구조를 사용하거나, GPT-4o와 같은 상용 VLM(Vision Language Model)에 의존한다.

- **Gap**: (1) 텍스트 기반 방식은 플랫폼별 불일치, 장황함, 확장성 부족 문제 존재, (2) 모듈식 프레임워크는 전문가 지식에 의존하며 새로운 상황에 취약하고, (3) 네이티브 에이전트 모델로의 전환에는 지각(perception), 추론(reasoning), 메모리(memory), 행동(action) 전체를 통합한 대규모 고품질 데이터의 부재라는 데이터 병목 문제가 있다.

- **Why**: 순수 비전(pure-vision) 기반 엔드-투-엔드 에이전트 모델은 인간의 인지 과정에 더 가깝고 더 적응적이지만, 실제 성능은 기대에 미치지 못하고 있다.

- **Approach**: 고품질 GUI 데이터 수집 및 System-2 추론 통합, 그리고 반복적 학습(iterative training)과 반성 튜닝(reflection tuning)을 통해 네이티브 GUI 에이전트 모델 UI-TARS를 개발한다.

## Achievement

![Figure 2](figures/fig2.webp) *GUI 에이전트의 진화 경로*

![Figure 3](figures/fig3.webp) *핵심 역량 및 평가 개요*

1. **벤치마크 우수 성능**: OSWorld에서 50스텝 기준 24.6점(Claude 22.0 초과), AndroidWorld에서 46.6점(GPT-4o 34.5 초과) 달성, 10개 이상의 GUI 에이전트 벤치마크에서 SOTA(State-of-the-Art) 성능 달성

2. **통합 아키텍처**: 지각, 행동 모델링, System-2 추론, 메모리를 하나의 엔드-투-엔드 모델로 통합하여 모듈식 프레임워크보다 우수한 성능 달성

3. **자동 데이터 수집 및 정제**: 수백 대의 가상 머신을 활용한 자동 궤적(trace) 수집 및 다단계 필터링으로 대규모 고품질 데이터 생성

## How

![Figure 4](figures/fig4.webp) *UI-TARS의 아키텍처 개요 및 핵심 역량*

- **강화된 지각(Enhanced Perception)**: 
  - 요소 설명(element description), 밀집 캡셔닝(dense captioning), 상태 전환 캡셔닝(state transition captioning), 시각적 추론 QA, Set-of-Mark 프롬프팅 등 5가지 지각 작업으로 구성된 대규모 데이터셋 구축
  - GUI 요소의 타입, 바운딩박스, 텍스트 내용 메타데이터 추출을 통한 세밀한 UI 이해

- **통합 행동 모델링(Unified Action Modeling)**:
  - 플랫폼별 의미적으로 동등한 행동을 표준화된 행동 공간으로 통합
  - 요소 설명과 공간 좌표를 쌍으로 하는 대규모 그라운딩(grounding) 데이터셋으로 정확한 상호작용 실현

- **System-2 추론(System-2 Reasoning)**:
  - 6M 개의 GUI 튜토리얼 수집 및 정제로 논리적 의사결정을 위한 GUI 지식 제공
  - 작업 분해(task decomposition), 장기 일관성(long-term consistency), 마일스톤 인식(milestone recognition), 시행착오(trial&error), 반성(reflection) 등 다양한 추론 패턴 주입
  - 각 행동 전에 명시적 "생각(thoughts)" 생성으로 지각과 행동을 의도적 의사결정과 연결

- **반복적 개선(Iterative Refinement)**:
  - 다단계 필터링: 규칙 기반 휴리스틱, VLM 점수 평가, 인간 검증
  - 반성 튜닝: 오류 수정(error correction)과 반성 후(post-reflection) 데이터 주석으로 에이전트가 자신의 실수를 학습하고 회복

![Figure 5](figures/fig5.webp) *지각 및 그라운딩 데이터 예시*

## Originality

- **순수 비전 기반 네이티브 모델**: 텍스트 표현에 대한 의존성을 완전히 제거하고 스크린샷만으로 동작하는 완전히 새로운 접근 방식

- **System-2 추론 통합**: GUI 에이전트 분야에서 명시적인 생각 과정을 포함한 의도적 추론을 체계적으로 적용한 첫 시도

- **자동화된 데이터 수집 파이프라인**: 수백 대의 가상 머신을 활용한 대규모 자동 궤적 생성 및 반성 기반 필터링 방식으로 데이터 병목 문제 해결

- **GUI 에이전트 진화 경로 분석**: 규칙 기반 에이전트에서 네이티브 에이전트 모델을 거쳐 활동적이고 평생학습하는 에이전트로의 진화 과정을 체계적으로 분석

- **멀티플랫폼 통합 행동 공간**: 웹, 모바일, 데스크톱 등 다양한 플랫폼의 행동을 의미적으로 통합하는 새로운 표현 방식

## Limitation & Further Study

- **데이터 규모의 한계**: 비록 대규모 자동 수집을 시도했으나, 텍스트 기반 에이전트나 VLM에 비해 여전히 상대적으로 적은 양의 세밀한 주석 데이터 필요

- **실시간 동적 환경의 제약**: 현재 구축된 가상 환경에서의 학습으로, 완전히 예측 불가능한 실제 사용자 인터페이스에 대한 일반화 능력은 미지수

- **System-2 추론 오버헤드**: 명시적 생각 과정이 추가되면서 응답 시간이 증가하는 트레이드오프로, 실시간 상황에서의 배포 고려 필요

- **후속 연구 방향**:
  - 활동적 학습(active learning)을 통한 인간 피드백 수집의 최소화
  - 평생학습(lifelong learning)으로 시간에 따른 인터페이스 변화에 적응하는 에이전트 개발
  - 다양한 자연어 지시사항(instruction)에 대한 강건성 개선
  - 크로스 도메인 전이 학습(transfer learning) 능력 강화

## Evaluation

- **Novelty**: 4.5/5 — 순수 비전 기반 네이티브 모델과 System-2 추론 통합은 창의적이나, 개별 기술들(VLM, 추론 패턴)은 기존 개념의 조합

- **Technical Soundness**: 4.5/5 — 명확한 아키텍처와 체계적인 데이터 구축 방식이 돋보이나, 반성 튜닝의 상세한 기술적 검증 부재

- **Significance**: 5/5 — GUI 에이전트 분야에서 다중 벤치마크를 선도하며, 모듈식 프레임워크를 넘어 엔드-투-엔드 모델의 실질적 우수성을 증명

- **Clarity**: 4/5 — 전반적으로 잘 구성되었으나, 일부 기술적 세부사항(예: 그라운딩 손실 함수, 반성 튜닝의 정량적 기준)의 설명 부족

- **Overall**: 4.5/5

**총평**: UI-TARS는 GUI 에이전트 분야의 패러다임 전환을 제시하는 중요한 논문으로, 엔드-투-엔드 네이티브 모델이 모듈식 프레임워크를 실제로 능가할 수 있음을 보여주었으며, 특히 자동화된 데이터 수집과 반성 기반 학습 메커니즘은 향후 유사한 구체화(embodied) AI 분야의 발전에 중요한 기여를 할 것으로 기대된다.

## Related Papers

- 🔄 다른 접근: [[papers/073_AI_Agents_in_Engineering_Design_A_Multi-Agent_Framework_for/review]] — GUI 자동화와 엔지니어링 설계 자동화 모두 인간-AI 협업을 다룹니다.
- 🏛 기반 연구: [[papers/590_Openhands_An_open_platform_for_ai_software_developers_as_gen/review]] — 일반적인 AI 소프트웨어 개발 플랫폼이 네이티브 GUI 에이전트의 기반이 됩니다.
- 🔗 후속 연구: [[papers/888_X-webagentbench_A_multilingual_interactive_web_benchmark_for/review]] — GUI 상호작용이 다국어 웹 에이전트 벤치마크로 확장됩니다.
- 🏛 기반 연구: [[papers/073_AI_Agents_in_Engineering_Design_A_Multi-Agent_Framework_for/review]] — 네이티브 에이전트의 상호작용이 엔지니어링 설계 자동화의 기반을 제공합니다.
- 🔄 다른 접근: [[papers/061_Agent_S_An_Open_Agentic_Framework_that_Uses_Computers_Like_a/review]] — Agent S와 UI-TARS는 모두 GUI 자동화를 다루지만, 인간과 유사한 컴퓨터 사용과 네이티브 에이전트 기반 자동화라는 서로 다른 접근 방식을 채택합니다.
