---
title: "165_Biokgbench_A_knowledge_graph_checking_benchmark_of_ai_agent"
authors:
  - "Xinna Lin"
  - "Siqi Ma"
  - "Junjie Shan"
  - "Xiaojing Zhang"
  - "Shell Xu Hu"
date: "2024"
doi: "arXiv:2407.00466"
arxiv: ""
score: 4.25
essence: "본 논문은 생의학 분야 AI 에이전트의 문헌 이해 능력을 평가하기 위해 **BioKGBench 벤치마크**를 제안한다. 기존 LLM 기반 평가의 환각(hallucination) 문제를 극복하기 위해 구조화된 지식그래프와 비구조화된 학술논문을 모두 활용하는 혼합형 평가 프레임워크를 도입한다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/Realistic_Discovery_Benchmarks"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Chang et al._2024_Biokgbench A knowledge graph checking benchmark of ai agent for biomedical science.pdf"
---

# BioKGBench: A Knowledge Graph Checking Benchmark of AI Agent for Biomedical Science

> **저자**: Xinna Lin, Siqi Ma, Junjie Shan, Xiaojing Zhang, Shell Xu Hu, Tiannan Guo, Stan Z. Li, Kaicheng Yu | **날짜**: 2024 | **DOI**: [arXiv:2407.00466](https://arxiv.org/abs/2407.00466)

---

## Essence

![Figure 1](figures/fig1.webp)
*그림 1: (좌) 기존 도메인 특화 AI 에이전트 벤치마크는 질의응답(QA) 같은 저수준 작업에만 집중하거나 과학자 코파일럿 복잡 파이프라인에 내재됨. (우) 본 논문은 지식그래프 질의응답(KGQA)과 과학 주장 검증(SCV)의 두 가지 원자적(atomic) 부작업으로 구성된 지식그래프 검증(KGCheck) 작업을 통해 생의학 AI 에이전트 평가의 격차를 해소함.*

본 논문은 생의학 분야 AI 에이전트의 문헌 이해 능력을 평가하기 위해 **BioKGBench 벤치마크**를 제안한다. 기존 LLM 기반 평가의 환각(hallucination) 문제를 극복하기 위해 구조화된 지식그래프와 비구조화된 학술논문을 모두 활용하는 혼합형 평가 프레임워크를 도입한다.

## Motivation

- **Known**: 
  - LLM 기반 AI 에이전트가 화학, 해양과학, 생의학 등 다양한 과학 분야로 확장되고 있음
  - 기존 평가는 MedQA, PubMedQA 등 QA 기반 벤치마크에 의존하며, LLM의 내재적 지식에 크게 의존하여 환각 문제 발생

- **Gap**: 
  - 과학자의 핵심 능력인 "문헌 이해"를 체계적으로 평가하는 벤치마크 부재
  - 기존 지식그래프(KG)는 수작업 구축으로 인해 유지 비용이 높고 정보 업데이트가 지연됨
  - 구조화된 데이터(KG)와 비구조화된 데이터(논문)를 함께 처리하는 에이전트 평가 기준 미흡

- **Why**: 
  - 생의학 KG(예: CKG)에는 오래된 정보나 오류가 존재하여 신뢰성 문제 발생
  - 에이전트가 외부 도구(검색, 그래프 쿼리)를 활용하여 환각을 완화해야 함
  - 과학자의 실제 업무(문헌 검토+데이터베이스 검색)를 모방하는 평가가 필요함

- **Approach**: 
  - "문헌 이해"를 두 가지 원자적 능력으로 분해: KGQA(구조화 데이터)와 SCV(비구조화 데이터)
  - 이 두 능력을 결합한 **Knowledge Graph Checking(KGCheck)** 작업 제안
  - 에이전트가 KG의 노드/트리플 정확성을 논문과 데이터베이스로 검증하도록 함

## Achievement

![Figure 2](figures/fig2.webp)
*그림 2: Clinical Knowledge Graph(CKG) 부분그래프는 12개 노드 유형과 18개 관계 유형을 포함.*

1. **포괄적 벤치마크 구축**: 
   - KGQA: 698개 질문(698=60 dev + 638 test)
   - SCV: 1,385개 데이터(120 dev + 1,265 test)  
   - KGCheck: 225개 전문가 주석 데이터(20 dev + 205 test)
   - CKG 부분그래프: 484,955개 노드, 18,959,943개 간선

2. **현존 에이전트의 한계 발굴**: 
   - GPT-4, Claude 등 최신 에이전트들이 벤치마크에서 부족한 성능 시현
   - 지식그래프 쿼리 및 문헌 검증 능력의 결합 필요성 증명

3. **실제 과학적 가치 입증**: 
   - BKGAgent로 CKG에서 **90개 이상의 사실적 오류** 발견
   - 지식베이스 업데이트를 위한 실용적 도구로의 활용 가능성 제시

## How

![Figure 3](figures/fig3.webp)
*그림 3: BKGAgent의 프레임워크.*

### 데이터 구성

- **KGQA 작업**: 
  - CKG에서 수작업으로 템플릿 설계(16개 질문 카테고리)
  - 세 가지 추론 유형: One-hop(56.0%), Multi-hop(28.7%), Conjunction(15.3%)
  - 템플릿 기반 자동 생성으로 확장

- **SCV 작업**: 
  - 동료 검토(peer-reviewed) 논문에서 추출한 과학적 주장 검증
  - 이진 분류: 참/거짓 주장 판정

- **KGCheck 작업**: 
  - KGQA와 SCV를 통합한 복합 작업
  - 에이전트가 KG 쿼리 결과를 논문 정보와 교차 검증

### BKGAgent 설계

- **도구 세트 (Tool Set)**:
  - KG 쿼리 도구: 특정 엔티티/관계 검색
  - 문헌 검색 도구: 관련 논문 추출(RAG 기반)
  - 검증 도구: LLM이 정보 일관성 판단

- **에이전트 루프**:
  1. KG에서 특정 주장/관계 쿼리
  2. 검색 엔진으로 관련 논문 수집
  3. LLM이 KG 정보와 논문 내용 비교
  4. 신뢰도 점수 할당 및 최종 판정

- **Retrieval-Augmented Generation (RAG)**: 
  - 도메인 기반 RAG를 활용한 정보 그라운딩
  - 환각 완화를 위해 외부 문헌으로 검증

## Originality

- **평가 관점의 혁신**: 
  - "AI Scientist" 관점에서 에이전트 평가(기존은 QA/실험 기반)
  - 구조화+비구조화 데이터 처리를 동시에 평가하는 첫 시도

- **실제 과학 업무 모방**: 
  - 문헌 검토+데이터베이스 쿼리라는 과학자의 실제 방법론 반영
  - 정적 벤치마크가 아닌 동적 지식그래프 검증 가능성 제시

- **생의학 도메인 특화**: 
  - CKG라는 실제 대규모 지식그래프 활용(484K 노드)
  - 도메인 전문가 주석을 통한 고품질 데이터셈(225개)

- **실질적 기여**: 
  - 기존 공개 KG의 오류 발견(90개+)으로 지식베이스 개선 가능성 입증
  - 에이전트 평가 → 지식베이스 개선이라는 선순환 시스템 제안

## Limitation & Further Study

- **한계**:
  - CKG의 부분그래프만 사용하여 전체 지식그래프 복잡성을 완전히 반영하지 못함
  - SCV 작업이 주로 이진 분류로 제한되어 더 정교한 주장 분석 미흡
  - 에이전트 평가에서 음성(false negative) 사례 분석 부족
  - 언어 다양성: 영어 중심으로 다언어 확장 미흡

- **후속 연구**:
  - 다른 생의학 도메인(약물 상호작용, 질환 치료법 등)으로 확장
  - 멀티모달 에이전트(이미지, 표, 그래프 처리) 평가 추가
  - 지식그래프 자동 업데이트 메커니즘 개발
  - 설명 가능성(explainability) 평가 지표 강화


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4/5
- Significance: 4.5/5
- Clarity: 4/5
- Overall: 4.25/5

**총평**: 본 논문은 생의학 AI 에이전트 평가의 중요한 공백을 메우며, 구조화된 지식그래프와 비구조화된 학술논문을 통합하는 혁신적인 벤치마크를 제시한다. 실제 과학 업무를 반영한 설계와 90개 이상의 지식베이스 오류 발견을 통해 실질적 가치를 입증했으나, 부분그래프 사용과 이진 분류 중심의 평가 설계는 추가 확장의 여지를 남긴다.

## Related Papers

- 🔗 후속 연구: [[papers/371_GeneAgent_self-verification_language_agent_for_gene-set_anal/review]] — 유전자 분석에서 검증된 자기검증 방법론을 지식 그래프 검사로 확장하여 더 넓은 생명과학 응용을 가능하게 한다.
- 🔗 후속 연구: [[papers/164_BioInformatics_Agent_BIA_Unleashing_the_Power_of_Large_Langu/review]] — BIA의 단일세포 RNA 시퀀싱 자동화는 BioKGBench의 생물학 지식그래프 검증 기능을 확장하여 실시간 데이터 분석과 결과 해석을 통합한 완전한 생물정보학 워크플로우를 제공합니다.
