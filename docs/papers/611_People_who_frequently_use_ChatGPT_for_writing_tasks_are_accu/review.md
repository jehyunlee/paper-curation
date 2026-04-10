---
title: "611_People_who_frequently_use_ChatGPT_for_writing_tasks_are_accu"
authors:
  - "Jenna Russell"
  - "Marzena Karpinska"
  - "Mohit Iyyer"
date: "2025.01"
doi: "10.48550/arXiv.2501.15654"
arxiv: ""
score: 4.4
essence: "LLM을 글쓰기 작업에 자주 사용하는 사람들은 특별한 학습 없이도 AI 생성 텍스트를 극도로 정확하게 탐지할 수 있으며, 자동 탐지 시스템보다 훨씬 우수한 성능을 보인다. 본 연구는 300개의 논픽션 기사에 대한 9명의 주석자 분석을 통해 이를 입증한다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Academic_Writing_Personalization"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Russell et al._2025_People who frequently use ChatGPT for writing tasks are accurate and robust detectors of AI-generate.pdf"
---

# People who frequently use ChatGPT for writing tasks are accurate and robust detectors of AI-generated text

> **저자**: Jenna Russell, Marzena Karpinska, Mohit Iyyer | **날짜**: 2025-01-26 | **DOI**: [10.48550/arXiv.2501.15654](https://doi.org/10.48550/arXiv.2501.15654)

---

## Essence

![Figure 1](figures/fig1.webp)
*Figure 1: 인간 전문가의 AI 생성 텍스트 주석 예시 - 판단, 신뢰도 점수, 상세 설명 포함*

LLM을 글쓰기 작업에 자주 사용하는 사람들은 특별한 학습 없이도 AI 생성 텍스트를 극도로 정확하게 탐지할 수 있으며, 자동 탐지 시스템보다 훨씬 우수한 성능을 보인다. 본 연구는 300개의 논픽션 기사에 대한 9명의 주석자 분석을 통해 이를 입증한다.

## Motivation

- **Known**: 자동 AI 텍스트 탐지기는 낮은 탐지율, 패러프레이징/휴머니제이션 같은 회피 전술에 대한 취약성, 설명 가능성 부족 등의 문제를 가진다. 기존 인간 탐지 연구는 대부분 ChatGPT 이전 시대에 수행되었다.

- **Gap**: 최신 LLM(GPT-4o, Claude-3.5-Sonnet, o1-Pro)이 생성한 텍스트, 특히 회피 전술이 적용된 텍스트에 대한 인간의 탐지 능력에 대한 체계적 연구가 부족하다.

- **Why**: AI 생성 텍스트가 학술 표절, 가짜 콘텐츠 생성에 대한 위험성이 증가하고 있으며(위키피디아 5%, PubMed 10%), 자동 시스템의 한계가 명확하므로 인간 탐지자의 역할 재평가가 필요하다.

- **Approach**: 다양한 LLM 배경을 가진 주석자들을 채용하여 5단계 실험(기본 모델 → 패러프레이징 → 휴머니제이션)에서 인간-AI 쌍을 이룬 기사 300개에 주석을 달게 하고, 판단 과정에 대한 상세 설명을 수집한다.

## Achievement

![Figure 2](figures/fig2.webp)
*Figure 2: 전문가 신뢰도는 난이도가 높아질수록 감소하지만 정확도는 유지*

1. **LLM 자주 사용자의 우수한 성능**: LLM을 글쓰기에 자주 사용하는 5명의 "전문가" 주석자의 다수결 투표는 300개 기사 중 단 1개만 오분류(99.67% 정확도). 비교군(LLM을 거의 사용하지 않는 주석자)은 거의 무작위 수준의 성능을 보임.

2. **자동 탐지 시스템 초월**: Pangram 상용 모델을 제외한 거의 모든 오픈소스 탐지기(Binoculars 6.7%, Fast-DetectGPT 23.3%)를 능가. 특히 O1-Pro 휴머니제이션 텍스트 탐지에서 전문가는 100% 정확도, 자동 방식은 심각한 성능 저하.

## How

![Figure 3](figures/fig3.webp)
*Figure 3: 전문가가 언급한 탐지 단서의 범주별 빈도 분포*

- **실험 설계**: 5개 단계별 배치 실험(60개 기사/배치, 30개 인간/30개 AI), 제목-부제를 동일하게 제어한 최소 쌍(minimal pairs) 구성, 피험자 내 설계(within-subjects design)로 개인차 최소화

- **주석 과정**: (1) 이진 판단, (2) 신뢰도 1-5점, (3) 클라우 하이라이트, (4) 단락 길이의 설명 수집

- **생성 전략**: 제목, 부제, 길이, 출판 출처를 지정한 프롬프트로 대응 AI 기사 생성. 실험 3, 5에서는 패러프레이징/휴머니제이션 명시 요청

- **탐지 신호 분석**: 
  - **가장 빈번**: "AI 어휘"(vibrant, crucial, significantly 등)
  - **주요 신호**: 공식적 문장/문서 구조(모호한 도입/결론), 창의성/매력도 부족
  - **보조 신호**: 가식성, 톤, 사실성

- **LLM 모방 실험**: 인간 전문가의 설명으로부터 도출한 가이드북을 LLM에 제공하는 프롬프팅 전략 → 기본 구성에서는 경쟁력 있지만 휴머니제이션에는 약함

## Originality

- 최신 상용 LLM(GPT-4o, Claude-3.5-Sonnet, o1-Pro)에 대한 첫 번째 대규모 인간 탐지 연구

- **LLM 자주 사용자**라는 새로운 인간 주석자 부분집단(population) 식별 및 특성화

- 패러프레이징/휴머니제이션 같은 현실적 회피 전술을 포함한 첫 체계적 연구

- 상세한 자유 형식 설명(paragraph-length explanation) 수집으로 인간 탐지 메커니즘에 대한 정성적 통찰 제공

- 최소 쌍 구성을 통한 엄격한 대조 설계 (내용/주제 혼동 제거)

## Limitation & Further Study

- **도메인 제한**: 영문 논픽션 기사(<1K 단어)만 대상. 과학 논문, 소셜 미디어, 창작 소설 등 다른 도메인으로의 일반화 불명확

- **표본 크기**: 단 5명의 전문가 주석자로 결론 도출. 더 큰 규모의 전문가 풀에서의 성능 재검증 필요

- **회피 전술의 불완전한 제거**: 패러프레이징과 휴머니제이션이 모든 AI 서명을 제거하지 못하므로, 더 강력한 회피 방법의 개발과 대응이 필요

- **LLM 가이드북 성능 격차**: LLM이 가이드북을 따라 인간 수준의 정확도 달성 실패 → 인간 탐지 프로세스의 묵시적 지식 이해 필요

- **후속 연구 방향**:
  - 다양한 도메인, 언어, 긴 텍스트로의 확장
  - 전문가-자동 탐지기 결합 시스템 개발
  - 더 정교한 회피 전술의 효과 분석
  - 전문가 설명으로부터 자동 탐지 특성 추출 방법 개발


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4/5
- Significance: 4.5/5
- Clarity: 4.5/5
- Overall: 4.4/5

**총평**: 현대 LLM 시대에 인간 탐지자의 잠재력을 체계적으로 재평가한 중요한 실증 연구이며, 실무적 가치가 높으나, 도메인과 전문가 표본의 제한성으로 인해 일반화 가능성에 주의가 필요하다.

## Related Papers

- 🏛 기반 연구: [[papers/280_Divergent_llm_adoption_and_heterogeneous_convergence_paths_i/review]] — LLM 사용자의 AI 텍스트 탐지 능력 연구가 학계의 LLM 채택 패턴과 그 영향 분석의 기초 통찰을 제공합니다.
- 🔗 후속 연구: [[papers/093_All_that_glitters_is_not_novel_Plagiarism_in_ai_generated_re/review]] — AI 생성 텍스트 탐지 연구에서 AI 생성 연구 논문의 표절 탐지로 확장하여 더 전문적인 영역의 AI 탐지 문제를 다룹니다.
- 🔄 다른 접근: [[papers/270_Detecting_llm-written_peer_reviews/review]] — ChatGPT 사용자의 탐지 능력과 LLM 작성 동료 검토 자동 탐지라는 서로 다른 AI 생성 텍스트 식별 접근법입니다.
- 🏛 기반 연구: [[papers/478_Large_language_models_penetration_in_scholarly_writing_and_p/review]] — ChatGPT 사용자의 AI 생성 텍스트 탐지 정확도 연구로 LLM 침투도 측정의 기술적 기반을 제공한다.
- 🧪 응용 사례: [[papers/861_Use_of_large_language_models_as_artificial_intelligence_tool/review]] — ChatGPT 사용자의 정확성 인식 연구가 의학 연구자들의 LLM 신뢰도 분석에 적용된다.
- ⚖️ 반론/비판: [[papers/511_LLMs_Outperform_Outsourced_Human_Coders_on_Complex_Textual_A/review]] — ChatGPT 사용자가 더 정확한 글쓰기 능력 평가를 받는다는 연구는 LLM이 모든 텍스트 작업에서 우수하지 않을 수 있음을 시사한다.
- 🏛 기반 연구: [[papers/280_Divergent_llm_adoption_and_heterogeneous_convergence_paths_i/review]] — ChatGPT 사용자들의 AI 텍스트 탐지 능력 연구로서 LLM 채택 패턴 분석의 기초 통찰을 제공합니다.
- 🏛 기반 연구: [[papers/093_All_that_glitters_is_not_novel_Plagiarism_in_ai_generated_re/review]] — AI 생성 텍스트 탐지 연구가 AI 생성 연구 논문의 정교한 표절 탐지 문제의 기초 기술적 배경을 제공합니다.
- 🔗 후속 연구: [[papers/284_Does_writing_with_language_models_reduce_content_diversity_a/review]] — 언어모델 사용이 글쓰기에 미치는 영향을 다양성 감소에서 정확성 인식으로 확장하여 더 포괄적인 사용자 행동 분석을 제공함
- 🏛 기반 연구: [[papers/635_Productivity_assessment_of_neural_code_completion/review]] — ChatGPT 사용자의 글쓰기 정확성 연구가 신경망 코드 완성 도구 사용자의 생산성 평가 방법론에 기초적인 사용자 행동 분석 틀을 제공한다.
