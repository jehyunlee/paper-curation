---
title: "881_When_ai_co-scientists_fail_Spot-a_benchmark_for_automated_ve"
authors:
  - "Guijin Son"
  - "Jiwoo Hong"
  - "Honglu Fan"
  - "Heejeong Nam"
  - "Hyunwoo Ko"
date: "2025"
doi: "N/A"
arxiv: ""
score: 4.0
essence: "대규모 언어모델(LLM)이 과학 논문의 오류를 자동으로 검증할 수 있는가를 묻는 본 논문은 83개 출판 논문과 91개의 검증된 오류로 구성된 SPOT 벤치마크를 제시하며, 최신 LLM들도 21.1% 이하의 재현율(recall)에 머물러 신뢰성 있는 학술 검증 자동화는 아직 불가능함을 보여준다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/LLM_Review_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Son et al._2025_When ai co-scientists fail Spot-a benchmark for automated verification of scientific research.pdf"
---

# When AI Co-Scientists Fail: SPOT—a Benchmark for Automated Verification of Scientific Research

> **저자**: Guijin Son, Jiwoo Hong, Honglu Fan, Heejeong Nam, Hyunwoo Ko, Seungwon Lim, Jinyeop Song, Jinhang Choi, Gonçalo Paulo, Youngjae Yu, Stella Biderman | **날짜**: 2025 | **DOI**: N/A

---

## Essence

![Figure 1: Overview of SPOT](figures/fig1.webp)
*SPOT 벤치마크의 구축 과정: 시드 수집(녹색)부터 검증, 정규화를 거쳐 평가 단계(파란색)까지 LLM 출력을 기준 오류와 비교*

대규모 언어모델(LLM)이 과학 논문의 오류를 자동으로 검증할 수 있는가를 묻는 본 논문은 83개 출판 논문과 91개의 검증된 오류로 구성된 SPOT 벤치마크를 제시하며, 최신 LLM들도 21.1% 이하의 재현율(recall)에 머물러 신뢰성 있는 학술 검증 자동화는 아직 불가능함을 보여준다.

## Motivation

- **Known**: LLM은 가설 생성, 코드 합성, 원고 작성 등 과학 연구의 "생성 역할(forward pass)"에서 활용되고 있으며, 대학원 수준의 STEM 능력을 보여주고 있음

- **Gap**: 반면 학술 검증(backward pass)이나 검증자(verifier)로서의 역할은 충분히 탐구되지 않았으며, 대부분의 시스템은 검증되지 않은 LLM 판사(LLM judges)에 의존하고 있음. 기존 사실 검증 연구는 일상적 지식 작업이나 특정 분야(예: 컴퓨터과학)에만 국한됨

- **Why**: 과학 연구의 신뢰성 확보를 위해 LLM의 실제 검증 능력에 대한 엄밀한 평가가 필수적

- **Approach**: 10개 학문 분야에 걸친 83개 최신 논문(2024년 이후 발표)에서 91개의 검증된 오류를 수집하고, 저자 확인 및 인간 주석가 교차검증을 거쳐 SPOT 벤치마크 구성

## Achievement

![Figure 2: Distribution of annotated errors by research domain and error type](figures/fig2.webp)
*오류의 학문 분야별, 유형별 분포: 수학/물리/컴퓨터과학은 수식/증명 오류에 집중, 생물학은 그림 중복에 편향*

1. **벤치마크 품질 확보**: 자동 필터링(2단계) → 저자 검증 → 인간 검증(2단계) → 정규화(GPT-4o + 수동 감사) 파이프라인으로 높은 신뢰도의 오류 데이터셋 구축. 평균 12,877개 토큰, 17.5개 이미지로 장문맥·다중모드 벤치마크 실현

2. **성능 급 부족 입증**: OpenAI o3(최고 성능 모델)도 pass@1에서 18.4% 수준의 성능만 달성. 8회 독립 시행에서 모델의 신뢰도(confidence)는 거의 0에 가까우며 일관된 오류 재현에 실패

3. **다모달 약점 노출**: 추론 모델들이 특히 그림 관련 오류 탐지에서 심각한 성능 저하를 보이며, 현재 멀티모달 능력의 한계 드러냄

4. **오류 분석**: 수학, 재료과학 전문가와의 사례 연구에서 모델이 웹 데이터에 부족한 장꼬리 지식(long-tail knowledge), 초장문맥 처리, 도메인 특정 관례 부재로 인한 학생 수준의 오류 반복

## How

![Figure 3: 오류 탐지 과정](figures/fig3.webp)
*TP/FP/FN 분류: 모델이 정확한 위치의 오류를 발견하면 TP, 벤치마크에 없는 오류를 지적하면 FP, 실제 오류를 놓치면 FN*

**데이터 수집 및 정규화:**
- WithdraxIV(철회 논문 14,000편)와 PubPeer(사후 익명 동료평가 사이트)에서 시드 수집
- GPT-4o를 통한 자동 필터링: (1) 명시적 위치 지정 여부, (2) 외부 자료 필요 여부
- 2024년 이후 발표 논문만 선별(모델 학습 데이터 오염 방지)
- 저자 직접 확인: PubPeer 댓글의 저자 응답 또는 WithdraxIV 자동 철회로만 확정
- 인간 검증(2단계): 조건 충족(자체포함성, 식별가능성, 저자 확인) 여부 확인 → 종합 감사
- PDF 정규화: Llama-Parse로 마크다운 변환 → 고충실 스크린샷 추출(페이지당 8개 이미지) → GPT-4o로 OCR 오류 수정 → 수동 감사

**평가 프로토콜:**
- 원문(텍스트+이미지)과 함께 구조화된 JSON 형식의 오류 반환 프롬프트 제시
- 진양성(TP): 모델 보고 위치와 벤치마크 주석이 일치 + LLM 확인을 통한 동일 오류 판정
- 재현율(recall), 정밀도(precision), pass@K 메트릭 사용

**오류 분류:**
- 귀납적 분류로 6가지 범주 도출: 수식/증명(37), 그림 중복(27), 데이터 불일치(18), 통계 보고(4), 시약 정체성(3), 실험 설계(2)
- 심각도: 정정 논문(59) vs. 철회(32)

## Originality

- **최초 시도**: LLM을 과학 논문 검증의 백워드 패스에 적용하는 벤치마크 제시. 기존 연구는 제너레이션 역할 중심
- **엄격한 큐레이션**: 저자 직접 확인 + 이중 인간 검증으로 "비논쟁적 오류(noncontroversial errors)"만 포함. 신뢰도 우선주의
- **다중모달·장문맥 복합성**: 평균 12k 토큰 + 17.5개 이미지로 기존 오류탐지 벤치마크(예: GPQA-D)보다 훨씬 현실적 복잡도 실현
- **도메인 다양성**: 10개 학문 분야의 자연스러운 오류 분포 반영(a priori 분류 X)
- **문서 정규화 혁신**: OCR 실패를 LLM의 책임으로 귀속시키기 위해 후처리 단계 도입(이전 연구는 원본 PDF 사용으로 파서 오류와 혼재)

## Limitation & Further Study

**한계:**
- **표본 크기**: 83개 논문은 고품질이나 절대 규모가 작음. 통계적 일반화 한계
- **도메인 편향**: 수학·컴퓨터과학 오류 편향(그림 중복 필터링으로 생물학 저대표)
- **시간적 편향**: 2024년 이후 논문만 포함으로 장시간 검증된 문제 미포함 가능성
- **저자 응답 의존성**: 저자가 응답하지 않은 실제 오류 누락(false negative 발생 가능)
- **LLM 기반 TP 판정**: 진양성 확인을 LLM에 의존하므로 순환 논리 위험

**후속 연구:**
- 더 큰 규모의 다중 도메인 오류 수집(특히 생물학, 의학)
- 오류 심각도의 세분화(현재는 정정/철회 이분법)
- LLM 검증자의 신뢰성 향상을 위한 프롬프팅·파인튜닝 전략 개발
- 인간 동료 평가자와 LLM 검증자의 성능 비교
- 도메인 특화 모델(수학, 과학) 벤치마킹
- 오류의 인과적 근원(부정확한 실험 설계 vs. 보고 오류) 분석

## Evaluation

- **Novelty**: 4.5/5 — LLM의 검증자 역할을 체계적으로 평가한 최초 시도이며, 저자 확인·다중 검증을 통한 높은 신뢰도 벤치마크 설계가 우수함. 다만 규모 제약으로 완전히 새로운 영역은 아님

- **Technical Soundness**: 4/5 — 데이터 수집·정규화·평가 프로토콜이 체계적이고 투명함. 다만 LLM 기반 TP 판정의 순환성과 도메인 불균형이 약점

- **Significance**: 4.5/5 — AI 기반 과학 검증의 현재 한계를 명확히 입증하고, 과학계의 신뢰성 우려에 실증적 근거 제공. 향후 LLM 개선의 목표 설정에 중요함

- **Clarity**: 4/5 — 논문 구조와 방법론이 명확하고 그림이 효과적임. 다만 오류 판정의 LLM 의존성 논의가 더 깊으면 좋음

- **Overall**: 4/5

**총평**: SPOT은 LLM의 약점을 체계적으로 드러내는 견고한 벤치마크로, 현재 AI 시스템이 신뢰성 있는 과학 검증자가 되기 위해 넘어야 할 실질적 거리가 얼마나 큰지를 증명한다. 규모 한계는 있으나, 저자 확인 + 이중 검증을 통한 질적 우수성과 다중모달 장문맥의 현실적 복잡도에서 의의가 크다.

## Related Papers

- ⚖️ 반론/비판: [[papers/630_Predicting_empirical_ai_research_outcomes_with_language_mode/review]] — 과학 논문 오류 검증의 한계와 연구 아이디어 성공 예측의 가능성을 대비하여 AI의 과학 연구 지원 능력의 현실적 범위를 파악할 수 있다.
- 🔄 다른 접근: [[papers/680_Reviewing_scientific_papers_for_critical_problems_with_reaso/review]] — 과학 논문 오류 자동 검증에서 서로 다른 데이터셋과 평가 방법을 사용하여 LLM의 학술 검증 능력을 다각도로 평가한다.
- 🔗 후속 연구: [[papers/753_Shared_imagination_Llms_hallucinate_alike/review]] — LLM의 공유된 환각 패턴이 과학 논문 오류 검증에서 나타나는 낮은 성능의 근본적 원인을 설명하는 이론적 틀을 제공한다.
- ⚖️ 반론/비판: [[papers/861_Use_of_large_language_models_as_artificial_intelligence_tool/review]] — AI 공동 과학자의 실패 벤치마크가 의학 연구에서 LLM 한계를 지적한다.
- 🧪 응용 사례: [[papers/252_Data_integrity_in_materials_science_in_the_era_of_AI_balanci/review]] — 재료 과학에서 AI 데이터 무결성 문제가 AI 과학자들의 실패 사례 분석과 자동화된 검증 시스템 개발에 핵심적인 동기를 제공한다
- 🏛 기반 연구: [[papers/321_Evaluating_Sakanas_AI_Scientist_Bold_Claims_Mixed_Results_an/review]] — AI 공동과학자 실패 시 자동 검증 벤치마크가 평가의 기반 제공
- 🔄 다른 접근: [[papers/145_Autoreproduce_Automatic_ai_experiment_reproduction_with_pape/review]] — AUTOREPRODUCE와 SPOT는 모두 과학 실험 재현성을 다루지만, 논문 계보 기반 자동 재현과 AI 과학자 검증이라는 서로 다른 접근 방식을 제시합니다.
- ⚖️ 반론/비판: [[papers/630_Predicting_empirical_ai_research_outcomes_with_language_mode/review]] — 연구 아이디어 성공 예측의 긍정적 결과와 과학 논문 오류 검증의 한계를 대비하여 AI의 과학 연구 지원 능력의 양면성을 보여준다.
- ⚖️ 반론/비판: [[papers/676_Reviewagents_Bridging_the_gap_between_human_and_ai-generated/review]] — AI 생성 심사평의 품질 향상 연구와 과학 논문 오류 검증의 한계 연구를 대비하여 AI 심사 시스템의 현실적 적용 가능성을 평가할 수 있다.
- 🔄 다른 접근: [[papers/680_Reviewing_scientific_papers_for_critical_problems_with_reaso/review]] — 철회된 논문 데이터와 검증된 오류 데이터를 활용한 두 연구 모두 과학적 오류 검출 능력을 평가하지만 서로 다른 데이터셋과 접근법을 사용한다.
- 🏛 기반 연구: [[papers/753_Shared_imagination_Llms_hallucinate_alike/review]] — LLM의 일관된 환각 패턴이 과학 논문 오류 검증에서 예측 가능한 실패 모드를 이해하는 핵심 개념적 기반을 제공한다.
