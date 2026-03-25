# Open Datasets in Learning Analytics: Trends, Challenges, and Best PRACTICE

> **저자**: Valdemar Svabensky, Brendan Flanagan, Erwin Daniel Lopez Zapata, Atsushi Shimada | **날짜**: 2026년 2월 | **DOI**: 10.1145/3798096 | **arXiv**: 2602.17314v1

---

## 핵심 요약
본 논문은 Learning Analytics(LA) 분야의 open dataset 현황에 대한 최대 규모의 체계적 서베이를 수행하였다. 2020-2024년 LAK, EDM, AIED 세 주요 학회에서 발표된 1,125편의 논문을 수동으로 검토하여 204편의 논문에서 사용된 172개의 고유한 open dataset을 발견, 분류, 분석하였다. 이 중 143개는 기존 서베이에서 포착되지 않은 새로운 데이터셋이다. 또한 연구자들을 위한 8개 항목의 PRACTICE 가이드라인 체크리스트를 제시하였다.

## 연구 배경 및 동기
- Open science와 FAIR 원칙(Findable, Accessible, Interoperable, Reusable)이 UNESCO, European Commission 등에서 강력히 권장되고 있으나, LA 분야에서의 실제 open dataset 가용성은 불투명
- 기존 LA dataset 서베이(Romero & Ventura 2020, Mihaescu & Popescu 2021 등)는 최대 44개 데이터셋만 보고하였으며, 이미 outdated 됨
- 재현성(reproducibility) 위기: LAK 2021-2022에서 단 5%의 논문만 raw dataset을 공개하였고(Haim et al.), 궁극적으로 재현 가능한 논문은 0편
- 교육 데이터의 privacy, 법적 제약(GDPR 등), 기관별 IRB 승인 문제 등이 데이터 공유의 장벽으로 작용

## 방법론
- **범위**: LAK, EDM, AIED 3개 학회의 2020-2024년 full/short paper 전수 조사(1,125편)
- **프로세스**: PRISMA 가이드라인에 따른 체계적 문헌 검토. 49편 제외(position paper, survey 등) 후 1,076편 후보 논문을 수동으로 심사
- **포함 기준**: (1) 데이터셋이 접근 가능하다고 명시, (2) 전자적으로 획득 가능(직접 다운로드, 로그인 후 다운로드, 또는 30일 이내 요청 응답), (3) 논문 결과 도출에 실제 사용된 데이터셋
- **검증**: Google NotebookLM 등 AI 도구를 시도했으나 부정확하여 완전 수동 검사로 전환. 제3, 4저자가 독립적으로 검증
- **분석**: Mann-Kendall trend test, sensitivity analysis 등 통계적 방법 활용

## 주요 결과
- 1,076편 후보 논문 중 **204편(19%)**만이 open dataset을 활용 또는 제공
- **172개 고유 데이터셋** 발견, 이 중 143개가 기존 서베이에 없는 새로운 발견
- 학회별 차이: EDM(29.7%) > AIED(18.7%) > LAK(10.9%) 순으로 open dataset 활용 비율이 높음
- "요청 시 제공" 데이터셋의 **절반(17/35)이 실제로 제공되지 않음** — 이메일 무응답(12건), 거절(3건) 등
- 데이터셋의 교육 맥락: K-12(94회)과 대학생(55회)이 지배적; STEM 교육(특히 수학)과 언어 학습이 주요 주제
- 미국 소재 학교 데이터셋이 압도적으로 많아 지리적 편향 존재
- 연도별 open dataset 증가 추세가 관찰되나 통계적으로 유의하지 않음(Mann-Kendall test)

## 독창성 및 기여
- LA 분야 **최대 규모**(172개)의 open dataset 체계적 서베이이며, 기존 서베이 대비 143개의 신규 데이터셋 발견
- 데이터셋의 교육적 맥락, 수집 방법, 기술적 속성, 분석 방법론까지 아우르는 **가장 상세한 분류 체계** 제공
- PRACTICE 약어를 활용한 8개 항목 가이드라인 체크리스트 제안 — 연구자들의 데이터 공개 실천을 위한 구체적 지침
- "요청 시 제공"의 비효율성을 실증적으로 입증(성공률 51.4%)하여 직접 다운로드 방식을 권장

## 한계 및 향후 연구
- **저자 언급 한계**: LAK, EDM, AIED 3개 학회에 한정되어 저널 논문이나 다른 학회(예: Learning at Scale, CSCL)의 데이터셋은 미포함; 5년이라는 시간 범위의 제약
- **추가 지적**: Science of science 관점에서 볼 때, 이 논문은 교육 데이터에 특화되어 있어 일반적인 과학 연구 데이터 공유 관행과의 비교가 부족함
- Open dataset 활용이 실제 연구 품질이나 citation impact에 미치는 영향에 대한 인과적 분석이 없음
- AI/LLM을 활용한 자동 데이터셋 탐지가 실패했다는 보고는 흥미로우나, 이에 대한 체계적 분석이 없음
- Global South 연구 기관의 데이터셋 부족 문제를 지적하면서도 이에 대한 구체적 해결책 제시가 미흡

## 평가
| 항목 | 점수 (1-5) |
|------|-----------|
| Novelty | 3 |
| Technical Soundness | 4 |
| Significance | 3 |
| Clarity | 5 |
| Overall | 3.5 |

**총평**: 방법론적으로 엄밀하고 실용적 가치가 높은 서베이 논문이나, 주된 기여가 데이터셋 목록의 확대와 가이드라인 제안에 머물러 있어 이론적 깊이는 제한적이다. LA 연구 커뮤니티에는 중요한 자원이 될 것이나, science of science 관점에서의 분석적 통찰은 다소 부족하다.
