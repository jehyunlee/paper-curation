# MatterChat: A Multi-Modal LLM for Material Science

> **저자**: Yingheng Tang, Wenbin Xu, Jie Cao, Weilu Gao, Steve Farrell, Benjamin Erichson, Michael W. Mahoney, Andy Nonaka, Zhi Yao | **날짜**: 2025-04-26 | **Repository**: arXiv | **DOI**: 10.48550/arXiv.2502.13107

---

## Essence

MatterChat는 무기 재료의 원자 구조 데이터와 텍스트 입력을 통합하는 구조 인식(structure-aware) 멀티모달 대형 언어 모델이다. 사전학습된 범용 기계학습 원자간 포텐셜(CHGNet)과 사전학습된 LLM(Mistral 7B)을 BLIP-2 스타일의 경량 브릿지 모듈로 연결하여, 재료 물성 예측(분류 6종 + 수치 3종)과 인간-AI 상호작용(과학적 추론, 합성 절차 안내)에서 GPT-4 및 기존 물리 ML 모델을 능가하는 성능을 달성했다.

## Motivation

- **알려진 것**: 그래프 기반 ML 모델(CGCNN, SchNet, CHGNet)이 재료 물성 예측에서 높은 정확도를 보이나, 텍스트 기반 상호작용이나 과학적 맥락 이해 능력이 부재
- **Gap**: 기존 LLM의 재료과학 적용은 화학식, SMILES, CIF 등 텍스트 기반 표현에 의존하여 원자 구조의 완전한 해상도(full resolution)를 상실하며, 순수 그래프 모델 대비 물성 예측 성능이 열등
- **왜 중요한가**: 재료 발견과 설계에서 구조적 정보와 언어적 정보를 동시에 활용하는 통합 모델이 필요하며, 이를 통해 전문가 지식 피드백 루프 구현 가능
- **접근법**: 사전학습된 uMLIP(CHGNet)에서 원자 임베딩을 추출하고, 학습 가능한 브릿지 모델로 LLM과 정렬하여 구조-언어 멀티모달 학습 실현

## Achievement

1. **분류 태스크 우수 성능**: 6개 분류 태스크(금속성, 밴드갭 유형, 안정성, 자성 등)에서 Vicuna, Mistral, SchNet, CHGNet 모두를 능가 -- 자성 예측 정확도 93.68%
2. **수치 예측 성능**: Formation energy RMSE 0.1500 eV/atom, Energy above hull RMSE 0.1053 eV/atom, Bandgap RMSE 0.5590 eV -- SchNet/CHGNet 대비 우수
3. **RAG 강화**: Multi-modal RAG 적용 시 Formation energy RMSE 0.1212, Bandgap RMSE 0.5058으로 추가 개선
4. **상용 LLM 대비 우위**: GNoME 신규 재료에 대한 formation energy 예측에서 GPT-4o, Gemini, DeepSeek 대비 ground truth에 훨씬 근접
5. **과학적 추론 및 합성 안내**: Si(Cmcm) 상의 불안정성 설명, GaN MOCVD 합성 절차, YIG 고상 반응 합성 프로토콜 등 구조 기반 심화 추론 시연
6. **효율적 학습**: 브릿지 모듈만 학습하고 그래프 인코더와 LLM은 동결하여 학습 비용 절감

## How

- **데이터**: Materials Project Trajectory(MPtrj) 데이터셋에서 relaxed 구조 142,899개 큐레이션. 9:1 train/test 분할. 각 구조에 12개 태스크(3 서술 + 9 물성) 생성
- **Material Processing Branch**: CHGNet(사전학습된 uMLIP)으로 결정 구조를 그래프로 인코딩하여 원자 수준 임베딩 추출. 원자=노드, 결합=엣지 표현
- **Bridge Model**: BLIP-2 아키텍처 영감의 다층 트랜스포머. 32개 학습 가능 쿼리 벡터가 교대 어텐션(짝수 층: cross-attention으로 원자 임베딩에서 특징 추출, 홀수 층: self-attention으로 표현 심화)을 수행. 선형 투영으로 LLM 호환 임베딩 생성
- **Language Processing Branch**: Mistral 7B LLM이 텍스트 프롬프트를 처리. 브릿지 모델의 쿼리 임베딩과 결합하여 최종 출력 생성
- **학습**: 2단계 -- (1) 사전학습: 그래프-텍스트 상관(contrastive loss) + 그래프 기반 텍스트 예측(conditional LM loss) + 그래프-텍스트 연관(BCE loss), (2) 미세조정: 12개 멀티태스크에 대한 supervised cross-entropy loss. 4 GPU x 8 노드 DDP 학습
- **Multi-modal RAG**: 추론 시 브릿지 모델 임베딩의 L2 유사도로 학습 세트에서 2개 유사 재료를 검색, 다수결/평균으로 최종 출력 집계
- **임베딩 분석**: UMAP 차원 축소 + SOAP 기술자 + REMatch 커널로 구조적 유사성과 물성 정보가 임베딩에 보존됨을 시각적으로 검증

## Originality

- **uMLIP-LLM 브릿지**: 사전학습된 범용 원자간 포텐셜(CHGNet)과 LLM을 경량 브릿지로 연결하는 최초의 시도 -- 기존 CIF/SMILES 텍스트 입력 대비 구조 정보의 완전한 보존
- **BLIP-2 아키텍처의 재료과학 적용**: 비전-언어 모델링의 bootstrapping 전략을 원자 구조-언어 정렬에 창의적으로 전이
- **Multi-modal RAG**: 구조 임베딩 기반 검색 증강 생성을 통해 추론 시 robustness 향상 -- 재료과학 특화 RAG의 새로운 패러다임
- **구조 기반 과학적 추론**: 원자 구조 입력에서 불안정성 이유, 합성 절차 등 심층 추론을 생성하는 working memory 메커니즘

## Limitation & Further Study

### 저자들이 언급한 한계

- 그래프-언어 정렬이 행동 수준(behavior-driven)에 머물며 완전한 표현 수준(representation-level) 정렬에 도달하지 못함
- 고정된 패러프레이즈 쿼리 세트 사용으로 언어적 다양성이 제한적
- 동결된 LLM이 일반 텍스트로 학습되어 재료과학 특화 추론에 한계 가능성

### 자체판단 아쉬운 점

- Bandgap RMSE 0.56 eV는 실용적 반도체 설계에는 아직 부족한 정확도 (실험적 불확실성 대비 큰 오차)
- 합성 절차 생성의 정확성에 대한 체계적 검증이 부재 -- 시연 수준에 머물며 hallucination 위험 평가 없음
- Materials Project 단일 소스에 의존하며, ICSD, AFLOW 등 다른 데이터베이스와의 교차 검증 부재
- CHGNet에 강하게 결합되어 있어, MACE, M3GNet 등 다른 uMLIP으로의 교체 유연성이 검증되지 않음
- 142,899개 학습 데이터의 원소 분포가 Pu까지로 제한되며, 희토류/악틴족 재료에 대한 성능 불확실
- GNoME 신규 재료에 대한 비교가 2개 샘플만으로 정량적 일반화 불가

### 후속 연구

- Contrastive loss를 포함한 end-to-end instructive fine-tuning으로 표현 수준 정렬 강화
- 그래프 생성 모듈(graph generative module) 통합을 통한 신규 재료 구조 발견으로 확장
- 재료과학 문헌 기반 LLM fine-tuning으로 도메인 특화 추론 능력 강화
- 언어적 다양성 확대 및 다국어 지원
- 다양한 uMLIP 백본(MACE, EquiformerV2 등)과의 호환성 검증

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 4/5 |
| Technical Soundness | 3/5 |
| Significance | 4/5 |
| Clarity | 4/5 |
| Overall | 4/5 |

**총평**: 사전학습된 uMLIP과 LLM을 경량 브릿지로 연결한다는 아이디어는 재료과학에서 멀티모달 AI의 실용적 방향을 제시한 의미 있는 연구이다. 특히 구조 정보의 완전한 보존과 인간-AI 상호작용의 동시 지원은 기존 접근법의 핵심 한계를 해결한다. 다만 수치 예측 정확도의 실용적 수준 도달 여부, 합성 절차 생성의 신뢰성 검증 부재, 단일 데이터 소스 의존 등은 후속 연구에서 보완이 필요하다.
