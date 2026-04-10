---
title: "702_Scholarcopilot_Training_large_language_models_for_academic_w"
authors:
  - "Yubo Wang"
  - "Xueguang Ma"
  - "Ping Nie"
  - "Huaye Zeng"
  - "Zhiheng Lyu"
date: "2025"
doi: "arXiv:2504.00824"
arxiv: ""
score: 4.0
essence: "학술 논문 작성을 위해 생성 과정과 인용 검색을 통합한 대규모 언어모델 프레임워크를 제시한다. 동적 검색 토큰 생성을 통해 필요한 시점에 정확한 학술 참고문헌을 검색하고 인용 정확도를 대폭 향상시킨다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Academic_Writing_Personalization"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Yeh et al._2025_Scholarcopilot Training large language models for academic writing with accurate citations.pdf"
---

# ScholarCopilot: Training Large Language Models for Academic Writing with Accurate Citations

> **저자**: Yubo Wang, Xueguang Ma, Ping Nie, Huaye Zeng, Zhiheng Lyu, Yuxuan Zhang, Benjamin Schneider, Yi Lu, Xiang Yue, Wenhu Chen | **날짜**: 2025 | **DOI**: [arXiv:2504.00824](https://arxiv.org/abs/2504.00824)

---

## Essence

![Figure 1](figures/fig1.webp)
*전통적인 RAG 시스템(좌)과 ScholarCopilot(우)의 비교. ScholarCopilot은 텍스트 생성 중 동적으로 검색 토큰([RET])을 생성하여 문맥-인식형 참고문헌 검색을 수행함*

학술 논문 작성을 위해 생성 과정과 인용 검색을 통합한 대규모 언어모델 프레임워크를 제시한다. 동적 검색 토큰 생성을 통해 필요한 시점에 정확한 학술 참고문헌을 검색하고 인용 정확도를 대폭 향상시킨다.

## Motivation

- **Known**: 최근 대규모 언어모델(GPT-4, Qwen2.5 등)은 유창한 학술 문체 생성이 가능하지만 인용 환각(citation hallucination)이 빈번함. 기존 RAG 시스템은 외부 지식베이스에서 참고문헌을 검색하여 팩트 일관성을 개선함.

- **Gap**: 전통적 RAG는 생성 전에 독립적으로 검색을 수행하는 정적 파이프라인 구조이므로: (1) 검색과 생성 모델의 분리된 최적화로 인한 표현 불일치, (2) 사전 결정된 검색으로 문맥-인식성 부족, (3) 사용자 제어 불가능.

- **Why**: 학술 논문 작성은 진화하는 정보 필요성(evolving information needs)을 가지므로, GPT-4 언급 시 정확히 그 시점에 관련 문헌을 검색해야 함.

- **Approach**: 통합된 생성-검색 프레임워크로 검색 토큰([RET])을 동적으로 생성하여 필요한 시점에 참고문헌을 검색하고, 단일 모델에서 두 목표를 함께 최적화함.

## Achievement

![Figure 2](figures/fig2.webp)
*전통적 RAG(정적 검색-생성 파이프라인)와 ScholarCopilot(동적 인터리빙)의 비교*

1. **검색 성능**: Top-1 검색 정확도 40.1% 달성 (E5-Mistral-7B-Instruct 15.0%, BM25 9.8% 초과)

2. **생성 품질**: 1,000개 샘플 평가에서 16.2/25점 획득 (Qwen-2.5-7B-Instruct 13.9점, Qwen-2.5-72B-Instruct 15.8점 초과). 관련성, 논리적 일관성, 학술적 엄밀성, 정보 완성도, 학술적 혁신성의 5가지 차원 평가.

3. **사용자 만족도**: 10명의 숙련된 학술 저자의 사용자 연구에서 ChatGPT 대비 인용 품질 100% 선호, 전체 유용성 70% 이상 선호.

## How

![Figure 3](figures/fig3.webp)
*ScholarCopilot 데이터셋 생성 파이프라인. arXiv에서 670K개 논문 수집 → 570K개 LaTeX 소스 파일 획득 → 501K개 구조화 문서 파싱 → 19M 인용 추출 → 16.8M 인용 매칭(arXiv 10M + Semantic Scholar 6.8M) → 500K 훈련 데이터셋*

![Figure 4](figures/fig4.webp)
*ScholarCopilot의 통합 훈련 프레임워크. 텍스트 생성의 다음 토큰 예측 손실과 인용 검색의 대조학습 손실을 함께 최적화하며, 검색 토큰([RET])이 동적으로 검색을 트리거함*

- **데이터셋 구성**: arXiv에서 2007-2024년 발행 컴퓨터과학 논문 500K개 수집, 평균 38개 인용 포함 (매칭율 87%)

- **통합 훈련 구조**: 단일 모델에서 (1) 다음 토큰 예측(next token prediction) 손실과 (2) 대조학습(contrastive learning) 손실을 함께 최적화

- **동적 검색 메커니즘**: 생성 과정 중 [RET] 토큰 생성 시 인용 데이터베이스 쿼리 실행, 검색된 논문 초록/주요 내용을 생성에 피드백

- **기저 모델**: Qwen-2.5-7B 기반, 효율성과 성능의 균형 유지

- **선택적 사용자 개입**: 반복적 프로세스 중 사용자가 인용을 수동으로 조정하거나 트리거 가능

## Originality

- **반복적 RAG의 학술 적용**: FLARE, SelfRAG 등의 기존 반복적 RAG를 학술 논문 작성이라는 특수한 도메인에 맞춤화. 명시적 쿼리 없이 문맥에서 암묵적으로 인용 의도를 추론하는 새로운 접근.

- **통합 생성-검색 모델**: 기존의 분리된 검색/생성 모델과 달리, 공유 표현을 통해 표현 불일치를 해결하고 계산 효율성 증대 (GritLM, OneGen과 유사하나 학술 인용에 특화)

- **대규모 학술 인용 데이터셋**: 500K 논문, 33개 매칭 인용/논문의 포괄적 인용 네트워크(citation networks) 포함. arXiv LaTeX 소스를 구조화하여 처리하는 파이프라인 개발.

- **학술 텍스트 품질의 다차원 평가**: 기존 QA 벤치마크와 달리, 학술 논문에 특화된 5가지 평가 차원(관련성, 일관성, 학술적 엄밀성, 완성도, 혁신성) 수립.

## Limitation & Further Study

- **도메인 제한**: 컴퓨터과학 분야에만 학습(arXiv). 다른 학제 간(interdisciplinary) 응용 가능성 미검증. 생의학, 사회과학 등 타 분야로의 확장 필요.

- **추론 시 인용 데이터베이스**: 훈련에는 16.8M 인용을 사용하나 추론 시에는 데이터 품질 보장을 위해 670K arXiv 논문으로만 제한. 더 큰 규모의 검색 코퍼스 활용 시 성능 향상 가능성.

- **평가 규모**: 인간 평가가 10명의 작성자 + 1,000개 샘플로 제한적. 더 광범위한 규모의 사용자 연구 및 실제 학술 저자 피드백 필요.

- **명시적 검색 정책 분석**: [RET] 토큰 생성 시점과 빈도에 대한 깊이 있는 분석 부재. 어떤 상황에서 과도하게 또는 부족하게 검색하는지 자세한 오류 분석 필요.

- **다언어 지원**: 현재 영어 논문만 처리. 비영어 학술 커뮤니티로의 확장 미진.

## Evaluation

- **Novelty**: 4/5 - 반복적 RAG의 학술 논문 작성 특화 적용과 통합 생성-검색 모델이 새로움. 다만, 기존 기법(FLARE, SelfRAG, GritLM)의 조합 및 개선 성격도 있음.

- **Technical Soundness**: 4/5 - 명확한 아키텍처와 대규모 데이터셋 기반. 그러나 대조학습 손실 함수 설계, 하드 네거티브 샘플링 전략 등의 기술적 세부사항이 요약된 본문에서 부분적으로만 설명됨.

- **Significance**: 4/5 - 학술 논문 작성 보조 도구로 실질적 가치 높음. ChatGPT 대비 우수한 성능. 다만 컴퓨터과학 한정, 현실 배포의 미지수(500K 학습 데이터, 추론 시 인용 제한).

- **Clarity**: 4/5 - 논문 구조가 명확하고 Figure들이 개념 설명에 효과적. 다만 훈련 절차의 상세 하이퍼파라미터와 손실 함수 정의가 요약문에 미흡.

- **Overall**: 4/5

**총평**: ScholarCopilot은 반복적 검색-생성 통합을 통해 학술 논문 작성에 특화된 실용적이고 혁신적인 솔루션을 제시한다. 대규모 학술 데이터셋 구축과 사용자 평가를 통해 실질적 가치를 입증했으나, 도메인 한정성과 상세한 기술 설명 부분에서 개선의 여지가 있다.

## Related Papers

- 🔄 다른 접근: [[papers/889_Xtragpt_Llms_for_human-ai_collaboration_on_controllable_acad/review]] — 학술 글쓰기에서 인용 검색 통합과 제어 가능한 수정 기능은 모두 글쓰기 지원을 목표로 하지만 서로 다른 작업 단계에 초점을 맞춘다.
- 🏛 기반 연구: [[papers/886_Wordcraft_A_human-ai_collaborative_editor_for_story_writing/review]] — 인간-AI 협업 글쓰기의 기본 개념이 학술 논문 작성이라는 전문적 영역에서 인용 검색과 생성을 통합한 특화된 시스템으로 발전한다.
- 🔗 후속 연구: [[papers/228_CoAuthor_Designing_a_Human-AI_Collaborative_Writing_Dataset/review]] — 인간-AI 협업 글쓰기 데이터셋을 학술 논문 작성이라는 전문 영역으로 확장하여 더 정교한 협업 모델을 구축한다.
- 🔗 후속 연구: [[papers/886_Wordcraft_A_human-ai_collaborative_editor_for_story_writing/review]] — 인간-AI 협업 글쓰기의 기본 개념이 학술 논문 작성이라는 전문적 영역에서 인용 검색과 동적 생성을 통합한 특화된 시스템으로 발전한다.
- 🔄 다른 접근: [[papers/889_Xtragpt_Llms_for_human-ai_collaboration_on_controllable_acad/review]] — 제어 가능한 학술 논문 수정과 인용 검색 통합 글쓰기는 모두 학술 글쓰기 지원을 목표로 하지만 수정과 생성이라는 다른 작업에 특화된다.
