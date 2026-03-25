# The Empowerment of Science of Science by Large Language Models: New Tools and Methods

> **저자**: Guoqiang Liang, Jingqian Gong, Mengxuan Li, Gege Lin, Shuo Zhang | **날짜**: 2025-11-19 | **Journal**: arXiv preprint | **DOI**: 10.48550/arXiv.2511.15370

---

## Essence

LLM의 핵심 기술(prompt engineering, RAG, fine-tuning, pre-training, tool learning)을 사용자 관점에서 체계적으로 정리하고, Science of Science(SciSci) 분야의 역사적 발전을 추적한 뒤, LLM이 SciSci에 적용될 수 있는 세 가지 방향 -- 과학적 인식(entity/relationship extraction을 통한 지식 그래프 구축), 과학적 평가(AI agent 기반), 과학적 예측(LLM 기반 multilayer network를 통한 research front 탐지) -- 을 제시하는 종합 리뷰 논문이다.

## Motivation

LLM이 NLP, 이미지 인식, 멀티모달 태스크에서 뛰어난 성능을 보이며 AGI로의 경로를 열고 있지만, SciSci(계량서지학/과학학) 분야에서의 활용 가능성은 체계적으로 탐구되지 않았다. SciSci는 전통적으로 인용 분석, 단어 빈도 분석, 통계 분석에 의존해 왔으나, BERT, GCN, 지식 그래프 등의 도입으로 방법론이 확장되고 있다. LLM의 비구조화 텍스트 처리 능력이 이 분야에 새로운 도구와 방법을 제공할 잠재력이 있다.

## Achievement

1. **LLM 기술 체계화**: 사용자 관점에서 prompt engineering → RAG(Naive/Advanced/Modular) → fine-tuning → pre-training → tool learning의 5단계 기술을 복잡도 순으로 정리. GPT 시리즈의 아키텍처 진화(GPT-1~GPT-4)를 파라미터/레이어/데이터 규모로 정량 비교
2. **SciSci 역사 추적**: 1960년대 SCI 도입부터 cumulative advantage, Matthew effect, invisible colleges를 거쳐, 복잡계 과학자/물리학자의 진입으로 GNN, multilayer network, hypergraph 방법론이 도입된 최근까지 개관
3. **Scientific perception**: LLM 기반 entity-relationship extraction 데모를 Kimi LLM + networkX로 구현. 전통적 co-word analysis 대비 의미 차원 정보가 풍부한 네트워크 구축 가능성 제시
4. **Scientific evaluation**: AI agent(= LLM + memory + function calling + tool usage) 기반 과학 평가 모델 제안. ChatGLM 기반 "transformative research evaluation AI agent"와 Dify 플랫폼 기반 설계 시연
5. **Scientific forecasting**: 5개 주요 LLM(GPT-4o, DeepSeek-V3 등) 비교 후, DeepSeek-V3로 Subject-Action-Object 구조 추출 및 PyMnet 기반 multilayer network를 통한 research front 예측 방법 제안

## How

- **방법론**: 종합 리뷰 + 간단한 데모/proof-of-concept 시연
- **Entity extraction demo**: Kimi LLM API를 호출하여 비구조화 텍스트에서 entity triplet 추출, networkX로 시각화 (코드 GitHub 공개)
- **LLM 비교**: GPT-4o, DeepSeek-V3, Gemini-Pro-1.5, Moonshoot-V1-8k, QwQ-32B-Preview를 input/output 비용, topic relevance, 처리 속도, context length 기준으로 비교
- **Research front 탐지**: DeepSeek-V3로 논문에서 Subject-Action-Object 구조 추출 → PyMnet toolkit으로 multilayer network 구축 → 시각화

## Originality

- SciSci 분야 연구자를 대상으로 LLM 기술을 접근성 높게 정리한 교육적 가치가 있는 리뷰
- AI agent 기반 과학 평가라는 새로운 방향을 제안하고 초기 프로토타입을 시연
- LLM 기반 multilayer network를 통한 research front 탐지라는 구체적 방법론 제안

## Limitation & Further Study

### 저자들이 언급한 한계
- 지면 제한으로 LLM의 SciSci 적용 가능성 중 많은 영역(full-text analysis, sentiment analysis, citation analysis 강화 등)이 미탐구
- AI agent의 효과가 아직 상당한 개선이 필요하다고 인정

### 리뷰어 판단 아쉬운 점
- 전반적으로 깊이보다 폭에 치중한 리뷰. LLM 기술 소개 부분(Section 1)이 일반적인 교과서 수준이며 SciSci 연구자에게 특화된 통찰이 부족
- 제시된 데모와 방법론(entity extraction, research front detection)이 매우 초보적이며 성능 평가(정확도, recall, 기존 방법론과의 비교)가 전혀 없음
- GPT-4 파라미터를 "1.76 trillion, 120 layers"로 기술하나 이는 검증되지 않은 루머 수준의 정보
- SciSciGPT(Shao et al., 2025)와 같은 동시대 관련 연구와의 비교가 전혀 없음
- 영어 교정이 필요한 부분이 다수 존재하며(예: "milion" 오타), 전반적인 학술적 완성도가 낮음
- arXiv preprint으로 peer review를 거치지 않은 상태

### 후속 연구
- LLM 기반 entity extraction의 정확도를 기존 NER/RE 방법론과 체계적으로 비교
- AI agent 기반 과학 평가의 신뢰성 검증(전문가 평가와의 일치도)
- Multilayer network 기반 research front 탐지의 정량적 검증(기존 co-citation cluster 방법론 대비)
- Full-text 분석, multimodal SciSci 등 미탐구 영역의 구체화

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 2/5 |
| Technical Soundness | 2/5 |
| Significance | 2/5 |
| Clarity | 3/5 |
| Overall | 2/5 |

**총평**: LLM 기술과 SciSci의 교차점을 폭넓게 조망하려는 시도는 의미 있으나, 기술 소개가 피상적이고, 제안된 방법론의 평가가 부재하며, 학술적 완성도가 낮아 현재 상태로는 분야에 대한 실질적 기여가 제한적이다.
