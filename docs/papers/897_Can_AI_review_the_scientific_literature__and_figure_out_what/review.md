---
title: "897_Can_AI_review_the_scientific_literature__and_figure_out_what"
authors:
  - "Helen Pearson"
date: "2024.11"
doi: "10.1038/d41586-024-03676-9"
arxiv: ""
score: 4.0
essence: "AI를 활용한 과학 문헌 검토 자동화의 가능성과 한계를 탐색하며, 대규모 언어 모델(LLM)이 문헌 종합에 도움이 될 수 있으나 신뢰성과 정확성 문제가 남아있음을 보여준다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/LLM_Review_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Pearson_2024_Can AI review the scientific literature — and figure out what it all means.pdf"
---

# Can AI review the scientific literature — and figure out what it all means?

> **저자**: Helen Pearson | **날짜**: 2024-11-13 | **DOI**: [10.1038/d41586-024-03676-9](https://doi.org/10.1038/d41586-024-03676-9)

---

## Essence


AI를 활용한 과학 문헌 검토 자동화의 가능성과 한계를 탐색하며, 대규모 언어 모델(LLM)이 문헌 종합에 도움이 될 수 있으나 신뢰성과 정확성 문제가 남아있음을 보여준다.

## Motivation

- **Known**: 과학자들은 수십 년간 연구 논문 검토 자동화를 시도해 왔으며, 기계학습과 AI 알고리즘을 활용해 논문 검색과 데이터 추출을 지원해 왔다. ChatGPT 등 LLM의 출현으로 이 분야에 새로운 관심이 촉발되었다.
- **Gap**: 현재 AI 도구는 서술적 문헌 검토(narrative review)는 부분적으로 자동화할 수 있으나, 엄격한 기준의 체계적 검토(systematic review)는 완전 자동화가 불가능하며, 환각(hallucination)과 부정확성 문제가 해결되지 않았다.
- **Why**: 과학 문헌의 폭발적 증가로 인해 연구자들이 모든 관련 논문을 검토하기 불가능해졌으며, 효율적인 문헌 종합은 의료 의사결정 등에서 환자 치료 지침 결정에 영향을 미쳐 매우 중요하다.
- **Approach**: FutureHouse의 PaperQA2 같은 검색 강화 생성(retrieval-augmented generation) 기술과 Consensus, Elicit 같은 AI 기반 과학 검색 엔진을 개발하여, 논문의 전체 텍스트 접근과 출처 기반 요약을 통해 정확성을 향상시키는 방식을 시도하고 있다.

## Achievement


- **PaperQA2의 성능**: FutureHouse의 AI 시스템이 17,000개 인간 유전자에 대한 위키백과 스타일 항목을 생성했으며, 인간 작성 항목보다 '추론 오류'가 절반 수준이었다.
- **체계적 검토 시간 단축**: Glasziou 팀이 체계적 검토 완성 시간을 9일에서 5일로 단축하는 기록을 달성했다.
- **부분 자동화 도구**: RobotSearch, RobotReviewer, Scite 등 논문 필터링, 편향 위험 평가, 주장 검증 등 체계적 검토의 특정 단계를 자동화하는 도구들이 개발되었다.
- **효율성 향상**: Elicit와 Research Kick 같은 도구가 논문 스크리닝, 데이터 추출, 섹션별 통찰 추출 등을 자동화하여 검토 프로세스의 노동 시간을 대폭 감소시킨다.

## How


- 검색 강화 생성(RAG) 기술: 사전 선택된 논문 모음을 LLM에 업로드하여 그 논문들로부터만 정보 추출, 환각 감소
- 다단계 검색 프로세스: 초기 검색 결과를 바탕으로 추가 인용과 핵심 구문을 추적하는 정교한 알고리즘 적용
- 전체 텍스트 접근: 초록만이 아닌 논문 전체 텍스트를 분석하여 더 정확한 종합 실현
- 출처 기반 요약: LLM이 요약 시 출처를 명시하도록 설정하여 추적성 확보
- 인간 검증: 생성된 내용을 PhD 및 박사후 생물학자 패널이 검증하여 정확성 평가
- 단계별 자동화: 논문 필터링, 편향 위험 평가, 데이터 추출 등 체계적 검토의 25개 단계 중 일부만 선택적 자동화

## Originality

- 대규모 언어 모델을 과학 문헌 종합에 적용한 새로운 시도로, 기존 기계학습 도구와 달리 전체 텍스트 분석 능력을 활용
- AI 생성 내용이 인간 작성 내용보다 추론 오류가 적다는 반직관적 발견 제시
- 검색 강화 생성 기술을 통해 LLM의 고질적 문제인 환각을 부분적으로 해결하는 실용적 접근법 제안
- FutureHouse의 오픈소스 PaperQA2는 기존 상용 도구와 달리 투명성과 재현성을 강조

## Limitation & Further Study

- **완전 자동화 불가능성**: 체계적 검토는 25개 이상의 신중한 단계를 필요로 하며, 현재 AI 도구는 부분 자동화만 가능하고 전문가 판단이 여전히 필수
- **환각 문제 지속**: 검색 강화 생성으로 감소했으나 완전히 제거되지 않으며, 비실존 학술 참고문헌 생성 위험 남존
- **접근성 제약**: 많은 도구가 공개 논문과 초록만 검색 가능하며, 유료 논문 전체 텍스트 접근은 계산 비용이 매우 높음
- **품질 관리 우려**: AI 도구로 인한 부정확하고 오도하는 검토가 문헌을 오염시킬 우려, 수십 년간 축적된 증거 종합의 좋은 관행이 훼손될 위험
- **계산 비용과 속도**: PaperQA2 같은 고급 시스템은 분 단위 처리 시간과 높은 컴퓨터 비용 필요
- **후속 연구 필요**: 기술 성숙도 향상, 도구 광범위 채택, 의료 임상 의사결정 활용 검증, 검토 품질 기준 재정의 필요

## Evaluation

- Novelty: 3/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 이 논문은 과학 문헌 검토의 AI 자동화 현황을 균형잡힌 시각으로 다루며, 기술의 진전된 가능성과 함께 완전 자동화의 현실적 한계, 품질 관리 문제 등을 충분히 지적한다. 연구 종합의 효율성 향상은 중요하지만, 과학적 정확성과 투명성의 기준 유지가 우선되어야 함을 강조하는 신중한 접근이 돋보인다.

## Related Papers

- 🔗 후속 연구: [[papers/080_AI_is_transforming_peer_review__and_many_scientists_are_worr/review]] — AI 기반 문헌 검토의 한계를 동료평가 변화라는 더 구체적 맥락에서 확장한다
- 🏛 기반 연구: [[papers/510_Llms_for_literature_review_Are_we_there_yet_arXiv_preprint_a/review]] — LLM의 문헌 검토 능력에 대한 기초적 평가를 제공한다
- 🧪 응용 사례: [[papers/732_Scireviewgen_a_large-scale_dataset_for_automatic_literature/review]] — 자동 문헌 검토 생성의 실제 적용 사례와 데이터셋을 제공한다
- 🏛 기반 연구: [[papers/080_AI_is_transforming_peer_review__and_many_scientists_are_worr/review]] — AI 문헌 검토의 기초적 문제점들이 동료평가 시스템 전반의 우려로 확장된다
- 🧪 응용 사례: [[papers/021_A_Review_on_Scientific_Knowledge_Extraction_using_Large_Lang/review]] — 의료 분야에서 LLM 기반 문헌 검토의 구체적 적용 가능성과 한계를 다룬다
