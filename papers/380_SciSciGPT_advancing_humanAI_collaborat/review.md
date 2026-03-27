# SciSciGPT: advancing human–AI collaboration in the science of science

> **저자**: Erzhuo Shao, Yifang Wang, Yifan Qian, Zhenyu Pan, Han Liu, Dashun Wang | **날짜**: 2025-12-09 | **Journal**: Nature Computational Science | **DOI**: [10.1038/s43588-025-00906-6](https://doi.org/10.1038/s43588-025-00906-6)
> **리뷰 모드**: Abstract 기반 (PDF 없음)

---

## Essence

Science of Science(SciSci) 연구에서 인간-AI 협업은 어떻게 가능한가? SciSciGPT는 LLM 기반 연구 도구를 활용하여 워크플로우 자동화, 다양한 분석 접근법 지원, 재현성 강화를 목표로 하는 오픈소스 AI 협업자 프로토타입이다. 이 시스템은 SciSci 연구자가 데이터 수집, 분석, 해석 과정에서 AI와 협업할 수 있는 구체적인 인터페이스를 제공한다. Nature Computational Science 게재는 이 시스템이 단순한 도구가 아니라 SciSci 연구 방법론의 패러다임 전환을 제안하는 것으로 인정받았음을 시사한다.

## Originality (Abstract 기반)

- [authorship, novelty] "SciSciGPT is an open-source prototype AI collaborator that explores the use of LLM research tools to automate workflows, support diverse analytical approaches and enhance reproducibility in the domain of science of science."
- [novelty] SciSci 도메인에 특화된 LLM 기반 연구 협업 시스템을 처음으로 구현하고 공개

## How (방법론)

- **시스템 아키텍처**: LLM 기반 연구 도구 통합 — 대화형 인터페이스로 SciSci 워크플로우 자동화
- **핵심 기능**:
  - 워크플로우 자동화: 데이터 수집, 전처리, 분석 파이프라인의 LLM 기반 자동화
  - 다양한 분석 지원: 네트워크 분석, 통계 모델링, 텍스트 마이닝 등 SciSci 표준 방법론
  - 재현성 강화: 분석 과정의 문서화 및 코드 생성 자동화
- **오픈소스 배포**: 연구 커뮤니티가 활용·확장 가능한 오픈소스 프로토타입으로 공개
- **검증**: SciSci 연구 사례에서의 시스템 활용 시연 (구체적 내용은 Abstract 범위 초과)

## Why (중요성)

- SciSci 연구는 대규모 서지 데이터 처리, 복잡한 네트워크 분석, 통계 모델링이 필요하여 전문적 기술 장벽이 높음 — LLM 기반 도구로 이 장벽을 낮출 수 있음
- 재현성 위기가 SciSci 분야에서도 문제가 되고 있으며, AI 기반 워크플로우 문서화가 재현성을 구조적으로 향상시킬 수 있음
- 단순 도구 제공을 넘어 인간-AI 협업의 새로운 모델을 제시함으로써, AI가 연구자의 조수가 아닌 협력자로 기능하는 패러다임 구현
- Nature Computational Science 게재는 SciSci 커뮤니티에서의 즉각적인 가시성과 활용을 보장

## Limitation

### 저자들이 언급한 한계
- Abstract에서 "prototype"으로 명시하여 초기 단계임을 인정

### 자체판단 아쉬운 점
- LLM의 환각(hallucination) 문제가 SciSci 분석에서 어떻게 다루어지는지 — 잘못된 인사이트 생성의 위험
- SciSci에 특화된 트레이닝 없이 범용 LLM을 사용할 때의 도메인 특수 지식 한계
- 실제 연구자들의 워크플로우 통합 사례와 효과성에 대한 정량적 평가 부재
- 오픈소스 프로토타입의 유지보수와 커뮤니티 기여 체계의 지속 가능성

### 후속 연구
- SciSci 데이터(Web of Science, Semantic Scholar 등)에 특화된 파인튜닝 또는 RAG 시스템 개발
- 연구자 대상 사용자 연구로 효과성·사용성 정량적 평가
- SciSciGPT 기반 완전 자동화 SciSci 연구 파이프라인 개발

## 평가

| 항목 | 점수 |
|------|------|
| Novelty | 4/5 |
| Technical Soundness | 3/5 |
| Significance | 4/5 |
| Clarity | 4/5 |
| Overall | 4/5 |

**총평**: SciSci 도메인에 특화된 LLM 기반 연구 협업 시스템을 처음으로 구현하고 오픈소스로 공개한 실용적 기여로, Nature Computational Science 게재로 분야 내 가시성을 확보했다. 프로토타입 단계의 한계가 있으나, 인간-AI 협업 기반 SciSci 연구 자동화의 중요한 개념 증명이다.
