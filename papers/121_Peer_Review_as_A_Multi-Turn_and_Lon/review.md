# Peer Review as A Multi-Turn and Long-Context Dialogue with Role-Based Interactions

- **저자**: Cheng Tan, Dongxin Lyu, Siyuan Li, Zhangyang Gao, Jingxuan Wei, Siqi Ma, Zicheng Liu, Stan Z. Li
- **소속**: Westlake University, Jilin University, University of Chinese Academy of Sciences
- **발표**: arXiv:2406.05688 (2024)
- **DOI**: [10.48550/arXiv.2406.05688](https://doi.org/10.48550/arXiv.2406.05688)

---

## Essence (핵심 요약)

학술 피어 리뷰 프로세스를 **multi-turn, long-context, role-based dialogue**로 재정식화(reformulate)하는 새로운 관점을 제안한다. 기존의 "논문 -> 리뷰" 단방향 생성이 아닌, Reviewer(초기 리뷰) -> Author(rebuttal) -> Reviewer(최종 리뷰) -> Decision Maker(결정)의 4턴 대화로 모델링한다. 이를 위해 ICLR(2017-2024)와 Nature Communications(2023)에서 26,841편 논문, 92,017개 리뷰, 5.67억 토큰 규모의 ReviewMT 데이터셋을 구축하고, 7개 오픈소스 LLM을 zero-shot과 supervised fine-tuning으로 벤치마크한다.

---

## Motivation (연구 동기)

기존 LLM 피어 리뷰 연구는 논문을 입력받아 리뷰를 생성하는 **단방향, 정적(static) 접근**에 국한되어 있다. 그러나 실제 피어 리뷰는 리뷰어의 초기 평가, 저자의 반박(rebuttal), 리뷰어의 최종 의견 수정, 그리고 편집자/AC의 결정이라는 **동적이고 반복적인 상호작용** 과정이다. 이 과정을 포착하지 못하면 LLM 리뷰 시스템은 실제 리뷰 프로세스의 본질적 가치인 건설적 대화와 논문 개선 기회를 반영할 수 없다. 또한 기존 instruction tuning 데이터셋은 대부분 single-turn에 집중하여 multi-turn, long-context 대화의 특성을 갖추지 못했다.

---

## Achievement (주요 성과)

1. **ReviewMT 데이터셋 구축**: 26,841편 논문, 92,017개 리뷰, 5.67억 토큰의 대규모 multi-turn 피어 리뷰 데이터셋. ICLR(2017-2024) + Nature Communications(2023) 수록
2. **4턴 대화 프레임워크 정식화**: 피어 리뷰를 Reviewer -> Author -> Reviewer -> Decision Maker의 role-based multi-turn dialogue로 공식화
3. **종합적 평가 메트릭 제안**: validity(paper/review/decision hit rate), text quality(BLEU, ROUGE, METEOR), score evaluation(MAE), decision evaluation(F1-score)
4. **7개 LLM 벤치마크**: LLaMA-3, Qwen, Baichuan2, ChatGLM3, Gemma, DeepSeek, Yuan-2의 zero-shot 및 SFT 성능 비교
5. **핵심 발견**: Zero-shot에서 review hit rate가 극히 낮으나(대부분 0-2%), SFT 후 극적 향상(Baichuan2: 0% -> 98.45%). Multi-turn 데이터(ICLR)로 학습 시 single-turn(NC) 대비 더 큰 성능 향상 관찰
6. **데이터셋 오픈소스**: github.com/chengtan9907/ReviewMT

---

## How (방법론)

### 프레임워크 정식화
4턴 대화로 피어 리뷰를 모델링:
- **Turn 1** (Reviewer): P -> {Ri} -- 논문으로부터 N명의 리뷰어가 초기 리뷰 생성 (Summary, Strengths, Weaknesses, Questions)
- **Turn 2** (Author): {Ri} -> {Ai} -- 각 리뷰에 대한 저자의 rebuttal
- **Turn 3** (Reviewer): {Ai} -> {R'i} -- rebuttal을 반영한 최종 리뷰 및 점수
- **Turn 4** (Decision Maker): {Ri, Ai, R'i} -> D -- 전체 대화를 종합한 accept/reject 결정

### 데이터 수집 및 처리
- **ICLR**: OpenReview API를 통해 2017-2024 논문 수집. Marker 도구로 PDF를 markdown 텍스트로 변환
- **Nature Communications**: Requests 라이브러리로 2023년 논문 크롤링. Peer Review File을 리뷰 정보로 통합
- JSON 포맷으로 통일. 각 턴의 필드를 구조화 (Title, Abstract, Main Text, Summary, Strengths, Weaknesses, Questions, Response, Final comment, Score, Meta review, Final decision)

### 실험 설정
- 7개 오픈소스 LLM을 LLaMA-factory로 구현
- ReviewMT-ICLR: 2017-2023 훈련, 2024에서 100편 테스트
- ReviewMT-NC: 100편 테스트, 나머지 훈련
- Zero-shot 및 SFT 성능 비교

---

## Originality (독창성)

1. **피어 리뷰의 multi-turn dialogue 재정식화**: 단방향 리뷰 생성이 아닌, 리뷰어-저자-결정자의 역할 기반 다턴 대화로 피어 리뷰를 모델링한 최초의 체계적 시도. 실제 학술 리뷰의 반복적 특성을 LLM 훈련 데이터로 포착
2. **대규모 multi-turn 리뷰 데이터셋**: 기존 리뷰 데이터셋(PeerRead, ASAP-Review 등)이 single-turn이거나 리뷰만 포함한 데 반해, rebuttal과 최종 리뷰, meta-review까지 포함한 완전한 대화 데이터 구축
3. **다학제적 범위**: ICLR(AI/ML)과 Nature Communications(자연과학 전반)를 결합하여, 리뷰 스타일과 학문 분야의 다양성 확보
4. **역할별 평가 메트릭**: 각 역할(reviewer, author, decision maker)에 맞춤화된 평가 메트릭 세트 제안

---

## Limitation & Further Study (한계 및 향후 연구)

### 한계
1. **Figure 미포함**: 논문 본문의 그림/표를 데이터셋에 포함하지 않아, 시각 정보가 핵심인 논문에 대한 리뷰 능력이 제한적
2. **제한된 학회/저널 범위**: ICLR과 Nature Communications에 국한되어, 다양한 학문 분야와 리뷰 문화를 대표하지 못함
3. **테스트 세트 규모**: 각 100편의 소규모 테스트 세트로, 통계적 신뢰도 확보에 한계
4. **편향 재생산 우려**: 인간 리뷰의 편향이 데이터셋에 내재되어 LLM이 이를 학습, 재생산할 위험
5. **실질적 리뷰 품질 미검증**: 텍스트 유사도 메트릭(BLEU, ROUGE)으로 리뷰 품질을 평가하지만, 실제 리뷰의 건설적 가치나 정확성은 측정하지 않음
6. **Nature Communications 데이터의 불완전성**: NC의 리뷰 데이터가 ICLR처럼 완전하지 않아 single-turn으로만 평가 가능

### 향후 연구 방향
- 다양한 학회 및 저널로 데이터셋 확장
- Figure 및 표를 포함한 멀티모달 리뷰 데이터셋 구축
- 리뷰의 건설성, 정확성을 직접 평가하는 메트릭 개발
- 편향 감지 및 완화 기법 적용

---

## Evaluation (총평)

본 논문의 가장 큰 기여는 피어 리뷰를 **multi-turn, role-based dialogue로 재정식화**한 개념적 프레임워크이다. 기존의 "논문 -> 리뷰" 단방향 패러다임에서 벗어나, 리뷰어-저자-결정자의 상호작용을 포착한다는 아이디어는 실제 학술 리뷰 프로세스의 본질에 더 부합하며, LLM 리뷰 시스템의 발전 방향을 제시한다.

데이터셋 구축 면에서 26,841편/92,017리뷰/5.67억 토큰의 규모와 ICLR+Nature Communications의 다학제적 범위는 의미 있으나, multi-turn 데이터가 완전한 것은 ICLR 부분뿐이라는 점은 아쉽다. 7개 LLM에 대한 벤치마크는 현재 모델들의 한계(zero-shot review hit rate < 20%)와 SFT의 효과를 잘 보여주지만, 실험 분석의 깊이가 다소 부족하다. 특히 "왜 특정 모델이 특정 메트릭에서 우수한가"에 대한 분석이나, 생성된 리뷰의 질적 분석이 없다.

평가 메트릭 측면에서 BLEU/ROUGE 같은 텍스트 유사도 메트릭은 리뷰 품질의 프록시로서 한계가 크며, 리뷰의 건설성이나 기술적 정확성을 반영하지 못한다. 또한 Figure를 포함하지 않은 점은 실용적 한계로 작용한다. 그럼에도, 피어 리뷰 자동화 연구의 방향을 정적 생성에서 동적 대화로 전환시키는 중요한 개념적 기여를 한 논문으로 평가할 수 있다.

## 평가
| 항목 | 점수 (1-5) |
|------|-----------|
| Novelty | 4 |
| Technical Soundness | 3 |
| Significance | 3 |
| Overall | 3.3 |

**총평**: 피어 리뷰를 다중 턴 대화로 재정의하고 26K 논문의 ReviewMT 데이터셋을 구축한 연구로, 대화형 피어 리뷰 모델링의 새 프레임워크를 제시하지만 생성 품질 평가가 표면적이다.
