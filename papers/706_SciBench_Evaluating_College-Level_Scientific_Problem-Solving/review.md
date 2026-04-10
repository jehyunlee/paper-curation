---
title: "706_SciBench_Evaluating_College-Level_Scientific_Problem-Solving"
authors:
  - "Xiaoxuan Wang"
  - "Ziniu Hu"
  - "Pan Lu"
  - "Yanqiao Zhu"
  - "Jieyu Zhang"
date: "2023.07"
doi: "N/A"
arxiv: ""
score: 4.5
essence: "본 논문은 대학 수준의 과학 문제 해결 능력을 평가하기 위한 포괄적 벤치마크인 SciBench를 제시한다. 기존 벤치마크의 고등학교 수준 문제 중심 한계를 극복하기 위해 869개의 대학 수준 수학, 화학, 물리 문제와 177개의 멀티모달 문제를 포함한 데이터셋을 구축했다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/AI_Research_Ideation"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Wang et al._2023_SciBench Evaluating College-Level Scientific Problem-Solving Abilities of Large Language Models.pdf"
---

# SciBench: Evaluating College-Level Scientific Problem-Solving Abilities of Large Language Models

> **저자**: Xiaoxuan Wang, Ziniu Hu, Pan Lu, Yanqiao Zhu, Jieyu Zhang, Satyen Subramaniam, Arjun R. Loomba, Shichang Zhang, Yizhou Sun, Wei Wang | **날짜**: 2023-07-20 | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1: Physical Chemistry 문제의 두 가지 프롬프팅 전략에 따른 GPT-4의 해결 시도. CoT 프롬프팅에서는 공식은 맞지만 계산 오류가 발생하고, Python 외부 도구 사용 시에는 수학적 관계 오해로 인한 오류 발생*

본 논문은 대학 수준의 과학 문제 해결 능력을 평가하기 위한 포괄적 벤치마크인 SciBench를 제시한다. 기존 벤치마크의 고등학교 수준 문제 중심 한계를 극복하기 위해 869개의 대학 수준 수학, 화학, 물리 문제와 177개의 멀티모달 문제를 포함한 데이터셋을 구축했다.

## Motivation

- **Known**: GPT-4가 GRE 정량 시험에서 80 백분위수(163/170)를 달성하는 등 LLM의 수학적 추론 능력이 향상되고 있음. Chain-of-Thought(CoT)와 외부 도구 활용 등 다양한 프롬프팅 전략이 제안되고 있음.

- **Gap**: 기존 벤치마크(ScienceQA, GSM8K, MATH, MMLU 등)는 (1) 고등학교 수준 문제에 편중, (2) 사칙연산 중심의 기본 계산만 평가, (3) 시각 요소 부재, (4) 다중 도메인의 심층적 추론 능력 미평가.

- **Why**: Figure 1의 예시처럼 CoT는 공식은 맞지만 계산에서 실패하고, 외부 도구 프롬프팅은 수학적 관계를 왜곡하는 등 단순 성능 개선만으로는 복잡한 과학 문제 해결의 진정한 능력을 평가할 수 없음.

- **Approach**: (1) 대학 수준의 개방형 서술식 문제 869개 수집, (2) 멀티모달 부분집합 177개 포함, (3) 폐쇄형 시험 문제 103개 추가, (4) 다양한 LLM(LLaMA-2, Mistral, Claude2, GPT-3.5, GPT-4 등)과 프롬프팅 전략 평가, (5) 상세한 오류 분석을 통해 10가지 필수 문제 해결 능력 분류.

## Achievement

![Table 1](figures/fig-table1.webp)

*Table 1: SciBench와 기타 벤치마크 비교. 대학 수준, 미적분, 통계, 시각 컨텍스트, 상세 해결책, 자유 응답 형식의 포괄성 입증*

1. **포괄적 벤치마크 구축**: 기존 벤치마크 대비 가장 광범위한 특성 보유 - 대학 수준, 다중 도메인(수학/화학/물리), 고급 계산(미적분/통계), 멀티모달 포함, 자유 응답형식, 상세 솔루션 제공.

2. **성능 격차 정량화**: 최고 성능 모델(CoT + 외부 도구)도 텍스트 데이터셋 43.22%, 멀티모달 데이터셋 13.8%, 폐쇄 시험 데이터셋 51.57%의 점수만 달성 - LLM의 심각한 한계 노출.

3. **체계적 오류 분석**: 인간 주석자의 자세한 비교 분석을 통해 "도메인 지식", "수학적 추론", "수치 계산", "상식 이해" 등 10가지 핵심 문제 해결 능력 분류 체계 수립.

4. **프롬프팅 전략의 trade-off 발견**: CoT, 영점학습(zero-shot), 소수점 학습(few-shot), 외부 도구 활용 등 어느 단일 전략도 모든 능력에서 우월하지 않으며, 특정 능력 향상이 다른 능력 저하를 초래할 수 있음을 실증.

## How

- **데이터셋 수집**: 대학 교과서(Atkins의 물리화학, Stewart의 미적분 등)에서 개방형 서술식 문제 수집, PDF에서 수동 추출하여 LaTeX로 형식화하여 학습 데이터 유출 위험 최소화.

- **멀티모달 포함**: 그래프, 도표, 구조식 등 시각 요소 포함 문제 177개로 비전-언어 모델(GPT-4V, InternLM-XComposer2 등) 평가 가능.

- **다양한 프롬프팅 전략**: 
  - Chain-of-Thought(CoT): 단계별 추론 생성 유도
  - 영점학습: 직접 답변 생성
  - 소수점 학습: 예제 제시 후 학습
  - 외부 도구: Python 및 Wolfram 언어 코드 생성 활용

- **자동화된 오류 분류**: LLM 기반 자기비평(self-critic) 방식으로 올바른 해답과 생성된 해답의 차이를 10가지 능력 카테고리로 자동 분류.

- **폐쇄 데이터셋**: 실제 대학 중기/기말 시험 문제 103개를 별도 보유하여 벤치마크 integrity 확보 및 모델 학습 데이터 유출 영향 배제.

## Originality

- **첫 대학 수준 과학 벤치마크**: 기존의 고등학교 수준 문제 중심 벤치마크를 넘어 진정한 대학 수준의 복잡한 과학 문제 평가 체계 최초 제시.

- **다중 계산 복잡도 포함**: 사칙연산에서 미적분, 미분방정식, 통계 등으로 평가 범위 확대 - LLM의 고급 수학적 추론 능력 진정한 평가 가능.

- **체계적 능력 분해**: 오류 분석을 통해 "도메인 지식", "공식 도출", "개념 이해", "수치 계산" 등 10가지 세분화된 문제 해결 능력 분류 - 향후 개선 방향의 명확한 로드맵 제시.

- **프롬프팅 전략의 trade-off 분석**: 단순 성능 비교를 넘어 각 전략의 강점과 약점을 능력 수준에서 정밀 분석 - 프롬프팅 기법의 한계 명확히 규명.

- **멀티모달 평가**: 비전-언어 모델의 성능이 텍스트 모델 대비 심각히 낮음(13.8%)을 최초 정량화.

## Limitation & Further Study

- **자동 평가의 한계**: 서술식 문제의 정확한 채점을 위해 주로 최종 답변의 수치 일치도만 평가하며, 부분 점수나 논리적 타당성 평가는 제한적 - 고급 채점 루브릭 개발 필요.

- **모델 범위**: 평가 대상이 주로 영어 기반 LLM에 편중되어 있어 다국어 모델이나 소규모 오픈소스 모델의 성능 파악 부족.

- **도메인별 세부 분석 부족**: 수학, 화학, 물리 간의 성능 차이 및 특화된 도메인 능력 개발 방향이 명확하지 않음 - 도메인별 세부 평가 프레임워크 필요.

- **외부 도구 활용의 최적화 미흡**: Python/Wolfram 코드 생성 후 실행 오류에 대한 피드백 루프나 자동 수정 메커니즘 부재.

- **후속 연구 방향**:
  - 대규모 언어 모델의 과학적 추론 능력 향상을 위한 특화 학습 방법론 개발
  - SciBench를 활용한 합성 데이터 생성(synthetic data generation)으로 모델 미세 조정
  - 멀티모달 모델의 시각-언어 통합 능력 개선 연구
  - 외부 도구 활용 시 오류 정정 메커니즘 도입
  - 도메인 특화 모델 개발 및 평가

## Evaluation

- **Novelty (신규성): 5/5**
  - 최초의 대학 수준 과학 벤치마크
  - 다중 도메인, 고급 계산, 멀티모달 포함의 종합성
  - 체계적 능력 분해 프레임워크 개발

- **Technical Soundness (기술적 건전성): 4/5**
  - 견고한 데이터 수집 및 형식화 프로세스 (PDF 수동 추출, LaTeX 변환)
  - 폐쇄 데이터셋을 통한 평가 무결성 보장
  - 다양한 LLM과 전략의 포괄적 평가
  - 아쉬운 점: 자동 채점의 한계, 부분 점수 평가 미흡

- **Significance (학문적 중요성): 5/5**
  - LLM의 과학적 추론 능력에 대한 새로운 평가 기준 제시
  - 현재 LLM의 심각한 한계(최고 43.22%) 정량화로 향후 개선 동기 제공
  - 프롬프팅 전략의 trade-off 발견으로 이론적 인사이트 제공
  - AI 연구와 과학 발견에의 실질적 기여 가능성

- **Clarity (명확성): 4/5**
  - 동기와 문제점이 명확히 설명됨 (Figure 1 예시 효과적)
  - 데이터셋 특성과 평가 방법론이 자세히 기술됨
  - 결과 제시가 종합적이나, 도메인별 세부 분석 결과 부족

- **Overall: 4.5/5**

**총평**: 

SciBench는 LLM의 과학적 추론 능력을 평가하기 위한 매우 중요한 벤치마크로, 기존 고등학교 수준의 단순 산술 중심 평가를 넘어 대학 수준의 복합 과학 문제로 확장했다는 점에서 큰 의의가 있다. 특히 10가지 세분화된 문제 해결 능력 분류와 프롬프팅 전략의 trade-off 분석은 향후 LLM 개선의 명확한 방향을 제시한다. 멀티모달 평가의 포함, 폐쇄 데이터셋을 통한 평가 무결성 보장, 다양한 LLM에 대한 포괄적 벤치마킹은 충분히 견고한 기초를 마련했다. 다만 자동 채점의 한계와 도메인별 세부 분석의 부족은 향후 개선 과제이며, 부분 점수 체계의 도입이나 논리적 타당성 평가 프레임워크의 개발이 필요하다. 전반적으로 과학 AI 분야의 발전에 중요한 표준이 될 수 있는 견고하고 영향력 있는 연구이다.

## Related Papers

- 🔄 다른 접근: [[papers/808_Theoremqa_A_theorem-driven_question_answering_dataset/review]] — 과학 문제 해결 능력을 대학 수준 vs 정리 증명 수준에서 각각 평가한다.
- 🔗 후속 연구: [[papers/552_Mmsci_A_dataset_for_graduate-level_multi-discipline_multimod/review]] — 대학 수준 과학 문제를 대학원 수준 멀티모달 과학으로 확장한다.
- 🏛 기반 연구: [[papers/090_AIRS-Bench_a_Suite_of_Tasks_for_Frontier_AI_Research_Science/review]] — 최전선 AI 연구 과학을 위한 기초적 벤치마크 역할을 한다.
- 🏛 기반 연구: [[papers/713_Scicueval_A_comprehensive_dataset_for_evaluating_scientific/review]] — 대학 수준의 과학 문제 해결 평가는 과학적 맥락 이해 능력 측정의 기반이 되는 문제 해결 능력 평가 방법론입니다
- 🔄 다른 접근: [[papers/697_Scaling_physical_reasoning_with_the_physics_dataset/review]] — 둘 다 과학 문제 해결 벤치마크이지만 PHYSICS는 물리 특화, SciBench는 대학 수준 전반을 다루는 차이가 있음
- 🔄 다른 접근: [[papers/808_Theoremqa_A_theorem-driven_question_answering_dataset/review]] — 둘 다 과학 문제 해결 벤치마크이지만 TheoremQA는 정리 중심, SciBench는 대학 수준 전반을 다루는 차이가 있음
- 🏛 기반 연구: [[papers/299_Earthse_A_benchmark_evaluating_earth_scientific_exploration/review]] — 대학 수준 과학 문제 해결 평가가 지구과학 벤치마크의 기반 제공
