# AI for Science: An Emerging Agenda

> **저자**: Philipp Berens, Kyle Cranmer, Neil D. Lawrence, Ulrike von Luxburg, Jessica Montgomery | **날짜**: 2023-03-07 | **arXiv**: 2303.04217

---

## Essence

2022년 9월 Dagstuhl Seminar 22382 "Machine Learning for Science: Bridging Data-Driven and Mechanistic Modelling"의 논의를 종합한 로드맵 보고서이다. AI for Science 분야의 핵심 연구 주제로 (1) 시뮬레이션 및 에뮬레이션, (2) 인과 추론, (3) 도메인 지식의 AI 통합을 제시하고, 지구과학, 천체물리학, 생물학, 농업과학, 신경과학 등 다양한 분야의 구체적 적용 사례를 통해 data-driven과 mechanistic 모델링의 연속체(continuum)를 구축하는 비전을 제안한다.

## Motivation

- **알려진 것**: AI/ML이 기후과학, 천체물리학, 발생생물학, 농업 등 다양한 과학 분야에서 이미 성과를 내고 있으며, 데이터 기반 분석의 잠재력이 입증됨
- **Gap**: 대부분의 AI 도구가 정적 사용자 모델과 일반적 벤치마크 기준으로 개발되어 도메인 과학자의 실제 필요와 괴리. Data-driven 모델과 mechanistic 모델 간의 분리가 과학적 발견의 병목. 학제간 협력의 구조적 인센티브 부족
- **왜 중요한가**: 21세기의 복잡계 과학(기후변화, 건강, 경제 등)을 이해하려면 다중 스케일, 다중 모달리티 데이터에서 인과관계를 추출하고 도메인 지식과 통합하는 새로운 방법론이 필요
- **접근법**: 시뮬레이션, 인과성, 도메인 지식 인코딩의 3축 연구 어젠다 + 커뮤니티/도구/인력 구축의 실천 로드맵

## Achievement

1. **포괄적 분야 조망**: 지구과학(FLUXNET, 빙하 모델링), 환경/농업(탄자니아 가금류 질병 진단, 사헬 수목 계수), 물리학(암흑물질, Schrodinger bridge), 생물학(단세포 전사체학, 신경과학) 등의 구체적 사례를 통해 AI for Science의 현황과 과제를 조망
2. **모델링 연속체 프레임워크**: Data-driven에서 strongly mechanistic까지의 모델링 스펙트럼을 제시하고, 대칭성/불변성/인과관계/물리법칙 등의 도메인 지식을 통해 두 극단을 연결하는 개념적 프레임워크 제안 (Figure 1)
3. **연구 어젠다 구체화**: Simulation-based inference (SBI), 인과 ML, 도메인 지식 인코딩의 3대 기술 축과 구체적 연구 질문 목록 (Annex B) 제시
4. **실천 로드맵**: (1) 방법론/응용 발전, (2) 도구/툴킷 투자, (3) 학제간 역량 구축, (4) 연구/실천 커뮤니티 성장의 4단계 행동 계획

## How

- **방법론**: Dagstuhl 세미나의 발표 및 토론을 종합한 정성적 분석. 약 30명의 세계적 연구자(Bernhard Scholkopf, Jakob Macke, Samuel Kaski 등)의 발표 초록과 토론 내용을 구조화
- **구성**: (1) 분야별 AI 적용 스냅샷 → (2) 시뮬레이션 구축 → (3) 데이터와 인과성 연결 → (4) 도메인 지식 인코딩 → (5) 연구 어젠다 → (6) 실천 로드맵의 논리적 흐름
- **핵심 개념**: Computational faithfulness (시뮬레이션 출력과 관측의 일관성), Scientific centaurs (인간-AI 협업체), Digital siblings (디지털 트윈의 과학적 버전), 모델링 연속체 (data-driven ↔ mechanistic)

## Originality

- **"Rendezvous point" 비전**: AI for Science를 단순한 도구 적용이 아닌, AI 연구와 도메인 과학이 만나는 "만남의 장"으로 개념화. 양방향 피드백 루프(AI가 과학을 발전시키고, 과학이 AI를 발전시킴)를 명시적으로 강조
- **Data-driven ↔ Mechanistic 연속체**: 물리법칙, 대칭성, 인과관계, 정성적 지식 등 다양한 수준의 도메인 지식을 통해 순수 데이터 모델과 순수 기계론적 모델을 연결하는 스펙트럼 제안. 이분법적 사고를 넘어서는 통합적 프레임워크
- **Scientific centaurs 개념**: 인간과 AI의 협업체로서, AI가 연구자의 목표를 모델링하고 암묵적 지식을 추출하는 "AI sidekick" 비전 제시

## Limitation & Further Study

### 저자들이 언급한 한계

- ML 벤치마크가 도메인 연구자의 기대와 반드시 일치하지 않으며, 과학적 맥락에서의 모델 신뢰성 보장을 위한 guardrail 필요
- 학제간 연구의 구조적 인센티브 부족 (커리어 경로, 출판 매체, 인정 체계)
- AI 도구의 craft skill (know-how)이 체계화되지 않아 비전문가의 접근성 제한

### 자체판단 아쉬운 점

- **2023년 시점의 한계**: LLM/foundation model의 과학적 활용에 대한 논의가 거의 없음. GPT-4 출시 직전에 작성되어, 이후 급격히 발전한 LLM 기반 과학 발견(예: 자율 실험, 논문 생성, 코드 생성 등)에 대한 전망이 부재
- **구체적 기술 기여 없음**: 세미나 보고서의 성격상 새로운 알고리즘이나 실험 결과를 제시하지 않으며, 기존 연구의 종합과 방향 제시에 그침
- **Global South 관점의 제한적 반영**: 탄자니아 가금류 사례를 포함하나, AI for Science의 글로벌 접근성, 계산 자원 불평등, 데이터 주권 문제에 대한 심층 논의 부족
- **평가 기준 미제시**: 제안된 로드맵의 성공을 어떻게 측정할 것인지에 대한 구체적 지표나 마일스톤이 없음
- **산업 관점 부재**: 학술 연구 중심의 논의로, 산업계에서의 AI for Science 활용과 기술 이전 관련 논의가 부족

### 후속 연구

- Foundation model/LLM의 과학적 발견 활용 (2023년 이후 급격히 발전)
- 자율 실험실(autonomous lab)과 AI scientist 구현
- AI for Science의 재현성, 신뢰성 프레임워크 개발
- 글로벌 AI for Science 인프라 구축 및 접근성 확대

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 3/5 |
| Technical Soundness | 3/5 |
| Significance | 4/5 |
| Clarity | 5/5 |
| Overall | 4/5 |

**총평**: AI for Science 분야의 가장 포괄적이고 체계적인 로드맵 중 하나로, Berens, Cranmer, Lawrence, von Luxburg, Montgomery 등 저명한 연구자들의 통찰이 잘 종합되어 있다. Data-driven과 mechanistic 모델링의 연속체 개념, computational faithfulness, scientific centaurs 등의 프레임워크는 분야의 방향성을 잘 정립한다. 다만 2023년 초 작성 시점의 한계로 LLM 혁명 이후의 급격한 변화를 반영하지 못하며, 새로운 기술적 기여보다는 기존 논의의 종합에 가깝다. AI for Science에 관심을 갖는 연구자라면 반드시 읽어야 할 기초 문헌이다.
