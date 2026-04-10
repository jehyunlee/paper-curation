---
title: "811_Tikzero_Zero-shot_text-guided_graphics_program_synthesis"
authors:
  - "Jonas Belouadi"
  - "Eddy Ilg"
  - "Margret Keuper"
  - "Hideki Tanaka"
  - "Masao Utiyama"
date: "2025"
doi: "arXiv:2503.11509"
arxiv: ""
score: 4.0
essence: "텍스트 설명으로부터 TikZ 그래픽 프로그램을 생성하는 문제를 해결하기 위해, 캡션-프로그램 정렬 데이터의 부족이라는 핵심 병목을 극복하는 TikZero를 제시한다. 이 방법은 이미지 표현을 매개자로 활용하여 그래픽 프로그램 생성과 텍스트 이해를 분리함으로써, 정렬되지 않은 대규모 데이터를 독립적으로 활용할 수 있다."
tags:
  - "cat/Scientific_Language_Processing_and_Visualization"
  - "sub/Scientific_Graphics_Evaluation"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Young et al._2025_Tikzero Zero-shot text-guided graphics program synthesis.pdf"
---

# TikZero: Zero-shot text-guided graphics program synthesis

> **저자**: Jonas Belouadi, Eddy Ilg, Margret Keuper, Hideki Tanaka, Masao Utiyama, Raj Dabre, Steffen Eger, Simone Ponzetto | **날짜**: 2025 | **DOI**: [arXiv:2503.11509](https://arxiv.org/abs/2503.11509)

---

## Essence

![Figure 2](figures/fig2.webp)
*Figure 2. 그래픽 프로그램 합성을 위한 학습 데이터 가용성 비교*

텍스트 설명으로부터 TikZ 그래픽 프로그램을 생성하는 문제를 해결하기 위해, 캡션-프로그램 정렬 데이터의 부족이라는 핵심 병목을 극복하는 TikZero를 제시한다. 이 방법은 이미지 표현을 매개자로 활용하여 그래픽 프로그램 생성과 텍스트 이해를 분리함으로써, 정렬되지 않은 대규모 데이터를 독립적으로 활용할 수 있다.

## Motivation

- **Known**: 
  - TikZ와 같은 그래픽 프로그래밍 언어는 벡터 포맷보다 높은 기하학적 정밀도와 편집 가능성을 제공
  - DeTikZify는 역 그래픽스(inverse graphics) 모델로 이미지에서 TikZ 프로그램을 생성하지만 텍스트 지도(guidance)가 없음
  - AutomaTikZ는 텍스트 지도 TikZ 합성을 시도하지만 성능이 제한적

- **Gap**: 
  - 캡션이 달린 그래픽 프로그램의 부족: 텍스트 기반 방법은 정렬된 caption-program 쌍에만 의존
  - 캡션이 달린 래스터 이미지와 정렬되지 않은 그래픽 프로그램의 대규모 데이터가 존재하지만 활용되지 않음

- **Why**: 
  - 학술 커뮤니티에서 TikZ 사용이 광범위하나, 학습 곡선이 가파름 (TeX Stack Exchange에서 가장 빈번하게 논의되는 주제)
  - 사람이 만든 고품질 그래픽 프로그램의 풀은 충분하지만 캡션이 없음

- **Approach**: 
  - 역 그래픽스 모델(VLM 기반)과 텍스트 조건 어댑터 네트워크를 분리
  - 어댑터는 캡션에서 비전 인코더의 이미지 패치 임베딩을 합성
  - 정렬되지 않은 캡션 이미지와 그래픽 프로그램으로 독립적으로 학습

## Achievement

![Figure 1](figures/fig1.webp)
*Figure 1. TikZero+와 AutomaTikZv2의 정성적 비교*

1. **새로운 아키텍처**: TikZero는 표현 공간 정렬(representation space alignment)을 통해 정렬된 데이터의 필요성을 제거하면서 텍스트 기반 그래픽 프로그램 합성을 달성

2. **데이터셋 기여**: DaTikZv3 데이터셋 공개 - 45만+ TikZ 프로그램과 ~17만 캡션 샘플 포함 (기존 DaTikZv2 대비 대폭 확대)

3. **성능 우수성**: 
   - TikZero는 AutomaTikZ, AutomaTikZv2 및 다른 엔드-투-엔드 학습 기선을 초과
   - TikZero+는 GPT-4o를 포함한 상용 모델과 주요 지표에서 동등하거나 우수한 성능

4. **효율성**: 어댑터 학습 중 문본 디코더(보통 가장 큰 구성 요소)를 로드할 필요 없음

## How

![Figure 3](figures/fig3.webp)
*Figure 3. TikZero의 아키텍처 개요*

**역 그래픽스 모델 기반**
- VLM(Vision-Language Model) 아키텍처 채용
- 비전 인코더가 이미지 임베딩 생성, 텍스트 디코더가 프로그램 생성
- 래스터화 이미지를 자동회귀적(autoregressive)으로 처리

**어댑터 네트워크 설계**
- 경량 텍스트 인코더: 캡션을 임베딩으로 변환
- 가능한 크로스-어텐션 레이어: 각 비전 인코더 레이어 전 삽입
- 프로브(probe): 이미지 입력 대체, 텍스트 조건 정보 전달
- 게이트 메커니즘: Sigmoid 게이트(초기값 0.5)로 각 레이어의 정보 흐름 제어

**학습 목표 (증류 기반)**
- 거리 함수: $L_{dist} = \frac{1}{|\mathcal{p}|} \sum_{p \in \mathcal{p}} dist(M_\theta(p|i), \tilde{M}_{\theta,\hat{\theta}}(p|\hat{i},t))$
- 원본 모델 파라미터는 완전히 고정(frozen)
- 어댑터 파라미터만 학습
- 코사인 거리 또는 MSE 거리 메트릭 사용

**학습 과정**
1. 비전 인코더로 이미지 패치 임베딩 계산
2. 어댑터를 통해 수정된 인코더 출력 생성
3. 캡션 조건만으로 원본 임베딩과의 증류 손실 최소화

## Originality

- **표현 공간 정렬 패러다임**: 기존 텍스트-투-이미지 생성에서의 글로벌 임베딩 사용과 달리, 패치-레벨 상세 정보에 집중하는 독창적 선택

- **계층별 가능성 게이팅**: Tanh 게이트의 영점 초기화 대신 Sigmoid 게이트를 사용하여 학습 수렴 가속화

- **데이터 활용 효율성**: 정렬되지 않은 다양한 데이터 소스(캡션 래스터 이미지, 그래픽 프로그램)를 독립적으로 활용하는 새로운 전략

- **복합 과학 그래픽 생성**: 단순한 벡터 그래픽이나 제한된 시각화 유형이 아닌, 임의의 과학 그래픽 생성이라는 미탐색 영역 개척

## Limitation & Further Study

- **데이터 품질 의존성**: 어댑터 성능이 캡션 이미지 데이터셋의 품질에 크게 의존 - 도메인 불일치 문제 가능성

- **패치-레벨 정보 필요성**: 어댑터가 비전 인코더의 패치 임베딩 정확히 재현해야 하므로, 패치 구조가 다른 비전 모델로 일반화 어려움

- **복잡한 프로그램 생성**: 현재 평가가 주로 상대적으로 단순한 과학 그래픽에 국한 - 매우 복잡한 상호작용적 그래픽 생성 능력 미검증

- **후속 연구 방향**:
  - 크로스 비전 모델 호환성 개선
  - 프로그램 정확성(컴파일 가능성) 메트릭 강화
  - 대화형 조정 기능 추가
  - 다국어 캡션 지원


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: TikZero는 텍스트 기반 그래픽 프로그램 합성의 데이터 부족 문제를 표현 공간 정렬이라는 우아한 해결책으로 해결하며, 대규모 비정렬 데이터의 활용을 통해 상용 모델과 경쟁할 수 있는 성능을 달성한 점에서 학술적·실무적 가치가 높다. 다만 비전 모델 특화, 복잡한 프로그램 생성의 제한성, 도메인 불일치 가능성 등이 미래 연구의 과제로 남아있다.

## Related Papers

- 🔄 다른 접근: [[papers/129_Automatikz_Text-guided_synthesis_of_scientific_vector_graphi/review]] — 둘 다 텍스트 기반 과학 벡터 그래픽 합성을 다루지만 하나는 TikZ 프로그램 생성에, 다른 하나는 AutomaTikZ를 통한 자동화에 초점을 맞춘다.
- 🔗 후속 연구: [[papers/337_Figgen_Text_to_scientific_figure_generation/review]] — 텍스트에서 과학 도형 생성의 확산 모델 기반 접근법이 TikZero의 TikZ 프로그램 합성과 상호 보완적인 기술을 제공한다.
- 🏛 기반 연구: [[papers/349_Fragment_and_Geometry_Aware_Tokenization_of_Molecules_for_St/review]] — 분자의 기하학적 토크나이제이션 기법이 TikZ 그래픽 프로그램의 구조적 표현 학습에 응용될 수 있는 이론적 기반을 제공한다.
- 🔗 후속 연구: [[papers/129_Automatikz_Text-guided_synthesis_of_scientific_vector_graphi/review]] — TikZero의 제로샷 그래픽 생성을 대규모 TikZ 데이터셋으로 학습한 발전된 버전
- 🔄 다른 접근: [[papers/197_Chartcoder_Advancing_multimodal_large_language_model_for_cha/review]] — 텍스트에서 그래픽 프로그램을 합성하는 TikZero와 유사하게 차트 이미지에서 코드를 생성하는 접근
