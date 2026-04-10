---
title: "337_Figgen_Text_to_scientific_figure_generation"
authors:
  - "J.A. Rodríguez"
  - "David Vázquez"
  - "Issam Laradji"
  - "Marco Pedersoli"
  - "Pau Rodríguez"
date: "2023"
doi: "arXiv:2306.00800"
arxiv: ""
score: 3.5
essence: "텍스트 설명으로부터 과학 논문의 도형(scientific figure)을 생성하는 새로운 문제를 제시하고, 확산 모델(diffusion model) 기반의 FigGen을 제안한 초기 탐색 연구이다. 자연 이미지와 달리 과학 도형은 이산적 컴포넌트(상자, 화살표, 텍스트)와 높은 기술적 복잡성을 포함하므로 새로운 도전과제를 제시한다."
tags:
  - "cat/Scientific_Language_Processing_and_Visualization"
  - "sub/Scientific_Figure_Captioning"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Rodríguez et al._2023_Figgen Text to scientific figure generation.pdf"
---

# Figgen: Text to scientific figure generation

> **저자**: J.A. Rodríguez, David Vázquez, Issam Laradji, Marco Pedersoli, Pau Rodríguez | **날짜**: 2023 | **DOI**: [arXiv:2306.00800](https://arxiv.org/abs/2306.00800)

---

## Essence

![Figure 1](figures/fig1.webp)
*Figure 1: Paper2Fig100k 테스트 셋의 캡션으로부터 생성된 모델의 샘플들*

텍스트 설명으로부터 과학 논문의 도형(scientific figure)을 생성하는 새로운 문제를 제시하고, 확산 모델(diffusion model) 기반의 FigGen을 제안한 초기 탐색 연구이다. 자연 이미지와 달리 과학 도형은 이산적 컴포넌트(상자, 화살표, 텍스트)와 높은 기술적 복잡성을 포함하므로 새로운 도전과제를 제시한다.

## Motivation

- **Known**: 최근 생성형 모델(GAN, 확산 모델)은 자연 이미지와 예술 생성에서 놀라운 성과를 달성했으며, 조건부 이미지 생성 기법들이 발전했다.

- **Gap**: 기존 텍스트-이미지 생성 연구는 자연 이미지 도메인에 집중되어 있으며, 과학 도형과 같은 특화된 영역은 미개척 상태이다.

- **Why**: 자동화된 과학 도형 생성은 연구자들의 시간과 노력을 절감할 수 있고, 접근성 높은 시각화를 통해 더 넓은 청중에게 연구 성과를 전달할 수 있다. 또한 이산적 그래픽 도메인에서의 생성 능력 탐색은 학문적 가치가 높다.

- **Approach**: Paper2Fig100k 데이터셋(논문-도형 쌍 81,194개)을 활용하여 잠재 확산 모델(latent diffusion model)을 훈련하고, 텍스트-도형 간 관계 학습을 시도한다.

## Achievement

![Figure 2](figures/fig2.webp)
*Figure 2: 다양한 Classifier-Free Guidance(CFG) 스케일에서 생성된 FigGenBase 샘플들*

1. **새로운 문제 정의**: 텍스트-과학 도형 생성(text-to-figure generation)을 명확히 정의하고 주요 도전과제(텍스트 길이 가변성, 다양한 도형 스타일, 종횡비 변화, 텍스트 렌더링 품질)를 식별했다.

2. **모델 및 데이터셋 공개**: 코드와 사전 훈련된 모델을 GitHub에 공개하여 커뮤니티의 추가 연구를 지원한다.

3. **기초 모델 구현**: 세 가지 규모의 모델(866M, 942M, 1.2B 파라미터)을 구현하고, 더 큰 텍스트 인코더(128-레이어 BERT)가 더 나은 성능을 제공함을 확인했다(FID: 281.25, CFG=5.0).

## How

- **이미지 인코더(Image Autoencoder)**: 
  - 픽셀 공간을 압축된 잠재 표현(latent space)으로 투영 (downsampling factor f=8)
  - KL 손실, VGG 지각 손실(perceptual loss), OCR 지각 손실 조합으로 학습
  - VQGAN의 적대적 절차(adversarial procedure) 적용으로 복원 품질 향상

- **텍스트 인코더(Text Encoder)**:
  - 기존 일반 목적 텍스트 인코더(CLIP 등)는 기술 문서 도메인 갭이 크므로, BERT를 확산 모델 훈련 중에 동시에 학습
  - 임베딩 채널 크기 512, 교차-주의 계층(cross-attention layers)으로 U-Net 조건화

- **확산 모델(Latent Diffusion Model)**:
  - U-Net 아키텍처로 잠재 공간에서 직접 확산 수행
  - 1000 단계의 선형 노이즈 스케줄(linear noise schedule)
  - 생성 시 DDIM 샘플러 200 단계 사용
  - Classifier-Free Guidance(CFG) 스케일 1.0~10.0으로 조건화 강도 조절

- **데이터 전처리**:
  - 극단적 종횡비 변화 문제 해결을 위해 흰색 패딩 적용
  - 종횡비 0.5~2 범위 내 이미지만 선택 (37,613 훈련, 9,506 검증)
  - 512×512로 처리 후 64×64로 다운샘플링

## Originality

- **새로운 문제 영역**: 과학 도형 생성이라는 미개척 분야를 처음으로 체계적으로 정의하고 연구했다.

- **도메인 특화 설계**: 기술 문서의 특수성을 고려하여 일반 목적 텍스트 인코더 대신 맞춤형 BERT 인코더를 제안했다.

- **손실 함수 조합**: OCR 지각 손실을 포함하여 텍스트 렌더링 품질 유지에 초점을 맞춘 혁신적 접근이다.

- **데이터셋 활용**: Paper2Fig100k라는 새로운 도메인 특화 데이터셋을 활용하여 해당 분야의 실제 요구를 반영했다.

## Limitation & Further Study

- **생성 품질 부족**: 저자들이 명시적으로 언급했듯이, 현재 생성된 도형들은 실제 연구자 사용에는 아직 준비되지 않은 수준이다(FID 282~302).

- **텍스트-이미지 정렬 미흡**: 기술 용어의 복잡성과 다양한 표현으로 인해 텍스트 설명과 시각 표현의 정렬이 불충분하다.

- **평가 지표 부재**: 이산적 객체의 생성 모델에 적합한 검증 지표와 손실 함수 설계가 필요하다. 기존의 FID, IS, KID 등은 자연 이미지용으로 설계되어 도형 생성 평가에 최적이 아니다.

- **텍스트 렌더링**: 도형 내 텍스트의 정확한 렌더링(글꼴, 크기, 방향, 위치)이 여전한 도전과제이다.

- **후속 연구 방향**:
  - 더 큰 규모의 데이터셋 확보 및 다양한 논문 분야 포괄
  - 그래프 신경망(GNN) 등 구조화된 정보 모델링 기법 탐색
  - 도형별 특화 모델 개발(그래프 vs. 아키텍처 vs. 테이블)
  - 가짜 논문 생성 방지를 위한 탐지 및 워터마크 기술 개발

## Evaluation

- **Novelty**: 4/5 - 새로운 문제 정의와 도메인이지만, 기술적으로는 기존 확산 모델의 직접 적용

- **Technical Soundness**: 3/5 - 기본 구현은 견고하지만, 성능이 실용 수준에 미치지 못함

- **Significance**: 3/5 - 중요한 문제를 제시하나, 현재 방법론의 유용성은 제한적

- **Clarity**: 4/5 - 문제 정의와 도전과제가 명확하게 제시됨. Tiny Paper 치고는 양호함

- **Overall**: 3.5/5

**총평**: 본 논문은 과학 도형 자동 생성이라는 미개척 문제를 처음 체계적으로 정의하고 탐색한 선도적 연구로서 학문적 가치가 있다. 다만 현재 기술 수준의 생성 품질이 실용 단계에 미치지 못하며, 도메인의 복잡성(텍스트-이미지 정렬, 이산적 구조 표현)을 완전히 해결하지 못한 초기 단계 연구이다.

## Related Papers

- 🔄 다른 접근: [[papers/601_PaperBanana_Automating_Academic_Illustration_for_AI_Scientis/review]] — 둘 다 AI를 이용한 과학 일러스트레이션 자동화를 다루지만 하나는 확산 모델 기반 과학 도형 생성에, 다른 하나는 학술 일러스트레이션 자동화에 초점을 맞춘다.
- 🔗 후속 연구: [[papers/296_Dynamic_Search_for_Inference-Time_Alignment_in_Diffusion_Mod/review]] — 확산 모델에서 추론 시점 정렬을 위한 동적 검색 기법이 FigGen의 과학 도형 생성 품질 향상에 적용될 수 있다.
- 🏛 기반 연구: [[papers/682_Reward-Guided_Iterative_Refinement_in_Diffusion_Models_at_Te/review]] — 확산 모델에서 보상 기반 반복적 정제 방법이 FigGen의 과학 도형 생성 정확도 개선에 기반을 제공한다.
- 🔗 후속 연구: [[papers/566_Multimodal_deepresearcher_Generating_text-chart_interleaved/review]] — 과학적 그림 생성 기술은 텍스트와 차트 통합 보고서에서 시각화 요소를 더욱 풍부하게 만드는 확장 기술입니다
- 🔄 다른 접근: [[papers/601_PaperBanana_Automating_Academic_Illustration_for_AI_Scientis/review]] — FigGen과 유사하게 텍스트에서 과학 그림 생성하지만 에이전트 기반 접근법 사용
- 🏛 기반 연구: [[papers/129_Automatikz_Text-guided_synthesis_of_scientific_vector_graphi/review]] — 텍스트에서 과학 그림 생성의 기본 아이디어가 TikZ 기반 벡터 그래픽으로 구현됨
- 🔗 후속 연구: [[papers/811_Tikzero_Zero-shot_text-guided_graphics_program_synthesis/review]] — 텍스트에서 과학 도형 생성의 확산 모델 기반 접근법이 TikZero의 TikZ 프로그램 합성과 상호 보완적인 기술을 제공한다.
