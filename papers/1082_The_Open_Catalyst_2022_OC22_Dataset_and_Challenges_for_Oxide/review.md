---
title: "1082_The_Open_Catalyst_2022_OC22_Dataset_and_Challenges_for_Oxide"
authors:
  - "Richard Tran"
  - "Janice Lan"
  - "Muhammed Shuaibi"
  - "Brandon M. Wood"
  - "Siddharth Goyal"
date: "2023.03"
doi: "10.1021/acscatal.2c05426"
arxiv: ""
score: 4.0
essence: "1.2백만 개 이상의 DFT 계산을 포함한 Open Catalyst 2020 (OC20) 데이터셋을 개발하여 산화물 전기촉매의 기계학습 모델 개발을 가능하게 했다."
tags:
  - "cat/Science_of_Science_Research"
  - "sub/AI_and_Large_Language_Models"
  - "topic/scisci"
---

# The Open Catalyst 2022 (OC22) Dataset and Challenges for Oxide Electrocatalysts

> **저자**: Richard Tran, Janice Lan, Muhammed Shuaibi, Brandon M. Wood, Siddharth Goyal, Abhishek Das, Javier Heras-Domingo, Adeesh Kolluru, Ammar Rizvi, Nima Shoghi, Anuroop Sriram, Félix Therrien, Jehad Abed, Oleksandr Voznyy, Edward H. Sargent, Zachary Ulissi, C. Lawrence Zitnick | **날짜**: 2023-03-03 | **DOI**: [10.1021/acscatal.2c05426](https://doi.org/10.1021/acscatal.2c05426)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1: Adsorbates, materials, calculations,*

1.2백만 개 이상의 DFT 계산을 포함한 Open Catalyst 2020 (OC20) 데이터셋을 개발하여 산화물 전기촉매의 기계학습 모델 개발을 가능하게 했다.

## Motivation

- **Known**: 촉매 발견과 최적화는 재생 에너지 및 환경 문제 해결에 중요하나, 기존 촉매 데이터셋은 다른 분야 대비 규모가 작아 머신러닝 모델의 일반화 능력이 제한적이었다.
- **Gap**: 헤테로 촉매 모델링을 위한 대규모 데이터셋 부재로 인해 다양한 원소 조성, 흡착분자 종류와 배치에 걸친 일반화 가능한 머신러닝 모델 개발이 어려웠다.
- **Why**: 대규모 다양한 촉매 데이터셋은 더 정확하고 일반화된 머신러닝 모델을 가능하게 하여 재생에너지, 연료전지, 비료 생산 등 사회적으로 중요한 문제 해결에 기여할 수 있다.
- **Approach**: Materials Project의 안정적 물질들로부터 55개 원소를 포함한 저밀러지수 표면에 82개 흡착분자를 배치하고 DFT 이완 계산(1.2백만 개 이상)을 수행하여 포괄적 데이터셋을 구축했으며, 세 가지 도메인 챌린지 태스크를 정의했다.

## Achievement

![Figure 1](figures/fig1.webp)

*Figure 1: Adsorbates, materials, calculations,*

- **대규모 데이터셋 구축**: 1,281,040개 DFT 이완 계산과 약 264,890,000개 단일점 평가를 포함하는 OC20 데이터셋 개발
- **포괄적 화학 공간 커버**: 55개 원소, 82개 흡착분자(질소, 탄소, 산소 화학 포함)를 포함하는 광범위한 촉매 및 흡착 시스템 고려
- **부가 정보 제공**: 이완 궤적, 바더 전하, LOBSTER 궤도 정보, 분자동역학 궤적 및 구조 섭동 데이터 포함
- **기준 모델 제시**: CGCNN, SchNet, DimeNet++ 등 그래프 신경망 모델 구현으로 커뮤니티 기준점 제공
- **공개 리더보드 플랫폼**: 커뮤니티 기여를 촉진하기 위한 공개 경쟁 및 오픈소스 소프트웨어 저장소 제공

## How

![Figure 2](figures/fig2.webp)

*Figure 2: The adsorbates used to generate the Open Catalyst Dataset contain oxygen, hydrogen, C1,*

- Materials Project에서 안정적 물질 선정 및 무작위로 저밀러지수 표면 샘플링
- 각 표면-흡착분자 조합에 대해 DFT 이완 계산 수행
- 구조 이완 전 원자 위치 무작위 섭동 및 단일점 DFT 계산
- 고온 ab initio 분자동역학(MD) 궤적 계산으로 모델 강건성 향상
- 세 가지 관련 태스크 정의: (1) Structure to Energy and Forces (S2EF), (2) Initial Structure to Relaxed Structure (IS2RS), (3) Initial Structure to Relaxed Adsorption Energy (IS2RE)
- Train/validation/test 분할로 보이지 않은 흡착분자, 결정 구조, 혹은 둘 다에 대한 일반화 능력 평가

## Originality

- 촉매 분야에서 전례 없는 규모(1.2백만+)의 DFT 데이터셋 구축으로 대규모 머신러닝 모델 훈련 가능 개시
- 다양한 원소(55개), 흡착분자(82개), 표면 배치를 포함한 포괄적 화학 공간 커버로 일반화 능력 강화
- 이완 궤적, 분자동역학, 구조 섭동 등 다양한 보조 정보 포함으로 모델 학습 풍부화
- 명확한 기차/검증/시험 분할 및 공개 경쟁 플랫폼으로 커뮤니티 표준화 연구 환경 조성
- 오픈소스 기준 모델 및 학습 인프라 제공으로 재현성 및 후속 연구 접근성 확보

## Limitation & Further Study

- 단일 흡착분자만 고려하여 다중 흡착분자 상호작용 미반영
- 이상화된 표면 구조로 실제 반응 조건(온도, 압력, 용매, 운동론 등)의 복잡성 미포함
- 계산된 DFT 스냅샷 기반으로 전체 반응 경로 및 전이 상태 에너지 장벽 예측 능력 제한
- 기준 모델 결과에서 상한선 부재로 더 큰 모델의 성능 한계 불명확
- **후속 연구 방향**: 다중 흡착분자, 용매 효과, 운동론 포함 확장; 더 큰 규모 모델 개발; 전이 상태 계산 추가; 실험 검증

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 이 연구는 촉매 과학 분야에 전례 없는 규모의 고품질 DFT 데이터셋을 제공함으로써 머신러닝 모델의 실질적 응용을 가능하게 하는 중요한 기여를 했으며, 공개 플랫폼과 명확한 벤치마크를 통해 커뮤니티 주도의 진전을 촉진했다.

## Related Papers

- 🏛 기반 연구: [[papers/1075_Open_Catalyst_2020_OC20_Dataset_and_Community_Challenges/review]] — OC20 데이터셋의 후속 버전으로 산화물 전기촉매 연구를 위한 더 확장된 DFT 계산 데이터를 제공한다.
- 🧪 응용 사례: [[papers/1070_Challenges_in_High-Throughput_Inorganic_Materials_Prediction/review]] — 무기 재료 예측의 고처리량 방법론이 전기촉매 재료 설계에 직접 적용될 수 있는 방법론적 기반을 제공한다.
