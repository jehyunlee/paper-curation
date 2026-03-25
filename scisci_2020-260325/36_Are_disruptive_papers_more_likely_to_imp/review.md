# Are disruptive papers more likely to impact technology and society?

> **저자**: Alex J. Yang, Xiaohui Yan, Haotian Hu, Hanlin Hu, Jia Kong, Sanhong Deng | **날짜**: 03/2025 | **Journal**: Journal of the Association for Information Science and Technology | **DOI**: 10.1002/asi.24947

---

## Essence
파괴적(disruptive) 논문이 기술과 사회에 더 큰 영향을 미치는가? 역설적이게도, CD index가 높은 논문은 특허 인용, 임상시험 활용, 뉴스 보도, 소셜미디어 확산 확률이 오히려 **낮았다**. 그러나 저자들이 제안한 "disruptive citation"(절대적 파괴적 인용 수) 지표로 측정하면, 파괴적 영향이 높은 논문은 기술·사회적 영역에 영향을 미칠 확률이 **유의미하게 높았다**. 이 차이는 CD index가 비율 지표로서 가지는 편향에 기인하며, 특히 최근 20년과 STEM 분야에서 두드러졌다.

## Motivation
과학적 발견은 기술 발전과 사회적 변화의 핵심 동력이지만, "파괴적" 과학이 실제로 기술과 사회에 더 큰 영향을 미치는지에 대한 실증적 증거는 부족했다. CD index는 파괴성의 표준 지표로 널리 사용되지만, 0 근처로의 중심화 경향, 인용 행태 편향 등 알려진 한계가 있어, CD index가 높은 논문이 반드시 높은 "파괴적 영향력"을 의미하는지가 불분명했다.

## Achievement
1. **CD index 역설**: CD index가 높을수록 기술·사회적 영향 확률이 낮음 → CD index에 대한 "편향(bias)" 확인
2. **Disruptive citation 제안**: 절대적 파괴적 인용 수(= 초점 논문만 인용하고 그 참고문헌은 인용하지 않는 논문 수)
3. Disruptive citation이 높은 논문은 **특허 인용(+), 임상시험(+), 뉴스(+), 소셜미디어(+)** 모두에서 높은 영향 확률
4. CD index 편향은 **최근 20년(2000-2020)**과 **STEM 분야**에서 더 두드러짐
5. 총 인용 수를 통제해도 disruptive citation의 긍정적 효과는 유지

## How
- **데이터**: Microsoft Academic Graph, 약 4,000만 편의 논문 (1950-2020), 전 분야
- **기술·사회적 영향 지표**: (1) 특허 인용, (2) 임상시험 인용, (3) 주요 뉴스 매체 보도, (4) 소셜미디어 언급
- **분석**: 로지스틱 회귀, 이질성 분석(연도별, 분야별), 대안 지표 로버스트니스 체크
- **핵심 개념**: CD index(상대적 비율) vs disruptive citation(절대적 수)

## Originality
- CD index의 "공공 영향력 편향"을 **4가지 사회적 영향 채널**을 통해 최초로 실증
- "Disruptive citation"이라는 **보완적 지표** 제안으로 CD index의 한계를 해결
- 과학의 파괴성과 사회적 영향력 사이의 관계를 분리하는 분석 프레임 제시

## Limitation & Further Study
### 저자들이 언급한 한계
- CD index의 한계가 disruptive citation으로 완전히 해결되지 않을 수 있음
- 특허 인용, 뉴스 보도 등은 사회적 영향의 대리변수일 뿐

### 리뷰어 판단 아쉬운 점
- Disruptive citation은 총 인용 수와 높은 상관관계를 가질 수밖에 없어, 단순히 "많이 인용된 논문"의 변형일 가능성
- 인과적 메커니즘(왜 파괴적 논문이 사회에 영향을 미치는가)에 대한 논의 부족
- "파괴적"이라는 개념의 조작적 정의가 여전히 인용 네트워크 구조에 의존

### 후속 연구
- Disruptive citation과 총 인용의 독립적 기여도 분석
- 텍스트 기반 파괴성 지표와의 비교
- 구체적 사례 연구를 통한 메커니즘 규명

## Evaluation
| 항목 | 점수 |
|------|------|
| Novelty | 4/5 |
| Technical Soundness | 4/5 |
| Significance | 4/5 |
| Clarity | 4/5 |
| Overall | 4/5 |

**총평**: CD index의 사회적 영향 측면에서의 편향을 대규모 데이터로 실증하고 보완 지표를 제안한 의미 있는 연구로, 과학의 파괴성 측정 논의에 중요한 기여를 한다.
