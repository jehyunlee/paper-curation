---
title: "414_Human-llm_coevolution_Evidence_from_academic_writing"
authors:
  - "Mingmeng Geng"
  - "Roberto Trotta"
date: "2025"
doi: "N/A"
arxiv: ""
score: 4.0
essence: "본 논문은 arXiv 논문 초록의 통계적 분석을 통해 인간과 대형언어모델(LLM)의 공진화(coevolution) 현상을 보여준다. 특히 2024년 초 ChatGPT의 과용 단어들이 지적된 직후부터 해당 단어들의 사용 빈도가 급감하는 현상을 발견했으며, 이는 연구자들이 LLM 출력을 의도적으로 수정하고 있음을 시사한다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Academic_Writing_Personalization"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Geng and Trotta_2025_Human-llm coevolution Evidence from academic writing.pdf"
---

# Human-LLM Coevolution: Evidence from Academic Writing

> **저자**: Mingmeng Geng, Roberto Trotta | **날짜**: 2025 | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp)
*arXiv 초록에서 ChatGPT가 선호하거나 비선호하는 단어들의 빈도 변화 추이*

본 논문은 arXiv 논문 초록의 통계적 분석을 통해 인간과 대형언어모델(LLM)의 공진화(coevolution) 현상을 보여준다. 특히 2024년 초 ChatGPT의 과용 단어들이 지적된 직후부터 해당 단어들의 사용 빈도가 급감하는 현상을 발견했으며, 이는 연구자들이 LLM 출력을 의도적으로 수정하고 있음을 시사한다.

## Motivation

- **Known**: ChatGPT 출시(2022년 말) 이후 학술 논문 작성에 LLM의 사용이 급증했으며, "delve", "intricate", "showcasing" 같은 특정 단어들이 LLM이 과도하게 사용하는 특성으로 지적되었음(2024년 4월경)

- **Gap**: 기계생성 텍스트(MGT, Machine-Generated Text) 탐지 기술이 발전하는 반면, 인간이 LLM 출력을 적응적으로 수정하는 현상에 대한 체계적 분석 부족. 단순 이분 분류(human vs. machine) 프레임워크로는 현실의 복합적 상황을 포착할 수 없음

- **Why**: LLM 탐지 기술의 한계가 계속 지적되고 있으며, 실제 학술 텍스트는 인간과 기계 생성 콘텐츠의 혼합물일 가능성이 높음

- **Approach**: 2018-2024년 arXiv 전체 논문(129만여 편) 초록의 월별 단어 빈도 분석을 통해 LLM 특성 단어의 시간적 변화를 추적하고, 기계생성 텍스트 탐지 도구(Binoculars)의 실제 성능을 검증

## Achievement

![Figure 2](figures/fig2.webp)
*2018-2024년 arXiv 초록에서 LLM 사용을 나타내는 단어들의 빈도 변화. (a)Liang et al. 2024b가 지적한 4개 단어, (b)Liang et al. 2024a가 지적한 6개 단어의 평균 빈도 추이*

1. **공진화 현상의 명확한 증거**: "delve", "intricate", "showcasing" 등 LLM 특성 단어는 2024년 3월-4월 이후 급감했으나, "significant", "additionally" 같은 상대적으로 일반적인 단어는 지속적으로 증가 중. 이는 연구자들이 주목받은 단어는 의도적으로 피하지만, 덜 주목받은 단어에는 민감하지 않음을 보여줌

2. **탐지 도구의 실제 한계**: Binoculars 등 최신 MGT 탐지기는 LLM으로 완전히 처리된 텍스트에 대해 통계적으로 유의미한 탐지 능력을 보이지 못함. 2023년 초록과 LLM 처리 초록 간 탐지 점수 차이 미미

3. **프롬프트 조작의 효과성**: LLM에 특정 단어 사용을 피하도록 명시한 프롬프트(P2)는 해당 단어의 빈도를 감소시키지만 완전히 제거하지는 못하며, 탐지기의 성능 변화는 미미함

![Figure 3](figures/fig3.webp)
*컴퓨터과학(CS) 초록과 다른 분야 초록의 단어 빈도 비율 비교. (a)2023년 vs. 2022년 비율, (b)2024년 Q1 vs. 2023-2024년 전체 빈도 비율*

4. **분야 간 확산**: CS 분야에서 더 자주 등장하는 단어들이 다른 학문 분야에서도 빈도가 증가하는 추세, LLM 영향이 학문 전반에 걸쳐 확대되고 있음을 시사

## How

![Figure 4](figures/fig4.webp)
*원본 arXiv 초록과 GPT-4o-mini로 처리한 버전의 단어 빈도 비교. P1: 일반 수정 프롬프트, P2: 특정 단어 금지 프롬프트*

![Figure 5](figures/fig5.webp)
*Binoculars를 이용한 MGT 탐지 결과. 낮은 점수는 기계생성 가능성 높음을 나타냄. (a)실제 논문 초록의 시간별 변화, (b)원본과 LLM 처리 초록 간 비교*

- **데이터 수집**: Kaggle의 arXiv 메타데이터(2018-2024, 약 129만 4천 편) 및 WithdrawArXiv 데이터셋 활용

- **단어 빈도 분석**: 월별로 정규화된 빈도 계산(10,000개 초록 기준), 비율 지표 Rij(T1, T2) = fij(T1)/fij(T2) 도입으로 기간 간 비교 정량화

- **필드별 분석**: 논문 주분류(Primary Category) 기준으로 CS와 기타 분야 분리 비교

- **LLM 처리 실험**: 2018-2025년 각 연도별 처음 1,000편 초록을 GPT-4o-mini(온도 1.0, top-p 0.9)로 처리하여 빈도 변화 관찰

- **탐지기 성능 평가**: Binoculars(SOTA MGT 탐지기) 적용하여 실제 초록과 LLM 처리 초록 간 탐지 성능 검증

## Originality

- **시간적 세분화**: 기존 단순 before/after 비교를 월별 추적으로 확장하여, 정확한 변곡점(2024년 3월-4월) 포착

- **선택적 적응 현상의 발견**: 연구자들이 "인식된" LLM 특성 단어만 선택적으로 회피하는 불완전한 적응 패턴을 실증적으로 보여줌

- **공진화 개념의 경험적 증명**: 인간-AI 상호적응이 추상적 논의가 아닌 구체적인 텍스트 변화로 실증됨

- **탐지기 한계의 실증적 폭로**: SOTA 도구의 이론적 성능과 실제 성능 간 괴리를 정량적으로 입증하고, 프롬프트 조작을 통한 회피 가능성 시연

- **통계적 관점의 대안 제시**: 단편적 텍스트 탐지 불가능성 하에서, 대규모 말뭉치의 빈도 분석을 장기 영향 측정의 실질적 대안으로 제안

## Limitation & Further Study

- **인과성 입증 제한**: 단어 빈도 감소가 명확히 LLM 탐지 논문/리뷰의 영향이라고 완전히 증명되지 않았으며, 대체 원인(새 모델 출시 등)의 가능성 배제 미흡

- **저자 의도 미추적**: 단어 빈도 변화는 관찰되지만, 연구자들이 실제로 의도적으로 수정했는지 또는 우연인지 직접 조사 부재 (설문 없음)

- **혼합 텍스트의 정량화 불가**: 인간-기계 혼합 정도를 정확히 측정할 수 있는 방법론 제시 부족

- **분야 간 세분화 미흡**: CS와 비CS 이분법만 사용하였으며, 물리학, 생물학, 수학 등 분야별 세부 분석 부재

- **후속 연구 방향**:
  - 다양한 LLM 모델(Claude, Gemini 등)의 언어 특성 비교 분석
  - 저자 설문/인터뷰를 통한 의도적 적응 여부 확인
  - 단어 빈도 이외의 문법적, 구조적 특성 분석 (문장 길이, 수동태 빈도, 복잡도 등)
  - 인용 패턴, 논문 수용 여부 등과 LLM 사용의 관계 추적

## Evaluation

- **Novelty**: 4/5 — 공진화 현상의 구체적 증거 제시는 신선하나, LLM 영향 분석 자체는 기존 연구의 연장

- **Technical Soundness**: 3.5/5 — 월별 정규화 빈도 분석은 견고하나, 인과성 입증 논리가 다소 약하고 탐지기 실험은 소수 사례에 제한됨

- **Significance**: 4/5 — MGT 탐지 기술의 근본적 한계를 실증적으로 드러내며, 학술 커뮤니티의 적응 메커니즘 이해에 기여. 정책적 함의 있음

- **Clarity**: 4.5/5 — 명확한 논리 구조와 효과적 시각화. 다만 일부 기술적 세부사항(rolling average 등)이 더 명시적으로 설명되면 좋음

- **Overall**: 4/5

**총평**: 인간과 LLM의 상호적응이라는 흥미로운 현상을 arXiv 대규모 텍스트 데이터로 명확히 증명하며, 현존 탐지 기술의 실질적 한계를 폭로함으로써 MGT 탐지 분야의 재성찰을 촉구하는 가치 있는 연구이다. 다만 인과성과 저자 의도에 대한 직접 증거 부족이 학술적 강도를 다소 제한한다.

## Related Papers

- 🔗 후속 연구: [[papers/444_Is_it_OK_for_AI_to_write_science_papers_Nature_survey_shows/review]] — arXiv 논문 분석을 통한 공진화 현상 발견을 Nature 설문의 AI 사용 윤리 논의로 확장하여 전체적인 변화상을 파악할 수 있습니다.
- 🔄 다른 접근: [[papers/284_Does_writing_with_language_models_reduce_content_diversity_a/review]] — AI 작문 도구 사용이 콘텐츠 다양성에 미치는 영향을 통계적 분석과 실험적 접근법으로 각각 다르게 탐구합니다.
- 🏛 기반 연구: [[papers/796_The_AI_writing_on_the_wall/review]] — 학술 작문에서 AI 사용의 기본적인 현상과 패턴이 인간-LLM 공진화 분석의 이론적 기반을 제공합니다.
- 🔗 후속 연구: [[papers/228_CoAuthor_Designing_a_Human-AI_Collaborative_Writing_Dataset/review]] — 인간-AI 협력 글쓰기 데이터셋 연구가 학술 글쓰기에서 인간과 LLM의 공진화 현상 분석으로 확장되었다
- 🏛 기반 연구: [[papers/641_Prototypical_human-ai_collaboration_behaviors_from_llm-assis/review]] — 인간-LLM 공진화에 대한 학술 글쓰기 증거가 프로토타입적 협력 행동 패턴의 장기적 발전과 상호 적응 과정의 이론적 배경을 제공함
- 🔗 후속 연구: [[papers/227_Closing_the_loop_Learning_to_generate_writing_feedback_via_l/review]] — 인간-LLM 협력 글쓰기의 일반적 패턴을 교육적 맥락으로 확장하여 피드백 생성에 특화된 방법론을 개발함
- 🏛 기반 연구: [[papers/444_Is_it_OK_for_AI_to_write_science_papers_Nature_survey_shows/review]] — arXiv 분석을 통한 실증적 공진화 증거가 Nature 설문의 AI 사용 윤리 논의에 데이터 기반 근거를 제공합니다.
- 🔗 후속 연구: [[papers/900_ChatGPT_has_entered_the_classroom_how_LLMs_could_transform_e/review]] — 교육 분야 LLM 적용을 인간-AI 협력적 글쓰기로 확장하여 실제 교육 현장의 변화를 보여준다
- 🏛 기반 연구: [[papers/607_Patterns_and_purposes_A_cross-journal_analysis_of_ai_tool_us/review]] — 인간-LLM 협력적 글쓰기의 진화 과정에서 AI 도구 사용 패턴의 기초 데이터를 제공한다
- 🏛 기반 연구: [[papers/565_Multi-novelty_Improve_the_diversity_and_novelty_of_contents/review]] — 인간-LLM 협력에서 콘텐츠 다양성 확보의 기술적 기초를 제공한다
