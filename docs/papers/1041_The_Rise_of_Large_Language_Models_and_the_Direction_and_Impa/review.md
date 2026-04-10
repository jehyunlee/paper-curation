---
title: "1041_The_Rise_of_Large_Language_Models_and_the_Direction_and_Impa"
authors:
  - "Yifan Qian"
  - "Zhe Wen"
  - "Alexander C. Furnas"
  - "Yue Bai"
  - "Erzhuo Shao"
date: "2026.01"
doi: "10.48550/arXiv.2601.15485"
arxiv: ""
score: 4.0
essence: "대규모 언어 모델(LLM)이 2023년 이후 급격히 확산되면서 연방 연구 자금 신청 제안서의 의미론적 독창성을 감소시키고 있으며, 이러한 변화가 NIH에서는 제안 성공률과 논문 출판량 증가와 연관되지만 NSF에서는 그러한 연관성이 관찰되지 않음을 보여준다."
tags:
  - "cat/Science_of_Science_Research"
  - "sub/AI_and_Large_Language_Models"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Qian et al._2026_The Rise of Large Language Models and the Direction and Impact of US Federal Research Funding.pdf"
---

# The Rise of Large Language Models and the Direction and Impact of US Federal Research Funding

> **저자**: Yifan Qian, Zhe Wen, Alexander C. Furnas, Yue Bai, Erzhuo Shao, Dashun Wang | **날짜**: 2026-01-21 | **DOI**: [10.48550/arXiv.2601.15485](https://doi.org/10.48550/arXiv.2601.15485)

---

## Essence

![Figure 1](figures/fig1.webp)

*Fig. 1: Rapid rise and bimodal distribution of LLM use in US federal research funding. (a-d) Corpus-level*

대규모 언어 모델(LLM)이 2023년 이후 급격히 확산되면서 연방 연구 자금 신청 제안서의 의미론적 독창성을 감소시키고 있으며, 이러한 변화가 NIH에서는 제안 성공률과 논문 출판량 증가와 연관되지만 NSF에서는 그러한 연관성이 관찰되지 않음을 보여준다.

## Motivation

- **Known**: 연방 연구 자금이 미국 과학 기업의 방향, 다양성, 영향력을 형성하며, LLM이 과학 저술과 평가에서 급속히 확산되고 있다.
- **Gap**: LLM의 급속한 보급에도 불구하고, 연방 자금 지원 파이프라인에서 LLM 사용이 어떻게 확산되고 있으며 연구 아이디어의 선정과 다양성에 어떤 영향을 미치는지에 대한 체계적인 증거가 부족하다.
- **Why**: 연방 자금 결정은 출판, 채용, 인정 등에 앞서 어떤 과학 아이디어를 추구할 것인지를 결정하므로, LLM 도입의 영향을 이해하는 것은 과학 정책, 연구 다양성, 공적 자금 투자의 책임성 측면에서 매우 중요하다.
- **Approach**: NSF와 NIH의 비공개 제안 제출 데이터(2개 R1 대학, 2021-2025)와 공개 수상 데이터를 결합하여 LLM 탐지 방법을 적용하고, LLM 사용과 의미론적 독창성, 제안 성공률, 출판 산출물 간의 관계를 분석한다.

## Achievement


- **LLM 사용의 급속한 확산**: ChatGPT 대중화(2023년)와 일치하여 NSF와 NIH 모두에서 LLM 관여도(α)가 급격히 증가
- **이분 분포 패턴**: 개별 제안서 수준에서 LLM 사용이 최소 사용과 실질적 사용(약 10-15%) 사이의 명확한 분리를 보임
- **의미론적 독창성 감소**: LLM 사용이 높을수록 의미론적 독창성이 일관되게 감소하고 최근 자금 지원 프로젝트와 유사성 증가
- **기관 의존적 결과**: NIH에서는 LLM 사용이 제안 성공률과 후속 출판 산출량 증가와 양의 상관관계를 보이지만 NSF에서는 유의미한 연관성 미관찰
- **제한된 영향력 증진**: NIH에서의 생산성 이득이 저인용 논문(non-hit papers)에 집중되고 고인용 논문에서는 이득 미관찰

## How


- LLM 탐지: Liang et al.의 확립된 방법을 적용하여 human-written 텍스트와 GPT-3.5-turbo가 생성한 텍스트의 단어 분포 비교
- 코퍼스 수준 분석: 각 월과 인접 2개월의 제안서를 병합하여 LLM 변경 문장 비율(α) 추정
- 개별 제안서 수준 분석: 각 제안서 초록에 대해 개별적으로 α 추정하여 이질성과 관계성 분석
- 의미론적 독창성 평가: 제안서가 최근 자금 지원 작업과 얼마나 유사한지를 의미론적 거리로 측정
- 통계 분석: 제안 성공률, 출판 산출물, 인용도 등과의 회귀 분석을 통해 연관성 검토

## Originality

- 비공개 제안 제출 데이터 접근: 자금 지원을 받지 못한 제안서를 포함한 완전한 제안 파이프라인 분석으로 기존 연구의 한계 극복
- 이중 데이터 소스 결합: 비공개 대학 제안 데이터와 공개 수상 데이터를 통합하여 파이프라인의 여러 단계에서 LLM 영향 추적
- 기관 간 비교: NSF와 NIH의 상이한 결과를 통해 기관의 특성과 평가 구조가 LLM 영향을 어떻게 조절하는지 규명
- 과학 정책 관련성: 연방 자금 지원이라는 상류 단계에서의 LLM 영향 분석으로 과학 다양성과 장기 영향에 대한 정책적 함의 도출

## Limitation & Further Study

- 제한된 기관 범위: 2개의 R1 대학 데이터만 사용하여 전국 단위 일반화에 제한
- LLM 탐지 방법의 한계: 특정 LLM 모델(GPT-3.5)을 기반으로 학습되어 다른 LLM 모델의 사용 패턴 포착에 제한적
- 인과성 규명 부족: 관찰된 상관관계가 LLM 사용의 직접적인 결과인지, 아니면 다른 혼재 변수(confounding variable)의 결과인지 명확히 구분되지 않음
- 단기 평가: 2025년 초까지의 데이터만 사용하여 LLM 도입의 장기적 영향 평가 불가
- 후속연구 방향: (1) 더 많은 기관과 학문 분야에서의 LLM 사용 패턴 조사, (2) 제안 평가자의 관점에서 LLM 사용이 평가에 미치는 영향 연구, (3) LLM 사용으로 인한 연구 다양성 감소가 과학적 혁신에 미치는 장기 영향 추적

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 이 논문은 LLM이 연방 연구 자금 지원 파이프라인에 미치는 영향을 최초로 대규모 실증 데이터로 분석한 중요한 연구로, 과학 정책과 연구 거버넌스에 시급한 함의를 제공하며 과학의 다양성과 혁신성을 둘러싼 중대한 쟁점을 제기한다.

## Related Papers

- 🔗 후속 연구: [[papers/1077_Quantifying_large_language_model_usage_in_scientific_papers/review]] — LLM 사용률 정량화 방법론을 통해 연구 제안서뿐만 아니라 학술논문 전반의 LLM 영향을 더 체계적으로 측정할 수 있다.
- ⚖️ 반론/비판: [[papers/953_Do_Large_Language_Models_Reduce_Research_Novelty_Evidence_fr/review]] — LLM이 연구의 참신성을 감소시키는지에 대한 상반된 관점을 제시하여 연방 자금 지원에 미치는 영향을 비판적으로 검토한다.
