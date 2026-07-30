"""Shared Audio Overview (browser-direct Gemini podcast) assets.

Used by both review pages (`review_to_html.py`, mode="paper") and the topic
index Deep Research panel (`build_topic_index.py`, mode="deep"). The core JS is
context-pluggable: each page either bakes a static `window._AUDIO` (paper) or
installs `window._audioContextProvider` returning a live context (deep).
localhost-only — the Gemini key is baked at build time and stripped on deploy.
"""
import json


def get_audio_css(accent, accent_dark, accent_bg):
    return f""".audio-bar {{ margin: 0.6rem 0 0.2rem; }}
.audio-btn {{ display: inline-flex; align-items: center; gap: 0.4rem; background: {accent}; color: #fff; border: none; border-radius: 20px; padding: 0.45rem 1rem; font-size: 0.85rem; font-weight: 600; cursor: pointer; font-family: inherit; box-shadow: 0 1px 4px rgba(0,0,0,0.12); }}
.audio-btn:hover {{ background: {accent_dark}; }}
.audio-btn:disabled {{ background: #bbb; cursor: not-allowed; box-shadow: none; }}
.audio-modal-bg {{ display: none; position: fixed; inset: 0; background: rgba(0,0,0,0.5); z-index: 10000; align-items: center; justify-content: center; padding: 1rem; }}
.audio-modal-bg.active {{ display: flex; }}
.audio-modal {{ background: #fff; border-radius: 14px; max-width: 540px; width: 100%; max-height: 92vh; overflow-y: auto; padding: 1.4rem 1.6rem; box-shadow: 0 8px 40px rgba(0,0,0,0.25); }}
.audio-modal h3 {{ margin: 0 0 0.2rem; color: {accent}; font-size: 1.15rem; }}
.audio-modal .sub {{ font-size: 0.8rem; color: #888; margin-bottom: 1rem; }}
.audio-row {{ margin-bottom: 0.9rem; }}
.audio-row > label {{ display: block; font-size: 0.82rem; font-weight: 700; color: #444; margin-bottom: 0.3rem; }}
.audio-seg {{ display: inline-flex; border: 1px solid #ddd; border-radius: 8px; overflow: hidden; }}
.audio-seg button {{ background: #fff; border: none; padding: 0.4rem 0.9rem; font-size: 0.85rem; cursor: pointer; font-family: inherit; color: #555; border-right: 1px solid #eee; }}
.audio-seg button:last-child {{ border-right: none; }}
.audio-seg button.on {{ background: {accent_bg}; color: {accent_dark}; font-weight: 700; }}
.audio-modal select, .audio-modal input[type=text], .audio-modal textarea {{ width: 100%; padding: 0.45rem 0.6rem; border: 1px solid #ddd; border-radius: 8px; font-size: 0.85rem; font-family: inherit; color: #333; background: #fff; }}
.audio-modal textarea {{ min-height: 80px; resize: vertical; line-height: 1.55; }}
.audio-adv-toggle {{ font-size: 0.82rem; color: {accent_dark}; cursor: pointer; user-select: none; font-weight: 600; }}
.audio-adv {{ display: none; margin-top: 0.6rem; }}
.audio-adv.open {{ display: block; }}
.audio-actions {{ display: flex; gap: 0.6rem; justify-content: flex-end; margin-top: 1.1rem; }}
.audio-actions .cancel {{ background: #eee; color: #555; }}
.audio-actions button {{ border: none; border-radius: 20px; padding: 0.5rem 1.2rem; font-size: 0.88rem; font-weight: 600; cursor: pointer; font-family: inherit; }}
.audio-actions .go {{ background: {accent}; color: #fff; }}
.audio-actions .go:disabled {{ background: #bbb; cursor: not-allowed; }}
.audio-status {{ font-size: 0.82rem; color: #666; margin-top: 0.8rem; min-height: 1.1em; }}
.audio-notice {{ font-size: 0.8rem; color: #555; background: #fffbe6; border: 1px solid #f0d97a; border-radius: 6px; padding: 0.55rem 0.7rem; margin-top: 0.7rem; display: none; }}
.audio-notice.show {{ display: block; }}
.audio-player {{ display: none; margin-top: 1rem; padding-top: 1rem; border-top: 1px solid #eee; }}
.audio-player.show {{ display: block; }}
.audio-player audio {{ width: 100%; margin-bottom: 0.6rem; }}
.audio-speed {{ display: flex; align-items: center; gap: 0.6rem; font-size: 0.82rem; color: #555; }}
.audio-speed input[type=range] {{ flex: 1; }}
.audio-dl {{ display: inline-block; margin-top: 0.6rem; font-size: 0.82rem; color: {accent_dark}; text-decoration: none; font-weight: 600; }}"""


def audio_modal_html(sub_text="팟캐스트형 오디오로 생성합니다. (Gemini · 키는 브라우저에만 저장 · 완성본은 이메일로도 전송)"):
    """Shared modal markup. Single instance per page; opened by openAudioModal()."""
    return """
<div class="audio-modal-bg" id="audio-modal-bg">
  <div class="audio-modal">
    <h3>\U0001F3A7 Audio Overview</h3>
    <div class="sub">__SUB__</div>
    <div class="audio-row">
      <label>화자 수</label>
      <div class="audio-seg" id="seg-speakers">
        <button data-v="1">1인</button><button data-v="2">2인</button><button data-v="3">3인</button>
      </div>
    </div>
    <div class="audio-row">
      <label>언어</label>
      <div class="audio-seg" id="seg-lang">
        <button data-v="ko">한국어</button><button data-v="en">English</button>
      </div>
    </div>
    <div class="audio-row">
      <label>대상 청중</label>
      <select id="audio-audience">
        <option value="general">일반인</option>
        <option value="student">대학생·대학원생</option>
        <option value="expert">전문가</option>
      </select>
    </div>
    <div class="audio-row">
      <label>길이</label>
      <div class="audio-seg" id="seg-length">
        <button data-v="10">10분</button><button data-v="20">20분</button><button data-v="30">30분</button><button data-v="50">50분</button>
      </div>
    </div>
    <div class="audio-row">
      <label>톤</label>
      <select id="audio-tone">
        <option value="friendly">친근한</option>
        <option value="academic">학술적</option>
        <option value="lively">활기찬</option>
      </select>
    </div>
    <div class="audio-row">
      <label>주안점 (선택)</label>
      <input type="text" id="audio-focus" placeholder="예: 방법론의 한계, 산업 응용 가능성">
    </div>
    <div class="audio-row">
      <span class="audio-adv-toggle" onclick="toggleAudioAdv()">▸ 고급: 구성 방향(대본 작성 지침) 직접 수정</span>
      <div class="audio-adv" id="audio-adv">
        <textarea id="audio-direction"></textarea>
      </div>
    </div>
    <div class="audio-notice" id="audio-notice"></div>
    <div class="audio-status" id="audio-status"></div>
    <div class="audio-actions">
      <button class="cancel" onclick="closeAudioModal()">닫기</button>
      <button class="go" id="audio-go" onclick="runAudioGen()">생성</button>
    </div>
    <div class="audio-player" id="audio-player">
      <audio id="audio-el" controls></audio>
      <div class="audio-speed">
        <span>속도</span>
        <input type="range" id="audio-speed" min="0.75" max="1.75" step="0.05" value="1">
        <span id="audio-speed-val">1.0x</span>
      </div>
      <a class="audio-dl" id="audio-dl" download="audio_overview.mp3">⬇ MP3 다운로드</a>
    </div>
  </div>
</div>""".replace("__SUB__", sub_text)


# Core browser logic, wrapped in an IIFE so its top-level consts never collide
# with a host page's own globals (build_topic_index has a large JS bundle). The
# four onclick-referenced handlers are exported to window at the end.
AUDIO_JS = r"""
(function() {
// Prefer OpenRouter (sk-or-…) for script + TTS. Legacy Gemini (AIza…) still
// works. Keys stay in the browser — sent only to OpenRouter / Google.
let GKEY = (window._OPENROUTER_KEY || window._GEMINI_KEY || "") || (function() {
  try {
    const ork = localStorage.getItem("_OPENROUTER_KEY") || "";
    if (ork) return ork;
    const llm = localStorage.getItem("_LLM_KEY") || "";
    if (llm && (String(llm).startsWith("sk-or-") || String(llm).startsWith("AIza"))) return llm;
    const direct = localStorage.getItem("_GEMINI_KEY") || "";
    if (direct) return direct;
    return "";
  } catch (e) { return ""; }
})();
function isOpenRouterKey(k) {
  return !!(k && String(k).startsWith("sk-or-"));
}
function rememberGeminiKey(k) {
  GKEY = k || "";
  if (isOpenRouterKey(GKEY)) {
    window._OPENROUTER_KEY = GKEY;
  } else {
    window._GEMINI_KEY = GKEY;
  }
  try {
    if (GKEY) {
      if (isOpenRouterKey(GKEY)) localStorage.setItem("_OPENROUTER_KEY", GKEY);
      else localStorage.setItem("_GEMINI_KEY", GKEY);
      const existing = localStorage.getItem("_LLM_KEY") || "";
      if (!existing) localStorage.setItem("_LLM_KEY", GKEY);
    }
  } catch (e) {}
}
function ensureGeminiKey() {
  if (GKEY) return GKEY;
  const k = prompt(
    "Audio Overview API Key가 필요합니다.\\n" +
    "권장: OpenRouter (sk-or-v1-...) https://openrouter.ai/keys\\n" +
    "또는 Gemini (AIza...) https://aistudio.google.com/apikey\\n" +
    "(브라우저에만 저장됩니다)"
  );
  if (!k) return "";
  const t = String(k).trim();
  if (!(t.startsWith("AIza") || t.startsWith("sk-or-"))) {
    alert("올바른 형식이 아닙니다. OpenRouter(sk-or-…) 또는 Gemini(AIza…) 키를 입력하세요.");
    return "";
  }
  rememberGeminiKey(t);
  return GKEY;
}
const AUDIO_MODE = window._AUDIO_MODE || "paper";
function audioCtx() {
  if (typeof window._audioContextProvider === "function")
    return window._audioContextProvider() || {title:"", review:"", connections:[]};
  return window._AUDIO || {title:"", review:"", connections:[]};
}
const SCRIPT_MODEL = "gemini-3.1-pro-preview";
const OR_SCRIPT_MODEL = "anthropic/claude-sonnet-5";
const TTS_MODEL = "gemini-2.5-flash-preview-tts";
const OR_TTS_MODEL = "openai/gpt-4o-mini-tts";
const GBASE = "https://generativelanguage.googleapis.com/v1beta/models/";
const OR_BASE = "https://openrouter.ai/api/v1";
const SAMPLE_RATE = 24000;
const MAX_CHUNK_CHARS = 2200;   // per TTS call, keeps long scripts within limits
const POOL = 3;                 // concurrent TTS calls

const DEFAULT_DIRECTION = {
  paper: {
    ko: "논문의 originality(독창성)를 중심으로, '같이 보면 좋은 논문'들과의 연관성(예: 장단점 비교, 대조, 후속, 보완 등)을 엮어서 전체 맥락을 파악할 수 있도록 구성한다.",
    en: "Center the narrative on the paper's originality, weaving in how it relates to the recommended related papers (e.g., pros/cons comparison, contrast, follow-up, complement) so the listener grasps the overall context."
  },
  deep: {
    ko: "질문에 대한 답을 중심으로, 인용된 논문들을 근거로 엮어 전체 맥락과 핵심 통찰을 설명한다.",
    en: "Center on answering the question, weaving in the cited papers as evidence to explain the overall context and the key insights."
  }
};
function defaultDirection(lang) { return (DEFAULT_DIRECTION[AUDIO_MODE] || DEFAULT_DIRECTION.paper)[lang]; }

const ROLES = {
  ko: {
    1: [{label:"내레이터", voice:"Kore", desc:"차분하고 명료한 1인 내레이터"}],
    2: [{label:"전문가", voice:"Kore", desc:"과학기술 전문가(여성). 핵심 내용을 정확하고 깊이 있게 설명한다."},
        {label:"리포터", voice:"Puck", desc:"파급효과와 의의에 관심이 많은 진행자(남성). 청취자 눈높이에서 질문하고 맥락을 넓힌다."}],
    3: [{label:"사회자", voice:"Leda", desc:"토론을 이끌고 핵심을 정리하는 진행자"},
        {label:"전문가", voice:"Kore", desc:"과학기술 전문가(여성). 핵심을 설명한다."},
        {label:"리포터", voice:"Algieba", desc:"파급효과와 맥락에 관심 많은 패널(남성)."}]
  },
  en: {
    1: [{label:"Narrator", voice:"Kore", desc:"a calm, clear solo narrator"}],
    2: [{label:"Expert", voice:"Kore", desc:"a science-and-technology expert (female) who explains the core precisely and in depth"},
        {label:"Reporter", voice:"Puck", desc:"a host (male) keen on impact and significance, asking listener-level questions and widening the context"}],
    3: [{label:"Host", voice:"Leda", desc:"a host who drives the discussion and sums up the key points"},
        {label:"Expert", voice:"Kore", desc:"a science-and-technology expert (female) explaining the core"},
        {label:"Reporter", voice:"Algieba", desc:"a panelist (male) keen on impact and context"}]
  }
};

// Gemini multi-speaker TTS needs a leading style instruction or it tries to
// "answer" the transcript as text instead of voicing it.
const TTS_PREFIX = {ko: "다음 대화를 자연스럽고 생동감 있게 읽어줘:\n", en: "Read the following conversation naturally and with energy:\n"};

const AUDIENCE = {
  ko: {general:"일반 대중", student:"대학생·대학원생", expert:"해당 분야 전문가"},
  en: {general:"a general audience", student:"undergraduate and graduate students", expert:"domain experts"}
};
const TONE = {
  ko: {friendly:"친근하지만 전문적이고, 청취자에게 말 걸 듯이", academic:"차분하고 학술적이며 정확하게", lively:"활기차고 박진감 있게"},
  en: {friendly:"warm yet professional, speaking directly to the listener", academic:"calm, academic and precise", lively:"lively and energetic"}
};

const SETTINGS_KEY = "paperAudioSettings";
function defaultSettings() {
  return {speakers:"2", lang:"ko", audience:"student", length:"10", tone:"friendly",
          focus:"", direction:defaultDirection("ko"), directionDirty:false};
}
function loadSettings() {
  try { return Object.assign(defaultSettings(), JSON.parse(localStorage.getItem(SETTINGS_KEY) || "{}")); }
  catch (e) { return defaultSettings(); }
}
function saveSettings(s) { try { localStorage.setItem(SETTINGS_KEY, JSON.stringify(s)); } catch (e) {} }

function setSeg(groupId, val) {
  document.querySelectorAll("#" + groupId + " button").forEach(function(b) {
    b.classList.toggle("on", b.getAttribute("data-v") === String(val));
  });
}
function getSeg(groupId) {
  const on = document.querySelector("#" + groupId + " button.on");
  return on ? on.getAttribute("data-v") : null;
}

function openAudioModal() {
  // Acquire the Gemini key lazily — at modal-open time. This lets
  // Cloudflare visitors paste their own key the first time and have it
  // remembered for subsequent sessions (localStorage).
  if (!ensureGeminiKey()) {
    // User dismissed the prompt or entered an invalid key. Don't open
    // the modal — pretending the form is usable would lead to a
    // confusing 401 deep inside the generation flow.
    return;
  }
  // We used to prompt for the email address here, but that forced
  // visitors to commit before they'd even seen the form. The recipient
  // list is now resolved inside runAudioGen() — the prompt fires once,
  // the first time they actually click "생성", and never again
  // (localStorage remembers it).
  const s = loadSettings();
  setSeg("seg-speakers", s.speakers);
  setSeg("seg-lang", s.lang);
  setSeg("seg-length", s.length);
  document.getElementById("audio-audience").value = s.audience;
  document.getElementById("audio-tone").value = s.tone;
  document.getElementById("audio-focus").value = s.focus || "";
  const dir = document.getElementById("audio-direction");
  dir.value = s.directionDirty ? s.direction : defaultDirection(s.lang);
  dir.dataset.dirty = s.directionDirty ? "1" : "";
  document.getElementById("audio-status").textContent = "";
  const _notice = document.getElementById("audio-notice");
  if (_notice) { _notice.textContent = ""; _notice.classList.remove("show"); }
  document.getElementById("audio-modal-bg").classList.add("active");
}
function closeAudioModal() { document.getElementById("audio-modal-bg").classList.remove("active"); }
function toggleAudioAdv() {
  const a = document.getElementById("audio-adv");
  a.classList.toggle("open");
  document.querySelector(".audio-adv-toggle").textContent =
    (a.classList.contains("open") ? "▾" : "▸") + " 고급: 구성 방향(대본 작성 지침) 직접 수정";
}

function wireAudioModal() {
  ["seg-speakers", "seg-lang", "seg-length"].forEach(function(gid) {
    document.querySelectorAll("#" + gid + " button").forEach(function(b) {
      b.addEventListener("click", function() {
        setSeg(gid, b.getAttribute("data-v"));
        if (gid === "seg-lang") {
          const dir = document.getElementById("audio-direction");
          if (!dir.dataset.dirty) dir.value = defaultDirection(b.getAttribute("data-v"));
        }
      });
    });
  });
  const dir = document.getElementById("audio-direction");
  if (dir) dir.addEventListener("input", function() { dir.dataset.dirty = "1"; });
  document.getElementById("audio-modal-bg").addEventListener("click", function(e) {
    if (e.target.id === "audio-modal-bg") closeAudioModal();
  });
}

function collectSettings() {
  const dir = document.getElementById("audio-direction");
  return {
    speakers: getSeg("seg-speakers") || "2",
    lang: getSeg("seg-lang") || "ko",
    audience: document.getElementById("audio-audience").value,
    length: getSeg("seg-length") || "10",
    tone: document.getElementById("audio-tone").value,
    focus: document.getElementById("audio-focus").value.trim(),
    direction: dir.value.trim(),
    directionDirty: dir.dataset.dirty === "1"
  };
}

function lengthGuide(min, lang) {
  // Calibrated from measured Gemini TTS rate (~560 ko chars/min) and over-asked
  // ~1.3x because the model under-fills long length targets. ko≈730 chars/min.
  const m = parseInt(min, 10);
  if (lang === "en") return "about " + m + " minutes — write at least " + (m * 200) +
    " words; fill the entire length with substantive discussion and do not wrap up early";
  return "약 " + m + "분 분량 — 한국어로 최소 " + (m * 730) +
    "자 이상 작성하고, 내용을 충분히 깊게 다뤄 분량을 끝까지 채울 것(중간에 서둘러 마무리하지 말 것)";
}

function connectionsText(lang) {
  const cs = audioCtx().connections || [];
  if (!cs.length) return "";
  const head = AUDIO_MODE === "deep"
    ? (lang === "en" ? "Cited papers (use as evidence):" : "인용된 논문 (근거로 엮을 것):")
    : (lang === "en" ? "Recommended related papers (weave these into the context):" : "같이 보면 좋은 논문 (맥락에 엮을 것):");
  const lines = cs.map(function(c) {
    return "- [" + (c.relation || "") + "] " + (c.title || "") + (c.reason ? " — " + c.reason : "");
  });
  return head + "\n" + lines.join("\n");
}

function buildScriptPrompt(s) {
  const ctx = audioCtx();
  const lang = s.lang;
  const roles = ROLES[lang][s.speakers];
  const tone = TONE[lang][s.tone];
  const aud = AUDIENCE[lang][s.audience];
  const len = lengthGuide(s.length, lang);
  const conns = connectionsText(lang);
  const srcLabel = AUDIO_MODE === "deep"
    ? (lang === "en" ? "Source material (the question and the generated answer)" : "분석 자료 (질문과 생성된 답변)")
    : (lang === "en" ? "Paper review" : "논문 리뷰 자료");
  let fmt;
  if (s.speakers === "1") {
    fmt = lang === "en"
      ? "- Format: a single narrator from start to finish; output narration text only, no speaker labels.\n- Do not invent a show name or introduce yourself by name; dive straight into the content."
      : "- 형식: 한 명의 내레이터가 처음부터 끝까지 진행. 화자 라벨 없이 순수 내레이션 텍스트만 출력.\n- 프로그램 이름이나 진행자 이름을 지어내 자기소개하지 말고, 곧바로 내용으로 들어갈 것.";
  } else {
    const roleLines = roles.map(function(r) { return "- " + r.label + ": " + r.desc; }).join("\n");
    const labels = roles.map(function(r) { return r.label; });
    fmt = (lang === "en"
        ? "- Format: a " + s.speakers + "-person conversational podcast.\n" + roleLines +
          "\n- Begin every utterance with exactly one of these labels followed by ': ' — " +
          labels.join(", ") + "\n- Natural turn-taking; no one speaks more than ~5 sentences in a row." +
          "\n- Exactly " + s.speakers + " speakers — never add a third speaker, narrator, or host." +
          "\n- The labels are voice tags only: speakers must NOT address each other by these labels or by any personal name, must NOT introduce themselves, and must NOT invent a show or host name. Dive straight into the substance."
        : "- 형식: " + s.speakers + "인 대화형 팟캐스트.\n" + roleLines +
          "\n- 각 발화는 반드시 다음 라벨 중 하나로 시작하고 콜론+공백을 붙일 것 — " +
          labels.join(", ") + "\n- 자연스러운 turn-taking, 한 명이 5문장 이상 연속 독점 금지." +
          "\n- 등장인물은 정확히 " + s.speakers + "명뿐 — 제3의 화자·내레이터·해설자를 절대 추가하지 말 것." +
          "\n- 라벨은 음성 구분용 표시일 뿐이다. 대사 속에서 서로를 그 라벨(예: '전문가님')이나 이름으로 부르지 말고, 자기·상대를 소개하거나 프로그램·진행자 이름을 지어내지 말 것. 곧바로 내용으로 들어갈 것.");
  }
  const focusLine = s.focus ? (lang === "en" ? "- Special emphasis: " + s.focus + "\n"
                                             : "- 주안점: " + s.focus + "\n") : "";
  if (lang === "en") {
    return "You are a science-podcast scriptwriter. Using the material below, write a script a listener can play in one sitting.\n\n" +
      "Requirements:\n- Length: " + len + "\n- Tone: " + tone + "\n- Target audience: " + aud +
      " — use vocabulary and analogies at this level.\n" + focusLine +
      "- Editorial direction: " + s.direction + "\n" + fmt +
      "\n- Spell out acronyms on first use, then abbreviate.\n- No markdown, no headers, no bullet symbols, no sound-effect or SSML tags.\n\n" +
      (conns ? conns + "\n\n" : "") +
      srcLabel + ":\n---\n" + ctx.review + "\n---\n\nOutput only the script body, starting immediately (no 'Script:' preamble).";
  }
  return "당신은 과학 팟캐스트 작가입니다. 아래 자료를 바탕으로 청취자가 한 번에 들을 수 있는 대본을 작성하세요.\n\n" +
    "요구사항:\n- 길이: " + len + "\n- 톤: " + tone + "\n- 대상 청취자: " + aud +
    " — 이 수준의 어휘와 비유로 설명할 것.\n" + focusLine +
    "- 구성 방향: " + s.direction + "\n" + fmt +
    "\n- 영어 약어는 첫 등장 시 한국어 풀이를 곁들이고 이후 약어 사용.\n- 마크다운 헤더·불릿·강조 기호 금지. 효과음·SSML 태그·괄호 안 메타 표기 없음.\n\n" +
    (conns ? conns + "\n\n" : "") +
    srcLabel + ":\n---\n" + ctx.review + "\n---\n\n위 요구사항에 따라 대본 본문만 출력하세요. '대본:' 같은 머리말 없이 바로 시작.";
}

async function geminiPost(model, body) {
  const r = await fetch(GBASE + model + ":generateContent?key=" + encodeURIComponent(GKEY), {
    method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify(body)
  });
  if (!r.ok) {
    let msg = r.status + " " + r.statusText;
    try { const j = await r.json(); if (j.error && j.error.message) msg = j.error.message; } catch (e) {}
    throw new Error(msg);
  }
  return r.json();
}

async function openRouterChat(prompt) {
  const r = await fetch(OR_BASE + "/chat/completions", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Authorization": "Bearer " + GKEY,
      "X-Title": "paper-curation-audio"
    },
    body: JSON.stringify({
      model: OR_SCRIPT_MODEL,
      max_tokens: 16000,
      temperature: 0.85,
      messages: [{ role: "user", content: prompt }]
    })
  });
  if (!r.ok) {
    let msg = r.status + " " + r.statusText;
    try { const j = await r.json(); if (j.error) msg = (j.error.message || JSON.stringify(j.error)); } catch (e) {}
    throw new Error(msg);
  }
  const j = await r.json();
  return ((((j.choices || [])[0] || {}).message || {}).content || "").trim();
}

async function openRouterTTS(text) {
  const r = await fetch(OR_BASE + "/audio/speech", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Authorization": "Bearer " + GKEY,
      "X-Title": "paper-curation-audio"
    },
    body: JSON.stringify({
      model: OR_TTS_MODEL,
      input: text,
      voice: "alloy",
      response_format: "mp3"
    })
  });
  if (!r.ok) {
    let msg = r.status + " " + r.statusText;
    try { msg = (await r.text()).slice(0, 200); } catch (e) {}
    throw new Error(msg);
  }
  const buf = await r.arrayBuffer();
  return new Uint8Array(buf);
}

async function callScript(prompt) {
  if (isOpenRouterKey(GKEY)) return openRouterChat(prompt);
  const j = await geminiPost(SCRIPT_MODEL, {
    contents: [{parts: [{text: prompt}]}],
    generationConfig: {temperature: 0.85, maxOutputTokens: 65536}
  });
  const parts = (((j.candidates || [])[0] || {}).content || {}).parts || [];
  return parts.map(function(p) { return p.text || ""; }).join("").trim();
}

function speechSingle(voice) {
  return {voiceConfig: {prebuiltVoiceConfig: {voiceName: voice}}};
}
function speechMulti(roles) {
  return {multiSpeakerVoiceConfig: {speakerVoiceConfigs: roles.map(function(r) {
    return {speaker: r.label, voiceConfig: {prebuiltVoiceConfig: {voiceName: r.voice}}};
  })}};
}

function b64ToBytes(b64) {
  const bin = atob(b64);
  const out = new Uint8Array(bin.length);
  for (let i = 0; i < bin.length; i++) out[i] = bin.charCodeAt(i);
  return out;
}

async function ttsCall(text, speechConfig) {
  if (isOpenRouterKey(GKEY)) {
    // OpenRouter TTS returns mp3 bytes (not PCM). Callers that expect PCM
    // for multi-speaker concat will use the mp3 path via decodeAudioData.
    return openRouterTTS(text);
  }
  const j = await geminiPost(TTS_MODEL, {
    contents: [{parts: [{text: text}]}],
    generationConfig: {responseModalities: ["AUDIO"], speechConfig: speechConfig}
  });
  const part = ((((j.candidates || [])[0] || {}).content || {}).parts || [])[0] || {};
  const data = (part.inlineData || part.inline_data || {}).data;
  if (!data) throw new Error("TTS 응답에 오디오가 없습니다");
  return b64ToBytes(data);
}

function parseTurns(script, labels) {
  // Flexible: treat any short "Label:" at line start as a turn boundary. A
  // stray 3rd speaker / narrator the model slipped in is remapped to an
  // allowed speaker (alternating), so multi-speaker TTS never voices a
  // phantom 3rd voice from a label embedded inside another turn's text.
  const allow = {}; labels.forEach(function(l, i) { allow[l] = i; });
  const re = /^([A-Za-z가-힣][A-Za-z가-힣0-9]{0,9})\s*:\s*(.*)$/;
  const turns = []; let cur = null, buf = [], lastIdx = -1;
  function flush() { if (cur && buf.join(" ").trim()) turns.push({speaker: cur, text: buf.join(" ").trim()}); }
  script.split(/\r?\n/).forEach(function(raw) {
    const line = raw.trim();
    if (!line) return;
    const m = line.match(re);
    if (m) {
      flush();
      const label = m[1];
      if (label in allow) { cur = label; lastIdx = allow[label]; }
      else { lastIdx = (lastIdx + 1) % labels.length; cur = labels[lastIdx]; }
      buf = [m[2].trim()];
    } else if (cur) buf.push(line);
  });
  flush();
  return turns;
}

function chunkParagraphs(text, maxChars) {
  const paras = text.split(/\n\s*\n/).map(function(p) { return p.replace(/\s+/g, " ").trim(); }).filter(Boolean);
  const chunks = []; let cur = "";
  paras.forEach(function(p) {
    if (cur && (cur.length + p.length + 1) > maxChars) { chunks.push(cur); cur = ""; }
    cur = cur ? cur + "\n" + p : p;
  });
  if (cur) chunks.push(cur);
  return chunks.length ? chunks : [text];
}

function chunkTurns(turns, maxChars) {
  const chunks = []; let cur = [], len = 0;
  turns.forEach(function(t) {
    const piece = t.speaker + ": " + t.text;
    if (cur.length && (len + piece.length + 1) > maxChars) { chunks.push(cur); cur = []; len = 0; }
    cur.push(piece); len += piece.length + 1;
  });
  if (cur.length) chunks.push(cur);
  return chunks.map(function(c) { return c.join("\n"); });
}

async function poolMap(items, worker, concurrency) {
  const results = new Array(items.length);
  let next = 0;
  async function run() {
    while (true) {
      const i = next++;
      if (i >= items.length) return;
      results[i] = await worker(items[i], i);
    }
  }
  const runners = [];
  for (let k = 0; k < Math.min(concurrency, items.length); k++) runners.push(run());
  await Promise.all(runners);
  return results;
}

function concatPcm(parts) {
  const silence = new Uint8Array(Math.floor(SAMPLE_RATE * 0.2) * 2); // 200ms
  const pieces = []; let total = 0;
  parts.forEach(function(p, i) {
    if (i) { pieces.push(silence); total += silence.length; }
    pieces.push(p); total += p.length;
  });
  const out = new Uint8Array(total); let off = 0;
  pieces.forEach(function(p) { out.set(p, off); off += p.length; });
  return out;
}

function pcmToMp3(pcm) {
  if (typeof lamejs === "undefined") throw new Error("MP3 인코더(lamejs) 로드 실패");
  const samples = new Int16Array(pcm.buffer, pcm.byteOffset, pcm.length >> 1);
  const enc = new lamejs.Mp3Encoder(1, SAMPLE_RATE, 64);
  const block = 1152, out = [];
  for (let i = 0; i < samples.length; i += block) {
    const buf = enc.encodeBuffer(samples.subarray(i, i + block));
    if (buf.length) out.push(new Uint8Array(buf));
  }
  const tail = enc.flush();
  if (tail.length) out.push(new Uint8Array(tail));
  return new Blob(out, {type: "audio/mpeg"});
}

function setStatus(msg) { document.getElementById("audio-status").textContent = msg; }

async function synthesize(s, script) {
  const roles = ROLES[s.lang][s.speakers];
  if (s.speakers === "1") {
    const chunks = chunkParagraphs(script, MAX_CHUNK_CHARS);
    const cfg = speechSingle(roles[0].voice);
    let done = 0;
    const parts = await poolMap(chunks, async function(c) {
      const pcm = await ttsCall(c, cfg);
      setStatus("🔊 음성 합성 " + (++done) + "/" + chunks.length);
      return pcm;
    }, POOL);
    return concatPcm(parts);
  }
  const labels = roles.map(function(r) { return r.label; });
  const turns = parseTurns(script, labels);
  if (!turns.length) throw new Error("대본에서 화자 라벨을 찾지 못했습니다");
  if (s.speakers === "2") {
    const chunks = chunkTurns(turns, MAX_CHUNK_CHARS);
    const cfg = speechMulti(roles);
    const prefix = TTS_PREFIX[s.lang] || TTS_PREFIX.ko;
    let done = 0;
    const parts = await poolMap(chunks, async function(c) {
      const pcm = await ttsCall(prefix + c, cfg);
      setStatus("🔊 음성 합성 " + (++done) + "/" + chunks.length);
      return pcm;
    }, POOL);
    return concatPcm(parts);
  }
  // 3 speakers: per-turn single-voice (Gemini multi-speaker caps at 2)
  const voiceMap = {}; roles.forEach(function(r) { voiceMap[r.label] = r.voice; });
  let done = 0;
  const parts = await poolMap(turns, async function(t) {
    const pcm = await ttsCall(t.text, speechSingle(voiceMap[t.speaker] || roles[0].voice));
    setStatus("🔊 음성 합성 " + (++done) + "/" + turns.length);
    return pcm;
  }, POOL);
  return concatPcm(parts);
}

let _audioUrl = null;
async function runAudioGen() {
  if (!ensureGeminiKey()) { setStatus("Gemini API Key가 필요합니다."); return; }
  const ctx = audioCtx();
  if (!ctx.review || !ctx.review.trim()) { setStatus("먼저 분석할 내용이 필요합니다."); return; }
  const go = document.getElementById("audio-go");
  go.disabled = true;
  const s = collectSettings();
  saveSettings(s);
  // Tell the user up front that they can leave the page — generation
  // can take several minutes and the finished MP3 will be emailed to
  // them automatically (so the tab need not stay open). We use a
  // persistent banner (audio-notice) so it doesn't get overwritten by
  // the progress messages in audio-status.
  const recipients = resolveAudioRecipients();
  const notice = document.getElementById("audio-notice");
  if (notice) {
    if (recipients.length) {
      notice.textContent = "📧 Audio Overview 작성이 완료되면 이메일로 보내드립니다 (" + recipients.join(", ") + "). 다른 작업을 하셔도 좋습니다.";
      notice.classList.add("show");
    } else {
      notice.classList.remove("show");
      notice.textContent = "";
    }
  }
  try {
    const scriptModel = isOpenRouterKey(GKEY) ? OR_SCRIPT_MODEL : SCRIPT_MODEL;
    setStatus("✍️ 대본 생성 중... (" + scriptModel + ")");
    const script = await callScript(buildScriptPrompt(s));
    if (!script) throw new Error("대본이 비어 있습니다");
    let blob;
    if (isOpenRouterKey(GKEY)) {
      // OpenRouter /audio/speech returns mp3 — chunk and concatenate blobs.
      setStatus("🔊 음성 합성 중... (" + OR_TTS_MODEL + ")");
      const chunks = chunkParagraphs(script, MAX_CHUNK_CHARS);
      let done = 0;
      const parts = [];
      for (let i = 0; i < chunks.length; i++) {
        parts.push(await openRouterTTS(chunks[i]));
        setStatus("🔊 음성 합성 " + (++done) + "/" + chunks.length);
      }
      blob = new Blob(parts, {type: "audio/mpeg"});
    } else {
      setStatus("🔊 음성 합성 중...");
      const pcm = await synthesize(s, script);
      setStatus("🎚️ MP3 인코딩 중...");
      blob = pcmToMp3(pcm);
    }
    if (_audioUrl) URL.revokeObjectURL(_audioUrl);
    _audioUrl = URL.createObjectURL(blob);
    const el = document.getElementById("audio-el");
    el.src = _audioUrl;
    if ("preservesPitch" in el) el.preservesPitch = true;
    const dl = document.getElementById("audio-dl");
    dl.href = _audioUrl;
    const fname = (ctx.title || "audio_overview").slice(0, 60).replace(/[^\w가-힣 -]/g, "").trim().replace(/\s+/g, "_") + ".mp3";
    dl.download = fname;
    document.getElementById("audio-player").classList.add("show");
    setStatus("✅ 완료 (" + Math.round(blob.size / 1024) + " KiB). 다운로드 가능.");

    // Send by email (optional). LOCAL pages have a baked recipient list;
    // WEB pages ask the visitor once and remember in localStorage. The send
    // always targets the deployed worker (absolute AUDIO_EMAIL_ENDPOINT), so
    // localhost / file:// pages can mail too; the download stays the fallback.
    try {
      const recipients = resolveAudioRecipients();
      if (recipients.length) {
        const MAX_MAIL_BYTES = 25 * 1024 * 1024;   // Resend/worker 첨부 상한
        if (blob.size > MAX_MAIL_BYTES) {
          setStatus("✅ 완료 — 다운로드 가능 (오디오 " + Math.round(blob.size / 1048576) + "MB > 이메일 첨부 한도 25MB → 이메일 생략. 위에서 MP3를 받으세요)");
        } else {
          setStatus("📧 이메일로 전송 중...");
          const ok = await sendAudioEmail(blob, fname, ctx.title || "Audio Overview", s.lang, recipients);
          if (ok) {
            setStatus("✅ 완료 — 다운로드 가능 + 이메일 발송됨 (" + recipients.join(", ") + ")");
          } else {
            setStatus("✅ 완료 — 다운로드 가능 (이메일 발송 실패. 위에서 직접 받으세요)");
          }
        }
      }
    } catch (mailErr) {
      console.warn("audio email send skipped:", mailErr);
    }
  } catch (e) {
    console.error(e);
    setStatus("오류: " + (e.message || e));
  } finally {
    go.disabled = false;
  }
}

// ── Email delivery helpers ──────────────────────────────────────────
function isLocalHost() {
  const h = window.location.hostname;
  return h === "localhost" || h === "127.0.0.1" || h === "0.0.0.0"
      || h.endsWith(".local") || window.location.protocol === "file:";
}

function resolveAudioRecipients() {
  // LOCAL pages: baked list (`window._LOCAL_EMAILS`) — the owner sees
  // every audio without ever being asked.
  // WEB pages: localStorage + first-time prompt.
  const baked = Array.isArray(window._LOCAL_EMAILS) ? window._LOCAL_EMAILS.filter(Boolean) : [];
  if (isLocalHost() && baked.length) return baked;
  let e = "";
  try { e = localStorage.getItem("_AUDIO_EMAIL") || ""; } catch (er) {}
  if (e) return [e];
  const entered = prompt(
    "Audio Overview 완성본을 이메일로 받으시려면 주소를 입력하세요.\n" +
    "(브라우저에만 저장되며 다음에 다시 묻지 않습니다. 비워두면 다운로드만 합니다.)"
  );
  if (!entered) return [];
  const t = String(entered).trim();
  if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(t)) {
    alert("이메일 형식이 올바르지 않습니다. 다운로드로 받으세요.");
    return [];
  }
  try { localStorage.setItem("_AUDIO_EMAIL", t); } catch (er) {}
  return [t];
}

// 로컬 페이지(localhost / file://)에는 /api 라우트가 없으므로 상대경로는
// worker 에 도달하지 못한다 — 항상 배포된 worker 절대경로로 발송한다.
var AUDIO_EMAIL_ENDPOINT = "https://paper-curation.jehyunlee.dev/api/audio-email";

async function sendAudioEmail(blob, filename, title, lang, recipients) {
  const fd = new FormData();
  fd.append("mp3", blob, filename);
  fd.append("filename", filename);
  fd.append("title", title || "Audio Overview");
  fd.append("lang", lang || "ko");
  for (const r of recipients) fd.append("email", r);
  try {
    const r = await fetch(AUDIO_EMAIL_ENDPOINT, { method: "POST", body: fd });
    if (!r.ok) {
      const txt = await r.text();
      console.warn("audio-email server returned", r.status, txt.slice(0, 200));
      return false;
    }
    return true;
  } catch (e) {
    console.warn("audio-email fetch failed:", e);
    return false;
  }
}

document.addEventListener("DOMContentLoaded", function() {
  // Button always enabled — clicking will trigger ensureGeminiKey()
  // which prompts the user when the page was deployed without a baked
  // key. We keep a hint in the button tooltip and a small inline note
  // when no key is cached so the visitor knows what to expect (some
  // browsers hide tooltips on mobile / dark mode, hence the visible
  // text fallback).
  const ob = document.getElementById("audio-open");
  if (ob && !GKEY) {
    ob.title = "클릭 시 Gemini API Key 입력 창이 뜹니다 (브라우저에만 저장)";
    const bar = ob.parentElement;
    if (bar && !bar.querySelector(".audio-hint")) {
      const hint = document.createElement("span");
      hint.className = "audio-hint";
      hint.textContent = "Gemini API Key 필요 (첫 클릭 시 입력)";
      hint.style.cssText = "margin-left:0.6rem;font-size:0.78rem;color:#888;";
      bar.appendChild(hint);
    }
  }
  if (!document.getElementById("audio-modal-bg")) return;
  wireAudioModal();
  const sp = document.getElementById("audio-speed");
  const el = document.getElementById("audio-el");
  if (sp && el) sp.addEventListener("input", function() {
    el.playbackRate = parseFloat(sp.value);
    document.getElementById("audio-speed-val").textContent = parseFloat(sp.value).toFixed(2) + "x";
  });
});

window.openAudioModal = openAudioModal;
window.closeAudioModal = closeAudioModal;
window.toggleAudioAdv = toggleAudioAdv;
window.runAudioGen = runAudioGen;
})();
"""


def audio_script_block(gemini_key, mode="paper", ctx=None, provider_js="",
                        local_emails=None):
    """Wrap AUDIO_JS with the injected key, mode, and either a static context
    (paper) or a context-provider snippet (deep).

    Always emits the script so deployed pages can still accept a
    user-provided key at runtime (the JS prompts the visitor on first
    click and remembers the result in localStorage). When no key is
    baked at build time we set the global to an empty string so the JS
    falls through to the localStorage / prompt path.

    ``local_emails`` is a list of recipient addresses baked into the
    build so the operator never has to retype them on localhost. The
    array is stripped on deploy by ``prepare_deploy.py`` so visitor
    pages always start with an empty list and prompt instead.
    """
    prefix = "window._GEMINI_KEY = " + json.dumps(gemini_key or "") + ";\n"
    prefix += "window._AUDIO_MODE = " + json.dumps(mode) + ";\n"
    prefix += "window._LOCAL_EMAILS = " + json.dumps(local_emails or []) + ";\n"
    if ctx is not None:
        prefix += "window._AUDIO = " + json.dumps(ctx, ensure_ascii=False) + ";\n"
    if provider_js:
        prefix += provider_js + "\n"
    return ('<script src="https://cdn.jsdelivr.net/npm/lamejs@1.2.1/lame.min.js"></script>\n'
            "<script>\n" + prefix + AUDIO_JS + "\n</script>")
