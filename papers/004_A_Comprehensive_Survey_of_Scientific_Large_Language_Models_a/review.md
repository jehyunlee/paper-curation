---
title: "004_A_Comprehensive_Survey_of_Scientific_Large_Language_Models_a"
authors:
  - "Yu Zhang"
  - "Xiusi Chen"
  - "Bowen Jin"
  - "Sheng Wang"
  - "Shuiwang Ji"
date: "2024.06"
doi: ""
arxiv: ""
score: 4.0
essence: "260개 이상의 과학 분야 대규모 언어 모델(LLM)을 포괄적으로 조사하여 다양한 분야와 모달리티에서의 아키텍처, 사전학습 기법, 데이터셋, 평가 과제를 통합적으로 분석하고 과학 발견에의 응용을 제시한다."
tags:
  - "cat/Academic_Peer_Review_Automation"
  - "sub/AI_Publishing_Trends"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Zhang et al._2024_A Comprehensive Survey of Scientific Large Language Models and Their Applications in Scientific Disc.pdf"
---

# A Comprehensive Survey of Scientific Large Language Models and Their Applications in Scientific Discovery

> **저자**: Yu Zhang, Xiusi Chen, Bowen Jin, Sheng Wang, Shuiwang Ji, Wei Wang, Jiawei Han | **날짜**: 2024-06-16 | **URL**: [https://arxiv.org/abs/2406.10833](https://arxiv.org/abs/2406.10833)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1 depicts three major types of scien-*

260개 이상의 과학 분야 대규모 언어 모델(LLM)을 포괄적으로 조사하여 다양한 분야와 모달리티에서의 아키텍처, 사전학습 기법, 데이터셋, 평가 과제를 통합적으로 분석하고 과학 발견에의 응용을 제시한다.

## Motivation

- **Known**: 일반 도메인의 LLM이 NLP에 혁신을 가져왔으며, 이를 과학 분야에 적용한 연구들이 증가하고 있다. 그러나 기존 조사들은 특정 분야(생의학, 화학) 또는 단일 모달리티에만 집중했다.
- **Gap**: 과학 LLM 연구가 다양한 분야와 모달리티에 걸쳐 진행되고 있으나, 이들 간의 교차 분야·교차 모달 연결성과 공통점을 체계적으로 분석한 종합적 조사가 부족하다.
- **Why**: 과학 분야의 다양한 데이터 타입(텍스트, 분자, 단백질, 그래프 등)과 LLM 아키텍처의 공통 원리를 파악함으로써 향후 과학 LLM 개발의 방향을 제시할 수 있다. LLM이 과학 발견 프로세스의 여러 단계를 가속화할 수 있음을 보여준다.
- **Approach**: 260개 이상의 과학 LLM을 8개 과학 분야(일반과학, 수학, 물리, 화학, 재료과학, 생물, 의학, 지구과학)와 8개 모달리티(언어, 그래프, 비전, 테이블, 분자, 단백질, 게놈, 기후 시계열)로 분류하여 조사한다. 각 모델의 사전학습 데이터셋, 아키텍처, 평가 과제를 정리하고 Figure 1의 3가지 주요 사전학습 전략으로 통합한다.

## Achievement

![Figure 1](figures/fig1.webp)

*Figure 1 depicts three major types of scien-*

- **포괄적 조사**: 260개 이상의 과학 LLM을 체계적으로 분류 및 정리하여 구조화된 요약(Table A1-A6) 제공
- **교차 분야·교차 모달 연결성 규명**: MLM(Masked Language Modeling), 다음 토큰 예측(Next Token Prediction), 대조 학습(Contrastive Learning)의 3가지 사전학습 전략으로 통합적 관점 제시
- **다양한 모달리티 처리 방법 분석**: 자연 순서 데이터(텍스트, 서열), 선형화된 데이터(SMILES, 테이블), 비전-언어 융합(Vision Encoder + Text) 등의 변환 기법 체계화
- **과학 발견 응용 사례 제시**: 가설 생성, 정리 증명, 실험 설계, 신약 발견, 기상 예측 등 과학 발견 프로세스의 다양한 단계에서의 LLM 활용 방안 소개

## How

![Figure 1](figures/fig1.webp)

*Figure 1 depicts three major types of scien-*

- 과학 논문 데이터베이스(AMiner, MAG, Semantic Scholar, S2ORC)로부터 대규모 코퍼스 구성
- BERT 기반 MLM, GPT 기반 다음 토큰 예측, CLIP 기반 대조 학습 등 3가지 사전학습 패러다임 분류
- 텍스트 입력: 논문·질문 그대로 사용 / 그래프 입력: 메타데이터(출판지, 저자, 인용)를 텍스트로 연결 / 분자 입력: SMILES 형식으로 선형화 / 단백질 입력: FASTA 형식 활용 / 이미지 입력: 비전 인코더로 시각 토큰화
- 각 분야별 표준 평가 과제 정의: 일반과학(NER, RE, QA, 분류), 그래프 연관(링크 예측, 검색, 추천)
- 모델 크기 범위 추적: 약 100M에서 100B 파라미터까지의 스케일 분석
- Appendix A에 구조화된 표(Table A1-A6)로 모델 정보 체계화

## Originality

- **최초의 다분야·다모달 통합 조사**: 기존의 분야별(생의학, 화학), 모달리티별 조사와 달리 8개 과학 분야 × 8개 모달리티의 교차 분석으로 새로운 관점 제시
- **통일된 사전학습 프레임워크**: 서로 다른 데이터 타입을 처리하는 다양한 LLM들을 3가지 기본 사전학습 전략(MLM, Next Token Prediction, Contrastive Learning)으로 통합하여 설명
- **데이터 선형화 기법의 체계적 분류**: 분자(SMILES), 테이블(셀 병렬화), 크리스탈 구조(입자 좌표), 이미지(비전 인코더) 등 복잡한 과학 데이터를 LLM 입력으로 변환하는 다양한 방법 정리
- **과학 발견 프로세스 전주기 분석**: 가설 생성부터 실험 설계, 신약 발견까지 LLM이 과학 워크플로우의 어느 단계를 지원하는지 명시적으로 제시

## Limitation & Further Study

- 조사 시점(2024년 9월)의 LLM만 포함되어 이후 급속히 발전하는 분야의 최신 모델을 반영하지 못할 수 있음
- 모델의 정성적 비교가 중심이며 정량적 벤치마크 비교가 제한적 - 동일 데이터셋에서의 성능 비교 부재
- 소규모 또는 비영어 과학 LLM에 대한 충분한 커버리지 부족 가능성
- 다모달 모델(예: 텍스트+이미지)의 상호작용 메커니즘에 대한 깊이 있는 분석 부족
- 후속 연구: (1) 분야별 최적의 사전학습 전략 선택 기준 개발, (2) 작은 과학 코퍼스에서의 전이학습 효율성 연구, (3) 도메인별 LLM과 일반 LLM의 성능 격차 실증적 분석, (4) 다모달 LLM의 모달리티 간 상호작용 메커니즘 규명

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 이 논문은 과학 분야의 LLM 연구를 처음으로 통합적이고 체계적으로 조사한 중요한 참고 자료로, 260개 이상 모델의 아키텍처와 사전학습 기법을 3가지 프레임워크로 단순화하여 분야 간 연결성을 명확히 한다. 과학 발견의 실제 응용까지 다루어 실무적 가치가 높으나, 정량적 비교 분석과 다모달 상호작용의 깊이 있는 탐구가 추가되면 더욱 완성도 높은 조사가 될 수 있다.

## Related Papers

- 🔄 다른 접근: [[papers/353_From_Automation_to_Autonomy_A_Survey_on_Large_Language_Model/review]] — LLM의 자율성 진화보다는 분야별 응용에 초점을 맞춘 상호 보완적 조사 연구이다.
- 🔗 후속 연구: [[papers/720_Scientific_Large_Language_Models_A_Survey_on_Biological__Che/review]] — 생물학과 화학 분야 과학 LLM에 특화된 조사로 포괄적 조사를 세분화하여 심화한다.
- 🏛 기반 연구: [[papers/840_Transforming_Science_with_Large_Language_Models_A_Survey_on/review]] — LLM이 과학을 변화시키는 방식에 대한 조사로 과학 분야 LLM 응용의 이론적 배경을 제공한다.
- 🔄 다른 접근: [[papers/353_From_Automation_to_Autonomy_A_Survey_on_Large_Language_Model/review]] — 과학 분야 LLM의 포괄적 조사로 자율성보다는 응용 분야에 초점을 맞춘 상호 보완적 관점을 제공한다.
- 🔄 다른 접근: [[papers/664_RelevAI-Reviewer_A_Benchmark_on_AI_Reviewers_for_Survey_Pape/review]] — 과학 대규모 언어모델에 대한 포괄적 조사가 논문 관련성 평가라는 특정 응용에 대한 다른 접근을 보여준다.
