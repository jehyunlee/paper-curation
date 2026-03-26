# Productivity Assessment of Neural Code Completion

## 메타 정보
- **저자**: Albert Ziegler, Eirini Kalliamvakou, X. Alice Li, Andrew Rice, Devon Rifkin, Shawn Simister, Ganesh Sittampalam, Edward Aftandilian
- **출판**: MAPS 2022 (ACM SIGPLAN International Symposium on Machine Programming)
- **DOI**: [10.1145/3520312.3534864](https://doi.org/10.1145/3520312.3534864)

---

## Essence (본질)
GitHub Copilot 사용자의 **체감 생산성(perceived productivity)**과 실제 사용 지표 간의 관계를 분석한 사례 연구이다. 2,631명의 설문 응답과 IDE 텔레메트리 데이터를 매칭하여, 제안 **수락률(acceptance rate)**이 코드의 지속성(persistence)이나 기여량 등 더 정교한 지표보다 체감 생산성을 더 잘 예측한다는 것을 발견했다.

## Motivation (동기)
신경망 기반 코드 완성 시스템(GitHub Copilot, Kite, TabNine 등)이 개발자 생산성을 높인다고 표방하지만, 이를 직접 측정하기 어렵다. 오프라인 평가(HumanEval 등)와 실제 IDE 사용 간에는 상당한 괴리가 있으며(예: IntelliCode의 Recall@5가 오프라인 90%에서 온라인 70%로 하락), 작업 완료 시간 같은 전통적 생산성 지표는 AI 코딩 도구의 이점을 충분히 포착하지 못한다. 사용자가 느끼는 생산성을 객관적 사용 데이터로 설명할 수 있는 지표를 찾는 것이 필요했다.

## Achievement (성과)
- **핵심 발견**: 수락률(accepted_per_shown, 평균 27%)이 체감 생산성과 가장 높은 상관관계 (Pearson r=0.24, p<0.0001)
- 지속성 지표(30초~600초 후 코드 변경 여부)는 수락률보다 낮은 상관관계 -- 짧은 기간의 지속성이 긴 기간보다 약간 나음
- PLS 회귀에서 첫 번째 성분(43.2% 설명)은 모든 지표의 양의 기여, 두 번째 성분(13.1%)은 수락률 vs 변경률 이분법 포착
- 수락률에 추가로 shown_per_hour, accepted_char_per_hour 등을 결합하면 예측력 향상
- **프로그래밍 언어별 차이**: Python, JavaScript가 TypeScript보다 높은 수락률 -- 비정적 타입 언어에서 신경망 도구의 상대적 강점 시사
- **시간 패턴 발견**: 주중 근무시간(21.2%) < 비근무시간(23%) < 주말(23.5%) 수락률, 단 이는 시간대 자체가 아닌 **사용자의 평소 활동 시간대** 여부에 의해 결정됨
- 평균 DCPU(일별 수락 완성 수) 31회 이상

## How (방법론)
1. **사용 지표 수집**: GitHub Copilot IDE 플러그인에서 완성 퍼널 이벤트 기록 (기회 -> 표시 -> 수락 -> 지속 여부 at 30/120/300/600초)
2. **생산성 설문**: SPACE 프레임워크 기반 (Satisfaction, Performance, Communication, Efficiency) 4개 차원 + 전반적 생산성 포함 12개 Likert 문항, 17,420명에게 발송하여 2,047명 매칭 가능 응답 수집
3. **분석**:
   - Pearson 상관계수 + F-통계 p값으로 개별 지표와 체감 생산성 간 관계 분석
   - PLS(Projection on Latent Structures) 회귀로 다중공선성 하에서 지표 결합 분석
   - 증분적 피처 선택(incremental feature selection)으로 지표 순위화
   - 시간대/요일별 수락률 패턴 분석 (부트스트랩 재표본)

## Originality (독창성)
- 코드 제안 도구에서 **사용 지표와 개발자 생산성/만족도 간 명확한 연결**을 확립한 최초의 연구
- 수락 이후의 **지속성(persistence)** 지표를 도입하여 수락률과 비교 -- 직관에 반하는 결과 제시
- SPACE 프레임워크를 AI 코딩 도구 평가에 최초 적용
- "코딩은 타이핑이 아니다" -- 유용한 템플릿으로서의 제안이 완벽한 코드 자동 생성보다 더 가치 있을 수 있다는 통찰
- IDE 내 코드 제안을 **챗봇과의 대화**에 비유하는 새로운 관점 제시
- 데이터셋 공개 (https://github.com/wunderalbert/prod-neural-materials)

## Limitation & Further Study (한계 및 후속 연구)
- **상관관계만 확인**: 인과관계 미확립 -- 수락률이 높아서 생산적인지, 생산적인 사용자가 수락률이 높은지 구분 불가
- **낮은 설명력**: 최고 지표(수락률)도 Pearson r=0.24로 상당한 미설명 분산 존재
- **체감 vs 실제 생산성**: 체감 생산성이 실제 작업 완료 시간 단축을 보장하지 않음 (선행 연구에서 확인)
- **단일 시스템**: GitHub Copilot(OpenAI Codex 기반)만 분석 -- 다른 엔진, UI, 지연 시간에서 결과가 달라질 수 있음
- **대리 지표 최적화 위험**: 수락률만 최적화하면 제안을 분할하는 등 실제 가치 없는 개선이 가능
- **설문 편향**: 커뮤니케이션 수신에 동의한 사용자만 대상, 자기선택 편향 가능
- 후속 연구: 챗봇 평가 방법론 차용, 대화적 코드 생성 품질 평가, 다중 시스템 비교

## Evaluation (평가)
| 항목 | 점수 (1-10) | 비고 |
|------|:-----------:|------|
| 참신성 (Novelty) | 7 | 사용 지표-체감 생산성 연결 최초 확립, 지속성 지표 도입 |
| 기술적 완성도 (Soundness) | 7 | 대규모 데이터(2,047명), PLS 회귀 등 체계적 분석, 다만 설명력 한계 |
| 유의미성 (Significance) | 8 | AI 코딩 도구 평가 및 제품 지표 설계에 실질적 영향 |
| 재현성 (Reproducibility) | 7 | 집계 데이터 공개, 다만 원시 텔레메트리 비공개 |
| 종합 (Overall) | 7 | AI 코드 완성 도구의 가치 측정 방법론에 대한 실용적이고 통찰력 있는 산업 연구 |
