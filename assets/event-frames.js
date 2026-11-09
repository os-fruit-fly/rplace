/* With scripts disabled, every dated frame remains visible in reading order. */
for (const player of document.querySelectorAll('.event-player')) {
  const frames = Array.from(player.querySelectorAll('.event-frame'));
  const controls = player.querySelector('.frame-controls');
  const input = controls.querySelector('input');
  const position = controls.querySelector('.frame-position');
  const previous = controls.querySelector('[data-step="-1"]');
  const next = controls.querySelector('[data-step="1"]');
  const toggle = document.createElement('button');
  toggle.type = 'button';
  controls.prepend(toggle);
  const motion = window.matchMedia('(prefers-reduced-motion: reduce)');
  let playing = !motion.matches;
  let current = playing ? frames.length - 1 : 0;
  let generation = 0;
  let timer;

  function schedule() {
    clearTimeout(timer);
    const version = ++generation;
    if (!playing || document.hidden) return;
    const image = frames[current].querySelector('img');
    image.loading = 'eager';
    image.decode().then(() => {
      if (generation !== version) return;
      const hold = current === frames.length - 1 ? 3000 : current === 0 ? 1600 : 900;
      timer = setTimeout(() => show((current + 1) % frames.length), hold);
    }).catch(() => {
      if (generation === version) setPlaying(false);
    });
  }

  function show(index) {
    current = Math.max(0, Math.min(frames.length - 1, index));
    frames.forEach((frame, i) => { frame.hidden = i !== current; });
    input.value = String(current + 1);
    position.textContent = 'Frame ' + (current + 1) + ' of ' + frames.length;
    input.setAttribute('aria-valuetext', position.textContent + ', ' + frames[current].querySelector('time').textContent);
    previous.disabled = current === 0;
    next.disabled = current === frames.length - 1;
    schedule();
  }

  function setPlaying(on) {
    playing = on;
    toggle.textContent = on ? 'Pause' : 'Play';
    toggle.setAttribute('aria-label', on ? 'Pause replay' : 'Play replay');
    position.setAttribute('aria-live', on ? 'off' : 'polite');
    schedule();
  }

  function selectFrame(index) {
    setPlaying(false);
    show(index);
  }

  function showLinkedFrame() {
    const index = frames.findIndex(frame => '#' + frame.id === location.hash);
    if (index < 0) return;
    selectFrame(index);
    player.scrollIntoView({ block: 'start' });
  }

  toggle.addEventListener('click', () => setPlaying(!playing));
  input.addEventListener('input', () => selectFrame(Number(input.value) - 1));
  for (const button of [previous, next]) {
    button.addEventListener('click', () => selectFrame(current + Number(button.dataset.step)));
  }
  for (const link of document.querySelectorAll('a[href^="#frame-"]')) {
    link.addEventListener('click', () => {
      if (location.hash === link.hash) requestAnimationFrame(showLinkedFrame);
    });
  }
  motion.addEventListener('change', () => setPlaying(!motion.matches));
  document.addEventListener('visibilitychange', schedule);
  controls.hidden = false;
  setPlaying(playing);
  show(current);
  showLinkedFrame();
  window.addEventListener('hashchange', showLinkedFrame);
}
