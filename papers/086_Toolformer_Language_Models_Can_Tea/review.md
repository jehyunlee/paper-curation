# Toolformer: Language Models Can Teach Themselves to Use Tools

> **저자**: Timo Schick, Jane Dwivedi-Yu, Roberto Dessi, Roberta Raileanu, Maria Lomeli, Luke Zettlemoyer, Nicola Cancedda, Thomas Scialom | **날짜**: 2023-02-09 | **arXiv**: 2302.04761 | **DOI**: 10.48550/arXiv.2302.04761

---

## Essence

Toolformer는 언어 모델이 외부 도구(계산기, QA 시스템, 검색 엔진, 번역기, 달력)의 사용법을 자기지도 학습 방식으로 스스로 학습하는 방법론이다. LM이 텍스트 내 잠재적 API 호출 위치와 인수를 생성하고, perplexity 감소 기준으로 유용한 호출만 필터링한 데이터셋으로 fine-tuning하여, 6.7B 파라미터 GPT-J 기반으로 175B GPT-3를 다수 태스크에서 능가하는 zero-shot 성능을 달성했다.

## Motivation

- **알려진 것**: 대규모 LM은 few-shot/zero-shot으로 다양한 태스크를 해결하지만, 산술 계산, 사실 검색, 최신 정보 접근, 저자원 언어 이해 등 기본적 기능에서 한계를 보임
- **Gap**: 기존 tool-augmented LM 접근법은 대량의 인간 어노테이션에 의존하거나(Komeili et al., LaMDA), 특정 태스크에서만 tool 사용을 지원하여(PAL, TALM) 범용적 tool 사용이 불가능
- **왜 중요한가**: LM이 자율적으로 "언제, 어떤 도구를, 어떤 인수로" 호출할지 결정할 수 있다면, 인간 감독 없이도 도구 활용의 범용성이 크게 확장됨
- **접근법**: LM 자체의 in-context learning으로 API 호출을 생성하고, API 응답이 future token prediction loss를 감소시키는지로 유용성을 판단하여 self-supervised 학습 데이터를 구축

## Achievement

1. **LAMA (사실 완성)**: Toolformer가 SQuAD 33.8, Google-RE 11.5, T-REx 53.5로 GPT-3(175B)의 26.8, 7.0, 39.8을 크게 능가 -- QA 도구를 98.1% 예시에서 자율 호출
2. **수학 추론**: ASDiv 40.4, SVAMP 29.4, MAWPS 44.0으로 GPT-3(175B)의 14.0, 10.0, 19.8 대비 약 3배 향상 -- Calculator 도구를 97.9% 예시에서 사용
3. **QA**: WebQS 26.3, NQ 17.7, TriviaQA 48.8로 GPT-J 대비 큰 폭 향상. 다만 GPT-3(175B)에는 미달
4. **언어 모델링 능력 유지**: WikiText/CCNet perplexity가 API 호출 비활성화 시 GPT-J+CC와 동일 (10.3/10.5) -- tool 학습이 언어 모델링 능력을 훼손하지 않음
5. **Scaling Law 발견**: Tool 활용 능력은 약 775M 파라미터부터 emergent하게 나타남. 작은 모델은 도구 사용 여부와 무관하게 유사한 성능

## How

- **Step 1 - API 호출 샘플링**: 각 API에 대해 few-shot 프롬프트 P(x)를 제공하여 LM이 텍스트 x의 각 위치 i에서 `<API>` 토큰 생성 확률 계산. 임계값 tau_s 초과 위치에서 최대 m개 API 호출 후보 생성
- **Step 2 - API 실행**: 생성된 API 호출을 실제 도구(Atlas QA, Python 계산기, BM25 Wikipedia 검색, NLLB 번역, 달력)로 실행하여 응답 획득
- **Step 3 - API 호출 필터링**: L_i^-(API 호출 없음 또는 응답 없는 호출) vs L_i^+(API 호출+응답 포함)의 weighted cross-entropy loss 차이가 tau_f 이상인 호출만 유지. 응답이 미래 토큰 예측에 도움이 되는 호출만 선별
- **Fine-tuning**: 필터링된 API 호출을 원본 텍스트에 삽입하여 augmented dataset C* 구성, 표준 LM objective로 GPT-J fine-tuning. 배치 크기 128, 학습률 1e-5, 최대 2,000 스텝
- **추론**: 디코딩 중 `<API>` 토큰이 top-k(k=10) 내에 있으면 API 호출 개시, `->` 토큰 생성 시 디코딩 중단 후 실제 API 호출, 응답 삽입 후 디코딩 재개. 입력당 최대 1회 API 호출 제한
- **5가지 도구**: QA(Atlas), Calculator(Python), WikiSearch(BM25+KILT), MT(NLLB 600M), Calendar

## Originality

- **Self-supervised Tool Learning**: 인간 어노테이션 없이 LM 자체의 perplexity 감소를 기준으로 유용한 API 호출을 자동 식별하는 최초의 범용적 접근법. "인간이 유용하다고 생각하는 것"과 "모델이 유용하다고 판단하는 것"이 다를 수 있다는 통찰에 기반
- **범용적 도구 사용**: 특정 태스크에 특화되지 않고, 모델이 자율적으로 "언제, 어떤 도구를, 어떤 인수로" 호출할지 결정. Zero-shot 설정에서 사전에 어떤 도구를 사용할지 지정하지 않음
- **언어 모델링 능력 비훼손**: Augmented dataset이 원본과 동일한 텍스트를 포함하도록 설계하여, 도구 학습이 핵심 LM 능력을 보존. 이는 기존 tool-augmented 접근법과 차별화되는 핵심 설계 원칙
- **Perplexity 기반 필터링**: L_i^- - L_i^+ >= tau_f 조건으로 API 호출의 유용성을 정량적으로 판단하는 우아한 필터링 메커니즘

## Limitation & Further Study

### 저자들이 언급한 한계

- **도구 체이닝 불가**: 각 도구의 API 호출이 독립적으로 생성되어, 한 도구의 출력을 다른 도구의 입력으로 사용하는 chain 호출이 불가능
- **대화형 도구 사용 불가**: 검색 결과 탐색, 쿼리 재구성 등 도구와의 interactive 사용이 지원되지 않음
- **입력 표현 민감성**: API 호출 여부가 입력의 정확한 표현(wording)에 민감하게 반응
- **Sample 비효율성**: 100만 개 이상의 문서 처리 후 Calculator API 유용 호출이 수천 개에 불과
- **API 호출 비용 미고려**: 도구별 계산 비용 차이를 고려하지 않고 API 호출 결정

### 자체판단 아쉬운 점

- 입력당 최대 1회 API 호출 제한으로 복합적 질문(예: 날짜 확인 후 QA)에 대응 불가 -- TEMPLAMA에서 Calendar의 활용률이 0.2%에 불과한 근본 원인
- GPT-J(6.7B)에서만 검증되어, 더 큰 모델이나 다른 아키텍처로의 일반화가 확인되지 않음
- 5가지 도구만 실험하여, 코드 실행기, 데이터베이스, 이미지 생성 등 더 복잡한 도구로의 확장 가능성이 미검증
- QA 벤치마크에서 GPT-3(175B)에 미달하는 성능은 검색 도구의 단순함(BM25)에도 원인이 있으나, 더 강력한 검색 시스템과의 결합이 시도되지 않음
- Filtering threshold tau_f의 선택이 도구별로 상이하며, 최적 임계값 결정에 대한 체계적 분석이 부족

### 후속 연구

- 도구 체이닝 및 interactive 도구 사용 지원으로 복합적 쿼리 해결
- Iterative bootstrapping을 통한 sample 효율성 향상
- 더 큰 모델(LLaMA, GPT-4급) 및 다양한 도구(코드 실행기, 웹 브라우저 등)로의 확장
- API 호출의 계산 비용을 고려한 cost-aware 호출 결정 메커니즘
- 실제로 이 방법론은 이후 Gorilla, ToolLLM, AnyTool 등 대규모 tool learning 연구의 기반이 됨

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 5/5 |
| Technical Soundness | 5/5 |
| Significance | 5/5 |
| Clarity | 5/5 |
| Overall | 5/5 |

**총평**: Tool learning 분야의 선구적 연구로, LM이 자기지도 학습 방식으로 외부 도구의 사용법을 스스로 학습할 수 있음을 최초로 체계적으로 입증했다. "perplexity 감소 = 유용한 API 호출"이라는 간결하면서도 강력한 원칙에 기반한 필터링 메커니즘이 핵심 혁신이며, 6.7B 모델이 175B GPT-3를 능가하는 결과는 도구 활용이 단순한 모델 스케일링의 대안이 될 수 있음을 보여준다. 도구 체이닝과 interactive 사용의 한계는 이후 연구들(AnyTool, ToolLLM 등)이 해결 방향을 제시했으나, Toolformer의 self-supervised 학습 패러다임은 여전히 이 분야의 근본적 토대로 남아 있다.
