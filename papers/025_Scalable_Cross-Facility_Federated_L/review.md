# Scalable Cross-Facility Federated Learning for Scientific Foundation Models on Multiple Supercomputers

## 메타 정보
- **저자**: Yijiang Li, Zilinghan Li, Kyle Chard, Ian Foster, Todd Munson, Ravi Madduri, Kibaek Kim
- **소속**: Argonne National Laboratory (MCS Division, DSL Division), University of Chicago
- **arXiv**: 2603.19544
- **날짜**: 2026-03-20
- **키워드**: federated learning, HPC, cross-facility, scientific foundation model, LLM fine-tuning

---

## 한줄 요약 (Essence)
4개의 미국 DOE 리더십급 슈퍼컴퓨터(Polaris, Aurora, Frontier, Perlmutter)에서 연합학습(FL)을 실행하는 교차 시설 프레임워크를 설계하고, 화학 instruction 데이터셋에서 Llama2-7B를 연합 파인튜닝하여 이기종 HPC 환경에서의 FL 실행 가능성과 알고리즘 선택의 중요성을 실증한 연구.

## 연구 동기 (Motivation)
과학 응용을 위한 AI는 개인정보 보호, 데이터 주권, 데이터 규모 등의 이유로 중앙 집중화할 수 없는 데이터에 대한 대규모 모델 학습이 필요하다. 연합학습(FL)은 원시 데이터 이동 없이 협력 학습을 가능하게 하지만, HPC 환경은 예측 불가능한 작업 스케줄러 큐잉 지연, 이기종 가속기 아키텍처, 시설별 독립적 보안 정책 등 클라우드/기업 환경과 근본적으로 다른 도전을 제기한다. 기존 FL 프레임워크(FATE, OpenFL, NVIDIA FLARE 등)는 이러한 HPC 특유의 제약을 다루지 않는다.

## 주요 성과 (Achievement)
- **4개 DOE 슈퍼컴퓨터에서의 대규모 FL 실증**: 1,700+ GPU를 활용한 64노드/시설 동기 실행 및 2노드/시설 큐 기반 비동기 실행
- **글로벌 모델 성능**: FedAvg로 8라운드 만에 test loss 1.39 -> 0.37 달성, 글로벌 모델이 모든 개별 클라이언트 모델보다 일관되게 우수
- **4개 FL 알고리즘 비교** (FedAvg, FedAsync, FedBuff, FedCompass): 현실적 큐잉 조건에서 FedCompass가 최저 최종 loss(0.4345) 달성, FedAvg 대비 4.5%, FedAsync 대비 19.3% 개선
- **처리량 이질성 정량화**: Aurora(2,100 samples/s)에서 Polaris(250 samples/s)까지 8배 이상 차이, GPU 메모리 용량이 DeepSpeed ZeRO 최적화 전략을 결정하는 핵심 요인
- **통신 비용 분석**: Globus Transfer로 시설 간 모델 전송 속도 특성화, co-location 시설(Aurora, Polaris)이 원격 시설(Perlmutter) 대비 최대 200 MB/s 빠른 전송

## 방법론 (How)
- **프레임워크**: APPFL(Advanced Privacy-Preserving Federated Learning) + Globus Compute(작업 디스패치) + Globus Transfer/ProxyStore(모델 파라미터 전송) + DeepSpeed(분산 학습)
- **과학적 사용 사례**: SMolInstruct 화학 instruction 데이터셋(330만 샘플, 14개 태스크) 기반 Llama2-7B 연합 파인튜닝
- **데이터 분배**: 태스크 그룹 기반 non-IID 분배 - Perlmutter(이름 변환), Polaris(물성 예측), Aurora(화학 반응), Frontier(분자 설명)
- **이중 실험 설계**: (1) 64노드 예약 기반 co-scheduled 동기 실행으로 상한 성능 측정, (2) 2노드 큐 기반 실행으로 현실적 조건 하 알고리즘 비교

## 독창성 (Originality)
- **HPC 환경 특유의 이질성을 체계적으로 정량화한 최초의 교차 시설 FL 연구**: 계산 처리량, 통신 비용, 큐잉 동역학의 세 차원에서 이질성을 분석하고, 이들이 FL 알고리즘 성능에 미치는 영향을 실증
- **스케줄러 인식(scheduler-aware) 알고리즘 설계의 필요성 제기**: 기존 FL 알고리즘이 큐 대기 시간 가변성이나 시설별 스케줄링 정책을 모델링하지 못함을 보이고, 이를 핵심 미해결 과제로 식별
- **3-엔진 아키텍처**: Globus Compute MPI Engine의 한계를 극복하기 위한 클라이언트측/서버측 Globus Compute Engine + MPI Engine의 설계
- Perlmutter의 40GB vs 80GB 구성 비교를 통해 **GPU 메모리가 최적화 전략(ZeRO-3 vs ZeRO-1)을 결정하고, 이것이 처리량에 4배 이상 차이를 만든다**는 실용적 통찰 제공

## 한계점 (Limitation)
- **수렴까지 학습하지 않음**: 8라운드(대규모) / 40 로컬 라운드(소규모)만 실행하여 기능 시연에 초점. 화학 LLM의 최종 성능이나 downstream 태스크 정확도 평가 없음
- **과학적 검증의 깊이 부족**: 화학 instruction 데이터셋을 사용했으나, 생성된 모델의 화학적 정확도(분자 유효성, 반응 예측 정확도 등)에 대한 평가가 전무
- **4개 시설 고정 구성**: 시설 수, 데이터 분배 방식, 노드 수 등의 하이퍼파라미터에 대한 sensitivity analysis가 제한적
- **재현성 제한**: 4개 DOE 슈퍼컴퓨터에 대한 접근 권한이 필요하며, 큐 대기 시간의 비결정적 특성으로 인해 정확한 재현이 어려움
- **프라이버시 보호 기법 미적용**: APPFL이 differential privacy와 secure aggregation을 지원하나, 본 실험에서는 프라이버시 보호 없이 평문 모델 업데이트만 교환

## 총평 (Evaluation)
과학 연구를 위한 연합학습의 인프라적 기반을 다진 중요한 시스템 연구이다. 4개의 서로 다른 아키텍처(NVIDIA A100, Intel Max, AMD MI250X)를 가진 리더십급 슈퍼컴퓨터에서 실제로 FL을 실행하고 성능을 체계적으로 분석한 점에서 높은 실증적 가치를 지닌다. 특히 GPU 메모리 용량이 최적화 전략을 결정하여 처리량에 4배 이상 영향을 미친다는 발견, 그리고 FedCompass가 계산 이질성 적응을 통해 다른 알고리즘을 능가한다는 결과는 실질적으로 유용하다. 다만 화학 LLM의 과학적 성능 평가가 없고, 프라이버시 보호 기법이 미적용된 점에서 "privacy-preserving"이라는 프레임워크 명칭과 실험 내용 사이에 간극이 있다. 향후 scheduler-aware FL 알고리즘과 계층적 집계 전략의 개발로 이어질 수 있는 유망한 연구 방향을 제시한다.

## 평가
| 항목 | 점수 (1-5) |
|------|-----------|
| Novelty | 3 |
| Technical Soundness | 4 |
| Significance | 3 |
| Overall | 3.3 |

**총평**: 4개 슈퍼컴퓨터에서 실제 연합학습을 실증한 인프라 연구로 시스템 설계의 실용적 통찰이 풍부하나 과학적 성능 평가가 부재하다.
