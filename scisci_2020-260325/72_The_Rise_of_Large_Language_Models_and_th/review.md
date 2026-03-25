# The Rise of Large Language Models and the Direction and Impact of US Federal Research Funding

> **저자**: Yifan Qian, Zhe Wen, Alexander C. Furnas, Yue Bai, Erzhuo Shao, Dashun Wang | **날짜**: 2026-01-21 | **Journal**: arXiv preprint | **DOI**: 10.48550/arXiv.2601.15485

---

## Essence

LLM 사용이 미국 연방 연구비(NSF/NIH) 제안서와 수상 과제에 급속히 확산되고 있으며, 이는 아이디어의 동질화, 선정 결과, 그리고 연구 산출물에 기관별로 상이한 영향을 미친다. LLM 활용도가 높은 제안서는 semantic distinctiveness가 4-5 percentile point 낮고, NIH에서는 LLM 사용이 선정 확률 ~4%p 증가 및 논문 산출 ~5% 증가와 연관되나 고인용 논문에는 효과가 없으며, NSF에서는 어떤 유의한 연관도 관측되지 않았다.

## Motivation

연방 연구비는 미국 과학 생태계의 방향, 다양성, 장기 영향을 결정하는 핵심 메커니즘이다. LLM이 과학 글쓰기에 급속히 확산되고 있지만, 이것이 공공 연구비 생태계를 어떻게 변화시키는지는 거의 알려져 있지 않다. 특히 미선정 제안서는 기밀이어서 대규모 연구가 불가능했다. LLM은 과학적 탐색을 확장할 잠재력과 동시에 기존 패턴으로의 수렴(exploitation 편향)을 야기할 우려를 모두 갖고 있어, 연구비 파이프라인에서의 실증적 증거가 시급하다.

## Achievement

1. **급속한 확산**: 2023년부터 NSF/NIH 모두에서 LLM 사용(α)이 급증. 개인 grant 수준에서 bimodal 분포(거의 미사용 vs 10-15% 수준의 실질적 사용)가 관측됨
2. **아이디어 동질화**: 4개 데이터셋(private/public x NSF/NIH) 모두에서, 동일 연구자 내에서도 LLM 활용이 높을수록 semantic distinctiveness가 유의하게 낮음(최근 선정 과제에 더 가까움). NSF award 기준 25th→75th percentile α 이동 시 ~5 percentile point 감소
3. **기관별 차등 효과(선정)**: NIH에서 LLM 사용은 선정 확률 ~4%p 증가와 유의하게 연관(investigator FE 포함). NSF에서는 유의한 관계 없음
4. **기관별 차등 효과(산출)**: NIH에서 높은 α는 ~5% 더 많은 논문 산출과 연관되나, top 5%/1% 고인용 논문에서는 효과 소멸. NSF에서는 논문 산출과 무관
5. 다양한 robustness check(promotional words 제거, L2 distance, logistic/negative binomial regression, 분야별/하위기관별 분석) 통과

## How

- **데이터**: (D1) 2개 R1 대학 NSF 제안서 1.6K건(기밀, funded+unfunded), (D2) NIH 제안서 4.1K건(기밀), (D3) NSF 공개 수상 57K건, (D4) NIH 공개 수상 74K건. 모두 2021-2025 start date
- **LLM 탐지**: Liang et al. (2025)의 distributional LLM-quantification framework 적용. 2021년 human-written 초록과 GPT-3.5-turbo로 rewrite한 초록의 단어 분포 비교로 α(LLM-modified 문장 비율) 추정. Corpus-level 및 individual grant-level 추정
- **Semantic distinctiveness**: SPECTER2 embedding으로 각 grant 초록과 동일 기관 전년도 선정 과제 초록 간 평균 cosine distance 계산, within-year percentile 변환
- **회귀 분석**: OLS with investigator, field, year fixed effects + log(funding) 통제. Proposal success(binary), log(# papers + 1), log(# hit papers + 1) 등 종속변수. 표준오차는 investigator 수준 clustering

## Originality

- **최초의 연구비 파이프라인 전체 분석**: 미선정 제안서를 포함한 기밀 데이터와 공개 수상 데이터를 결합하여, 제안서 작성 → 선정 → 연구 산출까지 LLM의 영향을 추적한 최초의 대규모 실증 연구
- **"Communication vs Execution" bottleneck 가설** 제시: LLM의 생산성 이득이 글쓰기(communication) 가속에 주로 작용하며, 연구 실행(execution) 제약은 해소하지 못한다는 중요한 이론적 프레임워크
- NSF와 NIH의 차등 효과를 통해 기관 구조와 심사 규범이 기술 도입의 결과를 어떻게 조절하는지 보여줌

## Limitation & Further Study

### 저자들이 언급한 한계
- α 측정이 초록 텍스트의 LLM 흔적만 포착하며, ideation, 문헌 합성, 실험 설계 등에서의 LLM 사용은 감지 불가
- 관측 연구이므로 인과 관계 주장에 한계(investigator FE로 완화하나 완전한 인과 추론은 아님)
- 고영향 연구는 장기간 후에 나타날 수 있어 현재 follow-up window(2023-2024 시작 과제)가 충분하지 않을 수 있음
- Publication count가 NSF 산출(소프트웨어, 데이터셋, 교육 등)보다 NIH 산출을 더 잘 포착할 수 있음

### 리뷰어 판단 아쉬운 점
- Private data가 2개 R1 대학에 한정되어 대표성에 한계. 소규모 기관, 비R1 대학, 비영어권 연구자에서의 패턴은 다를 수 있음
- LLM 탐지 방법이 GPT-3.5 기반인데, Claude, Gemini 등 다른 모델의 사용 패턴이 다를 수 있으며 탐지 정확도의 한계가 있음
- NIH에서의 선정률 증가와 논문 증가 사이의 기전이 명확하지 않음 — LLM이 제안서 품질을 높여서인지, 심사자의 편향을 이용한 것인지 구분 불가
- "아이디어 동질화"가 실제로 과학적 다양성 감소로 이어지는지에 대한 직접적 증거는 부족(semantic distance 감소 = 다양성 감소?)

### 후속 연구
- LLM 사용의 인과 효과 추정을 위한 자연실험 또는 RCT 설계
- 장기(5-10년) follow-up을 통한 고영향 연구 산출 분석
- 심사자 측의 LLM 사용과 그 영향 분석
- 비미국 기관 및 다양한 기관 유형에서의 재현 연구
- Exploration-exploitation trade-off의 정량적 측정과 최적 포트폴리오 거버넌스 설계

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 5/5 |
| Technical Soundness | 4/5 |
| Significance | 5/5 |
| Clarity | 5/5 |
| Overall | 5/5 |

**총평**: LLM이 미국 연방 연구비 생태계를 어떻게 변화시키고 있는지를 기밀 제안서 데이터와 공개 수상 데이터를 결합하여 체계적으로 분석한 선구적 연구로, 아이디어 동질화와 기관별 차등 효과라는 핵심 발견은 과학 정책에 즉각적 함의를 갖는다.
