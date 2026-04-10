---
title: "141_Autonomous_robotic_system_with_optical_coherence_tomography"
authors:
  - "Jesse Haworth"
  - "Rishi Biswas"
  - "Justin Opfermann"
  - "Michael Kam"
  - "Yaning Wang"
date: "2024"
doi: "arXiv:2410.07493"
arxiv: ""
score: 4.4
essence: "본 논문은 혈관 문합(vascular anastomosis)을 자율적으로 수행하는 최초의 로봇 시스템인 마이크로 스마트 조직 자율 로봇(µSTAR)을 개발했으며, OCT 기반 실시간 조직 감지와 신경망 기반 봉합 오류 감지를 통해 경험 많은 외과의들과 경쟁 가능한 수준의 성능을 ex vivo 조직에서 달성했다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/Autonomous_Laboratory_Biology"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Gerber et al._2024_Autonomous robotic system with optical coherence tomography guidance for vascular anastomosis.pdf"
---

# Autonomous robotic system with optical coherence tomography guidance for vascular anastomosis

> **저자**: Jesse Haworth, Rishi Biswas, Justin Opfermann, Michael Kam, Yaning Wang, Desire Pantalone, Francis X. Creighton, Robin Yang, Jin U. Kang, Axel Krieger | **날짜**: 2024 | **DOI**: [arXiv:2410.07493](https://arxiv.org/abs/2410.07493)

---

## Essence

![Figure 1](figures/fig1.webp) *그림 1: µSTAR 시스템 개요 - LBR Med 로봇팔, 혈관 위치 결정 시스템(MAPS), OCT 광섬유 및 마이크로카메라 장착 봉합 도구*

본 논문은 혈관 문합(vascular anastomosis)을 자율적으로 수행하는 최초의 로봇 시스템인 마이크로 스마트 조직 자율 로봇(µSTAR)을 개발했으며, OCT 기반 실시간 조직 감지와 신경망 기반 봉합 오류 감지를 통해 경험 많은 외과의들과 경쟁 가능한 수준의 성능을 ex vivo 조직에서 달성했다.

## Motivation

- **Known**: 혈관 문합은 장기 이식과 재건 수술에 필수적이지만, 1mm 이하의 소구경 혈관 작업은 높은 숙련도를 요구하며, 수동 봉합 시 재수술율이 7.9%에 달함. Da Vinci, MUSA, Symani 등의 기존 로봇 시스템은 원격 조종식이거나 자율 기능이 제한적.

- **Gap**: 기존 자율 로봇 시스템들(STAR, SNAP, SRT 등)은 장기(intestinal) 조직 봉합에는 성공했으나, 혈관의 작은 크기(1mm 이하), 복잡한 조직 변형, 높은 정밀도 요구사항 때문에 혈관 문합에 적용되지 못함. STAR의 구조광 영상 시스템은 해상도 부족, MAPS 초기 프로토타입은 실시간 감지 및 자율 조직 조작 불가.

- **Why**: 미국에서 2036년까지 의사 부족이 13,500~86,000명에 달할 것으로 예상되어, 개인 숙련도에 의존하지 않는 자율 시스템의 개발이 시급함.

- **Approach**: (1) OCT 광섬유 센서와 마이크로카메라 통합 봉합 도구 설계, (2) OCT 기반 고도화된 조직 분류 알고리즘, (3) 봉합 오류 자동 감지 신경망, (4) 멀티모달 영상 기반 자율 수술 제어기 및 워크플로우 개발.

## Achievement

![Figure 2](figures/fig2.webp) *그림 2: µSTAR의 봉합 워크플로우 - (A) 오른쪽 혈관에 needle outside-inside 진입, (B) 왼쪽 혈관에 inside-outside 진출, (C) 완성된 문합 봉합*

1. **첫 자율 혈관 문합 달성**: 실제 조직(ex vivo)에서 혈관 문합을 자율적으로 수행한 최초의 로봇 시스템 개발. 90%의 봉합을 인간 개입 없이 완료.

2. **수술의 정확성과 일관성 입증**: 누출 압력(leak pressure), 관강 감소(lumen reduction), 봉합 배치 변동성(suture placement variation) 측면에서 경험 많은 외과의들과 동등한 수준의 성능 달성.

3. **실시간 다중 센싱 기술**: OCT 기반 submillimeter 수준의 조직 변형 감지 및 마이크로카메라를 통한 봉합 품질 모니터링 통합.

4. **자동 오류 감지 및 보정**: 신경망 기반으로 놓친 봉합(missed suture)을 자율적으로 식별, 수정, 검증하는 기능으로 기존 자율 시스템의 한계 극복.

## How

![Figure 4](figures/fig4.webp) *그림 4: µSTAR 시스템 소프트웨어 아키텍처 - 다중 센서 데이터 통합 및 실시간 제어 흐름도*

**하드웨어 구성:**
- LBR Med 7-DOF (7자유도) 의료용 로봇팔 (KUKA)
- 수정된 Endo360 복강경 봉합 도구: 고정된 원형 경로로 곡선 바늘 구동
- 통합 OCT 시스템: 단일모드 광섬유(1060XP), 고속 소인(swept-source) OEM 엔진(AXSUN), 100kHz 깊이 프로필 획득
- 마이크로카메라(OV6946, OmniVision): 봉합 부위의 사전/사후 영상 캡처
- MAPS(Microvascular Anastomosis Positioning System): 혈관 정밀 회전 조작 및 고정

**제어 및 통신:**
- LBR Med와 호스트 컴퓨터: LAN 기반 조정
- 봉합 도구 제어: CAN (Controlled Area Network)
- OCT 데이터: TPS (Transaction Processing System) 연결
- 카메라 영상: Decklink Blackmagic Frame Grabber를 통한 저지연 전송

**핵심 알고리즘:**
- OCT 기반 조직 분류(tissue classification): 재료 유형 구분 및 봉합 깊이 정확성 향상
- 신경망 기반 놓친 봉합 감지: 봉합 실패 자동 식별 및 보정
- 자율 수술 제어기(autonomous surgical controller): 조직 조작 및 멀티모달 영상 기반 end-to-end 워크플로우

**임상 워크플로우 에뮬레이션:**
- 전통적 수동 봉합의 임프린터 클램프 방식을 MAPS 시스템으로 구현
- 혈관을 정밀하게 회전시켜 모든 측면에 접근 가능하게 하면서 과도한 토크 최소화

## Originality

- **첫 자율 혈관 봉합 로봇**: 기존 STAR, SNAP, SRT 등의 자율 시스템이 장기 조직에만 성공한 것과 달리, 실제 혈관 조직에서 자율 문합 달성.

- **OCT 기반 실시간 조직 감지**: 구조광(structured light) 대비 submillimeter 조직 변형까지 감지 가능한 고해상도 OCT 센서 통합. STAR의 단순 계획 업데이트 방식 대비 mm 수준의 실시간 오류 보정.

- **신경망 기반 오류 감지**: 자율 수술 시스템으로서 봉합 실패를 능동적으로 감지하고 자동 보정하는 메커니즘은 혁신적. 기존 시스템은 사후 검증만 가능.

- **멀티모달 센싱 통합**: OCT(깊이/재료 분석) + 마이크로카메라(품질 검증)의 보완적 센싱으로 종합적 조직 이해 제공.

## Limitation & Further Study

- **제한사항**:
  - ex vivo 조직 연구만 수행. 생리적 맥동, 혈류, 체온 등 in vivo 환경 미포함
  - 소수 표본(세부 통계 제시 부족) - "경험 많은 외과의와 동등"이라는 정성적 비교
  - OCT 신호의 조직 유형별 신뢰도 편차 가능성
  - 다양한 혈관 크기, 재료(동맥/정맥) 범위 제한 가능
  - MAPS 시스템의 회전 범위와 토크 한계로 인한 복잡한 혈관 기하학 대응 미흡

- **후속 연구 방향**:
  - In vivo 동물 모델(돼지, 토끼) 진행
  - 통계적으로 충분한 임상 데이터 수집 및 surgeon 비교 강화
  - OCT 센서의 다양한 혈관 타입(심근, 관상동맥, 정맥 등)에 대한 분류 정확도 향상
  - 더 큰 혈관(>2mm)으로의 확장
  - 실시간 혈류 감지 및 혈전 형성 예측 알고리즘 개발
  - 임상 적용 전 FDA 허가 취득 및 안전성 장기 추적


## Evaluation

- Novelty: 5/5
- Technical Soundness: 4/5
- Significance: 4.5/5
- Clarity: 4/5
- Overall: 4.4/5

**총평**: 본 논문은 혈관 문합이라는 고도의 정밀성을 요구하는 수술 영역에서 최초로 자율 로봇 시스템을 성공적으로 구현한 획기적 업적이다. OCT 기반 실시간 센싱과 신경망 기반 오류 감지라는 기술적 혁신이 돋보이며, ex vivo 실험에서 숙련 외과의와 동등한 성능을 입증했다는 점은 높이 평가할 만하다. 다만, 임상 적용을 위해서는 체계적인 in vivo 동물 실험, 통계적으로 충분한 표본 규모, 알고리즘의 투명성 향상이 필수적이다.

## Related Papers

- 🔄 다른 접근: [[papers/745_Self-driving_laboratories_to_autonomously_navigate_the_prote/review]] — 의료 수술과 생화학 실험이라는 서로 다른 영역에서 자율 로봇 시스템의 구현 방식을 비교한다.
- 🔗 후속 연구: [[papers/133_Automating_quantum_computing_laboratory_experiments_with_an/review]] — 의료용 자율 로봇을 양자 컴퓨팅 실험 자동화로 확장하여 더 넓은 과학 실험 영역을 포괄한다.
- 🏛 기반 연구: [[papers/310_Embodied_Science_Closing_the_Discovery_Loop_with_Agentic_Emb/review]] — 체현된 과학 발견의 구체적 구현 사례로서 물리적 실험과 AI의 결합 가능성을 실증한다.
- 🔗 후속 연구: [[papers/084_Ai-driven_robotics_for_free-space_optics/review]] — 광학 실험의 로봇 자동화가 OCT를 통한 자율 로봇 시스템으로 확장 가능합니다.
- 🔄 다른 접근: [[papers/745_Self-driving_laboratories_to_autonomously_navigate_the_prote/review]] — 생명과학과 의료 분야에서 각각 단백질 공학과 수술 로봇이라는 서로 다른 자율 실험실 구현을 보여준다.
- 🧪 응용 사례: [[papers/310_Embodied_Science_Closing_the_Discovery_Loop_with_Agentic_Emb/review]] — 광학 코히런스 단층촬영을 사용한 자율 로봇 시스템은 Embodied Science 패러다임의 구체적인 실현 사례다.
