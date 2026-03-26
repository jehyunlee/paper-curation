# MerLean: An Agentic Framework for Autoformalization in Quantum Computation

> **저자**: Yuanjie Ren, Jinzheng Li, Yidi Qi | **날짜**: 2026-02-18 | **Repository**: arXiv | **arXiv ID**: 2602.16554

---

## Essence

양자 계산 이론 분야의 연구 논문을 LaTeX 소스로부터 Lean 4 형식 증명 코드로 완전 자동 변환하는 에이전틱 프레임워크 MerLean을 제안한다. 추출-형식화-검증의 autoformalization 파이프라인과 검증된 코드를 다시 사람이 읽을 수 있는 LaTeX로 역변환하는 autoinformalization 파이프라인을 결합하여, 양방향 검증을 가능하게 한다. 3편의 양자 계산 논문(114개 명제)에서 2,050개 Lean 선언, 41,000줄 이상의 검증된 코드를 생성하여 end-to-end 형식화에 성공하였으며, 인간 개입 없이 완전 자동으로 수행되었다.

## Motivation

- **알려진 사실**: Autoformalization은 자연어 수학을 형식 검증 가능한 코드로 변환하는 것이 목표이며, LLM이 이 작업에 적합함이 입증됨. 양자 계산 이론은 선형대수, 그래프이론, 대수적 위상수학과 깊은 연결을 가지며, arXiv quant-ph의 연간 11,891편(2025년)이라는 검증 병목이 존재
- **격차(Gap)**: 기존 autoformalization 연구는 개별 정리/경쟁 문제 수준에 머물며, 전체 논문의 상호 연결된 정의-보조정리-정리를 end-to-end로 형식화하는 것은 미해결. Ax-Prover, Numina-Lean-Agent 등 최근 에이전틱 시스템도 인간 가이던스에 의존
- **접근법**: Claude Opus 4.5를 추론 엔진으로, lean-lsp-mcp를 통한 Lean 언어 서버 도구(goal 검사, hover info, semantic search)를 활용하여, compile-fix-verify 루프로 전체 논문을 자동 형식화

## Achievement

1. **3편 논문의 완전 자동 end-to-end 형식화**: Balanced Product Codes(44 명제, 14,997줄), Fault-Tolerant QC(47 명제, 18,557줄), Quantum Topology(23 명제, 미공개, 7,761줄)
2. **총 114개 명제에서 2,050개 Lean 선언 생성**: 평균 명제당 18.0개 선언, 21분 54초, 13.0회 컴파일 시도
3. **인간 개입 없는 형식화**: 기존 Ax-Prover, Numina-Lean-Agent와 달리 형식화 과정에서 human-in-the-loop 불필요
4. **데이터 오염 없는 검증**: Paper C(Quantum Topology)는 미공개 원고로 LLM 학습 데이터에 포함될 수 없음을 보장
5. **자동 보조 정리 발견**: 원논문에 명시되지 않은 중간 단계 보조 정리(edgeBoundary_card_eq_edgeCount, weight_inequality_core 등)를 에이전트가 자율적으로 도입
6. **연구 오류 발견**: Quantum Topology 논문의 모호한 정의에서 암묵적 가정 누락을 형식화 과정에서 발견, 저자가 수정 후 완전 형식화 성공

## How

- **Autoformalization 파이프라인**: (1) LaTeX 소스에서 수학적 명제 추출 및 다중 패스 정제(모호한 표현 구체화, 의존성 정렬) -> (2) 각 명제에 대해 compile-fix 루프(Lean 4 코드 생성 -> 컴파일 -> 오류 시 진단 피드백으로 수정, 최대 30회) -> (3) 컴파일 성공 후 faithfulness checking(원문 의미 반영 여부 자기 점검) -> (4) 최대 시도 초과 시 axiom phase(차단 subgoal을 공리로 변환)
- **Autoinformalization 파이프라인**: 검증된 Lean 코드를 사람이 읽을 수 있는 LaTeX "blueprint"로 역변환하여 의미적 정합성 검토 지원
- **도구**: Claude Opus 4.5(추론 엔진), lean-lsp-mcp(Model Context Protocol 서버, goal 검사/type signature/semantic search), leansearch/loogle(Mathlib 정리 검색), grep(Mathlib 소스 탐색)
- **Axiom 처리**: Mathlib에 없는 결과(Kunneth formula, spectral sequence 등)는 명시적 공리로 선언, sorry(불완전 증명)와 구분

## Originality

연구 논문 전체를 인간 개입 없이 완전 자동으로 형식화한 최초의 시스템이다. Ax-Prover나 Numina-Lean-Agent가 인간 가이던스(정의/정리/증명 전략 제공)에 의존하는 것과 달리, MerLean은 LaTeX 소스만으로 추출-형식화-검증-역변환의 전 과정을 자동화한다. 특히 autoinformalization을 통한 양방향 파이프라인은 형식화의 충실성(faithfulness)을 비전문가도 검토할 수 있게 하며, 미공개 원고에서의 오류 발견 사례는 형식화 기반 peer review의 실용적 가능성을 보여준다.

## Limitation & Further Study

### 저자들이 언급한 한계
- Mathlib의 공백(gaps)으로 인해 일부 명제(Balanced Product Codes의 9.1%)가 공리에 의존
- 기존 autoformalization 벤치마크(miniF2F, ProofNet)가 개별 정리 수준이어서 직접 비교가 불가능
- 양자 계산의 수학적 기반(선형대수, 함수해석)이 Mathlib에서 상대적으로 성숙하여, 다른 분야로의 일반화는 미검증

### 리뷰어 판단 아쉬운 점
- 정량적 비교 대상이 없어 성능의 상대적 위치를 판단하기 어려움 (M2F의 FATE-H 96%와 같은 외부 벤치마크 결과 부재)
- Faithfulness checking이 LLM의 자기 점검(self-reflection)에 의존하여, 체계적 오류의 탐지 보장이 없음. Autoinformalization이 이를 보완하나, 최종적으로 인간 검토에 의존
- 114개 명제 중 실제 "정리(theorem)"는 15개에 불과하고 나머지는 정의(49), 비고(26), 보조정리(20), 따름정리(4)로, 증명 난이도가 높은 핵심 결과의 비중이 제한적
- 3편 논문 모두 양자 계산 이론이라는 단일 도메인이므로, 대수기하, 정수론 등 다른 수학 분야에서의 성능은 미지수
- 공리(axiom) 선언의 적절성 판단이 수동 검토에 의존하며, 과도한 공리화로 형식화가 사실상 무의미해질 위험에 대한 체계적 제어가 없음

### 후속 연구
- 기존 autoformalization 벤치마크(miniF2F, ProofNet, FATE-H)에서의 정량적 평가
- 대수기하, 정수론 등 Mathlib 지원이 약한 분야로의 확장
- 논문 간 교차 형식화(여러 관련 논문의 결과를 하나의 통합 라이브러리로)
- 형식화 기반 자동 peer review 워크플로우의 실제 적용 및 평가

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 4/5 |
| Technical Soundness | 4/5 |
| Significance | 4/5 |
| Clarity | 4/5 |
| Overall | 4/5 |

**총평**: 연구 논문 전체의 완전 자동 형식화라는 의미 있는 마일스톤을 달성한 논문이다. 인간 개입 없이 3편의 양자 계산 논문을 41,000줄 이상의 검증된 Lean 코드로 변환한 성과는 인상적이며, autoinformalization을 통한 양방향 파이프라인과 미공개 원고에서의 오류 발견 사례는 형식화의 실용적 가치를 잘 보여준다. 다만 단일 도메인(양자 계산), 외부 벤치마크 부재, faithfulness의 자기 점검 의존성이 주요 한계이다. M2F와 비교하면 규모는 작지만(41K vs 154K LoC), 완전 자동이라는 점에서 차별화된다.
