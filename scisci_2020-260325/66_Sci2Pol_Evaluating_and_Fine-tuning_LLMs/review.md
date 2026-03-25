# Sci2Pol: Evaluating and Fine-tuning LLMs on Scientific-to-Policy Brief Generation

> **저자**: Weimin Wu, Alexander C. Furnas, Eddie Yang, Gefei Liu, Akhil Pandey Akella, Xuefeng Song, Dashun Wang, Han Liu | **날짜**: 2025-09-25 | **Journal**: arXiv preprint | **DOI**: 10.48550/arXiv.2509.21493

---

## Essence

과학 논문에서 정책 브리프(policy brief)를 생성하는 LLM의 능력을 평가하고 향상시키기 위한 최초의 벤치마크(Sci2Pol-Bench, 18개 태스크)와 학습 데이터셋(Sci2Pol-Corpus, 639쌍)을 제시했다. 13개 LLM 평가 결과, 최첨단 모델(Grok, DeepSeek-R1 등)도 정책 브리프 생성에서 상당한 개선 여지가 있으며, Sci2Pol-Corpus로 파인튜닝한 Gemma-27B가 GPT-4o와 DeepSeek-V3(671B)를 능가하는 성능을 달성했다.

## Motivation

- **알려진 것**: 과학적 증거를 정책에 반영하는 것은 기후변화, 공중보건 등 현대 사회의 핵심 과제이나, 대부분의 과학자는 정책 전문성이 부족하고 정책결정자는 밀도 높은 기술 논문을 실용적 지침으로 변환하기 어렵다.
- **갭**: LLM이 강력한 범용 능력을 보이지만, 정책 브리프 생성에서는 핵심 내용 누락, 환각(hallucination), 부적절한 톤, 낮은 행동가능성(actionability) 등의 한계를 보인다. 이 과제에 특화된 벤치마크나 학습 데이터셋이 존재하지 않았다.
- **접근법**: 인간 작성 프로세스를 반영한 5단계 분류체계(Autocompletion, Understanding, Summarization, Generation, Verification)에 기반한 18개 태스크 벤치마크를 구축하고, 560만 정책 문서에서 인용 기반으로 639쌍의 고품질 학습 데이터를 큐레이션한다.

## Achievement

1. **Sci2Pol-Bench 구축**: 85개 전문가 작성 논문-브리프 쌍(Nature Energy, Nature Climate Change 등)을 기반으로 5단계 18개 태스크를 설계하고, BERTScore/ROUGE의 한계를 입증하여 LLM-as-a-judge 기반 평가 지표를 개발했다.
2. **13개 LLM 대규모 평가**: Grok-3-beta가 평균 77.01로 1위, DeepSeek-R1(75.05) 2위, GPT-4o(72.12) 5위를 기록했으며, Autocompletion과 Understanding 태스크에서 모델 간 가장 큰 성능 차이가 관찰되었다.
3. **Sci2Pol-Corpus 큐레이션**: 560만 정책 문서 → 140,000 후보 쌍(인용 3편 이하 필터) → GPT-o3 조대/세밀 필터링 → 639쌍 선별 → in-context polishing의 체계적 파이프라인을 구축했다.
4. **파인튜닝 효과 입증**: LLaMA-3.1-8B(+7.64), Gemma-12B(+3.12), Gemma-27B(+2.03)의 일관된 성능 향상을 달성했으며, 파인튜닝된 Gemma-27B(73.43)가 GPT-4o(72.12)와 DeepSeek-V3(73.35)를 능가했다.
5. **LLM 실패 모드 분석**: 맥락 깊이 부족, 환각 위험, 가독성/톤 문제, 행동가능성 부족의 4가지 실패 유형을 구체적 사례와 함께 체계적으로 문서화했다.

## How

- **벤치마크 데이터**: 85개 전문가 작성 논문-브리프 쌍(Nature Energy 36, Nature Climate Change 25, JHSB 20 등), 기존 벤치마크(SciRIFF, MMLU-Pro) 통합
- **태스크 설계**: 객관식(Micro F1) 및 자유 작성(Reference-free/Reference-based Score) 형식; Generation 태스크는 Gemini-2.5-Pro 기반 LLM-as-a-judge로 다차원 평가(맥락 깊이, 환각, 가독성, 행동가능성)
- **코퍼스 큐레이션**: Overton.io 560만 정책 문서 → 인용 메타데이터로 140K 후보 쌍 → GPT-o3 조대 필터링(초록 기반, 1,407쌍) → 세밀 필터링(전문 기반, 639쌍) → 3개 전문가 작성 샘플 기반 in-context polishing
- **파인튜닝**: LLaMA-Factory, LoRA(rank 8, alpha 32), 6 에포크, 4x A100 80GB; 95/5 train/val split

## Originality

과학-정책 번역이라는 특수한 과제를 위한 최초의 체계적 벤치마크와 학습 데이터셋을 제시한 점이 핵심 기여이다. 특히 5단계 분류체계(Sci2Pol-Taxonomy)는 정책 브리프 작성의 인간 워크플로를 잘 반영하며, BERTScore/ROUGE의 한계를 실증적으로 보여준 후 태스크별 맞춤 LLM-judge 루브릭을 설계한 것이 방법론적으로 견실하다. 560만 정책 문서에서 639쌍을 큐레이션하는 대규모 파이프라인도 재현 가능한 기여이다.

## Limitation & Further Study

### 저자들이 언급한 한계
- Sci2Pol-Bench와 Sci2Pol-Corpus의 규모가 제한적이다(85쌍 벤치마크, 639쌍 코퍼스).
- 파인튜닝 결과가 아직 최고 상용 모델(Grok)을 능가하지 못한다.
- 85개 쌍이 Nature Energy, Nature Climate Change 등 에너지/기후 분야에 편중되어 있어 다른 분야로의 일반화가 제한적이다.
- JHSB의 20개 샘플에서 Policy Problem과 Study Methods 섹션이 GPT-o3에 의해 재구성되어 신뢰성이 낮을 수 있다.

### 리뷰어 판단 아쉬운 점
- LLM-as-a-judge(Gemini-2.5-Pro)의 신뢰성 검증이 10개 샘플에 대한 소규모 혼동 행렬(5/5 완벽 일치)에 의존하여, 체계적 검증으로 보기 어렵다.
- Generation 태스크(11-15)의 평가가 전적으로 LLM 판정에 의존하므로, LLM 간 상호 편향(GPT-o3로 데이터 구축 후 Gemini로 평가)의 잠재적 문제가 있다. Section F.7의 circularity 분석이 Task 16에만 한정된 점이 아쉽다.
- 에너지/기후 정책과 건강/사회 행동이라는 두 분야에 집중되어, 경제정책, 기술규제, 교육정책 등 다양한 정책 영역에 대한 적용 가능성이 검증되지 않았다.
- 정책 전문가의 실제 사용성 평가(usability study)가 없어, 생성된 브리프가 실제 정책 결정에 어떤 가치를 제공하는지 알 수 없다.

### 후속 연구
- 다학제/다언어 정책 브리프로의 확장 및 규모 확대
- 강화학습(RLHF) 등 고급 학습 전략을 통한 상용 모델 수준 달성
- 정책결정자를 대상으로 한 실제 사용성 및 신뢰성 평가

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 4/5 |
| Technical Soundness | 4/5 |
| Significance | 4/5 |
| Clarity | 4/5 |
| Overall | 4/5 |

**총평**: 과학-정책 번역이라는 중요하고 과소 연구된 과제에 대해 체계적인 벤치마크와 학습 데이터셋을 최초로 제시한 견실한 연구로, 5단계 분류체계 설계, 대규모 LLM 평가, 도메인 특화 파인튜닝의 효과 입증 등 다방면의 기여가 돋보이나, 분야 편중과 소규모 데이터셋이라는 현실적 제약이 일반화 가능성을 제한한다.
