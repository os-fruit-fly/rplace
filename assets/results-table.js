// One table: the mean room of each form on top, then every room, in the same columns (the kit's room table).
// Counts: the mean over every room of the form. Bars: the mean of the rooms' own shares (each room normalized first;
// rooms with no changes, or no codes, are left out of that bar).
const sum=a=>a.reduce((x,y)=>x+y,0);
function mean(rows){const m={n:rows.length,ch:sum(rows.map(x=>x.ch))/rows.length,co:sum(rows.map(x=>x.co))/rows.length,c:Array(8).fill(0),k:Array(8).fill(0),nc:0,nk:0};
  rows.forEach(x=>{const sc=sum(x.c),sk=sum(x.k);if(sc>0){m.nc++;x.c.forEach((v,i)=>m.c[i]+=v/sc)}if(sk>0){m.nk++;x.k.forEach((v,i)=>m.k[i]+=v/sk)}});
  m.c=m.c.map(v=>v/m.nc);m.k=m.k.map(v=>v/m.nk);return m}
const AVG={};'ABCDEF'.split('').forEach(f=>AVG[f]=mean(R.filter(x=>x.form==f)));AVG.all=mean(R);
const esc=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
function strip(v,note){const s=sum(v);if(!s)return '<div class="bar"></div>';
  return '<div class="bar" title="'+(note||'')+DN.map((d,i)=>d+': '+(100*v[i]/s).toFixed(0)+'%').join(', ')+'">'+v.map((x,i)=>'<span style="width:'+(100*x/s)+'%;background:'+DC[i]+'"></span>').join('')+'</div>'}
function avgRow(f){const m=AVG[f],lab=f=='all'?'Mean, all communities':'Mean, form '+f,tip=f=='all'?'':' title="'+esc(NAME[f])+'"';
  return '<tr class="avg'+(f=='all'?' all':'')+'"><th scope="row" class="stick"'+tip+'>'+lab+'</th><td>'+(f=='all'?'':'<span class="chip" style="background:'+FC[f]+'"></span>'+f)+'</td><td class="hide role">'+m.n+' communities</td>'+
    '<td class="n">'+m.ch.toFixed(1)+'</td><td>'+strip(m.c,'Mean of '+m.nc+' communities’ shares. ')+'</td><td class="n">'+Math.round(m.co).toLocaleString('en')+'</td><td>'+strip(m.k,'Mean of '+m.nk+' communities’ shares. ')+'</td><td class="hide"></td><td class="hide"></td></tr>'}
let key='form',dir=1;
function drawTable(){const f=document.getElementById('rt-f').value,r=document.getElementById('rt-r').value,q=document.getElementById('rt-q').value.toLowerCase();
  document.getElementById('rt-avg').innerHTML=(f?[f,'all']:['A','B','C','D','E','F','all']).map(avgRow).join('');
  const rows=R.filter(x=>(!f||x.form==f)&&(!r||x.role==r)&&(!q||x.room.toLowerCase().includes(q))).sort((a,b)=>{const A=a[key],B=b[key];return (A>B?1:A<B?-1:a.room.localeCompare(b.room))*dir});
  document.getElementById('rt-cnt').textContent=rows.length+' communities';
  document.getElementById('rt-tb').innerHTML=rows.map(x=>'<tr id="room-'+esc(x.room.toLowerCase())+'"><th scope="row" class="stick">'+(x.room==='PlaceNL'?'<a href="placenl.html">PlaceNL</a>':esc(x.room))+'</th><td><span class="chip" style="background:'+FC[x.form]+'"></span>'+x.form+'</td><td class="role hide">'+x.role+'</td>'+
    '<td class="n">'+x.ch+'</td><td>'+strip(x.c)+'</td><td class="n">'+x.co.toLocaleString('en')+'</td><td>'+strip(x.k)+'</td><td class="hide addr">'+esc(x.addr)+'</td><td class="hide">'+esc(x.beside)+'</td></tr>').join('')}
document.querySelectorAll('#rooms th[data-k]').forEach(th=>th.onclick=()=>{const k=th.dataset.k;dir=(key==k)?-dir:(k=='ch'||k=='co'?-1:1);key=k;draw()});
['rt-f','rt-r','rt-q'].forEach(id=>document.getElementById(id).oninput=draw);draw();

// Navigation and accessibility only. The imported values and mean() are unchanged.
function draw(){
  drawTable();
  const count=document.getElementById('rt-cnt'); count.setAttribute('role','status'); if(count.textContent==='1 communities')count.textContent='1 community';
  const rows=document.querySelectorAll('#rt-tb tr');
  if(!rows.length)document.getElementById('rt-tb').innerHTML='<tr><td colspan="9">No communities match. Clear the search or change the filters.</td></tr>';
  document.querySelectorAll('#rooms th[data-k]').forEach(th=>th.setAttribute('aria-sort',th.dataset.k===key?(dir===1?'ascending':'descending'):'none'));
  document.querySelectorAll('#rooms .bar[title]').forEach(bar=>{bar.setAttribute('role','img');bar.setAttribute('aria-label',bar.title)});
}
const queryRoom=new URLSearchParams(location.search).get('room');
const hashRoom=location.hash.startsWith('#room-')?decodeURIComponent(location.hash.slice(6)):null;
const chosen=R.find(x=>x.room.toLowerCase()===(queryRoom||hashRoom||'').toLowerCase());
if(chosen){document.getElementById('rt-q').value=chosen.room;draw();requestAnimationFrame(()=>{const row=document.getElementById('room-'+chosen.room.toLowerCase());if(row){row.classList.add('selected-room');row.scrollIntoView({block:'center'});}});}
