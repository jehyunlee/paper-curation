---
title: "888_X-webagentbench_A_multilingual_interactive_web_benchmark_for"
authors:
  - "Peng Wang"
  - "Ruihan Tao"
  - "Qiguang Chen"
  - "Mengkang Hu"
  - "Libo Qin"
date: "2025"
doi: "arXiv:2505.15372v1"
arxiv: ""
score: 4.2
essence: "본 논문은 대규모 언어모델(LLM) 기반 에이전트의 다국어 성능을 평가하기 위해 14개 언어, 2,800개의 지시문, 589,946개의 상품을 포함한 X-WebAgentBench 벤치마크를 제시한다. 기존 에이전트 벤치마크들이 영어 중심이었던 반면, 이 연구는 다국어 지시문과 다국어 환경을 동시에 포함한 최초의 종합적인 다국어 에이전트 평가 벤치마크를 구축하였다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/Realistic_Discovery_Benchmarks"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Wang et al._2025_X-webagentbench A multilingual interactive web benchmark for evaluating global agentic system.pdf"
---

# X-WebAgentBench: A Multilingual Interactive Web Benchmark for Evaluating Global Agentic System

> **저자**: Peng Wang, Ruihan Tao, Qiguang Chen, Mengkang Hu, Libo Qin | **날짜**: 2025 | **DOI**: [arXiv:2505.15372v1](https://arxiv.org/abs/2505.15372v1)

---

## Essence

![Figure 1](figures/fig1.webp)
*영어 환경과 다국어 환경에서 GPT-4o의 성능 비교: 다국어 환경에서 20% 이상 성능 저하 발생*

본 논문은 대규모 언어모델(LLM) 기반 에이전트의 다국어 성능을 평가하기 위해 14개 언어, 2,800개의 지시문, 589,946개의 상품을 포함한 X-WebAgentBench 벤치마크를 제시한다. 기존 에이전트 벤치마크들이 영어 중심이었던 반면, 이 연구는 다국어 지시문과 다국어 환경을 동시에 포함한 최초의 종합적인 다국어 에이전트 평가 벤치마크를 구축하였다.

## Motivation

- **Known**: LLM 기반 에이전트는 ReAct, Reflexion, MetaGPT 등의 방법론을 통해 상당한 성공을 거두었으며, Mind2Web, WebArena, OsWorld 등의 다양한 상호작용 벤치마크가 개발되었다.

- **Gap**: 기존의 모든 주요 에이전트 벤치마크가 영어 환경에만 집중되어 있으며, 다국어 지시문과 다국어 환경을 모두 제공하는 벤치마크가 부재하다.

- **Why**: 전 세계 7,000개 이상의 언어가 존재하고, 전자상거래 등 실제 글로벌 응용 환경에서는 사용자들이 모국어를 사용하여 에이전트와 상호작용한다. 그러나 GPT-4o 같은 최고 성능의 모델도 다국어 환경에서는 영어 대비 20% 이상 성능이 저하되는 문제가 있다.

- **Approach**: 영어 WebShop 벤치마크를 기반으로 하되, (a) 14개 대표 언어를 선정하여 (b) 지시문과 환경 데이터를 다국어로 번역하고, (c) 품질 검증을 통해 신뢰할 수 있는 다국어 에이전트 평가 벤치마크를 구축한다.

## Achievement

![Figure 2](figures/fig2.webp)
*X-WebAgentBench 구축의 4단계: (a) 데이터 준비, (b) 다국어 지시문 구성, (c) 다국어 환경 구성, (d) 품질 검증*

![Figure 3](figures/fig3.webp)
*X-WebAgentBench의 언어 분포(15개 언어, 청색=영어 영역, 녹색=다국어 영역) 및 상품 카테고리 분포*

1. **벤치마크 구축**: 14개 언어에 걸쳐 2,800개의 다국어 지시문과 589,946개의 다국어 상품 데이터를 포함한 첫 번째 종합적 다국어 에이전트 벤치마크 개발

2. **성능 분석**: 다양한 LLM과 교차언어 정렬(cross-lingual alignment) 방법의 효과를 체계적으로 평가하여, (a) 큰 모델의 경우 고급 교차언어 정렬이 성능을 크게 향상시키고, (b) 작은 모델의 경우 다국어 환경을 영어로 번역하는 것이 효과적이며, (c) 기존 에이전트 기법과 교차언어 기법의 단순 조합은 불충분함을 입증

3. **품질 보증**: 50개 제품에 대한 사전 검증을 통해 Google Translate(90% 이상)와 GPT-4 (74%)의 번역 정확도를 비교하고, 환경 데이터 번역에는 GPT-4를 선택하여 문맥적 뉘앙스를 정확히 포착

## How

![Figure 2](figures/fig2.webp)

### 2.1 데이터 준비 (Data Preparation)
- **언어 선택**: Conneau et al. (2018)을 따라 7개 언어족에 걸친 14개 대표 언어 선정 (자원 분포 균형 및 지리적 다양성 확보)
- **지시문 준비**: WebShop 데이터셋에서 500개의 명확한 제품 검색 지시문을 수동으로 선정
- **환경 준비**: 긴 문맥으로 인한 영향을 줄이기 위해 WebShop의 전자상거래 환경을 단순화 (평균 211개 상품/지시문)

### 2.2 다국어 지시문 구성 (Multilingual Instruction Construction)
- **사전 검증**: 50개 영어 지시문을 GPT-4와 Google Translate로 14개 언어로 번역하여 정확도 평가
- **번역 작업**: Google Translate API를 활용하여 500개 지시문을 14개 언어로 번역 → 2,800개의 다국어 지시문 생성

### 2.3 다국어 환경 구성 (Multilingual Environment Construction)
- **사전 검증**: 50개 상품에 대해 제목, 카테고리, 버튼, 설명, 커스터마이징 옵션 등 여러 필드를 GPT-4와 Google Translate로 비교 평가 → GPT-4가 15% 더 높은 정확도 달성
- **환경 번역**: 통일된 JSON 형식으로 표준화한 후 GPT-4를 사용하여 589,946개 상품을 14개 언어로 번역

### 2.4 품질 검증 (Quality Check)
- **온보딩 테스트**: 각 언어별 50개 테스트 지시문으로 주석자들의 평균 점수 ≥80% 확인
- **LLM 검증**: GPT-4를 사용하여 다국어 번역을 원본 영어와 비교 (0-10 척도에서 8점 이상만 포함)
- **수동 재검증**: 최종적으로 주석자가 수동 검증

## Originality

- **다국어 포괄성**: 기존 벤치마크들은 영어 환경만 제공했으나, 본 연구는 다국어 지시문과 다국어 상호작용 환경을 동시에 포함한 최초의 벤치마크 제시

- **다층적 품질 관리**: 지시문과 환경 데이터 번역 시 다양한 자동화 도구를 비교 평가(Google Translate vs GPT-4)하고, 각 단계별로 사전 검증→자동 번역→LLM 검증→수동 재검증의 4단계 품질 관리 체계 구축

- **교차언어 정렬 분석**: 큰 모델과 작은 모델에 대해 차별화된 교차언어 정렬 전략의 효과를 실증적으로 입증

- **저자원 언어 포함**: 단순히 고자원 언어뿐 아니라 태국어, 우르두어, 힌디어 등 저자원 언어도 포함하여 글로벌 적용성 강화

## Limitation & Further Study

- **번역 기반 벤치마크의 한계**: 자동 번역에 의존하기 때문에 각 언어의 문화적 특수성이나 관용적 표현이 충분히 반영되지 않을 가능성이 있으며, 특히 저자원 언어의 번역 품질이 제한적일 수 있다.

- **환경 다양성 부족**: WebShop 기반이므로 전자상거래 도메인에만 국한되어 있으며, 다른 실제 응용 환경(은행 서비스, 정부 시스템 등)에서의 에이전트 성능 평가가 불가능하다.

- **지시문 규모**: 500개의 기본 지시문(×14언어=2,800개)은 이전 벤치마크(WebShop의 12,087개)보다 작아서 통계적 신뢰성이 제한될 수 있다.

- **후속 연구**: 
  - 각 언어의 모국어 화자에 의한 직접 작성 지시문 포함
  - 다양한 도메인(금융, 의료, 행정 등)으로의 벤치마크 확대
  - 언어별 특화된 에이전트 설계 전략 개발
  - 저자원 언어의 성능 향상을 위한 언어 간 지식 전이(transfer learning) 방법 연구


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4/5
- Significance: 4.5/5
- Clarity: 4/5
- Overall: 4.2/5

**총평**: X-WebAgentBench는 다국어 에이전트 연구의 중요한 공백을 채운 첫 번째 종합적 벤치마크로서 학술적·실무적 가치가 높으며, 체계적인 품질 관리 방식이 돋보인다. 다만 전자상거래 도메인 중심, 상대적으로 작은 지시문 규모, 자동 번역의 근본적 한계 등으로 인해 추가 확장과 개선 여지가 있다.

## Related Papers

- 🔄 다른 접근: [[papers/782_SWE-bench_Can_Language_Models_Resolve_Real-World_GitHub_Issu/review]] — X-WebAgentBench가 다국어 웹 환경에서 에이전트를 평가하는 반면, SWE-bench는 GitHub 코드 저장소에서 실제 문제 해결 능력을 측정하는 대안적 벤치마킹 접근법을 제시합니다.
- 🔗 후속 연구: [[papers/429_Infiagent-dabench_Evaluating_agents_on_data_analysis_tasks/review]] — X-WebAgentBench의 다국어 웹 환경 평가를 InfiAgent-DABench의 데이터 분석 작업 평가와 결합하면 더 포괄적인 다중 에이전트 성능 벤치마크를 구축할 수 있습니다.
- 🔗 후속 연구: [[papers/849_UI-TARS_Pioneering_Automated_GUI_Interaction_with_Native_Age/review]] — GUI 상호작용이 다국어 웹 에이전트 벤치마크로 확장됩니다.
- 🔗 후속 연구: [[papers/871_WebAgent-R1_Training_Web_Agents_via_End-to-End_Multi-Turn_Re/review]] — X-WebAgentBench의 다국어 웹 벤치마크는 WebAgent-R1의 종단 간 학습 프레임워크를 다양한 언어 환경에서 평가하고 개선할 수 있다.
- 🧪 응용 사례: [[papers/872_Webdancer_Towards_autonomous_information_seeking_agency/review]] — X-WebAgentBench의 다국어 웹 벤치마크는 WebDancer의 자율적 정보 탐색 에이전트를 다양한 언어와 문화적 맥락에서 평가하고 개선할 수 있다.
