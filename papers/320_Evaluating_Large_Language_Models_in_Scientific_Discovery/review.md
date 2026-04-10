---
title: "320_Evaluating_Large_Language_Models_in_Scientific_Discovery"
authors:
  - "Mark Chen"
  - "Jerry Tworek"
  - "Heewoo Jun"
  - "Qiming Yuan"
  - "Henrique Pondé de Oliveira Pinto"
date: "2021"
doi: "N/A"
arxiv: ""
score: 4.5
essence: "GitHub 코드로 미세조정된 GPT 기반의 Codex 모델을 제시하고, 새로운 벤치마크인 HumanEval을 통해 함수형 정확성(functional correctness) 기반의 평가 체계를 제안한 논문이다. Codex는 도큐스트링(docstring)으로부터 Python 함수를 생성하는 능력에서 기존 모델들을 크게 능가한다."
tags:
  - "cat/AI-Powered_Scientific_Research_Frameworks"
  - "sub/Scientific_Code_Generation"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Chen et al._2021_Evaluating large language models trained on code.pdf"
---

# Evaluating large language models trained on code

> **저자**: Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Pondé de Oliveira Pinto, Jared Kaplan, Harrison Edwards, Yuri Burda, Nicholas Joseph, Greg Brockman, Alex Ray, Raul Puri, Gretchen Krueger, Michael Petrov, Heidy Khlaaf, Girish Sastry, Pamela Mishkin, Brooke Chan, Scott Gray, Nick Ryder | **날짜**: 2021 | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp)
*HumanEval 데이터셋에서 모델 크기에 따른 통과율. 단일 샘플 생성 시 Codex-12B는 28.8%, 100개 샘플 생성 후 단위 테스트 통과 샘플 선택 시 77.5% 달성*

GitHub 코드로 미세조정된 GPT 기반의 Codex 모델을 제시하고, 새로운 벤치마크인 HumanEval을 통해 함수형 정확성(functional correctness) 기반의 평가 체계를 제안한 논문이다. Codex는 도큐스트링(docstring)으로부터 Python 함수를 생성하는 능력에서 기존 모델들을 크게 능가한다.

## Motivation

- **Known**: GPT-3와 같은 대규모 언어 모델이 기본 프로그래밍 생성 능력을 보유하고 있지만, 코드 전용 모델의 성능은 체계적으로 평가되지 않았음. BLEU 스코어 등 텍스트 생성 메트릭은 의미적으로 동등하지만 표면적으로 다른 코드에 대해 신뢰성이 낮음.

- **Gap**: 코드 생성 모델을 평가할 수 있는 표준화된 벤치마크와 함수형 정확성 기반의 객관적 평가 메트릭이 부재함.

- **Why**: GitHub의 공개 코드 데이터가 풍부하고, 대규모 언어 모델이 다양한 도메인에서 성공했으므로 전문화된 코드 모델의 성능을 체계적으로 검증할 필요가 있음.

- **Approach**: (1) 164개의 수작업 프로그래밍 문제로 구성된 HumanEval 벤치마크 제작, (2) 단위 테스트 통과 여부로 평가하는 pass@k 메트릭 제안, (3) GitHub 코드로 GPT 모델 미세조정하여 Codex 개발, (4) 안전한 코드 실행 환경(sandbox) 구축.

## Achievement

![Figure 2](figures/fig2.webp)
*HumanEval 데이터셋의 3개 문제 예시와 Codex-12B가 생성한 정답. 도큐스트링만으로 함수를 완전히 구현하는 예시 제시*

1. **성능 향상**: 단일 샘플 기준 Codex-12B는 28.8% 해결률(GPT-3: 0%, GPT-J: 11.4%), 100개 샘플 생성 시 Codex-S는 77.5% 달성. 모델 크기 확대(300M → 12B)에 따른 성능 스케일링 확인.

2. **메트릭 기여**: pass@k 메트릭의 불편 추정량(unbiased estimator) 제안으로 샘플링 기반 평가의 분산(variance) 문제 해결. 함수형 정확성이 BLEU 점수보다 신뢰성 높음을 입증.

3. **평가 자산 공개**: 164개 문제의 HumanEval 벤치마크와 평가 프레임워크를 오픈소스로 공개하여 재현성 확보.

4. **실용적 응용**: 로그 확률(log-probability) 기반 샘플 선택으로 44.5% 해결률 달성 - 모든 샘플을 완전 평가할 수 없는 배포 환경에서 활용 가능.

## How

- **데이터 수집**: 2020년 5월 GitHub의 5,400만 공개 저장소에서 수집한 Python 파일(179GB → 필터링 후 159GB). 자동 생성 파일, 장행 코드 제거.

- **미세조정 전략**: GPT-3 모델 계열에서 출발(더 빠른 수렴). 사전학습된 자연어 표현 활용이지만, 미세조정 데이터셋 규모가 충분히 크면 성능 향상 제약.

- **Codex-S**: 올바르게 구현된 독립형 함수(standalone functions)로 추가 미세조정하여 37.7% 해결률 달성 - 도메인 특화의 효과 입증.

- **Pass@k 계산**: 
  ```
  pass@k = 1 - ∏(1 - k/(n-c+i)) for i=1 to k
  ```
  여기서 n=생성 샘플 수, c=정답 샘플 수. 단순 추정 1-(1-p̂)^k는 편향됨을 증명.

- **보안 샌드박스**: gVisor 컨테이너 런타임으로 호스트 리소스 에뮬레이션, eBPF 방화벽으로 악의적 네트워크 접근 차단.

## Originality

- **함수형 정확성 메트릭 도입**: 매칭 기반 메트릭(BLEU)의 한계를 지적하고 단위 테스트 기반 평가의 우월성을 체계적으로 입증. 프로그래밍 패러다임(테스트 주도 개발)과의 일맥상통.

- **Pass@k 불편 추정량 제안**: 표준 확률 추정이 높은 분산을 가질 때 수학적으로 안정적인 대안 제시 (Figure 3의 효율적 구현 포함).

- **HumanEval 벤치마크 구축**: GitHub 학습 데이터와의 오염(data contamination) 가능성을 인식하여 수작업 문제 생성. 인터뷰 스타일 질문으로 알고리즘 및 추론 능력 평가.

- **코드 생성 특화 모델 검증**: GPT 계열 모델을 코드에 맞춰 미세조정한 초기 대규모 시스템 평가. GitHub Copilot의 기술 기초 제시.

## Limitation & Further Study

- **HumanEval 규모**: 164개 문제는 포괄적 평가에 제한적. 프로그래밍 난이도 범위(소프트웨어 인터뷰 난이도)가 실무 복잡도와 거리 있음.

- **도큐스트링 의존성**: 모델이 명확한 자연어 사양(specification)을 요구. 불명확하거나 장쇄 연산 설명 시 성능 저하 - 변수 바인딩 문제 미해결.

- **단위 테스트 품질**: 경계 사례(edge cases) 포함 완전한 테스트 스위트가 항상 제공되지 않으면 거짓 양성(false positive) 가능성.

- **보안/윤리 평가 미흡**: 악의적 코드 생성 가능성, 라이선스 침해, 저작권 문제 등에 대한 정량적 분석 부재. 개요 수준의 논의만 포함.

- **후속 연구 방향**: (1) 더 복잡한 프로그래밍 작업(멀티파일, 라이브러리 활용)으로 확장, (2) 에러 수정 능력 평가, (3) 다국어 코드 지원, (4) 모델의 편향성 및 공정성 분석.

## Evaluation

- **Novelty**: 4/5 - 함수형 정확성 평가와 pass@k 메트릭은 새로우나, 개념 자체는 선행 연구(Kulal et al. 2019)에서 개시됨. HumanEval은 가치 있는 자산이나 규모 제약.

- **Technical Soundness**: 5/5 - 수학적 유도(pass@k 불편 추정량), 샌드박스 보안 설계, 데이터 필터링 전략이 엄밀함. 실험 설정 명확.

- **Significance**: 5/5 - GitHub Copilot의 기술 기초이며, 코드 생성 모델 평가의 표준 벤치마크 수립. 학계와 산업 모두에 광범위한 영향(인용 수 5000+).

- **Clarity**: 4/5 - 전반적으로 명확하나, 제한점(도큐스트링 의존성, 보안 우려)이 간략히 다루어짐. Figure 2의 구체적 예시는 도움이 됨.

- **Overall**: 4.5/5

**총평**: 이 논문은 코드 생성 모델의 평가 체계를 근본적으로 개선하고 실용적 벤치마크를 제공함으로써 프로그래밍 합성 분야에 중대한 기여를 했다. Codex 모델의 실제 성능은 놀라울 정도이나, 평가 범위의 한정과 윤리적 논의의 깊이 부족이 아쉬움.

## Related Papers

- 🏛 기반 연구: [[papers/770_Starcoder_2_and_the_stack_v2_The_next_generation/review]] — 함수형 정확성 기반 코드 평가 체계가 차세대 대규모 코드 생성 모델의 성능 측정과 개선에 필수적인 평가 기준을 제공했다
- 🏛 기반 연구: [[papers/771_Starcoder_may_the_source_be_with_you_arXiv_preprint_arXiv230/review]] — Codex의 코드 생성 능력 평가 방법론이 오픈소스 코드 생성 대형언어모델의 성능 측정과 벤치마킹에 중요한 기반이 되었다
- 🔗 후속 연구: [[papers/712_SciCode_A_Research_Coding_Benchmark_Curated_by_Scientists/review]] — 일반적인 코드 생성 평가가 과학자들이 직접 큐레이션한 과학 연구 문제 중심의 코딩 벤치마크로 구체화되었다
- 🔗 후속 연구: [[papers/671_Researchcodebench_Benchmarking_llms_on_implementing_novel_ma/review]] — 함수 생성 중심의 코드 평가가 새로운 기계학습 방법 구현을 위한 연구 코드 벤치마킹으로 확장되었다
- 🔗 후속 연구: [[papers/712_SciCode_A_Research_Coding_Benchmark_Curated_by_Scientists/review]] — 일반적인 프로그래밍 함수 생성 평가를 과학자들이 직접 설계한 실제 과학 연구 문제 해결 능력 평가로 발전시켰다
- 🏛 기반 연구: [[papers/770_Starcoder_2_and_the_stack_v2_The_next_generation/review]] — GitHub 코드 기반 모델 훈련과 함수형 정확성 평가 방법론이 대규모 오픈소스 코드 생성 모델 개발의 중요한 기반이 되었다
- 🏛 기반 연구: [[papers/771_Starcoder_may_the_source_be_with_you_arXiv_preprint_arXiv230/review]] — Codex의 코드 생성 평가 체계가 오픈소스 대형언어모델 기반 코드 생성의 성능 측정과 개선에 핵심적인 방법론을 제공했다
- 🏛 기반 연구: [[papers/1084_An_Autonomous_Large_Language_Model_Agent_for_Chemical_Litera/review]] — 자율 기계학습 연구 프레임워크는 코드 훈련된 대규모 언어모델의 평가 연구 결과를 기반으로 연구 코드 생성과 실험 자동화 기능을 구현합니다.
- 🏛 기반 연구: [[papers/010_A_hierarchical_framework_for_measuring_scientific_paper_inno/review]] — 코드 평가를 위한 LLM 활용 연구가 과학 논문의 혁신성을 측정하는 계층적 프레임워크 개발의 방법론적 기초를 제공함
