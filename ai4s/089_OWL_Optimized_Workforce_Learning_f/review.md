# OWL: Optimized Workforce Learning for General Multi-Agent Assistance in Real-World Task Automation

- **저자**: Mengkang Hu, Yuhang Zhou, Wendong Fan, Yuzhou Nie, Bowei Xia, Tao Sun, Ziyu Ye, Zhaoxuan Jin, Yingru Li, Qiguang Chen, Zeyu Zhang, Yifeng Wang, Qianshuo Ye, Bernard Ghanem, Ping Luo, Guohao Li
- **소속**: The University of Hong Kong, CAMEL-AI.org, Eigent.AI, UCSB, KAUST 등
- **출판**: arXiv preprint (2025.06)
- **DOI**: [10.48550/arXiv.2505.23885](https://doi.org/10.48550/arXiv.2505.23885)

---

## Essence (본질)

LLM 기반 멀티 에이전트 시스템의 **도메인 간 전이성(cross-domain transferability)** 문제를 해결하기 위한 계층적 멀티 에이전트 프레임워크 WORKFORCE와, 도메인 비종속적(domain-agnostic) Planner를 강화학습으로 최적화하는 학습 패러다임 OWL(Optimized Workforce Learning)을 제안한다. 핵심 설계 원칙은 "안정적인 코어(Planner), 교체 가능한 주변부(Worker Nodes)"로, 새로운 도메인에 적응할 때 Worker만 교체하면 되도록 전략적 계획과 도메인별 실행을 분리한 것이다.

---

## Motivation (동기)

1. **기존 MAS의 도메인 종속성**: MetaGPT는 소프트웨어 엔지니어링 SOP에 의존하여 다른 분야로 확장이 어렵고, MALT는 모든 에이전트를 별도로 학습해야 하는 등, 기존 시스템은 새로운 도메인 적용 시 전체 재설계 및 재학습이 필요했다.
2. **추론(Inference)과 학습(Training) 양쪽의 전이성 부족**: 추론 시에는 아키텍처 재설계가, 학습 시에는 전체 에이전트 앙상블의 재학습이 요구되어 유연성이 크게 제한되었다.
3. **오픈소스와 상용 시스템 간의 성능 격차**: OpenAI Deep Research 등 상용 시스템 대비 오픈소스 프레임워크의 성능이 크게 뒤처져 있었다.

---

## Achievement (성과)

- **GAIA 벤치마크 SOTA**: WORKFORCE가 오픈소스 최고 성능 69.70%를 달성하며, OpenAI Deep Research(67.36%)를 2.34% 상회하는 최초의 오픈소스 시스템이 되었다.
- **OWL 학습 효과**: Qwen2.5-32B-Instruct를 OWL로 학습한 결과, 36.36% -> 52.73% (+16.37%)로 대폭 향상되어 GPT-4o-mini(47.27%)와 Qwen2.5-72B(49.09%)를 능가했다.
- **Planner 학습의 효율성**: Planner만 학습해도(45.45%) Planner+Worker 동시 학습(46.68%)과 거의 동등한 성능을 보여, "Planner 최적화가 핵심"이라는 설계 가설을 검증했다.
- **Test-time Scaling**: Replanning 메커니즘을 통해 반복 횟수 증가에 따라 성능이 지속적으로 향상됨을 확인했다.

---

## How (방법론)

### 1. WORKFORCE 아키텍처 (추론 프레임워크)

| 구성 요소 | 역할 |
|----------|------|
| **Planner** | 도메인 비종속적 과제 분해 (task decomposition) |
| **Coordinator** | Worker 할당 및 하위 과제 관리, 중간 결과 통합 |
| **Worker Nodes** | 도메인별 전문 에이전트 (Web Agent, Document Agent, Reasoning/Coding Agent) |

- **통신 메커니즘**: 공유 Task Channel을 통한 중앙집중식 통신. Worker는 최종 결과만 채널에 게시하고, 도구 호출의 상세 컨텍스트는 각 하위 과제 범위 내에서 격리됨.
- **Replanning 메커니즘**: Worker가 실패를 자체 감지하면 Task Channel에 실패 정보를 게시하고, Planner가 피드백 기반으로 새로운 하위 과제를 생성.

### 2. OWL 학습 전략

**2단계 학습:**
1. **SFT (Supervised Fine-Tuning)**: GPT-4o-mini로 생성한 전문가 궤적(trajectory)에서 Planner 초기화. 3,466개 궤적 중 품질 필터링으로 1,599개 사용.
2. **DPO (Direct Preference Optimization)**: SFT 모델에서 각 질문당 4개 궤적을 rollout하여 정답/오답 쌍을 구성. 1,009개 선호 쌍으로 강화학습.

**Task Curriculum (4개 데이터셋):**
- HotpotQA: 다중 홉 추론 + 웹 브라우징
- WikiTableQuestions: 표 데이터 처리
- Math-related: 논리적 추론 + 코딩
- Infinity-MM: 멀티모달 처리

### 3. 주요 실험 결과

| 모델/시스템 | GAIA 평균 정확도 |
|------------|---------------|
| Single Agent (GPT-4o) | 37.58% |
| Role Playing (GPT-4o) | 54.55% |
| WORKFORCE (GPT-4o) | 60.61% |
| WORKFORCE (Claude-3.7-Sonnet) | **69.70%** |
| OpenAI Deep Research (O3) | 67.36% |
| OWL-trained Qwen2.5-32B | 52.73% |

---

## Originality (독창성)

1. **"안정적 코어, 교체 가능한 주변부" 설계**: 전략적 계획(Planner)과 도메인별 실행(Worker)의 명시적 분리를 통해, 추론과 학습 양쪽에서 도메인 전이성을 확보한 최초의 체계적 접근이다.
2. **Planner만 학습하는 효율적 패러다임**: 전체 에이전트 앙상블을 학습하는 기존 방식(MALT 등)과 달리, Planner만 최적화해도 충분하다는 것을 실증적으로 증명했다. Worker만 학습하면 오히려 성능이 하락한다는 반직관적 발견도 포함.
3. **멀티 에이전트 시스템의 Test-time Scaling**: Replanning을 통한 test-time compute scaling이 멀티 에이전트 시스템에서도 유효함을 보여주었다.
4. **체계적 오류 분석**: 실패 사례를 6개 대분류(Planner Error 21%, Worker Error 10%, Limited Tool 33%, Responding Error 8%, Ambiguity 10%, Model Limitation 19%)로 분류하여, 향후 개선 방향을 구체적으로 제시했다.

---

## Limitation & Further Study (한계 및 향후 연구)

### 한계
1. **도구 품질 의존성**: 고품질 도메인별 도구가 없는 영역에서는 실행 병목이 발생할 수 있다. 실제로 전체 오류의 32.69%가 도구 한계에서 기인했다.
2. **강화학습의 시간 비용**: 실제 환경(웹 검색 지연 등)에서의 RL 피드백 수집이 시간 소모적이다.
3. **GAIA 벤치마크 한정 평가**: 다른 멀티 에이전트 벤치마크나 실제 산업 응용에서의 검증이 부족하다.
4. **Level 3 과제의 상대적 약점**: 가장 어려운 Level 3에서는 Deep Research(58.03%)에 비해 WORKFORCE(42.31%)가 여전히 크게 뒤처진다.
5. **데이터 오염(Data Pollution) 가능성**: 에이전트가 HuggingFace 등에서 직접 정답을 가져올 수 있는 위험이 있어, URL 필터링 등의 대책이 필요하다.

### 향후 연구 방향
- Level 3 수준의 복잡한 과제 해결을 위한 Planner의 심층 추론 능력 강화
- 다양한 도메인 벤치마크에서의 WORKFORCE 검증
- Worker 자동 생성 및 도구 자동 구성 메커니즘
- 안전성 및 위험 행동 방지를 위한 에이전트 거버넌스 프레임워크

---

## Evaluation (총평)

OWL/WORKFORCE는 멀티 에이전트 시스템의 실용적 설계 원칙을 제시한 중요한 연구다. 특히 "Planner만 학습하면 된다"는 핵심 통찰은 멀티 에이전트 학습의 효율성을 크게 높이며, Worker만 학습하면 오히려 성능이 하락한다는 발견은 "효과적인 과제 분해가 개별 실행 능력보다 중요하다"는 시사점을 제공한다. 오픈소스 시스템으로서 OpenAI Deep Research를 넘어선 것은 의미 있는 성과이나, Level 3 과제에서의 약점과 도구 의존성은 여전히 해결해야 할 과제다. CAMEL-AI 기반의 완전 오픈소스 공개는 커뮤니티 기여를 촉진할 수 있는 긍정적 요소다. 향후 AI for Science 영역에서 WORKFORCE를 과학적 도구(시뮬레이션, 실험 자동화 등)와 결합하면 흥미로운 확장이 가능할 것이다.
