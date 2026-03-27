# ChartInstruct: Instruction Tuning for Chart Comprehension and Reasoning

**저자:** Ahmed Masry, Mehrad Shahmohammadi, Md Rizwan Parvez, Enamul Hoque, Shafiq Joty
**소속:** York University, QCRI, Salesforce Research, NTU Singapore
**출처:** arXiv:2403.09028 (2024.03)
**DOI:** [10.48550/arXiv.2403.09028](https://doi.org/10.48550/arXiv.2403.09028)

---

## Essence (본질)
차트 이해 및 추론을 위한 범용 비전-언어 모델(VLM)을 구축하기 위해, 71K개의 실세계 차트로부터 191K개의 instruction-following 데이터셋을 자동 생성하고, 이를 활용한 두 가지 시스템(end-to-end 모델과 pipeline 모델)을 제안하여 4개 벤치마크에서 SOTA를 달성한 연구이다.

## Motivation (동기)
차트는 데이터 분석과 의사결정에 핵심적인 시각화 도구이지만, 기존 차트 관련 모델들은 두 가지 근본적 한계가 있다. 첫째, 일반 비전-언어 모델을 파인튜닝한 방식은 차트 고유의 구조(바, 범례, 축 간 관계)를 간과하여 성능이 제한적이다. 둘째, UniChart, MatCha 등 차트 전용 모델은 한정된 소스와 좁은 태스크 범위에 집중하여 실제 다양한 사용 시나리오에 대응하지 못한다. 실세계 광범위 채택을 위해서는 모델이 사전에 정의되지 않은 다양한 태스크에도 대응할 수 있는 범용성이 필요하며, instruction tuning이 이에 대한 유망한 해법이다.

## Achievement (성과)
1. **대규모 차트 Instruction 데이터셋 구축:** 157개 온라인 플랫폼에서 수집한 실세계 차트 71K개로부터 GPT-3.5/GPT-4/Gemini를 활용하여 191K개의 다양한 instruction 생성 (요약 28%, QA 22%, CoT 추론 14%, 팩트 체킹 13%, 코딩 10%, LLM이 제안한 신규 태스크 12%)
2. **4개 벤치마크 SOTA 달성:**
   - ChartQA: Pipeline Flan-T5-XL이 평균 RA 72.0% (기존 UniChart 66.24% 대비 +5.76%p), human set에서 50.16%로 기존 최고 43.92% 대비 대폭 향상
   - Chart-to-Text: Statista에서 BLEU 43.53 (기존 39.4 대비 +4.13)
   - OpenCQA: BLEU 16.71 (기존 14.88 대비 +1.83)
   - ChartFC: 정확도 72.65% (기존 ChartBERT 63.8% 대비 +8.85%p)
3. **Human Evaluation:** ChartInstruct-Llama가 UniChart 대비 정보성(3.85 vs 3.2), 관련성(4.06 vs 2.74), 사실 정확성(3.66 vs 2.76) 모두에서 유의미하게 우수 (Mann-Whitney U test, p < 0.001)
4. **41K WebCharts 코퍼스 공개:** 157개 웹 도메인에서 수집한 다양한 스타일의 실세계 차트 이미지

## How (방법)
- **차트 코퍼스 수집:** (1) UniChart의 기존 611K 차트(Statista, Pew, OECD, OWID), (2) 157개 웹 도메인에서 Google 이미지 검색으로 수집한 41K WebCharts. VIT 분류기(91% 정확도)로 비차트 이미지 필터링, Gemini Pro Vision으로 데이터 테이블/제목 자동 추출
- **Instruction 생성:** 6가지 태스크 유형 -- 요약, Open-ended QA, 팩트 체킹, CoT 추론(변수 의존/독립), 코드 생성, LLM이 제안한 신규 태스크. GPT-3.5는 중간 복잡도, GPT-4는 고복잡도 태스크에 사용
- **End-to-End 시스템:** LLaVA 아키텍처 기반, CLIP 비전 인코더를 UniChart 비전 인코더로 교체. (1) alignment 단계 (어댑터만 학습, 비전 인코더+LLM 동결), (2) instruction tuning 단계 (어댑터+LLM 학습, 비전 인코더 동결). LLM으로 Llama2(7B) 또는 Flan-T5-XL(3B) 사용
- **Pipeline 시스템:** UniChart로 차트 이미지에서 데이터 테이블 추출 후, 텍스트화된 테이블+instruction을 LLM에 입력. alignment 단계 불필요
- **학습 환경:** 4x A100 GPU (80GB)

## Originality (독창성)
- **차트 도메인 최초의 포괄적 instruction tuning:** 기존 정의된 태스크뿐 아니라 LLM이 자동 제안한 신규 태스크(패턴/이상치 탐지, 상관관계 분석, 미래 예측 등)를 포함한 최초의 차트 instruction 데이터셋
- **차트 전용 비전 인코더와 LLM의 결합:** CLIP 대신 차트에 최적화된 UniChart 비전 인코더를 LLaVA 프레임워크에 통합한 설계
- **End-to-End vs Pipeline의 체계적 비교:** 두 아키텍처의 장단점을 태스크별로 분석하여, 추론 집약적 태스크에서는 pipeline이, 텍스트 생성 태스크에서는 end-to-end가 우수함을 확인
- **WebCharts 코퍼스:** 157개 다양한 웹 도메인에서 수집하여 기존 차트 데이터셋의 시각적 스타일 다양성 부족 문제를 해결
- **CoT 추론과 코드 생성 태스크 통합:** ToolFormer 영감의 변수 의존 질문과 PAL 영감의 코드 생성을 차트 도메인에 적용

## Limitation & Further Study (한계 및 향후 연구)
- **Chart-to-Table 태스크 미평가:** 주요 벤치마크 4개를 다루었으나 차트-테이블 변환 태스크는 포함되지 않음
- **Instruction 데이터 품질 한계:** 전문가 평가에서 출력의 완전 정확도가 61%에 불과하며, 부분 정확 8%, 나머지 31%는 오류 포함. 이는 instruction tuning 과정에 노이즈를 유입
- **Instruction 준수 불완전:** instruction tuning이 모델의 instruction 준수 능력을 크게 향상시켰으나, 완전히 일탈을 방지하지는 못함
- **복잡한 수치 추론의 한계:** ChartQA에서 SOTA를 달성했음에도, LLM의 수학 연산 불안정성으로 복잡한 수치 질문에서 여전히 오류 발생
- **사실 오류 생성:** 텍스트 생성 태스크에서 일관성 있는 텍스트를 생성하면서도 차트에서 지지되지 않는 사실적 오류를 포함하는 경우 존재
- **값 추정과 비교의 어려움:** 밀집되거나 세부 정보가 부족한 차트에서 시각 요소와 값의 매칭, 값 추정, 시각적 속성 기반 비교에서 오류
- **향후 연구:** 더 큰 규모의 LLM 적용, 멀티모달 입력(GPT-4V 등) 활용, 데이터 품질 개선을 위한 필터링 파이프라인, 더 다양한 차트 유형(3D, 지도 등) 지원

## Evaluation (평가)
ChartInstruct는 차트 이해 분야에서 instruction tuning 패러다임을 본격적으로 도입한 의미 있는 연구이다. 191K 규모의 다양한 instruction 데이터셋 구축과 4개 벤치마크에서의 일관된 SOTA 달성은 접근법의 유효성을 강하게 뒷받침한다. 특히 UniChart 비전 인코더를 LLaVA에 통합한 설계와, LLM이 자동으로 신규 태스크를 제안하도록 한 데이터 생성 전략은 독창적이다. End-to-end와 pipeline 두 시스템의 비교 분석은 실용적 관점에서 가치가 높으며, Flan-T5-XL(3B)이 Llama2(7B)와 유사한 성능을 보인 점은 계산 자원 제약 환경에서의 활용 가능성을 시사한다. 다만 생성 데이터의 정확도(61%)가 상대적으로 낮고, human evaluation이 저자 및 협력자에 의해 수행되어 평가 편향 가능성이 있다. Cohen's Kappa 0.447의 중간 수준 동의도도 평가의 주관성을 반영한다. 전반적으로 차트 이해 분야의 범용화를 위한 중요한 기반 연구로, 후속 연구(ChartGemma 등)에 직접적 영향을 미친 논문이다.

## 평가
| 항목 | 점수 (1-5) |
|------|-----------|
| Novelty | 4 |
| Technical Soundness | 4 |
| Significance | 3 |
| Overall | 3.7 |

**총평**: 191K 차트 인스트럭션 데이터셋과 LLM 기반 미세조정으로 4개 벤치마크 SOTA를 달성한 연구로, 체계적 파이프라인과 광범위한 평가가 차트 이해 분야의 견고한 기여를 이룬다.
