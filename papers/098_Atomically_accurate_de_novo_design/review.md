# Atomically accurate de novo design of antibodies with RFdiffusion

> **저자**: Nathaniel R. Bennett, Joseph L. Watson, Robert J. Ragotte, Andrew J. Borst, DéJenaé L. See, Connor Weidle, Riti Biswas, Yutong Yu, Ellen L. Shrock, Russell Ault, Philip J. Y. Leung, Buwei Huang, Inna Goreshnik, John Tam, Kenneth D. Carr, Benedikt Singer, Cameron Criswell, Basile I. M. Wicky, Dionne Vafeados, Mariana Garcia Sanchez, Ho Min Kim, Susana Vázquez Torres, Sidney Chan, Shirley M. Sun, Timothy Spear, Yi Sun, Keelan O'Reilly, John M. Maris, Nikolaos G. Sgourakis, Roman A. Melnyk, Chang C. Liu, David Baker | **날짜**: 2025 | **Journal**: bioRxiv | **DOI**: 10.1101/2024.03.14.585103

---

## Essence

RFdiffusion을 항체 설계에 특화하여 fine-tuning함으로써, 사용자가 지정한 epitope에 원자 수준 정확도로 결합하는 de novo 항체(VHH 및 scFv)를 완전히 computational하게 설계한 최초의 연구이다. Cryo-EM 구조 분석으로 설계된 CDR 루프 구조와 결합 모드가 계산 모델과 원자 수준에서 일치함을 실험적으로 검증했다.

## Motivation

- **알려진 것**: 항체는 현대 의학의 핵심 치료제(글로벌 160개 이상 허가, 시장가치 $445B 전망)이나, 발견 과정은 동물 면역화나 무작위 라이브러리 스크리닝에 의존
- **Gap**: 특정 epitope에 결합하는 항체를 순수하게 in silico에서 설계하는 방법이 존재하지 않았음. 기존 deep learning 기반 항체 서열 설계 방법들은 구조적으로 정확한 de novo 항체 설계에 실패
- **왜 중요한가**: Epitope-specific 항체 설계가 가능해지면, 수용체-리간드 상호작용 차단, 비면역우세 epitope 타겟팅 등 치료적으로 중요한 응용이 가능
- **접근법**: RFdiffusion을 항체 복합체 구조에 fine-tuning하여 CDR 루프와 rigid-body docking을 동시에 설계하고, yeast display screening으로 검증

## Achievement

1. **다중 타겟 VHH 설계 성공**: Influenza HA, C. difficile TcdB, SARS-CoV-2 RBD, RSV 등 질병 관련 타겟에 대해 epitope-specific VHH binder 생성 (TcdB: KD = 260 nM, HA: KD = 78 nM)
2. **원자 수준 구조 정확도**: Cryo-EM으로 검증한 anti-HA VHH(VHH_flu_01)의 backbone RMSD = 1.45 A, CDR3 RMSD = 0.8 A
3. **Affinity maturation**: OrthoRep을 이용한 in vivo 지속적 돌연변이로 초기 설계 대비 ~100배 친화도 향상, single-digit nanomolar 수준 달성
4. **scFv 설계 확장**: 6개 CDR 전체를 de novo로 설계한 scFv에서 TcdB 타겟 최고 KD = 72 nM 달성. Cryo-EM(3.6 A)으로 6개 CDR 모두 near-atomic precision 확인 (각 CDR backbone RMSD: 0.2~1.1 A)
5. **Phox2b-MHC 타겟팅**: 신경모세포종 관련 peptide-MHC 복합체에 대한 scFv binder 설계 (KD = 400 nM), 펩타이드 특이적 결합 확인

## How

- **RFdiffusion Fine-tuning**: PDB의 항체 복합체 구조로 fine-tuning. 항체 framework 구조/서열은 template track을 통해 2D pairwise distance/dihedral matrix로 제공 (global-frame-invariant). CDR 루프와 rigid-body dock만 diffusion으로 생성
- **Epitope 지정**: One-hot encoded "hotspot" feature로 타겟 단백질의 결합 epitope 잔기를 지정
- **서열 설계**: ProteinMPNN으로 CDR 루프 서열 설계 (framework는 고정)
- **구조 검증 필터**: RoseTTAFold2를 항체 구조에 fine-tuning하여 self-consistency 필터로 활용. 설계 모델과 RF2 예측 구조의 일치도로 후보 선별
- **실험 스크리닝**: Yeast surface display (타겟당 9,000개 설계) 또는 E. coli 발현 + SPR (타겟당 95개). 경쟁 결합 실험으로 epitope 특이성 확인
- **Combinatorial scFv 라이브러리**: 유사한 결합 모드를 가진 설계들의 heavy/light chain CDR을 structure-aware하게 조합하여 라이브러리 다양성 확보
- **Affinity maturation**: OrthoRep 시스템으로 yeast 내 연속적 hypermutation 수행

## Originality

- **최초의 epitope-specific de novo 항체 설계**: 기존 방법과 달리 기존 항체 구조에 의존하지 않고, 지정된 epitope에 대해 CDR 루프를 완전히 새로 생성하는 최초의 computational 프레임워크
- **CDR-focused diffusion training**: Framework를 global-frame-invariant template로 제공하면서 CDR만 noising/denoising하는 training regime으로, 항체 특유의 CDR-mediated 상호작용 설계를 가능하게 함
- **Structure-aware combinatorial assembly**: 동일한 binding mode의 설계들에서 heavy/light chain을 구조적으로 호환 가능한 조합으로 재구성하는 전략으로, 6개 CDR 동시 설계의 조합적 어려움을 극복
- **Cryo-EM 기반 원자 수준 검증**: De novo 설계 항체의 구조적 정확도를 cryo-EM으로 최초 검증하여, 설계-실험 간 원자 수준 일치를 입증

## Limitation & Further Study

### 저자들이 언급한 한계

- 실험적 성공률이 상당히 낮아 (iPTM > 0.6인 설계가 전체의 9%에 불과) 대규모 high-throughput 스크리닝이 필수적
- SARS-CoV-2 RBD VHH는 올바른 epitope에 결합했으나 binding mode가 설계와 달라 설계 실패로 분류
- 초기 설계의 친화도가 modest하여 OrthoRep을 통한 affinity maturation이 필수적
- Glycan 등 비단백질 원자를 설계 과정에서 고려하지 못함 (HA의 sub-stoichiometric binding 원인)

### 자체판단 아쉬운 점

- RoseTTAFold2 필터의 제한적 성능이 낮은 실험 성공률의 주요 원인이며, AlphaFold3 필터링은 후향적 분석에 그침 -- 실제 prospective 적용 결과가 없음
- VHH에서 scFv로의 확장 시 fixed pairing 라이브러리에서는 binder가 발견되지 않아, combinatorial assembly에 의존해야 하는 점은 설계 정확도의 근본적 한계를 시사
- Phox2b-MHC scFv의 경우 T cell 세포독성 실험에서 종양세포 사멸을 유도하지 못해, 실질적 치료 응용까지는 상당한 gap 존재
- 타겟당 수천~수만 개의 설계를 스크리닝해야 하므로, 순수한 in silico 설계라기보다 computational design + experimental screening의 hybrid 접근에 가까움

### 후속 연구

- AlphaFold3를 prospective 필터로 통합하여 실험 성공률 대폭 향상
- RFdiffusion All-Atom (RoseTTAFold-AA) 기반으로 glycan 포함 epitope 설계
- 인간 CDR 서열 분포에 가까운 서열 설계를 위한 ProteinMPNN 개선 (면역원성 저감)
- scFv에서 full antibody (IgG) 형식으로의 전환 및 developability 최적화
- Affinity maturation 없이 high-affinity binder를 직접 설계하는 one-shot 방법론 개발

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 5/5 |
| Technical Soundness | 4/5 |
| Significance | 5/5 |
| Clarity | 4/5 |
| Overall | 5/5 |

**총평**: 항체 설계의 패러다임을 근본적으로 전환시킬 잠재력을 가진 획기적 연구이다. RFdiffusion을 항체에 특화시켜 사용자 지정 epitope에 원자 수준 정확도로 결합하는 de novo 항체를 설계하고, cryo-EM으로 이를 검증한 최초의 사례로서 의의가 크다. 다만 낮은 실험 성공률과 affinity maturation 의존성은 향후 개선이 필요하며, AlphaFold3 기반 필터링과 all-atom 모델링의 통합이 이 분야의 다음 도약을 이끌 것으로 기대된다.
