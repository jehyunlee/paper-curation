---
title: "104_Are_we_there_yet_revealing_the_risks_of_utilizing_large_lang"
authors:
  - "Rui Ye"
  - "Xianghe Pang"
  - "Jingyi Chai"
  - "Jiaao Chen"
  - "Zhen-fei Yin"
date: "2024"
doi: "N/A"
arxiv: ""
score: 4.5
essence: "본 연구는 학술 피어 리뷰에 대규모 언어모델(LLM)을 활용할 때의 심각한 보안 취약점을 최초로 종합적으로 분석한 논문이다. 저자들은 명시적 조작(explicit manipulation)과 암시적 조작(implicit manipulation), 그리고 LLM의 내재적 결함을 통해 LLM 기반 리뷰어가 얼마나 쉽게 오도될 수 있는지를 실증적으로 입증한다."
tags:
  - "cat/Academic_Peer_Review_Automation"
  - "sub/AI_Peer_Review"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Ye et al._2024_Are we there yet revealing the risks of utilizing large language models in scholarly peer review.pdf"
---

# Are we there yet? revealing the risks of utilizing large language models in scholarly peer review

> **저자**: Rui Ye, Xianghe Pang, Jingyi Chai, Jiaao Chen, Zhen-fei Yin, Zhen Xiang, Xiaowen Dong, Jing Shao, Siheng Chen | **날짜**: 2024 | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp)
*그림 1: (a) 학술 커뮤니티가 피어 리뷰에 LLM 도입을 시작했으며, (b) 프롬프트 주입을 통한 명시적 조작, (c) LLM이 저자가 공개한 한계를 인용할 가능성이 높으며, (d) 불완전한 콘텐츠에도 부당히 높은 점수를 부여함*

본 연구는 학술 피어 리뷰에 대규모 언어모델(LLM)을 활용할 때의 심각한 보안 취약점을 최초로 종합적으로 분석한 논문이다. 저자들은 명시적 조작(explicit manipulation)과 암시적 조작(implicit manipulation), 그리고 LLM의 내재적 결함을 통해 LLM 기반 리뷰어가 얼마나 쉽게 오도될 수 있는지를 실증적으로 입증한다.

## Motivation

- **Known**: 최근 논문들(예: Nature 저널에서 30% 이상 겹침)이 LLM 기반 리뷰와 인간 리뷰 간 상당한 일치도를 보여주었으며, AI 학회들에서 이미 6.5-16.9%의 리뷰가 LLM의 영향을 받고 있음

- **Gap**: 학술 커뮤니티가 LLM을 리뷰 자동화에 널리 도입하고 있음에도 불구하고, 관련 보안 위험성에 대한 체계적이고 종합적인 분석이 부족함

- **Why**: 피어 리뷰는 과학 진실성의 핵심이며, 검증되지 않은 LLM 통합은 의도적 조작이나 편향된 평가를 통해 과학계에 심각한 손상을 초래할 수 있음

- **Approach**: ICLR 2024의 공개 피어 리뷰 데이터셋을 활용하여 (1) 명시적 조작(PDF에 작은 흰색 폰트로 조작 텍스트 주입), (2) 암시적 조작(저자가 한계를 의도적으로 강조), (3) 내재적 결함(불완전한 콘텐츠, 저자명 편향, 논문 길이 편향)에 대한 통제된 실험 수행

## Achievement

![Figure 2](figures/fig2.webp)
*그림 2: 조작 전후 리뷰 평점 비교*

1. **명시적 조작의 극단적 취약성**: 프롬프트 주입을 통해 LLM-조작 내용 일치도가 90% 이상 달성, 반면 LLM-인간 일치도는 53%에서 16%로 급락. 조작된 리뷰의 평점이 평균 5.34에서 7.99로 상승하여 거의 모든 논문이 긍정적 평가를 받음

2. **암시적 조작의 4.5배 높은 영향력**: 저자가 공개한 한계에 대해 LLM은 인간 리뷰어보다 4.5배 더 높은 일치도(consistency)를 보임. 이는 LLM이 저자의 프레이밍에 매우 취약함을 의미함

3. **내재적 결함의 광범위한 영향**: 
   - 불완전한 콘텐츠(제목만 있는 논문)가 완전한 논문의 42%보다 높거나 동등한 점수 획득
   - 단일 맹검(single-blind) 검토에서 저명 저자 표기가 더 호의적 리뷰 생성
   - 논문 길이가 길수록 더 호의적 피드백 수신

4. **시뮬레이션 영향**: 5%의 리뷰만 조작해도 상위 30% 순위에서 12%의 논문이 순위를 잃을 수 있음을 시뮬레이션으로 입증

## How

![Figure 3](figures/fig3.webp)
*그림 3: 상위 30% 논문에 대한 체계적 영향*

- **명시적 조작 방법론**:
  - PDF 파일의 결론 부분 이후에 극히 작은(거의 보이지 않는) 흰색 폰트로 조작 텍스트 삽입
  - 인간 리뷰어에게는 감지 불가능하나 PDF 파서에는 읽을 수 있음
  - 강점 강조, 약점 축소하는 방향으로 조작 내용 구성

- **암시적 조작 방법론**:
  - 저자가 한계사항(limitation statement)을 의도적으로 강조하는 시나리오
  - NeurIPS 등 일부 학회에서 권장하는 약점 공개 문화를 악용
  - 사소한 한계를 부풀려서 LLM의 리뷰 생성에 영향

- **내재적 결함 분석**:
  - 제목만, 초록만, 본문 일부 등 단계적으로 불완전한 콘텐츠 제공
  - 저자명 유무로 단일 맹검 설정 검증
  - 논문 길이 변수화를 통한 편향 측정

- **평가 지표**:
  - 일치도(consistency) 메트릭: 두 리뷰 간 핵심 포인트 겹침 정도
  - 1-10 스케일 평점: 직접적인 논문 채택 결정 요소
  - 상위 30% 순위 변화 시뮬레이션

## Originality

- **최초 종합 분석**: 학술 피어 리뷰 맥락에서 LLM의 조작 취약성을 체계적으로 최초 규명

- **실제적 공격 방법론**: PDF 주입 공격, 암시적 프레이밍 등 현실적이고 구현 가능한 조작 기법을 설계

- **다층 평가 체계**: 명시적-암시적 조작과 내재적 결함을 동시에 분석하여 다면적 위험 구조 도출

- **확률적 영향 모델링**: 5% 조작이 12% 순위 변화를 초래하는 것으로 실측하여 체계적 영향 정량화

- **실제 데이터 기반**: ICLR 2024 공개 리뷰 데이터를 활용하여 이론이 아닌 현실적 검증

## Limitation & Further Study

- **데이터셋 제한**: 현재 ICLR 2024에만 집중하였으며, Nature 저널 등 다른 학술 플랫폼으로의 확장이 필요

- **LLM 모델 범위**: 특정 LLM(주로 GPT 계열로 추정)에 기반한 분석으로, 다양한 오픈소스 모델(Llama, Claude 등)과의 일반화 필요

- **조작 탐지 방법 부재**: 본 논문은 위험성 노출에 중점이 있으며, 조작을 감지하는 방어 메커니즘 제시 부족

- **평가 모델의 투명성**: "평점 모델(rating model)"의 구체적 설계가 제시되지 않아 재현성 우려

- **후속 연구 방향**:
  - 조작 탐지 및 예방 기술 개발(watermarking, adversarial training)
  - 다양한 LLM 및 리뷰 파이프라인 확대 실험
  - 인간-LLM 협력형 검토 시스템의 안전한 설계
  - 장기적으로 LLM을 보조 도구가 아닌 완전 자동 리뷰어로 활용하기 위한 견고성 강화 연구

## Evaluation

- **Novelty**: 4.5/5 - 학술 피어 리뷰 보안 관점에서 최초이며, 조작 기법들이 혁신적이나, 일반적인 LLM 취약성의 피어 리뷰 적용일 수 있음

- **Technical Soundness**: 4/5 - 실험 설계가 논리적이고 ICLR 데이터 기반이나, 평점 모델 설계의 투명성 부족, 샘플 크기(n=?) 미기재

- **Significance**: 5/5 - 과학 진실성에 직결된 매우 중요한 주제이며, 현재 LLM 채택 추세에 대한 긴급한 경고 신호 제공. 정책 및 학회 운영에 즉각적 영향 가능

- **Clarity**: 4.5/5 - 글이 명확하고 Figure들이 직관적이며, 구체적 사례 제시가 좋으나, 일부 기술적 상세(일치도 계산, 평점 모델)가 불충분

- **Overall**: 4.5/5

**총평**: 본 논문은 LLM을 피어 리뷰에 도입하려는 학술 커뮤니티에 대해 시의적절하고 중요한 경고를 제시한다. 명시적·암시적 조작과 내재적 편향을 체계적으로 입증함으로써 LLM을 단독 리뷰어가 아닌 보조 도구로만 활용해야 함을 강하게 주장한다. 다만 다양한 모델 및 학회로의 확대 검증과 방어 메커니즘 제시를 통해 영향력을 더욱 높일 수 있을 것으로 예상된다.

## Related Papers

- 🔄 다른 접근: [[papers/270_Detecting_llm-written_peer_reviews/review]] — LLM이 작성한 피어 리뷰를 탐지하는 기술로 LLM 기반 리뷰 시스템의 보안 취약점을 보완할 수 있다.
- 🔗 후속 연구: [[papers/678_ReviewerGPT_An_Exploratory_Study_on_Using_Large_Language_Mod/review]] — LLM을 피어 리뷰에 활용하는 탐색적 연구로, 본 논문이 밝힌 보안 위험에 대한 실증적 배경을 제공한다.
- 🏛 기반 연구: [[papers/471_Large_Language_Models_Cannot_Self-Correct_Reasoning_Yet/review]] — LLM의 자기교정 추론 한계를 다루는 연구로, 피어 리뷰에서 LLM이 쉽게 조작당하는 이유를 설명한다.
- 🔄 다른 접근: [[papers/870_Vulnerability_of_text-matching_in_mlai_conference_reviewer_a/review]] — 학술 피어 리뷰 시스템의 또 다른 보안 취약점을 다루어 종합적인 보안 대책 수립에 필요하다.
- ⚖️ 반론/비판: [[papers/678_ReviewerGPT_An_Exploratory_Study_on_Using_Large_Language_Mod/review]] — LLM 논문 심사의 가능성 탐구와 대규모 언어 모델 활용의 위험성 분석을 통해 AI 심사 도입의 신중한 접근 필요성을 확인할 수 있다.
