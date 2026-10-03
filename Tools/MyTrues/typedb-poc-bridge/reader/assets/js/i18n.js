(()=>{
const normalize=v=>String(v||'').toLowerCase().startsWith('pt')?'pt-BR':'en';
const getLocale=()=>normalize(localStorage.getItem('mytrues.locale')||navigator.language||'pt-BR');
const get=(obj,path,fallback='')=>path.split('.').reduce((a,k)=>a&&a[k]!==undefined?a[k]:undefined,obj)??fallback;
async function load(surface){
 const locale=getLocale();
 const [common,specific]=await Promise.all([
  fetch('/i18n/'+locale+'/common.json',{cache:'no-store'}).then(r=>r.json()),
  fetch('/i18n/'+locale+'/'+surface+'.json',{cache:'no-store'}).then(r=>r.json())
 ]);
 return {locale,d:{...common,...specific}};
}
function apply(d){
 document.querySelectorAll('[data-i18n]').forEach(el=>{const v=get(d,el.dataset.i18n);if(v)el.textContent=v});
 document.querySelectorAll('[data-i18n-placeholder]').forEach(el=>{const v=get(d,el.dataset.i18nPlaceholder);if(v)el.placeholder=v});
 document.querySelectorAll('[data-i18n-aria]').forEach(el=>{const v=get(d,el.dataset.i18nAria);if(v)el.setAttribute('aria-label',v)});
}
function setLocale(locale){localStorage.setItem('mytrues.locale',normalize(locale));location.reload()}
window.MyTruesI18n={load,apply,setLocale,get,getLocale};
})();