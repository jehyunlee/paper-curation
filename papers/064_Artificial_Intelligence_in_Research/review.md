# Artificial Intelligence in Research and Development

## 메타 정보
- **저자**: Benjamin F. Jones (Kellogg School of Management, Northwestern University & NBER)
- **출처**: Economics of Transformative AI Workshop, Fall 2025, SIEPR, Stanford University (Preliminary Draft, 2025-09-16)
- **DOI**: 없음 (워크숍 발표 논문)
- **PDF**: [C:\Users\jehyu\GoogleDrive\Zotero\Jones, Benjamin_2025_Artificial Intelligence in Research and Development.pdf](C:\Users\jehyu\GoogleDrive\Zotero\Jones, Benjamin_2025_Artificial Intelligence in Research and Development.pdf)

---

## Essence (본질)
AI가 R&D(연구개발) 과정에 미치는 영향을 평가하기 위한 경제학적 프레임워크를 제시하는 이론 논문이다. R&D를 이질적 "태스크(task)"의 집합으로 모델링하고, AI의 영향을 결정하는 세 가지 핵심 요인을 식별한다: (a) AI가 수행할 수 있는 연구 태스크의 비율(gamma), (b) 해당 태스크에서의 AI 생산성(M), (c) 아이디어 생산에서의 병목(bottleneck) 강도(theta). 핵심 결론은 병목 효과가 매우 강력하여, 초지능(superintelligence) 수준의 AI라 하더라도 연구 태스크의 넓은 범위를 자동화하지 못하면 진보 속도의 가속은 제한적이라는 것이다.

## Motivation (동기)
AI 능력의 급속한 발전에 따라, AI가 단순 재화/서비스 생산을 넘어 "아이디어 생산 함수(ideas production function)" 자체를 변혁할 가능성이 대두되었다. Dario Amodei(Anthropic CEO)의 "지능의 한계수익(marginal returns to intelligence)" 개념처럼, 매우 강력한 AI가 진보 속도를 얼마나 가속할 수 있는지에 대한 체계적 분석 프레임워크가 필요했다. 기존 경제 성장 모델은 일반균형 맥락에 집중했으나, 개별 연구 분야 수준의 미시적 분석 도구가 부재했다.

## Achievement (성과)
1. **태스크 기반 R&D 생산 모델**: 인간과 기계(AI 포함)를 모두 포괄하는 아이디어 생산 함수를 구축. 모든 기계-태스크 이질성이 단일 생산성 지수 M_t로 집약됨을 증명 (Proposition 1)
2. **지능의 한계수익 정량화**:
   - 소규모 지능 증가: 진보 속도의 탄성치 = R&D 내 기계 지출 비율 s^X (약 1/3) (Corollary 2)
   - 대규모 지능 증가: M_t가 무한대로 가도, theta = -1일 때 진보 속도는 최대 2.25배 증가 (초기 s^X = 1/3 기준) (Corollary 3)
   - AI가 비노동 태스크의 절반만 담당할 경우: 무한 지능으로도 진보 속도 44% 증가에 불과 (Corollary 4)
3. **자동화 범위의 결정적 중요성**: AI가 더 많은 연구 태스크를 인수할수록 병목을 극복. 90% 인간 태스크 자동화 + 초지능 시 최대 225배 가속 가능하나, 25%만 자동화하면 최대 4배 (Corollary 6)
4. **Transformative AI(TAI) 조건 정량화**: 진보 속도 10배 가속을 위해서는 theta = -1일 때 인간 연구 태스크의 최소 50%를 AI가 대체해야 하며, 그 이상의 자동화가 초지능 요구를 극적으로 감소시킴 (Figure 5)
5. **이중 병목(double bottleneck) 문제**: 개별 R&D 과정의 병목 + 경제 전체 수준에서의 Baumol 비용 질병이 중첩되어, TAI의 달성을 더욱 어렵게 만듦
6. **AI 벤치마크와의 연결**: PaperBench 등의 벤치마킹 연구를 모델 파라미터 추정에 활용하는 방법론 제시

## How (방법)
- **태스크 기반 모델**: R&D를 단위 측도의 태스크 집합 j in [0,1]로 정의. 각 태스크는 기계 또는 인간이 수행하며, CES(Constant Elasticity of Substitution) 집합 함수로 결합 (theta < 0은 보완성/병목 의미)
- **최적화**: 고정 R&D 예산 D_t 하에서 진보 속도를 최대화하는 자본-노동 배분 문제를 해결 -> 닫힌 형태(closed-form) 해 도출
- **비교 정태 분석**: 기계 지능(M_t)의 소/대규모 증가, 자동화 비율(gamma_t) 증가, 양자 동시 변화에 대한 명시적 결과 도출
- **경험적 보정**: R&D 노동 지출 비율 ~2/3 (미국/OECD), Ahmadpoor & Jones(2019)의 theta 약 -1 추정치, Amdahl의 법칙(theta = -1) 등으로 파라미터 범위 설정
- **수학적 증명**: 모든 주요 결과에 대해 부록에서 완전한 증명 제공

## Originality (독창성)
- **"지능의 한계수익" 공식화**: AI 산업계의 비공식적 논의(Amodei의 에세이)를 엄밀한 경제학적 프레임워크로 전환한 최초의 체계적 시도
- **병목의 지배성 정량화**: 초지능이 좁은 범위의 태스크에서 무한한 생산성을 달성해도 진보 가속이 제한적이라는 반직관적 결과를 명시적으로 도출
- **TAI의 정량적 조건 제시**: "진보 속도 10배 가속"이라는 구체적 기준에 대해 필요한 자동화 비율과 생산성 배수의 조합을 시각화 (Figure 5)
- **이중 병목 개념**: 개별 R&D 병목과 경제 전체 Baumol 비용 질병의 중첩이라는 새로운 관점 제시
- **벤치마크 설계 제안**: AI 벤치마킹을 단순 정답률(산술 평균)이 아닌, 병목 구조를 반영하는 일반화 평균으로 재설계해야 함을 주장

## Limitation & Further Study (한계 및 후속 연구)

### 저자가 인정한 한계
- Preliminary Draft 단계로, 일반균형(general equilibrium) 효과를 명시적으로 다루지 않음 (부분균형 분석)
- AI의 미래 능력이 불확실하므로 구체적 예측보다는 개념적 프레임워크에 집중
- 창의적 탐색(creative search)을 "태스크"로 단순화하여 포착하며, 창의성의 본질적 특성 일부가 손실될 수 있음
- 새로운 도구가 새로운 인간 태스크를 창출하는 효과를 명시적으로 모델링하지 않음

### 자체 판단 한계
- **태스크의 독립성 가정**: 실제 연구에서는 태스크 간 복잡한 상호의존성과 순서 제약이 존재하나, CES 함수는 이를 대칭적 보완성으로 단순화
- **동적 분석 부족**: AI가 점진적으로 더 많은 태스크를 인수하는 과정의 경로 의존성(path dependency)이 분석되지 않음
- **질적 변화 미포착**: AI가 기존에 존재하지 않던 완전히 새로운 연구 방법론을 창출하는 가능성(태스크 공간 자체의 확장)이 모델에 반영되지 않음
- **theta 추정의 한계**: Ahmadpoor & Jones(2019)의 theta 약 -1 추정은 인간 투입 변동으로부터 식별된 것이며, AI 투입에 대해서도 동일한 값이 적용되는지 검증되지 않음
- **분야별 실증 부재**: 프레임워크의 유용성을 특정 연구 분야(예: 신약 개발, 재료 과학)에 실제 적용한 사례 분석이 없음

### 후속 연구 방향
- PaperBench, SWE-Bench 등의 벤치마크 데이터를 활용한 분야별 {C_t, gamma_t, theta} 실증 추정
- AI가 태스크 공간 자체를 확장하는 효과를 포함하는 확장 모델 개발
- 일반균형 맥락에서의 요소 가격 변화(AI 확산에 따른 인건비/계산 비용 변동)까지 포함하는 동적 모델
- 구체적 연구 분야(신약 개발, 소프트웨어 공학, 재료 과학)에 대한 실증적 사례 연구

## Evaluation (총평)
| 항목 | 점수 (1-10) |
|------|-----------|
| 신규성 (Novelty) | 8 |
| 기술적 깊이 (Technical Depth) | 8 |
| 실험적 검증 (Experimental Validation) | 3 |
| 재현 가능성 (Reproducibility) | 7 |
| 실용적 영향력 (Practical Impact) | 9 |
| 표현 명확성 (Clarity) | 9 |

**총평**: Stanford SIEPR 워크숍에서 발표된 이 예비 초안은 AI가 R&D에 미치는 영향을 평가하는 데 있어 가장 명확하고 실용적인 경제학적 프레임워크를 제공한다. 핵심 통찰은 단순하지만 강력하다: 병목(bottleneck)이 지배하는 세계에서, 초지능보다 자동화 범위가 훨씬 중요하다. "무한한 지능으로도 진보 속도가 2.25배밖에 증가하지 않을 수 있다"는 결과는, AI에 대한 과도한 기대와 과소평가 모두에 대해 정량적 근거를 제공한다. Dario Amodei의 "Machines of Loving Grace" 에세이에 대한 학술적 응답으로서, 정책 입안자와 연구 관리자에게 필수적인 사고 도구가 될 것이다. 실증적 검증은 향후 과제로 남아 있으나, 개념적 기여만으로도 높은 가치를 지닌다.

## 평가
| 항목 | 점수 (1-5) |
|------|-----------|
| Novelty | 4 |
| Technical Soundness | 4 |
| Significance | 5 |
| Overall | 4.3 |

**총평**: 병목 구조 하에서 초지능보다 자동화 범위가 더 중요하다는 반직관적 결론을 수학적으로 도출한 AI R&D 경제학 프레임워크의 핵심 기여 논문이다.
