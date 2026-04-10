---
title: "848_TxAgent_An_AI_Agent_for_Therapeutic_Reasoning_Across_a_Unive"
authors:
  - "Shanghua Gao"
  - "Richard Zhu"
  - "Zhenglun Kong"
  - "Ayush Noori"
  - "Xiaorui Su"
date: "2025.03"
doi: "미제공"
arxiv: ""
score: 4.25
essence: "정밀 치료(precision therapeutics)를 위해 211개의 생의학 도구(biomedical tools)를 활용한 다단계 추론 AI 에이전트 TxAgent를 제시하며, FDA 승인 약물 정보와 Open Targets 임상 정보를 통합하여 약물 상호작용, 금기사항, 환자별 맞춤 치료 전략을 분석한다."
tags:
  - "cat/AI-Powered_Scientific_Research_Frameworks"
  - "sub/Domain-specific_Language_Agents"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Gao et al._2025_TxAgent An AI Agent for Therapeutic Reasoning Across a Universe of Tools.pdf"
---

# TxAgent: An AI Agent for Therapeutic Reasoning Across a Universe of Tools

> **저자**: Shanghua Gao, Richard Zhu, Zhenglun Kong, Ayush Noori, Xiaorui Su, Curtis Ginder, Theodoros Tsiligkaridis, Marinka Zitnik | **날짜**: 2025-03-14 | **DOI**: [미제공](https://doi.org/)

---

## Essence

정밀 치료(precision therapeutics)를 위해 211개의 생의학 도구(biomedical tools)를 활용한 다단계 추론 AI 에이전트 TxAgent를 제시하며, FDA 승인 약물 정보와 Open Targets 임상 정보를 통합하여 약물 상호작용, 금기사항, 환자별 맞춤 치료 전략을 분석한다.

## Motivation

- **Known**: 대규모 언어모델(LLM)은 사전학습과 의료 데이터 미세조정(fine-tuning)으로 의료 작업을 처리할 수 있으며, 도구 증강 LLM은 검색기반 생성(RAG)을 통해 외부 지식을 활용할 수 있다.

- **Gap**: 기존 LLM은 (1) 업데이트된 생의학 지식에 실시간 접근 불가, (2) 환각(hallucination) 문제, (3) 다중 임상 변수에 대한 신뢰할 수 없는 추론, (4) 도구 증강 모델도 다단계 추론이 어렵다.

- **Why**: 정밀 치료는 약물 상호작용, 금기사항, 환자 특성(나이, 유전 인자, 질병 진행도), 동시약물복용(polypharmacy) 등 여러 요소를 종합적으로 평가해야 하며 반복적 추론이 필수이다.

- **Approach**: 검증된 생의학 도구 211개를 통합한 ToolUniverse와 다단계 추론이 가능한 미세조정 LLM, 적응형 도구 검색 모델(ToolRAG)을 결합한 AI 에이전트 개발.

## Achievement

1. **벤치마크 성능**: 5개 신규 벤치마크(DrugPC, BrandPC, GenericPC, TreatmentPC, DescriptionPC)에서 기존 LLM 및 도구사용 모델 초과
   - DrugPC: 92.1% 정확도 (GPT-4o: 66.3%, 25.8% 향상)
   - Llama-3.1-70B 대비 39.3% 향상 (모델은 1/9 크기)
   - DeepSeek-R1(671B) 대비 7.5% 높은 정확도

2. **강건성(Robustness)**: 약물명 변형(브랜드명, 일반명, 설명) 간 정확도 편차 <0.01 (GPT-4o: 9.96)
   - DescriptionPC: 56.5% 정확도 (GPT-4o 상대 8.3% 향상)

3. **맞춤형 치료**: TreatmentPC(456개 실제 치료 시나리오)에서 GPT-4o 대비 13.6%, Llama 대비 25.4% 향상

## How

- **ToolUniverse 구성**: 1939년 이후 FDA 승인 약물 전수, Open Targets 임상 통찰, openFDA, Human Phenotype Ontology 등 신뢰 출처 통합

- **학습 데이터셋**: 
  - 378,027개 명령어조정(instruction-tuning) 샘플
  - 85,340개 다단계 추론 흔적(reasoning trace)
  - 177,626개 추론 단계, 281,695개 함수 호출
  - QuestionGen 및 TraceGen 다중에이전트로 생성

- **인퍼런스 프로세스**:
  1. 치료 질문 또는 이전 도구 피드백 수신
  2. 사고 과정(thought process) 생성
  3. ToolRAG로 관련 도구 검색·선택
  4. 함수 호출 실행 및 피드백 받음
  5. 최종 답변에 도달할 때까지 반복 (FINISH 도구로 종료)

- **주요 능력**:
  - 검증된 지식 기반 도구 호출을 통한 정보 접지(knowledge grounding)
  - 목표 지향적 도구 선택 (예: 약물 용량 조회 시 get_dosage 자동 선택)
  - 미충족 정보 처리를 위한 다단계 추론

## Originality

- **새로운 데이터셋 구성**: 다중에이전트 시스템(TOOLGEN, QUESTIONGEN, TRACEGEN)으로 자동화된 도구 생성 및 학습 데이터 구축

- **ToolUniverse**: 211개 도구의 체계적 통합으로 의약학 지식의 단일 통합 인터페이스 제공

- **ToolRAG 모델**: 쿼리 문맥 기반 동적 도구 검색으로 정적 사전학습 극복

- **다양한 벤치마크 개발**: 구조화된 질의부터 비구조화 설명까지 포괄하는 평가 프레임워크

- **투명성 제공**: 최종 답변과 함께 상세한 추론 흔적 제시로 임상 의사결정의 설명 가능성 확보

## Limitation & Further Study

- **임상 검증 부재**: 실제 환자 데이터 또는 임상의 피드백을 통한 검증 필요

- **도구 지연성**: 외부 도구 호출의 지연 시간 영향 미분석

- **희귀약물/신약**: 1939년 이후 데이터 기반이므로 매우 최신 약물이나 임상시험약(IND) 정보 제한

- **환자 이질성**: 표준 임상 변수 중심으로, 다양한 민족·유전배경에서의 약물대사(pharmacogenomics) 개인화 수준 불명확

- **후속 연구**:
  - 실제 임상 환경에서의 배포 및 의료진 만족도 평가
  - 약물 유전체학(pharmacogenomics) 통합 강화
  - 도구 통합에 따른 지연성 최소화 기술
  - 다국가 임상 가이드라인 지원 확대

## Evaluation

- **Novelty**: 4.5/5 — 다중에이전트 도구 구축 및 211개 도구 통합은 참신하나, AI 에이전트 아키텍처 자체는 기존 work의 응용

- **Technical Soundness**: 4/5 — 다단계 추론, ToolRAG, 학습 데이터 구축 방법론 견고하지만, 실제 임상 검증 및 오류 분석 부족

- **Significance**: 4.5/5 — 정밀 의학 분야에 즉시 적용 가능하며 FDA 데이터 통합으로 실용성 높음. 다만 실제 임상 영향 입증 필요

- **Clarity**: 4/5 — 전체 구조와 벤치마크가 명확하나, 본문 후반 세부 기술 설명 일부 생략

- **Overall**: 4.25/5

**총평**: TxAgent는 대규모 생의학 도구 통합과 다단계 추론 능력으로 약물 치료 추천에서 기존 LLM을 크게 능가하는 의의 있는 성과이며, 정밀 의료 분야에서 즉각적 임상 응용이 가능하나 실제 환자 데이터 기반 임상 검증을 통한 보완이 필수적이다.

## Related Papers

- 🧪 응용 사례: [[papers/212_Chemist-X_Large_Language_Model-empowered_Agent_for_Reaction/review]] — 화학 반응 조건 최적화 기술을 치료 추론과 약물 상호작용 분석으로 확장 적용할 수 있다
- 🏛 기반 연구: [[papers/499_LLM_With_Tools_A_Survey/review]] — 도구를 활용한 LLM의 포괄적 조사가 211개 생의학 도구를 활용한 치료 추론 에이전트의 기반을 제공한다
- 🔗 후속 연구: [[papers/225_Clinicalgpt-r1_Pushing_reasoning_capability_of_generalist_di/review]] — 임상 추론을 위한 생성형 AI를 정밀 치료를 위한 다도구 AI 에이전트로 확장할 수 있다
