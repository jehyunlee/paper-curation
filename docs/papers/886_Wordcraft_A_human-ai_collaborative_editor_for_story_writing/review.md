---
title: "886_Wordcraft_A_human-ai_collaborative_editor_for_story_writing"
authors:
  - "Andy Coenen"
  - "Luke M. Davis"
  - "Daphne Ippolito"
  - "Emily Reif"
  - "Ann Yuan"
date: "2021"
doi: "N/A"
arxiv: ""
score: 4.0
essence: "신경 언어 모델의 능력을 활용하여 인간 작가와 AI 어시스턴트가 협력하는 스토리 쓰기 도구를 제시한다. Few-shot 학습과 대화형 인터페이스를 통해 단일 언어 모델으로 다양한 창작 작업을 지원한다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Academic_Writing_Personalization"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Coenen et al._2021_Wordcraft A human-ai collaborative editor for story writing.pdf"
---

# Wordcraft: A human-ai collaborative editor for story writing

> **저자**: Andy Coenen, Luke M. Davis, Daphne Ippolito, Emily Reif, Ann Yuan | **날짜**: 2021 | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp) *Wordcraft 에디터: 왼쪽은 텍스트 편집 영역, 오른쪽은 AI 어시스턴트의 다양한 상호작용 옵션 제공*

신경 언어 모델의 능력을 활용하여 인간 작가와 AI 어시스턴트가 협력하는 스토리 쓰기 도구를 제시한다. Few-shot 학습과 대화형 인터페이스를 통해 단일 언어 모델으로 다양한 창작 작업을 지원한다.

## Motivation

- **Known**: 신경 언어 모델이 실제 응용에 적용되고 있으나, 기존 상호작용 방식은 제한적이다. 각 기능마다 별도 모델 훈련이 필요한 문제가 있다.
- **Gap**: 스토리 작성의 다양한 단계(계획, 작성, 편집)에서 필요한 여러 종류의 작업을 유연하게 지원하는 통합 인터페이스가 부족하다.
- **Why**: 창작 활동은 사용자의 의도를 명확하게 전달하기 어렵고, 예상 밖의 결과도 창작의 기회가 될 수 있는 이상적인 테스트 환경이다.
- **Approach**: Few-shot 학습 기법과 대화형 언어 모델(Meena)을 활용하여 단일 모델로 다양한 창작 작업을 지원하는 협력형 에디터 개발

## Achievement

![Figure 2](figures/fig2.webp) *Few-shot 학습을 위한 단계별 대화 맥락: 인필링, 엘러보레이션, 리라이팅 작업의 예시*

![Figure 3](figures/fig3.webp) *사용자 요청에 따른 프롬프트 구성 과정: 사용자 스토리 → 대화 맥락 추가 → 모델 응답*

1. **다목적 창작 지원**: 연속 생성(continuation), 인필링(infilling), 엘러보레이션(elaboration), 리라이팅(rewriting) 등 다양한 작업을 단일 모델로 지원

2. **대화형 인터페이스의 우월성**: 일반 언어 모델 대비 대화형 모델(Meena)이 작가의 요청을 더 잘 이해하고 해석 가능한 응답을 제공하며, 불분명한 요청에 대해 명시적으로 피드백 가능

3. **유연한 상황 적응**: Few-shot 프롬프트를 통해 모델이 작업별 맥락을 학습하고 사용자 정의 쿼리 지원으로 예상하지 못한 창작 요청에도 대응 가능

## How

- **기반 모델**: Meena 대화 언어 모델 사용 (일반 목적 언어 모델과 비교 검토)
- **Few-shot 학습**: 각 작업별로 2-7개의 예시를 포함한 대화형 맥락 제작
  - 인필링: 6개 예시로 빈칸 채우기 작업 프레임
  - 엘러보레이션: 4개 예시로 상세 설명 작업 프레임
  - 리라이팅: 7개 예시로 스타일 변환 작업 프레임
- **프롬프트 구성**: 사용자 스토리 + 작업별 대화 맥락 + 사용자 요청을 조합하여 모델 입력 생성
- **UI 설계**: 텍스트 에디터의 친숙한 인터페이스 유지하면서 우측에 작업별 버튼 및 단축키 제공
- **디코딩**: Top-k 랜덤 샘플링(k=40) 사용으로 다양한 후보 생성

## Originality

- **대화형 모델의 창의 작문 활용**: 기존의 좌-우 생성(left-to-right generation) 패러다임을 벗어나 대화형 언어 모델을 스토리 작성의 협력 파트너로 활용

- **Few-shot 프롬프트의 창의적 설계**: 각 작업 유형별로 자연스러운 대화 형식의 예시 문맥을 수작업으로 구성하여 직관적이고 해석 가능한 프롬프팅 방식 제시

- **다중 상호작용 모드 통합**: 단일 모델로 연속 생성, 인필링, 엘러보레이션, 리라이팅, 자유형 질문 등 다양한 작업을 유연하게 지원하는 통합 프레임워크

- **HCI 관점의 탐색 공간**: 언어 모델의 능력과 한계를 테스트하고 사람들의 상호작용 패턴을 연구하는 실증적 플랫폼 제공

## Limitation & Further Study

- **한계**:
  - 현재 소규모 정성적 연구만 수행되어 대화형 모델 vs 일반 언어 모델의 우월성에 대한 체계적 검증 부족
  - Few-shot 프롬프트의 수작업 구성으로 인한 확장성 제한
  - 모델이 메타 텍스트(스토리 자체가 아닌 스토리 관련 설명)를 생성하는 문제 미해결
  - 문자 길이 지정 요청(예: "10단어")에 대한 정확도 미흡

- **후속 연구**:
  - Meena와 일반 목적 언어 모델의 체계적 비교 실험
  - 인간 피드백을 훈련 루프에 통합하는 파이프라인 개발
  - 동적 데이터셋 수집을 통한 지속적 훈련 및 평가 방법 개발
  - 사용자의 상호작용 패턴 및 창작 결과에 미치는 영향 분석

## Evaluation

- **Novelty**: 4/5 - 대화형 모델을 창작 협력자로 활용하는 접근과 다중 상호작용 모드 설계가 독창적이나, Few-shot 학습 자체는 기존 기법

- **Technical Soundness**: 3.5/5 - 프롬프트 설계와 모델 활용은 합리적이나, 체계적 비교 실험 부족으로 주요 주장(대화형 모델 우월성)의 기술적 근거 약함

- **Significance**: 4/5 - 창작 보조 도구의 실제 활용 가능성과 HCI 연구 플랫폼으로서의 가치가 높으나, 평가 방법론이 정립되지 않아 실제 효과 검증 필요

- **Clarity**: 4.5/5 - 인터페이스 설계와 구체적 사례가 명확하게 제시되었으나, 일부 기술적 세부사항(모델 선택 이유, 프롬프트 최적화 과정)에 대한 설명 부족

- **Overall**: 4/5

**총평**: 신경 언어 모델과 인간의 협력적 창작을 지원하는 실용적인 도구로서 가치 있는 연구이나, 핵심 주장들에 대한 체계적 검증과 평가 방법론이 부족하다는 점이 아쉽다. 향후 사용자 연구와 모델 비교 실험을 통해 강화될 필요가 있다.

## Related Papers

- 🔗 후속 연구: [[papers/702_Scholarcopilot_Training_large_language_models_for_academic_w/review]] — 인간-AI 협업 글쓰기의 기본 개념이 학술 논문 작성이라는 전문적 영역에서 인용 검색과 동적 생성을 통합한 특화된 시스템으로 발전한다.
- 🔗 후속 연구: [[papers/775_Step-back_profiling_Distilling_user_history_for_personalized/review]] — 인간-AI 협업 글쓰기를 다중 저자 과학 논문 작성으로 확장하여 개인화된 사용자 프로필 기반의 협업 지원이 가능하다.
- 🏛 기반 연구: [[papers/889_Xtragpt_Llms_for_human-ai_collaboration_on_controllable_acad/review]] — 인간-AI 협업 편집의 기본 프레임워크가 제어 가능한 학술 논문 수정을 위한 협업 모델의 이론적 기반을 제공한다.
- 🔗 후속 연구: [[papers/228_CoAuthor_Designing_a_Human-AI_Collaborative_Writing_Dataset/review]] — GPT-3 기반 창작 글쓰기 협력 연구가 스토리 작성을 위한 인간-AI 협력 에디터 개발로 확장되었다
- 🔄 다른 접근: [[papers/116_Augmenting_the_author_Exploring_the_potential_of_ai_collabor/review]] — 학술 논문 작성에서 스토리 작성으로 확장된 인간-AI 협력적 글쓰기 도구의 다른 응용을 보여준다.
- 🏛 기반 연구: [[papers/703_Scholawrite_A_dataset_of_end-to-end_scholarly_writing_proces/review]] — 인간의 비선형적 글쓰기 과정에 대한 이해가 AI 협력 스토리 편집기 개발의 인간-AI 상호작용 설계 기초가 됩니다.
- 🔗 후속 연구: [[papers/109_Assisting_in_writing_wikipedia-like_articles_from_scratch_wi/review]] — Wordcraft의 인간-AI 협업 편집 프레임워크가 STORM의 자동 기사 생성을 인터랙티브한 공동 창작 과정으로 발전시킨 연구임
- 🔗 후속 연구: [[papers/656_Read_revise_repeat_A_system_demonstration_for_human-in-the-l/review]] — 기본적인 인간-AI 협력 글쓰기를 반복적 개정과 피드백 통합을 통한 더 정교한 협력 편집 시스템으로 확장함
- 🔄 다른 접근: [[papers/375_Generating_full_length_wikipedia_biographies_The_impact_of_g/review]] — 스토리 작성을 위한 인간-AI 협업 편집기로 본 논문과 다른 장르에서의 생성 및 편향 문제를 다룬다.
- 🏛 기반 연구: [[papers/515_Machine-in-the-loop_rewriting_for_creative_image_captioning/review]] — 인간-AI 협업 편집기의 기본 개념이 창의적 이미지 캡션 작성의 기계-인-루프 시스템에 이론적 기반을 제공합니다.
- 🏛 기반 연구: [[papers/702_Scholarcopilot_Training_large_language_models_for_academic_w/review]] — 인간-AI 협업 글쓰기의 기본 개념이 학술 논문 작성이라는 전문적 영역에서 인용 검색과 생성을 통합한 특화된 시스템으로 발전한다.
- 🏛 기반 연구: [[papers/775_Step-back_profiling_Distilling_user_history_for_personalized/review]] — 인간-AI 협업 글쓰기의 기본 개념이 다중 저자 과학 논문 작성이라는 복잡한 협업 시나리오로 확장되어 개인화 기법을 통해 구현된다.
- 🔗 후속 연구: [[papers/889_Xtragpt_Llms_for_human-ai_collaboration_on_controllable_acad/review]] — 인간-AI 협업 글쓰기의 기본 개념을 제어 가능하고 맥락을 인식하는 학술 논문 수정이라는 특화된 기능으로 확장한다.
