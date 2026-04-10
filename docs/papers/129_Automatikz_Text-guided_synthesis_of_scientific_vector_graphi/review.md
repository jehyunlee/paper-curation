---
title: "129_Automatikz_Text-guided_synthesis_of_scientific_vector_graphi"
authors:
  - "Jonas Belouadi"
  - "Anne Lauscher"
  - "Steffen Eger"
date: "2023"
doi: "10.48550/arXiv.2310.00367"
arxiv: ""
score: 4.25
essence: "텍스트 설명으로부터 과학 논문용 벡터 그래픽을 자동으로 생성하기 위해 TikZ라는 추상 그래픽 언어를 중간 표현(intermediate representation)으로 활용하고, 대규모 TikZ 데이터셋(DaTikZ, 120k)을 구축하여 LLaMA와 CLIP 기반 하이브리드 모델(CLiMA)을 개발했다."
tags:
  - "cat/Scientific_Language_Processing_and_Visualization"
  - "sub/Scientific_Graphics_Evaluation"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Belouadi et al._2023_Automatikz Text-guided synthesis of scientific vector graphics with tikz.pdf"
---

# AutomaTikZ: Text-guided synthesis of scientific vector graphics with tikz

> **저자**: Jonas Belouadi, Anne Lauscher, Steffen Eger | **날짜**: 2023 | **DOI**: [10.48550/arXiv.2310.00367](https://doi.org/10.48550/arXiv.2310.00367)

---

## Essence

텍스트 설명으로부터 과학 논문용 벡터 그래픽을 자동으로 생성하기 위해 TikZ라는 추상 그래픽 언어를 중간 표현(intermediate representation)으로 활용하고, 대규모 TikZ 데이터셋(DaTikZ, 120k)을 구축하여 LLaMA와 CLIP 기반 하이브리드 모델(CLiMA)을 개발했다.

## Motivation

- **Known**: DALL-E, Stable Diffusion 등의 텍스트-이미지 생성 모델은 인상적인 결과를 보여주지만 래스터(raster) 형식의 저해상도 그래픽만 생성 가능함. 기존 벡터 그래픽 생성 연구는 저수준 SVG 경로 요소를 직접 생성하려다 기하학적 정확성 부족 또는 제한된 복잡도 문제를 야기함.

- **Gap**: 과학 논문에 적합한 고정밀 벡터 그래픽을 자동으로 생성할 수 있는 방법이 부재함. 특히 텍스트 설명과의 조건부 생성이 가능하면서도 충분한 복잡도를 지원하는 접근법이 없음.

- **Why**: 과학자들은 기하학적 정확성, 선명한 텍스트, 검색 가능한 텍스트 포함, 낮은 파일 크기 등을 요구함. 텍스트 기반 벡터 그래픽 언어(TikZ)는 이러한 요구사항을 만족하면서 고수준의 추상화를 제공함.

- **Approach**: TikZ를 중간 표현으로 활용하여 저수준 그래픽 요소 대신 고수준 프로그래밍 명령어를 생성하도록 함. 대규모 TikZ 데이터셋을 구축하고, 멀티모달 CLIP 임베딩으로 강화된 LLaMA 모델을 개발함.

## Achievement

![Figure 1: CLiMA, LLaMA, CLIP으로 생성한 과학 벡터 그래픽의 예시. 3D 손실함수 등고선도, 다층 퍼셉트론, 막대 그래프 등이 자동 생성됨](figures/fig1.webp)
*그림 1: CLiMA로 생성된 과학 벡터 그래픽 예시*

1. **DaTikZ 데이터셋 구축**: 웹사이트, TeX Stack Exchange, arXiv, GPT-4 생성 데이터 등 다양한 출처에서 수집한 120,789개의 TikZ-캡션 쌍으로 구성된 최초의 대규모 TikZ 데이터셋 창출. 62.71%는 데이터 증강(augmentation) 처리됨.

2. **미세조정 LLaMA 모델 성능 우위**: 자동 평가와 인간 평가 모두에서 DaTikZ로 미세조정된 LLaMA(7B/13B)가 GPT-4와 Claude 2보다 인간이 작성한 그래픽에 더 유사한 결과를 생성함을 입증.

3. **CLiMA 모델의 멀티모달 개선**: CLIP 임베딩으로 증강된 CLiMA는 텍스트-이미지 정렬 성능을 추가로 개선하며, 이미지를 입력으로 사용 가능하게 함으로써 성능 향상을 달성.

4. **일반화 능력 검증**: 모든 모델이 양호한 일반화 성능을 보이며 과도한 암기(memorization) 문제가 없음을 입증. 반면 GPT-4와 Claude 2는 더 단순한 결과를 생성하며 입력 캡션을 그대로 이미지에 복사하는 퇴화된 솔루션(degenerate solution)을 생성하는 경향을 보임.

## How

![Figure 2: 자동 평가 결과 - BLEU, METEOR, ROUGE-L, CIDEr 메트릭에서 모델 간 비교](figures/fig2.webp)
*그림 2: 자동 평가 결과 비교*

**데이터 수집 및 처리**:
- 웹사이트, TeX Stack Exchange (WizardLM으로 캡션 생성), arXiv (정규표현식으로 TikZ 추출), GPT-4 생성 예제 등 다층적 출처에서 수집
- 컴파일 가능성 검증 및 의존성 추출을 통한 품질 보증
- 약 12만 개의 컴파일 실패 사례 제거

**모델 아키텍처**:
- **LLaMA**: DaTikZ에서 직접 미세조정된 기본 모델
- **CLiMA**: LLaMA에 CLIP 비전 인코더와 교차 주의(cross-attention) 메커니즘 추가. 이미지-텍스트 정렬을 개선하고 이미지 기반 조건화 가능

**학습 전략**:
- 인과 언어 모델링(causal language modeling)으로 TikZ 코드 생성 학습
- CLIP 임베딩을 통한 의미적 정보 활용
- GPT-4에서 생성한 예제를 지식 증류(knowledge distillation)로 활용

**평가 방법론**:
- 자동 평가: BLEU, METEOR, ROUGE-L, CIDEr (생성된 코드와 참조 코드 비교)
- 인간 평가: Best-Worst Scaling (BWS)로 캡션 유사도와 참조 유사도 측정
- 일반화 검증: 학습 데이터에 없는 n-gram 비율 측정

## Originality

- **TikZ를 중간 표현으로 활용한 혁신**: 저수준 SVG 경로 대신 고수준 그래픽 언어를 활용하여 기하학적 정확성과 복잡도를 동시에 달성한 최초의 접근
- **대규모 TikZ 데이터셋 창출**: 산학에서 산재된 TikZ 자원을 최초로 체계적으로 수집하여 120k 규모의 구조화된 데이터셋 구축
- **멀티모달 LLM 강화**: CLIP 임베딩과 언어 모델의 효과적인 통합으로 텍스트-이미지 정렬 성능 향상
- **상용 모델과의 정량적 비교**: GPT-4, Claude 2와의 포괄적인 비교를 통해 도메인 특화 미세조정의 우월성 입증

## Limitation & Further Study

**한계점**:
- 자동 생성된 캡션(TeX Stack Exchange)의 품질 편차가 데이터 품질에 영향을 미칠 수 있음
- GPT-4로 생성된 인공 예제가 제한된 객체 범위만 커버하므로 다양성 부족
- TikZ는 과학 그래픽의 표현력 자체에 제약이 있음 (예: 자유로운 그림 스타일 표현 불가)
- 평가가 주로 코드 수준에서 이루어져 최종 렌더링된 그래픽의 시각적 품질 평가가 제한적
- 컴파일 실패율이 높음 (약 50% 이상)

**후속 연구 방향**:
- 더 정교한 캡션 생성 파이프라인으로 데이터 품질 향상
- 더 광범위한 객체 카테고리로 인공 데이터 확대
- 최종 렌더링 이미지에 대한 직접적인 시각적 평가 메트릭 개발
- TikZ 외 다른 그래픽 언어(MetaPost, Asymptote 등)로의 확장
- 사용자 피드백 기반 반복적 개선 메커니즘 구축
- 특정 도메인(생물학, 물리학 등)에 특화된 모델 개발


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 4.5/5
- Overall: 4.25/5

**총평**: 텍스트-벡터 그래픽 생성의 새로운 패러다임을 제시하는 우수한 연구로, 120k 규모의 TikZ 데이터셋과 공개 모델을 제공함으로써 학술 커뮤니티에 실질적 기여를 하고 있다. 다만 데이터 품질 검증 강화와 시각적 평가 방식 개선을 통해 추가 발전 가능성이 있다.

## Related Papers

- 🔄 다른 접근: [[papers/601_PaperBanana_Automating_Academic_Illustration_for_AI_Scientis/review]] — PaperBanana가 AI 과학자 특화인 반면 AutomaTikZ는 일반적인 과학 벡터 그래픽 생성
- 🔗 후속 연구: [[papers/811_Tikzero_Zero-shot_text-guided_graphics_program_synthesis/review]] — TikZero의 제로샷 그래픽 생성을 대규모 TikZ 데이터셋으로 학습한 발전된 버전
- 🔄 다른 접근: [[papers/783_Synchart_Synthesizing_charts_from_language_models/review]] — Synchart가 차트 합성에 특화된 반면 AutomaTikZ는 과학 벡터 그래픽 전반을 다룸
- 🏛 기반 연구: [[papers/337_Figgen_Text_to_scientific_figure_generation/review]] — 텍스트에서 과학 그림 생성의 기본 아이디어가 TikZ 기반 벡터 그래픽으로 구현됨
- 🔄 다른 접근: [[papers/601_PaperBanana_Automating_Academic_Illustration_for_AI_Scientis/review]] — 둘 다 과학 시각화 자동화를 다루지만 PaperBanana는 AI 과학자용, AutomaTikZ는 일반 과학용
- 🔄 다른 접근: [[papers/811_Tikzero_Zero-shot_text-guided_graphics_program_synthesis/review]] — 둘 다 텍스트 기반 과학 벡터 그래픽 합성을 다루지만 하나는 TikZ 프로그램 생성에, 다른 하나는 AutomaTikZ를 통한 자동화에 초점을 맞춘다.
