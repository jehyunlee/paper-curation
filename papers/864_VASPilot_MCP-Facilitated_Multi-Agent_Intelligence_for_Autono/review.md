---
title: "864_VASPilot_MCP-Facilitated_Multi-Agent_Intelligence_for_Autono"
authors:
  - "Jiaxuan Liu"
  - "Tiannian Zhu"
  - "Caiyuan Ye"
  - "Zhong Fang"
  - "Hongming Weng"
date: "2025.08"
doi: "10.48550/arXiv.2508.07035"
arxiv: ""
score: 4.0
essence: "VASPilot은 CrewAI 프레임워크와 Model Context Protocol(MCP)을 활용한 다중 에이전트 시스템으로, VASP(Vienna Ab initio Simulation Package) 밀도범함수이론(DFT) 계산의 전체 워크플로우를 완전 자동화한다. 이를 통해 연구자들은 계산 세부사항에서 벗어나 과학적 발견에 집중할 수 있다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/Computational_Fluid_Dynamics"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Liu et al._2025_VASPilot MCP-Facilitated Multi-Agent Intelligence for Autonomous VASP Simulations.pdf"
---

# VASPilot: MCP-Facilitated Multi-Agent Intelligence for Autonomous VASP Simulations

> **저자**: Jiaxuan Liu, Tiannian Zhu, Caiyuan Ye, Zhong Fang, Hongming Weng, Quansheng Wu | **날짜**: 2025-08-09 | **DOI**: [10.48550/arXiv.2508.07035](https://doi.org/10.48550/arXiv.2508.07035)

---

## Essence

![Figure 1](figures/fig1_overall_structure.webp)
*VASPilot의 전체 구조: 웹 서버, CrewAI 기반 다중 에이전트 협력 핵심, MCP 타입 도구 서버로 구성*

VASPilot은 CrewAI 프레임워크와 Model Context Protocol(MCP)을 활용한 다중 에이전트 시스템으로, VASP(Vienna Ab initio Simulation Package) 밀도범함수이론(DFT) 계산의 전체 워크플로우를 완전 자동화한다. 이를 통해 연구자들은 계산 세부사항에서 벗어나 과학적 발견에 집중할 수 있다.

## Motivation

- **Known**: VASP는 계산 재료과학에서 매우 중요한 도구이지만, 수동 설정, 모니터링, 후처리에 상당한 시간이 소요된다. VASPKIT, ASE, Pymatgen 등 기존 도구들이 입력 파일 생성과 기본 자동화를 제공하지만, 복잡한 다단계 작업에는 제한이 있다.

- **Gap**: 기존 도구들은 (1) 복잡한 다단계 작업의 자동화 부족, (2) 사용자 모니터링과 실시간 피드백 부재, (3) VASP에 특화된 다중 에이전트 프레임워크 부재라는 문제가 있다.

- **Why**: 최근 대규모언어모델(LLM)과 에이전트 기술의 발전은 복잡한 계산 워크플로우 자동화의 새로운 가능성을 열었다. 다중 에이전트 프레임워크는 복잡한 작업을 세분화하고, 전문화된 에이전트들의 조율된 실행으로 견고성과 확장성을 높일 수 있다.

- **Approach**: MCP 표준화 프로토콜과 CrewAI 프레임워크를 기반으로 (1) 4개 에이전트(Manager, Crystal Structure, VASP, Result Validation)의 협력 구조 설계, (2) VASP 특화 도구 세트 개발, (3) Flask 기반 웹 인터페이스 제공, (4) 다양한 벤치마크 검증을 수행했다.

## Achievement

![Figure 2](figures/fig2_tools_structure.webp)
*VASP 도구 구조: 입력파일 준비, 작업 제출, 계산 상태 확인, 결과 추출 및 시각화의 완전 자동화*

1. **완전 자동화 워크플로우**: 결정구조 검색(Materials Project)부터 입력파일 생성, Slurm 작업 제출, 에러 메시지 파싱, 동적 매개변수 조정을 통한 재시작까지 모든 단계를 수동 개입 없이 처리. 특히 '대기 계산(wait_calc)' 도구로 장시간 작업 중 네트워크 타임아웃 문제 해결.

2. **다양한 벤치마크 검증**: 
   - 자동 밴드구조(band structure) 및 상태밀도(DOS) 계산 (대칭성 보정 포함)
   - 평면파 커트오프(plane-wave cutoff) 수렴성 테스트
   - 다양한 반데르발스 보정을 포함한 격자 상수 최적화
   - 전이금속 이황화물(TMD)의 밴드갭 비교 분석
   모든 경우에서 수동 개입 없이 안정적으로 완료.

3. **직관적 사용자 인터페이스**: Flask 기반 웹 인터페이스로 실시간 진행 상황 추적, 실행 로그 접근, 구조 시각화, 플롯 드릴다운 제공.

4. **모듈식 확장성**: MCP 서버 배포만으로 다른 DFT 코드(Quantum Espresso 등)로 쉽게 확장 가능한 구조.

## How

- **다중 에이전트 설계**: Manager Agent가 사용자 미션을 이산적 작업으로 분해하여 전문화된 Worker Agent들(Crystal Structure, VASP, Result Validation)에 할당. 각 에이전트는 독립적 컨텍스트와 시스템 프롬프트 유지.

- **MCP 도구 서버**: VASP의 방대한 출력을 관리하기 위해 pymatgen 기반 도구 세트 구현
  - 입력파일 준비 및 Slurm 제출 (계산 ID 및 Slurm job ID 추적)
  - 상태 쿼리(check_calc_results): 실패 시 에러 메시지 반환, 성공 시 전체 결과 데이터베이스 저장
  - Python 플롯 도구(python_plot): 데이터베이스에서 계산 데이터 읽고 클라이언트 코드 실행

- **메모리 관리**: RAG(Retrieval-Augmented Generation) 기반 메모리 풀로 에이전트가 작업 시작 시 관련 이력 검색하여 컨텍스트 풍부화.

- **LLM 선택**: DeepSeek-V3-0324 사용 (다른 LLM으로 쉽게 교체 가능).

## Originality

- **VASP 특화 다중 에이전트 프레임워크**: 광범위한 VASP 사용자 기반에도 불구하고 VASP에 특화된 MAF가 부족했던 간격 메우기.

- **제로샷(Zero-shot) 미션 처리**: 사전 작업 예제 없이도 복잡한 미션을 처리 가능하도록 설계하여 적응성 극대화.

- **표준화된 MCP 프로토콜 적용**: 도구를 MCP로 캡슐화하여 다른 프레임워크에 최소 추가 작업으로 통합 가능한 재사용성 제공.

- **실시간 모니터링 인터페이스**: 과학자의 감시 필요성을 인정하고 직관적 웹 인터페이스로 결과 검증 가능성 보장.

- **에러 처리 및 동적 재시작**: 에러 메시지 파싱 후 매개변수 동적 조정으로 자동 재시작 능력.

## Limitation & Further Study

- **LLM 의존성**: 모든 에이전트가 동일 LLM(DeepSeek-V3)에 의존하므로, LLM의 성능 저하가 전체 시스템 영향. 다양한 LLM 조합의 효율성 비교 필요.

- **에러 처리 깊이**: 문서에서 "동적 매개변수 조정"이 구체적으로 어떤 규칙(휴리스틱)을 따르는지 명확하지 않음. 실패 원인 진단과 해결 전략의 더 정교한 설계 필요.

- **확장성 검증**: 초대형 시뮬레이션(수백 개 원자 이상) 또는 극도로 복잡한 워크플로우에서의 성능 평가 부재.

- **비용-효율성 분석**: 고성능 LLM 반복 호출의 연산 비용과 자동화로 절감되는 인적 비용의 정량적 비교 분석 필요.

- **후속 연구**: (1) 머신러닝 잠재력 탐사(생성 모델을 통한 새로운 구조 제안), (2) 실험 기기(로봇 팔 등)와의 통합, (3) 불확실성 정량화 및 신뢰도 평가 메커니즘 추가.


## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 3.5/5
- Overall: 4/5

**총평**: VASPilot은 LLM 기반 다중 에이전트 프레임워크를 VASP 자동화에 처음 체계적으로 적용한 의미 있는 시도로, 표준화된 MCP 프로토콜을 통해 재사용성과 확장성을 갖춘 실용적 도구이다. 다만 에러 처리의 깊이, 극단적 규모 작업의 검증, 그리고 동적 매개변수 조정 알고리즘의 투명성이 개선되면 더욱 강력한 기여가 될 수 있다.

## Related Papers

- 🔄 다른 접근: [[papers/589_OpenFOAMGPT_A_retrieval-augmented_large_language_model_LLM_a/review]] — OpenFOAM CFD 자동화와 유사하게 VASP DFT 계산을 자동화하는 다중 에이전트 시스템을 제시한다.
- 🔗 후속 연구: [[papers/133_Automating_quantum_computing_laboratory_experiments_with_an/review]] — 양자 컴퓨팅 실험 자동화에서 물리 계산 자동화로 확장된 응용 분야를 다룬다.
- 🧪 응용 사례: [[papers/826_Towards_Autonomous_Mathematics_Research/review]] — 자율적 수학 연구를 위한 자동화 시스템으로 계산 과학의 완전 자동화 비전을 공유한다.
- 🔄 다른 접근: [[papers/589_OpenFOAMGPT_A_retrieval-augmented_large_language_model_LLM_a/review]] — CFD 시뮬레이션 자동화와 유사하게 DFT 계산을 자동화하는 다중 에이전트 접근법을 제시한다.
