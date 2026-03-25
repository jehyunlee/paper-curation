# Scientific production in the era of Large Language Models

> **저자**: Keigo Kusumegi, Xinyu Yang, Paul Ginsparg, Mathijs de Vaan, Toby Stuart, Yian Yin | **날짜**: 2025 | **DOI**: 10.1126/science.adw3000

---

## 핵심 요약
본 연구는 Large Language Models(LLMs)이 과학 연구 생산에 미치는 거시적 영향을 210만 편의 preprint, 2.8만 건의 peer review 보고서, 2.46억 건의 온라인 접속 데이터를 활용하여 분석한다. LLM 도입이 연구자의 생산성을 23.7~89.3% 증가시키고, 언어적 복잡성과 논문 품질 간의 기존 양의 상관관계를 역전시키며, 연구자들이 더 다양한 선행 문헌을 접하도록 유도한다는 세 가지 핵심 발견을 제시한다.

## 연구 배경 및 동기
생성형 AI가 모든 학문 분야에서 빠르게 채택되고 있음에도 불구하고, LLM이 과학적 생산 전반에 미치는 체계적 영향에 대한 실증적 증거는 단편적이었다. 기존 연구들이 단백질 구조 예측이나 재료 발견 등 특정 과학적 맥락에서의 AI 활용을 다루었다면, 본 연구는 과학 기업 전체에 대한 LLM의 거시적 영향이라는 열린 질문에 답하고자 한다.

## 방법론
- **데이터**: arXiv(120만 편), bioRxiv(22.1만 편), SSRN(67.6만 편)의 2018-2024년 preprint와 ICLR-2024의 2.8만 건 peer review 보고서, arXiv 논문에 대한 2.46억 건의 조회/다운로드 기록 활용
- **LLM 사용 탐지**: ChatGPT 이전 시기의 human-written text token 분포와 GPT-3.5turbo로 재작성한 LLM-written text token 분포를 비교하는 텍스트 기반 AI 탐지 알고리즘 개발
- **분석**: Author-level fixed effects event model을 통한 생산성 분석, Flesch Reading Ease Score를 활용한 writing complexity 분석, differences-in-differences 분석을 통한 인용 행동 변화 분석

## 주요 결과
- LLM 채택 후 연구자의 논문 생산성이 arXiv 36.2%, bioRxiv 52.9%, SSRN 59.8% 증가
- 아시아계 연구자(비영어 모국어)의 생산성 증가가 가장 큼: bioRxiv 89.3%, SSRN 88.9%
- LLM 보조 논문에서 writing complexity와 논문 품질 간 관계가 역전됨 — 복잡한 문체의 LLM 보조 논문이 오히려 낮은 peer review 점수를 받음
- Bing Chat(GPT-4) 도입 후 사용자가 책(+26.3%), 더 최근 논문, 덜 인용된 논문에 접근하는 경향 증가
- LLM 채택자들은 11.9% 더 높은 확률로 책을 인용하고, 평균 0.379년 더 최근 문헌을 인용

## 독창성 및 기여
세 가지 대규모 preprint 저장소를 통합하여 LLM이 과학 생산에 미치는 거시적 영향을 최초로 체계적으로 분석한 연구이다. 특히 LLM이 writing complexity의 품질 신호 기능을 무력화한다는 발견과, 비영어권 연구자에 대한 비대칭적 생산성 효과의 정량화는 과학 정책에 중요한 시사점을 제공한다.

## 한계 및 향후 연구
- 인과적 식별 미비: AI 탐지 방법의 불완전성, self-selection bias 가능성
- 초록 기반 탐지로 전문 전체에서의 LLM 사용을 포착하지 못함
- ChatGPT 이후 초기 세대 LLM 데이터에 기반한 스냅샷이므로, 현재의 더 발전된 모델 효과는 미반영
- 향후 LLM이 학문 간 장벽을 낮추는 효과와 "invisible colleges" 대체 가능성에 대한 연구 필요

## 평가
| 항목 | 점수 |
|------|------|
| Novelty | 5/5 |
| Technical Soundness | 4/5 |
| Significance | 5/5 |
| Clarity | 5/5 |
| Overall | 5/5 |

**총평**: Science지에 게재된 본 연구는 LLM이 과학 생산 생태계를 근본적으로 재편하고 있음을 대규모 실증 데이터로 설득력 있게 보여주며, 과학 평가 체계의 재설계 필요성을 강력히 제기하는 landmark 연구이다.
