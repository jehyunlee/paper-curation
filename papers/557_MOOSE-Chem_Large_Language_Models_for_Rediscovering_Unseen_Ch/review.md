---
title: "557_MOOSE-Chem_Large_Language_Models_for_Rediscovering_Unseen_Ch"
authors:
  - "Zonglin Yang"
  - "Wanhao Liu"
  - "Ben Gao"
  - "Tong Xie"
  - "Yuqiang Li"
date: "2024"
doi: "10.48550/arXiv.2410.07076"
arxiv: ""
score: 4.25
essence: "대규모 언어모델(LLM)이 화학 분야의 연구 배경만으로 미발견 과학 가설을 자동으로 재발견할 수 있음을 최초로 증명한 연구이다. 이를 통해 LLM이 Nature/Science 수준의 화학 논문 가설들의 핵심 혁신을 포착하는 능력을 보였다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/AI_Drug_Discovery"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Yang et al._2024_MOOSE-Chem Large Language Models for Rediscovering Unseen Chemistry Scientific Hypotheses.pdf"
---

# MOOSE-Chem: Large Language Models for Rediscovering Unseen Chemistry Scientific Hypotheses

> **저자**: Zonglin Yang, Wanhao Liu, Ben Gao, Tong Xie, Yuqiang Li | **날짜**: 2024 | **DOI**: [10.48550/arXiv.2410.07076](https://doi.org/10.48550/arXiv.2410.07076)

---

## Essence

대규모 언어모델(LLM)이 화학 분야의 연구 배경만으로 미발견 과학 가설을 자동으로 재발견할 수 있음을 최초로 증명한 연구이다. 이를 통해 LLM이 Nature/Science 수준의 화학 논문 가설들의 핵심 혁신을 포착하는 능력을 보였다.

## Motivation

- **Known**: 최근 LLM이 사회과학 영역에서 새로운 가설 생성이 가능함이 보여졌으나(Yang et al. 2024b), 자연과학 특히 화학 영역에서의 과학 발견 능력은 여전히 불명확함. 기존 촉매 발견 연구(Sprueill et al. 2023; 2024)는 데이터 오염 문제 가능성이 있음.

- **Gap**: 화학 분야는 사회과학과 다르게 복잡한 시스템 구성이 필요하며, LLM이 이런 다중 영감(multiple inspirations)을 활용해 가설을 생성할 수 있는지 검증되지 않았음. 또한 가설 순위 매기기 작업은 선행 연구에서 거의 다루어지지 않았음.

- **Why**: 화학 가설 생성은 인지과학의 창의성 이론(두 개의 무관해 보이는 지식을 결합하는 과정)에 기반하며, 이를 LLM이 수행할 수 있다면 과학 발견을 가속화할 수 있음.

- **Approach**: 공식적인 수학적 분해를 통해 P(hypothesis|research background)를 세 가지 실행 가능한 소작업으로 분해: (1) 영감 논문 검색, (2) 영감 기반 가설 작성, (3) 가설 순위 매기기. 이를 구현한 MOOSE-Chem 프레임워크 개발.

## Achievement

1. **벤치마크 구축**: 2024년 이후 공개된 Nature/Science 및 상위급 저널의 51개 화학 논문으로 구성된 TOMATO-Chem 벤치마크를 화학박사 학생들이 수작업으로 주석처리(background, inspirations, hypothesis로 분해). 이는 수학 올림피아드 경쟁의 난이도 수준 모방.

2. **LLM의 과학 발견 능력 검증**: 2023년 12월 이전의 지식만 학습한 LLM을 사용하여 데이터 오염 없이 최대 51개 논문의 핵심 혁신을 재발견. 특히 영감 검색 작업에서 LLM의 뛰어난 성능 확인(분포 외 태스크임에도 불구하고).

3. **새로운 가정 제시**: LLM이 인간이 아직 인식하지 못한 잠재적 과학 지식 연관성을 이미 인코딩하고 있을 가능성 제안.

## How

- **세 단계 파이프라인**: 
  - 단계 1 - 영감 검색: LLM이 화학 문헌을 검색하여 연구 질문과 관련된 영감 논문 식별
  - 단계 2 - 가설 작성: 진화 알고리즘(evolutionary algorithm) 기반 접근으로 배경과 다중 영감을 결합하여 다양한 가설 생성
  - 단계 3 - 순위 매기기: 효율적인 순위 방법으로 고품질 가설을 상위에 배치

- **사회과학 방법과의 차이**:
  - 다중 영감(one to three inspirations) 수용으로 복잡한 화학 시스템 구성 가능
  - 진화 알고리즘을 통한 다양성 강화
  - 다단계 영감 검색 전략
  - 효율적인 순위 매기기 방법 도입

- **데이터 오염 방지**: 2023년 12월 기준 LLM 사용 + 2024년 이후 공개 논문 = 시간적 갭 확보

## Originality

- **최초 성과**: 화학 영역에서 LLM 기반 과학 가설 재발견의 가능성을 최초로 체계적으로 검증

- **수학적 기초**: P(hypothesis|research background)를 형식적으로 분해한 첫 번째 수학적 유도로 추상적 문제를 실행 가능한 부분과제로 변환

- **평가 방법론**: 과학 발견의 가설 순위 매기기 문제를 최초로 공식화하고 평가 기준 제시

- **고난도 벤치마크**: Nature/Science 수준의 2024년 최신 논문 기반 벤치마크는 기존 연구(사회과학, 촉매 발견)보다 훨씬 도전적

- **다중 영감 처리**: 사회과학의 단일 영감 가정을 화학의 다중 영감으로 확장한 혁신적 모델

## Limitation & Further Study

- **벤치마크 규모**: 51개 논문은 상대적으로 작은 규모로, 일반화 가능성 검증 필요. 특히 51개 중 얼마나 많은 가설을 실제로 재발견했는지 정량적 성공률 미제시.

- **평가 방법의 한계**: LLM 생성 가설의 "유사도" 평가 기준이 명확하지 않음. 정성적 평가에 의존할 수 있으며, 실제 과학적 검증(실험을 통한)이 누락됨.

- **"이미 인코딩된 지식" 가정의 검증 부족**: LLM이 실제로 잠재적 과학 지식을 보유하는지 vs. 단순 통계적 패턴 매칭인지 구분이 필요.

- **화학 도메인 편향**: 중합체 화학(41%) 및 유기화학(43%)에 집중되어 있어 다른 화학 분야 일반화 가능성 의문.

- **후속 연구 방향**:
  - 더 큰 규모의 벤치마크(수백~수천 논문) 구축
  - 실제 화학 실험으로 재발견 가설 검증
  - 다른 자연과학 영역(생물학, 물리학 등)으로 확장
  - LLM의 지식 출처 분석(오염 vs. 진정한 과학 지식 연관)


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4/5
- Significance: 4.5/5
- Clarity: 4/5
- Overall: 4.25/5

**총평**: MOOSE-Chem은 LLM의 화학 과학 발견 능력을 최초로 체계적으로 입증한 중요한 연구로, 수학적 분해 및 진화 알고리즘 기반 다중 영감 처리라는 독창적 접근이 돋보인다. 다만 상대적으로 작은 벤치마크 규모와 평가 기준의 엄밀성, 그리고 LLM이 실제로 새로운 과학 지식을 생성하는지 또는 기존 지식을 재조합하는지에 대한 심층 분석이 필요하다.

## Related Papers

- 🔄 다른 접근: [[papers/418_Hypothesis_Generation_for_Materials_Discovery_and_Design_Usi/review]] — 화학 vs 재료 과학에서 LLM 기반 과학적 발견의 다른 도메인 적용을 비교할 수 있다
- 🔗 후속 연구: [[papers/115_Augmenting_large_language_models_with_chemistry_tools/review]] — LLM에 화학 도구를 통합한 방법론을 미발견 화학 가설 재발견에 확장 적용할 수 있다
- 🔗 후속 연구: [[papers/558_Moose-chem3_Toward_experiment-guided_hypothesis_ranking_via/review]] — 실험 가이드 기반 가설 순위화로 화학 가설 재발견 방법론을 확장할 수 있다
- 🏛 기반 연구: [[papers/878_What_ChatGPT_and_generative_AI_mean_for_science/review]] — 생성형 AI가 과학 연구에 미치는 전반적 영향에 대한 이론적 기반을 제공한다
- 🔗 후속 연구: [[papers/305_Efficient_Evolutionary_Search_Over_Chemical_Space_with_Large/review]] — LLM 기반 화학 공간 진화 탐색이 미발견 화학 지식 재발견을 위한 더 포괄적인 대형언어모델 시스템으로 확장되었다
- 🏛 기반 연구: [[papers/115_Augmenting_large_language_models_with_chemistry_tools/review]] — LLM에 화학 도구를 통합하는 방법론이 미발견 화학 가설 재발견의 기반을 제공한다
