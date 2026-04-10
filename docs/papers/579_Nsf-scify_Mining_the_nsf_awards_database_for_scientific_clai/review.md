---
title: "579_Nsf-scify_Mining_the_nsf_awards_database_for_scientific_clai"
authors:
  - "D. Rao"
  - "Weiqiu You"
  - "Eric Wong"
  - "Chris Callison-Burch"
date: "2025"
doi: "N/A"
arxiv: ""
score: 4.2
essence: "NSF(미국 국립과학재단) 지원금 데이터베이스에서 과학적 주장(scientific claims)과 연구 제안(investigation proposals)을 대규모로 추출한 데이터셋 NSF-SCIFY를 제시한다. 1970년부터 2024년까지 50년간 400K개 이상의 지원금 초록에서 추정 280만 개의 과학적 주장을 추출하여 현재까지 가장 큰 규모의 과학적 주장 데이터셋을 구축했다."
tags:
  - "cat/LLM-Based_Scientific_Reasoning"
  - "sub/Scientific_Literature_Analysis"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Rao et al._2025_Nsf-scify Mining the nsf awards database for scientific claims.pdf"
---

# NSF-SCIFY: Mining the NSF Awards Database for Scientific Claims

> **저자**: D. Rao, Weiqiu You, Eric Wong, Chris Callison-Burch | **날짜**: 2025 | **DOI**: N/A

---

## Essence

![Figure 2](figures/fig2.webp)
*NSF 주요 지원 분야별 분포: 재료과학(3.9%), 수학물리과학(16.5%), 지구과학(13.8%) 등*

NSF(미국 국립과학재단) 지원금 데이터베이스에서 과학적 주장(scientific claims)과 연구 제안(investigation proposals)을 대규모로 추출한 데이터셋 NSF-SCIFY를 제시한다. 1970년부터 2024년까지 50년간 400K개 이상의 지원금 초록에서 추정 280만 개의 과학적 주장을 추출하여 현재까지 가장 큰 규모의 과학적 주장 데이터셋을 구축했다.

## Motivation

- **Known**: 기존 과학적 주장 검증 연구(SciFACT, PubHEALTH 등)는 출판된 학술 논문, 팩트체크 사이트, 뉴스 기사 등을 주요 출처로 활용했으며, 최대 수천 개 수준의 소규모 데이터셋에 불과함

- **Gap**: 과학 출판물의 연 4% 성장률에 따라 검증되지 않은 주장들이 증가하고 있으나, 기존 데이터셋은 규모가 작고 도메인이 제한적이며, 지원금 제안서라는 새로운 출처는 전혀 활용되지 않음

- **Why**: NSF는 미국 연방 기초 연구의 약 25%를 지원하며, 지원금 초록은 (1) 엄격한 전문가 심사를 거친 고품질 필터, (2) 출판 전 초기 단계의 주장 포착, (3) 공개적이고 재사용 가능한 자료, (4) 과학적 실천과 연구 진화 추적의 독특한 기회 제공

- **Approach**: Claude-3.5를 이용한 제로샷 프롬팅으로 검증 가능한 주장과 전향적 연구 제안을 구분하여 추출하는 방법 개발

## Achievement

![Figure 3](figures/fig3.webp)
*기술 초록과 비기술 초록의 t-SNE 임베딩 비교: STEL 스타일 임베딩으로 명확한 분리 관찰*

1. **대규모 데이터셋 구축**: NSF-SCIFY-MATSCI에서 재료과학 분야 16K개 초록으로부터 114K개 과학적 주장과 145K개 연구 제안 추출 (기존 최대 데이터셋 대비 10배 이상 규모)

2. **높은 자동 추출 성능**: 미세조정된 모델이 기본 모델 대비 100% 상대 개선율 달성, 조사 제안 추출에서 90% 이상 개선 달성

3. **기술-비기술 초록 생성**: BERTScore 0.85+ F1 달성, 기술 초록과 비기술 초록의 대칭 BLEU 유사도 1.5%로 실질적 재작성 확인

4. **LLM 기반 평가 메트릭 개발**: 클레임/제안 추출 품질 평가를 위한 새로운 평가 지표 제시

5. **공개 제공**: 모든 데이터셋, 학습된 모델, 평가 코드를 공개 배포

## How

- **데이터 수집**: NSF 지원금 데이터베이스(1970-2024)에서 412,155개의 파싱 가능한 지원금 레코드 획득

- **데이터 처리**: 각 레코드당 지원금 ID·제목·연도, 국/부서 정보, 기술/비기술 초록, 추출된 주장/제안, 관련 출판물(2014년 이후) 포함

- **클레임 및 제안 추출**: 
  - Anthropic Claude-3.5 모델 활용
  - 온도 0으로 설정하여 일관성 유지
  - 검증 가능한 주장(verifiable claims)과 전향적 연구 제안(investigation proposals) 동시 추출
  - 조인트 추출 방식으로 전향적 주장을 사실적 주장으로 오분류하는 문제 해결

- **프롬프트 설계**: JSON 객체 반환 구조로 지원금 ID, 기술/비기술 초록, 주장 리스트, 제안 리스트 포함

## Originality

- **새로운 데이터 출처**: 지원금 제안서(grant proposals)를 과학적 주장 추출의 최초 사용 출처로 확립 (기존: 논문, 뉴스, SNS)

- **새로운 과제 정의**: 기존 사실적 주장(factual claims)에 더해 미래 지향적 연구 의도(aspirational research intentions) 구분 추출 개발

- **초대규모 데이터셋**: 기존 최대 5K개 문서 대비 NSF-SCIFY-MATSCI만 16K개 문서, 전체 NSF-SCIFY는 400K개 문서 규모

- **메타과학 가능성**: 지원금 주장과 실제 조사 제안 간의 관계 연구로 과학적 실천과 연구 진화 추적 가능

- **학제간 범위**: 모든 STEM 분야 포함으로 기존 생의학 중심 데이터셋의 한계 극복

## Limitation & Further Study

- **추정 규모**: 전체 NSF-SCIFY의 280만 개 주장은 추정값이며, 대규모 처리 완료 시 정확 수치 업데이트 필요

- **부분 초록**: 비기술 초록이 약 19%의 지원금에서 부재하여 데이터 불완전성 존재

- **출판 연결 제한**: 출판물 연결이 2014년 이후만 가능하여 역사적 영향 추적 어려움

- **단일 LLM 사용**: 클로드 3.5만 사용하여 모델 간 추출 일관성 검증 부재

- **후속 연구 기회**:
  - 전체 NSF-SCIFY 대상 포괄적 처리
  - 주장과 실제 연구 결과 간 추적 가능성 분석
  - 다양한 LLM 모델 간 추출 결과 비교
  - 클레임 검증(claim verification) 모델 개발
  - 시간에 따른 과학적 주장 진화 추적

## Evaluation

- **Novelty**: 4.5/5 - 지원금 제안서라는 새로운 출처 활용, 주장/제안 구분 개발이 혁신적이나, 추출 방법은 기존 LLM 프롬팅 활용

- **Technical Soundness**: 4/5 - 제로샷 프롬팅과 미세조정 파이프라인이 견고하나, 출력 검증 및 품질 관리 상세가 부족, LLM 기반 평가 메트릭의 신뢰성 근거 필요

- **Significance**: 4.5/5 - 기존 대비 10배 이상 규모의 데이터셋 제공으로 높은 실질적 가치, 메타과학 및 과학정책 연구에 새로운 가능성 제시

- **Clarity**: 3.5/5 - 전반적 구성은 명확하나, 클레임 추출 품질 평가 세부사항, LLM 평가 메트릭 구체적 방법론 설명 부족, 일부 통계 제시 미흡

- **Overall**: 4.2/5

**총평**: NSF-SCIFY는 지원금 제안서라는 새로운 출처로부터 규모 면에서 획기적인 과학적 주장 데이터셋을 구축했으며, 주장과 연구 제안의 구분 추출이라는 새로운 과제를 정의함으로써 과학 검증 및 메타과학 연구에 중요한 자산을 제공한다. 다만 LLM 기반 추출과 평가의 신뢰성 검증이 더욱 강화될 필요가 있다.

## Related Papers

- 🔗 후속 연구: [[papers/600_Paper2Web_Lets_Make_Your_Paper_Alive/review]] — 과학적 주장 데이터셋을 활용한 논문의 멀티미디어 변환 및 상호작용화
- 🏛 기반 연구: [[papers/500_Llm-based_corroborating_and_refuting_evidence_retrieval_for/review]] — 대규모 과학적 주장 데이터셋이 주장 검증 시스템의 핵심 데이터 기반
- 🧪 응용 사례: [[papers/540_Mir_Methodology_inspiration_retrieval_for_scientific_researc/review]] — NSF 데이터베이스의 방법론적 계보를 연구 문제 해결에 활용한 응용 사례
- 🔗 후속 연구: [[papers/710_Sciclaimhunt_A_large_dataset_for_evidence-based_scientific_c/review]] — NSF 데이터를 확장하여 증거 기반 과학적 주장 탐지 시스템으로 발전
- 🏛 기반 연구: [[papers/600_Paper2Web_Lets_Make_Your_Paper_Alive/review]] — 대규모 과학적 주장 데이터셋이 논문 웹사이트 변환의 콘텐츠 기반 제공
- 🔗 후속 연구: [[papers/500_Llm-based_corroborating_and_refuting_evidence_retrieval_for/review]] — NSF 과학적 주장 데이터셋을 활용한 증거 검색 및 검증 시스템
- 🏛 기반 연구: [[papers/540_Mir_Methodology_inspiration_retrieval_for_scientific_researc/review]] — NSF 데이터베이스가 방법론적 영감 검색의 과학 연구 데이터 기반
