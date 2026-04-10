---
title: "167_Biomedlm_A_27_b_parameter_language_model_trained_on_biomedic"
authors:
  - "Elliot Bolton"
  - "Abhinav Venigalla"
  - "Michihiro Yasunaga"
  - "David Hall"
  - "Betty Xiong"
date: "2024"
doi: "arXiv:2403.18421"
arxiv: ""
score: 4.0
essence: "PubMed 논문 초록과 전체 문서로 훈련된 27억 매개변수 바이오메디컬 언어모델을 제시하며, 대규모 모델과 경쟁할 수 있는 강력한 성능을 달성하면서도 온디바이스 추론, 프라이버시 보호, 투명성과 경제성을 제공한다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/Multimodal_Scientific_Reasoning"
  - "topic/ai4s"
---

# BioMedLM: A 2.7B Parameter Language Model Trained on Biomedical Text

> **저자**: Elliot Bolton, Abhinav Venigalla, Michihiro Yasunaga, David Hall, Betty Xiong, Tony Lee, Roxana Daneshjou, Jonathan Frankle, Percy Liang, Michael Carbin, Christopher D. Manning | **날짜**: 2024 | **DOI**: [arXiv:2403.18421](https://arxiv.org/abs/2403.18421)

---

## Essence

PubMed 논문 초록과 전체 문서로 훈련된 27억 매개변수 바이오메디컬 언어모델을 제시하며, 대규모 모델과 경쟁할 수 있는 강력한 성능을 달성하면서도 온디바이스 추론, 프라이버시 보호, 투명성과 경제성을 제공한다.

## Motivation

- **Known**: GPT-4, Med-PaLM 2 같은 초대규모 언어모델들이 바이오메디컬 NLP 작업에서 우수한 성능을 달성하고 있음

- **Gap**: 이러한 대규모 모델들은 (1) 막대한 계산비용, (2) 원격 API 접근으로 인한 데이터 유출 위험, (3) HIPAA 준수의 어려움, (4) 폐쇄적 학습 데이터, (5) 미세조정 불가능 등의 심각한 문제를 가짐

- **Why**: 바이오메디컬 분야의 조직들, 특히 리소스가 제한적이고 프라이버시 요구사항이 엄격한 의료기관들이 접근 가능한 영역-특화(domain-specific) 소형 모델의 필요성 증대

- **Approach**: PubMed 데이터로만 훈련된 27억 매개변수 GPT-스타일 자동회귀(autoregressive) 모델 개발. 바이오메디컬 전용 토크나이저 사용, 투명한 학습 데이터 공개, 완전 오픈소스 공개

## Achievement

1. **다중선택 질의응답 성능**: MedMCQA (dev) 57.4%, MMLU Medical Genetics 70.0% 달성으로 훨씬 큰 모델들과 경쟁 가능한 수준 입증

2. **영역-특화 효과**: 동일 크기의 범용 모델(GPT-Neo 2.7B)에 비해 BioASQ, PubMedQA, MedQA 세 가지 작업에서 일관되게 높은 정확도 달성

3. **생성형 질의응답**: "족저근막염의 최적 치료법은?" 같은 환자 질문에 유용한 다문장 답변 생성 능력 입증

4. **실용성**: 단일 A100 GPU에서 미세조정 가능, 노트북에서 추론 실행 가능한 경량성 달성

## How

- **아키텍처**: GPT-2 방식의 디코더-전용 Transformer. 숨겨진 크기 2560, 20개 헤드, 32개 레이어, 어휘 크기 28,896, 시퀀스 길이 1024

- **바이오메디컬 전용 토크나이저**: Byte-Pair Encoding (BPE) 기반으로 PubMed 초록에서 훈련. 어휘 크기 28,896으로 설정하여 "chromatography" 같은 바이오메디컬 용어가 단일 토큰으로 표현되도록 최적화 (GPT-2에서는 "chrom/atogra/phy"로 분리됨)

- **학습 데이터**: PubMed 초록과 전체 논문으로만 구성된 독점적(exclusive) 훈련 데이터. 이는 범용 모델(The Pile 등)과의 명확한 대조 제공

- **학습 설정**: 상세한 손실(loss) 추적을 통한 안정적 수렴 모니터링 (100k 배치 이후의 학습 및 검증 손실 그래프 제시)

## Originality

- **영역-특화 소형 모델의 효과성 입증**: 기존 PubMedBERT, BioBERT 등 BERT 기반 모델들보다 더 현대적인 GPT-스타일 아키텍처로 바이오메디컬 특화의 가치를 재입증

- **투명성-성능 균형**: 학습 데이터, 아키텍처, 훈련 과정을 완전 공개하면서도 경쟁력 있는 성능 달성이라는 새로운 트렌드 제시

- **프라이버시-성능 트레이드오프 해결**: 온디바이스 추론으로 HIPAA 준수와 데이터 보안을 보장하면서 충분한 성능 제공

- **바이오메디컬 토크나이저의 정량적 영향 분석**: 도메인-특화 토크나이저가 구체적으로 어떤 용어들을 더 효율적으로 표현하는지 명시

## Limitation & Further Study

- **규모의 한계**: 27억 매개변수 제약으로 인한 복잡한 추론 작업에서의 성능 한계 가능성

- **학습 데이터 편향**: PubMed만을 학습 데이터로 사용하여 임상 노트, 방사선 보고서 등 다양한 바이오메디컬 텍스트 타입에 대한 일반화 능력 제한 가능

- **비교 분석 부족**: 동시 개발 모델인 BioGPT와의 상세한 성능 비교 부재

- **후속 연구 방향**: (1) 임상 텍스트로의 확장 학습, (2) 더 큰 바이오메디컬 모델 개발, (3) 하위 작업(downstream task) 별 최적화 연구

## Evaluation

- **Novelty**: 3.5/5
  - 바이오메디컬 영역-특화 모델 자체는 신규가 아니나, GPT-스타일 아키텍처 + 소형 모델 + 완전 투명성 조합은 새로운 패러다임 제시

- **Technical Soundness**: 4/5
  - 아키텍처 설계, 토크나이저 최적화, 훈련 절차가 체계적이고 견고함. 다만 상세한 하이퍼파라미터 튜닝 과정 설명 부족

- **Significance**: 4/5
  - 리소스 제약이 있는 의료기관에 즉시 적용 가능한 실용적 가치 높음. 오픈소스 공개로 커뮤니티 기여도 상당. 다만 성능 개선폭은 점진적 수준

- **Clarity**: 4.5/5
  - 동기부여와 문제 정의가 명확하고 설득력 있음. 기술 상세가 충분하나 일부 학습 통계 및 오류 분석 추가 필요

- **Overall**: 4/5

**총평**: BioMedLM은 대규모 언어모델의 접근성, 프라이버시, 투명성 문제를 정면으로 해결하는 실용적이고 윤리적인 모델로서, 특히 의료기관 등 제약이 많은 도메인에서 즉시 배포 가능한 솔루션을 제공한다. 영역-특화 훈련의 가치를 재증명하며 오픈소스 생태계에 의미 있는 기여를 한다.

## Related Papers

- 🔗 후속 연구: [[papers/530_Medbiolm_Optimizing_medical_and_biological_qa_with_fine-tune/review]] — 생명의학 QA 최적화에서 2.7B 매개변수 생명의학 언어모델로의 확장
- 🏛 기반 연구: [[papers/707_SciBERT_A_Pretrained_Language_Model_for_Scientific_Text/review]] — 과학 텍스트용 사전훈련 언어모델 SciBERT가 생명의학 모델의 기반 제공
- 🔄 다른 접근: [[papers/720_Scientific_Large_Language_Models_A_Survey_on_Biological__Che/review]] — 생물학과 화학 분야 과학 LLM 조사와 생명의학 특화 모델의 다른 접근법
- 🧪 응용 사례: [[papers/271_Developing_ChemDFM_as_a_large_language_foundation_model_for/review]] — 화학 분야 대형 언어 파운데이션 모델 개발에 생명의학 모델 적용
- 🧪 응용 사례: [[papers/720_Scientific_Large_Language_Models_A_Survey_on_Biological__Che/review]] — 생의학 특화 언어모델의 성공 사례를 생물학/화학 분야 LLM 개발에 참고할 수 있다
