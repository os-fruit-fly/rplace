/* Render verified reading copies only. Keep the saved text available unchanged. */
async function renderSavedFigures() {
  const blocks = [...document.querySelectorAll('.record-copy pre.mermaid')];
  if (!blocks.length || !window.mermaid) return;
  window.mermaid.initialize({
    startOnLoad: false, securityLevel: 'strict', suppressErrorRendering: true,
    maxTextSize: 150000, maxEdges: 1000, htmlLabels: false,
    secure: ['secure', 'securityLevel', 'startOnLoad', 'maxTextSize', 'maxEdges',
      'suppressErrorRendering', 'htmlLabels', 'themeCSS', 'themeVariables', 'theme', 'flowchart', 'look'],
    theme: 'base', look: 'classic', fontFamily: 'Archivo, sans-serif',
    themeVariables: {fontFamily: 'Archivo, sans-serif', primaryColor: '#ffffff',
      primaryTextColor: '#0d0d0d', primaryBorderColor: '#0d0d0d', lineColor: '#0d0d0d',
      secondaryColor: '#f5f5f4', tertiaryColor: '#ffffff'},
    flowchart: {htmlLabels: false, useMaxWidth: false}
  });
  await document.fonts.ready;
  for (const [index, block] of blocks.entries()) {
    const source = block.textContent;
    // These saved figures need only flowcharts. Reject active content and external resources.
    if (!/^\s*(flowchart|graph)\s+(LR|RL|TD|TB|BT)\b/.test(source)
        || /%%\{|\bclick\s|\bhref\s|\burl\s*\(|@import|(?:https?|javascript|data|file):/i.test(source)) continue;
    try {
      const id = `saved-figure-${index + 1}`;
      const rendered = await window.mermaid.render(id, source);
      const parsed = new DOMParser().parseFromString(rendered.svg, 'image/svg+xml');
      const svg = parsed.documentElement;
      if (svg.localName !== 'svg' || parsed.querySelector('parsererror, script, foreignObject, image')) {
        throw new Error('Unsupported diagram content');
      }
      for (const element of svg.querySelectorAll('*')) {
        for (const attribute of element.attributes) {
          if (/^on/i.test(attribute.name)
              || (/href$/i.test(attribute.name) && !attribute.value.startsWith('#'))) {
            throw new Error('Unsupported diagram action');
          }
        }
      }
      const figure = document.createElement('figure');
      figure.className = 'saved-diagram';
      const viewport = document.createElement('div');
      viewport.className = 'saved-diagram-view';
      viewport.tabIndex = 0;
      viewport.setAttribute('role', 'region');
      viewport.setAttribute('aria-label', `Saved figure ${index + 1}, scroll to see the full drawing`);
      const drawing = document.importNode(svg, true);
      viewport.append(drawing);
      const controls = document.createElement('div');
      controls.className = 'saved-diagram-controls';
      const zoomIn = document.createElement('button');
      const zoomOut = document.createElement('button');
      const fit = document.createElement('button');
      [zoomIn, zoomOut, fit].forEach(button => {button.type = 'button';});
      zoomIn.textContent = 'Zoom in';
      zoomOut.textContent = 'Zoom out';
      fit.textContent = 'Fit';
      controls.append(zoomIn, zoomOut, fit);
      let zoom = 1;
      const sizeDrawing = () => {
        const style = getComputedStyle(viewport);
        const width = viewport.clientWidth - parseFloat(style.paddingLeft) - parseFloat(style.paddingRight);
        drawing.style.width = `${Math.max(1, width) * zoom}px`;
        drawing.style.height = 'auto';
        zoomOut.disabled = fit.disabled = zoom === 1;
        zoomIn.disabled = zoom === 16;
      };
      zoomIn.onclick = () => {zoom = Math.min(16, zoom * 2); sizeDrawing();};
      zoomOut.onclick = () => {zoom = Math.max(1, zoom / 2); sizeDrawing();};
      fit.onclick = () => {zoom = 1; sizeDrawing(); viewport.scrollTo(0, 0);};
      const caption = document.createElement('figcaption');
      caption.append('Drawing from the saved source. ');
      const download = document.createElement('a');
      const url = URL.createObjectURL(new Blob([rendered.svg], {type: 'image/svg+xml'}));
      download.href = url;
      download.download = `checkpoint-figure-${index + 1}.svg`;
      download.textContent = 'Download SVG';
      caption.append(download);
      figure.append(controls, viewport, caption);
      const details = document.createElement('details');
      const summary = document.createElement('summary');
      summary.textContent = 'Diagram source';
      details.append(summary);
      block.before(figure, details);
      details.append(block);
      sizeDrawing();
      const resize = new ResizeObserver(sizeDrawing);
      resize.observe(viewport);
      window.addEventListener('pagehide', () => {resize.disconnect(); URL.revokeObjectURL(url);}, {once: true});
    } catch (_) {
      // A failed drawing never hides or changes the saved source.
      block.dataset.figureStatus = 'source-only';
    }
  }
}
renderSavedFigures();
