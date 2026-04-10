---
title: "513_M2F_Automated_Formalization_of_Mathematical_Literature_at_Sc"
authors:
  - "Zichen Wang"
  - "Wanli Ma"
  - "Zhenyu Ming"
  - "Gong Zhang"
  - "Kun Yuan"
date: "2026.02"
doi: "N/A"
arxiv: ""
score: 4.5
essence: "본 논문은 수학 교과서와 논문을 **프로젝트 규모의 Lean 형식화**로 자동 변환하는 최초의 에이전트 프레임워크 M2F를 제시한다. 검증자 피드백을 루프에 유지하며 세 주 안에 153,853줄의 형식화된 Lean 라이브러리를 생성하여 텍스트북 규모 형식화의 실용성을 입증했다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/Specialized_Domain_Agents"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Wang et al._2026_M2F Automated Formalization of Mathematical Literature at Scale.pdf"
---

# M2F: Automated Formalization of Mathematical Literature at Scale

> **저자**: Zichen Wang, Wanli Ma, Zhenyu Ming, Gong Zhang, Kun Yuan, Zaiwen Wen | **날짜**: 2026-02-19 | **DOI**: N/A

---

## Essence

![Figure 1: M2F 프로젝트 규모 자동 형식화 파이프라인](figures/fig1.webp)

본 논문은 수학 교과서와 논문을 **프로젝트 규모의 Lean 형식화**로 자동 변환하는 최초의 에이전트 프레임워크 M2F를 제시한다. 검증자 피드백을 루프에 유지하며 세 주 안에 153,853줄의 형식화된 Lean 라이브러리를 생성하여 텍스트북 규모 형식화의 실용성을 입증했다.

## Motivation

- **Known**: 신경 정리 증명기(Neural Theorem Prover)와 자동 형식화(Autoformalization) 연구는 개별 정리나 짧은 코드 스니펫 수준에 국한되어 있음. 기존 방법들은 잘 형성된 문장이 주어지거나 단편적 번역에 초점을 맞춤.

- **Gap**: 교과서와 논문 규모의 형식화는 **크로스 파일 의존성 관리, 임포트 해결, 전체 프로젝트의 end-to-end 컴파일 보장**이라는 상류(upstream) 문제가 미해결 상태. 이는 단순 증명 탐색보다 프로젝트 수준의 구조 오류(네임스페이스, 타입 체크, 의존성 정렬)가 더 큰 병목.

- **Why**: 형식 수학 라이브러리(mathlib, OptLib) 성장의 주요 장애물은 개별 증명이 아닌 프로젝트 컴파일 단계의 비용과 복잡도임.

- **Approach**: **검증자 인증 정제(VeriRefine, Verifier-Certified Refinement)** 원시 도입: Lean 툴체인 피드백을 유일한 수용 신호로 삼아, 컴파일 오류 감소 또는 증명 구멍 해결 시에만 편집을 커밋하는 two-stage 파이프라인.

## Achievement

![Figure 2: FATE-H에서의 PSR 비교](figures/fig2.webp)

1. **프로젝트 규모 형식화의 실현**: 
   - 실수 해석(Real Analysis) 312페이지, 볼록 해석(Convex Analysis) 140페이지, 논문 27페이지 총 479페이지를 3주 내에 **241개 파일, 4,116개 선언, 153,853줄의 완전 컴파일 가능한 Lean 라이브러리**로 변환
   - 전체 프로젝트 end-to-end 엘라보레이션(elaboration) 성공 달성
   - 이는 전문가가 수개월~수년 걸릴 작업을 자동화

2. **강력한 증명 성능**: 
   - FATE-H 벤치마크에서 **96% 증명 성공률(PSR)** 달성 (기준선 Seed-Prover 1.5: 80%, +16포인트 향상)
   - 매칭된 문장 조건에서 Stage 2의 100% PSR 달성 (컴파일된 프로젝트 내)

## How

![Figure 4: 워크플로우 능력 선언(Verifier-in-the-loop 파이프라인)](figures/fig4.webp)

### Stage 1: 문장 컴파일(Statement Compilation)

- **문서 분해**: LaTeX/PDF를 JSON 아이템으로 정규화, 페이지 정렬 추출 및 의존성 복구
- **선언 스켈레톤 생성**: LLM이 각 JSON 아이템에 대해 Lean 선언 제안 (증명에 sorry 허용)
- **의존성 추론 및 순서 정렬**: 원자 블록 간의 의존성 그래프 구축, 컴파일 가능한 순서 결정
- **반복적 수리**: VerifyFile(P, f) → (ok, Δf) 호출로 오류 진단, 제한된 패치 제안 및 검증자 피드백 기반 수용/취소
- **수렴 조건**: 모든 모듈/임포트가 오류 없이 엘라보레이션될 때까지 반복 (경고는 무시)

### Stage 2: 증명 수리(Proof Repair)

- **고정된 서명**: Stage 1의 문장 시그니처 잠금, 증명 본문과 선택적 로컬 헬퍼만 편집
- **목표 조건부 로컬 편집**: sorry 플레이홀더 위치 특정, 해당 Lean 선언 탐색
- **증명 계획 및 오류 수정**: 증명 후보 패치 제안 → 실패 시 진단 기반 제한 수리 및 재계획
- **파일 크기 가드**: 파일 오버사이징 전에 분할 트리거로 검증 안정성 유지
- **검증 정규화 예산**: VerifyFile 호출 횟수로 계산하여 벽시계 시간 변동성 감소

### VeriRefine 원시 (공통)

```
Edit Propose → VerifyFile → {
  if (err(Δ) < err(Δ_prev)) or (compiled && goal reduced):
    Commit
  else:
    Revert
}
```

## Originality

- **첫 프로젝트 규모 자동 형식화 프레임워크**: 기존 연구는 개별 증명이나 스니펫에 국한, M2F는 **전체 교과서/논문의 end-to-end 컴파일 가능성**을 최초로 달성

- **검증자 인증 정제(VeriRefine) 원시**: Lean 툴체인 피드백만을 수용 신호로 사용하는 새로운 정제 알고리즘. 회귀 누적 방지 및 측정 가능한 진행 보장

- **두 단계 분리 전략**: 지식 임포트(문장)와 증명 의무 해결(증명)을 분리하여, 프로젝트 수준의 구조 안정화 후 증명 탐색 수행. 기존의 병렬 또는 무차별 접근과 구별

- **출처 연결(Provenance) 기반 평가**: Span(D) → Decl(P) 매핑으로 형식 선언과 원문을 추적, 충실도 감시 및 end-to-end 평가 프로토콜 지원

- **검증자 정규화 메트릭**: 벽시계 시간 대신 VerifyFile 호출로 계산하여, 서로 다른 런과 에이전트 간 공정한 비교 가능

## Limitation & Further Study

### 한계

- **고정 환경 의존성(E)**: Lean 툴체인 버전과 mathlib 스냅샷이 고정되어야 하므로, 라이브러리 업데이트 시 형식화된 코드 유지보수 부담 발생 가능

- **순환 의존성(Circular Dependency) 미처리**: 현재 DAG 기반 의존성 순서 정렬이므로, 상호 참조가 있는 수학 구조 표현에 제약

- **LLM 제안의 의존성**: 초기 선언 스켈레톤과 증명 패치 제안이 LLM 능력에 의존. 강력한 기초 모델이 필수

- **평가 범위 제한**: FATE-H는 문장이 이미 형식화된 벤치마크. 불완전하거나 모호한 원문에 대한 견건성 평가 부족

- **스케일 한계 미확인**: 153K 줄은 상당하지만, 수백만 줄의 대규모 라이브러리나 이질적 영역의 혼합에 대한 확장성은 불명확

### 후속 연구

- 순환 의존성 처리를 위한 양방향 타입 체킹 또는 모듈 시스템 확장

- 동적 환경(라이브러리 업그레이드)에 대응하는 자동 코드 마이그레이션 파이프라인 개발

- 불완전한 또는 비공식적 원문(위키, 블로그)에 대한 견건성 강화

- 다른 증명 보조기(Coq, Isabelle, Agda) 지원 확대로 형식화 커버리지 증대

- 인간-AI 협업 모드에서의 상호작용 설계 및 검증자 피드백 가시화 개선


## Evaluation

- Novelty: 5/5
- Technical Soundness: 4.5/5
- Significance: 5/5
- Clarity: 4/5
- Overall: 4.5/5

**총평**: M2F는 자동 형식화 분야의 **패러다임 전환**을 시도하는 논문이다. 기존의 고립된 증명 탐색에서 벗어나 프로젝트 규모의 구조 문제(의존성, 임포트, 타입 안정성)를 **검증자 피드백 루프**로 해결하는 VeriRefine 원시는 창의적이며, 153K 줄의 완전 컴파일 가능한 Lean 코드 생성은 학술 기준을 크게 상회한다. 다만 고정 환경 의존성, 순환 의존성 미처리, 비정형 원문 견건성 등이 한계로 남아 있어, 완전한 산업 배포까지는 추가 작업이 필요하다.

## Related Papers

- 🏛 기반 연구: [[papers/264_Deepseek-prover_Advancing_theorem_proving_in_llms_through_la/review]] — 수학적 증명과 형식화에서 LLM의 근본적인 추론 능력 향상 방법론을 제공한다.
- 🔗 후속 연구: [[papers/482_Lean-star_Learning_to_interleave_thinking_and_proving/review]] — 기본적인 정리 증명을 대규모 교과서 형식화로 확장하여 실용적 응용 가능성을 보여준다.
- 🧪 응용 사례: [[papers/828_Towards_end-to-end_automation_of_AI_research/review]] — 수학 형식화 자동화가 과학 연구 전체 자동화의 핵심 구성요소로 작용할 수 있음을 입증한다.
