---
title: "1116_Harnessing_the_Power_of_Adversarial_Prompting_and_Large_Lang"
authors:
  - "Ioana Ciucă"
  - "Yuan-Sen Ting"
  - "Sandor Kruk"
  - "Kartheik Iyer"
date: "2023.06"
doi: "10.48550/arXiv.2306.11648"
arxiv: ""
score: 4.0
essence: "본 연구는 GPT-4와 적대적 프롬프팅(adversarial prompting)을 활용하여 천문학 분야에서 가설 생성 능력을 향상시키는 방법을 제시한다. NASA 천체물리학 데이터시스템(ADS)의 1,000개 논문을 맥락 정보로 제공할 때 적대적 프롬프팅이 특히 효과적임을 보여준다."
tags:
  - "cat/Science_of_Science_Research"
  - "sub/AI_and_Large_Language_Models"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Ciucă et al._2023_Harnessing the Power of Adversarial Prompting and Large Language Models for Robust Hypothesis Genera.pdf"
---

# Harnessing the Power of Adversarial Prompting and Large Language Models for Robust Hypothesis Generation in Astronomy

> **저자**: Ioana Ciucă, Yuan-Sen Ting, Sandor Kruk, Kartheik Iyer | **날짜**: 2023-06-20 | **DOI**: [10.48550/arXiv.2306.11648](https://doi.org/10.48550/arXiv.2306.11648)

---

## Essence

![Figure 2](figures/fig2.webp)

*Figure 2. Adversarial prompting and domain-specific context enrichment significantly enhance hypothesis generation quali*

본 연구는 GPT-4와 적대적 프롬프팅(adversarial prompting)을 활용하여 천문학 분야에서 가설 생성 능력을 향상시키는 방법을 제시한다. NASA 천체물리학 데이터시스템(ADS)의 1,000개 논문을 맥락 정보로 제공할 때 적대적 프롬프팅이 특히 효과적임을 보여준다.

## Motivation

- **Known**: LLM(Large Language Models)은 주의(attention) 메커니즘과 트랜스포머 아키텍처를 통해 뛰어난 자연어 이해 및 생성 능력을 갖추고 있다. 맥락 내 프롬프팅(in-context prompting)을 통해 도메인 특화 작업의 성능을 개선할 수 있다는 것이 알려져 있다.
- **Gap**: 천문학 분야는 훈련 말뭉치에 포함된 문헌이 제한적이어서 LLM의 환각(hallucination) 문제가 두드러진다. 맥락 프롬프팅만으로는 대규모 도메인 지식 코퍼스를 효과적으로 활용하지 못하고 있다.
- **Why**: 천문학은 다양한 소분야의 지식을 연결하는 것이 핵심이며, 공개 데이터 정책과 포괄적인 문헌 데이터베이스를 갖추어 LLM 연구의 이상적 사례이다. LLM을 과학 연구에 활용하기 위한 새로운 방법론 개발이 필요하다.
- **Approach**: 맥락 정보 검색 파이프라인(retrieval pipeline)을 통해 1,000개의 논문 청크를 벡터화하고, 생성 모델-비평 모델-중재 모델의 3단계 GPT-4 인스턴스를 활용한 적대적 피드백 루프를 구성한다. 반복적인 비판과 개선을 통해 가설의 질을 향상시킨다.

## Achievement

![Figure 2](figures/fig2.webp)

*Figure 2. Adversarial prompting and domain-specific context enrichment significantly enhance hypothesis generation quali*

- **적대적 프롬프팅의 효과성**: 적대적 프롬프팅(adversarial prompting)이 없을 때는 맥락 논문 수에 관계없이 가설 질이 정체하지만, 적용 시 뚜렷한 개선 효과를 보인다.
- **도메인 맥락과의 상관관계**: 적대적 프롬프팅을 적용했을 때 특히 1,000개 논문 맥락(N=1000)에서 가설 질과 논문 수 간의 강한 상관관계가 성립한다.
- **일관성 향상**: 적대적 프롬프팅이 가설과 비평의 질 일관성을 크게 개선시킨다.
- **저비용 도메인 적응**: 미세 조정이나 어댑터(adapter) 없이 프롬프팅만으로 도메인 특화 성능을 달성한다.

## How

![Figure 1](figures/fig1.webp)

*Figure 1. This figure illustrates the adversarial in-context prompting workflow using OpenAI’s GPT-4 model. The procedur*

- **데이터 수집**: NASA ADS에서 'Gaia', 은하 운동학, 구조, 진화 관련 키워드로 필터링한 1,000개 갈락틱 천문학(Galactic Astronomy) 논문 선정", '**전처리 및 임베딩**: PDF를 텍스트로 변환 후 1,000 토큰 단위 청크로 분할, OpenAI의 text-ada-002 모델로 임베딩
- **유사도 검색**: 쿼리를 임베딩한 후 벡터 데이터베이스에서 유사 청크 검색
- **맥락 압축**: Langchain의 맥락 압축(contextual compression)을 통해 무관한 정보 제거
- **3단계 적대적 루프**: (1) 생성 GPT-4가 가설 생성, (2) 비평 GPT-4가 약점 지적 및 개선안 제시, (3) 중재 GPT-4가 피드백을 질문 형식으로 재구성하여 생성 모델에 반환
- **반복 실험**: N∈{1, 10, 100, 1000}개 논문으로 각각 5회 반복, 2회 순환(3개 가설, 2개 비평), 총 60개 가설과 40개 비평 생성
- **인간 평가**: 2명의 도메인 전문가가 과학적 정확성, 창의성·실현가능성, 3개 기준으로 평가

## Originality

- **적대적 프롬프팅의 신규 활용**: 생성-비평-중재 3단계 GPT-4 인스턴스 구조를 통한 반복적 개선 루프는 기존의 단순 맥락 프롬프팅과 구별된다.
- **과학 분야의 LLM 적용**: 가설 생성이라는 고차원적 과학 작업에 LLM을 적용하고, 도메인 문헌 규모와 성능의 관계를 정량화한다.
- **저비용 도메인 적응 방법**: 미세 조정 없이 프롬프팅만으로 도메인 특화 능력을 확보하는 실용적 접근법을 제시한다.
- **천문학 특성 활용**: 천문학의 '연결의 학문' 특성과 공개 데이터 정책을 명시적으로 활용한 설계이다.

## Limitation & Further Study

- **주관적 평가**: 2명의 인간 평가자만 참여하여 주관성 문제가 있을 수 있으며, 더 큰 규모의 인간 평가와 평가자 간 합의도(inter-rater agreement) 분석이 필요하다.
- **좁은 도메인 범위**: 갈락틱 천문학에만 초점을 맞춰 다른 천문학 분야나 과학 분야에의 일반화 가능성을 검증하지 않았다.
- **비용 증가**: 3개의 GPT-4 인스턴스를 사용하므로 실제 응용에서는 상당한 API 비용이 발생한다.
- **맥락 윈도우 제한**: GPT-4의 약 8,000 토큰 윈도우 제약이 제공 가능한 맥락 정보를 제한한다.
- **후속 연구**: (1) 더 큰 규모의 인간 평가 및 자동 평가 지표 개발, (2) 다른 과학 분야(생물학, 물리학 등)로의 확장, (3) 비용 최적화(더 적은 인스턴스 또는 더 저렴한 모델 사용), (4) 적대적 프롬프팅의 최적 반복 횟수 결정

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 연구는 적대적 프롬프팅과 도메인 맥락 검색을 결합하여 LLM의 과학적 가설 생성 능력을 체계적으로 향상시키는 혁신적인 방법론을 제시한다. 미세 조정 없이 저비용으로 도메인 특화 성능을 달성할 수 있음을 입증하여 과학 연구에서 LLM 활용의 새로운 가능성을 열어준다.

## Related Papers

- 🔗 후속 연구: [[papers/1033_The_Empowerment_of_Science_of_Science_by_Large_Language_Mode/review]] — 과학의 과학 분야에서 대형 언어모델의 활용 가능성을 보여주는 구체적인 천문학 분야 적용 사례를 제시한다.
- 🔄 다른 접근: [[papers/962_Forecasting_high-impact_research_topics_via_machine_learning/review]] — 기계학습을 통한 고영향 연구 주제 예측과 다른 접근으로 적대적 프롬프팅을 통한 가설 생성 방법을 제안한다.
- 🔗 후속 연구: [[papers/1072_Embracing_Foundation_Models_for_Advancing_Scientific_Discove/review]] — 적대적 프롬프팅과 LLM을 활용한 연구 질문 생성이 과학 발견을 위한 기초 모델 활용의 구체적 구현 방법을 제시한다.
