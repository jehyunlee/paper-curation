---
title: "597_P2p_Automated_paper-to-poster_generation_and_fine-grained_be"
authors:
  - "Tao Sun"
  - "Enhao Pan"
  - "Zhengkai Yang"
  - "Kaixin Sui"
  - "Jiajun Shi"
date: "2025"
doi: "arXiv:2505.17104v1"
arxiv: ""
score: 4.25
essence: "학술 논문을 자동으로 고품질 학술 포스터(HTML 형식)로 변환하는 LLM 기반 다중 에이전트 프레임워크를 제안하며, 30,000개 이상의 대규모 지시 데이터셋과 세부 평가 벤치마크를 함께 제공한다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/Multi-Agent_Language_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Suárez‐Tangil et al._2025_P2p Automated paper-to-poster generation and fine-grained benchmark.pdf"
---

# P2P: Automated Paper-to-Poster Generation and Fine-Grained Benchmark

> **저자**: Tao Sun, Enhao Pan, Zhengkai Yang, Kaixin Sui, Jiajun Shi, Xianfu Cheng, Tongliang Li, Wenhao Huang, Ge Zhang, Jian Yang, Zhoujun Li | **날짜**: 2025 | **DOI**: [arXiv:2505.17104v1](https://arxiv.org/abs/2505.17104v1)

---

## Essence

![Figure 1](figures/fig1.webp)
*Figure 1: P2P의 다중 에이전트 아키텍처: Figure Agent는 시각 요소 처리, Section Agent는 콘텐츠 생성, Orchestrate Agent는 포스터 조립 및 HTML 렌더링을 담당*

학술 논문을 자동으로 고품질 학술 포스터(HTML 형식)로 변환하는 LLM 기반 다중 에이전트 프레임워크를 제안하며, 30,000개 이상의 대규모 지시 데이터셋과 세부 평가 벤치마크를 함께 제공한다.

## Motivation

- **Known**: 학술 포스터는 학회 발표의 핵심 도구이지만, 수동 제작은 시간이 많이 소모되고 기술을 요구함. 기존 템플릿 기반 또는 규칙 기반 접근법(template-based, rule-driven methods)은 학술 문서의 의미적 풍부성(semantic richness)과 구조적 뉘앙스를 포착하지 못함.

- **Gap**: 최근 다중모달 대형언어모델(MLLMs)의 발전에도 불구하고, 학술 포스터 생성 작업에 적용할 때 (1) 품질 제어 메커니즘 부족, (2) 표준화된 평가 벤치마크 부재, (3) 적절한 훈련 데이터셋 부족 등의 문제 존재.

- **Why**: 자동화된 포스터 생성으로 조기 연구자(early-career researcher)들의 부담을 줄이고 학술 성과 확산을 촉진할 필요성 있음.

- **Approach**: 특화된 에이전트(Figure Agent, Section Agent, Orchestrate Agent)와 검증 모듈을 통한 다단계 처리, 대규모 지시 데이터셋 구성, 세부 평가 프레임워크(fine-grained evaluation framework) 개발.

## Achievement

![Figure 2](figures/fig2.webp)
*Figure 2: 논문-포스터 변환 예시: 좌측 논문의 주요 요소(제목, 그림, 섹션)가 우측 생성된 포스터에 매핑됨*

1. **P2P 다중 에이전트 프레임워크**: 세 개의 특화된 에이전트와 각각의 검증 모듈(checker module)을 통해 반복적 개선(iterative refinement)을 수행하며, HTML/CSS 기반 렌더링으로 전문적인 포스터 생성 달성.

2. **P2P INSTRUCT 데이터셋**: 30,460개의 고품질 지시-응답 쌍(instruction-response pairs)으로 구성된 첫 대규모 학술 포스터 생성 특화 데이터셋 구축. Figure Describer를 통해 16,848개 그림 설명(평균 192 토큰), Section/Content/HTML Generator를 통해 13,612개 텍스트 콘텐츠 예제(평균 3,300 토큰 이상) 수집.

3. **P2P EVAL 벤치마크**: 121개 논문-포스터 쌍과 이중 평가 방법론(Universal Evaluation + Fine-Grained Evaluation)을 포함한 포괄적 평가 체계 제시. 33개 모델 평가를 통한 성능 검증.

## How

![Figure 1](figures/fig1.webp)

### Figure Agent (시각 요소 처리)
- DocLayout-YOLO를 이용한 그림/표 추출
- Figure Describer가 공간적 관계 분석으로 캡션 대응
- Figure Checker: (1) 중복 추출 방지, (2) 주요 시각 요소 포함 확인, (3) 정확한 시각-캡션 쌍 검증
- 신뢰도 임계값(confidence threshold)의 점진적 조정으로 정렬 달성

### Section Agent (텍스트 콘텐츠 생성)
- Section Generator: 입력 논문으로부터 포스터의 상세 구조 스키마(structural schema) 동적 추론
- Content Generator: 스키마 S, 원본 논문 D, 시각 요소 설명 F_d를 활용하여 포스터 텍스트 P_poster_text 생성
  - 수식: P_poster_text = M_text(D, S, F_d)
  - Markdown 스타일 그림 인덱스 참조를 최적 위치에 삽입하여 시각-텍스트 정렬 보장
- Section Checker: (1) 일관성 및 논리적 흐름, (2) 핵심 기여도 완전성, (3) 원본 논문 충실도, (4) 시각 요소 참조 정확성 검증

### Orchestrate Agent (포스터 조립 및 렌더링)
- HTML Generator: Markdown 형식 텍스트 P_poster_text와 시각 요소를 조합하여 HTML/CSS 포스터 생성
- 렌더링 원칙: (1) Content-Structure Decoupling, (2) Institutional Identity Alignment, (3) Responsive and Balanced Layout
- Poster Checker: 레이아웃 미학성(aesthetics)과 구조 무결성 평가, 반복적 조정

### P2P EVAL 평가 프레임워크
- **Universal Poster Evaluation**: 전반적 품질 차원 평가 (content fidelity, visual consistency, layout effectiveness)
- **Fine-Grained Poster Evaluation**: 공식 포스터 예시로부터 인간이 주석을 단 체크리스트(human-annotated checklist)에 대한 준수도 측정
- LLM-as-a-Judge 기반 자동 평가

## Originality

- **첫 번째 실무 적용 중심 다중 에이전트 프레임워크**: 논문-포스터 변환을 위해 특화된 세 개의 협력 에이전트와 검증 루프를 결합한 구조는 기존 템플릿 기반 접근과 차별화.

- **대규모 학술 포스터 특화 데이터셋**: 30K+ 규모의 P2P INSTRUCT는 처음으로 학술 포스터 생성 작업을 위해 설계된 지시 데이터셋으로, 그림 설명 및 다단계 콘텐츠 생성을 포함.

- **이중 평가 프레임워크 제안**: Universal과 Fine-Grained 평가를 결합한 P2P EVAL은 포스터 품질 평가를 위한 첫 표준화된 벤치마크로, 인간 주석 체크리스트와 자동 평가를 통합.

- **HTML/CSS 기반 렌더링**: 실제 학술 포스터로 활용 가능한 HTML 형식의 출력으로 실용성 극대화.

## Limitation & Further Study

- **평가 벤치마크 규모**: P2P EVAL의 121개 논문-포스터 쌍은 대규모 데이터셋이지만, 더 다양한 과학 분야 및 포스터 스타일 커버가 필요할 수 있음.

- **모델 의존성**: 프레임워크 성능이 LLM(특히 M_figure, M_text)의 능력에 크게 의존하며, 더 작은 모델에서의 성능 최적화 필요.

- **언어 제한**: 현재 영문 논문 중심으로, 다국어 포스터 생성 확장 필요.

- **시각 요소 복잡성**: 복잡한 다중 서브플롯이나 고도로 통합된 다이어그램의 설명 정확도 개선 여지 있음.

- **후속 연구 방향**: (1) 더 강력한 시각-언어 모델을 통한 정확도 향상, (2) 도메인별 맞춤 포스터 템플릿 개발, (3) 실시간 사용자 피드백 기반 반복 개선 메커니즘 추가.

## Evaluation

- **Novelty**: 4.5/5 
  - 학술 포스터 생성이라는 새로운 작업에 대한 다중 에이전트 접근, 대규모 데이터셋, 세부 평가 프레임워크의 통합은 혁신적. 다만 개별 기술(MLLM, LLM-as-a-Judge)은 기존 기법의 조합.

- **Technical Soundness**: 4/5
  - 구조화된 다중 에이전트 설계, 각 모듈의 명확한 역할 정의, 반복적 검증 루프는 견고함. 다만 Figure Checker의 신뢰도 임계값 조정 알고리즘의 세부 수학적 설명과 수렴 보장(convergence guarantee) 부재.

- **Significance**: 4.5/5
  - 학술 커뮤니케이션의 실질적 문제 해결, 대규모 데이터셋과 평가 벤치마크 제공으로 커뮤니티에 기여도 높음. 33개 모델 평가로 실증적 기초 제공하나, 사용자 만족도 평가(user satisfaction) 부재.

- **Clarity**: 4/5
  - 전반적으로 명확한 구조와 설명. Figure 1의 아키텍처 다이어그램이 효과적. 다만 일부 용어(예: "reflection loop", "institutional identity alignment")의 구체적 구현 방식에 대한 추가 설명 필요.

- **Overall**: 4.25/5

**총평**: P2P는 학술 포스터 자동 생성이라는 미개척 분야에 다중 에이전트, 대규모 데이터셋, 표준화된 평가 벤치마크를 종합적으로 제시함으로써 높은 실무적 가치와 학술적 의의를 갖추었으나, 기술적 심화와 사용자 검증이 추가되면 더욱 완성도 있는 연구가 될 것으로 기대된다.

## Related Papers

- 🔄 다른 접근: [[papers/600_Paper2Web_Lets_Make_Your_Paper_Alive/review]] — PDF를 웹사이트로 vs 논문을 포스터로 변환하는 유사하지만 다른 접근법
- 🔗 후속 연구: [[papers/601_PaperBanana_Automating_Academic_Illustration_for_AI_Scientis/review]] — P2P의 포스터 생성 기술을 학술 논문의 전체 일러스트레이션으로 확장
- 🔄 다른 접근: [[papers/773_Stealing_creators_workflow_A_creator-inspired_agentic_framew/review]] — 둘 다 학술 논문의 시각적 변환을 다루지만 하나는 동영상 생성에, 다른 하나는 포스터 생성에 초점을 맞춘다.
- 🔗 후속 연구: [[papers/599_Paper2poster_Towards_multimodal_poster_automation_from_scien/review]] — 논문을 포스터로 변환하는 작업을 자동화된 Paper-to-Poster 생성과 세밀한 벤치마킹으로 확장함
