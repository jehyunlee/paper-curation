---
title: "714_Scideator_Human-llm_scientific_idea_generation_grounded_in_r"
authors:
  - "Marissa Radensky"
  - "Simra Shahid"
  - "Raymond Fok"
  - "Pao Siangliulue"
  - "Tom Hope"
date: "2024"
doi: "arXiv:2409.14634"
arxiv: ""
score: 0
essence: "과학 논문 작성에서 기존 연구의 핵심 측면들을 새로운 방식으로 결합하여 창의적 아이디어를 생성하는 것을 지원하는 사람-LLM 협력 시스템이다. 사용자가 선택한 논문들로부터 추출된 구조화된 요소(목적·메커니즘·평가)를 대화형으로 재조합하여 새로운 연구 아이디어를 탐색하도록 설계되었다."
tags:
  - "cat/AI-Powered_Scientific_Research_Frameworks"
  - "sub/Biomedical_Research_Agents"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Jackson et al._2024_Scideator Human-llm scientific idea generation grounded in research-paper facet recombination.pdf"
---

# Scideator: Human-LLM scientific idea generation grounded in research-paper facet recombination

> **저자**: Marissa Radensky, Simra Shahid, Raymond Fok, Pao Siangliulue, Tom Hope, Daniel S. Weld | **날짜**: 2024 | **DOI**: [arXiv:2409.14634](https://arxiv.org/abs/2409.14634)

---

## Essence

![Figure 1](figures/fig1.webp)
*Scideator의 인터페이스: 사용자와 시스템이 논문의 핵심 요소(목적, 메커니즘, 평가)를 중심으로 상호작용하며 아이디어를 재조합하는 과정*

과학 논문 작성에서 기존 연구의 핵심 측면들을 새로운 방식으로 결합하여 창의적 아이디어를 생성하는 것을 지원하는 사람-LLM 협력 시스템이다. 사용자가 선택한 논문들로부터 추출된 구조화된 요소(목적·메커니즘·평가)를 대화형으로 재조합하여 새로운 연구 아이디어를 탐색하도록 설계되었다.

## Motivation

- **Known**: 
  - 과학자들은 기존 논문의 다양한 측면을 혼합하여 새로운 아이디어를 생성한다 (facet-based ideation).
  - 선행 연구에서는 논문의 구조화된 표현(목적, 메커니즘 등)이 창의적 탐색을 촉진함을 입증했다.
  - LLM은 아이디어 합성과 평가를 빠르게 수행할 수 있는 잠재력을 보여준다.

- **Gap**: 
  - 기존 facet 기반 연구는 유사 논문 제시에만 그쳤으며, 실제 아이디어 합성이나 참신성 평가 인터페이스가 없었다.
  - 인간-LLM 협력 시스템 중 facet 기반 과학 아이디어 생성을 다룬 연구가 없다.
  - 생성된 아이디어의 참신성 평가 메커니즘이 체계적으로 평가된 적 없다.

- **Why**: 
  - 끊임없이 확장되는 과학 문헌과 인지적 고착(cognitive fixation)으로 인해 과학자들이 새로운 영감을 발견하기 어려워지고 있다.
  - 구조화된 facet 표현은 사용자의 자유 텍스트 프롬핑보다 더 명확한 제어 신호를 제공할 수 있다.

- **Approach**: 
  - 세 개의 LLM 기반 모듈(유사 논문 탐색, 아이디어 생성, 참신성 검증)로 구성된 통합 시스템 개발.
  - 모든 단계에서 동일한 facet 표현(목적·메커니즘·평가) 유지.
  - 사용자-시스템 상호작용을 facet 수준의 선택·수정으로 구조화.

## Achievement

![Figure 3](figures/fig3.webp)
*사용자들이 LLM 제안보다 자신이 선택한 facet을 포함한 아이디어를 더 선호한 비율*

![Figure 5](figures/fig5.webp)
*Scideator vs. 기준 도구(baseline)의 창의성 지원 지수(CSI) 비교*

1. **Scideator 시스템**: 
   - 모듈 1(유사 논문 Facet 탐색): 목적-메커니즘 쌍을 기반으로 다양한 개념적 거리(근거리·원거리·극원거리)의 유사 논문 검색.
   - 모듈 2(Facet 아이디어 생성): 사용자가 선택한 facet들로부터 유추를 통해 새로운 아이디어 생성.
   - 모듈 3(아이디어 참신성 검증): facet 기반 매칭으로 기존 문헌과 비교하여 참신성 판정 및 개선 제안 제시.

2. **사용자 연구 결과** (22명의 컴퓨터과학 연구자 참여, 동일 대상 내 비교 설계):
   - Scideator가 기준 도구(동일 LLM 백본, facet 모듈 없음)보다 **유의미하게 더 높은 창의성 지원** 제공 (특히 아이디어 탐색 측면).
   - 사용자들이 기준 도구에서는 입력 논문을 주로 인용한 반면, **Scideator에서는 시스템의 facet과 생성 아이디어를 새로운 개념 발견의 근거로 제시** (입력 논문을 넘어서는 사고 확장 증거).
   - 사용자들이 **자유 텍스트 지시문 사용 감소**, facet 수준 제어 선호.
   - 사용자가 선택한 facet을 포함한 아이디어가 LLM 선택 아이디어보다 더 자주 선호됨.

3. **참신성 검증 성능**:
   - **Facet 기반 재정렬로 분류 정확도 13.79% → 89.66% 향상**.
   - 사용자들이 시스템의 '참신하지 않음' 판정을 확인하고 자신의 평가를 하향 조정하는 행동 관찰.

## How

![Figure 2](figures/fig2.webp)
*Scideator의 전체 워크플로우: (1) 입력 논문 제공 → (2) Facet 추출 및 유사 논문 검색 → (3) Facet 선택 및 재조합 → (4) 아이디어 생성 → (5) 참신성 평가 및 제안*

### 시스템 구조

**1. Shared Faceted Representation (공유 표현)**
   - 세 가지 facet으로 아이디어와 논문 표현:
     - **목적(Purpose)**: 해결하려는 문제
     - **메커니즘(Mechanism)**: 제안된 솔루션
     - **평가(Evaluation)**: 솔루션 효과 검증 방법
   - LLM 프롬프팅을 통해 제목·초록으로부터 짧은 구문(≤7단어) 추출.

**2. Module 1: Analogous Paper Facet Finder**
   - 입력 논문의 목적-메커니즘 쌍 추출.
   - 세 가지 거리 수준의 유사 논문 검색:
     - **근거리(Near)**: 동일 주제, 다른 접근법
     - **원거리(Far)**: 관련 영역, 추상적 구조 유사성
     - **극원거리(Very Far)**: 완전히 다른 영역, 고수준 유추
   - 검색된 논문에서 세 facet 추출.

**3. Module 2: Faceted Idea Generator**
   - 사용자가 검색된 논문들 중 흥미로운 facet 선택 (또는 시스템에 맡김).
   - 선택된 facet들을 유추를 통해 새로운 목적-메커니즘 조합으로 재조합.
   - 여러 아이디어 생성, 사용자가 추구할 아이디어 선택.

**4. Module 3: Idea Novelty Checker**
   - **Facet 기반 비교**: 생성된 아이디어가 다음 중 하나를 만족하면 참신:
     - 검색된 논문과 적어도 하나의 핵심 facet이 다름
     - 기존 facet의 고유한 조합
     - 새로운 영역 적용
   - **검색-재정렬 파이프라인**: 
     - 초기 논문 검색(general relevance)
     - facet 매칭 기준으로 재정렬
   - 참신하지 않은 아이디어에 대해 facet 교체 제안.

**5. 반복 루프**
   - 모듈 3의 제안 수용 → 모듈 2로 재생성
   - 새로운 facet 선택 → 모듈 1로 복귀
   - 사용자의 facet 수준 피드백이 각 모듈을 재구성.

### 핵심 설계 원칙

- **인간 중심 facet 재조합**: 사용자가 facet 선택, 시스템이 유추 기반 아이디어 생성.
- **거리 제어 검색**: 같은 주제부터 전혀 다른 분야까지 창의적 방향의 스펙트럼 제공.
- **참신성 평가 통합**: facet 기반 구조적 비교로 일관된 평가.

## Originality

- **첫 facet 기반 인간-LLM 과학 아이디어 생성 시스템**: 
  - 선행 연구는 유사 논문 제시에만 그쳤으나, 이 연구는 전체 아이디어 합성-평가 파이프라인 통합.

- **통일된 facet 표현의 일관된 활용**: 
  - 검색·생성·평가·피드백의 모든 단계에서 동일한 구조화된 표현 유지로, 사용자 신호의 명확성과 시스템의 일관성 극대화.

- **거리 제어 검색 메커니즘**: 
  - 창의적 탐색을 위해 동심원적 검색 공간(near/far/very far) 도입.

- **참신성 평가의 체계적 평가**: 
  - 인간-AI 아이디어 시스템에서 처음으로 참신성 판정 파이프라인과 사용자 해석 행동을 함께 분석.
  - Facet 기반 재정렬의 효과를 ablation으로 입증.

- **사용자 연구 설계의 엄밀성**: 
  - 동일 대상 내 비교(within-subjects) 설계로 confounding 제거.
  - 정성적(사용자 인터뷰) + 정량적(CSI 지수) 혼합 방법론.

## Limitation & Further Study

**한계:**
1. **작은 표본 규모**: 22명의 컴퓨터과학 연구자만 참여 → 다른 학문 분야 일반화 가능성 제한.
2. **한정된 입력 스케일**: 사용자가 제공하는 초기 논문 수(일반적으로 적음)가 아이디어 품질에 미치는 영향 미분석.
3. **Facet 추출 품질 평가 부재**: LLM 프롬프팅으로부터의 facet 추출 오류 및 그 영향에 대한 체계적 분석 없음.
4. **참신성 판정의 주관성**: 논문에서 facet 기반 정의를 도입했지만, 실제 전문가 간 동의도(inter-rater agreement) 측정 미흡.
5. **장기적 영향 평가 부재**: 생성된 아이디어가 실제 논문 작성으로 이어지는지, 얼마나 자주 발표되는지 추적 불가.
6. **기준 도구의 공정성**: 기준 도구가 동일 LLM을 사용하되 facet 모듈이 없으므로, 프롬프트 엔지니어링으로 성능 개선 가능성 존재.

**후속 연구:**
- 다양한 학문 분야(생물학, 물리학, 공학 등)로 확대 평가.
- 대규모 초기 논문 집합에서 facet 추출 및 검색 확장성 개선.
- 참신성 평가 기준의 학제 간 일반화 및 전문가 검증 강화.
- 사용자의 입력 논문 수에 따른 아이디어 품질 곡선 분석.
- 생성 아이디어의 실제 연구 영향도(citation, 후속 발표) 추적.
- facet 추출 오류와 시스템 성능의 상관관계 분석.

## Evaluation

- **Novelty**: 4.5/5
  - 첫 통합 facet 기반 인간-LLM 아이디어 생성 시스템으로 충분히 참신. 다만 개별 기술(retrieval, facet 표현)은 기존 아이디어 기반.

- **Technical Soundness**: 4/5
  - 전반적으로 견고한 시스템 설계 및 구현. Facet 기반 재정렬의 효과(13.79%→89.66%)

## Related Papers

- 🔄 다른 접근: [[papers/194_Chain_of_ideas_Revolutionizing_research_via_novel_idea_devel/review]] — 혁신적 연구 아이디어 개발을 위한 아이디어 연쇄 접근법이 논문 기반 아이디어 생성과 다른 방법론을 제시한다.
- 🔗 후속 연구: [[papers/518_Many_Heads_Are_Better_Than_One_Improved_Scientific_Idea_Gene/review]] — 다중 관점을 활용한 과학 아이디어 생성 개선이 인간-LLM 협력 시스템의 발전된 형태를 보여준다.
