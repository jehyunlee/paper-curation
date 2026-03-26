# Towards Autonomous Mathematics Research

> **저자**: Tony Feng, Trieu H. Trinh, Garrett Bingham, Dawsen Hwang, Yuri Chervonyi, Junehyuk Jung, Joonkyung Lee, Carlo Pagano, Sang-hyun Kim, Federico Pasqualotto, Sergei Gukov, Demis Hassabis, Quoc V. Le, Thang Luong 외 | **날짜**: 2026-02-10 | **arXiv**: 2602.10177

---

## Essence

Google DeepMind이 개발한 수학 연구 에이전트 Aletheia를 소개하고, 경시대회 수학에서 전문 연구 수학으로의 전환을 시도한 연구이다. Aletheia는 Gemini Deep Think 기반의 Generator-Verifier-Reviser 구조로, 자연어 기반 end-to-end 수학 추론을 수행한다. 주요 성과로 (A) 인간 개입 없이 생성된 출판 수준 논문(산술 기하학의 eigenweight 계산), (B) 인간-AI 협업 연구 논문, (C) Erdos 미해결 문제 700개 체계적 평가(4개 자율 해결), (D) FirstProof 벤치마크 선도 성적(10문제 중 6문제 해결)을 달성했다. 동시에 "Autonomous Mathematics Research Levels" 분류 체계와 "Human-AI Interaction Card"를 제안하여 AI 기여의 투명한 문서화를 촉구한다.

## Motivation

- **알려진 것**: AI가 2025 IMO에서 금메달 수준을 달성하여 경시대회 수학에서의 추론 능력이 입증됨. 그러나 경시대회 문제는 자기 완결적이고 고등학교 교과서 범위의 정리만 활용
- **Gap**: 연구 수학은 방대한 문헌의 고급 기법 종합이 필요하고, 수십 페이지에 달하는 긴 추론 체인이 요구됨. Foundation model의 전문 분야 이해가 훈련 데이터 부족으로 피상적이며, hallucination이 빈번
- **왜 중요한가**: AI가 자율적으로 새로운 수학 정리를 발견하고 증명할 수 있는지는 AI 기반 과학적 발견의 핵심 질문. 수학은 공리와 추론 규칙이 명확하여 AI 연구 능력 평가에 이상적 도메인
- **접근법**: IMO Gold 수준 Deep Think에 agentic harness(Generator-Verifier-Reviser)를 추가하고, 추론 시간 scaling law + 도구 사용(Google Search, 웹 브라우징)을 결합

## Achievement

1. **자율 연구 논문 (Feng26)**: 산술 기하학의 eigenweight를 인간 개입 없이 완전 자율적으로 계산. 인간 저자에게 익숙하지 않은 대수적 조합론 기법을 활용한 우아한 해법 도출
2. **Erdos 문제 체계적 평가**: 700개 미해결 문제에 Aletheia 배포. 212개 후보 해답 중 63개(31.5%) 기술적 정확, 13개(6.5%) 의미 있는 정답. 4개 문제를 자율적으로 해결
3. **FirstProof 선도 성적**: 학계 수학자가 출제한 10개 연구 수준 문제 중 6개 해결 (best-of-2). 특히 Problem 7은 출판 수준으로 평가
4. **Inference-time scaling law**: Olympiad에서 PhD 수준까지 확장되는 추론 시간 스케일링 법칙 발견. 2026년 1월 모델이 IMO Gold 모델 대비 약 100배 추론 효율 향상
5. **IMO 2025 P6 해결**: 이전 IMO Gold 모델이 실패했던 극난이도 문제를 extreme scale에서 해결

## How

- **Aletheia 아키텍처**: 3개 하위 에이전트 (Generator, Verifier, Reviser)가 반복 상호작용. Verifier가 승인하거나 시도 제한에 도달할 때까지 순환. 각 하위 에이전트는 Gemini base model 호출을 내부적으로 조율
- **핵심 설계 원칙**: 추론 모델의 최종 출력을 중간 thinking token과 분리하고, 검증 단계를 명시적으로 분리. 확장된 thinking trace가 오류의 조건부 확률을 인위적으로 높일 수 있다는 관찰에 기반
- **도구 사용**: Google Search + 웹 브라우징으로 citation hallucination 대폭 감소. Python 도구는 marginal 개선만 제공
- **평가**: (1) IMO-Proof Bench Advanced (30문제, 93% 점수), (2) FutureMath Basic (PhD 수준, 조건부 정확도 82%), (3) Erdos 문제 700개 체계적 배포, (4) FirstProof 10문제 (6/10 해결)
- **Ablation**: 동일 base model의 Gemini Deep Think (IMO scale) 대비 Aletheia가 더 낮은 compute에서 더 높은 성능 달성

## Originality

- **경시대회에서 연구 수학으로의 최초 체계적 전환**: IMO 금메달 수준에서 출판 가능한 연구 결과로의 전환을 처음으로 체계적으로 시도하고 문서화. 단순 문제 풀이를 넘어 새로운 정리를 자율적으로 발견하고 증명
- **Autonomous Mathematics Research Levels**: SAE 자율주행 레벨에서 영감을 받아, 자율성 축(H/C/A)과 수학적 중요도 축(Level 0-4)의 2차원 분류 체계 제안. AI 수학 연구의 투명한 소통을 위한 프레임워크
- **Human-AI Interaction Card**: 각 연구 성과에 대해 인간과 AI의 기여를 명시적으로 문서화하는 표준 양식 제안. AI 기반 과학 연구의 책임 있는 소통을 위한 실용적 도구
- **솔직한 한계 인정**: 성공 사례만 보고하는 관행에서 벗어나, 68.5%의 근본적 오류율, specification gaming 경향, 지속적 hallucination 문제를 투명하게 보고

## Limitation & Further Study

### 저자들이 언급한 한계

- AI가 연구 수학을 일관되게 풀 수 있다는 해석은 부적절. 성공 사례는 드물고, 자율 능력의 한계를 아는 직관이 현재로서는 중요
- Erdos 문제의 "자율 해결"이 사실 상당수가 매우 기초적(elementary)이었으며, 미해결로 남아있던 이유가 난이도가 아닌 주목 부족(obscurity)
- Hallucination이 여전히 주요 실패 모드. 도구 사용으로 노골적 citation 날조는 줄었으나, 실존 논문의 결과를 잘못 인용하는 미묘한 hallucination 지속
- 자율 결과가 인간 논문에 비해 상대적으로 짧고 기초적. 수학자들이 "진정한 창의성"으로 간주할 수준에는 미달

### 자체판단 아쉬운 점

- **재현성 제한**: Gemini Deep Think의 구체적 훈련 방법, 하이퍼파라미터, 추론 비용이 공개되지 않아 독립적 재현 불가능. Google DeepMind 내부 시스템에 완전히 의존
- **데이터 오염 우려**: IMO 2024 문제에 대한 knowledge cutoff 이슈를 저자들도 인정. Erdos 문제의 "독립적 재발견"도 사전 학습 중 간접적 흡수(subconscious plagiarism) 가능성을 배제하기 어려움
- **수학 분야 편향**: 성공 사례가 대수적 조합론, 이산 수학, 정수론 등 상대적으로 기초적인 분야에 집중. 해석학, 위상수학, 대수기하 등의 심층 연구에서의 능력은 미검증
- **비용 불투명**: "extreme scale" 추론의 실제 계산 비용이 구체적으로 제시되지 않아, 인간 수학자 대비 효율성 평가가 어려움
- **Verifier의 신뢰성**: 자연어 기반 비공식 검증에 의존하여, formal verification과의 gap이 존재. 수학적 정확성에 대한 궁극적 보장이 없음

### 후속 연구

- Formal verification과의 통합으로 증명의 완전한 정확성 보장
- 더 심층적이고 장기적인 수학 연구 프로젝트에서의 AI 협업 실험
- AI 수학 연구의 표준 문서화 체계 커뮤니티 합의 도출

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 5/5 |
| Technical Soundness | 4/5 |
| Significance | 5/5 |
| Clarity | 5/5 |
| Overall | 5/5 |

**총평**: 경시대회 수학에서 전문 연구 수학으로의 전환이라는 근본적 도전을 체계적으로 문서화한 landmark 논문이다. 인간 개입 없는 출판 수준 연구(Feng26), 700개 Erdos 문제의 체계적 평가, FirstProof 선도 성적 등 다층적 마일스톤이 인상적이다. 특히 68.5% 오류율과 hallucination 문제를 투명하게 보고하고, Autonomous Mathematics Research Levels와 HAI Card를 통해 AI 수학 연구의 책임 있는 소통 프레임워크를 제안한 점이 높이 평가된다. 현재 자율 결과가 "major advance" 수준에 도달하지 못했음을 명시적으로 인정하는 지적 정직성도 돋보인다. AI for Science의 가장 중요한 발전 중 하나로, 수학 연구에서 인간-AI 협업의 미래를 구체적으로 제시한 연구이다.
