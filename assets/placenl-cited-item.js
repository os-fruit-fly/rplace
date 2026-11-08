// A post can support several codes. Show all of its published passages together.
(() => {
  const idPattern = /^#item-([a-z0-9]+)$/;
  const panel = document.createElement('section');
  panel.hidden = true;
  panel.setAttribute('aria-label','Cited passages');
  const title = document.querySelector('main h1');
  if (!title) return;
  title.after(panel);
  function showItem() {
    panel.hidden = true;
    panel.replaceChildren();
    const match = idPattern.exec(location.hash);
    if (!match) return;
    const item = match[1];
    const citations = [...document.querySelectorAll('.cid[id^="code-"]')]
      .filter(el => el.textContent.trim().split(/\s*·\s*/).at(-1) === item);
    if (!citations.length) return;
    const heading = document.createElement('h2');
    heading.textContent = 'Coded passages from Reddit item '+item;
    heading.tabIndex = -1;
    const list = document.createElement('ul');
    for (const citation of citations) {
      const row = citation.closest('li');
      const li = document.createElement('li'), link = document.createElement('a');
      link.href = '#'+citation.id;
      link.textContent = citation.textContent.split('·')[0].trim()+' · '+row.querySelector('.fo').textContent;
      li.append(link);
      const quote = row.querySelector('q'),translation=row.querySelector('.en');
      if (quote) {const p=document.createElement('p');p.append(quote.cloneNode(true));if(translation)p.append(' ',translation.cloneNode(true));li.append(p);}
      list.append(li);
    }
    panel.append(heading,list);panel.hidden=false;
    heading.focus({preventScroll:true});panel.scrollIntoView();
  }
  window.addEventListener('hashchange',showItem);
  showItem();
})();
