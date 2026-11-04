/* Fit the complete drawing first. Zoom changes only its display size. */
for (const reader of document.querySelectorAll('.figure-reader')) {
  const view=reader.querySelector('.figure-window'), image=view.querySelector('img');
  const width=Number(reader.dataset.width),height=Number(reader.dataset.height);
  const controls=reader.querySelector('.figure-zoom'),output=controls.querySelector('output');
  let zoom=1,fitted=true;
  const fitScale=()=>Math.min(view.clientWidth/width,view.clientHeight/height);
  const draw=(next,fit=false)=>{
    const oldWidth=image.getBoundingClientRect().width||width;
    const cx=(view.scrollLeft+view.clientWidth/2)/oldWidth;
    const cy=(view.scrollTop+view.clientHeight/2)/(oldWidth*height/width);
    zoom=Math.max(.08,Math.min(8,next));fitted=fit;
    view.style.height=fit?'':'min(65vh, 680px)';
    image.style.width=width*zoom+'px';image.style.height=height*zoom+'px';
    if(fit){view.scrollLeft=0;view.scrollTop=0;}else{view.scrollLeft=cx*width*zoom-view.clientWidth/2;view.scrollTop=cy*height*zoom-view.clientHeight/2;}
    output.textContent=Math.round(zoom*100)+'%';
    controls.querySelector('[data-figure="out"]').disabled=zoom<=.08;
    controls.querySelector('[data-figure="in"]').disabled=zoom>=8;
  };
  const fit=()=>{view.style.height='';draw(fitScale(),true)};
  reader.classList.add('figure-ready');controls.hidden=false;
  controls.addEventListener('click',event=>{
    const action=event.target.dataset.figure;
    if(action==='fit')fit();
    if(action==='read'){draw(Math.max(fitScale(),2.2));view.scrollLeft=0;view.scrollTop=0;}
    if(action==='out')draw(zoom/1.5);
    if(action==='in')draw(zoom*1.5);
  });
  fit();
  const observer=new ResizeObserver(()=>{if(fitted)fit()});observer.observe(view);
  window.addEventListener('pagehide',()=>observer.disconnect(),{once:true});
}
