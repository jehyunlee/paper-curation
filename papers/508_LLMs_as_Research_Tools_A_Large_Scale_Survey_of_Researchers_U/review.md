---
title: "508_LLMs_as_Research_Tools_A_Large_Scale_Survey_of_Researchers_U"
authors:
  - "Zhehui Liao"
  - "Maria Antoniak"
  - "Inyoung Cheong"
  - "Evie Yu-Yen Cheng"
  - "Ai-Heng Lee"
date: "2024.10"
doi: "10.48550/arXiv.2411.05025"
arxiv: ""
score: 4.0
essence: "대규모 검증된 논문 저자 816명을 대상으로 LLM(Large Language Model)의 연구 활용 현황과 인식을 조사한 첫 대규모 실증 연구로, 연구자의 인구통계학적 배경에 따른 사용 양식과 윤리 인식의 차이를 드러냈다."
tags:
  - "cat/Cognitive_AI_Evaluation_and_Benchmarking"
  - "sub/Cognitive_LLM_Evaluation"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Liao et al._2024_LLMs as Research Tools A Large Scale Survey of Researchers' Usage and Perceptions.pdf"
---

# LLMs as Research Tools: A Large Scale Survey of Researchers' Usage and Perceptions

> **저자**: Zhehui Liao, Maria Antoniak, Inyoung Cheong, Evie Yu-Yen Cheng, Ai-Heng Lee, Kyle Lo, Joseph Chee Chang, Amy X. Zhang | **날짜**: 2024-10-30 | **DOI**: [10.48550/arXiv.2411.05025](https://doi.org/10.48550/arXiv.2411.05025)

---

## Essence

대규모 검증된 논문 저자 816명을 대상으로 LLM(Large Language Model)의 연구 활용 현황과 인식을 조사한 첫 대규모 실증 연구로, 연구자의 인구통계학적 배경에 따른 사용 양식과 윤리 인식의 차이를 드러냈다.

## Motivation

- **Known**: 생성형 AI 도구(ChatGPT 등)의 급속한 확산으로 많은 연구자들이 이미 LLM을 연구 workflow에 도입하고 있으며, 소규모 인터뷰·설문 연구에서 긍정적 사용 사례가 보고되고 있다.

- **Gap**: 기존 연구는 특정 분야에 한정되거나 소규모(N=20-72)이었으며, 연구자의 LLM 사용 방식, 사용 동기, 인식 차이에 관한 대규모 정량적 증거가 부족했다. 또한 인구통계학적 배경에 따른 사용 양식과 윤리 우려도의 차이가 충분히 규명되지 않았다.

- **Why**: LLM이 연구 생산성 향상, 연구 형평성 개선의 가능성을 제시하는 한편, 투명성, 재현성, 표절, 데이터 조작, 기술 저하 등 새로운 윤리적 위험을 초래할 수 있다. 집단 간 인식 차이가 입양 격차를 심화시켜 기존의 학술 불평등을 악화시킬 수 있다.

- **Approach**: Semantic Scholar에서 다양한 분야, 인구통계학적 배경, 경력 단계의 검증된 논문 저자 816명을 모집하여 LLM 사용 방식(정보 탐색, 편집, 아이디어 생성, 직접 작성, 데이터 정제/분석, 데이터 생성), 인식(위험, 이점, 윤리, 공개 의향), 인구통계학적 배경(인종, 성별, 영어 모국어 여부, 경험, 분야)의 관계를 설문 조사로 분석했다.

## Achievement

![Figure 2](figures/fig2.webp)
*각 사용 유형별 사용 빈도 분포 (N=816). 정보 탐색과 편집이 가장 자주 보고되고, 데이터 분석과 생성이 가장 적게 보고됨*

1. **광범위한 LLM 도입**: 응답자의 81%가 연구 workflow의 한 곳 이상에서 LLM을 사용 중이며, 정보 탐색과 편집(Information Seeking & Editing)이 가장 빈번하게 보고되고 데이터 분석 및 생성이 가장 적게 보고되었다.

2. **인구통계학적 격차와 형평성 기회**: 소수인종(non-White), 비모국어 영어 사용자, 초급 연구자들이 LLM을 더 자주 사용하며 이점을 더 높게 평가하는 반면, 여성, 논바이너리, 경력이 많은 연구자들은 윤리 우려가 더 크다. 이는 전통적으로 학술에서 소외된 집단의 형평성 개선 가능성을 시사하는 한편, 다른 집단의 낮은 채택률로 인한 새로운 불평등 위험을 경고한다.

![Figure 4](figures/fig4.webp)
*인구통계학적 특성별 LLM 사용 및 인식 현황. 각 히트맵은 사용 빈도, 위험 인식, 이점 평가, 윤리 우려, 공개 의향의 차이를 보여줌*

3. **분야별 규범 차이**: 컴퓨터과학 연구자들이 다른 분야 연구자들보다 LLM 사용 공개에 더 편안하고 윤리 우려가 낮다. 이는 각 분야마다 서로 다른 사회적 규범 형성이 필요함을 시사한다.

4. **LLM 출처 선호도**: 연구자들은 영리 기업의 상용 모델보다 오픈소스/비영리 LLM을 선호하는데, 이는 기존 대규모 상용 기업의 데이터 프라이버시, 투명성, 접근성 관련 우려 때문이다.

## How

![Figure 3](figures/fig3.webp)
*각 LLM 사용 유형별 참여자 수 분포. 정보 탐색이 가장 많은 참여자가 수행하는 작업임을 보여줌*

**조사 설계 및 분석 방법**:
- 검증된 논문 저자를 Semantic Scholar에서 모집하여 표본의 신뢰성 확보
- 6가지 LLM 사용 유형(정보 탐색, 편집, 아이디어 생성, 직접 작성, 데이터 정제/분석, 데이터 생성)과 4가지 인식 차원(위험, 이점, 윤리, 공개 의향)을 측정
- 5가지 인구통계학적 특성(인종, 성별, 영어 모국어 여부, 경력 단계, 분야)별 분석
- 정량적 분석: 빈도분석, 교차분석, 카이제곱 검정 및 다중 비교 보정
- 정성적 분석: 자유 응답 코딩 및 주제 분석(thematic analysis)
- 공개 설문 공시(GitHub 공개): 개인식별 정보 제거 후 학술 재사용 허용

**Figure 1의 설문 구조**:
- 참가자의 인구통계학적 정보, 6가지 사용 유형별 빈도, 각 사용 유형에 대한 인식(위험/이점/윤리) 평가, LLM 출처별 선호도, 피어/리뷰어 공개 의향

## Originality

- **첫 대규모 검증된 저자 설문**: 기존 N=20-72의 소규모 인터뷰/설문과 달리, 다양한 분야의 검증된 논문 저자 816명을 포함한 첫 대규모 양적 조사로, 추측(speculation)에 의존하던 기존 연구의 경험적 공백을 채움

- **인구통계학적 교차 분석의 심화**: 단순 인종/성별 분석을 넘어 영어 모국어 여부, 경력 단계, 분야, 출처(영리/비영리)의 교차 영향을 체계적으로 분석하여 집단 간 불평등의 다층성을 드러냄

- **형평성 관점의 재구성**: LLM 도입을 단순 생산성 증대가 아닌 학술 형평성 문제로 프레임화하여, 기존 소외 집단의 이점과 신규 차별 위험을 동시에 조명

- **사회적 규범 형성의 필요성 강조**: 필드별 LLM 인식 차이를 단순 수용/거절의 이분법이 아닌, 각 분야 내 규범 형성 과정으로 개념화

## Limitation & Further Study

- **자기 보고(self-report) 편향**: 응답자의 자가 평가에 의존하므로, 실제 사용 행동과 인식의 불일치 가능성이 있으며, 사회적 바람직성(social desirability bias) 영향을 배제할 수 없다.

- **표본 대표성 제한**: Semantic Scholar 사용자 중 설문 응답에 동의한 자들에 한정되어, 비디지털 접근 연구자나 저명도 낮은 연구자의 대표성 부족 가능성이 있다.

- **인과성 규명 부재**: 횡단면 설계로 인해 인구통계학적 배경이 LLM 사용을 초래하는지, 아니면 LLM 사용자가 특정 배경을 선택하는지의 인과 방향을 파악할 수 없다.

- **시간적 변화 미추적**: 2024년 현황만 조사하므로, LLM 기술 진화에 따른 인식 변화 추이를 추적하지 못했다. 향후 종단 설계(longitudinal survey)로 규범 형성 과정의 동적 변화를 추적할 필요가 있다.

- **분야별 심화 분석 부족**: 컴퓨터과학과 타 분야의 규범 차이를 확인했으나, 각 분야 내부의 세부 학문 간 차이나 분야별 특수성을 고려한 심층 인터뷰는 제한적이다.

- **개입 효과 미측정**: LLM 사용의 실제 연구 품질, 효율성, 창의성 영향에 관한 객관적 지표가 부재하므로, 인식과 실제 효과의 불일치 가능성을 검증해야 한다.

## Evaluation

- **Novelty(독창성)**: 4.5/5 — 대규모 검증된 저자 설문이라는 방법론 신규성과 형평성 관점의 재구성은 뛰어나나, LLM 사용 유형의 분류나 위험 카테고리가 기존 소규모 연구를 확장한 수준으로 개념적 혁신은 제한적

- **Technical Soundness(기술 건전성)**: 4/5 — 표본 모집, 설문 설계, 통계 분석이 충실하고 공개 공시로 재현성을 확보했으나, 자기 보고 편향 제어 및 인과 추론의 엄밀성이 부족하며, 다중 비교 보정(Bonferroni correction) 적용 여부가 명시되지 않은 부분이 있다.

- **Significance(중요성)**: 4.5/5 — LLM 기반 연구 도구의 실제 도입 현황과 인구통계학적 격차를 최초로 정량화하여, 정책 수립, 도구 설계, 윤리 논의의 경험적 근거를 제공한다. 특히 형평성 우려는 학술 공동체가 즉시 대응해야 할 중요 이슈다.

- **Clarity(명확성)**: 4.5/5 — 명확한 연구 질문, 체계적인 결과 제시, 풍부한 시각화(히트맵, 발산 막대 차트)로 복잡한 교차 분석을 효과적으로 전달했으나, 자유 응답의 정성적 분석 결과(코딩 스킴, 주제)가 본문 초반 15,000자에 제시되지 않아 정성 기여도를 온전히 평가하기 어렵다.

- **Overall(종합)**: 4/5

**총평**: 본 연구는 LLM의 학술 도입을 단순 기술 채택 문제가 아닌 연구 형평성 문제로 재프레임화하며, 816명의 검증된 저자를 조사한 첫 대규모 실증 자료를 제공한다. 인구통계학적 격차의 발견은 학술 공동체의 주목할 만한 성과이나, 자기 보고 편향과 인과성 규명 부재 등 방법론적 한계는 다음 단계 종단 또는 실험 설계 연구로 보완되어야 한다.

## Related Papers

- 🏛 기반 연구: [[papers/064_Agentic_AI_for_Scientific_Discovery_A_Survey_of_Progress_Cha/review]] — 과학 연구를 위한 에이전틱 AI의 종합적 조사가 연구자들의 LLM 사용 현황 조사의 이론적 맥락을 제공한다.
- 🔗 후속 연구: [[papers/410_How_deep_do_large_language_models_internalize_scientific_lit/review]] — LLM이 과학 문헌을 얼마나 깊이 내재화하는지에 대한 연구가 연구자들의 LLM 활용 방식 이해를 확장한다.
- 🧪 응용 사례: [[papers/607_Patterns_and_purposes_A_cross-journal_analysis_of_ai_tool_us/review]] — AI 도구 사용의 패턴과 목적에 대한 학술지 간 분석이 연구자 LLM 사용 조사의 실제 적용 결과이다.
- ⚖️ 반론/비판: [[papers/824_Towards_AI_for_science_developing_a_conceptual_basis_for_tra/review]] — 연구자들의 LLM 활용 실태 조사가 도서관 서비스 모델의 한계점을 지적한다.
- 🧪 응용 사례: [[papers/064_Agentic_AI_for_Scientific_Discovery_A_Survey_of_Progress_Cha/review]] — 연구자들의 LLM 사용 현황 조사가 과학 발견을 위한 에이전틱 AI 시스템의 실제 도입과 활용을 보여주는 구체적인 사례이다.
- 🏛 기반 연구: [[papers/074_AI_for_research_the_ultimate_guide_to_choosing_the_right_too/review]] — 연구자들의 LLM 사용에 대한 대규모 조사가 올바른 도구 선택 가이드의 실증적 근거를 제공한다.
- 🏛 기반 연구: [[papers/875_What_are_the_best_AI_tools_for_research_Natures_guide/review]] — 연구자들의 LLM 활용에 대한 대규모 설문 조사가 AI 도구 가이드 작성에 필요한 실제 사용 패턴과 요구사항을 파악하는 기초 데이터를 제공한다.
- 🔗 후속 연구: [[papers/912_Science_and_the_new_age_of_AI/review]] — 연구자들의 AI 도구 사용 현황을 더 광범위한 설문을 통해 확장 조사한다
