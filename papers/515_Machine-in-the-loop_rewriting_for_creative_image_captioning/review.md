---
title: "515_Machine-in-the-loop_rewriting_for_creative_image_captioning"
authors:
  - "Vishakh Padmakumar"
  - "He He"
date: "2021"
doi: "미기재"
arxiv: ""
score: 4.0
essence: "본 논문은 사용자가 주도권을 유지하면서 창의적 작문을 돕는 기계-인-루프 재작성 모델(Creative Rewriting Assistant, CRA)을 제안하며, 이미지 캡션 작성 과제에서 사용자와의 협력을 통해 더욱 서술적이고 비유적인 텍스트 생성을 지원한다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Table_Caption_Generation"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Padmakumar and He_2021_Machine-in-the-loop rewriting for creative image captioning.pdf"
---

# Machine-in-the-loop rewriting for creative image captioning

> **저자**: Vishakh Padmakumar, He He | **날짜**: 2021 | **DOI**: [미기재]

---

## Essence

![Figure 1](figures/fig1.webp)
*그림 1: 사용자가 중심이 되어 재작성할 텍스트 구간을 표시하면, 모델이 창의적인 대안을 제시하는 기계-인-루프 시스템*

본 논문은 사용자가 주도권을 유지하면서 창의적 작문을 돕는 기계-인-루프 재작성 모델(Creative Rewriting Assistant, CRA)을 제안하며, 이미지 캡션 작성 과제에서 사용자와의 협력을 통해 더욱 서술적이고 비유적인 텍스트 생성을 지원한다.

## Motivation

- **Known**: 기존 기계-인-루프 작문 시스템은 머신이 생성한 초안을 제공하는 방식이 사용되어 왔으나, 생성 텍스트가 작가의 의도에서 벗어나 실제 채택률이 매우 낮음(Clark et al., 2018; Akoury et al., 2020)

- **Gap**: 사용자에게 충분한 제어 권한을 제공하면서도 창의적 표현을 효과적으로 보조하는 상호작용 방식의 부재

- **Why**: 창의적 작문은 매우 개방적(open-ended)이므로, 기존의 단순 초안 생성이나 문장 단위 제속(continuation) 방식으로는 충분하지 않음

- **Approach**: 사용자가 명시적으로 특정 텍스트 구간을 표시하면 모델이 그 부분만 재작성(span rewriting) 또는 공백을 채우는(text infilling) 방식의 국소적(local) 편집 방식 도입

## Achievement

![Figure 2](figures/fig2.webp)
*그림 2: 창의적 텍스트 데이터셋의 주석을 활용하여 BART-Large로 일반적 문장을 생성하고, 이를 학습 데이터로 변환하는 과정*

1. **사용자 만족도 향상**: 사용자 연구(Amazon Mechanical Turk)에서 CRA가 기준 모델(BART infilling 모델)보다 훨씬 더 도움이 된다는 평가를 받음

2. **작문 품질 개선**: CRA와 협력하여 작성한 캡션이 독립적으로 작성한 캡션보다 더 창의적이고 다양한 어휘를 포함하며, 제3자 평가에서도 서술적 및 비유적 요소가 더 풍부함

3. **적응적 학습 가능**: 사용자의 승인/거절 피드백을 통해 모델을 지속적으로 미세조정(fine-tune)할 수 있어, 사용자 선호도에 적응 가능

## How

![Figure 3](figures/fig3.webp)
*그림 3: 기계-인-루프 협력과 독립 작성 간의 생성 텍스트 비교 예시*

- **훈련 데이터 구성**: Table 1의 6개 소스(감정 단어, 은유, 의성어 등의 주석이 있는 텍스트)에서 창의적 문장을 수집하고, 주석된 창의적 구간을 BART-Large로 대체하여 일반적 문장을 합성(42,000 학습 쌍)

- **모델 아키텍처**: BART 기반의 시퀀스-투-시퀀스 모델을 활용하여 창의적 문장을 예측하도록 학습

- **상호작용 설계**: 사용자 주도 방식(user-initiative)으로, 사용자가 필요할 때만 모델에 요청 → 모델이 여러 대안 제시 → 사용자가 선택하거나 거절

- **피드백 기반 적응**: 수락된 제안은 목표(창의적) 문장, 거절된 제안은 원본 입력을 목표로 하는 새로운 학습 쌍 생성 및 재훈련

- **재작성 원리**: 전체 텍스트가 아닌 특정 구간만 수정하여 문맥 이탈이나 부조화 문제 완화

## Originality

- **창의적 텍스트 데이터셋 합성**: 기존의 문학적 주석 데이터셋들을 창의적 글쓰기 모델 훈련용으로 재활용하는 독창적 접근법

- **국소적 편집 패러다임**: 전역적 초안 생성이 아닌 국소적 구간 재작성/공백 채우기를 통해 사용자 제어권 확보

- **사용자 그룹 간 영향 분석**: 기술이 능숙한 사용자와 초보 사용자에게 미치는 차별적 영향을 실증적으로 분석하는 사용자 중심 평가

- **실시간 적응 메커니즘**: 상호작용 로그에서 직접 학습하여 사용자 선호도에 동적으로 적응하는 구조

## Limitation & Further Study

- **제한적 평가 대상**: 창의적 이미지 캡션 작성이 실제 창의 글쓰기(시, 소설 등)의 프록시 과제이므로, 더 복잡한 쓰기 과제에서의 효과는 미검증

- **불균등한 효과**: 모델이 능숙한 작가에게 더 도움이 되어 숙련도 격차를 더욱 벌릴 가능성이 있으며, 초보 사용자를 위한 개선 방안 필요

- **이미지 미활용**: 모델이 이미지를 입력으로 활용하지 않아 시각적 맥락을 충분히 활용하지 못함

- **후속 연구**: (1) 초보 사용자를 위한 맞춤형 상호작용 설계, (2) 다양한 창의 글쓰기 장르 확대, (3) 개인화된 어조(tone) 학습, (4) 대규모 사용자 배포 후 장기적 효과 분석

## Evaluation

- **Novelty**: 4/5 – 기존 데이터셋 재활용과 국소적 재작성 패러다임은 새롭지만, 개별 기술 요소는 기존 방법론의 조합

- **Technical Soundness**: 4/5 – 훈련 데이터 합성 방식이 합리적이고 모델 아키텍처는 견고하나, 합성 데이터의 품질에 대한 심층 검증 부족

- **Significance**: 4/5 – 기계-인-루프 글쓰기 시스템의 실용적 기여와 사용자 그룹 간 영향 분석이 의미 있으나, 평가 범위가 제한적

- **Clarity**: 4/5 – 전반적으로 명확하게 작성되었으나, 인터페이스 디자인과 일부 실험 세부사항은 부록에 분산

- **Overall**: 4/5

**총평**: 본 논문은 사용자 제어권을 보장하면서도 창의적 작문을 보조하는 실용적이고 타당한 접근법을 제시하며, 특히 기술이 다양한 사용자 그룹에 미치는 차별적 영향을 분석한 점이 강점입니다. 다만 평가 과제의 제한성과 초보 사용자를 위한 해결책 부재가 향후 개선 과제입니다.

## Related Papers

- 🔄 다른 접근: [[papers/399_Helm_Highlighted_evidence_augmented_language_model_for_enhan/review]] — 창의적 캡션 작성에서 기계-인-루프 방식과 증거 강조 방식의 서로 다른 인간-AI 협업 접근법을 비교할 수 있습니다.
- 🔗 후속 연구: [[papers/708_SciCap_Generating_Captions_for_Scientific_Figures/review]] — 과학적 도형 캡션 생성을 창의적이고 비유적인 표현으로 확장하여 더 풍부한 서술이 가능한 방법을 제시합니다.
- 🏛 기반 연구: [[papers/886_Wordcraft_A_human-ai_collaborative_editor_for_story_writing/review]] — 인간-AI 협업 편집기의 기본 개념이 창의적 이미지 캡션 작성의 기계-인-루프 시스템에 이론적 기반을 제공합니다.
- 🔄 다른 접근: [[papers/399_Helm_Highlighted_evidence_augmented_language_model_for_enhan/review]] — 표 캡션 생성에서 기계-인-루프 접근법과 증거 강조 접근법의 비교 분석이 가능합니다.
