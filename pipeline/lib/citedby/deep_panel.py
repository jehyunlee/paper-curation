"""citedby 리포트에 얹는 Deep Research 패널.

`pdf_corpus.build_index` 가 만든 `_citedby_index.json`(+ int8 사이드카)을 읽어
**보유 PDF 전문**을 근거로 질문에 답한다. 코퍼스 Deep Research 와 같은 구조지만
훨씬 작다 — Deeper 다단계, figure 인라인, 리포트 export 는 뺐다. 근거가
review.md 가 아니라 **원문 PDF** 라는 점이 다르다.

동작 조건 — 반드시 **로컬 서버로 열어야 한다**:
    python pipeline/serve_local.py
    http://localhost:8000/papers/{slug}/citedby/report_*.html

`file://` 로 열면 (1) 인덱스 fetch 가 CORS 로 막히고 (2) 쿼리 임베딩에 필요한
`/api/embed` 가 없다. 그래서 패널이 스스로 감지해 안내를 띄운다. 리포트 자체는
서버 없이도 정상적으로 읽히므로, 이 패널만 비활성이 된다.

검색은 BM25(희소) + 코사인(밀집) 을 RRF 로 융합한다. 임베딩이 없으면
BM25 단독으로 자동 강등된다 — 키가 없어도 검색은 된다.
"""
from __future__ import annotations

import json

# 답변 생성 모델 — 리포트 독자가 BYOK 로 넣는다. citedby 본체의 3-provider
# cascade 와 같은 등급을 쓴다.
_MODELS = {
    "anthropic": "claude-sonnet-5",
    "openai": "gpt-4.1",
    "google": "gemini-3.1-flash",
}

_CSS = """
.dr{border:1px solid var(--line);border-radius:10px;padding:14px 16px;margin:18px 0 24px;background:#fbfcfd}
.dr h2{margin:0 0 4px;font-size:16px}
.dr .dr-sub{color:var(--soft);font-size:12.5px;margin-bottom:10px}
.dr-row{display:flex;gap:8px;align-items:center;flex-wrap:wrap}
.dr-q{flex:1;min-width:260px;font:inherit;font-size:14px;padding:8px 10px;
 border:1px solid var(--line);border-radius:7px}
.dr-key{font:inherit;font-size:12.5px;padding:7px 9px;border:1px solid var(--line);
 border-radius:7px;width:230px}
.dr-go{font:inherit;font-size:13px;font-weight:600;padding:8px 16px;border:0;
 border-radius:7px;background:var(--accent);color:#fff;cursor:pointer}
.dr-go[disabled]{opacity:.45;cursor:not-allowed}
.dr-status{font-size:12.5px;color:var(--soft);margin-top:8px;min-height:1.2em}
.dr-status.err{color:#c0392b}
.dr-ans{margin-top:12px;font-size:14.5px;line-height:1.75;white-space:pre-wrap}
.dr-refs{margin-top:12px;border-top:1px solid var(--line);padding-top:10px}
.dr-refs h4{margin:0 0 6px;font-size:13px;color:var(--soft)}
.dr-ref{font-size:12.5px;margin:3px 0;color:var(--soft)}
.dr-ref b{color:var(--ink)}
.dr-cite{display:inline-block;min-width:1.4em;text-align:center;font-size:11px;
 font-weight:700;background:#eef1f5;border-radius:4px;padding:0 4px;margin:0 1px}
.dr-off{font-size:13px;color:var(--soft);background:#fff7e6;border:1px solid #f0d9a8;
 border-radius:7px;padding:10px 12px;margin-top:8px;line-height:1.6}
.dr-off code{background:#fff;padding:1px 5px;border-radius:4px;font-size:12px}
"""

# 패널 JS. 인덱스는 리포트와 같은 디렉토리에 있다고 가정한다.
_JS = r"""
(function(){
  var IDX=null, EMB=null, READY=false;
  var $=function(id){return document.getElementById(id);};
  function status(msg,err){var el=$('drStatus'); if(!el)return;
    el.textContent=msg||''; el.className='dr-status'+(err?' err':'');}

  function offline(reason){
    var el=$('drOffline'); if(el){el.style.display='';
      var r=$('drOfflineWhy'); if(r) r.textContent=reason||'';}
    var row=$('drRow'); if(row) row.style.display='none';
  }

  // ── 인덱스 로드 ─────────────────────────────────────────────────────
  async function load(){
    if(location.protocol==='file:'){
      offline('file:// 로 열면 인덱스를 읽을 수 없습니다.'); return;
    }
    try{
      var r=await fetch(IDX_FILE);
      if(!r.ok) throw new Error('HTTP '+r.status);
      IDX=await r.json();
    }catch(e){ offline('인덱스를 찾지 못했습니다 ('+e.message+')'); return; }

    if(IDX.emb_file){
      try{
        var b=await fetch(IDX.emb_file);
        if(b.ok){ EMB=new Int8Array(await b.arrayBuffer()); }
      }catch(e){ /* 벡터 없으면 BM25 단독 */ }
    }
    buildBM25();
    READY=true;
    var n=Object.keys(IDX.papers||{}).length;
    status('준비됨 — 논문 '+n+'편 · 청크 '+IDX.count+'개'
           +(EMB?' · 하이브리드 검색':' · BM25 검색(임베딩 없음)'));
    var go=$('drGo'); if(go) go.disabled=false;
  }

  // ── BM25 (희소) ─────────────────────────────────────────────────────
  var DF={}, DOCS=[], AVG=0;
  function tok(s){
    return (s||'').toLowerCase().match(/[a-z0-9]+|[\uac00-\ud7a3]{2,}/g)||[];
  }
  function buildBM25(){
    DOCS=(IDX.chunks||[]).map(function(c){
      var t=tok(c.text), tf={};
      t.forEach(function(w){tf[w]=(tf[w]||0)+1;});
      Object.keys(tf).forEach(function(w){DF[w]=(DF[w]||0)+1;});
      return {tf:tf, len:t.length};
    });
    AVG=DOCS.reduce(function(a,d){return a+d.len;},0)/Math.max(1,DOCS.length);
  }
  function bm25(q){
    var N=DOCS.length, k1=1.5, b=0.75, qt=tok(q), out=[];
    for(var i=0;i<N;i++){
      var d=DOCS[i], s=0;
      for(var j=0;j<qt.length;j++){
        var f=d.tf[qt[j]]; if(!f) continue;
        var idf=Math.log(1+(N-DF[qt[j]]+0.5)/(DF[qt[j]]+0.5));
        s+=idf*(f*(k1+1))/(f+k1*(1-b+b*d.len/AVG));
      }
      if(s>0) out.push([i,s]);
    }
    return out.sort(function(a,c){return c[1]-a[1];}).slice(0,40);
  }

  // ── 밀집 검색 ───────────────────────────────────────────────────────
  async function embedQuery(q){
    var r=await fetch('/api/embed',{method:'POST',
      headers:{'Content-Type':'application/json'},body:JSON.stringify({text:q})});
    if(!r.ok) throw new Error('embed '+r.status);
    return (await r.json()).embedding;
  }
  function dense(vec){
    if(!EMB||!vec) return [];
    var dim=IDX.dim, n=IDX.count, out=[];
    // 인덱스 벡터는 L2 정규화 후 int8 이라 내적이 곧 코사인이다.
    var qn=0; for(var k=0;k<vec.length;k++) qn+=vec[k]*vec[k];
    qn=Math.sqrt(qn)||1;
    for(var i=0;i<n;i++){
      var off=i*dim, s=0;
      for(var d=0;d<dim;d++) s+=(EMB[off+d]/127)*(vec[d]/qn);
      out.push([i,s]);
    }
    return out.sort(function(a,c){return c[1]-a[1];}).slice(0,40);
  }
  function rrf(a,b){
    var R={}, K=60;
    a.forEach(function(x,i){R[x[0]]=(R[x[0]]||0)+1/(K+i+1);});
    b.forEach(function(x,i){R[x[0]]=(R[x[0]]||0)+1/(K+i+1);});
    return Object.keys(R).map(function(i){return [parseInt(i,10),R[i]];})
      .sort(function(x,y){return y[1]-x[1];}).slice(0,12);
  }

  // ── 답변 생성 (BYOK) ────────────────────────────────────────────────
  function provider(key){
    if(/^sk-ant-/.test(key)) return 'anthropic';
    if(/^sk-/.test(key)) return 'openai';
    if(/^AIza/.test(key)) return 'google';
    return '';
  }
  async function answer(q, refs, key){
    var ctx=refs.map(function(r,i){
      return '['+(i+1)+'] '+(r.title||'')+'\n'+r.text;
    }).join('\n\n');
    var prompt='다음은 어떤 논문을 인용한 논문들의 원문 발췌다.\n\n'+ctx+
      '\n\n질문: '+q+'\n\n규칙:\n- 위 발췌만 근거로 답한다. 없으면 없다고 말한다.\n'+
      '- 문장마다 근거를 [ref:N] 으로 표기한다.\n- 한국어로, 간결하게.';
    var p=provider(key);
    if(p==='anthropic'){
      var r=await fetch('https://api.anthropic.com/v1/messages',{method:'POST',
        headers:{'Content-Type':'application/json','x-api-key':key,
          'anthropic-version':'2023-06-01','anthropic-dangerous-direct-browser-access':'true'},
        body:JSON.stringify({model:MODELS.anthropic,max_tokens:1600,
          messages:[{role:'user',content:prompt}]})});
      if(!r.ok) throw new Error('Anthropic '+r.status);
      var j=await r.json();
      return (j.content||[]).map(function(c){return c.text||'';}).join('');
    }
    if(p==='openai'){
      var r2=await fetch('https://api.openai.com/v1/chat/completions',{method:'POST',
        headers:{'Content-Type':'application/json','Authorization':'Bearer '+key},
        body:JSON.stringify({model:MODELS.openai,max_completion_tokens:1600,
          messages:[{role:'user',content:prompt}]})});
      if(!r2.ok) throw new Error('OpenAI '+r2.status);
      var j2=await r2.json();
      return j2.choices[0].message.content||'';
    }
    if(p==='google'){
      var r3=await fetch('https://generativelanguage.googleapis.com/v1beta/models/'
        +MODELS.google+':generateContent?key='+encodeURIComponent(key),
        {method:'POST',headers:{'Content-Type':'application/json'},
         body:JSON.stringify({contents:[{parts:[{text:prompt}]}]})});
      if(!r3.ok) throw new Error('Gemini '+r3.status);
      var j3=await r3.json();
      return ((j3.candidates||[])[0]||{}).content?.parts?.[0]?.text||'';
    }
    throw new Error('키 형식을 알 수 없습니다 (sk-ant-/sk-/AIza)');
  }

  function renderRefs(refs){
    var el=$('drRefs'); if(!el) return;
    if(!refs.length){el.innerHTML=''; return;}
    el.innerHTML='<h4>근거</h4>'+refs.map(function(r,i){
      var link=r.attach?(' · <a href="zotero://open-pdf/library/items/'+r.attach
        +'">PDF 열기</a>'):'';
      return '<div class="dr-ref"><b>['+(i+1)+']</b> '+
        (r.title||'').replace(/</g,'&lt;')+link+'</div>';
    }).join('');
  }

  async function run(){
    var q=($('drQ')||{}).value||''; q=q.trim();
    if(!q||!READY) return;
    var key=(($('drKey')||{}).value||'').trim();
    $('drGo').disabled=true; $('drAns').textContent='';
    try{
      status('검색 중…');
      var sparse=bm25(q), dvec=null;
      if(EMB){
        try{ dvec=await embedQuery(q); }
        catch(e){ status('임베딩 실패 — BM25 단독으로 진행합니다'); }
      }
      var hits=rrf(sparse, dense(dvec));
      if(!hits.length){ status('관련 내용을 찾지 못했습니다', true);
        $('drGo').disabled=false; return; }

      var refs=hits.map(function(h){
        var c=IDX.chunks[h[0]], p=(IDX.papers||{})[c.slug]||{};
        return {text:c.text, title:p.title||c.slug, attach:p.zotero_attach||''};
      });
      renderRefs(refs);

      if(!key){ status('근거 '+refs.length+'건을 찾았습니다. 답변을 생성하려면 '+
        'API 키를 입력하세요 (브라우저에만 머뭅니다).'); $('drGo').disabled=false; return; }

      status('답변 생성 중…');
      var text=await answer(q, refs, key);
      $('drAns').innerHTML=text.replace(/</g,'&lt;')
        .replace(/\[ref:(\d+)\]/g,'<span class="dr-cite">$1</span>');
      status('완료 — 근거 '+refs.length+'건');
    }catch(e){ status(String(e.message||e), true); }
    $('drGo').disabled=false;
  }

  document.addEventListener('DOMContentLoaded', function(){
    var go=$('drGo'); if(go) go.addEventListener('click', run);
    var q=$('drQ'); if(q) q.addEventListener('keydown', function(e){
      if(e.key==='Enter') run(); });
    load();
  });
})();
"""


def panel_css() -> str:
    return _CSS


def panel_html(index_file: str, lbl: dict) -> str:
    """Deep Research 패널 마크업. `index_file` 은 리포트 기준 상대경로."""
    return (
        '<section class="dr no-print">'
        f'<h2>{lbl["dr_title"]}</h2>'
        f'<div class="dr-sub">{lbl["dr_sub"]}</div>'
        '<div class="dr-row" id="drRow">'
        f'<input id="drQ" class="dr-q" type="text" placeholder="{lbl["dr_ph"]}">'
        f'<input id="drKey" class="dr-key" type="password" '
        f'placeholder="{lbl["dr_key"]}">'
        f'<button id="drGo" class="dr-go" type="button" disabled>'
        f'{lbl["dr_go"]}</button>'
        "</div>"
        '<div class="dr-off" id="drOffline" style="display:none">'
        f'{lbl["dr_offline"]}'
        '<div id="drOfflineWhy" style="margin-top:6px;font-size:12px"></div>'
        "</div>"
        '<div class="dr-status" id="drStatus"></div>'
        '<div class="dr-ans" id="drAns"></div>'
        '<div class="dr-refs" id="drRefs"></div>'
        "</section>"
    )


def panel_script(index_file: str) -> str:
    return (
        "<script>\n"
        f"var IDX_FILE={json.dumps(index_file)};\n"
        f"var MODELS={json.dumps(_MODELS)};\n"
        f"{_JS}\n</script>"
    )
