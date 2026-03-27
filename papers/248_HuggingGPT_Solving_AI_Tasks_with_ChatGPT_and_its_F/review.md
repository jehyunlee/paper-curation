# HuggingGPT: Solving AI Tasks with ChatGPT and its Friends in Hugging Face

> **저자**: Yongliang Shen, Kaitao Song, Xu Tan, Dongsheng Li, Weiming Lu, Yueting Zhuang | **날짜**: 2023 | **URL**: https://proceedings.neurips.cc/paper_files/paper/2023/file/77c33e6a367922d003ff102ffb92b658-Paper-Conference.pdf
> **리뷰 모드**: Web-only (Abstract 기반)

---

## Essence (본질)
ChatGPT를 작업 계획자(planner)로, Hugging Face의 다양한 전문 모델들을 실행자(executor)로 활용하여 복잡한 AI 작업을 자동으로 분해·해결하는 HuggingGPT 에이전트 시스템을 제안한다.

## Originality (독창성)
- **What**: ChatGPT가 사용자 요청을 분석해 적절한 Hugging Face 모델을 선택·조합·실행하고 결과를 통합하는 에이전트 프레임워크
- **How**: (1) 작업 계획, (2) 모델 선택, (3) 작업 실행, (4) 응답 생성의 4단계 파이프라인; Hugging Face Hub의 수천 개 모델을 외부 도구로 활용
- **Why**: 단일 LLM은 모든 AI 작업을 처리할 수 없으나, LLM이 전문 모델들의 오케스트레이터 역할을 하면 멀티모달·다중 작업 처리가 가능해짐

## Summary (요약)
HuggingGPT(JARVIS)는 NeurIPS 2023에 발표된 LLM 에이전트 논문으로, ChatGPT가 자연어로 받은 복잡한 요청을 세부 작업으로 분해하고 Hugging Face의 전문화된 모델들을 도구로 호출해 해결하는 시스템이다. 이미지 생성, 음성 인식, 시각적 질의응답 등 이종 AI 작업을 단일 인터페이스로 처리할 수 있음을 보여준다. LLM 에이전트 및 도구 사용(tool-use) 연구의 주요 선구 논문 중 하나로 자리매김하고 있다.

## 평가
| 항목 | 점수 (1-5) |
|------|-----------|
| Novelty | 4 |
| Significance | 5 |
| Overall | 5 |

**총평**: LLM을 AI 모델 오케스트레이터로 활용하는 에이전트 패러다임을 선구적으로 제시한 NeurIPS 2023 논문으로, AI 에이전트 연구의 핵심 참조 문헌이다.
