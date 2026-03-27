# Large Language Models for Automated Open-domain Scientific Hypotheses Discovery

> **저자**: Zonglin Yang, Xinya Du, Junxian Li, Jie Zheng, Soujanya Poria, Erik Cambria | **날짜**: 2023 | **Link**: [https://arxiv.org/abs/2309.02726](https://arxiv.org/abs/2309.02726)

---

## Essence

LLM을 활용하여 open-domain raw web corpus로부터 자동으로 과학적 가설을 생성하는 최초의 시스템을 제안한 연구이다. 기존의 closed-domain, commonsense 수준 가설 생성과 달리, 사회과학 분야에서 '문헌에 존재하지 않는' novel하고 valid한 가설을 LLM이 생성할 수 있음을 GPT-4 및 전문가 평가를 통해 최초로 입증했다.

## Motivation

- **알려진 것**: 가설적 귀납(hypothetical induction)은 과학자가 관찰로부터 설명을 제안하는 핵심 추론 유형으로 인식됨
- **Gap**: 기존 연구는 수동 선별된 관찰 문장(closed-domain)과 상식 수준의 가설에 한정되어, 실제 과학적 발견과 거리가 있음
- **왜 중요한가**: Raw web corpus에서 자동으로 novel한 과학적 가설을 생성할 수 있다면, 과학적 발견의 속도를 획기적으로 가속화 가능
- **접근법**: Open-domain raw web corpus를 관찰 데이터로 사용하고, multi-module framework에 3가지 feedback mechanism을 결합하여 가설 생성 품질을 향상

## Achievement

1. 사회과학 분야 최초의 academic hypothesis discovery dataset 구축 -- open-domain raw web corpus 기반
2. GPT-4 기반 평가와 전문가 평가 모두에서 기존 방법 대비 우수한 가설 생성 성능 달성
3. 3가지 feedback mechanism (self-reflection, retrieval-augmented, iterative refinement)을 통한 체계적 성능 향상
4. LLM이 '문헌에 존재하지 않는(novel)' 동시에 '현실을 반영하는(valid)' 과학적 가설을 생성할 수 있음을 최초 입증

## How

- **데이터**: Open-domain raw web corpus를 관찰 소스로 활용, 사회과학 분야 가설-관찰 쌍으로 구성된 새로운 벤치마크 데이터셋 구축
- **Multi-module Framework**: 관찰 추출 → 패턴 인식 → 가설 생성의 파이프라인 구조로, 각 단계에서 LLM의 추론 능력을 활용
- **Feedback Mechanisms**: Self-reflection, retrieval-augmented verification, iterative refinement의 3가지 피드백으로 가설 품질 개선
- **평가 체계**: GPT-4 자동 평가와 domain expert 수동 평가를 병행하여 novelty, validity, helpfulness를 다각도로 검증

## Originality

- **Open-domain Scientific Hypothesis Discovery**: 수동 큐레이션 없이 raw web corpus에서 직접 가설을 도출하는 최초의 task 정의로, 기존 closed-domain 설정의 근본적 한계를 극복
- **Novel + Valid 가설 생성**: LLM이 단순 상식이 아닌 학술 문헌에 없는 새로운 가설을 생성하면서도 현실 반영성을 유지할 수 있음을 실증
- **Multi-feedback Framework**: Self-reflection, retrieval-augmented, iterative refinement을 결합한 체계적 가설 품질 향상 메커니즘 설계

**Abstract에서 추출된 독창성 문장**: In this work, we tackle these problems by proposing the first dataset for social science academic hypotheses discovery, with the final goal to create systems that automatically generate valid, novel, and helpful scientific hypotheses, given only a pile of raw web corpus.. Unlike previous settings, the new dataset requires (1) using open-domain data (raw web corpus) as observations; and (2) proposing hypotheses even new to humanity.. A multi-module framework is developed for the task, including three different feedback mechanisms to boost performance, which exhibits superior performance in terms of both GPT-4 based and expert-based evaluation.. To the best of our knowledge, this is the first work showing that LLMs are able to generate novel (''not existing in literature'') and valid (''reflecting reality'') scientific hypotheses.

## Limitation & Further Study

### 저자들이 언급한 한계

- 사회과학 분야에 한정된 실험으로, 자연과학 등 다른 분야로의 일반화 검증이 부족
- Generated hypothesis의 실험적 검증(empirical validation)까지 수행하지 못함
- GPT-4 기반 자동 평가의 신뢰성에 대한 추가 검증 필요

### 자체판단 아쉬운 점

- Web corpus의 품질과 편향이 생성되는 가설에 미치는 영향에 대한 분석이 부족
- 생성된 가설의 falsifiability(반증 가능성) 평가가 없어, 과학적 가설로서의 엄밀한 자격 검증이 미흡
- Human expert 평가의 규모가 제한적이며, inter-annotator agreement에 대한 보고가 불충분

### 후속 연구

- 자연과학, 공학 등 다양한 도메인으로의 확장 및 domain-specific knowledge integration
- 생성된 가설의 자동 실험 설계 및 검증 파이프라인 구축
- Multi-modal data (이미지, 표, 그래프)를 관찰 소스로 활용하는 확장

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 4/5 |
| Technical Soundness | 3/5 |
| Significance | 4/5 |
| Clarity | 4/5 |
| Overall | 4/5 |

**총평**: Open-domain에서 LLM 기반 과학적 가설 자동 생성이라는 새로운 연구 방향을 개척한 의미 있는 work이다. Task 정의와 dataset 구축의 기여가 크나, 생성된 가설의 실증적 검증과 도메인 일반화에 대한 후속 연구가 필요하다.
