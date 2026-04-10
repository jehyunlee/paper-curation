---
title: "691_S1-MMAlign_A_Large-Scale_Multi-Disciplinary_Dataset_for_Scie"
authors:
  - "He Wang"
  - "Longteng Guo"
  - "Pengkang Huo"
  - "Xuanxu Lin"
  - "Yichen Yuan"
date: "2026.01"
doi: "10.48550/arXiv.2601.00264"
arxiv: ""
score: 4.25
essence: "과학 논문의 2.5백만 편에서 수집한 1,550만 개의 이미지-텍스트 쌍으로 구성된 대규모 멀티모달 데이터셋을 제시한다. Qwen-VL 기반 의미 강화 파이프라인을 통해 희소한 원본 캡션을 논문의 추상, 인용 맥락과 결합하여 자급식의 과학적으로 근거 있는 설명으로 변환하며, CLIP 점수 기준 18.21% 정렬 개선을 달성한다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/Multimodal_Scientific_Reasoning"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Wang et al._2026_S1-MMAlign A Large-Scale, Multi-Disciplinary Dataset for Scientific Figure-Text Understanding.pdf"
---

# S1-MMAlign: A Large-Scale, Multi-Disciplinary Dataset for Scientific Figure-Text Understanding

> **저자**: He Wang, Longteng Guo, Pengkang Huo, Xuanxu Lin, Yichen Yuan, Jie Jiang, Jing Liu | **날짜**: 2026-01-01 | **DOI**: [10.48550/arXiv.2601.00264](https://doi.org/10.48550/arXiv.2601.00264)

---

## Essence

![Figure 2](./fig2_caption_distribution.png)
*그림 2: 원본 캡션과 의미 강화 캡션의 문자 길이 분포. 원본 캡션(주황색)은 평균 267±261자에서 강화된 캡션(파란색)은 759±251자로 2.8배 확장됨*

과학 논문의 2.5백만 편에서 수집한 1,550만 개의 이미지-텍스트 쌍으로 구성된 대규모 멀티모달 데이터셋을 제시한다. Qwen-VL 기반 의미 강화 파이프라인을 통해 희소한 원본 캡션을 논문의 추상, 인용 맥락과 결합하여 자급식의 과학적으로 근거 있는 설명으로 변환하며, CLIP 점수 기준 18.21% 정렬 개선을 달성한다.

## Motivation

- **Known**: 일반 도메인(예: COCO, LAION)의 멀티모달 학습이 성공적으로 발전했으며, "AI for Science" 패러다임이 가속화되고 있음

- **Gap**: 과학 이미지는 실험 장치, 히트맵, 현미경 이미지 등 복잡한 시각 정보를 담고 있으나, PDF의 원본 캡션은 "Figure 3: Ablation study results"처럼 맥락에 의존적이고 희소함. 이러한 "의미 간극(semantic gap)"은 모델이 차트 유형만 인식하고 과학적 의미를 이해하지 못하게 함

- **Why**: 과학적 이유 파악, 변수 관계 이해, 이론적 근거 제시 등을 위해 시각 신호와 이론적 배경을 통합한 고품질 데이터셋 필요

- **Approach**: 논문 제목, 초록, 지역 인용 맥락(local citation context)을 통합하여 Qwen-VL로 이미지를 재캡셔닝하는 AI 기반 의미 강화 파이프라인 도입

## Achievement

![Figure 1](./fig1_disciplinary_distribution.png)
*그림 1: S1-MMAlign의 주제 분포. 물리학(33%), 컴퓨터과학(25%), 천문학(13%), 생물학(10%), 수학(9%), 기타(10%)*

1. **대규모 다학제 데이터셋**: arXiv, bioRxiv, medRxiv, ChemRxiv 등 오픈 액세스 저장소에서 2.5백만 논문을 통해 1,550만 개의 이미지-텍스트 쌍 구축. 총 3.03TB 저장 크기, 물리학과 컴퓨터과학이 전체의 58%로 주요 구성

2. **의미 강화 효과**: 원본 캡션 대비 2.8배 길이 확장(267→759자), SciBERT 기반 의사 당혹도(pseudo-perplexity) 메트릭으로 의미적 모호성 감소 확인, CLIP 점수로 이미지-텍스트 정렬 18.21% 개선

3. **기술 검증**: 강화된 캡션이 생성형 환각(hallucination) 완화, 과학적 인과관계 포착, 하위 과제에서 더 견고한 기초 제공

## How

![Figure 3](./fig3_pipeline.png)
*그림 3: S1-MMAlign 데이터 구성 파이프라인. (1) 데이터 수집 → (2) 전처리 → (3) AI 처리 → (4) 구조화된 출력 생성*

**Phase 1: 데이터 수집**
- arXiv (LaTeX 소스), bioRxiv, medRxiv, ChemRxiv, Nature Communications 등 오픈 액세스 저장소 대상

**Phase 2: 전처리**
- arXiv 파이프라인: 아카이브 무결성 검증(~20% 거부율), LaTeX 파싱으로 이미지-캡션 매핑, EPS/PDF를 PNG로 래스터화, 5KB 미만 및 손상된 파일 필터링
- PDF 파이프라인: MinerU 기반 레이아웃 감지, 기하학적 근접도 매칭으로 다중 열 레이아웃 처리, 캡션 추출 및 정제

**Phase 3: 의미 강화**
- Qwen-VL(SigLip-2 인코더 탑재) 활용으로 고해상도 동적 입력 처리
- 논문 제목+초록+지역 인용 맥락 통합(knowledge-augmented context injection)으로 시각 인식을 과학적 해석으로 변환
- H100 GPU 클러스터 8개 활용, vLLM 라이브러리의 PagedAttention과 연속 배치 처리로 병렬화

**Phase 4: 구조화된 출력**
- JSONL 형식 메타데이터와 TAR 아카이브 이미지 저장소로 분리(유연한 접근 패턴 지원)

## Originality

- **과학 멀티모달의 의미 간극 문제 정식화**: 일반 도메인 데이터셋과 과학 데이터의 근본적 차이(맥락 의존성, 희소성) 명확히 규정하고 첫 대규모 해결책 제시

- **지식 보강 맥락 주입(Knowledge-Augmented Context Injection)**: 단순 이미지 캡셔닝을 넘어 논문 전체 맥락(제목, 초록, 인용)을 통합하여 인과관계 기반 설명 생성 – 과학 도메인 특화 설계

- **대규모 의미 품질 검증**: SciBERT 기반 의사 당혹도, CLIP 정렬 점수 등 정량적 지표로 강화 효과 입증(18.21% 개선)

- **멀티소스 이질적 데이터 처리**: LaTeX 소스와 PDF 문서를 각각 다른 파이프라인으로 처리하되 통일된 품질 표준 적용

## Limitation & Further Study

**한계**:
- 데이터셋 공개일(2026년) 관점에서 평가 시점의 VLM 성능에 의존적이며, Qwen-VL의 지역화(hallucination) 가능성 미언급
- 학문 분야 분포 불균형(물리·CS 편중 58%) – 생물, 의학, 화학 도메인 대표성 상대적 약함
- 원본 논문의 인용 맥락 누락 여부, 다국어 논문 처리 여부 불명확
- 재캡셔닝 파이프라인의 일관성 및 해석 편향(bias) 검증 부재

**후속 연구**:
- 강화된 캡션의 과학적 정확성에 대한 인간 주석자 검증
- 다운스트림 과제(과학 QA, 그래프 이해, 실험 설계 도움)에서 실제 성능 개선 입증
- 도메인별 세분화된 평가 메트릭 개발
- 동적 재캡셔닝 메커니즘으로 신규 논문에 대한 확장성 제고

## Evaluation

- **Novelty (독창성)**: 4.5/5
  - 과학 멀티모달의 의미 간극 문제를 명확히 하고 지식 보강 맥락 통합이 혁신적. 그러나 개별 기법(VLM, 맥락 통합)은 기존 개념의 응용.

- **Technical Soundness (기술 건전성)**: 4/5
  - 4단계 파이프라인 설계가 엄밀하고, 다중 소스 처리 및 전처리 로직이 타당함. 다만 재캡셔닝 파이프라인의 오류율 분석이 부재하고, 강화 효과의 정량화가 CLIP/pseudo-PPL에만 제한됨.

- **Significance (중요도)**: 4.5/5
  - "AI for Science" 시대에 핵심 기초 자원으로서 매우 가치 있음. 1,550만 쌍 규모와 공개 배포는 커뮤니티 영향력 클 것. 다만 실제 과학 발견 가속화 효과 미실증.

- **Clarity (명확성)**: 4/5
  - 4단계 파이프라인 설명, 의미 강화 동기 명확함. 그러나 Figure 4 이후 본문 불완전 수록으로 전체 구조 파악 어려움. 메타데이터 스키마 상세 명시 필요.

- **Overall (종합)**: 4.25/5

**총평**: 과학 멀티모달 학습의 의미 간극을 처음 대규모로 정의하고 지식 보강 맥락 주입으로 우아하게 해결한 데이터셋으로, 공개 배포를 통해 AI for Science 커뮤니티의 거대한 기초 자원이 될 것으로 기대된다. 다만 강화 파이프라인의 오류율, 도메인별 정확성, 하위 과제에서의 실질적 성능 이득에 대한 정밀한 검증이 보완되면 더욱 견고할 것이다.

## Related Papers

- 🔄 다른 접근: [[papers/551_MMC_Advancing_Multimodal_Chart_Understanding_with_Large-scal/review]] — 과학 vs 일반 차트 이해에서 멀티모달 대규모 데이터셋의 다른 접근법을 비교할 수 있다
- 🔗 후속 연구: [[papers/708_SciCap_Generating_Captions_for_Scientific_Figures/review]] — 과학적 그림 캡션 생성을 대규모 이미지-텍스트 정렬로 확장한 연구다
- 🏛 기반 연구: [[papers/336_FigCaps-HF_A_Figure-to-Caption_Generative_Framework_and_Benc/review]] — 그림-캡션 생성 프레임워크가 과학 논문 멀티모달 정렬의 기반을 제공한다
- 🧪 응용 사례: [[papers/566_Multimodal_deepresearcher_Generating_text-chart_interleaved/review]] — 멀티모달 과학 연구 생성에 대규모 과학 이미지-텍스트 데이터셋을 적용할 수 있다
