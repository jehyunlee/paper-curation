---
title: "656_Read_revise_repeat_A_system_demonstration_for_human-in-the-l"
authors:
  - "Wanyu Du"
  - "Zae Myung Kim"
  - "Vipul Raheja"
  - "Dhruv Kumar"
  - "Dongyeop Kang"
date: "2022"
doi: "N/A"
arxiv: ""
score: 4.2
essence: "본 논문은 인간 피드백을 통합한 반복적 텍스트 개정 시스템 R3(Read, Revise, Repeat)을 제시한다. 사용자가 모델의 편집 제안을 수용/거절하며 상호작용하는 방식으로 고품질 텍스트 개정을 달성한다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Self-Refining_Text_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Corradini et al._2022_Read, revise, repeat A system demonstration for human-in-the-loop iterative text revision.pdf"
---

# Read, Revise, Repeat: A System Demonstration for Human-in-the-Loop Iterative Text Revision

> **저자**: Wanyu Du, Zae Myung Kim, Vipul Raheja, Dhruv Kumar, Dongyeop Kang | **날짜**: 2022 | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp) *R3 시스템의 인간-기계 협력적 반복 텍스트 개정 파이프라인*

본 논문은 인간 피드백을 통합한 반복적 텍스트 개정 시스템 R3(Read, Revise, Repeat)을 제시한다. 사용자가 모델의 편집 제안을 수용/거절하며 상호작용하는 방식으로 고품질 텍스트 개정을 달성한다.

## Motivation

- **Known**: 대규모 언어모델(LLM)은 일회성(one-shot) 텍스트 개정 작업에서 우수한 성능을 보임
- **Gap**: 기존 신경망 기반 개정 시스템들은 인간 작문의 반복적(iterative) 특성과 사용자 피드백을 고려하지 않음. 반복적으로 적용한 일회성 모델은 노이즈 편집을 생성하여 사용자 부담 증가
- **Why**: 실제 인간 작가는 동시에 여러 제약(내용 커버리지, 언어 규범, 담화 관례 등)을 처리할 수 없어 반복적으로 개정함. 따라서 각 반복 단계에서 인간 피드백으로 해로운 편집을 필터링하면 더 높은 품질의 개정이 가능
- **Approach**: 인간-기계 협력 인터페이스를 통해 사용자가 모델의 편집 제안(edit intention 포함)을 승인/거절하고, 승인된 편집만 다음 반복 단계에 통합

## Achievement

![Figure 2](figures/fig2.webp) *R3의 사용자 인터페이스: (a) 로그인, (b) 가이드라인, (c) 문서 선택, (d) 편집 제안 및 상호작용 패널*

1. **반복적 개정의 해석성과 제어성 향상**: 편집 의도(fluency, coherence, clarity, style)를 명시적으로 표시하여 사용자에게 세밀한 통제권 제공. 이미 고품질인 부분은 재검토할 필요가 없어 인지 부하 감소

2. **효율성 증대**: 인간-기계 상호작용이 더 적은 반복 횟수와 편집으로 높은 품질의 개정 달성. 실증 실험에서 R3의 편집 수용률(acceptance rate)이 초기 개정 깊이(revision depth)에서 인간 작가 수준과 유사

3. **최초의 협력형 반복 개정 시스템**: 기존 일회성 방식의 개정 시스템과 달리 반복적 협력을 지원하는 최초의 실용적 시스템 구현

## How

- **편집 의도 식별 모델(Edit Intention Identification Models)**: 
  - 1단계: 편집 필요 여부를 이진 분류(edit-prediction classifier)
  - 2단계: 필요한 편집 유형 분류(edit-intention classifier) → 4개 카테고리(FLUENCY, COHERENCE, CLARITY, STYLE)

- **텍스트 개정 생성 모델(Text Revision Generation Model)**: 
  - PEGASUS 기반 사전학습 모델을 수집 데이터셋으로 미세조정
  - 원문 문장 + 예측된 편집 의도 → 개정된 문장 생성
  - latexdiff와 difflib로 모든 편집 추출

- **사용자 상호작용 플로우**:
  - 각 반복 깊이 t에서 시스템이 제안된 편집과 의도 제시
  - 사용자가 수용/거절 결정
  - 수용된 편집을 다음 반복에 통합
  - 최대 반복 깊이 도달 또는 추가 편집 부재 시 종료

## Originality

- 기존 연구와 달리 인간 피드백을 각 반복 단계에 통합하여 누적 노이즈 문제 해결
- 문서 수준의 반복적 다중 편집을 지원(기존: 일회성 문장 수준 변환)
- 편집 의도 명시화로 해석 가능성과 사용자 제어성을 동시에 달성
- HCI(Human-Computer Interaction) 관점에서 반복적 협력 시스템의 효과성을 체계적으로 평가

## Limitation & Further Study

- 실험 규모: 제시된 본문에서 RQ1-RQ3 설정만 언급되고 결과 분석이 불완전함
- 모델 아키텍처: PEGASUS 기반 상대적으로 기본적인 생성 모델 사용
- 평가 기준: 수용률(acceptance rate)만으로는 개정 품질의 충분한 평가 어려움. 일관성(consistency), 문법성(grammaticality) 등 다각적 평가 필요
- 문서 길이: 실험 범위(문서 길이, 도메인 등) 제한 가능성
- 향후: (1) 더 고급 모델 아키텍처 적용, (2) 다양한 도메인/작문 스타일 확대, (3) 최소 인간 노력으로 최대 품질 달성하는 최적화 알고리즘 개발

## Evaluation

- **Novelty**: 4.5/5 - 반복적 협력 개정 시스템의 최초 구현이나 기술 혁신은 제한적
- **Technical Soundness**: 4/5 - 견실한 방법론이나 상대적으로 기본적인 모델 기반. 평가 프로토콜 명확화 필요
- **Significance**: 4/5 - 실용적 쓰기 보조 도구로서 높은 가치. 학술적으로는 HCI 중심 기여
- **Clarity**: 4/5 - 전반적으로 명확하나 실험 결과 분석 부분이 본문에서 미완성
- **Overall**: 4.2/5

**총평**: 인간 피드백을 반복 단계마다 통합하여 개정 품질과 사용 경험을 동시에 개선하는 실용적 시스템이나, 기술적 독창성은 제한적이며 평가의 깊이를 심화할 필요가 있다.

## Related Papers

- 🔄 다른 접근: [[papers/227_Closing_the_loop_Learning_to_generate_writing_feedback_via_l/review]] — 둘 다 인간-AI 협력 글쓰기를 다루지만 하나는 직접적 인간 피드백, 다른 하나는 학생 시뮬레이터 기반 접근임
- 🏛 기반 연구: [[papers/791_Text_editing_by_command/review]] — 자연어 명령을 통한 텍스트 편집의 기초적 접근이 인간 피드백 기반 반복적 텍스트 개정 시스템의 이론적 토대를 제공함
- 🔗 후속 연구: [[papers/886_Wordcraft_A_human-ai_collaborative_editor_for_story_writing/review]] — 기본적인 인간-AI 협력 글쓰기를 반복적 개정과 피드백 통합을 통한 더 정교한 협력 편집 시스템으로 확장함
- 🔄 다른 접근: [[papers/227_Closing_the_loop_Learning_to_generate_writing_feedback_via_l/review]] — 둘 다 인간-AI 협력 글쓰기를 다루지만, 하나는 학생 시뮬레이터 기반 피드백, 다른 하나는 직접적 인간 피드백 방식임
- 🔗 후속 연구: [[papers/791_Text_editing_by_command/review]] — 자연어 명령 기반 텍스트 편집을 인간 피드백과 통합한 더 발전된 대화형 편집 시스템으로 확장함
- 🔄 다른 접근: [[papers/272_Diamonds_in_the_rough_Generating_fluent_sentences_from_early/review]] — 인간-루프 반복 시스템으로 본 논문의 자동 수정과 다른 접근법인 인간 참여형 수정을 제시한다.
