# MMC: Advancing Multimodal Chart Understanding with Large-scale Instruction Tuning

- **저자**: Fuxiao Liu, Xiaoyang Wang, Wenlin Yao, Jianshu Chen, Kaiqiang Song, Sangwoo Cho, Yaser Yacoob, Dong Yu
- **소속**: University of Maryland, College Park / Tencent AI Lab
- **발표**: arXiv:2311.10774, 2024-04-15
- **DOI**: [10.48550/arXiv.2311.10774](https://doi.org/10.48550/arXiv.2311.10774)

---

## Essence (본질)

차트 이미지 이해에 특화된 대규모 instruction tuning 데이터셋(MMC-Instruction, 600k 인스턴스)과 인간 주석 벤치마크(MMC-Benchmark, 9개 태스크), 그리고 이를 기반으로 학습한 멀티모달 차트 어시스턴트 모델(MMCA)을 제안하는 논문이다. 기존 LMM(Large Multimodal Model)들이 자연 이미지에는 강하지만 차트의 추상적 요소(추세선, 범례, 축 레이블 등)를 제대로 해석하지 못하는 문제를 체계적으로 해결하고자 한다.

## Motivation (동기)

- 기존 오픈소스 LMM(LLaVA, MiniGPT-4, mPLUG-Owl 등)은 자연 장면 이미지 이해에는 뛰어나지만, 차트 이미지의 고유한 추상적 요소(트렌드 라인, 색상 코딩된 범례, 데이터 포인트 등)를 정확히 해석하는 데 한계가 있다.
- 기존 차트 QA 데이터셋(FigureQA, DVQA, PlotQA)은 템플릿 기반 질문과 고정 어휘 답변에 의존하며, 규모와 다양성이 부족하다.
- 차트 이해 능력을 종합적으로 평가할 수 있는 인간 주석 벤치마크가 부재했다.

## Achievement (성과)

- **MMC-Instruction**: 600k 인스턴스의 대규모 차트 instruction tuning 데이터셋 구축. GPT-4를 활용해 다양한 언어 스타일과 태스크(정보 추출, 추론, 과학 차트 이해, chart-to-datatable, chart-to-json)를 포함.
- **MMC-Benchmark**: 9개 서로 다른 태스크(정보 추출, 추론, 맥락적 이해, 다중 차트 이해, 유형/주제 분류, 데이터테이블/JSON 변환, 주식 차트 분석)를 포함한 2k 규모의 인간 주석 벤치마크.
- **MMCA 모델**: 기존 오픈소스 LMM 대비 모든 9개 태스크에서 SOTA 달성. ChartQA(57.4), DocVQA(72.5), TextVQA(59.6)에서도 Pix2Struct, Donut 등 fine-tuned 모델을 능가.
- GPT-4V조차 Chart-to-DataTable 및 Chart-to-Json 태스크에서 저조한 성능을 보임을 밝혀, 이 분야의 도전적 과제를 구체적으로 제시.

## How (방법)

1. **데이터 구축**:
   - Chart-Text Alignment Data (210k): arXiv 논문에서 LaTeX 소스와 차트 이미지-캡션 쌍 수집.
   - 기존 공개 데이터셋 활용 (190k): Statista, PlotQA, VisText, ChartInfo, Unichart에서 선별.
   - GPT-4 생성 Instruction Data (200k): 차트 설명을 입력으로 GPT-4에 질문-답변 쌍 생성 요청.
   - 품질 관리: 20단어 초과 답변 제거, 비차트 관련 질문 필터링, 전문가 검증(91% 적절, 85% 정확).

2. **모델 아키텍처 (MMCA)**:
   - mPLUG-Owl 기반 (CLIP 비전 인코더 + Visual Abstractor + Vicuna 7B LLM).
   - **Stage-1**: 언어 디코더 동결, 비전 파트만 Chart-Text Alignment Data로 1 에포크 학습 (차트 시각 특징을 LLM 임베딩 공간에 매핑).
   - **Stage-2**: 비전 파트 동결, LoRA로 언어 모델을 Chart Instruction-Tuning Data로 3 에포크 학습.

3. **평가 프로토콜**:
   - Generation Ability Evaluation: GPT-4를 활용한 자유 형식 답변 정확도 평가 (Cohen's kappa 0.90).
   - Understanding Ability Evaluation: 객관식 QA 형식, GPT-4 불필요.

## Originality (독창성)

- 차트 이해를 위한 **최초의 대규모 instruction tuning 데이터셋**으로, 기존 데이터셋 대비 규모(600k), 태스크 다양성(9종), 답변 길이(평균 23.7 토큰)에서 압도적 우위.
- 9개 태스크를 아우르는 **최초의 인간 주석 차트 이해 벤치마크**로, 기존 벤치마크(ChartQA 등)의 한정적 평가 범위를 크게 확장.
- GPT-4V의 차트 이해 오류를 체계적으로 분석: Language Bias(35%), Perception Error(39%), Reasoning Error(15%), Lack of Knowledge(11%)로 분류하여, 향후 연구 방향을 구체적으로 제시.
- 비전 인코더 fine-tuning의 필요성을 ablation study로 입증 (ChartQA: 57.4 vs 54.2).

## Limitation & Further Study (한계 및 향후 연구)

- **모델 규모 제한**: 7B 파라미터 모델만 실험했으며, 13B 이상의 대규모 모델 실험은 GPU(A100) 부족으로 수행하지 못함.
- **Chart-to-DataTable/Json 성능 저조**: MMCA를 포함한 모든 모델이 이 두 태스크에서 매우 낮은 성능을 보이며, 이는 강력한 OCR 능력을 요구하는 태스크의 본질적 어려움을 반영.
- **다중 차트 이해 한계**: 다중 이미지 입력 학습 데이터 부족으로 Multiple Chart Understanding 성능이 상대적으로 낮음.
- **GPT-4 의존적 데이터 생성**: instruction tuning 데이터의 상당 부분이 GPT-4 생성이므로, GPT-4 자체의 한계(hallucination 포함)가 데이터 품질에 영향을 줄 수 있음.
- 향후 고해상도 비전 인코더, 세그멘테이션 기반 차트 요소 인식, 더 큰 규모의 LLM 백본 적용 등이 유망한 연구 방향.

## Evaluation (총평)

차트 이해라는 상대적으로 과소 연구된 영역에 대해 **데이터(MMC-Instruction), 벤치마크(MMC-Benchmark), 모델(MMCA)** 세 축을 모두 체계적으로 구축한 포괄적 연구이다. 특히 GPT-4V를 포함한 최신 모델들의 차트 이해 한계를 정량적으로 드러내고, 오류 유형을 세밀하게 분석한 점이 실용적 가치가 높다. 다만 7B 모델에 국한된 실험과 Chart-to-DataTable/Json의 근본적 한계 해결 방안이 미흡한 점은 아쉬움으로 남는다. 전반적으로 차트 멀티모달 이해 분야의 기반을 다진 중요한 기여로 평가된다.

## 평가
| 항목 | 점수 (1-5) |
|------|-----------|
| Novelty | 4 |
| Technical Soundness | 4 |
| Significance | 3 |
| Overall | 3.7 |

**총평**: 600K 멀티모달 차트 인스트럭션 데이터셋 MMC를 구축하고 이를 활용한 MMC-Instruction 모델로 차트 이해 분야의 데이터 부족 문제를 해소한 메릴랜드 대학의 실용적 기여이다.
