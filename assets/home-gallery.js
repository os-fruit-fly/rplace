(() => {
  const gallery = document.querySelector('.home-gallery');
  if (!gallery) return;
  const scenes = [{"files":["assets/gallery/canvas-12.webp","assets/gallery/canvas-00.webp","assets/gallery/canvas-01.webp","assets/gallery/canvas-02.webp","assets/gallery/canvas-03.webp","assets/gallery/canvas-04.webp","assets/gallery/canvas-05.webp","assets/gallery/canvas-06.webp","assets/gallery/canvas-07.webp","assets/gallery/canvas-08.webp","assets/gallery/canvas-09.webp","assets/gallery/canvas-10.webp","assets/gallery/canvas-11.webp","assets/gallery/canvas-12.webp"],"dates":["2017-04-03T16:58:54Z","2017-03-31T16:55:00Z","2017-03-31T22:55:00Z","2017-04-01T04:55:00Z","2017-04-01T10:55:00Z","2017-04-01T16:55:00Z","2017-04-01T22:55:00Z","2017-04-02T04:55:00Z","2017-04-02T10:55:00Z","2017-04-02T16:55:00Z","2017-04-02T22:55:00Z","2017-04-03T04:55:00Z","2017-04-03T10:55:00Z","2017-04-03T16:58:54Z"],"durations":[2000,850,600,600,600,600,600,600,600,600,600,600,600,900]},{"src":"assets/gallery/armenia.webp","width":78,"height":78,"dates":["2017-04-03T16:58:54Z","2017-04-01T12:00:00Z","2017-04-01T20:30:00Z","2017-04-01T22:15:00Z","2017-04-02T00:30:00Z","2017-04-02T02:00:00Z","2017-04-02T06:17:00Z","2017-04-02T09:00:00Z","2017-04-02T11:00:00Z","2017-04-02T12:50:00Z","2017-04-02T13:30:00Z","2017-04-02T14:15:00Z","2017-04-02T15:00:00Z","2017-04-02T16:40:00Z"],"durations":[3000,1600,900,900,900,900,900,900,900,900,900,900,900,900]},{"src":"assets/gallery/osu.webp","width":113,"height":113,"dates":["2017-04-03T16:58:54Z","2017-04-01T16:00:00Z","2017-04-01T23:00:00Z","2017-04-02T01:00:00Z","2017-04-02T03:30:00Z","2017-04-02T04:12:00Z","2017-04-02T05:00:00Z","2017-04-02T07:00:00Z","2017-04-02T09:30:00Z","2017-04-02T11:30:00Z","2017-04-02T16:00:00Z","2017-04-02T18:30:00Z","2017-04-02T21:30:00Z","2017-04-03T02:00:00Z","2017-04-03T07:30:00Z"],"durations":[3000,1600,900,900,900,900,900,900,900,900,900,900,900,900,900]},{"src":"assets/gallery/europe.webp?v=dove","width":135,"height":135,"dates":["2017-04-03T16:58:54Z","2017-03-31T22:00:00Z","2017-04-01T08:00:00Z","2017-04-01T10:00:00Z","2017-04-01T11:30:00Z","2017-04-01T13:00:00Z","2017-04-01T14:00:00Z","2017-04-01T15:30:00Z","2017-04-01T17:00:00Z","2017-04-01T18:30:00Z","2017-04-01T20:00:00Z","2017-04-02T04:00:00Z","2017-04-02T08:00:00Z","2017-04-02T20:00:00Z","2017-04-03T04:00:00Z","2017-04-03T14:00:00Z","2017-04-03T14:20:00Z","2017-04-03T14:40:00Z","2017-04-03T15:40:00Z"],"durations":[3000,1600,900,900,900,900,900,900,900,900,900,900,900,900,900,900,900,900,900]}];
  const slides = Array.from(gallery.querySelectorAll('.gallery-slide'));
  const tabs = Array.from(gallery.querySelectorAll('[data-pick]'));
  const bar = gallery.querySelector('.playback');
  const play = bar.querySelector('.play');
  const seek = bar.querySelector('input');
  const stamp = bar.querySelector('output');
  const motion = matchMedia('(prefers-reduced-motion: reduce)');
  const utc = new Intl.DateTimeFormat('en-GB', {day:'numeric',month:'short',hour:'2-digit',minute:'2-digit',timeZone:'UTC'});
  let view = 0, frame = 0, sheet = null, ready = false, generation = 0;
  let playing = !motion.matches, inView = false, reading = false;
  let timer = null, due = 0, left = 0;

  function stopClock() {
    if (timer !== null) {
      clearTimeout(timer);
      timer = null;
      left = Math.max(0, due - performance.now());
    }
  }
  function syncClock() {
    const running = playing && ready && !reading && inView && !document.hidden;
    if (!running) { stopClock(); return; }
    if (timer !== null) return;
    due = performance.now() + left;
    timer = setTimeout(() => {
      timer = null;
      if (frame >= Number(seek.max)) select((view + 1) % slides.length);
      else draw(frame + 1);
    }, left);
  }
  function setPlaying(on) {
    playing = on;
    play.textContent = on ? 'Pause' : 'Play';
    play.setAttribute('aria-label', on ? 'Pause gallery playback' : 'Play gallery');
    syncClock();
  }
  let load = 0;
  const canvasImage = slides[0].querySelector('.whole-canvas');
  const cursor = slides[0].querySelector('.hour-cursor');
  function failed() {
    stamp.textContent = 'Replay unavailable. Open the record below.';
    setPlaying(false);
  }
  async function draw(index) {
    stopClock();
    frame = index;
    seek.value = String(index);
    const scene = scenes[view];
    const rev = ++load;
    const cell = index % scene.dates.length;
    ready = false;
    if (view === 0) {
      const file = scene.files[cell];
      const img = new Image();
      img.src = file;
      try { await img.decode(); }
      catch { if (rev === load) failed(); return; }
      if (rev !== load) return;
      canvasImage.src = file;
      const hours = (Date.parse(scene.dates[cell]) - Date.UTC(2017,2,31,16))/3600000;
      const x = String(Math.min(364,5*hours));
      cursor.setAttribute('x1',x); cursor.setAttribute('x2',x);
    } else {
      const ctx = slides[view].querySelector('canvas').getContext('2d');
      ctx.drawImage(sheet,(cell%4)*scene.width,Math.floor(cell/4)*scene.height,
        scene.width,scene.height,0,0,scene.width,scene.height);
    }
    const time = utc.format(new Date(scene.dates[cell])) + ' UTC';
    stamp.textContent = time;
    seek.setAttribute('aria-valuetext',time);
    left = scene.durations[index] ?? 900;
    ready = true;
    syncClock();
  }
  async function select(index) {
    stopClock();
    const revision = ++generation;
    ++load;
    ready = false; sheet = null; view = index; reading = false;
    slides.forEach((slide,i) => { slide.hidden = i !== index; });
    tabs.forEach((tab,i) => tab.setAttribute('aria-pressed',String(i===index)));
    seek.hidden = false;
    seek.disabled = true;
    const scene = scenes[index];
    seek.max = String(index === 0 ? scene.files.length-1 : scene.durations.length);
    seek.value = '0';
    if (scene.src) {
      const img = new Image();
      img.src = scene.src;
      stamp.textContent = 'Loading replay…';
      try { await img.decode(); }
      catch { if (revision === generation) failed(); return; }
      if (revision !== generation) return;
      sheet = img;
    }
    seek.disabled = false;
    draw(0);
  }
  tabs.forEach((tab,i) => tab.addEventListener('click', () => select(i)));
  play.addEventListener('click', () => setPlaying(!playing));
  seek.addEventListener('input', () => { setPlaying(false); draw(Number(seek.value)); });
  motion.addEventListener('change', () => setPlaying(!motion.matches));
  document.addEventListener('visibilitychange',syncClock);
  gallery.querySelectorAll('figcaption').forEach(caption => {
    function hold() { reading = caption.matches(':focus-within'); syncClock(); }
    caption.addEventListener('focusin',hold);
    caption.addEventListener('focusout',()=>requestAnimationFrame(hold));
  });
  let touch = null;
  gallery.addEventListener('touchstart',e => {
    if (!e.target.closest('.gallery-image') || e.touches.length!==1) { touch=null; return; }
    touch = [e.touches[0].clientX,e.touches[0].clientY];
  },{passive:true});
  gallery.addEventListener('touchcancel',()=>{touch=null;});
  gallery.addEventListener('touchend',e => {
    if (!touch) return;
    const dx=e.changedTouches[0].clientX-touch[0],dy=e.changedTouches[0].clientY-touch[1];
    touch = null;
    if (Math.abs(dx)>40 && Math.abs(dx)>Math.abs(dy)*1.5) {
      select((view+(dx<0?1:-1)+slides.length)%slides.length);
    }
  },{passive:true});
  new IntersectionObserver(([entry])=>{
    inView = entry.isIntersecting && entry.intersectionRatio>=.35; syncClock();
  },{threshold:[0,.35]}).observe(gallery);
  bar.hidden = false;
  gallery.querySelector('.gallery-tabs').hidden = false;
  setPlaying(playing);
  select(0);
})();
