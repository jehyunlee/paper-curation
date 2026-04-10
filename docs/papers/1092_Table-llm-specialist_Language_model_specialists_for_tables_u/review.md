---
title: "1092_Table-llm-specialist_Language_model_specialists_for_tables_u"
authors:
  - "Ziwei Ji"
  - "Tiezheng Yu"
  - "Yan Xu"
  - "Nayeon Lee"
  - "Etsuko Ishii"
date: "2024"
doi: ""
arxiv: ""
score: 4.0
essence: "테이블 작업(데이터 정제, NL-to-SQL 등)에 특화된 언어모델을 만들기 위해 생성-검증 이중 작업의 반복적 미세조정 패러다임인 Table-Specialist를 제안한다. 수동 레이블 없이 자동 생성된 훈련 데이터로 강력한 성능과 일반화를 동시에 달성한다."
tags:
  - "cat/Scientific_Language_Processing_and_Visualization"
  - "sub/Domain-adapted_Instruction_Models"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Ji et al._2024_Table-llm-specialist Language model specialists for tables using iterative generator-validator fine.pdf"
---

# Table-llm-specialist: Language model specialists for tables using iterative generator-validator finetuning

> **저자**: Ziwei Ji, Tiezheng Yu, Yan Xu, Nayeon Lee, Etsuko Ishii, Pascale Fung | **날짜**: 2024 | **URL**: [https://arxiv.org/abs/2410.12164](https://arxiv.org/abs/2410.12164)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1: Performance vs. generalizability trade-offs: A visual comparison of different fine-tuning approaches for table*

테이블 작업(데이터 정제, NL-to-SQL 등)에 특화된 언어모델을 만들기 위해 생성-검증 이중 작업의 반복적 미세조정 패러다임인 Table-Specialist를 제안한다. 수동 레이블 없이 자동 생성된 훈련 데이터로 강력한 성능과 일반화를 동시에 달성한다.

## Motivation

- **Known**: GPT와 Llama 같은 대규모 언어모델은 자연어 작업에서 우수하지만, 테이블 작업에서는 성능이 부족하다. 기존 미세조정은 데이터셋별 미세조정(높은 성능, 낮은 일반화)과 범용 모델 미세조정(높은 일반화, 낮은 성능) 간의 trade-off 문제가 있다.
- **Gap**: 데이터셋별 미세조정은 한 벤치마크에서는 잘 작동하지만 다른 데이터셋으로 전이될 때 과적합으로 인해 성능 저하가 발생한다. 테이블 작업의 특수성을 활용한 전문화된 미세조정 방법이 부족하다.
- **Why**: 실제 사용 환경에서는 테스트 데이터를 미리 알 수 없으므로 다양한 테이블에 대해 일반화되면서도 높은 성능을 유지하는 모델이 필수적이다. 또한 더 작은 모델으로 GPT-4 수준의 성능을 달성하면 비용과 지연 시간을 크게 줄일 수 있다.
- **Approach**: 테이블 작업의 이중성(생성 작업과 분류 작업의 상호 대응)을 활용하여 Generator-Validator 패러다임을 제안한다. 생성 모델과 분류 모델을 반복적으로 미세조정하여 서로 생성한 데이터를 검증함으로써 수동 레이블 없이 훈련 데이터를 자동으로 생성한다.

## Achievement

![Figure 3](figures/fig3.webp)

*Figure 3: “Table-Specialist fine-tuning”: Quality vs. latency*

- **성능 향상**: Table-Specialist-GPT-3.5가 vanilla GPT-3.5뿐만 아니라 GPT-4 수준의 성능을 초과하여 달성, 여러 테이블 작업에서 입증됨
- **비용 효율성**: GPT-4 수준의 성능을 더 작은 모델(GPT-3.5)로 달성하여 배포 비용과 지연 시간 대폭 감소
- **일반화 능력**: 다양한 실제 테이블에서 체계적으로 생성된 훈련 데이터로 여러 벤치마크 간 우수한 일반화 성능 달성
- **실무 적용**: Microsoft Excel의 자동 데이터 정제 등 실제 사용 사례에 통합됨

## How

![Figure 5](figures/fig5.webp)

*Figure 5: Architecture of Table-Specialist using “Generator-Validator” fine-tuning for a given task type 𝑇(Error detecti*

- 테이블 작업의 이중성 인식: 각 생성 작업(예: NL-to-SQL)과 대응하는 분류 작업(SQL 검증) 식별
- Generator-Validator 반복 프레임워크 구성: 생성 모델이 데이터 생성, 분류 모델이 검증하는 반복 루프
- 테이블 특성 활용: 순열 불변성(permutation-invariance)과 실행 불변성(execution-invariance) 같은 테이블 고유 특성으로 약한 감시 신호 활용
- 다양한 실제 테이블 데이터 수집: 단일 벤치마크 대신 다양한 출처의 테이블로 훈련 데이터 생성
- 과적합 방지: 광범위한 테이블 데이터로 인한 자연스러운 정규화 효과로 일반화 능력 향상

## Originality

- 테이블 도메인에서 이중 작업(dual-task) 학습 개념의 첫 적용 - 기존 기계 번역과 컴퓨터 비전의 이중 학습 아이디어를 테이블에 적용
- 테이블 특화 자동 레이블링: 순열/실행 불변성 같은 테이블 고유 특성을 활용한 약한 감시 신호 생성
- 성능-일반화 trade-off 해결: 범용 모델의 높은 일반화성과 특화 모델의 높은 성능을 동시에 달성하는 새로운 위치 제시
- 대규모 언어모델의 과적합 문제 재조명: 175B 규모 GPT-3.5 같은 큰 모델도 테이블 작업에서 과적합 발생 입증

## Limitation & Further Study

- 각 테이블 작업마다 별도의 전문화 모델 필요: 다양한 작업에 대응하려면 여러 모델 관리 필요로 복잡도 증가
- 이중 작업이 존재하지 않는 테이블 작업에 대한 적용 가능성 미제시: 일방향 작업(unidirectional task)에 대한 확장 방안 부족
- 생성-검증 반복 프로세스의 수렴 조건과 최적화 전략에 대한 상세 분석 부족
- 후속 연구: 다중 작업 처리 능력이 있으면서도 높은 성능을 유지하는 하이브리드 접근법 개발, 이중 작업이 없는 경우의 대안 메커니즘 개발

## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 테이블 작업의 이중성을 창의적으로 활용하여 수동 레이블 없이도 높은 성능과 일반화를 동시에 달성한 혁신적 연구이다. Microsoft Excel 통합 등 실무 적용 가능성이 높으며, 특화-일반화 trade-off 문제 해결에 새로운 방향을 제시한다.

## Related Papers

- 🔄 다른 접근: [[papers/348_FRAG_A_Flexible_Modular_Framework_for_Retrieval-Augmented_Ge/review]] — RAG 프레임워크의 유연성 추구와 달리 테이블 작업에 특화된 전문 모델 개발 접근
- 🏛 기반 연구: [[papers/231_Codegen_An_open_large_language_model_for_code_with_multi-tur/review]] — 다중 턴 프로그램 합성 방법론을 테이블 작업 특화 모델 훈련에 적용한 기반
- 🧪 응용 사례: [[papers/751_SFT_Memorizes_RL_Generalizes_A_Comparative_Study_of_Foundati/review]] — 테이블 전문가 모델에서 생성-검증 이중 작업이 SFT 대비 일반화 성능 향상에 기여
- 🔗 후속 연구: [[papers/841_Tree-of-table_Unleashing_the_power_of_llms_for_enhanced_larg/review]] — 테이블 처리 능력을 Tree-of-Table 방법론으로 더욱 체계화한 확장 연구
- 🔗 후속 연구: [[papers/231_Codegen_An_open_large_language_model_for_code_with_multi-tur/review]] — 프로그램 합성 기법을 테이블 작업 특화 모델의 반복적 미세조정에 적용한 확장
- 🔄 다른 접근: [[papers/348_FRAG_A_Flexible_Modular_Framework_for_Retrieval-Augmented_Ge/review]] — 테이블 작업 전문가 모델과 달리 지식그래프 기반 RAG의 유연성을 통한 범용적 접근
