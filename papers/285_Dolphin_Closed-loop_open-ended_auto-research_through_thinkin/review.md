---
title: "285_Dolphin_Closed-loop_open-ended_auto-research_through_thinkin"
authors:
  - "Jiakang Yuan"
  - "Xiangchao Yan"
  - "Botian Shi"
  - "Tao Chen"
  - "Wanli Ouyang"
date: "2025"
doi: "N/A"
arxiv: ""
score: 4.0
essence: "DOLPHIN은 폐쇄 루프(closed-loop) 구조를 갖춘 LLM 기반의 자동 과학 연구 프레임워크로, 아이디어 생성, 실험 검증, 결과 피드백의 세 단계를 반복하며 연구 자동화 수준을 획기적으로 높인다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/Autonomous_Hypothesis_Discovery"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Yuan et al._2025_Dolphin Closed-loop open-ended auto-research through thinking, practice, and feedback.pdf"
---

# Dolphin: Closed-loop open-ended auto-research through thinking, practice, and feedback

> **저자**: Jiakang Yuan, Xiangchao Yan, Botian Shi, Tao Chen, Wanli Ouyang, Bo Zhang, Lei Bai, Yu Qiao, Bowen Zhou | **소속**: Fudan University, Shanghai Artificial Intelligence Laboratory | **날짜**: 2025 | **DOI**: N/A

---

## Essence

![Figure 1](https://arxiv.org/html/2501.03916v3/x1.png)
*과학 연구의 진화 단계: (a) 인간 주도 연구, (b) AI 보조 연구, (c) 반자동 연구, (d) 완전 자동 연구*

DOLPHIN은 폐쇄 루프(closed-loop) 구조를 갖춘 LLM 기반의 자동 과학 연구 프레임워크로, 아이디어 생성, 실험 검증, 결과 피드백의 세 단계를 반복하며 연구 자동화 수준을 획기적으로 높인다.

## Motivation

- **Known**: 
  - 최근 AI-Scientist 등 여러 자동 연구 프레임워크들이 아이디어 생성부터 논문 작성까지 일부 자동화를 달성함
  - LLM의 능력 향상으로 AI 보조 연구에서 반자동 연구로의 진화가 진행 중

- **Gap**: 
  - 기존 연구들은 생성된 아이디어의 질을 인간 평가나 LLM 평가에만 의존하며, 실제 실험 검증이 부족함
  - 실험 결과를 다시 아이디어 생성 단계로 피드백하는 메커니즘이 없어 인간 연구자의 반복적 개선 과정을 모방하지 못함
  - AI-Scientist도 자체 구축 데이터셋을 사용하여 기존 방법과의 의미 있는 비교 불가능

- **Why**: 
  - 인간 연구자는 실험 결과를 기반으로 아이디어를 반복적으로 개선하는 것이 핵심이며, 이는 진정한 자동 연구의 필수 요소
  - 공개 벤치마크 데이터셋을 이용한 검증으로 생성 아이디어의 실제 가치를 평가할 필요

- **Approach**: 
  - 폐쇄 루프 구조로 실험 결과를 다음 아이디어 생성에 활용
  - 작업 속성(task attribute) 기반 논문 랭킹으로 관련성 높은 참고문헌 선별
  - 예외 추적(exception-traceback) 기반 디버깅으로 코드 실행 성공률 향상
  - 공개 벤치마크(ModelNet40, CIFAR-100, SST-2 등)에서 검증

## Achievement

![Figure 2](https://arxiv.org/html/2501.03916v3/x2.png)
*DOLPHIN의 전체 프레임워크: 아이디어 생성 → 실험 검증 → 결과 피드백의 폐쇄 루프*

1. **폐쇄 루프 자동 연구 달성**: 기존 연구와 달리 실험 결과를 다시 아이디어 생성에 피드백하는 진정한 폐쇄 루프 구조 구현으로 연속적 성능 개선 실현

2. **공개 벤치마크에서 SOTA 달성**: 3D 점군 분류(3D point classification) 등 일부 작업에서 기존 인간 설계 SOTA 방법을 능가하는 아이디어 자동 생성 (PointNet 대비 성능 향상)

3. **작업 속성 기반 논문 랭킹**: 주제 관련성(topic relevance)과 작업 속성 관련성(task attribute relevance)을 동시에 고려하여 1-10 스코어링으로 부적절한 논문 필터링

4. **예외 추적 기반 디버깅**: 에러 추적(traceback) 정보로부터 지역 코드 구조를 분석하여 효율적으로 버그를 수정하고 코드 실행 성공률 향상

5. **간결한 방법 제안**: 현재의 인간 설계 SOTA 방법보다 더 간결한 구현으로 유사하거나 우수한 성능 달성

6. **MLE-bench 호환성**: AIDE 등 기존 코드 생성 파이프라인과 통합 가능하며 기술/코드 버전 업데이트 지원

## How

![Figure 3](https://arxiv.org/html/2501.03916v3/x3.png)
*예외 추적 기반 디버깅 프로세스: 에러 정보로부터 지역 코드 구조 분석*

**아이디어 생성 프로세스 (Ideas Generation)**:
- Semantic Scholar API를 통해 입력 주제 관련 논문 검색
- 작업 속성 추출: LLM이 입력 주제의 모델 입력(input), 출력(output) 등 특성 추출
- 두 기준 점수화: ① 입력 주제와의 관련성, ② 작업 속성 정렬도
- 점수 8 이상의 논문만 선별하여 아이디어 생성 참고문헌으로 활용
- 생성된 아이디어 필터링: 참신성(novelty), 독립성(independence) 등으로 평가

**실험 검증 프로세스 (Experimental Verification)**:
- 필터링된 아이디어 각각에 대해 실험 계획 수립
- 코드 템플릿 기반으로 구현 자동 생성
- 예외 추적 기반 디버깅:
  - Python 파일 실행 후 에러 발생 시 traceback 수집
  - 지역 코드 구조(local code structure) 분석으로 관련 부분 파악
  - 버그 수정 계획 수립 및 코드 수정
  - 반복 실행으로 성공 여부 판단

**결과 피드백 프로세스 (Results Feedback)**:
- 성공적으로 실행된 실험의 결과 자동 분석
- 개선(Improve), 유지(Keep), 거절(Decline) 분류
- 분석 결과를 메모리에 저장하여 다음 루프의 아이디어 생성에 활용
- 유사성 기반 검색으로 과거 경험 활용 및 새로운 프롬프트 생성

## Originality

- **진정한 폐쇄 루프 구조**: 기존의 일방향 파이프라인(아이디어 → 실험 → 논문)과 달리, 실험 결과를 아이디어 생성으로 피드백하는 폐쇄 루프 구현으로 인간 연구 프로세스에 더 가깝게 모사

- **작업 속성 기반 필터링**: 단순 키워드 또는 인용도 기반 논문 검색이 아닌, 작업의 입/출력 특성까지 고려한 정교한 논문 랭킹 메커니즘

- **예외 추적 기반 지역 코드 구조 분석**: 일반적인 LLM 코드 생성 후 통째로 재생성하는 방식이 아닌, 에러 정보의 지역 구조를 파악하여 효율적으로 디버깅

- **공개 벤치마크 검증**: AI-Scientist 등과 달리 ModelNet40, CIFAR-100 등 공개 벤치마크를 사용하여 생성 아이디어의 객관적 가치 입증

- **다양한 작업 및 모달리티 지원**: 3D 분류, 이미지 분류, 감정 분류 등 다양한 도메인에서 일관되게 작동하는 범용성

## Limitation & Further Study

- **평가 제약성**: 
  - 선별된 벤치마크 데이터셋들이 제한적이며, 더 광범위한 과학 분야(화학, 물리학, 생물학 등)에서의 검증 부족
  - 생성 아이디어의 참신성 정량화 방법 미흡
  - 인간 SOTA와의 정확한 비교를 위해 데이터셋별 상세 메타데이터 필요

- **확장성 문제**:
  - 대규모 모델 학습이 필요한 경우 계산 비용 급증
  - 매 루프마다 논문 검색, LLM 추론, 코드 생성 실행으로 인한 높은 시간 복잡도
  - 메모리 저장소의 효율적 관리 방안 부재

- **디버깅 한계**:
  - 예외 추적 기반 디버깅도 근본적인 로직 오류는 감지 어려움
  - 복잡한 아키텍처(예: 분산 학습) 디버깅 미지원

- **피드백 메커니즘 정교화**:
  - 결과 분석이 단순한 성능 지표 기반이며, 실패 원인 심층 분석 부족
  - 음수 결과(negative results)로부터의 학습 메커니즘 미흡

- **후속 연구 방향**:
  - 강화학습(RL) 또는 메타학습으로 피드백 신호를 더욱 정교하게 활용
  - 멀티에이전트 시스템으로 확장하여 협업 연구 환경 구현
  - 도메인 특화 LLM 또는 소형 모델 활용으로 비용 절감
  - 논문 작성 자동화까지 포함하여 완전 파이프라인 구현

## Evaluation

- **Novelty (독창성)**: 4/5
  - 폐쇄 루프 구조와 작업 속성 기반 필터링은 혁신적이나, 각 구성 요소(논문 검색, 코드 생성, 디버깅)는 기존 기법의 조합
  
- **Technical Soundness (기술적 타당성)**: 4/5
  - 논문 랭킹, 코드 생성, 디버깅 파이프라인은 잘 설계되었으나, 디버깅 메커니즘의 근본적 한계와 결과 분석의 단순성이 아쉬움
  
- **Significance (중요성)**: 4/5
  - 자동 과학 연구 분야에서 중요한 진전이며 여러 벤치마크에서 SOTA 달성이 의미 있으나, 평가 범위가 제한적이고 실용성 검증 필요
  
- **Clarity (명확성)**: 4/5
  - 전체 프레임워크 설명과 프로세스 흐름이 명확하며 Figure 2로 잘 시각화되었으나, 일부 상세 알고리즘(예: 아이디어 필터링 기준) 설명 부족
  
- **Overall (종합)**: 4/5

**총평**: DOLPHIN은 폐쇄 루프 구조와 작업 속성 기반 필터링으로 자동 과학 연구에 의미 있는 기여를 하며 공개 벤치마크에서 경쟁력 있는 결과를 보여주었으나, 평가 범위의 제한성과 디버깅 및 피드백 메커니즘의 정교화 여지가 있어 4점으로 평가된다.

## Related Papers

- 🔄 다른 접근: [[papers/578_Novelseek_When_agent_becomes_the_scientistbuilding_closed-lo/review]] — DOLPHIN과 InternAgent 모두 폐쇄 루프 과학 연구 자동화를 추구하지만 오픈엔드 vs 다중 분야 접근방식이 다르다.
- 🔗 후속 연구: [[papers/794_The_AI_Scientist-v2_Workshop-Level_Automated_Scientific_Disc/review]] — AI Scientist-v2는 DOLPHIN의 폐쇄 루프 연구 프레임워크를 에이전트 기반 트리 서치로 발전시켜 동료 심사까지 포함한다.
- 🏛 기반 연구: [[papers/828_Towards_end-to-end_automation_of_AI_research/review]] — AI 연구의 end-to-end 자동화 연구는 DOLPHIN의 아이디어-실험-피드백 순환 구조의 이론적 토대를 제공한다.
- 🔄 다른 접근: [[papers/578_Novelseek_When_agent_becomes_the_scientistbuilding_closed-lo/review]] — InternAgent와 DOLPHIN 모두 폐쇄 루프 과학 연구 자동화를 추구하지만 다중 분야 vs 오픈엔드 접근방식이 다르다.
- 🔗 후속 연구: [[papers/794_The_AI_Scientist-v2_Workshop-Level_Automated_Scientific_Disc/review]] — AI Scientist-v2는 DOLPHIN의 폐쇄 루프 연구 프레임워크를 에이전트 기반 트리 서치로 발전시켜 동료 심사까지 포함한다.
