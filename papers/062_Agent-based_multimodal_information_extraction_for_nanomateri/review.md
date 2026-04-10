---
title: "062_Agent-based_multimodal_information_extraction_for_nanomateri"
authors:
  - "R. Odobesku"
  - "K. Romanova"
  - "S. Mirzaeva"
  - "O. Zagorulko"
  - "R. Sim"
date: "2025"
doi: "10.1038/s41524-025-01674-7"
arxiv: ""
score: 4.0
essence: "nanoMINER은 대규모 언어모델(LLM)과 멀티모달 분석을 결합하여 나노물질 관련 과학 논문에서 구조화된 데이터를 자동으로 추출하는 다중 에이전트 시스템이다. 기존의 수동 데이터 수집을 자동화하면서도 높은 정확도(nanozyme의 경우 0.98)를 달성한다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/Specialized_Domain_Agents"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Odobesku et al._2025_Agent-based multimodal information extraction for nanomaterials.pdf"
---

# Agent-based multimodal information extraction for nanomaterials

> **저자**: R. Odobesku, K. Romanova, S. Mirzaeva, O. Zagorulko, R. Sim | **날짜**: 2025 | **DOI**: [10.1038/s41524-025-01674-7](https://doi.org/10.1038/s41524-025-01674-7)

---

## Essence

nanoMINER은 대규모 언어모델(LLM)과 멀티모달 분석을 결합하여 나노물질 관련 과학 논문에서 구조화된 데이터를 자동으로 추출하는 다중 에이전트 시스템이다. 기존의 수동 데이터 수집을 자동화하면서도 높은 정확도(nanozyme의 경우 0.98)를 달성한다.

## Motivation

- **Known**: 최근 LLM과 멀티모달 모델(GPT-4V, GPT-4o)의 발전으로 자연언어처리와 개체명 인식(NER) 성능이 크게 향상되었으며, 재료과학 분야에서의 데이터 추출 가능성이 인정되고 있다.

- **Gap**: 기존 접근법들(CHEMDBNER, NERRE, Sun et al.의 ChatGPT 기반 방법)은 ① 제한된 텍스트 세그먼트만 처리하여 문맥을 놓치고, ② 도표 해석에 인간 개입이 필요하며, ③ 동일 논문 내 개별 실험 구분 불가, ④ 완전한 논문 처리 불가라는 한계가 있다.

- **Why**: 과학 문헌의 지수적 증가와 재료과학 분야의 빠른 발전으로 자동화된 고정밀 데이터 추출이 필수적이다. 특히 화학 명명법의 복잡성과 교차 도메인 용어의 존재가 자동 추출을 어렵게 한다.

- **Approach**: 다중 에이전트 아키텍처 기반의 nanoMINER 시스템을 제안하여, 조정 에이전트(Main agent)가 NER 에이전트와 비전 에이전트를 오케스트레이션하며, YOLO와 GPT-4o를 활용해 텍스트와 시각 정보를 통합 처리한다.

## Achievement

![Figure 1](figures/fig1.webp)
*nanoMINER: 다중 에이전트 시스템의 구조로 PDF 입력부터 구조화된 데이터 출력까지의 전체 파이프라인 표시*

1. **나노물질 데이터 추출**: 19개 논문의 25개 실험에서 화학식, 결정계, 크기, 표면 개질 등의 매개변수를 추출했으며, 화학식과 코팅 분자에서 정규화된 Levenshtein 거리가 거의 0에 가까운 수준(~0.0)의 정확도 달성, 코팅 분자 무게 추출에서 0.66의 정밀도 달성

2. **나노자임 데이터 추출**: Km, Vmax, 최소/최대 기질 농도(Cmin, Cmax)에 대해 0.96 이상의 정밀도, 특히 kinetic parameter에서 0.98의 거의 완벽에 가까운 정밀도 달성

3. **기준 모델과의 비교**: 더 오래된 GPT-4o를 Main agent로 사용함에도 불구하고, 최신 GPT-4.1과 추론 모델(o3-mini, o4-mini)을 포함한 모든 기준 LLM을 평균 정밀도, 재현율, F1 스코어에서 지속적으로 상회

4. **암묵적 정보 추출**: 화학식으로부터 결정계를 추론하는 능력을 시연하여, 명시적 정보뿐만 아니라 암묵적 데이터도 추출 가능함을 입증

## How

![Figure 2](figures/fig2.webp)
*나노물질 데이터 추출 성능: 다양한 매개변수에 대한 정밀도, 재현율, F1 스코어 비교*

- **PDF 처리**: 입력 PDF에서 텍스트, 이미지, 플롯을 추출하여 모든 데이터 모달리티 확보

- **시각 정보 추출**: YOLO 모델을 통해 도표, 테이블, 화학식 구조 등의 객체 감지 및 식별, GPT-4o로 추출된 시각 정보를 텍스트 설명과 링크

- **텍스트 분할**: 원본 텍스트를 2048 토큰 청크로 분할하여 다양한 시스템 구성 요소의 효율적 처리 가능

- **ReAct 에이전트**: GPT-4o 기반의 Main agent가 ReAct 프레임워크로 다른 에이전트를 관리, function-calling 수행, 정보 통합

- **NER 에이전트**: 나노물질 논문에 맞게 미세조정된 Mistral-7B 및 Llama-3-8B 모델로 구성된 LLM 기반 에이전트가 중요 개체 추출, 생성된 딕셔너리로 Main agent의 정밀도 향상

- **비전 에이전트**: GPT-4o 기반으로 표준 PDF 추출 도구가 파싱할 수 없는 차트 및 비표준 테이블의 정확한 처리, Main agent에 추가 정보 제공

- **정보 통합 및 집계**: 모든 에이전트로부터의 출력을 aggregation하여 구조화되고 일관된 포맷의 최종 결과 생성

## Originality

- **다중 에이전트 오케스트레이션**: 단순한 파이프라인이 아닌 조정 에이전트 중심의 구조로, 텍스트와 비전 처리 간의 유연한 상호작용과 도표 데이터와 텍스트 설명의 조화 가능

- **완전 문서 처리**: 기존 방법과 달리 전체 논문을 맥락 손실 없이 처리하여, 논문 내 개별 실험 구분 및 종합적 데이터 추출 가능

- **멀티모달 통합**: YOLO, GPT-4o, 미세조정된 NER 모델을 조화롭게 결합하여 텍스트, 도표, 차트 등 다양한 정보원 활용

- **도메인 특화 미세조정**: 나노물질 분야에 맞게 Mistral-7B과 Llama-3-8B을 미세조정하여 화학 개체 추출의 정확도 향상

- **비교 우위**: 더 신규 LLM 모델들도 능가하는 성능 입증으로, 에이전트 분해와 오케스트레이션의 가치 증명

## Limitation & Further Study

- **데이터셋 규모**: 나노물질(19개) 및 나노자임(미명시)의 상대적으로 제한된 평가 데이터셋 규모로, 대규모 다양한 문헌에 대한 일반화 가능성 검증 필요

- **모델 선택 편향**: Main agent로 상대적으로 구형인 GPT-4o를 사용했으며, GPT-4.1이나 더 신규 모델 통합 시 추가 성능 향상 가능성 미탐색

- **오류 전파**: 각 에이전트의 오류가 최종 출력에 누적될 수 있는 메커니즘에 대한 상세한 분석 및 오류 정정 전략 부족

- **비용-효율성 분석**: 시스템의 계산 비용, API 호출 비용 등에 대한 경제성 분석 미포함

- **다른 재료과학 분야로의 확장**: 현재 나노물질과 나노자임에 제한되어 있으며, MOF, 고분자 재료, 2D 물질 등 다른 분야로의 일반화 연구 필요

- **사람-기계 협력**: 사용자 피드백을 통한 모델 지속적 개선, 신뢰도 스코어 제공 등의 상호작용적 개선 메커니즘 개발 필요


## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: nanoMINER은 다중 에이전트 오케스트레이션을 통해 과학 문헌에서의 구조화된 데이터 추출을 효과적으로 자동화한 의미 있는 연구이며, 향후 재료과학 및 생의학 분야에서 데이터 기반 발견을 가속화할 잠재력을 보유하고 있다. 다만 더 광범위한 재료 클래스에 대한 일반화 검증과 실제 도입 시 비용-효율성 분석이 필요하다.

## Related Papers

- 🔄 다른 접근: [[papers/524_MatViX_Multimodal_Information_Extraction_from_Visually_Rich/review]] — nanoMINER와 MatViX는 모두 과학 논문에서 구조화된 정보 추출을 다루지만, 나노물질 특화와 시각적 정보 처리라는 서로 다른 초점을 가집니다.
- 🔗 후속 연구: [[papers/193_CellAgent_An_LLM-driven_Multi-Agent_Framework_for_Automated/review]] — 나노물질 정보 추출을 위한 nanoMINER는 CellAgent의 세포 데이터 자동화 기법을 재료과학 영역으로 확장하여 멀티모달 과학 데이터 처리의 새로운 응용을 제시합니다.
