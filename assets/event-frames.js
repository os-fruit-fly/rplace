/* Without scripts, the complete canvas sequence remains in reading order. */
for (const player of document.querySelectorAll('.event-player')) {
  const frames = Array.from(player.querySelectorAll('.event-frame'));
  const controls = player.querySelector('.frame-controls');
  const input = controls.querySelector('input');
  const position = controls.querySelector('.frame-position');
  const buttons = controls.querySelectorAll('button');
  let current = 0;

  function show(index) {
    current = Math.max(0, Math.min(frames.length - 1, index));
    frames.forEach((frame, i) => { frame.hidden = i !== current; });
    input.value = String(current + 1);
    position.textContent = 'Frame ' + (current + 1) + ' of ' + frames.length;
    input.setAttribute('aria-valuetext', position.textContent + ', ' + frames[current].querySelector('time').textContent);
    buttons[0].disabled = current === 0;
    buttons[1].disabled = current === frames.length - 1;
  }
  function showLinkedFrame() {
    const index = frames.findIndex(frame => '#' + frame.id === location.hash);
    if (index < 0) return;
    show(index);
    player.scrollIntoView({block:'start'});
  }
  input.addEventListener('input', () => show(Number(input.value) - 1));
  for (const button of buttons) button.addEventListener('click', () => show(current + Number(button.dataset.step)));
  for (const link of document.querySelectorAll('a[href^="#frame-"]')) {
    link.addEventListener('click', () => {
      const index = frames.findIndex(frame => '#' + frame.id === link.hash);
      if (index >= 0) show(index);
      if (location.hash === link.hash) requestAnimationFrame(showLinkedFrame);
    });
  }
  show(0);
  controls.hidden = false;
  showLinkedFrame();
  window.addEventListener('hashchange', showLinkedFrame);
}
