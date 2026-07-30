// Cloudflare Worker entry — serves static assets from docs/ via the
// ASSETS binding, intercepts POST /api/audio-email to forward the generated
// MP3 to Resend for email delivery, and exposes POST /api/embed as a query
// embedding proxy for the Deep Research RAG UI (OpenRouter embeddings).
//
// Secrets (set via `npx wrangler secret put <NAME>`):
//   RESEND_API_KEY       — Resend API key (re_xxx). Required for /api/audio-email.
//   AUDIO_REPLY_TO       — Optional. Reply-To header.
//   AUDIO_FROM           — Optional. Override "From:" address.
//   OPENROUTER_API_KEY   — Required for /api/embed (qwen/qwen3-embedding-8b).
//                          Keeps the key server-side so the browser never sees it.
//   GOOGLE_API_KEY       — Legacy fallback for /api/embed if OPENROUTER unset.
//
// Limits:
//   - 25 MB request body (Resend attachment cap), 10 recipients max.
//   - One Resend call per recipient (Resend free tier: 100 mails/day).
//   - /api/embed: 2000-char query cap, single embeddings call per request.

const DEFAULT_FROM = "Paper Curation <onboarding@resend.dev>";
const MAX_ATTACHMENT_BYTES = 25 * 1024 * 1024;
const MAX_RECIPIENTS = 10;

const EMAIL_RE = /^[^@\s]+@[^@\s]+\.[^@\s]+$/;

// Deep Research 쿼리 임베딩 프록시 — OpenRouter qwen/qwen3-embedding-8b.
// dimensions=768; L2 정규화 후 돌려준다 (코사인 검색 정합).
const EMBED_MODEL = "qwen/qwen3-embedding-8b";
const EMBED_DIM = 768;
const MAX_QUERY_CHARS = 2000;
const OPENROUTER_EMBED_URL = "https://openrouter.ai/api/v1/embeddings";
const GEMINI_EMBED_MODEL = "gemini-embedding-001"; // legacy fallback

function bytesToBase64(bytes) {
  // Workers runtime has btoa but it expects a binary string. Build it in
  // 32 KB chunks so we don't blow the call-stack on multi-MB attachments.
  let s = "";
  const chunk = 0x8000;
  for (let i = 0; i < bytes.length; i += chunk) {
    s += String.fromCharCode.apply(null, bytes.subarray(i, i + chunk));
  }
  return btoa(s);
}

async function handleAudioEmail(request, env) {
  if (!env.RESEND_API_KEY) {
    return new Response("RESEND_API_KEY not configured on Worker", { status: 503 });
  }

  let form;
  try {
    form = await request.formData();
  } catch (e) {
    return new Response("Invalid form data", { status: 400 });
  }

  const recipients = form.getAll("email")
    .map(v => String(v).trim())
    .filter(v => EMAIL_RE.test(v));
  if (!recipients.length) {
    return new Response("No valid recipient", { status: 400 });
  }
  if (recipients.length > MAX_RECIPIENTS) {
    return new Response(`Too many recipients (max ${MAX_RECIPIENTS})`, { status: 400 });
  }

  const file = form.get("mp3");
  if (!file || typeof file === "string") {
    return new Response("Missing mp3 attachment", { status: 400 });
  }
  const buf = await file.arrayBuffer();
  if (buf.byteLength > MAX_ATTACHMENT_BYTES) {
    return new Response("Attachment too large", { status: 413 });
  }
  const b64 = bytesToBase64(new Uint8Array(buf));

  const filename = String(form.get("filename") || file.name || "audio-overview.mp3");
  const title = String(form.get("title") || "Audio Overview");
  const lang = String(form.get("lang") || "ko");
  const isKo = lang === "ko";

  const subject = isKo
    ? `[Paper Curation] Audio Overview: ${title}`
    : `[Paper Curation] Audio Overview: ${title}`;
  const html = isKo
    ? `<p>요청하신 Audio Overview 가 첨부되어 있습니다.</p>
       <p><b>제목</b>: ${escapeHtml(title)}</p>
       <p>이 메일은 Paper Curation 의 자동 발송입니다. 답장은 운영자에게 전달됩니다.</p>`
    : `<p>Your requested Audio Overview is attached.</p>
       <p><b>Title</b>: ${escapeHtml(title)}</p>
       <p>This is an automated message from Paper Curation. Replies route to the operator.</p>`;

  const payloadBase = {
    from: env.AUDIO_FROM || DEFAULT_FROM,
    subject,
    html,
    attachments: [{ filename, content: b64 }],
  };
  if (env.AUDIO_REPLY_TO) payloadBase.reply_to = env.AUDIO_REPLY_TO;

  const results = await Promise.all(recipients.map(async (to) => {
    const payload = { ...payloadBase, to: [to] };
    const r = await fetch("https://api.resend.com/emails", {
      method: "POST",
      headers: {
        "Authorization": `Bearer ${env.RESEND_API_KEY}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify(payload),
    });
    const text = await r.text();
    return { to, ok: r.ok, status: r.status, body: text.slice(0, 400) };
  }));

  const anyFail = results.some(r => !r.ok);
  const status = anyFail ? 502 : 200;
  return new Response(JSON.stringify({ results }), {
    status,
    headers: { "Content-Type": "application/json" },
  });
}

function escapeHtml(s) {
  return String(s).replace(/[&<>"']/g, (c) => ({
    "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;",
  }[c]));
}

function jsonResponse(obj, status = 200) {
  return new Response(JSON.stringify(obj), {
    status,
    headers: { "Content-Type": "application/json" },
  });
}

// gemini-embedding-001 은 outputDimensionality != 3072 일 때 비정규화 벡터를
// 돌려준다 (공식 가이드 명시). int8 양자화 전 단계와 동일하게 코사인 검색을
// 쓰려면 반드시 단위 벡터로 맞춰야 하므로 여기서 L2 정규화한다.
function l2normalize(vec) {
  let sumSq = 0;
  for (let i = 0; i < vec.length; i++) sumSq += vec[i] * vec[i];
  const norm = Math.sqrt(sumSq);
  if (!(norm > 0)) return vec.slice();
  const out = new Array(vec.length);
  for (let i = 0; i < vec.length; i++) out[i] = vec[i] / norm;
  return out;
}

async function handleEmbed(request, env) {
  if (!env.OPENROUTER_API_KEY && !env.GOOGLE_API_KEY) {
    return jsonResponse(
      { error: "OPENROUTER_API_KEY not configured on Worker" }, 503);
  }

  let body;
  try {
    body = await request.json();
  } catch (e) {
    return jsonResponse({ error: "Invalid JSON body" }, 400);
  }

  const text = (body && typeof body.text === "string") ? body.text.trim() : "";
  if (!text) {
    return jsonResponse({ error: "Missing or empty 'text'" }, 400);
  }
  if (text.length > MAX_QUERY_CHARS) {
    return jsonResponse(
      { error: `Query too long (max ${MAX_QUERY_CHARS} chars)` }, 413);
  }

  let values = null;
  let modelUsed = EMBED_MODEL;

  if (env.OPENROUTER_API_KEY) {
    let upstream;
    try {
      upstream = await fetch(OPENROUTER_EMBED_URL, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Authorization": "Bearer " + env.OPENROUTER_API_KEY,
          "X-Title": "paper-curation",
        },
        body: JSON.stringify({
          model: EMBED_MODEL,
          input: text,
          dimensions: EMBED_DIM,
        }),
      });
    } catch (e) {
      return jsonResponse({ error: "Embedding upstream request failed" }, 502);
    }
    if (!upstream.ok) {
      const detail = (await upstream.text()).slice(0, 400);
      return jsonResponse(
        { error: "Embedding upstream error", status: upstream.status, detail },
        502);
    }
    let data;
    try {
      data = await upstream.json();
    } catch (e) {
      return jsonResponse({ error: "Invalid embedding response" }, 502);
    }
    const item = data && data.data && data.data[0];
    values = item && item.embedding;
  } else {
    // Legacy Gemini fallback
    modelUsed = GEMINI_EMBED_MODEL;
    const apiUrl =
      `https://generativelanguage.googleapis.com/v1beta/models/${GEMINI_EMBED_MODEL}:embedContent`;
    let upstream;
    try {
      upstream = await fetch(apiUrl, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "x-goog-api-key": env.GOOGLE_API_KEY,
        },
        body: JSON.stringify({
          model: `models/${GEMINI_EMBED_MODEL}`,
          content: { parts: [{ text }] },
          taskType: "RETRIEVAL_QUERY",
          outputDimensionality: EMBED_DIM,
        }),
      });
    } catch (e) {
      return jsonResponse({ error: "Embedding upstream request failed" }, 502);
    }
    if (!upstream.ok) {
      const detail = (await upstream.text()).slice(0, 400);
      return jsonResponse(
        { error: "Embedding upstream error", status: upstream.status, detail },
        502);
    }
    let data;
    try {
      data = await upstream.json();
    } catch (e) {
      return jsonResponse({ error: "Invalid embedding response" }, 502);
    }
    values = data && data.embedding && data.embedding.values;
  }

  if (!Array.isArray(values) || values.length !== EMBED_DIM) {
    return jsonResponse({ error: "Unexpected embedding shape" }, 502);
  }

  const embedding = l2normalize(values);
  return jsonResponse({ embedding, model: modelUsed, dim: EMBED_DIM }, 200);
}

// Local pages (localhost / file://) call these APIs cross-origin — without
// CORS headers the browser cannot read the response and reports the send as
// failed even when the mail actually went out.
function corsPreflight() {
  return new Response(null, {
    status: 204,
    headers: {
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Methods": "POST, OPTIONS",
      "Access-Control-Allow-Headers": "Content-Type",
      "Access-Control-Max-Age": "86400",
    },
  });
}

function withCors(resp) {
  const h = new Headers(resp.headers);
  h.set("Access-Control-Allow-Origin", "*");
  return new Response(resp.body, { status: resp.status, headers: h });
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (url.pathname === "/api/audio-email") {
      if (request.method === "OPTIONS") return corsPreflight();
      if (request.method !== "POST") {
        return new Response("Method Not Allowed", {
          status: 405,
          headers: { "Allow": "POST" },
        });
      }
      return withCors(await handleAudioEmail(request, env));
    }
    if (url.pathname === "/api/embed") {
      if (request.method === "OPTIONS") return corsPreflight();
      if (request.method !== "POST") {
        return new Response("Method Not Allowed", {
          status: 405,
          headers: { "Allow": "POST" },
        });
      }
      return withCors(await handleEmbed(request, env));
    }
    // Everything else falls through to the static-assets binding.
    return env.ASSETS.fetch(request);
  },
};
