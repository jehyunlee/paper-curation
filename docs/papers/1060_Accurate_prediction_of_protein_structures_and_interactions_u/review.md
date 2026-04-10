---
title: "1060_Accurate_prediction_of_protein_structures_and_interactions_u"
authors:
  - "Minkyung Baek"
  - "Frank DiMaio"
  - "Ivan Anishchenko"
  - "Justas Dauparas"
  - "Sergey Ovchinnikov"
date: "2021.08"
doi: "10.1126/science.abj8754"
arxiv: ""
score: 4.0
essence: "3-트랙 신경망 아키텍처를 이용하여 1D 서열, 2D 거리 지도, 3D 좌표 정보를 동시에 처리함으로써 AlphaFold2에 근접한 단백질 구조 예측 정확도를 달성하고 단백질-단백질 복합체 모델링을 가능하게 했다."
tags:
  - "cat/LLM-Based_Scientific_Reasoning"
  - "sub/Domain-specific_Scientific_Reasoning"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Baek et al._2021_Accurate prediction of protein structures and interactions using a three-track neural network.pdf"
---

# Accurate prediction of protein structures and interactions using a three-track neural network

> **저자**: Minkyung Baek, Frank DiMaio, Ivan Anishchenko, Justas Dauparas, Sergey Ovchinnikov, Gyu Rie Lee, Jue Wang, Qian Cong, Lisa N. Kinch, R. Dustin Schaeffer, Claudia Millán, Hahnbeom Park, Carson Adams, Caleb R. Glassman, Andy DeGiovanni, Jose H. Pereira, Andria V. Rodrigues, Alberdina A. Van Dijk, Ana C. Ebrecht, Diederik J. Opperman, Theo Sagmeister, Christoph Buhlheller, Tea Pavkov-Keller, Manoj K. Rathinaswamy, Udit Dalwadi, Calvin K. Yip, John E. Burke, K. Christopher Garcia, Nick V. Grishin, Paul D. Adams, Randy J. Read, David Baker | **날짜**: 2021-08-20 | **DOI**: [10.1126/science.abj8754](https://doi.org/10.1126/science.abj8754)

---

## Essence

![Figure 1](figures/fig1.webp)

*Fig. 1. Network architecture and performance.*

3-트랙 신경망 아키텍처를 이용하여 1D 서열, 2D 거리 지도, 3D 좌표 정보를 동시에 처리함으로써 AlphaFold2에 근접한 단백질 구조 예측 정확도를 달성하고 단백질-단백질 복합체 모델링을 가능하게 했다.

## Motivation

- **Known**: AlphaFold2가 CASP14에서 획기적인 성능을 보였고, 딥러닝 방법이 단백질 구조 예측에서 기존 방법들을 능가한다는 것이 알려져 있다.
- **Gap**: AlphaFold2의 상세한 방법론이 공개되지 않아 학계에서 유사한 성능을 달성할 수 있는지, 그리고 더 효율적인 아키텍처가 가능한지 불명확했다.
- **Why**: 단백질 구조 예측은 생물학적 기능 이해와 신약 개발에 필수적이며, 접근 가능한 방법의 제시는 구조생물학 연구를 가속화할 수 있다.
- **Approach**: AlphaFold2의 핵심 아이디어(MSA 활용, attention 메커니즘, SE(3)-equivariant 변환, end-to-end 학습)를 기반으로 1D-2D-3D 정보를 동시에 처리하는 3-트랙 신경망을 설계하여 성능을 최적화했다.

## Achievement

![Figure 2](figures/fig2.webp)

*Fig. 2. Enabling experimental structure determination with RoseTTAFold.*

- **CASP14 성능**: 3-트랙 모델이 AlphaFold2에 근접한 구조 예측 정확도를 달성했으며, BAKER-ROSETTASERVER와 2-트랙 모델을 명확히 능가했다.
- **실험 구조 결정 가능**: X-ray 결정학 및 cryo-EM 모델링 문제를 신속하게 해결할 수 있어 실험 구조생물학 연구를 지원했다.
- **단백질 복합체 모델링**: 서열 정보만으로 정확한 단백질-단백질 복합체 모델을 생성하여 기존의 개별 소단위체 모델링 후 도킹 방식을 단축했다.
- **기능 통찰 제공**: 알려지지 않은 구조의 단백질에 대한 기능 정보를 제공하여 생물학적 해석을 가능하게 했다.
- **커뮤니티 공개**: RoseTTAFold 방법을 과학 커뮤니티에 공개하여 생물학 연구를 가속화했다.

## How

![Figure 1](figures/fig1.webp)

*Fig. 1. Network architecture and performance.*

- 다중 서열 정렬(MSA, Multiple Sequence Alignment)을 입력으로 사용하여 생물학적 정보를 최대한 활용
- 1D 서열 트랙: 아미노산 서열 정보 처리
- 2D 거리 지도 트랙: 잔기 간 거리 및 방향 정보 처리
- 3D 좌표 트랙: 백본 원자 좌표를 SE(3)-equivariant 변환으로 처리
- 세 트랙 간 정보 흐름: 1D-2D-3D 간 반복적인 정보 변환 및 통합
- Attention 메커니즘: 서열상 거리가 먼 잔기 간 상호작용 모델링
- End-to-end 학습: 서열 입력부터 3D 좌표까지 역전파를 통한 전체 매개변수 최적화
- 하드웨어 제약 극복: 260개 잔기의 불연속 서열 세그먼트 조합으로 대규모 단백질 처리
- 두 가지 최종 모델링 방식: (1) 예측된 거리/방향을 pyRosetta로 입력하여 전원자 모델 생성, (2) SE(3)-equivariant 레이어로 직접 백본 좌표 생성

## Originality

- AlphaFold2의 2-트랙 아키텍처를 3-트랙으로 확장하여 3D 좌표 정보의 더 밀접한 통합을 달성한 혁신적 아키텍처
- 1D, 2D, 3D 정보 간 양방향 정보 흐름을 통해 상호 보완적 추론이 가능하도록 설계
- 하드웨어 제약 조건 하에서 불연속 시퀀스 조합 전략으로 대규모 단백질 모델링 가능하게 함
- 단백질-단백질 복합체의 직접 예측으로 기존의 다단계 도킹 과정을 단축한 실용적 혁신

## Limitation & Further Study

- AlphaFold2보다 여전히 정확도가 낮은데, 이는 하드웨어 메모리 제약(모델 크기 제한), 다른 아키텍처/손실함수 선택, 추론 강도 차이에서 비롯된 것으로 보인다.
- GPU 메모리 요구사항이 상대적으로 높아서(전체 end-to-end 모델의 경우 24GB) 접근성 제약이 있을 수 있다.
- MSA 깊이와 모델 정확도 간 상관성이 기존 방법보다 낮아 특정 시나리오에서의 성능 예측이 어렵다.
- 후속 연구 방향: (1) 더 효율적한 3D 트랙 아키텍처 탐색, (2) 손실함수 최적화, (3) 하드웨어 발전에 따른 모델 확장, (4) 추가 MSA 데이터 활용, (5) 단백질 설계 역방향 문제로의 확장

## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: RoseTTAFold는 AlphaFold2의 핵심 개념을 3-트랙 아키텍처로 창의적으로 재구성하여 경쟁력 있는 성능을 달성했으며, 특히 공개 방식으로 제공됨으로써 단백질 구조 예측의 민주화와 구조생물학 연구 가속화에 크게 기여하는 획기적인 연구다.

## Related Papers

- 🔗 후속 연구: [[papers/487_Leveraging_biomolecule_and_natural_language_through_multi-mo/review]] — 단백질 구조 예측을 생물분자 다중모달 학습으로 확장한 포괄적 연구
- 🔄 다른 접근: [[papers/403_Highly_accurate_protein_structure_prediction_with_AlphaFold/review]] — AlphaFold2와 유사한 정확도를 다른 3-트랙 신경망으로 달성한 대안적 접근
- 🧪 응용 사례: [[papers/1106_The_BOS-Lig_Dataset_Accurate_Ligand_Charges_from_a_Consensus/review]] — 단백질 구조 예측 기술을 리간드 전하 예측 등 구체적 응용으로 확장
- 🔗 후속 연구: [[papers/686_Robust_deep_learning_based_protein_sequence_design_using_Pro/review]] — 단백질 구조 예측을 견고한 딥러닝 기반 서열 설계로 발전시킨 연구
- 🏛 기반 연구: [[papers/487_Leveraging_biomolecule_and_natural_language_through_multi-mo/review]] — 단백질 구조 예측 연구가 생물분자 다중모달 학습의 핵심 기반 기술
