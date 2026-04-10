---
title: "770_Starcoder_2_and_the_stack_v2_The_next_generation"
authors:
  - "Anton Lozhkov"
  - "Raymond Li"
  - "Loubna Ben Allal 외 다수 (Hugging Face"
  - "ServiceNow Research"
  - "Nvidia 등)"
date: "2024"
doi: "arXiv:2402.19173"
arxiv: ""
score: 4.5
essence: "BigCode 프로젝트에서 개발한 StarCoder2와 The Stack v2는 619개 프로그래밍 언어를 지원하는 대규모 오픈소스 코드 데이터셋과 이를 기반으로 훈련된 3B, 7B, 15B 규모의 코드 생성 모델로, 동일 규모의 기존 모델들을 능가하고 2배 이상 큰 모델과 비교 가능한 성능을 달성했다."
tags:
  - "cat/AI-Powered_Scientific_Research_Frameworks"
  - "sub/Scientific_Code_Generation"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/DeepSeek-AI et al._2024_Starcoder 2 and the stack v2 The next generation.pdf"
---

# StarCoder 2 and the Stack v2: The next generation

> **저자**: Anton Lozhkov, Raymond Li, Loubna Ben Allal 외 다수 (Hugging Face, ServiceNow Research, Nvidia 등) | **날짜**: 2024 | **DOI**: [arXiv:2402.19173](https://arxiv.org/abs/2402.19173)

---

## Essence

BigCode 프로젝트에서 개발한 StarCoder2와 The Stack v2는 619개 프로그래밍 언어를 지원하는 대규모 오픈소스 코드 데이터셋과 이를 기반으로 훈련된 3B, 7B, 15B 규모의 코드 생성 모델로, 동일 규모의 기존 모델들을 능가하고 2배 이상 큰 모델과 비교 가능한 성능을 달성했다.

## Motivation

- **Known**: Code LLM(대규모 언어 모델)은 개발자 생산성 향상(56% 증가)에 효과적이나, 대부분의 오픈 가중치 모델(CodeLlama, DeepSeekCoder)은 훈련 데이터를 공개하지 않음
- **Gap**: 데이터셋 비공개로 인해 ①콘텐츠 크리에이터의 데이터 사용 여부 파악 불가, ②편향성·독성 검증 불가, ③벤치마크 오염(contamination) 수준 파악 불가, ④과학적 재현성 및 재사용성 저하
- **Why**: 책임감 있고 투명한 Code LLM 개발 필요 → 완전 공개 접근(training data, framework, evaluation suite 모두 공개)
- **Approach**: Software Heritage 아카이브 기반으로 The Stack v2(900B+ unique tokens) 구축, 고품질 데이터 소스 다층화(GitHub PR, Kaggle, documentation), 투명한 데이터 관리(SWHID 공개, opt-out 지원)

## Achievement

1. **모델 성능**: 
   - StarCoder2-3B: 동급 모델(StableCode-3B, DeepSeekCoder-1.3B) 대비 우수, StarCoderBase-15B 능가
   - StarCoder2-15B: CodeLlama-13B 대비 유의미하게 우수, CodeLlama-34B와 동등 또는 우수 성능
   - DeepSeekCoder-33B보다 낮은 자원 언어(D, Julia, Lua, Perl) 및 코드 추론·수학 벤치마크에서 우수

2. **데이터셋 규모**: The Stack v1 대비 4배 확대(6.4TB → 900B+ tokens), 619개 프로그래밍 언어 지원

3. **투명성 구현**: SoftWare Heritage Persistent IDentifier(SWHID) 공개로 완전한 훈련 데이터 추적성 확보, OpenRAIL 라이선스 기반 모델 공개

## How

- **데이터 소스 다층화**:
  - Software Heritage 아카이브: 핵심 소스(GitHub 저장소 최신 버전, 주 브랜치만)
  - GitHub 이슈/PR, Kaggle/Jupyter 노트북
  - API 문서, 수학·코딩·추론 관련 자연어 데이터셋
  - 중간 표현(intermediate representations)

- **라이선스 전략**:
  - 저장소 레벨 라이선스 먼저 확인 → 파일 레벨 ScanCode Toolkit 적용
  - 허용 라이선스(permissive) + 미라이선스(unlicensed) 포함
  - 상업 라이선스·Copyleft 제외 (커뮤니티 우려)

- **데이터 정제 프로세스**:
  - 중복 제거(deduplication)
  - 저질 코드 필터링
  - PII(개인식별정보) 적색 처리
  - 악성 코드 제거
  - 개발자 opt-out 요청 처리

- **언어 감지**: 파일 확장자 대신 go-enry(GitHub linguist 기반) 언어 분류기 사용 → 658개 언어 감지

- **훈련 전략**:
  - 2단계 훈련: 4K 컨텍스트 윈도우 → 16K 컨텍스트 윈도우 파인튜닝
  - 3.3~4.3조 토큰으로 훈련 (Chinchilla 최적값 초과, 데이터 최대 5 에포크)

## Originality

- **완전 투명성**: SWHID 공개를 통한 훈련 데이터 완전 추적성 달성 (기존 모델과 차별)
- **대규모 다언어 지원**: 619개 언어 지원 (Stack v1의 384개 확대)
- **고품질 큐레이션**: 라이선스 기반 선별, 파일 레벨 라이선스 재판정 로직 개선
- **효율적 스케일링**: 컴퓨트 최적값 초과 훈련을 통한 소규모 모델의 대형 모델 대비 성능 달성
- **거버넌스 도구**: "Am I in The Stack" 등 개발자 친화적 opt-out 메커니즘

## Limitation & Further Study

- **StarCoder2-7B의 성능 이상**: 3B와 15B 모델은 우수하나 7B에서 상대적 성능 하락 → 명확한 원인 규명 필요
- **Copyleft 코드 제외**: 법적 불명확성으로 인한 제외로 일부 고품질 코드 손실 가능
- **데이터 오염 분석 미흡**: 벤치마크 오염 정도의 정량적 분석 부족
- **저자원 언어 성능**: 저자원 언어에서 DeepSeekCoder-33B 능가하나 절대 성능 수준의 추가 분석 필요
- **장기 보존 메커니즘**: Software Heritage 기반이나 지속적인 데이터 갱신 및 유지보수 전략 미상세


## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 5/5
- Clarity: 4/5
- Overall: 4.5/5

**총평**: 본 논문은 코드 LLM 분야에서 완전한 투명성을 구현한 획기적인 작업으로, 대규모 오픈소스 데이터셋과 이를 활용한 효율적인 모델 훈련을 통해 기존 폐쇄형 모델과 경쟁 가능한 성능을 달성했으며, 특히 다언어 지원과 거버넌스 측면에서 과학 커뮤니티에 실질적 기여를 제공한다. 다만 중간 규모(7B) 모델의 성능 이상과 copyleft 코드 제외의 정당성 심화 분석이 개선 필요 영역이다.

## Related Papers

- 🔗 후속 연구: [[papers/771_Starcoder_may_the_source_be_with_you_arXiv_preprint_arXiv230/review]] — StarCoder의 오픈소스 코드 생성 모델이 더 큰 규모와 다양한 언어 지원으로 발전한 차세대 버전이다
- 🏛 기반 연구: [[papers/320_Evaluating_Large_Language_Models_in_Scientific_Discovery/review]] — GitHub 코드 기반 모델 훈련과 함수형 정확성 평가 방법론이 대규모 오픈소스 코드 생성 모델 개발의 중요한 기반이 되었다
- 🧪 응용 사례: [[papers/135_Automl_in_the_age_of_large_language_models_Current_challenge/review]] — 대규모 코드 생성 모델의 성능 향상이 AutoML과 LLM의 상생적 통합을 통한 자동 최적화에 핵심적으로 기여한다
- 🧪 응용 사례: [[papers/712_SciCode_A_Research_Coding_Benchmark_Curated_by_Scientists/review]] — 다양한 프로그래밍 언어를 지원하는 코드 생성 모델이 과학자들의 실제 연구 문제 해결 능력 평가에 핵심적인 도구로 활용된다
- 🔄 다른 접근: [[papers/230_Code_llama_Open_foundation_models_for_code/review]] — 오픈소스 코드 생성을 위한 서로 다른 모델 아키텍처를 제시합니다.
- 🏛 기반 연구: [[papers/135_Automl_in_the_age_of_large_language_models_Current_challenge/review]] — AutoML과 LLM의 통합이 코드 생성 모델의 자동 최적화와 성능 향상에 필수적인 방법론적 기반을 제공한다
- 🏛 기반 연구: [[papers/320_Evaluating_Large_Language_Models_in_Scientific_Discovery/review]] — 함수형 정확성 기반 코드 평가 체계가 차세대 대규모 코드 생성 모델의 성능 측정과 개선에 필수적인 평가 기준을 제공했다
- 🏛 기반 연구: [[papers/771_Starcoder_may_the_source_be_with_you_arXiv_preprint_arXiv230/review]] — 오픈소스 코드 생성 모델의 책임감 있는 개발 원칙이 차세대 대규모 코드 모델 개발의 중요한 윤리적, 기술적 기반이 되었다
- 🔗 후속 연구: [[papers/263_Deepseek-coder_When_the_large_language_model_meets_programmi/review]] — StarCoder의 코드 생성 기술을 더 큰 규모와 상용 라이센스로 발전시킴
- 🔗 후속 연구: [[papers/741_Seed-coder_Let_the_code_model_curate_data_for_itself/review]] — StarCoder의 코드 생성 능력을 자가 큐레이션 데이터로 더욱 향상시킨 연구
