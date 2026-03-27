# Funding the Frontier: Visualizing the Broad Impact of Science and Science Funding

> **저자**: Yifang Wang, Yifan Qian, Xiaoyu Qi, Yian Yin, Shengqi Dang, Ziqing Qian, Benjamin F. Jones, Nan Cao, Dashun Wang | **날짜**: 2025-09-19 | **Journal**: arXiv preprint | **DOI**: [10.48550/arXiv.2509.16323](https://doi.org/10.48550/arXiv.2509.16323)
> **리뷰 모드**: Abstract 기반 (PDF 없음)

---

## Essence

과학 펀딩의 광범위한 사회적 영향을 어떻게 가시화할 수 있는가? 이 논문은 700만 연구과제를 1억 4천만 논문, 1억 6천만 특허, 1,090만 정책 문서, 80만 임상시험, 580만 뉴스피드와 연결하고 18억 인용 링크를 통합한 대규모 데이터 컬렉션 위에 시각 분석 시스템 **"Funding the Frontier(FtF)"**를 구축했다. 전문가 인터뷰와 사례 연구를 통한 평가에서, FtF는 연구자·펀더·정책 입안자·대학 지도자의 핵심 분석 수요를 충족하면서 예측 모델까지 통합하는 다면적 영향 분석 플랫폼으로 검증되었다.

## Originality (Abstract 기반)

- [authorship, novelty] "we present Funding the Frontier (FtF), a visual analysis system for researchers, funders, policymakers, university leaders, and the broad public."
- [authorship, action] "The system is built on a massive data collection that connects 7M research grants to 140M scientific publications, 160M patents, 10.9M policy documents, 800K clinical trials, and 5.8M newsfeeds, with 1.8B citation linkages among these entities."
- [novelty] "The system incorporates diverse impact metrics and predictive models that forecast future investment opportunities into an array of coordinated views."

## How (방법론)

- **데이터 통합**: 700만 연구과제 → 논문(1.4억) + 특허(1.6억) + 정책문서(1,090만) + 임상시험(80만) + 뉴스피드(580만), 18억 인용 링크로 연결
- **시각화 프레임워크**: Coordinated Multiple Views — 다양한 영향 지표와 예측 모델을 연동된 시각화 뷰들로 통합
- **영향 지표**:
  - 과학 영향력: 논문 인용
  - 기술 영향력: 특허 인용
  - 정책 영향력: 정책 문서 인용
  - 임상 영향력: 임상시험 연결
  - 미디어 영향력: 뉴스피드 언급
- **예측 모델**: 미래 투자 기회 예측 모델을 시각화 인터페이스에 통합
- **평가**: 전문가 인터뷰 + 사례 연구로 시스템 효과성 및 사용성 검증

## Why (중요성)

- 기존 과학 펀딩 영향 연구는 논문 출판에만 초점을 맞추어 특허·정책·임상·미디어로의 downstream 영향을 무시해 왔음
- 펀더가 희소 자원을 복잡한 연구 환경에 배분할 때 투명하고 포괄적인 영향 평가 도구가 필요하지만 현재 존재하지 않음
- 18억 인용 링크로 연결된 다분야 데이터 통합은 과학적 지식이 사회 전반에 파급되는 복잡한 경로를 처음으로 체계적으로 가시화
- 예측 모델 통합으로 사후 영향 평가를 넘어 사전 투자 기회 발굴이라는 새로운 펀딩 분석 패러다임 제시

## Limitation

### 저자들이 언급한 한계
- 전문가 인터뷰와 사례 연구 기반 평가는 소규모 사용자 집단에 한정 — 대규모 사용자 연구 필요
- 방대한 데이터 수집과 연결 과정에서 데이터 품질 및 누락 문제 가능성 언급

### 자체판단 아쉬운 점
- 18억 링크 구축에서 발생하는 오연결(false links)이 분석 결과를 왜곡할 수 있음
- 예측 모델의 정확도와 신뢰 구간에 대한 구체적 검증이 얼마나 이루어졌는지 불명확
- 영향 지표의 이질성(논문 인용 vs. 정책 인용 vs. 미디어 언급)을 어떻게 통합적으로 해석하는지에 대한 방법론적 명확성 필요

### 후속 연구
- 다양한 사용자 집단(연구자, 정책 입안자, 대중)에 대한 대규모 사용성 연구
- 예측 모델의 장기적 정확도 추적 및 개선
- 다국적 펀딩 시스템으로 확장하여 글로벌 과학 투자 지형도 구축

## 평가

| 항목 | 점수 |
|------|------|
| Novelty | 4/5 |
| Technical Soundness | 4/5 |
| Significance | 5/5 |
| Clarity | 4/5 |
| Overall | 4/5 |

**총평**: 700만 연구과제와 다양한 downstream 영향 지표를 18억 인용 링크로 통합한 전례 없는 규모의 과학 영향 분석 플랫폼으로, 과학 펀딩의 광범위한 사회적 파급을 처음으로 체계적으로 가시화한다. 데이터 품질과 예측 모델 검증의 엄밀성이 향후 과제이나, Science of Science와 과학 정책 연구의 인프라 혁신에 중요한 기여를 한다.
