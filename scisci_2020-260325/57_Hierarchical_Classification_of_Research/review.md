# Hierarchical Classification of Research Fields in the "Web of Science" Using Deep Learning

> **저자**: Susie Xi Rao, Peter H. Egger, Ce Zhang | **날짜**: 2024-07-25 | **Journal**: (arXiv preprint) | **DOI**: 10.48550/arXiv.2302.00390

---

## Essence

Deep learning 기반 계층적 텍스트 분류 시스템을 구축하여 학술 논문의 초록만으로 3단계 계층(discipline 44개, field 718개, subfield 1,485개)에 자동 분류하는 체계를 제시했다. Microsoft Academic Graph(MAG)의 1.6억 편 초록을 대상으로 CNN, RNN, Transformer 모델 총 3,140개 실험을 수행한 결과, single-label 분류의 77.13%, multi-label 분류의 78.19%에서 정확도 90% 이상을 달성했다. 이 분류 체계를 활용하여 44개 분야 및 718개 field 간 학제 간 인용 점수(interfieldness score)를 산출했다.

## Motivation

학술 연구 활동을 분야별로 체계적으로 분류하는 것은 연구 평가, 학제 간 연구 측정, 커리어 계획 등에 필수적이다. 그러나 기존 분류 체계들은 개별 학문 분야(ACM, JEL, PACS 등)에 한정되거나, MAG의 FOS(Field of Study) 태그처럼 분야 간 세분화 수준(granularity)이 불균일하고 계층 구조가 체계적이지 않다는 한계가 있었다. DFG, OECD, NSF 등 연구비 기관의 분류 체계도 포괄적인 글로벌 계층 구조를 제공하지 못한다. 이에 Wikipedia의 "List of academic fields"와 분야별 기존 분류를 결합하여 44개 discipline을 아우르는 통합적 3단계 계층 분류 체계를 구축하고, 대규모 neural network 기반 자동 분류를 통해 학제 간 연구 분석의 기반을 마련하고자 했다.

## Achievement

1. **대규모 계층적 분류 시스템 구축**: 44 disciplines, 718 fields, 1,485 subfields를 포괄하는 3단계 분류 체계 설계 및 구현, 모듈화된 구조로 개별 분야 모델의 선택적 재학습 가능
2. **높은 분류 정확도**: CNN/RNN 기반 single-label에서 77.13%의 모델이 90%+ 정확도 달성, CNN 평균 precision 95.96%; multi-label에서도 78.19%의 모델이 90%+ 정확도 달성
3. **Transformer 보완 효과**: CNN/RNN에서 precision 70% 미만인 49개(single-label) 및 51개(multi-label) 모델에 Transformer 적용 시 최대 33.27%(single-label) 및 51.9%(multi-label) 개선
4. **학제 간 인용 분석 프레임워크**: 718 field 간 인용 입출력 행렬 기반으로 intra-field, inter-field(within-discipline), interdisciplinary 인용 점수를 체계적으로 정의 및 측정
5. **학제 간 패턴 발견**: Computer Science, Chemistry, Biology, Engineering이 높은 상호 인용 관계를 형성하며, Natural sciences는 상대적으로 낮은 학제 간성, Social sciences와 Humanities는 높은 학제 간성을 보임

## How

- **데이터**: MAG (2018-05-17 스냅샷) 약 1.6억 학술 논문 초록, Wikipedia "List of academic fields"와 ACM/JEL/PACS 등 분야별 분류 체계를 결합한 label 시스템
- **모델 아키텍처**: DNN, CNN, RNN(GloVe 임베딩 기반), BERT Transformer; 모듈화된 계층 구조로 Level 0(44 disciplines), Level 1(718 fields), Level 2(1,485 subfields) 각각에 개별 모델 배치
- **학습 설정**: top-3000 빈도 단어 사용, 텍스트 최대 200토큰, batch size 1024(CNN/RNN)/16(BERT), 1 epoch, RMSProp/Adam optimizer, 60/40 train-test split
- **인프라**: NVIDIA RTX 3090 GPU 8/4대, 504GB RAM, LMDB 기반 효율적 데이터 로딩, MLFlow 실험 추적, TensorFlow MirroredStrategy 분산 학습
- **인용 분석**: Multi-label 분류 결과를 기반으로 718x718 field 간 인용 행렬 구축, row-normalization 후 demand/supply/net output 행렬 분석, interfieldness 및 interdisciplinarity score 정의

## Originality

분야별로 존재하던 개별 분류 체계(ACM, JEL, PACS 등)를 Wikipedia의 포괄적 분류와 결합하여 44개 학문 전체를 아우르는 통합적 3단계 계층 분류를 최초로 시도한 점이 독창적이다. 특히 모듈화된 설계로 개별 분야 모델만 선택적으로 재학습할 수 있어 실용성이 높다. 또한 분류 결과를 단순한 카테고리 배정에 그치지 않고, field 수준의 세밀한 학제 간 인용 분석(interfieldness)으로 확장하여 학제 간 연구의 정량적 측정 프레임워크를 제공한 것이 차별점이다.

## Limitation & Further Study

### 저자들이 언급한 한계

- Multi-label 설정에서 동일 샘플이 train/test 양쪽에 배정될 수 있는 stratified sampling 문제 (iterative stratification 미적용)
- Label independence 가정의 한계 -- 실제로는 분야 간 상관관계 존재
- MAG 데이터의 FOS 태그 품질 문제로 training data 매칭률이 51.3%에 그침
- 약 4.7%의 모델에서 precision 70% 미만의 극히 저조한 성능
- MAG 서비스 종료 후 OpenAlex로의 전환 필요

### 리뷰어 판단 아쉬운 점

- **시간적 동태성 부재**: 1800-2018년 전체를 정적으로 분석하여 분야 구조의 시간적 변화를 포착하지 못함
- **1 epoch 학습의 한계**: 계산 효율성 우선으로 단일 epoch만 학습하여 모델 성능의 상한을 충분히 탐색하지 않음
- **LLM 시대의 기술적 진부화**: 2018년 MAG 데이터와 기본적인 CNN/RNN 위주의 접근은 현재 GPT/LLaMA 등 대형 언어 모델 대비 기술적으로 구식
- **분류 체계의 주관성**: Wikipedia 기반 44개 discipline 선정과 계층 구조 설계에 상당한 수작업과 주관적 판단이 개입됨
- **영어 초록 중심**: 비영어권 학술 출판물에 대한 처리 방안이 논의되지 않음
- **Ground truth 검증 부족**: 분류 정확도를 MAG의 기존 태그와 비교하나, 해당 태그 자체의 신뢰성 문제를 충분히 다루지 않음

### 후속 연구

- OpenAlex 데이터 기반으로 시스템 재구축 및 시계열 학제 간 동학 분석
- LLM(GPT, LLaMA 등) 기반 zero-shot/few-shot 분류와의 성능 비교
- Human-in-the-loop 방식의 Label Studio 통합을 통한 분류 품질 지속적 개선
- 분야별 composition score(예: 30% CS + 70% Economics) 도출을 위한 label powerset 접근
- 지리적 차원을 추가한 학제 간 인용 패턴 분석

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 3/5 |
| Technical Soundness | 3/5 |
| Significance | 4/5 |
| Clarity | 3/5 |
| Overall | 3/5 |

**총평**: 44개 학문 분야 전체를 아우르는 통합적 계층 분류 시스템과 field 수준 학제 간 인용 분석이라는 야심찬 목표를 제시하지만, 2018년 MAG 데이터와 기본적 neural network에 의존한 기술적 접근이 현재 기준으로 다소 구식이며, 분류 체계 설계의 주관성과 일부 모델의 저조한 성능이 아쉽다.
