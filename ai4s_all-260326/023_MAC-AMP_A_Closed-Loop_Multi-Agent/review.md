# MAC-AMP: A Closed-Loop Multi-Agent Collaboration System for Multi-Objective Antimicrobial Peptide Design

## 메타 정보
- **저자**: Gen Zhou*, Sugitha Janarthanan*, Lianghong Chen, Pingzhao Hu
- **소속**: Western University (Computer Science, Biochemistry)
- **발표**: ICLR 2026 (Published as a conference paper)
- **arXiv**: 2602.14926
- **날짜**: 2026-02-16
- **키워드**: antimicrobial peptide, multi-agent collaboration, reinforcement learning, multi-objective optimization, LLM

---

## 한줄 요약 (Essence)
LLM 기반 다중 에이전트 피어 리뷰 시스템과 적응형 강화학습을 결합한 폐루프(closed-loop) 프레임워크 MAC-AMP를 제안하여, 항균 활성, 독성, 구조적 안정성, 신규성을 동시에 최적화하는 항균 펩타이드(AMP) 설계를 달성한 연구.

## 연구 동기 (Motivation)
항균제 내성(AMR)은 2021년에만 약 114만 명의 직접 사망을 야기한 글로벌 보건 위기이며, 항균 펩타이드(AMP)는 유망한 대안이지만 독성, 안정성, 제조 가능성 등의 병목이 존재한다. 기존 AI 기반 AMP 설계 모델은 대부분 항균 활성 단일 목표만 최적화하거나, 다목적 최적화 시 정적 가중치/임계값에 의존하여 reward hacking이나 diversity collapse가 발생한다. 또한 기존 멀티 에이전트 시스템은 대부분 개방 루프(open-loop)로 운영되어 자연어 출력을 실행 가능한 학습 신호로 변환하는 메커니즘이 부재하다.

## 주요 성과 (Achievement)
- 5개 박테리아 타겟(E. coli, S. aureus, P. aeruginosa, K. pneumoniae, E. faecium)에 대해 **항균 활성, 독성 감소, 구조적 신뢰성 모두에서 기존 모델(AMP-Designer, BroadAMP-GPT, PepGAN, Diff-AMP) 대비 최고 성능** 달성
  - E. coli: 활성 0.943, 독성 0.154, 구조 신뢰성 0.873
  - 실제 AMP 대비 독성이 현저히 낮음 (0.154 vs 0.558)
- 생성된 AMP의 **높은 신규성**: 기존 AMP 대비 최대 유사도 84.6%, 평균 유사도 ~27%
- **광범위 항균 활성**: E. coli 타겟 AMP의 40%가 5개 ESKAPE 병원체에 대해 광범위 활성 예측
- 외부 MIC 예측기(APEX 1.1) 독립 검증: 90개 AMP 중 85개가 3개 E. coli 균주 모두에 활성
- MD 시뮬레이션으로 구조적 안정성 확인 (RMSD 2-4 A)

## 방법론 (How)
MAC-AMP는 4개 핵심 모듈로 구성된 폐루프 시스템:
1. **Property Prediction Module**: MIC 예측기(ProtBERT fine-tuning), Macrel(AMP likelihood), ToxinPred 3.0(독성), OmegaFold(구조 신뢰성), Foldseek(템플릿 유사도), Biopython(물리화학적 프로파일)
2. **AI-Simulated Peer Review Module**: 3개 독립 Reviewer(GPT-5, Gemini 2.5, Perplexity)가 4개 차원(효율성, 안전성, 구조, 독창성)에서 가중 lexicon 태깅 기반 평가 → Area Chair가 합의 도출 및 divergence penalty 적용
3. **RL Refinement Module**: CS-based Reward Design Agent와 Biomedical Reward Alignment Agent가 협력하여 보상 함수 설계 → sandbox에서 3개 후보 함수 시험 후 Pareto 최적 선택 → 3 stage 적응형 최적화 (exploration → balance → convergence)
4. **Peptide Generation Module**: GPT-2 기반 auto-regressive 생성기 + soft prompt + PPO 학습

## 독창성 (Originality)
- **멀티 에이전트 합의를 실행 가능한 RL 보상 신호로 변환하는 최초의 폐루프 시스템**: 기존 MAC 시스템의 "자연어 출력 → 학습 신호 간극" 문제를 해결
- **AI-Simulated Peer Review**: 학술 피어 리뷰를 모방한 구조화된 다중 에이전트 평가 시스템으로, 태그 기반 정량화와 divergence penalty를 통해 합의의 질을 보장
- **Stage-based Adaptive Optimization**: 보상 함수가 학습 단계에 따라 공진화하여, 단일 정적 보상의 reward hacking 문제를 방지
- **도메인 비의존적 설계**: injectable knowledge 시스템으로 AMP 외 도메인(table-to-text)으로의 전이 가능성 시연

## 한계점 (Limitation)
- **In vitro/in vivo 실험 검증 부재**: 모든 평가가 계산적(in silico) 수준에 머무름. MIC 예측기 자체의 정확도(R^2=0.572)가 높지 않아, 실제 항균 활성과의 괴리 가능성
- **MIC 예측기의 순환 의존성**: MAC-AMP가 자체 학습한 MIC 예측기로 생성물을 평가하므로, 예측기 편향이 증폭될 위험
- **Reviewer 에이전트의 고정된 구성**: GPT-5, Gemini 2.5, Perplexity의 특정 조합에 대한 의존성이 높으며, 모델 업데이트 시 재현성에 영향
- **계산 비용**: 47.61 GPU시간 + $36.56 API 비용으로, 반복 실험이나 대규모 탐색에는 부담
- **Cross-domain 전이 실험이 예비적 수준**: ToTTo 데이터셋의 25%만 사용한 최소한의 평가

## 총평 (Evaluation)
ICLR 2026에 게재된 만큼 학술적 완성도가 높은 논문이다. 멀티 에이전트 합의를 실행 가능한 보상 함수로 변환하는 아키텍처는 AI4Science에서 LLM 에이전트 활용의 새로운 패러다임을 제시한다. 특히 3개 Reviewer 에이전트 각각의 역할 분석(potency driver, safety gatekeeper, structural mediator)과 광범위한 ablation study(Property Prediction, Peer Review, RL 각 모듈)는 시스템 설계의 합리성을 강하게 뒷받침한다. 다만 모든 검증이 in silico에 머물고 있어 실제 신약 개발 파이프라인으로의 translation은 향후 과제이며, MIC 예측기의 자기 참조적 평가 구조는 방법론적 우려 사항이다. 그럼에도 불구하고, 복잡한 다목적 분자 설계 문제에 대한 체계적이고 감사 가능한(auditable) 접근법으로서 높은 가치를 지닌다.
