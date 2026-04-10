---
title: "922_Vibe_physics_The_AI_grad_student"
authors:
  - "Anthropic"
date: "2025"
doi: ""
arxiv: ""
score: 4.0
essence: "Harvard 물리학 교수가 Claude AI를 감독하여 2주일 내에 고에너지 이론물리학 논문을 완성했으며, 이는 AI가 도메인 전문가의 지도 아래 frontier 과학 연구를 수행할 수 있음을 입증했다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/AI_Scientific_Discovery"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Anthropic_Vibe physics The AI grad student.pdf"
---

# Vibe physics: The AI grad student

> **저자**: Anthropic | **날짜**: 2025 | **URL**: [https://www.anthropic.com/research/vibe-physics](https://www.anthropic.com/research/vibe-physics)

---

## Essence

Harvard 물리학 교수가 Claude AI를 감독하여 2주일 내에 고에너지 이론물리학 논문을 완성했으며, 이는 AI가 도메인 전문가의 지도 아래 frontier 과학 연구를 수행할 수 있음을 입증했다.

## Motivation

- **Known**: LLM(Large Language Model)은 이미 대학원 1학년 과정 수준의 업무를 수행할 수 있으며, 수학 분야에서는 FunSearch, AlphaProof 등이 end-to-end 자동 연구에서 성과를 보였다.
- **Gap**: 이론물리학은 수학과 달리 물리적 직관, 적절한 근사 선택, 미묘한 함정 네비게이션이 필요한데, AI가 잘 정의된 G2 수준 프로젝트(대학원 2학년)를 수행할 수 있는지 검증되지 않았다.
- **Why**: AI가 frontier 이론물리학 문제를 자동으로 해결할 수 있다면 연구 생산성과 속도를 혁명적으로 증가시킬 수 있으며, 이는 과학 연구의 미래 방향을 결정하는 중요한 증거가 된다.
- **Approach**: Harvard 물리학 교수가 Claude Opus에게 C-parameter의 Sudakov shoulder resummation 계산(양자색역학 이론물리 문제)을 text prompt만으로 지도하며, 102개의 세분화된 작업을 7단계로 구조화하여 수행하게 했다.

## Achievement

1. **2주 내 고품질 논문 완성**: 통상 1년 걸리는 이론물리학 논문을 2주에 완성 (110개 초안, 36M tokens, 40시간 이상의 CPU compute 소요)
2. **Frontier 물리학 연구 수행**: Sudakov shoulder resummation 문제로 양자색역학의 기초 이해를 직접 진전시키는 기술적으로 엄밀한 논문 생산
3. **체계적 작업 관리**: 102개 작업을 markdown 파일 트리로 구조화하여 관리하며 이전 결과의 검색과 재참조를 효과적으로 수행
4. **수치 계산과 검증**: EVENT2 Fortran 코드 컴파일, Monte Carlo 시뮬레이션 실행, 이론 계산과 시뮬레이션 간 우수한 일치 달성
5. **도메인 전문가의 필수성 실증**: AI의 뛰어난 능력에도 불구하고 정확성 평가에 도메인 전문가가 필수적임을 입증

## How

- Claude 및 다른 LLM들에게 초기 계획 수립 단계에서 협력하여 최적의 아이디어 통합
- Master plan을 102개 세부 작업으로 분해하고 7단계(kinematics, NLO structure, SCET factorization, anomalous dimensions, resummation, matching, documentation)로 구조화
- 각 작업의 결과를 별도 markdown 파일에 저장하여 context 관리 최적화
- Claude에게 완료된 단계의 summary를 읽고 다음 작업 진행 전 검토하도록 지시
- 작업 진행 중 오류 발견 시 명확한 지시로 방향 재설정 (예: 건너뛴 작업 복구, 과도한 병렬 작업 분해)
- LaTeX 논문 초안 작성 시 'more prose' 프롬프팅과 반복적 피드백으로 품질 향상
- 수치 계산 부분은 사전에 분리하여 개별 감독

## Originality

- **G2 수준 문제 선택의 과학성**: 첫 번째로 well-defined, guaranteed success의 학부 수준 문제를 체계적으로 AI에 할당하여 단계적 capability 검증
- **Text prompt만으로의 엄격한 제약**: 파일 직접 편집 금지, 자신의 계산 붙여넣기 금지 규칙으로 AI의 순수 능력 평가
- **구조화된 markdown 트리 시스템**: LLM의 context 제약을 극복하는 novel한 작업 관리 방식 제시
- **Frontier 과학 수행 입증**: 단순 hypothesis generation/evaluation이 아닌 실제 physics intuition과 approximation 선택이 필요한 현실적 문제 해결
- **AI 과학자의 중간 단계 필요성 주장**: End-to-end autonomous AI scientist에 대한 회의적 입장으로 'graduate school' 단계의 중요성 강조

## Limitation & Further Study

- **도메인 전문가 의존**: AI가 뛰어나더라도 정확성 평가, 오류 감지, 방향 재설정에 domain expert의 적극적 감독 필수
- **Context 및 자율성 문제**: 초기 단계에서 Claude가 작업을 건너뛰거나 과도하게 병합하려는 오류 발생, 완전 자동화 불가능
- **수치 계산의 미묘함**: 정규화(normalization), 히스토그램 binning 등 단순한 계산에서도 여러 번의 시도와 보정 필요
- **특정 문제 유형 제한**: 이론물리학의 G3+ 수준 개방형 창의 문제나 paradigm-shifting frontier 문제는 여전히 입증되지 않음
- **높은 계산 비용**: 36M tokens, 40시간 이상 CPU compute는 모든 연구자에게 접근 가능하지 않은 리소스
- **후속 연구 방향**: AI-scientist 시스템의 scalability, G3+ 수준 문제 해결 능력, 완전 자동화 가능성에 대한 추가 검증 필요

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 이 논문은 AI가 도메인 전문가의 적절한 지도 아래 실제 frontier 과학 연구를 수행할 수 있음을 최초로 엄밀하게 입증하는 landmark 연구이며, 방법론의 혁신성(구조화된 markdown 시스템, G2 문제 선택)과 실제 고에너지물리학 진전으로 향후 AI-scientist 패러다임에 깊은 영향을 미칠 것으로 예상된다.

## Related Papers

- 🔄 다른 접근: [[papers/795_The_AI_Scientist_Towards_Fully_Automated_Open-Ended_Scientif/review]] — AI를 활용한 과학 연구 자동화의 두 가지 접근법을 비교하여 인간 감독 vs 완전 자동화의 장단점을 파악할 수 있다.
- 🔗 후속 연구: [[papers/673_Researchtown_Simulator_of_human_research_community/review]] — AI 대학원생 개념을 인간 연구 커뮤니티 시뮬레이션으로 확장하여 더 현실적인 연구 환경에서의 AI 활용 가능성을 탐색한다.
- 🏛 기반 연구: [[papers/352_From_AI_for_Science_to_Agentic_Science_A_Survey_on_Autonomou/review]] — 에이전틱 사이언스의 이론적 틀이 AI 대학원생 구현의 기초 개념과 방법론을 제공한다.
- 🔄 다른 접근: [[papers/911_Resummation_of_the_C-Parameter_Sudakov_Shoulder_Using_Effect/review]] — 고에너지 물리학 연구에서 AI 활용 방식을 비교할 수 있는 대조적 사례로서 서로 다른 접근법의 장단점을 분석할 수 있다.
