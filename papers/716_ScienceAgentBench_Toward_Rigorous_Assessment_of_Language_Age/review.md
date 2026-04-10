---
title: "716_ScienceAgentBench_Toward_Rigorous_Assessment_of_Language_Age"
authors:
  - "Ziru Chen"
  - "Shijie Chen"
  - "Yuting Ning"
  - "Qianheng Zhang"
  - "Boshi Wang"
date: "2025.03"
doi: "10.48550/arXiv.2410.05080"
arxiv: ""
score: 4.4
essence: "본 논문은 대규모언어모델(LLM) 기반 언어에이전트(Language Agents)의 데이터 기반 과학 발견 수행능력을 엄밀하게 평가하기 위한 벤치마크 ScienceAgentBench를 제시한다. 최근 LLM이 과학 연구 자동화를 완전히 자동화할 수 있다는 주장들에 대해, 개별 과학적 작업 단위에서의 체계적 평가의 중요성을 강조하고 현재 에이전트의 실제 역량의 한계를 명확히 한다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/Realistic_Discovery_Benchmarks"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Chen et al._2025_ScienceAgentBench Toward Rigorous Assessment of Language Agents for Data-Driven Scientific Discover.pdf"
---

# ScienceAgentBench: Toward Rigorous Assessment of Language Agents for Data-Driven Scientific Discovery

> **저자**: Ziru Chen, Shijie Chen, Yuting Ning, Qianheng Zhang, Boshi Wang, Botao Yu, Yifei Li, Zeyi Liao, Chen Wei, Zitong Lu, Vishal Dey, Mingyi Xue, Frazier N. Baker, Benjamin Burns, Daniel Adu-Ampratwum, Xuhui Huang, Xia Ning, Song Gao, Yu Su, Huan Sun | **날짜**: 2025-03-31 | **DOI**: [10.48550/arXiv.2410.05080](https://doi.org/10.48550/arXiv.2410.05080) | **출판처**: ICLR 2025

---

## Essence

본 논문은 대규모언어모델(LLM) 기반 언어에이전트(Language Agents)의 데이터 기반 과학 발견 수행능력을 엄밀하게 평가하기 위한 벤치마크 ScienceAgentBench를 제시한다. 최근 LLM이 과학 연구 자동화를 완전히 자동화할 수 있다는 주장들에 대해, 개별 과학적 작업 단위에서의 체계적 평가의 중요성을 강조하고 현재 에이전트의 실제 역량의 한계를 명확히 한다.

## Motivation

- **Known**: LLM의 코드 생성, 추론, 도구 활용 능력이 향상되면서 과학 발견 자동화에 대한 기대가 높아지고 있으며, 일부 연구("The AI Scientist" 등)에서 엔드-투-엔드 자동화 가능성을 주장하고 있다.

- **Gap**: 기존 평가 방식은 생성된 논문을 LLM 리뷰어로 평가하는 등 주관적이고 신뢰성이 낮으며, 과학 워크플로우의 개별 작업(데이터 처리, 모델 개발, 분석, 시각화)에 대한 객관적 평가 벤치마크가 부재하다.

- **Why**: 엔드-투-엔드 자동화를 주장하기 전에 데이터 기반 발견 워크플로우의 필수 작업들을 성공적으로 완수할 수 있는지 먼저 검증해야 하며, 이를 위해 과학적 진정성과 실제 적용가능성을 갖춘 벤치마크가 필수적이다.

- **Approach**: 4개 학문 분야(생물정보학, 계산화학, 지리정보과학, 심리인지신경과학)의 44편 논문에서 102개 작업을 추출하고, 9명의 분야별 전문가와 함께 검증하여 과학적 신뢰성을 확보한다. 모든 작업의 목표 출력을 자체 포함(self-contained) Python 프로그램으로 통일하고, 다단계 품질 관리를 수행한다.

## Achievement

![Figure 1](figures/fig1.webp)
*Figure 1: ScienceAgentBench의 세부 작업 분포(상) 및 생물정보학, 계산화학, 지리정보과학, 심리신경과학의 이질적 데이터 유형(하)*

1. **포괄적 벤치마크 구축**: 4개 분야, 44개 논문, 102개 작업으로 구성된 과학적으로 검증된 벤치마크 개발. 각 작업은 피어리뷰 논문의 공개 코드/데이터에서 직접 추출되어 실제 과학 문제의 높은 대표성 확보.

2. **엄격한 평가 체계 수립**: 생성 프로그램, 실행 결과(렌더링된 그림, 테스트셋 예측), 계산비용을 모두 검토하는 다차원 평가 메트릭과 작업 특화 루브릭 제시. 주석자-전문가 다단계 검증으로 데이터 품질 보증.

3. **현실적 성능 평가**: 5개 LLM(오픈웨이트/독점)을 3개 프레임워크(직접 프롬프팅, OpenHands CodeAct, 자체 디버깅)로 평가한 결과, 최고 성능 에이전트가 3번의 시도로도 **32.4%만 독립적 완수**, 전문가 지식 제공 시 **34.3%** 달성. OpenAI o1은 42.2%이나 비용이 10배 이상 높음.

4. **효율성-성능 트레이드오프 분석**: Claude-3.5-Sonnet 자체 디버깅이 OpenHands CodeAct 대비 10.8% 더 높은 정확도를 17배 낮은 API 비용으로 달성함을 입증, 실무적 에이전트 설계에 대한 통찰 제공.

## How

![Figure 2](figures/fig1.webp)
*Figure 2: 계산화학 작업의 4개 구성요소: (a) 작업 지시사항, (b) 데이터셋 정보, (c) 전문가 제공 지식, (d) 주석된 참조 프로그램*

- **작업 수집**: 과학 논문의 공개 코드/데이터에서 자체 포함적이고 충분히 문서화된 코드 예제 선별 → 벤치마크 작업으로 변환

- **데이터셋 처리**: 원본 논문의 데이터를 수집·전처리하고, 참조 프로그램 개발

- **4단계 품질 검증**: (1) 초기 작업 수집(110개) → (2) 실행 시간/환경 설정 문제로 4개 제거(106개) → (3) 데이터 오염 및 지름길(shortcut) 방지 전략 도입 → (4) 주석자-전문가 다단계 검증

- **데이터 오염 완화**: 공개 데이터셋의 학습 데이터 분할 재구성, 테스트셋 정답 우회 감지 메커니즘 도입으로 에이전트의 부정행위 방지

- **평가 메트릭**: 코드 구문(syntax), 실행 가능성(executability), 결과 정확도(correctness), 계산비용(cost) 종합 평가

- **에이전트 설정**: 직접 프롬프팅(baseline), OpenHands CodeAct(구조화된 에이전트), 자체 디버깅(반복적 오류 수정) 각각 3회 시도 제공

## Originality

- **벤치마크 설계의 과학적 진정성**: 논문-기반 작업 추출 + 분야별 전문가 검증 조합으로 높은 현실성 확보. 기존 LLM 평가 벤치마크(HumanEval, MBPP 등)와 달리 실제 학제 간 과학적 맥락 반영.

- **다차원 평가 체계**: 프로그램 품질, 실행 결과, 비용 을 모두 고려하는 통합 평가 프레임워크. 루브릭 기반 세분화된 평가로 단순 pass/fail을 넘어선 심화 분석 가능.

- **데이터 오염 문제의 체계적 대응**: LLM 사전학습에 포함된 공개 코드/데이터 활용 시 오염 우려를 두 가지 전략(데이터 재분할, 우회 행위 감지)으로 명시적 해결.

- **학제 간 통합**: 단일 분야가 아닌 4개 이질적 분야(생물/화학/지리/심리신경)의 데이터와 분석 방법론을 모두 포함하여 에이전트의 범용성 평가 가능.

- **현실적 인사이트**: 에이전트의 절대 성능뿐 아니라 비용-성능 트레이드오프를 분석함으로써 실무 배포 시 의사결정에 기여.

## Limitation & Further Study

- **작업 규모 제약**: 102개 작업으로는 데이터 기반 발견 워크플로우의 모든 시나리오를 포함하기 어렵다. 특히 더 복잡한 멀티스텝 작업이나 도메인 특화 분석 기법의 확장 필요.

- **평가 메트릭의 개방성**: 많은 과학적 작업은 여러 정당한 해결책이 존재하나, 현재 평가는 참조 프로그램과의 유사성 기반일 수 있다. 더 유연한 채점 메커니즘 개발 필요.

- **전문가 지식의 정성적 제공**: 현재 전문가 제공 지식의 형식과 깊이가 작업마다 다를 수 있으며, 이것이 성능에 미치는 영향의 체계적 분석 부재.

- **에이전트 프레임워크의 편중**: 평가 대상이 주로 영어 기반 LLM이고, 비영어권 과학자를 위한 다언어 지원 미흡.

- **후속 연구 방향**: (1) 더 많은 학문 분야와 복잡한 멀티스텝 작업 포함, (2) 에이전트가 생성한 결과물의 과학적 타당성을 평가하는 더 정교한 기준 개발, (3) 인간-에이전트 협업 방식의 벤치마킹, (4) 전이학습(transfer learning) 능력 평가.


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4.3/5
- Significance: 4.6/5
- Clarity: 4.2/5
- Overall: 4.4/5

**총평**: 본 논문은 LLM 기반 과학 에이전트의 성능을 엄밀하게 평가할 수 있는 고품질 벤치마크를 제시함으로써, 과장된 주장들에 대한 객관적 근거를 제공한다. 특히 피어리뷰 논문 기반 작업 추출과 분야별 전문가 검증을 통해 과학적 진정성을 확보한 점이 핵심 기여이며, 실제 과학자들의 생산성 향상을 목표로 한 현실적 문제 설정이 돋보인다. 다만 현재 에이전트의 32-42% 성능으로는 실무 활용에 아직 제약이 있으며, 이를 개선하기 위한 장기 연구 방향을 제시하는 데 논문의 가치가 있다.

## Related Papers

- 🏛 기반 연구: [[papers/782_SWE-bench_Can_Language_Models_Resolve_Real-World_GitHub_Issu/review]] — 현실적 문제 해결 능력 평가의 중요성을 보여주며 과학 발견 영역에서의 엄밀한 평가 기준을 제시한다.
- 🔗 후속 연구: [[papers/704_SciAgentGym_Benchmarking_Multi-Step_Scientific_Tool-use_in_L/review]] — 도구 활용 평가를 넘어 데이터 기반 과학 발견의 전체적 과정에 대한 포괄적 평가 체계를 제공한다.
- ⚖️ 반론/비판: [[papers/828_Towards_end-to-end_automation_of_AI_research/review]] — 완전 자동화 주장에 대해 개별 과학적 작업 단위에서의 체계적 평가가 우선되어야 함을 강조한다.
- 🧪 응용 사례: [[papers/724_SciHorizon_Benchmarking_AI-for-Science_Readiness_from_Scient/review]] — 언어 에이전트의 엄격한 평가가 SciHorizon의 AI 준비도 측정에 적용된다.
- 🔗 후속 연구: [[papers/170_Blade_Benchmarking_language_model_agents_for_data-driven_sci/review]] — 데이터 기반 과학 발견 벤치마크가 언어 에이전트의 과학 연구 전반에 대한 엄밀한 평가로 확장되었다
- 🏛 기반 연구: [[papers/160_BioAgents_Democratizing_Bioinformatics_Analysis_with_Multi-A/review]] — 생물정보학을 위한 다중 에이전트 시스템의 성능 평가에 과학 에이전트 벤치마크 방법론이 기초적인 평가 틀을 제공한다.
- 🔗 후속 연구: [[papers/782_SWE-bench_Can_Language_Models_Resolve_Real-World_GitHub_Issu/review]] — 소프트웨어 엔지니어링에서 드러난 한계를 과학 발견 영역으로 확장하여 보다 포괄적인 평가 기준을 제시한다.
- 🔄 다른 접근: [[papers/704_SciAgentGym_Benchmarking_Multi-Step_Scientific_Tool-use_in_L/review]] — 도구 활용 중심 평가와 데이터 기반 발견 평가라는 서로 다른 관점으로 과학 에이전트의 능력을 측정한다.
