# PersonaAI: An Interactive Agentic-AI Framework for Autonomous Hypothesis Generation and Validation in Aging

## 메타 정보
- **저자**: Byounggook Cho, Gi-Young Lee, Junghyun Jung, Junyeop Kim, GunHo Park, Patrick C. N. Martin, Hyobin Kim, Jeein Oh, Jong-Soo Kim, Jongpil Kim, Tae-Hyung Kim, Kyoung-Jae Won
- **소속**: Cedars-Sinai Medical Center / BioNexux (한국) / Dongguk University
- **출처**: bioRxiv preprint (2026-01-20)
- **DOI**: [10.64898/2026.01.16.699755](https://doi.org/10.64898/2026.01.16.699755)

---

## Essence
노화(aging) 연구를 위한 인터랙티브 에이전틱 AI 프레임워크 **PersonaAI**를 제안한다. 56만 편 이상의 노화 관련 문헌을 RAG(Retrieval-Augmented Generation) 기반으로 합성하여 메커니즘적 가설을 생성하고, 이를 single-cell RNA-seq 데이터로 자율적으로 in silico 검증하는 이중 구조(dual-phase) 시스템이다. 핵심은 완전 자율이 아닌 **human-in-the-loop** 방식으로, 연구자의 생물학적 직관을 AI의 대규모 문헌 합성 능력과 결합하여 가설 탐색 공간을 효율적으로 제한한다.

---

## Motivation
노화는 확률적(stochastic)이고 다중 스케일(multi-scale)적 특성을 가지며, 세포 이질성(cellular heterogeneity)으로 인해 인과 메커니즘 규명이 매우 어렵다. PubMed에 56만 편 이상의 노화 관련 논문이 색인되어 있어 개별 연구자가 이를 모두 소화하기 불가능하며, 고차원 single-cell 데이터의 해석에는 다학제적 전문성이 요구된다. 기존의 완전 자율 AI 시스템(AI Co-scientist, Virtual Lab 등)은 무제약적 확률 탐색에 의존해 계산 비용이 높고, 경험적 검증 메커니즘이 부재하다.

---

## Achievement
1. **Temporal cutoff 검증**: 2020년 이전 문헌만으로 114개 가설을 12개 노화 hallmark에 걸쳐 생성하고, 2021-2025년 발표 문헌으로 사후 검증. "Loss of Proteostasis" 사례에서 리보솜 번역 오류(translational infidelity) 가설이 Bottger et al. (2025), Stein et al. (2022), Martinez-Miguel et al. (2021)에 의해 확인됨.
2. **Senescent Cirbp+ hepatocyte 발견**: 벌크 조직 수준에서 보고된 CIRBP 상향조절을 single-cell 수준에서 간세포 특이적 노화 프로그램으로 해석. Cirbp 고발현 클러스터(C4)가 노화에 따라 확장되며 senescence 마커(Cdkn1a, Trp53)와 ER stress 조절자(Hspa5, Atf4)를 발현.
3. **남성 특이적 ASPC 감소의 혈관 니치 메커니즘 규명**: Perigonadal adipose tissue에서 남성의 혈관내피세포(VEC) 감소와 VEGF-VEGFR 신호축 붕괴가 지방줄기/전구세포(ASPC) 재생 능력 저하를 주도함을 밝힘. Ligand-receptor 상호작용 분석으로 남성 특이적 보호 paracrine 신호 약화 확인.

---

## How
- **가설 생성 모듈**: LangGraph 기반 상태 머신으로 구동되는 Self-Correcting RAG 시스템. 56만+ 논문(PubMed/PMC)을 인덱싱하고, 하이브리드 chunking + query expansion + FlashRank 재순위 매기기로 고정밀 검색 수행. "Generation-Critique-Refinement" 반복 루프로 재귀적 추론.
- **Meta-Prompting 아키텍처**: 3단계 위계적 프롬프트(Research Trend Scouting -> Idea Generation -> Hypothesis Finalization). Step-Back Prompting 원리를 적용하여 추상적 생물학 원리에서 구체적 분자 타겟으로 수렴.
- **Epistemic Persona Injection**: 도메인 전문가 페르소나를 주입하여 LLM의 확률적 변동을 억제하고 생물학적 타당성 범위 내로 출력 제한.
- **가설 평가 에이전트**: Claude Agent SDK 기반, 5개 특화 MCP(Model Context Protocol) 도구셋 통합 -- Aging Atlas(TileDB-SOMA), Single-cell Analysis(Scanpy/Harmony), CCI Analysis(LIANA), Trajectory(Slingshot/PAGA), Enrichment(GSEApy).
- **데이터**: Mouse Aging Atlas (25M+ cells, 17 tissues, 5 age points, 3-23 months).
- **자기 평가**: LLM 기반 스코어링 루브릭(0.0-1.0)으로 논리적 완성도 평가, 0.9 이상만 in silico 검증 단계로 전달.

---

## Originality
- **Human-in-the-loop 에이전틱 AI**: 기존 완전 자율 시스템(AI Scientist, AI Co-scientist)과 차별화되는 전략적 공동 파일럿(co-pilot) 접근. 연구자가 탐색 공간을 제한함으로써 brute-force 가설 생성의 비효율 해소.
- **문헌-데이터 통합 검증 루프**: RAG 기반 가설 생성과 single-cell 데이터 자율 검증을 하나의 프레임워크에서 연결한 최초 사례.
- **Temporal cutoff 벤치마킹**: 시간 기준 지식 차단으로 AI의 추론 능력을 단순 정보 검색과 구분하여 검증하는 방법론.
- **MCP(Model Context Protocol) 활용**: 비정형 자연어를 실행 가능한 생물정보학 워크플로우로 변환하여 코딩 전문성 없이도 복잡한 in silico 검증 가능.

---

## Limitation & Further Study
- **In silico 검증에 국한**: 모든 발견이 계산적 검증에 머물러 있으며, 실험적(in vitro/in vivo) 검증은 수행되지 않음. 특히 CIRBP+ hepatocyte의 senescence 기능적 역할과 VEGF-VEGFR 축 복원의 치료적 효과는 실험적 확인이 필요.
- **마우스 데이터 한정**: Mouse Aging Atlas에 기반하므로 인간으로의 일반화에 한계. 종간 보존성(cross-species conservation)에 대한 검증 부재.
- **단일 오믹스(single-cell transcriptomics)**: 현재 scRNA-seq만 활용하며, 멀티오믹스(epigenomics, proteomics, metabolomics) 통합은 향후 과제로 언급.
- **RAG 기반 추론의 본질적 한계**: 저자들도 인정하듯, RAG가 진정한 의미의 "새로운" 가설을 생성하는지 vs. 기존 지식의 조합에 불과한지에 대한 근본적 질문이 남아 있음.
- **Hallucination 완화, 완전 제거 불가**: Epistemic persona injection과 temporal cutoff로 위험을 줄이지만, 모든 출력은 여전히 "검증 대기 가설" 수준.
- **재현성**: 프롬프트 설계에 크게 의존하며, 다른 도메인으로의 이전 가능성(transferability)은 구체적으로 검증되지 않음.
- **정량적 벤치마크 부족**: 114개 가설의 temporal cutoff 검증 결과가 제시되나, 다른 AI 시스템과의 직접 비교 실험은 없음.

---

## Evaluation
노화 연구라는 복잡한 도메인에서 AI를 "자율 과학자"가 아닌 "전략적 공동 연구자"로 포지셔닝한 실용적 접근이 돋보인다. Temporal cutoff 검증은 AI의 추론 능력을 평가하는 설득력 있는 방법론이며, CIRBP+ hepatocyte와 남성 특이적 ASPC 감소 사례는 프레임워크의 발견 잠재력을 구체적으로 보여준다. 다만, 실험적 검증 부재와 마우스 모델 한정은 발견의 생물학적 임팩트를 제한하며, 다른 AI 시스템과의 정량 비교가 없어 상대적 우위를 판단하기 어렵다. Meta-prompting과 MCP 기반 아키텍처의 기술적 설계는 정교하나, 프롬프트 엔지니어링 의존도가 높아 범용성에 대한 추가 검증이 필요하다.
