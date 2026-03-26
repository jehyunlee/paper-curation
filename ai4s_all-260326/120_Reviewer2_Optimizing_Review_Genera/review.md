# Reviewer2: Optimizing Review Generation Through Prompt Generation

- **저자**: Zhaolin Gao, Kiante Brantley, Thorsten Joachims
- **소속**: Cornell University, Department of Computer Science
- **발표**: arXiv:2402.10886 (2024)
- **DOI**: [10.48550/arXiv.2402.10886](https://doi.org/10.48550/arXiv.2402.10886)

---

## Essence (핵심 요약)

LLM 기반 학술 논문 리뷰 자동 생성에서 **구체성(specificity)과 커버리지(coverage) 부족** 문제를 해결하기 위해, aspect prompt 생성과 리뷰 생성을 분리한 2단계 프레임워크 REVIEWER2를 제안한다. 첫 번째 LLM(Mp)이 논문을 분석하여 리뷰가 다룰 관점(aspect prompt)을 생성하고, 두 번째 LLM(Mr)이 해당 관점에 기반한 리뷰를 생성한다. 이를 위해 기존 리뷰 데이터셋에 aspect prompt를 자동 어노테이션하는 PGE(Prompt Generation with Evaluation) 파이프라인을 개발하고, 27k 논문 / 99k 리뷰의 대규모 데이터셋을 구축하여 공개한다.

---

## Motivation (연구 동기)

기존 LLM 리뷰 생성 방법은 두 가지 핵심 문제를 가진다. 첫째, fine-tuning이 진행될수록 생성 리뷰가 점점 **일반적(generic)** 이 되는 regression-to-the-mean 현상이 발생한다 (Table 1에서 학습 step 증가에 따라 "The paper is well-written and straightforward" 같은 범용 문장으로 수렴). 둘째, 인간 리뷰어들은 각자 다른 관점에 집중하지만, 단일 단계 생성은 이러한 **다양성을 포착하지 못한다**. 더 근본적으로, "논문을 리뷰하라"는 지시는 어떤 측면에 집중할지 명시하지 않아 모델에게 과도한 불확실성을 부여하는 under-specified 문제이다. 이는 연구 자원이 부족한 그룹의 연구자들에게 양질의 피드백 접근성을 제한하는 불평등 문제와도 연결된다.

---

## Achievement (주요 성과)

1. **품질**: 6개 학회 데이터셋(ICLR, NeurIPS, ACL, ARR, COLING, CONLL)에서 BLEU, ROUGE, BertScore 모두 REVIEWER2가 모든 베이스라인 대비 최고 성능 (예: ICLR BLEU 16.94 vs SINGLES 15.08)
2. **GPT-4 판정**: faithfulness(0.64), coverage(0.74), coherence(0.78), specificity(0.79)에서 일관되게 가장 높은 winrate 달성
3. **구체성 향상**: aspect prompt를 사용하는 방법(REVIEWER2)은 학습이 진행될수록 specificity가 증가하는 반면, prompt 없는 방법(SINGLES)은 감소 -- 학습과 구체성의 관계가 역전됨
4. **커버리지**: REVIEWER2의 coverability(COV) 지표가 REVIEWER2-E 대비 3~4배 낮아(ICLR: 4.22 vs 13.55), 다양한 aspect prompt로 인간 리뷰어 수준의 관점 다양성에 근접
5. **대규모 데이터셋**: 27,805편 논문, 99,727개 리뷰, 97,960개 aspect prompt를 포함하는 최초의 aspect prompt 어노테이션 리뷰 데이터셋 공개
6. **Cross-domain 적응성**: ICLR/NeurIPS로 학습 후 ACL, ARR, COLING, CONLL에서도 비교 가능한 BertScore 달성

---

## How (방법론)

### REVIEWER2 프레임워크
- **1단계 (Aspect Prompt 생성)**: Mp: p -> {x1, ..., xk}. 논문 p를 입력받아 리뷰가 다룰 관점 질문들을 생성
- **2단계 (리뷰 생성)**: Mr: (p, x) -> y. 논문 p와 aspect prompt x를 입력받아 해당 관점에 집중한 리뷰 y를 생성
- **기반 모델**: Llama-2-7B-Chat + LongLoRA (LoRA+ 및 S2-Attn)로 32k 컨텍스트 길이 지원, 전체 논문 텍스트 입력 가능

### PGE (Prompt Generation with Evaluation) 파이프라인
- **생성 단계**: Llama-2-70B-Chat에 ICL(in-context learning)을 적용하여 리뷰로부터 aspect prompt 역생성. 초기 100개 예시는 인간이 수동 정제
- **평가 단계**: 생성된 prompt를 5점 척도로 자동 평가. 5점 미달 시 재생성 (최대 5회). 93.6%가 3회 이내에 통과
- **핵심 인사이트**: prompt 공간에서 리뷰어 간 변동성을 명시적으로 모델링함으로써, 리뷰 공간에서의 노이즈를 감소시키고 구체적 생성을 가능하게 함 (Figure 2의 기하학적 직관)

### 새로운 평가 메트릭
- **SPE (Specificity)**: 생성 리뷰가 해당 논문의 참조 리뷰와의 유사도에서, 다른 논문의 참조 리뷰와의 유사도를 뺀 값. 높을수록 논문 특화 리뷰
- **COV (Coverability)**: 서로 다른 aspect prompt로 생성한 리뷰들 간 pairwise 유사도와 인간 리뷰들 간 유사도의 차이. 0에 가까울수록 인간 수준의 다양성

---

## Originality (독창성)

1. **리뷰 생성의 under-specification 문제 진단**: 개방형 리뷰 생성이 instruction following과 근본적으로 다르다는 통찰. "무엇을 리뷰할 것인가"의 불확실성이 regression-to-the-mean의 원인임을 이론적/실험적으로 규명
2. **2단계 분리 아키텍처**: aspect prompt 생성과 리뷰 생성을 분리하여, 리뷰어 간 관점 다양성을 prompt 공간에서 명시적으로 모델링하는 접근. 이는 조건부 생성에서 latent variable을 도입하는 것과 유사한 효과
3. **PGE 파이프라인**: 리뷰에서 aspect prompt를 역생성하고 자동 평가하는 자기 정렬(self-alignment) 방식의 데이터 증강. 인간 감독을 최소화하면서 97,960개의 고품질 prompt 생성
4. **SPE/COV 메트릭**: 리뷰 구체성과 관점 커버리지를 정량화하는 새로운 평가 메트릭 제안

---

## Limitation & Further Study (한계 및 향후 연구)

### 한계
1. **PGE와 REVIEWER2의 분리**: prompt 생성이 리뷰 생성과 독립적으로 수행되어, 생성된 prompt가 리뷰 품질 향상에 최적화되지 않음. 두 프로세스의 통합이 필요
2. **입력 불일치**: PGE는 리뷰만 입력으로 사용하지만 REVIEWER2는 논문+prompt를 사용. Llama-2-70B-Chat의 4096 토큰 제한으로 인한 제약
3. **도메인 지식 한계**: 사전학습 코퍼스에 의존하여 전문적 도메인 지식이 부족할 수 있으며, 도메인 적응 없이 심층적 기술 리뷰 생성이 어려움
4. **평가의 한계**: 자동 메트릭(BLEU, ROUGE, BertScore)과 GPT-4 판정에 의존하며, 실제 저자나 인간 리뷰어에 의한 유용성 평가가 부재
5. **Llama-2-7B 기반**: 비교적 소규모 모델 사용으로 최신 대형 모델 대비 리뷰 품질의 절대적 수준이 제한적일 수 있음

### 향후 연구 방향
- PGE와 REVIEWER2의 end-to-end 통합 학습
- 도메인 적응을 위한 2단계 사전학습 또는 RAG 기법 적용
- 실제 저자를 대상으로 한 유용성 사용자 연구

---

## Evaluation (총평)

REVIEWER2는 LLM 리뷰 생성의 핵심 문제인 "generic review 생성"을 **정확히 진단하고 원리적으로 해결**한 논문이다. 리뷰 생성이 under-specified task라는 통찰과, aspect prompt를 통해 리뷰어 간 관점 다양성을 명시적으로 모델링한다는 아이디어는 기술적으로 건전하며 직관적이다. Figure 2의 기하학적 직관과 Figure 6의 t-SNE 시각화가 이를 설득력 있게 뒷받침한다.

실험 설계는 체계적이며, 6개 학회에 걸친 in-domain/cross-domain 평가, SPE/COV라는 새로운 메트릭, 다양한 ablation을 통해 각 구성요소의 기여를 명확히 분리하였다. 27k/99k 규모의 aspect prompt 어노테이션 데이터셋의 공개도 커뮤니티에 대한 중요한 기여이다.

다만, 실제 리뷰 품질의 절대적 수준(저자에게 실질적으로 유용한지)에 대한 검증이 부족하고, 최신 대형 모델로의 확장 실험이 없는 점은 아쉽다. 또한 PGE의 자기 평가가 실제로 고품질 prompt를 보장하는지에 대한 인간 검증이 100개 초기 예시 외에는 체계적으로 이루어지지 않았다. 그럼에도, 리뷰 생성의 구조적 문제를 원리적으로 해결하는 접근은 후속 연구의 중요한 토대가 될 것이다.
