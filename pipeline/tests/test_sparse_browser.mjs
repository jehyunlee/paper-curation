// Behaviour contract for the Deep Research browser code emitted by
// pipeline/build_topic_index.py. The real Python string template is extracted,
// parsed by Node, and executed in a minimal DOM with fully mocked fetches.
// No provider or embedding request leaves this process.

import { execFileSync } from "node:child_process";
import { fileURLToPath } from "node:url";
import { dirname, resolve, join } from "node:path";
import { existsSync, mkdtempSync, readFileSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import vm from "node:vm";

const __dirname = dirname(fileURLToPath(import.meta.url));
const REPO = resolve(__dirname, "..", "..");
const TARGET = join(REPO, "pipeline", "build_topic_index.py");
const scratch = mkdtempSync(join(tmpdir(), "sparse-browser-"));
const extractor = join(scratch, "extract.py");
const outJs = join(scratch, "topic_index.js");

let failures = 0;
function assert(condition, message) {
  if (condition) console.log("  ok  - " + message);
  else { console.error("  FAIL- " + message); failures++; }
}

writeFileSync(extractor, [
  "import ast, sys",
  "tree = ast.parse(open(sys.argv[1], encoding='utf-8').read())",
  "values = []",
  "for node in ast.walk(tree):",
  "    if not isinstance(node, ast.Assign) or len(node.targets) != 1:",
  "        continue",
  "    target = node.targets[0]",
  "    if isinstance(target, ast.Name) and target.id == 'JS' and isinstance(node.value, ast.Constant) and isinstance(node.value.value, str):",
  "        values.append(node.value.value)",
  "assert values, 'static JS template not found'",
  "js = max(values, key=len)",
  "assert 'runDeepResearch' in js and 'deepLoadIndex' in js",
  "open(sys.argv[2], 'w', encoding='utf-8').write(js)",
  "print('extracted', len(js), 'chars')",
].join("\n"), "utf-8");

const standardPy = "/opt/homebrew/Caskroom/miniconda/base/envs/py312/bin/python";
const pyCandidate = process.env.PAPER_CURATION_PY312 || standardPy;
const py = existsSync(pyCandidate) ? pyCandidate : "python3";

let BROWSER_JS = "";
console.log("[1] emitted template parses");
try {
  console.log("  " + execFileSync(py, [extractor, TARGET, outJs], { encoding: "utf-8" }).trim());
  execFileSync(process.execPath, ["--check", outJs], { encoding: "utf-8" });
  BROWSER_JS = readFileSync(outJs, "utf-8");
  assert(true, "real build_topic_index JavaScript passes node --check");
} catch (error) {
  assert(false, "template extraction/parse: " + String(error && error.message || error).split("\n")[0]);
}
if (!BROWSER_JS) process.exit(1);

class ClassList {
  constructor() { this.names = new Set(); }
  add(...names) { for (const name of names) this.names.add(name); }
  remove(...names) { for (const name of names) this.names.delete(name); }
  contains(name) { return this.names.has(name); }
  toggle(name, force) {
    const on = force === undefined ? !this.names.has(name) : !!force;
    if (on) this.names.add(name); else this.names.delete(name);
    return on;
  }
}

class Element {
  constructor(tag, id, stats) {
    this.tagName = tag;
    this.id = id || "";
    this.stats = stats;
    this.style = {};
    this.classList = new ClassList();
    this.children = [];
    this.parentNode = null;
    this.dataset = {};
    this.disabled = false;
    this.checked = false;
    this.value = "";
    this._textContent = "";
  }
  get firstChild() { return this.children[0] || null; }
  get nextSibling() { return null; }
  get textContent() { return this._textContent; }
  set textContent(value) {
    this._textContent = String(value ?? "");
    if (this.id === "deep-status") this.stats.statuses.push(this._textContent);
  }
  appendChild(child) {
    if (child) { child.parentNode = this; this.children.push(child); }
    return child;
  }
  removeChild(child) {
    const i = this.children.indexOf(child);
    if (i >= 0) this.children.splice(i, 1);
    if (child) child.parentNode = null;
    return child;
  }
  insertBefore(child) { return this.appendChild(child); }
  remove() { if (this.parentNode) this.parentNode.removeChild(this); }
  addEventListener() {}
  querySelector() { return null; }
  querySelectorAll() { return []; }
  closest() { return null; }
  click() {}
}

function makeDocument(stats) {
  const elements = new Map();
  function get(id) {
    if (!elements.has(id)) {
      const el = new Element("div", id, stats);
      if (id === "deep-length") el.value = "short";
      if (id === "deep-model") el.value = "fast";
      elements.set(id, el);
    }
    return elements.get(id);
  }
  const body = new Element("body", "", stats);
  return {
    elements,
    body,
    getElementById: get,
    querySelector() { return null; },
    querySelectorAll() { return []; },
    addEventListener() {},
    createElement(tag) { return new Element(tag, "", stats); },
    createTextNode(text) {
      const node = new Element("#text", "", stats);
      node.textContent = text;
      return node;
    },
    createRange() {
      return {
        selectNodeContents() {},
        createContextualFragment(markup) {
          const fragment = new Element("#fragment", "", stats);
          fragment.markup = markup;
          return fragment;
        },
      };
    },
  };
}

function jsonResponse(value, status = 200) {
  return {
    ok: status >= 200 && status < 300,
    status,
    async json() { return value; },
    async text() { return JSON.stringify(value); },
  };
}

function binaryResponse(values) {
  const bytes = Int8Array.from(values);
  return {
    ok: true,
    status: 200,
    async arrayBuffer() {
      return bytes.buffer.slice(bytes.byteOffset, bytes.byteOffset + bytes.byteLength);
    },
  };
}

function providerDelta(backend, text) {
  if (backend === "anthropic") {
    return { type: "content_block_delta", index: 1, delta: { type: "text_delta", text } };
  }
  if (backend === "google") {
    return { candidates: [{ index: 0, content: { parts: [{ text }] } }] };
  }
  return { choices: [{ index: 0, delta: { content: text }, finish_reason: null }] };
}

function eventStreamResponse(events, fragmentSize = Infinity) {
  const payload = events.map((event) => "data: " +
    (typeof event === "string" ? event : JSON.stringify(event)) + "\n\n").join("");
  const bytes = new TextEncoder().encode(payload);
  let offset = 0;
  return {
    ok: true,
    status: 200,
    body: { getReader() { return { async read() {
      if (offset >= bytes.length) return { done: true, value: undefined };
      const end = Math.min(bytes.length, offset + fragmentSize);
      const value = bytes.slice(offset, end);
      offset = end;
      return { done: false, value };
    } }; } },
    async text() { return ""; },
  };
}

function streamResponse(answer, backend = "openai") {
  return eventStreamResponse([providerDelta(backend, answer), "[DONE]"]);
}

function deferred() {
  let resolve;
  const promise = new Promise((done) => { resolve = done; });
  return { promise, resolve };
}

// Explicit read barriers make overlapping runs deterministic, without sleeps,
// network calls, or relying on provider response timing. Abort is deliberately
// ignored here so a late post-cancellation chunk exercises the consumer guard.
function controlledProviderStream(backend) {
  const queue = [], barriers = [];
  let waiting = null, reads = 0;
  function deliver(part) {
    if (waiting) { const resolve = waiting; waiting = null; resolve(part); }
    else queue.push(part);
  }
  return {
    response: {
      ok: true, status: 200,
      body: { getReader() { return { read() {
        reads++;
        for (const barrier of barriers) if (reads >= barrier.count) barrier.resolve();
        if (queue.length) return Promise.resolve(queue.shift());
        return new Promise((resolve) => { waiting = resolve; });
      } }; } },
    },
    delta(text) {
      const wire = "data: " + JSON.stringify(providerDelta(backend, text)) + "\n\n";
      deliver({ done: false, value: new TextEncoder().encode(wire) });
    },
    end() { deliver({ done: true, value: undefined }); },
    waitForRead(count) {
      if (reads >= count) return Promise.resolve();
      return new Promise((resolve) => { barriers.push({ count, resolve }); });
    },
  };
}

function completionResponse(text) {
  return jsonResponse({ choices: [{ message: { content: text } }] });
}

function sparseFixture() {
  return {
    retrieval_mode: "bm25",
    model: null,
    dim: 0,
    quant: null,
    count: 3,
    papers: {
      protein: {
        title: "Protein Catalyst Design", year: 2025,
        url: "../papers/protein/index.html", external_url: "https://example.test/protein",
        authors: ["Ada Researcher"], first_author: "Ada Researcher", figures: [],
      },
      climate: {
        title: "Climate Policy", year: 2024,
        url: "../papers/climate/index.html", external_url: "https://example.test/climate",
        authors: ["Bea Scientist"], first_author: "Bea Scientist", figures: [],
      },
    },
    chunks: [
      { slug: "protein", section: "Essence", text: "Protein folding catalyst discovery uses graph neural networks.", text_sha: "sha-a" },
      { slug: "climate", section: "Essence", text: "Climate policy measures urban carbon emissions.", text_sha: "sha-b" },
      { slug: "protein", section: "Achievement", text: "Catalyst design improves protein stability.", text_sha: "sha-c" },
    ],
  };
}

function denseFixture(marker) {
  const value = {
    model: "legacy-embedding",
    dim: 2,
    quant: "int8-l2norm",
    count: 1,
    emb_file: "legacy-index.bin",
    papers: {
      dense: {
        title: "Dense Retrieval", year: 2023,
        url: "../papers/dense/index.html", external_url: "https://example.test/dense",
        authors: ["Dense Author"], first_author: "Dense Author", figures: [],
      },
    },
    chunks: [{ slug: "dense", section: "Essence", text: "Vector retrieval evidence." }],
  };
  if (marker) value.retrieval_mode = marker;
  return value;
}

function makeHarness(indices, options = {}) {
  const queue = indices.slice();
  let loadedIndex;
  const stats = { calls: [], providerBodies: [], statuses: [], prompts: [] };
  const document = makeDocument(stats);
  const fetchImpl = async (url, init = {}) => {
    const target = String(url);
    stats.calls.push({ url: target, init });
    if (target === "_search_index.json") {
      if (!queue.length) throw new Error("unexpected extra index request");
      loadedIndex = queue.shift();
      return jsonResponse(loadedIndex);
    }
    if (target === "legacy-index.bin") return binaryResponse([127, 0]);
    if (target === "/api/embed") {
      if (options.embedStatus) return jsonResponse({ error: "unavailable" }, options.embedStatus);
      return jsonResponse({ embedding: [1, 0], model: options.embedModel || loadedIndex.model, dim: loadedIndex.dim });
    }
    if (target.includes("api.openai.com/v1/chat/completions") ||
        target.includes("api.anthropic.com/v1/messages") ||
        target.includes("generativelanguage.googleapis.com")) {
      const body = JSON.parse(init.body);
      stats.providerBodies.push(body);
      if (options.providerResponse) {
        return options.providerResponse(body, stats.providerBodies.length, target, init);
      }
      const backend = target.includes("api.anthropic.com") ? "anthropic" :
        target.includes("generativelanguage.googleapis.com") ? "google" : "openai";
      return streamResponse(options.answer || "Grounded result [ref:1]", backend);
    }
    if (target === "_paper_connections.json") return jsonResponse({});
    if (target.startsWith("../papers/") && target.endsWith("/text.md")) {
      if (options.textResponse) return options.textResponse(target, init);
      return { ok: false, status: 404, async text() { return ""; } };
    }
    throw new Error("unexpected fetch: " + target);
  };

  const key = options.key || "sk-test-byok-not-a-credential";
  const storage = new Map([["_LLM_KEY", key]]);
  const context = {
    console,
    document,
    fetch: fetchImpl,
    localStorage: {
      getItem(key) { return storage.get(key) || ""; },
      setItem(key, value) { storage.set(key, String(value)); },
      removeItem(key) { storage.delete(key); },
    },
    prompt(message) {
      stats.prompts.push(message);
      if (options.prompt) return options.prompt(message);
      throw new Error("unexpected prompt");
    },
    setTimeout() { return 1; },
    clearTimeout() {},
    AbortController,
    TextDecoder,
    URL,
    Blob,
    atob(value) { return Buffer.from(value, "base64").toString("binary"); },
  };
  context.window = context;
  context.globalThis = context;
  vm.createContext(context);
  const prelude = [
    "let _ANTHROPIC_KEY = '';",
    "let _OPENAI_KEY = '';",
    "let _LLM_KEY = " + JSON.stringify(key) + ";",
    "window._PC_CROSS = false;",
  ].join("\n");
  const expose = `
    globalThis.__sparseBrowser = {
      validateDeepIndex,
      deepLoadIndex,
      sparseRetrieve,
      retrieveSeeds,
      runDeepResearch,
      deepRequestStop,
      state: () => ({
        index: DEEP.index,
        mode: DEEP.retrievalMode || '',
        answer: DEEP.currentAnswer,
        query: DEEP.currentQuery,
        refs: DEEP.currentRefs.slice(),
        running: DEEP.running,
        ftCache: DEEP._ftCache,
        embLength: DEEP.embI8 ? DEEP.embI8.length : 0,
      }),
    };
  `;
  new vm.Script(prelude + "\n" + BROWSER_JS + "\n" + expose, {
    filename: "emitted-build-topic-index.js",
  }).runInContext(context);
  return { api: context.__sparseBrowser, stats, document };
}

function callsMatching(stats, predicate) {
  return stats.calls.filter((call) => predicate(call.url));
}

console.log("[2] sparse loader and positive-only BM25 retrieval");
{
  const h = makeHarness([sparseFixture()]);
  const index = await h.api.deepLoadIndex();
  const hits = h.api.sparseRetrieve(index, "protein catalyst", null, null, 20);
  const misses = h.api.sparseRetrieve(index, "astronomy quasar", null, null, 20);
  const deeperSeeds = await h.api.retrieveSeeds(index, "protein catalyst");
  assert(h.api.state().mode === "bm25", "explicit bm25 + dim=0 selects sparse mode");
  assert(h.api.state().embLength === 0, "sparse load creates no binary-vector view");
  assert(hits.length === 2 && hits.every((hit) => hit.rrf > 0), "BM25 returns only positive lexical scores");
  assert(hits[0].chunk.slug === "protein", "BM25 ranks the lexical evidence first");
  assert(misses.length === 0, "zero lexical overlap returns no evidence");
  assert(deeperSeeds.length === 2, "Deeper seed retrieval uses the same sparse BM25 evidence");
  assert(h.stats.calls.length === 1 && h.stats.calls[0].url === "_search_index.json", "sparse loader fetches JSON only");
}

console.log("[3] sparse run uses grounded BYOK answer without embedding");
{
  const h = makeHarness([sparseFixture()]);
  await h.api.runDeepResearch("protein catalyst");
  const urls = h.stats.calls.map((call) => call.url);
  const body = h.stats.providerBodies[0];
  const userPrompt = body && body.messages && body.messages[1] && body.messages[1].content;
  assert(!urls.some((url) => url === "/api/embed"), "sparse run never calls the embedding proxy");
  assert(!urls.some((url) => url.endsWith(".bin")), "sparse run never fetches an embedding sidecar");
  assert(h.stats.providerBodies.length === 1, "matched evidence invokes the selected BYOK answer provider");
  assert(typeof userPrompt === "string" && userPrompt.includes("Protein folding catalyst discovery"), "answer request is grounded with the matched chunk text");
  assert(h.api.state().answer.includes("Grounded result"), "mock provider output reaches the Deep Research answer");
  assert(h.api.state().refs.length === 1 && h.api.state().refs[0].slug === "protein", "citations are wired to the matched paper");
  assert(h.stats.statuses.some((status) => status.includes("keyword/BM25")), "visible retrieval status identifies keyword/BM25 mode");
}

console.log("[4] sparse no-match stops before every LLM path");
for (const deeper of [false, true]) {
  const h = makeHarness([sparseFixture()]);
  h.document.getElementById("deep-deeper").checked = deeper;
  await h.api.runDeepResearch("astronomy quasar");
  assert(h.stats.providerBodies.length === 0, (deeper ? "Deeper" : "basic") + " no-match makes no answer/planning provider call");
  assert(callsMatching(h.stats, (url) => url === "/api/embed").length === 0, (deeper ? "Deeper" : "basic") + " sparse no-match makes no embedding call");
  assert(h.api.state().refs.length === 0 && h.api.state().answer === "", (deeper ? "Deeper" : "basic") + " no-match does not fabricate evidence");
}

console.log("[5] contradictory sparse metadata fails closed and is retryable");
{
  const invalid = sparseFixture();
  invalid.emb_file = "must-not-load.bin";
  const h = makeHarness([invalid, sparseFixture()]);
  let error = null;
  try { await h.api.deepLoadIndex(); } catch (caught) { error = caught; }
  assert(error && String(error.message).includes("Invalid BM25 search index"), "bm25 metadata carrying an embedding sidecar is rejected");
  assert(h.api.state().index === null, "failed load does not poison the cached index");
  assert(!h.stats.calls.some((call) => call.url === "must-not-load.bin"), "contradictory sparse sidecar is not fetched");
  const recovered = await h.api.deepLoadIndex();
  assert(recovered.retrieval_mode === "bm25" && h.api.state().mode === "bm25", "a corrected index can be loaded after failure");

  const badChunk = sparseFixture();
  badChunk.chunks[0].emb = "AA==";
  let chunkError = null;
  try { h.api.validateDeepIndex(badChunk); } catch (caught) { chunkError = caught; }
  assert(!!chunkError, "bm25 metadata carrying an inline vector is rejected");
  let markerError = null;
  try { h.api.validateDeepIndex({ ...sparseFixture(), retrieval_mode: "hybrid" }); } catch (caught) { markerError = caught; }
  assert(!!markerError, "hybrid marker with dim=0 is rejected instead of treated as sparse");
  const markerless = sparseFixture();
  delete markerless.retrieval_mode;
  let markerlessError = null;
  try { h.api.validateDeepIndex(markerless); } catch (caught) { markerlessError = caught; }
  assert(!!markerlessError, "dim=0 without the explicit bm25 marker is rejected");
}

console.log("[6] legacy dense retrieval remains dense and has no lexical fallback");
{
  const h = makeHarness([denseFixture("hybrid")], { embedModel: "different-model" });
  await h.api.runDeepResearch("vector retrieval");
  assert(h.stats.providerBodies.length === 0, "model-mismatched query vectors never reach the answer provider");
  assert(h.api.state().answer === "", "model mismatch does not produce an unsupported answer");
}
{
  const h = makeHarness([denseFixture()]);
  await h.api.runDeepResearch("vector retrieval");
  assert(h.api.state().mode === "dense", "valid legacy index without a marker retains the dense path");
  assert(callsMatching(h.stats, (url) => url === "legacy-index.bin").length === 1, "dense loader still fetches its vector sidecar");
  assert(callsMatching(h.stats, (url) => url === "/api/embed").length === 1, "dense run still embeds the query");
  assert(h.stats.providerBodies.length === 1 && h.api.state().answer.includes("Grounded result"), "dense retrieval still reaches the BYOK answer provider");
}
{
  const h = makeHarness([denseFixture("hybrid")], { embedStatus: 503 });
  await h.api.runDeepResearch("vector retrieval");
  assert(h.api.state().mode === "hybrid", "explicit hybrid metadata retains the dense/hybrid path");
  assert(h.stats.providerBodies.length === 0, "failed dense embedding does not fall back to lexical answer generation");
  assert(h.api.state().answer === "" && h.api.state().refs.length === 0, "failed dense retrieval leaves no pretend evidence");
}

const providerCases = [
  { backend: "anthropic", key: "sk-ant-test" },
  { backend: "openai", key: "sk-synthetic-not-a-credential" },
  { backend: "google", key: "AIza-synthetic-not-a-credential" },
];

console.log("[7] normal Korean provider SSE, split UTF-8 and citation tokens");
for (const { backend, key } of providerCases) {
  const first = "한국어 연구 결과는 정상입니다 [ref:", last = "1].";
  let events;
  if (backend === "anthropic") {
    events = [
      { type: "content_block_start", index: 0, content_block: { type: "thinking" } },
      { type: "content_block_delta", index: 0, delta: { type: "thinking_delta", thinking: "본문이 아닌 사고 과정" } },
      { type: "content_block_start", index: 1, content_block: { type: "text", text: "" } },
      providerDelta(backend, first),
      { type: "content_block_stop", index: 1 },
      { type: "content_block_start", index: 2, content_block: { type: "text", text: "" } },
      { type: "content_block_delta", index: 2, delta: { type: "text_delta", text: last } },
    ];
  } else if (backend === "openai") {
    events = [
      { choices: [{ index: 0, delta: { role: "assistant" } }] },
      { choices: [
        { index: 0, delta: { content: first } },
        { index: 1, delta: { content: "선택하지 않은 대체 답변" } },
      ] },
      providerDelta(backend, last), "[DONE]",
    ];
  } else {
    events = [
      { candidates: [
        { index: 0, content: { parts: [{ text: "한국어 연구 결과는 " }, { text: "정상입니다 [ref:" }] } },
        { index: 1, content: { parts: [{ text: "선택하지 않은 대체 답변" }] } },
      ] },
      providerDelta(backend, last),
    ];
  }
  const h = makeHarness([sparseFixture()], {
    key, providerResponse: () => eventStreamResponse(events, 1),
  });
  await h.api.runDeepResearch("protein catalyst");
  assert(h.api.state().answer === first + last, backend + " preserves Korean text and citations across byte/event boundaries");
  assert(!h.api.state().running, backend + " releases the run after a normal stream");
}

console.log("[8] a second entry cannot interleave independent provider streams");
for (const { backend, key } of providerCases) {
  const output = controlledProviderStream(backend);
  const h = makeHarness([sparseFixture()], {
    key,
    providerResponse: (_, n) => n === 1 ? output.response :
      streamResponse("다른 질문의 문장이 섞였습니다 [ref:1].", backend),
  });
  const pending = h.api.runDeepResearch("protein catalyst");
  await output.waitForRead(1);
  output.delta("첫 질문의 한국어 보고서 [ref:");
  await output.waitForRead(2);
  await h.api.runDeepResearch("climate policy");
  assert(h.stats.providerBodies.length === 1, backend + " ignores repeat Enter/rerun while streaming");
  assert(h.api.state().query === "protein catalyst" && h.api.state().refs[0].slug === "protein", backend + " retains the active query and reference numbering");
  assert(h.api.state().answer === "첫 질문의 한국어 보고서 [ref:", backend + " does not reset a partial citation on re-entry");
  output.delta("1].");
  output.end();
  await pending;
  assert(h.api.state().answer === "첫 질문의 한국어 보고서 [ref:1].", backend + " produces one intact report, not interwoven sentences");
}

console.log("[9] parallel Deeper drafts keep section order and one assembly stream");
{
  const output = controlledProviderStream("openai");
  const writers = [], writersReady = deferred();
  let assemblies = 0;
  const h = makeHarness([sparseFixture()], {
    providerResponse: (body) => {
      if (body.stream) return ++assemblies === 1 ? output.response :
        streamResponse("중복 취합기의 답변 [ref:1].");
      if (body.max_completion_tokens === 800) return completionResponse('["protein catalyst"]');
      if (body.max_completion_tokens === 1500) return completionResponse(JSON.stringify([
        { title: "첫 단락", refs: [1] }, { title: "둘째 단락", refs: [1] },
      ]));
      if (writers.length >= 2) return completionResponse("중복 실행의 단락 [ref:1].");
      const writer = deferred();
      writers.push(writer);
      if (writers.length === 2) writersReady.resolve();
      return writer.promise;
    },
  });
  h.document.getElementById("deep-deeper").checked = true;
  const pending = h.api.runDeepResearch("protein catalyst");
  await writersReady.promise;
  writers[1].resolve(completionResponse("둘째 단락의 결과 [ref:1]."));
  writers[0].resolve(completionResponse("첫 단락의 결과 [ref:1]."));
  await output.waitForRead(1);
  const assembler = h.stats.providerBodies.find((body) => body.stream);
  const drafts = assembler.messages[1].content;
  assert(drafts.indexOf("첫 단락의 결과") < drafts.indexOf("둘째 단락의 결과"), "out-of-order section completions reach the assembler in outline order");
  const before = h.stats.providerBodies.length;
  await h.api.runDeepResearch("climate policy");
  assert(h.stats.providerBodies.length === before, "Deeper re-entry cannot launch another planner/assembler");
  output.delta("취합한 한국어 보고서 [ref:");
  await output.waitForRead(2);
  output.delta("1].");
  output.end();
  await pending;
  assert(h.api.state().answer === "취합한 한국어 보고서 [ref:1].", "Deeper streams one intact report with the original citations");
}

console.log("[10] stop rejects late deltas, then permits a clean new report");
{
  const output = controlledProviderStream("openai");
  const h = makeHarness([sparseFixture()], {
    providerResponse: (_, n) => n === 1 ? output.response : streamResponse("새 보고서 [ref:1]."),
  });
  const pending = h.api.runDeepResearch("protein catalyst");
  await output.waitForRead(1);
  output.delta("중단 전의 완결된 문장 [ref:1].");
  await output.waitForRead(2);
  h.api.deepRequestStop();
  await h.api.runDeepResearch("climate policy");
  assert(h.stats.providerBodies.length === 1, "stop does not unlock the run while the old stream is still pending");
  output.delta(" 중단 뒤 늦게 도착한 조각 [ref:");
  output.end();
  await pending;
  assert(h.api.state().answer === "중단 전의 완결된 문장 [ref:1].", "late post-abort deltas never enter the saved partial report");
  await h.api.runDeepResearch("climate policy");
  assert(h.api.state().answer === "새 보고서 [ref:1]." && h.api.state().refs[0].slug === "climate", "a later run has a fresh answer and its own references");
}

console.log("[11] authentication retries release the old run before restarting");
{
  const output = controlledProviderStream("openai");
  const h = makeHarness([sparseFixture()], {
    prompt: () => "sk-replacement-synthetic-key",
    providerResponse: (_, n) => n === 1 ? jsonResponse({ error: "invalid_api_key" }, 401) :
      n === 2 ? output.response : streamResponse("중복 요청 [ref:1]."),
  });
  const pending = h.api.runDeepResearch("protein catalyst");
  await output.waitForRead(1);
  const calls = callsMatching(h.stats, (url) => url.includes("api.openai.com"));
  assert(calls.length === 2 && h.stats.prompts.length === 1, "auth failure still performs the explicit replacement-key retry");
  assert(calls[0].init.signal.aborted && !calls[1].init.signal.aborted, "the failed attempt is cancelled without aborting its replacement");
  assert(h.api.state().running, "the replacement owns the running lock");
  await h.api.runDeepResearch("climate policy");
  assert(h.stats.providerBodies.length === 2, "re-entry remains blocked during an auth retry");
  output.delta("새 키로 완결한 답변 [ref:1].");
  output.end();
  await pending;
  assert(h.api.state().answer === "새 키로 완결한 답변 [ref:1]." && !h.api.state().running, "auth retry completes and releases its own run");
}
{
  const h = makeHarness([sparseFixture()], {
    prompt: () => "sk-still-invalid-synthetic-key",
    providerResponse: () => jsonResponse({ error: "invalid_api_key" }, 401),
  });
  await h.api.runDeepResearch("protein catalyst");
  assert(h.stats.providerBodies.length === 4 && h.stats.prompts.length === 3, "auth retry remains capped at three replacements");
  assert(!h.api.state().running && h.api.state().answer === "", "exhausted auth attempts leave no active run or fabricated report");
}

console.log("[12] retired Deeper workers cannot join a retry or overwrite its cache");
{
  const output = controlledProviderStream("openai");
  const oldText = deferred();
  let climateFetches = 0, failedWriter = false;
  const h = makeHarness([sparseFixture()], {
    prompt: () => "sk-replacement-synthetic-key",
    textResponse: (url) => {
      if (url.includes("/climate/") && climateFetches++ === 0) return oldText.promise;
      return { ok: false, status: 404, async text() { return ""; } };
    },
    providerResponse: (body) => {
      if (body.stream) return output.response;
      if (body.max_completion_tokens === 800) return completionResponse('["protein climate"]');
      if (body.max_completion_tokens === 1500) return completionResponse(JSON.stringify([
        { title: "첫 단락", refs: [1] }, { title: "둘째 단락", refs: [2] },
      ]));
      if (!failedWriter) { failedWriter = true; return jsonResponse({ error: "invalid_api_key" }, 401); }
      return completionResponse("새 시도의 단락 [ref:1][ref:2].");
    },
  });
  h.document.getElementById("deep-deeper").checked = true;
  const pending = h.api.runDeepResearch("protein climate");
  await output.waitForRead(1);
  const before = h.stats.providerBodies.length;
  oldText.resolve({ ok: true, async text() { return "오래된 시도의 원문 조각"; } });
  // Drain only already-queued promise continuations from the retired worker.
  for (let i = 0; i < 20; i++) await Promise.resolve();
  assert(h.stats.providerBodies.length === before, "a retired section never starts an LLM request with the retry's signal");
  assert(h.api.state().ftCache.climate === null, "late old text cannot replace the retry's per-run cache entry");
  output.delta("재시도한 종합 결과 [ref:1][ref:2].");
  output.end();
  await pending;
  assert(h.api.state().answer === "재시도한 종합 결과 [ref:1][ref:2].", "only the retry's report is published");
}

if (failures) {
  console.error("\nFAILED: " + failures + " assertion(s)");
  process.exit(1);
}
console.log("\nALL PASS");
