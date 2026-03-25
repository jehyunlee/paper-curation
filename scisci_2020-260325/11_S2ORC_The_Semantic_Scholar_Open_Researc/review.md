# S2ORC: The Semantic Scholar Open Research Corpus

> **저자**: Kyle Lo, Lucy Lu Wang, Mark Neumann, Rodney Kinney, Daniel S. Weld | **날짜**: 2020 | **Journal**: Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics (ACL 2020) | **DOI**: 10.18653/v1/2020.acl-main.447

---

## Essence

S2ORC는 81.1M개의 영어 학술 논문으로 구성된 대규모 공개 연구 코퍼스로, 8.1M개 오픈액세스 논문의 구조화된 전문(full text), 73.4M개 논문의 초록, 380.5M개의 해결된 인용 링크를 포함하며, 수십 개 학문 분야를 아우르는 당시 최대 규모의 공개 기계판독 가능 학술 텍스트 컬렉션이다.

## Motivation

학술 논문에 대한 NLP 연구를 위해 인용 그래프(MAG, Semantic Scholar)와 텍스트 코퍼스(arXiv, PubMed Central, ACL Anthology) 등 다양한 자원이 존재했으나, 기존 코퍼스들은 규모가 작거나(AAN: 25k편), 특정 도메인에 한정되거나(PubMed: 생의학), 사용 가능한 전문을 제공하지 못하는(RefSeer: snippet만 제공) 한계가 있었다. 인용 문맥(citation context)과 논문 메타데이터를 결합한 bibliometric-enhanced 코퍼스가 필요했으나, 다학문 분야를 포괄하면서 대규모 전문 텍스트와 인용 링크를 함께 제공하는 자원은 부재했다. 이에 Semantic Scholar의 문헌 그래프를 기반으로 수백 개 출판사와 디지털 아카이브의 논문을 통합하여 S2ORC를 구축하였다.

## Achievement

1. **규모**: 81.1M개 논문, 8.1M개 GROBID 전문 파싱, 1.5M개 LaTeX 전문 파싱으로 PubMed Central OA(2.6M)의 3배 이상 전문 텍스트를 확보하였다.
2. **인용 링크**: 380.5M개의 논문 간 인용 링크를 해결하였으며, 이 중 156.5M개는 전문 내 인라인 인용 멘션에 연결된다.
3. **메타데이터 품질**: 논문 클러스터링 정확도 title 0.93 / authors 0.89, 참고문헌 링킹 정확도 title 1.00 / authors 0.92-0.96을 달성하였다.
4. **S2ORC-SciBERT 사전학습**: S2ORC 전문(16.4B 토큰)으로 학습한 BERT 모델이 SciBERT와 동등하거나 우수한 성능을 12개 과학 NLP 태스크에서 보여주었다(예: ChemProt REL 84.59 vs 83.64, SciERC REL 81.77 vs 79.97).
5. **COVID-19 대응**: S2ORC 파이프라인이 CORD-19 코퍼스 구축에 직접 활용되어 75K+ 다운로드, 수십 개 검색/QA 시스템에 사용되었다.

## How

- **데이터 소스**: Semantic Scholar 문헌 코퍼스(약 200M 논문 클러스터)에서 출발
- **PDF 처리**: ScienceParse v3.0.0(제목/저자 추출)과 GROBID v0.5.5(구조화된 전문, 인라인 인용, 참고문헌 추출)로 30.5M PDF를 처리
- **LaTeX 처리**: arXiv LaTeX 소스를 XML로 변환 후 구조 정보 추출(1.5M편)
- **메타데이터 선택**: 출판사 제공 메타데이터 우선, 다수결 투표로 canonical 메타데이터 결정
- **필터링**: 제목/저자 없음, 100자 미만 텍스트, 비영어 논문 제거(95.5M 클러스터 제외)
- **참고문헌 링킹**: 제목의 character 3-gram 기반 Jaccard+Containment 유사도(임계값 0.8)로 논문 매칭
- **오픈액세스 판별**: arXiv, ACL Anthology, PubMed Central OA, Unpaywall DB 활용

## Originality

- 다학문 분야를 포괄하는 최대 규모의 공개 구조화 학술 전문 코퍼스를 최초로 구축하였다.
- 인라인 인용뿐 아니라 그림/표/수식 참조까지 자동 감지하여 논문 객체에 연결하는 구조화된 어노테이션을 제공한다.
- PDF 파싱과 LaTeX 파싱을 결합하여 서로 다른 소스의 장점을 취하는 하이브리드 파이프라인을 설계하였다.
- 단일 통합 코퍼스에서 메타데이터, 전문, 인용 그래프를 모두 제공하여 bibliometric 분석과 NLP 태스크를 동시에 지원한다.

## Limitation & Further Study

### 저자들이 언급한 한계
- 95.5M 논문 클러스터가 필터링으로 제거되었으며, 그 중 80.0M개는 초록이나 PDF가 없는 저품질 클러스터이다.
- LaTeX 메타데이터 품질이 PDF 추출보다 낮아 메타데이터 선택에 사용하지 못한다.
- 물리학/수학 분야의 참고문헌에 제목이 없는 경우 링킹 알고리즘이 실패한다(LaTeX 링킹률 6.8 vs GROBID 19.3).
- 영어 논문만 포함하여 비영어권 학술 문헌이 제외된다.

### 리뷰어 판단 아쉬운 점
- GROBID에 크게 의존하는 파이프라인으로, GROBID의 인용 감지 F1 0.89는 완벽하지 않으며 오류가 코퍼스 전체에 전파될 수 있다.
- 논문 클러스터링이 제목 유사도와 DOI 겹침에 기반하여, 제목이 유사하지만 다른 논문이 잘못 병합되거나 동일 논문이 분리될 가능성이 있다.
- 오픈액세스 전문은 전체의 10%(8.1M/81.1M)에 불과하여, 대부분의 논문은 초록만 이용 가능하다.
- 학문 분야 분류가 Microsoft Academic에 의존하여 미분류(Unclassified) 논문이 상당수 존재한다.

### 후속 연구
- 다국어 학술 코퍼스로의 확장 및 비영어 논문 파싱 품질 개선
- 딥러닝 기반 PDF 파싱 도구(예: VILA, Nougat)를 활용한 전문 추출 품질 향상
- 시간에 따른 코퍼스 업데이트 자동화 파이프라인 구축
- 논문 간 의미적 관계(지지/반박/확장 등) 자동 분류 연구

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 4/5 |
| Technical Soundness | 4/5 |
| Significance | 5/5 |
| Clarity | 4/5 |
| Overall | 4/5 |

**총평**: 학술 텍스트 마이닝의 기반 인프라로서 탁월한 기여를 한 자원 논문으로, 81.1M 논문의 통합과 구조화된 전문 제공은 science of science 및 NLP 연구에 광범위한 영향을 미쳤으며, CORD-19 등 후속 프로젝트를 통해 실질적 사회적 임팩트를 입증하였다.
