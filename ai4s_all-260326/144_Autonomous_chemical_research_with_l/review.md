# Autonomous chemical research with large language models

> **저자**: Daniil A. Boiko, Robert MacKnight, Ben Kline, Gabe Gomes | **날짜**: 2023-12-21 | **Journal**: Nature | **DOI**: 10.1038/s41586-023-06792-0

---

## Essence

Coscientist는 GPT-4를 핵심 Planner로 활용하여 인터넷 검색, 문서 탐색, 코드 실행, 실험 자동화 도구를 통합한 multi-LLM 기반 AI 에이전트 시스템으로, 화학 합성 계획부터 로봇 liquid handler 제어, 클라우드 실험실 연동, 반응 조건 최적화까지 6가지 과제를 (반)자율적으로 수행한다. 특히 palladium 촉매 cross-coupling 반응(Suzuki-Miyaura, Sonogashira)의 자율 설계 및 실행과, 기존 데이터 기반 반응 조건 최적화에서 Bayesian optimization을 능가하는 성능을 실증했다.

## Motivation

- **알려진 것**: LLM이 자연어 처리, 생물학, 화학, 코드 생성 등 다양한 영역에서 뛰어난 성능을 보이며, 동시에 화학 연구 자동화(자율 반응 발견, flow synthesis, 모바일 로봇 플랫폼)도 크게 발전
- **Gap**: LLM의 과학적 추론 능력과 실험실 자동화 기술이 각각 발전했으나, 이 둘을 통합하여 실험을 자율적으로 설계하고 실행하는 시스템은 부재
- **왜 중요한가**: 자율적 실험 설계-실행 시스템은 연구 가속화의 핵심이며, LLM이 과학 프로세스에서 어떤 수준의 자율성을 달성할 수 있는지, 그 의사결정을 어떻게 이해할 수 있는지가 중요한 연구 질문
- **접근법**: GPT-4 기반 Planner에 웹 검색, 문서 검색, 코드 실행, 실험 자동화 모듈을 연결하는 모듈형 multi-agent 아키텍처 설계

## Achievement

1. **합성 계획**: 7개 화합물에 대해 GPT-4 + Web Searcher가 다른 모든 LLM(GPT-3.5, Claude 1.3, Falcon-40B)을 능가하는 화학적으로 정확한 합성 절차 제공
2. **문서 기반 API 학습**: Opentrons OT-2 Python API와 Emerald Cloud Lab(ECL) Symbolic Lab Language를 문서 검색만으로 학습하여 유효한 코드 생성 -- ECL HPLC 실험 코드가 실제 실행에 성공
3. **Liquid handler 제어**: 자연어 프롬프트("빨간 십자 그리기" 등)를 정확한 OT-2 프로토콜로 변환하여 실행
4. **통합 실험 수행**: Suzuki-Miyaura 및 Sonogashira cross-coupling 반응을 자율적으로 설계하고 liquid handler + heater-shaker로 실행 -- GC-MS로 목표 생성물(biphenyl, tolane) 형성 확인
5. **반응 최적화**: Pd 촉매 반응 데이터셋에서 GPT-4가 20회 반복 내에 Bayesian optimization보다 높은 normalized maximum advantage 달성, SMILES 문자열만으로도 화학적 추론 가능

## How

- **시스템 아키텍처**: Planner(GPT-4 chat completion) + 4개 명령어(GOOGLE, PYTHON, DOCUMENTATION, EXPERIMENT)로 구성된 모듈형 구조
- **Web Searcher**: 별도 LLM이 프롬프트를 검색 쿼리로 변환, Google Search API 호출, 웹페이지 브라우징 후 정보를 Planner에 전달
- **Documentation Searcher**: OpenAI ada embedding으로 API 문서 섹션을 벡터화, distance-based vector search로 관련 문서 검색 및 요약
- **Code Execution**: Docker 컨테이너에서 격리 실행, 오류 발생 시 LLM이 자동 수정
- **Automation**: Opentrons OT-2 Python API 또는 ECL SLL 코드로 실험 명령 생성 및 실행
- **최적화 실험**: Perera Suzuki 데이터셋(ligand, base, solvent 조합)과 Doyle Buchwald-Hartwig 데이터셋(ligand, additive, base 조합)을 lookup table로 사용, 최대 20회 반복의 yield 최대화 게임으로 설계
- **평가 지표**: Normalized advantage(현재 수율 - 평균 수율)/(최대 수율 - 평균 수율), NMA(누적 최대 normalized advantage)
- **검증**: GC-MS로 반응 생성물 확인, 합성 계획은 1-5 척도의 전문가 평가

## Originality

- **Tool-augmented LLM의 화학 실험 적용**: 웹 검색, 문서 검색, 코드 실행, 하드웨어 제어를 단일 LLM 에이전트에 통합한 최초의 Nature 수준 시스템 시연
- **문서 기반 새 API 학습**: 학습 데이터에 없는 ECL SLL을 문서만으로 학습하여 유효한 코드를 생성하는 능력 실증 -- LLM의 in-context learning 능력의 실용적 확장
- **LLM의 화학적 추론 능력 정량화**: 반응 조건 최적화를 게임으로 설계하고, normalized advantage metric으로 LLM의 화학적 reasoning이 반복에 따라 개선됨을 정량적으로 입증
- **SMILES 기반 추론**: 분자 구조의 SMILES 표현만으로도 전자적 성질에 기반한 화학적 추론이 가능함을 발견
- **자기 수정 능력**: 코드 오류 발생 시 문서를 참조하여 자율적으로 수정하는 closed-loop 학습 시연

## Limitation & Further Study

### 저자들이 언급한 한계

- 실험 셋업이 완전 자동화되지 않아(plate 수동 이동) "semi-autonomous" 수준에 머무름
- Web Searcher가 일부 단순 화합물(ethylacetate, benzoic acid)에서 오히려 성능이 낮아, 정보의 보편성이 방해가 될 수 있음
- 안전 우려로 인해 전체 코드와 프롬프트를 공개하지 않음
- ECL HPLC 실험에서 공기 방울 주입 등 품질 관리 문제 발생

### 자체판단 아쉬운 점

- 합성 계획 평가가 주관적 1-5 척도에 의존하며, 평가자 간 일치도(inter-rater reliability)에 대한 체계적 분석이 부족
- Cross-coupling 실험이 단 2개 반응(Suzuki, Sonogashira)에 한정되어, 다양한 반응 유형에 대한 일반화 가능성이 검증되지 않음
- 최적화 실험에서 GPT-4의 training data에 해당 데이터셋 정보가 포함되었을 가능성을 완전히 배제하지 못함 -- data contamination 우려
- Hallucination 문제가 web search로 "완화"되지만 근본적으로 해결되지 않으며, 잘못된 화학 정보 생성의 위험이 상존
- 비용 분석이 부재하여, 실제 연구 환경에서의 경제성을 판단하기 어려움
- GPT-4 외 다른 LLM(Claude, open-source 모델)을 Planner로 사용한 체계적 비교가 없음

### 후속 연구

- Reaxys, SciFinder 등 전문 반응 데이터베이스와의 연동을 통한 multistep synthesis 능력 강화
- ReAct, Chain of Thought, Tree of Thoughts 등 고급 프롬프팅 전략을 통한 추론 능력 향상
- 완전 자동화된 closed-loop 실험 시스템(로봇 팔, 자동 분석기 포함)으로의 확장
- 안전 가드레일 및 dual-use 방지 메커니즘의 체계적 개발
- Multi-modal 입력(스펙트럼 이미지, 실험 영상 등)을 직접 처리하는 시스템으로의 진화

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 4/5 |
| Technical Soundness | 4/5 |
| Significance | 5/5 |
| Clarity | 4/5 |
| Overall | 4/5 |

**총평**: Coscientist는 LLM을 화학 실험의 자율적 설계-실행에 적용한 선구적 연구로, "AI가 실제 물리적 실험을 수행한다"는 패러다임을 Nature에서 처음으로 대규모 실증했다. 모듈형 아키텍처 설계, 문서 기반 API 학습, 반응 최적화에서의 chemical reasoning 정량화 등 기술적 기여가 탄탄하며, 특히 GC-MS 검증을 통해 실제 화학 반응 생성물 형성을 확인한 점이 설득력 있다. 다만, 실험 규모와 다양성이 제한적이고, data contamination 우려가 완전히 해소되지 않아 후속 연구의 여지가 크다.
