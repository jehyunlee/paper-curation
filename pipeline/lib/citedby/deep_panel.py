"""citedby 리포트에 얹는 Deep Research 패널.

`pdf_corpus.build_index` 가 만든 `_citedby_index.json`(+ int8 사이드카)을 읽어
**보유 PDF 전문**을 근거로 질문에 답한다. 코퍼스 Deep Research 와 같은 구조지만
훨씬 작다. 기본 Deep 과 더 긴 Deeper, provider web search, streaming 답변,
figure 인라인, 개별 export 를 지원한다. 근거가 review.md 가 아니라 **원문 PDF**
라는 점이 다르다.

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
# 근거 수·출력 길이 — 답변이 "부실하다"는 보고의 직접 원인이 여기였다.
# 12청크 × 1,600토큰으로는 논문 여러 편을 비교할 여지가 없다.
TOPK = 28          # 최종 근거 청크 (2,200자 × 28 ≈ 6만 자 컨텍스트)
POOL = 120         # BM25/dense 각각의 후보 폭
PER_PAPER = 4      # 논문당 상한 — 한 편이 상위를 독식하지 못하게
MAX_OUT = 16000    # 기본 답변 토큰; Deeper 는 서버 상한 24,000 사용

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
.dr-opt{display:inline-flex;align-items:center;gap:4px;white-space:nowrap;
 font-size:12px;color:var(--soft);cursor:pointer;user-select:none}
.dr-opt input{margin:0;cursor:pointer}
.dr-deeper-note{font-size:11.5px;color:var(--accent);font-weight:600}
.dr-status{font-size:12.5px;color:var(--soft);margin-top:8px;min-height:1.2em}
.dr-status.err{color:#c0392b}
.dr-ans{margin-top:12px;font-size:14.5px;line-height:1.75;white-space:normal}
.dr-exp{display:flex;gap:6px;flex-wrap:wrap;margin-top:12px}
.dr-x{font:inherit;font-size:12.5px;padding:6px 12px;border:1px solid var(--line);
 border-radius:6px;background:#fff;cursor:pointer;color:var(--ink)}
.dr-x:hover{background:#f2f4f7}
.dr-ans h2{font-size:16px;margin:18px 0 6px}
.dr-ans h3{font-size:14px;margin:14px 0 4px}
.dr-ans ul,.dr-ans ol{margin:6px 0 10px;padding-left:22px}
.dr-ans li{margin:3px 0}
.dr-ans p{margin:8px 0}
.dr-ans code{background:#f2f4f7;padding:1px 5px;border-radius:4px;font-size:12.5px}
.dr-ans strong{font-weight:700}
.dr-refs{margin-top:12px;border-top:1px solid var(--line);padding-top:10px}
.dr-refs h4{margin:0 0 6px;font-size:13px;color:var(--soft)}
.dr-ref{font-size:12.5px;margin:3px 0;color:var(--soft)}
.dr-ref b{color:var(--ink)}
.dr-prev{color:#9aa0a8;font-size:11.5px;margin:2px 0 0 18px;line-height:1.5}
.dr-ref i{font-style:normal;color:#7a8089;font-size:11.5px}
.dr-cite{display:inline-block;min-width:1.4em;text-align:center;font-size:11px;
 font-weight:700;background:#eef1f5;border-radius:4px;padding:0 4px;margin:0 1px}
.dr-off{font-size:13px;color:var(--soft);background:#fff7e6;border:1px solid #f0d9a8;
 border-radius:7px;padding:10px 12px;margin-top:8px;line-height:1.6}
.dr-off code{background:#fff;padding:1px 5px;border-radius:4px;font-size:12px}
"""

# 패널 JS. 인덱스는 리포트와 같은 디렉토리에 있다고 가정한다.
_JS = r"""
(function(){
  var IDX=null, EMB=null, READY=false, LAST_MODEL='';
  var LAST={q:'',answer:'',refs:[],model:'',deeper:false,web:false};
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
    return out.sort(function(a,c){return c[1]-a[1];}).slice(0,POOL);
  }
  function rrf(a,b){
    var R={}, K=60;
    a.forEach(function(x,i){R[x[0]]=(R[x[0]]||0)+1/(K+i+1);});
    b.forEach(function(x,i){R[x[0]]=(R[x[0]]||0)+1/(K+i+1);});
    var ranked=Object.keys(R).map(function(i){return [parseInt(i,10),R[i]];})
      .sort(function(x,y){return y[1]-x[1];});
    // 한 논문이 상위를 독식하면 답변이 그 논문 요약이 된다. 논문당 상한을 두고
    // 폭을 확보한 뒤, 남는 자리를 점수순으로 채운다.
    var perPaper={}, picked=[], rest=[];
    for(var i=0;i<ranked.length && picked.length<TOPK;i++){
      var slug=IDX.chunks[ranked[i][0]].slug;
      perPaper[slug]=(perPaper[slug]||0)+1;
      if(perPaper[slug]<=PER_PAPER) picked.push(ranked[i]); else rest.push(ranked[i]);
    }
    for(var j=0;j<rest.length && picked.length<TOPK;j++) picked.push(rest[j]);
    return picked;
  }

  // ── 답변 생성 (서버 NDJSON streaming) ───────────────────────────────────
  async function answer(q, refs, deeper, web, onText){
    var ctx=refs.map(function(r,i){
      var head='['+(i+1)+'] '+(r.title||'');
      if(r.year) head+=' ('+r.year+')';
      if(r.section) head+=' — '+r.section;
      return head+'\n'+r.text;
    }).join('\n\n');
    var depth=deeper
      ? '- **Deeper Research**: 4~7개 분석 축으로 나눠 각 축을 충분히 전개하고, 논문 사이의 계보·대안·상충 결과·시간적 변화를 종합한다. 마지막에 전체 결론과 열린 질문을 별도 절로 완결한다.\n'
      : '';
    var prompt=
      '다음은 어떤 논문을 인용한 논문들의 **원문 발췌**다. 각 발췌는 논문 제목과 '+
      '섹션이 붙어 있다.\n\n'+ctx+'\n\n질문: '+q+'\n\n'+
      '## 작성 규칙\n'+
      '- 위 발췌를 주 근거로 삼는다. 발췌에 없는 내용은 지어내지 말고 "발췌 범위에서는 '+
      '확인되지 않는다"고 밝힌다.\n'+
      '- **구체적으로 쓴다.** 발췌에 있는 수치·데이터셋 이름·모델명·실험 조건·'+
      '정량 결과를 그대로 인용한다. "성능이 향상되었다" 같은 뭉뚱그린 표현 대신 '+
      '"F1 0.72 → 0.81" 처럼 적는다.\n'+
      '- **논문을 비교한다.** 같은 문제를 다룬 논문이 여럿이면 접근 차이와 결과 '+
      '차이를 나란히 놓는다. 상충하는 주장이 있으면 그 사실 자체를 짚는다.\n'+
      '- 근거를 문장 단위로 [ref:N] 표기한다. 한 문장에 근거가 여럿이면 '+
      '[ref:2][ref:5] 처럼 모두 적는다.\n'+depth+
      '- 구조: 먼저 **핵심 답변** 3~5문장, 다음 **논문별 근거**를 소제목으로 나눠 '+
      '상세히, 마지막에 **한계/미해결** 을 적는다.\n'+
      '- 답변은 반드시 완결된 문장과 결론으로 끝낸다.\n'+
      '- 분량은 아끼지 않는다. 선택한 모드의 모든 절과 결론을 충분히 완성한다.\n'+
      '- 한국어. 기술 용어는 English 그대로.';

    var r=await fetch('/api/citedby-answer',{method:'POST',
      headers:{'Content-Type':'application/json'},
      body:JSON.stringify({prompt:prompt,max_tokens:deeper?24000:MAX_OUT,
                           web_search:!!web,deeper:!!deeper})});
    if(!r.ok){
      var ej=await r.json().catch(function(){return {};});
      throw new Error(ej.error||('answer '+r.status));
    }
    if(!r.body) throw new Error('streaming response body가 없습니다');
    var reader=r.body.getReader(), dec=new TextDecoder(), buf='', text='', meta={};
    function consume(line){
      line=line.trim(); if(!line) return;
      var ev; try{ev=JSON.parse(line);}catch(e){return;}
      if(ev.event==='delta' && ev.text){
        text+=ev.text; onText(text);
      }else if(ev.event==='done'){
        meta=ev;
      }else if(ev.event==='error'){
        throw new Error(ev.message||'답변 stream 오류');
      }
    }
    while(true){
      var part=await reader.read();
      if(part.done) break;
      buf+=dec.decode(part.value,{stream:true});
      var pos;
      while((pos=buf.indexOf('\n'))>=0){
        var line=buf.slice(0,pos); buf=buf.slice(pos+1); consume(line);
      }
    }
    buf+=dec.decode();
    if(buf.trim()) consume(buf);
    if(!text.trim()) throw new Error('빈 답변을 받았습니다');
    LAST_MODEL=(meta.provider||'')+(meta.model?(' / '+meta.model):'');
    return text;
  }

  // ── 마크다운 렌더 ────────────────────────────────────────────────────
  // 코퍼스 Deep Research 와 같은 규약: marked.js 가 있으면 그걸 쓰고, 없으면
  // 최소 폴백. [ref:N] 은 렌더 후 클릭 가능한 배지로 바꾼다.
  function mdToMarkup(md){
    var h;
    if(window.marked){
      try{ h=window.marked.parse(md,{gfm:true,breaks:false}); }catch(e){}
    }
    if(h===undefined){
      h=String(md||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')
        .replace(/^#{4,6}\s+(.+)$/gm,'<h4>$1</h4>')
        .replace(/^### (.+)$/gm,'<h3>$1</h3>')
        .replace(/^## (.+)$/gm,'<h2>$1</h2>')
        .replace(/^# (.+)$/gm,'<h2>$1</h2>')
        .replace(/\*\*([^*]+)\*\*/g,'<strong>$1</strong>')
        .replace(/`([^`]+)`/g,'<code>$1</code>')
        .replace(/^\s*[-*+]\s+(.+)$/gm,'<li>$1</li>')
        .replace(/(<li>[\s\S]*?<\/li>)/g,'<ul>$1</ul>')
        .replace(/\n{2,}/g,'</p><p>');
      h='<p>'+h+'</p>';
    }
    return h.replace(/\[ref:(\d+)\]/g,'<span class="dr-cite">$1</span>');
  }

  // ── 내보내기 (코퍼스 Deep Research 와 동일 형식) ──────────────────────
  function citedNums(md){
    var s=new Set(), m, re=/\[ref:(\d+)\]/g;
    while((m=re.exec(md||''))) s.add(parseInt(m[1],10));
    return s;
  }
  function refUrl(r){
    if(r.doi) return 'https://doi.org/'+r.doi;
    if(r.arxiv) return 'https://arxiv.org/abs/'+r.arxiv;
    return r.url||'';
  }
  function buildFullMarkdown(){
    var lines=['# citedby Deep Research','','**Query**: '+LAST.q,
               '**Generated**: '+new Date().toISOString(),
               '**Model**: '+(LAST.model||'-'),'','---','',LAST.answer];
    var cited=citedNums(LAST.answer);
    if(cited.size>0){
      lines.push('','## References','');
      Array.from(cited).sort(function(a,b){return a-b;}).forEach(function(n){
        var r=LAST.refs[n-1]; if(!r) return;
        var href=refUrl(r);
        var au=r.authors?(String(r.authors).split(/[;,]/)[0].trim()+' et al. '):'';
        var yr=r.year?('('+r.year+'). '):'';
        var id=r.doi?(' DOI: https://doi.org/'+r.doi):(r.arxiv?(' arXiv:'+r.arxiv):'');
        lines.push('- ['+n+'] '+au+yr+(href?('['+r.title+']('+href+')'):r.title)+'.'+id);
      });
    }
    return lines.join('\n');
  }
  function safeName(s){
    return String(s||'질문').replace(/[\\/:*?"<>|\n\r\t]/g,' ')
      .replace(/\s+/g,' ').trim().slice(0,80)||'질문';
  }
  function dlBlob(name, text, mime){
    var b=new Blob([text],{type:mime||'text/markdown;charset=utf-8'});
    var a=document.createElement('a');
    a.href=URL.createObjectURL(b); a.download=name;
    document.body.appendChild(a); a.click();
    setTimeout(function(){document.body.removeChild(a);URL.revokeObjectURL(a.href);},100);
  }
  function exportMd(){
    if(!LAST.answer) return;
    var d=new Date().toISOString().slice(0,10);
    dlBlob('CITEDBY_'+d+'_'+safeName(LAST.q)+'.md', buildFullMarkdown());
  }
  // Obsidian 은 서버 라우트가 필요 없다 — obsidian://new URI 로 vault 에
  // 직접 만든다 (코퍼스 Deep Research 와 동일 방식).
  function exportObsidian(){
    if(!LAST.answer) return;
    var d=new Date().toISOString().slice(0,10);
    var file='notes/'+COLLECTION+'/help/CITEDBY_'+d+'_'+safeName(LAST.q);
    var body=['# '+LAST.q,'','> citedby Deep Research ('+new Date().toLocaleString()+
              (LAST.model?(' · '+LAST.model):'')+')','',
              '## My Notes','','(여기에 생각을 적으세요)','','---','',
              buildFullMarkdown()].join('\n');
    window.location.href='obsidian://new?vault=docs&file='+
      encodeURIComponent(file)+'&content='+encodeURIComponent(body);
    status('Obsidian 으로 보냈습니다 — '+file+'.md');
  }
  // PDF 는 전용 인쇄 창. 참고문헌의 DOI/URL 을 절대 링크로 심어, 파일을 받은
  // 사람이 그대로 클릭할 수 있게 한다.
  function exportPdf(){
    if(!LAST.answer) return;
    var cited=citedNums(LAST.answer);
    var refs=Array.from(cited).sort(function(a,b){return a-b;}).map(function(n){
      var r=LAST.refs[n-1]; if(!r) return '';
      var href=refUrl(r);
      var meta=[r.year||'', r.journal||''].filter(Boolean).join(' · ');
      return '<li><span class="n">['+n+']</span> '+
        (href?('<a href="'+href+'">'+esc(r.title)+'</a>'):esc(r.title))+
        (meta?(' <span class="m">'+esc(meta)+'</span>'):'')+
        (href?('<div class="u"><a href="'+href+'">'+esc(href)+'</a></div>'):'')+
        '</li>';
    }).join('');
    var css='body{font-family:-apple-system,BlinkMacSystemFont,"Apple SD Gothic Neo",'+
      '"Noto Sans KR",sans-serif;line-height:1.75;color:#1f2430;max-width:820px;'+
      'margin:0 auto;padding:28px 24px;word-break:keep-all}'+
      'h1{font-size:20px;margin:0 0 4px}h2{font-size:16px;margin:22px 0 8px;'+
      'border-bottom:1px solid #e2e5ec;padding-bottom:4px}h3{font-size:14px}'+
      '.meta{color:#5b6478;font-size:12px;margin-bottom:18px}'+
      '.dr-cite{display:inline-block;min-width:1.3em;text-align:center;font-size:10.5px;'+
      'font-weight:700;background:#eef1f5;border-radius:4px;padding:0 4px;margin:0 1px}'+
      'ol.refs{padding-left:0;list-style:none}ol.refs li{margin:7px 0;font-size:12.5px}'+
      'ol.refs .n{font-weight:700;margin-right:4px}ol.refs .m{color:#7a8089}'+
      'ol.refs .u{font-size:11px;margin-left:22px}'+
      'a{color:#1a4fa0}@page{size:A4;margin:16mm 14mm}'+
      '@media print{a{text-decoration:none}}';
    var w=window.open('','_blank');
    if(!w){ status('팝업이 차단되었습니다 — 허용 후 다시 시도하세요', true); return; }
    w.document.write('<!DOCTYPE html><html lang="ko"><head><meta charset="utf-8">'+
      '<title>'+esc(LAST.q)+'</title><style>'+css+'</style></head><body>'+
      '<h1>'+esc(LAST.q)+'</h1>'+
      '<div class="meta">citedby Deep Research · '+new Date().toLocaleString()+
      (LAST.model?(' · '+esc(LAST.model)):'')+'</div>'+
      mdToMarkup(LAST.answer)+
      (refs?('<h2>참고문헌</h2><ol class="refs">'+refs+'</ol>'):'')+
      '</body></html>');
    w.document.close();
    setTimeout(function(){ w.focus(); w.print(); }, 400);
  }
  function esc(s){return String(s||'').replace(/&/g,'&amp;').replace(/</g,'&lt;')
    .replace(/>/g,'&gt;').replace(/"/g,'&quot;');}

  function renderRefs(refs){
    var el=$('drRefs'); if(!el) return;
    if(!refs.length){el.innerHTML=''; return;}
    el.innerHTML='<h4>근거</h4>'+refs.map(function(r,i){
      var link=r.attach?(' · <a href="zotero://open-pdf/library/items/'+r.attach
        +'">PDF 열기</a>'):'';
      var sec=r.section?(' <i>'+r.section.replace(/</g,'&lt;')+'</i>'):'';
      var prev=(r.text||'').slice(0,180).replace(/</g,'&lt;');
      return '<div class="dr-ref"><b>['+(i+1)+']</b> '+
        (r.title||'').replace(/</g,'&lt;')+sec+link+
        '<div class="dr-prev">'+prev+'…</div></div>';
    }).join('');
  }

  async function run(){
    var q=($('drQ')||{}).value||''; q=q.trim();
    if(!q||!READY) return;
    var deeper=!!(($('drDeeper')||{}).checked);
    var web=!!(($('drWeb')||{}).checked);
    $('drGo').disabled=true; $('drAns').textContent='';
    var bar=$('drExport'); if(bar) bar.style.display='none';
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
        return {text:c.text, title:p.title||c.slug, attach:p.zotero_attach||'',
                section:c.section||'', year:p.year||'', authors:p.authors||'',
                doi:p.doi||'', arxiv:p.arxiv||'', url:p.url||p.external_url||''};
      });
      renderRefs(refs);

      LAST={q:q,answer:'',refs:refs,model:'',deeper:deeper,web:web};
      window._citedbyLast=LAST;
      status((deeper?'Deeper Research':'답변')+' 작성 중… 근거 '+refs.length+'건'+
             (web?' · web 검색':''));
      var text=await answer(q, refs, deeper, web, function(partial){
        LAST.answer=partial;
        $('drAns').innerHTML=mdToMarkup(partial);
      });
      LAST.answer=text; LAST.model=LAST_MODEL;
      window._citedbyLast=LAST;
      $('drAns').innerHTML=mdToMarkup(text);
      if(bar) bar.style.display='';
      status('완료 — 근거 '+refs.length+'건'+(LAST_MODEL?(' · '+LAST_MODEL):''));
    }catch(e){ status(String(e.message||e), true); }
    $('drGo').disabled=false;
  }

  document.addEventListener('DOMContentLoaded', function(){
    var go=$('drGo'); if(go) go.addEventListener('click', run);
    var map={drPdf:exportPdf, drMd:exportMd, drObs:exportObsidian,
             drAudioBtn:function(){
               // 오디오는 paper-curation 의 Audio Overview 모듈이 전담한다
               // (대본 생성 → Gemini TTS → mp3 → 이메일 발송까지 포함).
               // 여기서는 컨텍스트만 넘기고 모달을 연다.
               if(!LAST.answer){ status('먼저 질문에 답을 받으세요', true); return; }
               if(typeof window.openAudioModal==='function'){
                 window._citedbyAudioMode='deep'; window.openAudioModal();
               }
               else status('Audio Overview 모듈이 로드되지 않았습니다', true);
             }};
    Object.keys(map).forEach(function(id){
      var b=$(id); if(b) b.addEventListener('click', map[id]);
    });
    var q=$('drQ'); if(q) q.addEventListener('keydown', function(e){
      if(e.key==='Enter') run(); });
    var deeper=$('drDeeper'), note=$('drDeeperNote');
    if(deeper) deeper.addEventListener('change',function(){
      if(note) note.textContent=deeper.checked?'Long · 최상위 모델 · 심층 종합':'';
    });
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
        '<label class="dr-opt" title="코퍼스 밖 최신 자료를 web search로 보완">'
        '<input id="drWeb" type="checkbox">🌐 web</label>'
        '<label class="dr-opt" title="더 길고 구조적인 심층 종합">'
        '<input id="drDeeper" type="checkbox">Deeper</label>'
        '<span class="dr-deeper-note" id="drDeeperNote"></span>'
        f'<button id="drGo" class="dr-go" type="button" disabled>'
        f'{lbl["dr_go"]}</button>'
        "</div>"
        '<div class="dr-off" id="drOffline" style="display:none">'
        f'{lbl["dr_offline"]}'
        '<div id="drOfflineWhy" style="margin-top:6px;font-size:12px"></div>'
        "</div>"
        '<div class="dr-exp" id="drExport" style="display:none">'
        f'<button class="dr-x" id="drPdf" type="button">{lbl["exp_pdf"]}</button>'
        f'<button class="dr-x" id="drMd" type="button">{lbl["exp_md"]}</button>'
        f'<button class="dr-x" id="drObs" type="button">{lbl["exp_obs"]}</button>'
        f'<button class="dr-x" id="drAudioBtn" type="button">{lbl["exp_audio"]}</button>'
        "</div>"
        '<div class="dr-status" id="drStatus"></div>'
        '<div class="dr-ans" id="drAns"></div>'
        '<audio id="drAudio" controls style="display:none;width:100%;margin-top:10px"></audio>'
        '<div class="dr-refs" id="drRefs"></div>'
        "</section>"
    )


AUDIO_PROVIDER_JS = (
    "window._audioContextProvider = function() {\n"
    "  var mode = window._citedbyAudioMode || 'report';\n"
    "  var L = (window._citedbyLast || {});\n"
    "  if (mode === 'deep') {\n"
    "    if (L.answer) {\n"
    "      return {\n"
    "        title: (L.q || 'citedby-deep-research'),\n"
    "        review: '[질문]\\n' + (L.q || '') + '\\n\\n[답변]\\n' + L.answer,\n"
    "        connections: (L.refs || []).map(function(r) {\n"
    "          return {title: r.title, relation: '근거', reason: r.section || ''};\n"
    "        })\n"
    "      };\n"
    "    }\n"
    "  }\n"
    "  // 리포트 오디오는 Deep 답변 상태와 무관하게 citedby 본문만 읽는다.\n"
    "  var txt = function(sel) {\n"
    "    return Array.prototype.map.call(document.querySelectorAll(sel),\n"
    "      function(n) { return (n.innerText || '').trim(); })\n"
    "      .filter(Boolean).join('\\n\\n');\n"
    "  };\n"
    "  var seed = document.querySelector('.seed-title, h1');\n"
    "  var parts = [];\n"
    "  var ov = txt('.tl-over');\n"
    "  if (ov) parts.push('[인용 흐름 개요]\\n' + ov);\n"
    "  var streams = txt('.stc');\n"
    "  if (streams) parts.push('[연구 갈래]\\n' + streams);\n"
    "  var papers = Array.prototype.slice.call(document.querySelectorAll('.card'), 0, 30)\n"
    "    .map(function(n) { return (n.innerText || '').trim(); }).filter(Boolean);\n"
    "  if (papers.length) parts.push('[논문별 분석]\\n' + papers.join('\\n\\n'));\n"
    "  return {\n"
    "    title: (seed ? seed.innerText.trim() : 'citedby'),\n"
    "    review: parts.join('\\n\\n'),\n"
    "    connections: Array.prototype.slice.call(\n"
    "      document.querySelectorAll('.card h3, .card .t'), 0, 30).map(\n"
    "      function(n) {\n"
    "        return {title: (n.innerText || '').trim(),\n"
    "                relation: '인용', reason: ''};\n"
    "      })\n"
    "  };\n"
    "};"
)


def panel_script(index_file: str, collection: str = "") -> str:
    return (
        '<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>\n'
        "<script>\n"
        f"var IDX_FILE={json.dumps(index_file)};\n"
        f"var MODELS={json.dumps(_MODELS)};\n"
        f"var TOPK={TOPK};var POOL={POOL};var PER_PAPER={PER_PAPER};"
        f"var MAX_OUT={MAX_OUT};var COLLECTION={json.dumps(collection or '_cross')};\n"
        f"{_JS}\n</script>"
    )
