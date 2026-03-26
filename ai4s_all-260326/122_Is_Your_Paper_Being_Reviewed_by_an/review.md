# Is Your Paper Being Reviewed by an LLM? Investigating AI Text Detectability in Peer Review

- **저자**: Sungduk Yu, Man Luo, Avinash Madasu, Vasudev Lal, Phillip Howard
- **소속**: Intel Labs
- **발표**: arXiv:2410.03019 (2024)
- **DOI**: [10.48550/arXiv.2410.03019](https://doi.org/10.48550/arXiv.2410.03019)

---

## Essence (핵심 요약)

피어 리뷰에서 LLM이 생성한 텍스트를 **개별 리뷰 수준에서 탐지**하는 문제를 최초로 체계적으로 조사한 연구이다. GPT-4o와 Llama-3.1-70B로 ICLR 논문에 대한 16,000개의 AI 리뷰를 생성하고, 기존 AI 텍스트 탐지 방법(RoBERTa, Longformer, Originality AI, LLM-as-judge)의 성능을 평가한 결과, 낮은 false positive rate(FPR)에서 GPT-4o 리뷰 탐지가 매우 어렵다는 것을 발견한다. 이를 해결하기 위해 **Anchor Embeddings Detection** 방법을 제안하여, FPR 5%에서 GPT-4o 리뷰의 97%를 탐지하는 성과를 달성한다.

---

## Motivation (연구 동기)

AI 학회 논문 투고량이 급증하면서(ICLR: 2019년 1,565편 -> 2024년 7,306편) 리뷰어 부담이 가중되고 있으며, 이에 따라 LLM을 이용한 리뷰 작성의 유혹이 커지고 있다. 실제로 ICLR 2024 리뷰 중 AI 생성으로 추정되는 비율이 뚜렷한 상승 추세를 보이며, 최근 연구에서 6.5~16.9%의 리뷰가 LLM을 실질적으로 활용했을 수 있다고 추정했다. 그러나 기존 AI 텍스트 탐지 연구는 코퍼스 수준의 통계적 분석에 머물렀고, **실제 운영에 필요한 개별 리뷰 수준의 탐지 가능성**은 미탐구 상태였다. 특히 false positive(인간 리뷰를 AI로 오판)의 심각한 윤리적 결과를 고려할 때, 낮은 FPR에서의 탐지 성능이 핵심적이다.

---

## Achievement (주요 성과)

1. **기존 방법의 한계 실증**: FPR 5%에서 Originality AI는 GPT-4o 리뷰의 58.6%만 탐지, RoBERTa는 18.6%, Longformer는 45.7%에 불과. 높은 TPR을 달성하려면 20% 이상의 FPR을 감수해야 함
2. **Anchor Embeddings Detection 제안**: 동일 논문에 대해 AI 리뷰를 생성하여 "앵커"로 사용하고, 테스트 리뷰와의 의미적 유사도를 비교하는 방법. FPR 5%에서 GPT-4o 리뷰 TPR 96.7% (GPT-4o Anchor), AUC 0.99 달성
3. **LLM 모델 간 탐지 난이도 차이 규명**: Llama-3.1 리뷰는 대부분의 방법으로 높은 TPR로 탐지 가능하나, GPT-4o 리뷰는 기존 방법으로 탐지가 매우 어려움
4. **LLM judge 판단 근거 분석**: t-SNE 클러스터링을 통해 AI/인간 판정 근거를 분석. AI 판정 이유(반복적 표현, 일관성 부족, 형식적 어조)와 인간 판정 이유(주관적 의견, 대화체, 구체적 비판)를 체계적으로 정리
5. **공정성 우려 제기**: "non-native language use"가 AI 판정 이유로 등장하여, 비영어권 화자에 대한 차별 위험을 실증적으로 확인

---

## How (방법론)

### 데이터 수집
- ICLR 2019-2024의 논문과 리뷰를 OpenReview API로 수집
- GPT-4o와 Llama-3.1-70B로 500편(연도당) x 4 archetype(balanced, nitpicky, innovative, conservative) = 연간 4,000개, 총 16,000개 AI 리뷰 생성
- ICLR 2022 리뷰어 가이드라인을 프롬프트에 포함

### 탐지 방법 비교
1. **오픈소스 분류기**: RoBERTa (HC3 데이터셋 학습), Longformer (MAGE 테스트베드)
2. **상용 API**: Originality AI -- 0~1 AI 점수 반환
3. **LLM-as-judge**: GPT-4o, Llama-3.1-70B에 chain-of-thought reasoning으로 human/AI 이진 판정
4. **Anchor Embeddings (제안)**: 동일 논문에 대해 간단한 프롬프트로 AI 리뷰를 생성(Anchor Review), 테스트 리뷰와 SFR-Embedding-Mistral로 임베딩 후 cosine similarity 비교. 유사도가 높을수록 AI 생성 가능성

### 평가 프레임워크
- TPR(True Positive Rate)과 FPR(False Positive Rate)의 트레이드오프를 중심으로 평가
- FPR 5%와 20%에서의 TPR 비교, ROC-AUC 분석
- 5-fold cross validation으로 임계값 추정 정확도 검증

---

## Originality (독창성)

1. **개별 리뷰 수준 탐지의 최초 체계적 연구**: 기존의 코퍼스 수준 분석(Liang et al., 2024)에서 벗어나, 실제 운영에 필요한 개별 리뷰 탐지 가능성을 최초로 조사
2. **Anchor Embeddings Detection**: 일반적 AI 텍스트 탐지가 아닌, **논문 특화 AI 리뷰 생성 후 의미적 유사도 비교**라는 새로운 접근. AI 리뷰가 동일 논문에 대해 의미적으로 수렴한다는 통찰을 활용
3. **리뷰어 archetype 다양화**: balanced, nitpicky, innovative, conservative 4가지 페르소나를 도입하여 실제 리뷰 다양성을 시뮬레이션
4. **FPR 중심 평가 관점**: 학술 리뷰 맥락에서 false positive의 심각성을 강조하고, 실용적으로 의미 있는 FPR 수준(1-5%)에서의 성능을 중심으로 평가

---

## Limitation & Further Study (한계 및 향후 연구)

### 한계
1. **AI 리뷰의 현실성 제한**: 실제 부정 리뷰어는 다양한 프롬프트 전략, 부분적 편집, 인간-AI 혼합 작성을 할 수 있으나, 본 연구는 완전 AI 생성 리뷰만 다룸
2. **ICLR 한정**: AI/ML 분야의 ICLR 리뷰만 대상으로 하여, 다른 학문 분야나 학회로의 일반화 가능성 미검증
3. **Anchor 방법의 비용**: 테스트할 리뷰마다 해당 논문에 대한 AI 리뷰를 새로 생성해야 하므로, 대규모 적용 시 LLM API 비용이 발생
4. **시간적 열화**: Table S2에서 인간 리뷰의 FPR이 2021년 14.8% -> 2024년 46.8%로 급증, 실제 인간 리뷰에 AI 도구 사용이 증가하면서 탐지 경계가 흐려지는 문제
5. **비영어권 화자 편향**: LLM judge가 "non-native language use"를 AI 판정 근거로 사용하여 비영어권 리뷰어를 부당하게 분류할 위험

### 향후 연구 방향
- 인간-AI 혼합 리뷰(부분 AI 생성) 탐지
- 다양한 학문 분야 및 학회로 확장
- Watermarking 기반 사전적(proactive) 탐지 방법과의 결합
- 편향 완화를 위한 공정성 고려 탐지 모델 개발

---

## Evaluation (총평)

본 논문은 피어 리뷰에서의 AI 텍스트 탐지라는 **시의적절하고 실용적으로 중요한 문제**를 다룬다. 기존 AI 텍스트 탐지 방법들이 피어 리뷰 맥락에서 어떤 한계를 보이는지를 체계적으로 실증하고, 특히 GPT-4o 리뷰의 탐지가 낮은 FPR에서 극히 어렵다는 발견은 학술 커뮤니티에 중요한 경고를 제공한다.

제안된 Anchor Embeddings 방법은 직관적이면서도 효과적이다. "동일 논문에 대한 AI 리뷰들은 의미적으로 수렴한다"는 가정이 실험적으로 잘 뒷받침되며, FPR 5%에서 97% TPR이라는 결과는 기존 방법 대비 월등하다. 다만 이 방법은 완전 AI 생성 리뷰에 최적화되어 있으며, 인간이 AI 출력을 편집한 혼합 리뷰에 대한 성능은 미지수이다.

LLM judge의 판단 근거 분석(Table S4)은 특히 가치 있다. AI 판정이 "awkward sentence structure", "non-native language use"에 의존한다는 발견은 AI 탐지 도구가 비영어권 연구자를 차별할 수 있음을 시사하며, 이는 탐지 기술 개발에서 공정성 고려가 필수적임을 강조한다. 논문의 범위가 비교적 좁고(4페이지 본문) 실험이 ICLR에 한정되지만, 문제 정의와 방법론의 명확성, 그리고 실용적 시사점이 뛰어난 연구이다.
