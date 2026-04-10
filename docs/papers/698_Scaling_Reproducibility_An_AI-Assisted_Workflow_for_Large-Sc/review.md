---
title: "698_Scaling_Reproducibility_An_AI-Assisted_Workflow_for_Large-Sc"
authors:
  - "Yiqing Xu"
  - "Leo Yang Yang"
date: "2026.02"
doi: "arXiv:2602.16733"
arxiv: ""
score: 4.0
essence: "본 논문은 대규모 실증 연구의 재현성(reproducibility) 문제를 해결하기 위해 에이전트형 AI 워크플로우를 개발하고, 도구변수(instrumental variable, IV) 설계 92개 연구에서 87%의 종단 성공률을 달성했다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/AI-Powered_Research_Planning"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Xu and Yang_2026_Scaling Reproducibility An AI-Assisted Workflow for Large-Scale Reanalysis.pdf"
---

# Scaling Reproducibility: An AI-Assisted Workflow for Large-Scale Reanalysis

> **저자**: Yiqing Xu, Leo Yang Yang | **날짜**: 2026-02-17 | **DOI**: [arXiv:2602.16733](https://arxiv.org/abs/2602.16733)

---

## Essence

본 논문은 대규모 실증 연구의 재현성(reproducibility) 문제를 해결하기 위해 에이전트형 AI 워크플로우를 개발하고, 도구변수(instrumental variable, IV) 설계 92개 연구에서 87%의 종단 성공률을 달성했다.

## Motivation

- **Known**: 실증 사회과학에서 재현성은 연구 신뢰도의 핵심이며, 주요 저널들은 데이터와 코드 공개를 의무화함
- **Gap**: 재현 패키지의 이질적 구조, 소프트웨어 환경, 문서화 차이로 인해 대규모 재분석 시 높은 실행 비용 발생
- **Why**: 재현성 달성의 병목은 이론적 개선이 아닌 운영상 실행 - 이질적 코드베이스의 자동화 가능성이 있음
- **Approach**: 과학적 추론(과학자)과 계산 실행(AI)을 분리하여, 사전 지정된 진단 템플릿을 AI가 자동으로 실행하는 적응형 워크플로우 구축

## Achievement

![Figure 1](https://latex.codecogs.com/svg.image?%5Ctext%7BFigure%201%3A%20Agentic%20AI%20Workflow%20Overview%7D)

1. **높은 재현성 달성**: 92개 논문(67개 기존 + 25개 신규) 전체에서 87% 종단 성공률 달성; 데이터/코드 접근 가능 시 100% 정확한 2SLS 계수 재현
   
2. **확장된 평가 범위**: 단순 기준선 1개에서 논문당 최대 3개 IV 사양으로 확대(총 215개 사양), 워크플로우의 견고성 증명

3. **투명한 버전 관리**: 반복되는 장애 패턴을 구조화된 지식층에 기록하여 이질적 연구 간 적응 가능하면서도 각 파이프라인 버전의 안정성과 감시 추적(audit trail) 유지

4. **대규모 재분석 비용 절감**: 수년이 걸리던 수동 재분석을 자동화하여 확립된 실증 프로토콜 실행의 실질적 비용 감소

## How

![Figure 2](https://latex.codecogs.com/svg.image?%5Ctext%7BFigure%202%3A%20Diagnostic%20Report%20Example%7D)

- **삼층 구조**: (1) 과학자 설계 진단 템플릿 → (2) LLM 기반 작업 라우팅 및 모듈식 에이전트 조정 → (3) 구조화된 지식층의 장애 패턴 기록
  
- **모듈식 에이전트**: 재현 패키지 수집, 사양 식별, 계산 환경 재구성, 모델 실행, 표준화된 진단 보고서 생성
  
- **버전 제어된 실행**: 모든 수치 연산(데이터 준비, 추정, 진단)은 버전 제어 코드로 수행하여 고정 입력에 동일 출력 보장
  
- **적응형 휴먼-인-더-루프**: 새로운 재현 패키지에서 발생하는 장애 패턴을 일반화 규칙으로 인코딩하여 점진적 커버리지 확대
  
- **평가 방법론**: Lal et al. (2024)의 67개 수동 검증된 기준선 코퍼스 + 25개 신규 논문 확장, 단위는 개별 IV 사양(outcome-treatment-instrument-covariate 조합)

## Originality

- **AI-인간 분업 명확화**: 과학적 진단 설계는 인간(econometric 이론의 정밀도 기준 충족 필요), 실행은 AI로 명확히 역할 분담 - 현존 AI 역량의 현실적 인식
  
- **구조화된 지식층의 창의적 설계**: 단순 재시도 대신 장애 패턴을 버전 제어되는 규칙으로 체계화하여, 적응성과 투명성의 균형 달성
  
- **대규모 벤치마크 기반 평가**: 67개 수동 검증 기준선 + 25개 신규 샘플로 forward extension 검증, 재현성 연구에서 드문 체계적 평가
  
- **실제 이질성의 투명한 문서화**: appendix에서 만난 다양한 변동성 클래스와 대응 조정을 명시하여 재현 가능한 엔지니어링 프로세스 제시

## Limitation & Further Study

- **적용 범위의 제한**: 정치학·경제학의 도구변수 설계 중심; 데이터/코드 미접근 논문 제외 → 완전히 문서화되지 않은 연구나 다른 분야(의학, 자연과학 등)로의 확대 필요
  
- **재현성과 재복제성의 구분**: 보고된 결과 회복만 다룸 - 새 데이터에서의 유사 발견(replicability) 검증 불가, 이는 근본적 방법론 신뢰도 평가에 여전히 필요
  
- **기저 템플릿 의존성**: 잘 확립된 진단 템플릿과 투명성 규범이 있는 분야에서만 작동 - 신흥 방법론이나 탐험적 분석이 많은 분야에 적용 어려움
  
- **후속 연구**: (1) 다른 인과 추론 설계(DID, RDD, 매칭 등)로 확대; (2) AI의 진단 템플릿 설계 역할 증대 가능성 탐색; (3) 데이터 미접근 시나리오에서 역공학(reverse engineering) 기법 개발


## Evaluation

- Novelty: 4/5
- Technical Soundness: 4.5/5
- Significance: 4/5
- Clarity: 4.5/5
- Overall: 4/5

**총평**: 본 논문은 AI를 활용한 대규모 재현성 달성이 기술적으로 현실 가능함을 체계적으로 입증하였으며, 인간-AI 역할 분담의 명확한 설계와 버전 제어된 지식 축적으로 실무적 가치가 높으나, IV 설계 특화로 일반화 범위가 현재 제한적이고 근본적 재복제성 문제는 미해결이라는 한계가 있다.

## Related Papers

- 🏛 기반 연구: [[papers/654_Re_2_A_consistency-ensured_dataset_for_full-stage_peer_revie/review]] — 전체 단계 동료 심사를 위한 일관성 보장 데이터셋은 대규모 재현성 연구에서 AI 워크플로우 검증의 데이터 기반을 제공한다.
- 🧪 응용 사례: [[papers/885_Withdrarxiv_A_large-scale_dataset_for_retraction_study/review]] — 철회된 논문에 대한 대규모 데이터셋 연구는 AI 지원 재현성 워크플로우가 해결해야 할 연구 신뢰성 문제의 실제 사례를 보여준다.
- 🔗 후속 연구: [[papers/262_Deepreview_Improving_llm-based_paper_review_with_human-like/review]] — 인간 유사 논문 리뷰를 위한 DeepReview는 재현성 연구의 AI 워크플로우를 논문 품질 평가까지 확장한다.
