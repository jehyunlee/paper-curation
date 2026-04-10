---
title: "339_Fimo_A_challenge_formal_dataset_for_automated_theorem_provin"
authors:
  - "Chengwu Liu"
  - "Jianhao Shen"
  - "Huajian Xin"
  - "Zheng‐Ying Liu"
  - "Ye Yuan"
date: "2023"
doi: "arXiv:2309.04295"
arxiv: ""
score: 4.0
essence: "국제수학올림피아드(IMO) 수준의 149개 형식적 수학 문제와 자연언어 증명을 포함한 FIMO 데이터셋을 제시하며, 대규모언어모델(LLM)의 자동정리증명(Automated Theorem Proving, ATP) 능력이 IMO 수준에서 여전히 부족함을 보여준다."
tags:
  - "cat/LLM-Based_Scientific_Reasoning"
  - "sub/Domain-specific_Scientific_Reasoning"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Liu et al._2023_Fimo A challenge formal dataset for automated theorem proving.pdf"
---

# Fimo: A challenge formal dataset for automated theorem proving

> **저자**: Chengwu Liu, Jianhao Shen, Huajian Xin, Zheng‐Ying Liu, Ye Yuan, Haiming Wang, Lili Ju, Chuanyang Zheng, Yichun Yin, Lin Li, Ming Zhang, Qun Liu | **날짜**: 2023 | **DOI**: [arXiv:2309.04295](https://arxiv.org/abs/2309.04295)

---

## Essence

국제수학올림피아드(IMO) 수준의 149개 형식적 수학 문제와 자연언어 증명을 포함한 FIMO 데이터셋을 제시하며, 대규모언어모델(LLM)의 자동정리증명(Automated Theorem Proving, ATP) 능력이 IMO 수준에서 여전히 부족함을 보여준다.

## Motivation

- **Known**: 
  - 형식수학 데이터는 전문가의 노력이 많이 필요하여 극도로 부족함 (mathlib은 45MB vs GPT-3 훈련데이터 570GB)
  - 기존 형식수학 데이터셋(miniF2F)은 40개 정도만 실제 IMO 문제를 포함하며, 대부분 낮은 난이도
  - 기존 데이터셋은 형식 명제만 제공하고 자연언어 증명이 부재

- **Gap**: 
  - IMO 수준의 도전적 형식수학 문제 데이터셋 부족
  - 형식 명제와 자연언어 증명을 모두 포함한 완전한 데이터셋 없음
  - LLM의 IMO 수준 자동정리증명 능력 평가 기준 부재

- **Why**: 
  - IMO는 인간의 수학적 능력의 신뢰할 수 있는 지표이며, LLM의 복잡한 수학적 추론 능력 평가에 적합

- **Approach**: 
  - IMO 예비문제(Shortlisted Problems)를 자동형식화(auto-formalization)하여 정식화 비용 감소
  - 인간과 환경 피드백을 반복적으로 활용하여 형식화 성공률 향상
  - 형식 명제와 자연언어 증명을 모두 제공하는 완전한 데이터셋 구축

## Achievement

![Figure 1: 자동형식화 피드백 파이프라인](figures/fig1.webp)
*OCR → 자동형식화 → Lean 검증 → 반영 → 수동 검증 단계*

1. **FIMO 데이터셋 구축**: Lean 형식 언어로 작성된 149개 IMO 수준 형식 명제와 대응하는 자연언어 명제 및 증명 제공

2. **동적 피드백 기반 자동형식화**: LLM의 반성(reflection) 능력을 활용하여 Lean 컴파일러 오류 메시지와 인간 피드백을 반복적으로 제공, 형식화 성능 대폭 향상

3. **GPT-4 기준선 평가**: GPT-4를 데이터셋에 대해 평가하여 현재 LLM의 IMO 수준 정리증명의 심각한 한계 입증

## How

- **데이터셋 구성 파이프라인**:
  - **OCR 단계**: Mathpix 도구를 이용하여 IMO 예비문제 PDF를 LaTeX 코드로 변환, 수동 검증
  - **도메인 선택**: 형식화가 상대적으로 용이한 대수(Algebra)와 정수론(Number Theory) 문제만 선정
  - **증명 지향적 변환**: "예시 찾기" 형 문제를 "증명 가능한 명제"로 변환하여 형식화 가능성 확보

- **자동형식화 방법론**:
  - Wu et al.(2022)의 자동형식화 방법 기반으로 Isabelle 기반 few-shot 프롬프트를 Lean으로 수동 재작성
  - LLM 생성 형식 명제를 Lean 타입체커로 검증
  - 컴파일 오류 메시지 및 인간 피드백을 prompt에 반영하여 재생성 반복

- **수동 검증**: 모든 형식 명제가 원본 자연언어 명제와 의미론적으로 정렬되어 있는지 전문가 검토

## Originality

- **IMO 특화 데이터셋**: 기존 miniF2F(40개 IMO 문제)와 달리 149개 실제 IMO 예비문제로 구성된 대규모 고난이도 데이터셋 제공

- **다중 양식 통합**: 형식 명제(Lean)와 자연언어 명제/증명을 모두 제공하여, 형식-자연언어 연결 학습 및 DSP(Draft, Sketch, Prove) 같은 방법론 적용 가능

- **동적 피드백 형식화**: 단순 few-shot 형식화를 넘어 컴파일러 오류와 인간 피드백을 반복적으로 활용하는 체계적 방법론 제시

- **대규모 검증**: 149개 모든 형식 명제를 수동 검증하여 데이터 품질 보증

## Limitation & Further Study

- **도메인 제한**: 기하(Geometry)와 조합론(Combinatorics) 제외로 인해 IMO 문제의 약 50% 미포함 (Lean의 기하/조합론 라이브러리 미성숙)

- **제한된 모델 평가**: GPT-4만 평가하였으며, 다른 LLM(Claude, Gemini 등) 및 전문 ATP 도구(automated tactics generators) 미평가

- **형식화 완성도**: 자동형식화 성공 여부에 대한 정확한 통계 미제시 (논문 발췌 부분에서 결과 구체화 필요)

- **후속 연구 방향**:
  - 기하/조합론 도메인의 형식화 도구 개선
  - 형식-자연언어 상호 활용 학습 방법 개발
  - 인간 피드백 최소화를 위한 자동 피드백 생성 기법 연구

## Evaluation

- **Novelty**: 4/5
  - IMO 예비문제 기반 대규모 고난이도 데이터셋은 신규이나, 자동형식화 기법 자체는 기존 연구 기반

- **Technical Soundness**: 4/5
  - OCR-자동형식화-수동검증 파이프라인 체계적이고 합리적이나, 피드백 메커니즘의 상세 설명 부족

- **Significance**: 4/5
  - IMO 수준 ATP 연구에 중요한 벤치마크 제공하나, 도메인 제한과 모델 평가 부족으로 영향 제한

- **Clarity**: 4/5
  - 전반적으로 명확한 서술이나, 형식화 성공률, 사례 연구 결과 등 구체적 수치 제시 필요

- **Overall**: 4/5

**총평**: FIMO는 IMO 수준의 형식수학 벤치마크를 제공하는 가치 있는 데이터셋이지만, 기하/조합론 미포함 및 제한된 모델 평가를 보완하면 더욱 강력한 기여가 가능하다.

## Related Papers

- 🏛 기반 연구: [[papers/200_Chartist_Task-driven_Eye_Movement_Control_for_Chart_Reading/review]] — 수학 올림피아드 형식 문제가 차트 읽기 작업의 고차원 인지 능력 평가 기준
- 🔗 후속 연구: [[papers/264_Deepseek-prover_Advancing_theorem_proving_in_llms_through_la/review]] — IMO 수준 정리증명을 LLM 기반 증명으로 확장한 자동정리증명 발전
- 🔄 다른 접근: [[papers/539_Minif2f_a_cross-system_benchmark_for_formal_olympiad-level_m/review]] — IMO vs Olympiad 수준으로 유사하지만 다른 형식의 수학 정리증명 벤치마크
- 🏛 기반 연구: [[papers/808_Theoremqa_A_theorem-driven_question_answering_dataset/review]] — 정리 기반 질의응답이 형식적 수학 문제 해결의 방법론적 기초
- 🧪 응용 사례: [[papers/200_Chartist_Task-driven_Eye_Movement_Control_for_Chart_Reading/review]] — 수학 문제 해결에서의 시각적 주의 제어를 차트 읽기 작업으로 확장한 응용
- 🧪 응용 사례: [[papers/568_Mustard_Mastering_uniform_synthesis_of_theorem_and_proof_dat/review]] — 자동 정리 증명 분야의 실제 도전 과제들에 MUSTARD의 고품질 데이터를 적용할 수 있다
- 🔄 다른 접근: [[papers/182_Can_language_models_falsify_evaluating_algorithmic_reasoning/review]] — 형식 추론에서 LLM vs 전통적 자동 정리 증명의 다른 접근법을 비교할 수 있다
