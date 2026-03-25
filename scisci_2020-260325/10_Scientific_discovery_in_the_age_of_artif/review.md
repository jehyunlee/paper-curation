# Scientific discovery in the age of artificial intelligence

> **저자**: Hanchen Wang, Tianfan Fu, Yuanqi Du, Wenhao Gao, Kexin Huang, Ziming Liu, Payal Chandak, Shengchao Liu, Peter Van Katwyk, Andreea Deac, Anima Anandkumar, Karianne Bergen, Carla P. Gomes, Shirley Ho, Pushmeet Kohli, Joan Lasenby, Jure Leskovec, Tie-Yan Liu, Arjun Manrai, Debora Marks 외 | **날짜**: 2023 | **Journal**: Nature | **DOI**: 10.1038/s41586-023-06221-2

---

## Essence

AI는 과학적 발견의 전 과정(데이터 수집, 표현 학습, 가설 생성, 실험 설계, 시뮬레이션)을 **증강하고 가속화**하고 있다. 자기지도학습(self-supervised learning), 기하학적 딥러닝(geometric deep learning), 생성 모델(generative models)이 핵심 기술적 돌파구이며, AlphaFold2의 단백질 접힘 문제 해결과 수백만 입자 분자 시뮬레이션이 대표적 성과이다. 그러나 데이터 품질, 분포 외 일반화(out-of-distribution generalization), 해석 가능성, 인과 추론의 한계가 AI4Science의 근본적 도전으로 남아 있다.

## Motivation

- **알려진 것**: 2010년대 초 딥러닝의 부상 이래 AI는 과학 전 분야에서 대규모 데이터 통합, 측정 정밀화, 실험 자동화에 활용되어 왔다.
- **문제**: AI4Science 분야가 급속히 성장하고 있으나, 과학적 발견 과정의 각 단계에서 AI가 어떤 역할을 하고 어떤 한계가 있는지를 체계적으로 정리한 종합 리뷰가 부족했다.
- **왜 중요한가**: 과학의 가설 공간은 극도로 방대하며(예: 약 10^60개의 약물 유사 분자), AI 없이는 체계적 탐색이 불가능한 영역이 늘어나고 있다.
- **접근법**: 물리학, 화학, 생물학, 지구과학 등 다양한 분야의 AI 활용 사례를 과학적 발견의 단계별(데이터 수집 -> 표현 학습 -> 가설 생성 -> 실험/시뮬레이션)로 구조화하여 리뷰한다.

## Achievement

1. **과학적 발견 과정의 AI 통합 프레임워크 제시**: 데이터 수집·주석·생성·정제, 표현 학습, 가설 생성, 실험 설계·시뮬레이션의 4대 단계로 AI4Science를 체계화하고, 각 단계의 핵심 기술과 사례를 종합했다.
2. **핵심 기술적 돌파구 정리**: (1) 자기지도학습(대규모 비라벨 데이터 활용, foundation model), (2) 기하학적 딥러닝(대칭성, 그래프 신경망), (3) 생성 모델(VAE, GAN, diffusion, normalizing flow), (4) 강화학습(조합적 가설 공간 탐색)의 4가지 핵심 패러다임을 정리했다.
3. **분야 횡단적 사례 종합**: 입자물리(LHC 희귀 이벤트 탐지), 천체물리(중력파 검출 6자릿수 가속), 분자생물학(AlphaFold2, 단백질 언어 모델), 화학(합성 경로 계획, 110억 리간드 가상 스크리닝), 재료과학(배터리 설계), 핵융합(토카막 플라즈마 제어) 등 수십 개 분야의 사례를 통합했다.
4. **근본적 도전과제 식별**: 분포 외 일반화, 인과 추론, 멀티모달 데이터 통합, 해석 가능성, 데이터 품질·접근성, 이중 용도(dual use) 위험을 AI4Science의 6대 핵심 과제로 제시했다.
5. **과학 수행 방식의 변화 전망**: 자율 실험실(self-driving labs), 산학 협력 모델의 변화, AI 전문가를 포함한 연구팀 구성의 변화, 교육 프로그램의 필요성을 논의했다.

## How

- **리뷰 구조**: 과학적 발견의 단계별(Observations -> Hypotheses -> Experiments 순환)로 AI 기술을 매핑
- **기술 범위**: 딥 표현학습, 기하학적 딥러닝(GNN, equivariant networks), 자기지도학습(masked-language modeling, contrastive learning), 생성 모델(VAE, GAN, normalizing flow, diffusion), 강화학습(GFlowNet 포함), 신경 연산자(neural operators), physics-informed neural networks
- **적용 분야**: 입자물리, 천체물리, 분자생물학, 약물 발견, 화학 합성, 재료과학, 지구과학, 양자물리, 유전체학, 기상학
- **참고문헌**: 238편, 14페이지 Nature Review 형식

## Originality

- **과학적 발견 과정 전체에 대한 통합적 AI 리뷰**: 기존 리뷰들이 특정 분야(약물 발견, 재료 등)나 특정 기술(GNN, 강화학습 등)에 집중한 반면, 본 논문은 과학적 발견의 전 과정과 전 분야를 아우르는 최초의 포괄적 Nature 리뷰이다.
- **알고리즘-과학 단계 매핑**: 특정 AI 알고리즘이 과학적 발견의 어떤 단계에서 어떤 역할을 하는지를 체계적으로 매핑한 프레임워크를 제시했다.
- **Grand Challenges의 체계적 식별**: AI4Science의 실용적(데이터, 소프트웨어/하드웨어), 알고리즘적(일반화, 인과성, 해석 가능성), 제도적(과학 수행 방식, 윤리) 도전을 세 차원에서 정리한 점이 독창적이다.

## Limitation & Further Study

### 저자들이 언급한 한계
- AI 모델의 분포 외 일반화(out-of-distribution generalization)가 여전히 미해결이며, 전이학습(transfer learning)의 이론적 기반이 부족하다.
- 블랙박스 모델의 해석 가능성이 제한적이어서, 정책 결정이나 안전 관련 분야에서의 활용에 장벽이 된다.
- 과학 데이터셋의 불완전성, 편향, 접근성 제한이 AI 적용의 근본적 장애물이다.
- AI의 이중 용도(dual use) 위험과 윤리적 문제에 대한 체계적 대응이 필요하다.
- 인과 추론을 AI에 통합하는 것은 아직 초기 단계이며, 상관관계 기반 패턴 발견을 넘어서야 한다.

### 리뷰어 판단 아쉬운 점
- **깊이 vs. 폭의 트레이드오프**: 14페이지에 물리, 화학, 생물, 지구과학 전체를 다루다 보니 각 분야별 기술적 깊이가 불가피하게 제한적이다. 전문가에게는 새로운 통찰이 적을 수 있다.
- **실패 사례와 한계의 과소 보고**: 성공 사례 위주로 구성되어 있으며, AI 기반 약물 발견의 낮은 임상 성공률, AI 예측의 실험 검증 실패 사례 등 부정적 결과에 대한 논의가 부족하다.
- **LLM 시대 이전 관점**: 2023년 8월 출판이나, GPT-4 등 대규모 언어 모델이 과학 연구에 미치는 영향(코드 생성, 문헌 요약, 가설 브레인스토밍 등)에 대한 논의가 거의 없다.
- **정량적 비교 부재**: AI 방법론 간, 또는 AI vs. 전통적 방법 간의 체계적 정량 비교가 없이 사례를 나열하는 형식이다.
- **재현성 문제의 피상적 다룸**: AI 모델의 재현성 위기에 대해 벤치마크와 오픈소스를 언급하지만, 구체적 해결 방안이 부족하다.

### 후속 연구
- 특정 분야(예: AI for Materials, AI for Drug Discovery)에 대한 보다 심층적이고 정량적인 리뷰가 필요하다.
- LLM/Foundation Model 기반 과학적 발견(autonomous scientific agent 등)의 체계적 평가 연구가 요구된다.
- AI 기반 과학적 발견의 실험 검증 성공률과 실패 사례를 체계적으로 분석하는 메타 연구가 가능하다.
- 인과 추론과 딥러닝의 통합(causal representation learning)이 AI4Science의 핵심 연구 방향이 될 것이다.

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 3/5 |
| Technical Soundness | 4/5 |
| Significance | 5/5 |
| Clarity | 4/5 |
| Overall | 4/5 |

**총평**: AI4Science 분야의 현황과 전망을 과학적 발견의 전 과정에 걸쳐 포괄적으로 정리한 권위 있는 리뷰로, 분야의 지형도를 파악하는 데 탁월하나, 리뷰 특성상 개별 기술에 대한 깊이와 비판적 분석은 제한적이다.
