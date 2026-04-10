---
title: "779_Supporting_assessment_of_novelty_of_design_problems_using_co"
authors:
  - "Sanjay Singh"
  - "Amaresh Chakrabarti"
date: "2024"
doi: "미기재"
arxiv: ""
score: 4.0
essence: "본 논문은 SAPPhIRE 인과관계 모델을 활용하여 설계 문제(design problem)의 신규성(novelty)을 정량적으로 평가하는 프레임워크를 제안한다. 현재 문제와 과거 문제 데이터베이스 간의 텍스트 유사성을 SAPPhIRE의 다양한 추상화 수준에서 비교하여 신규성을 측정한다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/Materials_Discovery_Hypotheses"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Singh and Chakrabarti_2024_Supporting assessment of novelty of design problems using concept of problem sapphire.pdf"
---

# Supporting assessment of novelty of design problems using concept of problem sapphire

> **저자**: Sanjay Singh, Amaresh Chakrabarti | **날짜**: 2024 | **DOI**: [미기재]()

---

## Essence

![Fig. 2](figures/fig2.webp) 
*설계 문제의 신규성 평가를 위한 프레임워크*

본 논문은 SAPPhIRE 인과관계 모델을 활용하여 설계 문제(design problem)의 신규성(novelty)을 정량적으로 평가하는 프레임워크를 제안한다. 현재 문제와 과거 문제 데이터베이스 간의 텍스트 유사성을 SAPPhIRE의 다양한 추상화 수준에서 비교하여 신규성을 측정한다.

## Motivation

- **Known**: 
  - 설계 솔루션의 신규성 평가 방법론이 다수 존재 (빈도 기반, 거리 기반 측정)
  - 태스크 명확화(task clarification) 단계는 설계 프로세스에서 가장 조기 단계로, 변화에 대응하기 가장 효과적이고 비용-효율적
  
- **Gap**: 
  - 기존 연구는 설계 **솔루션**의 신규성만 평가 (예: Sarkar & Chakrabarti, Shah et al.)
  - 설계 **문제**의 신규성에 대한 평가 방법론이 부재
  - 문제 해결 초기 단계에서 문제의 신규성 파악이 자원 배분과 혁신 전략에 미치는 영향을 간과
  
- **Why**: 
  - 전체 설계 솔루션의 신규성은 문제의 신규성과 솔루션의 신규성 모두에 영향을 받음
  - 신규한 문제일수록 고부가가치 솔루션 개발 가능성 높음
  - 조기 단계에서의 신규성 평가가 R&D 자원의 전략적 배분을 가능하게 함
  
- **Approach**: 
  - SAPPhIRE 모델의 7개 추상화 수준(State change, Action, Parts, Physical Phenomena, Input, oRgan, Effect)을 설계 문제 분석에 적용
  - BERT 의미유사성 및 코사인 거리 기반 자동화된 비교 시스템 개발
  - 특허 데이터베이스와 설문조사를 통해 과거/현재 문제 수집 및 비교

## Achievement

![Fig. 1](figures/fig1.webp) 
*SAPPhIRE 인과관계 모델*

![Fig. 4](figures/fig4.webp)
*Problem SAPPhIRE 모델*

1. **신규성 평가 프레임워크 확립**: 
   - 8단계 체계적 방법론 제시 (문제 수집 → SAPPhIRE 변환 → 다층 유사성 비교 → 신규성 점수 산출)
   - 정성적 해석 범위 설정: 0-0.3 (낮음), 0.3-0.7 (중간), 0.7-1.0 (높음)

2. **자동화 솔루션 구현**: 
   - 사전학습 BERT 모델을 통한 액션 수준(Action level) 매칭 자동화
   - 워드 벡터 기반 코사인 거리 계산으로 처리 시간 단축
   - 수동 평가의 테디움(tedious) 문제 해결

3. **사례 연구를 통한 검증**: 
   - 전기 케틀(electric kettle) 사례에서 실제 적용 가능성 입증
   - 9개의 현재 문제 중 1개가 높은 신규성을 가짐을 확인

## How

![Fig. 5](figures/fig5.webp)
*과거 문제의 Problem SAPPhIREs ("액체 유출" 문제)*

**8단계 방법론**:

1. **과거 문제 수집**: 특허 데이터베이스 및 온라인 소스에서 과거 설계 문제 수집 및 분류
   
2. **현재 문제 수집**: 설문조사를 통해 이해관계자가 직면한 현재 문제 확보

3. **Problem SAPPhIRE 변환**: 자연언어 문제를 SAPPhIRE 모델의 7개 추상화 수준으로 기술
   - 각 수준에서 인과관계적 설명 제공

4. **Action 수준 매칭 (자동화)**: 
   - BERT 의미유사성을 사용하여 과거/현재 문제 간 액션 수준 비교
   - 매칭되는 문제 쌍만 후속 분석 대상으로 선정

5. **다층 유사성 비교**: 
   - Action 매칭된 쌍에 대해 나머지 6개 수준에서 문장/단어 유사성 분석
   - 워드벡터 기반 코사인 거리 계산

6. **수준별 유사성 점수 계산**: 
   - 각 SAPPhIRE 수준에서 Novelty = (1 - Similarity) 계산

7. **종합 신규성 점수**: 
   - 모든 수준의 신규성 점수 평균값으로 최종 점수 산출

8. **정성적 해석**: 
   - 0.7-1.0: 높은 신규성 (기존에 해결되지 않은 새로운 문제)
   - 0.3-0.7: 중간 신규성 (변형되거나 개선된 기존 문제)
   - 0-0.3: 낮은 신규성 (이미 알려진 문제)

## Originality

- **최초 시도**: 설계 문제의 신규성을 체계적으로 평가하는 학술적 시도
  
- **SAPPhIRE의 혁신적 응용**: 기존에 제품/솔루션 평가에만 사용된 SAPPhIRE 모델을 문제 기술(problem specification)에 적용
  
- **거리 기반 측정의 우월성**: 빈도 기반 측정의 한계(집합 크기 의존성, 비교 기준 모호성)를 극복하고, 일관된 참조점(reference database)에 대한 거리 기반 측정 도입
  
- **자동화 시스템**: 기존의 전문가 수동 평가를 BERT + 코사인 거리 알고리즘으로 자동화하여 확장성 향상

## Limitation & Further Study

**한계**:
- **샘플 크기 제한**: 단일 제품(전기 케틀) 사례만으로 검증되어 일반화 가능성 미흡
  
- **문제 기술의 주관성**: Problem SAPPhIRE로 변환하는 과정에서 분석자의 해석 차이 가능성
  
- **데이터베이스 완전성 가정**: 과거 문제 데이터베이스가 충분히 대표성을 가진다는 암묵적 가정
  
- **다중 도메인 검증 부재**: 산업 설계, 소프트웨어, 의료기기 등 다양한 도메인에서의 적용성 미확인
  
- **Action 수준 매칭의 제약**: Action 수준에서 먼저 필터링되어, 다른 수준에서만 신규한 문제를 놓칠 수 있음

**후속 연구**:
- 여러 제품/도메인에 대한 대규모 사례 연구로 신규성 평가 기준의 타당성 검증
- 문제 기술 과정의 표준화 및 지침서 개발
- 머신러닝 기반 자동 Problem SAPPhIRE 생성 알고리즘 개발
- 문제 신규성 평가 결과와 최종 설계 솔루션의 혁신도 간의 상관관계 분석
- 실시간 설계 프로세스에 통합된 협업 플랫폼 구축

## Evaluation

| 평가 항목 | 점수 | 근거 |
|---------|------|------|
| **Novelty (독창성)** | 4.5/5 | 설계 문제 신규성 평가라는 새로운 연구 주제 개척; SAPPhIRE 응용의 창의성; 다만 방법론 자체는 기존 기술(BERT, 코사인 유사성)의 조합 |
| **Technical Soundness (기술 타당성)** | 4/5 | SAPPhIRE 모델의 이론적 기반 견고; 다층 유사성 비교 논리 합리적; 다만 자동화 과정의 에러율이나 정확도 검증 미흡; Action 수준 사전 필터링의 정당성 미제시 |
| **Significance (중요성)** | 4/5 | 조기 설계 단계에서의 문제 신규성 평가는 전략적 가치 높음; R&D 자원 배분에 실질적 기여 가능; 다만 실제 산업 적용 사례와 영향도가 미흡 |
| **Clarity (명확성)** | 3.5/5 | 8단계 방법론이 명확히 제시됨; 사례 연구가 구체적; 다만 논문이 미완성인 듯 보임(본문이 중단됨); Problem SAPPhIRE 모델의 수준별 정의가 충분하지 않음 |
| **Overall (종합)** | 4/5 | 설계 혁신 초기 단계에서 문제의 신규성을 평가하려는 실용적이고 체계적인 접근; SAPPhIRE의 새로운 응용 가치; 다만 단일 사례 검증, 자동화 검증 부족, 논문 완성도 미흡 |

**총평**: 이 연구는 설계 과정에서 간과되어온 문제 신규성 평가에 처음 도전하는 가치 있는 시도로, SAPPhIRE 모델의 창의적 응용과 자동화 시스템을 제시하였다. 그러나 단일 제품 사례에 국한된 검증, 자동화 알고리즘의 정확성 미검증, 그리고 불완전한 논문 구성이 영향력을 제한한다. 후속 연구에서 다양한 도메인의 대규모 검증과 실제 산업 적용 사례를 통해 실용성을 입증할 필요가 있다.

## Related Papers

- 🏛 기반 연구: [[papers/777_Structuring_scientific_innovation_A_framework_for_modeling_a/review]] — 파괴적 혁신 지수를 통한 혁신적 지식 조합 평가 방법이 설계 문제 신규성 평가의 개념적 기반을 제공한다.
- 🔄 다른 접근: [[papers/010_A_hierarchical_framework_for_measuring_scientific_paper_inno/review]] — 과학 논문의 혁신성 측정이라는 유사한 목표이지만 SAPPhIRE 모델과 계층적 프레임워크라는 다른 접근법을 사용한다.
- 🔗 후속 연구: [[papers/313_Enabling_ai_scientists_to_recognize_innovation_A_domain-agno/review]] — 혁신 인식을 위한 도메인 무관 방법론을 설계 문제의 신규성 평가라는 구체적 영역에 적용한다.
- 🧪 응용 사례: [[papers/178_Can_ai_examine_novelty_of_patents_Novelty_evaluation_based_o/review]] — 설계 문제의 참신성 평가를 위한 코사인 유사도 사용으로 본 논문의 특허 신규성 평가 방법론을 설계 도메인에 적용한다.
