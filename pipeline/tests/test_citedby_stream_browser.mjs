// Execute the real citedby panel template with synthetic NDJSON streams.
// No provider, embedding, index-generation, or deployment request is made.
import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import { existsSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join, resolve } from "node:path";
import vm from "node:vm";

const REPO = resolve(dirname(fileURLToPath(import.meta.url)), "..", "..");
const standardPy = "/opt/homebrew/Caskroom/miniconda/base/envs/py312/bin/python";
const pyCandidate = process.env.PAPER_CURATION_PY312 || standardPy;
const py = existsSync(pyCandidate) ? pyCandidate : "python3";
const script = execFileSync(py, ["-c", [
  "import ast, json, pathlib, sys",
  "tree = ast.parse(pathlib.Path(sys.argv[1]).read_text(encoding='utf-8'))",
  "values = {}",
  "for node in tree.body:",
  "    if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):",
  "        name = node.targets[0].id",
  "        if name in ('_JS', 'TOPK', 'POOL', 'PER_PAPER', 'MAX_OUT'):",
  "            values[name] = ast.literal_eval(node.value)",
  "print('var IDX_FILE=\"_citedby_index.json\", COLLECTION=\"_cross\";')",
  "for name in ('TOPK', 'POOL', 'PER_PAPER', 'MAX_OUT'):",
  "    print('var ' + name + '=' + json.dumps(values[name]) + ';')",
  "print(values['_JS'])",
].join("\n"), join(REPO, "pipeline", "lib", "citedby", "deep_panel.py")], {
  encoding: "utf-8",
});

function deferred() {
  let resolve;
  const promise = new Promise((done) => { resolve = done; });
  return { promise, resolve };
}

function ndjsonResponse(events, fragmentSize = Infinity) {
  const bytes = new TextEncoder().encode(events.map((event) => JSON.stringify(event)).join("\n"));
  let offset = 0;
  return {
    ok: true, status: 200,
    body: { getReader() { return { async read() {
      if (offset >= bytes.length) return { done: true };
      const end = Math.min(bytes.length, offset + fragmentSize);
      const value = bytes.slice(offset, end);
      offset = end;
      return { done: false, value };
    } }; } },
  };
}

function answerResponse(text) {
  return ndjsonResponse([
    { event: "delta", text },
    { event: "done", provider: "synthetic", model: "test-model" },
  ]);
}

function controlledStream() {
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
    event(event) {
      deliver({ done: false, value: new TextEncoder().encode(JSON.stringify(event) + "\n") });
    },
    end() { deliver({ done: true }); },
    waitForRead(count) {
      if (reads >= count) return Promise.resolve();
      return new Promise((resolve) => { barriers.push({ count, resolve }); });
    },
  };
}

function fixture() {
  return {
    count: 2,
    papers: {
      protein: { title: "Protein Catalyst", year: 2025 },
      climate: { title: "Climate Policy", year: 2024 },
    },
    chunks: [
      { slug: "protein", section: "Results", text: "protein catalyst evidence" },
      { slug: "climate", section: "Methods", text: "climate policy evidence" },
    ],
  };
}

async function makeHarness(response) {
  const ready = deferred(), elements = new Map(), domReady = [];
  const stats = { requests: [], statuses: [] };
  class Element {
    constructor(id) {
      this.id = id;
      this.value = "";
      this.checked = false;
      this.disabled = false;
      this.style = {};
      this.className = "";
      this.innerHTML = "";
      this.children = [];
      this.listeners = new Map();
    }
    set textContent(text) {
      this.text = String(text);
      if (this.id === "drStatus") {
        stats.statuses.push(this.text);
        if (this.text.startsWith("준비됨")) ready.resolve();
      }
    }
    get textContent() { return this.text || ""; }
    addEventListener(type, handler) {
      const handlers = this.listeners.get(type) || [];
      handlers.push(handler);
      this.listeners.set(type, handlers);
    }
    emit(type, event = {}) {
      return Promise.all((this.listeners.get(type) || []).map((handler) => handler.call(this, event)));
    }
    appendChild(child) { this.children.push(child); return child; }
  }
  const document = {
    getElementById(id) {
      if (!elements.has(id)) elements.set(id, new Element(id));
      return elements.get(id);
    },
    createElement(tag) { return new Element(tag); },
    addEventListener(type, handler) {
      assert.equal(type, "DOMContentLoaded");
      domReady.push(handler);
    },
  };
  const context = {
    console, document, TextDecoder, URL,
    location: { protocol: "http:", hostname: "localhost", href: "http://localhost/report.html" },
    fetch: async (url, init = {}) => {
      if (url === "_citedby_index.json") return { ok: true, async json() { return fixture(); } };
      assert.equal(url, "/api/citedby-answer", "no unexpected network/embedding requests");
      const payload = JSON.parse(init.body);
      stats.requests.push(payload);
      return response(payload, stats.requests.length);
    },
  };
  context.window = context;
  vm.createContext(context);
  new vm.Script(script, { filename: "emitted-citedby-panel.js" }).runInContext(context);
  for (const handler of domReady) handler();
  await ready.promise;
  return {
    context, stats,
    el: (id) => document.getElementById(id),
    click(query) {
      document.getElementById("drQ").value = query;
      return document.getElementById("drGo").emit("click");
    },
    enter(query) {
      document.getElementById("drQ").value = query;
      return document.getElementById("drQ").emit("keydown", { key: "Enter" });
    },
  };
}

console.log("[1] normal citedby Korean stream preserves byte-split citations and EOF metadata");
{
  const h = await makeHarness(() => ndjsonResponse([
    { event: "delta", text: "한국어 근거를 비교합니다 [ref:" },
    { event: "delta", text: "1]." },
    { event: "done", provider: "synthetic", model: "test-model" },
  ], 1));
  await h.click("protein catalyst");
  assert.equal(h.context._citedbyLast.answer, "한국어 근거를 비교합니다 [ref:1].");
  assert.equal(h.context._citedbyLast.model, "synthetic / test-model");
  assert.match(h.el("drAns").innerHTML, /href="#dr-ref-1"/);
  assert.equal(h.stats.requests.length, 1);
  assert.equal(h.el("drGo").disabled, false);
}

console.log("[2] Enter cannot overwrite a pending citedby answer or its references");
{
  const output = controlledStream();
  const h = await makeHarness((_, n) => n === 1 ? output.response : answerResponse("다른 질문의 답변 [ref:1]."));
  const pending = h.click("protein catalyst");
  await output.waitForRead(1);
  output.event({ event: "delta", text: "첫 질문의 문장 [ref:" });
  await output.waitForRead(2);
  await h.enter("climate policy");
  assert.equal(h.stats.requests.length, 1);
  assert.equal(h.context._citedbyLast.q, "protein catalyst");
  assert.equal(h.context._citedbyLast.refs[0].title, "Protein Catalyst");
  assert.equal(h.context._citedbyLast.answer, "첫 질문의 문장 [ref:");
  output.event({ event: "delta", text: "1]." });
  output.event({ event: "done", provider: "synthetic", model: "test-model" });
  output.end();
  await pending;
  assert.equal(h.context._citedbyLast.answer, "첫 질문의 문장 [ref:1].");
  await h.click("climate policy");
  assert.equal(h.stats.requests.length, 2);
  assert.equal(h.context._citedbyLast.q, "climate policy");
  assert.equal(h.context._citedbyLast.answer, "다른 질문의 답변 [ref:1].");
}

console.log("[3] citedby Deeper holds one lock across planning and final streaming");
{
  const plan = controlledStream(), output = controlledStream();
  const h = await makeHarness((payload) => payload.purpose === "plan" ? plan.response : output.response);
  h.el("drDeeper").checked = true;
  const pending = h.click("protein catalyst");
  await plan.waitForRead(1);
  await h.enter("climate policy");
  assert.equal(h.stats.requests.length, 1);
  plan.event({ event: "delta", text: "1. 핵심 연구의 결과를 비교한다." });
  plan.event({ event: "done", provider: "synthetic", model: "planner" });
  plan.end();
  await output.waitForRead(1);
  await h.enter("climate policy");
  assert.equal(h.stats.requests.length, 2);
  assert.equal(h.stats.requests[0].purpose, "plan");
  assert.equal(h.stats.requests[1].purpose, "answer");
  assert.equal(h.stats.requests[1].deeper, true);
  assert.match(h.stats.requests[1].prompt, /핵심 연구의 결과를 비교한다/);
  output.event({ event: "delta", text: "심층 비교의 결론입니다 [ref:" });
  await output.waitForRead(2);
  output.event({ event: "delta", text: "1]." });
  output.event({ event: "done", provider: "synthetic", model: "deeper" });
  output.end();
  await pending;
  assert.equal(h.context._citedbyLast.q, "protein catalyst");
  assert.equal(h.context._citedbyLast.answer, "심층 비교의 결론입니다 [ref:1].");
  assert.equal(h.context._citedbyLast.plan, "1. 핵심 연구의 결과를 비교한다.");
  assert.equal(h.el("drGo").disabled, false);
}

console.log("[4] no-match and stream failures release the lock for a clean later run");
{
  const h = await makeHarness((_, n) => n === 1 ? ndjsonResponse([
    { event: "delta", text: "실패 전의 일부 문장 [ref:" },
    { event: "error", message: "synthetic stream failure" },
  ]) : answerResponse("다시 받은 완결된 답변 [ref:1]."));
  await h.click("quasar astronomy");
  assert.equal(h.stats.requests.length, 0);
  assert.equal(h.el("drGo").disabled, false);
  await h.click("protein catalyst");
  assert.equal(h.el("drGo").disabled, false);
  assert.match(h.el("drStatus").textContent, /synthetic stream failure/);
  await h.click("climate policy");
  assert.equal(h.stats.requests.length, 2);
  assert.equal(h.context._citedbyLast.answer, "다시 받은 완결된 답변 [ref:1].");
  assert.equal(h.context._citedbyLast.refs[0].title, "Climate Policy");
}
console.log("ALL PASS");
