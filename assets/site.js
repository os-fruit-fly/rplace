/* No analytics, research actions, or third-party resources. */
(() => {
  const theme=document.getElementById('theme');let mode='light';
  try{mode=localStorage.getItem('rplace-theme')||'light';}catch(_){}
  function applyTheme(){document.documentElement.dataset.theme=mode;if(theme)theme.textContent=`Theme: ${mode}`;}
  applyTheme();if(theme)theme.onclick=()=>{mode=['light','dark','system'][(['light','dark','system'].indexOf(mode)+1)%3];try{localStorage.setItem('rplace-theme',mode);}catch(_){}applyTheme();};
  const menu=document.querySelector('header .menu'),here=menu&&menu.querySelector('[aria-current]');const showHere=()=>{if(!here)return;const m=menu.getBoundingClientRect(),h=here.getBoundingClientRect();if(h.right>m.right-48)menu.scrollLeft+=h.right-m.right+60;};(document.fonts?document.fonts.ready:Promise.resolve()).then(()=>{if(menu&&menu.scrollWidth>menu.clientWidth)menu.classList.add('scrolls');showHere();});
  const tabs=document.querySelector('main .parts'),tab=tabs&&tabs.querySelector('[aria-current]');(document.fonts?document.fonts.ready:Promise.resolve()).then(()=>{if(!tab)return;const r=tabs.getBoundingClientRect(),t=tab.getBoundingClientRect();if(t.right>r.right-48)tabs.scrollLeft+=t.right-r.right+60;});
  document.querySelectorAll('.page-run pre.text code, .page-run pre code.language-text').forEach(code=>{
    const copy=document.createElement('button');copy.type='button';copy.textContent='Copy prompt';
    copy.onclick=async()=>{try{await navigator.clipboard.writeText(code.textContent);copy.textContent='Copied';}catch(_){copy.textContent='Select and copy the prompt above';}};code.parentElement.after(copy);
  });
  const picker=document.getElementById('stage-picker');if(picker)picker.onsubmit=e=>{e.preventDefault();location.href=document.getElementById('stage-choice').value;};
  const search=document.getElementById('reference-search');
  if(search){const rows=[...document.querySelectorAll('#reference-index li')];const filter=()=>{const terms=search.value.toLocaleLowerCase().trim().split(/\s+/).filter(Boolean);let count=0;rows.forEach(row=>{const text=row.textContent.toLocaleLowerCase();row.hidden=!terms.every(term=>text.includes(term));if(!row.hidden)count++;});document.getElementById('reference-count').textContent=`${count} of ${rows.length} manual entries`;document.getElementById('reference-empty').hidden=count>0;};search.addEventListener('input',filter);filter();}
  const resources=document.querySelector('.interview-parts details');
  if(resources){
    document.addEventListener('click',event=>{if(!resources.contains(event.target))resources.open=false;});
    resources.addEventListener('keydown',event=>{
      if(event.key==='Escape'&&resources.open){resources.open=false;resources.querySelector('summary').focus();}
    });
  }
  // Published links to a selected checkpoint keep their query and anchor on the directory.
  if(document.querySelector('.page-interviews #talk-to-a-saved-agent')){
    const url=new URL(location.href);
    const direct=['checkpoint','stage','entity','scope','page','local'].some(key=>url.searchParams.has(key));
    const oldMap=['#catalogue','#checkpoint-results','#community-map','#aggregator-map'].includes(url.hash);
    if(direct||oldMap||url.hash.startsWith('#checkpoint-')){
      if(!direct&&url.hash.startsWith('#checkpoint-')&&!oldMap)url.searchParams.set('checkpoint',url.hash.slice('#checkpoint-'.length));
      if(!direct&&url.hash==='#aggregator-map')url.searchParams.set('kind','aggregator');
      const next=new URL('all-interviews.html',url);next.search=url.search;next.hash=url.hash;
      location.replace(next.href);return;
    }
  }
  if(!document.getElementById('catalogue'))return;
  const el=(tag,text,cls)=>{const e=document.createElement(tag);if(text!=null)e.textContent=text;if(cls)e.className=cls;return e;};
  const link=(text,url)=>{const a=el('a',text);a.href=url;return a;};
  const list=document.getElementById('checkpoint-list'),status=document.getElementById('catalogue-status'),title=document.getElementById('selection-title'),other=document.getElementById('other-checkpoints'),otherList=document.getElementById('other-checkpoint-list'),otherSummary=document.getElementById('other-checkpoint-summary'),description=document.getElementById('stage-description');
  // Availability is supplied by the local preview or authenticated pilot, never inferred from a bundle alone.
  const choices=fetch('/api/interview-options',{cache:'no-store'}).then(r=>r.status===404?fetch('/api/local-interviews',{cache:'no-store'}):r).then(r=>r.ok?r.json():{checkpoints:[]}).catch(()=>({checkpoints:[]}));
  Promise.all([fetch('catalog.json').then(r=>{if(!r.ok)throw Error('Catalogue could not be loaded.');return r.json();}),fetch('config.json').then(r=>r.json()),choices,fetch('records/index.json').then(r=>r.ok?r.json():{checkpoints:{}}).catch(()=>({checkpoints:{}})),fetch('history.json').then(r=>{if(!r.ok)throw Error('Historical context could not be loaded.');return r.json();})]).then(([cat,config,available,records,historical])=>{
    const privateChoices=new Map((available.checkpoints||[]).filter(row=>cat.checkpoints.some(c=>c.id===row.id)).map(row=>[row.id,row]));
    const stageDescriptions=new Map([...document.querySelectorAll('[data-stage]')].map(a=>[a.dataset.stage,a.dataset.description]));const PAGE_SIZE=12;let page=1,selected='',invalid='',kind='aggregator',entity='',scope='featured';
    function readURL(){
      const q=new URLSearchParams(location.search);selected=q.get('checkpoint')||'';invalid='';const c=cat.checkpoints.find(x=>x.id===selected);
      if(selected&&!c)invalid='The requested checkpoint is not in this catalogue.';
      const requestedKind=q.get('kind');if(requestedKind&&!['community','aggregator'].includes(requestedKind))invalid='The requested study is not in this catalogue.';
      kind=c?.kind||(q.has('stage')?'aggregator':requestedKind)||'community';
      entity=c?(c.kind==='community'?c.entity:c.stage):(kind==='aggregator'?q.get('stage')||q.get('entity')||'':q.get('entity')||'');
      scope=q.get('scope')==='all'?'all':'featured';
      const n=Number(q.get('page'));page=Number.isSafeInteger(n)&&n>0?n:1;
    }
    function writeURL(){
      const u=new URL(location.href);u.search='';u.searchParams.set('kind',kind);if(entity)u.searchParams.set(kind==='aggregator'?'stage':'entity',entity);if(scope==='all'&&kind==='aggregator')u.searchParams.set('scope','all');if(page>1)u.searchParams.set('page',page);if(selected)u.searchParams.set('checkpoint',selected);
      history.pushState(null,'',u);
    }
    function matching(){
      if(invalid||!entity)return [];
      let rows=cat.checkpoints.filter(c=>c.kind===kind&&(c.kind==='community'?c.entity:c.stage)===entity);
      if(kind==='community'&&rows.some(c=>c.availability==='ready')){
        rows=rows.filter(c=>c.availability==='ready'||c.id===selected);
      }
      // Use the recorded close date, or saved date if no close timestamp exists.
      const savedTime=c=>Date.parse(c.closed_utc||historical.checkpoints[c.id]?.saved_utc)||0;
      return kind==='aggregator'?rows.sort((a,b)=>Number(b.availability==='ready')-Number(a.availability==='ready')||savedTime(b)-savedTime(a)||a.id.localeCompare(b.id)):rows;
    }
    function pager(total){
      const nav=el('nav',null,'catalogue-nav');nav.setAttribute('aria-label','Checkpoint pages');const pages=Math.max(1,Math.ceil(total/PAGE_SIZE));
      for(const [label,target]of [['Previous',page-1],['Next',page+1]]){const b=el('button',label);b.type='button';b.disabled=target<1||target>pages;b.onclick=()=>{page=target;selected='';writeURL();draw();(kind==='aggregator'?otherSummary:title).focus();};nav.append(b);}
      nav.append(el('span',`Page ${page} of ${pages}`));return nav;
    }
    function draw(){
      document.getElementById('checkpoint-results').hidden=!entity&&!invalid;
      document.getElementById('aggregator-map').hidden=kind!=='aggregator';document.getElementById('community-map').hidden=kind!=='community';other.hidden=true;otherList.replaceChildren();
      document.querySelectorAll('[data-kind]').forEach(a=>a.setAttribute('aria-current',a.dataset.kind===kind?'true':'false'));
      document.querySelectorAll('[data-stage],[data-entity]').forEach(a=>{const current=(kind==='aggregator'?a.dataset.stage:a.dataset.entity)===entity&&!!entity;if(current)a.setAttribute('aria-current','true');else a.removeAttribute('aria-current');});
      const rows=matching(),secondary=kind==='aggregator'?rows.slice(1):rows;
      if(selected){const i=secondary.findIndex(c=>c.id===selected);if(i>=0){page=Math.floor(i/PAGE_SIZE)+1;if(kind==='aggregator')scope='all';}}
      page=Math.min(page,Math.max(1,Math.ceil(secondary.length/PAGE_SIZE)));const start=(page-1)*PAGE_SIZE;
      const stageName=cat.stages.find(s=>s.id===entity)?.name;
      title.textContent=entity?(kind==='community'?'r/'+entity:entity+(stageName?' · '+stageName:'')):(kind==='community'?'Choose a community above':'Choose a stage above');
      description.replaceChildren();description.hidden=kind!=='aggregator'||!rows.length;
      if(!description.hidden)description.append((stageDescriptions.get(entity)||'')+' ',link('Full stage description','stages/'+encodeURIComponent(entity)+'.html')); 
      status.textContent='';status.hidden=true;
      list.replaceChildren();
      if(!rows.length){if(entity||invalid)list.append(el('p',invalid||'No checkpoints are listed for this selection.'));other.open=false;return;}
      const cardFor=(c,primary=false)=>{
        const card=el('article',null,primary?'checkpoint checkpoint-stage':'checkpoint');card.id='checkpoint-'+c.id;card.setAttribute('aria-label',c.milestone);
        if(!primary)card.append(el('h3',c.kind==='community'?c.title:`${c.milestone.split('.').pop()} · ${c.title}`));
        if(c.kind==='community'){const descriptions={'coding-close':'After coding: codes, themes and the case account.','R6':'After the local model: the account, model and coding structure.','D2':'After the return: how the population model fits this community.','D3':'After the re-check: how the revised model fits this community.'};if(descriptions[c.milestone])card.append(el('p',descriptions[c.milestone],'why'));}
        const privateChoice=privateChoices.get(c.id),ready=(c.availability==='ready'&&c.bundle?.url&&c.bundle?.sha256)||c.local_route?.kind==='review-archive',h=historical.checkpoints[c.id];
        if(!primary&&h.saved_utc)card.append(el('p','Saved '+h.saved_utc.slice(0,10),'checkpoint-date'));
        const actions=el('div',null,'actions chat-actions'),local=el('button','Run on your computer');
        let onlineURL='online-chat.html?checkpoint='+encodeURIComponent(c.id);
        if(config.hosted_url){const u=new URL('/talk',config.hosted_url);if(u.protocol==='https:'){u.searchParams.set('checkpoint',c.id);onlineURL=u.href;}}
        local.className='talk-action talk-local';
        const online=link('Chat Locally',onlineURL);online.className='talk-action';online.target='_blank';online.rel='noopener';online.setAttribute('aria-label','Chat Locally at '+(c.kind==='community'?'r/'+c.entity+' '+c.title:c.milestone)+', opens in a new tab');
        if(ready&&config.hosted_url&&Array.isArray(config.prepared_checkpoints)){
          const prepared=config.prepared_checkpoints.includes(c.id);
          const text=prepared?'Chat Locally opens a prepared copy.':'Chat Locally unpacks this checkpoint when you open it. Large checkpoints can take several minutes.';
          card.append(el('p',text,'why'));
        }
        if(ready||privateChoice){actions.append(online,local);card.append(actions);}
        const setup=el('section');setup.id='local-setup-'+c.id;card.append(setup);
        const control=window.RplaceLocalSetup.mount(local,setup,c);
        if(ready&&selected===c.id&&new URLSearchParams(location.search).get('local')==='1')control.open();
        if(!primary&&!ready)card.append(el('p',c.candidate?'This checkpoint is being prepared for interviews.':c.reason||'An interview is not available for this checkpoint.','why'));
        const evidence=el('details',null,'checkpoint-evidence');evidence.append(el('summary','Evidence and details'));
        if(primary){evidence.append(el('p',c.milestone+' · '+c.title));if(!ready)evidence.append(el('p',c.candidate?'This checkpoint is being prepared for interviews.':c.reason||'An interview is not available for this checkpoint.','why'));}
        const links=el('div',null,'actions'),record=records.checkpoints?.[c.id];
        if(record)links.append(link('Read saved outputs',record.page));
        if(h.record_url)links.append(link('Read the '+(c.record_url?(c.record_kind||'record'):'saved handback'),h.record_url));
        if(c.outputs_url)links.append(link('Browse published outputs',c.outputs_url));if(c.original_source)links.append(link('Original GitHub files',c.original_source.url));evidence.append(links);
        const state=privateChoice||ready?'ready':c.candidate?'pending':c.availability==='record-only'?'record':'none';evidence.append(el('span',privateChoice?'Ready for a private interview':c.availability==='ready'?'Verified bundle':c.candidate?'Restore checked, release pending':c.availability==='record-only'?'Record only':'Not available','badge badge-'+state));
        evidence.append(el('p',h.saved_utc?`Saved-state date: ${h.saved_utc}. ${h.saved_date_basis}`:'Saved-state date: not recorded.'));
        const source=el('p');if(!h.source_commit)source.append('Source commit: not recorded on this site.');else source.append('Source commit: ',h.source_commit.slice(0,12),`, ${h.source_commit_date}. This is the commit date, not the close date.`);evidence.append(source);
        for(const note of h.notes){const p=el('p',note.text+' ','notice');p.append(link(note.label,note.url));evidence.append(p);}
        if(c.outputs_url)evidence.append(el('p','Published outputs may include later work. Read saved outputs for the selected files at this checkpoint. The launcher verifies the full saved state.','why'));
        const d=el('details');d.append(el('summary','Provenance and restore details'));const dl=el('dl');for(const k of ['backend','model','effort','cli_version','restored_cli_version','session_id','parent_checkpoint','origin_run','outputs_scope'])dl.append(el('dt',k.replaceAll('_',' ')),el('dd',c[k]||'Not recorded'));d.append(dl);
        if(h.lineage){d.append(el('p',`Verified D2 fork parent: ${h.lineage.fork_parent}. Original session: ${h.lineage.forked_from_session}. Fork boundary ordinal: ${h.lineage.forked_from_ordinal_exclusive}. D3 retains D2 session ${h.lineage.d2_session} in run.json.`),link('Selected native identity evidence',`history-evidence/${c.entity}-D2-lineage.json`));}
        if(c.original_source)d.append(link('File-by-file source recipe',c.original_source.recipe),el('p',`${c.original_source.git_files} files from the original GitHub commit; ${c.original_source.supplement_files} saved files from the declared supplement. The main conversation comes from ${c.original_source.primary_transcript_from_git?'the original GitHub transcript':'the saved-session archive, not a Git-tracked transcript'}.`),link('How original-source restoration works','ORIGINAL-SOURCES.md'));
        if(ready&&c.bundle?.sha256)d.append(el('p',`Bundle SHA-256: ${c.bundle.sha256}`));evidence.append(d,link('Link to this checkpoint',`all-interviews.html?checkpoint=${encodeURIComponent(c.id)}`));card.append(evidence);return card;
      };
      if(kind==='aggregator'){
        list.append(cardFor(rows[0],true));
        other.hidden=secondary.length===0;other.open=scope==='all'&&!other.hidden;
        secondary.slice(start,start+PAGE_SIZE).forEach(c=>otherList.append(cardFor(c)));
        if(secondary.length>PAGE_SIZE)otherList.append(pager(secondary.length));
      }else{
        other.open=false;
        secondary.slice(start,start+PAGE_SIZE).forEach(c=>list.append(cardFor(c)));
        if(secondary.length>PAGE_SIZE)list.append(pager(secondary.length));
      }
    }
    function navigate(a){const q=new URL(a.href).searchParams;selected='';invalid='';page=1;kind=q.get('kind')||(q.has('stage')?'aggregator':kind);entity=q.get('stage')||q.get('entity')||'';scope='featured';writeURL();draw();if(entity)title.focus();}
    document.querySelectorAll('[data-kind],[data-stage],[data-entity]').forEach(a=>a.addEventListener('click',e=>{if(e.button!==0||e.metaKey||e.ctrlKey||e.shiftKey||e.altKey)return;e.preventDefault();navigate(a);}));
    other.ontoggle=()=>{
      if(other.hidden)return;
      const next=other.open?'all':'featured';if(next===scope)return;
      scope=next;if(!other.open)selected='';writeURL();
    };
    window.addEventListener('popstate',()=>{readURL();draw();});readURL();draw();if(selected&&document.getElementById('checkpoint-'+selected)){const card=document.getElementById('checkpoint-'+selected);card.tabIndex=-1;card.focus();}else if(entity)title.focus();
  }).catch(e=>{status.hidden=false;status.textContent=e.message+' Use the static list below.';status.className='error';list.append(link('All checkpoint records','checkpoint-index.html'));});
})();
// A link to a saved file (#03-timeline) opens its section on the checkpoint page.
(function(){function openTarget(){const id=decodeURIComponent(location.hash.slice(1));if(!id)return;const el=document.getElementById(id);if(!el)return;let d=el.tagName==='DETAILS'?el:el.closest('details'),opened=false;while(d){if(!d.open){d.open=true;opened=true;}d=d.parentElement&&d.parentElement.closest('details');}if(opened||el.tagName==='DETAILS')el.scrollIntoView();}window.addEventListener('hashchange',openTarget);if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',openTarget);else openTarget();})();
