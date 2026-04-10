---
title: "722_Scifibench_Benchmarking_large_multimodal_models_for_scientif"
authors:
  - "Jonathan C. Roberts"
  - "Kai Han"
  - "Neil Houlsby"
  - "Samuel Albanie"
date: "2024"
doi: "N/A"
arxiv: ""
score: 4.25
essence: "대규모 멀티모달 모델(LMM)의 과학 논문 그림 해석 능력을 평가하기 위한 벤치마크 SciFIBench를 제시하며, 2000개의 고품질 문제와 28개 모델의 종합 평가를 통해 현재 LMM의 과학 분야 적용 가능성을 체계적으로 검증한 연구이다."
tags:
  - "cat/Scientific_Language_Processing_and_Visualization"
  - "sub/Multimodal_Scientific_Benchmarks"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Roberts et al._2024_Scifibench Benchmarking large multimodal models for scientific figure interpretation.pdf"
---

# SciFIBench: Benchmarking Large Multimodal Models for Scientific Figure Interpretation

> **저자**: Jonathan C. Roberts, Kai Han, Neil Houlsby, Samuel Albanie | **날짜**: 2024 | **DOI**: N/A

---

## Essence

대규모 멀티모달 모델(LMM)의 과학 논문 그림 해석 능력을 평가하기 위한 벤치마크 SciFIBench를 제시하며, 2000개의 고품질 문제와 28개 모델의 종합 평가를 통해 현재 LMM의 과학 분야 적용 가능성을 체계적으로 검증한 연구이다.

## Motivation

- **Known**: GPT-4V, Gemini 등 최신 LMM은 다양한 분야(의료, 금융, 수학)에서 우수한 일반화 성능을 보이고 있으며, 과학 연구 보조 도구로 활용될 가능성이 높음
- **Gap**: 과학 논문의 핵심인 복잡한 그림 해석 능력에 대해 정량적 평가 벤치마크가 부재하며, 현재 모델들의 과학 그림 이해 능력이 명확히 특성화되지 않음
- **Why**: 과학 이미지는 고밀도의 의미론적 정보와 도메인 특화 표현을 포함하고 있어 일반 이미지 벤치마크로는 평가 불가능하며, 전문 지식이 필요한 ground truth 구성의 어려움
- **Approach**: arXiv 논문의 그림-캡션 쌍을 다중선택 문제로 변환하고, 적대적 필터링(adversarial filtering)과 인간 검증을 통해 고품질 문제 집합 구성

## Achievement

![Figure 1: SciFIBench 개요. 왼쪽: arXiv 논문에서 추출한 2000개의 다중선택형 과학 그림 해석 문제. 오른쪽: 28개 LMM 평가 프레임워크](figures/fig1.webp)

1. **벤치마크 구축**: arXiv에서 추출한 94k(CS) + 102k(일반) 그림-캡션 쌍으로부터 8개 범주의 2000개 고품질 문제 생성. 모든 문제에 대해 인간 검증 수행하여 응답 가능성 보장

2. **포괄적 평가**: GPT-4o, Gemini 1.5를 포함한 28개 LMM 평가로 현재 최고 성능 모델도 인간 기준선에 미치지 못함을 확인. 적대적 필터링이 문제 난이도 유의미하게 증가

3. **충실성 분석**: LLM(Gemini-Pro)을 활용한 자동 평가 방법 개발 및 모델의 추론 일관성(reasoning faithfulness) 프로빙 실시

## How

![Figure 2: SciFIBench 문제의 그림 크기 및 캡션 길이 분포](figures/fig2.webp)

**문제 구성 방법론**:

- **임베딩 기반 선택**: CLIP 기반 비전-언어 모델로 그림-캡션 쌍의 결합 임베딩(2048차원) 생성
- **벡터 데이터베이스 구축**: Faiss를 이용하여 임베딩 벡터 데이터베이스 구성
- **적대적 필터링**: 각 질문에 대해 k-최근접이웃(k-NN)에서 유클리드 거리 기반으로 유사도 높은 오답 선택지 선택 및 유사도 역치 이하의 중복 제거
- **난이도 기반 샘플링**: 오답 선택지들의 평균 거리를 난이도 지표로 사용하여 어려운 문제 우선 샘플링
- **인간 검증**: 각 범주별로 가장 어려운 문제들에 대해 도메인 전문가가 "응답 가능성" 검증

**작업 정의**:
- Figure→Caption: 주어진 그림에 대해 5개 캡션 중 정답 선택
- Caption→Figure: 주어진 캡션에 대해 5개 그림 중 정답 선택

## Originality

- **차별성**: 기존의 ChartQA, FigureQA 등 차트 특화 벤치마크와 달리 일반 과학 논문의 다양한 그림 유형 포함. 정량적 LMM 평가에 초점으로 기존 정성적 분석 연구와 구별
- **방법론**: arXiv 메타데이터를 활용한 자동화된 고품질 문제 생성 파이프라인 및 강력한 LLM을 평가기로 활용하는 창의적 자동 평가 방식
- **규모**: 2000개 문제 규모로 충분한 통계적 신뢰도 확보 및 커뮤니티 활용성 극대화
- **다중 평가 관점**: 단순 정확도를 넘어 추론 충실성(reasoning faithfulness)과 지시 따르기(instruction-following) 능력 프로빙

## Limitation & Further Study

- **데이터 편향**: arXiv CS 및 특정 범주에 집중된 데이터로 인한 도메인 편향 가능성. 다양한 과학 분야 확대 필요
- **선택지 크기 고정**: 모든 문제를 5개 선택지로 제한하여 실제 응용의 다양한 상황 반영 부족
- **자동 평가 신뢰성**: Gemini-Pro의 평가 정확도 검증 부족. 모델 편향이 평가에 영향 미칠 가능성
- **인간 기준선**: 전문가 1인 검증으로 인한 잠재적 주관성. 다중 평가자 합의 방식 도입 필요
- **후속 연구 방향**: 
  - 의료, 물리학 등 다양 분야 데이터 추가
  - Few-shot 학습 및 체인-오브-생각(chain-of-thought) 프롬프팅 효과 분석
  - 미세 조정(fine-tuning) 가능성 탐색
  - 그림 내 특정 요소(축, 범례 등) 해석 능력에 대한 세분화된 분석

## Evaluation

- **Novelty**: 4/5 - 과학 그림 이해 정량 평가라는 명확한 공백 메움. 다만 LMM 벤치마크 자체는 증가하는 추세
- **Technical Soundness**: 4/5 - 적대적 필터링과 인간 검증의 체계적 적용. 자동 평가 방식은 검증 부족
- **Significance**: 5/5 - 과학 AI 분야의 중요한 평가 도구 제공. 28개 모델 평가로 포괄성 우수. 공개 릴리스로 높은 커뮤니티 가치
- **Clarity**: 4/5 - 방법론 및 결과 명확히 제시. 일부 기술적 세부사항 보완 필요
- **Overall**: 4.25/5

**총평**: SciFIBench는 과학 분야의 LMM 능력 평가에 필수적인 벤치마크로서, 체계적인 문제 구성 방법론과 포괄적 평가를 통해 현재 모델의 한계를 명확히 드러낸다. 공개 릴리스와 다양한 분석을 통해 학계의 중요한 기여이나, 도메인 확대 및 평가 방식의 추가 검증이 향후 과제이다.

## Related Papers

- 🔄 다른 접근: [[papers/204_Chartx__chartvlm_A_versatile_benchmark_and_foundation_model/review]] — 차트 이해에 특화된 ChartX와 달리 전반적인 과학 논문 그림 해석 능력을 평가하는 포괄적 벤치마크
- 🔗 후속 연구: [[papers/197_Chartcoder_Advancing_multimodal_large_language_model_for_cha/review]] — 차트를 코드로 변환하는 ChartCoder의 기능을 과학 논문 그림 전반으로 확장한 평가 연구
- 🧪 응용 사례: [[papers/336_FigCaps-HF_A_Figure-to-Caption_Generative_Framework_and_Benc/review]] — 과학 그림 캡션 생성 모델의 성능을 체계적으로 평가할 수 있는 벤치마크 제공
- 🏛 기반 연구: [[papers/551_MMC_Advancing_Multimodal_Chart_Understanding_with_Large-scal/review]] — 대규모 차트 이해 데이터셋 MMC의 방법론을 과학 논문 그림으로 확장한 기반
- 🧪 응용 사례: [[papers/201_ChartLlama_A_Multimodal_LLM_for_Chart_Understanding_and_Gene/review]] — 차트 이해 전용 멀티모달 모델의 방법론이 과학 그림 전반을 다루는 대형 멀티모달 모델 벤치마킹에 핵심적으로 적용된다
- 🔗 후속 연구: [[papers/091_Aiscivision_A_framework_for_specializing_large_multimodal_mo/review]] — 과학적 수치 이해를 위한 대규모 다중모달 모델 벤치마킹으로 과학 영상 분류를 확장한다.
- 🧪 응용 사례: [[papers/627_Position_Multimodal_large_language_models_can_significantly/review]] — 과학 도표 이해를 위한 대형 멀티모달 모델 벤치마킹이 과학적 추론 향상의 실제적 평가 기준을 제공한다.
- 🏛 기반 연구: [[papers/142_AutoNumerics_An_Autonomous_PDE-Agnostic_Multi-Agent_Pipeline/review]] — AutoNumerics의 PDE 해석 자동화는 SciFIBench의 과학적 그림 이해 벤치마크에서 검증된 멀티모달 과학적 추론 능력을 수치해석 영역에 적용합니다.
- 🧪 응용 사례: [[papers/369_Gemini_a_family_of_highly_capable_multimodal_models/review]] — Gemini의 멀티모달 능력을 과학 분야 특화 벤치마크로 평가하는 연구
- 🧪 응용 사례: [[papers/551_MMC_Advancing_Multimodal_Chart_Understanding_with_Large-scal/review]] — MMC의 차트 이해 기술을 과학 분야 특화 멀티모달 벤치마크로 확장
- 🏛 기반 연구: [[papers/204_Chartx__chartvlm_A_versatile_benchmark_and_foundation_model/review]] — 과학 그림 해석 벤치마크 SciFIBench의 방법론을 차트 특화 영역에 적용한 기반
- 🔗 후속 연구: [[papers/435_Interfeedback_Unveiling_interactive_intelligence_of_large_mu/review]] — 정적 과학 그림 해석 평가를 대화형 피드백 기반 개선 능력으로 확장한 연구
- 🔗 후속 연구: [[papers/196_ChartAssisstant_A_Universal_Chart_Multimodal_Language_Model/review]] — 과학 논문 그림 해석을 차트라는 특정 시각 자료 유형으로 세분화한 확장
- 🧪 응용 사례: [[papers/336_FigCaps-HF_A_Figure-to-Caption_Generative_Framework_and_Benc/review]] — 과학 그림 해석 벤치마크에서 캡션 생성 모델의 성능을 체계적으로 평가
- 🏛 기반 연구: [[papers/1127_MMSD20_Towards_a_Reliable_Multi-modal_Sarcasm_Detection_Syst/review]] — 멀티모달 벤치마크 구축 방법론을 풍자 탐지라는 특정 작업에 적용한 기반
