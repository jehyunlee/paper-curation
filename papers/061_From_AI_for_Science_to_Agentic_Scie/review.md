# From AI for Science to Agentic Science: A Survey on Autonomous Scientific Discovery

- **저자**: Jiaqi Wei, Yuejin Yang, Xiang Zhang, Yuhan Chen, Xiang Zhuang, Zhangyang Gao, Dongzhan Zhou 외 다수
- **소속**: Shanghai Artificial Intelligence Laboratory, Zhejiang University, Fudan University, University of British Columbia 외
- **출판**: arXiv:2508.14111 (2025.10.20, v2)
- **DOI**: [10.48550/arXiv.2508.14111](https://doi.org/10.48550/arXiv.2508.14111)

---

## Essence (본질)

"AI for Science"에서 "Agentic Science"로의 전환을 체계적으로 정리한 포괄적 서베이 논문이다. AI 시스템이 단순 계산 도구(Computational Oracle)에서 자율적 연구 파트너(Autonomous Scientific Partner)로 진화하는 과정을 4단계 프레임워크로 정의하고, 생명과학·화학·재료과학·물리학 4개 도메인에서의 자율적 과학 발견(Autonomous Scientific Discovery) 사례를 종합적으로 리뷰한다. 기존 서베이들이 프로세스·자율성·메커니즘 관점을 개별적으로 다루었던 것과 달리, 이 세 관점을 통합하는 프레임워크를 제시한 것이 핵심 차별점이다.

## Motivation (동기)

LLM과 멀티모달 시스템의 급속한 발전으로 AI가 가설 생성, 실험 설계, 실행, 분석, 반복적 개선까지 수행할 수 있게 되었으나, 이러한 "Agentic Science" 패러다임을 체계적으로 이해하고 설계하기 위한 통합 프레임워크가 부재했다. 기존 서베이들은 워크플로우, 자율성 수준, 또는 아키텍처를 각각 독립적으로 다루어 파편화된 시각만 제공하고 있었다.

## Achievement (성과)

1. **4단계 진화 모델 정립**: AI의 역할을 (1) Computational Oracle, (2) Automated Research Assistant, (3) Autonomous Scientific Partner, (4) Generative Architect의 4단계로 구분하고, 각 단계의 형식적 정의를 제시
2. **5대 핵심 역량 분류**: 과학 에이전트의 기반 역량을 (i) 추론과 계획, (ii) 도구 통합, (iii) 메모리 메커니즘, (iv) 다중 에이전트 협업, (v) 최적화와 진화로 체계화
3. **4단계 발견 워크플로우**: 관찰·가설 생성 → 실험 계획·실행 → 데이터·결과 분석 → 합성·검증·진화의 동적 워크플로우 모델링
4. **4대 도메인 심층 리뷰**: 생명과학, 화학, 재료과학, 물리학 각각에서의 에이전트 시스템을 12개 이상의 세부 분야에 걸쳐 체계적으로 분류 및 리뷰
5. **"Nobel-Turing Test" 개념 제안**: 자율 에이전트가 노벨상급 발견을 달성할 수 있는가를 평가하는 벤치마크 개념을 제시

## How (방법론)

- **통합 프레임워크 설계**: 프로세스 지향(process-oriented), 자율성 지향(autonomy-oriented), 메커니즘 지향(mechanism-oriented)의 세 가지 기존 관점을 기반 역량(Foundational Capabilities) → 핵심 프로세스(Core Processes) → 도메인별 실현(Domain Realizations)의 계층 구조로 통합
- **체계적 분류 체계(Taxonomy)**: 각 핵심 역량에 대해 구조화된 분류표(Table 1-5)를 제시하여, 추론 구조(linear/non-linear/search), 적응 메커니즘(self-reflection/RL-augmented), 도구 유형(기초/도메인 특화/실험 플랫폼), 메모리 유형(작업 실행용/지식 허브), 협업 전략(계층적/숙의적/동적 적응형)을 분류
- **도메인별 사례 매핑**: 각 도메인에서 대표적 에이전트 시스템(Coscientist, Robin, ChemCrow, The AI Scientist, AlphaEvolve 등)을 워크플로우 단계별, 자율성 수준별로 매핑하여 종합 비교표 제시

## Originality (독창성)

- 기존 서베이가 단일 관점(프로세스 OR 자율성 OR 메커니즘)에 머물렀던 것을 **세 관점의 통합 프레임워크**로 발전시킨 것이 가장 큰 독창성
- Level 4 "Generative Architect"와 "Nobel-Turing Test" 등 미래 지향적 개념을 제시하여 연구 커뮤니티에 방향성 제공
- 단순 기술 리뷰를 넘어 **인간 과학자의 역할 변화**(실행자 → 전략가)를 함께 논의한 점이 차별적

## Limitation & Further Study (한계 및 향후 연구)

- **서베이 범위의 한계**: 84페이지의 방대한 분량에도 불구하고, 사회과학·공학 등 자연과학 외 분야의 에이전트 시스템은 다루지 않음
- **정량적 벤치마크 부재**: 에이전트 시스템 간의 정량적 성능 비교가 어렵고, 논문에서도 통일된 벤치마크 결과를 제시하지 못함. 현존하는 벤치마크(DiscoveryWorld, ScienceAgentBench 등)의 한계를 언급하지만 대안은 제시하지 않음
- **재현성 문제**: Agentic Science의 핵심 과제로 재현성(reproducibility)을 꼽으면서도, 에이전트 상태 로깅, 결정 정책, 환경 조건 기록 등의 표준화는 아직 미해결
- **검증 딜레마(Validation Dilemma)**: AI가 생성한 가설이 진정한 혁신인지 정교한 보간(interpolation)인지 구분하는 방법론이 아직 확립되지 않음
- **윤리적 거버넌스**: 이중 용도(dual-use) 위험, 책임 소재, 과학 노동 구조 변화 등의 윤리적 문제를 지적하지만, 구체적 해결 메커니즘은 향후 과제로 남김
- **향후 연구 방향**: 자율적 발명(Autonomous Invention), 학제간 대규모 합성(Interdisciplinary Synthesis at Scale), 글로벌 협력 연구 에이전트(Global Cooperation Research Agent) 생태계 구축

## Evaluation (총평)

AI for Science에서 Agentic Science로의 패러다임 전환을 가장 포괄적으로 정리한 서베이로, 이 분야에 진입하거나 전체 그림을 파악하려는 연구자에게 필수적인 참고 자료이다. 통합 프레임워크의 구조적 명확성과 4개 도메인에 걸친 폭넓은 커버리지가 강점이다. 다만, 서베이의 본질적 한계로서 각 시스템에 대한 깊이 있는 기술적 분석보다는 분류와 매핑에 초점을 두고 있어, 개별 시스템의 실제 성능이나 작동 방식에 대해서는 원 논문을 참조해야 한다. "Nobel-Turing Test"와 같은 도발적 제안은 연구 커뮤니티의 장기적 비전 설정에 기여하나, 단기적으로 실현 가능한 로드맵은 부족하다. 전체적으로, Agentic Science라는 신생 분야의 **지형도(landscape map)**로서 높은 완성도를 보여주는 논문이다.

## 평가
| 항목 | 점수 (1-5) |
|------|-----------|
| Novelty | 3 |
| Technical Soundness | 3 |
| Significance | 4 |
| Overall | 3.3 |

**총평**: AI4Science에서 Agentic Science로의 패러다임 전환을 체계적으로 정리한 포괄적 서베이로 분야 전체를 조망하는 중요한 참고 문헌이다.
