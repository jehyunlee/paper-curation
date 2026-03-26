# Using Artificial Intelligence for Systematic Review: The Example of Elicit

> **저자**: Nathan Bernard, Yoshimasa Sagawa Jr, Nathalie Bier, Thomas Lihoreau, Lionel Pazart, Thomas Tannou
> **학술지**: BMC Medical Research Methodology, 25(1):75, 2025
> **DOI**: [10.1186/s12874-025-02528-y](https://doi.org/10.1186/s12874-025-02528-y)

---

## 한줄 요약 (Essence)
AI 기반 연구 보조 도구 Elicit이 체계적 문헌 고찰(systematic review)의 스크리닝 단계에서 기존 방법론을 대체할 수 있는지를 반복성(repeatability), 정확성(accuracy), 신뢰성(reliability)의 세 기준으로 평가한 연구이다.

---

## 연구 동기 (Motivation)
- 체계적 문헌 고찰은 높은 완결성을 요구하는 시간 집약적 과정으로, AI 도구가 스크리닝, 비뚤림 평가, 데이터 추출 등에 활용되고 있다.
- GPT-3 기반의 Elicit은 의미적 유사성(semantic similarity)을 활용해 키워드 없이도 관련 논문을 검색하고 요약을 생성하는 독특한 기능을 제공한다.
- 기존에 AI 없이 수행한 umbrella review와 Elicit 기반 검색을 동일 조건으로 비교함으로써, AI 보조 스크리닝의 부가가치를 정량적으로 검증하고자 하였다.

---

## 핵심 성과 (Achievement)
- **반복성 부족**: 동일 질의를 3회 반복했을 때 각각 246, 169, 172건으로 결과가 크게 변동하였으며, 3회 합산 후 중복 제거 시 241건이 확인됨.
- **정확성**: 241건 중 제목/초록 스크리닝 후 29건이 전문 검토 대상이 되었고, 최종 6건이 포함됨. Elicit이 찾은 논문은 모두 연구 질문에 관련성이 높았다.
- **신뢰성**: 기존 umbrella review에서 최종 포함된 17건 중 Elicit이 식별한 것은 3건(17.6%)에 불과. 반면 Elicit만이 발견한 3건의 추가 논문이 있었으나, 이들은 umbrella review의 결론을 변경하지 못함.
- AI 도구는 보완적(complementary) 역할로는 유용하지만, 기존 방법론을 완전히 대체하기에는 부족하다는 결론.

---

## 방법론 (How)
1. **검색 설계**: Elicit에 기존 umbrella review와 동일한 연구 질문("What is the effectiveness of smart living environments in supporting ageing in place?")을 입력하고, 논문 유형(systematic review)과 출판 연도(2005~2021) 필터를 적용.
2. **연도별 분할 검색**: 9개 연도별로 검색을 반복하여 Elicit의 "8건 우선 표시" 제한을 우회하고, "show more"로 추가 논문을 모두 수집.
3. **반복성 평가**: 동일 질의를 서로 다른 시간대에 3회 반복(Trial 1~3)하여 결과의 일관성을 비교.
4. **정확성 평가**: Elicit 검색 결과를 기존 umbrella review와 동일한 포함/배제 기준으로 수동 선별.
5. **신뢰성 평가**: 각 선별 단계(제목/초록, 전문, 최종 포함)에서 Elicit과 기존 방법의 결과를 Venn diagram 방식으로 비교.

---

## 독창성 (Originality)
- AI 도구의 체계적 문헌 고찰 활용을 **반복성, 정확성, 신뢰성이라는 세 가지 독립적 기준**으로 분리하여 평가한 최초의 체계적 비교 연구 중 하나이다.
- 실제 출판된 umbrella review를 ground truth로 삼아 Elicit의 성능을 정량적으로 벤치마킹한 점이 실용적이다.
- Elicit이 Semantic Scholar 단일 데이터베이스에 의존한다는 구조적 한계를 실증적으로 드러냈다.

---

## 한계점 (Limitation)
- **단일 연구 질문**: 하나의 umbrella review 주제("smart living environments for ageing in place")에 대해서만 평가하여 일반화에 한계가 있다.
- **단일 AI 도구**: Elicit만 평가하였으며, 다른 AI 스크리닝 도구(ASReview, Rayyan 등)와의 비교가 없다.
- **시점 한정**: 2023년 4월 시점의 Elicit 버전으로 평가되었으며, 이후 도구의 성능 개선이 반영되지 않았다.
- **질문 민감도**: 연구 질문의 문구를 약간 바꾸면 Elicit의 결과와 인용 논문이 달라지는 문제를 지적했으나, 이에 대한 체계적 분석은 수행하지 않았다.
- Elicit이 umbrella review의 프로토콜 논문을 잘못 인용한 사례를 발견했으나, 이러한 hallucination 문제에 대한 심층 분석이 부족하다.

---

## 총평 (Evaluation)
AI 도구를 체계적 문헌 고찰에 적용할 때의 현실적 기대치를 설정하는 데 유용한 실증 연구이다. Elicit이 기존 방법으로 놓친 3건의 관련 논문을 추가로 발견한 점은 보완적 가치를 입증하지만, 17.6%라는 낮은 재현율과 반복 시 결과 변동성은 AI 단독 사용의 위험성을 명확히 보여준다. 다만, 연구 규모가 작고(단일 주제, 단일 도구) 2023년 시점의 평가라는 점에서 현재의 급속히 발전하는 AI 도구 생태계에 대한 일반화에는 주의가 필요하다. 향후 PRISMA-AI 가이드라인의 정립과 함께, 다양한 AI 도구를 복수의 연구 주제에 걸쳐 비교하는 대규모 벤치마크 연구가 기대된다.
