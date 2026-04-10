---
title: "730_Sciqag_A_framework_for_auto-generated_science_question_answe"
authors:
  - "Yuwei Wan"
  - "Yixuan Liu"
  - "Aswathy Ajith"
  - "Clara Grazian"
  - "Bram Hoex"
date: "2024"
doi: "arXiv:2405.09939"
arxiv: ""
score: 4.0
essence: "대규모 언어모델(LLM)을 활용하여 과학 논문으로부터 자동으로 고품질의 개방형 질의응답 쌍(188,042개 QA 쌍, 24개 과학 분야)을 생성하고, 세밀한 평가 지표(RACAR)로 품질을 필터링하는 SciQAG 프레임워크를 제안한다."
tags:
  - "cat/LLM-Based_Scientific_Reasoning"
  - "sub/Scientific_Literature_Analysis"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Skarlinski et al._2024_Sciqag A framework for auto-generated science question answering dataset with fine-grained evaluati.pdf"
---

# SciQAG: A framework for auto-generated science question answering dataset with fine-grained evaluation

> **저자**: Yuwei Wan, Yixuan Liu, Aswathy Ajith, Clara Grazian, Bram Hoex, Wenjie Zhang, Chunyu Kit, Tong Xie, Ian Foster | **날짜**: 2024 | **DOI**: [arXiv:2405.09939](https://arxiv.org/abs/2405.09939)

---

## Essence

![Figure 1](figures/fig1.webp)
*SciQAG 프레임워크: 과학 문헌으로부터 QA 생성 (점선은 선택적 미세조정)*

대규모 언어모델(LLM)을 활용하여 과학 논문으로부터 자동으로 고품질의 개방형 질의응답 쌍(188,042개 QA 쌍, 24개 과학 분야)을 생성하고, 세밀한 평가 지표(RACAR)로 품질을 필터링하는 SciQAG 프레임워크를 제안한다.

## Motivation

- **Known**: 기존 과학 QA 데이터셋(SciQ, ScienceQA 등)은 주로 선택지형(MCQ) 형식의 교과서 기반 문제로 구성되어 있으며, 크라우드소싱/전문가 주석에 의존하여 비용이 높다.

- **Gap**: (1) 문제 형식의 다양성 부족 (2) 실제 연구 수준의 어려운 문제 부족 (3) 고가의 인적 주석 의존성

- **Why**: 과학 LLM의 미세조정과 평가를 위해서는 대규모의 고품질 과학 QA 쌍이 필수적이다. 특히 개방형 질문(open-ended question)은 모델의 추론 능력을 더 강하게 검증할 수 있다.

- **Approach**: LLM 기반 QA 생성기(Generator)와 5차원 평가 지표(RACAR: Relevance, Agnosticism, Completeness, Accuracy, Reasonableness)를 갖춘 QA 평가기(Evaluator)로 구성된 자동화 프레임워크를 개발하여 비용 효율적인 대규모 데이터셋 구축을 추구한다.

## Achievement

![Figure 2](figures/fig2.webp)
*GPT-4 점수와 전문가 주석 점수 간의 Spearman/Pearson 상관계수*

1. **대규모 고품질 데이터셋 구축**: 22,743개 과학 논문에서 188,042개의 QA 쌍을 생성하고, SciQAG-24D 벤치마크 구성 (24개 과학 분야 커버)

2. **신뢰성 있는 평가 지표 개발**: RACAR 지표와 GPT-4 기반 자동 평가가 도메인 전문가 평가와 높은 상관계수(Spearman/Pearson > 0.7)를 보임으로써 자동화 평가의 타당성 검증

3. **미세조정 효과 입증**: SciQAG 데이터셋으로 미세조정한 LLM이 (a) 미지의 SciQAG 테스트 셋, (b) SciQ 벤치마크, (c) 실제 과학 과제 에서 모두 성능 향상을 시현

## How

- **QA 생성기(Generator)**: 
  - 입력: 과학 논문 텍스트
  - 프로세스: (1) 15개 핵심 키워드 추출 → (2) 키워드를 기반으로 10개 QA 쌍 생성
  - 폐쇄형(closed-book) QA 요구: 생성된 질문이 원문의 도표/그림에 의존하지 않도록 프롬프트 설계

- **QA 평가기(Evaluator)**:
  - 5차원 평가 지표(RACAR) 정의 및 GPT-4 기반 자동 평가 시스템 구축
  - 도메인 전문가 수동 평가를 통한 검증 (상관계수 > 0.7)
  - 낮은 품질 QA 쌍 필터링

- **미세조정 전략**: 
  - 개방형 또는 폐쇄형 LLM 모두 사용 가능 (프롬프팅 또는 미세조정)
  - 비용 효율성을 위해 오픈소스 LLM 미세조정 선택

## Originality

- **자동 생성 + 평가의 통합 프레임워크**: 기존 자동 QA 생성 방법은 사전 정의된 답변에 의존하거나 규칙 기반(지식 그래프 필요)이었으나, 본 논문은 미정의 답변으로부터 개방형 QA를 직접 생성

- **폐쇄형 개방형 QA 집중**: 기존 과학 QA 데이터셋 대부분이 선택지형(MCQ)이거나 제한된 도메인(AI, 생의학)이었으나, 본 논문은 24개 과학 분야의 개방형 QA를 대규모로 생성

- **5차원 평가 지표(RACAR)**: HoneyBee의 평가 메트릭을 확장하여 과학 QA 특화 평가 프레임워크 개발 및 GPT-4 기반 자동 평가의 타당성 입증

- **공개 자산**: 데이터셋, 미세조정 모델, 평가 코드를 모두 공개하여 연구 재현성과 커뮤니티 확산 지원

## Limitation & Further Study

- **생성 품질의 의존성**: QA 생성 품질이 초기 프롬프트 설계와 LLM 선택에 크게 의존하며, 생성 후 평가 필터링만으로는 근본적인 오류 완전히 제거 불가

- **평가 지표의 주관성**: RACAR 지표 자체가 여전히 LLM(GPT-4) 기반이므로, 도메인 특수 오류나 과학적 미묘한 차이를 완전히 포착하지 못할 가능성

- **도메인 불균형**: 24개 과학 분야 간 데이터 분포가 균등하지 않을 수 있으며, 특정 분야(예: 물리, 화학)에 편중되었을 가능성

- **후속 연구**: 
  - 다양한 LLM 아키텍처(open-source vs. closed-source)에 따른 생성 품질 비교 연구
  - 인간-LLM 협업 주석(hybrid annotation) 전략 탐색
  - 과학 도메인 특화 평가 지표 개발
  - 생성된 QA의 다양성/난이도 분포 분석 및 최적화

## Evaluation

- **Novelty**: 4/5 — 자동 생성과 평가의 통합 프레임워크는 새로우나, 개별 기술(LLM 기반 생성, 자동 평가)은 기존 연구 기반

- **Technical Soundness**: 4/5 — 5차원 평가 지표의 정의와 GPT-4 기반 자동 평가의 타당성 검증(도메인 전문가 상관계수)이 체계적이나, 생성 품질의 다면적 분석이 부족

- **Significance**: 4/5 — 188K+ QA 쌍의 대규모 다학제 데이터셋 공개는 과학 NLP 커뮤니티에 실질적 기여이나, 미세조정의 성능 향상 폭이 중간 수준

- **Clarity**: 4/5 — 프레임워크의 구조와 평가 지표 정의가 명확하나, 생성 프롬프트 상세 사항이 부록에만 기재되고, 데이터셋 통계(분야별 분포)가 불충분

- **Overall**: 4/5

**총평**: SciQAG는 폐쇄형 개방형 과학 QA 자동 생성의 실질적 해결책을 제시하며, 188K 규모의 다학제 데이터셋과 신뢰성 있는 평가 프레임워크를 제공하는 점에서 가치 있는 기여이다. 다만 생성 품질 보증의 근본적 한계와 평가 지표의 LLM 의존성에 대한 추가 검증이 필요하다.

## Related Papers

- 🔗 후속 연구: [[papers/729_Scipip_An_llm-based_scientific_paper_idea_proposer/review]] — SciPIP의 아이디어 생성 결과물을 SciQAG의 질의응답 쌍 생성에 활용하여 과학 지식의 자동 구조화를 확장할 수 있다.
- 🧪 응용 사례: [[papers/835_Towards_Scientific_Intelligence_A_Survey_of_LLM-based_Scient/review]] — SciQAG의 고품질 QA 데이터가 Scientific Agent의 지식 기반 구축과 추론 능력 향상을 위한 핵심 자원으로 활용될 수 있다.
- 🏛 기반 연구: [[papers/191_Causal_learning_for_socially_responsible_ai/review]] — SciQAG의 자동 질의응답 생성 방법론이 사회적 책임 AI를 위한 인과학습 도구들의 효과를 평가하는 체계적인 질문 생성에 적용될 수 있다.
- 🔄 다른 접근: [[papers/186_Can_large_language_models_unlock_novel_scientific_research_i/review]] — SciQAG의 자동 QA 생성과 LLM의 아이디어 생성 평가가 모두 과학 문헌으로부터 자동으로 지식을 추출하지만 서로 다른 형태의 산출물을 생성한다.
- 🏛 기반 연구: [[papers/729_Scipip_An_llm-based_scientific_paper_idea_proposer/review]] — SciPIP의 과학 논문 아이디어 생성 방법론이 SciQAG의 질의응답 데이터 생성을 위한 기반 기술로 활용될 수 있다.
- 🔄 다른 접근: [[papers/186_Can_large_language_models_unlock_novel_scientific_research_i/review]] — LLM의 아이디어 생성과 과학 QA 쌍 생성이 모두 과학 문헌으로부터 지식을 자동 추출하지만 다른 형태의 결과물을 산출한다.
- 🏛 기반 연구: [[papers/191_Causal_learning_for_socially_responsible_ai/review]] — 인과학습 도구의 체계적 평가를 위해 SciQAG의 자동 질의응답 생성 방법론이 편향성과 공정성 관련 질문 생성에 활용될 수 있다.
