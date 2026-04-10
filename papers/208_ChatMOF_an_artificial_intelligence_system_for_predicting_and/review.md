---
title: "208_ChatMOF_an_artificial_intelligence_system_for_predicting_and"
authors:
  - "Y. Kang"
  - "Jihan Kim"
date: "2024"
doi: "10.1038/s41467-024-48998-4"
arxiv: ""
score: 4.3
essence: "대규모 언어 모델(Large Language Model, LLM)을 활용하여 금속-유기 골격(Metal-Organic Framework, MOF)의 성질을 예측하고 신규 구조를 생성할 수 있는 인공지능 시스템 ChatMOF를 개발했다. 자연스러운 텍스트 입력만으로 복잡한 재료 과학 작업을 자동화할 수 있음을 보여주었다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/Multi-Agent_Scientific_Frameworks"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Kang and Kim_2024_ChatMOF an artificial intelligence system for predicting and generating metal-organic frameworks us.pdf"
---

# ChatMOF: an artificial intelligence system for predicting and generating metal-organic frameworks using large language models

> **저자**: Y. Kang, Jihan Kim | **날짜**: 2024 | **DOI**: [10.1038/s41467-024-48998-4](https://doi.org/10.1038/s41467-024-48998-4)

---

## Essence

![Figure 1](figures/fig1.webp)
*Fig. 1 | ChatMOF의 개념도(a)와 구조도(b). ChatMOF는 에이전트, 도구 모음, 평가기의 세 가지 핵심 요소로 구성되어 자연어 질문에 기반하여 금속-유기 골격의 성질을 예측하고 구조를 생성한다.*

대규모 언어 모델(Large Language Model, LLM)을 활용하여 금속-유기 골격(Metal-Organic Framework, MOF)의 성질을 예측하고 신규 구조를 생성할 수 있는 인공지능 시스템 ChatMOF를 개발했다. 자연스러운 텍스트 입력만으로 복잡한 재료 과학 작업을 자동화할 수 있음을 보여주었다.

## Motivation

- **Known**: 트랜스포머 기반 대규모 언어 모델(GPT-4, GPT-3.5 등)이 화학(chemistry), 의학(medicine), 생물학(biology) 등 다양한 분야에서 활용되고 있으며, 자율적 LLM 에이전트가 데이터 처리 및 결과 생성에서 우수한 성능을 보임.

- **Gap**: 재료 과학 분야, 특히 MOF와 같은 복잡한 고급 재료에 대한 LLM 활용은 여전히 미흡함. 두 가지 주요 문제: (1) 복잡한 재료의 구조를 텍스트로 표현할 수 있는 형식이 부족함, (2) 재료 과학 분야의 텍스트 형식 학습 데이터 부족.

- **Why**: MOF는 높은 기공성(porosity), 넓은 표면적(surface area), 우수한 조절 가능성(tunability) 때문에 화학 응용에 광범위하게 사용되며, 새로운 재료 설계 자동화의 필요성이 높음.

- **Approach**: LLM을 데이터베이스(CoREMOF, QMOF, MOFkey, DigiMOF)와 기계학습 모델(MOFTransformer)로 통합하는 멀티 컴포넌트 시스템 설계.

## Achievement

![Figure 2](figures/fig2.webp)
*Fig. 2 | 테이블 검색 도구의 예시. 사용자 질문에 따라 ChatMOF가 자동으로 데이터베이스에서 정보를 추출한다.*

![Figure 3](figures/fig3.webp)
*Fig. 3 | 예측기(predictor)의 사용 예시. MOFTransformer 모델을 선택하여 재료의 성질을 예측한다.*

1. **높은 예측 정확도**: GPT-4 기반 ChatMOF는 검색(searching) 96.9%, 예측(predicting) 95.7%, 생성(generating) 87.5%의 높은 정확도 달성.

2. **다중 작업 수행**: 데이터 검색(data retrieval), 성질 예측(property prediction), 구조 생성(structure generation)의 세 가지 핵심 작업을 자동으로 수행하며, 자연언어 입력만으로 사용자가 원하는 성질의 MOF 생성 가능.

3. **실질적 재료 생성**: 기존 LLM 연구가 문헌에서 추출한 데이터 기반의 응답 생성에 국한된 반면, ChatMOF는 실제 재료 구조 생성이 가능.

## How

![Figure 4](figures/fig4.webp)
*Fig. 4 | 유전 알고리즘(genetic algorithm)을 활용한 MOF 생성 프로세스.*

![Figure 5](figures/fig5.webp)
*Fig. 5 | 복합적 다단계 질문의 예시. CO₂ Henry 계수와 관련된 복잡한 쿼리 처리.*

**시스템 아키텍처:**
- **에이전트(Agent)**: ReAct 및 MRKL 방법론 기반으로 사용자 쿼리를 분석, 행동 결정, 입력 관리, 결과 관찰의 4단계 운영 수행. LLM을 중앙 조정자로 활용하여 전체 프로세스 관리.

- **도구 모음(Toolkit)**: 4가지 범주로 분류
  - **테이블 검색(Table-searcher)**: CoREMOF, QMOF 데이터베이스에서 사전 계산된 성질 추출
  - **인터넷 검색(Internet-searcher)**: 온라인 정보 수집
  - **예측기(Predictor)**: MOFTransformer 기계학습 모델을 활용한 성질 예측
  - **생성기(Generator)**: 유전 알고리즘을 통한 새로운 MOF 구조 생성
  - **유틸리티(Utilities)**: 계산기, 시각화기, 파일 입출력 등

- **평가기(Evaluator)**: 도구로부터 얻은 출력을 평가하여 최종 응답 생성 또는 재계획 지시.

**주요 기술 요소:**
- MOFTransformer: 원자, 결합 등 국소 특성과 표면적, 위상(topology) 등 전역 특성을 활용하여 100만 개의 가상 MOF로 사전학습 후 특정 성질별 미세조정.
- MOFkey 데이터베이스: 규칙 기반 방법으로 유기 링커, 금속 클러스터, 위상 정보 제공.
- DigiMOF 데이터베이스: 텍스트 마이닝을 통한 합성 조건 정보(유기 전구체, 금속 전구체, 용매).

## Originality

- **LLM과 재료 과학의 통합**: 문헌 정보 추출 수준을 넘어 실제 재료 구조 생성까지 확장한 혁신적 접근법.

- **구조화된 멀티 컴포넌트 설계**: 에이전트, 도구, 평가기의 계층적 구조로 자동 추론과 도구 선택을 효율적으로 구현.

- **자연언어 인터페이스의 실질화**: 형식적 쿼리 없이 자연언어만으로 전문적 재료 과학 작업 수행 가능하게 함으로써 사용성과 접근성 대폭 향상.

- **역설계(Inverse Design) 구현**: 사용자가 원하는 성질을 명시하면 그에 맞는 MOF 구조를 자동 생성하는 기능.

## Limitation & Further Study

- **생성 정확도 제약**: 87.5%의 생성 정확도는 검색, 예측에 비해 낮으며, 생성된 구조의 합성 가능성(synthesizability) 및 실험적 검증이 필요함.

- **데이터베이스 의존성**: 시스템의 성능이 CoREMOF, QMOF 등 기존 데이터베이스의 완전성과 정확성에 크게 의존하며, 데이터가 없는 신규 재료 클래스에 대해서는 한계 존재.

- **LLM의 제한된 전문성**: 보충 자료에서 보여주듯이 LLM 단독으로는 MOF 관련 전문 질문에 대한 정확한 응답 불가능하므로, 외부 도구와의 통합이 필수적.

- **계산 비용**: MOFTransformer 예측의 빠른 속도는 장점이나, 생성 프로세스(유전 알고리즘)의 계산 시간은 명시되지 않음.

- **후속 연구 방향**:
  - 합성 가능성 평가 모듈 추가
  - 실험적 검증을 통한 생성 구조의 신뢰성 확인
  - MOF 외 다른 다공성 재료(zeolite, COF 등)로 확장
  - 더 큰 규모의 재료 데이터베이스 구축 및 활용
  - 미세조정된 도메인 특화 LLM 개발

## Evaluation

- **Novelty (신독성)**: 4.5/5
  - LLM을 재료 설계에 활용하는 것 자체는 새로운 경향이나, 멀티 컴포넌트 시스템 설계와 실제 구조 생성까지 통합한 점은 혁신적. 다만 개별 기술(MOFTransformer, 유전 알고리즘)은 기존 방법론.

- **Technical Soundness (기술적 타당성)**: 4/5
  - 시스템 설계가 논리적이고 ReAct, MRKL 등 확립된 방법론 기반. 그러나 생성 정확도(87.5%)가 상대적으로 낮고, 생성 구조의 실제 합성 가능성에 대한 검증 부재.

- **Significance (의의)**: 4.5/5
  - MOF 설계 자동화는 재료 과학에서 상당한 실질적 가치 있음. 자연언어 인터페이스는 비전문가도 접근 가능하게 하는 장점. 그러나 현재는 MOF 중심으로 제한적.

- **Clarity (명확성)**: 4.5/5
  - 전반적으로 잘 구성되고 Figure로 개념을 효과적으로 설명. 다만 MOFTransformer의 상세 구조와 유전 알고리즘의 구체적 파라미터, 계산 시간 등 기술 세부사항 부분적 생략.

- **Overall (종합)**: 4.3/5

**총평**: ChatMOF는 대규모 언어 모델을 데이터베이스 및 기계학습과 결합하여 재료 과학 분야에 실질적 가치를 제공하는 혁신적 AI 시스템이며, 특히 자연언어 기반 인터페이스와 구조 생성 기능은 주목할 만하나, 생성 정확도 향상과 실험적 검증을 통한 추가 개발이 필요하다.

## Related Papers

- 🔄 다른 접근: [[papers/398_Harnessing_large_language_models_for_scientific_novelty_dete/review]] — MOF 예측과 생성에서 AI 시스템과 LLM 기반 데이터 수집이라는 서로 다른 접근법으로 화학 소재 연구를 자동화한다.
- 🔗 후속 연구: [[papers/523_MatterChat_A_Multi-Modal_LLM_for_Material_Science/review]] — 특정 화학 소재(MOF)에 특화된 시스템을 더 넓은 재료과학 영역으로 확장하여 포괄적인 멀티모달 LLM을 구축한다.
- 🏛 기반 연구: [[papers/764_Sparks_Multi-Agent_Artificial_Intelligence_Model_Discovers_P/review]] — 특정 과학 영역에서의 AI 시스템 성공 사례가 일반적인 자동화된 과학 발견의 가능성을 뒷받침한다.
- 🔄 다른 접근: [[papers/298_Earth-Agent_Unlocking_the_Full_Landscape_of_Earth_Observatio/review]] — 지구 관측 데이터와 화학 소재라는 서로 다른 과학 영역에서 멀티모달 AI 에이전트 접근법을 비교할 수 있다.
- 🔄 다른 접근: [[papers/398_Harnessing_large_language_models_for_scientific_novelty_dete/review]] — MOF와 화학 소재라는 유사한 영역에서 LLM 기반 지식 추출과 AI 시스템 구축의 서로 다른 접근법을 비교한다.
