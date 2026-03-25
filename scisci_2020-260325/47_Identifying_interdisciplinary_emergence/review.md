# Identifying interdisciplinary emergence in the science of science: combination of network analysis and BERTopic

> **저자**: Keungoui Kim, Dieter F. Kogler, Sira Maliphol | **날짜**: 2024-05-10 | **Journal**: Humanities and Social Sciences Communications | **DOI**: 10.1057/s41599-024-03044-y

---

## Essence

네트워크 분석(Eigenvector centrality)과 BERTopic을 결합하여 글로벌 학제간 과학의 emergence를 식별하는 새로운 방법론을 제시한다. Web of Science 메타데이터 약 745만 건(2012-2017) 중 학제간 논문 119만여 건을 분석한 결과, dominant science와 growing science가 명확히 구분되며, growing-science의 Eigenvector centrality는 다음 기간에 평균 0.348로 기타(0.093) 대비 약 3.7배 높은 값을 보여, 성장하는 학제간 분야가 실제로 영향력이 커짐을 확인했다. 주요 emerging topic으로 green technology와 health-related technology가 전 학제간 카테고리에서 공통적으로 나타났다.

## Motivation

- **기존 지식**: Science map과 bibliometric 분석은 과학 emergence를 탐지하는 데 널리 사용되어 왔으며, 빈도 기반 topic modeling(LDA 등)이 주요 도구였다.
- **한계/격차**: 기존 연구는 (1) 특정 저널/분야에 한정된 local map에 집중하여 글로벌 맥락을 놓치고, (2) 빈도 기반 방법은 canonical bias에 취약하며 문맥을 무시하고, (3) 사전 정의된 주제 범위 내에서만 emergence를 탐지해 학제간 경계 변화를 포착하지 못했다.
- **접근**: Schumpeterian knowledge recombination 관점에서 WoS 과학 카테고리 간 co-occurrence network를 구축하고, Eigenvector centrality의 성장률로 emerging field를 정의한 뒤, BERTopic(BERT embedding + UMAP + HDBSCAN + c-TF-IDF)으로 해당 분야의 latent topic을 비지도 학습으로 추출한다.

## Achievement

1. **글로벌 학제간 과학 지도 구축**: LSB-TE, LSB-PS, PS-TE, LSB-PS-TE 4개 학제간 분야에서 172개 subject, 1,137개 저널, 119만여 편의 네트워크를 생성
2. **Dominant vs. Growing science의 명확한 구분**: EIG 상위 10%와 EIG 성장률 상위 10%로 분류한 결과, 두 그룹이 거의 겹치지 않으며 growing-science가 다음 기간에 실제 영향력 증가 확인(평균 EIG 0.348 vs. 0.093)
3. **BERTopic 기반 emerging topic 식별**: 4개 학제간 분야에서 총 11개 주요 토픽 도출 (예: PS-TE의 수처리용 흡착/멤브레인, LSB-TE의 천연섬유 재료 등)
4. **Green & health technology의 범분야적 emergence 발견**: "Green & Sustainable Science & Technology"가 dominant과 growing 양쪽에 동시 출현하여 사회적 영향력이 큰 분야로 확인
5. **질적 검증(qualitative validation)**: 대표 논문 분석을 통해 BERTopic 결과가 비전문가에게도 해석 가능한 수준임을 확인

## How

- **데이터**: Web of Science Core Collection, 2012-2017년 STEM 분야 journal article, 약 745만 건 중 학제간(2개 이상 subheading) 119만 건 필터링
- **방법**:
  - Stage 1: 과학 카테고리-주제 co-occurrence network 구축 → Eigenvector centrality(EIG) 측정 → EIG 및 EIG 성장률 상위 10%로 dominant/growing science 분류
  - Stage 2: Growing science 논문 필터링 → BERTopic 적용 (all-MiniLM-L6-v2 embedding, UMAP 차원 축소, HDBSCAN 클러스터링, c-TF-IDF 토픽 생성)
  - Hyperparameter 최적화: n-gram range, topic 수, minimum topic size를 random search로 탐색, information entropy 최소화 기준
  - 질적 검증: 토픽별 대표 논문 3편씩 수작업 분석

## Originality

- Eigenvector centrality를 학제간 emergence의 **영향력 지표**로 사용한 최초 시도로, 기존 빈도/다양성 기반(Rao-Stirling diversity 등) 접근과 차별화
- BERTopic을 글로벌 학제간 과학 데이터셋에 적용한 초기 사례로, embedding 기반 topic modeling이 문맥 정보를 보존하면서 대규모 bibliometric 분석에 유효함을 입증
- Dominant science와 growing science를 개념적으로 분리하여, 이미 확립된 분야 vs. 미래 영향력이 커질 분야를 구분하는 프레임워크 제시

## Limitation & Further Study

### 저자들이 언급한 한계
- 자동 생성된 토픽 수가 적어 추가 emerging topic이 존재할 가능성
- WoS journal article에 한정되어 사회 혁신이나 비STEM 분야의 학제간성 미반영
- NLP 접근에 상당한 연산 자원 필요, 일상적 정책 활용에 장벽
- San Francisco Declaration on Research Assessment 관점에서 보다 광범위한 impact 측정 필요

### 리뷰어 판단 아쉬운 점
- **EIG 상위 10% 임계값의 자의성**: 임계값 변경에 따른 결과 민감도 분석(sensitivity analysis)이 부재하여, 10%라는 기준의 robustness가 검증되지 않음
- **시간 해상도 한계**: 3년 단위 2개 기간(2012-2014, 2015-2017)만 비교하여 emergence의 동적 궤적 추적이 어렵고, 일시적 변동 vs. 지속적 성장 구분 불가
- **인과적 설명 부재**: Growing science가 '왜' 성장하는지에 대한 분석 없이 네트워크 구조 변화만 기술
- **BERTopic 토픽 수 제한**: LSB-PS-TE의 경우 904편으로 2개 토픽만 도출되어 해석의 세밀함이 부족
- **비교 대상 부재**: LDA 등 기존 topic modeling과의 체계적 비교 실험이 없어 BERTopic의 상대적 우위를 정량적으로 평가하기 어려움

### 후속 연구
- 시계열 확장을 통한 Dynamic BERTopic 적용으로 토픽 진화 궤적 추적
- Recursive clustering을 활용한 다단계 토픽 세분화
- 인용 네트워크와 결합하여 emerging topic의 실제 scientific impact 측정
- 사회과학/인문학 포함 전 학문 분야로 확장

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 4/5 |
| Technical Soundness | 3/5 |
| Significance | 3/5 |
| Clarity | 3/5 |
| Overall | 3/5 |

**총평**: 네트워크 중심성과 BERTopic을 결합하여 글로벌 학제간 emergence를 탐지하는 독창적 프레임워크를 제시했으나, 임계값 민감도 분석 부재, 제한된 시간 범위, 기존 방법론과의 비교 실험 결여로 방법론적 엄밀성이 다소 부족하다.
