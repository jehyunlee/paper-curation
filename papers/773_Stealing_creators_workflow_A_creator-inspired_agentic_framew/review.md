---
title: "773_Stealing_creators_workflow_A_creator-inspired_agentic_framew"
authors:
  - "Jong Inn Park"
  - "Maanas Taneja"
  - "Qianwen Wang"
  - "Dongyeop Kang (University of Minnesota)"
date: "2025"
doi: "N/A"
arxiv: ""
score: 3.5
essence: "본 논문은 과학 논문을 짧은 형식의 동영상으로 변환하는 완전 자동화된 멀티-LLM 에이전트 프레임워크 SciTalk를 제안한다. 인간 크리에이터의 반복적 워크플로우에서 영감을 받아 피드백 루프를 통해 과학적 정확성과 시각적 품질을 향상시킨다."
tags:
  - "cat/Scientific_Language_Processing_and_Visualization"
  - "sub/LLM_Agent_Benchmarking"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Le et al._2025_Stealing creator’s workflow A creator-inspired agentic framework with iterative feedback loop for i.pdf"
---

# Stealing creator's workflow: A creator-inspired agentic framework with iterative feedback loop for improved scientific short-form generation

> **저자**: Jong Inn Park, Maanas Taneja, Qianwen Wang, Dongyeop Kang (University of Minnesota) | **날짜**: 2025 | **DOI**: N/A

---

## Essence

![Figure 1: 다중 에이전트 비디오 생성 파이프라인의 개념적 개요](figures/fig1.webp)
*전처리, 계획, 편집, 피드백 및 평가의 4단계로 구성된 파이프라인*

본 논문은 과학 논문을 짧은 형식의 동영상으로 변환하는 완전 자동화된 멀티-LLM 에이전트 프레임워크 SciTalk를 제안한다. 인간 크리에이터의 반복적 워크플로우에서 영감을 받아 피드백 루프를 통해 과학적 정확성과 시각적 품질을 향상시킨다.

## Motivation

- **Known**: 최근 확산 기반 비디오 생성 모델(diffusion-based video generation models)은 텍스트, 이미지 등으로부터 엔드-투-엔드 비디오 생성 가능. TikTok, Instagram Reels 등 플랫폼에서 과학 콘텐츠가 인기를 얻고 있음.

- **Gap**: 현존하는 생성형 모델은 과학적 사실성(factual accuracy) 유지 어려움. 복잡한 과학 지식을 정확하게 표현하는 시각적 아티팩트(visual artifacts) 발생. 전체 생성 방식은 신뢰성 있는 과학 콘텐츠 생성에 부적합.

- **Why**: 인간 크리에이터는 기획(planning), 제작(production), 편집(editing)의 반복적 다단계 프로세스를 거쳐 원문 자료(PDF, 그래프, 텍스트)에 기반한 그라운딩(grounding)된 콘텐츠 생성. 이러한 워크플로우는 과학적 무결성 유지에 필수적.

- **Approach**: 크리에이터 워크플로우를 모방한 구조화된 멀티-에이전트 프레임워크 제안. 생성형 모델 대신 비디오 편집 라이브러리 사용으로 시각적 충실도 보장. 피드백 에이전트를 통한 반복적 개선 메커니즘 도입.

## Achievement

![Figure 4: 반복(iteration)에 따른 평가 점수 추이](figures/fig4.webp)
*인간 평가와 모델 평가 모두에서 반복을 거쳐 개선 경향*

1. **멀티-에이전트 협업 체계**: 6개의 특화된 LLM 기반 에이전트(Flashtalk Generator, Sceneplan Generator, Background Assistant, Text Assistant, Effect Assistant, Layout Allocator)가 4단계 파이프라인에서 조율된 협업 수행. 단순 프롬프팅 기반선(baseline)보다 더 정확하고 매력적인 콘텐츠 생성 달성.

2. **반복적 피드백 루프**: Vision-Language Model 기반 Feedback Agent가 각 부분 장면(sub-scene)을 정성적·정량적 지표로 평가. Reflection Agent가 피드백을 프롬프트에 반영하여 점진적 개선 구현. 사용자 역할 시뮬레이션을 통한 자동화된 피드백 메커니즘.

## How

![Figure 2: 생성 에이전트들이 장면 구성에 기여하는 상세한 워크플로우](figures/fig2.webp)
*각 에이전트의 입출력과 역할 분담*

**프리프로세싱 단계 (Preprocessing)**
- arXiv 등 소스에서 논문 수집, 원문 텍스트 추출 (HTML/PDF)
- 그래프, 표, 스크린샷 등 시각 자산 추출 및 구조화된 형식으로 저장
- 원문 기반 그라운딩 보장

**계획 단계 (Planning)**
- Flashtalk Generator: 학술회의 플래시토크 형식 모방한 4부 구조 스크립트 생성
  - (1) Aggressive Hook, (2) Brief Context, (3) Intriguing Teaser, (4) Call to Action
- Audio/Avatar Assistant: 음성 및 아바타 애니메이션 mp3/mp4 생성
- Sceneplan Generator: 각 섹션을 1-5개 부분 장면으로 세분화, 타이밍 메타데이터 추가

**편집 단계 (Editing)**
- Background Assistant: 장면 설명과 가용 이미지 기반 배경 선택
- Text Assistant: 자막 및 화면상 텍스트 생성, 폰트 크기/색상/위치/지속시간 지정
- Effect Assistant: 시각 효과 적용
- Layout Allocator: 각 부분 장면의 시각적 레이아웃 결정
- 비디오 편집 라이브러리로 최종 클립 합성

**피드백 및 평가 단계 (Feedback & Evaluation)**
- Feedback Agent: 질적/양적 지표로 각 부분 장면 평가
- Evaluation Agent: 전체 비디오 품질 평가
- Reflection Agent: 피드백을 다음 반복 에이전트 프롬프트에 통합

## Originality

- **첫 시도 작업**: 에이전트 기반 과학 비디오 자동 생성을 체계적으로 다룬 최초 연구
- **크리에이터 워크플로우 모방**: 인간 창작자의 반복적 프로세스를 형식화하여 자동화 시스템에 구현
- **소스 기반 그라운딩**: 생성형 모델의 창의적 자유도 제약 대신 원문 자료(PDF, 그래프)를 직접 활용하여 과학적 정확성 우선시
- **자동화된 피드백 루프**: Vision-Language Model을 활용한 자동 평가와 프롬프트 개선 메커니즘 도입
- **멀티-에이전트 조율**: 단순 단일 에이전트가 아닌 6개 특화 에이전트의 체계적 조율로 모듈화된 제어 가능성 실현

## Limitation & Further Study

- **성능 한계**: 생성된 비디오가 여전히 인간 크리에이터의 일관성(coherence)과 완성도(polish) 수준에 미치지 못함
- **오류 누적**: 반복 과정에서 오류가 누적될 수 있다는 관찰. 피드백 오정렬(feedback misalignment) 및 시각적 혼잡(visual clutter) 문제 발생
- **예비 탐색 단계**: 본 연구가 새로운 영역의 초기 탐색 단계로, 워크플로우 최적화 및 시스템 견고성(robustness) 개선 필요
- **향후 방향**: 피드백 메커니즘 정교화, 에이전트 간 조율 개선, 더 큰 규모 평가 데이터셋 구축, 실시간 반복 최적화 알고리즘 개발 필요

## Evaluation

- **Novelty**: 4/5 — 에이전트 기반 과학 비디오 생성 태스크 자체가 신규이며, 크리에이터 워크플로우 모방과 피드백 루프 통합이 창의적. 다만 개별 기술 요소들은 기존 연구 기반.

- **Technical Soundness**: 3/5 — 파이프라인 설계가 논리적이고 체계적이나, 반복 과정에서의 오류 누적, 피드백 오정렬 문제 등 기술적 미흡. 평가 방법론 및 베이스라인 비교 부족.

- **Significance**: 3/5 — 과학 커뮤니케이션의 중요한 문제를 다루나, 현재 결과가 인간 수준에 미치지 못하여 실무적 영향력 제한적. 초기 탐색 논문으로 의미 있으나 완성도 낮음.

- **Clarity**: 4/5 — 파이프라인 구조와 에이전트 역할 설명이 명확하고 Figure 1-2가 도움됨. 다만 구체적인 프롬프트 예시와 실험 설정 상세 설명 부족.

- **Overall**: 3.5/5

**총평**: 과학 논문을 짧은 형식 동영상으로 변환하는 새로운 멀티-에이전트 프레임워크를 제안한 의미 있는 초기 연구이나, 생성 결과가 인간 수준에 미치지 못하고 반복 과정의 오류 누적 문제가 해결되지 않아 현재로선 방법론 검증 단계에 머물러 있다. 더 견고한 평가, 개선된 피드백 메커니즘, 그리고 실제 산업 적용 가능성 검증이 필요하다.

## Related Papers

- 🔄 다른 접근: [[papers/597_P2p_Automated_paper-to-poster_generation_and_fine-grained_be/review]] — 둘 다 학술 논문의 시각적 변환을 다루지만 하나는 동영상 생성에, 다른 하나는 포스터 생성에 초점을 맞춘다.
- 🔗 후속 연구: [[papers/600_Paper2Web_Lets_Make_Your_Paper_Alive/review]] — 논문을 웹으로 변환하는 Paper2Web 시스템이 SciTalk의 과학 논문 콘텐츠 변환 아이디어를 다른 매체로 확장한 사례를 제공한다.
- 🏛 기반 연구: [[papers/331_Exploring_collaboration_mechanisms_for_llm_agents_A_social_p/review]] — LLM 에이전트의 협업 메커니즘 연구가 SciTalk의 멀티-LLM 에이전트 프레임워크 설계에 이론적 기반을 제공한다.
