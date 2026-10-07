document.querySelectorAll('[data-action]').forEach(button=>button.addEventListener('click',()=>{document.querySelectorAll('.article-detail').forEach(d=>d.open=button.dataset.action==='expand')}));
function openHash(){const target=document.getElementById(location.hash.slice(1));if(target){const d=target.querySelector('.article-detail');if(d)d.open=true;document.querySelectorAll('.toc a').forEach(a=>a.classList.toggle('current',a.hash===location.hash));}}
window.addEventListener('hashchange',openHash);openHash();
document.querySelectorAll('.toc a').forEach(a=>a.addEventListener('click',()=>{const target=document.getElementById(a.hash.slice(1));if(target){const d=target.querySelector('.article-detail');if(d)d.open=true}}));
window.addEventListener('beforeprint',()=>{document.querySelectorAll('.article-detail').forEach(d=>{d.dataset.beforePrint=d.open;d.open=true})});
window.addEventListener('afterprint',()=>{document.querySelectorAll('.article-detail').forEach(d=>d.open=d.dataset.beforePrint==='true')});
