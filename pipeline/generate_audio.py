"""논문 리뷰(review.md) → Audio Overview (팟캐스트형 오디오) — CLI 폴백.

리뷰 페이지의 브라우저-직접 생성(Audio Overview 버튼)과 동일한 보이스·연관논문
컨텍스트·프롬프트·멀티스피커 prefix 를 사용한다. 브라우저 대신 배치/디버깅용으로
임의 슬러그를 처리하거나, 로컬 키가 없는 셸 환경에서 쓰는 용도.

사용 예:
    PYTHONUTF8=1 python pipeline/generate_audio.py --slug 514
    python pipeline/generate_audio.py --slug 514 --speakers 2 --length 20 --language en
    python pipeline/generate_audio.py --slug 514 --speakers 3 --tone lively
    python pipeline/generate_audio.py --slug 514 --focus "방법론의 한계" --speed 1.15

화자 수: 1(내레이터) / 2(전문가+리포터, 멀티스피커 1콜 청크) / 3(per-turn 합성).
길이: 10 / 20 / 30 분. 언어: ko / en (기본 ko).
기본 구성 방향: 논문 originality 중심 + '같이 보면 좋은 논문' 연관성 엮기.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from google import genai
from google.genai import types

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from config_loader import PAPERS_DIR as _PAPERS_DIR, get_google_key  # noqa: E402
import usage_log  # noqa: E402

PAPERS = Path(_PAPERS_DIR)
DOCS = PAPERS.parent

SCRIPT_MODEL = "gemini-3.1-pro-preview"
TTS_MODEL = "gemini-2.5-flash-preview-tts"
SAMPLE_RATE = 24_000
MAX_CHUNK_CHARS = 2200
TTS_WORKERS = 4
SILENCE_MS = 200
MP3_BITRATE_KBPS = 128

DEFAULT_DIRECTION = {
    "ko": "논문의 originality(독창성)를 중심으로, '같이 보면 좋은 논문'들과의 연관성(예: 장단점 비교, 대조, 후속, 보완 등)을 엮어서 전체 맥락을 파악할 수 있도록 구성한다.",
    "en": "Center the narrative on the paper's originality, weaving in how it relates to the recommended related papers (e.g., pros/cons comparison, contrast, follow-up, complement) so the listener grasps the overall context.",
}

# Mirror review_to_html.py ROLES so CLI output matches the in-browser feature.
ROLES = {
    "ko": {
        1: [{"label": "내레이터", "voice": "Kore", "desc": "차분하고 명료한 1인 내레이터"}],
        2: [{"label": "전문가", "voice": "Kore", "desc": "과학기술 전문가(여성). 논문의 originality와 기술적 핵심을 정확하고 깊이 있게 설명한다."},
            {"label": "리포터", "voice": "Puck", "desc": "논문의 파급효과와 의의에 관심이 많은 진행자(남성). 청취자 눈높이에서 질문하고, 같이 보면 좋은 논문들과의 관계를 짚으며 맥락을 넓힌다."}],
        3: [{"label": "사회자", "voice": "Leda", "desc": "토론을 이끌고 핵심을 정리하는 진행자"},
            {"label": "전문가", "voice": "Kore", "desc": "과학기술 전문가(여성). originality와 기술 핵심을 설명한다."},
            {"label": "리포터", "voice": "Algieba", "desc": "파급효과와 연관 논문에 관심 많은 패널(남성)."}],
    },
    "en": {
        1: [{"label": "Narrator", "voice": "Kore", "desc": "a calm, clear solo narrator"}],
        2: [{"label": "Expert", "voice": "Kore", "desc": "a science-and-technology expert (female) who explains the paper's originality and technical core precisely and in depth"},
            {"label": "Reporter", "voice": "Puck", "desc": "a host (male) keen on the paper's impact and significance, asking listener-level questions and connecting it to the recommended related papers"}],
        3: [{"label": "Host", "voice": "Leda", "desc": "a host who drives the discussion and sums up the key points"},
            {"label": "Expert", "voice": "Kore", "desc": "a science-and-technology expert (female) explaining originality and the technical core"},
            {"label": "Reporter", "voice": "Algieba", "desc": "a panelist (male) keen on impact and related papers"}],
    },
}
AUDIENCE = {
    "ko": {"general": "일반 대중", "student": "대학생·대학원생", "expert": "해당 분야 전문가"},
    "en": {"general": "a general audience", "student": "undergraduate and graduate students", "expert": "domain experts"},
}
TONE = {
    "ko": {"friendly": "친근하지만 전문적이고, 청취자에게 말 걸 듯이", "academic": "차분하고 학술적이며 정확하게", "lively": "활기차고 박진감 있게"},
    "en": {"friendly": "warm yet professional, speaking directly to the listener", "academic": "calm, academic and precise", "lively": "lively and energetic"},
}
# Gemini multi-speaker TTS needs a style instruction or it answers as text.
TTS_PREFIX = {"ko": "다음 대화를 자연스럽고 생동감 있게 읽어줘:\n",
              "en": "Read the following conversation naturally and with energy:\n"}


def resolve_slug(token: str) -> str:
    """Accept '514', '0514', or a slug prefix and return the full slug dir name."""
    cand = [d.name for d in PAPERS.iterdir()
            if d.is_dir() and re.match(r"^\d{3,}_", d.name)]
    if token in cand:
        return token
    if token.isdigit():
        want = int(token)
        for name in sorted(cand):
            m = re.match(r"^(\d+)_", name)
            if m and int(m.group(1)) == want:
                return name
    matches = [n for n in cand if n.startswith(token)]
    if len(matches) == 1:
        return matches[0]
    raise SystemExit(f"슬러그 '{token}' 를 특정할 수 없습니다 (matches={matches[:5]})")


def load_connections(slug: str) -> list[dict]:
    """Outgoing + incoming related-paper connections for this slug, with titles."""
    conns_all: dict[str, list] = {}
    for cpath in DOCS.glob("*/_paper_connections.json"):
        try:
            conns_all.update(json.loads(cpath.read_text(encoding="utf-8")))
        except Exception:
            pass
    titles = {}
    idx = PAPERS / "_papers_index.json"
    if idx.exists():
        for p in json.loads(idx.read_text(encoding="utf-8")):
            titles[p["slug"]] = p.get("title", p["slug"])
    labels = {"alternative": "다른 접근", "extension": "후속 연구", "foundation": "기반 연구",
              "counterpoint": "반론/비판", "application": "응용 사례"}
    out = []
    for c in conns_all.get(slug, []):
        out.append({"title": titles.get(c.get("slug", ""), c.get("slug", "")),
                    "relation": labels.get(c.get("relation", ""), c.get("relation", "")),
                    "reason": c.get("reason", "")})
    for src, cs in conns_all.items():
        if src == slug:
            continue
        for c in cs:
            if c.get("slug") == slug:
                out.append({"title": titles.get(src, src),
                            "relation": labels.get(c.get("relation", ""), c.get("relation", "")),
                            "reason": c.get("reason", "")})
    return out


def length_guide(minutes: int, lang: str) -> str:
    # Calibrated from measured Gemini TTS rate (~560 ko chars/min) and over-asked
    # ~1.3x because the model under-fills long length targets. ko≈730 chars/min.
    if lang == "en":
        return (f"about {minutes} minutes — write at least {minutes * 200} words; "
                "fill the entire length with substantive discussion and do not wrap up early")
    return (f"약 {minutes}분 분량 — 한국어로 최소 {minutes * 730}자 이상 작성하고, "
            "내용을 충분히 깊게 다뤄 분량을 끝까지 채울 것(중간에 서둘러 마무리하지 말 것)")


def connections_text(conns: list[dict], lang: str) -> str:
    if not conns:
        return ""
    head = ("Recommended related papers (weave these into the context):" if lang == "en"
            else "같이 보면 좋은 논문 (맥락에 엮을 것):")
    lines = [f"- [{c['relation']}] {c['title']}" + (f" — {c['reason']}" if c["reason"] else "")
             for c in conns]
    return head + "\n" + "\n".join(lines)


def build_prompt(review: str, conns: list[dict], speakers: int, lang: str,
                 audience: str, minutes: int, tone_key: str, focus: str,
                 direction: str) -> str:
    roles = ROLES[lang][speakers]
    tone = TONE[lang][tone_key]
    aud = AUDIENCE[lang][audience]
    length = length_guide(minutes, lang)
    conns_blk = connections_text(conns, lang)

    if speakers == 1:
        fmt = ("- Format: a single narrator from start to finish; output narration text only, no speaker labels.\n"
               "- Do not invent a show name or introduce yourself by name; dive straight into the content."
               if lang == "en" else
               "- 형식: 한 명의 내레이터가 처음부터 끝까지 진행. 화자 라벨 없이 순수 내레이션 텍스트만 출력.\n"
               "- 프로그램 이름이나 진행자 이름을 지어내 자기소개하지 말고, 곧바로 내용으로 들어갈 것.")
    else:
        role_lines = "\n".join(f"- {r['label']}: {r['desc']}" for r in roles)
        labels = ", ".join(r["label"] for r in roles)
        if lang == "en":
            fmt = (f"- Format: a {speakers}-person conversational podcast.\n{role_lines}\n"
                   f"- Begin every utterance with exactly one of these labels followed by ': ' — {labels}\n"
                   "- Natural turn-taking; no one speaks more than ~5 sentences in a row.\n"
                   f"- Exactly {speakers} speakers — never add a third speaker, narrator, or host.\n"
                   "- The labels are voice tags only: speakers must NOT address each other by these labels or by any "
                   "personal name, must NOT introduce themselves, and must NOT invent a show or host name. "
                   "Dive straight into the substance.")
        else:
            fmt = (f"- 형식: {speakers}인 대화형 팟캐스트.\n{role_lines}\n"
                   f"- 각 발화는 반드시 다음 라벨 중 하나로 시작하고 콜론+공백을 붙일 것 — {labels}\n"
                   "- 자연스러운 turn-taking, 한 명이 5문장 이상 연속 독점 금지.\n"
                   f"- 등장인물은 정확히 {speakers}명뿐 — 제3의 화자·내레이터·해설자를 절대 추가하지 말 것.\n"
                   "- 라벨은 음성 구분용 표시일 뿐이다. 대사 속에서 서로를 그 라벨(예: '전문가님')이나 이름으로 부르지 말고, "
                   "자기·상대를 소개하거나 프로그램·진행자 이름을 지어내지 말 것. 곧바로 내용으로 들어갈 것.")

    if lang == "en":
        focus_line = f"- Special emphasis: {focus}\n" if focus else ""
        return ("You are a science-podcast scriptwriter. Using the paper review below, "
                "write a script a listener can play in one sitting.\n\n"
                f"Requirements:\n- Length: {length}\n- Tone: {tone}\n- Target audience: {aud} "
                "— use vocabulary and analogies at this level.\n"
                f"{focus_line}- Editorial direction: {direction}\n{fmt}\n"
                "- Spell out acronyms on first use, then abbreviate.\n"
                "- No markdown, no headers, no bullet symbols, no sound-effect or SSML tags.\n\n"
                + (conns_blk + "\n\n" if conns_blk else "")
                + f"Paper review:\n---\n{review}\n---\n\n"
                "Output only the script body, starting immediately (no 'Script:' preamble).")
    focus_line = f"- 주안점: {focus}\n" if focus else ""
    return ("당신은 과학 팟캐스트 작가입니다. 아래 논문 리뷰를 바탕으로 청취자가 한 번에 들을 수 있는 대본을 작성하세요.\n\n"
            f"요구사항:\n- 길이: {length}\n- 톤: {tone}\n- 대상 청취자: {aud} — 이 수준의 어휘와 비유로 설명할 것.\n"
            f"{focus_line}- 구성 방향: {direction}\n{fmt}\n"
            "- 영어 약어는 첫 등장 시 한국어 풀이를 곁들이고 이후 약어 사용.\n"
            "- 마크다운 헤더·불릿·강조 기호 금지. 효과음·SSML 태그·괄호 안 메타 표기 없음.\n\n"
            + (conns_blk + "\n\n" if conns_blk else "")
            + f"논문 리뷰 자료:\n---\n{review}\n---\n\n"
            "위 요구사항에 따라 대본 본문만 출력하세요. '대본:' 같은 머리말 없이 바로 시작.")


def parse_turns(script: str, labels: list[str]) -> list[tuple[str, str]]:
    """Flexible: any short 'Label:' at line start is a turn boundary. A stray
    3rd speaker / narrator the model slipped in is remapped to an allowed
    speaker (alternating), so multi-speaker TTS never voices a phantom voice."""
    allow = {l: i for i, l in enumerate(labels)}
    pat = re.compile(r"^([A-Za-z가-힣][A-Za-z가-힣0-9]{0,9})\s*:\s*(.*)$")
    turns: list[tuple[str, str]] = []
    cur, buf, last_idx = None, [], -1

    def flush():
        if cur and " ".join(buf).strip():
            turns.append((cur, " ".join(buf).strip()))

    for raw in script.splitlines():
        line = raw.strip()
        if not line:
            continue
        m = pat.match(line)
        if m:
            flush()
            label = m.group(1)
            if label in allow:
                cur, last_idx = label, allow[label]
            else:
                last_idx = (last_idx + 1) % len(labels)
                cur = labels[last_idx]
            buf = [m.group(2).strip()]
        elif cur:
            buf.append(line)
    flush()
    return turns


def chunk_paragraphs(text: str, max_chars: int) -> list[str]:
    paras = [re.sub(r"\s+", " ", p).strip() for p in re.split(r"\n\s*\n", text)]
    paras = [p for p in paras if p]
    chunks, cur = [], ""
    for p in paras:
        if cur and len(cur) + len(p) + 1 > max_chars:
            chunks.append(cur)
            cur = ""
        cur = cur + "\n" + p if cur else p
    if cur:
        chunks.append(cur)
    return chunks or [text]


def chunk_turns(turns: list[tuple[str, str]], max_chars: int) -> list[str]:
    chunks, cur, ln = [], [], 0
    for sp, tx in turns:
        piece = f"{sp}: {tx}"
        if cur and ln + len(piece) + 1 > max_chars:
            chunks.append("\n".join(cur))
            cur, ln = [], 0
        cur.append(piece)
        ln += len(piece) + 1
    if cur:
        chunks.append("\n".join(cur))
    return chunks


def speech_single(voice: str) -> types.SpeechConfig:
    return types.SpeechConfig(voice_config=types.VoiceConfig(
        prebuilt_voice_config=types.PrebuiltVoiceConfig(voice_name=voice)))


def speech_multi(roles: list[dict]) -> types.SpeechConfig:
    return types.SpeechConfig(multi_speaker_voice_config=types.MultiSpeakerVoiceConfig(
        speaker_voice_configs=[
            types.SpeakerVoiceConfig(speaker=r["label"], voice_config=types.VoiceConfig(
                prebuilt_voice_config=types.PrebuiltVoiceConfig(voice_name=r["voice"])))
            for r in roles]))


def tts_call(client: genai.Client, text: str, cfg: types.SpeechConfig) -> bytes:
    last = None
    for attempt in range(1, 3):
        try:
            resp = client.models.generate_content(
                model=TTS_MODEL, contents=text,
                config=types.GenerateContentConfig(
                    response_modalities=["AUDIO"], speech_config=cfg,
                    http_options=types.HttpOptions(timeout=180_000)))
            usage_log.record_gemini(resp, TTS_MODEL)
            return resp.candidates[0].content.parts[0].inline_data.data
        except Exception as e:
            last = e
            if attempt == 2:
                break
            print(f"      TTS retry {attempt}/2: {type(e).__name__}", flush=True)
    raise last


def pool_synth(client, items, fn) -> list[bytes]:
    results: list[bytes | None] = [None] * len(items)
    with ThreadPoolExecutor(max_workers=TTS_WORKERS) as ex:
        futs = {ex.submit(fn, client, i): i for i in range(len(items))}
        done = 0
        for fut in as_completed(futs):
            idx, pcm = fut.result()
            results[idx] = pcm
            done += 1
            print(f"      [{done:>3}/{len(items)}] ({len(pcm) / 1024:.0f} KiB)", flush=True)
    return [r for r in results if r is not None]


def concat_pcm(parts: list[bytes]) -> bytes:
    silence = b"\x00\x00" * int(SAMPLE_RATE * SILENCE_MS / 1000)
    return silence.join(parts)


def time_stretch(pcm: bytes, speed: float) -> bytes:
    if abs(speed - 1.0) < 1e-3:
        return pcm
    try:
        import audiotsm
        import numpy as np
        from audiotsm.io.array import ArrayReader, ArrayWriter
    except ImportError:
        print("      (audiotsm/numpy 미설치 — --speed 무시)")
        return pcm
    arr = (np.frombuffer(pcm, dtype=np.int16).astype(np.float32) / 32768.0).reshape(1, -1)
    reader, writer = ArrayReader(arr), ArrayWriter(channels=1)
    audiotsm.wsola(channels=1, speed=speed).run(reader, writer)
    out = np.clip(writer.data, -1.0, 1.0)
    return (out * 32767).astype(np.int16).tobytes()


def write_mp3(path: Path, pcm: bytes) -> None:
    import lameenc
    enc = lameenc.Encoder()
    enc.set_bit_rate(MP3_BITRATE_KBPS)
    enc.set_in_sample_rate(SAMPLE_RATE)
    enc.set_channels(1)
    enc.set_quality(2)  # 0=best … 9=worst
    path.write_bytes(enc.encode(pcm) + enc.flush())


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="논문 리뷰 → Audio Overview (Gemini, CLI 폴백)")
    p.add_argument("--slug", required=True, help="슬러그 번호/이름 (예: 514)")
    p.add_argument("--speakers", type=int, choices=[1, 2, 3], default=2)
    p.add_argument("--language", choices=["ko", "en"], default="ko")
    p.add_argument("--audience", choices=["general", "student", "expert"], default="student")
    p.add_argument("--length", type=int, choices=[10, 20, 30], default=10, help="분량(분)")
    p.add_argument("--tone", choices=["friendly", "academic", "lively"], default="friendly")
    p.add_argument("--focus", default="", help="주안점(선택)")
    p.add_argument("--direction", default=None, help="구성 방향 덮어쓰기(미지정 시 언어별 기본값)")
    p.add_argument("--speed", type=float, default=1.0, help="재생 속도 배율(피치 유지, audiotsm 필요)")
    p.add_argument("--out", default=None, help="출력 MP3 경로(기본: <slug>/audio_overview.mp3)")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    from config_loader import get_openrouter_config
    from lib import openrouter as orouter

    or_cfg = get_openrouter_config()
    api_key = get_google_key()
    if not or_cfg and not api_key:
        print("ERROR: OPENROUTER_API_KEY (권장) 또는 GOOGLE_API_KEY 가 필요합니다.",
              file=sys.stderr)
        return 1

    slug = resolve_slug(args.slug)
    review_path = PAPERS / slug / "review.md"
    if not review_path.exists():
        print(f"ERROR: {review_path} 없음", file=sys.stderr)
        return 1
    review = review_path.read_text(encoding="utf-8")
    # strip YAML frontmatter
    while review.startswith("---"):
        lines = review.split("\n")
        end = next((i for i, l in enumerate(lines[1:], 1) if l.strip() == "---"), None)
        if end is None:
            break
        review = "\n".join(lines[end + 1:]).lstrip("\n")

    conns = load_connections(slug)
    lang = args.language
    direction = args.direction or DEFAULT_DIRECTION[lang]
    roles = ROLES[lang][args.speakers]
    prompt = build_prompt(review, conns, args.speakers, lang, args.audience,
                          args.length, args.tone, args.focus, direction)
    out_dir = PAPERS / slug

    if or_cfg:
        script_model = (or_cfg.get("models") or {}).get("sonnet",
                                                         "anthropic/claude-sonnet-5")
        print(f"[1/2] 대본 생성 (OpenRouter {script_model}) — slug={slug} "
              f"speakers={args.speakers} lang={lang} length={args.length}m")
        script = orouter.chat_text(
            [{"role": "user", "content": prompt}],
            model=script_model, max_tokens=16000, temperature=0.85)
        if not script:
            print("ERROR: 대본이 비었습니다.", file=sys.stderr)
            return 2
        (out_dir / "audio_script.txt").write_text(script, encoding="utf-8")
        print(f"      → audio_script.txt ({len(script):,}자)")

        tts_model = (or_cfg.get("models") or {}).get("tts", "openai/gpt-4o-mini-tts")
        print(f"[2/2] 음성 합성 (OpenRouter {tts_model})")
        chunks = chunk_paragraphs(script, MAX_CHUNK_CHARS)
        mp3_parts = []
        for i, chunk in enumerate(chunks, 1):
            mp3_parts.append(orouter.tts(chunk, model=tts_model, voice="alloy",
                                         response_format="mp3"))
            print(f"      [{i:>3}/{len(chunks)}]", flush=True)
        out = Path(args.out) if args.out else out_dir / "audio_overview.mp3"
        out.write_bytes(b"".join(mp3_parts))
        print(f"      → {out}  ({out.stat().st_size / 1024:.0f} KiB)")
        return 0

    # Legacy Gemini path
    client = genai.Client(api_key=api_key)
    print(f"[1/2] 대본 생성 ({SCRIPT_MODEL}) — slug={slug} speakers={args.speakers} "
          f"lang={lang} length={args.length}m connections={len(conns)}")
    resp = client.models.generate_content(
        model=SCRIPT_MODEL, contents=prompt,
        config=types.GenerateContentConfig(temperature=0.85, max_output_tokens=65536))
    usage_log.record_gemini(resp, SCRIPT_MODEL)
    script = (resp.text or "").strip()
    if not script:
        print("ERROR: 대본이 비었습니다.", file=sys.stderr)
        return 2
    (out_dir / "audio_script.txt").write_text(script, encoding="utf-8")
    print(f"      → audio_script.txt ({len(script):,}자)")

    print(f"[2/2] 음성 합성 ({TTS_MODEL})")
    if args.speakers == 1:
        chunks = chunk_paragraphs(script, MAX_CHUNK_CHARS)
        cfg = speech_single(roles[0]["voice"])
        parts = pool_synth(client, chunks, lambda c, i: (i, tts_call(c, chunks[i], cfg)))
        pcm = concat_pcm(parts)
    elif args.speakers == 2:
        labels = [r["label"] for r in roles]
        turns = parse_turns(script, labels)
        if not turns:
            print("ERROR: 화자 라벨 파싱 실패", file=sys.stderr)
            return 3
        chunks = chunk_turns(turns, MAX_CHUNK_CHARS)
        cfg = speech_multi(roles)
        prefix = TTS_PREFIX[lang]
        parts = pool_synth(client, chunks, lambda c, i: (i, tts_call(c, prefix + chunks[i], cfg)))
        pcm = concat_pcm(parts)
    else:
        labels = [r["label"] for r in roles]
        turns = parse_turns(script, labels)
        if not turns:
            print("ERROR: 화자 라벨 파싱 실패", file=sys.stderr)
            return 3
        vmap = {r["label"]: r["voice"] for r in roles}
        parts = pool_synth(client, turns,
                           lambda c, i: (i, tts_call(c, turns[i][1],
                                                     speech_single(vmap.get(turns[i][0], roles[0]["voice"])))))
        pcm = concat_pcm(parts)

    pcm = time_stretch(pcm, args.speed)
    out = Path(args.out) if args.out else out_dir / "audio_overview.mp3"
    write_mp3(out, pcm)
    dur = len(pcm) / 2 / SAMPLE_RATE
    print(f"      → {out}  ({out.stat().st_size / 1024:.0f} KiB, ~{dur:.0f}s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
