---
title: "801_The_llama_3_herd_of_models"
authors:
  - "Grattafiori"
  - "Aaron"
  - "Dubey"
  - "Abhimanyu"
  - "Jauhri"
date: "2024"
doi: "arXiv:2407.21783"
arxiv: ""
score: 4.0
essence: "Meta가 발표한 Llama 3는 8B, 70B, 405B 파라미터 규모의 대규모 언어모델 계열로, 15T 다국어 토큰으로 사전학습되었으며 128K 토큰 컨텍스트 윈도우를 지원하는 고성능 기반모델(foundation model)이다. GPT-4 수준의 성능을 달성하면서 다국어, 코딩, 추론, 도구 사용 능력을 기본적으로 지원한다."
tags:
  - "cat/Scientific_Language_Processing_and_Visualization"
  - "sub/Scientific_Language_Models"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Aaron et al._2024_The llama 3 herd of models.pdf"
---

# The Llama 3 Herd of Models

> **저자**: Grattafiori, Aaron, Dubey, Abhimanyu, Jauhri, Abhinav 외 다수 (Meta AI) | **날짜**: 2024.07.23 | **DOI**: [arXiv:2407.21783](https://arxiv.org/abs/2407.21783)

---

## Essence

Meta가 발표한 Llama 3는 8B, 70B, 405B 파라미터 규모의 대규모 언어모델 계열로, 15T 다국어 토큰으로 사전학습되었으며 128K 토큰 컨텍스트 윈도우를 지원하는 고성능 기반모델(foundation model)이다. GPT-4 수준의 성능을 달성하면서 다국어, 코딩, 추론, 도구 사용 능력을 기본적으로 지원한다.

## Motivation

- **Known**: 기존 Llama 2 모델은 1.8T 토큰으로 학습되었으며, 최신 모델들(GPT-4, Claude)과의 성능 격차가 존재함
- **Gap**: 대규모 언어모델의 성능 향상을 위해서는 데이터 품질/량, 훈련 규모, 복잡도 관리의 최적화가 필요함
- **Why**: 더욱 강력한 오픈소스 기반모델을 통해 AI 연구 커뮤니티의 혁신을 가속화하고 AGI로의 책임 있는 경로를 제시할 필요가 있음
- **Approach**: (1) 데이터 품질 개선 및 15T 토큰으로 확대 (2) 405B 규모로 3.8×10²⁵ FLOPs 투자 (3) 표준 Transformer 아키텍처 채택으로 안정성 극대화

## Achievement

1. **최고 성능 달성**: 
   - 405B 모델이 MMLU(87.3), HumanEval(89.0), GSM8K(96.8), ARC Challenge(96.9)에서 GPT-4 대비 동등 이상의 성능 달성
   - 8B, 70B 소형 모델도 동급 파라미터 모델 중 최고 성능(8B: MMLU 69.4, HumanEval 72.6)

2. **다국어 및 장문맥 지원**: 
   - 8개 이상 언어 지원 (MGSM 91.6)
   - 128K 토큰 컨텍스트 윈도우 (ZeroSCROLLS/QuALITY 95.2)

3. **도구 사용 능력**: BFCL에서 88.5 달성하여 제로샷 함수 호출 능력 확보

4. **멀티모달 확장**: 이미지, 비디오, 음성 인식 능력을 어댑터 기반 방식으로 통합 (아직 개발 중)

5. **안전성 강화**: Llama Guard 3를 통한 입출력 안전 필터링 및 DPO 기반의 인간 피드백 정렬

## How

![Figure 1: Llama 3의 전체 아키텍처 및 훈련 파이프라인](figures/fig1.webp)

**사전학습 (Pre-training)**
- 데이터 큐레이션: 웹, 학술 자료, 코드 등 다양한 소스에서 15T 토큰 수집
  - PII 및 성인 콘텐츠 제거 필터링
  - 맞춤형 HTML 파서로 보일러플레이트 제거 및 콘텐츠 정확도 향상
  - 수학/코드 구조 보존 처리
- 모델 아키텍처: 표준 Transformer (밀집형/Dense), 혼합 전문가 모델(MoE) 미채택
- 스케일링: 405B 파라미터, 8K→128K 토큰 윈도우 지속 학습
- 4D 병렬 처리: TP(Tensor Parallelism), CP(Context Parallelism), PP(Pipeline Parallelism), DP(Data Parallelism)

**사후학습 (Post-training)**
- 지도학습 미세조정(SFT): 지시 튜닝 데이터로 1차 정렬
- 거부 샘플링(RS): 고품질 응답 선별
- 직접 선호도 최적화(DPO): 인간 피드백 기반 정렬 (강화학습 대신 채택)

**멀티모달 확장 (미출시)**
- 이미지 인코더: 이미지-텍스트 쌍으로 사전학습
- 음성 인코더: 자체 감독 학습(마스킹 기반)
- 어댑터: 크로스-어텐션 레이어로 시각/음성 표현을 언어모델에 정렬

## Originality

- **데이터 엔지니어링**: 기존 1.8T 대비 15T 다국어 토큰으로 대폭 확대하며, 웹 데이터의 고도화된 필터링 파이프라인 개발
- **스케일 및 컴퓨팅 효율**: Llama 2 대비 ~50배 증가한 3.8×10²⁵ FLOPs를 투자하면서 소형 모델들을 계산 최적값 이상으로 훈련하여 추론 성능 우수화
- **아키텍처 선택의 정당화**: 표준 Transformer와 간단한 사후학습 방식(SFT+RS+DPO)을 고집하여 훈련 안정성과 확장성을 극대화
- **멀티모달 통합 방식**: 별도 인코더와 어댑터의 조합으로 기존 모델을 고정하면서 모달리티 추가 (기술적으로 새롭지는 않지만 체계적 접근)
- **공개 출시**: 405B 최대 모델 포함 완전한 모델 계열 및 Llama Guard 3 공개 (산업 표준 변화)

## Limitation & Further Study

- **멀티모달 모델의 미숙성**: 이미지, 비디오, 음성 기능이 여전히 개발 단계이며 성능 평가 및 비교가 제한적 (세부 벤치마크 부족)
- **컨텍스트 윈도우 확장의 메커니즘 부족**: 8K→128K 확장 과정의 기술적 세부사항이 제한적으로만 공개됨
- **사후학습 데이터의 투명성**: SFT, DPO 단계에 사용된 데이터의 규모, 품질 메트릭, 구성 비율이 부분적으로만 기술됨
- **다국어 성능의 편차**: 8B/70B는 영어 중심이었으나 3.1에서 다국어 지원 추가됨 (초기 버전 제한)
- **추론 비용 분석 부재**: 405B 모델의 실제 배포 시 지연시간(latency), 메모리 요구사항, 추론 비용 상세 분석 미흡
- **후속 연구 방향**:
  - 멀티모달 모델의 완전한 통합 및 성능 최적화
  - 장문맥 능력의 이론적 메커니즘 규명
  - 저리소스 언어에 대한 다국어 성능 확대
  - 강화학습 기반 사후학습과의 성능 비교


## Evaluation

- Novelty: 3.5/5
- Technical Soundness: 4.5/5
- Significance: 4.5/5
- Clarity: 4/5
- Overall: 4/5

**총평**: Llama 3는 데이터 품질 개선과 대규모 투자를 통해 GPT-4 수준의 성능을 달성한 중요한 오픈소스 기반모델이지만, 멀티모달 통합의 미흡함과 기술적 세부사항의 제한된 공개는 완전히 새로운 방법론보다는 기존 기법의 정교한 조합과 규모화의 측면에서 가치를 갖는다.

## Related Papers

- 🔄 다른 접근: [[papers/649_Qwen25_technical_report/review]] — 둘 다 대규모 언어 모델 시리즈이지만 하나는 Meta의 Llama 3이고 다른 하나는 Alibaba의 Qwen2.5로 서로 다른 접근법과 최적화 기술을 사용한다.
- 🏛 기반 연구: [[papers/369_Gemini_a_family_of_highly_capable_multimodal_models/review]] — Google의 Gemini 멀티모달 모델 패밀리가 Llama 3의 멀티모달 확장 및 성능 벤치마킹에 비교 기준을 제공한다.
- 🔗 후속 연구: [[papers/617_Phi-4_technical_report/review]] — Microsoft의 Phi-4가 Llama 3보다 작은 규모에서 효율적인 성능을 달성하는 방법을 보여주어 모델 크기 최적화 관점을 제공한다.
- 🧪 응용 사례: [[papers/026_A_survey_of_large_language_models/review]] — Llama 3 모델군을 통해 대규모 언어모델의 실제 구현과 성능을 구체적으로 보여준다.
- 🔄 다른 접근: [[papers/266_Deepseek-v3_technical_report/review]] — Llama 3와 유사한 성능을 MoE 아키텍처로 더 효율적으로 달성하는 경쟁 모델
- 🔄 다른 접근: [[papers/387_Gpt-4_technical_report/review]] — GPT-4와 경쟁하는 Meta의 오픈소스 언어 모델 시리즈
- 🔄 다른 접근: [[papers/370_Gemma_2_Improving_open_language_models_at_a_practical_size/review]] — Llama 3와 유사한 성능을 지식 증류 기반으로 더 작은 크기로 달성
- 🏛 기반 연구: [[papers/245_Crosslingual_capabilities_and_knowledge_barriers_in_multilin/review]] — Llama 3 모델군의 다국어 능력에서 발견되는 교차언어 지식 장벽 현상의 이론적 기반
- 🏛 기반 연구: [[papers/617_Phi-4_technical_report/review]] — Llama 3 모델군의 개선된 추론 능력을 더욱 특화시켜 STEM 성능을 향상시킨 발전
