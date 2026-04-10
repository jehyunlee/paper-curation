---
title: "117_Augmenting_the_veracity_and_explanations_of_complex_fact_che"
authors:
  - "Xiaocheng Zhang"
  - "Xi Wang"
  - "Yifei Lu"
  - "Jianing Wang"
  - "Zhuangzhuang Ye"
date: "2024"
doi: "미제공"
arxiv: ""
score: 4.0
essence: "본 논문은 중국어 기반의 첫 번째 포괄적 사실 검증 벤치마크인 **TrendFact**를 제시하며, 설명 생성 일관성(ECS)과 핫스팟 인식 능력(HPA)을 평가하는 새로운 메트릭을 도입한다. 추가적으로 동적 증거 증강과 영향도 점수 기반 반복적 자기 성찰을 결합한 **FactISR** 프레임워크를 제안하여 대형 언어 모델의 사실 검증 성능을 향상시킨다."
tags:
  - "cat/Cognitive_AI_Evaluation_and_Benchmarking"
  - "sub/Multi-Hop_Reasoning_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Zhang et al._2024_Augmenting the veracity and explanations of complex fact checking via iterative self-revision with l.pdf"
---

# Augmenting the veracity and explanations of complex fact checking via iterative self-revision with llms

> **저자**: Xiaocheng Zhang, Xi Wang, Yifei Lu, Jianing Wang, Zhuangzhuang Ye, Mengjiao Bao, Peng Yan, Xiaohong Su | **날짜**: 2024 | **DOI**: [미제공](https://doi.org/)

---

## Essence

![Figure 1](figures/fig1.webp) *TrendFact의 수치 추론을 포함하는 사실 검증 예제: 故宮(자금성)의 나이에 관한 주장과 검증 과정*

본 논문은 중국어 기반의 첫 번째 포괄적 사실 검증 벤치마크인 **TrendFact**를 제시하며, 설명 생성 일관성(ECS)과 핫스팟 인식 능력(HPA)을 평가하는 새로운 메트릭을 도입한다. 추가적으로 동적 증거 증강과 영향도 점수 기반 반복적 자기 성찰을 결합한 **FactISR** 프레임워크를 제안하여 대형 언어 모델의 사실 검증 성능을 향상시킨다.

## Motivation

- **Known**: 기존 사실 검증 벤치마크(FEVER, HOVER 등)는 주로 영어 기반이며, 설명 생성 평가가 부족하고, 모든 주장을 동등하게 취급한다.

- **Gap**: 
  1. 기존 벤치마크는 텍스트 설명이 거의 없어 설명 생성 성능 평가 불가
  2. 사회적 영향도가 다른 주장들에 대한 차등적 처리 능력(HPA) 평가 불가
  3. 중국어 기반의 포괄적 사실 검증 벤치마크 부재

- **Why**: 소셜 미디어에서의 허위 정보 확산으로 인한 COVID-19 인포데믹 등 사회적 위험이 증가하고 있으며, 고영향도 사건에 대한 시스템의 우선 처리 능력이 중요해짐.

- **Approach**: 
  1. 트렌딩 플랫폼과 전문 사실 검증 데이터셋에서 7,643개 샘플 수집
  2. 366,634개의 증거 라이브러리 구축
  3. ECS(설명 일관성 점수)와 HCPI(핫스팟 주장 인식 지수) 메트릭 정의
  4. 동적 증거 증강 기반 반복적 자기 성찰 프레임워크 제안

## Achievement

![Figure 2](figures/fig2.webp) *TrendFact 구축 프로세스: 주장 수집, 필터링, 증강, 증거 라이브러리 구축 및 다단계 샘플 검토*

1. **TrendFact 벤치마크**: 
   - 중국어 기반 첫 포괄적 사실 검증 벤치마크
   - 증거 검색, 사실 검증, 설명 생성, HPA 평가 모두 지원
   - 5개 도메인(공중보건, 과학, 사회, 정치, 문화) 커버
   - 단일 증거 샘플 85%, 다중 증거 샘플 15% 포함

2. **새로운 평가 메트릭**:
   - **ECS (Explanation Consistency Score)**: 생성된 설명이 검증 결과와의 일관성 평가
   - **HCPI (Hotspot Claim Perception Index)**: 시스템이 고영향도 사건 처리 능력 평가

3. **FactISR 프레임워크**: 
   - 기존 RAG(Retrieval Augmented Generation)의 성능 저하 극복
   - 동적 증거 증강 + 영향도 점수 기반 반복 자기 성찰 결합
   - 대형 언어 모델의 성능 향상 달성

## How

![Figure 3](figures/fig3.webp) *FactISR의 개요: 반복적 추론 과정을 통한 증거 동적 증강 및 자기 성찰*

**TrendFact 구축 방법론**:
- 트렌딩 플랫폼(Weibo, Baidu 등)과 기존 CHEF 데이터셋에서 병렬 수집
- 두 가지 소스별 독립적 증강 프로세스 적용
  - 트렌딩 주장: 클레임 재작성, 증거 검색, 필터링
  - CHEF 주장: 라벨 수정, 설명 주석, 품질 검증
- 금(gold) 증거와 검색 기반 증거 결합으로 증거 라이브러리 구성

**FactISR 방법론**:
- **동적 증거 증강**: 초기 검색 후 모델의 추론 결과에 기반하여 추가 증거 검색
- **영향도 점수 기반 반복 자기 성찰**: 주장의 사회적 영향도에 따라 다양한 강도의 재검토 수행
- **계산 효율성 개선**: 필요한 경우에만 반복 수행

**평가 메트릭 정의**:
- HPA = f(C, HI, R): 사건 카테고리, 핫스팟 지표(조회수, 토론량), 계산 리소스의 함수
- 핫스팟 지표: 조회수(Views), 댓글(Posts), 참여도(Engagements), 토론(Discussions)
- 위험도 점수(Risk Score)와 핫스팟 지표로부터 영향도 점수(Influence Score) 계산

## Originality

- **중국어 기반 포괄적 벤치마크**: 기존에 없던 설명 생성과 HPA 평가를 모두 포함하는 중국어 벤치마크 최초 개발

- **HPA 개념 도입**: "핫스팟 인식 능력"이라는 새로운 평가 지표 정의로 고영향도 사건 처리 능력 측정 체계화

- **이중 메트릭 제안**: ECS와 HCPI라는 상호보완적 메트릭으로 설명의 신뢰성과 시스템의 우선순위 할당 능력 동시 평가

- **동적 증거 증강 기법**: 고정된 증거 검색 대신 모델의 추론 과정에 따라 동적으로 증거 추가 검색하는 새로운 접근법

- **대규모 증거 라이브러리**: 366,634개의 출판 날짜 정보를 포함한 시간 인식형 증거 라이브러리

## Limitation & Further Study

- **언어 제한**: 중국어 기반이라 다언어 확장 필요. 영어 및 기타 주요 언어의 유사 벤치마크 개발 요구

- **샘플 크기**: 7,643개 샘플은 다른 대규모 벤치마크(30,000+)에 비해 상대적으로 작음. 더욱 다양한 도메인과 주제 확장 필요

- **증거 라이브러리 구성**: 온라인 검색을 통한 증거 수집의 시간적 한계 및 정적 라이브러리의 현실성 저하

- **HPA 메트릭의 보편성**: 영향도 점수 계산이 트렌딩 플랫폼 특화적일 수 있어, 다양한 도메인과 언어로의 일반화 어려움

- **후속 연구 방향**:
  1. 실시간 핫스팟 변화에 대응하는 동적 증거 라이브러리 개발
  2. 멀티모달(이미지, 비디오 포함) 사실 검증 확장
  3. 엣지 기기에서의 경량화된 HPA 모델 개발
  4. 크로스랭귀지 전이 학습 연구

## Evaluation

- **Novelty**: 4.5/5 
  - 중국어 기반의 설명 생성 + HPA 평가 벤치마크는 신규성 높음
  - HPA 개념 도입 및 ECS, HCPI 메트릭은 창의적이나, 근본적 알고리즘 혁신은 제한적

- **Technical Soundness**: 4/5
  - TrendFact 구축 방법론 체계적이고 명확함
  - FactISR의 반복적 자기 성찰 개념은 합리적이나 이론적 정당화 부족
  - 실험 결과 분석이 비교적 상세하나 통계적 유의성 검증 미흡

- **Significance**: 4/5
  - 중국어권 NLP 및 사실 검증 연구에 중요한 기여
  - HPA 개념은 실무 적용성이 높으나, 전 세계적 영향도는 제한적
  - 트렌딩 플랫폼 특화라 학술적 일반성은 중간 수준

- **Clarity**: 3.5/5
  - 전반적인 구조와 방법론은 명확함
  - 일부 중국어 예시로 인한 가독성 제약
  - HPA 정의식(식 1)이 추상적이며 실제 계산 방식 설명 부족

- **Overall**: 4/5

**총평**: TrendFact 벤치마크는 중국어 기반 사실 검증에서 설명 생성과 고영향도 사건 처리 능력 평가라는 새로운 차원을 추가하여 의미 있는 기여를 하지만, 제안된 FactISR 방법의 이론적 깊이가 부족하고 영어 기반 연구 커뮤니티와의 연계성이 제한적이라는 점은 개선이 필요하다.

## Related Papers

- 🔗 후속 연구: [[papers/332_Fact-checking_complex_claims_with_program-guided_reasoning/review]] — 프로그램 안내 추론을 통한 복잡한 주장 사실 검증은 TrendFact의 중국어 사실 검증을 더욱 정교한 추론 방식으로 확장한 방법론입니다
- 🏛 기반 연구: [[papers/441_Investigating_zero-and_few-shot_generalization_in_fact_verif/review]] — 사실 검증에서 제로샷과 퓨샷 일반화 조사는 복잡한 사실 검증에서 설명 일관성과 핫스팟 인식 능력 평가의 이론적 기반을 제공합니다
- 🔄 다른 접근: [[papers/267_Defame_Dynamic_evidencebased_fact-checking_with_multimodal_e/review]] — 다중 모달 증거 기반 사실 검증과 동적 증거 증강 기반 사실 검증은 모두 복합적 증거를 활용하는 서로 다른 접근법입니다
- 🏛 기반 연구: [[papers/124_Automated_justification_production_for_claim_veracity_in_fac/review]] — 팩트체킹 시스템의 정확성과 설명력 향상을 위한 기반 연구로서 정당화 생성의 이론적 토대를 제공한다.
