# Bridging the gap between science and society: Mapping libraries' strategies for engaging in the research impact process through semantic analysis

> **저자**: Wang Zuorong, Sun Jiaxuan, He Shan, Deng Sanhong, Wang Hao | **날짜**: 2026-03-20 | **Journal**: Information Research | **DOI**: 10.47989/ir31iconf64195

---

## Essence
도서관은 과학 연구의 사회적 영향력 창출 과정에서 어떤 전략을 사용하는가? UK Research Excellence Framework(REF)의 465개 도서관 관련 사례를 LLM+BERTopic으로 분석한 결과, 5가지 핵심 전략이 도출되었다: (1) 미디어 아웃리치와 공공 참여, (2) 공공 대화와 문화 전시, (3) 예술 협업과 체험형 경험, (4) 디지털 콘텐츠 창작과 지식 보급, (5) 대규모 이벤트 운영. 도서관의 기여는 예술·인문(76%)에 집중되며, 문화적(67%)·사회적(22%) 영향이 주를 이루었다.

## Motivation
과학 연구의 사회적 영향력은 학계를 넘어선 지식 보급에 달려 있다. 기존 연구는 대학, 기업, 정부, 시민 등 지식 생산자·소비자에 초점을 맞추었으나, 도서관 같은 지식 중개자(knowledge broker)의 역할은 체계적으로 연구되지 않았다. 도서관이 디지털 시대에 지식 보급의 능동적 매개체로 진화하고 있음에도 불구하고, 그들의 전략적 참여 방식에 대한 실증적 이해가 부족했다.

## Achievement
1. REF 데이터베이스에서 **465개 도서관 관여 사례**를 식별
2. LLM(GPT-4o) 추출 + BERTopic 클러스터링으로 **5가지 핵심 전략** 도출
3. 도서관 참여가 **예술·인문(76%)** 분야에 집중됨을 정량적으로 확인
4. **문화적 영향(67%)**과 **사회적 영향(22%)**이 주요 성과 유형임을 확인
5. LLM 추출의 정밀도 84%, 재현율 76% 달성

## How
- **데이터**: REF 2014(6,637건) + REF 2021(6,361건) 중 도서관 관련 465건
- **방법**: 도서관명 정확 매칭 → GPT-4o로 전략 추출(strategy, rationale, evidence_snippet) → BERTopic으로 16개 토픽 클러스터링 → 수동 병합으로 5개 핵심 전략 도출
- **품질 관리**: 50건(10%+) 무작위 표본의 수동 검증
- **가중치 최적화**: Silhouette Score로 (strategy 0.8, evidence 0.2) 최적 조합 선정

## Originality
- 연구 영향력 생성 과정에서 **도서관의 역할**을 체계적으로 분석한 최초의 연구
- LLM과 BERTopic을 결합한 **하이브리드 텍스트 분석 파이프라인** 제시
- REF 사례 데이터를 도서관 관점에서 재해석

## Limitation & Further Study
### 저자들이 언급한 한계
- UK REF에 국한된 데이터로 다른 국가·지역에 대한 일반화 제한
- 도서관 유형별 차별화된 전략 분석 미흡

### 리뷰어 판단 아쉬운 점
- 도서관의 "기여"와 "효과"를 구분하지 않음 — 도서관 참여가 연구 영향력을 실제로 높였는지에 대한 인과적 분석 부재
- 예술·인문 편중(76%)은 REF 사례 선정 자체의 편향일 가능성
- LLM 추출의 재현율 76%는 개선 여지가 있음

### 후속 연구
- 다양한 국가의 연구 영향력 평가 데이터로 확장
- 공공·학술 도서관 유형별 전략 비교
- 도서관 개입의 인과적 효과 측정

## Evaluation
| 항목 | 점수 |
|------|------|
| Novelty | 3/5 |
| Technical Soundness | 3/5 |
| Significance | 3/5 |
| Clarity | 4/5 |
| Overall | 3/5 |

**총평**: 도서관의 연구 영향력 매개 역할을 최초로 체계적으로 매핑한 의미 있는 시도이나, 기술적 분석에 머물러 인과적 효과 검증이 향후 과제로 남는다.
