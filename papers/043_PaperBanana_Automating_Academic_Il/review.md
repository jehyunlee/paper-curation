# PaperBanana: Automating Academic Illustration for AI Scientists

> **저자**: Dawei Zhu, Rui Meng, Yale Song, Xiyu Wei, Sujian Li, Tomas Pfister, Jinsung Yoon | **날짜**: 2026-01-30 | **Repository**: arXiv | **DOI**: 10.48550/arXiv.2601.23265

---

## Essence

PaperBanana는 학술 논문의 방법론 다이어그램과 통계 플롯을 자동 생성하는 에이전트 기반 프레임워크이다. Retriever, Planner, Stylist, Visualizer, Critic의 5개 특화 에이전트가 협업하여 참조 검색, 콘텐츠/스타일 계획, 이미지 렌더링, 반복적 자기 비평을 수행한다. NeurIPS 2025 논문에서 큐레이션한 PaperBananaBench(292 테스트 케이스)에서 faithfulness(+2.8%), conciseness(+37.2%), readability(+12.9%), aesthetics(+6.6%)로 기존 baseline을 일관되게 능가했다.

## Motivation

- **알려진 것**: LLM 기반 자율 AI 과학자(AI Scientist, Co-Scientist 등)가 문헌 리뷰, 아이디어 생성, 실험 반복을 자동화하고 있음
- **Gap**: 학술 논문의 시각적 커뮤니케이션, 특히 방법론 다이어그램 생성은 여전히 노동 집약적 병목으로 남아 있으며, 코드 기반 접근(TikZ, Python-PPTX)은 표현력 한계, 이미지 생성 모델은 학술 표준 미달
- **왜 중요한가**: 복잡한 기술 개념을 정확하고 미적으로 우수하게 시각화하는 것은 과학적 발견의 효과적 소통에 필수적이나, 전문 디자인 도구 숙련도가 요구되어 연구자에게 부담
- **접근법**: VLM과 이미지 생성 모델을 활용한 다중 에이전트 파이프라인으로, 참조 기반 학습과 반복적 자기 비평을 통해 출판 수준의 학술 일러스트 자동 생성

## Achievement

1. **전체 성능**: PaperBananaBench에서 Overall score 60.2% 달성 (Vanilla Nano-Banana-Pro 43.2%, Human 50.0% 대비)
2. **Conciseness 대폭 향상**: Vanilla 대비 +37.2%p로 가장 큰 개선 -- 에이전트 워크플로우가 핵심 정보 추출에 효과적임을 입증
3. **인간 평가 검증**: 50건 blind evaluation에서 PaperBanana 승률 72.7% / 무승부 20.7% / 패배 6.6%
4. **통계 플롯 확장**: 코드 기반 Visualizer로 전환하여 통계 플롯 생성에서도 인간 수준을 근접/초과 (Conciseness, Readability, Aesthetics에서 인간 상회)
5. **인간 다이어그램 개선**: 기존 인간 작성 다이어그램의 미적 품질 향상에서 56.2% 승률 달성
6. **벤치마크 구축**: NeurIPS 2025에서 큐레이션한 292개 테스트 + 292개 참조 세트의 PaperBananaBench 공개

## How

- **데이터**: NeurIPS 2025 논문 2,000편에서 MinerU 툴킷으로 방법론 섹션, 다이어그램, 캡션 추출. 종횡비 필터링(1.5~2.5) 후 인간 큐레이션을 거쳐 584개 샘플 확보, 292 테스트/292 참조로 분할
- **Retriever Agent**: VLM(Gemini-3-Pro)이 연구 도메인과 다이어그램 유형을 기준으로 참조 세트에서 가장 관련 높은 N개 예시를 생성적 검색(generative retrieval)
- **Planner Agent**: 소스 컨텍스트, 커뮤니케이티브 인텐트, 검색된 예시를 통한 in-context learning으로 상세한 텍스트 설명(P) 생성
- **Stylist Agent**: 전체 참조 컬렉션을 순회하여 색상, 레이아웃, 타이포그래피 등의 Aesthetic Guideline(G)을 자동 요약하고, 초기 설명을 스타일 최적화 버전(P*)으로 정제
- **Visualizer + Critic Loop**: 이미지 생성 모델(Nano-Banana-Pro)로 렌더링 후, Critic이 원본 컨텍스트 대비 사실 정합성, 시각적 결함을 평가하여 수정된 설명 제공. T=3회 반복
- **평가**: VLM-as-a-Judge 방식으로 faithfulness, conciseness, readability, aesthetics 4차원 참조 비교 평가. 계층적 집계(content > presentation)

## Originality

- **학술 일러스트 특화 에이전트 프레임워크**: 과학 논문 다이어그램 생성을 위해 검색-계획-스타일-시각화-비평의 5단계 파이프라인을 최초로 체계화
- **자동 Aesthetic Guideline 요약**: 참조 컬렉션 전체를 VLM으로 분석하여 학술 스타일 가이드라인을 자동 합성하는 새로운 접근
- **방법론 다이어그램 + 통계 플롯 통합**: 동일 프레임워크에서 Visualizer만 교체(이미지 생성 → 코드 생성)하여 두 유형 모두 지원
- **계층적 평가 프로토콜**: Faithfulness/Readability를 1차, Conciseness/Aesthetics를 2차로 구분하는 계층적 VLM-as-a-Judge 프로토콜 설계
- **PaperBananaBench**: NeurIPS 2025 기반 학술 다이어그램 생성 전용 벤치마크 최초 구축

## Limitation & Further Study

### 저자들이 언급한 한계

- 출력이 래스터 이미지로, 벡터 그래픽 대비 편집 불가능하고 확장성 제한
- 스타일 표준화와 다양성 간 트레이드오프 존재 -- 통일된 스타일 가이드가 표현의 다양성을 제약
- Fine-grained faithfulness(세밀한 연결 관계, 화살표 방향 등)에서 인간 대비 성능 격차 존재
- VLM-as-a-Judge 평가의 한계: 구조적 정확성 정량화 어려움, 미적 차원의 인간 선호 정렬 부족

### 자체판단 아쉬운 점

- 평가가 NeurIPS 2025 CS/AI 분야에 한정되어, 자연과학(물리, 화학, 생물) 논문 다이어그램으로의 일반화 가능성이 검증되지 않음
- Nano-Banana-Pro와 Gemini-3-Pro에 강하게 의존하며, 모델 교체 시 성능 변동이 큼 (GPT-Image-1.5로 교체 시 Overall 19.0%로 급감)
- 생성 비용(VLM API 호출 횟수, 이미지 생성 비용)에 대한 분석이 부재하여 실용성 판단이 어려움
- Faithfulness에서 여전히 인간(50.0%) 대비 45.8%로 미달 -- 핵심 평가 차원에서의 한계
- 참조 검색에서 random retriever와 semantic retriever의 성능 차이가 미미하여(48.3% vs 49.2%), 검색 컴포넌트의 실질적 기여가 불분명

### 후속 연구

- GUI Agent를 활용한 벡터 그래픽 편집 소프트웨어(Adobe Illustrator) 직접 조작을 통한 편집 가능 출력 생성
- 다양한 학문 분야(자연과학, 공학, 의학)로의 벤치마크 확장
- Test-time scaling을 통한 다양한 스타일 후보 생성 및 사용자 선택 워크플로우
- Fine-grained 구조 기반 평가 메트릭(그래프 기반 정확도 등) 개발
- 맞춤형 reward model 학습을 통한 미적 선호 정렬 개선

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 4/5 |
| Technical Soundness | 3/5 |
| Significance | 4/5 |
| Clarity | 5/5 |
| Overall | 4/5 |

**총평**: AI 과학자 파이프라인에서 시각적 커뮤니케이션이라는 간과된 병목을 정면으로 다룬 시의적절한 연구이다. 5개 에이전트의 체계적 파이프라인 설계와 자동 스타일 가이드라인 합성은 실용적 가치가 높으며, PaperBananaBench는 이 분야의 표준 평가 기준으로 기능할 잠재력이 있다. 다만 특정 상용 모델(Nano-Banana-Pro)에 대한 높은 의존도와 faithfulness 미달은 범용 도구로의 발전을 위해 해결해야 할 과제이다.
