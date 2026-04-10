---
title: "055_Advancing_multimodal_medical_capabilities_of_gemini"
authors:
  - "Lin Yang"
  - "Shawn Xu"
  - "Andrew Sellergren"
  - "Timo Kohlberger"
  - "Yuchen Zhou"
date: "2024"
doi: "arXiv:2405.03162v1"
arxiv: ""
score: 4.0
essence: "Gemini의 멀티모달 역량을 의료 영역에 특화시킨 Med-Gemini 모델 패밀리를 개발하여, 흉부 X선(CXR) 보고서 생성, 3D CT 해석, 의료 영상 분류, 유전체 위험도 예측 등 다양한 임상 작업에서 기존 최고 성능을 초과하거나 경쟁력 있는 결과를 달성했다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/Multimodal_Scientific_Reasoning"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Yang et al._2024_Advancing multimodal medical capabilities of gemini.pdf"
---

# Advancing multimodal medical capabilities of gemini

> **저자**: Lin Yang, Shawn Xu, Andrew Sellergren, Timo Kohlberger, Yuchen Zhou, Sofia Ira Ktena, Atilla P. Kiraly, Faruk Ahmed, Farhad Hormozdiari, Tiam Jaroensri, E.-W. Wang, Ellery Wulczyn, F Guimaraes Silvio Jamil, Theo Guidroz, Chuck Lau, Siyuan Qiao, Yun Liu, Akshay Goel, Kendall Park, Arnav Agharwal | **날짜**: 2024 | **DOI**: arXiv:2405.03162v1

---

## Essence

![Figure 1](figures/fig1.webp) *Med-Gemini 모델군의 구성과 다양한 의료 작업에서의 성능 개요*

Gemini의 멀티모달 역량을 의료 영역에 특화시킨 Med-Gemini 모델 패밀리를 개발하여, 흉부 X선(CXR) 보고서 생성, 3D CT 해석, 의료 영상 분류, 유전체 위험도 예측 등 다양한 임상 작업에서 기존 최고 성능을 초과하거나 경쟁력 있는 결과를 달성했다.

## Motivation

- **Known**: 의료 AI는 주로 단일 입출력 형태의 좁은 범위 작업에 집중해왔으며, 최근 GPT-4V, LLaVA 등 대규모 멀티모달 모델(LMM)의 발전으로 복잡한 멀티모달 추론이 가능해짐
- **Gap**: 일반 목적의 LMM은 의료 영상(방사선학, 병리학, 안과학, 피부과학) 및 유전체 데이터와 같은 특화된 의료 데이터에 최적화되지 않음. 임상 적용성을 평가하는 리고러스한 벤치마킹 부족
- **Why**: 의료는 본질적으로 인간 중심이며, 정교한 멀티모달 시스템이 임상 실무에 변혁적 영향을 미칠 수 있는 분야임. 임상 유용성과 상관관계 높은 평가 지표가 필요함
- **Approach**: Gemini를 7백만 샘플(3.7백만 의료 영상/사례)로 미세조정하여 2D/3D 방사선학, 병리학, 안과학, 피부과학, 유전체 데이터에 최적화된 Med-Gemini 개발. 22개 데이터셋, 5개 작업 유형에서 자동화 지표 및 전문가 평가 수행

## Achievement

![Figure 3](figures/fig3.webp) *의료 전문가에 의한 CXR 보고서 생성 평가 결과*

1. **CXR 보고서 생성**: 정상 사례에서 57-96%, 비정상 사례에서 43-65%의 AI 생성 보고서가 원래 방사선과 의사의 보고서와 "동등 이상"으로 평가. 두 개의 독립 데이터셋에서 기존 최고 성능을 절대값 1%~12% 상회

2. **3D CT 해석**: 멀티모달 모델 기반 3D CT 부피(volume) 보고서 생성 최초 시연. 53%의 AI 보고서가 임상적으로 수용 가능하나, 전문가 품질 달성을 위해 추가 연구 필요

3. **CXR 시각 질문 응답(VQA)**: 이전 최고 성능 초과. CXR 분류 및 방사선학 VQA에서 20개 작업 중 17개에서 기존 최고 성능(SoTA) 또는 기준점 초과

4. **병리학/안과학/피부과학 분류**: 20개 작업 중 18개에서 기준점 초과, 작업별 특화 모델 성능에 접근

5. **다유전자 위험도 예측(Polygenic Risk Prediction)**: 표준 선형 다유전자 위험도 점수(PRS) 기반 접근법 초과. 학습하지 않은 유전적으로 상관된 질병으로 일반화

## How

![Figure 2](figures/fig2.webp) *조직병리학 영상 분류 성능 분석*

- **기반 모델**: Gemini의 고급 추론, 멀티모달 이해, 장문맥 처리 능력을 상속하며, 환자 표현(patient representation)과 의료 지식으로 강화

- **학습 데이터**: 7백만 샘플의 주로 자유 형식 텍스트 및 의료 데이터 쌍 활용으로 비용이 많이 드는 전문가 라벨링 회피. 공개 데이터셋(MIMIC-CXR, ChestX-ray14 등)과 자체 큐레이션 데이터셋 혼합

- **미세조정 범위**: 
  - 2D 의료 영상: 분류, VQA, 보고서 생성
  - 3D 의료 영상: CT 보고서 생성
  - 유전체: 질병 위험도 예측

- **평가 전략**: 
  - 자동화 지표(RadGraph-F1, 정확도, AUC, F1 점수) 사용
  - CXR/CT 보고서 생성과 VQA-Rad 개방형 질문에는 전문가 인간 평가
  - 8개 도메인 외 데이터셋으로 일반화 능력 평가

- **데이터셋 개선**: MIMIC-CXR 분류 라벨 수정, MIMIC-CXR VQA 질문/답변 쌍 도입, PAD-UFES-20 및 VQA-Rad의 학습-테스트 오염 제거

## Originality

- **의료 특화 멀티모달 기초 모델의 체계적 확장**: Gemini를 의료 영역에 맞춰 미세조정한 종합적 모델 패밀리로, 방사선학, 병리학, 안과학, 피부과학, 유전체 등 다양한 의료 데이터 모달리티 통합

- **3D 의료 영상 멀티모달 모델 적용 최초 시연**: 대규모 멀티모달 모델을 3D CT 부피 보고서 생성에 적용한 최초 사례

- **임상 중심의 리고러스한 평가 체계**: 자동화 지표를 넘어 임상 적용성과 직접 상관된 전문가 평가 중심의 벤치마킹으로 모델 성능의 실제 임상 가치 검증

- **공개 벤치마크 품질 개선**: 기존 데이터셋의 라벨 오류 수정, 작업 범위 확장, 데이터 누수 제거로 방법론적 엄밀성 향상

- **유전체 위험도 예측의 멀티모달 접근**: 영상 기반 작업을 넘어 비영상 의료 도메인인 다유전자 위험도 예측에 멀티모달 모델 적용하여 장기 질병 예측의 잠재력 입증

## Limitation & Further Study

- **3D CT 보고서 생성의 임상 품질 격차**: 53%의 임상적 수용 가능성은 전문가 방사선과 의사 수준(>90% 기대)에 미치지 못하며, 모델 개선과 추가 평가 필요

- **안전-중요 의료 도메인의 규제 고려**: 안전 중요 의료 분야에 필요한 임상 검증, 규제 승인, 법적 책임성 검토 부족. 실제 임상 배포 전 충분한 개발과 평가 필요

- **도메인별 특화 모델과의 성능 격차**: 피부과학, 조직병리학, 안과학 분류에서 수십 배 많은 학습 샘플을 받은 특화 모델 성능에 아직 미치지 못함

- **다양성 제한**: 주로 미국 및 인도 기반 데이터셋에 중점으로 글로벌 다양성 부족. 특정 의료 조건(예: 희귀 질환)에 대한 성능 평가 미흡

- **후속 연구 방향**:
  - 3D 의료 영상 모델의 보고서 생성 품질 개선
  - 임상 실무 워크플로우 내 배포 평가 및 운영 성능 검증
  - 다양한 인구집단과 글로벌 데이터셋으로 공정성 및 일반화 평가
  - 의료진과 협력한 인간-AI 협업 시스템 개발

## Evaluation

- **Novelty**: 4/5
  - 3D CT 멀티모달 보고서 생성 최초 시연과 유전체 위험도 예측 통합은 신선함
  - 다만 기존 Gemini의 의료 특화 미세조정이 주요 방법론으로 근본적 기술 혁신은 제한적

- **Technical Soundness**: 4/5
  - 7백만 샘플 대규모 학습, 다중 데이터셋 활용, 전문가 평가 포함으로 방법론적 엄밀함
  - 데이터 누수 제거 및 벤치마크 개선으로 신뢰성 강화
  - 3D CT 평가 샘플 수 제한(92개)과 임상 검증 부재는 약점

- **Significance**: 4.5/5
  - CXR 보고서 생성에서 임상적으로 의미 있는 성과 달성(의사와 동등 이상 43-96%)
  - 멀티모달 기초 모델의 의료 적용 가능성 광범위하게 입증
  - 3D 영상과 유전체 통합으로 의료 AI 범위 확장
  - 다만 실제 임상 배포 검증 미비로 임상적 영향 확정 어려움

- **Clarity**: 4/5
  - 전체 구조와 결과 제시 명확하고 Figure 1이 효과적으로 전체 경관 요약
  - 다양한 작업과 데이터셋이 상세히 기술되어 재현성 높음
  - 일부 기술 세부사항(정확한 미세조정 절차, 하이퍼파라미터) 부족

- **Overall**: 4/5

**총평**: Med-Gemini는 대규모 멀티모달 기초 모델의 의료 특화에 있어 종합적이고 체계적인 접근을 보여주며, 특히 CXR 보고서 생성과 다양한 의료 영상 분류 작업에서 임상적으로 의미 있는 성과를 달성했다. 3D CT 해석과 유전체 위험도 예측 통합은 의료 AI의 범위를 확장하는 중요한 시도이나, 임상 배포 검증 부재와 3D 성능 격차는 실제 임상 영향 평가의 한계로 남는다.

## Related Papers

- 🧪 응용 사례: [[papers/552_Mmsci_A_dataset_for_graduate-level_multi-discipline_multimod/review]] — Med-Gemini의 의료 멀티모달 역량이 MMSCI 데이터셋의 생명과학 분야 벤치마크 평가에 직접 적용됨
- 🔗 후속 연구: [[papers/168_Biomni_A_General-Purpose_Biomedical_AI_Agent/review]] — BiOMNI의 일반 목적 생의학 AI 에이전트가 Med-Gemini의 특화된 의료 멀티모달 능력을 더 광범위한 생의학 영역으로 확장함
- 🧪 응용 사례: [[papers/244_Cross_sectional_pilot_study_on_clinical_review_generation_us/review]] — Gemini의 다중모달 의료 능력 향상이 임상 리뷰 생성에 적용될 수 있다.
