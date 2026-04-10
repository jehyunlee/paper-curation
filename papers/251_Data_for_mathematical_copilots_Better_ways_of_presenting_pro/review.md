---
title: "251_Data_for_mathematical_copilots_Better_ways_of_presenting_pro"
authors:
  - "Simon Frieder"
  - "Jonas Bayer"
  - "Sam Looi"
  - "Jacob Loader"
  - "Julius Berner"
date: "2024"
doi: "arXiv:2412.15184"
arxiv: ""
score: 4.3
essence: "현재 수학 AI 모델(특히 대형 언어 모델)을 훈련하고 평가하는 데 사용되는 데이터셋과 벤치마크는 수학 정리의 최종 증명만을 다루며, 증명의 동기, 발견 과정, 수학자의 사고 과정 등 더 풍부한 측면을 담지 못하고 있다. 본 논문은 수학적 코파일럿(mathematical copilots)의 능력 향상을 위해 데이터셋 설계와 평가 기준의 근본적인 개선이 필요함을 주장한다."
tags:
  - "cat/Scientific_Language_Processing_and_Visualization"
  - "sub/Formal_Theorem_Proving"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Borji_2024_Data for mathematical copilots Better ways of presenting proofs for machine learning.pdf"
---

# Data for mathematical copilots: Better ways of presenting proofs for machine learning

> **저자**: Simon Frieder, Jonas Bayer, Sam Looi, Jacob Loader, Julius Berner, Katherine M. Collins 외 | **날짜**: 2024 | **DOI**: [arXiv:2412.15184](https://arxiv.org/abs/2412.15184)

---

## Essence

현재 수학 AI 모델(특히 대형 언어 모델)을 훈련하고 평가하는 데 사용되는 데이터셋과 벤치마크는 수학 정리의 최종 증명만을 다루며, 증명의 동기, 발견 과정, 수학자의 사고 과정 등 더 풍부한 측면을 담지 못하고 있다. 본 논문은 수학적 코파일럿(mathematical copilots)의 능력 향상을 위해 데이터셋 설계와 평가 기준의 근본적인 개선이 필요함을 주장한다.

## Motivation

- **Known**: AlphaGeometry, GPT-4 등이 높은 수학 성능을 보이고 있으며, 여러 벤치마크에서 근포화(near-saturation) 상태에 도달하고 있다.

- **Gap**: 
  - 제한된 수학 복잡도 범위 (특정 데이터셋의 과도한 연구)
  - 최종 증명만 학습 데이터로 사용되고 증명 발견 과정은 미포함
  - Goodhart's law 현상: 벤치마크 성능이 개발 목표가 되면서 벤치마크 자체가 신뢰도 저하
  - 수학자의 다양한 연구 워크플로우가 데이터셋에 반영되지 않음

- **Why**: 현재 데이터셋은 정리 문장을 증명으로 직접 매핑하는 "결과 기반" 접근만 지원하여, 정말의 수학적 능력을 평가하기 어렵다.

- **Approach**: G. Pólya의 "motivated proof" 개념(1949)을 활용하여 증명 과정, 발견 과정, 중간 추론을 담는 더 풍부한 데이터셋 설계를 제안한다.

## Achievement

1. **3가지 모델 분류 체계 제시**:
   - 좁은(narrow) 모델: 특정 수학 영역 전문화, 형식 언어 필요 (예: AlphaGeometry, Newclid)
   - 광범위(broad) 모델: 일반 목적의 수학 코파일럿, 자연언어 상호작용, LLM 기반
   - 보편(universal) 모델: 완전 자동화, 향후 "AI 수학자"로 진화 가능

2. **현재 데이터셋의 4가지 체계적 문제점 규명**:
   - GSM8K 같은 특정 데이터셋 과도 연구
   - 고급 수학, 도구 사용 관련 데이터 부족
   - 형식 언어 vs. 자연언어 표현의 불일치
   - 평가의 확장성 문제

3. **수학 AI를 위한 데이터 감사 필요성 제기**: 윤리, 데이터 관리, 환경 발자국 등 도메인 특화 평가 기준 부재를 지적

## How

- **"motivated proof" 개념 활용**: 증명뿐만 아니라 증명을 하게 된 동기, 관련 개념, 대안적 접근 방식을 포함하는 데이터셋 설계

- **하이브리드 아키텍처 제안**:
  - Tool-integrated reasoning: LLM이 기호 시스템(symbolic systems)에 위임
  - Mixture-of-experts: 특화된 LLM 모듈 조합

- **증명 프로세스 감독(supervision)**: 최종 정답 여부만 아닌 중간 추론 단계 학습

- **워크플로우 기반 벤치마크**: 실제 수학자의 연구 방식(가설 생성, 반례 탐색 등)을 반영

- **형식-비형식 정렬(Formal-informal alignment)**: 같은 수학 내용을 여러 표현 방식으로 제공

## Originality

- **핵심 기여**: 수학 AI 데이터셋의 체계적 비판적 분석과 Pólya의 고전 개념을 현대 머신러닝에 재해석

- **새로운 관점**: 
  - "Bitter lesson"이 수학 분야에 직접 적용되지 않을 수 있음을 논증
  - 고품질 수학 데이터의 희소성과 암묵적 지식의 중요성 강조
  - End-to-end 학습이 수학에서는 한계가 있을 수 있음 지적

- **학제적 통합**: 도서관학, 기록학의 데이터 큐레이션 원칙을 머신러닝에 적용 제안

## Limitation & Further Study

- **한계**:
  - 구체적인 motivated proof 데이터셋 구현 사례 미제시 (제안 수준)
  - 데이터 큐레이션의 실제 비용 및 확장성 분석 부재
  - 형식 언어와 자연언어 정렬의 구체적 방법론 미상세
  - 다양한 증명 표현 스타일 반영 방안 불명확

- **후속 연구**:
  - Motivated proof 형식의 대규모 데이터셋 구축 (수학 커뮤니티 협력)
  - 도메인 특화 평가 메트릭 개발
  - 중간 추론 감독의 효과 실증적 검증
  - 형식-비형식 정렬 자동화 기법
  - 수학 교육학 관점에서의 증명 표현 최적화 연구

## Evaluation

- **Novelty**: 4.5/5
  - 수학 AI 데이터셋에 대한 최초의 체계적 비판적 분석
  - Pólya 개념의 창의적 재해석
  - 다만 개념 수준 제안으로 구체 구현은 미흡

- **Technical Soundness**: 4/5
  - 논리적 주장 일관성 우수
  - 기존 벤치마크 한계 분석 철저함
  - 구현 가능성 검증 부족

- **Significance**: 4.5/5
  - 수학 AI 커뮤니티의 방향성에 중대한 영향 가능
  - Goodhart's law 지적이 매우 타당
  - 실제 정책 변화로 전환되기까지의 과정 불명확

- **Clarity**: 4/5
  - 명확한 문제 정의와 분류 체계
  - 매우 긴 원고에서 핵심 메시지 일관성 유지
  - 기술적 세부사항과 개념의 균형 양호

- **Overall**: 4.3/5

**총평**: 수학 AI 분야의 데이터 기반 발전에 대한 중요한 성찰을 제공하며, Pólya의 "motivated proof"를 통해 실질적 개선 방향을 제시한 점이 우수하나, 구체적 구현 및 실증 검증 부족이 한계이다. 학계와 산업계 모두에 영향력 높은 문제 제기 논문이다.

## Related Papers

- 🔗 후속 연구: [[papers/539_Minif2f_a_cross-system_benchmark_for_formal_olympiad-level_m/review]] — miniF2F의 정적 증명 평가를 동기와 발견 과정을 포함한 풍부한 수학적 사고로 확장
- ⚖️ 반론/비판: [[papers/264_Deepseek-prover_Advancing_theorem_proving_in_llms_through_la/review]] — DeepSeek-Prover의 대규모 데이터 접근법과 달리 증명의 질적 측면과 사고 과정을 중시
- 🏛 기반 연구: [[papers/288_Draft_sketch_and_prove_Guiding_formal_theorem_provers_with_i/review]] — 비형식적 증명의 풍부한 정보가 형식적 증명 스케치 생성에 필수적임을 보여줌
- 🧪 응용 사례: [[papers/1095_Towards_large_language_models_as_copilots_for_theorem_provin/review]] — 수학 코파일럿의 데이터 요구사항을 LLM 기반 정리 증명 도구 개발에 적용
- 🏛 기반 연구: [[papers/288_Draft_sketch_and_prove_Guiding_formal_theorem_provers_with_i/review]] — 비형식적 증명의 중요성을 강조하며 형식 시스템과의 연결점을 제시
- ⚖️ 반론/비판: [[papers/264_Deepseek-prover_Advancing_theorem_proving_in_llms_through_la/review]] — 대규모 데이터 합성 접근법과 달리 증명의 동기와 사고 과정의 중요성을 간과할 수 있음
