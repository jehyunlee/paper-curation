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

function streamResponse(answer) {
  const payload = "data: " + JSON.stringify({
    choices: [{ delta: { content: answer }, finish_reason: null }],
  }) + "\n\ndata: [DONE]\n\n";
  const bytes = new TextEncoder().encode(payload);
  let sent = false;
  return {
    ok: true,
    status: 200,
    body: { getReader() { return { async read() {
      if (sent) return { done: true, value: undefined };
      sent = true;
      return { done: false, value: bytes };
    } }; } },
    async text() { return ""; },
  };
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
  const stats = { calls: [], providerBodies: [], statuses: [] };
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
    if (target.includes("api.openai.com/v1/chat/completions")) {
      stats.providerBodies.push(JSON.parse(init.body));
      return streamResponse(options.answer || "Grounded result [ref:1]");
    }
    if (target.startsWith("../papers/") && target.endsWith("/text.md")) {
      return { ok: false, status: 404, async text() { return ""; } };
    }
    throw new Error("unexpected fetch: " + target);
  };

  const storage = new Map([["_LLM_KEY", "sk-test-byok-not-a-credential"]]);
  const context = {
    console,
    document,
    fetch: fetchImpl,
    localStorage: {
      getItem(key) { return storage.get(key) || ""; },
      setItem(key, value) { storage.set(key, String(value)); },
      removeItem(key) { storage.delete(key); },
    },
    prompt() { throw new Error("unexpected prompt"); },
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
    "let _OPENAI_KEY = 'sk-test-byok-not-a-credential';",
    "let _LLM_KEY = 'sk-test-byok-not-a-credential';",
    "window._PC_CROSS = false;",
  ].join("\n");
  const expose = `
    globalThis.__sparseBrowser = {
      validateDeepIndex,
      deepLoadIndex,
      sparseRetrieve,
      retrieveSeeds,
      runDeepResearch,
      state: () => ({
        index: DEEP.index,
        mode: DEEP.retrievalMode || '',
        answer: DEEP.currentAnswer,
        refs: DEEP.currentRefs.slice(),
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

if (failures) {
  console.error("\nFAILED: " + failures + " assertion(s)");
  process.exit(1);
}
console.log("\nALL PASS");
