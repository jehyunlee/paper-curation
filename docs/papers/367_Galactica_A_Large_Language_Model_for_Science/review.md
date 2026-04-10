---
title: "367_Galactica_A_Large_Language_Model_for_Science"
authors:
  - "Ross Taylor"
  - "Marcin Kardas"
  - "Guillem Cucurull"
  - "Thomas Scialom"
  - "Anthony Hartshorn"
date: "2022.11"
doi: "10.48550/arXiv.2211.09085"
arxiv: ""
score: 4.2
essence: "Galactica는 48백만 편의 논문과 과학 자료로 학습된 대규모 언어모델(LLM)로, 과학 지식을 저장·조합·추론하여 정보 과잉 시대의 과학 연구를 지원하는 새로운 인터페이스를 제시한다. 일반 LLM과 달리 엄격히 선별된 과학 코퍼스를 활용하여 LaTeX 방정식, 화학식(SMILES), 단백질 서열 등 다양한 양식을 처리할 수 있다."
tags:
  - "cat/Scientific_Language_Processing_and_Visualization"
  - "sub/Scientific_Language_Models"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Taylor et al._2022_Galactica A Large Language Model for Science.pdf"
---

# Galactica: A Large Language Model for Science

> **저자**: Ross Taylor, Marcin Kardas, Guillem Cucurull, Thomas Scialom, Anthony Hartshorn, Elvis Saravia, Andrew Poulton, Viktor Kerkez, Robert Stojnic | **날짜**: 2022-11-16 | **DOI**: [10.48550/arXiv.2211.09085](https://doi.org/10.48550/arXiv.2211.09085)

---

## Essence

Galactica는 48백만 편의 논문과 과학 자료로 학습된 대규모 언어모델(LLM)로, 과학 지식을 저장·조합·추론하여 정보 과잉 시대의 과학 연구를 지원하는 새로운 인터페이스를 제시한다. 일반 LLM과 달리 엄격히 선별된 과학 코퍼스를 활용하여 LaTeX 방정식, 화학식(SMILES), 단백질 서열 등 다양한 양식을 처리할 수 있다.

## Motivation

- **Known**: 기존 LLM(GPT-3, PaLM, Chinchilla)은 일반 텍스트 코퍼스로 학습되어 과학 지식 작업에서 제한적 성능을 보임. 검색 엔진은 과학 지식을 직접 조직화하지 못하고 Wikipedia, UniProt, PubChem 등 이차 자료에 의존.

- **Gap**: 매일 arXiv에 516편의 논문이 제출되고 NCBI GenBank는 1.49×10¹² 뉴클레오타이드 염기를 보유하는 정보 과잉 시대에, 단순 검색을 넘어 과학 지식을 통합·조직화하고 새로운 연결을 도출할 수 있는 시스템 부재.

- **Why**: 언어모델은 가중치 메모리에 지식을 저장하고 표현 공간을 통해 정보를 연계할 수 있으며, 자동으로 문헌 리뷰나 백과사전 항목 같은 이차 콘텐츠를 생성할 수 있다는 이점 활용 필요.

- **Approach**: 고품질로 선별된 과학 코퍼스(108억 토큰)로부터 특수 토큰 인터페이스(인용문 토큰, 추론 메모리 토큰, 양식 특정 토큰)를 통해 학습하여 과학 작업에 최적화된 LLM 개발.

## Achievement

![Figure 1: 다양한 과학 양식 통합. 단백질 서열이 문서 맥락 내에서 주석과 함께 나타남](figures/fig1.webp)
*표 1: 과학 데이터의 토큰화 - 텍스트, LaTeX, 코드, SMILES, 아미노산 서열, DNA 서열 등을 통합*

1. **기술 지식 작업 우수성**
   - LaTeX 방정식: 68.2% (vs GPT-3 49.0%)
   - 화학 반응 및 IUPAC 이름 예측 우수

2. **추론 작업 성능**
   - 수학 MMLU: 41.3% (vs Chinchilla 35.7%)
   - MATH: 20.4% (120B 모델, vs PaLM 540B 8.8%, 매개변수 18배 적음)

3. **하위 작업(downstream task) 최신 기술(SOTA)**
   - PubMedQA: 77.6%
   - MedMCQA dev: 52.9%
   - BIG-bench: 일반 코퍼스 미학습에도 BLOOM, OPT-175B 초과

4. **새로운 능력 시연**
   - 인용 예측이 스케일에 따라 매끄럽게 증가, 희소/밀집 검색 방식 초과
   - 약감시 학습(weakly-supervised)으로 약물 발견 작업 수행
   - 자감시 학습으로 기능 그룹(functional groups) 같은 해석 가능한 속성 학습

## How

![Figure 2: 작업 맥락에서 "43, 29, 51, 13의 평균은?" 같은 질문에 대해 인간이 내부/외부 작업 메모리를 사용할 수 있음](figures/fig2.webp)

![Figure 3: 모델-기계 공생. <work> 작업 메모리 토큰이 있는 답변 예시](figures/fig3.webp)

- **데이터셋 설계 (표 2)**
  - 논문: 88억 토큰 (83.0%) - 48백만 편
  - 코드: 7억 토큰 (6.9%) - 2백만 파일
  - 참고 자료: 7억 토큰 (6.5%) - 8백만 문서
  - 지식 베이스: 2억 토큰 (2.0%)
  - 필터링된 CommonCrawl: 1억 토큰 (1.0%)
  - 프롬프트: 4천만 토큰 (0.3%)
  - 총 106억 토큰 (고품질, 선별된 코퍼스)

- **특수 토큰 인터페이스**
  - **인용 토큰**: 임의의 입력 맥락에서 인용문 예측 가능
  - **작업 메모리 토큰 (`<work>`)**: 단계별 추론을 래핑하여 내부 작업 메모리 모방
  - **양식 특정 토큰**: SMILES, 단백질 서열을 특수 토큰으로 래핑하여 자연언어 인터페이스 제공

- **반복 토큰 활용**
  - Chinchilla 스케일링 법칙(신선한 토큰만 고려)과 달리, 반복된 토큰으로 학습하여 상류(upstream) 및 하류(downstream) 성능 개선
  - 고품질 큐레이션 데이터셋의 이점 활용

- **마크다운 포맷 통일**
  - 모든 데이터를 공통 마크다운 형식으로 처리하여 소스 간 지식 융합

## Originality

- **과학 특화 LLM의 대규모화**: 기존 SciBERT, BioLM 등은 소규모였으나, Galactica는 108억 토큰의 대규모 과학 코퍼스로 학습한 첫 사례
  
- **다양한 과학 양식의 통합**: 텍스트뿐 아니라 LaTeX, SMILES, 단백질 서열, DNA 서열, 코드를 단일 모델에서 처리하는 멀티모달 접근법
  
- **과학 작업 특화 인터페이스**: 인용, 추론 메모리, 화학식 같은 도메인 특정 토큰을 체계적으로 설계하여 과학 작업 성능 향상
  
- **반복 토큰 활용을 통한 스케일링 법칙 재검토**: Chinchilla 법칙의 "신선한 토큰만" 가정을 도전하여 고품질 데이터셋에서는 반복 학습의 이점 입증
  
- **가중치 메모리 vs 검색의 재평가**: 인용 예측에서 언어모델이 튜닝된 희소/밀집 검색을 초과하여 문서 저장·검색의 패러다임 전환 가능성 제시

## Limitation & Further Study

- **할루시네이션 위험**: 가중치 메모리에 정보를 저장하면 정보 블렌딩 및 거짓 생성의 위험. 신뢰도 개선 방법론 필요

- **지식 업데이트 메커니즘 부재**: 새로운 과학 발견이 모델에 반영되는 방식 미해결. 주기적 재학습 또는 검색 증강(retrieval-augmentation) 결합 필요

- **미세한 지식의 검색 부재**: 특정 단백질 서열이나 외계행성 특성 같은 미세한 지식은 가중치 메모리만으로 부족하므로, 향후 더 큰 모델에서도 검색 증강 필요

- **평가의 한계**: 추론 작업이 여전히 일반 LLM에 비해 절대적으로 낮은 수준(MATH 20.4%). 도메인 특화의 이점이 추론 능력의 부족을 완전히 보상하지 못함

- **일반화 능력의 불명확성**: 과학 텍스트에 최적화되어 일반 작업(BIG-bench)에서 예상 외 성능. 과학과 일반 도메인 간의 트레이드오프 분석 필요

## Evaluation

- **Novelty**: 4.5/5
  - 과학 특화 대규모 LLM의 첫 시도이며 양식 통합, 특수 토큰 인터페이스 등 창의적이나, LLM 아키텍처 자체의 혁신은 미흡

- **Technical Soundness**: 4/5
  - 체계적인 데이터셋 설계와 평가가 강점이나, 반복 토큰의 이론적 근거가 약하고 할루시네이션 위험에 대한 완화 방안 부족

- **Significance**: 4.5/5
  - 과학 커뮤니티에 새로운 인터페이스 제공 가능성이 매우 높고, 가중치 메모리의 가치를 검색에 대비하여 재조명한 점에서 중요도 높음. 다만 신뢰도 개선이 실제 채택의 핵심

- **Clarity**: 4/5
  - 체계적인 구조와 충분한 실험 결과 제시로 읽기 좋으나, 데이터셋 큐레이션 기준과 특수 토큰 설계의 구체적 동작 방식에 대한 상세 설명 부족

- **Overall**: 4.2/5

**총평**: Galactica는 과학 지식 처리를 위해 큐레이션된 데이터와 특화된 인터페이스를 결합한 야심 찬 프로젝트로, 과학 LLM의 가능성을 실질적으로 입증했다. 특히 일반 LLM 대비 기술 지식에서의 우수성과 미리 학습된 프롬프트를 통한 조합 능력은 주목할 만하나, 추론 절대 성능의 한계와 할루시네이션 위험이 실제 과학 커뮤니티 채택의 걸림돌이 될 수 있다. 추후 검색 증강 및 신뢰도 검증 메커니즘과의 결합이 필수적이다.

## Related Papers

- 🔄 다른 접근: [[papers/617_Phi-4_technical_report/review]] — 과학 전문 대규모 모델 Galactica와 달리 Phi-4는 합성 데이터 중심으로 STEM 성능을 달성한 접근
- 🧪 응용 사례: [[papers/780_Surveyforge_On_the_outline_heuristics_memory-driven_generati/review]] — 과학 문헌 생성에 특화된 Galactica의 능력을 자동 설문지 생성에 활용하는 응용
- 🏛 기반 연구: [[papers/707_SciBERT_A_Pretrained_Language_Model_for_Scientific_Text/review]] — 과학 텍스트 사전훈련 모델 SciBERT의 접근을 대규모 과학 지식 모델로 확장한 기반
- 🔗 후속 연구: [[papers/720_Scientific_Large_Language_Models_A_Survey_on_Biological__Che/review]] — 생물학과 화학 분야 과학 언어모델 연구의 포괄적 확장 사례
- 🔄 다른 접근: [[papers/161_BioBERT_a_pre-trained_biomedical_language_representation_mod/review]] — 도메인 특화 사전학습과 범용 과학 언어모델이 각각 전문성과 범용성 측면에서 다른 접근법을 제시한다
- 🔗 후속 연구: [[papers/152_BERT_Pre-training_of_Deep_Bidirectional_Transformers_for_Lan/review]] — BERT의 과학 도메인 확장판으로 1200억 토큰의 과학 논문으로 학습된 대규모 모델
- 🔄 다른 접근: [[papers/707_SciBERT_A_Pretrained_Language_Model_for_Scientific_Text/review]] — SciBERT와 Galactica 모두 과학 텍스트 특화 모델이지만 규모와 접근법이 다름
- 🔗 후속 연구: [[papers/245_Crosslingual_capabilities_and_knowledge_barriers_in_multilin/review]] — 과학 특화 언어모델 Galactica가 다국어 환경에서 겪을 수 있는 교차언어 지식 장벽 분석
- 🔄 다른 접근: [[papers/617_Phi-4_technical_report/review]] — 과학 문헌 기반 Galactica와 달리 합성 데이터 중심 학습으로 STEM 성능을 달성한 접근
- 🧪 응용 사례: [[papers/780_Surveyforge_On_the_outline_heuristics_memory-driven_generati/review]] — 과학 지식에 특화된 Galactica의 능력을 자동 설문지 생성이라는 구체적 작업에 활용
- 🔗 후속 연구: [[papers/467_Large_Language_Models/review]] — 수학/물리학 중심 LLM 설명을 과학 전반의 대규모 언어모델 활용으로 확장한 포괄적 연구입니다.
