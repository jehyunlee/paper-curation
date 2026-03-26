# Revisiting Gene Ontology Knowledge Discovery with Hierarchical Feature Selection and Virtual Study Group of AI Agents

> **저자**: Cen Wan, Alex A. Freitas | **날짜**: 2026-03-20 | **arXiv**: 2603.20132

---

## Essence

Hierarchical feature selection으로 선별된 노화 관련 Gene Ontology(GO) term들을 LLM 기반 multi-agent "Virtual Study Group(VSG)"이 자동으로 생물학적 해석하는 agentic AI 프레임워크를 제안한 연구이다. 4개 모델 생물(예쁜꼬마선충, 초파리, 마우스, 효모)의 노화 관련 GO term에 대해 junior researcher, critic, senior researcher, principal investigator 역할의 AI agent들이 계층적으로 지식을 생성하고 비판적 검토를 수행한다. 대부분의 AI 생성 주장이 기존 문헌으로 검증 가능함을 보였다.

## Motivation

- **알려진 것**: Hierarchical feature selection(HIP, MR 등)이 GO term의 계층 구조를 활용하여 노화 관련 유전자의 가장 informative한 GO term을 선별할 수 있음. LLM은 지식 추출에서 잠재력을 보이나 hallucination 문제가 존재
- **Gap**: 기존 GO term 기반 생물학적 해석은 수동으로 이루어져 시간과 전문성이 많이 소요되며, 단일 LLM 기반 해석은 hallucination과 해석 가능성 부족 문제가 있음. GO 계층에서 독립적인 specific term 간의 연관성 발견이 특히 어려움
- **왜 중요한가**: 노화 생물학은 극도로 복잡한 메커니즘을 다루며, GO term 간 숨겨진 연관성을 자동으로 발견하면 새로운 노화 관련 가설 생성 가능
- **접근법**: 학술 연구 그룹의 계층적 토론 구조를 모방한 multi-agent 시스템으로, 비판적 리뷰 메커니즘을 통해 LLM hallucination을 완화

## Achievement

1. **문헌 검증 가능한 주장 생성**: 4개 모델 생물 모두에서 Virtual Junior Researcher A의 과학적 주장 대부분이 기존 연구 논문으로 검증 가능 (green-highlighted claims)
2. **비판적 리뷰 메커니즘 작동**: Virtual Junior Researcher B가 Researcher A의 과잉 일반화(oversimplification)를 효과적으로 지적하며, 조직 특이적 메커니즘 등 누락된 nuance를 보완
3. **계층적 종합**: Senior Researcher가 두 junior의 의견을 종합하고, Principal Investigator가 종간(cross-species) 패턴과 미래 연구 방향을 도출
4. **Hallucination 탐지**: 효모 연구에서 Hog1 deletion mutant에 대한 잘못된 주장 등 일부 hallucination을 식별하여 보고

## How

- **입력 데이터**: Wan & Freitas (2018)의 HIP hierarchical feature selection으로 선별된 GO term 테이블 (4개 모델 생물: C. elegans, D. melanogaster, M. musculus, S. cerevisiae, 각 2개 top-ranked GO term)
- **Agent 구조 (Virtual Study Group)**: 3계층 bottom-up 구조
  - Layer 1: Virtual Junior Researcher A (deepseek-r1) - GO term과 노화의 연관성 조사 + Virtual Junior Researcher B (qwen3-vl) - 비판적 리뷰
  - Layer 2: Virtual Senior Researcher (gpt-oss) - 두 junior의 보고서 종합
  - Layer 3: Virtual Principal Investigator (glm-4.7-flash) - 4개 모델 생물 종합 보고서 작성
- **구현**: CrewAI 프레임워크 + Ollama로 4종의 오픈소스 LLM 활용
- **검증**: 각 AI agent 출력의 과학적 주장을 수동 문헌 검토로 green(지지됨)/yellow(미지지) 표시

## Originality

- **학술 연구그룹 메타포**: 실제 연구실의 계층적 토론 구조(PhD 학생 → 포닥 → 교수)를 AI agent 시스템에 적용한 점이 직관적이며, 비판적 리뷰 메커니즘이 hallucination 완화에 기여
- **Feature Selection + Agentic AI 결합**: 기존 hierarchical feature selection 결과를 LLM agent의 입력으로 활용하여, 데이터 기반 feature 선별과 지식 기반 해석을 연결하는 파이프라인
- **다중 LLM 활용**: 서로 다른 역할에 서로 다른 LLM(deepseek-r1, qwen3-vl, gpt-oss, glm-4.7-flash)을 배정하여 모델 다양성을 확보

## Limitation & Further Study

### 저자들이 언급한 한계

- Hallucination 문제가 완전히 해결되지 않음 (효모 Hog1 관련 잘못된 주장, 마우스 연구의 존재하지 않는 인용)
- 일반적(generic) 정의의 GO term만 테스트했으며, 더 specific한 GO term에 대한 능력은 미검증
- Specific GO term의 경우 검증할 기존 문헌 자체가 부족할 수 있음

### 자체판단 아쉬운 점

- **정량적 평가 부재**: 과학적 주장의 정확도를 green/yellow 하이라이팅으로만 제시하고, precision/recall 등 체계적 정량 지표가 없음. "대부분 검증 가능"이라는 주관적 평가에 의존
- **Agent 역할 배정의 임의성**: 4개 LLM을 각 역할에 배정한 근거가 불명확. LLM 선택이 결과에 미치는 영향에 대한 ablation study가 없음
- **비판적 리뷰의 편향**: Virtual Junior Researcher B가 항상 비판적 입장만 취하고, Senior Researcher가 거의 항상 B의 의견에 동조하는 패턴이 반복되어, 실제 학술 토론의 다양성을 반영하지 못함
- **새로운 지식 발견 없음**: 모든 검증이 "기존 문헌으로 확인 가능"한 수준에 머물러, AI가 진정으로 새로운 생물학적 통찰을 제시했는지 불분명. 기존 지식의 재서술에 가까움
- **확장성 미검증**: GO term 2개씩만 테스트하여, 다수의 GO term을 동시에 고려하는 복잡한 시나리오에서의 성능이 불명
- **재현성 우려**: LLM 출력의 비결정적 특성상, 동일 입력에 대해 다른 결과가 나올 수 있으나 이에 대한 논의가 없음

### 후속 연구

- 더 specific한 GO term으로 확장하여 미지의 노화 관련 지식 발견 가능성 탐색
- LLM agent의 도구 사용(문헌 검색, 데이터베이스 쿼리) 능력 통합
- 정량적 평가 체계 구축 및 다양한 LLM 조합의 체계적 비교

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 2/5 |
| Technical Soundness | 2/5 |
| Significance | 2/5 |
| Clarity | 3/5 |
| Overall | 2/5 |

**총평**: 학술 연구그룹의 계층적 토론 구조를 AI agent 시스템에 적용한다는 아이디어는 직관적이나, 실행과 평가 측면에서 크게 부족하다. 정량적 평가 지표가 전무하고, AI가 생성한 지식이 기존 문헌의 재서술을 넘어서는 새로운 발견인지 불분명하며, LLM 선택의 근거와 재현성에 대한 논의가 없다. 비판적 리뷰 agent가 항상 동일한 패턴(oversimplifies/overstates 비판)을 보이고 senior가 거의 항상 동조하는 것은 실제 과학적 토론의 복잡성을 충분히 모사하지 못한다. Proof-of-concept 수준의 탐색적 연구로서의 가치는 있으나, 기술적 엄밀성과 실용적 기여 측면에서 개선이 필요하다.
