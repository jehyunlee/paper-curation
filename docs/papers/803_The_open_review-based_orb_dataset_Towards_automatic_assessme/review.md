---
title: "803_The_open_review-based_orb_dataset_Towards_automatic_assessme"
authors:
  - "Jarosław Szumega"
  - "Lamine Bougueroua"
  - "Blerina Gkotse"
  - "Pierre Jouvelot"
  - "Federico Ravotti"
date: "2023"
doi: "미명시"
arxiv: ""
score: 3.5
essence: "본 논문은 OpenReview.net과 SciPost.org에서 수집한 36,000개 이상의 과학논문과 89,000개 이상의 피어리뷰로 구성된 공개 피어리뷰 데이터셋(ORB: Open Review-Based dataset)을 소개한다. NLP 기반 자동 논문 평가 및 고에너지물리 실험 제안의 자동 심사를 지원하기 위한 포괄적인 데이터 인프라를 제공한다."
tags:
  - "cat/Academic_Peer_Review_Automation"
  - "sub/Citation_Dataset_Analysis"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Szumega et al._2023_The open review-based (orb) dataset Towards automatic assessment of scientific papers and experimen.pdf"
---

# The open review-based (orb) dataset: Towards automatic assessment of scientific papers and experiment proposals in high-energy physics

> **저자**: Jarosław Szumega, Lamine Bougueroua, Blerina Gkotse, Pierre Jouvelot, Federico Ravotti | **날짜**: 2023 | **DOI**: [미명시](https://doi.org/)

---

## Essence

본 논문은 OpenReview.net과 SciPost.org에서 수집한 36,000개 이상의 과학논문과 89,000개 이상의 피어리뷰로 구성된 공개 피어리뷰 데이터셋(ORB: Open Review-Based dataset)을 소개한다. NLP 기반 자동 논문 평가 및 고에너지물리 실험 제안의 자동 심사를 지원하기 위한 포괄적인 데이터 인프라를 제공한다.

## Motivation

- **Known**: 오픈 사이언스 운동과 함께 오픈 피어리뷰(Open Peer Review, OPR)가 확산되고 있으나, 공개 접근 가능한 피어리뷰 데이터셋이 극히 부족함. 기존 데이터셋들은 컴퓨터과학 분야의 특정 학회(NeurIPS 등)에만 집중되어 있음.

- **Gap**: RADNEXT 프로젝트에서 고에너지물리(HEP) 실험 제안의 자동 평가를 위한 머신러닝 모델을 개발하려 하나, 훈련에 필요한 데이터가 극도로 부족함. 또한 기존 오픈 피어리뷰 데이터셋은 전체 파이프라인(제출, 리뷰, 최종 결정)을 포괄하지 못함.

- **Why**: 머신러닝 기반 자동 평가 시스템이 편향 없이 높은 품질을 유지하려면 대규모의 다양한 샘플 데이터가 필수적임. 특히 거부된 논문과 상세한 반박(counter-examples)도 중요한 학습 자료임.

- **Approach**: 오픈 사이언스 원칙을 준수하는 OpenReview.net과 SciPost.org 플랫폼에서 대규모 논문-리뷰 데이터를 수집하고, 재사용 가능한 소프트웨어 인프라(Python API, ETL 프로세스)를 함께 제공하여 미래의 추가 소스 통합을 용이하게 함.

## Achievement

![Figure 3](figures/fig3.webp) *ETL 프로세스 및 연속적인 단계별 데이터 표현*

1. **포괄적 데이터셋 구축**: 36,949개의 고유 제출물, 92,879개의 리뷰, 최종 수용/거부 결정이 포함된 멀티도메인 데이터셋 제공. OpenReview.net에서 34,030개, SciPost.org에서 2,919개의 논문 수집.

2. **재사용 가능한 소프트웨어 인프라**: 
   - Python 기반 인터페이스 및 구현 (OrbRaw*, Orb* dataclasses)
   - 자동화된 ETL (Extract, Transform, Load) 프로세스로 정기적 업데이트 가능
   - REST API 기반 데이터 추출 및 웹 스크래핑 모듈 포함

3. **원본 데이터 기반 설계**: 기존 데이터셋과 달리 원본 소스 데이터를 보존하고, 사용자가 필요에 따라 전처리를 수행할 수 있도록 설계하여 실험의 범위를 확대함.

4. **NLP 응용 가능성 입증**: 
   - 텍스트 임베딩 기반 논문 수용 예측
   - 임베딩으로부터 채점 통계 추론

## How

![Figure 1](figures/fig1.webp) *OrbRaw* 인터페이스와 구현을 나타내는 UML 다이어그램*

![Figure 2](figures/fig2.webp) *ORB 프레임워크의 대상 Orb* 데이터클래스. OrbPapers의 모든 OrbSubmissions*

- **데이터 소스 선택**: 오픈 액세스 정책과 API/스크래핑 접근성을 기준으로 OpenReview.net (REST API 활용)과 SciPost.org (웹 스크래핑) 선정

- **데이터 구조 통일**: 
  - OpenReview.net의 비정형 "Note" 타입을 표준화된 OrbRaw 인터페이스로 변환
  - SciPost의 구조화된 6점 채점 시스템을 공통 스키마에 맞춤
  - 모든 메타데이터(제출 시간, 리뷰어 익명성, 최종 결정 등)를 통합

- **ETL 파이프라인 설계**: 
  1. Extract: API/웹 스크래핑으로 원본 데이터 수집
  2. Transform: 검증, 정규화, 스키마 매핑
  3. Load: 구조화된 Python dataclass 및 JSON 파일로 저장

- **확장성 고려**: 추가 데이터 소스(MDPI, PeerJ 등)를 향후 통합 가능하도록 모듈화된 구조 채택

- **NLP 실험**: 
  - Sentence-BERT 등을 활용한 논문 초록과 리뷰의 임베딩 생성
  - 임베딩 기반 수용/거부 분류기 훈련
  - 리뷰 점수 예측 모델 개발

## Originality

- 고에너지물리 도메인을 명시적으로 지원하는 **첫 대규모 오픈 피어리뷰 데이터셋**: 기존 데이터셋들이 NeurIPS, ICLR 등 컴퓨터과학에 편중되어 있으나, ORB는 멀티도메인(arXiv 포함)을 포괄.

- **원본 데이터 보존 + 사용자 맞춤형 전처리**: 기존 연구들이 수동 주석(annotation)과 강한 전처리를 적용하여 재사용성을 제한했으나, ORB는 원본 구조를 유지하고 API를 제공하여 다양한 실험 가능.

- **완전한 리뷰 파이프라인**: 제출물, 리뷰어 의견, 메타리뷰, 최종 결정을 모두 포함하여 리뷰 품질, 편향 분석, 결정 예측 등 다층적 연구 가능.

- **지속 가능한 인프라**: 단순 데이터 스냅샷이 아닌 자동화된 ETL 프로세스로 정기적 업데이트 및 새로운 소스 추가가 용이.

## Limitation & Further Study

**한계**:
- OpenReview.net의 불일관한 데이터 스키마로 인한 정보 손실 위험 (누락된 필드 처리 필요)
- SciPost.org의 API 부재로 웹 스크래핑 의존 → 플랫폼 변경 시 유지보수 부담
- 초기 버전은 영어 논문에만 국한 (다국어 지원 필요)
- 두 플랫폼 간 채점 시스템 상이로 인한 정규화의 어려움
- 리뷰어 익명성 정책 차이로 인한 데이터 일관성 문제
- 초기 NLP 실험이 기초적 수준 (BERT 임베딩 + 선형 분류기)으로 제한적

**후속 연구**:
- 논문 텍스트의 구조적 특징(제목, 초록, 결론 등 섹션별 분석)을 활용한 고도화된 예측 모델 개발
- 리뷰 텍스트의 감정 분석(sentiment analysis)과 논거 추출(argument mining)
- 리뷰어 편향 탐지 및 정량화
- 고에너지물리 전문 도메인 모델(SciBERT, SPECTER 등) 활용
- 추가 출판사(Springer, IEEE, MDPI)로부터 데이터 수집 및 통합
- 논문-리뷰 간 상호작용 분석 (저자 회신, 수정 반영도 등)


## Evaluation

- Novelty: 4/5
- Technical Soundness: 3.5/5
- Significance: 4/5
- Clarity: 3.5/5
- Overall: 3.5/5

**총평**: ORB 데이터셋은 오픈 피어리뷰 분야의 데이터 부족 문제를 크게 완화할 수 있는 중요한 자원이며, 특히 고에너지물리 실험 제안 자동 평가라는 구체적 응용을 지원한다는 점에서 가치가 있다. 다만 데이터 통합의 복잡성, NLP 실험의 기초적 수준, 플랫폼 의존성 등으로 인해 기술적 견고성에서 개선 여지가 있고, 대규모 실제 응용까지는 추가 연구가 필요하다. 오픈 사이언스 커뮤니티에 긍정적 기여를 할 수 있는 리소스이나, 개별 논문으로서의 기술적 혁신성은 제한적이다.

## Related Papers

- 🔄 다른 접근: [[papers/519_MARG_Multi-Agent_Review_Generation_for_Scientific_Papers/review]] — 다중 에이전트 리뷰 생성이 ORB 데이터셋 기반 평가와 다른 접근 방식을 제시한다.
- 🔗 후속 연구: [[papers/654_Re_2_A_consistency-ensured_dataset_for_full-stage_peer_revie/review]] — 피어 리뷰 전 과정에 대한 일관성 보장 데이터셋이 ORB의 적용 범위를 확장한다.
- 🧪 응용 사례: [[papers/150_Benchmark_for_evaluation_and_analysis_of_citation_recommenda/review]] — 인용 추천 평가 벤치마크가 ORB 데이터셋의 NLP 기반 논문 평가에 적용된다.
- 🏛 기반 연구: [[papers/522_MatPilot_an_LLM-enabled_AI_Materials_Scientist_under_the_Fra/review]] — 대규모 과학 문헌 데이터셋이 ORB의 피어 리뷰 자동화 연구에 기초가 된다.
- 🏛 기반 연구: [[papers/591_Openreview_should_be_protected_and_leveraged_as_a_community/review]] — 오픈 리뷰 기반 데이터셋으로 자동 평가 연구의 기반이 되어 OpenReview 플랫폼의 가치를 실증적으로 보여준다.
