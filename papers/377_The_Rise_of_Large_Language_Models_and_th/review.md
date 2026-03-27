# The Rise of Large Language Models and the Direction and Impact of US Federal Research Funding

> **저자**: Yifan Qian, Zhe Wen, Alexander C. Furnas, Yue Bai, Erzhuo Shao, Dashun Wang | **날짜**: 2026-01-21 | **Journal**: arXiv preprint | **DOI**: [10.48550/arXiv.2601.15485](https://doi.org/10.48550/arXiv.2601.15485)
> **리뷰 모드**: Abstract 기반 (PDF 없음)

---

## Essence

LLM의 부상이 미국 연방 연구 펀딩의 방향과 영향력을 어떻게 바꾸고 있는가? 이 논문은 NSF와 NIH에 제출된 기밀 제안서(펀딩된 것, 탈락한 것, 심사 중인 것 모두 포함)와 공개 수상 데이터를 결합하여, LLM이 연구 제안 작성에 미치는 영향을 체계적으로 분석한 최초의 대규모 연구다. 핵심 발견: (1) 2023년부터 LLM 사용이 급격히 증가하고 이분포(bimodal) 패턴을 보임; (2) LLM 사용이 높을수록 제안서의 의미론적 독특성이 낮아져 최근 펀딩된 연구와 유사해짐; (3) NIH에서는 LLM 사용이 제안 성공률과 논문 생산성 향상과 연관되지만, NSF에서는 그렇지 않다; (4) 생산성 향상이 최고 인용 논문보다 일반 논문에 집중됨.

## Originality (Abstract 기반)

- [authorship, novelty] "we examine LLM involvement at key stages of the federal funding pipeline by combining two complementary data sources: confidential National Science Foundation (NSF) and National Institutes of Health (NIH) proposal submissions from two large US R1 universities."
- [result, finding] "LLM use rises sharply beginning in 2023 and exhibits a bimodal distribution, indicating a clear split between minimal and substantive use."
- [result] "higher LLM involvement is consistently associated with lower semantic distinctiveness, positioning projects closer to recently funded work within the same agency."
- [result, finding] "LLM use is positively associated with proposal success and higher subsequent publication output at NIH, whereas no comparable associations are observed at NSF."
- [result] "the productivity gains at NIH are concentrated in non-hit papers rather than the most highly cited work."

## How (방법론)

- **데이터**:
  - 기밀 데이터: NSF + NIH에 2개 대형 R1 대학에서 제출된 제안서 (펀딩됨/탈락/심사중 모두 포함)
  - 공개 데이터: NSF + NIH 공개 수상 데이터 전수
- **LLM 관여도 측정**: 제안서 텍스트에서 LLM 사용 신호 탐지 (문체 특징, 특정 구문 패턴 등)
- **의미론적 독특성**: 텍스트 임베딩으로 각 제안서가 최근 펀딩된 연구들과 얼마나 유사한지 측정
- **성과 분석**:
  - 제안서 성공률 (LLM 사용 여부별)
  - 후속 논문 생산성 및 인용 분포
- **기관별 비교**: NSF vs. NIH 비교로 기관 특성에 따른 LLM 효과 차이 분석

## Why (중요성)

- LLM이 과학 글쓰기에 빠르게 확산되고 있으나, 펀딩 제안서 수준에서의 영향은 대부분 블랙박스로 남아 있었음
- LLM 사용이 의미론적 독특성을 낮춘다는 발견은 **연구 다양성과 포트폴리오 거버넌스**에 중요한 함의 — LLM이 과학적 아이디어의 동질화를 촉진할 수 있음
- NIH vs. NSF의 비대칭적 효과는 펀딩 기관의 평가 문화와 LLM 효과의 상호작용을 시사하며, 기관별 차별화된 LLM 정책 수립의 근거를 제공
- 생산성 향상이 hit 논문보다 일반 논문에 집중된다는 발견은 LLM이 과학의 양적 성장에는 기여하나 획기적 발견에는 제한적임을 시사

## Limitation

### 저자들이 언급한 한계
- 2개 R1 대학의 기밀 데이터에 한정되어 다양한 기관 유형(소규모 대학, 국립연구소 등)으로의 일반화 한계

### 자체판단 아쉬운 점
- LLM 관여도 측정 방법의 타당성 — LLM 사용을 텍스트 특징으로 정확히 감지할 수 있는지
- 상관관계 연구의 한계 — LLM 사용이 더 나은 제안서를 만드는 것인지, 이미 좋은 제안서를 쓰는 연구자가 LLM을 더 잘 활용하는지의 인과 방향 불명확
- 기밀 데이터 접근의 독점성 — 재현 불가능한 데이터가 결과 신뢰성 검증을 어렵게 함

### 후속 연구
- 더 많은 기관과 국가로 확장하여 LLM 사용 패턴의 다양성 분석
- LLM이 실제로 제안서 내용을 변화시키는지(내용 분석)에 대한 질적 연구 보완
- 장기적으로 LLM 확산이 과학 포트폴리오 다양성에 미치는 영향 추적

## 평가

| 항목 | 점수 |
|------|------|
| Novelty | 5/5 |
| Technical Soundness | 4/5 |
| Significance | 5/5 |
| Clarity | 4/5 |
| Overall | 5/5 |

**총평**: 기밀 펀딩 제안서 데이터를 활용하여 LLM이 연방 연구 펀딩 파이프라인에 미치는 영향을 최초로 대규모로 분석한 시의적절하고 중요한 연구다. LLM이 의미론적 독특성을 낮추고 NIH에서만 성공률을 높인다는 발견은 AI 시대 과학 포트폴리오 거버넌스에 직접적 함의를 가지며, 데이터 접근의 희귀성이 연구의 가치를 더욱 높인다.
