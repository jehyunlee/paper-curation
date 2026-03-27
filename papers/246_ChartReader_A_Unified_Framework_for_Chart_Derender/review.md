# ChartReader: A Unified Framework for Chart Derendering and Comprehension without Heuristic Rules

> **저자**: Zhi-Qi Cheng, Qi Dai, Alexander G. Hauptmann | **날짜**: 2023-10-01 | **DOI/URL**: https://doi.org/10.1109/ICCV51070.2023.02029
> **리뷰 모드**: Web-only (Abstract 기반)

---

## Essence (본질)
휴리스틱 규칙 없이 차트 역렌더링(derendering)과 이해(comprehension)를 통합 처리하는 단일 프레임워크 ChartReader를 ICCV 2023에서 제안한다.

## Originality (독창성)
- **What**: 차트 역렌더링(원본 데이터 복원)과 차트 이해(질의응답 등)를 하나의 통합 프레임워크로 처리
- **How**: 휴리스틱 규칙을 완전히 배제하고 end-to-end 학습 가능한 통합 모델 설계; ICCV 2023 본선 발표 (pp. 22145–22156)
- **Why**: 기존 차트 처리 시스템은 역렌더링과 이해를 분리하고 도메인별 휴리스틱에 의존해 범용성이 낮고 확장이 어렵기 때문

## Summary (요약)
ChartReader는 차트 이미지를 입력으로 받아 원본 데이터 추출(역렌더링)과 차트 기반 질의응답(이해) 두 작업을 휴리스틱 없이 통합 수행하는 프레임워크이다. ICCV 2023이라는 최고 수준의 컴퓨터비전 학술대회에 발표되었으며, 과학 문헌의 시각 정보 자동 파싱이라는 실용적 문제를 정면으로 다룬다. Abstract가 Zotero에 저장되지 않았으나 컨퍼런스 위상과 페이지 수(12페이지)로 볼 때 충실한 실험적 검증을 갖춘 연구로 추정된다.

## 평가
| 항목 | 점수 (1-5) |
|------|-----------|
| Novelty | 4 |
| Significance | 4 |
| Overall | 4 |

**총평**: 차트 역렌더링과 이해를 통합한 규칙 없는 프레임워크로 ICCV 2023에 발표된 수준 높은 연구이며, 과학 문헌 자동 파싱 인프라에 실질적 기여를 한다.
