(() => {
  const box = document.querySelector('[data-file-register]');
  if (!box) return;
  const input = box.querySelector('input');
  const status = box.querySelector('[role="status"]');
  const list = box.querySelector('ul');
  let request;
  async function searchFiles() {
    const query = input.value.trim().toLowerCase();
    list.replaceChildren();
    status.textContent = '';
    if (!query) return;
    try {
      if (!request) {
        request = fetch(box.dataset.fileRegister).then(response => {
          if (!response.ok) throw Error('Missing register');
          return response.json();
        }).then(data => {
          const files = new Map();
          for (const group of data.groups) {
            for (const output of group.outputs) {
              for (const file of output.members) files.set(file.path, file);
            }
          }
          return [...files.values()];
        });
      }
      const files = await request;
      if (query !== input.value.trim().toLowerCase()) return;
      const matches = files.filter(file => file.path.toLowerCase().includes(query));
      status.textContent = matches.length === 0 ? 'No matching filenames.' :
        matches.length > 30 ? matches.length + ' matches. Showing the first 30. Type more to narrow the list.' :
        matches.length + (matches.length === 1 ? ' matching file.' : ' matching files.');
      for (const file of matches.slice(0, 30)) {
        const li = document.createElement('li');
        const path = document.createElement('code');
        path.textContent = file.path;
        li.append(path, ' · ');
        const link = document.createElement('a');
        link.href = file.reading_url || '#archive-download';
        link.textContent = file.reading_url ? 'Open reading copy' : 'Original archive';
        li.append(link);
        list.append(li);
      }
    } catch {
      request = undefined;
      status.textContent = 'The search could not load. You can browse the file groups below.';
    }
  }
  box.hidden = false;
  input.addEventListener('input', searchFiles);
})();
