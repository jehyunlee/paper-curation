# A practical evaluation of AutoML tools for binary, multiclass, and multilabel classification

* **저자**: Marcelo V. C. Aragão, Augusto G. Afonso, Rafaela C. Ferraz, Rairon G. Ferreira, Sávio G. Leite, Felipe A. P. de Figueiredo, Samuel B. Mafra
* **학술지/출처**: Scientific Reports, 15, 17682 (2025)
* **DOI**: [10.1038/s41598-025-02149-x](https://doi.org/10.1038/s41598-025-02149-x)

---

## Essence (본질)
16개의 AutoML 프레임워크(AutoGluon, AutoSklearn, TPOT, PyCaret, Lightwood 등)를 binary, multiclass, multilabel 분류 과제에 걸쳐 체계적으로 벤치마크한 대규모 비교 연구이다. 21개 실제 OpenML 데이터셋에 5분 시간 제약 조건을 적용하고, weighted F1 score와 학습 시간을 기준으로 다층(per-dataset, across-datasets, all-datasets) 통계 검증을 수행하여 AutoML 도구 간 정확도-속도 트레이드오프를 정량적으로 규명하였다.

---

## Motivation (동기)
AutoML 도구의 종류가 급속히 증가하고 있지만, 기존 벤치마크 연구들은 binary/multiclass 중 일부 과제만 다루거나, 소수의 프레임워크만 비교하는 한계가 있었다. 특히 **multilabel 분류**에 대한 체계적 평가가 부족하여, 연구자와 실무자가 자신의 문제 특성에 맞는 도구를 선택하기 어려운 상황이었다. 본 연구는 세 가지 분류 유형을 통합적으로 다루며, 통계적 엄밀성을 갖춘 비교 프레임워크를 제시하고자 하였다.

---

## Achievement (성과)
- **AutoGluon**이 예측 정확도와 계산 효율성 간 최적의 균형을 달성하여 범용 솔루션으로 부상함 (F1 102승 vs 54패, Training Time 302승 vs 24패)
- **AutoSklearn**이 binary/multiclass에서 최고 예측 성능(평균 순위 1위)을 달성하였으나, 항상 5분 전체 학습 시간을 소진하는 단점이 있음
- **Lightwood**가 최단 학습 시간(순위 ~1.3)을 기록하였으나 정확도에서 열위
- 다수의 프레임워크가 **native multilabel 분류를 지원하지 않거나** label-powerset 변환에 의존하여 고카디널리티 환경에서 성능 저하를 보임
- Friedman + Nemenyi 사후 검정을 통해 프레임워크 간 성능 차이가 통계적으로 유의함을 확인 (F1: p=1.6×10⁻⁵, Time: p=1.8×10⁻²⁹)

---

## How (방법론)
1. **데이터셋**: OpenML에서 21개 실세계 데이터셋 선정 (binary 7, multiclass 7, multilabel 7), 다양한 도메인·복잡도·불균형 수준 포함
2. **실험 설계**: 5분 고정 시간 제약, 20회 독립 시행(소수 시드 2~71), 80/20 train/test 분할
3. **평가 지표**: Weighted F1 score (정확도), 학습 시간 (효율성)
4. **통계 분석**: 3계층 검증 체계
   - Per-dataset: 정규성 검정(Shapiro-Wilk) → 분산 동질성(Levene/Bartlett) → 적절한 모수/비모수 검정
   - Across-datasets: 분류 유형별 프레임워크 순위 비교
   - All-datasets: Friedman 검정 + Nemenyi 사후 비교, Critical Difference diagram
5. **Multilabel 처리**: Native multilabel과 Label Powerset 변환 두 방식 모두 평가
6. **하드웨어**: AMD Ryzen 9 5900X, 128GB RAM, RTX 3090, Ubuntu 22.04 (WSL)

---

## Originality (독창성)
- **세 가지 분류 유형(binary, multiclass, multilabel)을 단일 프레임워크에서 통합 비교한 최초의 체계적 연구**
- Native multilabel과 label-powerset 표현을 동시에 탐색하여, 다수 도구의 multilabel 지원 부재를 실증적으로 드러냄
- 단순 성능 비교를 넘어 **다층 통계 검증(per-dataset → across-datasets → all-datasets)**을 통해 결론의 통계적 견고성 확보
- 4개 선행 벤치마크와의 교차 비교를 통해 기존 문헌과의 맥락화 수행
- 전체 코드와 통계 분석 스크립트를 공개하여 재현 가능성 보장

---

## Limitation & Further Study (한계 및 향후 연구)
- **도메인 다양성 부족**: 의료, 금융, 사이버보안 등 전문 분야의 데이터셋이 부족하여 일반화에 한계
- **5분 시간 제약**: 장시간 반복 최적화에 특화된 프레임워크에 불리하게 작용할 수 있음
- **기본 설정만 사용**: 전문가 튜닝이 가능한 프레임워크의 잠재 성능을 충분히 반영하지 못함
- **평가 지표 제한**: 공정성(fairness), 해석가능성(interpretability), 에너지 효율성 등 보완적 관점 미포함
- **회귀 과제 제외**: 분류만 다루어 AutoML 전체 역량을 평가하기에는 범위 제한적
- 향후 연구로 **메타 AutoML 프레임워크**(과제에 따라 동적으로 도구를 선택), 강화학습/메타러닝 통합, 편향 완화 및 해석가능성 강화 제안

---

## Evaluation (총평)
AutoML 도구 선택에 실질적 가이드라인을 제공하는 포괄적이고 체계적인 벤치마크 연구이다. 16개 프레임워크 × 21개 데이터셋 × 20회 반복이라는 대규모 실험 설계와 3계층 통계 검증이 인상적이며, 특히 multilabel 분류에 대한 심층 분석은 기존 연구에서 소홀히 다루었던 영역을 보완한다. 다만, 5분이라는 단일 시간 제약과 기본 설정만을 사용한 점은 실제 활용 환경에서의 적용 가능성을 다소 제한한다. "최고 성능 도구가 아닌, 문제 특성과 자원 제약에 맞는 도구 선택"이라는 메시지는 실무자에게 유용한 관점이며, AutoGluon을 범용 추천 도구로 제시한 결론은 실험 데이터로 잘 뒷받침된다. 과학 연구에서 AutoML 도구를 도입하려는 연구자에게 필수 참고 문헌이 될 수 있다.

## 평가
| 항목 | 점수 (1-5) |
|------|-----------|
| Novelty | 2 |
| Technical Soundness | 4 |
| Significance | 3 |
| Overall | 3.0 |

**총평**: AutoML 도구들의 실용적 성능을 체계적으로 벤치마킹한 연구로 실무 적용 지침을 제공하나 방법론적 신규성은 낮다.
