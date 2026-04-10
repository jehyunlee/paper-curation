---
title: "270_Detecting_llm-written_peer_reviews"
authors:
  - "Vishisht Rao"
  - "Aounon Kumar"
  - "Himabindu Lakkaraju"
  - "Nihar B. Shah"
date: "2025"
doi: "arXiv:2503.15772v2"
arxiv: ""
score: 4.2
essence: "본 논문은 동료평가(peer review) 과정에 대규모언어모델(LLM)이 부정적으로 사용되는 것을 탐지하기 위해 **간접 프롬프트 주입(indirect prompt injection)** 기법을 통해 워터마크를 삽입하고, **통계적으로 엄밀한 검증 방법**으로 LLM 생성 리뷰를 검출하는 시스템을 제안한다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/AI_Review_Detection"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Liang et al._2025_Detecting llm-written peer reviews.pdf"
---

# Detecting LLM-written Peer Reviews

> **저자**: Vishisht Rao, Aounon Kumar, Himabindu Lakkaraju, Nihar B. Shah | **날짜**: 2025 | **DOI**: [arXiv:2503.15772v2](https://arxiv.org/abs/2503.15772)

---

## Essence

본 논문은 동료평가(peer review) 과정에 대규모언어모델(LLM)이 부정적으로 사용되는 것을 탐지하기 위해 **간접 프롬프트 주입(indirect prompt injection)** 기법을 통해 워터마크를 삽입하고, **통계적으로 엄밀한 검증 방법**으로 LLM 생성 리뷰를 검출하는 시스템을 제안한다.

## Motivation

- **Known**: 
  - ICLR 2024의 15.8% 이상의 리뷰가 AI 보조로 작성됨
  - NIH, Science 등 주요 기관이 LLM 기반 리뷰 금지 정책 시행
  - GPTZero 같은 기존 탐지 도구는 완전 생성 vs. AI 보조 텍스트 구분 실패

- **Gap**: 
  - 기존 탐지 방법(stylistic analysis, term frequency)은 가정에 의존하며 형식적 통계 보장 부재
  - 대규모 리뷰 평가 시 다중검정(multiple testing) 문제로 인한 거짓양성(false positive) 위험
  - Bonferroni 같은 표준 보정법은 통계력(statistical power)을 과도하게 감소

- **Why**: 
  - 과학적 신뢰성의 핵심인 동료평가 무결성 훼손 방지 필요
  - 정책 집행 가능성 높은 실질적 탐지 기법 부재

- **Approach**: 
  - 원고 PDF에 숨겨진 지시사항 임베딩 → LLM이 처리하여 워터마크 삽입
  - 가족단위오류율(FWER) 제어 통계 검증 프레임워크 개발
  - 인간 작성 리뷰의 특성에 무관한 형식적 보장 제공

## Achievement

![Figure 1: Workflow diagram](figures/fig1.webp)
*리뷰 탐지의 3단계 프로세스: 워터마킹 → 간접 프롬프트 주입 → 통계 검증*

1. **높은 워터마크 임베딩 성공률**:
   - 가짜 인용문(fake citation) 기반 워터마킹: 평균 **98.6%** 성공률
   - 암호화 프롬프트 주입(cryptic prompt injection): **91%** 성공률
   - NSF 그랜트 제안서: 최대 **89%** 성공률
   - ChatGPT 4o, Claude 3.5 Sonnet, Gemini 2.0 Flash 등 다양한 LLM 모두 효과적

2. **방어 기법에 대한 견고성**:
   - 다른 LLM에 의한 패러프레이징 후에도 **94%** 이상 워터마크 유지
   - 10,000+ 리뷰에서 **거짓양성 0건** 달성

3. **통계적 우수성**:
   - FWER 제어 테스트가 Bonferroni/Holm-Bonferroni보다 **통계력 우수**
   - 표준 보정법은 실무상 불가능(infeasible)한 수준의 검정력 저하 반면, 제안 방법은 실용성 유지

## How

- **워터마크 설계 기준**:
  - 통계적 검증 가능성 (FWER 제어)
  - 인간 작성 리뷰 변동성으로부터 독립적 오류율
  - 안정적 임베딩 성공률
  - 인간에게 눈에 띄지 않음 (inconspicuous)
  - 패러프레이징에 강건함

- **워터마크 유형**:
  - 가짜 인용문: 임의 생성된 저자/연도 조합 (예: "Smith et al., 2089")
  - 희귀 기술용어: 저빈도 도메인 특화 표현
  - 통계 구조화: 각 리뷰마다 독립적 임의 선택

- **간접 프롬프트 주입 기법**:
  - **화이트텍스트 삽입**: 배경색과 동일 색상 텍스트로 인간에게 불가시
  - **폰트 조작**: 특정 폰트나 크기 변조로 의도된 지시 임베딩
  - **암호화 프롬프트**: 적대적 재재구성(adversarial jailbreaking) 활용하여 탐지 회피 시도 우회

- **통계 검증 방법**:
  - 귀무가설: 워터마크의 존재는 우연에 의한 일치
  - 초기하분포(hypergeometric distribution) 기반 정확한 p-값 계산
  - FWER 제어로 다중검정 문제 해결
  - 인간 작성 리뷰 사전 데이터 불필요 (가정 독립적)

## Originality

- **최초 기여**:
  - LLM 피어리뷰 탐지 목적으로 **적대적 재재구성(adversarial jailbreaking) 재목적화** (기존은 해로운 출력 생성 용도)
  - **FWER 제어 통계 프레임워크**로 형식적 보장 제공하는 워터마킹 검증 방법 최초 개발
  - 인간 작성 텍스트 특성에 무관한 **모델-독립적 통계 설계**

- **기법의 차별성**:
  - 기존 stylistic analysis와 달리 동적 인간 작성 양식 변화에 영향받지 않음
  - 확률적 워터마크 선택으로 수학적 거짓양성 확률 상한(upper bound) 도출
  - 간접 프롬프트 주입의 여러 구현 방식 비교 분석 (화이트텍스트, 폰트, 암호화 프롬프트)

- **실험의 광범위성**:
  - 6개 주요 LLM (ChatGPT, Claude, Gemini, LLaMA 등)
  - 4개 실제 리뷰 데이터셋 (ICLR 2024, PeerRead, NSF 그랜트, ICPRS 2022)
  - 10,000+ 규모 대규모 검증

## Limitation & Further Study

- **실제 배포의 윤리 문제**:
  - 원고 파일 조작에 대한 투명성 공개 필요
  - 리뷰어 동의 없는 프롬프트 주입의 프라이버시 함의
  - 거짓양성으로 인한 무고 리뷰어 피해 리스크 관리 필요

- **LLM 진화에 따른 대응**:
  - 향후 LLM이 숨겨진 지시사항을 무시하도록 학습할 가능성
  - 신규 워터마크 회피 기법 개발 시 탐지 방법 재설계 필요

- **후속 연구 방향**:
  - 조직 차원 배포 프로토콜 및 정책 프레임워크 개발
  - 다국어 리뷰 및 도메인(의학, 법학 등) 확대 적용
  - LLM 기반 리뷰의 품질 평가와 탐지 효율성 간 트레이드오프 분석
  - 리뷰어 교육을 통한 자발적 준수 강화 방안 병행

## Evaluation

- **Novelty**: 4.5/5
  - FWER 제어 통계 프레임워크와 적대적 재재구성 적용은 창신적
  - 간접 프롬프트 주입의 아이디어는 선행 사례 존재하나, 엄밀한 통계 기초는 신규

- **Technical Soundness**: 4.5/5
  - 초기하분포 기반 정확한 p-값 계산과 수학적 논증 견고함
  - 실험 설계와 대규모 검증 철저함
  - 다만 원고 파일 조작 감지 가능성에 대한 분석 부재

- **Significance**: 4/5
  - 과학적 신뢰성 보호에 직접 기여하는 시의적절한 주제
  - 실제 정책 시행(NIH, Science 금지 규정) 배경 강함
  - 조직 차원 배포의 실용성은 윤리/기술적 장애물 존재

- **Clarity**: 4/5
  - 3단계 프레임워크 명확한 설명
  - 통계 방법론 수학적으로 엄밀하나, 실무자를 위한 직관 설명 추가 필요

- **Overall**: 4.2/5

**총평**: 동료평가 무결성이라는 중요한 현안에 대해 **통계적으로 형식화된 워터마킹 검증 방법**을 최초로 제시하며, 대규모 리뷰 평가 시 다중검정 문제를 체계적으로 해결한 기여도 높은 논문이다. 다만 실제 조직 배포 시 윤리적·기술적 고려사항 및 LLM 진화에 따른 지속 가능성에 대한 심화 논의가 필요하다.

## Related Papers

- 🔄 다른 접근: [[papers/445_Is_Your_Paper_Being_Reviewed_by_an_LLM_Investigating_AI_Text/review]] — 둘 다 학술 논문에서 AI 생성 텍스트를 탐지하는 문제를 다루지만 서로 다른 기술적 접근법을 사용함
- 🔗 후속 연구: [[papers/283_Do_Users_Write_More_Insecure_Code_with_AI_Assistants/review]] — AI 도구 사용의 부정적 영향을 코딩에서 동료평가로 확장하여 학술 무결성에 대한 광범위한 우려를 다룸
- 🏛 기반 연구: [[papers/678_ReviewerGPT_An_Exploratory_Study_on_Using_Large_Language_Mod/review]] — 동료평가에서 LLM 사용 가능성에 대한 탐색적 연구가 LLM 작성 리뷰 탐지 시스템 개발의 배경을 제공함
- 🔄 다른 접근: [[papers/104_Are_we_there_yet_revealing_the_risks_of_utilizing_large_lang/review]] — LLM이 작성한 피어 리뷰를 탐지하는 기술로 LLM 기반 리뷰 시스템의 보안 취약점을 보완할 수 있다.
- 🔗 후속 연구: [[papers/679_Revieweval_An_evaluation_framework_for_ai-generated_reviews/review]] — LLM이 작성한 피어 리뷰 탐지 기술을 활용하여 ReviewAgent의 자체 개선 루프에 검증 단계를 추가할 수 있다.
- 🔄 다른 접근: [[papers/852_Understanding_fine-grained_distortions_in_reports_of_scienti/review]] — 과학 논문의 왜곡 문제를 LLM이 생성한 리뷰 탐지 관점에서 접근하여 상호 보완적인 연구 방향을 제시한다.
- 🔄 다른 접근: [[papers/611_People_who_frequently_use_ChatGPT_for_writing_tasks_are_accu/review]] — ChatGPT 사용자의 탐지 능력과 LLM 작성 동료 검토 자동 탐지라는 서로 다른 AI 생성 텍스트 식별 접근법입니다.
- 🔗 후속 연구: [[papers/283_Do_Users_Write_More_Insecure_Code_with_AI_Assistants/review]] — AI 도구가 코딩 보안에 미치는 부정적 영향이 학술 동료평가 무결성으로 확장되는 유사한 우려사항임
- 🔗 후속 연구: [[papers/022_A_sentiment_consolidation_framework_for_meta-review_generati/review]] — 동료평가의 감정 통합을 AI 생성 리뷰 탐지와 결합하여 더 포괄적인 동료평가 품질 관리 방법을 제시함
- 🔗 후속 연구: [[papers/051_Admissions_in_the_age_of_AI_detecting_AI-generated_applicati/review]] — 동료 심사 리뷰에서 LLM으로 작성된 텍스트를 탐지하는 연구로 본 논문의 탐지 방법론을 학술 분야로 확장한다.
- 🏛 기반 연구: [[papers/445_Is_Your_Paper_Being_Reviewed_by_an_LLM_Investigating_AI_Text/review]] — LLM 작성 피어 리뷰 탐지의 기본 연구가 AI 텍스트 탐지 가능성 조사의 이론적 기반을 제공합니다.
