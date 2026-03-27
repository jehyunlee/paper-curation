# ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs

- **저자**: Yujia Qin, Shihao Liang, Yining Ye, Kunlun Zhu, Lan Yan, Yaxi Lu, Yankai Lin, Xin Cong, Xiangru Tang, Bill Qian, Sihan Zhao, Lauren Hong, Runchu Tian, Ruobing Xie, Jie Zhou, Mark Gerstein, Dahai Li, Zhiyuan Liu, Maosong Sun
- **소속**: Tsinghua University, ModelBest Inc., Renmin University of China, Yale University, WeChat AI (Tencent Inc.), Zhihu Inc.
- **출판**: arXiv preprint (2023.10)
- **DOI**: [10.48550/arXiv.2307.16789](https://doi.org/10.48550/arXiv.2307.16789)

---

## Essence (본질)

오픈소스 LLM(예: LLaMA)이 외부 API 도구를 활용하는 능력에서 폐쇄형 모델(ChatGPT, GPT-4)에 크게 뒤처지는 문제를 해결하기 위한 **범용 도구 사용 프레임워크**다. RapidAPI Hub에서 수집한 16,464개의 실제 REST API를 기반으로, 데이터 구축(ToolBench), 모델 학습(ToolLLaMA), 자동 평가(ToolEval)를 아우르는 종합적인 파이프라인을 제시한다. 핵심은 ChatGPT를 활용한 자동 데이터 구축과, 깊이 우선 탐색 기반 의사결정 트리(DFSDT)를 통한 추론 능력 강화에 있다.

---

## Motivation (동기)

1. **오픈소스 LLM의 도구 사용 능력 부재**: 기존 instruction tuning은 기본 언어 작업에 집중하여, API 호출 등 도구 활용 영역을 간과하고 있었다.
2. **기존 데이터셋의 한계**: 선행 연구들은 (i) 제한된 수의 API, (ii) 단일 도구만 사용하는 단순한 시나리오, (iii) ReACT/CoT의 열등한 계획 및 추론 능력이라는 세 가지 근본적 한계를 가지고 있었다.
3. **폐쇄형 모델 의존 탈피**: ChatGPT/GPT-4의 우수한 도구 사용 능력이 폐쇄형으로만 제공되어, AI 기술의 민주화와 커뮤니티 주도 혁신이 제한되고 있었다.

---

## Achievement (성과)

- **ToolBench 데이터셋 구축**: 49개 카테고리, 3,451개 도구, 16,464개 API, 126,486개 (instruction, solution path) 쌍으로 구성된 대규모 instruction-tuning 데이터셋을 자동 구축했다.
- **ToolLLaMA의 성능**: LLaMA-2 7B를 fine-tuning한 ToolLLaMA가 Text-Davinci-003, Claude-2를 능가하고, ChatGPT에 근접하는 도구 사용 성능을 달성했다 (평균 pass rate 66.7%, win rate 60.0%).
- **DFSDT의 우월성**: 제안된 DFSDT가 ReACT 대비 평균 pass rate를 35.3%에서 63.8%로 대폭 향상시켰다.
- **API Retriever**: 16,000+ API 풀에서 적절한 API를 자동 추천하는 신경망 기반 검색기를 개발하여, oracle API보다 오히려 높은 성능을 보였다.
- **OOD 일반화**: APIBench에서 학습 없이도 Gorilla(전용 모델)에 필적하는 zero-shot 일반화 성능을 달성했다.

---

## How (방법론)

### 1. ToolBench 데이터 구축 (3단계)

| 단계 | 내용 | 규모 |
|------|------|------|
| API 수집 | RapidAPI Hub에서 REST API 수집 및 품질 필터링 | 3,451 도구, 16,464 API |
| Instruction 생성 | ChatGPT로 단일/다중 도구 시나리오별 지시문 자동 생성 | ~200k 쌍 |
| Solution Path 주석 | DFSDT로 유효한 API 호출 경로 탐색 및 주석 | 126,486 쌍 |

- **샘플링 전략**: 단일 도구(I1), 카테고리 내 다중 도구(I2), 컬렉션 내 다중 도구(I3)의 세 가지 시나리오로 다양성을 확보했다.

### 2. DFSDT (Depth-First Search-based Decision Tree)

기존 ReACT의 두 가지 한계를 극복한다:
- **오류 전파 방지**: 잘못된 행동이 연쇄적으로 전파되는 것을 방지하기 위해, 탐색 중 되돌아가기(backtracking) 허용
- **탐색 공간 확장**: 단일 경로가 아닌 여러 추론 경로를 동시에 평가하여, 복잡한 지시문도 해결 가능
- pre-order traversal 변형을 사용하여 비용 효율성도 확보 (단순 지시문에서는 ReACT로 퇴화)

### 3. ToolEval (자동 평가)

- **Pass Rate**: 제한된 예산 내에서 지시문 완료 비율
- **Win Rate**: 두 solution path의 품질 비교 (ChatGPT 기반)
- 인간 평가와의 일치도: pass rate 87.1%, win rate 80.3%

### 4. API Retriever

- Sentence-BERT 기반 dense retriever로, instruction과 API 문서 간 임베딩 유사도 계산
- NDCG@5에서 평균 84.9% 달성 (BM25: 17.0%, Ada: 45.4%)

---

## Originality (독창성)

1. **DFSDT**: Tree-of-Thought(ToT)와 유사한 아이디어이나, 무한한 결정 공간을 가진 실제 도구 사용 문제에 맞게 설계된 점이 차별화된다. ReACT의 상위 호환으로, 단순한 경우 ReACT로 퇴화하여 효율성도 유지한다.
2. **대규모 실제 API 기반 데이터셋**: 기존 연구가 수십~수백 개의 API만 다룬 것과 달리, 16,000+ 실제 API를 포괄하는 최초의 대규모 도구 학습 데이터셋이다.
3. **End-to-End 파이프라인**: API 수집 -> instruction 생성 -> solution path 주석 -> 모델 학습 -> API retrieval -> 자동 평가까지, 도구 학습의 전 과정을 체계화한 최초의 시도다.
4. **API Retriever 통합**: 실제 사용 시 사용자가 API를 직접 선택할 필요 없이, 자연어 지시문만으로 적절한 API를 자동 추천받아 사용할 수 있는 실용적 파이프라인을 구현했다.

---

## Limitation & Further Study (한계 및 향후 연구)

### 한계
1. **ChatGPT 의존성**: ToolBench의 데이터 구축, ToolEval의 평가 모두 ChatGPT에 의존하므로, ChatGPT의 편향이 전파될 수 있다.
2. **API 시간 변동성**: RapidAPI의 API들은 시간에 따라 변하거나 비활성화될 수 있어, 재현성에 문제가 있을 수 있다.
3. **평가의 주관성**: 도구 사용의 "정답"이 무한할 수 있어, 인간 전문가 간에도 의견 불일치가 발생한다고 저자들이 인정하고 있다.
4. **모델 규모 제한**: LLaMA-2 7B만 실험하여, 더 큰 모델에서의 성능 변화를 확인하지 못했다.
5. **실제 배포 검증 부재**: 실제 사용자 환경에서의 robustness, latency, 안전성 등에 대한 검증이 없다.

### 향후 연구 방향
- 더 다양한 도구 유형(GUI 기반, 코드 실행 등)으로의 확장
- 다국어/다문화 환경에서의 도구 사용 능력 평가
- DFSDT의 비용 효율성을 더 개선하는 탐색 알고리즘 연구
- 실시간 API 변동에 적응하는 동적 학습 메커니즘 개발

---

## Evaluation (총평)

ToolLLM은 오픈소스 LLM의 도구 사용 능력을 체계적으로 향상시킨 선구적 연구다. 16,000+ 실제 API를 아우르는 ToolBench 데이터셋, DFSDT를 통한 추론 능력 강화, ToolEval을 통한 자동 평가라는 세 축이 유기적으로 결합되어 있다. 특히 DFSDT가 ReACT 대비 pass rate를 거의 두 배로 끌어올린 점은 인상적이며, 오픈소스 모델이 폐쇄형 모델에 근접할 수 있음을 실증적으로 보여주었다. 다만 ChatGPT에 대한 의존성과 API의 시간적 변동성은 근본적 한계로 남아 있으며, 실제 프로덕션 환경에서의 검증이 필요하다. 이후 등장한 function calling, tool use 관련 연구들의 토대가 된 중요한 기여다.

## 평가
| 항목 | 점수 (1-5) |
|------|-----------|
| Novelty | 4 |
| Technical Soundness | 4 |
| Significance | 5 |
| Overall | 4.3 |

**총평**: 16000개 이상 실제 API를 활용한 ToolLLM/ToolBench는 LLM 도구 사용 능력의 기반 인프라를 구축한 분야 필수 참고 논문이다.
