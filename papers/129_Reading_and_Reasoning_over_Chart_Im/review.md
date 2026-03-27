# Reading and Reasoning over Chart Images for Evidence-based Automated Fact-Checking

- **저자**: Mubashara Akhtar, Oana Cocarascu, Elena Simperl
- **소속**: Department of Informatics, King's College London
- **발표**: arXiv:2301.11843, 2023
- **DOI**: [10.48550/ARXIV.2301.11843](https://doi.org/10.48550/ARXIV.2301.11843)

---

## Essence (본질)

차트 이미지를 근거(evidence)로 활용한 자동 팩트체킹(Automated Fact-Checking, AFC)이라는 새로운 태스크를 제안하고, 이를 위한 최초의 모델 ChartBERT와 벤치마크 데이터셋 ChartFC(15,886개 차트-주장 쌍)를 구축한 논문이다. 텍스트 주장(claim)이 차트 이미지에 의해 지지(supports)되는지 반박(refutes)되는지를 판별하는 이진 분류 문제를 정의하고, OCR 기반 텍스트 추출과 구조적 임베딩을 결합한 BERT 확장 모델을 제시한다.

## Motivation (동기)

- 기존 AFC 연구는 텍스트, 테이블, 이미지(위변조 탐지) 중심이었으며, 차트 이미지를 근거로 한 주장 검증은 사실상 미탐구 영역이었다.
- 차트는 뉴스, 보고서, 과학 논문, SNS에서 광범위하게 사용되며, COVID-19 팬데믹 시기 정책 결정과 대중 커뮤니케이션에 핵심적 역할을 했다.
- 차트를 통한 미정보 전파는 의도적 왜곡 설계뿐 아니라 해석 과정(잘못된 비교, 상관/인과 혼동 등)에서도 발생하므로, 차트와 주장을 함께 이해하는 자동 검증 시스템이 필요하다.
- 기존 vision-language 모델들은 차트 고유의 구조적 정보(축 레이블, 범례, 바 위치 등)를 종합적으로 처리하는 데 한계가 있다.

## Achievement (성과)

- **ChartBERT 모델**: OCR 기반 읽기 컴포넌트 + 시퀀스 생성 컴포넌트 + 구조적 임베딩이 추가된 BERT 인코더로 구성된 최초의 차트 팩트체킹 모델. 63.8% 테스트 정확도 달성.
- **ChartFC 데이터셋**: TabFact를 시드로 자동 생성한 15,886개 차트-주장 쌍. 인간 평가에서 92% 검증 가능성 확인.
- **체계적 베이스라인 평가**: 5개 비전 인코더 x 3개 언어 인코더 x 5개 퓨전 방법 = 75개 VL 베이스라인을 체계적으로 평가. 최고 VL 베이스라인(BERT+ResNet+concatenation)은 62.7% 정확도.
- **추론 유형 분석**: 7가지 차트 추론 유형(retrieve value, filter, comparison, compute derived value, find extremum, determine range, find anomalies) 분류 체계를 적용하여, compute derived value에서 모델이 특히 취약함(38%)을 규명.

## How (방법)

1. **ChartBERT 아키텍처**:
   - **(1) Reading Component**: Tesseract OCR로 차트 이미지에서 텍스트 영역과 바운딩 박스(x, y, w, h) 추출.
   - **(2) Sequence Generation**: 추출된 텍스트를 (a) 좌표 기반 연결(concatenation) 또는 (b) 템플릿 기반(tmp1~tmp3) 시퀀스로 변환. tmp3("athlete is usain bolt when rank is 1") 형태가 최고 성능.
   - **(3) Encoding**: BERT 아키텍처에 x좌표 임베딩, y좌표 임베딩, 레이블 임베딩(축 레이블 여부) 3가지 구조적 임베딩을 추가하여 차트의 공간적 구조 학습.
   - **(4) Classification**: [CLS] 토큰 표현에 FC 레이어 + sigmoid로 supports/refutes 이진 분류.

2. **ChartFC 데이터셋 구축**:
   - TabFact(117k 주장, 16k Wikipedia 테이블)에서 출발.
   - 주장-테이블 열 링크 -> 서브테이블 생성(최대 20행, 2열) -> matplotlib/seaborn으로 바 차트 생성.
   - 차트 변형: 방향(수평/수직), 바 색상(녹/청/분홍), 배경(그리드 유무, 흰색/회색).

3. **VL 베이스라인 체계적 평가**:
   - 언어 인코더: BERT Embedder, LSTM, BERT
   - 비전 인코더: FC layer, AlexNet, ResNet-152, DenseNet, ViT
   - 퓨전: concatenation, multiplication, concatenation+GRU, MCB, Transformer layers

## Originality (독창성)

- **차트 기반 팩트체킹이라는 완전히 새로운 태스크**를 정의한 최초의 연구. 기존 AFC(텍스트/테이블/이미지 위변조)와 차트 QA/요약과는 본질적으로 다른 문제를 제기.
- BERT에 차트 고유의 **구조적 임베딩**(x/y 좌표, 레이블 임베딩)을 추가하여, 차트의 공간적 배치 정보를 텍스트 표현에 통합하는 접근이 독창적.
- 75개 VL 베이스라인의 **대규모 체계적 비교**를 통해, 인코더/퓨전 방법 선택이 성능에 미치는 영향을 정밀하게 분석한 점이 방법론적으로 의미 있다.
- 차트 추론 유형 분류(Amar et al., 2005 기반)를 팩트체킹에 적용하여, 모델의 실패 패턴을 추론 능력별로 진단한 분석이 통찰력 있다.

## Limitation & Further Study (한계 및 향후 연구)

- **바 차트만 포함**: TabFact 시드 데이터의 특성상 바 차트에만 국한되며, 파이 차트, 라인 차트, 산점도 등 다양한 차트 유형으로의 확장이 필수적.
- **합성 차트 사용**: matplotlib/seaborn으로 자동 생성된 차트만 사용하여 스타일 변화가 제한적. 실제 뉴스/보고서의 자연 차트는 훨씬 다양한 디자인 요소를 포함.
- **영어 전용**: 다국어 미정보 확산 현실을 반영하지 못함.
- **정확도 63.8%의 한계**: 최고 성능이 63.8%로, 실용적 배포에는 상당한 개선이 필요. 특히 compute derived value(38%) 등 수치 추론이 필요한 주장에서 취약.
- **이진 분류 한정**: supports/refutes만 판별하며, "Not Enough Information" 등 더 세밀한 판정 라벨이 없음.
- 향후 자연 차트 기반 데이터셋, 다중 차트 유형 확장, 수치 추론 강화 모델, 다국어 지원 등이 필요.

## Evaluation (총평)

차트 이미지 기반 팩트체킹이라는 중요하고 시의적절한 새 태스크를 정의하고, 모델(ChartBERT)과 데이터셋(ChartFC)을 함께 제공한 선구적 연구이다. 75개 VL 베이스라인의 대규모 체계적 평가와 추론 유형별 오류 분석은 후속 연구에 귀중한 참고점을 제공한다. 다만 바 차트/합성 데이터에만 국한된 실험 설계와 63.8%라는 아직 낮은 정확도는 연구의 초기 단계를 반영하며, 실세계 차트의 복잡성과 다양성을 다루기 위한 상당한 후속 연구가 요구된다.

## 평가
| 항목 | 점수 (1-5) |
|------|-----------|
| Novelty | 4 |
| Technical Soundness | 3 |
| Significance | 3 |
| Overall | 3.3 |

**총평**: 차트 팩트 체킹이라는 새 과제를 정의하고 15,886쌍의 ChartFC 데이터셋과 ChartBERT 모델을 제시한 연구로, 과제 정의의 독창성은 높으나 모델 성능과 데이터 다양성의 한계가 있다.
