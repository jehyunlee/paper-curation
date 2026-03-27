# A Perspective on Foundation Models in Chemistry

- **저자**: Junyoung Choi, Gunwook Nam, Jaesik Choi, Yousung Jung
- **출처**: JACS Au 5, 1499-1518 (2025)
- **DOI**: [10.1021/jacsau.4c01160](https://doi.org/10.1021/jacsau.4c01160)

---

## Essence (본질)
화학 및 재료 과학 분야에서 파운데이션 모델(foundation model)의 최근 발전을 체계적으로 정리한 관점(perspective) 논문이다. 물성 예측(property prediction), 기계학습 원자간 포텐셜(MLIP), 역설계(inverse design)의 세 가지 핵심 도메인에 걸쳐 "작은 파운데이션 모델(small FM)"과 "큰 파운데이션 모델(big FM)"로 분류하고, 사전학습 방법론(SSL, 멀티모달 학습, LLM 활용)과 함께 미래 방향을 논의한다.

## Motivation (동기)
화학/재료 분야의 ML은 레이블된 데이터 부족, 도메인 외(out-of-distribution) 화합물로의 외삽 한계, 기존 MLIP의 전이 가능성 제한 등 근본적 과제에 직면해 있다. NLP/CV에서 파운데이션 모델이 데이터 부족과 범용성 문제를 해결한 성공 사례에 영감을 받아, 화학 분야에서도 대규모 사전학습 모델을 통해 이러한 한계를 극복하고자 하는 연구가 급증하고 있다. 그러나 연구가 빠르게 확산되면서 현재 동향을 추적하고 유망한 접근법을 식별하기 어려워, 체계적 정리가 시의적절하다.

## Achievement (성과)
1. **체계적 분류 체계 제시**: 화학 FM을 small FM (단일 도메인: 물성 예측, MLIP, 역설계)과 big FM (다중 도메인: 물성+MLIP, 물성+역설계)으로 분류하는 명확한 프레임워크 제공
2. **포괄적 모델 서베이**: Table 1에 40개 이상의 주요 FM을 아키텍처, 사전학습 데이터, 방법론, 다운스트림 태스크별로 정리
3. **핵심 사전학습 전략 분석**:
   - GNN 기반: 대조학습(contrastive learning), 예측/생성 학습, 디노이징(denoising)
   - 언어 모델 기반: 마스크 언어 모델링, SMILES 기반 학습
   - 멀티모달: 구조-텍스트, SMILES-속성 등 다중 모달리티 통합
4. **Universal MLIP 동향 정리**: M3GNet, CHGNet, MACE-MP-0, GNoME, MatterSim 등 범용 MLIP의 발전과 파인튜닝 가능성 체계화
5. **미래 방향 제시**: 범위(scope), 성능(performance), 효율성(efficiency), 해석 가능성(interpretability) 4개 축의 발전 방향

## How (방법)
- **분류 기준**: 다운스트림 태스크 범위에 따라 small FM (단일 도메인 적응)과 big FM (다중 도메인 적응)으로 이분
- **방법론 정리**: 모델(GNN, 언어 모델)과 사전학습 방법(자기지도학습 — 대조/예측/생성 학습, 멀티모달 학습)을 먼저 개관한 후 도메인별 적용 사례 분석
- **도메인별 리뷰**:
  - 물성 예측: 대조학습(GraphCL, MolCLR, GraphMVP), 예측/생성 학습(GROVER, CrysGNN), 언어모델(MoLFormer, ChemBERTa-2)
  - MLIP: 범용 MLIP(M3GNet→CHGNet→MACE-MP-0→GNoME→MatterSim)의 진화, zero-shot/few-shot 성능
  - 역설계: 확산 모델(MatterGen), LLM 기반 생성(CrystalLLM, GP-MoLFormer)
  - 다중 도메인: 디노이징 기반(물성+MLIP), 멀티모달 학습(물성+역설계), LLM 활용(ChemDFM, nach0)

## Originality (독창성)
- Small FM vs Big FM의 이분 분류는 화학 FM의 현 위치와 궁극적 목표를 명확히 구분하는 유용한 프레임워크
- 물성 예측, MLIP, 역설계를 하나의 통합 관점에서 조망하면서 도메인 간 시너지(예: force field 학습이 물성 예측의 사전학습으로 작용)를 강조
- 데이터 스케일링, 모델 스케일링, GNN의 확장성 한계 등 실질적 과제를 구체적으로 짚어냄
- 해석 가능성(hallucination, model collapse)과 효율성(지식 증류, 양자화) 등 실용적 이슈까지 포괄

## Limitation & Further Study (한계 및 향후 연구)
- **리뷰 범위**: 주로 분자/결정 재료에 집중되어 표면, 계면, 비정질 재료 등은 상대적으로 소홀
- **실험적 검증 논의 부족**: FM이 생성한 물질의 실험적 합성/검증 사례에 대한 논의가 제한적
- **벤치마크 표준화**: 논문에서도 지적하듯, 화학 FM의 OOD 성능과 실용적 robustness를 평가할 표준 벤치마크가 아직 부족
- **GNN 스케일링**: GNN의 대규모화에 대한 연구가 초기 단계이며, oversmoothing과 차원의 저주 등 해결 과제가 남아 있음
- **멀티모달 결정 재료**: 분자 대비 결정 재료의 멀티모달 학습은 아직 미개척 영역
- **데이터 품질/일관성**: 이종 데이터베이스 통합 시 DFT 계산 설정 불일치, 노이즈 레이블 등의 문제가 스케일링 한계를 야기

## Evaluation (평가)
서울대 정유성 그룹이 JACS Au에 발표한 이 관점 논문은 화학 분야 파운데이션 모델의 현 상태를 가장 체계적으로 정리한 리뷰 중 하나이다. Small/Big FM 분류, Table 1의 포괄적 모델 서베이, 그리고 사전학습 전략별 장단점 분석은 이 분야에 입문하는 연구자에게 훌륭한 로드맵을 제공한다. 특히 force field 학습이 물성 예측의 효과적 사전학습이 될 수 있다는 통찰, GNN 스케일링의 현실적 한계, 데이터 품질 문제 등 실질적 과제를 솔직하게 다루는 점이 인상적이다. 다만 빠르게 발전하는 분야 특성상 2024년 하반기 이후의 주요 발전(예: 최신 universal MLIP 벤치마크, agentic AI 활용 등)은 포함되지 못한 한계가 있다. 한국 연구진의 화학 AI 분야 리뷰로서 국내외 연구 동향 파악에 유용하다.

## 평가
| 항목 | 점수 (1-5) |
|------|-----------|
| Novelty | 3 |
| Technical Soundness | 4 |
| Significance | 4 |
| Overall | 3.7 |

**총평**: 화학 분야 파운데이션 모델의 현황과 미래를 체계적으로 정리한 JACS Au 관점 논문으로, 분자·반응·재료 전 영역을 포괄하는 로드맵이 후속 연구자들에게 실질적 가이드를 제공한다.
