---
title: "776_Streamlining_the_review_process_Ai-generated_annotations_in"
authors:
  - "Óscar Díaz"
  - "Xabier Garmendia"
  - "Juanan Pereira"
date: "2024"
doi: "DOI"
arxiv: ""
score: 3.5
essence: "본 논문은 대규모 언어모델(LLM)을 학술 논문 심사 과정에 통합하되, AI가 전체 심사를 대체하는 것이 아니라 **manuscript annotation(원고 주석 달기)**이라는 특정 작업을 지원하는 방식을 제안한다. AnnotateGPT 플랫폼을 통해 AI와 인간 심사자의 협력을 위한 중간지점으로서 annotation의 역할을 검증한다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Expert_Review_Annotation"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Díaz et al._2024_Streamlining the review process Ai-generated annotations in research manuscripts.pdf"
---

# Streamlining the review process: AI-generated annotations in research manuscripts

> **저자**: Óscar Díaz, Xabier Garmendia, Juanan Pereira | **날짜**: 2024 | **DOI**: [DOI 미제공](https://arxiv.org/abs/2412.00281)

---

## Essence

![Figure 1](figures/fig1.webp)
*Fig. 1: 리뷰 보고서 및 그 UML 개념화*

본 논문은 대규모 언어모델(LLM)을 학술 논문 심사 과정에 통합하되, AI가 전체 심사를 대체하는 것이 아니라 **manuscript annotation(원고 주석 달기)**이라는 특정 작업을 지원하는 방식을 제안한다. AnnotateGPT 플랫폼을 통해 AI와 인간 심사자의 협력을 위한 중간지점으로서 annotation의 역할을 검증한다.

## Motivation

- **Known**: 연간 1,500만 시간 이상이 manuscript 심사에 소비되며, 심사자 1인당 평균 14개의 manuscript를 심사(각 5시간 소요). LLM은 aspect coverage와 informativeness 측면에서 인간 심사자를 능가할 수 있음.

- **Gap**: 기존 AI 기반 심사 시스템들은 자동화(automation)에 중점을 두어 인간의 판단을 완전히 대체하려 하지만, LLM 생성 심사 보고서는 고수준의 분석, 비판적 사고, 질문과 탐구 능력이 부족함. 또한 윤리적 문제 야기.

- **Why**: 심사의 효율성 증대와 실효성 유지 사이의 균형을 맞추면서도 윤리적 우려를 해결하기 위해서는 AI가 인간을 보강(augmentation)하는 역할이 필요함.

- **Approach**: annotation을 심사 프로세스의 전단계로 위치시켜, LLM이 중요한 구절을 미리 강조함으로써 심사자의 집중력을 향상시키고 가독성을 개선하는 방식 도입.

## Achievement

![Figure 2](figures/fig2.webp)
*Fig. 2: Annotation 생성 프로세스*

![Figure 3](figures/fig3.webp)
*Fig. 3: Annotation 중심 프롬프팅*

1. **Annotation 기반 AI-인간 협력 모델 제시**: 기존 '자동화(AI for automation)' 패러다임에서 벗어나 '보강(AI for augmentation)' 접근방식을 구현. 이는 심사자가 원고를 읽기 전에 LLM이 생성한 annotation을 통해 중요 부분을 미리 파악하게 함.

2. **AnnotateGPT 플랫폼 개발**: GPT-4를 활용한 전용 manuscript review 플랫폼을 구현하여 proof-of-concept 제공. 심사 기준별로 color-coding된 annotation을 지원하여 맥락화(contextualization)를 구현.

3. **구조화된 심사 프레임워크**: Review → CriterionReview → Annotation의 계층적 구조를 UML로 정의하여, 구체성(specificity), 맥락화(contextualization), 시의성(timeliness)을 만족하는 심사 구조를 제안.

## How

![Figure 4](figures/fig4.webp)
*Fig. 4: CriterionReview를 위한 다양한 관점*

- **Annotation 생성 단계**: LLM이 심사 기준(originality, rigor, relevance 등)에 따라 원고의 관련 구절을 자동 식별 및 하이라이트. 각 기준별로 서로 다른 색상으로 구분.

- **Criterion-driven Review 프로세스**: 심사자가 annotation된 원고를 기반으로 각 기준별로 원고의 충족도를 평가하는 반복적 과정 수행. 원고와 심사 기준 간의 부합도를 점진적으로 검토.

- **피드백 통합**: 교육학의 constructive feedback 원칙(Nicol의 10가지 권장사항 중 3가지 채택)을 심사 프로세스에 적용:
  - 맥락화: 심사 기준 명시, 긍정/부정 피드백 균형
  - 구체성: 원고의 특정 구절에 기반한 피드백
  - 시의성(성능성): reviewer의 처리 속도 및 집중력 향상

- **Platform 기능**: 
  - Annotation 시각화: color-coded highlights로 criteria 구분
  - Annotation-centric prompting: 수집된 annotation을 기반으로 criterion review 생성
  - 다중 관점 지원: 동일 annotation을 여러 criteria 관점에서 평가

## Originality

- **AI for augmentation vs. automation의 선택**: 기존 대부분의 연구가 AI의 자동화 능력에 초점을 맞춘 반면, 본 연구는 인간과 AI의 협력을 명시적으로 설계하는 점에서 차별화.

- **Annotation을 중간지점으로 정의**: 심사 프로세스에서 annotation이 갖는 역할을 체계적으로 분석하고, 이를 AI-인간 협력의 '적절한 중간지점(middle ground)'으로 제시하는 새로운 관점.

- **교육학 이론의 적용**: 학생 과제 피드백 원칙(Nicol)을 학술 peer review에 적응시켜, 구체성, 맥락화, 시의성의 세 가지 차원으로 심사 프로세스를 재구성.

- **구조화된 프레임워크**: Review-CriterionReview-Annotation의 계층적 UML 모델을 통해 annotation 기반 심사를 형식화.

## Limitation & Further Study

- **제한된 평가 규모**: TAM(Technology Acceptance Model) 설문조사 참여자가 9명으로 매우 소수. 통계적 신뢰성이 낮으며, 결과의 일반화 가능성이 제한적.

- **LLM 성능 검증 부재**: 논문의 제시된 부분(첫 15,000자)에서는 AnnotateGPT의 annotation 정확도, 재현율, 정밀도 등의 정량적 평가 결과가 불명확함. GPT-4가 실제로 어떤 품질의 annotation을 생성하는지에 대한 구체적 증거 부족.

- **인간 심사자 연구 부재**: 실제 심사자들이 annotation된 원고를 사용했을 때 심사 시간, 심사 품질, 원고 리딩 패턴 등이 어떻게 변하는지에 대한 실증적 데이터 부족.

- **다양한 분야 검증 필요**: 논문에서 제시된 부분에서는 특정 분야(NLP, ML 등)의 특수성을 고려한 평가가 제시되지 않음.

- **후속 연구 방향**:
  - 더 큰 규모의 사용자 연구(n>50) 수행
  - 다양한 학문 분야(humanities, social sciences 등)에서의 annotation 성능 비교
  - 심사 시간 단축, 심사 품질 향상 등의 객관적 지표 측정
  - 다양한 LLM(Claude, Gemini 등)과의 비교 연구
  - 심사자가 LLM annotation을 무비판적으로 수용하는 'automation bias' 발생 가능성 검증

## Evaluation

- **Novelty**: 4/5
  - AI-human collaboration의 중간지점으로 annotation을 명시적으로 제시하는 새로운 관점 제공
  - 기존 자동화 중심 연구와의 명확한 차별성
  - 다만 annotation 개념 자체는 새로운 것이 아니며, LLM 활용도 기존 연구들과 유사

- **Technical Soundness**: 3/5
  - UML 모델을 통한 체계적 프레임워크 설계는 견고함
  - 교육학 이론의 적용은 적절하나, 실제 구현 및 평가 부분이 논문의 제시된 범위에서 미흡
  - LLM annotation의 정확도, recall 등 핵심 기술 지표가 명확히 제시되지 않음

- **Significance**: 3/5
  - Peer review 시스템의 현실적 과제(reviewer burden)를 다루는 중요한 주제
  - AI for augmentation 관점의 확산은 학술 커뮤니티에 의의 있음
  - 다만 9명의 제한된 평가로는 영향력 검증이 부족하며, 실제 저널 심사 프로세스에 적용 가능성 미지수

- **Clarity**: 4/5
  - 동기와 접근방식이 명확하게 설명됨
  - 관련 연구와의 위치 설정이 체계적
  - 다만 완전한 평가 결과와 구현 세부사항이 제시 범위를 벗어남

- **Overall**: 3.5/5

**총평**: 학술 심사에서 LLM을 보강(augmentation) 도구로 활용하는 새로운 패러다임을 제시하고, annotation을 중심으로 AI-인간 협력의 설계를 체계화한 점은 의미 있으나, 소규모 사용자 평가(n=9)와 제한된 기술 검증으로 인해 학술적 임팩트와 실용성 입증이 미흡한 상태.

## Related Papers

- 🔄 다른 접근: [[papers/080_AI_is_transforming_peer_review__and_many_scientists_are_worr/review]] — AI가 전체 심사를 대체하는 것에 대한 우려를 주석 달기라는 협력적 접근으로 완화한다
- 🏛 기반 연구: [[papers/809_Three_AI-powered_steps_to_faster_smarter_peer_review/review]] — AI 보조 동료평가의 구체적 구현 방법으로 효율적 워크플로우의 기초를 제공한다
- 🔗 후속 연구: [[papers/1087_Gpt4_is_slightly_helpful_for_peer-review_assistance_A_pilot/review]] — GPT-4의 동료평가 보조 역할을 원고 주석이라는 구체적 작업으로 특화한다
- 🔗 후속 연구: [[papers/809_Three_AI-powered_steps_to_faster_smarter_peer_review/review]] — AI 주석 달기를 포함한 더 포괄적인 동료평가 워크플로우로 확장한다
- 🔗 후속 연구: [[papers/609_Peerarg_Argumentative_peer_review_with_llms/review]] — AI 주석 달기를 포함한 더 체계적이고 논리적인 동료평가 시스템으로 확장한다
