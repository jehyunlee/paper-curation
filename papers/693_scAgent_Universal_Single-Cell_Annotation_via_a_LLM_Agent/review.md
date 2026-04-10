---
title: "693_scAgent_Universal_Single-Cell_Annotation_via_a_LLM_Agent"
authors:
  - "Yuren Mao"
  - "Yu Mi"
  - "Peigen Liu"
  - "Mengfei Zhang"
  - "Hanqing Liu"
date: "2025"
doi: "10.48550/arXiv.2504.04698"
arxiv: ""
score: 4.0
essence: "대규모 언어 모델(LLM) 기반 에이전트를 활용한 범용 단일세포 주석(cell annotation) 프레임워크로, 조직 간 일반화, 신규 세포 타입 발견, 데이터 효율성을 동시에 달성한다. scAgent는 160개 세포 타입과 35개 조직에서 우수한 성능을 보여준다."
tags:
  - "cat/Cognitive_AI_Evaluation_and_Benchmarking"
  - "sub/AI_Chemistry_Planning"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Mao et al._2025_scAgent Universal Single-Cell Annotation via a LLM Agent.pdf"
---

# scAgent: Universal Single-Cell Annotation via a LLM Agent

> **저자**: Yuren Mao, Yu Mi, Peigen Liu, Mengfei Zhang, Hanqing Liu | **날짜**: 2025 | **DOI**: [10.48550/arXiv.2504.04698](https://doi.org/10.48550/arXiv.2504.04698)

---

## Essence

![Figure 1](figures/fig1.webp) *scAgent의 전체 프레임워크: (a) 다양한 사용자 쿼리에 대응하는 능력, (b) 계획 모듈의 구조, (c) 행동 공간의 구성, (d) 메모리 모듈의 정보*

대규모 언어 모델(LLM) 기반 에이전트를 활용한 범용 단일세포 주석(cell annotation) 프레임워크로, 조직 간 일반화, 신규 세포 타입 발견, 데이터 효율성을 동시에 달성한다. scAgent는 160개 세포 타입과 35개 조직에서 우수한 성능을 보여준다.

## Motivation

- **Known**: 단일세포 RNA-seq(scRNA-seq) 기반의 딥러닝 모델들이 특정 조직의 고정된 수의 세포 타입 주석에서 진전을 이루었다. 마커 유전자 기반 방법과 참조 데이터 기반 방법이 존재한다.
  
- **Gap**: 기존 CTA(Cell Type Annotation) 모델들은 조직 간 일반화 능력이 부족하고, 신규 세포 타입의 발견과 확장이 불가능하며, 데이터 효율성이 낮다. 최근 scTab도 신규 세포 타입 발견 불가능 및 데이터 비효율 문제가 있다.
  
- **Why**: 범용 세포 주석은 Human Cell Atlas(HCA)와 같은 대규모 작업에 필수적이며, 다양한 조직과 세포 타입을 아우르는 통합적 솔루션이 필요하다.
  
- **Approach**: LLM 기반의 자율 에이전트 아키텍처로 계획 모듈(Planning Module), 행동 공간(Action Space), 메모리 모듈(Memory Module)을 통해 다중 턴 상호작용으로 세포 주석을 자동화한다.

## Achievement

![Figure 2](figures/fig2.webp) *교차 조직 CTA 성능: (a,b) CG 데이터셋과 TS 데이터셋에서 정확도, 가중 F1-score, 매크로 F1-score 비교 (c) 혼동 행렬을 통한 다양한 세포 타입 분류 (d,e) 조직별 가중 F1-score 성능*

1. **최첨단 성능**: CG 데이터셋에서 매크로 F1-score 89.31%로 두 번째 순위 방법(scTab 10X data, 82.58%)을 6.73 포인트 앞지르며, 10배 적은 훈련 데이터로 달성

2. **우수한 일관성**: 모든 조직에서 우수한 성능 유지(표준편차 ~0.07), 특히 자궁, 태반, 유방 등 8개 중요 조직에서 99% 이상의 가중 F1-score 달성

3. **데이터 효율성**: 동일한 크기의 훈련 데이터에서 scGPT 등 기존 방법 대비 현저히 높은 성능

## How

![Figure 3](figures/fig3.webp) *신규 세포 발견 및 배치 효과 보정 성능*

- **계획 모듈**: DeepSeek-R1 671B LLM을 기반으로 사용자 쿼리를 입력받아 행동 공간의 도구와 메모리 정보를 통합하여 상세한 실행 계획 생성

- **행동 공간**: 
  - scGPT(3,300만 세포 학습) 기반 scRNA 모델을 주요 임베딩 모델로 사용
  - 30개 이상의 MoE-LoRA(Mixture-of-Experts with Low-Rank Adaptation) 조직별 플러그인 구현
  - 저계수(low-rank) 어댑터만 미세조정하여 데이터 효율성 극대화
  - 아웃라이어 검출 및 임베딩 비교 도구로 신규 세포 타입 발견 지원
  - 증분 학습(Incremental Training) 도구로 지속적 업데이트 가능

- **메모리 모듈**: 
  - CELLxGENE와 Tabula Sapiens의 공개 데이터셋과 사용자 업로드 데이터 저장
  - Milvus 벡터 데이터베이스에 scGPT(플러그인 적용 여부)로 생성한 임베딩 저장
  - 쿼리 로그, 도구 실행 순서, 캐시로 의사결정 효율화

- **MoE-LoRA 아키텍처**: 기반 모델의 사전학습 가중치 공유하면서 조직별 저계수 어댑터로 재앙적 망각(catastrophic forgetting) 방지 및 무한 확장성 보장

## Originality

- **LLM 기반 에이전트 프레임워크**: 기존 CTA의 단순 분류 접근에서 벗어나 LLM의 추론 능력으로 적응형 계획 생성 및 다중 턴 상호작용 가능

- **MoE-LoRA 플러그인 아키텍처**: 조직별 특화 모듈의 동적 통합으로 높은 성능 유지하면서 파라미터 효율성 극대화

- **신규 세포 타입 발견**: 임베딩 기반 아웃라이어 검출과 메모리 비교를 통한 자동화된 미지의 세포 타입 검출

- **데이터 효율적 확장성**: 증분 학습 도구를 통해 새로운 데이터 추가 시 기존 성능 유지하면서 지속적 개선

## Limitation & Further Study

- **제한사항**:
  - DeepSeek-R1 671B와 같은 대규모 LLM의 높은 계산 비용으로 인한 실용성 저하 가능성
  - 메모리 모듈의 임베딩 저장 및 검색 과정의 확장성에 대한 구체적 성능 분석 부족
  - 신규 세포 타입 발견의 정확도 평가 지표가 제한적

- **후속 연구**:
  - 경량 LLM(예: Llama, Qwen)으로의 플러닝 모듈 대체 가능성 탐색
  - 다중 모달(멀티 오믹스) 데이터 통합 확장
  - 실제 임상 데이터 적용 및 검증 필요
  - 신규 세포 타입 판별 기준의 생물학적 타당성 강화

## Evaluation

- **Novelty**: 4.5/5
  - LLM 에이전트 적용의 참신성과 MoE-LoRA 플러그인의 창의성은 높으나, 개별 기술 조합의 성격

- **Technical Soundness**: 4/5
  - 전체 아키텍처 설계는 견고하나, 신규 세포 발견의 기술적 타당성 및 하이퍼파라미터 선택에 대한 설명 부족

- **Significance**: 4.5/5
  - 범용 세포 주석 문제의 실질적 해결과 160개 세포 타입 35개 조직에 걸친 광범위한 검증으로 높은 영향력

- **Clarity**: 3.5/5
  - 전체 구조는 명확하나, 각 도구의 상세한 작동 원리와 임베딩 분석 방법에 대한 기술적 설명 미흡

- **Overall**: 4/5

**총평**: scAgent는 LLM 기반 에이전트 아키텍처와 MoE-LoRA 플러그인을 결합하여 범용 세포 주석의 세  가지 과제(일반화, 신규 발견, 확장성)를 동시에 해결한 혁신적 접근법으로, 광범위한 실험적 검증을 통해 우수한 성능을 입증했다. 다만 LLM 계산 비용과 신규 세포 판별 기준의 생물학적 엄밀성에 대한 보완이 필요하다.

## Related Papers

- 🧪 응용 사례: [[papers/064_Agentic_AI_for_Scientific_Discovery_A_Survey_of_Progress_Cha/review]] — 과학 발견을 위한 에이전틱 AI 시스템의 구체적인 생물학 분야 적용 사례로서 단일세포 주석에 특화된다.
- 🔗 후속 연구: [[papers/193_CellAgent_An_LLM-driven_Multi-Agent_Framework_for_Automated/review]] — LLM 기반 다중 에이전트 세포 분석 프레임워크가 범용 단일세포 주석을 더 포괄적인 세포 분석으로 확장한다.
- 🏛 기반 연구: [[papers/431_Integrated_analysis_of_multimodal_single-cell_data/review]] — 멀티모달 단일세포 데이터 통합 분석이 LLM 기반 세포 주석 프레임워크의 데이터 처리 기반을 제공한다.
- 🔄 다른 접근: [[papers/189_CASSIA_a_multi-agent_large_language_model_for_reference_free/review]] — 단일세포 주석 작업에 대한 다른 LLM 기반 접근법
- 🏛 기반 연구: [[papers/064_Agentic_AI_for_Scientific_Discovery_A_Survey_of_Progress_Cha/review]] — 과학 발견을 위한 에이전틱 AI의 종합적 체계가 단일세포 주석과 같은 구체적인 생물학 응용의 이론적 프레임워크를 제공한다.
- 🔗 후속 연구: [[papers/431_Integrated_analysis_of_multimodal_single-cell_data/review]] — 가중 최근접 이웃 기반 멀티모달 데이터 통합이 LLM 에이전트를 활용한 범용 단일세포 주석 시스템으로 발전했다
- 🔗 후속 연구: [[papers/193_CellAgent_An_LLM-driven_Multi-Agent_Framework_for_Automated/review]] — 단일세포 주석화를 위한 LLM 에이전트를 자동화된 분석 파이프라인으로 확장할 수 있다
- 🔄 다른 접근: [[papers/069_Agentomics-ML_Autonomous_Machine_Learning_Experimentation_Ag/review]] — 단일 세포 주석을 위한 LLM 에이전트의 다른 접근 방식을 제시한다.
- 🧪 응용 사례: [[papers/344_Foundation_models_in_bioinformatics/review]] — LLM 에이전트 기반 단일 세포 주석화가 생물정보학 기초 모델의 실제 적용 사례를 보여줍니다.
- 🧪 응용 사례: [[papers/681_Revisiting_Gene_Ontology_Knowledge_Discovery_with_Hierarchic/review]] — LLM 에이전트를 통한 단일 세포 주석의 구체적 적용으로 생물학적 지식 추출을 보여준다.
