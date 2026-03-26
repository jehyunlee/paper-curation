# InternAgent: When Agent Becomes the Scientist -- Building Closed-Loop System from Hypothesis to Verification

> **저자**: InternAgent Team, Bo Zhang, Shiyang Feng, Xiangchao Yan, Jiakang Yuan, Runmin Ma, Yusong Hu, Zhiyin Yu, Xiaohan He, Songtao Huang, Shaowei Hou, Zheng Nie, Zhilong Wang, Jinyao Liu, Tianshuo Peng, Peng Ye, Dongzhan Zhou, Shufei Zhang, Xiaosong Wang, Yilan Zhang | **날짜**: 2025 | **Link**: [https://arxiv.org/abs/2505.16938](https://arxiv.org/abs/2505.16938)

---

## Essence

과학 연구의 전 과정(가설 → 검증)을 자율적으로 수행하는 통합 closed-loop multi-agent framework인 InternAgent를 제안한다. 12개 과학 연구 태스크에서 scalability, interactivity, efficiency의 세 가지 핵심 장점을 갖추며, reaction yield prediction(27.6%→35.4%, 12시간), enhancer activity prediction(0.65→0.79, 4시간) 등에서 유의미한 성능 향상을 달성했다.

## Motivation

- **알려진 것**: AI가 과학 연구의 효율성을 높이고 혁신을 가속화하고 있으나, 대부분 개별 단계에 국한
- **Gap**: 가설 생성부터 실험 검증까지의 전체 연구 루프를 자율적으로 수행하는 통합 프레임워크 부재
- **왜 중요한가**: Autonomous Scientific Research(ASR)를 통해 연구자가 복잡한 문제를 전례 없는 속도와 정밀도로 해결 가능
- **접근법**: Multi-agent framework으로 연구 파이프라인 전체를 closed-loop으로 통합하고, human expert feedback과 multi-agent interaction을 지원

## Achievement

1. 12개 과학 연구 태스크에 걸친 범용적 적용 가능성(Scalability) 입증
2. Reaction yield prediction: 27.6% → 35.4% (12시간 내 달성)
3. Enhancer activity prediction: accuracy 0.65 → 0.79 (4시간 내 달성)
4. 2D semantic segmentation: precision 78.8% → 81.0% (30시간 내 달성)
5. Human expert feedback과 자동 end-to-end 프로세스의 seamless 통합(Interactivity)

## How

- **Multi-agent Architecture**: 다수의 전문화된 agent가 협업하여 아이디어 생성, 코드 구현, 실험 수행, 결과 분석의 전체 루프를 수행
- **Closed-loop Design**: 가설 생성 → 실험 설계 → 구현 → 검증의 순환 구조로 자동 개선
- **Human-in-the-loop**: 자동화 프로세스 중 domain expert의 피드백을 수용하는 인터페이스 제공
- **다양한 실험 도메인**: 화학(반응 수율), 생물학(enhancer 활성), 컴퓨터 비전(semantic segmentation) 등 12개 분야에서 검증

## Originality

- **Closed-loop ASR Framework**: 가설에서 검증까지의 전체 과학 연구 루프를 multi-agent로 자동화한 최초의 통합 프레임워크
- **Scalability across Domains**: 단일 프레임워크로 12개 이질적인 과학 분야에 적용 가능함을 입증한 범용성
- **Interactive Autonomy**: 완전 자동화와 human-in-the-loop의 균형을 맞춘 설계로, 실용적 ASR 시스템의 새로운 패러다임 제시

**Abstract에서 추출된 독창성 문장**: We introduce InternAgent, a unified closed-loop multi-agent framework to conduct Autonomous Scientific Research (ASR) across various scientific research fields, enabling researchers to tackle complicated problems in these fields with unprecedented speed and precision.. InternAgent highlights three key advantages: 1) Scalability: InternAgent has demonstrated its versatility across 12 scientific research tasks, capable of generating innovative ideas to enhance the performance of baseline code.. 2) Interactivity: InternAgent provides an interface for human expert feedback and multi-agent interaction in automated end-to-end processes, allowing for the seamless integration of domain expert knowledge.. 3) Efficiency: InternAgent has achieved promising performance gains in several scientific fields with significantly less time cost compared to human efforts.. For instance, in reaction yield prediction, it increased from 27.6% to 35.4% in just 12 hours; in enhancer activity prediction, accuracy rose from 0.65 to 0.79 with only 4 hours of processing; and in 2D semantic segmentation, precision advanced from 78.8% to 81.0% in a mere 30 hours.

## Limitation & Further Study

### 저자들이 언급한 한계

- 성능 개선폭이 task에 따라 상이하며, 일부 task에서는 제한적 향상
- 현재 baseline code 개선에 초점이 맞춰져 있어, 근본적으로 새로운 연구 방향 제시 능력은 미검증

### 자체판단 아쉬운 점

- 12개 task 모두에서의 정량적 비교가 불충분하며, cherry-picked 결과일 가능성 배제 어려움
- Agent 간 coordination overhead와 failure mode에 대한 분석이 부족
- Human expert feedback의 기여도와 순수 autonomous 성능의 분리 평가가 없어, 시스템의 실질적 자율성 판단 어려움
- Baseline code 개선과 진정한 scientific discovery의 차이에 대한 critical discussion 부재

### 후속 연구

- 진정한 novel hypothesis 생성 능력에 대한 체계적 평가
- 실험실 자동화(robotic lab)와의 통합을 통한 wet-lab ASR 구현
- Agent failure recovery 및 hallucination detection 메커니즘 강화

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 4/5 |
| Technical Soundness | 3/5 |
| Significance | 4/5 |
| Clarity | 4/5 |
| Overall | 4/5 |

**총평**: 과학 연구의 전체 루프를 closed-loop multi-agent로 자동화한 의미 있는 시스템으로, 12개 분야에서의 범용성이 인상적이다. 다만 baseline 코드 개선과 진정한 과학적 발견 사이의 간극, 그리고 human feedback 기여도의 분리 평가가 향후 핵심 과제이다.
