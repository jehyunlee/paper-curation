# FigCaps-HF: A Figure-to-Caption Generative Framework and Benchmark with Human Feedback

* **저자**: Ashish Singh, Prateek Agarwal, Zixuan Huang, Arpita Singh, Tong Yu, Sungchul Kim, Victor Bursztyn, Nikos Vlassis, Ryan A. Rossi
* **기관**: University of Massachusetts Amherst; Adobe Research
* **발행**: arXiv, 2023
* **DOI**: [10.48550/ARXIV.2307.10867](https://doi.org/10.48550/ARXIV.2307.10867)
* **PDF**: [arXiv 2307.10867](https://arxiv.org/abs/2307.10867)

---

## Essence (본질)

과학 논문의 **그림(figure)에 대한 캡션 자동 생성**을 독자 선호도에 맞춰 최적화하는 프레임워크 **FigCaps-HF**를 제안한다. 핵심은 두 가지로, (1) 소량의 도메인 전문가 피드백으로 학습한 **인간 피드백 예측 모델**(Human Feedback Prediction Model)이 대규모 데이터셋 전체의 캡션 품질을 자동으로 평가하고, (2) **오프라인 Upside-Down RL(UDRL)** 기반 RLHF를 통해 생성 모델을 독자 선호에 맞춰 미세조정한다. BLIP을 기반 모델로 사용할 때 ROUGE-L 16.9%, BLEU 35.7%, METEOR 9%의 성능 향상을 달성했으며, 133,543개 그림-캡션 쌍에 대한 피드백 점수를 포함하는 벤치마크 데이터셋을 공개하였다.

---

## Motivation (연구 동기)

- 과학 논문의 그림 캡션은 연구 내용 전달에 핵심적이나, 실제로는 50% 이상이 독자에게 도움이 되지 않는 저품질 캡션으로 작성됨 (arXiv cs.CL 논문 기준)
- 기존 캡션 생성 모델은 논문에서 추출한 그림-캡션 쌍으로 학습하기 때문에, 원본 캡션의 저품질이 생성 모델에 그대로 전파됨
- 독자의 선호도(도움됨, 핵심 메시지, 시각적 설명력, OCR 내용)를 반영한 학습 프레임워크가 부재하여, 생성된 캡션이 독자 기대와 괴리됨

---

## Achievement (주요 성과)

1. **RLHF 기반 그림 캡션 생성 프레임워크**: 도메인 전문가 피드백을 활용한 최초의 과학 그림 캡션 생성 RLHF 프레임워크
2. **효율적 피드백 예측 모델**: 단 400개의 전문가 레이블로 106,834개 캡션의 품질 점수를 정확히 추론 (median 정합도 높음)
3. **오프라인 UDRL 적용**: 기존 on-policy RLHF 대비 계산 효율적이면서 동등 이상의 성능. 보상 모델이 훈련 후 불필요
4. **일관된 성능 향상**: BLIP-RLHF에서 ROUGE-L 15.2(+16.9%), BLEU 1.9(+35.7%), METEOR 14.5(+9%) 달성
5. **다양한 ablation**: 피드백 양자화 수준(binary vs multi-level), 피드백 메트릭 종류(Takeaway/Visual이 Helpfulness보다 효과적), 임베딩 모델 선택, 피드백 위치(prepend vs append) 등 체계적 분석
6. **공개 벤치마크**: 133,543개 그림-캡션 쌍 + 4가지 품질 메트릭 점수 데이터셋 공개

---

## How (방법론)

- **인간 피드백 예측 모델**: 400개 그림-캡션 쌍에 대해 도메인 전문가가 4가지 메트릭(Helpfulness, Takeaway, Visual-descriptiveness, OCR) 1-5점 평가 → MCSE 임베딩 + 2-layer MLP 회귀 모델 학습 → 전체 데이터셋에 점수 추론
- **Upside-Down RL (오프라인 RLHF)**: 예측된 보상 점수를 이진화(good/bad) 또는 다단계 양자화하여 제어 토큰으로 변환 → 캡션 앞에 제어 토큰을 붙여 조건부 언어 모델링으로 미세조정 (수식: L_HF = cross-entropy with control token prepended)
- **추론 시**: 항상 "good" 토큰을 조건으로 주어 고품질 캡션 생성 유도
- **기반 모델**: BLIP(vision-language 사전학습), ViT+GPT2 등 다양한 아키텍처에서 실험
- **평가 지표**: ROUGE-L, BLEU, METEOR

---

## Originality (독창성)

- **오프라인 UDRL의 RLHF 적용**: 기존 RLHF가 주로 on-policy PPO를 사용하는 데 반해, 오프라인 보상 조건부 행동 복제(reward-conditioned behavioral cloning)를 적용하여 훨씬 단순하고 효율적인 프레임워크 구축
- **소량 전문가 피드백의 확장**: 400개 레이블만으로 10만 건 이상의 피드백을 추론하는 2단계 파이프라인은 실용적이며, 다른 도메인에도 일반화 가능
- **다차원 품질 메트릭**: 단일 점수가 아닌 4가지 독립적 품질 축(Helpfulness, Takeaway, Visual, OCR)을 정의하여 세밀한 피드백 제공
- 다만, 기법 자체(UDRL, 제어 토큰)는 기존 방법론의 직접적 적용에 가까움

---

## Limitation & Further Study (한계 및 향후 연구)

- **다중 피드백 동시 활용 불가**: 현재 프레임워크는 한 번에 하나의 피드백 메트릭만 사용 가능하며, 여러 보상 신호를 복합적으로 활용하는 메커니즘이 없음
- **보상 양자화의 제약**: 연속 보상 점수를 이산 토큰으로 변환해야 하므로 정보 손실이 발생하며, 세밀한 품질 구분이 어려움
- **생성 캡션의 절대 품질**: ROUGE-L 15~17, BLEU 2 수준으로 절대적 성능은 아직 낮으며, 실제 사용에는 부족
- **단일 모달리티 피드백**: 피드백 예측 모델이 주로 텍스트 임베딩에 의존하며, 그림 자체의 시각적 특성을 충분히 활용하지 못함
- **평가의 한계**: 자동 메트릭(ROUGE, BLEU, METEOR)만 사용하며, 인간 평가나 LLM 기반 평가가 부재
- **향후 방향**: 다중 보상 신호 통합, 멀티모달 피드백 모델(그림+텍스트 결합 인코딩), 연속 보상 활용 방법, 다양한 도메인/데이터 분포로의 일반화 검증

---

## Evaluation (평가)

| 항목 | 점수 (1-10) | 비고 |
|------|:-----------:|------|
| **참신성 (Novelty)** | 6 | 오프라인 UDRL의 그림 캡션 RLHF 적용은 새롭지만, 개별 기법(UDRL, 제어 토큰)은 기존 연구의 직접 적용 |
| **기술적 깊이 (Technical Depth)** | 6 | 프레임워크 설계는 명확하나, 피드백 예측 모델이 단순 MLP 회귀이고 시각 정보 활용이 제한적 |
| **실용성 (Practicality)** | 7 | 소량 레이블로 대규모 피드백 추론하는 파이프라인은 실용적. 벤치마크 데이터셋 공개도 유용 |
| **완성도 (Completeness)** | 7 | 다양한 ablation(양자화 수준, 피드백 종류, 임베딩 모델, 위치)을 수행했으나 인간 평가 부재 |
| **영향력 (Impact)** | 6 | 과학 그림 캡션이라는 니치 영역에서 의미 있으나, 절대 성능과 일반화 측면에서 영향력 제한적 |
| **종합 (Overall)** | **6.5** | 소량 전문가 피드백을 효율적으로 활용하는 실용적 프레임워크와 벤치마크 기여는 의미 있으나, 기술적 깊이와 절대 성능 면에서 아쉬움 |

## 평가
| 항목 | 점수 (1-5) |
|------|-----------|
| Novelty | 3 |
| Technical Soundness | 3 |
| Significance | 3 |
| Overall | 3.0 |

**총평**: 소량 전문가 피드백으로 과학 그림 캡션 생성을 RLHF 방식으로 최적화하는 실용적 프레임워크로, 공개 벤치마크 기여도가 있으나 절대 성능은 아직 제한적이다.
