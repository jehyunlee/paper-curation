---
title: "051_Admissions_in_the_age_of_AI_detecting_AI-generated_applicati"
authors:
  - "Yijun Zhao"
  - "Alexander Borelli"
  - "Fernando Martinez"
  - "Haoran Xue"
  - "Gary M. Weiss"
date: "2024.11"
doi: "10.1038/s41598-024-77847-z"
arxiv: ""
score: 4.0
essence: "ChatGPT와 같은 생성형 AI의 발전으로 인해 대학원 입시에서 AI로 생성되거나 수정된 추천서(LOR)와 지원 동기서(SOI)를 탐지하기 위한 도메인 특화 분류 모델을 개발하였으며, 충분한 훈련 샘플을 갖춘 특화된 탐지기가 높은 정확도를 달성할 수 있음을 보여준다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Human-AI_Performance_Detection"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Zhao et al._2024_Admissions in the age of AI detecting AI-generated application materials in higher education.pdf"
---

# Admissions in the age of AI: detecting AI-generated application materials in higher education

> **저자**: Yijun Zhao, Alexander Borelli, Fernando Martinez, Haoran Xue, Gary M. Weiss | **날짜**: 2024-11-02 | **DOI**: [10.1038/s41598-024-77847-z](https://doi.org/10.1038/s41598-024-77847-z)

---

## Essence

ChatGPT와 같은 생성형 AI의 발전으로 인해 대학원 입시에서 AI로 생성되거나 수정된 추천서(LOR)와 지원 동기서(SOI)를 탐지하기 위한 도메인 특화 분류 모델을 개발하였으며, 충분한 훈련 샘플을 갖춘 특화된 탐지기가 높은 정확도를 달성할 수 있음을 보여준다.

## Motivation

- **Known**: 일반적이고 보편적으로 효과적인 AI 텍스트 탐지 모델 개발이 현재 기술로는 불가능하며, OpenAI를 포함한 상용 도구들도 신뢰성이 낮음(AI 생성 텍스트 탐지율 26%, 위양성률 9%)
- **Gap**: 고등교육의 입시 과정에서 AI 생성 또는 AI 수정 텍스트를 신뢰성 있게 탐지할 수 있는 실용적인 도구가 부재함
- **Why**: 지원자들의 진정한 능력을 평가하고 공정하고 신뢰성 있는 입시 제도를 유지하기 위해서는 AI 생성 자료를 탐지할 필요가 있음. 특히 SOI는 의사소통 능력 평가 수단으로 작용하므로 AI 수정 여부 판별이 중요함
- **Approach**: Fordham University의 석사 프로그램(컴퓨터과학, 데이터과학)에서 수집한 3,755개의 추천서와 1,973개의 지원 동기서를 이용하여 도메인 특화 분류 모델 개발

## Achievement

![Figure 1](figures/fig1.webp)
*대화형 웹 인터페이스를 통한 AI 생성 LOR 및 SOI 탐지 시스템*

1. **도메인 특화 모델의 우수성**: 도메인 특화 데이터로 훈련된 모든 모델(Naïve Bayes, Logistic Regression, BERT, DistilBERT)이 우수한 성능을 달성하였으며, 특히 Transformer 기반 LLM이 AI 수정 문서 탐지에서 전통 머신러닝 모델을 능가함

2. **AI 수정 텍스트 탐지 가능**: 단순히 AI 생성 텍스트뿐 아니라 인간 저자가 작성한 원문을 AI가 수정한 텍스트도 정확히 식별할 수 있음을 입증

3. **특성 분석**: ChatGPT는 인간이 작성한 텍스트와 구별되는 고유한 어휘, 문단 구조, 단어 빈도 특성을 보유함을 통계적으로 입증

## How

- **데이터 수집**: Fordham University 석사 프로그램 지원서에서 3,755개 LOR과 1,973개 SOI 추출, FERPA 준수를 위해 익명화 처리
- **AI 텍스트 생성**: GPT-3.5 Turbo API를 이용하여 각 문서에 대응하는 AI 생성 버전과 AI 수정 버전 생성 (프롬프트는 지원자의 입시 데이터로부터 도출)
- **분류 모델**: 
  - 전통 머신러닝: Naïve Bayes, Logistic Regression
  - Transformer 기반: BERT, DistilBERT
- **검증 데이터**: GPT-wiki-intro 오픈 액세스 데이터셋 활용하여 도메인 특화 탐지기의 타당성 검증
- **배포**: GitHub를 통한 코드 공개 및 대화형 웹 인터페이스 제공

## Originality

- **도메인 특화 접근**: 범용 탐지 모델이 아닌 고등교육 입시 서류에 특화된 모델 개발로 실용성 강화
- **AI 수정 텍스트 탐지**: 기존 대부분의 연구가 AI 생성 텍스트만 다룬 반면, 인간 원문의 AI 수정을 별도로 탐지하는 문제 정의 및 해결
- **실제 운영 데이터 활용**: 학술 데이터셋이 아닌 실제 대학 입시 서류 3,700+건 사용으로 현실성 확보
- **실용적 배포**: 웹 기반 인터페이스로 실제 대학이 운영 중 사용 가능한 도구 제공

## Limitation & Further Study

- **제한된 도메인**: Fordham University의 컴퓨터과학/데이터과학 석사 프로그램에 한정되어 다른 학과나 학위 과정으로의 일반화 가능성 미확인
- **특정 AI 모델**: GPT-3.5 Turbo로 생성된 텍스트만 테스트되었으며, Claude, Gemini 등 다른 생성형 AI의 탐지 성능 미평가
- **AI 기술 진화**: 향후 더욱 정교한 AI 모델이 출현할 경우 탐지 성능 저하 가능성
- **후속 연구 방향**:
  - 다양한 학문 분야 및 문서 유형으로 확장
  - 다중 생성형 AI 모델에 대한 탐지 성능 비교
  - 적대적 프롬프트(adversarial prompts)에 대한 견고성 평가
  - 탐지 모델의 실시간 업데이트 메커니즘 개발

## Evaluation

- **Novelty**: 4/5
  - AI 수정 텍스트 탐지라는 새로운 문제 정의와 실제 입시 데이터 활용이 차별적이나, 도메인 특화 접근 자체는 기존 연구에서 제시된 개념

- **Technical Soundness**: 4/5
  - 적절한 모델 선택, 명확한 데이터셋 구성, 합리적인 성능 평가 수행. 다만 하이퍼파라미터 튜닝, 교차 검증 전략 등 세부 기술 설명 부족

- **Significance**: 4/5
  - 고등교육 입시의 학사 무결성 보호라는 중요한 사회적 문제 해결. 실용적 웹 도구 제공으로 실제 영향력 기대. 하지만 범용성 제한으로 인한 확대 적용의 어려움

- **Clarity**: 4/5
  - 논문 구조가 명확하고 동기, 방법론, 결과가 논리적으로 제시됨. Figure 1의 웹 인터페이스 시각화가 유용함. 일부 통계 결과의 구체적 수치 제시 미흡

- **Overall**: 4/5

**총평**: 본 연구는 생성형 AI의 발전에 따른 고등교육의 현실적 과제인 입시 자료 위조 탐지를 도메인 특화 모델로 해결하는 실용적이고 신뢰성 있는 접근을 제시하며, AI 수정 텍스트 탐지라는 새로운 관점을 도입했다는 점에서 의미가 있으나, 범용성 제한과 단일 AI 모델 평가라는 한계가 있다.

## Related Papers

- 🏛 기반 연구: [[papers/206_ChatGPT_outperforms_crowd_workers_for_text-annotation_tasks/review]] — 텍스트 주석 작업에서 ChatGPT의 성능을 보여주는 기초 연구로 AI 생성 텍스트 탐지의 이론적 배경을 제공한다.
- 🔗 후속 연구: [[papers/270_Detecting_llm-written_peer_reviews/review]] — 동료 심사 리뷰에서 LLM으로 작성된 텍스트를 탐지하는 연구로 본 논문의 탐지 방법론을 학술 분야로 확장한다.
- 🔄 다른 접근: [[papers/445_Is_Your_Paper_Being_Reviewed_by_an_LLM_Investigating_AI_Text/review]] — AI가 논문 심사에 사용되고 있는지 조사하는 다른 접근법으로 동일한 문제의식을 다른 각도에서 다룬다.
