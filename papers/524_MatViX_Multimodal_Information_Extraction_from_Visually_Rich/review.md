---
title: "524_MatViX_Multimodal_Information_Extraction_from_Visually_Rich"
authors:
  - "Ghazal Khalighinejad"
  - "Sharon Scott"
  - "Ollie Liu"
  - "Kelly Anderson"
  - "Rickard Stureborg"
date: "2024"
doi: "10.48550/arXiv.2410.20494"
arxiv: ""
score: 4.25
essence: "재료과학 분야의 과학 논문에서 텍스트, 표, 그림에 분산된 구조화된 정보를 추출하는 멀티모달 정보 추출(Multimodal Information Extraction, MIE) 벤치마크를 제시한다. 324개의 전문가 주석 논문과 1,688개의 복잡한 구조화된 JSON 파일로 구성된 MATVIX 데이터셋을 소개하며, 비전-랭귀지 모델(Vision-Language Models, VLMs)의 성능을 평가한다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Publication_Concept_Extraction"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Khalighinejad et al._2024_MatViX Multimodal Information Extraction from Visually Rich Articles.pdf"
---

# MatViX: Multimodal Information Extraction from Visually Rich Articles

> **저자**: Ghazal Khalighinejad, Sharon Scott, Ollie Liu, Kelly Anderson, Rickard Stureborg | **날짜**: 2024 | **DOI**: [10.48550/arXiv.2410.20494](https://doi.org/10.48550/arXiv.2410.20494)

---

## Essence

![Figure 1](figures/fig1.webp) *그림 1: 텍스트와 그림 간의 상호연결된 데이터를 포함하는 논문의 예시 및 샘플 특성과 구성 세부사항을 캡처하는 JSON 구조*

재료과학 분야의 과학 논문에서 텍스트, 표, 그림에 분산된 구조화된 정보를 추출하는 멀티모달 정보 추출(Multimodal Information Extraction, MIE) 벤치마크를 제시한다. 324개의 전문가 주석 논문과 1,688개의 복잡한 구조화된 JSON 파일로 구성된 MATVIX 데이터셋을 소개하며, 비전-랭귀지 모델(Vision-Language Models, VLMs)의 성능을 평가한다.

## Motivation

- **Known**: 기존의 FUNSD, CORD, Kleister 등 문서 분석 데이터셋들은 복잡한 레이아웃과 긴 문서를 다루지만, 단순 개체명 인식(NER) 수준의 작업에 국한되며 과학 문서의 멀티모달 특성을 고려하지 않음. PNCExtract는 전체 길이 논문을 다루지만 텍스트만 대상으로 함.

- **Gap**: 과학 논문에서 텍스트, 표, 그림에 걸쳐 분산된 복잡한 N-ary 관계 추출(N-ary relation extraction)을 수행하는 진정한 멀티모달 벤치마크가 부재. 특히 재료과학에서 그림의 곡선(curves)과 텍스트 간의 상호연결 정보 추출이 어려움.

- **Why**: 재료과학에서 구조화된 정보 추출은 새로운 재료 발견을 가속화할 수 있으며, GNoME와 같은 도구들이 이를 입증. 그러나 장문 문서의 토큰 제한(BERT의 512 토큰 한계)과 계층적 JSON 생성의 복잡성으로 기존 방법들이 부적합.

- **Approach**: 장문 컨텍스트를 처리 가능한 VLMs를 제로샷(zero-shot) 방식으로 벤치마킹하고, Fréchet 거리를 이용한 곡선 유사도 평가 방법을 제안. DePlot 같은 전문화된 모델과의 조합도 검토.

## Achievement

![Figure 2](figures/fig2.webp) *그림 2: 그림과 해당 샘플의 예시. 특성의 데이터 포인트들이 그림에서 추출됨을 보여줌*

1. **포괄적 벤치마크 구축**: 고분자 나노복합재료(PNC) 231개, 생분해 고분자(PBD) 93개 총 324개의 전체 길이 과학 논문에서 1,688개의 구조화된 JSON 파일 생성. 평균 8,905 토큰의 장문 문서 포함.

2. **멀티모달 평가 방법론 개발**: 구성(composition)을 기반으로 샘플 정렬 후, Fréchet 거리를 통해 예측과 실제 곡선의 유사도 측정. 계층적 구조 정렬 평가 방법 제시로 단순 개체 인식 이상의 복잡성 반영.

3. **VLM 성능 분석**: GPT-4o 등 최신 비전-랭귀지 모델들의 제로샷 성능을 벤치마킹하고, DePlot(도표→표 변환) 모델과의 결합으로 그림 추출 성능 개선 가능성 입증. 현재 모델의 상당한 개선 여지 확인.

## How

![Figure 3](figures/fig3.webp) *그림 3: BaTiO3 나노복합재료에서 손실 탄젠트의 감소와 유전 상수의 증가를 보여주는 예시*

- **데이터 수집 및 정제**: NanoMine 저장소의 불일치한 XML 기반 데이터를 표준화하여 JSON 형식으로 변환. 43개 속성을 6개 주요 특성(열적, 전기적, 기계적, 점탄성, 부피적, 유변학적)으로 범주화.

- **PNC 샘플 정의**: 각 샘플을 성분(matrix, filler) 및 특성(properties) 섹션으로 구성된 구조화된 JSON 객체로 표현. 수치 데이터는 실험 조건(헤더)과 함께 기록.

- **PBD 샘플 수집**: 재료과학 전문가 2인이 93개 논문을 선별하고, 1인이 추출 후 1인이 검증하는 이중 검증 체계 적용.

- **계층적 구조 추출**: 단순 개체명 인식을 넘어 N-ary 관계 추출로 재료 구성 요소 간의 복잡한 상호작용을 포착.

- **곡선 유사도 평가**: Fréchet 거리를 이용하여 예측 곡선과 실제 곡선 간 전체 추세의 유사성 측정. 기존의 정확도(accuracy) 기반 평가의 한계 극복.

## Originality

- **첫 멀티모달 과학 문서 벤치마크**: 텍스트, 표, 그림 모두를 포함하면서 동시에 N-ary 관계 추출을 요구하는 첫 번째 과학 도메인 데이터셋. 기존 데이터셋들(FUNSD, CORD, PolyIE, PNCExtract)은 이러한 조건을 동시에 만족하지 못함.

- **도메인 특화 평가 메트릭**: 곡선 데이터에 대한 Fréchet 거리 기반 평가와 계층적 구조 정렬 평가로, 단순 엔티티 매칭을 넘어 복잡한 과학 데이터의 의미론적 정확성 측정.

- **장문 컨텍스트 처리**: 512 토큰 제한의 BERT 기반 모델들을 벗어나 평균 8,905 토큰의 전체 논문을 한 번에 처리하는 VLM 기반 접근.

- **전문가 주석**: PNC는 NanoMine 저장소 기반이지만 재료과학 전문가에 의해 검증되었으며, PBD는 완전한 전문가 이중 검증 체계로 높은 품질 보장.

## Limitation & Further Study

- **제한된 도메인 범위**: 고분자 나노복합재료와 생분해 고분자 두 가지 영역에만 국한. 재료과학의 다른 중요 분야(세라믹, 금속, 반도체)로의 확장 부재.

- **현재 모델의 낮은 성능**: 벤치마킹 결과 VLMs의 성능이 여전히 충분하지 않으며, 특히 복잡한 계층적 구조 추출에서 개선 필요.

- **DePlot의 제한성**: DePlot 모델과의 조합이 일부 개선을 보이나, 복잡한 멀티플롯(multi-plot) 그림이나 비표준 그래프 형식에 대한 처리 능력 미흡.

- **후속 연구 방향**:
  - 장문 문서의 멀티모달 이해를 위한 전문화된 아키텍처 개발
  - 과학 도메인 특화 사전학습(pre-training) 모델 개발
  - 추론 시간 계산량 최적화로 실용적 적용성 개선
  - 다양한 과학 분야로 확장 가능한 범용 추출 프레임워크 구축


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4/5
- Significance: 4.5/5
- Clarity: 4/5
- Overall: 4.25/5

**총평**: 멀티모달 과학 문서 정보 추출이라는 명확한 공백을 채우며 체계적으로 설계된 벤치마크를 제공하는 점에서 높은 가치가 있으나, 제한된 도메인 범위와 현재 모델의 낮은 성능 그 자체가 개선의 긴급성을 보여주는 과제이다.

## Related Papers

- 🔗 후속 연구: [[papers/564_Multi-llm_collaborative_caption_generation_in_scientific_doc/review]] — 다중 LLM 협업 캡션 생성이 MatViX의 멀티모달 정보 추출을 과학 문서의 시각적 요소 설명 생성으로 확장한 구체적 응용 연구임
- 🏛 기반 연구: [[papers/708_SciCap_Generating_Captions_for_Scientific_Figures/review]] — 과학 그림을 위한 캡션 생성 기술이 재료과학 논문의 복잡한 시각적 정보를 구조화된 텍스트로 변환하는 MatViX 시스템의 핵심 구성 요소를 제공함
- 🔄 다른 접근: [[papers/336_FigCaps-HF_A_Figure-to-Caption_Generative_Framework_and_Benc/review]] — FigCaps-HF의 그림-캡션 생성 프레임워크가 MatViX의 멀티모달 추출과 다른 접근법으로 과학 문서의 시각적 정보를 처리하는 상호 보완적 방법론임
- 🔄 다른 접근: [[papers/062_Agent-based_multimodal_information_extraction_for_nanomateri/review]] — nanoMINER와 MatViX는 모두 과학 논문에서 구조화된 정보 추출을 다루지만, 나노물질 특화와 시각적 정보 처리라는 서로 다른 초점을 가집니다.
