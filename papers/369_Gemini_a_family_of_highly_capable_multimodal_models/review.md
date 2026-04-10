---
title: "369_Gemini_a_family_of_highly_capable_multimodal_models"
authors:
  - "Gemini Robotics Team"
  - "Rohan Anil"
  - "Sebastian Borgeaud"
  - "Jean-Baptiste Alayrac"
  - "Jiahui Yu"
date: "2023"
doi: "N/A"
arxiv: ""
score: 4.5
essence: "Google이 개발한 Gemini는 이미지, 오디오, 비디오, 텍스트를 네이티브하게 처리하는 멀티모달 대규모 언어 모델 패밀리로, Ultra, Pro, Nano 세 가지 크기로 제공되며 30개의 32개 벤치마크 중에서 최첨단 성능을 달성한다."
tags:
  - "cat/Scientific_Language_Processing_and_Visualization"
  - "sub/Multimodal_Scientific_Benchmarks"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Team et al._2023_Gemini a family of highly capable multimodal models.pdf"
---

# Gemini: a family of highly capable multimodal models

> **저자**: Gemini Robotics Team, Rohan Anil, Sebastian Borgeaud, Jean-Baptiste Alayrac, Jiahui Yu, Radu Soricut, Johan Schalkwyk, Andrew M. Dai, Anja Hauth, Katie Millican, David M. Silver, Melvin Johnson, Ioannis Antonoglou, Julian Schrittwieser, Amelia Glaese, Jilin Chen, Emily Pitler, Timothy Lillicrap, Angeliki Lazaridou, Orhan Fırat | **날짜**: 2023 | **DOI**: N/A

---

## Essence

![Figure 2](figures/fig2.webp)
*Gemini 모델은 텍스트, 이미지, 오디오, 비디오의 인터리빙된 시퀀스를 입력으로 받아 텍스트와 이미지가 섞인 응답을 생성할 수 있다.*

Google이 개발한 Gemini는 이미지, 오디오, 비디오, 텍스트를 네이티브하게 처리하는 멀티모달 대규모 언어 모델 패밀리로, Ultra, Pro, Nano 세 가지 크기로 제공되며 30개의 32개 벤치마크 중에서 최첨단 성능을 달성한다.

## Motivation

- **Known**: 기존 대규모 언어 모델(LLM)들은 주로 텍스트에 중심을 두거나 멀티모달 능력이 제한적이었으며, 서로 다른 크기의 모델 계열이 부족했다.

- **Gap**: 단일 아키텍처로 텍스트, 이미지, 오디오, 비디오를 동시에 처리하면서도 복잡한 추론과 크로스모달 이해를 수행할 수 있는 통합 모델 패밀리가 없었다.

- **Why**: 멀티모달 이해는 교육, 과학, 프로그래밍 등 다양한 실제 응용 분야에서 중요하며, 디바이스 상 배포부터 클라우드 기반 추론까지 다양한 계산 환경을 지원할 필요가 있다.

- **Approach**: Transformer 디코더를 기반으로 하되 멀티모달 입력(텍스트, 이미지, 오디오, 비디오)을 처리하도록 설계하고, 32k 컨텍스트 길이를 지원하며, 대규모 TPU 인프라를 활용하여 세 가지 크기(Ultra, Pro, Nano)의 모델을 동시에 개발한다.

## Achievement

![Figure 1](figures/fig1.webp)
*Gemini 모델이 학생의 물리 문제 풀이를 검증하는 예시로, 필기 인식, 문제 이해, LaTeX 생성 능력을 보여준다.*

1. **벤치마크 성능 우위**: Gemini Ultra가 평가된 32개 벤치마크 중 30개에서 최첨단 성능 달성
   - MMLU에서 처음으로 인간 전문가 수준 성능(90% 이상) 달성
   - MMMU 벤치마크에서 62.4% 기록 (이전 최고 기록 대비 5% 이상 개선)
   - 이미지 이해 9/9, 비디오 이해 6/6, 음성 인식 및 번역 5/5 벤치마크에서 최첨단 달성

2. **크로스모달 추론 능력**: 텍스트, 이미지, 오디오를 네이티브하게 처리하면서 복잡한 추론 수행
   - 필기 인식 + 물리 문제 이해 + LaTeX 생성의 통합 능력 시연
   - AlphaCode 2와 통합하여 경쟁 프로그래밍 플랫폼 Codeforces 상위 15% 달성 (이전 상위 50% 대비 개선)

3. **효율적인 모델 계열**: 온디바이스 배포용 Nano 모델(1.8B~3.25B 파라미터)도 크기 대비 뛰어난 성능 제공

## How

![Figure 2](figures/fig2.webp)
*다양한 모달리티의 입력이 인터리빙된 형태로 처리되는 구조*

- **아키텍처**: Transformer 디코더 기반으로 멀티쿼리 어텐션(multi-query attention) 등 효율성 개선 기법 적용
  
- **멀티모달 인코딩**:
  - 이미지: Flamingo, CoCa, PaLI 기반의 비주얼 인코더 사용
  - 오디오: Universal Speech Model (USM) 16kHz 기능으로 직접 수집, 텍스트 변환 시 손실되는 뉘앙스 포착
  - 비디오: 프레임 시퀀스로 인코딩하여 32k 컨텍스트 창 활용
  - 가변 입력 해상도 지원으로 세밀한 이해가 필요한 작업에 더 많은 계산 할당

- **대규모 훈련 인프라**:
  - TPUv5e 및 TPUv4 활용, SuperPods (4096칩) 활용
  - JAX와 Pathways를 통한 단일 컨트롤러 프로그래밍 모델로 훈련 간소화
  - GSPMD 파티셔너와 MegaScale XLA 컴파일러로 최적화
  - 메모리 내 중복 복제를 통한 빠른 복구로 97%의 goodput 달성 (PaLM-2 대비 85% → 97% 개선)

- **안정성**: 결정적 재생(deterministic replay)과 사전 정적 SDC 스캐너로 Silent Data Corruption 감지 및 제거

- **포스트훈련**: 
  - Gemini Apps (대화형 AI Gemini 및 Gemini Advanced용)
  - Gemini API (Google AI Studio 및 Cloud Vertex AI용)
  - 두 가지 변형으로 서로 다른 사용 사례에 최적화

## Originality

- **진정한 멀티모달 아키텍처**: 텍스트, 이미지, 오디오, 비디오를 처음부터 하나의 모델로 처리하는 네이티브 멀티모달 설계 (기존 모델들은 후속 추가 또는 텍스트 변환 기반)

- **대규모 훈련 혁신**: 97% goodput 달성을 위한 메모리 내 중복 복제 전략과 Silent Data Corruption 대응 기법

- **모델 크기 계열화**: Ultra(복잡한 추론), Pro(확장성), Nano(온디바이스) 등 다양한 배포 요구에 부응하는 체계적인 계열 구성

- **이산 이미지 토큰 기반 출력**: 멀티모달 입력뿐만 아니라 이미지 출력도 가능한 구조

## Limitation & Further Study

- **컨텍스트 길이 제한**: 32k 토큰 컨텍스트 길이는 매우 긴 멀티모달 시퀀스에서는 여전히 제약이 될 수 있음

- **계산 비용**: Ultra 모델은 TPUv4 대규모 클러스터 필요로 하여 접근성 제한

- **평가 범위**: 보고된 벤치마크가 주로 영문 기반이며, 다양한 언어와 문화권에서의 성능 검증 필요

- **안전성 및 편향**: 논문에서 responsible deployment를 언급하나, 구체적인 안전성 평가 결과와 편향 분석이 제한적으로 제시됨

- **후속 연구 방향**:
  - 더 긴 컨텍스트 처리 능력 확장
  - 다언어 성능 향상
  - 멀티모달 편향 분석 및 완화
  - 온디바이스 모델의 추가 최적화

## Evaluation

- **Novelty**: 4.5/5 - 진정한 멀티모달 네이티브 아키텍처와 대규모 훈련 혁신이 눈에 띄지만, 개별 기술(Transformer, 시각 인코더)의 개선은 점진적임

- **Technical Soundness**: 4.5/5 - 견고한 아키텍처와 신뢰할 수 있는 대규모 훈련 인프라 구축이 잘 설명되었으나, 일부 기술 세부사항(포스트훈련 기법)이 상세하지 않음

- **Significance**: 5/5 - 멀티모달 AI의 새로운 기준 제시, MMLU 인간 전문가 성능 달성, 교육·과학·프로그래밍 등 광범위한 응용 잠재력

- **Clarity**: 4/5 - 전반적으로 명확하지만, 논문이 매우 길고 일부 기술 인프라 설명이 전문가 대상이라 일반 독자 접근성이 다소 떨어짐

- **Overall**: 4.5/5

**총평**: Gemini는 텍스트, 이미지, 오디오, 비디오를 통합적으로 처리하는 진정한 멀티모달 모델로서, MMLU 인간 전문가 수준 달성 및 30/32 벤치마크 최첨단 성능 기록을 통해 멀티모달 AI의 새로운 기준을 제시하며, 대규모 훈련 인프라 혁신(97% goodput)은 향후 초대형 모델 개발의 모범 사례가 될 것으로 기대된다.

## Related Papers

- 🔄 다른 접근: [[papers/387_Gpt-4_technical_report/review]] — GPT-4와 경쟁하는 Google의 멀티모달 모델로 다른 회사의 접근법을 보여줌
- 🧪 응용 사례: [[papers/551_MMC_Advancing_Multimodal_Chart_Understanding_with_Large-scal/review]] — Gemini의 멀티모달 능력이 MMC의 차트 이해 작업에 직접 적용될 수 있음
- 🔗 후속 연구: [[papers/368_Gemini_15_Unlocking_multimodal_understanding_across_millions/review]] — Gemini 1.5로 발전하면서 더 긴 컨텍스트와 향상된 멀티모달 이해 능력을 제공
- 🧪 응용 사례: [[papers/722_Scifibench_Benchmarking_large_multimodal_models_for_scientif/review]] — Gemini의 멀티모달 능력을 과학 분야 특화 벤치마크로 평가하는 연구
- 🔄 다른 접근: [[papers/387_Gpt-4_technical_report/review]] — Gemini와 함께 멀티모달 AI의 양대 모델로 서로 다른 회사의 접근법을 대표함
- 🧪 응용 사례: [[papers/551_MMC_Advancing_Multimodal_Chart_Understanding_with_Large-scal/review]] — Gemini 같은 멀티모달 모델의 차트 이해 능력을 전문적으로 평가하고 개선하는 연구
- 🏛 기반 연구: [[papers/801_The_llama_3_herd_of_models/review]] — Google의 Gemini 멀티모달 모델 패밀리가 Llama 3의 멀티모달 확장 및 성능 벤치마킹에 비교 기준을 제공한다.
- 🔄 다른 접근: [[papers/1127_MMSD20_Towards_a_Reliable_Multi-modal_Sarcasm_Detection_Syst/review]] — 범용 멀티모달 모델과 달리 풍자 탐지라는 특정 작업에 특화된 시스템 구축
