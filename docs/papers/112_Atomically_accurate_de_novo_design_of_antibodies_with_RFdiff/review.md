---
title: "112_Atomically_accurate_de_novo_design_of_antibodies_with_RFdiff"
authors:
  - "Nathaniel R. Bennett"
  - "Joseph L. Watson"
  - "Robert J. Ragotte"
  - "Andrew J. Borst"
  - "DéJenaé L. See"
date: "2025.02"
doi: "10.1101/2024.03.14.585103"
arxiv: ""
score: 0
essence: "본 연구는 RFdiffusion 신경망의 항체 특화 미세조정을 통해 원자 수준의 정확도로 사용자가 지정한 에피토프(epitope)에 결합하는 항체 가변 영역(VHH, scFv)을 완전히 컴퓨터 기반으로 설계할 수 있음을 처음으로 입증했다. 초기 계산 설계부터 효율성 성숙(affinity maturation)까지 체계화된 파이프라인을 제시하고 크라이오-EM 구조 검증으로 설계 정확도를 확인했다."
tags:
  - "cat/AI-Powered_Scientific_Research_Frameworks"
  - "sub/Protein_Structure_Prediction"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Bennett et al._2025_Atomically accurate de novo design of antibodies with RFdiffusion.pdf"
---

# Atomically accurate de novo design of antibodies with RFdiffusion

> **저자**: Nathaniel R. Bennett, Joseph L. Watson, Robert J. Ragotte, Andrew J. Borst, DéJenaé L. See, Connor Weidle, Riti Biswas, Yutong Yu, Ellen L. Shrock, Russell Ault, Philip J. Y. Leung, Buwei Huang, Inna Goreshnik, John Tam, Kenneth D. Carr, Benedikt Singer, Cameron Criswell, Basile I. M. Wicky, Dionne Vafeados, Mariana Garcia Sanchez, Ho Min Kim, Susana Vázquez Torres, Sidney Chan, Shirley M. Sun, Timothy Spear, Yi Sun, Keelan O'Reilly, John M. Maris, Nikolaos G. Sgourakis, Roman A. Melnyk, Chang C. Liu, David Baker | **날짜**: 2025-02-28 | **DOI**: [10.1101/2024.03.14.585103](https://doi.org/10.1101/2024.03.14.585103)

---

## Essence

본 연구는 RFdiffusion 신경망의 항체 특화 미세조정을 통해 원자 수준의 정확도로 사용자가 지정한 에피토프(epitope)에 결합하는 항체 가변 영역(VHH, scFv)을 완전히 컴퓨터 기반으로 설계할 수 있음을 처음으로 입증했다. 초기 계산 설계부터 효율성 성숙(affinity maturation)까지 체계화된 파이프라인을 제시하고 크라이오-EM 구조 검증으로 설계 정확도를 확인했다.

## Motivation

- **Known**: 항체는 현대 의약품의 핵심이지만 현재의 항체 개발은 동물 면역화(immunization) 또는 무작위 라이브러리 스크리닝에 의존하고 있다. 기존 계산 설계 방법들은 기존 항체 구조에 잔기를 이식하거나 깊은학습 네트워크를 통해 항체 서열을 설계하지만, 원자 수준의 정확도를 갖춘 de novo 항체 설계는 아직 달성되지 않았다.

- **Gap**: 원본 RFdiffusion(vanilla RFdiffusion)은 일반 이차 구조(α-helix, β-strand)에 기반한 결합을 주로 설계하므로 항체의 특징인 복잡한 CDR(상보성 결정 영역, complementarity-determining region) 루프를 포함한 de novo 항체 설계에 실패한다.

- **Why**: 항체는 특이적이고 높은 친화도를 갖춘 치료제이므로 임의의 에피토프를 표적할 수 있는 이상적인 de novo 항체 설계 방법이 절실하다. 이는 (1) 임의의 에피토프 표적화, (2) 최적화된 항체 프레임워크 구조 유지, (3) 항체의 강체 위치 샘플링을 가능해야 한다.

- **Approach**: RFdiffusion과 RoseTTAFold2(RF2)를 항체 구조에 대해 미세조정(fine-tuning)하여 CDR-매개 인터페이스 설계에 특화시키고, ProteinMPNN을 이용한 서열 설계, yeast display 스크리닝, OrthoRep을 통한 친화도 성숙, 그리고 크라이오-EM 구조 검증을 포함한 통합 파이프라인을 구축했다.

## Achievement

1. **RFdiffusion 항체 설계 능력 확립**: 프로젝트 시작 시 항체 구조의 PDB 비율이 매우 낮음(~8,100개 vs >200,000개 전체 구조)에도 불구하고, 전체 PDB에서 학습한 사전학습 모델을 항체 복합체로 미세조정하여 효과적인 설계 생성이 가능하게 했다. 설계된 항체들은 학습 데이터셋의 서열과 크게 다르면서도 표적 에피토프와 다양한 상호작용을 형성한다.

2. **원자 수준 정확도의 구조 검증**: 4개 질병 관련 에피토프에 대한 VHH 결합체를 인플루엔자 혈구응집소(hemagglutinin)와 클로스트리디움 디피실 톡신 B(TcdB)에서 표현. 크라이오-EM 구조 결정으로 (i) 설계된 VHH의 올바른 면역글로불린(Ig) 폴드 확인, (ii) 의도된 결합 자세 확인, (iii) 인플루엔자-표적 VHH의 경우 CDR 루프 배치의 원자 정확성 확인. 특히 TcdB 결합 scFv 중 하나는 6개 CDR 루프 모두의 원자 정확한 배치가 검증되었다.

3. **친화도 성숙을 통한 성능 향상**: 초기 계산 설계는 겸손한 친화도를 보였지만 OrthoRep 기반 친화도 성숙을 통해 단일 숫자 나노몰 범위의 결합체로 개선되었으며, 의도된 에피토프 선택성은 유지되었다.

4. **scFv 조합 설계의 증명**: 설계된 중쇄(heavy chain) CDR과 경쇄(light chain) CDR을 결합하여 TcdB와 Phox2b peptide-MHC 복합체에 대한 scFv 설계를 처음으로 달성. 두 개의 TcdB scFv에서 올바른 Ig 폴드와 결합 자세를 크라이오-EM으로 확인했다.

## How

![Figure 1: Overview of RFdiffusion for antibody design](figures/fig1.webp)
*Figure 1: RFdiffusion 항체 설계 개요. (A) 미세조정 과정에서 항체 복합체 구조를 노이징하여 학습, (B) 추론 시 프레임워크 서열과 구조를 제공, (C) 전역 프레임 불변성을 통해 강체 위치 샘플링 가능, (D) 표적 에피토프 지정을 위한 핫스팟(hotspot) 특징 적응*

### RFdiffusion 미세조정 방법

- **네트워크 구조 유지**: AlphaFold2/RF2의 frame representation(각 잔기의 Cα 좌표 및 N-Cα-C 강체 방향)을 사용하는 확산 모델 구조 유지
  
- **노이징 및 학습**: 3D 가우시안 노이즈로 좌표 부패, SO(3) 브라운 운동으로 방향 부패. 각 타임스텝에서 예측 구조(pX0)와 실제 구조(X0) 간의 평균 제곱 오차(MSE) 손실 최소화

- **항체 특화 훈련**: 항체 복합체 구조에 우선적으로 미세조정하되, 항체 구조만 부패시키고 표적 구조는 보존. 프레임워크 구조를 2D 거리 및 이면각 행렬로 template track에 제공하여 절대적 3D 위치는 설계 대상으로 남김

- **CDR 루프 중심 설계**: 핫스팟 특징을 적응하여 CDR 루프가 상호작용할 표적 잔기 지정. 이를 통해 강체 위치와 CDR 배치 동시 설계

- **서열 설계**: RFdiffusion 구조 생성 후 ProteinMPNN을 사용하여 CDR 루프 서열 설계

### RoseTTAFold2 미세조정 방법

![Figure 2: Biochemical characterization of designed VHHs](figures/fig2.webp)
*Figure 2: 설계된 VHH의 생화학적 특성화. 다양한 생물물리학적 방법으로 VHH 결합체의 특이성과 친화도 검증*

- **항체-항원 구조 예측 특화**: RF2 네트워크를 항체 구조에 미세조정하되, 학습 시 표적 구조와 에피토프 위치 정보 제공. 이를 통해 CDR 예측 정확도 및 항체-표적 결합 방향 예측 개선

- **자체 일관성(self-consistency) 필터링**: RFdiffusion이 생성한 설계 구조를 미세조정 RF2로 재예측하여 설계 구조와의 유사도 평가. 높은 신뢰도로 의도한 방식으로 결합 예측되는 VHH를 선정

- **교차 반응성 분석**: 비관련 단백질에 대한 예측 결합을 평가하여 의도하지 않은 결합 최소화

- **인터페이스 품질 평가**: Rosetta ddG로 계산된 인터페이스 품질 측정

### 스크리닝 및 친화도 성숙

- **Yeast display 스크리닝**: 계산 설계된 VHH/scFv를 yeast display 라이브러리로 발현하여 표적 에피토프에 대한 결합체 선별

- **OrthoRep 기반 친화도 성숙**: 무작위 뮤탈 로드 재조합 플라스미드(pOrtho)를 사용하여 VHH CDR 서열의 진화적 최적화. 높은 돌연변이율(mutation rate)로 신속한 친화도 개선

### 구조 검증

![Figure 3: Cryo-EM structural characterization of two de novo designed VHHs](figures/fig3.webp)
*Figure 3: 두 de novo 설계 VHH의 크라이오-EM 구조 특성화. 원자 수준의 설계 정확도 확인*

- **크라이오-EM 데이터 수집 및 처리**: 설계된 VHH 또는 scFv와 항원의 복합체에 대한 고해상도 구조 결정

- **구조 비교**: 설계 모델 구조와 실험적으로 결정된 구조의 RMSD 계산 및 비교

- **CDR 루프 정확도**: 개별 CDR 루프(H1, H2, H3 및 scFv의 경우 L1, L2, L3)의 배치 정확성 검증

## Originality

- **첫 원자 정확한 de novo 항체 설계 달성**: 단순한 서열 예측이 아닌 3D 구조 및 에피토프 특이성을 포함한 완전한 항체 설계는 본 연구가 최초이다.

- **항체 특화 미세조정 전략**: 한정된 항체 PDB 데이터(~8,100개)에도 불구하고 대규모 사전학습 모델의 미세조정을 통해 효과적인 설계를 가능하게 한 접근법의 독창성이 높다.

- **강체 위치 설계 포함**: 프레임워크를 고정하면서도 강체 위치와 CDR 루프를 동시에 설계하는 방식은 기존 이식 기반 방법과 근본적으로 다르다.

- **VHH와 scFv 모두 달성**: 나노바디(VHH)뿐 아니라 완전한 단일 쇄 가변 단편(scFv) 설계까지 확장한 점이 중요하다.

- **다중 검증 방법**: 생화학적 특성화, 자체 일관성 필터, RF2 재예측, 크라이오-EM 구조화학 등 다양한 독립적 검증 방법으로 설계 신뢰성을 입증했다.

## Limitation & Further Study

- **초기 친화도의 제한**: 계산 설계된 항체의 초기 친화도가 겸손하여 OrthoRep 기반 친화도 성숙이 필수적이다. 초기 설계 단계에서 더 높은 친화도를 달성하는 방법 개발이 필요하다.

- **제한된 에피토프 검증**: 현재 4개 질병 관련 에피토프에서만 검증되었으므로, 더 광범위한 에피토프와 표적 단백질에서의 일반화 가능성을 평가해야 한다.

- **계산 비용**: 미세조정 모델의 훈련 및 추론에 필요한 계산 자원에 대한 상세한 정보가 제한적이다.

- **프레임워크 유연성**: 현재 방법은

## Related Papers

- 🔄 다른 접근: [[papers/256_De_novo_design_of_protein_structure_and_function_with_RFdiff/review]] — 맞춤형 단백질 설계를 위한 자율적 종단간 접근법이 RFdiffusion 기반 항체 설계와 다른 방법론을 제시한다.
- 🔗 후속 연구: [[papers/171_Boltz-1_Democratizing_Biomolecular_Interaction_Modeling/review]] — 생체분자 상호작용 모델링의 민주화가 원자 수준 정확한 항체 설계의 발전된 형태를 보여준다.
- 🔗 후속 연구: [[papers/805_The_Virtual_Lab_of_AI_agents_designs_new_SARS-CoV-2_nanobodi/review]] — RFdiffusion을 사용한 원자적으로 정확한 항체 설계가 Virtual Lab의 나노바디 설계 방법론을 더 정밀한 구조적 정확도로 확장한 발전된 접근이다.
