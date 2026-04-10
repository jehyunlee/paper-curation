---
title: "649_Qwen25_technical_report"
authors:
  - "Qwen An Yang"
  - "Baosong Yang"
  - "Beichen Zhang"
  - "Binyuan Hui"
  - "Bo Zheng"
date: "2024"
doi: "아직"
arxiv: ""
score: 0
essence: "본 논문은 Qwen2.5 대규모 언어 모델(LLM) 시리즈를 소개하며, 사전학습 데이터를 7조에서 18조 토큰으로 확대하고, 감독 미세조정(SFT), 직접 선호도 최적화(DPO), 그룹 상대 정책 최적화(GRPO) 등 고도화된 후학습 기법을 적용하여 이전 버전 대비 대폭 향상된 성능을 달성했다."
tags:
  - "cat/Scientific_Language_Processing_and_Visualization"
  - "sub/Scientific_Language_Models"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Yang et al._2024_Qwen2.5 technical report.pdf"
---

# Qwen2.5 technical report

> **저자**: Qwen An Yang, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu, Chengyuan Li, Dayiheng Liu, Fei Huang, Guanting Dong, Haoran Wei, Huan Lin, Jian Yang, Jianhong Tu, Jianwei Zhang, Jianxin Yang, Jiaxin Yang, Jingren Zhou, Junyang Lin, Kai Dang | **날짜**: 2024 | **DOI**: 아직 미정

---

## Essence

![Figure 1](figures/fig1.webp)
*Qwen 시리즈의 반복적 개발 과정에서 데이터 스케일링의 중요성을 시각화. Qwen2.5는 18조 토큰으로 사전학습되어 수학, MBPP, BBH, MMLU 벤치마크에서 우수한 성능을 보임.*

본 논문은 Qwen2.5 대규모 언어 모델(LLM) 시리즈를 소개하며, 사전학습 데이터를 7조에서 18조 토큰으로 확대하고, 감독 미세조정(SFT), 직접 선호도 최적화(DPO), 그룹 상대 정책 최적화(GRPO) 등 고도화된 후학습 기법을 적용하여 이전 버전 대비 대폭 향상된 성능을 달성했다.

## Motivation

- **Known**: 최근 대규모 언어 모델의 발전으로 AGI의 징후가 보이고 있으며, 모델 및 데이터 스케일링과 사전학습-SFT-RLHF 패러다임이 언어 이해, 생성, 추론 능력의 향상을 가능하게 함. Llama, Mistral 등 오픈 가중치 모델들이 LLM 접근성을 민주화했음.

- **Gap**: Qwen2의 경우 생성 길이(2K 토큰), 구조화된 데이터 처리(표, JSON), 도구 사용성 등에서 제한이 있었고, 3B, 14B, 32B 같은 중간 규모 모델이 부재하여 리소스 제약 시나리오에서의 선택지가 제한됨.

- **Why**: 다양한 규모와 용도에 맞춘 효율적인 모델 시리즈가 필요하며, 특히 코딩, 수학 등 전문 영역에서의 강화와 더 우수한 인간 선호도 정렬이 요구됨.

- **Approach**: 사전학습 데이터 대폭 확대(18조 토큰)와 고품질 필터링, 수학/코딩 데이터 통합, 합성 데이터 생성, 도메인 균형화를 통해 데이터 개선. 0.5B~72B 밀집(dense) 모델과 MoE 기반 Turbo/Plus 모델의 다양한 사이즈 제공. 초장문(1M 토큰) 문맥 처리 및 고급 후학습 기법 도입.

## Achievement

![Figure 2](figures/fig2.webp)
*Qwen2.5-Turbo의 100만 토큰 길이 Passkey Retrieval 작업 성능. 초장문 처리 능력을 입증.*

1. **데이터 스케일링의 효과**: 사전학습 데이터를 18조 토큰으로 확대함으로써 수학, 코딩, 상식 및 전문 지식에서 현저한 향상 달성. 특히 MMLU, BBH, MBPP 벤치마크에서 이전 버전 대비 큰 성능 향상.

2. **경쟁력 있는 오픈 가중치 모델**: Qwen2.5-72B-Instruct가 약 5배 큰 Llama-3-405B-Instruct와 경쟁 가능한 성능 달성. 0.5B부터 72B까지 7가지 사이즈로 다양한 배포 시나리오 지원.

3. **MoE 기반 API 모델**: Qwen2.5-Turbo와 Qwen2.5-Plus가 각각 GPT-4o-mini, GPT-4o와 경쟁 가능한 비용-효율성 제공.

4. **초장문 처리 능력**: Qwen2.5-Turbo가 1M(100만) 토큰 문맥 길이 지원. 생성 길이를 2K에서 8K 토큰으로 확대.

5. **구조화된 데이터 처리 개선**: 표, JSON 등 구조화된 입력/출력에 대한 더 나은 지원.

## How

### 사전학습 데이터 개선

- **고급 필터링**: Qwen2-Instruct 모델을 데이터 품질 필터로 활용하여 다차원 분석을 통한 정교한 평가 및 채점. 이는 Qwen2의 확대된 다국어 사전학습 능력을 활용한 향상된 방식.

- **도메인 특화 데이터 통합**: Qwen2.5-Math와 Qwen2.5-Coder의 고품질 데이터셋을 사전학습 단계에 직접 통합하여 수학 추론 및 코드 생성 능력 강화.

- **합성 데이터 생성**: Qwen2-72B-Instruct와 Qwen2-Math-72B-Instruct로부터 고품질 합성 데이터 생성. 일반 보상 모델과 Qwen2-Math-RM-72B를 통한 엄격한 필터링으로 품질 보증.

- **균형 잡힌 데이터 혼합**: Qwen2-Instruct 모델을 활용한 도메인 분류 및 균형화. 전자상거래, SNS 등 과다 대표된 도메인은 다운샘플링하고, 기술, 과학, 학문 영역은 업샘플링하여 정보가 풍부한 훈련 데이터셋 구성.

### 하이퍼파라미터 스케일링 법칙

- 모델 크기별 최적 학습률(learning rate, μ_opt)과 배치 크기(batch size, B_opt) 도출.

- 밀집 모델(44M~14B) 및 MoE 모델(활성화된 파라미터 44M~1B)에 대한 광범위한 실험을 통해 모델 아키텍처와 훈련 데이터 크기 간의 관계 분석.

- MoE 모델의 활성화된 파라미터와 전체 파라미터 튜닝을 통해 밀집 모델(예: Qwen2.5-72B, 14B)과의 성능 동등성 달성.

### 장문맥 사전학습

![Figure 3](figures/fig3.webp)
*Qwen2.5-Turbo와 Qwen2.5-7B의 TTFT(첫 토큰까지의 시간) 비교. 완전 어텐션 대비 최적화된 구현의 효율성을 보여줌.*

- **2단계 사전학습**: 초기 4,096 토큰 문맥 길이로 학습 후, 최종 단계에서 32,768 토큰으로 확대(소형 모델 제외).

- **Turbo 모델의 특수 처리**: 1M 토큰까지의 초장문 처리 능력 구현을 위한 전문화된 훈련.

### 아키텍처 특징

- **밀집 모델**: Transformer 기반 디코더 아키텍처 유지. Grouped Query Attention(GQA), SwiGLU 활성화 함수, Rotary Positional Embeddings(RoPE), RMSNorm 등 활용.

- **MoE 모델**: 표준 FFN 층을 MoE 층으로 대체. 세밀한 전문가 분할(fine-grained expert segmentation)과 공유 전문가 라우팅(shared experts routing) 구현.

- **토큰화**: BBPE 기반 토크나이저, 151,643개의 정규 토큰 어휘. 제어 토큰을 3개에서 22개로 확대(도구 기능 관련 토큰 추가).

### 후학습(Post-training)

- **감독 미세조정(SFT)**: 100만 개 이상의 샘플을 통한 복잡한 SFT 구현.

- **직접 선호도 최적화(DPO)**: 오프라인 학습 단계에서의 선호도 기반 최적화.

- **그룹 상대 정책 최적화(GRPO)**: 온라인 학습 단계에서의 정책 최적화. 인간 선호도 정렬 강화.

- **성능 향상 영역**: 장문 생성, 구조화 데이터 분석, 지시 준수.

## Originality

- **대규모 다단계 데이터 개선**: 필터링, 도메인 특화 데이터 통합, 합성 데이터, 도메인 균형화를 조합한 포괄적 데이터 전략은 기존 연구의 일부를 개선했으나 개별 기법의 조합 측면에서 창의적.

- **스케일링 법칙의 실질적 응용**: 하이퍼파라미터 최적화에 스케일링 법칙을 체계적으로 적용하여 다양한 모델 크기에서의 최적 훈련 조건 도출. 이는 기존의 모델 크기 결정 중심의 스케일링 법칙 연구와 차별화.

- **다양한 모델 사이즈 제공**: 0.5B~72B 밀집 모델에 MoE 기반 API 모델을 결합하여 제공하는 생태계 구축은 실무적 기여.

- **초장문 처리의 구현**: 1M 토큰 문맥 처리는 기술적 성취이나, 개념적 신규성은 제한적.

## Limitation & Further Study

- **기술 보고서의 제한**: 본 논문은 기술 보고서로서 새로운 알고리즘이나 이론적 통찰보다는 공학적 개선 사항을 중심으로 기술. 각 개선 사항의 개별 기여도에 대한 정밀한 절제 연구(ablation study) 부재.

- **데이터 상세정보 공개 미흡**: 18조 토큰 데이터셋의 도메인 구성, 필터링 기준, 합성 데이터 생성 방식 등에 대한 상세한 공개가 제한적이어서 재현성 저해 우려.

- **비교 분석의 한계**: 동일한 계산 예산 조건에서의 직접 비교가 제한적. MoE 모델의 경우 API 기반으로만 제공되어 상세한 기술 분석 어려움.

- **후학습 기법의 창의성**: DPO와 GRPO는 기존 기법이며, 이들의 결합 및 다단계 적용 효과에 대한 이론적 분석 부족.

- **후속 연구 방향**: (1) 더 큰 규모 모델에서의 스케일링 법칙 검증, (2) 초장문 처리의 효율성 개선, (3) 특화 모델(수학, 코딩) 개발 심화, (4) 다국어 성능 확대 기대.

## Evaluation

- **Novelty**: 3/5
  - 개별 기법들의 조합 및 실질적 응용이 주된 기여. 스케일링 법칙의 하이퍼파라미터 최적화 응용은 차별화되나, 대체로 기존 기법의 공학적 개선.

- **Technical Soundness**: 4/5
  - 체계적인 실험과 광범위한 벤치마크 평가를 통한 검증. 데이터 처리 및 모델 아키텍처 설계가 견고함. 다만 절제 연구 부재로 개별 기여도 검증 한계.

- **Significance**: 4/5
  - 다양한 규모의 오픈 가중치 모델 제공으로 LLM 접근성 강화 및 실제 배포 시나리오 충족. 상태 최고 수준의 오픈 가중치 모델 성능 달성 의미 큼. 다만 기술적 혁신성은 제한적.

- **Clarity**: 4/5
  - 논문 구성이 명확하고 주요 성과가 잘 정리됨. Figure와 Table이 효과적으로 정보를 전달. 다만 일부 기술 세부사항(예: Mo

## Related Papers

- 🔄 다른 접근: [[papers/266_Deepseek-v3_technical_report/review]] — 둘 다 중국 기업의 최신 대규모 언어 모델이지만 하나는 Alibaba의 Qwen2.5이고 다른 하나는 DeepSeek의 DeepSeek-v3로 서로 다른 기술적 접근법을 사용한다.
- 🏛 기반 연구: [[papers/370_Gemma_2_Improving_open_language_models_at_a_practical_size/review]] — Google의 Gemma 2 모델이 실용적 규모에서 오픈 언어 모델을 개선하는 방법을 제시하여 Qwen2.5의 성능 향상 기법과 비교할 수 있는 기준을 제공한다.
- 🔗 후속 연구: [[papers/751_SFT_Memorizes_RL_Generalizes_A_Comparative_Study_of_Foundati/review]] — SFT와 RL의 비교 연구가 Qwen2.5에서 사용된 DPO와 GRPO 같은 후학습 기법의 효과를 이론적으로 뒷받침한다.
- 🔄 다른 접근: [[papers/801_The_llama_3_herd_of_models/review]] — 둘 다 대규모 언어 모델 시리즈이지만 하나는 Meta의 Llama 3이고 다른 하나는 Alibaba의 Qwen2.5로 서로 다른 접근법과 최적화 기술을 사용한다.
