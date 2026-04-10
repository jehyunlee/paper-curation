---
title: "277_Discoverybench_Towards_data-driven_discovery_with_large_lang"
authors:
  - "Bodhisattwa Prasad Majumder"
  - "Harshit Surana"
  - "D. P. Agarwal"
  - "Bhavana Dalvi Mishra"
  - "Abhijeetsingh Meena"
date: "2024"
doi: "N/A"
arxiv: ""
score: 4.0
essence: "본 논문은 대규모 언어모델(LLM)이 데이터셋만으로 가설을 자동으로 탐색하고 검증할 수 있는지 평가하기 위한 최초의 포괄적 벤치마크 **DiscoveryBench**를 제시한다. 264개의 실제 과제와 903개의 합성 과제로 구성되어 있으며, 현재 최고 성능 LLM도 25%의 정확도만 달성하여 자동화된 데이터 기반 발견의 난제를 드러낸다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/Realistic_Discovery_Benchmarks"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Majumder et al._2024_Discoverybench Towards data-driven discovery with large language models.pdf"
---

# Discoverybench: Towards data-driven discovery with large language models

> **저자**: Bodhisattwa Prasad Majumder, Harshit Surana, D. P. Agarwal, Bhavana Dalvi Mishra, Abhijeetsingh Meena, Aryan Prakhar, Tirth Vora, Tushar Khot, Ashish Sabharwal, Peter E. Clark | **날짜**: 2024 | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp)
*각 DiscoveryBench 과제는 목표와 데이터셋으로 구성되며, 통계 분석과 과학적 의미 추론이 필요하고, 다면적 평가를 통해 엄밀하게 평가됨*

본 논문은 대규모 언어모델(LLM)이 데이터셋만으로 가설을 자동으로 탐색하고 검증할 수 있는지 평가하기 위한 최초의 포괄적 벤치마크 **DiscoveryBench**를 제시한다. 264개의 실제 과제와 903개의 합성 과제로 구성되어 있으며, 현재 최고 성능 LLM도 25%의 정확도만 달성하여 자동화된 데이터 기반 발견의 난제를 드러낸다.

## Motivation

- **Known**: 최근 LLM의 코드 생성, 함수 호출, 데이터 분석 능력이 급격히 발전하고 있으며, 일부 연구에서 데이터 기반 가설 탐색의 가능성을 제시함
- **Gap**: 그러나 다양한 도메인과 실제 연구 환경에서 LLM이 얼마나 효과적으로 자동화된 데이터 기반 발견을 수행할 수 있는지 체계적으로 평가할 수 있는 벤치마크가 부재함
- **Why**: 기존 AutoML이나 통계 분석 데이터셋은 파이프라인 설계, 의미론적 추론, 가설 도출 등 포괄적인 발견 과정을 평가하지 못함
- **Approach**: 발행된 과학 논문에서 추출한 실제 발견 과제와 합성 과제를 통해 정형화된 벤치마크를 구축하고, 다면적(faceted) 평가 프레임워크를 제안

## Achievement

![Figure 4](figures/fig4.webp)
*DB-REAL과 DB-SYNTH에서 다양한 에이전트-LLM 조합의 가설 매칭 스코어(HMS)*

1. **포괄적 벤치마크 구축**: 사회학, 공학 등 6개 도메인에서 발행된 20개 이상의 논문으로부터 264개의 실제 발견 과제 추출 및 검증된 워크플로우 제공. 복잡도 제어를 위해 48개 도메인에 걸친 903개의 합성 과제 추가

2. **정형화된 발견 프레임워크**: 가설을 문맥(context), 변수(variables), 관계(relationship)의 3개 차원으로 분해하는 구조화된 형식 제시. 가설 의미 트리(hypothesis semantic tree)를 도입하여 복잡한 계층적 가설 표현 가능

3. **체계적인 평가 방식**: 개방형 답변을 다면적으로 평가할 수 있는 엄밀한 평가 메커니즘 개발. 기존 수치 답변 기반 평가의 한계를 극복하고 부분 정확도 반영

4. **광범위한 성능 분석**: 오픈소스 및 폐쇄형 LLM을 포함한 여러 추론 프레임워크 평가. 최고 성능이 25%에 불과함을 입증하여 미해결 과제 명시

## How

![Figure 2](figures/fig2.webp)
*가설의 계층적 구조를 표현하는 의미 트리: 루트는 목표 변수, 리프는 독립 변수, 내부 노드는 중간 가설의 목표 변수*

- **과제 정의**: 하나 이상의 데이터셋 D와 자연언어 발견 목표 G가 주어졌을 때, G를 해결하는 가설 h = ψ(c, v, r)을 최고의 특이성(specificity)으로 도출
  
- **DB-REAL 구성**: 
  - 발행된 논문의 데이터 분석 부분 수동 추출
  - 각 과제는 원본 데이터셋, 메타데이터, 목표, 기준 가설, 검증된 워크플로우 포함
  - 다양한 난이도 시뮬레이션(파생 변수의 관찰성 조정)

- **DB-SYNTH 구성**:
  - LLM을 활용한 합성 과제 생성으로 체계적인 변동성 확보
  - 과제 난이도를 제어 가능한 변수로 조정
  - 특정 패턴의 영향을 고립시켜 분석 가능

- **Discovery Agent 평가**:
  - 다양한 LLM 기반 추론 프레임워크 테스트
  - 코드 생성 및 실행 능력 활용
  - 도메인별, 목표 유형별 성과 분석

- **다면적 평가 메커니즘**:
  - 문맥, 변수, 관계의 각 차원별로 개별 점수 계산
  - 부분 정확도 반영(예: 변수는 일부만 정확)
  - 최종 종합 스코어 도출

## Originality

- 기존 AutoML/통계 분석 벤치마크와 달리 **완전한 발견 파이프라인**을 포괄: 가설 도출, 의미론적 추론, 파이프라인 설계 등 포함

- **정형화된 가설 표현**: 발행된 과학 논문에서 영감을 받은 실제 가설의 구조를 수학적으로 형식화한 최초의 시도

- **가설 의미 트리**: 복잡한 계층적 가설 관계를 그래프 구조로 표현하는 새로운 개념 도입으로 다층적 발견 과제 처리 가능

- **개방형 답변 평가**: 엄밀한 수치 기준 없이 자유로운 형식의 과학적 발견을 다면적으로 평가하는 프레임워크 최초 제시

- **진정한 다중도메인 설계**: 사회학부터 공학까지 6개 실제 도메인과 48개 합성 도메인에서 체계적으로 과제 수집

## Limitation & Further Study

- **평가 메커니즘의 제약**: 다면적 평가가 여전히 인간 판단에 부분 의존하며, 자동화된 평가의 일관성 검증 필요

- **LLM 성능의 저조함**: 최고 25% 정확도는 현재 LLM의 과학적 발견 자동화에 근본적인 한계 존재를 의미하며, 어느 능력이 부족한지 더 깊은 분석 필요

- **데이터셋 규모의 한계**: 264개 실제 과제는 다양한 도메인과 발견 유형을 완전히 대표하기에 부족할 수 있음

- **합성 데이터의 현실성**: 합성 과제의 생성 방식이 실제 과학 연구의 복잡성을 완전히 반영하지 못할 가능성

- **후속 연구**: 
  - 구체적 실패 모드 분석: 의미론적 추론 vs. 통계 분석 능력의 상대적 약점 규명
  - 다단계 추론 전략의 개선: 에이전트의 워크플로우 설계 능력 강화
  - 도메인 특화 모델 개발: 특정 과학 분야에 최적화된 발견 시스템 구축
  - 인터랙티브 발견 패러다임: 사용자 피드백을 활용한 반복적 개선 메커니즘

## Evaluation

- **Novelty**: 4.5/5
  - 데이터 기반 발견의 완전한 파이프라인을 다루는 최초의 포괄적 벤치마크
  - 가설 의미 트리 등 새로운 형식화 프레임워크 제시
  - 다면적 평가 메커니즘의 창의성
  - 다만, 기초 개념은 기존 연구에서 영감

- **Technical Soundness**: 4/5
  - 정형화된 가설 표현과 평가 프레임워크의 엄밀성
  - 광범위한 평가 대상(여러 LLM과 추론 방식)
  - 합성 데이터 생성 프로세스의 타당성
  - 다만, 평가 일관성 검증(inter-annotator agreement) 관련 상세 기술 부족

- **Significance**: 4/5
  - 자동화된 과학적 발견이라는 중요한 미해결 문제에 대한 첫 체계적 평가
  - 향후 LLM 기반 발견 시스템 개발의 기준점 제공
  - 하지만 현실 과학 연구 적용을 위한 추가 개선 필요성 명확

- **Clarity**: 4/5
  - 명확한 과제 정의 및 형식화
  - 실제 사례를 통한 직관적 설명
  - 다만, 가설 의미 트리의 수학적 정의가 다소 복잡하게 표현됨

- **Overall**: 4/5

**총평**: DiscoveryBench는 LLM 기반 자동화된 과학적 발견의 능력을 체계적으로 평가하는 중요한 첫 번째 벤치마크로서, 새로운 형식화 프레임워크와 다면적 평가 메커니즘을 제시한다. 264개의 실제 과제와 903개의 합성 과제로 구성된 포괄적인 자원을 제공하며, 현재 LLM의 25% 저조한 성능은 이 분야의 미해결 과제를 명확히 드러낸다. 다만 평가 일관성 검증이 보완되고, 실패 모드에 대한 더 깊은 분석이 이루어진다면 이 벤치마크는 향후 과학적 발견 자동화 연구의 중요한 추진력이 될 것으로 기대된다.

## Related Papers

- 🔄 다른 접근: [[papers/704_SciAgentGym_Benchmarking_Multi-Step_Scientific_Tool-use_in_L/review]] — SciAgentGym과 DiscoveryBench 모두 과학적 도구 사용을 평가하지만 다단계 vs 데이터 중심 발견에 초점을 둔다.
- ⚖️ 반론/비판: [[papers/187_Can_LLMs_Generate_Novel_Research_Ideas_A_Large-Scale_Human_S/review]] — 인간 평가자들이 LLM이 생성한 새로운 연구 아이디어를 선호한다는 발견은 DiscoveryBench의 25% 성공률과 대조적이다.
- 🔗 후속 연구: [[papers/146_Autosdt_Scaling_data-driven_discovery_tasks_toward_open_co-s/review]] — AutoSDT의 데이터 주도형 발견 방법론이 DiscoveryBench의 과학적 발견 평가에 적용될 수 있음
