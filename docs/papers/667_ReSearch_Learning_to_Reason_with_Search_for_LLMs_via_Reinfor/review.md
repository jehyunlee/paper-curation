---
title: "667_ReSearch_Learning_to_Reason_with_Search_for_LLMs_via_Reinfor"
authors:
  - "Mingyang Chen"
  - "Tianpeng Li"
  - "Haoze Sun"
  - "Yijie Zhou"
  - "Chenzheng Zhu"
date: "2025"
doi: "10.48550/arXiv.2503.19470"
arxiv: ""
score: 4.0
essence: "ReSearch는 강화학습(RL)을 통해 대규모 언어모델(LLM)이 추론 과정 중 언제 어떻게 검색을 수행할지를 자동으로 학습하는 프레임워크이다. 감독 데이터 없이 검색 쿼리, 텍스트 기반 사고(thinking), 검색 결과를 통합한 추론 체인을 만들어 다중 홉(multi-hop) 질문 답변에서 8.9~22.4%의 성능 향상을 달성했다."
tags:
  - "cat/Reinforcement_Learning_and_Self-Verification"
  - "sub/Search-Augmented_Language_Models"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Chen et al._2025_ReSearch Learning to Reason with Search for LLMs via Reinforcement Learning.pdf"
---

# ReSearch: Learning to Reason with Search for LLMs via Reinforcement Learning

> **저자**: Mingyang Chen, Tianpeng Li, Haoze Sun, Yijie Zhou, Chenzheng Zhu | **날짜**: 2025 | **DOI**: [10.48550/arXiv.2503.19470](https://doi.org/10.48550/arXiv.2503.19470)

---

## Essence

![Figure 1](figures/fig1.webp)
*그림 1: ReSearch와 기준선(baseline) 방법들의 벤치마크 성능 비교. 모든 기준선은 Qwen2.5-32B-Instruct 기반.*

ReSearch는 강화학습(RL)을 통해 대규모 언어모델(LLM)이 추론 과정 중 언제 어떻게 검색을 수행할지를 자동으로 학습하는 프레임워크이다. 감독 데이터 없이 검색 쿼리, 텍스트 기반 사고(thinking), 검색 결과를 통합한 추론 체인을 만들어 다중 홉(multi-hop) 질문 답변에서 8.9~22.4%의 성능 향상을 달성했다.

## Motivation

- **Known**: OpenAI-o1과 DeepSeek-R1의 성공으로 LLM의 체인형 추론 능력이 증명되었고, 검색 기반 생성(RAG)도 환각(hallucination) 감소에 효과적임이 알려져 있음.
  
- **Gap**: 기존 다중 단계 RAG 방법들은 수작업으로 설계된 프롬프트나 휴리스틱에 의존하며, 추론 단계 레이블 작성이 비용과 시간 면에서 비실용적임. 현재의 강화학습 접근법은 내부 추론 능력 향상에 초점을 두고 외부 지식 검색과의 통합은 제한적으로 탐구됨.

- **Why**: 복잡한 다중 단계 문제는 여러 번의 검색이 필요하며, 언제 검색할지, 어떤 쿼리로 검색할지를 결정하는 추론 능력이 핵심이지만 이를 감독 학습으로 확보하기 어려움.

- **Approach**: 강화학습(GRPO)을 활용하여 추론(thinking), 검색 쿼리(search), 검색 결과(result)를 하나의 통합 체인으로 취급하고, 최종 답변의 정확도만으로 보상 신호를 주어 감독 데이터 없이 학습.

## Achievement

![Figure 1](figures/fig1.webp)
*그림 1: ReSearch와 기준선 방법들의 벤치마크 성능 비교*

1. **강력한 일반화 성능**: 하나의 훈련 데이터셋에서만 학습했음에도 HotpotQA(63.6%), 2Wiki(54.2%), MuSiQue(33.4%), Bamboogle(54.4%) 등 여러 벤치마크에서 일관되게 기준선 대비 8.9~22.4%의 절대 성능 향상 달성.

2. **모델 규모별 효과성**: Qwen2.5-7B와 Qwen2.5-32B 양쪽 모두에서 성공적으로 훈련되어 방법론의 확장성 입증.

3. **자동 추론 능력 도출**: 강화학습 과정에서 사전 정의된 휴리스틱 없이 반성(reflection)과 자기 수정(self-correction) 같은 고급 추론 능력이 자연스럽게 발현됨.

## How

![Figure 2](figures/fig2.webp)
*그림 2: ReSearch의 훈련 개요. (a) GRPO 파이프라인. (b) 검색을 포함한 롤아웃 생성 프로세스의 세부사항*

### 훈련 메커니즘

- **GRPO 알고리즘**: Group Relative Policy Optimization을 사용하여 별도의 비평 모델 없이 롤아웃 그룹에서 기준선을 추정하고, 정규화된 이점(normalized advantage)을 통해 정책을 최적화. KL 발산 페널티로 참조 정책으로부터의 편차를 제어.

- **검색 통합 롤아웃**: 텍스트 기반 사고에 더하여 `<search>` 태그로 쿼리를 생성하고, 검색 환경에서 결과를 획득한 후 `<result>` 태그로 감싸서 다음 생성에 활용. 이 과정이 반복되어 다중 단계 검색을 자동 조율.

- **검색 결과 마스킹**: 손실 계산 시 검색 환경에서 제공된 검색 결과 토큰은 제외하고, 모델이 생성한 사고 및 검색 쿼리 토큰만 포함하여 훈련 편향 제거.

- **프롬프트 템플릿**: 기반 모델과 명령어 조정 모델 각각을 위해 설계된 간단한 템플릿으로 특정 형식 준수를 유도. 스페셜 태그 인식을 통해 롤아웃 생성 프로세스 조율.

- **보상 설계**: 최종 답변의 F1 점수로 계산한 답변 보상(answer reward)과 형식 정확성(format reward)의 두 가지 규칙 기반 보상만 사용하여 단순성과 효과성 달성.

## Originality

- **처음의 통합 프레임워크**: 추론 과정 자체에 검색 작업을 불가분의 요소로 통합하고, 검색 시기와 방법을 추론이 주도하도록 설계한 것은 기존 RAG 연구와 구별됨.

- **감독 데이터 제거**: 추론 단계의 레이블 데이터 없이 최종 보상만으로 학습하는 접근은 실용성 측면에서 기존 방법들보다 우월함. 이는 DeepSeek-R1의 순수 추론 학습을 다중 단계 검색까지 확장.

- **검색 결과 마스킹 기법**: RL 손실 계산에서 외부에서 제공된 검색 결과를 제외하는 처리는 이론적으로 명확하고, 모델의 편향을 방지하는 정교한 설계.

- **자동 추론 능력 도출**: 사전 정의된 규칙 없이 강화학습 과정에서 반성과 자기 수정이 자동으로 발현되는 현상을 실증적으로 보여줌.

## Limitation & Further Study

- **검색 환경 의존성**: 방법론이 외부 검색 환경(Wikipedia 등)의 품질과 응답 속도에 의존하며, 검색 실패 시 모델의 행동 방식에 대한 분석 부족.

- **보상 함수의 단순성**: 현재 규칙 기반 보상(F1 점수, 형식 검사)은 단순하지만, 복잡한 추론 경로에서 희소 보상(sparse reward) 문제가 발생할 가능성 있음.

- **훈련 비용 미상**: GRPO 훈련에 필요한 계산량, 롤아웃 샘플 수, 수렴 속도 등의 상세한 훈련 비용 분석 제시 부족.

- **평가 데이터셋 제한**: 주로 영어 다중 홉 QA 벤치마크에서만 평가되었으며, 다른 추론 작업(수학, 코딩 등)이나 다국어 성능은 미지수.

- **향후 연구 방향**:
  - 더 복잡한 보상 설계나 학습 가능한 보상 모델(learned reward model) 도입
  - 검색 환경 오류 처리 및 불완전한 정보 상황에서의 대응 방안
  - 다른 도구(계산기, API 호출 등)와의 통합 확장
  - 훈련 효율성 및 샘플 효율성 개선

## Evaluation

| 항목 | 평가 |
|------|------|
| **Novelty (독창성)** | 4.5/5 |
| **Technical Soundness (기술적 건전성)** | 4/5 |
| **Significance (중요도)** | 4/5 |
| **Clarity (명확성)** | 3.5/5 |
| **Overall (종합)** | 4/5 |

**총평**: ReSearch는 추론과 검색을 통합하는 새로운 관점에서 강화학습을 적용하여 감독 데이터 없이도 다중 홉 질문 답변에서 뚜렷한 성능 개선을 달성한 실질적 가치 높은 논문이다. 다만 보상 함수의 단순성, 훈련 비용 분석 부재, 평가 데이터셋의 제한성 등으로 인해 완전성 면에서는 약간의 개선 여지가 있다.

## Related Papers

- 🔄 다른 접근: [[papers/740_Search-R1_Training_LLMs_to_Reason_and_Leverage_Search_Engine/review]] — 두 논문 모두 강화학습 기반 검색을 다루되 ReSearch는 다중홉 질문 답변, Search-R1은 검색 엔진과의 통합에 특화되어 있다.
- 🏛 기반 연구: [[papers/873_WebThinker_Empowering_Large_Reasoning_Models_with_Deep_Resea/review]] — WebThinker의 웹 탐색과 정보 수집 통합은 ReSearch의 검색 쿼리와 추론 체인 생성에 더 동적인 정보 수집 방법론을 제공한다.
- 🧪 응용 사례: [[papers/602_Paperqa_Retrieval-augmented_generative_agent_for_scientific/review]] — PaperQA의 과학 문헌 검색 증강 생성은 ReSearch의 강화학습 기반 검색 학습을 학술 문헌 도메인에 직접 적용한 실제 사례를 보여준다.
- 🔗 후속 연구: [[papers/873_WebThinker_Empowering_Large_Reasoning_Models_with_Deep_Resea/review]] — ReSearch의 강화학습 기반 검색 학습은 WebThinker의 웹 탐색 능력을 더욱 체계적이고 자동화된 방식으로 발전시킨다.
- 🔄 다른 접근: [[papers/740_Search-R1_Training_LLMs_to_Reason_and_Leverage_Search_Engine/review]] — 두 논문 모두 검색 기반 추론을 다루되 Search-R1은 검색 엔진 활용, ReSearch는 다중홉 질문 답변에 특화되어 있다.
- 🔗 후속 연구: [[papers/743_Self-critique_guided_iterative_reasoning_for_multi-hop_quest/review]] — 기본적인 추론 학습을 검색과 강화학습을 통한 더 체계적인 추론 능력 향상 방법으로 확장함
