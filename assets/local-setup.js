/* One local setup panel, shared by stage guides and the checkpoint catalogue. */
(() => {
  const base=new URL('../',document.currentScript.src);
  const node=(tag,text)=>{const n=document.createElement(tag);if(text)n.textContent=text;return n;};
  const link=(text,path)=>{const a=node('a',text);a.href=new URL(path,base).href;return a;};
  const command=(parent,text,label='Copy command')=>{
    const pre=node('pre',text),copy=node('button',label);copy.type='button';
    copy.onclick=async()=>{try{await navigator.clipboard.writeText(text);copy.textContent='Copied';}catch(_){copy.textContent='Select and copy the command above';}};
    parent.append(pre,copy);
  };
  function render(panel,c,communityName){
    panel.replaceChildren();
    const heading=node('h3',c.kind==='aggregator'?'Run '+c.stage+' locally':'Run '+(communityName||'r/'+c.entity)+' locally');
    heading.id=panel.id+'-title';panel.setAttribute('aria-labelledby',heading.id);panel.append(heading);
    panel.append(node('p','Checkpoint '+c.milestone+': '+c.title+'.'));
    if(c.local_route?.kind==='review-archive'){renderArchive(panel,c,c.local_route);return;}
    if(c.local_route?.kind==='published-git'){renderGit(panel,c,c.local_route);return;}
    if(c.local_route?.kind==='release-launcher'){renderRelease(panel,c,c.local_route);return;}
    if(c.availability!=='ready'||!c.bundle?.url||!c.bundle?.sha256){panel.append(node('p',c.reason||'This checkpoint is not yet available for local interviews.'));return;}
    if(!/^[A-Za-z0-9][A-Za-z0-9_.-]*$/.test(c.id)||!['codex','claude'].includes(c.backend))throw Error('This checkpoint needs a manually checked launch command.');
    panel.append(node('p','Paste this command into Terminal on your Mac or Linux computer. It downloads and verifies the launcher and checkpoint, asks you to sign in if needed, and opens the selected interview.'));
    const downloads=new URL('downloads',base),quote=value=>"'"+value.replaceAll("'","'\\''")+"'";
    if(downloads.protocol==='https:'||(downloads.protocol==='http:'&&['localhost','127.0.0.1','[::1]'].includes(downloads.hostname))){
      const run='set -e; script=$(curl -fsSL "$1/start-interview.sh"); exec bash -c "$script" -- "$2" "$1"';
      command(panel,'bash -c '+quote(run)+' _ '+quote(downloads.href)+' '+quote(c.id));
    }else panel.append(node('p','Open this guide through its HTTPS website or a localhost preview to copy the setup command. The steps below are also available.'));
    panel.append(node('p','Use Python 3.11 or newer, Git, GitHub CLI and the supported '+(c.backend==='claude'?'Claude Code':'Codex')+' version. Missing tools or access are reported before an interview starts.'));
    panel.append(node('p','No model turn begins until you ask a question. Questions use your own account.'));
    panel.append(node('h4','Or follow these steps'));
    const steps=node('ol');steps.className='local-setup-steps';
    const download=node('li');download.append(link('Download the interview launcher','downloads/rplace-interviews.zip'),node('p','Extract the ZIP and open Terminal in its rplace-interviews folder. Follow the full setup instructions for dependencies.'));
    const login=node('li');login.append(node('p','Sign in with your account.'));command(login,'python3 -m website.interview login '+c.backend,'Copy sign-in command');
    const launch=node('li');launch.append(node('p','Open checkpoint '+c.milestone+'.'));command(launch,'python3 -m website.interview launch '+c.id,'Copy launch command');
    steps.append(download,login,launch);panel.append(steps);
    const offline=node('details');offline.append(node('summary','Already downloaded the checkpoint?'),link('Verified checkpoint bundle',c.bundle.url));command(offline,'python3 -m website.interview launch '+c.id+' --bundle /path/to/bundle.tar.gz','Copy offline command');panel.append(offline);
    panel.append(link('Full setup instructions','guides/interviews.html#open-an-interview-on-your-computer'));
  }
  /* The review copy: one archive per checkpoint, downloaded, checked, unpacked and resumed by get-checkpoint.sh. */
  function renderArchive(panel,c,r){
    if(!/^[A-Za-z0-9][A-Za-z0-9_.-]*$/.test(r.archive)||!['codex','claude'].includes(c.backend)||r.command!=='curl -fL '+r.script_url+' -o get-checkpoint.sh && bash get-checkpoint.sh '+r.archive)throw Error('This checkpoint needs a manually checked launch command.');
    const cli=c.backend==='claude'?'Claude Code':'Codex';
    panel.append(node('p','Paste this command into Terminal on your Mac or Linux computer. It downloads the release helper, then this checkpoint\'s archive, which it checks, unpacks in ~/rplace-checkpoints and opens as a private interview page on your computer. Large archives come in parts, joined automatically.'));
    const privacy=node('p','The original archive retains Reddit usernames. ');
    privacy.append(link('How participant identities are handled','guides/history.html#release-access'));
    command(panel,r.command);
    panel.append(privacy);
    const version=(c.cli_version||'').replace(/\s*\(Claude Code\)/,'').replace(/^codex-cli\s+/,'');
    panel.append(node('p','Use Python 3.11 or newer and '+cli+(version?' '+version:'')+'. Allow about three times the archive\'s size in free disk space. No model turn begins until you ask a question; questions use your own account.'));
    panel.append(node('h4','Or follow these steps'));
    const steps=node('ol');steps.className='local-setup-steps';
    const get=node('li');const rel=node('a','Download get-checkpoint.sh');rel.href=r.script_url;get.append(rel,node('p','The release helper; read it before running it if you like. The release also lists every archive and its checksum.'));
    const open=node('li');open.append(node('p','Run it with this checkpoint\'s archive name.'));command(open,'bash get-checkpoint.sh '+r.archive,'Copy the step');
    steps.append(get,open);panel.append(steps);
    panel.append(link('Full setup instructions','guides/interviews.html#open-an-interview-on-your-computer'));
  }
  /* A checkpoint opened with the release launcher of 4 November 2026: the exact command from the release's ALL-COMMANDS.md. */
  function renderRelease(panel,c,r){
    const rel=r.release;
    if(!rel||!['codex','claude'].includes(c.backend)||!r.command.includes(rel.start_url)||!r.command.trimEnd().endsWith("'"+c.id+"'"))throw Error('This checkpoint needs a manually checked launch command.');
    const cli=c.backend==='claude'?'Claude Code':'Codex';
    panel.append(node('p','Paste this command into Terminal on your Mac or Linux computer. It downloads and verifies the interview launcher from the release of 4 November 2026, checks your tools, asks you to sign in if needed, and opens a private interview page on your computer.'));
    command(panel,r.command);
    panel.append(node('p',c.bundle?.url?'It restores the checkpoint from its verified bundle; every restored file must match the tested manifest.':'It restores the checkpoint from the original files in the research repository and a hashed supplement of saved files; every restored file must match the tested manifest.'));
    panel.append(node('p','Use Python 3.11 or newer, Git, GitHub CLI and the supported '+cli+' version, and allow up to about '+rel.max_free_gib+' GiB of free disk space. An unsupported version or a failed sign-in stops the command; it never starts a new agent.'));
    panel.append(node('p','No model turn begins until you ask a question. Questions use your own account. Run one interview at a time.'));
    panel.append(node('h4','Or follow these steps'));
    const steps=node('ol');steps.className='local-setup-steps';
    const get=node('li');get.append(link('Download the interview launcher',rel.launcher.url),node('p','About '+Math.round(rel.launcher.bytes/1024**2)+' MB. Its SHA-256 must be '+rel.launcher.sha256+'.'));command(get,'shasum -a 256 rplace-interviews.zip','Copy check command');
    const open=node('li');open.append(node('p','Extract it, open Terminal in its rplace-interviews folder and open checkpoint '+c.milestone+'. The command signs you in if needed.'));command(open,'python3 -m website.quickstart '+c.id,'Copy launch command');
    steps.append(get,open);panel.append(steps);
    if(c.bundle?.url){const offline=node('details');offline.append(node('summary','Already downloaded the checkpoint?'),link('Verified checkpoint bundle',c.bundle.url));command(offline,'python3 -m website.interview launch '+c.id+' --bundle /path/to/bundle.tar.gz','Copy offline command');panel.append(offline);}
    panel.append(link('Full setup instructions','guides/interviews.html#open-an-interview-on-your-computer'));
  }
  /* A checkpoint opened from the published r-place workspace (handoff checkpoints-20261104): no bundle, Claude Code in the terminal. */
  function renderGit(panel,c,r){
    if(c.backend!=='claude'||r.opens!=='claude-cli'||!/^https:\/\/raw\.githubusercontent\.com\/os-fruit-fly\/os-fruit-fly\.github\.io\/[0-9a-f]{40}\//.test(r.starter_url)||!r.command.includes(r.starter_url.replace(/\/start-e2b-from-rplace\.sh$/,'')))throw Error('This checkpoint needs a manually checked launch command.');
    const leg=c.milestone.split('.').pop(),gib=Math.round(r.minimum_free_bytes/1024**3),cli=r.cli_version.split(' ')[0];
    panel.append(node('p','Paste this command into Terminal on your Mac or Linux computer. It restores the published r-place workspace at commit '+r.commit.slice(0,7)+' and the unchanged '+leg+' conversation from GitHub, checks every file, asks you to sign in to Claude if needed, and opens a separate interview in Claude Code, in your terminal.'));
    command(panel,r.command);
    panel.append(node('p','This is the published workspace, not every file of the original local snapshot: '+r.snapshot_files_not_restored+' local files, such as older conversations, local settings and bookkeeping, are not in it. The saved conversation stays unchanged; your interview runs as a fork with its own session.'));
    panel.append(node('p','Use Python 3.11 or newer, Git, Claude Code '+cli+' and '+gib+' GiB of free disk space. If the Claude Code version or the sign-in check fails, the command stops; it never starts a new analyst.'));
    panel.append(node('p','No model turn begins until you ask a question. Questions use your own account.'));
    panel.append(node('h4','Or follow these steps'));
    const steps=node('ol');steps.className='local-setup-steps';
    const get=node('li');get.append(link('Download the '+leg+' launcher',r.launcher.url),node('p','About '+Math.round(r.launcher.bytes/1024)+' KB of code and metadata, no research data. Its SHA-256 must be '+r.launcher.sha256+'.'));command(get,'shasum -a 256 e2b-git-launcher.zip','Copy check command');
    const prep=node('li');prep.append(node('p','Extract it and check the files without signing in. This downloads the published workspace from GitHub, about 7 GB.'));command(prep,'unzip e2b-git-launcher.zip && python3 -B rplace-e2b-git/tools/e2b_from_rplace.py --prepare-only','Copy check command');
    const open=node('li');open.append(node('p','Open the interview in Claude Code.'));command(open,'python3 -B rplace-e2b-git/tools/e2b_from_rplace.py','Copy launch command');
    steps.append(get,prep,open);panel.append(steps);
    panel.append(link('Full setup instructions','guides/interviews.html#open-an-interview-on-your-computer'));
  }
  let catalogue;
  const entry=id=>{
    if(!catalogue)catalogue=fetch(new URL('catalog.json',base)).then(r=>{if(!r.ok)throw Error('The checkpoint catalogue could not be loaded.');return r.json();}).catch(e=>{catalogue=null;throw e;});
    return catalogue.then(cat=>{const c=cat.checkpoints.find(c=>c.id===id);if(!c)throw Error('This checkpoint is not in the catalogue.');return c;});
  };
  function mount(button,panel,checkpoint){
    panel.hidden=true;panel.classList.add('local-setup');panel.setAttribute('role','region');
    button.title='Run on your computer with the checkpoint’s terminal command';button.type='button';button.setAttribute('aria-controls',panel.id);button.setAttribute('aria-expanded','false');
    let loaded=false;
    async function toggle(){
      const open=button.getAttribute('aria-expanded')!=='true';button.setAttribute('aria-expanded',String(open));panel.hidden=!open;
      if(!open||loaded||panel.hasAttribute('aria-busy'))return;

      panel.replaceChildren(node('p','Loading local setup…'));
      panel.tabIndex=0;
      panel.setAttribute('aria-label','Loading local setup');
      panel.setAttribute('aria-busy','true');

      let checkpointData, error;
      try{checkpointData=typeof checkpoint==='string'?await entry(checkpoint):checkpoint;}
      catch(e){error=e;}

      // Tab can enter or leave the loading panel while the catalogue is in flight.
      const focused=document.activeElement;
      const follow=focused!==panel && focused.matches(':focus-visible') &&
        (panel.compareDocumentPosition(focused)&Node.DOCUMENT_POSITION_FOLLOWING) &&
        focused.getBoundingClientRect().top<innerHeight && focused.getBoundingClientRect().bottom>0;
      try{
        if(error)throw error;
        render(panel,checkpointData,button.dataset.communityName);
        loaded=true;
        panel.removeAttribute('aria-label');
      }catch(e){
        const message=node('p',e.message+' Close and reopen Chat Locally to retry.');
        message.setAttribute('role','status');
        panel.replaceChildren(message);
        panel.removeAttribute('aria-labelledby');
        panel.setAttribute('aria-label','Local setup unavailable');
      }
      panel.tabIndex=-1;
      panel.removeAttribute('aria-busy');
      if(focused===panel){
        (panel.querySelector('button,a[href]')||panel).focus();
      }else if(follow && focused.getBoundingClientRect().top>=innerHeight){
        // The expanded instructions may have pushed the next focused link off screen.
        focused.scrollIntoView({block:'nearest'});
      }
    }
    button.addEventListener('click',toggle);return {open:()=>button.getAttribute('aria-expanded')==='true'?Promise.resolve():toggle()};
  }
  window.RplaceLocalSetup={mount};
  document.querySelectorAll('button[data-local-checkpoint]').forEach(button=>{
    const panel=document.getElementById(button.getAttribute('aria-controls'));
    if(panel)mount(button,panel,button.dataset.localCheckpoint);
  });
})();
