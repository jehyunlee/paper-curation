# Fast Parallel Algorithms for Short-Range Molecular Dynamics

> **저자**: S. Plimpton | **날짜**: 1993 | **Journal**: Journal of Computational Physics | **DOI**: 10.1006/JCPH.1995.1039

---

## Essence

단거리 분자동역학(MD) 시뮬레이션을 위한 세 가지 병렬화 전략—원자 분해(atom decomposition), 힘 분해(force decomposition), 공간 분해(spatial decomposition)—을 체계적으로 비교 분석한 논문이다. 공간 분해 방식이 통신 비용 측면에서 $O(N^{1/3})$으로 가장 우수하여 대규모 시뮬레이션에 최적임을 보였으며, 이 연구는 현재 가장 널리 사용되는 MD 소프트웨어인 LAMMPS의 직접적 기원이 되었다.

## Motivation

- **알려진 것**: MD 시뮬레이션은 원자 간 상호작용을 시간적으로 적분하여 물성을 계산하지만, 단일 프로세서로는 수천~수만 원자 이상 처리가 불가능했음
- **Gap**: 병렬 컴퓨터가 등장했으나, MD를 효율적으로 병렬화하는 체계적 방법이 확립되지 않았고, 어떤 분해 전략이 어떤 조건에서 최적인지 불명확했음
- **왜 중요한가**: 수백만~수억 원자 규모의 시뮬레이션이 가능해져야 실제 재료·생체 시스템 연구가 가능함
- **접근법**: 세 가지 병렬화 전략을 수학적으로 분석하고, 실제 하이퍼큐브(hypercube) 병렬 컴퓨터에서 벤치마크 비교

## Achievement

1. **원자 분해**: 통신 비용 $O(N)$ — 원자 수에 비례하여 확장성 불량
2. **힘 분해**: 통신 비용 $O(N/\sqrt{P})$ — 개선되었으나 여전히 제한적
3. **공간 분해**: 통신 비용 $O(N^{1/3} / P^{2/3})$ — 최적; 원자 수 증가에도 통신 부하 최소
4. 512 프로세서에서 거의 선형적 speedup(near-linear scaling) 달성, 수백만 원자 시뮬레이션 실현
5. 세 방법론의 적용 조건과 한계를 체계적으로 분류하여 MD 병렬화의 교과서적 기준 제시

## How

- **하드웨어**: Intel iPSC/860 하이퍼큐브 병렬 컴퓨터 (512 프로세서)
- **알고리즘**: 단거리 Lennard-Jones 포텐셜, neighbor list 방법
- **분석**: 통신 부하(communication overhead), 계산 부하 균형(load balancing), 메모리 사용량 이론적 분석 후 실험 검증
- **벤치마크**: 균일 원자 분포 가정 시와 불균일 시스템에서의 성능 비교
- **병렬 통신 패턴**: 링(ring), 트리, 하이퍼큐브 토폴로지 활용

## Originality

- 세 병렬화 전략을 동일한 수학적 프레임워크로 비교 분석한 최초의 체계적 연구
- 공간 분해의 이론적 우월성을 증명하고 구현한 것이 이후 모든 대규모 MD 코드의 설계 원칙이 됨
- LAMMPS(Large-scale Atomic/Massively Parallel Simulator)의 직접적 이론적·구현적 기반

## Limitation & Further Study

### 저자들이 언급한 한계

- 균일한 원자 밀도 분포 가정 — 불균일 시스템(기포, 계면 등)에서는 load imbalance 발생 가능
- 장거리 정전기 상호작용(Ewald summation 등) 처리 방법 미포함

### 자체판단 아쉬운 점

- Reactive force field(ReaxFF 등)나 coarse-grained model에서의 병렬화 전략은 다루지 않음
- GPU 병렬화 시대를 예측하지 못했으나, 이는 당시 시대적 한계

### 후속 연구

- LAMMPS 개발 및 지속적 확장 (현재 수억 원자 시뮬레이션 가능)
- GPU 가속 MD (NAMD, GROMACS GPU 버전 등)
- 신경망 포텐셜(NNP)과 결합한 대규모 ML-MD 시뮬레이션

## Evaluation

- Novelty: 4/5
- Technical Soundness: 5/5
- Significance: 5/5
- Clarity: 5/5
- Overall: 5/5

**총평**: 분자동역학 시뮬레이션의 대규모 병렬화를 체계적으로 확립한 이정표 논문으로, LAMMPS라는 사실상의 표준 MD 소프트웨어의 직접적 기반이 되어 계산 재료과학·생물물리학 연구를 수십 년간 견인했다.
