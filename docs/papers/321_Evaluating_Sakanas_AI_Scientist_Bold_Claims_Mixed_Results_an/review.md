---
title: "321_Evaluating_Sakanas_AI_Scientist_Bold_Claims_Mixed_Results_an"
authors:
  - "Joeran Beel"
  - "Min-Yen Kan"
  - "Moritz Baumgart"
date: "2025"
doi: "N/A"
arxiv: ""
score: 4.0
essence: "Sakana.ai의 AI Scientist는 연구 전체 생명주기(아이디어 생성, 실험 설계 및 실행, 논문 작성, 피어 리뷰)를 자동화하겠다고 주장하는 시스템이지만, 본 논문의 체계적 평가 결과 문헌 검토, 실험 실행, 원고 작성 등 여러 영역에서 심각한 결함을 발견했다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/AI_Scientific_Discovery"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Genderen_2025_Evaluating sakana’s ai scientist for autonomous research Wishful thinking or an emerging reality to.pdf"
---

# Evaluating Sakana's AI Scientist for Autonomous Research: Wishful Thinking or an Emerging Reality Towards 'Artificial Research Intelligence'(ARI)? arXiv preprint arXiv:2502.14297, 2025.

> **저자**: Joeran Beel, Min-Yen Kan, Moritz Baumgart | **날짜**: 2025 | **DOI**: N/A

---

## Essence

Sakana.ai의 AI Scientist는 연구 전체 생명주기(아이디어 생성, 실험 설계 및 실행, 논문 작성, 피어 리뷰)를 자동화하겠다고 주장하는 시스템이지만, 본 논문의 체계적 평가 결과 문헌 검토, 실험 실행, 원고 작성 등 여러 영역에서 심각한 결함을 발견했다.

## Motivation

- **Known**: 최근 LLM 기반 AI 시스템들이 과학 발견을 지원하거나 자동화할 수 있다는 주장이 증가하고 있으며, Sakana.ai의 AI Scientist는 특히 "$15로 완전한 연구 논문 생성", "인간 개입 최소화" 등 대담한 주장으로 학계와 미디어에서 광범위한 관심을 받음.

- **Gap**: AI Scientist에 대한 대담한 주장에도 불구하고 직접 실험을 통한 독립적이고 체계적인 평가가 부재함. 대부분의 긍정적 평가는 Sakana의 공식 정보에만 의존하고 있음.

- **Why**: 인공 연구 지능(Artificial Research Intelligence, ARI)이 현실화되려면 이러한 시스템의 실제 능력과 한계를 정확히 파악해야 하며, 특히 정보검색(IR) 커뮤니티는 자동화된 연구가 자신들의 분야에 미칠 영향을 이해해야 함.

- **Approach**: AI Scientist를 직접 설치하고 운영하여 (1) 문헌 검토 프로세스, (2) 실험 실행의 견고성, (3) 생성된 원고의 질, (4) 비용-시간 효율성 등을 체계적으로 평가.

## Achievement

1. **문헌 검토의 근본적 결함**: AI Scientist는 단순 키워드 검색에만 의존하여 문헌을 표면적으로 검토하며, 마이크로-배칭(micro-batching for SGD) 같은 확립된 개념을 "새로운 아이디어"로 잘못 분류함.

2. **실험 실행의 불안정성**: 제안된 12개 실험 중 5개(42%)가 코딩 오류로 실패했으며, 실행된 실험들도 논리적 결함을 포함. 예를 들어 에너지 효율성 최적화 실험이 더 많은 계산 리소스를 소비하면서 정확도 개선을 보고하는 모순 발생.

3. **낮은 논문 품질**: 생성된 논문들의 중앙값 인용 수는 5개에 불과하고, 대부분 구식(2020년 이후는 34개 중 5개만), 구조적 오류(누락된 그림, 반복된 섹션, "Conclusions Here" 같은 플레이스홀더), 할루시네이션된 수치 결과 포함.

4. **제한된 적응성**: 반복 실험에서 코드는 평균 8% 정도만 증가하여 최소한의 개선 시도만 함.

5. **비용-시간 효율성의 현실화**: 완전한 연구 논문 생성에 $6-$15, 3.5시간의 인간 개입만 소요되어 기존 연구자 대비 현저히 빠르고 저렴함.

## How

- **실험 설정**: 제3저자(컴퓨터과학 3학년 학사, Python 숙련도 높음)가 소비자 노트북과 대학 컴퓨팅 클러스터에서 설치 및 실행 (설치 시간: ~5시간)
- **평가 항목**: 
  - 아이디어 생성의 참신성(novelty) 평가
  - 실험 코드 실행 성공률 및 결과 논리성 검증
  - 생성된 원고의 인용 품질, 구조적 정확성, 수치 결과 검증
  - 코드 수정 범위 분석
  - 원가 및 실행 시간 측정
- **재현성**: GitHub 저장소에 실험 코드베이스와 Singularity 컨테이너 정의 파일 제공

## Originality

- **처음의 체계적 독립 평가**: AI Scientist에 대한 최초의 직접 실험 기반 상세 평가로, 공식 주장과 실제 성능의 격차를 실증적으로 문서화함.

- **"Artificial Research Intelligence(ARI)" 개념 정의**: AI Scientist와 같은 자동화된 연구 시스템을 설명하는 새로운 용어 도입 (AGI보다는 낮지만 인간과 구분 불가능한 연구 능력).

- **다층적 평가 프레임워크**: 아이디어 생성, 실험 설계, 코드 실행, 결과 분석, 논문 작성, 피어 리뷰 등 연구 전체 생명주기에 걸친 평가로 각 단계의 구체적 문제점 도출.

- **학제간 관점**: IR 커뮤니티의 관점에서 자동화된 연구 시스템의 의미를 탐색하여, 문헌 검색, 인용 분석, 실험 설계 자동화 등 IR 핵심 분야와의 연관성을 강조.

## Limitation & Further Study

- **한계**:
  - 평가자가 학사 학생이어서, 전문 연구자의 관점에서의 평가는 제한적 (저자들은 이를 명시적으로 인정하며 "하한선"이라 표현)
  - 논문에서 제시된 구체적인 실패 사례와 출력 예시가 제한적으로 보임 (본문 15,000자 제한으로 전체 증거 제시 불가)
  - 다른 경쟁 도구(Google의 AI Co-Scientist 등)와의 비교 평가 부재

- **후속 연구**:
  - 파일럿 프로젝트와 ARI 벤치마크 경쟁 개발
  - 연구 로그(research logs) 및 마크업 언어를 통한 표준화된 AI 연구 속성 프레임워크 개발
  - 시간 경과에 따른 AI Scientist 성능 추적 연구
  - IR 커뮤니티 내에서 자동화된 연구 시스템의 거버넌스와 윤리적 함의에 대한 논의 시작

## Evaluation

- **Novelty (참신성)**: 4/5 — 최초의 체계적 독립 평가이지만, AI 시스템 비판적 분석이라는 주제 자체는 증가하는 추세
  
- **Technical Soundness (기술적 건전성)**: 4/5 — 실험 설계가 합리적이고 재현 가능하나, 평가자 수준 제한과 통계적 엄밀성 강화 여지

- **Significance (중요성)**: 5/5 — AI 드라이빈 연구 자동화라는 시의적절하고 중요한 주제이며, 학계·산업계 모두에 영향을 미칠 실질적 함의 제공

- **Clarity (명확성)**: 4/5 — 전체 구조와 주요 발견이 명확하나, 제한된 지면(본문 15,000자)으로 인해 일부 사례의 상세 설명 부족

- **Overall (종합)**: 4/5

**총평**: 본 논문은 과대 광고된 AI 시스템에 대한 첫 체계적 비판적 평가로서 학술 공동체에 중요한 현실 검증을 제공하며, 문헌 검토부터 실험 실행까지 구체적인 결함을 입증함으로써 ARI 기술의 현주소를 명확히 하고 향후 발전 방향을 제시한다는 점에서 매우 가치 있는 연구다.

## Related Papers

- ⚖️ 반론/비판: [[papers/795_The_AI_Scientist_Towards_Fully_Automated_Open-Ended_Scientif/review]] — AI Scientist의 심각한 결함 발견이 완전 자동화된 과학 발견의 한계를 지적
- 🔗 후속 연구: [[papers/828_Towards_end-to-end_automation_of_AI_research/review]] — AI 연구의 종단간 자동화에서 Sakana AI Scientist 평가로의 확장
- 🔄 다른 접근: [[papers/857_Unlocking_the_Potential_of_AI_Researchers_in_Scientific_Disc/review]] — 과학 발견에서 AI 연구자 잠재력과 AI Scientist 결함의 다른 평가 접근법
- 🏛 기반 연구: [[papers/881_When_ai_co-scientists_fail_Spot-a_benchmark_for_automated_ve/review]] — AI 공동과학자 실패 시 자동 검증 벤치마크가 평가의 기반 제공
- 🧪 응용 사례: [[papers/857_Unlocking_the_Potential_of_AI_Researchers_in_Scientific_Disc/review]] — 사카나 AI Scientist 평가 연구가 AI 연구자의 실제 과학 연구 능력을 검증한다.
- 🔗 후속 연구: [[papers/081_Ai_scientists_fail_without_strong_implementation_capability/review]] — AI Scientist 평가를 통해 자율 연구의 실제 한계를 구체적으로 분석한다
- 🔗 후속 연구: [[papers/795_The_AI_Scientist_Towards_Fully_Automated_Open-Ended_Scientif/review]] — AI Scientist의 실제 연구 수행 능력을 다양한 관점에서 평가한 확장 연구다
