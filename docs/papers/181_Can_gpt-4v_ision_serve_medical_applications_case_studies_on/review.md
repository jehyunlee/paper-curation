---
title: "181_Can_gpt-4v_ision_serve_medical_applications_case_studies_on"
authors:
  - "Chaoyi Wu"
  - "Jiayu Lei"
  - "Qiaoyu Zheng"
  - "Weike Zhao"
  - "Weixiong Lin"
date: "2023"
doi: "arXiv:2310.09909"
arxiv: ""
score: 4.0
essence: "본 논문은 OpenAI의 GPT-4V(ision) 모델이 의료 영상 진단 작업에서 실제로 임상 적용 가능한지를 체계적으로 평가한 연구이다. 17개 신체 시스템과 8개 영상 모달리티를 포함한 광범위한 사례 연구를 통해 GPT-4V의 의료 진단 능력과 한계를 명확히 규명했다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/Multimodal_Scientific_Reasoning"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Xu and Tao_2023_Can gpt-4v (ision) serve medical applications case studies on gpt-4v for multimodal medical diagnos.pdf"
---

# Can gpt-4v (ision) serve medical applications? case studies on gpt-4v for multimodal medical diagnosis

> **저자**: Chaoyi Wu, Jiayu Lei, Qiaoyu Zheng, Weike Zhao, Weixiong Lin, Xiaoman Zhang, Xiao Zhou, Ziheng Zhao, Ya Zhang, Yanfeng Wang, Weidi Xie | **날짜**: 2023 | **DOI**: [arXiv:2310.09909](https://arxiv.org/abs/2310.09909)

---

## Essence

![Figure 1](figures/fig1.webp)
*의료 시스템 17개와 영상 모달리티 8개를 포괄하는 평가 프레임워크*

본 논문은 OpenAI의 GPT-4V(ision) 모델이 의료 영상 진단 작업에서 실제로 임상 적용 가능한지를 체계적으로 평가한 연구이다. 17개 신체 시스템과 8개 영상 모달리티를 포함한 광범위한 사례 연구를 통해 GPT-4V의 의료 진단 능력과 한계를 명확히 규명했다.

## Motivation

- **Known**: 최근 대규모 기초 모델(Large Foundation Models)의 발전으로 생성형 AI가 큰 주목을 받고 있으며, 의료 분야 적용 가능성에 대한 기대가 높아지고 있음
- **Gap**: GPT-4V와 같은 멀티모달 대규모 언어 모델이 실제 의료 영상 진단에서 어느 정도 성능을 발휘하는지에 대한 체계적인 평가가 부족함
- **Why**: 의료는 환자 안전이 최우선이므로, 실제 임상 도입 전에 현재 생성형 AI 모델의 정확한 능력과 한계를 파악할 필요가 있음
- **Approach**: 중추신경계(CNS), 심장, 흉부, 종양학 등 17개 신체 시스템에 대해 X-ray, CT, MRI, PET, DSA, 유방촬영술, 초음파, 병리 등 8개 모달리티의 의료 영상을 활용하여 GPT-4V를 다각도로 평가

## Achievement

![Figure 2](figures/fig2.webp)
*GPT-4V의 단일 뇌 MRI 영상 분석 사례*

1. **영상 모달리티 및 해부학적 구조 인식 우수**: GPT-4V는 의료 영상의 촬영 방식(X-ray, CT, MRI 등)과 신체 부위를 정확하게 식별할 수 있으며, 이 분야에서는 상대적으로 높은 성능을 보임

2. **질병 진단에서 심각한 한계**: 정확한 질병 진단 능력이 현저히 부족하며, 특히 드문 질환이나 복잡한 임상 소견의 경우 오진 또는 관련 없는 답변을 생성함

3. **보고서 생성 시 구조화된 형식은 가능하지만 내용 정확성 부족**: 임상 리포트 형식을 적절히 작성하지만 실제 의료 정보의 정확성과 완전성이 부족함

4. **다중 영상 분석의 어려움**: 동일 모달리티의 여러 영상(다양한 각도의 뷰)이나 서로 다른 모달리티의 영상을 통합 분석하는 데 significant challenges를 보임

5. **환자 병력에 대한 과도한 의존성**: 환자의 의료 기록이 제공되면 답변이 크게 달라지며, 이는 모델이 영상 정보보다 텍스트 정보에 더 큰 가중치를 두는 경향을 시사함

## How

![Figure 3](figures/fig3.webp)
*해부학적 구조 및 이상 소견 위치 파악 평가 사례*

- **사례 선정**: 17개 신체 시스템별로 실제 임상 사례 수집 및 다양한 질환 포함
- **영상 처리**: 원본 의료 영상을 GPT-4V 입력 형식에 맞게 전처리
- **질문 프롬프트**: 의료 모달리티 인식, 해부학적 구조 인식, 질병 진단, 리포트 생성, 병변 위치 파악 등 다양한 임상 작업에 맞춘 프롬프트 설계
- **검증 방법**: 전문가 주석(annotation)과 참고 캡션(reference caption)을 이용한 정성적 평가
- **다중 라운드 상호작용**: 모델의 답변 변경 가능성과 hallucination 문제 검증
- **환자 병력 조건**: 환자 의료 기록 유무에 따른 성능 차이 분석

## Originality

- **포괄적 의료 도메인 커버리**: 17개 신체 시스템과 8개 영상 모달리티를 모두 포함한 최초의 체계적 평가
- **다양한 임상 작업 평가**: 단순 분류를 넘어 진단, 리포트 생성, 위치 파악, 다중 영상 분석 등 실제 임상 워크플로우를 반영한 평가
- **신뢰성 문제 심층 분석**: Hallucination, 일관성 부족, 성능 변동성 등 의료 적용에 치명적인 문제들을 구체적으로 규명
- **병리학 영상 포함**: 기존 의료 AI 연구에서 종종 간과되는 병리학적 영상 분석도 포함
- **공개 리소스**: 모든 평가 사례 이미지를 공개하여 재현성과 추가 연구 가능성 확보

## Limitation & Further Study

- **한계**:
  - 정성적 평가 중심으로 대규모 정량적 메트릭이 부재
  - 평가 사례 수가 제한적일 수 있어 통계적 신뢰도 측면에서 일반화의 한계
  - GPT-4V의 특정 버전만 평가하였으므로 향후 버전 업데이트 시 결과 변경 가능
  - 의료진의 주관적 평가에 의존하는 부분이 존재
  - 패턴 인식보다는 논리적 추론이 필요한 복잡한 임상 추론 능력의 평가 부족

- **향후 연구 방향**:
  - 더 대규모의 정량적 평가 지표 개발 및 적용
  - 다른 대규모 멀티모달 모델들(Claude Vision, Gemini 등)과의 비교 연구
  - 특정 의료 영역에 특화된 파인튜닝(fine-tuning)의 효과 검증
  - Hallucination 문제 해결을 위한 개선 방안 연구
  - 의료 전문가와의 협력을 통한 하이브리드 진단 시스템 개발
  - 임상 안전성 검증 표준 개발


## Evaluation

- Novelty: 4/5
- Technical Soundness: 3.5/5
- Significance: 4.5/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 논문은 급속히 발전하는 생성형 AI의 의료 적용 가능성에 대한 현실적이고 체계적인 평가를 제공함으로써 과도한 기대감을 조절하고 진정한 의료 AI의 발전 방향을 제시하는 중요한 기여를 한다. 특히 광범위한 의료 도메인 커버리지와 다양한 임상 작업 평가는 높이 평가되지만, 대규모 정량적 메트릭 부재와 평가 사례 수의 제한은 향후 개선이 필요한 부분이다.

## Related Papers

- 🧪 응용 사례: [[papers/727_Scimage_How_good_are_multimodal_large_language_models_at_sci/review]] — 과학 이미지에서 다중모달 LLM 성능 평가를 의료 영상 진단에 적용
- 🔄 다른 접근: [[papers/322_Evaluation_of_openai_o1_Opportunities_and_challenges_of_agi/review]] — OpenAI o1 AGI 평가와 GPT-4V 의료 응용의 다른 AI 역량 평가 접근법
- 🏛 기반 연구: [[papers/388_GPT-4o_System_Card/review]] — GPT-4o 시스템 카드가 GPT-4V 의료 응용의 기술적 기반 제공
- 🏛 기반 연구: [[papers/097_An_autonomous_AI_agent_for_universal_behavior_analysis/review]] — BehaveAgent의 멀티모달 행동 분석은 GPT-4V의 의료 응용 연구에서 검증된 비전-언어 모델의 시각적 추론 능력을 동물 행동학 영역으로 확장한 것입니다.
