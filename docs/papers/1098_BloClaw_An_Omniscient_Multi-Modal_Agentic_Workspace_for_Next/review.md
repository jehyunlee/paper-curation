---
title: "1098_BloClaw_An_Omniscient_Multi-Modal_Agentic_Workspace_for_Next"
authors:
  - "Yao Qin"
  - "Yangyang Yan"
  - "Jinhua Pang"
  - "Xiaoming Zhang"
date: "2026"
doi: "10.48550/ARXIV.2604.00550"
arxiv: ""
score: 4.0
essence: "BloClaw는 LLM 기반 AI 과학자를 위한 멀티모달 운영체제로, XML-Regex 라우팅, 실행 샌드박스 모니터링, 동적 UI를 통해 JSON 기반 도구 호출의 취약성을 해결한다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/Multi-Agent_Scientific_Frameworks"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Qin et al._2026_BloClaw An Omniscient, Multi-Modal Agentic Workspace for Next-Generation Scientific Discovery.pdf"
---

# BloClaw: An Omniscient, Multi-Modal Agentic Workspace for Next-Generation Scientific Discovery

> **저자**: Yao Qin, Yangyang Yan, Jinhua Pang, Xiaoming Zhang | **날짜**: 2026 | **DOI**: [10.48550/ARXIV.2604.00550](https://doi.org/10.48550/ARXIV.2604.00550)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1: Global Architecture of BloClaw. Demonstrating*

BloClaw는 LLM 기반 AI 과학자를 위한 멀티모달 운영체제로, XML-Regex 라우팅, 실행 샌드박스 모니터링, 동적 UI를 통해 JSON 기반 도구 호출의 취약성을 해결한다.

## Motivation

- **Known**: LLM을 과학 연구에 통합한 AI Scientists 프레임워크(ChemCrow, Coscientist 등)가 존재하지만, 실제 배포 환경에서 JSON 직렬화 실패, 그래픽 출력 손실, 경직된 인터페이스 문제가 발생한다.
- **Gap**: 현재 Agent-Tool 통신 방식은 JSON 스키마에 의존하여 복잡한 코드나 화학 구조식 생성 시 직렬화 붕괴가 발생하며, LLM이 시각화 저장을 누락할 때 출력이 손실되는 문제가 있다.
- **Why**: 과학 발견 자동화가 LLM 기반으로 진화하고 있으나, 프로덕션 환경의 기술적 병목이 AI4S(AI for Science) 실용화를 저해하고 있어 근본적인 아키텍처 혁신이 필요하다.
- **Approach**: BloClaw는 (1) XML-Regex 이중 추적 라우팅, (2) Python monkey-patching 기반 런타임 상태 가로채기, (3) 상태 주도형 동적 뷰포트 UI의 세 가지 아키텍처 혁신을 통해 문제를 해결한다.

## Achievement

![Figure 2](figures/fig2.webp)

*Figure 2: Comparison between traditional JSON decoding*

- **XML-Regex 라우팅 프로토콜**: JSON 대비 오류율 0.2%(JSON 17.6%)로 직렬화 실패 통계적 제거
- **런타임 상태 가로채기 샌드박스**: Python monkey-patching으로 Plotly/Matplotlib 시각화를 자동 캡처하여 100% 시각 렌더링 성공률 달성
- **멀티모달 통합**: 화학정보학(RDKit), 단백질 폴딩(ESMFold), 분자 도킹, RAG 등 4가지 과학 모달리티 종합 벤치마킹
- **자가 진화 능력**: CREATE_TOOL 지시어를 통한 자동 도구 생성 및 저장으로 지속적 기능 확장
- **멀티모달 파일 RAG**: PDF/CSV/PDB 파일 150ms 이내 처리로 99-100% 성공률 달성

## How

![Figure 3](figures/fig3.webp)

*Figure 3: The Runtime State Interception Protocol seam-*

- LLM에게 의미론적 XML 태그(<thought>, <action>, <target>)로 응답 포맷 지정 후 Regex Maximal Extraction으로 최장 연속 유효 문자열 추출
- Python exec() 격리 환경 내에서 plt.show() 무효화 및 실행 후 Plotly/Matplotlib 객체를 강제 가로채 Base64/HTML로 컴파일
- MVC 패러다임의 decoupled 아키텍처로 계산 작업을 프론트엔드과 분리하여 상태 관리 안정성 확보
- 로컬 RDKit 바이너리 연결, ESMAtlas API 라우팅, 3Dmol.js 렌더링으로 화학/생물 모달리티 통합
- PyPDF2와 pandas를 통한 다중 파일 형식 프로빙 및 LLM 기반 데이터 파이프라인 자동 생성

## Originality

- JSON 대신 XML-Regex 이중 추적 라우팅으로 LLM 할루시네이션 견고성 획기적 개선(37% → 0.95% 오류율)
- Monkey-patching을 통한 'hijacked execution sandbox'로 LLM이 I/O 누락 시에도 100% 시각화 캡처", '상태 주도형 동적 뷰포트로 minimal command deck과 interactive spatial rendering 간 seamless morphing
- 자동 도구 생성(CREATE_TOOL)으로 AGI의 tool-making 특성을 구현한 자가 진화 패러다임
- 멀티모달 실시간 RAG와 구조 생물학 시뮬레이션의 통합으로 종합 AI4S 플랫폼 구현

## Limitation & Further Study

- 논문이 2026년 4월 arXiv 게재로 향후 peer review 거쳐야 하며, 장기 안정성 데이터 부재
- stress test가 N=1k 규모이고 실제 대규모 배포 환경에서의 성능 검증 필요
- Local-LLM 통합과 로봇 액체 핸들러 API(Self-Driving Labs)는 미래 계획으로 아직 미구현
- CORS 우회, monkey-patching 등 기술이 보안/샌드박스 강건성 측면 상세 분석 부족
- 후속 연구는 zero-trust 배포, 로봇 통합, 더 큰 규모 과학 워크플로우 검증 필요

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: BloClaw는 LLM 기반 과학 자동화의 실제 배포 병목을 명확히 진단하고 XML-Regex, monkey-patching, 동적 UI 등 혁신적 기술로 대폭 해결한 중요한 시스템이다. 종합적 벤치마킹과 실용적 성과로 AI4S 분야의 실질적 진전을 제시하나, 대규모 배포와 보안 면에서의 추가 검증이 필요하다.

## Related Papers

- 🏛 기반 연구: [[papers/769_StableToolBench_Towards_Stable_Large-Scale_Benchmarking_on_T/review]] — BloClaw의 멀티모달 에이전트 작업공간은 StableToolBench의 대규모 도구 벤치마킹 연구에서 확인된 도구 사용 안정성 요구사항을 기반으로 XML-Regex 라우팅 시스템을 설계했습니다.
- 🔗 후속 연구: [[papers/815_ToolLLM_Facilitating_Large_Language_Models_to_Master_16000_R/review]] — BloClaw는 ToolLLM의 16000+ 도구 마스터링 프레임워크를 확장하여 JSON 기반 도구 호출의 취약성을 해결하는 더 견고한 도구 통합 환경을 제공합니다.
