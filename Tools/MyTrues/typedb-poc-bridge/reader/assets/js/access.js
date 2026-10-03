document.addEventListener('DOMContentLoaded',async()=>{
 const {d,locale}=await MyTruesI18n.load('access');MyTruesI18n.apply(d);document.documentElement.lang=locale;
 const p=new URLSearchParams(location.search);if(p.get('status'))document.getElementById('access-status').textContent=d.unavailable;
 const lang=document.getElementById('lang');if(lang){lang.textContent=locale==='pt-BR'?'EN':'PT';lang.onclick=()=>MyTruesI18n.setLocale(locale==='pt-BR'?'en':'pt-BR')}
});