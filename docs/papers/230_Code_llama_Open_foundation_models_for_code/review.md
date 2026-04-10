---
title: "230_Code_llama_Open_foundation_models_for_code"
authors:
  - "Baptiste Rozière"
  - "Jonas Gehring"
  - "Fabian Gloeckle"
  - "Sten Sootla"
  - "Itai Gat"
date: "2023"
doi: "-"
arxiv: ""
score: 4.5
essence: "Code Llama는 Llama 2 기반의 오픈소스 코드 생성 대규모언어모델(Large Language Model, LLM) 계열로, 코드 인필링(infilling), 장문맥 처리, 명령어 추종 능력을 갖춘 차세대 코드 생성 모델이다. 7B부터 70B 파라미터까지 4가지 크기의 모델과 3가지 변형(기본, Python 특화, Instruct)을 제공하며, 공개 모델 중 최고 수준의 성능을 달성한다."
tags:
  - "cat/LLM-Based_Scientific_Reasoning"
  - "sub/Large_Language_Model_Agents"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Rozière et al._2023_Code llama Open foundation models for code.pdf"
---

# Code llama: Open foundation models for code

> **저자**: Baptiste Rozière, Jonas Gehring, Fabian Gloeckle, Sten Sootla, Itai Gat, Xiaoqing Tan, Yossi Adi, Jingyu Liu, Tal Remez, J. Rapin, Artyom Kozhevnikov, I. Evtimov, Joanna Bitton, Manish P Bhatt, Cristian Canton Ferrer, Aaron Grattafiori, Wenhan Xiong, Alexandre D'efossez, Jade Copet, Faisal Azhar | **날짜**: 2023 | **DOI**: -

---

## Essence

![Figure 2: Code Llama 특화 파이프라인. 다양한 미세조정(fine-tuning) 단계를 거쳐 기반 모델에서 Instruct 모델로 발전](figures/fig2.webp)

Code Llama는 Llama 2 기반의 오픈소스 코드 생성 대규모언어모델(Large Language Model, LLM) 계열로, 코드 인필링(infilling), 장문맥 처리, 명령어 추종 능력을 갖춘 차세대 코드 생성 모델이다. 7B부터 70B 파라미터까지 4가지 크기의 모델과 3가지 변형(기본, Python 특화, Instruct)을 제공하며, 공개 모델 중 최고 수준의 성능을 달성한다.

## Motivation

- **Known**: 기존의 AlphaCode, StarCoder 등 코드 생성 LLM은 주로 코드 데이터만으로 학습되었으며, Codex는 일반 언어 모델에서 미세조정되었다.

- **Gap**: 일반 목적 기반 모델에서 시작하는 것이 코드 전용 학습보다 나은지, 코드 인필링과 장문맥(100K 토큰) 처리를 효율적으로 지원하는 방법이 무엇인지, 그리고 다양한 프로그래밍 작업에서 실용적인 성능을 발휘하는 방법이 명확하지 않았다.

- **Why**: IDE에서의 실시간 코드 완성, 저장소 수준의 추론(repository-level reasoning), 안전하고 도움이 되는 코드 생성을 지원하려면 이러한 능력들이 필수적이다.

- **Approach**: Llama 2 기반에서 시작하여 단계적 특화를 수행한다: (1) 500B~1T 토큰의 코드 중심 데이터로 사전학습, (2) 인필링 목표(FIM, Fill-In-the-Middle) 추가, (3) RoPE 위치 임베딩 수정을 통한 장문맥 미세조정(16K→100K 토큰), (4) 지도 학습과 자기-지도(self-instruct) 데이터로 명령어 미세조정.

## Achievement

![Figure 1: Code Llama-Instruct(34B) 모델의 Bash 명령어 쿼리 응답 예시. 자연어 질문을 파싱하여 적절한 옵션을 제시하고 해설을 제공](figures/fig1.webp)

1. **벤치마크 성능**: HumanEval에서 최고 67%, MBPP에서 65% 달성(공개 모델 기준 최우수). Code Llama-Python 7B가 Llama 2 70B를 HumanEval과 MBPP에서 초과. MultiPL-E(다언어) 벤치마크에서 모든 공개 모델 초과.

2. **모델 다양성**: 기본 모델(Code Llama), Python 특화 모델(Code Llama-Python), 명령어 추종 모델(Code Llama-Instruct)로 상이한 사용 사례 커버. 7B, 13B, 34B, 70B 크기로 배포 확장성 제공.

3. **핵심 기능**: 인필링 가능 모델(7B, 13B, 70B)은 문서 중간의 코드 완성 지원. 최대 100K 토큰까지 처리 가능(16K 학습 후 fine-tuning). 자동생성 지도 데이터로 안전성과 진실성 개선.

## How

![Figure 2: Code Llama 특화 파이프라인. 기초 모델에서 출발하여 코드 학습(500B 토큰), 인필링, Python 특화(100B), 장문맥 미세조정, 명령어 미세조정(~5B) 단계 거침](figures/fig2.webp)

- **기반 선택**: Llama 2에서 초기화하여 일반 언어 이해 능력 유지. 코드 전용 학습 대비 우월함을 실증적으로 검증.

- **인필링 메커니즘**: 인과 마스킹(causal masking) 기반 FIM 목표. 훈련 문서를 접두사(prefix), 중간(middle), 접미사(suffix)로 분할(균일 분포 샘플링)하여 90% 확률로 변환. PSM(prefix-suffix-middle)과 SPM(suffix-prefix-middle) 형식 50:50 혼합. 토크나이저 특수 토큰 추가로 경계 표시.

- **장문맥 미세조정(LCFT)**: 위치 보간(position interpolation) 기반. RoPE의 회전 주파수 기본 주기(base period) 수정으로 4K→16K 학습, 추론 시 100K까지 확장. 계산 효율을 위해 LCFT를 별도 단계로 분리.

- **데이터 구성**: 공개 코드 데이터 92% + 코드 관련 자연언어 8%(StackOverflow 등). 자연언어 배치 샘플링으로 언어 이해 능력 보존.

- **명령어 미세조정**: Llama 2로 생성한 코딩 문제 + Code Llama가 생성한 단위 테스트(unit test) 및 솔루션으로 자기-지도 데이터셋 구성. 독점 지도 데이터와 혼합하여 안전성, 성실성, 편향 완화.

## Originality

- **기반 모델 활용의 정당화**: 코드 전용 학습 vs. 일반 기초 모델 미세조정 비교 실험으로 후자의 우월성을 실증 입증(구간 내 예산 동일).

- **FIM의 실용적 구현**: PSM/SPM 형식 혼합, 토크나이저 특수 토큰, 분포 이동(distribution shift) 완화 등 세밀한 설계로 인필링 효과 극대화.

- **위치 보간의 개선**: 기존 선형 다운스케일링 대신 기본 주기 수정으로 더 간단하고 효과적인 장문맥 확장.

- **자기-지도 데이터셋**: 모델 자신이 생성한 단위 테스트와 솔루션으로 명령어 미세조정 데이터 자동 생성. 안전성-성능 트레이드오프 체계적 분석.

- **모델 가족의 다양성**: 용도별(기본/Python/Instruct), 크기별(7B~70B) 조합으로 폭넓은 배포 시나리오 지원.

## Limitation & Further Study

- **인필링과 성능 상충**: 인필링 목표 추가가 기본 코드 생성 벤치마크(HumanEval 등)에 미치는 영향이 완전히 분석되지 않음. Code Llama-Python은 일부 크기에서 인필링 없이 학습됨.

- **장문맥 성능 평가 제한**: LCFT 적용 후 표준 벤치마크에서 성능 저하 여부를 정량적으로 충분히 제시하지 않음. 초장문맥(100K 토큰) 환경에서의 실제 활용도 평가 부족.

- **언어별 특화 부족**: Python만 특화 모델 제공. Java, C++ 등 다른 주요 언어의 특화 모델 개발 기회.

- **평가 벤치마크의 한계**: HumanEval, MBPP는 상대적으로 단순 함수 생성 작업. 실제 소프트웨어 개발의 복잡한 요구사항 반영 필요.

- **명령어 미세조정 데이터의 품질**: 자기-지도 데이터의 품질 검증 및 편향 제거 방법에 대한 상세 설명 부족.

- **후속 연구 방향**: (1) 다양한 프로그래밍 언어 특화 모델 확대, (2) 장문맥에서의 저장소 수준 추론(repository-level code understanding) 평가, (3) 코드 버그 탐지, 코드 리팩토링 등 고차 작업 확대.

## Evaluation

- **Novelty**: 4/5
  - 기반 모델 활용, FIM 구현, 위치 보간 개선 등이 점진적 발전. 자기-지도 데이터 구성은 참신. 다만 개별 기법들은 기존 연구의 조합.

- **Technical Soundness**: 4.5/5
  - 실험 설계가 체계적이고 ablation study 충분. 장문맥 LCFT 메커니즘이 명확하나, 인필링과 성능 상충 분석이 부분적.

- **Significance**: 5/5
  - 공개 코드 생성 모델의 새로운 벤치마크 수립. 다양한 크기와 특화 모델 제공으로 실무 활용성 극대화. 상업 라이선스로 광범위한 채택 가능성.

- **Clarity**: 4/5
  - 전반적으로 명확한 구조와 표현. Figure 2의 파이프라인이 직관적. 다만 일부 기술 세부사항(예: SPM의 토크나이제이션 차이)은 충분히 설명되지 않음.

- **Overall**: 4.5/5

**총평**: Code Llama는 체계적인 다단계 특화 전략으로 공개 코드 생성 LLM의 실용성과 성능을 동시에 달성한 견고한 연구이다. 특히 인필링과 장문맥 지원, 다양한 모델 가족으로 실제 개발 환경의 요구사항에 부응하는 점이 핵심 강점이며, 상업용 라이선스 공개를 통해 산업 활용도 높다.

## Related Papers

- 🧪 응용 사례: [[papers/731_Scireplicate-bench_Benchmarking_llms_in_agent-driven_algorit/review]] — Code Llama의 코드 생성 능력이 과학 논문의 알고리즘 복제에 활용됩니다.
- 🏛 기반 연구: [[papers/546_Mlgym_A_new_framework_and_benchmark_for_advancing_ai_researc/review]] — 코드 생성 모델이 AI 연구 에이전트 개발의 기반이 됩니다.
- 🔄 다른 접근: [[papers/770_Starcoder_2_and_the_stack_v2_The_next_generation/review]] — 오픈소스 코드 생성을 위한 서로 다른 모델 아키텍처를 제시합니다.
- 🏛 기반 연구: [[papers/047_ActionIE_Action_Extraction_from_Scientific_Literature_with_P/review]] — 코드 생성을 위한 오픈 대형 언어모델은 과학 문헌의 실험 절차를 Python 코드로 변환하는 ActionIE의 기술적 기반입니다
- 🧪 응용 사례: [[papers/546_Mlgym_A_new_framework_and_benchmark_for_advancing_ai_researc/review]] — 코드 생성 모델이 AI 연구 에이전트 프레임워크에 활용됩니다.
- 🧪 응용 사례: [[papers/731_Scireplicate-bench_Benchmarking_llms_in_agent-driven_algorit/review]] — Code Llama의 코드 생성 능력이 알고리즘 복제 벤치마크에 활용됩니다.
- 🏛 기반 연구: [[papers/383_Geometry_Informed_Tokenization_of_Molecules_for_Language_Mod/review]] — 코드용 오픈 파운데이션 모델이 분자 언어모델 생성의 기반 제공
- 🔄 다른 접근: [[papers/263_Deepseek-coder_When_the_large_language_model_meets_programmi/review]] — Code Llama와 유사한 코드 특화 LLM이지만 상용 사용 가능한 오픈소스로 차별화
- 🔄 다른 접근: [[papers/741_Seed-coder_Let_the_code_model_curate_data_for_itself/review]] — Code Llama와 유사한 코드 모델이지만 데이터 전처리에서 완전 자동화 달성
