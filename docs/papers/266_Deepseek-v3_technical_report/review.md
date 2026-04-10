---
title: "266_Deepseek-v3_technical_report"
authors:
  - "DeepSeek-AI"
  - "Aixin Liu"
  - "Bei Feng"
  - "Bing Xue"
  - "Bingxuan Wang"
date: "2024"
doi: "arXiv:2412.19437v2"
arxiv: ""
score: 4.5
essence: "671B 매개변수를 가진 혼합 전문가(Mixture-of-Experts, MoE) 언어 모델 DeepSeek-V3를 제시하며, 토큰당 37B만 활성화되어 효율적 추론을 실현한다. 보조 손실 없는 부하 균형 전략과 다중 토큰 예측(Multi-Token Prediction, MTP) 목표를 도입하여 뛰어난 성능을 달성하면서도 2.788M H800 GPU 시간이라는 경제적 훈련 비용으로 완성했다."
tags:
  - "cat/Scientific_Language_Processing_and_Visualization"
  - "sub/Scientific_Language_Models"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/DeepSeek-AI et al._2024_Deepseek-v3 technical report.pdf"
---

# Deepseek-v3 technical report

> **저자**: DeepSeek-AI, Aixin Liu, Bei Feng, Bing Xue, Bingxuan Wang, Bowen Wu, Chengda Lu, Chenggang Zhao, Chengqi Deng, Chenyu Zhang, Chong Ruan, Damai Dai, Daya Guo, Dejian Yang, Deli Chen, Dongjie Ji, Erhang Li, Fangyun Lin, Fengze Dai, Fuli Luo | **날짜**: 2024 | **DOI**: arXiv:2412.19437v2

---

## Essence

![Figure 1](figures/fig1.webp)
*그림 1: DeepSeek-V3와 동종 모델들의 벤치마크 성능 비교*

671B 매개변수를 가진 혼합 전문가(Mixture-of-Experts, MoE) 언어 모델 DeepSeek-V3를 제시하며, 토큰당 37B만 활성화되어 효율적 추론을 실현한다. 보조 손실 없는 부하 균형 전략과 다중 토큰 예측(Multi-Token Prediction, MTP) 목표를 도입하여 뛰어난 성능을 달성하면서도 2.788M H800 GPU 시간이라는 경제적 훈련 비용으로 완성했다.

## Motivation

- **Known**: 기존 대규모 언어 모델(LLM)들은 높은 훈련 비용과 추론 지연으로 인해 실용화에 제약이 있으며, MoE 아키텍처는 전문가 간 부하 불균형과 효율성 문제를 야기함.

- **Gap**: DeepSeek-V2 이후 더욱 향상된 아키텍처 혁신과 훈련 효율화 기법이 필요하며, 특히 보조 손실(auxiliary loss) 없이 부하 균형을 달성하고 저정밀(low-precision) 훈련의 대규모 적용 검증이 부족함.

- **Why**: 개방형 모델의 성능을 폐쇄형 최고 성능 모델(GPT-4o, Claude-3.5)에 근접시키면서도 훈련 비용을 획기적으로 절감하기 위해서는 알고리즘, 프레임워크, 하드웨어의 공동 설계가 필수적.

- **Approach**: (1) 보조 손실 없는 부하 균형 전략 도입, (2) 다중 토큰 예측 훈련 목표 적용, (3) FP8 혼합 정밀도 훈련 프레임워크 구현, (4) DualPipe 파이프라인 병렬화와 계산-통신 중첩(computation-communication overlap) 최적화, (5) DeepSeek-R1으로부터의 추론 능력 증류(knowledge distillation).

## Achievement

![Figure 2](figures/fig2.webp)
*그림 2: DeepSeek-V3의 기본 아키텍처 (다중 헤드 잠재 주의 및 DeepSeekMoE)*

1. **성능 우월성**: 
   - MMLU-Pro 75.9, GPQA-Diamond 59.1, MATH-500 90.2 등에서 모든 개방형 모델 능가
   - MMLU 88.5로 GPT-4o 및 Claude-3.5와 경쟁 수준의 성능 달성
   - AIME 2024에서 39.2% Pass@1 달성 (o1-preview 능가 가능)

2. **훈련 비용 혁신**:
   - 총 2.788M H800 GPU 시간 (약 $5.576M) 소요
   - 1조 토큰당 180K GPU 시간 = 2048 GPU 클러스터에서 3.7일
   - 2개월 이내 사전 훈련 완료

3. **훈련 안정성**: 전체 훈련 과정에서 회복 불가능한 손실 급증(loss spikes)이나 롤백(rollback) 없음

4. **기술 검증**: 671B 규모의 초대형 모델에서 FP8 혼합 정밀도 훈련의 실효성 최초 입증

## How

![Figure 3](figures/fig3.webp)
*그림 3: 다중 토큰 예측(MTP) 구현 방식*

![Figure 4](figures/fig4.webp)
*그림 4: 전방향 및 역방향 청크 쌍의 중첩 전략*

![Figure 5](figures/fig5.webp)
*그림 5: 8개 PP rank와 20개 마이크로배치에 대한 DualPipe 스케줄링 예시*

**아키텍처 개선:**
- Multi-Head Latent Attention (MLA): 키-값(KV) 캐시 크기를 대폭 감소시켜 추론 효율 증대
- DeepSeekMoE: 토큰당 37B만 활성화하여 계산량 최적화

**부하 균형 전략:**
- 보조 손실 제거로 모델 성능 저하 방지
- 배치 단위 및 시퀀스 단위 부하 균형 비교 분석
- 전문가(expert) 특화 패턴 유지

**다중 토큰 예측:**
- 단일 토큰이 아닌 다음 N개 토큰 동시 예측으로 학습 신호 강화
- 추론 시 추측적 디코딩(speculative decoding)으로 활용 가능

**FP8 혼합 정밀도 훈련:**
- 양자화(quantization) 및 곱셈 단계에서 정밀도 개선
- 저정밀 저장 및 통신으로 메모리 및 대역폭 절감
- BF16과 비교하여 훈련 속도 및 메모리 효율성 입증

**훈련 프레임워크 최적화:**
- DualPipe: 파이프라인 기포(pipeline bubble) 최소화
- 계산-통신 중첩: 노드 간 all-to-all 통신 오버헤드 근처(near-zero) 달성
- InfiniBand 및 NVLink 대역폭 최적 활용
- 테인서 병렬화(tensor parallelism) 없이 훈련 가능

**사전 훈련:**
- 14.8조 고품질 다양한 토큰으로 훈련
- 32K → 128K 컨텍스트 길이 2단계 확장
- 데이터 구성 및 하이퍼파라미터 세심한 설계

**사후 훈련:**
- Supervised Fine-Tuning (SFT): 지시 따르기 능력 강화
- Reinforcement Learning (RL): 보상 모델 기반 정책 최적화
- Group Relative Policy Optimization (GRPO): 그룹 상대 보상 활용
- DeepSeek-R1 증류: 추론 능력 이전 및 생성 길이 제어

## Originality

- **보조 손실 제거 부하 균형**: 기존 MoE 모델들이 부하 균형을 위해 보조 손실을 도입하면 모델 성능이 저하되는 문제를 해결하는 혁신적 방안 제시

- **FP8 대규모 훈련 검증**: 671B 초대형 모델에서 FP8 혼합 정밀도 훈련의 안정성과 효과성을 최초로 대규모로 입증

- **DualPipe 파이프라인 병렬화**: 계산-통신 중첩을 통해 노드 간 MoE 전문가 분산 배치 시 통신 오버헤드 최소화

- **다중 토큰 예측 훈련 목표**: 단순 다음 토큰 예측 대신 다중 토큰 동시 예측으로 모델 성능 향상

- **DeepSeek-R1 증류 방법론**: 장형 Chain-of-Thought 추론 능력을 표준 LLM으로 효과적으로 이전하는 새로운 파이프라인

## Limitation & Further Study

- **데이터 시큐리티**: 데이터 구성 상세 정보 부재로 재현성 및 독립적 검증에 제약

- **컨텍스트 길이 한계**: 최대 128K 토큰으로 초장문(ultra-long context) 작업에는 제한적

- **추론 지연**: 671B 모델 크기로 인한 절대적 추론 지연 시간 단축 여지 필요

- **하드웨어 의존성**: H800 특화 최적화로 다른 가속기(예: TPU, AMD MI300) 이식성 미검증

- **후속 연구 방향**:
  - 더욱 경량화된 모델(distilled models) 개발
  - 200K 이상 초장문 컨텍스트 확장
  - 멀티모달(multimodal) 능력 통합
  - 자동회귀 외 다른 생성 목표 탐색
  - 하드웨어 독립적 최적화 기법 개발

## Evaluation

- **Novelty**: 4.5/5 – 보조 손실 제거, FP8 대규모 훈련, DualPipe 등 여러 혁신 기여하나 각각 개별 개선 성격

- **Technical Soundness**: 4.5/5 – 상세한 기술 설명과 광범위한 ablation 연구로 신뢰성 높음. 다만 FP8 정밀도 손실 가능성에 대한 더 깊은 이론적 분석 부족

- **Significance**: 5/5 – 개방형 최고 성능 모델 달성, 훈련 비용 획기적 절감($5.576M), 산업적 영향력 극대

- **Clarity**: 4/5 – 기술 설명 충실하나 DualPipe 알고리즘 상세 설명과 all-to-all 통신 커널 구현이 다소 간략

- **Overall**: 4.5/5

**총평**: DeepSeek-V3는 아키텍처 혁신(보조 손실 제거, 다중 토큰 예측), 훈련 최적화(FP8, DualPipe, 계산-통신 중첩), 사후 훈련 고도화(R1 증류)를 통해 개방형 모델의 성능 한계를 획기적으로 상향 조정하면서도 훈련 비용을 대폭 절감한 획기적 기여를 달성했다. 다만 데이터 구성 세부 정보 공개 부재와 하드웨어 특화 최적화의 이식성 문제가 향후 과제로 남아있다.

## Related Papers

- 🔄 다른 접근: [[papers/387_Gpt-4_technical_report/review]] — GPT-4와 경쟁하는 대규모 MoE 모델로 효율성과 성능 면에서 다른 접근법을 제시
- ⚖️ 반론/비판: [[papers/370_Gemma_2_Improving_open_language_models_at_a_practical_size/review]] — DeepSeek-V3의 대규모 MoE 접근법과 달리 Gemma 2는 경량화된 효율적 모델에 집중
- 🔄 다른 접근: [[papers/801_The_llama_3_herd_of_models/review]] — Llama 3와 유사한 성능을 MoE 아키텍처로 더 효율적으로 달성하는 경쟁 모델
- 🔗 후속 연구: [[papers/617_Phi-4_technical_report/review]] — Phi-4의 효율적 소형 모델 철학을 대규모 MoE로 확장한 접근법
- ⚖️ 반론/비판: [[papers/370_Gemma_2_Improving_open_language_models_at_a_practical_size/review]] — DeepSeek-V3의 대규모 MoE와 달리 Gemma 2는 소형 모델의 효율성과 실용성 강조
- 🔄 다른 접근: [[papers/649_Qwen25_technical_report/review]] — 둘 다 중국 기업의 최신 대규모 언어 모델이지만 하나는 Alibaba의 Qwen2.5이고 다른 하나는 DeepSeek의 DeepSeek-v3로 서로 다른 기술적 접근법을 사용한다.
