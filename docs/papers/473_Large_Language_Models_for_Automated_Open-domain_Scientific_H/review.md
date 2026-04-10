---
title: "473_Large_Language_Models_for_Automated_Open-domain_Scientific_H"
authors:
  - "Zonglin Yang"
  - "Xinya Du"
  - "Junxian Li"
  - "Jie Zheng"
  - "Soujanya Poria"
date: "2023.09"
doi: "미제공"
arxiv: ""
score: 4.0
essence: "본 논문은 대규모 언어모델(LLM)을 활용하여 원본 웹 코퍼스로부터 자동으로 새로운 사회과학 학술 가설을 발견하는 첫 번째 시스템을 제안한다. 기존의 제한된 폐쇄 도메인 환경과 상식 수준의 가설을 넘어, 개방 도메인 관찰로부터 학술 문헌에 존재하지 않는 혁신적이고 타당한 과학 가설 생성을 달성했다."
tags:
  - "cat/Academic_Peer_Review_Automation"
  - "sub/AI_Peer_Review"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Yang et al._2023_Large Language Models for Automated Open-domain Scientific Hypotheses Discovery.pdf"
---

# Large Language Models for Automated Open-domain Scientific Hypotheses Discovery

> **저자**: Zonglin Yang, Xinya Du, Junxian Li, Jie Zheng, Soujanya Poria, Erik Cambria | **날짜**: 2023-09-06 | **DOI**: [미제공](https://doi.org/)

---

## Essence

본 논문은 대규모 언어모델(LLM)을 활용하여 원본 웹 코퍼스로부터 자동으로 새로운 사회과학 학술 가설을 발견하는 첫 번째 시스템을 제안한다. 기존의 제한된 폐쇄 도메인 환경과 상식 수준의 가설을 넘어, 개방 도메인 관찰로부터 학술 문헌에 존재하지 않는 혁신적이고 타당한 과학 가설 생성을 달성했다.

## Motivation

- **Known**: 과거 가설적 귀납법(hypothetical induction) 연구는 (1) 수작업으로 선별된 폐쇄 도메인 관찰 데이터, (2) 상식 수준의 기본 가설에 국한되어 있었음

- **Gap**: 실제 학술 환경에서 필요한 개방 도메인 원본 데이터로부터 새로운 과학 가설을 자동 발견하는 시스템의 부재

- **Why**: 과학적 발전은 기존 관찰로부터 새로운 가설을 제안하는 능력에 의존하며, 이를 자동화하면 연구 생산성 향상 가능

- **Approach**: 다중 모듈 프레임워크(MOOSE)와 세 가지 피드백 메커니즘을 통해 LLM의 가설 생성 능력 증강

## Achievement

1. **첫 번째 개방 도메인 데이터셋 구축**: 사회과학 학술 가설 발견을 위한 최초의 벤치마크 데이터셋(TOMATO) 제시, 원본 웹 코퍼스를 관찰로 사용

2. **신규성과 타당성 달성**: GPT-4 기반 및 전문가 평가 기준으로 LLM이 문헌에 존재하지 않는(novel) 동시에 현실을 반영하는(valid) 과학 가설 생성 능력 실증적 증명

3. **다중 피드백 메커니즘 개발**: 세 가지 피드백 메커니즘을 통해 성능 향상, 모듈식 구조로 확장성 제공

## How

- **관찰 추출(Observation Extraction)**: 개방 도메인 웹 코퍼스에서 관련 관찰 문장 추출
  
- **가설 생성 모듈(Hypothesis Generation Module)**: 프롬프트 엔지니어링과 in-context learning을 활용한 LLM 기반 가설 생성

- **피드백 메커니즘**:
  - 논리적 피드백(Logical Feedback): 가설의 논리적 일관성 검증
  - 원본 기반 피드백(Source-grounded Feedback): 제시된 관찰로부터의 근거 확인
  - 학술 기반 피드백(Literature-grounded Feedback): 기존 학술 문헌과의 관계성 평가

- **반복적 정제(Iterative Refinement)**: 피드백을 기반으로 가설 재생성 및 개선

## Originality

- **패러다임 전환**: 폐쇄 도메인에서 개방 도메인으로, 상식 수준에서 학술 수준 가설로의 진화

- **신규성 정의 및 측정**: "문헌에 존재하지 않음(novel)"을 명확히 정의하고 이를 자동으로 검증하는 방법론 제시

- **다중 피드백 메커니즘**: 단순 생성이 아닌 검증-정제 루프를 통한 가설 품질 관리

- **벤치마크 데이터셋**: 사회과학 분야 첫 번째 구조화된 가설 발견 데이터셋 제공

## Limitation & Further Study

- **도메인 제한**: 사회과학 분야에 집중, 자연과학 및 기술 분야로의 확장 필요

- **평가 메트릭 개선**: GPT-4 기반 평가의 신뢰도 향상, 더 포괄적인 전문가 평가 체계 구축

- **확장성**: 더 큰 규모의 웹 코퍼스 처리 및 실시간 가설 발견 시스템으로의 발전

- **투명성**: 가설의 생성 과정 및 근거에 대한 해석 가능성(interpretability) 강화

- **학술 적용**: 실제 학술 커뮤니티에서의 활용 가능성 검증 및 연구 프로세스 통합

## Evaluation

- **Novelty**: 4.5/5
  - 개방 도메인 가설 발견이라는 새로운 문제 설정이 혁신적이나, 기술적 혁신은 기존 LLM 활용의 연장선상

- **Technical Soundness**: 4/5
  - 다중 피드백 메커니즘의 설계가 합리적이나, 각 피드백의 독립적 효과 분석 부재

- **Significance**: 4/5
  - 학술 연구 프로세스 자동화의 중요한 첫 걸음이나, 실제 학술 커뮤니티 도입까지의 거리 존재

- **Clarity**: 3.5/5
  - 전반적 구조는 명확하나, MOOSE 프레임워크의 상세 구현 및 피드백 메커니즘 간의 상호작용 설명 부족

- **Overall**: 4/5

**총평**: 본 논문은 LLM을 활용한 자동 학술 가설 발견이라는 도전적이고 실질적인 문제를 제시하며, 개방 도메인 데이터로부터 신규이면서도 타당한 과학 가설을 생성할 수 있음을 최초로 실증했다. 다만 기술적 혁신성은 상대적으로 제한적이며, 실제 학술 적용을 위한 추가 검증과 개선이 필요하다.

## Related Papers

- 🔄 다른 접근: [[papers/419_Hypothesis_Generation_with_Large_Language_Models/review]] — LLM을 활용한 가설 생성의 다른 접근법으로 개방 도메인과 일반적 방법론을 비교할 수 있다.
- 🔗 후속 연구: [[papers/666_Research_hypothesis_generation_over_scientific_knowledge_gra/review]] — 과학 지식 그래프 기반 연구 가설 생성으로 웹 코퍼스에서 발견한 가설을 체계적으로 검증할 수 있다.
- 🏛 기반 연구: [[papers/330_Exploiting_LLMs_for_Automatic_Hypothesis_Assessment_via_a_Lo/review]] — 프로그램 기반 추론을 통한 자동 가설 평가로 혁신적 가설의 타당성 검증 방법론을 제공한다.
