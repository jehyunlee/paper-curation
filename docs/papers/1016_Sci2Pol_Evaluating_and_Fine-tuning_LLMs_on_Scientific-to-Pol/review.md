---
title: "1016_Sci2Pol_Evaluating_and_Fine-tuning_LLMs_on_Scientific-to-Pol"
authors:
  - "Weimin Wu"
  - "Alexander C. Furnas"
  - "Eddie Yang"
  - "Gefei Liu"
  - "Akhil Pandey Akella"
date: "2025.09"
doi: "10.48550/arXiv.2509.21493"
arxiv: ""
score: 4.0
essence: "과학 논문을 정책 문서로 변환하는 LLM의 능력을 평가하고 개선하기 위해 벤치마크(Sci2Pol-Bench)와 학습 데이터셋(Sci2Pol-Corpus)을 제시한다."
tags:
  - "cat/Scientific_Impact_and_Innovation"
  - "sub/Artificial_intelligence_and_science"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Wu et al._2025_Sci2Pol Evaluating and Fine-tuning LLMs on Scientific-to-Policy Brief Generation.pdf"
---

# Sci2Pol: Evaluating and Fine-tuning LLMs on Scientific-to-Policy Brief Generation

> **저자**: Weimin Wu, Alexander C. Furnas, Eddie Yang, Gefei Liu, Akhil Pandey Akella, Xuefeng Song, Dashun Wang, Han Liu | **날짜**: 2025-09-25 | **DOI**: [10.48550/arXiv.2509.21493](https://doi.org/10.48550/arXiv.2509.21493)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1: Overview of Sci2Pol-Taxonomy and Dataset Source. (a) Sci2Pol-Taxonomy defines a*

과학 논문을 정책 문서로 변환하는 LLM의 능력을 평가하고 개선하기 위해 벤치마크(Sci2Pol-Bench)와 학습 데이터셋(Sci2Pol-Corpus)을 제시한다.

## Motivation

- **Known**: LLM은 일반적 능력이 우수하지만, 과학 논문을 정책 담당자용 간결한 문서로 변환하는 데 어려움을 겪는다. 기존 평가 지표(BERTScore, ROUGE)는 정책 문서 품질을 적절히 포착하지 못한다.
- **Gap**: 과학-정책 간 변환 작업을 위한 전문 벤치마크와 학습 데이터가 부재하며, 이 도메인에 특화된 평가 방법론이 필요하다.
- **Why**: 정책 입안자들이 복잡한 과학 연구를 정책 결정에 활용하는 것이 어려워 사회적 과제 해결이 지연되고 있으며, LLM의 체계적 개선을 통해 과학-정책 간극을 해소할 수 있다.
- **Approach**: 인간의 작성 프로세스를 반영하는 5단계 분류체계(자동완성, 이해, 요약, 생성, 검증)를 기반으로 18개 작업의 벤치마크를 설계하고, LLM-as-a-judge 방식의 새로운 평가 지표를 제안한다.

## Achievement

![Figure 2](figures/fig2.webp)

*Figure 2: Overview of the Sci2Pol-Corpus Curation Process. It consists of 639 high-quality pa-*

- **Sci2Pol-Bench 개발**: 85개의 전문가 작성 논문-정책 문서 쌍을 기반으로 18개 작업(객관식 및 개방형)으로 구성된 최초의 과학-정책 변환 벤치마크 구축
- **새로운 평가 지표**: 기존 BERTScore와 ROUGE의 한계를 지적하고, 전문가 판단과 일치하는 LLM 기반 평가 메트릭 제안
- **Sci2Pol-Corpus 구축**: 560만 개 정책 기록에서 140,000개 후보 쌍을 추출한 후 LLM 필터링과 전문가 샘플을 활용한 in-context 폴리싱을 거쳐 639개 고품질 쌍 확보
- **광범위한 평가**: 13개의 최신 LLM(오픈소스 및 상용) 성능 평가로 주요 한계점 도출
- **미세조정 성과**: Sci2Pol-Corpus로 미세조정한 Gemma-27B가 훨씬 큰 GPT-4o 및 DeepSeek-V3(671B)를 초과

## How

![Figure 2](figures/fig2.webp)

*Figure 2: Overview of the Sci2Pol-Corpus Curation Process. It consists of 639 high-quality pa-*

- 5단계 분류체계(Sci2Pol-Taxonomy)에 기반한 벤치마크 설계: 자동완성, 이해, 요약, 생성, 검증 단계별 작업 정의
- 85개 전문가 작성 논문-정책 문서 쌍(Nature Energy, Nature Climate Change 등 고임팩트 저널 출처)을 도메인 타겟으로 활용
- 생성 작업(Task 11-15)을 위한 LLM-as-a-judge 기반 참고문헌-무관 평가 메트릭 개발
- 560만 정책 기록에서 인용 논문-정책 문서 쌍 매칭을 통해 140,000개 후보 추출
- LLM 기반 자동 필터링 후 3개의 전문가 샘플을 참조로 한 in-context 폴리싱으로 639개 최종 쌍 확보
- LLaMA-3.1-8B, Gemma-12B, Gemma-27B 세 모델을 Sci2Pol-Corpus로 지도학습 미세조정

## Originality

- 과학-정책 변환 작업을 위한 최초의 벤치마크 및 학습 데이터셋 제시
- 인간의 작성 프로세스 반영한 5단계 분류체계 제안으로 체계적 평가 프레임워크 제시
- 기존 자동 평가 지표의 한계를 실증적으로 지적하고 LLM 기반 새로운 평가 메트릭 개발
- 대규모 정책 기록 데이터베이스를 활용한 자동 쌍 추출 및 고품질 필터링 파이프라인 구축
- 정책 문서 작성의 4대 핵심 실패 요인(문맥 깊이 부족, 할루시네이션, 부적절한 톤, 낮은 실행 가능성) 체계적 분석

## Limitation & Further Study

- Sci2Pol-Corpus의 최종 크기(639쌍)가 대규모 모델 미세조정 관점에서는 상대적으로 소규모이며, 데이터 확대를 위한 추가 수집 필요
- 85개 전문가 쌍이 주로 영미권 고임팩트 저널 출처로 지리적·학문적 다양성이 제한적
- LLM-as-a-judge 방식의 평가 메트릭이 특정 LLM(Gemini-2.5-Pro)에 의존하며 평가 편향 가능성
- 정책 문서의 다양한 형식(정책 제안, 위험 평가, 실행 계획 등)에 대한 세분화된 평가 필요
- 후속 연구: 다국어 및 다양한 정책 맥락 포함으로 벤치마크 확장, 강화학습(RLHF)을 통한 성능 개선 탐색, 도메인 특화 평가 지표 개발

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 과학과 정책 간의 중요한 격차를 해소하기 위한 최초의 전문화된 벤치마크와 데이터셋을 제시하며, 체계적 분류체계와 새로운 평가 메트릭을 통해 LLM의 한계를 명확히 규명하고 미세조정으로 성능 개선을 입증한 의미 있는 연구다.

## Related Papers

- 🔄 다른 접근: [[papers/1073_MOLIERE_Automatic_Biomedical_Hypothesis_Generation_System/review]] — 생의학 분야에서 과학 지식을 다른 형태(가설 vs 정책문서)로 변환하는 자동화 시스템의 다른 접근법을 보여준다.
- 🏛 기반 연구: [[papers/1051_Unsupervised_Word_Embeddings_Capture_Latent_Knowledge_from_M/review]] — 의료 문헌에서 잠재 지식을 추출하는 비지도 학습 방법론이 과학-정책 변환의 기술적 기반을 제공한다.
- 🧪 응용 사례: [[papers/945_Coevolution_of_policy_and_science_during_the_pandemic/review]] — 과학-정책 번역에서 LLM을 활용하여 팬데믹 동안 정책과 과학의 상호작용을 자동화된 방법으로 분석한다.
- 🧪 응용 사례: [[papers/1043_The_selective_use_of_physics_knowledge_in_policy_how_interdi/review]] — 과학-정책 번역에서 LLM을 활용한 자동화된 접근법으로 물리학 지식의 정책 영향력 분석을 확장할 수 있다.
- 🧪 응용 사례: [[papers/974_Information_Pathways_in_Online_Science_Communication_The_Rol/review]] — 과학-정책 커뮤니케이션 경로 분석을 LLM 기반 평가 도구로 자동화하여 실시간 모니터링 가능
