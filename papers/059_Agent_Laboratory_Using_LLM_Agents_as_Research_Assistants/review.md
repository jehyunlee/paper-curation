---
title: "059_Agent_Laboratory_Using_LLM_Agents_as_Research_Assistants"
authors:
  - "Samuel Schmidgall"
  - "Yusheng Su"
  - "Ze Wang"
  - "Ximeng Sun"
  - "Jialian Wu"
date: "2025.06"
doi: "10.48550/arXiv.2501.04227"
arxiv: ""
score: 4.0
essence: "Agent Laboratory는 인간의 연구 아이디어 실행을 지원하는 자율적 LLM 기반 프레임워크로, 문헌 검토, 실험 수행, 보고서 작성의 세 단계를 거쳐 완전한 연구 성과물을 생성한다. 기존 자동화 연구 방법 대비 84% 비용 감축을 달성하면서도 높은 품질의 기계학습 연구를 수행할 수 있음을 보여준다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/AI-Powered_Research_Planning"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Schmidgall et al._2025_Agent Laboratory Using LLM Agents as Research Assistants.pdf"
---

# Agent Laboratory: Using LLM Agents as Research Assistants

> **저자**: Samuel Schmidgall, Yusheng Su, Ze Wang, Ximeng Sun, Jialian Wu, Xiaodong Yu, Jiang Liu, Michael Moor, Zicheng Liu, Emad Barsoum | **날짜**: 2025-06-17 | **DOI**: [10.48550/arXiv.2501.04227](https://doi.org/10.48550/arXiv.2501.04227)

---

## Essence

![Figure 1](figures/fig1.webp)
*Agent Laboratory는 인간의 연구 아이디어를 입력받아 특화된 LLM 에이전트 파이프라인을 통해 연구 보고서와 코드 저장소를 생성한다.*

Agent Laboratory는 인간의 연구 아이디어 실행을 지원하는 자율적 LLM 기반 프레임워크로, 문헌 검토, 실험 수행, 보고서 작성의 세 단계를 거쳐 완전한 연구 성과물을 생성한다. 기존 자동화 연구 방법 대비 84% 비용 감축을 달성하면서도 높은 품질의 기계학습 연구를 수행할 수 있음을 보여준다.

## Motivation

- **Known**: LLM 기반 연구 자동화(ResearchAgent, AI Scientist 등)가 진행 중이며, LLM이 인간보다 더 참신한 아이디어 생성 능력을 보임. 다만 실행 가능성(feasibility)과 구현 세부사항에서는 약점 존재.

- **Gap**: 기존 자동 연구 방식은 인간의 입력 없이 독립적으로 아이디어 생성→실행을 수행. 반면 많은 고품질 아이디어가 탐색되지 못하고 있으며, LLM은 저수준 구현에서 여전히 제약을 가짐.

- **Why**: 연구자가 창의적 구상(ideation)에 더 집중하고 코딩/문서작성의 부담을 덜 수 있다면 과학 발견 가속화 가능. 동시에 인간 피드백과 자동화의 결합이 더 효과적인 연구 수행을 가능하게 함.

- **Approach**: 인간이 제시한 연구 아이디어를 입력받아, 특화된 LLM 에이전트(PhD 에이전트, Postdoc 에이전트 등)가 문헌 검토→실험 설계 및 수행→논문 작성을 자동으로 진행. 각 단계에서 사용자 피드백 가능한 co-pilot 모드 제공.

## Achievement

![Figure 2](figures/fig2.webp)
*Agent Laboratory의 세 가지 핵심 단계: 문헌 검토(Literature Review), 실험 수행(Experimentation), 보고서 작성(Report Writing) 및 각 단계의 역할과 도구.*

1. **모델 성능 비교**: o1-preview 기반 Agent Laboratory가 가장 우수한 연구 성과물 생성. o1-mini는 실험 품질 점수에서 최고 달성. gpt-4o는 모든 지표에서 뒤처짐.

2. **자동화된 실험 수행**: mle-solver를 통해 MLE-Bench 과제의 부분집합에서 최첨단(SOTA) 성능 달성. MLAB, OpenHands, AIDE 대비 더 많은 금메달·은메달 획득. 생성된 머신러닝 코드가 기존 방법 대비 경쟁력 있는 성능 발휘.

3. **인간-AI 협력 효과**: Co-pilot 모드(사용자 피드백 포함)에서 자율 모드보다 높은 점수 달성. 사용자 만족도 높음(계속 사용 의향 표시).

4. **경제성**: 단 $2.33 USD (gpt-4o 백엔드)로 1편의 논문 생성. 기존 자동 연구 방법 대비 84% 비용 절감.

5. **평가 불일치 발견**: 자동화된 평가 vs. 인간 평가의 격차 발생(6.1/10 vs. 3.8/10). 자동화 평가가 품질을 과대평가하는 경향.

## How

![Figure 3](figures/fig3.webp)
*mle-solver의 반복적 워크플로우: 실험 코드 생성, 실행, 오류 처리, 결과 해석의 순환 과정.*

- **문헌 검토 단계**: PhD 에이전트가 arXiv, Google Scholar 등에서 관련 문헌 검색. 논문 요약 및 핵심 개념 추출. 연구 맥락 정립.

- **실험 설계 및 수행**: Postdoc 에이전트가 실험 계획 수립. **mle-solver** 도구가 코드 생성→실행→디버깅→결과 수집의 반복 프로세스 담당. 머신러닝 파이프라인(데이터 처리, 모델 학습, 평가) 자동화.

- **보고서 작성**: **paper-solver**가 논문 골격 생성→각 섹션 작성→그림/표 삽입→형식 검수. 과학적 글쓰기 규범 준수.

- **Co-pilot 인터페이스**: 각 단계(문헌 검토 후, 실험 계획 후, 초안 완성 후 등)에서 사용자가 피드백·수정 지시 제공 가능. 에이전트가 반영하여 재실행.

- **백엔드 유연성**: 계산 자원 제약 고려하여 다양한 모델(o1-preview, o1-mini, gpt-4o, Claude 등) 선택 가능. CPU/GPU 메모리 수준에 맞춰 조정 가능.

## Originality

- **인간 중심 자동화**: 기존 자동화 연구(AI Scientist, ResearchAgent)와 달리 인간의 초기 아이디어를 출발점으로 하는 co-pilot 방식 도입. 창의성과 실행 가능성의 보완적 결합.

- **체계적 평가 프레임워크**: NeurIPS 스타일 동료 검토(peer review) 방식 평가, 인간 평가자 참여, 실험 품질/보고서 품질/유용성의 다차원 평가 지표 설계.

- **mle-solver 및 paper-solver 개발**: 특화된 에이전트 도구로 머신러닝 실험과 학술 작성의 반복적 오류 수정 및 최적화 자동화.

- **비용 효율성 수량화**: 기존 방법 대비 84% 비용 절감이라는 구체적 수치 제시. 접근성 향상의 증거.

- **인간-자동화 간 갭 분석**: 자동 평가 vs. 인간 평가의 불일치 발견·분석으로 향후 평가 방법론 개선의 필요성 강조.

## Limitation & Further Study

- **평가의 제한성**: 조사 참여 연구자 수, 논문 수, 도메인 범위가 제한적일 가능성. 특정 분야(예: NLP, Computer Vision)에 치중되었을 수 있음. 다양한 과학 분야(화학, 생물학 등)로의 확대 필요.

- **자동 평가의 신뢰성**: 자동 평가(예: LLM 기반 스코어)가 인간 평가를 훨씬 과대평가. 더 정밀한 자동 평가 방식 개발 필요.

- **인간 피드백의 정성화**: Co-pilot 모드에서 피드백의 형태(자유 텍스트, 선택지, 강도 등)와 최적 반복 횟수에 대한 체계적 분석 부족. 메타 학습(meta-learning) 통합 고려.

- **실험-이론의 균형**: 생성된 논문이 주로 실험 중심(empirical). 이론적 통찰이나 증명 필요한 분야에서의 성능 미평가.

- **장기 영향 추적**: 생성된 논문이 실제 인용되거나 추후 연구에 영향을 미치는지 추적 부재. 과학 생태계 내 실제 기여도 평가 필요.

- **다중 에이전트 조율 메커니즘**: 여러 에이전트 간 충돌, 역할 중복, 협력 효율성 최적화 방안에 대한 깊이 있는 분석 부재.

## Evaluation

- **Novelty (새로움)**: 4/5  
  인간 주도 아이디어 + 자동화 실행의 co-pilot 방식은 신선함. 다만 개별 기술(LLM 에이전트, 도구 사용, 반복 개선)은 기존 작업의 조합.

- **Technical Soundness (기술적 견고성)**: 4/5  
  실험 설계, 구현, 평가 방법론이 체계적. 그러나 자동 평가의 신뢰성 문제, 평가 도메인 제한성, 일부 성능 수치의 통계적 유의성 검증 부족.

- **Significance (의의)**: 4/5  
  연구 가속화와 비용 절감 목표의 실질적 성취. 다만 생성 논문의 학계 수용도, 사회적 영향은 아직 미진. 인간 중심 설계는 실용적 가치 높음.

- **Clarity (명확성)**: 4/5  
  논문 구조, Figure, 방법론 설명이 명확. 일부 기술 세부사항(프롬프트 설계, 오류 처리 로직)의 공개 부족으로 재현성 제약.

- **Overall (종합)**: 4/5

**총평**: Agent Laboratory는 인간의 창의성을 존중하면서 LLM 에이전트의 자동화 능력을 활용하는 실용적이고 경제적인 연구 지원 시스템을 제시한다. 특히 co-pilot 모드와 비용 효율성은 실질적 기여도가 높으나, 생성된 연구의 과학적 영향력, 평가 방법론의 신뢰성, 다양한 과학 분야로의 일반화 가능성 측면에서 추가 검증과 개선이 요구된다.

## Related Papers

- 🔄 다른 접근: [[papers/825_Towards_an_AI_co-scientist/review]] — Agent Laboratory와 Towards an AI co-scientist는 모두 AI 연구 지원을 다루지만, 인간 아이디어 실행 지원과 완전 자율적 공동 연구라는 서로 다른 협업 모델을 제시합니다.
- 🔗 후속 연구: [[papers/668_ResearchAgent_Iterative_Research_Idea_Generation_over_Scient/review]] — Agent Laboratory의 연구 자동화 프레임워크는 ResearchAgent의 반복적 연구 아이디어 생성을 확장하여 실험 수행과 보고서 작성까지 포괄하는 완전한 연구 파이프라인을 구축합니다.
