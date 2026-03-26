# Augmenting large language models with chemistry tools

> **저자**: Andres M. Bran, Sam Cox, Oliver Schilter, Carlo Baldassari, Andrew D. White, Philippe Schwaller | **날짜**: 2024-05-08 | **Journal**: Nature Machine Intelligence | **DOI**: 10.1038/s42256-024-00832-8

---

## Essence

ChemCrow는 GPT-4에 18개의 전문가 설계 화학 도구를 통합한 LLM 화학 에이전트로, 유기 합성, 약물 발견, 재료 설계 전반에 걸쳐 화학 과제를 자동화한다. ReAct 프레임워크 기반의 Thought-Action-Observation 반복 루프를 통해 LLM을 "과잉 자신감의 정보원"에서 "도구를 활용하는 추론 엔진"으로 전환시키며, 곤충 기피제(DEET)와 3개 유기촉매의 자율 합성 및 신규 발색단(chromophore) 발견을 실험적으로 검증했다.

## Motivation

- **알려진 것**: LLM이 다양한 영역에서 강력한 성능을 보이지만, 기본 수학 연산이나 화학 변환(IUPAC-to-SMILES 등) 같은 작업에서 체계적으로 실패하며, 외부 지식 소스에 대한 접근이 제한됨
- **Gap**: 화학 분야의 AI 도구(반응 예측, 역합성, 분자 생성 등)가 개별적으로 발전했으나, 실험 화학자의 computational skill 부족과 도구 간 통합/상호운용성 부재로 인해 이들의 잠재력이 충분히 활용되지 못함
- **왜 중요한가**: LLM의 추론 능력과 전문 화학 도구의 정확성을 결합하면, 전문가에게는 효율적 조수 역할을, 비전문가에게는 정확한 화학 지식 접근의 진입 장벽을 낮추는 효과
- **접근법**: ReAct/MRKL 프레임워크로 GPT-4를 reasoning engine으로 활용하고, 18개 화학 도구(분자, 반응, 안전, 일반)를 LangChain을 통해 통합

## Achievement

1. **자율 합성 실행**: DEET(곤충 기피제)와 3개 thiourea 유기촉매(Schreiner's, Ricci's, Takemoto's)를 IBM RoboRXN 플랫폼에서 자율적으로 계획 및 실행하여 목표 화합물 합성 성공
2. **신규 발색단 발견**: 데이터 정제, random forest 모델 학습, 후보 스크리닝, 합성 계획까지 자동 수행하여 목표 흡수 파장 369 nm 근처의 새로운 chromophore 발견(측정값 336 nm)
3. **14개 use case 평가**: 합성 계획, 분자 설계, 화학 논리 등 3개 카테고리, 14개 과제에서 전문가 4명의 평가 결과 ChemCrow가 GPT-4 단독 대비 화학적 정확성과 과제 완성도에서 일관되게 우수
4. **LLM 평가 vs 인간 평가 괴리 발견**: EvaluatorGPT는 GPT-4의 유창하지만 부정확한 답변을 선호하는 반면, 인간 전문가는 ChemCrow의 사실적 정확성을 선호 -- LLM 기반 평가의 한계를 실증
5. **안전 가드레일**: 화학무기 전구체 데이터베이스 대조, 폭발물 확인, GHS 안전 정보 제공 등 hard-coded + prompted 안전 메커니즘 구현
6. **오픈소스 공개**: 12개 도구 포함 오픈소스 버전을 GitHub에 공개

## How

- **프레임워크**: LangChain 기반 ReAct(Thought-Action-Action Input-Observation) 반복 루프, GPT-4 (temperature 0.1)
- **18개 도구 구성**:
  - **분자 도구(8개)**: Name2SMILES, SMILES2Price, Name2CAS, Similarity, ModifyMol, PatentCheck, FuncGroups, SMILES2Weight
  - **반응 도구(4개)**: NameRXN (NextMove Software), ReactionPredict (RXN4Chemistry API), ReactionPlanner (역합성 + 다단계 합성), ReactionExecute (RoboRXN 로봇 연동)
  - **안전 도구(3개)**: ControlledChemicalCheck (OPCW/Australia Group 목록 대조), ExplosiveCheck (GHS 폭발성 확인), SafetySummary (PubChem 기반 안전 요약)
  - **일반 도구(3개)**: WebSearch (SerpAPI), LitSearch (paper-qa + FAISS), Python REPL, Human
- **실험 검증**: IBM RoboRXN 로봇 플랫폼에서 합성 실행, UV-Vis 분광법으로 chromophore 특성 확인, MS(ESI) 및 NMR로 생성물 확인
- **평가 방법**: (1) 인간 전문가 4명이 화학 정확성/추론 품질/과제 완성도 3차원 평가, (2) EvaluatorGPT(LLM 기반 자동 평가), (3) GPT-4 단독(도구 없음)과의 비교

## Originality

- **18개 전문 도구의 체계적 통합**: 분자, 반응, 안전, 일반 4개 범주의 도구를 단일 LLM 에이전트에 통합한 최초의 포괄적 화학 도구셋 -- 이전 연구들이 개별 도구나 제한된 도구셋만 사용한 것과 대비
- **실험적 검증의 폭**: 단순 합성뿐 아니라 ML 모델 학습을 통한 신규 분자 발견(chromophore)까지 포함하여, LLM 화학 에이전트의 다양한 작업 모드를 실증
- **자율 합성 절차 적응**: RoboRXN 플랫폼의 합성 검증 오류를 LLM이 자율적으로 수정(용매량 조절 등)하는 closed-loop 적응 능력 시연
- **LLM 평가의 한계 실증**: 과학적 사실성이 중요한 과제에서 LLM 자기평가(EvaluatorGPT)가 인간 전문가 평가와 체계적으로 불일치함을 보여, LLM-as-judge의 한계를 경고
- **안전 메커니즘 선제 설계**: dual-use 위험을 인식하고, 화학무기 전구체 대조 등의 안전 가드레일을 에이전트 설계에 내장

## Limitation & Further Study

### 저자들이 언급한 한계

- 도구의 수량과 품질에 의해 시스템 성능이 제한되며, 합성 엔진의 정확도가 개선되면 전체 성능도 향상 가능
- 평가 과제가 14개로 제한적이며, closed-source GPT-4 API 의존으로 개별 결과의 재현성이 보장되지 않음
- 도구 사용 reasoning이 결함 있을 경우 정확한 도구도 무용지물이 되는 "garbage in, garbage out" 문제
- 지적재산권 문제에 대한 명확한 가이드라인이 부재

### 자체판단 아쉬운 점

- 합성된 4개 화합물이 모두 알려진 분자로, 진정한 의미의 "신규 합성 경로 발견"이라기보다 기존 경로의 자동 실행에 가까움(chromophore 제외)
- 인간 전문가 평가자가 4명으로 통계적 검정력이 제한적이며, 평가자 간 일치도(inter-rater reliability) 보고가 부족
- Coscientist(Boiko et al., Nature 2023)와의 체계적 비교가 없어, 두 시스템의 상대적 장단점을 파악하기 어려움
- 도구 실패 시의 fallback 메커니즘이나 오류 전파 분석이 부족
- 비용 분석이 없어 실제 연구실에서의 경제성을 판단하기 어려움

### 후속 연구

- 이미지 처리, 스펙트럼 분석 등 multimodal 도구 통합을 통한 능력 확장
- Open-source LLM(LLaMA, Vicuna 등)으로의 이식을 통한 재현성 및 접근성 향상
- 더 다양하고 어려운 화학 과제에 대한 대규모 벤치마크 개발
- RLHF 기반 validation/peer-review 시스템 내장을 통한 추론 신뢰성 향상
- 약물 발견의 전체 파이프라인(target identification - hit discovery - lead optimization)에 대한 end-to-end 적용

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 4/5 |
| Technical Soundness | 4/5 |
| Significance | 4/5 |
| Clarity | 5/5 |
| Overall | 4/5 |

**총평**: ChemCrow는 LLM을 화학 전문 도구와 체계적으로 통합한 선구적 연구로, 18개 도구의 포괄적 설계, 로봇 플랫폼과의 실제 합성 실행, 신규 chromophore 발견이라는 세 가지 축에서 강력한 기여를 한다. 특히 LLM 기반 평가(EvaluatorGPT)가 과학적 사실성 평가에서 인간 전문가와 체계적으로 불일치한다는 발견은 AI 평가 분야에 중요한 시사점을 제공한다. Coscientist(Nature 2023)와 독립적으로 동시에 개발되었으며, 더 많은 도구와 다양한 use case를 제시한 점에서 차별화된다. 오픈소스 공개와 안전 가드레일 설계는 책임있는 AI 개발의 모범 사례이다.
