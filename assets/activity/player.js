(() => {
  const figure = document.querySelector('[data-hourly-map]');
  if (!figure) return;
  const kind = figure.dataset.hourlyMap;
  const canvas = figure.querySelector('canvas');
  const poster = figure.querySelector('img');
  const context = canvas.getContext('2d');
  if (!context) return;
  const controls = figure.querySelector('.map-controls');
  const play = controls.querySelector('button');
  const slider = controls.querySelector('input');
  const stamp = figure.querySelector('.map-time');
  const value = figure.querySelector('.map-value');
  const marker = document.querySelector('#selected-hour');
  const hourTotals = document.querySelector('#hour-totals');
  const reduced = matchMedia('(prefers-reduced-motion: reduce)');
  const number = new Intl.NumberFormat('en-US');
  const utc = new Intl.DateTimeFormat('en-GB', {
    timeZone: 'UTC', month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit'
  });
  const sheet = new Image();
  sheet.src = 'assets/activity/' + kind + '.webp';
  let playing = !reduced.matches;
  let hour = Number(slider.value);
  let preview = true;
  let timer;
  let series;
  function draw() {
    const entry = series[hour];
    context.drawImage(sheet, hour % 4 * 200, Math.floor(hour / 4) * 200, 200, 200, 0, 0, 200, 200);
    const when = utc.format(new Date(entry.start_utc)) + ' UTC';
    stamp.textContent = 'Hour ' + hour + ' · ' + when;
    slider.value = String(hour);
    slider.setAttribute('aria-valuetext', stamp.textContent);
    value.textContent = kind === 'placements' ? number.format(entry.placements) + ' placements' :
      (100 * entry.repaints / entry.placements).toFixed(1) + '% repaints';
    if (marker) {
      marker.setAttribute('x', String(54 + 8 * hour));
      hourTotals.textContent = 'Hour ' + hour + ' had ' + number.format(entry.first_placements) +
        ' first placements, ' + number.format(entry.changed_color) + ' color changes and ' +
        number.format(entry.repaints) + ' repaints.';
    }
  }
  function schedule() {
    clearTimeout(timer);
    play.textContent = playing ? 'Pause' : 'Play';
    play.setAttribute('aria-label', playing ? 'Pause the hourly map' : 'Play the hourly map');
    if (!playing || document.hidden) return;
    timer = setTimeout(() => {
      hour = preview ? 0 : (hour + 1) % series.length;
      preview = false;
      draw();
      schedule();
    }, preview || hour === 72 ? 2000 : 550);
  }
  async function start() {
    const [response] = await Promise.all([fetch('assets/activity/hourly.csv'), sheet.decode()]);
    if (!response.ok) throw new Error('hourly counts unavailable');
    const rows = (await response.text()).trim().split(/\r?\n/);
    const names = rows.shift().split(',');
    series = rows.map(row => Object.fromEntries(row.split(',').map((v, i) => [names[i], v])));
    if (series.length !== 73 || sheet.naturalWidth !== 800 || sheet.naturalHeight !== 3800) return;
    draw();
    canvas.hidden = false;
    poster.hidden = true;
    controls.hidden = false;
    if (marker) marker.removeAttribute('visibility');
    play.addEventListener('click', () => {
      playing = !playing;
      schedule();
    });
    slider.addEventListener('input', () => {
      playing = preview = false;
      hour = Number(slider.value);
      draw();
      schedule();
    });
    document.addEventListener('visibilitychange', schedule);
    reduced.addEventListener('change', () => {
      playing = !reduced.matches;
      schedule();
    });
    schedule();
  }
  start().catch(() => {
    controls.hidden = true;
  });
})();
