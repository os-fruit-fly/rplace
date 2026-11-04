/* Reviewer navigation never contains provider credentials. */
(async()=>{
  const entry=document.querySelector('[data-reviewer-entry]');if(!entry)return;
  try{
    const r=await fetch('/api/hosted-session',{cache:'no-store'});
    if(r.ok){const session=await r.json();if(session.authenticated){entry.textContent='Open interviews';entry.href=new URL('open-interviews.html',entry.href).href;return;}}
    const config=await fetch(new URL('config.json',entry.href)).then(r=>r.json());
    if(config.hosted_url){const base=new URL(config.hosted_url);if(base.protocol==='https:')entry.href=new URL('/open-interviews.html',base).href;}
  }catch(_){}
})();
