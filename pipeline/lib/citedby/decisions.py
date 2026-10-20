"""OpenAI Decision API — 판정형 질문을 확률로 받는 citedby 의 분류 경로.

Decision API(`client.decisions.create`)는 글을 생성하지 않는다. 입력 하나에
predicate / choice / score 질문을 최대 200개 붙여 보내면 질문마다 **확률**을
돌려준다. 그래서 "이 논문이 주제와 관련 있나" 같은 예/아니오 판정에는 JSON
생성보다 낫다 — 출력 토큰이 0이고, 응답 개수·순서가 질문과 정확히 일치하며,
JSON 파싱 실패가 없다.

근거 문장이 필요한 단계(컬렉션 추천 사유, 논문 연결 설명)에는 쓰지 않는다.
Decision 응답에는 텍스트가 없다.

필요 조건: `openai>=3.35` SDK, `OPENAI_API_KEY`. 지원 모델은 `gpt-6-luna` 하나.
"""
from __future__ import annotations

import json
import logging

logger = logging.getLogger(__name__)

DECISION_MODEL = "gpt-6-luna"
MAX_QUESTIONS = 200
_SCHEMA_VERSION = "citedby-decision-v1"


def decide(input_text: str, questions: list[dict], *, key: str,
           cache_dir=None) -> list[dict] | None:
    """`questions` 에 대한 답 목록(질문 순서 그대로). 실패하면 None.

    답은 SDK 모델의 `model_dump()` — `type` 이 predicate 면 `probability`,
    choice 면 `choice`·`confidence`·`probabilities`, refusal 이면 값이 없다.
    `cache_dir` 를 주면 같은 (입력, 질문) 은 재실행 시 네트워크를 타지 않는다.
    """
    if not key or not questions:
        return None
    if len(questions) > MAX_QUESTIONS:
        raise ValueError(f"Decision API는 요청당 질문 {MAX_QUESTIONS}개까지다 "
                         f"(받음: {len(questions)})")

    def _run():
        from openai import OpenAI
        client = OpenAI(api_key=key, timeout=180.0, max_retries=4)
        resp = client.decisions.create(model=DECISION_MODEL, input=input_text,
                                       questions=questions)
        return [answer.model_dump() for answer in resp.answers]

    try:
        if cache_dir:
            from api._llm import cached_call
            material = json.dumps({"input": input_text, "questions": questions},
                                  ensure_ascii=False, sort_keys=True)
            answers = cached_call(
                cache_dir, material, DECISION_MODEL, _run,
                schema_version=_SCHEMA_VERSION,
                is_complete=lambda r: isinstance(r, list) and len(r) == len(questions))
        else:
            answers = _run()
    except Exception as e:  # noqa: BLE001 — 호출부가 다음 경로로 넘어간다
        logger.warning("Decision API 실패 (%s): %s", DECISION_MODEL, str(e)[:160])
        return None

    if not isinstance(answers, list) or len(answers) != len(questions):
        logger.warning("Decision API 답 개수 불일치: 질문 %d개, 답 %s개",
                       len(questions), len(answers) if isinstance(answers, list) else "?")
        return None
    return answers
