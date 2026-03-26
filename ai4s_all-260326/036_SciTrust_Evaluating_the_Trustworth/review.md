# SciTrust: Evaluating the Trustworthiness of Large Language Models for Science

**저자:** Emily Herron, Junqi Yin, Feiyi Wang
**출처:** SC24-W: Workshops of the International Conference for High Performance Computing, Networking, Storage and Analysis (2024)
**DOI:** 10.1109/SCW63240.2024.00017
**PDF:** [IEEE Xplore](https://ieeexplore.ieee.org/document/10820709)

---

## 한줄 요약 (Essence)
과학 분야에서 LLM의 신뢰성을 체계적으로 평가하기 위한 종합 프레임워크 SciTrust를 제안하고, 컴퓨터과학·화학·생물학·물리학 4개 분야의 오픈엔디드 벤치마크를 통해 5개 LLM의 truthfulness, accuracy, hallucination, sycophancy를 다면적으로 분석한 연구.

---

## 연구 동기 (Motivation)
- LLM이 과학 연구에 점점 더 활용되고 있으나, 과학적 맥락에서의 **신뢰성(trustworthiness)** 평가는 체계적으로 이루어지지 않고 있음
- 기존 벤치마크는 일반 목적 평가에 치우쳐 있으며, 과학 분야 특화 LLM(Galactica, SciGLM 등)과 범용 모델 간의 신뢰성 비교가 부족
- 특히 과학적 추론에서 발생하는 **hallucination(환각)** 과 **sycophancy(아첨성 응답)** 문제는 연구 결과의 정확성에 치명적 영향을 미칠 수 있음
- 고성능 컴퓨팅(HPC) 환경에서의 대규모 평가 확장성도 중요한 고려사항

---

## 주요 성과 (Achievement)
- **4개 과학 분야**(CS, Chemistry, Biology, Physics)에 대한 **새로운 오픈엔디드 벤치마크** 4종 구축
- 전통적 메트릭과 LLM 기반 평가를 결합한 **다면적 평가 접근법** 제안
- 5개 LLM(범용 1개 + 과학 특화 4개) 평가 결과:
  - **Llama3-70B-Instruct**가 전반적으로 가장 우수한 성능
  - 과학 특화 모델 중에서는 **Galactica-120B**와 **SciGLM-6B**가 상대적으로 강점
- HPC 시스템에서의 성능 및 확장성 검증 완료
- 프레임워크, 스크립트, 데이터셋 전체를 [GitHub](https://github.com/herronej/SciTrust)에 오픈소스로 공개

---

## 방법론 (How)
1. **벤치마크 설계:** CS, Chemistry, Biology, Physics 각 분야별로 오픈엔디드 질문을 설계하여, 단순 정답 맞추기가 아닌 서술형 응답을 요구
2. **평가 차원:** 4가지 핵심 축으로 평가
   - **Truthfulness:** 사실에 기반한 정확한 정보 제공 여부
   - **Accuracy:** 과학적 정확도
   - **Hallucination:** 존재하지 않는 정보의 생성 정도
   - **Sycophancy:** 사용자 의견에 맹목적으로 동조하는 경향
3. **평가 방식:** 전통적 자동 메트릭(BLEU, ROUGE 등)과 LLM-as-a-Judge 방식을 결합하여 다면적 평가 수행
4. **HPC 확장성:** 고성능 컴퓨팅 환경에서의 대규모 병렬 평가 파이프라인 구현 및 검증

---

## 독창성 (Originality)
- 과학 분야에 특화된 **신뢰성 평가 프레임워크**를 최초로 체계화한 점이 핵심 기여
- 단순 정확도가 아닌 hallucination과 sycophancy까지 포함하는 **다차원 평가 체계**는 과학 AI 신뢰성 연구의 기반을 마련
- 오픈엔디드 벤치마크를 통해 LLM의 자유로운 과학적 서술 능력을 평가한 것은 기존 MCQ 기반 벤치마크와 차별화
- HPC 확장성까지 고려한 실용적 프레임워크 설계

---

## 한계 (Limitation)
- **평가 대상 모델 수가 5개로 제한적**이며, GPT-4, Claude 등 최신 상용 모델이 포함되지 않아 일반화에 한계
- 오픈엔디드 벤치마크의 **평가 기준(ground truth)** 설정이 주관적일 수 있으며, LLM-as-a-Judge 방식 자체의 편향 가능성
- 워크숍 논문(7페이지)이라 각 분야별 벤치마크의 세부 설계와 질문 구성에 대한 **상세한 기술이 부족**
- 과학 분야가 4개로 한정되어 있으며, 의학·지구과학·공학 등 다른 분야로의 확장 필요
- 시간에 따른 모델 성능 변화나 **모델 업데이트에 따른 재현성** 문제는 다루지 않음

---

## 총평 (Evaluation)
SciTrust는 과학 분야 LLM의 신뢰성을 체계적으로 평가하려는 의미 있는 시도이다. Truthfulness, accuracy, hallucination, sycophancy의 4가지 축을 제시한 것은 향후 과학 AI 벤치마크 연구의 좋은 출발점이 된다. 다만 워크숍 논문의 분량 제약으로 인해 벤치마크 설계의 깊이와 실험의 규모가 다소 제한적이며, 최신 상용 모델과의 비교가 없는 점이 아쉽다. 오픈소스 공개는 후속 연구를 위한 긍정적 기여이나, 프레임워크의 실질적 활용과 커뮤니티 채택 여부는 향후 확인이 필요하다. 전반적으로 과학 AI 신뢰성이라는 중요한 주제에 대한 **기초적이지만 가치 있는 프레임워크 연구**로 평가할 수 있다.
