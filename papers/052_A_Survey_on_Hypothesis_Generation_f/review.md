# A Survey on Hypothesis Generation for Scientific Discovery in the Era of Large Language Models

## 메타 정보
- **저자**: Atilla Kaan Alkan, Shashwat Sourav, Maja Jablonska, Simone Astarita, Rishabh Chakrabarty, Nikhil Garuda, Pranav Khetarpal, Maciej Pióro, Dimitrios Tanoglidis, Kartheik G. Iyer, Mugdha S. Polimera, Michael J. Smith, Tirthankar Ghosal, Marc Huertas-Company, Sandor Kruk, Kevin Schawinski, Ioana Ciuca (UniverseTBD 등 17개 기관)
- **출처**: arXiv:2504.05496 (Preprint, under review), 2025-04-07
- **DOI**: [10.48550/arXiv.2504.05496](https://doi.org/10.48550/arXiv.2504.05496)
- **PDF**: [C:\Users\jehyu\GoogleDrive\Zotero\Alkan et al._2025_A Survey on Hypothesis Generation for Scientific Discovery in the Era of Large Language Models.pdf](C:\Users\jehyu\GoogleDrive\Zotero\Alkan et al._2025_A Survey on Hypothesis Generation for Scientific Discovery in the Era of Large Language Models.pdf)

---

## Essence (본질)
LLM 시대에 과학적 가설 생성(Scientific Hypothesis Generation, SHG)을 위한 방법론을 체계적으로 정리한 서베이 논문이다. 전통적 문헌 기반 발견(Literature-Based Discovery, LBD)부터 텍스트 마이닝, 지도학습, 그래프 기반 방법, 그리고 최신 LLM 기반 접근법(프롬프팅, 파인튜닝, RAG, 지식 그래프 통합, 멀티 에이전트 시스템)까지를 아우르는 분류 체계(taxonomy)를 제시한다. 생성된 가설의 품질 평가 방법론(전문가 평가, 자동화 메트릭, 신규성 평가, 분야별 평가)도 종합하며, 환각(hallucination), 해석 가능성, 편향, 멀티모달 통합, 인간-AI 협업 등 핵심 도전과제와 미래 방향을 논의한다.

## Motivation (동기)
과학 문헌의 폭발적 증가와 학문 분야 간 분절화(disciplinary fragmentation)로 인해, 연구자가 분야를 횡단하며 새로운 가설을 도출하기 어려워지고 있다. LLM이 방대한 과학 텍스트를 처리·종합하여 가설 생성을 보조할 가능성이 부각되었으나, 이 분야의 방법론, 평가 전략, 도전과제를 체계적으로 정리한 참고 문헌이 부재했다.

## Achievement (성과)
1. **분류 체계 제시**: SHG 방법론을 Human-Centric → LBD → Text-Mining → Supervised Learning → Graph-Based → LLM-Driven (Prompting / Fine-Tuning / RAG / Knowledge Graphs / Multi-Agent)으로 계층적으로 분류
2. **LLM 기반 파이프라인 정리**: 직접/적대적 프롬프팅, 도메인 파인튜닝, 지식 그래프 통합(KG-CoI), 멀티 에이전트 시스템 등 최신 기법을 구조화
3. **평가 방법론 종합**: 전문가 평가(블라인드 리뷰, 쌍대 비교), 자동화 평가(텍스트 관련성, 모델 기반 메트릭, 신규성 평가), 분야별 평가(생의학, 화학, 천문학, 사회과학)를 망라
4. **미래 방향 제시**: RAG 기반 환각 저감, chain-of-thought 추론 경로 추적, 멀티 에이전트 협업 프레임워크, 메타러닝 기반 교차 도메인 전이, 윤리적 거버넌스 등

## How (방법)
- arXiv API를 통해 cs.CL 분류 하 2005~2025년 논문을 체계적으로 검색 (핵심 개념, 최신 기법, 전통 기법별 검색어 사용)
- 제목·초록 기반 1차 필터링 후 수동 스크리닝으로 방법론 패러다임, 과학 도메인, 가설 표현 방식별 분류
- 시계열적 진화 추적: Swanson(1986)의 LBD부터 현재 LLM 멀티 에이전트 시스템까지의 발전 흐름을 도식화 (Figure 1: 분류 체계, Figure 2: LLM 파이프라인)

## Originality (독창성)
- SHG를 위한 최초의 **포괄적 분류 체계(taxonomy)**를 제시하여, 전통적 LBD와 LLM 기반 방법을 하나의 통합 프레임워크로 연결
- 가설 품질 향상 기법(novelty boosting, structured reasoning)과 평가 전략을 별도 축으로 분리하여 분석한 점이 기존 서베이 대비 차별화
- 천문학, 화학, 사회과학 등 다양한 도메인별 평가 기준의 차이를 명시적으로 다룸

## Limitation & Further Study (한계 및 후속 연구)

### 저자가 인정한 한계
- LLM의 환각 문제가 과학적 맥락에서 특히 위험하며, 해석 가능성(interpretability) 부족으로 가설의 근거 추적이 어려움
- 훈련 데이터의 편향이 생성되는 가설의 방향을 왜곡할 수 있음
- 도메인 파인튜닝 시 과적합(overfitting) 위험으로 범용성이 저하될 수 있음
- AI 생성 가설의 저작권, 책임 소재, 오용 가능성 등 윤리적 문제가 미해결

### 자체 판단 한계
- **검색 범위의 제한**: arXiv cs.CL 분류로 한정하여, 생의학(PubMed), 재료과학, 물리학 등 도메인 특화 저널에서의 가설 생성 연구가 누락되었을 가능성이 높음
- **실증적 비교 부재**: 각 방법론의 성능을 동일 벤치마크에서 정량적으로 비교한 실험이 없어, 어떤 접근법이 어떤 조건에서 우수한지 판단하기 어려움
- **최신 에이전트 프레임워크 부족**: 2024~2025년 급부상한 AI Scientist, SciMON, ResearchAgent 등 구체적 시스템에 대한 심층 분석이 부족
- **멀티모달 가설 생성**: 이미지, 분자 구조, 실험 데이터 등 비텍스트 모달리티를 활용한 가설 생성에 대한 논의가 피상적

### 후속 연구 방향
- 동일 벤치마크(예: OpenReview 논문 데이터셋)에서 프롬프팅, RAG, 파인튜닝, 멀티 에이전트의 정량적 비교 실험
- 멀티모달 LLM(GPT-4V, Gemini)을 활용한 실험 데이터 → 가설 생성 파이프라인 구축
- 생성된 가설의 장기 추적 평가: 실제 연구로 이어지는 가설의 비율 측정
- 도메인별 가설 생성 품질 평가를 위한 표준화된 벤치마크 데이터셋 구축

## Evaluation (총평)
| 항목 | 점수 (1-10) |
|------|-----------|
| 신규성 (Novelty) | 5 |
| 기술적 깊이 (Technical Depth) | 5 |
| 실험적 검증 (Experimental Validation) | 3 |
| 재현 가능성 (Reproducibility) | 4 |
| 실용적 영향력 (Practical Impact) | 6 |
| 표현 명확성 (Clarity) | 7 |

**총평**: LLM 기반 과학적 가설 생성이라는 시의적절한 주제를 다루며, 전통적 LBD부터 최신 LLM 기법까지의 진화를 일관된 분류 체계로 정리한 유용한 참고 문헌이다. 그러나 서베이 논문으로서 검색 범위가 arXiv cs.CL로 한정된 점, 각 방법론 간 정량적 비교 실험이 부재한 점, 그리고 2024~2025년의 급속한 발전(AI Scientist, SciMON 등)을 충분히 반영하지 못한 점이 아쉽다. 과학적 가설 생성 연구의 입문자에게는 좋은 출발점이 될 수 있으나, 실무적 가이드라인을 기대하는 독자에게는 구체성이 부족하다.

## 평가
| 항목 | 점수 (1-5) |
|------|-----------|
| Novelty | 3 |
| Technical Soundness | 3 |
| Significance | 3 |
| Overall | 3.0 |

**총평**: LLM 시대 과학적 가설 생성 방법론을 전통 LBD부터 멀티 에이전트까지 통합 분류한 서베이로 입문 참고 자료로서 가치가 있다.
