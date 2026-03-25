# The Rise of Large Language Models and the Direction and Impact of US Federal Research Funding

> **저자**: Yifan Qian, Zhe Wen, Alexander C. Furnas, Yue Bai, Erzhuo Shao, Dashun Wang | **날짜**: 2026년 1월 | **arXiv**: 2601.15485v1

---

## 핵심 요약
본 논문은 LLM(Large Language Model)의 부상이 미국 연방 연구 자금 시스템을 어떻게 재편하고 있는지를 대규모 실증 분석으로 밝힌다. NSF와 NIH의 비공개 제안서(funded + unfunded)와 공개 수상 데이터를 결합하여, LLM 사용이 2023년부터 급격히 증가하되 bimodal 분포를 보이며, LLM 사용이 높을수록 연구 제안의 semantic distinctiveness가 낮아져 최근 지원된 과제와 유사해지는 경향을 발견하였다. 이 효과는 기관에 따라 상이하여, NIH에서는 LLM 사용이 채택 확률 및 논문 생산량과 양의 상관을 보이나 NSF에서는 유의미한 관계가 없다.

## 연구 배경 및 동기
- 연방 연구 자금은 미국 과학 기업의 방향, 다양성, 장기적 영향력을 결정하는 핵심 메커니즘
- LLM이 과학적 글쓰기와 평가에 미치는 영향에 대한 관심이 커지고 있으나, 연구 자금 배분 단계에서의 영향은 거의 알려져 있지 않음
- LLM은 과학적 아이디어의 명확한 표현과 학제간 탐색을 촉진할 수 있는 반면, 기존 corpus에 학습되어 있어 언어적 다양성과 아이디어 탐색 범위를 축소할 우려 존재
- NIH(NOT-OD-25-132)와 NSF가 generative AI 사용에 대한 가이드라인을 발표하는 등 정책적으로도 시급한 주제

## 방법론
- **데이터셋 4종**:
  - D1(비공개 NSF 제안서): 2개 R1 대학, 1.6K건(2021-2025), funded/unfunded/pending 포함
  - D2(비공개 NIH 제안서): 동일 대학, 4.1K건
  - D3(공개 NSF 수상): Dimensions 기반, 57K건
  - D4(공개 NIH 수상): 74K건
- **LLM 탐지**: Liang et al.(2024)의 distributional LLM-quantification framework 적용. 2021년 인간 작성 텍스트와 GPT-3.5-turbo 재작성 텍스트의 단어 분포 비교로 LLM 수정 문장 비율(alpha) 추정
- **Semantic distinctiveness**: SPECTER2 임베딩으로 각 제안서/수상의 abstract와 동일 기관의 전년도 수상 abstract 간 cosine distance 계산, 연도 내 백분위로 변환
- **회귀 분석**: Grant start year, field, investigator(PI/co-PI) fixed effects를 포함한 OLS 회귀. Investigator fixed effects로 동일 연구자 내 비교 가능
- **Robustness checks**: Flesch Reading Ease, promotional language 제거, 비교 세트 변경(2년), L2 distance, logistic/negative binomial 회귀, 분야별/하위 기관별 분석

## 주요 결과
- **LLM 사용 급증**: 2022년 말 ChatGPT 출시 이후 2023년부터 alpha가 급격히 상승. Bimodal 분포로 "최소 사용"과 "상당한 사용" 그룹이 명확히 분리
- **Semantic distinctiveness 감소**: 4개 데이터셋 모두에서 LLM 사용이 높을수록 semantic distinctiveness가 유의하게 낮음. NSF 수상 기준 IQR 이동 시 ~5 percentile point, NIH 기준 ~4 point 감소. Investigator fixed effects 포함 시에도 동일한 패턴 — 동일 연구자의 제안서도 LLM 사용이 높을 때 덜 독창적
- **기관별 차별적 효과**: NIH에서 LLM 사용(alpha)은 채택 확률과 양의 상관(IQR 이동 시 ~4 percentage point 증가). NSF에서는 유의하지 않음
- **논문 산출**: NIH 수상에서 alpha가 높으면 ~5% 더 많은 논문 산출. 그러나 이 증가분은 **non-hit papers에 집중**(top 5% 논문에서는 유의하지 않음). NSF에서는 유의한 관계 없음
- **Writing complexity**: LLM 사용이 높을수록 Flesch Reading Ease가 낮아져(더 복잡한 문장) LLM이 글쓰기 복잡도를 높이는 경향

## 독창성 및 기여
- **비공개 제안서 데이터**를 활용한 최초의 대규모 LLM-funding pipeline 분석. 기존 연구가 공개 수상 데이터에 한정된 반면, funded/unfunded 모두를 포함하여 selection 효과를 직접 관찰
- LLM이 과학적 아이디어의 **positioning, selection, translation** 세 단계 모두에 영향을 미침을 체계적으로 입증
- **기관 의존적(agency-dependent) 효과**라는 중요한 발견 — NIH vs. NSF의 리뷰 문화와 인센티브 구조의 차이를 시사
- Individual-level productivity 증가와 system-level diversity 감소가 공존할 수 있다는 최근의 AI-science 연구(Furnas et al., 2025)를 연구 자금 맥락으로 확장
- LLM 사용에 따른 **idea homogenization**의 실증적 증거를 최초로 제시

## 한계 및 향후 연구
- **저자 언급 한계**: LLM 탐지가 abstract의 텍스트 흔적에만 의존하며, ideation, 문헌 합성, 실험 설계 등에서의 LLM 활용은 포착하지 못함; 2개 R1 대학의 비공개 데이터로 일반화에 제약; 출판물 기반 성과 측정의 한계(소프트웨어, 데이터셋 등 미반영)
- **추가 지적**: Correlation과 causation의 구분이 충분하지 않음. LLM 사용이 높은 연구자와 낮은 연구자 간의 미관측 이질성이 결과를 구동할 수 있음(investigator fixed effects가 시간불변 특성만 통제)
- LLM 탐지 모델이 GPT-3.5 기반으로 학습되어 Claude, Gemini 등 다른 모델의 사용을 정확히 포착하는지 불확실
- NIH에서의 양의 효과가 LLM의 실질적 기여인지, NIH 리뷰 프로세스의 특성(incremental research 선호)에 의한 것인지 구분이 어려움
- 2023-2025년의 짧은 관찰 기간으로 장기적 영향(high-impact work의 축적 시간)을 평가하기 어려움

## 평가
| 항목 | 점수 (1-5) |
|------|-----------|
| Novelty | 5 |
| Technical Soundness | 4 |
| Significance | 5 |
| Clarity | 5 |
| Overall | 5 |

**총평**: LLM이 과학 연구 자금 시스템에 미치는 영향을 최초로 대규모 실증 분석한 획기적 연구로, 비공개 제안서 데이터의 활용, 기관별 차별적 효과의 발견, 그리고 idea homogenization에 대한 경고 등 science policy에 즉각적 함의를 갖는다. Dashun Wang 그룹의 science of science 연구 역량이 돋보이는 논문이다.
