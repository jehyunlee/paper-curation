---
title: "451_Knowledge-guided_large_language_model_for_material_science"
authors:
  - "Guanjie Wang"
  - "Jingjing Hu"
  - "Jian Zhou"
  - "Sen Liu"
  - "Qingjiang Li"
date: "2025.02"
doi: "10.1016/j.revmat.2025.100007"
arxiv: ""
score: 4.2
essence: "ChatGPT로 촉발된 대규모 언어모델(LLM)의 혁신을 재료과학 분야에 체계적으로 적용하기 위한 지식-안내식 도메인 특화 모델 개발 및 활용 방법론을 제시한 종합 리뷰 논문이다. 본 논문은 LLM 구축부터 재료 발견에의 실제 응용까지 전주기적 가이드라인을 제공한다."
tags:
  - "cat/AI-Powered_Scientific_Research_Frameworks"
  - "sub/Domain-specific_Language_Agents"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Wang et al._2025_Knowledge-guided large language model for material science.pdf"
---

# Knowledge-guided large language model for material science

> **저자**: Guanjie Wang, Jingjing Hu, Jian Zhou, Sen Liu, Qingjiang Li, Zhimei Sun | **날짜**: 2025-02-01 | **DOI**: [10.1016/j.revmat.2025.100007](https://doi.org/10.1016/j.revmat.2025.100007)

---

## Essence

![Fig. 1](figures/fig1.webp)
*그림 1: 최근 년도별 대규모 언어모델의 발전 timeline. 오픈소스 LLM은 노란색으로 표시*

ChatGPT로 촉발된 대규모 언어모델(LLM)의 혁신을 재료과학 분야에 체계적으로 적용하기 위한 지식-안내식 도메인 특화 모델 개발 및 활용 방법론을 제시한 종합 리뷰 논문이다. 본 논문은 LLM 구축부터 재료 발견에의 실제 응용까지 전주기적 가이드라인을 제공한다.

## Motivation

- **Known**: LLM(GPT-3, ChatGPT 등)이 자연언어처리에서 뛰어난 성능을 보였으며, 헬스케어, 화학, 물리학 등 다양한 과학 분야에서 잠재력을 입증했다.

- **Gap**: 그러나 재료과학에 특화된 도메인-특화 LLM 개발은 여전히 미흡하며, 일반 목적 모델을 재료 관련 과제에 적응시키는 구체적 전략과 실용적 지침이 부재하다.

- **Why**: 재료과학은 다중 공간-시간 스케일, 복잡한 시스템, 다양한 데이터 소스를 포함하는 고도로 학제적인 분야이며, 기존 도메인-특화 모델의 확장성과 적응성으로는 이러한 복잡성을 충분히 해결할 수 없다.

- **Approach**: LLM 구축 프레임워크(목표 결정, 데이터 큐레이션, 모델 아키텍처 설계, 훈련 및 평가 프레임워크), 도메인 특화 방법론(파인튜닝, 검색-증강 생성, 프롬프트 엔지니어링, AI 에이전트), 재료과학 응용 분야를 체계적으로 검토한다.

## Achievement

![Fig. 2](figures/fig2.webp)
*그림 2: LLM을 처음부터 구축하기 위한 프레임워크*

1. **LLM 개발 이정표 정리**: 통계적 언어모델(1990s) → 신경 언어모델(2000s) → 사전학습 언어모델/BERT → 초대형 모델(GPT-3, PaLM) → ChatGPT/GPT-4 → 다중모드 모델(Claude 3, LLaMA 3)까지의 진화 과정을 시간별로 체계화했다.

2. **실용적 LLM 구축 가이드라인**: 범위-목표 결정 → 아키텍처 설계 → 데이터 큐레이션 → 훈련 프레임워크 수립 → 평가 체계 구축의 5단계 프로세스를 제시했다. 

3. **도메인 특화 방법론의 비교분석**: 파인튜닝, 매개변수 효율적 파인튜닝(PEFT), 검색-증강 생성(RAG), 프롬프트 엔지니어링의 장단점을 상세히 분석하고 적용 시나리오를 제시했다.

4. **재료과학 응용 사례 확대**: 정형화된 정보 추출, 물성 예측, 신규 화합물 발견, 자율 실험실, 로봇 기반 재료 발견까지 구체적 응용 분야를 매핑했다.

## How

![Fig. 3](figures/fig3.webp)
*그림 3: LLM 파인튜닝을 위한 프레임워크. (a) 매개변수 효율적 파인튜닝의 3가지 단계*

![Fig. 4](figures/fig4.webp)
*그림 4: 검색-증강 생성(RAG)의 개요*

![Fig. 5](figures/fig5.webp)
*그림 5: (a) 비에이전트, (b) 에이전트, (c) 다중 에이전트 워크플로우*

**재료과학 LLM 구축 및 적용 방법론**:

- **아키텍처 설계**: Transformer 기반 구조 채택 → 자기-주의(Self-Attention) 메커니즘으로 재료 데이터 간 관계성 포착 → 다중-헤드 주의(Multi-Head Attention)로 다양한 재료 정보 표현 → 위치 인코딩으로 원자 배열이나 합성 경로 등 시퀀셜 정보 처리

- **데이터 큐레이션**: 실험 측정값, 고처리량 시뮬레이션, 문헌 데이터베이스 등 다양한 출처에서 고품질 도메인-관련 데이터 수집 및 정제 → 재료 특성별(구성, 구조, 성질)로 데이터 분류

- **파인튜닝 전략**: 전체 모델 파인튜닝(Full Fine-tuning) vs 매개변수 효율적 파인튜닝(LoRA, Prefix Tuning 등) 선택 → 계산 자원과 정확도 트레이드오프 고려

- **검색-증강 생성(RAG)**: 외부 재료 데이터베이스(Materials Project, ICSD 등)를 지식 소스로 연결 → 검색 결과를 기반으로 생성 → 할루시네이션 완화 및 최신 정보 반영

- **프롬프트 엔지니어링**: 재료 특성 예측 시 화학식, 결정 구조, 공정 조건 등을 체계적으로 입력 → Few-shot 예시 제공으로 모델 성능 향상

- **AI 에이전트**: 도구(계산 소프트웨어, 데이터베이스) 활용 능력 → 자율적 추론 → 다중 에이전트 협력으로 복잡한 재료 발견 과정 자동화

## Originality

- 일반적 LLM 리뷰가 아닌 **재료과학 특화 관점**에서 도메인 맞춤 LLM 개발 프로세스를 체계적으로 정립한 점이 독창적이다.

- 모델 구축(From Scratch) → 도메인 특화 방법(Fine-tuning, RAG, 프롬프트) → 실제 응용(자율 실험실, 로봇)까지 **전주기적 통합 가이드라인**을 처음으로 제시했다.

- 기존 리뷰대비 **구체적 구현 기술**(PEFT, LoRA, Prefix Tuning 등)과 **도구/플랫폼 정보**까지 포함하여 실제 연구자가 활용 가능한 수준의 상세함을 제공한다.

- AI 에이전트와 다중 에이전트 시스템을 재료 발견에 명시적으로 적용하는 새로운 관점을 제시한다.

## Limitation & Further Study

- **데이터 부족**: 재료과학 도메인의 고품질, 공개 데이터셋이 제한적이며, 특정 재료 클래스(예: 신소재)의 학습 데이터 희소성이 여전히 과제이다.

- **계산 자원 장벽**: 수십억 개 매개변수를 가진 대규모 모델 훈련에는 막대한 GPU/TPU 자원이 필요하여 중소 연구그룹의 진입장벽이 높다.

- **할루시네이션 문제**: LLM의 신뢰성 보장, 특히 재료 물성 예측과 같은 중요한 응용에서 잘못된 정보 생성 방지 메커니즘이 미흡하다.

- **벤치마킹 표준화 부재**: 재료과학 LLM의 성능 평가를 위한 통합적 평가 메트릭과 벤치마크 데이터셋 개발이 필요하다.

- **후속 연구 방향**: (1) 오픈소스 재료 데이터베이스 통합 강화, (2) 파운데이션 모델(Foundation Model)을 재료과학에 맞게 적응시키는 기법 개발, (3) 설명가능성(Explainability) 향상, (4) AI 안전성 및 윤리 지침 정립 필요하다.

## Evaluation

- **Novelty (독창성)**: 4.5/5 - 재료과학 특화 LLM 개발의 체계적 프레임워크를 처음 제시하나, 개별 기술(파인튜닝, RAG 등)은 기존 기술의 재조합이다.

- **Technical Soundness (기술적 타당성)**: 4/5 - Transformer 아키텍처 및 도메인 특화 방법론은 충분히 검증되었으나, 재료과학 특정 구현 상세는 추가 검증이 필요하다.

- **Significance (중요성)**: 4.5/5 - 재료 발견 가속화라는 중요한 응용 잠재력이 있으나, 현실적 제약(데이터 부족, 계산 자원)으로 인한 즉각적 영향은 제한적이다.

- **Clarity (명확성)**: 4/5 - 전반적으로 잘 구조화되었으나, 일부 기술 용어의 상세 설명과 구체적 구현 코드 예시가 보강되면 더욱 명확할 것이다.

- **Overall (종합)**: 4.2/5

**총평**: 본 논문은 ChatGPT 시대의 재료과학 연구 혁신을 위해 LLM을 실제로 구축하고 활용하는 방법을 체계적으로 정리한 중요한 종합 리뷰이며, 도메인-특화 LLM 개발의 실용적 로드맵을 제공한다는 점에서 학술적·실무적 가치가 높으나, 재료과학 특정 데이터셋과 할루시네이션 방지 기술의 고도화 같은 후속 연구가 절실하다.

## Related Papers

- 🔄 다른 접근: [[papers/523_MatterChat_A_Multi-Modal_LLM_for_Material_Science/review]] — 재료과학 LLM이라는 동일한 목표를 지식 안내와 구조 인식이라는 서로 다른 접근법으로 구현합니다.
- 🔗 후속 연구: [[papers/111_AtomAgents_Alloy_design_and_discovery_through_physics-aware/review]] — 재료과학 LLM의 이론적 방법론을 합금 설계라는 구체적 응용으로 확장하는 실용적 사례입니다.
- 🏛 기반 연구: [[papers/346_Foundation-Model_Surrogates_Enable_Data-Efficient_Active_Lea/review]] — 재료 발견을 위한 능동 학습 시스템의 도메인 특화 언어 모델 기반을 제공합니다.
- 🧪 응용 사례: [[papers/015_A_Perspective_on_Foundation_Models_in_Chemistry/review]] — 재료과학 안내 대형 언어모델은 화학 분야 파운데이션 모델의 구체적인 재료과학 응용 사례입니다
- 🏛 기반 연구: [[papers/111_AtomAgents_Alloy_design_and_discovery_through_physics-aware/review]] — 재료과학 분야 LLM 활용의 이론적 기초와 체계적 방법론을 제공합니다.
- 🧪 응용 사례: [[papers/260_DeepCRE_Transforming_Drug_RD_via_AI-Driven_Cross-drug_Respon/review]] — 재료과학 LLM 방법론을 약물 발견이라는 생의학 도메인에 적용하는 학제간 접근을 보입니다.
- 🧪 응용 사례: [[papers/346_Foundation-Model_Surrogates_Enable_Data-Efficient_Active_Lea/review]] — 재료과학 LLM 방법론을 능동 학습 기반 소재 발견에 구체적으로 적용하는 실용적 사례입니다.
- 🔄 다른 접근: [[papers/523_MatterChat_A_Multi-Modal_LLM_for_Material_Science/review]] — 재료과학 특화 LLM이라는 동일한 목표를 구조 인식과 지식 안내라는 상호 보완적 방법으로 달성합니다.
- 🔗 후속 연구: [[papers/626_Polymer_Brushes_and_Grafted_Polymers_AIML-Driven_Synthesis_S/review]] — 재료과학 LLM 방법론을 중합체 브러시라는 특정 재료 시스템에 적용하는 전문화된 사례입니다.
- 🔗 후속 연구: [[papers/613_Personalized_graph-based_retrieval_for_large_language_models/review]] — 지식 안내 언어 모델의 개념을 개인화된 지식 그래프로 확장하여 더 정교한 사용자별 정보 검색이 가능하다.
