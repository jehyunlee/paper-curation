---
title: "057_aedfact_Scientific_fact-checking_made_easier_via_semi-automa"
authors:
  - "Enes Altuncu"
  - "Jason R.C. Nurse"
  - "Meryem Bagriacik"
  - "Sophie Kaleba"
  - "Haiyue Yuan"
date: "2023"
doi: "arXiv:2305.07796"
arxiv: ""
score: 3.5
essence: "본 논문은 웹 브라우저 확장 프로그램인 aedFaCT를 제시하여, 뉴스 기사의 주요 키워드를 자동으로 추출하고 이를 바탕으로 신뢰할 수 있는 뉴스 매체의 전문가 의견과 동료 심사 학술논문을 반자동으로 검색함으로써 과학적 팩트체킹을 용이하게 한다. 사용자는 수집된 다양한 전문가 의견을 통해 의심스러운 과학적 주장의 진위를 판단할 수 있다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Fact_Verification_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Zhou et al._2023_aedfact Scientific fact-checking made easier via semi-automatic discovery of relevant expert opinio.pdf"
---

# aedFaCT: Scientific fact-checking made easier via semi-automatic discovery of relevant expert opinions

> **저자**: Enes Altuncu, Jason R.C. Nurse, Meryem Bagriacik, Sophie Kaleba, Haiyue Yuan, Lisa Bonheme, Shujun Li | **날짜**: 2023 | **DOI**: [arXiv:2305.07796](https://arxiv.org/abs/2305.07796)

---

## Essence

![Figure 1](figures/fig1.webp) *aedFaCT의 시스템 아키텍처*

본 논문은 웹 브라우저 확장 프로그램인 aedFaCT를 제시하여, 뉴스 기사의 주요 키워드를 자동으로 추출하고 이를 바탕으로 신뢰할 수 있는 뉴스 매체의 전문가 의견과 동료 심사 학술논문을 반자동으로 검색함으로써 과학적 팩트체킹을 용이하게 한다. 사용자는 수집된 다양한 전문가 의견을 통해 의심스러운 과학적 주장의 진위를 판단할 수 있다.

## Motivation

- **Known**: 팩트 체크 시 자동화된 방법들이 존재하지만, 다양한 맥락·언어·형식에 대응하기에 불충분하며 인간의 신뢰(trust)와 사용성(usability) 같은 요소를 충분히 고려하지 못함. 전문가(특히 과학자)는 거짓 정보에 대항하는 데 중요한 역할을 하며 사회에서 높은 신뢰도를 갖음.

- **Gap**: 기존의 전문가-기자 협력 체계는 과학적 의사소통의 어려움, 이상치(outlier) 전문가의 존재, 부적절한 전문가 선정 등으로 인해 제한적임. 여러 전문가의 의견을 활용한 팩트체킹 도구의 필요성이 부족함.

- **Why**: 일반 사용자와 전문 팩트체커는 신뢰할 수 있는 정보(학술논문, 팩트체킹 보고서, 주류 뉴스, 위키피디아)를 선호하며, 여러 출처의 전문가 의견을 수집하는 것은 수동 검색에 많은 시간이 소요됨.

- **Approach**: 포커스 그룹 논의를 통해 사용자의 팩트체킹 정신 모델을 분석한 후, 반자동 시스템을 설계하여 키워드 추출, 전문가 의견 및 학술논문 검색, 관련 연구자 식별을 자동화.

## Achievement

![Figure 2](figures/fig2.webp) *키워드 추출 단계의 사용자 인터페이스*

![Figure 3](figures/fig3.webp) *검색된 뉴스 기사의 출력 예시*

![Figure 4](figures/fig4.webp) *검색된 학술논문과 공동저자 정보의 출력 예시*

1. **포커스 그룹 기반 설계**: 연구자, 일반 독자 관점에서 팩트체킹 프로세스를 분석하여, 시스템이 자동으로 처리해야 할 작업(키워드 추출, 증거 검색)과 사용자 판단이 필요한 부분을 명확히 구분.

2. **반자동 팩트체킹 플랫폼**: 대상 기사에서 후보 키워드를 자동 추출하고, 이를 이용해 신뢰할 수 있는 뉴스 매체의 전문가 의견, 동료 심사 논문, 관련 연구자 정보를 통합 검색하여 제시.

3. **실용적 효율성 검증**: 3명의 독립 테스터를 통한 평가에서 aedFaCT가 기존의 수동 검색 기반 팩트체킹보다 빠른 사용자 경험을 제공하면서도 검색된 증거의 질을 유지함을 확인.

## How

- **포커스 그룹 논의 (Section 3)**: 3가지 시나리오(연구자 관점, 일반 독자 관점, 전문가 의견 활용)에서 팩트체킹 프로세스를 체계적으로 분석하여 사용자 요구사항 도출.

- **키워드 추출**: 뉴스 기사에서 자동으로 관련 키워드를 추출하여 검색 쿼리 생성.

- **다중 출처 검색**: 추출된 키워드를 기반으로 (1) 신뢰할 수 있는 뉴스 매체에서 전문가 의견, (2) Google Scholar/PubMed 등에서 동료 심사 학술논문, (3) 관련 영역의 연구자 정보를 자동 검색.

- **사용자 중심 인터페이스**: 검색 결과를 직관적으로 시각화하여 사용자가 쉽게 증거를 평가하고 최종 판단을 내릴 수 있도록 설계.

- **웹 브라우저 확장**: Chrome 기반 확장 프로그램으로 구현하여 기존 뉴스 읽기 워크플로우에 원활히 통합.

## Originality

- 전문가 의견의 자동 발견이라는 새로운 접근: 기존 시스템들(BRENDA, FADE, The Factual)은 주로 자동 검증이나 출처 신뢰도 평가에 초점을 맞췄으나, aedFaCT는 여러 전문가의 의견을 체계적으로 수집하는 데 중점.

- 포커스 그룹 기반의 사용자 연구: 팩트체킹의 정신 모델을 실증적으로 분석하여 시스템 설계에 반영한 인간 중심 접근.

- 반자동 (semi-automatic) 설계 철학: 기계 자동화와 인간 판단을 명확히 구분하여, 신뢰성이 중요한 팩트체킹 업무에서 사용자의 최종 의사결정권을 보장.

- 공개 소스 제공: GitHub에서 소스코드를 공개하여 재현성과 커뮤니티 기여 가능성을 높임.

## Limitation & Further Study

- **포커스 그룹의 제한성**: 3명의 컴퓨터과학 박사과정생(특정 분야 전문가)을 대상으로 한 포커스 그룹은 일반 대중의 행동을 충분히 대표하기 어려움. 더 다양한 배경의 참여자를 포함한 후속 사용자 연구 필요.

- **키워드 추출 정확성**: 자동 키워드 추출의 질이 전체 시스템 성능에 직접 영향을 미치는데, 추출 방법의 정확도에 대한 상세한 평가가 부족.

- **제한된 데이터 소스**: 신뢰할 수 있는 뉴스 매체의 범위가 제한적일 수 있으며, 비영어권 뉴스나 다국어 팩트체킹에 대한 확장성 미흡.

- **이상치 전문가 식별 부재**: 논문에서 지적한 "이상치 전문가(outlier expert)"를 자동으로 감지하거나 필터링하는 메커니즘 부재.

- **평가 규모의 소규모성**: 3명의 테스터만으로 평가하여 통계적 신뢰도와 일반화 가능성이 제한적.

- **향후 과제**: (1) 더 정교한 평판 평가(reputation scoring) 시스템 개발, (2) 사실 검증의 자동화 수준 향상, (3) 다국어 및 다중 모달(multimodal) 팩트체킹으로의 확장, (4) 대규모 사용자 평가 및 실제 팩트체킹 전문가와의 협력 검증.

## Evaluation

- **Novelty**: 3.5/5
  - 전문가 의견의 자동 발견이라는 아이디어는 흥미로우나, 기술적으로는 기존의 정보 검색(IR) 기술 조합에 불과함.

- **Technical Soundness**: 3/5
  - 포커스 그룹 연구는 방법론적으로 제한적이고, 키워드 추출 등 핵심 기술에 대한 상세한 설명이 부족. 평가가 소규모로 제한적.

- **Significance**: 3.5/5
  - 팩트체킹의 실제 필요성과 전문가 역할의 중요성을 잘 동기부여하였으나, 시스템의 실제 영향도와 적용 범위가 아직 검증 부족.

- **Clarity**: 4/5
  - 전반적으로 논문이 명확하고 잘 구성되었으나, 기술 상세(특히 정보 검색 방법)에서 설명이 미흡.

- **Overall**: 3.5/5

**총평**: aedFaCT는 팩트체킹에 인간 중심 설계와 전문가 의견 활용이라는 실용적 관점을 도입한 의미 있는 응용 연구이나, 기술적 혁신성이 제한적이고 평가의 규모와 엄밀성이 불충분하여 학술적 기여도는 중간 정도이다. 특히 포커스 그룹 분석을 바탕으로 한 시스템 설계 방법론은 참고할 만하나, 향후 대규모 실제 사용자 평가와 자동화 기술의 고도화가 필요하다.

## Related Papers

- 🏛 기반 연구: [[papers/685_Robust_claim_verification_through_fact_detection/review]] — 일반적인 사실 검증 방법론을 과학적 맥락에 특화된 형태로 구현한다
- 🔗 후속 연구: [[papers/328_Explainable_biomedical_claim_verification_with_large_languag/review]] — 과학적 팩트체킹을 의료 분야로 확장하고 설명가능성을 추가한다
- 🔄 다른 접근: [[papers/221_Claimver_Explainable_claim-level_verification_and_evidence_a/review]] — 웹 기반 반자동 검색 대신 지식 그래프를 활용한 체계적 주장 검증 방법을 제시한다
- 🧪 응용 사례: [[papers/685_Robust_claim_verification_through_fact_detection/review]] — 사실 검증의 일반적 방법론을 과학적 팩트체킹이라는 구체적 영역에 적용한다
- 🔗 후속 연구: [[papers/221_Claimver_Explainable_claim-level_verification_and_evidence_a/review]] — 반자동 팩트체킹을 더 체계적이고 설명가능한 프레임워크로 발전시킨다
- 🔄 다른 접근: [[papers/328_Explainable_biomedical_claim_verification_with_large_languag/review]] — 웹 기반 반자동 검색 대신 LLM과 SHAP를 결합한 대화형 검증 시스템을 제시한다
