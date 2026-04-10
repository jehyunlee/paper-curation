---
title: "760_Small_Language_Models_are_the_Future_of_Agentic_AI"
authors:
  - "Peter Belcak"
  - "Greg Heinrich"
  - "Shizhe Diao"
  - "Yonggan Fu"
  - "Xin Dong"
date: "2025.06"
doi: "10.48550/arXiv.2506.02153"
arxiv: ""
score: 4.0
essence: "현재 에이전트 AI 시스템은 대규모 언어모델(LLM)에 의존하고 있으나, 본 논문은 소규모 언어모델(SLM)이 에이전트의 반복적이고 전문화된 작업에 더 적합하며 경제적이므로 에이전트 AI의 미래를 주도할 것이라는 입장을 제시한다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/Multi-Agent_Language_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Belcak et al._2025_Small Language Models are the Future of Agentic AI.pdf"
---

# Small Language Models are the Future of Agentic AI

> **저자**: Peter Belcak, Greg Heinrich, Shizhe Diao, Yonggan Fu, Xin Dong, Saurav Muralidharan, Yingyan Celine Lin, Pavlo Molchanov | **날짜**: 2025-06-02 | **DOI**: [10.48550/arXiv.2506.02153](https://doi.org/10.48550/arXiv.2506.02153)

---

## Essence

현재 에이전트 AI 시스템은 대규모 언어모델(LLM)에 의존하고 있으나, 본 논문은 소규모 언어모델(SLM)이 에이전트의 반복적이고 전문화된 작업에 더 적합하며 경제적이므로 에이전트 AI의 미래를 주도할 것이라는 입장을 제시한다.

## Motivation

- **Known**: 현재 대부분의 에이전트 AI 시스템은 LLM API 엔드포인트에 의존하고 있으며, 2024년 기준 클라우드 인프라 투자가 570억 달러에 달한다.

- **Gap**: 에이전트 시스템의 실제 작업은 제한된 범위의 전문화된 반복 작업인데도 불구하고, 일반용 대규모 모델을 사용하는 것이 표준 관행으로 남아있다.

- **Why**: 에이전트 시스템의 경제성, 환경 지속성, 자원 효율성을 고려할 때 SLM으로의 전환이 필수적이다. 에이전트 AI 시장이 2034년까지 약 2000억 달러로 성장할 것으로 예상되므로, 리소스 활용의 최적화가 중요하다.

- **Approach**: 
  1. SLM의 충분한 성능 입증 (V1)
  2. 에이전트 시스템에서의 운영적 우월성 확인 (V2)
  3. 경제성 분석 (V3)
  4. LLM-to-SLM 변환 알고리즘 제시

## Achievement

![Figure 1: An illustration of agentic systems with different modes of agency. Left: Language model agency. The language model acts both as the HCI and the orchestrator of tool calls to carry out a task. Right: Code agency. The language model fills the role of the HCI (optionally) while a dedicated controller code orchestrates all interactions.](figures/fig1.webp)

*에이전트 시스템의 두 가지 운영 방식: 좌측은 언어모델이 인터페이스와 도구 호출을 모두 조율하는 방식, 우측은 코드 기반 컨트롤러가 상호작용을 조율하는 방식*

1. **SLM의 충분한 성능 입증**:
   - Phi-2 (2.7B): 30B 모델 수준의 상식추론, ~15배 빠른 속도
   - Phi-3 Small (7B): 70B 모델 수준의 코드생성 성능
   - Nemotron-H (2-9B): 30B LLM 수준의 명령어 따르기, 한 자리 수 추론 비용
   - xLAM-2-8B: GPT-4o와 Claude 3.5를 능가하는 도구 호출 성능
   - DeepSeek-R1-Distill-7B: Claude-3.5-Sonnet 및 GPT-4o 초과 성능

2. **경제성 우월성**:
   - 추론 효율성: 7B SLM은 70-175B LLM 대비 10-30배 저렴
   - 미세조정(Fine-tuning) 민첩성: GPU 몇 시간으로 완료 (LLM은 주 단위)
   - 엣지 배포: 소비자 GPU에서 로컬 실행 가능
   - 인프라 운영: GPU/노드 간 병렬화 필요성 감소로 유지보수 비용 절감

3. **이질형 에이전트 시스템 제안**:
   - SLM을 기본 모델로 사용하고 필요시에만 선택적으로 LLM 호출
   - 특화된 SLM 조합으로 모듈식 아키텍처 구성

## How

- **성능 평가 기준**:
  - 상식추론 능력 (기본 이해도 지표)
  - 도구 호출 및 코드생성 능력 (모델-도구/코드 인터페이스 통신 능력)
  - 명령어 따르기 능력 (코드-모델 인터페이스 응답 능력)

- **SLM 강화 기법**:
  - 추론 시간 기법: 자체 일관성(self-consistency), 검증자 피드백(verifier feedback)
  - 도구 증강(tool augmentation): Toolformer (6.7B)가 GPT-3 (175B)를 능가
  - 구조화된 추론: 1-3B 모델이 수학 문제에서 30B+ LLM과 경쟁

- **정의 및 범주**:
  - SLM: 일반 소비자 전자기기에 탑재 가능하고 단일 사용자 요청에 대해 실용적인 지연시간으로 추론 가능한 모델 (2025년 기준 ~10B 이하)
  - LLM: SLM이 아닌 모든 언어모델

## Originality

- **혁신성**:
  - LLM 중심의 에이전트 아키텍처에 대한 체계적인 도전 제기 (기존에는 자동화된 관행)
  - 에이전트 시스템의 특성(반복성, 전문화, 비대화형)과 모델 선택의 부정렬을 명확히 지적
  - 57억 달러 대 560억 달러의 시장-투자 불균형 문제를 경제적으로 분석

- **실무적 기여**:
  - LLM-to-SLM 변환 알고리즘 제시
  - 인기 오픈소스 에이전트에 대한 교체 가능성 사례 연구 (부록)
  - 이질형 에이전트 시스템에 대한 설계 원칙 제공

- **시대적 필요성**:
  - AI 인프라 비용 급증과 환경 지속성 문제에 대한 실질적 대안 제시
  - 커뮤니티 피드백을 위한 개방형 플랫폼(research.nvidia.com/labs/lpr/slm-agents) 제공

## Limitation & Further Study

- **현재 한계**:
  - 논문이 입장(position paper)이므로 완전한 실증 데이터가 부족할 수 있음
  - 모든 에이전트 작업이 SLM으로 대체 가능한지에 대한 경계 조건이 명확하지 않음
  - 특정 도메인(예: 장문맥 추론, 멀티홉 추론)에서 SLM의 성능 한계에 대한 상세 분석 부재
  - 기존 LLM 인프라에 대한 대규모 투자로 인한 실질적 전환 장벽 분석 미흡

- **후속 연구 필요 사항**:
  - 실제 프로덕션 환경에서 LLM-to-SLM 전환의 성능 및 비용 벤치마크
  - 다양한 에이전트 아키텍처(Agentic RAG, ReAct, 자율 에이전트 등)별 SLM 적용 성과 측정
  - 도메인별 최적 SLM 선택 기준과 자동 선택 메커니즘 개발
  - 비전-언어 모델(VLM)에 대한 동일 분석 확장
  - 이질형 에이전트 시스템의 오케스트레이션 및 최적화 알고리즘 개발
  - 비용-성능 트레이드오프 곡선의 정량적 매핑


## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 5/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 논문은 현재 LLM 중심의 에이전트 AI 산업에 대한 경제적·기술적·환경적 비판을 제기하고 SLM 기반 에이전트 시스템으로의 전환을 주장하는 중요한 입장 논문이다. NVIDIA 연구진의 체계적인 주장과 다양한 최신 SLM 모델들의 성능 사례를 통해 기술적 타당성을 입증하며, 수백억 달러 규모의 인프라 투자 불일치 문제를 날카롭게 지적한다. 다만 대규모 실증 데이터와 프로덕션 환경의 검증, 그리고 체계적인 도메인별 경계 조건 분석이 추가되면 더욱 강력한 주장이 될 수 있다. 에이전트 AI의 빠른 성장과 AI 비용 효율성에 대한 업계 관심을 고려할 때, 커뮤니티 논의를 촉발할 만한 가치 있는 기여다.

## Related Papers

- ⚖️ 반론/비판: [[papers/388_GPT-4o_System_Card/review]] — GPT-4o의 대규모 모델 능력과 달리 소규모 언어모델이 에이전트 AI의 미래라는 관점은 모델 크기에 대한 상반된 시각을 제시한다.
- 🏛 기반 연구: [[papers/823_Towards_a_Science_of_Scaling_Agent_Systems/review]] — 에이전트 시스템 확장의 과학은 소규모 언어모델이 에이전트 AI에서 어떻게 효과적으로 확장될 수 있는지에 대한 이론적 기반을 제공한다.
- 🔗 후속 연구: [[papers/464_Large_Language_Model_based_Multi-Agents_A_Survey_of_Progress/review]] — LLM 기반 다중 에이전트의 진전 조사는 소규모 언어모델의 에이전트 적합성을 기존 대규모 모델 기반 에이전트 연구와 비교 분석한다.
- ⚖️ 반론/비판: [[papers/033_A_survey_on_large_language_model_based_autonomous_agents/review]] — 소형 언어모델이 에이전틱 AI의 미래라는 대안적 관점을 제시한다.
