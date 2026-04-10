---
title: "1094_Towards_a_Medical_AI_Scientist"
authors:
  - "Hongtao Wu"
  - "Boyun Zheng"
  - "Dingjie Song"
  - "Yu Jiang"
  - "Jianfeng Gao"
date: "2026.03"
doi: "10.48550/arXiv.2603.28589"
arxiv: ""
score: 4.0
essence: "임상 의학 연구에 특화된 첫 번째 자율 AI 과학자 시스템으로, 문헌 기반 증거 추론, 실험 실행, 논문 작성을 자동화하며 MICCAI 수준의 품질을 달성한다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/Clinical_Multi-Agent_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Wu et al._2026_Towards a Medical AI Scientist.pdf"
---

# Towards a Medical AI Scientist

> **저자**: Hongtao Wu, Boyun Zheng, Dingjie Song, Yu Jiang, Jianfeng Gao, Lei Xing, Lichao Sun, Yixuan Yuan | **날짜**: 2026-03-30 | **DOI**: [10.48550/arXiv.2603.28589](https://doi.org/10.48550/arXiv.2603.28589)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1 | a, System workflow: fully-automated multi-agents system for end-to-end scientific discovery*

임상 의학 연구에 특화된 첫 번째 자율 AI 과학자 시스템으로, 문헌 기반 증거 추론, 실험 실행, 논문 작성을 자동화하며 MICCAI 수준의 품질을 달성한다.

## Motivation

- **Known**: 대규모 언어 모델(LLM)과 AI 에이전트 기술이 과학적 가설 생성, 실험 수행, 논문 작성을 자동화할 수 있으나, 기존 AI Scientists는 도메인 무관적이고 의료 데이터의 복잡성과 윤리적 제약을 고려하지 못한다.
- **Gap**: 임상 의료 분야의 특수성(의료 증거 기반 추론, 이질적 데이터 모달리티, 윤리 정책 준수)을 고려한 자율 연구 시스템이 부재하며, 이를 평가할 표준화된 벤치마크도 없다.
- **Why**: 의료 데이터와 문헌의 폭발적 증가로 인한 인간 주도 연구의 병목 현상을 해결하고, AI를 통해 의료 AI 연구의 효율성을 획기적으로 향상시킬 수 있기 때문이다.
- **Approach**: 임상의-엔지니어 협력 추론 메커니즘을 통해 문헌 기반 증거로부터 임상적 가설을 생성하고, 세 가지 연구 모드(논문 재현, 문헌 기반 혁신, 과제 기반 탐색)로 자율성 수준을 구분하며, 의료 쓰기 규범과 윤리 정책을 기반으로 논문을 자동 작성한다.

## Achievement


- **아이디어 생성 우수성**: 171개 사례, 19개 임상 과제, 6개 데이터 모달리티에서 상용 LLM을 능숙성(novelty), 성숙도(maturity), 윤리성(ethicality), 일반화 가능성(generalizability), 효용성(utility), 해석가능성(interpretability) 측면에서 일관되게 상회
- **실험 실행 신뢰성**: 제안된 방법과 구현 간 강한 일치도 달성 및 실행 가능한 실험의 높은 성공률 입증
- **논문 품질**: 이중맹검 평가에서 평균 4.60±0.56점으로 MICCAI 수준 경합, ISBI와 BIBM 논문을 일관되게 상회
- **학술적 검증**: 생성된 논문 1건이 ICAIS 2025에서 피어 리뷰를 거쳐 채택됨

## How


- **Idea Proposer**: 구조화된 문헌 검색과 분석으로 임상 선행 지식 도출 및 임상의-엔지니어 공동 추론을 통해 검증 가능한 증거 기반 가설 생성
- **Experimental Executor**: 일반 목적 실행 도구와 의료 전문 도구박스를 통합하여 이질적이고 복잡한 임상 데이터 형식 처리 및 자체 수정 가능한 모델 개발 파이프라인 구성
- **Manuscript Composer**: 계층적 구조화된 의료 쓰기 규범과 윤리 검토 메커니즘을 적용하여 증거 기반의 일관성 있는 논문 초안 자동 생성
- **Med-AI Bench**: 6개 의료 데이터 모달리티(의료 영상, 영상, EHR, 생리신호, 텍스트, 멀티모달)에서 19개 대표 과제별로 난이도 3단계(쉬움, 중간, 어려움)와 입력 모드 3가지로 171개 평가 케이스 구성

## Originality

- 의료 AI 연구에 특화된 첫 번째 자율 과학자 프레임워크로, 기존 도메인 무관적 AI Scientists를 의료 분야의 특수성에 적응시킨 새로운 접근법
- 임상의-엔지니어 협력 추론 메커니즘으로 생성된 아이디어의 추적성(traceability)과 의료 증거 기반 타당성을 획기적으로 개선
- 의료 데이터 모달리티의 이질성, 윤리 정책, 의료 쓰기 규범을 명시적으로 통합한 end-to-end 자동화 연구 파이프라인 구축
- 의료 AI 자율 연구 시스템 평가를 위한 첫 표준화된 벤치마크(Med-AI Bench) 개발

## Limitation & Further Study

- **평가 범위 제한**: 19개 의료 AI 과제로 제한되어 있으며, 임상 번역(clinical translation)으로의 실제 영향은 검증되지 않음
- **생성된 논문 품질**: MICCAI 수준에 접근하나 여전히 모상(coverage) 측면에서 인간 작성 논문보다 열등하며, 복잡한 통계 분석이나 예상치 못한 발견(serendipitous discovery)에 취약할 가능성
- **윤리 및 안전성**: 의료 연구의 윤리적 게이트키핑 메커니즘이 적용되나, 환자 데이터 프라이버시와 신뢰성 검증에 대한 상세한 논의 부족
- **후속 연구**: (1) 더 광범위한 임상 도메인과 희귀 질환으로 확대, (2) 임상의와의 장기 협력 연구를 통한 실제 임상 번역 평가, (3) 생성된 아이디어의 신약 개발이나 임상 시험 단계 적용 검증, (4) 다국가 다문화 의료 컨텍스트에서의 일반화 가능성 평가

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 임상 의료 분야의 특수성을 처음으로 체계적으로 반영한 자율 AI 과학자 시스템으로, 의료 증거 기반 추론과 윤리 정책 통합을 통해 MICCAI 수준의 논문 생성을 달성하며 의료 AI 연구 자동화의 새로운 가능성을 제시한다.

## Related Papers

- 🔗 후속 연구: [[papers/262_Deepreview_Improving_llm-based_paper_review_with_human-like/review]] — 의료 AI 과학자는 DeepReview의 인간 유사 논문 리뷰 기법을 확장하여 임상 연구 전체 과정의 자동화까지 포괄하는 의료 특화 AI 연구자를 구현합니다.
- 🔄 다른 접근: [[papers/795_The_AI_Scientist_Towards_Fully_Automated_Open-Ended_Scientif/review]] — 의료 AI 과학자와 The AI Scientist는 모두 자율 과학 연구를 다루지만, 임상 의학 특화와 범용 과학 발견이라는 서로 다른 도메인 접근법을 취합니다.
- 🔗 후속 연구: [[papers/612_PersonaAI_An_Interactive_Agentic-AI_Framework_for_Autonomous/review]] — 의료 AI 과학자 개발이 노화 연구의 가설 생성과 검증을 더 포괄적인 의료 연구로 확장할 수 있습니다.
