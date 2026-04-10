---
title: "680_Reviewing_scientific_papers_for_critical_problems_with_reaso"
authors:
  - "Tianmai M. Zhang"
  - "Neil F. Abernethy (University of Washington)"
date: "2025"
doi: "arXiv:2505.23824v2"
arxiv: ""
score: 4.0
essence: "본 논문은 대규모 언어 모델(LLM)을 과학 논문의 비판적 오류 검출 도구로 활용하는 방안을 제시하며, 철회된 arXiv 논문 데이터셋을 바탕으로 추론형 LLM들의 성능과 비용을 평가합니다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/LLM_Review_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Singhal et al._2025_Reviewing scientific papers for critical problems with reasoning llms Baseline approaches and autom.pdf"
---

# Reviewing scientific papers for critical problems with reasoning llms: Baseline approaches and automatic evaluation

> **저자**: Tianmai M. Zhang, Neil F. Abernethy (University of Washington) | **날짜**: 2025 | **DOI**: [arXiv:2505.23824v2](https://arxiv.org/abs/2505.23824v2)

---

## Essence

본 논문은 대규모 언어 모델(LLM)을 과학 논문의 비판적 오류 검출 도구로 활용하는 방안을 제시하며, 철회된 arXiv 논문 데이터셋을 바탕으로 추론형 LLM들의 성능과 비용을 평가합니다.

## Motivation

- **Known**: 최근 LLM이 동료 심사(peer review) 과정에 활용되고 있으나, LLM이 인간 심사자처럼 전체 리뷰를 생성하는 방식은 부책임한 사용을 조장할 수 있음
- **Gap**: 현기존 연구들은 LLM이 생성한 전체 리뷰를 인간 리뷰와 비교하는 방식에만 집중하고 있으며, 보조적 역할로서의 활용 가능성을 충분히 탐구하지 않음
- **Why**: 동료 심사 위기(수탁 증가로 인한 심사 부담)를 해결하기 위해서는 LLM을 인간 심사자의 경쟁자가 아닌 보조 도구로 위치지어야 함
- **Approach**: LLM을 "원고 품질 검사기(manuscript quality checker)"로 활용하여 중대한 오류와 논리적 결함을 자동 식별하고, LLM을 판정자(judge)로 활용한 자동 평가 프레임워크를 제안

## Achievement

![Table 2: LLM 체커의 성능 및 비용 비교](표2.png)
*표 2: 다양한 모델들의 문제 식별 개수, 히트율(HR@5), 평균 정밀도(AP@5), 토큰 사용량 및 예상 비용 비교*

1. **o3 모델의 우수한 성능**: o3가 모든 모델 중 가장 높은 히트율(HR@5: 48.2% for PDF, 50.6% for LaTeX)을 달성하면서도 적정한 비용 수준 유지
2. **형식 저항성 차이**: Gemini 모델은 LaTeX 형식으로 전환 시 성능 저하(39.2% → 36.3%)를 보였으나, OpenAI o-시리즈 모델은 안정적(48.2% → 50.6%)
3. **Claude 3.7 Sonnet의 한계**: PDF 접근 방식에서 64.9%의 논문에서 문제를 발견하지 못하는 낮은 성능(HR@5: 11.0%)
4. **포괄적 평가 프레임워크**: 도메인 전문가 모집의 어려움을 극복하기 위해 여러 LLM 판정자를 활용한 자동 평가 방식 제시

## How

**데이터셋 구축:**
- WithdrawArxiv 데이터셋(2024년 9월까지 철회된 논문)의 6,018개 "중대한 사실적/방법론적 오류" 사례에서 시작
- Gemini 2.5 Flash를 이용한 1차 필터링(2,190건)과 수동 검토(1,225건) 수행
- 최종 테스트셋: 245건(20%), 훈련/검증셋: 980건(80%)
- 수학 50%, 물리학 26%, 컴퓨터과학 20% 분포

**평가 방법론:**
- **3가지 접근 방식**: (1) PDF 첨부, (2) OCR 결과를 프롬프트에 포함, (3) LaTeX 스크립트 포함
- **자동 평가 파이프라인**: 2개의 LLM 판정자(Gemini 2.5 Pro, o3)가 독립적으로 식별된 문제가 저자의 오류 설명과 정확히 일치하는지 평가
- **메트릭**: Hit Rate at k (HR@k), Mean Average Precision (MAP@k), 정밀도(Precision)

**실험 설정:**
- k=5(보고 가능한 최대 문제 개수), nc=nj=1, m=2
- 5개 추론형 LLM 테스트: Gemini 2.5 Pro/Flash, o3, o4-mini, Claude 3.7 Sonnet

## Originality

- **새로운 프레임 재정의**: 동료 심사에서 LLM의 역할을 "경쟁자"에서 "보조 도구"로 전환하는 개념 제시
- **자동 평가 방법론**: 도메인 전문가 없이 LLM 판정자를 활용한 확장 가능한 평가 프레임워크 개발
- **실제 철회 데이터**: 가정이 아닌 실제 철회 논문(1,225건)을 활용한 실증적 평가 수행
- **비용 효율성 분석**: 토큰 사용량과 API 비용을 체계적으로 보고하여 실제 배포 가능성 평가
- **공개 자료 제공**: 데이터셋, 코드, 모델 출력물을 공개하여 재현성 및 후속 연구 촉진

## Limitation & Further Study

- **LLM 판정자의 한계**: 최종 판정이 LLM의 정확성에 의존하므로 "금표준(gold standard)"이 없음. Claude 3.7 Sonnet이 판정자로 부적격 판정된 점은 판정자 선정의 불확실성 시사
- **형식 제약**: LaTeX 접근 방식에서 이미지 무시, PDF 전처리 파이프라인의 벤더별 차이로 인한 공정한 비교 어려움
- **제한된 프롬프트**: 수학 및 물리학 논문이 풍부한 데이터셋에도 불구하고 일반적이고 간단한 지시문(generic task instruction)만 사용
- **도메인별 일반화**: 수학, 물리학, 컴퓨터과학 중심으로 의학, 생물학 등 다른 분야의 성능 미검증
- **후속 연구 방향**:
  - OCR 기반 접근 방식의 체계적 평가
  - 도메인 전문가 수동 평가를 통한 자동 평가 방식 검증
  - 특화된 프롬프트 엔지니어링으로 성능 개선
  - 다중 모달 논문(이미지, 표 등) 처리 능력 강화
  - 더 큰 규모의 실제 검증 연구(기저 사항: 현재 nc=1로 단일 실행만 수행)

## Evaluation

- **Novelty (독창성)**: 4/5 - LLM 역할의 개념적 재정의와 자동 평가 프레임워크는 새로우나, 기본 기술(LLM-as-judge)은 기존 아이디어 활용
- **Technical Soundness (기술적 건전성)**: 3.5/5 - 방법론 자체는 합리적이나, 데이터셋 필터링 과정에서 LLM 사용(잠재적 순환성), 판정자 자격 판정 기준 모호
- **Significance (중요성)**: 4/5 - 동료 심사 위기 해결에 실질적 기여 가능성 높음. 공개 데이터셋과 프레임워크는 향후 연구의 기초 제공
- **Clarity (명확성)**: 4/5 - 전체적으로 명확하게 제시되나, 판정자 선정 과정(Claude 제외 이유)과 일부 설계 결정 사항의 상세 설명 부족
- **Overall**: 4/5

**총평**: 본 논문은 LLM을 동료 심사 보조 도구로 위치지어 책임감 있는 활용을 추구하며, 실제 철회 데이터를 바탕으로 한 실증적 평가와 자동 평가 프레임워크를 제시하여 학술 출판 시스템의 개선에 유의미한 기여를 합니다. 다만 자동 평가 방식의 검증과 도메인 별 일반화 측면에서 추가 연구가 필요합니다.

## Related Papers

- 🏛 기반 연구: [[papers/678_ReviewerGPT_An_Exploratory_Study_on_Using_Large_Language_Mod/review]] — LLM의 일반적 논문 심사 능력 탐색이 비판적 문제 검출이라는 특화된 심사 업무 수행 가능성 평가의 기초가 된다.
- 🔄 다른 접근: [[papers/881_When_ai_co-scientists_fail_Spot-a_benchmark_for_automated_ve/review]] — 철회된 논문 데이터와 검증된 오류 데이터를 활용한 두 연구 모두 과학적 오류 검출 능력을 평가하지만 서로 다른 데이터셋과 접근법을 사용한다.
- 🔗 후속 연구: [[papers/692_Safescientist_Toward_risk-aware_scientific_discoveries_by_ll/review]] — 안전한 과학적 발견을 위한 위험 인식 시스템으로 확장하여 오류 검출을 넘어 예방적 안전 조치까지 포함한다.
- 🔗 후속 연구: [[papers/678_ReviewerGPT_An_Exploratory_Study_on_Using_Large_Language_Mod/review]] — LLM의 논문 심사 가능성 탐색을 비판적 문제 검출이라는 특화된 영역으로 확장하여 더 구체적인 적용 방안을 제시한다.
- 🔄 다른 접근: [[papers/881_When_ai_co-scientists_fail_Spot-a_benchmark_for_automated_ve/review]] — 과학 논문 오류 자동 검증에서 서로 다른 데이터셋과 평가 방법을 사용하여 LLM의 학술 검증 능력을 다각도로 평가한다.
