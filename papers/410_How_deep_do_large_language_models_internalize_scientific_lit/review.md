---
title: "410_How_deep_do_large_language_models_internalize_scientific_lit"
authors:
  - "Andres Algaba"
  - "Vincent Holst"
  - "Floriano Tori"
  - "Melika Mobini"
  - "Brecht Verbeken"
date: "2025"
doi: "N/A"
arxiv: ""
score: 4.2
essence: "대규모 언어 모델(LLM)이 과학 논문의 참고문헌 생성 시 이미 인용도가 높은 논문들을 지속적으로 선호함으로써 인용의 마태 효과(Matthew effect)를 강화하며, 이는 학문 영역 간 편향의 차이에도 불구하고 일관되게 나타난다. 이러한 현상은 과학 지식의 발견과 확산 방식을 재형성할 가능성이 있다."
tags:
  - "cat/Academic_Peer_Review_Automation"
  - "sub/AI_Publishing_Trends"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Algaba et al._2025_How deep do large language models internalize scientific literature and citation practices arXiv pr.pdf"
---

# How deep do large language models internalize scientific literature and citation practices? arXiv preprint arXiv:2504.02767, 2025.

> **저자**: Andres Algaba, Vincent Holst, Floriano Tori, Melika Mobini, Brecht Verbeken, Sylvia Wenmackers, Vincent Ginis | **날짜**: 2025 | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp)
*그림 1: 논문의 제목, 저자, 연도, 학술지, 초록을 기반으로 LLM이 생성한 참고문헌과 인간의 인용 패턴을 비교하는 실험 개요*

대규모 언어 모델(LLM)이 과학 논문의 참고문헌 생성 시 이미 인용도가 높은 논문들을 지속적으로 선호함으로써 인용의 마태 효과(Matthew effect)를 강화하며, 이는 학문 영역 간 편향의 차이에도 불구하고 일관되게 나타난다. 이러한 현상은 과학 지식의 발견과 확산 방식을 재형성할 가능성이 있다.

## Motivation

- **Known**: LLM은 수학 문제 해결, 코드 생성 등에서 뛰어난 성능을 보이며, 과학 연구에 빠르게 도입되고 있다. 과학 논문은 최근성(recency) 선호, 짧은 제목 선호, 저명한 학술지 선호 등 다양한 인용 편향을 보이고, 이는 학문 영역에 따라 상이하다.

- **Gap**: LLM이 인간의 인용 관행과 얼마나 일치하는지, 학문 영역별 성능 차이, 기존 인용 동학에 미칠 영향에 대해 명확하지 않다. 특히 LLM의 매개변수 지식(parametric knowledge)만으로 생성한 참고문헌 추천이 어떤 편향을 띠는지 체계적으로 분석된 바가 없다.

- **Why**: LLM이 과학 종합(scientific synthesis)에 점점 더 통합될수록, 그들이 어떻게 과학적 지식 발견과 확산을 형성하는지 이해하는 것이 중요하다. 자동화 편향(automation bias)으로 인해 LLM의 제안이 연구자의 선행 연구 발견 과정을 왜곡할 수 있다.

- **Approach**: SciSciNet 데이터베이스에서 1999-2021년 Q1 학술지의 10,000개 논문을 표본 추출하고, GPT-4o에 각 논문의 초록 정보를 기반으로 참고문헌 생성을 요청(총 274,951개 참고문헌). 생성된 참고문헌의 특성(발행년, 저자 수, 제목 길이, 인용도 등)을 인간이 작성한 참고문헌과 비교 분석.

## Achievement

![Figure 3](figures/fig3.webp)
*그림 3: 학문 영역과 시간에 따른 생성 참고문헌의 존재율(existence rate) 및 인용 특성 비교*

1. **마태 효과의 강화(Matthew effect reinforcement)**: LLM이 생성한 참고문헌 중 실제로 존재하는 참고문헌들(existence rate 42.6%)은 인간의 참고문헌 대비 현저히 높은 중앙값 인용도를 보임. 이는 이미 인용도 높은 논문이 더욱 많은 추가 인용을 받는 누적 우위 현상을 의미하며, 모든 학문 영역과 시간 기간에 걸쳐 일관되게 관찰됨.

2. **학문 영역별 편차**: 인문학과 사회과학에서는 40-50%의 높은 존재율을 보이는 반면, 정확한 과학(exact sciences)에서는 더 낮은 존재율을 나타냄. 이는 인문학과 사회과학이 더 오래된 참고문헌을 인용하는 경향과 관련됨.

3. **체계적인 인용 편향**: LLM은 더 최근의 참고문헌(더 짧은 제목, 더 많은 저자)을 선호하며, 이는 인간의 인용 패턴과 일부 차이를 보임. 의미론적 유사성(textual embedding) 분석 결과, 생성된 참고문헌의 의미적 적절성은 인간의 참고문헌과 비교할 수 있는 수준이나, 네트워크 특성에서는 저자 자기인용을 감소시킴.

## How

![Figure 4](figures/fig4.webp)
*그림 4: 생성된 참고문헌의 체계적 편향 - 발행연도, 저자 수, 제목 길이 선호도*

- **데이터 수집**: SciSciNet에서 Q1 저널 논문 10,000개 선별(조건: 1999-2021년 발행, 3-54개 참고문헌, 최소 1회 이상 인용, 유효한 DOI와 초록 보유)

- **LLM 쿼리**: "다음 논문의 제목, 저자, 연도, 학술지, 초록이 주어졌을 때, 이 논문과 관련 있는 n개의 참고문헌을 제시하세요"

- **검증**: Fuzzy matching을 통해 생성된 참고문헌의 존재 여부를 SciSciNet에서 검증(보수적 임계값 적용으로 실제 존재율 저추정 가능성)

- **비교 분석**: 생성 참고문헌과 인간 참고문헌의 인용도, 발행연도, 저자 수, 제목 길이, 의미적 임베딩(cosine similarity), 네트워크 특성(citation network) 비교

- **통계 분석**: 초점 논문(focal paper) 수준에서 Wilcoxon signed-rank 검정 수행

## Originality

- 기존 LLM 벤치마크(fact verification, literature review writing, in-text citation)와 달리 **초록 기반의 참고문헌 생성**이라는 보다 현실적인 시나리오 설정

- **매개변수 지식만 활용**한 LLM 평가로 검색/검색증강생성(RAG) 기반 접근과 구분하여 LLM의 내재적 편향 분석

- **마태 효과의 강화**를 체계적으로 정량화한 첫 대규모 실증 연구(274,951개 참고문헌, 10,000개 논문)

- 단순 존재 여부를 넘어 **의미론적 적절성, 네트워크 특성, 학문 영역별 편차**를 종합적으로 분석

- 실제 과학 지식 확산 메커니즘에 미칠 영향에 대한 **정책적 함의** 제시

## Limitation & Further Study

- **실험 환경의 제한성**: 현실의 LLM 활용은 외부 데이터 검색, 사용자와의 상호작용을 포함하나, 본 연구는 순수 매개변수 지식만 평가. 따라서 실제 운영 환경에서의 영향은 다를 수 있음.

- **존재율 저추정 가능성**: Fuzzy matching의 보수적 임계값으로 인해 실제 존재하는 참고문헌의 일부가 누락되었을 가능성

- **학문 영역 대표성 편향**: 정확한 과학(특히 의학, 생물학, 화학)에 편중된 표본으로 인문학과 사회과학 결과의 일반화 한계

- **시간 범위 제한**: 1999-2021년으로 제한되어 최근 LLM 발전에 따른 인용 동학 변화 미포착. 최신 모델(GPT-4o 이후)과의 비교 필요

- **후속 연구**: (1) 검색 기능을 활성화한 LLM의 인용 패턴 변화 분석, (2) 실제 연구자의 LLM 활용 추적 연구, (3) 다양한 LLM 모델 간 비교, (4) 인용 피드백 루프의 장기 시뮬레이션, (5) 학문 영역별 미세한 편향 분석

## Evaluation

- **Novelty**: 4.5/5 — LLM의 내재적 인용 편향을 대규모로 분석한 첫 연구이며, 마태 효과 강화라는 구체적 발견이 새로움. 다만 기술적으로는 기존 방법론의 조합.

- **Technical Soundness**: 4/5 — 방법론은 견고하고 통계 검정이 적절하나, fuzzy matching의 보수성으로 인한 존재율 저추정 가능성과 표본 편향(정확한 과학 과다 표현) 개선 필요.

- **Significance**: 4.5/5 — 과학 커뮤니티의 지식 발견 방식과 출판 동학에 미칠 실질적 영향이 크며, LLM 통합의 잠재적 위험을 명확히 제시. 정책 수립에 근거 제공.

- **Clarity**: 4/5 — 대체로 명확하고 체계적이나, 일부 기술적 세부사항(fuzzy matching 임계값, 통계 검정 결과)이 부록으로만 제시되어 본문 가독성 개선 여지 있음.

- **Overall**: 4.2/5

**총평**: 본 논문은 LLM이 과학 참고문헌 생성 시 체계적으로 마태 효과를 강화하며 인간의 인용 관행과 차이를 보인다는 중요한 발견을 대규모 실증 데이터로 제시하여, AI 도입이 과학적 지식 발견의 형태를 재편할 수 있음을 시사한다. 다만 순수 매개변수 지식 기반 평가라는 제한과 학문 영역 표본 편향을 고려할 때, 실제 운영 환경에서의 영향은 추가 검증이 필요하다.

## Related Papers

- 🔄 다른 접근: [[papers/373_Generalization_Bias_in_Large_Language_Model_Summarization_of/review]] — LLM의 과학 요약에서 일반화 편향을 다루어 인용 편향과 함께 LLM의 과학 문헌 처리 한계를 보완적으로 이해할 수 있다.
- 🔗 후속 연구: [[papers/478_Large_language_models_penetration_in_scholarly_writing_and_p/review]] — 학술 저술에서 LLM 사용 추세 분석의 한 부분으로 참고문헌 생성 시 편향 패턴을 실증적으로 입증한다.
- 🏛 기반 연구: [[papers/460_Language_models_surface_the_unwritten_code_of_science_and_so/review]] — 언어 모델이 과학과 사회의 암묵적 코드를 드러내는 연구로 마태 효과 강화 현상의 이론적 배경을 제공한다.
- 🔄 다른 접근: [[papers/373_Generalization_Bias_in_Large_Language_Model_Summarization_of/review]] — LLM이 과학 문헌을 내재화하는 방식의 편향을 다루어 일반화 편향과 함께 종합적 이해가 필요하다.
- 🔄 다른 접근: [[papers/478_Large_language_models_penetration_in_scholarly_writing_and_p/review]] — LLM이 과학 문헌을 내재화하는 방식과 함께 학술 워크플로우 전반의 LLM 영향을 종합적으로 이해할 수 있다.
- 🔗 후속 연구: [[papers/508_LLMs_as_Research_Tools_A_Large_Scale_Survey_of_Researchers_U/review]] — LLM이 과학 문헌을 얼마나 깊이 내재화하는지에 대한 연구가 연구자들의 LLM 활용 방식 이해를 확장한다.
