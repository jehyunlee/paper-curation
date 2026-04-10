 # 연구 대시보드

  ## 고득점 논문 (scisci)
  ```dataview
  TABLE score, essence
  FROM "papers"
  WHERE contains(tags, "topic/scisci") AND score >= 4
  SORT score DESC
  ```

  ## AI & 과학정책 관련
  ```dataview
  TABLE score, essence
  FROM "papers"
  WHERE contains(tags, "cat/AI_and_LLM_in_Science") OR contains(tags, "cat/Science_Policy_and_Funding")
  SORT score DESC
  ```

  ## 인용 분석 관련
  ```dataview
  TABLE score, essence
  FROM "papers"
  WHERE contains(tags, "cat/Citation_and_Impact_Analysis")
  SORT score DESC
  ```