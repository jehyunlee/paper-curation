#!/usr/bin/env python3
"""정리편(총정리) 다이제스트 — 'Dashun Wang 연구 흐름 따라잡기' 1~11강 전체를 되짚고,
우리가 챙겨야 할 핵심 인사이트를 하나의 강의노트로 정리한다.

- 근거: 11강 커리큘럼의 핵심 논문 리뷰(내 코퍼스) + 이미 발송된 강의노트(1~5강 report.md).
- 그림: 지난번에 만든 '전체 논문 그림'(curriculum_map.png)을 상단에 그대로 싣는다.
- 스타일: 기존 11강과 동일한 HTML 템플릿(purple hero · MathJax · figure interleave).
- 발송: 기본은 jehyun.lee@gmail.com 한 명에게 먼저(테스트) → 확인 후 전체 반으로 재발송.

사용:
    PC_AGENT_DIR=docs/_agent/dashun_wang \
    PYTHONUTF8=1 python pipeline/build_summary_lecture.py            # 생성 + jehyun.lee@gmail.com 발송
    ... --build-only                                                # 생성만(메일 없음)
    ... --recipients "a@b.com,c@d.com"                              # 수신자 지정
"""
import argparse
import base64
import os
import re
import sys
from datetime import datetime
from pathlib import Path

PIPE = Path(__file__).resolve().parent
# 레저/산출물 경로는 docs/_agent/dashun_wang (없으면 env 로 넘겨받음)
os.environ.setdefault("PC_AGENT_DIR", str(PIPE.parent / "docs" / "_agent" / "dashun_wang"))
sys.path.insert(0, str(PIPE))

import html as H  # noqa: E402
import agent_lecture_digest as ald  # noqa: E402
from config_loader import get_google_key  # noqa: E402
from google import genai  # noqa: E402
from google.genai import types  # noqa: E402
import usage_log  # noqa: E402

MAP_PNG = ald.AGENT_DIR / "curriculum_map.png"
OUT_HTML = ald.OUTDIR / "lecture_00_summary.html"
OUT_MD = ald.OUTDIR / "lecture_00_summary_report.md"
OUT_MP3 = ald.OUTDIR / "lecture_00_summary.mp3"
OUT_SCRIPT = ald.OUTDIR / "lecture_00_summary_script.txt"


# ── 근거 수집 (11강 전체) ────────────────────────────────────────────────────
def one_liner(L):
    obj = (L.get("objectives") or [""])[0]
    obj = re.sub(r"\s+", " ", obj).strip()
    return obj[:70] + ("…" if len(obj) > 70 else "")


def summary_evidence(led):
    """1~11강 전체를 아우르는 근거 텍스트. 강별 학습목표 + 핵심 논문 리뷰 발췌 +
    (있으면) 이미 발송한 강의노트 발췌."""
    blocks = []
    for L in sorted(led["lectures"], key=lambda x: x["lecture"]):
        n = L["lecture"]
        objs = "\n".join(f"    - {o}" for o in L["objectives"])
        plines = []
        for p in L["papers"]:
            rev = ald.read_review(p["slug"], 900)
            rev = re.sub(r"\s+", " ", rev).strip()
            plines.append(f"  · ({p.get('year','')}) {p['title']}\n      {rev or '(요약 없음)'}")
        report_md = ald.OUTDIR / f"lecture_{n:02d}_report.md"
        note = ""
        if report_md.exists():
            txt = report_md.read_text(encoding="utf-8").strip()
            note = f"\n  [이미 발송한 제{n}강 강의노트 발췌]\n  {txt[:3800]}"
        blocks.append(
            f"### 제{n}강 · {L['title']}\n  학습목표:\n{objs}\n  핵심 논문:\n"
            + "\n".join(plines) + note
        )
    return "\n\n".join(blocks)


# ── 정리편 리포트 합성 (코퍼스 기반, 웹 검색 없음) ──────────────────────────
def synthesize_summary(course, led, evidence):
    total = led["total"]
    arc = "\n".join(
        f"    제{L['lecture']}강 「{L['title']}」 — {one_liner(L)}"
        for L in sorted(led["lectures"], key=lambda x: x["lecture"])
    )
    prompt = (
        f"당신은 '{course}' 심화 강의 시리즈를 이끌어 온 전문 연구자입니다. "
        f"지금까지 제1강부터 제{total}강까지 총 {total}개의 강의를 모두 마쳤고, 오늘은 시리즈를 갈무리하는 "
        f"**정리편(총정리)** 강의노트를 집필합니다.\n\n"
        f"지금까지의 여정:\n{arc}\n\n"
        "이 정리편의 목적은 두 가지입니다.\n"
        "  (1) 지난 11강을 관통하는 큰 흐름을 되짚어 준다 — 개별 강의의 요약 나열이 아니라, "
        "'연구 대상의 확장 축(논문→과학자→팀→기관→생태계→AI·인간)'과 "
        "'데이터·방법론의 확장 축(단일 사례연구→개인 경력→교차 도메인 데이터셋→오픈 인프라→시뮬레이션·LLM)'이라는 "
        "두 축을 따라 Dashun Wang의 연구가 어떻게 진화했는지를 하나의 서사로 엮는다.\n"
        "  (2) 우리가 실제로 챙겨야 할 인사이트를 정리한다 — 강의를 가로지르는 핵심 발견들을 "
        "연구자·연구기관(청중은 KIST 등 연구현장)의 관점에서 '그래서 우리는 무엇을 해야 하는가'로 번역한다.\n\n"
        "작성 지침:\n"
        "- 도입부: 11강 전체를 한 문단으로 조망하며 두 개의 확장 축을 제시하고 시작.\n"
        "- ## 큰 흐름 되짚기: 11강을 5~6개의 '국면(phase)'으로 묶어(예: 인간 동역학·네트워크 → 영향력 정량화 → "
        "경력·팀·실패 → 기관·정책·팬데믹 → 오픈 인프라·AI) 각 국면의 핵심 메시지, 대표 논문(제목·연도), "
        "그리고 '무엇이 반박·정교화되었는가'의 계보 서사를 압축적으로 정리. 논문 단순 나열 금지, 방법론·메시지 축으로 엮기.\n"
        "- ## 우리가 챙겨야 할 인사이트: 강의를 관통하는 통찰을 6~9개의 소제목으로 정리. 각 인사이트마다 "
        "(a) 무엇을 알게 됐나(근거 논문 제목·연도·수치), (b) 왜 중요한가, (c) 연구자/기관은 이를 어떻게 활용할까(실천 함의)를 구체적으로. "
        "예: 소규모 팀의 파괴적 혁신 vs 대규모 팀의 발전적 혁신(CD-index), 핫스트릭의 존재와 무작위성, "
        "초기 실패의 역설과 약한 유대, 피벗 페널티, 정책·과학의 공진화, AI·인간 협업과 벤치마크 착시, Q-모델·랜덤 임팩트 규칙 등.\n"
        "- ## 남는 질문과 다음 지평: 아직 열려 있는 질문(인과 추론의 한계, 재현성, AI가 발견의 주체가 될 때의 평가·저작권 등)과 "
        "이 시리즈 이후 우리가 계속 지켜볼 방향을 짧게.\n"
        "- 인용은 (논문 제목, 연도)로 본문에 명시. 필요하면 수식은 LaTeX($...$)로. 전문가 청중·학술적 톤·마크다운(## 소제목, 단락).\n"
        "- 강의 요약을 나열해 놓은 목차가 아니라, 읽고 나면 '11강을 관통하는 하나의 지도'가 머리에 남는 글이어야 함.\n"
        "- **최소 14,000자 이상**. 메타·머리말 없이 곧바로 정리편 본문으로 시작.\n\n"
        f"=== 근거 (11강 커리큘럼 코퍼스 + 이미 발송한 강의노트) ===\n{evidence}"
    )
    errs = []
    # 1) Gemini gemini-3.1-pro — 원 시리즈(1~11강) 저자 모델
    try:
        client = genai.Client(api_key=get_google_key())
        cfg = types.GenerateContentConfig(temperature=0.55, max_output_tokens=40000)
        resp = client.models.generate_content(model=ald.REPORT_MODEL, contents=prompt, config=cfg)
        try:
            usage_log.record_gemini(resp, ald.REPORT_MODEL)
        except Exception:
            pass
        txt = (resp.text or "").strip()
        if len(txt) >= 3000:
            return txt, ald.REPORT_MODEL
        errs.append(("gemini", f"과소 응답 {len(txt)}자"))
    except Exception as e:
        errs.append(("gemini", str(e)[:140]))

    # 2) OpenRouter/Anthropic Sonnet — 파이프라인 기본 합성 모델
    try:
        from lib.llm_client import get_chat_client, resolve_model
        ac = get_chat_client(timeout=600.0, max_retries=4)
        out = []
        with ac.messages.stream(model=resolve_model("sonnet"), max_tokens=32000,
                                messages=[{"role": "user", "content": prompt}]) as stream:
            for chunk in stream.text_stream:
                out.append(chunk)
        txt = "".join(out).strip()
        if len(txt) >= 3000:
            return txt, resolve_model("sonnet")
        errs.append(("claude", f"과소 응답 {len(txt)}자"))
    except Exception as e:
        errs.append(("claude", str(e)[:140]))

    raise RuntimeError("모든 합성 백엔드 실패: " + " | ".join(f"{p}:{m}" for p, m in errs))


# ── 그림: 강별 대표 논문 1편씩(있는 것만) → figure interleave 용 core ──────────
def representative_core(led):
    core = []
    for L in sorted(led["lectures"], key=lambda x: x["lecture"]):
        for p in L["papers"]:
            d = ald._find_dir(p["slug"])
            if d and (d / "figures").is_dir() and list((d / "figures").glob("fig*.webp")):
                core.append({"slug": p["slug"], "title": p["title"],
                             "year": p.get("year"), "link": ald.paper_link(p["slug"])})
                break
    return core


# ── HTML (기존 11강과 동일 스타일 + 상단 전체 논문 그림) ──────────────────────
def make_summary_html(course, report_md, led, map_uri, figs):
    total = led["total"]
    lec_html = "".join(
        f'<li><b>제{L["lecture"]}강</b> · {H.escape(L["title"])}'
        f'<div class="reason">{H.escape(one_liner(L))}</div></li>'
        for L in sorted(led["lectures"], key=lambda x: x["lecture"])
    )
    map_block = (
        '<div class="card"><h3>🗺️ 전체 연구 지도 — 11강에 등장한 모든 논문</h3>'
        f'<figure class="paper-fig"><img src="{map_uri}" alt="Dashun Wang 전체 연구 지도" loading="lazy">'
        '<figcaption>논문 127편(Wang 그룹 66 · 타 그룹 61) · 1976–2026 · 숫자 1~11은 각 강의 핵심 논문 군집을 표시. '
        '주황=Wang 그룹, 회색=관련 타 그룹, 밝을수록 오래된 논문.</figcaption></figure></div>'
    ) if map_uri else ""
    body = ald._interleave(ald.md_to_html(report_md), figs)
    today = datetime.now().strftime("%Y-%m-%d")
    return f"""<!DOCTYPE html><html lang="ko"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>정리편 — {H.escape(course)} 1~{total}강 총정리</title>
<style>
body{{font-family:'KoPub Dotum',-apple-system,'Noto Sans KR',sans-serif;line-height:1.85;color:#222;max-width:860px;margin:0 auto;padding:2rem 1.4rem;background:#fbfbfd}}
.hero{{background:linear-gradient(135deg,#1a0d2a,#3a1a5c 55%,#6b21a8);color:#fff;border-radius:16px;padding:1.9rem 1.7rem;margin-bottom:1.6rem}}
.hero .kicker{{opacity:.82;font-size:.85rem;font-weight:600}}
.hero h1{{font-size:1.4rem;margin:.35rem 0 .25rem}}
.card{{background:#fff;border:1px solid #eee;border-radius:12px;padding:1.1rem 1.35rem;margin-bottom:1.3rem}}
.card h3{{font-size:.95rem;color:#6B21A8;margin-bottom:.55rem}}
.card ul,.card ol{{margin:0 0 0 1.15rem}} .card li{{margin:.45rem 0}}
.rel{{display:inline-block;font-size:.72rem;font-weight:700;color:#6B21A8;background:#f3e8ff;border-radius:999px;padding:.05rem .5rem;margin-right:.35rem}}
.reason{{font-size:.85rem;color:#666;margin:.15rem 0 .2rem}}
h2{{font-size:1.14rem;color:#6B21A8;margin:1.7rem 0 .6rem;border-bottom:1px solid #eee;padding-bottom:.3rem}}
h3{{font-size:1.02rem;margin:1.1rem 0 .4rem}}
p{{margin:.6rem 0}} a{{color:#7c3aed}}
.foot{{color:#999;font-size:.82rem;border-top:1px solid #eee;margin-top:2rem;padding-top:1rem}}
.paper-fig{{margin:1.3rem 0;text-align:center}}
.paper-fig img{{max-width:min(100%,720px);border:1px solid #e6e6e6;border-radius:10px;box-shadow:0 1px 6px rgba(0,0,0,.07)}}
.paper-fig figcaption{{font-size:.8rem;color:#777;margin-top:.45rem;font-style:italic;line-height:1.5}}
.fig-gallery{{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:1.1rem;margin:1.3rem 0}}
.fig-gallery .paper-fig{{margin:0}}
.fig-gallery .paper-fig img{{max-width:100%}}
@media (max-width:620px){{body{{padding:1.1rem .75rem}}}}
</style>
{ald.MATHJAX_HEAD}
</head><body>
<div class="hero"><div class="kicker">{H.escape(course)} · 정리편 (총정리) · 1~{total}강</div>
<h1>11강을 관통하는 하나의 지도 — 되짚기와 우리가 챙겨야 할 인사이트</h1>
<div style="opacity:.85;font-size:.9rem">{today} · Deeper Research 자동 다이제스트</div></div>
{map_block}
<div class="card"><h3>📚 지난 여정 — 11강 한눈에</h3><ol>{lec_html}</ol></div>
{body}
<div class="foot">Dashun Wang 연구 흐름 따라잡기 · 정리편 · Deeper Research 자동 다이제스트 · Paper Curation</div>
</body></html>"""


# ── Audio Overview (2인·전문가·학술·한국어) — 대본=Claude Sonnet, TTS=Gemini ─────
def _audio_script_part(ac, i, seg, n_seg, labels, rolelines):
    if i == 0:
        pos = "도입부: 아주 짧게 한두 마디로 '11강을 마친 정리편'임을 짚고 바로 본론(장황한 인사 금지)"
    elif i == n_seg - 1:
        pos = "마무리: 11강을 관통하는 핵심 통찰과 우리가 챙길 점을 종합하며 자연스럽게 끝맺음"
    else:
        pos = "앞 대화에 자연스럽게 이어서 진행(재소개·재인사 금지)"
    prompt = (
        f"당신은 전문가 청중용 학술 2인 팟캐스트 대본을 씁니다. 화자는 정확히 2명뿐:\n{rolelines}\n"
        f"각 발화는 '{labels[0]}:' 또는 '{labels[1]}:' 로 시작(콜론+공백). 이 부분은 전체 {n_seg}개 중 {i+1}번째. {pos}.\n"
        "이것은 'Dashun Wang 연구 흐름 따라잡기' 11강 전체를 갈무리하는 **정리편** 팟캐스트입니다. "
        "아래 내용을 **약 3,400~4,000자, 6~8 turn**의 깊이 있는 한국어 대화로 작성. 전체 오디오는 30~40분 목표라 과도한 반복·장황한 요약은 피한다. "
        "방법·수치·연구 계보와 '당시엔 X로 여겨졌으나 후대엔 Y로 밝혀졌다'식 수정 서사를 구체적으로 풀되 청취자 눈높이 비유도 곁들일 것. "
        "라벨 외 머리말·메타·프로그램명 금지.\n\n"
        f"내용:\n{seg}"
    )
    from lib.llm_client import resolve_model as _resolve_model
    resp = ac.messages.create(model=_resolve_model("sonnet"), max_tokens=8000,
                              messages=[{"role": "user", "content": prompt}])
    txt = "".join(b.text for b in resp.content if getattr(b, "type", "") == "text").strip()
    return i, txt


def build_audio(report_text):
    """정리편 Audio Overview. 대본=Claude Sonnet(2인 대화), 음성=Gemini 멀티스피커 TTS."""
    import generate_audio as ga
    import lameenc
    from lib.llm_client import get_chat_client, resolve_model
    from concurrent.futures import ThreadPoolExecutor, as_completed
    lang = "ko"
    roles = ga.ROLES[lang][2]
    labels = [r["label"] for r in roles]
    rolelines = "\n".join(f"- {r['label']}: {r['desc']}" for r in roles)

    paras = [p for p in re.split(r"\n\s*\n", report_text) if p.strip()]
    n_seg = max(5, min(7, len(report_text) // 2600))
    if len(paras) >= n_seg:
        per = -(-len(paras) // n_seg)
        segs = ["\n\n".join(paras[i:i + per]) for i in range(0, len(paras), per)]
    else:
        sz = max(1, -(-len(report_text) // n_seg))
        segs = [report_text[i:i + sz] for i in range(0, len(report_text), sz)]

    ac = get_chat_client(timeout=600.0, max_retries=4)
    scripts = [""] * len(segs)
    print(f"     대본 병렬 생성 {len(segs)} parts ({resolve_model('sonnet')})", flush=True)
    with ThreadPoolExecutor(max_workers=3) as ex:
        futs = {ex.submit(_audio_script_part, ac, i, seg, len(segs), labels, rolelines): i
                for i, seg in enumerate(segs)}
        for fut in as_completed(futs):
            i, t = fut.result()
            scripts[i] = t
            print(f"       대본 {i+1}/{len(segs)} · {len(t):,}자", flush=True)
    script = "\n".join(s for s in scripts if s)
    if not script:
        raise RuntimeError("대본 생성 실패")

    turns = ga.parse_turns(script, labels)
    max_script_chars = 25_000
    if turns and len(script) > max_script_chars:
        reserve = turns[-2:] if len(turns) > 2 else []
        reserve_chars = sum(len(a) + len(b) + 3 for a, b in reserve)
        kept, used = [], 0
        for lab, txt in (turns[:-len(reserve)] if reserve else turns):
            add = len(lab) + len(txt) + 3
            if kept and used + add + reserve_chars > max_script_chars:
                break
            kept.append((lab, txt)); used += add
        if reserve:
            kept.extend(reserve)
        turns = kept
        script = "\n".join(f"{lab}: {txt}" for lab, txt in turns)
        print(f"     대본 길이 상한 적용 · {len(script):,}자", flush=True)

    gc = genai.Client(api_key=get_google_key())
    if turns:
        chunks = ga.chunk_turns(turns, ga.MAX_CHUNK_CHARS)
        cfg = ga.speech_multi(roles)
        prefix = ga.TTS_PREFIX[lang]
        get = lambda k: prefix + chunks[k]
    else:
        chunks = ga.chunk_paragraphs(script, ga.MAX_CHUNK_CHARS)
        cfg = ga.speech_single(roles[0]["voice"])
        get = lambda k: chunks[k]
    print(f"     TTS {len(chunks)} chunks (gemini multi-speaker) ...", flush=True)
    parts = [None] * len(chunks)
    with ThreadPoolExecutor(max_workers=2) as ex:
        futs = {ex.submit(ga.tts_call, gc, get(k), cfg): k for k in range(len(chunks))}
        done = 0
        for fut in as_completed(futs):
            parts[futs[fut]] = fut.result()
            done += 1
            print(f"       [{done}/{len(chunks)}]", flush=True)
    pcm = ga.concat_pcm([p for p in parts if p])
    enc = lameenc.Encoder()
    enc.set_bit_rate(64)
    enc.set_in_sample_rate(ga.SAMPLE_RATE)
    enc.set_channels(1)
    enc.set_quality(2)
    mp3 = enc.encode(pcm) + enc.flush()
    return mp3, script, len(pcm) / 2 / ga.SAMPLE_RATE / 60


# ── 메일 ─────────────────────────────────────────────────────────────────────
def deliver(html, led, recipients, mp3_path=None):
    total = led["total"]
    course = led["course"]
    attachments = [("정리편_Dashun_Wang_총정리.html", html.encode("utf-8"))]
    map_html = ""
    if MAP_PNG.exists():
        attachments.append(("전체연구지도.png", MAP_PNG.read_bytes(), "summary-map"))
        map_html = (
            '<div style="margin:8px 0 16px"><img src="cid:summary-map" alt="전체 연구 지도" '
            'style="width:100%;max-width:760px;border:1px solid #eee;border-radius:12px">'
            '<p style="color:#777;font-size:.82rem;margin:6px 0 0">11강에 등장한 논문 127편(1976–2026)을 한 장에. '
            '숫자 1~11은 각 강의 핵심 군집입니다.</p></div>')
    audio_line = ""
    if mp3_path and Path(mp3_path).exists():
        mp3 = Path(mp3_path).read_bytes()
        if len(mp3) < 28 * 1024 * 1024:                 # Resend 40MB(base64 ~1.37x) 안전선
            attachments.append(("정리편_Audio_Overview.mp3", mp3))
            audio_line = " · Audio Overview(MP3, 2인·전문가·학술 팟캐스트)"
            print(f"     오디오 첨부 {len(mp3)/1048576:.1f}MB")
        else:
            print(f"     ⚠️ 오디오 {len(mp3)/1048576:.1f}MB — 첨부 한도 초과, 제외(OUTDIR 보관)")
    lec_html = "".join(
        f'<li><b>제{L["lecture"]}강</b> · {H.escape(L["title"])}</li>'
        for L in sorted(led["lectures"], key=lambda x: x["lecture"]))
    body = (
        f"<p><b>{H.escape(course)} · 정리편(총정리) · 1~{total}강</b></p>"
        "<h2>11강을 관통하는 하나의 지도 — 되짚기와 우리가 챙겨야 할 인사이트</h2>"
        f"{map_html}"
        "<p>지난 11강을 무사히 마쳤습니다. 이번 정리편은 개별 강의 요약이 아니라, "
        "<b>연구 대상의 확장 축</b>(논문→과학자→팀→기관→생태계→AI·인간)과 "
        "<b>데이터·방법론의 확장 축</b>(사례연구→개인 경력→교차 도메인→오픈 인프라→AI)을 따라 "
        "11강을 하나의 서사로 되짚고, 우리가 실제로 챙겨야 할 인사이트로 번역했습니다.</p>"
        "<p style='background:#faf5ff;border:1px solid #eadcff;border-radius:10px;padding:.8rem 1rem'>"
        "<b>🙏 감사의 말씀</b><br>지난 11강 동안 이 강의 시리즈를 함께 읽고 들어주셔서 진심으로 감사드립니다. "
        "매주 Dashun Wang 그룹의 연구를 따라가며 '과학을 과학으로 들여다보는' 시선을 함께 벼릴 수 있어 뜻깊었습니다. "
        "이 정리편이 지난 여정을 한눈에 되짚고, 각자의 연구 현장에서 오래 곱씹을 인사이트로 남기를 바랍니다. "
        "앞으로도 좋은 논문으로 다시 찾아뵙겠습니다. 고맙습니다.</p>"
        f"<p><b>📚 지난 여정</b></p><ol>{lec_html}</ol>"
        f"<p>첨부: 정리편 강의노트(HTML · 상단 전체 연구 지도 · 강 사이사이 대표 그림) · 전체 연구 지도(PNG){audio_line}.</p>"
        f"<p style='color:#999;font-size:.85rem'>Paper Curation 자동 발송 · {datetime.now().strftime('%Y-%m-%d %H:%M')}</p>")
    subject = f"[정리편/총정리] {course} — 1~{total}강에서 챙길 인사이트"
    st, resp = ald.send_email(recipients, subject, body, attachments)
    print(f"     이메일 {'성공' if st == 200 else '실패'} (status {st}) {resp}  → {recipients}")
    return st == 200


def main():
    ap = argparse.ArgumentParser(description="정리편(총정리) 다이제스트 생성/발송")
    ap.add_argument("--recipients", default="jehyun.lee@gmail.com",
                    help="쉼표구분 수신자 (기본: jehyun.lee@gmail.com 한 명 — 먼저 테스트)")
    ap.add_argument("--build-only", action="store_true", help="생성만, 메일 없음")
    ap.add_argument("--reuse", action="store_true", help="이미 만든 리포트(md) 재사용, Gemini 재호출 안 함")
    ap.add_argument("--all", action="store_true", help="레저(curriculum.json)의 전체 수신자 명단으로 발송")
    ap.add_argument("--no-audio", action="store_true", help="Audio Overview 생성 생략")
    ap.add_argument("--reuse-audio", action="store_true", help="이미 만든 mp3 재사용, TTS 재호출 안 함")
    args = ap.parse_args()

    led = ald.load_ledger()
    course = led["course"]
    total = led["total"]
    ald.OUTDIR.mkdir(parents=True, exist_ok=True)
    print(f"[정리편] {course} · 1~{total}강 총정리")

    if args.reuse and OUT_MD.exists():
        report = OUT_MD.read_text(encoding="utf-8")
        print(f"  리포트 재사용 ({len(report):,}자)")
    else:
        print("  1) 근거 수집 (11강 전체 코퍼스 + 강의노트)")
        evidence = summary_evidence(led)
        print(f"     근거 {len(evidence):,}자")
        print("  2) Deeper Research 정리편 합성 (Gemini → Claude Sonnet fallback)")
        report, used_model = synthesize_summary(course, led, evidence)
        OUT_MD.write_text(report, encoding="utf-8")
        print(f"     리포트 {len(report):,}자 (모델: {used_model}) → {OUT_MD}")

    print("  3) 전체 논문 그림 + 대표 그림 수집")
    map_uri = ""
    if MAP_PNG.exists():
        map_uri = "data:image/png;base64," + base64.b64encode(MAP_PNG.read_bytes()).decode()
        print(f"     전체 연구 지도 {MAP_PNG.stat().st_size/1024:.0f}KB")
    else:
        print(f"     ⚠️ 전체 논문 그림 없음: {MAP_PNG}")
    figs = ald.gather_figures(representative_core(led), per_paper=1, total_cap=9)
    print(f"     대표 그림 {len(figs)}개")

    html = make_summary_html(course, report, led, map_uri, figs)
    OUT_HTML.write_text(html, encoding="utf-8")
    print(f"     HTML {len(html)/1024:.0f}KB → {OUT_HTML}")

    mp3_path = None
    if not args.no_audio:
        if args.reuse_audio and OUT_MP3.exists():
            mp3_path = OUT_MP3
            print(f"  3.5) 오디오 재사용 ({OUT_MP3.stat().st_size/1048576:.1f}MB)")
        else:
            print("  3.5) Audio Overview 생성 (대본 Claude Sonnet · 음성 Gemini 멀티스피커)")
            try:
                mp3, script, mins = build_audio(report)
                OUT_MP3.write_bytes(mp3)
                OUT_SCRIPT.write_text(script, encoding="utf-8")
                mp3_path = OUT_MP3
                print(f"     오디오 {len(mp3)/1048576:.1f}MB · ~{mins:.0f}분 · 대본 {len(script):,}자 → {OUT_MP3}")
            except Exception as e:
                print(f"     ⚠️ 오디오 생성 실패(문서·그림만 발송): {str(e)[:180]}")

    if args.build_only:
        print("[정리편] 생성만 완료(메일 없음).")
        return 0

    if args.all:
        recipients = list(led.get("recipients") or [])
    else:
        recipients = [r.strip() for r in args.recipients.split(",") if r.strip()]
    print(f"  4) 메일 발송 → {recipients}")
    ok = deliver(html, led, recipients, mp3_path)
    print(f"[정리편] {'완료' if ok else '실패'}.")
    return 0 if ok else 1


if __name__ == "__main__":
    from _env_guard import force_py312
    force_py312()
    sys.exit(main())
