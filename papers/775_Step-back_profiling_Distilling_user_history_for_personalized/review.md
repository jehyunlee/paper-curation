---
title: "775_Step-back_profiling_Distilling_user_history_for_personalized"
authors:
  - "Xiangru Tang"
  - "Xingyao Zhang"
  - "Yanjun Shao"
  - "Jie Wu"
  - "Yilun Zhao"
date: "2024"
doi: "arXiv:2406.14275"
arxiv: ""
score: 4.0
essence: "본 논문은 사용자 이력(user history)을 간결한 프로필로 증류(distill)하여 LLM을 개인화하는 **STEP-BACK PROFILING** 기법을 제안한다. 특히 다중 저자 과학 논문 작성이라는 현실적 시나리오에서 협업 글쓰기를 지원하기 위해 개발되었다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Academic_Writing_Personalization"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Tang et al._2024_Step-back profiling Distilling user history for personalized scientific writing.pdf"
---

# Step-back profiling: Distilling user history for personalized scientific writing

> **저자**: Xiangru Tang, Xingyao Zhang, Yanjun Shao, Jie Wu, Yilun Zhao, Arman Cohan, Ming Gong, Dongmei Zhang, Mark Gerstein | **날짜**: 2024 | **DOI**: [arXiv:2406.14275](https://arxiv.org/abs/2406.14275)

---

## Essence

![Figure 1](figures/fig1.webp)
*그림 1: STEP-BACK PROFILING 개요. 각 사용자의 과거 논문을 압축하여 프로필 표현을 생성하고, 이를 LLM 생성 과정에 증강하는 방식*

본 논문은 사용자 이력(user history)을 간결한 프로필로 증류(distill)하여 LLM을 개인화하는 **STEP-BACK PROFILING** 기법을 제안한다. 특히 다중 저자 과학 논문 작성이라는 현실적 시나리오에서 협업 글쓰기를 지원하기 위해 개발되었다.

## Motivation

- **Known**: 
  - 기존 LLM 개인화 연구는 단일 사용자 맥락에 초점을 맞춤
  - 검색 증강(retrieval-augmented) 방식은 원본 사용자 데이터의 비압축 형태를 사용
  - 컨텍스트 길이 제한으로 인해 광대한 사용자 이력 활용이 비현실적

- **Gap**: 
  - 현대 과학 출판은 수십~수백 명의 저자가 협업하는 경우가 증가 중
  - 다중 저자 협업 시나리오에서 모델의 성능 평가 벤치마크 부재
  - 개별 저자의 전문성과 다양한 글쓰기 스타일을 동시에 모델링하는 방법 부족

- **Why**: 
  - 메모리 제약을 고려하면서도 핵심 사용자 특성만 추출 필요
  - 팀 과학(team science) 시대의 협업 연구 효율화 요구
  - LLM 기반 개인화 시스템의 실질적 적용성 향상

- **Approach**: 
  - 사용자 이력을 고수준 개념과 언어 특성으로 압축하는 프로필 생성
  - 다중 사용자 프로필의 순차적 연결(concatenation)
  - 새로운 **Personalized Scientific Writing (PSW)** 벤치마크 구축

## Achievement

![Figure 2](figures/fig2.webp)
*그림 2: LaMP 벤치마크에서 STEP-BACK PROFILING의 성능. 대부분의 LaMP 작업에서 우수한 성능 달성*

1. **LaMP 벤치마크 개선**: 기존 방법 대비 최대 3.6점 성능 향상 달성 (7개 개인화 작업)

2. **다중 저자 협업 글쓰기 검증**: PSW 데이터셋을 통해 협업 논문 작성에서 사용자 특성 포착의 효과성 입증

3. **프로필 기반 생성의 우월성**: 원본 이력 직접 사용보다 추상화된 프로필 사용이 더 효율적임을 실증

4. **확장성 확보**: 제한된 컨텍스트 길이 내에서 더 많은 사용자 정보 활용 가능

## How

![Figure 1](figures/fig1.webp)
*STEP-BACK PROFILING의 4단계 절차*

**절차 구성**:

- **User Profile Gisting**: LLM을 이용하여 각 사용자의 이력 Hi를 짧은 "gist" 표현으로 응축 (Gist(·) 함수)
  - 사용자의 고수준 특성(traits)과 관심사(interests) 캡처

- **Multi-User Profile Concatenation**: 개별 프로필 Pu1, Pu2, ..., Pun을 순서 민감적으로 결합하여 통합 표현 PU 생성

- **Retrieval-Augmented Generation (선택사항)**: 입력 x에 대해 각 저자의 이력에서 관련 스니펫 상위-k개 검색
  - 증강된 입력: x̃ = [x; R1,k; R2,k; ...; Rn,k]

- **Personalized Output Generation**: LLM이 증강 입력(또는 원본 입력)과 연결된 프로필 PU로 조건지어 개인화된 출력 생성
  - y = Generate(x̃, PU)

**PSW 벤치마크 설계**:

- **UP-0**: Research Interest Generation (저자 프로필 구축)
- **PSW-1**: Research Topic Generation (공동 연구 주제)
- **PSW-2**: Research Question Generation (연구 질문)
- **PSW-3**: Paper Abstract Generation (논문 요약)
- **PSW-4**: Paper Title Generation (논문 제목)

**평가 방식**: GPT-4-turbo 기반 체인-오브-씽크(chain-of-thought) 프롬프팅으로 일관성, 유창성, 관련성, 참신성 평가

## Originality

- **다중 저자 개인화의 체계적 제안**: 단일 사용자 중심 기존 연구에서 벗어나 협업 시나리오로 확장

- **프로필 증류 개념의 신규성**: 원본 이력의 비효율적 직접 사용 대신 LLM 기반 추상화 방식 도입

- **PSW 벤치마크의 현실성**: 실제 과학 논문 저자 구성과 이력을 기반으로 한 현실적 평가 데이터셋

- **훈련 없는 개인화(training-free) 접근**: 사전 학습된 LLM만으로 구현 가능한 실용성

- **다중 저자 순서 민감성 분석**: 저자 순서가 모델 성능에 미치는 영향 실증적 검증

## Limitation & Further Study

- **프로필 생성의 품질 의존성**: Gist(·) 함수의 성능에 전체 시스템이 의존하며, 저품질 프로필 생성 시 하류 작업 악화 가능

- **다중 저자 상호작용 모델링 부족**: 현재 방식은 프로필의 단순 연결로, 저자 간 협업 역학관계(dynamics)를 명시적으로 모델링하지 않음

- **평가 방식의 한계**: GPT-4 기반 자동 평가가 사용되었으나, 실제 인간 평가와의 일관성 검증 필요

- **저자 이력의 길이 제약**: 수십 년 경력의 저자는 방대한 논문 이력을 가지므로, 실제 프로필 생성 시 정보 손실 가능

- **후속 연구 방향**:
  - 저자 간 협업 패턴을 명시적으로 모델링하는 구조적 프로필 표현 개발
  - 인간 평가 기반 검증 및 도메인 전문가 평가 추가
  - 장기 저자 이력 처리를 위한 계층적 프로필 추상화 연구
  - 다국어 과학 논문으로 확장된 평가


## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 논문은 협업 과학 글쓰기라는 현실적 문제를 정의하고, 사용자 이력의 효율적 압축을 통한 LLM 개인화 방법을 제시한 점에서 기여도가 높다. 다만 저자 간 상호작용의 명시적 모델링과 인간 평가 기반 검증이 강화되면 더욱 설득력 있는 연구가 될 수 있다.

## Related Papers

- 🔗 후속 연구: [[papers/613_Personalized_graph-based_retrieval_for_large_language_models/review]] — 사용자 이력 증류 기법이 개인화된 그래프 기반 검색에서 효율적인 사용자 프로필 생성을 위한 핵심 전처리 방법론으로 활용된다.
- 🏛 기반 연구: [[papers/886_Wordcraft_A_human-ai_collaborative_editor_for_story_writing/review]] — 인간-AI 협업 글쓰기의 기본 개념이 다중 저자 과학 논문 작성이라는 복잡한 협업 시나리오로 확장되어 개인화 기법을 통해 구현된다.
- 🔄 다른 접근: [[papers/889_Xtragpt_Llms_for_human-ai_collaboration_on_controllable_acad/review]] — 사용자 이력 기반 개인화와 제어 가능한 맥락 인식 수정은 모두 개인화된 학술 글쓰기 지원을 목표로 하지만 서로 다른 개인화 전략을 사용한다.
- 🏛 기반 연구: [[papers/613_Personalized_graph-based_retrieval_for_large_language_models/review]] — 사용자 이력 증류 기법이 개인화된 그래프 기반 검색에서 콜드스타트 문제 해결을 위한 핵심 전처리 방법론으로 활용된다.
- 🔗 후속 연구: [[papers/886_Wordcraft_A_human-ai_collaborative_editor_for_story_writing/review]] — 인간-AI 협업 글쓰기를 다중 저자 과학 논문 작성으로 확장하여 개인화된 사용자 프로필 기반의 협업 지원이 가능하다.
- 🔄 다른 접근: [[papers/889_Xtragpt_Llms_for_human-ai_collaboration_on_controllable_acad/review]] — 맥락 인식 제어 가능한 수정과 사용자 이력 기반 개인화는 모두 개인화된 학술 글쓰기를 지원하지만 서로 다른 개인화 메커니즘을 사용한다.
