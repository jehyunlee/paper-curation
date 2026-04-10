---
title: "403_Highly_accurate_protein_structure_prediction_with_AlphaFold"
authors:
  - "John Jumper"
  - "Richard Evans"
  - "Alexander Pritzel"
  - "Tim Green"
  - "Michael Figurnov"
date: "2021.08"
doi: "10.1038/s41586-021-03819-2"
arxiv: ""
score: 5.0
essence: "AlphaFold는 아미노산 서열만으로 단백질의 3차원 구조를 원자 수준의 정확도로 예측하는 딥러닝 모델로, 50년 이상의 단백질 폴딩 문제를 근본적으로 해결한 획기적인 성과이다."
tags:
  - "cat/AI-Powered_Scientific_Research_Frameworks"
  - "sub/Protein_Structure_Prediction"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Jumper et al._2021_Highly accurate protein structure prediction with AlphaFold.pdf"
---

# Highly accurate protein structure prediction with AlphaFold

> **저자**: John Jumper, Richard Evans, Alexander Pritzel, Tim Green, Michael Figurnov, Olaf Ronneberger, Kathryn Tunyasuvunakool, Russ Bates, Augustin Žídek, Anna Potapenko, Alex Bridgland, Clemens Meyer, Simon A. A. Kohl, Andrew J. Ballard, Andrew Cowie, Bernardino Romera-Paredes, Stanislav Nikolov, Rishub Jain, Jonas Adler, Trevor Back, Stig Petersen, David Reiman, Ellen Clancy, Michal Zielinski, Martin Steinegger, Michalina Pacholska, Tamas Berghammer, Sebastian Bodenstein, David Silver, Oriol Vinyals, Andrew W. Senior, Koray Kavukcuoglu, Pushmeet Kohli, Demis Hassabis | **날짜**: 2021-08-26 | **DOI**: [10.1038/s41586-021-03819-2](https://doi.org/10.1038/s41586-021-03819-2)

---

## Essence

AlphaFold는 아미노산 서열만으로 단백질의 3차원 구조를 원자 수준의 정확도로 예측하는 딥러닝 모델로, 50년 이상의 단백질 폴딩 문제를 근본적으로 해결한 획기적인 성과이다.

## Motivation

- **Known**: 약 100,000개의 단백질 구조가 실험적으로 규명되었으나, 이는 알려진 수십억 개의 단백질 서열의 극히 일부에 불과함. 기존 방법들은 상동 구조(homologous structure)가 없는 경우 원자 수준의 정확도를 달성하지 못함.

- **Gap**: 단백질 구조 결정에는 수개월에서 수년의 실험 작업이 필요하며, 계산 생물학적 접근이 이 병목을 해결할 필요가 있음. 50년 이상 열린 문제인 "단백질 폴딩 문제(protein folding problem)"의 구조 예측 부분이 미해결 상태.

- **Why**: 대규모 구조 생물정보학(structural bioinformatics)을 활성화하고, 생물의학 연구에 필요한 구조 정보를 신속하게 제공할 필요가 있음.

- **Approach**: 진화적 정보(다중 서열 정렬, MSA), 물리적 제약, 기하학적 제약을 통합하는 혁신적인 신경망 아키텍처 설계. CASP14(Critical Assessment of protein Structure Prediction) 평가에서 성능 검증.

## Achievement

![Figure 1](figures/fig1.webp)
*AlphaFold가 생성한 고정확도 구조: (a) CASP14 데이터셋에서 다른 상위 15개 방법과의 성능 비교, (b-d) 정확한 백본 및 사이드 체인 예측, 특히 큰 단백질의 도메인 패킹 정확도 시연*

1. **CASP14 벤치마크에서의 압도적 성능**: 
   - 백본 정확도(Cα r.m.s.d.₉₅): 중앙값 0.96 Å (신뢰 구간 0.85–1.16 Å)
   - 차상위 방법: 2.8 Å (2.7–4.0 Å) — 약 3배 향상
   - 전체 원자 정확도: 1.5 Å r.m.s.d.₉₅ vs. 차상위 3.5 Å
   - 탄소 원자 폭(~1.4 Å)과 비슷한 수준의 정밀도 달성

2. **일반화 및 신뢰도**:
   - 최근 PDB에 등록된 구조(학습 데이터 컷오프 이후)에서도 높은 정확도 유지 (Figure 2)
   - 예측된 국소 거리 차이 검사(pLDDT) 지표가 실제 정확도를 신뢰할 수 있게 예측
   - 2,180개 잔기 단백질의 정확한 도메인 패킹 예측 가능

## How

![Figure 3](figures/fig3.webp)
*Evoformer 블록의 구조: MSA 표현과 페어 표현 간의 정보 흐름을 보여주는 그래프 추론 프레임워크*

**네트워크 아키텍처의 핵심 혁신**:

- **Evoformer (진화 변환기)**: 
  - 다중 서열 정렬(MSA)을 N_seq × N_res 배열로, 잔기 쌍을 N_res × N_res 배열로 표현
  - MSA 표현이 페어 표현으로의 외적(outer product) 연산을 통해 매 블록에서 지속적으로 업데이트 (기존 방식의 일회성 적용 개선)
  - 그래프 추론 문제로 단백질 구조 예측을 재정의 (엣지 = 인접한 잔기 간의 관계)

- **구조 모듈(Structure Module)**:
  - 각 잔기의 회전과 변환(global rigid body frames)으로 명시적 3D 구조 도입
  - 체인 구조 분리로 구조의 모든 부분의 동시적 국소 정제 가능
  - 등변(equivariant) 트랜스포머: 명시적으로 표현되지 않은 사이드 체인 원자에 대한 암시적 추론
  - 방향성 정확도에 큰 가중치를 두는 손실 함수

- **반복적 정제(Recycling)**:
  - 컴퓨터 비전에서 영감받은 기법으로, 손실을 반복 계산하고 출력을 같은 모듈에 재귀적으로 입력
  - 최소한의 추가 학습 시간으로 상당한 정확도 개선

- **학습 전략**:
  - 마스크된 MSA 손실(masked MSA loss): 비표지 단백질 서열로부터 자기 증류(self-distillation) 학습
  - 중간 손실(intermediate loss)을 사용한 단계적 정제
  - 자신의 정확도 추정치 학습

## Originality

- **구조 문제의 그래프 추론 재정의**: 전통적 물리 기반 또는 진화 기반 접근과 달리, 페어 표현을 통한 직접적 공간-진화 관계 추론
  
- **Evoformer의 혁신적 설계**: MSA와 페어 표현의 지속적 양방향 통신으로 진화적 신호의 효율적 처리

- **등변 구조 모듈**: 3D 기하학적 제약을 신경망에 내재화하여 명시적 좌표 예측 가능

- **자기 증류 및 신뢰도 추정**: 비표지 데이터 활용 및 예측 신뢰도의 정량적 평가로 실무 적용성 향상

## Limitation & Further Study

- **계산 비용**: 큰 단백질의 MSA 구성에 상당한 계산 자원 필요. 매우 깊은 MSA 처리 방안 필요
  
- **단량체 예측 중심**: 복합체(complex) 구조 예측 능력은 논문에서 제한적으로 다루어짐

- **템플릿 의존성**: 템플릿이 있는 경우와 없는 경우의 성능 차이 분석 필요

- **후속 과제**: 
  - 단백질 상호작용 및 복합체 구조 예측으로 확장
  - 동적 구조 변화(conformational dynamics) 예측
  - 구조 기반 약물 설계 등 실제 응용에서의 검증
  - 해석 가능성(interpretability) 강화


## Evaluation

- Novelty: 5/5
- Technical Soundness: 5/5
- Significance: 5/5
- Clarity: 4/5
- Overall: 5/5

**총평**: 이 논문은 50년 이상 미해결된 단백질 폴딩 문제를 딥러닝으로 거의 완전히 해결한 역사적 성과로, 진화적 정보와 기하학적 제약을 창의적으로 통합한 혁신적 아키텍처를 제시하며, 구조 생물학과 생의학 연구에 패러다임 전환을 가져왔다.

## Related Papers

- 🔗 후속 연구: [[papers/046_Accurate_structure_prediction_of_biomolecular_interactions_w/review]] — AlphaFold의 단일 단백질 구조 예측을 생체분자 복합체 상호작용 예측으로 확장한 직접적인 발전이다
- 🧪 응용 사례: [[papers/1129_SARS-CoV-2_simulations_go_exascale_to_predict_dramatic_spike/review]] — 정확한 단백질 구조 예측이 바이러스 스파이크 단백질의 동역학 시뮬레이션과 약물 타겟 발견에 필수적인 출발점을 제공한다
- 🏛 기반 연구: [[papers/718_Scientific_discovery_in_the_age_of_artificial_intelligence/review]] — 단백질 폴딩 문제 해결이 AI를 통한 과학적 발견의 대표적 성공사례로서 AI4Science 발전의 이정표가 되었다
- 🔗 후속 연구: [[papers/342_Foundation_Models_for_Environmental_Science_A_Survey_of_Emer/review]] — 단백질 구조 예측의 성공이 환경 과학 분야 파운데이션 모델 개발에 중요한 방법론적 영감을 제공한다
- 🔄 다른 접근: [[papers/1060_Accurate_prediction_of_protein_structures_and_interactions_u/review]] — AlphaFold2와 유사한 정확도를 다른 3-트랙 신경망으로 달성한 대안적 접근
- 🏛 기반 연구: [[papers/046_Accurate_structure_prediction_of_biomolecular_interactions_w/review]] — AlphaFold 2의 단일 단백질 구조 예측 기술을 기반으로 생체분자 복합체 예측으로 확장한 직접적인 후속 연구이다
- 🏛 기반 연구: [[papers/718_Scientific_discovery_in_the_age_of_artificial_intelligence/review]] — AlphaFold와 같은 획기적 성과들이 AI를 통한 과학적 발견 변모에 대한 종합적 조망의 대표적 사례로 제시된다
- 🔗 후속 연구: [[papers/065_Agentic_End-to-End_De_Novo_Protein_Design_for_Tailored_Dynam/review]] — AlphaFold의 구조 예측을 넘어 동역학적 특성까지 제어 가능한 단백질 설계로 확장합니다.
- 🏛 기반 연구: [[papers/1129_SARS-CoV-2_simulations_go_exascale_to_predict_dramatic_spike/review]] — 단백질 구조 예측 기술이 바이러스 스파이크 단백질의 동역학 시뮬레이션에 필수적인 구조적 기반을 제공한다
