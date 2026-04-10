---
title: "1074_OLMo_Accelerating_the_Science_of_Language_Models"
authors:
  - "Dirk Groeneveld"
  - "Iz Beltagy"
  - "Pete Walsh"
  - "Akshita Bhagia"
  - "Rodney Kinney"
date: "2024.06"
doi: "10.48550/arXiv.2402.00838"
arxiv: ""
score: 4.0
essence: "OLMo는 완전히 공개된 언어 모델로 학습 데이터, 훈련 코드, 평가 코드를 모두 함께 공개하여 언어 모델에 대한 과학적 연구를 가능하게 한다."
tags:
  - "cat/Science_of_Science_Research"
  - "sub/AI_and_Large_Language_Models"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Groeneveld et al._2024_OLMo Accelerating the Science of Language Models.pdf"
---

# OLMo: Accelerating the Science of Language Models

> **저자**: Dirk Groeneveld, Iz Beltagy, Pete Walsh, Akshita Bhagia, Rodney Kinney, Oyvind Tafjord, Ananya Harsh Jha, Hamish Ivison, Ian Magnusson, Yizhong Wang, Shane Arora, David Atkinson, Russell Authur, Khyathi Raghavi Chandu, Arman Cohan, Jennifer Dumas, Yanai Elazar, Yuling Gu, Jack Hessel, Tushar Khot, William Merrill, Jacob Morrison, Niklas Muennighoff, Aakanksha Naik, Crystal Nam, Matthew E. Peters, Valentina Pyatkin, Abhilasha Ravichander, Dustin Schwenk, Saurabh Shah, Will Smith, Emma Strubell, Nishant Subramani, Mitchell Wortsman, Pradeep Dasigi, Nathan Lambert, Kyle Richardson, Luke Zettlemoyer, Jesse Dodge, Kyle Lo, Luca Soldaini, Noah A. Smith, Hannaneh Hajishirzi | **날짜**: 2024-06-07 | **DOI**: [10.48550/arXiv.2402.00838](https://doi.org/10.48550/arXiv.2402.00838)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1: Accuracy score progression of OLMo-7B on 8 core end-tasks score from Catwalk evaluation suite*

OLMo는 완전히 공개된 언어 모델로 학습 데이터, 훈련 코드, 평가 코드를 모두 함께 공개하여 언어 모델에 대한 과학적 연구를 가능하게 한다.

## Motivation

- **Known**: 대규모 언어 모델들이 상용화되면서 가장 강력한 모델들은 폐쇄되었으며, 훈련 데이터, 아키텍처, 개발 과정이 공개되지 않는 상황이다.
- **Gap**: 기존의 공개 모델들도 가중치와 추론 코드만 공개했을 뿐, 훈련 데이터와 훈련 코드를 함께 공개하는 완전히 오픈한 경쟁력 있는 모델이 부족했다.
- **Why**: 언어 모델의 편향성, 위험성, 성능 특성을 과학적으로 연구하기 위해서는 모델, 데이터, 코드가 모두 공개되어야 한다.
- **Approach**: Decoder-only transformer 아키텍처 기반으로 1B/7B 규모의 OLMo 모델을 개발하고, Dolma라는 공개 사전학습 데이터셋과 평가 프레임워크를 함께 제공한다.

## Achievement

![Figure 2](figures/fig2.webp)

*Figure 2: Bits per byte on 11 evaluation data sources from Paloma and their combination (Magnusson et al., 2023),*

- **완전 개방 프레임워크**: 모델 가중치, 훈련 데이터(Dolma), 훈련 코드, 평가 코드, 중간 체크포인트, 훈련 로그를 Apache 2.0 라이선스로 모두 공개
- **다양한 모델 변형**: 서로 다른 아키텍처, 옵티마이저, 하드웨어에 대응하는 7B 모델 4개 변형과 1B 모델 공개
- **포괄적 데이터셋**: 11.5TB의 Dolma 데이터셋으로 2T 토큰 이상 학습, Common Crawl, GitHub, Reddit 등 6개 소스에서 2.668조 토큰 포함
- **평가 인프라**: Catwalk(다운스트림 평가)와 Paloma(퍼플렉시티 기반 평가) 포함한 완전한 평가 프레임워크 제공
- **적응 기법**: TÜLU 데이터를 활용한 명령어 미세조정(instruction finetuning) 및 선호도 정렬(preference alignment) 시연

## How


- Decoder-only transformer 아키텍처에 PaLM/LLaMA 개선 사항 적용 (편향 제거, 비매개변수 layer norm, SwiGLU 활성화함수, RoPE 위치 임베딩)
- Dolma 데이터셋 구축: 언어 필터링 → 품질 필터링 → 콘텐츠 필터링 → 중복 제거 → 다중 소스 혼합 → 토큰화 파이프라인
- in-loop 평가 설정으로 아키텍처 선택 최적화 (훈련 처리량 최대화 vs 손실 스파이크/발산 위험 최소화)
- AdamW 옵티마이저 사용 (β₁=0.9, β₂=0.95, ε=1.0E-5) 및 배치 크기 ~4M으로 학습
- 수백 개의 중간 체크포인트를 HuggingFace에서 제공

## Originality

- 기존 Pythia, BLOOM 이후 가장 포괄적인 공개 모델 프레임워크: 데이터, 코드, 로그, 체크포인트를 모두 투명하게 공개
- Dolma 데이터셋의 개발과 공개 - 데이터 큐레이션 원칙, 도구, 분석 자료를 모두 함께 제공
- WIMBD 등 데이터셋 분석 도구 오픈소스화로 재현성 및 추가 연구 가능성 극대화
- 여러 하드웨어 유형에서의 다양한 모델 변형 제공으로 실제 적용 가능성 증대

## Limitation & Further Study

- 모델 규모가 7B/1B 수준으로 최근 주요 모델들(Llama 2 70B, GPT-4)보다 작음
- LLM360과 유사한 목표를 가진 경쟁적 연구가 동시에 진행되고 있음
- 평가 결과가 논문 일부에서만 제시되어 있으며, 더 광범위한 벤치마크 비교 필요
- 안전성(safety) 및 정렬(alignment)에 대한 상세한 분석이 제한적
- **후속 연구**: (1) 사전학습 데이터와 모델 성능의 관계 심화 연구, (2) 더 큰 규모 모델로의 확장, (3) 다양한 언어에 대한 지원 확대, (4) 강화학습 기반 정렬 방법 개발

## Evaluation

- Novelty: 3/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: OLMo는 완전한 개방성과 투명성을 바탕으로 언어 모델 연구의 새로운 표준을 제시하며, 과학적 재현성과 커뮤니티 혁신을 크게 가능하게 하는 중요한 기여이다.

## Related Papers

- 🏛 기반 연구: [[papers/1079_REFORMS_Consensus-based_Recommendations_for_Machine-learning/review]] — 기계학습 기반 과학 연구의 타당성과 재현성을 보장하는 REFORMS 체크리스트가 공개 언어 모델 연구의 품질 기준을 제공한다.
- 🧪 응용 사례: [[papers/1115_Google_Scholar_Microsoft_Academic_Scopus_Dimensions_Web_of_S/review]] — 다양한 학술 데이터베이스 비교 연구를 통해 OLMo와 같은 공개 모델의 과학적 연구 활용도를 실증적으로 평가할 수 있다.
