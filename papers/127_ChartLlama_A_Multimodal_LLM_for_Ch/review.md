# ChartLlama: A Multimodal LLM for Chart Understanding and Generation

**저자:** Yucheng Han, Chi Zhang, Xin Chen, Xu Yang, Zhibin Wang, Gang Yu, Bin Fu, Hanwang Zhang
**소속:** NTU Singapore, Tencent, Southeast University
**출처:** arXiv:2311.16483 (2023.11)
**DOI:** [10.48550/ARXIV.2311.16483](https://doi.org/10.48550/ARXIV.2311.16483)

---

## Essence (본질)
GPT-4의 언어 및 코딩 능력을 활용하여 차트 데이터 생성, 차트 그림 생성, instruction 데이터 생성의 3단계 파이프라인으로 고품질 합성 instruction-tuning 데이터셋(11K 차트, 160K instruction, 10개 차트 유형, 7개 태스크)을 구축하고, 이를 기반으로 차트 이해와 생성을 동시에 수행하는 멀티모달 LLM인 ChartLlama를 제안한 연구이다.

## Motivation (동기)
GPT-4V 등장 이후에도 멀티모달 LLM은 차트와 같은 특화된 시각적 표현의 해석에 현저한 한계를 보인다. 기존 차트 데이터셋들은 두 가지 근본적 문제가 있다. (1) 웹 크롤러로 수집한 차트에 수동 어노테이션을 의존하여 데이터 품질이 낮고 어노테이션이 불완전하다. (2) 기존 데이터셋은 단순 QA나 캡셔닝 위주로, 차트의 고수준 이해(트렌드 분석, 데이터 해석)나 차트 생성/편집 등 실세계 활용 시나리오를 포괄하지 못한다. 특히 차트 생성 태스크는 Python 코드 어노테이션의 부재로 기존 방법으로는 지도 학습이 사실상 불가능했다.

## Achievement (성과)
1. **전통적 벤치마크 SOTA:**
   - ChartQA: Human 48.96%, Augmented 90.36%, 평균 69.66%로 당시 기존 최고 UniChart(66.24%) 대비 +3.42%p
   - Chart-to-Text: Pew 14.23, Statista 40.71 (BLEU-4)로 기존 최고 대비 개선
   - Chart Extraction: Human Precision 84.92%, F1 84.89%로 DePlot(81.32%) 대비 우수
2. **신규 태스크에서 LLaVA-1.5 대비 대폭 개선:** Detailed Description 74.2 vs 67.2, Chart-to-chart 성공률 73% vs 46%, Text-to-chart 성공률 81% vs 77%, Chart-editing 성공률 71% vs 38%
3. **신규 차트 유형 QA 능력:** Funnel(70.59%), Gantt(56.64%), Heatmap(53.18%), Scatter(54.97%) 등 기존 모델이 지원하지 않던 차트 유형에서 UniChart 및 Baseline 대비 압도적 성능
4. **10개 차트 유형, 7개 태스크 지원:** bar, line, pie, polar, funnel, gantt, heatmap, scatter, box, candlestick

## How (방법)
- **3단계 데이터 생성 파이프라인 (전적으로 GPT-4 활용):**
  1. **Chart Data Generation:** GPT-4에 차트 주제, 데이터 트렌드, 행/열 크기, 차트 유형 등을 지정하여 합성 테이블 데이터 생성. 기존 차트 데이터셋을 참조하여 다양성 보강
  2. **Chart Figure Generation:** GPT-4의 코딩 능력으로 Matplotlib 기반 차트 플로팅 코드 생성. 함수 문서와 in-context 예시 제공 (성공률 85%)
  3. **Instruction Data Generation:** 차트 설명, 원시 데이터, 차트 코드를 종합하여 GPT-4로 QA, 요약, 데이터 추출, 상세 설명, chart-to-chart, text-to-chart, chart-editing 등 7가지 태스크의 instruction 데이터 생성
- **모델 아키텍처:** LLaVA-1.5 기반. CLIP ViT-L/14@336px 비전 인코더 + 2-layer MLP projection + LLM (LoRA rank 128로 효율적 학습)
- **평가:** 전통적 태스크(ChartQA, Chart-to-text, Chart extraction)는 기존 메트릭 사용, 신규 태스크는 GPT-4 기반 평가 메트릭 설계

## Originality (독창성)
- **차트 이해와 생성의 통합:** 기존 연구가 차트 "이해"에만 집중한 반면, chart-to-chart(디렌더링), text-to-chart(생성), chart-editing(편집)을 포함하여 이해와 생성을 하나의 모델에서 동시에 수행하는 최초의 시도
- **완전 합성 데이터 파이프라인:** 웹 크롤링이나 수동 어노테이션 없이 GPT-4만으로 데이터 테이블 -> 차트 이미지 -> instruction 데이터를 end-to-end로 생성. 이 방법은 차트 유형이나 태스크를 쉽게 확장할 수 있는 유연성 제공
- **10개 차트 유형 지원:** 기존 데이터셋이 bar/line/pie 3종에 한정된 반면, polar, funnel, gantt, heatmap, scatter, box, candlestick을 추가. 특히 GPT-4의 코드 생성 능력으로 비표준 차트 유형도 자동 생성 가능
- **GPT-4 기반 평가 메트릭 설계:** Chart-to-text의 BLEU-4 한계를 지적하고, 태스크별 맞춤형 GPT-4 평가 프롬프트를 설계

## Limitation & Further Study (한계 및 향후 연구)
- **합성 데이터의 한계:** 모든 차트가 GPT-4로 합성되어, 실세계 차트의 시각적 다양성(폰트, 레이아웃, 해상도 변이)을 완전히 재현하지 못할 수 있음. 후속 연구인 ChartInstruct와 ChartGemma가 실세계 차트 활용으로 이 문제를 해결
- **다국어 OCR 미지원:** 비전 인코더가 다국어 OCR을 처리하지 못하여 비영어 텍스트를 포함하는 차트에서 활용이 제한됨
- **기본적 에러 필터링만 수행:** 데이터 생성 과정에서 형식 확인과 코드 실행 가능 여부만 검증하며, 내용의 의미적 정확성에 대한 자동 검증은 미구현
- **13B 모델 크기:** 후속 연구(ChartGemma 3B)에 비해 대형이며, 실세계 배포에 불리
- **Chart-to-text 평가의 BLEU-4 한계:** ground truth가 적은 상황에서 BLEU-4의 불합리성을 인식하면서도, GPT-4 평가의 재현성 문제는 동일하게 존재
- **향후 연구:** 다국어 OCR 지원 비전 인코더 개발, 더 효과적인 자동 스크리닝 메커니즘, 다른 도메인(과학 도표, 의료 이미지 등)으로의 파이프라인 확장

## Evaluation (평가)
ChartLlama는 차트 도메인에서 instruction tuning을 위한 완전 합성 데이터 파이프라인이라는 중요한 방법론적 기여를 한 선구적 연구이다. GPT-4의 언어-코드 능력을 3단계로 분리 활용하는 파이프라인 설계는 직관적이면서도 효과적이며, 차트 유형과 태스크의 확장이 용이하다는 점은 큰 실용적 가치가 있다. 특히 차트 "생성"과 "편집"을 이해와 함께 통합한 것은 이 분야에서 독창적인 시도이다. ChartQA, Chart-to-text, Chart extraction에서의 SOTA 달성과, 6개 비표준 차트 유형에 대한 QA 성능은 파이프라인의 유효성을 뒷받침한다. 다만 합성 데이터만 사용한 점은 실세계 차트에 대한 일반화에 본질적 한계가 있으며, 이는 후속 연구(ChartInstruct의 실세계 차트 수집, ChartGemma의 이미지 직접 활용)에서 개선된다. 또한 GPT-4 의존적 데이터 생성은 비용과 재현성 측면에서 과제가 남으며, 신규 태스크 평가가 LLaVA-1.5 단일 베이스라인과의 비교에 그친 점은 아쉬움으로 지적된다. 전반적으로 차트 이해/생성 분야의 instruction tuning 패러다임을 개척한 중요한 연구로, ChartInstruct 및 ChartGemma와 함께 이 분야의 기초를 형성한 논문이다.

## 평가
| 항목 | 점수 (1-5) |
|------|-----------|
| Novelty | 4 |
| Technical Soundness | 3 |
| Significance | 3 |
| Overall | 3.3 |

**총평**: 합성 데이터 파이프라인으로 차트 이해와 생성을 동시에 가능하게 한 NTU/Tencent 연구로, 이해-생성 통합 접근이 차별적이나 합성 데이터 품질의 실제 평가 한계가 있다.
