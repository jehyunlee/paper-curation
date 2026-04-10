"""
D3.js force-directed network visualization.

_paper_connections.json + _papers_index.json → network.html
- Category colors, score-based node size, hover (essence), click (review link)
- Category toggle, relation type filter, search, ego network

Usage:
  PYTHONUTF8=1 python pipeline/generate_network.py --topic ai4s
  PYTHONUTF8=1 python pipeline/generate_network.py --topic scisci
"""

import argparse
import json
import os
from collections import defaultdict
from datetime import datetime

from config_loader import PAPERS_DIR as _PAPERS_DIR, get_topic_dir

PAPERS_DIR = str(_PAPERS_DIR)

RELATION_COLORS = {
    "alternative": "#3B82F6",
    "extension": "#10B981",
    "foundation": "#8B5CF6",
    "counterpoint": "#F59E0B",
    "application": "#EF4444",
}


def log(msg):
    ts = datetime.now().strftime("%H:%M:%S")
    print(f"[{ts}] {msg}", flush=True)


def build_network_data(topic):
    with open(os.path.join(PAPERS_DIR, "_papers_index.json"), "r", encoding="utf-8") as f:
        all_papers = json.load(f)

    topic_dir = str(get_topic_dir(topic))
    with open(os.path.join(topic_dir, "_paper_connections.json"), "r", encoding="utf-8") as f:
        connections = json.load(f)

    # Load UMAP coordinates if available
    umap_path = os.path.join(topic_dir, "_umap_coords.json")
    umap_coords = {}
    if os.path.exists(umap_path):
        with open(umap_path, "r", encoding="utf-8") as f:
            umap_coords = json.load(f)

    topic_papers = [p for p in all_papers if topic in p.get("topics", [])]

    # Tab10 base colors + shade function for sub-categories
    TAB10 = [
        (31, 119, 180), (255, 127, 14), (44, 160, 44), (214, 39, 40),
        (148, 103, 189), (140, 86, 75), (227, 119, 194), (127, 127, 127),
        (188, 189, 34), (23, 190, 207),
    ]

    def _shade(rgb, factor):
        """Lighten (>1) or darken (<1) a color."""
        r, g, b = rgb
        if factor > 1:
            r = min(255, int(r + (255 - r) * (factor - 1)))
            g = min(255, int(g + (255 - g) * (factor - 1)))
            b = min(255, int(b + (255 - b) * (factor - 1)))
        else:
            r = int(r * factor)
            g = int(g * factor)
            b = int(b * factor)
        return f"#{r:02x}{g:02x}{b:02x}"

    all_cat_names = sorted(set(
        p.get("classifications", {}).get(topic, {}).get("primary_category", "Other")
        for p in topic_papers
    ))
    SHAPES = ["circle", "square", "triangle", "diamond"]
    cat_colors = {}
    cat_shapes = {}
    for i, c in enumerate(all_cat_names):
        if c == "Other":
            cat_colors[c] = "#999999"
            cat_shapes[c] = "circle"
        else:
            base = TAB10[i % len(TAB10)]
            shade_level = 1.0 + 0.3 * (i // len(TAB10))
            cat_colors[c] = _shade(base, shade_level)
            cat_shapes[c] = SHAPES[(i // len(TAB10)) % len(SHAPES)]

    nodes = []
    slug_set = set()
    for p in topic_papers:
        slug = p["slug"]
        cls = p.get("classifications", {}).get(topic, {})
        cat = cls.get("primary_category", "Other")
        sub = cls.get("sub_category", "")
        score = p.get("score", 0) or 0
        year = str(p.get("date", ""))[:4]
        num = slug.split("_")[0] if "_" in slug else ""
        all_cats = cls.get("all_categories", [cat])
        is_multi = len(all_cats) > 1
        coord = umap_coords.get(slug, {})
        nodes.append({
            "id": slug, "num": num, "title": p.get("title", ""),
            "category": cat, "all_categories": all_cats,
            "sub_category": sub, "score": score,
            "year": year, "essence": (p.get("essence", "") or "")[:200],
            "color": cat_colors.get(cat, "#999999"),
            "shape": cat_shapes.get(cat, "circle"),
            "multi": is_multi,
            "ux": coord.get("x"), "uy": coord.get("y"),
            "ux3": coord.get("x3"), "uy3": coord.get("y3"), "uz3": coord.get("z3"),
        })
        slug_set.add(slug)

    links = []
    for slug, conns in connections.items():
        if slug not in slug_set:
            continue
        for c in conns:
            target = c.get("slug", "")
            if target in slug_set:
                links.append({
                    "source": slug, "target": target,
                    "relation": c.get("relation", "alternative"),
                    "reason": c.get("reason", ""),
                    "color": RELATION_COLORS.get(c.get("relation", ""), "#ccc"),
                })

    cats = sorted(set(n["category"] for n in nodes))
    years = sorted(set(n["year"] for n in nodes if n["year"] and n["year"].isdigit() and 1900 <= int(n["year"]) <= 2100))

    # Sub-category colors: shade of parent category color
    # Build cat → sub mapping
    cat_subs = defaultdict(set)
    for n in nodes:
        cat_subs[n["category"]].add(n.get("sub_category", "General"))

    # Find parent tab10 index for each category
    cat_to_tab_idx = {}
    for i, c in enumerate(all_cat_names):
        if c != "Other":
            cat_to_tab_idx[c] = i % len(TAB10)

    sub_colors = {}
    for cat, subs in cat_subs.items():
        tab_idx = cat_to_tab_idx.get(cat, 7)  # default gray
        base = TAB10[tab_idx]
        sorted_subs = sorted(subs)
        for j, s in enumerate(sorted_subs):
            # Vary shade: 0.6 (dark) → 1.4 (light) across sub-categories
            n_subs = len(sorted_subs)
            factor = 0.6 + 0.8 * j / max(1, n_subs - 1) if n_subs > 1 else 1.0
            sub_colors[s] = _shade(base, factor)

    has3D = any(n.get("ux3") is not None for n in nodes)
    return nodes, links, cat_colors, cat_shapes, sub_colors, years, has3D


def _escape_html(text):
    """Escape HTML special characters."""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;").replace("'", "&#x27;")


def generate_html(nodes, links, cat_colors, cat_shapes, sub_colors, years, topic, has3D=False):
    nodes_json = json.dumps(nodes, ensure_ascii=False)
    links_json = json.dumps(links, ensure_ascii=False)
    cat_colors_json = json.dumps(cat_colors, ensure_ascii=False)

    year_min = years[0] if years else "2020"
    year_max = years[-1] if years else "2026"

    # Pre-compute category counts
    cat_counts = {}
    for n in nodes:
        cat_counts[n["category"]] = cat_counts.get(n["category"], 0) + 1
    cat_shapes_json = json.dumps(cat_shapes, ensure_ascii=False)
    cat_counts_json = json.dumps(cat_counts, ensure_ascii=False)
    sub_colors_json = json.dumps(sub_colors, ensure_ascii=False)
    sub_counts = {}
    for n in nodes:
        sc = n.get("sub_category", "")
        if sc:
            sub_counts[sc] = sub_counts.get(sc, 0) + 1
    sub_counts_json = json.dumps(sub_counts, ensure_ascii=False)
    # cat → subs hierarchy
    cat_subs_map = defaultdict(list)
    for n in nodes:
        sc = n.get("sub_category", "General")
        if sc not in cat_subs_map[n["category"]]:
            cat_subs_map[n["category"]].append(sc)
    for k in cat_subs_map:
        cat_subs_map[k].sort()
    cat_subs_json = json.dumps(dict(cat_subs_map), ensure_ascii=False)

    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{_escape_html(topic)} &mdash; Paper Network</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/font-kopub/1.0/kopubdotum.css">
<script src="https://d3js.org/d3.v7.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/three@0.128.0/build/three.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js"></script>
<style>
* {{ margin:0;padding:0;box-sizing:border-box; }}
:root {{
  --bg:#0a0a1a; --panel:#14142a; --panel-border:#333; --text:#e0e0e0; --text-dim:#aaa;
  --text-muted:#888; --text-faint:#666; --input-bg:#1a1a2e; --input-border:#444;
  --accent:#4361EE; --accent-hover:#5a75f5; --node-stroke:#1a1a2e; --ghost-opacity:0.08;
}}
body.light {{
  --bg:#f5f5f8; --panel:#ffffff; --panel-border:#ddd; --text:#222; --text-dim:#555;
  --text-muted:#777; --text-faint:#999; --input-bg:#f0f0f5; --input-border:#ccc;
  --accent:#3351D6; --accent-hover:#4a66ee; --node-stroke:#f5f5f8; --ghost-opacity:0.12;
}}
body {{ font-family:'KoPub Dotum',-apple-system,sans-serif;background:var(--bg);color:var(--text);overflow:hidden; }}
svg {{ width:100vw;height:100vh; }}
#controls {{
  position:fixed;top:1rem;left:1rem;width:280px;
  background:var(--panel);border-radius:12px;padding:1rem;
  box-shadow:0 4px 20px rgba(0,0,0,0.5);z-index:10;
  max-height:calc(100vh - 2rem);overflow-y:auto;
  transition:width 0.25s ease,padding 0.25s ease;
}}
#controls.collapsed {{
  width:40px;padding:0.5rem;overflow:hidden;
}}
#controls.collapsed .controls-inner {{ display:none; }}
#controls-toggle {{
  position:absolute;top:0.5rem;right:0.5rem;
  background:none;border:none;color:var(--text-dim);cursor:pointer;
  font-size:0.9rem;line-height:1;padding:0.1rem 0.3rem;
  border-radius:4px;
}}
#controls-toggle:hover {{ color:var(--text);background:var(--input-bg); }}
#controls.collapsed #controls-toggle {{ right:0.3rem;top:0.3rem; }}
#controls h2 {{ font-size:1.1rem;margin-bottom:0.8rem;color:var(--text);padding-right:1.5rem; }}
#controls h3 {{ font-size:0.82rem;color:var(--text-dim);margin:0.8rem 0 0.4rem;text-transform:uppercase;letter-spacing:0.05em; }}
#search {{ width:100%;padding:0.5rem 0.8rem;border:1px solid var(--input-border);border-radius:8px;background:var(--input-bg);color:var(--text);font-size:0.9rem;font-family:inherit;outline:none;margin-bottom:0.3rem; }}
#search:focus {{ border-color:var(--accent); }}
#search-count {{ font-size:0.75rem;color:var(--text-muted);margin-bottom:0.5rem;min-height:1em; }}
.cat-toggle {{ display:flex;align-items:center;gap:0.5rem;padding:0.2rem 0;cursor:pointer;font-size:0.82rem;user-select:none; }}
.cat-toggle:hover {{ color:var(--text); }}
.cat-dot {{ width:10px;height:10px;border-radius:50%;flex-shrink:0; }}
.cat-toggle.off {{ opacity:0.25; }}
.cat-count {{ color:var(--text-faint);font-size:0.75rem;margin-left:auto; }}
.rel-toggle {{ display:inline-flex;align-items:center;gap:0.3rem;padding:0.2rem 0.6rem;border-radius:12px;margin:0.15rem;font-size:0.75rem;cursor:pointer;user-select:none;border:1px solid;opacity:0.9; }}
.rel-toggle.off {{ opacity:0.2; }}
#year-slider-box input[type=range] {{ width:100%;accent-color:#4361EE; }}
.hl-btn {{ display:inline-block;padding:0.2rem 0.6rem;border-radius:12px;margin:0.15rem;font-size:0.75rem;cursor:pointer;user-select:none;border:1px solid var(--text-faint);color:var(--text);transition:all 0.15s; }}
.hl-btn:hover {{ border-color:var(--accent);color:var(--text); }}
.hl-btn.active {{ background:var(--accent);border-color:var(--accent);color:var(--text); }}
.cat-tree-item {{ margin-bottom:0.2rem; }}
.cat-tree-header {{ display:flex;align-items:center;gap:0.4rem;padding:0.2rem 0;cursor:pointer;font-size:0.82rem;user-select:none; }}
.cat-tree-header:hover {{ color:var(--text); }}
.cat-tree-header.off {{ opacity:0.25; }}
.cat-tree-arrow {{ font-size:0.65rem;color:var(--text-faint);width:12px;text-align:center; }}
.cat-tree-subs {{ margin-left:1.2rem;display:none; }}
.cat-tree-subs.open {{ display:block; }}
.sub-toggle-item {{ display:flex;align-items:center;gap:0.4rem;padding:0.1rem 0;cursor:pointer;font-size:0.75rem;user-select:none;color:var(--text-dim); }}
.sub-toggle-item:hover {{ color:var(--text); }}
.sub-toggle-item.off {{ opacity:0.25; }}
#force-controls input[type=range] {{ width:100%;accent-color:#4361EE; }}
.force-row {{ display:flex;align-items:center;gap:0.5rem;font-size:0.78rem;color:var(--text-dim);margin:0.2rem 0; }}
.force-row span {{ min-width:50px; }}
#info {{
  position:fixed;top:0;right:0;width:420px;height:100vh;
  background:var(--panel);border-radius:0;padding:1.2rem;
  border-left:1px solid var(--panel-border);
  box-shadow:-4px 0 20px rgba(0,0,0,0.5);z-index:11;
  overflow-y:auto;
  transform:translateX(100%);
  transition:transform 0.28s cubic-bezier(0.4,0,0.2,1);
}}
#info.open {{ transform:translateX(0); }}
#info-close {{
  position:absolute;top:0.7rem;right:0.8rem;
  background:none;border:none;color:var(--text-muted);cursor:pointer;
  font-size:1.2rem;line-height:1;padding:0.2rem 0.4rem;
  border-radius:4px;
}}
#info-close:hover {{ color:var(--text);background:var(--input-bg); }}
#info h3 {{ font-size:0.95rem;color:var(--text);margin-bottom:0.4rem;padding-right:2rem; }}
.info-meta {{ font-size:0.8rem;color:var(--text-dim);margin-bottom:0.4rem; }}
.info-essence {{ font-size:0.85rem;color:var(--text);line-height:1.5;margin-bottom:0.5rem; }}
.info-actions {{ font-size:0.8rem;margin-bottom:0.5rem; }}
.info-actions a {{ color:#4361EE;text-decoration:none;cursor:pointer; }}
.info-actions a:hover {{ text-decoration:underline; }}
.review-btn {{
  display:inline-block;padding:0.35rem 0.9rem;border-radius:8px;
  background:var(--accent);color:var(--text) !important;font-size:0.82rem;
  text-decoration:none !important;margin-bottom:0.4rem;
}}
.review-btn:hover {{ background:#5a75f5;text-decoration:none !important; }}
.conn-item {{ font-size:0.78rem;padding:0.15rem 0;color:var(--text-dim); }}
.conn-rel {{ font-weight:600;margin-right:0.3rem; }}
.conn-link {{ color:var(--text);cursor:pointer;text-decoration:none; }}
.conn-link:hover {{ color:var(--text);text-decoration:underline; }}
#stats {{
  position:fixed;top:1rem;right:1rem;
  background:var(--panel);border-radius:12px;padding:0.8rem 1rem;
  font-size:0.8rem;color:var(--text-muted);z-index:10;
}}
#stats span {{ color:var(--text);font-weight:600; }}
#info-hint-btn {{
  background:none;border:none;color:var(--text-faint);cursor:pointer;
  font-size:0.8rem;margin-left:0.5rem;
  border-radius:50%;width:1.2rem;height:1.2rem;
  display:inline-flex;align-items:center;justify-content:center;
}}
#info-hint-btn:hover {{ color:var(--text);background:var(--input-bg); }}
#shortcuts-popup {{
  display:none;position:fixed;top:3.2rem;right:1rem;
  background:var(--panel);border:1px solid var(--panel-border);border-radius:10px;
  padding:0.8rem 1rem;font-size:0.78rem;color:var(--text);z-index:30;
  min-width:240px;box-shadow:0 4px 16px rgba(0,0,0,0.6);
}}
#shortcuts-popup.open {{ display:block; }}
#shortcuts-popup h4 {{ color:var(--text);margin-bottom:0.5rem;font-size:0.82rem; }}
#shortcuts-popup table {{ border-collapse:collapse;width:100%; }}
#shortcuts-popup td {{ padding:0.15rem 0.4rem; }}
#shortcuts-popup td:first-child {{ color:#4361EE;font-family:monospace;white-space:nowrap; }}
#tooltip {{
  position:fixed;background:var(--panel);color:var(--text);
  padding:0.5rem 0.9rem;border-radius:6px;font-size:0.78rem;
  pointer-events:none;z-index:20;max-width:400px;line-height:1.4;display:none;
}}
#tooltip .tt-title {{ font-weight:600;margin-bottom:0.2rem; }}
#tooltip .tt-essence {{ color:var(--text-dim);font-size:0.74rem;margin-top:0.2rem; }}
#tooltip .tt-score {{ display:inline-block;width:8px;height:8px;border-radius:50%;margin-right:0.3rem;vertical-align:middle; }}
.link-tooltip {{
  position:fixed;background:var(--panel);color:var(--text);
  padding:0.35rem 0.7rem;border-radius:6px;font-size:0.75rem;
  pointer-events:none;z-index:20;max-width:320px;line-height:1.4;display:none;
}}
#node-labels {{ pointer-events:none; }}
.node-label {{
  font-size:10px;fill:#fff;
  text-shadow:0 1px 3px #000;
  paint-order:stroke;stroke:#000;stroke-width:3px;
}}
#canvas3d {{ position:fixed;top:0;left:0;width:100vw;height:100vh;display:none;z-index:1; }}
</style>
</head>
<body>
<div id="controls">
  <button id="controls-toggle" title="Collapse/Expand">&laquo;</button>
  <div class="controls-inner">
  <h2>{_escape_html(topic)} Paper Network</h2>
  <input type="text" id="search" placeholder="Search papers...">
  <div id="search-count"></div>
  <h3>Color by</h3>
  <div id="colorby-btns">
    <span class="hl-btn active" id="colorby-cat">Category</span>
    <span class="hl-btn" id="colorby-sub">Sub-category</span>
  </div>
  <h3>Categories <span class="hl-btn" id="sel-all" style="font-size:0.65rem">All</span> <span class="hl-btn" id="sel-none" style="font-size:0.65rem">None</span></h3>
  <div id="cat-tree"></div>
  <h3>Relations</h3>
  <div id="rel-filters"></div>
  <h3>Year Filter</h3>
  <div id="year-slider-box">
    <input type="range" id="year-min" min="{year_min}" max="{year_max}" value="{year_min}" style="width:120px">
    <input type="range" id="year-max" min="{year_min}" max="{year_max}" value="{year_max}" style="width:120px">
    <div id="year-label" style="font-size:0.8rem;color:#ccc;margin-top:0.2rem">{year_min} &mdash; {year_max}</div>
  </div>
  <h3>Highlight</h3>
  <div id="highlight-btns">
    <span class="hl-btn" id="hl-hub">Hub (top 10)</span>
    <span class="hl-btn" id="hl-bridge">Bridge</span>
    <span class="hl-btn" id="hl-reset">Reset</span>
  </div>
  <h3>View</h3>
  <div id="view-btns">
    <span class="hl-btn" id="view-reset" title="Reset zoom, pan and position to the initial layout">Reset View</span>
  </div>
  <h3>Layout</h3>
  <div id="layout-btns">
    <span class="hl-btn active" id="layout-umap">UMAP 2D</span>
    {'<span class="hl-btn" id="layout-3d">UMAP 3D</span>' if has3D else ''}
    <span class="hl-btn" id="layout-force">Force</span>
  </div>
  <h3>Node Size <span id="node-size-label" style="font-size:0.75rem;color:#ccc">1.0x</span></h3>
  <div><input type="range" id="node-size-slider" min="0.2" max="3.0" step="0.1" value="1.0" style="width:100%;accent-color:#4361EE"></div>
  <h3>Theme</h3>
  <div id="theme-btns">
    <span class="hl-btn active" id="theme-dark">Dark</span>
    <span class="hl-btn" id="theme-light">Light</span>
  </div>
  <h3>Force</h3>
  <div id="force-controls">
    <div class="force-row"><span>Repulsion</span><input type="range" id="f-charge" min="-300" max="-10" value="-80"></div>
    <div class="force-row"><span>Distance</span><input type="range" id="f-dist" min="10" max="200" value="60"></div>
    <div class="force-row"><span>Link</span><input type="range" id="f-str" min="5" max="100" value="40"></div>
    <div class="force-row"><span>Gravity</span><input type="range" id="f-grav" min="1" max="20" value="5"></div>
  </div>
  </div>
</div>
<div id="stats"><span id="node-count">0</span> papers &middot; <span id="link-count">0</span> connections <button id="info-hint-btn" title="Keyboard shortcuts">&#x24D8;</button></div>
<div id="shortcuts-popup">
  <h4>Shortcuts &amp; Controls</h4>
  <table>
    <tr><td>scroll</td><td>zoom in/out</td></tr>
    <tr><td>drag</td><td>pan</td></tr>
    <tr><td>click node</td><td>show detail</td></tr>
    <tr><td>Shift+click cat</td><td>expand sub-categories</td></tr>
    <tr><td>Esc</td><td>clear selection / ego</td></tr>
    <tr><td>/</td><td>focus search</td></tr>
    <tr><td>F</td><td>toggle Force / UMAP</td></tr>
    <tr><td>?</td><td>toggle this popup</td></tr>
  </table>
</div>
<div id="info"><button id="info-close" title="Close">&times;</button></div>
<div id="tooltip"></div>
<div class="link-tooltip" id="link-tooltip"></div>
<svg id="graph"></svg>
<canvas id="canvas3d"></canvas>
<script>
// Data
const nodesRaw = {nodes_json};
const linksRaw = {links_json};
const catColors = {cat_colors_json};
const catShapes = {cat_shapes_json};
const catCounts = {cat_counts_json};
const shapeMap = {{
  circle: d3.symbolCircle,
  square: d3.symbolSquare,
  triangle: d3.symbolTriangle,
  diamond: d3.symbolDiamond,
}};
const subColors = {sub_colors_json};
const subCounts = {sub_counts_json};
let colorBy = "cat"; // "cat" or "sub"
const catSubs = {cat_subs_json};
const relColors = {json.dumps(RELATION_COLORS)};
const relLabels = {{
  alternative:"\\uD83D\\uDD04 \\uB2E4\\uB978 \\uC811\\uADFC",
  extension:"\\uD83D\\uDD17 \\uD6C4\\uC18D \\uC5F0\\uAD6C",
  foundation:"\\uD83C\\uDFDB \\uAE30\\uBC18 \\uC5F0\\uAD6C",
  counterpoint:"\\u2696\\uFE0F \\uBC18\\uB860/\\uBE44\\uD310",
  application:"\\uD83E\\uDDEA \\uC751\\uC6A9"
}};

const activeCats = new Set(Object.keys(catColors));
const activeRels = new Set(Object.keys(relColors));
let egoId = null;
let yearMin = {year_min}, yearMax = {year_max};
let hlMode = null; // null, "hub", "bridge"
const hasUMAP = nodesRaw.some(n => n.ux !== null && n.uy !== null);
const has3D = {'true' if has3D else 'false'};
let useUMAP = hasUMAP;
let use3D = false;

// SVG setup — fixed coordinate system so layout is INDEPENDENT of browser size.
// The SVG element still fills the viewport (CSS: width:100vw; height:100vh),
// but viewBox + preserveAspectRatio make the content scale uniformly while
// keeping the same aspect ratio and identical force-simulation geometry.
const svg = d3.select("#graph");
const W = 1600, H = 1000;  // fixed logical canvas (16:10)
svg.attr("viewBox",[0,0,W,H]).attr("preserveAspectRatio","xMidYMid meet");
const defs = svg.append("defs");
const glowFilter = defs.append("filter").attr("id","glow").attr("x","-50%").attr("y","-50%").attr("width","200%").attr("height","200%");
glowFilter.append("feGaussianBlur").attr("in","SourceGraphic").attr("stdDeviation","5").attr("result","blur1");
glowFilter.append("feGaussianBlur").attr("in","SourceGraphic").attr("stdDeviation","2").attr("result","blur2");
const feMerge = glowFilter.append("feMerge");
feMerge.append("feMergeNode").attr("in","blur1");
feMerge.append("feMergeNode").attr("in","blur2");
feMerge.append("feMergeNode").attr("in","SourceGraphic");
const g = svg.append("g");

// Scale UMAP coords to screen if available
if(hasUMAP){{
  const uxs=nodesRaw.filter(n=>n.ux!==null).map(n=>n.ux);
  const uys=nodesRaw.filter(n=>n.uy!==null).map(n=>n.uy);
  const uxMin=Math.min(...uxs),uxMax=Math.max(...uxs);
  const uyMin=Math.min(...uys),uyMax=Math.max(...uys);
  const pad=80;
  nodesRaw.forEach(n=>{{
    if(n.ux!==null){{
      n.umapX=pad+(n.ux-uxMin)/(uxMax-uxMin||1)*(W-2*pad);
      n.umapY=pad+(n.uy-uyMin)/(uyMax-uyMin||1)*(H-2*pad);
      n.x=n.umapX; n.y=n.umapY;
    }}
  }});
}}

// Scale 3D UMAP coords to [-50, +50] bounding box
if(has3D){{
  const x3s=nodesRaw.filter(n=>n.ux3!==null&&n.ux3!==undefined).map(n=>n.ux3);
  const y3s=nodesRaw.filter(n=>n.uy3!==null&&n.uy3!==undefined).map(n=>n.uy3);
  const z3s=nodesRaw.filter(n=>n.uz3!==null&&n.uz3!==undefined).map(n=>n.uz3);
  if(x3s.length){{
    const x3Min=Math.min(...x3s),x3Max=Math.max(...x3s);
    const y3Min=Math.min(...y3s),y3Max=Math.max(...y3s);
    const z3Min=Math.min(...z3s),z3Max=Math.max(...z3s);
    const scale=50;
    nodesRaw.forEach(n=>{{
      if(n.ux3!==null&&n.ux3!==undefined){{
        n.umap3X=(n.ux3-x3Min)/(x3Max-x3Min||1)*2*scale-scale;
        n.umap3Y=(n.uy3-y3Min)/(y3Max-y3Min||1)*2*scale-scale;
        n.umap3Z=(n.uz3-z3Min)/(z3Max-z3Min||1)*2*scale-scale;
      }}
    }});
  }}
}}

// Force simulation
const sim = d3.forceSimulation()
  .force("link",d3.forceLink().id(d=>d.id).distance(useUMAP?30:60).strength(useUMAP?0.05:0.4))
  .force("charge",d3.forceManyBody().strength(useUMAP?-15:-80))
  .force("x",d3.forceX(d=>useUMAP&&d.umapX?d.umapX:W/2).strength(useUMAP?0.3:0.05))
  .force("y",d3.forceY(d=>useUMAP&&d.umapY?d.umapY:H/2).strength(useUMAP?0.3:0.05))
  .force("collide",d3.forceCollide(d=>nr(d)+2))
  .alphaDecay(0.02);

// Pre-compute degree (connection count) per node
const degree = {{}};
linksRaw.forEach(l=>{{
  const s=l.source.id||l.source, t=l.target.id||l.target;
  degree[s]=(degree[s]||0)+1;
  degree[t]=(degree[t]||0)+1;
}});
let nodeSizeMul=1.0;
function nr(d){{ return Math.max(3,Math.min(16,2+Math.sqrt(degree[d.id]||0)*2))*nodeSizeMul; }}
document.getElementById("node-size-slider").addEventListener("input",function(){{
  nodeSizeMul=parseFloat(this.value);
  document.getElementById("node-size-label").textContent=nodeSizeMul.toFixed(1)+"x";
  nodeG.selectAll("path.node").attr("d",d=>d3.symbol().type(shapeMap[d.shape]||d3.symbolCircle).size(nr(d)*nr(d)*3)());
  if(scene3) build3DObjects();
}});

const linkG = g.append("g");
const nodeG = g.append("g");
const labelG = g.append("g").attr("id","node-labels");
const tooltip = document.getElementById("tooltip");
const linkTooltip = document.getElementById("link-tooltip");
const info = document.getElementById("info");

// Track current zoom level for label rendering
let currentZoom = 1;
const zoomBehavior = d3.zoom().scaleExtent([0.1,8]).on("zoom",e=>{{
  g.attr("transform",e.transform);
  currentZoom = e.transform.k;
  updateLabels();
}});
svg.call(zoomBehavior);

function isNodeActive(n){{
  if(!activeCats.has(n.category)) return false;
  if(!activeSubs.has(n.sub_category||"General")) return false;
  if(n.year&&n.year.match(/^\\d{{4}}$/)&&(parseInt(n.year)<yearMin||parseInt(n.year)>yearMax)) return false;
  return true;
}}
function getVisible(){{
  // Mark all nodes active/inactive instead of filtering
  nodesRaw.forEach(n=>{{ n._active = isNodeActive(n); }});
  const activeIds = new Set(nodesRaw.filter(n=>n._active).map(n=>n.id));
  let ls = linksRaw.filter(l=>activeRels.has(l.relation)&&activeIds.has(l.source.id||l.source)&&activeIds.has(l.target.id||l.target));
  if(egoId){{
    const neighbors = new Set([egoId]);
    ls.forEach(l=>{{
      const s=l.source.id||l.source, t=l.target.id||l.target;
      if(s===egoId) neighbors.add(t);
      if(t===egoId) neighbors.add(s);
    }});
    nodesRaw.forEach(n=>{{ if(n._active && !neighbors.has(n.id)) n._active=false; }});
    const nids2 = new Set(nodesRaw.filter(n=>n._active).map(n=>n.id));
    ls = ls.filter(l=>nids2.has(l.source.id||l.source)&&nids2.has(l.target.id||l.target));
  }}
  return [nodesRaw, ls];
}}
const ghostOp = ()=> parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--ghost-opacity'))||0.08;

function render(){{
  const [ns,ls] = getVisible();
  const activeCount = ns.filter(n=>n._active).length;
  document.getElementById("node-count").textContent=activeCount;
  document.getElementById("link-count").textContent=ls.length;

  const lk = linkG.selectAll("line").data(ls,d=>(d.source.id||d.source)+"-"+(d.target.id||d.target)+"-"+d.relation);
  lk.exit().remove();
  const lkE = lk.enter().append("line")
    .attr("stroke",d=>d.color).attr("stroke-opacity",0.3).attr("stroke-width",1)
    .on("mouseover",(e,d)=>{{
      d3.select(e.currentTarget).attr("stroke-width",2.5).attr("stroke-opacity",0.85);
      const s=d.source.id||d.source, t=d.target.id||d.target;
      nodeG.selectAll("path.node").filter(n=>n.id===s||n.id===t).attr("filter","url(#glow)");
      linkTooltip.style.display="block";
      linkTooltip.style.left=(e.clientX+10)+"px";
      linkTooltip.style.top=(e.clientY-8)+"px";
      linkTooltip.textContent=(relLabels[d.relation]||d.relation)+(d.reason?" \u2014 "+d.reason.slice(0,80):"");
    }})
    .on("mouseout",(e,d)=>{{
      d3.select(e.currentTarget).attr("stroke-width",1).attr("stroke-opacity",0.3);
      nodeG.selectAll("path.node").attr("filter",null);
      linkTooltip.style.display="none";
    }});
  const lkAll = lkE.merge(lk);

  const nd = nodeG.selectAll("path.node").data(ns,d=>d.id);
  nd.exit().remove();
  const ndE = nd.enter().append("path").attr("class","node")
    .attr("d",d=>d3.symbol().type(shapeMap[d.shape]||d3.symbolCircle).size(nr(d)*nr(d)*3)())
    .attr("fill",d=>d.color)
    .attr("stroke",d=>d.multi?"#666":getComputedStyle(document.documentElement).getPropertyValue('--node-stroke')).attr("stroke-width",d=>d.multi?1.5:0.5)
    .attr("cursor","pointer")
    .call(d3.drag()
      .on("start",(e,d)=>{{ if(useUMAP) return; if(!e.active)sim.alphaTarget(0.3).restart();d.fx=d.x;d.fy=d.y;}})
      .on("drag",(e,d)=>{{ if(useUMAP) return; d.fx=e.x;d.fy=e.y;}})
      .on("end",(e,d)=>{{ if(useUMAP) return; if(!e.active)sim.alphaTarget(0);d.fx=null;d.fy=null;}}))
    .on("mouseover",(e,d)=>{{
      if(!d._active) return;
      d3.select(e.currentTarget).attr("filter","url(#glow)").raise();
      tooltip.style.display="block";
      tooltip.style.left=(e.clientX+12)+"px";
      tooltip.style.top=(e.clientY-10)+"px";
      const cats = d.all_categories ? d.all_categories.join(" \\u00B7 ") : d.category;
      const essenceSnip = d.essence?(d.essence.slice(0,100)+(d.essence.length>100?"...":"")):"";
      tooltip.innerHTML = '<div class="tt-title"><span class="tt-score" style="background:'+d.color+'"></span>['+d.num+'] '+d.title+'</div>'
        +'<div style="font-size:0.72rem;color:var(--text-muted);margin-bottom:0.15rem">'+cats+' \\u00B7 '+d.year+' \\u00B7 score:'+d.score+'</div>'
        +(essenceSnip?'<div class="tt-essence">'+essenceSnip+'</div>':'');
    }})
    .on("mouseout",(e,d)=>{{d3.select(e.currentTarget).attr("filter",null);tooltip.style.display="none";}})
    .on("click",(e,d)=>{{if(!d._active) return; e.stopPropagation();showInfo(d);}});
  const ndAll = ndE.merge(nd);

  // Base styling: active vs ghost
  const go = ghostOp();
  ndAll.attr("fill",d=>{{
      const c = colorBy==="sub"?(subColors[d.sub_category]||"#999"):d.color;
      return d._active ? c : c;
    }})
    .attr("opacity",d=>d._active?1:go)
    .attr("d",d=>d3.symbol().type(shapeMap[d.shape]||d3.symbolCircle).size(nr(d)*nr(d)*3)())
    .attr("pointer-events",d=>d._active?"all":"none");

  // Highlight modes (only affect active nodes)
  if(egoId){{
    ndAll.filter(d=>d._active).attr("opacity",d=>d.id===egoId?1:0.8);
  }} else if(hlMode==="hub"){{
    const activeNs = ns.filter(n=>n._active);
    const sorted = [...activeNs].sort((a,b)=>(degree[b.id]||0)-(degree[a.id]||0));
    const top10 = new Set(sorted.slice(0,10).map(n=>n.id));
    ndAll.filter(d=>d._active).attr("opacity",d=>top10.has(d.id)?1:go*1.5)
      .attr("d",d=>d3.symbol().type(shapeMap[d.shape]||d3.symbolCircle).size((top10.has(d.id)?nr(d)*2:nr(d))**2*3)());
    lkAll.attr("stroke-opacity",d=>{{
      const s=d.source.id||d.source,t=d.target.id||d.target;
      return top10.has(s)||top10.has(t)?0.5:0.04;
    }});
  }} else if(hlMode==="bridge"){{
    const bridgeIds = new Set();
    ls.forEach(l=>{{
      const sn=ns.find(n=>n.id===(l.source.id||l.source));
      const tn=ns.find(n=>n.id===(l.target.id||l.target));
      if(sn&&tn&&sn._active&&tn._active&&sn.category!==tn.category){{ bridgeIds.add(sn.id); bridgeIds.add(tn.id); }}
    }});
    ndAll.filter(d=>d._active).attr("opacity",d=>bridgeIds.has(d.id)?1:go*1.5)
      .attr("d",d=>d3.symbol().type(shapeMap[d.shape]||d3.symbolCircle).size((bridgeIds.has(d.id)?nr(d)*1.5:nr(d))**2*3)());
    lkAll.attr("stroke-opacity",d=>{{
      const s=d.source.id||d.source,t=d.target.id||d.target;
      return bridgeIds.has(s)&&bridgeIds.has(t)?0.6:0.04;
    }});
  }}

  // Position update helper
  function positionAll(){{
    lkAll.attr("x1",d=>d.source.x).attr("y1",d=>d.source.y).attr("x2",d=>d.target.x).attr("y2",d=>d.target.y);
    ndAll.attr("transform",d=>"translate("+(d.x||0)+","+(d.y||0)+")");
    updateLabels();
  }}

  const activeNs = ns.filter(n=>n._active);
  if(useUMAP){{
    // UMAP: no simulation — direct positioning
    sim.stop();
    // Ensure all nodes have UMAP coordinates set as x,y
    ns.forEach(n=>{{ if(n.umapX!=null) {{ n.x=n.umapX; n.y=n.umapY; }} }});
    // Resolve link references (D3 needs source/target as objects)
    const nodeMap = {{}};
    ns.forEach(n=>{{ nodeMap[n.id]=n; }});
    ls.forEach(l=>{{
      if(typeof l.source==="string") l.source=nodeMap[l.source]||l.source;
      if(typeof l.target==="string") l.target=nodeMap[l.target]||l.target;
    }});
    positionAll();
  }} else {{
    // Force mode: run simulation with only active nodes
    activeNs.forEach(n=>{{ n.fx=null; n.fy=null; }});
    sim.nodes(activeNs);
    sim.force("link").links(ls);
    sim.on("tick", positionAll);
    sim.alpha(0.3).restart();
  }}
}}

function updateLabels(){{
  // Labels disabled — tooltip and info panel are sufficient
  labelG.selectAll("text").remove();
  return;
  const activeNs = nodesRaw.filter(n=>n._active);
  const showNum = currentZoom > 2;
  const showTitle = currentZoom > 4;
  if(!showNum){{ labelG.selectAll("text").remove(); return; }}
  const lbls = labelG.selectAll("text.node-label").data(activeNs, d=>d.id);
  lbls.exit().remove();
  const lblsE = lbls.enter().append("text").attr("class","node-label");
  lblsE.merge(lbls)
    .attr("x",d=>(d.x||0)+nr(d)+2)
    .attr("y",d=>(d.y||0)+3)
    .text(d=>showTitle?(d.title?d.title.slice(0,25)+"…":"["+d.num+"]"):"["+d.num+"]");
}}

function showInfo(d){{
  const conns = linksRaw.filter(l=>{{
    const s=l.source.id||l.source, t=l.target.id||l.target;
    return s===d.id||t===d.id;
  }});
  const infoCats = d.all_categories ? d.all_categories.join(" &middot; ") : d.category;
  let html = '<button id="info-close" title="Close" onclick="closeInfo()">&times;</button>';
  html += "<h3>["+esc(d.num)+"] "+esc(d.title)+"</h3>";
  html += '<div class="info-meta"><span style="color:'+d.color+'">\u25CF</span> '+esc(infoCats)+"<br>"+d.year+" &middot; score:"+d.score+" &middot; "+conns.length+" connections</div>";
  html += '<div class="info-essence">'+esc(d.essence)+"</div>";
  html += '<div class="info-actions">';
  html += '<a class="review-btn" href="../papers/'+d.id+'/index.html" target="_blank">\\u2192 Review</a> ';
  if(egoId===d.id) html += '<a onclick="clearEgo()">\\u26D4 Ego \\uD574\\uC81C</a>';
  else html += '<a onclick="setEgo(\\''+d.id+'\\')">\\uD83D\\uDD0D Ego Network</a>';
  html += "</div><hr style=\\"border:none;border-top:1px solid #333;margin:0.4rem 0\\">";
  conns.slice(0,20).forEach(l=>{{
    const s=l.source.id||l.source, t=l.target.id||l.target;
    const oid = s===d.id?t:s;
    const o = nodesRaw.find(n=>n.id===oid);
    const name = o?"["+o.num+"] "+o.title:oid;
    html += '<div class="conn-item"><span class="conn-rel" style="color:'+l.color+'">'+(relLabels[l.relation]||l.relation)+'</span><a class="conn-link" data-id="'+oid+'">'+esc(name)+'</a></div>';
  }});
  info.innerHTML = html;
  info.classList.add("open");
}}
window.closeInfo = function(){{ info.classList.remove("open"); }};

function esc(s){{ return String(s).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;"); }}
window.setEgo = function(id){{ egoId=id; render(); const d=nodesRaw.find(n=>n.id===id); if(d)showInfo(d); }};
window.clearEgo = function(){{ egoId=null; render(); closeInfo(); }};
svg.on("click",()=>{{ closeInfo(); if(egoId){{egoId=null;render();}} }});
info.addEventListener("click",function(e){{
  const link=e.target.closest(".conn-link");
  if(link){{
    e.stopPropagation();
    const id=link.dataset.id;
    const n=nodesRaw.find(x=>x.id===id);
    if(n) showInfo(n);
  }}
}});
info.addEventListener("mouseover",function(e){{
  const link=e.target.closest(".conn-link");
  if(link){{
    const id=link.dataset.id;
    nodeG.selectAll("path.node").filter(d=>d.id===id).attr("filter","url(#glow)");
  }}
}});
info.addEventListener("mouseout",function(e){{
  const link=e.target.closest(".conn-link");
  if(link) nodeG.selectAll("path.node").attr("filter",null);
}});

// (Category filters handled by buildTree above)

// Relation filters
const rf = document.getElementById("rel-filters");
Object.keys(relColors).forEach(rel=>{{
  const el = document.createElement("span");
  el.className="rel-toggle";
  el.style.borderColor=relColors[rel]; el.style.color=relColors[rel];
  el.textContent=relLabels[rel]||rel;
  el.onclick=()=>{{
    if(activeRels.has(rel)){{activeRels.delete(rel);el.classList.add("off");}}
    else{{activeRels.add(rel);el.classList.remove("off");}}
    render();
  }};
  rf.appendChild(el);
}});

// Search
document.getElementById("search").addEventListener("input",function(){{
  const q=this.value.toLowerCase().trim();
  const sc=document.getElementById("search-count");
  const go=ghostOp();
  if(!q){{ nodeG.selectAll("path.node").attr("opacity",d=>d._active?1:go).attr("d",d=>d3.symbol().type(shapeMap[d.shape]||d3.symbolCircle).size(nr(d)*nr(d)*3)()); linkG.selectAll("line").attr("stroke-opacity",0.3); sc.textContent=""; return; }}
  let c=0;
  nodeG.selectAll("path.node").attr("opacity",d=>{{
    if(!d._active) return go;
    const m=d.title.toLowerCase().includes(q)||d.essence.toLowerCase().includes(q)||d.num.includes(q);
    if(m)c++; return m?1:go;
  }}).attr("d",d=>{{
    const m=d._active&&(d.title.toLowerCase().includes(q)||d.essence.toLowerCase().includes(q)||d.num.includes(q));
    const sz=m?nr(d)*1.5:nr(d);
    return d3.symbol().type(shapeMap[d.shape]||d3.symbolCircle).size(sz*sz*3)();
  }});
  linkG.selectAll("line").attr("stroke-opacity",0.04);
  sc.textContent=c+" results";
}});

// Hierarchical tree view + color toggle
const activeSubs = new Set(); // active sub-categories
function buildTree(){{
  const tree=document.getElementById("cat-tree");
  tree.innerHTML="";
  activeCats.clear(); activeSubs.clear();
  Object.keys(catColors).forEach(cat=>activeCats.add(cat));
  Object.keys(subColors).forEach(sub=>activeSubs.add(sub));

  Object.keys(catColors).forEach(cat=>{{
    const item=document.createElement("div");
    item.className="cat-tree-item";

    const header=document.createElement("div");
    header.className="cat-tree-header";
    const arrow=document.createElement("span");
    arrow.className="cat-tree-arrow"; arrow.textContent="\\u25B6";
    const dot=document.createElement("span");
    dot.className="cat-dot"; dot.style.background=catColors[cat];
    const txt=document.createTextNode(cat);
    const cnt=document.createElement("span");
    cnt.className="cat-count"; cnt.textContent=catCounts[cat]||0;
    header.appendChild(arrow); header.appendChild(dot); header.appendChild(txt); header.appendChild(cnt);

    const subsDiv=document.createElement("div");
    subsDiv.className="cat-tree-subs";

    const subs=catSubs[cat]||[];
    subs.forEach(sub=>{{
      activeSubs.add(sub);
      const sel=document.createElement("div");
      sel.className="sub-toggle-item";
      const sdot=document.createElement("span");
      sdot.className="cat-dot"; sdot.style.background=subColors[sub]||"#999";
      const stxt=document.createTextNode(sub);
      const scnt=document.createElement("span");
      scnt.className="cat-count"; scnt.textContent=subCounts[sub]||0;
      sel.appendChild(sdot); sel.appendChild(stxt); sel.appendChild(scnt);
      sel.onclick=(e)=>{{
        e.stopPropagation();
        if(activeSubs.has(sub)){{activeSubs.delete(sub);sel.classList.add("off");}}
        else{{activeSubs.add(sub);sel.classList.remove("off");}}
        render(); if(use3D) update3D();
      }};
      subsDiv.appendChild(sel);
    }});

    // Click header: toggle category on/off
    header.onclick=(e)=>{{
      if(e.shiftKey){{
        // Shift+click: expand/collapse subs
        subsDiv.classList.toggle("open");
        arrow.textContent=subsDiv.classList.contains("open")?"\\u25BC":"\\u25B6";
      }} else {{
        if(activeCats.has(cat)){{
          activeCats.delete(cat);
          header.classList.add("off");
          subs.forEach(s=>activeSubs.delete(s));
          subsDiv.querySelectorAll(".sub-toggle-item").forEach(s=>s.classList.add("off"));
        }} else {{
          activeCats.add(cat);
          header.classList.remove("off");
          subs.forEach(s=>activeSubs.add(s));
          subsDiv.querySelectorAll(".sub-toggle-item").forEach(s=>s.classList.remove("off"));
        }}
        render(); if(use3D) update3D();
      }}
    }};

    item.appendChild(header);
    item.appendChild(subsDiv);
    tree.appendChild(item);
  }});
}}
buildTree();

document.getElementById("sel-all").onclick=function(){{
  Object.keys(catColors).forEach(c=>activeCats.add(c));
  Object.keys(subColors).forEach(s=>activeSubs.add(s));
  document.querySelectorAll(".cat-tree-header").forEach(h=>h.classList.remove("off"));
  document.querySelectorAll(".sub-toggle-item").forEach(s=>s.classList.remove("off"));
  render(); if(use3D) update3D();
}};
document.getElementById("sel-none").onclick=function(){{
  activeCats.clear(); activeSubs.clear();
  document.querySelectorAll(".cat-tree-header").forEach(h=>h.classList.add("off"));
  document.querySelectorAll(".sub-toggle-item").forEach(s=>s.classList.add("off"));
  render(); if(use3D) update3D();
}};

document.getElementById("colorby-cat").onclick=function(){{
  colorBy="cat";
  this.classList.add("active");
  document.getElementById("colorby-sub").classList.remove("active");
  render();
}};
document.getElementById("colorby-sub").onclick=function(){{
  colorBy="sub";
  this.classList.add("active");
  document.getElementById("colorby-cat").classList.remove("active");
  render();
}};

// Layout toggle
function setLayoutBtnsActive(id){{
  ["layout-umap","layout-force"].forEach(bid=>{{
    const el=document.getElementById(bid);
    if(el) el.classList.toggle("active",bid===id);
  }});
  const btn3d=document.getElementById("layout-3d");
  if(btn3d) btn3d.classList.toggle("active",id==="layout-3d");
}}

if(hasUMAP){{
  document.getElementById("layout-umap").onclick=function(){{
    hide3D();
    useUMAP=true;
    setLayoutBtnsActive("layout-umap");
    sim.force("link").distance(30).strength(0.05);
    sim.force("charge").strength(-15);
    sim.force("x",d3.forceX(d=>d.umapX||W/2).strength(0.3));
    sim.force("y",d3.forceY(d=>d.umapY||H/2).strength(0.3));
    sim.alpha(1).restart();
    render();
  }};
  document.getElementById("layout-force").onclick=function(){{
    hide3D();
    useUMAP=false;
    setLayoutBtnsActive("layout-force");
    nodesRaw.forEach(n=>{{ n.fx=null; n.fy=null; }});
    sim.force("link").distance(60).strength(0.4);
    sim.force("charge").strength(-80);
    sim.force("x",d3.forceX(W/2).strength(0.05));
    sim.force("y",d3.forceY(H/2).strength(0.05));
    sim.alpha(1).restart();
    render();
  }};
}} else {{
  document.getElementById("layout-umap").style.display="none";
  document.getElementById("layout-force").classList.add("active");
}}
if(has3D){{
  document.getElementById("layout-3d").onclick=function(){{
    setLayoutBtnsActive("layout-3d");
    show3D();
  }};
}}

// Year slider
const ymSlider=document.getElementById("year-min"), yxSlider=document.getElementById("year-max"), yLabel=document.getElementById("year-label");
function updateYear(){{ yearMin=parseInt(ymSlider.value); yearMax=parseInt(yxSlider.value); if(yearMin>yearMax){{const t=yearMin;yearMin=yearMax;yearMax=t;}} yLabel.textContent=yearMin+" \\u2014 "+yearMax; render(); }}
ymSlider.addEventListener("input",updateYear);
yxSlider.addEventListener("input",updateYear);

// Highlight buttons
document.getElementById("hl-hub").onclick=function(){{
  hlMode=hlMode==="hub"?null:"hub";
  document.querySelectorAll(".hl-btn").forEach(b=>b.classList.remove("active"));
  if(hlMode) this.classList.add("active");
  render();
}};
document.getElementById("hl-bridge").onclick=function(){{
  hlMode=hlMode==="bridge"?null:"bridge";
  document.querySelectorAll(".hl-btn").forEach(b=>b.classList.remove("active"));
  if(hlMode) this.classList.add("active");
  render();
}};
document.getElementById("hl-reset").onclick=function(){{
  hlMode=null; egoId=null;
  document.querySelectorAll(".hl-btn").forEach(b=>b.classList.remove("active"));
  info.classList.remove("open");
  render();
}};

// Reset View: restore zoom/pan to the initial (identity) transform so the
// graph snaps back to the canonical layout regardless of how the user has
// zoomed, dragged or scrolled around.
document.getElementById("view-reset").onclick=function(){{
  svg.transition().duration(500).call(zoomBehavior.transform, d3.zoomIdentity);
}};

// Force controls
document.getElementById("f-charge").addEventListener("input",function(){{
  sim.force("charge").strength(parseInt(this.value));
  sim.alpha(0.3).restart();
}});
document.getElementById("f-dist").addEventListener("input",function(){{
  sim.force("link").distance(parseInt(this.value));
  sim.alpha(0.3).restart();
}});
document.getElementById("f-str").addEventListener("input",function(){{
  sim.force("link").strength(parseInt(this.value)/100);
  sim.alpha(0.3).restart();
}});
document.getElementById("f-grav").addEventListener("input",function(){{
  const v=parseInt(this.value)/100;
  sim.force("x").strength(v);
  sim.force("y").strength(v);
  sim.alpha(0.3).restart();
}});

// Theme toggle
document.getElementById("theme-dark").onclick=function(){{
  document.body.classList.remove("light");
  this.classList.add("active");
  document.getElementById("theme-light").classList.remove("active");
  nodeG.selectAll("path.node").attr("stroke",d=>d.multi?"#666":getComputedStyle(document.documentElement).getPropertyValue('--node-stroke'));
  if(scene3) scene3.background=new THREE.Color(getBgColor());
  render();
}};
document.getElementById("theme-light").onclick=function(){{
  document.body.classList.add("light");
  this.classList.add("active");
  document.getElementById("theme-dark").classList.remove("active");
  nodeG.selectAll("path.node").attr("stroke",d=>d.multi?"#666":getComputedStyle(document.documentElement).getPropertyValue('--node-stroke'));
  if(scene3) scene3.background=new THREE.Color(getBgColor());
  render();
}};

// Controls collapse/expand
const ctrlPanel = document.getElementById("controls");
const ctrlToggle = document.getElementById("controls-toggle");
ctrlToggle.addEventListener("click",function(e){{
  e.stopPropagation();
  ctrlPanel.classList.toggle("collapsed");
  ctrlToggle.innerHTML = ctrlPanel.classList.contains("collapsed")?"&raquo;":"&laquo;";
}});

// Info-hint / shortcuts popup
const shortcutsPopup = document.getElementById("shortcuts-popup");
document.getElementById("info-hint-btn").addEventListener("click",function(e){{
  e.stopPropagation();
  shortcutsPopup.classList.toggle("open");
}});
document.addEventListener("click",function(){{ shortcutsPopup.classList.remove("open"); }});
shortcutsPopup.addEventListener("click",function(e){{ e.stopPropagation(); }});

// Keyboard shortcuts
document.addEventListener("keydown",function(e){{
  const tag = document.activeElement.tagName;
  if(tag==="INPUT"||tag==="TEXTAREA") {{
    if(e.key==="Escape") document.activeElement.blur();
    return;
  }}
  if(e.key==="Escape") {{
    closeInfo();
    if(egoId){{ egoId=null; render(); }}
    shortcutsPopup.classList.remove("open");
  }} else if(e.key==="/") {{
    e.preventDefault();
    document.getElementById("search").focus();
  }} else if(e.key==="f"||e.key==="F") {{
    if(hasUMAP) {{
      useUMAP=!useUMAP;
      if(useUMAP) {{
        document.getElementById("layout-umap").classList.add("active");
        document.getElementById("layout-force").classList.remove("active");
        sim.force("link").distance(30).strength(0.05);
        sim.force("charge").strength(-15);
        sim.force("x",d3.forceX(d=>d.umapX||W/2).strength(0.3));
        sim.force("y",d3.forceY(d=>d.umapY||H/2).strength(0.3));
        render();
        return;
      }} else {{
        document.getElementById("layout-force").classList.add("active");
        document.getElementById("layout-umap").classList.remove("active");
        nodesRaw.forEach(n=>{{ n.fx=null; n.fy=null; }});
        sim.force("link").distance(60).strength(0.4);
        sim.force("charge").strength(-80);
        sim.force("x",d3.forceX(W/2).strength(0.05));
        sim.force("y",d3.forceY(H/2).strength(0.05));
      }}
      sim.alpha(1).restart();
    }}
  }} else if(e.key==="?") {{
    shortcutsPopup.classList.toggle("open");
  }}
}});

// ── Three.js 3D renderer ──────────────────────────────────────────────────
let scene3=null,camera3=null,renderer3=null,controls3=null;
let spheres3=[],lines3=[],raycaster3=null,mouse3=new THREE.Vector2();
let hovered3=null,animFrameId=null;

function getBgColor(){{
  return document.body.classList.contains("light")?"#f5f5f8":"#0a0a1a";
}}

function init3D(){{
  if(scene3) return; // already initialized
  const canvas=document.getElementById("canvas3d");
  scene3=new THREE.Scene();
  scene3.background=new THREE.Color(getBgColor());

  camera3=new THREE.PerspectiveCamera(60,window.innerWidth/window.innerHeight,0.1,2000);
  camera3.position.set(0,0,160);

  renderer3=new THREE.WebGLRenderer({{canvas,antialias:true}});
  renderer3.setSize(window.innerWidth,window.innerHeight);
  renderer3.setPixelRatio(Math.min(window.devicePixelRatio,2));

  controls3=new THREE.OrbitControls(camera3,renderer3.domElement);
  controls3.enableDamping=true;
  controls3.dampingFactor=0.08;

  // Ambient + directional light
  scene3.add(new THREE.AmbientLight(0xffffff,0.7));
  const dl=new THREE.DirectionalLight(0xffffff,0.8);
  dl.position.set(50,80,60);
  scene3.add(dl);

  raycaster3=new THREE.Raycaster();
  raycaster3.params.Points.threshold=1;

  canvas.addEventListener("mousemove",on3DMouseMove);
  canvas.addEventListener("click",on3DClick);
  window.addEventListener("resize",on3DResize);

  build3DObjects();
  animate3D();
}}

function nodeColor3(n){{
  return colorBy==="sub"?(subColors[n.sub_category]||"#999"):n.color;
}}

function build3DObjects(){{
  // Remove old objects
  spheres3.forEach(s=>scene3.remove(s));
  lines3.forEach(l=>scene3.remove(l));
  spheres3=[]; lines3=[];

  const go=ghostOp();
  const nodeMap={{}};

  nodesRaw.forEach(n=>{{
    if(n.umap3X===undefined) return;
    const r=Math.max(1.2,Math.min(5,0.8+Math.sqrt(degree[n.id]||0)*0.8))*nodeSizeMul;
    const geo=new THREE.SphereGeometry(r,12,8);
    const col=nodeColor3(n);
    const active=isNodeActive(n);
    const mat=new THREE.MeshPhongMaterial({{
      color:col,
      transparent:true,
      opacity:active?1:go,
    }});
    const mesh=new THREE.Mesh(geo,mat);
    mesh.position.set(n.umap3X,n.umap3Y,n.umap3Z);
    mesh.userData={{node:n}};
    scene3.add(mesh);
    spheres3.push(mesh);
    nodeMap[n.id]=mesh;
  }});

  // Links
  const [,ls]=getVisible();
  ls.forEach(l=>{{
    const s=l.source.id||l.source, t=l.target.id||l.target;
    const sm=nodeMap[s], tm=nodeMap[t];
    if(!sm||!tm) return;
    const pts=[sm.position.clone(),tm.position.clone()];
    const geo=new THREE.BufferGeometry().setFromPoints(pts);
    const mat=new THREE.LineBasicMaterial({{color:l.color,transparent:true,opacity:0.25}});
    const line=new THREE.Line(geo,mat);
    scene3.add(line);
    lines3.push(line);
  }});
}}

function update3D(){{
  if(!scene3) return;
  const go=ghostOp();
  spheres3.forEach(mesh=>{{
    const n=mesh.userData.node;
    const active=isNodeActive(n);
    mesh.material.opacity=active?1:go;
    mesh.material.color.set(nodeColor3(n));
    mesh.visible=true;
  }});
}}

function animate3D(){{
  if(!use3D){{ animFrameId=null; return; }}
  animFrameId=requestAnimationFrame(animate3D);
  controls3.update();
  renderer3.render(scene3,camera3);
}}

function on3DMouseMove(e){{
  if(!scene3) return;
  const rect=renderer3.domElement.getBoundingClientRect();
  mouse3.x=((e.clientX-rect.left)/rect.width)*2-1;
  mouse3.y=-((e.clientY-rect.top)/rect.height)*2+1;
  raycaster3.setFromCamera(mouse3,camera3);
  const hits=raycaster3.intersectObjects(spheres3);
  if(hits.length){{
    const n=hits[0].object.userData.node;
    if(hovered3!==n){{
      hovered3=n;
      tooltip.style.display="block";
      const cats=n.all_categories?n.all_categories.join(" \\u00B7 "):n.category;
      const ess=n.essence?(n.essence.slice(0,100)+(n.essence.length>100?"...":"")):"";
      tooltip.innerHTML='<div class="tt-title"><span class="tt-score" style="background:'+n.color+'"></span>['+n.num+'] '+n.title+'</div>'
        +'<div style="font-size:0.72rem;color:var(--text-muted);margin-bottom:0.15rem">'+cats+' \\u00B7 '+n.year+' \\u00B7 score:'+n.score+'</div>'
        +(ess?'<div class="tt-essence">'+ess+'</div>':'');
    }}
    tooltip.style.left=(e.clientX+12)+"px";
    tooltip.style.top=(e.clientY-10)+"px";
  }} else {{
    hovered3=null;
    tooltip.style.display="none";
  }}
}}

function on3DClick(e){{
  if(!scene3) return;
  const rect=renderer3.domElement.getBoundingClientRect();
  mouse3.x=((e.clientX-rect.left)/rect.width)*2-1;
  mouse3.y=-((e.clientY-rect.top)/rect.height)*2+1;
  raycaster3.setFromCamera(mouse3,camera3);
  const hits=raycaster3.intersectObjects(spheres3);
  if(hits.length){{
    showInfo(hits[0].object.userData.node);
  }}
}}

function on3DResize(){{
  if(!camera3||!renderer3) return;
  camera3.aspect=window.innerWidth/window.innerHeight;
  camera3.updateProjectionMatrix();
  renderer3.setSize(window.innerWidth,window.innerHeight);
}}

function show3D(){{
  use3D=true;
  document.getElementById("graph").style.display="none";
  document.getElementById("canvas3d").style.display="block";
  init3D();
  scene3.background=new THREE.Color(getBgColor());
  build3DObjects();
  if(!animFrameId) animate3D();
}}

function hide3D(){{
  use3D=false;
  document.getElementById("canvas3d").style.display="none";
  document.getElementById("graph").style.display="block";
}}
// ── End Three.js 3D renderer ──────────────────────────────────────────────

render();
</script>
</body>
</html>"""


def main():
    parser = argparse.ArgumentParser(description="Generate d3.js paper network")
    parser.add_argument("--topic", default="ai4s")
    args = parser.parse_args()

    topic = args.topic
    topic_dir = str(get_topic_dir(topic))

    log(f"Building network for {topic}...")
    nodes, links, cat_colors, cat_shapes, sub_colors, years, has3D = build_network_data(topic)
    log(f"  {len(nodes)} nodes, {len(links)} links, has3D={has3D}")

    html = generate_html(nodes, links, cat_colors, cat_shapes, sub_colors, years, topic, has3D=has3D)

    out_path = os.path.join(topic_dir, "network.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    log(f"  Written: {out_path} ({len(html):,} chars)")
    log("Done!")


if __name__ == "__main__":
    main()
