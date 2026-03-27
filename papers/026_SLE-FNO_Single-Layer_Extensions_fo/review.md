# SLE-FNO: Single-Layer Extensions for Task-Agnostic Continual Learning in Fourier Neural Operators

- **저자**: Mahmoud Elhadidy, Roshan M. D'Souza, Amirhossein Arzani
- **기관**: University of Utah, University of Wisconsin-Milwaukee
- **발표**: arXiv:2603.20410 (2026.03.20)
- **키워드**: Continual Learning, Fourier Neural Operator, Catastrophic Forgetting, Scientific Machine Learning

---

## 한줄 요약 (Essence)
Fourier Neural Operator(FNO)에 단일 태스크별 레이어를 추가하는 SLE-FNO를 제안하여, 과학적 기계학습 서로게이트 모델의 지속적 학습(continual learning) 시 catastrophic forgetting 없이 새로운 분포 외(OOD) 태스크에 효율적으로 적응하는 방법론이다.

---

## 연구 동기 (Motivation)
과학적 기계학습(SciML)에서 서로게이트 모델은 통상 학습 데이터와 동일한 분포의 추론 데이터를 가정하지만, 실제 환경에서는 새로운 실험 조건이나 시뮬레이션 영역이 기존 학습 분포를 벗어나는 경우가 빈번하다. 특히 유체역학에서는 기하학적 변화, 경계 조건, 유동 레짐 변화가 비선형적으로 해를 변화시킨다. 기존 fine-tuning은 catastrophic forgetting을 야기하고, 전체 재학습은 계산 비용이 과도하다. 따라서 이전 데이터 접근 없이도 새 태스크에 적응하면서 기존 지식을 보존하는 continual learning 프레임워크가 필요하다.

---

## 주요 성과 (Achievement)
1. **SLE-FNO 제안**: 사전학습된 FNO backbone을 완전히 동결하고, 태스크별로 단일 FNO 레이어만 추가하여 잔차 보정(residual correction)을 학습. 태스크당 파라미터 증가는 1.5~4.4%에 불과
2. **Zero forgetting 달성**: 아키텍처 기반 접근법으로 이전 태스크 성능 저하가 전혀 없음
3. **Task-agnostic 추론**: KPCA 기반 OOD 검출기를 통해 태스크 레이블 없이 자동으로 적절한 SLE-FNO 브랜치로 라우팅, 실험에서 100% 태스크 식별 정확도 달성
4. **포괄적 벤치마크**: EWC, LwF, Replay, OGD, GEM, PiggyBack, LoRA 등 주요 CL 방법론과의 체계적 비교 수행
5. **실용적 문제 적용**: 맥동성 동맥류 혈류에서의 시간평균 벽면전단응력(TAWSS) 예측이라는 실제 CFD 기반 문제에 적용

---

## 방법론 (How)

### 데이터셋
- 230개의 CFD 시뮬레이션 (이상화된 동맥류 기하구조)
- 입력: 심장 주기 내 5개 시점의 2D 농도장 슬라이스 + 공간 좌표 (7채널, 64x64)
- 출력: 시간평균 벽면전단응력(TAWSS)의 2D 투영 (1채널)
- 4개 태스크로 분할: Task A (200개, 베이스라인), Task B/C/D (각 10개, OOD)

### SLE-FNO 아키텍처
1. 사전학습된 FNO(4 Fourier 레이어, 64 hidden channels)로 Task A 학습
2. 새 태스크 k 등장 시 backbone 전체 동결
3. lifted representation z₀에서 작동하는 단일 태스크별 FNO 레이어 g_k 추가
4. 최종 출력: frozen backbone 출력 + SLE-FNO 잔차 보정
5. Sobolev norm loss로 값과 그래디언트 모두 매칭

### Task-agnostic 라우팅
- 각 태스크 학습 시 입력 데이터에 대해 Kernel PCA(KPCA) 모델 피팅
- 추론 시 모든 KPCA 검출기의 재구성 오류 계산
- 최소 재구성 오류를 갖는 태스크의 SLE-FNO 브랜치로 라우팅
- Random Fourier Features로 가우시안 커널 근사

### 비교 방법론
- **정규화 기반**: EWC (Fisher Information Matrix), LwF (지식 증류)
- **리플레이 기반**: Random Reservoir Replay, K-means Replay
- **최적화 기반**: OGD (직교 그래디언트), GEM/A-GEM (에피소딕 메모리)
- **아키텍처 기반**: PiggyBack (마스크), LoRA (저랭크 어댑터)

### 평가 지표
- Relative L² error → 지수 변환을 통한 정확도 메트릭 R
- Average Accuracy (AA): 학습 단계별 전체 태스크 평균 성능
- Forgetting Measure (F): 이전 태스크의 최대 성능 대비 현재 성능 하락

---

## 독창성 (Originality)
1. **FNO 구조 활용 설계**: 일반적인 어댑터와 달리 FNO의 스펙트럴 특성을 활용하여 사전학습 모델이 학습한 저주파 구조 위에 고주파 잔차 보정만 학습
2. **극도의 파라미터 효율**: 단일 FNO 레이어만으로 태스크별 적응 (LoRA, PiggyBack 대비 더 단순하면서도 경쟁력 있는 성능)
3. **SciML 회귀 문제에 대한 체계적 CL 벤치마크**: 대부분의 CL 연구가 분류 문제에 집중하는 반면, 연속 물리장 예측이라는 고유한 도전 과제를 다룸
4. **KPCA 기반 OOD 검출과 아키텍처 확장의 결합**: 태스크 레이블 없는 완전 자동화된 추론 파이프라인 구현

---

## 한계 (Limitation)
1. **제한된 태스크 수**: 4개 태스크(A→B→C→D)만으로 평가하여, 수십~수백 개 태스크가 순차적으로 등장하는 장기 CL 시나리오에서의 확장성 미검증
2. **소규모 OOD 데이터**: Task B/C/D가 각각 8개 학습 샘플로 매우 작아, 보다 다양한 데이터 규모에서의 성능 불확실
3. **단일 문제 도메인**: 맥동성 혈류의 TAWSS 예측이라는 특정 CFD 문제에만 적용되어, 다른 물리 시스템으로의 일반화 가능성 미확인
4. **선형적 잔차 합산**: SLE-FNO의 잔차가 frozen backbone 출력에 단순 덧셈으로 결합되어, 태스크 간 분포 차이가 극단적인 경우 표현력 부족 가능
5. **KPCA 라우팅의 확장성**: 태스크 수 증가 시 KPCA 모델 수도 선형 증가하며, 입력 공간에서의 태스크 간 중첩이 클 경우 라우팅 정확도 저하 가능성
6. **논문 후반부 결과 미완**: Stage 4, Discussion, Conclusion 등이 제공된 버전에서 잘려 있어 최종 종합 평가를 완전히 확인하기 어려움

---

## 총평 (Evaluation)
과학적 기계학습에서 상대적으로 덜 탐구된 continual learning 문제를 체계적으로 다루었다는 점에서 의의가 크다. FNO의 스펙트럴 구조를 활용한 SLE-FNO 설계는 직관적이면서도 효과적이며, 태스크당 1.5~4.4% 파라미터 추가만으로 zero forgetting을 달성한 것은 인상적이다. 특히 EWC, LwF, OGD, GEM, Replay, PiggyBack, LoRA 등 주요 CL 방법론을 동일 조건에서 비교한 포괄적 벤치마크는 SciML 커뮤니티에 유용한 참조점을 제공한다. KPCA 기반 task-agnostic 라우팅의 100% 정확도도 주목할 만하다. 다만, 단일 응용 문제와 소수 태스크에 한정된 실험으로 일반화 가능성에 대한 의문이 남으며, 장기적 태스크 축적 시의 확장성에 대한 추가 연구가 필요하다. 전반적으로 SciML에서의 CL 연구의 좋은 출발점을 제시하는 논문이다.

## 평가
| 항목 | 점수 (1-5) |
|------|-----------|
| Novelty | 3 |
| Technical Soundness | 4 |
| Significance | 3 |
| Overall | 3.3 |

**총평**: FNO에 지속학습을 적용하는 SLE 프레임워크로 SciML에서의 catastrophic forgetting 문제를 체계적으로 다룬 탄탄한 연구다.
