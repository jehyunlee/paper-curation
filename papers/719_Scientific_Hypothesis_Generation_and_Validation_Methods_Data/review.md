---
title: "719_Scientific_Hypothesis_Generation_and_Validation_Methods_Data"
authors:
  - "Abbi Abdel-Rehim"
  - "Hector Zenil"
  - "Oghenejokpeme Orhobor"
  - "Marie Fisher"
  - "Ross J. Collins"
date: "2025.06"
doi: "10.1098/rsif.2024.0674"
arxiv: ""
score: 4.0
essence: "GPT-4를 이용하여 유방암 치료를 위한 새로운 약물 조합 가설을 생성하고 실험실에서 검증하여, LLM(Large Language Model)이 과학적 가설 생성의 가치 있는 도구임을 입증했다."
tags:
  - "cat/AI-Powered_Scientific_Research_Frameworks"
  - "sub/Biomedical_Research_Agents"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Abdel-Rehim et al._2025_Scientific hypothesis generation by large language models laboratory validation in breast cancer tr.pdf"
---

# Scientific hypothesis generation by large language models: laboratory validation in breast cancer treatment

> **저자**: Abbi Abdel-Rehim, Hector Zenil, Oghenejokpeme Orhobor, Marie Fisher, Ross J. Collins, Elizabeth Bourne, Gareth W. Fearnley, Emma Tate, Holly X. Smith, Larisa N. Soldatova, Ross King | **날짜**: 06/2025 | **DOI**: [10.1098/rsif.2024.0674](https://doi.org/10.1098/rsif.2024.0674)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1. The overall structure of our experiments. GPT4 was previously trained on data on a large fraction of the text *

GPT-4를 이용하여 유방암 치료를 위한 새로운 약물 조합 가설을 생성하고 실험실에서 검증하여, LLM(Large Language Model)이 과학적 가설 생성의 가치 있는 도구임을 입증했다.

## Motivation

- **Known**: LLM은 다양한 작업에서 뛰어난 성능을 보이고 있으며, 과학 분야에서도 텍스트 요약, 데이터 분석, 논문 작성 등 여러 응용이 가능하다. 다만 LLM의 확률적 구조로 인한 'hallucination(환각)' 현상은 대부분의 응용에서 해롭다.
- **Gap**: LLM이 과학적 가설 생성에 유용할 수 있는 가능성은 명확하지만, 이를 실제 실험으로 검증한 연구는 거의 없었다. 특히 유방암 치료와 같은 실제 임상 응용 분야에서의 활용 가능성을 체계적으로 검증한 사례가 부족하다.
- **Why**: 유방암은 여성에서 가장 흔한 암이며, 약물 내성으로 인한 치료 효과 감소가 문제인데, LLM을 통한 신약 조합 발굴은 신약 개발 시간과 비용을 단축할 수 있는 잠재력이 크다.
- **Approach**: GPT-4에 MCF7 유방암 세포주에 대해 작용하고 MCF10A 정상 세포주에는 해를 끼치지 않는 FDA 승인 약물 조합을 제시하도록 프롬프트하고, 생성된 가설에 대해 실험실 검증을 수행하여 synergy score를 평가했다.

## Achievement


- **첫 번째 반복 성공**: GPT-4가 제시한 12개 약물 조합 중 3개가 양성 대조군을 초과하는 synergy score 달성
- **적응형 가설 생성**: 초기 결과를 바탕으로 GPT-4가 생성한 새로운 조합 중 4개 테스트 중 3개가 양성 synergy score 달성
- **높은 특이성**: 8개 조합이 MCF7에서 MCF10A보다 높은 HSA score 보유
- **광범위한 synergy 발견**: 12개 가설 조합 중 10개에서 synergistic 영역 확인
- **문헌에 없는 신규 가설**: 생성된 모든 약물 조합이 암 치료 문헌에 존재하지 않는 완전히 새로운 조합

## How

![Figure 1](figures/fig1.webp)

*Figure 1. The overall structure of our experiments. GPT4 was previously trained on data on a large fraction of the text *

- GPT-4에 구체적 프롬프트 제시 (MCF7 표적, MCF10A 피해 회피, synergistic 가능성)
- 비암 치료제(non-antineoplastic drugs) 중심의 FDA 승인 약물 조합 생성
- SynergyFinder 3.0 소프트웨어를 이용한 HSA(Highest Single Agent) synergy score 계산
- 양성 및 음성 대조군 설정 (양성: doxorubicin + cyclophosphamide, 음성: 유해가능 약물 조합)
- 두 번째 반복: 초기 결과를 입력으로 새로운 약물 조합 생성 및 재검증

## Originality

- LLM의 'hallucination'을 부정적 특성이 아닌 과학 가설 생성의 긍정적 자산으로 재해석하는 새로운 관점", '실제 실험실 검증을 통해 LLM 생성 가설의 실질적 가치를 객관적으로 입증한 첫 사례
- 반복적 학습-검증 루프(두 번째 반복)를 통한 적응형 가설 생성 시연
- 기존 문헌에 없는 완전히 새로운 약물 조합의 체계적 발굴

## Limitation & Further Study

- 제한된 표본 크기: 12개 조합만 테스트하여 통계적 일반화 한계
- 단일 세포주 모델: MCF7만 사용하여 유방암의 다양한 분자 아형(molecular subtype) 미반영
- 대조군 선택 편향: 연구자 자신이 대조군을 선택하지 않고 GPT-4에 의존
- 메커니즘 분석 부재: synergy가 발생하는 생물학적 메커니즘에 대한 심화 분석 필요
- 후속 연구: (1) 더 많은 유방암 세포주 및 환자 유래 샘플(PDX) 모델에서 검증, (2) in vivo 동물 모델 실험, (3) synergy 메커니즘의 상세 분석, (4) 다른 암종으로의 확장 가능성 평가

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 연구는 LLM이 단순한 정보 도구를 넘어 과학적 발견의 실질적 파트너가 될 수 있음을 최초로 엄격하게 입증한 획기적 연구이다. 약물 조합 개발이라는 임상적으로 중요한 분야에서 실현 가능성을 보여주었으나, 통계적 견고성과 메커니즘 규명을 위한 추가 연구가 필요하다.

## Related Papers

- 🔄 다른 접근: [[papers/820_Toward_Reliable_Scientific_Hypothesis_Generation_Evaluating/review]] — 생의학 가설 생성에서 GPT-4 기반 실험 검증과 신뢰성 평가 중심 접근법을 비교할 수 있습니다.
- 🔗 후속 연구: [[papers/418_Hypothesis_Generation_for_Materials_Discovery_and_Design_Usi/review]] — 재료 발견과 설계를 위한 LLM 가설 생성이 유방암 치료로 확장된 구체적 의료 응용 사례입니다.
- 🏛 기반 연구: [[papers/819_Toward_reliable_biomedical_hypothesis_generation_Evaluating/review]] — 신뢰할 수 있는 생의학 가설 생성 평가가 GPT-4 기반 약물 조합 가설의 검증 방법론 기반을 제공합니다.
- 🔗 후속 연구: [[papers/009_A_GENTIC_H_YPOTHESIS__A_SURVEY_ON_HYPOTHESIS_GENERATION_USIN/review]] — 대규모 언어모델의 과학적 가설 생성을 실제 실험 결과와 연결하여 확장한다.
