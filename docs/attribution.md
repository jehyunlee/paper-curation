# 서지 확정 — 누가 어디 소속인가

![저자↔기관 확정 파이프라인](../attribution_workflow.png)

> 🐱 **열 마리 고양이가 순서대로 시도하고, 사서 고양이가 전부 검문합니다.**

"AI4S에서 가장 활발한 기관 20곳과 그곳의 우수 연구자"를 코퍼스로 답하려면 두
가지가 필요하다. **논문이 어떤 기관을 달고 있는가**는 세기 쉽지만, **저자를 그
기관 중 하나에 귀속시키는 것**은 바이라인의 위첨자를 읽어야 한다. 후자가 안 되면
기관별 연구자 순위에 **그 기관에 있던 적 없는 사람**이 올라온다.

## 근거 사다리 — 위에서 실패해야 아래를 시도한다

출처는 "그 소속을 얼마나 직접 말하는가" 순으로 배열돼 있다. 위 칸이 답을 내면
아래 칸은 아예 실행되지 않고, 모든 행에는 **어느 칸이 만들었는지** 태그가 붙는다.

|칸|출처|무엇을 읽나|
|---|---|---|
|1|`openalex`|출판사가 기탁한 저자별 소속 (ROR 기반)|
|2|`scopus`|같은 응답 안의 `authors.author[].affiliation`|
|3|`pdf.byline-marker`|`1` `a` `♣` `α` 위첨자를 소속 블록과 대응|
|4|`pdf.stacked-byline`|이름 아래에 소속이 쌓인 다단 조판|
|5|`pdf.inline-affiliation`|`NAME, Institution, Country` (ACM)|
|6|`pdf.author-information`|문서 뒤 `AUTHOR INFORMATION` 블록 (ACS)|
|7|`pdf.shared-byline`|마커가 없으면 = 전원이 공유한다는 진술|
|8|`pdf.sole-author`|저자가 한 명이면 모든 소속이 그 사람 것|
|9|`pdf.sole-affiliation`|기관이 하나면 모호함이 없음|
|10|`llm.byline`|렌더링한 1페이지를 읽음 — 나머지가 전부 실패했을 때|

10번은 마지막이자 가장 넓다. 후행 마커·그리스 문자·이메일 대체·좁은 각주가
렌더링된 페이지에서는 그냥 보이기 때문이다. 열두 번의 레이아웃 수정으로 85.8%
까지 온 뒤, 이 한 칸이 **54편을 한 번에** 풀었다.

## 사서 고양이 — 모든 것이 통과하는 단 하나의 관문

**어떤 출처도 기관을 직접 쓰지 못한다.** 반환된 소속 문자열은 예외 없이 *그 논문
자신의* 기관 행과 토큰 대조를 통과해야 하고, 고른 행의 정식 명칭이 그 문자열과
무관하면 거부된다.

이것이 LLM을 안전하게 쓰는 이유이기도 하다. 모델은 **추출기일 뿐 권위가 아니다** —
지어낸 기관은 매칭할 상대가 없어 DB에 들어오지 못한다.

## ROR과 명단

기관 링크의 **89.6%가 ROR로 정체성이 확정**된다. 나머지는 세 부류이고
`pipeline/data/institution_registry.json` 이 그것만 담는다.

- **상위 그룹** — ROR이 `Nvidia (United States)` 와 `(United Kingdom)` 을 가진 채
  둘을 잇는 간선을 주지 않는다(Google·Microsoft 와 달리). 국가를 골라 하나로
  강제하지 않고 **상위만 공유**시킨다.
- **정식 표기** — `Shanghai Innovation Institute`(2025 설립), `Galbot` 처럼 ROR이
  아직 없는 곳의 표기를 통일한다.
- **제외** — `Independent Researcher`(41편)는 기관이 아니라 "소속이 없다"는 진술이다.

```bash
python pipeline/audit_institution_names.py            # 미해결을 논문 수 순으로
python pipeline/audit_institution_names.py --propose  # 명단 초안 (사람이 결정)
```

## 미해결은 답이 아니다

마커를 읽을 수 없는 다기관 논문은 전원×전기관으로 연결되고 `pdf.unmarked-multi`
로 표시된다. **리포트는 이 등급을 세지 않는다.** 세면 그 기관에 있던 적 없는
사람이 순위에 오르기 때문이다. 그림에서 회색 고양이가 줄 밖에 격리돼 있는 이유다.

## 두 게이트

|도구|무엇을 막나|
|---|---|
|`check_attribution_regression.py`|파서를 넓히다 다른 데를 좁히는 것. 논문 단위로 스냅샷을 떠 **손실·획득·재분류를 따로** 보고한다. 총계로는 "신규 40 / 손실 40"이 변화 0으로 보인다|
|`check_attribution_accuracy.py`|두 출처가 **공통점 없는 기관**을 말하는 쌍을 뽑아 원문과 대조|

회귀 검사가 실제로 막은 것들: 마커 알파벳을 발견된 문자로만 제한(회귀 330),
소속 블록을 고정 기호로 파싱(125), 근거 없는 200자 상한(116).

### 일치율은 보고하지 않는다

OpenAlex 대비 일치율을 내려 했으나 **지표로 쓸 수 없다.** 겸직과 입도 차이 때문이다.

```
Ming Y. Lu   OpenAlex: Brigham and Women's Hospital, Mass General, MIT
             PDF     : Broad Institute, Harvard Medical School   ← 양쪽 다 맞음
Gang Huang   OpenAlex: Peking University
             PDF     : National Key Laboratory of Data Space …   ← 후자가 전자 산하
```

대신 **공통점이 없는 쌍만** 뽑아 국가 불일치 순으로 정렬하고, 원문 front matter로
어느 쪽이 맞는지 판정한다. 272쌍 전수 판정 결과:

|판정|건수|의미|
|---|---:|---|
|`pdf-supported`|122 (44.9%)|원문이 파서 쪽을 담고 있음 → **외부 기탁 오류**|
|`both-present`|101 (37.1%)|둘 다 원문에 있음 → 겸직, 오류 아님|
|`neither-present`|27 (9.9%)|원문으로 판정 불가|
|`openalex-supported`|22 (8.1%)|**우리 파서 오류** — 실제 검토 대상|

**외부 기탁이 우리 파서보다 5.5배 자주 틀린다.** OpenAlex 는 `1Rutgers University`
가 적힌 논문에 네덜란드의 `Rutgers Sexual and Reproductive Health and Rights` 를
붙였다. 이 목록의 실질적 가치는 파서 버그가 아니라 **외부 오염을 찾는 데** 있다.

## 정확도는 표본 수동 검증으로만 확인된다

|검증|결과|
|---|---|
|LLM 판독 vs 마커 파서 (30편, 70쌍)|88.6% 일치, 불일치 8건 중 2건은 파서가 틀림|
|`shared-byline` 수동 검토 (16편)|4편 오류 발견 → 규칙 수정|
|국가 불일치 272쌍 원문 대조|파서 오류 8.1%|

## 현재 수치

|지표|값|
|---|---:|
|기관이 붙은 논문|3,758 / 4,196 (89.6%)|
|ROR로 확정된 기관 링크|11,839 / 13,208 (89.6%)|
|저자↔기관 근거 확정 논문|3,628 (86.5%)|
|신뢰 링크|24,449건|
|추정 링크 (질의 제외)|8,360건|

## 실행

```bash
# 전량 재계산 — 저장된 행은 여러 파서 세대가 뒤섞여 있을 수 있다
python pipeline/build_bibliography_db.py --recompute-author-institutions

# 나머지를 렌더링한 1페이지로 읽기
python pipeline/extract_byline_llm.py --validate --limit 30   # 먼저 채점
python pipeline/extract_byline_llm.py --unresolved --execute

# 남은 것의 원인 분류
python pipeline/audit_author_attribution.py
python pipeline/audit_author_attribution.py --stage D --limit 5

# 그림 다시 그리기 (수치는 DB 에서 읽는다)
python pipeline/generate_attribution_diagram.py --style cat
```

## 결과물

```bash
python pipeline/report_field_leaders.py --topic ai4s --top 20
```

`reports/build/ai4s_field_leaders.md` — 기관 20곳과 각 기관의 대표 연구자.
근거가 확정된 링크만 세고, 커버리지를 함께 출력한다. 일부만 수집된 지표로 순위를
매기면 **수집된 논문이 먼저 올라올 뿐**이기 때문이다.
