---
title: "178_Can_ai_examine_novelty_of_patents_Novelty_evaluation_based_o"
authors:
  - "Hayato Ikoma"
  - "Teruko Mitamura (Carnegie Mellon University)"
date: "2025"
doi: "arXiv:2502.06316"
arxiv: ""
score: 4.0
essence: "본 논문은 대규모 언어모델(LLM)의 특허 신규성(novelty) 평가 능력을 최초로 체계적으로 검증하기 위해, 실제 특허 심사 사례를 기반으로 한 데이터셋을 구축하고 다양한 모델의 성능을 비교 분석한 연구이다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Patent_Citation_Prediction"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Leal et al._2025_Can ai examine novelty of patents Novelty evaluation based on the correspondence between patent cl.pdf"
---

# Can AI Examine Novelty of Patents?: Novelty Evaluation Based on the Correspondence between Patent Claim and Prior Art

> **저자**: Hayato Ikoma, Teruko Mitamura (Carnegie Mellon University) | **날짜**: 2025 | **DOI**: [arXiv:2502.06316](https://arxiv.org/abs/2502.06316)

---

## Essence

![Figure 1](figures/fig1.webp)
*특허 심사 과정: 심사관이 특허 청구항과 선행기술 문서를 비교하여 거절 이유를 판단하고, 출원인이 청구항을 수정한 후 재심사하는 반복 과정*

본 논문은 대규모 언어모델(LLM)의 특허 신규성(novelty) 평가 능력을 최초로 체계적으로 검증하기 위해, 실제 특허 심사 사례를 기반으로 한 데이터셋을 구축하고 다양한 모델의 성능을 비교 분석한 연구이다.

## Motivation

- **Known**: NLP 분야에서 특허 분류, 검색 등 다양한 특허 관련 작업이 연구되어 왔으나, 특허의 신규성 평가는 여전히 미탐색 영역으로 남아있음. 최근 장문 문맥을 처리할 수 있는 LLM이 개발됨.

- **Gap**: 특허 신규성 평가는 전통적으로 특허심사관의 전문적 판단에만 의존해왔으며, 청구항(claim)과 선행기술(prior art) 문서 간의 대응 관계를 분석하는 체계적인 AI 평가 연구가 부재함.

- **Why**: 특허 신규성 평가 자동화는 심사관과 출원인 모두의 업무 부담을 크게 줄이고, 전문성 부족 집단의 특허 획득 접근성을 높일 수 있음.

- **Approach**: (1) 실제 특허청 거절 통지서(Non-Final Rejection) 기반 신규성 평가 데이터셋 구축, (2) 분류 및 생성 모델 모두를 활용한 청구항-인용문헌(C-T: Claim-Cited Texts) 대응 관계 분석.

## Achievement

![Figure 2](figures/fig2.webp)
*특허 심사 과정의 전체 흐름과 데이터 추출 출처: 비신규 사례는 원본 청구항, 신규 사례는 수정된 청구항 사용*

1. **최초 데이터셋 구축**: 2014-2015년 USPTO IPC G06F(전자 데이터 처리) 분야 3,975건의 특허 사례로부터 청구항-인용문헌 쌍 데이터셋 구성 (훈련:검증:테스트 = 80:10:10, 길이 편향 제거를 위한 전처리 적용)

2. **모델 성능 비교**: 분류 모델(Longformer)은 신규성 평가에 제한적 성능을 보였으나, 생성 모델(Llama, GPT-4o)은 합리적 수준의 정확도로 예측하고 청구항과 선행기술 간 관계를 설명할 수 있음을 입증

3. **실무 적용성 검증**: 실제 특허 심사 프로세스를 반영한 거절 통지서 기반 접근으로 모델 설명의 신뢰성 및 해석 가능성 확보

## How

- **작업 설정**: 이진 분류 작업으로 청구항과 인용된 선행기술 문헌의 관계로부터 신규성 유무 판정. 단일 청구항만 사용한 조건(C input)과 청구항+인용문헌 조건(C-T input) 모두 평가

- **데이터 구성**: 
  - 비신규(Non-Novel): 거절 통지된 원본 청구항 + 인용된 선행기술 문헌의 해당 문단
  - 신규(Novel): 수정된 최종 청구항 + 동일 인용문헌 문단
  - 청구항 길이별 그룹화 후 레이블 균형화 (1:1 비율)

- **모델 및 방법론**:
  - 분류 모델: Longformer(인코더 기반, 4,096 토큰), Llama2/3(디코더 기반, 4,096~8,192 토큰), GPT-4o
  - 학습 패러다임: Zero-shot, Few-shot(2-shot), 감독학습 미세조정(QLoRA PEFT)
  - 분류 방식: (1) 선형 분류 헤드 활용, (2) 프롬프트 기반 텍스트 생성

- **프롬프트 설계**: 실제 특허 심사 프로세스를 모방한 지시문으로 모델 가이드

## Originality

- **최초 신규성 평가 작업 정의**: 청구항과 선행기술의 **대응 관계 분석**에 기반한 신규성 평가는 선행 연구의 단순 특성 기반 또는 통사/의미 분석 기반 접근과 차별화

- **실제 심사 문서 활용**: USPTO 거절 통지서(Non-Final Rejection)로부터 **직접 추출된 관련 문단**을 사용함으로써 어떤 청구항 요소가 선행기술에서 발견되었는지 명시적으로 식별 가능

- **확장 가능 데이터셋**: 대량으로 보관된 거절 통지서 기록을 활용한 향후 데이터셋 확대의 용이성

- **이중 입력 조건 평가**: C 입력(청구항 만)과 C-T 입력(청구항+인용문헌) 모두 평가하여 정밀한 모델 성능 판단

## Limitation & Further Study

- **분류 모델의 성능 한계**: Longformer 등 인코더 기반 분류 모델이 신규성 평가에 충분하지 못함. 더 정교한 분석 메커니즘 필요

- **생성 모델의 편향성**: 장문 문맥 처리 시 모델이 특정 길이나 구조에 편향될 가능성에 대한 심층 분석 부족

- **데이터셋 규모 제한**: 단일 IPC 분야(G06F)의 제한된 기간(2014-2015) 데이터로 일반화 능력 검증 필요

- **설명 품질 정량화**: 생성 모델 설명의 정확성이 "충분하다"는 정성적 평가로만 제시되어, 자동 평가 메트릭 개발 필요

- **후속 연구 방향**:
  - 다양한 IPC 기술 분야 데이터셋 확대
  - 최신 모델(예: GPT-4o 기반 미세조정)의 체계적 검증
  - 명시성(non-obviousness) 등 다른 특허성 요건으로 확대
  - 심사관 의견과 모델 예측의 불일치 분석


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 3.5/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 논문은 특허 신규성 평가라는 미탐색 영역에서 실제 심사 사례 기반 데이터셋을 처음 구축하고 LLM의 능력을 검증한 의미 있는 연구이다. 생성 모델의 가능성을 보여주었으나, 분류 모델 부진의 원인 분석, 설명의 자동 평가 메트릭 개발, 그리고 다양한 기술 분야로의 일반화가 필요하다.

## Related Papers

- 🧪 응용 사례: [[papers/779_Supporting_assessment_of_novelty_of_design_problems_using_co/review]] — 설계 문제의 참신성 평가를 위한 코사인 유사도 사용으로 본 논문의 특허 신규성 평가 방법론을 설계 도메인에 적용한다.
- 🔄 다른 접근: [[papers/313_Enabling_ai_scientists_to_recognize_innovation_A_domain-agno/review]] — AI 과학자의 혁신 인식을 위한 도메인 무관 알고리즘으로 특허 신규성과 유사한 평가 문제를 다른 접근법으로 해결한다.
- 🏛 기반 연구: [[papers/322_Evaluation_of_openai_o1_Opportunities_and_challenges_of_agi/review]] — OpenAI o1의 평가를 통해 AGI의 기회와 도전을 분석하여 본 논문의 LLM 특허 평가 능력 연구의 기술적 배경을 제공한다.
- 🔄 다른 접근: [[papers/605_PatFig_Generating_Short_and_Long_Captions_for_Patent_Figures/review]] — 둘 다 AI의 특허 분야 활용을 다루지만 하나는 특허 도형 캡션 생성에, 다른 하나는 특허 신규성 검토에 초점을 맞춘다.
- 🔗 후속 연구: [[papers/010_A_hierarchical_framework_for_measuring_scientific_paper_inno/review]] — 특허의 신규성 평가를 과학 논문의 혁신성 측정으로 확장하여 더 포괄적인 지적 창작물 평가 방법을 제시함
- 🧪 응용 사례: [[papers/313_Enabling_ai_scientists_to_recognize_innovation_A_domain-agno/review]] — AI의 특허 신규성 평가 능력 연구에서 본 논문의 혁신성 인식 알고리즘을 특허 도메인에 적용할 수 있다.
