(() => {
  const formPicker = document.getElementById('form-choice');
  const roomPicker = document.getElementById('room-choice');
  const bars = document.getElementById('bars');
  const preferred = {A:'FloydVsVoid', B:'PlaceNL', C:'cubers', D:'gorillaz', E:'warframe', F:'dallasstars'};
  const ns = 'http://www.w3.org/2000/svg';
  const total = values => values.reduce((acc, value) => acc + value, 0);
  const pct = value => new Intl.NumberFormat('en', {style:'percent', maximumFractionDigits:1}).format(value);
  function shares(values) {
    const amount=total(values);
    return amount ? values.map(v => v/amount) : null;
  }
  function formMean(rows,key) {
    const eligible=rows.map(r => shares(r[key])).filter(Boolean);
    return eligible.length ? DN.map((_,i) => total(eligible.map(v => v[i]))/eligible.length) : null;
  }
  function rectangle(x,width,color) {
    const r=document.createElementNS(ns,'rect');
    r.setAttribute('x',x);r.setAttribute('width',width);r.setAttribute('height','10');r.setAttribute('fill',color);
    return r;
  }
  function strip(label, values) {
    const row=document.createElement('div');row.className='bar-row';
    const name=document.createElement('span');name.textContent=label;row.append(name);
    if(!values){row.append('No assigned values');return row;}
    const svg=document.createElementNS(ns,'svg');
    svg.setAttribute('viewBox','0 0 100 10');svg.setAttribute('preserveAspectRatio','none');
    svg.setAttribute('role','img');svg.setAttribute('aria-label',DN.map((d,i)=>d+' '+pct(values[i])).join(', '));
    let x=0;
    values.forEach((v,i)=>{
      if(!v)return;
      const r=rectangle(x,v*100,DC[i]), t=document.createElementNS(ns,'title');
      t.textContent=DN[i]+' '+pct(v);r.append(t);svg.append(r);x+=v*100;
    });
    row.append(svg);return row;
  }
  const key=document.getElementById('key');
  DN.forEach((d,i)=>{
    const label=document.createElement('span'),chip=document.createElementNS(ns,'svg');
    chip.setAttribute('aria-hidden','true');chip.setAttribute('width',10);chip.setAttribute('height',10);
    chip.append(rectangle(0,10,DC[i]));label.append(chip,d);key.append(label);
  });
  const roomsByForm = new Map();
  for(const letter of Object.keys(preferred)){
    const rooms=R.filter(row=>row.form===letter).sort((a,b)=>a.room.localeCompare(b.room,'en',{sensitivity:'base'}));
    roomsByForm.set(letter,{rooms,changes:formMean(rooms,'c'),codes:formMean(rooms,'k')});
  }
  function showRoom() {
    const form=formPicker.value,group=roomsByForm.get(form),r=group.rooms.find(x=>x.room===roomPicker.value);
    const placement=r.ch>=5?'This community helped shape the tree.':'This community was assigned after the tree was built.';
    document.getElementById('profile-heading').textContent='r/'+r.room+' in form '+form;
    document.getElementById('profile-description').textContent='r/'+r.room+' contributed '+r.ch+' selected changes and '+r.co+' coded concepts. '+placement+' The strips compare its profile with the average for the '+group.rooms.length+' communities in form '+form+'.';
    bars.replaceChildren(strip('Community changes',shares(r.c)),strip('Form '+form+' changes',group.changes),strip('Community codes',shares(r.k)),strip('Form '+form+' codes',group.codes));
    document.getElementById('repair-path').hidden=r.room!=='PlaceNL';
    document.getElementById('dutch-profile').hidden=r.room!=='PlaceNL';
    const account=document.getElementById('form-account');
    account.href='population-forms.html#form-'+form;
    account.textContent='Read the account of form '+form;
    const link=document.getElementById('row-link');
    const url=new URL('population-forms.html', document.baseURI);
    url.searchParams.set('room',r.room);url.hash='room-'+r.room.toLowerCase();
    link.href=url.href;link.textContent='Inspect r/'+r.room+' in the table of 705 communities';
  }
  function chooseForm(requestedRoom) {
    const letter=formPicker.value;
    const rooms=roomsByForm.get(letter).rooms;
    const selected=rooms.some(r=>r.room===requestedRoom)?requestedRoom:preferred[letter];
    roomPicker.replaceChildren(...rooms.map(r=>new Option('r/'+r.room,r.room,false,r.room===selected)));
    showRoom();
  }
  function rememberSelection() {
    const url=new URL(location.href);
    url.searchParams.set('form',formPicker.value);
    url.searchParams.set('room',roomPicker.value);
    history.replaceState(null,'',url);
  }
  function restoreSelection() {
    const params=new URLSearchParams(location.search);
    const form=params.get('form');
    formPicker.value=roomsByForm.has(form)?form:'B';
    chooseForm(params.get('room'));
  }
  // A reader can open a form in a new tab or move straight to its profile here.
  document.querySelector('.forms').addEventListener('click',event=>{
    const link=event.target.closest('a');
    if(!link || event.button!==0 || event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
    event.preventDefault();
    history.pushState(null,'',link.href);
    restoreSelection();
    document.getElementById('profile-tool').scrollIntoView();
    document.getElementById('profile-heading').focus({preventScroll:true});
  });
  window.addEventListener('popstate',restoreSelection);
  formPicker.addEventListener('change',()=>{chooseForm();rememberSelection()});
  roomPicker.addEventListener('change',()=>{showRoom();rememberSelection()});
  restoreSelection();
  document.getElementById('interactive-profile').hidden=false;
})();
