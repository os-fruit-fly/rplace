(() => {
  function openStage() {
    const stage = document.getElementById(location.hash.slice(1));
    if (stage && stage.classList.contains('stage-def')) {
      const link = stage.querySelector('h4 a');
      if (link) location.replace(link.href);
    }
  }
  openStage();
  window.addEventListener('hashchange', openStage);
})();
