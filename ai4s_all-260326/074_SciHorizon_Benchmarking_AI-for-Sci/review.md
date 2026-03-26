# SciHorizon: Benchmarking AI-for-Science Readiness from Scientific Data to Large Language Models

**저자:** Chuan Qin, Xin Chen, Chengrui Wang, Pengmin Wu, Xi Chen, Yihang Cheng, Jingyi Zhao, Meng Xiao, Xiangchao Dong, Qingqing Long, Boya Pan, Han Wu, Chengzan Li, Yuanchun Zhou, Hui Xiong, Hengshu Zhu
**출처:** arXiv:2503.13503 (2025)
**DOI:** [10.48550/arXiv.2503.13503](https://doi.org/10.48550/arXiv.2503.13503)
**PDF:** `C:\Users\jehyu\GoogleDrive\Zotero\Qin et al._2025_SciHorizon Benchmarking AI-for-Science Readiness from Scientific Data to Large Language Models.pdf`

---

## 한줄 요약 (Essence)
AI4Science의 준비도(readiness)를 **과학 데이터 품질**과 **LLM 역량** 두 축에서 종합적으로 평가하는 프레임워크 SciHorizon을 제안하고, 약 1,500개 데이터셋과 20개 이상 LLM에 대한 벤치마크 결과를 공개 플랫폼(www.scihorizon.cn)으로 제공한다.

## 연구 동기 (Motivation)
- AI4Science가 급성장하고 있으나, 과학 데이터의 AI 활용 적합성(AI-readiness)을 체계적으로 평가하는 프레임워크가 부재
- 기존 LLM 벤치마크는 특정 분야에 국한되거나(JEEBench, MultiMedQA), 단순 사실 회상(factual recall)에 편향되어 있어 과학적 추론·멀티모달리티·연구 윤리(Values)를 포괄하는 세분화된 평가가 필요
- 과학 데이터와 AI 모델의 준비도를 동시에 조망하는 통합 프레임워크가 없음

## 핵심 성과 (Achievement)
- **과학 데이터 평가 프레임워크**: Quality, FAIRness, Explainability, Compliance 4대 차원(15개 하위 지표)으로 AI-ready 데이터 평가 체계 수립
- **LLM 평가 프레임워크**: Knowledge, Understanding, Reasoning, Multimodality, Values 5대 핵심 지표(16개 하위 차원)로 다학문 LLM 역량 벤치마크 구축
- 지구과학·생명과학 분야 AI-ready 추천 데이터셋 목록 제시(Table 1, 2)
- 30개 LLM에 대한 5개 과학 분야(수학, 물리, 화학, 생명과학, 지구우주과학) 종합 평가: DeepSeek-V3(67.29) > Claude-3.5-Sonnet(65.01) > O1-Mini(64.58) 순
- **최초로 LLM의 과학 연구 가치(Values) 정렬도 평가**를 도입(학술 무결성, 공정성, 투명성 등 7개 윤리 원칙)

## 방법론 (How)
- **데이터 평가**: Delphi 방식의 전문가 합의 + 자동 메타데이터 검증 툴킷(CAS FAIR 인증 도구) 결합의 하이브리드 접근법. 2018~2023년 Scientific Data, ESSD 등 peer-reviewed 저널의 데이터 논문 약 1,500건 분석
- **LLM 평가**: 기존 공개 벤치마크(AGIEval, C-Eval, GPQA, MMLU, SciEval 등)를 전문가 검수 하에 통합·정제하여 객관식 문항으로 표준화. Knowledge는 Factuality/Robustness/Externalization/Helpfulness 4단계로 세분화
- **Values 평가**: GPT 기반 4단계 파이프라인으로 시나리오 기반 윤리 문항 자동 생성 후 전문가 검수(Relevance, Clarity, Fairness, Validity)
- **Multimodality**: 과학 차트 이해(Understanding)와 추론(Reasoning)으로 분리 평가

## 독창성 (Originality)
- 데이터 품질과 모델 역량을 하나의 프레임워크에서 동시 평가하는 **이중 관점(dual-perspective)** 접근이 독창적
- LLM의 **과학 연구 윤리(Values)** 평가를 최초로 벤치마크에 포함시킨 점이 차별적
- Knowledge 차원을 Factuality를 넘어 Robustness(노이즈 내성), Externalization(지식 표현 능력), Helpfulness(소형 모델 지원 능력)로 세분화한 설계가 정교
- 온라인 플랫폼(www.scihorizon.cn)을 통한 결과 공개로 지속적 업데이트와 커뮤니티 활용 가능

## 한계점 (Limitation)
- 데이터 AI-readiness 평가가 **지구과학과 생명과학 두 분야에만 국한**되어 있어 범용성 검증이 부족
- LLM 평가가 대부분 **객관식 문항 정답률** 기반이어서, 실제 과학 연구 수행 능력(가설 생성, 실험 설계, 논문 작성 등)과의 괴리가 존재
- Values 평가 문항이 GPT로 자동 생성된 후 전문가가 필터링하는 방식이라 **벤치마크 오염(contamination)** 및 특정 LLM에 유리한 편향 가능성
- 평가 대상 LLM이 2024년 말 기준이어서 GPT-4.5, Claude 3.5 Haiku 등 이후 모델은 미포함
- 데이터 평가의 15개 하위 지표 간 **가중치 설정 근거가 불명확**하며, Delphi 프로세스의 구체적 수렴 기준이 제시되지 않음
- 중국 연구기관 중심의 데이터셋에 편향(CAS 소속 데이터 리포지토리 비중이 높음)

## 총평 (Evaluation)
SciHorizon은 AI4Science의 성숙도를 데이터 품질과 모델 역량의 양면에서 체계적으로 진단하려는 야심찬 시도이다. 특히 LLM의 과학 연구 윤리 정렬도(Values)를 벤치마크에 포함시킨 것은 시의적절하며, 5개 과학 분야 x 5개 평가 차원의 세밀한 매트릭스는 모델 선택 시 유용한 참조점을 제공한다. DeepSeek-V3가 종합 1위, O1-Mini가 추론 특화, Claude-3.5-Sonnet이 화학·윤리 분야 강세라는 발견은 실용적 가치가 높다. 다만 평가 방식이 객관식 정답률에 크게 의존하여 실제 과학 연구 맥락에서의 AI 활용 능력을 충분히 반영하지 못하며, 데이터 평가 범위가 두 분야에 한정된 점은 향후 확장이 필요하다. 온라인 플랫폼을 통한 지속적 업데이트 가능성은 이 벤치마크의 장기적 가치를 높이는 요소이다.
