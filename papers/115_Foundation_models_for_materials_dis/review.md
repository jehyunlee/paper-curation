# Foundation Models for Materials Discovery -- Current State and Future Directions

- **저자**: Edward O. Pyzer-Knapp, Matteo Manica, Peter Staar, Lucas Morin, Patrick Ruch, Teodoro Laino, John R. Smith, Alessandro Curioni
- **소속**: IBM Research Europe, Xyme (Oxford), IBM Research TJ Watson
- **출처**: npj Computational Materials, 11:61 (2025-03-06)
- **DOI**: [10.1038/s41524-025-01538-0](https://doi.org/10.1038/s41524-025-01538-0)

---

## Essence (본질)

Foundation model(LLM을 포함하는 대규모 사전학습 모델의 총칭)이 재료 발견(materials discovery) 분야에 어떻게 적용되고 있는지를 조망하는 perspective 논문이다. 데이터 추출, 물성 예측, 분자 생성, 합성 계획의 네 가지 핵심 과제에서의 현황을 리뷰하고, 향후 멀티모달 모델, 새로운 데이터 캡처 방식, 멀티피델리티(multi-fidelity) 접근법이 이 분야의 방향을 결정할 것이라 전망한다.

## Motivation (동기)

- AI의 역사는 데이터 표현(representation)의 진화 역사이며, hand-crafted features에서 deep learning을 거쳐 foundation model의 일반화 가능한 표현으로 발전해 왔다.
- 재료과학 데이터는 소규모이고 분산되어 있으며, 'activity cliff'(미세한 구조 차이가 물성에 큰 영향을 주는 현상)처럼 미묘한 의존성이 존재하여 데이터 품질이 특히 중요하다.
- Foundation model의 "한 번 학습, 다양한 task에 적용" 패러다임이 데이터 부족 문제를 완화할 수 있는 잠재력이 있다.
- 기존 리뷰들이 LLM 자체에 집중한 반면, 재료 발견이라는 응용 관점에서 foundation model 전반(encoder-only, decoder-only, encoder-decoder)을 포괄적으로 다룬 perspective가 필요하다.

## Achievement (성과)

- 재료 발견에서 foundation model이 활용되는 **4대 핵심 과제**를 체계적으로 정리하였다:
  1. **데이터 추출**: 특허/논문에서 NER, Vision Transformer, GNN을 활용한 분자 구조 및 물성 추출. Plot2Spectra, DePlot 등 외부 도구와의 통합 가능성 제시.
  2. **물성 예측**: BERT 기반 encoder-only 모델(ChemBERTa, MatSciBERT 등)이 주류이나 GPT 기반 모델도 증가 추세. MLIP(Machine Learned Interatomic Potentials)를 foundation model로 재해석(MACE, ANI, AIMNET 등).
  3. **분자 생성**: VAE, GAN, GNN, Transformer, Diffusion 모델 등 다양한 기법 활용. GuacaMol, Moses, TDC, GT4SD 등 오픈 벤치마크/툴킷의 등장이 접근성을 높임.
  4. **합성 예측**: Molecular Transformer(반응 예측을 기계번역으로 접근), prompt 기반 역합성, 150억 파라미터 규모 화학 foundation model(BatGPT-Chem) 등 발전.
- **미래 방향 3가지**를 구체적으로 제안: (1) 멀티모달 모델, (2) 실험실 자동 기록을 위한 새로운 데이터 캡처, (3) 멀티피델리티 모델.

## How (방법)

이 논문은 실험/모델 개발이 아닌 perspective(전망) 논문으로, 방법론 섹션 대신 현황 리뷰와 미래 전망을 제시한다.

- AI 표현학습의 역사적 발전(expert systems -> ML -> deep learning -> foundation models)을 타임라인으로 정리.
- Encoder/Decoder/Encoder-Decoder 아키텍처별로 재료 발견 과제와의 매핑을 테이블로 정리(Table 1).
- 물성 예측에 사용되는 아키텍처의 분포를 원형 차트로 분석(BERT 계열이 지배적, GPT 증가 추세).
- 155개 참고문헌을 통해 포괄적인 문헌 조사를 수행.

## Originality (독창성)

- **Foundation model을 재료 발견 전 과정에 매핑**: 데이터 추출 -> 물성 예측 -> 분자 생성 -> 합성 계획이라는 재료 발견 파이프라인의 각 단계에 foundation model을 체계적으로 대응시킨 점이 독특하다.
- **MLIP를 foundation model로 재해석**: MEGNET, MACE, ANI 등의 interatomic potential 모델을 foundation model의 관점에서 해석하여, 전통적 시뮬레이션과 foundation model 패러다임을 연결한 점이 새롭다.
- **멀티피델리티 모델의 중요성 강조**: 다양한 정확도/비용의 데이터를 통합 활용하는 multi-fidelity 접근을 재료 발견 특유의 데이터 희소성 해결책으로 제안한 점이 의미 있다.
- **실험 자동 기록 비전**: 멀티모달 foundation model을 활용한 실험실 절차의 실시간 자동 전사(transcription) 개념을 재료과학 맥락에서 제안하였다.

## Limitation & Further Study (한계 및 향후 연구)

- **Perspective 논문의 본질적 한계**: 새로운 실험 결과나 모델을 제시하지 않으며, 기존 문헌의 정리와 전망에 그친다.
- **2D 표현 의존**: 현재 물성 예측 모델의 대부분이 SMILES/SELFIES 같은 2D 표현에 기반하여, 3D conformational 정보가 누락되는 문제를 지적하지만 구체적 해결책은 제시하지 않는다.
- **데이터 품질/편향 문제**: activity cliff, 데이터 소스 편향(유기화학/약물 발견 편중), 재현성 문제를 지적하지만 아직 해결이 미진하다.
- **모델 전이가능성/적절성 평가**: model roughness 같은 평가 기법이 등장하고 있으나 아직 미해결 문제이다.
- **향후 과제**: 대규모 고품질 멀티모달 재료 데이터셋 구축, FAIR 원칙에 따른 실험 데이터 표준화, 멀티피델리티 foundation model 개발, 실험실 자동 문서화 시스템 실용화 등이 필요하다.

## Evaluation (총평)

IBM Research 팀이 작성한 이 perspective는 foundation model의 재료 발견 응용을 10페이지의 간결한 분량에 잘 정리한 유용한 개관이다. 특히 데이터 추출부터 합성까지의 전 파이프라인을 foundation model 관점에서 일관되게 조망한 점, MLIP를 foundation model 프레임워크에 포함시킨 점, 멀티피델리티 모델의 중요성을 강조한 점이 차별화된다. 다만 IBM의 자체 연구(Molecular Transformer, GT4SD, Text-chem T5 등)에 대한 인용이 비중 있게 다뤄져 있어 다소 자기 참조적인 면이 있고, 최신 LLM(GPT-4, Claude 등)의 in-context learning이나 에이전트(agent) 기반 접근에 대한 논의가 상대적으로 얕다. 재료과학에서 AI를 활용하려는 연구자에게 분야 전체의 지형을 파악하는 입문 자료로 적합하다.

## 평가
| 항목 | 점수 (1-5) |
|------|-----------|
| Novelty | 3 |
| Technical Soundness | 3 |
| Significance | 3 |
| Overall | 3.0 |

**총평**: IBM Research의 재료 발견을 위한 파운데이션 모델 관점 논문으로, 현황과 미래 방향을 개괄적으로 정리했지만 구체적 실험 근거나 독창적 방법론 없이 비전 제시에 그친다.
