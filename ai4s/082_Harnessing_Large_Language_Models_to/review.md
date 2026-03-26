# Harnessing Large Language Models to Collect and Analyze Metal-Organic Framework Property Data Set

> **저자**: Yeonghun Kang, Wonseok Lee, Taeun Bae, Seunghee Han, Huiwon Jang, Jihan Kim | **날짜**: 2025-02-05 | **Journal**: Journal of the American Chemical Society (JACS), 147(5), 3943-3958 | **DOI**: 10.1021/jacs.4c11085

---

## Essence

L2M3(Large Language Model MOF Miner)는 LLM 체인을 활용하여 40,000편 이상의 MOF 논문에서 합성 조건과 물성 데이터를 자동 추출하고 구조화된 데이터베이스를 구축하는 시스템이다. 추출 정확도 F1 0.93 이상을 달성하였으며, 구축된 데이터를 활용하여 시뮬레이션-실험 데이터 간 괴리의 원인(잔류 종)을 규명하고, LLM 기반 합성 조건 추천 시스템(recommendation score 0.83)을 개발하였다.

## Motivation

- **알려진 것**: MOF는 가스 저장, 분리, 촉매 등 다양한 응용 분야를 가진 다공성 소재로, 수만 편의 연구 논문이 축적되어 있음. 기존 rule-based 및 ML 기반 데이터 마이닝 기법이 MOF 데이터 추출에 활용되어 왔음
- **Gap**: 기존 연구는 1-2개 물성만 추출하거나, 합성 조건만 추출하고 물성과 연결하지 못하는 한계. 또한 rule-based 방법은 새로운 대상 확장 시 높은 비용이 소요되며, 시뮬레이션 데이터와 실험 데이터 간 괴리의 원인이 체계적으로 규명되지 않음
- **왜 중요한가**: 실험 데이터의 대규모 수집은 ML 기반 소재 발견의 정확도를 높이는 핵심 요소이며, structure-synthesis-property 관계 이해가 MOF 설계 최적화에 필수적
- **접근법**: 다중 LLM 에이전트(categorization-inclusion-extraction 3단계 체인)를 통해 텍스트와 테이블 모두에서 32가지 물성과 21가지 합성 조건을 JSON 형식으로 자동 추출, CCDC 데이터베이스와 매칭

## Achievement

1. **대규모 데이터 추출**: 40,000편 이상의 논문에서 39,476편 분석 완료, 32가지 정의된 물성 + 21가지 합성 조건 카테고리 추출
2. **높은 정확도**: Categorization F1 > 0.96, Inclusion F1 > 0.94, Extraction F1 > 0.93 달성 -- 테이블 마이닝은 F1 1.00
3. **시뮬레이션-실험 괴리 규명**: 실험 데이터로 학습한 ML 모델(R^2 = 0.803, XGBoost 밀도 예측)이 시뮬레이션 데이터 학습 모델(R^2 = 0.495)보다 현저히 우수함을 입증. SHAP 분석으로 잔류 종(residual species)이 주요 원인임을 규명
4. **합성 조건 추천 시스템**: GPT-4o/GPT-3.5 fine-tuning 기반 추천 시스템이 median recommendation score 0.83 달성, 향후 5년간의 합성 조건도 효과적으로 예측
5. **ChatMOF 통합**: L2M3 데이터베이스를 ChatMOF 챗봇과 연동하여 대화형 합성 정보 검색 기능 구현

## How

- **데이터 수집**: ACS, Elsevier, RSC, Springer 4개 출판사에서 41,681편 수집. CSD MOF subset 기준 + Scopus 키워드 검색
- **LLM 체인 아키텍처**: 3단계 파이프라인 -- (1) Categorization (GPT-3.5-turbo fine-tuned, 723 예시), (2) Inclusion (GPT-3.5-turbo fine-tuned, 681 예시), (3) Extraction (GPT-4 prompt engineering)
- **적응형 프롬프트**: Inclusion 단계 결과에 따라 Extraction 프롬프트를 동적으로 구성하여 프롬프트 길이 감소 및 정확도 향상
- **데이터 통합**: 메타데이터(이름, 심볼, 화학식, refcode, 격자상수) 기반 동일 물질 매칭, CCDC 데이터베이스와 구조 연결
- **ML 분석**: Descriptor-based (RF, XGBoost, SVM, KNN) + CGCNN + MOFTransformer로 밀도 예측, SHAP 분석으로 feature importance 도출
- **합성 추천**: 60,735개 합성 조건 중 9,044개를 정제하여 GPT-4o/GPT-3.5 fine-tuning, precursor 입력 기반 합성 조건 생성
- **비용**: Langchain 기반 자동화, fine-tuning이 prompt engineering 대비 약 95% 비용 절감

## Originality

- **Multi-LLM 체인 기반 대규모 소재 데이터 마이닝**: 단일 LLM 대비 정확도와 비용 효율성 모두 우수한 3단계 LLM 체인 아키텍처를 MOF 분야에 최초로 적용하여 20개 이상 물성을 동시 추출
- **Structure-Synthesis-Property 삼각 연결**: 합성 조건과 물성을 함께 추출하고 CCDC 구조 데이터와 연결하여, 기존에 불가능했던 삼각 관계 분석을 가능하게 함
- **시뮬레이션-실험 괴리의 정량적 원인 분석**: 잔류 종(용매, modulator, counter ion)이 밀도 차이의 주요 원인임을 데이터 기반으로 규명하고, 분자량과 밀도 차이 간 상관관계(Pearson r = 0.64) 발견
- **LLM 기반 합성 조건 추천**: 예측(prediction)이 아닌 추천(recommendation) 패러다임으로 합성 조건 생성 문제를 재정의하여, LLM의 생성 능력을 효과적으로 활용

## Limitation & Further Study

### 저자들이 언급한 한계

- Extraction 단계에서 합성 방법 간 유사성(solvothermal vs chemical synthesis)으로 인한 분류 오류 존재
- GPT-4-32K API를 비용 문제로 도입하지 못하여 8000 토큰 초과 시 GPT-3.5-turbo로 대체
- 오픈소스 LLM(Llama 등)이 GPT 대비 낮은 정확도를 보여 상용 API 의존성 존재

### 자체판단 아쉬운 점

- 40,000편 규모에서의 전체 추출 비용에 대한 구체적 분석이 부족하여, 실제 재현 시 예산 규모를 가늠하기 어려움
- 합성 조건 추천 시스템의 recommendation score가 published 조건과의 유사도이므로, 실제 합성 성공률과의 관계가 검증되지 않음 (wet-lab 검증 부재)
- Outlier 분석(Fig. 5b)의 6가지 유형 분류가 수동으로 이루어져 체계적 자동화가 되지 않음
- 텍스트에서 추출한 물성값의 단위 통일 및 정규화 과정에 대한 상세 설명이 부족
- CCDC 매칭률이 명시적으로 보고되지 않아, 전체 데이터 중 구조-물성-합성이 모두 연결된 비율을 알기 어려움

### 후속 연구

- Wet-lab 검증을 통한 합성 조건 추천 시스템의 실제 성공률 평가
- 오픈소스 LLM의 fine-tuning을 통한 상용 API 의존성 탈피
- MOF 이외 소재(제올라이트, COF, 페로브스카이트 등)로의 확장 (Note S6에서 가능성 시사)
- 잔류 종 제거 전략과 MOF 성능 최적화 간 관계에 대한 심화 연구
- 합성 데이터 증가에 따른 추천 시스템 성능 향상 추적

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 4/5 |
| Technical Soundness | 5/5 |
| Significance | 5/5 |
| Clarity | 4/5 |
| Overall | 4/5 |

**총평**: JACS에 게재된 본 연구는 LLM 체인을 활용하여 MOF 분야의 대규모 실험 데이터 마이닝을 성공적으로 자동화한 모범적 사례이다. 40,000편 이상의 논문에서 높은 정확도(F1 > 0.93)로 물성과 합성 조건을 동시에 추출하고, 이를 구조 데이터와 연결하여 시뮬레이션-실험 괴리의 원인을 규명한 점이 핵심 기여이다. 합성 조건 추천 시스템까지 개발하여 실용적 가치를 높였으며, 프롬프트 조정만으로 다른 소재 분야로 쉽게 확장 가능한 점이 높이 평가된다. AI for Science에서 LLM 기반 과학 문헌 마이닝의 새로운 표준을 제시한 연구이다.
