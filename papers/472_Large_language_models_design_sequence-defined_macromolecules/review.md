---
title: "472_Large_language_models_design_sequence-defined_macromolecules"
authors:
  - "Wesley F. Reinhart"
  - "Antonia Statt"
date: "2024"
doi: "10.1038/s41524-024-01449-6"
arxiv: ""
score: 4.0
essence: "사전학습된 대규모언어모델(LLM)인 Claude 3.5 Sonnet을 진화 최적화(evolutionary optimization) 알고리즘으로 활용하여 거대 분자의 자기조립 구조를 설계할 수 있음을 입증한 연구로, 전통적인 능동학습(active learning)과 진화 알고리즘보다 우수한 성능을 보였다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/Protein-Drug_Design_Models"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Reinhart and Statt_2024_Large language models design sequence-defined macromolecules via evolutionary optimization.pdf"
---

# Large language models design sequence-defined macromolecules via evolutionary optimization

> **저자**: Wesley F. Reinhart, Antonia Statt | **날짜**: 2024 | **DOI**: [10.1038/s41524-024-01449-6](https://doi.org/10.1038/s41524-024-01449-6)

---

## Essence

사전학습된 대규모언어모델(LLM)인 Claude 3.5 Sonnet을 진화 최적화(evolutionary optimization) 알고리즘으로 활용하여 거대 분자의 자기조립 구조를 설계할 수 있음을 입증한 연구로, 전통적인 능동학습(active learning)과 진화 알고리즘보다 우수한 성능을 보였다.

## Motivation

- **Known**: 거대 분자의 자기조립은 나노-패터닝, 단백질 폴딩 등 기술 및 생물학적으로 중요하며, 서열이 정의된 거대 분자(sequence-defined macromolecules)는 뛰어난 조절성으로 인해 유망한 신소재 클래스이다. 그러나 가능한 서열 수가 천문학적이라 전수조사는 불가능하다.

- **Gap**: 기존 연구들은 RNN을 활용한 예측 모델 개발에 ~1000개의 학습 샘플이 필요했으며, 계산 과학에서는 상당히 큰 규모였다. 또한 거대 분자 설계에 최적화된 기계학습 모델 개발이 필요했다.

- **Why**: 최근 LLM의 진화 최적화 능력(emergent capability)에 대한 연구가 증가하고 있으며, 사전학습된 LLM을 도메인 특화 데이터 미세조정 없이 직접 활용할 수 있다면 하이퍼파라미터 튜닝 부담을 줄이면서도 자기반영(self-reflection) 등 새로운 능력을 활용할 수 있다.

- **Approach**: 비감독학습으로부터 얻은 2D 순서 매개변수(order parameter Z) 표현과 이전의 RNN 모델을 활용하여, LLM이 반복적으로 단량체 서열을 제안하고 점수를 받는 루프 구조에서 목표 형태에 가장 가까운 서열을 찾도록 설계했다.

## Achievement

![Figure 1](figures/fig1.webp) 
*Fig. 1: LLM 기반 진화 최적화의 개념도. (a) 단량체 서열→MD 시뮬레이션→2D 순서 매개변수 Z 추출 파이프라인, (d) LLM 에이전트가 서열을 제안하면 RNN 모델로 평가하는 반복 루프*

![Figure 2](figures/fig2.webp) 
*Fig. 2: 최적화 알고리즘 성능 비교. (b) 최고 3개 후보의 평균 거리, (c) 역치값 이하의 서열 개수, (d) 6가지 목표 형태에 대한 종합 성과 (씨앗 없음/있음)*

1. **LLM의 우수한 수렴성**: LLM 기반 최적화기는 활동적 학습과 진화 알고리즘보다 빠르게 목표 영역에 수렴하며, 탐색(exploration)과 착취(exploitation) 사이의 균형을 효과적으로 유지했다. 초기 5회 반복에서 올바른 영역을 찾고, 마지막 5회에서 다양한 우수 해를 발견했다.

2. **일관된 우수 성능**: 12개 테스트 케이스(6가지 목표 형태 × 씨앗 있음/없음) 중 11개에서 LLM 기반 방법이 최고 평균 성능을 기록했다. 씨앗 지원 시 중앙값 성능이 특히 향상되었으며, 모든 형태에서 중앙값 k=0인 경우가 사라졌다.

3. **문맥 무시 상황에서의 자동 추론**: 문맥 정보를 제공하지 않은 "oracle" 프롬프트에서도 LLM은 단백질 폴딩 문제로 자동 추론하면서 효과적으로 수행했다. 이는 LLM이 암묵적 도메인 지식을 활용하고 있음을 시사한다.

## How

![Figure 1 상세](figures/fig1.webp) 
*Fig. 1e-g: 대표적 LLM 최적화 과정. (e) 반복별 거리 변화, (f-g) 잠재 공간(latent space Z)에서의 수열 위치 변화 추이*

- **문제 설정**: 비감독학습으로부터 추출한 2D 순서 매개변수 Z 공간에서, 주어진 목표 형태 Z_t까지의 거리를 최소화하는 단량체 서열 x를 찾는 역 설계(inverse design) 문제

- **LLM 기반 루프**: 
  1. LLM이 배치 단위로 단량체 서열 후보들을 제안
  2. 사전학습된 RNN 모델 f(x)→Z̃를 통해 각 후보의 거리 d 계산
  3. 점수와 함께 피드백을 LLM에 반환
  4. LLM이 이 정보를 바탕으로 다음 배치 생성

- **비교 알고리즘**:
  - 활동적 학습: Random Forest 앙상블 사용
  - 진화 알고리즘: 2점 교배(two-point crossover) 적용
  - 기저선: 무작위 서열 선택

- **평가 지표**:
  - 거리 d* = 1.34 (확률적 자기조립으로 인한 RMSD의 약 2배)를 역치로 설정
  - 평가 지표: 최고 3개 후보의 평균 거리, 역치 이하 서열 개수(k)

- **프롬프트 변형**: "oracle" (문맥 무제공)과 "scientific" (MD 시뮬레이션 상세 설명 제공) 두 가지 프롬프트 비교

## Originality

- **LLM을 진화 최적화기로 활용**: 최근 발견된 LLM의 새로운 emergent behavior를 재료 설계 문제에 실제 적용한 최초 사례

- **미세조정 불필요**: 상용 사전학습 모델(Claude 3.5 Sonnet)을 도메인 특화 데이터로 미세조정하지 않고 직접 사용하여 재현성과 적용성을 향상

- **자동 도메인 추론**: 문맥 없이도 LLM이 문제를 단백질 폴딩으로 자동 추론하며 우수한 성능을 발휘하는 현상 발견—LLM의 내부 지식 활용을 시사

- **다중 형태에 대한 체계적 벤치마킹**: 6가지 목표 형태(액적, 문자열, 막, 소포, 웜라이크 미셀, 구형 미셀)에서 반복 실험으로 통계적 신뢰성 확보

## Limitation & Further Study

- **RNN 근사값 기반 평가**: 실제 MD 시뮬레이션(f(x)→Z)이 아닌 RNN 근사값(f(x)→Z̃)을 기반으로 최적화했으므로, 발견된 서열이 실제 시뮬레이션에서도 목표 형태를 형성하는지 검증 필요

- **높은 회차별 분산**: 대상 형태에 따라 복제(replica) 간 성과 편차가 크며, 일부 경우 모든 알고리즘이 중앙값 k=0을 기록—문제의 어려움을 시사하고 개선 방법 필요

- **LLM의 진화 최적화 메커니즘 미해명**: LLM이 실제로 어떤 방식으로 진화 전략을 수행하는지에 대한 해석 불충분

- **확장성 미검증**: 더 긴 서열, 더 복잡한 형태 공간, 다중 목적 최적화 문제로의 확장 가능성 불명확

- **후속 연구 방향**:
  - 최적화된 서열에 대한 전체 MD 시뮬레이션 검증
  - LLM의 프롬프트 엔지니어링 최적화를 통한 성능 향상 탐색
  - 다른 LLM 모델(GPT-4, Gemini 등)과의 비교
  - 생물학적 타당성이 있는 거대 분자 설계로 응용

## Evaluation

- **Novelty**: 4/5
  - LLM을 진화 최적화기로 재료 설계에 적용한 점은 신선하나, LLM의 진화 최적화 능력 자체는 선행 연구에서 보고된 emergent behavior

- **Technical Soundness**: 4/5
  - 실험 설계 및 비교 알고리즘 선정이 타당하고, 통계적 신뢰성(5회 반복)을 확보했으나, RNN 근사값 기반 평가로 인한 한계

- **Significance**: 4/5
  - 거대 분자 설계와 같은 조합론적 최적화 문제에서 LLM의 실용성을 입증했으나, 실제 MD 검증 부재로 인한 영향 제한

- **Clarity**: 4.5/5
  - 문제 설정, 방법론, 결과 프레젠테이션이 명확하고 Figure가 잘 구성되었으나, LLM의 내부 메커니즘에 대한 설명 부족

- **Overall**: 4/5

**총평**: 본 논문은 대규모언어모델의 emergent behavior를 재료 과학의 실제 문제에 창의적으로 적용하여 기존 최적화 방법을 능가하는 성과를 보였다. 다만 RNN 근사값 기반 평가와 실제 MD 검증 부재, 그리고 LLM의 작동 원리에 대한 이론적 이해 부족이 한계로 지적되며, 향후 이러한 점들이 보완되면 더욱 강력한 기여가 될 수 있을 것으로 판단된다.

## Related Papers

- 🔄 다른 접근: [[papers/459_Language_Models_for_Controllable_DNA_Sequence_Design/review]] — 언어 모델을 활용한 생체분자 설계라는 공통 주제이지만 거대분자 자기조립과 DNA 서열 설계로 응용 영역이 다르다.
- 🏛 기반 연구: [[papers/469_Large_Language_Models_as_Evolutionary_Optimizers/review]] — 진화 최적화 알고리즘으로서의 LLM 활용 방법론이 거대분자 설계에 적용된 사례이다.
- 🔗 후속 연구: [[papers/305_Efficient_Evolutionary_Search_Over_Chemical_Space_with_Large/review]] — 화학 공간에서의 효율적인 진화 탐색 기법을 거대분자 설계에 확장 적용할 수 있다.
- 🔄 다른 접근: [[papers/459_Language_Models_for_Controllable_DNA_Sequence_Design/review]] — 거대분자 설계를 위한 LLM 활용이라는 공통점이 있지만, DNA 서열 생성과 자기조립 구조 설계라는 다른 타겟을 다룬다.
