---
title: "552_Mmsci_A_dataset_for_graduate-level_multi-discipline_multimod"
authors:
  - "Zekun Li"
  - "Xianjun Yang"
  - "Kyuri Choi"
  - "Wanrong Zhu"
  - "Ryan Hsieh"
date: "2024"
doi: "N/A"
arxiv: ""
score: 4.2
essence: "본 논문은 Nature Communications의 동료평가 논문 131,393개로부터 742,273개의 이미지를 수집하여, 72개 학문 분야의 대학원 수준 복잡한 과학 시각화를 이해하기 위한 대규모 멀티모달 데이터셋(MMSCI)을 제시한다. 이를 통해 19개 언어비전모델(Large Vision Language Models, LVLMs)을 평가하며, 미세 조정 및 사전 학습을 통해 모델 성능을 향상시킬 수 있음을 보여준다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/Multimodal_Scientific_Reasoning"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Wu et al._2024_Mmsci A dataset for graduate-level multi-discipline multimodal scientific understanding.pdf"
---

# MMSCI: A dataset for graduate-level multi-discipline multimodal scientific understanding

> **저자**: Zekun Li, Xianjun Yang, Kyuri Choi, Wanrong Zhu, Ryan Hsieh, HyeonJung Kim, Jin Hyuk Lim, Sungyoung Ji, Byungju Lee, Xifeng Yan, Linda Ruth Petzold, Stephen D. Wilson, Woosang Lim, William Yang Wang | **날짜**: 2024 | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp)
*그림 1: MMSCI 데이터셋의 상위 20개 과학 분야별 논문 수와 이미지 수*

본 논문은 Nature Communications의 동료평가 논문 131,393개로부터 742,273개의 이미지를 수집하여, 72개 학문 분야의 대학원 수준 복잡한 과학 시각화를 이해하기 위한 대규모 멀티모달 데이터셋(MMSCI)을 제시한다. 이를 통해 19개 언어비전모델(Large Vision Language Models, LVLMs)을 평가하며, 미세 조정 및 사전 학습을 통해 모델 성능을 향상시킬 수 있음을 보여준다.

## Motivation

- **Known**: 최근 LVLMs는 시각적 문맥을 포함한 문제 해결에서 뛰어난 능력을 보이고 있으며, 이들은 과학 분야의 AI 어시스턴트로서 큰 잠재력을 가지고 있다.

- **Gap**: 기존 과학 이미지 이해 데이터셋들(FigureQA, SciCap, SciFiBench 등)은 막대 그래프, 산점도 등 단순한 차트에만 초점을 맞추고 있으며, 제한된 과학 분야(주로 컴퓨터 과학)만 다루고 있다. 현미경 사진, 분광법 이미지, 3D 모델, 분자 구조 등 복잡한 과학 시각화를 해석하려면 대학원 수준의 도메인 전문 지식이 필요하나 이를 평가할 데이터셋이 부족하다.

- **Why**: 과학 논문의 도형들은 압축되고 복잡한 정보를 담고 있으며, 전문적 해석이 필수적이다. 이를 효과적으로 평가할 수 있는 포괄적 데이터셋과 벤치마크가 필요하다.

- **Approach**: 동료평가된 Nature Communications 논문에서 고품질 이미지와 메타데이터를 수집하고, 다양한 시각화 유형을 포함하는 포괄적 데이터셋을 구축한다. 도형 설명(figure captioning)과 다지선다형 질문(multiple-choice questions) 벤치마크를 구성하여 LVLMs와 인간 전문가의 성능을 비교 평가한다.

## Achievement

![Figure 2](figures/fig2.webp)
*그림 2: MMSCI의 7가지 이질적 과학 이미지 유형 예시 (정량적 데이터 시각화 53.5%, 개략도 13.2%, 현미경 사진 14.7% 등)*

1. **포괄적 데이터셋 구축**: 72개 과학 분야, 131,393개 논문, 742,273개 이미지로 구성된 대규모 고품질 멀티모달 데이터셋 구축. 기존 데이터셋(주로 CS 분야)과 달리 자연과학 전반을 폭넓게 커버하며 다양한 시각화 유형 포함

2. **어려운 벤치마크 과제 개발**: 도형 설명과 다지선다형 질문 과제 설계로, 다수의 오픈소스 모델이 무작위 추측 수준 이하의 성능을 보이는 등 과제의 난이도와 현재 모델의 한계를 명확히 드러냄

3. **LVLM 성능 평가 및 기준선 제시**: GPT-4o와 Claude-3.5-Sonnet이 최고 성능 모델이며, 일부 경우 도메인 전문가를 초과하는 성능을 달성함을 확인. 미세 조정된 Qwen2-VL-7B이 다지선다형 문제에서 GPT-4o 성능을 상회

4. **훈련 자원으로서의 가치 입증**: 과제 특화 데이터로 미세 조정 시 성능 향상 달성, 그리고 기사와 이미지의 인터리브(interleaved) 데이터로 사전 학습 시 재료과학 등 하위 과제에서 성능 개선 확인

## How

![Figure 3](figures/fig3.webp)
*그림 3: 부-도형 캡션 추출의 예시와 벤치마크 데이터 구성*

- **데이터 수집**: Nature Communications 웹사이트에서 개방 접근(open-access), 동료평가 논문의 제목, 초록, 본문, 참고문헌, 도형, 캡션을 체계적으로 수집

- **데이터 정제 및 처리**: 
  - LaTeX 수식을 평문으로 변환 (pylatexenc 사용)
  - 정규표현식을 활용한 부-도형 캡션 자동 추출 (514,054개 부-도형/도형 식별)
  - GPT-4o를 이용한 벤치마크 테스트셋의 이미지 분류

- **도형 분류**: 7가지 주요 범주로 수작업 분류 후 자동화 (정량적 데이터 시각화, 개략도, 현미경 사진, 모의 이미지, 지도, 육안 사진, 실험 결과 시각화)

- **벤치마크 과제 설계**: 
  - 도형 설명(captioning) 과제: 도형에 대한 상세한 설명 생성
  - 다지선다형 질문(MCQ) 과제: 도형 해석에 기반한 4지선다형 문제 풀이

- **평가 방법론**: 
  - 19개 LVLM 모델 평가 (독점 모델: GPT-4o, Claude 시리즈 등 / 오픈소스: Qwen2-VL, MiniCPM-V 등)
  - 인간 전문가(도메인 박사) 평가를 통한 성능 비교
  - 자동 평가 지표(BLEU, CIDEr, METEOR 등 사용)

- **훈련 응용**:
  - 과제 특화 감독 미세 조정(SFT) 데이터 구축: MCQ 데이터를 지시 따르기(instruction-following) 형식으로 변환
  - 인터리브 논문-도형 데이터 구축: 기사 본문과 도형을 교대로 배열하여 연속 사전 학습 수행

## Originality

- **도메인 광범위성**: 기존 CS/수학 중심에서 벗어나 물리학, 화학, 생물학, 재료과학 등 72개 다양한 과학 분야 포괄. 이는 초학문적(cross-disciplinary) LVLM 평가를 가능하게 함

- **시각화 유형 다양성**: 단순 차트를 넘어 현미경 이미지, 3D 모델, 분자 구조, 스펙트로그램, 히트맵 등 7가지 이질적 시각화 유형 포함으로 현실적인 과학 논문의 복잡성 반영

- **고품질 소스**: 비동료평가 arXiv 논문 대신 Nature Communications의 동료평가 논문만 사용하여 데이터 신뢰성 확보

- **규모와 자동화**: 부-도형 캡션 자동 추출(514,054개) 및 이미지 분류 자동화로 대규모 데이터셋 구축 효율성 증대

- **훈련 자원화**: 단순 벤치마크를 넘어 미세 조정 및 사전 학습용 구조화된 데이터 제공으로 모델 개선 경로 제시

## Limitation & Further Study

- **시각적 설명의 어려움**: 모든 모델이 정확한 도형 캡션 생성에 어려움을 보임. 특히 세밀한 의미(nuanced semantics) 포착 부족이 지속적 도전 과제

- **도메인별 성능 격차**: 특정 과학 분야(예: 재료과학)에서는 성능 향상이 명확하지만, 다른 분야에서는 개선 정도가 미흡한 점이 있어 분야별 맞춤형 접근 필요

- **인간 평가의 한계**: 인간 전문가 평가도 완벽하지 않으며, 분야별로 평가자 간 동의도(inter-annotator agreement) 차이가 있을 수 있음

- **일반화 성능**: Nature Communications 데이터로 훈련된 모델이 다른 출판사 논문이나 비영어 과학 논문에 대한 일반화 성능은 평가되지 않음

**후속 연구 방향**:
- 비영어 과학 논문 포함으로 다언어 과학 이해 능력 개선
- 도메인별 특화 모델 개발
- 멀티모달 과학 문제 해결(multimodal science problem solving) 과제 확장
- 도형과 텍스트의 더욱 정교한 상호작용(interaction) 모델링

## Evaluation

- **Novelty (혁신성): 4.5/5**
  - 과학 분야의 포괄성과 다양한 시각화 유형 포함은 기존 데이터셋 대비 명확한 진전
  - 다만 벤치마크 과제 자체(captioning, MCQ)는 기존 방식의 조합

- **Technical Soundness (기술 건전성): 4/5**
  - 데이터 수집 및 처리 방법이 체계적이고 명확함
  - 정규표현식 기반 부-도형 추출, GPT-4o 기반 분류는 합리적 접근
  - 다만 자동 분류의 정확성 검증 세부사항 부족

- **Significance (중요성): 4.5/5**
  - 고품질 대규모 멀티모달 데이터셋으로 과학 AI 분야에 실질적 기여
  - 미세 조정 및 사전 학습을 통한 실제 성능 향상 입증
  - 도메인 전문가와 경쟁하는 수준의 모델 성능은 응용 가치 높음

- **Clarity (명확성): 4/5**
  - 데이터셋 구성, 벤치마크 설계, 평가 방법이 체계적으로 설명됨
  - 도형 예시(Figure 2)가 시각화 유형을 명확히 제시
  - 다만 일부 통계 정보(예: 도형 크기 분포, 캡션 길이 통계)가 추가되면 더 명확할 것

- **Overall (종합): 4.2/5**

**총평**: MMSCI는 과학 분야의 복잡한 멀티모달 이해를 다루는 대규모 고품질 데이터셋으로, 기존 차트 중심 벤치마크의 한계를 극복하고 다양한 도메인의 graduate-level 시각화 해석을 가능하게 한다. 실제 미세 조정과 사전 학습을 통한 성능 향상을 입증함으로써 과학 AI 어시스턴트 개발의 중요한 기반을 제공하며, 특히 도메인 전문가 수준의 모델 성능 달성은 실무적 가치를 입증한다.

## Related Papers

- 🔄 다른 접근: [[papers/737_Sciverse_Unveiling_the_knowledge_comprehension_and_visual_re/review]] — 둘 다 과학 멀티모달 벤치마크를 제공하지만 MMSCI는 대학원 수준 복잡성에, SCIVERSE는 세밀한 능력 평가에 집중함
- 🏛 기반 연구: [[papers/551_MMC_Advancing_Multimodal_Chart_Understanding_with_Large-scal/review]] — MMC의 차트 이해 기술이 MMSCI의 과학 시각화 데이터 처리 방법론의 핵심 구성요소임
- 🔗 후속 연구: [[papers/713_Scicueval_A_comprehensive_dataset_for_evaluating_scientific/review]] — 대학원 수준의 다학제 멀티모달 과학 데이터셋은 SciCUEval의 과학적 맥락 이해를 더욱 고도화한 벤치마크입니다
- 🔗 후속 연구: [[papers/706_SciBench_Evaluating_College-Level_Scientific_Problem-Solving/review]] — 대학 수준 과학 문제를 대학원 수준 멀티모달 과학으로 확장한다.
- 🔄 다른 접근: [[papers/737_Sciverse_Unveiling_the_knowledge_comprehension_and_visual_re/review]] — 둘 다 과학 멀티모달 평가를 위한 벤치마크이지만 SCIVERSE는 세밀한 능력 분석에, MMSCI는 대규모 데이터 수집에 집중함
- 🧪 응용 사례: [[papers/055_Advancing_multimodal_medical_capabilities_of_gemini/review]] — Med-Gemini의 의료 멀티모달 역량이 MMSCI 데이터셋의 생명과학 분야 벤치마크 평가에 직접 적용됨
- 🏛 기반 연구: [[papers/261_Deepresearch_bench_A_comprehensive_benchmark_for_deep_resear/review]] — 대학원 수준 다중 분야 다중모달 데이터세트가 연구 벤치마크의 기반 제공
- 🔗 후속 연구: [[papers/1106_The_BOS-Lig_Dataset_Accurate_Ligand_Charges_from_a_Consensus/review]] — 대학원 수준 다학제 다중모달 과학 데이터셋으로 본 논문의 화학 데이터를 더 광범위한 과학 도메인으로 확장한다.
