---
title: "026_A_survey_of_large_language_models"
authors:
  - "Wayne Xin Zhao"
  - "Kun Zhou"
  - "Junyi Li"
  - "Tianyi Tang"
  - "Xiaolei Wang"
date: "2023"
doi: ""
arxiv: ""
score: 4.0
essence: "대규모 언어모델(LLM)의 발전 과정을 통계적 언어모델부터 신경망 언어모델, 사전학습 언어모델을 거쳐 현재의 생성형 대규모 모델까지 체계적으로 조사한 종합 서베이 논문이다."
tags:
  - "cat/AI-Powered_Scientific_Research_Frameworks"
  - "sub/AI_for_Science_Taxonomy"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Zhao et al._2023_A survey of large language models.pdf"
---

# A survey of large language models

> **저자**: Wayne Xin Zhao, Kun Zhou, Junyi Li, Tianyi Tang, Xiaolei Wang, Yupeng Hou, Yingqian Min, Beichen Zhang, Junjie Zhang, Zican Dong, Yifan Du, Yang Chen, Yushuo Chen, Zhipeng Chen, Jinhao Jiang, Ruiyang Ren, Yifan Li, Xinyu Tang, Zikang Liu, Peiyu Liu | **날짜**: 2023 | **URL**: [https://arxiv.org/abs/2303.18223](https://arxiv.org/abs/2303.18223)

---

## Essence

![Figure 2](figures/fig2.webp)

*Fig. 2: An evolution process of the four generations of language models (LM) from the perspective of task solving capaci*

대규모 언어모델(LLM)의 발전 과정을 통계적 언어모델부터 신경망 언어모델, 사전학습 언어모델을 거쳐 현재의 생성형 대규모 모델까지 체계적으로 조사한 종합 서베이 논문이다.

## Motivation

- **Known**: 언어모델은 1990년대부터 연구되어 왔으며, Transformer 기반 사전학습 언어모델(PLM)의 등장으로 자연어처리 성능이 크게 향상되었다. 최근 모델 규모 증가에 따른 새로운 능력(인-컨텍스트 러닝 등)이 발현되고 있다.
- **Gap**: LLM의 급속한 발전에도 불구하고 체계적인 기술 진화, 적응 튜닝, 활용 방식, 성능 평가에 대한 종합적 이해가 부족하다. ChatGPT 이후 관련 연구가 폭증하면서 통일된 관점의 조사가 필요하다.
- **Why**: LLM은 자연어처리를 넘어 다양한 실세계 문제를 해결할 수 있는 범용 AI 알고리즘으로 진화하고 있으며, 이러한 기술 진화는 전체 AI 커뮤니티에 혁명적 영향을 미치고 있기 때문이다.
- **Approach**: 4가지 주요 측면(사전학습, 적응 튜닝, 활용, 성능 평가)에서 LLM의 기술 진화와 핵심 발견사항을 체계적으로 검토하고, 이용 가능한 자원과 미래 연구 방향을 정리한다.

## Achievement

![Figure 1](figures/fig1.webp)

*Fig. 1: The trends of the cumulative numbers of arXiv papers that contain the keyphrases “language model” (since June 20*

- **언어모델의 4단계 진화 프레임워크**: 통계적 언어모델(1990s) → 신경망 언어모델(2013) → 사전학습 언어모델(2018) → 대규모 언어모델(2020)로의 체계적 진화 과정을 시각화
- **스케일링 법칙과 창발 능력 규명**: 모델 파라미터가 특정 규모를 초과하면 인-컨텍스트 러닝 등 소규모 모델에 없는 특별한 능력이 나타나는 현상 분석
- **ChatGPT 이후의 연구 급증 정량화**: arXiv 논문 수가 일일 평균 0.40건에서 8.58건으로 증가(20배 이상)하여 LLM 연구의 폭증적 성장 입증
- **종합적 기술 체계화**: 사전학습, 프롬프트 기반 완성, 적응 튜닝, 정렬 등 LLM의 핵심 기술들을 통합적으로 정리

## How

![Figure 3](figures/fig3.webp)

*Fig. 3: A timeline of representative LLMs released in recent years. Models with publicly available checkpoints are*

- arXiv 논문 데이터베이스를 활용한 시계열 분석으로 연구 동향 추적
- GPT, BERT, LLaMA 등 대표 모델들의 기술 진화 과정 비교 분석
- 모델 파라미터 규모별 성능 변화 추이를 통한 스케일링 효과 검증
- 사전학습 전략, 미세조정(Fine-tuning), 프롬프트 기법 등 다양한 적응 방법 분류
- 벤치마크 데이터셋(GLUE, SuperGLUE 등)을 통한 성능 평가 체계화

## Originality

- 언어모델의 역사를 4단계 발전 프레임워크로 새롭게 구조화하여 각 단계의 핵심 특징과 전환점을 명확화
- 스케일링 법칙(Scaling Law)과 창발 능력(Emergent Abilities)의 관계를 처음으로 체계적으로 설명
- ChatGPT 출시 전후의 연구 양의 급격한 변화를 정량적으로 입증하여 기술 파급 효과 강조
- 사전학습, 적응 튜닝, 활용, 평가의 4개 축으로 LLM 생태계를 다차원 분석

## Limitation & Further Study

- 논문이 2026년 3월 버전으로 매우 최신이지만, LLM 기술의 급속한 발전으로 인해 몇 개월 후 새로운 모델과 기법이 지속적으로 등장할 수 있다
- 정성적 평가와 정량적 지표의 균형이 필요하며, 특정 작업(코드 생성, 추론 등)에 대한 상세 분석 보강 가능
- LLM의 사회적 영향(윤리, 편향, 환경 비용 등)에 대한 심화 논의 부족
- 후속연구로는 LLM의 해석 가능성(Interpretability) 향상, 환각(Hallucination) 감소, 멀티모달 모델 통합 방향 제시 필요

## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 이 서베이는 대규모 언어모델의 발전 역사와 핵심 기술을 체계적으로 정리한 매우 시의적절한 종합 자료로, 연구자와 실무자 모두에게 LLM의 현황을 이해하는 데 필수적인 참고자료이다.

## Related Papers

- 🧪 응용 사례: [[papers/801_The_llama_3_herd_of_models/review]] — Llama 3 모델군을 통해 대규모 언어모델의 실제 구현과 성능을 구체적으로 보여준다.
- 🏛 기반 연구: [[papers/1093_The_fifth_era_of_science_Artificial_scientific_intelligence/review]] — 인공 과학 지능의 이론적 토대로서 대규모 언어모델의 발전 과정을 제공한다.
- 🏛 기반 연구: [[papers/467_Large_Language_Models/review]] — 대규모 언어모델에 대한 포괄적 조사가 수학/물리학 배경 독자를 위한 LLM 강의노트의 기초 자료를 제공합니다.
