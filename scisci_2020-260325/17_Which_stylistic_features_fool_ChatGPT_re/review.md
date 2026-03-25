# Which stylistic features fool ChatGPT research evaluations?
> **저자**: Kayvan Kousha, Mike Thelwall | **날짜**: 2026-03-16 | **Journal**: arXiv preprint | **DOI**: arXiv:2603.14919
---

## Essence
ChatGPT는 인간 전문가보다 초록의 언어적 복잡성(linguistic complexity)에 더 민감하게 반응하여 높은 점수를 부여한다. UK REF2021에 제출된 99,277편의 논문 초록을 분석한 결과, 34개 평가 단위(UoA) 중 23개에서 Flesch-Kincaid Grade Level과 ChatGPT 점수 간 유의한 양의 상관관계가 나타났으나, REF 전문가 점수에서는 9개 UoA에서만 유의했다. 예를 들어, 임상의학에서 Flesch-Kincaid Grade Level과의 Spearman 상관계수가 ChatGPT 0.329 vs. REF 전문가 0.124로 큰 차이를 보였다.

## Motivation
- **알려진 것**: LLM은 제목과 초록만으로도 연구 품질을 중간 정도로 예측할 수 있으며, 전문(full text)보다 오히려 더 나은 상관관계를 보이는 역설적 현상이 보고됨
- **갭**: LLM이 연구 품질과 무관한 텍스트의 문체적 특성(가독성, 언어 복잡성, 길이)에 의해 "속는지"는 체계적으로 검증된 바 없음
- **왜 중요한가**: LLM 기반 연구 평가가 실제 적용될 경우, 저자들이 연구 품질이 아닌 글쓰기 스타일을 조작하여 점수를 높일 가능성이 있음
- **접근법**: REF2021 데이터셋에서 다양한 가독성 지표(Flesch Reading Ease, Flesch-Kincaid Grade Level, Gunning Fog 등)와 ChatGPT/REF 전문가 점수 간 Spearman 순위 상관관계를 비교 분석

## Achievement
1. **언어 복잡성 편향 확인**: 34개 UoA 중 23개에서 Flesch-Kincaid Grade Level과 ChatGPT 점수 간 유의한 양의 상관, REF 전문가 점수는 9개에서만 유의
2. **어휘 복잡성 민감도**: 단어당 음절 수(syllables per word)와 ChatGPT 점수 간 28/34 UoA에서 유의한 양의 상관 vs. REF 전문가 점수는 11/34 UoA에서만 유의
3. **분야별 차이**: 의생명 및 STEM 분야에서는 짧지만 복잡한 초록이, 사회과학/인문학에서는 긴 초록이 ChatGPT에서 높은 점수를 받는 경향
4. **인용 영향과의 비교**: ChatGPT 점수는 인용 영향(NLCS)보다 초록 복잡성과 더 강한 상관관계를 보임
5. **문장 길이 효과**: 문장당 단어 수도 ChatGPT 점수와 더 강하게 상관 (임상의학: 0.306 vs. 0.150)

## How
- **데이터**: UK REF2021에 제출된 99,277편 고유 저널 논문 (최하위 10% 짧은 초록 제외)
- **LLM 점수**: ChatGPT-4o, ChatGPT-4o mini, ChatGPT-5 mini의 API를 통해 제목+초록 기반 평가, 각 5회 반복 평균
- **전문가 점수**: REF2021 학과 평균 점수 (프록시) + UoA 1-6에 대해 논문 500편씩 개별 전문가 점수
- **텍스트 분석**: Python textstat 라이브러리로 Flesch Reading Ease, Flesch-Kincaid Grade Level, Gunning Fog, SMOG, ARI, 단어 수, 문장당 단어 수, 단어당 음절 수 계산
- **통계**: Spearman 순위 상관계수 + 부트스트랩 95% 신뢰구간

## Originality
- LLM 연구 평가에서 **초록의 문체적 특성이 미치는 영향**을 34개 학문 분야에 걸쳐 대규모로 체계적 비교한 최초의 연구
- ChatGPT 점수, REF 전문가 점수, 인용 영향의 **3자 비교**를 통해 LLM 고유의 편향을 분리
- 단순한 가독성 지표(Flesch-Kincaid 등)만으로도 LLM 평가의 조작 가능성을 실증적으로 보여줌

## Limitation & Further Study

### 저자들이 언급한 한계
- 영국 단일 국가 데이터로, 비영어권에서는 다른 패턴이 나타날 수 있음
- REF 제출 논문은 이미 품질이 사전 선별되어 상관관계가 약화되었을 가능성
- 대규모 데이터셋에서는 개별 REF 전문가 점수가 아닌 학과 평균 점수를 프록시로 사용
- 상관분석이므로 인과관계는 입증되지 않음
- 초록 구조(배경, 방법, 결론 등)나 방법론적 세부사항 같은 추가 텍스트 특성은 미분석

### 리뷰어 판단 아쉬운 점
- ChatGPT-4o/5 mini만 사용하여, 최신 reasoning 모델(o1, o3 등)이나 다른 LLM(Gemini, Claude)에서 동일한 편향이 있는지 미확인
- 프롬프트에 "언어 스타일을 무시하라"는 지시를 추가했을 때의 효과를 실험적으로 검증하지 않음
- 인과관계 부재를 인정하면서도, 언어 복잡성과 연구 주제 난이도 간의 교란 효과(confounding)에 대한 통제가 부족
- 초록의 언어적 복잡성이 실제 연구의 방법론적 복잡성과 상관될 수 있는데, 이를 분리하는 분석이 없음

### 후속 연구
- 초록을 의도적으로 단순화/복잡화한 **실험적 연구**(causal design)로 인과관계 검증 필요
- 프롬프트 엔지니어링을 통한 편향 완화 전략의 효과성 검증
- 비영어 논문 및 다국어 LLM에서의 재현성 연구
- 초록 구조(structured vs. unstructured)가 LLM 평가에 미치는 영향 분석

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 4/5 |
| Technical Soundness | 3/5 |
| Significance | 4/5 |
| Clarity | 4/5 |
| Overall | 4/5 |

**총평**: LLM 기반 연구 평가의 실질적 위험 요소인 언어적 복잡성 편향을 대규모 데이터로 실증한 시의적절한 연구이나, 상관분석에 머물러 인과적 메커니즘 규명과 편향 완화 방안의 실험적 검증이 후속 과제로 남아 있다.
