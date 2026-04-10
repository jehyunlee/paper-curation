---
title: "678_ReviewerGPT_An_Exploratory_Study_on_Using_Large_Language_Mod"
authors:
  - "Ryan Liu"
  - "Nihar B. Shah"
date: "2023.06"
doi: "10.48550/arXiv.2306.00622"
arxiv: ""
score: 4.0
essence: "급속도로 발전하는 대규모 언어 모델(LLM)이 과학 논문 심사 과정에서 검토자를 보조할 수 있는지 실증적으로 평가한 연구로, GPT-4가 특정 작업에서는 유망하지만 완전한 논문 평가는 아직 불가능함을 보여준다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/LLM_Review_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Liu and Shah_2023_ReviewerGPT An Exploratory Study on Using Large Language Models for Paper Reviewing.pdf"
---

# ReviewerGPT? An Exploratory Study on Using Large Language Models for Paper Reviewing

> **저자**: Ryan Liu, Nihar B. Shah | **날짜**: 2023-06-01 | **DOI**: [10.48550/arXiv.2306.00622](https://doi.org/10.48550/arXiv.2306.00622)

---

## Essence

급속도로 발전하는 대규모 언어 모델(LLM)이 과학 논문 심사 과정에서 검토자를 보조할 수 있는지 실증적으로 평가한 연구로, GPT-4가 특정 작업에서는 유망하지만 완전한 논문 평가는 아직 불가능함을 보여준다.

## Motivation

- **Known**: LLM들은 다양한 분야에서 뛰어난 성능을 보이고 있으며, 과학 심사 과정은 투고 증가와 검토자 과부하로 심각하게 압박받고 있음
- **Gap**: LLM이 논문 심사의 어느 부분에서 실질적으로 유용한지, 어떤 작업은 가능하고 어떤 작업은 불가능한지에 대한 체계적인 평가 부재
- **Why**: 전 세계 연구자들이 심사에 투자하는 막대한 시간 비용(수백만 시간)과 인간 검토자도 오류 있는 논문을 놓치는 문제(30-40% 정도)를 해결할 필요
- **Approach**: 세 가지 구체적인 심사 작업(오류 탐지, 체크리스트 검증, 논문 비교)을 설계하여 GPT-4의 성능을 정량적으로 평가

## Achievement

1. **오류 탐지 능력**: 의도적으로 오류를 삽입한 13개의 단편 논문 중 7개(53.8%)에서 오류 탐지 성공. 이는 인간 검토자의 오류 탐지율과 비슷한 수준으로, 수학적 오류와 개념적 오류 모두 포함
   
2. **체크리스트 검증**: NeurIPS 2022의 15개 논문에서 119개의 {체크리스트 질문, 논문} 쌍에 대해 86.6% 정확도 달성. 저자의 응답과도 동일한 86.6% 일치율을 보였으며, 50%의 LLM 오류는 논문의 텍스트로 판단 불가능한 질문(예: 그림의 정보 필요)에서 발생

3. **논문 비교 선택의 한계**: 명확하게 우월한 초록으로 구성된 10개 쌍 중 6개(60%)에서 실패. 편향된 결과 해석, 매개변수 범위 오독, 통계 경계값 오해, 프롬프트 인젝션 공격에 취약, 과장된 표현에 영향을 받는 등의 문제 확인

## How

- **모델 선택**: 파일럿 스터디를 통해 Bard, Vicuna, Koala, Alpaca, LLaMa, Dolly, OpenAssistant, StableLM 등 8개 모델과 비교한 결과 GPT-4만이 오류 탐지 가능
  
- **프롬프팅 전략**: 단순히 "리뷰를 작성하라"는 요청보다 "오류를 찾아라"와 같은 구체적인 질문을 포함한 타겟 프롬프트가 훨씬 효과적
  
- **오류 탐지 실험**: 3가지 프롬프트 변형(Direct, One-Shot, Few-Shot) 사용하여 단계별 추론(step-by-step reasoning) 활용
  
- **체크리스트 검증**: 저자가 "예"로 답변한 항목들을 수동으로 라벨링하고 관련 논문 섹션과 함께 제시하여 3회 응답의 다수결로 최종 판단
  
- **비교 평가**: 동일한 초록에 추가 결과를 포함, 유행어/과장 표현 삽입 등 의도적인 변수 조작

## Originality

- LLM을 논문 심사의 구체적인 세부 작업으로 나누어 평가한 최초의 체계적 연구
- 오류가 의도적으로 삽입된 13개의 단편 논문 데이터셋과 119개의 체크리스트 {질문, 논문} 쌍 레이블링된 데이터셋 공개
- 프롬프팅 전략에 따른 성능 차이를 정량적으로 입증
- LLM의 약점(선택적 평가, 요약 평가)을 체계적으로 드러낸 실증 분석

## Limitation & Further Study

- **데이터 규모 제한**: 오류 탐지 13개, 비교 평가 10개 쌍으로 통계적 일반화 어려움
- **모델 범위**: GPT-4만 심도 있게 평가하여 다른 최신 모델(Claude 등)과의 비교 부재
- **도메인 한정**: 컴퓨터 과학 분야에만 초점, 다른 학문 분야의 적용 가능성 미지수
- **평가 기준의 주관성**: "우월한 초록" 설계가 다소 인위적일 수 있으며, 실제 피어 리뷰의 복잡성 미반영
- **후속 연구**: (1) 더 큰 규모의 데이터셋으로 신뢰도 향상, (2) 인간 검토자와의 직접 비교, (3) Chain-of-Thought 등 고급 프롬프팅 기법 적용, (4) 여러 모델의 앙상블 활용, (5) 특정 분야별 미세조정(fine-tuning) 가능성

## Evaluation

- **Novelty**: 4/5 - LLM을 구체적인 심사 작업으로 분해하여 평가한 점은 새로우나, 단편적 실험 설계
- **Technical Soundness**: 3.5/5 - 방법론은 명확하지만 샘플 크기가 작고, 일부 비교 평가의 설계가 인위적
- **Significance**: 4/5 - 심사 자동화의 가능성과 한계를 명확히 제시하여 정책 및 향후 연구에 영향력 있음
- **Clarity**: 4.5/5 - 명확한 구조와 결과 제시, 다만 일부 실험 세부사항(인간 라벨링 프로토콜, ICC 등) 부족
- **Overall**: 4/5

**총평**: 급부상하는 LLM의 논문 심사 활용 가능성을 최초로 체계적으로 탐색한 중요한 연구로, GPT-4가 오류 탐지와 체크리스트 검증에서는 유망하지만 완전한 평가는 아직 불가능함을 실증했다. 다만 소규모 실험 데이터셋과 제한된 모델 비교가 일반화 가능성을 다소 제약한다.

## Related Papers

- 🔗 후속 연구: [[papers/680_Reviewing_scientific_papers_for_critical_problems_with_reaso/review]] — LLM의 논문 심사 가능성 탐색을 비판적 문제 검출이라는 특화된 영역으로 확장하여 더 구체적인 적용 방안을 제시한다.
- 🏛 기반 연구: [[papers/665_Remor_Automated_peer_review_generation_with_llm_reasoning_an/review]] — LLM 논문 심사의 기초적 실증 연구가 추론 기능을 갖춘 고급 자동 심사 시스템 개발의 가능성과 한계를 보여주는 출발점이 된다.
- ⚖️ 반론/비판: [[papers/104_Are_we_there_yet_revealing_the_risks_of_utilizing_large_lang/review]] — LLM 논문 심사의 가능성 탐구와 대규모 언어 모델 활용의 위험성 분석을 통해 AI 심사 도입의 신중한 접근 필요성을 확인할 수 있다.
- 🔗 후속 연구: [[papers/104_Are_we_there_yet_revealing_the_risks_of_utilizing_large_lang/review]] — LLM을 피어 리뷰에 활용하는 탐색적 연구로, 본 논문이 밝힌 보안 위험에 대한 실증적 배경을 제공한다.
- 🧪 응용 사례: [[papers/128_Automatically_evaluating_the_paper_reviewing_capability_of_l/review]] — LLM 기반 피어 리뷰 탐색의 구체적 실증 연구 사례
- 🧪 응용 사례: [[papers/664_RelevAI-Reviewer_A_Benchmark_on_AI_Reviewers_for_Survey_Pape/review]] — LLM을 활용한 탐색적 논문 검토 연구가 AI 리뷰어의 실제 구현과 평가 방안을 제시한다.
- 🏛 기반 연구: [[papers/270_Detecting_llm-written_peer_reviews/review]] — 동료평가에서 LLM 사용 가능성에 대한 탐색적 연구가 LLM 작성 리뷰 탐지 시스템 개발의 배경을 제공함
- 🔗 후속 연구: [[papers/127_Automatic_evaluation_metrics_for_artificially_generated_scie/review]] — 논문 심사에서 대규모 언어 모델 사용에 대한 탐색적 연구로 본 논문의 평가 지표를 실제 심사 환경에 적용한다.
- 🔗 후속 연구: [[papers/445_Is_Your_Paper_Being_Reviewed_by_an_LLM_Investigating_AI_Text/review]] — 학술 리뷰에서 LLM 사용 탐색을 AI 텍스트 탐지 방법론 개발로 확장하여 더 정확한 식별 기술을 제시합니다.
- 🏛 기반 연구: [[papers/665_Remor_Automated_peer_review_generation_with_llm_reasoning_an/review]] — LLM의 논문 심사 가능성에 대한 탐색적 연구가 고급 추론 기능을 갖춘 자동 심사 시스템 개발의 기초적인 실증 근거를 제공한다.
- 🏛 기반 연구: [[papers/680_Reviewing_scientific_papers_for_critical_problems_with_reaso/review]] — LLM의 일반적 논문 심사 능력 탐색이 비판적 문제 검출이라는 특화된 심사 업무 수행 가능성 평가의 기초가 된다.
