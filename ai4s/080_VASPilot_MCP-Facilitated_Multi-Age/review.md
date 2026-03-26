# VASPilot: MCP-Facilitated Multi-Agent Intelligence for Autonomous VASP Simulations

- **저자**: Jiaxuan Liu, Tiannian Zhu, Caiyuan Ye, Zhong Fang, Hongming Weng, Quansheng Wu
- **소속**: Institute of Physics, Chinese Academy of Sciences; University of Chinese Academy of Sciences; Songshan Lake Materials Laboratory
- **DOI**: [10.48550/arXiv.2508.07035](https://doi.org/10.48550/arXiv.2508.07035)
- **발행일**: 2025-08-09
- **키워드**: VASP, DFT, Multi-Agent System, Model Context Protocol, CrewAI, Laboratory Automation, Computational Materials Science

---

## Essence

VASP(Vienna Ab initio Simulation Package) 기반 밀도범함수이론(DFT) 시뮬레이션을 완전 자동화하는 오픈소스 멀티 에이전트 플랫폼 **VASPilot**을 소개한다. CrewAI 프레임워크와 Model Context Protocol(MCP)을 기반으로 구축되며, Manager Agent + 3개 특화 Worker Agent(Crystal Structure Agent, VASP Agent, Result Validation Agent)가 결정 구조 검색, 입력 파일 생성, Slurm 작업 제출, 오류 파싱 및 파라미터 자동 조정, 결과 시각화까지 전 과정을 수행한다. 2H-MoS2의 밴드 구조/DOS 계산, ENCUT 수렴 테스트, 다양한 van der Waals 보정에 따른 격자 상수 최적화, 전이금속 디칼코게나이드(TMD) 밴드갭 비교 등의 벤치마크에서 수동 개입 없이 성공적으로 완료되었다.

---

## Motivation

DFT 계산은 재료 과학에서 필수적이지만, VASP 워크플로는 입력 파일 준비, 작업 제출, 모니터링, 오류 처리, 후처리 등 상당한 수동 작업을 요구한다. VASPKIT, ASE, Pymatgen 등 기존 도구가 일부 부담을 덜어주지만, 다양한 물질/조건을 비교하는 복잡한 연구 시나리오에서는 여전히 반복적인 스크립트 작성과 작업 관리가 필요하다. LLM 기반 멀티 에이전트 시스템이 이 문제를 해결할 잠재력이 있으나, VASP에 특화된 MAF(Multi-Agent Framework)는 부재했다. 특히 zero-shot 미션(사전 예제 없는 복잡 태스크) 처리와 직관적 사용자 인터페이스가 미해결 과제이다.

---

## Achievement

1. **VASP 전용 멀티 에이전트 자동화 플랫폼**: CrewAI + MCP 기반으로 DFT 워크플로 전체를 자동화하는 최초의 VASP 특화 오픈소스 시스템
2. **자동 오류 복구**: VASP 실행 중 발생하는 오류(예: Bravais lattice 불일치)를 자동으로 파싱하고 파라미터(symprec 등)를 조정하여 재시작
3. **Zero-shot 복합 미션 수행**: 사전 예제 없이도 ENCUT 수렴 테스트, 다중 vdW 보정 비교, 교차 물질 밴드갭 비교 등 복잡한 워크플로 완료
4. **직관적 웹 인터페이스**: Flask 기반 UI로 자연어 미션 제출, 실시간 워크플로 추적, 에이전트/도구 실행 이력 드릴다운, 구조 시각화 제공
5. **오픈소스 공개**: GitHub에서 소스 코드와 문서 공개, MaterialsGalaxy 포털에서 대화형 데모 제공

---

## How

### 아키텍처 (3개 컴포넌트)

#### 1. CrewAI 기반 멀티 에이전트 코어
| 에이전트 | 역할 | 도구 |
|---------|------|------|
| Manager Agent | 미션 분해, 태스크 위임, 결과 종합 | - |
| Crystal Structure Agent | 결정 구조 검색/조작/분석 | search_MP (Materials Project) |
| VASP Agent | VASP 계산 실행/시각화 | vasp_relaxation, vasp_scf, vasp_nscf, wait_calc, python_plot |
| Result Validation Agent | 계산 결과 정확도/신뢰성 검증 | check_file_exist, read_calc_results, check_calc_results |

- 모든 에이전트는 DeepSeek-V3-0324 기반 (교체 가능)
- 각 Worker Agent는 독립적 컨텍스트와 시스템 프롬프트 유지
- RAG(Retrieval-Augmented Generation) 기반 메모리 풀로 이전 태스크 결과 활용

#### 2. MCP(Model Context Protocol) 도구 서버
- **입력 준비 도구**: pymatgen으로 VASP 입력 파일 자동 생성, Slurm 스케줄러에 작업 제출, 고유 calculation ID로 추적
- **상태 조회 도구(check_calc_results)**: 실패 시 VASP 오류 메시지 반환, 성공 시 전체 결과(총 에너지, 밴드갭, 페르미 에너지 등) 추출 및 DB 저장
- **시각화 도구(python_plot)**: calculation ID 기반으로 데이터 검색, 에이전트가 생성한 Python 코드 실행하여 그래프 생성
- MCP 표준 준수로 다른 DFT 코드(Quantum Espresso 등)로의 확장이 MCP 서버 배포만으로 가능

#### 3. Flask 기반 웹 인터페이스
- 자연어로 미션 제출, 실시간 플로우차트로 진행 상황 시각화
- Agent Execution / Tool Execution 로그의 드릴다운 검사
- 결정 구조 파일 및 생성된 그래프의 즉시 미리보기

### 벤치마크 결과
1. **2H-MoS2 밴드 구조/DOS**: Materials Project에서 구조 검색 -> 구조 이완 -> SCF (Bravais lattice 오류 자동 수정) -> NSCF -> 밴드 구조/DOS 플로팅, 모두 자동 완료
2. **ENCUT 수렴 테스트**: 300-500 eV 범위에서 총 에너지 계산 및 수렴 그래프 자동 생성
3. **vdW 보정 비교**: DFT-D2, DFT-D3(제로/BJ 댐핑), Tkatchenko-Scheffler, optB86, optB88, SCAN+rVV10, r2SCAN+rVV10, rVV10, optPBE-vdW 등 10가지 보정법으로 격자 상수 최적화 및 실험값 대비 비교
4. **TMD 밴드갭 비교**: MoS2, MoSe2, WS2, WSe2의 밴드갭 계산 및 비교 바 차트 생성

---

## Originality

1. **VASP 특화 멀티 에이전트 시스템**: 응축물질물리학에서 가장 널리 사용되는 VASP에 특화된 최초의 LLM 기반 자동화 플랫폼
2. **MCP 기반 모듈형 도구 설계**: VASP의 방대한 출력을 LLM이 처리할 수 있도록, 중앙 DB를 통한 calculation ID 기반 경량 인터페이스 설계 -- LLM의 I/O 한계를 우회하는 실용적 해결책
3. **자동 오류 복구 메커니즘**: VASP 오류 메시지를 파싱하여 symprec 등 파라미터를 자동 조정하고 재시작하는 에이전트 수준의 디버깅
4. **Zero-shot 복합 미션**: 태스크별 예제 없이도 다중 조건/물질 비교와 같은 복잡한 연구 시나리오를 자율적으로 완료
5. **코드 확장성**: MCP 서버만 추가하면 Quantum Espresso, CASTEP 등 다른 DFT 코드로 쉽게 확장 가능한 설계

---

## Limitation & Further Study

### 한계
- **벤치마크의 범위**: 검증이 2H-MoS2와 TMD에 국한되어 있으며, 금속, 강상관 전자계, 자성체 등 더 도전적인 시스템에 대한 테스트 부재
- **단일 LLM 의존**: DeepSeek-V3-0324에 대한 평가만 제시 -- 다른 LLM(GPT-4, Claude 등)에서의 성능 비교 없음
- **비용 및 효율성**: LLM API 호출 비용과 수동 워크플로 대비 시간/비용 절감에 대한 정량 분석 부재
- **복잡한 워크플로 한계**: phonon 계산, NEB(nudged elastic band), AIMD(ab initio molecular dynamics) 등 고급 VASP 워크플로에 대한 지원 미확인
- **오류 복구의 범위**: symprec 조정 외에 수렴 실패, 메모리 부족, 잘못된 초기 구조 등 다양한 VASP 오류에 대한 자동 복구 범위 불명확
- **보안**: Slurm 클러스터에 대한 에이전트의 직접 작업 제출이 보안 및 자원 관리 측면에서 우려

### 향후 연구
- 추가 에이전트/도구 통합으로 phonon, 전자수송, 광학 특성 계산 지원 확장
- MCP 서버 추가를 통한 Quantum Espresso, CASTEP 등 다른 DFT 코드 지원
- 다양한 LLM 백엔드에 대한 성능 비교 연구
- 고처리량(high-throughput) 계산 시나리오에서의 확장성 검증
- 연구자 사용성 평가(user study)를 통한 UI/UX 개선

---

## Evaluation

### 강점
- VASP 사용자 커뮤니티의 실질적 고충(반복적 입력 준비, 오류 처리, 작업 관리)을 정확히 타겟팅
- MCP 기반 모듈형 설계가 다른 DFT 코드로의 확장을 구조적으로 보장
- 자동 오류 복구(symprec 조정)가 실제 VASP 워크플로에서 빈번히 발생하는 문제를 해결
- Zero-shot으로 다중 vdW 보정 비교(10가지)를 성공적으로 수행한 것은 에이전트의 일반화 능력을 잘 보여줌
- 오픈소스 공개와 웹 데모 제공으로 재현성과 접근성 확보
- 웹 UI가 에이전트 실행의 투명성을 제공하여 연구자의 검증을 지원

### 약점
- 벤치마크가 비교적 단순한 반도체 시스템에 국한 -- 강상관 전자계, 자성체, 표면/인터페이스 등 실질적으로 도전적인 문제에 대한 검증 필요
- 기존 자동화 도구(AiiDA, FireWorks, atomate 등)와의 체계적 비교 부재 -- LLM 기반 접근의 부가 가치가 명확하지 않음
- LLM의 환각(hallucination) 가능성에 대한 논의 없음 -- 잘못된 INCAR 파라미터 설정이나 부적절한 k-point 선택 등의 위험
- Result Validation Agent의 검증 깊이가 불분명 -- 결과의 물리적 타당성(예: 밴드갭이 합리적 범위인지)을 얼마나 판단할 수 있는지 미기술

### 총평
VASP 워크플로 자동화에 LLM 멀티 에이전트를 적용한 실용적이고 잘 설계된 오픈소스 시스템이다. MCP 기반 모듈형 아키텍처, 자동 오류 복구, zero-shot 복합 미션 처리는 계산 재료 과학 연구자에게 실질적 가치를 제공한다. 특히 웹 UI를 통한 투명한 워크플로 추적이 연구자의 신뢰 구축에 기여한다. 다만, 더 복잡한 물리 시스템과 고급 VASP 기능에 대한 검증, 기존 워크플로 관리 도구와의 비교, LLM 환각에 대한 안전장치 논의가 보완되면 영향력이 크게 높아질 것이다. 응축물질물리학/재료 과학 분야에서 AI for Science의 구체적 실현 사례로서 가치가 높다.
