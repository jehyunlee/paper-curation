# ChartGemma: Visual Instruction-tuning for Chart Reasoning in the Wild

**저자:** Ahmed Masry, Megh Thakkar, Aayush Bajaj, Aaryaman Kartha, Enamul Hoque, Shafiq Joty
**소속:** York University, MILA, Salesforce Research, NTU Singapore
**출처:** arXiv:2407.04172 (2024.07, v2: 2024.11)
**DOI:** [10.48550/ARXIV.2407.04172](https://doi.org/10.48550/ARXIV.2407.04172)

---

## Essence (본질)
기존 차트 이해 모델들이 데이터 테이블 기반으로 instruction 데이터를 생성하고, 약하게 정렬된 비전-언어 백본을 사용하는 두 가지 핵심 한계를 해결하기 위해, 차트 이미지로부터 직접 instruction 데이터를 생성하고 강하게 정렬된 PaliGemma(3B)를 백본으로 활용하는 ChartGemma를 제안한다. 5개 벤치마크에서 SOTA를 달성하면서도 기존 모델(7B~13B) 대비 현저히 작은 크기를 유지한다.

## Motivation (동기)
차트 이해를 위한 기존 instruction-tuned 모델들은 두 가지 축에서 근본적 약점이 있다. (1) **데이터 테이블 의존성:** instruction 데이터가 차트의 기저 데이터 테이블로부터 생성되어, 차트 이미지에 담긴 시각적 트렌드, 패턴, 색상, 범례 등 고수준 정보를 포착하지 못한다. Table 1에서 동일 LLM(Gemini Flash 1.5)이 데이터 테이블과 차트 이미지를 각각 입력받았을 때, 이미지 기반이 훨씬 풍부하고 맥락적인 요약을 생성함을 보여준다. (2) **약한 비전-언어 정렬:** 기존 방법들이 제한된 데이터나 아키텍처로 약하게 정렬된 VLM을 백본으로 사용하여, 실세계 복잡한 차트에 대한 일반화가 제한된다.

## Achievement (성과)
1. **ChartQA SOTA:** 평균 RA 80.16% 달성 (human set 69.52%로 기존 최고 ChartAssistant 65.90% 대비 +3.62%p). 3B 파라미터로 13B ChartAssistant에 필적하거나 능가
2. **ChartFC/ChartCheck:** ChartFC 70.33%, ChartCheck T1 71.50%, T2 74.31%로 기존 모델들과 동등 이상. 특히 ChartCheck(zero-shot)에서 강한 성능은 실세계 차트에 대한 일반화 능력 입증
3. **Open-ended 태스크:** GPT-4 평가에서 Chart2Text, OpenCQA, Web 세트 전반에 걸쳐 ChartInstruct-LLaMA2 대비 정보성과 사실 정확성 우위
4. **Human Evaluation:** 100개 웹 차트에 대해 정보성(3.79 vs 3.18), 사실 정확성(3.59 vs 2.80)에서 유의미하게 우수 (p < 10^-5), 구조는 동등 (3.82 vs 3.80)
5. **데이터 품질 개선:** instruction 정확도 82% (ChartInstruct의 61% 대비 +21%p)
6. **빠른 수렴:** 2 epoch에서 최적 성능 달성, PaliGemma의 강한 정렬 덕분

## How (방법)
- **차트 코퍼스:** 3개 카테고리 -- 합성 차트(PlotQA 5K, ChartFC 12.7K), 전문 웹사이트(Statista/Pew/OECD/OWID 등 52.7K), 웹 크롤링(WebCharts 51K). 총 122,857개 차트
- **Visual Instruction 생성:** 차트 이미지를 직접 Gemini Flash 1.5에 입력하여 instruction 데이터 생성 (데이터 테이블 불필요). Predefined 태스크(CoT, 요약, 팩트 체킹, Chart-to-Markdown, 코드 생성)와 Open-ended 태스크(트렌드 분석, 데이터 비교, 시각화 해석 등)
- **아키텍처 (PaliGemma 3B):** SigLIP 비전 인코더(448x448 해상도, 14x14 패치) + Gemma-2B LLM. 입력 시각/텍스트 토큰에 full attention, 출력 토큰에 causal attention 적용
- **1단계 학습:** 기존 2단계(alignment + instruction tuning) 대신, PaliGemma의 강한 사전 정렬(100억 이미지-텍스트 쌍 학습) 덕분에 alignment 단계 생략. 비전 인코더 동결, LLM만 파인튜닝
- **Ablation:** (1) 이미지 기반 vs 테이블 기반 instruction 데이터 효과 검증, (2) PaliGemma vs LLaVA 백본 효과 검증

## Originality (독창성)
- **차트 이미지로부터 직접 instruction 생성:** 데이터 테이블 없이 차트 이미지만으로 instruction 데이터를 생성하는 최초의 접근. 이를 통해 데이터 테이블이 없는 웹 차트도 활용 가능하고, 시각적 트렌드와 패턴을 포착하는 더 풍부한 instruction 생성
- **강하게 정렬된 백본 활용:** 100억 이미지-텍스트 쌍으로 학습된 PaliGemma를 백본으로 채택하여, alignment 단계를 생략하고도 우수한 성능 달성. 기존 약하게 정렬된 CLIP/LLaVA 기반 접근과의 차별화
- **모델 효율성:** 3B 파라미터로 7B~13B 모델을 능가하는 성능, 실세계 배포 가능성 확대
- **ChartInstruct(같은 저자 그룹의 선행 연구)의 핵심 한계를 정면으로 해결:** 테이블 기반 데이터의 61% 정확도 문제를 이미지 기반으로 82%로 개선

## Limitation & Further Study (한계 및 향후 연구)
- **독점 LLM 의존:** instruction 데이터 생성에 Gemini Flash 1.5(독점 모델) 사용, 상업적 환경에서 활용 제한 가능
- **입력 해상도 제약:** 448x448 해상도로 고해상도 차트의 텍스트가 리사이징 시 읽기 어려워짐. 896x896 지원 가능하나 처리 시간이 이차적으로 증가하여 비실용적
- **평가 재현성:** GPT-4를 평가자로 사용하며, 폐쇄형 모델의 빈번한 업데이트와 폐기 가능성이 결과 재현성에 위협
- **할루시네이션:** 사실적으로 부정확한 진술이나 실행 불가능한 코드를 간헐적으로 생성
- **복잡한 시각적 스타일 차트:** 전문 웹사이트(Pew, Statista) 차트 대비 웹 크롤링 차트에서 사실 정확성과 정보성이 상대적으로 낮음
- **향후 연구:** 인간 작성 instruction을 포함한 더 다양한 데이터셋 구축, 복잡한 시각 요소에 특화된 벤치마크와 차트 관련 평가 메트릭 제안

## Evaluation (평가)
ChartGemma는 ChartInstruct의 저자 그룹이 자체 한계를 정면으로 인식하고 해결한 후속 연구로, "데이터 테이블 대신 차트 이미지에서 직접 instruction 생성"이라는 핵심 아이디어가 간결하면서도 효과적임을 설득력 있게 보여준다. Table 1의 동일 LLM 비교 실험은 이 접근의 당위성을 직관적으로 입증하며, ablation 연구(Table 3)가 instruction 데이터와 백본 모델 각각의 기여를 명확히 분리한 점은 실험 설계의 강점이다. 3B 파라미터로 13B 모델을 능가하는 효율성은 실용적 가치가 높다. 다만, GPT-4 기반 평가의 재현성 문제, 독점 모델(Gemini) 의존성, 그리고 human evaluation에서 Cohen's Kappa 0.538의 중간 동의도는 한계로 지적된다. 또한 Open-ended 태스크에서 BLEU를 명시적으로 배제하고 GPT-4 평가만 사용한 것은 기존 연구와의 직접 비교를 어렵게 만든다. 전반적으로, 차트 이미지 직접 활용이라는 패러다임 전환과 효율적 모델 설계를 통해 차트 이해 분야를 한 단계 발전시킨 연구이며, 코드/모델/데이터의 공개로 후속 연구에 대한 기여도가 높다.

## 평가
| 항목 | 점수 (1-5) |
|------|-----------|
| Novelty | 4 |
| Technical Soundness | 4 |
| Significance | 3 |
| Overall | 3.7 |

**총평**: PaliGemma 3B 백본에 이미지 기반 인스트럭션 튜닝을 적용해 효율적 차트 이해를 달성한 연구로, 소형 모델로 대형 모델에 필적하는 성능을 보인 데이터 효율성이 핵심 기여이다.
