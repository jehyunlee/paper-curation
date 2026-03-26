# ResearchGym: Evaluating Language Model Agents on Real-World AI Research

> **저자**: Aniketh Garikaparthi, Manasi Patwardhan, Arman Cohan | **날짜**: 2026-02-16 | **arXiv**: 2602.15112 | **분야**: cs.AI

---

## Essence

ResearchGym은 LLM 에이전트가 end-to-end 연구(가설 제안, 실험 설계, 구현, 평가)를 수행할 수 있는지를 객관적으로 평가하는 벤치마크 및 실행 환경이다. ICML, ICLR, ACL의 oral/spotlight 논문 5편에서 핵심 방법론을 제거한 39개 sub-task를 구성하고, GPT-5 기반 에이전트를 평가한 결과 baseline 대비 개선은 15회 중 단 1회(6.7%)에 그쳤으나, 해당 1회에서는 ICML 2025 Spotlight 논문의 SOTA를 초과하는 "capability-reliability gap"을 발견했다.

## Motivation

- **알려진 것**: LLM 기반 자동 연구 시스템들이 다수 제안되었으나, self-reported 사례 중심으로 체계적 비교가 부재
- **Gap**: 기존 벤치마크들은 연구 사이클의 일부만 평가하거나(ideation만, implementation만), 클러스터급 GPU가 필요하거나, LLM judge에 의존하여 gaming에 취약하거나, 오래된 태스크로 contamination 위험이 존재
- **왜 중요한가**: AI 에이전트의 실제 연구 역량을 과대평가하지 않으려면, 최신 논문 기반의 execution-graded, single-GPU 접근 가능한 closed-loop 벤치마크가 필요
- **접근법**: 2025년 수상 논문에서 저자 솔루션을 제거하고 baseline만 남긴 컨테이너화된 환경을 구축하여, 에이전트가 가설 제안부터 실험까지 수행하도록 설계

## Achievement

1. **벤치마크 구성**: 5개 태스크(continual learning, cross-modal retrieval, time series explanation, materials tokenization, RL replay buffer), 39개 sub-task를 contamination-aware하게 구축
2. **Capability-Reliability Gap 발견**: GPT-5 에이전트가 15회 실행 중 1회(6.7%)에서만 baseline을 초과했으나, 해당 단일 실행에서 ICML Spotlight SOTA를 11.5% 초과 (CPD(A)=0.589 vs SOTA=0.463)
3. **Sub-task 완료율**: 평균 26.5%에 불과하며, 성능은 약 9시간 후 plateau -- 추가 자원 투입의 수확체감 확인
4. **Scaffold 비교**: Claude Code (Opus-4.5), Codex (GPT-5.2) 등 proprietary scaffold에서도 동일한 gap 관찰; Codex가 디버깅 능력에서 우세하나 전체 패턴은 유사
5. **7가지 장기 실패 모드 분류**: overconfidence, optimization myopia, 병렬 실험 실패, context-length 한계, reward hacking 등 체계적 분류

## How

- **벤치마크 구축 파이프라인**: 1,387편 수상 논문 → GPT-5 기반 자동 필터링(structured card 추출) → 90편 shortlist → 인간 QA로 5편 최종 선정 + 3편 dev set
- **Task Packaging**: 각 논문의 repository에서 핵심 method 제거, dataset/evaluation script/baseline 보존, Docker 컨테이너화, grade.sh 스크립트 제공
- **에이전트 (rg-agent)**: Inspect 프레임워크 기반 ReAct-style tool-use loop, GPT-5 (reasoning effort 'high'), bash/python/web-search/async-jobs 등 10종 도구 제공
- **평가 메트릭**: Normalized Performance (Agent Score / SOTA Score), Completion Rate, Improvement Rate
- **무결성 검증**: inspection-agent로 post-hoc 감사 -- grading script 변조, 결과 조작, cross-run contamination 탐지
- **Ablation**: 추가 자원(+12h, +$10), information hint(핵심 아이디어 제공), scaffold 변경(Claude Code, Codex), async-jobs
- **제약**: single NVIDIA A100, 12시간/10$ API budget, 웹 검색 2024.10 이전으로 제한, 160개 논문 관련 URL 차단

## Originality

- **Full-loop + Execution-graded 벤치마크**: ideation과 experimentation을 모두 요구하면서 LLM judge가 아닌 논문 원본 evaluation script으로 채점하는 최초의 접근 가능한(single-GPU) 벤치마크
- **Contamination-aware 설계**: 2025년 수상 논문만 사용하여 frontier LLM의 knowledge cutoff 이후 발표된 논문으로 구성
- **Capability-Reliability Gap 개념화**: 에이전트가 간헐적으로 SOTA를 달성할 수 있지만 일관성이 극히 낮다는 현상을 정량적으로 입증
- **장기 실패 모드의 체계적 분류**: 35회 이상 end-to-end 실행의 trajectory(총 1B+ token) 분석을 통해 overconfidence, premature convergence, blind spot 등 7가지 패턴 도출
- **Inspection Agent**: reward hacking 탐지를 위한 post-hoc audit agent 설계 및 검증 (100% true positive)

## Limitation & Further Study

### 저자들이 언급한 한계

- 현재 5개 태스크로 규모가 작으며, multi-modal reasoning(의료 영상, 비디오, 음성) 태스크가 포함되지 않음
- 이론/분석/증명 기반 주관적 연구는 의도적으로 배제 -- 객관적 metric으로 평가 가능한 경험적 ML 태스크에 한정
- Frontier LLM만 non-trivial 성능을 보여 직접 training 실험이 불가능하며, 소형 모델 학습 가능성은 미검증

### 자체판단 아쉬운 점

- 태스크당 3회 반복 실행은 통계적으로 충분하지 않으며, 관찰된 극단적 분산(e.g., CL의 Acc 30.75 +/- 37.39)에 대한 신뢰구간이 넓어 결론의 견고성이 제한적
- Baseline으로 GPT-5와 ReAct scaffold만 주로 사용하여, multi-agent 시스템이나 evolutionary search 등 다른 paradigm에서의 성능 차이를 충분히 탐색하지 못함
- Hint ablation에서 SOTA 아이디어를 주어도 implementation이 주요 병목이라는 결론은 흥미롭지만, hint의 구체성 수준에 따른 sensitivity analysis가 부족
- 웹 검색을 2024.10 이전으로 제한하고 160개 URL을 차단하는 것은 contamination 방지에 효과적이나, 실제 연구자가 최신 문헌을 참조하는 상황과 괴리가 있어 에이전트의 실질적 연구 역량을 과소평가할 가능성 존재

### 후속 연구

- Multi-modal, 대규모 데이터셋 구축 등 messy long-horizon 작업을 포함하는 태스크 확장
- Agent의 idea diversity 향상을 위한 scaffolding 전략 -- 현재 에이전트들이 baseline 코드에 고착되어 유사한 방법만 반복 제안하는 문제 해결
- Long-horizon context 관리 개선 -- 150K token 이후 성능 저하를 완화하는 hierarchical memory 또는 structured note-taking 메커니즘 연구
- Gym-style 환경을 활용한 RL 기반 research agent fine-tuning
- 인간 연구자와의 직접 비교 실험 (동일 시간/자원 조건)

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 4/5 |
| Technical Soundness | 4/5 |
| Significance | 5/5 |
| Clarity | 4/5 |
| Overall | 4/5 |

**총평**: AI 에이전트의 자율 연구 역량을 closed-loop으로 객관 평가하는 최초의 접근 가능한 벤치마크를 제시한 시의적절한 연구이다. "Capability-reliability gap"이라는 핵심 발견 -- 에이전트가 간헐적으로 인간 SOTA를 초과할 수 있으나 극히 비신뢰적이라는 점 -- 은 AI4Science 커뮤니티에서 자동 연구 시스템의 현실적 기대치를 교정하는 데 중요한 기여이다. 특히 7가지 장기 실패 모드의 체계적 분류와 reward hacking 사례 분석은 향후 research agent 설계에 실질적 지침을 제공한다.
