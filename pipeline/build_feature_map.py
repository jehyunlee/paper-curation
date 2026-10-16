#!/usr/bin/env python3
"""Build docs/feature-map.html — an interactive tree of Paper Curation features.

Registry features come from ``pipeline/features.json`` (single source); the
full-curation pipeline, in-browser features and options are described here
because they are workflow stages rather than registry entries. The output is
one self-contained HTML file (no CDN, no network).

Usage:
  PYTHONUTF8=1 python pipeline/build_feature_map.py
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "pipeline" / "features.json"
OUTPUT = ROOT / "docs" / "feature-map.html"

PATH_GROUPS = {
    "reading": ("read", "Read · 읽기·내보내기", "API 키 없이 생성된 결과를 읽고 내보냅니다."),
    "ai": ("ai", "AI · 논문 AI", "선택한 제공자 하나로 논문 한 편 또는 여러 편을 다룹니다."),
    "collection": ("collection", "Collection · 컬렉션 관리", "컬렉션 전체에 대한 색인·지표·동기화. 명시적으로 요청할 때만 실행합니다."),
    "optional": ("optional", "Optional · 선택 기능", "비용이나 외부 전송이 따르는 기능. 각각 따로 계획·확인합니다."),
}

COST = {"local": "로컬 · 비용 없음", "paid": "유료 API", "provider-dependent": "제공자에 따라 다름 (Ollama는 로컬)",
        "unpriced": "외부 서비스 (단가 미산정)"}

DETAILS = {
    "review": "PDF에서 텍스트·그림을 추출하고 선택한 제공자가 6개 섹션 한국어 리뷰(Essence·Motivation·Achievement·How·Originality·Evaluation)를 씁니다. review.md · index.html · bibliography.json을 만듭니다.",
    "summary": "선택한 PDF 본문만 근거로 원문 인용이 붙은 요약을 만듭니다. 인용을 찾지 못한 주장은 거부합니다.",
    "chat": "PDF 본문에 근거한 질의응답. 답마다 원문 인용을 붙입니다.",
    "comparison": "여러 논문을 같은 기준으로 비교하고 각 주장에 원문 인용을 붙입니다.",
    "extract": "로컬 PDF에서 text.md와 figures/를 추출합니다. 텍스트는 OpenDataLoader(없으면 경고 후 PyMuPDF), 그림은 PyMuPDF 기하 크롭.",
    "keyword-search": "BM25 키워드 색인을 만들고 조회합니다. API 키가 필요 없습니다.",
    "semantic-search": "Gemini 임베딩 + BM25를 RRF로 결합한 hybrid 색인·조회.",
    "metrics": "Crossref·OpenAlex·Scopus에서 피인용 이력과 레퍼런스를 누적합니다(기본 30일 증분).",
    "bibliography-update": "서지 DB(SQLite)에 논문·저자·기관 귀속을 반영합니다. 기본 offline.",
    "institution-export": "공개 가능한 기관표를 내보냅니다.",
    "audio": "기존 리뷰로 팟캐스트형 MP3를 만듭니다(Gemini 스크립트 + TTS). 이메일은 보내지 않습니다.",
    "timeline-text": "카테고리별 연구 흐름 내러티브를 씁니다(Anthropic).",
    "timeline-image": "PaperBanana로 카테고리·메인 타임라인 그림을 만듭니다.",
    "zotero-sync": "Zotero 원격 상태와 동기화합니다. 기본 dry-run, 적용 시 로컬 삭제가 일어날 수 있습니다.",
    "publish": "Cloudflare Workers와 gh-pages 스텁으로 배포합니다. 명시적 확인이 필요합니다.",
    "email": "이미 만든 MP3를 Resend로 보냅니다.",
}


def n(label, desc, *, kind="stage", meta=None, children=None):
    node = {"label": label, "desc": desc, "kind": kind}
    if meta:
        node["meta"] = meta
    if children:
        node["children"] = children
    return node


def registry_nodes(features):
    groups = {key: [] for key in PATH_GROUPS}
    for f in features:
        cred = f.get("credential", {})
        meta = {
            "기능 ID": f["id"],
            "모듈": f.get("module", ""),
            "그룹": f.get("group", ""),
            "제공자": ", ".join(f.get("supported_providers") or []) or "없음",
            "비용": COST.get(cred.get("cost_class"), cred.get("cost_class", "")),
            "전송": cred.get("transmission", ""),
            "런타임": ", ".join(f.get("runtime") or []),
        }
        node = n(f"{f.get('label_ko', f['id'])}", DETAILS.get(f["id"], f.get("label_en", "")),
                 kind="feature", meta=meta)
        groups.setdefault(f.get("start_path", "optional"), []).append(node)
    out = []
    for key, (kind, label, desc) in PATH_GROUPS.items():
        if groups.get(key):
            out.append(n(label, desc, kind=kind, children=groups[key]))
    return out


def build_tree(features):
    return n("Paper Curation", "Zotero 논문을 구조화 리뷰·분류·연결·검색·타임라인으로 바꾸는 시스템입니다. 노드를 눌러 설명을 보고, ▸ 를 눌러 펼치세요.", kind="root", children=[
        n("시작점", "같은 공통 실행기로 들어가는 세 가지 입구.", kind="group", children=[
            n("Paper Curio (Zotero 우클릭)", "Zotero 9/10 플러그인. 논문 우클릭 → 리뷰 생성, 기능 모듈, AI Chat, Citedby.", meta={"설치": "paper-curio-zotero9.xpi / zotero10.xpi"}),
            n("명령줄 run_feature.py", "기능 하나를 계획(plan) → 확인 → 실행(execute)합니다."),
            n("전체 큐레이션 run_full.py", "컬렉션 전체를 순서대로 처리하는 고급 경로. 아래 '전체 큐레이션 파이프라인' 참조."),
        ]),
        n("공통 실행기", "모든 기능이 같은 안전장치를 거칩니다.", kind="group", children=[
            n("레지스트리 features.json", f"기능 {len(features)}개의 요구조건·제공자·전송 대상·비용을 정의합니다."),
            n("계획 (plan)", "실행 전 요구조건, 데이터가 전송되는 곳, 비용을 JSON으로 보여줍니다. 쓰기 없음."),
            n("확인", "사용자가 계획을 보고 승인합니다. 배포·동기화·이메일은 명시적 확인 필수."),
            n("실행 (execute)", "코퍼스 예약·등록 잠금, 비용 상한, 실패 시 부분 결과 보존, 다른 제공자로 자동 전송 없음."),
            n("자격증명", "환경변수 → OS 키 저장소(credential:<provider>). 평문 설정 파일에 키를 저장하지 않습니다."),
        ]),
        n("기능 (레지스트리)", "pipeline/features.json에 등록된 독립 기능. 경로별로 묶었습니다.", kind="group",
          children=registry_nodes(features)),
        n("전체 큐레이션 파이프라인", "run_full.py --mode curate가 아래 단계를 순서대로 실행합니다.", kind="group", children=[
            n("수집", "논문을 모아 Zotero와 맞춥니다.", children=[
                n("검색 · 등록 (선택)", "arXiv · Semantic Scholar · OpenAlex 병렬 검색 후 Zotero 등록."),
                n("동기화", "Zotero 컬렉션 변경분을 가져옵니다."),
                n("중복 정리", "같은 논문의 중복 항목을 찾습니다(dry-run 기본)."),
                n("PDF 연결 감사", "audit_zotero_pdf: 서지정보와 PDF 내용이 맞는지 확인합니다."),
            ]),
            n("리뷰", "논문마다 구조화 리뷰를 만듭니다.", children=[
                n("텍스트·그림 추출", "OpenDataLoader → PyMuPDF fallback, 그림은 기하 크롭."),
                n("서지-PDF 일치 검사", "Zotero 제목·DOI와 PDF가 다르면 리뷰하지 않습니다."),
                n("구조화 리뷰", "Claude Sonnet이 6섹션 한국어 review.md 작성."),
                n("피인용·레퍼런스", "citations.md 누적 + references.md (soft step)."),
            ]),
            n("분석", "카테고리와 논문 관계를 만듭니다.", children=[
                n("토픽 모델링·분류", "SPECTER2 + UMAP + HDBSCAN. LLM 호출 0회. 한 논문은 최대 3개 카테고리."),
                n("같이 보면 좋은 논문", "SPECTER2 + 제목·저자 BM25 RRF 후보 → Claude Haiku가 두 리뷰를 읽고 공통점·차이를 담은 한 문장 작성. 무관한 쌍 제거, 판정 결과 캐시."),
                n("카테고리 요약", "카테고리별 요약과 세부 주제."),
                n("타임라인", "Opus 내러티브 + PaperBanana 카테고리·메인 타임라인 그림."),
            ]),
            n("출판", "읽을 수 있는 결과물을 만듭니다.", children=[
                n("검증", "validate_papers --strict: 섹션·링크·그림·타임라인 정합성."),
                n("논문 페이지", "review_to_html: 논문별 index.html."),
                n("토픽 인덱스", "build_topic_index: 카테고리 카드, Deep Research, Audio Overview 내장."),
                n("검색 인덱스", "BM25 + Gemini 임베딩 hybrid 색인과 전체 통합 인덱스."),
                n("서지 DB", "build → finalize → 연결 반영 → strict 검사 → 맥미니 전송."),
                n("로컬 열람", "serve_local.py로 전체 텍스트와 함께 열람."),
            ]),
        ]),
        n("브라우저 안 기능", "토픽 페이지에서 바로 쓰는 기능.", kind="group", children=[
            n("Deep Research", "자연어 질문 → hybrid 검색 → 독자 자신의 키(Anthropic/OpenAI/Google)로 답변 + [N] 인용."),
            n("Audio Overview", "Gemini TTS로 MP3를 만들어 내려받습니다(배포본은 이메일 전달 가능)."),
            n("Obsidian 연동", "메모가 다음 질의에 반영되는 지식 축적."),
        ]),
        n("선택 옵션", "플래그나 모드로 켤 때만 실행.", kind="optional", children=[
            n("O-1 콘텐츠 배포", "--mode deploy: Cloudflare Workers + gh-pages 스텁."),
            n("O-2 Insights + 네트워크", "--insights: 카테고리 간 인사이트 + UMAP 2D/3D 인터랙티브 네트워크."),
            n("워크플로 그림", "generate_usage_diagram / generate_workflow: 고양이 스타일 기본, --style plain 대체."),
        ]),
        n("분석·관리 도구", "파이프라인 밖에서 쓰는 도구.", kind="group", children=[
            n("Citedby", "한 논문의 인용 계보를 OpenAlex·Scopus·S2·arXiv에서 모아 HTML 보고서로 만듭니다."),
            n("저자·기관 귀속", "OpenAlex → Scopus → PDF 바이라인 → ROR/ORCID 순서로 저자-기관을 확정합니다."),
            n("복구 도구", "auto_recover · fix_matching · validate: 잘못 연결된 PDF와 깨진 리뷰를 찾아 고칩니다."),
            n("기관 보고서", "서지 DB로 연구 흐름·병렬 연구실·대표 연구자 보고서를 만듭니다."),
        ]),
    ])


TEMPLATE = r"""<!doctype html>
<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Paper Curation 기능 지도</title>
<style>
:root{--bg:#fbfaf7;--ink:#1f2933;--muted:#6b7280;--line:#cbd5e1;--root:#334155;--group:#475569;--read:#3f8f5f;--ai:#3b6bb5;--collection:#c57a2e;--optional:#8b5cf6;--feature:#0f766e;--stage:#64748b}
*{box-sizing:border-box}body{margin:0;font:15px/1.55 -apple-system,BlinkMacSystemFont,"Apple SD Gothic Neo","Noto Sans KR",sans-serif;background:var(--bg);color:var(--ink)}
header{padding:18px 24px 10px;border-bottom:1px solid #e5e7eb;background:#fff;display:flex;gap:16px;align-items:center;flex-wrap:wrap}
h1{font-size:20px;margin:0 12px 0 0}
input{padding:8px 12px;border:1px solid var(--line);border-radius:999px;min-width:240px;font:inherit}
button{padding:7px 12px;border:1px solid var(--line);border-radius:999px;background:#fff;cursor:pointer;font:inherit}
button:hover{background:#f1f5f9}
.legend{display:flex;gap:10px;flex-wrap:wrap;font-size:13px;color:var(--muted)}
.legend span::before{content:"";display:inline-block;width:10px;height:10px;border-radius:50%;margin-right:5px;background:var(--c)}
main{display:grid;grid-template-columns:minmax(0,1fr) minmax(300px,380px);height:calc(100vh - 66px)}
#tree{overflow:auto;padding:28px 24px 80px}
.tree ul{position:relative;display:flex;flex-direction:column;justify-content:center;gap:10px;margin:0;padding:0 0 0 34px;list-style:none}
.tree>ul{padding-left:0}
.tree li{position:relative;display:flex;align-items:center;margin:0}
.tree li::before{content:"";position:absolute;left:-17px;top:50%;width:17px;border-top:1.6px solid var(--line)}
.tree>ul>li::before{display:none}
.tree li::after{content:"";position:absolute;left:-17px;top:-5px;bottom:-5px;border-left:1.6px solid var(--line)}
.tree li:first-child::after{top:50%}.tree li:last-child::after{bottom:50%}.tree li:only-child::after{display:none}
.tree>ul>li::after{display:none}
.tree li>ul::before{content:"";position:absolute;left:0;top:50%;width:17px;border-top:1.6px solid var(--line)}
.node{display:inline-flex;align-items:center;gap:6px;padding:7px 12px;border-radius:12px;background:#fff;border:1.6px solid var(--c,#94a3b8);cursor:pointer;user-select:none;white-space:nowrap;transition:.12s;box-shadow:0 1px 2px rgba(0,0,0,.04)}
.node:hover{transform:translateY(-1px);box-shadow:0 4px 12px rgba(0,0,0,.09)}
.node.sel{background:var(--c);color:#fff}
.node.hit{outline:3px solid #facc15;outline-offset:2px}
.tog{width:14px;text-align:center;color:var(--muted);font-size:12px}
.node.sel .tog{color:#fff}
.badge{font-size:11px;padding:1px 6px;border-radius:999px;background:#f1f5f9;color:#475569}
.node.sel .badge{background:rgba(255,255,255,.25);color:#fff}
li.closed>ul{display:none}
aside{border-left:1px solid #e5e7eb;background:#fff;padding:22px;overflow:auto;overflow-wrap:anywhere}
aside h2{margin:0 0 4px;font-size:18px}
.path{font-size:12px;color:var(--muted);margin-bottom:12px}
.kind{display:inline-block;font-size:12px;padding:2px 8px;border-radius:999px;color:#fff;background:var(--c);margin-bottom:10px}
aside p{margin:0 0 14px}
dl{display:grid;grid-template-columns:max-content 1fr;gap:6px 12px;font-size:13px;margin:0 0 14px}
dt{color:var(--muted);white-space:nowrap}dd{margin:0;overflow-wrap:anywhere}
.kids a{display:block;padding:4px 0;color:#2563eb;cursor:pointer;font-size:14px}
@media(max-width:860px){main{grid-template-columns:1fr;height:auto}aside{border-left:0;border-top:1px solid #e5e7eb}}
</style></head><body>
<header><h1>Paper Curation 기능 지도</h1>
<input id="q" placeholder="기능 검색 (예: 리뷰, BM25, 배포)">
<button id="open">모두 펼치기</button><button id="close">모두 접기</button>
<div class="legend">
<span style="--c:var(--read)">Read</span><span style="--c:var(--ai)">AI</span><span style="--c:var(--collection)">Collection</span><span style="--c:var(--optional)">선택</span><span style="--c:var(--feature)">레지스트리 기능</span><span style="--c:var(--stage)">단계</span>
</div></header>
<main><section id="tree" class="tree"></section><aside id="panel"></aside></main>
<script>
const TREE = __TREE__;
const COLORS={root:"var(--root)",group:"var(--group)",read:"var(--read)",ai:"var(--ai)",collection:"var(--collection)",optional:"var(--optional)",feature:"var(--feature)",stage:"var(--stage)"};
const KIND={root:"전체",group:"영역",read:"Read 경로",ai:"AI 경로",collection:"Collection 경로",optional:"선택 기능",feature:"레지스트리 기능",stage:"단계"};
let id=0;const byId={};
function index(node,parent,depth){node.id=++id;node.parent=parent;node.depth=depth;byId[node.id]=node;(node.children||[]).forEach(c=>index(c,node,depth+1));}
index(TREE,null,0);
function color(node){let n=node;while(n&&(n.kind==="stage"))n=n.parent;return COLORS[n?n.kind:"stage"];}
function render(node){
  const li=document.createElement("li");li.dataset.id=node.id;
  if(node.depth>=1&&node.children)li.classList.add("closed");
  const d=document.createElement("span");d.className="node";d.style.setProperty("--c",node.kind==="stage"?color(node):COLORS[node.kind]);
  const t=document.createElement("span");t.className="tog";t.textContent=node.children?(li.classList.contains("closed")?"▸":"▾"):"•";
  d.append(t,document.createTextNode(node.label));
  if(node.children){const b=document.createElement("span");b.className="badge";b.textContent=node.children.length;d.append(b);}
  d.onclick=()=>{if(node.children)toggle(li);select(node,true);};
  li.append(d);
  if(node.children){const ul=document.createElement("ul");node.children.forEach(c=>ul.append(render(c)));li.append(ul);}
  node.el=d;node.li=li;return li;
}
function toggle(li,force){const closed=force===undefined?!li.classList.contains("closed"):force;li.classList.toggle("closed",closed);
  const t=li.querySelector(":scope>.node>.tog");if(t&&li.querySelector(":scope>ul"))t.textContent=closed?"▸":"▾";}
function path(node){const p=[];let n=node.parent;while(n){p.unshift(n.label);n=n.parent;}return p.join(" › ");}
function esc(s){return String(s).replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));}
function select(node,keep){
  document.querySelectorAll(".node.sel").forEach(e=>e.classList.remove("sel"));node.el.classList.add("sel");
  let n=node.parent;while(n){toggle(n.li,false);n=n.parent;}
  if(!keep&&node.children)toggle(node.li,false);
  const c=node.kind==="stage"?color(node):COLORS[node.kind];
  let h=`<div class="path">${esc(path(node))||"&nbsp;"}</div><h2>${esc(node.label)}</h2><span class="kind" style="--c:${c}">${KIND[node.kind]}</span><p>${esc(node.desc)}</p>`;
  if(node.meta){h+="<dl>"+Object.entries(node.meta).filter(([,v])=>v).map(([k,v])=>`<dt>${esc(k)}</dt><dd>${esc(v)}</dd>`).join("")+"</dl>";}
  if(node.children){h+=`<div class="kids"><b>하위 항목 ${node.children.length}개</b>`+node.children.map(k=>`<a data-id="${k.id}">${esc(k.label)}</a>`).join("")+"</div>";}
  const panel=document.getElementById("panel");panel.innerHTML=h;
  panel.querySelectorAll("a[data-id]").forEach(a=>a.onclick=()=>{const k=byId[a.dataset.id];select(k);k.el.scrollIntoView({block:"center",inline:"center",behavior:"smooth"});});
  history.replaceState(null,"","#"+encodeURIComponent(node.label));
}
const root=document.createElement("ul");root.append(render(TREE));document.getElementById("tree").append(root);
document.getElementById("open").onclick=()=>document.querySelectorAll("li").forEach(li=>li.querySelector(":scope>ul")&&toggle(li,false));
document.getElementById("close").onclick=()=>document.querySelectorAll("li").forEach(li=>{if(byId[li.dataset.id].depth>=1&&li.querySelector(":scope>ul"))toggle(li,true);});
document.getElementById("q").oninput=e=>{const q=e.target.value.trim().toLowerCase();
  Object.values(byId).forEach(n=>{const hit=q&&(n.label+" "+n.desc+" "+JSON.stringify(n.meta||{})).toLowerCase().includes(q);n.el.classList.toggle("hit",!!hit);
    if(hit){let p=n.parent;while(p){toggle(p.li,false);p=p.parent;}}});};
const hash=decodeURIComponent(location.hash.slice(1));select(Object.values(byId).find(n=>n.label===hash)||TREE);
</script></body></html>
"""


def main() -> int:
    features = json.loads(REGISTRY.read_text(encoding="utf-8"))["features"]
    tree = build_tree(features)
    payload = json.dumps(tree, ensure_ascii=False).replace("</", "<\\/")
    OUTPUT.write_text(TEMPLATE.replace("__TREE__", payload), encoding="utf-8")
    print(f"wrote {OUTPUT.relative_to(ROOT)} ({len(features)} registry features)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
