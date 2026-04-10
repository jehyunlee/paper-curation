---
title: "138_Autonomous_chemical_research_with_large_language_models"
authors:
  - "Daniil A. Boiko"
  - "Robert MacKnight"
  - "Ben Kline"
  - "Gabe Gomes"
date: "2023.12"
doi: "10.1038/s41586-023-06792-0"
arxiv: ""
score: 4.3
essence: "GPT-4 기반의 다중 대형 언어 모델(LLM) 에이전트인 Coscientist는 웹 검색, 코드 실행, 실험 자동화를 통합하여 복잡한 화학 실험을 자율적으로 설계·계획·수행할 수 있는 시스템이다. 팔라듐 촉매 교차 결합 반응 최적화를 포함한 6가지 다양한 작업에서 자동화 실험 설계의 실행 가능성을 입증했다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/AI_Scientific_Discovery"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Boiko et al._2023_Autonomous chemical research with large language models.pdf"
---

# Autonomous chemical research with large language models

> **저자**: Daniil A. Boiko, Robert MacKnight, Ben Kline, Gabe Gomes | **날짜**: 2023-12-21 | **DOI**: [10.1038/s41586-023-06792-0](https://doi.org/10.1038/s41586-023-06792-0)

---

## Essence

![Figure 1](figures/fig1.webp)
*Coscientist의 시스템 아키텍처. 플래너 모듈이 중심이 되어 웹 검색, 파이썬 코드 실행, 문서 검색, 실험 자동화 모듈들을 조율한다.*

GPT-4 기반의 다중 대형 언어 모델(LLM) 에이전트인 Coscientist는 웹 검색, 코드 실행, 실험 자동화를 통합하여 복잡한 화학 실험을 자율적으로 설계·계획·수행할 수 있는 시스템이다. 팔라듐 촉매 교차 결합 반응 최적화를 포함한 6가지 다양한 작업에서 자동화 실험 설계의 실행 가능성을 입증했다.

## Motivation

- **Known**: Transformer 기반 LLM이 자연어 처리, 생물학, 화학, 프로그래밍 등 다양한 분야에서 괄목할 만한 진전을 이루고 있으며, 동시에 화학 실험 자동화 기술도 빠르게 발전하고 있음
- **Gap**: LLM의 강력한 추론 능력과 실험 자동화 기술을 결합하여 진정한 의미의 자율 과학 연구 시스템을 구축하려는 노력이 부족함
- **Why**: LLM이 과학적 프로세스에서 어느 정도의 자율성을 달성할 수 있는지, 그리고 자율 에이전트의 의사결정을 어떻게 이해할 수 있는지에 대한 근본적 질문에 답할 필요가 있음
- **Approach**: GPT-4를 중심 플래너로 하는 멀티모듈 아키텍처를 설계하여 웹 검색, 코드 실행, 문서 검색, 실험 자동화 API를 통합 연결

## Achievement

![Figure 2](figures/fig2.webp)
*다양한 LLM의 화학 합성 계획 능력 비교. GPT-4 기반 웹 검색이 다른 모델들 대비 우수한 성능을 보임.*

1. **합성 계획 능력**: 웹 검색 기능이 통합된 GPT-4 (search-gpt-4)가 아세트아미노펜, 아스피린, 니트로아닐린, 페놀프탈레인 등에서 최고 점수를 달성하며, 검색 없는 순수 LLM을 크게 능가함

2. **문서 기반 자동화**: Opentrons Python API와 Emerald Cloud Lab Symbolic Lab Language(SLL) 문서를 이용하여 로봇식 액체 핸들러 제어 및 클라우드 실험실 자동화 명령 실행 가능

3. **반자율 실험 설계**: 팔라듐 촉매 Suzuki 및 Sonogashira 교차 결합 반응 최적화를 포함한 복합 화학 작업 수행

4. **모듈식 확장성**: 6가지 다양한 작업(합성 계획, 문서 검색, 고수준 클라우드 랩 명령, 저수준 액체 핸들러 제어, 다중 하드웨어 모듈 통합, 데이터 분석 기반 최적화)에서 검증됨

## How

![Figure 3](figures/fig3.webp)
*문서 검색 시스템. Ada 임베딩을 사용한 벡터 데이터베이스 기반 문서 검색 및 요약.*

- **플래너 모듈**: GPT-4 채팅 완성 모델이 4개 명령어(GOOGLE, PYTHON, DOCUMENTATION, EXPERIMENT)를 조율하며 단계적 추론 수행

- **웹 검색 모듈**: GPT-4 기반 웹 검색 쿼리 생성 → Google Search API 호출 → 웹 페이지 브라우징 → 결과 요약 → 플래너 피드백 루프

- **코드 실행 모듈**: Docker 컨테이너에서 안전하게 Python 코드 실행, 오류 발생 시 LLM이 자동으로 코드 수정

- **문서 검색**: Ada 임베딩으로 API 문서를 벡터화하고 쿼리와의 거리 기반 검색으로 관련 문서 섹션 선택 (Transformer 기반 벡터 DB 사용)

- **실험 자동화**: EXPERIMENT 명령어가 생성된 코드를 하드웨어 API로 전달하거나 수작업 절차 제공

- **Hallucination 방지**: 웹 검색을 통해 실제 데이터로 LLM의 답변을 Grounding하여 환각 현상 감소

## Originality

- 단순한 LLM 활용이 아닌 실제 로봇 하드웨어 및 클라우드 랩 플랫폼과의 양방향 통합 달성

- 멀티모듈 에이전트 아키텍처에서 웹 검색, 문서 검색, 코드 실행을 유기적으로 결합하는 설계

- Ada 임베딩 기반 벡터 검색을 통해 기술 문서 이해 및 활용의 정확도 향상 방법 제시

- 화학 실험의 실제 구현(팔라듐 촉매 교차 결합)을 통해 자율 연구의 실용성 입증

- 플래너의 의사결정 과정이 모두 자연어로 기록되어 설명 가능성(explainability) 확보

## Limitation & Further Study

- **주요 한계**:
  - 평가 척도의 주관성 (5점 만점 중 3점 이상 모두 화학적으로 정확하지만 세부 수준에 따라 차등 평가)
  - 광범위하게 알려진 화학물질(에틸아세테이트, 벤조산)에서는 성능 저하
  - Ibuprofen 합성과 같이 복잡한 다단계 합성에서는 여전히 제한적 성능
  - 실험 오류 및 부작용 처리에 대한 구체적 기술 미흡

- **후속 연구 방향**:
  - Reaxys, SciFinder 같은 전문 반응 데이터베이스 연결로 성능 향상
  - ReAct, Chain of Thought, Tree of Thoughts 같은 고급 프롬프팅 기법 적용
  - 시스템의 이전 진술 분석을 통한 정확도 개선
  - 더 많은 화학 반응 최적화 사례 수행 및 결과 자동 분석 능력 강화
  - 안전성 및 위험 물질 취급 프로토콜 개발

## Evaluation

- **Novelty**: 4.5/5 — LLM을 실제 실험실 하드웨어 및 클라우드 플랫폼과 통합하는 방식은 혁신적이지만, 개별 기술(벡터 검색, 프롬프트 엔지니어링)은 기존 방법론의 응용

- **Technical Soundness**: 4/5 — 아키텍처 설계 및 모듈 통합이 체계적이고, 실제 실험 구현으로 검증했으나, 대규모 자동화 실험의 신뢰성 평가 데이터 부족

- **Significance**: 5/5 — 과학 자동화의 미래 방향을 제시하는 중요한 선행 사례로, 화학뿐 아니라 생물학, 재료과학 등으로 확장 가능성이 높음

- **Clarity**: 4.5/5 — 시스템 아키텍처와 개별 모듈 설명이 명확하고, Figure 활용이 우수하나, 실험 오류 처리 및 부작용 관리 절차에 대한 설명 부족

- **Overall**: 4.3/5

**총평**: 이 논문은 대형 언어 모델을 실제 화학 실험 자동화와 결합한 획기적인 사례를 제시하며, 특히 웹 검색을 통한 Hallucination 방지와 문서 검색을 통한 API 활용이 인상적이다. 다만 대규모 자동화 실험의 신뢰성, 오류 처리 능력, 그리고 현재 시스템의 한계(복잡한 다단계 합성, 주관적 평가)에 대한 더 깊은 분석이 필요하다.

## Related Papers

- 🔄 다른 접근: [[papers/096_An_automatic_end-to-end_chemical_synthesis_development_platf/review]] — LLM 기반 화학 자동화의 서로 다른 구현 범위와 접근법을 보여준다.
- 🏛 기반 연구: [[papers/684_Robot-assisted_mapping_of_chemical_reaction_hyperspaces_and/review]] — LLM 기반 화학 실험 설계가 로봇 기반 반응 매핑의 인지적 기반을 제공한다.
- 🔗 후속 연구: [[papers/213_ChemReasoner_Heuristic_Search_over_a_Large_Language_Models_K/review]] — 화학 자동화를 휴리스틱 탐색 기반 추론으로 확장한다.
- 🔗 후속 연구: [[papers/684_Robot-assisted_mapping_of_chemical_reaction_hyperspaces_and/review]] — LLM 기반 화학 자동화를 로봇 플랫폼으로 확장하여 더 체계적인 반응 매핑을 제공한다.
- 🔄 다른 접근: [[papers/096_An_automatic_end-to-end_chemical_synthesis_development_platf/review]] — LLM 기반 화학 합성 자동화의 서로 다른 구현 방식과 범위를 제시한다.
- 🔄 다른 접근: [[papers/239_CRISPR-GPT_for_agentic_automation_of_gene-editing_experiment/review]] — 화학 연구 자동화와 유전자 편집 자동화는 모두 실험실 워크플로우를 LLM으로 자동화하는 접근방식을 공유한다.
- 🧪 응용 사례: [[papers/1129_SARS-CoV-2_simulations_go_exascale_to_predict_dramatic_spike/review]] — 대규모 분자 시뮬레이션 결과를 AI 기반 자율 화학 연구 시스템에 적용하여 약물 개발을 가속화할 수 있다
