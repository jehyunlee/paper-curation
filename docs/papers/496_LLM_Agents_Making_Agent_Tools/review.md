---
title: "496_LLM_Agents_Making_Agent_Tools"
authors:
  - "G. Wölflein"
  - "Dyke Ferber"
  - "D. Truhn"
  - "Ognjen Arandjelovi'c"
  - "J. Kather"
date: "2025"
doi: "10.48550/arXiv.2502.11705"
arxiv: ""
score: 4.2
essence: "TOOLMAKER는 과학 논문의 공개 코드 저장소로부터 LLM 호환 도구를 자동으로 생성하는 에이전트 프레임워크로, 기존에 사람이 수동으로 구현해야 했던 복잡한 과학 도구들을 자동화한다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/Multi-Agent_Language_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Wölflein et al._2025_LLM Agents Making Agent Tools.pdf"
---

# LLM Agents Making Agent Tools

> **저자**: G. Wölflein, Dyke Ferber, D. Truhn, Ognjen Arandjelovi'c, J. Kather | **날짜**: 2025 | **DOI**: [10.48550/arXiv.2502.11705](https://doi.org/10.48550/arXiv.2502.11705)

---

## Essence

![Figure 1](figures/fig1.webp) *에이전트가 런타임에 동적으로 확장 가능한 도구 집합을 보유하는 미래 비전*

TOOLMAKER는 과학 논문의 공개 코드 저장소로부터 LLM 호환 도구를 자동으로 생성하는 에이전트 프레임워크로, 기존에 사람이 수동으로 구현해야 했던 복잡한 과학 도구들을 자동화한다.

## Motivation

- **Known**: 
  - LLM 에이전트는 외부 도구(tool) 활용을 통해 다단계 추론 능력을 보유하며, 소프트웨어 공학, 의료, 법률, 과학 연구 등 다양한 분야에서 성과를 보임
  - 재현성에 대한 과학 커뮤니티의 강조로 연구 논문에 공개 코드가 대량으로 공개되고 있음

- **Gap**: 
  - 현존 LLM 에이전트들은 사람 개발자가 사전에 구현하고 통합한 도구에만 의존하여, 도구의 부재 또는 부적절함으로 인해 일반화 능력이 제한됨
  - 기존 도구 생성(tool creation) 방식들(CRAFT, CREATOR, LATM)은 도구를 처음부터 구축하기 때문에 단순한 기능만 가능하며, OS 상호작용이나 복잡한 외부 의존성 관리를 할 수 없음
  - 의료/생물학 분야 연구자들은 높은 기술 진입장벽으로 인해 공개된 복잡한 도구들을 효과적으로 활용하지 못함

- **Why**: 
  - 현대 과학 도구의 복잡도(계산 요구사항, 데이터 요구량, 코드량)가 급증하여 수동 개발이 현실적이지 않음
  - 의료 같은 고위험 분야에서는 엄격한 검증, 테스트, 품질보증이 필수이므로 처음부터 구축한 도구는 신뢰성 문제 야기

- **Approach**: 
  - 기존 공개 코드 저장소를 재활용하는 방식으로 전환하여, 이미 검증된 도구들을 LLM 호환 형태로 자동 변환
  - 환경 설정(Docker)과 도구 구현(Python 함수) 두 단계의 에이전트 워크플로우 설계
  - 자체 수정 메커니즘(closed-loop self-correction)으로 디버깅 자동화

## Achievement

![Figure 2](figures/fig2.webp) *TOOLMAKER의 입력(작업 설명, 논문, GitHub URL, 사용 예시)과 출력(Docker 컨테이너, Python 함수)*

1. **벤치마크 구축**: 
   - TM-BENCH: 의료(병리학, 방사선학, 오믹스) 및 비의료(LLM, 3D 비전) 분야의 15개 복잡한 계산 작업과 100개 이상의 단위 테스트로 구성
   - 기존 벤치마크와 달리 의존성 사전 설치 가정 없이 완전 개방형 환경에서 평가

2. **우수한 성과**: 
   - 80% 작업 성공률로 현존 최고 수준의 소프트웨어 공학 에이전트(OpenHands 등)를 크게 상회
   - 종단간(end-to-end) 워크플로우 지원: 리소스 다운로드, 의존성 관리, 대규모 코드베이스 탐색, 코드 구현/테스트/디버깅

## How

![Figure 3](figures/fig3.webp) *TOOLMAKER 워크플로우: 환경 설정 → 도구 구현 단계의 2단계 프로세스*

### 핵심 설계 요소

**1) 워크플로우 상태 표현**
- 상태 s = ⟨h, e⟩로 정의 (h: 대화 이력, e: 환경 상태)
- 모든 컴포넌트는 S → S × R 함수로 모델링 (상태 변환 + 반환값)

**2) 워크플로우 컴포넌트**
- **LLM 호출**: 대화 이력만 업데이트 (환경 미변경)
  - OpenAI gpt-4o-2024-08-06 모델 사용
- **환경 상호작용**: Docker 컨테이너에서 bash 명령 실행, 파일 읽/쓰기, 실행 결과 관찰
  - 의존성 설치, 모델 다운로드, 환경 변수 설정 등 OS 조작 가능
- **에이전트**: 두 요소 조합으로 자동 결정 및 실행

**3) 2단계 워크플로우**

**Stage 1: 환경 설정 (Environment Setup)**
- GitHub 저장소 클론, requirements 파일 분석
- 의존성 설치 시도 및 충돌 해결
- 체크포인트된 Docker 이미지로 재현 가능한 스냅샷 생성

**Stage 2: 도구 구현 (Tool Implementation)**
- 코드베이스 탐색 및 관련 함수/클래스 식별
- 작업 설명과 입출력 인자 기반으로 Python 함수 생성
- 단위 테스트 실행 및 오류 수정을 위한 폐쇄 루프 자기 수정(self-correction)

**4) 자기 수정 메커니즘**
- 테스트 실패 시 에러 메시지 분석
- LLM이 코드 수정 방안 재생성
- 최대 반복 횟수까지 재시도

**5) 최소한의 도구 정의**
- 작업 설명 (텍스트)
- GitHub URL
- 필수 입력 인자 목록 + 예시값

## Originality

- **새로운 문제 정의**: 기존 "도구 생성"(처음부터 구축)과 달리 "도구 변환"(기존 코드 재활용) 패러다임으로 전환
  
- **OS 상호작용 통합**: 이전 도구 생성 방식들(CRAFT, CREATOR, LATM)이 불가능했던 bash 명령, 파일 I/O, 웹 브라우징 등 실제 OS 조작 구현

- **복잡한 실제 작업 지원**: 
  - 단순 수학 문제가 아닌 의존성 설치, 모델 다운로드, 대규모 코드베이스 탐색을 포함하는 실제 과학 연구 도구 자동화

- **포괄적 벤치마크**: 
  - 기존 벤치마크(HumanEval, CodexGLUE 등)는 표준 라이브러리만 사용하는 단순 함수 생성만 평가
  - TM-BENCH는 종단간 실제 워크플로우 평가로 실무 적용성 검증

- **의료/과학 도메인 특화**: 
  - 병리학, 방사선학, 오믹스 등 고급 도메인별 작업으로 학제간 적용성 입증

## Limitation & Further Study

- **Docker 의존성**: 
  - Docker 컨테이너에 의존하여 배포 환경의 제약 가능성
  - 일부 특수한 GPU/하드웨어 설정에서 호환성 문제 가능

- **코드 이해의 한계**: 
  - 매우 큰 코드베이스(수십만 줄)에서는 관련 함수 식별의 정확도 저하 예상
  - 암시적 전역 상태나 복잡한 초기화 로직이 있는 경우 자동화 어려움

- **일반화 한계**: 
  - TM-BENCH가 15개 작업으로 제한되어 다양한 도메인으로의 일반화 검증 필요
  - 학술 논문 코드의 품질 편향(publication bias) 미반영

- **후속 연구 방향**:
  - 멀티에이전트 협력을 통한 더 복잡한 도구 생성
  - 동적 도구 선택 및 조합으로 메타-도구(meta-tool) 개발
  - 도구 검증/테스트 자동화를 위한 형식 검증(formal verification) 도입
  - 프라이빗 데이터가 있는 실험 환경에서의 안전한 도구 생성
  - 사용자 피드백 기반 반복적 도구 개선 메커니즘

## Evaluation

- **Novelty**: 4.5/5
  - 기존 도구 생성 연구의 패러다임 전환(처음부터 구축 → 재활용)은 창의적
  - OS 상호작용 통합은 실질적 진전
  - 다만 LLM 에이전트 아키텍처 자체는 기존 기법의 조합

- **Technical Soundness**: 4/5
  - 워크플로우 상태 모델링(⟨h, e⟩) 및 컴포넌트 설계는 명확하고 체계적
  - Docker 기반 재현성 보장이 적절
  - 자기 수정 루프의 수렴성/반복 한계에 대한 이론적 논의 부족
  - 테스트 커버리지 설정의 주관성(어떤 테스트가 충분한가) 미해결

- **Significance**: 4.5/5
  - 의료/생명과학 등 고급 도메인의 LLM 에이전트 실용화에 직접적 기여
  - 공개 과학 코드의 재활용을 통해 연구 민주화 가능성 제시
  - 80% 성공률은 실무 배포 가능성을 시사
  - 응용 범위는 명확하나 근본적인 AI 연구 이론으로의 기여는 제한적

- **Clarity**: 4/5
  - 전체 구조와 동기 설명이 명확하고 figures가 효과적
  - Figure 3의 워크플로우가 이해하기 쉬움
  - 수식 표기(⟨h, e⟩, S, H, E 등)가 정확하나 본문에서 더 자세한 설명 필요
  - 구체적 프롬프트 예시나 에러 처리 케이스 상세 설명 부족

- **Overall**: 4.2/5

**총평**: TOOLMAKER는 공개 과학 코드 재활용이라는 현실적인 문제를 타깃하여 LLM 에이전트의 실용성을 크게 향상시킨 논문으로, 특히 의료/과학 분야에서의 도구 접근성 민주화라는 중요한 사회적 임팩트를 제시한다. 다만 이론적 기여는 제한적이며, 벤치마크 규모 확대와 실제 배포 환경에서의 신뢰성 검증이 향후 과제이다.

## Related Papers

- 🔄 다른 접근: [[papers/122_Automated_Extraction_of_Mechanical_Constitutive_Models_from/review]] — TOOLMAKER의 코드 저장소 기반 도구 생성과 기계적 구성 모델의 문헌 기반 추출은 서로 다른 소스에서 과학 도구를 자동 생성하는 접근이다.
- 🔗 후속 연구: [[papers/813_Toolformer_Language_Models_Can_Teach_Themselves_to_Use_Tools/review]] — Toolformer의 언어 모델 자체 도구 사용 학습이 TOOLMAKER의 과학 논문 기반 자동 도구 생성으로 발전한 확장된 형태이다.
- 🏛 기반 연구: [[papers/499_LLM_With_Tools_A_Survey/review]] — 도구 사용을 위한 LLM 조사 연구가 TOOLMAKER의 과학 도구 자동 생성 및 LLM 호환성 구현의 이론적 기반을 제공한다.
- 🔄 다른 접근: [[papers/122_Automated_Extraction_of_Mechanical_Constitutive_Models_from/review]] — 기계적 구성 모델의 문헌 기반 추출과 TOOLMAKER의 코드 저장소 기반 도구 생성은 서로 다른 소스에서 과학 지식을 자동화하는 대안적 접근이다.
