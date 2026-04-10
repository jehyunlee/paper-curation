---
title: "262_Deepreview_Improving_llm-based_paper_review_with_human-like"
authors:
  - "Minjun Zhu"
  - "Yixuan Weng"
  - "Linyi Yang"
  - "Yue Zhang"
date: "2025"
doi: "arXiv:2503.08569v1"
arxiv: ""
score: 4.2
essence: "본 논문은 LLM(Large Language Models)을 이용한 학술지 논문 심사를 개선하기 위해, 인간 전문가의 심사 과정을 모방하는 다단계 구조화된 프레임워크 DeepReview를 제안한다. DeepReview-13K 데이터셋으로 훈련된 DeepReviewer-14B 모델은 기존 모델들(CycleReviewer-70B, GPT-o1, DeepSeek-R1)을 능가하면서도 더 적은 토큰을 사용한다."
tags:
  - "cat/Academic_Peer_Review_Automation"
  - "sub/AI_Peer_Review"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Zhu et al._2025_Deepreview Improving llm-based paper review with human-like deep thinking process.pdf"
---

# DeepReview: Improving LLM-based Paper Review with Human-like Deep Thinking Process

> **저자**: Minjun Zhu, Yixuan Weng, Linyi Yang, Yue Zhang | **날짜**: 2025 | **DOI**: [arXiv:2503.08569v1](https://arxiv.org/abs/2503.08569)

---

## Essence

본 논문은 LLM(Large Language Models)을 이용한 학술지 논문 심사를 개선하기 위해, 인간 전문가의 심사 과정을 모방하는 다단계 구조화된 프레임워크 DeepReview를 제안한다. DeepReview-13K 데이터셋으로 훈련된 DeepReviewer-14B 모델은 기존 모델들(CycleReviewer-70B, GPT-o1, DeepSeek-R1)을 능가하면서도 더 적은 토큰을 사용한다.

## Motivation

- **Known**: 최근 LLM이 자동화된 논문 심사 시스템에 점차 활용되고 있으며, AI-Scientist, AgentReview, CycleReviewer 등의 접근법이 개발되었다.

- **Gap**: 기존 LLM 기반 심사 시스템들은 (1) 구조화된 세밀한 추론 과정을 학습할 수 있는 데이터셋 부족, (2) 논문의 복잡한 과학적 내용 평가에 필요한 도메인 지식 제한, (3) 근거 없는 환각(hallucination) 생성, (4) 천편일률적이고 실행 불가능한 피드백 제공 등의 문제를 가지고 있다.

- **Why**: 견고한 피드백은 과학 발전과 동료 심사의 무결성(integrity)을 위해 필수적이나, 현존 시스템은 신뢰성 있는 평가 프레임워크 개발에 실패하고 있다.

- **Approach**: (1) 신규성 검증(Novelty Verification), (2) 다차원 평가(Multi-dimensional Review), (3) 신뢰성 검증(Reliability Verification)을 통합한 구조화된 다단계 심사 프레임워크 개발, (2) 검색-랭킹, 자체 검증, 자체 성찰을 포함한 종합적 데이터 합성 파이프라인 구축, (3) 세밀한 심사 추론 체인을 담은 DeepReview-13K 데이터셋 구성.

## Achievement

![Figure 1: DeepReviewer의 개요. (a) 실제 연구논문 입력 예시, (b) 신규성 검증, 다차원 리뷰, 신뢰성 검증을 포함한 다단계 추론 과정 출력, (c) Fast/Standard/Best 세 가지 추론 모드](figures/fig1.webp)

1. **정량적 성능 개선**: 
   - Rating MSE: CycleReviewer-70B 대비 44.80% 향상
   - Ranking (Spearman 상관계수): 6.04% 향상
   - Selection (정확도): 1.80% 향상
   - LLM-as-a-judge 평가에서 GPT-o1 및 DeepSeek-R1 대비 각각 88.21%, 80.20%의 승률 달성

2. **안정성 강화**: 명시적 견고성(robustness) 훈련 없이도 적대적 공격(adversarial attack)에 대한 높은 저항성 입증

3. **효율성**: 14B 모델이 70B 모델(CycleReviewer)을 능가하며, 더 적은 토큰 소비로 성능 개선

4. **Test-Time Scaling**: 추론 경로(reasoning path)와 응답 길이 조정을 통해 성능 향상 가능성 입증

## How

![Figure 1에서 (c) 섹션: Fast/Standard/Best 모드의 다양한 추론 경로](figures/fig1.webp)

**데이터셋 구성 (DeepReview-13K)**:
- OpenReview 플랫폼과 arXiv에서 ICLR 2024-2025 총 18,976개 논문 수집
- 각 논문마다 3개 리뷰어의 평가(Strengths, Weaknesses, Questions), 반박 토론, 표준화된 점수(1-10 전체 평가 + Soundness/Presentation/Contribution 각 1-4), 메타 리뷰 및 최종 결정 정보 수집
- 최종 13,378개 유효 샘플로 구성

**다단계 심사 프레임워크**:
- **신규성 검증**: 관련 선행 연구 파악 및 논문의 혁신성 평가
- **다차원 리뷰**: 방법론 검증, 실험 검증, 종합적 분석을 통해 다면적 평가 수행
- **신뢰성 검증**: 약점 진술에 대한 증거 수집 및 분석으로 주장의 타당성 확보
- **메타 리뷰 및 최종 평가**: 여러 리뷰어의 평가를 종합하여 최종 평점 및 결정 도출

**추론 모드**:
- **Fast 모드**: 신속한 평가 필요 시 사용
- **Standard 모드**: 균형잡힌 효율성과 품질 제공
- **Best 모드**: 최고 품질의 심화된 분석 제공

**평가 방법론**:
- **정량적 평가**: MAE, MSE, 정확도, F1 (평점 예측), Spearman 상관계수 (순위), 정확도 (쌍별 선택)
- **정성적 평가**: Gemini-2.0-Flash-Thinking을 판정자(judge)로 활용한 LLM-as-a-judge 패러다임

## Originality

- **구조화된 추론 프레임워크**: 기존 end-to-end 생성 접근법과 달리, 신규성-다차원 평가-신뢰성 검증의 명시적 단계를 통해 전문가 심사 과정을 체계적으로 모방

- **세밀한 추론 체인 데이터셋**: 최종 심사 결과뿐 아니라 중간 추론 단계를 포함한 DeepReview-13K는 기존 집계된 리뷰만 제공하는 오픈 데이터셋과 차별화

- **Test-Time Scaling 활용**: 추론 경로와 응답 길이 조정을 통한 성능 향상은 최근 O1/DeepSeek-R1의 test-time compute scaling 개념을 학술 심사 영역에 처음 적용

- **종합 벤치마크**: 정량 평가(3가지 과제) + 정성 평가(LLM-as-a-judge)를 통합한 DeepReview-Bench는 기존 ROUGE/BLEU 같은 단순 텍스트 유사도 지표를 넘어선 심화된 평가 방식 제시

- **다중 모드 제공**: Fast/Standard/Best 세 가지 추론 모드는 사용자의 효율성-품질 트레이드오프 선택을 가능하게 함

## Limitation & Further Study

- **도메인 전문성의 한계**: LLM 기반 시스템은 특정 분야의 깊은 전문 지식이 필요한 평가(예: 실험 설계의 기술적 타당성, 수학적 증명의 정확성)에서 여전히 인간 전문가에 미치지 못할 수 있다.

- **검색 의존성**: 신규성 검증 및 신뢰성 검증 단계에서 관련 문헌 검색의 품질과 완전성이 최종 결과에 크게 영향을 미칠 수 있으나, 검색 시스템의 한계가 미처 다루어지지 않음.

- **평가 편향**: LLM-as-a-judge 패러다임에서 판정자로 사용되는 Gemini-2.0-Flash-Thinking의 가능한 편향성이 정성적 평가 결과에 미칠 영향에 대한 분석 부재.

- **실제 심사 환경 적용**: 학습 데이터로 사용된 ICLR 논문 중심의 학습이 다른 분야 및 학술지의 심사에 얼마나 일반화되는지 검증 필요.

- **후속 연구 방향**:
  - (1) 다양한 학문 분야의 심사 데이터 확대를 통한 교차 분야 일반화 성능 검증
  - (2) 인간 심사자와의 협력 시나리오에서 상호작용 방식 최적화
  - (3) 구조화된 피드백의 실제 저자 만족도 및 논문 개선 효과에 대한 실증 연구
  - (4) 적대적 공격 유형의 다양화 및 더욱 심화된 견고성 평가

## Evaluation

- **Novelty (독창성)**: 4.5/5
  - 구조화된 다단계 프레임워크와 세밀한 추론 체인 데이터셋은 참신하며, test-time scaling의 학술 심사 적용도 새로움. 다만 개별 구성 요소(검색, 자체 검증, 자체 성찰)는 기존 기법의 조합.

- **Technical Soundness (기술적 건전성)**: 4/5
  - 데이터 수집, 모델 훈련, 평가 방법론이 체계적이고 실험 설계가 합리적. 다만 검색 시스템의 세부 사항, 하이퍼파라미터 선택 근거, 데이터 품질 관리 프로세스 등에 대한 기술적 깊이가 다소 부족.

- **Significance (중요성)**: 4.5/5
  - 논문 심사의 자동화는 과학 커뮤니티의 중요한 과제이며, 실제 ICLR 2025에 적용될 예정. 공개 모델, 데이터셋, 코드 제공으로 재현성과 후속 연구 촉진에 기여할 것으로 기대. 다만 여전히 인간 심사자 보조 도구 역할에 제한.

- **Clarity (명확성)**: 4/5
  - 전체 구조와 주요 성과가 명확히 제시되었으나, 다단계 추론의 상세한 구현 방식(특히 각 단계 간 정보 흐름), 모드별 상세 기술, 검색 랭킹 방법 등이 본문에서는 충분히 설명되지 않아 부록 참조 필요.

- **Overall (종합)**: 4.2/5

**총평**: DeepReview는 LLM 기반 논문 심사 시스템의 신뢰성과 효율성을 크게 향상시키는 구조화된 접근법을 제시하며, 대규모 공개 데이터셋과 모델을 통해 학술 커뮤니티에 즉시적 기여를 한다. 다만 다양한 학문 분야로의 일반화, 인간-AI 협력 효과의 실증적 검증, 기술적 세부 사항의 더욱 충실한 설명이 후속 과제로 남아있다.

## Related Papers

- 🔄 다른 접근: [[papers/679_Revieweval_An_evaluation_framework_for_ai-generated_reviews/review]] — AI 생성 리뷰의 평가 프레임워크와 함께 LLM 기반 리뷰 시스템의 품질 향상을 위한 상호 보완적 접근이다.
- 🔗 후속 연구: [[papers/608_Peer_Review_as_A_Multi-Turn_and_Long-Context_Dialogue_with_R/review]] — 다중턴 대화 기반 피어 리뷰를 인간과 같은 심층 사고로 개선하여 더 정교한 리뷰 생성이 가능하다.
- 🏛 기반 연구: [[papers/242_CRITIC_Large_Language_Models_Can_Self-Correct_with_Tool-Inte/review]] — 도구 통합 기반 자기교정 기법으로 DeepReview의 다단계 구조화 프레임워크의 이론적 기반을 제공한다.
- 🔄 다른 접근: [[papers/608_Peer_Review_as_A_Multi-Turn_and_Long-Context_Dialogue_with_R/review]] — 인간과 같은 심층 사고를 통한 LLM 리뷰 개선과 함께 피어 리뷰의 다양한 개선 방향을 제시한다.
- 🔄 다른 접근: [[papers/679_Revieweval_An_evaluation_framework_for_ai-generated_reviews/review]] — LLM 기반 리뷰 개선을 위한 구조화된 프레임워크와 함께 AI 리뷰 시스템의 품질과 신뢰성을 종합적으로 향상시킨다.
- 🏛 기반 연구: [[papers/739_Seagraph_Unveiling_the_whole_story_of_paper_review_comments/review]] — 인간과 유사한 리뷰 생성 방법론이 SEAGraph의 의미론적 분석에 기초 이론을 제공한다.
- 🏛 기반 연구: [[papers/537_Mind_the_blind_spots_A_focus-level_evaluation_framework_for/review]] — DeepReview의 인간 유사 논문 리뷰 개선 방법은 포커스 레벨 평가 프레임워크의 이론적 기반을 제공합니다
- 🔗 후속 연구: [[papers/654_Re_2_A_consistency-ensured_dataset_for_full-stage_peer_revie/review]] — 인간다운 논문 리뷰 개선 방법이 Re2 데이터셋을 활용한 리뷰 품질 향상으로 확장될 수 있습니다.
- 🔗 후속 연구: [[papers/070_Agentreview_Exploring_peer_review_dynamics_with_llm_agents/review]] — 기본적인 LLM 리뷰 생성을 사회적 요인과 편향을 고려한 복잡한 시뮬레이션으로 발전시킨다.
- 🔗 후속 연구: [[papers/1094_Towards_a_Medical_AI_Scientist/review]] — 의료 AI 과학자는 DeepReview의 인간 유사 논문 리뷰 기법을 확장하여 임상 연구 전체 과정의 자동화까지 포괄하는 의료 특화 AI 연구자를 구현합니다.
- 🔗 후속 연구: [[papers/698_Scaling_Reproducibility_An_AI-Assisted_Workflow_for_Large-Sc/review]] — 인간 유사 논문 리뷰를 위한 DeepReview는 재현성 연구의 AI 워크플로우를 논문 품질 평가까지 확장한다.
- 🔗 후속 연구: [[papers/083_AI-Driven_Review_Systems_Evaluating_LLMs_in_Scalable_and_Bia/review]] — DeepReview의 인간형 검토 개선 방법이 AI-Driven Review Systems의 편향 인식 메커니즘과 결합되어 더 정교한 자동 검토 시스템을 구성할 수 있음
- 🔗 후속 연구: [[papers/665_Remor_Automated_peer_review_generation_with_llm_reasoning_an/review]] — 인간과 유사한 논문 리뷰를 추론 능력과 다목적 최적화로 확장하여 더 균형잡힌 심사평 생성이 가능하다.
