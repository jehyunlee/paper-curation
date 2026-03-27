# Hierarchical Classification of Research Fields in the "Web of Science" Using Deep Learning

> **저자**: Susie Xi Rao, Peter H. Egger, Ce Zhang | **날짜**: 2024-07-25 | **Journal**: arXiv preprint | **arXiv**: [2302.00390](https://arxiv.org/abs/2302.00390) | **DOI**: [10.48550/arXiv.2302.00390](https://doi.org/10.48550/arXiv.2302.00390)
> **리뷰 모드**: Abstract only (PDF 없음)

---

## Essence

논문 초록으로부터 3계층(discipline, field, subfield) 계층적 분류를 딥러닝으로 자동화할 수 있는가? Microsoft Academic Graph(MAG, 2018-05-17) 기준 **1억 6천만 건**의 초록 스니펫을 대상으로, 44개 discipline · 718개 field · 1,485개 subfield의 계층적 레이블을 CNN, RNN, Transformer로 분류한 결과: 단일 레이블 및 다중 레이블 분류 모두에서 **77~78%의 실험에서 90% 이상의 정확도**를 달성했다. 총 3,140개의 실험을 수행하여 모델 성능을 체계적으로 평가했으며, 미래 과학 논문 인덱싱 시스템의 백본으로 제안된다.

## Originality (Abstract 기반)

- [authorship, novelty, action] "This paper presents a hierarchical classification system that automatically categorizes a scholarly publication using its abstract into a three-tier hierarchical label set (discipline, field, subfield) in a multi-class setting."
- [novelty] "The classification system distinguishes 44 disciplines, 718 fields and 1,485 subfields among 160 million abstract snippets."
- [result] "The classification accuracy is > 90% in 77.13% and 78.19% of the single-label and multi-label classifications, respectively."

## How (방법론)

- **데이터**: MAG 1억 6천만 건 초록 스니펫 (2018-05-17 버전), 3계층 레이블 (44 disciplines / 718 fields / 1,485 subfields)
- **모델**: CNN(Convolutional Neural Networks), RNN(Recurrent Neural Networks), Transformer 세 계열
- **학습 방식**: 배치 학습, 모듈화·분산 방식으로 학제 간 및 분야 내 다중 레이블 분류 지원
- **평가**: 총 3,140개 실험, 단일 레이블 및 다중 레이블 설정 모두 평가

## Why (중요성)

- WoS 등 학술 데이터베이스의 수동 분류는 비용과 시간이 크며 일관성이 부족, 자동화된 고정확도 분류가 필요
- 학제 간 분류와 다중 레이블 지원은 현대 연구의 융합적 특성을 반영하는 데 필수적

## Limitation

- MAG 데이터가 2022년 서비스 종료되어 지속적 데이터 업데이트 불가 — OpenAlex 등 대안 데이터소스로의 이전 필요
- 1억 6천만 건 학습을 위한 계산 비용이 매우 높아 재현성 제약
- 3계층 분류 체계가 MAG의 카테고리를 따르므로, 다른 분류 체계(WoS 분야, Scopus ASJC)로의 이전 가능성 불명확

## Further Study

- OpenAlex 또는 Semantic Scholar로 데이터 소스 이전 및 모델 업데이트
- LLM(Large Language Model) 기반 제로샷/퓨샷 분류와의 성능 비교
- 새롭게 출현하는 학제 분야에 대한 오픈 집합 분류(open-set classification) 확장

## 평가

| 항목 | 점수 |
|------|------|
| Novelty | 3/5 |
| Technical Soundness | 4/5 |
| Significance | 4/5 |
| Clarity | 4/5 |
| Overall | 4/5 |

**총평**: 1억 6천만 건 규모의 논문을 3계층 계층적 분류로 자동화하는 대규모 딥러닝 시스템을 체계적으로 구축한 공학적으로 탄탄한 논문이다. MAG 데이터 의존성이 장기 활용의 제약이나, 과학 논문의 자동 분류 인프라로서의 잠재적 가치는 상당하다.
