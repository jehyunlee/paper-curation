# Autonomous Agents for Scientific Discovery: Orchestrating Scientists, Language, Code, and Physics

> **저자**: Lianhao Zhou, Hongyi Ling, Cong Fu, Yepeng Huang, Michael Sun, Wendi Yu, Xiaoxuan Wang, Xiner Li, Xingyu Su, Junkai Zhang, Xiusi Chen, Chenxing Liang, Xiaofeng Qian, Heng Ji, Wei Wang, Marinka Zitnik, Shuiwang Ji | **날짜**: 2025-10-10 | **Repository**: arXiv | **arXiv ID**: 2510.09901

---

## Essence

LLM 기반 과학적 에이전트의 역할과 발전을 체계적으로 조망하는 서베이 논문이다. 과학적 발견의 전 주기를 가설 발견(Hypothesis Discovery), 실험 설계 및 실행(Experimental Design & Execution), 결과 분석 및 정제(Result Analysis & Refinement)의 3단계로 구조화하고, 각 단계에서 LLM 에이전트가 인간 과학자, 자연어, 컴퓨터 언어, 물리 정보를 어떻게 오케스트레이션하는지를 정보 이론적 프레임워크를 통해 분석한다. 생명과학, 화학, 재료과학, 물리학 등 7개 도메인에 걸친 100여 개 이상의 과학 에이전트 시스템을 포괄적으로 분류한다.

## Motivation

과학적 발견은 전통적으로 인간의 직관과 반복적 실험에 의존해 왔으나, 데이터의 복잡성과 규모가 급증하면서 인간 주도 방식의 한계(높은 비용, 인지적 편향, 방대한 가설 공간 탐색의 어려움)가 부각되고 있다. LLM의 추론, 계획, 멀티모달 처리 능력이 비약적으로 발전하면서, 이를 과학적 발견에 활용하는 에이전트 연구가 폭발적으로 증가했다. 그러나 기존 서베이들은 범용 LLM 에이전트에 초점을 맞추거나, 과학적 에이전트를 다루더라도 단편적인 분류에 머물러, 과학적 발견 프로세스의 각 단계에서 정보가 어떻게 변환되는지에 대한 통합적 분석 프레임워크가 부재했다.

## Achievement

1. **정보 이론적 프레임워크 제안**: Information Entropy, Verifiability, Dissipation의 세 가지 정보 속성을 기반으로, 과학적 발견의 각 단계에서 Human Intent → Natural Language → Computer Language → Physical Information으로의 정보 변환 과정을 체계적으로 분석. 각 단계의 자동화 난이도를 엔트로피/소산 수준으로 정량화
2. **5단계 자율성 프레임워크**: Human-Led Model(Level 1)에서 Full AI Autonomy(Level 5)까지 과학 에이전트의 자율성을 5단계로 분류하는 체계 제시. 기존 역할 기반 분류보다 정보 처리 능력에 근거한 세밀한 구분
3. **포괄적 방법론 분류**: 가설 발견(Knowledge Extraction, Hypothesis Generation, Screening/Validation), 실험 설계/실행(Tool Use 4가지 전략, Tool Creation), 결과 분석/정제(3가지 패러다임, 3가지 검증 전략)의 전체 파이프라인에 걸친 방법론 분류 체계(taxonomy)
4. **도메인별 에이전트 카탈로그**: Genomics, Protein, Medicine, Chemistry, Materials, Physics 등 7개 분야에 걸친 100+ 에이전트 시스템의 상세 리뷰 및 성과 정리
5. **핵심 논의**: LLM에서 에이전트로의 도약 필요성("Humanity's Knowledge Closure" 개념), Agentic RL의 과학 적용 시 4가지 핵심 문제(Environment, Action, Observation, Reward), 세렌디피티의 역할

## How

- **분석 프레임워크**: 정보 이론(Shannon entropy)과 열역학 제2법칙, Landauer 원리를 결합하여, 과학적 발견을 개방 시스템에서의 비가역적 엔트로피 감소 과정으로 모델링
- **분류 방법론**: 과학적 발견 3단계 x 정보 유형 4가지의 매트릭스를 구성하고, 각 셀의 엔트로피 수준과 전체 소산 정도를 히트맵 및 레이더 차트로 시각화
- **문헌 조사**: 260+ 과학 LLM을 다룬 기존 서베이들과 최신 에이전트 시스템 논문들을 체계적으로 수집하여, 방법론별/도메인별 분류표 작성
- **비교 분석**: Scientific Agent vs General LLM Agent의 6가지 차원(목적, 지식 기반, 추론, 도구 사용, 메모리, 평가 메트릭) 비교

## Originality

- **정보 이론에 기반한 과학적 발견 분석**이 이 논문의 가장 차별화된 기여. 기존 서베이들이 역할 기반 또는 태스크 기반 분류에 머문 반면, 엔트로피-검증가능성-소산의 삼중 렌즈를 통해 각 단계의 자동화 난이도를 정량적으로 분석한 최초의 시도
- **Tool Creation을 독립적인 핵심 단계로 부각**: 기존 문헌에서 Tool Use에 부수적으로 다뤄지던 Tool Creation을 "가장 높은 엔트로피와 소산을 가진 최난이도 단계"로 명시적으로 격상
- **LLM의 Knowledge Closure 개념**: LLM이 기존 인류 지식 내부에서만 추론할 수 있는 본질적 한계를, 에이전트의 물리적 세계와의 상호작용을 통해 극복해야 한다는 명확한 논증

## Limitation & Further Study

### 저자들이 언급한 한계
- Agentic RL을 과학적 발견에 적용할 때의 4대 난제: 이질적 환경(Environment), 무한한 행동 공간(Action), 멀티모달 관찰(Observation), 희소하고 모호한 보상(Reward)
- LLM의 likelihood 최적화 학습 특성이 세렌디피티(우연한 발견)를 구조적으로 방해
- 물리적 법칙에 대한 깊은 이해, 물리적 도구와의 강건한 통합, 실험 환경과의 정교한 상호작용 메커니즘이 아직 미성숙

### 리뷰어 판단 아쉬운 점
- 정보 이론적 프레임워크가 **개념적 수준에 머물러 정량적 검증이 부재**. "Very High / High / Medium / Low" 수준의 정성적 분류이며, 실제 엔트로피 값을 계산하거나 실증적으로 측정한 결과가 없음
- 5단계 자율성 프레임워크 역시 **경험적 근거 없이 제안된 개념적 모델**. 실제 에이전트 시스템을 이 프레임워크에 매핑하여 검증하는 사례 연구가 없음
- 도메인별 에이전트 리뷰가 매우 포괄적이나, **비판적 비교 분석이 부족**. 각 시스템의 성과를 나열하는 데 치중하여, 동일 도메인 내 에이전트 간의 체계적 벤치마크 비교가 거의 없음
- **재현성 및 실패 사례에 대한 논의가 제한적**. 성공 사례 위주로 기술되어, 각 에이전트의 실패 모드나 한계점에 대한 비판적 분석이 부족
- Tool Creation 관련 논문이 상대적으로 소수(AlphaEvolve, CodePDE 등 5-6편)로, 이 단계에 대한 분석의 깊이가 다른 단계에 비해 얕음

### 후속 연구
- 정보 이론적 프레임워크의 정량적 검증을 위한 실증 연구
- 과학적 발견을 위한 Agentic RL의 보상 함수 설계(novelty, impact, reproducibility 측정)
- 물리적 실험 장비와의 안전하고 강건한 인터페이스 설계
- 세렌디피티를 촉진하는 확률적 탐색 전략의 에이전트 통합
- 표준화된 과학 에이전트 벤치마크 개발

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 4/5 |
| Technical Soundness | 3/5 |
| Significance | 4/5 |
| Clarity | 4/5 |
| Overall | 4/5 |

**총평**: 과학적 발견을 위한 LLM 기반 에이전트를 정보 이론적 관점에서 체계적으로 조망한 포괄적 서베이로, 특히 엔트로피-검증가능성-소산 프레임워크와 5단계 자율성 모델은 이 분야의 사고 틀에 기여하는 독창적 제안이다. 다만 이론적 프레임워크가 정성적 수준에 머물고 실증적 검증이 부재하며, 도메인별 에이전트 리뷰가 비판적 비교보다는 성과 나열에 치우친 점이 아쉽다.
