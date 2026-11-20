// =========================================================
// Scripts compartidos · Portal Académico Prof. Fili — UV
// Todas las páginas cargan este archivo al final del <body>:
//   <script src="assets/site.js"></script>
// =========================================================

// Cambiar entre pestañas de código (MATLAB / Python)
function showTab(btn, paneId){
  const block = btn.closest('.code-block');
  block.querySelectorAll('.code-tabs button').forEach(b => {
    if(!b.classList.contains('copy')) b.classList.remove('active');
  });
  block.querySelectorAll('.code-pane').forEach(p => p.classList.remove('active'));
  btn.classList.add('active');
  block.querySelector('#' + paneId).classList.add('active');
}

// Copiar el código visible del bloque
function copyCode(btn){
  const pane = btn.closest('.code-block').querySelector('.code-pane.active code');
  if(!pane) return;
  navigator.clipboard.writeText(pane.innerText).then(() => {
    const prev = btn.textContent;
    btn.textContent = '¡copiado!';
    setTimeout(() => btn.textContent = prev, 1400);
  });
}

// Marcar en la barra superior la página actual
(function(){
  const here = location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.topnav a').forEach(a => {
    if(a.getAttribute('href') === here) a.classList.add('current');
  });
})();

// Resaltar en la barra lateral la semana visible
(function(){
  const links = document.querySelectorAll('.sidebar a[href^="#s"]');
  if(!links.length || !('IntersectionObserver' in window)) return;
  const map = {};
  links.forEach(a => {
    const id = a.getAttribute('href').slice(1);
    if(document.getElementById(id)) map[id] = a;
  });
  const obs = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if(e.isIntersecting){
        links.forEach(a => a.classList.remove('active'));
        const a = map[e.target.id];
        if(a) a.classList.add('active');
      }
    });
  }, { rootMargin: '-40% 0px -55% 0px' });
  document.querySelectorAll('section.week[id]').forEach(s => obs.observe(s));
})();
