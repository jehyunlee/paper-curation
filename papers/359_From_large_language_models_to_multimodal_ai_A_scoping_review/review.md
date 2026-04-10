---
title: "359_From_large_language_models_to_multimodal_ai_A_scoping_review"
authors:
  - "Lukas Buess"
  - "Matthias Keicher"
  - "Nassir Navab"
  - "Andreas Maier"
  - "Soroosh Tayebi Arasteh"
date: "2025"
doi: "arXiv:2502.09242"
arxiv: ""
score: 4.3
essence: "본 논문은 의료 분야에서 생성형 AI의 진화를 체계적으로 검토한 스코핑 리뷰로, 텍스트 기반 대규모 언어모델(LLM)에서 의료 영상, 임상 데이터를 통합하는 멀티모달 AI 시스템으로의 전환을 추적하며, PRISMA-ScR 가이드라인을 따라 2020-2024년 발표된 144개 논문을 분석했다."
tags:
  - "cat/AI-Powered_Scientific_Research_Frameworks"
  - "sub/Biological_Foundation_Models"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Zawacki‐Richter et al._2025_From large language models to multimodal ai A scoping review on the potential of generative ai in m.pdf"
---

# From large language models to multimodal AI: A scoping review on the potential of generative AI in medicine

> **저자**: Lukas Buess, Matthias Keicher, Nassir Navab, Andreas Maier, Soroosh Tayebi Arasteh | **날짜**: 2025 | **DOI**: [arXiv:2502.09242](https://arxiv.org/abs/2502.09242)

---

## Essence

![Figure 1](figures/fig1.webp) 
*의료 분야의 멀티모달 AI 파이프라인: (A) 다양한 의료 데이터 양식 수집 및 처리, (B) AI 모델에 의한 통합 표현 변환, (C) 리포트 생성, 대화 지원, 치료 계획 등의 인사이트 생성, (D) 피드백을 통한 반복적 최적화*

본 논문은 의료 분야에서 생성형 AI의 진화를 체계적으로 검토한 스코핑 리뷰로, 텍스트 기반 대규모 언어모델(LLM)에서 의료 영상, 임상 데이터를 통합하는 멀티모달 AI 시스템으로의 전환을 추적하며, PRISMA-ScR 가이드라인을 따라 2020-2024년 발표된 144개 논문을 분석했다.

## Motivation

- **Known**: ChatGPT 등 생성형 AI 모델이 의료 분야에서 임상 문서 작성, 진단 지원 등에 활용되고 있으며, AI 생성 방사선 리포트가 작성 시간을 약 25% 단축할 수 있음이 입증됨

- **Gap**: 의료 데이터는 텍스트, 의료 영상, 실험실 결과, 유전체 데이터 등 다양한 양식을 포함하고 있으나, 기존 리뷰는 멀티모달 AI의 통합, 평가 방법론, 임상 실제 적용에 대한 포괄적 분석이 부족함

- **Why**: 생성형 AI 분야가 빠르게 진화하고 있으며, 의료 데이터의 이질성 통합, 모델 해석가능성, 윤리 문제, 임상 검증 등 critical challenges가 존재함

- **Approach**: PubMed, IEEE Xplore, Web of Science에서 체계적 검색 후 수동 검색으로 보완하여 텍스트 기반 LLM, 멀티모달 모델, 데이터셋, 평가 지표를 분류 분석

## Achievement

![Figure 2](figures/fig2.webp) 
*PRISMA 플로우 다이어그램: 데이터베이스 4,384개 레코드에서 60개, 수동 검색 83개를 포함하여 총 144개 논문 선정*

1. **텍스트 기반 LLM의 의료 응용 체계화**: BioBERT, BioMistral 등 의료 특화 모델들이 supervised finetuning(SFT), prompt engineering, RLHF(강화학습) 등 다양한 기법으로 임상 문서화, 의료 문헌 요약, 진단 지원에 활용되고 있음을 분류

2. **멀티모달 AI로의 패러다임 전환 확인**: 단순 텍스트 처리에서 의료 영상, 임상 노트, 구조화된 데이터를 단일 모델 내 통합하는 멀티모달 대규모 언어모델(MLLM)로의 전환이 진단 지원, 의료 리포트 생성, 약물 발견, 대화형 AI 혁신을 주도

3. **평가 방법론의 gap 규명**: 어휘 기반 지표(BLEU, ROUGE), 임상 특화 지표, 모델 신뢰성·임상 관련성·일반화 가능성 평가의 불일치 확인

## How

![Figure 3](figures/fig3.webp)
*멀티모달 아키텍처: (A) CLIP 기반 모델 - 임베딩 정렬 (B) 크로스 어텐션 (C) 융합 기법*

- **데이터 수집 및 처리**: 의료 영상(X-ray, CT, MRI), 임상 노트, 실험실 결과, 유전체 데이터 등 다양한 양식을 구조화된 형태로 수집

- **모델 아키텍처**: Transformer 기반 self-attention 메커니즘으로 문맥 관계 및 장거리 의존성 포착; CLIP 기반 모델, 크로스 어텐션, 멀티 모달 융합 기법 활용

- **텍스트 LLM 적응 기법**:
  - Supervised Finetuning (SFT): 의료 특화 데이터로 사전학습 모델 미세조정
  - Prompt Engineering: 설계된 입력 프롬프트로 추가 학습 없이 성능 달성
  - RLHF/RLAIF: 전문가 피드백 또는 AI 피드백으로 임상 기대값 정렬

- **멀티모달 통합**: 다양한 데이터 타입을 통합 표현으로 변환하여 포괄적 의사결정 지원 시스템 구현

![Figure 4](figures/fig4.webp)
*의료 분야의 생성형 AI 평가: 어휘 기반 지표(BLEU, ROUGE), 임상 특화 지표, 자동 평가 vs. 인간 평가*

## Originality

- 2020-2024년 최신 논문 144개를 체계적으로 분석하여 텍스트 중심 LLM에서 멀티모달 AI로의 진화 추적

- 의료 생성형 AI 특화 평가 방법론에 초점을 맞춰, 일반 NLG 지표(BLEU, ROUGE)와 임상 맥락 지표 간의 gap을 명시적으로 규명

- PRISMA-ScR 가이드라인을 엄격히 준수하며 3개 데이터베이스 검색 + 수동 검색으로 보완하여 최신 프리프린트와 데이터셋까지 포함

- 데이터셋(텍스트 기반, 멀티모달), 모델 아키텍처, 애플리케이션 영역을 이중 계층 분류로 구조화하여 현황을 종합적으로 제시

## Limitation & Further Study

- **한계**:
  - 분석 기간이 2020년 이후로 제한되어 초기 기초 연구 축적에 대한 맥락 부족 가능성
  - 비영어 원문 제외로 다국어 의료 AI 개발 현황 미반영
  - 스코핑 리뷰 특성상 메타분석 미수행으로 정량적 효과 크기 비교 불가
  - 개인정보보호(GDPR, HIPAA)와 같은 규제 환경이 개발에 미치는 영향 상세 분석 부족

- **후속 연구**:
  - 멀티모달 AI의 임상 검증 및 실제 의료 현장 도입 연구 필요
  - 모델 해석가능성(explainability) 향상 기법 개발
  - 이질적 의료 데이터 타입 통합 방법론 고도화
  - 윤리, 공정성, 투명성 평가 기준 표준화
  - 구조화되지 않은 의료 데이터(비정형 이미지, 자유 텍스트) 활용 개선

## Evaluation

- **Novelty**: 4/5
  - 최신 멀티모달 AI를 의료에 특화하여 체계화한 점은 높이 평가되나, 기본 개념은 기존 리뷰를 확장한 수준

- **Technical Soundness**: 4/5
  - PRISMA-ScR 가이드라인 엄격 준수, 이중 계층 분류로 논리적 구조 견고함. 다만 정성적 분석이 주가 되어 정량적 메타분석 부재

- **Significance**: 5/5
  - 의료 AI의 현재 상태와 key challenges(해석가능성, 임상 검증, 윤리)를 명확히 규명하여 향후 개발 방향 제시에 높은 실용적 가치

- **Clarity**: 4/5
  - 전체 구조가 명확하고 텍스트 LLM → 멀티모달 AI 진화 과정이 잘 드러남. 일부 기술 용어에 대한 초보자 설명 보강 가능

- **Overall**: 4.3/5

**총평**: 본 논문은 의료 분야의 생성형 AI 진화를 최신 발표까지 포함하여 체계적으로 정리한 필수 참고 리뷰이며, 특히 멀티모달 통합과 평가 방법론의 gap을 명확히 규명함으로써 향후 연구자와 개발자에게 실질적 방향을 제시한다.

## Related Papers

- 🔄 다른 접근: [[papers/720_Scientific_Large_Language_Models_A_Survey_on_Biological__Che/review]] — 생의학 분야 멀티모달 AI와 생물학/화학 특화 언어모델이라는 다른 접근으로 의료 AI를 발전시킨다
- 🧪 응용 사례: [[papers/225_Clinicalgpt-r1_Pushing_reasoning_capability_of_generalist_di/review]] — 생성형 AI의 임상 추론 능력을 의료 분야 멀티모달 시스템 발전의 실제 사례로 보여준다
- 🏛 기반 연구: [[papers/168_Biomni_A_General-Purpose_Biomedical_AI_Agent/review]] — 범용 생의학 AI 에이전트가 의료 멀티모달 AI 발전의 기술적 기반을 제공한다
