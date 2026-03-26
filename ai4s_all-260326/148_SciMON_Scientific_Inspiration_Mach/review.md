# SciMON: Scientific Inspiration Machines Optimized for Novelty

> **저자**: Qingyun Wang, Doug Downey, Heng Ji, Tom Hope | **날짜**: 2024 | **Conference**: ACL 2024 (Long Papers) | **DOI**: 10.18653/v1/2024.acl-long.18

---

## Essence

SciMON은 과학 문헌으로부터 새로운 연구 방향을 자연어로 생성하는 프레임워크로, 기존의 이진 링크 예측(binary link prediction) 방식의 Literature-Based Discovery(LBD)를 근본적으로 탈피한다. 배경 문맥(문제, 동기, 실험 설정)을 입력으로 받아 과거 논문에서 "영감(inspiration)"을 검색하고, 반복적 novelty boosting을 통해 기존 연구와 차별화된 아이디어를 생성한다. GPT-4가 전반적으로 낮은 기술적 깊이와 참신성을 보이는 문제를 부분적으로 완화하는 데 성공했다.

## Motivation

- **알려진 것**: Literature-Based Discovery(LBD)는 Swanson(1986) 이래 약 40년간 연구되어 왔으나, 개념 쌍 간의 링크 예측(예: 약물-질병 관계)이라는 극히 제한된 형식에 국한
- **Gap**: 기존 LBD는 가설의 표현력이 극도로 제한적이며, 연구자가 고려하는 맥락(목표 응용, 제약 조건, 동기)을 포착하지 못함. 또한 생성된 아이디어의 참신성(novelty)을 명시적으로 최적화하지 않음
- **왜 중요한가**: LLM이 비약적으로 발전했지만 GPT-4조차 새로운 과학적 아이디어를 생성하는 데 어려움을 겪으며, 이를 체계적으로 평가하고 개선하는 프레임워크가 부재
- **접근법**: 배경 문맥을 입력으로 받아 문헌 기반 영감을 검색(semantic/KG/citation neighbors)하고, iterative novelty boosting으로 기존 연구 대비 차별성을 반복 강화하는 생성 프레임워크 설계

## Achievement

1. **새로운 문제 설정 정의**: 배경 문맥에서 자연어 과학 아이디어를 생성하는 최초의 체계적 평가 프레임워크 제시
2. **GPT-4 기반 모델 우위**: GPT4FS와 GPT4FS+KG가 다른 모든 모델 대비 큰 폭으로 우수 (helpful 비율 73%, 66%)
3. **Iterative novelty boosting 효과**: 1차 반복에서 54-56%의 아이디어가 참신성 향상, 2차 반복에서 추가 58% 향상 달성
4. **도메인 일반화**: NLP 도메인 외에 생화학 도메인에서도 Meditron+SN 모델이 80% helpful 평가 획득
5. **Ground truth 대비 한계 규명**: 85%의 비교에서 실제 논문 아이디어가 기술적 깊이와 참신성에서 현저히 우위 -- AI 가설 생성의 근본적 도전 과제 정량화

## How

- **데이터 수집**: 67,408편의 ACL Anthology 논문에서 scientific IE(PL-Marker, SciCo, ScispaCy)를 사용하여 배경 문장과 아이디어 문장 쌍 자동 추출. 시간 기반 분할(train: <2021, dev: 2021, test: 2022)
- **Inspiration Retrieval Module**: 세 가지 소스에서 영감 검색
  - Semantic Neighbors: SentenceBERT(all-mpnet-base-v2) 기반 유사 배경-아이디어 쌍 검색 (k=20)
  - KG Neighbors: 과학 논문에서 추출한 글로벌 knowledge graph의 인접 노드(task/method/material/metric) 활용
  - Citation Neighbors: 인용 네트워크에서 유사한 논문 제목을 SentenceBERT로 검색 (k=5)
- **Generation Module**: GPT-3.5/4의 zero-shot/few-shot/retrieval-augmented 설정과 T5 fine-tuning. In-context contrastive objective(InfoNCE loss)로 배경 복사 방지
- **Iterative Novelty Boosting**: 생성된 아이디어를 SentenceBERT로 문헌 코퍼스와 비교, cosine similarity > 0.6인 유사 연구 발견 시 "기존 연구와 다르게 수정하라"는 프롬프트로 반복 업데이트
- **평가**: 6명의 NLP 전문가(대학원 수준)에 의한 4가지 인간 평가 연구 (relevance, novelty, clarity, helpfulness)

## Originality

- **문제 설정의 전환**: LBD의 이진 링크 예측에서 자연어 기반 개방형 아이디어 생성으로의 패러다임 전환 -- 가설 공간의 표현력을 근본적으로 확장
- **Iterative Novelty Boosting**: 생성된 아이디어를 문헌과 반복 비교하여 참신성을 명시적으로 최적화하는 최초의 메커니즘. 연구자가 관련 연구를 확인하고 아이디어를 수정하는 과정을 모방
- **In-context Contrastive Objective**: 배경 문맥의 단어를 negative sample로 사용하여 입력 복사를 억제하는 새로운 학습 목표
- **다중 소스 영감 검색**: 의미적 유사도, knowledge graph, 인용 네트워크를 결합한 다층적 영감 검색 체계

## Limitation & Further Study

### 저자들이 언급한 한계

- GPT-4 생성 아이디어의 85%가 실제 논문 대비 기술적 깊이와 참신성이 현저히 부족 -- 근본적 품질 격차 존재
- 모델이 인기 개념의 피상적 조합(예: "Dynamic Syntax-Aware Graph Fusion Networks")에 의존하는 경향
- IE 전처리 파이프라인의 노이즈(관계 추출 정확도 65%)가 데이터 품질에 영향
- GPU 제약으로 7B 파라미터 이하 모델만 실험, GPT API 변경으로 재현성 제한

### 자체판단 아쉬운 점

- NLP 도메인 중심 평가로 자연과학(물리, 화학, 생물학) 등 실험 기반 분야에서의 일반화 가능성이 검증되지 않음
- 생성된 아이디어의 실현 가능성(feasibility)이나 실제 연구로의 전환 가능성에 대한 평가가 부재
- Novelty boosting이 종종 generic한 용어(dynamic, adaptive, multi-modal) 추가에 그치며, 진정한 개념적 혁신보다는 표면적 차별화에 머무르는 한계
- 인간 평가자가 대학원생으로 한정되어 시니어 연구자의 관점이 반영되지 않음
- 단일 문장 수준의 아이디어 생성에 국한되어, 실제 연구 제안서 수준의 구체적이고 구조화된 가설 생성으로 확장 필요

### 후속 연구

- 수식, 표, 그림 등 멀티모달 분석을 통한 배경 문맥 확장
- Seed term 없이 완전 자율적 아이디어 생성으로의 확장
- 생성된 아이디어의 실험적 검증 가능성 평가 체계 구축
- 더 큰 규모의 LLM(GPT-4급 이상) 및 도메인 특화 모델과의 결합

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 4/5 |
| Technical Soundness | 3/5 |
| Significance | 4/5 |
| Clarity | 4/5 |
| Overall | 4/5 |

**총평**: 과학적 가설 생성을 이진 링크 예측에서 자연어 기반 개방형 생성으로 전환한 선구적 연구로, 문제 설정 자체의 참신성이 높다. Iterative novelty boosting과 다중 소스 영감 검색이라는 구체적 방법론을 제시하고, GPT-4의 과학적 아이디어 생성 능력을 최초로 체계적으로 평가한 점에서 AI for Science 분야에 중요한 기여를 했다. 다만, 생성된 아이디어가 실제 논문 대비 현저히 낮은 품질을 보이는 근본적 한계를 드러냈으며, 이는 LLM 기반 과학적 창의성의 현주소를 솔직하게 보여주는 의미 있는 결과이다.
