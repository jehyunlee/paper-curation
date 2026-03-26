# Pelican: Correcting Hallucination in Vision-LLMs via Claim Decomposition and Program of Thought Verification

## 메타 정보
- **저자**: Pritish Sahu, Karan Sikka, Ajay Divakaran (SRI International)
- **출판**: arXiv preprint, 2024
- **DOI**: [10.48550/ARXIV.2407.02352](https://doi.org/10.48550/ARXIV.2407.02352)

---

## Essence (본질)
대규모 비전-언어 모델(LVLM)의 환각(hallucination)을 탐지하고 교정하기 위한 구조화된 파이프라인 Pelican을 제안한다. LVLM의 시각적 주장(claim)을 1차 술어(first-order predicate) 기반의 원자적 하위 주장으로 분해하고, Program-of-Thought 프롬프팅으로 Python 코드를 생성하여 외부 시각 도구(객체 탐지, VQA)를 유연하게 조합해 검증한 뒤, LLM의 추론 능력으로 최종 판정 및 교정을 수행한다. MMHal-Bench에서 환각률을 기존 최선 방법 대비 27% 감소시켰다.

## Motivation (동기)
- LVLM(LLaVA, InstructBlip, mPlug-OWL 등)은 시각적 instruction following에서 뛰어난 성능을 보이지만, 존재하지 않는 객체 언급, 잘못된 속성 기술, 부정확한 공간 관계 등의 환각 문제로 신뢰성과 실용성이 제한된다.
- 기존 환각 완화 방법들은 (a) 학습 데이터 확장(LLaVA-1.5), (b) RLHF 기반 정렬(DRESS, RLHF-V), (c) 자기 피드백 수정(Volcano) 등이 있으나, 정밀한 시각적 그라운딩 부족, 약한 문맥 통합, 비효과적 추론 등의 한계가 있다.
- 기존 claim verification 접근법인 Woodpecker는 하위 질문 간 계산 공유가 없고, 특정 객체 인스턴스 참조가 불가능하며, 도구 조합의 유연성이 부족하다.

## Achievement (성과)
- **MMHal-Bench**: 다양한 베이스라인 LVLM에 Pelican 적용 시 환각률 8~32% 감소. 최선 환각 완화 기법(Volcano-13B) 대비 27% 환각률 감소(0.52 -> 0.38). Woodpecker 대비 38% 감소.
- **MME 벤치마크**: mPlug-OWL에 적용 시 146% 향상(248 -> 611). LLaVA-v1.6 대비 count와 position에서 각각 약 40% 향상. 전체 Total 715로 모든 기존 방법 능가.
- **GAVIE**: 정확도(Accuracy) 일관적 향상. 예: InstructBlip 5.61 -> 6.66, mPlug-OWL 3.88 -> 6.55.
- **POPE**: 3개 모델 모두에서 Pelican 적용 시 91% 정확도로 수렴, precision 93.62% 달성.
- **Ablation**: 공유 변수 제거 시 MME Total 590 -> 576, 공유 변수+공유 계산 모두 제거 시 485로 하락. 특히 position 범주에서 122 -> 97로 급감.

## How (방법)
1. **Visual Table (시각 테이블)**: 주장에서 LLM으로 핵심 시각 개체를 파싱한 뒤, YOLOv9(closed-vocabulary)와 Grounding-DINO(open-vocabulary)를 조합하여 객체를 탐지하고 Pandas DataFrame으로 저장. VQA 도구로 false positive를 추가 검증.
2. **Claim Decomposition (주장 분해)**: LLM 프롬팅으로 주장을 Exists, Count, Position, Color, Type, Wearing 등의 1차 술어 기반 (predicate, question) 쌍으로 분해. 중간 변수($variable_name)를 도입하여 특정 객체 인스턴스를 참조하고, 하위 질문 간 의존성 그래프(computational graph)를 구성.
3. **Program of Thought (PoT) 기반 검증**: LLM이 각 하위 질문에 대해 Python 코드를 생성하여 시각 도구(VQA, 객체 탐지, 상대 위치 계산)를 조합. 핵심 혁신: (a) 이전 하위 주장의 답변을 컨텍스트로 공유하여 중복 계산 제거 및 적응적 교정, (b) 중간 변수로 특정 인스턴스 참조, (c) 자연어 추론과 코드 계산의 결합.
4. **Integrated Verification Synthesis (통합 검증 합성)**: LLM이 모든 하위 주장의 (질문, 답변) 쌍을 종합하여 CoT 스타일 추론으로 주장의 정확성을 판정. 불일치 발견 시 환각을 제거한 수정된 주장을 생성.

## Originality (독창성)
- **계산 그래프로서의 주장 분해**: 시각적 주장을 1차 술어 기반 하위 주장의 체인으로 분해하고, 이를 의존성이 있는 계산 그래프로 개념화한 것은 기존 fact-checking 연구를 시각 도메인에 체계적으로 확장한 독창적 접근이다.
- **중간 변수와 공유 계산**: 하위 주장 간 중간 변수 공유($person_riding 등)와 이전 답변의 컨텍스트 전달은 Woodpecker 대비 핵심적 개선으로, 다중 객체가 관련된 복잡한 주장의 검증 정확도를 크게 향상시켰다.
- **PoT와 시각 도구의 유연한 조합**: Program-of-Thought 프롬팅으로 Python 코드를 생성하여 시각 도구를 네이티브 Python 연산자와 조합하는 방식은, 고정된 도구 호출 파이프라인보다 훨씬 유연하고 다양한 추론 패턴을 지원한다.

## Limitation & Further Study (한계 및 향후 연구)
- **시각 도구의 취약성(Brittleness)**: YOLO/DETR는 매우 작은 객체, 비정상적 문맥의 객체, 어휘 외 개체에 자주 실패하고, Grounding-DINO는 false positive가 많다. LLaVA-v1.6 VQA 도구도 객체 속성 질문에서 자주 오답을 반환한다.
- **LLM 출력의 비일관성**: temperature=0에서도 무작위성이 관찰되며, LLM이 복합 명사("sports ball" -> "ball", "bath towel" -> "towel")를 분리하여 객체 탐지기 실패를 유발한다. 코드 생성 단계에서 Python 인터프리터 오류가 발생하여 3회 재시도가 필요한 경우도 있다.
- **Claim 기반 검증의 한계**: (question, answer) -> claim 변환 과정에서 원래 질문의 맥락이 손실되어, GAVIE에서 relevancy 점수가 오히려 하락하는 경우가 발생한다.
- **상충 증거 처리 미흡**: 도구 실패로 인한 상충 증거를 적절히 처리하지 못하여, 올바른 주장을 부정확하게 판정하는 사례가 있다(Figure 12 참조).
- **추론 비용**: LLaVA-1.5 대비 MMHal-Bench에서 약 300배 느린 추론 시간(1.185초 vs 5분 58초). 실시간 응용에는 부적합하다.
- **GPT-4o 의존**: 파이프라인의 주요 단계(주장 분해, 코드 생성, 통합 검증)가 GPT-4o에 의존하여, 비용과 재현성 측면에서 제약이 있다.

## Evaluation (평가)
Pelican은 **LVLM 환각 문제에 대한 가장 체계적이고 구조화된 사후 교정(post-hoc correction) 프레임워크** 중 하나이다. 핵심 강점은 복잡한 시각적 주장을 원자적 하위 주장으로 분해하고, 코드 생성을 통해 시각 도구를 유연하게 조합하며, 하위 주장 간 계산을 공유하는 일관된 파이프라인 설계에 있다. MMHal-Bench에서 Woodpecker 대비 38%, Volcano-13B 대비 27%의 환각률 감소는 이 접근법의 효과를 실증한다. 특히 count와 position 같은 도전적 범주에서 40% 이상의 향상은, 중간 변수와 공유 계산이 다중 객체 추론에 핵심적임을 보여준다. 다만, 시각 도구의 취약성이라는 근본적 한계가 여전하며, 논문 스스로 이를 솔직히 인정한 점은 높이 평가할 만하다. GPT-4o 의존성과 높은 추론 비용은 실용적 배포의 주요 장벽이며, 향후 경량화된 로컬 모델로의 대체와 도구 호출의 병렬화가 필요하다. 전반적으로, NLP의 fact-checking 패러다임을 멀티모달 환각 교정에 성공적으로 적용한 의미 있는 연구로, 신뢰할 수 있는 LVLM 구축을 위한 중요한 빌딩 블록을 제공한다.
