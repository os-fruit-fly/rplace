(async()=>{
  const q=new URLSearchParams(location.search),fragment=new URLSearchParams(location.hash.slice(1)),checkpoint=q.get('checkpoint'),sid=q.get('interview');
  const status=document.getElementById('invite-status'),form=document.getElementById('invite-form'),button=document.getElementById('invite-submit');
  const selected=new URLSearchParams();if(checkpoint)selected.set('checkpoint',checkpoint);if(/^[0-9a-f]{32}$/.test(sid||''))selected.set('interview',sid);
  // Only fixed, same-origin destinations. Arbitrary next URLs are never used.
  const target=q.get('next')==='open-interviews'?'open-interviews.html':checkpoint?'online-chat.html?'+selected:'open-interviews.html';
  document.getElementById('invite-local').href=checkpoint?'local-chat.html?checkpoint='+encodeURIComponent(checkpoint):'interviews.html';
  const invite=fragment.get('invite');history.replaceState(null,'',location.pathname+location.search);
  async function submit(code){button.disabled=true;status.textContent='Signing in…';try{
    const r=await fetch('/api/invite',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({invite:code}),cache:'no-store'});let d;try{d=await r.json();}catch(_){throw Error('Online interviews are not connected here yet. Use Chat Locally.');}if(!r.ok)throw Error(d.error||'The invitation could not be opened.');location.replace(target);
  }catch(e){status.textContent=e.message;button.disabled=false;}}
  form.onsubmit=e=>{e.preventDefault();submit(document.getElementById('invite-code').value.trim());};
  try{const r=await fetch('/api/hosted-session',{cache:'no-store'});if(!r.ok){status.textContent=r.status===404?'Online interviews are not connected to this preview yet. Use Chat Locally below.':'The online interview server is unavailable. Try again later or use Chat Locally.';form.hidden=true;return;}if((await r.json()).authenticated){location.replace(target);return;}}catch(_){status.textContent='The online interview server could not be reached. Try again later or use Chat Locally.';form.hidden=true;return;}
  if(invite)await submit(invite);
})();
