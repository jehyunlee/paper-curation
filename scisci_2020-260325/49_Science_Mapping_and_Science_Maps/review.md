# Science Mapping and Science Maps

> **저자**: Eugenio Petrovich | **날짜**: 2021 | **Journal**: Knowledge Organization | **DOI**: 10.5771/0943-7444-2021-7-8-535

---

## Essence

Science mapping의 개념적, 이론적, 방법론적 쟁점을 포괄적으로 정리한 백과사전적 리뷰 논문이다. Citation-based map(direct citation, bibliographic coupling, co-citation), term-based map(co-word analysis, NLP 기반), co-authorship network, interlocking editorship network, patent map, geographic map 등 주요 유형을 체계적으로 분류하고, 데이터 수집부터 전처리, 네트워크 추출, 정규화, 시각화(graph-based vs. distance-based), enrichment(clustering, overlay), 해석에 이르는 7단계 워크플로우를 제시한다. 또한 science map의 객관성, 출판된 과학 vs. 실행 중인 과학, 인용의 의미 등 인식론적 쟁점까지 논의한다.

## Motivation

- **기존 지식**: Science mapping은 1960년대 SCI 창설 이후 co-citation(Small 1973), bibliographic coupling(Kessler 1963), co-word analysis(Callon et al. 1983) 등 다양한 기법이 발전해왔고, CiteSpace, VOSviewer 등 도구가 보급되면서 "Cambrian explosion of science maps"(Borner et al. 2015)라 불리는 폭발적 성장기에 진입했다.
- **한계/격차**: Science mapping 방법론이 여러 학문(scientometrics, 정보과학, 데이터 과학, 과학사회학)에 걸쳐 분산되어 있어, 비전문가가 개념적/이론적 기반을 이해하기 어려웠다. 특히 수학적 공식화에 치중한 기존 문헌은 방법론 선택의 의미와 한계를 충분히 설명하지 못했다.
- **접근**: 수학적 공식화보다 **개념적, 이론적, 방법론적 이슈**에 초점을 맞춰, 연구자와 정책결정자 모두가 science map을 이해하고 독립적으로 평가할 수 있도록 체계적 입문서를 제공한다.

## Achievement

1. **7단계 표준 워크플로우 체계화**: 데이터 수집 → 전처리 → 네트워크 추출 → 정규화 → 시각화 → enrichment → 해석의 단계를 명확히 구조화
2. **Science map 유형의 포괄적 분류**: Citation-based(direct linkage, bibliographic coupling, co-citation), term-based(classic co-word, NLP-based), co-authorship, interlocking editorship, patent-based, geographic map 6개 유형을 체계적으로 정리
3. **정규화 문제의 명확한 설명**: 단위 크기 차이에 의한 왜곡 문제를 직관적으로 설명하고, local(cosine, association strength, Jaccard) vs. global(Pearson's r, Chi-squared) 접근의 차이를 정리
4. **시각화 아티팩트 경고**: MDS의 차원 축소 과정에서 발생하는 시각적 아티팩트(quasi-circular layout, 숨겨진 차원의 "터널" 효과)를 구체적으로 경고
5. **인식론적 논의**: Science map의 객관성(mechanical objectivity vs. bottom-up objectivity), 출판된 과학의 한계, 인용의 의미(normative vs. socio-constructivist theory)에 대한 심층 논의

## How

- **데이터**: 156편의 참고문헌을 기반으로 한 narrative review
- **방법**: ISKO Encyclopedia of Knowledge Organization 항목으로 기획된 개념적 리뷰. Science mapping의 역사(중세 지식의 나무 → SCI → 현대 도구), 데이터 소스(WoS, Scopus, Google Scholar, Dimensions, OpenAlex), field delineation 전략(기존 분류 활용, ad hoc 검색, 네트워크 기반 클러스터링), 각 map 유형의 구축 원리와 해석 방법을 체계적으로 서술

## Originality

- Science mapping의 **방법론적 선택지**를 중립적 입장에서 체계적으로 정리한 점이 독창적. 특정 기법의 우위를 주장하기보다 각 접근의 rationale, 장단점, 해석 시 주의사항을 균형 있게 제시
- Knowledge Organization 관점에서 science map의 위치를 명확히 규정: 기존 KOS(taxonomies, ontologies)를 대체하는 것이 아니라 **보완**하는 도구로 위치 설정
- 과학철학/과학사회학적 쟁점(객관성, science-in-action, citation theory)을 science mapping 맥락에 통합하여 해석의 깊이를 더함

## Limitation & Further Study

### 저자들이 언급한 한계
- 과학은 끊임없이 진화하는 분야이므로 본 리뷰도 시간이 지나면 갱신이 필요
- 인문학에서의 science mapping 적용은 인용 관행, 출판 유형, 데이터베이스 커버리지 차이로 인해 제한적
- 정규화 방법에 대한 합의가 35년 이상 지속된 논쟁임에도 결론에 도달하지 못함

### 리뷰어 판단 아쉬운 점
- **최신 방법론 미반영**: 2021년 출판이지만 embedding 기반 접근(BERT, Doc2Vec 등), deep learning 기반 과학 분석, OpenAlex 등 최근 오픈 데이터 소스의 발전이 거의 다루어지지 않음
- **실증적 비교 부재**: 각 방법론의 장단점을 개념적으로만 서술하고, 동일 데이터셋에 대한 다양한 접근의 실증적 비교 결과는 제시하지 않음
- **소프트웨어 도구 리뷰의 제한성**: CiteSpace와 VOSviewer만 부록에서 다루고, Gephi, Bibliometrix, SciMAT, CitNetExplorer 등 다른 주요 도구에 대한 논의가 부족
- **동적/시계열 분석의 얕은 다룸**: Temporal mapping 방법(longitudinal, historiograph, alluvial)을 소개만 하고 각 접근의 비교 분석이 부족

### 후속 연구
- Embedding 기반 topic modeling(BERTopic 등)과 기존 co-word analysis의 체계적 비교
- 오픈 bibliometric 데이터(OpenAlex, Semantic Scholar)가 science mapping 결과에 미치는 영향 평가
- AI/LLM을 활용한 클러스터 해석 자동화 방법론 개발
- 인문학/사회과학 분야에 맞춤화된 science mapping 프레임워크 구축

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 3/5 |
| Technical Soundness | 4/5 |
| Significance | 4/5 |
| Clarity | 5/5 |
| Overall | 4/5 |

**총평**: Science mapping 분야의 개념적, 방법론적 지형을 비전문가도 이해할 수 있도록 명쾌하게 정리한 우수한 입문서로, 인식론적 논의까지 포함하여 깊이가 있으나, embedding/deep learning 등 최신 방법론의 부재가 아쉽다.
