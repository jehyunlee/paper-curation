---
title: "601_PaperBanana_Automating_Academic_Illustration_for_AI_Scientis"
authors:
  - "Dawei Zhu"
  - "Rui Meng"
  - "Yale Song"
  - "Xiyu Wei"
  - "Sujian Li"
date: "2026.01"
doi: "10.48550/arXiv.2601.23265"
arxiv: ""
score: 4.3
essence: "본 논문은 자율 AI 과학자(Autonomous AI Scientists)의 시각화 병목을 해결하기 위해, 에이전트 기반 프레임워크 PaperBanana를 제안한다. 이는 VLM(Vision Language Model)과 이미지 생성 모델을 활용하여 학술 출판 기준을 충족하는 다이어그램과 플롯을 자동으로 생성한다."
tags:
  - "cat/Scientific_Language_Processing_and_Visualization"
  - "sub/Scientific_Figure_Captioning"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Zhu et al._2026_PaperBanana Automating Academic Illustration for AI Scientists.pdf"
---

# PaperBanana: Automating Academic Illustration for AI Scientists

> **저자**: Dawei Zhu, Rui Meng, Yale Song, Xiyu Wei, Sujian Li, Tomas Pfister, Jinsung Yoon | **날짜**: 2026-01-30 | **DOI**: [10.48550/arXiv.2601.23265](https://doi.org/10.48550/arXiv.2601.23265)

---

## Essence

![Figure 1: PaperBanana가 생성한 방법론 다이어그램과 통계 플롯 예시](figures/fig1.webp)
*그림 1: PaperBanana가 생성한 방법론 다이어그램과 통계 플롯의 예시로, 학술 일러스트레이션 생성 자동화의 잠재력을 보여줌*

본 논문은 자율 AI 과학자(Autonomous AI Scientists)의 시각화 병목을 해결하기 위해, 에이전트 기반 프레임워크 PaperBanana를 제안한다. 이는 VLM(Vision Language Model)과 이미지 생성 모델을 활용하여 학술 출판 기준을 충족하는 다이어그램과 플롯을 자동으로 생성한다.

## Motivation

- **Known**: 대규모 언어 모델(LLM) 기반의 자율 AI 과학자가 문헌 검토, 아이디어 생성, 실험 반복 등 연구 생명주기의 많은 부분을 자동화할 수 있게 되었다.

- **Gap**: 현재 자율 AI 과학자들은 텍스트 분석과 코드 실행에는 능숙하지만, 학술 출판 기준을 충족하는 다이어그램과 플롯 같은 시각화 자료 생성에는 여전히 어려움을 겪고 있다. 기존 코드 기반 방법(TikZ, SVG)은 구조화된 내용에는 효과적이나 현대 AI 논문의 복잡한 시각 요소(맞춤형 아이콘, 특수한 형태)를 표현하는 데 한계가 있다.

- **Why**: 전문 일러스트레이션 도구의 사용법이 복잡하고, 연구자들이 고품질의 논문 그림을 만드는 데 상당한 시간과 노력을 투자해야 하므로, 이는 과학 발견의 효율적인 시각적 소통을 방해하는 주요 병목이다.

- **Approach**: 참조(reference) 기반의 협업 워크플로우를 설계하여, 검색(Retriever), 계획(Planner), 스타일 적용(Stylist), 시각화(Visualizer), 비판(Critic) 5개의 특화된 에이전트를 조율하고, 자기 비판을 통한 반복적 정제(iterative refinement)로 출판 기준을 충족하는 일러스트레이션을 생성한다.

## Achievement

![Figure 2: PaperBanana 프레임워크 개요](figures/fig2.webp)
*그림 2: 선형 계획 단계와 반복 정제 루프로 구성된 PaperBanana의 전체 아키텍처*

1. **벤치마크 구축**: NeurIPS 2025 논문에서 수집한 292개의 방법론 다이어그램 테스트 케이스와 292개의 참조 사례로 구성된 PaperBananaBench를 구축하여, 학술 일러스트레이션 평가를 위한 체계적 기준을 제공한다.

2. **성능 우수성**: 충실성(+2.8%), 간결성(+37.2%), 가독성(+12.9%), 미학성(+6.6%)의 모든 차원에서 기존 기법을 능가하며, 종합 점수에서 +17.0%의 개선을 달성한다.

3. **다중 작업 확장성**: 방법론 다이어그램뿐 아니라 통계 플롯 생성으로도 성공적으로 확장되며, Python Matplotlib 코드 생성 방식으로 수치 정확도를 보장한다.

## How

![Figure 3: PaperBananaBench 통계](figures/fig3.webp)
*그림 3: PaperBananaBench 테스트 셋의 통계 (총 292개 샘플, 평균 원본 문맥 길이 3,020.1 단어, 그림 캡션 70.4 단어)*

### 다섯 에이전트 협업 메커니즘

- **Retriever Agent**: 입력된 원본 내용(S)과 의사 소통 의도(C)로부터 참조 세트 R에서 관련성 높은 N개의 예시 E를 선택. VLM 기반의 생성적 검색(generative retrieval) 방식으로 연구 도메인 및 다이어그램 유형의 매칭도를 평가하며, 시각 구조 유사성을 우선시한다.

- **Planner Agent**: 검색된 예시들의 in-context learning을 통해 비구조화된 원본 내용을 정교한 텍스트 설명 P로 변환. 논리적 흐름과 구조적 일관성을 보장한다.

- **Stylist Agent**: 참조 컬렉션 전체를 순회하여 색상 팔레트, 도형, 화살표, 레이아웃, 타이포그래피 등을 아우르는 학술 스타일 가이드라인 G를 자동 합성. 초기 설명 P를 미학적으로 최적화된 버전 P*로 정제한다.

- **Visualizer-Critic 루프**: Visualizer가 최적화된 설명 P*를 이미지 생성 모델로 변환(I_t = Image-Gen(P_t)). Critic이 생성된 이미지를 원본 내용(S, C)과 대조하여 사실적 불일치, 시각적 오류를 식별하고 개선된 설명 P_{t+1}을 생성. T=3 라운드 동안 반복 수행하여 최종 출력 I = I_T 생성.

- **통계 플롯 확장**: Visualizer가 Python Matplotlib 코드로 변환(I_t = VLM_code(P_t))하여 수치 정확성을 확보하고, Critic이 렌더링된 플롯을 평가하여 부정확성을 해결한다.

### 평가 방법론

- VLM-as-a-Judge 접근법으로 인간이 생성한 일러스트레이션 대비 충실성, 간결성, 가독성, 미학성의 4가지 차원에서 참조 기반 점수 부여. 인간 평가와의 상관관계로 신뢰도 검증.

## Originality

- **에이전트 협업 아키텍처**: 다섯 개의 특화된 에이전트를 체계적으로 조율하는 방식은 기존 단일 모델 기반 접근과 차별화되며, 참조 기반 학습으로 스타일과 논리 모두를 향상시킨다.

- **학술 스타일 자동 합성**: 참조 컬렉션으로부터 미학적 가이드라인을 자동 추출하는 방식은 수동 정의의 불완전성을 극복하고 확장성을 제공한다.

- **통합 벤치마크**: 최신 NeurIPS 논문에서 수집한 292개 사례로 구성된 PaperBananaBench는 학술 일러스트레이션 평가를 위한 최초의 체계적 벤치마크이다.

- **다중 모드 작업 지원**: 방법론 다이어그램(이미지 생성)과 통계 플롯(코드 생성)을 통합 프레임워크로 지원하는 유연성.

## Limitation & Further Study

- **이미지 생성 모델 의존성**: 최신 VLM과 이미지 생성 모델의 성능에 크게 의존하므로, 이들 모델의 발전에 따라 성능이 변동할 수 있다.

- **복잡한 다이어그램 한계**: 매우 높은 수준의 예술적 표현이 필요하거나 도메인 특화 기호가 많은 다이어그램의 경우 여전히 수동 조정이 필요할 수 있다.

- **계산 비용**: 5개 에이전트의 협업과 3라운드의 반복 정제는 상당한 API 호출을 수반하므로, 대규모 자동화 시나리오에서 실용성 검토가 필요하다.

- **후속 연구**: (1) 기존 인간 생성 일러스트레이션을 개선하는 데 프레임워크 활용, (2) 통계 플롯 생성에서 이미지 생성 모델의 직접 활용 가능성 탐구, (3) 다른 학문 분야(과학, 공학 등)로의 일반화.

## Evaluation

- **Novelty**: 4.5/5
  - 에이전트 협업 아키텍처와 참조 기반 학습은 창의적이나, 개별 기법들은 기존 방법의 조합에 가깝다.

- **Technical Soundness**: 4/5
  - 전반적으로 견고한 방법론이나, 벤치마크 필터링 기준(aspect ratio 제한)이 다소 제한적이며, VLM-as-a-Judge의 신뢰도 분석이 더 상세할 필요가 있다.

- **Significance**: 4.5/5
  - 자율 AI 과학자의 시각화 병목을 직접 해결하는 실질적 기여이며, 새로운 벤치마크 제공으로 후속 연구 활성화 가능성이 높다.

- **Clarity**: 4/5
  - 전반적으로 명확하게 작성되었으나, 각 에이전트의 프롬프트 설계 철학이 주문(Appendix)으로 미루어져 본문의 완결성이 다소 떨어진다.

- **Overall**: 4.3/5

**총평**: PaperBanana는 자율 AI 과학자의 중요한 약점인 시각화 자동화를 체계적으로 해결하는 실용적이고 잘 설계된 솔루션으로, 새로운 벤치마크와 함께 학술 커뮤니티에 의미 있는 기여를 제공한다. 다만 개별 기법의 창의성과 모델 의존성에 대한 보완이 있으면 더욱 강력한 논문이 될 수 있다.

## Related Papers

- 🔄 다른 접근: [[papers/129_Automatikz_Text-guided_synthesis_of_scientific_vector_graphi/review]] — 둘 다 과학 시각화 자동화를 다루지만 PaperBanana는 AI 과학자용, AutomaTikZ는 일반 과학용
- 🔗 후속 연구: [[papers/336_FigCaps-HF_A_Figure-to-Caption_Generative_Framework_and_Benc/review]] — FigCaps-HF의 캡션 생성을 넘어 전체 다이어그램과 플롯을 자동 생성하는 발전된 시스템
- 🔄 다른 접근: [[papers/337_Figgen_Text_to_scientific_figure_generation/review]] — FigGen과 유사하게 텍스트에서 과학 그림 생성하지만 에이전트 기반 접근법 사용
- 🔗 후속 연구: [[papers/597_P2p_Automated_paper-to-poster_generation_and_fine-grained_be/review]] — P2P의 포스터 생성 기술을 학술 논문의 전체 일러스트레이션으로 확장
- 🔗 후속 연구: [[papers/600_Paper2Web_Lets_Make_Your_Paper_Alive/review]] — 논문 일러스트레이션 자동화를 전체 웹사이트 변환으로 확장한 발전된 형태
- 🔄 다른 접근: [[papers/129_Automatikz_Text-guided_synthesis_of_scientific_vector_graphi/review]] — PaperBanana가 AI 과학자 특화인 반면 AutomaTikZ는 일반적인 과학 벡터 그래픽 생성
- 🔄 다른 접근: [[papers/337_Figgen_Text_to_scientific_figure_generation/review]] — 둘 다 AI를 이용한 과학 일러스트레이션 자동화를 다루지만 하나는 확산 모델 기반 과학 도형 생성에, 다른 하나는 학술 일러스트레이션 자동화에 초점을 맞춘다.
