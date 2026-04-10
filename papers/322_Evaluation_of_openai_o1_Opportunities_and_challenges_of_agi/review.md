---
title: "322_Evaluation_of_openai_o1_Opportunities_and_challenges_of_agi"
authors:
  - "Tianyang Zhong"
  - "Zheng Liu"
  - "Yi Pan"
  - "Yutong Zhang"
  - "Yifan Zhou"
date: "2024"
doi: "10.48550/arXiv.2409.18486"
arxiv: ""
score: 4.25
essence: "OpenAI의 o1-preview 대규모 언어 모델(LLM)을 다양한 복잡 추론 작업에 걸쳐 포괄적으로 평가한 결과, 컴퓨터 과학, 수학, 자연과학, 의학, 언어학, 사회과학 등 여러 영역에서 인간 수준 이상의 성능을 달성했으며, 이는 인공일반지능(AGI) 달성을 위한 중요한 진전을 시사한다."
tags:
  - "cat/AI-Powered_Scientific_Research_Frameworks"
  - "sub/AI_for_Science_Taxonomy"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Zhong et al._2024_Evaluation of openai o1 Opportunities and challenges of agi.pdf"
---

# Evaluation of openai o1: Opportunities and challenges of agi

> **저자**: Tianyang Zhong, Zheng Liu, Yi Pan, Yutong Zhang, Yifan Zhou, Shizhe Liang, Zihao Wu, Yanjun Lyu, Peng Shu, Xiaowei Yu, C. Cao, Hanqi Jiang, Hanxu Chen, Yiwei Li, Junhao Chen, Huawen Hu, Yihe Liu, Huaqin Zhao, Shaochen Xu, Haixing Dai | **날짜**: 2024 | **DOI**: [10.48550/arXiv.2409.18486](https://doi.org/10.48550/arXiv.2409.18486)

---

## Essence

OpenAI의 o1-preview 대규모 언어 모델(LLM)을 다양한 복잡 추론 작업에 걸쳐 포괄적으로 평가한 결과, 컴퓨터 과학, 수학, 자연과학, 의학, 언어학, 사회과학 등 여러 영역에서 인간 수준 이상의 성능을 달성했으며, 이는 인공일반지능(AGI) 달성을 위한 중요한 진전을 시사한다.

## Motivation

- **Known**: 기존 LLM들은 특정 도메인에서 우수한 성능을 보이지만, 복잡한 추론이 필요한 다양한 도메인의 문제들에 대한 일관된 평가가 부족했다.

- **Gap**: o1 모델의 체인-오브-사고(Chain-of-Thought) 추론과 강화학습(Reinforcement Learning)을 통한 개선사항이 실제로 어느 정도의 성능 향상을 가져오는지, 그리고 AGI로의 진전 정도를 정량적으로 평가하는 종합 벤치마크가 필요했다.

- **Why**: LLM의 빠른 발전과 실제 응용 가능성을 고려할 때, 다양한 분야에서의 능력을 체계적으로 평가함으로써 강점과 한계를 명확히 파악할 필요가 있다.

- **Approach**: 컴퓨터 과학부터 의료, 인문학까지 27개 주요 영역에서 공개 데이터셋과 도메인 전문가의 평가를 활용한 종합적인 벤치마크(AGI-Benchmark 1.0) 구축 및 실험 수행.

## Achievement

1. **코딩 및 프로그래밍**: 경쟁 프로그래밍 문제에서 83.3% 성공률 달성으로 많은 인간 전문가를 능가
   
2. **의료 분야**: 방사선학 보고서 생성에서 다른 평가 대상 모델들을 능가하는 성능, 전자건강기록(EHR) 진단 및 의료 지식 질문 답변에서 높은 정확도

3. **수학**: 고등학교 수준의 수학 경시대회 문제에서 100% 정확도 달성, 상세한 단계별 풀이 제공

4. **자연언어 처리**: 일반 및 의료 전문 영역의 자연언어 추론(Natural Language Inference)에서 우수한 성능

5. **칩 설계**: EDA(Electronic Design Automation) 스크립트 생성 및 버그 분석에서 전문화된 모델 능가

6. **인문과학**: 인류학, 지질학 등 전문 분야에서 깊이 있는 이해력과 추론 능력 입증

7. **금융**: 정량적 투자(Quantitative Investing)에서 포괄적인 금융 지식과 통계 모델링 능력 시연

8. **사회분석**: 소셜 미디어 분석, 감정 분석, 감정 인식에서 효과적인 성능

## How

- **Chain-of-Thought 추론**: 중간 추론 과정을 명시적으로 생성하여 복잡한 문제 해결 능력 강화

- **강화학습(RL) 기반 최적화**: RLHF(Reinforcement Learning from Human Feedback)를 통해 인간 선호도에 맞춘 반응 생성

- **다단계 추론**: 복잡한 문제를 단계별로 분해하여 체계적으로 해결하는 방식

- **도메인 간 지식 통합**: 여러 분야의 지식을 효과적으로 결합하여 새로운 문제 해결

- **27개 영역 벤치마크**: 공개 데이터셋(LeetCode, MedQA, ScienceQA 등)을 활용한 체계적 평가 및 도메인 전문가 검증

## Originality

- **광범위한 다중 도메인 평가**: 단순한 특정 영역 평가를 넘어 27개 주요 학문 분야를 포함한 종합적 벤치마크 구축으로 AGI 특성을 다면적으로 평가

- **AGI-Benchmark 1.0 제시**: 향후 LLM 평가를 위한 표준화된 벤치마크 프레임워크 제안

- **도메인 전문가 협업**: 의학, 칩 설계, 인류학 등 각 분야의 전문가 30명 이상이 참여한 깊이 있는 평가

- **실제 적용 가능성 검증**: 이론적 평가를 넘어 방사선학 보고서 생성, 칩 설계 등 실제 산업 응용 분야에서의 성능 검증

- **정성적·정량적 분석 병행**: 단순 정확도 통계뿐 아니라 상세한 사례 분석과 오류 분석 제시

## Limitation & Further Study

- **멀티모달 능력 부족**: 현재 텍스트 기반 평가에 중심을 두고 있으며, 시각적 정보와 결합한 멀티모달 성능 평가 필요

- **더 단순한 문제에서의 오류**: 복잡한 추론이 필요한 작업에서는 뛰어나지만, 간단한 문제에서는 때때로 실패하는 역설적 현상 설명 필요

- **높은 도메인 특화 개념의 한계**: 극도로 특화된 전문 개념에 대한 이해에서는 여전히 한계 존재

- **비용 및 계산 효율성**: 인프라 비용 및 응답 시간 고려한 실제 배포 가능성 평가 부족

- **장기 추론의 안정성**: 매우 긴 사슬의 추론이 필요한 작업에서 중간 과정의 오류 누적 가능성 미검증

- **도메인 외 일반화**: 평가에 포함되지 않은 새로운 도메인으로의 성능 전이 가능성 미실증

- **윤리적 고려사항**: 의료, 금융 등 민감한 분야에서의 실제 배포 시 윤리적 가이드라인 및 규제 필요성

## Evaluation

- **Novelty (독창성)**: 4/5
  - 광범위한 다중 도메인 평가와 AGI-Benchmark 1.0 제시는 의미 있지만, 각 영역 평가 방법 자체는 기존 방식의 조합

- **Technical Soundness (기술적 건전성)**: 4/5
  - 체계적인 평가 프로토콜과 도메인 전문가 검증이 탄탄하나, 일부 평가 지표의 객관성(예: 주관적 평가 영역) 개선 필요

- **Significance (중요성)**: 5/5
  - AGI 달성 가능성을 보여주는 중대한 실증적 증거이며, 다양한 분야의 연구자와 실무자에게 즉각적인 영향

- **Clarity (명확성)**: 4/5
  - 27개 영역에 대한 상세한 설명과 풍부한 사례 제시로 이해하기 쉽지만, 일부 통계 분석 결과 해석에 깊이 부족

- **Overall (종합)**: 4.25/5

**총평**: 본 논문은 OpenAI o1의 능력을 가장 광범위하게 평가한 첫 종합 연구로서, 다양한 분야에서 인간 수준 이상의 성능을 실증함으로써 AGI 달성에 대한 중요한 근거를 제시했으며, 제시된 AGI-Benchmark 1.0은 향후 LLM 평가의 표준이 될 수 있는 중대한 기여이다. 다만 멀티모달 통합, 도메인 외 일반화, 그리고 실제 배포 시 윤심사항 등에서 추가 연구가 필요하다.

## Related Papers

- 🏛 기반 연구: [[papers/833_Towards_reasoning_era_A_survey_of_long_chain-of-thought_for/review]] — o1의 뛰어난 성능이 Long CoT 추론 특성에서 기인한다는 이론적 근거를 제공한다
- 🔗 후속 연구: [[papers/585_Openai_o1_system_card/review]] — OpenAI o1 시스템 카드를 통해 AGI 평가 결과의 구체적 시스템 구현을 확인할 수 있다
- ⚖️ 반론/비판: [[papers/471_Large_Language_Models_Cannot_Self-Correct_Reasoning_Yet/review]] — LLM의 추론 자기교정 한계와 o1의 인간 수준 추론 성능 사이의 대조적 관점을 제시한다
- 🧪 응용 사례: [[papers/846_TrustLLM_Trustworthiness_in_Large_Language_Models/review]] — OpenAI O1 모델 평가가 신뢰성 차원에서 구체적 사례 연구가 됨
- 🔗 후속 연구: [[papers/683_RM-R1_Reward_Modeling_as_Reasoning/review]] — OpenAI o1의 추론 능력 평가는 RM-R1의 생성형 보상 모델이 실제로 달성할 수 있는 성능 상한을 보여준다.
- 🧪 응용 사례: [[papers/833_Towards_reasoning_era_A_survey_of_long_chain-of-thought_for/review]] — OpenAI o1의 뛰어난 추론 성능이 Long CoT의 특성에서 기인한다는 실증적 증거를 제공한다
- 🔄 다른 접근: [[papers/181_Can_gpt-4v_ision_serve_medical_applications_case_studies_on/review]] — OpenAI o1 AGI 평가와 GPT-4V 의료 응용의 다른 AI 역량 평가 접근법
- 🔗 후속 연구: [[papers/585_Openai_o1_system_card/review]] — OpenAI o1 평가 연구는 o1 시스템 카드의 안전성과 강건성 개선 주장을 AGI 맥락에서 기회와 도전으로 확장 분석한다.
- 🔗 후속 연구: [[papers/387_Gpt-4_technical_report/review]] — GPT-4를 기반으로 한 OpenAI o1의 추론 능력 평가 연구
- 🏛 기반 연구: [[papers/178_Can_ai_examine_novelty_of_patents_Novelty_evaluation_based_o/review]] — OpenAI o1의 평가를 통해 AGI의 기회와 도전을 분석하여 본 논문의 LLM 특허 평가 능력 연구의 기술적 배경을 제공한다.
