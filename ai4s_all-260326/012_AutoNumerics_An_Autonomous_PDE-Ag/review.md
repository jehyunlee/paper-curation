# AutoNumerics: An Autonomous, PDE-Agnostic Multi-Agent Pipeline for Scientific Computing

> **저자**: Jianda Du, Youran Sun, Haizhao Yang | **날짜**: 2026-02-19 | **Repository**: arXiv | **arXiv ID**: 2602.17607

---

## Essence

자연어로 기술된 편미분방정식(PDE) 문제를 입력받아, LLM 기반 멀티 에이전트 시스템이 자율적으로 수치 솔버를 설계-구현-디버깅-검증하는 프레임워크 AutoNumerics를 제안한다. 블랙박스 뉴럴 솔버와 달리 고전 수치해석에 기반한 해석 가능한(transparent) 솔버를 생성하며, coarse-to-fine 실행 전략과 잔차(residual) 기반 자기 검증 메커니즘을 도입하였다. 24개 대표 PDE 문제에서 CodePDE 대비 약 6자릿수 이상 낮은 오차를 달성하였다.

## Motivation

- **알려진 사실**: PDE는 과학/공학 모델링의 수학적 기초이나, 정확한 수치 솔버 설계에는 이산화 기법 선택, 안정성/수렴 조건 검증 등 상당한 전문 지식이 필요함. PINNs, FNO 등 뉴럴 솔버는 유연하나 계산 비용이 높고 해석 가능성이 낮음
- **격차(Gap)**: 기존 LLM 기반 PDE 접근법은 블랙박스 뉴럴 네트워크 생성(Lang-PINN), 고정 라이브러리(FEniCS) 호출, 또는 코드 생성(CodePDE)에 한정되며, 수치 기법의 자율적 선택과 정확성 검증이 통합되지 않음
- **접근법**: Planner-Coder-Critic-Selector-Reasoning의 멀티 에이전트 파이프라인으로, 후보 수치 기법 생성 -> 구현 -> coarse-to-fine 디버깅 -> 잔차 기반 검증 -> 최적 솔버 선택의 전 과정을 자동화

## Achievement

1. **CodePDE 벤치마크 5개 문제 전부에서 최저 오차 달성**: 기하 평균 nRMSE 9.00x10^-9로, CodePDE(5.08x10^-3) 및 FNO(9.52x10^-3) 대비 약 6자릿수 우위
2. **200개 PDE 벤치마크 구축**: 1D~5D, 타원/포물/쌍곡형, 선형/비선형, Dirichlet/Neumann/주기 경계조건을 포괄하는 대규모 벤치마크 제안
3. **24개 대표 PDE 평가**: 해석해가 있는 19개 중 11개에서 상대 L2 오차 10^-6 이하, Poisson(5.41x10^-16)과 Helmholtz 2D(3.50x10^-16)에서 기계 정밀도 수준 달성
4. **PDE 구조 기반 자율적 수치 기법 선택**: 주기 경계 -> Fourier spectral, Dirichlet 타원형 -> Chebyshev spectral, Dirichlet 포물형 -> FD/FEM implicit 등 구조적으로 적절한 기법을 일관되게 선택
5. **Coarse-to-fine 전략의 효과**: 저해상도에서 논리 오류를 먼저 수정하고 고해상도에서 안정성 문제를 해결하여, 디버깅 효율을 높임

## How

- **프레임워크 구조**: (1) Planner Agent가 10개 후보 수치 기법 생성 및 점수화 -> (2) 상위 5개를 Coder Agent가 구현 -> (3) Critic Agent가 coarse grid에서 논리 오류 수정 -> (4) 고해상도 grid에서 안정성 검증 -> (5) 실패 시 Fresh Restart -> (6) 잔차 기반 검증 -> (7) Reasoning Agent가 이론적 분석 생성
- **검증 메트릭**: 해석해 있을 때 상대 L2 오차(eL2), 암묵적 해석 관계가 있을 때 implicit residual(eimpl), 해석해 없을 때 PDE 잔차(eres)의 3가지 메트릭 사용
- **LLM 백엔드**: GPT-4.1 단일 모델 사용
- **실행 설정**: 코드 생성/coarse grid/고해상도 실행의 최대 재시도 횟수 2/4/6회, 각 실행 최대 120초

## Originality

LLM 멀티 에이전트가 자연어 PDE 기술로부터 고전 수치해석 기반의 해석 가능한 솔버를 자율적으로 생성하는 최초의 end-to-end 프레임워크이다. 핵심 기여는 (1) 잘못 설계된(ill-designed) PDE 명세를 탐지하고 필터링하는 추론 모듈, (2) 논리 오류와 수치 안정성 문제를 분리하는 coarse-to-fine 전략, (3) 해석해 없이도 솔버 품질을 평가하는 잔차 기반 검증이며, 이들의 조합이 기존 뉴럴/LLM 기반 솔버 대비 극적인 정확도 향상을 이끌어냈다.

## Limitation & Further Study

### 저자들이 언급한 한계
- 고차원(5D 이상) 및 고차(4차) PDE에서 정확도가 현저히 떨어짐 (Biharmonic: 6.14x10^-1, 5D Helmholtz: 9.8x10^-1)
- 정규 도메인(regular domain)만 평가하였으며, 복잡한 기하 형상은 미검증
- GPT-4.1 단일 LLM에 종속되어 있으며, 생성된 코드에 대한 형식적 수렴/안정성 보장이 없음

### 리뷰어 판단 아쉬운 점
- 200개 PDE 벤치마크를 구축했으나 실제 평가는 24개에 국한되어, 벤치마크의 포괄성 대비 검증 범위가 좁음
- 실행 시간(20~230초)은 보고되었으나, LLM API 호출 비용에 대한 분석이 없어 실용성 판단이 어려움
- 비교 대상이 뉴럴 솔버(U-Net, FNO, PINN 등)와 CodePDE로 한정되어, 전문가가 직접 구현한 고전 솔버와의 비교가 부재
- Fresh Restart 메커니즘이 실패한 코드 경로를 완전히 폐기하므로, 부분적 수정이 가능한 경우에도 비효율적일 수 있음
- 비정형 도메인, 적응적 메시, 병렬 컴퓨팅 등 실제 과학 컴퓨팅의 핵심 요소가 다루어지지 않음

### 후속 연구
- 복잡 기하 도메인(비정형 메시, 다중 스케일) 지원 확장
- 다중 LLM 앙상블 또는 오픈소스 LLM으로의 백엔드 확장
- 생성된 솔버의 형식적 수렴 증명 자동 생성
- 역문제(inverse problem) 및 최적 제어 문제로의 확장
- 200개 전체 벤치마크에 대한 체계적 평가 및 공개

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 4/5 |
| Technical Soundness | 4/5 |
| Significance | 4/5 |
| Clarity | 4/5 |
| Overall | 4/5 |

**총평**: LLM 멀티 에이전트로 해석 가능한 고전 수치 솔버를 자율 생성하는 명확한 기여를 가진 논문으로, coarse-to-fine 전략과 잔차 기반 검증의 조합이 CodePDE 대비 6자릿수 이상의 정확도 향상을 이끌어낸 점이 인상적이다. 다만 정규 도메인과 저차원 문제에 국한된 평가, 단일 LLM 종속성, 그리고 실제 과학 컴퓨팅 워크플로우와의 괴리가 현재의 주요 한계이다.
