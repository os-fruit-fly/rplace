(async()=>{
  const root=document.querySelector('[data-chat-route]');if(!root)return;
  const route=root.dataset.chatRoute,q=new URLSearchParams(location.search),checkpoint=q.get('checkpoint')||'';
  const status=document.getElementById('route-status'),content=document.getElementById('route-content');
  const node=(tag,text)=>{const n=document.createElement(tag);if(text)n.textContent=text;return n;};
  const link=(text,url,newTab=false)=>{const a=node('a',text);a.href=url;if(newTab){a.target='_blank';a.rel='noopener';}return a;};
  const selected=checkpoint?'?checkpoint='+encodeURIComponent(checkpoint):'';
  const json=async(path,body)=>{const r=await fetch(path,{method:body?'POST':'GET',headers:body?{'Content-Type':'application/json'}:{},body:body?JSON.stringify(body):undefined,cache:'no-store'});if(path==='/api/hosted-session'&&r.status===404)return {authenticated:false};let d;try{d=await r.json();}catch(_){throw Error('Online interviews are not connected to this website yet.');}if(!r.ok)throw Error(d.error||'The interview server is unavailable.');return d;};
  const login=()=>{const p=new URLSearchParams();if(checkpoint)p.set('checkpoint',checkpoint);if(/^[0-9a-f]{32}$/.test(q.get('interview')||''))p.set('interview',q.get('interview'));if(route==='open-interviews')p.set('next','open-interviews');location.replace('login.html?'+p);};
  if(document.getElementById('route-local'))document.getElementById('route-local').href='local-chat.html'+selected;
  try{
    if(route==='local-chat'){
      const destination=new URL('interviews.html',location.href);
      if(checkpoint){destination.searchParams.set('checkpoint',checkpoint);destination.searchParams.set('local','1');destination.hash='checkpoint-'+checkpoint;}
      location.replace(destination.href);return;
    }
    const configResponse=await fetch(new URL('config.json',location.href),{cache:'no-store'});
    if(!configResponse.ok)throw Error('The interview settings could not be loaded.');
    const config=await configResponse.json();
    if(config.hosting_mode==='static'){
      if(config.hosted_url){
        const origin=new URL(config.hosted_url);
        if(origin.protocol!=='https:'||origin.username||origin.password)throw Error('The interview server address is not valid.');
        if(origin.origin===location.origin)throw Error('The interview server is not connected yet.');
        const page=route==='open-interviews'?'open-interviews.html':route==='login'?'login.html':'online-chat.html';
        const destination=new URL('/'+page,origin);destination.search=location.search;destination.hash=location.hash;
        location.replace(destination.href);return;
      }
      status.textContent='Online interviews are not connected yet.';
      content.replaceChildren(node('p','You can read the study here and use Run on your computer to open a checkpoint on your own computer. Checkpoint downloads come from the public research repository.'));
      if(document.getElementById('retention-note'))document.getElementById('retention-note').hidden=true;
      return;
    }
    const session=await json('/api/hosted-session');if(!session.authenticated){login();return;}
    if(route==='online-chat'){
      if(!checkpoint){status.textContent='Choose a checkpoint before opening a chat.';content.append(link('Choose a checkpoint','interviews.html'));return;}
      const rows=await json('/api/checkpoints');if(!rows.some(c=>c.id===checkpoint)){status.textContent='This checkpoint is not available on the interview server. No other checkpoint was opened.';return;}
      const p=new URLSearchParams({checkpoint});if(/^[0-9a-f]{32}$/.test(q.get('interview')||''))p.set('interview',q.get('interview'));
      location.replace('/talk?'+p);return;
    }
    let previous='',loading=false;
    const phases={waiting_restore:'Waiting to restore',restoring_originals:'Restoring and verifying original files',downloading:'Downloading files',unpacking_verifying:'Unpacking and verifying',checking_identity:'Checking session identity',files_ready:'Ready for a question',opening_conversation:'Opening the saved conversation',answering:'Answering',ready:'Ready',error:'Needs operator attention'};
    async function refresh(){if(loading)return;loading=true;try{
      const data=await json('/api/interviews');status.textContent=data.interviews.length+' of '+data.capacity+' interview slots in use.';
      document.getElementById('retention-note').textContent='Each interview closes after inactivity lasting '+Math.round(data.idle_seconds/60)+' minutes. Closing a browser tab does not close an interview immediately. A server restart also ends access to these copies.';
      const digest=JSON.stringify(data);if(previous===digest)return;previous=digest;content.replaceChildren();
      if(!data.interviews.length){content.append(node('p','You have no open interviews. Choose a checkpoint and select Chat Online.'));return;}
      for(const s of data.interviews){
        const item=node('article');item.className='checkpoint';item.append(node('h2',s.title),node('p',phases[s.phase]||s.status));
        const actions=node('div');actions.className='actions';const open=link('Return to interview',s.url,true),exportButton=node('button','Export'),close=node('button','Close interview');open.className='talk-action';actions.append(open,exportButton,close);item.append(actions);
        const confirmation=node('div');confirmation.hidden=true;confirmation.className='close-confirmation';const cancel=node('button','Keep open'),confirm=node('button','Close and delete copy');confirmation.append(node('p','Export first to keep the conversation. Closing deletes this interview and its disposable files. The original checkpoint stays intact.'),cancel,confirm);item.append(confirmation);
        close.onclick=()=>{confirmation.hidden=false;cancel.focus();};cancel.onclick=()=>{confirmation.hidden=true;close.focus();};
        confirm.onclick=async()=>{confirm.disabled=true;try{await json('/api/interviews/'+s.id+'/end',{});previous='';await refresh();}catch(e){status.textContent=e.message;confirm.disabled=false;}};
        exportButton.onclick=async()=>{try{const d=await json('/api/interviews/'+s.id+'/export'),url=URL.createObjectURL(new Blob([JSON.stringify(d,null,2)],{type:'application/json'})),a=link('Export',url);a.download='checkpoint-interview-'+s.id+'.json';a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);}catch(e){status.textContent=e.message;}};
        content.append(item);
      }
    }catch(e){status.textContent=e.message+' Your interviews were not restarted.';}finally{loading=false;}}
    await refresh();setInterval(refresh,15000);
  }catch(e){status.textContent=e.message;content.append(link('Choose a checkpoint','interviews.html'));}
})();
