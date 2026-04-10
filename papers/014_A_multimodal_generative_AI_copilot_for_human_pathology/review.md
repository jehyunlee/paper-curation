---
title: "014_A_multimodal_generative_AI_copilot_for_human_pathology"
authors:
  - "Ming Y. Lu"
  - "Bowen Chen"
  - "Drew F. K. Williamson"
  - "Richard J. Chen"
  - "Melissa Zhao"
date: "2024.10"
doi: "10.1038/s41586-024-07618-3"
arxiv: ""
score: 4.0
essence: "PathChat는 병리학에 특화된 시각-언어 기반 생성형 AI 어시스턴트로, 조직병리 이미지와 자연어를 모두 이해하고 복잡한 병리학 관련 질의에 답변할 수 있다."
tags:
  - "cat/Academic_Peer_Review_Automation"
  - "sub/Expert_Review_Automation"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Lu et al._2024_A multimodal generative AI copilot for human pathology.pdf"
---

# A multimodal generative AI copilot for human pathology

> **저자**: Ming Y. Lu, Bowen Chen, Drew F. K. Williamson, Richard J. Chen, Melissa Zhao, Aaron K. Chow, Kenji Ikemura, Ahrong Kim, Dimitra Pouli, Ankush Patel, Amr Soliman, Chengkuan Chen, Tong Ding, Judy J. Wang, Georg Gerber, Ivy Liang, Long Phi Le, Anil V. Parwani, Luca L. Weishaupt, Faisal Mahmood | **날짜**: 2024-10-10 | **DOI**: [10.1038/s41586-024-07618-3](https://doi.org/10.1038/s41586-024-07618-3)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1*

PathChat는 병리학에 특화된 시각-언어 기반 생성형 AI 어시스턴트로, 조직병리 이미지와 자연어를 모두 이해하고 복잡한 병리학 관련 질의에 답변할 수 있다.

## Motivation

- **Known**: 계산병리학(computational pathology)에서 작업별 예측 모델과 자기지도학습(self-supervised learning) 기반 비전 인코더가 진전을 이뤘으나, 병리학 특화 다중모달 AI 어시스턴트 개발은 미흡했다.
- **Gap**: 생성형 AI의 폭발적 성장에도 불구하고 병리학 전문 분야에 맞춤화된 일반목적의 다중모달 비전-언어 AI 어시스턴트와 코파일럿(copilot) 연구가 부족하다.
- **Why**: 병리학 분야에서 자동화된 형태학적 해석, 임상의사 결정 지원, 의료 교육 및 연구에 활용될 수 있어 임상 진단과 의료 접근성 향상에 중요하다.
- **Approach**: UNI 비전 인코더를 병리학에 맞게 적응시키고 사전학습된 Llama 2 LLM과 결합한 후, 456,000개 이상의 다양한 시각-언어 지시어(999,202개 질답)로 전체 시스템을 미세조정하여 PathChat을 구축했다.

## Achievement

![Figure 2](figures/fig2.webp)

*Figure 2*

- **다중선택 진단 문제 성능**: 다양한 조직 출처와 질병 모델의 사례에서 최첨단(SOTA) 성능 달성
- **개방형 질문 평가**: 병리학 관련 다양한 질의에 대해 더 정확하고 병리의가 선호하는 응답 생성
- **비전-언어 멀티모달 능력**: 시각과 자연언어 입력을 유연하게 처리 가능
- **응용 분야 확장**: 병리학 교육, 연구, 인간-루프 임상의사결정에서 실질적 활용 가능성 입증

## How

![Figure 1](figures/fig1.webp)

*Figure 1*

- UNI 비전 인코더: 100만 개 이상의 조직병리 이미지 패치로 자기지도학습 사전학습
- 비전-언어 사전학습: 118만 개의 병리 이미지-캡션 쌍으로 추가 학습
- 멀티모달 프로젝터: 비전 인코더를 13B 파라미터 Llama 2 LLM과 연결
- 지시어 미세조정: 456,000개 이상의 큐레이션된 지시어 데이터셋으로 학습
- 전문가 평가 벤치마크: 개방형 병리학 시각 질문-답변 데이터셋 구축 및 전문가 감수

## Originality

- 병리학 특화 다중모달 LLM 아키텍처 설계 및 구현(SOTA 비전 인코더와 LLM 결합)
- 병리학 도메인에 맞춘 규모의 시각-언어 지시어 데이터셋 구축(456,000+ 개 지시어)
- 병리 전문가 감수를 받은 고품질 개방형 질답 벤치마크 개발
- GPT-4V 등 범용 모델과의 병리학 특화 비교 평가를 통한 성능 우위 입증

## Limitation & Further Study

- 임상 실제 도입 전 대규모 임상 검증 및 규제 승인 필요
- 특정 희귀 질환이나 지역 특이적 병리학 사례에 대한 성능 제한 가능성
- 모델의 오류나 환각(hallucination) 가능성에 대한 안전장치 및 모니터링 체계 필요
- 의료 전문성이 필요한 최종 진단 결정은 반드시 병리의의 판단이 선행되어야 함
- 후속 연구: 더 다양한 병리학 특수분야 데이터 포함, 실제 임상 워크플로우 통합, 사용자 피드백 기반 지속적 개선

## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: PathChat은 병리학 분야에 특화된 최초의 실용적 다중모달 생성형 AI 어시스턴트로, 대규모 도메인 특화 데이터 구축과 체계적인 평가를 통해 높은 임상적 가치를 시연한 획기적인 연구이다.

## Related Papers

- 🔄 다른 접근: [[papers/507_Llmeval-med_A_real-world_clinical_benchmark_for_medical_llms/review]] — 의료 LLM의 임상 벤치마크 평가와 다른 접근으로 병리학 특화 멀티모달 AI 시스템을 제시한다.
- 🔗 후속 연구: [[papers/529_MedAgents_Large_Language_Models_as_Collaborators_for_Zero-sh/review]] — 제로샷 의료 진단을 위한 다중 에이전트 협업으로 PathChat의 병리학 전문 기능을 확장한다.
- 🏛 기반 연구: [[papers/168_Biomni_A_General-Purpose_Biomedical_AI_Agent/review]] — 범용 생물의학 AI 에이전트로 병리학 특화 AI 어시스턴트 개발의 기술적 기반을 제공한다.
- 🔄 다른 접근: [[papers/507_Llmeval-med_A_real-world_clinical_benchmark_for_medical_llms/review]] — 병리학 분야의 멀티모달 AI 시스템으로 의료 LLM 평가의 다른 접근 방식을 보여준다.
