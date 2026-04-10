---
title: "1095_Towards_large_language_models_as_copilots_for_theorem_provin"
authors:
  - "Baptiste Rozière"
  - "Jonas Gehring"
  - "Fabian Gloeckle"
  - "Sten Sootla"
  - "Itai Gat"
date: "2024"
doi: ""
arxiv: ""
score: 4.0
essence: "Lean Copilot은 대규모 언어모델(LLM)을 Lean 증명보조기에 직접 통합하여 인간 수학자가 정리 증명을 보조받을 수 있는 neuro-symbolic 프레임워크이다. 이를 통해 전술 제안, 증명 탐색, 전제 선택 등의 증명 자동화 도구를 제공한다."
tags:
  - "cat/Scientific_Language_Processing_and_Visualization"
  - "sub/Formal_Theorem_Proving"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Rozière et al._2024_Towards large language models as copilots for theorem proving in lean.pdf"
---

# Towards large language models as copilots for theorem proving in lean

> **저자**: Baptiste Rozière, Jonas Gehring, Fabian Gloeckle, Sten Sootla, Itai Gat, Xiaoqing Ellen Tan, Yossi Adi, Jingyu Liu, Sauvestre, Romain, Tal Remez, Jérémy Rapin, Artyom Kozhevnikov, Ivan Evtimov, Joanna Bitton, Manish Bhatt, Cristian Canton Ferrer, Aaron Grattafiori, Wenhan Xiong, Alexandre Défossez, Jade Copet | **날짜**: 2024 | **URL**: [https://arxiv.org/abs/2404.12534](https://arxiv.org/abs/2404.12534)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1: Lean Copilot provides a general framework for running LLM inference in Lean, either*

Lean Copilot은 대규모 언어모델(LLM)을 Lean 증명보조기에 직접 통합하여 인간 수학자가 정리 증명을 보조받을 수 있는 neuro-symbolic 프레임워크이다. 이를 통해 전술 제안, 증명 탐색, 전제 선택 등의 증명 자동화 도구를 제공한다.

## Motivation

- **Known**: 기존 신경 정리 증명(neural theorem proving) 연구들은 LLM을 증명보조기와 결합하여 자동 증명을 목표로 했으나, 고정된 학습 데이터로 인해 새로운 영역의 정리 증명에 어려움을 겪고 있다. 현재 LLM 기반 증명기들은 완전 자율 모드에서만 작동하며 인간과의 협력을 고려하지 않는다.
- **Gap**: 기존 LLM 기반 증명기들은 완전히 자동화된 증명을 추구하지만, 실제로는 새로운 영역의 정리나 도전적인 정리 증명에서 성능이 낮다. 또한 Lean의 기호 체계에 LLM 추론을 직접 통합하는 기술적 도전이 미충족 상태이다.
- **Why**: 현실의 수학자들은 직관보다 전제 검색(premise lookup) 같은 반복적 작업에 많은 시간을 소비한다. LLM이 copilot으로 작동하여 이러한 루틴 작업을 자동화하면 전문가는 고수준의 증명 전략에 집중할 수 있게 되어 생산성이 크게 향상된다.
- **Approach**: Lean 커널 내에서 직접 LLM 추론을 실행하는 일반 프레임워크를 설계했으며, 로컬 또는 서버 기반 실행을 모두 지원한다. 세 가지 주요 도구(전술 제안, 증명 탐색, 전제 선택)를 구현하고 ReProver 모델을 기본으로 사용하면서 사용자 정의 모델도 지원한다.

## Achievement

![Figure 2](figures/fig2.webp)

*Figure 2: The frontend of Lean Copilot’s SUGGEST_TACTICS. The user imports Lean Copilot just*

- **프레임워크 개발**: Lean 커널에서 직접 실행 가능한 LLM 추론 프레임워크(Lean Copilot) 구현. 로컬(GPU 有無) 및 클라우드 기반 추론을 모두 지원
- **자동화 성능**: SEARCH_PROOF가 평균 74.2%의 증명 스텝 자동화 달성 (AESOP 대비 85% 향상)
- **인간 보조 성능**: 인간 수학자 보조 시 평균 2.08개의 수동 입력만 필요 (AESOP 3.86개 vs)
- **실용적 배포**: MIT 라이선스로 오픈소스 공개, Lean 패키지로 간단히 설치 가능하여 커뮤니티 채택 용이
- **투명성**: 평가 코드 및 상세 결과를 공개하여 재현성 보장

## How

![Figure 1](figures/fig1.webp)

*Figure 1: Lean Copilot provides a general framework for running LLM inference in Lean, either*

- CTranslate2를 사용하여 로컬에서 LLM 추론을 효율적으로 실행하거나 서버 프로세스 통신을 통해 원격 실행 지원
- ReProver 모델의 전제 검색(premise retrieval) 능력을 활용하여 관련 보조정리(lemma) 자동 식별
- Best-first 탐색 알고리즘과 LLM 신뢰도 점수를 결합하여 완전한 증명 탐색 (SEARCH_PROOF)
- 단일 전술 생성(tactic generation)과 증명 탐색을 결합하여 단계적 증명 자동화
- Mathematics in Lean 교과서 전체에서 평가하여 실제 사용성 검증
- 텍스트-텍스트 및 텍스트-벡터 생성용 저수준 인터페이스 제공으로 확장 가능한 설계

## Originality

- **최초의 실용적 LLM-증명보조기 통합**: 기존 연구와 달리 실제 Lean 워크플로우에서 사용 가능한 도구로 구현한 최초 사례
- **Copilot 패러다임 도입**: 완전 자동화 대신 인간-AI 협력을 강조하는 새로운 접근법으로, 현실의 수학자 작업에 맞춤
- **Lean 내부 추론 기술**: 기호 체계인 Lean에서 신경망 추론을 직접 실행하는 기술적 혁신
- **멀티레벨 자동화**: 단일 전술 제안부터 완전 증명 탐색까지 다양한 수준의 자동화 도구 제공

## Limitation & Further Study

- **도메인 일반화 제한**: ReProver 모델이 학습 데이터와 다른 영역의 정리 증명에서 성능 저하 (논문에서도 언급)
- **모델 의존성**: 기본 모델(ReProver)의 성능이 전체 시스템 성능을 결정하므로, 더 강력한 LLM 필요
- **확장성 미검증**: Mathematics in Lean만 평가했으므로, Mathlib4 전체 또는 다른 증명보조기(Coq, Isabelle)에서의 성능 미확인
- **계산 비용 분석 부재**: 로컬 vs 서버 기반 실행의 효율성 트레이드오프 미상세 분석
- **후속연구 방향**: (1) 더 강력한 증명 생성 LLM 통합, (2) 자동화된 증명 데이터가 LLM 재학습에 미치는 긍정적 피드백 루프 구현, (3) 다른 형식 검증 시스템으로 확장, (4) 인간-AI 협력의 최적 상호작용 패턴 연구

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 논문은 LLM을 증명보조기에 실제로 통합하는 실용적이면서도 혁신적인 접근법을 제시하며, 완전 자동화 대신 인간 전문가를 보조하는 copilot 패러다임을 도입함으로써 현실 수학자의 생산성 향상에 직접 기여한다. 오픈소스 공개와 높은 자동화 성능(AESOP 대비 85% 향상)으로 학계와 실무에 즉시 임팩트를 미칠 수 있는 우수한 연구이다.

## Related Papers

- 🔄 다른 접근: [[papers/642_Proving_theorems_recursively/review]] — 완전 자동화된 재귀적 증명과 달리 인간 수학자와 AI의 협업을 통한 증명 보조 접근
- 🧪 응용 사례: [[papers/030_A_survey_on_deep_learning_for_theorem_proving/review]] — 정리 증명 심층학습 서베이에서 제시된 방법론들을 실제 Lean 환경에서 구현한 응용
- 🏛 기반 연구: [[papers/617_Phi-4_technical_report/review]] — 수학적 추론에 강한 Phi-4와 같은 모델을 정리 증명 보조 도구로 활용할 기반
- 🔗 후속 연구: [[papers/264_Deepseek-prover_Advancing_theorem_proving_in_llms_through_la/review]] — DeepSeek-Prover의 LLM 기반 증명 방법을 인간-AI 협업 환경으로 확장
- 🧪 응용 사례: [[papers/539_Minif2f_a_cross-system_benchmark_for_formal_olympiad-level_m/review]] — miniF2F 벤치마크를 활용하여 LLM 기반 정리 증명 코파일럿의 성능을 체계적으로 평가
- 🧪 응용 사례: [[papers/251_Data_for_mathematical_copilots_Better_ways_of_presenting_pro/review]] — 수학 코파일럿의 데이터 요구사항을 LLM 기반 정리 증명 도구 개발에 적용
- 🔄 다른 접근: [[papers/642_Proving_theorems_recursively/review]] — Lean Copilot의 인간-AI 협업 접근과 달리 완전 자동화된 재귀적 증명 방식 추구
- 🏛 기반 연구: [[papers/030_A_survey_on_deep_learning_for_theorem_proving/review]] — 정리 증명 자동화 연구 동향이 Lean Copilot과 같은 실용적 도구 개발의 기반
