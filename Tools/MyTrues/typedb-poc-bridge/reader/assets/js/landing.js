document.addEventListener('DOMContentLoaded',async()=>{
 const {d,locale}=await MyTruesI18n.load('landing');MyTruesI18n.apply(d);
 document.documentElement.lang=locale;document.title=d.meta_title||'MyTrues';
 const lang=document.getElementById('lang');if(lang){lang.textContent=locale==='pt-BR'?'EN':'PT';lang.onclick=()=>MyTruesI18n.setLocale(locale==='pt-BR'?'en':'pt-BR')}
 const form=document.getElementById('interest-form'),button=document.getElementById('submit'),message=document.getElementById('message');
 form?.addEventListener('submit',async e=>{
  e.preventDefault();message.textContent='';button.disabled=true;button.textContent=d.sending;
  try{
   const payload={display_name:document.getElementById('name').value.trim(),email:document.getElementById('email').value.trim(),website:document.getElementById('website').value};
   const r=await fetch('/api/interest',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(payload)});
   const data=await r.json().catch(()=>({}));if(!r.ok)throw new Error(data.detail||d.error_generic);
   form.reset();message.textContent=d.success;
  }catch(err){message.textContent=err.message||d.error_generic}
  finally{button.disabled=false;button.textContent=d.submit}
 });
 document.getElementById('year').textContent=new Date().getFullYear();
});