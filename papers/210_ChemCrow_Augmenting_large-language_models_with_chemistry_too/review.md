---
title: "210_ChemCrow_Augmenting_large-language_models_with_chemistry_too"
authors:
  - "Andres M Bran"
  - "Sam Cox"
  - "Oliver Schilter"
  - "Carlo Baldassari"
  - "Andrew D White"
date: "2023.04"
doi: "N/A"
arxiv: ""
score: 4.2
essence: "대규모 언어 모델(LLM)에 18개의 화학 전문 도구를 통합하여 유기합성, 신약 개발, 재료 설계 등 다양한 화학 작업을 자율적으로 수행할 수 있는 ChemCrow 에이전트를 개발했다. GPT-4를 기반으로 하는 이 시스템은 Thought-Action-Observation 루프를 통해 화학 문제 해결에서 LLM의 고질적 한계를 극복한다."
tags:
  - "cat/Cognitive_AI_Evaluation_and_Benchmarking"
  - "sub/AI_Chemistry_Planning"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Bran et al._2023_ChemCrow Augmenting large-language models with chemistry tools.pdf"
---

# ChemCrow: Augmenting large-language models with chemistry tools

> **저자**: Andres M Bran, Sam Cox, Oliver Schilter, Carlo Baldassari, Andrew D White, Philippe Schwaller | **날짜**: 2023-04-11 | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp)
*그림 1: ChemCrow의 개요 및 도구 집합. (a) 작업 해결 프로세스의 개요. (b) 구현된 18개의 도구 세트*

대규모 언어 모델(LLM)에 18개의 화학 전문 도구를 통합하여 유기합성, 신약 개발, 재료 설계 등 다양한 화학 작업을 자율적으로 수행할 수 있는 ChemCrow 에이전트를 개발했다. GPT-4를 기반으로 하는 이 시스템은 Thought-Action-Observation 루프를 통해 화학 문제 해결에서 LLM의 고질적 한계를 극복한다.

## Motivation

- **Known**: 지난 수십 년간 탁월한 계산 화학 도구들이 개발되었으나, 각각 높은 학습곡선을 가진 고립된 환경에서만 작동하고 있다(RXN for Chemistry, AIZynthFinder 등). LLM은 자연어 처리에서 뛰어난 성능을 보이지만, 화학 관련 작업에서는 IUPAC 명명법 변환, 기본 화학 연산 등에 실패한다.

- **Gap**: 분산된 화학 도구들을 통합하는 단일 플랫폼의 부재로 계산 화학의 잠재력이 미활용되고 있으며, LLM 역시 외부 지식 소스 접근이 불가능하여 과학 응용에 제한적이다.

- **Why**: 전문 화학자의 접근성 향상과 비전문가의 진입 장벽 제거, 그리고 실험 및 계산 화학 간 격차 해소를 통한 과학적 진전이 필요하다.

- **Approach**: ReAct(Reasoning + Acting)과 MRKL 프레임워크를 기반으로 LLM에 화학 특화 도구를 통합한 에이전트 시스템 구축. 18개의 도구(반응 도구, 분자 도구, 안전 도구, 검색 도구, 표준 도구)를 개발하고 클라우드 연결 로봇 합성 플랫폼(RoboRXN)과 연동.

## Achievement

![Figure 2](figures/fig2.webp)
*그림 2: 실험 검증. (a) 사용자가 ChemCrow를 시작하는 스크립트 예시. (b) 티오우레아 유기촉매 쿼리 및 합성. (c) IBM Research RoboRXN 합성 플랫폼. (d) 실험으로 검증된 화합물들*

![Figure 3](figures/fig3.webp)
*그림 3: 신규 색소 발견으로 이어진 인간-AI 협력. 좌측: 인간의 입력 및 행동. 우측: ChemCrow의 행동 및 최종 제안*

1. **자율 화학 합성**: ChemCrow는 "곤충 기피제 합성 계획 및 실행"이라는 단순한 입력으로부터 DEET 및 3개의 티오우레아 유기촉매(Schreiner's, Ricci's, Takemoto's)의 합성을 자율적으로 계획하고 실행했다. RoboRXN 플랫폼에서 4개의 합성이 모두 성공적으로 수행되었으며, ActionCleaner 기능을 통해 유효하지 않은 합성 절차를 자동으로 반복 수정하였다.

2. **인간-AI 협력을 통한 신규 분자 발견**: 머신러닝 모델 학습, 데이터 정제, 특성 예측을 자동으로 수행하여 목표 파장(369nm)에 근접한 신규 색소(E)-3-methyl-4-(2-(3'-(methylsulfonamido)-[1,1'-biphenyl]-4-yl)vinyl)benzoate를 제안했으며, 실험적 합성과 분석을 통해 검증(측정 파장 336nm)되었다.

3. **광범위한 평가**: 14개의 사용 사례에서 ChemCrow와 순수 GPT-4의 성능을 LLM 기반 평가자(EvaluatorGPT)와 전문가 인간 평가를 통해 비교 분석했으며, ChemCrow의 화학 작업 자동화 효과를 입증했다.

## How

![Figure 4](figures/fig4.webp)
*그림 4: 다양한 화학 작업 범위에서 GPT-4와 ChemCrow의 비교 성능*

![Figure 5](figures/fig5.webp)
*그림 5: ChemCrow가 제공하는 안전 지침 예시*

- **에이전트 아키텍처**: Thought-Action-Action Input-Observation 반복 루프 구현
  - Thought: 현재 작업 상태 추론 및 최종 목표와의 연관성 고려
  - Action: 실행할 도구 선택
  - Action Input: 선택된 도구의 입력 파라미터 지정
  - Observation: 도구 실행 결과 수신 및 다음 반복으로 진행

- **18개 도구 세트**:
  - **반응 도구**: ReactionPlanner(합성 경로 계획), ReactionExecute(RoboRXN 플랫폼 연동)
  - **분자 도구**: Name2SMILES(IUPAC 명명법→SMILES 변환), OPSIN 활용
  - **안전 도구**: 화학 물질 안전성 정보 제공
  - **검색 도구**: LitSearch/WebSearch(문헌 및 웹 검색)
  - **표준 도구**: 데이터 처리, 머신러닝 모델 학습

- **평가 방법론**:
  - LLM 기반 평가: EvaluatorGPT가 작업 완수 여부 및 추론 과정 정확성 평가
  - 전문가 인간 평가: 화학자가 결과의 과학적 타당성 검증
  - 혼합 평가: 정량적·정성적 피드백 결합

## Originality

- **최초 통합적 접근**: 분산된 화학 도구들을 단일 LLM 에이전트로 통합하여 유기합성, 신약 개발, 재료 설계 전 영역을 포괄한 첫 시스템
  
- **물리적 실험 연동**: 클라우드 기반 로봇 합성 플랫폼과의 직접 연동으로 LLM이 실제 분자 합성을 수행하는 최초 사례 (기존 연구는 계산 수준에 한정)

- **적응형 자동화**: ActionCleaner를 통해 유효하지 않은 합성 절차를 자동으로 수정하는 자가 교정 메커니즘 개발

- **신규성에 대한 실험적 증거**: 인간-AI 협력을 통해 실제 신규 색소를 발견하고 실험적으로 검증

- **평가 방법론의 혁신**: 화학 작업 평가를 위해 LLM 평가자와 전문가 평가를 결합한 하이브리드 평가 체계 제시

## Limitation & Further Study

- **평가자의 신뢰성 문제**: "놀랍게도 GPT-4 평가자는 명백히 틀린 GPT-4 완성도와 ChemCrow의 성능을 구분하지 못한다"는 발견은 LLM 기반 평가의 한계를 노출. 향후 더욱 정교한 평가 기준이나 다중 전문가 평가 시스템 필요

- **도구 집합의 제한성**: 18개 도구는 여전히 화학의 전 영역을 커버하지 못함. 특히 이론 계산 화학, 분석 화학, 고분자 화학 등 추가 도구 개발 필요

- **인간 개입 필요성**: 부분적으로 여전히 인간의 검증과 개입(예: 합성 결과 확인, 최적화 결정)이 필수적이므로 완전 자동화 달성이 미흡

- **안전성 검증 부족**: 화학 안전성 관련 도구는 포함되었으나, 극도로 위험한 반응이나 물질 취급에 대한 학습 데이터가 제한적일 가능성

- **재현성 및 일반화**: 특정 도구와 플랫폼(RoboRXN, GPT-4)에 의존적이므로 다른 화학 도구나 LLM으로의 이식성 및 일반화 가능성 미검증

- **후속 연구 방향**:
  - 추가 도구 개발 및 자동 도구 탐색 메커니즘 구축
  - 다양한 LLM 모델(Claude, Llama 등)과의 호환성 평가
  - 더욱 강력한 평가 벤치마크 개발 및 표준화
  - 실패 사례에 대한 근본 원인 분석 및 에러 복구 메커니즘 강화

## Evaluation

- **Novelty**: 4.5/5 - 화학 도구와 LLM의 통합은 새로운 접근이지만, ReAct/MRKL 프레임워크 자체는 기존 논문(동시대 연구 포함)을 기반. 물리적 합성 플랫폼 연동은 높은 독창성을 가짐.

- **Technical Soundness**: 4/5 - 전반적으로 견고한 기술 구현이나, 평가 방법론(특히 LLM 평가자의 한계)에서 약점 노출. 자동화 오류 처리(ActionCleaner) 메커니즘은 창의적이나 다른 오류 유형에 대한 일반성 미흡.

- **Significance**: 4.5/5 - 화학 분야에서 LLM 응용의 실질적 영향을 최초로 입증했고, 전문가와 비전문가 모두에게 높은 실용적 가치. 다만 신규 색소 발견은 규모가 제한적이고 산업적 영향은 아직 검증 필요.

- **Clarity**: 4/5 - 전반적으로 명확한 설명과 풍부한 Figure로 이해하기 쉬움. 다만 18개 도구의 상세 기술 사양과 한계, 평가 결과의 정량적 지표가 본문에 충분하지 않음 (부록 참조 필요).

- **Overall**: 4.2/5

**총평**: ChemCrow는 LLM을 화학 도구와 물리적 실험 플랫폼에 효과적으로 연결하여 자율 화학 합성과 신규 분자 발견을 실현한 획기적 연구다. 특히 실험 검증과 인간-AI 협력 사례는 설득력 있으나, LLM 평가자의 신뢰성 문제와 도구 집합의 제한성, 완전 자동화 달성의 미흡함은 향후 개선이 필요한 과제로 남는다.

## Related Papers

- 🔄 다른 접근: [[papers/271_Developing_ChemDFM_as_a_large_language_foundation_model_for/review]] — 화학 AI 에이전트의 다른 구현 방식으로 도구 통합 vs 파운데이션 모델
- 🏛 기반 연구: [[papers/115_Augmenting_large_language_models_with_chemistry_tools/review]] — LLM에 화학 도구 통합의 기본 연구가 ChemCrow의 직접적 기반
- 🔄 다른 접근: [[papers/271_Developing_ChemDFM_as_a_large_language_foundation_model_for/review]] — 화학 분야 LLM의 다른 구현 방식으로 도구 통합 vs 파운데이션 모델 접근
- 🔗 후속 연구: [[papers/461_LARC_Towards_Human-level_Constrained_Retrosynthesis_Planning/review]] — ChemCrow의 화학 도구 증강 언어모델은 LARC의 제약조건 기반 역합성 계획을 더욱 발전시킨 형태입니다
- 🔄 다른 접근: [[papers/047_ActionIE_Action_Extraction_from_Scientific_Literature_with_P/review]] — Python 코드 생성을 통한 화학 행동 추출과 화학 도구로 증강된 대형 언어모델은 모두 과학 문헌의 실험 절차를 자동화하는 서로 다른 접근법입니다
- 🔗 후속 연구: [[papers/316_Enhancing_chemical_reaction_and_retrosynthesis_prediction_wi/review]] — 화학 도구를 활용한 LLM 확장이 ChemDual의 화학 반응 예측 프레임워크와 상호 보완적인 접근법이다.
- 🔗 후속 연구: [[papers/209_ChemAgent_Self-updating_Library_in_Large_Language_Models_Imp/review]] — 화학 추론 능력이 더 포괄적인 화학 도구 활용으로 확장됩니다.
- 🔗 후속 연구: [[papers/176_CACTUS_Chemistry_Agent_Connecting_Tool_Usage_to_Science/review]] — 화학정보학 도구 통합을 화학 증강 대화형 시스템으로 발전시킨 연구
- 🔄 다른 접근: [[papers/115_Augmenting_large_language_models_with_chemistry_tools/review]] — 화학 분야에서 LLM 도구 증강의 다른 접근법과 구현 방식을 비교할 수 있다
- 🔄 다른 접근: [[papers/1106_The_BOS-Lig_Dataset_Accurate_Ligand_Charges_from_a_Consensus/review]] — 화학 대응 LLM 확장과 정확한 리간드 전하 결정의 다른 접근법
