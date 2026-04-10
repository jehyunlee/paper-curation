---
title: "179_Can_ai_replace_human_subjects_a_large-scale_replication_of_p"
authors:
  - "Ziyan Cui"
  - "Ning Li"
  - "Huaikang Zhou (Tsinghua University)"
date: "2024"
doi: "미제공"
arxiv: ""
score: 4.0
essence: "대규모 심리학 실험 156개를 GPT-4, Claude 3.5 Sonnet, DeepSeek v3 등 3개의 최신 LLM으로 재현한 결과, LLM은 주효과 73-81%의 높은 재현율을 보이지만 인종, 성별 등 사회적으로 민감한 주제에서는 현저히 낮은 성과를 보였으며, 효과크기가 인간 연구보다 2-3배 크다는 체계적 편차를 드러냈다."
tags:
  - "cat/LLM-Based_Scientific_Reasoning"
  - "sub/Scientific_Literature_Analysis"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Kessler et al._2024_Can ai replace human subjects a large-scale replication of psychological experiments with llms.pdf"
---

# Can AI Replace Human Subjects? A Large-Scale Replication of Psychological Experiments with LLMs

> **저자**: Ziyan Cui, Ning Li, Huaikang Zhou (Tsinghua University) | **날짜**: 2024 | **DOI**: [미제공]

---

## Essence

![Figure 2](figures/fig2.webp) *주요 특성별 주효과(Main Effects) 재현율 비교*

대규모 심리학 실험 156개를 GPT-4, Claude 3.5 Sonnet, DeepSeek v3 등 3개의 최신 LLM으로 재현한 결과, LLM은 주효과 73-81%의 높은 재현율을 보이지만 인종, 성별 등 사회적으로 민감한 주제에서는 현저히 낮은 성과를 보였으며, 효과크기가 인간 연구보다 2-3배 크다는 체계적 편차를 드러냈다.

## Motivation

- **Known**: 초기 연구들은 LLM이 심리학적 평가와 경제적 의사결정 시뮬레이션에서 혼재된 결과를 보여주고 있으며, 일부는 LLM-인간 반응의 높은 일치도를 보고하는 반면 다른 연구는 개인 수준의 행동과 특정 인구통계학적 프로필 시뮬레이션에서 현저한 차이를 드러냄
  
- **Gap**: 기존 연구들은 제한된 수의 자의적으로 선정된 실험에만 의존하여 다양한 심리 현상과 실험 조건에 걸친 LLM의 능력에 대한 포괄적 결론을 도출하기 어려움. 사회적으로 민감한 주제(인종, 성별, 윤리)에서 LLM과 인간 반응 간의 체계적 차이에 대한 이해 부족

- **Why**: LLM이 인간 피험자를 얼마나 효과적으로 대체할 수 있는지, 어느 조건에서 신뢰성이 낮은지를 파악하는 것이 사회과학 연구의 방법론적 혁신에 필수적

- **Approach**: 2015-2024년 5개 상위 저널(Academy of Management Journal, Organizational Behavior and Human Decision Making, Journal of Applied Psychology, Journal of Personality and Social Psychology, Journal of Experimental Psychology: General)에서 무작위로 선정한 156개의 시나리오 기반 실험을 3개 LLM으로 재현하는 대규모 "실리콘 재현(silicon replication)" 연구 실시

## Achievement

![Figure 3](figures/fig3.webp) *GPT-4의 원본 및 재현 p값 비교*

![Figure 4](figures/fig4.webp) *GPT-4의 주효과 r값 비교 (원본 vs 재현)*

1. **높은 주효과 재현율**: GPT-4는 주효과의 72.7%, 상호작용효과의 45.7% 재현 성공. Claude와 DeepSeek는 더욱 높은 재현율 달성. 이는 원본 연구의 방향성과 통계적 유의성이 잘 보존됨을 의미

2. **사회적으로 민감한 주제에서의 현저한 성능 저하**: 인종 변수가 포함된 연구의 경우 GPT-4의 주효과 재현율이 76.8%에서 41.5%로 급락. 이는 LLM의 가치 정렬(value alignment)과 사회적 바람직성 편향(social desirability bias)에 기인

3. **체계적인 효과크기 증폭**: LLM에서 생성된 효과크기가 인간 연구보다 Fisher Z값으로 약 2-3배 큼. 원본 연구에서 귀무가설(null findings)을 보인 경우 LLM은 68-83%의 높은 비율로 유의미한 주효과를 생성

4. **더 좁은 신뢰구간**: LLM 응답은 피로, 주의산만, 반응 불일치가 없어 더 명확한 데이터 패턴을 보이며, 이는 심리 효과의 정교한 감지 가능성을 시사하면서도 제1종 오류(Type I error) 위험성도 제시

## How

![Figure 1](figures/fig1.webp) *연구 설계 및 과정*

- **표본 선정**: 5개 상위 저널에서 각 10개 논문씩 무작위 선정하여 총 156개 연구 확보. 자기 경험 보고, 프라이밍 기법, 생리적 측정, 종단 설계, 집단 상호작용 포함 연구는 제외

- **프롬프트 설계**: (1) 맥락/역할 설정 (2) 시나리오 설명 (3) 변수 측정 (4) 응답 형식 설정의 4개 핵심 요소로 구성. JSON 형식 출력으로 체계적 분석 용이

- **검증 및 적응**: 35.3%의 연구는 LLM의 "주의 집중 실패(failed attention)"를 해결하기 위해 프롬프트 재구조화. 인간 피험자 실험의 파일럿 테스트와 유사한 검증 프로세스 적용

- **균형잡힌 비교**: 각 원본 연구마다 동일 수의 LLM 응답 생성하여 공정한 비교 보장. 경영학(70개) 및 심리학(86개) 간 균형잡힌 표현

- **표준화된 평가 지표**: 재현율(replication rate), p값 분포, 효과크기, 연구 특성의 영향을 분석

## Originality

- **규모의 혁신성**: 단일 LLM이 아닌 3개의 서로 다른 최신 LLM을 포함한 최대 규모(156개 연구, 690개 주효과, 164개 상호작용효과)의 비교 재현 연구

- **체계적 편차 규명**: LLM의 가치 정렬과 사회적 바람직성 편향이 구체적으로 어느 조건(인종, 성별, 윤리)에서 성능을 저하시키는지를 정량화

- **효과크기 증폭 현상의 발견**: LLM이 단순히 더 정확한 것이 아니라 체계적으로 더 큰 효과를 생성한다는 점 입증 - 이는 "깨끗한 데이터"와 "과다 추정" 사이의 이중 해석 가능성 제시

- **방법론적 프레임워크**: "실리콘 재현"이라는 새로운 용어 도입 및 체계화된 프롬프트 설계-검증-적응 절차 개발

- **개방 과학**: 전체 데이터셋, 실험 프롬프트, API 호출 코드, 코딩 시트를 OSF 저장소에 공개

## Limitation & Further Study

- **표본 특성의 제한**: 시나리오 기반 실험(vignette studies)에만 초점. 행동 실험, 종단 연구, 생리적 측정이 필요한 연구로 일반화 불가능

- **프롬프트 적응의 이상화**: 35.3%의 연구가 프롬프트 수정을 요구했는데, 이것이 "개념적 재현(conceptual replication)"으로의 이동을 의미. 순수 외적 재현성(literal replication)을 완전히 달성하지 못함

- **메커니즘 규명 부족**: LLM이 왜 인종/성별 관련 실험에서 성능이 낮은지에 대한 심층 메커니즘 분석 부족. 가치 정렬의 구체적 구현 방식에 대한 설명 필요

- **효과크기 증폭의 원인**: LLM의 "깨끗한 데이터"가 실제로 더 정확한 심리 효과를 반영하는지, 아니면 모델 편향인지 구분 필요. 신경망 내부 메커니즘 분석 필요

- **후속 연구 방향**:
  - 사회적 민감성에 대한 정렬 조정(alignment tuning)이 성능 개선 가능성 탐색
  - 인간 피험자와 LLM 응답의 하이브리드 접근법 개발
  - 기타 LLM 아키텍처(open-source 모델 안정성 향상) 및 멀티모달 입력 능력 개선
  - 종단 연구나 행동 실험을 위한 LLM 확장 가능성 탐색

## Evaluation

- **Novelty**: 4/5
  - 규모와 체계성에서 독창적이고, 사회적 민감성 관련 발견이 새로움. 다만 LLM의 일반적 편향성 자체는 이미 알려진 현상
  
- **Technical Soundness**: 4/5
  - 엄격한 방법론과 체계적 설계. 다만 프롬프트 적응(35.3%)이 표준화된 과정에서 벗어나며, 개별 모델 내 변동성(temperature, seed) 보고 부재
  
- **Significance**: 4/5
  - 사회과학 연구 방법론에 중요한 함의 제시. LLM의 현실적 활용 한계를 명확히 하여 실제 연구자들의 의사결정에 직결. 다만 LLM 기술 발전 속도가 빨라 빠른 구식화 가능성
  
- **Clarity**: 4/5
  - 명확한 시각화와 체계적 설명. 다만 일부 기술적 세부사항(프롬프트 적응 기준, 각 모델 간 차이의 원인)이 주 본문에서 부족
  
- **Overall**: 4/5

**총평**: 이 논문은 AI 시대 사회과학 연구 방법론의 중대한 전환점을 다룬 가치 있는 대규모 실증 연구이다. LLM의 가능성과 한계를 명확하게 규명하고, 특히 사회적으로 민감한 주제에서의 체계적 편차를 입증함으로써 "LLM이 인간을 완전히 대체할 수 없다"는 중요한 결론을 제시한다. 다만 빠르게 진화하는 LLM 기술에 대응하기 위해 지속적 모니터링과 미세 조정(fine-tuning) 전략에 대한 후속 연구가 필요하다.

## Related Papers

- 🔗 후속 연구: [[papers/821_Towards_a_client-centered_assessment_of_llm_therapists_by_cl/review]] — 심리학 실험 재현을 LLM 치료사의 클라이언트 중심 평가로 확장한 의료 응용
- 🏛 기반 연구: [[papers/237_Confidence_in_Large_Language_Model_Evaluation_A_Bayesian_App/review]] — 제한된 샘플에서 LLM 평가하는 베이지안 방법론이 심리학 실험 재현의 통계적 기반
- 🔗 후속 연구: [[papers/838_Training_socially_aligned_language_models_in_simulated_human/review]] — 심리학 실험 재현을 사회적으로 정렬된 언어모델 훈련으로 발전시킨 연구
- 🔄 다른 접근: [[papers/173_Bridging_social_psychology_and_llm_reasoning_Conflict-aware/review]] — 심리학 실험 재현 vs 사회심리학과 LLM 추론 연결의 서로 다른 심리학 접근
- 🏛 기반 연구: [[papers/821_Towards_a_client-centered_assessment_of_llm_therapists_by_cl/review]] — 심리학 실험 재현 연구가 LLM 치료사 평가에서 인간 행동 시뮬레이션의 기반
- 🔗 후속 연구: [[papers/237_Confidence_in_Large_Language_Model_Evaluation_A_Bayesian_App/review]] — 베이지안 LLM 평가 방법론을 대규모 심리학 실험 재현 검증으로 확장한 응용
- 🔄 다른 접근: [[papers/188_Can_we_automatize_scientific_discovery_in_the_cognitive_scie/review]] — 인간 피험자 대체 AI와 인지과학 자동화의 다른 접근법
- 🔄 다른 접근: [[papers/757_Simulating_tabular_datasets_through_llms_to_rapidly_explore/review]] — LLM을 활용한 가설 탐색에서 데이터셋 시뮬레이션과 실제 인간 대상 연구 복제의 서로 다른 접근법을 비교하여 각각의 유효성을 검증할 수 있다.
- 🔗 후속 연구: [[papers/477_Large_language_models_pass_the_turing_test/review]] — LLM이 인간을 대체할 수 있는 가능성을 사회과학 실험 맥락에서 체계적으로 검증
