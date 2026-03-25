# Which Stylistic Features Fool ChatGPT Research Evaluations?

> **저자**: Kayvan Kousha, Mike Thelwall | **날짜**: 2026 | **소속**: University of Wolverhampton; University of Sheffield, UK

---

## 핵심 요약
본 논문은 ChatGPT가 학술 논문의 연구 품질을 평가할 때 abstract의 readability 및 linguistic complexity와 같은 문체적 특성에 인간 전문가보다 더 크게 영향을 받는지를 분석한다. UK REF2021에 제출된 99,277편의 journal article을 대상으로 readability indicator와 ChatGPT 점수 간의 상관관계를 조사한 결과, ChatGPT는 언어적으로 복잡한 abstract에 체계적으로 더 높은 점수를 부여하는 경향이 있음을 발견하였다.

## 연구 배경 및 동기
LLM 기반 연구 평가가 전문가 평가와 중간 수준의 일치도를 보이지만, 그 이유가 명확하지 않다. 특히 LLM이 full text보다 title과 abstract만으로 더 나은 성능을 보이는 역설적 현상은 LLM이 연구 품질과 무관한 문서 속성을 활용하고 있을 가능성을 시사한다. 기존 연구에서 abstract 길이, 기술 용어 사용 등이 ChatGPT 점수에 영향을 미칠 수 있다는 단편적 증거가 있었지만, abstract의 textual feature와 LLM 점수 간의 체계적 관계는 분석된 바 없었다.

## 방법론
- **데이터**: UK REF2021에 제출된 99,277편의 고유 journal article (34개 Unit of Assessment)
- **LLM 점수**: ChatGPT-4o, ChatGPT-4o mini, ChatGPT-5 mini의 평균 점수 (5회 반복 평균)
- **전문가 점수**: REF departmental average score를 proxy로 사용; UoA 1-6은 개별 점수(500편/UoA)도 활용
- **Readability 지표**: Flesch Reading Ease, Flesch-Kincaid Grade Level, Gunning Fog, SMOG, ARI (textstat 라이브러리)
- **Textual 지표**: abstract length (word count), words per sentence, syllables per word
- **분석**: Spearman rank correlation + bootstrapped 95% confidence interval
- **추가 비교**: Normalised Log-transformed Citation Score (NLCS 2024)와의 비교

## 주요 결과
- **Flesch-Kincaid Grade Level**: 34개 UoA 중 23개에서 ChatGPT 점수와 통계적으로 유의한 양의 상관관계; REF 전문가 점수는 9개 UoA에서만 유의한 양의 상관
- **Syllables per word**: 28/34 UoA에서 ChatGPT와 유의한 양의 상관 vs. 전문가 점수는 11개 UoA에서만 유의
- **Abstract length**: 분야별 차이가 크며, 의학 분야에서는 짧지만 복잡한 abstract가 높은 ChatGPT 점수를, 인문학에서는 긴 abstract가 높은 점수를 받음
- **Clinical Medicine** 예시: syllables per word와 ChatGPT 상관 0.329 vs. REF 전문가 0.124
- **Citation impact 비교**: ChatGPT는 linguistic complexity에 민감하지만, citation 기반 지표는 오히려 약한 음의 상관을 보임

## 독창성 및 기여
LLM 기반 연구 평가에서 linguistic complexity bias를 대규모 데이터(99,277편)와 34개 학문 분야에 걸쳐 체계적으로 실증한 최초의 연구이다. ChatGPT가 전문가보다 문체적 복잡성에 더 민감하다는 발견은 LLM 기반 평가 시스템의 공정성과 조작 가능성에 대한 중요한 경고를 제공한다. 또한 citation impact와의 비교를 통해 LLM bias가 citation bias와는 질적으로 다른 패턴임을 보여준다.

## 한계 및 향후 연구
- **저자 언급 한계**: UK 단일 국가 데이터, REF departmental average를 proxy로 사용한 점, correlation 분석이므로 인과관계 입증 불가, abstract structure 등 추가 textual feature 미고려
- **추가 지적**: (1) ChatGPT-4o/5 mini 세대에 한정되어 향후 모델에서의 재현성 검증 필요, (2) prompt engineering을 통한 bias 완화 가능성에 대한 실험적 검증이 부재, (3) 비영어권 논문에서의 패턴은 전혀 다를 수 있음, (4) REF에 제출된 논문은 이미 quality-selected된 샘플이라 range restriction이 존재

## 평가
| 항목 | 점수 (1-5) |
|------|-----------|
| Novelty | 4 |
| Technical Soundness | 4 |
| Significance | 5 |
| Clarity | 5 |
| Overall | 4.5 |

**총평**: LLM 기반 연구 평가의 실질적 위험을 대규모 데이터로 설득력 있게 입증한 시의적절하고 중요한 연구로, Science of Science 및 AI governance 분야 모두에 함의가 크다.
